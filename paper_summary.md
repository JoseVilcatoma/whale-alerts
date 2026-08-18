# Paper trading — resultado de la simulación

Actualizado: 2026-08-17 20:57:34 (hora de Perú)

**Bankroll inicial:** $1,000.00
**Bankroll actual:** $826.23
**Retorno acumulado:** -17.38%
**Peor caída desde un máximo (drawdown):** 34.31%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $10.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $641.65 en 76 posiciones abiertas (disponible para nuevas apuestas: $184.58)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 23 | 7 | 0 | +48.43 USD |
| swisstony | 17 | 2 | 10 | +46.30 USD |
| 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 | 3 | 0 | 0 | +22.19 USD |
| casualbet2020 | 2 | 0 | 0 | +21.67 USD |
| 3edmond.dantes | 1 | 0 | 0 | +11.28 USD |
| bigspending | 1 | 0 | 0 | +10.83 USD |
| Dota2winner | 1 | 0 | 0 | +9.61 USD |
| crisp1973 | 1 | 0 | 0 | +9.61 USD |
| MaoZeDonK | 1 | 0 | 0 | +6.39 USD |
| IMAREALPERSON | 9 | 5 | 0 | +5.80 USD |
| alaskabaked | 1 | 1 | 1 | +3.67 USD |
| CORGI8 | 4 | 6 | 0 | +1.20 USD |
| HVAB | 3 | 0 | 0 | +0.30 USD |
| AV23IUa | 0 | 0 | 1 | +0.00 USD |
| 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 | 9 | 9 | 0 | -0.36 USD |
| Sassy-Bucket | 5 | 7 | 0 | -0.65 USD |
| SDTrading | 2 | 2 | 1 | -1.87 USD |
| 1winstreak1 | 7 | 7 | 0 | -5.25 USD |
| TeGeeLP | 0 | 1 | 0 | -10.00 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 0 | 1 | 3 | -10.00 USD |
| Lakersfan111 | 10 | 10 | 0 | -15.25 USD |
| SineNooneEI | 1 | 2 | 0 | -17.50 USD |
| midwicket72 | 3 | 4 | 0 | -26.82 USD |
| RN1 | 52 | 25 | 29 | -28.86 USD |
| 111111111115 | 11 | 12 | 0 | -33.43 USD |
| g42gh6524h5h5 | 9 | 10 | 0 | -37.06 USD |
| HomeRunHazard | 22 | 15 | 5 | -46.28 USD |
| wr0ngw4yb3tt0r | 10 | 16 | 0 | -64.24 USD |
| ferrariChampions2026 | 70 | 52 | 26 | -73.51 USD |

## Análisis general

