#!/usr/bin/env python3
"""Expedition „Schulfest“ (Klasse 8): Laplace-Wahrscheinlichkeit · Gesetz der großen Zahlen · Gleichungssystem · Ungleichung mit Entscheidung.
Aufruf: python3 -I inhalte/generatoren/expedition_schulfest.py → inhalte/expeditionen/8-schulfest.json"""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _exp8 import B, PI, zt, zahl, luecken, auswahl, schreibe  # noqa: E402,F401

p = Fr(3, 12)
assert p == Fr(1, 4) and 240 * p == 60
e = Fr(260 - 180, 2 - 1); k = 180 - e
assert (k, e) == (100, 80) and k + 2 * e == 260
assert 240 - 60 * Fr('3.5') == 30 and 240 - 60 * 4 == 0

L, G, S, U = B('stochastik.grundbegriffe', 'laplace'), B('stochastik.grundbegriffe', 'grosse_zahlen'), B('gleichungen.lgs2', 'sachaufgabe'), B('gleichungen.ungleichungen', 'sachaufgabe')
rad = {'typ': 'kreisdiagramm', 'zahlen': False, 'werte': [{'name': 'G' if i % 4 == 0 else 'N', 'wert': 30} for i in range(12)]}
schreibe({
    'schluessel': '8-schulfest', 'titel': 'Schulfest',
    'einleitung': 'Beim Schulfest betreut deine Klasse ein Glücksrad und eine Losbude. Das Glücksrad hat 12 gleich große Felder; 3 davon sind Gewinnfelder (G), die anderen Nieten (N). '
                  'Mit dem Geld aus beiden Ständen soll die Klassenkasse aufgefüllt werden.',
    'voraussetzungen': [L, G, S, U],
    'teile': [
        luecken('a', 'Das Glücksrad hat 12 gleich große Felder, 3 davon sind Gewinnfelder. Wie groß ist die Wahrscheinlichkeit, bei einer Drehung zu gewinnen? Gib den Bruch gekürzt an.',
                'P(Gewinn) = □/□', 'Zähler und Nenner, vollständig gekürzt.', [1, 4], ['3 // 3', '12 // 3'],
                'Gegeben: 12 gleich wahrscheinliche Felder, 3 günstige. Gesucht: P(Gewinn). Ansatz: Laplace: günstige : mögliche. Rechnung: 3/12 = 1/4. Antwort: Die Wahrscheinlichkeit ist 1/4.',
                'Sind alle Felder gleich groß? Dann zählen.', L, grafik=rad),
        zahl('b', 'Bei jeder Drehung gewinnt man mit der Wahrscheinlichkeit 1/4. Im Lauf des Nachmittags wird das Rad 240-mal gedreht. Mit wie vielen Gewinnen muss die Klasse ungefähr rechnen?',
             60, '240 / 4',
             'Gegeben: P = 1/4, 240 Drehungen. Gesucht: erwartete Anzahl der Gewinne. Ansatz: Bei vielen Versuchen liegt die relative Häufigkeit nahe an der Wahrscheinlichkeit. '
             'Rechnung: 240 · 1/4 = 60. Antwort: Etwa 60 Gewinne.',
             'Welcher Anteil der Drehungen gewinnt ungefähr?', G),
        luecken('c', 'An der Losbude kostet ein Los für Kinder 1 €, für Erwachsene 2 €. Am Ende sind 180 Lose verkauft, in der Kasse liegen 260 €. Wie viele Kinderlose und wie viele Erwachsenenlose waren es?',
                '□ Kinderlose und □ Erwachsenenlose', 'Je Lücke eine ganze Zahl.', [k, e], ['180 - 80', '260 - 180'],
                'Gegeben: k + e = 180 (Anzahl), 1 · k + 2 · e = 260 (Euro). Gesucht: k und e. Ansatz: Subtrahieren: (k + 2e) − (k + e) = 260 − 180. '
                'Rechnung: e = 80, k = 180 − 80 = 100. Probe: 100 + 160 = 260 ✓. Antwort: 100 Kinderlose und 80 Erwachsenenlose.',
                'Eine Gleichung zählt die Lose, die andere das Geld.', S),
        auswahl('d', 'Eine Drehung am Glücksrad kostet 1 €. Bei 240 Drehungen rechnet die Klasse mit etwa 60 Gewinnen. Jeder Gewinn ist ein Preis, den die Klasse für 3,50 € eingekauft hat. '
                     'Bleibt am Glücksrad voraussichtlich Geld übrig?',
                'Ja: Etwa 240 € Einnahmen stehen etwa 210 € für Preise gegenüber, es bleiben etwa 30 € übrig.',
                ['Nein: Die Preise kosten zusammen mehr, als die Drehungen einbringen.', 'Ja: Es bleiben genau 240 € übrig, weil die Preise schon bezahlt sind.',
                 'Nein: Bei 240 Drehungen gibt es auch 240 Gewinne.'],
                'Gegeben: 240 Drehungen zu 1 €, etwa 60 Gewinne zu je 3,50 €. Gesucht: Bleibt Geld übrig? Ansatz: Einnahmen − Kosten > 0. '
                'Rechnung: 240 − 60 · 3,50 = 240 − 210 = 30 > 0. Allgemein bleibt Geld übrig, solange 240 − 60p > 0, also p < 4 € je Preis. '
                'Antwort: Ja, voraussichtlich etwa 30 € – genau vorhersagen kann man es wegen des Zufalls nicht.',
                'Vergleiche, was alle Drehungen einbringen, mit dem, was alle Preise kosten.', U),
    ],
})
