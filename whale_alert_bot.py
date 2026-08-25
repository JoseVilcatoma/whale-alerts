"""
whale_alert_bot.py — versión "en vivo" (websocket), enfocada 100% en velocidad

Se conecta al chorro en vivo de TODAS las apuestas de Polymarket y avisa al
instante apenas alguno de los vigilados (top del ranking, semana + mes
combinados, con un mínimo de 7 días de permanencia) hace una apuesta fuerte.

Además lleva un registro de resultados (results.json / results.md) marcando
ganó/perdió apenas cada mercado resuelve, para saber a quién le conviene
seguir de verdad.

Variables de entorno (se configuran en el workflow / como Secrets):
  TELEGRAM_BOT_TOKEN            - token de tu bot de Telegram (obligatorio)
  TELEGRAM_CHAT_ID              - chat_id adonde mandar los mensajes (obligatorio)
  WHALE_THRESHOLD              - monto mínimo en USD para avisar (default: 1000)
  TOP_N                        - a cuántos de CADA período vigilar (default: 20)
  LB_CATEGORY                  - OVERALL, SPORTS, POLITICS, CRYPTO, ESPORTS,
                                  CULTURE, ECONOMICS (default: OVERALL)
  LEADERBOARD_REFRESH_SECONDS  - cada cuánto refresca la lista de vigilados
                                  (default: 900)
  MIN_WATCH_DAYS               - mínimo de días que se sigue vigilando a
                                  alguien aunque salga del top (default: 7)
  MAX_RUNTIME_SECONDS          - cuándo cortar solo, antes que lo corte GitHub
                                  (default: 21000 = 5h50m)
"""

import json
import os
import socket
import sys
import threading
import time
import re as _re_mod
from datetime import datetime, timezone
from pathlib import Path

import requests
import websocket
import urllib3.util.connection as urllib3_cn

# --- Arreglo para "Network is unreachable" en GitHub Actions ---
def _allowed_gai_family():
    return socket.AF_INET

urllib3_cn.allowed_gai_family = _allowed_gai_family

DATA_API = "https://data-api.polymarket.com"
GAMMA_API = "https://gamma-api.polymarket.com"
RTDS_URL = "wss://ws-live-data.polymarket.com"
RESULTS_FILE = Path(__file__).parent / "results.json"
SUMMARY_FILE = Path(__file__).parent / "results.md"
WATCHED_FILE = Path(__file__).parent / "watched.json"

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
WHALE_THRESHOLD = float(os.environ.get("WHALE_THRESHOLD", "1000"))
PUBLICAR_RESULTADOS = os.environ.get("PUBLICAR_RESULTADOS", "1") not in ("0", "false", "no")
MAX_DIAS_RESOLUCION = float(os.environ.get("MAX_DIAS_RESOLUCION", "2"))
BACKUP_INTERVAL = float(os.environ.get("BACKUP_INTERVAL", "300"))
MUDO_SEGUNDOS = float(os.environ.get("MUDO_SEGUNDOS", "25"))
# Si una ballena vende algo que NO le habíamos alertado, ¿avisar igual?
# Por defecto no, para no llenar el canal de salidas sin contexto.
PUBLICAR_VENTAS = os.environ.get("PUBLICAR_VENTAS", "0") not in ("0", "false", "no")
# Solo deportes y esports (fútbol, MLB, NBA, NFL, Dota, CS2, LoL, Valorant,
# tenis, UFC...). Poner "0" para dejar entrar también política, cripto, etc.
SOLO_DEPORTES = os.environ.get("SOLO_DEPORTES", "1") not in ("0", "false", "no")
# Si en una misma ronda se resuelven más de N apuestas, se manda un resumen
# agrupado en vez de un mensaje por cada una (evita el bombardeo tras reiniciar).
# Ventana para fusionar los pedazos ("fills") de una misma orden grande.
# Polymarket parte las órdenes: sin esto, una decisión cuenta 4-5 veces.
FILL_MERGE_WINDOW = float(os.environ.get("FILL_MERGE_WINDOW", "120"))
# No alertar operaciones más viejas que esto (en minutos). Protege sobre todo
# al respaldo por API, que trae historial y podría avisar de partidos ya jugados.
MAX_EDAD_MINUTOS = float(os.environ.get("MAX_EDAD_MINUTOS", "20"))
# Ignorar apuestas a resultados ya casi definidos: a 95¢ (cuota 1.05) no se
# está prediciendo nada, se recoge el último centavo, y eso infla el % de
# acierto sin decir nada de la habilidad del apostador.
PRECIO_MAX = float(os.environ.get("PRECIO_MAX", "95"))   # en centavos
PRECIO_MIN = float(os.environ.get("PRECIO_MIN", "3"))    # el extremo opuesto
TOP_N = int(os.environ.get("TOP_N", "20"))
LB_CATEGORY = os.environ.get("LB_CATEGORY", "OVERALL")

# Ballenas que NO queremos seguir. Se ponen nombres o wallets separados por
# coma en la variable EXCLUIDOS del workflow. Comparamos por las dos cosas
# porque el nombre se puede cambiar en Polymarket, la wallet no.
EXCLUIDOS = {e.strip().lower() for e in os.environ.get("EXCLUIDOS", "").split(",") if e.strip()}


def esta_excluido(username, wallet):
    if not EXCLUIDOS:
        return False
    return ((username or "").lower() in EXCLUIDOS
            or (wallet or "").lower() in EXCLUIDOS)

LB_PERIODS = ["WEEK", "MONTH"]

LEADERBOARD_REFRESH_SECONDS = int(os.environ.get("LEADERBOARD_REFRESH_SECONDS", "900"))
MIN_WATCH_DAYS = float(os.environ.get("MIN_WATCH_DAYS", "7"))
MAX_RUNTIME_SECONDS = int(os.environ.get("MAX_RUNTIME_SECONDS", str(5 * 3600 + 50 * 60)))

watched = {}           # wallet (minúsculas) -> username
watched_meta = {}      # wallet -> {"username":..., "added_at": ts} — para el mínimo de 7 días
msg_count = 0
last_msg_at = time.time()
current_ws = None
raw_samples_shown = 0
seen_keys = set()      # dedupe de trades ya alertados en esta corrida
lock = threading.Lock()
run_start = time.time()
stop_flag = threading.Event()

results = []            # cada apuesta que alertamos: {..., "status": "pending"/"won"/"lost"}
results_dirty = False
_market_cache = {}


def load_json(path):
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            return None
    return None


