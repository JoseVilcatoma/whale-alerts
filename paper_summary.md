# Paper trading — resultado de la simulación

Actualizado: 2026-08-16 04:36:25 (hora de Perú)

**Bankroll inicial:** $1,000.00
**Bankroll actual:** $905.58
**Retorno acumulado:** -9.44%
**Peor caída desde un máximo (drawdown):** 20.18%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $10.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $450.00 en 45 posiciones abiertas (disponible para nuevas apuestas: $455.58)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 23 | 9 | 3 | +42.91 USD |
| 111111111115 | 10 | 5 | 7 | +33.24 USD |
| bigspending | 1 | 0 | 1 | +10.83 USD |
| Sassy-Bucket | 2 | 3 | 0 | +9.29 USD |
| 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 | 1 | 0 | 0 | +3.89 USD |
| HomeRunHazard | 5 | 2 | 7 | +2.79 USD |
| Lakersfan111 | 6 | 6 | 9 | +1.63 USD |
| CORGI8 | 4 | 6 | 0 | +1.20 USD |
| SineNooneEI | 0 | 0 | 1 | +0.00 USD |
| 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 | 9 | 9 | 0 | -0.36 USD |
| SDTrading | 2 | 2 | 0 | -1.87 USD |
| 1winstreak1 | 7 | 7 | 0 | -5.25 USD |
| g42gh6524h5h5 | 9 | 7 | 5 | -7.06 USD |
| TeGeeLP | 0 | 1 | 0 | -10.00 USD |
| midwicket72 | 1 | 2 | 1 | -18.10 USD |
| IMAREALPERSON | 4 | 3 | 2 | -18.56 USD |
| RN1 | 11 | 10 | 8 | -40.39 USD |
| ferrariChampions2026 | 37 | 33 | 0 | -44.40 USD |
| wr0ngw4yb3tt0r | 10 | 15 | 1 | -54.24 USD |

## Análisis general

