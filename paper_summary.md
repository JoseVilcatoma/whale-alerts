# Paper trading — resultado de la simulación

Actualizado: 2026-08-17 19:13:05 (hora de Perú)

**Bankroll inicial:** $1,000.00
**Bankroll actual:** $829.64
**Retorno acumulado:** -17.04%
**Peor caída desde un máximo (drawdown):** 34.31%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $10.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $800.00 en 80 posiciones abiertas (disponible para nuevas apuestas: $29.64)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 23 | 7 | 0 | +48.43 USD |
| swisstony | 15 | 2 | 5 | +43.70 USD |
| 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 | 3 | 0 | 0 | +22.19 USD |
| casualbet2020 | 2 | 0 | 0 | +21.67 USD |
| 3edmond.dantes | 1 | 0 | 0 | +11.28 USD |
| bigspending | 1 | 0 | 0 | +10.83 USD |
| Dota2winner | 1 | 0 | 0 | +9.61 USD |
| crisp1973 | 1 | 0 | 0 | +9.61 USD |
| MaoZeDonK | 1 | 0 | 0 | +6.39 USD |
| IMAREALPERSON | 9 | 5 | 0 | +5.80 USD |
| alaskabaked | 1 | 1 | 0 | +3.67 USD |
| CORGI8 | 4 | 6 | 0 | +1.20 USD |
| HVAB | 2 | 0 | 0 | +0.20 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 0 | 0 | 4 | +0.00 USD |
| AV23IUa | 0 | 0 | 1 | +0.00 USD |
| 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 | 9 | 9 | 0 | -0.36 USD |
| SDTrading | 2 | 2 | 1 | -1.87 USD |
| 1winstreak1 | 7 | 7 | 0 | -5.25 USD |
| Sassy-Bucket | 4 | 7 | 1 | -9.88 USD |
| TeGeeLP | 0 | 1 | 0 | -10.00 USD |
| Lakersfan111 | 10 | 10 | 0 | -15.25 USD |
| SineNooneEI | 1 | 2 | 0 | -17.50 USD |
| 111111111115 | 11 | 11 | 1 | -23.43 USD |
| HomeRunHazard | 22 | 13 | 7 | -26.28 USD |
| midwicket72 | 3 | 4 | 0 | -26.82 USD |
| RN1 | 42 | 21 | 26 | -27.24 USD |
| g42gh6524h5h5 | 9 | 10 | 0 | -37.06 USD |
| wr0ngw4yb3tt0r | 10 | 16 | 0 | -64.24 USD |
| ferrariChampions2026 | 55 | 45 | 34 | -99.82 USD |

## Análisis general

