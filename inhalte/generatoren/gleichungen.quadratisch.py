#!/usr/bin/env python3
"""Thema gleichungen.quadratisch – Quadratische Gleichungen (allgemein), Klasse 9."""
import sys
from math import isqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(904)
L2 = 'x₁ = □; x₂ = □'
H2 = 'kleinere Lösung zuerst'


def nz(n):
    return R.choice([i for i in range(-n, n + 1) if i != 0])


def wurzel_c(a, b, c):
    """Rechenausdrücke der beiden Lösungen (kleinere zuerst) über die Lösungsformel."""
    D = b * b - 4 * a * c
    s = isqrt(D)
    assert s * s == D
    x1, x2 = Fr(-b - s, 2 * a), Fr(-b + s, 2 * a)
    e1, e2 = f'(-({b}) - {s}) / (2 * {a})', f'(-({b}) + {s}) / (2 * {a})'
    return (x1, x2, e1, e2) if x1 <= x2 else (x2, x1, e2, e1)


ETAPPEN = [
    {'lernziel': 'reinquadratisch', 'titel': 'Gleichungen ohne x-Glied lösen',
     'regel': 'Bei ax² + c = 0 stellst du nach ⟦x²⟧ um. Ist x² = d mit d > 0, gibt es ⟦zwei Lösungen ±√d⟧; bei d = 0 eine, bei d < 0 ⟦keine⟧.',
     'schritte': ['3x² − 75 = 0 | + 75, dann : 3 ergibt x² = 25.', 'x₁ = ⟦−5⟧ und x₂ = ⟦5⟧.'],
     'probe': '3 · (−5)² − 75 = 75 − 75 = 0 ✓',
     'fehler': 'x² = 25 ⇒ x = 5 ist unvollständig: Auch (−5)² = 25. Die Lösungsmenge ist ⟦{−5; 5}⟧.'},
    {'lernziel': 'ausklammern', 'titel': 'Gleichungen ohne Zahlglied lösen',
     'regel': 'Bei ax² + bx = 0 ⟦klammerst du x aus⟧: x(ax + b) = 0. Ein Produkt ist null, wenn ein ⟦Faktor null⟧ ist (Satz vom Nullprodukt).',
     'schritte': ['2x² − 12x = 0 ⇔ x(2x − 12) = 0.', 'x = 0 oder 2x − 12 = 0, also ⟦x₁ = 0, x₂ = 6⟧.'],
     'probe': '2 · 6² − 12 · 6 = 72 − 72 = 0 ✓',
     'fehler': '2x² = 12x | : x ergibt nur x = 6 – dabei geht die Lösung ⟦x = 0⟧ verloren. Nie durch x teilen, sondern ausklammern.'},
    {'lernziel': 'faktorisieren', 'titel': 'Faktorisieren und Nullprodukt',
     'regel': 'Steht die Gleichung als ⟦Produkt = 0⟧, liest du die Lösungen ab: (x − p)(x − q) = 0 ⇔ ⟦x = p oder x = q⟧. Binomische Formeln helfen beim Faktorisieren.',
     'schritte': ['x² − 8x + 16 = 0: 2. binomische Formel, also (x − 4)² = 0.', 'Nur x − 4 = 0, also eine Lösung: ⟦x = 4⟧.'],
     'probe': '4² − 8 · 4 + 16 = 16 − 32 + 16 = 0 ✓',
     'fehler': '(x + 3)(x − 2) = 0 ⇒ x = 3 oder x = −2 ist falsch: Die ⟦Vorzeichen drehen sich um⟧. Richtig: x = −3 oder x = 2.'},
    {'lernziel': 'ergaenzung', 'titel': 'Quadratische Ergänzung',
     'regel': 'Bei x² + bx + c = 0 ergänzt du ⟦(b/2)²⟧ auf beiden Seiten, sodass links ⟦(x + b/2)²⟧ steht. Dann wie bei x² = d weiterrechnen.',
     'schritte': ['x² + 6x − 7 = 0 ⇔ x² + 6x + 9 = 7 + 9.', '(x + 3)² = 16 ⇒ x + 3 = ±4 ⇒ ⟦x₁ = −7, x₂ = 1⟧.'],
     'probe': '1² + 6 · 1 − 7 = 0 ✓',
     'fehler': 'x² + 6x − 7 = 0 ⇒ (x + 6)² = 7 ist falsch: In die Klammer gehört die ⟦Hälfte⟧ von 6, und (b/2)² = 9 muss auf ⟦beiden Seiten⟧ ergänzt werden.'},
    {'lernziel': 'loesungsformel', 'titel': 'Die Lösungsformel anwenden',
     'regel': 'Für ax² + bx + c = 0 (a ≠ 0) gilt ⟦x₁,₂ = (−b ± √(b² − 4ac)) / (2a)⟧. Den Term ⟦D = b² − 4ac⟧ unter der Wurzel heißt Diskriminante.',
     'schritte': ['2x² − 5x − 3 = 0: a = 2, b = −5, c = −3. D = 25 + 24 = 49.', 'x₁,₂ = (5 ± 7) / 4, also ⟦x₁ = −0,5; x₂ = 3⟧.'],
     'probe': '2 · 3² − 5 · 3 − 3 = 18 − 15 − 3 = 0 ✓',
     'fehler': 'Bei b = −5 ist −b = −5 falsch: Minus mal Minus ergibt ⟦−b = 5⟧. Auch b² = (−5)² = 25, nicht −25.'},
    {'lernziel': 'diskriminante', 'titel': 'Wie viele Lösungen gibt es?',
     'regel': 'Die Diskriminante entscheidet: ⟦D > 0⟧ zwei Lösungen, ⟦D = 0⟧ genau eine, ⟦D < 0⟧ keine Lösung.',
     'schritte': ['x² − 4x + 7 = 0: D = (−4)² − 4 · 1 · 7 = 16 − 28 = −12.', 'D < 0, also ⟦keine Lösung⟧.'],
     'probe': 'Quadratische Ergänzung: (x − 2)² + 3 = 0 – links steht immer mindestens 3 ✓',
     'fehler': '„D = −12, also zwei Lösungen, weil man ± rechnet“ ist falsch: Aus einer ⟦negativen⟧ Zahl gibt es keine Quadratwurzel.'},
    {'lernziel': 'sachaufgabe', 'titel': 'Sachaufgaben lösen',
     'regel': 'Variable festlegen, ⟦Gleichung aufstellen⟧, lösen und die Lösungen am ⟦Sachzusammenhang prüfen⟧ (z. B. keine negativen Längen).',
     'schritte': ['Ein Rechteck ist 4 cm länger als breit und hat 45 cm² Fläche: x(x + 4) = 45 ⇔ x² + 4x − 45 = 0.',
                  'Lösungen x = −9 und x = 5; nur ⟦x = 5⟧ ist eine Länge. Das Rechteck ist 5 cm breit und 9 cm lang.'],
     'probe': '5 cm · 9 cm = 45 cm² ✓',
     'fehler': 'Die Lösung x = −9 als Breite anzugeben ist falsch: Längen sind ⟦positiv⟧. Diese Lösung passt nicht zum Sachzusammenhang.'},
]