def get_market(slug, max_age=180):
    """Trae los datos de un mercado.
    Si ya CERRÓ, el dato no cambia más y se cachea para siempre.
    Si sigue ABIERTO, se vuelve a consultar cada max_age segundos en vez de
    quedarse pegado con la primera respuesta — si no, el bot no se entera
    nunca de que el partido terminó y las resoluciones se acumulan hasta
    el próximo reinicio."""
    if not slug:
        return None
    guardado = _market_cache.get(slug)
    if guardado:
        m, cuando = guardado
        if m and m.get("closed"):
            return m
        if time.time() - cuando < max_age:
            return m
    try:
        r = requests.get(f"{GAMMA_API}/markets/slug/{slug}",
                         params={"include_tag": "true"}, timeout=8)
        m = r.json() if r.ok else None
    except Exception:
        m = None
    _market_cache[slug] = (m, time.time())
    return m


SPORT_KEYWORDS = [
    r"\bvs\.?\b", r"\bnba\b", r"\bnfl\b", r"\bmlb\b", r"\bnhl\b", r"\bwnba\b",
    r"\bsoccer\b", r"\bf[úu]tbol\b", r"\bdota\b", r"\bcs2\b", r"\bcsgo\b",
    r"\bcounter-?strike\b", r"\bleague of legends\b", r"\blol\b", r"\bvalorant\b",
    r"\besports?\b", r"\be-sports\b", r"\btennis\b", r"\batp\b", r"\bwta\b",
    r"\bufc\b", r"\bmma\b", r"\bboxing\b", r"\bcricket\b", r"\bgolf\b",
    r"\bpremier league\b", r"\bla liga\b", r"\bserie a\b", r"\bbundesliga\b",
    r"\bligue 1\b", r"\bmls\b", r"\bchampions league\b", r"\blibertadores\b",
    r"\bsudamericana\b", r"\bbaseball\b", r"\bbasketball\b", r"\bhockey\b",
]


def es_deporte(market):
    """¿Es un mercado de deportes o esports? Polymarket marca internamente
    los deportivos con el campo 'sports', que es la vía más confiable: sirve
    para cualquier liga y en cualquier idioma. Las etiquetas y las palabras
    clave quedan como respaldo."""
    if not market:
        return False
    if market.get("sports"):
        return True
    for t in (market.get("tags") or []):
        etiqueta = (t.get("label") or t.get("slug") or "") if isinstance(t, dict) else str(t)
        etiqueta = etiqueta.lower()
        if etiqueta in ("sports", "esports", "e-sports"):
            return True
        if any(_re_mod.search(k, etiqueta) for k in SPORT_KEYWORDS):
            return True
    texto = f"{market.get('title','')} {market.get('slug','')}".lower()
    return any(_re_mod.search(k, texto) for k in SPORT_KEYWORDS)


def _norm(s):
    """Normaliza un nombre para comparar: minúsculas, sin acentos ni signos."""
    import unicodedata
    s = unicodedata.normalize("NFKD", (s or "")).encode("ascii", "ignore").decode()
    return " ".join(_re_mod.sub(r"[^a-z0-9 ]", " ", s.lower()).split())


def _buscar_outcome(outcomes, outcome):
    """Encuentra el índice del resultado. Prueba coincidencia exacta y, si no,
    formas más flexibles: uno contenido en el otro, o apellido en común.
    Polymarket a veces nombra distinto al mismo jugador ('Hemery' vs
    'Calvin Hemery'), y con comparación exacta la apuesta quedaba pendiente
    para siempre."""
    objetivo = _norm(outcome)
    norm = [_norm(o) for o in outcomes]
    if objetivo in norm:
        return norm.index(objetivo)
    for i, o in enumerate(norm):
        if o and objetivo and (o in objetivo or objetivo in o):
            return i
    # último recurso: coincidencia por apellido / palabra significativa
    pal = {p for p in objetivo.split() if len(p) > 3}
    for i, o in enumerate(norm):
        if pal & {p for p in o.split() if len(p) > 3}:
            return i
    return -1


def market_result(market, outcome):
    """'won' / 'lost' / 'open' / 'anulada' / None."""
    if not market:
        return None
    if not market.get("closed"):
        return "open"
    try:
        outcomes = json.loads(market["outcomes"])
        prices = [float(p) for p in json.loads(market["outcomePrices"])]
    except Exception:
        return None

    idx = _buscar_outcome(outcomes, outcome)
    if idx == -1:
        print(f"  ⚠ no encontré '{outcome}' entre {outcomes} (precios {prices})",
              file=sys.stderr)
        return None

    p = prices[idx]
    if p >= 0.99:
        return "won"
    if p <= 0.01:
        return "lost"

    # El mercado cerró pero el precio no es 0 ni 1. Si hay un ganador claro
    # (alguna opción muy arriba), decidimos por ahí.
    mayor = max(prices)
    if mayor >= 0.9:
        return "won" if prices.index(mayor) == idx else "lost"

    # Precios repartidos (típico de partido anulado o retiro): no hay
    # resultado deportivo. La marcamos anulada para que no quede pendiente
    # eternamente ni ensucie las estadísticas.
    print(f"  ⚠ '{outcome}' cerró sin ganador claro (precios {prices}) -> anulada",
          file=sys.stderr)
    return "anulada"


def log_result_pending(username, wallet, trade, usd, odds, msg_id=None):
    global results_dirty
    with lock:
        results.append({
            "telegram_msg_id": msg_id,
            "timestamp": trade.get("timestamp"),
            "username": username,
            "wallet": wallet,
            "slug": trade.get("slug"),
            "title": trade.get("title"),
            "outcome": trade.get("outcome"),
            "side": trade.get("side"),
            "usd": usd,
            "odds_at_bet": odds,
            "status": "pending",
        })
        results_dirty = True


def resolve_pending_results():
    global results_dirty
    changed = False
    with lock:
        pending = [r for r in results if r["status"] == "pending"]
    if pending:
        print(f"[resolver] revisando {len(pending)} pendientes...")
    abiertos = irresolubles = 0
    recien_resueltas = []
    for r in pending:
        if not r.get("slug"):
            irresolubles += 1
            continue
        market = get_market(r["slug"])
        outcome = market_result(market, r["outcome"])
        if outcome == "anulada":
            with lock:
                r["status"] = "anulada"
                r["profit_usd"] = 0.0
            changed = True
            print(f"  ⊘ anulada: {r['username']} — {(r.get('title') or '')[:40]}")
            continue
        if outcome in ("won", "lost"):
            with lock:
                r["status"] = outcome
            changed = True
            print(f"  ✔ resuelta: {r['username']} — {(r.get('title') or '')[:40]} → {outcome}")
            recien_resueltas.append((r, outcome))
        elif market is None:
            print(f"  ⚠ {r['slug']}: no pude consultar el mercado")
        elif not market.get("closed"):
            abiertos += 1
        else:
            print(f"  ⚠ {r['slug']}: cerrado pero no pude determinar el resultado "
                  f"para '{r.get('outcome')}'")
        time.sleep(0.1)
    # Cada desenlace se publica individualmente, enlazado a su alerta original.
    if PUBLICAR_RESULTADOS:
        for r, outcome in recien_resueltas:
            publicar_desenlace(r, outcome)

    if abiertos:
        print(f"  … {abiertos} siguen abiertos en Polymarket (todavía sin resolución oficial)")
    if irresolubles:
        print(f"  ⚠ {irresolubles} sin slug: nunca van a resolverse (registros viejos)")
    if changed:
        results_dirty = True


