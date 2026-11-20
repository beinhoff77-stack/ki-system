#!/usr/bin/env python3
"""Neunzehnte Runde, Teil A (Zweig durchsicht-kl10): Gesamtdurchsicht Klasse 10 – Nachbesserungen an freigegebenen Themen.

Jeder Generator der Klasse 10 bekommt ganz am Ende einen Abschnitt DURCHSICHT. Die Änderungen laufen ERST NACH allen früheren Runden
auf der fertigen Datei. Alte Aufgaben werden über ihre Stelle in der Datei (Index) angesprochen; zur Sicherheit wird der Anfang des
Fragetexts mitgegeben und geprüft. Arten wie im Auftrag:
  stufe(i, s, ...)            a) nur Feld s ändern
  berichtige(i, ..., o/h/w/c) b) Lösung, Tipp, Lösungsweg, Rechenausdruck bei gleicher Frage
  ersetze(i, ..., neu)        c) Aufgabe an derselben Stelle durch eine bessere ersetzen; alter Fragetext → Liste „ersetzt“
  neu(lz, s, aufgabe)         d) neue Übung (hinten angehängt)
  karte(lz, feld=wert, ...)   e) Lernkarte verbessern (Lernziel, Titel, Reihenfolge bleiben)
Bausteine für neue Aufgaben: Z (Zahl), A (Auswahl), L (Lücken) – Lösungen werden gegen „c“ nachgerechnet (aus _befunde).

Nachweis gegen den freigegebenen Stand:
    python3 -I -B inhalte/generatoren/_durchsicht_kl10.py <thema> [<git-stand, Standard: origin/lernen-app>]
Jede alte Aufgabe ist an ihrer Stelle entweder unverändert, nur umgestuft (nur s), nur berichtigt (nur o/h/w/c) oder ersetzt (neue Frage,
gleiche Lernkarte/Teilfähigkeit/Pool); neue Aufgaben nur hinten und nur als Übung; außerhalb der Aufgaben nur geänderte Felder gemeldeter Lernkarten
und angehängte „offen“-Einträge.
"""
import collections
import difflib  # noqa: F401
import json
import random
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _befunde import _z, _l  # noqa: E402
from _bausatz import rechne  # noqa: E402
from fractions import Fraction as Fr  # noqa: E402

THEMEN = Path(__file__).resolve().parent.parent / 'themen'
KARTENFELDER = {'einstieg', 'woerter', 'bild', 'schritte', 'fehler', 'fehler_bild', 'regel', 'probe'}


