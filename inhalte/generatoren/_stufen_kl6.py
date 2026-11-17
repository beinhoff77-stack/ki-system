"""Zwanzigste Runde, Klasse 6 (Zweig stufen-kl6): echte Stufe 3 und Knobel-Bordkarten.

Jeder Generator der Klasse 6 ruft am Ende von __main__ stufen_datei(schluessel, ST) auf. Das liest die fertige Themendatei und
1. gibt jeder alten Übung ihren Typ g (Vorschlag nach Textmerkmalen, von Hand je Lernkarte geprüft; Abweichungen stehen als ST.typ(...) im Generator),
   bei Bedarf eine neue Stufe s (ST.typ(..., s=...)); Frage, Antworten und alle anderen Felder bleiben gleich;
2. markiert „überzählig“: mehr als 2 Übungen desselben Typs mit gleichem Satzbau je Stufe, auf Stufe 3 mehr als 3 je Typ – diese behalten KEIN g
   (der Haupt-Chat sperrt sie) und stehen in /tmp/stufen_<thema>.json;
3. hängt neue Übungen (ST.neu) und Knobel-Bordkarten (ST.knobel, Pool bonus) an die Lernkarte an;
4. ordnet die Übungen jeder Lernkarte neu (nur innerhalb ihrer bisherigen Plätze): Stufe 1, 2, 3, darin nie zwei gleiche Typen
   und nie zwei gleich gebaute Fragen direkt hintereinander.
Nachweis: _stufen_kl6_nachweis.py.
"""
import collections
import json
import random
import re
from pathlib import Path

from _befunde import _z, _l

THEMEN = Path(__file__).resolve().parent.parent / 'themen'
GEDANKEN = {1: ('direkt', 'erkennen'), 2: ('mehrschritt', 'einkleidung', 'umkehr', 'darstellung'),
            3: ('rueckwaerts', 'verknuepfen', 'begruenden', 'fehler', 'transfer', 'parameter', 'pruefung')}
STUFE_VON = {g: s for s, gs in GEDANKEN.items() for g in gs}
ZAHL = re.compile(r'[−-]?\d+(?:[  ]\d{3})*(?:[,.]\d+)?')


def bauplan(a):
    return re.sub(r'\s+', ' ', ZAHL.sub('#', str((a.get('f') or {}).get('text', '')))).strip()


SACH = re.compile(r'€|\bkg\b|\bkm\b|\bl\b|\bm\b|Kinder|Klasse|Kind |Preis|kostet|Konto|Bank|Umfrage|Rezept|Garten|Schule|Flasche|Pizza|Kuchen|'
                  r'Stunde|Minuten|Tag|Liter|Meter|Gramm|Bus|Rad|Besucher|Saft|Torte|Weg|Strecke|Spiel|Familie|Laden|Zimmer|Tank|Glas|Becher')


def vorschlag(a):
    """Typ-Vorschlag nach Textmerkmalen; wird je Lernkarte von Hand geprüft und mit ST.typ(...) korrigiert."""
    t = a['f']['text']; s = a['s']; y = a['y']; graf = 'grafik' in a['f']
    if s == 1:
        if y == 'auswahl' or graf or re.match(r'(Welche|Welcher|Welches|Wie heißt|Lies|Was ist|Ist |Stimmt|Wofür|Für welche)', t):
            return 'erkennen'
        return 'direkt'
    if s == 2:
        if graf: return 'darstellung'
        if re.search(r'Wie groß ist (n|k|e|a|der Exponent)|□|Welche Zahl (gehört|musst)|rückwärts|vorher|Wie viel (kostete|war)|am Anfang|fehlt|gesucht', t):
            return 'umkehr'
        if SACH.search(t) and len(t.split()) >= 10: return 'einkleidung'
        return 'mehrschritt'
    if re.search(r'Kind (rechnet|schreibt|gibt|sagt)|rechnet:|rechnet |Fehler|falsch\?|Was ist falsch|richtige Ergebnis|Wie heißt das richtige|Was stimmt', t):
        return 'fehler' if re.search(r'rechnet|schreibt|gibt .* an|Fehler|falsch', t) else 'begruenden'
    if re.search(r'Stimmt|stimmt|Ohne zu rechnen|größer oder kleiner|Welche Aussage|Kann das|Was kann man sagen|richtig\?|immer|widerlegt|Beispiel', t):
        return 'begruenden'
    if re.search(r'[Ff]ür welche|Für welchen|Wie viele (verschiedene|Paare)|möglich|ganzen Zahlen n|Welchen Exponenten', t):
        return 'parameter'
    if re.search(r'vorher|am Anfang|Wie hieß|ursprünglich|eingezahlt|kostete .* vorher|Wie viel Geld wurde|Wie lang', t):
        return 'rueckwaerts'
    return 'transfer'