def publicar_resumen_desenlaces(lista):
    """Cuando se resuelven muchas apuestas juntas (típico después de que el
    bot estuvo apagado un rato), manda un solo mensaje con el resumen en
    lugar de uno por apuesta."""
    ganadas = [x for x in lista if x[1] == "won"]
    perdidas = [x for x in lista if x[1] == "lost"]
    total_pnl = sum(ganancia_de(r) or 0 for r, _ in lista)
    bal = f"+${total_pnl:,.0f}" if total_pnl >= 0 else f"-${abs(total_pnl):,.0f}"

    msg = f"📋 Se resolvieron {len(lista)} apuestas\n\n"
    msg += f"✅ {len(ganadas)} ganadas   ❌ {len(perdidas)} perdidas\n"
    msg += f"💵 Balance del lote: {bal}\n\n"
    for r, outcome in lista[:12]:
        ico = "✅" if outcome == "won" else "❌"
        g = ganancia_de(r) or 0
        gs = f"+${g:,.0f}" if g >= 0 else f"-${abs(g):,.0f}"
        msg += f"{ico} {r['username']} — {(r.get('title') or '')[:32]} ({gs})\n"
    if len(lista) > 12:
        msg += f"\n…y {len(lista) - 12} más."
    send_telegram(msg)


def publicar_desenlace(r, outcome):
    """Publica cómo terminó una apuesta que ya habíamos anunciado, junto al
    récord acumulado de esa ballena. Esto es lo que ningún canal de alertas
    hace: todos publican la entrada, nadie vuelve a decir cómo salió."""
    with lock:
        propias = [x for x in results if x["wallet"] == r["wallet"]
                   and x["status"] in ("won", "lost")]
    ganadas = sum(1 for x in propias if x["status"] == "won")
    perdidas = sum(1 for x in propias if x["status"] == "lost")
    total = ganadas + perdidas

    icono = "✅ GANÓ" if outcome == "won" else "❌ PERDIÓ"
    pnl = ganancia_de(r)
    msg = f"{icono} — desenlace\n\n"
    msg += f"👤 {r['username']}\n"
    msg += f"📊 {r['title']}\n"
    msg += f"🎯 Había apostado a: {r['outcome']} "
    msg += f"({r['odds_at_bet']}¢ = {a_cuota(r['odds_at_bet'])})\n"
    msg += f"💵 Apostó: ${r['usd']:,.0f}\n"
    if pnl is not None:
        if pnl >= 0:
            msg += f"💰 Ganó: +${pnl:,.0f}  (cobra ${r['usd'] + pnl:,.0f})\n"
        else:
            msg += f"🔻 Perdió: -${abs(pnl):,.0f}\n"
    msg += "\n"
    if total >= 3:
        pct = round(ganadas / total * 100)
        msg += f"📈 Récord de {r['username']} desde que lo seguimos: "
        msg += f"{ganadas}-{perdidas} ({pct}% de acierto)"
        if total < 10:
            msg += f"\n⚠️ Muestra chica todavía ({total} resueltas)"
    # Responder al mensaje de la apuesta original, para que queden enlazados
    send_telegram(msg, responder_a=r.get("telegram_msg_id"))


