#!/usr/bin/env python3
"""Expedition „Saftbar“ (Klasse 8): Verhältnisgleichung · Bruchgleichung · Gleichungssystem (Mischung) · Preis pro Liter mit Entscheidung.
Aufruf: python3 -I inhalte/generatoren/expedition_saftbar.py → inhalte/expeditionen/8-saftbar.json"""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _exp8 import B, PI, zt, zahl, luecken, auswahl, schreibe  # noqa: E402,F401

saft = Fr(750) * 2 / 5
assert saft == 300
x = 2 / Fr(1, 4) - 2
assert x == 6 and Fr(2) / (2 + x) == Fr(1, 4)
# Mischung: a Liter 40-%-Saft, b Liter 100-%-Saft: a + b = 10, 0,4a + b = 7
a = Fr(10 - 7) / (1 - Fr(4, 10)); b = 10 - a
assert (a, b) == (5, 5) and Fr(4, 10) * a + b == 7
kosten = a * Fr('1.20') + b * Fr('2.40')
assert kosten == 18 and kosten / 10 == Fr('1.8') < Fr('1.95')

V, E, S, P = B('gleichungen.bruch', 'verhaeltnis'), B('gleichungen.bruch', 'ein_bruch'), B('gleichungen.lgs2', 'sachaufgabe'), B('groessen.proportional', 'sach')
schreibe({
    'schluessel': '8-saftbar', 'titel': 'Saftbar',
    'einleitung': 'Für das Sportfest betreibt eure Klasse eine Saftbar. Ihr mischt Schorlen und Fruchtgetränke selbst. '
                  'Auf den Packungen steht der Fruchtgehalt in Prozent: 100-%-Saft ist reiner Saft, ein 40-%-Fruchtsaftgetränk enthält 40 % Saft und 60 % Wasser.',
    'voraussetzungen': [V, E, S, P],
    'teile': [
        zahl('a', 'Eine Apfelschorle wird aus Saft und Wasser im Verhältnis 2 : 3 gemischt. Wie viele Milliliter Saft sind in einem 750-ml-Krug Schorle?', saft, '750 * 2 / 5',
             'Gegeben: Saft : Wasser = 2 : 3, zusammen 750 ml. Gesucht: Saftmenge. Ansatz: 2 von 5 Teilen sind Saft: s : 750 = 2 : 5. Rechnung: 750 : 5 · 2 = 300. '
             'Antwort: Im Krug sind 300 ml Saft (und 450 ml Wasser).',
             'Wie viele Teile hat die Mischung insgesamt?', V, einheit='ml'),
        zahl('b', 'In einen Kanister kommen 2 Liter Saft und x Liter Wasser. Der Saftanteil ist dann 2/(2 + x). Er soll genau 25 % betragen. Wie viele Liter Wasser muss man dazugeben?',
             x, '2 / 0.25 - 2',
             'Gegeben: 2/(2 + x) = 0,25, x ≥ 0. Gesucht: x. Ansatz: Mit (2 + x) multiplizieren. Rechnung: 2 = 0,25 · (2 + x) ⇒ 8 = 2 + x ⇒ x = 6. Probe: 2/8 = 0,25 ✓. '
             'Antwort: Man gibt 6 Liter Wasser dazu.',
             'Multipliziere beide Seiten mit dem Nenner.', E, einheit='l'),
        luecken('c', 'Ihr wollt 10 Liter eines Getränks mit 70 % Fruchtgehalt mischen – aus einem 40-%-Fruchtsaftgetränk und aus 100-%-Saft. Wie viele Liter nehmt ihr von jeder Sorte?',
                '□ l vom 40-%-Getränk und □ l vom 100-%-Saft', 'Je Lücke eine ganze Zahl.', [a, b], ['(10 - 7) / 0.6', '10 - 5'],
                'Gegeben: zusammen 10 l, darin 70 % von 10 l = 7 l reiner Saft. Gesucht: a (40 %) und b (100 %). Ansatz: a + b = 10 und 0,4a + 1 · b = 7. '
                'Rechnung: Subtrahieren: (a + b) − (0,4a + b) = 10 − 7 ⇒ 0,6a = 3 ⇒ a = 5, b = 5. Probe: 2 + 5 = 7 ✓. Antwort: Je 5 Liter von beiden Sorten.',
                'Eine Gleichung zählt die Liter, die andere den reinen Saft darin.', S),
        auswahl('d', 'Das 40-%-Getränk kostet 1,20 € pro Liter, der 100-%-Saft 2,40 € pro Liter. Für 10 Liter eures 70-%-Getränks braucht ihr je 5 Liter von beiden. '
                     'Im Großmarkt gibt es fertigen 70-%-Nektar für 1,95 € pro Liter. Was ist für 10 Liter günstiger?',
                'Selbst mischen: 18 € für 10 Liter, also 1,80 € pro Liter.',
                ['Der fertige Nektar, weil 1,95 € weniger als 2,40 € ist.', 'Beides kostet gleich viel, weil der Fruchtgehalt gleich ist.', 'Selbst mischen: 12 € für 10 Liter.'],
                'Gegeben: 5 l zu 1,20 €/l, 5 l zu 2,40 €/l, fertig 1,95 €/l. Gesucht: günstigere Lösung. Ansatz: Preis ist proportional zur Menge – jede Sorte einzeln rechnen. '
                'Rechnung: 5 · 1,20 + 5 · 2,40 = 6 + 12 = 18 €; fertig: 10 · 1,95 = 19,50 €. Antwort: Selbst mischen ist um 1,50 € günstiger.',
                'Rechne beide Sorten einzeln: Menge mal Literpreis.', P),
    ],
})
