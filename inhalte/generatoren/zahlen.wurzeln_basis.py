#!/usr/bin/env python3
"""Thema zahlen.wurzeln_basis – Elementare Wurzeln (Klasse 9). Schreibt inhalte/themen/zahlen.wurzeln_basis.json."""
import sys
from math import isqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(901)


def kw(r):
    """ganzzahlige dritte Wurzel"""
    n = round(r ** (1 / 3))
    assert n ** 3 == r
    return n


ETAPPEN = [
    {'lernziel': 'quadratwurzel', 'titel': 'Quadratwurzeln von Quadratzahlen',
     'regel': 'Die ⟦Quadratwurzel⟧ √a ist die Zahl ⟦ohne Minus⟧, die mit sich selbst multipliziert a ergibt. Die Zahl unter dem Wurzelzeichen heißt ⟦Radikand⟧.',
     'schritte': ['Gesucht ist √196: Welche Zahl mal sich selbst ergibt 196?', '14 · 14 = 196, also √196 = ⟦14⟧.'],
     'probe': '14² = 196 ✓',
     'fehler': '√196 = 98 ist falsch: Wurzelziehen ist nicht halbieren. 98 · 98 = 9 604, nicht 196. Richtig ist ⟦14⟧.'},
    {'lernziel': 'wurzel_dezimal', 'titel': 'Wurzeln aus Dezimalzahlen und Brüchen',
     'regel': 'Bei Dezimalzahlen: Die Wurzel hat ⟦halb so viele Nachkommastellen⟧ wie der Radikand. Bei Brüchen: ⟦Zähler und Nenner⟧ einzeln radizieren.',
     'schritte': ['√0,64: 0,64 hat 2 Nachkommastellen, √64 = 8, die Wurzel hat 1 Nachkommastelle.', '√0,64 = ⟦0,8⟧, denn 0,8 · 0,8 = 0,64.', '√(4/81) = √4 / √81 = ⟦2/9⟧.'],
     'probe': '0,8² = 0,64 ✓',
     'fehler': '√0,64 = 0,08 ist falsch: 0,08 · 0,08 = 0,0064. Die Wurzel hat ⟦halb so viele⟧ Nachkommastellen, also 0,8.'},
    {'lernziel': 'kubikwurzel', 'titel': 'Dritte Wurzeln (Kubikwurzeln)',
     'regel': 'Die ⟦dritte Wurzel⟧ ∛a (für a ≥ 0) ist die Zahl, die ⟦dreimal mit sich selbst⟧ multipliziert a ergibt. Sie macht das Hoch-3-Nehmen rückgängig.',
     'schritte': ['Gesucht ist ∛343: Welche Zahl hoch 3 ergibt 343?', '7 · 7 · 7 = 49 · 7 = 343, also ∛343 = ⟦7⟧.'],
     'probe': '7³ = 343 ✓',
     'fehler': '∛343 = 343 : 3 ≈ 114 ist falsch: Die dritte Wurzel ist ⟦nicht durch 3 teilen⟧. Richtig ist 7, denn 7³ = 343.'},
    {'lernziel': 'abschaetzen', 'titel': 'Zwischen welchen Zahlen liegt √a?',
     'regel': 'Ist a keine Quadratzahl, suchst du die ⟦Quadratzahlen direkt darunter und darüber⟧. Die Wurzel liegt zwischen deren Wurzeln.',
     'schritte': ['√90: Die Quadratzahlen um 90 sind 81 und 100.', '√81 = 9 und √100 = 10, also ⟦9 < √90 < 10⟧.'],
     'probe': '9² = 81 < 90 < 100 = 10² ✓',
     'fehler': '„√90 liegt zwischen 45 und 46“ ist falsch: Das ist die Hälfte von 90. Vergleiche mit ⟦Quadratzahlen⟧: 9² = 81, 10² = 100.'},
    {'lernziel': 'wurzel_deuten', 'titel': 'Wurzeln richtig deuten',
     'regel': '√a ist ⟦nie negativ⟧ und nur für ⟦a ≥ 0⟧ erklärt. Die Gleichung x² = a (a > 0) hat aber ⟦zwei Lösungen⟧: √a und −√a.',
     'schritte': ['x² = 25: Sowohl 5² als auch (−5)² ergeben 25.', 'Die Gleichung hat die Lösungen ⟦5 und −5⟧, aber √25 ist nur ⟦5⟧.'],
     'probe': '(−5)² = 25 ✓, 5² = 25 ✓',
     'fehler': '√(9 + 16) = √9 + √16 = 7 ist falsch: Erst den Radikanden berechnen. √(9 + 16) = √25 = ⟦5⟧.'},
    {'lernziel': 'wurzel_sache', 'titel': 'Seitenlänge aus Fläche und Volumen',
     'regel': 'Quadrat: Seitenlänge a = ⟦√A⟧. Würfel: Kantenlänge a = ⟦∛V⟧. Einheiten: aus cm² wird cm, aus cm³ wird cm.',
     'schritte': ['Ein Quadrat hat 169 cm² Flächeninhalt. a = √169 cm.', '13 · 13 = 169, also a = ⟦13 cm⟧.'],
     'probe': '13 cm · 13 cm = 169 cm² ✓',
     'fehler': 'Bei A = 169 cm² ist a = 169 : 4 cm falsch: Durch 4 teilt man den ⟦Umfang⟧, nicht die Fläche. Aus der Fläche zieht man die ⟦Wurzel⟧.'},
]


