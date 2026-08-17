# Paper trading — resultado de la simulación

Actualizado: 2026-08-17 10:38:00 (hora de Perú)

**Bankroll inicial:** $1,000.00
**Bankroll actual:** $787.05
**Retorno acumulado:** -21.30%
**Peor caída desde un máximo (drawdown):** 34.31%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $10.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $580.00 en 58 posiciones abiertas (disponible para nuevas apuestas: $207.05)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 23 | 7 | 0 | +48.43 USD |
| 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 | 3 | 0 | 0 | +22.19 USD |
| casualbet2020 | 2 | 0 | 0 | +21.67 USD |
| 3edmond.dantes | 1 | 0 | 0 | +11.28 USD |
| bigspending | 1 | 0 | 0 | +10.83 USD |
| swisstony | 6 | 1 | 11 | +10.75 USD |
| Dota2winner | 1 | 0 | 0 | +9.61 USD |
| crisp1973 | 1 | 0 | 0 | +9.61 USD |
| IMAREALPERSON | 9 | 5 | 1 | +5.80 USD |
| CORGI8 | 4 | 6 | 0 | +1.20 USD |
| HVAB | 1 | 0 | 2 | +0.68 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 0 | 0 | 1 | +0.00 USD |
| MaoZeDonK | 0 | 0 | 1 | +0.00 USD |
|  | 0 | 0 | 4 | +0.00 USD |
| 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 | 9 | 9 | 0 | -0.36 USD |
| SDTrading | 2 | 2 | 3 | -1.87 USD |
| 1winstreak1 | 7 | 7 | 0 | -5.25 USD |
| Sassy-Bucket | 4 | 7 | 1 | -9.88 USD |
| TeGeeLP | 0 | 1 | 0 | -10.00 USD |
| Lakersfan111 | 10 | 10 | 0 | -15.25 USD |
| SineNooneEI | 0 | 2 | 0 | -20.00 USD |
| 111111111115 | 11 | 11 | 0 | -23.43 USD |
| midwicket72 | 3 | 4 | 0 | -26.82 USD |
| RN1 | 41 | 22 | 3 | -35.92 USD |
| g42gh6524h5h5 | 9 | 10 | 0 | -37.06 USD |
| HomeRunHazard | 18 | 13 | 16 | -48.93 USD |
| wr0ngw4yb3tt0r | 10 | 16 | 0 | -64.24 USD |
| ferrariChampions2026 | 39 | 36 | 15 | -66.03 USD |

## Análisis general