def build_summary_md():
    per_wallet = {}
    for r in results:
        w = r["wallet"]
        per_wallet.setdefault(w, {"username": r["username"], "won": 0, "lost": 0,
                                   "pending": 0, "usd": 0.0, "pnl": 0.0})
        per_wallet[w]["usd"] += r.get("usd", 0) or 0
        pnl_r = ganancia_de(r)
        if pnl_r is not None:
            per_wallet[w]["pnl"] = per_wallet[w].get("pnl", 0.0) + pnl_r
        if r["status"] == "won" or (r["status"] == "cerrada_venta" and r.get("profit_usd", 0) >= 0):
            per_wallet[w]["won"] += 1
        elif r["status"] == "lost" or (r["status"] == "cerrada_venta" and r.get("profit_usd", 0) < 0):
            per_wallet[w]["lost"] += 1
        else:
            per_wallet[w]["pending"] += 1

    tot_g = sum(1 for r in results if r["status"] == "won"
                or (r["status"] == "cerrada_venta" and r.get("profit_usd", 0) >= 0))
    tot_p = sum(1 for r in results if r["status"] == "lost"
                or (r["status"] == "cerrada_venta" and r.get("profit_usd", 0) < 0))
    tot_pend = sum(1 for r in results if r["status"] == "pending")
    tot_usd = sum(r.get("usd", 0) or 0 for r in results)
    resueltas = tot_g + tot_p
    pct_global = round(tot_g / resueltas * 100) if resueltas else 0

    # Balance global: sumamos el resultado real de todas las resueltas
    balance = 0.0
    apostado_resuelto = 0.0
    for r in results:
        g = ganancia_de(r)
        if g is not None:
            balance += g
            apostado_resuelto += r.get("usd", 0) or 0
    roi = (balance / apostado_resuelto * 100) if apostado_resuelto else 0

    # Qué habría pasado copiando con un monto fijo en cada apuesta.
    # Sirve para separar "aciertan seguido" de "ganan plata", que no es lo mismo.
    STAKE_FIJO = 100.0
    bal_fijo = 0.0
    n_fijo = 0
    for r in results:
        p = (r.get("odds_at_bet") or 0) / 100.0
        if r["status"] == "won" and p > 0:
            bal_fijo += STAKE_FIJO * (1 - p) / p
            n_fijo += 1
        elif r["status"] == "lost":
            bal_fijo -= STAKE_FIJO
            n_fijo += 1
    roi_fijo = (bal_fijo / (STAKE_FIJO * n_fijo) * 100) if n_fijo else 0

    signo = lambda v: f"+${v:,.0f}" if v >= 0 else f"-${abs(v):,.0f}"

    hora_peru = time.gmtime(time.time() - 5 * 3600)  # Perú = UTC-5
    lines = [
        "# Apuestas fuertes en Polymarket",
        "",
        f"Actualizado: {time.strftime('%Y-%m-%d %H:%M:%S', hora_peru)} (hora de Perú)",
        "",
        f"Seguimos **toda** apuesta de ${WHALE_THRESHOLD:,.0f} o más, de cualquier apostador.",
        "",
        "## Totales",
        "",
        f"- Apuestas registradas: **{len(results)}**  (${tot_usd:,.0f} en total)",
        f"- Resueltas: **{resueltas}** — {tot_g} ganadas / {tot_p} perdidas "
        f"(**{pct_global}%** de acierto)",
        f"- Pendientes: {tot_pend}",
        f"- Apostadores distintos: {len(per_wallet)}",
        "",
        "### Balance",
        "",
        f"- **Resultado de los apostadores: {signo(balance)}** "
        f"sobre ${apostado_resuelto:,.0f} apostados (ROI **{roi:+.1f}%**)",
        f"- Copiando ${STAKE_FIJO:,.0f} fijo en cada una: **{signo(bal_fijo)}** "
        f"sobre ${STAKE_FIJO * n_fijo:,.0f} (ROI **{roi_fijo:+.1f}%**)",
        "",
        "> Acertar seguido no es lo mismo que ganar plata: se puede tener alto "
        "porcentaje de acierto y balance negativo si las ganadas pagan poco y "
        "las perdidas son grandes.",
        "",
        "_Menos de 8 apuestas resueltas no es muestra confiable — se marca con ⚠️._",
        "",
        "## Por apostador (ordenado por monto apostado)",
        "",
        "| Apostador | Ganadas | Perdidas | Pendientes | % Acierto | Total apostado | Balance |",
        "|---|---|---|---|---|---|---|",
    ]

    orden = sorted(per_wallet.values(), key=lambda d: -d["usd"])[:40]
    for d in orden:
        tr = d["won"] + d["lost"]
        if tr == 0:
            pct_str = "—"
        elif tr < 8:
            pct_str = f"⚠️ {round(d['won']/tr*100)}% ({tr})"
        else:
            pct_str = f"{round(d['won']/tr*100)}%"
        bal = d.get("pnl", 0.0)
        bal_str = f"+${bal:,.0f}" if bal >= 0 else f"-${abs(bal):,.0f}"
        if d["won"] + d["lost"] == 0:
            bal_str = "—"
        lines.append(f"| {d['username']} | {d['won']} | {d['lost']} | {d['pending']} | "
                     f"{pct_str} | ${d['usd']:,.0f} | {bal_str} |")
    if len(per_wallet) > 40:
        lines.append(f"\n_(mostrando los 40 de mayor monto, de {len(per_wallet)} en total)_")

    # --- detalle de cada apuesta, lo que pediste ---
    lines += ["", "## Detalle de las últimas 60 apuestas", "",
              "| Apostador | Mercado | Apostó a | Cuota | Apostó | Ganó/Perdió | Resultado |",
              "|---|---|---|---|---|---|---|"]
    icono = {"won": "✅ Ganada", "lost": "❌ Perdida", "pending": "⏳ Pendiente",
             "cerrada_venta": "💰 Vendida antes", "anulada": "⊘ Anulada"}
    for r in sorted(results, key=lambda x: x.get("timestamp") or 0, reverse=True)[:60]:
        titulo = (r.get("title") or "").replace("|", "-")
        outcome = (r.get("outcome") or "").replace("|", "-")
        if outcome.lower() in ("over", "under", "yes", "no"):
            linea = ""
            for sep in ("O/U", "o/u", "Over/Under"):
                if sep in titulo:
                    linea = titulo.split(sep)[-1].strip()
                    break
            if not linea:
                import re as _re
                m = _re.search(r"([+-]?\d+\.?\d*)\s*$", titulo)
                linea = m.group(1) if m else ""
            if linea:
                outcome = f"{outcome} {linea}"
        pnl = ganancia_de(r)
        if pnl is None:
            pnl_str = "—"
        elif pnl >= 0:
            pnl_str = f"+${pnl:,.0f}"
        else:
            pnl_str = f"-${abs(pnl):,.0f}"
        cuota = a_cuota(r.get("odds_at_bet"))
        lines.append(
            f"| {r['username']} | {titulo} | {outcome} | "
            f"{cuota} ({r.get('odds_at_bet','?')}¢) | ${r.get('usd',0):,.0f} | {pnl_str} | "
            f"{icono.get(r['status'], r['status'])} |"
        )

    SUMMARY_FILE.write_text("\n".join(lines) + "\n")


def get_leaderboard_period(period):
    r = requests.get(
        f"{DATA_API}/v1/leaderboard",
        params={"category": LB_CATEGORY, "timePeriod": period, "orderBy": "PNL", "limit": TOP_N},
        timeout=15,
    )
    r.raise_for_status()
    return r.json()


def get_combined_leaderboard():
    combined = {}
    for period in LB_PERIODS:
        try:
            for t in get_leaderboard_period(period):
                w = t.get("proxyWallet")
                if w and w not in combined:
                    combined[w] = t
        except Exception as e:
            print(f"Error trayendo ranking de {period}: {e}", file=sys.stderr)
    return combined


def market_url(trade):
    slug = trade.get("eventSlug") or trade.get("slug")
    return f"https://polymarket.com/event/{slug}" if slug else "https://polymarket.com"


def get_portfolio_value(wallet):
    try:
        r = requests.get(f"{DATA_API}/value", params={"user": wallet}, timeout=8)
        data = r.json() if r.ok else None
        if data:
            return data[0].get("value")
    except Exception as e:
        print(f"Error trayendo portafolio: {e}", file=sys.stderr)
    return None


def stake_line(usd, wallet):
    """Muestra qué parte de su cartera representa la apuesta.
    OJO: si la ballena ya retiró su capital, la cartera queda casi vacía y
    el porcentaje se dispara a números sin sentido (llegamos a ver
    5.485.761%). En esos casos es más honesto no mostrar el porcentaje."""
    value = get_portfolio_value(wallet)
    if not value or value <= 0:
        return ""
    pct = usd / value * 100
    if pct > 100:
        # apostó más de lo que hoy tiene en cartera: el dato no es interpretable
        return (f"💰 Cartera visible: ${value:,.0f} "
                f"(menor que la apuesta — probablemente retiró fondos)\n")
    return f"💰 Stake: {pct:.1f}% de su cartera (${value:,.0f} total)\n"


def build_ticket(username, trade, usd, odds, wallet):
    p = (odds or 0) / 100.0
    pago = usd * (1 - p) / p if 0 < p < 1 else 0
    return (
        f"🐋 {username} — nueva apuesta fuerte\n\n"
        f"🎟️ TICKET DE APUESTA\n"
        f"Apostador: {username}\n"
        f"Acción: {'COMPRA' if trade.get('side') == 'BUY' else 'VENTA'} — \"{trade.get('outcome','')}\"\n"
        f"Mercado: {trade.get('title','')}\n"
        f"Monto: ${usd:,.0f}\n"
        f"Cuota: {a_cuota(odds)} ({odds}¢ = {odds}% implícito)\n"
        f"Si gana cobra: ${usd + pago:,.0f} (+${pago:,.0f})\n"
        f"{stake_line(usd, wallet)}"
        f"Operar: {market_url(trade)}\n"
        f"Verificar: https://polymarket.com/profile/{wallet}"
    )


