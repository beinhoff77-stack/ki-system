"""Zehnte Runde (Zweig schwer-kl5): schwerere Übungen nach Prüfungsvorbild für die Themen der Klasse 5.

Jeder Themen-Generator ruft am Ende ergaenze(DATEI, NEU, start) auf. Die neuen Aufgaben werden HINTER alle
bisherigen Aufgaben gehängt und benutzen einen eigenen Zufallsstart (nur zum Mischen der Antworten).
Dadurch bleiben alle bisherigen Aufgaben (Stand lernen-app) unverändert. Nachweis: _schwer_kl5_nachweis.py.

Lösungen werden hier berechnet: Z() rechnet o.wert aus dem Rechenausdruck c, L() die Lückenwerte aus der Liste c,
A() bekommt die richtige Antwort aus einer Rechnung oder einer Prüffunktion im Themen-Generator.
"""
import ast
import json
import operator
import random
from fractions import Fraction

_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv, ast.Mod: operator.mod}


def rechne(ausdruck):
    """Exakt rechnen wie tools/inhalt_pruefen.py (Fraction)."""
    def ev(n):
        if isinstance(n, ast.Expression): return ev(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return Fraction(str(n.value)) if isinstance(n.value, float) else Fraction(n.value)
        if isinstance(n, ast.BinOp) and type(n.op) in _OPS: return _OPS[type(n.op)](ev(n.left), ev(n.right))
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Pow): return ev(n.left) ** int(ev(n.right))
        if isinstance(n, ast.UnaryOp): return -ev(n.operand) if isinstance(n.op, ast.USub) else ev(n.operand)
        if isinstance(n, ast.Call) and n.func.id in ('abs', 'min', 'max'):
            return {'abs': abs, 'min': min, 'max': max}[n.func.id](*[ev(a) for a in n.args])
        raise ValueError(ast.dump(n))
    return ev(ast.parse(str(ausdruck), mode='eval'))


def zahl(fr):
    """Fraction -> int oder endliche Dezimalzahl (sonst Fehler)."""
    if fr.denominator == 1: return int(fr)
    d = fr.denominator
    for p in (2, 5):
        while d % p == 0: d //= p
    assert d == 1, f'kein endlicher Dezimalbruch: {fr}'
    return float(fr)


def de(x):
    """Zahl deutsch: −, Leerzeichen als Tausendertrenner, Dezimalkomma."""
    if isinstance(x, Fraction): x = zahl(x)
    if isinstance(x, float) and x.is_integer(): x = int(x)
    if isinstance(x, int):
        s = f'{abs(x):,}'.replace(',', ' ') if abs(x) >= 1000 else str(abs(x))
    else:
        s = repr(abs(x)).replace('.', ',')
    return ('−' if x < 0 else '') + s


def Z(s, text, c, w, h, einheit=None, grafik=None, toleranz=None):
    o = {'wert': zahl(rechne(c))}
    if einheit: o['einheit'] = einheit
    if toleranz: o['toleranz'] = toleranz
    f = {'text': text}
    if grafik: f['grafik'] = grafik
    return {'s': s, 'y': 'zahl', 'f': f, 'o': o, 'c': c, 'w': w, 'h': h}


def A(s, text, richtig, falsche, w, h, grafik=None):
    f = {'text': text}
    if grafik: f['grafik'] = grafik
    opts = [richtig] + list(falsche)
    assert 3 <= len(opts) <= 4 and len(set(opts)) == len(opts), opts
    return {'s': s, 'y': 'auswahl', 'f': f, '_richtig': richtig, '_opts': opts, 'w': w, 'h': h}


def wahl(s, text, optionen, ist_richtig, w, h, grafik=None):
    """Auswahl, bei der das Programm die richtige Antwort bestimmt: ist_richtig(option) muss für genau eine Option wahr sein."""
    r = [o for o in optionen if ist_richtig(o)]
    assert len(r) == 1, (text, r)
    return A(s, text, r[0], [o for o in optionen if o != r[0]], w, h, grafik)