class Durchsicht:
    Z = staticmethod(_z)
    L = staticmethod(_l)

    def __init__(self, thema, seed):
        self.thema = thema
        self.R = random.Random(seed)
        self.ops = []
        self.zusatz = []
        self.karten = {}
        self.offen = []
        self.ersetzt = []
        self.sebastian = []
        self.z = collections.Counter()

    def A(self, text, richtig, falsche, w, h, grafik=None):
        richtig = str(richtig)
        f = []
        for x in falsche:
            x = str(x)
            if x != richtig and x not in f: f.append(x)
        assert 2 <= len(f) <= 3, (text, f)
        opt = f[:]
        self.R.shuffle(opt)
        i = self.R.randrange(len(opt) + 1)
        opt.insert(i, richtig)
        a = {'y': 'auswahl', 'f': {'text': text}, 'a': opt, 'o': {'index': i}, 'w': w, 'h': h}
        if grafik is not None: a['f']['grafik'] = grafik
        return a

    def stufe(self, idx, s, anfang):
        for i in (idx if isinstance(idx, (list, tuple, range)) else [idx]):
            self.ops.append(('stufe', i, anfang, {'s': s}))

    def berichtige(self, i, anfang, **felder):
        assert set(felder) <= {'o', 'h', 'w', 'c'}, felder
        self.ops.append(('berichtige', i, anfang, felder))

    def ersetze(self, i, anfang, neu, s=None):
        self.ops.append(('ersetze', i, anfang, {'neu': neu, 's': s}))

    def neu(self, lz, s, aufgabe):
        assert aufgabe is not None
        self.zusatz.append((lz, s, aufgabe))

    def karte(self, lz, **felder):
        assert set(felder) <= KARTENFELDER, felder
        self.karten.setdefault(lz, {}).update(felder)

    def offen_neu(self, text):
        self.offen.append(text)

    def fuer_sebastian(self, text):
        self.sebastian.append(text)

    def anwenden(self, mindestens=4):
        pfad = THEMEN / f'{self.thema}.json'
        roh = pfad.read_text(encoding='utf-8')
        d = json.loads(roh)
        A = d['aufgaben']
        texte = {a['f']['text'] for a in A}
        schon = set()
        for art, i, anfang, dat in self.ops:
            a = A[i]
            assert a['f']['text'].startswith(anfang), f'{self.thema}: Aufgabe {i} beginnt mit „{a["f"]["text"][:50]}“, erwartet „{anfang}“'
            assert i not in schon or art == 'stufe', f'{self.thema}: Aufgabe {i} doppelt bearbeitet'
            schon.add(i)
            if art == 'stufe':
                assert a['p'] == 'uebung' and a['s'] != dat['s'], (i, a['s'], dat['s'])
                a['s'] = dat['s']
                self.z['umgestuft'] += 1
            elif art == 'berichtige':
                for k, v in dat.items():
                    if k == 'h' and a['p'] != 'uebung': continue
                    a[k] = v
                if a['y'] == 'zahl' and 'c' in a:
                    assert rechne(a['c']) == Fr(str(a['o']['wert'])), f'Nachrechnung falsch: {a["c"]}'
                self.z['berichtigt'] += 1
            else:
                n = json.loads(json.dumps(dat['neu']))
                assert n['f']['text'] not in texte, f'Ersatztext schon vorhanden: {n["f"]["text"]}'
                texte.add(n['f']['text'])
                neu = {'l': a['l'], 't': a['t'], 'p': a['p'], 's': dat['s'] or a['s'], **n}
                if neu['p'] != 'uebung': neu.pop('h', None)
                else: assert neu.get('h'), 'Tipp fehlt'
                assert len(neu['w']) >= 15
                self.ersetzt.append(a['f']['text'])
                A[i] = neu
                self.z['ersetzt'] += 1
        tf = {t_lz: t['k'] for t in d['inhalt']['teilfaehigkeiten'] for t_lz in t['lernziele']}
        for lz, s, n in self.zusatz:
            assert n['f']['text'] not in texte, f'Dublette: {n["f"]["text"]}'
            texte.add(n['f']['text'])
            assert n.get('h') and len(n['w']) >= 15
            A.append({'l': lz, 't': tf[lz], 'p': 'uebung', 's': s, **json.loads(json.dumps(n))})
            self.z['neu'] += 1
        for e in d['inhalt']['etappen']:
            if e['lernziel'] in self.karten:
                e.update(self.karten[e['lernziel']])
                if 'probe' in self.karten[e['lernziel']] and self.karten[e['lernziel']]['probe'] is None: e.pop('probe')
                self.z['Lernkarten verbessert'] += 1
        if self.offen: d.setdefault('offen', []).extend(self.offen)
        st = collections.Counter((a['l'], a['s']) for a in A if a['p'] == 'uebung')
        for e in d['inhalt']['etappen']:
            for s in (1, 2, 3):
                assert st[(e['lernziel'], s)] >= mindestens, f'{self.thema}/{e["lernziel"]}: nur {st[(e["lernziel"], s)]} Übungen auf Stufe {s}'
        pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')
        print(f'  DURCHSICHT {self.thema}: ' + ', '.join(f'{k} {v}' for k, v in self.z.items()))
        Path(f'/tmp/durchsicht_{self.thema}.json').write_text(json.dumps(
            {'ersetzt': self.ersetzt, 'sebastian': self.sebastian, 'zaehler': dict(self.z), 'karten': sorted(self.karten)}, ensure_ascii=False, indent=1))
        return d


