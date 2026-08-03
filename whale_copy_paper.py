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
        r = requests.get(f"{GAMMA_API}/markets/slug/{slug}", timeout=8)
        m = r.json() if r.ok else None
    except Exception:
        m = None
    _market_cache[slug] = (m, time.time())
    return m


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


# ---------- selección de los 5 vigilados por % de rendimiento ----------
def get_leaderboard_period(period):
    r = requests.get(
        f"{DATA_API}/v1/leaderboard",
        params={"category": LB_CATEGORY, "timePeriod": period, "orderBy": "PNL", "limit": TOP_N_CANDIDATES},
        timeout=15,
    )
    r.raise_for_status()
    return r.json()


def compute_top5_by_roi():
    """Junta candidatos de semana+mes (por PnL en $, igual que el bot de
    alertas) y de ahí calcula el % de rendimiento real de cada uno
    (pnl ÷ valor de portafolio) para quedarse con los 5 mejores por %."""
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

    scored = []
    for w, t in candidates.items():
        pnl = t.get("pnl")
        value = get_portfolio_value(w)
        if pnl is None or not value or value < MIN_WHALE_PORTFOLIO:
            continue  # portafolio casi vacío -> el % se dispara sin ser real habilidad, se descarta
        roi_pct = pnl / value * 100
        scored.append((w, t.get("userName", "anon"), roi_pct))

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
        if tr["status"] == "won":
            per_wallet[w]["won"] += 1
            per_wallet[w]["pnl_usd"] += tr.get("profit_usd", 0.0)
        elif tr["status"] == "lost":
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
            "slug": slug,
            "title": trade.get("title"),
            "outcome": trade.get("outcome"),
            "side": trade.get("side"),
            "whale_usd": whale_usd,
            "whale_pct": round(whale_pct, 3),
            "paper_stake_usd": round(paper_stake, 2),
            "odds_at_bet": odds,
            "status": "pending",
            "profit_usd": 0.0,
            "overlaps_with": same_day_others,
            "recortado_por_bankroll": recortado,
        })
        trades_dirty = True

    aviso = f"🧪 PAPER — {username} apostó {whale_pct:.2f}% de su portafolio\n"
    aviso += f"Réplica simulada: ${paper_stake:,.2f}\n"
    aviso += f"Mercado: {trade.get('title','')}\n"
    if recortado:
        aviso += "⚠️ Recortado: no había suficiente bankroll disponible para replicar el % completo\n"
    if same_day_others:
        aviso += f"⚠️ Coincide hoy con: {', '.join(same_day_others)}\n"
    send_telegram(aviso)


def resolve_pending_trades():
    global trades_dirty, bankroll
    with lock:
        pending = [tr for tr in trades if tr["status"] == "pending"]
    for tr in pending:
        market = get_market(tr["slug"])
        result = market_result(market, tr["outcome"])
        if result not in ("won", "lost"):
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

    whale_usd = (trade.get("size") or 0) * (trade.get("price") or 0)
    whale_value = get_portfolio_value(wallet)
    if not whale_value or whale_value <= 0:
        return
    whale_pct = whale_usd / whale_value * 100
    if whale_pct < MIN_TRADE_PCT:
        return  # apuesta demasiado chica para el propio portafolio del vigilado, se ignora como ruido

    username = watched.get(wallet, "anon")
    odds = round((trade.get("price") or 0) * 100)

    with lock:
        allocated = sum(tr["paper_stake_usd"] for tr in trades if tr["status"] == "pending")
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
    with lock:
        TRADES_FILE.write_text(json.dumps(trades, indent=2))
        STATE_FILE.write_text(json.dumps({"bankroll": bankroll, "history": bankroll_history}, indent=2))
        build_summary_md()
        WATCHED_FILE.write_text(json.dumps(watched_meta, indent=2))
    os.system('git config user.name "whale-copy-paper-bot"')
    os.system('git config user.email "actions@github.com"')
    os.system("git add paper_trades.json paper_state.json paper_summary.md paper_watched.json")
    os.system('git diff --staged --quiet || git commit -m "actualizar simulación de paper trading"')
    os.system("git push")
    trades_dirty = False


def background_worker():
    global last_msg_at
    last_lb_refresh = 0
    last_resolve_check = 0
    last_save = time.time()
    while not stop_flag.is_set():
        now = time.time()

        if now - last_lb_refresh > LEADERBOARD_REFRESH_SECONDS or not watched:
            top5 = compute_top5_by_roi()
            cutoff = now - MIN_WATCH_DAYS * 86400
            with lock:
                current_wallets = {w for w, _, _ in top5}
                for w, name, roi in top5:
                    if w not in watched_meta:
                        watched_meta[w] = {"username": name, "added_at": now, "roi_pct": round(roi, 2)}
                    else:
                        watched_meta[w]["username"] = name
                        watched_meta[w]["roi_pct"] = round(roi, 2)
                for w in list(watched_meta.keys()):
                    if w not in current_wallets and watched_meta[w]["added_at"] < cutoff:
                        del watched_meta[w]
                watched.clear()
                watched.update({w: m["username"] for w, m in watched_meta.items()})
            print(f"[ranking] top {TOP_K_REPLICATE} por %% de rendimiento: "
                  + ", ".join(f"{m['username']} ({m['roi_pct']:+.1f}%)" for m in watched_meta.values()))
            last_lb_refresh = now

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