- **Apuestas resueltas:** 362
- **Aciertos:** 197 (54.4%)
- **Cuota promedio de entrada:** 56.8%
- **Stake promedio:** $10.00
- **Total apostado (suma de stakes):** $3,620.00
- **ROI sobre lo apostado:** -7.29%

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 1-19% (bomba) | 3 | 0.0% | 14.7% | -14.7 pp |
| 20-39% | 42 | 21.4% | 32.3% | -10.8 pp |
| 40-59% | 178 | 47.8% | 49.5% | -1.7 pp |
| 60-79% | 101 | 65.3% | 69.0% | -3.6 pp |
| 80-94% | 29 | 96.6% | 86.9% | +9.7 pp |
| 95-99% (casi seguro) | 9 | 100.0% | 97.7% | +2.3 pp |

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
| wnba-por-phx-2026-08-16 | HomeRunHazard, Sassy-Bucket |
| lol-ly-sen-2026-08-16-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, ChonkyChocolateCake |
| val-c9-eg2-2026-08-16-game2 | IMAREALPERSON, casualbet2020 |
| mex-tij-caz-2026-08-16-total-3pt5 | ferrariChampions2026, swisstony |
| mex-tij-caz-2026-08-16-caz | RN1, swisstony |
| mex-tij-caz-2026-08-16-tij | RN1, swisstony |
| atp-blockx-cobolli-2026-08-17 | ferrariChampions2026, swisstony |
| mlb-atl-min-2026-08-17-spread-away-1pt5 | HomeRunHazard, SDTrading |
| atp-papoe-cerny-2026-08-17 | HomeRunHazard, RN1 |
| atp-fatic-donald-2026-08-17 | HomeRunHazard, RN1, swisstony |
| wnba-dal-gsv-2026-08-17-total-163pt5 | , HomeRunHazard |
| atp-ribeiro-nagal-2026-08-17 | HomeRunHazard, RN1, ferrariChampions2026, swisstony |
| itf-aleksey-boschma-2026-08-17 | 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000, RN1 |
| mlb-det-pit-2026-08-17 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, HomeRunHazard |
| lol-t1-dnf-2026-08-17-game4 | MaoZeDonK, ferrariChampions2026 |
| atp-langmo-boitan-2026-08-17 | HomeRunHazard, RN1 |
| atp-radulov-monday-2026-08-17 | HomeRunHazard, ferrariChampions2026 |
| atp-tirante-landalu-2026-08-17 | , ferrariChampions2026 |
| atp-filip-hardt-2026-08-17 | HomeRunHazard, swisstony |
| wta-swiatek-sakkari-2026-08-17 | ferrariChampions2026, swisstony |
| wta-parry-boisson-2026-08-17 | HomeRunHazard, ferrariChampions2026, swisstony |
| itf-tikhon-olmo-2026-08-17 | HVAB, swisstony |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| HomeRunHazard | Cincinnati Open: Diane Parry vs Lois Boi | Lois Boisson (BUY) | 74% | 10.00 | 6.4% | ⏳ pendiente | — |
| HomeRunHazard | Spread: Golden State Valkyries (-5.5) | Golden State Valkyries (BUY) | 54% | 10.00 | 1.4% | ⏳ pendiente | — |
| swisstony | ITF W50 Prague Women: Anastasia Tikhonov | Anastasia Tikhonova (BUY) | 99% | 10.00 | 0.5% | ⏳ pendiente | — |
| HVAB | ITF W50 Prague Women: Anastasia Tikhonov | Anastasia Tikhonova (BUY) | 98% | 10.00 | 2542.2% | ⏳ pendiente | — |
| swisstony | Will IF Gnistan win on 2026-08-17? | No (BUY) | 69% | 10.00 | 0.3% | ⏳ pendiente | — |
| HomeRunHazard | Prague 2: Jakub Filip vs Nick Hardt | Nick Hardt (BUY) | 98% | 10.00 | 1.2% | ⏳ pendiente | — |
| HomeRunHazard | Spread: Golden State Valkyries (-7.5) | Golden State Valkyries (BUY) | 45% | 10.00 | 0.8% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Thiago Agustin Tirante  | Martin Landaluce (BUY) | 62% | 10.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Alexander Blockx vs Fla | Flavio Cobolli (BUY) | 49% | 10.00 | 0.3% | ⏳ pendiente | — |
| swisstony | IF Gnistan vs. Tampereen Ilves: O/U 3.5 | Over (BUY) | 72% | 10.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Diane Parry vs Lois Boi | Diane Parry (BUY) | 47% | 10.00 | 0.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Stefano Napolitano vs Ugo B | Ugo Blanchet (BUY) | 49% | 10.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Stefano Napolitano vs Ugo B | Stefano Napolitano (BUY) | 51% | 10.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Alexander Blockx vs Fla | Alexander Blockx (BUY) | 49% | 10.00 | 4.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Iga Swiatek vs Maria Sa | Iga Swiatek (BUY) | 91% | 10.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Roehampton: Iliyan Radulov vs Johannus M | Johannus Monday (BUY) | 65% | 10.00 | 1.6% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: Natus Vincere vs Team Heretics (BO3 | Natus Vincere (BUY) | 71% | 10.00 | 4.3% | ⏳ pendiente | — |
| swisstony | Cincinnati Open: Diane Parry vs Lois Boi | Diane Parry (BUY) | 50% | 10.00 | 1.0% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: Natus Vincere vs Team Heretics - Ga | Natus Vincere (BUY) | 65% | 10.00 | 5.8% | ⏳ pendiente | — |
| SDTrading | Spread: Atlanta Braves (-1.5) | Minnesota Twins (BUY) | 59% | 10.00 | 16.3% | ⏳ pendiente | — |
| IMAREALPERSON | Game Handicap: Navi (-1.5) vs Team Heret | Team Heretics (BUY) | 57% | 10.00 | 14.2% | ⏳ pendiente | — |
| swisstony | Cincinnati Open: Iga Swiatek vs Maria Sa | Iga Swiatek (BUY) | 89% | 10.00 | 1.5% | ⏳ pendiente | — |
|  | Dallas Wings vs. Golden State Valkyries: | Under (BUY) | 54% | 10.00 | 2.2% | ⏳ pendiente | — |
| swisstony | IF Gnistan vs. Tampereen Ilves: O/U 2.5 | Over (BUY) | 80% | 10.00 | 2.4% | ⏳ pendiente | — |
|  | Will Pisa SC win on 2026-08-17? | Yes (BUY) | 58% | 10.00 | 20.2% | ⏳ pendiente | — |
| swisstony | Prague 2: Jakub Filip vs Nick Hardt | Nick Hardt (BUY) | 94% | 10.00 | 0.8% | ⏳ pendiente | — |
| HVAB | ITF W35 Krakow Women: Gaia Maduzzi vs Sa | Gaia Maduzzi (BUY) | 98% | 10.00 | 74.7% | ⏳ pendiente | — |
| swisstony | IF Gnistan vs. Tampereen Ilves: O/U 3.5 | Under (BUY) | 63% | 10.00 | 0.8% | ⏳ pendiente | — |
| swisstony | IF Gnistan vs. Tampereen Ilves: O/U 1.5 | Over (BUY) | 84% | 10.00 | 0.6% | ⏳ pendiente | — |
| Sassy-Bucket | St. Louis Cardinals vs. Cincinnati Reds: | Under (BUY) | 53% | 10.00 | 394.3% | ⏳ pendiente | — |
