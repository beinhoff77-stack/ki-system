#!/usr/bin/env python3
"""Thema funktionen.quadratisch – Quadratische Funktionen (Klasse 9)."""
import sys
from math import isqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(907)
SCH = 'S(□ | □)'


def nz(n):
    return R.choice([i for i in range(-n, n + 1) if i != 0])


def sform(a, d, e):
    """Scheitelform als Text: y = a(x − d)² + e"""
    af = '' if a == 1 else '−' if a == -1 else dz(a)
    t = f'y = {af}{minus_klammer(d)}²' if d != 0 else f'y = {af}x²'
    if e: t += f' {plus(e)}'
    return t


ETAPPEN = [
    {'lernziel': 'scheitel', 'titel': 'Scheitelpunkt ablesen',
     'regel': 'In der ⟦Scheitelform⟧ y = a(x − d)² + e liegt der Scheitel bei ⟦S(d | e)⟧. Achtung: In der Klammer steht x ⟦minus⟧ d.',
     'schritte': ['y = 2(x + 3)² − 5 = 2(x − (−3))² + (−5).', 'Also d = −3 und e = −5: ⟦S(−3 | −5)⟧.'],
     'probe': 'x = −3 eingesetzt: 2 · 0² − 5 = −5 ✓',
     'fehler': 'Bei y = (x + 3)² − 5 den Scheitel S(3 | −5) abzulesen ist falsch: x + 3 = x − (−3), also ⟦d = −3⟧.'},
    {'lernziel': 'parameter', 'titel': 'Was bewirken a, d und e?',
     'regel': '⟦a > 0⟧: nach oben geöffnet, ⟦a < 0⟧: nach unten. ⟦|a| > 1⟧ gestreckt (schmaler), ⟦|a| < 1⟧ gestaucht (breiter). d verschiebt nach rechts/links, e nach oben/unten.',
     'schritte': ['y = −0,5(x − 1)² + 4: a = −0,5 < 0 und |a| < 1.', 'Die Parabel ist ⟦nach unten geöffnet, gestaucht⟧ und hat den Scheitel S(1 | 4).'],
     'probe': 'Der Scheitel ist hier der höchste Punkt ✓',
     'fehler': '„y = −3x² ist gestaucht, weil −3 < 1“ ist falsch: Es kommt auf den ⟦Betrag⟧ an. |−3| = 3 > 1, die Parabel ist gestreckt.'},
    {'lernziel': 'umformen', 'titel': 'Von der allgemeinen zur Scheitelform',
     'regel': 'Aus y = ax² + bx + c wird mit ⟦quadratischer Ergänzung⟧ die Scheitelform: a ausklammern, (b/(2a))² ergänzen und wieder abziehen. Kurz: ⟦d = −b/(2a)⟧, e = y(d).',
     'schritte': ['y = x² − 6x + 5 = x² − 6x + 9 − 9 + 5.', '= (x − 3)² − 4, also ⟦S(3 | −4)⟧.'],
     'probe': 'd = −(−6)/(2 · 1) = 3; y(3) = 9 − 18 + 5 = −4 ✓',
     'fehler': 'y = x² − 6x + 5 = (x − 6)² + 5 ist falsch: In die Klammer gehört die ⟦Hälfte⟧ von 6, und die Ergänzung 9 muss wieder ⟦abgezogen⟧ werden.'},
    {'lernziel': 'nullstellen', 'titel': 'Nullstellen bestimmen',
     'regel': 'Nullstellen: ⟦y = 0 setzen⟧ und die quadratische Gleichung lösen. Die ⟦Anzahl⟧ erkennst du an der Diskriminante oder an Scheitel und Öffnung.',
     'schritte': ['y = x² − 2x − 8: 0 = x² − 2x − 8, D = 4 + 32 = 36.', 'x₁,₂ = (2 ± 6)/2: ⟦x₁ = −2, x₂ = 4⟧.'],
     'probe': '(−2)² − 2 · (−2) − 8 = 4 + 4 − 8 = 0 ✓',
     'fehler': '„S(2 | 3), nach oben geöffnet, hat zwei Nullstellen“ ist falsch: Der tiefste Punkt liegt ⟦über⟧ der x-Achse, es gibt ⟦keine⟧ Nullstelle.'},
    {'lernziel': 'punkte', 'titel': 'Funktionswerte und Punktprobe',
     'regel': 'Für den ⟦Funktionswert⟧ x einsetzen und ausrechnen. ⟦Punktprobe⟧: Liegt P(u | v) auf dem Graphen, muss f(u) = v gelten.',
     'schritte': ['f(x) = −x² + 4x + 1, P(3 | 4): f(3) = −9 + 12 + 1.', 'f(3) = 4 = v, also ⟦P liegt auf dem Graphen⟧.'],
     'probe': 'Klammern beim Einsetzen: −(3)² = −9 ✓',
     'fehler': 'Bei f(x) = −x² ist f(−3) = 9 falsch: Erst quadrieren, dann das Minus davor: ⟦−(−3)² = −9⟧.'},
    {'lernziel': 'bestimmen', 'titel': 'Funktionsterm bestimmen',
     'regel': 'Scheitel bekannt: ⟦y = a(x − d)² + e⟧ ansetzen und a mit einem Punkt bestimmen. Nullstellen bekannt: ⟦y = a(x − x₁)(x − x₂)⟧. Drei Punkte: Gleichungssystem.',
     'schritte': ['Scheitel S(1 | −2), Punkt P(3 | 6): y = a(x − 1)² − 2.', '6 = a · 2² − 2 ⇒ 4a = 8 ⇒ ⟦a = 2⟧, also y = 2(x − 1)² − 2.'],
     'probe': 'x = 3: 2 · 4 − 2 = 6 ✓',
     'fehler': '6 = a(3 − 1)² − 2 ⇒ 6 = 2a − 2 ist falsch: Die Klammer wird ⟦quadriert⟧: (3 − 1)² = 4, also 6 = 4a − 2.'},
    {'lernziel': 'extremwert', 'titel': 'Extremwertprobleme lösen',
     'regel': 'Stelle die Größe, die maximal/minimal werden soll, als ⟦quadratische Funktion⟧ einer Variablen auf. Der ⟦Scheitel⟧ liefert das Maximum bzw. Minimum.',
     'schritte': ['Rechteck mit Umfang 20 m: Seiten x und 10 − x, A(x) = x(10 − x) = −x² + 10x.', 'A(x) = −(x − 5)² + 25: Maximum bei ⟦x = 5⟧, A = 25 m² (ein Quadrat).'],
     'probe': 'x = 4: A = 24 < 25 ✓',
     'fehler': 'Beim Umfang 20 m die zweite Seite 20 − x zu nennen ist falsch: Der Umfang enthält ⟦jede Seite zweimal⟧, also 2x + 2y = 20 ⇒ y = 10 − x.'},
]


