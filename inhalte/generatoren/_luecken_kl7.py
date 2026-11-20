#!/usr/bin/env python3
"""Achtzehnte Runde, Teil B (luecken-kl7): neue Lernkarten laut Lehrplan in bestehende Themen der Klasse 7 einfügen.

Die neuen Karten werden NACH dem bisherigen Zusammenbau in die fertige Themen-Datei eingesetzt
(eigener Abschnitt im Generator, eigener fester Zufallsstart):
- die Lernkarte an der Stelle „nach <lernziel>“ in inhalt.etappen,
- ihr Lernziel in denselben Abschnitt, in teilfaehigkeiten und in bewertung (Pflicht oder Vertiefung),
- ihre Aufgaben (18 Übungen 4/6/8, 1 Test, 3 Korrektur, 6 Sicherung) HINTEN an aufgaben.
Alle bisherigen Lernkarten und Aufgaben bleiben dadurch Zeichen für Zeichen gleich.
Jede Lösung wird beim Bau nachgerechnet (Zahl/Lücken über „c“, Auswahl über eine eigene Prüffunktion).

Nachweis: python3 -I inhalte/generatoren/_luecken_kl7_nachweis.py <thema_schluessel>
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
PLAN = {('uebung', 1): 4, ('uebung', 2): 6, ('uebung', 3): 8, ('test', 2): 1, ('korrektur', 2): 3, ('sicherung', 2): 6}


def _schluessel(a):
    """Gleicher Dublettenschlüssel wie tools/inhalt_pruefen.py."""
    f = a['f']
    return f['text'].strip() + '|' + json.dumps(a.get('a'), ensure_ascii=False) + '|' + json.dumps(f.get('schablone'), ensure_ascii=False) + '|' + \
        json.dumps(f.get('grafik'), sort_keys=True)


class Leer(Exception):
    """Ein Generator hat keine neue Variante mehr (z. B. derselbe Sachverhalt schon abgefragt)."""


def begrenzt():
    """Zähler je Karte: gleiche Sachverhalte höchstens n-mal abfragen (wirft Leer)."""
    import collections as _c
    z = _c.Counter()

    def oft(schluessel, n=1):
        if z[schluessel] >= n: raise Leer(schluessel)
        z[schluessel] += 1
    return oft


class Bau:
    """Aufgaben-Bausteine. Jede Funktion gibt (aufgabe, art) zurück; art: 'pruefung', 'knobel' oder None."""

    def __init__(self, R):
        self.R = R
        self.pos = collections.Counter()

    @staticmethod
    def Z(text, wert, c, w, h, einheit=None, art=None, grafik=None):
        ist = rechne(c)
        assert ist == Fr(wert), f'Nachrechnung falsch: {c} = {ist}, Lösung {wert} ({text})'
        o = {'wert': jw(Fr(wert))}
        if einheit: o['einheit'] = einheit
        a = {'y': 'zahl', 'f': {'text': text}, 'o': o, 'c': c, 'w': w, 'h': h}
        if grafik is not None: a['f']['grafik'] = grafik
        return a, art

    def A(self, text, richtig, falsche, w, h, art=None, grafik=None, pruef=None):
        """pruef(antwort) -> True, wenn die Antwort richtig ist: wird für alle Antworten ausgewertet (genau eine richtig)."""
        richtig = str(richtig)
        f = []
        for x in map(str, falsche):
            if x != richtig and x not in f: f.append(x)
        assert 2 <= len(f) <= 3, f'2–3 falsche Antworten nötig: {text} / {f}'
        if pruef is not None:
            assert pruef(richtig), f'richtige Antwort fällt durch die Prüfung: {text} / {richtig}'
            for x in f: assert not pruef(x), f'falsche Antwort wäre auch richtig: {text} / {x}'
        a = f[:]
        self.R.shuffle(a)
        n = len(a) + 1
        frei = [i for i in range(n) if self.pos[(n, i)] == min(self.pos[(n, j)] for j in range(n))]
        i = self.R.choice(frei)
        a.insert(i, richtig)
        aufg = {'y': 'auswahl', 'f': {'text': text}, 'a': a, 'o': {'index': i}, 'w': w, 'h': h}
        if grafik is not None: aufg['f']['grafik'] = grafik
        aufg['_pos'] = (n, i)
        return aufg, art

    @staticmethod
    def L(text, schablone, werte, c, w, h, hinweis, art=None, grafik=None):
        assert schablone.count('□') == len(werte) == len(c)
        for ci, v in zip(c, werte):
            assert rechne(ci) == Fr(v), f'Lücke falsch: {ci} != {v}'
            assert Fr(v).denominator == 1
        a = {'y': 'luecken', 'f': {'text': text, 'schablone': schablone, 'hinweis': hinweis},
             'o': {'werte': [int(v) for v in werte]}, 'c': list(c), 'w': w, 'h': h}
        if grafik is not None: a['f']['grafik'] = grafik
        return a, art


class Karte:
    """Eine neue Lernkarte mit allen Aufgaben.

    stufen: {1: [gen, …], 2: [gen, …], 3: [gen, …]} – gen(R, B) -> (aufgabe, art)
    fest3:  Liste fester Stufe-3-Aufgaben (gen ohne Zufall), werden zuerst verwendet (Prüfungsvorbild, Knobel)
    pools:  Generatoren für test/korrektur/sicherung (Standard: stufen[2])
    """

    def __init__(self, etappe, nach, abschnitt, tf_text, stufen, fest3=(), pools=None, vertiefung=False):
        self.etappe, self.nach, self.abschnitt, self.tf_text = etappe, nach, abschnitt, tf_text
        self.stufen, self.fest3, self.pools, self.vertiefung = stufen, list(fest3), pools or {}, vertiefung

    def aufgaben(self, R, gesehen, beispiele):
        B = Bau(R)
        l = self.etappe['lernziel']
        raus, zaehl = [], collections.Counter()

        def nimm(gen, p, s, versuche=80):
            for _ in range(versuche):
                try:
                    a, art = gen(R, B)
                except Leer:
                    return False
                k = _schluessel(a)
                kt = a['f']['text'].strip() + '|' + json.dumps(a['f'].get('grafik'), sort_keys=True)  # gleicher Text nur mit anderer Zeichnung
                if k in gesehen or kt in gesehen_text or a['f']['text'] in beispiele: continue
                gesehen.add(k)
                gesehen_text.add(kt)
                pos = a.pop('_pos', None)
                if pos: B.pos[pos] += 1
                if p != 'uebung': a.pop('h', None)
                raus.append({'l': l, 't': l, 'p': p, 's': s, **a})
                zaehl[(p, s)] += 1
                if p == 'uebung' and s == 3: zaehl[art] += 1
                return True
            return False

        gesehen_text = set()
        for gen in self.fest3: assert nimm(gen, 'uebung', 3, 1), f'{l}: feste Aufgabe doppelt ({gen.__name__})'
        for (p, s), n in PLAN.items():
            quelle = self.stufen[s] if p == 'uebung' else self.pools.get(p, self.stufen[2])
            k = R.randrange(len(quelle))
            while zaehl[(p, s)] < n:
                for d in range(len(quelle)):
                    if nimm(quelle[(k + d) % len(quelle)], p, s):
                        k += d + 1
                        break
                else:
                    raise AssertionError(f'{l}: keine neue Aufgabe mehr ({p}, Stufe {s})')
        for (p, s), n in PLAN.items(): assert zaehl[(p, s)] == n, (l, p, s, zaehl[(p, s)])
        assert zaehl['pruefung'] >= 2 and zaehl['knobel'] >= 1, f'{l}: Stufe 3 braucht ≥ 2 Prüfungsvorbild und 1 Knobel ({dict(zaehl)})'
        return raus


def einfuegen(schluessel, karten, seed, quelle=None, offen=()):
    """Setzt die neuen Karten in inhalte/themen/<schluessel>.json ein (alte Karten und Aufgaben bleiben unverändert)."""
    R = random.Random(seed)
    pfad = THEMEN / f'{schluessel}.json'
    roh = pfad.read_text(encoding='utf-8')
    d = json.loads(roh)
    inh = d['inhalt']
    gesehen = {_schluessel(a) for a in d['aufgaben']}
    neue = []
    for k in karten:
        e = k.etappe
        l = e['lernziel']
        lz = [x['lernziel'] for x in inh['etappen']]
        assert l not in lz, f'{l} gibt es schon'
        i = lz.index(k.nach) + 1
        inh['etappen'].insert(i, e)
        ab = [a for a in inh['abschnitte'] if a['titel'] == k.abschnitt]
        assert len(ab) == 1, k.abschnitt
        al = ab[0]['lernziele']
        al.insert(al.index(k.nach) + 1 if k.nach in al else len(al), l)
        tf = inh['teilfaehigkeiten']
        j = next(n for n, t in enumerate(tf) if k.nach in t['lernziele'])
        tf.insert(j + 1, {'k': l, 'text': k.tf_text, 'lernziele': [l]})
        liste = inh['bewertung']['lernziele_vertiefung' if k.vertiefung else 'lernziele_pflicht']
        liste.insert(liste.index(k.nach) + 1 if k.nach in liste else len(liste), l)
        beispiele = {(s['text'] if isinstance(s, dict) else s) for s in e['schritte']}
        neu = k.aufgaben(R, gesehen, beispiele)
        neue += neu
        print(f'  {l:18} +{len(neu)} Aufgaben ({"Vertiefung" if k.vertiefung else "Pflicht"}, nach {k.nach})')
    d['aufgaben'] += neue
    if quelle: inh.setdefault('quellen', {})['luecken_kl7'] = quelle
    if offen: d.setdefault('offen', []).extend(offen)
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')
    print(f'{pfad.name}: +{len(karten)} Lernkarten, +{len(neue)} Aufgaben (luecken-kl7) → {len(inh["etappen"])} Karten, {len(d["aufgaben"])} Aufgaben')


# ---------- kleine Hilfen für die Generatoren ----------
import math  # noqa: E402


def zf(n):
    """Ganze Zahl / Bruch mit echtem Minuszeichen und Dezimalkomma."""
    v = Fr(n)
    s = str(v.numerator) if v.denominator == 1 else f'{float(v):g}'.replace('.', ',')
    return s.replace('-', '−')


def pk(name, x, y):
    return f'{name}({zf(x)} | {zf(y)})'


def r3(v):
    return round(v + 0.0, 3)


def koord(punkte, x=None, y=None, **extra):
    """Koordinatensystem mit benannten Punkten [(x, y, name)]; Bereich mit Rand 1 um alle Punkte und 0."""
    xs = [0] + [p[0] for p in punkte] + list(x or [])
    ys = [0] + [p[1] for p in punkte] + list(y or [])
    g = {'typ': 'koordinaten', 'x': [int(math.floor(min(xs))) - 1, int(math.ceil(max(xs))) + 1],
         'y': [int(math.floor(min(ys))) - 1, int(math.ceil(max(ys))) + 1]}
    if punkte: g['punkte'] = [{'x': jw(Fr(p[0])), 'y': jw(Fr(p[1])), **({'name': p[2]} if len(p) > 2 else {})} for p in punkte]
    g.update(extra)
    return g


def fig(punkte, **extra):
    g = {'typ': 'figur', 'punkte': {k: [r3(v[0]), r3(v[1])] for k, v in punkte.items()}}
    g.update(extra)
    return g


def pol(r, grad):
    return (r * math.cos(math.radians(grad)), r * math.sin(math.radians(grad)))