- **Apuestas resueltas:** 450
- **Aciertos:** 261 (58.0%)
- **Cuota promedio de entrada:** 59.2%
- **Stake promedio:** $9.99
- **Total apostado (suma de stakes):** $4,496.02
- **ROI sobre lo apostado:** -4.84%

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 1-19% (bomba) | 3 | 0.0% | 14.7% | -14.7 pp |
| 20-39% | 42 | 21.4% | 32.3% | -10.8 pp |
| 40-59% | 209 | 47.8% | 49.6% | -1.7 pp |
| 60-79% | 132 | 68.9% | 69.3% | -0.4 pp |
| 80-94% | 46 | 93.5% | 86.3% | +7.2 pp |
| 95-99% (casi seguro) | 18 | 100.0% | 97.9% | +2.1 pp |

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
| mlb-det-pit-2026-08-17 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, AV23IUa, RN1, ferrariChampions2026 |
| wta-parry-boisson-2026-08-17 | HomeRunHazard, ferrariChampions2026, swisstony |
| wta-swiatek-sakkari-2026-08-17 | HomeRunHazard, ferrariChampions2026 |
| mlb-stl-cin-2026-05-24-total-9pt5 | Sassy-Bucket, ferrariChampions2026 |
| wta-cirstea-kalinsk-2026-08-17 | alaskabaked, ferrariChampions2026, swisstony |
| arg-vel-def-2026-08-17-total-2pt5 | RN1, ferrariChampions2026 |
| atp-jodar-tabilo-2026-08-17 | RN1, ferrariChampions2026, swisstony |
| atp-fery-minaur-2026-08-17 | HVAB, RN1, ferrariChampions2026 |
| mlb-sd-nym-2026-08-17 | 111111111115, ferrariChampions2026 |
| arg-gye-tal-2026-08-17-tal | RN1, ferrariChampions2026, swisstony |
| wta-shnaide-chwalin-2026-08-17 | HVAB, RN1, ferrariChampions2026 |
| mlb-mia-phi-2026-08-17 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, RN1 |
| atp-alves-pavlovi-2026-08-17 | HVAB, ferrariChampions2026 |
| mlb-bal-tb-2026-08-17 | RN1, alaskabaked, ferrariChampions2026 |
| mlb-oak-kc-2026-08-17 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, RN1, ferrariChampions2026 |
| mlb-bal-tb-2026-08-17-spread-home-1pt5 | RN1, ferrariChampions2026 |
| mlb-stl-cin-2026-08-17 | RN1, ferrariChampions2026 |
| wta-noskova-tauson-2026-08-17 | RN1, ferrariChampions2026 |
| bra-int-cre-2026-08-17-total-4pt5 | RN1, ferrariChampions2026 |
| bra-int-cre-2026-08-17-int | RN1, ferrariChampions2026, swisstony |
| mlb-sd-nym-2026-08-17-spread-home-2pt5 | RN1, ferrariChampions2026 |
| mlb-ari-bos-2026-08-17-total-7pt5 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, ferrariChampions2026 |
| bra-int-cre-2026-08-17-total-1pt5 | RN1, ferrariChampions2026 |
| bra-int-cre-2026-08-17-cre | RN1, ferrariChampions2026 |
| mlb-atl-min-2026-08-17 | RN1, ferrariChampions2026 |
| atp-hijikat-mensik-2026-08-17 | RN1, ferrariChampions2026 |
| mlb-cws-chc-2026-08-17 | RN1, alaskabaked, ferrariChampions2026 |
| atp-zverev-atmane-2026-08-17 | RN1, ferrariChampions2026 |
| mex-nec-leo-2026-08-17-first-half-total-2pt5 | RN1, swisstony |
| atp-lehecka-fils-2026-08-17 | RN1, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| ferrariChampions2026 | Los Angeles Dodgers vs. Colorado Rockies | Over (BUY) | 50% | 10.00 | 0.6% | ⏳ pendiente | — |
| RN1 | Atlanta Braves vs. Minnesota Twins | Minnesota Twins (BUY) | 71% | 10.00 | 1.1% | ⏳ pendiente | — |
| RN1 | Atlanta Braves vs. Minnesota Twins: O/U  | Under (BUY) | 51% | 10.00 | 0.4% | ⏳ pendiente | — |
| RN1 | Will CA Talleres win on 2026-08-17? | No (BUY) | 99% | 10.00 | 0.3% | ⏳ pendiente | — |
| RN1 | Will CD Huachipato win on 2026-08-17? | No (BUY) | 99% | 10.00 | 0.2% | ⏳ pendiente | — |
| RN1 | Los Angeles Dodgers vs. Colorado Rockies | Los Angeles Dodgers (BUY) | 93% | 10.00 | 0.3% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Alexandra Eala vs Amand | Alexandra Eala (BUY) | 48% | 10.00 | 2.1% | ⏳ pendiente | — |
| RN1 | Miami Marlins vs. Philadelphia Phillies | Philadelphia Phillies (BUY) | 96% | 10.00 | 1.1% | ⏳ pendiente | — |
| RN1 | Spread: New York Mets (-2.5) | San Diego Padres (BUY) | 84% | 10.00 | 4.1% | ✅ ganada | +1.90 |
| RN1 | Spread: Philadelphia Phillies (-2.5) | Miami Marlins (BUY) | 71% | 10.00 | 2.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Club Necaxa vs. Club León FC: O/U 1.5 | Over (BUY) | 72% | 1.24 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Detroit Tigers vs. Pittsburgh Pirates: O | Over (BUY) | 43% | 10.00 | 0.2% | ✅ ganada | +13.26 |
| RN1 | CSD Macara vs. CD Universidad Catolica d | Over (BUY) | 72% | 0.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Chicago White Sox vs. Chicago Cubs | Chicago White Sox (BUY) | 56% | 0.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Jiri Lehecka vs Arthur  | Arthur Fils (BUY) | 63% | 0.00 | 5.6% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Jiri Lehecka vs Arthur  | Arthur Fils (BUY) | 63% | 0.00 | 4.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Will CA Talleres win on 2026-08-17? | No (BUY) | 99% | 0.00 | 0.3% | ⏳ pendiente | — |
| alaskabaked | Chicago White Sox vs. Chicago Cubs | Chicago White Sox (BUY) | 54% | 0.00 | 11.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Will Club León FC win on 2026-08-17? | No (BUY) | 62% | 0.00 | 0.5% | ⏳ pendiente | — |
| swisstony | CSD Macara vs. CD Universidad Catolica d | Over (BUY) | 78% | 0.00 | 0.2% | ⏳ pendiente | — |
| swisstony | Will CA Gimnasia y Esgrima de Mendoza wi | Yes (BUY) | 86% | 0.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: David Jorda Sanchis vs Alan Maga | Alan Magadan (BUY) | 55% | 2.60 | 1.6% | ⏳ pendiente | — |
| ferrariChampions2026 | St. Louis Cardinals vs. Cincinnati Reds | St. Louis Cardinals (BUY) | 79% | 10.00 | 3.0% | ⏳ pendiente | — |
| swisstony | Club Necaxa vs. Club León FC: 1st Half O | Under (BUY) | 89% | 10.00 | 0.3% | ⏳ pendiente | — |
| RN1 | Club Necaxa vs. Club León FC: 1st Half O | Under (BUY) | 88% | 10.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Miami Marlins vs. Philadelphia Phillies: | Under (BUY) | 53% | 6.02 | 1.1% | ❌ perdida | -6.02 |
| RN1 | Miami Marlins vs. Philadelphia Phillies: | Under (BUY) | 65% | 10.00 | 0.5% | ❌ perdida | -10.00 |
| ferrariChampions2026 | SC Internacional vs. Clube do Remo: O/U  | Under (BUY) | 61% | 10.00 | 0.2% | ⏳ pendiente | — |
| HVAB | Cancun: Felipe Meligeni Alves vs Luka Pa | Felipe Meligeni Alves (BUY) | 99% | 10.00 | 8.8% | ✅ ganada | +0.10 |
| swisstony | Will SC Internacional win on 2026-08-17? | Yes (BUY) | 89% | 10.00 | 1.9% | ⏳ pendiente | — |
