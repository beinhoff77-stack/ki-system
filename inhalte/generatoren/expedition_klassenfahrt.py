#!/usr/bin/env python3
"""Expedition „Klassenfahrt“ (Klasse 8): indirekte Proportionalität · Term aufstellen · Ungleichung · verminderter Grundwert.
Aufruf: python3 -I inhalte/generatoren/expedition_klassenfahrt.py → inhalte/expeditionen/8-klassenfahrt.json"""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _exp8 import B, zt, zahl, luecken, auswahl, schreibe

BUS = Fr(840)            # Busmiete gesamt, gleich verteilt
NACHT = Fr(28)           # Herberge je Kind und Nacht
ANTEIL = BUS / 28        # Busanteil bei 28 Kindern = 30 €
GRENZE = Fr(150)         # höchstens 150 € je Kind
RABATT = Fr(15, 100)     # 15 % auf die Übernachtungen ab 5 Nächten

assert BUS / 24 == 35 and ANTEIL == 30
n_max = max(n for n in range(0, 20) if NACHT * n + ANTEIL <= GRENZE)
assert n_max == 4
mit_rabatt = ANTEIL + 5 * NACHT * (1 - RABATT)
assert mit_rabatt == Fr(149) and mit_rabatt <= GRENZE and ANTEIL + 5 * NACHT == 170 and ANTEIL + 4 * NACHT == 142

I, L, U, P = B('groessen.indirekt', 'sach'), B('funktionen.linear', 'aufstellen'), B('gleichungen.ungleichungen', 'sachaufgabe'), B('bruch.prozent_grundwert', 'vermindert')
schreibe({
    'schluessel': '8-klassenfahrt', 'titel': 'Klassenfahrt',
    'einleitung': 'Deine Klasse plant eine Klassenfahrt an die Ostsee. Der Reisebus kostet für alle zusammen 840 €, die Miete wird gleichmäßig auf die Kinder verteilt. '
                  'In der Jugendherberge zahlt jedes Kind 28 € pro Nacht. Die Eltern haben gesagt: Mehr als 150 € pro Kind soll die Fahrt nicht kosten.',
    'voraussetzungen': [I, L, U, P],
    'teile': [
        zahl('a', 'Der Bus kostet 840 €. Fahren 24 Kinder mit, zahlt jedes 35 €. Jetzt haben sich 28 Kinder angemeldet. Wie viel Euro Busgeld zahlt jedes Kind?',
             ANTEIL, '840 / 28',
             'Gegeben: 840 € werden gleich verteilt. Gesucht: Anteil bei 28 Kindern. Ansatz: Kinder · Anteil = 840 € bleibt gleich (indirekt proportional). '
             'Rechnung: 840 : 28 = 30. Antwort: Jedes Kind zahlt 30 € für den Bus.',
             'Mehr Kinder teilen sich denselben Betrag. Was bleibt gleich?', I, einheit='€'),
        luecken('b', 'Jedes Kind zahlt 30 € für den Bus und 28 € für jede Nacht in der Herberge. Stelle den Term für die Kosten K(n) eines Kindes bei n Nächten auf.',
                'K(n) = □ · n + □', 'Je Lücke eine ganze Zahl (Euro).', [NACHT, ANTEIL], ['28', '30'],
                'Gegeben: 28 € je Nacht, 30 € einmal für den Bus. Gesucht: K(n). Ansatz: Was mit jeder Nacht dazukommt, steht vor n; was einmal anfällt, ist der feste Teil. '
                'Antwort: K(n) = 28 · n + 30.',
                'Welcher Betrag kommt mit jeder Nacht dazu, welcher nur einmal?', L),
        zahl('c', 'Ein Kind zahlt 28 € pro Nacht und einmal 30 € für den Bus. Es soll höchstens 150 € zahlen. Wie viele Nächte kann die Klasse höchstens bleiben?',
             n_max, '(150 - 30) // 28',
             'Gegeben: K(n) = 28n + 30, höchstens 150 €. Gesucht: größte ganze Zahl n. Ansatz: 28n + 30 ≤ 150. '
             'Rechnung: 28n ≤ 120, also n ≤ 120 : 28 ≈ 4,3; ganze Nächte: n = 4 (Probe: 4 Nächte kosten 142 €, 5 Nächte kosten 170 €). Antwort: höchstens 4 Nächte.',
             'Stelle eine Ungleichung auf. Kann man eine halbe Nacht buchen?', U),
        auswahl('d', 'Die Herberge macht ein Angebot: Wer 5 Nächte bucht, bekommt 15 % Rabatt auf die Übernachtungen (28 € pro Nacht). Der Bus (30 € pro Kind) wird nicht billiger. '
                     'Kann die Klasse jetzt 5 Nächte bleiben, ohne dass ein Kind mehr als 150 € zahlt?',
                'Ja: Mit Rabatt kostet es 149 € pro Kind.',
                ['Nein: Auch mit Rabatt kostet es mehr als 150 € pro Kind.', 'Nein: Mit Rabatt kostet es 151 € pro Kind.', 'Nein: Schon 4 Nächte kosten mehr als 150 €.'],
                f'Gegeben: 5 Nächte zu 28 €, 15 % Rabatt nur darauf, Bus 30 €. Gesucht: Kosten pro Kind und Entscheidung. Ansatz: verminderter Grundwert: 85 % von 5 · 28 €. '
                f'Rechnung: 5 · 28 = 140 €; 140 · 0,85 = 119 €; 119 + 30 = {zt(mit_rabatt)} €. Antwort: {zt(mit_rabatt)} € ≤ 150 € – die Klasse kann 5 Nächte bleiben.',
                'Rechne erst den Preis der Übernachtungen mit Rabatt aus, dann kommt der Bus dazu.', P),
    ],
})