- **Apuestas resueltas:** 237
- **Aciertos:** 124 (52.3%)
- **Cuota promedio de entrada:** 53.1%
- **Stake promedio:** $10.00
- **Total apostado (suma de stakes):** $2,370.00
- **ROI sobre lo apostado:** -5.61%

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 1-19% (bomba) | 3 | 0.0% | 14.7% | -14.7 pp |
| 20-39% | 40 | 22.5% | 32.3% | -9.8 pp |
| 40-59% | 123 | 49.6% | 49.4% | +0.1 pp |
| 60-79% | 54 | 68.5% | 68.1% | +0.4 pp |
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
| dota2-lgd-ty-2026-08-16 | Lakersfan111, SineNooneEI |
| lol-lgd-jdg-2026-08-16-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, g42gh6524h5h5 |
| lol-t1-gen-2026-08-16 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, 111111111115 |
| lol-t1-gen-2026-08-16-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, 111111111115, g42gh6524h5h5 |
| atp-dougaz-matsuok-2026-08-16 | HomeRunHazard, RN1 |
| lol-lgd-jdg-2026-08-16 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, g42gh6524h5h5 |
| lol-t1-gen-2026-08-16-game2 | IMAREALPERSON, g42gh6524h5h5 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| bigspending | Will Incheon United FC win on 2026-08-16 | Yes (BUY) | 46% | 10.00 | 10.8% | ⏳ pendiente | — |
| IMAREALPERSON | Valorant: Cloud9 vs Evil Geniuses (BO3)  | Evil Geniuses (BUY) | 50% | 10.00 | 71.4% | ⏳ pendiente | — |
| RN1 | Sion: Gerard Campana Lee vs Franco Riber | Gerard Campana Lee (BUY) | 96% | 10.00 | 2.6% | ⏳ pendiente | — |
| IMAREALPERSON | LoL: T1 vs Gen.G - Game 2 Winner | T1 (BUY) | 52% | 10.00 | 89.0% | ⏳ pendiente | — |
| g42gh6524h5h5 | LoL: T1 vs Gen.G - Game 2 Winner | Gen.G (BUY) | 58% | 10.00 | 112.7% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: LGD Gaming vs JD Gaming (BO3) - LPL | LGD Gaming (BUY) | 52% | 10.00 | 6.3% | ⏳ pendiente | — |
| g42gh6524h5h5 | LoL: LGD Gaming vs JD Gaming (BO3) - LPL | LGD Gaming (BUY) | 41% | 10.00 | 38.5% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: LGD Gaming vs JD Gaming (BO3) - LPL | LGD Gaming (BUY) | 43% | 10.00 | 62.9% | 💰 vendida anticipada | +1.40 |
| HomeRunHazard | Astana: Aziz Dougaz vs Hayato Matsuoka | Aziz Dougaz (BUY) | 41% | 10.00 | 0.9% | ⏳ pendiente | — |
| RN1 | ITF M25 Kursumlijska Banja 3 Men: Sean C | Stefan Horia Haita (BUY) | 61% | 10.00 | 2.2% | ⏳ pendiente | — |
| HomeRunHazard | Prague: Matyas Kozlovsky vs Javier Barra | Javier Barranco Cosano (BUY) | 91% | 10.00 | 2.4% | ⏳ pendiente | — |
| RN1 | Astana: Aziz Dougaz vs Hayato Matsuoka | Aziz Dougaz (BUY) | 67% | 10.00 | 11.1% | ⏳ pendiente | — |
| RN1 | ITF W35 Bydgoszcz Women: Daria Kuczer vs | Daria Kuczer (BUY) | 50% | 10.00 | 1.0% | ⏳ pendiente | — |
| g42gh6524h5h5 | LoL: T1 vs Gen.G - Game 1 Winner | T1 (BUY) | 69% | 10.00 | 220.6% | ⏳ pendiente | — |
| g42gh6524h5h5 | LoL: T1 vs Gen.G - Game 1 Winner | Gen.G (BUY) | 73% | 10.00 | 38.3% | ⏳ pendiente | — |
| g42gh6524h5h5 | LoL: LGD Gaming vs JD Gaming - Game 2 Wi | JD Gaming (BUY) | 66% | 10.00 | 34.2% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: LGD Gaming vs JD Gaming (BO3) - LPL | JD Gaming (BUY) | 89% | 10.00 | 12.2% | 💰 vendida anticipada | -3.15 |
| RN1 | Astana: Aziz Dougaz vs Hayato Matsuoka | Hayato Matsuoka (BUY) | 51% | 10.00 | 20.2% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: T1 vs Gen.G - Game 1 Winner | Gen.G (BUY) | 72% | 10.00 | 66.7% | ⏳ pendiente | — |
| RN1 | ITF W15 Bucharest 3 Women: Maria Sara Po | Maria Sara Popa (BUY) | 70% | 10.00 | 7.4% | ✅ ganada | +4.29 |
| 111111111115 | LoL: T1 vs Gen.G (BO3) - LCK Round 3-4 L | Gen.G (BUY) | 59% | 10.00 | 0.6% | ⏳ pendiente | — |
| 111111111115 | LoL: T1 vs Gen.G - Game 1 Winner | Gen.G (BUY) | 59% | 10.00 | 16.1% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: T1 vs Gen.G (BO3) - LCK Round 3-4 L | Gen.G (BUY) | 58% | 10.00 | 106.0% | 💰 vendida anticipada | +1.55 |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: LGD Gaming vs JD Gaming - Game 2 Wi | JD Gaming (BUY) | 64% | 10.00 | 162.1% | ⏳ pendiente | — |
| RN1 | Prague: Marek Gengel vs Svyatoslav Gulin | Svyatoslav Gulin (BUY) | 51% | 10.00 | 1.9% | ⏳ pendiente | — |
| SineNooneEI | Dota 2: LGD Gaming vs Team Yandex (BO3)  | Team Yandex (BUY) | 73% | 10.00 | 125.3% | ⏳ pendiente | — |
| RN1 | ITF W15 Tianjin 2 Women: Chengyiyi Yuan  | Thasaporn Naklo (BUY) | 83% | 10.00 | 2.7% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: LGD Gaming vs JD Gaming - Game 1 Wi | JD Gaming (BUY) | 80% | 10.00 | 6.7% | 💰 vendida anticipada | -1.50 |
| HomeRunHazard | Kansas City Royals vs. Los Angeles Angel | Over (BUY) | 48% | 10.00 | 0.8% | ⏳ pendiente | — |
| midwicket72 | Metro Bank One Day Cup: Leicestershire v | Leicestershire (BUY) | 47% | 10.00 | 15.3% | ⏳ pendiente | — |
