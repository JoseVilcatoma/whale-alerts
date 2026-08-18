# Paper trading — resultado de la simulación

Actualizado: 2026-08-18 12:44:58 (hora de Perú)

**Bankroll inicial:** $1,000.00
**Bankroll actual:** $817.04
**Retorno acumulado:** -18.30%
**Peor caída desde un máximo (drawdown):** 34.31%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $10.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $600.00 en 60 posiciones abiertas (disponible para nuevas apuestas: $217.04)

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
| sentrio | 1 | 0 | 6 | +9.23 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 3 | 1 | 0 | +8.78 USD |
| swisstony | 27 | 9 | 15 | +8.14 USD |
| SDTrading | 3 | 2 | 0 | +7.00 USD |
| MaoZeDonK | 1 | 0 | 0 | +6.39 USD |
| IMAREALPERSON | 9 | 5 | 0 | +5.80 USD |
| CORGI8 | 4 | 6 | 0 | +1.20 USD |
| HVAB | 3 | 0 | 0 | +0.30 USD |
| GoalLineGhost | 0 | 0 | 4 | +0.00 USD |
| 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 | 9 | 9 | 0 | -0.36 USD |
| Sassy-Bucket | 5 | 7 | 0 | -0.65 USD |
| alaskabaked | 1 | 3 | 0 | -4.53 USD |
| 1winstreak1 | 7 | 7 | 0 | -5.25 USD |
| Lakersfan111 | 11 | 10 | 0 | -6.02 USD |
| RN1 | 84 | 38 | 10 | -6.99 USD |
| TeGeeLP | 0 | 1 | 0 | -10.00 USD |
| AV23IUa | 0 | 1 | 0 | -10.00 USD |
| Kulilun | 0 | 1 | 0 | -10.00 USD |
| SineNooneEI | 1 | 2 | 0 | -17.50 USD |
| danielwolfmorales3pddb6dl6 | 0 | 2 | 3 | -20.00 USD |
| midwicket72 | 3 | 4 | 0 | -26.82 USD |
| HomeRunHazard | 25 | 17 | 1 | -31.87 USD |
| 111111111115 | 12 | 13 | 0 | -33.82 USD |
| g42gh6524h5h5 | 9 | 10 | 0 | -37.06 USD |
| wr0ngw4yb3tt0r | 10 | 16 | 0 | -64.24 USD |
| ferrariChampions2026 | 117 | 74 | 21 | -84.48 USD |

## Análisis general

