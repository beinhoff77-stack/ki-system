#!/usr/bin/env python3
"""Thema gleichungen.exponential – Exponentialgleichungen (Klasse 10). Schreibt inhalte/themen/gleichungen.exponential.json."""
import sys
import math
from math import ceil, log
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import *  # noqa: E402,F403

start(1001)
TIEF = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')
HZ = HOCHZ


def lb(b):
    """log zur Basis b als Text"""
    return 'lg' if b == 10 else f'log{str(b).translate(TIEF)}'


def pt(b, n):
    """Potenz b^n als Text"""
    return f'{b}{str(n).translate(HZ)}' if n >= 0 else f'{b}^({dz(n)})'


def cf(x):
    x = Fr(x)
    if x.denominator == 1: return str(int(x))
    if endlich(x): return str(float(x))
    return f'({x.numerator}/{x.denominator})'


def zt(x):
    """Zahl als Text: Dezimalzahl oder Bruch"""
    x = Fr(x)
    return dz(x) if endlich(x) else br(x)


ETAPPEN = [
    {'lernziel': 'logarithmus', 'titel': 'Logarithmen berechnen',
     'regel': '⟦log_b(x)⟧ ist der Exponent, mit dem man b potenzieren muss, um x zu erhalten: ⟦b^y = x ⇔ y = log_b(x)⟧ (b > 0, b ≠ 1, x > 0). lg steht für log₁₀.',
     'schritte': ['log₂(32): Mit welchem Exponenten wird 2 zu 32?', '2⁵ = 32, also ⟦log₂(32) = 5⟧.'],
     'probe': '2 · 2 · 2 · 2 · 2 = 32 ✓',
     'fehler': 'log₂(32) = 32 : 2 = 16 ist falsch: Der Logarithmus fragt nach dem ⟦Exponenten⟧, nicht nach einem Quotienten.'},
    {'lernziel': 'gleiche_basis', 'titel': 'Gleichungen mit gleicher Basis',
     'regel': 'Lassen sich beide Seiten als Potenzen ⟦derselben Basis⟧ schreiben, setzt du die ⟦Exponenten gleich⟧: b^u = b^v ⇔ u = v.',
     'schritte': ['3^(x − 1) = 81 und 81 = 3⁴.', 'x − 1 = 4, also ⟦x = 5⟧.'],
     'probe': '3^(5 − 1) = 3⁴ = 81 ✓',
     'fehler': '3^(x − 1) = 81 ⇒ x − 1 = 81 : 3 ist falsch: Man vergleicht die ⟦Exponenten⟧, dazu muss 81 erst als 3⁴ geschrieben werden.'},
    {'lernziel': 'mit_log_loesen', 'titel': 'Mit dem Logarithmus lösen',
     'regel': 'Ist keine gemeinsame Basis erkennbar: Potenz allein stellen, dann ⟦logarithmieren⟧: b^x = c ⇔ ⟦x = log_b(c) = lg c : lg b⟧. Ergebnis sinnvoll runden.',
     'schritte': ['3 · 2^x = 30 ⇔ 2^x = 10.', 'x = lg 10 : lg 2 ≈ ⟦3,32⟧ (auf zwei Nachkommastellen).'],
     'probe': '2^3,32 ≈ 9,99 ✓',
     'fehler': '3 · 2^x = 30 ⇒ 6^x = 30 ist falsch: 3 · 2^x ist nicht (3 · 2)^x. Erst ⟦durch 3 teilen⟧, dann logarithmieren.'},
    {'lernziel': 'potenzregel', 'titel': 'Die Potenzregel für Logarithmen',
     'regel': 'Ein Exponent im Logarithmus wird zum ⟦Faktor⟧: ⟦log_b(a^r) = r · log_b(a)⟧. Warum? Schreib a = b^y, also y = log_b(a). Dann ist a^r = (b^y)^r = b^(r · y). Der Exponent davon ist r · y = r · log_b(a). So holt man die Unbekannte aus dem Exponenten.',
     'schritte': ['5^x = 2^(x + 1): beide Seiten mit lg: x · lg 5 = (x + 1) · lg 2.', 'x(lg 5 − lg 2) = lg 2 ⇒ x = lg 2 : (lg 5 − lg 2) ≈ ⟦0,76⟧.'],
     'probe': '5^0,76 ≈ 3,40; 2^1,76 ≈ 3,39 ✓ (Rundung)',
     'fehler': 'lg(5x) = x · lg 5 ist falsch: Die Potenzregel gilt nur für ⟦Potenzen⟧ 5^x, nicht für Produkte 5 · x.'},
    {'lernziel': 'wachstum', 'titel': 'Wachstum und Zerfall: Wann?',
     'regel': 'Wachstum: ⟦N(t) = N₀ · q^t⟧ (q = 1 + p bei Zunahme um p, q = 1 − p bei Abnahme). Gesucht ist t: N₀ · q^t = Ziel ⇒ ⟦t = log_q(Ziel : N₀)⟧.',
     'schritte': ['1 000 € mit 4 % Zinseszins. Wann sind es 1 500 €? 1,04^t = 1,5.', 't = lg 1,5 : lg 1,04 ≈ 10,34, also nach ⟦11 vollen Jahren⟧.'],
     'probe': '1 000 · 1,04¹¹ ≈ 1 539 € > 1 500 €, aber 1,04¹⁰ · 1 000 ≈ 1 480 € ✓',
     'fehler': 'Bei 4 % Zinsen q = 4 oder q = 0,04 zu nehmen ist falsch: Der ⟦Wachstumsfaktor⟧ ist q = 1,04.'},
    {'lernziel': 'verstehen', 'titel': 'Aussagen über Logarithmen prüfen',
     'regel': 'log_b(x) gibt es nur für ⟦x > 0⟧. Es gilt ⟦log_b(1) = 0⟧ und ⟦log_b(b) = 1⟧. Für Summen gibt es keine Potenzregel: lg(a + b) ≠ lg a + lg b.',
     'schritte': ['Behauptung: 2^x = −8 hat die Lösung x = −3.', '2^(−3) = 1/8 > 0. Eine Potenz 2^x ist ⟦immer positiv⟧, also keine Lösung.'],
     'probe': 'lg(−8) zeigt der Taschenrechner als Fehler ✓',
     'fehler': '„Bei 2^x = −8 einfach x = −3“ ist falsch: Ein negatives Vorzeichen im Exponenten erzeugt einen ⟦Kehrwert⟧, kein negatives Ergebnis.'},
]

# Zeichnungen für die Lernkarten
_E = {e['lernziel']: e for e in ETAPPEN}
_E['logarithmus']['bild'] = koord([{'art': 'exp', 'a': 1, 'b': 2, 'name': 'y = 2ˣ'}], x=(-1, 6), y=(0, 36), punkte=[{'x': 5, 'y': 32, 'name': '(5 | 32)'}],
                                  strecken=[[5, 0, 5, 32, 'gestrichelt'], [0, 32, 5, 32, 'gestrichelt']])
_E['mit_log_loesen']['bild'] = koord([{'art': 'exp', 'a': 1, 'b': 2, 'name': 'y = 2ˣ'}], x=(-1, 5), y=(0, 16), waagrecht=[10],
                                     punkte=[{'x': 3.32, 'y': 10, 'name': 'x ≈ 3,32'}])
