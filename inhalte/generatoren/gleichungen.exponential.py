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
     'regel': 'Ein Exponent im Logarithmus wird zum ⟦Faktor⟧: ⟦log_b(a^r) = r · log_b(a)⟧. So holt man die Unbekannte aus dem Exponenten.',
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
    if typ < 0.7:
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


def g_potenzregel(s):
    if s == 1:
        b = R.choice([2, 3, 5, 10])
        a = R.choice([2, 3, 4, 5, 7]) if b == 10 else b ** R.randint(1, 3)
        r = R.randint(2, 9)
        if b != 10:
            n = round(log(a, b))
            return zahl(f'Berechne {lb(b)}({a}^{r}) mit der Potenzregel.', f'{lb(b)}({a}^{r}) = {r} · {lb(b)}({a}) = {r} · {n} = {r * n}.',
                        'Ziehe den Exponenten als Faktor vor den Logarithmus.', r * n, f'{r} * {n} + ({b} ** {n} - {a})')
        return luecken(f'Schreibe lg({a}^{r}) mit der Potenzregel als Vielfaches von lg {a}.', f'□ · lg {a}', 'Faktor', [r],
                       f'lg({a}^{r}) = {r} · lg {a}.', 'Der Exponent wird zum Faktor.', c=[str(r)])
    if s == 2:
        base, l = R.choice([(2, Fr(3010, 10000)), (3, Fr(4771, 10000)), (5, Fr(6990, 10000)), (7, Fr(8451, 10000))])
        r = R.randint(2, 6)
        return zahl(f'Es gilt lg {base} ≈ {dz(l)}. Berechne damit lg({base}^{r}) (ohne Taschenrechner).',
                    f'lg({base}^{r}) = {r} · lg {base} ≈ {r} · {dz(l)} = {dz(r * l)}.', 'Potenzregel: Exponent als Faktor.', r * l, f'{r} * {cf(l)}')
    typ = R.random()
    if typ < 0.6:
        a, b2 = R.sample([2, 3, 5, 7], 2)
        m = R.choice([1, 2, -1])
        # a^x = b2^(x + m)  ⇒  x lg a = (x + m) lg b2  ⇒  x = m lg b2 / (lg a − lg b2)
        x = m * lg(b2) / (lg(a) - lg(b2))
        v = gerundet(x, 2)
        if v is None: return None
        return zahl(f'Löse {a}^x = {b2}^(x {plus(m)}). Runde auf zwei Nachkommastellen.',
                    f'x · lg {a} = (x {plus(m)}) · lg {b2} ⇒ x(lg {a} − lg {b2}) = {dz(m)} · lg {b2} ⇒ x ≈ {dz(v)}.',
                    'Logarithmiere beide Seiten, wende die Potenzregel an und sammle die x-Terme.', v, f'round({K(x)}, 2)', tol=0.01)
    a = R.randint(2, 9)
    return auswahl(f'Welche Umformung ist richtig (x > 0)?', f'lg(x^{a}) = {a} · lg x',
                   [f'lg({a}x) = {a} · lg x', f'lg(x^{a}) = (lg x)^{a}', f'lg(x + {a}) = lg x + lg {a}'],
                   f'Die Potenzregel holt nur den Exponenten einer Potenz heraus: lg(x^{a}) = {a} · lg x. Produkte und Summen sind etwas anderes.',
                   'Steht die Zahl als Exponent, als Faktor oder als Summand?')