def g_quadratwurzel(s):
    if s == 1:
        n = R.randint(2, 15)
    elif s == 2:
        n = R.choice([R.randint(16, 25), 10 * R.randint(2, 9), 100 * R.randint(1, 3)])
    else:
        if R.random() < 0.5:
            a, b = R.randint(2, 20), R.randint(2, 20)
            k = R.randint(2, 5)
            text = f'Berechne {k} · √{dz(a * a)} − √{dz(b * b)}.'
            return zahl(text, f'√{dz(a * a)} = {a} und √{dz(b * b)} = {b}, also {k} · {a} − {b} = {dz(k * a - b)}.',
                        'Ziehe zuerst beide Wurzeln, dann Punkt vor Strich.', k * a - b, f'{k} * ({a * a} / {a}) - ({b * b} / {b})')
        n = R.randint(26, 40)
    r = n * n
    assert isqrt(r) == n
    return zahl(f'Berechne √{dz(r)}.', f'{n} · {n} = {dz(r)}, also √{dz(r)} = {n}.',
                'Welche Zahl ergibt mit sich selbst multipliziert den Radikanden?', n, f'{r} / {n}')


def g_wurzel_dezimal(s):
    if s == 1 or (s == 2 and R.random() < 0.5):
        n = R.randint(2, 9) if s == 1 else R.randint(11, 19)
        k = R.choice([1, 2]) if s == 1 else R.choice([1, 2, 3])
        w_ = Fr(n, 10 ** k)
        r = w_ * w_
        return zahl(f'Berechne √{dz(r)}.', f'{dz(w_)} · {dz(w_)} = {dz(r)}, also √{dz(r)} = {dz(w_)}.',
                    'Ziehe die Wurzel ohne Komma und halbiere die Anzahl der Nachkommastellen.', w_, f'{float(r)} / {float(w_)}')
    a, b = R.randint(1, 12), R.randint(2, 15)
    if Fr(a, b).denominator != b: return None
    if s == 3 and R.random() < 0.5:
        k = R.randint(2, 4)
        text = f'Berechne {k} · √({a * a}/{b * b}). Gib das Ergebnis als gekürzten Bruch an.'
        e = Fr(k * a, b)
        return luecken(text, '□/□', 'Zähler / Nenner (gekürzt)', [e.numerator, e.denominator],
                       f'√({a * a}/{b * b}) = {a}/{b}, mal {k} ergibt {br(e)}.',
                       'Erst Zähler und Nenner einzeln radizieren, dann multiplizieren und kürzen.',
                       c=[f'{e.numerator}', f'{e.denominator}'])
    return luecken(f'Berechne √({a * a}/{b * b}).', '□/□', 'Zähler / Nenner', [a, b],
                   f'√{a * a} = {a} und √{b * b} = {b}, also √({a * a}/{b * b}) = {a}/{b}.',
                   'Ziehe die Wurzel aus Zähler und Nenner einzeln.', c=[f'{a * a} // {a}', f'{b * b} // {b}'])