_E['wachstum']['bild'] = koord([{'art': 'exp', 'a': 1000, 'b': 1.04, 'bereich': [0, 15]}], x=(0, 15), y=(0, 2000), waagrecht=[1500],
                               senkrecht=[10.34], name_x='t', name_y='K', schritt_y=250)
_E['verstehen']['bild'] = koord([{'art': 'exp', 'a': 1, 'b': 2, 'name': 'y = 2ˣ'}], x=(-4, 4), y=(-10, 16), waagrecht=[-8])


def g_logarithmus(s):
    b = R.choice([2, 3, 4, 5, 10])
    if s == 1:
        n = R.randint(1, {2: 8, 3: 5, 4: 4, 5: 4, 10: 6}[b])
        x = b ** n
        return zahl(f'Berechne {lb(b)}({dz(x)}).', f'{pt(b, n)} = {dz(x)}, also {lb(b)}({dz(x)}) = {n}.', f'Mit welchem Exponenten wird {b} zu {dz(x)}?',
                    n, f'{n} + ({b} ** {n} - {x})')
    if s == 2:
        n = R.choice([-1, -2, -3, -1, -2, 0]) if b != 10 else R.choice([-1, -2, -3, -4, 0])
        x = Fr(b) ** n
        xt = dz(x) if b == 10 else br(x)
        return zahl(f'Berechne {lb(b)}({xt}).', f'{pt(b, n)} = {xt}, also {lb(b)}({xt}) = {dz(n)}.',
                    'Ein Kehrwert entsteht durch einen negativen Exponenten; b⁰ = 1.', n, f'{n} + ({b} ** ({n}) - {cf(x)})')
    typ = R.random()
    if typ < 0.3:
        # log_b(x) = n, gesucht b
        b, n = R.choice([(b_, n_) for b_ in range(2, 13) for n_ in (2, 3, 4) if 8 <= b_ ** n_ <= 5000])
        x = b ** n
        return zahl(f'Es gilt log_b({dz(x)}) = {n}. Bestimme die Basis b.', f'log_b({dz(x)}) = {n} heißt b^{n} = {dz(x)}, also b = {b}.',
                    'Schreibe die Gleichung als Potenz: b hoch … ergibt …', b, f'{b} + ({b} ** {n} - {x})')
    if typ < 0.6:
        # log_b(x) = n (auch negativ), gesucht x
        b = R.choice([2, 3, 4, 5, 10])
        n = R.choice([-3, -2, -1, 2, 3, 4]) if b != 10 else R.choice([-3, -2, -1, 2, 3])
        x = Fr(b) ** n
        if n > 0 and x > 5000: return None
        if x.denominator == 1:
            return zahl(f'Es gilt {lb(b)}(x) = {n}. Bestimme x.', f'{lb(b)}(x) = {n} heißt x = {pt(b, n)} = {dz(x)}.',
                        'Der Logarithmus ist der Exponent: Basis hoch Logarithmus ergibt x.', x, f'{b} ** {n}')
        if b == 10:
            return zahl(f'Es gilt lg(x) = {dz(n)}. Bestimme x als Dezimalzahl.', f'lg(x) = {dz(n)} heißt x = 10^({dz(n)}) = {dz(x)}.',
                        'Der Logarithmus ist der Exponent: 10 hoch Logarithmus ergibt x.', x, f'10 ** ({n})')
        return bruch_luecke(f'Es gilt {lb(b)}(x) = {dz(n)}. Bestimme x als Bruch.', x, f'{lb(b)}(x) = {dz(n)} heißt x = {pt(b, n)} = {br(x)}.',
                            'Ein negativer Exponent bedeutet Kehrwert.', c=['1', f'{b} ** {-n}'])
    k = R.choice([1, 3, 5, 7])
    b = R.choice([2, 3, 5])
    if b ** k > 5000: return None
    v = Fr(k, 2)
    xt = f'√{dz(b ** k)}'
    return zahl(f'Berechne {lb(b)}({xt}).', f'{xt} = {b}^({k}/2) = {b}^{dz(v)}, also {lb(b)}({xt}) = {dz(v)}.',
                'Schreibe die Wurzel als Potenz mit Exponent ½.', v, f'{cf(v)} + ({b} ** (2 * {cf(v)}) - {b ** k})')


def g_gleiche_basis(s):
    b = R.choice([2, 3, 5])
    if s == 1:
        n = R.randint(2, {2: 9, 3: 6, 5: 4}[b])
        return zahl(f'Löse {b}^x = {dz(b ** n)}.', f'{dz(b ** n)} = {pt(b, n)}, also x = {n}.', f'Schreibe {dz(b ** n)} als Potenz von {b}.',
                    n, f'{n} + ({b} ** {n} - {b ** n})')
    if s == 2 and R.random() < 0.4:
        # rechte Seite ist ein Kehrwert: 2^x = 1/16, 5^(x − 1) = 0,2
        n = R.randint(1, {2: 5, 3: 4, 5: 3}[b])
        r = Fr(1, b ** n)
        rt = dz(r) if b in (2, 5) and R.random() < 0.5 else br(r)
        k = R.choice([0, 0, -1, 1, -2, 2])
        x = -n - k
        ex = f'x {plus(k)}' if k else 'x'
        links = f'{b}^({ex})' if k else f'{b}^x'
        gl = f'{rt} = 1/{dz(b ** n)}' if rt != br(r) else rt
        schluss = f'{ex} = −{n} ⇒ x = {dz(x)}' if k else f'x = {dz(x)}'
        return zahl(f'Löse {links} = {rt}.', f'{gl} = {b}^(−{n}) ⇒ {schluss}.',
                    'Ein Kehrwert ist eine Potenz mit negativem Exponenten.', x, f'{x} + ({b} ** ({x} + ({k})) * {b ** n} - 1)')
    if s == 2:
        k = R.randint(-4, 4)
        n = R.randint(1, {2: 7, 3: 5, 5: 3}[b])
        x = n - k
        if k == 0: return None
        exp_t = f'x {plus(k)}'
        return zahl(f'Löse {b}^({exp_t}) = {dz(b ** n)}.', f'{dz(b ** n)} = {pt(b, n)} ⇒ {exp_t} = {n} ⇒ x = {dz(x)}.',
                    'Rechte Seite als Potenz derselben Basis schreiben, dann Exponenten gleichsetzen.', x, f'{x} + ({b} ** ({x} + ({k})) - {b ** n})')
    typ = R.random()
    if typ < 0.4:
        # 4^x = 2^n bzw. 9^x = 3^n
        b, B = R.choice([(2, 4), (3, 9), (2, 8)])
        e = {4: 2, 9: 2, 8: 3}[B]
        n = R.randint(1, 9)
        x = Fr(n, e)
        if x.denominator == 1: return None
        return zahl(f'Löse {B}^x = {dz(b ** n)}.', f'{B} = {pt(b, e)}, {dz(b ** n)} = {pt(b, n)} ⇒ {e}x = {n} ⇒ x = {zt(x)}.',
                    f'Schreibe beide Seiten als Potenz von {b}.', x, f'{cf(x)} + ({b} ** ({e} * {cf(x)}) - {b ** n})') if endlich(x) else \
            bruch_luecke(f'Löse {B}^x = {dz(b ** n)}. Gib x als gekürzten Bruch an.', x,
                         f'{B} = {pt(b, e)}, {dz(b ** n)} = {pt(b, n)} ⇒ {e}x = {n} ⇒ x = {br(x)}.', f'Schreibe beide Seiten als Potenz von {b}.',
                         c=[f'{n} * {x.denominator} // {e}', f'{x.denominator}'])
    if typ < 0.6:
        # B^(x + k) = b^n mit B = b^e  ⇒  e(x + k) = n
        b, B, e = R.choice([(2, 4, 2), (3, 9, 2), (2, 8, 3), (5, 25, 2)])
        n = R.randint(1, {2: 7, 3: 5, 5: 4}[b])
        k = R.choice([-2, -1, 1, 2])
        x = Fr(n, e) - k
        if not endlich(x) or n % e == 0: return None
        return zahl(f'Löse {B}^(x {plus(k)}) = {dz(b ** n)}.',
                    f'{B} = {pt(b, e)}, {dz(b ** n)} = {pt(b, n)} ⇒ {e} · (x {plus(k)}) = {n} ⇒ x {plus(k)} = {zt(Fr(n, e))} ⇒ x = {dz(x)}.',
                    f'Welche gemeinsame Basis haben {B} und {dz(b ** n)}?', x, f'{cf(x)} + ({b} ** ({e} * ({cf(x)} + ({k}))) - {b ** n})')
    if typ < 0.75:
        n = R.randint(1, {2: 6, 3: 4, 5: 3}[b])
        return zahl(f'Löse (1/{b})^x = {dz(b ** n)}.', f'(1/{b})^x = {b}^(−x) = {pt(b, n)} ⇒ −x = {n} ⇒ x = −{n}.',
                    'Schreibe 1/b als b hoch −1.', -n, f'({-n}) + ({b} ** (-({-n})) - {b ** n})')
    a = R.randint(2, 5)
    n = R.randint(1, {2: 7, 3: 5, 5: 3}[b])
    return zahl(f'Löse {a} · {b}^x = {dz(a * b ** n)}.', f'{b}^x = {dz(a * b ** n)} : {a} = {dz(b ** n)} = {pt(b, n)} ⇒ x = {n}.',
                'Teile zuerst durch den Faktor vor der Potenz.', n, f'{n} + ({b} ** {n} - {a * b ** n} / {a})')


