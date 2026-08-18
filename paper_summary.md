# Paper trading — resultado de la simulación

Actualizado: 2026-08-18 10:40:33 (hora de Perú)

**Bankroll inicial:** $1,000.00
**Bankroll actual:** $824.90
**Retorno acumulado:** -17.51%
**Peor caída desde un máximo (drawdown):** 34.31%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $10.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $200.00 en 20 posiciones abiertas (disponible para nuevas apuestas: $624.90)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 23 | 7 | 0 | +48.43 USD |
| 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 | 4 | 0 | 0 | +28.32 USD |
| casualbet2020 | 2 | 0 | 0 | +21.67 USD |
| 3edmond.dantes | 1 | 0 | 0 | +11.28 USD |
| bigspending | 1 | 0 | 0 | +10.83 USD |
| Dota2winner | 1 | 0 | 0 | +9.61 USD |
| crisp1973 | 1 | 0 | 0 | +9.61 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 3 | 1 | 0 | +8.78 USD |
| swisstony | 25 | 9 | 0 | +7.41 USD |
| SDTrading | 3 | 2 | 0 | +7.00 USD |
| MaoZeDonK | 1 | 0 | 0 | +6.39 USD |
| IMAREALPERSON | 9 | 5 | 0 | +5.80 USD |
| alaskabaked | 1 | 2 | 0 | +3.67 USD |
| CORGI8 | 4 | 6 | 0 | +1.20 USD |
| HVAB | 3 | 0 | 0 | +0.30 USD |
| sentrio | 0 | 0 | 4 | +0.00 USD |
| GoalLineGhost | 0 | 0 | 4 | +0.00 USD |
| Kulilun | 0 | 0 | 1 | +0.00 USD |
| 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 | 9 | 9 | 0 | -0.36 USD |
| Sassy-Bucket | 5 | 7 | 0 | -0.65 USD |
| 1winstreak1 | 7 | 7 | 0 | -5.25 USD |
| RN1 | 84 | 38 | 1 | -6.99 USD |
| TeGeeLP | 0 | 1 | 0 | -10.00 USD |
| AV23IUa | 0 | 1 | 0 | -10.00 USD |
| Lakersfan111 | 10 | 10 | 1 | -15.25 USD |
| SineNooneEI | 1 | 2 | 0 | -17.50 USD |
| midwicket72 | 3 | 4 | 0 | -26.82 USD |
| HomeRunHazard | 25 | 17 | 1 | -31.87 USD |
| 111111111115 | 11 | 12 | 2 | -33.43 USD |
| g42gh6524h5h5 | 9 | 10 | 0 | -37.06 USD |
| wr0ngw4yb3tt0r | 10 | 16 | 0 | -64.24 USD |
| ferrariChampions2026 | 107 | 71 | 6 | -96.02 USD |

## Análisis general

