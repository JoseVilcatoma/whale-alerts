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

import requests
import websocket
import urllib3.util.connection as urllib3_cn

# --- Arreglo para "Network is unreachable" en GitHub Actions ---
def _allowed_gai_family():
    return socket.AF_INET

urllib3_cn.allowed_gai_family = _allowed_gai_family

DATA_API = "https://data-api.polymarket.com"
RTDS_URL = "wss://ws-live-data.polymarket.com"

NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "").strip()
WHALE_THRESHOLD = float(os.environ.get("WHALE_THRESHOLD", "1000"))
TOP_N = int(os.environ.get("TOP_N", "20"))
LB_CATEGORY = os.environ.get("LB_CATEGORY", "OVERALL")
LB_PERIODS = ["WEEK", "MONTH"]

LEADERBOARD_REFRESH_SECONDS = int(os.environ.get("LEADERBOARD_REFRESH_SECONDS", "900"))
MAX_RUNTIME_SECONDS = int(os.environ.get("MAX_RUNTIME_SECONDS", str(5 * 3600 + 50 * 60)))

watched = {}          # wallet (minúsculas) -> username
msg_count = 0
seen_keys = set()      # dedupe de trades ya alertados en esta corrida
lock = threading.Lock()
run_start = time.time()
stop_flag = threading.Event()


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


def build_ticket(username, trade, usd, odds):
    return (
        f"🐋 {username} — nueva apuesta fuerte\n\n"
        f"🎟️ TICKET DE APUESTA\n"
        f"Apostador: {username}\n"
        f"Acción: {'COMPRA' if trade.get('side') == 'BUY' else 'VENTA'} — \"{trade.get('outcome','')}\"\n"
        f"Mercado: {trade.get('title','')}\n"
        f"Monto: ${usd:,.0f}\n"
        f"Cuota: {odds}%\n"
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
    ws.send(json.dumps({"subscriptions": [{"topic": "activity", "type": "trades"}]}))


def on_ws_message(ws, message):
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
    send_ntfy(build_ticket(username, trade, usd, odds))


def on_ws_error(ws, error):
    print(f"[en vivo] error de conexión: {error}", file=sys.stderr)


def on_ws_close(ws, code, msg):
    print("[en vivo] conexión cerrada, reconectando...")


# ---------- hilo de fondo: solo actualiza la lista de vigilados ----------
def background_worker():
    last_lb_refresh = 0
    while not stop_flag.is_set():
        now = time.time()
        if now - last_lb_refresh > LEADERBOARD_REFRESH_SECONDS or not watched:
            combined = get_combined_leaderboard()
            with lock:
                watched.clear()
                watched.update({w.lower(): t.get("userName", "anon") for w, t in combined.items()})
            print(f"[ranking] {len(watched)} apostadores vigilados: {list(watched.values())}")
            last_lb_refresh = now
        time.sleep(5)


def main():
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

    print("Ciclo terminado — GitHub va a arrancar uno nuevo con el cron.")


if __name__ == "__main__":
    main()