def procesar_trade(trade, origen="stream"):
    """Evalúa un trade y, si pasa todos los filtros, alerta y lo registra.
    Se usa tanto para lo que llega por el websocket como para lo que
    recuperamos por API tras una desconexión."""
    wallet_raw = trade.get("proxyWallet")
    wallet = wallet_raw.lower() if wallet_raw else None
    if not wallet:
        return False

    usd = (trade.get("size") or 0) * (trade.get("price") or 0)
    if usd < WHALE_THRESHOLD:
        return False

    # --- DEDUPLICACIÓN EN TRES CAPAS ---
    # El mismo trade puede llegar por el websocket Y por el respaldo de API,
    # con diferencias mínimas (decimales del monto, 1 segundo en el timestamp).
    # Si no lo detectamos, el monto se duplica y TODA la tabla queda mal.
    tx = (trade.get("transactionHash") or "").lower()
    claves = []

    # 1) El hash de transacción es el identificador único en la blockchain.
    #    Si coincide, es literalmente la misma operación.
    if tx:
        claves.append(f"tx:{tx}")

    # 2) Sin hash, o por si viniera distinto: identidad lógica del trade,
    #    redondeando monto al dólar y agrupando el tiempo en ventanas de 10s
    #    para absorber las diferencias entre fuentes.
    claves.append("id:{}|{}|{}|{}|{}".format(
        (trade.get("proxyWallet") or "").lower(),
        trade.get("slug"),
        trade.get("outcome"),
        round((trade.get("size") or 0) * (trade.get("price") or 0)),
        int((trade.get("timestamp") or 0) // 10),
    ))

    # 3) La misma ventana pero corrida 5 segundos, para el caso en que las dos
    #    copias caigan justo a ambos lados del corte de la ventana.
    claves.append("id:{}|{}|{}|{}|{}".format(
        (trade.get("proxyWallet") or "").lower(),
        trade.get("slug"),
        trade.get("outcome"),
        round((trade.get("size") or 0) * (trade.get("price") or 0)),
        int(((trade.get("timestamp") or 0) + 5) // 10),
    ))

    if any(k in seen_keys for k in claves):
        return False
    for k in claves:
        seen_keys.add(k)
    if len(seen_keys) > 20000:
        seen_keys.clear()

    username = (trade.get("name") or trade.get("pseudonym")
                or trade.get("userName") or f"{wallet[:6]}…{wallet[-4:]}")

    if esta_excluido(username, wallet):
        return False

    if not trade.get("slug") or not trade.get("outcome"):
        print(f"[omitida] {username}: ${usd:,.0f} — el feed mandó el trade sin "
              f"slug u outcome, no se podría resolver después")
        return False

    precio_c = round((trade.get("price") or 0) * 100)
    if precio_c >= PRECIO_MAX or precio_c <= PRECIO_MIN:
        print(f"[omitida] {username}: ${usd:,.0f} a {precio_c}¢ — resultado ya definido")
        return False

    # Solo deportes y esports: nada de política, geopolítica ni cripto.
    if SOLO_DEPORTES:
        mercado = get_market(trade.get("slug"))
        if not es_deporte(mercado):
            print(f"[omitida] {username}: ${usd:,.0f} — no es un mercado de "
                  f"deportes/esports: {trade.get('title')}")
            return False

    dias = dias_hasta_resolver(trade.get("slug"))
    if dias is None:
        print(f"[omitida] {username}: ${usd:,.0f} — no pude determinar cuándo resuelve "
              f"'{trade.get('slug')}'")
        return False
    if dias > MAX_DIAS_RESOLUCION:
        print(f"[omitida] {username}: ${usd:,.0f} pero resuelve en ~{dias:.0f} días "
              f"— {trade.get('title')}")
        return False

    # Antigüedad de la operación: el respaldo por API trae historial, y sin
    # esto puede alertar apuestas de partidos que ya terminaron hace horas.
    ts = trade.get("timestamp") or 0
    edad_min = (time.time() - ts) / 60 if ts else 0
    if edad_min > MAX_EDAD_MINUTOS:
        print(f"[omitida] {username}: ${usd:,.0f} — la operación es de hace "
              f"{edad_min:.0f} min, demasiado vieja para alertar")
        return False

    # ¿El mercado sigue abierto? Si Polymarket ya lo cerró, el evento terminó
    # y no tiene sentido alertar la apuesta.
    mercado_actual = get_market(trade.get("slug"))
    if mercado_actual and mercado_actual.get("closed"):
        print(f"[omitida] {username}: ${usd:,.0f} — el mercado ya está cerrado "
              f"en Polymarket: {trade.get('title')}")
        return False

    marca = "🐋 EN VIVO" if origen == "stream" else "🐋 RECUPERADA"
    side = (trade.get("side") or "").upper()

    if side == "SELL":
        # ¿Esta venta cierra una apuesta que ya habíamos alertado? Si es así,
        # podemos decir exactamente cuánto ganó saliendo antes del final.
        with lock:
            abiertas = [x for x in results if x["status"] == "pending"
                        and x["wallet"] == wallet
                        and x["slug"] == trade.get("slug")
                        and x["outcome"] == trade.get("outcome")]
        if abiertas:
            entrada = abiertas[0]
            p_ent = (entrada.get("odds_at_bet") or 0) / 100.0
            pnl_pct = ((precio_c / 100.0) / p_ent - 1) * 100 if p_ent > 0 else 0
            invertido = sum(x.get("usd", 0) or 0 for x in abiertas)
            with lock:
                for x in abiertas:
                    x["status"] = "cerrada_venta"
                    x["profit_usd"] = round((x.get("usd", 0) or 0) * pnl_pct / 100, 2)
                    x["precio_salida"] = precio_c
            globals()["results_dirty"] = True
            ganancia = invertido * pnl_pct / 100
            sg = "+" if ganancia >= 0 else ""
            print(f"{marca} 💰 CERRÓ — {username}: entró a {entrada['odds_at_bet']}¢, "
                  f"salió a {precio_c}¢ ({sg}{pnl_pct:.1f}%) en {trade.get('title')}")
            send_telegram(
                f"💰 {username} — CERRÓ LA POSICIÓN\n\n"
                f"📊 {trade.get('title','')}\n"
                f"🎯 {trade.get('outcome','')}\n"
                f"📥 Entró a {entrada['odds_at_bet']}¢ (cuota {a_cuota(entrada['odds_at_bet'])})\n"
                f"📤 Salió a {precio_c}¢ (cuota {a_cuota(precio_c)})\n"
                f"💵 Resultado: {sg}{pnl_pct:.1f}% → {sg}${ganancia:,.0f}\n\n"
                f"No esperó el final del evento.",
                responder_a=entrada.get("telegram_msg_id"),
            )
            return False

        # Una venta NO es una apuesta nueva: la ballena está saliendo de una
        # posición, normalmente para tomar ganancia. Registrarla como apuesta
        # distorsiona la tabla (la marcaría ganada/perdida según cómo termine
        # el partido, cuando en realidad ya cobró y salió).
        if not PUBLICAR_VENTAS:
            print(f"[venta] {username}: ${usd:,.0f} a {precio_c}¢ en "
                  f"{trade.get('title')} — sale de la posición, no se registra")
            return False
        print(f"{marca} 💰 SALIDA — {username}: vendió ${usd:,.0f} a {precio_c}¢ "
              f"en {trade.get('title')}")
        send_telegram(
            f"💰 {username} — SALIDA DE POSICIÓN\n\n"
            f"Vendió ${usd:,.0f} a {precio_c}¢ (cuota {a_cuota(precio_c)})\n"
            f"Mercado: {trade.get('title','')}\n"
            f"Resultado: {trade.get('outcome','')}\n\n"
            f"⚠️ Está saliendo, no entrando. Si compró más barato, "
            f"está tomando ganancia sin esperar el final."
        )
        return False   # no se registra en la tabla de apuestas

    # --- FUSIÓN DE FILLS ---
    # Polymarket parte las órdenes grandes en varios pedazos que llegan como
    # trades separados. Sin esto, una sola decisión se registra 4-5 veces:
    # infla los conteos y distorsiona el % de acierto y el balance.
    # Usamos el timestamp del PROPIO trade (el que da Polymarket), no la hora
    # en que lo procesamos: dos fills de la misma orden llegan con el mismo
    # segundo o uno de diferencia, aunque el bot los procese con demora.
    ts_trade = trade.get("timestamp") or time.time()

    # Reservamos el lugar dentro del lock ANTES de mandar nada a Telegram, para
    # que un segundo fill que llegue mientras tanto encuentre con qué fusionar.
    with lock:
        previa = next((x for x in results
                       if x["status"] == "pending"
                       and x["wallet"] == wallet
                       and x["slug"] == trade.get("slug")
                       and x["outcome"] == trade.get("outcome")
                       and abs(ts_trade - (x.get("ultimo_fill") or 0)) < FILL_MERGE_WINDOW), None)
        if previa:
            total_previo = previa.get("usd", 0) or 0
            # ¿Es la MISMA operación llegando dos veces (por el stream y por el
            # respaldo de API, con mínimas diferencias de redondeo), o un fill
            # nuevo de una orden partida? Si el monto y el precio coinciden
            # casi exacto, es un duplicado: se ignora, NO se suma.
            if (abs(usd - total_previo) / max(total_previo, 1) < 0.01
                    and precio_c == previa["odds_at_bet"]):
                print(f"   ↳ duplicado ignorado de {username}: ${usd:,.0f} "
                      f"(ya registrado, mismo monto y precio)")
                globals()["_dup_detectado"] = True
            else:
                nuevo_total = total_previo + usd
                previa["odds_at_bet"] = round(
                    (total_previo * previa["odds_at_bet"] + usd * precio_c) / nuevo_total)
                previa["usd"] = nuevo_total
                previa["ultimo_fill"] = ts_trade
                previa["fills"] = previa.get("fills", 1) + 1
                print(f"   ↳ fill adicional de {username}: +${usd:,.0f} "
                      f"(total ${nuevo_total:,.0f}, {previa['fills']} fills)")
            globals()["results_dirty"] = True

    if previa:
        return False

    # Creamos el registro PRIMERO (dentro del lock) y mandamos el mensaje
    # después. Así no queda ninguna ventana sin registro donde un fill
    # simultáneo se escape.
    log_result_pending(username, wallet, trade, usd, precio_c, None)
    with lock:
        registro = results[-1]
        registro["ultimo_fill"] = ts_trade
        registro["fills"] = 1

    print(f"{marca} — {username}: ${usd:,.0f} en {trade.get('title')}")
    msg_id = send_telegram(build_ticket(username, trade, usd, precio_c, wallet))
    with lock:
        registro["telegram_msg_id"] = msg_id
    return True


def auditar_montos():
    """Revisa el archivo buscando señales de que algún monto está inflado por
    duplicación. No corrige nada solo: avisa en el log para poder verificar
    contra el perfil real en Polymarket. Una tabla con montos mal es peor que
    no tener tabla, así que conviene enterarse temprano."""
    from collections import defaultdict
    grupos = defaultdict(list)
    with lock:
        copia = list(results)
    for x in copia:
        grupos[(x.get("wallet"), x.get("slug"), x.get("outcome"))].append(x)

    sospechosos = 0
    for clave, lista in grupos.items():
        if len(lista) < 2:
            continue
        # Varios registros del mismo apostador+mercado+resultado: puede ser
        # legítimo (entradas separadas en el tiempo) o duplicación.
        lista.sort(key=lambda z: z.get("timestamp") or 0)
        for a, b in zip(lista, lista[1:]):
            dt = abs((b.get("timestamp") or 0) - (a.get("timestamp") or 0))
            ma, mb = a.get("usd", 0) or 0, b.get("usd", 0) or 0
            if dt <= 30 and abs(ma - mb) / max(ma, 1) < 0.01:
                sospechosos += 1
                print(f"[auditoría] ⚠️ posible duplicado: {a.get('username')} — "
                      f"${ma:,.0f} y ${mb:,.0f} con {dt}s de diferencia en "
                      f"{(a.get('title') or '')[:40]}", file=sys.stderr)
    if sospechosos:
        print(f"[auditoría] ⚠️ {sospechosos} par(es) sospechoso(s) — verificá "
              f"contra el perfil en Polymarket antes de confiar en esos montos",
              file=sys.stderr)
    return sospechosos


def recuperar_perdidas():
    """Red de seguridad: consulta a la API las operaciones grandes recientes
    y procesa las que el websocket no vio (por desconexión o mensajes
    perdidos). La deduplicación por transactionHash evita repetir alertas."""
    try:
        r = requests.get(
            f"{DATA_API}/trades",
            params={"limit": 500, "takerOnly": "false",
                    "filterType": "CASH", "filterAmount": int(WHALE_THRESHOLD)},
            timeout=20,
        )
        if not r.ok:
            print(f"[respaldo] la API respondió {r.status_code}", file=sys.stderr)
            return
        trades = r.json()
        if not isinstance(trades, list):
            return
    except Exception as e:
        print(f"[respaldo] error consultando la API: {e}", file=sys.stderr)
        return

    recuperadas = 0
    for t in trades:
        try:
            if procesar_trade(t, origen="api"):
                recuperadas += 1
        except Exception as e:
            print(f"[respaldo] error procesando un trade: {e}", file=sys.stderr)
    if recuperadas:
        print(f"[respaldo] ⚠️ se recuperaron {recuperadas} apuestas que el stream se perdió")
    else:
        print(f"[respaldo] revisadas {len(trades)} operaciones grandes — nada nuevo")


def dias_hasta_resolver(slug):
    """Cuántos días faltan para que resuelva el mercado.

    IMPORTANTE — orden de prioridad:
      1) La fecha del SLUG (mlb-chc-wsh-2026-08-11). Es la del partido y no
         tiene ambigüedad. Va primero porque la API a veces devuelve la fecha
         del evento contenedor (la serie completa), lo que hacía que partidos
         de HOY se descartaran como "resuelve en ~7 días".
      2) Si el slug no trae fecha, la fecha de la API.
      3) Si no hay ninguna, None -> el que llama descarta (los eventos de
         corto plazo siempre tienen fecha; sin fecha suele ser largo plazo).
    """
    import re as _re
    dias_slug = None
    m2 = _re.search(r"(20\d{2})-(\d{2})-(\d{2})", slug or "")
    if m2:
        try:
            fecha = datetime(int(m2.group(1)), int(m2.group(2)), int(m2.group(3)),
                             23, 59, tzinfo=timezone.utc)
            dias_slug = (fecha - datetime.now(timezone.utc)).total_seconds() / 86400
        except Exception:
            dias_slug = None

    dias_api = None
    m = get_market(slug)
    if m:
        fin = m.get("endDate") or m.get("endDateIso") or m.get("end_date")
        if fin:
            try:
                fin_dt = datetime.fromisoformat(str(fin).replace("Z", "+00:00"))
                dias_api = (fin_dt - datetime.now(timezone.utc)).total_seconds() / 86400
            except Exception:
                dias_api = None

    # Si las dos existen y difieren mucho, dejamos rastro para poder auditarlo
    if dias_slug is not None and dias_api is not None and abs(dias_slug - dias_api) > 1:
        print(f"[fecha] '{slug}': slug dice {dias_slug:.1f} días, API dice "
              f"{dias_api:.1f} — uso la del slug")

    if dias_slug is not None:
        return dias_slug
    return dias_api


def send_telegram(text, responder_a=None):
    """Envía un mensaje y devuelve su message_id (o None si falló).
    Si se pasa responder_a, el mensaje sale como respuesta a ese otro,
    que es lo que permite enlazar el desenlace con la apuesta original."""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return None
    try:
        cuerpo = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text,
            "disable_web_page_preview": True,
        }
        if responder_a:
            cuerpo["reply_to_message_id"] = responder_a
            cuerpo["allow_sending_without_reply"] = True
        r = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json=cuerpo,
            timeout=10,
        )
        if not r.ok:
            print(f"[telegram] ⚠️ respuesta {r.status_code}: {r.text[:300]}", file=sys.stderr)
        else:
            try:
                return r.json().get("result", {}).get("message_id")
            except Exception:
                return None
    except Exception as e:
        print(f"Error mandando a Telegram: {e}", file=sys.stderr)
    return None


