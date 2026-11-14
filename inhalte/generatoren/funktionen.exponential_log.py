#!/usr/bin/env python3
"""Thema funktionen.exponential_log – Exponential- und Logarithmusfunktionen (Klasse 10)."""
import sys
from math import log
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import *  # noqa: E402,F403

start(1003)
TIEF = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')


def lb(b):
    return 'lg' if b == 10 else f'log{str(b).translate(TIEF)}'


def cf(x):
    x = Fr(x)
    if x.denominator == 1: return str(int(x))
    if endlich(x): return str(float(x))
    return f'({x.numerator}/{x.denominator})'


def zt(x):
    x = Fr(x)
    return dz(x) if endlich(x) else br(x)


def ft(a, b):
    """f(x) = a · b^x als Text"""
    return f'{dz(a) if a != 1 else ""}{" · " if a != 1 else ""}{zt(b)}^x' if not isinstance(b, Fr) or b.denominator == 1 or endlich(b) else f'{dz(a)} · ({br(b)})^x'


ETAPPEN = [
    {'lernziel': 'werte', 'titel': 'Funktionswerte von a · bˣ',
     'regel': 'Bei der ⟦Exponentialfunktion⟧ f(x) = a · b^x (a ≠ 0, b > 0, b ≠ 1) steht x im ⟦Exponenten⟧. a ist der ⟦Anfangswert⟧ f(0), b der ⟦Wachstumsfaktor⟧. b^(−n) = 1/bⁿ.',
     'schritte': ['f(x) = 5 · 2^x, gesucht f(3) und f(−1).', 'f(3) = 5 · 8 = ⟦40⟧; f(−1) = 5 · ½ = ⟦2,5⟧.'],
     'probe': 'f(0) = 5 · 1 = 5 = a ✓',
     'fehler': 'f(3) = (5 · 2)³ = 1 000 ist falsch: Nur ⟦2⟧ wird potenziert, dann mit 5 multipliziert: 5 · 2³ = 40.'},
    {'lernziel': 'faktor', 'titel': 'Wachstumsfaktor und Prozent',
     'regel': 'Zunahme um p % pro Schritt: ⟦b = 1 + p/100⟧. Abnahme um p %: ⟦b = 1 − p/100⟧. b > 1: Wachstum, 0 < b < 1: Zerfall.',
     'schritte': ['Ein Bestand nimmt jährlich um 12 % ab.', 'b = 1 − 0,12 = ⟦0,88⟧, also f(t) = f(0) · 0,88^t.'],
     'probe': '100 · 0,88 = 88, das sind 12 weniger ✓',
     'fehler': 'Bei 12 % Abnahme b = 0,12 zu nehmen ist falsch: Dann blieben nur 12 % übrig. Es bleiben ⟦88 %⟧, also b = 0,88.'},
    {'lernziel': 'modell', 'titel': 'Ein Wachstumsmodell aufstellen',
     'regel': 'Anfangswert a = f(0). Den Faktor b erhältst du aus dem Quotienten ⟦aufeinanderfolgender Werte⟧ (gleicher Abstand). Verdopplung alle T Schritte: ⟦f(t) = a · 2^(t/T)⟧.',
     'schritte': ['Bakterien: 400 zu Beginn, Verdopplung alle 3 Stunden.', 'f(t) = 400 · 2^(t/3); nach 12 h: 400 · 2⁴ = ⟦6 400⟧.'],
     'probe': 'f(3) = 400 · 2 = 800 ✓',
     'fehler': 'Nach 12 h mit 400 · 2 · 12 zu rechnen ist falsch: Das wäre ⟦lineares⟧ Wachstum. Exponentiell wird ⟦4-mal verdoppelt⟧.'},
    {'lernziel': 'graph', 'titel': 'Eigenschaften der Graphen',
     'regel': 'Der Graph von f(x) = a · b^x (a > 0) schneidet die y-Achse in ⟦(0 | a)⟧, hat die ⟦x-Achse als Asymptote⟧ und ist für b > 1 ⟦steigend⟧, für 0 < b < 1 ⟦fallend⟧. Er hat keine Nullstelle.',
     'schritte': ['f(x) = 3 · 0,5^x: b = 0,5 < 1.', 'Graph ⟦fällt⟧, geht durch (0 | 3) und nähert sich für große x der x-Achse.'],
     'probe': 'f(10) = 3 · 0,5¹⁰ ≈ 0,003 > 0 ✓',
     'fehler': '„f(x) = 3 · 0,5^x hat eine Nullstelle bei großem x“ ist falsch: Die Werte werden ⟦beliebig klein, aber nie 0⟧.'},
    {'lernziel': 'logfunktion', 'titel': 'Die Logarithmusfunktion',
     'regel': 'f(x) = log_b(x) ist die ⟦Umkehrfunktion⟧ von g(x) = b^x: x- und y-Werte werden ⟦vertauscht⟧. Sie ist nur für ⟦x > 0⟧ definiert und geht durch (1 | 0) und (b | 1).',
     'schritte': ['g(x) = 2^x geht durch (3 | 8).', 'f(x) = log₂(x) geht durch ⟦(8 | 3)⟧, denn log₂(8) = 3.'],
     'probe': '2³ = 8 ✓',
     'fehler': '„log₂(x) ist für alle x definiert“ ist falsch: 2^y ist immer positiv, deshalb gibt es log₂(x) nur für ⟦x > 0⟧.'},
    {'lernziel': 'zeitpunkt', 'titel': 'Wann wird ein Wert erreicht?',
     'regel': 'Gesucht ist x mit a · b^x = c: erst durch a teilen, dann ⟦logarithmieren⟧: x = log_b(c/a) = lg(c/a) : lg b. ⟦Verdopplungszeit⟧ T₂ = lg 2 : lg b, ⟦Halbwertszeit⟧ T½ = lg 0,5 : lg b.',
     'schritte': ['f(t) = 200 · 1,05^t. Wann ist f(t) = 300?', '1,05^t = 1,5 ⇒ t = lg 1,5 : lg 1,05 ≈ ⟦8,3⟧.'],
     'probe': '200 · 1,05^8,3 ≈ 300 ✓',
     'fehler': '200 · 1,05^t = 300 ⇒ 210^t = 300 ist falsch: 200 · 1,05^t ist ein Produkt, ⟦erst durch 200 teilen⟧.'},
]

