# Paper trading — resultado de la simulación

Actualizado: 2026-08-16 22:01:07 (hora de Perú)

**Bankroll inicial:** $1,000.00
**Bankroll actual:** $712.84
**Retorno acumulado:** -28.72%
**Peor caída desde un máximo (drawdown):** 37.04%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $10.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $270.00 en 27 posiciones abiertas (disponible para nuevas apuestas: $442.84)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 22 | 7 | 1 | +44.73 USD |
| 3edmond.dantes | 1 | 0 | 0 | +11.28 USD |
| bigspending | 1 | 0 | 0 | +10.83 USD |
| Dota2winner | 1 | 0 | 0 | +9.61 USD |
| crisp1973 | 1 | 0 | 0 | +9.61 USD |
| 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 | 2 | 0 | 0 | +8.38 USD |
| CORGI8 | 4 | 6 | 0 | +1.20 USD |
| casualbet2020 | 0 | 0 | 2 | +0.00 USD |
| WTSA | 0 | 0 | 2 | +0.00 USD |
| MaoZeDonK | 0 | 0 | 1 | +0.00 USD |
| 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 | 9 | 9 | 0 | -0.36 USD |
| SDTrading | 2 | 2 | 0 | -1.87 USD |
| 1winstreak1 | 7 | 7 | 0 | -5.25 USD |
| Sassy-Bucket | 4 | 7 | 0 | -9.88 USD |
| TeGeeLP | 0 | 1 | 0 | -10.00 USD |
| Lakersfan111 | 10 | 10 | 0 | -15.25 USD |
| SineNooneEI | 0 | 2 | 0 | -20.00 USD |
| IMAREALPERSON | 7 | 5 | 2 | -20.19 USD |
| 111111111115 | 11 | 11 | 0 | -23.43 USD |
| midwicket72 | 3 | 4 | 0 | -26.82 USD |
| g42gh6524h5h5 | 9 | 9 | 1 | -27.06 USD |
| HomeRunHazard | 15 | 13 | 4 | -51.35 USD |
| ferrariChampions2026 | 38 | 34 | 13 | -53.41 USD |
| RN1 | 26 | 18 | 1 | -53.73 USD |
| wr0ngw4yb3tt0r | 10 | 16 | 0 | -64.24 USD |

## Análisis general