def g_scheitel(s):
    d, e = R.randint(-9, 9), R.randint(-9, 9)
    if s == 1:
        a = 1
        if R.random() < 0.3: d = 0
    else:
        a = R.choice([-3, -2, -1, 2, 3, 4, Fr(1, 2), Fr(-1, 2)])
    if s == 3 and R.random() < 0.5:
        # Scheitelform mit „+ e“ vorne oder ausgeschrieben
        if e == 0: return None
        txt = f'y = {dz(e)} {"+" if a > 0 else "−"} {"" if abs(a) == 1 else dz(abs(a))}{minus_klammer(d)}²'
        if d == 0: return None
        return luecken(f'Gib den Scheitel der Parabel {txt} an.', SCH, 'x-Wert, y-Wert', [d, e],
                       f'Umgestellt: {sform(a, d, e)}, also S({dz(d)} | {dz(e)}).', 'Ordne zuerst zur Scheitelform y = a(x − d)² + e.',
                       c=[f'{d}', f'{e}'])
    return luecken(f'Gib den Scheitel der Parabel {sform(a, d, e)} an.', SCH, 'x-Wert, y-Wert', [d, e],
                   f'{sform(a, d, e)} ist Scheitelform mit d = {dz(d)} und e = {dz(e)}: S({dz(d)} | {dz(e)}).',
                   'Lies d aus der Klammer (x − d) mit umgedrehtem Vorzeichen ab.', c=[f'{d}', f'{e}'])


