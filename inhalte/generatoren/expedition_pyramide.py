#!/usr/bin/env python3
"""Expedition „Die Stufenpyramide“ (Klasse 5) – Quadratzahlen, geschickt addieren, runden, Zehnerpotenzen, schriftlich rechnen.
Aufruf: python3 -I inhalte/generatoren/expedition_pyramide.py → inhalte/expeditionen/5-pyramide.json"""
import sys
from fractions import Fraction as Fr
from math import lcm
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _expedition_kl5 import B, auswahl, expedition, luecken, roemisch_wert, schreibe, zahl, zahlwort, zt  # noqa: E402,F401

SCHICHTEN = [i * i for i in range(1, 6)]
UNTEN = 17
STEINE = 2347819
gerundet = round(STEINE, -5)
assert gerundet == 2300000 and gerundet % 100000 == 0
exp = 5
assert 23 * 10 ** exp == gerundet
PRO_TAG, JAHR, JAHRE = 300, 365, 20
geschafft = PRO_TAG * JAHR * JAHRE
fehlt = gerundet - geschafft
assert fehlt == 110000
antworten = [f'Ja, es bleiben {zt(fehlt)} Steine übrig.', f'Nein, es fehlen {zt(fehlt)} Steine.', 'Ja, es passt genau.', f'Nein, es fehlen {zt(fehlt * 10)} Steine.']

tabelle = {'typ': 'tabelle', 'kopf': ['Schicht von oben', '1', '2', '3', '4', '5'], 'zeilen': [['Würfel'] + [str(s) for s in SCHICHTEN]]}

teile = [
    zahl('a', f'Neben deinem kleinen Modell steht im Museum ein großes Modell aus denselben Holzwürfeln. Es hat unten eine Schicht aus {UNTEN} · {UNTEN} Würfeln. Wie viele Würfel sind das ({UNTEN}²)?',
         UNTEN ** 2, f'{UNTEN} * {UNTEN}', f'{UNTEN}² = {UNTEN} · {UNTEN} = {UNTEN ** 2} Würfel.',
         f'Rechne {UNTEN} · 10 + {UNTEN} · 7.', B('zahlen.potenzen_basis', 'quadrat'), grafik=tabelle),
    zahl('b', f'Die kleine Pyramide hat 5 Schichten mit {", ".join(map(str, SCHICHTEN[:-1]))} und {SCHICHTEN[-1]} Würfeln. Wie viele Würfel sind es zusammen? Rechne geschickt.',
         sum(SCHICHTEN), ' + '.join(map(str, SCHICHTEN)),
         f'Geschickt zusammenfassen: (1 + 9) + (4 + 16) + 25 = 10 + 20 + 25 = {sum(SCHICHTEN)}.',
         'Suche zwei Zahlen, die zusammen eine glatte Zehnerzahl ergeben.', B('zahlen.rechengesetze', 'vorteil')),
    zahl('c', f'Die echten Pyramiden sind nicht aus Holzwürfeln, sondern aus riesigen Steinblöcken gebaut – und haben viel mehr Schichten als jedes Modell. '
              f'Eine erfundene Riesenpyramide hätte {zt(STEINE)} Steine. Runde diese Zahl auf Hunderttausender.',
         gerundet, f'{gerundet}', f'An der Hunderttausenderstelle steht 3, rechts daneben die Zehntausenderziffer 4: abrunden. {zt(STEINE)} ≈ {zt(gerundet)}.',
         'Welche Ziffer steht rechts neben der Hunderttausenderstelle?', B('zahlen.natuerlich', 'runden_regel')),
    zahl('d', f'Es gilt {zt(gerundet)} = 23 · 10 hoch ?. Welcher Exponent gehört an die Stelle des Fragezeichens?',
         exp, f'{exp}', f'Hinter der 23 stehen {exp} Nullen: {zt(gerundet)} = 23 · {zt(10 ** exp)} = 23 · 10⁵.',
         'Zähle die Nullen hinter der 23.', B('zahlen.potenzen_basis', 'zehner')),
    auswahl('e', f'Ein Bautrupp setzt jeden Tag {PRO_TAG} Steine, ein Jahr hat {JAHR} Tage. Reichen {JAHRE} Jahre für {zt(gerundet)} Steine?',
            antworten[1], [a for a in antworten if a != antworten[1]],
            f'{PRO_TAG} · {JAHR} = {zt(PRO_TAG * JAHR)} Steine im Jahr. · {JAHRE} = {zt(geschafft)} Steine. '
            f'Das ist weniger als {zt(gerundet)}: Es fehlen {zt(gerundet)} − {zt(geschafft)} = {zt(fehlt)} Steine. Die Zeit reicht nicht.',
            'Rechne zuerst aus, wie viele Steine in einem Jahr gesetzt werden.', B('zahlen.rechengesetze', 'schriftlich'), ordnung=antworten),
]

schreibe(expedition('pyramide', 'Die Stufenpyramide',
                    'In einem Museum in Kairo baust du mit Holzwürfeln eine Stufenpyramide nach. Jede Schicht ist ein Quadrat aus Würfeln: '
                    'oben 1 Würfel, darunter 2 · 2, dann 3 · 3 und so weiter. Die Tabelle zeigt die kleine Pyramide.', teile))
