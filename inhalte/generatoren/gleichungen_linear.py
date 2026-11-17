#!/usr/bin/env python3
"""Thema gleichungen.linear – Lineare Gleichungen (Gymnasium Bayern, Klasse 7). Nachbau Runde 5.

Äquivalenzumformungen mit Waage, Variable auf beiden Seiten, Klammern, Probe und Fehler finden,
Sonderfälle (keine/unendlich viele Lösungen), Sachaufgaben aufstellen, lösen und deuten.
"""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _nachbau import A, L, Z, baue, cz, dez, kl, lin, mit_bild, waage, zt  # noqa: E402

META = {'thema_schluessel': 'gleichungen.linear', 'thema_id': 2, 'block_id': 61, 'klasse': {'gym_by': 7, 'rs_by': 7, 'ib_myp': 2}}
LQ = 'L = ℚ (jede Zahl)'
L0 = 'L = { } (keine Lösung)'


def kla(a, b, var='x'):
    """a(x + b) als Text."""
    vor = '' if a == 1 else ('−' if a == -1 else zt(a))
    return f'{vor}({lin(1, b, var)})'


def fz(x):
    x = Fr(x)
    return ('−' if x < 0 else '') + f'{abs(x.numerator)}/{x.denominator}'


def plus(term):
    return f' − {term[1:]}' if term.startswith('−') else f' + {term}'


def endlich(x):
    return dez(Fr(x)) is not None


def sig(b):
    """„− 5“ bzw. „+ 5“ als Umformung, die b wegbringt."""
    return f'− {zt(b)}' if b > 0 else f'+ {zt(-b)}'


def xsig(c):
    return f'− {lin(c, 0)}' if c > 0 else f'+ {lin(-c, 0)}'


def bruchluecke(text, x, w, h=''):
    x = Fr(x)
    return L(text, 'x = □/□', [x.numerator, x.denominator], [str(x.numerator), str(x.denominator)], w, h,
             hinweis='Trage Zähler und Nenner vollständig gekürzt ein; ein Minus gehört in den Zähler.')


def flaeche_bild():
    return {'typ': 'figur', 'label': 'Rechteck mit Breite 3 und Länge x + 2, geteilt in die Flächen 3 · x und 3 · 2',
            'punkte': {'_A': [0, 0], '_E': [4, 0], '_B': [6, 0], '_C': [6, 3], '_F': [4, 3], '_D': [0, 3]},
            'flaeche': ['_A', '_B', '_C', '_D'],
            'linien': [['_A', '_E', 'x'], ['_E', '_B', '2'], ['_B', '_C'], ['_C', '_F'], ['_F', '_D'], ['_D', '_A', '3'], ['_E', '_F', '', 'gestrichelt']]}


ETAPPEN = [
    {'lernziel': 'waage', 'titel': 'Äquivalenzumformungen an der Waage',
     'regel': 'Eine Gleichung ist wie eine Waage im Gleichgewicht. Sie bleibt im Gleichgewicht, wenn du auf ⟦beiden Seiten dasselbe⟧ tust: '
              'dieselbe Zahl addieren oder subtrahieren, mit derselben Zahl (nicht 0) multiplizieren oder durch sie dividieren. '
              'Das heißt ⟦Äquivalenzumformung⟧. Schreibe sie hinter einen Strich, z. B. | − 5.',
     'schritte': ['Ein Paket mit 3 gleichen Dosen (je x kg) und 5 kg Zusatzgewicht wiegt 20 kg: 3x + 5 = 20   | − 5',
                  '3x = 15   | : 3',
                  '⟦x = 5⟧. Eine Dose wiegt 5 kg.'],
     'probe': '3 · 5 + 5 = 20 ✓',
     'fehler': 'Nur auf einer Seite umformen: Aus 3x + 5 = 20 wird mit | − 5 nicht 3x = 25 und auch nicht 3x = 20. '
               'Die 5 verschwindet links, also muss sie auch rechts ⟦abgezogen⟧ werden: 3x = 15.',
     'bild': waage('3x + 5', '20'),
     '_verbot': ['3x + 5 = 20']},
    {'lernziel': 'beide_seiten', 'titel': 'Die Variable auf beiden Seiten',
     'regel': 'Steht x auf beiden Seiten, bringst du zuerst alle ⟦x-Glieder auf eine Seite⟧ (am besten dorthin, wo mehr x stehen) und alle ⟦Zahlen auf die andere⟧. '
              'An der Waage: Auf beiden Seiten gleich viele Dosen wegnehmen.',
     'schritte': ['Links 5 Dosen und 3 kg, rechts 2 Dosen und 15 kg: 5x + 3 = 2x + 15   | − 2x',
                  '3x + 3 = 15   | − 3',
                  '3x = 12   | : 3  →  ⟦x = 4⟧'],
     'probe': 'links 5 · 4 + 3 = 23, rechts 2 · 4 + 15 = 23 ✓',
     'fehler': 'Das Vorzeichen beim Herüberbringen vergessen: Aus 5x + 3 = 2x + 15 wird mit | − 2x nicht 7x + 3 = 15. '
               'Rechts wird 2x ⟦weggenommen⟧, also links auch: 5x − 2x = 3x.',
     'bild': waage('5x + 3', '2x + 15'),
     '_verbot': ['5x + 3 = 2x + 15']},
    {'lernziel': 'klammern', 'titel': 'Gleichungen mit Klammern',
     'regel': 'Löse zuerst die ⟦Klammern auf⟧: Der Faktor vor der Klammer wird mit ⟦jedem⟧ Summanden multipliziert. Ein ⟦Minus vor der Klammer⟧ dreht alle Vorzeichen in der Klammer um. '
              'Dann fasst du zusammen und löst wie gewohnt.',
     'schritte': ['Drei Tüten mit je x Äpfeln und 2 Birnen sind 3x + 6 Früchte – wie beim Rechteck: 3(x + 2) = 3x + 6.',
                  '3(x + 2) = 2x + 11  →  3x + 6 = 2x + 11   | − 2x − 6',
                  '⟦x = 5⟧'],
     'probe': '3 · (5 + 2) = 21 und 2 · 5 + 11 = 21 ✓',
     'fehler': '−(x + 3) ist nicht −x + 3. Das Minus gilt für die ⟦ganze⟧ Klammer: −(x + 3) = −x − 3. Ebenso ist 3(x + 2) nicht 3x + 2, sondern 3x + 6.',
     'bild': flaeche_bild(),
     '_verbot': ['3(x + 2) = 2x + 11']},
    {'lernziel': 'probe', 'titel': 'Probe machen und Fehler finden',
     'regel': 'Die ⟦Probe⟧ zeigt, ob eine Lösung stimmt: Setze sie in die ⟦ursprüngliche⟧ Gleichung ein und berechne beide Seiten ⟦getrennt⟧. '
              'Stimmen sie nicht überein, suchst du den Fehler Zeile für Zeile.',
     'schritte': ['Jemand löst 4x − 7 = x + 8 so: 3x − 7 = 8, dann 3x = 1, also x = 1/3.',
                  'Probe mit 1/3: links 4/3 − 7 ≈ −5,7, rechts 1/3 + 8 ≈ 8,3. Passt nicht.',
                  'Fehler in Zeile 2: | + 7 ergibt 3x = 15, also ⟦x = 5⟧. Probe: 13 = 13 ✓'],
     'fehler': 'Die Probe in einer umgeformten Zeile statt in der ursprünglichen Gleichung machen. Ist schon die Umformung falsch, passt die Probe dort trotzdem – der Fehler bleibt ⟦unentdeckt⟧.',
     '_verbot': ['4x − 7 = x + 8']},
    {'lernziel': 'sonderfaelle', 'titel': 'Keine oder unendlich viele Lösungen',
     'regel': 'Manchmal fällt x beim Umformen ganz weg. Bleibt eine ⟦falsche⟧ Aussage stehen (z. B. 3 = 5), gibt es ⟦keine Lösung⟧: L = { }. '
              'Bleibt eine ⟦wahre⟧ Aussage stehen (z. B. 6 = 6), ist ⟦jede Zahl⟧ eine Lösung: L = ℚ.',
     'schritte': ['Zwei Handytarife: beide 2 € pro GB, der eine mit 3 € Grundgebühr, der andere mit 5 €: 2x + 3 = 2x + 5   | − 2x',
                  '3 = 5 ist falsch. Die Tarife kosten ⟦nie⟧ gleich viel: L = { }.',
                  'Dagegen 2(x + 3) = 2x + 6 führt zu 6 = 6 – wahr für jedes x: ⟦L = ℚ⟧.'],
     'fehler': 'Aus 3 = 5 auf „x = 0“ schließen oder aus 6 = 6 auf „x = 6“. Wenn x weg ist, entscheidet nur, ob die Aussage ⟦wahr oder falsch⟧ ist.',
     '_verbot': ['2x + 3 = 2x + 5', '2(x + 3) = 2x + 6']},
    {'lernziel': 'sach', 'titel': 'Sachaufgaben mit Gleichungen',
     'regel': 'So gehst du vor: ⟦1. Variable festlegen⟧ (x = …), ⟦2. Gleichung aufstellen⟧, ⟦3. lösen⟧, ⟦4. Antwort im Sachzusammenhang⟧ – und prüfen, ob die Lösung ⟦sinnvoll⟧ ist '
              '(keine halben Personen, keine negativen Längen).',
     'schritte': ['Tarif A: 10 € Grundgebühr und 2 € pro GB. Tarif B: 4 € pro GB. Ab wie vielen GB sind beide gleich teuer?',
                  'x = Anzahl GB. 10 + 2x = 4x   | − 2x  →  10 = 2x   | : 2  →  x = 5.',
                  'Bei ⟦5 GB⟧ kosten beide 20 €.'],
     'probe': '10 + 2 · 5 = 20 und 4 · 5 = 20 ✓',
     'fehler': '„Zwei aufeinanderfolgende Zahlen ergeben zusammen 31“ ist nicht x + x = 31 (dann wäre x = 15,5 – keine ganze Zahl). '
               'Die zweite Zahl ist ⟦x + 1⟧: x + (x + 1) = 31, also x = 15 und 16.'},
]


# ---------------- Waage / Äquivalenzumformungen ----------------
def g_waage(R, s):
    if s == 1:
        art = R.choice(['plus', 'mal', 'naechste', 'plus_neg'])
        x = R.choice([v for v in range(-12, 16) if v])
        if art in ('plus', 'plus_neg'):
            b = R.choice([v for v in range(-20, 21) if v])
            c = x + b
            return Z(f'Löse {lin(1, b)} = {zt(c)}.', x, f'{c} - ({b})', f'| {sig(b)}: x = {zt(c)} {sig(b)} = {zt(x)}. Probe: {zt(x)} {"+" if b > 0 else "−"} {abs(b)} = {zt(c)} ✓',
                     'Welche Zahl musst du auf beiden Seiten addieren oder subtrahieren, damit x allein steht?')
        if art == 'mal':
            a = R.choice([v for v in range(-9, 10) if v not in (0, 1, -1)])
            return Z(f'Löse {lin(a, 0)} = {zt(a * x)}.', x, f'{a * x} / ({a})', f'| : {kl(a)}: x = {zt(a * x)} : {kl(a)} = {zt(x)}.',
                     'Durch welche Zahl musst du beide Seiten teilen?')
        a, b = R.randint(2, 9), R.choice([v for v in range(-15, 16) if v])
        c = a * x + b
        return A(R, f'Welche Umformung ist bei {lin(a, b)} = {zt(c)} als erste sinnvoll?', f'| {sig(b)}', [f'| {sig(-b)}', f'| : {zt(c)}', f'| − {a}'],
                 f'Zuerst die Zahl ohne x wegbringen: | {sig(b)} ergibt {lin(a, 0)} = {zt(c - b)}. Danach | : {a}.',
                 'Was steht links außer dem x-Glied? Wie bekommst du es weg?')
    if s == 2:
        art = R.choice(['normal', 'normal', 'neg_a', 'ergebnis'])
        x = R.choice([v for v in range(-15, 21) if v])
        a = R.randint(2, 12) if art != 'neg_a' else -R.randint(2, 9)
        b = R.choice([v for v in range(-30, 31) if v])
        c = a * x + b
        if art == 'ergebnis':
            return A(R, f'Welche Gleichung entsteht aus {lin(a, b)} = {zt(c)} durch | {sig(b)}?', f'{lin(a, 0)} = {zt(c - b)}',
                     [f'{lin(a, 0)} = {zt(c + b)}', f'{lin(a, b)} = {zt(c - b)}', f'x = {zt(c - b)}'],
                     f'Links fällt {zt(b)} weg, rechts rechnest du {zt(c)} {sig(b)} = {zt(c - b)}.', 'Beide Seiten verändern sich.')
        return Z(f'Löse {lin(a, b)} = {zt(c)}.', x, f'({c} - ({b})) / ({a})',
                 f'| {sig(b)}: {lin(a, 0)} = {zt(c - b)}. | : {kl(a)}: x = {zt(x)}. Probe: {zt(a)} · {kl(x)} {"+" if b > 0 else "−"} {abs(b)} = {zt(c)} ✓',
                 'Erst die Zahl ohne x wegbringen, dann durch die Zahl vor dem x teilen.' + (' Achtung: Sie ist negativ.' if a < 0 else ''))
    art = R.choice(['minus_x', 'bruch', 'dezimal', 'bruchloesung'])
    if art == 'minus_x':
        x = R.choice([v for v in range(-20, 21) if v])
        b = R.choice([v for v in range(-15, 16) if v])
        c = b - x
        return Z(f'Löse {zt(b)} − x = {zt(c)}.', x, f'{b} - ({c})',
                 f'| {sig(b)}: −x = {zt(c - b)}. | · (−1): x = {zt(x)}. Probe: {zt(b)} − {kl(x)} = {zt(c)} ✓',
                 'Am Ende steht −x = … . Was ist dann x?')
    if art == 'bruch':
        n = R.choice([2, 3, 4, 5])
        z = R.randint(1, n - 1)
        if Fr(z, n).denominator != n: return g_waage(R, s)
        x = n * R.choice([v for v in range(-8, 13) if v])
        b = R.choice([v for v in range(-10, 11) if v])
        c = Fr(z, n) * x + b
        return Z(f'Löse {z}/{n} x {"+" if b > 0 else "−"} {abs(b)} = {zt(c)}.', x, f'(({cz(c)}) - ({b})) * {n} / {z}',
                 f'| {sig(b)}: {z}/{n} x = {zt(c - b)}. | · {n}: ' + (f'{z}x = {zt((c - b) * n)}. | : {z}: x = {zt(x)}.' if z != 1 else f'x = {zt(x)}.'),
                 f'Multipliziere mit {n}, um den Bruch loszuwerden.')
    if art == 'dezimal':
        a = R.choice([Fr(1, 2), Fr(3, 2), Fr(5, 2), Fr(1, 4)])
        x = R.choice([v for v in range(-10, 21) if v and (a * v).denominator == 1])
        b = R.choice([v for v in range(-9, 10) if v])
        c = a * x + b
        return Z(f'Löse {zt(a)}x {"+" if b > 0 else "−"} {abs(b)} = {zt(c)}.', x, f'(({cz(c)}) - ({b})) / ({cz(a)})',
                 f'| {sig(b)}: {zt(a)}x = {zt(c - b)}. | : {zt(a)}: x = {zt(x)}.', 'Dividieren durch eine Dezimalzahl: Erweitere so, dass du durch eine ganze Zahl teilst.')
    a = R.choice([2, 3, 4, 5, 6, 8])
    b = R.choice([v for v in range(-12, 13) if v])
    c = R.choice([v for v in range(-20, 21) if (v - b) % a])
    x = Fr(c - b, a)
    return bruchluecke(f'Löse {lin(a, b)} = {zt(c)}. Gib x als Bruch an.', x,
                       f'| {sig(b)}: {lin(a, 0)} = {zt(c - b)}. | : {a}: x = {zt(c - b)}/{a}' + (f' = {fz(x)}.' if x.denominator != a else '.'),
                       'Die Lösung ist keine ganze Zahl. Kürze den Bruch am Ende.')