def g_parameter(s):
    typ = R.choice({1: 'ab', 2: 'abc', 3: 'cde'}[s])
    if typ == 'a':
        a = R.choice([-4, -3, -2, -1, Fr(-1, 2), Fr(-1, 4), Fr(1, 4), Fr(1, 2), 2, 3, 5])
        d, e = R.randint(-5, 5), R.randint(-5, 5)
        o = 'nach oben' if a > 0 else 'nach unten'
        f = 'gestreckt' if abs(a) > 1 else 'gestaucht' if abs(a) < 1 else 'weder gestreckt noch gestaucht'
        richtig = f'{o} geöffnet, {f}'
        andere = [f'{"nach unten" if a > 0 else "nach oben"} geöffnet, {f}', f'{o} geöffnet, {"gestaucht" if abs(a) > 1 else "gestreckt"}',
                  f'{"nach unten" if a > 0 else "nach oben"} geöffnet, {"gestaucht" if abs(a) > 1 else "gestreckt"}']
        return auswahl(f'Wie sieht die Parabel {sform(a, d, e)} im Vergleich zur Normalparabel aus?', richtig, andere,
                       f'a = {dz(a)}: {"positiv" if a > 0 else "negativ"} ⇒ {o} geöffnet; |a| = {dz(abs(a))} {">" if abs(a) > 1 else "<"} 1 ⇒ {f}.',
                       'Vorzeichen von a: Öffnung. Betrag von a: Streckung oder Stauchung.')
    if typ == 'b':
        d, e = nz(6), nz(6)
        rl = f'{abs(d)} nach {"rechts" if d > 0 else "links"}'
        ou = f'{abs(e)} nach {"oben" if e > 0 else "unten"}'
        richtig = sform(1, d, e)
        andere = [sform(1, -d, e), sform(1, d, -e), sform(1, -d, -e)]
        return auswahl(f'Die Normalparabel wird um {rl} und um {ou} verschoben. Welche Gleichung hat die neue Parabel?', richtig, andere,
                       f'Verschiebung nach {"rechts" if d > 0 else "links"} um {abs(d)}: d = {dz(d)}; nach {"oben" if e > 0 else "unten"} um {abs(e)}: e = {dz(e)}. Also {richtig}.',
                       'Nach rechts verschieben: In der Klammer steht ein Minus.')
    if typ == 'c':
        d, e = nz(8), R.randint(-8, 8)
        return auswahl(f'Jemand liest bei {sform(1, d, e)} den Scheitel S({dz(-d)} | {dz(e)}) ab. Was stimmt?',
                       f'Falsch: S({dz(d)} | {dz(e)}), denn die Klammer ist (x − d).',
                       ['Richtig.', f'Falsch: S({dz(e)} | {dz(d)})', f'Falsch: S({dz(-d)} | {dz(-e)})'],
                       f'{minus_klammer(d)} = x − ({dz(d)}), also d = {dz(d)}. Bei x = {dz(d)} wird die Klammer null.',
                       'Für welches x wird die Klammer null?')
    if typ == 'd':
        a = R.choice([-3, -2, 2, 3])
        b = R.choice([Fr(-1, 2), Fr(1, 3), Fr(1, 2), Fr(-1, 3)])
        if R.random() < 0.5: a, b = b, a
        schmal = a if abs(a) > abs(b) else b
        return auswahl(f'Welche der Parabeln y = {dz(a) if endlich(a) else br(a)}x² und y = {dz(b) if endlich(b) else br(b)}x² ist schmaler?',
                       f'y = {dz(schmal) if endlich(schmal) else br(schmal)}x²', [f'y = {dz(a + b - schmal) if endlich(a + b - schmal) else br(a + b - schmal)}x²', 'beide gleich breit', 'Das hängt vom Vorzeichen ab.'],
                       f'Schmaler ist die Parabel mit dem größeren Betrag von a: |{br(schmal)}| > |{br(a + b - schmal)}|.',
                       'Vergleiche die Beträge von a.')
    e = R.randint(1, 9)
    a = R.choice([-2, -1, 1, 2])
    d = nz(5)
    n = 'zwei' if (a > 0 and e < 0) or (a < 0 and e > 0) else 'keine'
    e = e if R.random() < 0.5 else -e
    n = 'zwei Nullstellen' if (a > 0) != (e > 0) else 'keine Nullstelle'
    return auswahl(f'Ohne zu rechnen: Wie viele Nullstellen hat {sform(a, d, e)}?', n, ['zwei Nullstellen', 'genau eine Nullstelle', 'keine Nullstelle'],
                   f'Scheitel S({dz(d)} | {dz(e)}) liegt {"über" if e > 0 else "unter"} der x-Achse, Parabel {"nach oben" if a > 0 else "nach unten"} geöffnet: {n}.',
                   'Wo liegt der Scheitel, und in welche Richtung ist die Parabel geöffnet?')