def g_mit_log_loesen(s):
    if s == 1:
        b = R.choice([2, 3, 5, 7, 10])
        c = R.choice([x for x in range(2, 200) if abs(log(x, b) - round(log(x, b))) > 0.05])
        x = log(c) / log(b)
        v = gerundet(x, 2)
        if v is None: return None
        a = zahl(f'Löse {b}^x = {c}. Runde auf zwei Nachkommastellen. (Die Zeichnung zeigt y = {b}^x und y = {c} zum Abschätzen.)',
                 f'Der Schnittpunkt liegt etwa bei x ≈ {dz(round(x))}. Genau: x = {lb(b)}({c}) = lg {c} : lg {b} ≈ {dz(v)}.',
                 'Schätze mit der Zeichnung, dann logarithmiere beide Seiten.', v, f'round({K(x)}, 2)', tol=0.01)
        xr = (min(-1, math.floor(x) - 1), max(3, math.ceil(x) + 1))
        return mit_grafik(a, koord([{'art': 'exp', 'a': 1, 'b': b}], x=xr, y=(0, round(c * 1.4)), waagrecht=[c]))
    if s == 2:
        a = R.randint(2, 9)
        q = R.choice([Fr(3, 2), Fr(6, 5), Fr(5, 4), 2, 3, Fr(1, 2), Fr(4, 5)])
        c = R.randint(a + 1, 20 * a) if q > 1 else Fr(R.randint(1, 9 * a), 10)
        if q < 1 and c >= a: return None
        r = Fr(c) / a
        x = log(r) / log(q)
        v = gerundet(x, 2)
        if v is None or abs(x - round(x)) < 0.05: return None
        return zahl(f'Löse {a} · {dz(q)}^x = {dz(c)}. Runde auf zwei Nachkommastellen.',
                    f'{dz(q)}^x = {dz(c)} : {a} = {zt(r)} ⇒ x = lg({zt(r)}) : lg {dz(q)} ≈ {dz(v)}.',
                    'Erst durch den Faktor teilen, dann logarithmieren.', v, f'round({K(x)}, 2)', tol=0.01)
    b = R.choice([2, 3, 5])
    k, m = R.choice([2, 3]), R.randint(-3, 3)
    c = R.randint(2, 300)
    # b^(k x + m) = c  ⇒  x = (log_b c − m)/k
    x = (log(c) / log(b) - m) / k
    v = gerundet(x, 2)
    if v is None or abs(log(c, b) - round(log(c, b))) < 0.05: return None
    ex = f'{k}x {plus(m)}' if m else f'{k}x'
    return zahl(f'Löse {b}^({ex}) = {c}. Runde auf zwei Nachkommastellen.',
                f'{ex} = {lb(b)}({c}) ≈ {dz(round(log(c, b), 4))} ⇒ x ≈ {dz(v)}.', 'Erst den ganzen Exponenten bestimmen, dann nach x auflösen.',
                v, f'round({K(x)}, 2)', tol=0.01)


def _gl_zwei_basen():
    a, b2 = R.sample([2, 3, 5, 7], 2)
    m = R.choice([1, 2, -1, 3, -2])
    # a^x = b2^(x + m)  ⇒  x lg a = (x + m) lg b2  ⇒  x = m lg b2 / (lg a − lg b2)
    x = m * lg(b2) / (lg(a) - lg(b2))
    v = gerundet(x, 2)
    if v is None: return None
    return zahl(f'Löse {a}^x = {b2}^(x {plus(m)}). Runde auf zwei Nachkommastellen.',
                f'x · lg {a} = (x {plus(m)}) · lg {b2} ⇒ x(lg {a} − lg {b2}) = {dz(m)} · lg {b2} ⇒ x ≈ {dz(v)}.',
                'Logarithmiere beide Seiten, wende die Potenzregel an und sammle die x-Terme.', v, f'round({K(x)}, 2)', tol=0.01)


