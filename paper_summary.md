# Paper trading — resultado de la simulación

Actualizado: 2026-08-17 16:50:12 (hora de Perú)

**Bankroll inicial:** $1,000.00
**Bankroll actual:** $763.04
**Retorno acumulado:** -23.70%
**Peor caída desde un máximo (drawdown):** 34.31%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $10.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $510.00 en 51 posiciones abiertas (disponible para nuevas apuestas: $253.04)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 23 | 7 | 0 | +48.43 USD |
| swisstony | 12 | 2 | 3 | +38.88 USD |
| 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 | 3 | 0 | 0 | +22.19 USD |
| casualbet2020 | 2 | 0 | 0 | +21.67 USD |
| bigspending | 1 | 0 | 0 | +10.83 USD |
| Dota2winner | 1 | 0 | 0 | +9.61 USD |
| crisp1973 | 1 | 0 | 0 | +9.61 USD |
| MaoZeDonK | 1 | 0 | 0 | +6.39 USD |
| IMAREALPERSON | 9 | 5 | 0 | +5.80 USD |
| 3edmond.dantes | 1 | 1 | 0 | +1.28 USD |
| CORGI8 | 4 | 6 | 0 | +1.20 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 0 | 0 | 3 | +0.00 USD |
| alaskabaked | 0 | 0 | 2 | +0.00 USD |
| 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 | 9 | 9 | 0 | -0.36 USD |
| HVAB | 0 | 1 | 0 | -0.62 USD |
| SDTrading | 2 | 2 | 1 | -1.87 USD |
| 1winstreak1 | 7 | 7 | 0 | -5.25 USD |
| Sassy-Bucket | 4 | 7 | 1 | -9.88 USD |
| TeGeeLP | 0 | 1 | 0 | -10.00 USD |
| Lakersfan111 | 10 | 10 | 0 | -15.25 USD |
| SineNooneEI | 1 | 2 | 0 | -17.50 USD |
| 111111111115 | 11 | 11 | 0 | -23.43 USD |
| HomeRunHazard | 22 | 13 | 7 | -26.28 USD |
| midwicket72 | 3 | 4 | 0 | -26.82 USD |
| RN1 | 39 | 21 | 1 | -33.45 USD |
| g42gh6524h5h5 | 9 | 10 | 0 | -37.06 USD |
| wr0ngw4yb3tt0r | 10 | 16 | 0 | -64.24 USD |
| ferrariChampions2026 | 56 | 50 | 33 | -140.88 USD |

## Análisis general

