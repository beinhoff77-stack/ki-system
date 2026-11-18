#!/usr/bin/env python3
"""Expedition „Sparen für den Roller“ (Klasse 8): Wertetabelle · Schnittpunkt · Rabatt · Ungleichung mit Entscheidung.
Aufruf: python3 -I inhalte/generatoren/expedition_roller.py → inhalte/expeditionen/8-roller.json"""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _exp8 import B, PI, zt, zahl, luecken, auswahl, schreibe  # noqa: E402,F401

DU = lambda x: 60 + 15 * x          # du: 60 € gespart, jede Woche 15 € dazu
BR = lambda x: 150 + 6 * x          # dein Bruder: 150 € gespart, jede Woche 6 € dazu
PREIS, RABATT = Fr(299), Fr(20, 100)
neu = PREIS * (1 - RABATT)
assert neu == Fr('239.2')
x_gleich = Fr(150 - 60, 15 - 6)
assert x_gleich == 10 and DU(10) == BR(10) == 210
w_du = min(x for x in range(60) if DU(x) >= neu)
w_br = min(x for x in range(60) if BR(x) >= neu)
assert (w_du, w_br) == (12, 15)

W, S, R, U = B('funktionen.grundbegriffe', 'wertetabelle'), B('funktionen.linear', 'schnittpunkte'), B('bruch.prozent', 'rabatt_aufschlag'), B('gleichungen.ungleichungen', 'sachaufgabe')
tab = {'typ': 'tabelle', 'kopf': ['Wochen x', '0', '2', '4', '6'], 'zeilen': [['Guthaben in €', '60', '?', '?', '?']]}
schreibe({
    'schluessel': '8-roller', 'titel': 'Sparen für den Roller',
    'einleitung': 'Du und dein Bruder wollt euch jeweils einen Tretroller kaufen. Du hast schon 60 € gespart und legst jede Woche 15 € von deinem Ferienjob dazu. '
                  'Dein Bruder hat 150 € gespart und legt jede Woche 6 € Taschengeld dazu. Der Roller kostet im Laden 299 €.',
    'voraussetzungen': [W, S, R, U],
    'teile': [
        luecken('a', 'Du hast 60 € gespart und legst jede Woche 15 € dazu. Ergänze die Wertetabelle: Wie viel Geld hast du nach 2, nach 4 und nach 6 Wochen?',
                'nach 2 Wochen □ € · nach 4 Wochen □ € · nach 6 Wochen □ €', 'Je Lücke eine ganze Zahl.', [DU(2), DU(4), DU(6)], ['60 + 15 * 2', '60 + 15 * 4', '60 + 15 * 6'],
                'Gegeben: Start 60 €, jede Woche 15 € mehr. Gesucht: Werte nach 2, 4, 6 Wochen. Ansatz: f(x) = 60 + 15x. Rechnung: 60 + 30 = 90; 60 + 60 = 120; 60 + 90 = 150. '
                'Antwort: 90 €, 120 €, 150 €.',
                'In 2 Wochen kommen 2 · 15 € dazu.', W, grafik=tab),
        luecken('b', 'Dein Guthaben nach x Wochen ist 60 + 15x Euro, das deines Bruders 150 + 6x Euro. Nach wie vielen Wochen habt ihr gleich viel Geld, und wie viel ist das?',
                'nach □ Wochen, je □ €', 'Je Lücke eine ganze Zahl.', [x_gleich, DU(x_gleich)], ['(150 - 60) / (15 - 6)', '60 + 15 * 10'],
                'Gegeben: 60 + 15x und 150 + 6x. Gesucht: Schnittpunkt. Ansatz: Gleichsetzen. Rechnung: 60 + 15x = 150 + 6x ⇒ 9x = 90 ⇒ x = 10; 60 + 150 = 210. '
                'Antwort: Nach 10 Wochen habt ihr beide 210 €.',
                'Setze die beiden Terme gleich.', S),
        zahl('c', 'Der Roller kostet 299 €. Im Sommerschlussverkauf gibt es 20 % Rabatt. Wie viel kostet der Roller dann?', neu, '299 * 0.8',
             'Gegeben: 299 €, 20 % Rabatt. Gesucht: neuer Preis. Ansatz: Es bleiben 80 % des Preises. Rechnung: 299 · 0,8 = 239,20. Antwort: Der Roller kostet 239,20 €.',
             'Wie viel Prozent des Preises musst du noch zahlen?', R, einheit='€'),
        auswahl('d', 'Der Roller kostet im Schlussverkauf 239,20 €. Du hast nach x Wochen 60 + 15x Euro, dein Bruder 150 + 6x Euro. Wer kann sich den Roller zuerst leisten, und wann?',
                'Du nach 12 Wochen, dein Bruder erst nach 15 Wochen.',
                ['Dein Bruder zuerst, weil er am Anfang mehr Geld hat.', 'Beide nach 10 Wochen, weil ihr dann gleich viel habt.', 'Du nach 15 Wochen, dein Bruder nach 12 Wochen.'],
                'Gegeben: Preis 239,20 €; 60 + 15x und 150 + 6x. Gesucht: kleinste ganze Wochenzahl für jeden. Ansatz: 60 + 15x ≥ 239,2 und 150 + 6x ≥ 239,2. '
                'Rechnung: 15x ≥ 179,2 ⇒ x ≥ 11,9…, also 12 Wochen (dann 240 €). 6x ≥ 89,2 ⇒ x ≥ 14,8…, also 15 Wochen (dann 240 €). '
                'Nach 10 Wochen habt ihr zwar gleich viel, aber erst 210 €. Antwort: Du kannst den Roller nach 12 Wochen kaufen, dein Bruder nach 15 Wochen.'
                .replace('11,9…', '179,2 : 15 ≈ 11,95').replace('14,8…', '89,2 : 6 ≈ 14,87'),
                'Stelle für jeden eine Ungleichung mit „mindestens 239,20 €“ auf. Es zählen nur volle Wochen.', U),
    ],
})