_E = {e['lernziel']: e for e in ETAPPEN}
_E['werte']['bild'] = koord([{'art': 'exp', 'a': 5, 'b': 2, 'name': 'f'}], x=(-2, 4), y=(0, 45),
                            punkte=[{'x': 3, 'y': 40, 'name': '(3 | 40)'}, {'x': -1, 'y': 2.5, 'name': '(−1 | 2,5)'}])
_E['faktor']['bild'] = koord([{'art': 'exp', 'a': 100, 'b': 0.88, 'name': '100 · 0,88ᵗ'}, {'art': 'exp', 'a': 100, 'b': 1.12, 'name': '100 · 1,12ᵗ'}],
                             x=(0, 10), y=(0, 320), name_x='t')
_E['modell']['bild'] = koord([{'art': 'exp', 'a': 400, 'b': 2 ** (1 / 3), 'bereich': [0, 12]}], x=(0, 12), y=(0, 7000), name_x='t', schritt_x=3,
                             punkte=[{'x': t, 'y': 400 * 2 ** (t // 3)} for t in (0, 3, 6, 9, 12)])
_E['graph']['bild'] = koord([{'art': 'exp', 'a': 3, 'b': 0.5, 'name': 'f'}], x=(-2, 6), y=(0, 13), punkte=[{'x': 0, 'y': 3, 'name': '(0 | 3)'}])
_E['logfunktion']['bild'] = koord([{'art': 'exp', 'a': 1, 'b': 2, 'name': '2ˣ'}, {'art': 'log', 'b': 2, 'name': 'log₂ x', 'name_x': 5}, {'art': 'linear', 'm': 1, 't': 0}],
                                  x=(-3, 9), y=(-3, 9), punkte=[{'x': 3, 'y': 8, 'name': '(3 | 8)'}, {'x': 8, 'y': 3, 'name': '(8 | 3)'}])
_E['zeitpunkt']['bild'] = koord([{'art': 'exp', 'a': 200, 'b': 1.05, 'bereich': [0, 16]}], x=(0, 16), y=(0, 450), waagrecht=[300], senkrecht=[8.3], name_x='t')


def exp_bild(a, b, x=(-3, 4)):
    return koord([{'art': 'exp', 'a': zahlwert_json(a), 'b': zahlwert_json(b)}], x=x, ymax=abs(a) * 12)


def g_werte(s):
    if s == 1:
        a, b, x = R.randint(1, 9), R.choice([2, 3, 10]), R.randint(1, 4)
        if b == 10 and x > 3: return None
        v = a * b ** x
        return zahl(f'Berechne f({x}) für f(x) = {a} · {b}^x.', f'f({x}) = {a} · {b}^{x} = {a} · {dz(b ** x)} = {dz(v)}.',
                    'Erst potenzieren, dann mit a multiplizieren.', v, f'{a} * {b} ** {x}')
    if s == 2:
        a, b, x = R.choice([2, 4, 5, 8, 10, 20, 40, 100]), R.choice([2, 4, 5, 10]), R.randint(-3, -1)
        v = a * Fr(b) ** x
        if not endlich(v): return None
        return zahl(f'Berechne f({dz(x)}) für f(x) = {a} · {b}^x.', f'f({dz(x)}) = {a} · {b}^({dz(x)}) = {a} : {dz(b ** -x)} = {dz(v)}.',
                    'Ein negativer Exponent bedeutet Kehrwert.', v, f'{a} * {b} ** ({x})')
    a, b, x = R.choice([100, 200, 400, 1000]), R.choice([Fr(1, 2), Fr(3, 2), Fr(6, 5), Fr(4, 5), Fr(11, 10), Fr(9, 10)]), R.randint(2, 4)
    v = a * b ** x
    if not endlich(v): return None
    return zahl(f'Berechne f({x}) für f(x) = {a} · {dz(b)}^x.', f'{dz(b)}^{x} = {dz(b ** x)}; f({x}) = {a} · {dz(b ** x)} = {dz(v)}.',
                'Potenziere die Dezimalzahl sorgfältig (Nachkommastellen addieren sich).', v, f'{a} * {cf(b)} ** {x}')


def g_faktor(s):
    p = R.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 25, 30, 40])
    zu = R.random() < 0.5
    b = 1 + Fr(p, 100) if zu else 1 - Fr(p, 100)
    ding = R.choice(['ein Guthaben', 'eine Einwohnerzahl', 'ein Bestand an Tieren', 'der Wert eines Autos', 'eine Pflanzenfläche', 'die Zahl der Nutzer einer App'])
    if s == 1:
        return zahl(f'{ding[0].upper() + ding[1:]} {"wächst" if zu else "nimmt"} jedes Jahr um {p} % {"" if zu else "ab"}'.rstrip() + '. Wie groß ist der Wachstumsfaktor b?',
                    f'b = 1 {"+" if zu else "−"} {p}/100 = {dz(b)}.', 'Wie viel Prozent bleiben bzw. kommen dazu?', b, f'1 {"+" if zu else "-"} {p} / 100')
    if s == 2:
        a = R.choice([50, 200, 1500, 8000, 120])
        return zahl(f'f(t) = {dz(a)} · {dz(b)}^t beschreibt einen Bestand (t in Jahren). Um wie viel Prozent {"wächst" if zu else "sinkt"} er pro Jahr?',
                    f'b = {dz(b)} {">" if zu else "<"} 1: {"Zunahme" if zu else "Abnahme"} um |{dz(b)} − 1| · 100 % = {p} %.', 'Vergleiche b mit 1.', p,
                    f'abs({cf(b)} - 1) * 100', einheit='%')
    if R.random() < 0.5:
        return auswahl(f'Beschreibt f(t) = {R.choice([20, 300, 5000])} · {dz(b)}^t Wachstum oder Zerfall, und um wie viel Prozent pro Schritt?',
                       f'{"Wachstum" if zu else "Zerfall"} um {p} %',
                       [f'{"Zerfall" if zu else "Wachstum"} um {p} %', f'{"Wachstum" if zu else "Zerfall"} um {dz(b * 100)} %',
                        f'{"Wachstum" if zu else "Zerfall"} um {100 - p} %'],
                       f'b = {dz(b)} {">" if zu else "<"} 1, Änderung {p} % pro Schritt.', 'Ist b größer oder kleiner als 1?')
    n = R.randint(2, 3)
    q = b ** n
    if not endlich(q) or len(dz(q)) > 9: return None
    return zahl(f'{ding[0].upper() + ding[1:]} ändert sich jedes Jahr um {"+" if zu else "−"}{p} %. Um welchen Faktor ändert er sich in {n} Jahren?',
                f'Faktor pro Jahr {dz(b)}; in {n} Jahren {dz(b)}^{n} = {dz(q)}.', 'Die Faktoren werden multipliziert, nicht die Prozente addiert.', q,
                f'{cf(b)} ** {n}')


def g_modell(s):
    if s == 1:
        a, T, k = R.choice([50, 100, 200, 300, 400, 500]), R.choice([2, 3, 4, 5, 6, 20, 30]), R.randint(2, 5)
        t = T * k
        v = a * 2 ** k
        einh = 'min' if T >= 20 else 'h'
        return zahl(f'Eine Kultur enthält zu Beginn {a} Zellen und verdoppelt sich alle {T} {einh}. Wie viele Zellen sind es nach {t} {einh}?',
                    f'{t} : {T} = {k} Verdopplungen: {a} · 2^{k} = {dz(v)}.', 'Wie oft passt die Verdopplungszeit in die Zeitspanne?', v, f'{a} * 2 ** ({t} / {T})')
    if s == 2:
        a = R.choice([20, 40, 50, 80, 100, 250])
        b = R.choice([Fr(3, 2), 2, 3, Fr(5, 4), Fr(6, 5), Fr(1, 2), Fr(4, 5)])
        f1 = a * b
        if not endlich(f1): return None
        return zahl(f'Eine Exponentialfunktion hat f(0) = {a} und f(1) = {dz(f1)}. Bestimme den Wachstumsfaktor b in f(x) = a · b^x.',
                    f'a = f(0) = {a}; b = f(1) : f(0) = {dz(f1)} : {a} = {dz(b)}.', 'Teile zwei aufeinanderfolgende Werte.', b, f'{cf(f1)} / {a}')
    a = R.choice([10, 20, 50, 100, 200])
    b = R.choice([2, 3, Fr(3, 2), Fr(1, 2), Fr(6, 5), Fr(9, 10)])
    x1 = R.randint(1, 3)
    y1, y2 = a * b ** x1, a * b ** (x1 + 2)
    if not (endlich(y1) and endlich(y2)) or len(dz(y2)) > 9: return None
    if R.random() < 0.5:
        return zahl(f'Der Graph von f(x) = a · b^x (b > 0) geht durch P({x1} | {dz(y1)}) und Q({x1 + 2} | {dz(y2)}). Bestimme b.',
                    f'f({x1 + 2}) : f({x1}) = b² = {dz(y2)} : {dz(y1)} = {dz(b * b)} ⇒ b = {dz(b)} (b > 0).', 'Der Quotient der y-Werte ist b hoch Abstand der x-Werte.',
                    b, f'({cf(y2)} / {cf(y1)}) / {cf(b)}')
    return zahl(f'Der Graph von f(x) = a · b^x geht durch P({x1} | {dz(y1)}) und Q({x1 + 2} | {dz(y2)}). Bestimme den Anfangswert a.',
                f'b² = {dz(y2)} : {dz(y1)} ⇒ b = {dz(b)}; a = {dz(y1)} : {dz(b)}^{x1} = {dz(a)}.', 'Erst b bestimmen, dann a aus einem Punkt.', a,
                f'{cf(y1)} / {cf(b)} ** {x1}')


def g_graph(s):
    a = R.choice([1, 2, 3, 4, 5, 10])
    b = R.choice([Fr(1, 2), Fr(1, 3), 2, 3, Fr(3, 2), Fr(4, 5), 5])
    steig = b > 1
    typ = R.choice({1: 'abz', 2: 'abcz', 3: 'cdez'}[s])
    fx = f'f(x) = {a if a != 1 else ""}{" · " if a != 1 else ""}{"(" + br(b) + ")" if not endlich(b) else dz(b)}^x'
    bild = exp_bild(a, b)
    if typ == 'z':
        richtig = (f'{a} · ' if a != 1 else '') + (f'({br(b)})' if not endlich(b) else zt(b)) + '^x'
        andere = [(f'{a} · ' if a != 1 else '') + (f'({br(1 / b)})' if not endlich(1 / b) else zt(1 / b)) + '^x',
                  f'{a + 1} · ' + (f'({br(b)})' if not endlich(b) else zt(b)) + '^x',
                  f'{zt(b)} · {a if a != 1 else 2}^x']
        return mit_grafik(auswahl('Welcher Funktionsterm f(x) passt zum gezeichneten Graphen?', richtig, andere,
                                  f'y-Achsenabschnitt (0 | {a}) ⇒ a = {a}; der Graph {"steigt" if steig else "fällt"} ⇒ b {">" if steig else "<"} 1; f(1) = {zt(a * b)} ⇒ b = {zt(b)}.',
                                  'Lies f(0) ab (das ist a) und vergleiche f(1) mit f(0) (Faktor b).'), bild)
    if typ == 'a':
        return mit_grafik(luecken(f'In welchem Punkt schneidet der Graph von {fx} die y-Achse? (Zur Kontrolle ist der Graph gezeichnet.)', 'S(□ | □)', 'x- und y-Koordinate', [0, a],
                       f'f(0) = {a} · 1 = {a}, also S(0 | {a}).', 'Setze x = 0 ein.', c=['0', f'{a} * {cf(b)} ** 0']), bild)
    if typ == 'b':
        return auswahl(f'Ist der Graph von {fx} steigend oder fallend?', 'steigend' if steig else 'fallend', ['steigend', 'fallend', 'zuerst steigend, dann fallend'],
                       f'b = {zt(b)} {">" if steig else "<"} 1 (und a > 0): {"steigend" if steig else "fallend"}.', 'Vergleiche den Wachstumsfaktor mit 1.')
    if typ == 'c':
        return auswahl(f'Welche Aussage über den Graphen von {fx} ist richtig?', 'Er hat keine Nullstelle.',
                       ['Er schneidet die x-Achse genau einmal.', f'Er geht durch (1 | {a}).', 'Er hat die y-Achse als Asymptote.'],
                       f'{zt(b)}^x ist immer positiv, also auch {a} · {zt(b)}^x > 0. Die x-Achse ist Asymptote. f(1) = {zt(a * b)}.',
                       'Kann a · b^x null werden?')
    if typ == 'd':
        b2 = R.choice([2, 3, 4, 5])
        return auswahl(f'Wie entsteht der Graph von g(x) = (1/{b2})^x aus dem Graphen von f(x) = {b2}^x?', 'durch Spiegelung an der y-Achse',
                       ['durch Spiegelung an der x-Achse', 'durch Verschiebung nach unten', 'durch Spiegelung an der Winkelhalbierenden y = x'],
                       f'(1/{b2})^x = {b2}^(−x) = f(−x): Spiegelung an der y-Achse.', 'Schreibe 1/b als b hoch −1.')
    m = R.choice([1, 2, 3, -1, -2])
    return auswahl(f'Welche Asymptote hat der Graph von g(x) = {b if isinstance(b, int) else 2}^x {plus(m)}?', f'y = {dz(m)}', ['y = 0', f'y = {dz(-m)}', f'x = {dz(m)}'],
                   f'b^x nähert sich 0; um {dz(m)} verschoben nähert sich g(x) dem Wert {dz(m)}.', 'Wohin nähert sich b^x, und was bewirkt die Verschiebung?')


def g_logfunktion(s):
    b = R.choice([2, 3, 4, 5, 10])
    if s == 1:
        n = R.randint(1, {2: 7, 3: 5, 4: 4, 5: 4, 10: 5}[b])
        x = b ** n
        return zahl(f'Berechne f({dz(x)}) für f(x) = {lb(b)}(x).', f'{b}^{n} = {dz(x)}, also f({dz(x)}) = {n}.', 'Mit welchem Exponenten wird die Basis zu x?', n,
                    f'{n} + ({b} ** {n} - {x})')
    typ = R.random()
    if s == 2:
        if typ < 0.5:
            n = R.randint(1, 4)
            x = b ** n
            return luecken(f'Der Graph von g(x) = {b}^x geht durch P({n} | {dz(x)}). Welcher Punkt liegt deshalb auf dem Graphen von f(x) = {lb(b)}(x)?',
                           'Q(□ | □)', 'x- und y-Koordinate', [x, n], f'Umkehrfunktion: Koordinaten tauschen ⇒ Q({dz(x)} | {n}).',
                           'Bei der Umkehrfunktion werden x und y vertauscht.', c=[f'{b} ** {n}', f'{n}'])
        return auswahl(f'Für welche x ist f(x) = {lb(b)}(x) definiert?', 'für alle x > 0', ['für alle x', 'für alle x ≥ 0', 'für alle x ≠ 0'],
                       f'{b}^y ist immer positiv, also gibt es {lb(b)}(x) nur für x > 0.', 'Welche Werte nimmt b^y an?')
    if typ < 0.4:
        n = R.randint(-3, -1)
        x = Fr(b) ** n
        return zahl(f'Berechne f({zt(x)}) für f(x) = {lb(b)}(x).', f'{b}^({dz(n)}) = {zt(x)}, also f({zt(x)}) = {dz(n)}.',
                    'Kehrwerte entstehen durch negative Exponenten.', n, f'{n} + ({b} ** ({n}) - {cf(x)})')
    if typ < 0.7:
        return auswahl(f'Durch welchen Punkt gehen die Graphen aller Funktionen f(x) = log_b(x)?', '(1 | 0)', ['(0 | 1)', '(0 | 0)', '(1 | 1)'],
                       'log_b(1) = 0 für jede Basis b, denn b⁰ = 1.', 'Welcher x-Wert liefert immer den Exponenten 0?') if R.random() < 0.5 else \
            auswahl(f'Welche Funktion ist die Umkehrfunktion von f(x) = {lb(b)}(x)?', f'g(x) = {b}^x', [f'g(x) = x^{b}', f'g(x) = {b}x', f'g(x) = −{lb(b)}(x)'],
                    f'{lb(b)} macht das Potenzieren mit Basis {b} rückgängig; umgekehrt: g(x) = {b}^x.', 'Was hebt den Logarithmus auf?')
    x = R.randint(2, 99)
    v = gerundet(logb(b, x), 2)
    if v is None or abs(logb(b, x) - round(logb(b, x))) < 0.01: return None
    return zahl(f'Berechne f({x}) für f(x) = {lb(b)}(x) auf zwei Nachkommastellen.', f'{lb(b)}({x}) = lg {x} : lg {b} ≈ {dz(v)}.',
                'Mit dem Taschenrechner: lg x : lg b.', v, f'round({K(logb(b, x))}, 2)', tol=0.01)


def g_zeitpunkt(s):
    if s == 1:
        a, b = R.choice([100, 200, 500, 1000]), R.choice([Fr(105, 100), Fr(11, 10), Fr(12, 10), Fr(103, 100), Fr(15, 10)])
        k = R.choice([2, 3, 5, 10])
        t = log(k) / log(float(b))
        v = gerundet(t, 1)
        if v is None: return None
        return zahl(f'f(t) = {a} · {dz(b)}^t. Für welches t ist f(t) = {dz(a * k)}? Runde auf eine Nachkommastelle.',
                    f'{dz(b)}^t = {k} ⇒ t = lg {k} : lg {dz(b)} ≈ {dz(v)}.', 'Erst durch den Anfangswert teilen, dann logarithmieren.', v, f'round({K(t)}, 1)', tol=0.1)
    if s == 2:
        p = R.choice([2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20])
        zu = R.random() < 0.5
        b = 1 + p / 100 if zu else 1 - p / 100
        T = log(2 if zu else 0.5) / log(b)
        v = gerundet(T, 1)
        if v is None: return None
        return zahl(f'Ein Bestand {"wächst" if zu else "nimmt"} um {p} % pro Jahr{"" if zu else " ab"}. Berechne die {"Verdopplungszeit" if zu else "Halbwertszeit"} (eine Nachkommastelle).',
                    f'b = {dz(Fr(100 + (p if zu else -p), 100))}; {"T₂ = lg 2" if zu else "T½ = lg 0,5"} : lg {dz(Fr(100 + (p if zu else -p), 100))} ≈ {dz(v)} Jahre.',
                    'Löse b^T = 2 bzw. b^T = 0,5.', v, f'round({K(T)}, 1)', einheit='Jahre', tol=0.1)
    a, c = R.choice([(80, 20), (100, 10), (60, 15), (500, 100), (90, 30)])
    p = R.choice([5, 8, 10, 15, 20])
    b = 1 - p / 100
    t = log(c / a) / log(b)
    v = gerundet(t, 1)
    if v is None: return None
    return zahl(f'Ein heißes Getränk hat eine Übertemperatur von {a} °C (über der Raumtemperatur), die pro Minute um {p} % abnimmt. Nach wie vielen Minuten beträgt sie nur noch {c} °C (eine Nachkommastelle)?',
                f'{a} · {dz(Fr(100 - p, 100))}^t = {c} ⇒ t = lg({zt(Fr(c, a))}) : lg {dz(Fr(100 - p, 100))} ≈ {dz(v)} min.', 'Modell aufstellen, durch den Anfangswert teilen, logarithmieren.',
                v, f'round({K(t)}, 1)', einheit='min', tol=0.1)


GEN = schoen({'werte': g_werte, 'faktor': g_faktor, 'modell': g_modell, 'graph': g_graph, 'logfunktion': g_logfunktion, 'zeitpunkt': g_zeitpunkt})

if __name__ == '__main__':
    bauen('funktionen.exponential_log',
          'Exponentielles Wachstum und Zerfall mit f(x) = a · b^x beschreiben, Graphen deuten, Logarithmusfunktion als Umkehrung nutzen und Zeitpunkte berechnen.',
          ['f(x) = a · b^x: a = f(0) Anfangswert, b Wachstumsfaktor (b > 1 Wachstum, 0 < b < 1 Zerfall).', 'p % Zunahme: b = 1 + p/100; Abnahme: b = 1 − p/100.',
           'Graph: durch (0 | a), x-Achse als Asymptote, keine Nullstelle.', 'log_b(x) ist Umkehrfunktion von b^x, nur für x > 0; durch (1 | 0).'],
          [('Exponentialfunktion', ['werte', 'faktor', 'modell']), ('Graphen und Logarithmus', ['graph', 'logfunktion']), ('Anwenden', ['zeitpunkt'])],
          ETAPPEN, GEN,
          meiden={'werte': ['f(3) für f(x) = 5 · 2^x', 'f(−1) für f(x) = 5 · 2^x'], 'faktor': ['um 12 % ab.'], 'modell': ['400 Zellen und verdoppelt sich alle 3 h'],
                  'logfunktion': ['P(3 | 8)'], 'zeitpunkt': ['200 · 1,05^t. Für welches t ist f(t) = 300']},
          offen=['Zeichnungen: Jede Lernkarte hat ein Koordinatensystem (Exponential- und Logarithmuskurve, Spiegelung an y = x, Zielwert als waagrechte Linie). Aufgaben „Welcher Term passt zum Graphen?“ und y-Achsenabschnitt zeigen den Graphen.',
                 'Gerundete Ergebnisse mit Toleranz 0,1 bzw. 0,01; Logarithmuswerte als 12-stellige Konstanten in c.'])
