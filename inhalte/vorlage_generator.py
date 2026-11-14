#!/usr/bin/env python3
"""VORLAGE – so baut ein Chat eine Themen-Datei (Werkstatt #150).

Kopieren nach inhalte/generatoren/<thema_schluessel>.py, anpassen, ausführen:
    python3 -I inhalte/generatoren/<thema>.py      -> schreibt inhalte/themen/<thema>.json
    python3 -I tools/inhalt_pruefen.py inhalte/themen/<thema>.json

Grundsätze: Aufgaben werden vom Programm erzeugt, jede Lösung wird berechnet (nie von Hand
getippt), jede Zahl-Aufgabe bekommt den Rechenausdruck "c". Keine Schulbuchaufgaben abschreiben.
Dieses Beispiel ist absichtlich klein (Thema „Beispiel: Rechnen mit ganzen Zahlen“, KEIN echtes Thema).
"""
import json
import random
from pathlib import Path

R = random.Random(150)          # fester Startwert: gleiche Datei bei jedem Lauf
ZIEL = Path(__file__).resolve().parent / 'beispiel_vorlage.json'  # echte Themen: .../themen/<thema>.json


def zt(n):
    """Zahl deutsch schreiben: Minus als −, Tausender mit Leerzeichen."""
    s = f'{abs(n):,}'.replace(',', ' ')
    return ('−' if n < 0 else '') + s


def kl(n):
    return f'({zt(n)})' if n < 0 else zt(n)


# ---------- Lernkarten (Erklärung wie im Mathe-Lernblatt: Regel, Beispiel Schritt für Schritt, Probe, typischer Fehler) ----------
ETAPPEN = [
    {'lernziel': 'addieren', 'titel': 'Ganze Zahlen addieren',
     'regel': 'Gleiche Vorzeichen: Beträge ⟦addieren⟧, Vorzeichen behalten. Verschiedene Vorzeichen: Beträge ⟦subtrahieren⟧, Vorzeichen der Zahl mit dem größeren Betrag.',
     'schritte': ['(−7) + 4: verschiedene Vorzeichen, also 7 − 4 = 3.', 'Der größere Betrag (7) ist negativ, also ⟦−3⟧.'],
     'probe': '−3 − 4 = −7 ✓',
     'fehler': '(−7) + 4 = −11 ist falsch: Bei verschiedenen Vorzeichen wird nicht addiert, sondern ⟦subtrahiert⟧.'},
    {'lernziel': 'subtrahieren', 'titel': 'Ganze Zahlen subtrahieren',
     'regel': 'Eine Zahl subtrahieren heißt ihre ⟦Gegenzahl addieren⟧: a − (−b) = a + b.',
     'schritte': ['5 − (−3) wird zu 5 + 3.', '5 + 3 = ⟦8⟧.'],
     'probe': '8 + (−3) = 5 ✓',
     'fehler': '5 − (−3) = 2 ist falsch: Minus mal Minus wird ⟦Plus⟧.'},
    {'lernziel': 'multiplizieren', 'titel': 'Ganze Zahlen multiplizieren',
     'regel': 'Gleiche Vorzeichen ergeben ⟦plus⟧, verschiedene Vorzeichen ⟦minus⟧.',
     'schritte': ['(−6) · 4: Beträge 6 · 4 = 24.', 'Verschiedene Vorzeichen, also ⟦−24⟧.'],
     'probe': '(−24) : 4 = −6 ✓',
     'fehler': '(−6) · (−4) = −24 ist falsch: Zwei Minus ergeben ⟦Plus⟧, also 24.'},
]


def g_addieren(stufe):
    g = {1: 20, 2: 100, 3: 1000}[stufe]
    a, b = R.randint(-g, g), R.randint(-g, g)
    if a >= 0 and b >= 0: a = -a or -1
    return {'y': 'zahl', 'f': {'text': f'Berechne {kl(a)} + {kl(b)}.'}, 'o': {'wert': a + b}, 'c': f'({a}) + ({b})',
            'w': f'{"Gleiche" if (a < 0) == (b < 0) else "Verschiedene"} Vorzeichen: Ergebnis {kl(a)} + {kl(b)} = {zt(a + b)}.',
            'h': 'Vergleiche zuerst die Vorzeichen. Gleich: Beträge addieren. Verschieden: Beträge subtrahieren.'}