def a_cuota(precio_centavos):
    """Convierte el precio de Polymarket (en centavos, 0-100) a cuota decimal,
    la de toda la vida. Ej: 40¢ -> 2.50 ; 62¢ -> 1.61 ; 80¢ -> 1.25."""
    p = (precio_centavos or 0) / 100.0
    if p <= 0 or p >= 1:
        return "—"
    return f"{1/p:.2f}"


def ganancia_de(r):
    """Cuánto ganó o perdió esa apuesta, según cómo resolvió."""
    # Si cerró vendiendo antes del final, el resultado ya quedó calculado
    # con el precio de salida al momento de la venta.
    if r.get("status") == "anulada":
        return None
    if r.get("status") == "cerrada_venta":
        return r.get("profit_usd", 0.0)
    p = (r.get("odds_at_bet") or 0) / 100.0
    usd = r.get("usd", 0) or 0
    if r["status"] == "won" and p > 0:
        return usd * (1 - p) / p
    if r["status"] == "lost":
        return -usd
    return None


# ---------- websocket en vivo ----------
def on_ws_open(ws):
    global last_msg_at
    last_msg_at = time.time()
    print("[en vivo] conectado — escuchando todas las apuestas de Polymarket")
    ws.send(json.dumps({
        "action": "subscribe",
        "subscriptions": [{"topic": "activity", "type": "trades"}]
    }))