def g_umformen(s):
    d, e = nz(7), R.randint(-9, 9)
    a = 1 if s < 3 else R.choice([-2, -1, 2, 3])
    if s == 2 and R.random() < 0.4: a = -1
    b, c = -2 * a * d, a * d * d + e
    allg = f'y = {poly(a, b, c)}'
    if s == 1 and R.random() < 0.5:
        return zahl(f'Bei {allg} liegt der Scheitel bei x = −b/(2a). Berechne die x-Koordinate des Scheitels.',
                    f'x = −({dz(b)})/(2 · {kl(a)}) = {dz(d)}.', 'Lies b und a mit Vorzeichen ab.', d, f'-({b}) / (2 * ({a}))')
    return luecken(f'Bestimme den Scheitel von {allg}.', SCH, 'x-Wert, y-Wert', [d, e],
                   f'Quadratische Ergänzung: {allg} = {sform(a, d, e)[4:]}, also S({dz(d)} | {dz(e)}).',
                   'Klammere a aus (falls nötig) und ergänze die Hälfte des x-Koeffizienten zum Quadrat.',
                   c=[f'-({b}) / (2 * ({a}))', f'({a}) * ({d}) ** 2 + ({b}) * ({d}) + ({c})'])


def g_nullstellen(s):
    if s == 1:
        p, q = sorted(R.sample([i for i in range(-9, 10)], 2))
        return luecken(f'Bestimme die Nullstellen von y = {minus_klammer(p)} · {minus_klammer(q)}.'.replace('x · ', 'x · ').replace('= x ·', '= x ·'),
                       'x₁ = □; x₂ = □', 'kleinere zuerst', [p, q],
                       f'Ein Produkt ist null, wenn ein Faktor null ist: x = {dz(p)} oder x = {dz(q)}.', 'Setze jeden Faktor gleich null.',
                       c=[f'min({p}, {q})', f'max({p}, {q})'])
    if s == 2:
        a = R.choice([1, 1, -1, 2])
        p, q = sorted(R.sample(range(-8, 9), 2))
        b, c = -a * (p + q), a * p * q
        D = b * b - 4 * a * c
        r = isqrt(D)
        return luecken(f'Bestimme die Nullstellen von y = {poly(a, b, c)}.', 'x₁ = □; x₂ = □', 'kleinere zuerst', [p, q],
                       f'0 = {poly(a, b, c)}; D = {dz(D)}; x₁,₂ = ({dz(-b)} ± {r}) / {dz(2 * a)}: {dz(p)} und {dz(q)}.',
                       'Setze y = 0 und löse die quadratische Gleichung.',
                       c=[f'min((-({b}) - {r}) / (2 * ({a})), (-({b}) + {r}) / (2 * ({a})))', f'max((-({b}) - {r}) / (2 * ({a})), (-({b}) + {r}) / (2 * ({a})))'])
    a, b, c = nz(3), nz(8), nz(9)
    D = b * b - 4 * a * c
    n = 'zwei Nullstellen' if D > 0 else 'genau eine Nullstelle' if D == 0 else 'keine Nullstelle'
    return auswahl(f'Wie viele Nullstellen hat der Graph von y = {poly(a, b, c)}?', n, ['zwei Nullstellen', 'genau eine Nullstelle', 'keine Nullstelle'],
                   f'D = {kl(b)}² − 4 · {kl(a)} · {kl(c)} = {dz(D)}, also {n}.', 'Berechne die Diskriminante.')


