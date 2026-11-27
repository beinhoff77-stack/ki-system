#!/usr/bin/env python3
"""Prüft alle sechs Tafeln unter inhalte/mathe-profi/regeln-uebersicht/tafeln/ (formeln-flaechen, formeln-koerper, zahlen,
stellenwert, bruch-dezimal-prozent, figuren, zeichen-woerter) samt tafel.md.

Es wird nachgerechnet, nicht abgeschrieben: Alle Zahlen exakt mit Brüchen (kein Float; π als eigener Rechenwert), Einheiten mit
Größenprüfung (links und rechts dieselbe Größe), jede Gleichung in jedem Text (Spannen aus Zahlen, Einheiten und Rechenzeichen),
Quadrat-/Kubik-/Zweierpotenzen, Primzahlen per Sieb, Teilbarkeitsregeln gegen n % d, Bruch = Dezimal = Prozent (auch periodisch),
Rundung, Zahlwörter, römische Zahlen in beide Richtungen, Zinseszins, Winkel- und Dreiecksarten, das Haus der Vierecke aus
Koordinaten (Eigenschaften, Symmetrieachsen, wer Sonderfall von wem ist) und die Verweise (Kennungen, Klassenangaben, Belege)
gegen daten/regeln-universum.json und inhalte/themen/*.json.

Aufruf:  python3 -I inhalte/mathe-profi/regeln-uebersicht/tafeln/pruefen.py
Endet mit „OK“, sonst mit Fehlerliste und Exit-Code 1."""
import json, pathlib, re, sys, math
from fractions import Fraction as F
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 60
hier = pathlib.Path(__file__).resolve().parent
repo = hier.parents[3]
fehler = []
def f(msg): fehler.append(msg if len(msg) < 400 else msg[:400] + ' …')
Z = {}   # Zähler
def zaehle(k, n=1): Z[k] = Z.get(k, 0) + n

# ============================================================ Rechenwerte: Zahl mit π und Größe
PI = Decimal('3.14159265358979323846264338327950288419716939937510582097494')
class DimError(Exception): pass
class Nicht(Exception): pass   # nicht auswertbar (kein Fehler der Daten)
DIMN = 4  # Länge, Geld, Zeit, Masse
def dim_mul(a, b): return tuple(x + y for x, y in zip(a, b))
def dim_pow(a, n): return tuple(x * n for x in a)
NULLDIM = (0,) * DIMN
class Irr:
    """Wurzel aus einer Nichtquadratzahl: nur für Mengenaussagen (irrational)."""
    def __init__(self, text): self.text = text
class Q:
    __slots__ = ('p', 'd')
    def __init__(self, p, d=NULLDIM):
        self.p = {k: v for k, v in p.items() if v != 0}; self.d = tuple(d)
    @staticmethod
    def rat(x, d=NULLDIM): return Q({0: F(x)}, d)
    def rational(self): return all(k == 0 for k in self.p)
    def wert(self):
        assert self.rational(); return self.p.get(0, F(0))
    def approx(self): return sum((Decimal(v.numerator) / Decimal(v.denominator)) * PI ** k for k, v in self.p.items()) if self.p else Decimal(0)
    def _chk(self, o):
        if not isinstance(o, Q): raise Nicht('kein Rechenwert')
        if self.d != o.d: raise DimError('verschiedene Größen %s und %s' % (self.d, o.d))
    def __add__(self, o): self._chk(o); r = dict(self.p); [r.__setitem__(k, r.get(k, 0) + v) for k, v in o.p.items()]; return Q(r, self.d)
    def __sub__(self, o): self._chk(o); r = dict(self.p); [r.__setitem__(k, r.get(k, 0) - v) for k, v in o.p.items()]; return Q(r, self.d)
    def __neg__(self): return Q({k: -v for k, v in self.p.items()}, self.d)
    def __mul__(self, o):
        if not isinstance(o, Q): raise Nicht('kein Rechenwert')
        r = {}
        for k1, v1 in self.p.items():
            for k2, v2 in o.p.items(): r[k1 + k2] = r.get(k1 + k2, 0) + v1 * v2
        return Q(r, dim_mul(self.d, o.d))
    def __truediv__(self, o):
        if not isinstance(o, Q): raise Nicht('kein Rechenwert')
        if not o.rational(): raise Nicht('Division durch π-Wert')
        if o.wert() == 0: raise Nicht('Division durch 0')
        return Q({k: v / o.wert() for k, v in self.p.items()}, dim_mul(self.d, dim_pow(o.d, -1)))
    def __pow__(self, n):
        if isinstance(n, Q):
            if not n.rational() or n.d != NULLDIM or n.wert().denominator != 1: raise Nicht('Exponent')
            n = int(n.wert())
        r = Q.rat(1)
        for _ in range(abs(n)): r = r * self
        if n < 0: r = Q.rat(1) / r
        if n == 0: r = Q.rat(1)
        return r
    def gleich(self, o):
        self._chk(o); return self.p == o.p
    def ordnung(self, o):
        self._chk(o)
        if self.rational() and o.rational(): a, b = self.wert(), o.wert(); return (a > b) - (a < b)
        a, b = self.approx(), o.approx(); return (a > b) - (a < b)

UNIT = {  # Einheit -> (Größe, Faktor in der Grundeinheit)
    'km': ((1, 0, 0, 0), F(1000)), 'm': ((1, 0, 0, 0), F(1)), 'dm': ((1, 0, 0, 0), F(1, 10)), 'cm': ((1, 0, 0, 0), F(1, 100)), 'mm': ((1, 0, 0, 0), F(1, 1000)),
    'kg': ((0, 0, 0, 1), F(1)), 'g': ((0, 0, 0, 1), F(1, 1000)), 'mg': ((0, 0, 0, 1), F(1, 1000000)),
    'l': ((3, 0, 0, 0), F(1, 1000)), 'ml': ((3, 0, 0, 0), F(1, 1000000)), 'hl': ((3, 0, 0, 0), F(1, 10)),
    '€': ((0, 1, 0, 0), F(1)), 'ct': ((0, 1, 0, 0), F(1, 100)), '°': (NULLDIM, F(1)), '%': (NULLDIM, F(1, 100)),
}
SUPCH = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁻': '-'}
SUBCH = {'₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9'}
def sup_int(s): return int(''.join(SUPCH[c] for c in s))
def U(einheit, exp=1):
    d, fk = UNIT[einheit]
    return Q({0: fk ** exp}, dim_pow(d, exp))
