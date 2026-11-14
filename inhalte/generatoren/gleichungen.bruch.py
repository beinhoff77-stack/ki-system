#!/usr/bin/env python3
"""Thema gleichungen.bruch – Bruch- und Verhältnisgleichungen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, Z, baue, bruch, cz, ist_endlich, kl, lin, mit_bild, zt  # noqa: E402

META = {'thema_schluessel': 'gleichungen.bruch', 'thema_id': 5, 'block_id': 60, 'klasse': {'gym_by': 8, 'rs_by': 8}}

ETAPPEN = [
    {'lernziel': 'definitionsmenge', 'titel': 'Definitionsmenge einer Bruchgleichung',
     'regel': 'Bei einer ⟦Bruchgleichung⟧ steht x im Nenner. Bevor du rechnest, schließt du alle Zahlen aus, die einen ⟦Nenner 0⟧ machen.',
     'schritte': ['2/(x − 1) = 3/(x + 4)', 'x − 1 = 0 für x = 1; x + 4 = 0 für x = −4.', '⟦D = ℚ \\ {−4; 1}⟧'],
     'fehler': 'Bei 2/(x − 1) = 3/(x + 4) reicht es nicht, nur x = 1 auszuschließen. ⟦Jeder⟧ Nenner zählt, auch der auf der rechten Seite.',
     '_verbot': ['2/(x − 1) = 3/(x + 4)']},
    {'lernziel': 'ein_bruch', 'titel': 'Bruchgleichungen mit einem Bruch',
     'regel': 'Multipliziere beide Seiten mit dem ⟦Nenner⟧. Dann ist der Bruch weg und du löst eine lineare Gleichung. Zum Schluss prüfst du, ob die Lösung in ⟦D⟧ liegt.',
     'schritte': ['12/(x − 2) = 3. Zuerst D = ℚ \\ {2}.', 'Beide Seiten · (x − 2): 12 = 3 · (x − 2) = 3x − 6.', '18 = 3x, also ⟦x = 6⟧. 6 liegt in D.',
                  'Schneller mit der Umkehrfrage: 12 geteilt durch was ergibt 3? Durch 4. Also x − 2 = 4 und x = 6.'],
     'probe': '12/(6 − 2) = 12/4 = 3 ✓',
     'fehler': 'Aus 12/(x − 2) = 3 wird nicht 12 = 3x − 2. Der Nenner wird als ⟦Ganzes⟧ multipliziert: 3 · (x − 2) = 3x − 6.',
     '_verbot': ['12/(x − 2) = 3']},
    {'lernziel': 'ueber_kreuz', 'titel': 'Zwei Brüche: über Kreuz multiplizieren',
     'regel': 'Steht auf jeder Seite ⟦genau ein⟧ Bruch, multiplizierst du ⟦über Kreuz⟧: aus a/b = c/d wird a · d = c · b. Warum? Du nimmst beide Seiten mit b und mit d mal – dann kürzt sich links das b und rechts das d weg.',
     'schritte': ['4/(x + 1) = 2/(x − 3)   D = ℚ \\ {−1; 3}', 'Über Kreuz: 4(x − 3) = 2(x + 1)', '4x − 12 = 2x + 2 → 2x = 14 → ⟦x = 7⟧'],
     'probe': '4/8 = 0,5 und 2/4 = 0,5 ✓',
     'fehler': 'Über Kreuz heißt Zähler links mal Nenner ⟦rechts⟧. 4 · (x + 1) = 2 · (x − 3) ist falsch – da wurde jeder Zähler mit dem eigenen Nenner malgenommen. Und Vorsicht: Bei 4/(x + 1) + 1 = 2/(x − 3) steht links eine Summe, dann geht über Kreuz ⟦nicht⟧ – nimm den Hauptnenner.',
     '_verbot': ['4/(x + 1) = 2/(x − 3)']},
    {'lernziel': 'hauptnenner', 'titel': 'Mit dem Hauptnenner multiplizieren',
     'regel': 'Stehen mehrere Brüche in der Gleichung, multiplizierst du ⟦jedes Glied⟧ mit dem ⟦Hauptnenner⟧. Danach kommt kein Bruch mehr vor.',
     'schritte': ['5/x + 1/(2x) = 2   HN = 2x', '| · 2x: 10 + 1 = 4x', '11 = 4x → ⟦x = 2,75⟧'],
     'fehler': 'Ein Glied vergessen: Wer bei 5/x + 1/(2x) = 2 nur die Brüche mit 2x malnimmt, bekommt 10 + 1 = 2 – das x ist verschwunden und die Gleichung ist Unsinn. Auch die ⟦2 auf der rechten Seite⟧ wird mit 2x multipliziert: 11 = 4x.',
     '_verbot': ['5/x + 1/(2x) = 2']},
    {'lernziel': 'scheinloesung', 'titel': 'Lösung prüfen: Gehört sie zu D?',
     'regel': 'Eine errechnete Zahl ist nur dann Lösung, wenn sie in ⟦D⟧ liegt. Sonst ist sie eine ⟦Scheinlösung⟧ und die Lösungsmenge ist leer: L = { }.',
     'schritte': ['(x + 1)/(x − 3) = 4/(x − 3)   D = ℚ \\ {3}', '| · (x − 3): x + 1 = 4 → x = 3', '3 liegt nicht in D: ⟦L = { }⟧'],
     'fehler': 'L = {3} ist hier falsch: Für x = 3 wird der Nenner 0, die Gleichung hat dort ⟦keinen Sinn⟧. Deshalb immer zuerst D bestimmen.',
     '_verbot': ['(x + 1)/(x − 3) = 4/(x − 3)']},
    {'lernziel': 'verhaeltnis', 'titel': 'Verhältnisgleichungen',
     'regel': 'Eine ⟦Verhältnisgleichung⟧ hat die Form a : b = c : d. Es gilt die ⟦Produktgleichheit⟧: a · d = b · c (Außenglieder mal Außenglieder = Innenglieder mal Innenglieder).',
     'schritte': ['Pfannkuchen: Auf 4 Eier kommen 10 Esslöffel Mehl. Wie viel Mehl für 6 Eier? Das Verhältnis Mehl : Eier bleibt gleich: x : 6 = 10 : 4.',
                  'Produktgleichheit: 4 · x = 6 · 10 = 60.', '⟦x = 15⟧ Esslöffel Mehl.'],
     'probe': 'Mit dem Faktor: Auf 1 Ei kommen 10 : 4 = 2,5 EL, also 6 · 2,5 = 15 ✓',
     'fehler': 'x = 6 · 4 : 10 = 2,4 ist falsch – mit mehr Eiern braucht man nicht weniger Mehl! Die ⟦Außenglieder⟧ x und 4 werden miteinander multipliziert, ebenso die Innenglieder 6 und 10: 4x = 60.',
     '_verbot': ['x : 6 = 10 : 4']},
    {'lernziel': 'graphisch', 'titel': 'Bruchgleichung am Graphen lösen',
     'regel': 'Jede Seite einer Gleichung ist ein Funktionsterm. Zeichne ⟦beide Graphen⟧. Wo sie sich ⟦schneiden⟧, sind beide Seiten gleich: Die x-Werte der Schnittpunkte sind die Lösungen.',
     'schritte': ['Gleichung 6/x = x − 1. Links die Hyperbel y = 6/x, rechts die Gerade y = x − 1.', 'Die Graphen schneiden sich in (3 | 2) und in (−2 | −3).',
                  'Die Lösungen sind ⟦x = 3⟧ und ⟦x = −2⟧.'],
     'probe': '6/3 = 2 und 3 − 1 = 2 ✓. 6/(−2) = −3 und −2 − 1 = −3 ✓',
     'fehler': 'Die y-Werte als Lösung angeben: L = {2; −3} ist falsch. Gesucht sind die ⟦x-Werte⟧ der Schnittpunkte, denn x ist die Unbekannte der Gleichung.',
     'bild': {'typ': 'koordinaten', 'x': [-6, 6], 'y': [-6, 6],
              'graphen': [{'art': 'hyperbel', 'a': 6, 'b': 0, 'c': 0, 'name': 'y = 6/x'}, {'art': 'linear', 'm': 1, 't': -1, 'name': 'y = x − 1'}],
              'punkte': [{'x': 3, 'y': 2, 'name': '(3 | 2)'}, {'x': -2, 'y': -3, 'name': '(−2 | −3)'}]},
     '_verbot': ['6/x = x − 1']},
]


def quad1(p, q):
    """x² + p·x + q mit richtigen Vorzeichen."""
    t = lin(p, q) if p else zt(q)
    if t == '0': return 'x²'
    return 'x² ' + ('− ' + t[1:] if t.startswith('−') else '+ ' + t)


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
        vorlage = R.choice(['bruch_zahl', 'zahl_bruch'] if st == 1 else ['bruch_zahl', 'zahl_bruch', 'faktor'])
        if st == 1:
            x = Fr(R.choice([j for j in range(-12, 13) if j])); c = Fr(R.choice([2, 3, 4, 5, -2, -3]))
            a = c * x; b = 0
            text = f'{zt(a)}/x = {zt(c)}' if vorlage == 'bruch_zahl' else f'{zt(c)} = {zt(a)}/x'
            weg = f'D = ℚ \\ {{0}}. · x: {zt(a)} = {zt(c)}x → x = {zt(a)} : {kl(c)} = {zt(x)}. Umkehrfrage: {zt(a)} geteilt durch {zt(x)} ergibt {zt(c)}.'
            cc = f'{cz(a)} / {cz(c)}'
        elif st == 2 and vorlage == 'faktor':
            k = R.choice([2, 3, 4, 5]); c = Fr(R.choice([2, 3, 4, 6, -2, -3])); x = Fr(R.choice([j for j in range(-9, 10) if j]))
            a = c * k * x
            text = f'{zt(a)}/({k}x) = {zt(c)}'
            weg = f'D = ℚ \\ {{0}}. · {k}x: {zt(a)} = {zt(c * k)}x → x = {zt(a)} : {kl(c * k)} = {zt(x)}.'
            cc = f'{cz(a)} / ({cz(c)} * {k})'
        elif st == 2:
            b = R.choice([j for j in range(-9, 10) if j]); c = Fr(R.choice([2, 3, 4, 5, -2, -4])); x = Fr(R.randint(-10, 12))
            if x == -b or x + b == 0: continue
            a = c * (x + b)
            text = f'{zt(a)}/{N(1, b)} = {zt(c)}' if vorlage == 'bruch_zahl' else f'{zt(c)} = {zt(a)}/{N(1, b)}'
            weg = (f'D = ℚ \\ {{{zt(-b)}}}. · {N(1, b)}: {zt(a)} = {zt(c)}({lin(1, b)}) = {lin(c, c * b)} → {lin(c, 0)} = {zt(a - c * b)} → x = {zt(x)}. '
                   f'Umkehrfrage: {zt(a)} geteilt durch {zt(x + b)} ergibt {zt(c)}, also {lin(1, b)} = {zt(x + b)}.')
            cc = f'({cz(a)} - ({cz(c * b)})) / {cz(c)}'
        elif R.random() < .4:
            # x im Zähler mit Faktor: (k·x + a0)/(x − b) = c
            k = R.choice([2, 3, 4]); a0, b = R.randint(-9, 9), R.choice([j for j in range(-9, 10) if j]); c = Fr(R.choice([1, 5, 6, -1, -2]))
            if c == k or a0 == 0: continue
            x = (c * b + a0) / (c - k)
            if x == b or not ist_endlich(x) or abs(x) > 50 or len(zt(x)) > 6: continue
            text = f'({lin(k, a0)})/{N(1, -b)} = {zt(c)}'
            weg = f'D = ℚ \\ {{{zt(b)}}}. · {N(1, -b)}: {lin(k, a0)} = {lin(c, -c * b)} → {lin(k - c, 0)} = {zt(-c * b - a0)} → x = {zt(x)}. {zt(x)} liegt in D.'
            cc = f'({cz(c * b)} + ({a0})) / ({cz(c)} - {k})'
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
            weg = f'Über Kreuz: {a}({lin(1, d)}) = {lin(c, 0)} → {lin(a, a * d)} = {lin(c, 0)} → {zt(a * d)} = {lin(c - a, 0)} → x = {zt(x)}.'
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
            weg = (f'Über Kreuz: ({lin(1, a)})({lin(1, d)}) = ({lin(1, c)})({lin(1, b)}). Ausmultiplizieren: {quad1(a + d, a * d)} = {quad1(c + b, c * b)}. '
                   f'x² fällt weg: {lin(a + d - c - b, 0)} = {zt(c * b - a * d)} → x = {zt(x)}.')
            cc = f'({c} * ({b}) - ({a}) * ({d})) / (({a}) + ({d}) - ({c}) - ({b}))'
        if x not in ex and ist_endlich(x) and abs(x) <= 60 and len(zt(x)) <= 6: break
    weg = f'D = {mengentext(ex)}. ' + weg.replace(' → x → x =', ' → x =')
    weg = re_doppelt(weg) + f' {zt(x)} liegt in D.'
    return Z(f'Löse {text}.', x, cc, weg, h)


def re_doppelt(w):
    """„… → x = 47 → x = 47.“ und „x = 47 → x = 47“ vermeiden."""
    import re
    return re.sub(r'(x = [^ →]+) → \1\.', r'\1.', w)


def g_hauptnenner(R, st):
    h = 'Bestimme den Hauptnenner und multipliziere jedes Glied damit.'
    while True:
        if st == 1:
            a, b, c = R.randint(1, 12), R.randint(1, 12), R.choice([1, 2, 3, 4, 5])
            x = Fr(a + b, c)
            text = f'{a}/x + {b}/x = {c}'
            weg = f'HN = x. · x: {a} + {b} = {lin(c, 0)} → ' + (f'x = {a + b} : {c} = {zt(x)}.' if c != 1 else f'x = {a + b}.')
            cc = f'({a} + {b}) / {c}'
        elif st == 2:
            a, b, k, c = R.randint(1, 9), R.randint(1, 9), R.choice([2, 3, 4, 5]), R.choice([1, 2, 3, 4, -1, -2])
            op = R.choice(['+', '−'])
            z = k * a + b if op == '+' else k * a - b
            x = Fr(z, c * k)
            text = f'{a}/x {op} {b}/({k}x) = {zt(c)}'
            weg = f'HN = {k}x. · {k}x: {k * a} {op} {b} = {lin(c * k, 0)} → {zt(z)} = {lin(c * k, 0)} → x = {zt(x)}.'
            cc = f'({k} * {a} {"+" if op == "+" else "-"} {b}) / ({c} * {k})'
        elif R.random() < .35:
            t1, t2 = R.choice([(12, 6), (6, 3), (10, 15), (12, 4), (20, 30), (6, 12), (8, 24), (15, 10), (9, 18), (12, 12)])
            x = Fr(t1 * t2, t1 + t2)
            if not ist_endlich(x) or len(zt(x)) > 5: continue
            kontext = R.choice([('Ein Wasserhahn füllt eine Wanne allein in {a} Minuten, ein zweiter in {b} Minuten. Wie viele Minuten dauert es mit beiden zusammen?', 'min'),
                                ('Zwei Kinder streichen einen Zaun. Das erste bräuchte allein {a} Stunden, das zweite {b} Stunden. Wie lange brauchen sie zusammen (in Stunden)?', 'h'),
                                ('Zwei Pumpen leeren einen Teich. Die erste allein schafft es in {a} Stunden, die zweite in {b} Stunden. Wie lange dauert es mit beiden (in Stunden)?', 'h')])
            text_s = kontext[0].format(a=t1, b=t2) + f' Löse 1/{t1} + 1/{t2} = 1/x.'
            return Z(text_s, x, f'{t1} * {t2} / ({t1} + {t2})',
                     f'HN = {t1 * t2 // __import__("math").gcd(t1, t2)}x. In einer Zeiteinheit schafft der erste 1/{t1}, der zweite 1/{t2} der Arbeit. '
                     f'1/{t1} + 1/{t2} = {bruch(Fr(1, t1) + Fr(1, t2))} = 1/x → x = {zt(x)} {kontext[1]}.',
                     'Jeder schafft pro Minute bzw. Stunde einen Bruchteil der Arbeit. Zusammen schaffen sie die Summe davon.', einheit=kontext[1])
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
                sg = '+' if c > 0 else '−'
                text = f'{a}/{N(1, d)} = {b}/{N(1, d)} {sg} {zt(abs(c))}'
                weg = (f'HN = {lin(1, d)}. · {N(1, d)}: {a} = {b} {sg} {"" if abs(c) == 1 else zt(abs(c))}({lin(1, d)}) → {a - b} = {lin(c, c * d)} → '
                       + (f'{lin(c, 0)} = {zt(a - b - c * d)} → ' if c != 1 else '') + f'x = {zt(x)}.')
                cc = f'({a} - {b}) / ({c}) - ({d})'
                if x == -d: continue
        if x != 0 and ist_endlich(x) and len(zt(x)) <= 6: break
    return Z(f'Löse {text}.', x, cc, weg, h)


def g_scheinloesung(R, st):
    if st >= 2 and R.random() < .25:
        b = R.choice([j for j in range(-8, 9) if j]); a = R.choice([j for j in range(-8, 9) if j and j != -b])
        c = a + b
        if c == 0: return g_scheinloesung(R, st)
        text = f'{N(1, a)}/{N(1, -b)} = {zt(c)}/{N(1, -b)}'
        return A(R, f'Warum ist x = {zt(b)} keine Lösung von {text}, obwohl die Rechnung x = {zt(b)} ergibt?',
                 f'Für x = {zt(b)} ist der Nenner 0, die Gleichung ist dort nicht definiert.',
                 ['Weil man falsch gerechnet hat.', f'Weil {zt(b)} {"positiv" if b > 0 else "negativ"} ist.', f'Weil {zt(b)} nicht im Zähler vorkommt.'],
                 f'D = ℚ \\ {{{zt(b)}}}: Für x = {zt(b)} wird {lin(1, -b)} = 0. Die Rechnung ist richtig, aber {zt(b)} ist eine Scheinlösung. L = {{ }}.',
                 'Setze die Zahl in den Nenner ein.')
    a, b = R.choice([j for j in range(-8, 9) if j]), R.choice([j for j in range(-8, 9) if j])
    if a == -b: return g_scheinloesung(R, st)
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
            if ist_endlich(x) and len(zt(x)) <= 5 and a != c and b != c: break
        return Z(f'Löse die Verhältnisgleichung x : {a} = {b} : {c}.', x, f'{a} * {b} / {c}',
                 f'{c}x = {a} · {b} = {a * b} → x = {a * b} : {c} = {zt(x)}.', h)
    if st == 2 and R.random() < .4:
        art = R.choice(['saft', 'beton', 'farbe'])
        if art == 'saft':
            a, b = R.choice([(1, 4), (1, 3), (1, 5), (2, 3)]); m = R.choice([100, 150, 200, 250, 300])
            x = Fr(m * b, a)
            return Z(f'Saft und Wasser werden im Verhältnis {a} : {b} gemischt. Wie viel Wasser (in ml) brauchst du für {m} ml Saft?', x, f'{m} * {b} / {a}',
                     f'Saft : Wasser = {a} : {b} = {m} : x → {a}x = {m * b} → x = {zt(x)} ml.', 'Stelle die Verhältnisgleichung Saft : Wasser auf.', einheit='ml')
        if art == 'beton':
            a, b = R.choice([(1, 5), (1, 4), (1, 3)]); k = R.choice([15, 20, 30, 40, 60])
            x = Fr(k * a, b)
            if not ist_endlich(x): return g_verhaeltnis(R, st)
            return Z(f'Für Beton mischt man Zement und Kies im Verhältnis {a} : {b}. Wie viel kg Zement braucht man für {k} kg Kies?', x, f'{k} * {a} / {b}',
                     f'Zement : Kies = {a} : {b} = x : {k} → {b}x = {k * a} → x = {zt(x)} kg.', 'Zement steht vorne, Kies hinten – in beiden Verhältnissen gleich.', einheit='kg')
        a, b = R.choice([(2, 3), (3, 5), (1, 2), (3, 4)]); w = R.choice([6, 9, 12, 15, 20])
        x = Fr(w * a, b)
        if not ist_endlich(x): return g_verhaeltnis(R, st)
        return Z(f'Für ein Grün mischt man gelbe und blaue Farbe im Verhältnis {a} : {b}. Wie viele Liter gelbe Farbe braucht man für {w} Liter blaue?', x, f'{w} * {a} / {b}',
                 f'Gelb : Blau = {a} : {b} = x : {w} → {b}x = {w * a} → x = {zt(x)} l.', 'Stelle die Verhältnisgleichung Gelb : Blau auf.', einheit='l')
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


def hyp_name(a, p, c=0):
    n = f'{zt(a)}/{"x" if p == 0 else "(" + lin(1, -p) + ")"}'
    return f'y = {n}' + (f' {"+" if c > 0 else "−"} {zt(abs(c))}' if c else '')


def g_graphisch(R, st):
    h = 'Suche den Schnittpunkt der Graphen. Die Lösung ist sein x-Wert.'
    if st == 1:
        # a/(x − p) = c mit waagrechter Gerade
        while True:
            p, c = R.randint(-3, 3), R.choice([-3, -2, -1, 1, 2, 3, 4])
            d = R.choice([j for j in range(-4, 5) if j])          # x0 − p
            a = c * d; x0 = p + d
            if abs(x0) <= 6 and a != 0: break
        gr = {'typ': 'koordinaten', 'x': [-7, 7], 'y': [-6, 6],
              'graphen': [{'art': 'hyperbel', 'a': a, 'b': -p, 'c': 0, 'name': hyp_name(a, p)}, {'art': 'linear', 'm': 0, 't': c, 'name': f'y = {zt(c)}'}]}
        G = f'{zt(a)}/{"x" if p == 0 else "(" + lin(1, -p) + ")"} = {zt(c)}'
        return mit_bild(A(R, f'Lies die Lösung von {G} am Schnittpunkt ab.', f'x = {zt(x0)}',
                          [f'x = {zt(c)}' if c != x0 else f'x = {zt(-x0)}', f'x = {zt(p)}' if p != x0 else f'x = {zt(x0 + 1)}', f'x = {zt(a)}' if a != x0 else f'x = {zt(-a)}'],
                          f'Die Hyperbel trifft die Gerade y = {zt(c)} bei x = {zt(x0)}. Probe: {zt(a)} : {kl(x0 - p)} = {zt(c)} ✓', h), gr)
    if st == 2:
        # a/x = x + t mit zwei Schnittpunkten
        while True:
            r1, r2 = R.sample([j for j in range(-5, 6) if j], 2)
            a, t = -r1 * r2, -(r1 + r2)
            if a != 0 and abs(a) <= 12 and all(abs(r + t) <= 6 for r in (r1, r2)): break
        r1, r2 = sorted((r1, r2))
        gr = {'typ': 'koordinaten', 'x': [-6, 6], 'y': [-7, 7],
              'graphen': [{'art': 'hyperbel', 'a': a, 'b': 0, 'c': 0, 'name': hyp_name(a, 0)}, {'art': 'linear', 'm': 1, 't': t, 'name': f'y = {lin(1, t)}'}]}
        G = f'{zt(a)}/x = {lin(1, t)}'
        y1, y2 = r1 + t, r2 + t
        if R.random() < .35:
            gr['punkte'] = [{'x': r1, 'y': y1}, {'x': r2, 'y': y2}]
            return mit_bild(Z(f'Die Graphen zu {G} schneiden sich zweimal. Gib die größere Lösung an.', r2, f'{r2}',
                              f'Schnittpunkte ({zt(r1)} | {zt(y1)}) und ({zt(r2)} | {zt(y2)}). Lösungen x = {zt(r1)} und x = {zt(r2)}; die größere ist {zt(r2)}. '
                              f'Probe: {zt(a)} : {kl(r2)} = {zt(Fr(a, r2))} und {zt(r2)} {"+" if t >= 0 else "−"} {zt(abs(t))} = {zt(y2)} ✓', h), gr)
        richtig = f'L = {{{zt(r1)}; {zt(r2)}}}'
        falsch = [f'L = {{{"; ".join(zt(v) for v in sorted({y1, y2}))}}}' if {y1, y2} != {r1, r2} else f'L = {{{zt(-r2)}; {zt(-r1)}}}',
                  f'L = {{{zt(r2)}}}', f'L = {{{zt(-r2)}; {zt(-r1)}}}' if {-r1, -r2} != {r1, r2} else f'L = {{{zt(r1)}}}']
        return mit_bild(A(R, f'Löse {G} mit den Graphen.', richtig, falsch,
                          f'Schnittpunkte ({zt(r1)} | {zt(y1)}) und ({zt(r2)} | {zt(y2)}). Die x-Werte sind die Lösungen: {richtig}.', h), gr)
    # Stufe 3: Anzahl der Lösungen / keine Lösung an der Asymptote
    art = R.choice(['asymptote', 'eine', 'zwei'])
    a = R.choice([2, 3, 4, 6, -2, -4])
    c = R.choice([-2, -1, 1, 2])
    gr = {'typ': 'koordinaten', 'x': [-6, 6], 'y': [-6, 6], 'graphen': [{'art': 'hyperbel', 'a': a, 'b': 0, 'c': c, 'name': hyp_name(a, 0, c)}]}
    G0 = f'{zt(a)}/x {"+" if c > 0 else "−"} {zt(abs(c))}'
    if art == 'asymptote':
        gr['graphen'].append({'art': 'linear', 'm': 0, 't': c, 'name': f'y = {zt(c)}'})
        n, w = 0, f'Die Hyperbel kommt der Geraden y = {zt(c)} beliebig nahe, trifft sie aber nie: {zt(a)}/x wäre 0, das geht nicht. L = {{ }}.'
        G = f'{G0} = {zt(c)}'
    elif art == 'eine':
        k = R.choice([j for j in range(-4, 5) if j and j != c])
        if (k - c) == 0 or Fr(a, k - c).denominator != 1: return g_graphisch(R, st)
        gr['graphen'].append({'art': 'linear', 'm': 0, 't': k, 'name': f'y = {zt(k)}'})
        n, w = 1, f'Die waagrechte Gerade y = {zt(k)} schneidet die Hyperbel genau einmal, bei x = {zt(Fr(a, k - c))}.'
        G = f'{G0} = {zt(k)}'
    else:
        # Gerade y = −x·sign(a) … : a/x + c = m·x + c, zwei Schnittpunkte, wenn a/m > 0
        m = 1 if a > 0 else -1
        gr['graphen'].append({'art': 'linear', 'm': m, 't': c, 'name': f'y = {lin(m, c)}'})
        n, w = 2, f'Die Gerade y = {lin(m, c)} schneidet beide Äste der Hyperbel: zwei Schnittpunkte, also zwei Lösungen.'
        G = f'{G0} = {lin(m, c)}'
    return mit_bild(A(R, f'Wie viele Lösungen hat die Gleichung {G}? Entscheide am Bild.', f'{n} Lösung{"en" if n != 1 else ""}',
                      [f'{k} Lösung{"en" if k != 1 else ""}' for k in (0, 1, 2) if k != n] + ['unendlich viele Lösungen'], w,
                      'Zähle die Schnittpunkte der beiden Graphen.'), gr)


GEN = {'definitionsmenge': g_definitionsmenge, 'ein_bruch': g_ein_bruch, 'ueber_kreuz': g_ueber_kreuz, 'hauptnenner': g_hauptnenner,
       'scheinloesung': g_scheinloesung, 'verhaeltnis': g_verhaeltnis, 'graphisch': g_graphisch}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Bruchgleichungen lösen', ['definitionsmenge', 'ein_bruch', 'ueber_kreuz', 'hauptnenner']), ('Prüfen', ['scheinloesung']), ('Verhältnisse und Graphen', ['verhaeltnis', 'graphisch'])],
         'Bruchgleichungen lösen, dabei die Definitionsmenge beachten, und Verhältnisgleichungen mit der Produktgleichheit lösen.',
         ['Erst D bestimmen: Kein Nenner darf 0 werden.', 'Mit dem (Haupt-)Nenner multiplizieren, dann linear lösen.',
          'Lösung nicht in D → Scheinlösung, L = { }.', 'a : b = c : d ⇔ a · d = b · c.'],
         offen=['Prüfvorschlag „grafisch deuten“ für ein_bruch ist in der neuen Karte „graphisch“ umgesetzt (dort passt er zum Lernziel).'])
