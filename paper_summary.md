# Paper trading — resultado de la simulación

Actualizado: 2026-08-16 02:20:01 (hora de Perú)

**Bankroll inicial:** $1,000.00
**Bankroll actual:** $922.13
**Retorno acumulado:** -7.79%
**Peor caída desde un máximo (drawdown):** 17.46%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $10.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $260.00 en 26 posiciones abiertas (disponible para nuevas apuestas: $662.13)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 21 | 6 | 0 | +44.73 USD |
| 111111111115 | 8 | 4 | 8 | +30.12 USD |
| Lakersfan111 | 6 | 5 | 10 | +11.63 USD |
| bigspending | 1 | 0 | 0 | +10.83 USD |
| Sassy-Bucket | 2 | 3 | 0 | +9.29 USD |
| 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 | 1 | 0 | 0 | +3.89 USD |
| HomeRunHazard | 5 | 2 | 3 | +2.79 USD |
| CORGI8 | 4 | 6 | 0 | +1.20 USD |
| 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 | 9 | 9 | 0 | -0.36 USD |
| SDTrading | 2 | 2 | 0 | -1.87 USD |
| 1winstreak1 | 7 | 7 | 0 | -5.25 USD |
| g42gh6524h5h5 | 9 | 7 | 0 | -7.06 USD |
| TeGeeLP | 0 | 1 | 0 | -10.00 USD |
| midwicket72 | 1 | 2 | 0 | -18.10 USD |
| IMAREALPERSON | 4 | 3 | 0 | -18.56 USD |
| RN1 | 9 | 9 | 3 | -42.54 USD |
| wr0ngw4yb3tt0r | 10 | 14 | 2 | -44.24 USD |
| ferrariChampions2026 | 37 | 33 | 0 | -44.40 USD |

## Análisis general

