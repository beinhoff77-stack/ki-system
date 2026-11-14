#!/usr/bin/env python3
"""Thema funktionen.grundbegriffe – Zuordnung und Funktion (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, Z, baue, cz, einsetzen, ist_endlich, kl, lin, zt  # noqa: E402

META = {'thema_schluessel': 'funktionen.grundbegriffe', 'thema_id': 32, 'block_id': 73, 'klasse': {'gym_by': 8, 'rs_by': 8}}

ETAPPEN = [
    {'lernziel': 'eindeutig', 'titel': 'Ist die Zuordnung eine Funktion?',
     'regel': 'Eine ⟦Funktion⟧ ordnet ⟦jedem⟧ x-Wert aus der Definitionsmenge ⟦genau einen⟧ y-Wert zu. Dass verschiedene x denselben y-Wert haben, ist erlaubt.',
     'schritte': ['Zuordnung: (1 | 5), (2 | 7), (3 | 5)', 'Jedes x kommt nur einmal vor. Dass 1 und 3 beide auf 5 gehen, stört nicht.', '⟦Es ist eine Funktion.⟧'],
     'fehler': '(2 | 4), (2 | 6) ist ⟦keine⟧ Funktion: Dem x-Wert 2 sind zwei y-Werte zugeordnet. Umgekehrt wäre (2 | 4), (3 | 4) aber eine Funktion.',
     '_verbot': ['(1 | 5), (2 | 7), (3 | 5)']},
    {'lernziel': 'funktionswert', 'titel': 'Funktionswerte berechnen',
     'regel': 'Der ⟦Funktionsterm⟧ f(x) sagt, wie man aus x den y-Wert berechnet. f(3) heißt: ⟦3 für x einsetzen⟧.',
     'schritte': ['f(x) = 2x² − 3, gesucht f(−2)', 'f(−2) = 2 · (−2)² − 3 = 2 · 4 − 3', '⟦f(−2) = 5⟧'],
     'fehler': 'f(−2) bei f(x) = 2x² − 3 ist nicht 2 · (−4) − 3 = −11: (−2)² = ⟦+4⟧. Negative Zahlen beim Einsetzen immer in Klammern setzen.',
     '_verbot': ['2x² − 3']},
    {'lernziel': 'stelle', 'titel': 'Zu einem y-Wert das x finden',
     'regel': 'Gesucht ist die ⟦Stelle⟧ x, an der f den Wert y hat. Dazu setzt du f(x) = y und ⟦löst die Gleichung⟧ nach x.',
     'schritte': ['f(x) = 3x − 4. Für welches x ist f(x) = 11?', '3x − 4 = 11 → 3x = 15', '⟦x = 5⟧'],
     'probe': 'f(5) = 15 − 4 = 11 ✓',
     'fehler': 'Bei „f(x) = 11“ ist nicht f(11) gesucht. 11 ist der ⟦y-Wert⟧, x ist unbekannt.',
     '_verbot': ['f(x) = 3x − 4']},
    {'lernziel': 'wertetabelle', 'titel': 'Wertetabellen lesen und ergänzen',
     'regel': 'In einer ⟦Wertetabelle⟧ steht oben x, unten f(x). Fehlende Werte berechnest du mit dem Term. Ohne Term suchst du eine ⟦Regel⟧, die zu allen Paaren passt.',
     'schritte': ['f(x) = 4 − x²', 'x = −1: 4 − 1 = 3; x = 0: 4; x = 3: 4 − 9 = −5', 'Tabelle: (−1 | 3), (0 | 4), (3 | ⟦−5⟧)'],
     'fehler': 'Ein Term passt nur, wenn er für ⟦alle⟧ Paare der Tabelle stimmt. Stimmt er für zwei Paare, kann er beim dritten trotzdem falsch sein.',
     '_verbot': ['4 − x²']},
    {'lernziel': 'mengen', 'titel': 'Definitionsmenge und Wertemenge',
     'regel': 'Die ⟦Definitionsmenge⟧ D enthält alle x, die man einsetzen darf. Die ⟦Wertemenge⟧ W enthält alle y-Werte, die dabei herauskommen.',
     'schritte': ['f(x) = 2x + 1 mit D = {0; 1; 3}', 'f(0) = 1, f(1) = 3, f(3) = 7', '⟦W = {1; 3; 7}⟧'],
     'fehler': 'Bei f(x) = 1/(x − 2) ist D nicht ℚ: Für x = 2 wird der Nenner 0. Also ⟦D = ℚ \\ {2}⟧.',
     '_verbot': ['D = {0; 1; 3}']},
    {'lernziel': 'nullstellen', 'titel': 'Nullstellen berechnen',
     'regel': 'Eine ⟦Nullstelle⟧ ist ein x mit f(x) = 0. Dort schneidet der Graph die ⟦x-Achse⟧. Du findest sie, indem du ⟦f(x) = 0⟧ löst.',
     'schritte': ['f(x) = 2x − 7', '2x − 7 = 0 → 2x = 7', '⟦x = 3,5⟧'],
     'fehler': 'Die Nullstelle von f(x) = 2x − 7 ist nicht −7: f(0) = −7 ist der ⟦y-Achsenabschnitt⟧. Für die Nullstelle muss ⟦y = 0⟧ sein.',
     '_verbot': ['2x − 7']},
    {'lernziel': 'punkt_graph', 'titel': 'Liegt der Punkt auf dem Graphen?',
     'regel': 'Ein Punkt P(a | b) liegt auf dem ⟦Graphen⟧ von f, wenn ⟦f(a) = b⟧ ist. Setze die x-Koordinate ein und vergleiche mit der y-Koordinate.',
     'schritte': ['f(x) = x² − 2x, Punkt P(3 | 3)', 'f(3) = 9 − 6 = 3', '3 = 3: ⟦P liegt auf dem Graphen.⟧'],
     'fehler': 'Bei P(3 | 1) setzt man nicht die 1 für x ein. Die ⟦erste⟧ Koordinate ist x, die ⟦zweite⟧ ist y.',
     '_verbot': ['x² − 2x']},
]


def nz(R, lo=-6, hi=6):
    return R.choice([k for k in range(lo, hi + 1) if k])


def quad(a, b, c):
    """a·x² + b·x + c als Text."""
    s = ''
    if a: s = ('−' if a < 0 else '') + ('' if abs(a) == 1 else zt(abs(a))) + 'x²'
    for k, v in ((b, 'x'), (c, '')):
        if not k: continue
        t = lin(k, 0) if v else zt(k)
        s = t if not s else s + (' − ' if k < 0 else ' + ') + t.lstrip('−')
    return s or '0'


def paare(ps):
    return ', '.join(f'({zt(x)} | {zt(y)})' for x, y in ps)


EIND = ['Ja, jedem x ist genau ein y zugeordnet.', 'Nein, einem x sind zwei verschiedene y zugeordnet.',
        'Nein, zwei verschiedene x haben denselben y-Wert.', 'Nein, die y-Werte müssen größer werden.']
SITUATIONEN = [
    ('Jedem Schüler einer Klasse wird sein Geburtsdatum zugeordnet.', True),
    ('Jedem Datum wird zugeordnet, welche Schüler einer Klasse an diesem Tag Geburtstag haben (einzeln aufgezählt).', False),
    ('Jeder Zahl wird ihr Quadrat zugeordnet.', True),
    ('Jeder positiven Zahl wird eine Zahl zugeordnet, deren Quadrat sie ist.', False),
    ('Jeder Uhrzeit eines Tages wird die an einem Ort gemessene Temperatur zugeordnet.', True),
    ('Jeder gemessenen Temperatur wird die Uhrzeit zugeordnet, zu der sie gemessen wurde.', False),
    ('Jedem Auto wird sein Kennzeichen zugeordnet.', True),
    ('Jeder Postleitzahl wird eine Straße in diesem Gebiet zugeordnet.', False),
    ('Jeder Menge Äpfel (in kg) wird ihr Preis bei festem Kilopreis zugeordnet.', True),
    ('Jedem Kreis wird sein Flächeninhalt zugeordnet.', True),
    ('Jedem Flächeninhalt wird ein Rechteck mit diesem Inhalt zugeordnet.', False),
    ('Jeder natürlichen Zahl wird einer ihrer Teiler zugeordnet.', False),
    ('Jeder natürlichen Zahl wird die Anzahl ihrer Teiler zugeordnet.', True),
    ('Jeder Person wird ihre Körpergröße am heutigen Tag zugeordnet.', True),
    ('Jeder Körpergröße wird eine Person mit dieser Größe zugeordnet.', False),
]


def g_eindeutig(R, st):
    if st == 2 and R.random() < .5:
        sit, ok = R.choice(SITUATIONEN)
        r = 'Ja, das ist eine Funktion.' if ok else 'Nein, das ist keine Funktion.'
        return A(R, f'Ist diese Zuordnung eine Funktion? {sit}', r,
                 ['Nein, das ist keine Funktion.' if ok else 'Ja, das ist eine Funktion.', 'Das kann man ohne Zahlen nicht entscheiden.'],
                 'Jedem Ausgangswert ist genau ein Wert zugeordnet.' if ok else 'Zu einem Ausgangswert kann es mehrere zugeordnete Werte geben (oder keinen).',
                 'Frage dich: Kann es zu einem Ausgangswert zwei verschiedene Ergebnisse geben?')
    n = R.randint(4, 6)
    xs = R.sample(range(-6, 10), n)
    ys = [R.randint(-5, 9) for _ in xs]
    art = R.choice(['ok', 'doppel_y', 'doppel_x']) if st == 1 else R.choice(['ok', 'doppel_y', 'doppel_x', 'doppel_y'])
    if art == 'doppel_y':
        ys[1] = ys[0]
    ps = list(zip(xs, ys))
    if art == 'doppel_x':
        x0 = xs[0]; ps.append((x0, ys[0] + R.choice([1, 2, -3])))
    R.shuffle(ps)
    if st == 3:
        # vier Zuordnungen, eine ist keine Funktion
        listen = []
        for k in range(4):
            xs = R.sample(range(-5, 9), 4); ys = [R.randint(-4, 8) for _ in xs]
            if k == 1: ys[1] = ys[0]
            ps2 = list(zip(xs, ys))
            if k == 0: ps2.append((xs[2], ys[2] + R.choice([1, -2])))
            R.shuffle(ps2)
            listen.append(paare(ps2))
        return A(R, 'Welche Zuordnung ist KEINE Funktion?', listen[0], listen[1:],
                 f'Bei {listen[0]} kommt ein x-Wert zweimal mit verschiedenen y-Werten vor. Gleiche y-Werte bei verschiedenen x sind erlaubt.',
                 'Suche einen x-Wert, der zweimal vorkommt.')
    r = EIND[1] if art == 'doppel_x' else EIND[0]
    return A(R, f'Ist die Zuordnung {paare(ps)} eine Funktion?', r, [e for e in EIND if e != r],
             'Ein x-Wert hat zwei y-Werte – keine Funktion.' if art == 'doppel_x' else 'Jeder x-Wert kommt nur einmal vor – also Funktion (gleiche y-Werte sind erlaubt).',
             'Schau nur auf die x-Werte: Kommt einer doppelt vor?')


def zufall_f(R, st):
    """(Text, Funktion) – lineare, quadratische oder Bruch-Funktion."""
    art = R.choice({1: ['lin'], 2: ['lin', 'quad', 'quad'], 3: ['quad', 'bruch', 'lin_dez']}[st])
    if art == 'lin':
        m, t = nz(R, -6, 6), R.randint(-9, 9)
        return lin(m, t), (lambda x: m * x + t), f'({m}) * ({{x}}) + ({t})'
    if art == 'lin_dez':
        m, t = Fr(nz(R, -9, 9), R.choice([2, 4, 5])), Fr(R.randint(-20, 20), 2)
        return lin(m, t), (lambda x: m * x + t), f'{cz(m)} * ({{x}}) + {cz(t)}'
    if art == 'quad':
        a, b, c = nz(R, -3, 3), R.randint(-5, 5), R.randint(-9, 9)
        return quad(a, b, c), (lambda x: a * x * x + b * x + c), f'({a}) * ({{x}})**2 + ({b}) * ({{x}}) + ({c})'
    a, b = nz(R, -12, 12), nz(R, -5, 5)
    return f'{zt(a)}/({lin(1, b)})', (lambda x: Fr(a) / (x + b)), f'{a} / (({{x}}) + ({b}))'


def g_funktionswert(R, st):
    while True:
        txt, f, c = zufall_f(R, st)
        x = Fr(R.randint(-6, 6))
        if st == 3 and R.random() < .4: x = Fr(R.choice([-5, -3, -1, 1, 3, 5]), 2)
        try: y = f(x)
        except ZeroDivisionError: continue
        if ist_endlich(y) and len(zt(y)) <= 7: break
    return Z(f'Berechne f({zt(x)}) für f(x) = {txt}.', y, c.format(x=cz(x)),
             f'x = {zt(x)} einsetzen: f({zt(x)}) = {einsetzen(txt, x)} = {zt(y)}.',
             'Setze die Zahl für jedes x ein. Negative Zahlen in Klammern!')


def g_stelle(R, st):
    if st == 3 and R.random() < .5:
        while True:
            a, y = nz(R, -24, 24), R.choice([k for k in range(-8, 9) if k not in (0, 1, -1)])
            x = Fr(a, y)
            if ist_endlich(x) and len(zt(x)) <= 5: break
        return Z(f'Für welches x ist f(x) = {zt(y)}, wenn f(x) = {zt(a)}/x?', x, f'{a} / ({y})',
                 f'{zt(a)}/x = {zt(y)} → {zt(a)} = {zt(y)}x → x = {zt(a)} : {kl(y)} = {zt(x)}.', 'Multipliziere mit x, dann teile.')
    while True:
        m = Fr(nz(R, -6, 6)) if st < 3 else Fr(nz(R, -9, 9), R.choice([1, 2, 4]))
        t = Fr(R.randint(-9, 9))
        x = Fr(R.randint(-8, 9)) if st == 1 else Fr(R.randint(-16, 16), R.choice([1, 2]))
        y = m * x + t
        if m != 0 and (m, t) != (1, 0) and ist_endlich(y) and len(zt(y)) <= 6: break
    return Z(f'Für welches x gilt f(x) = {zt(y)}, wenn f(x) = {lin(m, t)}?', x, f'({cz(y)} - ({cz(t)})) / {cz(m)}',
             f'{lin(m, t)} = {zt(y)} → {lin(m, 0)} = {zt(y - t)} → x = {zt(x)}.', 'Setze den Term gleich dem y-Wert und löse nach x.')


def g_wertetabelle(R, st):
    if st == 3:
        m, t = nz(R, -5, 5), R.randint(-6, 6)
        xs = sorted(R.sample(range(-3, 5), 3))
        ps = [(x, m * x + t) for x in xs]
        richtig = lin(m, t)
        falsch = [lin(-m, t), lin(m, -t) if t else lin(m, 1), lin(t, m) if t and t != m else lin(m + 1, t), lin(m, ps[0][1] - m * xs[0] + 1)]
        # falsche Terme dürfen nicht zu allen Paaren passen
        falsch = [f for f, (mm, tt) in zip(falsch, [(-m, t), (m, -t if t else 1), (t, m) if t and t != m else (m + 1, t), (m, ps[0][1] - m * xs[0] + 1)])
                  if any(mm * x + tt != y for x, y in ps)]
        return A(R, f'Welcher Funktionsterm passt zur Wertetabelle {paare(ps)}?', f'f(x) = {richtig}', [f'f(x) = {f}' for f in falsch],
                 f'Probe: ' + '; '.join(f'f({zt(x)}) = {zt(y)}' for x, y in ps) + '. Nur f(x) = ' + richtig + ' passt zu allen Paaren.',
                 'Setze die x-Werte in jeden Term ein. Der richtige Term passt zu allen Paaren.')
    txt, f, c = zufall_f(R, 2 if st == 2 else 1)
    xs = sorted(R.sample(range(-4, 6), 4))
    try: ps = [(x, f(Fr(x))) for x in xs]
    except ZeroDivisionError: return g_wertetabelle(R, st)
    if any(not ist_endlich(y) for _, y in ps): return g_wertetabelle(R, st)
    k = R.randrange(4)
    if st == 2 and 'x²' not in txt and R.random() < .5:
        # fehlender x-Wert bei linearer Funktion
        x0, y0 = ps[k]
        tab = ', '.join(f'({zt(x)} | {zt(y)})' if i != k else f'(□ | {zt(y)})' for i, (x, y) in enumerate(ps))
        m = (ps[1][1] - ps[0][1]) / (xs[1] - xs[0]); t = ps[0][1] - m * xs[0]
        return Z(f'Wertetabelle zu f(x) = {txt}: {tab}. Welcher x-Wert fehlt?', x0, f'({cz(y0)} - ({cz(t)})) / {cz(m)}',
                 f'{txt} = {zt(y0)} lösen: x = {zt(x0)}.', 'Setze f(x) gleich dem y-Wert und löse nach x.')
    x0, y0 = ps[k]
    tab = ', '.join(f'({zt(x)} | {zt(y)})' if i != k else f'({zt(x)} | □)' for i, (x, y) in enumerate(ps))
    return Z(f'Wertetabelle zu f(x) = {txt}: {tab}. Welcher y-Wert fehlt?', y0, c.format(x=x0),
             f'x = {zt(x0)} einsetzen: f({zt(x0)}) = {einsetzen(txt, x0)} = {zt(y0)}.', 'Setze den x-Wert in den Term ein.')


def mengentext(xs):
    return '{' + '; '.join(zt(x) for x in sorted(set(xs))) + '}'


def g_mengen(R, st):
    if st == 1:
        b = nz(R, -9, 9); a = nz(R, -9, 9)
        return A(R, f'Gib die maximale Definitionsmenge von f(x) = {zt(a)}/({lin(1, -b)}) an.', f'D = ℚ \\ {{{zt(b)}}}',
                 [f'D = ℚ \\ {{{zt(-b)}}}', 'D = ℚ', f'D = ℚ \\ {{{zt(a)}}}' if a not in (b, -b) else 'D = ℚ \\ {0}'],
                 f'Der Nenner {lin(1, -b)} ist 0 für x = {zt(b)}. Diese Zahl muss raus.', 'Welche Zahl macht den Nenner 0?')
    if st == 2:
        txt, f, _ = zufall_f(R, 2)
        if '/' in txt: return g_mengen(R, st)
        D = sorted(R.sample(range(-3, 4), R.randint(3, 4)))
        W = [f(Fr(x)) for x in D]
        falsch = [mengentext(D), mengentext([w + 1 for w in W]), mengentext([-w for w in W]) if any(W) else mengentext([1, 2])]
        return A(R, f'f(x) = {txt} mit D = {mengentext(D)}. Gib die Wertemenge W an.', 'W = ' + mengentext(W), ['W = ' + s for s in falsch],
                 'Funktionswerte: ' + ', '.join(f'f({zt(x)}) = {zt(w)}' for x, w in zip(D, W)) + f'. W = {mengentext(W)}.',
                 'Berechne für jedes x aus D den Funktionswert. Gleiche Werte schreibt man nur einmal.')
    art = R.choice(['quadrat', 'betrag', 'konst', 'bruch2'])
    c = R.randint(-6, 6)
    if art == 'quadrat':
        r = f'W = {{y | y ≥ {zt(c)}}}'
        return A(R, f'f(x) = x² {"+" if c >= 0 else "−"} {abs(c)} mit D = ℚ. Welche Wertemenge hat f?', r, [f'W = {{y | y ≤ {zt(c)}}}', 'W = ℚ', f'W = {{y | y ≥ 0}}' if c else 'W = {y | y > 0}'],
                 f'x² ist nie negativ, kleinster Wert 0 (bei x = 0). Also f(x) ≥ {zt(c)}.', 'Welchen kleinsten Wert kann x² annehmen?')
    if art == 'konst':
        return A(R, f'f(x) = {zt(c)} mit D = ℚ. Welche Wertemenge hat f?', f'W = {{{zt(c)}}}', ['W = ℚ', f'W = ℚ \\ {{{zt(c)}}}', '{0}'],
                 f'Jedem x wird derselbe Wert {zt(c)} zugeordnet. Also W = {{{zt(c)}}}.', 'Welche y-Werte können überhaupt herauskommen?')
    if art == 'bruch2':
        a, b = R.sample([k for k in range(-6, 7) if k], 2)
        return A(R, f'Gib die maximale Definitionsmenge von f(x) = 1/(({lin(1, -a)})({lin(1, -b)})) an.', f'D = ℚ \\ {mengentext([a, b])}',
                 [f'D = ℚ \\ {mengentext([-a, -b])}', f'D = ℚ \\ {{{zt(a)}}}', 'D = ℚ'],
                 f'Der Nenner ist 0 für x = {zt(a)} und für x = {zt(b)}.', 'Ein Produkt ist 0, wenn einer der Faktoren 0 ist.')
    return A(R, f'f(x) = −x² {"+" if c >= 0 else "−"} {abs(c)} mit D = ℚ. Welche Wertemenge hat f?', f'W = {{y | y ≤ {zt(c)}}}',
             [f'W = {{y | y ≥ {zt(c)}}}', 'W = ℚ', 'W = {y | y ≤ 0}' if c else 'W = {y | y < 0}'],
             f'−x² ist nie positiv, größter Wert 0. Also f(x) ≤ {zt(c)}.', 'Welchen größten Wert kann −x² annehmen?')


def g_nullstellen(R, st):
    if st == 1 or (st == 2 and R.random() < .5):
        while True:
            m = Fr(nz(R, -8, 8)); x0 = Fr(R.randint(-9, 9)) if st == 1 else Fr(R.randint(-20, 20), R.choice([2, 4, 5]))
            t = -m * x0
            if ist_endlich(x0) and t.denominator == 1: break
        return Z(f'Berechne die Nullstelle von f(x) = {lin(m, t)}.', x0, f'-({cz(t)}) / {cz(m)}',
                 f'{lin(m, t)} = 0 → {lin(m, 0)} = {zt(-t)} → x = {zt(x0)}.', 'Setze f(x) = 0 und löse nach x.')
    if st == 2:
        a, b = R.sample([k for k in range(-7, 8) if k], 2)
        r = f'x = {zt(min(a, b))} und x = {zt(max(a, b))}'
        return A(R, f'Welche Nullstellen hat f(x) = ({lin(1, -a)})({lin(1, -b)})?', r,
                 [f'x = {zt(min(-a, -b))} und x = {zt(max(-a, -b))}', f'x = {zt(a * b)}', f'x = {zt(-a)} und x = {zt(b)}' if -a != b else 'keine Nullstelle'],
                 f'Ein Produkt ist 0, wenn ein Faktor 0 ist: {lin(1, -a)} = 0 → x = {zt(a)}; {lin(1, -b)} = 0 → x = {zt(b)}.',
                 'Wann ist ein Produkt gleich 0?')
    while True:
        a, b, c = nz(R, -6, 6), R.randint(-12, 12), nz(R, -6, 6)
        x0 = Fr(-b, a)
        if x0 != c and ist_endlich(x0) and len(zt(x0)) <= 5 and b: break
    if R.random() < .5:
        return Z(f'Berechne die Nullstelle von f(x) = ({lin(a, b)})/({lin(1, -c)}).', x0, f'-({b}) / ({a})',
                 f'Ein Bruch ist 0, wenn der Zähler 0 ist (und der Nenner nicht): {lin(a, b)} = 0 → x = {zt(x0)}. Nenner dort: {zt(x0 - c)} ≠ 0.',
                 'Ein Bruch ist 0, wenn sein Zähler 0 ist.')
    a, b = nz(R, -5, 5), nz(R, -12, 12)
    x1 = Fr(-b, a)
    if not ist_endlich(x1) or len(zt(x1)) > 5: return g_nullstellen(R, st)
    r = f'x = 0 und x = {zt(x1)}'
    return A(R, f'Welche Nullstellen hat f(x) = x({lin(a, b)})?', r, [f'nur x = {zt(x1)}', f'x = 0 und x = {zt(-x1)}', f'x = 0 und x = {zt(b)}' if b != x1 else 'nur x = 0'],
             f'x = 0 oder {lin(a, b)} = 0 → x = {zt(x1)}.', 'Ein Produkt ist 0, wenn einer der Faktoren 0 ist. Vergiss den Faktor x nicht.')


def g_punkt_graph(R, st):
    if st == 3:
        while True:
            a, k = nz(R, -5, 6), Fr(nz(R, -6, 6), R.choice([1, 1, 2]))
            t = R.randint(-6, 6)
            b = k * a + t
            if b.denominator == 1: break
        return Z(f'Der Punkt P({zt(a)} | {zt(b)}) liegt auf dem Graphen von f(x) = k · x {"+" if t >= 0 else "−"} {abs(t)}. Bestimme k.', k, f'({cz(b)} - ({t})) / ({a})',
                 f'f({zt(a)}) = {zt(b)}: k · {kl(a)} {"+" if t >= 0 else "−"} {abs(t)} = {zt(b)} → k · {kl(a)} = {zt(b - t)} → k = {zt(k)}.',
                 'Setze die Koordinaten von P in die Gleichung y = f(x) ein und löse nach k.')
    txt, f, _ = zufall_f(R, st)
    if '/' in txt: return g_punkt_graph(R, st)
    while True:
        x = Fr(R.randint(-4, 5)); y = f(x)
        if y != x and abs(y) < 60: break
    richtig = f'P({zt(x)} | {zt(y)})'
    falsch = [f'P({zt(y)} | {zt(x)})', f'P({zt(x)} | {zt(y + R.choice([1, -1, 2]))})', f'P({zt(-x)} | {zt(y)})' if f(-x) != y else f'P({zt(x + 1)} | {zt(y)})']
    falsch = [p for p in falsch if p != richtig]
    return A(R, f'Welcher Punkt liegt auf dem Graphen von f(x) = {txt}?', richtig, falsch,
             f'f({zt(x)}) = {zt(y)}, also liegt {richtig} auf dem Graphen.', 'Setze die x-Koordinate ein und vergleiche mit der y-Koordinate.')


GEN = {'eindeutig': g_eindeutig, 'funktionswert': g_funktionswert, 'stelle': g_stelle, 'wertetabelle': g_wertetabelle,
       'mengen': g_mengen, 'nullstellen': g_nullstellen, 'punkt_graph': g_punkt_graph}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Was ist eine Funktion?', ['eindeutig', 'mengen']), ('Mit dem Term rechnen', ['funktionswert', 'stelle', 'wertetabelle']),
          ('Graph und Nullstellen', ['nullstellen', 'punkt_graph'])],
         'Funktionen als eindeutige Zuordnungen erkennen; mit Funktionsterm, Wertetabelle und Graph arbeiten; Definitions- und Wertemenge sowie Nullstellen bestimmen.',
         ['Funktion: Jedem x genau ein y.', 'f(a) berechnen: a einsetzen. f(x) = b lösen: x gesucht.',
          'Nullstelle: f(x) = 0. P(a | b) liegt auf dem Graphen, wenn f(a) = b.'],
         offen=['Graphen zeichnen und ablesen (Funktionswerte, Nullstellen, Wertemenge am Graphen) sowie „Ist dieser Graph eine Funktion?“ (senkrechte Linie) brauchen ein '
                'Koordinatensystem in der App; nicht gebaut.'])
