# Paper trading — resultado de la simulación

Actualizado: 2026-08-16 06:38:12 (hora de Perú)

**Bankroll inicial:** $1,000.00
**Bankroll actual:** $878.24
**Retorno acumulado:** -12.18%
**Peor caída desde un máximo (drawdown):** 21.70%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $10.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $290.00 en 29 posiciones abiertas (disponible para nuevas apuestas: $588.24)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 21 | 6 | 0 | +44.73 USD |
| 111111111115 | 10 | 6 | 4 | +23.24 USD |
| bigspending | 1 | 0 | 0 | +10.83 USD |
| Sassy-Bucket | 2 | 3 | 0 | +9.29 USD |
| 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 | 1 | 0 | 0 | +3.89 USD |
| HomeRunHazard | 5 | 2 | 3 | +2.79 USD |
| CORGI8 | 4 | 6 | 0 | +1.20 USD |
| Dota2winner | 0 | 0 | 1 | +0.00 USD |
| 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 | 9 | 9 | 0 | -0.36 USD |
| SDTrading | 2 | 2 | 0 | -1.87 USD |
| 1winstreak1 | 7 | 7 | 0 | -5.25 USD |
| Lakersfan111 | 7 | 7 | 6 | -5.38 USD |
| g42gh6524h5h5 | 9 | 7 | 0 | -7.06 USD |
| TeGeeLP | 0 | 1 | 0 | -10.00 USD |
| midwicket72 | 1 | 2 | 0 | -18.10 USD |
| IMAREALPERSON | 4 | 3 | 2 | -18.56 USD |
| ferrariChampions2026 | 37 | 33 | 0 | -44.40 USD |
| RN1 | 9 | 10 | 12 | -52.54 USD |
| wr0ngw4yb3tt0r | 10 | 15 | 1 | -54.24 USD |

## Análisis general