def g_punkte(s):
    a, b, c = nz(3), R.randint(-6, 6), R.randint(-9, 9)
    u = R.randint(-4, 4)
    fu = a * u * u + b * u + c
    if s == 1:
        return zahl(f'Berechne f({dz(u)}) für f(x) = {poly(a, b, c)}.', f'f({dz(u)}) = {kl(a)} · {kl(u)}² {plus(b)} · {kl(u)} {plus(c)} = {dz(fu)}.',
                    'Setze die Zahl mit Klammern ein: erst Potenz, dann Punkt, dann Strich.', fu, f'({a}) * ({u}) ** 2 + ({b}) * ({u}) + ({c})')
    if s == 2:
        auf = R.random() < 0.5
        v = fu if auf else fu + R.choice([-2, -1, 1, 2, 2 * a * u * u])
        if not auf and v == fu: return None
        return auswahl(f'Liegt P({dz(u)} | {dz(v)}) auf dem Graphen von f(x) = {poly(a, b, c)}?',
                       f'{"Ja" if auf else "Nein"}, denn f({dz(u)}) = {dz(fu)}.',
                       [f'{"Nein" if auf else "Ja"}, denn f({dz(u)}) = {dz(fu)}.', f'{"Ja" if not auf else "Nein"}, denn f({dz(u)}) = {dz(v + 1)}.',
                        f'{"Ja" if auf else "Nein"}, denn f({dz(u)}) = {dz(-fu) if fu else 1}.'],
                       f'f({dz(u)}) = {kl(a)} · {kl(u)}² {plus(b)} · {kl(u)} {plus(c)} = {dz(fu)} {"=" if auf else "≠"} {dz(v)}, also {"liegt P auf" if auf else "liegt P nicht auf"} dem Graphen.', 'Setze die x-Koordinate ein und vergleiche mit der y-Koordinate.')
    if u == 0: return None
    return zahl(f'Der Punkt P({dz(u)} | {dz(fu)}) liegt auf dem Graphen von f(x) = {poly(a, b, 0)} + c. Bestimme c.',
                f'{dz(fu)} = {kl(a)} · {kl(u)}² {plus(b)} · {kl(u)} + c = {dz(a * u * u + b * u)} + c ⇒ c = {dz(c)}.',
                'Setze die Koordinaten von P ein und löse nach c auf.', c, f'({fu}) - (({a}) * ({u}) ** 2 + ({b}) * ({u}))')


def g_bestimmen(s):
    if s == 3 and R.random() < 0.4:
        a, b, c = nz(3), R.randint(-5, 5), R.randint(-6, 6)
        xs = [0, R.choice([1, 2]), R.choice([-1, -2])]
        pts = [(t, a * t * t + b * t + c) for t in xs]
        ptxt = ', '.join(f'({dz(t)} | {dz(y)})' for t, y in pts)
        M = [[t * t, t, 1] for t, _ in pts]
        det = lambda m: m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])  # noqa: E731
        rhs = [y for _, y in pts]
        cs = []
        for j in range(3):
            Mj = [[rhs[i] if k == j else M[i][k] for k in range(3)] for i in range(3)]
            cs.append(f'{det(Mj)} / {det(M)}')
        return luecken(f'Bestimme die Parabel y = ax² + bx + c durch {ptxt}.', 'a = □; b = □; c = □', 'Werte von a, b, c', [a, b, c],
                       f'Aus ({dz(xs[0])} | {dz(pts[0][1])}) folgt c = {dz(c)}; die anderen Punkte liefern a = {dz(a)}, b = {dz(b)}: y = {poly(a, b, c)}.',
                       'Setze die Punkte ein; der Punkt mit x = 0 liefert sofort c.', c=cs)
    if s == 1 or (s == 3 and R.random() < 0.5):
        d, e, a = R.randint(-5, 5), R.randint(-6, 6), nz(3)
        u = d + nz(3)
        v = a * (u - d) ** 2 + e
        return zahl(f'Eine Parabel hat den Scheitel S({dz(d)} | {dz(e)}) und geht durch P({dz(u)} | {dz(v)}). Bestimme a in y = a(x − d)² + e.',
                    f'{dz(v)} = a · ({dz(u)} − {kl(d)})² {plus(e)} = {dz((u - d) ** 2)}a {plus(e)} ⇒ a = {dz(a)}.',
                    'Setze Scheitel und Punkt in die Scheitelform ein.', a, f'(({v}) - ({e})) / (({u}) - ({d})) ** 2')
    p, q = sorted(R.sample(range(-6, 7), 2))
    a = nz(3)
    u = R.choice([t for t in range(-6, 7) if t not in (p, q)])
    v = a * (u - p) * (u - q)
    return zahl(f'Eine Parabel hat die Nullstellen x₁ = {dz(p)} und x₂ = {dz(q)} und geht durch P({dz(u)} | {dz(v)}). Bestimme a in y = a(x − x₁)(x − x₂).',
                f'{dz(v)} = a · ({dz(u)} − {kl(p)})({dz(u)} − {kl(q)}) = {dz((u - p) * (u - q))}a ⇒ a = {dz(a)}.',
                'Setze die Nullstellen in die Produktform ein, dann den Punkt.', a, f'({v}) / ((({u}) - ({p})) * (({u}) - ({q})))')


