#!/usr/bin/env python3
"""Thema gleichungen.lgs2 – Lineare Gleichungssysteme mit 2 Unbekannten (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, Z, baue, cz, eur, kl, lin, zt  # noqa: E402

META = {'thema_schluessel': 'gleichungen.lgs2', 'thema_id': 6, 'block_id': 59, 'klasse': {'gym_by': 8, 'rs_by': 9}}

ETAPPEN = [
    {'lernziel': 'pruefen', 'titel': 'Ist das Zahlenpaar eine Lösung?',
     'regel': 'Ein Zahlenpaar (x | y) ist ⟦Lösung⟧ des Gleichungssystems, wenn es ⟦beide⟧ Gleichungen erfüllt. Prüfe durch Einsetzen in I und in II.',
     'schritte': ['I: x + y = 5   II: 2x − y = 1   Paar (2 | 3)', 'I: 2 + 3 = 5 ✓   II: 4 − 3 = 1 ✓', '⟦(2 | 3) ist Lösung.⟧'],
     'fehler': 'Erfüllt (4 | 1) nur x + y = 5, ist es ⟦keine⟧ Lösung des Systems: In II gilt 8 − 1 = 7 ≠ 1. Beide Gleichungen müssen stimmen.',
     '_verbot': ['x + y = 5']},
    {'lernziel': 'einsetzen', 'titel': 'Einsetzungsverfahren',
     'regel': 'Ist eine Gleichung nach einer Variablen aufgelöst (z. B. y = …), ⟦setzt du diesen Term⟧ in die andere Gleichung ein. Dann bleibt eine Gleichung mit nur einer Variablen.',
     'schritte': ['I: y = 2x − 1   II: 3x + y = 9', 'I in II: 3x + (2x − 1) = 9 → 5x = 10 → x = 2', 'x in I: y = 2 · 2 − 1 = 3. ⟦L = {(2 | 3)}⟧'],
     'fehler': 'Beim Einsetzen die ⟦Klammer⟧ nicht vergessen: 3x − (2x − 1) ist 3x − 2x + 1, nicht 3x − 2x − 1.',
     '_verbot': ['y = 2x − 1']},
    {'lernziel': 'gleichsetzen', 'titel': 'Gleichsetzungsverfahren',
     'regel': 'Sind ⟦beide⟧ Gleichungen nach derselben Variablen aufgelöst, setzt du die rechten Seiten ⟦gleich⟧.',
     'schritte': ['I: y = 3x − 4   II: y = x + 2', '3x − 4 = x + 2 → 2x = 6 → x = 3', 'y = 3 + 2 = 5. ⟦L = {(3 | 5)}⟧'],
     'fehler': 'Mit x = 3 ist die Aufgabe nicht fertig: Die Lösung ist ein ⟦Zahlenpaar⟧. Setze x noch ein, um y zu bestimmen.',
     '_verbot': ['y = 3x − 4']},
    {'lernziel': 'addition', 'titel': 'Additionsverfahren',
     'regel': 'Multipliziere die Gleichungen so, dass vor einer Variablen ⟦Gegenzahlen⟧ stehen. Addierst du dann die Gleichungen, ⟦fällt diese Variable weg⟧.',
     'schritte': ['I: 2x + 3y = 12   II: x − y = 1', 'II · 3: 3x − 3y = 3', 'I + II: 5x = 15 → x = 3; aus II: y = 2. ⟦L = {(3 | 2)}⟧'],
     'fehler': 'Wer II mit 3 multipliziert, muss ⟦jedes⟧ Glied multiplizieren – auch die rechte Seite: 3x − 3y = 3, nicht 3x − 3y = 1.',
     '_verbot': ['2x + 3y = 12']},
    {'lernziel': 'loesbarkeit', 'titel': 'Wie viele Lösungen hat das System?',
     'regel': 'Fällt beim Rechnen ⟦x und y⟧ weg, entscheidet die Rest-Aussage: Eine ⟦falsche⟧ Aussage (z. B. 0 = 5) heißt keine Lösung, eine ⟦wahre⟧ (0 = 0) heißt unendlich viele Lösungen.',
     'schritte': ['I: y = 2x + 1   II: y = 2x − 3', 'Gleichsetzen: 2x + 1 = 2x − 3 → 1 = −3', 'Falsche Aussage: ⟦keine Lösung⟧ (parallele Geraden).'],
     'fehler': 'Bei 0 = 0 ist nicht „x = 0“ die Lösung. Die Aussage ist ⟦immer⟧ wahr: Jedes Paar, das eine Gleichung erfüllt, erfüllt auch die andere – unendlich viele Lösungen.',
     '_verbot': ['y = 2x + 1']},
    {'lernziel': 'verfahren', 'titel': 'Welches Verfahren ist geschickt?',
     'regel': 'Alle Verfahren führen zum Ziel. ⟦Gleichsetzen⟧, wenn beide Gleichungen nach derselben Variablen aufgelöst sind. ⟦Einsetzen⟧, wenn eine aufgelöst ist. ⟦Addition⟧, wenn vor einer Variablen Gegenzahlen oder Vielfache stehen.',
     'schritte': ['I: 4x + 5y = 3   II: 2x − 5y = 9', 'Vor y stehen 5 und −5: Gegenzahlen.', 'Am geschicktesten: ⟦Additionsverfahren⟧.'],
     'fehler': 'Bei I: y = 3x und II: y = x + 4 musst du nichts umstellen. Hier erst nach x aufzulösen kostet ⟦unnötige⟧ Schritte – gleichsetzen ist schneller.',
     '_verbot': ['4x + 5y = 3']},
    {'lernziel': 'sachaufgabe', 'titel': 'Sachaufgaben mit zwei Unbekannten',
     'regel': 'Lege für die beiden gesuchten Größen ⟦Variablen⟧ fest (x, y). Übersetze jede Information in ⟦eine Gleichung⟧, löse das System und antworte im Satz.',
     'schritte': ['In einem Stall sind Hühner (x) und Kaninchen (y): 10 Köpfe, 28 Beine.', 'I: x + y = 10   II: 2x + 4y = 28', 'II − 2 · I: 2y = 8 → y = 4, x = 6. ⟦6 Hühner, 4 Kaninchen⟧'],
     'fehler': 'Die Beine-Gleichung ist nicht x + y = 28: Ein Huhn hat ⟦2⟧, ein Kaninchen ⟦4⟧ Beine. Jede Information braucht die passenden Faktoren.',
     '_verbot': ['10 Köpfe, 28 Beine']},
]


def g2(a, b):
    """a·x + b·y als Text."""
    s = lin(a, 0) if a else ''
    if b:
        t = lin(b, 0, 'y')
        s = t if not s else s + (' − ' if b < 0 else ' + ') + (t.lstrip('−'))
    return s or '0'


def gl(a, b, c):
    return f'{g2(a, b)} = {zt(c)}'


def sys_text(e1, e2):
    return f'I: {e1}   II: {e2}'


def nz(R, lo=-6, hi=6):
    return R.choice([k for k in range(lo, hi + 1) if k])


def frage(R, x, y, text, weg, h, ccx, ccy):
    if R.random() < .5:
        return Z(f'{text} Gib x an.', x, ccx, weg, h)
    return Z(f'{text} Gib y an.', y, ccy, weg, h)


def g_pruefen(R, st):
    while True:
        x, y = R.randint(-6, 8), R.randint(-6, 8)
        a1, b1, a2, b2 = nz(R), nz(R), nz(R), nz(R)
        if a1 * b2 - a2 * b1: break
    c1, c2 = a1 * x + b1 * y, a2 * x + b2 * y
    T = sys_text(gl(a1, b1, c1), gl(a2, b2, c2))
    def erf(p, q): return (a1 * p + b1 * q == c1, a2 * p + b2 * q == c2)
    if st == 3:
        kand = [(x, y), (y, x), (x + 1, y), (x, y - 1)]
        p, q = R.choice(kand)
        e = erf(p, q)
        if p == x and q == y: richtig = 'Ja, beide Gleichungen sind erfüllt.'
        elif e == (True, False): richtig = 'Nein, nur Gleichung I ist erfüllt.'
        elif e == (False, True): richtig = 'Nein, nur Gleichung II ist erfüllt.'
        else: richtig = 'Nein, keine der beiden Gleichungen ist erfüllt.'
        alle = ['Ja, beide Gleichungen sind erfüllt.', 'Nein, nur Gleichung I ist erfüllt.', 'Nein, nur Gleichung II ist erfüllt.', 'Nein, keine der beiden Gleichungen ist erfüllt.']
        return A(R, f'Gegeben: {T}. Ist ({zt(p)} | {zt(q)}) eine Lösung?', richtig, [s for s in alle if s != richtig],
                 f'I: {zt(a1 * p + b1 * q)} {"=" if e[0] else "≠"} {zt(c1)}. II: {zt(a2 * p + b2 * q)} {"=" if e[1] else "≠"} {zt(c2)}.',
                 'Setze x und y in jede Gleichung einzeln ein.')
    # falsche Paare: erfüllen nur eine Gleichung oder sind vertauscht
    falsch = []
    for p in range(x - 6, x + 7):
        if b1 and (c1 - a1 * p) % b1 == 0:
            q = (c1 - a1 * p) // b1
            if (p, q) != (x, y): falsch.append((p, q))
    R.shuffle(falsch)
    falsch = falsch[:2] + [(y, x)] if (y, x) != (x, y) else falsch[:3]
    falsch = [f for f in falsch if erf(*f) != (True, True)]
    return A(R, f'Gegeben: {T}. Welches Zahlenpaar ist die Lösung?', f'({zt(x)} | {zt(y)})', [f'({zt(p)} | {zt(q)})' for p, q in falsch] + [f'({zt(x + 1)} | {zt(y)})'],
             f'({zt(x)} | {zt(y)}) erfüllt I: {zt(c1)} = {zt(c1)} und II: {zt(c2)} = {zt(c2)}. Andere Paare erfüllen höchstens eine Gleichung.',
             'Ein Paar, das nur eine Gleichung erfüllt, ist keine Lösung.')


def g_einsetzen(R, st):
    h = 'Setze den Term für y (oder x) in die andere Gleichung ein. Klammern setzen!'
    while True:
        x, y = R.randint(-6, 8), R.randint(-6, 8)
        if st == 1:
            m, t = nz(R, -4, 5), 0
            a, b = R.randint(1, 5), R.choice([1, 2, -1])
        else:
            m, t = nz(R, -4, 5), nz(R, -9, 9)
            a, b = nz(R, -5, 6), nz(R, -4, 4)
        y = m * x + t
        if a + b * m != 0 and abs(y) <= 40: break
    c = a * x + b * y
    if st == 3 and R.random() < .5:
        # nach x aufgelöst
        x2, y2 = y, x
        T = sys_text(f'x = {lin(m, t, "y")}', gl(b, a, c))
        weg = (f'I in II: {zt(b)} · ({lin(m, t, "y")}) {"+" if a > 0 else "−"} {lin(abs(a), 0, "y")} = {zt(c)} → {lin(b * m + a, b * t, "y")} = {zt(c)} → y = {zt(y2)}. '
               f'In I: x = {zt(x2)}.')
        return frage(R, x2, y2, f'Löse mit dem Einsetzungsverfahren: {T}.', weg, h, f'({m}) * ({y2}) + ({t})', f'({c} - ({b}) * ({t})) / (({b}) * ({m}) + ({a}))')
    T = sys_text(f'y = {lin(m, t)}', gl(a, b, c))
    weg = (f'I in II: {g2(a, 0)} {"+" if b > 0 else "−"} {"" if abs(b) == 1 else str(abs(b)) + " · "}({lin(m, t)}) = {zt(c)} → '
           f'{lin(a + b * m, b * t)} = {zt(c)} → x = {zt(x)}. In I: y = {zt(y)}.')
    return frage(R, x, y, f'Löse mit dem Einsetzungsverfahren: {T}.', weg, h, f'({c} - ({b}) * ({t})) / (({a}) + ({b}) * ({m}))', f'({m}) * ({x}) + ({t})')


def g_gleichsetzen(R, st):
    h = 'Setze die beiden rechten Seiten gleich und löse nach x.'
    while True:
        x = R.randint(-6, 8)
        m1, m2 = nz(R, -5, 5), nz(R, -5, 5)
        t1 = nz(R, -9, 9)
        if m1 == m2: continue
        y = m1 * x + t1
        t2 = y - m2 * x
        if abs(y) <= 40 and abs(t2) <= 30: break
    if st == 1:
        m2, t2 = 0 if R.random() < .3 else m2, t2
        if m2 == 0: t2 = y
    if st == 3:
        # zweite Gleichung erst umstellen: k·y = k·m2·x + k·t2  (k ≠ 1)  oder  y − m2x = t2
        k = R.choice([2, 3, -2])
        T = sys_text(f'y = {lin(m1, t1)}', gl(-k * m2, k, k * t2))
        weg = (f'II nach y auflösen: y = {lin(m2, t2)}. Gleichsetzen: {lin(m1, t1)} = {lin(m2, t2)} → {lin(m1 - m2, 0)} = {zt(t2 - t1)} → x = {zt(x)}. y = {zt(y)}.')
    else:
        T = sys_text(f'y = {lin(m1, t1)}', f'y = {lin(m2, t2)}')
        weg = f'{lin(m1, t1)} = {lin(m2, t2)} → {lin(m1 - m2, 0)} = {zt(t2 - t1)} → x = {zt(x)}. In I: y = {zt(y)}.'
    return frage(R, x, y, f'Löse mit dem Gleichsetzungsverfahren: {T}.', weg, h if st < 3 else 'Löse zuerst Gleichung II nach y auf.',
                 f'({t2} - ({t1})) / (({m1}) - ({m2}))', f'({m1}) * ({x}) + ({t1})')


def g_addition(R, st):
    h = 'Sorge dafür, dass vor x oder y Gegenzahlen stehen. Dann addiere die Gleichungen.'
    while True:
        x, y = R.randint(-6, 8), R.randint(-6, 8)
        if st == 1:
            a1, a2, b1 = nz(R), nz(R), R.randint(1, 6)
            b2 = -b1
            k1, k2 = 1, 1
        elif st == 2:
            a1, b1 = nz(R), nz(R)
            k = R.choice([2, 3, -2, -3])
            a2, b2 = nz(R), -b1 // 1
            b2 = Fr(-b1, k)
            if b2.denominator != 1: continue
            b2 = int(b2); k1, k2 = 1, k
        else:
            a1, b1, a2, b2 = nz(R), nz(R), nz(R), nz(R)
            k1, k2 = abs(b2), abs(b1)
            if b1 * b2 > 0: k2 = -k2
        if a1 * b2 - a2 * b1 and (k1 * b1 + k2 * b2 == 0): break
    c1, c2 = a1 * x + b1 * y, a2 * x + b2 * y
    T = sys_text(gl(a1, b1, c1), gl(a2, b2, c2))
    A_ = k1 * a1 + k2 * a2; C_ = k1 * c1 + k2 * c2
    teil = []
    if k1 != 1: teil.append(f'I · {kl(k1)}: {gl(k1 * a1, k1 * b1, k1 * c1)}')
    if k2 != 1: teil.append(f'II · {kl(k2)}: {gl(k2 * a2, k2 * b2, k2 * c2)}')
    weg = ('. '.join(teil) + '. ' if teil else '') + f'Addieren: {lin(A_, 0)} = {zt(C_)} → x = {zt(x)}. Einsetzen: y = {zt(y)}.'
    return frage(R, x, y, f'Löse mit dem Additionsverfahren: {T}.', weg, h,
                 f'({k1} * ({c1}) + ({k2}) * ({c2})) / ({k1} * ({a1}) + ({k2}) * ({a2}))', f'({c1} - ({a1}) * ({x})) / ({b1})')


ANTW = ['genau eine Lösung', 'keine Lösung', 'unendlich viele Lösungen']


def g_loesbarkeit(R, st):
    if st == 3 and R.random() < .6:
        # Parameter so bestimmen, dass keine Lösung
        a1, b1 = nz(R, -5, 5), nz(R, -5, 5); k = R.choice([2, 3, -2, -1])
        c1 = R.randint(-9, 9); c2 = k * c1 + R.choice([1, 2, 3, -1, -4])
        T = sys_text(gl(a1, b1, c1), f'{g2(k * a1, 0)} + a · y = {zt(c2)}')
        return Z(f'{T}. Für welchen Wert von a hat das Gleichungssystem keine Lösung?', k * b1, f'{k} * ({b1})',
                 f'Keine Lösung, wenn II die linke Seite von I mal {kl(k)} ist, die rechte Seite aber nicht: a = {kl(k)} · {kl(b1)} = {zt(k * b1)}. '
                 f'Dann steht rechts {zt(c2)} statt {zt(k * c1)}.', 'Vergleiche die Faktoren vor x. Mit welcher Zahl wurde I multipliziert?')
    art = R.choice(ANTW)
    if st == 1:
        m = nz(R, -4, 4); t1 = R.randint(-9, 9)
        if art == ANTW[0]:
            m2 = R.choice([k for k in range(-4, 5) if k != m]); t2 = R.randint(-9, 9)
        elif art == ANTW[1]:
            m2, t2 = m, t1 + R.choice([1, 2, 3, -2, -5])
        else:
            m2, t2 = m, t1
        e2 = f'y = {lin(m2, t2)}' if art != ANTW[2] else f'{g2(-2 * m, 2)} = {zt(2 * t1)}'
        T = sys_text(f'y = {lin(m, t1)}', e2)
        grund = {ANTW[0]: 'Verschiedene Steigungen: Die Geraden schneiden sich in einem Punkt.', ANTW[1]: f'Gleichsetzen ergibt {zt(t1)} = {zt(t2)}: falsch. Parallele Geraden.',
                 ANTW[2]: 'II durch 2 geteilt und nach y aufgelöst ergibt genau I. Beide Gleichungen beschreiben dieselbe Gerade.'}[art]
    else:
        a1, b1 = nz(R), nz(R); c1 = R.randint(-12, 12); k = R.choice([2, 3, -2, -1, -3])
        if art == ANTW[0]:
            a2, b2 = k * a1 + R.choice([1, -1, 2]), k * b1; c2 = R.randint(-12, 12)
        elif art == ANTW[1]:
            a2, b2, c2 = k * a1, k * b1, k * c1 + R.choice([1, 2, -3, 5])
        else:
            a2, b2, c2 = k * a1, k * b1, k * c1
        T = sys_text(gl(a1, b1, c1), gl(a2, b2, c2))
        grund = {ANTW[0]: f'Die linke Seite von II ist kein Vielfaches der linken Seite von I: Es gibt genau ein Lösungspaar.',
                 ANTW[1]: f'I · {kl(k)} ergibt links dasselbe wie II, rechts aber {zt(k * c1)} statt {zt(c2)}: Widerspruch.',
                 ANTW[2]: f'II ist genau I · {kl(k)}: Beide Gleichungen haben dieselben Lösungen.'}[art]
    return A(R, f'Wie viele Lösungen hat {T}?', art, [a for a in ANTW if a != art], grund,
             'Vergleiche die beiden Gleichungen: Ist eine ein Vielfaches der anderen – links, rechts, oder beides?')


VERF = ['Einsetzungsverfahren', 'Gleichsetzungsverfahren', 'Additionsverfahren']


def g_verfahren(R, st):
    art = R.choice(VERF)
    x, y = R.randint(-5, 7), R.randint(-5, 7)
    if art == 'Gleichsetzungsverfahren':
        m1, m2 = R.sample([k for k in range(-5, 6) if k], 2)
        var = R.choice(['x', 'y'])
        if var == 'y':
            T = sys_text(f'y = {lin(m1, y - m1 * x)}', f'y = {lin(m2, y - m2 * x)}')
        else:
            T = sys_text(f'x = {lin(m1, x - m1 * y, "y")}', f'x = {lin(m2, x - m2 * y, "y")}')
        grund = f'Beide Gleichungen sind nach {var} aufgelöst: rechte Seiten gleichsetzen.'
    elif art == 'Einsetzungsverfahren':
        m = nz(R, -4, 4)
        while True:
            a, b = nz(R, -5, 5), nz(R, -5, 5)
            if abs(b) != abs(a * m) and a != 0: break
        T = sys_text(f'y = {lin(m, y - m * x)}', gl(a, b, a * x + b * y)) if R.random() < .5 else sys_text(gl(a, b, a * x + b * y), f'y = {lin(m, y - m * x)}')
        grund = 'Eine Gleichung ist schon nach y aufgelöst, die andere nicht: einsetzen.'
    else:
        a1, a2, b1 = nz(R), nz(R), R.randint(2, 7)
        if abs(a1) == 1 or abs(a2) == 1: a1, a2 = a1 * 2, a2 * 3
        T = sys_text(gl(a1, b1, a1 * x + b1 * y), gl(a2, -b1, a2 * x - b1 * y))
        grund = f'Vor y stehen {b1} und −{b1}: Addieren lässt y sofort wegfallen.'
    return A(R, f'Welches Verfahren ist für {T} am geschicktesten?', art, [v for v in VERF if v != art], grund,
             'Schau, ob eine Gleichung schon nach x oder y aufgelöst ist, und ob Gegenzahlen vorkommen.')


def g_sachaufgabe(R, st):
    art = R.choice({1: ['zahlen', 'tiere', 'muenzen'], 2: ['eintritt', 'tiere', 'muenzen', 'zahlen'], 3: ['eintritt', 'tarif', 'mischung']}[st])
    if art == 'zahlen':
        a, b = sorted(R.sample(range(3, 60), 2), reverse=True)
        return Z(f'Die Summe zweier Zahlen ist {a + b}, ihre Differenz ist {a - b}. Wie heißt die größere Zahl?', a, f'({a + b} + {a - b}) / 2',
                 f'I: x + y = {a + b}, II: x − y = {a - b}. I + II: 2x = {2 * a} → x = {a}, y = {b}.', 'Stelle zwei Gleichungen auf und addiere sie.')
    if art == 'tiere':
        x, y = R.randint(3, 25), R.randint(2, 20)
        k = x + y; bn = 2 * x + 4 * y
        if R.random() < .5:
            return Z(f'Auf einem Hof leben Hühner und Kaninchen, zusammen {k} Tiere mit {bn} Beinen. Wie viele Kaninchen sind es?', y, f'({bn} - 2 * {k}) / 2',
                     f'I: x + y = {k}, II: 2x + 4y = {bn}. II − 2 · I: 2y = {bn - 2 * k} → y = {y}.', 'Hühner haben 2, Kaninchen 4 Beine.')
        return Z(f'Auf einem Hof leben Hühner und Kaninchen, zusammen {k} Tiere mit {bn} Beinen. Wie viele Hühner sind es?', x, f'{k} - ({bn} - 2 * {k}) / 2',
                 f'I: x + y = {k}, II: 2x + 4y = {bn}. II − 2 · I: 2y = {bn - 2 * k} → y = {y}, x = {k} − {y} = {x}.', 'Hühner haben 2, Kaninchen 4 Beine.')
    if art == 'muenzen':
        w1, w2 = R.choice([(2, 1), (Fr(1, 2), Fr(1, 5)), (2, Fr(1, 2)), (1, Fr(1, 2))])
        x, y = R.randint(3, 20), R.randint(3, 20)
        n, W = x + y, w1 * x + w2 * y
        n1, n2 = {Fr(2): '2-€', Fr(1): '1-€', Fr(1, 2): '50-Cent', Fr(1, 5): '20-Cent'}[Fr(w1)], {Fr(2): '2-€', Fr(1): '1-€', Fr(1, 2): '50-Cent', Fr(1, 5): '20-Cent'}[Fr(w2)]
        return Z(f'In einer Spardose sind {n} Münzen, nur {n1}- und {n2}-Stücke, zusammen {eur(W)} €. Wie viele {n1}-Stücke sind es?', x,
                 f'({cz(W)} - {cz(w2)} * {n}) / ({cz(w1)} - {cz(w2)})',
                 f'I: x + y = {n}, II: {g2(w1, w2)} = {zt(W)}. y = {n} − x einsetzen: {lin(Fr(w1) - Fr(w2), 0)} = {zt(W - Fr(w2) * n)}' + ('' if Fr(w1) - Fr(w2) == 1 else f' → x = {x}') + '.',
                 'x = Anzahl der wertvolleren Münzen. Eine Gleichung für die Anzahl, eine für den Wert.')
    if art == 'eintritt':
        p1, p2 = R.choice([(12, 7), (9, 5), (15, 8), (Fr(21, 2), 6), (8, Fr(9, 2)), (14, 9)])
        x, y = R.randint(2, 30), R.randint(2, 40)
        n, G = x + y, p1 * x + p2 * y
        return Z(f'Eine Eintrittskarte kostet für Erwachsene {eur(p1)} €, für Kinder {eur(p2)} €. Eine Gruppe aus {n} Personen zahlt {eur(G)} €. Wie viele Kinder sind dabei?', y,
                 f'({cz(p1)} * {n} - {cz(G)}) / ({cz(p1)} - {cz(p2)})',
                 f'I: x + y = {n}, II: {eur(p1)}x + {eur(p2)}y = {eur(G)}. x = {n} − y einsetzen: {eur(Fr(p1) * n)} − {eur(Fr(p1) - Fr(p2))}y = {eur(G)} → y = {y}.',
                 'x = Erwachsene, y = Kinder. Eine Gleichung für die Personen, eine für den Preis.')
    if art == 'tarif':
        g1, p1 = R.choice([20, 30, 35, 40, 50]), R.choice([30, 35, 40, 45])
        p2 = p1 + R.choice([5, 10, 15])
        t = Fr(R.randint(1, 8) * 2 + R.choice([0, 1]), 2)
        gB = g1 + (p1 - p2) * t
        if gB < 0 or gB.denominator != 1: return g_sachaufgabe(R, st)
        return Z(f'Handwerker A berechnet {g1} € Anfahrt und {p1} € pro Stunde, Handwerker B {zt(gB)} € Anfahrt und {p2} € pro Stunde. Nach wie vielen Stunden kosten beide gleich viel?', t,
                 f'({g1} - {cz(gB)}) / ({p2} - {p1})', f'I: y = {lin(p1, g1)}, II: y = {lin(p2, gB)}. Gleichsetzen: {lin(p1 - p2, 0)} = {zt(gB - g1)} → x = {zt(t)} h.',
                 'Stelle für jeden Handwerker eine Gleichung y = Anfahrt + Preis · x auf und setze gleich.', einheit='h')
    # Mischung
    k1, k2 = R.choice([(2, 6), (4, 10), (3, 8), (5, 12)])     # € pro kg
    x, y = R.randint(2, 12), R.randint(2, 12)
    m, P = x + y, k1 * x + k2 * y
    return Z(f'Ein Händler mischt Nüsse zu {k1} € pro kg mit Nüssen zu {k2} € pro kg. Er erhält {m} kg Mischung im Wert von {P} €. Wie viel kg der billigeren Sorte verwendet er?', x,
             f'({k2} * {m} - {P}) / ({k2} - {k1})', f'I: x + y = {m}, II: {k1}x + {k2}y = {P}. y = {m} − x: {k1}x + {k2 * m} − {k2}x = {P} → {k1 - k2}x = {P - k2 * m} → x = {x}.',
             'Eine Gleichung für die Masse, eine für den Preis.', einheit='kg')


GEN = {'pruefen': g_pruefen, 'einsetzen': g_einsetzen, 'gleichsetzen': g_gleichsetzen, 'addition': g_addition,
       'loesbarkeit': g_loesbarkeit, 'verfahren': g_verfahren, 'sachaufgabe': g_sachaufgabe}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Grundidee', ['pruefen']), ('Lösungsverfahren', ['einsetzen', 'gleichsetzen', 'addition', 'verfahren']),
          ('Verstehen und Anwenden', ['loesbarkeit', 'sachaufgabe'])],
         'Lineare Gleichungssysteme mit zwei Unbekannten rechnerisch lösen, Lösbarkeit begründen, das passende Verfahren wählen und Sachaufgaben lösen.',
         ['Lösung = Zahlenpaar (x | y), das beide Gleichungen erfüllt.',
          'Gleichsetzen, Einsetzen oder Addieren – Ziel: eine Gleichung mit nur einer Variablen.',
          'Falsche Aussage (0 = 5): keine Lösung. Wahre Aussage (0 = 0): unendlich viele Lösungen.'],
         offen=['Lehrplan/Umfang: Gleichungssysteme auch grafisch lösen (Schnittpunkt zweier Geraden) und Lösbarkeit an der Lage der Geraden zeigen. '
                'Dafür braucht die App ein Koordinatensystem mit Geraden; nicht gebaut.',
                'Die Lösung ist ein Zahlenpaar. Da die App je Aufgabe nur eine Zahl abfragen kann, fragen die Rechenaufgaben abwechselnd nach x oder y. '
                'Ein Antworttyp „Zahlenpaar“ wäre sinnvoll.'])