def g_reinquadratisch(s):
    if s == 1:
        r = R.randint(2, 15)
        if R.random() < 0.5:
            return luecken(f'Löse x² = {r * r}.', L2, H2, [-r, r], f'x = ±√{r * r}, also x₁ = −{r}, x₂ = {r}.',
                           'Denke an beide Vorzeichen.', c=[f'-{r * r} / {r}', f'{r * r} / {r}'])
        return luecken(f'Löse x² − {r * r} = 0.', L2, H2, [-r, r], f'x² = {r * r}, also x = ±{r}.',
                       'Bringe die Zahl auf die andere Seite.', c=[f'-{r * r} / {r}', f'{r * r} / {r}'])
    if s == 2:
        a, r = R.randint(2, 6), R.randint(1, 10)
        k = a * r * r
        if R.random() < 0.3:
            return auswahl(f'Welche Lösungsmenge hat {a}x² + {k} = 0?', 'L = { }', [f'L = {{−{r}; {r}}}', f'L = {{{r}}}', f'L = {{−{r}}}'],
                           f'{a}x² = −{k} ⇔ x² = −{r * r}. Ein Quadrat ist nie negativ, also keine Lösung.',
                           'Stelle nach x² um. Kann ein Quadrat negativ sein?')
        return luecken(f'Löse {a}x² − {k} = 0.', L2, H2, [-r, r], f'{a}x² = {k} ⇔ x² = {r * r}, also x = ±{r}.',
                       'Erst nach x² auflösen, dann die Wurzel ziehen.', c=[f'-({k} / {a}) / {r}', f'({k} / {a}) / {r}'])
    p, r = nz(9), R.randint(1, 8)
    x1, x2 = p - r, p + r
    if R.random() < 0.3:
        return auswahl(f'Welche Lösungsmenge hat {minus_klammer(p)}² = {-r * r}?', 'L = { }',
                       [f'L = {{{dz(x1)}; {dz(x2)}}}', f'L = {{{dz(p)}}}', f'L = {{{dz(-r)}; {dz(r)}}}'],
                       f'Ein Quadrat kann nicht {-r * r} ergeben, also keine Lösung.', 'Kann ein Quadrat negativ sein?')
    return luecken(f'Löse {minus_klammer(p)}² = {r * r}.', L2, H2, [x1, x2],
                   f'{minus_klammer(p)[1:-1]} = ±{r}, also x₁ = {dz(p)} − {r} = {dz(x1)}, x₂ = {dz(p)} + {r} = {dz(x2)}.',
                   'Ziehe zuerst die Wurzel: Die Klammer ist ± die Wurzel.', c=[f'{p} - {r * r} / {r}', f'{p} + {r * r} / {r}'])


