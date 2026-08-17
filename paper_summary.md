# Paper trading — resultado de la simulación

Actualizado: 2026-08-17 02:20:57 (hora de Perú)

**Bankroll inicial:** $1,000.00
**Bankroll actual:** $773.48
**Retorno acumulado:** -22.65%
**Peor caída desde un máximo (drawdown):** 34.31%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $10.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $80.00 en 8 posiciones abiertas (disponible para nuevas apuestas: $693.48)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 23 | 7 | 0 | +48.43 USD |
| casualbet2020 | 2 | 0 | 0 | +21.67 USD |
| 3edmond.dantes | 1 | 0 | 0 | +11.28 USD |
| bigspending | 1 | 0 | 0 | +10.83 USD |
| Dota2winner | 1 | 0 | 0 | +9.61 USD |
| crisp1973 | 1 | 0 | 0 | +9.61 USD |
| 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 | 2 | 0 | 0 | +8.38 USD |
| IMAREALPERSON | 9 | 5 | 0 | +5.80 USD |
| swisstony | 3 | 1 | 2 | +4.32 USD |
| CORGI8 | 4 | 6 | 0 | +1.20 USD |
| 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 | 9 | 9 | 0 | -0.36 USD |
| SDTrading | 2 | 2 | 0 | -1.87 USD |
| 1winstreak1 | 7 | 7 | 0 | -5.25 USD |
| Sassy-Bucket | 4 | 7 | 0 | -9.88 USD |
| TeGeeLP | 0 | 1 | 0 | -10.00 USD |
| Lakersfan111 | 10 | 10 | 0 | -15.25 USD |
| SineNooneEI | 0 | 2 | 0 | -20.00 USD |
| 111111111115 | 11 | 11 | 0 | -23.43 USD |
| midwicket72 | 3 | 4 | 0 | -26.82 USD |
| g42gh6524h5h5 | 9 | 10 | 0 | -37.06 USD |
| HomeRunHazard | 15 | 12 | 3 | -41.35 USD |
| RN1 | 29 | 18 | 2 | -47.77 USD |
| ferrariChampions2026 | 37 | 34 | 1 | -54.40 USD |
| wr0ngw4yb3tt0r | 10 | 16 | 0 | -64.24 USD |

## Análisis general