# ---------------- Variable auf beiden Seiten ----------------
def bs_gleichung(R, groß=12, neg=True, loesung=None):
    while True:
        a, c = R.sample([v for v in range(-groß, groß + 1) if v] if neg else list(range(1, groß + 1)), 2)
        x = loesung if loesung is not None else R.choice([v for v in range(-10, 13) if v])
        b = R.choice([v for v in range(-25, 26) if v])
        d = (a - c) * x + b
        if d and abs(d) <= 60 and d != b: return a, b, c, d, x


def g_beide_seiten(R, s):
    if s == 1:
        a, b, c, d, x = bs_gleichung(R, 8, neg=False)
        if a < c: a, c = c, a; d = (a - c) * x + b
        if not d: return g_beide_seiten(R, s)
        return Z(f'Löse {lin(a, b)} = {lin(c, d)}.', x, f'(({d}) - ({b})) / ({a} - {c})',
                 f'| {xsig(c)}: {lin(a - c, b)} = {zt(d)}. | {sig(b)}: {lin(a - c, 0)} = {zt(d - b)}. ' + (f'| : {a - c}: ' if a - c != 1 else '') + f'x = {zt(x)}.',
                 'Bringe zuerst die x-Glieder auf die Seite mit mehr x.')
    if s == 2:
        art = R.choice(['normal', 'normal', 'normal', 'schritt'])
        a, b, c, d, x = bs_gleichung(R, 12)
        if art == 'schritt':
            if c == 0: return g_beide_seiten(R, s)
            return A(R, f'Welche Gleichung entsteht aus {lin(a, b)} = {lin(c, d)} durch | {xsig(c)}?', f'{lin(a - c, b)} = {zt(d)}',
                     [f'{lin(a + c, b)} = {zt(d)}', f'{lin(a - c, b)} = {lin(-c, d) if c else zt(d)}', f'{lin(a, b)} = {zt(d)}'],
                     f'Rechts verschwindet {lin(c, 0)}. Links: {lin(a, 0)} {xsig(c)} = {lin(a - c, 0)}. Ergebnis: {lin(a - c, b)} = {zt(d)}.',
                     'Auf beiden Seiten dasselbe abziehen bzw. addieren.')
        return Z(f'Löse {lin(a, b)} = {lin(c, d)}.', x, f'(({d}) - ({b})) / (({a}) - ({c}))',
                 f'| {xsig(c)}: {lin(a - c, b)} = {zt(d)}. | {sig(b)}: {lin(a - c, 0)} = {zt(d - b)}. ' + (f'| : {kl(a - c)}: ' if a - c != 1 else '') + f'x = {zt(x)}.',
                 'Alle x-Glieder auf eine Seite, alle Zahlen auf die andere.')
    art = R.choice(['x_rechts', 'bruch', 'vier_glieder'])
    if art == 'x_rechts':
        c, a = sorted(R.sample(range(2, 12), 2))
        a, c = c, a  # links weniger x
        x = R.choice([v for v in range(-9, 12) if v])
        b = R.choice([v for v in range(-20, 21) if v])
        d = (a - c) * x + b
        return Z(f'Löse {lin(a, b)} = {lin(c, d)}.', x, f'(({d}) - ({b})) / (({a}) - ({c}))',
                 f'Rechts stehen mehr x. | {xsig(a)}: {zt(b)} = {lin(c - a, d)}. | {sig(d)}: {zt(b - d)} = {lin(c - a, 0)}. | : {c - a}: x = {zt(x)}.',
                 'Rechts stehen mehr x. Bringe die x-Glieder dorthin – dann bleibt der Faktor positiv.')
    if art == 'bruch':
        while True:
            a, c = R.sample(range(-9, 10), 2)
            if a - c not in (0, 1, -1) and a and c: break
        b = R.choice([v for v in range(-15, 16) if v])
        d = R.choice([v for v in range(-15, 16) if (v - b) % (a - c)])
        x = Fr(d - b, a - c)
        return bruchluecke(f'Löse {lin(a, b)} = {lin(c, d)}. Gib x als Bruch an.', x,
                           f'| {xsig(c)}: {lin(a - c, b)} = {zt(d)}. | {sig(b)}: {lin(a - c, 0)} = {zt(d - b)}. | : {kl(a - c)}: x = {fz(x)}.',
                           'Rechne wie immer. Am Ende teilst du durch eine Zahl, die nicht aufgeht.')
    a, b, c, d, x = bs_gleichung(R, 9)
    e, f = R.randint(1, 6), R.choice([v for v in range(-9, 10) if v])
    # a x + b + e x = c x + d + f  →  (a+e) x + b = c x + (d+f)
    d2 = (a + e - c) * x + b - f
    if a + e == c or not d2: return g_beide_seiten(R, s)
    links = f'{lin(a, b)} + {lin(e, 0)}'
    rechts = f'{lin(c, d2)} {"+" if f > 0 else "−"} {abs(f)}'
    return Z(f'Löse {links} = {rechts}.', x, f'(({d2}) + ({f}) - ({b})) / (({a}) + {e} - ({c}))',
             f'Erst jede Seite zusammenfassen: {lin(a + e, b)} = {lin(c, d2 + f)}. Dann | {xsig(c)}: {lin(a + e - c, b)} = {zt(d2 + f)}. '
             f'| {sig(b)}: {lin(a + e - c, 0)} = {zt(d2 + f - b)}. x = {zt(x)}.',
             'Fasse zuerst auf jeder Seite für sich zusammen.')


# ---------------- Klammern ----------------
def g_klammern(R, s):
    if s == 1:
        art = R.choice(['einfach', 'einfach', 'aufloesen'])
        a = R.randint(2, 9)
        b = R.choice([v for v in range(-12, 13) if v])
        x = R.choice([v for v in range(-10, 13) if v])
        c = a * (x + b)
        if art == 'aufloesen':
            return A(R, f'Wie lautet {kla(a, b)} ohne Klammer?', lin(a, a * b), [lin(a, b), lin(1, a * b), lin(a, -a * b)],
                     f'Die {a} wird mit jedem Summanden multipliziert: {a} · x {"+" if b > 0 else "−"} {a} · {abs(b)} = {lin(a, a * b)}.',
                     'Multipliziere den Faktor mit jedem Summanden in der Klammer.')
        return Z(f'Löse {kla(a, b)} = {zt(c)}.', x, f'{c} / {a} - ({b})',
                 f'Klammer auflösen: {lin(a, a * b)} = {zt(c)}. | {sig(a * b)}: {lin(a, 0)} = {zt(c - a * b)}. | : {a}: x = {zt(x)}. '
                 f'(Oder gleich | : {a}: {lin(1, b)} = {zt(c // a)}.)',
                 'Löse die Klammer auf – oder teile beide Seiten zuerst durch den Faktor vor der Klammer.')
    if s == 2:
        art = R.choice(['rechts_x', 'minus', 'minus', 'aufloesen_minus'])
        x = R.choice([v for v in range(-10, 13) if v])
        if art == 'rechts_x':
            a = R.randint(2, 7); b = R.choice([v for v in range(-9, 10) if v])
            c = R.choice([v for v in range(-6, 7) if v != a])
            d = (a - c) * x + a * b
            return Z(f'Löse {kla(a, b)} = {lin(c, d)}.', x, f'(({d}) - {a} * ({b})) / ({a} - ({c}))',
                     f'Klammer auflösen: {lin(a, a * b)} = {lin(c, d)}. | {xsig(c) if c else "− 0"}: {lin(a - c, a * b)} = {zt(d)}. | {sig(a * b)}: {lin(a - c, 0)} = {zt(d - a * b)}. x = {zt(x)}.',
                     'Erst die Klammer auflösen, dann x-Glieder und Zahlen sortieren.')
        if art == 'minus':
            p = R.randint(5, 30); b = R.choice([v for v in range(-9, 10) if v])
            c = p - (x + b)
            return Z(f'Löse {p} − {kla(1, b)} = {zt(c)}.', x, f'{p} - ({b}) - ({c})',
                     f'Minus vor der Klammer dreht die Vorzeichen: {p} − x {"−" if b > 0 else "+"} {abs(b)} = {zt(c)}, also {lin(-1, p - b)} = {zt(c)}. '
                     f'| {sig(p - b)}: −x = {zt(c - p + b)}. x = {zt(x)}.',
                     'Ein Minus vor der Klammer ändert alle Vorzeichen in der Klammer.')
        b = R.choice([v for v in range(-9, 10) if v]); a = R.randint(2, 6)
        return A(R, f'Wie lautet −{a}(x {"+" if b > 0 else "−"} {abs(b)}) ohne Klammer?', lin(-a, -a * b),
                 [lin(-a, a * b), lin(-a, b), lin(a, -a * b)],
                 f'−{a} mal jeden Summanden: −{a} · x = {lin(-a, 0)} und −{a} · {kl(b)} = {zt(-a * b)}. Zusammen: {lin(-a, -a * b)}.',
                 'Achte auf das Minus: Es wird mit beiden Summanden multipliziert.')
    art = R.choice(['zwei', 'zwei', 'beide'])
    x = R.choice([v for v in range(-9, 12) if v])
    if art == 'zwei':
        a, c = R.randint(2, 6), R.randint(2, 6)
        if a == c: return g_klammern(R, s)
        b, d = R.choice([v for v in range(-8, 9) if v]), R.choice([v for v in range(-8, 9) if v])
        e = a * (x + b) - c * (x + d)
        return Z(f'Löse {kla(a, b)} − {kla(c, d)} = {zt(e)}.', x, f'(({e}) - {a} * ({b}) + {c} * ({d})) / ({a} - {c})',
                 f'Auflösen: {lin(a, a * b)}{plus(lin(-c, -c * d))} = {zt(e)}. '
                 f'Zusammenfassen: {lin(a - c, a * b - c * d)} = {zt(e)}. Dann x = {zt(x)}.',
                 'Vorsicht beim Minus vor der zweiten Klammer: Beide Vorzeichen in ihr drehen sich um.')
    a, c = R.sample(range(2, 8), 2)
    b, d = R.choice([v for v in range(-8, 9) if v]), R.choice([v for v in range(-9, 10) if v])
    # a(x + b) = c(x + d) + f
    f = a * (x + b) - c * (x + d)
    if f == 0: return g_klammern(R, s)
    return Z(f'Löse {kla(a, b)} = {kla(c, d)} {"+" if f > 0 else "−"} {abs(f)}.', x, f'({c} * ({d}) + ({f}) - {a} * ({b})) / ({a} - {c})',
             f'Auflösen: {lin(a, a * b)} = {lin(c, c * d + f)}. | {xsig(c)}: {lin(a - c, a * b)} = {zt(c * d + f)}. | {sig(a * b)}: {lin(a - c, 0)} = {zt(c * d + f - a * b)}. x = {zt(x)}.',
             'Beide Klammern auflösen, rechts zusammenfassen, dann sortieren.')


# ---------------- Probe und Fehler ----------------
def g_probe(R, s):
    if s == 1:
        a, b, c, d, x = bs_gleichung(R, 8)
        n = x if R.random() < .5 else x + R.choice([-2, -1, 1, 2])
        li, re = a * n + b, c * n + d
        if n == x:
            return A(R, f'Ist x = {zt(n)} eine Lösung von {lin(a, b)} = {lin(c, d)}?', f'Ja: Beide Seiten ergeben {zt(li)}.',
                     [f'Nein: links {zt(li)}, rechts {zt(li + c)}.', f'Nein: links {zt(li - b)}, rechts {zt(re)}.'],
                     f'Links: {zt(a)} · {kl(n)} {"+" if b > 0 else "−"} {abs(b)} = {zt(li)}. Rechts: {zt(c)} · {kl(n)} {"+" if d > 0 else "−"} {abs(d)} = {zt(re)}. Gleich ✓',
                     'Setze die Zahl links und rechts getrennt ein.')
        return A(R, f'Ist x = {zt(n)} eine Lösung von {lin(a, b)} = {lin(c, d)}?', f'Nein: links {zt(li)}, rechts {zt(re)}.',
                 [f'Ja: Beide Seiten ergeben {zt(li)}.', f'Ja: Beide Seiten ergeben {zt(re)}.'],
                 f'Links: {zt(li)}, rechts: {zt(re)}. Verschieden, also keine Lösung. Die Lösung ist x = {zt(x)}.',
                 'Setze die Zahl links und rechts getrennt ein.')
    if s == 2:
        art = R.choice(['zeile', 'zeile', 'korrekt'])
        a, b, c, d, x = bs_gleichung(R, 9)
        k = a - c
        if k in (0, 1, -1): return g_probe(R, s)
        fehler = R.choice(['vorzeichen_x', 'vorzeichen_zahl', 'teilen'])
        z1 = f'{lin(k, b)} = {zt(d)}'
        z2 = f'{lin(k, 0)} = {zt(d - b)}'
        if fehler == 'vorzeichen_x':
            zeilen = [f'{lin(a + c, b)} = {zt(d)}', f'{lin(a + c, 0)} = {zt(d - b)}']
            wo, gr = 'Zeile 1', f'Statt {lin(a, 0)} {xsig(c)} = {lin(k, 0)} wurde {lin(a + c, 0)} gerechnet.'
            if a + c == 0: return g_probe(R, s)
            erg = Fr(d - b, a + c)
        elif fehler == 'vorzeichen_zahl':
            zeilen = [z1, f'{lin(k, 0)} = {zt(d + b)}']
            wo, gr = 'Zeile 2', f'| {sig(b)} heißt rechts {zt(d)} {sig(b)} = {zt(d - b)}, nicht {zt(d + b)}.'
            erg = Fr(d + b, k)
        else:
            zeilen = [z1, z2]
            wo, gr = 'Zeile 3', f'Bei {lin(k, 0)} = {zt(d - b)} muss durch {kl(k)} geteilt werden, nicht {"mit" } {kl(k)} multipliziert.'
            erg = Fr((d - b) * k)
        erg_t = zt(erg) if endlich(erg) else fz(erg)
        weg = ' → '.join(f'({i + 1}) {z}' for i, z in enumerate(zeilen + [f'x = {erg_t}']))
        if art == 'korrekt':
            return Z(f'In dieser Rechnung zu {lin(a, b)} = {lin(c, d)} steckt ein Fehler: {weg}. Wie heißt die richtige Lösung?', x, f'(({d}) - ({b})) / ({k})',
                     f'{wo} ist falsch. {gr} Richtig: {z1} → {z2} → x = {zt(x)}.', 'Mache die Probe mit dem Ergebnis und prüfe jede Zeile.')
        return A(R, f'Gleichung {lin(a, b)} = {lin(c, d)}. Rechnung: {weg}. In welcher Zeile steckt der Fehler?', wo,
                 [z for z in ['Zeile 1', 'Zeile 2', 'Zeile 3', 'Kein Fehler'] if z != wo][:3],
                 f'{gr} Richtig: {z1} → {z2} → x = {zt(x)}.', 'Prüfe jede Umformung einzeln. Was wurde auf beiden Seiten gemacht?')
    art = R.choice(['null', 'quadrat', 'aussage'])
    if art == 'null':
        a, b, c = R.randint(2, 6), R.randint(1, 9), R.randint(10, 40)
        return A(R, f'Jemand multipliziert {lin(a, b)} = {c} auf beiden Seiten mit 0 und erhält 0 = 0. Er folgert: „Jede Zahl ist eine Lösung.“ Stimmt das?',
                 'Nein: Mal 0 ist keine Äquivalenzumformung.', ['Ja: 0 = 0 ist immer wahr.', 'Ja: Auf beiden Seiten dasselbe ist erlaubt.', 'Nein: Es kommt 0 = c heraus.'],
                 f'Mit 0 multiplizieren macht aus jeder Gleichung 0 = 0 – dabei geht die Information verloren. Darum ist nur Multiplizieren mit Zahlen ≠ 0 erlaubt. '
                 f'Die Gleichung hat genau eine Lösung: x = {zt(Fr(c - b, a))}.', 'Welche Zahl ist beim Multiplizieren und Dividieren ausgeschlossen – und warum?')
    if art == 'quadrat':
        x = R.choice([v for v in range(-9, 10) if v not in (0,)])
        a, b, c, d, _ = bs_gleichung(R, 8, loesung=x)
        L_, R_ = a * x + b, c * x + d
        return A(R, f'Die Probe für x = {zt(x)} bei {lin(a, b)} = {lin(c, d)} wird so geschrieben: „{lin(a, b)} = {lin(c, d)} | x = {zt(x)} → {zt(L_)} = {zt(R_)} ✓“. '
                    'Welche Aussage stimmt?', f'Die Lösung stimmt, weil beide Seiten {zt(L_)} ergeben.',
                 [f'Die Lösung stimmt nicht, weil {zt(L_)} ≠ {zt(x)}.', 'Man darf bei der Probe nicht einsetzen.', f'Die Lösung ist {zt(L_)}.'],
                 f'Bei der Probe vergleicht man die Werte beider Seiten, nicht mit x. Beide Seiten ergeben {zt(L_)} – also stimmt x = {zt(x)}.',
                 'Was wird bei der Probe miteinander verglichen?')
    a, b = R.randint(2, 8), R.choice([v for v in range(-9, 10) if v])
    x = R.choice([v for v in range(-6, 9) if v])
    c = a * x + b
    return A(R, f'Jemand rechnet bei {lin(a, b)} = {zt(c)}: „| : {a} → {lin(1, b)} = {zt(Fr(c, a)) if endlich(Fr(c, a)) else fz(Fr(c, a))}“. Was ist falsch?',
             f'Beim Teilen muss jeder Summand links geteilt werden, also auch {zt(b)}.',
             ['Nichts, die Umformung stimmt.', 'Man darf nie durch eine Zahl teilen.', f'Rechts muss mit {a} multipliziert werden.'],
             f'| : {a} gilt für die ganze linke Seite: x {"+" if b > 0 else "−"} {zt(Fr(abs(b), a)) if endlich(Fr(abs(b), a)) else f"{abs(b)}/{a}"} = … . Besser zuerst | {sig(b)}, dann | : {a}: x = {zt(x)}.',
             'Wird beim Teilen jeder Teil der linken Seite geteilt?')