def g_subtrahieren(stufe):
    g = {1: 20, 2: 100, 3: 1000}[stufe]
    a, b = R.randint(-g, g), -R.randint(1, g)
    return {'y': 'zahl', 'f': {'text': f'Berechne {kl(a)} − {kl(b)}.'}, 'o': {'wert': a - b}, 'c': f'({a}) - ({b})',
            'w': f'Gegenzahl addieren: {kl(a)} − {kl(b)} = {kl(a)} + {zt(-b)} = {zt(a - b)}.',
            'h': 'Schreibe die Subtraktion als Addition der Gegenzahl.'}


def g_multiplizieren(stufe):
    g = {1: 10, 2: 15, 3: 30}[stufe]
    a, b = R.choice([-1, 1]) * R.randint(2, g), -R.randint(2, g)
    if stufe == 3 and R.random() < .5:
        e = a * b; antw = [zt(e), zt(-e), zt(abs(a) + abs(b))]
        if len(set(antw)) < 3: antw[2] = zt(e + 10)
        R.shuffle(antw)
        return {'y': 'auswahl', 'f': {'text': f'Was ergibt {kl(a)} · {kl(b)}?'}, 'a': antw, 'o': {'index': antw.index(zt(e))}, 'c': f'({a}) * ({b})',
                'w': f'Beträge: {abs(a)} · {abs(b)} = {abs(e)}. {"Gleiche" if (a < 0) == (b < 0) else "Verschiedene"} Vorzeichen, also {zt(e)}.',
                'h': 'Erst die Beträge multiplizieren, dann das Vorzeichen bestimmen.'}
    return {'y': 'zahl', 'f': {'text': f'Berechne {kl(a)} · {kl(b)}.'}, 'o': {'wert': a * b}, 'c': f'({a}) * ({b})',
            'w': f'Beträge: {abs(a)} · {abs(b)} = {abs(a * b)}. {"Gleiche" if (a < 0) == (b < 0) else "Verschiedene"} Vorzeichen, also {zt(a * b)}.',
            'h': 'Erst die Beträge multiplizieren, dann das Vorzeichen bestimmen.'}


GEN = {'addieren': g_addieren, 'subtrahieren': g_subtrahieren, 'multiplizieren': g_multiplizieren}
# Je Lernkarte: 12 Übungen (4 je Stufe), 1 Test, 3 Korrektur, 6 Sicherung = 22 Varianten, alle verschieden.
PLAN = [('uebung', 1)] * 4 + [('uebung', 2)] * 4 + [('uebung', 3)] * 4 + [('test', 2)] + [('korrektur', 2)] * 3 + [('sicherung', 2)] * 6


def aufgaben():
    out = []
    for e in ETAPPEN:
        gesehen = set(s for s in e['schritte'])
        for pool, stufe in PLAN:
            for _ in range(500):
                a = GEN[e['lernziel']](stufe)
                if a['f']['text'] not in gesehen: break
            else:
                raise SystemExit(f'zu wenige Varianten für {e["lernziel"]}')
            gesehen.add(a['f']['text'])
            if pool != 'uebung': a.pop('h', None)
            out.append({'l': e['lernziel'], 't': e['lernziel'], 'p': pool, 's': stufe, **a})
    return out


DATEI = {
    'thema_schluessel': 'beispiel.vorlage', 'thema_id': 0, 'block_id': 0,
    'klasse': {'gym_by': 5, 'rs_by': 5}, 'autor': 'Claude (Vorlage)',
    'inhalt': {
        'ziel': 'Mit ganzen Zahlen addieren, subtrahieren und multiplizieren.',
        'merke': ['Gleiche Vorzeichen: plus. Verschiedene: minus.', 'Minus einer negativen Zahl = plus.'],
        'abschnitte': [{'titel': 'Plus und Minus', 'lernziele': ['addieren', 'subtrahieren']},
                       {'titel': 'Mal', 'lernziele': ['multiplizieren']}],
        'etappen': ETAPPEN,
        'teilfaehigkeiten': [{'k': e['lernziel'], 'text': e['titel'], 'lernziele': [e['lernziel']]} for e in ETAPPEN],
        'bewertung': {'lernziele_pflicht': [e['lernziel'] for e in ETAPPEN], 'lernziele_vertiefung': [], 'testaufgaben_je_lernziel': 1},
        'quellen': {'erklaerungen': 'Eigene Fassung (Claude).', 'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern.'},
    },
    'aufgaben': aufgaben(),
}

if __name__ == '__main__':
    ZIEL.parent.mkdir(parents=True, exist_ok=True)
    ZIEL.write_text(json.dumps(DATEI, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'{ZIEL.name}: {len(DATEI["aufgaben"])} Aufgaben')