- **Apuestas resueltas:** 578
- **Aciertos:** 346 (59.9%)
- **Cuota promedio de entrada:** 61.1%
- **Stake promedio:** $9.79
- **Total apostado (suma de stakes):** $5,657.67
- **ROI sobre lo apostado:** -3.87%

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 1-19% (bomba) | 3 | 0.0% | 14.7% | -14.7 pp |
| 20-39% | 42 | 21.4% | 32.3% | -10.8 pp |
| 40-59% | 260 | 48.8% | 49.8% | -0.9 pp |
| 60-79% | 168 | 69.6% | 68.8% | +0.9 pp |
| 80-94% | 77 | 84.4% | 86.6% | -2.2 pp |
| 95-99% (casi seguro) | 28 | 100.0% | 97.5% | +2.5 pp |

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
| arg-gye-tal-2026-08-17-tal | ferrariChampions2026, swisstony |
| wta-shnaide-chwalin-2026-08-17 | HVAB, RN1, ferrariChampions2026 |
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
| lol-ns-dnf-2026-08-18 | Lakersfan111, ferrariChampions2026, sentrio |
| wta-eala-anisimo-2026-08-17 | RN1, ferrariChampions2026, swisstony |
| atp-paul-vallejo-2026-08-17 | RN1, ferrariChampions2026, swisstony |
| itf-hanleil-osminki-2026-08-18 | 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000, RN1 |
| mex-pac-pue-2026-08-17-pue | RN1, swisstony |
| mex-pac-pue-2026-08-17-pac | RN1, swisstony |
| mex-pac-pue-2026-08-17-total-4pt5 | RN1, swisstony |
| atp-bruncli-kumstat-2026-08-17 | RN1, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| ferrariChampions2026 | Counter-Strike: SPARTA vs MOUZ NXT (BO3) | SPARTA (BUY) | 83% | 10.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Prague 2: Oriol Roca Batalla vs Radu Mih | Oriol Roca Batalla (BUY) | 49% | 10.00 | 3.8% | ⏳ pendiente | — |
| ferrariChampions2026 | Arizona Diamondbacks vs. Boston Red Sox: | Under (BUY) | 53% | 10.00 | 4.1% | ⏳ pendiente | — |
| RN1 | ITF W50 Prague Women: Lucie Havlickova v | Lucie Havlickova (BUY) | 95% | 10.00 | 0.8% | ✅ ganada | +0.53 |
| ferrariChampions2026 | Prague 2: Petr Brunclik vs Jan Kumstat | Petr Brunclik (BUY) | 43% | 10.00 | 6.7% | ❌ perdida | -10.00 |
| RN1 | ITF M15 Kursumlijska Banja 12 Men: Dimit | Dimitar Kisimov (BUY) | 53% | 10.00 | 0.4% | ✅ ganada | +8.87 |
| RN1 | Prague 2: Petr Brunclik vs Jan Kumstat | Petr Brunclik (BUY) | 41% | 10.00 | 0.9% | ❌ perdida | -10.00 |
| RN1 | Prague 2: Petr Brunclik vs Jan Kumstat | Jan Kumstat (BUY) | 57% | 10.00 | 5.5% | ✅ ganada | +7.54 |
| ferrariChampions2026 | Prague 2: Petr Brunclik vs Jan Kumstat | Jan Kumstat (BUY) | 56% | 10.00 | 1.7% | ✅ ganada | +7.86 |
| ferrariChampions2026 | Roehampton: Alec Deckers vs Patrick Brad | Patrick Brady (BUY) | 84% | 10.00 | 2.6% | ✅ ganada | +1.90 |
| ferrariChampions2026 | Roehampton: Yuta Shimizu vs Anton Matuse | Anton Matusevich (BUY) | 55% | 10.00 | 1.2% | ✅ ganada | +8.18 |
| Kulilun | Cincinnati Open: Andrey Rublev vs Nuno B | Andrey Rublev (BUY) | 64% | 10.00 | 116.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Roehampton: Michael Geerts vs Billy Blay | Michael Geerts (BUY) | 59% | 10.00 | 1.8% | ✅ ganada | +6.95 |
| ferrariChampions2026 | KBO: Kia Tigers vs. Hanwha Eagles | Kia Tigers (BUY) | 69% | 10.00 | 1.6% | ✅ ganada | +4.49 |
| sentrio | Will Fenerbahçe SK win on 2026-08-18? | No (BUY) | 52% | 10.00 | 1.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Sion: Ognjen Milic vs Lucio Ratti | Lucio Ratti (BUY) | 68% | 10.00 | 0.6% | ✅ ganada | +4.71 |
| ferrariChampions2026 | Counter-Strike: MASONIC vs Bebop (BO3) - | MASONIC (BUY) | 61% | 10.00 | 1.3% | ✅ ganada | +6.39 |
| ferrariChampions2026 | Sion: Dimitar Kuzmanov vs Marvin Moeller | Dimitar Kuzmanov (BUY) | 66% | 10.00 | 4.5% | ✅ ganada | +5.15 |
| GoalLineGhost | Fenerbahçe SK vs. Olympique Lyonnais: O/ | Under (BUY) | 85% | 10.00 | 8.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Prague 2: Javier Barranco Cosano vs Mart | Javier Barranco Cosano (BUY) | 58% | 10.00 | 4.1% | ✅ ganada | +7.24 |
| ferrariChampions2026 | Counter-Strike: MASONIC vs Bebop (BO3) - | Bebop (BUY) | 60% | 10.00 | 0.6% | ❌ perdida | -10.00 |
| GoalLineGhost | Will GNK Dinamo Zagreb win on 2026-08-18 | Yes (BUY) | 57% | 10.00 | 7.8% | ⏳ pendiente | — |
| ferrariChampions2026 | ITF W75 Kursumlijska Banja 3 Women: Sami | Samira De Stefano (BUY) | 68% | 10.00 | 1.1% | ✅ ganada | +4.71 |
| ferrariChampions2026 | LoL: Nongshim Red Force vs DN SOOPers -  | DN SOOPers (BUY) | 67% | 10.00 | 0.6% | ⏳ pendiente | — |
| ferrariChampions2026 | ITF W35 Verbier Women: Cristina Pescucci | Franziska Sziedat (BUY) | 97% | 10.00 | 0.3% | ✅ ganada | +0.31 |
| ferrariChampions2026 | Sion: Dominic Stephan Stricker vs Raphae | Dominic Stephan Stricker (BUY) | 96% | 10.00 | 0.5% | ✅ ganada | +0.42 |
| ferrariChampions2026 | LoL: Nongshim Red Force vs DN SOOPers (B | DN SOOPers (BUY) | 86% | 10.00 | 1.3% | ⏳ pendiente | — |
| GoalLineGhost | Fenerbahçe SK vs. Olympique Lyonnais: O/ | Under (BUY) | 67% | 10.00 | 6.9% | ⏳ pendiente | — |
| sentrio | Los Angeles Sparks vs. Connecticut Sun:  | Under (BUY) | 52% | 10.00 | 1.3% | ⏳ pendiente | — |
| ferrariChampions2026 | ITF W15 Logrono Women: Victoria Gomez O' | Victoria Gomez O'Hayon (BUY) | 80% | 10.00 | 1.9% | ✅ ganada | +2.50 |
