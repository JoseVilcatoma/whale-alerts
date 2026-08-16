# Paper trading — resultado de la simulación

Actualizado: 2026-08-16 15:34:09 (hora de Perú)

**Bankroll inicial:** $1,000.00
**Bankroll actual:** $844.29
**Retorno acumulado:** -15.57%
**Peor caída desde un máximo (drawdown):** 27.79%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $10.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $340.00 en 34 posiciones abiertas (disponible para nuevas apuestas: $504.29)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 22 | 7 | 1 | +44.73 USD |
| Sassy-Bucket | 3 | 3 | 8 | +20.12 USD |
| 3edmond.dantes | 1 | 0 | 0 | +11.28 USD |
| bigspending | 1 | 0 | 0 | +10.83 USD |
| Dota2winner | 1 | 0 | 0 | +9.61 USD |
| 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 | 2 | 0 | 0 | +8.38 USD |
| HomeRunHazard | 5 | 2 | 9 | +2.79 USD |
| CORGI8 | 4 | 6 | 0 | +1.20 USD |
| SineNooneEI | 0 | 0 | 3 | +0.00 USD |
| crisp1973 | 0 | 0 | 1 | +0.00 USD |
| 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 | 9 | 9 | 0 | -0.36 USD |
| SDTrading | 2 | 2 | 0 | -1.87 USD |
| 1winstreak1 | 7 | 7 | 0 | -5.25 USD |
| g42gh6524h5h5 | 9 | 7 | 3 | -7.06 USD |
| TeGeeLP | 0 | 1 | 0 | -10.00 USD |
| 111111111115 | 11 | 10 | 1 | -13.43 USD |
| Lakersfan111 | 10 | 10 | 0 | -15.25 USD |
| midwicket72 | 2 | 2 | 3 | -17.23 USD |
| IMAREALPERSON | 6 | 4 | 3 | -20.60 USD |
| ferrariChampions2026 | 37 | 33 | 0 | -44.40 USD |
| wr0ngw4yb3tt0r | 10 | 16 | 0 | -64.24 USD |
| RN1 | 25 | 18 | 2 | -65.01 USD |

## Análisis general

