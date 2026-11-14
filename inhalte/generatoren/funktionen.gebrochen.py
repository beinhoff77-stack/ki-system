#!/usr/bin/env python3
"""Thema funktionen.gebrochen – Gebrochen-rationale Funktionen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, Z, baue, cz, ist_endlich, kl, lin, zt  # noqa: E402

META = {'thema_schluessel': 'funktionen.gebrochen', 'thema_id': 34, 'block_id': 71, 'klasse': {'gym_by': 8}}

ETAPPEN = [
    {'lernziel': 'indirekt', 'titel': 'Indirekte Proportionalität',
     'regel': 'Bei einer ⟦indirekten Proportionalität⟧ gehört zum Doppelten von x die Hälfte von y. Das ⟦Produkt x · y⟧ ist immer gleich: y = k/x. Der Graph ist eine ⟦Hyperbel⟧.',
     'schritte': ['4 Pumpen leeren ein Becken in 6 Stunden.', 'Produkt: 4 · 6 = 24 (Pumpen-Stunden)', '3 Pumpen brauchen 24 : 3 = ⟦8 Stunden⟧.'],
     'fehler': 'Mehr Pumpen brauchen ⟦weniger⟧ Zeit. Wer 6 : 4 · 3 = 4,5 h rechnet, behandelt die Zuordnung fälschlich als direkt proportional.',
     '_verbot': ['4 Pumpen']},
    {'lernziel': 'definitionsmenge', 'titel': 'Definitionsmenge von a/(x + b) + c',
     'regel': 'f(x) = a/(x + b) + c ist für ⟦x = −b⟧ nicht definiert, weil dann der Nenner 0 ist. Also ⟦D = ℚ \\ {−b}⟧.',
     'schritte': ['f(x) = 3/(x − 2) + 1', 'Nenner x − 2 = 0 für x = 2', '⟦D = ℚ \\ {2}⟧'],
     'fehler': 'Bei f(x) = 3/(x − 2) + 1 fehlt nicht −2 in D: Der Nenner x − 2 wird für ⟦x = +2⟧ null. Das Vorzeichen dreht sich um.',
     '_verbot': ['3/(x − 2) + 1']},
    {'lernziel': 'asymptoten', 'titel': 'Asymptoten bestimmen',
     'regel': 'Eine ⟦Asymptote⟧ ist eine Gerade, der sich der Graph immer mehr nähert. Bei f(x) = a/(x + b) + c: ⟦senkrechte⟧ Asymptote x = −b, ⟦waagrechte⟧ Asymptote y = c.',
     'schritte': ['f(x) = 2/(x + 4) − 3', 'Senkrecht: x + 4 = 0 → ⟦x = −4⟧', 'Waagrecht: ⟦y = −3⟧ (für große x wird 2/(x + 4) fast 0)'],
     'fehler': 'Die waagrechte Asymptote von 2/(x + 4) − 3 ist nicht y = 2. Der Zähler a bestimmt sie nicht, sondern die ⟦Verschiebung c = −3⟧.',
     '_verbot': ['2/(x + 4) − 3']},
    {'lernziel': 'achsenpunkte', 'titel': 'Schnittpunkte mit den Achsen',
     'regel': '⟦y-Achse⟧: x = 0 einsetzen (falls 0 in D). ⟦x-Achse⟧ (Nullstelle): f(x) = 0 lösen. Ist c = 0, gibt es ⟦keine⟧ Nullstelle, weil a/(x + b) nie 0 ist.',
     'schritte': ['f(x) = 6/(x + 1) − 2', 'y-Achse: f(0) = 6 − 2 = 4 → (0 | 4)', 'Nullstelle: 6/(x + 1) = 2 → x + 1 = 3 → ⟦x = 2⟧'],
     'fehler': 'f(x) = 5/(x − 1) hat keine Nullstelle bei x = 0: f(0) = −5. Ein Bruch ist nur 0, wenn der ⟦Zähler 0⟧ ist – und 5 ist nie 0.',
     '_verbot': ['6/(x + 1) − 2']},
    {'lernziel': 'parameter', 'titel': 'Verschieben: Einfluss von b und c',
     'regel': 'Der Graph von a/(x + b) + c entsteht aus a/x durch Verschieben: um ⟦−b in x-Richtung⟧ (bei x − 3 also 3 nach ⟦rechts⟧) und um ⟦c in y-Richtung⟧.',
     'schritte': ['f(x) = 1/(x − 3) + 2 aus g(x) = 1/x', 'x − 3: um 3 nach rechts', '+ 2: um 2 nach oben. ⟦Asymptoten x = 3, y = 2⟧'],
     'fehler': 'Bei 1/(x − 3) geht es nicht nach links: Das Minus in der Klammer bedeutet eine Verschiebung nach ⟦rechts⟧ (die Lücke liegt bei x = 3).',
     '_verbot': ['1/(x − 3) + 2']},
    {'lernziel': 'beurteilen', 'titel': 'Aussagen über Hyperbeln prüfen',
     'regel': 'Prüfe Aussagen mit D, den Asymptoten und Funktionswerten. Wichtig: Der Graph von a/(x + b) + c berührt ⟦keine⟧ seiner beiden Asymptoten.',
     'schritte': ['Aussage: „f(x) = 4/x + 1 nimmt den Wert 1 an.“', '4/x = 0 hat keine Lösung.', 'Die Aussage ist ⟦falsch⟧: y = 1 ist die waagrechte Asymptote.'],
     'fehler': 'Dass sich der Graph der Asymptote nähert, heißt nicht, dass er sie irgendwann erreicht. a/(x + b) wird ⟦nie genau 0⟧.',
     '_verbot': ['4/x + 1']},
]


def nz(R, lo=-6, hi=6):
    return R.choice([k for k in range(lo, hi + 1) if k])


def ft(a, b, c):
    """a/(x + b) + c als Text."""
    s = f'{zt(a)}/x' if b == 0 else f'{zt(a)}/({lin(1, b)})'
    if c: s += f' {"+" if c > 0 else "−"} {zt(abs(c))}'
    return s


def g_indirekt(R, st):
    if st == 1:
        k = R.choice([12, 18, 24, 30, 36, 48, 60, 72, 120])
        x1 = R.choice([d for d in range(2, 13) if k % d == 0]); x2 = R.choice([d for d in range(1, 25) if k % d == 0 and d != x1])
        art = R.choice(['maler', 'pumpen', 'kiste'])
        if art == 'maler':
            t = f'{x1} Maler streichen ein Haus in {k // x1} Tagen. Wie viele Tage brauchen {x2} Maler (bei gleicher Arbeitsweise)?'
        elif art == 'pumpen':
            t = f'{x1} gleiche Pumpen leeren einen Teich in {k // x1} Stunden. Wie viele Stunden brauchen {x2} Pumpen?'
        else:
            t = f'Ein Vorrat reicht für {x1} Tiere {k // x1} Tage. Wie viele Tage reicht er für {x2} Tiere?'
        return Z(t, Fr(k, x2), f'{x1} * {k // x1} / {x2}', f'Produkt: {x1} · {k // x1} = {k}. {k} : {x2} = {zt(Fr(k, x2))}.',
                 'Mehr ... – weniger ...: Berechne zuerst das konstante Produkt.')
    if st == 2:
        if R.random() < .5:
            v1 = R.choice([40, 50, 60, 80, 90, 100, 120]); t1 = Fr(R.choice([2, 3, 4, 5, 6]), R.choice([1, 2]))
            s = v1 * t1; v2 = R.choice([v for v in (30, 40, 45, 50, 60, 75, 80, 100, 120, 150) if v != v1])
            t2 = s / v2
            if not ist_endlich(t2): return g_indirekt(R, st)
            return Z(f'Mit {v1} km/h dauert eine Fahrt {zt(t1)} h. Wie lange dauert sie mit {v2} km/h?', t2, f'{v1} * {cz(t1)} / {v2}',
                     f'v · t ist die Strecke: {v1} · {zt(t1)} = {zt(s)} km. t = {zt(s)} : {v2} = {zt(t2)} h.', 'Geschwindigkeit · Zeit = Strecke bleibt gleich.', einheit='h')
        k = R.choice([12, 24, 36, 48, 60]); xs = R.sample([d for d in range(1, 13) if k % d == 0], 3)
        x0 = R.choice([d for d in range(1, 61) if k % d == 0 and d not in xs])
        ps = ', '.join(f'({x} | {k // x})' for x in xs)
        return Z(f'Die Tabelle {ps} gehört zu einer indirekten Proportionalität. Welcher y-Wert gehört zu x = {x0}?', Fr(k, x0), f'{xs[0]} * {k // xs[0]} / {x0}',
                 f'x · y = {xs[0]} · {k // xs[0]} = {k}. y = {k} : {x0} = {zt(Fr(k, x0))}.', 'Berechne das Produkt x · y.')
    k = R.choice([12, 18, 24, 30, 36])
    xs = sorted(R.sample([d for d in range(1, 13) if k % d == 0], 3))
    art = R.choice(['indirekt', 'direkt', 'keine'])
    if art == 'indirekt': ys = [k // x for x in xs]
    elif art == 'direkt': ys = [2 * x for x in xs]
    else: ys = [k // xs[0], k // xs[0] - 2, k // xs[0] - 3]
    ps = ', '.join(f'({x} | {y})' for x, y in zip(xs, ys))
    opts = {'indirekt': 'indirekt proportional', 'direkt': 'direkt proportional', 'keine': 'weder direkt noch indirekt proportional'}
    prod = ', '.join(str(x * y) for x, y in zip(xs, ys)); quot = ', '.join(zt(Fr(y, x)) for x, y in zip(xs, ys))
    return A(R, f'Wie ist die Zuordnung {ps}?', opts[art], [v for kk, v in opts.items() if kk != art] + ['indirekt, weil y kleiner wird'] if art == 'keine' else [v for kk, v in opts.items() if kk != art],
             f'Produkte x · y: {prod}. Quotienten y : x: {quot}. ' + {'indirekt': 'Produkte gleich → indirekt.', 'direkt': 'Quotienten gleich → direkt.', 'keine': 'Weder Produkte noch Quotienten sind gleich.'}[art],
             'Prüfe: Sind alle Produkte x · y gleich? Sind alle Quotienten y : x gleich?')


def g_definitionsmenge(R, st):
    a, b, c = nz(R, -9, 9), nz(R, -8, 8), R.randint(-6, 6)
    if st == 3:
        k = R.choice([2, 4, 5]); m = R.choice([j for j in range(-9, 10) if j % k])
        T = f'{zt(a)}/({lin(k, m)}){"" if not c else (" + " if c > 0 else " − ") + str(abs(c))}'
        x0 = Fr(-m, k)
        return Z(f'Welche Zahl gehört nicht zur Definitionsmenge von f(x) = {T}?', x0, f'-({m}) / {k}',
                 f'{lin(k, m)} = 0 → x = {zt(x0)}. D = ℚ \\ {{{zt(x0)}}}.', 'Setze den Nenner gleich 0 und löse.')
    if st == 1 or R.random() < .5:
        return A(R, f'Gib die Definitionsmenge von f(x) = {ft(a, b, c)} an.', f'D = ℚ \\ {{{zt(-b)}}}',
                 [f'D = ℚ \\ {{{zt(b)}}}', 'D = ℚ', f'D = ℚ \\ {{{zt(c)}}}' if c not in (b, -b) else 'D = ℚ \\ {0}'],
                 f'Nenner {lin(1, b)} = 0 für x = {zt(-b)}. D = ℚ \\ {{{zt(-b)}}}.', 'Welche Zahl macht den Nenner 0? Achte auf das Vorzeichen.')
    return Z(f'Welche Zahl gehört nicht zur Definitionsmenge von f(x) = {ft(a, b, c)}?', -b, f'-({b})',
             f'Nenner {lin(1, b)} = 0 für x = {zt(-b)}.', 'Welche Zahl macht den Nenner 0?')


def g_asymptoten(R, st):
    a, b, c = nz(R, -9, 9), R.choice([0] + [k for k in range(-8, 9) if k]) if st == 1 else nz(R, -8, 8), nz(R, -6, 6)
    if st == 3 and R.random() < .5:
        # Term aus Asymptoten bestimmen
        r = ft(a, b, c)
        f = [ft(a, -b, c), ft(a, b, -c), ft(a, c, b) if c != b else ft(a, -c, -b)]
        return A(R, f'Eine Hyperbel f(x) = {zt(a)}/(x + b) + c hat die Asymptoten x = {zt(-b)} und y = {zt(c)}. Wie heißt der Term?', f'f(x) = {r}', [f'f(x) = {t}' for t in f],
                 f'x = {zt(-b)} → b = {zt(b)}; y = {zt(c)} → c = {zt(c)}. f(x) = {r}.', 'Die senkrechte Asymptote liegt bei x = −b, die waagrechte bei y = c.')
    if R.random() < .5:
        return Z(f'Gib die senkrechte Asymptote von f(x) = {ft(a, b, c)} an. x = □', -b, f'-({b})',
                 f'Nenner {lin(1, b)} = 0 für x = {zt(-b)}. Senkrechte Asymptote: x = {zt(-b)}.', 'Wo ist der Nenner 0?')
    return Z(f'Gib die waagrechte Asymptote von f(x) = {ft(a, b, c)} an. y = □', c, f'{c}',
             f'Für sehr große x wird {zt(a)}/({lin(1, b)}) fast 0. Also nähert sich f dem Wert {zt(c)}: y = {zt(c)}.', 'Was bleibt übrig, wenn der Bruch fast 0 wird?')


def g_achsenpunkte(R, st):
    while True:
        a, b, c = nz(R, -12, 12), nz(R, -6, 6), R.randint(-6, 6)
        y0 = Fr(a, b) + c
        x0 = Fr(-a, c) - b if c else None
        if st == 1:
            if ist_endlich(y0) and len(zt(y0)) <= 5: break
        else:
            if c and ist_endlich(x0) and len(zt(x0)) <= 5 and x0 != -b: break
    if st == 1:
        return Z(f'In welchem Punkt schneidet der Graph von f(x) = {ft(a, b, c)} die y-Achse? Gib den y-Wert an.', y0, f'{a} / ({b}) + ({c})',
                 f'f(0) = {zt(a)}/{kl(b)}{"" if not c else (" + " if c > 0 else " − ") + str(abs(c))} = {zt(y0)}.', 'Auf der y-Achse ist x = 0.')
    if st == 3 and R.random() < .35:
        a, b = nz(R, -9, 9), nz(R, -6, 6)
        return A(R, f'Welche Nullstelle hat f(x) = {ft(a, b, 0)}?', 'keine Nullstelle', [f'x = {zt(-b)}', 'x = 0', f'x = {zt(a)}'],
                 f'{zt(a)}/({lin(1, b)}) = 0 wäre nur möglich, wenn der Zähler {zt(a)} null wäre. Keine Nullstelle.', 'Wann ist ein Bruch gleich 0?')
    return Z(f'Berechne die Nullstelle von f(x) = {ft(a, b, c)}.', x0, f'-({a}) / ({c}) - ({b})',
             f'{zt(a)}/({lin(1, b)}) = {zt(-c)} → {lin(1, b)} = {zt(a)} : {kl(-c)} = {zt(Fr(-a, c))} → x = {zt(x0)}.',
             'Setze f(x) = 0, bringe c auf die andere Seite und multipliziere mit dem Nenner.')


def verschiebung(b, c):
    t = []
    if b: t.append(f'um {zt(abs(b))} nach {"links" if b > 0 else "rechts"}')
    if c: t.append(f'um {zt(abs(c))} nach {"oben" if c > 0 else "unten"}')
    return ' und '.join(t)


def g_parameter(R, st):
    a, b, c = nz(R, -6, 6), nz(R, -7, 7), nz(R, -6, 6)
    if st == 1:
        c = 0 if R.random() < .5 else c
        if c: b = 0
        T = ft(a, b, c)
        r = verschiebung(b, c)
        f = [verschiebung(-b, -c), verschiebung(c, b) if b else verschiebung(-c, 0) or 'um 1 nach oben', 'gar nicht – der Graph ist gleich']
        return A(R, f'Wie entsteht der Graph von f(x) = {T} aus dem Graphen von g(x) = {zt(a)}/x?', f'Verschiebung {r}', [x if x.startswith('gar') else f'Verschiebung {x}' for x in f if x],
                 (f'Im Nenner steht {lin(1, b)}: Verschiebung {verschiebung(b, 0)}.' if b else f'{"+" if c > 0 else "−"} {abs(c)} hinter dem Bruch: Verschiebung {verschiebung(0, c)}.'),
                 'Steht in der Klammer x − 3, geht es nach rechts. + c verschiebt nach oben.')
    if st == 2:
        T = ft(a, b, c)
        r = verschiebung(b, c)
        f = [verschiebung(-b, c), verschiebung(b, -c), verschiebung(-b, -c)]
        return A(R, f'Wie entsteht der Graph von f(x) = {T} aus dem Graphen von g(x) = {zt(a)}/x?', f'Verschiebung {r}', [f'Verschiebung {x}' for x in f],
                 f'Asymptoten von f: x = {zt(-b)}, y = {zt(c)}. Bei g: x = 0, y = 0. Also Verschiebung {r}.', 'Vergleiche die Asymptoten von f und g.')
    r = ft(a, b, c)
    f = [ft(a, -b, c), ft(a, b, -c), ft(a, -b, -c)]
    return A(R, f'Der Graph von g(x) = {zt(a)}/x wird {verschiebung(b, c)} verschoben. Wie heißt der neue Funktionsterm?', f'f(x) = {r}', [f'f(x) = {x}' for x in f],
             f'{verschiebung(b, 0)}: x wird zu {lin(1, b)}. {verschiebung(0, c)}: + {kl(c)}. f(x) = {r}.', 'Nach rechts um d: x − d in die Klammer. Nach oben um e: + e.')


def g_beurteilen(R, st):
    while True:
        a, b, c = nz(R, -8, 8), nz(R, -6, 6), nz(R, -5, 5)
        x0 = Fr(-a, c) - b
        if ist_endlich(x0) and x0 != -b and len(zt(x0)) <= 5: break
    f = lambda x: Fr(a) / (x + b) + c
    T = ft(a, b, c)
    x1 = R.choice([k for k in range(-5, 6) if k != -b])
    al = [
        (f'Der Graph schneidet die Gerade y = {zt(c)}.', False), (f'f ist für x = {zt(-b)} nicht definiert.', True),
        (f'f ist für x = {zt(b)} nicht definiert.', b == -b), (f'Die Nullstelle ist x = {zt(x0)}.', True),
        (f'f({zt(x1)}) = {zt(f(Fr(x1)))}', True), (f'f({zt(x1)}) = {zt(f(Fr(x1)) + 1)}', False),
        (f'Die waagrechte Asymptote ist y = {zt(a)}.', a == c), (f'Die senkrechte Asymptote ist x = {zt(-b)}.', True),
        (f'Der Graph hat zwei Nullstellen.', False), (f'Der Graph schneidet die y-Achse bei y = {zt(f(Fr(0)))}.', True),
    ]
    al = [(t, w) for t, w in al if not (t.startswith('f(') and not ist_endlich(f(Fr(x1))))]
    wahr = [t for t, w in al if w]; falsch = [t for t, w in al if not w]
    if st == 1 or (st == 2 and R.random() < .5):
        t = R.choice(wahr)
        return A(R, f'Welche Aussage über f(x) = {T} ist richtig?', t, R.sample(falsch, 3),
                 f'Richtig: {t} Asymptoten x = {zt(-b)}, y = {zt(c)}; Nullstelle {zt(x0)}.', 'Bestimme D, Asymptoten und Nullstelle, dann vergleiche.')
    t = R.choice(falsch)
    return A(R, f'Welche Aussage über f(x) = {T} ist FALSCH?', t, R.sample(wahr, 3),
             f'Falsch: {t} Asymptoten x = {zt(-b)}, y = {zt(c)}; der Graph berührt die Asymptoten nie.', 'Bestimme D, Asymptoten und Nullstelle, dann vergleiche.')


GEN = {'indirekt': g_indirekt, 'definitionsmenge': g_definitionsmenge, 'asymptoten': g_asymptoten, 'achsenpunkte': g_achsenpunkte,
       'parameter': g_parameter, 'beurteilen': g_beurteilen}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Indirekte Proportionalität', ['indirekt']), ('Hyperbeln untersuchen', ['definitionsmenge', 'asymptoten', 'achsenpunkte']),
          ('Parameter und Verstehen', ['parameter', 'beurteilen'])],
         'Indirekte Proportionalitäten erkennen und Funktionen f(x) = a/(x + b) + c untersuchen: Definitionsmenge, Asymptoten, Achsenschnittpunkte, Verschiebungen.',
         ['Indirekt proportional: x · y = konstant, y = k/x.', 'f(x) = a/(x + b) + c: D = ℚ \\ {−b}, Asymptoten x = −b und y = c.',
          'x − 3 in der Klammer: 3 nach rechts. + c: c nach oben.'],
         offen=['Lehrplan: Graphen mit Asymptoten zeichnen. Die App kann keine Hyperbeln und Asymptoten zeichnen; Aufgaben „Welcher Graph gehört zu …?“ fehlen.'])
