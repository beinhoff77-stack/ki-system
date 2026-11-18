#!/usr/bin/env python3
"""Expedition „Der Uhrturm“ (Klasse 5) – Winkel an der Uhr, Zeitspannen, Vielfache.
Aufruf: python3 -I inhalte/generatoren/expedition_uhrturm.py → inhalte/expeditionen/5-uhrturm.json"""
import sys
from fractions import Fraction as Fr
from math import lcm
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _expedition_kl5 import B, auswahl, expedition, luecken, roemisch_wert, schreibe, zahl, zahlwort, zt  # noqa: E402,F401


def zeigerwinkel(h, m):
    """Kleinerer Winkel zwischen den Zeigern (Grad, exakt)."""
    d = abs(Fr(30) * (h % 12) + Fr(m, 2) - 6 * m)
    return min(d, 360 - d)


w4 = zeigerwinkel(4, 0)
NACH, STUNDE = 3, 60
tage = STUNDE // NACH
GLOCKE, LAMPE = 15, 6
gemeinsam = lcm(GLOCKE, LAMPE)
zeiten = {'3:00 Uhr': (3, 0), '3:30 Uhr': (3, 30), '9:30 Uhr': (9, 30), '6:15 Uhr': (6, 15)}
recht = [z for z, (h, m) in zeiten.items() if zeigerwinkel(h, m) == 90]
assert recht == ['3:00 Uhr'] and w4 == 120 and gemeinsam == 30

teile = [
    zahl('a', 'Wie groß ist der kleinere Winkel zwischen Stunden- und Minutenzeiger um 4:00 Uhr?', w4, '4 * 30',
         'Zwischen zwei benachbarten Zahlen auf dem Zifferblatt liegen 360° : 12 = 30°. Um 4:00 Uhr liegen 4 solche Abstände zwischen den Zeigern: 4 · 30° = 120°.',
         'Wie viel Grad liegen zwischen zwei benachbarten Zahlen?', B('geometrie.winkel', 'uhr'), einheit='°'),
    zahl('b', f'Die Turmuhr geht jeden Tag {NACH} Minuten nach. Nach wie vielen Tagen zeigt sie genau eine Stunde zu wenig an?',
         tage, f'{STUNDE} // {NACH}', f'Eine Stunde sind {STUNDE} Minuten. Jeden Tag kommen {NACH} Minuten dazu: {STUNDE} : {NACH} = {tage} Tage.',
         'Rechne eine Stunde in Minuten um.', B('groessen.einheiten', 'zeit')),
    luecken('c', f'Die Glocke schlägt alle {GLOCKE} Minuten, eine Lampe auf dem Turm blinkt alle {LAMPE} Minuten. Um 12:00 Uhr passiert beides gleichzeitig. '
                 'Um wie viel Uhr passiert es zum nächsten Mal gleichzeitig?',
            '□:□ Uhr', [12, gemeinsam], ['12', f'{gemeinsam}'], 'Stunden und Minuten je als ganze Zahl.',
            f'Glocke: 15, 30, 45 … Minuten nach 12 Uhr. Lampe: 6, 12, 18, 24, 30 … Minuten. Die erste gemeinsame Zahl ist {gemeinsam}: um 12:{gemeinsam} Uhr.',
            'Schreib für beide auf, wie viele Minuten nach 12 Uhr sie dran sind.', B('zahlen.teilbarkeit', 'vielfache')),
    auswahl('d', 'Für ein Foto sollen die beiden Zeiger genau einen rechten Winkel bilden. Welche Uhrzeit passt?',
            recht[0], [z for z in zeiten if z not in recht],
            'Um 3:00 Uhr: 3 Abstände · 30° = 90°. Um halb steht der Stundenzeiger schon in der Mitte zwischen zwei Zahlen (15° weiter): '
            '3:30 Uhr ergibt 75°, 9:30 Uhr 105°. Um 6:15 Uhr steht der Stundenzeiger ein Viertel hinter der 6 (7,5°), es sind 97,5°.',
            'Der Stundenzeiger bewegt sich auch zwischen den vollen Stunden weiter.', B('geometrie.winkel', 'uhr'), ordnung=list(zeiten)),
]

schreibe(expedition('uhrturm', 'Der Uhrturm',
                    'In Timbuktu steigst du auf einen alten Turm mit einer großen Uhr, einer Glocke und einer Lampe. '
                    'Die Uhr hat einen Stundenzeiger und einen Minutenzeiger.', teile))