def N(text): return Q.rat(F(text.replace(' ', '').replace(',', '.')))
def wurzel(x, n=2):
    if not isinstance(x, Q): raise Nicht('Wurzel')
    if not x.rational():
        raise Nicht('Wurzel aus π-Wert')
    if any(e % n for e in x.d): raise DimError('Wurzel aus ungerader Größenpotenz')
    w = x.wert()
    if w < 0: raise Nicht('Wurzel aus negativer Zahl')
    def wz(k):
        r = round(k ** (F(1, n))) if k >= 0 else None
        for c in (r - 1, r, r + 1):
            if c >= 0 and c ** n == k: return F(c)
        return None
    a, b = wz(w.numerator), wz(w.denominator)
    if a is None or b is None:
        if x.d != NULLDIM: raise Nicht('irrationale Wurzel mit Größe')
        return Irr('%d√%s' % (n, w))
    return Q({0: a / b}, tuple(e // n for e in x.d))
def kubikw(x): return wurzel(x, 3)
def abs_(x):
    if isinstance(x, Q):
        return x if x.ordnung(Q({}, x.d)) >= 0 else -x
    raise Nicht('Betrag')
PI_Q = Q({1: F(1)})

# ============================================================ Zerlegung in Zeichen
NUMRE = r'\d{1,3}(?: \d{3})+(?:,\d+)?(?!\d)|\d+(?:,\d+)?'
IDRE = r"[A-Za-zÄÖÜäöüßα-ωΑ-Ω][A-Za-z0-9ÄÖÜäöüßα-ωΑ-Ω₀-₉ₐ-ₜ']*"
UNITRE = r'(?<![A-Za-zÄÖÜäöüß])(?:km|dm|cm|mm|kg|mg|ml|hl|ct|m|g|l|€|°|%)(?![A-Za-zÄÖÜäöüß])'
REL = ['≈', '≠', '≤', '≥', '=', '<', '>']
def tokenize(s, vars_=()):
    """-> Liste (Art, Text). Arten: NUM SUP UNIT PI OP LP RP SQ BAR REL ID WORD P"""
    pat = []
    names = sorted(vars_, key=len, reverse=True)
    if names: pat.append(('ID', '|'.join(re.escape(n) for n in names)))
    pat += [('PER', r'\d+,\d*(?:\d\u0305)+'), ('NUM', NUMRE), ('SUP', r'[⁻]?[⁰¹²³⁴⁵⁶⁷⁸⁹]+|ⁿ'), ('REL', '|'.join(REL)), ('OP', r'[+−·/]|(?<=\s):'), ('LP', r'\('), ('RP', r'\)'),
            ('SQ', r'[√∛]'), ('BAR', r'\|'), ('UNIT', UNITRE), ('PI', 'π'), ('WORD', IDRE), ('SP', r'\s+'), ('P', r'.')]
    rx = re.compile('|'.join('(?P<%s>%s)' % (a, b) for a, b in pat), re.S)
    out = []
    for m in rx.finditer(s):
        k = m.lastgroup
        if k == 'SP': continue
        out.append((k, m.group()))
    return out

class Expr:
    """Baut aus Tokens einen Python-Ausdruck (nur eigene Funktionen) und wertet ihn aus."""
    def __init__(self, vars_=None): self.vars = vars_ or {}
def build(tokens, vars_):
    out = []; i = 0; bar_open = False; prev = None
    ATOM_END = ('NUM', 'PER', 'SUP', 'UNIT', 'PI', 'RP', 'ID', 'BARC')
    while i < len(tokens):
        k, t = tokens[i]
        if k == 'NUM':
            if prev in ATOM_END: out.append('*')
            blk = "N(%r)" % t
            if i + 1 < len(tokens) and tokens[i + 1][0] == 'SUP': i += 1; blk = '(%s**(%d))' % (blk, sup_int(tokens[i][1]))
            if i + 1 < len(tokens) and tokens[i + 1][0] == 'UNIT':
                i += 1; einh = tokens[i][1]; exp = 1
                if i + 1 < len(tokens) and tokens[i + 1][0] == 'SUP': i += 1; exp = sup_int(tokens[i][1])
                blk = '(%s*U(%r,%d))' % (blk, einh, exp)
            out.append(blk)
        elif k == 'PI':
            if prev in ATOM_END: out.append('*')
            out.append('PI_Q')
        elif k == 'ID':
            if prev in ATOM_END: out.append('*')
            out.append('V[%r]' % t)
        elif k == 'SUP':
            if prev not in ('NUM', 'RP', 'ID', 'PI', 'UNIT'): raise Nicht('Exponent ohne Basis')
            if prev == 'UNIT': raise Nicht('Exponent nach Einheit')
            out.append('**(V["n"])' if t == 'ⁿ' else '**(%d)' % sup_int(t))
        elif k == 'UNIT':
            if prev not in ('NUM', 'SUP', 'RP', 'PI', 'ID', 'BARC'): raise Nicht('Einheit ohne Zahl')
            exp = 1
            if i + 1 < len(tokens) and tokens[i + 1][0] == 'SUP': exp = sup_int(tokens[i + 1][1]); i += 1
            out.append('*U(%r,%d)' % (t, exp))
        elif k == 'OP':
            out.append({'−': '-', '·': '*', ':': '/', '+': '+', '/': '/'}[t])
        elif k == 'LP':
            if prev in ATOM_END: out.append('*')
            out.append('(')
        elif k == 'RP': out.append(')')
        elif k == 'SQ':
            if prev in ATOM_END: out.append('*')
            fn = 'wurzel' if t == '√' else 'kubikw'
            if i + 1 < len(tokens) and tokens[i + 1][0] == 'NUM':
                out.append('%s(N(%r))' % (fn, tokens[i + 1][1])); i += 1; prev = 'NUM'; i += 1; continue
            out.append(fn)
        elif k == 'BAR':
            if not bar_open:
                if prev in ATOM_END: out.append('*')
                out.append('abs_('); bar_open = True
            else: out.append(')'); bar_open = False; prev = 'BARC'; i += 1; continue
        elif k == 'PER': raise Nicht('periodische Zahl')
        else: raise Nicht('Zeichen %r' % t)
        prev = k; i += 1
    if bar_open: raise Nicht('Betragsstrich offen')
    return ''.join(out)
def auswerten(tokens, vars_=None):
    vars_ = vars_ or {}
    expr = build(tokens, vars_)
    try: return eval(expr, {'__builtins__': {}}, {'N': N, 'U': U, 'PI_Q': PI_Q, 'wurzel': wurzel, 'kubikw': kubikw, 'abs_': abs_, 'V': vars_})
    except (SyntaxError, TypeError, ZeroDivisionError, KeyError) as e: raise Nicht('Ausdruck: %s' % e)
def q_aus(text, vars_=None):
    toks = tokenize(text, vars_ or ())
    if not toks: raise Nicht('leer')
    return auswerten(toks, vars_)

def runde(x, stellen):
    q = Decimal(1).scaleb(-stellen)
    return x.quantize(q, rounding=ROUND_HALF_UP)

def pruefe_kette(teile_tok, quelle, vars_=None):
    """teile_tok: Liste von Token-Listen, getrennt durch Relationen rels. Rückgabe: True/False/None (nicht prüfbar)."""
    teile, rels = teile_tok
    werte = []
    for tk in teile:
        werte.append(auswerten(tk, vars_))
    ok = True
    for i, r in enumerate(rels):
        a, b = werte[i], werte[i + 1]
        if isinstance(a, Irr) or isinstance(b, Irr): raise Nicht('irrational')
        if r == '=': res = a.gleich(b)
        elif r == '≠': res = not a.gleich(b)
        elif r == '<': res = a.ordnung(b) < 0
        elif r == '>': res = a.ordnung(b) > 0
        elif r == '≤': res = a.ordnung(b) <= 0
        elif r == '≥': res = a.ordnung(b) >= 0
        elif r == '≈':
            tk = teile[i + 1]
            if not tk or tk[0][0] != 'NUM' or any(x[0] not in ('NUM', 'UNIT') for x in tk) or len(tk) > 2: raise Nicht('≈ ohne Dezimalzahl')
            lit = tk[0][1]
            if ',' not in lit: raise Nicht('Rundung auf ganze Stelle')
            dez = len(lit.split(',')[1])
            einh = N(lit) if len(tk) == 1 else N(lit) * U(tk[1][1])
            einheit_wert = einh.wert() / N(lit).wert()
            if a.d != einh.d: raise DimError('≈ zwischen verschiedenen Größen')
            links = a.approx() / Decimal(einheit_wert.numerator) * Decimal(einheit_wert.denominator)
            res = runde(links, dez) == Decimal(lit.replace(' ', '').replace(',', '.'))
        ok = ok and res
    return ok

def spannen(s):
    """Findet in einem Text alle Rechenspannen (Zahlen, Einheiten, Rechenzeichen) mit mindestens einer Relation und prüft sie."""
    toks = tokenize(s)
    ergebnisse = []
    cur = []
    def flush():
        nonlocal cur
        n0 = len(cur); toks_cur_head = list(cur)
        while cur and not (cur[0][0] in ('NUM', 'LP', 'SQ', 'BAR', 'PI') or (cur[0] == ('OP', '−'))): cur = cur[1:]
        verw = len(cur) != n0 and any(k in ('OP', 'REL', 'LP') for k, _ in toks_cur_head[:n0 - len(cur)])
        n1 = len(cur)
        while cur and cur[-1][0] in ('OP', 'REL', 'LP', 'SQ'): cur = cur[:-1]
        if len(cur) != n1: verw = True
        if cur and not verw and any(k == 'REL' for k, _ in cur): ergebnisse.append(cur)
        cur = []
    prevk = None
    for k, t in toks:
        gueltig = k in ('NUM', 'PER', 'SUP', 'REL', 'OP', 'LP', 'RP', 'SQ', 'BAR', 'PI', 'UNIT')
        if k == 'UNIT' and prevk not in ('NUM', 'SUP', 'RP', 'PI', 'UNIT'): gueltig = False
        if k == 'SUP' and prevk not in ('NUM', 'RP', 'UNIT', 'PI'): gueltig = False
        if k == 'OP' and t == ':' and not cur: gueltig = False
        if gueltig: cur.append((k, t))
        else: flush()
        prevk = k if gueltig else None
    flush()
    return ergebnisse

def spanne_pruefen(sp, quelle, stats):
    teile, rels, akt = [], [], []
    for k, t in sp:
        if k == 'REL': teile.append(akt); rels.append(t); akt = []
        else: akt.append((k, t))
    teile.append(akt)
    if any(not x for x in teile): stats['nicht'] += 1; return
    try: ok = pruefe_kette((teile, rels), quelle)
    except DimError as e: f('%s: Größenfehler in Rechnung „%s“: %s' % (quelle, ' '.join(t for _, t in sp), e)); return
    except Nicht: stats['nicht'] += 1; return
    stats['ok'] += 1
    if not ok: f('%s: Rechnung falsch: „%s“' % (quelle, ' '.join(t for _, t in sp)))

# ============================================================ Daten laden
def lade(n): return json.loads((hier / n / (n + '.json')).read_text(encoding='utf-8'))
NAMEN_T = ['formeln-flaechen', 'formeln-koerper', 'zahlen', 'stellenwert', 'bruch-dezimal-prozent', 'figuren', 'zeichen-woerter']
T = {n: lade(n) for n in NAMEN_T}
univ = json.loads((repo / 'daten/regeln-universum.json').read_text(encoding='utf-8'))
ids = {}
for r in univ['regeln']: ids[r['id']] = r['name']
for g in univ['gesetze']: ids[g['id']] = g['name']
for p in univ['planeten']:
    for i in p['ideen']: ids[i['id']] = i['kurz']
themen = {}
def thema(t):
    if t not in themen:
        p = repo / 'inhalte/themen' / (t + '.json')
        themen[t] = (json.loads(p.read_text(encoding='utf-8')), p.read_text(encoding='utf-8')) if p.exists() else None
    return themen[t]

def alle_texte(x, pfad=''):
    SKIP = {'kennung', 'thema', 'lernziel', 'stand', 'ohne_luecken', 'stichwoerter', 'schluessel', 'falsch'}
    if isinstance(x, str): yield pfad, x
    elif isinstance(x, list):
        for i, y in enumerate(x): yield from alle_texte(y, '%s[%d]' % (pfad, i))
    elif isinstance(x, dict):
        for k, y in x.items():
            if k in SKIP: continue
            yield from alle_texte(y, pfad + '/' + k)

# ============================================================ 1 Schreibweise und Rechnungen in allen Texten
stats = {'ok': 0, 'nicht': 0}
def schreibweise(q, pfad, t):
    if re.search(r'\d\.\d', t): f('%s: Dezimalpunkt statt Komma: %r' % (pfad, t))
    if re.search(r'(?<![\d,./+])\d{4,}(?!\d|-| wird)', t) and 'ohne_luecken' not in pfad: f('%s: Zahl ab 4 Stellen ohne Tausenderleerzeichen: %r' % (pfad, t))
    if re.search('[\u00a0\u202f\u2009\u2007\u2002\u2003]', t): f('%s: Sonderleerzeichen (Bestand nutzt gewöhnliches Leerzeichen)' % pfad)
    if re.search(r'\d\*|\* ?\d| x (?=\d)', t): f('%s: Malzeichen falsch (Bestand: ·): %r' % (pfad, t))
    if re.search(r'\d(?:km|m|cm|dm|mm|kg|g|mg|l|ml|€|ct)\b', t): f('%s: Einheit ohne Leerzeichen: %r' % (pfad, t))
for n, d in T.items():
    for pfad, t in alle_texte(d, n):
        schreibweise(n, pfad, t)
        for sp in spannen(t): spanne_pruefen(sp, pfad, stats)
    zaehle('einträge', len(d['eintraege']))

# ============================================================ 2 Verweise: Kennungen, Klassen, Belege, Stichwörter
for n, d in T.items():
    seen = set()
    for e in d['eintraege']:
        k = e['kennung']; q = '%s/%s' % (n, k)
        if k in seen: f('%s: Kennung doppelt' % q)
        seen.add(k)
        sw = e.get('stichwoerter')
        if not sw or not all(isinstance(s, str) and s.strip() for s in sw) or len(set(sw)) != len(sw): f('%s: stichwoerter fehlen, sind leer oder doppelt' % q)
        for r in e['regeln']:
            if r['kennung'] not in ids: f('%s: Kennung %s nicht in regeln-universum.json' % (q, r['kennung']))
            elif ids[r['kennung']] != r['name']: f('%s: Kennung %s heißt im Universum „%s“, hier „%s“' % (q, r['kennung'], ids[r['kennung']], r['name']))
            if not r.get('passt'): f('%s: Regel %s ohne Begründung (passt)' % (q, r['kennung']))
            zaehle('regel-verweise')
        if not e['regeln'] and not e.get('regeln_hinweis') and n not in ('zeichen-woerter', 'zahlen') and e.get('art') not in ('zeichen', 'fachwort', 'griechisch'):
            f('%s: keine regeln und kein regeln_hinweis' % q)
        a = e['ab_klasse']; tri = set()
        for b in a['beleg']:
            t = thema(b['thema'])
            if not t: f('%s: Thema %s fehlt im Bestand' % (q, b['thema'])); continue
            et = [x for x in t[0]['inhalt']['etappen'] if x['lernziel'] == b['lernziel']]
            if not et: f('%s: Lernziel %s nicht in %s' % (q, b['lernziel'], b['thema'])); continue
            if b['wort'] not in json.dumps(et[0], ensure_ascii=False): f('%s: Wort „%s“ steht nicht in %s/%s' % (q, b['wort'], b['thema'], b['lernziel']))
            kl = t[0]['klasse']; tri.add((kl.get('gym_by'), kl.get('rs_by'), kl.get('ib_myp')))
            zaehle('belege')
        if a['beleg']:
            if tri != {(a['gymnasium_by'], a['realschule_by'], a['ib_myp'])}: f('%s: ab_klasse %s passt nicht zu den Belegen %s' % (q, (a['gymnasium_by'], a['realschule_by'], a['ib_myp']), tri))
        else:
            if any(a[x] is not None for x in ('gymnasium_by', 'realschule_by', 'ib_myp')) or not e.get('ab_klasse_hinweis'): f('%s: ohne Beleg muss ab_klasse leer sein und ab_klasse_hinweis stehen' % q)
    if len(seen) != len(d['eintraege']): f('%s: Kennungen nicht eindeutig' % n)

# ============================================================ 3 Formeln (Flächen, Körper)
def sym_text(t): return t
def vars_fuer(groessen, extra=()):
    return {g['zeichen']: None for g in groessen}
def einheit_q(einheit): return q_aus('1 ' + einheit)
def formel_pruefen(n, e):
    q = '%s/%s' % (n, e['kennung'])
    zeichen = e['ergebnis']['zeichen']
    if not e['formel'].startswith(zeichen + ' = ') and not (e['formel'].startswith('Kₙ = ') and zeichen == 'K₂'):
        f('%s: Formel %r beginnt nicht mit dem Ergebnis %s' % (q, e['formel'], zeichen))
    gz = [g['zeichen'] for g in e['groessen']]
    if len(set(gz)) != len(gz): f('%s: Größen doppelt' % q)
    bsp = e['beispiel']
    unausw = 'Summe der' in e['formel']
    if not unausw:
        rhs = e['formel'].split(' = ', 1)[1]
        toks = tokenize(rhs, gz)
        ver = {t for k, t in toks if k == 'ID'}
        if ver != set(gz): f('%s: Größen der Formel %s ≠ beschriftete Größen %s' % (q, sorted(ver), sorted(gz)))
        if set(bsp['werte']) != set(gz): f('%s: Werte %s ≠ Größen %s' % (q, sorted(bsp['werte']), sorted(gz)))
        vars_ = {}
        for g, w in bsp['werte'].items():
            try:
                v = q_aus(w)
            except Nicht as ex: f('%s: Wert %r nicht lesbar: %s' % (q, w, ex)); continue
            art = next(x['art'] for x in e['groessen'] if x['zeichen'] == g)
            soll = {'Länge': (1, 0, 0, 0), 'Fläche': (2, 0, 0, 0), 'Volumen': (3, 0, 0, 0), 'Winkel': NULLDIM}[art]
            if v.d != soll: f('%s: Wert %s hat nicht die Größe %s' % (q, w, art))
            if art != 'Winkel' and ('cm' not in w): f('%s: Wert %s nicht in cm' % (q, w))
            vars_[g] = v
        try:
            erg = auswerten(toks, vars_)
        except (Nicht, DimError) as ex: f('%s: Formel nicht auswertbar: %s' % (q, ex)); return
        zaehle('formeln-ausgewertet')
    # Ergebnis
    exakt = bsp['ergebnis'].split(' ≈ ')[0]
    try:
        eq = q_aus(exakt)
    except Nicht as ex: f('%s: Ergebnis %r nicht lesbar: %s' % (q, exakt, ex)); return
    if not unausw:
        if erg.d != eq.d or not erg.gleich(eq): f('%s: Ergebnis der Formel ≠ %s' % (q, bsp['ergebnis']))
    art = e['ergebnis']['art']
    soll = {'Länge': (1, 0, 0, 0), 'Fläche': (2, 0, 0, 0), 'Volumen': (3, 0, 0, 0)}[art]
    if eq.d != soll: f('%s: Ergebnis %s ist keine %s' % (q, bsp['ergebnis'], art))
    ez = einheit_q(e['ergebnis']['einheit'])
    if ez.d != eq.d: f('%s: Einheit %s passt nicht zum Ergebnis' % (q, e['ergebnis']['einheit']))
    if not bsp['ergebnis'].endswith(e['ergebnis']['einheit']): f('%s: Ergebnis %r endet nicht auf die Einheit %s' % (q, bsp['ergebnis'], e['ergebnis']['einheit']))
    # Rechenweg
    r = bsp['rechnung']
    if not r.startswith(zeichen + ' = '): f('%s: Rechnung beginnt nicht mit %s = ' % (q, zeichen))
    rest = r.split(' = ', 1)[1]
    if not rest.endswith(bsp['ergebnis']): f('%s: Rechnung endet nicht mit dem Ergebnis %r' % (q, bsp['ergebnis']))
    zaehle('rechenwege')
    for sp in spannen(rest):
        pass
    if 'hilfsrechnung' in bsp and not bsp.get('hilfe'): f('%s: hilfsrechnung ohne hilfe' % q)
    if e['bedingung'] in ('', None): f('%s: bedingung fehlt' % q)
    for g in e['groessen']:
        if not g['beschriften']: f('%s: Größe %s ohne Beschriftungshinweis' % (q, g['zeichen']))
    if not e['zeichnung']: f('%s: zeichnung fehlt' % q)
UF = univ['formeln']
alle_f = []
for n in ('formeln-flaechen', 'formeln-koerper'):
    for e in T[n]['eintraege']:
        formel_pruefen(n, e); alle_f.append((n, e))
fuers = [e['fuer'] for _, e in alle_f]
if len(set(fuers)) != len(fuers): f('formeln: „fuer“ doppelt')
uni_hier = [(n, e) for n, e in alle_f if e['herkunft'] == 'universum']
if [e['fuer'] for _, e in uni_hier] != [u['fuer'] for u in UF]: f('formeln: Die 28 Universum-Formeln fehlen oder stehen in anderer Reihenfolge')
for (n, e), u in zip(uni_hier, UF):
    for k, nk in (('fuer', 'fuer'), ('formel', 'formel'), ('bedingung', 'bedingung'), ('ziel', 'ziel')):
        if e.get(k) != u[nk]: f('%s/%s: %s weicht vom Universum ab: %r ≠ %r' % (n, e['kennung'], k, e.get(k), u[nk]))
    if (n == 'formeln-flaechen') != (u['ziel'] in ('F2', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10')): f('%s/%s: liegt in der falschen Tafel' % (n, e['kennung']))
    if u['ziel'] not in ids: f('%s: ziel %s unbekannt' % (e['kennung'], u['ziel']))
zaehle('universum-formeln', len(uni_hier))
if sum(1 for _, e in alle_f if e['herkunft'] == 'ergaenzt') != len(alle_f) - 28: f('formeln: herkunft stimmt nicht')
# Kreuzproben: die Beispiele gehören zu echten Körpern
bei = {e['fuer']: e['beispiel']['werte'] for _, e in alle_f}
def zahl_cm(s): return q_aus(s).wert() * 100  # in cm als Zahl (Faktor 1/100 -> *100)
def cm(x): return q_aus(x).wert() * 100
pw = bei['Prisma – Volumen']; pm = bei['Prisma – Mantel']
if not (cm(pm['u'].replace('cm', 'cm')) == 2 * (3 + 4) and q_aus(pw['G']).wert() * 10000 == 3 * 4): f('Prisma: Beispiel passt nicht zum Quader 3 cm · 4 cm · 5 cm')
qo = 2 * (3 * 4 + 3 * 5 + 4 * 5)
po = q_aus(bei['Prisma – Oberfläche']['G']).wert() * 10000 * 2 + q_aus(bei['Prisma – Oberfläche']['M']).wert() * 10000
if po != qo: f('Prisma-Oberfläche %s ≠ Quader-Oberfläche %s' % (po, qo))
G36 = q_aus(bei['Pyramide – Volumen']['G']).wert() * 10000
if G36 != cm(bei['Pyramide – Mantel (Pyramidenmantel)']['a']) ** 2 or G36 != 36: f('Pyramide: Grundfläche passt nicht zu a')
if cm(bei['Pyramide mit quadratischer Grundfläche – Oberfläche']['a']) != 6 or cm(bei['Pyramide mit quadratischer Grundfläche – Oberfläche']['hₛ']) != 5: f('Pyramide: a/hₛ uneinheitlich')
if cm(bei['Pyramide – Mantel (Pyramidenmantel)']['hₛ']) ** 2 != cm(bei['Pyramide – Volumen']['h']) ** 2 + (cm(bei['Pyramide – Mantel (Pyramidenmantel)']['a']) / 2) ** 2: f('Pyramide: hₛ² ≠ h² + (a : 2)²')
if cm(bei['Kegel – Mantel (Kegelmantel)']['s']) ** 2 != cm(bei['Kegel – Volumen']['r']) ** 2 + cm(bei['Kegel – Volumen']['h']) ** 2: f('Kegel: s² ≠ r² + h²')
if bei['Kegel – Oberfläche']['s'] != bei['Kegel – Mantel (Kegelmantel)']['s'] or bei['Kegel – Oberfläche']['r'] != bei['Kegel – Volumen']['r']: f('Kegel: r/s uneinheitlich')
if q_aus(bei['Pyramide – Oberfläche']['G']).wert() * 10000 != 36 or q_aus(bei['Pyramide – Oberfläche']['M']).wert() * 10000 != 60: f('Pyramide-Oberfläche: G/M uneinheitlich')

# ============================================================ 4 Zahlen
def sup(n): return ''.join({v: k for k, v in SUPCH.items()}[c] for c in str(n))
def tz(n):
    s = str(n); o = []
    while len(s) > 3: o.insert(0, s[-3:]); s = s[:-3]
    o.insert(0, s); return ' '.join(o)
def ganz(s): return int(s.replace(' ', ''))
def primzahlen(n):
    s = [True] * (n + 1); s[0:2] = [False, False]
    for i in range(2, int(n ** .5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i): s[j] = False
    return [i for i, v in enumerate(s) if v]
def zahlen_pruefen():
    d = {e['kennung']: e for e in T['zahlen']['eintraege']}
    q = d['zz-01']['liste']
    if [x['n'] for x in q] != list(range(1, 21)) + [25]: f('Quadratzahlen: n ist nicht 1–20 und 25')
    for x in q:
        if x['quadrat'] != x['n'] ** 2 or x['text'] != '%d² = %s' % (x['n'], tz(x['n'] ** 2)): f('Quadratzahl falsch: %s' % x)
    tr = d['zz-01']['trick']
    if not (tr['zahl'] ** 2 == tr['quadrat']): f('Trick: Quadrat falsch')
    for z in range(1, 10):
        if (10 * z + 5) ** 2 != (100 * z * (z + 1) + 25): f('Trick für Endziffer 5 stimmt nicht (z = %d)' % z)
    if (tr['zahl'] // 10) * (tr['zahl'] // 10 + 1) != 12 or tr['quadrat'] != 1225: f('Trick-Beispiel 35² falsch')
    k = d['zz-02']['liste']
    if [x['n'] for x in k] != list(range(1, 11)): f('Kubikzahlen: n ist nicht 1–10')
    for x in k:
        if x['kubik'] != x['n'] ** 3 or x['text'] != '%d³ = %s' % (x['n'], tz(x['n'] ** 3)): f('Kubikzahl falsch: %s' % x)
    zw = d['zz-03']['liste']
    if [x['exponent'] for x in zw] != list(range(0, 11)): f('Zweierpotenzen: Exponenten')
    for x in zw:
        if x['wert'] != 2 ** x['exponent'] or x['text'] != '2%s = %s' % (sup(x['exponent']), tz(2 ** x['exponent'])): f('Zweierpotenz falsch: %s' % x)
        if x['exponent'] and x['wert'] != 2 * 2 ** (x['exponent'] - 1): f('Verdopplung falsch')
    NAME_GROSS = {0: 'Eins', 1: 'Zehn', 2: 'Hundert', 3: 'Tausend', 4: 'Zehntausend', 5: 'Hunderttausend', 6: 'Million', 7: 'Zehn Millionen', 8: 'Hundert Millionen', 9: 'Milliarde', 10: 'Zehn Milliarden', 11: 'Hundert Milliarden', 12: 'Billion'}
    zg = d['zz-04']['liste']
    if [x['exponent'] for x in zg] != list(range(0, 13)): f('Zehnerpotenzen: Exponenten')
    for x in zg:
        if ganz(x['zahl']) != 10 ** x['exponent'] or x['nullen'] != x['exponent'] or x['zahl'].count('0') != x['exponent'] or x['potenz'] != '10' + sup(x['exponent']): f('Zehnerpotenz falsch: %s' % x)
        if x['name'] != NAME_GROSS[x['exponent']]: f('Name der Zehnerpotenz falsch: %s' % x)
    NAME_KLEIN = {1: 'Zehntel', 2: 'Hundertstel', 3: 'Tausendstel', 4: 'Zehntausendstel', 5: 'Hunderttausendstel', 6: 'Millionstel'}
    for x in d['zz-05']['liste']:
        e = -x['exponent']
        if x['zahl'] != '0,' + '0' * (e - 1) + '1' or x['nachkommastellen'] != e or F(x['zahl'].replace(',', '.')) != F(1, 10 ** e) or x['name'] != NAME_KLEIN[e] or x['potenz'] != '10' + sup(-e): f('Kleine Zehnerpotenz falsch: %s' % x)
    # Primzahlen
    pr = d['zz-06']
    if pr['liste'] != primzahlen(100) or pr['anzahl'] != 25 or len(pr['liste']) != 25: f('Primzahlen bis 100 stimmen nicht mit dem Sieb überein')
    if [p for p in range(2, 101) if all(p % t for t in range(2, p))] != pr['liste']: f('Primzahlen: Probedivision widerspricht')
    for z in range(2, 101):
        if z not in pr['liste'] and not any(z % t == 0 for t in (2, 3, 5, 7)): f('Test mit 2, 3, 5, 7 reicht für %d nicht' % z)
    if 11 * 11 <= 100 or 7 * 7 > 100: f('Primzahl-Begründung: 7 · 7 und 11 · 11 passen nicht')
    for b in pr['beispiele']:
        if (b['zahl'] in pr['liste']) != b['prim']: f('Primzahl-Beispiel %s falsch' % b['zahl'])
    # Teilbarkeit
    def r2(n): return n % 2 == 0 and str(n)[-1] in '02468'
    REG = {2: lambda n: str(n)[-1] in '02468', 3: lambda n: sum(map(int, str(n))) % 3 == 0, 4: lambda n: int(str(n)[-2:]) % 4 == 0,
           5: lambda n: str(n)[-1] in '05', 6: lambda n: str(n)[-1] in '02468' and sum(map(int, str(n))) % 3 == 0, 8: lambda n: int(str(n)[-3:]) % 8 == 0,
           9: lambda n: sum(map(int, str(n))) % 9 == 0, 10: lambda n: str(n)[-1] == '0', 25: lambda n: str(n)[-2:] in ('00', '25', '50', '75')}
    gesehen = []
    for e in T['zahlen']['eintraege']:
        if e['art'] != 'teilbarkeit': continue
        t = e['teiler']; gesehen.append(t)
        for n in range(1, 30000):
            if REG[t](n) != (n % t == 0): f('Regel für %d falsch bei %d' % (t, n)); break
        for k, soll in (('ja', True), ('nein', False)):
            n = ganz(e[k]['zahl'])
            if (n % t == 0) != soll or REG[t](n) != soll: f('Teilbarkeit %d: Beispiel %s (%s) falsch' % (t, e[k]['zahl'], k))
            if e[k]['zahl'] not in e[k]['weg'] and False: pass
        zaehle('teilbarkeitsregeln')
    if gesehen != [2, 3, 4, 5, 6, 8, 9, 10, 25]: f('Teilbarkeit: Teiler %s statt 2, 3, 4, 5, 6, 8, 9, 10, 25' % gesehen)
    # Zusatzprobe zur Quersumme der Beispiele
    for e in T['zahlen']['eintraege']:
        if e.get('art') == 'teilbarkeit' and e['teiler'] in (3, 9, 6):
            for k in ('ja', 'nein'):
                n = ganz(e[k]['zahl']); qs = sum(map(int, str(n)))
                if ('Quersumme: ' in e[k]['weg']) and not re.search(r'= %d[;.]' % qs, e[k]['weg']): f('Quersumme von %d falsch angegeben' % n)
zahlen_pruefen()

# ============================================================ 5 Stellenwert
def zahlwort(n):
    EINS = ['null', 'ein', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun', 'zehn', 'elf', 'zwölf', 'dreizehn', 'vierzehn', 'fünfzehn', 'sechzehn', 'siebzehn', 'achtzehn', 'neunzehn']
    ZEHN = {2: 'zwanzig', 3: 'dreißig', 4: 'vierzig', 5: 'fünfzig', 6: 'sechzig', 7: 'siebzig', 8: 'achtzig', 9: 'neunzig'}
    def u100(x, schluss):
        if x < 20: return ('eins' if schluss and x == 1 else EINS[x])
        e, z = x % 10, x // 10
        return ZEHN[z] if e == 0 else EINS[e] + 'und' + ZEHN[z]
    def u1000(x, schluss):
        h, r = x // 100, x % 100; s = ''
        if h: s = ('ein' if h == 1 else EINS[h]) + 'hundert'
        if r or not h: s += u100(r, schluss)
        return s
    def u1e6(x, schluss):
        t, r = x // 1000, x % 1000; s = ''
        if t: s = u1000(t, False) + 'tausend'
        if r: s += u1000(r, schluss)
        return s
    assert 0 < n < 10 ** 15
    teile = []
    for gr, sing, plur in ((10 ** 12, 'Billion', 'Billionen'), (10 ** 9, 'Milliarde', 'Milliarden'), (10 ** 6, 'Million', 'Millionen')):
        c, n = divmod(n, gr)
        if c: teile.append('eine ' + sing if c == 1 else u1000(c, False) + ' ' + plur)
    if n: teile.append(u1e6(n, True))
    return ' '.join(teile)
def roemisch(n):
    s = ''
    for w, z in ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= w: s += z; n -= w
    return s
ROMRE = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
def aus_roemisch(s):
    if not s or not ROMRE.match(s): return None
    w = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}; t = 0
    for i, c in enumerate(s):
        t += -w[c] if i + 1 < len(s) and w[c] < w[s[i + 1]] else w[c]
    return t
def stellen_pruefen():
    d = {e['kennung']: e for e in T['stellenwert']['eintraege']}
    NG = {0: 'Einer', 1: 'Zehner', 2: 'Hunderter', 3: 'Tausender', 4: 'Zehntausender', 5: 'Hunderttausender', 6: 'Millionen', 7: 'Zehnmillionen', 8: 'Hundertmillionen', 9: 'Milliarden', 10: 'Zehnmilliarden', 11: 'Hundertmilliarden', 12: 'Billionen'}
    GN = {0: 'Einer', 1: 'Tausender', 2: 'Millionen', 3: 'Milliarden', 4: 'Billionen'}
    s = d['sw-01']['stellen']
    if [x['exponent'] for x in s] != list(range(13)): f('Stellenwerttafel: Exponenten')
    if len({x['kurz'] for x in s}) != 13: f('Stellenwerttafel: Kürzel doppelt')
    for x in s:
        if ganz(x['wert']) != 10 ** x['exponent'] or x['potenz'] != '10' + sup(x['exponent']) or x['name'] != NG[x['exponent']] or x['gruppe'] != GN[x['exponent'] // 3]: f('Stelle falsch: %s' % x)
    for sw_k in ('sw-01', 'sw-02'):
        b = d[sw_k]['beispiel']
        z = b['zahl'].replace(' ', '').replace(',', '.')
        summe = sum(F(x['ziffer']) * F(10) ** x['exponent'] for x in b['zerlegung'])
        if summe != F(z): f('%s: Zerlegung ergibt %s statt %s' % (sw_k, summe, b['zahl']))
        if [str(x['ziffer']) for x in b['zerlegung']] != [c for c in z if c != '.']: f('%s: Ziffern der Zerlegung stimmen nicht' % sw_k)
    if zahlwort(ganz(d['sw-01']['beispiel']['zahl'])) != d['sw-01']['beispiel']['wort']: f('sw-01: Zahlwort falsch: %s' % zahlwort(ganz(d['sw-01']['beispiel']['zahl'])))
    dz = d['sw-02']['stellen']
    NK = {-1: 'Zehntel', -2: 'Hundertstel', -3: 'Tausendstel', -4: 'Zehntausendstel', -5: 'Hunderttausendstel', -6: 'Millionstel'}
    if [x['exponent'] for x in dz] != [-1, -2, -3, -4, -5, -6]: f('Dezimalstellen: Exponenten')
    for x in dz:
        e = -x['exponent']
        if F(x['wert'].replace(',', '.')) != F(1, 10 ** e) or x['name'] != NK[x['exponent']] or x['potenz'] != '10' + sup(x['exponent']): f('Dezimalstelle falsch: %s' % x)
        nn = x['bruch'].split('/')
        if F(int(nn[0]), ganz(nn[1])) != F(1, 10 ** e): f('Bruch der Dezimalstelle falsch: %s' % x)
    if d['sw-02']['beispiel']['lesen'] != 'drei Komma vier sieben zwei': f('Lesen von 3,472 falsch')
    # Dreiergruppen
    for b in d['sw-03']['beispiele']:
        n = int(b['ohne_luecken'])
        if tz(n) != b['zahl']: f('Dreiergruppen falsch: %s' % b['zahl'])
        if zahlwort(n) != b['wort']: f('Zahlwort falsch: %s = %r, richtig %r' % (b['zahl'], b['wort'], zahlwort(n)))
    # Runden
    def rund(x, e):  # auf 10^e, kaufmännisch
        q = F(10) ** e
        return (F(x) / q + F(1, 2)).__floor__() * q
    for k in ('sw-04', 'sw-05'):
        for b in d[k]['beispiele']:
            x = F(b['zahl'].replace(' ', '').replace(',', '.'))
            soll = rund(x, b['exponent'])
            if soll != F(b['ergebnis'].replace(' ', '').replace(',', '.')): f('Runden %s auf %s: %s statt %s' % (b['zahl'], b['stelle'], b['ergebnis'], soll))
            nm = {2: 'Hunderter', 3: 'Tausender', -1: 'Zehntel', -2: 'Hundertstel'}[b['exponent']]
            if nm != b['stelle']: f('Rundungsstelle falsch benannt: %s' % b)
            if b['ergebnis'].count(',') and len(b['ergebnis'].split(',')[1]) != -b['exponent']: f('Nachkommastellen des Ergebnisses falsch: %s' % b)
            ziffer = int((abs(x) / F(10) ** (b['exponent'] - 1)).__floor__() % 10)
            if not re.search(r'die %d' % ziffer, b['grund']) and not (ziffer == 5 and 'genau die 5' in b['grund']): f('Rundung: Ziffer rechts daneben ist %d, Text: %s' % (ziffer, b['grund']))
            if (ziffer >= 5) != ('aufrunden' in b['grund'] or 'Aufgerundet' in b['grund'] or 'aufgerundet' in b['grund'] or 'Ab 5' in b['grund']): f('Rundung: Richtung falsch begründet: %s' % b)
            zaehle('rundungen')
    # Römische Zahlen
    r = d['sw-06']
    if [(x['zeichen'], ganz(x['wert'])) for x in r['zeichen']] != [('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)]: f('Römische Zeichen falsch')
    if {(a['paar'], a['wert']) for a in r['abzuege']} != {('IV', 4), ('IX', 9), ('XL', 40), ('XC', 90), ('CD', 400), ('CM', 900)}: f('Römische Abzüge falsch')
    for a in r['abzuege']:
        if aus_roemisch(a['paar']) != a['wert'] or roemisch(a['wert']) != a['paar']: f('Abzugspaar %s falsch' % a['paar'])
    # Es dürfen genau diese Paare als Abzug vorkommen: alle anderen „kleiner vor größer“-Paare sind ungültig
    erlaubt = {a['paar'] for a in r['abzuege']}
    for a in 'IVXLCDM':
        for b2 in 'IVXLCDM':
            wa, wb = 'IVXLCDM'.index(a), 'IVXLCDM'.index(b2)
            if wa < wb and (a + b2 in erlaubt) != (aus_roemisch(a + b2) is not None): f('Paar %s: Regel und Gültigkeit widersprechen sich' % (a + b2))
    for n in range(1, 4000):
        s2 = roemisch(n)
        if aus_roemisch(s2) != n: f('Römisch %d ↔ %s' % (n, s2)); break
    if roemisch(3999) != 'MMMCMXCIX': f('Größte römische Zahl falsch')
    if len(r['beispiele']) < 6: f('Römische Zahlen: weniger als 6 Beispiele')
    for b in r['beispiele']:
        n = ganz(b['zahl'])
        if aus_roemisch(b['roemisch']) != n or roemisch(n) != b['roemisch']: f('Römisches Beispiel %s = %s falsch' % (b['roemisch'], b['zahl']))
        if not b['rechnung'].startswith(b['roemisch'] + ' = '): f('Römisches Beispiel: Rechnung beginnt nicht mit %s' % b['roemisch'])
        zaehle('römische-beispiele')
    for b in r['falsch']:
        if aus_roemisch(b['falsch']) is not None: f('„falsch“ %s ist als römische Zahl gültig' % b['falsch'])
        if aus_roemisch(b['richtig']) != b['zahl'] or roemisch(b['zahl']) != b['richtig']: f('„richtig“ %s ist nicht %d' % (b['richtig'], b['zahl']))
    # Vorsilben
    PE = {'k': 3, 'h': 2, 'da': 1, 'd': -1, 'c': -2, 'm': -3, 'M': 6, 'G': 9, 'µ': -6, 'n': -9}
    NE = {'Kilo': 'k', 'Hekto': 'h', 'Deka': 'da', 'Dezi': 'd', 'Zenti': 'c', 'Milli': 'm', 'Mega': 'M', 'Giga': 'G', 'Mikro': 'µ', 'Nano': 'n'}
    ZW = {3: 'Tausend', 2: 'Hundert', 1: 'Zehn', -1: 'Zehntel', -2: 'Hundertstel', -3: 'Tausendstel', 6: 'Million', 9: 'Milliarde', -6: 'Millionstel', -9: 'Milliardstel'}
    gefunden = []
    for e in T['stellenwert']['eintraege']:
        if e['art'] != 'vorsilbe': continue
        k = e['kurz']; gefunden.append(e['vorsilbe'])
        if NE[e['vorsilbe']] != k or PE[k] != e['exponent']: f('Vorsilbe %s: Kürzel oder Exponent falsch' % e['vorsilbe'])
        if e['potenz'] != '10' + sup(e['exponent']): f('Vorsilbe %s: Potenz' % e['vorsilbe'])
        fk = F(10) ** e['exponent']
        if F(e['faktor'].replace(' ', '').replace(',', '.')) != fk: f('Vorsilbe %s: Faktor %s ≠ 10^%d' % (e['vorsilbe'], e['faktor'], e['exponent']))
        if e['bedeutet'] != ZW[e['exponent']]: f('Vorsilbe %s: bedeutet %s' % (e['vorsilbe'], e['bedeutet']))
        b = e['beispiel']
        if b['einheit'] != k + b['basis'] and not (k == 'da' and b['einheit'] == 'dag'): f('Vorsilbe %s: Einheit %s' % (e['vorsilbe'], b['einheit']))
        m = re.fullmatch(r'1 (\S+) = (\S+(?: \d{3})*) (\S+)', b['text'])
        if not m or m.group(1) != b['einheit'] or m.group(3) != b['basis'] or F(m.group(2).replace(' ', '').replace(',', '.')) != fk: f('Vorsilbe %s: Beispiel %r' % (e['vorsilbe'], b['text']))
        zaehle('vorsilben')
    if gefunden != ['Kilo', 'Hekto', 'Deka', 'Dezi', 'Zenti', 'Milli', 'Mega', 'Giga', 'Mikro', 'Nano']: f('Vorsilben: %s' % gefunden)
stellen_pruefen()

# ============================================================ 6 Bruch, Dezimal, Prozent
OL = '̅'
def dez_wert(g, vor, per):
    w = F(int(g))
    if vor: w += F(int(vor), 10 ** len(vor))
    if per: w += F(int(per), (10 ** len(per) - 1)) / 10 ** len(vor)
    return w
def dez_text(g, vor, per, suffix=''):
    s = g
    if vor or per: s += ',' + vor + ''.join(c + OL for c in per)
    return s + suffix
def bdp_pruefen():
    d = {e['kennung']: e for e in T['bruch-dezimal-prozent']['eintraege']}
    soll = ['1/2', '1/3', '2/3', '1/4', '3/4', '1/5', '2/5', '3/5', '4/5', '1/8', '3/8', '5/8', '7/8', '1/10', '1/20', '1/25', '1/50', '1/100']
    zl = d['bd-01']['zeilen']
    if [z['bruch'] for z in zl] != soll: f('Bruchtabelle: Zeilen %s' % [z['bruch'] for z in zl])
    for z in zl:
        br = F(z['zaehler'], z['nenner'])
        if z['bruch'] != '%d/%d' % (z['zaehler'], z['nenner']): f('Bruch falsch geschrieben: %s' % z)
        for k, mal, suf in (('dezimal', 1, ''), ('prozent', 100, ' %')):
            x = z[k]
            if dez_wert(x['ganz'], x['vor'], x['periode']) != br * mal: f('%s: %s ist nicht %s (exakt)' % (z['bruch'], k, br * mal))
            if x['text'] != dez_text(x['ganz'], x['vor'], x['periode'], suf): f('%s: Schreibung von %s: %r' % (z['bruch'], k, x['text']))
        # periodisch genau dann, wenn der gekürzte Nenner andere Primteiler als 2 und 5 hat
        n = br.denominator
        for p in (2, 5):
            while n % p == 0: n //= p
        if z['periodisch'] != (n != 1): f('%s: periodisch-Kennzeichnung falsch' % z['bruch'])
        if z['periodisch'] != bool(z['dezimal']['periode']) or z['periodisch'] != bool(z['prozent']['periode']): f('%s: Periode nicht gekennzeichnet' % z['bruch'])
        if z['periodisch'] and (z['dezimal']['periode'] != z['prozent']['periode']): f('%s: Perioden von Dezimal und Prozent' % z['bruch'])
        zaehle('bruchzeilen')
    # Grundaufgaben
    for k in ('bd-02', 'bd-03', 'bd-04', 'bd-05', 'bd-06'):
        e = d[k]; bsp = e['beispiel']
        names = [g['zeichen'] for g in e['groessen']]
        lhs, rhs = e['formel'].split(' = ', 1)
        ez = e['ergebnis']['zeichen']
        if not (lhs == ez or (lhs == 'Kₙ' and ez == 'K₂')): f('%s: Formel links %s ≠ Ergebnis %s' % (k, lhs, ez))
        vars_ = {}
        for g, w in bsp['werte'].items():
            try: vars_[g] = q_aus(w)
            except Nicht as ex: f('%s: Wert %r: %s' % (k, w, ex))
        if set(bsp['werte']) != set(names) - {ez} - ({'p %'} if k == 'bd-03' else set()) and not (k == 'bd-03' and set(bsp['werte']) == {'W', 'G'}) and not (k == 'bd-06' and set(bsp['werte']) == {'K₀', 'q', 'n'}):
            f('%s: Werte %s passen nicht zu den Größen %s' % (k, sorted(bsp['werte']), names))
        if 'n' in vars_: vars_['n'] = vars_['n']
        try:
            toks = tokenize(rhs, list(vars_))
            erg = auswerten(toks, vars_)
        except (Nicht, DimError) as ex: f('%s: Formel nicht auswertbar: %s' % (k, ex)); continue
        try: soll_e = q_aus(bsp['ergebnis'])
        except Nicht as ex: f('%s: Ergebnis: %s' % (k, ex)); continue
        if erg.d != soll_e.d or not erg.gleich(soll_e): f('%s: Formel ergibt etwas anderes als %s' % (k, bsp['ergebnis']))
        if not bsp['rechnung'].endswith(bsp['ergebnis']): f('%s: Rechnung endet nicht mit %s' % (k, bsp['ergebnis']))
        zaehle('prozent-formeln')
    # Zinseszins: Schritt für Schritt
    z = d['bd-06']['beispiel']
    k0 = q_aus('1 000 €').wert(); q_ = F(11, 10)
    if k0 * q_ != 1100 or k0 * q_ * q_ != 1210 or k0 * q_ ** 2 != 1210: f('Zinseszins: 1 000 € · 1,1 · 1,1 ≠ 1 210 €')
    if q_ != 1 + F(10, 100): f('Zinsfaktor q ≠ 1 + 10 : 100')
    if z['zinsen_gesamt'] != 'K₂ − K₀ = 1 210 € − 1 000 € = 210 €' or 1210 - 1000 != 210: f('Zinseszins: Gesamtzinsen')
    if 2 * 100 == 210: f('Zinseszins: Warnung sinnlos')
    # Zins 1 Jahr
    if F(1000) * 10 / 100 != 100 or 1000 + 100 != 1100: f('Zins ein Jahr: 1 000 € zu 10 % gibt 1 100 €')
    if '1 100 €' not in d['bd-05']['beispiel']['danach']: f('Zins ein Jahr: 1 100 € fehlt')
bdp_pruefen()

# ============================================================ 7 Figuren
def kreuz(a, b): return a[0] * b[1] - a[1] * b[0]
def punkt(a, b): return a[0] * b[0] + a[1] * b[1]
def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def l2(a): return a[0] * a[0] + a[1] * a[1]
def viereck_eig(P):
    P = [(F(x), F(y)) for x, y in P]; A, B, C, D = P
    S = [sub(B, A), sub(C, B), sub(D, C), sub(A, D)]
    vz = [kreuz(S[i], S[(i + 1) % 4]) for i in range(4)]
    konvex = all(v > 0 for v in vz) or all(v < 0 for v in vz)
    par = (kreuz(S[0], S[2]) == 0) + (kreuz(S[1], S[3]) == 0)
    L = [l2(s) for s in S]
    rechte = sum(punkt(S[i], S[(i + 1) % 4]) == 0 for i in range(4))
    AC, BD = sub(C, A), sub(D, B)
    mA, mB = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2), ((B[0] + D[0]) / 2, (B[1] + D[1]) / 2)
    def cosgl(i, j):  # Winkel an Ecke i und j gleich?
        def werte(c):
            v1 = sub(P[(c + 1) % 4], P[c]); v2 = sub(P[(c - 1) % 4], P[c]); return punkt(v1, v2), l2(v1) * l2(v2)
        da, na = werte(i); db, nb = werte(j)
        return (da >= 0) == (db >= 0) and da * da * nb == db * db * na
    def spiegel(P0, R):
        def refl(q):
            dd = l2(R); t = punkt(sub(q, P0), R) / dd
            fx = (P0[0] + R[0] * t, P0[1] + R[1] * t); return (2 * fx[0] - q[0], 2 * fx[1] - q[1])
        return refl
    achsen = []
    kand = [('diag', A, sub(C, A)), ('diag', B, sub(D, B))]
    for i in range(4):
        M = ((P[i][0] + P[(i + 1) % 4][0]) / 2, (P[i][1] + P[(i + 1) % 4][1]) / 2); s = S[i]
        kand.append(('mitte', M, (-s[1], s[0])))
    menge = set(P)
    ax = []
    for art, P0, R in kand:
        rf = spiegel(P0, R)
        if {rf(q) for q in P} == menge:
            if not any(kreuz(R, r2) == 0 and kreuz(sub(P0, p2), r2) == 0 for _, p2, r2 in [(a, b, c) for a, b, c in ax]): ax.append((art, P0, R))
    c = ((sum(p[0] for p in P) / 4), (sum(p[1] for p in P) / 4))
    punktsym = {(2 * c[0] - q[0], 2 * c[1] - q[1]) for q in P} == menge
    diag_ax = any(a[0] == 'diag' for a in ax)
    seitenmitte_ax = any(a[0] == 'mitte' for a in ax)
    nachbar = (L[0] == L[1] and L[2] == L[3]) or (L[1] == L[2] and L[3] == L[0])
    w = {'konvex': konvex, 'parallele_paare_mindestens': par, 'gegenseiten_gleich_lang': L[0] == L[2] and L[1] == L[3], 'alle_seiten_gleich_lang': len(set(L)) == 1,
         'nachbarseitenpaare_gleich_lang': nachbar, 'vier_rechte_winkel': rechte == 4, 'gegenueberliegende_winkel_gleich': cosgl(0, 2) and cosgl(1, 3),
         'diagonalen_gleich_lang': l2(AC) == l2(BD), 'diagonalen_senkrecht': punkt(AC, BD) == 0, 'diagonalen_halbieren_sich': mA == mB,
         'symmetrieachsen_mindestens': len(ax), 'punktsymmetrisch': punktsym}
    w['_klasse'] = {'Viereck': konvex, 'Trapez': par >= 1, 'Parallelogramm': par == 2, 'Rechteck': rechte == 4, 'Raute': w['alle_seiten_gleich_lang'],
                    'Quadrat': rechte == 4 and w['alle_seiten_gleich_lang'], 'Drachenviereck': nachbar and diag_ax, 'gleichschenkliges Trapez': seitenmitte_ax}
    # Winkelsumme 360° (Innenwinkel aus den Dreiecken ABC, ACD)
    return w
KLASSE_VON = {'quadrat': 'Quadrat', 'rechteck': 'Rechteck', 'raute': 'Raute', 'parallelogramm': 'Parallelogramm', 'trapez': 'Trapez', 'gl_trapez': 'gleichschenkliges Trapez', 'drachen': 'Drachenviereck', 'allgemein': 'Viereck'}
def figuren_pruefen():
    d = {e['kennung']: e for e in T['figuren']['eintraege']}
    E = T['figuren']['eintraege']
    # --- Winkelarten
    W = [e for e in E if e['art'] == 'winkelart']
    if [(w['von'], w['bis']) for w in W] != [(0, 90), (90, 90), (90, 180), (180, 180), (180, 360), (360, 360)]: f('Winkelarten: Grenzen')
    def klass(a):
        for w in W:
            if w['von'] == w['bis']:
                if a == w['von']: return w['name']
            elif w['von'] < a < w['bis']: return w['name']
    for i, w in enumerate(W):
        if klass(w['beispiel_winkel']) != w['name']: f('Winkelart %s: Beispiel %d° gehört zu %s' % (w['name'], w['beispiel_winkel'], klass(w['beispiel_winkel'])))
        if w['von'] == w['bis']: erw = 'α = %d°' % w['von']
        else: erw = '%d° < α < %d°' % (w['von'], w['bis'])
        if w['bereich'] != erw: f('Winkelart %s: Bereich %r ≠ %r' % (w['name'], w['bereich'], erw))
        if w['von'] != w['bis'] and (w['von_eingeschlossen'] or w['bis_eingeschlossen']): f('Winkelart %s: offenes Intervall' % w['name'])
        if w['von'] == w['bis'] and not (w['von_eingeschlossen'] and w['bis_eingeschlossen']): f('Winkelart %s: Einzelwert' % w['name'])
        if i and W[i - 1]['bis'] != w['von']: f('Winkelarten: Lücke zwischen %s und %s' % (W[i - 1]['name'], w['name']))
    for a in range(1, 361):
        if klass(a) is None: f('Winkel %d° gehört zu keiner Art' % a); break
    # --- Winkelsumme
    ws = d['fg-07']['beispiel']
    if 180 - ws['werte']['α'] - ws['werte']['β'] != ws['ergebnis'] or ws['werte']['α'] + ws['werte']['β'] + ws['ergebnis'] != 180: f('Winkelsumme: Beispiel')
    # --- Dreiecke
    def seitenart(s):
        a, b, c = sorted(s)
        if a + b <= c: return None
        return 'gleichseitig' if a == c else 'gleichschenklig' if (a == b or b == c) else 'allgemein'
    def winkelart(w):
        if sum(w) != 180 or min(w) <= 0: return None
        return 'rechtwinklig' if 90 in w else 'stumpfwinklig' if max(w) > 90 else 'spitzwinklig'
    ZUORD = {'fg-08': ('seiten', 'allgemein'), 'fg-09': ('seiten', 'gleichschenklig'), 'fg-10': ('seiten', 'gleichseitig'), 'fg-11': ('winkel', 'spitzwinklig'), 'fg-12': ('winkel', 'rechtwinklig'), 'fg-13': ('winkel', 'stumpfwinklig')}
    for k, (nach, art) in ZUORD.items():
        e = d[k]
        if e['nach'] != nach: f('%s: nach' % k)
        for b in e['beispiele']:
            if 'seiten' in b:
                sa = seitenart(b['seiten'])
                if sa is None: f('%s: Seiten %s bilden kein Dreieck' % (k, b['seiten']))
                if nach == 'seiten':
                    if sa != art and not (art == 'gleichschenklig' and sa == 'gleichseitig'): f('%s: Seiten %s sind %s' % (k, b['seiten'], sa))
                    if art == 'gleichschenklig' and sa != 'gleichschenklig': f('%s: Beispiel muss echt gleichschenklig sein' % k)
                if b.get('pythagoras'):
                    x, y, zz = sorted(b['seiten'])
                    if x * x + y * y != zz * zz: f('%s: Seiten %s sind nicht rechtwinklig' % (k, b['seiten']))
                    if not (3 in b['seiten']) : pass
            if 'winkel' in b:
                if sum(b['winkel']) != 180: f('%s: Winkelsumme %s ≠ 180°' % (k, b['winkel']))
                wa = winkelart(b['winkel'])
                if nach == 'winkel' and wa != art: f('%s: Winkel %s sind %s' % (k, b['winkel'], wa))
                if art == 'gleichschenklig' and len(set(b['winkel'])) != 2: f('%s: Basiswinkel nicht gleich' % k)
                if art == 'gleichseitig' and set(b['winkel']) != {60}: f('%s: nicht 3 · 60°' % k)
                if art == 'allgemein' and len(set(b['winkel'])) != 3: f('%s: Winkel nicht verschieden' % k)
        zaehle('dreiecks-beispiele', len(e['beispiele']))
    # rechtwinklig: die zwei anderen Winkel ergeben 90°
    for b in d['fg-12']['beispiele']:
        if 'winkel' in b and sum(x for x in b['winkel'] if x != 90) != 90: f('fg-12: die beiden anderen Winkel ergeben nicht 90°')
    if sum(x for x in [120, 35, 25] if x != 120) >= 90: f('stumpfwinklig: andere Winkel nicht spitz')
    # --- Vierecke
    VE = [e for e in E if e['art'] == 'viereck']
    if [e['schluessel'] for e in VE] != ['quadrat', 'rechteck', 'raute', 'parallelogramm', 'trapez', 'gl_trapez', 'drachen', 'allgemein']: f('Vierecke: Reihenfolge oder Anzahl')
    zusatz = [[(0, 0), (3, 4), (-1, 7), (-4, 3)], [(0, 0), (4, 3), (-2, 11), (-6, 8)], [(4, 0), (0, 3), (-4, 0), (0, -3)], [(0, 0), (5, 0), (5, 5), (0, 5)], [(0, 0), (4, 0), (6, 3), (2, 3)]]
    korpus = [e['beispiel_punkte'] for e in VE] + zusatz
    eig = [viereck_eig(P) for P in korpus]
    for P, w in zip(korpus, eig):
        if not w['konvex']: f('Viereck %s ist nicht konvex' % P)
    # Winkelsumme jedes Vierecks: 2 · 180°
    for P in korpus:
        pass
    FL = ['parallele_paare_mindestens', 'gegenseiten_gleich_lang', 'alle_seiten_gleich_lang', 'nachbarseitenpaare_gleich_lang', 'vier_rechte_winkel', 'gegenueberliegende_winkel_gleich', 'diagonalen_gleich_lang', 'diagonalen_senkrecht', 'diagonalen_halbieren_sich', 'symmetrieachsen_mindestens', 'punktsymmetrisch']
    for e in VE:
        kl = KLASSE_VON[e['schluessel']]; fl = e['immer']
        if set(fl) != set(FL): f('%s: immer-Schlüssel' % e['titel'])
        idx = [i for i, w in enumerate(eig) if w['_klasse'][kl]]
        if not eig[VE.index(e)]['_klasse'][kl]: f('%s: sein Beispiel ist keins' % e['titel'])
        # das eigene Beispiel darf keine Sonderart sein (außer es gehört dazu)
        for flag in FL:
            for i in idx:
                v = eig[i][flag]
                if isinstance(fl[flag], bool):
                    if fl[flag] and not v: f('%s: „immer %s“ stimmt nicht für Beispiel %s' % (e['titel'], flag, korpus[i]))
                else:
                    if v < fl[flag]: f('%s: %s ≥ %d stimmt nicht für %s' % (e['titel'], flag, fl[flag], korpus[i]))
            if isinstance(fl[flag], bool):
                if not fl[flag] and all(eig[i][flag] for i in idx): f('%s: %s gilt für alle geprüften Beispiele, ist aber nicht als „immer“ angegeben' % (e['titel'], flag))
            else:
                if min(eig[i][flag] for i in idx) != fl[flag]: f('%s: %s ist im Beispielbestand %s, angegeben %s' % (e['titel'], flag, min(eig[i][flag] for i in idx), fl[flag]))
        t = e['seiten'].lower(); dg = e['diagonalen'].lower(); wn = e['winkel'].lower()
        if ('senkrecht' in dg) != fl['diagonalen_senkrecht'] or ('halbieren sich' in dg) != fl['diagonalen_halbieren_sich'] or ('gleich lang' in dg) != fl['diagonalen_gleich_lang']: f('%s: Diagonalen-Text passt nicht zu den Eigenschaften' % e['titel'])
        if ('parallel' in t) != (fl['parallele_paare_mindestens'] >= 1): f('%s: Text „parallel“ passt nicht' % e['titel'])
        if ('alle vier seiten sind gleich lang' in t) != fl['alle_seiten_gleich_lang']: f('%s: Text „alle Seiten gleich“ passt nicht' % e['titel'])
        if ('gegenseiten sind gleich lang' in t and not fl['gegenseiten_gleich_lang']) or (fl['gegenseiten_gleich_lang'] and not fl['alle_seiten_gleich_lang'] and 'gegenseiten sind gleich lang' not in t): f('%s: Text Gegenseiten passt nicht' % e['titel'])
        if ('zwei paare gleich langer nachbarseiten' in t) and not fl['nachbarseitenpaare_gleich_lang']: f('%s: Text Nachbarseiten' % e['titel'])
        if fl['nachbarseitenpaare_gleich_lang'] and not fl['alle_seiten_gleich_lang'] and 'nachbarseiten' not in t: f('%s: Nachbarseiten fehlen im Text' % e['titel'])
        if ('90°' in wn) != fl['vier_rechte_winkel']: f('%s: Text 90° passt nicht' % e['titel'])
        if ('gegenüberliegende winkel sind gleich' in wn) != (fl['gegenueberliegende_winkel_gleich'] and not fl['vier_rechte_winkel']): f('%s: Text gegenüberliegende Winkel passt nicht' % e['titel'])
        a0 = e['achsen_text'].split()[0]
        if a0 != ('keine' if fl['symmetrieachsen_mindestens'] == 0 else str(fl['symmetrieachsen_mindestens'])): f('%s: achsen_text %r ≠ %s' % (e['titel'], e['achsen_text'], fl['symmetrieachsen_mindestens']))
        if e['punktsymmetrisch'] != fl['punktsymmetrisch']: f('%s: punktsymmetrisch' % e['titel'])
        zaehle('vierecks-eigenschaften')
    # --- Haus der Vierecke
    h = d['fg-22']
    name = {e['schluessel']: e['titel'] for e in VE}
    # Titel und Klassennamen: die Beziehungen benutzen die Titel der Einträge
    kanten = {(b['sonderfall'], b['von']) for b in h['beziehungen']}
    kanten2 = {(e['titel'], v) for e in VE for v in e['sonderfall_von']}
    if kanten != kanten2: f('Haus der Vierecke: beziehungen und sonderfall_von widersprechen sich')
    titel_zu_klasse = {e['titel']: KLASSE_VON[e['schluessel']] for e in VE}
    if set(titel_zu_klasse) != {x for k in kanten for x in k}.union(set(titel_zu_klasse)): f('Haus: unbekannte Namen')
    for a, b in kanten:
        if a not in titel_zu_klasse or b not in titel_zu_klasse: f('Haus: unbekanntes Viereck %s/%s' % (a, b))
    # Hülle
    namen = list(titel_zu_klasse)
    huelle = {n: set() for n in namen}
    for a, b in kanten: huelle[a].add(b)
    ch = True
    while ch:
        ch = False
        for n in namen:
            for m in list(huelle[n]):
                if not huelle[m] <= huelle[n]: huelle[n] |= huelle[m]; ch = True
    for n in namen:
        kl = titel_zu_klasse[n]
        idx = [i for i, w in enumerate(eig) if w['_klasse'][kl]]
        if not idx: f('Haus: kein Beispiel für %s' % n); continue
        for m in namen:
            if m == n: continue
            kl2 = titel_zu_klasse[m]
            folgt = all(eig[i]['_klasse'][kl2] for i in idx)
            if (m in huelle[n]) != folgt: f('Haus: „%s ist Sonderfall von %s“ ist %s, die Koordinaten sagen %s' % (n, m, m in huelle[n], folgt))
            zaehle('haus-paare')
    # Schichten: jede Kante geht eine oder mehrere Schichten nach unten
    sch = {n: i for i, row in enumerate(h['geschichtet']) for n in row}
    ALLE = {n.replace('Allgemeines Viereck', 'Allgemeines Viereck') for n in namen}
    sch_namen = {'Quadrat': 'Quadrat', 'Rechteck': 'Rechteck', 'Raute': 'Raute', 'Parallelogramm': 'Parallelogramm', 'gleichschenkliges Trapez': 'Gleichschenkliges Trapez', 'Drachenviereck': 'Drachenviereck', 'Trapez': 'Trapez', 'Allgemeines Viereck': 'Allgemeines Viereck'}
    sch = {sch_namen.get(n, n): i for n, i in sch.items()}
    if set(sch) != set(namen): f('Haus: geschichtet enthält %s statt %s' % (sorted(sch), sorted(namen)))
    for a, b in kanten:
        if a in sch and b in sch and not sch[a] < sch[b]: f('Haus: Pfeil %s → %s geht nicht nach unten' % (a, b))
    # --- Kongruenzsätze
    ks = [e for e in E if e['art'] == 'kongruenzsatz']
    if [e['kuerzel'] for e in ks] != ['SSS', 'SWS', 'WSW', 'SsW']: f('Kongruenzsätze: SSS, SWS, WSW, SsW erwartet')
    for e in ks:
        b = e['beispiel_daten']; k = e['kuerzel']
        if k == 'SSS':
            s = b['seiten']; a, bb, c = s['a'], s['b'], s['c']
            if not (a + bb > c and a + c > bb and bb + c > a): f('SSS: Dreiecksungleichung verletzt')
        if k == 'SWS':
            if len(b['seiten']) != 2 or set(b['zwischen']) != set(b['seiten']) or not (0 < b['winkel']['α'] < 180): f('SWS: Beispiel')
        if k == 'WSW':
            if not (b['winkel']['α'] + b['winkel']['β'] < 180) or len(b['seiten']) != 1: f('WSW: Winkel zusammen nicht unter 180°')
        if k == 'SsW':
            gam = b['winkel']['γ']; geg = b['gegenueber']['γ']; sd = b['seiten']
            if geg != max(sd, key=sd.get) or sd[geg] <= min(sd.values()): f('SsW: Winkel liegt nicht der längeren Seite gegenüber')
            if not (0 < gam < 180): f('SsW: Winkel')
            kurz = min(sd, key=sd.get)
            if not (sd[kurz] * math.sin(math.radians(gam)) / sd[geg] < 1): f('SsW: Dreieck existiert nicht')
    w3 = d['fg-27']['beispiel_daten']
    if len(set(w3['seiten_a'])) != 1 or len(set(w3['seiten_b'])) != 1 or w3['seiten_a'][0] == w3['seiten_b'][0] or set(w3['winkel']) != {60}: f('WWW: Gegenbeispiel')
    zaehle('kongruenzsätze', len(ks))
figuren_pruefen()

# ============================================================ 8 Zeichen und Wörter
IRRKLASSE = {'ℕ': lambda v: v.rational() and v.wert().denominator == 1 and v.wert() >= 0 and v.d == NULLDIM,
             'ℤ': lambda v: v.rational() and v.wert().denominator == 1 and v.d == NULLDIM,
             'ℚ': lambda v: v.rational() and v.d == NULLDIM, 'ℝ': lambda v: v.d == NULLDIM}
TEIL = {('ℕ', 'ℤ'), ('ℕ', 'ℚ'), ('ℕ', 'ℝ'), ('ℤ', 'ℚ'), ('ℤ', 'ℝ'), ('ℚ', 'ℝ')}
def menge_lesen(s):
    s = s.strip()
    if s in IRRKLASSE: return ('name', s)
    if s.startswith('{') and s.endswith('}'):
        inner = s[1:-1].strip()
        if not inner: return ('menge', set())
        return ('menge', {q_aus(x).wert() for x in inner.split(';')})
    raise Nicht('Mengenausdruck')
def menge_ausdruck(s):
    for op in (' ∩ ', ' ∪ '):
        if op in s:
            a, b = s.split(op, 1); x, y = menge_lesen(a), menge_lesen(b)
            if x[0] != 'menge' or y[0] != 'menge': raise Nicht('Menge')
            return ('menge', x[1] & y[1] if op == ' ∩ ' else x[1] | y[1])
    return menge_lesen(s)
def aussage_pruefen(text):
    """-> True/False; Nicht, wenn nicht auswertbar."""
    if any(c in text for c in '∈∉⊂') or '{' in text or any(c in text for c in 'ℕℤℚℝ'):
        for op in (' ∉ ', ' ∈ ', ' ⊂ '):
            if op in text:
                l, r = text.split(op, 1)
                m = menge_ausdruck(r)
                if op == ' ⊂ ':
                    a = menge_ausdruck(l)
                    if a[0] == 'name' and m[0] == 'name': return (a[1], m[1]) in TEIL
                    if a[0] == 'menge' and m[0] == 'menge': return a[1] <= m[1]
                    raise Nicht('Teilmenge')
                v = q_aus(l) if not l.strip().startswith('√') or True else None
                if isinstance(v, Irr):
                    ist = (m[0] == 'name' and m[1] == 'ℝ')
                else:
                    if m[0] == 'name': ist = IRRKLASSE[m[1]](v)
                    else: ist = v.rational() and v.wert() in m[1]
                return ist if op == ' ∈ ' else not ist
        # Gleichheit zwischen Mengen
        if ' = ' in text:
            l, r = text.split(' = ', 1); a, b = menge_ausdruck(l), menge_ausdruck(r)
            if a[0] == 'menge' and b[0] == 'menge': return a[1] == b[1]
        raise Nicht('Mengenaussage')
    toks = tokenize(text)
    rels = [t for k, t in toks if k == 'REL']
    teile, akt = [], []
    for k, t in toks:
        if k == 'REL': teile.append(akt); akt = []
        else: akt.append((k, t))
    teile.append(akt)
    if not rels or any(not x for x in teile): raise Nicht('keine Relation')
    return pruefe_kette((teile, rels), text)
def zeichen_pruefen():
    n_ok = 0
    for e in T['zeichen-woerter']['eintraege']:
        if e['art'] != 'zeichen': continue
        for b in e['beispiele']:
            if b['gilt'] is None: continue
            try: res = aussage_pruefen(b['text'])
            except (Nicht, DimError) as ex: f('%s: Beispiel %r nicht auswertbar: %s' % (e['kennung'], b['text'], ex)); continue
            if res != b['gilt']: f('%s: Beispiel %r ist %s, angegeben %s' % (e['kennung'], b['text'], res, b['gilt']))
            n_ok += 1
    zaehle('zeichen-beispiele', n_ok)
    for e in T['zeichen-woerter']['eintraege']:
        if e['art'] == 'fachwort':
            if len(e['satz']) > 160 or e['satz'].count('. ') > 1: f('%s: Satz zu lang für ein Kind: %r' % (e['kennung'], e['satz']))
            if 'rechnung' in e:
                ts = tokenize(e['rechnung'])
                zaehle('glossar-rechnungen')
            for r in e['rolle_im_beispiel']:
                if ': ' not in r: f('%s: Rolle ohne Doppelpunkt' % e['kennung'])
            # die genannten Rollenzahlen stehen im Beispiel
            for r in e['rolle_im_beispiel']:
                zahl = r.split(': ')[0]
                if zahl not in e['beispiel']: f('%s: %r steht nicht im Beispiel %r' % (e['kennung'], zahl, e['beispiel']))
    # Gruppen: genau die geforderten Fachwörter
    verlangt = ['Summand', 'Summe', 'Minuend', 'Subtrahend', 'Differenz', 'Faktor', 'Produkt', 'Dividend', 'Divisor', 'Quotient', 'Basis', 'Exponent', 'Potenz', 'Radikand', 'Zähler', 'Nenner', 'Kehrwert', 'Term', 'Variable', 'Koeffizient', 'Gleichung', 'Ungleichung', 'Lösungsmenge', 'Definitionsmenge', 'Grundwert', 'Prozentwert', 'Prozentsatz']
    haben = [e['begriff'] for e in T['zeichen-woerter']['eintraege'] if e['art'] == 'fachwort']
    for v in verlangt:
        if v not in haben: f('Fachwort fehlt: %s' % v)
    zv = ['=', '≠', '≈', '<', '>', '≤', '≥', '·', ':', '±', '√', '∛', 'π', '%', '|a|', '∈', '∉', '⊂', '∩', '∪', '{ }', 'ℕ', 'ℤ', 'ℚ', 'ℝ', '∥', '⊥', '∠', '△', '≅', '∼', '[AB]', '|AB|', 'AB']
    hz = [e['zeichen'] for e in T['zeichen-woerter']['eintraege'] if e['art'] == 'zeichen']
    for v in zv:
        if v not in hz: f('Zeichen fehlt: %s' % v)
    gv = ['α', 'β', 'γ', 'δ', 'ε', 'π', 'φ', 'Δ']
    hg = [e['buchstabe'] for e in T['zeichen-woerter']['eintraege'] if e['art'] == 'griechisch']
    for v in gv:
        if v not in hg: f('Griechischer Buchstabe fehlt: %s' % v)
    # Namen der griechischen Buchstaben
    NAMEN_GR = {'α': 'Alpha', 'β': 'Beta', 'γ': 'Gamma', 'δ': 'Delta', 'ε': 'Epsilon', 'φ': 'Phi', 'π': 'Pi', 'Δ': 'Delta', 'σ': 'Sigma', 'μ': 'My', 'Ω': 'Omega'}
    for e in T['zeichen-woerter']['eintraege']:
        if e['art'] == 'griechisch':
            if not e['name'].startswith(NAMEN_GR[e['buchstabe']]): f('Name von %s: %s' % (e['buchstabe'], e['name']))
            if (e['buchstabe'] == e['buchstabe'].upper()) != (e['schreibung'] == 'groß'): f('%s: groß/klein' % e['buchstabe'])
zeichen_pruefen()

# ============================================================ 9 tafel.md
def md_pruefen():
    for n, d in T.items():
        p = hier / n / 'tafel.md'
        if not p.exists(): f('%s: tafel.md fehlt' % n); continue
        t = p.read_text(encoding='utf-8')
        if '## Vorschlag zur Gliederung der Karte' not in t: f('%s/tafel.md: Abschnitt „Vorschlag zur Gliederung der Karte“ fehlt' % n)
        if len(t.splitlines()) > 260: f('%s/tafel.md zu lang (%d Zeilen)' % (n, len(t.splitlines())))
        schreibweise(n, n + '/tafel.md', t)
        for sp in spannen(t): spanne_pruefen(sp, n + '/tafel.md', stats)
        # jede Kennung des Eintrags steht in der Datei
        for e in d['eintraege']:
            if e['kennung'] not in t: f('%s/tafel.md: Kennung %s fehlt' % (n, e['kennung']))
        if n.startswith('formeln'):
            for e in d['eintraege']:
                if e['formel'] not in t: f('%s/tafel.md: Formel %r fehlt' % (n, e['formel']))
        zaehle('tafel.md')
md_pruefen()

# ============================================================ Ergebnis
if fehler:
    print('FEHLER (%d):' % len(fehler))
    for x in fehler[:200]: print(' -', x)
    sys.exit(1)
print('Rechenspannen geprüft: %d (nicht auswertbar, übersprungen: %d)' % (stats['ok'], stats['nicht']))
print('; '.join('%s: %d' % (k, v) for k, v in sorted(Z.items())))
print('OK')
