#!/usr/bin/env python3
"""Thema gleichungen.exponential – Exponentialgleichungen (Klasse 10). Schreibt inhalte/themen/gleichungen.exponential.json."""
import sys
import math
from math import ceil, log
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import *  # noqa: E402,F403
from _schwer_kl10 import ergaenzen  # noqa: E402

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

# ---------- KLAR: Lernkarten im neuen Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst nach dem Bauen der Aufgaben eingesetzt (bauen(..., klar=KLAR)), die Aufgaben bleiben wörtlich gleich.
# Muster: einstieg (≤ 35 Wörter) → Kartenbild → Schritte als {text, bild} (Bildergeschichte) → „Pass auf!“ (fehler + fehler_bild) → MERKE (regel).
_BAKT = {'typ': 'koordinaten', 'x': [0, 6], 'y': [0, 36], 'graphen': [{'art': 'exp', 'a': 1, 'b': 2, 'name': 'Bakterien'}],
         'name_x': 'Stunden', 'name_y': 'Anzahl', 'schritt_y': 4}
_DREI = {'typ': 'koordinaten', 'x': [0, 5], 'y': [0, 60], 'graphen': [{'art': 'exp', 'a': 3, 'b': 2, 'name': '3 · 2ˣ'}],
         'waagrecht': [30], 'name_x': 'Stunden', 'name_y': 'Anzahl', 'schritt_y': 10}
_KONTO = {'typ': 'koordinaten', 'x': [0, 15], 'y': [0, 2000], 'graphen': [{'art': 'exp', 'a': 1000, 'b': 1.04, 'bereich': [0, 15], 'name': 'Konto'}],
          'waagrecht': [1500], 'name_x': 'Jahre', 'name_y': '€', 'schritt_y': 500}