# ---------------- Sonderfälle ----------------
OPT3 = ['genau eine Lösung', 'keine Lösung', 'unendlich viele Lösungen']


def g_sonderfaelle(R, s):
    if s == 1:
        a = R.randint(2, 9)
        b, d = R.sample([v for v in range(-15, 16) if v], 2)
        art = R.choice(['keine', 'alle', 'eine'])
        if art == 'keine':
            return A(R, f'Wie viele Lösungen hat {lin(a, b)} = {lin(a, d)}?', OPT3[1], [OPT3[0], OPT3[2]],
                     f'| − {lin(a, 0)}: {zt(b)} = {zt(d)} – falsch. Also L = {{ }}.', 'Was passiert, wenn du die x-Glieder auf eine Seite bringst?')
        if art == 'alle':
            return A(R, f'Wie viele Lösungen hat {kla(a, b)} = {lin(a, a * b)}?',
                     OPT3[2], [OPT3[0], OPT3[1]],
                     f'Klammer auflösen: {lin(a, a * b)} = {lin(a, a * b)}. | − {lin(a, 0)}: {zt(a * b)} = {zt(a * b)} – wahr für jedes x. L = ℚ.',
                     'Löse die Klammer auf und vergleiche beide Seiten.')
        c = R.choice([v for v in range(1, 10) if v != a])
        return A(R, f'Wie viele Lösungen hat {lin(a, b)} = {lin(c, d)}?', OPT3[0], [OPT3[1], OPT3[2]],
                 f'Die Faktoren vor x sind verschieden ({a} und {c}). Nach | {xsig(c)} bleibt {lin(a - c, b)} = {zt(d)} – genau eine Lösung: x = {zt(Fr(d - b, a - c))}.',
                 'Vergleiche die Zahlen vor dem x auf beiden Seiten.')
    if s == 2:
        art = R.choice(['menge_keine', 'menge_alle', 'versteckt'])
        a = R.randint(2, 6)
        b = R.choice([v for v in range(-9, 10) if v])
        if art == 'menge_keine':
            e = R.choice([v for v in range(-9, 10) if v and v != a * b])
            t = f'{kla(a, b)} = {lin(a, e)}'
            return A(R, f'Bestimme die Lösungsmenge von {t}.', L0, [LQ, f'L = {{{zt(e - a * b)}}}', 'L = {0}'],
                     f'{lin(a, a * b)} = {lin(a, e)}. | − {lin(a, 0)}: {zt(a * b)} = {zt(e)} – falsch. L = {{ }}.',
                     'Löse die Klammer auf und bringe die x-Glieder zusammen.')
        if art == 'menge_alle':
            c = R.randint(1, 4)
            t = f'{kla(a, b)} − {lin(c, 0)} = {lin(a - c, a * b)}' if a > c else f'{kla(a, b)} = {lin(a, a * b)}'
            return A(R, f'Bestimme die Lösungsmenge von {t}.', LQ, [L0, f'L = {{{zt(a * b)}}}', 'L = {0}'],
                     f'Nach Auflösen und Zusammenfassen stehen links und rechts dieselben Terme. Übrig bleibt eine wahre Aussage – jede Zahl ist Lösung: L = ℚ.',
                     'Fasse beide Seiten so weit wie möglich zusammen.')
        c = R.randint(1, 5)
        d = R.choice([v for v in range(-9, 10) if v])
        # c x + a x + b = (a + c) x + d
        wahr = R.random() < .5
        if wahr: d = b
        return A(R, f'Wie viele Lösungen hat {lin(c, b)} + {lin(a, 0)} = {lin(a + c, d)}?', OPT3[2] if wahr else OPT3[1],
                 [OPT3[0], OPT3[1] if wahr else OPT3[2]],
                 f'Links zusammenfassen: {lin(a + c, b)}. Nach | − {lin(a + c, 0)}: {zt(b)} = {zt(d)} – {"wahr, also L = ℚ" if wahr else "falsch, also L = { }"}.',
                 'Fasse zuerst die linke Seite zusammen.')
    art = R.choice(['ergaenzen_alle', 'ergaenzen_keine', 'deuten'])
    a, b = R.randint(2, 9), R.choice([v for v in range(-12, 13) if v])
    if art == 'ergaenzen_alle':
        k = R.randint(2, 5)
        return Z(f'Welche Zahl muss für □ stehen, damit {kla(k, b)} = {lin(k, 0)} + □ unendlich viele Lösungen hat?', k * b, f'{k} * ({b})',
                 f'Links aufgelöst: {lin(k, k * b)}. Rechts muss dasselbe stehen, also □ = {zt(k * b)}. Dann gilt die Gleichung für jedes x.',
                 'Löse links die Klammer auf. Was muss rechts stehen, damit beide Seiten gleich sind?')
    if art == 'ergaenzen_keine':
        if b == 1: b = 2
        return Z(f'Welche Zahl muss für □ stehen, damit {lin(a, b)} = □ · x + 1 keine Lösung hat?', a, f'{a}',
                 f'Keine Lösung gibt es, wenn x beim Umformen wegfällt und eine falsche Aussage bleibt. x fällt weg, wenn rechts auch {lin(a, 0)} steht: □ = {a}. Dann bleibt {zt(b)} = 1 – falsch.',
                 'Wann fällt x beim Umformen weg?')
    g, p1, p2 = R.choice([(3, 2, 2), (5, 3, 3), (4, 1, 1)])
    g2 = g + R.randint(1, 4)
    return A(R, f'Tarif A: {g} € Grundgebühr und {p1} € pro Stunde. Tarif B: {g2} € Grundgebühr und {p2} € pro Stunde. Die Gleichung {lin(p1, g)} = {lin(p2, g2)} führt zu {g} = {g2}. Was bedeutet das?',
             'Die Tarife sind nie gleich teuer; A ist immer billiger.', ['Die Tarife sind nach 0 Stunden gleich teuer.', 'Die Tarife sind immer gleich teuer.', f'Nach {g2 - g} Stunden sind sie gleich teuer.'],
             f'{g} = {g2} ist falsch, also gibt es keine Lösung. Weil der Stundenpreis gleich ist, bleibt A immer um {g2 - g} € billiger.',
             'Ist die Aussage wahr oder falsch? Was heißt das für die Tarife?')


# ---------------- Sachaufgaben ----------------
def g_sach(R, s):
    if s == 1:
        art = R.choice(['folge', 'umfang', 'alter', 'gleichung'])
        if art == 'folge':
            n = R.choice([2, 3])
            x = R.randint(5, 60)
            S = n * x + (1 if n == 2 else 3)
            return Z(f'{n} aufeinanderfolgende natürliche Zahlen ergeben zusammen {S}. Wie heißt die kleinste?', x, f'({S} - {1 if n == 2 else 3}) // {n}',
                     f'x + (x + 1){" + (x + 2)" if n == 3 else ""} = {S} → {n}x + {1 if n == 2 else 3} = {S} → x = {x}.',
                     'Nenne die kleinste Zahl x. Wie heißen dann die nächsten?')
        if art == 'umfang':
            x = R.randint(3, 25); d = R.randint(2, 10)
            U = 2 * x + 2 * (x + d)
            return Z(f'Ein Rechteck ist {d} cm länger als breit. Sein Umfang beträgt {U} cm. Wie breit ist es?', x, f'({U} - 2 * {d}) // 4',
                     f'Breite x, Länge x + {d}. 2x + 2(x + {d}) = {U} → 4x + {2 * d} = {U} → 4x = {U - 2 * d} → x = {x} cm.',
                     'Breite x. Wie drückst du die Länge mit x aus?', einheit='cm')
        if art == 'alter':
            x = R.randint(6, 14); k = R.choice([3, 4]); d = R.choice([0, 2, 4])
            S = x + k * x + d
            if not 26 <= k * x + d <= 50: return g_sach(R, s)
            satz = f'Eine Mutter ist {k}-mal so alt wie ihr Sohn.' if d == 0 else f'Eine Mutter ist {d} Jahre älter als das {k}-Fache des Alters ihres Sohnes.'
            return Z(f'{satz} Zusammen sind sie {S} Jahre alt. Wie alt ist der Sohn?',
                     x, f'({S} - {d}) // {k + 1}',
                     f'Sohn x, Mutter {lin(k, d)}. x + {lin(k, d)} = {S} → {lin(k + 1, d)} = {S} → x = {x}.',
                     'Alter des Sohnes = x. Drücke das Alter der Mutter mit x aus.', einheit='Jahre')
        a, x = R.randint(3, 8), R.randint(4, 15)
        b = R.randint(5, 20)
        return A(R, f'Ein Fitnessstudio kostet {b} € Aufnahmegebühr und {a} € pro Woche. Nach wie vielen Wochen hat man insgesamt {b + a * x} € bezahlt? Welche Gleichung passt?',
                 f'{lin(a, b)} = {b + a * x}', [f'{lin(b, a)} = {b + a * x}', f'{a}(x + {b}) = {b + a * x}', f'{lin(a + b, 0)} = {b + a * x}'],
                 f'Die Gebühr {b} € zahlt man einmal, die {a} € jede Woche: {lin(a, b)} = {b + a * x}. Lösung: x = {x} Wochen.',
                 'Was zahlt man einmal, was jede Woche?')
    if s == 2:
        art = R.choice(['tarif', 'sparen', 'sparen', 'gleichung2'])
        if art == 'tarif':
            g, p1, p2 = R.randint(5, 20), R.randint(1, 3), R.randint(4, 6)
            if g % (p2 - p1): return g_sach(R, s)
            x = g // (p2 - p1)
            return Z(f'Tarif A: {g} € Grundgebühr und {p1} € pro GB. Tarif B: keine Grundgebühr, {p2} € pro GB. Bei wie vielen GB kosten beide gleich viel?', x, f'{g} // ({p2} - {p1})',
                     f'{lin(p1, g)} = {lin(p2, 0)} | − {lin(p1, 0)} → {g} = {lin(p2 - p1, 0)} → x = {x} GB. Dann kosten beide {p2 * x} €.',
                     'Stelle für jeden Tarif einen Term auf und setze sie gleich.', einheit='GB')
        if art == 'sparen':
            a, b, d, x = R.randint(10, 60), R.randint(2, 6), R.randint(1, 5), R.randint(3, 12)
            c = a + (b + d) * x
            if (c - a) % (b + d): return g_sach(R, s)
            x = (c - a) // (b + d)
            return Z(f'Lena hat {a} € und spart jede Woche {b} € dazu. Tom hat {c} € und gibt jede Woche {d} € aus. Nach wie vielen Wochen haben beide gleich viel?', x,
                     f'({c} - {a}) // ({b} + {d})', f'{lin(b, a)} = {zt(c)} − {lin(d, 0)} | + {lin(d, 0)} − {a} → {lin(b + d, 0)} = {c - a} → x = {x} Wochen. Beide haben dann {a + b * x} €.',
                     'Lena: Startbetrag plus Sparen. Tom: Startbetrag minus Ausgaben.', einheit='Wochen')
        x = R.randint(10, 40); d = R.randint(3, 15)
        S = x + (x + d) + 2 * x
        return Z(f'Drei Kinder sammeln Pfandflaschen. Das zweite sammelt {d} mehr als das erste, das dritte doppelt so viele wie das erste. Zusammen sind es {S} Flaschen. Wie viele sammelt das erste?',
                 x, f'({S} - {d}) // 4', f'x + (x + {d}) + 2x = {S} → 4x + {d} = {S} → 4x = {S - d} → x = {x}.',
                 'Das erste Kind sammelt x Flaschen. Drücke die anderen mit x aus.')
    art = R.choice(['deuten', 'deuten', 'rueckwaerts', 'tarif_ab'])
    if art == 'deuten':
        S = R.choice([v for v in range(30, 120) if (v - 1) % 2 == 1])
        x = Fr(S - 1, 2)
        return A(R, f'„Zwei aufeinanderfolgende natürliche Zahlen ergeben zusammen {S}.“ Die Gleichung x + (x + 1) = {S} liefert x = {zt(x)}. Was folgt daraus?',
                 'Es gibt keine solchen Zahlen, weil x keine natürliche Zahl ist.',
                 [f'Die Zahlen sind {zt(x)} und {zt(x + 1)}.', f'Die Zahlen sind {int(x)} und {int(x) + 1}.', 'Man hat sich verrechnet.'],
                 f'Die Rechnung stimmt ({zt(x)} + {zt(x + 1)} = {S}), aber {zt(x)} ist keine natürliche Zahl. Zwei aufeinanderfolgende natürliche Zahlen ergeben immer eine ungerade Summe – {S} ist gerade.',
                 'Passt die Lösung zur Frage? Welche Zahlen sind erlaubt?')
    if art == 'rueckwaerts':
        x = R.randint(20, 80) * 2
        a = R.randint(10, 30)
        rest = x // 2 - a
        if rest <= 0: return g_sach(R, s)
        return Z(f'Jemand gibt die Hälfte des Geldes für ein Spiel aus und dann noch {a} € für Essen. Übrig bleiben {rest} €. Wie viel Geld war es am Anfang?', x, f'({rest} + {a}) * 2',
                 f'x − x/2 − {a} = {rest} → x/2 − {a} = {rest} → x/2 = {rest + a} → x = {x} €.', 'Startbetrag x. Was wird abgezogen?', einheit='€')
    g1, p1 = R.randint(10, 30), R.randint(2, 4)
    g2, p2 = R.randint(0, 8), R.randint(p1 + 1, p1 + 4)
    if (g1 - g2) % (p2 - p1) or g1 <= g2: return g_sach(R, s)
    x = (g1 - g2) // (p2 - p1)
    return A(R, f'Tarif A: {g1} € und {p1} € pro Stunde. Tarif B: {g2} € und {p2} € pro Stunde. Die Gleichung ergibt x = {x}. Welcher Tarif ist bei {x + 3} Stunden günstiger?',
             'Tarif A', ['Tarif B', 'Beide gleich teuer'],
             f'Bei {x} Stunden sind beide gleich teuer. Danach wächst B schneller ({p2} € statt {p1} € pro Stunde). Bei {x + 3} h: A {g1 + p1 * (x + 3)} €, B {g2 + p2 * (x + 3)} €.',
             'Was passiert nach dem Schnittpunkt? Welcher Tarif hat den höheren Stundenpreis?')


import re  # noqa: E402


def _glatt(f):
    def g(R, s):
        a = f(R, s)
        a['w'] = re.sub(r'(?<![\d/])x = (\S+)\. x = \1\.', r'x = \1.', a['w'])
        a['w'] = re.sub(r'(−?\d+)x = (\S+)\. x = ', lambda m: f'{m.group(1)}x = {m.group(2)}. | : {"(" + m.group(1) + ")" if m.group(1).startswith("−") else m.group(1)}: x = ', a['w'])
        return a
    return g