def on_ws_message(ws, message):
    global last_msg_at
    last_msg_at = time.time()

    if message == "PONG":
        return

    global raw_samples_shown
    if raw_samples_shown < 3:
        raw_samples_shown += 1
        print(f"[diagnóstico] mensaje crudo #{raw_samples_shown}: {message[:1500]}")

    try:
        msg = json.loads(message)
    except Exception:
        return
    is_trade = (msg.get("topic") == "activity" and msg.get("type") == "trades") or msg.get("type") == "trades"
    if not is_trade:
        return
    trade = msg.get("payload") or msg.get("data") or msg
    wallet_raw = trade.get("proxyWallet")
    wallet = wallet_raw.lower() if wallet_raw else None

    global msg_count
    msg_count += 1
    if msg_count % 500 == 0:
        print(f"[en vivo] {msg_count} trades del chorro global recibidos hasta ahora (siguen llegando)")

    if not wallet:
        return

    # Toda la lógica de filtros y alerta vive en procesar_trade(), compartida
    # con la recuperación por API para que se comporten exactamente igual.
    procesar_trade(trade, origen="stream")


def on_ws_error(ws, error):
    print(f"[en vivo] error de conexión: {error}", file=sys.stderr)


def on_ws_close(ws, code, msg):
    print("[en vivo] conexión cerrada, reconectando...")


# ---------- hilo de fondo: vigilados + revisión de resultados ----------
def _git(comando, timeout=60):
    """Ejecuta un comando de git con TIEMPO LÍMITE.
    Antes usábamos os.system(), que bloquea para siempre si el comando se
    cuelga (por ejemplo un push esperando credenciales o con la red trabada).
    Cuando eso pasaba, el hilo de guardado quedaba muerto y el bot seguía
    funcionando pero sin subir nada al repo.
    Devuelve el código de salida, o None si se pasó del tiempo."""
    import subprocess
    try:
        r = subprocess.run(comando, shell=True, timeout=timeout,
                           capture_output=True, text=True)
        return r.returncode
    except subprocess.TimeoutExpired:
        print(f"[guardar] ⏱ '{comando}' superó los {timeout}s y se canceló",
              file=sys.stderr)
        return None
    except Exception as e:
        print(f"[guardar] error ejecutando '{comando}': {e}", file=sys.stderr)
        return None


ultimo_guardado_ok = [time.time()]