KLAR = {
 'logarithmus': {
  'einstieg': 'Bakterien verdoppeln sich jede Stunde: Aus 1 werden 2, 4, 8, 16, 32. Wie viele Stunden dauert es bis 32? '
              'Diese Anzahl der Verdopplungen heißt ⟦Logarithmus⟧.',
  'woerter': [['Logarithmus', 'die Hochzahl, mit der aus der Basis die Zahl wird: log₂(32) = 5'],
              ['Basis', 'die Zahl, die immer wieder malgenommen wird, hier 2'],
              ['Exponent', 'die kleine Hochzahl: wie oft malgenommen wird']],
  'bild': _BAKT,
  'schritte': [{'text': 'Gesucht ist log₂(32): 2 hoch wie viel ergibt 32? Die Basis ist 2.',
                'bild': {'punkte': [{'x': 0, 'y': 1, 'name': 'Start: 1'}]}},
               {'text': 'Verdoppeln, bis 32 erreicht ist: 2, 4, 8, 16, 32.',
                'bild': {'punkte': [{'x': 0, 'y': 1}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}, {'x': 3, 'y': 8}, {'x': 4, 'y': 16}, {'x': 5, 'y': 32}]}},
               {'text': 'Das waren fünf Verdopplungen, also 2⁵ = 32. Der Exponent ist 5.'},
               {'text': 'Also ⟦log₂(32) = 5⟧: Nach 5 Stunden sind es 32.',
                'bild': {'punkte': [{'x': 5, 'y': 32, 'name': '5 h: 32'}], 'strecken': [[5, 0, 5, 32, 'gestrichelt'], [0, 32, 5, 32, 'gestrichelt']]}}],
  'fehler': 'log₂(32) = 32 : 2 = 16 ist falsch. 16 Bakterien gab es eine Stunde vorher. Gesucht ist die ⟦Anzahl der Verdopplungen⟧: 5.',
  'fehler_bild': {'punkte': [{'x': 4, 'y': 16, 'name': '16: vorher'}, {'x': 5, 'y': 32, 'name': '32'}]},
  'regel': 'Der Logarithmus ist der Exponent, der aus b die Zahl x macht. Es gilt ⟦b^y = x ⇔ y = log_b(x)⟧.'},
 'gleiche_basis': {
  'einstieg': 'Bei einem Kettenbrief schickt jeder den Brief an 3 neue Leute. Auf den Stufen gibt es 1, 3, 9, 27, 81 Briefe. '
              'Auf welcher Stufe sind es 81? Das zeigt eine Potenz mit ⟦gleicher Basis⟧.',
  'woerter': [['gleiche Basis', 'beide Seiten als Potenz derselben Zahl schreiben, hier 3'],
              ['Exponenten gleichsetzen', 'gleiche Basis und gleiches Ergebnis: dann sind auch die Hochzahlen gleich']],
  'bild': {'typ': 'tabelle', 'kopf': ['Stufe', '1', '2', '3', '4', '5'], 'zeilen': [['Briefe', '1', '3', '9', '27', '81']]},
  'schritte': [{'text': 'Auf Stufe x gibt es 3^(x − 1) Briefe. Gesucht: 3^(x − 1) = 81.'},
               {'text': '81 als Potenz von 3 schreiben: 81 = 3⁴.',
                'bild': {'zeilen': [['Briefe', '1', '3', '9', '27', '81'], ['Potenz', '3⁰', '3¹', '3²', '3³', '3⁴']]}},
               {'text': 'Gleiche Basis 3 auf beiden Seiten. Also Exponenten gleichsetzen: x − 1 = 4.'},
               {'text': 'Auf beiden Seiten 1 addieren: ⟦x = 5⟧. Auf Stufe 5 sind es 81.'}],
  'fehler': 'x − 1 = 81 : 3 = 27 ist falsch. 27 Briefe gab es eine Stufe vorher. Verglichen werden die ⟦Exponenten⟧, also erst 81 = 3⁴ schreiben.',
  'fehler_bild': {'zeilen': [['Briefe', '1', '3', '9', '27 = vorher', '81']]},
  'regel': 'Schreibe beide Seiten als Potenz derselben Basis. Dann ⟦setze die Exponenten gleich⟧: b^u = b^v ⇔ u = v.'},
 'mit_log_loesen': {
  'einstieg': 'Diesmal starten 3 Bakterien und verdoppeln sich jede Stunde. Nach 3 Stunden sind es 24, nach 4 Stunden 48. '
              'Wann sind es genau 30? Das findet man durch ⟦Logarithmieren⟧.',
  'woerter': [['logarithmieren', 'den Logarithmus bilden, um an den Exponenten zu kommen'],
              ['lg', 'Logarithmus zur Basis 10, Taste „log“ am Taschenrechner'],
              ['≈', 'ungefähr gleich, also gerundet']],
  'bild': _DREI,
  'schritte': [{'text': '3 · 2^x = 30 heißt: 3 Bakterien, x Stunden verdoppelt, ergeben 30.'},
               {'text': 'Zuerst durch 3 teilen, damit die Potenz allein steht: 2^x = 10.'},
               {'text': '2³ = 8 und 2⁴ = 16. Also liegt x zwischen 3 und 4.',
                'bild': {'punkte': [{'x': 3, 'y': 24, 'name': '3 h: 24'}, {'x': 4, 'y': 48, 'name': '4 h: 48'}]}},
               {'text': 'Logarithmieren: x = lg 10 : lg 2 ≈ ⟦3,32⟧ Stunden.',
                'bild': {'punkte': [{'x': 3.32, 'y': 30, 'name': '≈ 3,32 h'}], 'senkrecht': [3.32]}}],
  'fehler': '3 · 2^x = 30 ⇒ 6^x = 30 ist falsch. Nur die 2 wird verdoppelt, die 3 ist der Anfang. Erst ⟦durch 3 teilen⟧.',
  'fehler_bild': {'graphen': [{'art': 'exp', 'a': 3, 'b': 2, 'name': '3 · 2ˣ'}, {'art': 'exp', 'a': 1, 'b': 6, 'name': '6ˣ ≠'}]},
  'regel': 'Erst die Potenz allein stellen, dann logarithmieren. Für b^x = c gilt ⟦x = lg c : lg b⟧.'},
 'potenzregel': {
  'einstieg': 'In Schale A werden aus 1 Bakterium jede Stunde fünfmal so viele. In Schale B verdoppeln sich 2 Bakterien jede Stunde. '
              'Wann sind es gleich viele? Dafür braucht man die ⟦Potenzregel⟧.',
  'woerter': [['Potenzregel', 'lg(a^r) = r · lg a: der Exponent darf als Faktor nach vorn'],
              ['Faktor', 'eine Zahl, mit der malgenommen wird']],
  'bild': {'typ': 'koordinaten', 'x': [0, 1.5], 'y': [0, 12], 'name_x': 'Stunden', 'name_y': 'Anzahl',
           'graphen': [{'art': 'exp', 'a': 1, 'b': 5, 'name': 'A: 5ˣ'}, {'art': 'exp', 'a': 2, 'b': 2, 'name': 'B: 2 · 2ˣ'}]},
  'schritte': [{'text': 'Gleich viele heißt: 5^x = 2^(x + 1).'},
               {'text': 'Auf beiden Seiten lg nehmen. Der Exponent wandert als Faktor nach vorn.'},
               {'text': 'Das ergibt x · lg 5 = (x + 1) · lg 2.'},
               {'text': 'Alles mit x nach links: x · (lg 5 − lg 2) = lg 2.'},
               {'text': 'Teilen: x = lg 2 : (lg 5 − lg 2) ≈ ⟦0,76⟧ Stunden.',
                'bild': {'punkte': [{'x': 0.76, 'y': 3.4, 'name': 'gleich viele'}], 'senkrecht': [0.76]}}],
  'fehler': 'lg(5x) = x · lg 5 ist falsch. Die Potenzregel gilt nur für ⟦Potenzen⟧ wie 5^x, nicht für Produkte wie 5 · x.',
  'regel': 'Ein Exponent im Logarithmus wird zum Faktor. Es gilt ⟦log_b(a^r) = r · log_b(a)⟧, denn a^r = b^(r · log_b a).'},
 'wachstum': {
  'einstieg': 'Oma legt 1 000 € mit 4 % Zinseszins an. Jedes Jahr wird das Konto mit 1,04 malgenommen. '
              'Wann sind es 1 500 €? Die Zahl 1,04 heißt ⟦Wachstumsfaktor⟧.',
  'woerter': [['Zinseszins', 'Zinsen, die im nächsten Jahr selbst wieder Zinsen bringen'],
              ['Wachstumsfaktor', 'die Zahl, mit der jedes Jahr malgenommen wird: 100 % + 4 % = 1,04'],
              ['t', 'die Zeit in Jahren']],
  'bild': _KONTO,
  'schritte': [{'text': 'Nach t Jahren: 1 000 · 1,04^t €.'},
               {'text': 'Gesucht ist t mit 1 000 · 1,04^t = 1 500.'},
               {'text': 'Durch 1 000 teilen: 1,04^t = 1,5.'},
               {'text': 'Logarithmieren: t = lg 1,5 : lg 1,04 ≈ 10,34.', 'bild': {'senkrecht': [10.34]}},
               {'text': 'Zinsen gibt es am Jahresende. ⟦Nach 11 Jahren⟧ sind 1 500 € erreicht.',
                'bild': {'x': [8, 13], 'y': [1300, 1700], 'schritt_y': 100,
                         'punkte': [{'x': 10, 'y': 1480, 'name': '10 J.: 1 480 €'}, {'x': 11, 'y': 1539, 'name': '11 J.: 1 539 €'}]}}],
  'fehler': 'Der Faktor ist nicht 0,04. Dann blieben nach einem Jahr nur 40 €. Richtig ist ⟦1,04⟧: das ganze Geld plus 4 %.',
  'fehler_bild': {'x': [0, 15], 'y': [0, 2000], 'schritt_y': 500, 'punkte': [],
                  'graphen': [{'art': 'exp', 'a': 1000, 'b': 1.04, 'bereich': [0, 15], 'name': '1,04'},
                              {'art': 'exp', 'a': 1000, 'b': 0.04, 'bereich': [0, 15], 'name': '0,04?'}]},
  'regel': 'Ansatz Anfangswert · q^t = Ziel, dann logarithmieren. Bei Zunahme um p ist ⟦q = 1 + p⟧, bei Abnahme q = 1 − p.'},
 'verstehen': {
  'einstieg': 'Rückwärts gerechnet halbieren sich die Bakterien jede Stunde: 1, 1/2, 1/4 … Sie werden weniger, aber nie null oder negativ. '
              'Manche Gleichungen haben deshalb ⟦keine Lösung⟧.',
  'woerter': [['Kehrwert', '1 geteilt durch die Zahl: von 8 ist es 1/8'],
              ['keine Lösung', 'keine Zahl für x macht die Gleichung wahr']],
  'bild': {'typ': 'koordinaten', 'x': [-4, 4], 'y': [-10, 16], 'graphen': [{'art': 'exp', 'a': 1, 'b': 2, 'name': 'y = 2ˣ'}], 'waagrecht': [-8]},
  'schritte': [{'text': 'Behauptung: 2^x = −8 hat die Lösung x = −3.'},
               {'text': 'Probe: 2^(−3) ist der Kehrwert von 2³, also 1/8.',
                'bild': {'punkte': [{'x': -3, 'y': 0.125, 'name': '1/8'}]}},
               {'text': '1/8 ist positiv. Der Graph von 2^x bleibt immer über der x-Achse.'},
               {'text': 'Er trifft die Linie bei −8 nie. Also hat 2^x = −8 ⟦keine Lösung⟧.'}],
  'fehler': 'Ein Minus im Exponenten macht die Zahl nicht negativ, es bildet den ⟦Kehrwert⟧. Wie bei den Bakterien rückwärts: weniger, aber nie unter null.',
  'regel': 'Logarithmen gibt es nur von Zahlen größer als 0. Merke ⟦log_b(1) = 0⟧ und log_b(b) = 1.'},
}


