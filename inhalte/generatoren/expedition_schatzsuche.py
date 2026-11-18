#!/usr/bin/env python3
"""Expedition „Die Schatzsuche“ (Klasse 5) – Koordinaten, Drehungen, Reihenfolgen zählen, Neunerregel, Zeit.
Aufruf: python3 -I inhalte/generatoren/expedition_schatzsuche.py → inhalte/expeditionen/5-schatzsuche.json"""
import sys
from fractions import Fraction as Fr
from math import lcm
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _expedition_kl5 import B, auswahl, expedition, luecken, roemisch_wert, schreibe, zahl, zahlwort, zt  # noqa: E402,F401
from itertools import permutations  # noqa: E402

START, RECHTS, OBEN = (-4, -2), 6, 5
ziel = (START[0] + RECHTS, START[1] + OBEN)
RICHT = ['Norden', 'Osten', 'Süden', 'Westen']
DREH = 270
blick = RICHT[(RICHT.index('Norden') + DREH // 90) % 4]
ZIFFERN = [1, 2, 3, 4, 5]
codes = [int(''.join(map(str, p))) for p in permutations(ZIFFERN, 3)]
neun = [c for c in codes if c % 9 == 0]
SEK, WARTEN_MIN = 20, 5
dauer = Fr(len(neun) * SEK, 60)
assert len(codes) == 60 and len(neun) == 12 and dauer == 4 and blick == 'Westen'
antworten = [f'Ja, es dauert höchstens {zt(dauer)} Minuten.', 'Nein, es dauert 240 Minuten.', 'Nein, es dauert 6 Minuten.', 'Ja, es dauert genau 5 Minuten.']

karte = {'typ': 'koordinaten', 'x': [-5, 4], 'y': [-3, 4], 'schritt_x': 1, 'schritt_y': 1, 'punkte': [{'x': START[0], 'y': START[1], 'name': 'S'}]}

teile = [
    luecken('a', f'Du startest bei S {"(" + zt(START[0]) + " | " + zt(START[1]) + ")"}, gehst {RECHTS} Kästchen nach rechts und dann {OBEN} Kästchen nach oben. '
                 'An welchem Punkt stehst du jetzt?',
            '(□ | □)', list(ziel), [f'{START[0]} + {RECHTS}', f'{START[1]} + {OBEN}'], 'Erst die x-Koordinate, dann die y-Koordinate; negative Zahlen mit Minus.',
            f'Nach rechts ändert sich x: {zt(START[0])} + {RECHTS} = {ziel[0]}. Nach oben ändert sich y: {zt(START[1])} + {OBEN} = {ziel[1]}. Du stehst bei ({ziel[0]} | {ziel[1]}).',
            'Rechts und links ändern nur x, oben und unten nur y.', B('geometrie.grundbegriffe', 'koordinaten'), grafik=karte),
    auswahl('b', f'Dort schaust du nach Norden und drehst dich um {DREH}° im Uhrzeigersinn. In welche Himmelsrichtung schaust du jetzt?',
            blick, [r for r in RICHT if r != blick],
            f'{DREH}° sind drei Vierteldrehungen (3 · 90°). Im Uhrzeigersinn: Norden → Osten → Süden → Westen.',
            'Wie viele Vierteldrehungen sind 270°?', B('geometrie.winkel', 'drehungen'), ordnung=RICHT),
    zahl('c', 'Die Schatztruhe hat ein Zahlenschloss mit 3 Stellen. Jede Stelle ist eine der Ziffern 1, 2, 3, 4 oder 5, und keine Ziffer kommt doppelt vor. '
              'Wie viele verschiedene Codes gibt es?',
         len(codes), '5 * 4 * 3', f'Erste Stelle: 5 Ziffern, zweite: noch 4, dritte: noch 3. 5 · 4 · 3 = {len(codes)} Codes.',
         'Wie viele Ziffern bleiben für die zweite und die dritte Stelle?', B('stochastik.kombinatorik', 'reihenfolgen')),
    zahl('d', 'Auf einem Zettel steht: „Der Code ist durch 9 teilbar.“ Wie viele dreistellige Codes aus drei verschiedenen Ziffern von 1 bis 5 sind durch 9 teilbar?',
         len(neun), '2 * 6',
         'Durch 9 teilbar heißt: Die Quersumme ist durch 9 teilbar. Drei verschiedene Ziffern von 1 bis 5 ergeben höchstens 5 + 4 + 3 = 12, also muss die Quersumme 9 sein. '
         'Das geht nur mit 1, 3, 5 oder mit 2, 3, 4. Jede dieser Gruppen kann man auf 3 · 2 · 1 = 6 Arten anordnen: 2 · 6 = 12 Codes '
         f'(z. B. 135, 153, …, 234, 243, …).',
         'Welche Quersumme kann ein solcher Code höchstens haben?', B('zahlen.teilbarkeit', 'neunerregel')),
    auswahl('e', f'Es kommen {len(neun)} Codes in Frage. Jedes Ausprobieren dauert {SEK} Sekunden. Der Wächter kommt in {WARTEN_MIN} Minuten zurück. '
                 'Schaffst du sicher alle Versuche, bevor er da ist?',
            antworten[0], antworten[1:],
            f'{len(neun)} · {SEK} s = {len(neun) * SEK} s. 60 s sind 1 Minute: {len(neun) * SEK} s = {zt(dauer)} min. Das ist weniger als {WARTEN_MIN} Minuten – '
            'auch wenn der richtige Code der letzte ist.',
            'Rechne alle Sekunden zusammen und dann in Minuten um.', B('groessen.einheiten', 'zeit'), ordnung=antworten),
]

schreibe(expedition('schatzsuche', 'Die Schatzsuche',
                    'Auf einer Insel findest du eine Schatzkarte mit Koordinatensystem; ein Kästchen ist ein Schritt. '
                    'Die Truhe ist mit einem Zahlenschloss gesichert, und ein Wächter macht gerade eine Runde.', teile))
