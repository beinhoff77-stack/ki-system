#!/usr/bin/env python3
"""Expedition „Kerzenwerkstatt“ (Klasse 8): Quadervolumen · Funktionswert · Ungleichung · Schnittpunkt zweier Geraden.
Aufruf: python3 -I inhalte/generatoren/expedition_kerzen.py → inhalte/expeditionen/8-kerzen.json"""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _exp8 import B, PI, zt, zahl, luecken, auswahl, schreibe  # noqa: E402,F401

A0, A_RATE = Fr(24), Fr(3, 2)    # Kerze A: 24 cm hoch, brennt 1,5 cm pro Stunde
B0, B_RATE = Fr(18), Fr(1)       # Kerze B: 18 cm hoch, brennt 1 cm pro Stunde
hA = lambda t: A0 - A_RATE * t
hB = lambda t: B0 - B_RATE * t

vol = 5 * 5 * A0
assert vol == 600 and hA(6) == 15
t_max = max(t for t in range(0, 30) if hA(t) >= 3)
assert t_max == 14 and hA(14) == 3 and hA(15) < 3
t_gleich = (A0 - B0) / (A_RATE - B_RATE)
assert t_gleich == 12 and hA(12) == hB(12) == 6 and hA(6) != hB(6) and A0 / A_RATE == 16

V, F, U, S = B('messen.volumen', 'quader'), B('funktionen.grundbegriffe', 'funktionswert'), B('gleichungen.ungleichungen', 'sachaufgabe'), B('funktionen.linear', 'schnittpunkte')
graf = {'typ': 'koordinaten', 'x': [0, 18], 'y': [0, 26], 'schritt_x': 2, 'schritt_y': 4, 'name_x': 'Stunden', 'name_y': 'cm',
        'graphen': [{'art': 'linear', 'm': -1.5, 't': 24, 'name': 'A', 'bereich': [0, 16]}, {'art': 'linear', 'm': -1, 't': 18, 'name': 'B', 'bereich': [0, 18]}]}
schreibe({
    'schluessel': '8-kerzen', 'titel': 'Kerzenwerkstatt',
    'einleitung': 'Für den Weihnachtsbasar gießt eure Klasse Kerzen. Kerze A ist ein Quader mit quadratischem Boden (5 cm × 5 cm) und 24 cm hoch; '
                  'sie brennt in jeder Stunde 1,5 cm herunter. Kerze B ist 18 cm hoch und brennt in jeder Stunde 1 cm herunter.',
    'voraussetzungen': [V, F, U, S],
    'teile': [
        zahl('a', 'Kerze A ist ein Quader: Boden 5 cm × 5 cm, Höhe 24 cm. Wie viel cm³ Wachs braucht man für eine solche Kerze?', vol, '5 * 5 * 24',
             'Gegeben: Quader 5 cm · 5 cm · 24 cm. Gesucht: Volumen. Ansatz: V = Länge · Breite · Höhe. Rechnung: 5 · 5 · 24 = 600. Antwort: Man braucht 600 cm³ Wachs.',
             'Volumen eines Quaders: Grundfläche mal Höhe.', V, einheit='cm³'),
        zahl('b', 'Kerze A ist nach t Stunden h(t) = 24 − 1,5 · t Zentimeter hoch. Wie hoch ist sie nach 6 Stunden?', hA(6), '24 - 1.5 * 6',
             'Gegeben: h(t) = 24 − 1,5t. Gesucht: h(6). Ansatz: 6 für t einsetzen. Rechnung: 24 − 9 = 15. Antwort: Nach 6 Stunden ist Kerze A noch 15 cm hoch.',
             'Setze t = 6 ein; Punkt vor Strich.', F, einheit='cm'),
        zahl('c', 'Kerze A ist nach t Stunden 24 − 1,5 · t Zentimeter hoch. Sie soll ausgeblasen werden, solange noch mindestens 3 cm übrig sind, damit man sie später weiter benutzen kann. '
                  'Wie viele volle Stunden darf sie höchstens brennen?', t_max, '(24 - 3) / 1.5',
             'Gegeben: Höhe 24 − 1,5t, mindestens 3 cm. Gesucht: größte Stundenzahl t. Ansatz: 24 − 1,5t ≥ 3. '
             'Rechnung: −1,5t ≥ −21 ⇒ t ≤ 14 (beim Teilen durch −1,5 dreht sich das Zeichen). Probe: Nach 14 h sind genau 3 cm übrig, nach 15 h nur 1,5 cm. Antwort: höchstens 14 Stunden.',
             'Stelle eine Ungleichung mit „mindestens“ auf.', U, einheit='h'),
        auswahl('d', 'Beide Kerzen werden um 18 Uhr angezündet. Kerze A ist nach t Stunden 24 − 1,5 · t cm hoch, Kerze B 18 − t cm. Der Graph zeigt beide. '
                     'Jemand sagt: „Um 6 Uhr morgens sind beide Kerzen gleich hoch.“ Was stimmt?',
                'Ja: Nach 12 Stunden sind beide 6 cm hoch.',
                ['Nein: Die Kerzen werden nie gleich hoch.', 'Nein: Gleich hoch sind sie schon um Mitternacht.', 'Ja, aber Kerze A ist dann schon abgebrannt.'],
                'Gegeben: A: 24 − 1,5t, B: 18 − t. Gesucht: Wann gleich hoch? Ansatz: Gleichsetzen (Schnittpunkt der Graphen). '
                'Rechnung: 24 − 1,5t = 18 − t ⇒ 6 = 0,5t ⇒ t = 12; Höhe 18 − 12 = 6 cm. 18 Uhr + 12 Stunden = 6 Uhr. Um Mitternacht (t = 6) ist A 15 cm und B 12 cm hoch; '
                'abgebrannt ist A erst nach 16 Stunden. Antwort: Die Aussage stimmt.',
                'Setze beide Terme gleich und rechne die Uhrzeit aus.', S, grafik=graf),
    ],
})
