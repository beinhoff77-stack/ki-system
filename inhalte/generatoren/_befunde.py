"""Dreizehnte Runde: gemeldete Mängel in vorhandenen Aufgaben beheben (Zweig befunde).

Jeder betroffene Generator bekommt am Ende einen Abschnitt BEFUNDE. Die Korrekturen werden ERST NACH dem vollständigen Bau
(inkl. Umbau und Zehnter Runde) auf die fertige Datei angewendet. Jede Korrektur sucht ihre Aufgabe über Lernkarte + genauen
Fragetext (+ optional ein Stück Text, das in Antworten/Lösung vorkommen muss) und verlangt, dass genau die erwartete Anzahl
Treffer gefunden wird. Alle anderen Aufgaben bleiben Zeichen für Zeichen gleich (Nachweis: _befunde_nachweis.py).

Arten (wie im Auftrag):
  stufe(...)     a) nur Feld s ändern
  loesung(...)   b) o / h / w / c berichtigen, Frage und Antworten bleiben gleich
  ersetze(...)   c)/d) Aufgabe durch eine berichtigte mit NEUER Frage ersetzen (gleiche Stelle, gleicher Pool, gleiche Stufe
                 sofern nicht anders angegeben); der alte Fragetext kommt in die Liste „ersetzt“
  neu(...)       zusätzliche Übung, wenn nach dem Umstufen eine Stufe unter 3 fällt
Bausteine für neue Aufgaben: Z (Zahl), A (Auswahl), L (Lücken) – Lösungen werden gegen „c“ nachgerechnet.
"""
import collections
import json
import random
from fractions import Fraction as Fr
from pathlib import Path

from _bausatz import jw, rechne

THEMEN = Path(__file__).resolve().parent.parent / 'themen'


def _z(text, wert, c, w, h, einheit=None, toleranz=None, grafik=None):
    if isinstance(wert, float): wert = Fr(str(wert))
    if toleranz is not None and not c.startswith('round('):
        n = len(str(toleranz).split('.')[1]) if '.' in str(toleranz) else 0
        c = f'round({c}, {n})' if n else f'round({c})'
    assert rechne(c) == Fr(wert), f'Nachrechnung falsch: {c} = {rechne(c)}, Lösung {wert} ({text})'
    o = {'wert': jw(wert)}
    if einheit: o['einheit'] = einheit
    if toleranz is not None: o['toleranz'] = toleranz
    a = {'y': 'zahl', 'f': {'text': text}, 'o': o, 'c': c, 'w': w, 'h': h}
    if grafik is not None: a['f']['grafik'] = grafik
    return a


def _l(text, schablone, werte, c, w, h, hinweis='Je Lücke eine ganze Zahl.', grafik=None):
    assert schablone.count('□') == len(werte) == len(c)
    for ci, v in zip(c, werte):
        assert rechne(ci) == Fr(v), f'Lücke falsch: {ci} != {v} ({text})'
    a = {'y': 'luecken', 'f': {'text': text, 'schablone': schablone, 'hinweis': hinweis}, 'o': {'werte': [int(v) for v in werte]}, 'c': list(c), 'w': w, 'h': h}
    if grafik is not None: a['f']['grafik'] = grafik
    return a


