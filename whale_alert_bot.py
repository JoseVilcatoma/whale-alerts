"""
whale_alert_bot.py — versión en bucle continuo

Vigila a los mejores apostadores combinando el ranking de la SEMANA y el
del MES (sin duplicados), revisando sus apuestas cada pocos segundos.
Pensado para correr dentro de un solo job de GitHub Actions que dura
varias horas, y se reinicia solo (via cron) antes de que GitHub lo corte.

Variables de entorno (se configuran en el workflow / como Secrets):
  NTFY_TOPIC                - nombre de tu canal de ntfy (obligatorio)
  WHALE_THRESHOLD           - monto mínimo en USD para avisar (default: 1000)
  TOP_N                     - a cuántos de CADA período vigilar (default: 10)
  LB_CATEGORY               - OVERALL, SPORTS, POLITICS, CRYPTO, ESPORTS,
                               CULTURE, ECONOMICS (default: OVERALL)
  POLL_SECONDS              - cada cuánto revisa trades nuevos (default: 10)
  LEADERBOARD_REFRESH_SECONDS - cada cuánto refresca el ranking (default: 900)
  SAVE_STATE_EVERY_SECONDS  - cada cuánto guarda progreso (default: 300)
  MAX_RUNTIME_SECONDS       - cuándo cortar solo, antes que lo corte GitHub
                               (default: 21000 = 5h50m)
"""

import json
import os
import socket
import sys
import time
from pathlib import Path

import requests
import urllib3.util.connection as urllib3_cn

# --- Arreglo para "Network is unreachable" en GitHub Actions ---
# Los runners a veces resuelven ntfy.sh/data-api a una dirección IPv6 sin ruta
# real de salida, y la conexión falla antes de intentar por IPv4. Esto fuerza
# a que todas las conexiones salgan por IPv4 únicamente.
def _allowed_gai_family():
    return socket.AF_INET

urllib3_cn.allowed_gai_family = _allowed_gai_family

DATA_API = "https://data-api.polymarket.com"
STATE_FILE = Path(__file__).parent / "state.json"

NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "").strip()
WHALE_THRESHOLD = float(os.environ.get("WHALE_THRESHOLD", "1000"))
TOP_N = int(os.environ.get("TOP_N", "10"))
LB_CATEGORY = os.environ.get("LB_CATEGORY", "OVERALL")
LB_PERIODS = ["WEEK", "MONTH"]  # combinamos ambos, sin duplicados

POLL_SECONDS = int(os.environ.get("POLL_SECONDS", "10"))
LEADERBOARD_REFRESH_SECONDS = int(os.environ.get("LEADERBOARD_REFRESH_SECONDS", "900"))
SAVE_STATE_EVERY_SECONDS = int(os.environ.get("SAVE_STATE_EVERY_SECONDS", "300"))
MAX_RUNTIME_SECONDS = int(os.environ.get("MAX_RUNTIME_SECONDS", str(5 * 3600 + 50 * 60)))


def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            return {}
    return {}


def save_and_commit_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))
    os.system('git config user.name "whale-alert-bot"')
    os.system('git config user.email "actions@github.com"')
    os.system("git add state.json")
    os.system('git diff --staged --quiet || git commit -m "actualizar estado"')
    os.system("git push")


def get_leaderboard_period(period):
    r = requests.get(
        f"{DATA_API}/v1/leaderboard",
        params={"category": LB_CATEGORY, "timePeriod": period, "orderBy": "PNL", "limit": TOP_N},
        timeout=15,
    )
    r.raise_for_status()
    return r.json()


def get_combined_leaderboard():
    """Top de la semana + top del mes, sin duplicar wallets."""
    combined = {}
    for period in LB_PERIODS:
        try:
            for t in get_leaderboard_period(period):
                wallet = t.get("proxyWallet")
                if wallet and wallet not in combined:
                    combined[wallet] = t
        except Exception as e:
            print(f"Error trayendo ranking de {period}: {e}", file=sys.stderr)
    return list(combined.values())


def get_recent_trades(wallet):
    r = requests.get(f"{DATA_API}/trades", params={"user": wallet, "limit": 25}, timeout=15)
    r.raise_for_status()
    return r.json()


def market_url(trade):
    slug = trade.get("eventSlug") or trade.get("slug")
    return f"https://polymarket.com/event/{slug}" if slug else "https://polymarket.com"


def build_ticket(username, trade, usd, odds):
    return (
        f"🐋 {username} — nueva apuesta fuerte\n\n"
        f"🎟️ TICKET DE APUESTA\n"
        f"Apostador: {username}\n"
        f"Acción: {'COMPRA' if trade['side'] == 'BUY' else 'VENTA'} — \"{trade.get('outcome','')}\"\n"
        f"Mercado: {trade.get('title','')}\n"
        f"Monto: ${usd:,.0f}\n"
        f"Cuota: {odds}%\n"
        f"Operar: {market_url(trade)}"
    )


def send_ntfy(text):
    if not NTFY_TOPIC:
        print("NTFY_TOPIC no configurado.", file=sys.stderr)
        return
    try:
        requests.post(f"https://ntfy.sh/{NTFY_TOPIC}", data=text.encode("utf-8"), timeout=10)
    except Exception as e:
        print(f"Error mandando a ntfy: {e}", file=sys.stderr)


def check_wallet(wallet, username, state):
    last_seen = state.get(wallet, 0)
    try:
        trades = get_recent_trades(wallet)
    except Exception as e:
        print(f"Error trayendo trades de {username}: {e}", file=sys.stderr)
        return
    new_last_seen = last_seen
    for trade in sorted(trades, key=lambda t: t.get("timestamp", 0)):
        ts = trade.get("timestamp", 0)
        if ts <= last_seen:
            continue
        new_last_seen = max(new_last_seen, ts)
        usd = (trade.get("size") or 0) * (trade.get("price") or 0)
        if usd < WHALE_THRESHOLD:
            continue
        odds = round((trade.get("price") or 0) * 100)
        print(f"🐋 {username}: ${usd:,.0f} en {trade.get('title')}")
        send_ntfy(build_ticket(username, trade, usd, odds))
    state[wallet] = new_last_seen


def main():
    state = load_state()
    start = time.time()
    traders = []
    last_lb_refresh = 0
    last_state_save = time.time()

    print(f"Arrancando — top {TOP_N} de SEMANA+MES ({LB_CATEGORY}), umbral ${WHALE_THRESHOLD:,.0f}, cada {POLL_SECONDS}s")

    while time.time() - start < MAX_RUNTIME_SECONDS:
        now = time.time()

        if now - last_lb_refresh > LEADERBOARD_REFRESH_SECONDS or not traders:
            traders = get_combined_leaderboard()
            print(f"Ranking combinado ({len(traders)} apostadores): {[t.get('userName') for t in traders]}")
            last_lb_refresh = now

        for trader in traders:
            wallet = trader.get("proxyWallet")
            username = trader.get("userName", "anon")
            if wallet:
                check_wallet(wallet, username, state)

        if time.time() - last_state_save > SAVE_STATE_EVERY_SECONDS:
            save_and_commit_state(state)
            last_state_save = time.time()

        time.sleep(POLL_SECONDS)

    save_and_commit_state(state)
    print("Ciclo terminado — GitHub va a arrancar uno nuevo con el cron.")


if __name__ == "__main__":
    main()