def g_ausklammern(s):
    if s == 1:
        b = nz(12)
        return luecken(f'Löse x² {plus_v(b)} = 0.', L2, H2, sorted([0, -b]), f'x(x {plus(b)}) = 0, also x = 0 oder x = {dz(-b)}.',
                       'Klammere x aus.', c=[f'min(0, -({b}))', f'max(0, -({b}))'])
    a, x2 = R.randint(2, 7), nz(9)
    b = -a * x2
    if s == 2:
        return luecken(f'Löse {poly(a, b, 0)} = 0.', L2, H2, sorted([0, x2]),
                       f'x({a}x {plus(b)}) = 0, also x = 0 oder {a}x = {dz(-b)}, x = {dz(x2)}.',
                       'Klammere x aus und setze jeden Faktor gleich null.', c=[f'min(0, -({b}) / {a})', f'max(0, -({b}) / {a})'])
    if R.random() < 0.5:
        return luecken(f'Löse {a}x² = {poly(-b, 0)}.', L2, H2, sorted([0, x2]),
                       f'{poly(a, b, 0)} = 0 ⇔ x({a}x {plus(b)}) = 0, also x = 0 oder x = {dz(x2)}.',
                       'Bringe alles auf eine Seite – nicht durch x teilen!', c=[f'min(0, -({b}) / {a})', f'max(0, -({b}) / {a})'])
    return auswahl(f'Jemand löst {a}x² = {poly(-b, 0)}, indem er durch x teilt, und erhält x = {dz(x2)}. Was stimmt?',
                   f'Unvollständig: Auch x = 0 ist eine Lösung.',
                   ['Richtig, das ist die einzige Lösung.', f'Falsch: Die Lösung ist x = {dz(-x2)}.', f'Falsch: Die Lösung ist x = {dz(x2 * a)}.'],
                   f'Durch x teilen ist nur für x ≠ 0 erlaubt. Ausklammern: x({a}x {plus(b)}) = 0 liefert x = 0 und x = {dz(x2)}.',
                   'Was passiert beim Teilen durch x mit der Möglichkeit x = 0?')


def g_faktorisieren(s):
    if s == 1:
        p, q = nz(9), nz(9)
        if p == q: return None
        lo, hi = sorted([p, q])
        return luecken(f'Löse {minus_klammer(p)} · {minus_klammer(q)} = 0.', L2, H2, [lo, hi],
                       f'Satz vom Nullprodukt: {minus_klammer(p)[1:-1]} = 0 oder {minus_klammer(q)[1:-1]} = 0, also x = {dz(p)} oder x = {dz(q)}.',
                       'Wann ist ein Produkt null?', c=[f'min({p}, {q})', f'max({p}, {q})'])
    if s == 2:
        p = nz(12)
        if R.random() < 0.5:
            return luecken(f'Löse {poly(1, -2 * p, p * p)} = 0.', 'x = □', 'die einzige Lösung', [p],
                           f'Binomische Formel: {minus_klammer(p)}² = 0, also x = {dz(p)}.',
                           'Erkennst du eine binomische Formel?', c=[f'-({-2 * p}) / 2'])
        a, r = R.randint(1, 5), R.randint(1, 10)
        return luecken(f'Löse {poly(a * a, 0, -r * r)} = 0 durch Faktorisieren.', L2, H2, [Fr(-r, a), Fr(r, a)] if r % a == 0 else [0, 0],
                       f'3. binomische Formel: ({a if a > 1 else ""}x − {r})({a if a > 1 else ""}x + {r}) = 0, also x = ±{br(Fr(r, a))}.',
                       'Erkennst du die 3. binomische Formel?', c=[f'-{r} / {a}', f'{r} / {a}']) if r % a == 0 else None
    p, q = nz(9), nz(9)
    if p == q: return None
    b, c = -(p + q), p * q
    lo, hi = sorted([p, q])
    return luecken(f'Löse {poly(1, b, c)} = 0. Tipp: Faktorisiere in (x − p)(x − q).', L2, H2, [lo, hi],
                   f'Gesucht p, q mit p + q = {dz(p + q)} und p · q = {dz(c)}: p = {dz(lo)}, q = {dz(hi)}. ({minus_klammer(lo)[1:-1]})({minus_klammer(hi)[1:-1]}) = 0.',
                   'Suche zwei Zahlen, deren Produkt das Zahlglied und deren Summe die Gegenzahl von b ist.',
                   c=[wurzel_c(1, b, c)[2], wurzel_c(1, b, c)[3]])