def g_kubikwurzel(s):
    if s == 1:
        n = R.randint(1, 6)
        r = n ** 3
        return zahl(f'Berechne ∛{dz(r)}.', f'{n} · {n} · {n} = {dz(r)}, also ∛{dz(r)} = {n}.',
                    'Welche Zahl ergibt dreimal mit sich selbst multipliziert den Radikanden?', kw(r), f'{r} / ({n} * {n})')
    if s == 2:
        typ = R.random()
        if typ < 0.5:
            n = R.choice([7, 8, 9, 10, 11, 12, 20, 30, 40, 50])
            r = n ** 3
            return zahl(f'Berechne ∛{dz(r)}.', f'{n}³ = {dz(r)}, also ∛{dz(r)} = {n}.',
                        'Probiere Zahlen hoch 3. Endziffer des Radikanden hilft.', kw(r), f'{r} / ({n} * {n})')
        n, k = R.randint(1, 9), R.choice([1, 2])
        w_ = Fr(n, 10 ** k)
        r = w_ ** 3
        return zahl(f'Berechne ∛{dz(r)}.', f'{dz(w_)}³ = {dz(r)}, also ∛{dz(r)} = {dz(w_)}.',
                    'Die dritte Wurzel hat ein Drittel so viele Nachkommastellen wie der Radikand.', w_, f'{float(r)} / ({float(w_)} * {float(w_)})')
    if R.random() < 0.5:
        a, b = R.randint(1, 6), R.randint(2, 10)
        if Fr(a, b).denominator != b: return None
        return luecken(f'Berechne ∛({a ** 3}/{b ** 3}).', '□/□', 'Zähler / Nenner', [a, b],
                       f'∛{a ** 3} = {a} und ∛{b ** 3} = {b}, also {a}/{b}.',
                       'Ziehe die dritte Wurzel aus Zähler und Nenner einzeln.', c=[f'{a ** 3} // ({a} * {a})', f'{b ** 3} // ({b} * {b})'])
    a, b = R.randint(2, 6), R.randint(2, 10)
    return zahl(f'Berechne ∛{dz(a ** 3)} · √{dz(b * b)}.', f'∛{dz(a ** 3)} = {a}, √{dz(b * b)} = {b}, also {a} · {b} = {a * b}.',
                'Ziehe jede Wurzel einzeln, dann multiplizieren.', a * b, f'({a ** 3} / ({a} * {a})) * ({b * b} / {b})')


def g_abschaetzen(s):
    if s == 3 and R.random() < 0.5:
        n = R.randint(2, 9)
        r = R.randint(n ** 3 + 1, (n + 1) ** 3 - 1)
        return luecken(f'Zwischen welchen aufeinanderfolgenden natürlichen Zahlen liegt ∛{dz(r)}?', '□ < ∛' + dz(r) + ' < □',
                       'kleinere Zahl, größere Zahl', [n, n + 1],
                       f'{n}³ = {n ** 3} < {dz(r)} < {(n + 1) ** 3} = {n + 1}³, also {n} < ∛{dz(r)} < {n + 1}.',
                       'Suche die Kubikzahlen direkt unter und über dem Radikanden.', c=[f'{n}', f'{n} + 1'])
    g = {1: (2, 9), 2: (10, 20), 3: (21, 40)}[s]
    n = R.randint(*g)
    r = R.randint(n * n + 1, (n + 1) ** 2 - 1)
    if isqrt(r) != n: return None
    return luecken(f'Zwischen welchen aufeinanderfolgenden natürlichen Zahlen liegt √{dz(r)}?', '□ < √' + dz(r) + ' < □',
                   'kleinere Zahl, größere Zahl', [n, n + 1],
                   f'{n}² = {dz(n * n)} < {dz(r)} < {dz((n + 1) ** 2)} = {n + 1}², also {n} < √{dz(r)} < {n + 1}.',
                   'Suche die Quadratzahlen direkt unter und über dem Radikanden.', c=[f'{n}', f'{n} + 1'])