def save_and_commit_results():
    global results_dirty
    with lock:
        RESULTS_FILE.write_text(json.dumps(results, indent=2))
        build_summary_md()
        WATCHED_FILE.write_text(json.dumps(watched_meta, indent=2))
    try:
        _git('git config user.name "whale-alert-bot"', 15)
        _git('git config user.email "actions@github.com"', 15)
        _git("git add results.json results.md watched.json", 30)
        _git('git diff --staged --quiet || git commit -m "actualizar resultados y vigilados"', 30)

        subido = False
        for intento in range(3):
            if _git("git push", 90) == 0:
                subido = True
                break
            print(f"[guardar] push rechazado (intento {intento+1}/3), "
                  f"bajando cambios ajenos y reintentando...", file=sys.stderr)
            _git("git fetch origin main", 60)
            if _git('git merge --no-edit -X ours origin/main', 60) != 0:
                _git("git merge --abort", 30)
                print("[guardar] no se pudo fusionar, se reintenta en el próximo ciclo",
                      file=sys.stderr)
                break

        if subido:
            ultimo_guardado_ok[0] = time.time()
            results_dirty = False
        else:
            mins = (time.time() - ultimo_guardado_ok[0]) / 60
            print(f"[guardar] ⚠️ no se pudo subir. Van {mins:.0f} min sin guardar "
                  f"en el repo.", file=sys.stderr)
            if mins > 15:
                print(f"[guardar] 🚨 ALERTA: {mins:.0f} MINUTOS SIN GUARDAR — "
                      f"revisá el workflow, algo está trabado", file=sys.stderr)
                send_telegram(f"⚠️ El bot lleva {mins:.0f} minutos sin poder "
                               f"guardar en GitHub. Sigue recibiendo apuestas, "
                               f"pero la tabla no se está actualizando.")
    except Exception as e:
        import traceback
        print(f"[guardar] error, se reintenta en el próximo ciclo: {e}", file=sys.stderr)
        traceback.print_exc()


def background_worker_vigilado():
    """Envuelve al hilo de fondo. Si se muere por un error inesperado, lo
    relanza en vez de dejarlo caído en silencio (que fue lo que pasó: el bot
    seguía recibiendo apuestas pero nadie guardaba nada en el repo)."""
    while not stop_flag.is_set():
        try:
            background_worker()
            return   # salida normal
        except Exception as e:
            import traceback
            print(f"[vigilante] el hilo de fondo se cayó: {e} — relanzando en 10s",
                  file=sys.stderr)
            traceback.print_exc()
            time.sleep(10)


def background_worker():
    global last_msg_at
    last_lb_refresh = 0
    last_heartbeat = time.time()
    last_resolve_check = 0
    last_backup_check = time.time()   # esperar un ciclo antes del primer respaldo
    last_save = time.time()
    while not stop_flag.is_set():
        now = time.time()

        if now - last_lb_refresh > LEADERBOARD_REFRESH_SECONDS or not watched:
            combined = get_combined_leaderboard()  # wallet original -> trader dict, del top actual
            cutoff = now - MIN_WATCH_DAYS * 86400
            with lock:
                added, dropped = 0, 0
                for w, t in combined.items():
                    wl = w.lower()
                    if wl not in watched_meta:
                        watched_meta[wl] = {"username": t.get("userName", "anon"), "added_at": now}
                        added += 1
                    else:
                        watched_meta[wl]["username"] = t.get("userName", watched_meta[wl]["username"])
                current_top_wallets = {w.lower() for w in combined.keys()}
                for wl in list(watched_meta.keys()):
                    if wl not in current_top_wallets and watched_meta[wl]["added_at"] < cutoff:
                        del watched_meta[wl]
                        dropped += 1
                watched.clear()
                watched.update({wl: m["username"] for wl, m in watched_meta.items()})
            print(f"[ranking] {len(watched)} vigilados (+{added} nuevos, -{dropped} vencidos tras {MIN_WATCH_DAYS} días): {list(watched.values())}")
            last_lb_refresh = now

        if now - last_heartbeat > 120:
            print(f"[heartbeat] mensajes recibidos del chorro hasta ahora: {msg_count}")
            last_heartbeat = now

        if now - last_resolve_check > 60:
            resolve_pending_results()
            last_resolve_check = now

        # Red de seguridad: recuperar por API lo que el stream se perdió
        # durante desconexiones (el stream se queda mudo cada tanto).
        if now - last_backup_check > BACKUP_INTERVAL:
            try:
                recuperar_perdidas()
                auditar_montos()
            except Exception as e:
                print(f"[respaldo] falló, se reintenta luego: {e}", file=sys.stderr)
            last_backup_check = now

        if now - last_msg_at > MUDO_SEGUNDOS and current_ws is not None:
            print("[en vivo] 60s sin recibir nada — la conexión parece muda, forzando reconexión...")
            try:
                current_ws.close()
            except Exception:
                pass
            last_msg_at = time.time()

        if now - last_save > 120:
            print("[resultados] guardando progreso en el repo...")
            save_and_commit_results()
            last_save = now

        time.sleep(5)


def main():
    loaded = load_json(RESULTS_FILE)
    if loaded:
        results.extend(loaded)
        print(f"[resultados] cargados {len(results)} registros anteriores")

    loaded_watched = load_json(WATCHED_FILE)
    if loaded_watched:
        watched_meta.update(loaded_watched)
        with lock:
            watched.update({wl: m["username"] for wl, m in watched_meta.items()})
        print(f"[ranking] cargados {len(watched_meta)} vigilados de corridas anteriores")

    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("¡Falta TELEGRAM_BOT_TOKEN o TELEGRAM_CHAT_ID! No va a poder avisar nada.", file=sys.stderr)
    else:
        print("[telegram] mandando mensaje de prueba...")
        send_telegram("✅ Whale Alerts bot conectado\n\nSi ves este mensaje en Telegram, todo funciona bien. Las próximas apuestas fuertes de los vigilados van a llegar acá.")

    bg = threading.Thread(target=background_worker_vigilado, daemon=True)
    bg.start()

    while not watched and time.time() - run_start < 60:
        time.sleep(1)

    global current_ws, last_msg_at
    ws = websocket.WebSocketApp(
        RTDS_URL, on_open=on_ws_open, on_message=on_ws_message,
        on_error=on_ws_error, on_close=on_ws_close,
    )
    current_ws = ws
    last_msg_at = time.time()
    intentos_fallidos = 0

    while time.time() - run_start < MAX_RUNTIME_SECONDS:
        conectado_desde = time.time()
        ws.run_forever(ping_interval=15, ping_timeout=8)
        if time.time() - run_start >= MAX_RUNTIME_SECONDS:
            break
        # Si la conexión duró un rato razonable, no fue un fallo persistente:
        # reseteamos la espera para que el próximo reintento sea inmediato.
        if time.time() - conectado_desde > 60:
            intentos_fallidos = 0
        intentos_fallidos += 1
        espera = min(1 * (2 ** (intentos_fallidos - 1)), 30)  # 1,2,4,8,16,30s
        print(f"[en vivo] reintentando conexión en {espera}s "
              f"(intento {intentos_fallidos})...")
        time.sleep(espera)

    stop_flag.set()
    resolve_pending_results()
    save_and_commit_results()
    print("Ciclo terminado — GitHub va a arrancar uno nuevo con el cron.")


if __name__ == "__main__":
    main()