- **Apuestas resueltas:** 238
- **Aciertos:** 123 (51.7%)
- **Cuota promedio de entrada:** 53.1%
- **Stake promedio:** $10.00
- **Total apostado (suma de stakes):** $2,380.00
- **ROI sobre lo apostado:** -6.81%

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 1-19% (bomba) | 3 | 0.0% | 14.7% | -14.7 pp |
| 20-39% | 40 | 22.5% | 32.3% | -9.8 pp |
| 40-59% | 123 | 48.8% | 49.4% | -0.6 pp |
| 60-79% | 55 | 67.3% | 68.2% | -0.9 pp |
| 80-94% | 14 | 100.0% | 85.0% | +15.0 pp |
| 95-99% (casi seguro) | 3 | 100.0% | 97.7% | +2.3 pp |

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

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| RN1 | DSC Arminia Bielefeld vs. FC Energie Cot | Over (BUY) | 64% | 10.00 | 1.0% | ⏳ pendiente | — |
| RN1 | ADO Den Haag vs. FC Groningen: O/U 4.5 | Over (BUY) | 82% | 10.00 | 0.6% | ⏳ pendiente | — |
| RN1 | ADO Den Haag vs. FC Groningen: O/U 3.5 | Over (BUY) | 85% | 10.00 | 0.6% | ⏳ pendiente | — |
| IMAREALPERSON | LoL: Kiwoom DRX vs HANJIN BRION - Game 1 | HANJIN BRION (BUY) | 99% | 10.00 | 31.0% | ⏳ pendiente | — |
| HomeRunHazard | Chicago Sky vs. Seattle Storm: O/U 178.5 | Over (BUY) | 48% | 10.00 | 0.7% | ⏳ pendiente | — |
| RN1 | Hamburg: Jan Kumstat vs Marvin Moeller | Jan Kumstat (BUY) | 51% | 10.00 | 4.3% | ⏳ pendiente | — |
| RN1 | Will Hannover 96 win on 2026-08-16? | No (BUY) | 58% | 10.00 | 3.2% | ⏳ pendiente | — |
| RN1 | Roehampton: Peter Makk vs Roan Jones | Peter Makk (BUY) | 99% | 10.00 | 2.3% | ⏳ pendiente | — |
| RN1 | Roehampton: Rhys Lawlor vs Nicolas Tepma | Rhys Lawlor (BUY) | 48% | 10.00 | 0.9% | ⏳ pendiente | — |
| RN1 | ITF M25 Kursumlijska Banja 3 Men: Sean C | Stefan Horia Haita (BUY) | 57% | 10.00 | 1.4% | ⏳ pendiente | — |
| IMAREALPERSON | Dota 2: LGD Gaming vs Team Yandex (BO3)  | LGD Gaming (BUY) | 47% | 10.00 | 2.7% | ⏳ pendiente | — |
| Dota2winner | Dota 2: LGD Gaming vs Team Yandex (BO3)  | Team Yandex (BUY) | 51% | 10.00 | 23.6% | ⏳ pendiente | — |
| RN1 | ITF M25 Muttenz Men: Luca Staeheli vs Lo | Louis Wessels (BUY) | 51% | 10.00 | 1.5% | ⏳ pendiente | — |
| RN1 | Will FC Groningen win on 2026-08-16? | Yes (BUY) | 97% | 10.00 | 1.0% | ⏳ pendiente | — |
| RN1 | ITF W35 Vigo Women: Sonja Zhiyenbayeva v | Sonja Zhiyenbayeva (BUY) | 92% | 10.00 | 11.1% | ⏳ pendiente | — |
| HomeRunHazard | Milwaukee Brewers vs. Los Angeles Dodger | Los Angeles Dodgers (BUY) | 62% | 10.00 | 0.9% | ⏳ pendiente | — |
| Lakersfan111 | Dota 2: LGD Gaming vs Team Yandex - Game | Team Yandex (BUY) | 66% | 10.00 | 1.2% | ⏳ pendiente | — |
| 111111111115 | Dota 2: Iron Wing vs GamerLegion - Game  | Iron Wing (BUY) | 74% | 10.00 | 25.7% | ✅ ganada | +3.51 |
| Lakersfan111 | Dota 2: LGD Gaming vs Team Yandex - Game | Team Yandex (BUY) | 66% | 10.00 | 4.8% | ❌ perdida | -10.00 |
| Lakersfan111 | Dota 2: LGD Gaming vs Team Yandex (BO3)  | Team Yandex (BUY) | 73% | 10.00 | 0.4% | ⏳ pendiente | — |
| 111111111115 | Counter-Strike: TheMongolz vs paiN - Map | paiN (BUY) | 46% | 10.00 | 0.3% | ⏳ pendiente | — |
| 111111111115 | Dota 2: Team Spirit vs Team Resilience - | Team Spirit (BUY) | 72% | 10.00 | 3.3% | ❌ perdida | -10.00 |
| Lakersfan111 | Game Handicap: TY (-1.5) vs LGD Gaming ( | Team Yandex (BUY) | 44% | 10.00 | 0.4% | ⏳ pendiente | — |
| RN1 | Yellow-Red KV Mechelen vs. Standard Lieg | Over (BUY) | 47% | 10.00 | 3.3% | ⏳ pendiente | — |
| RN1 | Atlas FC vs. Tigres de la UANL: O/U 3.5 | Over (BUY) | 36% | 10.00 | 1.7% | ❌ perdida | -10.00 |
| RN1 | Will Tigres de la UANL win on 2026-08-15 | No (BUY) | 95% | 10.00 | 0.9% | ✅ ganada | +0.53 |
| RN1 | Will Tigres de la UANL win on 2026-08-15 | Yes (BUY) | 42% | 10.00 | 1.9% | ❌ perdida | -10.00 |
| 111111111115 | Dota 2: Aurora vs BoomBoys - Game 2 Winn | BoomBoys (BUY) | 51% | 10.00 | 276.3% | ✅ ganada | +9.61 |
| wr0ngw4yb3tt0r | Arsenal FC vs. Manchester City: O/U 2.5 | Under (BUY) | 49% | 10.00 | 53.4% | ⏳ pendiente | — |
| HomeRunHazard | Portland Fire vs. Phoenix Mercury: O/U 1 | Under (BUY) | 50% | 10.00 | 0.6% | ⏳ pendiente | — |