- **Apuestas resueltas:** 323
- **Aciertos:** 166 (51.4%)
- **Cuota promedio de entrada:** 55.1%
- **Stake promedio:** $10.00
- **Total apostado (suma de stakes):** $3,230.00
- **ROI sobre lo apostado:** -10.45%

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 1-19% (bomba) | 3 | 0.0% | 14.7% | -14.7 pp |
| 20-39% | 42 | 21.4% | 32.3% | -10.8 pp |
| 40-59% | 169 | 45.6% | 49.6% | -4.1 pp |
| 60-79% | 82 | 64.6% | 68.3% | -3.7 pp |
| 80-94% | 20 | 100.0% | 85.6% | +14.4 pp |
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
| mlb-sea-hou-2026-08-16 | HomeRunHazard, ferrariChampions2026 |
| val-c9-eg2-2026-08-16-game2 | IMAREALPERSON, casualbet2020, ferrariChampions2026 |
| mls-sea-vwh-2026-08-16-vwh | WTSA, ferrariChampions2026 |
| wta-valento-svitoli-2026-08-16 | HomeRunHazard, ferrariChampions2026 |
| val-c9-eg2-2026-08-16 | MaoZeDonK, ferrariChampions2026 |
| atp-sonego-tiafoe-2026-08-16 | HomeRunHazard, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| ferrariChampions2026 | Seattle Sounders FC vs. Vancouver Whitec | Over (BUY) | 56% | 10.00 | 1.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Tereza Valentova vs Eli | Tereza Valentova (BUY) | 73% | 10.00 | 3.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: ALKA vs QUINTESSÊNCIA (B | ALKA (BUY) | 61% | 10.00 | 0.9% | ⏳ pendiente | — |
| MaoZeDonK | Valorant: Cloud9 vs Evil Geniuses (BO3)  | Cloud9 (BUY) | 44% | 10.00 | 9.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Valorant: Cloud9 vs Evil Geniuses (BO3)  | Evil Geniuses (BUY) | 56% | 10.00 | 7.2% | ⏳ pendiente | — |
| HomeRunHazard | Cincinnati Open: Lorenzo Sonego vs Franc | Frances Tiafoe (BUY) | 60% | 10.00 | 9.5% | ⏳ pendiente | — |
| HomeRunHazard | Cincinnati Open: Lorenzo Sonego vs Franc | Lorenzo Sonego (BUY) | 41% | 10.00 | 0.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Lorenzo Sonego vs Franc | Lorenzo Sonego (BUY) | 42% | 10.00 | 1.4% | ⏳ pendiente | — |
| WTSA | Will CF Cruz Azul win on 2026-08-16? | No (BUY) | 61% | 10.00 | 14.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Lorenzo Sonego vs Franc | Frances Tiafoe (BUY) | 64% | 10.00 | 3.6% | ⏳ pendiente | — |
| HomeRunHazard | Sonego vs. Tiafoe: Match O/U 23.5 | Over (BUY) | 51% | 10.00 | 0.5% | ⏳ pendiente | — |
| HomeRunHazard | Cincinnati Open: Tereza Valentova vs Eli | Elina Svitolina (BUY) | 81% | 10.00 | 3.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Seattle Mariners vs. Houston Astros | Seattle Mariners (BUY) | 91% | 10.00 | 0.3% | ✅ ganada | +0.99 |
| ferrariChampions2026 | Seattle Mariners vs. Houston Astros: O/U | Over (BUY) | 66% | 10.00 | 3.4% | ❌ perdida | -10.00 |
| HomeRunHazard | Spread: Seattle Mariners (-1.5) | Seattle Mariners (BUY) | 47% | 10.00 | 2.3% | ❌ perdida | -10.00 |
| ferrariChampions2026 | Austin FC vs. FC Dallas: O/U 2.5 | Over (BUY) | 48% | 10.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Valorant: Cloud9 vs Evil Geniuses (BO3)  | Cloud9 (BUY) | 73% | 10.00 | 4.5% | ⏳ pendiente | — |
| WTSA | Will Vancouver Whitecaps FC win on 2026- | Yes (BUY) | 54% | 10.00 | 4.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Tereza Valentova vs Eli | Elina Svitolina (BUY) | 82% | 10.00 | 14.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: FC Dallas (-1.5) | Austin FC (BUY) | 67% | 10.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Will Vancouver Whitecaps FC win on 2026- | No (BUY) | 51% | 10.00 | 1.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Valorant: Cloud9 vs Evil Geniuses - Map  | Cloud9 (BUY) | 56% | 10.00 | 0.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Valorant: Cloud9 vs Evil Geniuses - Map  | Evil Geniuses (BUY) | 43% | 10.00 | 0.8% | ⏳ pendiente | — |
| casualbet2020 | Valorant: Cloud9 vs Evil Geniuses - Map  | Evil Geniuses (BUY) | 42% | 10.00 | 3.4% | ⏳ pendiente | — |
| IMAREALPERSON | Valorant: Cloud9 vs Evil Geniuses - Map  | Evil Geniuses (BUY) | 43% | 10.00 | 9.8% | ⏳ pendiente | — |
| HomeRunHazard | Seattle Mariners vs. Houston Astros: O/U | Under (BUY) | 79% | 10.00 | 0.4% | ✅ ganada | +2.66 |
| HomeRunHazard | Seattle Mariners vs. Houston Astros: O/U | Over (BUY) | 47% | 10.00 | 0.5% | ❌ perdida | -10.00 |
| HomeRunHazard | Cincinnati Open: Ben Shelton vs Jaime Fa | Ben Shelton (BUY) | 61% | 10.00 | 4.9% | ❌ perdida | -10.00 |
| HomeRunHazard | Cincinnati Open: Coco Gauff vs Liudmila  | Coco Gauff (BUY) | 74% | 10.00 | 3.6% | ✅ ganada | +3.51 |
| HomeRunHazard | Portland Fire vs. Phoenix Mercury | Phoenix Mercury (BUY) | 48% | 10.00 | 1.1% | ❌ perdida | -10.00 |
