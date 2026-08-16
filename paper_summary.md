# Paper trading — resultado de la simulación

Actualizado: 2026-08-16 08:40:48 (hora de Perú)

**Bankroll inicial:** $1,000.00
**Bankroll actual:** $878.82
**Retorno acumulado:** -12.12%
**Peor caída desde un máximo (drawdown):** 22.19%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $10.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $690.00 en 69 posiciones abiertas (disponible para nuevas apuestas: $188.82)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 21 | 6 | 1 | +44.73 USD |
| 111111111115 | 10 | 6 | 6 | +23.24 USD |
| bigspending | 1 | 0 | 0 | +10.83 USD |
| Sassy-Bucket | 2 | 3 | 0 | +9.29 USD |
| 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 | 1 | 0 | 1 | +3.89 USD |
| HomeRunHazard | 5 | 2 | 21 | +2.79 USD |
| CORGI8 | 4 | 6 | 0 | +1.20 USD |
| Dota2winner | 0 | 0 | 1 | +0.00 USD |
| Lakersfan111 | 8 | 7 | 5 | -0.23 USD |
| 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 | 9 | 9 | 0 | -0.36 USD |
| SDTrading | 2 | 2 | 9 | -1.87 USD |
| 1winstreak1 | 7 | 7 | 0 | -5.25 USD |
| g42gh6524h5h5 | 9 | 7 | 2 | -7.06 USD |
| TeGeeLP | 0 | 1 | 0 | -10.00 USD |
| midwicket72 | 1 | 2 | 1 | -18.10 USD |
| IMAREALPERSON | 4 | 3 | 2 | -18.56 USD |
| ferrariChampions2026 | 37 | 33 | 0 | -44.40 USD |
| wr0ngw4yb3tt0r | 10 | 15 | 2 | -54.24 USD |
| RN1 | 15 | 12 | 18 | -57.12 USD |

## Análisis general

- **Apuestas resueltas:** 247
- **Aciertos:** 130 (52.6%)
- **Cuota promedio de entrada:** 53.9%
- **Stake promedio:** $10.00
- **Total apostado (suma de stakes):** $2,470.00
- **ROI sobre lo apostado:** -6.54%

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 1-19% (bomba) | 3 | 0.0% | 14.7% | -14.7 pp |
| 20-39% | 40 | 22.5% | 32.3% | -9.8 pp |
| 40-59% | 125 | 48.0% | 49.5% | -1.5 pp |
| 60-79% | 58 | 69.0% | 68.0% | +1.0 pp |
| 80-94% | 16 | 100.0% | 85.1% | +14.9 pp |
| 95-99% (casi seguro) | 5 | 100.0% | 98.0% | +2.0 pp |

## Mercados donde coincidieron 2+ vigilados (para calibrar el tope futuro)

