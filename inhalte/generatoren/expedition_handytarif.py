#!/usr/bin/env python3
"""Expedition „Handytarif“ (Klasse 8) – Beispiel für das Format der Expeditionen (Werkstatt-Wunsch 176, Bau-Auftrag G Teil 2).

Aufruf:  python3 -I inhalte/generatoren/expedition_handytarif.py   → schreibt inhalte/expeditionen/8-handytarif.json
Alle Lösungen rechnet das Programm (Fraction, exakt). Jeder Teil nennt die Werte, die er braucht – wer einen Teil falsch hat, kann mit dem nächsten trotzdem weiterrechnen.
"""
import json
from fractions import Fraction as Fr
from pathlib import Path

ZIEL = Path(__file__).resolve().parent.parent / 'expeditionen' / '8-handytarif.json'

GRUND_A, MIN_A = Fr(5), Fr('0.10')      # Tarif A: 5 € Grundgebühr + 0,10 € je Minute
FLAT_B = Fr(12)                          # Tarif B: 12 € im Monat, alles inklusive
AUFSCHLAG = Fr(15, 100)                  # Tarif B wird 15 % teurer


def zt(x):
    """Zahl deutsch: Dezimalkomma, Minus −."""
    x = Fr(x); s = f'{float(x):.2f}'.rstrip('0').rstrip('.') if x.denominator != 1 else str(x.numerator)
    return s.replace('-', '−').replace('.', ',')