def g_potenzregel(s):
    pool = AKT['pool']
    if pool in ('korrektur', 'sicherung') and AKT['nr'] == 0:
        return _gl_zwei_basen()
    if s == 1:
        b = R.choice([2, 3, 5, 10])
        a = R.choice([2, 3, 4, 5, 7]) if b == 10 else b
        r = R.randint(2, 15)
        if b != 10:
            # Stufe 1: nur ein Schritt (Basis gleich, log_b(b) = 1)
            return zahl(f'Berechne {lb(b)}({a}^{r}) mit der Potenzregel.', f'{lb(b)}({a}^{r}) = {r} · {lb(b)}({a}) = {r} · 1 = {r}.',
                        'Ziehe den Exponenten als Faktor vor den Logarithmus.', r, f'{r} + ({b} ** 1 - {a})')
        return luecken(f'Schreibe lg({a}^{r}) mit der Potenzregel als Vielfaches von lg {a}.', f'□ · lg {a}', 'Faktor', [r],
                       f'lg({a}^{r}) = {r} · lg {a}.', 'Der Exponent wird zum Faktor.', c=[str(r)])
    if s == 2 and R.random() < 0.35:
        # zwei Schritte: Potenzregel und log_b(a) mit a = b^k
        b = R.choice([2, 3, 5])
        k = R.randint(2, 3)
        a = b ** k
        r = R.randint(2, 9)
        return zahl(f'Berechne {lb(b)}({a}^{r}) mit der Potenzregel.', f'{lb(b)}({a}^{r}) = {r} · {lb(b)}({a}) = {r} · {k} = {r * k}.',
                    f'Ziehe den Exponenten vor und bestimme dann {lb(b)}({a}).', r * k, f'{r} * {k} + ({b} ** {k} - {a})')
    if s == 2:
        base, l = R.choice([(2, Fr(3010, 10000)), (3, Fr(4771, 10000)), (5, Fr(6990, 10000)), (7, Fr(8451, 10000))])
        r = R.randint(2, 6)
        return zahl(f'Es gilt lg {base} ≈ {dz(l)}. Berechne damit lg({base}^{r}) (ohne Taschenrechner).',
                    f'lg({base}^{r}) = {r} · lg {base} ≈ {r} · {dz(l)} = {dz(r * l)}.', 'Potenzregel: Exponent als Faktor.', r * l, f'{r} * {cf(l)}')
    typ = R.random()
    if typ < 0.6:
        return _gl_zwei_basen()
    a = R.randint(2, 9)
    return auswahl(f'Welche Umformung ist richtig (x > 0)?', f'lg(x^{a}) = {a} · lg x',
                   [f'lg({a}x) = {a} · lg x', f'lg(x^{a}) = (lg x)^{a}', f'lg(x + {a}) = lg x + lg {a}'],
                   f'Die Potenzregel holt nur den Exponenten einer Potenz heraus: lg(x^{a}) = {a} · lg x. Produkte und Summen sind etwas anderes.',
                   'Steht die Zahl als Exponent, als Faktor oder als Summand?')


def _eur(v):
    ganz, nach = f'{v:.2f}'.split('.')
    return f'{dz(int(ganz))},{nach}'


def _w_kapital():
    p = R.choice([2, 3, 4, 5, 6, 8])
    n = R.randint(2, 5)
    K0 = R.choice([1000, 2000, 2500, 5000, 10000])
    q = 1 + Fr(p, 100)
    Kn = float(K0 * q ** n)
    v = gerundet(Kn, 2)
    if v is None: return None
    return zahl(f'Ein Kapital von {dz(K0)} € wird mit {p} % pro Jahr verzinst (Zinseszins). Wie groß ist es nach {n} Jahren? Runde auf Cent.',
                f'K = {dz(K0)} · {dz(q)}^{n} ≈ {_eur(v)} €.', 'Wachstumsfaktor 1 + p/100, so oft multiplizieren wie Jahre vergehen.',
                v, f'round({K0} * {cf(q)} ** {n}, 2)', einheit='€', tol=0.01)


def _w_zeit_einfach():
    """q^t = k direkt nach der Erklärung (Stufe 1)."""
    p = R.choice([2, 3, 4, 5, 6, 8, 10])
    k = R.choice([Fr(3, 2), 2, 3, Fr(5, 4)])
    q = Fr(100 + p, 100)
    t = log(k) / log(q)
    v = gerundet(t, 1)
    if v is None: return None
    return zahl(f'Ein Betrag wächst jedes Jahr um {p} %. Löse {dz(q)}^t = {dz(k)}, um zu sehen, wann er das {dz(k)}-Fache erreicht hat. Runde auf eine Nachkommastelle.',
                f't = lg {dz(k)} : lg {dz(q)} ≈ {dz(v)} Jahre.', 'Logarithmiere beide Seiten: t = lg(rechte Seite) : lg(Basis).', v, f'round({K(t)}, 1)',
                einheit='Jahre', tol=0.1)


def _w_verdoppeln():
    p = R.choice([2, 3, 4, 5, 6, 8, 9])
    q = 1 + p / 100
    t = log(2) / log(q)
    n = ceil(t)
    if t - int(t) < 0.02: return None
    return zahl(f'Ein Guthaben wird mit {p} % pro Jahr verzinst. Nach wie vielen vollen Jahren hat es sich erstmals verdoppelt?',
                f'{dz(Fr(100 + p, 100))}^t = 2 ⇒ t = lg 2 : lg {dz(Fr(100 + p, 100))} ≈ {dz(round(t, 2))}, also nach {n} Jahren.',
                'Löse q^t = 2 und runde auf die nächste ganze Zahl nach oben.', n, f'-(-{K(t)} // 1)', einheit='Jahre')


def _w_zerfall_menge():
    T = R.choice([5, 8, 12, 20, 30])
    k = R.randint(2, 5)
    m0 = R.choice([80, 160, 200, 320, 400])
    m = Fr(m0, 2 ** k)
    if not endlich(m): return None
    return zahl(f'Ein radioaktiver Stoff hat eine Halbwertszeit von {T} Tagen. Anfangs sind {m0} mg vorhanden. Wie viel ist nach {T * k} Tagen noch da?',
                f'{T * k} Tage = {k} Halbwertszeiten: {m0} · 0,5^{k} = {dz(m)} mg.', 'Wie oft passt die Halbwertszeit in die Zeitspanne?', m,
                f'{m0} * 0.5 ** {k}', einheit='mg')


def _w_halbieren():
    p = R.choice([5, 10, 15, 20, 25, 30])
    q = 1 - p / 100
    t = log(0.5) / log(q)
    v = gerundet(t, 1)
    if v is None: return None
    return zahl(f'Der Wert eines Geräts nimmt jedes Jahr um {p} % ab. Nach wie vielen Jahren ist er auf die Hälfte gesunken (eine Nachkommastelle)?',
                f'{dz(Fr(100 - p, 100))}^t = 0,5 ⇒ t = lg 0,5 : lg {dz(Fr(100 - p, 100))} ≈ {dz(v)} Jahre.', 'Abnahme um p %: Faktor 1 − p/100.',
                v, f'round({K(t)}, 1)', einheit='Jahre', tol=0.1)


def _w_population():
    p = R.choice([3, 5, 8, 10, 12, 15, 20])
    N0, Z = R.choice([(1000, 5000), (500, 2000), (2000, 3000), (100, 1000), (40, 300)])
    q = 1 + p / 100
    t = log(Z / N0) / log(q)
    v = gerundet(t, 1)
    if v is None: return None
    return zahl(f'Eine Population wächst um {p} % pro Woche von {dz(N0)} auf {dz(Z)} Tiere. Nach wie vielen Wochen ist das der Fall (eine Nachkommastelle)?',
                f'{dz(N0)} · {dz(Fr(100 + p, 100))}^t = {dz(Z)} ⇒ t = lg({zt(Fr(Z, N0))}) : lg {dz(Fr(100 + p, 100))} ≈ {dz(v)} Wochen.',
                'Teile durch den Anfangswert, dann logarithmieren.', v, f'round({K(t)}, 1)', einheit='Wochen', tol=0.1)


