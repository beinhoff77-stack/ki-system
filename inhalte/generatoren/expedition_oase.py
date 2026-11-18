#!/usr/bin/env python3
"""Expedition „In der Oase“ (Klasse 5) – Koordinaten, Maßstab, Drehungen, Kreis und zwei Kreise.
Aufruf: python3 -I inhalte/generatoren/expedition_oase.py → inhalte/expeditionen/5-oase.json"""
import sys
from fractions import Fraction as Fr
from math import lcm
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _expedition_kl5 import B, auswahl, expedition, luecken, roemisch_wert, schreibe, zahl, zahlwort, zt  # noqa: E402,F401

ZELT, BRUNNEN, PALME = (-3, 2), (5, 2), (2, -2)
abst_kaestchen = BRUNNEN[0] - ZELT[0]          # beide auf y = 2
MASSSTAB = 10000
abst_m = abst_kaestchen * MASSSTAB // 100        # 1 Kästchen = 1 cm auf der Karte
RICHT = ['Norden', 'Osten', 'Süden', 'Westen']   # im Uhrzeigersinn
blick = RICHT[(RICHT.index('Osten') - 1) % 4]    # 90° gegen den Uhrzeigersinn
R_KAMEL = 3                                       # Kästchen = 300 m
plaetze = {'(5 | −2)': (5, -2), '(3 | 2)': (3, 2), '(9 | 2)': (9, 2), '(5 | 6)': (5, 6)}


def abstand_achsen(p, q):
    assert p[0] == q[0] or p[1] == q[1]
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


erlaubt = [n for n, p in plaetze.items() if abstand_achsen(p, BRUNNEN) <= R_KAMEL]
assert len(erlaubt) == 1
FUNK = 500
beide = FUNK + FUNK - abst_m
assert beide > 0

karte = {'typ': 'koordinaten', 'x': [-5, 7], 'y': [-3, 5], 'schritt_x': 1, 'schritt_y': 1,
         'punkte': [{'x': ZELT[0], 'y': ZELT[1], 'name': 'Z'}, {'x': BRUNNEN[0], 'y': BRUNNEN[1], 'name': 'B'}, {'x': PALME[0], 'y': PALME[1], 'name': 'P'}]}

teile = [
    luecken('a', 'Auf der Karte sind dein Zelt Z, der Brunnen B und eine Palme P eingezeichnet. Welche Koordinaten hat die Palme P?',
            '(□ | □)', list(PALME), [str(PALME[0]), str(PALME[1])], 'Erst die x-Koordinate, dann die y-Koordinate; negative Zahlen mit Minus.',
            f'P liegt {PALME[0]} Kästchen rechts vom Ursprung und {-PALME[1]} Kästchen darunter: P ({PALME[0]} | {zt(PALME[1])}).',
            'Erst nach rechts oder links zählen, dann nach oben oder unten.', B('geometrie.grundbegriffe', 'koordinaten'), grafik=karte),
    zahl('b', f'Zelt Z (−3 | 2) und Brunnen B (5 | 2) liegen auf der Karte {abst_kaestchen} cm auseinander. Die Karte hat den Maßstab 1 : {zt(MASSSTAB)}. '
              'Wie viele Meter sind das in Wirklichkeit?',
         abst_m, f'{abst_kaestchen} * {MASSSTAB} // 100',
         f'1 cm auf der Karte sind {zt(MASSSTAB)} cm = {MASSSTAB // 100} m in Wirklichkeit. {abst_kaestchen} cm sind {abst_kaestchen} · {MASSSTAB // 100} m = {abst_m} m.',
         f'Wie viele Meter sind {zt(MASSSTAB)} cm?', B('groessen.einheiten', 'massstab'), einheit='m'),
    auswahl('c', 'Am Zelt schaust du genau nach Osten zum Brunnen. Du drehst dich um 90° gegen den Uhrzeigersinn. In welche Himmelsrichtung schaust du jetzt?',
            blick, [r for r in RICHT if r != blick],
            'Im Uhrzeigersinn folgen Norden, Osten, Süden, Westen. Gegen den Uhrzeigersinn geht es von Osten eine Vierteldrehung (90°) zurück: nach Norden.',
            'Stell dich hin und dreh dich wirklich: Gegen den Uhrzeigersinn heißt nach links.', B('geometrie.winkel', 'drehungen'), ordnung=RICHT),
    auswahl('d', f'Die Kamele dürfen höchstens 300 m vom Brunnen B (5 | 2) entfernt sein; auf der Karte sind das {R_KAMEL} Kästchen. Welcher Platz ist erlaubt?',
            erlaubt[0], [n for n in plaetze if n not in erlaubt],
            'Alle erlaubten Plätze liegen in der Kreisfläche um B mit dem Radius 3 Kästchen. (3 | 2) ist 2 Kästchen von B entfernt, '
            'die anderen drei Plätze je 4 Kästchen – zu weit.',
            'Zähle für jeden Platz die Kästchen bis B.', B('geometrie.ortslinien', 'kreislinie'), ordnung=list(plaetze)),
    zahl('e', f'Dein Funkgerät am Zelt reicht {FUNK} m weit, das Funkgerät am Brunnen ebenfalls {FUNK} m. Zelt und Brunnen sind {abst_m} m voneinander entfernt. '
              'Auf dem geraden Weg zwischen ihnen: Wie lang ist das Stück, auf dem man beide Funkgeräte empfängt?',
         beide, f'{FUNK} + {FUNK} - {abst_m}',
         f'Gemessen vom Zelt: Das Zelt-Funkgerät reicht von 0 m bis {FUNK} m. Das Brunnen-Funkgerät reicht vom Brunnen {FUNK} m zurück, also ab {abst_m} − {FUNK} = {abst_m - FUNK} m. '
         f'Beide gibt es zwischen {abst_m - FUNK} m und {FUNK} m: {FUNK} − {abst_m - FUNK} = {beide} m.',
         'Zeichne den Weg als Strecke und markiere, wie weit jedes Funkgerät reicht.', B('geometrie.ortslinien', 'zwei_kreise'), einheit='m'),
]

schreibe(expedition('oase', 'In der Oase',
                    'Bei Kairo machst du eine Tour in die Wüste. Auf der Karte ist ein Koordinatensystem eingezeichnet; ein Kästchen ist 1 cm lang. '
                    'Dein Zelt Z steht bei (−3 | 2), der Brunnen B bei (5 | 2).', teile))
