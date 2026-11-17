"""Zwanzigste Runde (Zweig stufen-kl10): echte Stufe 3 und Knobel-Bordkarten für Klasse 10.

Läuft als letzter Abschnitt jedes Generators auf der fertigen Themendatei:
  S = Stufen('thema')
  S.g('lernziel', direkt=[0, 1], erkennen=[5], ...)   # Typ je vorhandener Übung (Index wie in origin/lernen-app); die Stufe folgt aus dem Typ
  S.neu('lernziel', 'transfer', S.Z(...))               # neue Übung, Typ bestimmt die Stufe
  S.bonus('lernziel', S.Z(...))                          # Knobel-Bordkarte (Pool bonus, Typ knobel, Stufe 3)
  S.anwenden()
Überzählig: Von Übungen mit gleichem Typ und gleichem Satzbau (Fragetext ohne Zahlen) bleiben die ersten zwei; die weiteren bekommen
KEIN g, behalten ihre Stufe und stehen in der Liste „überzählig“ (der Haupt-Chat sperrt sie). Ohne sie muss jede Lernkarte die strengen
Regeln von tools/inhalt_pruefen.py erfüllen – das prüft anwenden() mit dem Prüfskript selbst an einer Kopie ohne die überzähligen.
Reihenfolge: je Lernkarte Übungen nach Stufe, darin nie zwei gleiche Typen und nie zwei gleich gebaute direkt hintereinander;
überzählige werden so eingestreut, dass keine Gruppe „gleich gebaut hintereinander“ entsteht. Danach Test/Korrektur/Sicherung, dann Bonus.
Nachweis gegen origin/lernen-app: python3 -I -B inhalte/generatoren/_stufen_kl10.py <thema>
"""
import collections
import json
import random
import subprocess
import sys
import tempfile
from fractions import Fraction as Fr
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
sys.path.insert(0, str(HIER.parent.parent / 'tools'))
from _befunde import _z, _l  # noqa: E402
from _bausatz import rechne  # noqa: E402
import inhalt_pruefen as IP  # noqa: E402

THEMEN = HIER.parent / 'themen'
STUFE_VON = IP.STUFE_VON
S3_HOECHSTENS = 3       # je Typ höchstens 3 auf Stufe 3 (Auftrag Zwanzigste Runde)
MIN_ANZAHL = {1: 4, 2: 6, 3: 8}


