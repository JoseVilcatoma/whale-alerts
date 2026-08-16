# Paper trading — resultado de la simulación

Actualizado: 2026-08-16 05:55:12 (hora de Perú)

**Bankroll inicial:** $1,000.00
**Bankroll actual:** $884.42
**Retorno acumulado:** -11.56%
**Peor caída desde un máximo (drawdown):** 20.89%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $10.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $490.00 en 49 posiciones abiertas (disponible para nuevas apuestas: $394.42)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 23 | 9 | 3 | +42.91 USD |
| 111111111115 | 10 | 5 | 7 | +33.24 USD |
| bigspending | 1 | 0 | 1 | +10.83 USD |
| Sassy-Bucket | 2 | 3 | 0 | +9.29 USD |
| Lakersfan111 | 7 | 6 | 8 | +4.62 USD |
| 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 | 1 | 0 | 0 | +3.89 USD |
| CORGI8 | 4 | 6 | 0 | +1.20 USD |
| SineNooneEI | 0 | 0 | 2 | +0.00 USD |
| 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 | 9 | 9 | 0 | -0.36 USD |
| SDTrading | 2 | 2 | 0 | -1.87 USD |
| 1winstreak1 | 7 | 7 | 0 | -5.25 USD |
| HomeRunHazard | 7 | 3 | 7 | -5.58 USD |
| g42gh6524h5h5 | 9 | 7 | 5 | -7.06 USD |
| TeGeeLP | 0 | 1 | 0 | -10.00 USD |
| midwicket72 | 1 | 2 | 1 | -18.10 USD |
| IMAREALPERSON | 5 | 5 | 2 | -24.78 USD |
| ferrariChampions2026 | 37 | 33 | 0 | -44.40 USD |
| RN1 | 14 | 12 | 12 | -49.94 USD |
| wr0ngw4yb3tt0r | 10 | 15 | 1 | -54.24 USD |

## Análisis general