- **Apuestas resueltas:** 404
- **Aciertos:** 224 (55.4%)
- **Cuota promedio de entrada:** 58.1%
- **Stake promedio:** $10.00
- **Total apostado (suma de stakes):** $4,040.00
- **ROI sobre lo apostado:** -7.09%

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 1-19% (bomba) | 3 | 0.0% | 14.7% | -14.7 pp |
| 20-39% | 42 | 21.4% | 32.3% | -10.8 pp |
| 40-59% | 191 | 47.6% | 49.5% | -1.9 pp |
| 60-79% | 120 | 66.7% | 69.3% | -2.6 pp |
| 80-94% | 37 | 89.2% | 86.6% | +2.6 pp |
| 95-99% (casi seguro) | 11 | 100.0% | 98.0% | +2.0 pp |

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
| atp-papoe-cerny-2026-08-17 | HomeRunHazard, RN1 |
| atp-fatic-donald-2026-08-17 | HomeRunHazard, RN1, swisstony |
| atp-ribeiro-nagal-2026-08-17 | RN1, ferrariChampions2026 |
| itf-aleksey-boschma-2026-08-17 | 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000, RN1 |
| mlb-det-pit-2026-08-17 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, ferrariChampions2026 |
| wta-parry-boisson-2026-08-17 | HomeRunHazard, ferrariChampions2026, swisstony |
| wta-swiatek-sakkari-2026-08-17 | HomeRunHazard, ferrariChampions2026 |
| mlb-stl-cin-2026-05-24-total-9pt5 | Sassy-Bucket, ferrariChampions2026 |
| wta-cirstea-kalinsk-2026-08-17 | HVAB, alaskabaked, ferrariChampions2026 |
| lal-dep-elc-2026-08-17-dep | 3edmond.dantes, ferrariChampions2026 |
| mlb-stl-cin-2026-05-24 | alaskabaked, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| ferrariChampions2026 | Cincinnati Open: Brandon Nakashima vs Da | Brandon Nakashima (BUY) | 46% | 10.00 | 0.9% | ⏳ pendiente | — |
| swisstony | Will CA Lanús win on 2026-08-17? | No (BUY) | 99% | 10.00 | 0.2% | ⏳ pendiente | — |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | Spread: Los Angeles Dodgers (-1.5) | Los Angeles Dodgers (BUY) | 63% | 10.00 | 14.2% | ⏳ pendiente | — |
| swisstony | CA Lanús vs. CA Independiente: O/U 3.5 | Under (BUY) | 51% | 10.00 | 1.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: New York Mets (-1.5) | San Diego Padres (BUY) | 65% | 10.00 | 1.5% | ⏳ pendiente | — |
| HVAB | Cincinnati Open: Sorana Cirstea vs Anna  | Sorana Cirstea (BUY) | 64% | 10.00 | 310.3% | 💰 vendida anticipada | -0.62 |
| ferrariChampions2026 | Cincinnati Open: Sorana Cirstea vs Anna  | Sorana Cirstea (BUY) | 41% | 10.00 | 10.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Palermo FC vs. US Lecce: O/U 2.5 | Under (BUY) | 47% | 10.00 | 0.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Magdalena Frech vs Elen | Elena Rybakina (BUY) | 82% | 10.00 | 9.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Kingston: Elias Ymer vs Paul Jubb | Paul Jubb (BUY) | 49% | 10.00 | 0.6% | ⏳ pendiente | — |
| ferrariChampions2026 | UD Almería vs. CD Eldense: O/U 4.5 | Under (BUY) | 53% | 10.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Stefanos Sakellaridis vs Ka | Karl Poling (BUY) | 47% | 10.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: ENJOY vs HAVU (BO3) - CC | ENJOY (BUY) | 87% | 10.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Will RC Deportivo A Coruña win on 2026-0 | Yes (BUY) | 74% | 10.00 | 1.7% | ❌ perdida | -10.00 |
| ferrariChampions2026 | Spread: RC Deportivo A Coruña (-1.5) | Elche CF (BUY) | 78% | 10.00 | 0.2% | ✅ ganada | +2.82 |
| ferrariChampions2026 | Quebec City: Stefanos Sakellaridis vs Ka | Stefanos Sakellaridis (BUY) | 85% | 10.00 | 3.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Kingston: Dan Martin vs Lautaro Midon | Lautaro Midon (BUY) | 93% | 10.00 | 1.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Cardiff City FC vs. Wrexham AFC: O/U 4.5 | Under (BUY) | 94% | 10.00 | 0.2% | ⏳ pendiente | — |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | Athletics vs. Kansas City Royals | Kansas City Royals (BUY) | 64% | 10.00 | 121.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Will Samsunspor win on 2026-08-17? | No (BUY) | 68% | 10.00 | 0.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Set 1 Winner: Fery vs Minaur | Fery (BUY) | 51% | 10.00 | 0.2% | ❌ perdida | -10.00 |
| ferrariChampions2026 | Will Wrexham AFC win on 2026-08-17? | Yes (BUY) | 63% | 10.00 | 0.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Cardiff City FC vs. Wrexham AFC: O/U 1.5 | Over (BUY) | 91% | 10.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Will Cardiff City FC win on 2026-08-17? | No (BUY) | 88% | 10.00 | 1.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Sion: Dimitris Sakellaridis vs Oleksandr | Dimitris Sakellaridis (BUY) | 53% | 10.00 | 2.9% | ❌ perdida | -10.00 |
| ferrariChampions2026 | St. Louis Cardinals vs. Cincinnati Reds | St. Louis Cardinals (BUY) | 70% | 10.00 | 7.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Will RC Deportivo A Coruña vs. Elche CF  | No (BUY) | 79% | 10.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | RC Deportivo A Coruña vs. Elche CF: O/U  | Over (BUY) | 81% | 10.00 | 1.6% | ✅ ganada | +2.35 |
| ferrariChampions2026 | Cincinnati Open: Diana Shnaider vs Maja  | Diana Shnaider (BUY) | 89% | 10.00 | 3.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Sorana Cirstea vs Anna  | Anna Kalinskaya (BUY) | 41% | 10.00 | 2.5% | ⏳ pendiente | — |