class Stufen:
    def __init__(self, thema, seed=20):
        self.thema = thema
        self.R = random.Random(seed)
        self.typ = {}            # index -> g
        self.lz_von = {}         # index -> lernziel laut Angabe
        self.neue = []           # (lz, g, aufgabe)
        self.boni = []           # (lz, aufgabe)
        self.weg = set()         # ausdrücklich überzählig
        self.leiter = {}         # lz -> (s1, s2, s3)
        self.t_von = {}          # lz -> Teilfähigkeit für neue Aufgaben (optional)

    # ---- Bausteine ----
    Z = staticmethod(_z)
    L = staticmethod(_l)

    def ZR(self, text, x, n, w, h, einheit=None, grafik=None):
        """Zahl-Aufgabe mit gerundetem Ergebnis (Logarithmus, Wurzel, π): x wird in Python berechnet, c rundet nach."""
        wert = round(x, n) if n else int(round(x))
        return _z(text, wert, f'round({x:.12f}, {n})' if n else f'round({x:.12f})', w, h, einheit=einheit,
                  toleranz=(1 if n == 0 else float(f'1e-{n}')), grafik=grafik)

    def A(self, text, richtig, falsche, w, h, grafik=None):
        richtig = str(richtig)
        f = []
        for x in falsche:
            x = str(x)
            assert x != richtig, (text, x)
            if x not in f: f.append(x)
        assert 2 <= len(f) <= 3, (text, f)
        opt = f[:]
        self.R.shuffle(opt)
        i = self.R.randrange(len(opt) + 1)
        opt.insert(i, richtig)
        a = {'y': 'auswahl', 'f': {'text': text}, 'a': opt, 'o': {'index': i}, 'w': w, 'h': h}
        if grafik is not None: a['f']['grafik'] = grafik
        return a

    # ---- Angaben ----
    def g(self, lz, **typen):
        for g, idx in typen.items():
            assert g in STUFE_VON, g
            for i in (idx if isinstance(idx, (list, tuple, range)) else [idx]):
                assert i not in self.typ, f'{self.thema}: Übung {i} doppelt typisiert'
                self.typ[i] = g
                self.lz_von[i] = lz

    def ueberzaehlig(self, *idx):
        self.weg.update(idx)

    def stufenleiter(self, lz, s1, s2, s3):
        self.leiter[lz] = (s1, s2, s3)

    def neu(self, lz, g, aufgabe):
        assert g in STUFE_VON, g
        self.neue.append((lz, g, aufgabe))

    def bonus(self, lz, aufgabe):
        self.boni.append((lz, aufgabe))

    # ---- Anwenden ----
    def anwenden(self):
        pfad = THEMEN / f'{self.thema}.json'
        roh = pfad.read_text(encoding='utf-8')
        d = json.loads(roh)
        A = d['aufgaben']
        karten = [e['lernziel'] for e in d['inhalt']['etappen']]
        tf = {lz: t['k'] for t in d['inhalt']['teilfaehigkeiten'] for lz in t['lernziele']}
        texte = {a['f']['text'] for a in A}
        bericht = {'thema': self.thema, 'karten': {}, 'ueberzaehlig': [], 'umgestuft': 0, 'neu': 0, 'bonus': 0}
        # 1. Typen der vorhandenen Übungen
        vorher = collections.Counter()
        for i, a in enumerate(A):
            if a['p'] != 'uebung': continue
            assert i in self.typ, f'{self.thema}: Übung {i} ({a["l"]}, S{a["s"]}) ohne Typ: {a["f"]["text"][:80]}'
            assert self.lz_von[i] == a['l'], f'{self.thema}: Übung {i} gehört zu {a["l"]}, nicht {self.lz_von[i]}'
            vorher[(a['l'], a['s'], self.typ[i])] += 1
        assert set(self.typ) <= {i for i, a in enumerate(A) if a['p'] == 'uebung'}, 'Typ für Nicht-Übung angegeben'
        # Überzählig: je (Lernkarte, Typ, Satzbau) die ersten zwei behalten
        gruppe = collections.defaultdict(list)
        for i in sorted(self.typ):
            gruppe[(A[i]['l'], self.typ[i], IP.bauplan(A[i]))].append(i)
        weg = set(self.weg)
        for xs in gruppe.values():
            weg.update(xs[IP.MAX_GLEICH_GEBAUT:])
        alt_s = {i: a['s'] for i, a in enumerate(A)}
        for i, g in self.typ.items():
            if i in weg: continue
            A[i]['g'] = g
            if A[i]['s'] != STUFE_VON[g]:
                A[i]['s'] = STUFE_VON[g]
                bericht['umgestuft'] += 1
        for i in sorted(weg):
            bericht['ueberzaehlig'].append({'l': A[i]['l'], 's': A[i]['s'], 'text': A[i]['f']['text']})
        # 2. neue Übungen und Bonus
        for lz, g, n in self.neue:
            n = json.loads(json.dumps(n))
            assert lz in karten, lz
            assert n['f']['text'] not in texte, f'Dublette: {n["f"]["text"]}'
            texte.add(n['f']['text'])
            assert n.get('h') and len(n['w']) >= 15, n['f']['text']
            A.append({'l': lz, 't': self.t_von.get(lz, tf[lz]), 'p': 'uebung', 's': STUFE_VON[g], 'g': g, **n})
            bericht['neu'] += 1
        for lz, n in self.boni:
            n = json.loads(json.dumps(n))
            assert n['f']['text'] not in texte, f'Dublette: {n["f"]["text"]}'
            texte.add(n['f']['text'])
            assert n.get('h') and len(n['w']) >= 40, n['f']['text']
            A.append({'l': lz, 't': self.t_von.get(lz, tf[lz]), 'p': 'bonus', 's': 3, 'g': 'knobel', **n})
            bericht['bonus'] += 1
        for x in A:
            if x['y'] == 'zahl' and 'c' in x:
                assert rechne(x['c']) == Fr(str(x['o']['wert'])), f'Nachrechnung: {x["f"]["text"][:60]}'
        # 3. Regeln je Lernkarte (ohne Überzählige) und neue Reihenfolge
        weg_ids = {id(A[i]) for i in weg}
        neu_A = []
        for lz in karten:
            ue = [a for a in A if a['l'] == lz and a['p'] == 'uebung']
            aktiv = [a for a in ue if id(a) not in weg_ids]
            raus = [a for a in ue if id(a) in weg_ids]
            nach = collections.Counter((a['s'], a['g']) for a in aktiv)
            for s in (1, 2, 3):
                xs = [a for a in aktiv if a['s'] == s]
                typen = collections.Counter(a['g'] for a in xs)
                assert len(xs) >= MIN_ANZAHL[s], f'{self.thema}/{lz}: Stufe {s} hat {len(xs)} Übungen, mindestens {MIN_ANZAHL[s]}'
                assert len(typen) >= IP.MIN_TYPEN[s], f'{self.thema}/{lz}: Stufe {s} hat {len(typen)} Typen {dict(typen)}'
                assert max(typen.values()) <= (len(xs) + 1) // 2, f'{self.thema}/{lz}: Stufe {s}: ein Typ zu häufig, sonst stehen zwei gleiche hintereinander: {dict(typen)}'
                if s == 3:
                    zuviel = {g: n for g, n in typen.items() if n > S3_HOECHSTENS}
                    assert not zuviel, f'{self.thema}/{lz}: Stufe 3 mehr als {S3_HOECHSTENS} je Typ: {zuviel}'
            reihe = []
            for s in (1, 2, 3):
                reihe += self._ordne([a for a in aktiv if a['s'] == s])
            for a in raus:
                self._einstreuen(reihe, a)
            for k in range(1, len(reihe)):
                p, q = reihe[k - 1], reihe[k]
                assert not (p.get('g') and p.get('g') == q.get('g')), f'{self.thema}/{lz}: zwei „{q["g"]}“ hintereinander'
            andere = [a for a in A if a['l'] == lz and a['p'] not in ('uebung', 'bonus')]
            boni = [a for a in A if a['l'] == lz and a['p'] == 'bonus']
            assert len(boni) <= IP.MAX_BONUS
            neu_A += reihe + andere + boni
            vor = collections.Counter({(s, g): n for (l, s, g), n in vorher.items() if l == lz})
            bericht['karten'][lz] = {'vorher': {f'{s}|{g}': n for (s, g), n in sorted(vor.items())},
                                     'nachher': {f'{s}|{g}': n for (s, g), n in sorted(nach.items())},
                                     'ueberzaehlig': len(raus), 'bonus': len(boni), 'leiter': self.leiter.get(lz)}
            assert lz in self.leiter, f'{self.thema}/{lz}: Stufen-Leiter fehlt'
        assert len(neu_A) == len(A) and {id(a) for a in neu_A} == {id(a) for a in A}
        d['aufgaben'] = neu_A
        pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')
        # 4. strenge Prüfung an einer Kopie ohne die Überzähligen
        kopie = json.loads(json.dumps(d))
        kopie['aufgaben'] = [a for a in kopie['aufgaben'] if not (a['p'] == 'uebung' and a.get('g') is None)]
        with tempfile.TemporaryDirectory() as td:
            k = Path(td) / f'{self.thema}.json'
            k.write_text(json.dumps(kopie, ensure_ascii=False), encoding='utf-8')
            f, w, info = IP.pruefe(k)
        assert not f, f'{self.thema}: strenge Prüfung ohne Überzählige: {f[:5]}'
        assert info['gleich_gebaut_hintereinander'] == 0, info
        print(f'  STUFEN {self.thema}: neu {bericht["neu"]}, Knobel {bericht["bonus"]}, umgestuft {bericht["umgestuft"]}, überzählig {len(bericht["ueberzaehlig"])}; '
              f'strenge Prüfung ohne Überzählige OK')
        Path(f'/tmp/stufen_{self.thema}.json').write_text(json.dumps(bericht, ensure_ascii=False, indent=1))
        return d

    def _ordne(self, xs):
        """Keine zwei gleichen Typen und keine zwei gleich gebauten Übungen direkt hintereinander (gierig, größter Rest zuerst)."""
        rest = list(xs)
        reihe = []
        while rest:
            vor = reihe[-1] if reihe else None
            zahl = collections.Counter(a['g'] for a in rest)
            def gut(a):
                return vor is None or (a['g'] != vor['g'] and IP.bauplan(a) != IP.bauplan(vor))
            kand = [a for a in rest if gut(a)] or [a for a in rest if vor is None or a['g'] != vor['g']] or rest
            kand.sort(key=lambda a: -zahl[a['g']])
            a = kand[0]
            reihe.append(a)
            rest.remove(a)
        return reihe

    def _einstreuen(self, reihe, a):
        b = IP.bauplan(a)
        bp = [IP.bauplan(x) for x in reihe]
        for erlaubt in (1, 2):      # erst ohne gleich gebauten Nachbarn, sonst höchstens zwei gleich gebaute in Folge (Gruppe erst ab 3)
            for k in range(len(reihe) + 1):
                links = 0
                while k - 1 - links >= 0 and bp[k - 1 - links] == b: links += 1
                rechts = 0
                while k + rechts < len(bp) and bp[k + rechts] == b: rechts += 1
                if links + rechts + 1 <= erlaubt:
                    reihe.insert(k, a)
                    return
        raise AssertionError(f'{self.thema}: kein Platz für überzählige Übung „{a["f"]["text"][:60]}“')