# ---------- Zehnte Runde (Zweig schwer-kl10): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Zufallsstart (nur zum Mischen der Antworten); wird erst NACH bauen(...) aufgerufen, alte Aufgaben bleiben gleich.
# Vorbilder (Typ und Niveau, eigene Zahlen und Einkleidung): Realschul-Abschlussprüfung Bayern Mathematik I 2021/2022 (A 1:
# Wachstumsrate aus zwei Werten, erstes Jahr über einer Grenze, zwei Vorgänge gleichsetzen), Abitur Bayern Prüfungsteil A
# (exakte Werte ohne Hilfsmittel, Definitionsmenge von lg/ln), Grundwissen G9 (Ausklammern bei Exponentialgleichungen).
def schwer():
    start(10010)
    N = []

    def neu(l, s, a):
        a['l'], a['s'] = l, s
        N.append(a)

    def rz(wahr, nd):
        return gerundet(wahr, nd), f'round({K(wahr)}, {nd})'

    # --- logarithmus ---
    neu('logarithmus', 2, luecken('Zwischen welchen aufeinanderfolgenden ganzen Zahlen liegt log₂(50)? Ohne Taschenrechner.', '□ < log₂(50) < □',
                                  'Zwei ganze Zahlen', [5, 6], '2⁵ = 32 < 50 < 64 = 2⁶, also 5 < log₂(50) < 6.',
                                  'Suche die Zweierpotenzen direkt unter und über 50.', c=['5', '6']))
    neu('logarithmus', 2, zahl('Berechne log₄(8) ohne Taschenrechner.', '4 = 2² und 8 = 2³. Gesucht ist y mit 4^y = 8, also 2^(2y) = 2³, 2y = 3, y = 1,5.',
                               'Schreibe 4 und 8 als Potenzen von 2.', Fr(3, 2), '3 / 2'))
    neu('logarithmus', 3, zahl('Berechne ohne Taschenrechner: log₂(8) + log₃(1/9) − lg(1 000).',
                               'log₂(8) = 3, log₃(1/9) = −2 (denn 3^(−2) = 1/9), lg(1 000) = 3. Also 3 + (−2) − 3 = −2.',
                               'Bestimme jeden Logarithmus einzeln: Welcher Exponent passt?', -2, '3 + (-2) - 3'))
    neu('logarithmus', 3, zahl('Es gilt log_b(1/27) = −3. Bestimme die Basis b.', 'log_b(1/27) = −3 heißt b^(−3) = 1/27, also b³ = 27 und b = 3.',
                               'Ein negativer Exponent bedeutet Kehrwert: b^(−3) = 1/b³.', 3, '3 + (3 ** (-3) - 1 / 27)'))
    a = auswahl('Ordne ohne Taschenrechner: a = log₂(7), b = log₃(30), c = lg(0,5).', 'c < a < b', ['a < b < c', 'c < b < a', 'a < c < b'],
                'lg(0,5) < 0, weil 0,5 < 1. 2² = 4 < 7 < 8 = 2³, also liegt a zwischen 2 und 3. 3³ = 27 < 30 < 81, also liegt b zwischen 3 und 4. Damit c < a < b.',
                'Schätze jeden Logarithmus zwischen zwei ganzen Zahlen ein.')
    neu('logarithmus', 3, a)
    neu('logarithmus', 3, zahl('Löse log₂(log₃(x)) = 2.', 'Von außen nach innen: log₂(…) = 2 heißt log₃(x) = 2² = 4. Dann x = 3⁴ = 81.',
                               'Rückwärts denken: Was muss in der Klammer von log₂ stehen?', 81, '3 ** (2 ** 2)'))

    # --- gleiche_basis ---
    neu('gleiche_basis', 2, zahl('Löse 25^x = 1/125.', '25 = 5², 1/125 = 5^(−3). Also 5^(2x) = 5^(−3), 2x = −3, x = −1,5.',
                                 'Schreibe beide Seiten als Potenz von 5.', Fr(-3, 2), '-3 / 2'))
    neu('gleiche_basis', 2, zahl('Löse 4^x = 8^(x − 1).', '4^x = 2^(2x), 8^(x − 1) = 2^(3x − 3). Also 2x = 3x − 3, x = 3.',
                                 'Schreibe 4 und 8 als Potenzen von 2 und multipliziere die Exponenten.', 3, '3'))
    neu('gleiche_basis', 3, zahl('Löse 3^(x + 1) + 3^x = 108.', '3^(x + 1) = 3 · 3^x. Ausklammern: 3^x · (3 + 1) = 108, also 3^x = 27 = 3³ und x = 3.',
                                 'Schreibe 3^(x + 1) als 3 · 3^x und klammere 3^x aus.', 3, '3 + (3 ** 4 + 3 ** 3 - 108)'))
    neu('gleiche_basis', 3, zahl('Löse 2^(x + 2) − 2^x = 48.', '2^(x + 2) = 4 · 2^x. Ausklammern: 2^x · (4 − 1) = 48, also 2^x = 16 = 2⁴ und x = 4.',
                                 'Schreibe 2^(x + 2) als 4 · 2^x und klammere 2^x aus.', 4, '4 + (2 ** 6 - 2 ** 4 - 48)'))
    neu('gleiche_basis', 3, luecken('Löse 4^x − 6 · 2^x + 8 = 0.', 'x₁ = □; x₂ = □', 'Kleinere Lösung zuerst',
                                    [1, 2], 'Mit u = 2^x: u² − 6u + 8 = 0, also (u − 2)(u − 4) = 0. u = 2 gibt x = 1, u = 4 gibt x = 2.',
                                    'Es gilt 4^x = (2^x)². Ersetze 2^x durch u; dann entsteht eine quadratische Gleichung.', c=['1', '2']))
    neu('gleiche_basis', 3, zahl('Für welche Zahl a hat die Gleichung 2^(x + a) = 8^x die Lösung x = 2?',
                                 '8^x = 2^(3x). Gleiche Exponenten: x + a = 3x. Mit x = 2: 2 + a = 6, also a = 4.',
                                 'Setze x = 2 ein und vergleiche die Exponenten.', 4, '3 * 2 - 2'))

    # --- mit_log_loesen ---
    w, c = rz(lg(3) / lg(1.2), 2)
    neu('mit_log_loesen', 2, zahl('Löse 5 · 1,2^x + 3 = 18. Runde auf zwei Nachkommastellen.', f'5 · 1,2^x = 15, also 1,2^x = 3. x = lg 3 : lg 1,2 ≈ {dz(w)}.',
                                  'Zuerst 3 abziehen, dann durch 5 teilen.', w, c, tol=0.01))
    w, c = rz(3 / lg(2), 2)
    neu('mit_log_loesen', 2, zahl('Löse 2^(x/3) = 10. Runde auf zwei Nachkommastellen.', f'x/3 = lg 10 : lg 2 ≈ 3,3219, also x = 3 · 3,3219 ≈ {dz(w)}.',
                                  'Logarithmiere, dann multipliziere mit 3.', w, c, tol=0.01))
    w, c = rz(lg(5) / lg(2), 2)
    neu('mit_log_loesen', 3, zahl('Löse 2^x + 2^(x + 1) = 15. Runde auf zwei Nachkommastellen.',
                                  f'2^(x + 1) = 2 · 2^x. Ausklammern: 2^x · 3 = 15, also 2^x = 5 und x = lg 5 : lg 2 ≈ {dz(w)}.',
                                  'Klammere 2^x aus, bevor du logarithmierst.', w, c, tol=0.01))
    xg = lg(0.25) / lg(0.8)
    neu('mit_log_loesen', 3, zahl('Bestimme die kleinste ganze Zahl x mit 6 · 0,8^x < 1,5.',
                                  f'0,8^x < 0,25. Logarithmieren: x · lg 0,8 < lg 0,25. Weil lg 0,8 negativ ist, dreht sich das Zeichen: x > {dz(round(xg, 2))}. Kleinste ganze Zahl: 7.',
                                  'Achtung: Beim Teilen durch eine negative Zahl dreht sich das Ungleichheitszeichen.', math.floor(xg) + 1, '7'))
    w, c = rz(lg(300), 2)
    neu('mit_log_loesen', 3, zahl('Löse 5^x · 2^x = 300. Runde auf zwei Nachkommastellen.', f'5^x · 2^x = (5 · 2)^x = 10^x. Also 10^x = 300 und x = lg 300 ≈ {dz(w)}.',
                                  'Gleiche Exponenten: Fasse die Basen zu einer Potenz zusammen.', w, c, tol=0.01))
    neu('mit_log_loesen', 3, bruch_luecke('Für welche Zahl c hat die Gleichung 3^x = c die Lösung x = −2?', Fr(1, 9),
                                          'x = −2 einsetzen: c = 3^(−2) = 1/3² = 1/9.', 'Rückwärts denken: Setze die Lösung in die Gleichung ein.', c=['1', '3 ** 2']))

    # --- potenzregel ---
    neu('potenzregel', 2, zahl('Berechne lg(0,001⁴) mit der Potenzregel.', 'lg(0,001⁴) = 4 · lg 0,001 = 4 · (−3) = −12.',
                               'lg 0,001 ist der Exponent von 10, der 0,001 ergibt.', -12, '4 * (-3)'))
    neu('potenzregel', 2, luecken('Vereinfache log₂(8^x) mit der Potenzregel.', '□x', 'Zahl vor x', [3],
                                  'log₂(8^x) = x · log₂(8) = x · 3 = 3x.', 'Der Exponent x wird zum Faktor; dann log₂(8) berechnen.', c=['3']))
    neu('potenzregel', 3, zahl('Es gilt lg 2 ≈ 0,30103. Wie viele Ziffern hat die Zahl 2¹⁰⁰?',
                               'lg(2¹⁰⁰) = 100 · lg 2 ≈ 30,103. Also ist 10³⁰ < 2¹⁰⁰ < 10³¹. Eine Zahl zwischen 10³⁰ und 10³¹ hat 31 Ziffern.',
                               '10³ hat 4 Ziffern, 10⁴ hat 5 Ziffern. Zwischen welchen Zehnerpotenzen liegt 2¹⁰⁰?', 31, '100 * 30103 // 100000 + 1'))
    w, c = rz(lg(3) / (2 * lg(5) - lg(3)), 2)
    neu('potenzregel', 3, zahl('Löse 5^(2x) = 3^(x + 1). Runde auf zwei Nachkommastellen.',
                               f'2x · lg 5 = (x + 1) · lg 3. Ordnen: x · (2 lg 5 − lg 3) = lg 3, also x = lg 3 : (2 lg 5 − lg 3) ≈ {dz(w)}.',
                               'Logarithmiere beide Seiten, setze die Klammer (x + 1) und sammle alle x auf einer Seite.', w, c, tol=0.01))
    neu('potenzregel', 3, auswahl('Jemand löst 2^x = 3^(x − 1) so: „x · lg 2 = x − 1 · lg 3“. Was ist der Fehler?',
                                  'Die Klammer fehlt: richtig ist (x − 1) · lg 3.',
                                  ['Kein Fehler.', 'Man darf nicht logarithmieren, weil die Basen verschieden sind.', 'Richtig wäre x · lg 2 = x · lg 3 − 1.'],
                                  'Die Potenzregel holt den ganzen Exponenten x − 1 als Faktor heraus: lg(3^(x − 1)) = (x − 1) · lg 3. Ohne Klammer wird nur 1 mit lg 3 multipliziert.',
                                  'Welcher Teil ist der Exponent von 3?'))
    neu('potenzregel', 3, zahl('Es gilt log₂(a) = 6. Berechne log₂(a²) + log₂(√a).', 'log₂(a²) = 2 · 6 = 12; √a = a^0,5, also log₂(√a) = 0,5 · 6 = 3. Summe: 15.',
                               'Schreibe √a als Potenz von a und nutze die Potenzregel zweimal.', 15, '2 * 6 + 6 / 2'))

    # --- wachstum ---
    w, c = rz(3 ** 0.25, 2)
    neu('wachstum', 2, zahl('Eine Bakterienkultur verdreifacht sich alle 4 Stunden. Um welchen Faktor wächst sie pro Stunde? Runde auf zwei Nachkommastellen.',
                            f'q⁴ = 3, also q = 3^(1/4) ≈ {dz(w)}.', 'Vier gleiche Faktoren q ergeben zusammen 3.', w, c, tol=0.01))
    t = lg(1 / 3) / lg(0.85)
    neu('wachstum', 2, zahl('Ein Auto kostet neu 30 000 € und verliert jedes Jahr 15 % seines Werts. Nach wie vielen vollen Jahren ist es erstmals weniger als 10 000 € wert?',
                            f'30 000 · 0,85^t < 10 000 ⇔ 0,85^t < 1/3 ⇔ t > lg(1/3) : lg 0,85 ≈ {dz(round(t, 2))}. Also nach 7 Jahren.',
                            'Abnahme um 15 %: q = 0,85. Achte beim Ergebnis auf „erstmals“.', math.floor(t) + 1, '7'))
    q = 1.2 ** (1 / 3)
    w, c = rz((q - 1) * 100, 1)
    neu('wachstum', 3, zahl('Eine Kinokarte kostete 2021 genau 9,00 € und 2024 genau 10,80 €. Der Preis stieg jedes Jahr um denselben Prozentsatz. Um wie viel Prozent pro Jahr? Runde auf eine Nachkommastelle.',
                            f'9 · q³ = 10,80, also q³ = 1,2 und q = 1,2^(1/3) ≈ 1,0627. Das sind etwa {dz(w)} % pro Jahr.',
                            'Zwischen 2021 und 2024 liegen 3 Jahre. Stelle 9 · q³ = 10,80 auf.', w, c, einheit='%', tol=0.1))
    t = lg(15 / 9) / lg(q)
    neu('wachstum', 3, zahl('Eine Kinokarte kostete 2021 genau 9,00 € und 2024 genau 10,80 € (gleicher Prozentsatz jedes Jahr). In welchem Jahr kostet sie bei gleicher Entwicklung erstmals mehr als 15 €?',
                            f'q³ = 1,2. 9 · q^t > 15 ⇔ q^t > 5/3 ⇔ t > lg(5/3) : lg q = 3 · lg(5/3) : lg 1,2 ≈ {dz(round(t, 2))}. Also t = 9, das Jahr 2021 + 9 = 2030.',
                            'Zähle t ab 2021. Nutze lg q = lg 1,2 : 3.', 2021 + math.floor(t) + 1, '2021 + 9'))
    t = lg(1.25) / lg(1.04 / 1.02)
    neu('wachstum', 3, zahl('Konto A: 5 000 € mit 2 % Zinseszins. Konto B: 4 000 € mit 4 % Zinseszins. Nach wie vielen vollen Jahren hat Konto B erstmals mehr Geld als Konto A?',
                            f'4 000 · 1,04^t > 5 000 · 1,02^t ⇔ (1,04 : 1,02)^t > 1,25 ⇔ t > lg 1,25 : lg(1,04 : 1,02) ≈ {dz(round(t, 2))}. Also nach 12 Jahren.',
                            'Setze beide Kontostände an und teile durch 4 000 · 1,02^t.', math.floor(t) + 1, '12'))
    n = lg(0.01) / lg(0.5)
    neu('wachstum', 3, zahl('Ein Stoff zerfällt mit fester Halbwertszeit. Nach wie vielen Halbwertszeiten ist erstmals weniger als 1 % übrig?',
                            f'0,5^n < 0,01 ⇔ n > lg 0,01 : lg 0,5 ≈ {dz(round(n, 2))}. Also nach 7 Halbwertszeiten (0,5⁷ ≈ 0,8 %).',
                            'Nach n Halbwertszeiten ist der Anteil 0,5^n übrig. Die Halbwertszeit selbst brauchst du nicht.', math.floor(n) + 1, '7'))

    # --- verstehen ---
    neu('verstehen', 2, auswahl('Für welche Zahlen x ist lg(x − 3) definiert?', 'x > 3', ['x ≥ 3', 'x > 0', 'alle x ≠ 3'],
                                'Der Logarithmus braucht ein positives Argument: x − 3 > 0, also x > 3. Für x = 3 wäre das Argument 0.',
                                'Was muss für die Zahl in der Klammer gelten?'))
    neu('verstehen', 2, auswahl('Welche Gleichung hat keine Lösung?', '3^x = 0', ['2^x = 0,5', 'lg x = −2', '5^(x − 1) = 1'],
                                '3^x ist immer positiv, wird also nie 0. Die anderen: x = −1, x = 0,01, x = 1.',
                                'Kann eine Potenz mit positiver Basis 0 werden?'))
    neu('verstehen', 3, auswahl('Für welche Zahlen c hat die Gleichung 2^x + 3 = c eine Lösung?', 'c > 3', ['c ≥ 3', 'c > 0', 'für alle c'],
                                '2^x nimmt alle positiven Werte an, aber nie 0. Also nimmt 2^x + 3 alle Werte größer als 3 an.',
                                'Welche Werte kann 2^x annehmen? Was ändert „+ 3“?'))
    neu('verstehen', 3, auswahl('Jemand behauptet: „lg(x²) = 2 hat genau die Lösung x = 10.“ Was stimmt?', 'Falsch: auch x = −10 ist eine Lösung.',
                                ['Richtig.', 'Falsch: die Lösung ist x = 100.', 'Falsch: die Lösung ist x = √10.'],
                                'lg(x²) = 2 heißt x² = 100, also x = 10 oder x = −10. Probe: (−10)² = 100 > 0. Die Umformung zu 2 · lg x gilt nur für x > 0.',
                                'Löse zuerst nach x² auf. Welche Zahlen haben das Quadrat 100?'))
    neu('verstehen', 3, auswahl('Wie viele Lösungen hat die Gleichung 2^x = x + 1?', '2', ['0', '1', '3'],
                                'x = 0 (1 = 1) und x = 1 (2 = 2) sind Lösungen. Der Graph von 2^x krümmt sich nach oben und schneidet eine Gerade höchstens zweimal.',
                                'Probiere kleine ganze Zahlen. Denk an die Form der Graphen.'))
    neu('verstehen', 3, auswahl('Die Zahl x = log₂(3) − 1 ist die Lösung einer der Gleichungen. Welcher?', '2^(x + 1) = 3', ['2^x = 3 − 1', '2^(x − 1) = 3', '2^x + 1 = 3'],
                                'Aus x = log₂(3) − 1 folgt x + 1 = log₂(3), also 2^(x + 1) = 3.', 'Bringe die −1 auf die andere Seite und schreibe die Gleichung als Potenz.'))
    return N


