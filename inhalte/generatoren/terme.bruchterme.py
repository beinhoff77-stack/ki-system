#!/usr/bin/env python3
"""Thema terme.bruchterme – Bruchterme (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, L, Z, baue, bruch, cz, ist_endlich, kl, lin, mono, pot, zt  # noqa: E402

META = {'thema_schluessel': 'terme.bruchterme', 'thema_id': 31, 'block_id': 60, 'klasse': {'gym_by': 8, 'rs_by': 8}}

ETAPPEN = [
    {'lernziel': 'definitionsmenge', 'titel': 'Definitionsmenge bestimmen',
     'regel': 'Ein ⟦Bruchterm⟧ hat eine Variable im Nenner. Durch 0 darf man nicht teilen. Die ⟦Definitionsmenge⟧ D enthält alle Zahlen, für die ⟦kein Nenner 0⟧ wird.',
     'schritte': ['5/(x − 3): Nenner x − 3 = 0 für x = 3.', 'Also ⟦D = ℚ \\ {3}⟧ (alle rationalen Zahlen außer 3).'],
     'fehler': 'Bei (x − 2)/(x + 4) ist nicht 2 auszuschließen: Der ⟦Zähler⟧ darf 0 sein. Nur x = −4 macht den ⟦Nenner⟧ 0, also D = ℚ \\ {−4}.',
     '_verbot': ['5/(x − 3)']},
    {'lernziel': 'termwert', 'titel': 'Werte von Bruchtermen berechnen',
     'regel': 'Setze die Zahl für x ein und rechne ⟦Zähler und Nenner getrennt⟧ aus. Liegt die Zahl nicht in D, hat der Term ⟦keinen Wert⟧.',
     'schritte': ['T(x) = (2x + 1)/(x − 1) für x = 3', 'Zähler: 2 · 3 + 1 = 7, Nenner: 3 − 1 = 2', 'T(3) = 7/2 = ⟦3,5⟧'],
     'fehler': 'Für x = 1 ist T(1) nicht 3/0 = 0: Durch 0 teilen geht nicht. T(1) ist ⟦nicht definiert⟧.',
     '_verbot': ['(2x + 1)/(x − 1)']},
    {'lernziel': 'kuerzen', 'titel': 'Bruchterme kürzen',
     'regel': 'Kürzen heißt: Zähler und Nenner durch denselben ⟦Faktor⟧ teilen. Summen musst du vorher ⟦ausklammern⟧ – aus Summen darf man nicht kürzen.',
     'schritte': ['(3x + 6)/(5x + 10)', '= 3(x + 2)/(5(x + 2))', '(x + 2) kürzen: ⟦3/5⟧ (für x ≠ −2)'],
     'fehler': '(x + 6)/3 ist nicht x + 2: Die 6 ist ein ⟦Summand⟧, kein Faktor. Richtig wäre nur (3x + 6)/3 = x + 2.',
     '_verbot': ['(3x + 6)/(5x + 10)']},
    {'lernziel': 'erweitern', 'titel': 'Bruchterme erweitern',
     'regel': 'Erweitern heißt: Zähler und Nenner mit demselben Term ⟦multiplizieren⟧. So machst du Brüche ⟦gleichnamig⟧ (gleicher Nenner).',
     'schritte': ['3/(2x) soll den Nenner 8x² bekommen.', '8x² : (2x) = 4x, also mit 4x erweitern.', 'Neuer Zähler: 3 · 4x = ⟦12x⟧'],
     'fehler': 'Erweitert man 3/(2x) mit 4x, wird nicht nur der Nenner multipliziert. Auch der ⟦Zähler⟧ ändert sich: 12x/(8x²), nicht 3/(8x²).',
     '_verbot': ['3/(2x)']},
    {'lernziel': 'addieren', 'titel': 'Bruchterme addieren und subtrahieren',
     'regel': 'Gleicher Nenner: ⟦Zähler addieren⟧, Nenner bleibt. Verschiedene Nenner: erst auf den ⟦Hauptnenner⟧ erweitern.',
     'schritte': ['2/x + 3/(4x): Hauptnenner 4x.', '2/x = 8/(4x)', '8/(4x) + 3/(4x) = ⟦11/(4x)⟧'],
     'fehler': '2/x + 3/x ist nicht 5/(2x): Die ⟦Nenner werden nicht addiert⟧. Richtig ist 5/x.',
     '_verbot': ['2/x + 3/(4x)']},
    {'lernziel': 'multiplizieren', 'titel': 'Bruchterme multiplizieren und dividieren',
     'regel': 'Multiplizieren: ⟦Zähler mal Zähler, Nenner mal Nenner⟧, dann kürzen. Dividieren: mit dem ⟦Kehrbruch⟧ multiplizieren.',
     'schritte': ['(4x/9) · (3/x²)', '= 12x/(9x²)', 'kürzen mit 3x: ⟦4/(3x)⟧'],
     'fehler': 'Bei (2/x) : (4/x²) teilt man nicht Zähler durch Zähler und Nenner durch Nenner „irgendwie“: Multipliziere mit dem ⟦Kehrbruch⟧ x²/4. Ergebnis: 2x²/(4x) = x/2.',
     '_verbot': ['(4x/9) · (3/x²)']},
    {'lernziel': 'fehler_finden', 'titel': 'Richtig oder falsch umgeformt?',
     'regel': 'Prüfe eine Umformung, indem du eine ⟦Zahl einsetzt⟧ (aus D). Kommt links und rechts etwas anderes heraus, ist die Umformung ⟦falsch⟧.',
     'schritte': ['Behauptung: (x + 4)/4 = x + 1', 'Teste x = 4: links 8/4 = 2, rechts 5.', '2 ≠ 5, also ⟦falsch⟧. Richtig: (x + 4)/4 = x/4 + 1.'],
     'fehler': 'Ein einziges passendes Beispiel beweist keine Umformung: (x + 4)/4 = x + 1 stimmt zufällig für x = 0. Ein ⟦Gegenbeispiel⟧ genügt aber, um sie zu widerlegen.',
     '_verbot': ['(x + 4)/4 = x + 1']},
]


def nenner_lin(a, b):
    """a·x + b als Text in Klammern, falls Summe."""
    t = lin(a, b)
    return f'({t})' if b != 0 else t


def mengentext(xs):
    xs = sorted(set(xs))
    return 'ℚ' if not xs else 'ℚ \\ {' + '; '.join(zt(x) for x in xs) + '}'


def g_definitionsmenge(R, st):
    if st == 1:
        a, b = R.randint(1, 9), R.randint(-9, 9)
        if b == 0: b = 4
        z = R.choice([str(a), lin(1, R.randint(1, 5)), lin(2, -R.randint(1, 5))])
        T = f'{z}/{nenner_lin(1, -b)}'
        if R.random() < .5:
            return Z(f'Für welche Zahl ist der Term {T} nicht definiert?', b, f'{b}', f'Nenner {lin(1, -b)} = 0 für x = {zt(b)}.',
                     'Setze den Nenner gleich 0 und löse nach x.')
        return A(R, f'Gib die Definitionsmenge von {T} an.', mengentext([b]), [mengentext([-b]), mengentext([0]), 'ℚ'],
                 f'Nenner {lin(1, -b)} = 0 für x = {zt(b)}, also D = {mengentext([b])}.', 'Welche Zahl macht den Nenner 0?')
    if st == 2:
        while True:
            k, m = R.choice([2, 3, 4, 5, -2, -4]), R.randint(-12, 12)
            if m and ist_endlich(Fr(m, k)) and Fr(m, k).denominator != 1 or R.random() < .3 and m and m % k == 0: break
        x0 = Fr(m, k)
        T = f'{R.randint(1, 9)}/{nenner_lin(k, -m)}'
        if R.random() < .6:
            return Z(f'Für welche Zahl ist der Term {T} nicht definiert?', x0, f'{m} / ({k})',
                     f'{lin(k, -m)} = 0 → {lin(k, 0)} = {zt(m)} → x = {zt(x0)}.', 'Setze den Nenner gleich 0 und löse die Gleichung.')
        b = R.randint(1, 8) * R.choice([-1, 1])
        T = f'{R.randint(1, 9)}/(x({lin(1, -b)}))'
        return A(R, f'Gib die Definitionsmenge von {T} an.', mengentext([0, b]), [mengentext([b]), mengentext([0, -b]), mengentext([-b])],
                 f'Ein Produkt ist 0, wenn ein Faktor 0 ist: x = 0 oder {lin(1, -b)} = 0, also x = {zt(b)}. D = {mengentext([0, b])}.',
                 'Ein Produkt im Nenner ist 0, wenn einer der Faktoren 0 ist.')
    # Stufe 3: zwei Nenner / Zähler mit Nullstelle als Falle
    if R.random() < .5:
        b, c = R.sample([k for k in range(-8, 9) if k], 2)
        z = R.choice([k for k in range(-8, 9) if k not in (b, c, 0)])
        T = f'{nenner_lin(1, -z)}/(({lin(1, -b)})({lin(1, -c)}))'
        return A(R, f'Gib die Definitionsmenge von {T} an.', mengentext([b, c]), [mengentext([b, c, z]), mengentext([-b, -c]), mengentext([z])],
                 f'Nenner 0 für x = {zt(b)} oder x = {zt(c)}. Der Zähler darf 0 sein. D = {mengentext([b, c])}.',
                 'Nur der Nenner zählt. Jeder Faktor im Nenner liefert eine ausgeschlossene Zahl.')
    b = R.randint(1, 8) * R.choice([-1, 1]); k = R.choice([2, 4, 5]); m = R.choice([j for j in range(-9, 10) if j % k])
    T = f'{R.randint(1, 9)}/{nenner_lin(1, -b)} + {R.randint(1, 9)}/{nenner_lin(k, -m)}'
    return A(R, f'Gib die Definitionsmenge von {T} an.', mengentext([b, Fr(m, k)]), [mengentext([b]), mengentext([-b, Fr(-m, k)]), mengentext([b, m])],
             f'Erster Nenner 0 für x = {zt(b)}, zweiter für {lin(k, 0)} = {zt(m)}, also x = {zt(Fr(m, k))}. D = {mengentext([b, Fr(m, k)])}.',
             'Bestimme für jeden Nenner die Zahl, die ihn 0 macht.')


def g_termwert(R, st):
    while True:
        a, b = R.randint(-5, 6), R.randint(-9, 9)
        c, d = R.choice([1, 1, 2, -1, 3]), R.randint(-8, 8)
        x0 = R.randint(-6, 8)
        if a == 0 or d == 0: continue
        nen = c * x0 + d
        if nen == 0: continue
        w = Fr(a * x0 + b, nen)
        if not ist_endlich(w) or len(zt(w)) > 6: continue
        if st == 1 and (c != 1 or w.denominator != 1): continue
        if st == 2 and w.denominator == 1 and R.random() < .5: continue
        break
    zx = lin(a, b); nx = lin(c, d)
    T = f'({zx})/({nx})' if b else f'{zx}/({nx})'
    if st == 3 and R.random() < .45:
        # Wert außerhalb von D
        xn = Fr(-d, c)
        if xn.denominator == 1:
            andere = [zt(Fr(a * xn + b, 1)), '0', zt(a * xn + b + 1)]
            return A(R, f'Welchen Wert hat T(x) = {T} für x = {zt(xn)}?', 'Keinen: T ist dort nicht definiert.', andere,
                     f'Nenner: {lin(c, 0).replace("x", "· " + kl(xn)) if c != 1 else kl(xn)} {"+" if d > 0 else "−"} {abs(d)} = 0. Durch 0 teilen geht nicht.',
                     'Rechne zuerst den Nenner aus.')
    return Z(f'Berechne T({zt(x0)}) für T(x) = {T}.', w, f'(({a}) * ({x0}) + ({b})) / (({c}) * ({x0}) + ({d}))',
             f'Zähler: {zt(a * x0 + b)}, Nenner: {zt(nen)}. T({zt(x0)}) = {zt(a * x0 + b)}/{kl(nen) if nen < 0 else zt(nen)} = {zt(w)}.',
             'Setze die Zahl in Zähler und Nenner getrennt ein. Achte auf Klammern bei negativen Zahlen.')


def g_kuerzen(R, st):
    if st == 1:
        while True:
            t = R.randint(2, 6)
            p, q = R.randint(1, 6) * t, R.randint(1, 6) * t
            e1, e2 = R.randint(1, 4), R.randint(1, 4)
            if p != q and e1 != e2: break
        c = Fr(p, q); e = e1 - e2
        T = f'{p}{pot("x", e1)}/({q}{pot("x", e2)})'
        r = mono(c, e)
        return A(R, f'Kürze vollständig: {T}', r, [mono(c, e1 + e2) if e1 + e2 <= 6 else mono(c, e + 1), mono(Fr(p - t, q - t), e) if p - t > 0 and q - t > 0 and Fr(p - t, q - t) != c else mono(3 * c, e), mono(c, -e), mono(c * 2, e)],
                 f'Zahlen: {p}/{q} = {bruch(c)}. Potenzen: {pot("x", e1)}/{pot("x", e2)} = {mono(1, e)}. Ergebnis: {r}.',
                 'Kürze Zahlen und Potenzen von x getrennt. Gleiche Faktoren x fallen weg.')
    if st == 2:
        art = R.choice(['faktor', 'x_ausklammern'])
        if art == 'faktor':
            while True:
                k, m, b = R.randint(2, 9), R.randint(2, 9), R.randint(-7, 7)
                if k != m and b: break
            T = f'({lin(k, k * b)})/({lin(m, m * b)})'
            r = bruch(Fr(k, m))
            return A(R, f'Kürze vollständig: {T}', r, [f'{bruch(Fr(k * b, m * b) + 1)}', f'({lin(k, b)})/({lin(m, b)})', f'{zt(k * b)}/{kl(m * b)} · x'],
                     f'Ausklammern: {k}({lin(1, b)})/({m}({lin(1, b)})). ({lin(1, b)}) kürzen: {r}.', 'Klammere im Zähler und im Nenner die Zahl vor x aus.')
        b, c = R.randint(-8, 8) or 3, R.randint(2, 9)
        T = f'({lin(1, 0)}² {"+" if b > 0 else "−"} {abs(b) if abs(b) != 1 else ""}x)/({c}x)'
        r = f'({lin(1, b)})/{c}'
        return A(R, f'Kürze vollständig: {T}', r, [lin(1, b), f'(x² {"+" if b > 0 else "−"} {abs(b)})/{c}', f'({lin(1, b)})/({c}x)'],
                 f'Zähler: x({lin(1, b)}). Mit x kürzen: {r}.', 'Klammere im Zähler x aus.')
    art = R.choice(['vorzeichen', 'binom', 'binom'])
    if art == 'vorzeichen':
        k, b = R.randint(2, 9), R.randint(1, 9)
        T = f'({lin(k, -k * b)})/({b} − x)'
        return A(R, f'Kürze vollständig: {T}', zt(-k), [zt(k), f'{k}x', lin(k, -b)],
                 f'{lin(k, -k * b)} = {k}(x − {b}) und {b} − x = −(x − {b}). Also {k}(x − {b})/(−(x − {b})) = {zt(-k)}.',
                 'Im Nenner steht fast dasselbe wie in der Klammer im Zähler – nur mit umgekehrtem Vorzeichen.')
    b = R.randint(1, 9); s = R.choice([1, -1])
    T = f'(x² − {b * b})/({lin(1, s * b)})'
    r = lin(1, -s * b)
    return A(R, f'Kürze vollständig: {T}', r, [lin(1, s * b), f'x − {b * b}' if s > 0 else f'x + {b * b}', f'x² − {b}'],
             f'3. binomische Formel: x² − {b * b} = (x + {b})(x − {b}). Mit ({lin(1, s * b)}) kürzen: {r}.',
             'Erkenne die 3. binomische Formel: a² − b² = (a + b)(a − b).')


def g_erweitern(R, st):
    h = 'Teile den neuen Nenner durch den alten. Mit diesem Term multiplizierst du auch den Zähler.'
    if st == 1:
        a, b = R.randint(1, 9), R.randint(2, 6)
        f = R.randint(2, 5)
        alt, neu = f'{a}/({b}x)', f'{b * f}x²'
        return L(f'Erweitere {alt} auf den Nenner {neu}. Gib den neuen Zähler ein.', '□x', [a * f], [f'{a}*{f}'],
                 f'{neu} : ({b}x) = {f}x. Zähler: {a} · {f}x = {a * f}x.', h)
    if st == 2:
        b = R.randint(1, 9) * R.choice([-1, 1]); d, f = R.randint(2, 5), R.randint(2, 4)
        alt = f'({lin(1, b)})/{d}'
        return L(f'Erweitere {alt} auf den Nenner {d * f}. Gib den neuen Zähler ein.', '□x + □', [f, f * b], [f'{f}', f'{f}*({b})'],
                 f'{d * f} : {d} = {f}. Zähler: {f} · ({lin(1, b)}) = {lin(f, f * b)}.', h)
    if R.random() < .5:
        a, b = R.randint(1, 9), R.randint(1, 9) * R.choice([-1, 1])
        alt, neu = f'{a}/({lin(1, b)})', f'x² {"+" if b > 0 else "−"} {abs(b) if abs(b) != 1 else ""}x'
        return L(f'Erweitere {alt} auf den Nenner {neu}. Gib den neuen Zähler ein.', '□x', [a], [f'{a}'],
                 f'{neu} = x({lin(1, b)}). Mit x erweitern: Zähler {lin(a, 0)}.', 'Klammere im neuen Nenner x aus.')
    b, c, f = R.randint(1, 9) * R.choice([-1, 1]), R.randint(1, 9) * R.choice([-1, 1]), R.randint(2, 5)
    alt, neu = f'({lin(1, b)})/({lin(1, c)})', f'{lin(f, f * c)}'
    return L(f'Erweitere {alt} auf den Nenner {neu}. Gib den neuen Zähler ein.', '□x + □', [f, f * b], [f'{f}', f'{f}*({b})'],
             f'{neu} = {f}({lin(1, c)}). Mit {f} erweitern: {f} · ({lin(1, b)}) = {lin(f, f * b)}.', 'Klammere im neuen Nenner eine Zahl aus.')


def g_addieren(R, st):
    if st == 1:
        a, b, c = R.randint(1, 9), R.randint(1, 9), R.randint(-6, 6)
        op = R.choice(['+', '−'])
        n = lin(1, c)
        r_z = a + b if op == '+' else a - b
        N = f'({n})' if c else 'x'
        return A(R, f'Fasse zusammen: {a}/{N} {op} {b}/{N}', f'{zt(r_z)}/{N}' if r_z else '0',
                 [f'{zt(r_z)}/(2{N})' if c else f'{zt(r_z)}/(2x)', f'{zt(r_z)}/{N}²' if c else f'{zt(r_z)}/x²', f'{zt(a + b if op == "−" else a - b)}/{N}'],
                 f'Gleicher Nenner: Zähler {a} {op} {b} = {zt(r_z)}, Nenner bleibt: {zt(r_z)}/{N}.', 'Gleicher Nenner: nur die Zähler verrechnen.')
    if st == 2:
        a, b, k = R.randint(1, 9), R.randint(1, 9), R.randint(2, 6)
        op = R.choice(['+', '−'])
        if R.random() < .5:
            z = k * a + b if op == '+' else k * a - b
            r = mono(Fr(z, k), -1) if z else '0'
            return A(R, f'Fasse zusammen: {a}/x {op} {b}/({k}x)', r, [f'{zt(a + b if op == "+" else a - b)}/({k + 1}x)', mono(Fr(a + b if op == '+' else a - b, k), -1), f'{zt(z)}/({k}x²)'],
                     f'Hauptnenner {k}x: {a}/x = {k * a}/({k}x). {k * a} {op} {b} = {zt(z)}. Ergebnis {zt(z)}/({k}x)' + (f' = {r}' if r != f'{zt(z)}/({k}x)' else '') + '.',
                     'Erweitere den ersten Bruch auf den Hauptnenner.')
        r = f'({lin(a, -b if op == "−" else b)})/x²'
        return A(R, f'Fasse zusammen: {a}/x {op} {b}/x²', r, [f'{zt(a - b if op == "−" else a + b)}/x²', f'{zt(a - b if op == "−" else a + b)}/x³', f'({lin(a, -b if op == "−" else b)})/x³'],
                 f'Hauptnenner x²: {a}/x = {lin(a, 0)}/x². Ergebnis: {r}.', 'Der Hauptnenner ist x². Erweitere den ersten Bruch mit x.')
    a, b, c = R.randint(1, 6), R.randint(1, 6), R.randint(1, 8) * R.choice([-1, 1])
    r = f'({lin(a + b, a * c)})/(x({lin(1, c)}))'
    return A(R, f'Fasse zusammen: {a}/x + {b}/({lin(1, c)})', r,
             [f'{a + b}/(x + {lin(1, c)})', f'{a + b}/(x({lin(1, c)}))', f'({lin(a + b, c)})/(x({lin(1, c)}))'],
             f'Hauptnenner x({lin(1, c)}). Zähler: {a}({lin(1, c)}) + {lin(b, 0)} = {lin(a + b, a * c)}. Ergebnis: {r}.',
             'Der Hauptnenner ist das Produkt der beiden Nenner.')


def g_multiplizieren(R, st):
    def zufall():
        while True:
            p, q, e = R.randint(1, 9), R.randint(2, 9), R.randint(-3, 3)
            if gcd(p, q) == 1 and e != 0: return Fr(p, q), e
    if st in (1, 2):
        (c1, e1), (c2, e2) = zufall(), zufall()
        if st == 1 and e1 * e2 > 0: e2 = -e2
        div = st == 2 and R.random() < .6
        if div:
            c, e = c1 / c2, e1 - e2
            op, w0 = ':', f'Mit dem Kehrbruch von {mono(c2, e2)} multiplizieren: {mono(c1, e1)} · {mono(1 / c2, -e2)}'
            falsch = [mono(c1 * c2, e1 + e2), mono(c2 / c1, e2 - e1), mono(c1 / c2, e1 + e2)]
        else:
            c, e = c1 * c2, e1 + e2
            op, w0 = '·', 'Zähler mal Zähler, Nenner mal Nenner'
            falsch = [mono(c1 * c2, e1 - e2), mono(c1 / c2, e), mono(c1 * c2 * 2, e), mono(c1 + c2, e)]
        if e > 6 or e < -6: return g_multiplizieren(R, st)
        r = mono(c, e)
        return A(R, f'Berechne und kürze: ({mono(c1, e1)}) {op} ({mono(c2, e2)})', r, falsch, f'{w0}, dann kürzen: {r}.',
                 'Erst multiplizieren (bei „:“ mit dem Kehrbruch), dann Zahlen und x getrennt kürzen.')
    b = R.randint(1, 9) * R.choice([-1, 1]); p, q = R.randint(2, 9), R.randint(2, 9)
    if p == q: q += 1
    g = gcd(p, q)
    K = f'({lin(1, b)})'
    r = f'{p // g}/({q // g}{K})' if q // g != 1 else f'{p // g}/{K}'
    return A(R, f'Berechne und kürze: ({lin(1, b)})/{q} · {p}/{K}²', r, [f'{p // g}{K}/{q // g}', f'{p}/({q}{K}²)', f'{p // g}/{q // g}'],
             f'Zähler: {p}{K}, Nenner: {q}{K}². Kürzen mit {g}{K}' + ('' if g > 1 else '') + f': {r}.', f'{K}² = {K} · {K}. Ein Faktor {K} kürzt sich.')


def aussagen(R):
    """(Aussage, wahr?, Begründung) – Wahrheitswerte zusätzlich per Einsetzen geprüft."""
    a, b = R.sample(range(2, 10), 2)
    c = R.randint(2, 9)
    al = [
        (f'(x + {a})/{a} = x + 1', False, f'Aus der Summe x + {a} darf man nicht kürzen. Richtig: x/{a} + 1.', lambda x: ((x + a) / a, x + 1)),
        (f'({a}x)/{a} = x', True, f'{a} ist ein Faktor und darf gekürzt werden.', lambda x: (a * x / a, x)),
        (f'{a}/x + {b}/x = {a + b}/(2x)', False, f'Die Nenner werden nicht addiert. Richtig: {a + b}/x.', lambda x: (Fr(a) / x + Fr(b) / x, Fr(a + b) / (2 * x))),
        (f'{a}/x · {b}/x = {a * b}/x²', True, 'Zähler mal Zähler, Nenner mal Nenner.', lambda x: (Fr(a) / x * Fr(b) / x, Fr(a * b) / x ** 2)),
        (f'(x + {a})/(x + {b}) = {a}/{b}', False, 'x ist ein Summand und darf nicht gekürzt werden.', lambda x: ((x + a) / (x + b), Fr(a, b))),
        (f'({a}x + {a * b})/{a} = x + {b}', True, f'Zähler = {a}(x + {b}), dann {a} kürzen.', lambda x: ((a * x + a * b) / a, x + b)),
        (f'(x/{a}) : {b} = x/{a * b}', True, f'Durch {b} teilen heißt mit 1/{b} multiplizieren.', lambda x: (x / a / b, x / (a * b))),
        (f'(x/{a}) : {b} = {b}x/{a}', False, f'Durch {b} teilen ist nicht mal {b}. Richtig: x/{a * b}.', lambda x: (x / a / b, b * x / a)),
        (f'1/x + 1/{a} = 2/(x + {a})', False, f'Hauptnenner {a}x: richtig ist (x + {a})/({a}x).', lambda x: (1 / x + Fr(1, a), 2 / (x + a))),
        (f'x²/(x + {a}) = x − {a}', False, 'Im Zähler steht keine binomische Formel, nichts lässt sich kürzen.', lambda x: (x ** 2 / (x + a), x - a)),
        (f'(x² − {a * a})/(x − {a}) = x + {a}', True, f'3. binomische Formel: x² − {a * a} = (x + {a})(x − {a}).', lambda x: ((x ** 2 - a * a) / (x - a), x + a)),
        (f'{c}/({c}x) = 1/x', True, f'{c} ist Faktor in Zähler und Nenner.', lambda x: (Fr(c) / (c * x), 1 / x)),
        (f'{c}/({c} + x) = 1/x', False, f'Im Nenner ist {c} ein Summand, man darf nicht kürzen.', lambda x: (Fr(c) / (c + x), 1 / x)),
        (f'(−x − {a})/(x + {a}) = −1', True, f'Zähler = −(x + {a}).', lambda x: ((-x - a) / (x + a), Fr(-1))),
    ]
    for t, w, _, f in al:     # Kontrolle: wahr ⇔ für mehrere Testzahlen gleich
        gleich = all(f(Fr(x))[0] == f(Fr(x))[1] for x in (Fr(1, 3), Fr(17, 7), Fr(-23, 11), Fr(101, 13)))
        assert gleich == w, t
    return [(t, w, g) for t, w, g, _ in al]


def g_fehler_finden(R, st):
    al = aussagen(R)
    wahr = [(t, g) for t, w, g in al if w]; falsch = [(t, g) for t, w, g in al if not w]
    if st == 1 or (st == 2 and R.random() < .5):
        t, g = R.choice(wahr)
        return A(R, 'Welche Umformung ist richtig (für alle x aus D)?', t, [x for x, _ in R.sample(falsch, 3)],
                 f'Richtig: {t}. {g} Bei den anderen findest du durch Einsetzen ein Gegenbeispiel.',
                 'Setze eine einfache Zahl ein, z. B. x = 1, und vergleiche beide Seiten.')
    t, g = R.choice(falsch)
    return A(R, 'Welche Umformung ist FALSCH?', t, [x for x, _ in R.sample(wahr, 3)],
             f'Falsch: {t}. {g}', 'Suche ein Gegenbeispiel durch Einsetzen.')


GEN = {'definitionsmenge': g_definitionsmenge, 'termwert': g_termwert, 'kuerzen': g_kuerzen, 'erweitern': g_erweitern,
       'addieren': g_addieren, 'multiplizieren': g_multiplizieren, 'fehler_finden': g_fehler_finden}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Grundlagen', ['definitionsmenge', 'termwert']), ('Kürzen und Erweitern', ['kuerzen', 'erweitern']),
          ('Rechnen', ['addieren', 'multiplizieren', 'fehler_finden'])],
         'Bruchterme verstehen: Definitionsmenge bestimmen, Werte berechnen, kürzen, erweitern und mit Bruchtermen rechnen.',
         ['Nenner darf nie 0 sein: Diese Zahlen fehlen in D.', 'Kürzen nur aus Produkten, nie aus Summen.',
          'Addieren: erst gleichnamig machen. Multiplizieren: Zähler · Zähler, Nenner · Nenner. Dividieren: mal Kehrbruch.'],
         offen=['Die README nennt für Brüche als Ergebnis die Lückenschablone „□/□“. Die App liest Lücken aber als Polynom-Term (z. B. „□x + □“); '
                'einen Bruch kann sie dort nicht auswerten. Bruch-Ergebnisse sind deshalb als Auswahl gebaut, Lücken nur für Zähler-Terme.'])
