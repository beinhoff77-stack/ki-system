#!/usr/bin/env python3
"""Thema abbildungen.determinanten2 – Zweireihige Determinanten (Realschule Bayern, Klasse 7, WPF I)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _rs import *  # noqa: E402,F403

start(7401)
NAMEN = 'ABCDEF'


def d2(a, b):
    return det(a, b)


def zufallsvek(g, pos=False):
    lo = 0 if pos else -g
    while True:
        v = (R.randint(lo, g), R.randint(lo, g))
        if v != (0, 0): return v


def sub(p, q):
    return (q[0] - p[0], q[1] - p[1])


def vieleck_rechnung(ps):
    """Fläche über Vektoren von A aus: ½ · (D₁ + D₂ + …). Liefert (Fläche, Lösungsweg, c)."""
    A = ps[0]
    v = [sub(A, p) for p in ps[1:]]
    teile, cs, ds = [], [], []
    for i in range(len(v) - 1):
        d = d2(v[i], v[i + 1])
        ds.append(d)
        teile.append(f'D{"₁₂₃₄₅"[i]} = {det_text(v[i], v[i + 1])} = {dz(d)}')
        cs.append(f'({det_c(v[i], v[i + 1])})')
    F = Fr(sum(ds), 2)
    vtext = ', '.join(f'Vektor A{NAMEN[i + 1]} = {vek(*v[i])}' for i in range(len(v)))
    w = f'{vtext}. ' + '; '.join(teile) + f'. A = ½ · ({" + ".join(kl(d) for d in ds)}) = {dz(F)} FE.'
    return F, w, '(' + ' + '.join(cs) + ') / 2', v


ETAPPEN = [
    {'lernziel': 'det_berechnen', 'titel': 'Eine Determinante berechnen',
     'regel': 'Schreibe zwei Vektoren a = (a₁ | a₂) und b = (b₁ | b₂) als Spalten nebeneinander. Die ⟦Determinante⟧ ist die Zahl ⟦a₁ · b₂ − a₂ · b₁⟧: „links oben mal rechts unten minus links unten mal rechts oben“ – über Kreuz.',
     'bild': {'typ': 'tabelle', 'kopf': ['', 'a', 'b'], 'zeilen': [['x', '4', '1'], ['y', '2', '3']]},
     'schritte': ['Vektoren a = (4 | 2) und b = (1 | 3): oben steht 4 und 1, unten 2 und 3 (siehe Tabelle).',
                  'Über Kreuz: 4 · 3 − 2 · 1 = 12 − 2 = ⟦10⟧.'],
     'probe': 'Vertauschst du a und b, kommt −10 heraus: 1 · 2 − 3 · 4 = −10. Die Reihenfolge zählt.',
     'fehler': '4 · 3 ⟦+⟧ 2 · 1 = 14 ist falsch: Zwischen den beiden Produkten steht ein ⟦Minus⟧. Ebenso falsch: 4 · 2 − 1 · 3 (das rechnet waagrecht statt über Kreuz).'},
    {'lernziel': 'parallelogramm', 'titel': 'Fläche eines Parallelogramms',
     'regel': 'Spannen die Vektoren AB und AD das Parallelogramm ABCD auf (Ecken ⟦gegen den Uhrzeigersinn⟧), dann gilt: ⟦A = Determinante aus AB und AD⟧ in Flächeneinheiten (FE). Stell dir die Determinante als Maschine vor, die aus zwei Pfeilen die Fläche zwischen ihnen macht.',
     'bild': {'typ': 'koordinaten', 'x': [0, 7], 'y': [0, 5], 'schritt_x': 1, 'schritt_y': 1,
              'punkte': [{'x': 1, 'y': 1, 'name': 'A'}, {'x': 5, 'y': 1, 'name': 'B'}, {'x': 6, 'y': 4, 'name': 'C'}, {'x': 2, 'y': 4, 'name': 'D'}],
              'strecken': [[1, 1, 5, 1], [5, 1, 6, 4], [6, 4, 2, 4], [2, 4, 1, 1]]},
     'schritte': ['A(1 | 1), B(5 | 1), D(2 | 4): Vektor AB = (5 − 1 | 1 − 1) = (4 | 0), Vektor AD = (2 − 1 | 4 − 1) = (1 | 3).',
                  'Determinante: 4 · 3 − 0 · 1 = 12. Das Parallelogramm hat ⟦12 FE⟧.'],
     'probe': 'Grundseite 4, Höhe 3: 4 · 3 = 12 ✓',
     'fehler': 'Mit den Punkten selbst rechnen, also 5 · 4 − 1 · 2 = 18, ist falsch: Zuerst die ⟦Vektoren⟧ AB und AD bilden (Spitze minus Fuß), erst dann die Determinante.'},
    {'lernziel': 'dreieck', 'titel': 'Fläche eines Dreiecks',
     'regel': 'Ein Dreieck ABC ist ein ⟦halbes Parallelogramm⟧. Deshalb gilt bei ABC gegen den Uhrzeigersinn: ⟦A = ½ · Determinante aus AB und AC⟧.',
     'schritte': ['A(−1 | 0), B(4 | 1), C(1 | 5): Vektor AB = (5 | 1), Vektor AC = (2 | 5).',
                  'Determinante: 5 · 5 − 1 · 2 = 23. Fläche: ½ · 23 = ⟦11,5 FE⟧.'],
     'bild': {'typ': 'koordinaten', 'x': [-2, 5], 'y': [-1, 6], 'schritt_x': 1, 'schritt_y': 1,
              'punkte': [{'x': -1, 'y': 0, 'name': 'A'}, {'x': 4, 'y': 1, 'name': 'B'}, {'x': 1, 'y': 5, 'name': 'C'}],
              'strecken': [[-1, 0, 4, 1], [4, 1, 1, 5], [1, 5, -1, 0]]},
     'fehler': 'Das ⟦½⟧ vergessen: 23 FE wäre die Fläche des ganzen Parallelogramms, das Dreieck ist nur die Hälfte, also 11,5 FE.'},
    {'lernziel': 'umlaufsinn', 'titel': 'Was sagt das Vorzeichen?',
     'regel': 'Die Formel braucht die Ecken ⟦gegen den Uhrzeigersinn⟧ (mathematisch positiver Umlaufsinn). Ist die Determinante ⟦negativ⟧, laufen die Ecken im Uhrzeigersinn – die Fläche ist der ⟦Betrag⟧. Ist sie ⟦0⟧, liegen die Punkte auf einer Geraden: kein Dreieck.',
     'schritte': ['A(0 | 0), B(1 | 4), C(5 | 1): Vektor AB = (1 | 4), Vektor AC = (5 | 1). Determinante: 1 · 1 − 4 · 5 = −19.',
                  'Negativ: A → B → C läuft ⟦im Uhrzeigersinn⟧. Richtig benannt (A, C, B) ergibt sich +19, Fläche ⟦9,5 FE⟧.'],
     'fehler': '„Die Fläche ist −9,5 FE“ ist falsch: Flächen sind nie negativ. Das Minus zeigt nur die ⟦falsche Reihenfolge⟧ der Ecken an.'},
    {'lernziel': 'viereck', 'titel': 'Fläche eines Vierecks',
     'regel': 'Die ⟦Diagonale AC⟧ zerlegt das Viereck ABCD in die Dreiecke ABC und ACD. Darum gilt: ⟦A = ½ · (Determinante aus AB und AC + Determinante aus AC und AD)⟧. Das klappt auch bei Drachen, Trapezen und schiefen Vierecken.',
     'bild': {'typ': 'koordinaten', 'x': [-1, 6], 'y': [-1, 5], 'schritt_x': 1, 'schritt_y': 1,
              'punkte': [{'x': 0, 'y': 0, 'name': 'A'}, {'x': 5, 'y': 1, 'name': 'B'}, {'x': 4, 'y': 4, 'name': 'C'}, {'x': 1, 'y': 3, 'name': 'D'}],
              'strecken': [[0, 0, 5, 1], [5, 1, 4, 4], [4, 4, 1, 3], [1, 3, 0, 0], [0, 0, 4, 4, 'gestrichelt']]},
     'schritte': ['A(0 | 0), B(5 | 1), C(4 | 4), D(1 | 3): Vektoren AB = (5 | 1), AC = (4 | 4), AD = (1 | 3).',
                  'D₁ = 5 · 4 − 1 · 4 = 16; D₂ = 4 · 3 − 4 · 1 = 8.',
                  'A = ½ · (16 + 8) = ⟦12 FE⟧.'],
     'fehler': 'Nur ½ · Determinante aus AB und AD zu rechnen (½ · 14 = 7) ist falsch: Das ist das Dreieck ABD – das Stück ⟦BCD fehlt⟧. Immer über die Diagonale AC in zwei Dreiecke zerlegen.'},
    {'lernziel': 'vieleck', 'titel': 'Fläche eines Vielecks',
     'regel': 'Ein n-Eck zerlegst du von A aus wie einen ⟦Fächer⟧ in Dreiecke. Mit den Vektoren AB, AC, AD, AE … rechnest du die Determinanten ⟦benachbarter Vektoren⟧, addierst sie und nimmst die ⟦Hälfte⟧.',
     'bild': {'typ': 'koordinaten', 'x': [-1, 6], 'y': [-1, 6], 'schritt_x': 1, 'schritt_y': 1,
              'punkte': [{'x': 0, 'y': 0, 'name': 'A'}, {'x': 4, 'y': 0, 'name': 'B'}, {'x': 5, 'y': 3, 'name': 'C'}, {'x': 2, 'y': 5, 'name': 'D'}, {'x': -1, 'y': 3, 'name': 'E'}],
              'strecken': [[0, 0, 4, 0], [4, 0, 5, 3], [5, 3, 2, 5], [2, 5, -1, 3], [-1, 3, 0, 0], [0, 0, 5, 3, 'gestrichelt'], [0, 0, 2, 5, 'gestrichelt']]},
     'schritte': ['Fünfeck A(0 | 0), B(4 | 0), C(5 | 3), D(2 | 5), E(−1 | 3): AB = (4 | 0), AC = (5 | 3), AD = (2 | 5), AE = (−1 | 3).',
                  'D₁ = 4 · 3 − 0 · 5 = 12; D₂ = 5 · 5 − 3 · 2 = 19; D₃ = 2 · 3 − 5 · (−1) = 11.',
                  'A = ½ · (12 + 19 + 11) = ⟦21 FE⟧.'],
     'fehler': 'Determinanten von Vektoren bilden, die ⟦nicht nebeneinander⟧ liegen (z. B. AB und AD), zählt Dreiecke doppelt oder lässt Stücke aus. Immer der Reihe nach: AB mit AC, AC mit AD, AD mit AE.'},
]


# ---------- Generatoren ----------
def g_det_berechnen(s):
    if s == 1:
        a, b = zufallsvek(6, True), zufallsvek(6, True)
        return zahl(f'Berechne die Determinante der Vektoren a = {vek(*a)} und b = {vek(*b)}.',
                    f'Über Kreuz: {det_text(a, b)} = {dz(d2(a, b))}.', 'Links oben mal rechts unten, minus links unten mal rechts oben.',
                    d2(a, b), det_c(a, b))
    if s == 2:
        a, b = zufallsvek(9), zufallsvek(9)
        if 0 in a + b and R.random() < 0.6: return None
        return zahl(f'Berechne die Determinante der Vektoren a = {vek(*a)} und b = {vek(*b)}.',
                    f'Über Kreuz: {det_text(a, b)} = {dz(a[0] * b[1])} − {kl(a[1] * b[0])} = {dz(d2(a, b))}.',
                    'Negative Zahlen in Klammern setzen. Minus mal Minus ergibt Plus.', d2(a, b), det_c(a, b))
    art = R.random()
    a, b = zufallsvek(8), zufallsvek(8)
    D = d2(a, b)
    if art < 0.4:
        plus_f = a[0] * b[1] + a[1] * b[0]
        waag = a[0] * a[1] - b[0] * b[1]
        if len({D, plus_f, waag, -D}) < 4: return None
        return auswahl(f'Welchen Wert hat die Determinante der Vektoren a = {vek(*a)} und b = {vek(*b)}?', dz(D),
                       [dz(plus_f), dz(waag), dz(-D)], f'Über Kreuz: {det_text(a, b)} = {dz(D)}.',
                       'Achte auf das Minus zwischen den Produkten und auf die Reihenfolge a, dann b.')
    # Umkehraufgabe: fehlende Koordinate
    x = R.randint(-6, 6)
    a = (x, R.randint(-5, 5))
    b = (R.randint(-5, 5), R.choice([i for i in range(-6, 7) if i not in (0,)]))
    D = d2(a, b)
    return zahl(f'Die Determinante der Vektoren a = (x | {dz(a[1])}) und b = {vek(*b)} hat den Wert {dz(D)}. Berechne x.',
                f'x · {kl(b[1])} − {kl(a[1])} · {kl(b[0])} = {dz(D)} ⇔ {dz(b[1])}x {plus(-a[1] * b[0])} = {dz(D)} ⇔ x = {dz(x)}.',
                'Stelle die Determinante mit x auf und löse die Gleichung.', x, f'({D} + ({a[1]}) * ({b[0]})) / ({b[1]})')


def parallelogramm(g=4):
    while True:
        A = (R.randint(-4, 3), R.randint(-4, 3))
        u, v = zufallsvek(g), zufallsvek(g)
        if d2(u, v) > 0: return A, u, v


def g_parallelogramm(s):
    if s == 1:
        u, v = zufallsvek(6, True), zufallsvek(6, True)
        if d2(u, v) <= 0: return None
        return zahl(f'Die Vektoren AB = {vek(*u)} und AD = {vek(*v)} spannen ein Parallelogramm ABCD auf. Berechne seinen Flächeninhalt in FE.',
                    f'A = {det_text(u, v)} = {dz(d2(u, v))} FE.', 'Determinante aus AB und AD.', d2(u, v), det_c(u, v), einheit='FE')
    A, u, v = parallelogramm(5)
    B, D = (A[0] + u[0], A[1] + u[1]), (A[0] + v[0], A[1] + v[1])
    C = (B[0] + v[0], B[1] + v[1])
    F = d2(u, v)
    w0 = f'Vektor AB = {vek(*u)}, Vektor AD = {vek(*v)}. A = {det_text(u, v)} = {dz(F)} FE.'
    if s == 2:
        a = zahl(f'Berechne den Flächeninhalt des Parallelogramms ABCD mit {pkt("A", *A)}, {pkt("B", *B)} und {pkt("D", *D)}.',
                 w0, 'Bilde zuerst die Vektoren AB und AD: Spitze minus Fuß.', F, det_c(u, v), einheit='FE')
        return bild(a, koord_bild([A, B, C, D], ['A', 'B', 'C', 'D'])) if R.random() < 0.4 else a
    art = R.random()
    if art < 0.35:
        return zahl(f'Gegeben sind {pkt("A", *A)}, {pkt("B", *B)} und {pkt("C", *C)} des Parallelogramms ABCD. Berechne den Flächeninhalt.',
                    f'Im Parallelogramm ist Vektor AD = Vektor BC = {vek(*v)}. Vektor AB = {vek(*u)}. A = {det_text(u, v)} = {dz(F)} FE.',
                    'D ist nicht gegeben. Welcher Vektor ist genauso lang und gleich gerichtet wie AD?', F, det_c(u, v), einheit='FE')
    if art < 0.7:
        m = R.choice([2, 5, 10])
        return zahl(f'Ein Beet hat die Form eines Parallelogramms ABCD mit {pkt("A", *A)}, {pkt("B", *B)} und {pkt("D", *D)} '
                    f'(1 Längeneinheit = {m} m). Wie viele m² ist es groß?',
                    w0 + f' 1 FE = {m} m · {m} m = {m * m} m², also {dz(F)} · {m * m} = {dz(F * m * m)} m².',
                    f'Erst in FE rechnen. Ein Kästchen ist {m} m mal {m} m groß.', F * m * m, f'({det_c(u, v)}) * {m * m}', einheit='m²')
    falsch = A[0] * D[1] - A[1] * D[0]
    falsch2 = B[0] * D[1] - B[1] * D[0]
    return auswahl(f'Welchen Flächeninhalt hat das Parallelogramm ABCD mit {pkt("A", *A)}, {pkt("B", *B)} und {pkt("D", *D)}?',
                   f'{dz(F)} FE', [f'{dz(abs(falsch2))} FE', f'{dz(Fr(F, 2))} FE', f'{dz(F + 2 * abs(u[0]))} FE', f'{dz(abs(falsch))} FE'],
                   w0 + ' Mit den Punktkoordinaten selbst zu rechnen oder zu halbieren ist falsch.',
                   'Vektoren bilden, dann die Determinante – beim Parallelogramm ohne ½.')


def dreieck(g=5):
    while True:
        A = (R.randint(-4, 3), R.randint(-4, 3))
        u, v = zufallsvek(g), zufallsvek(g)
        if d2(u, v) > 0: return A, u, v


def g_dreieck(s):
    if s == 1:
        u, v = zufallsvek(7, True), zufallsvek(7, True)
        if d2(u, v) <= 0: return None
        F = Fr(d2(u, v), 2)
        return zahl(f'Die Vektoren AB = {vek(*u)} und AC = {vek(*v)} spannen das Dreieck ABC auf. Berechne seinen Flächeninhalt in FE.',
                    f'A = ½ · ({det_text(u, v)}) = ½ · {dz(d2(u, v))} = {dz(F)} FE.', 'Determinante aus AB und AC, dann halbieren.',
                    F, f'({det_c(u, v)}) / 2', einheit='FE')
    A, u, v = dreieck(6)
    B, C = (A[0] + u[0], A[1] + u[1]), (A[0] + v[0], A[1] + v[1])
    D = d2(u, v)
    F = Fr(D, 2)
    w0 = f'Vektor AB = {vek(*u)}, Vektor AC = {vek(*v)}. A = ½ · ({det_text(u, v)}) = ½ · {dz(D)} = {dz(F)} FE.'
    if s == 2:
        a = zahl(f'Berechne den Flächeninhalt des Dreiecks ABC mit {pkt("A", *A)}, {pkt("B", *B)} und {pkt("C", *C)}.',
                 w0, 'Vektoren von A aus bilden, Determinante, dann ½.', F, f'({det_c(u, v)}) / 2', einheit='FE')
        return bild(a, koord_bild([A, B, C], ['A', 'B', 'C'])) if R.random() < 0.4 else a
    art = R.random()
    if art < 0.4:
        # C liegt auf der Geraden y = k; gesucht: x-Koordinate von C, sodass die Fläche stimmt
        cx = R.randint(-5, 6)
        C = (cx, R.randint(2, 7))
        A, B = (R.randint(-4, 0), R.randint(-3, 0)), None
        u = (R.randint(3, 7), R.randint(-1, 1))
        B = (A[0] + u[0], A[1] + u[1])
        v = (C[0] - A[0], C[1] - A[1])
        if u[1] == 0 or d2(u, v) <= 0: return None
        F = Fr(d2(u, v), 2)
        # ½(u0*(cy-ay) - u1*(cx-ax)) = F  ->  cx = ax + (u0*(cy-ay) - 2F)/u1
        return zahl(f'Gegeben: {pkt("A", *A)}, {pkt("B", *B)} und C(x | {dz(C[1])}). Das Dreieck ABC (gegen den Uhrzeigersinn) hat {dz(F)} FE. Berechne x.',
                    f'Vektor AB = {vek(*u)}, Vektor AC = (x {plus(-A[0])} | {dz(C[1] - A[1])}). '
                    f'½ · ({dz(u[0])} · {kl(C[1] - A[1])} − {kl(u[1])} · (x {plus(-A[0])})) = {dz(F)} ⇔ x = {dz(cx)}.',
                    'Stelle die Flächenformel mit x auf. Erst mit 2 multiplizieren, dann nach x auflösen.',
                    cx, f'{A[0]} + ({u[0]} * ({C[1] - A[1]}) - 2 * ({cz(F)})) / ({u[1]})')
    if art < 0.7:
        return auswahl(f'Welchen Flächeninhalt hat das Dreieck ABC mit {pkt("A", *A)}, {pkt("B", *B)} und {pkt("C", *C)}?',
                       f'{dz(F)} FE', [f'{dz(D)} FE', f'{dz(Fr(abs(u[0] * v[1] + u[1] * v[0]), 2))} FE', f'{dz(Fr(abs(B[0] * C[1] - B[1] * C[0]), 2))} FE'],
                       w0, 'Vektoren, Determinante über Kreuz – und das ½ nicht vergessen.')
    m = R.choice([10, 20, 50])
    return zahl(f'Auf einem Plan (1 Längeneinheit = {m} m) liegt ein dreieckiges Feld mit den Ecken {pkt("A", *A)}, {pkt("B", *B)} und {pkt("C", *C)}. Wie groß ist es in m²?',
                w0 + f' 1 FE = {m * m} m², also {dz(F)} · {m * m} = {dz(F * m * m)} m².',
                f'Erst die Fläche in FE, dann mal {m} · {m}.', F * m * m, f'({det_c(u, v)}) / 2 * {m * m}', einheit='m²')


def g_umlaufsinn(s):
    while True:
        A = (R.randint(-4, 3), R.randint(-4, 3))
        u, v = zufallsvek(5), zufallsvek(5)
        if d2(u, v) != 0: break
    B, C = (A[0] + u[0], A[1] + u[1]), (A[0] + v[0], A[1] + v[1])
    D = d2(u, v)
    sinn = 'gegen den Uhrzeigersinn' if D > 0 else 'im Uhrzeigersinn'
    w0 = f'Vektor AB = {vek(*u)}, Vektor AC = {vek(*v)}. Determinante: {det_text(u, v)} = {dz(D)}.'
    if s == 1:
        a = auswahl(f'Für A, B, C ist die Determinante aus AB und AC gleich {dz(D)}. Wie laufen die Ecken A → B → C?',
                    sinn, ['im Uhrzeigersinn' if D > 0 else 'gegen den Uhrzeigersinn', 'Die Punkte liegen auf einer Geraden.'],
                    f'{dz(D)} ist {"positiv" if D > 0 else "negativ"}, also läuft A → B → C {sinn}.', 'Achte nur auf das Vorzeichen.')
        return a
    if s == 2:
        if R.random() < 0.5:
            return auswahl(f'Wie laufen die Ecken A → B → C für {pkt("A", *A)}, {pkt("B", *B)} und {pkt("C", *C)}?',
                           sinn, ['im Uhrzeigersinn' if D > 0 else 'gegen den Uhrzeigersinn', 'Die Punkte liegen auf einer Geraden.'],
                           w0 + f' {"Positiv" if D > 0 else "Negativ"}: {sinn}.', 'Berechne die Determinante aus AB und AC und schau auf das Vorzeichen.')
        return zahl(f'Berechne den Flächeninhalt des Dreiecks mit den Ecken {pkt("A", *A)}, {pkt("B", *B)} und {pkt("C", *C)}.',
                    w0 + f' Fläche = ½ · |{dz(D)}| = {dz(Fr(abs(D), 2))} FE.', 'Ist die Determinante negativ, nimm den Betrag.',
                    Fr(abs(D), 2), f'abs({det_c(u, v)}) / 2', einheit='FE')
    art = R.random()
    if art < 0.35:
        # Kollinear?
        k = R.choice([-2, -1, 2, 3])
        u = (R.randint(-3, 3), R.randint(-3, 3))
        if u == (0, 0): return None
        v = (k * u[0], k * u[1]) if R.random() < 0.5 else (k * u[0] + R.choice([-1, 1]), k * u[1])
        B, C = (A[0] + u[0], A[1] + u[1]), (A[0] + v[0], A[1] + v[1])
        D = d2(u, v)
        if D == 0:
            richtig = 'Die Punkte liegen auf einer Geraden – es gibt kein Dreieck.'
        else:
            richtig = f'Sie bilden ein Dreieck mit {dz(Fr(abs(D), 2))} FE.'
        f = ['Die Punkte liegen auf einer Geraden – es gibt kein Dreieck.', f'Sie bilden ein Dreieck mit {dz(Fr(abs(D) + 2, 2))} FE.',
             'Man kann es nicht entscheiden, ohne zu zeichnen.', f'Sie bilden ein Dreieck mit {dz(abs(D) + 1)} FE.']
        return auswahl(f'Bilden {pkt("A", *A)}, {pkt("B", *B)} und {pkt("C", *C)} ein Dreieck?', richtig, f,
                       f'Vektor AB = {vek(*u)}, Vektor AC = {vek(*v)}. Determinante: {det_text(u, v)} = {dz(D)}. '
                       + ('Null heißt: AB und AC liegen auf einer Geraden.' if D == 0 else f'Fläche ½ · {dz(abs(D))} = {dz(Fr(abs(D), 2))} FE.'),
                       'Was bedeutet es, wenn die Determinante 0 ist?')
    if art < 0.7:
        if D > 0: u, v, B, C, D = v, u, C, B, -D
        F = Fr(-D, 2)
        return auswahl(f'Jemand rechnet für {pkt("A", *A)}, {pkt("B", *B)}, {pkt("C", *C)} die Fläche „½ · ({det_text(u, v)}) = {dz(Fr(D, 2))} FE“. Was stimmt?',
                       f'Die Ecken laufen im Uhrzeigersinn; die Fläche ist {dz(F)} FE.',
                       [f'Richtig, das Dreieck hat {dz(Fr(D, 2))} FE.', 'Falsch gerechnet: Es gibt kein Dreieck, weil das Ergebnis negativ ist.',
                        f'Die Fläche ist {dz(-D)} FE.'],
                       f'{det_text(u, v)} = {dz(D)} ist negativ, also läuft A → B → C im Uhrzeigersinn. Fläche: ½ · {dz(-D)} = {dz(F)} FE.',
                       'Kann eine Fläche negativ sein? Was zeigt das Minus an?')
    if D < 0: u, v, B, C, D = v, u, C, B, -D
    # Reihenfolge der Ecken angeben: Welche Benennung ist gegen den Uhrzeigersinn?
    return auswahl(f'Die Ecken {pkt("P", *A)}, {pkt("Q", *B)} und {pkt("R", *C)} sollen gegen den Uhrzeigersinn benannt werden. Welche Reihenfolge passt?',
                   'P → Q → R', ['P → R → Q', 'Q → P → R', 'R → Q → P'],
                   f'Vektor PQ = {vek(*u)}, Vektor PR = {vek(*v)}. Determinante: {det_text(u, v)} = {dz(D)} > 0, also P → Q → R gegen den Uhrzeigersinn.',
                   'Rechne die Determinante für P → Q → R. Ist sie positiv?')


def g_viereck(s):
    if s == 1:
        ps = zufalls_vieleck(4, -1, 6, start_null=True)
        F, w, c, v = vieleck_rechnung(ps)
        return zahl(f'Für das Viereck ABCD gilt: Vektor AB = {vek(*v[0])}, Vektor AC = {vek(*v[1])}, Vektor AD = {vek(*v[2])}. Berechne den Flächeninhalt.',
                    w, 'Zwei Determinanten: AB mit AC und AC mit AD. Addieren, halbieren.', F, c, einheit='FE')
    ps = zufalls_vieleck(4, -4, 5)
    F, w, c, v = vieleck_rechnung(ps)
    txt = ', '.join(pkt(NAMEN[i], *p) for i, p in enumerate(ps))
    if s == 2:
        a = zahl(f'Berechne den Flächeninhalt des Vierecks ABCD mit {txt}.', w,
                 'Zerlege mit der Diagonale AC in zwei Dreiecke. Vektoren AB, AC, AD von A aus.', F, c, einheit='FE')
        return bild(a, koord_bild(ps, list('ABCD'))) if R.random() < 0.4 else a
    art = R.random()
    if art < 0.4:
        nur = Fr(det(v[0], v[2]), 2)
        ohne = sum(det(v[i], v[i + 1]) for i in range(2))
        return auswahl(f'Welchen Flächeninhalt hat das Viereck ABCD mit {txt}?', f'{dz(F)} FE',
                       [f'{dz(nur)} FE', f'{dz(ohne)} FE', f'{dz(Fr(det(v[0], v[1]), 2))} FE'], w,
                       'Beide Dreiecke ABC und ACD zählen – und am Ende halbieren.')
    if art < 0.7:
        m = R.choice([10, 20])
        return zahl(f'Ein Grundstück hat auf dem Plan (1 Längeneinheit = {m} m) die Ecken {txt}. Wie groß ist es in m²?',
                    w + f' 1 FE = {m * m} m², also {dz(F)} · {m * m} = {dz(F * m * m)} m².', f'Erst in FE rechnen, dann mal {m * m}.',
                    F * m * m, f'{c} * {m * m}', einheit='m²')
    # Trapez/Drachen: Ecke D fehlt und wird aus Parallelität bestimmt? -> einfacher: Fehler finden
    falsch = Fr(sum(abs(det(v[i], v[i + 1])) for i in range(2)), 1)
    return auswahl(f'Jemand rechnet für ABCD mit {txt}: „A = Determinante aus AB und AC + Determinante aus AC und AD = {dz(falsch)} FE“. Was stimmt?',
                   f'Das ½ fehlt: A = {dz(F)} FE.', ['Richtig gerechnet.', f'Es fehlt AB mit AD: A = {dz(falsch + det(v[0], v[2]))} FE.',
                                                       f'Man muss durch 4 teilen: A = {dz(Fr(falsch, 4))} FE.'],
                   w, 'Jede Determinante ist ein Parallelogramm – das Dreieck ist die Hälfte davon.')


def g_vieleck(s):
    if s == 1:
        ps = zufalls_vieleck(5, -2, 6, start_null=True)
        F, w, c, v = vieleck_rechnung(ps)
        return zahl('Für das Fünfeck ABCDE gilt: ' + ', '.join(f'Vektor A{NAMEN[i + 1]} = {vek(*v[i])}' for i in range(4)) + '. Berechne den Flächeninhalt.',
                    w, 'Drei Determinanten benachbarter Vektoren addieren und halbieren.', F, c, einheit='FE')
    n = 5 if s == 2 else R.choice([5, 6])
    ps = zufalls_vieleck(n, -4, 5)
    F, w, c, v = vieleck_rechnung(ps)
    txt = ', '.join(pkt(NAMEN[i], *p) for i, p in enumerate(ps))
    name = {5: 'Fünfeck ABCDE', 6: 'Sechseck ABCDEF'}[n]
    des = {5: 'des Fünfecks ABCDE', 6: 'des Sechsecks ABCDEF'}[n]
    eines = {5: 'eines Fünfecks', 6: 'eines Sechsecks'}[n]
    if s == 2:
        a = zahl(f'Berechne den Flächeninhalt {des} mit {txt}.', w,
                 'Vektoren von A zu allen anderen Ecken, dann Determinanten der Nachbarn.', F, c, einheit='FE')
        return bild(a, koord_bild(ps, list(NAMEN[:n]))) if R.random() < 0.5 else a
    art = R.random()
    if art < 0.35:
        m = R.choice([5, 10, 20])
        return zahl(f'Ein Spielplatz hat auf dem Plan (1 Längeneinheit = {m} m) die Form {eines} {name[-6:] if n == 6 else name[-5:]} mit {txt}. Wie viele m² Rasen braucht man?',
                    w + f' 1 FE = {m * m} m², also {dz(F)} · {m * m} = {dz(F * m * m)} m².', 'Fläche in FE, dann umrechnen.',
                    F * m * m, f'{c} * {m * m}', einheit='m²')
    if art < 0.7:
        anz = n - 2
        return auswahl(f'Wie viele Determinanten brauchst du für die Fläche {eines}, wenn du von A aus zerlegst?',
                       f'{anz}', [f'{n}', f'{n - 1}', f'{anz - 1}'],
                       f'Von A aus entstehen {anz} Dreiecke (eines weniger als die {n - 1} Vektoren). Für jedes Dreieck eine Determinante.',
                       'Zähle die Dreiecke im Fächer von A aus.')
    a = zahl(f'Berechne den Flächeninhalt {des} mit {txt}.', w,
             'Ordne die Vektoren der Reihe nach und rechne nur Nachbarn.', F, c, einheit='FE')
    return bild(a, koord_bild(ps, list(NAMEN[:n])))


# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402


def _ko(x, y, punkte, strecken=(), **extra):
    return {'typ': 'koordinaten', 'x': x, 'y': y, 'schritt_x': 1, 'schritt_y': 1,
            'punkte': [{'x': a, 'y': b, 'name': n} for n, (a, b) in punkte.items()],
            'strecken': [list(s) for s in strecken], **extra}


def _rand(*ps):
    return [[*ps[i], *ps[(i + 1) % len(ps)]] for i in range(len(ps))]


_PA = {'A': (1, 1), 'B': (5, 1), 'C': (6, 4), 'D': (2, 4)}
_DR = {'A': (-1, 0), 'B': (4, 1), 'C': (1, 5)}
_UM = {'A': (0, 0), 'B': (1, 4), 'C': (5, 1)}
_VI = {'A': (0, 0), 'B': (5, 1), 'C': (4, 4), 'D': (1, 3)}
_FU = {'A': (0, 0), 'B': (4, 0), 'C': (5, 3), 'D': (2, 5), 'E': (-1, 3)}

UMBAU = {
    'det_berechnen': {
        'einstieg': 'Ein Gärtner zeichnet seine Beete auf Karopapier. Zwei Pfeile vom selben Eckpunkt spannen ein Beet auf. '
                    'Aus den Pfeilen bekommt man mit einer kurzen Rechnung eine Zahl. Sie heißt ⟦Determinante⟧.',
        'woerter': [['Vektor', 'ein Pfeil, beschrieben durch „so weit nach rechts | so weit nach oben“, z. B. (4 | 2)'],
                    ['Determinante', 'eine Zahl aus zwei Vektoren: über Kreuz malnehmen, dann abziehen']],
        'bild': _ko([0, 6], [0, 6], {}, pfeile=[[0, 0, 4, 2, 'a'], [0, 0, 1, 3, 'b']]),
        'schritte': [
            {'text': 'Die Vektoren sind a = (4 | 2) und b = (1 | 3).'},
            {'text': 'Schreibe sie als Spalten: oben 4 und 1, unten 2 und 3.',
             'bild': {'typ': 'tabelle', 'kopf': ['', 'a', 'b'], 'zeilen': [['nach rechts', '4', '1'], ['nach oben', '2', '3']]}},
            {'text': 'Über Kreuz malnehmen: 4 · 3 = 12 und 2 · 1 = 2.'},
            {'text': 'Abziehen: 12 − 2 = ⟦10⟧. So groß ist die Fläche zwischen den Pfeilen.',
             'bild': _ko([0, 6], [0, 6], {}, pfeile=[[0, 0, 4, 2, 'a'], [0, 0, 1, 3, 'b']],
                         flaechen=[{'punkte': [[0, 0], [4, 2], [5, 5], [1, 3]]}])},
        ],
        'fehler': 'Plus statt Minus: 4 · 3 + 2 · 1 = 14 ist falsch. Zwischen den beiden Produkten steht immer ein ⟦Minus⟧.',
        'regel': 'Determinante: über Kreuz malnehmen, dann abziehen. ⟦Oben links mal unten rechts⟧ minus unten links mal oben rechts.',
    },
    'parallelogramm': {
        'einstieg': 'Ein Beet hat die Form eines Parallelogramms. Seine Ecken A, B, C, D liegen auf dem Plan gegen den Uhrzeigersinn. '
                    'Wie groß ist das Beet? Die Pfeile AB und AD verraten es.',
        'woerter': [['Parallelogramm', 'Viereck, bei dem gegenüberliegende Seiten parallel und gleich lang sind'],
                    ['gegen den Uhrzeigersinn', 'die Ecken linksherum ablaufen: A, dann B, dann C, dann D'],
                    ['FE', 'Flächeneinheit: ein Kästchen auf dem Plan']],
        'bild': _ko([0, 7], [0, 5], _PA, _rand(*_PA.values())),
        'schritte': [
            {'text': 'Einen Vektor rechnest du als Spitze minus Fuß.'},
            {'text': 'AB = (5 − 1 | 1 − 1) = (4 | 0).',
             'bild': {'pfeile': [[1, 1, 5, 1, 'AB']]}},
            {'text': 'Ebenso AD = (2 − 1 | 4 − 1) = (1 | 3).',
             'bild': {'pfeile': [[1, 1, 5, 1, 'AB'], [1, 1, 2, 4, 'AD']]}},
            {'text': 'Determinante: 4 · 3 − 0 · 1 = ⟦12⟧. Das Beet hat 12 FE.',
             'bild': {'flaechen': [{'punkte': [list(p) for p in _PA.values()]}]}},
        ],
        'fehler': 'Mit den Punkten selbst rechnen: 5 · 4 − 1 · 2 = 18 ist falsch. '
                  'Das wäre ein anderes Parallelogramm. Erst die ⟦Vektoren⟧ AB und AD bilden.',
        'fehler_bild': {'pfeile': [[0, 0, 5, 1, 'B'], [0, 0, 2, 4, 'D']], 'flaechen': [{'punkte': [[0, 0], [5, 1], [7, 5], [2, 4]]}]},
        'regel': 'Fläche des Parallelogramms = Determinante aus AB und AD. Ecken ⟦gegen den Uhrzeigersinn⟧ benennen, Ergebnis in FE.',
    },
    'dreieck': {
        'einstieg': 'Ein Beet ist dreieckig. Zwei gleiche Dreiecke ergeben zusammen ein Parallelogramm. '
                    'Also hat das Dreieck die ⟦halbe Fläche⟧ des Parallelogramms aus denselben Pfeilen.',
        'woerter': [['1/2 ·', 'die Hälfte davon nehmen, also durch 2 teilen']],
        'bild': _ko([-2, 7], [-1, 7], _DR, _rand(*_DR.values())),
        'schritte': [
            {'text': 'Die Pfeile sind AB = (5 | 1) und AC = (2 | 5).',
             'bild': {'pfeile': [[-1, 0, 4, 1, 'AB'], [-1, 0, 1, 5, 'AC']]}},
            {'text': 'Determinante: 5 · 5 − 1 · 2 = 23. Das ist das ganze Parallelogramm.',
             'bild': {'strecken': _rand(*_DR.values()) + [[4, 1, 6, 6, 'gestrichelt'], [6, 6, 1, 5, 'gestrichelt']],
                      'flaechen': [{'punkte': [[-1, 0], [4, 1], [6, 6], [1, 5]]}]}},
            {'text': 'Das Dreieck ist die Hälfte: 1/2 · 23 = ⟦11,5 FE⟧.',
             'bild': {'flaechen': [{'punkte': [list(p) for p in _DR.values()]}]}},
        ],
        'fehler': 'Die 1/2 vergessen: 23 FE ist das ganze Parallelogramm. Das Dreieck ist nur die Hälfte, also ⟦11,5 FE⟧.',
        'fehler_bild': {'flaechen': [{'punkte': [[-1, 0], [4, 1], [6, 6], [1, 5]]}]},
        'regel': 'Dreieck = halbes Parallelogramm. Fläche = ⟦1/2 · Determinante aus AB und AC⟧, Ecken gegen den Uhrzeigersinn.',
    },
    'umlaufsinn': {
        'einstieg': 'Um ein Beet kannst du linksherum oder rechtsherum gehen. Die Determinante merkt das: '
                    'Linksherum ist sie positiv, rechtsherum negativ. Die Richtung heißt ⟦Umlaufsinn⟧.',
        'woerter': [['Umlaufsinn', 'die Richtung, in der man die Ecken der Reihe nach abläuft'],
                    ['Betrag', 'die Zahl ohne Minus: Der Betrag von −19 ist 19']],
        'bild': _ko([-1, 6], [-1, 5], _UM, _rand(*_UM.values())),
        'schritte': [
            {'text': 'Die Pfeile sind AB = (1 | 4) und AC = (5 | 1).',
             'bild': {'pfeile': [[0, 0, 1, 4, 'AB'], [0, 0, 5, 1, 'AC']]}},
            {'text': 'Determinante: 1 · 1 − 4 · 5 = ⟦−19⟧.'},
            {'text': 'Das Minus heißt: A → B → C läuft im Uhrzeigersinn.',
             'bild': {'pfeile': [[0, 0, 1, 4], [1, 4, 5, 1], [5, 1, 0, 0]]}},
            {'text': 'Die Fläche ist der Betrag: 1/2 · 19 = ⟦9,5 FE⟧.',
             'bild': {'pfeile': None, 'flaechen': [{'punkte': [list(p) for p in _UM.values()]}]}},
        ],
        'fehler': '„Die Fläche ist −9,5 FE“ ist falsch. Flächen sind nie negativ. Das Minus zeigt nur die ⟦falsche Reihenfolge⟧ der Ecken.',
        'regel': 'Negative Determinante: Die Ecken laufen im Uhrzeigersinn. Die Fläche ist dann der ⟦Betrag⟧. Bei 0 liegen die Punkte auf einer Geraden.',
    },
    'viereck': {
        'einstieg': 'Ein Beet hat vier Ecken, aber keine besondere Form. Spanne eine Schnur von A nach C. '
                    'Sie teilt das Beet in zwei Dreiecke. Diese Schnur heißt ⟦Diagonale⟧.',
        'woerter': [['Diagonale', 'Strecke zwischen zwei Ecken, die nicht nebeneinanderliegen']],
        'bild': _ko([-1, 6], [-1, 5], _VI, _rand(*_VI.values())),
        'schritte': [
            {'text': 'Die Diagonale AC teilt das Viereck in die Dreiecke ABC und ACD.',
             'bild': {'strecken': _rand(*_VI.values()) + [[0, 0, 4, 4, 'gestrichelt']]}},
            {'text': 'AB = (5 | 1), AC = (4 | 4), AD = (1 | 3).',
             'bild': {'pfeile': [[0, 0, 5, 1, 'AB'], [0, 0, 4, 4, 'AC'], [0, 0, 1, 3, 'AD']]}},
            {'text': 'Dreieck ABC: 5 · 4 − 1 · 4 = 16.',
             'bild': {'flaechen': [{'punkte': [[0, 0], [5, 1], [4, 4]]}]}},
            {'text': 'Dreieck ACD: 4 · 3 − 4 · 1 = 8.',
             'bild': {'flaechen': [{'punkte': [[0, 0], [5, 1], [4, 4]]}, {'punkte': [[0, 0], [4, 4], [1, 3]]}]}},
            {'text': 'Fläche: 1/2 · (16 + 8) = ⟦12 FE⟧.'},
        ],
        'fehler': 'Nur 1/2 · Determinante aus AB und AD rechnen ist falsch. Das ist nur das Dreieck ABD, das Stück ⟦BCD fehlt⟧.',
        'fehler_bild': {'pfeile': None, 'flaechen': [{'punkte': [[0, 0], [5, 1], [1, 3]]}],
                        'strecken': _rand(*_VI.values()) + [[5, 1, 1, 3, 'gestrichelt']]},
        'regel': 'Viereck: mit der Diagonale AC in zwei Dreiecke teilen. Beide Determinanten addieren, dann ⟦halbieren⟧.',
    },
    'vieleck': {
        'einstieg': 'Ein großes Beet hat fünf Ecken. Von Ecke A aus spannst du Schnüre zu allen anderen Ecken. '
                    'Wie bei einem ⟦Fächer⟧ entstehen lauter Dreiecke.',
        'woerter': [['Fächer', 'Dreiecke, die alle die Ecke A gemeinsam haben'],
                    ['benachbart', 'direkt nebeneinander, z. B. die Pfeile AC und AD']],
        'bild': _ko([-2, 6], [-1, 6], _FU, _rand(*_FU.values())),
        'schritte': [
            {'text': 'Von A aus zerlegen: drei Dreiecke ABC, ACD und ADE.',
             'bild': {'strecken': _rand(*_FU.values()) + [[0, 0, 5, 3, 'gestrichelt'], [0, 0, 2, 5, 'gestrichelt']]}},
            {'text': 'Pfeile AB, AC, AD, AE: Rechne immer zwei benachbarte zusammen.',
             'bild': {'pfeile': [[0, 0, 4, 0, '(4|0)'], [0, 0, 5, 3, '(5|3)'], [0, 0, 2, 5, '(2|5)'], [0, 0, -1, 3, '(−1|3)']]}},
            {'text': 'AB mit AC: 4 · 3 − 0 · 5 = 12.',
             'bild': {'flaechen': [{'punkte': [[0, 0], [4, 0], [5, 3]]}]}},
            {'text': 'Ebenso AC mit AD: 19. AD mit AE: 11.',
             'bild': {'flaechen': [{'punkte': [[0, 0], [4, 0], [5, 3]]}, {'punkte': [[0, 0], [5, 3], [2, 5]]},
                                   {'punkte': [[0, 0], [2, 5], [-1, 3]]}]}},
            {'text': 'Fläche: 1/2 · (12 + 19 + 11) = ⟦21 FE⟧.'},
        ],
        'fehler': 'Pfeile überspringen, etwa AB mit AD: Dann fehlen Stücke oder zählen doppelt. '
                  'Immer der Reihe nach: AB mit AC, ⟦AC mit AD⟧, AD mit AE.',
        'fehler_bild': {'pfeile': None, 'flaechen': [{'punkte': [[0, 0], [4, 0], [2, 5]]}]},
        'regel': 'Vieleck: von A aus in Dreiecke zerlegen. Determinanten ⟦benachbarter Pfeile⟧ addieren, dann halbieren.',
    },
}
UMBAU_OFFEN = ['Umbau (Paket UR): Die Lernkarten zeigen Vektoren jetzt als Pfeile. Die Aufgaben-Grafiken zeigen sie weiter als Strecken, '
               'weil Aufgaben beim Umbau unverändert bleiben.']


GEN = {'det_berechnen': g_det_berechnen, 'parallelogramm': g_parallelogramm, 'dreieck': g_dreieck,
       'umlaufsinn': g_umlaufsinn, 'viereck': g_viereck, 'vieleck': g_vieleck}


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-1) ----------
# Prüfungsvorbilder: Realschul-Abschlussprüfung Mathematik I (Bayern), Aufgaben „Parallelogramme ABCnDn / Dreiecke ABCn …
# in Abhängigkeit von der x-Koordinate“ (z. B. ISB-Beispielaufgabe B 4, AP 2006/2008), Jahrgangsstufentest 8 I (2021: Lücken
# in einer Determinante ergänzen). Typ und Aufbau übernommen, Zahlen und Wortlaut eigen.
def durchsicht(d):
    from _rsib1 import Z, A, L, nachtrag
    S = 'Schreibe den Term mit den Zahlen.'
    nachtrag(d,
        umstufen={
            'Welchen Wert hat die Determinante der Vektoren a = (1 | 5) und b = (8 | 2)?': 2,
            'Welchen Flächeninhalt hat das Parallelogramm ABCD mit A(2 | 3), B(−3 | 6) und D(0 | −2)?': 2,
            'Welchen Flächeninhalt hat das Parallelogramm ABCD mit A(1 | −4), B(−4 | −1) und D(0 | −9)?': 2,
            'Welchen Flächeninhalt hat das Dreieck ABC mit A(−2 | 3), B(−3 | 2) und C(0 | 0)?': 2,
            'Welchen Flächeninhalt hat das Viereck ABCD mit A(−4 | −2), B(2 | 4), C(−3 | 4), D(−4 | 1)?': 2,
            'Welchen Flächeninhalt hat das Viereck ABCD mit A(−1 | −4), B(4 | 1), C(3 | 5), D(−1 | 4)?': 2,
        },
        ersetzen={
            'Für A, B, C ist die Determinante aus AB und AC gleich −15. Wie laufen die Ecken A → B → C?':
                A(1, 'Für A, B, C ist die Determinante aus AB und AC gleich 0. Was bedeutet das?',
                  'Die Punkte liegen auf einer Geraden.', ['gegen den Uhrzeigersinn', 'im Uhrzeigersinn'],
                  'Determinante 0 heißt Fläche 0: A, B und C liegen auf einer Geraden, es gibt kein Dreieck.',
                  'Was heißt eine Fläche von 0?'),
            'Für A, B, C ist die Determinante aus AB und AC gleich −6. Wie laufen die Ecken A → B → C?':
                A(1, 'Für A, B, C ist die Determinante aus AB und AC gleich 8. Wie laufen die Ecken A → B → C?',
                  'gegen den Uhrzeigersinn', ['im Uhrzeigersinn', 'Die Punkte liegen auf einer Geraden.'],
                  'Die Determinante 8 ist positiv: A → B → C läuft gegen den Uhrzeigersinn.',
                  'Positiv oder negativ?'),
        },
        neu={
            'det_berechnen': [
                L(3, 'In der Determinante der Vektoren a = (3 | □) und b = (2 | 5) fehlt eine Zahl. Die Determinante hat den Wert 7. Welche Zahl fehlt?',
                  'a = (3 | □)', [4], ['(3*5 - 7)/2'],
                  '3 · 5 − □ · 2 = 7 ⇒ 15 − 2 · □ = 7 ⇒ 2 · □ = 8 ⇒ □ = 4.',
                  'Schreibe die Rechnung über Kreuz mit □ hin und löse nach □ auf.'),
                L(3, 'Die Vektoren a = (x | 2) und b = (3 | 4) hängen von x ab. Gib ihre Determinante als Term an.',
                  '□x + □', [4, -6], ['4', '-2*3'],
                  'x · 4 − 2 · 3 = 4x − 6.', 'Rechne über Kreuz wie mit Zahlen; x bleibt stehen.', hinweis=S),
                Z(3, 'Die Determinante der Vektoren a und b hat den Wert 7. Welchen Wert hat die Determinante, wenn du a und b vertauschst (erst b, dann a)?',
                  -7, '-7', 'Beim Vertauschen tauschen die beiden Produkte die Plätze: aus 12 − 5 wird 5 − 12. Das Ergebnis wechselt das Vorzeichen: −7.',
                  'Probiere es mit a = (4 | 1) und b = (5 | 3) aus.'),
                Z(3, 'Die Determinante der Vektoren a und b hat den Wert 5. Welchen Wert hat die Determinante der Vektoren 2 · a und b?',
                  10, '2*5', 'Verdoppelst du a, verdoppelt sich jedes Produkt mit einer Zahl aus a. Also verdoppelt sich die Determinante: 10. '
                  'Im Bild: Das Parallelogramm wird doppelt so lang.', 'Was passiert mit dem Parallelogramm, wenn ein Pfeil doppelt so lang wird?'),
            ],
            'parallelogramm': [
                L(3, 'Gegeben sind A(0 | 0) und B(4 | 1). Die Punkte D liegen bei D(x | 3) mit x < 12. Sie bilden Parallelogramme ABCD. '
                     'Gib den Flächeninhalt in Abhängigkeit von x an.',
                  'A(x) = (□ · x + □) FE', [-1, 12], ['-1*1', '4*3'],
                  'AB = (4 | 1), AD = (x | 3). Determinante: 4 · 3 − 1 · x = 12 − x. Also A(x) = (−1 · x + 12) FE.',
                  'Bilde AB und AD wie sonst – in AD steht jetzt x.'),
                Z(3, 'Gegeben sind A(0 | 0), B(4 | 1) und D(x | 3). Für welches x hat das Parallelogramm ABCD den Flächeninhalt 8 FE?',
                  4, '12 - 8', 'Fläche: 4 · 3 − 1 · x = 12 − x. Gleichung 12 − x = 8 ⇒ x = 4.',
                  'Stelle die Fläche als Term auf und setze ihn gleich 8.'),
                Z(3, 'Gegeben sind A(0 | 0), B(4 | 1) und D(x | 3). Für welches x entsteht kein Parallelogramm, weil A, B und D auf einer Geraden liegen?',
                  12, '4*3/1', 'Kein Parallelogramm heißt Fläche 0: 12 − x = 0 ⇒ x = 12. Probe: D(12 | 3) = 3 · B, also auf der Geraden durch A und B.',
                  'Welche Fläche hat ein „plattgedrücktes“ Parallelogramm?'),
                A(3, 'Ein Parallelogramm ABCD hat 6 FE. Man verdoppelt alle Koordinaten von A, B, C und D. Wie groß ist das neue Parallelogramm?',
                  '24 FE', ['12 FE', '6 FE', '48 FE'],
                  'Beide Pfeile AB und AD werden doppelt so lang. Jedes Produkt in der Determinante wird 2 · 2 = 4-mal so groß: 4 · 6 = 24 FE.',
                  'Rechne mit AB = (3 | 0) und AD = (0 | 2) und dann mit den doppelten Pfeilen.'),
            ],
            'dreieck': [
                L(3, 'Gegeben sind A(0 | 0) und B(6 | 0). Die Punkte C liegen bei C(x | x + 1) mit x > −1. Gib den Flächeninhalt der Dreiecke ABC in Abhängigkeit von x an.',
                  'A(x) = (□ · x + □) FE', [3, 3], ['6/2', '6*1/2'],
                  'AB = (6 | 0), AC = (x | x + 1). Determinante: 6 · (x + 1) − 0 · x = 6x + 6. Halbieren: A(x) = (3 · x + 3) FE.',
                  'Rechne mit AC = (x | x + 1) über Kreuz und halbiere am Ende.'),
                Z(3, 'Gegeben sind A(0 | 0), B(6 | 0) und C(x | x + 1). Für welches x hat das Dreieck ABC den Flächeninhalt 12 FE?',
                  3, '(12 - 3)/3', 'Fläche: 1/2 · 6 · (x + 1) = 3x + 3. Gleichung 3x + 3 = 12 ⇒ 3x = 9 ⇒ x = 3.',
                  'Stelle zuerst die Fläche als Term in x auf.'),
                A(3, 'Ein Dreieck ABC hat 10 FE. Man verschiebt C parallel zur Seite AB an eine andere Stelle. Wie groß ist das neue Dreieck?',
                  '10 FE', ['größer als 10 FE', 'kleiner als 10 FE', 'Das kann man nicht sagen.'],
                  'Bei einer Verschiebung parallel zu AB bleibt der Abstand von C zur Seite AB gleich. Grundseite und Höhe bleiben, also bleibt die Fläche 10 FE.',
                  'Was ändert sich an Grundseite AB und Höhe?'),
            ],
            'umlaufsinn': [
                Z(3, 'Gegeben sind A(1 | 1), B(5 | 3) und C(x | 5). Für welches x liegen die drei Punkte auf einer Geraden?',
                  9, '1 + 16/2', 'AB = (4 | 2), AC = (x − 1 | 4). Determinante: 4 · 4 − 2 · (x − 1) = 0 ⇒ 16 = 2x − 2 ⇒ x = 9.',
                  'Auf einer Geraden heißt Determinante 0.'),
                A(3, 'Gegeben sind A(0 | 0), B(4 | 0) und C(3 | y). Für welche y laufen die Ecken A → B → C gegen den Uhrzeigersinn?',
                  'für y > 0', ['für y < 0', 'für y > 3', 'für jedes y'],
                  'AB = (4 | 0), AC = (3 | y). Determinante: 4 · y − 0 · 3 = 4y. Gegen den Uhrzeigersinn heißt positiv: 4y > 0, also y > 0.',
                  'Rechne die Determinante mit y aus und frage: Wann ist sie positiv?'),
            ],
            'viereck': [
                L(3, 'Gegeben sind A(0 | 0), B(6 | 0), D(0 | 4) und die Punkte C(x | 5) mit x > 0. Gib den Flächeninhalt der Vierecke ABCD in Abhängigkeit von x an.',
                  'A(x) = (□ · x + □) FE', [2, 15], ['4/2', '6*5/2'],
                  'AB = (6 | 0), AC = (x | 5), AD = (0 | 4). ABC: 6 · 5 − 0 · x = 30. ACD: x · 4 − 5 · 0 = 4x. A(x) = 1/2 · (30 + 4x) = (2 · x + 15) FE.',
                  'Teile mit der Diagonale AC. In AC steht x.'),
                Z(3, 'Gegeben sind A(0 | 0), B(6 | 0), C(x | 5) und D(0 | 4). Für welches x hat das Viereck ABCD den Flächeninhalt 25 FE?',
                  5, '(25 - 15)/2', 'Fläche: 1/2 · (30 + 4x) = 2x + 15. Gleichung 2x + 15 = 25 ⇒ x = 5.',
                  'Erst die Fläche als Term in x, dann gleich 25 setzen.'),
                A(3, 'Du teilst ein Viereck ABCD einmal mit der Diagonale AC und einmal mit der Diagonale BD. Was gilt für die beiden Ergebnisse?',
                  'Beide Wege geben dieselbe Fläche.', ['Mit BD kommt immer mehr heraus.', 'Mit AC kommt immer mehr heraus.', 'Die Ergebnisse hängen von der Lage im Koordinatensystem ab.'],
                  'Beide Diagonalen zerlegen dasselbe Viereck lückenlos in zwei Dreiecke. Die Gesamtfläche bleibt gleich.',
                  'Was ändert sich am Viereck selbst, wenn du anders zerschneidest?'),
                Z(3, 'Von einem Viereck ABCD weißt du: Die Determinante aus AB und AC ist 18. Das Viereck hat 15 FE. Wie groß ist die Determinante aus AC und AD?',
                  12, '2*15 - 18', 'Fläche = 1/2 · (18 + ?) = 15 ⇒ 18 + ? = 30 ⇒ ? = 12.',
                  'Schreibe die Flächenformel hin und rechne rückwärts.'),
            ],
            'vieleck': [
                L(3, 'Gegeben sind A(0 | 0), B(4 | 0), C(6 | 3), D(2 | 6) und die Punkte E(x | 4) mit x ≤ 0. Gib den Flächeninhalt der Fünfecke ABCDE in Abhängigkeit von x an.',
                  'A(x) = (□ · x + □) FE', [-3, 25], ['-6/2', '(12 + 30 + 8)/2'],
                  'AB mit AC: 4 · 3 − 0 · 6 = 12. AC mit AD: 6 · 6 − 3 · 2 = 30. AD mit AE: 2 · 4 − 6 · x = 8 − 6x. '
                  'A(x) = 1/2 · (50 − 6x) = (−3 · x + 25) FE.',
                  'Nur die letzte Determinante (AD mit AE) enthält x.'),
                Z(3, 'Gegeben sind A(0 | 0), B(4 | 0), C(6 | 3), D(2 | 6) und E(x | 4) mit x ≤ 0. Für welches x hat das Fünfeck ABCDE den Flächeninhalt 31 FE?',
                  -2, '(25 - 31)/3', 'Fläche: 1/2 · (12 + 30 + 8 − 6x) = 25 − 3x. Gleichung 25 − 3x = 31 ⇒ −3x = 6 ⇒ x = −2.',
                  'Stelle zuerst die Fläche als Term in x auf.'),
                Z(3, 'Für ein Fünfeck ABCDE gilt: AB mit AC ergibt 10, AC mit AD ergibt 14. Das Fünfeck hat 20 FE. Welchen Wert hat die Determinante aus AD und AE?',
                  16, '2*20 - 10 - 14', 'Fläche = 1/2 · (10 + 14 + ?) = 20 ⇒ 24 + ? = 40 ⇒ ? = 16.',
                  'Verdopple die Fläche und ziehe die bekannten Determinanten ab.'),
            ],
        })


# ---- STUFEN (Zwanzigste Runde, Zusatz RS/IB, Zweig stufen-rsib-1) ----
from _stufen_rsib1 import Stufen, stufen  # noqa: E402

ST = Stufen('abbildungen.determinanten2', 20_71_1)
Z, A, L = ST.Z, ST.A, ST.L

# det_berechnen
ST.stufenleiter('det_berechnen', 'Die Determinante zweier Vektoren über Kreuz ausrechnen und die richtige Rechnung erkennen.',
                'Fehlende Koordinate aus dem Wert bestimmen, Pfeile aus einer Beschreibung übersetzen, Determinanten verrechnen, einfache Sachsituation.',
                'Rechenregeln begründen (Vertauschen, Vervielfachen, Addieren), Vorzeichenfehler finden, Parameter mit Determinante 0, mehrteilige Prüfungsaufgabe.')
ST.typ('det_berechnen', '/^(Berechne|Welchen Wert hat) die Determinante/', 'direkt')
ST.typ('det_berechnen', '/^(Die Determinante der Vektoren a = \\(x|In der Determinante)/', 'umkehr')
ST.typ('det_berechnen', '/hängen von x ab/', 'parameter')
ST.typ('det_berechnen', '/^Die Determinante der Vektoren a und b hat den Wert/', 'begruenden')
ST.neu('det_berechnen', 'erkennen', A('Welche Rechnung liefert die Determinante der Vektoren a = (3 | 1) und b = (2 | 4)?', '3 · 4 − 1 · 2', ['3 · 2 − 1 · 4', '3 · 4 + 1 · 2', '1 · 2 − 3 · 4'],
       'Über Kreuz: obere Zahl von a mal untere Zahl von b, minus untere Zahl von a mal obere Zahl von b: 3 · 4 − 1 · 2 = 10.', 'Schreibe a und b als Spalten nebeneinander.'))
ST.neu('det_berechnen', 'erkennen', A('Welches Vektorpaar hat die Determinante 0?', 'a = (2 | 3) und b = (4 | 6)', ['a = (2 | 3) und b = (3 | 2)', 'a = (1 | 0) und b = (0 | 1)', 'a = (2 | 3) und b = (−2 | 3)'],
       '2 · 6 − 3 · 4 = 0. Die Pfeile zeigen in dieselbe Richtung (b = 2 · a), sie spannen keine Fläche auf. Die anderen Paare ergeben −5, 1 und 12.', 'Wann spannen zwei Pfeile keine Fläche auf?'))
ST.neu('det_berechnen', 'darstellung', Z('Pfeil a führt 3 Kästchen nach rechts und 2 nach oben, Pfeil b 1 Kästchen nach links und 4 nach oben. Berechne die Determinante der beiden Pfeile.', 14, '3 * 4 - 2 * (-1)',
       'a = (3 | 2), b = (−1 | 4), denn „nach links“ ist negativ. 3 · 4 − 2 · (−1) = 12 + 2 = 14.', 'Übersetze zuerst jeden Pfeil in Koordinaten.'))
ST.neu('det_berechnen', 'mehrschritt', Z('Gegeben sind a = (2 | 1), b = (3 | 4) und c = (1 | −2). Berechne die Determinante von a und b plus die Determinante von b und c.', -5, '(2 * 4 - 1 * 3) + (3 * (-2) - 4 * 1)',
       'a und b: 2 · 4 − 1 · 3 = 5. b und c: 3 · (−2) − 4 · 1 = −10. Summe: 5 + (−10) = −5.', 'Rechne die beiden Determinanten einzeln.'))
ST.neu('det_berechnen', 'einkleidung', Z('Eine Fliese hat die Form eines Parallelogramms. Ihre Kanten sind die Pfeile (20 | 0) und (6 | 15), alles in cm. Wie groß ist die Fliese?', 300, '20 * 15 - 0 * 6',
       'Die Determinante ist die Fläche: 20 · 15 − 0 · 6 = 300 cm².', 'Die Determinante der Kantenpfeile ist die Fläche.', einheit='cm²'))
ST.neu('det_berechnen', 'fehler', A('Jemand rechnet die Determinante von a = (4 | 2) und b = (1 | 3) so: 4 · 3 + 2 · 1 = 14. Was stimmt?', 'Falsch: Man zieht ab: 4 · 3 − 2 · 1 = 10.',
       ['Richtig.', 'Falsch: 4 · 1 − 2 · 3 = −2.', 'Falsch: 4 · 2 − 1 · 3 = 5.'],
       'Die Determinante ist „über Kreuz malnehmen, dann abziehen“. Plus statt Minus ergibt 14 statt 10.', 'Plus oder minus zwischen den beiden Produkten?'))
ST.neu('det_berechnen', 'fehler', A('Jemand rechnet die Determinante von a = (5 | −2) und b = (3 | 1) so: 5 · 1 − (−2) · 3 = 5 − 6 = −1. Was stimmt?', 'Falsch: − (−2) · 3 = + 6, also 5 + 6 = 11.',
       ['Richtig.', 'Falsch: 5 · 3 − (−2) · 1 = 17.', 'Falsch: Das Ergebnis ist 1.'],
       '(−2) · 3 = −6. Davon wird abgezogen: 5 − (−6) = 5 + 6 = 11. Der Fehler steckt im Vorzeichen.', 'Rechne (−2) · 3 erst aus und ziehe dann ab.'))
ST.neu('det_berechnen', 'parameter', L('Für welche Zahl t hat die Determinante der Vektoren a = (t | 2) und b = (8 | 4) den Wert 0?', 't = □', [4], ['16 / 4'],
       'Determinante: t · 4 − 2 · 8 = 4t − 16. 4t − 16 = 0 ⇒ 4t = 16 ⇒ t = 4. Probe: a = (4 | 2) und b = (8 | 4) = 2 · a zeigen in dieselbe Richtung.', 'Stelle die Determinante als Term mit t auf.'))
ST.neu('det_berechnen', 'begruenden', A('Stimmt: Addiert man zu b das Doppelte von a, ändert sich die Determinante von a und b nicht?', 'Ja: Es kommt zweimal die Determinante von a mit a dazu, und die ist 0.',
       ['Nein, sie verdoppelt sich.', 'Nein, sie wird 0.', 'Nur wenn a = b ist.'],
       'Beispiel a = (2 | 1), b = (1 | 3): Determinante 5. b + 2a = (5 | 5): 2 · 5 − 1 · 5 = 5. Allgemein: Die Determinante von a mit a ist immer 0 – darum ändert sich nichts.', 'Probiere es mit einem Beispiel aus.'))
ST.neu('det_berechnen', 'pruefung', L('Gegeben sind a = (4 | 1) und b = (x | 3). a) Berechne die Determinante für x = 2. b) Für welches x ist die Determinante 0? c) Für welches x ist sie −8?', 'a) □; b) □; c) □', [10, 12, 20],
       ['4 * 3 - 1 * 2', '12', '12 + 8'], 'Determinante: 4 · 3 − 1 · x = 12 − x. a) 12 − 2 = 10. b) 12 − x = 0 ⇒ x = 12. c) 12 − x = −8 ⇒ x = 20.', 'Stelle zuerst die Determinante als Term mit x auf.'))
ST.knobel('det_berechnen', Z('Die Vektoren a = (n | 1) und b = (1 | n) mit einer natürlichen Zahl n spannen eine Fläche von 48 FE auf. Wie groß ist n?', 7, '7',
          'Determinante: n · n − 1 · 1 = n² − 1. n² − 1 = 48 ⇒ n² = 49 ⇒ n = 7 (n ist natürlich, also nicht −7). Probe: 7 · 7 − 1 = 48.', 'Schreibe die Determinante mit n auf.'))
ST.knobel('det_berechnen', Z('Die Determinante von a und b ist 3. Wie groß ist die Determinante von a + b und a − b (erst a + b, dann a − b)?', -6, '-2 * 3',
          'Probiere ein Beispiel mit Determinante 3: a = (3 | 0), b = (0 | 1). a + b = (3 | 1), a − b = (3 | −1). 3 · (−1) − 1 · 3 = −6. '
          'Allgemein: Ausmultiplizieren ergibt −(a mit b) + (b mit a) = −2 · 3 = −6, weil a mit a und b mit b je 0 sind.', 'Such dir ein einfaches Beispiel mit Determinante 3.'))

# parallelogramm
ST.stufenleiter('parallelogramm', 'Mit zwei gegebenen Spannvektoren die Fläche eines Parallelogramms ausrechnen; die Spannvektoren erkennen.',
                'Spannvektoren aus Eckpunkten bilden, mit Maßstab in m² umrechnen, fehlende Koordinate aus der Fläche, Grundseite mal Höhe mit Determinante vergleichen.',
                'Fläche in Abhängigkeit von x, Lage auf einer Geraden, Wirkung von Verdoppeln und Verschieben begründen, Fehler „Ortsvektoren statt Spannvektoren“, Höhe aus der Fläche, Prüfungsaufgabe mit C.')
ST.typ('parallelogramm', 'Die Vektoren AB', 'direkt')
ST.typ('parallelogramm', '/^(Berechne|Welchen) (den )?Flächeninhalt/', 'mehrschritt')
ST.typ('parallelogramm', 'Ein Beet', 'einkleidung')
ST.typ('parallelogramm', '/^Gegeben sind A\\(0 \\| 0\\)/', 'parameter')
ST.typ('parallelogramm', 'Ein Parallelogramm ABCD hat 6 FE', 'begruenden')
ST.neu('parallelogramm', 'erkennen', A('Welche Vektoren spannen das Parallelogramm ABCD mit A(1 | 2), B(5 | 2) und D(2 | 5) auf?', 'AB = (4 | 0) und AD = (1 | 3)',
       ['AB = (6 | 4) und AD = (3 | 7)', 'AB = (−4 | 0) und AD = (−1 | −3)', 'AB = (4 | 0) und AD = (2 | 5)'],
       'Spitze minus Fuß: AB = (5 − 1 | 2 − 2) = (4 | 0), AD = (2 − 1 | 5 − 2) = (1 | 3).', 'Rechne Spitze minus Fuß.'))
ST.neu('parallelogramm', 'direkt', Z('Ein Parallelogramm wird von den Vektoren a = (5 | 1) und b = (2 | 4) aufgespannt. Wie groß ist es?', 18, '5 * 4 - 1 * 2',
       '5 · 4 − 1 · 2 = 20 − 2 = 18 FE.', 'Determinante über Kreuz.', einheit='FE'))
ST.neu('parallelogramm', 'umkehr', Z('Das Parallelogramm aus AB = (6 | 0) und AD = (2 | h) hat 30 FE (h > 0). Wie groß ist h?', 5, '30 // 6',
       'Determinante: 6 · h − 0 · 2 = 6h. 6h = 30 ⇒ h = 5.', 'Stelle die Determinante mit h auf.'))
ST.neu('parallelogramm', 'darstellung', A('Ein Parallelogramm hat die Ecken A(0 | 0), B(4 | 0), C(6 | 3) und D(2 | 3). Grundseite AB mal Höhe ergibt 4 · 3 = 12 FE. Was ergibt die Determinante aus AB und AD?',
       '4 · 3 − 0 · 2 = 12 FE, also dasselbe', ['4 · 2 − 0 · 3 = 8 FE', '4 · 3 + 0 · 2 = 12 FE, aber nur zufällig', '6 · 3 − 0 · 4 = 18 FE'],
       'AB = (4 | 0), AD = (2 | 3). Determinante 4 · 3 − 0 · 2 = 12. Beide Wege liefern dieselbe Fläche.', 'Bilde AB und AD aus den Ecken.'))
ST.neu('parallelogramm', 'fehler', A('Jemand berechnet das Parallelogramm ABCD mit A(1 | 1), B(4 | 2) und D(2 | 5) mit der Determinante von (4 | 2) und (2 | 5): 16 FE. Was stimmt?',
       'Falsch: Man braucht AB = (3 | 1) und AD = (1 | 4); die Fläche ist 11 FE.', ['Richtig.', 'Falsch: Die Fläche ist 8 FE.', 'Falsch: Man muss das Ergebnis noch halbieren.'],
       'Mit den Punkten selbst (Ortsvektoren) rechnet man ein anderes Parallelogramm aus, eines mit Ecke im Ursprung. Richtig: AB = (3 | 1), AD = (1 | 4), 3 · 4 − 1 · 1 = 11.', 'Welche Pfeile gehen von A aus?'))
ST.neu('parallelogramm', 'verknuepfen', Z('Das Parallelogramm ABCD mit A(0 | 0), B(3 | 4) und D(−2 | 5) hat die Grundseite AB mit der Länge 5. Wie hoch ist es über AB?', 4.6, '(3 * 5 - 4 * (-2)) / 5',
       'Fläche: 3 · 5 − 4 · (−2) = 15 + 8 = 23 FE. Fläche = Grundseite · Höhe ⇒ h = 23 : 5 = 4,6.', 'Erst die Fläche mit der Determinante, dann die Formel Grundseite mal Höhe.'))
ST.neu('parallelogramm', 'begruenden', A('Stimmt: Verschiebt man das ganze Parallelogramm um 3 nach rechts, bleibt die Determinante aus AB und AD gleich?', 'Ja: Die Pfeile AB und AD ändern sich beim Verschieben nicht.',
       ['Nein, sie wird um 3 größer.', 'Nein, sie wird um 9 größer.', 'Nur wenn A im Ursprung liegt.'],
       'Beim Verschieben wird zu jeder x-Koordinate 3 addiert. Spitze minus Fuß bleibt gleich, also auch AB, AD und die Fläche.', 'Was passiert mit „Spitze minus Fuß“?'))
ST.neu('parallelogramm', 'pruefung', L('Gegeben sind A(1 | 1), B(6 | 2) und D(2 | 4) eines Parallelogramms ABCD. a) Berechne die Koordinaten von C. b) Berechne den Flächeninhalt.', 'C(□ | □); A = □ FE', [7, 5, 14],
       ['6 + 1', '2 + 3', '5 * 3 - 1 * 1'], 'AB = (5 | 1), AD = (1 | 3). a) C = B + AD = (6 + 1 | 2 + 3) = (7 | 5). b) 5 · 3 − 1 · 1 = 14 FE.', 'Von B aus geht es so weiter wie von A nach D.'))
ST.knobel('parallelogramm', Z('Das Parallelogramm ABCD hat die Ecken A(0 | 0), B(4 | 1), C(5 | 4) und D(1 | 3). Wie viele Gitterpunkte (Punkte mit ganzzahligen Koordinaten) liegen echt im Inneren?', 10, '10',
          'Fläche: 4 · 3 − 1 · 1 = 11 FE. Auf dem Rand liegen nur die 4 Ecken, weil auf den Seiten (4 | 1) und (1 | 3) keine Gitterpunkte dazwischen liegen. '
          'Zeichnen und Zählen ergibt Zeile y = 1: (1 | 1), (2 | 1), (3 | 1); y = 2: (1 | 2) bis (4 | 2), das sind 4; y = 3: (2 | 3), (3 | 3), (4 | 3). Zusammen 3 + 4 + 3 = 10.', 'Zeichne genau und zähle Zeile für Zeile.'))
ST.knobel('parallelogramm', Z('Im Parallelogramm ABCD mit A(0 | 0), B(4 | 0), C(5 | 3) und D(1 | 3) schneiden sich die Diagonalen in M. Wie groß ist das Dreieck ABM?', 3, '4 * 3 / 4',
          'Die Diagonalen halbieren sich und zerlegen das Parallelogramm in vier gleich große Dreiecke. Fläche: 4 · 3 − 0 · 1 = 12 FE, also ABM = 12 : 4 = 3 FE. '
          'Probe: M(2,5 | 1,5), AB = (4 | 0), AM = (2,5 | 1,5): ½ · (4 · 1,5 − 0) = 3.', 'Wie teilen die beiden Diagonalen das Parallelogramm?', einheit='FE'))

# dreieck
ST.stufenleiter('dreieck', 'Mit zwei Spannvektoren die Dreiecksfläche als halbe Determinante ausrechnen.',
                'Spannvektoren aus Ecken bilden, Plan mit Maßstab, fehlende Koordinate aus der Fläche.',
                'Fläche in Abhängigkeit von x, Verschieben und Verkleinern begründen, Fehler „Halbieren vergessen“, Mittelpunkt nutzen, Koordinaten selbst festlegen, Prüfungsaufgabe.')
ST.typ('dreieck', 'Die Vektoren AB', 'direkt')
ST.typ('dreieck', '/^(Berechne|Welchen) (den )?Flächeninhalt/', 'mehrschritt')
ST.typ('dreieck', 'Auf einem Plan', 'einkleidung')
ST.typ('dreieck', 'Gegeben: A(', 'umkehr')
ST.typ('dreieck', '/^Gegeben sind A\\(0 \\| 0\\)/', 'parameter')
ST.typ('dreieck', 'Ein Dreieck ABC hat 10 FE', 'begruenden')
ST.neu('dreieck', 'erkennen', A('Wie hängen die Fläche des Dreiecks ABC und die Determinante aus AB und AC zusammen (Determinante positiv)?', 'Die Fläche ist die Hälfte der Determinante.',
       ['Die Fläche ist das Doppelte der Determinante.', 'Beide sind gleich groß.', 'Die Fläche ist ein Viertel der Determinante.'],
       'AB und AC spannen ein Parallelogramm auf. Die Seite BC halbiert es, das Dreieck ist die Hälfte.', 'Denk an das Parallelogramm aus AB und AC.'))
ST.neu('dreieck', 'direkt', Z('Berechne den Flächeninhalt des Dreiecks mit A(0 | 0), B(6 | 0) und C(2 | 5).', 15, '(6 * 5 - 0 * 2) / 2',
       'AB = (6 | 0), AC = (2 | 5). Determinante 6 · 5 − 0 · 2 = 30. Dreieck: 30 : 2 = 15 FE.', 'Halbe Determinante.', einheit='FE'))
ST.neu('dreieck', 'fehler', A('Jemand berechnet das Dreieck mit AB = (4 | 1) und AC = (2 | 3) so: 4 · 3 − 1 · 2 = 10 FE. Was stimmt?', 'Falsch: 10 ist das Parallelogramm, das Dreieck hat 5 FE.',
       ['Richtig.', 'Falsch: Es hat 20 FE.', 'Falsch: Es hat 7 FE.'], 'Die Determinante 10 gehört zum Parallelogramm. Das Dreieck ist die Hälfte: 5 FE.', 'Was fehlt noch nach der Determinante?'))
ST.neu('dreieck', 'verknuepfen', Z('M ist der Mittelpunkt der Strecke AB mit A(0 | 0) und B(6 | 2). C liegt bei (1 | 5). Wie groß ist das Dreieck AMC?', 7, '(3 * 5 - 1 * 1) / 2',
       'M = (3 | 1). AM = (3 | 1), AC = (1 | 5). ½ · (3 · 5 − 1 · 1) = ½ · 14 = 7 FE. Das ist die Hälfte von Dreieck ABC (14 FE).', 'Bestimme zuerst M.', einheit='FE'))
ST.neu('dreieck', 'transfer', Z('Ein dreieckiges Grundstück: Vom Eckpunkt A aus liegt B 40 m östlich und 10 m nördlich, C liegt 10 m östlich und 30 m nördlich. Wie groß ist das Grundstück?', 550, '(40 * 30 - 10 * 10) / 2',
       'Lege A in den Ursprung, Osten = x, Norden = y: AB = (40 | 10), AC = (10 | 30). ½ · (40 · 30 − 10 · 10) = ½ · 1 100 = 550 m².', 'Lege selbst ein Koordinatensystem mit A im Ursprung.', einheit='m²'))
ST.neu('dreieck', 'pruefung', L('Gegeben ist das Dreieck ABC mit A(−1 | −2), B(5 | 0) und C(1 | 4). a) Gib AB und AC an. b) Berechne den Flächeninhalt.', 'AB = (□ | □); AC = (□ | □); A = □ FE', [6, 2, 2, 6, 16],
       ['5 + 1', '0 + 2', '1 + 1', '4 + 2', '(6 * 6 - 2 * 2) / 2'], 'a) AB = (5 − (−1) | 0 − (−2)) = (6 | 2), AC = (2 | 6). b) ½ · (6 · 6 − 2 · 2) = ½ · 32 = 16 FE.', 'Spitze minus Fuß, Vorsicht bei negativen Koordinaten.'))
ST.neu('dreieck', 'begruenden', A('Stimmt: Halbiert man alle Koordinaten von A, B und C, halbiert sich die Fläche des Dreiecks?', 'Nein: Sie wird nur ein Viertel so groß.',
       ['Ja, genau.', 'Nein, sie bleibt gleich.', 'Nein, sie verdoppelt sich.'],
       'AB und AC werden halbiert. In der Determinante werden beide Produkte mit ½ · ½ = ¼ multipliziert. Beispiel: AB = (4 | 0), AC = (0 | 4): 8 FE; halbiert: (2 | 0), (0 | 2): 2 FE.', 'Probiere ein Beispiel aus.'))
ST.knobel('dreieck', L('A(0 | 0) und B(4 | 0) sind fest. C liegt auf der Geraden y = x + 1, und das Dreieck ABC hat 10 FE. Gib beide möglichen x-Koordinaten von C an.', 'x₁ = □; x₂ = □', [-6, 4], ['-6', '4'],
          'C(x | x + 1). AB = (4 | 0), AC = (x | x + 1). Fläche = ½ · |4 · (x + 1)| = 2 · |x + 1| = 10 ⇒ |x + 1| = 5. Also x + 1 = 5 (x = 4) oder x + 1 = −5 (x = −6). '
          'C kann oberhalb oder unterhalb von AB liegen.', 'C kann über oder unter der x-Achse liegen.'))
ST.knobel('dreieck', Z('Im Quadrat A(0 | 0), B(6 | 0), C(6 | 6), D(0 | 6) ist M der Mittelpunkt von BC. Wie groß ist das Dreieck AMD?', 18, '(6 * 6 - 3 * 0) / 2',
          'M(6 | 3). AM = (6 | 3), AD = (0 | 6). ½ · (6 · 6 − 3 · 0) = 18 FE – genau die Hälfte des Quadrats. Das gilt für jeden Punkt M auf BC: Grundseite AD = 6, Höhe immer 6.', 'Rechne – und überlege, ob das Ergebnis von der Lage von M abhängt.', einheit='FE'))

# umlaufsinn
ST.stufenleiter('umlaufsinn', 'Aus dem Vorzeichen der Determinante den Umlaufsinn ablesen.',
                'Umlaufsinn aus Eckpunkten berechnen, Fläche als Betrag, Vertauschen der Pfeile, Laufweg im Alltag.',
                'Reihenfolge gegen den Uhrzeigersinn festlegen, Fehler mit negativer Fläche finden, Lage auf einer Geraden begründen, Parameter für Umlaufsinn und Gerade.')
ST.typ('umlaufsinn', 'Für A, B, C ist die Determinante', 'erkennen')
ST.typ('umlaufsinn', '/^(Wie laufen die Ecken|Berechne den Flächeninhalt)/', 'mehrschritt')
ST.typ('umlaufsinn', 'Die Ecken P', 'verknuepfen')
ST.typ('umlaufsinn', 'Jemand rechnet', 'fehler')
ST.typ('umlaufsinn', 'Bilden A', 'begruenden')
ST.typ('umlaufsinn', 'Gegeben sind A(', 'parameter')
ST.neu('umlaufsinn', 'direkt', A('Berechne die Determinante aus AB = (2 | 1) und AC = (1 | 3). Wie laufen die Ecken A → B → C?', '5, gegen den Uhrzeigersinn', ['5, im Uhrzeigersinn', '−5, im Uhrzeigersinn', '7, gegen den Uhrzeigersinn'],
       '2 · 3 − 1 · 1 = 5 > 0: gegen den Uhrzeigersinn.', 'Positiv heißt gegen den Uhrzeigersinn.'))
ST.neu('umlaufsinn', 'umkehr', A('Für A, B, C ergibt die Determinante aus AB und AC den Wert −14. Welchen Wert hat die Determinante aus AC und AB (Reihenfolge vertauscht)?', '14', ['−14', '7', '−7'],
       'Vertauscht man die beiden Pfeile, ändert sich nur das Vorzeichen: 14. Das passt: A → C → B läuft andersherum als A → B → C.', 'Was ändert sich beim Vertauschen?'))
ST.neu('umlaufsinn', 'einkleidung', A('Auf einem Sportplatz läuft jemand von der Ecke A(0 | 0) zur Fahne B(30 | 10), dann zur Fahne C(10 | 40) und zurück zu A. Läuft er gegen den Uhrzeigersinn?', 'Ja, die Determinante ist 1 100 > 0.',
       ['Nein, die Determinante ist −1 100.', 'Nein, die Punkte liegen auf einer Geraden.', 'Das kann man ohne Zeichnung nicht sagen.'],
       'AB = (30 | 10), AC = (10 | 40). 30 · 40 − 10 · 10 = 1 100 > 0: gegen den Uhrzeigersinn.', 'Berechne die Determinante aus AB und AC.'))
ST.knobel('umlaufsinn', Z('A(0 | 0) und B(5 | 0) sind fest. C(x | y) hat ganzzahlige Koordinaten mit −3 ≤ x ≤ 3 und −3 ≤ y ≤ 3. Für wie viele solche Punkte C laufen A → B → C gegen den Uhrzeigersinn?', 21, '3 * 7',
          'AB = (5 | 0), AC = (x | y). Determinante 5 · y − 0 · x = 5y. Sie ist positiv genau für y > 0, also y = 1, 2, 3. Für x gibt es jeweils 7 Werte: 3 · 7 = 21. Auf x kommt es gar nicht an.',
          'Schreibe die Determinante mit x und y auf. Welche Koordinate zählt?'))
ST.knobel('umlaufsinn', Z('A(1 | 2), B(4 | 3) und C(x | 6) mit einer ganzen Zahl x. Welchen kleinsten Flächeninhalt kann das Dreieck ABC haben, wenn es ein echtes Dreieck sein soll (Fläche nicht 0)?', 0.5, '1 / 2',
          'AB = (3 | 1), AC = (x − 1 | 4). Determinante: 3 · 4 − 1 · (x − 1) = 13 − x. Für x = 13 liegen die Punkte auf einer Geraden (Fläche 0). '
          'Kleinster Wert ungleich 0: x = 12 oder x = 14 mit |13 − x| = 1, Fläche ½ · 1 = 0,5 FE.', 'Wann ist die Fläche 0? Was liegt knapp daneben?', einheit='FE'))

# viereck
ST.stufenleiter('viereck', 'Ein Viereck mit drei gegebenen Pfeilen AB, AC, AD in zwei Dreiecke zerlegen und die Fläche ausrechnen.',
                'Pfeile aus den Ecken bilden, Grundstück auf einem Plan, fehlende Determinante aus der Fläche bestimmen.',
                'Fehler „½ vergessen“ finden, Zerlegung über die andere Diagonale begründen, Drachen und Rechteck als Sonderfall, Parameter x, Prüfungsaufgabe.')
ST.typ('viereck', 'Für das Viereck', 'direkt')
ST.typ('viereck', '/^(Berechne|Welchen) (den )?Flächeninhalt/', 'mehrschritt')
ST.typ('viereck', 'Jemand rechnet', 'fehler')
ST.typ('viereck', 'Ein Grundstück', 'einkleidung')
ST.typ('viereck', 'Gegeben sind A(', 'parameter')
ST.typ('viereck', 'Du teilst ein Viereck', 'begruenden')
ST.typ('viereck', 'Von einem Viereck', 'umkehr')
ST.neu('viereck', 'erkennen', A('In welche zwei Dreiecke zerlegt die Diagonale AC das Viereck ABCD?', 'ABC und ACD', ['ABD und BCD', 'ABC und BCD', 'ACD und ABD'],
       'Die Diagonale AC verbindet A und C. Auf der einen Seite liegt B (Dreieck ABC), auf der anderen D (Dreieck ACD).', 'Welche Ecken liegen links und rechts der Diagonale?'))
ST.neu('viereck', 'direkt', Z('Berechne den Flächeninhalt des Vierecks mit A(0 | 0), B(4 | 0), C(5 | 3) und D(0 | 2).', 11, '(4 * 3 - 0 * 5 + 5 * 2 - 3 * 0) / 2',
       'AB = (4 | 0), AC = (5 | 3), AD = (0 | 2). AB mit AC: 12. AC mit AD: 5 · 2 − 3 · 0 = 10. Fläche: ½ · (12 + 10) = 11 FE.', 'Zwei Determinanten, dann halbieren.', einheit='FE'))
ST.neu('viereck', 'transfer', Z('Ein Flugdrachen hat die Ecken A(0 | 0), B(3 | 4), C(0 | 10) und D(−3 | 4), Maße in dm. Wie viel dm² Stoff braucht man?', 30, '(3 * 10 - 4 * 0 + 0 * 4 - 10 * (-3)) / 2',
       'AB = (3 | 4), AC = (0 | 10), AD = (−3 | 4). AB mit AC: 30. AC mit AD: 0 · 4 − 10 · (−3) = 30. ½ · 60 = 30 dm². Probe: Diagonalen 6 und 10, ½ · 6 · 10 = 30.', 'Zerlege von A aus.', einheit='dm²'))
ST.neu('viereck', 'verknuepfen', A('Was liefert die Determinanten-Methode für das Rechteck ABCD mit A(0 | 0), B(a | 0), C(a | b) und D(0 | b)?', '½ · (a · b + a · b) = a · b',
       ['½ · a · b', '2 · a · b', 'a + b'], 'AB = (a | 0), AC = (a | b), AD = (0 | b). AB mit AC: a · b. AC mit AD: a · b − b · 0 = a · b. ½ · 2ab = ab – die bekannte Rechteckformel.',
       'Rechne mit den Buchstaben wie mit Zahlen.'))
ST.neu('viereck', 'pruefung', L('Gegeben ist das Viereck ABCD mit A(−2 | −1), B(4 | −2), C(5 | 3) und D(0 | 4). a) Gib AC an. b) Berechne den Flächeninhalt.', 'AC = (□ | □); A = □ FE', [7, 4, 29],
       ['5 + 2', '3 + 1', '((6 * 4 - (-1) * 7) + (7 * 5 - 4 * 2)) / 2'],
       'AB = (6 | −1), AC = (7 | 4), AD = (2 | 5). AB mit AC: 24 + 7 = 31. AC mit AD: 35 − 8 = 27. ½ · 58 = 29 FE.', 'Erst alle drei Pfeile, dann zwei Determinanten.'))
ST.knobel('viereck', Z('Im Quadrat A(0 | 0), B(6 | 0), C(6 | 6), D(0 | 6) liegen P(6 | 2) auf BC und Q(2 | 6) auf CD. Wie groß ist das Dreieck APQ?', 16, '(6 * 6 - 2 * 2) / 2',
          'AP = (6 | 2), AQ = (2 | 6): ½ · (36 − 4) = 16 FE. Andere Idee: Quadrat 36 minus drei Dreiecke ABP (6), AQD (6) und PCQ (½ · 4 · 4 = 8): 36 − 20 = 16.', 'Du kannst rechnen oder vom Quadrat etwas abziehen.', einheit='FE'))
ST.knobel('viereck', Z('Die Mittelpunkte der vier Seiten des Vierecks A(0 | 0), B(8 | 0), C(6 | 6), D(0 | 4) bilden ein neues Viereck. Wie groß ist es?', 18, '36 / 2',
          'ABCD: AB = (8 | 0), AC = (6 | 6), AD = (0 | 4): ½ · (48 + 24) = 36 FE. Mittelpunkte (4 | 0), (7 | 3), (3 | 5), (0 | 2). '
          'Von (4 | 0) aus: (3 | 3), (−1 | 5), (−4 | 2): ½ · ((15 + 3) + (−2 + 20)) = 18 FE – genau die Hälfte. Das gilt für jedes Viereck.', 'Berechne beide Flächen und vergleiche.', einheit='FE'))

# vieleck
ST.stufenleiter('vieleck', 'Ein Fünfeck mit gegebenen Pfeilen von A aus in drei Dreiecke zerlegen; wissen, wie viele Determinanten man braucht.',
                'Pfeile aus den Ecken bilden, Sechseck, Spielplatz mit Maßstab, Ecken aus einer Tabelle, fehlende Determinante aus der Fläche.',
                'Fehler „ein Dreieck zu viel“, Unabhängigkeit von der Startecke und Umlaufsinn nach Spiegeln begründen, L-Form mit Rechtecken prüfen, Hauswand als Modell, Parameter, Prüfungsaufgabe.')
ST.typ('vieleck', 'Für das Fünfeck', 'direkt')
ST.typ('vieleck', 'Wie viele Determinanten', 'erkennen')
ST.typ('vieleck', 'Berechne den Flächeninhalt des', 'mehrschritt')
ST.typ('vieleck', 'Ein Spielplatz', 'einkleidung')
ST.typ('vieleck', 'Gegeben sind A(', 'parameter')
ST.typ('vieleck', 'Für ein Fünfeck', 'umkehr')
ST.neu('vieleck', 'darstellung', Z('Die Ecken eines Fünfecks stehen in einer Tabelle: A(0 | 0), B(4 | 0), C(5 | 3), D(2 | 5), E(0 | 3). Berechne den Flächeninhalt.', 18.5, '(4 * 3 - 0 * 5 + 5 * 5 - 3 * 2 + 2 * 3 - 5 * 0) / 2',
       'AB = (4 | 0), AC = (5 | 3), AD = (2 | 5), AE = (0 | 3). 12 + (25 − 6) + (6 − 0) = 37. ½ · 37 = 18,5 FE.', 'Bilde die vier Pfeile von A aus.', einheit='FE'))
ST.neu('vieleck', 'fehler', A('Jemand rechnet beim Fünfeck ABCDE die Determinanten AB mit AC, AC mit AD, AD mit AE und dazu AE mit AB, addiert und halbiert. Was stimmt?',
       'Falsch: AE mit AB gehört nicht dazu, es sind nur drei Dreiecke.', ['Richtig, das sind die vier Dreiecke.', 'Falsch: Man darf nicht halbieren.', 'Falsch: Es fehlt noch AB mit AD.'],
       'Von A aus entstehen beim Fünfeck nur drei Dreiecke: ABC, ACD und ADE. Jedes weitere Produkt verfälscht das Ergebnis.', 'Wie viele Dreiecke entstehen beim Fünfeck?'))
ST.neu('vieleck', 'begruenden', A('Stimmt: Zerlegt man ein Vieleck von der Ecke C statt von A aus, kommt dieselbe Fläche heraus?', 'Ja, die Fläche hängt nicht davon ab, wo man zerlegt.',
       ['Nein, von A aus ist es immer mehr.', 'Nur bei Fünfecken.', 'Nein, das Vorzeichen ist dann immer negativ.'],
       'Die Fläche ist eine Eigenschaft der Figur. Jede Zerlegung in Dreiecke liefert dieselbe Summe, solange die Ecken in derselben Reihenfolge laufen.', 'Hängt die Fläche einer Figur von der Rechnung ab?'))
ST.neu('vieleck', 'begruenden', A('Ein Fünfeck ABCDE (gegen den Uhrzeigersinn) hat 20 FE. Man spiegelt es an der y-Achse und rechnet mit denselben Buchstaben. Was ergibt die halbe Summe der Determinanten?', '−20, weil die Ecken jetzt im Uhrzeigersinn laufen',
       ['20, es ändert sich nichts', '−40', '0'], 'Spiegeln dreht den Umlaufsinn um. Jede Determinante wechselt das Vorzeichen, die Fläche bleibt 20 FE.', 'Was macht eine Spiegelung mit dem Umlaufsinn?'))
ST.neu('vieleck', 'verknuepfen', Z('Ein L-förmiges Sechseck hat die Ecken A(0 | 0), B(6 | 0), C(6 | 2), D(2 | 2), E(2 | 5), F(0 | 5). Berechne die Fläche mit Determinanten (von A aus).', 18,
       '(6 * 2 - 0 * 6 + 6 * 2 - 2 * 2 + 2 * 5 - 2 * 2 + 2 * 5 - 5 * 0) / 2',
       'AB mit AC: 12. AC mit AD: 12 − 4 = 8. AD mit AE: 10 − 4 = 6. AE mit AF: 10 − 0 = 10. ½ · 36 = 18 FE. Probe mit Rechtecken: 6 · 2 + 2 · 3 = 18.', 'Prüfe dein Ergebnis mit zwei Rechtecken.', einheit='FE'))
ST.neu('vieleck', 'transfer', Z('Eine Hauswand ist 4 m breit und bis zur Dachkante 4 m hoch, der Giebel in der Mitte ist 6 m hoch. Lege die Wand in ein Koordinatensystem und berechne ihre Fläche mit Determinanten.', 20,
       '(4 * 4 - 0 * 4 + 4 * 6 - 4 * 2 + 2 * 4 - 6 * 0) / 2',
       'Ecken A(0 | 0), B(4 | 0), C(4 | 4), D(2 | 6), E(0 | 4). 16 + (24 − 8) + (8 − 0) = 40. ½ · 40 = 20 m². Probe: Rechteck 16 + Dreieck 4.', 'Lege eine Ecke der Wand in den Ursprung.', einheit='m²'))
ST.neu('vieleck', 'pruefung', Z('Ein Fünfeck hat die Ecken A(1 | 0), B(5 | 1), C(6 | 4), D(3 | 6) und E(0 | 3). Zerlege von A aus und berechne den Flächeninhalt.', 22.5,
       '((4 * 4 - 1 * 5) + (5 * 6 - 4 * 2) + (2 * 3 - 6 * (-1))) / 2',
       'AB = (4 | 1), AC = (5 | 4), AD = (2 | 6), AE = (−1 | 3). 11 + 22 + 12 = 45. ½ · 45 = 22,5 FE.', 'Vier Pfeile, drei Determinanten.', einheit='FE'))
ST.knobel('vieleck', Z('Aus einem Quadrat mit A(0 | 0), C(6 | 6) entsteht ein Achteck, indem man an jeder Ecke ein Dreieck mit zwei Schenkeln der Länge 2 abschneidet. Wie groß ist das Achteck?', 28, '36 - 4 * 2',
          'Das Quadrat hat 36 FE. Jedes abgeschnittene Dreieck hat ½ · 2 · 2 = 2 FE, vier davon 8 FE. 36 − 8 = 28 FE. '
          'Mit Determinanten über die Ecken (2 | 0), (4 | 0), (6 | 2), (6 | 4), (4 | 6), (2 | 6), (0 | 4), (0 | 2) kommt dasselbe heraus.', 'Muss man wirklich sechs Determinanten rechnen?', einheit='FE'))
ST.knobel('vieleck', Z('Das Fünfeck A(0 | 0), B(6 | 0), C(6 | 4), D(3 | 6), E(0 | 4) wird zum Viereck ABCE, indem man die Ecke D weglässt. Um wie viel FE wird die Fläche kleiner?', 6, '((-3) * 0 - 2 * (-6)) / 2',
          'Der Unterschied ist genau das Dreieck CDE. CD = (−3 | 2), CE = (−6 | 0): ½ · ((−3) · 0 − 2 · (−6)) = 6 FE. Probe: Fünfeck 30 FE, Rechteck ABCE 24 FE.', 'Welche Figur fällt weg?', einheit='FE'))


if __name__ == '__main__':
    d = bauen('abbildungen.determinanten2',
          'Flächen von Dreiecken, Vierecken und Vielecken im Koordinatensystem mit zweireihigen Determinanten berechnen.',
          ['Determinante: a₁ · b₂ − a₂ · b₁ (über Kreuz).',
           'Parallelogramm: A = Determinante aus AB und AD. Dreieck: A = ½ · Determinante aus AB und AC.',
           'Ecken gegen den Uhrzeigersinn benennen; negatives Ergebnis heißt falsche Reihenfolge.',
           'Vielecke von A aus in Dreiecke zerlegen: Determinanten benachbarter Vektoren addieren, halbieren.'],
          [('Determinanten', ['det_berechnen']), ('Dreieck und Parallelogramm', ['parallelogramm', 'dreieck', 'umlaufsinn']),
           ('Vierecke und Vielecke', ['viereck', 'vieleck'])],
          ETAPPEN, GEN,
          offen=['Die App kann keine Vektorpfeile zeichnen; Vektoren erscheinen als Strecken. App-Wunsch: Pfeilspitzen bei Strecken im Koordinatensystem.',
                 'Determinanten werden als „Determinante der Vektoren a und b“ ausgeschrieben; die Spaltenschreibweise steht nur als Tabelle in der Lernkarte.'])
    umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=['Die App kann keine Vektorpfeile zeichnen'])
    durchsicht(d)
    stufen('abbildungen.determinanten2', ST)