GEN = {'waage': g_waage, 'beide_seiten': g_beide_seiten, 'klammern': g_klammern, 'probe': g_probe, 'sonderfaelle': g_sonderfaelle, 'sach': g_sach}
GEN = {k: _glatt(v) for k, v in GEN.items()}
TEIL = {'waage': 'umformen', 'beide_seiten': 'umformen', 'klammern': 'umformen', 'probe': 'pruefen', 'sonderfaelle': 'pruefen', 'sach': 'anwenden',
        '_texte': [('umformen', 'Lineare Gleichungen durch Äquivalenzumformungen lösen'), ('pruefen', 'Lösungen prüfen, Fehler finden, Sonderfälle erkennen'),
                   ('anwenden', 'Gleichungen zu Sachsituationen aufstellen, lösen und deuten')]}

# Verständliche Fassung (Runde 7, Maßstab inhalte/README.md „Verständliche Erklärungen“):
# Alltagssituation zuerst (einstieg), jedes neue Wort erklärt (woerter), Beispiel in kleinen Schritten, Merksatz am Ende (regel).
# Durchgehende Situationen: Balkenwaage mit Dosen, Obsttüten, Handytarife.
KLAR = {
 'waage': {
  'einstieg': 'Auf einer Balkenwaage liegen links 3 gleich schwere Dosen und ein 5-kg-Gewicht, rechts liegen 20 kg. Die Waage ist im Gleichgewicht. Wie schwer ist eine Dose? Nimmst du auf beiden Seiten dasselbe weg, bleibt die Waage im Gleichgewicht – bis am Ende eine einzelne Dose allein dasteht. So ein Schritt heißt ⟦Äquivalenzumformung⟧.',
  'woerter': [['Term', 'eine Rechnung aus Zahlen, Buchstaben und Rechenzeichen, zum Beispiel 3x + 5'], ['Gleichung', 'zwei Terme mit einem Gleichheitszeichen dazwischen – wie eine Waage im Gleichgewicht'], ['x', 'hier das Gewicht einer Dose in kg, das wir noch nicht kennen (die Variable)'],
              ['3x', '3 · x, also drei Dosen'], ['Lösung', 'die Zahl für x, bei der beide Seiten gleich viel ergeben'],
              ['Äquivalenzumformung', 'auf beiden Seiten dasselbe tun, sodass das Gleichgewicht bleibt'], ['| − 5', 'Notiz hinter dem Strich: „auf beiden Seiten 5 abziehen“'],
              ['Probe', 'die Lösung zur Kontrolle in die Gleichung einsetzen']],
  'schritte': ['Die Waage als Gleichung: 3x + 5 = 20. Gesucht ist das Gewicht x einer Dose.',
               'Nimm auf beiden Seiten 5 kg weg (| − 5), damit links nur noch die Dosen liegen: 3x = 15.',
               'Drei Dosen wiegen also 15 kg. Teile beide Seiten durch 3 (| : 3): x = 15 : 3.',
               'Eine Dose wiegt ⟦x = 5⟧ kg.'],
  'regel': 'So löst du eine Gleichung: Tu auf ⟦beiden Seiten dasselbe⟧ – dieselbe Zahl addieren oder subtrahieren, mit derselben Zahl (nicht 0) multiplizieren oder durch sie dividieren. Das ist eine ⟦Äquivalenzumformung⟧; schreib sie hinter einen Strich, zum Beispiel | − 5.',
  'fehler': 'Nur auf einer Seite umformen: Aus 3x + 5 = 20 wird mit | − 5 nicht 3x = 25 und auch nicht 3x = 20. Nimmt man links 5 kg herunter und rechts nichts, kippt die Waage. Rechts muss man ebenfalls 5 ⟦abziehen⟧: 3x = 15.'},
 'beide_seiten': {
  'einstieg': 'Jetzt liegen auf beiden Seiten der Waage Dosen: links 5 Dosen und 3 kg, rechts 2 Dosen und 15 kg. Nimm auf beiden Seiten 2 Dosen weg – die Waage bleibt im Gleichgewicht, und rechts liegen keine Dosen mehr. So bringst du die ⟦Variable auf eine Seite⟧.',
  'woerter': [['x-Glied', 'ein Teil mit x, zum Beispiel 5x oder 2x (Dosen)'], ['Zahlglied', 'ein Teil ohne x, zum Beispiel 3 oder 15 (Gewichte)'],
              ['| − 2x', 'auf beiden Seiten 2x abziehen, also 2 Dosen wegnehmen']],
  'schritte': ['Die Gleichung ist 5x + 3 = 2x + 15.',
               'Nimm auf beiden Seiten 2 Dosen weg (| − 2x): Links bleiben 5x − 2x = 3x, rechts verschwindet das x. Es bleibt 3x + 3 = 15.',
               'Nimm auf beiden Seiten 3 kg weg (| − 3): 3x = 12.',
               'Teile beide Seiten durch 3 (| : 3): ⟦x = 4⟧.'],
  'regel': 'So löst du, wenn x auf beiden Seiten steht: Bring zuerst alle ⟦x-Glieder auf eine Seite⟧ (am besten dorthin, wo mehr x stehen) und alle ⟦Zahlglieder auf die andere⟧. An der Waage heißt das: auf beiden Seiten gleich viele Dosen wegnehmen.',
  'fehler': 'Aus 5x + 3 = 2x + 15 wird mit | − 2x nicht 7x + 3 = 15. Rechts werden 2 Dosen ⟦weggenommen⟧, also links auch: 5x − 2x = 3x. Wer links 2 Dosen dazulegt, bringt die Waage aus dem Gleichgewicht.'},
 'klammern': {
  'einstieg': 'In drei Tüten liegen je ein paar Äpfel – wie viele, weiß man nicht – und je 2 Birnen. In allen drei Tüten zusammen sind also 3-mal so viele Äpfel und 3 · 2 = 6 Birnen. Mit einer Klammer schreibt man das kurz als 3(x + 2). Um damit zu rechnen, muss man die ⟦Klammer auflösen⟧.',
  'woerter': [['3(x + 2)', '3 · (x + 2): drei Tüten mit je x Äpfeln und 2 Birnen'], ['Klammer auflösen', 'die Zahl vor der Klammer mit jedem Teil in der Klammer malnehmen: 3(x + 2) = 3x + 6'],
              ['Summand', 'ein Teil einer Summe, zum Beispiel x und 2 in x + 2'], ['−(x + 3)', 'Minus vor der Klammer: alle Vorzeichen in der Klammer drehen sich um, also −x − 3']],
  'schritte': ['Die Gleichung ist 3(x + 2) = 2x + 11.',
               'Löse die Klammer auf: 3 mal x und 3 mal 2. Das ergibt 3x + 6 = 2x + 11.',
               'Nimm auf beiden Seiten 2x weg (| − 2x): x + 6 = 11.',
               'Nimm auf beiden Seiten 6 weg (| − 6): ⟦x = 5⟧.'],
  'regel': 'So löst du Gleichungen mit Klammern: Löse zuerst die ⟦Klammern auf⟧ – die Zahl vor der Klammer wird mit ⟦jedem⟧ Summanden malgenommen. Ein ⟦Minus vor der Klammer⟧ dreht alle Vorzeichen in der Klammer um. Dann fasst du zusammen und löst wie gewohnt.',
  'fehler': '3(x + 2) ist nicht 3x + 2. In jeder der drei Tüten liegen 2 Birnen, zusammen also 6. Ebenso ist −(x + 3) nicht −x + 3. Das Minus gilt für die ⟦ganze⟧ Klammer: −(x + 3) = −x − 3.'},
 'probe': {
  'einstieg': 'An der Kasse rechnet die Kassiererin dir dein Wechselgeld heraus, und du zählst kurz nach, ob es stimmt. Bei Gleichungen gibt es auch so eine Kontrolle: Du setzt deine Lösung in die Aufgabe ein und prüfst, ob beide Seiten gleich viel ergeben. Das ist die ⟦Probe⟧.',
  'woerter': [['ursprüngliche Gleichung', 'die Gleichung, wie sie in der Aufgabe stand – vor allen Umformungen'], ['≈', '„ungefähr gleich“, wenn eine Zahl gerundet ist'], ['1/3', 'ein Drittel']],
  'schritte': ['Jemand löst 4x − 7 = x + 8 so: Erst 3x − 7 = 8, dann 3x = 1, also x = 1/3.',
               'Probe in der ursprünglichen Gleichung: Links ergibt 4 · 1/3 − 7 ≈ −5,7, rechts 1/3 + 8 ≈ 8,3. Die Seiten sind verschieden, die Lösung ist also falsch.',
               'Suche den Fehler Zeile für Zeile: Von 3x − 7 = 8 kommt man mit | + 7 auf 3x = 15, nicht auf 3x = 1.',
               'Richtig ist ⟦x = 5⟧. Probe: links 4 · 5 − 7 = 13, rechts 5 + 8 = 13. ✓'],
  'regel': 'So machst du die ⟦Probe⟧: Setze die Lösung in die ⟦ursprüngliche⟧ Gleichung ein und rechne beide Seiten ⟦getrennt⟧ aus. Sind sie verschieden, suchst du den Fehler Zeile für Zeile.',
  'fehler': 'Die Probe in einer umgeformten Zeile statt in der ursprünglichen Gleichung machen: Ist schon die Umformung falsch, passt die Probe dort trotzdem – der Fehler bleibt ⟦unentdeckt⟧. Das ist, als würdest du das Wechselgeld mit einer schon falsch abgeschriebenen Rechnung vergleichen.'},
 'sonderfaelle': {
  'einstieg': 'Zwei Handytarife kosten beide 2 € pro Gigabyte. Der eine hat 3 € Grundgebühr, der andere 5 €. Ab wie vielen Gigabyte sind sie gleich teuer? Nie – der zweite ist immer 2 € teurer. Manche Gleichungen haben ⟦keine Lösung⟧, andere sogar ⟦unendlich viele⟧.',
  'woerter': [['GB', 'Gigabyte, eine Menge an Internet-Daten'], ['Lösungsmenge L', 'alle Zahlen, die die Gleichung erfüllen'], ['L = { }', 'leere Menge: keine Zahl passt'],
              ['ℚ', 'die rationalen Zahlen: alle Brüche und Dezimalzahlen, positiv und negativ'], ['L = ℚ', 'jede dieser Zahlen passt'],
              ['Aussage', 'ein Satz wie „3 = 5“, der wahr oder falsch ist']],
  'schritte': ['Die Tarife als Gleichung: 2x + 3 = 2x + 5. Nimm auf beiden Seiten 2x weg (| − 2x).',
               'Es bleibt 3 = 5. Das x ist ganz verschwunden, und 3 = 5 ist falsch.',
               'Die Tarife kosten also ⟦nie⟧ gleich viel: L = { }.',
               'Anders bei 2(x + 3) = 2x + 6: Klammer auflösen ergibt 2x + 6 = 2x + 6, nach | − 2x bleibt 6 = 6. Das ist wahr, egal welches x: ⟦L = ℚ⟧.'],
  'regel': 'So erkennst du Sonderfälle: Fällt x beim Umformen ganz weg, schau auf die übrig gebliebene Aussage. Ist sie ⟦falsch⟧ (wie 3 = 5), gibt es ⟦keine Lösung⟧: L = { }. Ist sie ⟦wahr⟧ (wie 6 = 6), ist ⟦jede Zahl⟧ eine Lösung: L = ℚ.',
  'fehler': 'Aus 3 = 5 auf „x = 0“ schließen oder aus 6 = 6 auf „x = 6“ passt nicht: Bei den beiden Handytarifen gibt es keine Datenmenge, bei der sie gleich viel kosten. Wenn x weg ist, entscheidet nur, ob die Aussage ⟦wahr oder falsch⟧ ist.'},
 'sach': {
  'einstieg': 'Tarif A kostet 10 € Grundgebühr und 2 € pro Gigabyte, Tarif B nur 4 € pro Gigabyte ohne Grundgebühr. Bei wenig Daten ist B günstiger, bei viel Daten A. Wo genau liegt die Grenze? Solche Fragen aus dem Alltag löst man mit einer Gleichung – das ist eine ⟦Sachaufgabe⟧.',
  'woerter': [['Sachaufgabe', 'eine Aufgabe aus dem Alltag, die man mit einer Gleichung löst'], ['Variable festlegen', 'aufschreiben, wofür x steht, zum Beispiel x = Anzahl der GB'],
              ['sinnvoll', 'passt zur Situation: keine halben Personen, keine negativen Längen'], ['aufeinanderfolgende Zahlen', 'ganze Zahlen direkt hintereinander, zum Beispiel 15 und 16']],
  'schritte': ['Lege die Variable fest: x ist die Anzahl der Gigabyte.',
               'Stelle für beide Tarife einen Term auf und setze sie gleich: 10 + 2x = 4x.',
               'Löse: Auf beiden Seiten 2x weg (| − 2x) ergibt 10 = 2x. Beide Seiten durch 2 (| : 2) ergibt x = 5.',
               'Antwort: Bei ⟦5 GB⟧ kosten beide 20 €. Darunter ist B günstiger, darüber A.'],
  'regel': 'So löst du eine Sachaufgabe: ⟦1. Variable festlegen⟧ (x = …), ⟦2. Gleichung aufstellen⟧, ⟦3. lösen⟧, ⟦4. Antwort im Sachzusammenhang⟧ geben – und prüfen, ob die Lösung ⟦sinnvoll⟧ ist.',
  'fehler': '„Zwei aufeinanderfolgende Zahlen ergeben zusammen 31“ ist nicht x + x = 31 – dann wäre x = 15,5, und es gäbe keine zwei ganzen Zahlen. Die zweite Zahl ist um eins größer, also ⟦x + 1⟧: x + (x + 1) = 31 ergibt x = 15; die Zahlen sind 15 und 16.'},
}
for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl7.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl7 import mit_umbau  # noqa: E402


def waage_kipp(links, rechts):
    """Gekippte Balkenwaage (links leichter, steigt hoch) – für den Fehler „nur auf einer Seite umgeformt“."""
    return {'typ': 'figur', 'label': f'Waage nicht mehr im Gleichgewicht: links {links}, rechts {rechts}',
            'punkte': {'_A': [1.5, 2.7], '_B': [8.5, 1.3], '_S': [5, 2], '_F1': [4, 0], '_F2': [6, 0],
                       '_L1': [-0.5, 3.3], '_L2': [3.5, 3.3], '_R1': [6.5, 1.9], '_R2': [10.5, 1.9],
                       '_LA': [1.5, 3.3], '_RA': [8.5, 1.9]},
            'flaeche': ['_S', '_F1', '_F2'],
            'linien': [['_A', '_B'], ['_A', '_LA'], ['_B', '_RA'], ['_L1', '_L2', links], ['_R1', '_R2', rechts]]}


def _tarife(graphen, punkte=None, x=(0, 8), y=(0, 30)):
    b = {'typ': 'koordinaten', 'x': list(x), 'y': list(y), 'graphen': graphen, 'name_x': 'GB', 'name_y': '€', 'schritt_y': 5}
    if punkte: b['punkte'] = punkte
    return b


_AB_PAR = [{'art': 'linear', 'm': 2, 't': 3, 'name': '3 €'}, {'art': 'linear', 'm': 2, 't': 5, 'name': '5 €'}]

