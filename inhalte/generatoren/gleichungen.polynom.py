#!/usr/bin/env python3
"""Thema gleichungen.polynom – Polynomgleichungen (Klasse 10). Schreibt inhalte/themen/gleichungen.polynom.json."""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import *  # noqa: E402,F403

start(1002)
IDX = '₁₂₃₄₅'


def schab(n):
    return '; '.join(f'x{IDX[i]} = □' for i in range(n))


def nz(n):
    return R.choice([i for i in range(-n, n + 1) if i != 0])


def mal(*fs):
    """Polynom-Koeffizienten multiplizieren (höchster Grad zuerst)."""
    out = [1]
    for f in fs:
        n = [0] * (len(out) + len(f) - 1)
        for i, a in enumerate(out):
            for j, b in enumerate(f):
                n[i + j] += a * b
        out = n
    return out


def wert_c(k, x):
    """Rechenausdruck: Polynom mit Koeffizienten k an der Stelle x (für Probe)."""
    n = len(k) - 1
    return ' + '.join(f'({c}) * ({x}) ** {n - i}' for i, c in enumerate(k))


def faktor(p, hoch=1):
    t = minus_klammer(p)
    if hoch > 1: t = (t if t != 'x' else 'x') + str(hoch).translate(HOCHZ)
    return t


def loes_luecken(text, lsg, k, w, h):
    """Lösungen (verschieden, aufsteigend) als Lücken; c prüft, dass jede Lösung das Polynom k zu 0 macht."""
    lsg = sorted(set(lsg))
    return luecken(text, schab(len(lsg)), 'alle Lösungen, kleinste zuerst', lsg, w, h,
                   c=[f'{x} + ({wert_c(k, x)})' for x in lsg])


ETAPPEN = [
    {'lernziel': 'ausklammern', 'titel': 'Lösen durch Ausklammern',
     'regel': 'Fehlt das Zahlglied, klammerst du die ⟦höchste gemeinsame Potenz von x⟧ aus. Dann gilt der ⟦Satz vom Nullprodukt⟧: Ein Produkt ist null, wenn ein Faktor null ist.',
     'schritte': ['x³ − 5x² + 6x = 0 ⇔ x(x² − 5x + 6) = 0.', 'x = 0 oder x² − 5x + 6 = 0 ⇒ ⟦x₁ = 0, x₂ = 2, x₃ = 3⟧.'],
     'probe': '3³ − 5 · 9 + 18 = 27 − 45 + 18 = 0 ✓',
     'fehler': 'x³ − 5x² + 6x = 0 durch x zu teilen ist falsch: Dabei geht die Lösung ⟦x = 0⟧ verloren. Ausklammern statt teilen.'},
    {'lernziel': 'nullprodukt', 'titel': 'Produktform lesen',
     'regel': 'Steht das Polynom als ⟦Produkt von Faktoren⟧, setzt du jeden Faktor null. Ein Faktor wie x² + 4 wird ⟦nie null⟧ und liefert keine Lösung.',
     'schritte': ['(x + 2)(x² − 9)(x² + 1) = 0.', 'x = −2; x² = 9 ⇒ x = ±3; x² = −1 geht nicht: ⟦L = {−3; −2; 3}⟧.'],
     'probe': 'x = −3: (−1) · 0 · 10 = 0 ✓',
     'fehler': 'Aus x² + 1 = 0 die Lösung x = −1 abzulesen ist falsch: (−1)² + 1 = 2 ≠ 0. Ein ⟦Quadrat plus positive Zahl⟧ ist nie null.'},
    {'lernziel': 'substitution', 'titel': 'Biquadratische Gleichungen',
     'regel': 'Bei ⟦ax⁴ + bx² + c = 0⟧ setzt du ⟦z = x²⟧ und löst az² + bz + c = 0. Danach ⟦rücksubstituieren⟧: x² = z₁ und x² = z₂ (nur z ≥ 0 liefert Lösungen).',
     'schritte': ['x⁴ − 10x² + 9 = 0, z = x²: z² − 10z + 9 = 0 ⇒ z₁ = 1, z₂ = 9.', 'x² = 1 ⇒ x = ±1; x² = 9 ⇒ x = ±3: ⟦L = {−3; −1; 1; 3}⟧.'],
     'probe': '3⁴ − 10 · 9 + 9 = 81 − 90 + 9 = 0 ✓',
     'fehler': 'Mit z₁ = 1 und z₂ = 9 aufzuhören ist unvollständig: Gesucht ist x, nicht z. Erst die ⟦Rücksubstitution⟧ liefert die vier Lösungen.'},
    {'lernziel': 'vielfachheit', 'titel': 'Vielfachheit von Nullstellen',
     'regel': 'Kommt der Faktor (x − a) ⟦k-mal⟧ vor, ist a eine ⟦k-fache Nullstelle⟧. Bei ⟦ungerader⟧ Vielfachheit wechselt das Vorzeichen, bei ⟦gerader⟧ nicht (der Graph berührt die x-Achse nur).',
     'schritte': ['f(x) = (x − 1)²(x + 2)³: x = 1 ist doppelte, x = −2 dreifache Nullstelle.', 'Bei x = 1 ⟦kein Vorzeichenwechsel⟧ (gerade), bei x = −2 ⟦Vorzeichenwechsel⟧ (ungerade).'],
     'probe': 'f(0,9) > 0 und f(1,1) > 0 ✓',
     'fehler': '„(x − 1)² hat die Nullstellen 1 und −1“ ist falsch: (x − 1)² = 0 nur für x = 1. Das ist ⟦eine doppelte⟧ Nullstelle.'},
    {'lernziel': 'verstehen', 'titel': 'Aussagen über Polynomgleichungen',
     'regel': 'Eine Gleichung n-ten Grades hat ⟦höchstens n⟧ Lösungen. Bei geradem Grad kann es ⟦keine⟧ geben, bei ungeradem Grad gibt es ⟦mindestens eine⟧.',
     'schritte': ['Behauptung: x⁴ + 3x² + 2 = 0 hat vier Lösungen, weil der Grad 4 ist.', 'x⁴ ≥ 0 und 3x² ≥ 0, also ist die linke Seite ≥ 2: ⟦keine Lösung⟧.'],
     'probe': 'z² + 3z + 2 = 0 ⇒ z = −1, z = −2: beide negativ ✓',
     'fehler': '„Grad 4 heißt genau 4 Lösungen“ ist falsch: Der Grad gibt nur die ⟦Höchstzahl⟧ an.'},
]