def g_wachstum(s):
    if s == 1:
        p = R.choice([2, 3, 4, 5, 6, 8, 10])
        n = R.randint(2, 4)
        K0 = R.choice([1000, 2000, 5000, 10000])
        q = 1 + Fr(p, 100)
        Kn = K0 * q ** n
        if not endlich(Kn): return None
        return zahl(f'Ein Kapital von {dz(K0)} € wird mit {p} % pro Jahr verzinst (Zinseszins). Wie groß ist es nach {n} Jahren?',
                    f'K = {dz(K0)} · {dz(q)}^{n} = {dz(Kn)} €.', 'Wachstumsfaktor 1 + p/100, so oft multiplizieren wie Jahre vergehen.',
                    Kn, f'{K0} * {cf(q)} ** {n}', einheit='€')
    if s == 2:
        typ = R.random()
        if typ < 0.5:
            p = R.choice([2, 3, 4, 5, 6, 8])
            q = 1 + p / 100
            t = log(2) / log(q)
            n = ceil(t)
            if t - int(t) < 0.02: return None
            return zahl(f'Ein Guthaben wird mit {p} % pro Jahr verzinst. Nach wie vielen vollen Jahren hat es sich erstmals verdoppelt?',
                        f'{dz(Fr(100 + p, 100))}^t = 2 ⇒ t = lg 2 : lg {dz(Fr(100 + p, 100))} ≈ {dz(round(t, 2))}, also nach {n} Jahren.',
                        'Löse q^t = 2 und runde auf die nächste ganze Zahl nach oben.', n, f'-(-{K(t)} // 1)', einheit='Jahre')
        T = R.choice([5, 8, 12, 20, 30])
        k = R.randint(2, 5)
        m0 = R.choice([80, 160, 200, 320, 400])
        m = Fr(m0, 2 ** k)
        if not endlich(m): return None
        return zahl(f'Ein radioaktiver Stoff hat eine Halbwertszeit von {T} Tagen. Anfangs sind {m0} mg vorhanden. Wie viel ist nach {T * k} Tagen noch da?',
                    f'{T * k} Tage = {k} Halbwertszeiten: {m0} · 0,5^{k} = {dz(m)} mg.', 'Wie oft passt die Halbwertszeit in die Zeitspanne?', m,
                    f'{m0} * 0.5 ** {k}', einheit='mg')
    typ = R.random()
    if typ < 0.4:
        p = R.choice([3, 5, 8, 10, 12, 15, 20])
        N0, Z = R.choice([(1000, 5000), (500, 2000), (2000, 3000), (100, 1000), (40, 300)])
        q = 1 + p / 100
        t = log(Z / N0) / log(q)
        v = gerundet(t, 1)
        if v is None: return None
        return zahl(f'Eine Population wächst um {p} % pro Woche von {dz(N0)} auf {dz(Z)} Tiere. Nach wie vielen Wochen ist das der Fall (eine Nachkommastelle)?',
                    f'{dz(N0)} · {dz(Fr(100 + p, 100))}^t = {dz(Z)} ⇒ t = lg({zt(Fr(Z, N0))}) : lg {dz(Fr(100 + p, 100))} ≈ {dz(v)} Wochen.',
                    'Teile durch den Anfangswert, dann logarithmieren.', v, f'round({K(t)}, 1)', einheit='Wochen', tol=0.1)
    if typ < 0.7:
        p = R.choice([5, 10, 15, 20, 25, 30])
        q = 1 - p / 100
        t = log(0.5) / log(q)
        v = gerundet(t, 1)
        if v is None: return None
        return zahl(f'Der Wert eines Geräts nimmt jedes Jahr um {p} % ab. Nach wie vielen Jahren ist er auf die Hälfte gesunken (eine Nachkommastelle)?',
                    f'{dz(Fr(100 - p, 100))}^t = 0,5 ⇒ t = lg 0,5 : lg {dz(Fr(100 - p, 100))} ≈ {dz(v)} Jahre.', 'Abnahme um p %: Faktor 1 − p/100.',
                    v, f'round({K(t)}, 1)', einheit='Jahre', tol=0.1)
    T = R.choice([6, 8, 10, 25])
    rest = R.choice([10, 20, 30, 40, 60, 70])
    t = T * log(rest / 100) / log(0.5)
    v = gerundet(t, 1)
    if v is None: return None
    return zahl(f'Ein Medikament wird mit einer Halbwertszeit von {T} Stunden abgebaut. Nach welcher Zeit sind noch {rest} % vorhanden (eine Nachkommastelle)?',
                f'0,5^(t/{T}) = {dz(Fr(rest, 100))} ⇒ t = {T} · lg {dz(Fr(rest, 100))} : lg 0,5 ≈ {dz(v)} h.', 'Ansatz N₀ · 0,5^(t/T) und durch N₀ teilen.',
                v, f'round({K(t)}, 1)', einheit='h', tol=0.1)


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
        if b ** (n - 1) == n: return None
        return auswahl(f'Jemand rechnet {lb(b)}({dz(b ** n)}) = {dz(b ** n)} : {b} = {dz(b ** (n - 1))}. Was stimmt?', f'Falsch, {lb(b)}({dz(b ** n)}) = {n}',
                       ['Richtig', f'Falsch, {lb(b)}({dz(b ** n)}) = {dz(b ** n * b)}', f'Falsch, {lb(b)}({dz(b ** n)}) = {dz(Fr(b ** n, 2)) if endlich(Fr(b ** n, 2)) else n + 1}'],
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
GEN = schoen(GEN)

if __name__ == '__main__':
    bauen('gleichungen.exponential',
          'Logarithmen verstehen und Exponentialgleichungen lösen – mit gleicher Basis oder durch Logarithmieren mit der Potenzregel, auch bei Wachstum und Zerfall.',
          ['b^y = x ⇔ y = log_b(x); lg = log₁₀.', 'Gleiche Basis: Exponenten gleichsetzen.', 'Sonst: Potenz allein stellen, logarithmieren: x = lg c : lg b.',
           'Potenzregel: log_b(a^r) = r · log_b(a).'],
          [('Logarithmus', ['logarithmus', 'gleiche_basis']), ('Lösen mit dem Logarithmus', ['mit_log_loesen', 'potenzregel']),
           ('Anwenden und Verstehen', ['wachstum', 'verstehen'])],
          ETAPPEN, GEN,
          meiden={'logarithmus': ['log₂(32).'], 'gleiche_basis': ['3^(x − 1) = 81.'], 'mit_log_loesen': ['3 · 2^x = 30'],
                  'potenzregel': ['5^x = 2^(x + 1)'], 'wachstum': ['4 % pro Jahr verzinst (Zinseszins). Wie groß'], 'verstehen': ['2^x = −8']},
          offen=['Zeichnungen: Lernkarten „logarithmus“, „mit_log_loesen“, „wachstum“ und „verstehen“ haben ein Koordinatensystem; Aufgaben zum Abschätzen (Stufe 1 „mit_log_loesen“) und zu „keine Lösung“ zeigen den Graphen. Die Exponenten heißen in den Graphnamen „2^x“ (Text).',
                 'Nur die Potenzregel für Logarithmen (lehrplan_gym). Produkt- und Quotientenregel sind bewusst nicht enthalten.',
                 'Rechenausdruck c bei exakten Logarithmen: prüft b^n = x (z. B. „5 + (2 ** 5 − 32)“), weil das Prüfskript keinen Logarithmus kennt; gerundete Lösungen als 12-stellige Konstante mit Toleranz 0,01 bzw. 0,1.',
                 'Schreibweise: Exponenten mit Unbekannten als „2^x“ bzw. „3^(x − 1)“, Logarithmus als „log₂(32)“ und „lg“.'])