UMBAU = {
 'waage': {
  'einstieg': 'Auf einer Balkenwaage liegen links 3 gleiche Dosen und 5 kg, rechts 20 kg. Die Waage ist im Gleichgewicht. Wie schwer ist eine Dose? Man nimmt auf beiden Seiten dasselbe weg: eine ⟦Äquivalenzumformung⟧.',
  'woerter': [['Gleichung', 'zwei Seiten mit Gleichheitszeichen – wie eine Waage im Gleichgewicht'], ['x', 'das unbekannte Gewicht einer Dose'],
              ['Äquivalenzumformung', 'auf beiden Seiten dasselbe tun']],
  'bild': waage('3x + 5', '20'),
  'schritte': [{'text': 'Als Gleichung: 3x + 5 = 20. Gesucht ist x.'},
               {'text': 'Auf beiden Seiten 5 kg wegnehmen: 3x = 15.', 'bild': waage('3x', '15')},
               {'text': 'Beide Seiten durch 3 teilen: ⟦x = 5⟧. Eine Dose wiegt 5 kg.', 'bild': waage('x', '5')},
               {'text': 'Probe: 3 · 5 + 5 = 20. ✓'}],
  'fehler': 'Nimmt man nur links 5 kg weg, kippt die Waage. Aus 3x + 5 = 20 wird nicht 3x = 20, sondern ⟦3x = 15⟧.',
  'fehler_bild': waage_kipp('3x', '20'),
  'regel': 'Tu auf ⟦beiden Seiten dasselbe⟧. So bleibt die Gleichung im Gleichgewicht, bis x allein steht.'},
 'beide_seiten': {
  'einstieg': 'Jetzt liegen auf beiden Seiten Dosen. Links: 5 Dosen und 3 kg. Rechts: 2 Dosen und 15 kg. Nimm auf beiden Seiten 2 Dosen weg. So bringst du die ⟦Variable auf eine Seite⟧.',
  'woerter': [['Variable', 'der Buchstabe x für das unbekannte Gewicht'], ['x-Glied', 'ein Teil mit x, zum Beispiel 5x']],
  'bild': waage('5x + 3', '2x + 15'),
  'schritte': [{'text': 'Das x-Glied 2x auf beiden Seiten wegnehmen: 3x + 3 = 15.', 'bild': waage('3x + 3', '15')},
               {'text': 'Auf beiden Seiten 3 kg wegnehmen: 3x = 12.', 'bild': waage('3x', '12')},
               {'text': 'Beide Seiten durch 3 teilen: ⟦x = 4⟧.', 'bild': waage('x', '4')}],
  'fehler': 'Aus 5x + 3 = 2x + 15 wird nicht 7x + 3 = 15. Rechts werden 2 Dosen ⟦weggenommen⟧, also links auch: 5x − 2x = 3x.',
  'fehler_bild': waage_kipp('7x + 3', '15'),
  'regel': 'Bring alle ⟦x-Glieder auf eine Seite⟧ und alle Zahlen auf die andere. Nimm dazu auf beiden Seiten dasselbe weg.'},
 'klammern': {
  'einstieg': 'In drei Tüten liegen je ein paar Äpfel und 2 Birnen. Mit x Äpfeln pro Tüte sind das 3 · (x + 2) Früchte. Um damit zu rechnen, muss man die ⟦Klammer auflösen⟧.',
  'woerter': [['Klammer auflösen', 'die Zahl vor der Klammer mit jedem Teil darin malnehmen'], ['3(x + 2)', 'kurz für 3 · (x + 2)']],
  'bild': flaeche_bild(),
  'schritte': [{'text': 'Die Gleichung ist 3(x + 2) = 2x + 11.'},
               {'text': 'Klammer auflösen: 3x + 6 = 2x + 11.'},
               {'text': 'Auf beiden Seiten 2x wegnehmen: x + 6 = 11.'},
               {'text': 'Auf beiden Seiten 6 wegnehmen: ⟦x = 5⟧.'}],
  'fehler': '3(x + 2) ist nicht 3x + 2. In jeder der drei Tüten sind 2 Birnen, zusammen ⟦6⟧. Ein Minus vor der Klammer dreht alle Vorzeichen um.',
  'regel': 'Erst die ⟦Klammern auflösen⟧: Jeder Teil wird malgenommen. Ein Minus vor der Klammer dreht alle Vorzeichen um.'},
 'probe': {
  'einstieg': 'An der Kasse zählst du dein Wechselgeld nach. Bei Gleichungen gibt es auch so eine Kontrolle: Lösung einsetzen und beide Seiten vergleichen. Das ist die ⟦Probe⟧.',
  'woerter': [['ursprüngliche Gleichung', 'die Gleichung aus der Aufgabe, vor dem Umformen'], ['≈', 'ungefähr gleich (gerundet)'],
              ['Probe', 'Lösung einsetzen und beide Seiten getrennt ausrechnen']],
  'bild': {'typ': 'tabelle', 'kopf': ['Lösung', 'links: 4x − 7', 'rechts: x + 8'], 'zeilen': [['x = 1/3', '?', '?']]},
  'schritte': [{'text': 'Jemand löst 4x − 7 = x + 8 und erhält x = 1/3.'},
               {'text': 'Einsetzen in die ursprüngliche Gleichung: links ≈ −5,7, rechts ≈ 8,3.', 'bild': {'zeilen': [['x = 1/3', '≈ −5,7', '≈ 8,3']]}},
               {'text': 'Die Seiten sind verschieden. Die Lösung ist falsch, richtig ist x = 5.'},
               {'text': 'Mit x = 5 ergeben beide Seiten 13. ⟦Stimmt.⟧', 'bild': {'zeilen': [['x = 1/3', '≈ −5,7', '≈ 8,3'], ['x = 5', '13', '13']]}}],
  'fehler': 'Die Probe in einer schon umgeformten Zeile beweist nichts. War dort ein Fehler, bleibt er ⟦unentdeckt⟧. Setze immer in die ursprüngliche Gleichung ein.',
  'regel': 'Setze die Lösung in die ⟦ursprüngliche Gleichung⟧ ein. Beide Seiten müssen dasselbe ergeben.'},
 'sonderfaelle': {
  'einstieg': 'Zwei Handytarife kosten beide 2 € pro Gigabyte. Der eine hat 3 € Grundgebühr, der andere 5 €. Sind sie je gleich teuer? Nie! Manche Gleichungen haben ⟦keine Lösung⟧.',
  'woerter': [['GB', 'Gigabyte: eine Menge an Internet-Daten'], ['L = { }', 'keine Zahl passt: leere Lösungsmenge'], ['L = ℚ', 'jede Zahl passt']],
  'bild': _tarife(_AB_PAR, x=(0, 6), y=(0, 20)),
  'schritte': [{'text': 'Gleichung mit x in GB: 2x + 3 = 2x + 5.'},
               {'text': 'Beide Seiten minus 2x: Es bleibt 3 = 5. Das ist falsch, egal welches x.'},
               {'text': 'Die Linien laufen parallel und treffen sich nie: ⟦L = { }⟧.'},
               {'text': 'Bei 2(x + 3) = 2x + 6 bleibt 6 = 6: ⟦L = ℚ⟧.',
                'bild': {'graphen': [{'art': 'linear', 'm': 2, 't': 6, 'name': 'beide gleich'}]}}],
  'fehler': 'Aus 3 = 5 folgt nicht „x = 0“. Wenn x verschwindet, entscheidet nur: Ist der Rest ⟦wahr oder falsch⟧?',
  'regel': 'Fällt x weg, zählt nur der Rest. ⟦Falsch⟧: keine Lösung. Wahr: Jede Zahl ist eine Lösung.'},
 'sach': {
  'einstieg': 'Tarif A kostet 10 € Grundgebühr und 2 € pro GB. Tarif B kostet 4 € pro GB. Bei welcher Datenmenge kosten beide gleich viel? Das ist eine ⟦Sachaufgabe⟧.',
  'woerter': [['Sachaufgabe', 'Aufgabe aus dem Alltag, gelöst mit einer Gleichung'], ['Variable festlegen', 'aufschreiben, wofür x steht']],
  'bild': _tarife([{'art': 'linear', 'm': 2, 't': 10, 'name': 'A'}, {'art': 'linear', 'm': 4, 't': 0, 'name': 'B'}], y=(0, 35)),
  'schritte': [{'text': 'Variable festlegen: x ist die Anzahl GB.'},
               {'text': 'Beide Preise gleichsetzen: 10 + 2x = 4x.'},
               {'text': 'Auf beiden Seiten 2x weg: 10 = 2x, also x = 5.'},
               {'text': 'Bei ⟦5 GB⟧ kosten beide 20 €.', 'bild': {'punkte': [{'x': 5, 'y': 20, 'name': 'gleich teuer'}]}}],
  'fehler': 'Die Antwort ist nicht nur „x = 5“. Gefragt ist die Datenmenge: ⟦Bei 5 GB⟧ kosten beide 20 €. Antworte immer im Sachzusammenhang.',
  'regel': 'Variable festlegen, ⟦Gleichung aufstellen⟧, lösen und im Sachzusammenhang antworten.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---------- Zehnte Runde (schwer-kl7): schwerere Übungen nach Prüfungsvorbild ----------
# Vorbilder (nur Typ und Niveau, eigene Zahlen und Einkleidung): Bayerischer Mathematik-Test 8 (ISB) 2019 B2, 2021 A3, 2023 A2 (Sachaufgabe
# mit Eintrittskarten), 2024 A1 (Klammer mit Minus; Zahl ersetzen, damit x = 2 Lösung ist); Jahrgangsstufentest Realschule 8 (2025, Nr. 12, 13, 15);
# Schulaufgabe Klasse 7 Gymnasium (Lösungsmenge mit Grundmenge, Fehler in einer Rechnung finden). Eigener Zufallsstart, alte Aufgaben bleiben gleich.
from _schwer_kl7 import Neu, anhaengen  # noqa: E402


def schwer():
    N = Neu(7002)
    P = 'pruefung'
    K = 'knobel'
    BR = 'Zähler und Nenner eintragen; ein Minus gehört in den Zähler.'
    LM = {'q': 'L = ℚ (jede Zahl)', 'l': 'L = { } (keine Lösung)'}
    # waage
    N.Z('waage', 2, 'Löse 0,4x − 1,2 = 2.', 8, '(2 + 1.2) / 0.4', 'Plus 1,2: 0,4x = 3,2. Geteilt durch 0,4: x = 8.', 'Erst die Zahl weg, dann durch 0,4 teilen.')
    N.Z('waage', 2, 'Löse 12 − 3x = 0.', 4, '12 / 3', 'Plus 3x: 12 = 3x. Geteilt durch 3: x = 4.', 'Bring 3x auf die andere Seite, damit es positiv wird.')
    N.Z('waage', 3, 'Löse x/3 + x/6 = 5.', 10, '5 * 6 / 3',
        'Mal 6 (Hauptnenner): 2x + x = 30, also 3x = 30 und x = 10. Probe: 10/3 + 10/6 = 20/6 + 10/6 = 5 ✓.',
        'Multipliziere beide Seiten mit dem Hauptnenner 6.', art=P)
    N.Z('waage', 3, 'Welche Zahl muss im Kästchen stehen, damit die Gleichung 3x + □ = −5 die Lösungsmenge L = {−4} hat?', 7, '-5 - 3 * (-4)',
        'x = −4 einsetzen: 3 · (−4) + □ = −5, also −12 + □ = −5 und □ = 7.', 'Setze die Lösung ein und rechne das Kästchen aus.', art=P)
    N.Z('waage', 3, 'Löse −3/5 x + 2 = 8.', -10, '(8 - 2) / (-3/5)',
        'Minus 2: −3/5 x = 6. Mal (−5/3): x = −10. Probe: −3/5 · (−10) + 2 = 6 + 2 = 8 ✓.',
        'Teilen durch −3/5 ist dasselbe wie mal (−5/3). Achte auf das Vorzeichen.')
    N.A('waage', 3, 'Jemand rechnet bei 5x = 3x: „Ich teile beide Seiten durch x und erhalte 5 = 3. Also gibt es keine Lösung.“ Was stimmt?',
        'Falsch: x = 0 ist eine Lösung. Durch x darf man nicht teilen, weil x null sein kann.',
        ['Richtig: 5 = 3 ist falsch, also L = { }.', 'Falsch: Jede Zahl ist eine Lösung.', 'Richtig, denn durch x teilen ist immer erlaubt.'],
        'Probe mit x = 0: 5 · 0 = 3 · 0 ✓. Richtig umformen: minus 3x gibt 2x = 0, also x = 0. Teilen durch x wäre Teilen durch 0.',
        'Setze x = 0 ein. Was passiert beim Teilen durch x, wenn x = 0 ist?', art=K)
    # beide_seiten
    N.Z('beide_seiten', 2, 'Löse 1,5x + 4 = 0,5x − 3.', -7, '(-3 - 4) / (1.5 - 0.5)', 'Minus 0,5x: x + 4 = −3. Minus 4: x = −7.', 'Bring die x-Glieder nach links.')
    N.Z('beide_seiten', 2, 'Löse 9 − 4x = 2x − 15.', 4, '(9 + 15) / (2 + 4)', 'Plus 4x: 9 = 6x − 15. Plus 15: 24 = 6x. Also x = 4.', 'Bring die x-Glieder auf die Seite, auf der mehr x stehen.')
    N.Z('beide_seiten', 3, 'Löse 2,5x − 6 = 4,5x + 10.', -8, '(10 + 6) / (2.5 - 4.5)',
        'Minus 2,5x: −6 = 2x + 10. Minus 10: −16 = 2x. Also x = −8. Probe: −20 − 6 = −26 und −36 + 10 = −26 ✓.',
        'Dezimalzahlen wie ganze Zahlen behandeln. Welche Seite hat mehr x?', art=P)
    N.Z('beide_seiten', 3, 'In der Gleichung 4x − 3 = 2x + □ soll x = 5 die Lösung sein. Welche Zahl gehört in das Kästchen?', 7, '4 * 5 - 3 - 2 * 5',
        'x = 5 einsetzen: 20 − 3 = 10 + □, also 17 = 10 + □ und □ = 7.', 'Setze x = 5 auf beiden Seiten ein.', art=P)
    N.Z('beide_seiten', 3, 'Auf einer Waage liegen links 3 gleiche Kugeln und 4 Würfel, rechts 1 Kugel und 10 Würfel. Die Waage ist im Gleichgewicht. Ein Würfel wiegt 15 g. Wie schwer ist eine Kugel?', 45,
        '(10 - 4) * 15 / (3 - 1)',
        'Gleichung: 3k + 4 · 15 = k + 10 · 15, also 3k + 60 = k + 150. Minus k und minus 60: 2k = 90, k = 45 g.',
        'Nimm auf beiden Seiten 1 Kugel und 4 Würfel weg. Was bleibt?', einheit='g', art=K)
    N.L('beide_seiten', 3, 'Löse 4x − 7 = 10x + 2. Gib x als gekürzten Bruch an.', 'x = □/□', [-3, 2], ['-3', '2'],
        'Minus 4x: −7 = 6x + 2. Minus 2: −9 = 6x. x = −9/6 = −3/2.', 'Am Ende kürzen. Das Minus steht im Zähler.', BR)
    # klammern
    N.Z('klammern', 2, 'Löse 3(2x − 1) = 4x + 9.', 6, '(9 + 3) / (6 - 4)', 'Klammer auflösen: 6x − 3 = 4x + 9. Minus 4x, plus 3: 2x = 12, x = 6.', 'Erst 3 mal jeden Teil der Klammer.')
    N.Z('klammern', 2, 'Löse −(x − 4) = 2x + 1.', 1, '(4 - 1) / 3', 'Minus vor der Klammer: −x + 4 = 2x + 1. Plus x, minus 1: 3 = 3x, x = 1.', 'Das Minus vor der Klammer dreht beide Vorzeichen um.')
    N.Z('klammern', 3, 'Löse 7x − (4x − 9) = 30.', 7, '(30 - 9) / 3',
        'Klammer weg, Vorzeichen drehen: 7x − 4x + 9 = 30. Zusammenfassen: 3x + 9 = 30, also 3x = 21 und x = 7.',
        'Achtung: −(4x − 9) = −4x + 9.', art=P)
    N.Z('klammern', 3, 'Löse 3(x − 2) − 2(2x + 1) = 4.', -12, '(4 + 6 + 2) / (3 - 4)',
        '3x − 6 − 4x − 2 = 4. Zusammenfassen: −x − 8 = 4. Also −x = 12 und x = −12.',
        'Beide Klammern einzeln auflösen; vor der zweiten steht −2.', art=P)
    N.Z('klammern', 3, 'Löse 0,5(4x − 6) = 3 − (x − 3).', 3, '(3 + 3 + 3) / (2 + 1)',
        'Links: 2x − 3. Rechts: 3 − x + 3 = 6 − x. 2x − 3 = 6 − x, also 3x = 9 und x = 3.', 'Beide Seiten zuerst einzeln vereinfachen.')
    N.L('klammern', 3, 'Löse (x + 3)(x − 1) = x(x + 4). Gib x als gekürzten Bruch an.', 'x = □/□', [-3, 2], ['-3', '2'],
        'Links: x² − x + 3x − 3 = x² + 2x − 3. Rechts: x² + 4x. Minus x²: 2x − 3 = 4x, also −3 = 2x und x = −3/2.',
        'Multipliziere jede Klammer aus. Was passiert mit dem x²?', BR, art=K)
    # probe
    N.A('probe', 2, 'Ist x = −2 eine Lösung von 3(x + 4) = 2 − 2x?', 'Ja: Beide Seiten ergeben 6.', ['Nein: links 6, rechts −2.', 'Nein: links 10, rechts 6.', 'Ja: Beide Seiten ergeben −2.'],
        'Links: 3 · (−2 + 4) = 3 · 2 = 6. Rechts: 2 − 2 · (−2) = 2 + 4 = 6. Gleich, also Lösung.', 'Setze −2 in beide Seiten der ursprünglichen Gleichung ein.')
    N.A('probe', 2, 'Welche der Zahlen erfüllt die Gleichung 2x − 3 = x − 1?', '2', ['−1', '0', '1'],
        'Probe mit x = 2: 4 − 3 = 1 und 2 − 1 = 1 ✓. Bei −1, 0, 1 sind die Seiten verschieden.', 'Setze jede Zahl ein und vergleiche beide Seiten.')
    N.Z('probe', 3, 'Die Gleichung 6x − 2(x + □) = 10 soll die Lösung x = 4 haben. Welche Zahl gehört in das Kästchen?', 3, '(6 * 4 - 2 * 4 - 10) / 2',
        'x = 4: 24 − 2(4 + □) = 10. Also 2(4 + □) = 14, 4 + □ = 7 und □ = 3.', 'Setze x = 4 ein und rechne rückwärts.', art=P)
    N.A('probe', 3, 'Rechnung zu 5 − 2(x − 3) = 1: (1) 5 − 2x − 6 = 1 → (2) −2x − 1 = 1 → (3) x = −1. In welcher Zeile steckt der erste Fehler?', 'Zeile 1',
        ['Zeile 2', 'Zeile 3', 'Kein Fehler'],
        '−2 · (−3) = +6, nicht −6. Richtig: 5 − 2x + 6 = 1. Zeilen 2 und 3 rechnen mit dem Fehler korrekt weiter.', 'Prüfe das Vorzeichen beim Auflösen der Klammer.', art=P)
    N.Z('probe', 3, 'Rechnung zu 5 − 2(x − 3) = 1: (1) 5 − 2x − 6 = 1 → (2) −2x − 1 = 1 → (3) x = −1. Wie heißt die richtige Lösung?', 5, '(5 + 6 - 1) / 2',
        'Richtig: 5 − 2x + 6 = 1, also 11 − 2x = 1, −2x = −10 und x = 5. Probe: 5 − 2 · 2 = 1 ✓.', 'Löse die Klammer mit dem richtigen Vorzeichen auf.', art=P)
    N.A('probe', 3, 'Aus x = 3 folgt durch Quadrieren beider Seiten x² = 9. Haben x = 3 und x² = 9 dieselbe Lösungsmenge?', 'Nein: x² = 9 hat auch die Lösung −3.',
        ['Ja: Quadrieren ist eine Äquivalenzumformung.', 'Ja: Beide haben nur die Lösung 3.', 'Nein: x² = 9 hat keine Lösung.'],
        '(−3)² = 9, aber −3 ≠ 3. Quadrieren kann neue Lösungen dazubringen – es ist keine Äquivalenzumformung. Darum ist die Probe wichtig.',
        'Probiere x = −3 in beiden Gleichungen.', art=K)
    # sonderfaelle
    N.A('sonderfaelle', 2, 'Bestimme die Lösungsmenge von 3(x − 2) + 6 = 3x.', LM['q'], [LM['l'], 'L = {0}', 'L = {6}'],
        '3x − 6 + 6 = 3x, also 3x = 3x. Minus 3x: 0 = 0, immer wahr. Jede Zahl ist Lösung.', 'Löse die Klammer auf und fasse zusammen.')
    N.A('sonderfaelle', 2, 'Bestimme die Lösungsmenge von 6x − 3(2x − 1) = 1.', LM['l'], [LM['q'], 'L = {1}', 'L = {0}'],
        '6x − 6x + 3 = 1, also 3 = 1. Das ist falsch, egal welches x: keine Lösung.', 'Achtung: −3 · (−1) = +3.')
    N.A('sonderfaelle', 3, 'Bestimme die Lösungsmenge von 2x + 5 = 8 für die Grundmenge G = ℕ (natürliche Zahlen).', 'L = { }',
        ['L = {1,5}', 'L = {1}', 'L = ℕ'],
        '2x = 3, also x = 1,5. 1,5 ist keine natürliche Zahl. In G = ℕ gibt es keine Lösung: L = { }.', 'Löse zuerst. Liegt die Lösung in der Grundmenge?', art=P)
    N.A('sonderfaelle', 3, 'Bestimme die Lösungsmenge von 3(x + 2) = 3x + 6 − x.', 'L = {0}', [LM['q'], LM['l'], 'L = {6}'],
        '3x + 6 = 2x + 6 (rechts zusammenfassen). Minus 2x, minus 6: x = 0. Wegen des −x ist es nicht 0 = 0.', 'Rechts erst zusammenfassen: 3x − x.', art=P)
    N.Z('sonderfaelle', 3, 'Für welchen Wert von a hat die Gleichung (a − 2) · x = 6 keine Lösung?', 2, '2',
        'Für a = 2 steht dort 0 · x = 6, also 0 = 6 – falsch für jedes x. Für jedes andere a gibt es genau eine Lösung x = 6 : (a − 2).',
        'Wann verschwindet x? Dann bleibt eine Aussage ohne x.', art=K)
    N.A('sonderfaelle', 3, 'Welche Gleichung hat KEINE Lösung?', '2(x + 1) = 2x + 1', ['2(x + 1) = 2x + 2', '2(x + 1) = x + 2', '2x = 0'],
        '2(x + 1) = 2x + 1 wird zu 2 = 1: falsch, keine Lösung. 2(x + 1) = 2x + 2 hat L = ℚ; die anderen haben je die Lösung x = 0.', 'Löse jede Gleichung kurz.')
    # sach
    N.Z('sach', 2, 'Die Summe dreier aufeinanderfolgender ganzer Zahlen ist −27. Wie heißt die größte der drei Zahlen?', -8, '(-27 - 3) / 3 + 2',
        'x + (x + 1) + (x + 2) = −27, also 3x + 3 = −27, 3x = −30, x = −10. Die Zahlen: −10, −9, −8. Größte: −8.', 'Nenne die kleinste Zahl x. Wie heißen die anderen?')
    N.Z('sach', 2, 'Ein Seil von 12 m wird in zwei Teile geschnitten. Ein Teil ist 2,4 m länger als der andere. Wie lang ist das kürzere Teil?', Fr('4.8'), '(12 - 2.4) / 2',
        'x + (x + 2,4) = 12, also 2x = 9,6 und x = 4,8 m. Probe: 4,8 + 7,2 = 12 ✓.', 'Kürzeres Teil x, längeres x + 2,4.', einheit='m')
    N.A('sach', 3, 'Ein Theater hat 240 Plätze, alle sind verkauft. Kinder zahlen 6 €, Erwachsene 11 €. Die Einnahmen betragen 2 140 €. x ist die Zahl der Kinderkarten. Welche Gleichung passt?',
        '6x + 11(240 − x) = 2 140', ['6x + 11x = 2 140', '6x + 11 · 240 = 2 140', '6(240 − x) + 11x = 2 140'],
        'Kinder: x Karten zu 6 €. Erwachsene: der Rest, 240 − x Karten zu 11 €. Zusammen 2 140 €.', 'Wie viele Erwachsenenkarten sind es, wenn x Kinderkarten verkauft wurden?', art=P)
    N.Z('sach', 3, 'Ein Theater hat 240 Plätze, alle sind verkauft. Kinder zahlen 6 €, Erwachsene 11 €. Die Einnahmen betragen 2 140 €. Wie viele Kinderkarten wurden verkauft?', 100, '(11 * 240 - 2140) / (11 - 6)',
        '6x + 11(240 − x) = 2 140 → 6x + 2 640 − 11x = 2 140 → −5x = −500 → x = 100 Kinderkarten. Probe: 600 € + 140 · 11 € = 2 140 € ✓.',
        'Stelle die Gleichung mit x Kinderkarten auf und löse die Klammer auf.', einheit='Karten', art=P)
    N.Z('sach', 3, 'Ein rechteckiges Gehege wird an eine Mauer gebaut; die Mauer ersetzt eine lange Seite. Für die anderen drei Seiten gibt es 50 m Zaun. Die lange Seite ist doppelt so lang wie eine kurze. Wie lang ist eine kurze Seite?',
        Fr('12.5'), '50 / 4',
        'Kurze Seite x, lange 2x. Zaun: x + x + 2x = 50, also 4x = 50 und x = 12,5 m.', 'Welche Seiten brauchen Zaun? Mach eine Skizze.', einheit='m', art=P)
    N.Z('sach', 3, 'Ein Vater ist heute dreimal so alt wie seine Tochter. In 12 Jahren ist er nur noch doppelt so alt wie sie. Wie alt ist die Tochter heute?', 12, '2 * 12 - 12',
        'Tochter t, Vater 3t. In 12 Jahren: 3t + 12 = 2(t + 12) → 3t + 12 = 2t + 24 → t = 12. Probe: 36 + 12 = 48 = 2 · 24 ✓.',
        'Beide werden 12 Jahre älter. Stelle die Gleichung für „in 12 Jahren“ auf.', einheit='Jahre', art=K)
    return N


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('gleichungen.linear', 13_7_3)
# a) ein bzw. zwei Umformungen wie Stufe 2
BF.stufe('waage', 'Löse −11 − x = 5.', 2)
BF.stufe('waage', 'Löse 2,5x + 4 = 29.', 2)
# c) Ablenker „Es kommt 0 = c heraus“ ist unverständlich (c nirgends erklärt) → Aufgabe mit klarem Ablenker
BF.ersetze('probe', 'Jemand multipliziert 6x + 6 = 21 auf beiden Seiten mit 0 und erhält 0 = 0. Er folgert: „Jede Zahl ist eine Lösung.“ Stimmt das?', BF.A(
    'Jemand multipliziert die Gleichung 6x + 6 = 21 auf beiden Seiten mit 0 und erhält 0 = 0. Er folgert: „Jede Zahl ist eine Lösung.“ Hat er recht?',
    'Nein: Mal 0 ist keine Äquivalenzumformung.',
    ['Nein: Es kommt 6 = 21 heraus.', 'Ja: 0 = 0 ist immer wahr.', 'Ja: Auf beiden Seiten dasselbe ist erlaubt.'],
    'Mit 0 multiplizieren macht aus jeder Gleichung 0 = 0 – dabei geht die Information verloren. Darum ist nur Multiplizieren mit Zahlen ≠ 0 erlaubt. Die Gleichung hat genau eine Lösung: x = 2,5.',
    'Welche Zahl ist beim Multiplizieren und Dividieren ausgeschlossen – und warum?'))
# a) prüft nur das Deuten von „−10 = −10“
BF.stufe('probe', 'Die Probe für x = −4 bei x − 6 = −5x − 30 wird so geschrieben: „x − 6 = −5x − 30 | x = −4 → −10 = −10 ✓“. Welche Aussage stimmt?', 2)
# a) Gleichung mit zwei Bezügen aufstellen → Stufe 2
BF.stufe('sach', 'Eine Mutter ist 4 Jahre älter als das 3-Fache des Alters ihres Sohnes. Zusammen sind sie 44 Jahre alt. Wie alt ist der Sohn?', 2)

# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Klasse 7, siehe _durchsicht_kl7.py) ----
# Vorbilder (Typ und Niveau, eigene Zahlen): BMT8 (ISB) 2019 B2, 2024 A3 (Klammern, Lücke so füllen, dass x eine Lösung ist), 2023 A7 (Rest-Term);
# Jahrgangsstufentest Realschule 8 (ISB) 2025 II (Bewegungsaufgabe, Füllstand).
from _durchsicht_kl7 import Durchsicht, durchsicht_datei  # noqa: E402

DS = Durchsicht('gleichungen.linear', 19_7_5)
# beide_seiten: „längere Gleichung zum Zusammenfassen“ ist mehrschrittig, aber kein anderer Gedanke → zwei von drei auf Stufe 2
DS.stufe('beide_seiten', 'Löse 3x − 21 + 6x = −4x − 92 + 6.', 2)
DS.stufe('beide_seiten', 'Löse −8x + 5 + x = x − 1 − 2.', 2)
# klammern: Stufe 3 bestand fast nur aus „zwei Klammern auflösen und lösen“ (längere Rechnung) → drei davon Stufe 2, dafür andere Gedanken neu
for _t in ['Löse 2(x + 7) = 5(x + 9) − 55.', 'Löse 2(x − 2) − 4(x − 8) = 32.', 'Löse 2(x − 5) − 5(x − 8) = 27.']:
    DS.stufe('klammern', _t, 2)
DS.neu('klammern', 3, DS.A('Jemand löst 8 − 2(x − 3) = 4 so: 8 − 2x − 6 = 4, also −2x = 2 und x = −1. Was stimmt?',
                           'Falsch: (−2) · (−3) = +6. Richtig ist 8 − 2x + 6 = 4, also x = 5.',
                           ['Richtig gerechnet, x = −1.', 'Falsch: Richtig ist 8 − 2x − 3 = 4, also x = 0,5.', 'Falsch: Man darf die Klammer nicht auflösen.'],
                           'Minus vor der 2 und minus in der Klammer ergeben plus: −2 · (−3) = +6. 8 − 2x + 6 = 4 → −2x = −10 → x = 5. Probe: 8 − 2 · 2 = 4 ✓.',
                           'Prüfe das Vorzeichen beim zweiten Glied der Klammer – oder mach die Probe mit x = −1.'))
DS.neu('klammern', 3, DS.Z('Welche Zahl muss im Kästchen stehen, damit 3(x − □) = x + 4 die Lösung x = 5 hat?', 2, '(15 - 9) / 3',
                           'x = 5 einsetzen: 3(5 − □) = 9, also 5 − □ = 3 und □ = 2. Probe: 3(5 − 2) = 9 = 5 + 4 ✓.',
                           'Setze x = 5 ein. Dann ist nur noch das Kästchen unbekannt.'))
DS.neu('klammern', 3, DS.Z('Ein Dreieck hat die Seiten x cm, 2(x − 1) cm und (x + 4) cm. Sein Umfang ist 26 cm. Wie lang ist die kürzeste Seite?', 6, '(26 - 2) / 4',
                           'x + 2x − 2 + x + 4 = 26 → 4x + 2 = 26 → x = 6. Seiten 6 cm, 10 cm, 10 cm. Die kürzeste ist 6 cm.',
                           'Gleichung für den Umfang aufstellen, Klammer auflösen. Danach alle drei Seiten ausrechnen.', einheit='cm'))
# probe: „Probe-Schreibweise deuten“ steht schon in Stufe 2 → Stufe 2
DS.stufe('probe', 'Die Probe für x = −8 bei −8x − 16 = −3x + 24 wird so geschrieben: „−8x − 16 = −3x + 24 | x = −8 → 48 = 48 ✓“. Welche Aussage stimmt?', 2)
# sonderfaelle: dreimal „□ für unendlich viele Lösungen“ in Stufe 3 → zwei davon Stufe 2
DS.stufe('sonderfaelle', 'Welche Zahl muss für □ stehen, damit 5(x + 4) = 5x + □ unendlich viele Lösungen hat?', 2)
DS.stufe('sonderfaelle', 'Welche Zahl muss für □ stehen, damit 3(x + 3) = 3x + □ unendlich viele Lösungen hat?', 2)
# sach: fünfmal „Lena spart, Tom gibt aus“ in Stufe 2, je zweimal derselbe Typ in Stufe 3 → Abwechslung
DS.ersetze('sach', 'Lena hat 54 € und spart jede Woche 6 € dazu. Tom hat 164 € und gibt jede Woche 5 € aus. Nach wie vielen Wochen haben beide gleich viel?',
           DS.Z('Im Kino zahlt ein Erwachsener 3 € mehr als ein Kind. Zwei Erwachsene und drei Kinder zahlen zusammen 41 €. Wie viel kostet eine Kinderkarte?', 7,
                '(41 - 6) / 5', 'Kinderkarte x €: 2(x + 3) + 3x = 41 → 5x + 6 = 41 → x = 7. Eine Kinderkarte kostet 7 €.',
                'Lege x als Preis der Kinderkarte fest. Was kostet dann eine Erwachsenenkarte?', einheit='€'), pools=('uebung',))
DS.ersetze('sach', 'Lena hat 42 € und spart jede Woche 6 € dazu. Tom hat 152 € und gibt jede Woche 4 € aus. Nach wie vielen Wochen haben beide gleich viel?',
           DS.Z('Vier Seiten eines Fünfecks sind gleich lang, die fünfte ist 4 cm länger. Der Umfang ist 54 cm. Wie lang ist die längste Seite?', 14,
                '(54 - 4) / 5 + 4', 'Kurze Seite x: 5x + 4 = 54 → x = 10. Die längste Seite ist 10 + 4 = 14 cm.',
                'Gefragt ist die längste Seite, nicht x.', einheit='cm'), pools=('uebung',))
DS.ersetze('sach', '„Zwei aufeinanderfolgende natürliche Zahlen ergeben zusammen 66.“ Die Gleichung x + (x + 1) = 66 liefert x = 32,5. Was folgt daraus?',
           DS.Z('Zug A fährt um 8 Uhr mit 80 km/h los. Zug B fährt auf derselben Strecke um 9 Uhr mit 120 km/h hinterher. Um wie viel Uhr holt B den Zug A ein?', 11,
                '8 + 120 / 40', 'A ist t Stunden unterwegs, B eine Stunde weniger: 80t = 120(t − 1) → 40t = 120 → t = 3. Das ist um 8 + 3 = 11 Uhr.',
                'Gleich weit gefahren heißt: Weg von A = Weg von B. B fährt eine Stunde kürzer.', einheit='Uhr'))
DS.ersetze('sach', 'Tarif A: 28 € und 2 € pro Stunde. Tarif B: 0 € und 4 € pro Stunde. Die Gleichung ergibt x = 14. Welcher Tarif ist bei 17 Stunden günstiger?',
           DS.Z('Ein Kanister ist zu einem Drittel gefüllt. Nach dem Nachfüllen von 10 Litern ist er zu drei Vierteln voll. Wie viele Liter passen hinein?', 24,
                '10 / (3/4 - 1/3)', 'Inhalt V: 1/3 V + 10 = 3/4 V → 10 = (3/4 − 1/3) V = 5/12 V → V = 24 Liter.',
                'Stelle eine Gleichung mit dem ganzen Inhalt V auf. Die 10 Liter füllen den Unterschied zwischen 1/3 und 3/4.', einheit='l'))
# ---- DURCHSICHT ENDE ----


# ---- STUFEN (Zwanzigste Runde: echte Stufe 3 und Knobel-Bordkarten, siehe _stufen_kl7.py) ----
# Vorbilder (Typ und Niveau, eigene Zahlen): BMT8 (ISB) – „Löse die Gleichung“ mit Dezimalzahlen und Klammern, Zahl aus einer Lösung bestimmen,
# Sachaufgabe mit Gesamtkosten; Knobel nach der Art von Känguru 7/8 und Mathematik-Olympiade (Flasche und Korken, Altersrätsel, Kerzen, Köpfe und Beine).
from _stufen_kl7 import Stufen, stufen_datei  # noqa: E402

ST = Stufen('gleichungen.linear', 20_7_5)
# waage
ST.leiter('waage', 'x ± a = b mit einer Umformung lösen; passende Umformung erkennen.',
          'ax ± b = c in zwei Schritten, Umformungen notieren, Bruch als Faktor, Waage mit Päckchen.',
          'Brüche als Faktoren verknüpfen, Kästchen für eine Lösung, Zahlenrätsel rückwärts, Fehler „durch x teilen“, Umformungen begründen, Prüfungsaufgabe mit Dezimalzahlen.')
ST.regel('waage', 1, '', 'direkt')
ST.regel('waage', 2, 'Welche Gleichung entsteht', 'darstellung')
ST.regel('waage', 2, '', 'mehrschritt')
ST.regel('waage', 3, 'Löse 3/4 x', 'mehrschritt', neu_s=2)
ST.regel('waage', 3, 'Kästchen', 'parameter')
ST.regel('waage', 3, 'Jemand', 'fehler')
ST.regel('waage', 3, '', 'verknuepfen')
ST.neu('waage', 1, 'erkennen', ST.A('Welche Umformung löst x − 7 = 12 in einem Schritt?', 'auf beiden Seiten + 7', ['auf beiden Seiten − 7', 'nur rechts + 7', 'auf beiden Seiten · 7'],
                                    'x − 7 + 7 = x. Damit die Waage im Gleichgewicht bleibt, muss auch rechts + 7 gerechnet werden: x = 19.', 'Wie wird man die − 7 neben dem x los?'))
ST.neu('waage', 2, 'einkleidung', ST.Z('Auf einer Waage liegen links 3 gleiche Päckchen und ein 200-g-Gewicht, rechts Gewichte mit zusammen 1 100 g. Die Waage ist im Gleichgewicht. Wie schwer ist ein Päckchen?',
                                       300, '(1100 - 200) / 3', '3x + 200 = 1 100. Minus 200: 3x = 900. Durch 3: x = 300 g.', 'Nimm auf beiden Seiten 200 g weg.', einheit='g'))
ST.neu('waage', 3, 'rueckwaerts', ST.Z('Ich denke mir eine Zahl, multipliziere sie mit 4 und ziehe 9 ab. Ich erhalte 23. Welche Zahl habe ich mir gedacht?', 8, '(23 + 9) / 4',
                                       'Gleichung 4x − 9 = 23. Rückwärts: 23 + 9 = 32, 32 : 4 = 8. Probe: 4 · 8 − 9 = 23 ✓.', 'Mache die Rechenschritte in umgekehrter Reihenfolge rückgängig.'))
ST.neu('waage', 3, 'pruefung', ST.Z('Löse die Gleichung 0,5x + 1,5 = 4.', 5, '(4 - 1.5) / 0.5', '0,5x = 2,5. Durch 0,5 (oder mal 2): x = 5. Probe: 2,5 + 1,5 = 4 ✓.', 'Ziehe zuerst 1,5 ab.'))
ST.neu('waage', 3, 'begruenden', ST.A('Warum darf man bei einer Gleichung auf beiden Seiten dieselbe Zahl abziehen?', 'Weil beide Seiten gleich bleiben – wie bei einer Waage, von der man links und rechts gleich viel wegnimmt.',
                                      ['Weil die Zahl dann verschwindet.', 'Weil man das bei jeder Rechnung darf.', 'Man darf es nur bei positiven Zahlen.'],
                                      'Zwei gleich große Werte bleiben gleich, wenn man von beiden dasselbe abzieht. Deshalb hat die neue Gleichung dieselbe Lösung (Äquivalenzumformung).',
                                      'Denke an eine Waage im Gleichgewicht.'))
ST.knobel('waage', ST.Z('Eine Flasche mit Korken kostet 1,10 €. Die Flasche kostet 1 € mehr als der Korken. Wie viel Cent kostet der Korken?', 5, '(110 - 100) / 2',
                        'Viele antworten 10 Cent – dann kostete die Flasche 1,10 € und beides zusammen 1,20 €. Richtig: Korken x Cent, Flasche x + 100 Cent. '
                        'x + x + 100 = 110, also 2x = 10 und x = 5. Probe: 5 Cent + 1,05 € = 1,10 € ✓.',
                        'Prüfe die erste Antwort, die dir einfällt, mit einer Probe.'))
ST.knobel('waage', ST.Z('Ein Ziegelstein wiegt 1 kg und einen halben Ziegelstein. Wie viel Kilogramm wiegt ein ganzer Ziegelstein?', 2, '1 / (1 - 0.5)',
                        'Gleichung: x = 1 + x/2. Zieht man x/2 ab: x/2 = 1, also x = 2 kg. Anschaulich: Auf der Waage halten ein halber Ziegel und 1 kg dem ganzen Ziegel stand – der halbe Ziegel wiegt also 1 kg.',
                        'Lege einen Ziegelstein auf die eine Seite einer Waage. Was muss auf die andere?', einheit='kg'))
# beide_seiten
ST.leiter('beide_seiten', 'x auf beiden Seiten mit einem Schritt auf eine Seite bringen; sinnvollen ersten Schritt erkennen.',
          'Mehrere x- und Zahlglieder, negative Faktoren, Umformungen notieren, Sparvergleich.',
          'Lösungen als Bruch, Kästchen für eine Lösung, Waage mit Kugeln und Würfeln, Zahlenrätsel, Fehler beim Seitenwechsel, Prüfungsaufgabe mit Dezimalzahlen.')
ST.regel('beide_seiten', 1, '', 'direkt')
ST.regel('beide_seiten', 2, 'Welche Gleichung entsteht', 'darstellung')
ST.regel('beide_seiten', 2, '', 'mehrschritt')
ST.regel('beide_seiten', 3, 'Löse 2x − 14 + 5x', 'mehrschritt', neu_s=2)
ST.regel('beide_seiten', 3, 'Löse 2,5x', 'mehrschritt', neu_s=2)
ST.regel('beide_seiten', 3, 'Kästchen', 'parameter')
ST.regel('beide_seiten', 3, 'Waage', 'transfer')
ST.regel('beide_seiten', 3, '', 'verknuepfen')
ST.neu('beide_seiten', 1, 'erkennen', ST.A('Was ist bei 5x + 3 = 2x + 12 ein sinnvoller erster Schritt?', 'auf beiden Seiten − 2x', ['auf beiden Seiten : 5', 'links − 3 und rechts + 3', 'auf beiden Seiten + 5x'],
                                           'Mit − 2x stehen alle x links: 3x + 3 = 12. „Links − 3, rechts + 3“ ist keine Äquivalenzumformung, und : 5 macht die rechte Seite unnötig schwer.',
                                           'Ziel: x nur noch auf einer Seite.'))
ST.neu('beide_seiten', 2, 'einkleidung', ST.Z('Anna hat 30 € und spart jede Woche 5 €. Ben hat 50 € und spart jede Woche 3 €. Nach wie vielen Wochen haben beide gleich viel?', 10, '(50 - 30) / (5 - 3)',
                                              '30 + 5x = 50 + 3x. Minus 3x und minus 30: 2x = 20, x = 10. Probe: 80 € = 80 € ✓.', 'Schreibe für beide den Betrag nach x Wochen auf.'))
ST.neu('beide_seiten', 3, 'fehler', ST.A('Jemand löst 7x − 4 = 3x + 8 so: „7x − 3x = 8 − 4, also 4x = 4 und x = 1.“ Was stimmt?', 'Falsch: Aus − 4 wird auf der anderen Seite + 4; richtig ist 4x = 12, x = 3.',
                                         ['Richtig.', 'Falsch: Richtig ist x = 2.', 'Falsch: Richtig ist x = −1.'],
                                         'Auf beiden Seiten + 4 rechnen: 7x = 3x + 12. Dann − 3x: 4x = 12, x = 3. Probe: 21 − 4 = 17 = 9 + 8 ✓.', 'Mache die Probe mit x = 1.'))
ST.neu('beide_seiten', 3, 'rueckwaerts', ST.Z('Lea denkt sich eine Zahl. Das Fünffache der Zahl minus 6 ist so viel wie das Doppelte der Zahl plus 9. Welche Zahl?', 5, '(9 + 6) / (5 - 2)',
                                              '5x − 6 = 2x + 9. Minus 2x: 3x − 6 = 9. Plus 6: 3x = 15, x = 5. Probe: 25 − 6 = 19 = 10 + 9 ✓.', 'Übersetze beide Seiten in Terme.'))
ST.neu('beide_seiten', 3, 'pruefung', ST.Z('Löse die Gleichung 1,2x + 0,8 = 0,4x + 4,8.', 5, '(4.8 - 0.8) / (1.2 - 0.4)', '0,8x = 4, x = 5. Probe: 6 + 0,8 = 6,8 = 2 + 4,8 ✓.', 'Bringe zuerst alle x auf die linke Seite.'))
ST.knobel('beide_seiten', ST.Z('Ich bin 24 Jahre alt und jetzt dreimal so alt, wie du warst, als ich so alt war, wie du jetzt bist. Wie alt bist du?', 16, '96 / 6',
                               'Du bist y Jahre alt, der Altersunterschied ist 24 − y. Als ich y war, war das vor 24 − y Jahren; du warst damals y − (24 − y) = 2y − 24. '
                               'Bedingung: 24 = 3(2y − 24) = 6y − 72, also 6y = 96 und y = 16. Probe: Unterschied 8; als ich 16 war, warst du 8, und 24 = 3 · 8 ✓.',
                               'Der Altersunterschied bleibt immer gleich. Gib ihm einen Namen.'))
ST.knobel('beide_seiten', ST.Z('Zwei gleich lange Kerzen werden gleichzeitig angezündet. Die erste brennt in 4 Stunden ganz ab, die zweite in 6 Stunden. Nach wie vielen Stunden ist die zweite doppelt so lang wie die erste?',
                               3, '1 / (1 / 2 - 1 / 6)',
                               'Länge 1. Nach t Stunden: erste 1 − t/4, zweite 1 − t/6. Bedingung: 1 − t/6 = 2(1 − t/4) = 2 − t/2. Also t/2 − t/6 = 1, t/3 = 1, t = 3. '
                               'Probe: erste 1/4, zweite 1/2 – doppelt so lang ✓.',
                               'Welcher Bruchteil der Kerze brennt pro Stunde ab?'))
# klammern
ST.leiter('klammern', 'Klammer ausmultiplizieren und a(x + b) = c lösen; gleichwertige Gleichung erkennen.',
          'Minusklammern, Klammern auf beiden Seiten, zwei Klammern, Kinokasse, Klammer zurückgewinnen.',
          'Produkt zweier Klammern, Fehler mit dem Vorzeichen, Kästchen, Dreieck, Zahlenrätsel rückwärts, Prüfungsaufgabe.')
ST.regel('klammern', 1, 'Löse', 'direkt')
ST.regel('klammern', 1, '', 'direkt')
ST.regel('klammern', 2, '', 'mehrschritt')
ST.regel('klammern', 3, 'Löse 7x − (4x', 'mehrschritt', neu_s=2)
ST.regel('klammern', 3, 'Löse 2(x + 1)', 'mehrschritt', neu_s=2)
ST.regel('klammern', 3, 'Löse 3(x − 2) − 2(2x', 'mehrschritt', neu_s=2)
ST.regel('klammern', 3, 'Jemand', 'fehler')
ST.regel('klammern', 3, 'Kästchen', 'parameter')
ST.regel('klammern', 3, 'Dreieck', 'transfer')
ST.regel('klammern', 3, '', 'verknuepfen')
ST.neu('klammern', 1, 'erkennen', ST.A('Welche Gleichung hat dieselbe Lösung wie 3(x + 2) = 21?', '3x + 6 = 21', ['3x + 2 = 21', 'x + 2 = 21', '3x + 6 = 63'],
                                       'Ausmultiplizieren: 3 · x + 3 · 2 = 3x + 6. Die rechte Seite bleibt 21. Beide Gleichungen haben die Lösung x = 5.', 'Multipliziere die Klammer aus.'))
ST.neu('klammern', 2, 'einkleidung', ST.Z('Drei Freunde kaufen je ein Kinoticket zu x € und je eine Cola zu 2 €. Sie zahlen zusammen 27 €. Wie teuer ist ein Ticket?', 7, '27 / 3 - 2',
                                          '3(x + 2) = 27. Durch 3: x + 2 = 9, x = 7 €.', 'Was zahlt einer der drei?', einheit='€'))
ST.neu('klammern', 2, 'umkehr', ST.Z('Ergänze: 5(x + □) = 5x + 35', 7, '35 / 5', '5 · □ = 35, also □ = 7.', 'Welche Zahl mal 5 ergibt 35?'))
ST.neu('klammern', 3, 'rueckwaerts', ST.Z('Eine Zahl wird um 4 vermindert, das Ergebnis wird verdreifacht. Man erhält 21. Wie heißt die Zahl?', 11, '21 / 3 + 4',
                                          '3(x − 4) = 21. Durch 3: x − 4 = 7, x = 11. Probe: (11 − 4) · 3 = 21 ✓.', 'Mache das Verdreifachen zuerst rückgängig.'))
ST.neu('klammern', 3, 'pruefung', ST.Z('Löse die Gleichung 2(3x − 1) − 3(x + 2) = 4.', 4, '(4 + 2 + 6) / 3', '6x − 2 − 3x − 6 = 4, also 3x − 8 = 4, 3x = 12, x = 4. Probe: 2 · 11 − 3 · 6 = 4 ✓.',
                                       'Multipliziere beide Klammern aus; achte auf − 3 · (+ 2).'))
ST.knobel('klammern', ST.Z('Löse: 1(x − 1) + 2(x − 2) + 3(x − 3) + 4(x − 4) = 0', 3, '(1 + 4 + 9 + 16) / 10',
                           'Ausmultiplizieren: x + 2x + 3x + 4x = 10x und 1 + 4 + 9 + 16 = 30. Also 10x − 30 = 0 und x = 3. '
                           'Probe: 1 · 2 + 2 · 1 + 3 · 0 + 4 · (−1) = 2 + 2 + 0 − 4 = 0 ✓.',
                           'Sammle die x-Glieder und die Zahlen getrennt.'))
ST.knobel('klammern', ST.Z('Diophant war ein Sechstel seines Lebens Kind, ein Zwölftel Jugendlicher und ein Siebtel unverheiratet. 5 Jahre nach der Hochzeit kam sein Sohn, der halb so alt wurde wie Diophant. 4 Jahre nach dem Sohn starb Diophant. Wie alt wurde er?',
                           84, '9 / (1 - (1 / 6 + 1 / 12 + 1 / 7 + 1 / 2))',
                           'Lebensalter x: x/6 + x/12 + x/7 + 5 + x/2 + 4 = x. Hauptnenner 84: 14x + 7x + 12x + 42x = 75x, also 75x/84 + 9 = x. '
                           'Dann x − 75x/84 = 9x/84 = 9 und x = 84. Probe: 14 + 7 + 12 + 5 + 42 + 4 = 84 ✓.',
                           'Zerlege das Leben in alle genannten Abschnitte. Zusammen ergeben sie das ganze Leben.'))
# probe
ST.leiter('probe', 'Einsetzen und prüfen, ob eine Zahl Lösung ist; Sinn der Probe erkennen.',
          'Fehlerzeile in einer Rechnung finden, Probe richtig aufschreiben, Kandidaten testen, Stiftepackungen.',
          'Unzulässige Umformungen (· 0, falsch geteilt, Quadrieren) begründen, Fehler finden und korrigieren, Kästchen, Prüfungsaufgabe mit Auswahl.')
ST.regel('probe', 1, '', 'direkt')
ST.regel('probe', 2, 'Die Probe für', 'darstellung')
ST.regel('probe', 2, '', 'mehrschritt')
ST.regel('probe', 3, 'multipliziert', 'begruenden')
ST.regel('probe', 3, 'Quadrieren', 'begruenden')
ST.regel('probe', 3, 'Kästchen', 'parameter')
ST.regel('probe', 3, 'Wie heißt die richtige Lösung', 'verknuepfen')
ST.regel('probe', 3, '', 'fehler')
ST.neu('probe', 1, 'erkennen', ST.A('Was macht man bei der Probe einer Gleichung?', 'Man setzt die Lösung in beide Seiten der ursprünglichen Gleichung ein und vergleicht.',
                                    ['Man rechnet die Umformungen noch einmal rückwärts.', 'Man setzt die Lösung nur in die letzte Zeile ein.', 'Man prüft, ob die Lösung positiv ist.'],
                                    'Nur die ursprüngliche Gleichung zeigt, ob die Zahl wirklich passt. Ein Fehler in einer Umformung würde sich in der letzten Zeile nicht zeigen.',
                                    'In welche Gleichung muss man einsetzen, damit auch Umformungsfehler auffallen?'))
ST.neu('probe', 2, 'einkleidung', ST.A('Mia hat 4 volle Packungen Stifte und 3 einzelne Stifte, zusammen 39 Stifte. Sie sagt: „In einer Packung sind 9 Stifte.“ Stimmt das?', 'Ja: 4 · 9 + 3 = 39.',
                                       ['Nein: 4 · 9 + 3 = 40.', 'Nein: Es sind 9,75 Stifte.', 'Ja: 39 : 4 ≈ 9.'],
                                       'Gleichung 4x + 3 = 39. Probe mit x = 9: 36 + 3 = 39 ✓. Die Antwort „39 : 4 ≈ 9“ vergisst die 3 einzelnen Stifte.', 'Setze 9 in die Gleichung 4x + 3 = 39 ein.'))
ST.neu('probe', 3, 'pruefung', ST.A('Welche der Zahlen −3, −1, 1, 3 ist eine Lösung von 2(x − 1) = 5x + 7?', '−3', ['−1', '1', '3'],
                                    'x = −3: links 2 · (−4) = −8, rechts −15 + 7 = −8 ✓. Bei −1: −4 und 2; bei 1: 0 und 12; bei 3: 4 und 22.', 'Setze jede Zahl in beide Seiten ein.'))
ST.knobel('probe', ST.Z('Die Gleichung ax + 6 = 2x + b hat die Lösungen x = 1 und x = 2. Wie groß ist a + b?', 8, '2 + 6',
                        'Eine Gleichung dieser Form hat genau eine, keine oder unendlich viele Lösungen. Mit zwei Lösungen muss sie unendlich viele haben: Beide Seiten sind gleich, also a = 2 und b = 6. '
                        'Probe: 2x + 6 = 2x + 6 gilt für 1 und 2 ✓. a + b = 8.',
                        'Wie viele Lösungen kann eine solche Gleichung überhaupt haben?'))
ST.knobel('probe', ST.Z('x = 3 ist eine Lösung von ax − 4 = 2x + a. Wie groß ist a?', 5, '(6 + 4) / (3 - 1)',
                        'Setze x = 3 ein: 3a − 4 = 6 + a. Jetzt ist a die Unbekannte: 2a = 10, a = 5. Probe: 15 − 4 = 11 und 6 + 5 = 11 ✓.',
                        'Setze die bekannte Lösung ein. Was ist dann noch unbekannt?'))
# sonderfaelle
ST.leiter('sonderfaelle', 'Erkennen, ob eine Gleichung keine, eine oder unendlich viele Lösungen hat.',
          'Lösungsmenge angeben, Kästchen für unendlich viele Lösungen, Handytarife ohne Treffpunkt.',
          'Tarif-Deutung, Parameter für keine oder unendlich viele Lösungen, Grundmenge, Fehler „L = {6}“, Gleichung ohne Lösung begründen.')
ST.regel('sonderfaelle', 1, '(x', 'direkt')
ST.regel('sonderfaelle', 1, '', 'erkennen')
ST.regel('sonderfaelle', 2, 'Welche Zahl muss', 'umkehr')
ST.regel('sonderfaelle', 2, '', 'mehrschritt')
ST.regel('sonderfaelle', 3, 'Tarif', 'transfer')
ST.regel('sonderfaelle', 3, 'Welche Zahl muss', 'parameter')
ST.regel('sonderfaelle', 3, 'Für welchen Wert', 'parameter')
ST.regel('sonderfaelle', 3, 'Grundmenge', 'begruenden')
ST.regel('sonderfaelle', 3, 'KEINE', 'begruenden')
ST.regel('sonderfaelle', 3, 'Bestimme die Lösungsmenge von', 'verknuepfen')
ST.neu('sonderfaelle', 2, 'einkleidung', ST.A('Handytarif A kostet 5 € Grundgebühr und 0,10 € pro Minute, Tarif B 8 € Grundgebühr und 0,10 € pro Minute. Bei wie vielen Minuten kosten beide gleich viel?',
                                              'nie: B ist immer 3 € teurer', ['bei 30 Minuten', 'bei 3 Minuten', 'immer'],
                                              '5 + 0,1x = 8 + 0,1x führt zu 5 = 8 – falsch. Die Gleichung hat keine Lösung: Pro Minute kosten beide gleich viel, B bleibt immer 3 € teurer.',
                                              'Stelle die Gleichung auf und vereinfache.'))
ST.neu('sonderfaelle', 3, 'fehler', ST.A('Jemand formt 2(x + 3) = 2x + 6 um und erhält 6 = 6. Er schreibt: „L = {6}.“ Was stimmt?', 'Falsch: 6 = 6 ist immer wahr, also ist jede Zahl Lösung: L = ℚ.',
                                         ['Richtig.', 'Falsch: L = { }.', 'Falsch: L = {0}.'],
                                         'Das x ist verschwunden, und die Aussage 6 = 6 stimmt für jedes x. Die 6 ist keine Lösung für x, sondern nur das, was übrig bleibt.',
                                         'Probiere x = 1 in der Ausgangsgleichung.'))
ST.knobel('sonderfaelle', ST.Z('Für welche Zahl a hat die Gleichung a · (a · x − 1) = 4x − 2 unendlich viele Lösungen?', 2, '0 - (-2)',
                               'Ausmultipliziert: a²x − a = 4x − 2. Unendlich viele Lösungen gibt es nur, wenn beide Seiten gleich sind: a² = 4 und a = 2. '
                               'a² = 4 gilt für a = 2 und a = −2. Bei a = −2 steht aber 4x + 2 = 4x − 2 da – keine Lösung. Nur a = 2 passt: 4x − 2 = 4x − 2.',
                               'Vergleiche die x-Glieder und die Zahlen beider Seiten getrennt. Prüfe jeden Kandidaten.'))
ST.knobel('sonderfaelle', ST.A('Lisa sagt: „Ich habe eine Gleichung der Form ax + b = cx + d gefunden, die genau zwei Lösungen hat.“ Kann das stimmen?',
                               'Nein: Wer zwei Lösungen hat, hat sogar unendlich viele.', ['Ja, z. B. wenn a = c ist.', 'Ja, wenn b und d negativ sind.', 'Nein: Jede solche Gleichung hat genau eine Lösung.'],
                               'Umgeformt: (a − c)x = d − b. Ist a ≠ c, gibt es genau eine Lösung. Ist a = c, steht 0 = d − b da: entweder immer wahr (unendlich viele) oder nie (keine). '
                               'Genau zwei Lösungen sind also unmöglich.',
                               'Bringe alle x auf eine Seite und unterscheide die Fälle.'))
# sach
ST.leiter('sach', 'Einfache Sachaufgabe mit einer Gleichung lösen; passende Gleichung erkennen.',
          'Alter, Pfand, Sparen, Kino, Seil, Zahlenfolgen; Gleichung zu einer Situation auswählen.',
          'Geld rückwärts, Ergebnis deuten, Tarife, Züge, Kanister, Theaterkasse, Gehege, Altersrätsel, Prüfungsaufgabe Klassenfahrt.')
ST.regel('sach', 1, 'Welche Gleichung passt', 'erkennen')
ST.regel('sach', 1, '', 'direkt')
ST.regel('sach', 2, 'Fünfecks', 'mehrschritt')
ST.regel('sach', 2, 'ganzer Zahlen', 'mehrschritt')
ST.regel('sach', 2, '', 'einkleidung')
ST.regel('sach', 3, 'Hälfte', 'rueckwaerts')
ST.regel('sach', 3, 'Was folgt', 'begruenden')
ST.regel('sach', 3, 'Welche G', 'begruenden')
ST.regel('sach', 3, 'Tarif', 'transfer')
ST.regel('sach', 3, 'Zug', 'transfer')
ST.regel('sach', 3, 'Gehege', 'transfer')
ST.regel('sach', 3, '', 'verknuepfen')
ST.neu('sach', 2, 'darstellung', ST.A('Ein Bus hat 52 Plätze. Es sitzen dreimal so viele Erwachsene wie Kinder darin, 8 Plätze bleiben frei. Welche Gleichung passt (x = Zahl der Kinder)?',
                                      'x + 3x + 8 = 52', ['3x + 8 = 52', 'x + 3x = 52 + 8', 'x + 3x − 8 = 52'],
                                      'Kinder x, Erwachsene 3x, freie Plätze 8 – zusammen alle 52 Plätze. Lösung: 4x = 44, x = 11 Kinder.', 'Was ergibt zusammen alle 52 Plätze?'))
ST.neu('sach', 3, 'pruefung', ST.Z('Für einen Ausflug zahlt jedes der 24 Kinder gleich viel. Der Bus kostet 336 €, der Eintritt 5 € pro Kind. Wie viel zahlt jedes Kind?', 19, '(336 + 24 * 5) / 24',
                                   '24x = 336 + 24 · 5 = 456, also x = 19 €. Oder: 336 : 24 = 14 € Bus pro Kind, plus 5 € Eintritt.', 'Welche Kosten fallen insgesamt an?', einheit='€'))
ST.knobel('sach', ST.Z('Auf einem Hof gibt es Hühner und Kaninchen, zusammen 30 Köpfe und 84 Beine. Wie viele Kaninchen sind es?', 12, '(84 - 2 * 30) / 2',
                       'Stell dir vor, alle 30 Tiere stehen auf zwei Beinen: 60 Beine. Es fehlen 24 Beine – jedes Kaninchen hat 2 mehr, also 12 Kaninchen. '
                       'Mit Gleichung: 2(30 − k) + 4k = 84, 60 + 2k = 84, k = 12. Probe: 18 Hühner (36 Beine) + 12 Kaninchen (48 Beine) = 84 ✓.',
                       'Was wäre, wenn alle Tiere Hühner wären?'))
ST.knobel('sach', ST.Z('Ein Wanderer geht eine Strecke hin mit 4 km/h und auf demselben Weg zurück mit 6 km/h. Insgesamt braucht er 5 Stunden. Wie lang ist die Strecke (einfach)?', 12, '5 / (1 / 4 + 1 / 6)',
                       'Für s km braucht er hin s/4 Stunden und zurück s/6 Stunden. s/4 + s/6 = 5. Hauptnenner 12: 3s/12 + 2s/12 = 5s/12 = 5, also s = 12 km. '
                       'Probe: 3 h hin + 2 h zurück = 5 h ✓. (Die Durchschnittsgeschwindigkeit ist 24 km : 5 h = 4,8 km/h, nicht 5 km/h.)',
                       'Wie lange braucht er für einen Kilometer hin und für einen zurück?', einheit='km'))
# ---- STUFEN ENDE ----


if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Umformen', ['waage', 'beide_seiten', 'klammern']), ('Prüfen und Sonderfälle', ['probe', 'sonderfaelle']), ('Anwenden', ['sach'])],
         'Lineare Gleichungen mit Äquivalenzumformungen lösen – auch mit Klammern und x auf beiden Seiten –, die Probe machen, Sonderfälle erkennen und Sachaufgaben lösen.',
         ['Äquivalenzumformung: auf beiden Seiten dasselbe tun (mal/geteilt nie mit 0).', 'Erst Klammern auflösen, dann x-Glieder auf eine Seite, Zahlen auf die andere.',
          'Minus vor der Klammer dreht alle Vorzeichen in der Klammer um.', 'x fällt weg: falsche Aussage → L = { }, wahre Aussage → L = ℚ.',
          'Probe in der ursprünglichen Gleichung; Lösung im Sachzusammenhang deuten.'],
         offen=['Lehrplanbezug: lehrplan_gym ist leer; umgesetzt nach „umfang“. Grundmenge ℚ (Klasse 7); Brüche als Lösung über Lücken □/□.',
                'Bruchgleichungen (x im Nenner) und Ungleichungen gehören zu gleichungen.bruch bzw. gleichungen.ungleichungen (Kl. 8) und sind weggelassen.'],
         teil=TEIL)
    anhaengen(META['thema_schluessel'], schwer())
    befunde_datei(META['thema_schluessel'], BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden
    durchsicht_datei(META['thema_schluessel'], DS)  # Neunzehnte Runde: zuletzt
    stufen_datei(META['thema_schluessel'], ST)  # Zwanzigste Runde: zuletzt
