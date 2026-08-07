"""
whale_copy_paper.py — SIMULADOR de copy-trading (paper trading, sin dinero real)

Qué hace, en criollo:
  1. Cada cierto tiempo arma una lista de candidatos (el mismo pool que ya usa
     whale_alert_bot.py: top N por PnL en dólares, semana + mes combinados).
  2. Para cada candidato calcula su % DE RENDIMIENTO (no PnL en dólares):
         roi = pnl_del_periodo / valor_actual_de_su_portafolio
     y se queda con los 5 mejores por ese %. Estos son los "vigilados".
  3. Escucha el mismo chorro en vivo de trades de Polymarket. Cuando alguno
     de los 5 vigilados hace una apuesta, calcula qué % de SU PROPIO
     portafolio representó esa apuesta, y replica ese mismo % pero sobre
     un bankroll simulado (arranca en INITIAL_BANKROLL, ver abajo).
  4. Guarda cada apuesta simulada como "pending" y, cuando el mercado
     resuelve, calcula si esa posición de papel ganó o perdió y ACTUALIZA
     el bankroll simulado.
  5. No aplica ningún tope por mercado ni límite de pérdida todavía —eso se
     define después de ver los datos de las primeras semanas—, pero SÍ deja
     registrado cuándo dos o más vigilados apostaron al mismo mercado el
     mismo día, para poder calibrar ese tope más adelante con datos reales.
  6. No toca ninguna wallet real, no firma nada, no gasta nada. Es 100%
     simulación — todo el "dinero" de este script es un número en un
     archivo JSON.

Variables de entorno (todas opcionales, tienen default):
  TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID   - si están, manda avisos "🧪 PAPER"
                                            (podés reusar las mismas que ya
                                            tenés, o poner otro chat aparte)
  INITIAL_BANKROLL           - bankroll simulado inicial en USD (default 1000)
  TOP_N_CANDIDATES           - candidatos por período antes de filtrar por
                                % de rendimiento (default 20, igual que el
                                bot de alertas)
  TOP_K_REPLICATE            - a cuántos de los mejores por % replicar
                                (default 5)
  MIN_TRADE_PCT              - ignora apuestas del vigilado que representen
                                menos de este % de SU portafolio, para no
                                replicar "ruido" de apuestas chiquitas
                                (default 0.1)
  LB_CATEGORY                 - igual que el bot de alertas (default OVERALL)
  LEADERBOARD_REFRESH_SECONDS - cada cuánto se recalculan los 5 vigilados
                                 (default 900 = 15 min)
  MIN_WATCH_DAYS              - mínimo de días que se sigue vigilando a
                                 alguien aunque salga del top 5 (default 7)
  MAX_RUNTIME_SECONDS         - cuándo cortar solo (default 21000 = 5h50m)
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


def _allowed_gai_family():
    return socket.AF_INET

urllib3_cn.allowed_gai_family = _allowed_gai_family

DATA_API = "https://data-api.polymarket.com"
GAMMA_API = "https://gamma-api.polymarket.com"
RTDS_URL = "wss://ws-live-data.polymarket.com"

TRADES_FILE = Path(__file__).parent / "paper_trades.json"
STATE_FILE = Path(__file__).parent / "paper_state.json"
SUMMARY_FILE = Path(__file__).parent / "paper_summary.md"
WATCHED_FILE = Path(__file__).parent / "paper_watched.json"

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "").strip()

INITIAL_BANKROLL = float(os.environ.get("INITIAL_BANKROLL", "1000"))
TOP_N_CANDIDATES = int(os.environ.get("TOP_N_CANDIDATES", "20"))
TOP_K_REPLICATE = int(os.environ.get("TOP_K_REPLICATE", "5"))
MIN_TRADE_PCT = float(os.environ.get("MIN_TRADE_PCT", "0.1"))
MIN_WHALE_PORTFOLIO = float(os.environ.get("MIN_WHALE_PORTFOLIO", "2000"))
MAX_DAYS_TO_RESOLUTION = float(os.environ.get("MAX_DAYS_TO_RESOLUTION", "1"))  # solo mercados que resuelven el mismo día
MIN_SHORT_TERM_SHARE = float(os.environ.get("MIN_SHORT_TERM_SHARE", "0.3"))  # % mínimo de sus apuestas recientes que deben ser de corto plazo
ACTIVITY_SAMPLE_SIZE = int(os.environ.get("ACTIVITY_SAMPLE_SIZE", "10"))  # cuántas apuestas recientes de cada candidato se revisan
FILL_MERGE_WINDOW_SECONDS = float(os.environ.get("FILL_MERGE_WINDOW_SECONDS", "15"))  # fusiona fills de la misma compra dentro de esta ventana
ALLTIME_TOP_N = int(os.environ.get("ALLTIME_TOP_N", "600"))  # exige aparecer entre los N mejores históricos (toda la vida), no solo semana/mes
LB_CATEGORY = os.environ.get("LB_CATEGORY", "OVERALL")
LB_PERIODS = ["WEEK", "MONTH"]

LEADERBOARD_REFRESH_SECONDS = int(os.environ.get("LEADERBOARD_REFRESH_SECONDS", "900"))
MIN_WATCH_DAYS = float(os.environ.get("MIN_WATCH_DAYS", "0"))  # 0 = solo los 5 del momento, sin colchón
MAX_RUNTIME_SECONDS = int(os.environ.get("MAX_RUNTIME_SECONDS", str(5 * 3600 + 50 * 60)))

watched = {}        # wallet (minúsculas) -> username   (los 5 vigilados actuales)
watched_meta = {}    # wallet -> {"username":..., "added_at": ts, "roi_pct": ...}
msg_count = 0
last_msg_at = time.time()
current_ws = None
seen_keys = set()
lock = threading.Lock()
run_start = time.time()
stop_flag = threading.Event()

trades = []           # cada posición simulada: {..., "status": "pending"/"won"/"lost"}
trades_dirty = False
_market_cache = {}
_portfolio_cache = {}   # wallet -> (valor, timestamp) — para no pedir de más

bankroll = INITIAL_BANKROLL
bankroll_history = []   # [{"timestamp":..., "bankroll":..., "event":...}, ...]


# ---------- utilidades básicas ----------
def load_json(path, default=None):
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            return default
    return default


def get_portfolio_value(wallet, max_age=60):
    """Valor total del portafolio de una wallet, con cache corto (1 min)
    para no pedirle de más a la API pero mantener el % lo más al día posible."""
    now = time.time()
    cached = _portfolio_cache.get(wallet)
    if cached and now - cached[1] < max_age:
        return cached[0]
    try:
        r = requests.get(f"{DATA_API}/value", params={"user": wallet}, timeout=8)
        data = r.json() if r.ok else None
        value = data[0].get("value") if data else None
    except Exception as e:
        print(f"Error trayendo portafolio: {e}", file=sys.stderr)
        value = None
    _portfolio_cache[wallet] = (value, now)
    return value


def get_market(slug, max_age=300):
    """Trae los datos de un mercado. Si ya está cerrado, el dato no cambia
    más y se cachea para siempre. Si todavía está abierto, se vuelve a
    consultar cada max_age segundos en vez de quedarse pegado con la
    primera respuesta."""
    if not slug:
        return None
    cached = _market_cache.get(slug)
    if cached:
        m, fetched_at = cached
        if m and m.get("closed"):
            return m
        if time.time() - fetched_at < max_age:
            return m
    try:
        r = requests.get(f"{GAMMA_API}/markets/slug/{slug}", params={"include_tag": "true"}, timeout=8)
        m = r.json() if r.ok else None
    except Exception:
        m = None
    _market_cache[slug] = (m, time.time())
    return m


def days_to_resolution(market):
    """Cuántos días faltan para que el mercado resuelva, según su fecha de
    cierre esperada. Si no se puede determinar, devuelve None (y en ese
    caso se deja pasar la apuesta, para no perdernos algo válido por un
    dato faltante)."""
    if not market:
        return None
    end = market.get("endDate") or market.get("endDateIso") or market.get("end_date")
    if not end:
        return None
    try:
        end_dt = datetime.fromisoformat(end.replace("Z", "+00:00"))
        now_dt = datetime.now(timezone.utc)
        return (end_dt - now_dt).total_seconds() / 86400
    except Exception:
        return None


SPORT_KEYWORDS = [
    "soccer", "futbol", "fútbol", "football", "premier league", "champions league",
    "la liga", "serie a", "bundesliga", "mls", "libertadores", "sudamericana",
    "dota", "cs2", "csgo", "counter-strike", "counter strike",
    "league of legends", "lol:", "valorant",
    "esports", "e-sports",
    "baseball", "mlb",
    "nba", "basketball",
    "nfl",
    "nhl", "hockey",
    "tennis", "atp", "wta",
    "cricket",
]


def is_sports_market(market):
    """Detecta si un mercado es de deportes/esports. Polymarket marca
    internamente los mercados deportivos con un campo 'sports' — si está
    presente, es 100% seguro que es deporte, sin importar el idioma del
    título o de qué liga se trate (esto es lo que hacía que ligas de
    fútbol fuera de las 5-6 grandes que tenía a mano, como el Brasileirão,
    se colaran como "no deportivo"). Las etiquetas y palabras clave quedan
    como respaldo por si ese campo no viene en la respuesta."""
    if not market:
        return False
    if market.get("sports"):
        return True
    tags = market.get("tags") or []
    for t in tags:
        label = (t.get("label") or t.get("slug") or "") if isinstance(t, dict) else str(t)
        label = label.lower()
        if label in ("sports", "esports", "e-sports") or any(k in label for k in SPORT_KEYWORDS):
            return True
    text = f"{market.get('title','')} {market.get('slug','')}".lower()
    return any(k in text for k in SPORT_KEYWORDS)


def market_result(market, outcome):
    if not market or not market.get("closed"):
        return "open" if market else None
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


# ---------- selección de los 5 vigilados por % de rendimiento, ----------
# ---------- pero solo entre los que de verdad operan en corto plazo -----
def get_leaderboard_period(period):
    r = requests.get(
        f"{DATA_API}/v1/leaderboard",
        params={"category": LB_CATEGORY, "timePeriod": period, "orderBy": "PNL", "limit": TOP_N_CANDIDATES},
        timeout=15,
    )
    r.raise_for_status()
    return r.json()


def get_alltime_profitable_wallets(limit=ALLTIME_TOP_N):
    """Trae el ranking histórico completo (toda la vida en Polymarket, no
    solo semana/mes) y devuelve el set de wallets que aparecen ahí — es
    decir, gente con ganancia neta sostenida a largo plazo, no solo una
    buena racha reciente. Alguien como texaskid (-74.9% de ROI histórico)
    nunca aparecería acá, aunque haya tenido un mes espectacular.
    Devuelve None si la consulta falla, para no bloquear a todo el mundo
    por un error de red pasajero."""
    try:
        r = requests.get(
            f"{DATA_API}/v1/leaderboard",
            params={"category": LB_CATEGORY, "timePeriod": "ALL", "orderBy": "PNL", "limit": limit},
            timeout=15,
        )
        r.raise_for_status()
        return {(t.get("proxyWallet") or "").lower() for t in r.json() if t.get("proxyWallet")}
    except Exception as e:
        print(f"Error trayendo ranking histórico (ALL): {e}", file=sys.stderr)
        return None


def get_recent_trades(wallet, limit=ACTIVITY_SAMPLE_SIZE):
    try:
        r = requests.get(
            f"{DATA_API}/activity",
            params={"user": wallet, "limit": limit, "type": "TRADE"},
            timeout=10,
        )
        return r.json() if r.ok else []
    except Exception:
        return []


def short_term_trade_ratio(wallet):
    """Mira las últimas apuestas reales de la wallet y calcula qué % de
    ellas fueron en deportes/esports Y en mercados que resolvían en
    MAX_DAYS_TO_RESOLUTION días o menos desde el momento en que apostó.
    Devuelve None si no hay datos suficientes para opinar."""
    acts = get_recent_trades(wallet)
    if not acts:
        return None
    short, counted = 0, 0
    for a in acts:
        slug = a.get("slug")
        ts = a.get("timestamp")
        if not slug or not ts:
            continue
        market = get_market(slug)
        if not market:
            continue
        end = market.get("endDate") or market.get("endDateIso") or market.get("end_date")
        if not end:
            continue
        try:
            end_dt = datetime.fromisoformat(end.replace("Z", "+00:00"))
            trade_dt = datetime.fromtimestamp(ts, tz=timezone.utc)
            days = (end_dt - trade_dt).total_seconds() / 86400
        except Exception:
            continue
        counted += 1
        if days <= MAX_DAYS_TO_RESOLUTION and is_sports_market(market):
            short += 1
    if counted == 0:
        return None
    return short / counted


def compute_top5_by_roi():
    """Junta candidatos de semana+mes (por PnL en $, igual que el bot de
    alertas), descarta a los de portafolio muy chico (artefacto de %), a
    los que no operan mayormente en corto plazo, y a los que no tienen un
    historial ganador sostenido a largo plazo (evita casos como texaskid:
    buen mes puntual viniendo de un historial muy negativo). De los que
    quedan, se queda con los 5 mejores por % de rendimiento reciente."""
    candidates = {}
    for period in LB_PERIODS:
        try:
            for t in get_leaderboard_period(period):
                w = (t.get("proxyWallet") or "").lower()
                if not w:
                    continue
                candidates.setdefault(w, t)
        except Exception as e:
            print(f"Error trayendo ranking de {period}: {e}", file=sys.stderr)

    alltime_ok = get_alltime_profitable_wallets()

    scored = []
    for w, t in candidates.items():
        pnl = t.get("pnl")
        value = get_portfolio_value(w)
        if pnl is None or not value or value < MIN_WHALE_PORTFOLIO:
            continue  # portafolio casi vacío -> el % se dispara sin ser real habilidad, se descarta

        if alltime_ok is not None and w not in alltime_ok:
            continue  # buen mes/semana puntual, pero sin historial ganador sostenido a largo plazo

        ratio = short_term_trade_ratio(w)
        if ratio is None or ratio < MIN_SHORT_TERM_SHARE:
            continue  # no opera mayormente en mercados de corto plazo, no nos sirve para este bot

        roi_pct = pnl / value * 100
        scored.append((w, t.get("userName", "anon"), roi_pct, ratio))

    scored.sort(key=lambda x: x[2], reverse=True)
    return scored[:TOP_K_REPLICATE]


# ---------- reporte ----------
def max_drawdown_pct():
    peak = INITIAL_BANKROLL
    worst = 0.0
    for h in bankroll_history:
        peak = max(peak, h["bankroll"])
        dd = (peak - h["bankroll"]) / peak * 100 if peak > 0 else 0
        worst = max(worst, dd)
    return worst


def build_summary_md():
    per_wallet = {}
    for tr in trades:
        w = tr["wallet"]
        per_wallet.setdefault(w, {"username": tr["username"], "won": 0, "lost": 0, "pending": 0, "pnl_usd": 0.0})
        if tr["status"] == "won" or (tr["status"] == "cerrada_venta" and tr.get("profit_usd", 0.0) >= 0):
            per_wallet[w]["won"] += 1
            per_wallet[w]["pnl_usd"] += tr.get("profit_usd", 0.0)
        elif tr["status"] == "lost" or (tr["status"] == "cerrada_venta" and tr.get("profit_usd", 0.0) < 0):
            per_wallet[w]["lost"] += 1
            per_wallet[w]["pnl_usd"] += tr.get("profit_usd", 0.0)
        else:
            per_wallet[w]["pending"] += 1

    total_return_pct = (bankroll - INITIAL_BANKROLL) / INITIAL_BANKROLL * 100

    # coincidencias: mismo mercado, 2+ vigilados, dentro de las últimas 24h
    overlaps = {}
    for tr in trades:
        key = tr["slug"]
        overlaps.setdefault(key, set()).add(tr["username"])
    overlap_markets = {k: v for k, v in overlaps.items() if len(v) > 1}

    hora_peru = time.gmtime(time.time() - 5 * 3600)
    lines = [
        "# Paper trading — resultado de la simulación",
        "",
        f"Actualizado: {time.strftime('%Y-%m-%d %H:%M:%S', hora_peru)} (hora de Perú)",
        "",
        f"**Bankroll inicial:** ${INITIAL_BANKROLL:,.2f}",
        f"**Bankroll actual:** ${bankroll:,.2f}",
        f"**Retorno acumulado:** {total_return_pct:+.2f}%",
        f"**Peor caída desde un máximo (drawdown):** {max_drawdown_pct():.2f}%",
        "",
        "_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._",
        "",
        "## Por vigilado",
        "",
        "| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |",
        "|---|---|---|---|---|",
    ]
    for w, d in sorted(per_wallet.items(), key=lambda kv: -kv[1]["pnl_usd"]):
        lines.append(f"| {d['username']} | {d['won']} | {d['lost']} | {d['pending']} | {d['pnl_usd']:+,.2f} USD |")

    lines += ["", "## Mercados donde coincidieron 2+ vigilados (para calibrar el tope futuro)", ""]
    if overlap_markets:
        lines.append("| Mercado | Vigilados que coincidieron |")
        lines.append("|---|---|")
        for slug, names in overlap_markets.items():
            lines.append(f"| {slug} | {', '.join(sorted(names))} |")
    else:
        lines.append("_Todavía no hubo coincidencias._")

    lines += ["", "## Últimas 30 apuestas de papel (detalle)", "",
               "| Apostador | Mercado | Apostó a | Precio | Stake ($) | Estado | Resultado |",
               "|---|---|---|---|---|---|---|"]
    for tr in sorted(trades, key=lambda t: t["timestamp_added"], reverse=True)[:30]:
        estado = {"pending": "⏳ pendiente", "won": "✅ ganada", "lost": "❌ perdida",
                  "cerrada_venta": "💰 vendida anticipada"}.get(tr["status"], tr["status"])
        resultado = f"{tr['profit_usd']:+,.2f}" if tr["status"] != "pending" else "—"
        titulo = (tr.get("title") or "(sin título)")[:40]
        lines.append(
            f"| {tr.get('username','')} | {titulo} | {tr.get('outcome','')} ({tr.get('side','')}) | "
            f"{tr.get('odds_at_bet',0)}% | {tr.get('paper_stake_usd',0):,.2f} | {estado} | {resultado} |"
        )

    SUMMARY_FILE.write_text("\n".join(lines) + "\n")


def send_telegram(text):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json={"chat_id": TELEGRAM_CHAT_ID, "text": text, "disable_web_page_preview": True},
            timeout=10,
        )
    except Exception as e:
        print(f"Error mandando a Telegram: {e}", file=sys.stderr)


# ---------- registrar y resolver posiciones de papel ----------
def log_paper_trade(username, wallet, trade, whale_usd, whale_pct, paper_stake, odds, recortado=False):
    global trades_dirty
    slug = trade.get("slug")
    same_day_others = sorted({
        tr["username"] for tr in trades
        if tr["slug"] == slug and tr["username"] != username
        and time.time() - tr["timestamp_added"] < 86400
    })
    with lock:
        trades.append({
            "timestamp": trade.get("timestamp"),
            "timestamp_added": time.time(),
            "username": username,
            "wallet": wallet,
            "slug": slug or "",
            "title": trade.get("title") or "(sin título)",
            "outcome": trade.get("outcome") or "",
            "side": trade.get("side") or "",
            "whale_usd": whale_usd,
            "whale_pct": round(whale_pct, 3),
            "paper_stake_usd": round(paper_stake, 2),
            "odds_at_bet": odds,
            "status": "pending",
            "profit_usd": 0.0,
            "overlaps_with": same_day_others,
            "recortado_por_bankroll": recortado,
            "last_fill_at": time.time(),
            "fills": 1,
        })
        trades_dirty = True

    aviso = f"🧪 PAPER — {username} apostó {whale_pct:.2f}% de su portafolio\n"
    aviso += f"Réplica simulada: ${paper_stake:,.2f}\n"
    aviso += f"Mercado: {trade.get('title','')}\n"
    aviso += f"Apuesta a: {trade.get('outcome','')} ({trade.get('side','')})\n"
    aviso += f"Precio al momento de apostar: {odds}%\n"
    if recortado:
        aviso += "⚠️ Recortado: no había suficiente bankroll disponible para replicar el % completo\n"
    if same_day_others:
        aviso += f"⚠️ Coincide hoy con: {', '.join(same_day_others)}\n"
    send_telegram(aviso)


def resolve_pending_trades():
    global trades_dirty, bankroll
    with lock:
        pending = [tr for tr in trades if tr["status"] == "pending"]
    if pending:
        print(f"[resolver] revisando {len(pending)} posiciones pendientes...")
    for tr in pending:
        market = get_market(tr["slug"])
        result = market_result(market, tr["outcome"])
        if result not in ("won", "lost"):
            if market is None:
                print(f"  ⚠ {tr['slug']}: no se pudo consultar el mercado (posible error de red o slug incorrecto)")
            elif not market.get("closed"):
                print(f"  … {tr['slug']}: todavía abierto/sin resolver en Polymarket")
            else:
                print(f"  ⚠ {tr['slug']}: cerrado pero no pude determinar won/lost para el outcome '{tr['outcome']}' — revisar formato de outcomes/outcomePrices")
            time.sleep(0.1)
            continue
        stake = tr["paper_stake_usd"]
        odds = tr["odds_at_bet"] / 100.0  # precio 0-1 al momento de apostar
        if result == "won" and odds > 0:
            profit = stake * (1 - odds) / odds
        else:
            profit = -stake
        with lock:
            tr["status"] = result
            tr["profit_usd"] = round(profit, 2)
            bankroll += profit
            bankroll_history.append({
                "timestamp": time.time(),
                "bankroll": round(bankroll, 2),
                "event": f"{result}: {tr['username']} — {tr['title']}",
            })
        trades_dirty = True
        time.sleep(0.1)


# ---------- websocket en vivo (idéntico patrón al bot de alertas) ----------
def on_ws_open(ws):
    global last_msg_at
    last_msg_at = time.time()
    print("[paper] conectado — escuchando trades de los 5 vigilados por % de rendimiento")
    ws.send(json.dumps({"action": "subscribe", "subscriptions": [{"topic": "activity", "type": "trades"}]}))


def close_position_early(username, wallet, trade, sell_price_pct):
    """Cuando la ballena vende (SELL), busca las posiciones de papel
    pendientes que tengamos abiertas para esa misma wallet+mercado+resultado
    y las cierra YA, al precio actual — igual que hace la ballena en la
    vida real al tomar ganancia (o cortar pérdida) antes de que el mercado
    resuelva."""
    global bankroll, trades_dirty
    slug = trade.get("slug")
    outcome = trade.get("outcome")
    with lock:
        abiertas = [tr for tr in trades if tr["status"] == "pending" and tr["wallet"] == wallet
                    and tr["slug"] == slug and tr["outcome"] == outcome]
        if not abiertas:
            return False
        total_profit = 0.0
        for tr in abiertas:
            entry = tr["odds_at_bet"] / 100.0
            stake = tr["paper_stake_usd"]
            profit = stake * (sell_price_pct / 100.0 / entry - 1) if entry > 0 else -stake
            tr["status"] = "cerrada_venta"
            tr["profit_usd"] = round(profit, 2)
            tr["closed_price"] = sell_price_pct
            total_profit += profit
        bankroll += total_profit
        bankroll_history.append({
            "timestamp": time.time(),
            "bankroll": round(bankroll, 2),
            "event": f"venta anticipada: {username} — {trade.get('title')} ({total_profit:+.2f} USD)",
        })
        trades_dirty = True
    print(f"🧪 PAPER — {username}: VENDE y cierra {len(abiertas)} posición(es) de papel en "
          f"{trade.get('title')} al {sell_price_pct}% -> {total_profit:+,.2f} USD")
    send_telegram(f"🧪 PAPER — {username} vendió (toma ganancia/corta pérdida)\n"
                   f"Cerramos la réplica en {trade.get('title')} — {trade.get('outcome')}\n"
                   f"Resultado: {total_profit:+,.2f} USD")
    return True


def on_ws_message(ws, message):
    global last_msg_at, msg_count
    last_msg_at = time.time()
    if message == "PONG":
        return
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

    msg_count += 1
    if not wallet or wallet not in watched:
        return

    key = f"{trade.get('transactionHash','')}_{trade.get('timestamp')}_{trade.get('asset')}_{trade.get('size')}"
    if key in seen_keys:
        return
    seen_keys.add(key)
    if len(seen_keys) > 5000:
        seen_keys.clear()

    username = watched.get(wallet, "anon")
    odds = round((trade.get("price") or 0) * 100)
    side = (trade.get("side") or "").upper()

    # SELL: no abre nada nuevo, intenta cerrar lo que ya teníamos replicado
    if side == "SELL":
        cerro_algo = close_position_early(username, wallet, trade, odds)
        if not cerro_algo:
            print(f"🧪 PAPER — {username}: vendió en {trade.get('title')} pero no teníamos "
                  f"posición de papel abierta ahí — se ignora")
        return

    # BUY: sigue la lógica de siempre, abrir una posición de papel nueva
    whale_usd = (trade.get("size") or 0) * (trade.get("price") or 0)
    whale_value = get_portfolio_value(wallet)
    if not whale_value or whale_value <= 0:
        return
    whale_pct = whale_usd / whale_value * 100
    if whale_pct < MIN_TRADE_PCT:
        return  # apuesta demasiado chica para el propio portafolio del vigilado, se ignora como ruido

    market = get_market(trade.get("slug"))
    days_left = days_to_resolution(market)
    if days_left is not None and days_left > MAX_DAYS_TO_RESOLUTION:
        print(f"🧪 PAPER — {username}: se ignora, el mercado resuelve en ~{days_left:.0f} días "
              f"(más del límite de {MAX_DAYS_TO_RESOLUTION:.0f}) — {trade.get('title')}")
        return
    if not is_sports_market(market):
        print(f"🧪 PAPER — {username}: se ignora, no es un mercado de deportes/esports — {trade.get('title')}")
        return

    merge_or_open_position(username, wallet, trade, whale_usd, whale_pct, odds)


def merge_or_open_position(username, wallet, trade, whale_usd, whale_pct, odds):
    """Si la misma ballena ya tiene una compra reciente (dentro de
    FILL_MERGE_WINDOW_SECONDS) en el mismo mercado+resultado, la suma a esa
    posición en vez de abrir una nueva — así una compra grande que Polymarket
    ejecuta en varios pedacitos no compite contra sí misma por el bankroll
    disponible."""
    global trades_dirty
    slug = trade.get("slug")
    outcome = trade.get("outcome")
    now = time.time()

    with lock:
        existente = next((tr for tr in trades if tr["status"] == "pending" and tr["wallet"] == wallet
                           and tr["slug"] == slug and tr["outcome"] == outcome and tr.get("side") == "BUY"
                           and now - tr.get("last_fill_at", tr["timestamp_added"]) < FILL_MERGE_WINDOW_SECONDS), None)
        allocated = sum(tr["paper_stake_usd"] for tr in trades if tr["status"] == "pending")

    if existente:
        combined_whale_usd = existente["whale_usd"] + whale_usd
        whale_value = get_portfolio_value(wallet)
        combined_pct = combined_whale_usd / whale_value * 100 if whale_value else whale_pct
        desired_total = combined_pct / 100 * bankroll
        available = max(0.0, bankroll - allocated)
        faltante = max(0.0, desired_total - existente["paper_stake_usd"])
        adicional = min(faltante, available)
        nuevo_stake_total = existente["paper_stake_usd"] + adicional
        nuevo_odds = odds
        if nuevo_stake_total > 0:
            nuevo_odds = round((existente["paper_stake_usd"] * existente["odds_at_bet"] + adicional * odds) / nuevo_stake_total)
        with lock:
            existente["paper_stake_usd"] = round(nuevo_stake_total, 2)
            existente["whale_usd"] = combined_whale_usd
            existente["whale_pct"] = round(combined_pct, 3)
            existente["odds_at_bet"] = nuevo_odds
            existente["last_fill_at"] = now
            existente["fills"] = existente.get("fills", 1) + 1
            if adicional < faltante:
                existente["recortado_por_bankroll"] = True
            trades_dirty = True
        print(f"🧪 PAPER — {username}: fill adicional fusionado en {trade.get('title')} "
              f"(+${adicional:,.2f}, total ${nuevo_stake_total:,.2f}, {existente['fills']} fills)")
        return

    with lock:
        available = max(0.0, bankroll - allocated)
    desired_stake = whale_pct / 100 * bankroll
    recortado = desired_stake > available
    paper_stake = min(desired_stake, available)

    if paper_stake <= 0:
        print(f"🧪 PAPER — {username}: se ignora, no queda bankroll disponible "
              f"(${allocated:,.2f} ya comprometidos en posiciones pendientes)")
        return

    nota = " [recortado por falta de bankroll disponible]" if recortado else ""
    print(f"🧪 PAPER — {username}: {whale_pct:.2f}% -> ${paper_stake:,.2f} en {trade.get('title')}{nota}")
    log_paper_trade(username, wallet, trade, whale_usd, whale_pct, paper_stake, odds, recortado)


def on_ws_error(ws, error):
    print(f"[paper] error de conexión: {error}", file=sys.stderr)


def on_ws_close(ws, code, msg):
    print("[paper] conexión cerrada, reconectando...")


# ---------- hilo de fondo ----------
def save_and_commit():
    global trades_dirty
    try:
        with lock:
            TRADES_FILE.write_text(json.dumps(trades, indent=2))
            STATE_FILE.write_text(json.dumps({"bankroll": bankroll, "history": bankroll_history}, indent=2))
            build_summary_md()
            WATCHED_FILE.write_text(json.dumps(watched_meta, indent=2))
        os.system('git config user.name "whale-copy-paper-bot"')
        os.system('git config user.email "actions@github.com"')
        os.system("git add paper_trades.json paper_state.json paper_summary.md paper_watched.json")
        os.system('git diff --staged --quiet || git commit -m "actualizar simulación de paper trading"')

        for intento in range(3):
            push_ok = os.system("git push") == 0
            if push_ok:
                break
            print(f"[save_and_commit] push rechazado (intento {intento+1}/3), "
                  f"bajando cambios ajenos y quedándonos con nuestra versión de los paper_* si hay choque...",
                  file=sys.stderr)
            os.system("git fetch origin main")
            # Usamos merge (no rebase) con estrategia "ours" para los hunks
            # que choquen: como los archivos paper_* se recalculan enteros
            # desde la memoria en cada ciclo, no hay nada que perder
            # prefiriendo siempre nuestra versión más reciente si hay un
            # conflicto real de contenido (por ejemplo, si quedó una
            # corrida vieja del mismo bot corriendo en paralelo).
            merge_ok = os.system('git merge --no-edit -X ours origin/main') == 0
            if not merge_ok:
                os.system("git merge --abort")
                print("[save_and_commit] no se pudo fusionar automáticamente, se reintenta en el próximo ciclo",
                      file=sys.stderr)
                break
        trades_dirty = False
    except Exception as e:
        import traceback
        print(f"[save_and_commit] error al guardar, se reintenta en el próximo ciclo: {e}", file=sys.stderr)
        traceback.print_exc()


def ranking_worker():
    """Hilo aparte para el análisis pesado (revisar el historial de cada
    candidato). Corre en su propio ciclo y JAMÁS bloquea el guardado de
    archivos, aunque tarde varios minutos en completar una vuelta."""
    last_lb_refresh = 0
    while not stop_flag.is_set():
        try:
            now = time.time()
            if now - last_lb_refresh > LEADERBOARD_REFRESH_SECONDS or not watched:
                print("[ranking] arrancando análisis de candidatos (puede tardar varios minutos)...")
                top5 = compute_top5_by_roi()
                cutoff = time.time() - MIN_WATCH_DAYS * 86400
                with lock:
                    current_wallets = {w for w, _, _, _ in top5}
                    for w, name, roi, ratio in top5:
                        if w not in watched_meta:
                            watched_meta[w] = {"username": name, "added_at": time.time(), "roi_pct": round(roi, 2),
                                                "short_term_pct": round(ratio * 100, 1)}
                        else:
                            watched_meta[w]["username"] = name
                            watched_meta[w]["roi_pct"] = round(roi, 2)
                            watched_meta[w]["short_term_pct"] = round(ratio * 100, 1)
                    for w in list(watched_meta.keys()):
                        if w not in current_wallets and watched_meta[w]["added_at"] < cutoff:
                            del watched_meta[w]
                    watched.clear()
                    watched.update({w: m["username"] for w, m in watched_meta.items()})
                print(f"[ranking] top {TOP_K_REPLICATE} por %% de rendimiento (corto plazo): "
                      + ", ".join(f"{m['username']} ({m['roi_pct']:+.1f}%, {m['short_term_pct']:.0f}% corto plazo)"
                                  for m in watched_meta.values()))
                last_lb_refresh = time.time()
        except Exception as e:
            import traceback
            print(f"[ranking_worker] error, se ignora y se reintenta en el próximo ciclo: {e}", file=sys.stderr)
            traceback.print_exc()
        time.sleep(10)


def background_worker():
    """Hilo liviano: guarda, resuelve apuestas pendientes y cuida la
    conexión. Corre siempre a tiempo, sin depender de lo que tarde el
    análisis de ranking (ese vive en ranking_worker, aparte)."""
    global last_msg_at
    last_resolve_check = 0
    last_save = time.time()
    while not stop_flag.is_set():
        try:
            now = time.time()

            if now - last_resolve_check > 60:
                resolve_pending_trades()
                last_resolve_check = now

            if now - last_msg_at > 60 and current_ws is not None:
                try:
                    current_ws.close()
                except Exception:
                    pass
                last_msg_at = time.time()

            if now - last_save > 120:
                save_and_commit()
                last_save = now

            # Si ya se cumplió el tiempo máximo de corrida, forzamos el cierre
            # del websocket para que el hilo principal salga de run_forever()
            # y el bot pueda terminar prolijo (guardar todo) en vez de que
            # GitHub lo mate de un tirón sin guardar nada.
            if now - run_start > MAX_RUNTIME_SECONDS and current_ws is not None:
                print("[paper] tiempo máximo alcanzado, cerrando para terminar prolijo...")
                try:
                    current_ws.close()
                except Exception:
                    pass
                stop_flag.set()

        except Exception as e:
            import traceback
            print(f"[background_worker] error en un ciclo, se ignora y se sigue: {e}", file=sys.stderr)
            traceback.print_exc()

        time.sleep(5)


def main():
    global bankroll
    state = load_json(STATE_FILE)
    if state:
        bankroll = state.get("bankroll", INITIAL_BANKROLL)
        bankroll_history.extend(state.get("history", []))
        print(f"[paper] bankroll cargado: ${bankroll:,.2f}")

    loaded_trades = load_json(TRADES_FILE, [])
    trades.extend(loaded_trades)

    loaded_watched = load_json(WATCHED_FILE, {})
    watched_meta.update(loaded_watched)
    watched.update({w: m["username"] for w, m in watched_meta.items()})

    if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
        send_telegram(f"✅ Paper trading bot conectado — bankroll simulado: ${bankroll:,.2f}")

    bg = threading.Thread(target=background_worker, daemon=True)
    bg.start()
    rk = threading.Thread(target=ranking_worker, daemon=True)
    rk.start()

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
        print("[paper] reintentando conexión en 5s...")
        time.sleep(5)

    stop_flag.set()
    resolve_pending_trades()
    save_and_commit()
    print("Ciclo terminado — GitHub va a arrancar uno nuevo con el cron.")


if __name__ == "__main__":
    main()
