"""Zwanzigste Runde (Klasse 8): echte Stufe 3 und Knobel-Bordkarten.

Wird NACH allen bisherigen Bauschritten eingesetzt: baue = mit_stufen(baue, ST). Nachweis: _stufen_nachweis.py.

- typ(lz, muster, g)     Typ für vorhandene Übungen der Lernkarte (Regex auf den Fragetext, erste passende Regel gewinnt).
                         Die Stufe folgt aus dem Typ (s = Stufe von g); Frage und Antworten bleiben gleich.
- neu(lz, g, aufgabe)    neue Übung (einzeln entworfen), Stufe aus g.
- knobel(lz, aufgabe)    Knobel-Bordkarte (Pool bonus, Typ knobel, Stufe 3).
- leiter(lz, s1, s2, s3) Stufen-Leiter für den Bericht.
Überzählig (nicht gelöscht, ohne g, im Bericht): je Lernkarte, Stufe und Vorlage ab der 4. Aufgabe, je Typ und gleichem Satzbau ab der 3.,
auf Stufe 3 je Typ ab der 4. Danach werden die Übungen jeder Lernkarte so angeordnet, dass nie zwei gleiche Typen und nie zwei gleich gebaute
Aufgaben direkt hintereinander stehen.
"""
import collections
import json
import re
import sys
from pathlib import Path

from _befunde import THEMEN
from _durchsicht_kl8 import Durchsicht

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'tools'))
from inhalt_pruefen import STUFE_VON, GEDANKEN, bauplan  # noqa: E402

MIND = {1: (4, 2), 2: (6, 3), 3: (8, 4)}


def vorlage(a):
    """Bauplan, bei dem auch Terme/Gleichungen zusammengefasst sind – erkennt „dieselbe Vorlage“."""
    out = []
    for tok in bauplan(a).split():
        e = bool(re.search(r'[#=□]', tok)) or bool(re.fullmatch(r'[xyab()\[\]+−\-·:<>≤≥|²³/.,;∞]+', tok))
        tok = 'E' if e else tok
        if not (tok == 'E' and out and out[-1] == 'E'): out.append(tok)
    return ' '.join(out)


