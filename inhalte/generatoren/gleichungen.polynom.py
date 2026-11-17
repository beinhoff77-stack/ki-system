#!/usr/bin/env python3
"""Thema gleichungen.polynom – Polynomgleichungen (Klasse 10). Schreibt inhalte/themen/gleichungen.polynom.json."""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import *  # noqa: E402,F403
from _schwer_kl10 import ergaenzen  # noqa: E402

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



# ---------- KLAR: Lernkarten im neuen Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst nach dem Bauen der Aufgaben eingesetzt (bauen(..., klar=KLAR)), die Aufgaben bleiben wörtlich gleich.
# Muster: einstieg (≤ 35 Wörter) → Kartenbild → Schritte als {text, bild} (Bildergeschichte) → „Pass auf!“ (fehler + fehler_bild) → MERKE (regel).
KLAR = {
 'ausklammern': {
  'einstieg': 'Ein Rechenmodell beschreibt die Höhe einer Achterbahn über dem Boden. Wo fährt sie genau auf Bodenhöhe? '
              'Weil in jedem Teil der Rechnung ein x steckt, hilft ⟦Ausklammern⟧.',
  'woerter': [['Ausklammern', 'einen gemeinsamen Faktor vor eine Klammer ziehen'],
              ['Zahlglied', 'eine Zahl ohne x in der Summe'],
              ['Satz vom Nullprodukt', 'ein Produkt ist 0, wenn ein Faktor 0 ist']],
  'bild': {'typ': 'koordinaten', 'x': [-1, 4], 'y': [-4, 4], 'graphen': [{'art': 'poly', 'k': [0, 6, -5, 1], 'name': 'Höhe'}],
           'name_x': 'Strecke', 'name_y': 'Höhe'},
  'schritte': [{'text': 'Höhe 0 heißt: x³ − 5x² + 6x = 0. Ein Zahlglied fehlt.'},
               {'text': 'x ausklammern: x · (x² − 5x + 6) = 0.'},
               {'text': 'Satz vom Nullprodukt: x = 0 oder x² − 5x + 6 = 0.', 'bild': {'punkte': [{'x': 0, 'y': 0, 'name': '0'}]}},
               {'text': 'Die Klammer ist (x − 2)(x − 3). Lösungen: ⟦0, 2 und 3⟧.',
                'bild': {'punkte': [{'x': 0, 'y': 0, 'name': '0'}, {'x': 2, 'y': 0, 'name': '2'}, {'x': 3, 'y': 0, 'name': '3'}]}}],
  'fehler': 'Durch x zu teilen ist falsch: Dabei geht die Lösung ⟦x = 0⟧ verloren. Gerade dort startet die Bahn auf Bodenhöhe.',
  'fehler_bild': {'punkte': [{'x': 0, 'y': 0, 'name': 'verloren!'}, {'x': 2, 'y': 0}, {'x': 3, 'y': 0}]},
  'regel': 'Fehlt das Zahlglied, klammere x aus. Dann jeden Faktor nach dem ⟦Satz vom Nullprodukt⟧ gleich 0 setzen.'},
 'nullprodukt': {
  'einstieg': 'Beim Einkauf gilt: Anzahl mal Preis ergibt den Betrag. Er ist nur 0 €, wenn eine der beiden Zahlen 0 ist. '
              'So liest man auch die ⟦Produktform⟧ einer Gleichung.',
  'woerter': [['Produktform', 'die Gleichung als Malaufgabe aus Klammern'],
              ['±3', 'plus 3 und minus 3, also beide Zahlen'],
              ['L', 'die Lösungsmenge: alle Lösungen in geschweiften Klammern']],
  'bild': {'typ': 'tabelle', 'kopf': ['Faktor', 'ist 0 bei'], 'zeilen': [['x + 2', '?'], ['x² − 9', '?'], ['x² + 1', '?']]},
  'schritte': [{'text': 'Gegeben: (x + 2)(x² − 9)(x² + 1) = 0. Drei Faktoren werden malgenommen.'},
               {'text': 'x + 2 = 0 gilt bei x = −2.', 'bild': {'zeilen': [['x + 2', '−2'], ['x² − 9', '?'], ['x² + 1', '?']]}},
               {'text': 'x² − 9 = 0 heißt x² = 9, also x = ±3.', 'bild': {'zeilen': [['x + 2', '−2'], ['x² − 9', '−3 und 3'], ['x² + 1', '?']]}},
               {'text': 'x² + 1 ist immer mindestens 1. Zusammen: ⟦L = {−3; −2; 3}⟧.',
                'bild': {'zeilen': [['x + 2', '−2'], ['x² − 9', '−3 und 3'], ['x² + 1', 'nie']]}}],
  'fehler': 'x² + 1 = 0 hat nicht die Lösung −1, denn (−1)² + 1 = 2. ⟦Quadrat plus 1⟧ ist nie 0 – wie ein Einkauf mit Versandkosten.',
  'fehler_bild': {'zeilen': [['x + 2', '−2'], ['x² − 9', '−3 und 3'], ['x² + 1', '−1? Probe: 2']]},
  'regel': 'Setze jeden Faktor einzeln gleich 0. Ein Faktor wie x² + 1 liefert ⟦keine Lösung⟧.'},
 'substitution': {
  'einstieg': 'In der Klasse heißt Maximilian nur „Max“, gemeint ist dieselbe Person. In x⁴ − 10x² + 9 = 0 nennt man x² kurz z. '
              'Dieses Umbenennen heißt ⟦Substitution⟧.',
  'woerter': [['Substitution', 'einen Teil durch einen neuen Buchstaben ersetzen: z = x²'],
              ['biquadratisch', 'nur x⁴, x² und eine Zahl kommen vor'],
              ['Rücksubstitution', 'am Ende wieder x² statt z schreiben und x ausrechnen']],
  'bild': {'typ': 'tabelle', 'kopf': ['z = x²', 'x'], 'zeilen': [['?', '?']]},
  'schritte': [{'text': 'Die Gleichung ist biquadratisch. Mit z = x² wird x⁴ zu z².'},
               {'text': 'Neu: z² − 10z + 9 = (z − 1)(z − 9) = 0.',
                'bild': {'zeilen': [['z = 1', '?'], ['z = 9', '?']]}},
               {'text': 'Rücksubstitution: x² = 1 ergibt ±1, x² = 9 ergibt ±3.',
                'bild': {'zeilen': [['z = 1', '−1 und 1'], ['z = 9', '−3 und 3']]}},
               {'text': 'Alle Lösungen: ⟦L = {−3; −1; 1; 3}⟧.'}],
  'fehler': 'Bei z = 1 und z = 9 aufzuhören ist unvollständig. Gefragt ist x, nicht der Kurzname z. Erst die ⟦Rücksubstitution⟧ liefert x.',
  'fehler_bild': {'zeilen': [['z = 1', 'fehlt!'], ['z = 9', 'fehlt!']]},
  'regel': 'Setze z = x² und löse die neue Gleichung. Dann ⟦rücksubstituieren⟧: Nur z ≥ 0 liefert Lösungen für x.'},
 'vielfachheit': {
  'einstieg': 'Die Achterbahn fährt an manchen Stellen durch den Boden in einen Graben. An anderen setzt sie nur kurz auf und steigt wieder. '
              'Das verrät die ⟦Vielfachheit⟧ der Nullstelle.',
  'woerter': [['Vielfachheit', 'wie oft der Faktor einer Nullstelle vorkommt'],
              ['Vorzeichenwechsel', 'die Werte wechseln von positiv zu negativ oder umgekehrt'],
              ['berührt', 'der Graph setzt auf der x-Achse auf und kehrt um']],
  'bild': {'typ': 'koordinaten', 'x': [-3, 2], 'y': [-10, 20], 'graphen': [{'art': 'poly', 'k': [8, -4, -10, 1, 4, 1], 'name': 'f'}]},
  'schritte': [{'text': 'f(x) = (x − 1)²(x + 2)³ hat die Nullstellen 1 und −2.',
                'bild': {'punkte': [{'x': 1, 'y': 0}, {'x': -2, 'y': 0}]}},
               {'text': '(x − 1) kommt zweimal vor: Vielfachheit 2, also gerade.',
                'bild': {'punkte': [{'x': 1, 'y': 0, 'name': 'doppelt'}, {'x': -2, 'y': 0}]}},
               {'text': 'Kein Vorzeichenwechsel: Der Graph ⟦berührt⟧ die x-Achse bei 1 nur.'},
               {'text': '(x + 2) kommt dreimal vor, ungerade: Vorzeichenwechsel, der Graph schneidet bei −2.',
                'bild': {'punkte': [{'x': 1, 'y': 0, 'name': 'doppelt'}, {'x': -2, 'y': 0, 'name': 'dreifach'}]}}],
  'fehler': '(x − 1)² hat nicht die Nullstellen 1 und −1, denn (−1 − 1)² = 4. Es gibt nur ⟦x = 1⟧, doppelt. Dort setzt die Bahn nur auf.',
  'fehler_bild': {'punkte': [{'x': 1, 'y': 0, 'name': '1: doppelt'}, {'x': -1, 'y': 4, 'name': 'bei −1: 4'}]},
  'regel': 'Kommt (x − a) k-mal vor, ist a eine k-fache Nullstelle. Ungerades k: ⟦Vorzeichenwechsel⟧. Gerades k: nur berühren.'},
 'verstehen': {
  'einstieg': 'Wie oft kann die Achterbahn auf Bodenhöhe sein? Bei einer Gleichung mit x⁴ höchstens viermal, vielleicht seltener oder nie. '
              'Die höchste Hochzahl heißt ⟦Grad⟧.',
  'woerter': [['Grad', 'die höchste Hochzahl von x in der Gleichung'],
              ['höchstens', 'diese Anzahl oder weniger']],
  'bild': {'typ': 'koordinaten', 'x': [-3, 3], 'y': [-2, 12], 'graphen': [{'art': 'poly', 'k': [2, 0, 3, 0, 1], 'name': 'x⁴ + 3x² + 2'}]},
  'schritte': [{'text': 'Behauptung: x⁴ + 3x² + 2 = 0 hat vier Lösungen, denn Grad 4.'},
               {'text': 'x⁴ und 3x² sind nie negativ, denn x⁴ = (x²)².'},
               {'text': 'Die linke Seite ist deshalb immer mindestens 2.', 'bild': {'punkte': [{'x': 0, 'y': 2, 'name': 'tiefster Wert 2'}]}},
               {'text': 'Die Gleichung hat ⟦keine Lösung⟧. Der Graph erreicht die x-Achse nie.'}],
  'fehler': '„Grad 4 heißt genau 4 Lösungen“ ist falsch. Der Grad nennt nur die ⟦Höchstzahl⟧ – wie ein Aufzug für höchstens 4 Personen.',
  'regel': 'Grad n heißt: ⟦höchstens n⟧ Lösungen. Bei geradem Grad kann es keine geben, bei ungeradem mindestens eine.'},
}


