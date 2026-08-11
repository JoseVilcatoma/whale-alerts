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
MAX_DIAS_RESOLUCION = float(os.environ.get("MAX_DIAS_RESOLUCION", "2"))  # solo apuestas que resuelven en 1-2 días
# Ignorar apuestas a resultados ya casi definidos: a 95¢ (cuota 1.05) no se
# está prediciendo nada, se recoge el último centavo, y eso infla el % de
# acierto sin decir nada de la habilidad del apostador.
PRECIO_MAX = float(os.environ.get("PRECIO_MAX", "95"))   # en centavos
PRECIO_MIN = float(os.environ.get("PRECIO_MIN", "3"))    # el extremo opuesto
TOP_N = int(os.environ.get("TOP_N", "20"))
LB_CATEGORY = os.environ.get("LB_CATEGORY", "OVERALL")
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


def get_market(slug):
    if not slug:
        return None
    if slug in _market_cache:
        return _market_cache[slug]
    try:
        r = requests.get(f"{GAMMA_API}/markets/slug/{slug}", timeout=8)
        m = r.json() if r.ok else None
    except Exception:
        m = None
    _market_cache[slug] = m
    return m


def market_result(market, outcome):
    """'won' / 'lost' / 'open' / None (todavía no se puede determinar)."""
    if not market:
        return None
    if not market.get("closed"):
        return "open"
    try:
        outcomes = json.loads(market["outcomes"])
        prices = json.loads(market["outcomePrices"])
        idx = next((i for i, o in enumerate(outcomes) if (o or "").lower() == (outcome or "").lower()), -1)
        if idx == -1:
            return None
        p = float(prices[idx])
        if p >= 0.99:
            return "won"
        if p <= 0.01:
            return "lost"
        return None
    except Exception:
        return None


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
    for r in pending:
        if not r.get("slug"):
            irresolubles += 1
            continue
        market = get_market(r["slug"])
        outcome = market_result(market, r["outcome"])
        if outcome in ("won", "lost"):
            with lock:
                r["status"] = outcome
            changed = True
            print(f"  ✔ resuelta: {r['username']} — {(r.get('title') or '')[:40]} → {outcome}")
            if PUBLICAR_RESULTADOS:
                publicar_desenlace(r, outcome)
        elif market is None:
            print(f"  ⚠ {r['slug']}: no pude consultar el mercado")
        elif not market.get("closed"):
            abiertos += 1
        else:
            print(f"  ⚠ {r['slug']}: cerrado pero no pude determinar el resultado "
                  f"para '{r.get('outcome')}'")
        time.sleep(0.1)
    if abiertos:
        print(f"  … {abiertos} siguen abiertos en Polymarket (todavía sin resolución oficial)")
    if irresolubles:
        print(f"  ⚠ {irresolubles} sin slug: nunca van a resolverse (registros viejos)")
    if changed:
        results_dirty = True


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
        if r["status"] == "won":
            per_wallet[w]["won"] += 1
        elif r["status"] == "lost":
            per_wallet[w]["lost"] += 1
        else:
            per_wallet[w]["pending"] += 1

    tot_g = sum(1 for r in results if r["status"] == "won")
    tot_p = sum(1 for r in results if r["status"] == "lost")
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
    icono = {"won": "✅ Ganada", "lost": "❌ Perdida", "pending": "⏳ Pendiente"}
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
        f"Operar: {market_url(trade)}"
    )


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
            # si el mensaje original ya no existe, que igual se envíe suelto
            cuerpo["allow_sending_without_reply"] = True
        r = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json=cuerpo,
            timeout=10,
        )
        if r.status_code != 200:
            print(f"[telegram] ⚠️ respuesta {r.status_code}: {r.text[:300]}", file=sys.stderr)
        else:
            try:
                return r.json().get("result", {}).get("message_id")
            except Exception:
                return None
    except Exception as e:
        print(f"Error mandando a Telegram: {e}", file=sys.stderr)
    return None


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


def a_cuota(precio_centavos):
    """Convierte el precio de Polymarket (en centavos, 0-100) a cuota decimal,
    la de toda la vida. Ej: 40¢ -> 2.50 ; 62¢ -> 1.61 ; 80¢ -> 1.25."""
    p = (precio_centavos or 0) / 100.0
    if p <= 0 or p >= 1:
        return "—"
    return f"{1/p:.2f}"


