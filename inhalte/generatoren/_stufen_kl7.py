"""Zwanzigste Runde (stufen-kl7): echte Stufe 3 und Knobel-Bordkarten für die Themen der Klasse 7.

Wird NACH allen früheren Runden auf die fertige Themen-Datei angewendet (eigener Abschnitt STUFEN im Generator, eigener Zufallsstart):
  regel(lz, s, muster, g, neu_s=None)  alte Übungen der Stufe s, deren Fragetext `muster` enthält (oder Regex „re:…“), bekommen den Typ g
                                        (mit neu_s zusätzlich eine andere Stufe – Frage und Antworten bleiben gleich)
  neu(lz, s, g, aufgabe)               neue Übung (einzeln entworfen)
  knobel(lz, aufgabe)                  Knobel-Bordkarte (Pool bonus, Typ knobel, Stufe 3)
Danach:
  - „überzählig“: Gibt es auf einer Stufe mehr als 2 alte Übungen desselben Typs mit gleichem Satzbau (Fragetext ohne Zahlen),
    behalten die ersten zwei ihren Typ; die übrigen bleiben ohne Typ und stehen in der Liste „überzählig“ (der Haupt-Chat sperrt sie).
  - Prüfung je Lernkarte (ohne die überzähligen): Stufe 1 ≥ 4 Übungen / ≥ 2 Typen, Stufe 2 ≥ 6 / ≥ 3, Stufe 3 ≥ 8 / ≥ 4 Typen, je Typ ≤ 3;
    höchstens 2 Übungen je Stufe, Typ und Satzbau; 1–3 Knobel-Bordkarten.
  - Reihenfolge: Die Übungen einer Lernkarte werden in ihren bisherigen Plätzen neu angeordnet, so dass nie zwei Aufgaben desselben Typs
    und nie zwei gleich gebaute direkt hintereinander stehen; neue Übungen und Knobel-Bordkarten folgen direkt dahinter.
Alte Aufgaben ändern sich nur in g (und s, wo angegeben). Nachweis: python3 -I inhalte/generatoren/_stufen_nachweis.py <thema>
"""
import collections
import json
import random
import re
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.dont_write_bytecode = True
HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
from _bausatz import jw, rechne  # noqa: E402

THEMEN = HIER.parent / 'themen'
GEDANKEN = {1: ('direkt', 'erkennen'), 2: ('mehrschritt', 'einkleidung', 'umkehr', 'darstellung'),
            3: ('rueckwaerts', 'verknuepfen', 'begruenden', 'fehler', 'transfer', 'parameter', 'pruefung')}
STUFE_VON = {g: s for s, gs in GEDANKEN.items() for g in gs}
ZAHL = re.compile(r'[−-]?\d+(?:[  ]\d{3})*(?:[,.]\d+)?')


def bauplan(a):
    return re.sub(r'\s+', ' ', ZAHL.sub('#', str(a['f']['text']))).strip()


def _schl(a):
    f = a['f']
    return f['text'].strip() + '|' + json.dumps(a.get('a'), ensure_ascii=False) + '|' + json.dumps(f.get('schablone'), ensure_ascii=False) + '|' + \
        json.dumps(f.get('grafik'), sort_keys=True)