def g_ergaenzung(s):
    h = nz(8)
    b = 2 * h
    d = R.randint(1, 10)
    if s < 3:
        if s == 1:
            r = d
            d = r * r
        c = h * h - d
        rechts = d
        if h > 0:
            sch = '(x + □)² = □'
            werte = [h, rechts]
        else:
            sch = '(x − □)² = □'
            werte = [-h, rechts]
        return luecken(f'Bringe {poly(1, b, c)} = 0 mit quadratischer Ergänzung auf die Form {sch.replace("□", "…")}.', sch,
                       'Zahl in der Klammer, Zahl rechts', werte,
                       f'Hälfte von {dz(b)} ist {dz(h)}, ergänze {dz(h * h)}: {poly(1, b, h * h)} = {dz(-c)} + {dz(h * h)}, also {minus_klammer(-h)}² = {dz(rechts)}.',
                       'Halbiere den Koeffizienten von x und quadriere ihn.', c=[f'abs({b}) / 2', f'({b} / 2) ** 2 - ({c})'])
    r = R.randint(1, 9)
    c = h * h - r * r
    x1, x2, e1, e2 = wurzel_c(1, b, c)
    return luecken(f'Löse {poly(1, b, c)} = 0 mit quadratischer Ergänzung.', L2, H2, [x1, x2],
                   f'{minus_klammer(-h)}² = {dz(-c)} + {dz(h * h)} = {r * r}, also x {plus(h)} = ±{r}: x₁ = {dz(x1)}, x₂ = {dz(x2)}.',
                   'Ergänze (b/2)² auf beiden Seiten, dann Wurzel ziehen.', c=[e1, e2])


def g_loesungsformel(s):
    if s == 1:
        a, b, c = nz(5), nz(9), nz(12)
        D = b * b - 4 * a * c
        return zahl(f'Berechne die Diskriminante von {poly(a, b, c)} = 0.', f'D = b² − 4ac = {kl(b)}² − 4 · {kl(a)} · {kl(c)} = {dz(b * b)} {plus(-4 * a * c)} = {dz(D)}.',
                    'Lies a, b und c mit Vorzeichen ab und setze in b² − 4ac ein.', D, f'({b}) ** 2 - 4 * ({a}) * ({c})')
    if s == 2:
        a = R.choice([1, 1, 2, 3, -1, -2])
        p, q = nz(7), nz(7)
        if p == q: return None
        b, c = -a * (p + q), a * p * q
        x1, x2, e1, e2 = wurzel_c(a, b, c)
        D = b * b - 4 * a * c
        return luecken(f'Löse {poly(a, b, c)} = 0 mit der Lösungsformel.', L2, H2, [x1, x2],
                       f'a = {dz(a)}, b = {dz(b)}, c = {dz(c)}; D = {dz(D)}, √D = {isqrt(D)}; x₁,₂ = ({dz(-b)} ± {isqrt(D)}) / {dz(2 * a)}: {dz(x1)} und {dz(x2)}.',
                       'Erst a, b, c ablesen, dann D berechnen.', c=[e1, e2])
    a = R.choice([2, 4, -2])
    p = Fr(nz(9), 2)
    if p.denominator == 1: return None
    q = nz(6)
    b = -a * (p + q)
    c = a * p * q
    if b.denominator != 1 or c.denominator != 1: return None
    b, c = int(b), int(c)
    x1, x2, e1, e2 = wurzel_c(a, b, c)
    return zahl(f'Löse {poly(a, b, c)} = 0 mit der Lösungsformel. Gib die größere Lösung an.',
                f'D = {dz(b * b - 4 * a * c)}, √D = {isqrt(b * b - 4 * a * c)}; x₁ = {dz(x1)}, x₂ = {dz(x2)}. Größere Lösung: {dz(x2)}.',
                'Setze sorgfältig mit Vorzeichen in die Lösungsformel ein.', x2, e2)


