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