- **Apuestas resueltas:** 406
- **Aciertos:** 232 (57.1%)
- **Cuota promedio de entrada:** 58.6%
- **Stake promedio:** $10.00
- **Total apostado (suma de stakes):** $4,060.00
- **ROI sobre lo apostado:** -5.28%

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 1-19% (bomba) | 3 | 0.0% | 14.7% | -14.7 pp |
| 20-39% | 42 | 21.4% | 32.3% | -10.8 pp |
| 40-59% | 188 | 48.4% | 49.5% | -1.1 pp |
| 60-79% | 119 | 68.1% | 69.3% | -1.3 pp |
| 80-94% | 40 | 92.5% | 86.4% | +6.1 pp |
| 95-99% (casi seguro) | 14 | 100.0% | 98.0% | +2.0 pp |

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
| wta-shnaide-chwalin-2026-08-17 | HVAB, RN1, ferrariChampions2026 |
| mlb-bal-tb-2026-08-17 | RN1, alaskabaked, ferrariChampions2026 |
| mlb-oak-kc-2026-08-17 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, RN1, ferrariChampions2026 |
| mlb-bal-tb-2026-08-17-spread-home-1pt5 | RN1, ferrariChampions2026 |
| wta-noskova-tauson-2026-08-17 | RN1, ferrariChampions2026 |
| bra-int-cre-2026-08-17-total-4pt5 | RN1, ferrariChampions2026 |
| bra-int-cre-2026-08-17-int | RN1, ferrariChampions2026 |
| mlb-ari-bos-2026-08-17-total-7pt5 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, ferrariChampions2026 |
| bra-int-cre-2026-08-17-cre | RN1, ferrariChampions2026 |
| mlb-cws-chc-2026-08-17 | RN1, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| RN1 | Chicago White Sox vs. Chicago Cubs: O/U  | Over (BUY) | 54% | 10.00 | 2.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Arizona Diamondbacks vs. Boston Red Sox: | Over (BUY) | 49% | 10.00 | 1.3% | ⏳ pendiente | — |
| RN1 | Will Clube do Remo win on 2026-08-17? | No (BUY) | 98% | 10.00 | 0.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Chicago White Sox vs. Chicago Cubs: O/U  | Under (BUY) | 53% | 10.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Chicago White Sox vs. Chicago Cubs | Chicago Cubs (BUY) | 59% | 10.00 | 0.2% | ⏳ pendiente | — |
| RN1 | Chicago White Sox vs. Chicago Cubs | Chicago Cubs (BUY) | 59% | 10.00 | 0.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: Kansas City Royals (-2.5) | Athletics (BUY) | 43% | 10.00 | 0.8% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Felipe Meligeni Alves vs Luka Pa | Luka Pavlovic (BUY) | 64% | 10.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Athletics vs. Kansas City Royals | Kansas City Royals (BUY) | 82% | 10.00 | 0.9% | ⏳ pendiente | — |
| RN1 | Spread: New York Mets (-1.5) | San Diego Padres (BUY) | 57% | 10.00 | 0.5% | ⏳ pendiente | — |
| RN1 | Will CD Universidad Catolica del Ecuador | Yes (BUY) | 47% | 10.00 | 0.4% | ⏳ pendiente | — |
| RN1 | Athletics vs. Kansas City Royals | Kansas City Royals (BUY) | 82% | 10.00 | 0.6% | ⏳ pendiente | — |
| ferrariChampions2026 | San Diego Padres vs. New York Mets | New York Mets (BUY) | 65% | 10.00 | 0.2% | ⏳ pendiente | — |
| RN1 | Spread: Cincinnati Reds (-1.5) | St. Louis Cardinals (BUY) | 90% | 10.00 | 0.9% | ⏳ pendiente | — |
| RN1 | CA Vélez Sarsfield vs. CSyD Defensa y Ju | Under (BUY) | 68% | 10.00 | 2.9% | ⏳ pendiente | — |
| ferrariChampions2026 | San Diego Padres vs. New York Mets | San Diego Padres (BUY) | 42% | 10.00 | 0.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Rinky Hijikata vs Jakub | Jakub Mensik (BUY) | 89% | 10.00 | 1.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Set 1 Winner: Noskova vs Tauson | Noskova (BUY) | 72% | 10.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Atlanta Braves vs. Minnesota Twins | Minnesota Twins (BUY) | 45% | 10.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Will Clube do Remo win on 2026-08-17? | No (BUY) | 98% | 10.00 | 0.6% | ⏳ pendiente | — |
| ferrariChampions2026 | SC Internacional vs. Clube do Remo: O/U  | Over (BUY) | 90% | 10.00 | 0.4% | ⏳ pendiente | — |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | Arizona Diamondbacks vs. Boston Red Sox: | Under (BUY) | 50% | 10.00 | 1.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Arizona Diamondbacks vs. Boston Red Sox: | Over (BUY) | 53% | 10.00 | 3.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Kingston: Blaise Bicknell vs Max Purcell | Max Purcell (BUY) | 81% | 10.00 | 0.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: New York Mets (-2.5) | San Diego Padres (BUY) | 72% | 10.00 | 1.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Will SC Internacional win on 2026-08-17? | Yes (BUY) | 83% | 10.00 | 1.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Linda Noskova vs Clara  | Clara Tauson (BUY) | 46% | 10.00 | 1.0% | ⏳ pendiente | — |
| RN1 | Guarani FC SP vs. Ypiranga FC RS: 1st Ha | Under (BUY) | 92% | 10.00 | 0.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Emma Navarro vs Jessica | Jessica Pegula (BUY) | 89% | 10.00 | 3.2% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Linda Noskova vs Clara  | Clara Tauson (BUY) | 50% | 10.00 | 0.7% | ⏳ pendiente | — |