- **Apuestas resueltas:** 334
- **Aciertos:** 176 (52.7%)
- **Cuota promedio de entrada:** 55.4%
- **Stake promedio:** $10.00
- **Total apostado (suma de stakes):** $3,340.00
- **ROI sobre lo apostado:** -8.29%

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 1-19% (bomba) | 3 | 0.0% | 14.7% | -14.7 pp |
| 20-39% | 42 | 21.4% | 32.3% | -10.8 pp |
| 40-59% | 173 | 47.4% | 49.5% | -2.2 pp |
| 60-79% | 87 | 64.4% | 68.6% | -4.2 pp |
| 80-94% | 22 | 100.0% | 85.9% | +14.1 pp |
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
| wnba-por-phx-2026-08-16 | HomeRunHazard, Sassy-Bucket |
| lol-ly-sen-2026-08-16-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, ChonkyChocolateCake |
| val-c9-eg2-2026-08-16-game2 | IMAREALPERSON, casualbet2020 |
| mex-tij-caz-2026-08-16-total-3pt5 | ferrariChampions2026, swisstony |
| mex-tij-caz-2026-08-16-caz | RN1, swisstony |
| mex-tij-caz-2026-08-16-tij | RN1, swisstony |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| RN1 | ITF W35 Verbier Women: Micol Salvadori v | Micol Salvadori (BUY) | 42% | 10.00 | 1.5% | ⏳ pendiente | — |
| HomeRunHazard | Dallas Wings vs. Golden State Valkyries: | Over (BUY) | 49% | 10.00 | 1.2% | ⏳ pendiente | — |
| swisstony | Cincinnati Open: Alexander Blockx vs Fla | Flavio Cobolli (BUY) | 48% | 10.00 | 0.6% | ⏳ pendiente | — |
| HomeRunHazard | Miami Marlins vs. Philadelphia Phillies: | Under (BUY) | 63% | 10.00 | 1.0% | ⏳ pendiente | — |
| HomeRunHazard | Detroit Tigers vs. Pittsburgh Pirates: O | Under (BUY) | 53% | 10.00 | 1.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Prague: Jakub Paul vs Rudolf Molleker | Jakub Paul (BUY) | 45% | 10.00 | 0.8% | ⏳ pendiente | — |
| RN1 | ITF M25 Taipei Men: Nitin Kumar Sinha vs | Nitin Kumar Sinha (BUY) | 83% | 10.00 | 1.0% | ✅ ganada | +2.05 |
| swisstony | Club Tijuana vs. CF Cruz Azul: O/U 3.5 | Under (BUY) | 49% | 10.00 | 0.7% | ✅ ganada | +10.41 |
| swisstony | Will Club Tijuana win on 2026-08-16? | Yes (BUY) | 71% | 10.00 | 3.5% | ⏳ pendiente | — |
| RN1 | Will Club Tijuana win on 2026-08-16? | Yes (BUY) | 71% | 10.00 | 1.2% | ⏳ pendiente | — |
| RN1 | Will CF Cruz Azul win on 2026-08-16? | No (BUY) | 93% | 10.00 | 6.8% | ✅ ganada | +0.75 |
| swisstony | Club Tijuana vs. CF Cruz Azul: O/U 3.5 | Over (BUY) | 68% | 10.00 | 0.9% | ❌ perdida | -10.00 |
| swisstony | Will CF Cruz Azul win on 2026-08-16? | No (BUY) | 93% | 10.00 | 4.8% | ✅ ganada | +0.75 |
| swisstony | Will Club Tijuana vs. CF Cruz Azul end i | No (BUY) | 76% | 10.00 | 0.3% | ✅ ganada | +3.16 |
| ferrariChampions2026 | Club Tijuana vs. CF Cruz Azul: O/U 3.5 | Over (BUY) | 67% | 10.00 | 0.4% | ❌ perdida | -10.00 |
| casualbet2020 | Valorant: Cloud9 vs Evil Geniuses - Map  | Evil Geniuses (BUY) | 42% | 10.00 | 3.4% | ✅ ganada | +13.81 |
| IMAREALPERSON | Valorant: Cloud9 vs Evil Geniuses - Map  | Evil Geniuses (BUY) | 43% | 10.00 | 9.8% | ✅ ganada | +13.26 |
| HomeRunHazard | Seattle Mariners vs. Houston Astros: O/U | Under (BUY) | 79% | 10.00 | 0.4% | ✅ ganada | +2.66 |
| HomeRunHazard | Seattle Mariners vs. Houston Astros: O/U | Over (BUY) | 47% | 10.00 | 0.5% | ❌ perdida | -10.00 |
| HomeRunHazard | Cincinnati Open: Ben Shelton vs Jaime Fa | Ben Shelton (BUY) | 61% | 10.00 | 4.9% | ❌ perdida | -10.00 |
| HomeRunHazard | Cincinnati Open: Coco Gauff vs Liudmila  | Coco Gauff (BUY) | 74% | 10.00 | 3.6% | ✅ ganada | +3.51 |
| HomeRunHazard | Portland Fire vs. Phoenix Mercury | Phoenix Mercury (BUY) | 48% | 10.00 | 1.1% | ❌ perdida | -10.00 |
| HomeRunHazard | Seattle Mariners vs. Houston Astros | Seattle Mariners (BUY) | 63% | 10.00 | 7.6% | ✅ ganada | +5.87 |
| HomeRunHazard | Seattle Mariners vs. Houston Astros | Houston Astros (BUY) | 41% | 10.00 | 2.1% | ❌ perdida | -10.00 |
| HomeRunHazard | Seattle Mariners vs. Houston Astros: O/U | Over (BUY) | 55% | 10.00 | 0.7% | ❌ perdida | -10.00 |
| HomeRunHazard | Cincinnati Open: Coco Gauff vs Liudmila  | Liudmila Samsonova (BUY) | 57% | 10.00 | 0.3% | ❌ perdida | -10.00 |
| HomeRunHazard | Spread: Seattle Mariners (-1.5) | Houston Astros (BUY) | 58% | 10.00 | 0.7% | ✅ ganada | +7.24 |
| HomeRunHazard | Spread: Seattle Mariners (-2.5) | Houston Astros (BUY) | 73% | 10.00 | 1.8% | ✅ ganada | +3.70 |
| casualbet2020 | Valorant: Cloud9 vs Evil Geniuses - Map  | Cloud9 (BUY) | 56% | 10.00 | 43.3% | ✅ ganada | +7.86 |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: LYON vs Sentinels - Game 2 Winner | LYON (BUY) | 73% | 10.00 | 34.2% | ✅ ganada | +3.70 |