class Stufen:
    def __init__(self, thema, seed):
        self.thema, self.R = thema, random.Random(seed)
        self.regeln = collections.defaultdict(list)   # lz -> [(s, muster, g, neu_s)]
        self.neue = collections.defaultdict(list)     # lz -> [(s, g, aufgabe)]
        self.knobel_ = collections.defaultdict(list)
        self.leitern = {}
        self.ueberzaehlig = []
        self.zaehler = collections.Counter()
        self.vorher, self.nachher = {}, {}

    # ---------- Bausteine ----------
    @staticmethod
    def Z(text, wert, c, w, h, einheit=None, grafik=None):
        ist = rechne(c)
        assert ist == Fr(str(wert)) if isinstance(wert, float) else ist == Fr(wert), f'Nachrechnung falsch: {c} = {ist}, Lösung {wert} ({text})'
        o = {'wert': jw(Fr(str(wert)) if isinstance(wert, float) else Fr(wert))}
        if einheit: o['einheit'] = einheit
        a = {'y': 'zahl', 'f': {'text': text}, 'o': o, 'c': c, 'w': w, 'h': h}
        if grafik is not None: a['f']['grafik'] = grafik
        return a

    @staticmethod
    def L(text, schablone, werte, c, w, h, hinweis='Trage in jedes Feld eine Zahl ein.', grafik=None):
        assert schablone.count('□') == len(werte) == len(c), text
        for ci, v in zip(c, werte):
            assert rechne(ci) == Fr(v), f'Lücke falsch: {ci} != {v} ({text})'
        a = {'y': 'luecken', 'f': {'text': text, 'schablone': schablone, 'hinweis': hinweis}, 'o': {'werte': [int(v) for v in werte]}, 'c': list(c), 'w': w, 'h': h}
        if grafik is not None: a['f']['grafik'] = grafik
        return a

    def A(self, text, richtig, falsche, w, h, grafik=None, pruef=None):
        richtig = str(richtig)
        f = []
        for x in map(str, falsche):
            if x != richtig and x not in f: f.append(x)
        assert 2 <= len(f) <= 3, (text, f)
        if pruef is not None:
            assert pruef(richtig), f'richtige Antwort fällt durch: {text}'
            for x in f: assert not pruef(x), f'falsche Antwort wäre richtig: {text} / {x}'
        opt = f[:]
        self.R.shuffle(opt)
        i = self.R.randrange(len(opt) + 1)
        opt.insert(i, richtig)
        a = {'y': 'auswahl', 'f': {'text': text}, 'a': opt, 'o': {'index': i}, 'w': w, 'h': h}
        if grafik is not None: a['f']['grafik'] = grafik
        return a

    # ---------- Angaben ----------
    def leiter(self, lz, s1, s2, s3):
        self.leitern[lz] = (s1, s2, s3)

    def regel(self, lz, s, muster, g, neu_s=None):
        assert STUFE_VON[g] == (neu_s or s), (lz, muster, g)
        self.regeln[lz].append((s, muster, g, neu_s))

    def neu(self, lz, s, g, aufgabe):
        assert STUFE_VON[g] == s, (lz, g, s)
        self.neue[lz].append((s, g, aufgabe))

    def knobel(self, lz, aufgabe):
        self.knobel_[lz].append(aufgabe)

    # ---------- Anwenden ----------
    @staticmethod
    def _passt(muster, text):
        return re.search(muster[3:], text) is not None if muster.startswith('re:') else muster in text

    def anwenden(self, d):
        lzs = [e['lernziel'] for e in d['inhalt']['etappen']]
        tf = {lz: next(t['k'] for t in d['inhalt']['teilfaehigkeiten'] if lz in t['lernziele']) for lz in lzs}
        texte = {_schl(a) for a in d['aufgaben']}
        fehler = []
        for lz in lzs:
            plaetze = [i for i, a in enumerate(d['aufgaben']) if a['l'] == lz and a['p'] == 'uebung']
            alte = [d['aufgaben'][i] for i in plaetze]
            self.vorher[lz] = collections.Counter((a['s'], a.get('g', '–')) for a in alte)
            benutzt = collections.Counter()
            for a in alte:
                for k, (s, muster, g, neu_s) in enumerate(self.regeln[lz]):
                    if a['s'] == s and self._passt(muster, a['f']['text']):
                        benutzt[k] += 1
                        if neu_s and neu_s != a['s']:
                            a['s'] = neu_s
                            self.zaehler['umgestuft'] += 1
                        a['g'] = g
                        break
                else:
                    fehler.append(f'{lz}: keine Regel für Stufe {a["s"]}: „{a["f"]["text"][:90]}“')
            for k, r in enumerate(self.regeln[lz]):
                if not benutzt[k]: fehler.append(f'{lz}: Regel ohne Treffer: {r}')
            # überzählig: mehr als 2 alte Übungen je Stufe, Typ und Satzbau
            gruppen = collections.defaultdict(list)
            for a in alte:
                if a.get('g'): gruppen[(a['s'], a['g'], bauplan(a))].append(a)
            for (s, g, b), xs in gruppen.items():
                for a in xs[2:]:
                    del a['g']
                    self.ueberzaehlig.append((lz, s, a['f']['text']))
            # neue Übungen und Knobel-Bordkarten
            neu = []
            for s, g, aufg in self.neue[lz]:
                a = {'l': lz, 't': tf[lz], 'p': 'uebung', 's': s, 'g': g, **aufg}
                k = _schl(a)
                assert k not in texte, f'Dublette: {a["f"]["text"]}'
                assert a.get('h') and len(a['w']) >= 15, a['f']['text']
                texte.add(k)
                neu.append(a)
            self.zaehler['neu'] += len(neu)
            bonus = []
            for aufg in self.knobel_[lz]:
                a = {'l': lz, 't': tf[lz], 'p': 'bonus', 's': 3, 'g': 'knobel', **aufg}
                k = _schl(a)
                assert k not in texte, f'Dublette: {a["f"]["text"]}'
                assert a.get('h') and len(a['w']) >= 60, f'Knobel braucht Tipp und ausführlichen Weg: {a["f"]["text"][:60]}'
                texte.add(k)
                bonus.append(a)
            self.zaehler['knobel'] += len(bonus)
            # Prüfung der Mengen (ohne überzählige)
            alle = alte + neu
            mit = [a for a in alle if a.get('g')]
            for s, (mn, mt) in {1: (4, 2), 2: (6, 3), 3: (8, 4)}.items():
                xs = [a for a in mit if a['s'] == s]
                typen = collections.Counter(a['g'] for a in xs)
                if len(xs) < mn or len(typen) < mt: fehler.append(f'{lz}: Stufe {s} hat {len(xs)} Übungen / {len(typen)} Typen {dict(typen)}, nötig {mn} / {mt}')
                if s == 3 and max(typen.values() or [0]) > 3: fehler.append(f'{lz}: Stufe 3 mehr als 3 Übungen eines Typs: {dict(typen)}')
                bau = collections.Counter((a['g'], bauplan(a)) for a in xs)
                for (g, b), n in bau.items():
                    if n > 2: fehler.append(f'{lz}: Stufe {s}, Typ {g}: {n}× „{b[:60]}“')
            if not 1 <= len(bonus) <= 3: fehler.append(f'{lz}: {len(bonus)} Knobel-Bordkarten')
            self.nachher[lz] = collections.Counter((a['s'], a.get('g') or 'überzählig') for a in alle)
            # Reihenfolge: nie zwei gleiche Typen / Satzbauten hintereinander
            folge = self._ordnen(alle)
            if folge is None: fehler.append(f'{lz}: keine Reihenfolge ohne gleiche Typen hintereinander gefunden')
            else:
                for i, a in zip(plaetze, folge[:len(plaetze)]): d['aufgaben'][i] = a
                rest = folge[len(plaetze):] + bonus
                ende = plaetze[-1] + 1
                d['aufgaben'][ende:ende] = rest
        assert not fehler, 'STUFEN ' + self.thema + ':\n  ' + '\n  '.join(fehler)
        return d

    def _ordnen(self, aufg):
        R = random.Random(len(aufg) * 7919 + 17)
        for _ in range(400):
            rest = aufg[:]
            folge = []
            while rest:
                vor = folge[-1] if folge else None
                kand = [a for a in rest if vor is None or ((a.get('g') or id(a)) != (vor.get('g') or id(vor)) and bauplan(a) != bauplan(vor))]
                if not kand: break
                # bevorzugt die Gruppe mit den meisten verbleibenden Aufgaben (verhindert Stau am Ende)
                zahl = collections.Counter(a.get('g') or bauplan(a) for a in rest)
                m = max(zahl[a.get('g') or bauplan(a)] for a in kand)
                beste = [a for a in kand if zahl[a.get('g') or bauplan(a)] == m]
                a = R.choice(beste)
                folge.append(a)
                rest.remove(a)
            if not rest: return folge
        return None

    def bericht(self):
        z = self.zaehler
        return f'{self.thema}: umgestuft {z["umgestuft"]}, neu {z["neu"]}, Knobel {z["knobel"]}, überzählig {len(self.ueberzaehlig)}'


def stufen_datei(schluessel, st):
    pfad = THEMEN / f'{schluessel}.json'
    roh = pfad.read_text(encoding='utf-8')
    d = st.anwenden(json.loads(roh))
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')
    print('  STUFEN ' + st.bericht())
    (Path('/tmp') / f'stufen_{schluessel}.json').write_text(json.dumps(
        {'zaehler': dict(st.zaehler), 'ueberzaehlig': st.ueberzaehlig, 'leitern': st.leitern,
         'vorher': {l: {f'{s}:{g}': n for (s, g), n in c.items()} for l, c in st.vorher.items()},
         'nachher': {l: {f'{s}:{g}': n for (s, g), n in c.items()} for l, c in st.nachher.items()}}, ensure_ascii=False, indent=1))
    return d