GEN = schoen(GEN)

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('gleichungen.exponential', 13_10_1)
# a) gleicher Aufgabentyp wie Stufe 2 („a · b^x = c“ falsch umgeformt; „Welche Aussage ist falsch? lg(a + b) …“)
BF.stufe('verstehen', 'Jemand formt 2 · 2^x = 76 um zu 4^x = 76. Was stimmt?', 2)
BF.stufe('verstehen', 'Jemand formt 4 · 5^x = 24 um zu 20^x = 24. Was stimmt?', 2)
for _s in ('lg(6 + 3)', 'lg(3 + 2)', 'lg(6 + 2)', 'lg(9 + 4)'):
    BF.stufe('verstehen', 'Welche Aussage ist falsch?', 2, enthaelt=_s)
# a) „Welche Lösung hat b^x = −…?“ auf Stufe 1 und 2 → einheitlich Stufe 1
BF.stufe('verstehen', 'Welche Lösung hat 3^x = −81? Die Zeichnung zeigt y = 3^x und y = −81.', 1)
BF.stufe('verstehen', 'Welche Lösung hat 3^x = −9? Die Zeichnung zeigt y = 3^x und y = −9.', 1)
# d) Karte „Wachstum und Zerfall: Wann?“ – die Zinseszins-Aufgaben fragten nach dem Betrag, nicht nach dem Zeitpunkt
_h = 'Teile zuerst durch den Anfangswert. Dann logarithmieren: t = lg(rechte Seite) : lg(Basis).'
for _k, _p, _n, _ziel, _t, _w in [
        ('5 000', '6', '5', '7 000', 5.8, 't = lg(7 000 : 5 000) : lg 1,06 = lg 1,4 : lg 1,06 ≈ 5,8 Jahre.'),
        ('2 000', '2', '2', '2 500', 11.3, 't = lg(2 500 : 2 000) : lg 1,02 = lg 1,25 : lg 1,02 ≈ 11,3 Jahre.'),
        ('1 000', '6', '2', '2 000', 11.9, 't = lg(2 000 : 1 000) : lg 1,06 = lg 2 : lg 1,06 ≈ 11,9 Jahre.')]:
    _f = f'1,0{_p}'
    _c = {5.8: 'round(5.774472998624, 1)', 11.3: 'round(11.268381108059, 1)', 11.9: 'round(11.895661045942, 1)'}[_t]
    BF.ersetze('wachstum', f'Ein Kapital von {_k} € wird mit {_p} % pro Jahr verzinst (Zinseszins). Wie groß ist es nach {_n} Jahren? Runde auf Cent.', BF.Z(
        f'Ein Kapital von {_k} € wird mit {_p} % pro Jahr verzinst (Zinseszins). Löse {_k} · {_f}^t = {_ziel}, um zu sehen, wann es auf {_ziel} € angewachsen ist. Runde auf eine Nachkommastelle.',
        _t, _c, _w, _h, einheit='Jahre', toleranz=0.1))

