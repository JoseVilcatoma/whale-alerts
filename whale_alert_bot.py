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
            if PUBLICAR_RESULTADOS:
                publicar_desenlace(r, outcome)
        time.sleep(0.1)
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
    msg = f"{icono} — desenlace\n\n"
    msg += f"👤 {r['username']}\n"
    msg += f"📊 {r['title']}\n"
    msg += f"🎯 Había apostado a: {r['outcome']} (a {r['odds_at_bet']}¢)\n"
    msg += f"💵 Monto: ${r['usd']:,.0f}\n\n"
    if total >= 3:
        pct = round(ganadas / total * 100)
        msg += f"📈 Récord de {r['username']} desde que lo seguimos: "
        msg += f"{ganadas}-{perdidas} ({pct}% de acierto)"
        if total < 10:
            msg += f"\n⚠️ Muestra chica todavía ({total} resueltas)"
    send_telegram(msg)


def build_summary_md():
    per_wallet = {}
    for r in results:
        w = r["wallet"]
        per_wallet.setdefault(w, {"username": r["username"], "won": 0, "lost": 0,
                                   "pending": 0, "usd": 0.0})
        per_wallet[w]["usd"] += r.get("usd", 0) or 0
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
        "_Menos de 8 apuestas resueltas no es muestra confiable — se marca con ⚠️._",
        "",
        "## Por apostador (ordenado por monto apostado)",
        "",
        "| Apostador | Ganadas | Perdidas | Pendientes | % Acierto | Total apostado |",
        "|---|---|---|---|---|---|",
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
        lines.append(f"| {d['username']} | {d['won']} | {d['lost']} | {d['pending']} | "
                     f"{pct_str} | ${d['usd']:,.0f} |")
    if len(per_wallet) > 40:
        lines.append(f"\n_(mostrando los 40 de mayor monto, de {len(per_wallet)} en total)_")

    # --- detalle de cada apuesta, lo que pediste ---
    lines += ["", "## Detalle de las últimas 60 apuestas", "",
              "| Apostador | Mercado | Apostó a | Precio | Monto | Resultado |",
              "|---|---|---|---|---|---|"]
    icono = {"won": "✅ Ganada", "lost": "❌ Perdida", "pending": "⏳ Pendiente"}
    for r in sorted(results, key=lambda x: x.get("timestamp") or 0, reverse=True)[:60]:
        lines.append(
            f"| {r['username']} | {(r.get('title') or '')[:38]} | {r.get('outcome','')} | "
            f"{r.get('odds_at_bet','?')}¢ | ${r.get('usd',0):,.0f} | "
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


def send_telegram(text):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    try:
        r = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": text,
                "disable_web_page_preview": True,
            },
            timeout=10,
        )
        if r.status_code != 200:
            print(f"[telegram] ⚠️ respuesta {r.status_code}: {r.text[:300]}", file=sys.stderr)
    except Exception as e:
        print(f"Error mandando a Telegram: {e}", file=sys.stderr)


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

    odds = round((trade.get("price") or 0) * 100)
    print(f"🐋 EN VIVO — {username}: ${usd:,.0f} en {trade.get('title')}")
    send_telegram(build_ticket(username, trade, usd, odds, wallet))
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
        WATCHED_FILE.write_text(json.dumps(watched_meta, indent=2))
    os.system('git config user.name "whale-alert-bot"')
    os.system('git config user.email "actions@github.com"')
    os.system("git add results.json results.md watched.json")
    os.system('git diff --staged --quiet || git commit -m "actualizar resultados y vigilados"')
    os.system("git push")
    results_dirty = False


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

        if results_dirty and now - last_save > 120:
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