_E = {e['lernziel']: e for e in ETAPPEN}
_E['ausklammern']['bild'] = koord([g_poly([1, -5, 6, 0], name='f')], x=(-1, 4), y=(-4, 4),
                                  punkte=[{'x': 0, 'y': 0}, {'x': 2, 'y': 0}, {'x': 3, 'y': 0}])
_E['substitution']['bild'] = koord([g_poly([1, 0, -10, 0, 9], name='f')], x=(-4, 4), y=(-20, 20),
                                   punkte=[{'x': v, 'y': 0} for v in (-3, -1, 1, 3)])
_E['vielfachheit']['bild'] = koord([g_poly(mal([1, -1], [1, -1], [1, 2], [1, 2], [1, 2]), name='f')], x=(-3, 2), y=(-10, 20),
                                   punkte=[{'x': 1, 'y': 0, 'name': 'doppelt'}, {'x': -2, 'y': 0, 'name': 'dreifach'}])
_E['verstehen']['bild'] = koord([g_poly([1, 0, 3, 0, 2], name='f')], x=(-3, 3), y=(-2, 12))


def graph_von(kf, nst, x=None):
    lo, hi = (min(nst) - 1.5, max(nst) + 1.5) if x is None else x
    ws = [abs(sum(c * t ** (len(kf) - 1 - i) for i, c in enumerate(kf))) for t in [lo + (hi - lo) * j / 50 for j in range(51)]]
    m = sorted(ws)[int(len(ws) * 0.8)] or 1
    return koord([g_poly(kf)], x=(math.floor(lo), math.ceil(hi)), ymax=max(4, m * 1.2), punkte=[{'x': v, 'y': 0} for v in sorted(set(nst))])


def g_ausklammern(s):
    if s == 1:
        k = R.randint(1, 10)
        if R.random() < 0.5:
            kf = [1, 0, -k * k, 0]
            return loes_luecken(f'Löse x³ − {k * k}x = 0.', [0, -k, k], kf, f'x(x² − {k * k}) = 0 ⇒ x = 0 oder x = ±{k}.', 'Klammere x aus.')
        b = nz(9)
        kf = [1, b, 0]
        return loes_luecken(f'Löse {poly(1, b, 0)} = 0.', [0, -b], kf, f'x(x {plus(b)}) = 0 ⇒ x = 0 oder x = {dz(-b)}.', 'Klammere x aus.')
    if s == 2:
        p, q = R.sample([i for i in range(-7, 8) if i != 0], 2)
        a = R.choice([1, 1, 2, -1])
        kf = [a * c for c in mal([1, -p], [1, -q])] + [0]
        return loes_luecken(f'Löse {poly(*kf)} = 0.', [0, p, q], kf,
                            f'x({poly(*kf[:-1])}) = 0 ⇒ x = 0 oder {poly(*kf[:-1])} = 0 ⇒ x = {dz(min(p, q))} oder x = {dz(max(p, q))}.',
                            'Klammere x aus und löse die quadratische Gleichung.')
    typ = R.random()
    if typ < 0.5:
        k = R.randint(1, 6)
        a = R.choice([1, 2, 3])
        kf = [a, 0, -a * k * k, 0, 0]
        return loes_luecken(f'Löse {poly(*kf)} = 0.', [-k, 0, k], kf, f'{poly(a, 0, 0) if a > 1 else "x²"}(x² − {k * k}) = 0 ⇒ x = 0 (doppelt) oder x = ±{k}.',
                            'Klammere die höchste gemeinsame Potenz x² aus.')
    p, q = R.sample([i for i in range(-5, 6) if i != 0], 2)
    kf = mal([1, -p], [1, -q]) + [0, 0]
    return loes_luecken(f'Löse {poly(*kf)} = 0.', [0, p, q], kf,
                        f'x²({poly(*kf[:-2])}) = 0 ⇒ x = 0 oder x = {dz(min(p, q))} oder x = {dz(max(p, q))}.', 'Klammere x² aus.')