def g_wurzel_deuten(s):
    typ = R.choice({1: 'abdf', 2: 'abcdef', 3: 'ce'}[s])
    n = R.randint(3, 20)
    q = n * n
    if typ == 'a':
        return auswahl(f'Welche Aussage über √{dz(q)} stimmt?', f'√{dz(q)} = {n}',
                       [f'√{dz(q)} = ±{n}', f'√{dz(q)} = {dz(q // 2) if q % 2 == 0 else dz(Fr(q, 2))}', f'√{dz(q)} = −{n}'],
                       f'Die Wurzel ist immer die nicht-negative Zahl: {n} · {n} = {dz(q)}, also √{dz(q)} = {n}.',
                       'Kann eine Quadratwurzel negativ sein?')
    if typ == 'b':
        return auswahl(f'Welche Lösungen hat die Gleichung x² = {dz(q)}?', f'x = {n} und x = −{n}',
                       [f'nur x = {n}', f'nur x = −{n}', 'keine Lösung'],
                       f'{n}² = {dz(q)} und ({"−"}{n})² = {dz(q)}. Beide Zahlen lösen die Gleichung.',
                       'Prüfe auch die negative Zahl: Was ergibt (−x)²?')
    if typ == 'c':
        a, b = R.randint(2, 12), R.randint(2, 12)
        s_ = a * a + b * b
        rs = isqrt(s_)
        ist = rs * rs == s_
        richtig = f'Falsch: √{dz(s_)} {"= " + str(rs) if ist else "ist keine ganze Zahl"}, nicht {a + b}'
        return auswahl(f'Jemand rechnet: √({a * a} + {b * b}) = √{a * a} + √{b * b} = {a + b}. Was stimmt?', richtig,
                       ['Richtig, man darf die Wurzel aus jedem Summanden einzeln ziehen', f'Falsch: Das Ergebnis ist {a * b}',
                        f'Richtig, denn {a} + {b} = {a + b}'],
                       f'Erst den Radikanden berechnen: {a * a} + {b * b} = {dz(s_)}. Probe: {a + b}² = {dz((a + b) ** 2)} ≠ {dz(s_)}.',
                       'Rechne zuerst aus, was unter der Wurzel steht, und mache die Probe durch Quadrieren.')
    if typ == 'd':
        return auswahl(f'Was gilt für √(−{dz(q)})?', 'Sie ist nicht definiert (keine reelle Zahl).',
                       [f'√(−{dz(q)}) = −{n}', f'√(−{dz(q)}) = {n}', f'√(−{dz(q)}) = 0'],
                       f'Jede Zahl mal sich selbst ist nie negativ ({n} · {n} = {dz(q)}, (−{n}) · (−{n}) = {dz(q)}). Für −{dz(q)} gibt es keine Quadratwurzel.',
                       'Kann eine Zahl mal sich selbst eine negative Zahl ergeben?')
    if typ == 'e':
        m = R.randint(3, 14)
        r = m * m
        if r % 2 or r // 4 == m: return None
        return auswahl(f'Jemand sagt: „√{dz(r)} = {dz(r // 2)}, denn Wurzelziehen heißt halbieren.“ Was stimmt?',
                       f'Falsch: {dz(r // 2)}² = {dz((r // 2) ** 2)}. Richtig ist √{dz(r)} = {m}.',
                       ['Richtig, Wurzelziehen ist halbieren', f'Falsch: Richtig ist √{dz(r)} = {dz(r // 4) if r % 4 == 0 else r * 2}',
                        f'Falsch: Richtig ist √{dz(r)} = −{m}'],
                       f'Probe durch Quadrieren: {dz(r // 2)} · {dz(r // 2)} = {dz((r // 2) ** 2)} ≠ {dz(r)}. Aber {m} · {m} = {dz(r)}.',
                       'Mache die Probe: Quadriere das behauptete Ergebnis.')
    r = R.choice([x for x in range(2, 99) if isqrt(x) ** 2 != x])
    return auswahl(f'Welchen Wert hat (√{r})²?', dz(r), [f'√{r}', dz(2 * r), dz(r * r)],
                   f'(√{r})² = √{r} · √{r} = {r}, denn √{r} ist genau die Zahl, deren Quadrat {r} ist.',
                   'Was bedeutet √a? Welche Zahl entsteht beim Quadrieren?')