def L(s, text, schablone, hinweis, c, w, h, grafik=None):
    f = {'text': text, 'schablone': schablone, 'hinweis': hinweis}
    if grafik: f['grafik'] = grafik
    werte = [zahl(rechne(x)) for x in c]
    assert all(isinstance(v, int) for v in werte), werte
    return {'s': s, 'y': 'luecken', 'f': f, 'o': {'werte': werte}, 'c': list(c), 'w': w, 'h': h}


def einzig(werte):
    """Genau eine Lösung (z. B. aus einer Suche über alle Kandidaten) – sonst Fehler."""
    w = sorted(set(werte))
    assert len(w) == 1, w
    return w[0]


def _schluessel(a):
    f = a['f']
    return (str(f.get('text', '')).strip() + '|' + json.dumps(a.get('a'), ensure_ascii=False) + '|'
            + json.dumps(f.get('schablone'), ensure_ascii=False) + '|' + json.dumps(f.get('grafik'), sort_keys=True))


def ergaenze(datei, neu, start, mindest=6):
    """neu: {lernziel: [Aufgaben aus Z/A/L/wahl]}. Hängt sie als Übungen an datei['aufgaben'] an."""
    R = random.Random(start)
    et = datei['inhalt']['etappen']
    lz_liste = [e['lernziel'] for e in et]
    assert set(neu) == set(lz_liste), (set(lz_liste) ^ set(neu))
    alt = datei['aufgaben']
    teil = {}
    for a in alt: teil.setdefault(a['l'], a['t'])
    gesehen = {_schluessel(a) for a in alt}
    beispiele = {(s['text'] if isinstance(s, dict) else s) for e in et for s in e['schritte']}
    dazu = []
    for lz in lz_liste:
        liste = neu[lz]
        st = [a['s'] for a in liste]
        assert len(liste) >= mindest and st.count(3) >= 4 and st.count(2) >= 2, (lz, st)
        for a in liste:
            a = dict(a)
            if a['y'] == 'auswahl':
                opts = list(a.pop('_opts')); r = a.pop('_richtig')
                R.shuffle(opts)
                a['a'] = opts; a['o'] = {'index': opts.index(r)}
            b = {'l': lz, 't': teil[lz], 'p': 'uebung', 's': a.pop('s')}
            b.update({k: a[k] for k in ('y', 'f', 'a', 'o', 'zahl', 'c', 'w', 'h') if k in a})
            k = _schluessel(b)
            assert k not in gesehen, f'Dublette: {b["f"]["text"]}'
            assert b['f']['text'] not in beispiele
            assert len(b['w']) >= 15 and b['h']
            gesehen.add(k)
            dazu.append(b)
    datei['aufgaben'] = alt + dazu
    return dazu


def M(s, text, start, ende, abschnitte, ziel, w, h, beschriftet='anfang_ende'):
    """Markierung auf dem Zahlenstrahl; der Index wird aus ziel berechnet."""
    schritt = Fraction(ende - start, abschnitte)
    idx = (Fraction(ziel) - start) / schritt
    assert idx.denominator == 1 and 0 <= idx <= abschnitte, idx
    g = {'typ': 'zahlenstrahl', 'start': start, 'ende': ende, 'abschnitte': abschnitte, 'beschriftet': beschriftet}
    return {'s': s, 'y': 'markierung', 'f': {'text': text, 'grafik': g}, 'o': {'index': int(idx)}, 'zahl': ziel, 'w': w, 'h': h}


def rw(term):
    """Wert eines deutsch geschriebenen Terms (·, :, −, eckige Klammern, Leerzeichen-Tausender) – zum Bestimmen der richtigen Auswahl."""
    t = term.replace('·', '*').replace(':', '/').replace('−', '-').replace('[', '(').replace(']', ')').replace(' ', '')
    import re
    t = re.sub(r'(?<=\d) (?=\d{3}\b)', '', t)
    return rechne(t)
