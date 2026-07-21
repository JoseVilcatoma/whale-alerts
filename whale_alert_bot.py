"""
whale_alert_bot.py

Revisa el top del ranking de Polymarket, detecta apuestas fuertes de esos
apostadores, y manda un push por ntfy.sh directo al celular.

Pensado para correr en GitHub Actions cada 5 minutos (no necesita servidor propio).

Variables de entorno esperadas (se configuran como Secrets en GitHub):
  NTFY_TOPIC        - nombre de tu canal de ntfy (obligatorio)
  WHALE_THRESHOLD   - monto mínimo en USD para avisar (default: 1000)
  TOP_N             - a cuántos del ranking vigilar (default: 10)
  LB_CATEGORY       - categoría del ranking: OVERALL, SPORTS, POLITICS,
                       CRYPTO, ESPORTS, CULTURE, ECONOMICS (default: OVERALL)
  LB_PERIOD         - DAY, WEEK, MONTH o ALL (default: DAY)
"""

import json
import os
import sys
from pathlib import Path

import requests

DATA_API = "https://data-api.polymarket.com"
STATE_FILE = Path(__file__).parent / "state.json"

NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "").strip()
WHALE_THRESHOLD = float(os.environ.get("WHALE_THRESHOLD", "1000"))
TOP_N = int(os.environ.get("TOP_N", "10"))
LB_CATEGORY = os.environ.get("LB_CATEGORY", "OVERALL")
LB_PERIOD = os.environ.get("LB_PERIOD", "DAY")


def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            return {}
    return {}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))


def get_leaderboard():
    r = requests.get(
        f"{DATA_API}/v1/leaderboard",
        params={
            "category": LB_CATEGORY,
            "timePeriod": LB_PERIOD,
            "orderBy": "PNL",
            "limit": TOP_N,
        },
        timeout=15,
    )
    r.raise_for_status()
    return r.json()


def get_recent_trades(wallet):
    r = requests.get(
        f"{DATA_API}/trades",
        params={"user": wallet, "limit": 25},
        timeout=15,
    )
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
        print("NTFY_TOPIC no configurado, no se puede avisar.", file=sys.stderr)
        return
    try:
        # Sin headers extra a propósito: es el formato que ntfy confirma que
        # siempre funciona, sin depender de nada más.
        requests.post(f"https://ntfy.sh/{NTFY_TOPIC}", data=text.encode("utf-8"), timeout=10)
    except Exception as e:
        print(f"Error mandando a ntfy: {e}", file=sys.stderr)


def main():
    state = load_state()
    try:
        leaderboard = get_leaderboard()
    except Exception as e:
        print(f"Error trayendo el ranking: {e}", file=sys.stderr)
        return

    for trader in leaderboard:
        wallet = trader.get("proxyWallet")
        username = trader.get("userName", "anon")
        if not wallet:
            continue

        last_seen = state.get(wallet, 0)
        try:
            trades = get_recent_trades(wallet)
        except Exception as e:
            print(f"Error trayendo trades de {username}: {e}", file=sys.stderr)
            continue

        new_last_seen = last_seen
        # de más viejo a más nuevo, para que las notis lleguen en orden
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

    save_state(state)


if __name__ == "__main__":
    main()
