#!/usr/bin/env python3
"""Thema zahlen.rationale_exponenten – Rationale Exponenten und n-te Wurzel (Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(903)
HOCH = str.maketrans('0123456789−-', '⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁻')


def wz(n, a):
    """n-te Wurzel als Text, z. B. ⁴√81"""
    if n == 2: return f'√{a}'
    return f'{str(n).translate(HOCH)}√{a}'


def ex(q):
    """Exponent als Text: x^(2/3), x^3"""
    q = Fr(q)
    return str(q.numerator).replace('-', '−') if q.denominator == 1 else f'({br(q)})'


def pot(b, q):
    return f'{b}^{ex(q)}'


ETAPPEN = [
    {'lernziel': 'nte_wurzel', 'titel': 'n-te Wurzeln berechnen',
     'regel': 'Für a ≥ 0 ist ⟦ⁿ√a⟧ die nicht-negative Zahl, deren n-te Potenz a ergibt. n heißt ⟦Wurzelexponent⟧, a heißt Radikand.',
     'schritte': ['⁴√625: Welche Zahl hoch 4 ergibt 625?', '5⁴ = 25 · 25 = 625, also ⁴√625 = ⟦5⟧.'],
     'probe': '5 · 5 · 5 · 5 = 625 ✓',
     'fehler': '⁴√625 = 625 : 4 ist falsch: Der Wurzelexponent sagt, ⟦wie oft⟧ eine Zahl mit sich selbst multipliziert wird – nicht, wodurch man teilt.'},
    {'lernziel': 'potenz_wert', 'titel': 'Potenzen mit Bruch-Exponent berechnen',
     'regel': 'Für a > 0 gilt: ⟦a^(m/n) = (ⁿ√a)^m = ⁿ√(a^m)⟧. Ein negativer Exponent bedeutet ⟦Kehrwert⟧: a^(−m/n) = 1 / a^(m/n).',
     'schritte': ['27^(2/3): Nenner 3 heißt dritte Wurzel: ³√27 = 3.', 'Zähler 2 heißt quadrieren: 3² = ⟦9⟧.'],
     'probe': '9³ = 729 = 27² ✓',
     'fehler': '27^(2/3) = 27 · 2 : 3 = 18 ist falsch: Der Nenner bedeutet ⟦Wurzel⟧, der Zähler ⟦Potenz⟧ – man multipliziert nicht mit dem Bruch.'},
    {'lernziel': 'umwandeln', 'titel': 'Wurzeln als Potenzen schreiben',
     'regel': '⟦ⁿ√(x^m) = x^(m/n)⟧ für x ≥ 0: Der Wurzelexponent wird zum ⟦Nenner⟧, der Exponent unter der Wurzel zum ⟦Zähler⟧. Den Bruch kürzen.',
     'schritte': ['⁶√(x⁴): Wurzelexponent 6 in den Nenner, Exponent 4 in den Zähler: x^(4/6).', 'Kürzen: ⟦x^(2/3)⟧.'],
     'probe': '(x^(2/3))³ = x² und (⁶√(x⁴))³ = √(x⁴) = x² ✓',
     'fehler': '⁶√(x⁴) = x^(6/4) ist falsch: Zähler und Nenner sind ⟦vertauscht⟧. Der Wurzelexponent gehört in den Nenner.'},
    {'lernziel': 'zusammenfassen', 'titel': 'Potenzen und Wurzeln zusammenfassen',
     'regel': 'Die Potenzgesetze gelten auch für Bruch-Exponenten (Basis > 0): ⟦x^p · x^q = x^(p+q)⟧, ⟦x^p : x^q = x^(p−q)⟧, ⟦(x^p)^q = x^(p·q)⟧.',
     'schritte': ['√x · ³√x = x^(1/2) · x^(1/3) = x^(1/2 + 1/3).', '1/2 + 1/3 = 3/6 + 2/6 = 5/6, also ⟦x^(5/6) = ⁶√(x⁵)⟧.'],
     'probe': '(x^(5/6))⁶ = x⁵ ✓',
     'fehler': 'x^(1/2) · x^(1/3) = x^(1/6) ist falsch: Beim Multiplizieren werden die Exponenten ⟦addiert⟧, nicht multipliziert.'},
    {'lernziel': 'gleichung_exp', 'titel': 'Gleichungen mit Bruch-Exponent (x > 0)',
     'regel': 'Bei x^(m/n) = c (x > 0) potenzierst du beide Seiten mit dem ⟦Kehrwert⟧ n/m: x = ⟦c^(n/m)⟧. Bei xⁿ = c ist die positive Lösung ⁿ√c.',
     'schritte': ['x^(3/2) = 64 mit x > 0: beide Seiten hoch 2/3.', 'x = 64^(2/3) = (³√64)² = 4² = ⟦16⟧.'],
     'probe': '16^(3/2) = (√16)³ = 4³ = 64 ✓',
     'fehler': 'x^(3/2) = 64 ⇒ x = 64 · 2/3 ist falsch: Man ⟦potenziert⟧ mit dem Kehrwert des Exponenten, man multipliziert nicht.'},
    {'lernziel': 'verstehen', 'titel': 'Aussagen über Potenzen prüfen',
     'regel': 'Bruch-Exponenten sind nur für ⟦Basen ≥ 0⟧ (negative Exponenten: > 0) erklärt. Ein negativer Exponent macht das Ergebnis ⟦nicht negativ⟧, sondern zum Kehrwert.',
     'schritte': ['Behauptung: 25^(−1/2) = −5.', '25^(−1/2) = 1 / 25^(1/2) = 1/√25 = ⟦1/5⟧. Die Behauptung ist falsch.'],
     'probe': '(1/5)² = 1/25 = 25^(−1) ✓',
     'fehler': '9^(1/2) = 4,5 ist falsch: Hoch 1/2 bedeutet ⟦Quadratwurzel⟧, nicht halbieren. 9^(1/2) = 3.'},
]


def g_nte_wurzel(s):
    if s == 1:
        n = R.choice([3, 4])
        r = R.randint(2, 5 if n == 3 else 4)
    elif s == 2:
        if R.random() < 0.5:
            n, r = R.choice([4, 5, 6]), Fr(R.randint(1, 5), 10)
            a = r ** n
            return zahl(f'Berechne {wz(n, dz(a))}.', f'{dz(r)}^{n} = {dz(a)}, also {wz(n, dz(a))} = {dz(r)}.',
                        'Ziehe die Wurzel ohne Komma; die Nachkommastellen werden durch ' + str(n) + ' geteilt.', r,
                        f'{float(a)} / {float(r)} ** {n - 1}')
        n = R.choice([4, 5, 6])
        r = R.randint(2, {4: 6, 5: 4, 6: 3}[n])
    else:
        if R.random() < 0.5:
            n1, n2 = R.sample([3, 4, 5], 2)
            r1, r2 = R.randint(2, 4), R.randint(2, 4)
            k = R.randint(2, 5)
            e = k * r1 - r2
            return zahl(f'Berechne {k} · {wz(n1, dz(r1 ** n1))} − {wz(n2, dz(r2 ** n2))}.',
                        f'{wz(n1, dz(r1 ** n1))} = {r1}, {wz(n2, dz(r2 ** n2))} = {r2}; {k} · {r1} − {r2} = {e}.',
                        'Berechne jede Wurzel einzeln, dann Punkt vor Strich.', e,
                        f'{k} * ({r1 ** n1} / {r1} ** {n1 - 1}) - {r2 ** n2} / {r2} ** {n2 - 1}')
        n = R.choice([4, 5, 6])
        b = R.choice([2, 4, 5]) if n != 6 else 2
        a = Fr(1, b ** n)
        return zahl(f'Berechne {wz(n, "(1/" + dz(b ** n) + ")")} als Dezimalzahl.',
                    f'{b}^{n} = {dz(b ** n)}, also {wz(n, "(1/" + dz(b ** n) + ")")} = 1/{b} = {dz(Fr(1, b))}.',
                    'Ziehe die Wurzel aus Zähler und Nenner einzeln.', Fr(1, b), f'1 / ({b ** n} / {b} ** {n - 1})')
    a = r ** n
    return zahl(f'Berechne {wz(n, dz(a))}.', f'{r}^{n} = {dz(a)}, also {wz(n, dz(a))} = {r}.',
                'Welche Zahl ergibt ' + str(n) + '-mal mit sich selbst multipliziert den Radikanden?', r, f'{a} / {r} ** {n - 1}')


def g_potenz_wert(s):
    n = R.choice([2, 3, 4]) if s < 3 else R.choice([2, 3, 4, 5])
    r = R.randint(2, {2: 12, 3: 5, 4: 3, 5: 2}[n])
    m = 1 if s == 1 else R.randint(2, 3 if n > 2 else 5)
    if Fr(m, n).denominator != n: return None
    a = r ** n
    if s == 3:
        e = Fr(1, r ** m)
        t = f'Berechne {pot(dz(a), Fr(-m, n))}.'
        w = f'{pot(dz(a), Fr(-m, n))} = 1 / {pot(dz(a), Fr(m, n))} = 1 / ({wz(n, dz(a))})^{m} = 1 / {r}^{m} = {br(e)}.'
        h = 'Negativer Exponent: Kehrwert bilden. Dann Wurzel (Nenner) und Potenz (Zähler).'
        if endlich(e):
            return zahl(t + ' Gib das Ergebnis als Dezimalzahl an.', w[:-1] + f' = {dz(e)}.', h, e, f'1 / {r} ** {m}')
        return luecken(t, '1/□', 'Nenner', [r ** m], w, h, c=[f'{r} ** {m}'])
    e = r ** m
    return zahl(f'Berechne {pot(dz(a), Fr(m, n))}.',
                f'Nenner {n}: {wz(n, dz(a))} = {r}' + (f'; Zähler {m}: {r}^{m} = {dz(e)}.' if m > 1 else '; Zähler 1: Ergebnis ' + dz(e) + '.'),
                'Der Nenner des Exponenten gibt die Wurzel an, der Zähler die Potenz.', e, f'{r} ** {m}')


def g_umwandeln(s):
    if s == 1:
        n = R.randint(2, 9)
        if R.random() < 0.5:
            return luecken(f'Schreibe {wz(n, "x") if n > 2 else "√x"} (x ≥ 0) als Potenz.', 'x^(□/□)', 'Zähler / Nenner', [1, n],
                           f'{"√x" if n == 2 else wz(n, "x")} = x^(1/{n}): Wurzelexponent {n} wird Nenner.',
                           'Welche Zahl gehört in den Nenner: der Wurzelexponent oder die Hochzahl?', c=['1', f'{n}'])
        m = R.randint(2, 9)
        if Fr(m, n).denominator != n: return None
        return luecken(f'Schreibe {wz(n, "(x" + str(m).translate(HOCH) + ")")} (x ≥ 0) als Potenz mit Bruch-Exponent.', 'x^(□/□)',
                       'Zähler / Nenner', [m, n], f'Wurzelexponent {n} in den Nenner, Exponent {m} in den Zähler: x^({m}/{n}).',
                       'Der Wurzelexponent wird zum Nenner.', c=[f'{m}', f'{n}'])
    if s == 2:
        n, m = R.randint(3, 12), R.randint(2, 10)
        q = Fr(m, n)
        if q.denominator in (1, n): return None
        return luecken(f'Schreibe {wz(n, "(x" + str(m).translate(HOCH) + ")")} (x ≥ 0) als Potenz. Kürze den Exponenten.', 'x^(□/□)',
                       'Zähler / Nenner (gekürzt)', [q.numerator, q.denominator],
                       f'x^({m}/{n}), gekürzt x^({q.numerator}/{q.denominator}).', 'Erst umschreiben, dann den Bruch im Exponenten kürzen.',
                       c=[f'{m} // {m // q.numerator}', f'{n} // {n // q.denominator}'])
    if R.random() < 0.5:
        n, m = R.randint(2, 7), R.randint(2, 7)
        if Fr(m, n).denominator != n: return None
        richtig = wz(n, f'(x{str(m).translate(HOCH)})') if n > 2 else f'√(x{str(m).translate(HOCH)})'
        falsch = [wz(m, f'(x{str(n).translate(HOCH)})') if m > 2 else f'√(x{str(n).translate(HOCH)})', f'x{str(m).translate(HOCH)} : {n}',
                  f'{n} · √(x{str(m).translate(HOCH)})']
        return auswahl(f'Welcher Term ist gleich x^({m}/{n}) für x ≥ 0?', richtig, falsch,
                       f'Nenner {n} wird zum Wurzelexponenten, Zähler {m} zum Exponenten unter der Wurzel: x^({m}/{n}) = {richtig}.',
                       'Welche Zahl wird zum Wurzelexponenten?')
    n = R.randint(2, 8)
    return luecken(f'Schreibe 1/{wz(n, "x") if n > 2 else "√x"} (x > 0) als Potenz.', 'x^(□/□)', 'Zähler (mit Vorzeichen) / Nenner',
                   [-1, n], f'1/{wz(n, "x") if n > 2 else "√x"} = 1/x^(1/{n}) = x^(−1/{n}).',
                   'Ein Bruch mit Potenz im Nenner lässt sich mit negativem Exponenten schreiben.', c=['-1', f'{n}'])


def g_zusammenfassen(s):
    def q_txt(q):
        return f'x^({br(q)})' if q.denominator > 1 else f'x^{dz(q)}'
    typ = R.choice({1: 'm', 2: 'mdp', 3: 'wk'}[s])
    if typ == 'm':
        p, q = Fr(R.randint(1, 5), R.randint(2, 6)), Fr(R.randint(1, 5), R.randint(2, 6))
        e, t, w = p + q, f'{q_txt(p)} · {q_txt(q)}', 'addiert'
    elif typ == 'd':
        p, q = Fr(R.randint(1, 9), R.randint(2, 6)), Fr(R.randint(1, 5), R.randint(2, 6))
        e, t, w = p - q, f'{q_txt(p)} : {q_txt(q)}', 'subtrahiert'
    elif typ == 'p':
        p, q = Fr(R.randint(1, 5), R.randint(2, 6)), Fr(R.randint(1, 5), R.randint(2, 6))
        e, t, w = p * q, f'({q_txt(p)})^({br(q)})', 'multipliziert'
    elif typ == 'w':
        n1, n2 = R.sample([2, 3, 4, 5, 6], 2)
        m1 = R.randint(1, 3)
        p, q = Fr(m1, n1), Fr(1, n2)
        if p.denominator != n1: return None
        w1 = ('√' if n1 == 2 else wz(n1, '')) + (f'(x{str(m1).translate(HOCH)})' if m1 > 1 else 'x')
        w2 = ('√' if n2 == 2 else wz(n2, '')) + 'x'
        e, t, w = p + q, f'{w1} · {w2}', 'addiert'
    else:
        n1, n2 = R.sample([2, 3, 4, 5], 2)
        p, q = Fr(1, n1), Fr(1, n2)
        w1 = ('√' if n1 == 2 else wz(n1, '')) + 'x'
        w2 = ('√' if n2 == 2 else wz(n2, '')) + 'x'
        e, t, w = p - q, f'{w1} : {w2}', 'subtrahiert'
    if p.denominator == 1 or q.denominator == 1 or e.denominator == 1 or e == 0: return None
    return luecken(f'Fasse zu einer Potenz zusammen (x > 0): {t}.', 'x^(□/□)', 'Zähler (mit Vorzeichen) / Nenner, gekürzt',
                   [e.numerator, e.denominator],
                   f'Exponenten {w}: {br(p)} und {br(q)} ergibt {br(e)}, also x^({br(e)}).',
                   'Schreibe Wurzeln als Potenzen und wende das passende Potenzgesetz an.',
                   c=[f'{e.numerator}', f'{e.denominator}'])


def g_gleichung_exp(s):
    if s == 1:
        n = R.choice([2, 3, 4, 5])
        r = R.randint(2, {2: 15, 3: 6, 4: 4, 5: 3}[n])
        c = r ** n
        return zahl(f'Löse x^{n} = {dz(c)} für x > 0.', f'x = {wz(n, dz(c))} = {r}, denn {r}^{n} = {dz(c)}.',
                    'Ziehe auf beiden Seiten die passende Wurzel.', r, f'{c} / {r} ** {n - 1}')
    if s == 2:
        n = R.choice([2, 3, 4])
        c = R.randint(2, {2: 15, 3: 6, 4: 4}[n])
        x = c ** n
        return zahl(f'Löse x^(1/{n}) = {c} für x > 0.', f'Beide Seiten hoch {n}: x = {c}^{n} = {dz(x)}.',
                    'Mit welcher Zahl musst du potenzieren, damit links nur x steht?', x, f'{c} ** {n}')
    m, n = R.choice([(3, 2), (2, 3), (3, 4), (4, 3), (5, 2), (2, 5), (3, 5)])
    r = R.randint(2, {2: 6, 3: 4, 4: 3, 5: 2}[n] if n != 2 else 5)
    # x = r^n  ⇒  x^(m/n) = r^m
    x, c = r ** n, r ** m
    return zahl(f'Löse x^({m}/{n}) = {dz(c)} für x > 0.',
                f'Beide Seiten hoch {n}/{m}: x = {dz(c)}^({n}/{m}) = ({wz(m, dz(c))})^{n} = {r}^{n} = {dz(x)}.',
                'Potenziere mit dem Kehrwert des Exponenten.', x, f'{r} ** {n}')


def g_verstehen(s):
    typ = R.choice({1: 'ab', 2: 'abcd', 3: 'cde'}[s])
    if typ == 'a':
        r = R.randint(2, 12)
        a = r * r
        return auswahl(f'Was ist {a}^(−1/2)?', f'1/{r}', [f'−{r}', f'−{dz(Fr(a, 2))}', f'{dz(Fr(a, 2))}'],
                       f'{a}^(−1/2) = 1 / {a}^(1/2) = 1/√{a} = 1/{r}.', 'Negativer Exponent: Kehrwert. Hoch 1/2: Quadratwurzel.')
    if typ == 'b':
        r = R.randint(2, 15)
        a = r * r
        if a % 2: a2 = dz(Fr(a, 2))
        else: a2 = dz(a // 2)
        return auswahl(f'Jemand rechnet {a}^(1/2) = {a2}. Was stimmt?', f'Falsch, {a}^(1/2) = √{a} = {r}.',
                       ['Richtig, hoch 1/2 bedeutet halbieren.', f'Falsch, {a}^(1/2) = {dz(a * a)}.', f'Falsch, {a}^(1/2) = −{r}.'],
                       f'Hoch 1/2 bedeutet Quadratwurzel: √{a} = {r}, denn {r}² = {a}.', 'Was bedeutet der Nenner 2 im Exponenten?')
    if typ == 'c':
        n = R.choice([3, 5])
        r = R.randint(2, 4)
        a = r ** n
        return auswahl(f'Ist (−{a})^(1/{n}) nach der Definition aus dem Unterricht erklärt?',
                       'Nein, Bruch-Exponenten sind nur für nicht-negative Basen definiert.',
                       [f'Ja, (−{a})^(1/{n}) = −{r}.', f'Ja, (−{a})^(1/{n}) = {r}.', f'Ja, (−{a})^(1/{n}) = −{br(Fr(a, n))}.'],
                       f'Zwar ist (−{r})^{n} = −{a}, aber die Schreibweise a^(1/n) ist nur für a ≥ 0 festgelegt – sonst entstünden Widersprüche (z. B. (−8)^(1/3) und (−8)^(2/6)).',
                       'Für welche Basen ist a^(1/n) festgelegt?')
    if typ == 'd':
        n, k = R.randint(2, 5), R.randint(2, 3)
        return auswahl(f'Welche Aussage gilt für x ≥ 0?', f'x^({k}/{k * n}) = x^(1/{n})',
                       [f'x^({k}/{k * n}) = x^{k}', f'x^({k}/{k * n}) = x^({k * n}/{k})', f'x^({k}/{k * n}) = {k} · x^(1/{n})'],
                       f'Den Bruch im Exponenten darf man kürzen: {k}/{k * n} = 1/{n}.', 'Kann man den Bruch im Exponenten kürzen?')
    r = R.randint(2, 4)
    m, n = R.choice([(2, 3), (3, 2), (3, 4), (2, 5)])
    if n == 2: r = R.randint(2, 9)
    a = r ** n
    return auswahl(f'Jemand rechnet {a}^({m}/{n}) = {a} · {m} : {n}. Was ist richtig?', f'{a}^({m}/{n}) = {dz(r ** m)}',
                   [f'{a}^({m}/{n}) = {br(Fr(a * m, n))}', f'{a}^({m}/{n}) = {br(Fr(a * n, m))}', f'{a}^({m}/{n}) = {dz(r * m)}'],
                   f'Nenner {n}: {wz(n, a)} = {r}; Zähler {m}: {r}^{m} = {dz(r ** m)}.', 'Nenner = Wurzel, Zähler = Potenz.')


import re  # noqa: E402


def _hoch(t):
    return re.sub(r'\^(\d+)', lambda m_: m_.group(1).translate(HOCH), t)


def _schoen(g):
    def f(s):
        a = g(s)
        if a:
            a['f']['text'] = _hoch(a['f']['text'])
            a['w'] = _hoch(a['w'])
            if 'a' in a: a['a'] = [_hoch(x) for x in a['a']]
        return a
    return f


GEN = {'nte_wurzel': g_nte_wurzel, 'potenz_wert': g_potenz_wert, 'umwandeln': g_umwandeln, 'zusammenfassen': g_zusammenfassen,
       'gleichung_exp': g_gleichung_exp, 'verstehen': g_verstehen}
GEN = {k: _schoen(v) for k, v in GEN.items()}

if __name__ == '__main__':
    bauen('zahlen.rationale_exponenten',
          'n-te Wurzeln berechnen, Wurzeln und Potenzen mit rationalen Exponenten ineinander umwandeln und zusammenfassen.',
          ['ⁿ√a (a ≥ 0) ist die nicht-negative Zahl b mit bⁿ = a.', 'a^(m/n) = ⁿ√(a^m) = (ⁿ√a)^m für a ≥ 0 (bei negativem Exponenten a > 0).',
           'a^(−q) = 1/a^q.', 'Potenzgesetze gelten auch für Bruch-Exponenten.'],
          [('n-te Wurzel', ['nte_wurzel', 'potenz_wert']), ('Umwandeln und Zusammenfassen', ['umwandeln', 'zusammenfassen']),
           ('Gleichungen und Verstehen', ['gleichung_exp', 'verstehen'])],
          ETAPPEN, GEN,
          meiden={'nte_wurzel': ['⁴√625.'], 'potenz_wert': ['27^(2/3).'], 'umwandeln': ['⁶√(x⁴)'], 'zusammenfassen': ['√x · ³√x.', 'x^(1/2) · x^(1/3).'],
                  'gleichung_exp': ['= 64 für'], 'verstehen': ['25^(−1/2)', '9^(1/2)']},
          offen=['Exponenten werden als Text „x^(2/3)“ geschrieben, weil die App keine Hochstellung von Brüchen kann. Falls eine Formel-Darstellung kommt, Texte umstellen.',
                 'Gleichungen xⁿ = c mit negativen Lösungen und Lösungsanzahl stehen im Thema gleichungen.potenz; hier nur x > 0.'])