def g_wurzel_sache(s):
    typ = R.random()
    if s == 1:
        n = R.randint(4, 20)
        return zahl(f'Ein quadratisches Beet hat einen Flächeninhalt von {dz(n * n)} m². Wie lang ist eine Seite?',
                    f'a = √{dz(n * n)} m = {n} m, denn {n} · {n} = {dz(n * n)}.', 'Beim Quadrat gilt A = a · a.', n,
                    f'{n * n} / {n}', einheit='m')
    if s == 2:
        if typ < 0.5:
            n = R.randint(2, 12)
            ding = R.choice(['Ein Würfel aus Holz', 'Ein würfelförmiger Behälter', 'Ein Spielwürfel aus Kunststoff', 'Ein Würfel aus Ton'])
            return zahl(f'{ding} hat ein Volumen von {dz(n ** 3)} cm³. Wie lang ist eine Kante?',
                        f'a = ∛{dz(n ** 3)} cm = {n} cm, denn {n}³ = {dz(n ** 3)}.', 'Beim Würfel gilt V = a · a · a.', n,
                        f'{n ** 3} / ({n} * {n})', einheit='cm')
        n = R.randint(5, 30)
        return zahl(f'Ein quadratischer Platz hat {dz(n * n)} m² Fläche. Wie lang ist sein Umfang?',
                    f'Seite a = √{dz(n * n)} m = {n} m. Umfang u = 4 · {n} m = {4 * n} m.',
                    'Bestimme zuerst die Seitenlänge, dann den Umfang.', 4 * n, f'4 * ({n * n} / {n})', einheit='m')
    if typ < 0.4:
        n = R.randint(2, 15)
        o = 6 * n * n
        return zahl(f'Ein Würfel hat eine Oberfläche von {dz(o)} cm². Wie lang ist eine Kante?',
                    f'Eine Seitenfläche: {dz(o)} : 6 = {dz(n * n)} cm². a = √{dz(n * n)} cm = {n} cm.',
                    'Ein Würfel hat 6 gleiche quadratische Seitenflächen.', n, f'({o} / 6) / {n}', einheit='cm')
    if typ < 0.7:
        n = R.randint(2, 10)
        return zahl(f'Ein Würfel hat ein Volumen von {dz(n ** 3)} dm³. Wie groß ist seine Oberfläche?',
                    f'a = ∛{dz(n ** 3)} dm = {n} dm. O = 6 · {n}² dm² = {dz(6 * n * n)} dm².',
                    'Bestimme zuerst die Kantenlänge aus dem Volumen.', 6 * n * n, f'6 * ({n ** 3} / ({n} * {n})) ** 2', einheit='dm²')
    n = R.randint(3, 12)
    k = R.randint(2, 6)
    return zahl(f'{k} gleich große quadratische Fliesen bedecken zusammen {dz(k * n * n)} dm². Wie lang ist eine Fliesenseite?',
                f'Eine Fliese: {dz(k * n * n)} : {k} = {dz(n * n)} dm². Seite = √{dz(n * n)} dm = {n} dm.',
                'Berechne zuerst die Fläche einer einzelnen Fliese.', n, f'({k * n * n} / {k}) / {n}', einheit='dm')


GEN = {'quadratwurzel': g_quadratwurzel, 'wurzel_dezimal': g_wurzel_dezimal, 'kubikwurzel': g_kubikwurzel,
       'abschaetzen': g_abschaetzen, 'wurzel_deuten': g_wurzel_deuten, 'wurzel_sache': g_wurzel_sache}

if __name__ == '__main__':
    bauen('zahlen.wurzeln_basis',
          'Quadratwurzeln und dritte Wurzeln als Umkehrung des Quadrierens bzw. Hoch-3-Nehmens bestimmen, abschätzen und anwenden.',
          ['√a ist die nicht-negative Zahl, deren Quadrat a ist (a ≥ 0).', '∛a ist die Zahl, deren dritte Potenz a ist.',
           'x² = a (a > 0) hat zwei Lösungen: √a und −√a.', 'Keine Quadratzahl? Zwischen die benachbarten Quadratzahlen einordnen.'],
          [('Quadratwurzeln', ['quadratwurzel', 'wurzel_dezimal']), ('Dritte Wurzeln und Abschätzen', ['kubikwurzel', 'abschaetzen']),
           ('Verstehen und Anwenden', ['wurzel_deuten', 'wurzel_sache'])],
          ETAPPEN, GEN,
          meiden={'quadratwurzel': ['√196.'], 'wurzel_dezimal': ['√0,64.', '√(4/81)'], 'kubikwurzel': ['∛343.'],
                  'abschaetzen': ['√90?'], 'wurzel_deuten': ['x² = 25?'], 'wurzel_sache': [' 169 m²']},
          offen=['Rechenausdruck c bei Wurzeln: Das Prüfskript kann keine Wurzeln rechnen. c prüft deshalb die Umkehrung (z. B. 196 / 14 = 14 bzw. 343 / (7 · 7) = 7).'])