def g_diskriminante(s):
    if s == 1 or (s == 2 and R.random() < 0.5):
        a, b, c = nz(4), nz(8), nz(10)
        D = b * b - 4 * a * c
        n = 'zwei Lösungen' if D > 0 else 'genau eine Lösung' if D == 0 else 'keine Lösung'
        return auswahl(f'Wie viele Lösungen hat {poly(a, b, c)} = 0?', n, ['zwei Lösungen', 'genau eine Lösung', 'keine Lösung'],
                       f'D = {kl(b)}² − 4 · {kl(a)} · {kl(c)} = {dz(D)}{" > 0" if D > 0 else " < 0" if D < 0 else ""}, also {n}.',
                       'Berechne D = b² − 4ac und achte auf das Vorzeichen.')
    if s == 2:
        h = R.randint(1, 10)
        b = 2 * h * R.choice([1, -1])
        return zahl(f'Für welche Zahl c hat x² {plus_v(b)} + c = 0 genau eine Lösung?', f'Genau eine Lösung bei D = 0: {dz(b * b)} − 4c = 0, also c = {dz(h * h)}.',
                    'Setze die Diskriminante gleich null.', h * h, f'({b}) ** 2 / 4')
    if R.random() < 0.5:
        h = R.randint(2, 9)
        c = h * h
        return zahl(f'Für welche positive Zahl k hat x² + kx + {c} = 0 genau eine Lösung?',
                    f'D = k² − 4 · {c} = 0 ⇔ k² = {4 * c} ⇔ k = ±{2 * h}; positiv: k = {2 * h}.',
                    'Setze D = 0 und löse nach k.', 2 * h, f'(4 * {c}) / ({2 * h})')
    a, b, c = R.randint(1, 4), nz(6), R.randint(1, 10)
    D = b * b - 4 * a * c
    if D >= 0: return None
    return auswahl(f'Jemand sagt: „{poly(a, b, c)} = 0 hat zwei Lösungen, weil die Lösungsformel ± enthält.“ Was stimmt?',
                   f'Falsch: D = {dz(D)} < 0, es gibt keine Lösung.',
                   ['Richtig: Wegen ± gibt es immer zwei Lösungen.', f'Falsch: Es gibt genau eine Lösung x = {br(Fr(-b, 2 * a))}.',
                    f'Richtig: D = {dz(-D)} > 0.'],
                   f'D = {kl(b)}² − 4 · {a} · {c} = {dz(D)}. Aus einer negativen Zahl gibt es keine Wurzel, also keine Lösung.',
                   'Berechne zuerst die Diskriminante.')