- **Apuestas resueltas:** 246
- **Aciertos:** 130 (52.8%)
- **Cuota promedio de entrada:** 54.0%
- **Stake promedio:** $10.00
- **Total apostado (suma de stakes):** $2,460.00
- **ROI sobre lo apostado:** -6.01%

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 1-19% (bomba) | 3 | 0.0% | 14.7% | -14.7 pp |
| 20-39% | 40 | 22.5% | 32.3% | -9.8 pp |
| 40-59% | 125 | 49.6% | 49.4% | +0.2 pp |
| 60-79% | 56 | 67.9% | 68.3% | -0.4 pp |
| 80-94% | 17 | 94.1% | 85.8% | +8.4 pp |
| 95-99% (casi seguro) | 5 | 100.0% | 97.0% | +3.0 pp |

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
| dota2-lgd-ty-2026-08-16 | Lakersfan111, SineNooneEI |
| lol-lgd-jdg-2026-08-16-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, g42gh6524h5h5 |
| lol-t1-gen-2026-08-16 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, 111111111115 |
| lol-t1-gen-2026-08-16-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, 111111111115, g42gh6524h5h5 |
| atp-dougaz-matsuok-2026-08-16 | HomeRunHazard, RN1 |
| lol-lgd-jdg-2026-08-16 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, g42gh6524h5h5 |
| lol-t1-gen-2026-08-16-game2 | IMAREALPERSON, g42gh6524h5h5 |
| lol-drx-bro2-2026-08-16-game1 | IMAREALPERSON, SineNooneEI |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| RN1 | ITF M25 Muttenz Men: Luca Staeheli vs Lo | Luca Staeheli (BUY) | 75% | 10.00 | 2.0% | ⏳ pendiente | — |
| SineNooneEI | LoL: Kiwoom DRX vs HANJIN BRION - Game 1 | HANJIN BRION (BUY) | 52% | 10.00 | 9.4% | ⏳ pendiente | — |
| RN1 | Prague: Jiri Cizek vs Norbert Gombos | Norbert Gombos (BUY) | 86% | 10.00 | 2.9% | ⏳ pendiente | — |
| IMAREALPERSON | LoL: Kiwoom DRX vs HANJIN BRION - Game 1 | Kiwoom DRX (BUY) | 49% | 10.00 | 23.5% | ⏳ pendiente | — |
| RN1 | Sion: Nicolas Parizzia vs Theo Papamalam | Nicolas Parizzia (BUY) | 48% | 10.00 | 1.9% | ⏳ pendiente | — |
| RN1 | ADO Den Haag vs. FC Groningen: O/U 2.5 | Over (BUY) | 73% | 10.00 | 2.5% | ⏳ pendiente | — |
| RN1 | Sion: Michael Zhu vs Thiago Cigarran | Thiago Cigarran (BUY) | 73% | 10.00 | 5.2% | ⏳ pendiente | — |
| IMAREALPERSON | LoL: Weibo Gaming vs Invictus Gaming - G | Weibo Gaming (BUY) | 52% | 10.00 | 46.0% | 💰 vendida anticipada | -2.12 |
| RN1 | ITF W35 Bydgoszcz Women: Daria Kuczer vs | Yelyzaveta Kotliar (BUY) | 86% | 10.00 | 3.1% | ⏳ pendiente | — |
| HomeRunHazard | Miami Marlins vs. Cincinnati Reds: O/U 9 | Under (BUY) | 55% | 10.00 | 0.7% | ⏳ pendiente | — |
| HomeRunHazard | Astana: Aziz Dougaz vs Hayato Matsuoka | Hayato Matsuoka (BUY) | 94% | 10.00 | 5.9% | ✅ ganada | +0.64 |
| HomeRunHazard | New York Yankees vs. Toronto Blue Jays:  | Under (BUY) | 54% | 10.00 | 3.2% | ⏳ pendiente | — |
| RN1 | ITF M15 Malmö Men: Karl Friberg vs John  | Karl Friberg (BUY) | 90% | 10.00 | 4.2% | ⏳ pendiente | — |
| RN1 | Will CA Barracas Central win on 2026-08- | No (BUY) | 64% | 10.00 | 3.3% | ⏳ pendiente | — |
| RN1 | ITF M25 Idanha-a-Nova Men: Dan Added vs  | Philip Henning (BUY) | 96% | 10.00 | 5.0% | ✅ ganada | +0.42 |
| IMAREALPERSON | LoL: T1 vs Gen.G - Game 2 Winner | T1 (BUY) | 55% | 10.00 | 23.7% | 💰 vendida anticipada | -5.64 |
| bigspending | Will Incheon United FC win on 2026-08-16 | Yes (BUY) | 46% | 10.00 | 90.8% | ⏳ pendiente | — |
| IMAREALPERSON | Valorant: Cloud9 vs Evil Geniuses (BO3)  | Evil Geniuses (BUY) | 50% | 10.00 | 71.4% | ⏳ pendiente | — |
| RN1 | Sion: Gerard Campana Lee vs Franco Riber | Gerard Campana Lee (BUY) | 96% | 10.00 | 2.6% | ✅ ganada | +0.42 |
| IMAREALPERSON | LoL: T1 vs Gen.G - Game 2 Winner | T1 (BUY) | 52% | 10.00 | 89.0% | 💰 vendida anticipada | +1.54 |
| g42gh6524h5h5 | LoL: T1 vs Gen.G - Game 2 Winner | Gen.G (BUY) | 58% | 10.00 | 112.7% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: LGD Gaming vs JD Gaming (BO3) - LPL | LGD Gaming (BUY) | 52% | 10.00 | 6.3% | ⏳ pendiente | — |
| g42gh6524h5h5 | LoL: LGD Gaming vs JD Gaming (BO3) - LPL | LGD Gaming (BUY) | 41% | 10.00 | 38.5% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: LGD Gaming vs JD Gaming (BO3) - LPL | LGD Gaming (BUY) | 43% | 10.00 | 62.9% | 💰 vendida anticipada | +1.40 |
| HomeRunHazard | Astana: Aziz Dougaz vs Hayato Matsuoka | Aziz Dougaz (BUY) | 41% | 10.00 | 0.9% | ❌ perdida | -10.00 |
| RN1 | ITF M25 Kursumlijska Banja 3 Men: Sean C | Stefan Horia Haita (BUY) | 61% | 10.00 | 2.2% | ⏳ pendiente | — |
| HomeRunHazard | Prague: Matyas Kozlovsky vs Javier Barra | Javier Barranco Cosano (BUY) | 91% | 10.00 | 2.4% | ✅ ganada | +0.99 |
| RN1 | Astana: Aziz Dougaz vs Hayato Matsuoka | Aziz Dougaz (BUY) | 67% | 10.00 | 11.1% | ❌ perdida | -10.00 |
| RN1 | ITF W35 Bydgoszcz Women: Daria Kuczer vs | Daria Kuczer (BUY) | 50% | 10.00 | 1.0% | ⏳ pendiente | — |
| g42gh6524h5h5 | LoL: T1 vs Gen.G - Game 1 Winner | T1 (BUY) | 69% | 10.00 | 220.6% | ⏳ pendiente | — |
