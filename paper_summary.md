# Paper trading — resultado de la simulación

Actualizado: 2026-08-16 17:07:03 (hora de Perú)

**Bankroll inicial:** $1,000.00
**Bankroll actual:** $805.40
**Retorno acumulado:** -19.46%
**Peor caída desde un máximo (drawdown):** 29.62%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $10.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $160.00 en 16 posiciones abiertas (disponible para nuevas apuestas: $645.40)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 22 | 8 | 0 | +39.97 USD |
| 3edmond.dantes | 1 | 0 | 0 | +11.28 USD |
| bigspending | 1 | 0 | 0 | +10.83 USD |
| Dota2winner | 1 | 0 | 0 | +9.61 USD |
| crisp1973 | 1 | 0 | 0 | +9.61 USD |
| HomeRunHazard | 8 | 3 | 5 | +9.28 USD |
| 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 | 2 | 0 | 0 | +8.38 USD |
| CORGI8 | 4 | 6 | 0 | +1.20 USD |
| 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 | 9 | 9 | 0 | -0.36 USD |
| Sassy-Bucket | 4 | 6 | 6 | -1.36 USD |
| SDTrading | 2 | 2 | 0 | -1.87 USD |
| 1winstreak1 | 7 | 7 | 0 | -5.25 USD |
| SineNooneEI | 1 | 2 | 0 | -7.78 USD |
| TeGeeLP | 0 | 1 | 0 | -10.00 USD |
| IMAREALPERSON | 8 | 5 | 1 | -13.24 USD |
| Lakersfan111 | 10 | 10 | 1 | -15.25 USD |
| midwicket72 | 3 | 3 | 1 | -16.82 USD |
| 111111111115 | 11 | 11 | 0 | -23.43 USD |
| g42gh6524h5h5 | 9 | 10 | 1 | -37.06 USD |
| ferrariChampions2026 | 37 | 33 | 0 | -44.40 USD |
| RN1 | 26 | 18 | 1 | -53.73 USD |
| wr0ngw4yb3tt0r | 10 | 16 | 0 | -64.24 USD |

## Análisis general