class Befunde:
    def __init__(self, thema, seed):
        self.thema = thema
        self.R = random.Random(seed)
        self.ops = []          # (art, lz, text, enthaelt, anzahl, daten)
        self.zusatz = []       # (lz, s, aufgabe)
        self.ersetzt = []      # alte Fragetexte
        self.nicht = []        # (Befund, Begründung)
        self.sebastian = []    # Hinweise „für Sebastian“
        self.zaehler = collections.Counter()

    # ---------- Bausteine ----------
    Z = staticmethod(_z)
    L = staticmethod(_l)

    def A(self, text, richtig, falsche, w, h, grafik=None, index=None):
        richtig = str(richtig)
        f = []
        for x in falsche:
            x = str(x)
            if x != richtig and x not in f: f.append(x)
        assert 2 <= len(f) <= 3, (text, f)
        opt = f[:]
        self.R.shuffle(opt)
        i = self.R.randrange(len(opt) + 1) if index is None else index
        opt.insert(i, richtig)
        a = {'y': 'auswahl', 'f': {'text': text}, 'a': opt, 'o': {'index': i}, 'w': w, 'h': h}
        if grafik is not None: a['f']['grafik'] = grafik
        return a

    # ---------- Korrekturen ----------
    def stufe(self, lz, text, s, enthaelt=None, anzahl=1, pools=('uebung',)):
        self.ops.append(('stufe', lz, text, enthaelt, anzahl, {'s': s, 'pools': pools}))

    def loesung(self, lz, text, enthaelt=None, anzahl=1, pools=None, **felder):
        assert set(felder) <= {'o', 'h', 'w', 'c'}, felder
        self.ops.append(('loesung', lz, text, enthaelt, anzahl, {'felder': felder, 'pools': pools}))

    def ersetze(self, lz, text, neu, enthaelt=None, s=None, pools=None):
        """neu: fertige Aufgabe (Z/A/L) oder Liste davon (eine je Treffer, in Reihenfolge der Datei)."""
        neue = neu if isinstance(neu, list) else [neu]
        self.ops.append(('ersetze', lz, text, enthaelt, len(neue), {'neu': neue, 's': s, 'pools': pools}))

    def neu(self, lz, s, aufgabe):
        self.zusatz.append((lz, s, aufgabe))

    def nicht_umgesetzt(self, befund, grund):
        self.nicht.append((befund, grund))

    def fuer_sebastian(self, text):
        self.sebastian.append(text)

    # ---------- Anwenden ----------
    def _treffer(self, d, lz, text, enthaelt, pools):
        out = []
        for i, a in enumerate(d['aufgaben']):
            if a['l'] != lz or a['f']['text'] != text: continue
            if pools and a['p'] not in pools: continue
            if enthaelt and enthaelt not in json.dumps(a, ensure_ascii=False): continue
            out.append(i)
        return out

    def anwenden(self, d):
        texte = {a['f']['text'] for a in d['aufgaben']}
        for art, lz, text, enthaelt, anzahl, dat in self.ops:
            idx = self._treffer(d, lz, text, enthaelt, dat.get('pools'))
            assert len(idx) == anzahl, f'{self.thema}/{lz}: {len(idx)} Treffer statt {anzahl} für „{text}“ ({enthaelt})'
            if art == 'stufe':
                for i in idx:
                    assert d['aufgaben'][i]['s'] != dat['s'], (lz, text)
                    d['aufgaben'][i]['s'] = dat['s']
                self.zaehler['umgestuft'] += len(idx)
            elif art == 'loesung':
                for i in idx:
                    a = d['aufgaben'][i]
                    for k, v in dat['felder'].items():
                        if k == 'h' and a['p'] != 'uebung': continue
                        a[k] = v
                    if a['y'] == 'zahl' and 'c' in a:
                        ist = rechne(a['c']); soll = Fr(str(a['o']['wert']))
                        assert ist == soll, f'Nachrechnung falsch nach Berichtigung: {a["c"]} = {ist}, Lösung {soll}'
                self.zaehler['berichtigt'] += len(idx)
            else:
                for i, n in zip(idx, dat['neu']):
                    alt = d['aufgaben'][i]
                    assert n['f']['text'] not in texte, f'Ersatztext schon vorhanden: {n["f"]["text"]}'
                    texte.add(n['f']['text'])
                    a = {'l': alt['l'], 't': alt['t'], 'p': alt['p'], 's': dat['s'] or alt['s'], **json.loads(json.dumps(n))}
                    if a['p'] != 'uebung': a.pop('h', None)
                    else: assert a.get('h'), 'Tipp fehlt'
                    assert len(a['w']) >= 15
                    d['aufgaben'][i] = a
                    if text not in self.ersetzt: self.ersetzt.append(text)
                self.zaehler['ersetzt'] += len(idx)
        if self.zusatz:
            tf = {lz: next((t['k'] for t in d['inhalt']['teilfaehigkeiten'] if lz in t.get('lernziele', [])), lz) for lz in [e['lernziel'] for e in d['inhalt']['etappen']]}
            letzte = {a['l']: i for i, a in enumerate(d['aufgaben'])}
            neu = collections.defaultdict(list)
            for lz, s, n in self.zusatz:
                assert n['f']['text'] not in texte, n['f']['text']
                texte.add(n['f']['text'])
                neu[lz].append({'l': lz, 't': tf[lz], 'p': 'uebung', 's': s, **n})
            out = []
            for i, a in enumerate(d['aufgaben']):
                out.append(a)
                if letzte.get(a['l']) == i: out.extend(neu.pop(a['l'], []))
            assert not neu
            d['aufgaben'] = out
            self.zaehler['neu'] += len(self.zusatz)
        self.zaehler['nicht umgesetzt'] = len(self.nicht)
        # Mindestens 3 Übungen je Stufe und Lernkarte
        st = collections.Counter((a['l'], a['s']) for a in d['aufgaben'] if a['p'] == 'uebung')
        for e in d['inhalt']['etappen']:
            for s in (1, 2, 3):
                assert st[(e['lernziel'], s)] >= 3, f'{self.thema}/{e["lernziel"]}: nur {st[(e["lernziel"], s)]} Übungen auf Stufe {s}'
        return d

    def bericht(self):
        z = self.zaehler
        return (f'{self.thema}: umgestuft {z["umgestuft"]}, berichtigt {z["berichtigt"]}, ersetzt {z["ersetzt"]}, neu {z["neu"]}, '
                f'nicht umgesetzt {len(self.nicht)}')


def mit_befunden(baue, bef):
    def baue_befunde(meta, *args, **kwargs):
        d = baue(meta, *args, **kwargs)
        bef.anwenden(d)
        pfad = THEMEN / f"{meta['thema_schluessel']}.json"
        pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('  BEFUNDE ' + bef.bericht())
        # Liste für das Postfach (wird vom Bericht-Skript gelesen)
        (Path('/tmp') / f'befunde_{meta["thema_schluessel"]}.json').write_text(json.dumps(
            {'ersetzt': bef.ersetzt, 'nicht': bef.nicht, 'sebastian': bef.sebastian, 'zaehler': dict(bef.zaehler)}, ensure_ascii=False, indent=1))
        return d
    return baue_befunde


def befunde_anwenden(datei, bef):
    """Für Generatoren, die eine fertige DATEI (dict) bauen und erst unter __main__ schreiben (Kl. 5, 6, 7, 9, 10):
    Korrekturen direkt auf DATEI anwenden; geschrieben wird wie bisher von schreibe(...)."""
    bef.anwenden(datei)
    print('  BEFUNDE ' + bef.bericht())
    (Path('/tmp') / f'befunde_{bef.thema}.json').write_text(json.dumps(
        {'ersetzt': bef.ersetzt, 'nicht': bef.nicht, 'sebastian': bef.sebastian, 'zaehler': dict(bef.zaehler)}, ensure_ascii=False, indent=1))
    return datei