- **Apuestas resueltas:** 229
- **Aciertos:** 120 (52.4%)
- **Cuota promedio de entrada:** 52.9%
- **Stake promedio:** $10.00
- **Total apostado (suma de stakes):** $2,290.00
- **ROI sobre lo apostado:** -5.16%

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 1-19% (bomba) | 3 | 0.0% | 14.7% | -14.7 pp |
| 20-39% | 39 | 23.1% | 32.5% | -9.4 pp |
| 40-59% | 120 | 49.2% | 49.4% | -0.2 pp |
| 60-79% | 50 | 70.0% | 67.7% | +2.3 pp |
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

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| RN1 | ITF M15 Tianjin 2 Men: Kosuke Ogura vs O | Omar Jasika (BUY) | 56% | 10.00 | 1.9% | ⏳ pendiente | — |
| HomeRunHazard | Chicago Sky vs. Seattle Storm | Chicago Sky (BUY) | 54% | 10.00 | 1.0% | ⏳ pendiente | — |
| Lakersfan111 | LoL: Top Esports vs EDward Gaming (BO3)  | Top Esports (BUY) | 84% | 10.00 | 3.1% | ⏳ pendiente | — |
| HomeRunHazard | Milwaukee Brewers vs. Los Angeles Dodger | Los Angeles Dodgers (BUY) | 62% | 10.00 | 0.9% | ⏳ pendiente | — |
| Lakersfan111 | Dota 2: LGD Gaming vs Team Yandex - Game | Team Yandex (BUY) | 66% | 10.00 | 1.2% | ⏳ pendiente | — |
| 111111111115 | Dota 2: Iron Wing vs GamerLegion - Game  | Iron Wing (BUY) | 74% | 10.00 | 25.7% | ⏳ pendiente | — |
| Lakersfan111 | Dota 2: LGD Gaming vs Team Yandex - Game | Team Yandex (BUY) | 66% | 10.00 | 4.8% | ⏳ pendiente | — |
| Lakersfan111 | Dota 2: LGD Gaming vs Team Yandex (BO3)  | Team Yandex (BUY) | 73% | 10.00 | 0.4% | ⏳ pendiente | — |
| 111111111115 | Counter-Strike: TheMongolz vs paiN - Map | paiN (BUY) | 46% | 10.00 | 0.3% | ⏳ pendiente | — |
| 111111111115 | Dota 2: Team Spirit vs Team Resilience - | Team Spirit (BUY) | 72% | 10.00 | 3.3% | ⏳ pendiente | — |
| Lakersfan111 | Game Handicap: TY (-1.5) vs LGD Gaming ( | Team Yandex (BUY) | 44% | 10.00 | 0.4% | ⏳ pendiente | — |
| RN1 | Yellow-Red KV Mechelen vs. Standard Lieg | Over (BUY) | 47% | 10.00 | 3.3% | ⏳ pendiente | — |
| RN1 | Atlas FC vs. Tigres de la UANL: O/U 3.5 | Over (BUY) | 36% | 10.00 | 1.7% | ❌ perdida | -10.00 |
| RN1 | Will Tigres de la UANL win on 2026-08-15 | No (BUY) | 95% | 10.00 | 0.9% | ✅ ganada | +0.53 |
| RN1 | Will Tigres de la UANL win on 2026-08-15 | Yes (BUY) | 42% | 10.00 | 1.9% | ❌ perdida | -10.00 |
| 111111111115 | Dota 2: Aurora vs BoomBoys - Game 2 Winn | BoomBoys (BUY) | 51% | 10.00 | 276.3% | ⏳ pendiente | — |
| wr0ngw4yb3tt0r | Arsenal FC vs. Manchester City: O/U 2.5 | Under (BUY) | 49% | 10.00 | 53.4% | ⏳ pendiente | — |
| HomeRunHazard | Portland Fire vs. Phoenix Mercury: O/U 1 | Under (BUY) | 50% | 10.00 | 0.6% | ⏳ pendiente | — |
| Lakersfan111 | Dota 2: Iron Wing vs GamerLegion - Game  | GamerLegion (BUY) | 25% | 10.00 | 2.0% | ⏳ pendiente | — |
| HomeRunHazard | Cincinnati Open: Alexander Zverev vs Cam | Cameron Norrie (BUY) | 40% | 10.00 | 3.7% | ❌ perdida | -10.00 |
| RN1 | Atlas FC vs. Tigres de la UANL: O/U 2.5 | Over (BUY) | 75% | 10.00 | 1.7% | ✅ ganada | +3.33 |
| 111111111115 | Counter-Strike: MOUZ vs PARIVISION (BO3) | PARIVISION (BUY) | 35% | 10.00 | 10.3% | ⏳ pendiente | — |
| Lakersfan111 | Dota 2: Team Spirit vs Team Resilience ( | Team Spirit (BUY) | 77% | 10.00 | 2.4% | ⏳ pendiente | — |
| Lakersfan111 | Counter-Strike: Astralis vs NIP - Map 1  | Astralis (BUY) | 47% | 10.00 | 6.4% | ⏳ pendiente | — |
| 111111111115 | Counter-Strike: Astralis vs NIP - Map 1  | NIP (BUY) | 53% | 10.00 | 35.3% | ⏳ pendiente | — |
| wr0ngw4yb3tt0r | UFC 330: Islam Makhachev vs. Ian Machado | Islam Makhachev (BUY) | 69% | 10.00 | 1.8% | ✅ ganada | +4.49 |
| Lakersfan111 | Map Handicap: VIT (-1.5) vs Lynn Vision  | Lynn Vision (BUY) | 29% | 10.00 | 4.3% | ⏳ pendiente | — |
| RN1 | Texas Rangers vs. Athletics | Texas Rangers (BUY) | 89% | 10.00 | 4.0% | ✅ ganada | +1.24 |
| RN1 | Cincinnati Open: Alexander Zverev vs Cam | Cameron Norrie (BUY) | 36% | 10.00 | 10.4% | ❌ perdida | -10.00 |
| HomeRunHazard | Cincinnati Open: Alexander Zverev vs Cam | Alexander Zverev (BUY) | 62% | 10.00 | 0.5% | ✅ ganada | +6.13 |
