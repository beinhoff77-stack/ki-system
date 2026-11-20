#!/usr/bin/env python3
"""Zehnte Runde (schwer-kl7): schwerere Aufgaben nach Prüfungsvorbild für die Themen der Klasse 7.

Die neuen Aufgaben werden NACH dem bisherigen Zusammenbau an die fertige Themen-Datei angehängt
(eigener Abschnitt, eigener fester Zufallsstart). Alle bisherigen Aufgaben, Lernkarten und Texte
bleiben dadurch Zeichen für Zeichen gleich. Jede Lösung wird hier berechnet bzw. nachgerechnet.

Nachweis „alte Aufgaben unverändert“: python3 -I inhalte/generatoren/_schwer_kl7_nachweis.py <thema_schluessel>
"""
import collections
import json
import random
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.dont_write_bytecode = True
HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
from _bausatz import jw, rechne  # noqa: E402

THEMEN = HIER.parent / 'themen'


def _schluessel(a):
    """Gleicher Dublettenschlüssel wie tools/inhalt_pruefen.py."""
    f = a['f']
    return f['text'].strip() + '|' + json.dumps(a.get('a'), ensure_ascii=False) + '|' + json.dumps(f.get('schablone'), ensure_ascii=False) + '|' + \
        json.dumps(f.get('grafik'), sort_keys=True)


class Neu:
    """Sammelt neue Übungen. art: 'pruefung' (nach Prüfungsvorbild), 'knobel' oder None."""

    def __init__(self, seed):
        self.R = random.Random(seed)
        self.liste = []
        self.pos = collections.Counter()

    def _dazu(self, l, s, a, art, grafik):
        assert s in (2, 3), s
        assert a['h'] and len(a['w']) >= 15, a
        if grafik is not None: a['f']['grafik'] = grafik
        self.liste.append((l, s, art, a))
        return a

    def Z(self, l, s, text, wert, c, w, h, einheit=None, toleranz=None, art=None, grafik=None):
        ist = rechne(c)
        if toleranz is None:
            assert ist == Fr(wert), f'Nachrechnung falsch: {c} = {ist}, Lösung {wert} ({text})'
        else:
            assert abs(ist - Fr(wert)) <= Fr(str(toleranz)), f'außerhalb Toleranz: {c} = {float(ist)}, Lösung {wert}'
            assert ist == Fr(wert), f'„c“ muss den gerundeten Wert ergeben: {c}'
        o = {'wert': jw(Fr(wert))}
        if einheit: o['einheit'] = einheit
        if toleranz is not None: o['toleranz'] = toleranz
        return self._dazu(l, s, {'y': 'zahl', 'f': {'text': text}, 'o': o, 'c': c, 'w': w, 'h': h}, art, grafik)

    def A(self, l, s, text, richtig, falsche, w, h, art=None, grafik=None):
        richtig = str(richtig)
        f = []
        for x in map(str, falsche):
            if x != richtig and x not in f: f.append(x)
        assert 2 <= len(f) <= 3, f'2–3 falsche Antworten nötig: {text} / {f}'
        a = f[:]
        self.R.shuffle(a)
        n = len(a) + 1
        frei = [i for i in range(n) if self.pos[(n, i)] == min(self.pos[(n, j)] for j in range(n))]
        i = self.R.choice(frei)
        self.pos[(n, i)] += 1
        a.insert(i, richtig)
        return self._dazu(l, s, {'y': 'auswahl', 'f': {'text': text}, 'a': a, 'o': {'index': i}, 'w': w, 'h': h}, art, grafik)

    def L(self, l, s, text, schablone, werte, c, w, h, hinweis, art=None, grafik=None):
        assert schablone.count('□') == len(werte) == len(c)
        for ci, v in zip(c, werte):
            assert rechne(ci) == Fr(v), f'Lücke falsch: {ci} != {v}'
            assert Fr(v).denominator == 1
        return self._dazu(l, s, {'y': 'luecken', 'f': {'text': text, 'schablone': schablone, 'hinweis': hinweis},
                                  'o': {'werte': [int(v) for v in werte]}, 'c': list(c), 'w': w, 'h': h}, art, grafik)


def anhaengen(schluessel, neu):
    """Hängt die neuen Übungen an inhalte/themen/<schluessel>.json an (alte Aufgaben bleiben unverändert)."""
    pfad = THEMEN / f'{schluessel}.json'
    roh = pfad.read_text(encoding='utf-8')
    d = json.loads(roh)
    lz = [e['lernziel'] for e in d['inhalt']['etappen']]
    teil = {}
    for a in d['aufgaben']:
        teil.setdefault(a['l'], a['t'])
    gesehen = {_schluessel(a) for a in d['aufgaben']}
    beispiele = {(s['text'] if isinstance(s, dict) else s) for e in d['inhalt']['etappen'] for s in e['schritte']}
    zaehl = collections.Counter()
    for l, s, art, a in neu.liste:
        assert l in lz, l
        k = _schluessel(a)
        assert k not in gesehen, f'Dublette: {a["f"]["text"][:80]}'
        assert a['f']['text'] not in beispiele, a['f']['text']
        gesehen.add(k)
        d['aufgaben'].append({'l': l, 't': teil[l], 'p': 'uebung', 's': s, **a})
        zaehl[(l, s)] += 1
        zaehl[(l, art)] += 1
        if s == 3: zaehl[(l, art, 3)] += 1
    for l in lz:
        assert zaehl[(l, 3)] >= 4 and zaehl[(l, 2)] >= 2, f'{l}: zu wenige neue Aufgaben ({zaehl[(l, 3)]}× Stufe 3, {zaehl[(l, 2)]}× Stufe 2)'
        assert zaehl[(l, 'pruefung', 3)] >= 2, f'{l}: weniger als 2 Stufe-3-Aufgaben nach Prüfungsvorbild'
    neu_text = json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else '')
    pfad.write_text(neu_text, encoding='utf-8')
    print(f'{pfad.name}: +{len(neu.liste)} neue Übungen (schwer-kl7) → {len(d["aufgaben"])} Aufgaben')
    for l in lz:
        print(f'  {l:18} Stufe 2: {zaehl[(l, 2)]}  Stufe 3: {zaehl[(l, 3)]}  (Prüfungsvorbild {zaehl[(l, "pruefung")]}, davon Stufe 3: {zaehl[(l, "pruefung", 3)]}; Knobel {zaehl[(l, "knobel")]})')