def ganancia_de(r):
    """Cuánto ganó o perdió esa apuesta, según cómo resolvió."""
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

    # Ahora NO filtramos por ranking: cualquiera que supere el umbral entra.
    # Filtramos primero por monto porque es lo más barato de evaluar.
    usd = (trade.get("size") or 0) * (trade.get("price") or 0)
    if usd < WHALE_THRESHOLD:
        return

    key = f"{trade.get('transactionHash','')}_{trade.get('timestamp')}_{trade.get('asset')}_{trade.get('size')}"
    if key in seen_keys:
        return
    seen_keys.add(key)
    if len(seen_keys) > 5000:
        seen_keys.clear()

    # El nombre viene en el propio trade; si no, usamos la wallet abreviada
    username = (trade.get("name") or trade.get("pseudonym")
                or trade.get("userName") or f"{wallet[:6]}…{wallet[-4:]}")

    # Sin slug o sin outcome no podemos consultar el mercado después, así que
    # la apuesta quedaría "pendiente" para siempre. Mejor no registrarla.
    if not trade.get("slug") or not trade.get("outcome"):
        print(f"[omitida] {username}: ${usd:,.0f} — el feed mandó el trade sin "
              f"slug u outcome, no se podría resolver después")
        return

    # Descartar apuestas a resultados ya definidos (cuota ~1.01): no son
    # predicción, y ensucian el % de acierto de la tabla.
    precio_c = round((trade.get("price") or 0) * 100)
    if precio_c >= PRECIO_MAX or precio_c <= PRECIO_MIN:
        print(f"[omitida] {username}: ${usd:,.0f} a {precio_c}¢ "
              f"(cuota {a_cuota(precio_c)}) — resultado ya definido")
        return

    # Solo nos interesan apuestas de corta duración: si el mercado resuelve
    # más allá del límite, la ignoramos (nada de "campeón a fin de año").
    dias = dias_hasta_resolver(trade.get("slug"))
    if dias is None:
        print(f"[omitida] {username}: ${usd:,.0f} — no pude determinar cuándo resuelve "
              f"'{trade.get('slug')}' (casi siempre es un mercado de largo plazo)")
        return
    if dias > MAX_DIAS_RESOLUCION:
        print(f"[omitida] {username}: ${usd:,.0f} pero resuelve en ~{dias:.0f} días "
              f"— {trade.get('title')}")
        return

    odds = round((trade.get("price") or 0) * 100)
    print(f"🐋 EN VIVO — {username}: ${usd:,.0f} en {trade.get('title')}")
    msg_id = send_telegram(build_ticket(username, trade, usd, odds, wallet))
    log_result_pending(username, wallet, trade, usd, odds, msg_id)


def on_ws_error(ws, error):
    print(f"[en vivo] error de conexión: {error}", file=sys.stderr)


def on_ws_close(ws, code, msg):
    print("[en vivo] conexión cerrada, reconectando...")


# ---------- hilo de fondo: vigilados + revisión de resultados ----------
def save_and_commit_results():
    global results_dirty
    with lock:
        RESULTS_FILE.write_text(json.dumps(results, indent=2))
        build_summary_md()
        WATCHED_FILE.write_text(json.dumps(watched_meta, indent=2))
    try:
        os.system('git config user.name "whale-alert-bot"')
        os.system('git config user.email "actions@github.com"')
        os.system("git add results.json results.md watched.json")
        os.system('git diff --staged --quiet || git commit -m "actualizar resultados y vigilados"')

        for intento in range(3):
            if os.system("git push") == 0:
                break
            # El otro bot (paper trading) subió algo mientras tanto. Como cada
            # bot escribe archivos distintos, nos quedamos con lo nuestro si
            # hay choque y reintentamos.
            print(f"[guardar] push rechazado (intento {intento+1}/3), "
                  f"bajando cambios ajenos y reintentando...", file=sys.stderr)
            os.system("git fetch origin main")
            if os.system('git merge --no-edit -X ours origin/main') != 0:
                os.system("git merge --abort")
                print("[guardar] no se pudo fusionar, se reintenta en el próximo ciclo",
                      file=sys.stderr)
                break
        results_dirty = False
    except Exception as e:
        import traceback
        print(f"[guardar] error, se reintenta en el próximo ciclo: {e}", file=sys.stderr)
        traceback.print_exc()


def background_worker():
    global last_msg_at
    last_lb_refresh = 0
    last_heartbeat = time.time()
    last_resolve_check = 0
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

        if now - last_msg_at > 60 and current_ws is not None:
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

    bg = threading.Thread(target=background_worker, daemon=True)
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

    while time.time() - run_start < MAX_RUNTIME_SECONDS:
        ws.run_forever(ping_interval=30, ping_timeout=10)
        if time.time() - run_start >= MAX_RUNTIME_SECONDS:
            break
        print("[en vivo] reintentando conexión en 5s...")
        time.sleep(5)

    stop_flag.set()
    resolve_pending_results()
    save_and_commit_results()
    print("Ciclo terminado — GitHub va a arrancar uno nuevo con el cron.")


if __name__ == "__main__":
    main()
