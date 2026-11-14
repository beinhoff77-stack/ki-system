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


GEN = {'det_berechnen': g_det_berechnen, 'parallelogramm': g_parallelogramm, 'dreieck': g_dreieck,
       'umlaufsinn': g_umlaufsinn, 'viereck': g_viereck, 'vieleck': g_vieleck}

if __name__ == '__main__':
    bauen('abbildungen.determinanten2',
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