| Mercado | Vigilados que coincidieron |
|---|---|
| dota2-og-huliga-2026-08-14-game2 | 111111111115, CORGI8 |
| dota2-flc-gl-2026-08-14-game2 | 111111111115, CORGI8 |
| mlb-mil-lad-2026-08-14-spread-home-2pt5 | 1winstreak1, RN1 |
| lol-fox1-dnf-2026-08-15-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, Lakersfan111, ferrariChampions2026, g42gh6524h5h5 |
| lol-fox1-dnf-2026-08-15-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, Lakersfan111, ferrariChampions2026, g42gh6524h5h5 |
| dota2-lgd-xtreme-2026-08-14 | 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592, 111111111115, ferrariChampions2026 |
| dota2-ngx-vg-2026-08-15-game1 | 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592, 111111111115, ferrariChampions2026 |
| dota2-flc-gl-2026-08-14 | 111111111115, ferrariChampions2026 |
| dota2-ironwi-liquid-2026-08-15 | 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592, ferrariChampions2026 |
| dota2-ironwi-liquid-2026-08-15-game1 | 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592, 111111111115, ferrariChampions2026 |
| atp-matsuok-sultano-2026-08-15 | RN1, ferrariChampions2026 |
| dota2-vsn2-ts8-2026-08-15-game1 | 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592, CORGI8, ferrariChampions2026 |
| dota2-boombo-aur1-2026-08-15-game1 | 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592, ferrariChampions2026 |
| jap-ura-san-2026-08-15-san | bigspending, ferrariChampions2026 |
| dota2-tr7-xtreme-2026-08-15-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, CORGI8, ferrariChampions2026, g42gh6524h5h5 |
| lol-hle1-kt-2026-08-15 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, ferrariChampions2026 |
| dota2-lgd-vg-2026-08-15-game1 | 111111111115, ferrariChampions2026 |
| dota2-lgd-vg-2026-08-15-game2 | 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592, 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, IMAREALPERSON, ferrariChampions2026, g42gh6524h5h5 |
| lol-tt-al-2026-08-15 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, ferrariChampions2026 |
| lol-tt-al-2026-08-15-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, ferrariChampions2026, g42gh6524h5h5 |
| cs2-mglz-navi-2026-08-15 | CORGI8, ferrariChampions2026 |
| dota2-boombo-flc-2026-08-15-game1 | 111111111115, CORGI8, ferrariChampions2026, g42gh6524h5h5 |
| dota2-tr7-xtreme-2026-08-15-game2 | CORGI8, ferrariChampions2026 |
| lol-tt-al-2026-08-15-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, 111111111115, ferrariChampions2026 |
| lol-fox1-dnf-2026-08-15 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, ferrariChampions2026 |
| dota2-ironwi-ty-2026-08-15-game1 | 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592, CORGI8 |
| mlb-wsh-nym-2026-08-15-total-8pt5 | SDTrading, Sassy-Bucket |
| mlb-sd-cle-2026-08-15 | 1winstreak1, SDTrading |
| lol-sk-fnc-2026-08-15-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, g42gh6524h5h5 |
| mlb-cws-det-2026-08-15 | 1winstreak1, wr0ngw4yb3tt0r |
| lol-g2-shft-2026-08-15-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, IMAREALPERSON, TeGeeLP, g42gh6524h5h5 |
| lol-g2-shft-2026-08-15-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, IMAREALPERSON, g42gh6524h5h5 |
| mlb-stl-chc-2026-08-15 | 1winstreak1, wr0ngw4yb3tt0r |
| mlb-nyy-tor-2026-08-15-total-7pt5 | 1winstreak1, Sassy-Bucket, wr0ngw4yb3tt0r |
| mlb-cws-det-2026-08-15-spread-away-1pt5 | 1winstreak1, wr0ngw4yb3tt0r |
| lol-sr-dig-2026-08-15-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, g42gh6524h5h5 |
| lol-sr-dig-2026-08-15 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, g42gh6524h5h5 |
| lol-sr-dig-2026-08-15-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, g42gh6524h5h5 |
| mlb-tex-oak-2026-08-15 | HomeRunHazard, RN1, Sassy-Bucket |
| atp-zverev-norrie-2026-08-15 | HomeRunHazard, RN1 |
| cs2-ast10-nip-2026-08-16-game1 | 111111111115, Lakersfan111 |
| dota2-ironwi-gl-2026-08-16-game1 | 111111111115, Lakersfan111 |
| dota2-lgd-ty-2026-08-16 | Dota2winner, IMAREALPERSON, Lakersfan111 |
| lol-drx-bro2-2026-08-16 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, 111111111115 |
| mlb-stl-chc-2026-08-16-total-9pt5 | HomeRunHazard, SDTrading |
| mlb-kc-laa-2026-08-16-total-9pt5 | HomeRunHazard, SDTrading |
| mlb-bal-tb-2026-08-16-total-7pt5 | HomeRunHazard, SDTrading |
| mlb-tex-oak-2026-08-16-total-10pt5 | HomeRunHazard, wr0ngw4yb3tt0r |
| mlb-mia-cin-2026-08-16-total-8pt5 | HomeRunHazard, SDTrading |
| mlb-mia-cin-2026-08-16-total-9pt5 | HomeRunHazard, SDTrading |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| ChonkyChocolateCake | Game Handicap: TES (-1.5) vs EDward Gami | Top Esports (BUY) | 59% | 10.00 | 12.5% | ⏳ pendiente | — |
| SDTrading | Miami Marlins vs. Cincinnati Reds: O/U 9 | Under (BUY) | 60% | 10.00 | 6.0% | ⏳ pendiente | — |
| HomeRunHazard | Miami Marlins vs. Cincinnati Reds: O/U 9 | Over (BUY) | 42% | 10.00 | 1.5% | ⏳ pendiente | — |
| SDTrading | Miami Marlins vs. Cincinnati Reds: O/U 8 | Under (BUY) | 49% | 10.00 | 2.1% | ⏳ pendiente | — |
| HomeRunHazard | Miami Marlins vs. Cincinnati Reds: O/U 8 | Over (BUY) | 53% | 10.00 | 1.9% | ⏳ pendiente | — |
| SDTrading | San Diego Padres vs. Cleveland Guardians | Under (BUY) | 54% | 10.00 | 0.5% | ⏳ pendiente | — |
| HomeRunHazard | Spread: Kansas City Royals (-1.5) | Los Angeles Angels (BUY) | 61% | 10.00 | 0.9% | ⏳ pendiente | — |
| HomeRunHazard | Portland Fire vs. Phoenix Mercury: O/U 1 | Over (BUY) | 51% | 10.00 | 0.4% | ⏳ pendiente | — |
| HomeRunHazard | Prague: Luciano Emanuel Ambrogi vs Vojte | Luciano Emanuel Ambrogi (BUY) | 94% | 10.00 | 1.8% | ⏳ pendiente | — |
| wr0ngw4yb3tt0r | Texas Rangers vs. Athletics: O/U 10.5 | Under (BUY) | 55% | 10.00 | 11.9% | ⏳ pendiente | — |
| HomeRunHazard | Texas Rangers vs. Athletics: O/U 10.5 | Under (BUY) | 56% | 10.00 | 2.2% | ⏳ pendiente | — |
| HomeRunHazard | Texas Rangers vs. Athletics: O/U 10.5 | Over (BUY) | 47% | 10.00 | 0.5% | ⏳ pendiente | — |
| SDTrading | Seattle Mariners vs. Houston Astros | Houston Astros (BUY) | 56% | 10.00 | 35.4% | ⏳ pendiente | — |
| SDTrading | San Diego Padres vs. Cleveland Guardians | Cleveland Guardians (BUY) | 50% | 10.00 | 1.9% | ⏳ pendiente | — |
| midwicket72 | The Hundred, Women: Trent Rockets vs Sun | Trent Rockets (BUY) | 59% | 10.00 | 26.5% | ⏳ pendiente | — |
| SDTrading | Baltimore Orioles vs. Tampa Bay Rays: O/ | Under (BUY) | 53% | 10.00 | 6.4% | ⏳ pendiente | — |
| ChonkyChocolateCake | LoL: Team Secret Whales vs CTBC Flying O | Team Secret Whales (BUY) | 51% | 10.00 | 11.3% | ⏳ pendiente | — |
| HomeRunHazard | Baltimore Orioles vs. Tampa Bay Rays: O/ | Over (BUY) | 51% | 10.00 | 1.1% | ⏳ pendiente | — |
| SDTrading | Kansas City Royals vs. Los Angeles Angel | Under (BUY) | 58% | 10.00 | 1.9% | ⏳ pendiente | — |
| HomeRunHazard | Kansas City Royals vs. Los Angeles Angel | Over (BUY) | 44% | 10.00 | 2.6% | ⏳ pendiente | — |
| HomeRunHazard | Kansas City Royals vs. Los Angeles Angel | Under (BUY) | 57% | 10.00 | 7.9% | ⏳ pendiente | — |
| HomeRunHazard | Kansas City Royals vs. Los Angeles Angel | Under (BUY) | 45% | 10.00 | 1.0% | ⏳ pendiente | — |
| SDTrading | St. Louis Cardinals vs. Chicago Cubs: O/ | Over (BUY) | 44% | 10.00 | 3.0% | ⏳ pendiente | — |
| HomeRunHazard | St. Louis Cardinals vs. Chicago Cubs: O/ | Under (BUY) | 58% | 10.00 | 1.5% | ⏳ pendiente | — |
| SDTrading | St. Louis Cardinals vs. Chicago Cubs: O/ | Over (BUY) | 55% | 10.00 | 5.4% | ⏳ pendiente | — |
| HomeRunHazard | Spread: Toronto Blue Jays (-2.5) | New York Yankees (BUY) | 78% | 10.00 | 8.2% | ⏳ pendiente | — |
| HomeRunHazard | Spread: Boston Red Sox (-1.5) | Pittsburgh Pirates (BUY) | 61% | 10.00 | 3.1% | ⏳ pendiente | — |
| HomeRunHazard | New York Yankees vs. Toronto Blue Jays:  | Under (BUY) | 66% | 10.00 | 0.8% | ⏳ pendiente | — |
| HomeRunHazard | New York Yankees vs. Toronto Blue Jays:  | Under (BUY) | 44% | 10.00 | 0.7% | ⏳ pendiente | — |
| 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 | Sion: Dimitris Sakellaridis vs Gian Luca | Dimitris Sakellaridis (BUY) | 69% | 10.00 | 222.0% | ⏳ pendiente | — |