def g_sachaufgabe(s):
    typ = R.random()
    if s == 1:
        x = R.randint(3, 20)
        return zahl(f'Das Quadrat einer positiven Zahl ist {dz(x * x)}. Wie heißt die Zahl?', f'x² = {dz(x * x)}, x = ±{x}; positiv: x = {x}.',
                    'Stelle die Gleichung x² = … auf.', x, f'{x * x} / {x}')
    if s == 2:
        x, d = R.randint(3, 15), R.randint(1, 8)
        A = x * (x + d)
        return zahl(f'Ein Rechteck ist {d} cm länger als breit und hat einen Flächeninhalt von {dz(A)} cm². Wie breit ist es?',
                    f'x(x + {d}) = {dz(A)} ⇔ {poly(1, d, -A)} = 0. Lösungen {dz(-x - d)} und {x}; Breite {x} cm.',
                    'Breite x, Länge x + ' + str(d) + '. Flächeninhalt = Länge · Breite.', x, wurzel_c(1, d, -A)[3], einheit='cm')
    if typ < 0.35:
        n = R.randint(3, 30)
        p = n * (n + 1)
        return zahl(f'Das Produkt zweier aufeinanderfolgender positiver ganzer Zahlen ist {dz(p)}. Wie heißt die kleinere Zahl?',
                    f'x(x + 1) = {dz(p)} ⇔ x² + x − {dz(p)} = 0. Lösungen {dz(-n - 1)} und {n}; positiv: {n}.',
                    'Nenne die kleinere Zahl x. Wie heißt die nächste Zahl?', n, wurzel_c(1, 1, -p)[3])
    if typ < 0.7:
        a, b, w = R.randint(6, 20), R.randint(4, 15), R.randint(1, 4)
        A = (a + 2 * w) * (b + 2 * w) - a * b
        return zahl(f'Um ein rechteckiges Beet ({a} m × {b} m) wird ein gleich breiter Weg gelegt. Der Weg hat {dz(A)} m² Fläche. Wie breit ist er?',
                    f'({a} + 2x)({b} + 2x) − {a * b} = {dz(A)} ⇔ {poly(4, 2 * (a + b), -A)} = 0. Positive Lösung x = {w}.',
                    'Ganze Fläche mit Weg minus Beetfläche = Wegfläche.', w, wurzel_c(4, 2 * (a + b), -A)[3], einheit='m')
    t = R.randint(2, 6)
    v = 5 * t + R.randint(0, 4) * 5
    h = v * t - 5 * t * t
    if h <= 0: return None
    return zahl(f'Ein Ball wird senkrecht nach oben geworfen. Seine Höhe über dem Abwurfpunkt ist h(t) = {v}t − 5t² (t in s, h in m). Nach wie vielen Sekunden ist er zum ersten Mal {dz(h)} m hoch?',
                f'{v}t − 5t² = {dz(h)} ⇔ 5t² − {v}t + {dz(h)} = 0. Lösungen t = {dz(wurzel_c(5, -v, h)[0])} und t = {dz(wurzel_c(5, -v, h)[1])}; zuerst bei {dz(wurzel_c(5, -v, h)[0])} s.',
                'Setze h(t) gleich der Höhe und bringe alles auf eine Seite. Zum ersten Mal = kleinere Lösung.',
                wurzel_c(5, -v, h)[0], wurzel_c(5, -v, h)[2], einheit='s')


GEN = {'reinquadratisch': g_reinquadratisch, 'ausklammern': g_ausklammern, 'faktorisieren': g_faktorisieren,
       'ergaenzung': g_ergaenzung, 'loesungsformel': g_loesungsformel, 'diskriminante': g_diskriminante, 'sachaufgabe': g_sachaufgabe}

if __name__ == '__main__':
    bauen('gleichungen.quadratisch',
          'Quadratische Gleichungen mit der passenden Methode lösen und die Anzahl der Lösungen mit der Diskriminante begründen.',
          ['Ohne x-Glied: nach x² umstellen, ± Wurzel. Ohne Zahlglied: x ausklammern.', 'Produkt = 0: Satz vom Nullprodukt.',
           'Lösungsformel: x₁,₂ = (−b ± √(b² − 4ac)) / (2a).', 'D > 0: zwei, D = 0: eine, D < 0: keine Lösung.'],
          [('Sonderfälle', ['reinquadratisch', 'ausklammern', 'faktorisieren']), ('Allgemeine Verfahren', ['ergaenzung', 'loesungsformel']),
           ('Lösbarkeit und Anwendung', ['diskriminante', 'sachaufgabe'])],
          ETAPPEN, GEN,
          meiden={'reinquadratisch': ['3x² − 75 = 0'], 'ausklammern': ['2x² − 12x = 0'], 'faktorisieren': ['x² − 8x + 16 = 0'],
                  'ergaenzung': ['x² + 6x − 7 = 0'], 'loesungsformel': ['2x² − 5x − 3 = 0'], 'diskriminante': ['x² − 4x + 7 = 0'],
                  'sachaufgabe': ['4 cm länger als breit und hat einen Flächeninhalt von 45']},
          offen=['Lösungen werden als Lücken „x₁ = □; x₂ = □“ (kleinere zuerst) abgefragt; Lösungen mit Wurzeln (irrational) sind bewusst ausgelassen, weil Lücken nur ganze Zahlen erlauben. Im Unterricht kommen sie vor – ggf. Antworttyp „Wurzelterm“ nachrüsten.',
                 'Grafische Deutung (Nullstellen der Parabel) steht im Thema funktionen.quadratisch.'])