BF.ersetze('wachstum', 'Ein Kapital von 2 000 € wird mit 2 % pro Jahr verzinst (Zinseszins). Wie groß ist es nach 3 Jahren? Runde auf Cent.', BF.Z(
    'Ein Kapital von 2 000 € wird mit 2 % pro Jahr verzinst (Zinseszins). Löse 2 000 · 1,02^t = 3 000, um zu sehen, wann es auf 3 000 € angewachsen ist. Runde auf eine Nachkommastelle.',
    20.5, 'round(20.475318857634, 1)', 't = lg(3 000 : 2 000) : lg 1,02 = lg 1,5 : lg 1,02 ≈ 20,5 Jahre.', _h, einheit='Jahre', toleranz=0.1), pools=('sicherung',))
# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    datei = bauen('gleichungen.exponential',
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
    ergaenzen(datei, schwer())
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden


# ---------- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl10) ----------
# Gesamtdurchsicht: jede Lernkarte und jede Aufgabe gelesen und nachgerechnet. Läuft ganz am Ende auf der fertigen Datei.
def durchsicht():
    from _durchsicht_kl10 import Durchsicht
    D = Durchsicht('gleichungen.exponential', 19020)
    # logarithmus: „log₂(x) = 3, bestimme x“ ist die einfache Umkehrung (Stufe 2), kein anderer Gedanke
    D.stufe(13, 2, 'Es gilt log₂(x) = 3')
    D.stufe(17, 2, 'Es gilt log₃(x) = 3')
    # gleiche_basis: „a · b^x = c“ heißt nur: erst teilen (Abwandlung, Stufe 2)
    D.stufe([41, 42, 45], 2, 'Löse ')
    # mit_log_loesen: b^(mx + n) = c ist die Stufe-2-Rechnung mit einem linearen Schritt mehr → Stufe 2
    D.stufe(range(68, 74), 2, 'Löse ')
    # potenzregel: b^x = a^(x + n) ist genau das vorgerechnete Beispiel; die dreifache Auswahl „Welche Umformung ist richtig?“ ist Wissen, kein anderer Gedanke
    D.stufe([96, 97, 101], 2, 'Löse ')
    D.stufe([98, 99, 100], 2, 'Welche Umformung ist richtig')
    D.neu('potenzregel', 3, D.Z('Es gilt lg 2 ≈ 0,301. Bestimme log₂(10) ohne Taschenrechner. Runde auf zwei Nachkommastellen.', 3.32, 'round(1 / 0.301, 2)',
                                 'y = log₂(10) heißt 2^y = 10. Auf beiden Seiten lg: y · lg 2 = lg 10 = 1. Also y = 1 : 0,301 ≈ 3,32.',
                                 'Schreibe y = log₂(10) als Potenzgleichung und nimm auf beiden Seiten lg.', toleranz=0.01))
    # wachstum: Population 40 → 300 bei 5 % ist die Stufe-1-Rechnung in Worten → Stufe 2
    D.stufe(127, 2, 'Eine Population wächst um 5 %')
    # verstehen: Abwechslung – fünfmal „keine Lösung“ (Stufe 1) und sechsmal „Welche Aussage ist falsch?“ (Stufe 2) hintereinander
    D.ersetze(144, 'Welche Lösung hat 5^x = −15 625', D.A('Welchen Wert hat log₇(7)?', '1', ['0', '7', '49'],
                                                          '7¹ = 7, also log₇(7) = 1. Allgemein: log_b(b) = 1.', 'Mit welchem Exponenten wird aus 7 wieder 7?'))
    D.ersetze(151, 'Welche Lösung hat 3^x = −9', D.A('Welche Zahl ist 2^(−3)?', '1/8', ['−8', '−6', '8'],
                                                     'Ein Minus im Exponenten bildet den Kehrwert: 2^(−3) = 1 : 2³ = 1/8. Das Ergebnis bleibt positiv.',
                                                     'Ein negativer Exponent macht die Zahl nicht negativ. Was macht er?'))
    D.ersetze(153, 'Welche Aussage ist falsch', D.A('Für welche Zahlen x ist log₂(5 − x) definiert?', 'x < 5', ['x > 5', 'x ≤ 5', 'x > 0'],
                                                    'Logarithmen gibt es nur von Zahlen größer als 0: 5 − x > 0 ⇔ x < 5. Bei x = 5 wäre es log₂(0) – nicht definiert.',
                                                    'Was in der Klammer steht, muss größer als 0 sein.'))
    D.ersetze(154, 'Welche Aussage ist falsch', D.A('Welche Lösung hat 4^x = 1?', 'x = 0', ['x = 1', 'x = 1/4', 'keine Lösung'],
                                                    'Jede Zahl hoch 0 ist 1: 4⁰ = 1. Also x = log₄(1) = 0.', 'Mit welchem Exponenten wird aus einer Zahl 1?'))
    D.ersetze(156, 'Welche Aussage ist falsch', D.A('Jemand sagt: „lg(1 000) ist dreimal so groß wie lg(10).“ Was stimmt?', 'Richtig.',
                                                    ['Falsch: lg(1 000) ist hundertmal so groß.', 'Falsch: lg(1 000) = 1 000 : 10 = 100.', 'Falsch: Beide sind gleich groß.'],
                                                    'lg(1 000) = 3, denn 10³ = 1 000; lg(10) = 1. Also dreimal so groß – wie die Potenzregel sagt: lg(10³) = 3 · lg 10.',
                                                    'Berechne beide Logarithmen einzeln.'))
    # Lernkarte mit_log_loesen: „x = lg 10 : lg 2“ kam ohne Begründung (die Potenzregel folgt erst eine Karte später)
    D.karte('mit_log_loesen', schritte=[
        {'text': '3 · 2^x = 30 heißt: 3 Bakterien, x Stunden verdoppelt, ergeben 30.'},
        {'text': 'Zuerst durch 3 teilen, damit die Potenz allein steht: 2^x = 10.'},
        {'text': '2³ = 8 und 2⁴ = 16. Also liegt x zwischen 3 und 4.',
         'bild': {'punkte': [{'x': 3, 'y': 24, 'name': '3 h: 24'}, {'x': 4, 'y': 48, 'name': '4 h: 48'}]}},
        {'text': 'Nach der Bedeutung des Logarithmus ist x = log₂(10).'},
        {'text': 'Der Rechner rechnet das als lg 10 : lg 2 ≈ ⟦3,32⟧ Stunden.',
         'bild': {'punkte': [{'x': 3.32, 'y': 30, 'name': '≈ 3,32 h'}], 'senkrecht': [3.32]}}])
    # Lernkarte wachstum: „q = 1 + p“ ließ offen, ob p in Prozent gemeint ist
    D.karte('wachstum', regel='Ansatz Anfangswert · q^t = Ziel, dann logarithmieren. Zunahme um p %: ⟦q = 1 + p/100⟧, Abnahme: q = 1 − p/100.')
    D.anwenden()


if __name__ == '__main__':
    durchsicht()  # Neunzehnte Runde (durchsicht-kl10) – ganz am Ende