class Stufen:
    def __init__(self, thema, seed):
        self.thema = thema
        self.R = random.Random(seed)
        self.korr = []      # (lz, text, g, s, enthaelt, anzahl)
        self.extra = []     # (lz, aufgabe)
        self.ueber_hand = []  # (lz, text, enthaelt)
        self.leitern = {}
        self.knobel_grund = {}

    # ---------- Bausteine (neue Aufgaben) ----------
    def Z(self, g, text, wert, c, w, h, **kw):
        a = _z(text, wert, c, w, h, **kw); a['g'] = g; return a

    def L(self, g, text, schablone, werte, c, w, h, **kw):
        a = _l(text, schablone, werte, c, w, h, **kw); a['g'] = g; return a

    def A(self, g, text, richtig, falsche, w, h, grafik=None):
        richtig = str(richtig)
        f = []
        for x in falsche:
            x = str(x)
            if x != richtig and x not in f: f.append(x)
        assert 2 <= len(f) <= 3, (text, f)
        opt = f[:]; self.R.shuffle(opt)
        i = self.R.randrange(len(opt) + 1); opt.insert(i, richtig)
        a = {'y': 'auswahl', 'f': {'text': text}, 'a': opt, 'o': {'index': i}, 'w': w, 'h': h, 'g': g}
        if grafik is not None: a['f']['grafik'] = grafik
        return a

    def M(self, g, text, start, ende, n, wert, w, h):
        from fractions import Fraction as Fr
        st, en, v = Fr(str(start)), Fr(str(ende)), Fr(str(wert))
        i = (v - st) / (en - st) * n
        assert i.denominator == 1 and 0 <= i <= n, (text, i)
        js = lambda x: int(x) if x.denominator == 1 else float(x)
        return {'y': 'markierung', 'f': {'text': text, 'grafik': {'typ': 'zahlenstrahl', 'start': js(st), 'ende': js(en), 'abschnitte': n, 'beschriftet': 'anfang_ende'}},
                'o': {'index': int(i)}, 'w': w, 'h': h, 'g': g}

    # ---------- Angaben je Lernkarte ----------
    def leiter(self, lz, s1, s2, s3):
        self.leitern[lz] = [s1, s2, s3]

    def typ(self, lz, text, g, s=None, enthaelt=None, anzahl=1):
        self.korr.append((lz, text, g, s, enthaelt, anzahl))

    def typ_bau(self, lz, s, anfang, g, neu_s=None):
        """alle alten Übungen der Stufe s, deren Fragetext mit anfang beginnt"""
        self.korr.append((lz, ('^', s, anfang), g, neu_s, None, None))

    def ueber(self, lz, text, enthaelt=None, anzahl=1):
        self.ueber_hand.append((lz, text, enthaelt, anzahl))

    def neu(self, lz, a):
        assert a['g'] in STUFE_VON, a['g']
        self.extra.append((lz, dict(a, p='uebung', s=STUFE_VON[a['g']])))

    def knobel(self, lz, a, grund=None):
        a = dict(a, p='bonus', s=3, g='knobel')
        assert a.get('h') and len(a.get('w', '')) >= 60, ('Knobel braucht Tipp und ausführlichen Weg', a['f']['text'])
        self.extra.append((lz, a))
        if grund: self.knobel_grund[lz] = grund

    # ---------- Anwenden ----------
    def anwenden(self, d):
        auf = d['aufgaben']
        lzs = [e['lernziel'] for e in d['inhalt']['etappen']]
        teil = {e['lernziel']: (e.get('teilfaehigkeit') or e['lernziel']) for e in d['inhalt']['etappen']}
        alt_t = {}
        for a in auf: alt_t.setdefault(a['l'], a['t'])
        bericht = {'thema': self.thema, 'leitern': self.leitern, 'vorher': {}, 'nachher': {}, 'ueberzaehlig': {}, 'neu': {}, 'knobel': {}, 'umgestuft': 0,
                   'knobel_grund': self.knobel_grund}
        for lz in lzs:
            ue = [a for a in auf if a['l'] == lz and a['p'] == 'uebung']
            bericht['vorher'][lz] = dict(collections.Counter(f"{a['s']}:{a.get('g', '-')}" for a in ue))
            for a in ue:
                if 'g' not in a: a['g'] = vorschlag(a)
        # Korrekturen von Hand
        for lz, text, g, s, enthaelt, anzahl in self.korr:
            if isinstance(text, tuple):
                _, st0, anf = text
                xs = [a for a in auf if a['l'] == lz and a['p'] == 'uebung' and a['s'] == st0 and a['f']['text'].startswith(anf)]
                assert xs, f'{self.thema}/{lz}: kein Treffer für Anfang „{anf}“ auf Stufe {st0}'
            else:
                xs = [a for a in auf if a['l'] == lz and a['p'] == 'uebung' and a['f']['text'] == text and (not enthaelt or enthaelt in json.dumps(a, ensure_ascii=False))]
                assert len(xs) == anzahl, f'{self.thema}/{lz}: {len(xs)} Treffer statt {anzahl} für „{text}“'
            for a in xs:
                if s is not None:
                    assert a['s'] != s, (lz, text, 'Stufe schon', s)
                    a['s'] = s; bericht['umgestuft'] += 1
                assert g is None or STUFE_VON[g] == a['s'], (lz, text, g, a['s'])
                if g is None: a['_ueber'] = True
                else: a['g'] = g
        for lz, text, enthaelt, anzahl in self.ueber_hand:
            xs = [a for a in auf if a['l'] == lz and a['p'] == 'uebung' and a['f']['text'] == text and (not enthaelt or enthaelt in json.dumps(a, ensure_ascii=False))]
            assert len(xs) == anzahl, f'{self.thema}/{lz}: {len(xs)} Treffer statt {anzahl} für „{text}“ (überzählig)'
            for a in xs: a['_ueber'] = True
        for a in auf:
            if a['p'] == 'uebung' and a['l'] in lzs and not a.get('_ueber'):
                assert STUFE_VON[a['g']] == a['s'], (a['l'], a['f']['text'], a['g'], a['s'])
        # neue Aufgaben einfügen (hinter der letzten Aufgabe der Lernkarte)
        texte = {a['f']['text'] for a in auf}
        for lz, a in self.extra:
            assert a['f']['text'] not in texte, ('doppelt', a['f']['text'])
            texte.add(a['f']['text'])
            a = {'l': lz, 't': alt_t[lz], **a}
            a = {k: a[k] for k in ('l', 't', 'p', 's', 'g', 'y', 'f', 'a', 'o', 'c', 'w', 'h') if k in a}
            letzte = max(i for i, x in enumerate(auf) if x['l'] == lz)
            auf.insert(letzte + 1, a)
            bericht['knobel' if a['p'] == 'bonus' else 'neu'].setdefault(lz, []).append(a['f']['text'])
        # überzählig: > 2 gleich gebaute desselben Typs je Stufe; Stufe 3: > 3 je Typ
        for lz in lzs:
            ue = [a for a in auf if a['l'] == lz and a['p'] == 'uebung']
            grp = collections.defaultdict(list)
            for a in ue:
                if not a.get('_ueber'): grp[(a['s'], a['g'], bauplan(a))].append(a)
            for xs in grp.values():
                alte = [a for a in xs if '_neu' not in a]
                for a in xs[2:]: a['_ueber'] = True
            je3 = collections.defaultdict(list)
            for a in ue:
                if a['s'] == 3 and not a.get('_ueber'): je3[a['g']].append(a)
            for g, xs in je3.items():
                for a in xs[3:]: a['_ueber'] = True
            for a in ue:
                if a.get('_ueber'):
                    a.pop('g', None)
                    bericht['ueberzaehlig'].setdefault(lz, []).append(a['f']['text'])
            # neu ordnen innerhalb der bisherigen Plätze
            plaetze = [i for i, a in enumerate(auf) if a['l'] == lz and a['p'] == 'uebung']
            ue = [auf[i] for i in plaetze]
            neu = self._ordne(ue)
            for i, a in zip(plaetze, neu): auf[i] = a
            bericht['nachher'][lz] = dict(collections.Counter(f"{a['s']}:{a.get('g', '-')}" for a in neu))
        for a in auf: a.pop('_ueber', None)
        (Path('/tmp') / f'stufen_{self.thema}.json').write_text(json.dumps(bericht, ensure_ascii=False, indent=1))
        return d

    def _ordne(self, ue):
        """Eine Reihenfolge: möglichst Stufe 1, 2, 3; nie zwei gleiche Typen und möglichst nie zwei gleich gebaute Fragen nebeneinander,
        niemals drei gleich gebaute hintereinander (wenn es irgend geht)."""
        R = list(ue); out = []
        while R:
            zb = collections.Counter(bauplan(a) for a in R)
            def gtyp_ok(a):
                return not out or 'g' not in a or out[-1].get('g') != a['g']
            def streng(a):
                return gtyp_ok(a) and (not out or bauplan(out[-1]) != bauplan(a))
            def mittel(a):
                return gtyp_ok(a) and not (len(out) >= 2 and bauplan(out[-1]) == bauplan(a) == bauplan(out[-2]))
            # häufige Baupläne zuerst, sonst bleiben sie am Ende übrig
            kand = sorted(R, key=lambda a: (a['s'], -zb[bauplan(a)], 'g' not in a))
            min_s = kand[0]['s']
            top, m = zb.most_common(1)[0]
            if m > len(R) - m + 1:  # strenges Abwechseln geht nicht mehr: den häufigsten Bauplan paarweise setzen
                w = next((a for a in kand if bauplan(a) == top and mittel(a)), None)
                if w is not None:
                    R.remove(w); out.append(w); continue
            wahl = (next((a for a in kand if a['s'] == min_s and streng(a)), None) or next((a for a in kand if streng(a)), None)
                    or next((a for a in kand if mittel(a)), None) or kand[0])
            R.remove(wahl); out.append(wahl)
        return out


def stufen_datei(schluessel, st):
    pfad = THEMEN / f'{schluessel}.json'
    roh = pfad.read_text(encoding='utf-8')
    d = st.anwenden(json.loads(roh))
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')
    print(f'  STUFEN {schluessel}: neu {sum(len(v) for v in json.loads((Path("/tmp") / f"stufen_{schluessel}.json").read_text())["neu"].values())}')
    return d