- **Apuestas resueltas:** 600
- **Aciertos:** 361 (60.2%)
- **Cuota promedio de entrada:** 61.3%
- **Stake promedio:** $9.80
- **Total apostado (suma de stakes):** $5,877.67
- **ROI sobre lo apostado:** -3.72%

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 1-19% (bomba) | 3 | 0.0% | 14.7% | -14.7 pp |
| 20-39% | 42 | 21.4% | 32.3% | -10.8 pp |
| 40-59% | 270 | 49.3% | 49.8% | -0.5 pp |
| 60-79% | 174 | 69.0% | 68.7% | +0.3 pp |
| 80-94% | 78 | 84.6% | 86.6% | -2.0 pp |
| 95-99% (casi seguro) | 33 | 100.0% | 97.5% | +2.5 pp |

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
| lol-sly-tlnpir-2026-08-18 | ferrariChampions2026, sentrio |
| atp-rublev-borges-2026-08-18 | Kulilun, alaskabaked, danielwolfmorales3pddb6dl6, ferrariChampions2026 |
| atp-bruncli-kumstat-2026-08-17 | RN1, ferrariChampions2026 |
| atp-prado-ficovic-2026-08-17 | danielwolfmorales3pddb6dl6, ferrariChampions2026, swisstony |
| wta-siniako-keys-2026-08-18 | ferrariChampions2026, swisstony |
| atp-zheng-musetti-2026-08-18 | RN1, danielwolfmorales3pddb6dl6, ferrariChampions2026, swisstony |
| atp-glinka-bax-2026-08-17 | ferrariChampions2026, sentrio |
| atp-fritz-aguilar-2026-08-18 | ferrariChampions2026, swisstony |
| ucl-fen-lyo-2026-08-18-total-2pt5 | RN1, swisstony |
| atp-lajovic-daniel-2026-08-18 | RN1, ferrariChampions2026 |
| clf-fch-bmu-2026-08-18-total-5pt5 | RN1, ferrariChampions2026 |
| atp-royer-miguel-2026-08-17 | ferrariChampions2026, swisstony |
| clf-fch-bmu-2026-08-18-spread-away-1pt5 | RN1, swisstony |
| clf-fch-bmu-2026-08-18-fch | RN1, swisstony |
| itf-iva-mazzola-2026-08-18 | RN1, ferrariChampions2026 |
| wta-tjen-andreev-2026-08-18 | RN1, swisstony |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| swisstony | Spread: Fenerbahçe SK (-2.5) | Olympique Lyonnais (BUY) | 92% | 10.00 | 0.3% | ⏳ pendiente | — |
| RN1 | Fenerbahçe SK vs. Olympique Lyonnais: O/ | Over (BUY) | 53% | 10.00 | 2.5% | ⏳ pendiente | — |
| swisstony | Will Olympique Lyonnais win on 2026-08-1 | No (BUY) | 75% | 10.00 | 0.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Kingston: Valentin Royer vs Luis Guto Mi | Valentin Royer (BUY) | 94% | 10.00 | 2.5% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Michael Zheng vs Lorenz | Lorenzo Musetti (BUY) | 98% | 10.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Michael Zheng vs Lorenz | Lorenzo Musetti (BUY) | 96% | 10.00 | 2.5% | ⏳ pendiente | — |
| swisstony | Cincinnati Open: Aryna Sabalenka vs Xiny | Aryna Sabalenka (BUY) | 91% | 10.00 | 0.9% | ⏳ pendiente | — |
| RN1 | Quebec City: Dusan Lajovic vs Taro Danie | Taro Daniel (BUY) | 57% | 10.00 | 0.3% | ⏳ pendiente | — |
| swisstony | Cincinnati Open: Janice Tjen vs Mirra An | Mirra Andreeva (BUY) | 96% | 10.00 | 2.2% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Janice Tjen vs Mirra An | Mirra Andreeva (BUY) | 96% | 10.00 | 4.1% | ⏳ pendiente | — |
| RN1 | 1. FC Heidenheim vs. Bayern Munich: O/U  | Under (BUY) | 57% | 10.00 | 1.3% | ⏳ pendiente | — |
| RN1 | Will 1. FC Heidenheim vs. Bayern Munich  | No (BUY) | 94% | 10.00 | 2.6% | ⏳ pendiente | — |
| swisstony | Will 1. FC Heidenheim win on 2026-08-18? | No (BUY) | 99% | 10.00 | 3.2% | ⏳ pendiente | — |
| swisstony | Cincinnati Open: Michael Zheng vs Lorenz | Lorenzo Musetti (BUY) | 91% | 10.00 | 0.7% | ⏳ pendiente | — |
| RN1 | Spread: Bayern Munich (-1.5) | 1. FC Heidenheim (BUY) | 83% | 10.00 | 0.3% | ⏳ pendiente | — |
| RN1 | ITF W35 Bistrita Women: Iva Ivanova vs A | Iva Ivanova (BUY) | 56% | 10.00 | 3.2% | ⏳ pendiente | — |
| ferrariChampions2026 | ITF W35 Bistrita Women: Iva Ivanova vs A | Alessandra Mazzola (BUY) | 46% | 10.00 | 2.9% | ⏳ pendiente | — |
| RN1 | Will 1. FC Heidenheim win on 2026-08-18? | No (BUY) | 95% | 10.00 | 2.2% | ⏳ pendiente | — |
| swisstony | Will Bayern Munich win on 2026-08-18? | No (BUY) | 44% | 10.00 | 0.2% | ⏳ pendiente | — |
| swisstony | Spread: Bayern Munich (-1.5) | 1. FC Heidenheim (BUY) | 80% | 10.00 | 0.8% | ⏳ pendiente | — |
| swisstony | Spread: Bayern Munich (-2.5) | 1. FC Heidenheim (BUY) | 95% | 10.00 | 0.5% | ⏳ pendiente | — |
| swisstony | Kingston: Valentin Royer vs Luis Guto Mi | Valentin Royer (BUY) | 93% | 10.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Kingston: Daniil Glinka vs Florent Bax | Daniil Glinka (BUY) | 76% | 10.00 | 0.9% | ⏳ pendiente | — |
| ferrariChampions2026 | 1. FC Heidenheim vs. Bayern Munich: O/U  | Under (BUY) | 46% | 10.00 | 1.2% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: Bushido Wildcats vs Team Phoenix -  | Bushido Wildcats (BUY) | 84% | 10.00 | 0.5% | ⏳ pendiente | — |
| swisstony | Spread: Bayern Munich (-3.5) | 1. FC Heidenheim (BUY) | 98% | 10.00 | 1.2% | ⏳ pendiente | — |
| swisstony | Cincinnati Open: Taylor Fritz vs Daniel  | Taylor Fritz (BUY) | 89% | 10.00 | 1.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Dusan Lajovic vs Taro Danie | Dusan Lajovic (BUY) | 57% | 10.00 | 7.1% | ⏳ pendiente | — |
| swisstony | Will Al Okhdood SC win on 2026-08-18? | Yes (BUY) | 62% | 10.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: ⁠Movistar KOI Fénix vs Barça eSport | ⁠Movistar KOI Fénix (BUY) | 92% | 10.00 | 0.6% | ⏳ pendiente | — |