def g_extremwert(s):
    typ = R.random()
    if s == 1:
        a, d, e = R.choice([-1, -2, 1, 2]), R.randint(-6, 6), R.randint(-9, 9)
        art = 'größten' if a < 0 else 'kleinsten'
        b, c = -2 * a * d, a * d * d + e
        return zahl(f'Welchen {art} Wert nimmt f(x) = {poly(a, b, c)} an?',
                    f'f(x) = {sform(a, d, e)[4:]}; Scheitel S({dz(d)} | {dz(e)}), {"höchster" if a < 0 else "tiefster"} Punkt: {dz(e)}.',
                    'Bestimme den Scheitel; sein y-Wert ist der Extremwert.', e, f'({a}) * ({d}) ** 2 + ({b}) * ({d}) + ({c})')
    if s == 2:
        if typ < 0.5:
            U = 4 * R.randint(3, 30)
            h = U // 4
            return zahl(f'Ein rechteckiges Gehege soll mit {dz(U)} m Zaun umgeben werden. Welchen größten Flächeninhalt kann es haben?',
                        f'Seiten x und {dz(U // 2)} − x: A(x) = −x² + {dz(U // 2)}x = −(x − {dz(h)})² + {dz(h * h)}. Maximum {dz(h * h)} m² (Quadrat).',
                        'Drücke die zweite Seite durch x aus und bestimme den Scheitel von A(x).', h * h, f'({U} / 4) * ({U} / 2 - {U} / 4)', einheit='m²')
        S = 2 * R.randint(5, 40)
        return zahl(f'Zwei Zahlen haben die Summe {S}. Wie groß ist ihr Produkt höchstens?',
                    f'P(x) = x({S} − x) = −(x − {S // 2})² + {dz((S // 2) ** 2)}: höchstens {dz((S // 2) ** 2)} (bei x = {S // 2}).',
                    'Nenne eine Zahl x und drücke die andere durch x aus.', (S // 2) ** 2, f'({S} / 2) * ({S} - {S} / 2)')
    if typ < 0.35:
        L = 4 * R.randint(5, 30)
        x = L // 4
        return zahl(f'An einer Hauswand soll ein rechteckiger Auslauf mit {dz(L)} m Zaun abgegrenzt werden (die Wand ersetzt eine Seite). Welche Fläche ist höchstens möglich?',
                    f'Seiten x, x und {dz(L)} − 2x: A(x) = x({dz(L)} − 2x) = −2(x − {dz(x)})² + {dz(2 * x * x)}. Maximum {dz(2 * x * x)} m².',
                    'Zwei Seiten senkrecht zur Wand heißen x; die dritte Seite ist der Rest des Zauns.', 2 * x * x,
                    f'({L} / 4) * ({L} - 2 * ({L} / 4))', einheit='m²')
    if typ < 0.7:
        v, t = R.choice([(10, 1), (20, 2), (15, Fr(3, 2)), (25, Fr(5, 2)), (30, 3), (5, Fr(1, 2))])
        h0 = R.randint(0, 3) * Fr(1, 2)
        # h(t) = −5t² + v t + h0, Scheitel bei t = v/10
        hmax = -5 * t * t + v * t + h0
        return zahl(f'Ein Ball fliegt nach h(t) = −5t² + {v}t {plus(h0) if h0 else ""}'.rstrip() + ' (t in s, h in m). Wie hoch fliegt er höchstens?',
                    f'Scheitel bei t = −{v}/(2 · (−5)) = {dz(t)} s; h({dz(t)}) = {dz(hmax)} m.',
                    'Die größte Höhe ist der y-Wert des Scheitels. Nutze t = −b/(2a).', hmax,
                    f'-5 * ({v} / 10) ** 2 + {v} * ({v} / 10) + {float(h0)}', einheit='m')
    p0, n0, dp, dn = R.choice([(10, 200, 1, 10), (20, 300, 2, 10), (8, 400, 1, 20), (12, 120, 1, 5), (30, 600, 5, 50)])
    # Preis p = p0 + k·dp, Absatz n = n0 − k·dn, Einnahmen E(k) = (p0 + k dp)(n0 − k dn)
    kopt = Fr(n0 * dp - p0 * dn, 2 * dp * dn)
    if kopt.denominator != 1 or kopt <= 0: return None
    E = (p0 + kopt * dp) * (n0 - kopt * dn)
    return zahl(f'Ein Verein verkauft {n0} Karten zu je {p0} €. Je {dp} € Preiserhöhung werden {dn} Karten weniger verkauft. Welcher Preis bringt die höchsten Einnahmen?',
                f'E(k) = ({p0} + {dp}k)({n0} − {dn}k), Scheitel bei k = {dz(kopt)}: Preis {dz(p0 + kopt * dp)} €, Einnahmen {dz(E)} €.',
                'k = Anzahl der Erhöhungen. Einnahmen = Preis · Anzahl; Scheitel von E(k) bestimmen.', p0 + kopt * dp,
                f'{p0} + (({n0}) * ({dp}) - ({p0}) * ({dn})) / (2 * {dp} * {dn}) * {dp}', einheit='€')


GEN = {'scheitel': g_scheitel, 'parameter': g_parameter, 'umformen': g_umformen, 'nullstellen': g_nullstellen,
       'punkte': g_punkte, 'bestimmen': g_bestimmen, 'extremwert': g_extremwert}

if __name__ == '__main__':
    bauen('funktionen.quadratisch',
          'Parabeln in Scheitelform und allgemeiner Form deuten, Nullstellen bestimmen, Terme aufstellen und Extremwertprobleme lösen.',
          ['Scheitelform y = a(x − d)² + e: Scheitel S(d | e).', 'a > 0 nach oben, a < 0 nach unten; |a| > 1 gestreckt, |a| < 1 gestaucht.',
           'Nullstellen: y = 0 setzen. Anzahl über D oder Scheitel und Öffnung.', 'Extremwert = y-Wert des Scheitels.'],
          [('Parabeln lesen', ['scheitel', 'parameter', 'umformen']), ('Rechnen mit dem Term', ['nullstellen', 'punkte', 'bestimmen']),
           ('Anwenden', ['extremwert'])],
          ETAPPEN, GEN,
          meiden={'scheitel': ['y = 2(x + 3)² − 5 '], 'umformen': ['y = x² − 6x + 5.'], 'nullstellen': ['y = x² − 2x − 8.'],
                  'bestimmen': ['S(1 | −2) und geht durch P(3 | 6)'], 'extremwert': ['mit 20 m Zaun']},
          offen=['Lernkarten „scheitel“ und „parameter“ brauchen Zeichnung: Parabel im Koordinatensystem (Scheitel und Öffnung am Graphen ablesen, Graph einer Gleichung zuordnen). Bisher nur über Terme und Worte.',
                 'Lernkarte „nullstellen“: Nullstellen am Graphen ablesen wäre mit Funktionsgraphen-Zeichnung möglich.',
                 'Parabel durch drei Punkte kommt auch im Thema gleichungen.lgs3 vor (dort ausführlich), hier nur als Stufe-3-Variante.'])