def g_nullprodukt(s):
    if s == 1:
        p, q, r = R.sample(range(-8, 9), 3)
        kf = mal([1, -p], [1, -q], [1, -r])
        return loes_luecken(f'Löse {faktor(p)} · {faktor(q)} · {faktor(r)} = 0.', [p, q, r], kf,
                            f'Jeder Faktor null: x = {dz(p)}, x = {dz(q)}, x = {dz(r)}.', 'Setze jeden Faktor gleich null.')
    if s == 2:
        p, k = nz(8), R.randint(1, 6)
        if abs(p) == k: return None
        kf = mal([1, -p], [1, 0, -k * k])
        return loes_luecken(f'Löse {faktor(p)}(x² − {k * k}) = 0.', [p, -k, k], kf,
                            f'x = {dz(p)} oder x² = {k * k} ⇒ x = ±{k}.', 'Auch x² − … = 0 liefert zwei Lösungen.')
    p, k, m = nz(8), R.randint(1, 5), R.randint(1, 9)
    if abs(p) == k: return None
    if R.random() < 0.5:
        kf = mal([1, -p], [1, 0, -k * k], [1, 0, m])
        return loes_luecken(f'Löse {faktor(p)}(x² − {k * k})(x² + {m}) = 0.', [p, -k, k], kf,
                            f'x = {dz(p)}; x² = {k * k} ⇒ ±{k}; x² = −{m} hat keine Lösung.', 'Prüfe bei jedem Faktor, ob er überhaupt null werden kann.')
    kf = mal([1, -p], [1, -p], [1, 0, m])
    return loes_luecken(f'Löse {faktor(p, 2)}(x² + {m}) = 0.', [p], kf, f'{faktor(p)} = 0 ⇒ x = {dz(p)}; x² + {m} > 0 immer.',
                        'Welcher Faktor kann null werden?')


def g_substitution(s):
    if s == 1:
        a, b = sorted(R.sample(range(1, 8), 2))
        z1, z2 = a * a, b * b
        return luecken(f'Löse x⁴ {plus(-(z1 + z2))}x² {plus(z1 * z2)} = 0 mit z = x². Gib zuerst nur die Lösungen für z an.', 'z₁ = □; z₂ = □',
                       'kleinere zuerst', [z1, z2], f'z² − {z1 + z2}z + {z1 * z2} = 0 ⇒ z₁ = {z1}, z₂ = {z2}.', 'Ersetze x⁴ durch z² und x² durch z.',
                       c=[f'{z1} + ({z1}) ** 2 - {z1 + z2} * {z1} + {z1 * z2}', f'{z2} + ({z2}) ** 2 - {z1 + z2} * {z2} + {z1 * z2}'])
    if s == 2:
        a, b = sorted(R.sample(range(1, 8), 2))
        z1, z2 = a * a, b * b
        kf = [1, 0, -(z1 + z2), 0, z1 * z2]
        return loes_luecken(f'Löse {poly(*kf)} = 0.', [-b, -a, a, b], kf,
                            f'z = x²: z² − {z1 + z2}z + {z1 * z2} = 0 ⇒ z = {z1} oder z = {z2} ⇒ x = ±{a}, ±{b}.', 'Substituiere z = x², dann rücksubstituieren.')
    if R.random() < 0.35:
        z1, z2 = sorted(R.sample(range(1, 13), 2))
        quad = {1, 4, 9}
        if z1 in quad and z2 in quad: return None
        kf = [1, 0, -(z1 + z2), 0, z1 * z2]
        welche = R.choice([w for w, zz in (('kleinste', z1), ('größte', z2)) if zz not in quad])
        z = z1 if welche == 'kleinste' else z2
        x = math.sqrt(z)
        v = gerundet(x, 2)
        if v is None: return None
        xt = lambda zz: str(int(math.isqrt(zz))) if zz in quad else f'√{zz}'  # noqa: E731
        return zahl(f'Löse {poly(*kf)} = 0. Gib die {welche} positive Lösung auf zwei Nachkommastellen an.',
                    f'z = x²: z² − {z1 + z2}z + {z1 * z2} = 0 ⇒ z₁ = {z1}, z₂ = {z2}. Positive Lösungen: x = {xt(z1)} und x = {xt(z2)}; die {welche} ist {xt(z)} ≈ {dz(v)}.',
                    'Substituiere z = x². Aus x² = z folgt x = √z – das muss keine ganze Zahl sein.', v, f'round({K(x)}, 2)', tol=0.01)
    a = R.randint(1, 7)
    z1 = a * a
    z2 = -R.randint(1, 20)
    k = R.choice([1, 1, 2])
    kf = [k * c for c in [1, 0, -(z1 + z2), 0, z1 * z2]]
    if R.random() < 0.6:
        return loes_luecken(f'Löse {poly(*kf)} = 0.', [-a, a], kf,
                            f'{"Durch " + str(k) + " teilen, " if k > 1 else ""}z = x²: z₁ = {z1}, z₂ = {dz(z2)}. x² = {z1} ⇒ x = ±{a}; x² = {dz(z2)} hat keine Lösung.',
                            'Nach der Substitution: Welche z-Werte liefern wirklich x-Werte?')
    m, n = R.randint(1, 9), R.randint(1, 9)
    kf = [1, 0, m + n, 0, m * n]
    return auswahl(f'Welche Lösungsmenge hat {poly(*kf)} = 0?', 'L = { }', [f'L = {{−{m}; −{n}}}', f'L = {{−√{m}; √{m}}}' if math.isqrt(m) ** 2 != m else f'L = {{−{math.isqrt(m)}; {math.isqrt(m)}}}', f'L = {{{m}; {n}}}'],
                   f'z² + {m + n}z + {m * n} = 0 ⇒ z = −{m}, z = −{n}. Beide negativ, x² kann nicht negativ sein: keine Lösung.',
                   'Substituiere und prüfe das Vorzeichen der z-Lösungen.')