class Stufen(Durchsicht):
    def __init__(self, thema, seed):
        super().__init__(thema, seed)
        self.regeln = []           # (lz, regex, g)
        self.neue = []             # (lz, g, aufgabe)
        self.bonus = []            # (lz, aufgabe)
        self.leitern = {}
        self.nur_ein_knobel = {}
        self.quellen = []
        self.ueberzaehlig = []

    def typ(self, lz, muster, g):
        assert g in STUFE_VON, g
        self.regeln.append((lz, re.compile(muster), g))

    def neu(self, lz, g, aufgabe):
        assert g in STUFE_VON, g
        self.neue.append((lz, g, aufgabe))

    def knobel(self, lz, aufgabe):
        self.bonus.append((lz, aufgabe))

    def leiter(self, lz, s1, s2, s3):
        self.leitern[lz] = (s1, s2, s3)

    def quelle(self, text):
        self.quellen.append(text)

    # ------------------------------------------------------------------
    def anwenden(self, d):
        auf = d['aufgaben']
        tf = {e['lernziel']: next((t['k'] for t in d['inhalt']['teilfaehigkeiten'] if e['lernziel'] in t.get('lernziele', [])), e['lernziel'])
              for e in d['inhalt']['etappen']}
        karten = [e['lernziel'] for e in d['inhalt']['etappen']]
        self.vorher = {lz: collections.Counter(a['s'] for a in auf if a['l'] == lz and a['p'] == 'uebung') for lz in karten}
        # 1. Typen für vorhandene Übungen
        ohne = [f'{a["l"]}/S{a["s"]}: {a["f"]["text"]}' for a in auf if a['p'] == 'uebung'
                and not any(lz == a['l'] and rx.search(a['f']['text']) for lz, rx, g in self.regeln)]
        assert not ohne, f'{self.thema}: kein Typ für\n  ' + '\n  '.join(ohne)
        for a in auf:
            if a['p'] != 'uebung': continue
            g = next((g for lz, rx, g in self.regeln if lz == a['l'] and rx.search(a['f']['text'])), None)
            if STUFE_VON[g] != a['s']: self.zaehler['umgestuft'] += 1
            a['g'], a['s'] = g, STUFE_VON[g]
        # 2. neue Übungen und Knobel-Bordkarten
        texte = {a['f']['text'] for a in auf}
        neu_je = collections.defaultdict(list)
        for lz, g, n in self.neue:
            assert n['f']['text'] not in texte, f'schon vorhanden: {n["f"]["text"]}'
            texte.add(n['f']['text'])
            a = {'l': lz, 't': tf[lz], 'p': 'uebung', 's': STUFE_VON[g], 'g': g, **json.loads(json.dumps(n))}
            assert a.get('h') and len(a['w']) >= 15, a
            neu_je[lz].append(a)
        for lz, n in self.bonus:
            assert n['f']['text'] not in texte, f'schon vorhanden: {n["f"]["text"]}'
            texte.add(n['f']['text'])
            a = {'l': lz, 't': tf[lz], 'p': 'bonus', 's': 3, 'g': 'knobel', **json.loads(json.dumps(n))}
            assert a.get('h') and len(a['w']) >= 40, a
            neu_je[lz].append(a)
        self.zaehler['neu'] = len(self.neue)
        self.zaehler['knobel'] = len(self.bonus)
        # 3. überzählig (alte Übungen, in Dateireihenfolge)
        for lz in karten:
            alt = [a for a in auf if a['l'] == lz and a['p'] == 'uebung']
            ue = alt + [a for a in neu_je[lz] if a['p'] == 'uebung']
            v, b, t = collections.Counter(), collections.Counter(), collections.Counter()
            for a in ue:
                ks = (a['s'], vorlage(a)); kb = (a['s'], a['g'], bauplan(a))
                zu_viel = v[ks] >= 3 or b[kb] >= 2 or (a['s'] == 3 and t[a['g']] >= 3)
                if zu_viel:
                    assert a in alt, f'{self.thema}/{lz}: neue Aufgabe wäre überzählig: {a["f"]["text"]}'
                    self.ueberzaehlig.append((lz, a['s'], a['f']['text']))
                    del a['g']
                    continue
                v[ks] += 1; b[kb] += 1; t[a['g']] += 1
        # 4. Reihenfolge je Lernkarte
        reihe = {}
        for lz in karten:
            ue = [a for a in auf if a['l'] == lz and a['p'] == 'uebung'] + [a for a in neu_je[lz] if a['p'] == 'uebung']
            reihe[lz] = self.ordne(ue) + [a for a in neu_je[lz] if a['p'] == 'bonus']
        letzte = {lz: max(i for i, a in enumerate(auf) if a['l'] == lz and a['p'] == 'uebung') for lz in karten}
        neu_liste, zeiger = [], {lz: 0 for lz in karten}
        for i, a in enumerate(auf):
            if a['p'] != 'uebung':
                neu_liste.append(a); continue
            lz = a['l']
            neu_liste.append(reihe[lz][zeiger[lz]]); zeiger[lz] += 1
            if i == letzte[lz]:
                neu_liste.extend(reihe[lz][zeiger[lz]:]); zeiger[lz] = len(reihe[lz])
        assert len(neu_liste) == len(auf) + sum(len(x) for x in neu_je.values())
        d['aufgaben'] = neu_liste
        self.pruefe(d, karten)
        return d

    @staticmethod
    def ordne(ue):
        rest = list(ue)
        out = []
        schl = lambda a: a.get('g') or ('ü', bauplan(a))
        while rest:
            vor = out[-1] if out else None
            def ok(a):
                return vor is None or (schl(a) != schl(vor) and bauplan(a) != bauplan(vor))
            kand = [a for a in rest if ok(a)] or rest
            zahl = collections.Counter(schl(a) for a in rest)
            best = max(kand, key=lambda a: (zahl[schl(a)], -rest.index(a)))
            out.append(best); rest.remove(best)
        return out

    def pruefe(self, d, karten):
        self.ergebnis = {}
        for lz in karten:
            ue = [a for a in d['aufgaben'] if a['l'] == lz and a['p'] == 'uebung' and 'g' in a]
            je = {s: collections.Counter(a['g'] for a in ue if a['s'] == s) for s in (1, 2, 3)}
            for s, (n, k) in MIND.items():
                assert sum(je[s].values()) >= n and len(je[s]) >= k, f'{self.thema}/{lz}: Stufe {s} hat {dict(je[s])}, verlangt {n} Übungen mit {k} Typen'
            assert max(je[3].values()) <= 3, f'{self.thema}/{lz}: Stufe 3 je Typ höchstens 3: {dict(je[3])}'
            alle = [a for a in d['aufgaben'] if a['l'] == lz and a['p'] == 'uebung']
            for x, y in zip(alle, alle[1:]):
                assert not ('g' in x and x.get('g') == y.get('g')), f'{self.thema}/{lz}: zwei gleiche Typen hintereinander: {x["f"]["text"][:50]} / {y["f"]["text"][:50]}'
            kn = sum(1 for a in d['aufgaben'] if a['l'] == lz and a['p'] == 'bonus')
            assert kn == 2 or (kn == 1 and lz in self.nur_ein_knobel), f'{self.thema}/{lz}: {kn} Knobel-Bordkarten'
            assert lz in self.leitern, f'{self.thema}/{lz}: Stufen-Leiter fehlt'
            self.ergebnis[lz] = {s: dict(je[s]) for s in (1, 2, 3)}

    def bericht(self):
        z = self.zaehler
        return (f'{self.thema}: umgestuft {z["umgestuft"]}, neu {z["neu"]}, Knobel {z["knobel"]}, überzählig {len(self.ueberzaehlig)}')


def mit_stufen(baue, st):
    def baue_stufen(meta, *args, **kwargs):
        d = baue(meta, *args, **kwargs)
        st.anwenden(d)
        pfad = THEMEN / f"{meta['thema_schluessel']}.json"
        pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('  STUFEN ' + st.bericht())
        Path('/tmp').joinpath(f'stufen_{st.thema}.json').write_text(json.dumps(
            {'leitern': st.leitern, 'vorher': {k: dict(v) for k, v in st.vorher.items()}, 'nachher': st.ergebnis,
             'ueberzaehlig': st.ueberzaehlig, 'zaehler': dict(st.zaehler), 'quellen': st.quellen, 'nur_ein_knobel': st.nur_ein_knobel},
            ensure_ascii=False, indent=1))
        return d
    return baue_stufen
