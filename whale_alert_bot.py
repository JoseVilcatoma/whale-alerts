"""
whale_alert_bot.py — versión "en vivo" (websocket), enfocada 100% en velocidad

Se conecta al chorro en vivo de TODAS las apuestas de Polymarket y avisa al
instante apenas alguno de los vigilados (top del ranking, semana + mes
combinados) hace una apuesta fuerte. Sin análisis extra que pueda demorar
nada — la prioridad acá es la velocidad.

Variables de entorno (se configuran en el workflow / como Secrets):
  NTFY_TOPIC                   - nombre de tu canal de ntfy (obligatorio)
  WHALE_THRESHOLD              - monto mínimo en USD para avisar (default: 1000)
  TOP_N                        - a cuántos de CADA período vigilar (default: 20)
  LB_CATEGORY                  - OVERALL, SPORTS, POLITICS, CRYPTO, ESPORTS,
                                  CULTURE, ECONOMICS (default: OVERALL)
  LEADERBOARD_REFRESH_SECONDS  - cada cuánto refresca la lista de vigilados
                                  (default: 900)
  MAX_RUNTIME_SECONDS          - cuándo cortar solo, antes que lo corte GitHub
                                  (default: 21000 = 5h50m)
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

# --- Arreglo para "Network is unreachable" en GitHub Actions ---
def _allowed_gai_family():
    return socket.AF_INET

urllib3_cn.allowed_gai_family = _allowed_gai_family

DATA_API = "https://data-api.polymarket.com"
GAMMA_API = "https://gamma-api.polymarket.com"
RTDS_URL = "wss://ws-live-data.polymarket.com"
RESULTS_FILE = Path(__file__).parent / "results.json"
SUMMARY_FILE = Path(__file__).parent / "results.md"

NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "").strip()
WHALE_THRESHOLD = float(os.environ.get("WHALE_THRESHOLD", "1000"))
TOP_N = int(os.environ.get("TOP_N", "20"))
LB_CATEGORY = os.environ.get("LB_CATEGORY", "OVERALL")
LB_PERIODS = ["WEEK", "MONTH"]

LEADERBOARD_REFRESH_SECONDS = int(os.environ.get("LEADERBOARD_REFRESH_SECONDS", "900"))
MAX_RUNTIME_SECONDS = int(os.environ.get("MAX_RUNTIME_SECONDS", str(5 * 3600 + 50 * 60)))

watched = {}          # wallet (minúsculas) -> username
msg_count = 0
raw_samples_shown = 0
seen_keys = set()      # dedupe de trades ya alertados en esta corrida
lock = threading.Lock()
run_start = time.time()
stop_flag = threading.Event()

results = []           # cada apuesta que alertamos: {..., "status": "pending"/"won"/"lost"}
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


def log_result_pending(username, wallet, trade, usd, odds):
    global results_dirty
    with lock:
        results.append({
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
    """Revisa las pendientes contra Polymarket y marca ganó/perdió si ya resolvieron."""
    global results_dirty
    changed = False
    with lock:
        pending = [r for r in results if r["status"] == "pending"]
    for r in pending:
        market = get_market(r["slug"])
        outcome = market_result(market, r["outcome"])
        if outcome in ("won", "lost"):
            with lock:
                r["status"] = outcome
            changed = True
        time.sleep(0.1)  # prudencia con la API pública
    if changed:
        results_dirty = True


def build_summary_md():
    per_wallet = {}
    for r in results:
        w = r["wallet"]
        per_wallet.setdefault(w, {"username": r["username"], "won": 0, "lost": 0, "pending": 0})
        if r["status"] == "won":
            per_wallet[w]["won"] += 1
        elif r["status"] == "lost":
            per_wallet[w]["lost"] += 1
        else:
            per_wallet[w]["pending"] += 1

    rows = []
    for w, d in per_wallet.items():
        total_resolved = d["won"] + d["lost"]
        pct = round(d["won"] / total_resolved * 100) if total_resolved else None
        rows.append((d["username"], d["won"], d["lost"], d["pending"], pct))
    rows.sort(key=lambda x: (x[4] is None, -(x[4] or 0)))

    lines = [
        "# Resultados de las apuestas fuertes alertadas",
        "",
        f"Actualizado: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}",
        "",
        "| Apostador | Ganadas | Perdidas | Pendientes | % Acierto |",
        "|---|---|---|---|---|",
    ]
    for username, won, lost, pending, pct in rows:
        pct_str = f"{pct}%" if pct is not None else "—"
        lines.append(f"| {username} | {won} | {lost} | {pending} | {pct_str} |")
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
    value = get_portfolio_value(wallet)
    if not value or value <= 0:
        return ""
    pct = usd / value * 100
    return f"💰 Stake: {pct:.1f}% de su portafolio (${value:,.0f} total)\n"


def build_ticket(username, trade, usd, odds, wallet):
    return (
        f"🐋 {username} — nueva apuesta fuerte\n\n"
        f"🎟️ TICKET DE APUESTA\n"
        f"Apostador: {username}\n"
        f"Acción: {'COMPRA' if trade.get('side') == 'BUY' else 'VENTA'} — \"{trade.get('outcome','')}\"\n"
        f"Mercado: {trade.get('title','')}\n"
        f"Monto: ${usd:,.0f}\n"
        f"Cuota: {odds}%\n"
        f"{stake_line(usd, wallet)}"
        f"Operar: {market_url(trade)}"
    )


def send_ntfy(text):
    if not NTFY_TOPIC:
        return
    try:
        requests.post(f"https://ntfy.sh/{NTFY_TOPIC}", data=text.encode("utf-8"), timeout=10)
    except Exception as e:
        print(f"Error mandando a ntfy: {e}", file=sys.stderr)


# ---------- websocket en vivo ----------
def on_ws_open(ws):
    print("[en vivo] conectado — escuchando todas las apuestas de Polymarket")
    ws.send(json.dumps({
        "action": "subscribe",
        "subscriptions": [{"topic": "activity", "type": "trades"}]
    }))


def on_ws_message(ws, message):
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

    if not wallet or wallet not in watched:
        return
    print(f"[match] {watched.get(wallet)} hizo una apuesta (revisando monto...)")

    key = f"{trade.get('transactionHash','')}_{trade.get('timestamp')}_{trade.get('asset')}_{trade.get('size')}"
    if key in seen_keys:
        return
    seen_keys.add(key)
    if len(seen_keys) > 5000:
        seen_keys.clear()

    usd = (trade.get("size") or 0) * (trade.get("price") or 0)
    if usd < WHALE_THRESHOLD:
        return

    username = watched.get(wallet, "anon")
    odds = round((trade.get("price") or 0) * 100)
    print(f"🐋 EN VIVO — {username}: ${usd:,.0f} en {trade.get('title')}")
    send_ntfy(build_ticket(username, trade, usd, odds, wallet))
    log_result_pending(username, wallet, trade, usd, odds)


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
    os.system('git config user.name "whale-alert-bot"')
    os.system('git config user.email "actions@github.com"')
    os.system("git add results.json results.md")
    os.system('git diff --staged --quiet || git commit -m "actualizar resultados"')
    os.system("git push")
    results_dirty = False


def background_worker():
    last_lb_refresh = 0
    last_heartbeat = time.time()
    last_resolve_check = 0
    last_save = time.time()
    while not stop_flag.is_set():
        now = time.time()
        if now - last_lb_refresh > LEADERBOARD_REFRESH_SECONDS or not watched:
            combined = get_combined_leaderboard()
            with lock:
                watched.clear()
                watched.update({w.lower(): t.get("userName", "anon") for w, t in combined.items()})
            print(f"[ranking] {len(watched)} apostadores vigilados: {list(watched.values())}")
            last_lb_refresh = now
        if now - last_heartbeat > 120:
            print(f"[heartbeat] mensajes recibidos del chorro hasta ahora: {msg_count}")
            last_heartbeat = now
        if now - last_resolve_check > 180:
            resolve_pending_results()
            last_resolve_check = now
        if results_dirty and now - last_save > 300:
            print("[resultados] guardando progreso en el repo...")
            save_and_commit_results()
            last_save = now
        time.sleep(5)


def main():
    loaded = load_json(RESULTS_FILE)
    if loaded:
        results.extend(loaded)
        print(f"[resultados] cargados {len(results)} registros anteriores")

    if not NTFY_TOPIC:
        print("¡Falta NTFY_TOPIC! No va a poder avisar nada.", file=sys.stderr)
    else:
        print(f"[ntfy] mandando push de prueba al canal '{NTFY_TOPIC}'...")
        send_ntfy(f"✅ Whale Alerts bot conectado\n\nSi ves este mensaje en tu celular, el canal ntfy '{NTFY_TOPIC}' funciona bien. Las próximas apuestas fuertes de los vigilados van a llegar acá.")

    bg = threading.Thread(target=background_worker, daemon=True)
    bg.start()

    while not watched and time.time() - run_start < 60:
        time.sleep(1)

    ws = websocket.WebSocketApp(
        RTDS_URL, on_open=on_ws_open, on_message=on_ws_message,
        on_error=on_ws_error, on_close=on_ws_close,
    )

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
