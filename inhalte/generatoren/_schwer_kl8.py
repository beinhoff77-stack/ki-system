"""Zehnte Runde, Klasse 8: schwerere Aufgaben nach Prüfungsvorbild (Zweig schwer-kl8).

Jeder Generator bekommt einen Abschnitt SCHWER. Die neuen Übungen werden ERST NACH dem vollständigen Bau der
bisherigen Datei angehängt (eigener fester Zufallsstart, eigene Positionsverteilung bei Auswahl-Aufgaben).
Dadurch bleiben alle bisherigen Aufgaben, Lernkarten und Zeichnungen Zeichen für Zeichen gleich.

Neue Aufgaben stehen direkt hinter der letzten Aufgabe ihrer Lernkarte. Jede Lösung wird berechnet:
Zahl-Aufgaben und Lücken werden mit dem Prüfrechner (tools/inhalt_pruefen.py) gegen "c" nachgerechnet.
Kennzeichen der Art (nur hier im Programm, nicht in der Datei): 'P' = nach Prüfungsvorbild, 'K' = Knobelaufgabe.
"""
import collections
import json
import random
from fractions import Fraction as Fr
from pathlib import Path

from _bausatz import jw, rechne

THEMEN = Path(__file__).resolve().parent.parent / 'themen'


class Neu:
    def __init__(self, seed):
        self.R = random.Random(seed)
        self.pos = collections.Counter()
        self.liste = []          # (lernziel, stufe, art, aufgabe)

    def _add(self, lz, s, art, a, h, grafik):
        assert s in (2, 3) and h and len(a['w']) >= 15, (lz, a['f']['text'])
        if grafik is not None: a['f']['grafik'] = grafik
        a['h'] = h
        self.liste.append((lz, s, art, a))
        return a

    def z(self, lz, s, text, wert, c, w, h, einheit=None, toleranz=None, grafik=None, art=''):
        if isinstance(wert, float): wert = Fr(str(wert))
        if toleranz is not None and not c.startswith('round('):
            # gerundetes Ergebnis: Rechenausdruck rundet wie verlangt (Toleranz = eine Einheit der letzten Stelle)
            n = len(str(toleranz).split('.')[1]) if '.' in str(toleranz) else 0
            c = f'round({c}, {n})' if n else f'round({c})'
        ist = rechne(c)
        assert ist == Fr(wert), f'Nachrechnung falsch: {c} = {ist}, Lösung {wert} ({text})'
        o = {'wert': jw(wert) if toleranz is None else float(wert)}
        if einheit: o['einheit'] = einheit
        if toleranz is not None: o['toleranz'] = toleranz
        return self._add(lz, s, art, {'y': 'zahl', 'f': {'text': text}, 'o': o, 'c': c, 'w': w}, h, grafik)

    def a(self, lz, s, text, richtig, falsche, w, h, grafik=None, art=''):
        richtig = str(richtig)
        f = []
        for x in falsche:
            x = str(x)
            if x != richtig and x not in f: f.append(x)
        assert 2 <= len(f) <= 3, f'2–3 falsche Antworten nötig: {text} / {f}'
        opt = f[:]
        self.R.shuffle(opt)
        n = len(opt) + 1
        frei = [i for i in range(n) if self.pos[(n, i)] == min(self.pos[(n, j)] for j in range(n))]
        i = self.R.choice(frei)
        self.pos[(n, i)] += 1
        opt.insert(i, richtig)
        return self._add(lz, s, art, {'y': 'auswahl', 'f': {'text': text}, 'a': opt, 'o': {'index': i}, 'w': w}, h, grafik)

    def l(self, lz, s, text, schablone, werte, c, w, h, hinweis='Tippe den ganzen Term ein, z. B. 3x − 2.', grafik=None, art=''):
        assert schablone.count('□') == len(werte) == len(c)
        for ci, v in zip(c, werte):
            assert rechne(ci) == Fr(v), f'Lücke falsch: {ci} != {v} ({text})'
            assert Fr(v).denominator == 1
        return self._add(lz, s, art, {'y': 'luecken', 'f': {'text': text, 'schablone': schablone, 'hinweis': hinweis},
                                      'o': {'werte': [int(v) for v in werte]}, 'c': list(c), 'w': w}, h, grafik)

    def einbauen(self, d):
        """Hängt die neuen Übungen je Lernkarte hinter deren letzte Aufgabe. Prüft Dubletten über das ganze Thema."""
        lz_alle = [e['lernziel'] for e in d['inhalt']['etappen']]
        beispiele = {(s['text'] if isinstance(s, dict) else s) for e in d['inhalt']['etappen'] for s in e['schritte']}
        schl = lambda a: (a['f']['text'], json.dumps(a.get('a'), ensure_ascii=False), json.dumps(a['f'].get('schablone'), ensure_ascii=False),
                          json.dumps(a['f'].get('grafik'), sort_keys=True))
        texte = {a['f']['text'] for a in d['aufgaben']}
        gesehen = {schl(a) for a in d['aufgaben']}
        neu = collections.defaultdict(list)
        # Teilfähigkeit wie in der Datei festgelegt (meist = Lernziel; manche Themen fassen Lernziele zusammen)
        tf = {lz: next((t['k'] for t in d['inhalt']['teilfaehigkeiten'] if lz in t.get('lernziele', [])), lz) for lz in lz_alle}
        for lz, s, art, a in self.liste:
            assert lz in lz_alle, f'Lernkarte {lz} gibt es nicht'
            # gleicher Text nur bei Auswahl-Aufgaben mit anderen Antworten (wie im Bestand üblich)
            assert a['y'] == 'auswahl' or a['f']['text'] not in texte, f'Text schon vorhanden: {a["f"]["text"]}'
            assert a['f']['text'] not in beispiele and schl(a) not in gesehen, f'doppelt: {a["f"]["text"]}'
            texte.add(a['f']['text']); gesehen.add(schl(a))
            neu[lz].append({'l': lz, 't': tf[lz], 'p': 'uebung', 's': s, **a})
        out = []
        letzte = {a['l']: i for i, a in enumerate(d['aufgaben'])}
        for i, a in enumerate(d['aufgaben']):
            out.append(a)
            if letzte.get(a['l']) == i: out.extend(neu.pop(a['l'], []))
        assert not neu, f'Lernkarten ohne alte Aufgaben: {list(neu)}'
        d['aufgaben'] = out
        return d

    def bericht(self):
        z = collections.Counter((lz, s) for lz, s, _, _ in self.liste)
        art = collections.Counter((lz, x) for lz, _, a, _ in self.liste for x in a)
        return {lz: {'s2': z[(lz, 2)], 's3': z[(lz, 3)], 'P': art[(lz, 'P')], 'K': art[(lz, 'K')]}
                for lz in dict.fromkeys(lz for lz, *_ in self.liste)}


def mit_schwer(baue, neu):
    def baue_schwer(meta, *args, **kwargs):
        d = baue(meta, *args, **kwargs)
        neu.einbauen(d)
        pfad = THEMEN / f"{meta['thema_schluessel']}.json"
        pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        b = neu.bericht()
        print(f"  + {len(neu.liste)} neue Übungen (Zehnte Runde): " + ', '.join(f"{k} {v['s3']}×S3/{v['s2']}×S2 (P{v['P']} K{v['K']})" for k, v in b.items()))
        return d
    return baue_schwer
