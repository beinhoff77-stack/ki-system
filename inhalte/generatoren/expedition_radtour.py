#!/usr/bin/env python3
"""Expedition „Radtour“ (Klasse 8): Maßstab · indirekte Proportionalität · Steigung aus zwei Punkten · Ungleichung mit Zeit.
Aufruf: python3 -I inhalte/generatoren/expedition_radtour.py → inhalte/expeditionen/8-radtour.json"""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _exp8 import B, PI, zt, zahl, luecken, auswahl, schreibe  # noqa: E402,F401

KARTE_CM, MASSSTAB = 36, 100000
STRECKE = Fr(KARTE_CM * MASSSTAB, 100000)          # in km
assert STRECKE == 36
assert 36 / Fr(18) == 2 and 36 / Fr(12) == 3       # Zeit bei 18 bzw. 12 km/h
v = Fr(36 - 6, 2)
assert v == 15
fahrt_min = STRECKE / v * 60
assert fahrt_min == 144 and 9 * 60 + fahrt_min + 45 == 12 * 60 + 9 and 180 - fahrt_min == 36

M, I, Z, U = B('groessen.einheiten', 'massstab'), B('groessen.indirekt', 'sach'), B('funktionen.linear', 'zwei_punkte'), B('gleichungen.ungleichungen', 'sachaufgabe')
graf = {'typ': 'koordinaten', 'x': [0, 3], 'y': [0, 50], 'schritt_x': 0.5, 'schritt_y': 10, 'name_x': 'Stunden', 'name_y': 'km',
        'graphen': [{'art': 'linear', 'm': 15, 't': 6, 'bereich': [0, 2.4]}], 'punkte': [{'x': 0, 'y': 6, 'name': 'P'}, {'x': 2, 'y': 36, 'name': 'Q'}, {'x': 2.4, 'y': 42, 'name': 'See'}]}
schreibe({
    'schluessel': '8-radtour', 'titel': 'Radtour zum See',
    'einleitung': 'Eine Gruppe fährt mit dem Fahrrad vom Ort zum Badesee. Die Route ist auf einer Radkarte eingezeichnet. '
                  'Am See soll Pause gemacht werden, und zurück geht es mit dem Zug, der um 12:00 Uhr am See abfährt.',
    'voraussetzungen': [M, I, Z, U],
    'teile': [
        zahl('a', 'Auf der Radkarte im Maßstab 1 : 100 000 ist die Route 36 cm lang. Wie viele Kilometer sind das in Wirklichkeit?', STRECKE, '36 * 100000 / 100000',
             'Gegeben: 36 cm auf der Karte, Maßstab 1 : 100 000. Gesucht: wirkliche Länge. Ansatz: 1 cm auf der Karte sind 100 000 cm = 1 km. '
             'Rechnung: 36 · 100 000 cm = 3 600 000 cm = 36 km. Antwort: Die Route ist 36 km lang.',
             'Wie viele Kilometer sind 100 000 cm?', M, einheit='km'),
        zahl('b', 'Für die 36 km braucht die Gruppe mit 18 km/h genau 2 Stunden. Wie viele Stunden braucht sie, wenn sie nur 12 km/h schafft?', 3, '18 * 2 / 12',
             'Gegeben: 18 km/h → 2 h, die Strecke bleibt gleich. Gesucht: Zeit bei 12 km/h. Ansatz: Geschwindigkeit · Zeit = 36 km bleibt gleich (indirekt proportional). '
             'Rechnung: 36 : 12 = 3. Antwort: Sie braucht 3 Stunden.',
             'Langsamer heißt länger – was bleibt gleich?', I, einheit='h'),
        zahl('c', 'Die Route führt an einer Straße mit Kilometersteinen entlang. Sie beginnt am Kilometerstein 6; der See liegt am Kilometerstein 42 (6 km + 36 km Route). '
                  'Der Graph zeigt die Fahrt: Beim Start (0 Stunden) ist die Gruppe am Kilometerstein 6, nach 2 Stunden kommt sie am Kilometerstein 36 vorbei – '
                  'das ist ein Zwischenpunkt, noch nicht der See. Sie fährt gleichmäßig. '
                  'Wie viele Kilometer schafft sie in einer Stunde?', v, '(36 - 6) / 2',
             'Gegeben: P(0 | 6), Q(2 | 36). Gesucht: Steigung m (km pro Stunde). Ansatz: m = Unterschied der km : Unterschied der Stunden. '
             'Rechnung: (36 − 6) : (2 − 0) = 30 : 2 = 15. Die 30 km sind die ersten 30 der 36 km Route; bis zum See (Kilometerstein 42) fehlen noch 6 km. '
             'Antwort: Sie fährt 15 km in einer Stunde.',
             'Lies die beiden Punkte ab: Wie viele km kommen in 2 Stunden dazu?', Z, einheit='km', grafik=graf),
        auswahl('d', 'Die Gruppe startet um 9:00 Uhr am Kilometerstein 6 und fährt die ganze Route von 36 km bis zum See am Kilometerstein 42 mit 15 km/h. Am See will sie 45 Minuten Pause machen, bevor sie zum Zug geht, der um 12:00 Uhr abfährt. '
                     'Schafft sie den Zug?',
                'Nein: Sie wäre erst um 12:09 Uhr fertig; die Pause dürfte höchstens 36 Minuten dauern.',
                ['Ja, sie ist kurz vor 12 Uhr fertig.', 'Ja, weil 2 Stunden Fahrt und 45 Minuten Pause weniger als 3 Stunden sind.', 'Das kann man ohne die Länge der Pause nicht sagen.'],
                'Gegeben: 36 km mit 15 km/h, Start 9:00 Uhr, 45 min Pause, Zug 12:00 Uhr. Gesucht: Reicht die Zeit? Ansatz: Fahrzeit + Pause ≤ 180 Minuten. '
                'Rechnung: 36 : 15 = 2,4 h = 144 min. 144 + 45 = 189 min > 180 min, also 12:09 Uhr. Für die Pause p gilt 144 + p ≤ 180 ⇒ p ≤ 36. '
                'Antwort: Mit 45 Minuten Pause verpasst die Gruppe den Zug.',
                'Rechne die Fahrzeit in Minuten um. 2,4 Stunden sind nicht 2 Stunden 40 Minuten.', U),
    ],
})