def ab_minuten(flat):
    """Kleinste ganze Minutenzahl, ab der die Flatrate günstiger ist als Tarif A: 5 + 0,10·x > flat."""
    grenze = (flat - GRUND_A) / MIN_A
    return int(grenze) + 1 if grenze.denominator == 1 else -(-grenze.numerator // grenze.denominator)


cent_a, grund_cent = int(MIN_A * 100), int(GRUND_A * 100)
ab_c = ab_minuten(FLAT_B)
flat_neu = FLAT_B * (1 + AUFSCHLAG)
ab_d = ab_minuten(flat_neu)
assert (GRUND_A + MIN_A * ab_c > FLAT_B) and not (GRUND_A + MIN_A * (ab_c - 1) > FLAT_B)
assert (GRUND_A + MIN_A * ab_d > flat_neu) and not (GRUND_A + MIN_A * (ab_d - 1) > flat_neu)

graphen = [  # Reihenfolge der Antworten: 1, 2, 3 – richtig ist Graph 2
    {'art': 'linear', 'm': float(MIN_A / 2), 't': float(GRUND_A), 'name': '1'},   # Fehler: Minutenpreis halbiert
    {'art': 'linear', 'm': float(MIN_A), 't': float(GRUND_A), 'name': '2'},       # Tarif A
    {'art': 'linear', 'm': float(MIN_A), 't': 0, 'name': '3'},                    # Fehler: Grundgebühr vergessen
]

expedition = {
    'schluessel': '8-handytarif',
    'klasse': {'gym_by': 8},
    'titel': 'Handytarif',
    'autor': 'Claude (Bau-Auftrag G, Beispiel)',
    'einleitung': 'Du brauchst einen neuen Handytarif. Tarif A kostet 5 € Grundgebühr im Monat und 0,10 € je telefonierter Minute. '
                  'Tarif B ist eine Flatrate: 12 € im Monat, egal wie lange du telefonierst. Welcher Tarif lohnt sich für dich?',
    'voraussetzungen': [
        {'thema_schluessel': 'funktionen.linear', 'lernziel': 'aufstellen'},
        {'thema_schluessel': 'funktionen.linear', 'lernziel': 'graph_ablesen'},
        {'thema_schluessel': 'gleichungen.ungleichungen', 'lernziel': 'sachaufgabe'},
        {'thema_schluessel': 'bruch.prozent_grundwert', 'lernziel': 'vermehrt'},
    ],
    'teile': [
        {'k': 'a', 'y': 'luecken',
         'f': {'text': 'Tarif A: 5 € Grundgebühr und 0,10 € je Minute. Stelle den Term für die Kosten K(x) in Cent auf, wenn du x Minuten telefonierst.',
               'schablone': '□x + □', 'hinweis': 'Kosten in Cent: zuerst der Preis je Minute, dann die Grundgebühr'},
         'o': {'werte': [cent_a, grund_cent]}, 'c': ['0.10 * 100', '5 * 100'],
         'w': f'Je Minute kommen {cent_a} Cent dazu, die Grundgebühr sind {grund_cent} Cent: K(x) = {cent_a}x + {grund_cent}.',
         'h': 'Rechne erst beides in Cent um: 1 € = 100 Cent.',
         'bezug': {'thema_schluessel': 'funktionen.linear', 'lernziel': 'aufstellen'}},
        {'k': 'b', 'y': 'auswahl',
         'f': {'text': 'Tarif A in Euro: K(x) = 0,10 · x + 5. Welcher Graph gehört zu Tarif A?',
               'grafik': {'typ': 'koordinaten', 'x': [0, 120], 'y': [0, 20], 'schritt_x': 20, 'schritt_y': 5, 'name_x': 'Minuten', 'name_y': '€', 'graphen': graphen}},
         'a': ['Graph 1', 'Graph 2', 'Graph 3'], 'o': {'index': 1},
         'w': 'Tarif A beginnt bei 5 € (bei 0 Minuten) und steigt in 10 Minuten um 1 €: bei 100 Minuten sind es 15 €. Das ist Graph 2. '
              'Graph 3 vergisst die Grundgebühr, Graph 1 steigt nur halb so schnell.',
         'h': 'Wo schneidet der Graph die senkrechte Achse? Und wie viel kosten 100 Minuten?',
         'bezug': {'thema_schluessel': 'funktionen.linear', 'lernziel': 'graph_ablesen'}},
        {'k': 'c', 'y': 'zahl',
         'f': {'text': 'Tarif A kostet 5 € + 0,10 € je Minute, Tarif B 12 € im Monat. Ab wie vielen ganzen Minuten im Monat ist Tarif B günstiger?'},
         'o': {'wert': ab_c}, 'c': '(12 - 5) / 0.10 + 1',
         'w': f'B ist günstiger, wenn 5 + 0,10 · x > 12, also 0,10 · x > 7 und x > 70. Ab {ab_c} Minuten ist B günstiger (bei genau 70 Minuten kosten beide 12 €).',
         'h': 'Stelle eine Ungleichung auf: Kosten von A > Kosten von B.',
         'bezug': {'thema_schluessel': 'gleichungen.ungleichungen', 'lernziel': 'sachaufgabe'}},
        {'k': 'd', 'y': 'zahl',
         'f': {'text': 'Tarif B (bisher 12 €) wird 15 % teurer. Tarif A bleibt bei 5 € + 0,10 € je Minute. Ab wie vielen ganzen Minuten ist Tarif B jetzt günstiger?'},
         'o': {'wert': ab_d}, 'c': '(12 * 1.15 - 5) / 0.10 + 1',
         'w': f'Neuer Preis von B: 12 € · 1,15 = {zt(flat_neu)} €. B ist günstiger, wenn 5 + 0,10 · x > {zt(flat_neu)}, also 0,10 · x > {zt(flat_neu - GRUND_A)} '
              f'und x > {zt((flat_neu - GRUND_A) / MIN_A)}. Ab {ab_d} Minuten ist B günstiger.',
         'h': 'Rechne zuerst den neuen Preis von B aus (vermehrter Grundwert), dann wie in Teil c.',
         'bezug': {'thema_schluessel': 'bruch.prozent_grundwert', 'lernziel': 'vermehrt'}},
    ],
}

ZIEL.parent.mkdir(parents=True, exist_ok=True)
ZIEL.write_text(json.dumps(expedition, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(f'geschrieben: {ZIEL.name} ({len(expedition["teile"])} Teile; Antworten c = {ab_c}, d = {ab_d})')