def _vzw(p, q, m, n, ja, mit_bild):
    """Vorzeichenwechsel-Frage; ja gibt vor, ob die richtige Antwort „Ja“ ist (ausgewogen)."""
    kandidaten = [(z, k) for z, k in ((p, m), (q, n)) if (k % 2 == 1) == ja]
    if not kandidaten: return None
    ziel, k = R.choice(kandidaten)
    vw = k % 2 == 1
    f = f'f(x) = {faktor(p, m)} · {faktor(q, n)}'
    kf = mal(*([[1, -p]] * m + [[1, -q]] * n))
    zusatz = ' (Die Zeichnung zeigt den Graphen.)' if mit_bild else ''
    a = auswahl(f'{f}. Wechselt f bei x = {dz(ziel)} das Vorzeichen?{zusatz}', f'{"Ja" if vw else "Nein"}, die Nullstelle ist {k}-fach ({"ungerade" if vw else "gerade"}).',
                [f'{"Nein" if vw else "Ja"}, die Nullstelle ist {k}-fach ({"ungerade" if vw else "gerade"}).', 'Ja, an jeder Nullstelle wechselt das Vorzeichen.',
                 'Nein, das Vorzeichen hängt nur vom Leitkoeffizienten ab.'],
                f'Faktor {faktor(ziel)} hoch {k}: {"ungerade Potenz wechselt das Vorzeichen" if vw else "gerade Potenz bleibt nicht-negativ, kein Vorzeichenwechsel"}.',
                'Gerade oder ungerade Vielfachheit?' + (' Schneidet oder berührt der Graph die x-Achse?' if mit_bild else ''))
    return mit_grafik(a, graph_von(kf, [p, q])) if mit_bild else a