GEN = schoen({'ausklammern': g_ausklammern, 'nullprodukt': g_nullprodukt, 'substitution': g_substitution, 'vielfachheit': g_vielfachheit,
              'verstehen': g_verstehen})

# ---------- Zehnte Runde (Zweig schwer-kl10): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Zufallsstart (nur zum Mischen der Antworten); wird erst NACH bauen(...) aufgerufen, alte Aufgaben bleiben gleich.
# Vorbilder (Typ und Niveau, eigene Zahlen): Bayerischer Mathematik-Test 10 (2025, Aufgabe 1: Gleichung durch Ausklammern lösen,
# „Geben Sie einen Term an, sodass …“), Abitur Bayern Prüfungsteil A (2023: Grad aus Nullstellen begründen; IlluPA A2: x⁴ − kx² mit Parameter),
# Grundwissen G9 (faktorisieren, Vielfachheit ablesen). Rechenausdruck c bei Lücken wie oben: „x + f(x)“ prüft jede Lösung durch Einsetzen.
def schwer():
    start(10011)
    N = []

    def neu(l, s, a):
        a['l'], a['s'] = l, s
        N.append(a)

    def pc(expr, xs):
        return [f'({x}) + ({expr.replace("x", f"({x})")})' for x in xs]

    # --- ausklammern ---
    neu('ausklammern', 2, luecken('Löse 3x³ = 12x².', schab(2), 'Lösungen aufsteigend', [0, 4],
                                  '3x³ − 12x² = 0 ⇒ 3x²(x − 4) = 0 ⇒ x = 0 (doppelt) oder x = 4. Wer durch x² teilt, verliert x = 0.',
                                  'Alles auf eine Seite bringen, dann 3x² ausklammern. Nicht durch x² teilen!', c=pc('3*x**3 - 12*x**2', [0, 4])))
    neu('ausklammern', 2, luecken('Löse x⁵ − 16x³ = 0.', schab(3), 'Lösungen aufsteigend', [-4, 0, 4],
                                  'x³(x² − 16) = 0 ⇒ x = 0 (dreifach) oder x² = 16 ⇒ x = ±4.', 'Klammere die höchste gemeinsame Potenz x³ aus.',
                                  c=pc('x**5 - 16*x**3', [-4, 0, 4])))
    neu('ausklammern', 3, luecken('Die Gleichung x³ − kx = 0 hat die Lösung x = 5. Bestimme k und die beiden anderen Lösungen.', 'k = □; x₁ = □; x₂ = □',
                                  'k, dann die anderen Lösungen aufsteigend', [25, -5, 0],
                                  'x = 5 einsetzen: 125 − 5k = 0 ⇒ k = 25. Dann x(x² − 25) = 0 ⇒ x = 0 oder x = ±5. Neben 5 also −5 und 0.',
                                  'Setze x = 5 ein, um k zu finden. Danach x ausklammern.', c=['125 // 5', '-5 + ((-5)**3 - 25*(-5))', '0']))
    neu('ausklammern', 3, luecken('Löse 2x⁴ + 6x³ = 20x².', schab(3), 'Lösungen aufsteigend', [-5, 0, 2],
                                  '2x⁴ + 6x³ − 20x² = 0 ⇒ 2x²(x² + 3x − 10) = 0 ⇒ 2x²(x + 5)(x − 2) = 0 ⇒ x = 0, x = −5, x = 2.',
                                  'Erst alles auf eine Seite, dann 2x² ausklammern; die Klammer ist quadratisch.', c=pc('2*x**4 + 6*x**3 - 20*x**2', [-5, 0, 2])))
    neu('ausklammern', 3, luecken('Löse x²(x − 1) = 4(x − 1).', schab(3), 'Lösungen aufsteigend', [-2, 1, 2],
                                  'x²(x − 1) − 4(x − 1) = 0 ⇒ (x − 1)(x² − 4) = 0 ⇒ x = 1 oder x = ±2. Wer durch (x − 1) teilt, verliert x = 1.',
                                  'Nicht durch (x − 1) teilen: Bring alles auf eine Seite und klammere (x − 1) aus.', c=pc('x**2*(x - 1) - 4*(x - 1)', [-2, 1, 2])))
    neu('ausklammern', 3, luecken('Löse x³ = x²(x − 2) + 18.', schab(2), 'Lösungen aufsteigend', [-3, 3],
                                  'Rechts ausmultiplizieren: x³ = x³ − 2x² + 18. x³ fällt weg: 2x² = 18 ⇒ x² = 9 ⇒ x = ±3.',
                                  'Multipliziere die rechte Seite aus. Was passiert mit x³?', c=pc('x**3 - x**2*(x - 2) - 18', [-3, 3])))

    # --- nullprodukt ---
    neu('nullprodukt', 2, luecken('Löse (3x − 6)(x² + 2x) = 0.', schab(3), 'Lösungen aufsteigend', [-2, 0, 2],
                                  '3x − 6 = 0 ⇒ x = 2. x² + 2x = x(x + 2) = 0 ⇒ x = 0 oder x = −2.', 'Jeden Faktor null setzen; der zweite Faktor braucht noch Ausklammern.',
                                  c=pc('(3*x - 6)*(x**2 + 2*x)', [-2, 0, 2])))
    neu('nullprodukt', 2, luecken('Löse (x² − 9)(x² + 9) = 0.', schab(2), 'Lösungen aufsteigend', [-3, 3],
                                  'x² − 9 = 0 ⇒ x = ±3. x² + 9 = 0 hat keine Lösung, weil x² + 9 immer positiv ist.', 'Untersuche beide Faktoren einzeln.',
                                  c=pc('(x**2 - 9)*(x**2 + 9)', [-3, 3])))
    neu('nullprodukt', 3, auswahl('Welche Gleichung hat genau die Lösungen −2, 0 und 3?', 'x(x + 2)(x − 3) = 0',
                                  ['x(x − 2)(x + 3) = 0', '(x + 2)(x − 3) = 0', 'x + (x + 2)(x − 3) = 0'],
                                  'Zu x = −2 gehört der Faktor (x + 2), zu x = 3 der Faktor (x − 3), zu x = 0 der Faktor x. Die Summe x + … ist kein Produkt mehr.',
                                  'Welcher Faktor wird bei x = −2 null?'))
    neu('nullprodukt', 3, zahl('Wie viele verschiedene Lösungen hat (x² − 4)(x² − 5x + 6) = 0?',
                               'x² − 4 = 0 ⇒ x = ±2. x² − 5x + 6 = (x − 2)(x − 3) = 0 ⇒ x = 2 oder x = 3. Die 2 kommt doppelt vor: verschieden sind −2, 2, 3.',
                               'Löse beide Faktoren und streiche doppelte Lösungen.', 3, '3'))
    neu('nullprodukt', 3, zahl('Für welche positive Zahl a hat (x − a)(x² − 9) = 0 nur zwei verschiedene Lösungen?',
                               'x² − 9 = 0 liefert schon −3 und 3. Nur zwei verschiedene Lösungen gibt es, wenn x = a eine davon ist: a = 3 (oder a = −3). Positiv: a = 3.',
                               'Welche Lösungen liefert x² − 9 = 0 schon? Wann bringt (x − a) nichts Neues?', 3, '3'))
    neu('nullprodukt', 3, luecken('Löse (x − 1)³ = x − 1.', schab(3), 'Lösungen aufsteigend', [0, 1, 2],
                                  '(x − 1)³ − (x − 1) = 0 ⇒ (x − 1)((x − 1)² − 1) = 0. Also x − 1 = 0 oder (x − 1)² = 1, d. h. x − 1 = ±1. Lösungen: 0, 1, 2.',
                                  'Fasse x − 1 als einen Block auf und klammere ihn aus.', c=pc('(x - 1)**3 - (x - 1)', [0, 1, 2])))

    # --- substitution ---
    neu('substitution', 2, luecken('Löse x⁴ − 13x² + 36 = 0.', schab(4), 'Lösungen aufsteigend', [-3, -2, 2, 3],
                                   'z = x²: z² − 13z + 36 = 0 ⇒ z = 4 oder z = 9 ⇒ x = ±2 oder x = ±3.', 'Setze z = x² und löse die quadratische Gleichung.',
                                   c=pc('x**4 - 13*x**2 + 36', [-3, -2, 2, 3])))
    neu('substitution', 2, luecken('Löse x⁴ − 3x² − 4 = 0.', schab(2), 'Lösungen aufsteigend', [-2, 2],
                                   'z = x²: z² − 3z − 4 = 0 ⇒ z = 4 oder z = −1. Nur z = 4 ist möglich: x = ±2.', 'Prüfe beim Rücksubstituieren, ob z negativ ist.',
                                   c=pc('x**4 - 3*x**2 - 4', [-2, 2])))
    neu('substitution', 3, zahl('Für welche positive Zahl k hat x⁴ − kx² + 16 = 0 genau zwei Lösungen?',
                                'z = x²: z² − kz + 16 = 0. Genau zwei Lösungen für x gibt es, wenn z eine einzige (doppelte) positive Lösung hat: (z − 4)² = z² − 8z + 16. Also k = 8, dann x = ±2.',
                                'Wie viele Lösungen x liefert ein positives z? Was muss für die Gleichung in z dann gelten?', 8, '2 * 4'))
    neu('substitution', 3, luecken('Löse x⁶ − 9x³ + 8 = 0.', schab(2), 'Lösungen aufsteigend', [1, 2],
                                   'z = x³: z² − 9z + 8 = 0 ⇒ z = 1 oder z = 8. x³ = 1 ⇒ x = 1; x³ = 8 ⇒ x = 2.',
                                   'Hier passt z = x³. Jede Zahl hat genau eine dritte Wurzel.', c=pc('x**6 - 9*x**3 + 8', [1, 2])))
    neu('substitution', 3, luecken('Löse (x² − 3)² − 4(x² − 3) − 12 = 0.', schab(4), 'Lösungen aufsteigend', [-3, -1, 1, 3],
                                   'u = x² − 3: u² − 4u − 12 = 0 ⇒ u = 6 oder u = −2. x² − 3 = 6 ⇒ x = ±3; x² − 3 = −2 ⇒ x = ±1.',
                                   'Ersetze den Block x² − 3 durch eine neue Variable. Nicht ausmultiplizieren!', c=pc('(x**2 - 3)**2 - 4*(x**2 - 3) - 12', [-3, -1, 1, 3])))
    neu('substitution', 3, auswahl('Jemand löst x⁴ − 5x² − 36 = 0 und schreibt L = {−3; −2; 2; 3}. Was stimmt?', 'Falsch: z = −4 liefert keine Lösung, L = {−3; 3}.',
                                   ['Richtig.', 'Falsch: L = {−4; 9}.', 'Falsch: L = {−9; 4}.'],
                                   'z² − 5z − 36 = 0 ⇒ z = 9 oder z = −4. x² = 9 ⇒ x = ±3. x² = −4 ist unmöglich; ±2 sind falsch (Probe: 16 − 20 − 36 ≠ 0).',
                                   'Mache die Probe mit x = 2.'))

    # --- vielfachheit ---
    neu('vielfachheit', 2, zahl('f(x) = x³ · (x − 2)² · (x + 1). Welchen Grad hat f?', 'Die Exponenten addieren sich: 3 + 2 + 1 = 6.',
                                'Beim Ausmultiplizieren entsteht als höchste Potenz x hoch (Summe der Vielfachheiten).', 6, '3 + 2 + 1'))
    neu('vielfachheit', 2, zahl('Es gilt x⁴ − 6x³ + 9x² = x²(x − 3)². Welche Vielfachheit hat die Nullstelle x = 3?', 'Der Faktor (x − 3) steht im Quadrat: doppelte Nullstelle.',
                                'Zähle, wie oft der Faktor (x − 3) vorkommt.', 2, '2'))
    neu('vielfachheit', 3, zahl('f(x) = x⁵ − 8x³ + 16x. Welche Vielfachheit hat die Nullstelle x = 2?',
                                'f(x) = x(x⁴ − 8x² + 16) = x(x² − 4)² = x(x − 2)²(x + 2)². Also ist x = 2 eine doppelte Nullstelle.',
                                'Klammere x aus. Die Klammer ist ein Quadrat (binomische Formel).', 2, '2 + (2**5 - 8*2**3 + 16*2)'))
    neu('vielfachheit', 3, zahl('Eine ganzrationale Funktion hat bei x = 1 eine doppelte und bei x = −2 eine dreifache Nullstelle. Welchen Grad hat sie mindestens?',
                                'Sie enthält mindestens die Faktoren (x − 1)² und (x + 2)³. Das ergibt mindestens Grad 2 + 3 = 5.',
                                'Schreibe die nötigen Faktoren auf und addiere die Exponenten.', 5, '2 + 3'))
    neu('vielfachheit', 3, zahl('An wie vielen Stellen wechselt f(x) = (x − 1)² · (x + 3)³ · (x − 4) das Vorzeichen?',
                                'Vorzeichenwechsel nur bei ungerader Vielfachheit: x = −3 (dreifach) und x = 4 (einfach). Bei x = 1 (doppelt) berührt der Graph nur.',
                                'Prüfe jede Nullstelle: gerade oder ungerade Vielfachheit?', 2, '2'))
    neu('vielfachheit', 3, zahl('Für welche positive Zahl a hat f(x) = x · (x − 2) · (x − a)² eine dreifache Nullstelle?',
                                'Eine dreifache Nullstelle entsteht, wenn (x − a)² mit einem anderen Faktor zusammenfällt. a = 2 gibt (x − 2)³. (a = 0 gäbe x³, ist aber nicht positiv.)',
                                'Mit welchem anderen Faktor kann (x − a)² zusammenfallen?', 2, '2'))

    # --- verstehen ---
    neu('verstehen', 2, auswahl('Welche Gleichung hat keine reelle Lösung?', 'x⁴ + 2x² + 1 = 0', ['x⁴ − 2x² + 1 = 0', 'x³ + 1 = 0', 'x⁴ − 1 = 0'],
                                'x⁴ + 2x² + 1 = (x² + 1)² ist immer mindestens 1. Die anderen haben x = ±1 bzw. x = −1 als Lösung.',
                                'Erkennst du eine binomische Formel?'))
    neu('verstehen', 2, zahl('Eine Gleichung 5. Grades hat die Lösungen 0, 1 und 2. Wie viele weitere Lösungen kann sie höchstens noch haben?',
                             'Grad 5: höchstens 5 Lösungen. Drei sind bekannt, also höchstens 2 weitere.', 'Wie viele Lösungen hat eine Gleichung 5. Grades höchstens?', 2, '5 - 3'))
    neu('verstehen', 3, auswahl('Welche Gleichung 4. Grades hat genau drei verschiedene Lösungen?', 'x²(x² − 1) = 0',
                                ['x⁴ − 1 = 0', 'x⁴ − 5x² + 4 = 0', 'x⁴ + x² = 0'],
                                'x²(x² − 1) = 0: x = 0 (doppelt), x = ±1 – drei verschiedene. x⁴ − 1 = 0: ±1; x⁴ − 5x² + 4 = 0: ±1, ±2; x⁴ + x² = 0: nur 0.',
                                'Löse jede Gleichung kurz und zähle verschiedene Lösungen.'))
    neu('verstehen', 3, luecken('Der Graph einer Funktion 3. Grades mit Leitkoeffizient 1 schneidet die x-Achse bei x = −3 und berührt sie bei x = 1. Gib den Term ausmultipliziert an.',
                                'x³ + □x² + □x + □', 'Koeffizienten', [1, -5, 3],
                                'Schneiden: einfacher Faktor (x + 3). Berühren: doppelter Faktor (x − 1)². f(x) = (x + 3)(x² − 2x + 1) = x³ + x² − 5x + 3.',
                                'Welche Vielfachheit gehört zu „berühren“? Stelle erst die Produktform auf.', c=['-2 + 3', '1 - 6', '3']))
    neu('verstehen', 3, zahl('Verlängert man jede Kante eines Würfels um 2 cm, wächst sein Volumen um 152 cm³. Wie lang war eine Kante?',
                             '(x + 2)³ − x³ = 152 ⇒ 6x² + 12x + 8 = 152 ⇒ x² + 2x − 24 = 0 ⇒ (x + 6)(x − 4) = 0. Eine Länge ist positiv: x = 4 cm.',
                             'Stelle (x + 2)³ − x³ = 152 auf. Beim Ausmultiplizieren fällt x³ weg.', 4, '4 + ((4 + 2)**3 - 4**3 - 152)', einheit='cm'))
    neu('verstehen', 3, auswahl('Jemand sagt: „x³ = −27 hat keine Lösung, weil man aus negativen Zahlen keine Wurzel ziehen kann.“ Was stimmt?',
                                'Falsch: x = −3, denn (−3)³ = −27.', ['Richtig.', 'Falsch: x = 3 und x = −3.', 'Falsch: x = −9.'],
                                'Eine ungerade Potenz einer negativen Zahl ist negativ: (−3)³ = −27. Nur bei geraden Potenzen gibt es keine Lösung für negative Werte.',
                                'Rechne (−3)³ aus.'))
    return N


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('gleichungen.polynom', 13_10_2)
# a) gleicher Typ wie Stufe 2
BF.stufe('verstehen', 'Jemand löst x³ = 4x, indem er durch x teilt, und erhält x = ±2. Was stimmt?', 2)
BF.stufe('vielfachheit', 'f(x) = (x + 2)² · (x − 2)³. Wechselt f bei x = 2 das Vorzeichen?', 2)
BF.nicht_umgesetzt('vielfachheit: Ablenker „Nein, die Nullstelle ist 3-fach (ungerade)“ in sich widersprüchlich', 'Laut Befund kein Fehler; als Ablenker zulässig (prüft, ob man „ungerade ⇒ Wechsel“ kennt).')
BF.nicht_umgesetzt('Lückenaufgaben „x₁ = □; x₂ = □ …“ verraten die Zahl der Lösungen', 'Steht bereits unter „offen“; Runde 10 fragt die Anzahl teils als Zahl ab. Ein Umbau aller Lückenaufgaben wäre keine Einzelkorrektur.')

# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    datei = bauen('gleichungen.polynom',
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
    ergaenzen(datei, schwer())
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden


# ---------- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl10) ----------
# Gesamtdurchsicht: jede Lernkarte und jede Aufgabe gelesen und nachgerechnet. Läuft ganz am Ende auf der fertigen Datei.
def durchsicht():
    from _durchsicht_kl10 import Durchsicht
    D = Durchsicht('gleichungen.polynom', 19070)
    # ausklammern: x⁴ − ax² bzw. x²(x² + bx + c) = Stufe-1/2-Rechnung mit x² statt x
    D.stufe(range(12, 18), 2, 'Löse ')
    # nullprodukt: der Faktor x² + c ohne Lösung ist die Falle der Lernkarte, drei Faktoren ihr Beispiel → Stufe 2
    D.stufe([40, 41, 42, 43, 44, 45], 2, 'Löse (x')
    # substitution: „L = { }“ dreimal auf Stufe 3; Wurzel-Lösungen sind die Stufe-2-Rechnung mit Rundung
    D.stufe([69, 71], 2, 'Welche Lösungsmenge hat')
    D.stufe([70, 73], 2, 'Löse x⁴')
    # vielfachheit: Vorzeichenwechsel und Grad eines Produkts stehen schon auf Stufe 2
    D.stufe(99, 2, 'f(x) = (x + 4)³')
    D.stufe(101, 2, 'f(x) = (x − 4)³')
    # verstehen: Graph zuordnen und fehlende Rücksubstitution stehen gleich auf Stufe 2; fünfmal „durch x geteilt“ auf Stufe 2 – zwei ersetzt
    D.stufe(128, 2, 'Welcher Funktionsterm passt')
    D.stufe(129, 2, 'Bei x⁴ − 61x² + 900 = 0')
    D.ersetze(121, 'Jemand löst x³ = 36x',
              D.Z('Wie viele reelle Lösungen hat die Gleichung x⁴ − 16 = 0?', 2, '2',
                  'x⁴ − 16 = (x² − 4)(x² + 4) = 0. x² = 4 ergibt x = ±2; x² = −4 hat keine Lösung. Also 2 Lösungen.',
                  'Zerlege mit der dritten binomischen Formel in zwei Faktoren.'))
    D.ersetze(125, 'Jemand löst x³ = 4x',
              D.A('Jemand sagt: „x⁴ = 81 hat nur die Lösung x = 3.“ Was stimmt?', 'Falsch: Auch x = −3 ist Lösung, denn (−3)⁴ = 81.',
                  ['Richtig.', 'Falsch: x = 81 : 4.', 'Falsch: Die Lösungen sind 3 und 9.'],
                  'Bei geradem Exponenten gibt es zwei Lösungen mit entgegengesetztem Vorzeichen: x = ±3. Probe: (−3)⁴ = 81.',
                  'Was ergibt (−3)⁴?'))
    D.anwenden()


