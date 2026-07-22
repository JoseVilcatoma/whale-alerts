"""
whale_alert_bot.py — versión en bucle continuo con especialidad por deporte

Vigila a los mejores apostadores combinando el ranking de la SEMANA y el
del MES (sin duplicados). Cada vez que uno hace una apuesta fuerte, el
ticket incluye su récord histórico específico en la categoría de esa
apuesta (fútbol, baloncesto, CS2, LoL, Dota, NFL, tenis, etc.), para saber
si es un "especialista" ahí o no.

Variables de entorno (se configuran en el workflow / como Secrets):
  NTFY_TOPIC                   - nombre de tu canal de ntfy (obligatorio)
  WHALE_THRESHOLD              - monto mínimo en USD para avisar (default: 1000)
  TOP_N                        - a cuántos de CADA período vigilar (default: 10)
  LB_CATEGORY                  - OVERALL, SPORTS, POLITICS, CRYPTO, ESPORTS,
                                  CULTURE, ECONOMICS (default: OVERALL)
  POLL_SECONDS                 - cada cuánto revisa trades nuevos (default: 10)
  LEADERBOARD_REFRESH_SECONDS  - cada cuánto refresca el ranking (default: 900)
  SAVE_STATE_EVERY_SECONDS     - cada cuánto guarda progreso (default: 300)
  STATS_REFRESH_HOURS          - cada cuánto re-analiza el historial de un
                                  apostador (default: 24)
  MAX_RUNTIME_SECONDS          - cuándo cortar solo, antes que lo corte GitHub
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
def _allowed_gai_family():
    return socket.AF_INET

urllib3_cn.allowed_gai_family = _allowed_gai_family

DATA_API = "https://data-api.polymarket.com"
GAMMA_API = "https://gamma-api.polymarket.com"
STATE_FILE = Path(__file__).parent / "state.json"
STATS_FILE = Path(__file__).parent / "stats.json"

NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "").strip()
WHALE_THRESHOLD = float(os.environ.get("WHALE_THRESHOLD", "1000"))
TOP_N = int(os.environ.get("TOP_N", "10"))
LB_CATEGORY = os.environ.get("LB_CATEGORY", "OVERALL")
LB_PERIODS = ["WEEK", "MONTH"]

POLL_SECONDS = int(os.environ.get("POLL_SECONDS", "10"))
LEADERBOARD_REFRESH_SECONDS = int(os.environ.get("LEADERBOARD_REFRESH_SECONDS", "900"))
SAVE_STATE_EVERY_SECONDS = int(os.environ.get("SAVE_STATE_EVERY_SECONDS", "300"))
STATS_REFRESH_HOURS = float(os.environ.get("STATS_REFRESH_HOURS", "24"))
MAX_RUNTIME_SECONDS = int(os.environ.get("MAX_RUNTIME_SECONDS", str(5 * 3600 + 50 * 60)))

# ---------- clasificación por deporte/categoría (misma lógica que el dashboard) ----------
SPECIALTY_RULES = [
    ("Baloncesto", ["nba", "basketball", "euroleague", "baloncesto"]),
    ("Béisbol", ["mlb", "baseball", "béisbol", "beisbol"]),
    ("Fútbol Americano", ["nfl", "ncaaf", "college football"]),
    ("Fútbol", ["soccer", "premier league", "la liga", "champions league", "world cup",
                "uefa", "mls", "serie a", "bundesliga", "ligue 1", "fútbol", "futbol"]),
    ("Hockey", ["nhl", "hockey"]),
    ("Tenis", ["tennis", "atp", "wta", "tenis"]),
    ("MMA / Boxeo", ["mma", "ufc", "boxing", "boxeo"]),
    ("Golf", ["golf", "pga"]),
    ("Automovilismo", ["nascar", "f1", "formula 1"]),
    ("CS2", ["counter-strike", "cs2", "csgo"]),
    ("League of Legends", ["league of legends", "lol esports", "lck", "lec", "lcs"]),
    ("Dota 2", ["dota"]),
    ("Valorant", ["valorant"]),
    ("Esports (otros)", ["esports", "esport"]),
    ("Cripto", ["crypto", "bitcoin", "ethereum", "cripto"]),
    ("Política", ["politics", "elections", "política", "politica", "election"]),
    ("Economía", ["economy", "fed", "inflation", "economía", "economia"]),
    ("Cultura", ["culture", "entertainment", "movies", "music", "cultura"]),
]

_market_cache = {}


def get_market(slug):
    if not slug:
        return None
    if slug in _market_cache:
        return _market_cache[slug]
    try:
        r = requests.get(f"{GAMMA_API}/markets/slug/{slug}", timeout=15)
        m = r.json() if r.ok else None
    except Exception:
        m = None
    _market_cache[slug] = m
    return m


def classify_market(market, fallback_title=""):
    if not market:
        text = (fallback_title or "").lower()
        labels = []
    else:
        labels = [(t.get("label") or "").lower() for t in (market.get("tags") or [])]
        text = ((market.get("question") or market.get("title") or fallback_title or "") + " " +
                 (market.get("category") or "")).lower()
    for name, keywords in SPECIALTY_RULES:
        if any(k in l for k in keywords for l in labels) or any(k in text for k in keywords):
            return name
    return None


def market_result(market, outcome):
    """Devuelve 'won' / 'lost' / 'open' / None (desconocido/ambiguo)."""
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


# ---------- estado persistido ----------
def load_json(path):
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            return {}
    return {}


def save_and_commit(paths_and_data, message):
    for path, data in paths_and_data:
        path.write_text(json.dumps(data, indent=2))
    os.system('git config user.name "whale-alert-bot"')
    os.system('git config user.email "actions@github.com"')
    for path, _ in paths_and_data:
        os.system(f"git add {path.name}")
    os.system(f'git diff --staged --quiet || git commit -m "{message}"')
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


def get_recent_trades(wallet, limit=25):
    r = requests.get(f"{DATA_API}/trades", params={"user": wallet, "limit": limit}, timeout=15)
    r.raise_for_status()
    return r.json()


def market_url(trade):
    slug = trade.get("eventSlug") or trade.get("slug")
    return f"https://polymarket.com/event/{slug}" if slug else "https://polymarket.com"


# ---------- backfill de especialidad (analiza historial una vez por apostador) ----------
def backfill_wallet_stats(wallet, username, stats):
    print(f"Analizando historial de {username} para calcular especialidad...")
    try:
        trades = get_recent_trades(wallet, limit=60)
    except Exception as e:
        print(f"  error trayendo historial de {username}: {e}", file=sys.stderr)
        return

    seen_slugs = set()
    categories = {}
    for t in trades:
        slug = t.get("slug")
        if not slug or slug in seen_slugs:
            continue
        seen_slugs.add(slug)
        market = get_market(slug)
        result = market_result(market, t.get("outcome"))
        if result not in ("won", "lost"):
            continue
        cat = classify_market(market, t.get("title"))
        if not cat:
            continue
        categories.setdefault(cat, {"won": 0, "lost": 0})
        categories[cat][result] += 1
        time.sleep(0.12)  # ser prudentes con la API pública

    stats[wallet] = {"userName": username, "updated_at": time.time(), "categories": categories}
    resumen = ", ".join(f"{c}: {v['won']}G-{v['lost']}P" for c, v in categories.items()) or "sin datos suficientes"
    print(f"  especialidad de {username}: {resumen}")


def specialty_line(wallet, category, stats):
    if not category:
        return ""
    entry = stats.get(wallet, {}).get("categories", {}).get(category)
    if not entry:
        return f"\n📊 Especialidad en {category}: sin historial suficiente todavía"
    total = entry["won"] + entry["lost"]
    if total < 3:
        return f"\n📊 {category}: {entry['won']}G-{entry['lost']}P (muestra chica todavía)"
    pct = round(entry["won"] / total * 100)
    return f"\n📊 Especialidad en {category}: {entry['won']}G-{entry['lost']}P ({pct}% acierto)"


def build_ticket(username, trade, usd, odds, wallet, stats):
    market = get_market(trade.get("slug"))
    category = classify_market(market, trade.get("title"))
    spec_line = specialty_line(wallet, category, stats)
    return (
        f"🐋 {username} — nueva apuesta fuerte\n\n"
        f"🎟️ TICKET DE APUESTA\n"
        f"Apostador: {username}\n"
        f"Acción: {'COMPRA' if trade['side'] == 'BUY' else 'VENTA'} — \"{trade.get('outcome','')}\"\n"
        f"Mercado: {trade.get('title','')}\n"
        f"Categoría: {category or 'sin clasificar'}\n"
        f"Monto: ${usd:,.0f}\n"
        f"Cuota: {odds}%"
        f"{spec_line}\n"
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


def check_wallet(wallet, username, state, stats):
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
        send_ntfy(build_ticket(username, trade, usd, odds, wallet, stats))
    state[wallet] = new_last_seen


def next_wallet_needing_backfill(traders, stats):
    cutoff = time.time() - STATS_REFRESH_HOURS * 3600
    candidates = [
        t for t in traders
        if t.get("proxyWallet") and stats.get(t["proxyWallet"], {}).get("updated_at", 0) < cutoff
    ]
    if not candidates:
        return None
    candidates.sort(key=lambda t: stats.get(t["proxyWallet"], {}).get("updated_at", 0))
    return candidates[0]


def main():
    state = load_json(STATE_FILE)
    stats = load_json(STATS_FILE)
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

        # una sola actualización de especialidad por vuelta, para repartir el costo
        candidate = next_wallet_needing_backfill(traders, stats)
        if candidate:
            backfill_wallet_stats(candidate["proxyWallet"], candidate.get("userName", "anon"), stats)

        for trader in traders:
            wallet = trader.get("proxyWallet")
            username = trader.get("userName", "anon")
            if wallet:
                check_wallet(wallet, username, state, stats)

        if time.time() - last_state_save > SAVE_STATE_EVERY_SECONDS:
            save_and_commit([(STATE_FILE, state), (STATS_FILE, stats)], "actualizar estado y especialidades")
            last_state_save = time.time()

        time.sleep(POLL_SECONDS)

    save_and_commit([(STATE_FILE, state), (STATS_FILE, stats)], "actualizar estado y especialidades")
    print("Ciclo terminado — GitHub va a arrancar uno nuevo con el cron.")


if __name__ == "__main__":
    main()