def g_vielfachheit(s):
    p, q = R.sample(range(-6, 7), 2)
    m, n = R.randint(1, 4), R.randint(1, 4)
    f = f'f(x) = {faktor(p, m)}{"" if True else ""} · {faktor(q, n)}'
    if s == 1:
        ziel, k = R.choice([(p, m), (q, n)])
        kf = mal(*([[1, -p]] * m + [[1, -q]] * n))
        return zahl(f'{f}. Welche Vielfachheit hat die Nullstelle x = {dz(ziel)}?', f'Der Faktor {faktor(ziel)} kommt {k}-mal vor: {k}-fache Nullstelle.',
                    'Zähle, wie oft der passende Faktor vorkommt (Exponent).', k, f'{k} + ({wert_c(kf, ziel)})')
    pool, nr = AKT['pool'], AKT['nr']
    ohne_bild = pool in ('korrektur', 'sicherung')
    if s == 2 and not ohne_bild:
        return _vzw(p, q, m, n, nr % 2 == 0, True)
    if s == 2:
        return _vzw(p, q, m, n, nr % 2 == 0, False)
    if nr % 3 == 0:
        return _vzw(p, q, m, n, (nr // 3) % 2 == 0, False)
    typ = R.random()
    if typ < 0.5:
        a = R.randint(1, 6)
        kf = [1, 0, -2 * a * a, 0, a ** 4]
        return luecken(f'Die Gleichung {poly(*kf)} = 0 hat zwei doppelte Lösungen. Gib sie an.', 'x₁ = □; x₂ = □', 'kleinere zuerst', [-a, a],
                       f'{poly(*kf)} = (x² − {a * a})² = (x − {a})²(x + {a})² ⇒ x = ±{a}, jeweils doppelt.', 'Erkennst du eine binomische Formel mit z = x²?',
                       c=[f'{-a} + ({wert_c(kf, -a)})', f'{a} + ({wert_c(kf, a)})'])
    if m + n < 4: return None
    kf = mal(*([[1, -p]] * m + [[1, -q]] * n))
    return zahl(f'{f}. Welchen Grad hat f, wenn man ausmultipliziert?', f'Grad = Summe der Vielfachheiten = {m} + {n} = {m + n}.',
                'Jeder Faktor (x − a) trägt den Grad 1 bei.', m + n, f'{m} + {n} + ({len(kf) - 1} - {m + n})')


def _sach():
    if R.random() < 0.5:
        # Quader x · x · (x + c) = V
        x, c = R.randint(2, 9), R.randint(1, 6)
        V = x * x * (x + c)
        kf = [1, c, 0, -V]
        # nur eine positive Lösung (f ist für x > 0 streng wachsend)
        return zahl(f'Ein Quader hat die Kantenlängen x, x und x + {c} (in cm) und das Volumen {V} cm³. Bestimme x.',
                    f'x · x · (x + {c}) = {V} ⇒ x³ + {c}x² − {V} = 0. Probieren mit Teilern von {V}: x = {x}, denn {x}² · {x + c} = {V}. '
                    f'Weitere positive Lösungen gibt es nicht, weil x³ + {c}x² mit x wächst.',
                    'Stelle die Volumengleichung auf und probiere kleine ganze Zahlen (Teiler des Volumens).', x, f'{x} + ({wert_c(kf, x)})', einheit='cm')
    L = R.choice([12, 16, 20, 24, 30])
    x = R.randint(1, L // 2 - 2)
    V = x * (L - 2 * x) ** 2
    ganz = [t for t in range(1, L // 2) if t * (L - 2 * t) ** 2 == V]
    if ganz != [x]: return None
    kf = [4, -4 * L, L * L, -V]
    return zahl(f'Aus einem {L} cm × {L} cm großen Karton werden an den Ecken Quadrate mit der Seitenlänge x cm ausgeschnitten und die Ränder hochgeklappt. '
                f'Die Schachtel hat das Volumen V = x · ({L} − 2x)². Für welches ganzzahlige x ist V = {dz(V)} cm³?',
                f'x · ({L} − 2x)² = {dz(V)}. Sinnvoll ist nur 0 < x < {L // 2}. Probieren: x = {x} ergibt {x} · {L - 2 * x}² = {dz(V)}. Andere ganze Zahlen passen nicht.',
                f'Welche Werte kann x überhaupt haben? Setze ganze Zahlen zwischen 1 und {L // 2 - 1} ein.', x, f'{x} + ({wert_c(kf, x)})', einheit='cm')


def g_verstehen(s):
    typ = R.choice({1: 'ab', 2: 'abcdf', 3: 'cdeffgg'}[s])
    if typ == 'g':
        return _sach()
    if typ == 'a':
        n = R.randint(3, 8)
        return auswahl(f'Wie viele Lösungen kann eine Polynomgleichung vom Grad {n} höchstens haben?', str(n), [str(n - 1), str(n + 1), str(2 * n)],
                       f'Eine Gleichung n-ten Grades hat höchstens n Lösungen, hier {n}.', 'Der Grad ist die Höchstzahl.')
    if typ == 'b':
        n = R.choice([3, 5, 7])
        return auswahl(f'Kann eine Polynomgleichung vom Grad {n} ganz ohne Lösung sein?', 'Nein, bei ungeradem Grad gibt es mindestens eine Lösung.',
                       ['Ja, wie bei x² + 1 = 0.', f'Nein, sie hat immer genau {n} Lösungen.', 'Ja, wenn das Zahlglied positiv ist.'],
                       'Bei ungeradem Grad geht der Graph von „unten“ nach „oben“ (oder umgekehrt) und muss die x-Achse schneiden.',
                       'Denke an den Verlauf des Graphen für sehr große und sehr kleine x.')
    if typ == 'c':
        k = R.randint(2, 7)
        return auswahl(f'Jemand löst x³ = {k * k}x, indem er durch x teilt, und erhält x = ±{k}. Was stimmt?', 'Unvollständig: Auch x = 0 ist Lösung.',
                       ['Richtig, mehr Lösungen gibt es nicht.', f'Falsch: Nur x = {k} ist Lösung.', f'Falsch: x = {k * k}.'],
                       f'x³ − {k * k}x = x(x² − {k * k}) = 0 ⇒ x = 0 oder x = ±{k}. Beim Teilen durch x geht x = 0 verloren.', 'Was passiert beim Teilen mit x = 0?')
    if typ == 'd':
        a, b = sorted(R.sample(range(1, 7), 2))
        return auswahl(f'Bei x⁴ − {a * a + b * b}x² + {a * a * b * b} = 0 gibt jemand als Lösung „z = {a * a} und z = {b * b}“ an. Was fehlt?',
                       f'Die Rücksubstitution: x = ±{a} und x = ±{b}.', ['Nichts, die Lösung ist vollständig.', f'Nur x = {a} und x = {b}.', f'Die Probe z = {a * a + b * b}.'],
                       f'z = x² war nur eine Hilfsvariable. Aus x² = {a * a} und x² = {b * b} folgen vier Lösungen.', 'Wonach war gefragt: z oder x?')
    if typ == 'f':
        p, q = sorted(R.sample(range(-4, 5), 2))
        m, n = R.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 2)])
        if p == -q or m == n: return None  # sonst wären zwei Antworten dieselbe Funktion
        kf = mal(*([[1, -p]] * m + [[1, -q]] * n))
        t = lambda a, b_: f'f(x) = {faktor(p, a)} · {faktor(q, b_)}'  # noqa: E731
        richtig = t(m, n)
        falsch = [t(n, m), t(m + 1 if m % 2 else m - 1 or 1, n), f'f(x) = {faktor(-p, m)} · {faktor(-q, n)}']
        return mit_grafik(auswahl('Welcher Funktionsterm passt zum gezeichneten Graphen?', richtig, falsch,
                                  f'Nullstellen bei {dz(p)} und {dz(q)} (nicht {dz(-p)}, {dz(-q)}). Bei x = {dz(p)} {"schneidet" if m % 2 else "berührt"} der Graph die x-Achse ({m}-fach), bei x = {dz(q)} {"schneidet" if n % 2 else "berührt"} er sie ({n}-fach).',
                                  'Lies die Nullstellen ab und achte darauf, ob der Graph die x-Achse schneidet oder nur berührt.'), graph_von(kf, [p, q]))
    if typ == 'e':
        m = R.randint(1, 9)
        return auswahl(f'Wie viele Lösungen hat x⁴ + {m}x² = 0?', 'genau eine (x = 0)', ['keine', 'zwei', 'vier'],
                       f'x²(x² + {m}) = 0 ⇒ x² = 0 ⇒ x = 0; x² + {m} = 0 ist unlösbar.', 'Klammere x² aus und prüfe beide Faktoren.')
    return None



# ---------- KLAR: verständliche Fassung der Lernkarten (Runde 7) ----------
# Wird erst nach dem Bauen der Aufgaben eingesetzt (bauen(..., klar=KLAR)), die Aufgaben bleiben wörtlich gleich.
KLAR = {
 'ausklammern': {
  'einstieg': 'Ein Rechenmodell beschreibt die Höhe einer Achterbahnstrecke über dem Boden. An manchen Stellen fährt die Bahn genau auf Bodenhöhe, '
              'dazwischen geht es auf einen Hügel oder hinunter in einen Graben. Gesucht sind die Stellen, an denen die Höhe 0 ist. '
              'Weil in jedem Teil der Rechnung derselbe Faktor steckt, kann man ihn nach vorn ziehen – das heißt ⟦Ausklammern⟧.',
  'woerter': [['x', 'die Stelle entlang der Strecke'],
              ['x³ und x²', 'x · x · x und x · x'],
              ['Zahlglied', 'ein Teil ohne x, also eine reine Zahl; in x³ − 5x² + 6x fehlt es'],
              ['ausklammern', 'einen gemeinsamen Faktor vor eine Klammer ziehen: x³ − 5x² + 6x = x · (x² − 5x + 6)'],
              ['Satz vom Nullprodukt', 'ein Produkt ist 0, wenn mindestens einer der Faktoren 0 ist'],
              ['quadratische Gleichung', 'eine Gleichung mit x² als höchster Potenz; lösbar mit der Lösungsformel'],
              ['x₁, x₂, x₃', 'die erste, zweite und dritte Lösung']],
  'bild': {'typ': 'koordinaten', 'x': [-1, 4], 'y': [-4, 4], 'graphen': [{'art': 'poly', 'k': [0, 6, -5, 1], 'name': 'Höhe'}],
           'punkte': [{'x': 0, 'y': 0}, {'x': 2, 'y': 0}, {'x': 3, 'y': 0}], 'name_x': 'Stelle x', 'name_y': 'Höhe'},
  'schritte': ['Die Höhe ist 0, wenn x³ − 5x² + 6x = 0 gilt. In allen drei Teilen steckt mindestens ein x.',
               'Ein x ausklammern: x · (x² − 5x + 6) = 0.',
               'Ein Produkt ist 0, wenn ein Faktor 0 ist. Also ist x = 0 oder x² − 5x + 6 = 0.',
               'Die quadratische Gleichung hat die Lösungen 2 und 3, denn x² − 5x + 6 = (x − 2)(x − 3). Zusammen: ⟦x₁ = 0, x₂ = 2, x₃ = 3⟧.'],
  'regel': 'So löst du eine Gleichung ohne Zahlglied: die ⟦höchste gemeinsame Potenz von x ausklammern⟧. Dann nach dem ⟦Satz vom Nullprodukt⟧ '
           'jeden Faktor einzeln gleich 0 setzen und lösen.',
  'fehler': 'x³ − 5x² + 6x = 0 durch x zu teilen ist falsch: Dabei geht die Lösung ⟦x = 0⟧ verloren – dabei startet die Bahn genau dort auf Bodenhöhe. '
            'Durch x darf man nicht teilen, wenn x auch 0 sein kann. Ausklammern statt teilen.'},
 'nullprodukt': {
  'einstieg': 'Beim Einkaufen gilt: Anzahl mal Preis ergibt den Betrag. Der Betrag ist nur dann 0 €, wenn man nichts kauft oder wenn die Ware nichts kostet. '
              'Allgemein ist ein Produkt genau dann 0, wenn einer der Faktoren 0 ist. Steht eine Gleichung schon als Malaufgabe aus Klammern da, '
              'liest man ihre Lösungen deshalb Klammer für Klammer ab. Diese Schreibweise heißt ⟦Produktform⟧.',
  'woerter': [['Produktform', 'die linke Seite ist als Malaufgabe aus Klammern geschrieben, z. B. (x + 2)(x² − 9)'],
              ['Faktor', 'eine der Klammern, die miteinander malgenommen werden'],
              ['(x + 2)(x² − 9)', 'zwei Klammern direkt nebeneinander bedeuten: malnehmen'],
              ['±3', '„plus oder minus 3“: beide Zahlen 3 und −3'],
              ['L = {−3; −2; 3}', 'die Lösungsmenge: alle Lösungen in geschweiften Klammern']],
  'schritte': ['Gegeben ist (x + 2)(x² − 9)(x² + 1) = 0. Hier werden drei Faktoren malgenommen.',
               'Erster Faktor: x + 2 = 0 ergibt x = −2.',
               'Zweiter Faktor: x² − 9 = 0 heißt x² = 9. Das gilt für x = 3 und für x = −3, denn auch (−3)² = 9.',
               'Dritter Faktor: x² + 1 = 0 würde x² = −1 verlangen. Ein Quadrat ist nie negativ, also kommt hier nichts dazu. Zusammen: ⟦L = {−3; −2; 3}⟧.'],
  'regel': 'So liest du die Produktform: ⟦jeden Faktor einzeln gleich 0 setzen⟧ und lösen. Ein Faktor wie x² + 1 ist immer mindestens 1 '
           'und liefert ⟦keine Lösung⟧.',
  'fehler': 'Aus x² + 1 = 0 die Lösung x = −1 abzulesen ist falsch: (−1)² + 1 = 1 + 1 = 2 und nicht 0. Ein ⟦Quadrat plus eine positive Zahl⟧ ist nie 0 – '
            'wie eine Bestellung mit Versandkosten, die nie 0 € kostet.'},
 'substitution': {
  'einstieg': 'In der Klasse sagt niemand „Maximilian Alexander“, alle sagen kurz „Max“ – gemeint ist trotzdem dieselbe Person. '
              'Bei Gleichungen geht das genauso. In x⁴ − 10x² + 9 = 0 kommt x nur als x² und als x⁴ = (x²)² vor. '
              'Gibt man x² den Kurznamen z, wird daraus eine quadratische Gleichung. Dieses Umbenennen heißt ⟦Substitution⟧.',
  'woerter': [['x⁴', 'x · x · x · x, also (x²)²'],
              ['biquadratische Gleichung', 'eine Gleichung der Form ax⁴ + bx² + c = 0: nur x⁴, x² und eine Zahl'],
              ['a, b, c', 'Platzhalter für feste Zahlen'],
              ['Substitution', 'einen Teil durch einen neuen Buchstaben ersetzen, hier z = x²'],
              ['z₁, z₂', 'die beiden Lösungen der Gleichung mit z'],
              ['Rücksubstitution', 'am Ende wieder x² statt z schreiben und nach x lösen'],
              ['z ≥ 0', 'z ist größer oder gleich 0']],
  'schritte': ['Gegeben ist x⁴ − 10x² + 9 = 0. Setze z = x², dann ist x⁴ = z².',
               'Die Gleichung heißt jetzt z² − 10z + 9 = 0. Sie hat die Lösungen z₁ = 1 und z₂ = 9, denn z² − 10z + 9 = (z − 1)(z − 9).',
               'Rücksubstitution: Aus x² = 1 folgt x = 1 oder x = −1. Aus x² = 9 folgt x = 3 oder x = −3.',
               'Alle vier Lösungen zusammen: ⟦L = {−3; −1; 1; 3}⟧.'],
  'regel': 'So löst du ⟦ax⁴ + bx² + c = 0⟧: ⟦z = x² setzen⟧ und az² + bz + c = 0 lösen. Dann ⟦rücksubstituieren⟧: x² = z₁ und x² = z₂ lösen. '
           'Nur ein z ≥ 0 liefert Lösungen für x.',
  'fehler': 'Mit z₁ = 1 und z₂ = 9 aufzuhören ist unvollständig. Gefragt ist nach x, nicht nach dem Kurznamen z – wie wenn im Zeugnis nur „Max“ stünde. '
            'Erst die ⟦Rücksubstitution⟧ liefert die vier Lösungen.'},
 'vielfachheit': {
  'einstieg': 'Zurück zur Achterbahn. An manchen Stellen auf Bodenhöhe fährt die Bahn durch und taucht auf der anderen Seite in einen Graben ab. '
              'An anderen Stellen setzt sie nur kurz auf und steigt wieder. Ob sie hindurchfährt oder nur aufsetzt, verrät die ⟦Vielfachheit⟧ der Nullstelle.',
  'woerter': [['Nullstelle', 'eine Stelle x, an der der Wert 0 ist (Bahn auf Bodenhöhe)'],
              ['f(x)', 'der Wert der Funktion f an der Stelle x (hier: die Höhe)'],
              ['(x − 1)²', 'der Faktor (x − 1) kommt zweimal vor'],
              ['k-fache Nullstelle', 'der Faktor kommt k-mal vor: doppelt heißt 2-mal, dreifach 3-mal'],
              ['Vorzeichenwechsel', 'die Werte wechseln von positiv zu negativ oder umgekehrt (die Bahn fährt durch den Boden)'],
              ['berühren', 'der Graph setzt auf der x-Achse auf und kehrt um, ohne sie zu kreuzen'],
              ['gerade, ungerade', '2, 4, 6 … sind gerade Zahlen; 1, 3, 5 … ungerade']],
  'schritte': ['Gegeben ist f(x) = (x − 1)²(x + 2)³. Die Nullstellen sind 1 und −2.',
               'Der Faktor (x − 1) steht zweimal da, also ist 1 eine doppelte Nullstelle. Der Faktor (x + 2) steht dreimal da, also ist −2 eine dreifache Nullstelle.',
               'Bei x = 1: (x − 1)² ist links und rechts von 1 positiv. Das Vorzeichen von f ändert sich nicht, der Graph ⟦berührt⟧ die x-Achse nur.',
               'Bei x = −2: (x + 2)³ ist links von −2 negativ und rechts davon positiv. Dort gibt es einen ⟦Vorzeichenwechsel⟧, der Graph schneidet die x-Achse.'],
  'regel': 'So liest du die Vielfachheit: Kommt der Faktor (x − a) ⟦k-mal⟧ vor, ist a eine ⟦k-fache Nullstelle⟧. Ungerades k: ⟦Vorzeichenwechsel⟧, '
           'der Graph schneidet. Gerades k: kein Wechsel, der Graph berührt die x-Achse nur.',
  'fehler': '„(x − 1)² hat die Nullstellen 1 und −1“ ist falsch: Für x = −1 ist (−1 − 1)² = 4 und nicht 0. (x − 1)² ist nur für x = 1 gleich 0 – '
            'das ist ⟦eine doppelte⟧ Nullstelle, an der die Bahn nur aufsetzt.'},
 'verstehen': {
  'einstieg': 'Wie oft kann die Achterbahn auf Bodenhöhe sein? Das hängt von der höchsten Potenz in ihrer Gleichung ab. '
              'Eine Gleichung mit x⁴ hat höchstens vier Lösungen – es können aber auch weniger sein oder gar keine. Diese höchste Potenz heißt ⟦Grad⟧.',
  'woerter': [['Grad', 'die höchste Hochzahl von x in der Gleichung; bei x⁴ + 3x² + 2 ist er 4'],
              ['n-ten Grades', 'mit dem Grad n; n steht für eine Zahl'],
              ['höchstens', 'diese Anzahl oder weniger'],
              ['≥', '„größer oder gleich“']],
  'schritte': ['Behauptung: x⁴ + 3x² + 2 = 0 hat vier Lösungen, weil der Grad 4 ist.',
               'x⁴ und x² sind Quadrate (x⁴ = (x²)²), also nie negativ: x⁴ ≥ 0 und 3x² ≥ 0.',
               'Deshalb ist die linke Seite immer mindestens 0 + 0 + 2 = 2. Sie kann nie 0 werden.',
               'Die Gleichung hat ⟦keine Lösung⟧. Der Grad 4 sagt nur: höchstens vier Lösungen.'],
  'regel': 'So schätzt du die Zahl der Lösungen ab: Eine Gleichung n-ten Grades hat ⟦höchstens n⟧ Lösungen. Bei geradem Grad kann es ⟦keine⟧ geben, '
           'bei ungeradem Grad gibt es ⟦mindestens eine⟧.',
  'fehler': '„Grad 4 heißt genau 4 Lösungen“ ist falsch. Der Grad nennt nur die ⟦Höchstzahl⟧ – wie ein Aufzug „für höchstens 4 Personen“, '
            'der auch mit einer Person oder leer fährt.'},
}

GEN = schoen({'ausklammern': g_ausklammern, 'nullprodukt': g_nullprodukt, 'substitution': g_substitution, 'vielfachheit': g_vielfachheit,
              'verstehen': g_verstehen})

if __name__ == '__main__':
    bauen('gleichungen.polynom',
          'Gleichungen höheren Grades durch Ausklammern, Satz vom Nullprodukt oder Substitution lösen und Nullstellen mit Vielfachheit deuten.',
          ['Kein Zahlglied: höchste gemeinsame x-Potenz ausklammern (nie durch x teilen).', 'Produkt = 0: jeden Faktor null setzen.',
           'Biquadratisch: z = x², quadratisch lösen, rücksubstituieren (nur z ≥ 0).', 'k-fache Nullstelle: ungerade k mit, gerade k ohne Vorzeichenwechsel.'],
          [('Lösungsverfahren', ['ausklammern', 'nullprodukt', 'substitution']), ('Nullstellen deuten', ['vielfachheit', 'verstehen'])],
          ETAPPEN, GEN, klar=KLAR,
          meiden={'ausklammern': ['x³ − 5x² + 6x = 0'], 'substitution': ['x⁴ − 10x² + 9 = 0'], 'verstehen': ['x⁴ + 3x² + 2 = 0', 'x⁴ − 10x² + 9 = 0']},
          offen=['Zeichnungen: Graphen in den Lernkarten „ausklammern“, „substitution“, „vielfachheit“, „verstehen“; Aufgaben zum Vorzeichenwechsel und „Welcher Term passt zum Graphen?“ zeigen den Graphen. Selbst skizzieren kann das Kind in der App noch nicht (Lehrplan: „Graph skizzieren“).',
                 'Polynomdivision ist nicht enthalten (lehrplan_gym nennt nur Ausklammern und Substitution).',
                 'Lösungen werden als Lücken „x₁ = □; …“ ohne Wiederholung (aufsteigend) abgefragt; die Anzahl der Lücken verrät, wie viele Lösungen es gibt. Wer das vermeiden will, braucht einen Antworttyp „Lösungsmenge“.',
                 'Rechenausdruck c bei Lücken: „x + f(x)“ – ergibt nur dann x, wenn f(x) = 0, prüft also jede Lösung durch Einsetzen.',
                 'Prüfung eingearbeitet (Runde 3): Substitution mit nicht ganzzahligen Lösungen (zahl, Toleranz 0,01), Vorzeichenwechsel in Stufe 3/Korrektur/Sicherung ohne Grafik und Ja/Nein ausgewogen, Sachaufgaben (Quader, Schachtel aus Karton) in „verstehen“ Stufe 3.'])