if __name__ == '__main__':
    durchsicht()  # Neunzehnte Runde (durchsicht-kl10) – ganz am Ende


# ---------- STUFEN (Zwanzigste Runde, Zweig stufen-kl10) ----------
def stufen():
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _stufen_kl10 import Stufen
    S = Stufen('gleichungen.polynom', 2070)
    Z, A, L = S.Z, S.A, S.L

    # --- ausklammern ---
    S.stufenleiter('ausklammern', 'x ausklammern und mit dem Satz vom Nullprodukt lösen; erkennen, wann das geht.',
                   'Quadratische Klammer lösen, x² ausklammern, erst umstellen, Graph und Sachsituation.',
                   'Parameter aus einer Lösung, Gleichungen mit (x − 1) auf beiden Seiten, Fehler „durch x teilen“, Begründen, Koeffizienten rückwärts, binomische Formel.')
    S.g('ausklammern', direkt=[0, 5, 1, 2, 4, 3], mehrschritt=[6, 10, 7, 8, 9, 11, 12, 15, 17, 13, 14, 16, 141], umkehr=[140],
        parameter=[142], pruefung=[143], transfer=[144, 145])
    S.ueberzaehlig(5, 2, 4, 10, 7, 9, 11, 14, 15, 16, 141)
    S.neu('ausklammern', 'erkennen', A('Welche Gleichung kann man direkt durch Ausklammern von x lösen?', 'x³ − 4x² + 3x = 0', ['x³ − 4x² + 3 = 0', 'x² + 5 = 0', 'x³ = 8'],
                                       'Nur dort hat jedes Glied mindestens ein x und rechts steht 0: x(x² − 4x + 3) = 0.', 'Hat jedes Glied ein x? Steht rechts 0?'))
    S.neu('ausklammern', 'erkennen', A('x · (x² − 4) = 0. Was folgt nach dem Satz vom Nullprodukt?', 'x = 0 oder x² − 4 = 0', ['x = 0 und x² − 4 = 0 gleichzeitig', 'nur x² − 4 = 0', 'x = 4'],
                                       'Ein Produkt ist 0, wenn mindestens ein Faktor 0 ist – das „oder“ zählt.', 'Wann ist ein Produkt null?'))
    S.neu('ausklammern', 'einkleidung', Z('Ein geworfener Ball hat die Höhe h(t) = −t³ + 4t² (t in s, h in m, nur für 0 ≤ t ≤ 4). Wann ist er nach dem Abwurf wieder auf Höhe 0?', 4, '4',
                                          '−t³ + 4t² = t²(4 − t) = 0 ⇒ t = 0 (Abwurf) oder t = 4.', 'Klammere t² aus.', einheit='s'))
    S.neu('ausklammern', 'darstellung', A('Der Graph von f(x) = x³ − x schneidet die x-Achse dreimal. An welchen Stellen?', '−1, 0 und 1', ['nur bei 0', '0 und 1', '−1 und 1'],
                                          'x³ − x = x(x² − 1) = x(x − 1)(x + 1) = 0.', 'Klammere x aus.'))
    S.neu('ausklammern', 'fehler', A('Jemand löst x³ − 4x² = 0 so: „x³ = 4x², durch x² teilen: x = 4.“ Was stimmt?', 'Unvollständig: Auch x = 0 ist Lösung; durch x² darf man nur für x ≠ 0 teilen.',
                                     ['Richtig, x = 4 ist die einzige Lösung.', 'Falsch: x = 2.', 'Falsch: x = −4 ist die einzige Lösung.'],
                                     'x²(x − 4) = 0 ⇒ x = 0 oder x = 4. Beim Teilen durch x² geht die Lösung 0 verloren.', 'Was passiert, wenn x = 0 ist?'))
    S.neu('ausklammern', 'begruenden', A('Hat jede Gleichung der Form x³ + bx² + cx = 0 die Lösung x = 0?', 'Ja: x lässt sich ausklammern, und x = 0 macht das Produkt null.',
                                         ['Nein, nur wenn c = 0 ist.', 'Nein, nur wenn b und c positiv sind.', 'Ja, aber nur für b = c.'],
                                         'x(x² + bx + c) = 0: Für x = 0 ist der erste Faktor 0 – egal, wie b und c sind.', 'Setze x = 0 ein.'))
    S.neu('ausklammern', 'verknuepfen', Z('Löse x³ − 6x² + 9x = 0. Gib die Lösung an, die nicht 0 ist.', 3, '3', 'x(x² − 6x + 9) = x(x − 3)² = 0 ⇒ x = 0 oder x = 3 (doppelt).', 'Die Klammer ist eine binomische Formel.'))
    S.neu('ausklammern', 'rueckwaerts', L('Die Gleichung x³ + bx² + cx = 0 hat die Lösungen 0, 2 und 5. Bestimme b und c.', 'b = □; c = □', [-7, 10], ['-(2 + 5)', '2 * 5'],
                                          'x(x − 2)(x − 5) = x(x² − 7x + 10) = x³ − 7x² + 10x. Also b = −7, c = 10.', 'Schreibe die Gleichung in Produktform und multipliziere aus.', hinweis='ganze Zahlen mit Vorzeichen'))
    S.bonus('ausklammern', Z('Wie viele reelle Lösungen hat x⁵ = x?', 3, '3', 'x⁵ − x = x(x⁴ − 1) = x(x² − 1)(x² + 1) = 0. Lösungen 0, 1, −1; x² + 1 ist nie 0. Also 3.',
                             'Bringe alles auf eine Seite und klammere aus.'))
    S.bonus('ausklammern', Z('Für welche positive ganze Zahl n hat x³ − nx² + 4x = 0 genau zwei verschiedene Lösungen?', 4, '4',
                             'x(x² − nx + 4) = 0. Neben 0 braucht die Klammer genau eine (doppelte) Lösung: n² − 16 = 0 ⇒ n = 4 (Lösung x = 2). Dass 0 Lösung der Klammer ist, geht nicht (4 ≠ 0).',
                             'Wann hat eine quadratische Gleichung genau eine Lösung?'))

    # --- nullprodukt ---
    S.stufenleiter('nullprodukt', 'In einer Produktform jeden Faktor null setzen.',
                   'Faktoren wie x² − a² und x² + c, doppelte Faktoren, Nullstellen am Graphen.',
                   'Gleichung zu vorgegebenen Lösungen, Zahl der Lösungen, Parameter, Fehler „= 6 statt = 0“, Faktoren ohne Lösung begründen, Lösungsmenge wie im BMT, rückwärts.')
    S.g('nullprodukt', direkt=[28, 29, 31, 30, 32, 33], mehrschritt=[34, 35, 39, 36, 37, 38, 43, 146], umkehr=[40, 41, 44, 45, 42, 147],
        rueckwaerts=[148], verknuepfen=[149], parameter=[150], transfer=[151])
    S.ueberzaehlig(31, 32, 33, 35, 39, 37, 38, 41, 44, 45)
    S.neu('nullprodukt', 'erkennen', A('Wann ist ein Produkt aus mehreren Faktoren gleich 0?', 'wenn mindestens ein Faktor 0 ist', ['nur wenn alle Faktoren 0 sind', 'wenn ein Faktor negativ ist', 'wenn die Summe der Faktoren 0 ist'],
                                       'Satz vom Nullprodukt: Ein Faktor 0 genügt.', 'Was ist 0 mal irgendetwas?'))
    S.neu('nullprodukt', 'erkennen', A('Welcher Faktor liefert in (x − 4)(x² + 9) = 0 keine Lösung?', 'x² + 9', ['x − 4', 'beide Faktoren', 'keiner der Faktoren'],
                                       'x² + 9 ist immer mindestens 9. Nur x − 4 = 0 liefert x = 4.', 'Kann x² + 9 null werden?'))
    S.neu('nullprodukt', 'darstellung', A('An welchen Stellen schneidet der Graph von f(x) = (x + 1)(x² − 4) die x-Achse?', '−2, −1 und 2', ['nur bei −1', '−1 und 4', '−4, −1 und 4'],
                                          'x + 1 = 0 ⇒ −1; x² − 4 = 0 ⇒ ±2.', 'Setze jeden Faktor null.'))
    S.neu('nullprodukt', 'fehler', A('Jemand löst (x − 2)(x + 3) = 6 so: „x − 2 = 6 oder x + 3 = 6, also x = 8 oder x = 3.“ Was stimmt?', 'Falsch: Der Satz vom Nullprodukt gilt nur, wenn rechts 0 steht.',
                                     ['Richtig.', 'Falsch: x = 2 oder x = −3.', 'Falsch: Es gibt keine Lösung.'],
                                     'Probe x = 8: 6 · 11 = 66 ≠ 6. Richtig: ausmultiplizieren, x² + x − 12 = 0 ⇒ x = 3 oder x = −4.', 'Mach die Probe mit x = 8.'))
    S.neu('nullprodukt', 'begruenden', A('Hat die Gleichung (x² + 4)(x⁴ + 1) = 0 eine Lösung?', 'Nein: Beide Faktoren sind immer positiv.', ['Ja: x = ±2.', 'Ja: x = ±1.', 'Ja: x = 0.'],
                                         'x² + 4 ≥ 4 und x⁴ + 1 ≥ 1. Ein Produkt positiver Zahlen ist nie 0.', 'Kann einer der Faktoren 0 werden?'))
    S.neu('nullprodukt', 'pruefung', L('Bestimme alle Lösungen von x(x − 1)(x² − 16) = 0 (kleinste zuerst).', 'x₁ = □; x₂ = □; x₃ = □; x₄ = □', [-4, 0, 1, 4], ['-4', '0', '1', '4'],
                                       'x = 0, x = 1 und x² = 16 ⇒ x = ±4. Sortiert: −4, 0, 1, 4.', 'Setze jeden Faktor null.', hinweis='kleinste zuerst'))
    S.neu('nullprodukt', 'rueckwaerts', Z('Die Gleichung (x − a)(x − 2a) = 0 hat die Lösung 6, die andere Lösung ist kleiner. Welche?', 3, '6 // 2',
                                          'Entweder a = 6 (dann ist 2a = 12 größer – passt nicht) oder 2a = 6, also a = 3. Die andere Lösung ist 3.', 'Welcher Faktor kann 6 liefern?'))
    S.bonus('nullprodukt', Z('Wie viele Lösungen hat (x − 1)(x − 2)(x − 3) = (x − 1)(x − 2)(x − 4)?', 2, '2',
                             'Alles nach links: (x − 1)(x − 2)[(x − 3) − (x − 4)] = (x − 1)(x − 2) · 1 = 0 ⇒ x = 1 oder x = 2. Wer durch (x − 1)(x − 2) teilt, erhält −3 = −4 und übersieht beide Lösungen.',
                             'Teile nicht – klammere den gemeinsamen Teil aus.'))
    S.bonus('nullprodukt', Z('(x − a)(x − b) = 0 hat die Lösungen 3 und 7. Welche größere Lösung hat (2x − a)(2x − b) = 0?', 3.5, '7 / 2',
                             'a und b sind 3 und 7. 2x = 3 oder 2x = 7 ⇒ x = 1,5 oder 3,5. Die größere ist 3,5.', 'Bestimme zuerst a und b.'))

    # --- substitution ---
    S.stufenleiter('substitution', 'Biquadratische Gleichungen erkennen und mit z = x² in eine quadratische Gleichung übersetzen.',
                   'Vollständig lösen mit Rücksubstitution, negative z, Dezimalwerte, Sachsituation.',
                   'Faktor vor x⁴, Parameter k, x⁶ und Klammer-Substitution, Fehler mit negativem z, genau drei Lösungen begründen, Koeffizienten rückwärts.')
    S.g('substitution', direkt=[56, 57, 58, 59, 60, 61], mehrschritt=[62, 63, 64, 65, 66, 67, 152, 70, 73, 153], umkehr=[68, 69, 71],
        pruefung=[72], parameter=[154], transfer=[155, 156], fehler=[157])
    S.ueberzaehlig(63, 73)
    S.neu('substitution', 'erkennen', A('Welche Gleichung ist biquadratisch?', 'x⁴ − 5x² + 4 = 0', ['x³ − 5x + 4 = 0', 'x⁴ − 5x³ + 4 = 0', 'x⁴ − 5x = 0'],
                                        'Biquadratisch: nur x⁴, x² und eine Zahl.', 'Welche Hochzahlen kommen vor?'))
    S.neu('substitution', 'erkennen', A('Was wird aus x⁴ − 13x² + 36 = 0 mit z = x²?', 'z² − 13z + 36 = 0', ['z⁴ − 13z² + 36 = 0', 'z − 13z + 36 = 0', 'z² − 13 + 36 = 0'],
                                        'x⁴ = (x²)² = z² und x² = z.', 'Schreibe x⁴ als (x²)².'))
    S.neu('substitution', 'einkleidung', Z('Ein Quadrat hat die Seite x cm und den Flächeninhalt A = x² cm². Es gilt A² − 20A + 64 = 0, und die Fläche ist größer als 5 cm². Wie lang ist die Seite?', 4, '4',
                                           'A² − 20A + 64 = (A − 4)(A − 16) = 0 ⇒ A = 4 oder A = 16. Wegen A > 5 ist A = 16, also x = 4 cm.', 'Löse zuerst nach A, dann nach x.', einheit='cm'))
    S.neu('substitution', 'begruenden', A('Kann eine biquadratische Gleichung genau drei verschiedene Lösungen haben?', 'Ja, wenn z = 0 eine Lösung ist, z. B. x⁴ − x² = 0 mit −1, 0 und 1.',
                                          ['Nein, immer 0, 2 oder 4.', 'Ja, z. B. x⁴ − 5x² + 4 = 0.', 'Nein, weil Lösungen immer paarweise ±x vorkommen.'],
                                          'Zu z > 0 gehören zwei Lösungen ±√z, zu z = 0 nur x = 0. So entsteht eine ungerade Anzahl.', 'Was liefert z = 0?'))
    S.neu('substitution', 'rueckwaerts', Z('Eine Gleichung x⁴ + bx² + c = 0 hat genau die Lösungen ±1 und ±4. Bestimme c.', 16, '1 * 16',
                                           'Die z-Werte sind 1 und 16: (z − 1)(z − 16) = z² − 17z + 16. Also c = 16 (b = −17).', 'Welche Lösungen hat die Gleichung für z?'))
    S.neu('substitution', 'verknuepfen', Z('Löse (x² − 1)² = 9. Gib die positive Lösung an.', 2, '2', 'x² − 1 = 3 oder x² − 1 = −3. Also x² = 4 (x = ±2) oder x² = −2 (keine Lösung).',
                                           'Ziehe zuerst die Wurzel: Welche Zahlen ergeben quadriert 9?'))
    S.bonus('substitution', Z('Für wie viele ganze Zahlen k mit 1 ≤ k ≤ 10 hat x⁴ − kx² + 9 = 0 genau vier verschiedene Lösungen?', 4, '10 - 7 + 1',
                              'Vier Lösungen brauchen zwei verschiedene positive z in z² − kz + 9 = 0. Ihr Produkt ist 9 > 0, ihre Summe k > 0, also beide positiv, sobald es zwei gibt: k² − 36 > 0 ⇒ k > 6. k = 7, 8, 9, 10.',
                              'Welche Bedingung braucht z² − kz + 9 = 0?'))
    S.bonus('substitution', Z('Wie viele reelle Lösungen hat x⁸ − 17x⁴ + 16 = 0?', 4, '4',
                              'Mit z = x⁴: z² − 17z + 16 = (z − 1)(z − 16) = 0. x⁴ = 1 ⇒ x = ±1; x⁴ = 16 ⇒ x = ±2. Vier Lösungen.', 'Substituiere diesmal z = x⁴.'))

    # --- vielfachheit ---
    S.stufenleiter('vielfachheit', 'Die Vielfachheit einer Nullstelle an der Hochzahl der Klammer ablesen.',
                   'Vorzeichenwechsel aus der Vielfachheit, Grad einer Produktform, Vielfachheit aus einer Zerlegung.',
                   'Doppelte Lösungen durch binomische Formeln, Mindestgrad, Zahl der Vorzeichenwechsel, Parameter, Fehler, Begründen.')
    S.g('vielfachheit', direkt=[84, 85, 86, 87, 88, 89], darstellung=[90, 91, 92, 93, 94, 95], umkehr=[96, 99, 159], mehrschritt=[101, 158],
        verknuepfen=[97, 98, 100], transfer=[160, 162], rueckwaerts=[161], parameter=[163])
    S.ueberzaehlig(87, 88, 89, 92, 93, 94, 95, 99)
    S.neu('vielfachheit', 'erkennen', A('Welcher Faktor gehört zu einer doppelten Nullstelle bei x = −3?', '(x + 3)²', ['(x − 3)²', '2(x + 3)', '(x + 3)³'],
                                        'Nullstelle −3: Klammer (x + 3); doppelt: Hochzahl 2.', 'Welche Klammer wird bei x = −3 null?'))
    S.neu('vielfachheit', 'erkennen', A('Bei welchen Nullstellen wechselt der Graph das Vorzeichen?', 'bei Nullstellen mit ungerader Vielfachheit', ['bei Nullstellen mit gerader Vielfachheit', 'bei allen Nullstellen', 'bei keiner Nullstelle'],
                                        'Ungerade Vielfachheit: Schnitt mit Vorzeichenwechsel; gerade: Berührung.', 'Denke an x und an x².'))
    S.neu('vielfachheit', 'fehler', A('Jemand sagt: „f(x) = (x − 2)² · (x + 1) wechselt bei x = 2 das Vorzeichen.“ Was stimmt?', 'Falsch: Bei der doppelten Nullstelle 2 berührt der Graph nur, ohne Vorzeichenwechsel.',
                                      ['Richtig.', 'Falsch: f hat bei 2 keine Nullstelle.', 'Falsch: f wechselt nur bei 2 das Vorzeichen, nicht bei −1.'],
                                      '(x − 2)² ist links und rechts von 2 positiv – das Vorzeichen bestimmt nur (x + 1).', 'Welches Vorzeichen hat (x − 2)² links und rechts von 2?'))
    S.neu('vielfachheit', 'begruenden', A('Eine ganzrationale Funktion vom Grad 4 hat eine dreifache Nullstelle a. Hat sie noch eine weitere Nullstelle?',
                                          'Ja: Der übrige Faktor ist linear und liefert eine Nullstelle (ist sie gleich a, ist a vierfach).',
                                          ['Nein, nie.', 'Nur wenn der Leitkoeffizient positiv ist.', 'Ja, und zwar immer zwei weitere.'],
                                          'f(x) = (x − a)³ · (c · x + d) mit c ≠ 0: Der lineare Faktor ist bei x = −d/c null.', 'Welcher Grad bleibt für den übrigen Faktor?'))
    S.bonus('vielfachheit', Z('f(x) = (x − 1)(x − 2)²(x − 3)³(x − 4)⁴. An wie vielen Nullstellen wechselt f das Vorzeichen?', 2, '2',
                              'Vorzeichenwechsel nur bei ungerader Vielfachheit: x = 1 (einfach) und x = 3 (dreifach). Zwei Stellen.', 'Welche Vielfachheiten sind ungerade?'))
    S.bonus('vielfachheit', Z('Welchen Grad hat f(x) = (x − 1)(x − 2)²(x − 3)³ · … · (x − 10)¹⁰?', 55, '10 * 11 // 2',
                              'Der Grad ist die Summe der Vielfachheiten: 1 + 2 + … + 10 = 55 (Gauß: 10 · 11 : 2).', 'Addiere alle Hochzahlen geschickt.'))

    # --- verstehen ---
    S.stufenleiter('verstehen', 'Einfache Potenzgleichungen lösen und die höchstmögliche Zahl von Lösungen kennen.',
                   'Graph und Term zuordnen, Lösungen zählen, Gleichungen ohne Lösung erkennen, Würfelkante aus dem Volumen.',
                   'Fehler beim Teilen und bei der Rücksubstitution, Aussagen begründen, Sachaufgaben (Quader, Schachtel, Würfel), Term rückwärts aus Nullstellen.')
    S.g('verstehen', erkennen=[112, 114, 115, 113, 116, 117], fehler=[118, 119, 123, 122, 129], darstellung=[120, 128], mehrschritt=[121, 165], begruenden=[125, 124, 169],
        umkehr=[164], transfer=[126, 127], rueckwaerts=[166, 167], verknuepfen=[168])
    S.ueberzaehlig(114, 116, 129)
    S.neu('verstehen', 'direkt', Z('Löse x³ = 8.', 2, '2', '2³ = 8, also x = 2 (eine Lösung, denn (−2)³ = −8).', 'Welche Zahl hoch drei ergibt 8?'))
    S.neu('verstehen', 'direkt', L('Löse x² = 49 (kleinere Lösung zuerst).', 'x₁ = □; x₂ = □', [-7, 7], ['-7', '7'], '7² = 49 und (−7)² = 49.', 'Denke auch an die negative Zahl.', hinweis='kleinste zuerst'))
    S.neu('verstehen', 'einkleidung', Z('Ein Würfel hat das Volumen 125 cm³. Wie lang ist eine Kante?', 5, '5', 'x³ = 125 ⇒ x = 5 cm, denn 5 · 5 · 5 = 125.', 'Volumen = Kante hoch drei.', einheit='cm'))
    S.bonus('verstehen', Z('Wie viele reelle Lösungen hat x³ + x² + x + 1 = 0?', 1, '1',
                           'Gruppieren: x²(x + 1) + (x + 1) = (x + 1)(x² + 1) = 0. Nur x = −1; x² + 1 ist nie 0. Also eine Lösung.', 'Fasse die Glieder paarweise zusammen.'))
    S.bonus('verstehen', Z('Für welche ganze Zahl x gilt x³ − x = 120?', 5, '5',
                           'x³ − x = (x − 1) · x · (x + 1): das Produkt dreier aufeinanderfolgender Zahlen. 120 = 4 · 5 · 6, also x = 5.', 'Klammere x aus und zerlege weiter.'))
    S.anwenden()


if __name__ == '__main__':
    stufen()  # Zwanzigste Runde (stufen-kl10) – ganz am Ende


# ---- BEREINIGEN (Einundzwanzigste Runde) ----
if __name__ == '__main__':
    from _bereinigen import bereinigen_datei
    bereinigen_datei('gleichungen.polynom')
# ---- BEREINIGEN ENDE ----