- **Apuestas resueltas:** 305
- **Aciertos:** 160 (52.5%)
- **Cuota promedio de entrada:** 54.8%
- **Stake promedio:** $10.00
- **Total apostado (suma de stakes):** $3,050.00
- **ROI sobre lo apostado:** -7.87%

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 1-19% (bomba) | 3 | 0.0% | 14.7% | -14.7 pp |
| 20-39% | 42 | 21.4% | 32.3% | -10.8 pp |
| 40-59% | 161 | 47.8% | 49.8% | -2.0 pp |
| 60-79% | 73 | 65.8% | 68.5% | -2.7 pp |
| 80-94% | 19 | 100.0% | 85.3% | +14.7 pp |
| 95-99% (casi seguro) | 7 | 100.0% | 98.0% | +2.0 pp |

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
| lol-g2-fnc-2026-08-16-game1 | ChonkyChocolateCake, IMAREALPERSON, SineNooneEI |
| lol-g2-fnc-2026-08-16-game2 | ChonkyChocolateCake, SineNooneEI |
| lol-png1-fxw7-2026-08-16-game2 | ChonkyChocolateCake, IMAREALPERSON, SineNooneEI |
| lol-ly-sen-2026-08-16-game-handicap-away-1pt5 | ChonkyChocolateCake, IMAREALPERSON |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| ChonkyChocolateCake | Game Handicap: LY (-1.5) vs Sentinels (+ | LYON (BUY) | 55% | 10.00 | 13.8% | ⏳ pendiente | — |
| IMAREALPERSON | Game Handicap: LY (-1.5) vs Sentinels (+ | Sentinels (BUY) | 46% | 10.00 | 29.7% | ⏳ pendiente | — |
| Lakersfan111 | LoL: T1 vs DN SOOPers (BO5) - KeSPA Cup  | DN SOOPers (BUY) | 63% | 10.00 | 97.8% | ⏳ pendiente | — |
| Sassy-Bucket | Indiana Fever vs. Atlanta Dream: O/U 188 | Under (BUY) | 53% | 10.00 | 3.6% | ⏳ pendiente | — |
| Sassy-Bucket | Indiana Fever vs. Atlanta Dream: O/U 187 | Under (BUY) | 51% | 10.00 | 33.8% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: FlyQuest vs Cloud9 - Game 1 Winner | FlyQuest (BUY) | 42% | 10.00 | 2.4% | 💰 vendida anticipada | -4.76 |
| Sassy-Bucket | Colorado Rockies vs. San Francisco Giant | Over (BUY) | 54% | 10.00 | 8.3% | ✅ ganada | +8.52 |
| Sassy-Bucket | St. Louis Cardinals vs. Chicago Cubs: O/ | Under (BUY) | 57% | 10.00 | 0.8% | ❌ perdida | -10.00 |
| Sassy-Bucket | Chicago Sky vs. Seattle Storm: O/U 179.5 | Over (BUY) | 44% | 10.00 | 7.0% | ⏳ pendiente | — |
| Sassy-Bucket | St. Louis Cardinals vs. Chicago Cubs: O/ | Under (BUY) | 47% | 10.00 | 16.7% | ❌ perdida | -10.00 |
| IMAREALPERSON | LoL: paiN Gaming vs Fluxo W7M - Game 2 W | paiN Gaming (BUY) | 59% | 10.00 | 12.5% | ✅ ganada | +6.95 |
| SineNooneEI | LoL: paiN Gaming vs Fluxo W7M - Game 2 W | paiN Gaming (BUY) | 45% | 10.00 | 8.4% | ✅ ganada | +12.22 |
| ChonkyChocolateCake | LoL: paiN Gaming vs Fluxo W7M - Game 2 W | Fluxo W7M (BUY) | 59% | 10.00 | 64.1% | ❌ perdida | -10.00 |
| SineNooneEI | LoL: G2 Esports vs Fnatic - Game 2 Winne | G2 Esports (BUY) | 73% | 10.00 | 42.3% | ❌ perdida | -10.00 |
| ChonkyChocolateCake | LoL: G2 Esports vs Fnatic - Game 2 Winne | G2 Esports (BUY) | 72% | 10.00 | 113.4% | ❌ perdida | -10.00 |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: G2 Esports vs Fnatic (BO3) - LEC Re | Fnatic (BUY) | 47% | 10.00 | 100.6% | 💰 vendida anticipada | +10.00 |
| Sassy-Bucket | Kansas City Royals vs. Los Angeles Angel | Over (BUY) | 52% | 10.00 | 71.9% | ⏳ pendiente | — |
| IMAREALPERSON | LoL: G2 Esports vs Fnatic - Game 1 Winne | Fnatic (BUY) | 49% | 10.00 | 13.9% | ✅ ganada | +10.41 |
| Sassy-Bucket | Kansas City Royals vs. Los Angeles Angel | Over (BUY) | 42% | 10.00 | 33.9% | ⏳ pendiente | — |
| IMAREALPERSON | LoL: G2 Esports vs Fnatic - Game 1 Winne | G2 Esports (BUY) | 49% | 10.00 | 27.2% | ❌ perdida | -10.00 |
| crisp1973 | Will SK Slavia Praha win on 2026-08-16? | No (BUY) | 51% | 10.00 | 366.9% | ✅ ganada | +9.61 |
| midwicket72 | The Hundred: Trent Rockets vs Manchester | Trent Rockets (BUY) | 55% | 10.00 | 19.5% | ❌ perdida | -10.00 |
| ChonkyChocolateCake | LoL: G2 Esports vs Fnatic - Game 1 Winne | G2 Esports (BUY) | 63% | 10.00 | 29.1% | ❌ perdida | -10.00 |
| midwicket72 | Metro Bank One Day Cup: Leicestershire v | Leicestershire (BUY) | 92% | 10.00 | 5.4% | ✅ ganada | +0.87 |
| SineNooneEI | LoL: G2 Esports vs Fnatic - Game 1 Winne | G2 Esports (BUY) | 76% | 10.00 | 9.5% | ❌ perdida | -10.00 |
| midwicket72 | The Hundred: Trent Rockets vs Manchester | Manchester Super Giants (BUY) | 49% | 10.00 | 18.1% | ✅ ganada | +10.41 |
| Sassy-Bucket | Miami Marlins vs. Cincinnati Reds: O/U 8 | Over (BUY) | 51% | 10.00 | 210.1% | ❌ perdida | -10.00 |
| Sassy-Bucket | Boston Red Sox vs. Pittsburgh Pirates: O | Over (BUY) | 48% | 10.00 | 12.0% | ✅ ganada | +10.83 |
| midwicket72 | Metro Bank One Day Cup: Middlesex vs Dur | Durham (BUY) | 42% | 10.00 | 21.0% | ⏳ pendiente | — |
| IMAREALPERSON | Counter-Strike: Astralis vs NIP - Map 2  | NIP (BUY) | 56% | 10.00 | 51.5% | ✅ ganada | +7.86 |