def _w_medikament():
    T = R.choice([6, 8, 10, 25])
    rest = R.choice([10, 20, 30, 40, 60, 70])
    t = T * log(rest / 100) / log(0.5)
    v = gerundet(t, 1)
    if v is None: return None
    return zahl(f'Ein Medikament wird mit einer Halbwertszeit von {T} Stunden abgebaut. Nach welcher Zeit sind noch {rest} % vorhanden (eine Nachkommastelle)?',
                f'0,5^(t/{T}) = {dz(Fr(rest, 100))} ⇒ t = {T} · lg {dz(Fr(rest, 100))} : lg 0,5 ≈ {dz(v)} h.', 'Ansatz N₀ · 0,5^(t/T) und durch N₀ teilen.',
                v, f'round({K(t)}, 1)', einheit='h', tol=0.1)


def _w_halbwertszeit():
    """Halbwertszeit bestimmen – aus der Abnahmerate oder aus zwei Messwerten."""
    if R.random() < 0.5:
        p = R.choice([2, 3, 4, 5, 6, 8, 12])
        t = log(0.5) / log(1 - p / 100)
        v = gerundet(t, 1)
        if v is None: return None
        return zahl(f'Ein Stoff nimmt pro Tag um {p} % ab. Wie groß ist die Halbwertszeit? Runde auf eine Nachkommastelle.',
                    f'Faktor q = {dz(Fr(100 - p, 100))}. q^T = 0,5 ⇒ T = lg 0,5 : lg {dz(Fr(100 - p, 100))} ≈ {dz(v)} Tage.',
                    'Die Halbwertszeit ist die Zeit, nach der nur noch die Hälfte da ist: q^T = 0,5.', v, f'round({K(t)}, 1)', einheit='Tage', tol=0.1)
    m0 = R.choice([40, 80, 100, 120, 200])
    m1 = R.choice(list(range(m0 // 2 + 5, m0 - 4, 5)))
    d = R.choice([5, 6, 8, 10, 12])
    # q^d = m1/m0  ⇒  T = d · lg 0,5 / lg(m1/m0)
    t = d * log(0.5) / log(m1 / m0)
    v = gerundet(t, 1)
    if v is None or t > 200: return None
    return zahl(f'Von {m0} mg eines Stoffs sind nach {d} Tagen noch {m1} mg übrig. Wie groß ist die Halbwertszeit? Runde auf eine Nachkommastelle.',
                f'q^{d} = {m1} : {m0} = {zt(Fr(m1, m0))}. Die Halbwertszeit T erfüllt q^T = 0,5, also T = {d} · lg 0,5 : lg {zt(Fr(m1, m0))} ≈ {dz(v)} Tage.',
                'Bestimme zuerst, welcher Anteil nach der gegebenen Zeit übrig ist. Dann: Nach wie vielen Tagen ist es die Hälfte?',
                v, f'round({K(t)}, 1)', einheit='Tage', tol=0.1)


def _w_rate():
    """Wachstumsrate in % bestimmen (keine Zeitfrage)."""
    if R.random() < 0.5:
        K0 = R.choice([2000, 4000, 5000, 8000, 10000])
        f = R.choice([Fr(7, 5), Fr(13, 10), Fr(6, 5), Fr(3, 2), Fr(5, 4)])
        n = R.choice([5, 8, 10, 12, 15])
        K1 = K0 * f
        p = (float(f) ** (1 / n) - 1) * 100
        v = gerundet(p, 1)
        if v is None: return None
        return zahl(f'Ein Kapital wächst mit Zinseszins in {n} Jahren von {dz(K0)} € auf {dz(K1)} €. Wie hoch ist der Zinssatz? Runde auf eine Nachkommastelle.',
                    f'q^{n} = {dz(K1)} : {dz(K0)} = {dz(f)} ⇒ q = {dz(f)}^(1/{n}) ≈ {dz(round(1 + p / 100, 4))}, also p ≈ {dz(v)} %.',
                    'Bestimme den Wachstumsfaktor q pro Jahr; der Zinssatz ist q − 1 in Prozent.', v, f'round({K(p)}, 1)', einheit='%', tol=0.1)
    k, wort = R.choice([(2, 'verdoppelt'), (3, 'verdreifacht'), (4, 'vervierfacht')])
    n = R.choice([3, 4, 5, 6, 8])
    p = (k ** (1 / n) - 1) * 100
    v = gerundet(p, 1)
    if v is None: return None
    return zahl(f'Eine Bakterienkultur {wort} sich in {n} Stunden. Um wie viel Prozent wächst sie pro Stunde? Runde auf eine Nachkommastelle.',
                f'q^{n} = {k} ⇒ q = {k}^(1/{n}) ≈ {dz(round(1 + p / 100, 4))}, also Wachstum ≈ {dz(v)} % pro Stunde.',
                'Gesucht ist der Faktor q pro Stunde: q hoch Stundenzahl ergibt die Vervielfachung.', v, f'round({K(p)}, 1)', einheit='%', tol=0.1)


def g_wachstum(s):
    # Regel der Prüfung: mindestens die Hälfte der Aufgaben je Pool fragt nach der Zeit t.
    pool, nr = AKT['pool'], AKT['nr']
    if pool != 'uebung':
        if nr % 2 == 0:
            return R.choice([_w_verdoppeln, _w_halbieren, _w_medikament, _w_population, _w_halbwertszeit])()
        return R.choice([_w_kapital, _w_zerfall_menge, _w_rate])()
    if s == 1:
        return _w_zeit_einfach() if nr % 2 == 0 else _w_kapital()
    if s == 2:
        return _w_zerfall_menge() if nr % 3 == 0 else R.choice([_w_verdoppeln, _w_halbieren])()
    if nr % 3 == 2:
        return _w_rate()
    return R.choice([_w_population, _w_medikament, _w_halbwertszeit])()


def g_verstehen(s):
    typ = R.choice({1: 'abc', 2: 'abcde', 3: 'def'}[s])
    if typ == 'a':
        b = R.choice([2, 3, 5, 10, 7])
        return auswahl(f'Welchen Wert hat {lb(b)}(1)?', '0', ['1', str(b), 'nicht definiert'],
                       f'{b}⁰ = 1, also {lb(b)}(1) = 0.', 'Welcher Exponent macht jede Basis zu 1?')
    if typ == 'b':
        b = R.choice([2, 3, 5, 10])
        n = R.randint(2, 6)
        a = auswahl(f'Welche Lösung hat {b}^x = −{dz(b ** n)}? Die Zeichnung zeigt y = {b}^x und y = −{dz(b ** n)}.', 'keine Lösung', [f'x = −{n}', f'x = {n}', f'x = −1/{n}'],
                    f'{b}^x ist für jedes x positiv ({b}^(−{n}) = 1/{dz(b ** n)}). Die Gerade y = −{dz(b ** n)} wird nie geschnitten.',
                    'Kann eine Potenz mit positiver Basis negativ sein?')
        return mit_grafik(a, koord([{'art': 'exp', 'a': 1, 'b': b}], x=(-4, 4), y=(-(b ** n) * 1.25, b ** n * 1.25), waagrecht=[-(b ** n)]))
    if typ == 'c':
        b = R.choice([2, 3, 4, 5])
        n = R.randint(2, 5)
        falsch_wert = b ** (n - 1)
        if falsch_wert == n: return None
        ablenker = [w for w in (b ** (2 * n), n - 1, n + 1) if w not in (falsch_wert, n)]
        return auswahl(f'Jemand rechnet {lb(b)}({dz(b ** n)}) = {dz(b ** n)} : {b} = {dz(falsch_wert)}. Was stimmt?', f'Falsch, {lb(b)}({dz(b ** n)}) = {n}',
                       ['Richtig'] + [f'Falsch, {lb(b)}({dz(b ** n)}) = {dz(w)}' for w in ablenker],
                       f'Gesucht ist der Exponent: {pt(b, n)} = {dz(b ** n)}.', 'Wonach fragt der Logarithmus?')
    if typ == 'd':
        a, b = R.randint(2, 5), R.choice([2, 3, 5])
        c = R.randint(10, 99)
        return auswahl(f'Jemand formt {a} · {b}^x = {c} um zu {a * b}^x = {c}. Was stimmt?', f'Falsch: Erst durch {a} teilen: {b}^x = {zt(Fr(c, a))}.',
                       ['Richtig', f'Falsch: Es muss {b}^x = {c - a} heißen.', f'Falsch: Es muss {b}^({a}x) = {c} heißen.'],
                       f'{a} · {b}^x ist ein Produkt; der Faktor {a} gehört nicht zur Basis. Richtig ist {b}^x = {c} : {a}.',
                       'Was wird zuerst gerechnet: Potenz oder Multiplikation?')
    if typ == 'e':
        a, b = R.randint(2, 9), R.randint(2, 9)
        if a == b: return None
        return auswahl(f'Welche Aussage ist falsch?', f'lg({a} + {b}) = lg {a} + lg {b}',
                       [f'lg({a}^{b}) = {b} · lg {a}', 'lg 10 = 1', 'lg 1 = 0'],
                       f'Für Summen gibt es keine solche Regel: lg({a + b}) ≈ {dz(round(lg(a + b), 3))}, aber lg {a} + lg {b} ≈ {dz(round(lg(a) + lg(b), 3))}.',
                       'Prüfe jede Aussage mit dem Taschenrechner.')
    p = R.choice([3, 4, 5, 6, 8])
    return auswahl(f'Ein Betrag wächst jährlich um {p} %. Welche Gleichung beschreibt, wann er sich verdreifacht hat?', f'{dz(Fr(100 + p, 100))}^t = 3',
                   [f'{p}^t = 3', f'{dz(Fr(p, 100))}^t = 3', f'1 + {p}t = 3'],
                   f'Wachstumsfaktor q = 1 + {p}/100 = {dz(Fr(100 + p, 100))}; verdreifacht: q^t = 3.', 'Wie lautet der Wachstumsfaktor bei p % Zunahme?')


GEN = {'logarithmus': g_logarithmus, 'gleiche_basis': g_gleiche_basis, 'mit_log_loesen': g_mit_log_loesen, 'potenzregel': g_potenzregel,
       'wachstum': g_wachstum, 'verstehen': g_verstehen}

# ---------- KLAR: verständliche Fassung der Lernkarten (Runde 7) ----------
# Wird erst nach dem Bauen der Aufgaben eingesetzt (bauen(..., klar=KLAR)), die Aufgaben bleiben wörtlich gleich.
KLAR = {
 'logarithmus': {
  'einstieg': 'In einer Schale mit Nährlösung verdoppeln sich Bakterien jede Stunde. Aus 1 Bakterium werden 2, dann 4, 8, 16 und 32. '
              'Wie viele Stunden hat es gedauert, bis es 32 sind? Du zählst, wie oft mit 2 malgenommen wurde: 5-mal, also 5 Stunden. '
              'Diese Anzahl heißt ⟦Logarithmus⟧.',
  'woerter': [['2⁵', 'Potenz: 2 · 2 · 2 · 2 · 2 = 32 – die 2 wird 5-mal malgenommen'],
              ['Basis', 'die Zahl, die immer wieder malgenommen wird (hier 2: Verdoppeln)'],
              ['Exponent', 'die kleine hochgestellte Zahl: wie oft malgenommen wird (hier 5 Stunden)'],
              ['log₂(32)', 'gelesen „Logarithmus von 32 zur Basis 2“: der Exponent, mit dem aus 2 die 32 wird'],
              ['b^y', '„b hoch y“: b wird y-mal malgenommen (b und y stehen für irgendwelche Zahlen)'],
              ['log_b(x)', 'allgemein: der Exponent, mit dem aus der Basis b die Zahl x wird'],
              ['⇔', '„ist gleichbedeutend mit“: beide Aussagen sagen dasselbe'],
              ['≠', '„ist nicht gleich“'],
              ['lg', 'Logarithmus zur Basis 10, Taste „log“ am Taschenrechner: lg 1 000 = 3, weil 10³ = 1 000']],
  'bild': {'typ': 'koordinaten', 'x': [-1, 6], 'y': [0, 36], 'graphen': [{'art': 'exp', 'a': 1, 'b': 2, 'name': 'y = 2ˣ'}],
           'punkte': [{'x': 5, 'y': 32, 'name': 'nach 5 h: 32'}], 'strecken': [[5, 0, 5, 32, 'gestrichelt'], [0, 32, 5, 32, 'gestrichelt']],
           'name_x': 'Stunden', 'name_y': 'Bakterien'},
  'schritte': ['Gesucht ist log₂(32). Die Frage dahinter lautet: 2 hoch wie viel ergibt 32?',
               'Nimm die 2 so lange mit 2 mal, bis 32 erreicht ist: 2, 4, 8, 16, 32.',
               'Das waren fünf Zweien, also gilt 2⁵ = 32.',
               'Der gesuchte Exponent ist 5: ⟦log₂(32) = 5⟧. Die Bakterien haben 5 Stunden gebraucht.'],
  'regel': 'So berechnest du log_b(x): Frage, mit welchem ⟦Exponenten⟧ man die Basis b potenzieren muss, damit x herauskommt. '
           'Kurz: ⟦b^y = x ⇔ y = log_b(x)⟧. Das geht nur für b > 0, b ≠ 1 und x > 0. lg ist der Logarithmus zur Basis 10.',
  'fehler': 'log₂(32) = 32 : 2 = 16 ist falsch. 16 wäre die Zahl der Bakterien eine Stunde früher. Der Logarithmus fragt nach der '
            '⟦Anzahl der Verdopplungen⟧, also nach dem Exponenten: 5.'},
 'gleiche_basis': {
  'einstieg': 'Bei einem Kettenbrief schreibt eine Person den ersten Brief. Wer einen Brief bekommt, schickt ihn an 3 neue Leute weiter. '
              'Auf Stufe 1 gibt es also 1 Brief, auf Stufe 2 sind es 3, auf Stufe 3 sind es 9, auf Stufe 4 sind es 27 – jede Stufe dreimal so viele. '
              'Auf welcher Stufe sind es 81 Briefe? Schreibt man 81 als ⟦Potenz mit derselben Basis⟧ 3, kann man die Stufe ablesen.',
  'woerter': [['x', 'die gesuchte Zahl, hier die Stufe'],
              ['3^(x − 1)', '3 hoch (x − 1): die Zahl der Briefe auf Stufe x (Stufe 1: 3⁰ = 1, Stufe 2: 3¹ = 3 …)'],
              ['3⁰ = 1', 'eine Zahl hoch 0 ergibt immer 1'],
              ['gleiche Basis', 'beide Seiten der Gleichung als Potenz derselben Zahl schreiben, hier 3'],
              ['Exponenten gleichsetzen', 'sind Basis und Ergebnis gleich, müssen auch die Exponenten gleich sein'],
              ['b^u = b^v ⇔ u = v', 'dieselbe Regel allgemein: gleiche Basis b, gleiches Ergebnis, also gleiche Exponenten u und v']],
  'schritte': ['Die Gleichung lautet 3^(x − 1) = 81. Links steht eine Potenz mit der Basis 3.',
               'Schreibe auch 81 als Potenz von 3: 3 · 3 · 3 · 3 = 81, also 81 = 3⁴.',
               'Jetzt steht da 3^(x − 1) = 3⁴. Die Basis ist gleich, also müssen die Exponenten gleich sein: x − 1 = 4.',
               'Auf beiden Seiten 1 dazuzählen: ⟦x = 5⟧. Auf Stufe 5 sind es 81 Briefe.'],
  'regel': 'So löst du solche Gleichungen: Schreibe beide Seiten als Potenzen ⟦derselben Basis⟧. Dann ⟦setze die Exponenten gleich⟧ '
           '(b^u = b^v ⇔ u = v) und löse die Gleichung, die dabei entsteht.',
  'fehler': '3^(x − 1) = 81 ⇒ x − 1 = 81 : 3 = 27 ist falsch. 27 ist die Zahl der Briefe eine Stufe vorher, nicht die Stufe selbst. '
            'Verglichen werden die ⟦Exponenten⟧ – dazu muss 81 erst als 3⁴ geschrieben werden.'},
 'mit_log_loesen': {
  'einstieg': 'Zurück zu den Bakterien. Diesmal liegen am Anfang 3 Bakterien in der Schale, und sie verdoppeln sich wieder jede Stunde. '
              'Nach 3 Stunden sind es 24, nach 4 Stunden schon 48. Wann genau sind es 30? Die Antwort liegt zwischen 3 und 4 Stunden. '
              'Ausrechnen kann man sie, wenn man beide Seiten der Gleichung ⟦logarithmiert⟧.',
  'woerter': [['3 · 2^x', '3 Bakterien am Anfang, x Stunden lang verdoppelt'],
              ['Potenz allein stellen', 'so umformen, dass auf einer Seite nur noch 2^x steht'],
              ['logarithmieren', 'den Logarithmus der Zahl bilden, um den Exponenten zu bekommen'],
              ['lg 10 : lg 2', 'so rechnet der Taschenrechner log₂(10) aus: lg der Zahl geteilt durch lg der Basis'],
              ['log_b(c) = lg c : lg b', 'die Umrechnung allgemein: jeden Logarithmus mit der lg-Taste berechnen'],
              ['≈', '„ungefähr gleich“ – das Ergebnis ist gerundet']],
  'bild': {'typ': 'koordinaten', 'x': [-1, 5], 'y': [0, 16], 'graphen': [{'art': 'exp', 'a': 1, 'b': 2, 'name': 'y = 2ˣ'}],
           'punkte': [{'x': 3.32, 'y': 10, 'name': 'x ≈ 3,32'}], 'waagrecht': [10], 'name_x': 'Stunden'},
  'schritte': ['Die Gleichung 3 · 2^x = 30 bedeutet: 3 Bakterien, x Stunden lang verdoppelt, ergeben 30.',
               'Zuerst die Potenz allein stellen: Beide Seiten durch 3 teilen ergibt 2^x = 10.',
               '10 ist keine Potenz von 2, denn 2³ = 8 und 2⁴ = 16. Also liegt x zwischen 3 und 4.',
               'Mit dem Logarithmus ausrechnen: x = log₂(10) = lg 10 : lg 2 ≈ ⟦3,32⟧. Nach gut 3 Stunden sind es 30 Bakterien.'],
  'regel': 'So löst du b^x = c, wenn keine gemeinsame Basis passt: Erst die Potenz ⟦allein stellen⟧, dann ⟦logarithmieren⟧: '
           '⟦x = log_b(c) = lg c : lg b⟧. Das Ergebnis sinnvoll runden.',
  'fehler': '3 · 2^x = 30 ⇒ 6^x = 30 ist falsch. Verdoppelt wird nur die 2 – die 3 ist die Anzahl am Anfang und wird nicht mit hochgenommen. '
            '3 · 2^x ist nicht (3 · 2)^x. Erst ⟦durch 3 teilen⟧, dann logarithmieren.'},
 'potenzregel': {
  'einstieg': 'In zwei Schalen wachsen verschiedene Bakterien. In Schale A liegt anfangs 1 Bakterium, und jede Stunde werden es fünfmal so viele. '
              'In Schale B liegen anfangs 2, und sie verdoppeln sich jede Stunde. A holt B bald ein – aber wann genau? '
              'Die gesuchte Zeit steht jetzt auf beiden Seiten oben im Exponenten. Herunter holt man sie mit der ⟦Potenzregel für Logarithmen⟧.',
  'woerter': [['5^x', 'Anzahl in Schale A nach x Stunden'],
              ['2^(x + 1)', 'gleich 2 · 2^x: Anzahl in Schale B nach x Stunden'],
              ['Faktor', 'eine Zahl, mit der malgenommen wird'],
              ['Potenzregel', 'lg(a^r) = r · lg(a): ein Exponent im Logarithmus darf als Faktor nach vorn'],
              ['log_b(a^r) = r · log_b(a)', 'dieselbe Regel für jede Basis b'],
              ['ausmultiplizieren', 'eine Klammer auflösen: (x + 1) · lg 2 = x · lg 2 + lg 2']],
  'schritte': ['Gleich viele Bakterien heißt: 5^x = 2^(x + 1). Auf beiden Seiten steht x im Exponenten.',
               'Nimm auf beiden Seiten den lg. Mit der Potenzregel wandern die Exponenten als Faktoren nach vorn: x · lg 5 = (x + 1) · lg 2.',
               'Rechts ausmultiplizieren und alles mit x nach links bringen: x · lg 5 − x · lg 2 = lg 2, also x · (lg 5 − lg 2) = lg 2.',
               'Durch die Klammer teilen: x = lg 2 : (lg 5 − lg 2) ≈ ⟦0,76⟧. Nach etwa einer Dreiviertelstunde sind es in beiden Schalen gleich viele.'],
  'regel': 'Ein Exponent im Logarithmus wird zum ⟦Faktor⟧: ⟦log_b(a^r) = r · log_b(a)⟧. So gehst du vor: beide Seiten logarithmieren, '
           'die Exponenten als Faktoren nach vorn holen, nach x auflösen. Warum es stimmt: Ist a = b^y, dann ist a^r = b^(r · y), '
           'also log_b(a^r) = r · y = r · log_b(a).',
  'fehler': 'lg(5x) = x · lg 5 ist falsch. Die Potenzregel gilt nur für ⟦Potenzen⟧ wie 5^x (die 5 wird x-mal malgenommen), '
            'nicht für Produkte wie 5x (5 mal x).'},
 'wachstum': {
  'einstieg': 'Oma legt 1 000 € auf ein Sparkonto mit 4 % Zinsen pro Jahr. Die Zinsen bleiben auf dem Konto und bringen im nächsten Jahr selbst wieder Zinsen. '
              'Nach einem Jahr sind es 1 040 €, nach zwei Jahren 1 081,60 €. Wann sind es 1 500 €? '
              'Das Konto wird jedes Jahr mit derselben Zahl malgenommen – so etwas heißt ⟦exponentielles Wachstum⟧.',
  'woerter': [['Zinseszins', 'Zinsen, die selbst wieder Zinsen bringen'],
              ['Wachstumsfaktor q', 'die Zahl, mit der jedes Jahr malgenommen wird: bei +4 % ist q = 1,04'],
              ['p', 'der Prozentsatz als Dezimalzahl: 4 % = 0,04'],
              ['N₀', 'der Anfangswert (hier 1 000 €); die kleine 0 heißt „zum Zeitpunkt 0“'],
              ['t', 'die Zeit, hier in Jahren'],
              ['N(t) = N₀ · q^t', 'der Wert nach t Jahren'],
              ['Zerfall', 'Abnahme um einen festen Prozentsatz; dann ist q = 1 − p kleiner als 1']],
  'bild': {'typ': 'koordinaten', 'x': [0, 15], 'y': [0, 2000], 'graphen': [{'art': 'exp', 'a': 1000, 'b': 1.04, 'bereich': [0, 15]}],
           'waagrecht': [1500], 'senkrecht': [10.34], 'name_x': 't (Jahre)', 'name_y': 'Konto (€)', 'schritt_y': 250},
  'schritte': ['Nach t Jahren sind 1 000 · 1,04^t Euro auf dem Konto. Gesucht ist t mit 1 000 · 1,04^t = 1 500.',
               'Durch 1 000 teilen, damit die Potenz allein steht: 1,04^t = 1,5.',
               'Logarithmieren: t = lg 1,5 : lg 1,04 ≈ 10,34.',
               'Zinsen gibt es nur am Jahresende. Nach 10 Jahren sind es erst etwa 1 480 €, deshalb sind die 1 500 € nach ⟦11 vollen Jahren⟧ erreicht.'],
  'regel': 'So findest du den Zeitpunkt t: Ansatz ⟦N₀ · q^t = Ziel⟧ aufschreiben (Zunahme um p: q = 1 + p, Abnahme um p: q = 1 − p), '
           'durch N₀ teilen und logarithmieren: ⟦t = lg(Ziel : N₀) : lg q⟧.',
  'fehler': 'Bei 4 % Zinsen q = 4 oder q = 0,04 zu nehmen ist falsch. Mit 4 würde das Geld jedes Jahr vervierfacht, mit 0,04 bliebe nur ein winziger Rest. '
            'Der ⟦Wachstumsfaktor⟧ ist q = 1,04: das ganze Geld (1) plus 4 % (0,04).'},
 'verstehen': {
  'einstieg': 'Bei den Bakterien wird die Zahl jede Stunde größer. Rechnet man rückwärts, halbiert sie sich jede Stunde: 1, ½, ¼ … '
              'Sie wird immer kleiner, aber nie null und nie negativ. Deshalb gibt es Gleichungen mit Potenzen, die ⟦keine Lösung⟧ haben, '
              'und Zahlen, von denen es keinen Logarithmus gibt.',
  'woerter': [['2^(−3)', 'ein Minus im Exponenten bedeutet Kehrwert: 2^(−3) = 1/2³ = 1/8'],
              ['Kehrwert', '1 geteilt durch die Zahl, zum Beispiel ist 1/8 der Kehrwert von 8'],
              ['keine Lösung', 'es gibt keine Zahl, die man für x einsetzen kann, damit die Gleichung stimmt'],
              ['log_b(1) = 0', 'jede Basis hoch 0 ergibt 1'],
              ['log_b(b) = 1', 'jede Basis hoch 1 ergibt sich selbst'],
              ['Graph von y = 2^x', 'die Kurve, die zu jedem x den Wert 2^x zeigt']],
  'schritte': ['Behauptung: 2^x = −8 hat die Lösung x = −3.',
               'Probe: 2^(−3) ist der Kehrwert von 2³, also 1/8. Das ist positiv und nicht −8.',
               'Egal welches x man einsetzt, 2^x ist immer größer als 0. Der Graph von y = 2^x bleibt ganz über der x-Achse.',
               'Also hat 2^x = −8 ⟦keine Lösung⟧, und die Behauptung ist falsch.'],
  'regel': 'So prüfst du Aussagen über Logarithmen: Einen Logarithmus gibt es nur von Zahlen ⟦größer als 0⟧. '
           'Merke ⟦log_b(1) = 0⟧ und ⟦log_b(b) = 1⟧. Für Summen gibt es keine Regel: lg(a + b) ist nicht lg a + lg b.',
  'fehler': '„Bei 2^x = −8 ist x = −3“ ist falsch. Ein Minus im Exponenten macht die Zahl nicht negativ, es bildet den ⟦Kehrwert⟧ – '
            'wie bei den Bakterien rückwärts: Es werden weniger, aber nie weniger als null.'},
}

GEN = schoen(GEN)

if __name__ == '__main__':
    bauen('gleichungen.exponential',
          'Logarithmen verstehen und Exponentialgleichungen lösen – mit gleicher Basis oder durch Logarithmieren mit der Potenzregel, auch bei Wachstum und Zerfall.',
          ['b^y = x ⇔ y = log_b(x); lg = log₁₀.', 'Gleiche Basis: Exponenten gleichsetzen.', 'Sonst: Potenz allein stellen, logarithmieren: x = lg c : lg b.',
           'Potenzregel: log_b(a^r) = r · log_b(a).'],
          [('Logarithmus', ['logarithmus', 'gleiche_basis']), ('Lösen mit dem Logarithmus', ['mit_log_loesen', 'potenzregel']),
           ('Anwenden und Verstehen', ['wachstum', 'verstehen'])],
          ETAPPEN, GEN, klar=KLAR,
          meiden={'logarithmus': ['log₂(32).'], 'gleiche_basis': ['3^(x − 1) = 81.'], 'mit_log_loesen': ['3 · 2^x = 30'],
                  'potenzregel': ['5^x = 2^(x + 1)'], 'wachstum': ['4 % pro Jahr verzinst (Zinseszins). Wie groß'], 'verstehen': ['2^x = −8']},
          offen=['Zeichnungen: Lernkarten „logarithmus“, „mit_log_loesen“, „wachstum“ und „verstehen“ haben ein Koordinatensystem; Aufgaben zum Abschätzen (Stufe 1 „mit_log_loesen“) und zu „keine Lösung“ zeigen den Graphen. Die Exponenten heißen in den Graphnamen „2^x“ (Text).',
                 'Nur die Potenzregel für Logarithmen (lehrplan_gym). Produkt- und Quotientenregel sind bewusst nicht enthalten.',
                 'Rechenausdruck c bei exakten Logarithmen: prüft b^n = x (z. B. „5 + (2 ** 5 − 32)“), weil das Prüfskript keinen Logarithmus kennt; gerundete Lösungen als 12-stellige Konstante mit Toleranz 0,01 bzw. 0,1.',
                 'Schreibweise: Exponenten mit Unbekannten als „2^x“ bzw. „3^(x − 1)“, Logarithmus als „log₂(32)“ und „lg“.',
                 'Prüfung eingearbeitet (Runde 3): Potenzregel begründet; neue Aufgabentypen Basis/Argument bestimmen, Kehrwert-Exponenten, gemeinsame Basis mit Verschiebung, Halbwertszeit und Wachstumsrate bestimmen. „wachstum“: in jedem Pool mindestens die Hälfte Zeitfragen; Geldbeträge auf Cent mit Toleranz 0,01.'])
