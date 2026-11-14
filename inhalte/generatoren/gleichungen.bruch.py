#!/usr/bin/env python3
"""Thema gleichungen.bruch – Bruch- und Verhältnisgleichungen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, Z, baue, cz, ist_endlich, kl, lin, zt  # noqa: E402

META = {'thema_schluessel': 'gleichungen.bruch', 'thema_id': 5, 'block_id': 60, 'klasse': {'gym_by': 8, 'rs_by': 8}}

ETAPPEN = [
    {'lernziel': 'definitionsmenge', 'titel': 'Definitionsmenge einer Bruchgleichung',
     'regel': 'Bei einer ⟦Bruchgleichung⟧ steht x im Nenner. Bevor du rechnest, schließt du alle Zahlen aus, die einen ⟦Nenner 0⟧ machen.',
     'schritte': ['2/(x − 1) = 3/(x + 4)', 'x − 1 = 0 für x = 1; x + 4 = 0 für x = −4.', '⟦D = ℚ \\ {−4; 1}⟧'],
     'fehler': 'Bei 2/(x − 1) = 3/(x + 4) reicht es nicht, nur x = 1 auszuschließen. ⟦Jeder⟧ Nenner zählt, auch der auf der rechten Seite.',
     '_verbot': ['2/(x − 1) = 3/(x + 4)']},
    {'lernziel': 'ein_bruch', 'titel': 'Bruchgleichungen mit einem Bruch',
     'regel': 'Multipliziere beide Seiten mit dem ⟦Nenner⟧. Dann ist der Bruch weg und du löst eine lineare Gleichung. Zum Schluss prüfst du, ob die Lösung in ⟦D⟧ liegt.',
     'schritte': ['12/(x − 2) = 3   D = ℚ \\ {2}', '| · (x − 2): 12 = 3(x − 2) = 3x − 6', '18 = 3x → ⟦x = 6⟧, 6 liegt in D.'],
     'probe': '12/(6 − 2) = 12/4 = 3 ✓',
     'fehler': 'Aus 12/(x − 2) = 3 wird nicht 12 = 3x − 2. Der Nenner wird als ⟦Ganzes⟧ multipliziert: 3 · (x − 2) = 3x − 6.',
     '_verbot': ['12/(x − 2) = 3']},
    {'lernziel': 'ueber_kreuz', 'titel': 'Zwei Brüche: über Kreuz multiplizieren',
     'regel': 'Steht auf jeder Seite genau ein Bruch, multiplizierst du ⟦über Kreuz⟧: aus a/b = c/d wird a · d = c · b.',
     'schritte': ['4/(x + 1) = 2/(x − 3)   D = ℚ \\ {−1; 3}', 'Über Kreuz: 4(x − 3) = 2(x + 1)', '4x − 12 = 2x + 2 → 2x = 14 → ⟦x = 7⟧'],
     'probe': '4/8 = 0,5 und 2/4 = 0,5 ✓',
     'fehler': 'Über Kreuz heißt Zähler links mal Nenner ⟦rechts⟧. 4 · (x + 1) = 2 · (x − 3) ist falsch – das sind Zähler und Nenner derselben Seite.',
     '_verbot': ['4/(x + 1) = 2/(x − 3)']},
    {'lernziel': 'hauptnenner', 'titel': 'Mit dem Hauptnenner multiplizieren',
     'regel': 'Stehen mehrere Brüche in der Gleichung, multiplizierst du ⟦jedes Glied⟧ mit dem ⟦Hauptnenner⟧. Danach kommt kein Bruch mehr vor.',
     'schritte': ['5/x + 1/(2x) = 2   HN = 2x', '| · 2x: 10 + 1 = 4x', '11 = 4x → ⟦x = 2,75⟧'],
     'fehler': 'Beim Multiplizieren mit dem Hauptnenner darf kein Glied vergessen werden: Auch die ⟦2 auf der rechten Seite⟧ wird mit 2x multipliziert.',
     '_verbot': ['5/x + 1/(2x) = 2']},
    {'lernziel': 'scheinloesung', 'titel': 'Lösung prüfen: Gehört sie zu D?',
     'regel': 'Eine errechnete Zahl ist nur dann Lösung, wenn sie in ⟦D⟧ liegt. Sonst ist sie eine ⟦Scheinlösung⟧ und die Lösungsmenge ist leer: L = { }.',
     'schritte': ['(x + 1)/(x − 3) = 4/(x − 3)   D = ℚ \\ {3}', '| · (x − 3): x + 1 = 4 → x = 3', '3 liegt nicht in D: ⟦L = { }⟧'],
     'fehler': 'L = {3} ist hier falsch: Für x = 3 wird der Nenner 0, die Gleichung hat dort ⟦keinen Sinn⟧. Deshalb immer zuerst D bestimmen.',
     '_verbot': ['(x + 1)/(x − 3) = 4/(x − 3)']},
    {'lernziel': 'verhaeltnis', 'titel': 'Verhältnisgleichungen',
     'regel': 'Eine ⟦Verhältnisgleichung⟧ hat die Form a : b = c : d. Es gilt die ⟦Produktgleichheit⟧: a · d = b · c (Außenglieder mal = Innenglieder mal).',
     'schritte': ['x : 6 = 10 : 4', 'Produktgleichheit: 4x = 6 · 10 = 60', '⟦x = 15⟧'],
     'fehler': 'Bei x : 6 = 10 : 4 ist x nicht 6 · 4 : 10. Die ⟦Außenglieder⟧ x und 4 werden multipliziert, ebenso die Innenglieder 6 und 10.',
     '_verbot': ['x : 6 = 10 : 4']},
]


def N(a, b):
    """Nenner a·x + b mit Klammern."""
    return f'({lin(a, b)})' if b else lin(a, b) if a != 1 else 'x'


def mengentext(xs):
    xs = sorted(set(xs))
    return 'ℚ' if not xs else 'ℚ \\ {' + '; '.join(zt(x) for x in xs) + '}'


def g_definitionsmenge(R, st):
    if st == 1:
        b, a, c = R.choice([k for k in range(-9, 10) if k]), R.randint(1, 12), R.randint(1, 9)
        G = f'{a}/{N(1, -b)} = {c}'
        return A(R, f'Bestimme die Definitionsmenge von {G}.', mengentext([b]), [mengentext([-b]), mengentext([0]), mengentext([b, c])],
                 f'Nenner {lin(1, -b)} = 0 für x = {zt(b)}. D = {mengentext([b])}.', 'Setze den Nenner gleich 0.')
    if st == 2:
        b, d = R.sample([k for k in range(-9, 10) if k], 2)
        G = f'{R.randint(1, 9)}/{N(1, -b)} = {R.randint(1, 9)}/{N(1, -d)}'
        return A(R, f'Bestimme die Definitionsmenge von {G}.', mengentext([b, d]), [mengentext([b]), mengentext([d]), mengentext([-b, -d])],
                 f'Linker Nenner 0 für x = {zt(b)}, rechter für x = {zt(d)}. D = {mengentext([b, d])}.', 'Jeder Nenner liefert eine ausgeschlossene Zahl.')
    k = R.choice([2, 3, 4, 5]); m = R.choice([j for j in range(-12, 13) if j and j % k == 0])
    b = R.choice([j for j in range(-6, 7) if j and j != m // k])
    G = f'{R.randint(1, 9)}/{N(k, -m)} = {R.randint(1, 9)}/(x{N(1, -b)})'
    return A(R, f'Bestimme die Definitionsmenge von {G}.', mengentext([m // k, 0, b]), [mengentext([m, 0, b]), mengentext([m // k, b]), mengentext([-(m // k), 0, -b])],
             f'{lin(k, -m)} = 0 für x = {zt(m // k)}; x({lin(1, -b)}) = 0 für x = 0 oder x = {zt(b)}. D = {mengentext([m // k, 0, b])}.',
             'Ein Produkt im Nenner ist 0, wenn ein Faktor 0 ist.')


def g_ein_bruch(R, st):
    h = 'Multipliziere mit dem Nenner und löse dann die lineare Gleichung.'
    while True:
        if st == 1:
            x = Fr(R.choice([j for j in range(-12, 13) if j])); c = Fr(R.choice([2, 3, 4, 5, -2, -3]))
            a = c * x; b = 0
            text = f'{zt(a)}/x = {zt(c)}'
            weg = f'D = ℚ \\ {{0}}. · x: {zt(a)} = {zt(c)}x → x = {zt(a)} : {kl(c)} = {zt(x)}.'
            cc = f'{cz(a)} / {cz(c)}'
        elif st == 2:
            b = R.choice([j for j in range(-9, 10) if j]); c = Fr(R.choice([2, 3, 4, 5, -2, -4])); x = Fr(R.randint(-10, 12))
            if x == -b or x + b == 0: continue
            a = c * (x + b)
            text = f'{zt(a)}/{N(1, b)} = {zt(c)}'
            weg = f'D = ℚ \\ {{{zt(-b)}}}. · {N(1, b)}: {zt(a)} = {zt(c)}({lin(1, b)}) = {lin(c, c * b)} → {lin(c, 0)} = {zt(a - c * b)} → x = {zt(x)}.'
            cc = f'({cz(a)} - ({cz(c * b)})) / {cz(c)}'
        else:
            a0, b = R.randint(-9, 9), R.choice([j for j in range(-9, 10) if j]); c = Fr(R.choice([2, 3, 4, 5, -1, -2, -3]))
            if c == 1: continue
            x = (c * b + a0) / (c - 1)
            if x == b or not ist_endlich(x) or abs(x) > 50 or a0 == 0: continue
            text = f'{N(1, a0)}/{N(1, -b)} = {zt(c)}'
            weg = (f'D = ℚ \\ {{{zt(b)}}}. · {N(1, -b)}: {lin(1, a0)} = {lin(c, -c * b)} → {lin(1 - c, 0) if 1 - c != 0 else "0"} = {zt(-c * b - a0)} → x = {zt(x)}.')
            cc = f'({cz(c * b)} + ({a0})) / ({cz(c)} - 1)'
        if st != 3 or x != b: break
    return Z(f'Löse {text}.', x, cc, weg, h)


def g_ueber_kreuz(R, st):
    h = 'Bestimme zuerst D. Dann über Kreuz multiplizieren und die lineare Gleichung lösen.'
    while True:
        if st == 1:
            a, c, d = R.randint(1, 9), R.randint(1, 9), R.choice([j for j in range(-9, 10) if j])
            if a == c: continue
            x = Fr(a * d, c - a)
            text = f'{a}/x = {c}/{N(1, d)}'
            ex = [0, -d]
            weg = f'Über Kreuz: {a}({lin(1, d)}) = {c}x → {lin(a, a * d)} = {c}x → {zt(a * d)} = {lin(c - a, 0)} → x = {zt(x)}.'
            cc = f'{a} * ({d}) / ({c} - {a})'
        elif st == 2:
            a, c = R.randint(1, 9), R.randint(1, 9); b, d = R.sample([j for j in range(-9, 10) if j], 2)
            if a == c: continue
            x = Fr(c * b - a * d, a - c)
            text = f'{a}/{N(1, b)} = {c}/{N(1, d)}'
            ex = [-b, -d]
            weg = f'Über Kreuz: {a}({lin(1, d)}) = {c}({lin(1, b)}) → {lin(a, a * d)} = {lin(c, c * b)} → {lin(a - c, 0)} = {zt(c * b - a * d)} → x = {zt(x)}.'
            cc = f'({c} * ({b}) - {a} * ({d})) / ({a} - {c})'
        else:
            a, b, c, d = [R.choice([j for j in range(-8, 9) if j]) for _ in range(4)]
            if a + d - c - b == 0 or len({b, d}) < 2: continue
            x = Fr(c * b - a * d, a + d - c - b)
            text = f'{N(1, a)}/{N(1, b)} = {N(1, c)}/{N(1, d)}'
            ex = [-b, -d]
            weg = (f'Über Kreuz: ({lin(1, a)})({lin(1, d)}) = ({lin(1, c)})({lin(1, b)}). Ausmultiplizieren: x² + {lin(a + d, a * d)} = x² + {lin(c + b, c * b)}. '
                   f'x² fällt weg: {lin(a + d - c - b, 0)} = {zt(c * b - a * d)} → x = {zt(x)}.')
            cc = f'({c} * ({b}) - ({a}) * ({d})) / (({a}) + ({d}) - ({c}) - ({b}))'
        if x not in ex and ist_endlich(x) and abs(x) <= 60 and len(zt(x)) <= 6: break
    return Z(f'Löse {text}.', x, cc, weg, h)


def g_hauptnenner(R, st):
    h = 'Bestimme den Hauptnenner und multipliziere jedes Glied damit.'
    while True:
        if st == 1:
            a, b, c = R.randint(1, 12), R.randint(1, 12), R.choice([1, 2, 3, 4, 5])
            x = Fr(a + b, c)
            text = f'{a}/x + {b}/x = {c}'
            weg = f'HN = x. · x: {a} + {b} = {c}x → x = {a + b} : {c} = {zt(x)}.'
            cc = f'({a} + {b}) / {c}'
        elif st == 2:
            a, b, k, c = R.randint(1, 9), R.randint(1, 9), R.choice([2, 3, 4, 5]), R.choice([1, 2, 3, 4, -1, -2])
            op = R.choice(['+', '−'])
            z = k * a + b if op == '+' else k * a - b
            x = Fr(z, c * k)
            text = f'{a}/x {op} {b}/({k}x) = {zt(c)}'
            weg = f'HN = {k}x. · {k}x: {k * a} {op} {b} = {lin(c * k, 0)} → {zt(z)} = {lin(c * k, 0)} → x = {zt(x)}.'
            cc = f'({k} * {a} {"+" if op == "+" else "-"} {b}) / ({c} * {k})'
        else:
            if R.random() < .5:
                a, b, c = R.randint(1, 9), R.randint(1, 9), R.choice([1, 2, 3, 4, 6])
                x = Fr(3 * a + 2 * b, 6 * c)
                text = f'{a}/(2x) + {b}/(3x) = {c}'
                weg = f'HN = 6x. · 6x: {3 * a} + {2 * b} = {6 * c}x → x = {3 * a + 2 * b} : {6 * c} = {zt(x)}.'
                cc = f'(3 * {a} + 2 * {b}) / (6 * {c})'
            else:
                a, b, c, d = R.randint(2, 12), R.randint(1, 9), R.choice([1, 2, 3, 4, -1, -2]), R.choice([j for j in range(-5, 6) if j])
                if a == b: continue
                x = Fr(a - b, c) - d
                text = f'{a}/{N(1, d)} = {b}/{N(1, d)} + {zt(c)}'
                weg = (f'HN = {lin(1, d)}. · {N(1, d)}: {a} = {b} + {zt(c)}({lin(1, d)}) → {a - b} = {lin(c, c * d)} → '
                       f'{lin(c, 0)} = {zt(a - b - c * d)} → x = {zt(x)}.')
                cc = f'({a} - {b}) / ({c}) - ({d})'
                if x == -d: continue
        if x != 0 and ist_endlich(x) and len(zt(x)) <= 6: break
    return Z(f'Löse {text}.', x, cc, weg, h)


def g_scheinloesung(R, st):
    a, b = R.choice([j for j in range(-8, 9) if j]), R.choice([j for j in range(-8, 9) if j])
    schein = R.random() < (.6 if st >= 2 else .5)
    c = a + b if schein else R.choice([j for j in range(-12, 13) if j not in (a + b, 0)])
    if c == 0: return g_scheinloesung(R, st)
    x = c - a
    if st == 3 and R.random() < .5:
        # Variante mit Faktor im Zähler
        k = R.choice([2, 3, 4])
        c = k * b if schein else R.choice([j for j in range(-12, 13) if j not in (k * b, 0)])
        x = Fr(c, k)
        if not schein and (not ist_endlich(x) or x == b): return g_scheinloesung(R, st)
        text = f'{k}x/{N(1, -b)} = {zt(c)}/{N(1, -b)}'
        weg0 = f'D = ℚ \\ {{{zt(b)}}}. · {N(1, -b)}: {k}x = {zt(c)} → x = {zt(x)}.'
    else:
        if not schein and x == b: return g_scheinloesung(R, st)
        text = f'{N(1, a)}/{N(1, -b)} = {zt(c)}/{N(1, -b)}'
        weg0 = f'D = ℚ \\ {{{zt(b)}}}. · {N(1, -b)}: {lin(1, a)} = {zt(c)} → x = {zt(x)}.'
    if x == b:
        richtig, falsch = 'L = { }', [f'L = {{{zt(b)}}}', f'L = {{{zt(-b)}}}', 'L = ℚ']
        weg = weg0 + f' {zt(b)} liegt nicht in D, also Scheinlösung: L = {{ }}.'
    else:
        richtig, falsch = f'L = {{{zt(x)}}}', ['L = { }', f'L = {{{zt(b)}}}', f'L = {{{zt(-x)}}}' if x else 'L = {1}']
        weg = weg0 + f' {zt(x)} liegt in D: L = {{{zt(x)}}}.'
    return A(R, f'Gib die Lösungsmenge von {text} an.', richtig, falsch, weg,
             'Bestimme zuerst D. Prüfe am Ende, ob deine Lösung in D liegt.')


def g_verhaeltnis(R, st):
    h = 'Produktgleichheit: Außenglieder mal = Innenglieder mal.'
    if st == 1:
        while True:
            a, b, c = R.randint(2, 15), R.randint(2, 20), R.randint(2, 10)
            x = Fr(a * b, c)
            if ist_endlich(x) and len(zt(x)) <= 5: break
        return Z(f'Löse die Verhältnisgleichung x : {a} = {b} : {c}.', x, f'{a} * {b} / {c}',
                 f'{c}x = {a} · {b} = {a * b} → x = {a * b} : {c} = {zt(x)}.', h)
    if st == 2:
        while True:
            a, b, c = R.randint(2, 15), R.randint(2, 12), R.randint(2, 20)
            x = Fr(a * c, b)
            if ist_endlich(x) and len(zt(x)) <= 5: break
        return Z(f'Löse die Verhältnisgleichung {a} : x = {b} : {c}.', x, f'{a} * {c} / {b}',
                 f'Außenglieder: {a} · {c} = {a * c}. Innenglieder: {b}x. Also x = {a * c} : {b} = {zt(x)}.', h)
    art = R.choice(['rezept', 'karte', 'mischung', 'gleichung'])
    if art == 'rezept':
        p1, m1 = R.choice([4, 6, 8]), R.choice([200, 250, 300, 400, 500, 600])
        p2 = R.choice([j for j in (2, 3, 5, 9, 10, 12) if j != p1])
        x = Fr(m1 * p2, p1)
        if not ist_endlich(x): return g_verhaeltnis(R, st)
        return Z(f'Für {p1} Personen braucht man {m1} g Mehl. Wie viel Mehl braucht man für {p2} Personen?', x, f'{m1} * {p2} / {p1}',
                 f'x : {p2} = {m1} : {p1} → {p1}x = {m1 * p2} → x = {zt(x)} g.', 'Stelle eine Verhältnisgleichung auf: Mehl : Personen.', einheit='g')
    if art == 'karte':
        M = R.choice([10000, 20000, 25000, 50000])
        cm = Fr(R.choice([2, 3, 4, 5, 6, 8, 12, 15]), R.choice([1, 2]))
        km = cm * M / 100000
        return Z(f'Eine Karte hat den Maßstab 1 : {zt(M)}. Zwei Orte sind auf der Karte {zt(cm)} cm voneinander entfernt. Wie weit sind sie in Wirklichkeit entfernt (in km)?', km,
                 f'{cz(cm)} * {M} / 100000', f'1 : {zt(M)} = {zt(cm)} : x → x = {zt(cm * M)} cm = {zt(km)} km.', 'Rechne erst in cm, dann in km um (1 km = 100 000 cm).', einheit='km')
    if art == 'mischung':
        a, b = R.choice([(1, 3), (1, 4), (2, 3), (1, 5), (2, 5), (3, 4)])
        gesamt = (a + b) * R.choice([50, 100, 150, 200, 250])
        x = Fr(gesamt * a, a + b)
        return Z(f'Saftschorle wird im Verhältnis Saft : Wasser = {a} : {b} gemischt. Wie viel Saft (in ml) braucht man für {gesamt} ml Schorle?', x,
                 f'{gesamt} * {a} / ({a} + {b})', f'Saft : Gesamt = {a} : {a + b}. x : {gesamt} = {a} : {a + b} → x = {zt(x)} ml.',
                 'Saft und Wasser zusammen sind die Gesamtmenge: Saft : Gesamt = a : (a + b).', einheit='ml')
    while True:
        a, b, c = R.randint(2, 9), R.randint(2, 9), R.choice([j for j in range(-8, 9) if j])
        x = Fr(a * c, b - a) if b != a else None
        if x is not None and ist_endlich(x) and len(zt(x)) <= 5: break
    return Z(f'Löse die Verhältnisgleichung x : {a} = {N(1, c)} : {b}.', x, f'{a} * ({c}) / ({b} - {a})',
             f'{b}x = {a}({lin(1, c)}) = {lin(a, a * c)} → {lin(b - a, 0)} = {zt(a * c)} → x = {zt(x)}.', h)


GEN = {'definitionsmenge': g_definitionsmenge, 'ein_bruch': g_ein_bruch, 'ueber_kreuz': g_ueber_kreuz, 'hauptnenner': g_hauptnenner,
       'scheinloesung': g_scheinloesung, 'verhaeltnis': g_verhaeltnis}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Bruchgleichungen lösen', ['definitionsmenge', 'ein_bruch', 'ueber_kreuz', 'hauptnenner']), ('Prüfen', ['scheinloesung']), ('Verhältnisse', ['verhaeltnis'])],
         'Bruchgleichungen lösen, dabei die Definitionsmenge beachten, und Verhältnisgleichungen mit der Produktgleichheit lösen.',
         ['Erst D bestimmen: Kein Nenner darf 0 werden.', 'Mit dem (Haupt-)Nenner multiplizieren, dann linear lösen.',
          'Lösung nicht in D → Scheinlösung, L = { }.', 'a : b = c : d ⇔ a · d = b · c.'],
         offen=['Lehrplan: Bruchgleichungen auch graphisch als Schnittpunkt zweier Graphen deuten. Dafür braucht die App Funktionsgraphen; nicht gebaut.'])