- **Apuestas resueltas:** 283
- **Aciertos:** 150 (53.0%)
- **Cuota promedio de entrada:** 54.7%
- **Stake promedio:** $10.00
- **Total apostado (suma de stakes):** $2,830.00
- **ROI sobre lo apostado:** -7.28%

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 1-19% (bomba) | 3 | 0.0% | 14.7% | -14.7 pp |
| 20-39% | 42 | 21.4% | 32.3% | -10.8 pp |
| 40-59% | 145 | 47.6% | 49.7% | -2.1 pp |
| 60-79% | 67 | 68.7% | 68.2% | +0.4 pp |
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

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: FlyQuest vs Cloud9 - Game 1 Winner | FlyQuest (BUY) | 42% | 10.00 | 2.4% | ⏳ pendiente | — |
| Sassy-Bucket | Colorado Rockies vs. San Francisco Giant | Over (BUY) | 54% | 10.00 | 8.3% | ⏳ pendiente | — |
| Sassy-Bucket | St. Louis Cardinals vs. Chicago Cubs: O/ | Under (BUY) | 57% | 10.00 | 0.8% | ⏳ pendiente | — |
| Sassy-Bucket | Chicago Sky vs. Seattle Storm: O/U 179.5 | Over (BUY) | 44% | 10.00 | 7.0% | ⏳ pendiente | — |
| Sassy-Bucket | St. Louis Cardinals vs. Chicago Cubs: O/ | Under (BUY) | 47% | 10.00 | 16.7% | ⏳ pendiente | — |
| IMAREALPERSON | LoL: paiN Gaming vs Fluxo W7M - Game 2 W | paiN Gaming (BUY) | 59% | 10.00 | 12.5% | ⏳ pendiente | — |
| SineNooneEI | LoL: paiN Gaming vs Fluxo W7M - Game 2 W | paiN Gaming (BUY) | 45% | 10.00 | 8.4% | ⏳ pendiente | — |
| ChonkyChocolateCake | LoL: paiN Gaming vs Fluxo W7M - Game 2 W | Fluxo W7M (BUY) | 59% | 10.00 | 64.1% | ⏳ pendiente | — |
| SineNooneEI | LoL: G2 Esports vs Fnatic - Game 2 Winne | G2 Esports (BUY) | 73% | 10.00 | 42.3% | ⏳ pendiente | — |
| ChonkyChocolateCake | LoL: G2 Esports vs Fnatic - Game 2 Winne | G2 Esports (BUY) | 72% | 10.00 | 113.4% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: G2 Esports vs Fnatic (BO3) - LEC Re | Fnatic (BUY) | 47% | 10.00 | 100.6% | 💰 vendida anticipada | +10.00 |
| Sassy-Bucket | Kansas City Royals vs. Los Angeles Angel | Over (BUY) | 52% | 10.00 | 71.9% | ⏳ pendiente | — |
| IMAREALPERSON | LoL: G2 Esports vs Fnatic - Game 1 Winne | Fnatic (BUY) | 49% | 10.00 | 13.9% | ⏳ pendiente | — |
| Sassy-Bucket | Kansas City Royals vs. Los Angeles Angel | Over (BUY) | 42% | 10.00 | 33.9% | ⏳ pendiente | — |
| IMAREALPERSON | LoL: G2 Esports vs Fnatic - Game 1 Winne | G2 Esports (BUY) | 49% | 10.00 | 27.2% | ⏳ pendiente | — |
| crisp1973 | Will SK Slavia Praha win on 2026-08-16? | No (BUY) | 51% | 10.00 | 366.9% | ⏳ pendiente | — |
| midwicket72 | The Hundred: Trent Rockets vs Manchester | Trent Rockets (BUY) | 55% | 10.00 | 19.5% | ⏳ pendiente | — |
| ChonkyChocolateCake | LoL: G2 Esports vs Fnatic - Game 1 Winne | G2 Esports (BUY) | 63% | 10.00 | 29.1% | ⏳ pendiente | — |
| midwicket72 | Metro Bank One Day Cup: Leicestershire v | Leicestershire (BUY) | 92% | 10.00 | 5.4% | ✅ ganada | +0.87 |
| SineNooneEI | LoL: G2 Esports vs Fnatic - Game 1 Winne | G2 Esports (BUY) | 76% | 10.00 | 9.5% | ⏳ pendiente | — |
| midwicket72 | The Hundred: Trent Rockets vs Manchester | Manchester Super Giants (BUY) | 49% | 10.00 | 18.1% | ⏳ pendiente | — |
| Sassy-Bucket | Miami Marlins vs. Cincinnati Reds: O/U 8 | Over (BUY) | 51% | 10.00 | 210.1% | ⏳ pendiente | — |
| Sassy-Bucket | Boston Red Sox vs. Pittsburgh Pirates: O | Over (BUY) | 48% | 10.00 | 12.0% | ✅ ganada | +10.83 |
| midwicket72 | Metro Bank One Day Cup: Middlesex vs Dur | Durham (BUY) | 42% | 10.00 | 21.0% | ⏳ pendiente | — |
| IMAREALPERSON | Counter-Strike: Astralis vs NIP - Map 2  | NIP (BUY) | 56% | 10.00 | 51.5% | ✅ ganada | +7.86 |
| Sassy-Bucket | Boston Red Sox vs. Pittsburgh Pirates | Pittsburgh Pirates (BUY) | 50% | 10.00 | 128.3% | ⏳ pendiente | — |
| 3edmond.dantes | Will RCD Espanyol de Barcelona win on 20 | Yes (BUY) | 47% | 10.00 | 304.7% | ✅ ganada | +11.28 |
| HomeRunHazard | Spread: Toronto Blue Jays (-2.5) | New York Yankees (BUY) | 78% | 10.00 | 4.1% | ⏳ pendiente | — |
| HomeRunHazard | Spread: Boston Red Sox (-1.5) | Pittsburgh Pirates (BUY) | 61% | 10.00 | 3.1% | ⏳ pendiente | — |
| HomeRunHazard | New York Yankees vs. Toronto Blue Jays:  | Under (BUY) | 66% | 10.00 | 0.8% | ⏳ pendiente | — |