# ---------- Nachweis ----------
def _k(x): return json.dumps(x, ensure_ascii=False, sort_keys=True)


def nachweis(thema, stand='origin/lernen-app'):
    rel = f'inhalte/themen/{thema}.json'
    wurzel = THEMEN.parent.parent
    alt = json.loads(subprocess.run(['git', '-C', str(wurzel), 'show', f'{stand}:{rel}'], capture_output=True, check=True, text=True).stdout)
    neu = json.loads((THEMEN / f'{thema}.json').read_text(encoding='utf-8'))
    ok = True

    def fehler(m):
        nonlocal ok
        ok = False
        print('  FEHLER', m)

    for k in sorted(set(alt) | set(neu)):
        if k in ('aufgaben', 'inhalt', 'offen'): continue
        if _k(alt.get(k)) != _k(neu.get(k)): fehler(f'Feld {k} geändert')
    ai, ni = alt['inhalt'], neu['inhalt']
    for k in sorted(set(ai) | set(ni)):
        if k == 'etappen': continue
        if _k(ai.get(k)) != _k(ni.get(k)): fehler(f'inhalt.{k} geändert')
    if [e['lernziel'] for e in ai['etappen']] != [e['lernziel'] for e in ni['etappen']]: fehler('Lernkarten umsortiert/gelöscht')
    for ea, en in zip(ai['etappen'], ni['etappen']):
        felder = sorted(x for x in set(ea) | set(en) if _k(ea.get(x)) != _k(en.get(x)))
        if felder:
            if set(felder) - KARTENFELDER: fehler(f'Karte {ea["lernziel"]}: unerlaubte Felder {felder}')
            print(f'  Karte {ea["lernziel"]} verbessert: {felder}')
    ao, no = alt.get('offen', []), neu.get('offen', [])
    if no[:len(ao)] != ao: fehler('alte offen-Einträge geändert')
    A, N = alt['aufgaben'], neu['aufgaben']
    z = collections.Counter()
    for i, a in enumerate(A):
        if i >= len(N): fehler(f'Aufgabe {i} fehlt'); continue
        b = N[i]
        if _k(a) == _k(b): z['unverändert'] += 1; continue
        felder = {x for x in set(a) | set(b) if _k(a.get(x)) != _k(b.get(x))}
        if any(a[x] != b[x] for x in ('l', 't', 'p')): fehler(f'Aufgabe {i}: l/t/p geändert'); continue
        if felder == {'s'}: z['umgestuft'] += 1
        elif felder <= {'o', 'h', 'w', 'c'}: z['berichtigt'] += 1
        elif felder <= {'o', 'h', 'w', 'c', 's'} and 'f' not in felder: z['berichtigt+umgestuft'] += 1
        elif 'f' in felder and a['f']['text'] != b['f']['text']: z['ersetzt'] += 1
        else: fehler(f'Aufgabe {i}: Felder {sorted(felder)} geändert, Frage gleich')
    for b in N[len(A):]:
        if b['p'] != 'uebung': fehler('neue Aufgabe außerhalb des Übungs-Pools')
        z['neu'] += 1
    st = collections.Counter((a['l'], a['s']) for a in N if a['p'] == 'uebung')
    kn = min(st[(e['lernziel'], s)] for e in ni['etappen'] for s in (1, 2, 3))
    print(f'{thema}: alt {len(A)}, neu {len(N)}; ' + ', '.join(f'{k} {v}' for k, v in sorted(z.items())) + f'; kleinste Zahl Übungen je Karte und Stufe: {kn}')
    print('NACHWEIS OK' if ok else 'NACHWEIS FEHLGESCHLAGEN')
    return ok


if __name__ == '__main__':
    sys.exit(0 if nachweis(*sys.argv[1:]) else 1)