# ---------- Nachweis ----------
def _k(x): return json.dumps(x, ensure_ascii=False, sort_keys=True)


def nachweis(thema, stand='origin/lernen-app'):
    alt = json.loads(subprocess.run(['git', 'show', f'{stand}:inhalte/themen/{thema}.json'], capture_output=True, text=True, check=True,
                                    cwd=HIER.parent.parent).stdout)
    neu = json.loads((THEMEN / f'{thema}.json').read_text(encoding='utf-8'))
    ohne = {k: v for k, v in alt.items() if k != 'aufgaben'}
    assert _k(ohne) == _k({k: v for k, v in neu.items() if k != 'aufgaben'}), 'außer den Aufgaben hat sich etwas geändert'
    def kern(a): return _k({k: v for k, v in a.items() if k not in ('g', 's')})
    pool = collections.Counter(kern(a) for a in neu['aufgaben'])
    z = collections.Counter()
    for a in alt['aufgaben']:
        k = kern(a)
        assert pool[k] > 0, f'alte Aufgabe fehlt oder verändert: {a["f"]["text"][:70]}'
        pool[k] -= 1
    alt_k = collections.Counter(kern(a) for a in alt['aufgaben'])
    for a in neu['aufgaben']:
        k = kern(a)
        if alt_k[k] > 0:
            alt_k[k] -= 1
            z['alt'] += 1
        else:
            assert a.get('g') and a['p'] in ('uebung', 'bonus'), f'neue Aufgabe ohne Typ: {a["f"]["text"][:60]}'
            z['neu ' + a['p']] += 1
    st = collections.Counter()
    altmap = collections.defaultdict(list)
    for a in alt['aufgaben']: altmap[kern(a)].append(a['s'])
    for a in neu['aufgaben']:
        if altmap.get(kern(a)):
            s0 = altmap[kern(a)].pop(0)
            if s0 != a['s']: st['umgestuft'] += 1
            if a.get('g'): st['mit g'] += 1
            elif a['p'] == 'uebung': st['überzählig (ohne g)'] += 1
    print(f'{thema}: alt {len(alt["aufgaben"])}, neu {len(neu["aufgaben"])}; ' + ', '.join(f'{k} {v}' for k, v in {**z, **st}.items()))
    print('NACHWEIS OK')


if __name__ == '__main__':
    nachweis(sys.argv[1])
