#!/usr/bin/env python3
"""Thema abbildungen.matrizen – Matrizen und Abbildungen mit Matrizen (Realschule Bayern Klasse 10, IB MYP 4)."""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _rs import *  # noqa: E402,F403

start(4901)
LP, HP = "P'(□ | □)", 'Trage die x- und die y-Koordinate des Bildpunkts ein.'
LM, HM = '(□ □; □ □)', 'Zeilenweise: oben links, oben rechts, unten links, unten rechts.'


def nz(n):
    return R.choice([i for i in range(-n, n + 1) if i != 0])


def mat(m):
    (a, b), (c, d) = m
    return f'({dz(a)}  {dz(b)}; {dz(c)}  {dz(d)})'


def mal(m, p):
    (a, b), (c, d) = m
    return (a * p[0] + b * p[1], c * p[0] + d * p[1])


def mm(m, n):
    (a, b), (c, d) = m
    (e, f), (g, h) = n
    return ((a * e + b * g, a * f + b * h), (c * e + d * g, c * f + d * h))


def det2(m):
    (a, b), (c, d) = m
    return a * d - b * c


def zuf_mat(g=5, null=True):
    while True:
        m = ((R.randint(-g, g), R.randint(-g, g)), (R.randint(-g, g), R.randint(-g, g)))
        if null or 0 not in (m[0] + m[1]): return m


def lin2(a, b):
    """a·x + b·y als Text (ohne 1x, ohne Nullglieder)"""
    t = poly(a, 0) if a else ''
    if b:
        t = (t + ' ' + plus_v(b, 'y')) if t else poly(b, 0).replace('x', 'y')
    return t or '0'


def flach(m):
    return [m[0][0], m[0][1], m[1][0], m[1][1]]


ABB = {
    'Spiegelung an der x-Achse': ((1, 0), (0, -1)),
    'Spiegelung an der y-Achse': ((-1, 0), (0, 1)),
    'Punktspiegelung am Ursprung': ((-1, 0), (0, -1)),
    'Spiegelung an der Geraden y = x': ((0, 1), (1, 0)),
    'Drehung um O um 90°': ((0, -1), (1, 0)),
    'Drehung um O um 270° (−90°)': ((0, 1), (-1, 0)),
}

ETAPPEN = [
    {'lernziel': 'bildpunkt', 'titel': 'Bildpunkte mit einer Matrix',
     'regel': 'Eine ⟦Matrix⟧ ist ein Zahlenschema mit Zeilen und Spalten. Hier schreiben wir sie ⟦zeilenweise⟧: M = (a  b; c  d). Die Abbildung P(x | y) ↦ P\'(x\' | y\') rechnet ⟦Zeile mal Spalte⟧: ⟦x\' = a · x + b · y⟧ und ⟦y\' = c · x + d · y⟧.',
     'bild': {'typ': 'tabelle', 'kopf': ['M', 'mal x', 'mal y'], 'zeilen': [['Zeile 1 → x\'', '2', '−1'], ['Zeile 2 → y\'', '3', '4']]},
     'schritte': ["M = (2  −1; 3  4), P(5 | 2). x' = 2 · 5 + (−1) · 2 = 8.", "y' = 3 · 5 + 4 · 2 = 23. Also ⟦P'(8 | 23)⟧."],
     'fehler': "Spaltenweise statt zeilenweise zu rechnen, also x' = 2 · 5 + 3 · 2 = 16, ist falsch: Für x' nimmst du die ⟦erste Zeile⟧ (2 und −1)."},
    {'lernziel': 'abbildungsmatrix', 'titel': 'Matrizen bekannter Abbildungen',
     'regel': 'Die Spalten der Matrix sind die ⟦Bilder der Einheitspunkte⟧ (1 | 0) und (0 | 1). Spiegelung an der x-Achse: ⟦(1  0; 0  −1)⟧. Drehung um O um 90°: ⟦(0  −1; 1  0)⟧. Zentrische Streckung mit Faktor k: ⟦(k  0; 0  k)⟧.',
     'schritte': ['Spiegelung an der y-Achse: (1 | 0) ↦ (−1 | 0), (0 | 1) ↦ (0 | 1).', 'Diese Bilder als Spalten: ⟦(−1  0; 0  1)⟧.'],
     'probe': "P(3 | 2): x' = −3, y' = 2 – gespiegelt an der y-Achse ✓",
     'fehler': 'Für die Drehung um 90° die Matrix (0  1; −1  0) zu nehmen ist falsch: Das dreht um ⟦−90°⟧ (im Uhrzeigersinn). (1 | 0) muss auf ⟦(0 | 1)⟧ gehen.'},
    {'lernziel': 'drehung', 'titel': 'Drehung um einen beliebigen Winkel',
     'regel': 'Die Drehung um O um den Winkel φ (gegen den Uhrzeigersinn) hat die Matrix ⟦(cos φ  −sin φ; sin φ  cos φ)⟧. Also ⟦x\' = x · cos φ − y · sin φ⟧ und ⟦y\' = x · sin φ + y · cos φ⟧.',
     'schritte': ["P(4 | 0), φ = 30°: x' = 4 · cos 30° − 0 = 4 · 0,866… ≈ 3,46.", "y' = 4 · sin 30° + 0 = 4 · 0,5 = 2. Also ⟦P'(3,46 | 2)⟧."],
     'probe': 'Abstand zu O bleibt 4: 3,46² + 2² ≈ 16 ✓',
     'fehler': "x' = x · cos φ + y · sin φ ist falsch: In der ersten Zeile steht ⟦−sin φ⟧. Sonst dreht man in die falsche Richtung."},
    {'lernziel': 'rechnen', 'titel': 'Mit Matrizen rechnen',
     'regel': 'Matrizen gleicher Größe ⟦addierst⟧ du Eintrag für Eintrag. Beim ⟦Vervielfachen⟧ wird jeder Eintrag mal die Zahl genommen. Beim ⟦Multiplizieren⟧ A · B rechnest du ⟦Zeile von A mal Spalte von B⟧. A · B beschreibt die Abbildung „erst B, dann A“.',
     'schritte': ['A = (1  2; 0  3), B = (4  0; 1  −1). Oben links: Zeile 1 von A mal Spalte 1 von B: 1 · 4 + 2 · 1 = 6.',
                  'Ebenso die anderen Einträge: A · B = ⟦(6  −2; 3  −3)⟧.'],
     'probe': 'Oben rechts: 1 · 0 + 2 · (−1) = −2 ✓',
     'fehler': 'A · B Eintrag für Eintrag zu multiplizieren, also (4  0; 0  −3), ist falsch: Beim Matrizenprodukt gilt ⟦Zeile mal Spalte⟧. Außerdem ist meist ⟦A · B ≠ B · A⟧.'},
    {'lernziel': 'inverse', 'titel': 'Determinante und Umkehrmatrix',
     'regel': 'Die ⟦Determinante⟧ von M = (a  b; c  d) ist ⟦a · d − b · c⟧. Ist sie ⟦nicht 0⟧, gibt es die ⟦inverse Matrix⟧ M⁻¹ = 1/(ad − bc) · (d  −b; −c  a). Sie macht die Abbildung rückgängig.',
     'schritte': ['M = (3  1; 5  2): det M = 3 · 2 − 1 · 5 = 1.', 'M⁻¹ = (2  −1; −5  3) (Hauptdiagonale tauschen, Nebendiagonale Vorzeichen wechseln, durch 1 teilen).'],
     'probe': 'M · M⁻¹: oben links 3 · 2 + 1 · (−5) = 1, oben rechts 3 · (−1) + 1 · 3 = 0 ✓',
     'fehler': 'Bei M⁻¹ auch b und c zu ⟦vertauschen⟧, also (2  −5; −1  3), ist falsch: Nur a und d tauschen die Plätze; b und c ⟦bleiben⟧, bekommen aber das andere Vorzeichen.'},
    {'lernziel': 'skalarprodukt', 'titel': 'Skalarprodukt und Winkel',
     'regel': 'Das ⟦Skalarprodukt⟧ zweier Vektoren a = (a₁ | a₂) und b = (b₁ | b₂) ist die Zahl ⟦a₁ · b₁ + a₂ · b₂⟧. Ist es ⟦0⟧, stehen die Vektoren ⟦senkrecht⟧ aufeinander. Den Winkel liefert ⟦cos φ = (a · b) : (|a| · |b|)⟧.',
     'schritte': ['a = (3 | 4), b = (4 | −3): a · b = 12 − 12 = 0, also ⟦senkrecht⟧.',
                  'a = (3 | 4), c = (5 | 0): a · c = 15; |a| = 5, |c| = 5; cos φ = 15 : 25 = 0,6 ⇒ ⟦φ ≈ 53,1°⟧.'],
     'fehler': 'a · b = (3 · 4 | 4 · (−3)) = (12 | −12) ist falsch: Das Skalarprodukt ist ⟦eine Zahl⟧, kein Vektor. Die Produkte werden ⟦addiert⟧.'},
]


# ---------- Generatoren ----------
def g_bildpunkt(s):
    m = zuf_mat(3 if s == 1 else 5)
    if s == 1:
        m = ((R.randint(0, 4), R.randint(0, 4)), (R.randint(0, 4), R.randint(0, 4)))
    p = (nz(6), nz(6)) if s > 1 else (R.randint(1, 6), R.randint(1, 6))
    q = mal(m, p)
    (a, b), (c, d) = m
    w = f"x' = {kl(a)} · {kl(p[0])} + {kl(b)} · {kl(p[1])} = {dz(q[0])}; y' = {kl(c)} · {kl(p[0])} + {kl(d)} · {kl(p[1])} = {dz(q[1])}. P'({dz(q[0])} | {dz(q[1])})."
    cc = [f'({a}) * ({p[0]}) + ({b}) * ({p[1]})', f'({c}) * ({p[0]}) + ({d}) * ({p[1]})']
    if s in (1, 2):
        return luecken(f'Bilde P({dz(p[0])} | {dz(p[1])}) mit M = {mat(m)} ab.', LP, HP, q, w, 'Zeile 1 mal (x | y) gibt x\', Zeile 2 gibt y\'.', c=cc)
    art = R.random()
    if art < 0.35:
        sp = (a * p[0] + c * p[1], b * p[0] + d * p[1])
        if sp == q: return None
        return auswahl(f'Welcher Bildpunkt entsteht, wenn P({dz(p[0])} | {dz(p[1])}) mit M = {mat(m)} abgebildet wird?', f"P'({dz(q[0])} | {dz(q[1])})",
                       [f"P'({dz(sp[0])} | {dz(sp[1])})", f"P'({dz(a * p[0])} | {dz(d * p[1])})", f"P'({dz(q[1])} | {dz(q[0])})"], w,
                       'Zeilenweise rechnen, nicht spaltenweise.')
    if art < 0.7:
        return luecken(f"Die Abbildung hat die Gleichungen x' = {poly(a, 0)} {plus_v(b, 'y')} und y' = {poly(c, 0)} {plus_v(d, 'y')}. Gib die Matrix an.".replace('x\' = 0 ', "x' = ").replace("y' = 0 ", "y' = "),
                       LM, HM, flach(m), f'Die Koeffizienten zeilenweise: M = {mat(m)}.', 'Vor x und y stehen die Einträge der Zeilen.', c=[str(v) for v in flach(m)]) \
            if 0 not in flach(m) else None
    # Urpunkt gesucht (det = ±1)
    m = R.choice([((2, 1), (1, 1)), ((3, 2), (1, 1)), ((1, 1), (0, 1)), ((2, 3), (1, 2)), ((1, -1), (1, 0)), ((3, 1), (2, 1))])
    q = mal(m, p)
    return luecken(f"Die Abbildung mit M = {mat(m)} bildet P auf P'({dz(q[0])} | {dz(q[1])}) ab. Berechne P.", 'P(□ | □)', 'x, y', p,
                   f"Gleichungssystem: {lin2(*m[0])} = {dz(q[0])} und {lin2(*m[1])} = {dz(q[1])}. Lösung P({dz(p[0])} | {dz(p[1])}).",
                   'Stelle die zwei Abbildungsgleichungen auf und löse das Gleichungssystem.',
                   c=[f'(({m[1][1]}) * ({q[0]}) - ({m[0][1]}) * ({q[1]})) / ({det2(m)})', f'(({m[0][0]}) * ({q[1]}) - ({m[1][0]}) * ({q[0]})) / ({det2(m)})'])


def g_abbildungsmatrix(s):
    name, m = R.choice(list(ABB.items()))
    if s == 1:
        p = (nz(6), nz(6))
        q = mal(m, p)
        return luecken(f'Bilde P({dz(p[0])} | {dz(p[1])}) durch die {name} ab. Die Matrix ist {mat(m)}.', LP, HP, q,
                       f"x' = {kl(m[0][0])} · {kl(p[0])} + {kl(m[0][1])} · {kl(p[1])} = {dz(q[0])}; y' = {kl(m[1][0])} · {kl(p[0])} + {kl(m[1][1])} · {kl(p[1])} = {dz(q[1])}.",
                       'Zeile mal Spalte.', c=[f'({m[0][0]}) * ({p[0]}) + ({m[0][1]}) * ({p[1]})', f'({m[1][0]}) * ({p[0]}) + ({m[1][1]}) * ({p[1]})'])
    if s == 2:
        if R.random() < 0.5:
            andere = [mat(v) for k, v in ABB.items() if k != name]
            return auswahl(f'Welche Matrix beschreibt die {name}?', mat(m), R.sample(andere, 3),
                           f'Bilder der Einheitspunkte: (1 | 0) ↦ ({dz(m[0][0])} | {dz(m[1][0])}), (0 | 1) ↦ ({dz(m[0][1])} | {dz(m[1][1])}). Als Spalten: {mat(m)}.',
                           'Wohin gehen (1 | 0) und (0 | 1)? Das sind die Spalten.')
        k = R.choice([2, 3, -2, Fr(1, 2), Fr(5, 2), -1])
        if Fr(k).denominator != 1:
            return auswahl(f'Welche Matrix beschreibt die zentrische Streckung an O mit k = {dz(k)}?', mat(((k, 0), (0, k))),
                           [mat(((k, 0), (0, 1))), mat(((0, k), (k, 0))), mat(((1, k), (k, 1)))],
                           f'Jede Koordinate wird mit {dz(k)} multipliziert: ({dz(k)}  0; 0  {dz(k)}).', 'x\' = k · x und y\' = k · y.')
        return luecken(f'Gib die Matrix der zentrischen Streckung an O mit k = {dz(k)} an.', LM, HM, [k, 0, 0, k],
                       f"x' = {kl(k)} · x und y' = {kl(k)} · y, also ({dz(k)}  0; 0  {dz(k)}).", 'Beide Koordinaten werden mit k multipliziert.',
                       c=[str(k), '0', '0', str(k)])
    art = R.random()
    if art < 0.4:
        andere = [k for k in ABB if k != name]
        return auswahl(f'Welche Abbildung beschreibt die Matrix {mat(m)}?', name, R.sample(andere, 3),
                       f'(1 | 0) ↦ ({dz(m[0][0])} | {dz(m[1][0])}) und (0 | 1) ↦ ({dz(m[0][1])} | {dz(m[1][1])}): das ist die {name}.',
                       'Bilde die Einheitspunkte (1 | 0) und (0 | 1) ab.')
    if art < 0.7:
        # zweimal 90° = 180°
        n2 = mm(ABB['Drehung um O um 90°'], ABB['Drehung um O um 90°'])
        return luecken('Berechne die Matrix für zweimal nacheinander „Drehung um O um 90°“, also (0  −1; 1  0) · (0  −1; 1  0).', LM, HM, flach(n2),
                       f'Zeile mal Spalte: (−1  0; 0  −1). Zweimal 90° ist 180° – die Punktspiegelung am Ursprung.',
                       'Matrizen multiplizieren: Zeile mal Spalte.', c=[str(v) for v in flach(n2)]) if R.random() < 0.3 else \
            luecken(f'Gib die Matrix der {name} an.', LM, HM, flach(m),
                    f'(1 | 0) ↦ ({dz(m[0][0])} | {dz(m[1][0])}), (0 | 1) ↦ ({dz(m[0][1])} | {dz(m[1][1])}). Matrix {mat(m)}.',
                    'Bilder der Einheitspunkte als Spalten.', c=[str(v) for v in flach(m)])
    return auswahl('Jemand gibt für die Drehung um O um 90° (gegen den Uhrzeigersinn) die Matrix (0  1; −1  0) an. Was stimmt?',
                   'Falsch: Das ist die Drehung um −90°. Richtig ist (0  −1; 1  0).',
                   ['Richtig.', 'Falsch: Richtig ist (−1  0; 0  −1).', 'Falsch: Richtig ist (0  1; 1  0).'],
                   '(1 | 0) muss auf (0 | 1) gehen. Mit (0  1; −1  0) geht (1 | 0) auf (0 | −1) – das ist eine Drehung im Uhrzeigersinn.',
                   'Bilde (1 | 0) ab und schau, wohin es zeigt.') if R.random() < 0.5 else None


WINKEL = [30, 45, 60, 120, 135, 150, 20, 40, 70, 110, 200, 300]


def g_drehung(s):
    phi = R.choice(WINKEL)
    co, si = math.cos(math.radians(phi)), math.sin(math.radians(phi))
    p = (R.randint(1, 8), 0) if s == 1 else (nz(6), nz(6))
    xs = p[0] * co - p[1] * si
    ys = p[0] * si + p[1] * co
    welche = R.choice(['x', 'y'])
    wert = xs if welche == 'x' else ys
    if gerundet(wert, 2) is None: return None
    r = round(wert, 2)
    w = (f"x' = {kl(p[0])} · cos {phi}° − {kl(p[1])} · sin {phi}° ≈ {dz(round(xs, 2))}; "
         f"y' = {kl(p[0])} · sin {phi}° + {kl(p[1])} · cos {phi}° ≈ {dz(round(ys, 2))}.")
    c = f'round({wert:.12f}, 2)'
    if s in (1, 2):
        return zahl(f"P({dz(p[0])} | {dz(p[1])}) wird um O um {phi}° gedreht. Berechne {welche}' auf zwei Dezimalen.", w,
                    "x' = x · cos φ − y · sin φ; y' = x · sin φ + y · cos φ.", r, c)
    art = R.random()
    if art < 0.35:
        return auswahl(f'Welche Matrix beschreibt die Drehung um O um {phi}°?', f'(cos {phi}°  −sin {phi}°; sin {phi}°  cos {phi}°)',
                       [f'(cos {phi}°  sin {phi}°; −sin {phi}°  cos {phi}°)', f'(sin {phi}°  −cos {phi}°; cos {phi}°  sin {phi}°)', f'(cos {phi}°  −sin {phi}°; −sin {phi}°  cos {phi}°)'],
                       'Drehmatrix: (cos φ  −sin φ; sin φ  cos φ). Das Minus steht oben rechts.', 'Wo steht das Minus?')
    if art < 0.7:
        return zahl(f"P({dz(p[0])} | {dz(p[1])}) wird um O um {phi}° gedreht. Berechne {welche}' auf zwei Dezimalen.", w,
                    'Setze in die Drehmatrix ein. Achte auf das Minus bei sin φ in der ersten Zeile.', r, c)
    # Abstand bleibt
    d2_ = p[0] ** 2 + p[1] ** 2
    dist = math.sqrt(d2_)
    if gerundet(dist, 2) is None: return None
    return zahl(f"P({dz(p[0])} | {dz(p[1])}) wird um O um {phi}° gedreht. Wie weit ist P' vom Ursprung entfernt? Runde auf zwei Dezimalen.",
                f'Eine Drehung um O ändert den Abstand zu O nicht: |OP| = √({kl(p[0])}² + {kl(p[1])}²) = √{d2_} ≈ {dz(round(dist, 2))}.',
                'Rechnen ist nicht nötig, wenn du weißt, was eine Drehung mit dem Abstand zu O macht.', round(dist, 2), f'round({dist:.12f}, 2)')


def g_rechnen(s):
    A, B = zuf_mat(5), zuf_mat(5)
    if s == 1:
        if R.random() < 0.5:
            S = tuple(tuple(A[i][j] + B[i][j] for j in range(2)) for i in range(2))
            return luecken(f'Berechne A + B für A = {mat(A)} und B = {mat(B)}.', LM, HM, flach(S), f'Eintrag für Eintrag addieren: A + B = {mat(S)}.',
                           'Gleiche Stellen addieren.', c=[f'({flach(A)[i]}) + ({flach(B)[i]})' for i in range(4)])
        k = nz(4)
        S = tuple(tuple(k * A[i][j] for j in range(2)) for i in range(2))
        return luecken(f'Berechne {kl(k)} · A für A = {mat(A)}.', LM, HM, flach(S), f'Jeden Eintrag mal {dz(k)}: {mat(S)}.',
                       'Jeder Eintrag wird mit der Zahl multipliziert.', c=[f'{k} * ({v})' for v in flach(A)])
    A, B = zuf_mat(4), zuf_mat(4)
    P = mm(A, B)
    (a, b), (c, d) = A
    (e, f), (g, h) = B
    w = (f'Oben links: {kl(a)} · {kl(e)} + {kl(b)} · {kl(g)} = {dz(P[0][0])}; oben rechts: {kl(a)} · {kl(f)} + {kl(b)} · {kl(h)} = {dz(P[0][1])}; '
         f'unten links: {kl(c)} · {kl(e)} + {kl(d)} · {kl(g)} = {dz(P[1][0])}; unten rechts: {kl(c)} · {kl(f)} + {kl(d)} · {kl(h)} = {dz(P[1][1])}.')
    cc = [f'({a})*({e})+({b})*({g})', f'({a})*({f})+({b})*({h})', f'({c})*({e})+({d})*({g})', f'({c})*({f})+({d})*({h})']
    if s == 2:
        return luecken(f'Berechne A · B für A = {mat(A)} und B = {mat(B)}.', LM, HM, flach(P), w, 'Zeile von A mal Spalte von B.', c=cc)
    art = R.random()
    if art < 0.35:
        falsch = ((a * e, b * f), (c * g, d * h))
        Q = mm(B, A)
        if Q == P or falsch == P: return None
        return auswahl(f'Was ergibt A · B für A = {mat(A)} und B = {mat(B)}?', mat(P), [mat(falsch), mat(Q), mat(tuple(tuple(A[i][j] + B[i][j] for j in range(2)) for i in range(2)))],
                       w, 'Zeile mal Spalte – und auf die Reihenfolge achten.')
    if art < 0.7:
        Q = mm(B, A)
        gleich = Q == P
        return auswahl(f'Gilt A · B = B · A für A = {mat(A)} und B = {mat(B)}?', 'Ja' if gleich else 'Nein',
                       ['Nein' if gleich else 'Ja', 'Das gilt für alle Matrizen.'],
                       f'A · B = {mat(P)}, B · A = {mat(Q)}. ' + ('Hier zufällig gleich.' if gleich else 'Verschieden – die Reihenfolge zählt.'),
                       'Rechne beide Produkte aus.')
    # Verkettung: erst Spiegelung an x-Achse, dann Drehung 90°
    n1, m1 = R.choice(list(ABB.items()))
    n2, m2 = R.choice([(k, v) for k, v in ABB.items() if k != n1])
    V = mm(m2, m1)
    return luecken(f'Erst wird die {n1} ausgeführt, dann die {n2}. Gib die Matrix der Verkettung an (zweite Matrix · erste Matrix).', LM, HM, flach(V),
                   f'{mat(m2)} · {mat(m1)} = {mat(V)}.', '„Erst B, dann A“ heißt A · B.',
                   c=[f'({m2[0][0]})*({m1[0][0]})+({m2[0][1]})*({m1[1][0]})', f'({m2[0][0]})*({m1[0][1]})+({m2[0][1]})*({m1[1][1]})',
                      f'({m2[1][0]})*({m1[0][0]})+({m2[1][1]})*({m1[1][0]})', f'({m2[1][0]})*({m1[0][1]})+({m2[1][1]})*({m1[1][1]})'])


EINS = [((2, 1), (1, 1)), ((3, 1), (5, 2)), ((2, 3), (1, 2)), ((4, 3), (1, 1)), ((5, 2), (2, 1)), ((3, 2), (4, 3)), ((1, 2), (1, 3)),
        ((2, 5), (1, 3)), ((3, 5), (1, 2)), ((4, 1), (3, 1)), ((5, 3), (3, 2)), ((2, -1), (-3, 2)), ((1, -2), (1, -1)), ((3, -1), (-2, 1))]


def g_inverse(s):
    if s == 1:
        m = zuf_mat(6)
        return zahl(f'Berechne die Determinante von M = {mat(m)}.', f'det M = {kl(m[0][0])} · {kl(m[1][1])} − {kl(m[0][1])} · {kl(m[1][0])} = {dz(det2(m))}.',
                    'Hauptdiagonale mal minus Nebendiagonale mal.', det2(m), f'({m[0][0]}) * ({m[1][1]}) - ({m[0][1]}) * ({m[1][0]})')
    m = R.choice(EINS)
    if R.random() < 0.5: m = ((m[1][1], m[0][1]), (m[1][0], m[0][0]))
    D = det2(m)
    (a, b), (c, d) = m
    inv = ((d * D, -b * D), (-c * D, a * D))  # D = ±1
    w = f'det M = {kl(a)} · {kl(d)} − {kl(b)} · {kl(c)} = {dz(D)}. M⁻¹ = 1/{kl(D)} · ({dz(d)}  {dz(-b)}; {dz(-c)}  {dz(a)}) = {mat(inv)}.'
    if D not in (1, -1): return None
    if s == 2:
        return luecken(f'Berechne die inverse Matrix von M = {mat(m)}.', LM, HM, flach(inv), w,
                       'a und d tauschen, b und c Vorzeichen wechseln, durch die Determinante teilen.', c=[f'({v}) / ({D})' for v in (d, -b, -c, a)])
    art = R.random()
    if art < 0.35:
        k = R.choice([2, 3])
        sing = ((k, 2 * k), (1, 2)) if R.random() < 0.5 else ((nz(4), 0), (nz(4), 0))
        if R.random() < 0.5:
            return auswahl(f'Hat M = {mat(sing)} eine inverse Matrix?', 'Nein, denn det M = 0.',
                           ['Ja, jede Matrix hat eine.', f'Ja, M⁻¹ = {mat(((sing[1][1], -sing[0][1]), (-sing[1][0], sing[0][0])))}.', 'Nein, weil ein Eintrag größer als 1 ist.'],
                           f'det M = {kl(sing[0][0])} · {kl(sing[1][1])} − {kl(sing[0][1])} · {kl(sing[1][0])} = 0. Durch 0 kann man nicht teilen.',
                           'Berechne zuerst die Determinante.')
        return auswahl(f'Welche Matrix ist die Inverse von M = {mat(m)}?', mat(inv),
                       [mat(((d * D, -c * D), (-b * D, a * D))), mat(((d, b), (c, a))), mat(((-a, -b), (-c, -d)))], w,
                       'Probe: M · M⁻¹ muss (1  0; 0  1) ergeben.')
    if art < 0.7:
        x = R.randint(-6, 6)
        m2 = ((x, R.randint(1, 5)), (R.randint(1, 5), R.randint(1, 5)))
        D2 = det2(m2)
        return zahl(f'Für welches x hat M = (x  {dz(m2[0][1])}; {dz(m2[1][0])}  {dz(m2[1][1])}) keine inverse Matrix?',
                    f'Keine Inverse, wenn det M = 0: x · {dz(m2[1][1])} − {kl(m2[0][1])} · {dz(m2[1][0])} = 0 ⇒ x = {dz(Fr(m2[0][1] * m2[1][0], m2[1][1]))}.',
                    'Setze die Determinante gleich 0.', Fr(m2[0][1] * m2[1][0], m2[1][1]), f'{m2[0][1]} * {m2[1][0]} / {m2[1][1]}') \
            if endlich(Fr(m2[0][1] * m2[1][0], m2[1][1])) else None
    # Urpunkt mit Inverse
    p = (nz(5), nz(5))
    q = mal(m, p)
    return luecken(f"M = {mat(m)} bildet P auf P'({dz(q[0])} | {dz(q[1])}) ab. Berechne P mit der inversen Matrix.", 'P(□ | □)', 'x, y', p,
                   w + f" P = M⁻¹ · P' = ({dz(p[0])} | {dz(p[1])}).", 'Erst M⁻¹ bestimmen, dann M⁻¹ mal P\'.',
                   c=[f'({inv[0][0]}) * ({q[0]}) + ({inv[0][1]}) * ({q[1]})', f'({inv[1][0]}) * ({q[0]}) + ({inv[1][1]}) * ({q[1]})'])


TRIPEL = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 6, 10), (4, 3, 5), (12, 5, 13), (0, 5, 5), (5, 0, 5), (0, 4, 4), (3, 0, 3)]


def g_skalarprodukt(s):
    a, b = (nz(7), nz(7)), (nz(7), nz(7))
    sp = a[0] * b[0] + a[1] * b[1]
    w = f'a · b = {kl(a[0])} · {kl(b[0])} + {kl(a[1])} · {kl(b[1])} = {dz(sp)}.'
    if s == 1:
        return zahl(f'Berechne das Skalarprodukt von a = {vek(*a)} und b = {vek(*b)}.', w, 'x mal x plus y mal y.', sp,
                    f'({a[0]}) * ({b[0]}) + ({a[1]}) * ({b[1]})')
    if s == 2:
        if R.random() < 0.5:
            k = nz(3)
            bb = (-k * a[1], k * a[0]) if R.random() < 0.5 else (-k * a[1] + R.choice([-1, 1]), k * a[0])
            sp2 = a[0] * bb[0] + a[1] * bb[1]
            return auswahl(f'Stehen a = {vek(*a)} und b = {vek(*bb)} senkrecht aufeinander?', 'Ja' if sp2 == 0 else 'Nein',
                           ['Nein' if sp2 == 0 else 'Ja', 'Das kann man nur mit einer Zeichnung entscheiden.'],
                           f'a · b = {kl(a[0])} · {kl(bb[0])} + {kl(a[1])} · {kl(bb[1])} = {dz(sp2)}. ' + ('Null: senkrecht.' if sp2 == 0 else 'Nicht null: nicht senkrecht.'),
                           'Berechne das Skalarprodukt.')
        y = R.randint(-6, 6)
        bx = R.choice([d for d in (-4, -3, -2, -1, 1, 2, 3, 4)])
        ax = R.randint(-6, 6)
        # a = (ax | 2), b = (bx | y): ax*bx + 2*y = 0 -> gesucht ax so dass ... wir fragen nach y
        a2 = (bx * 2, nz(4))
        if (a2[0] * R.choice([1])) == 0: return None
        # gesucht t mit (t | a2[1]) · (bx | 2) = 0 -> t*bx + 2*a2[1] = 0
        t = Fr(-2 * a2[1], bx)
        if not endlich(t): return None
        return zahl(f'Für welches t stehen a = (t | {dz(a2[1])}) und b = ({dz(bx)} | 2) senkrecht aufeinander?',
                    f'a · b = {dz(bx)}t {plus(2 * a2[1])} = 0 ⇒ t = {dz(t)}.', 'Senkrecht heißt Skalarprodukt 0.', t, f'-2 * ({a2[1]}) / ({bx})')
    art = R.random()
    u = R.choice(TRIPEL)
    v = R.choice(TRIPEL)
    u = (u[0] * R.choice([1, -1]), u[1] * R.choice([1, -1]), u[2])
    v = (v[0] * R.choice([1, -1]), v[1] * R.choice([1, -1]), v[2])
    if (u[0], u[1]) == (0, 0) or (v[0], v[1]) == (0, 0): return None
    spr = u[0] * v[0] + u[1] * v[1]
    co = Fr(spr, u[2] * v[2])
    phi = math.degrees(math.acos(float(co)))
    if gerundet(phi, 1) is None: return None
    if art < 0.6:
        return zahl(f'Berechne den Winkel zwischen a = {vek(u[0], u[1])} und b = {vek(v[0], v[1])} auf eine Dezimale.',
                    f'a · b = {dz(spr)}; |a| = {u[2]}, |b| = {v[2]}; cos φ = {dz(spr)} : {u[2] * v[2]} = {dz(co) if endlich(co) else br(co)} ⇒ φ ≈ {dz(round(phi, 1))}°.',
                    'cos φ = Skalarprodukt geteilt durch das Produkt der Längen.', round(phi, 1), f'round({phi:.12f}, 1)', einheit='°')
    return auswahl(f'Jemand berechnet für a = {vek(*a)} und b = {vek(*b)}: a · b = {vek(a[0] * b[0], a[1] * b[1])}. Was stimmt?',
                   f'Falsch: Das Skalarprodukt ist eine Zahl: {dz(sp)}.', ['Richtig.', f'Falsch: a · b = {vek(a[0] + b[0], a[1] + b[1])}.', f'Falsch: a · b = {dz(a[0] * b[1] - a[1] * b[0])}.'],
                   w, 'Ist das Skalarprodukt ein Vektor oder eine Zahl?')


GEN = {'bildpunkt': g_bildpunkt, 'abbildungsmatrix': g_abbildungsmatrix, 'drehung': g_drehung, 'rechnen': g_rechnen,
       'inverse': g_inverse, 'skalarprodukt': g_skalarprodukt}

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import ko, pkte, tab  # noqa: E402

_SP = ['', 'Spalte 1', 'Spalte 2']


def _bp(x, y):
    return tab(['M', 'mal x = 5', 'mal y = 2', 'ergibt'], ['Zeile 1 → x′', '2', '−1', x], ['Zeile 2 → y′', '3', '4', y])


def _ab(a, b, c, d):
    return tab(['A · B', 'Spalte 1', 'Spalte 2'], ['Zeile 1', a, b], ['Zeile 2', c, d])


_E = {'E₁': (1, 0), 'E₂': (0, 1)}
_M = [['M Zeile 1', '3', '1'], ['M Zeile 2', '5', '2']]
UMBAU = {
    'bildpunkt': {
        'einstieg': 'Ein Grafikprogramm verschiebt, dreht und spiegelt Bilder. Dafür speichert es vier Zahlen in einem Schema '
                    'mit zwei Zeilen. So ein Zahlenschema heißt ⟦Matrix⟧.',
        'woerter': [['Matrix', 'Zahlenschema mit Zeilen und Spalten; hier zeilenweise geschrieben: (a  b; c  d)'],
                    ['Zeile mal Spalte', 'die Zahlen einer Zeile mit x und y malnehmen und addieren']],
        'bild': _bp('?', '?'),
        'schritte': [
            {'text': 'M = (2  −1; 3  4) bildet P(5 | 2) ab.'},
            {'text': 'Zeile mal Spalte: x′ = 2 · 5 + (−1) · 2 = 8.', 'bild': _bp('8', '?')},
            {'text': 'Mit Zeile 2: y′ = 3 · 5 + 4 · 2 = 23.', 'bild': _bp('8', '23')},
            {'text': 'Also ⟦P′(8 | 23)⟧.',
             'bild': ko([-1, 10], [-2, 25], pkte({'P': (5, 2), 'P′': (8, 23)}), schritt=0, schritt_x=2, schritt_y=5, pfeile=[[5, 2, 8, 23]])},
        ],
        'fehler': 'Spaltenweise rechnen ist falsch: 2 · 5 + 3 · 2 = 16. Für x′ nimmst du die ⟦erste Zeile⟧, also 2 und −1.',
        'regel': 'Bildpunkt: ⟦Zeile mal Spalte⟧. Die erste Zeile ergibt x′, die zweite Zeile ergibt y′.',
    },
    'abbildungsmatrix': {
        'einstieg': 'Das Grafikprogramm muss nur wissen, wohin (1 | 0) und (0 | 1) gehen. '
                    'Daraus baut es die ganze Matrix. Die beiden heißen ⟦Einheitspunkte⟧.',
        'woerter': [['Einheitspunkte', 'die Punkte (1 | 0) und (0 | 1)'],
                    ['Spalte', 'die Zahlen, die in der Matrix untereinanderstehen']],
        'bild': ko([-2, 2], [-2, 2], _E),
        'schritte': [
            {'text': 'Spiegelung an der y-Achse: (1 | 0) geht nach (−1 | 0).',
             'bild': {'punkte': pkte({**_E, 'E₁′': (-1, 0)}), 'pfeile': [[1, 0, -1, 0]]}},
            {'text': '(0 | 1) liegt auf der Achse und bleibt, wo er ist.'},
            {'text': 'Bilder als Spalten: ⟦(−1  0; 0  1)⟧.', 'bild': tab(_SP, ['Zeile 1', '−1', '0'], ['Zeile 2', '0', '1'])},
        ],
        'fehler': '(0  1; −1  0) dreht nicht um 90°, sondern um ⟦−90°⟧. Bei +90° muss (1 | 0) nach (0 | 1) gehen.',
        'fehler_bild': ko([-2, 2], [-2, 2], pkte({'E₁': (1, 0), 'falsch': (0, -1)}), pfeile=[[1, 0, 0, -1, '−90°']]),
        'regel': 'Die Spalten sind die ⟦Bilder der Einheitspunkte⟧. Erst (1 | 0) abbilden, dann (0 | 1), beides als Spalte eintragen.',
    },
    'drehung': {
        'einstieg': 'Ein Riesenrad dreht eine Gondel um seine Mitte. Die Gondel bleibt gleich weit von der Mitte entfernt. '
                    'Für jeden Winkel φ gibt es eine ⟦Drehmatrix⟧.',
        'woerter': [['φ', 'griechischer Buchstabe „phi“ für den Drehwinkel'],
                    ['Drehmatrix', '(cos φ  −sin φ; sin φ  cos φ); dreht um O gegen den Uhrzeigersinn']],
        'bild': ko([-1, 5], [-1, 5], {'P': (4, 0), 'O': (0, 0)}, kreise=[{'m': [0, 0], 'r': 4}]),
        'schritte': [
            {'text': 'P(4 | 0) wird um φ = 30° gedreht.'},
            {'text': 'x′ = 4 · cos 30° − 0 · sin 30° ≈ 3,46.'},
            {'text': 'y′ = 4 · sin 30° + 0 · cos 30° = 2.'},
            {'text': 'Also ⟦P′(3,46 | 2)⟧, wieder 4 von der Mitte entfernt.',
             'bild': {'punkte': pkte({'P': (4, 0), 'O': (0, 0), 'P′': (3.46, 2)}), 'strecken': [[0, 0, 4, 0], [0, 0, 3.46, 2]]}},
        ],
        'fehler': 'x′ = x · cos φ + y · sin φ ist falsch. Oben rechts steht ⟦−sin φ⟧, sonst dreht es falsch herum.',
        'regel': 'Drehung um φ: ⟦(cos φ  −sin φ; sin φ  cos φ)⟧. Der Abstand zu O bleibt gleich.',
    },
    'rechnen': {
        'einstieg': 'Das Programm soll erst spiegeln und dann drehen. Statt zweimal zu rechnen, fasst es beide Matrizen zu einer zusammen. '
                    'Das heißt ⟦Matrizen multiplizieren⟧.',
        'woerter': [['A · B', 'das Matrizenprodukt: erst B anwenden, dann A'],
                    ['Einträge', 'die vier Zahlen einer Matrix']],
        'bild': _ab('?', '?', '?', '?'),
        'schritte': [
            {'text': 'A = (1  2; 0  3) und B = (4  0; 1  −1).'},
            {'text': 'Oben links in A · B: Zeile 1 von A mal Spalte 1 von B.'},
            {'text': '1 · 4 + 2 · 1 = 6.', 'bild': _ab('6', '?', '?', '?')},
            {'text': 'Ebenso die anderen Einträge: A · B = ⟦(6  −2; 3  −3)⟧.', 'bild': _ab('6', '−2', '3', '−3')},
        ],
        'fehler': 'Eintrag für Eintrag malnehmen, also (4  0; 0  −3), ist falsch. Es gilt ⟦Zeile mal Spalte⟧, und meist ist A · B ≠ B · A.',
        'fehler_bild': _ab('4 ✗', '0 ✗', '0 ✗', '−3 ✗'),
        'regel': 'A · B: ⟦Zeile von A mal Spalte von B⟧. Addieren und Vervielfachen gehen dagegen Eintrag für Eintrag.',
    },
    'inverse': {
        'einstieg': 'Das Programm soll eine Drehung rückgängig machen. Dafür braucht es die umgekehrte Matrix. '
                    'Sie heißt ⟦inverse Matrix⟧ und existiert nur, wenn die Determinante nicht 0 ist.',
        'woerter': [['Determinante', 'die Zahl a · d − b · c'],
                    ['inverse Matrix', 'macht die Abbildung rückgängig; geschrieben M⁻¹']],
        'bild': tab(_SP, *_M),
        'schritte': [
            {'text': 'Determinante von M: 3 · 2 − 1 · 5 = 1.'},
            {'text': 'Sie ist nicht 0, also gibt es die inverse Matrix.'},
            {'text': 'a und d tauschen, b und c bekommen ein Minus.',
             'bild': tab(_SP, *_M, ['M⁻¹ Zeile 1', '2', '−1'], ['M⁻¹ Zeile 2', '−5', '3'])},
            {'text': 'Durch die Determinante 1 teilen: ⟦M⁻¹ = (2  −1; −5  3)⟧.'},
        ],
        'fehler': '(2  −5; −1  3) ist falsch. b und c ⟦bleiben an ihrem Platz⟧ und wechseln nur das Vorzeichen.',
        'regel': 'Inverse: a und d tauschen, b und c mit Minus. Dann ⟦durch die Determinante teilen⟧, die nicht 0 sein darf.',
    },
    'skalarprodukt': {
        'einstieg': 'Ein Zimmermann prüft, ob zwei Balken einen rechten Winkel bilden. Mit Vektoren geht das ohne Geodreieck: '
                    'Er rechnet eine Zahl aus. Sie heißt ⟦Skalarprodukt⟧.',
        'woerter': [['Skalarprodukt', 'a₁ · b₁ + a₂ · b₂ – eine Zahl, kein Vektor'],
                    ['senkrecht', 'im rechten Winkel'], ['|a|', 'die Länge des Vektors a']],
        'bild': ko([-1, 6], [-4, 5], pfeile=[[0, 0, 3, 4, 'a'], [0, 0, 4, -3, 'b']]),
        'schritte': [
            {'text': 'Skalarprodukt von a = (3 | 4) und b = (4 | −3):'},
            {'text': '3 · 4 + 4 · (−3) = 0, also ⟦senkrecht⟧.'},
            {'text': 'Mit c = (5 | 0) ist a · c = 15.', 'bild': {'pfeile': [[0, 0, 3, 4, 'a'], [0, 0, 5, 0, 'c']]}},
            {'text': '|a| = |c| = 5, also cos φ = 15 : 25 = 0,6.'},
            {'text': 'Der Winkel ist ⟦φ ≈ 53,1°⟧.'},
        ],
        'fehler': '(12 | −12) als Ergebnis ist falsch. Das Skalarprodukt ist ⟦eine Zahl⟧: Die Produkte werden addiert.',
        'regel': 'Skalarprodukt: ⟦a₁ · b₁ + a₂ · b₂⟧. Ist es 0, stehen die Vektoren senkrecht aufeinander.',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


if __name__ == '__main__':
    d = bauen('abbildungen.matrizen',
          'Abbildungen im Koordinatensystem mit Matrizen beschreiben (Spiegelung, Drehung, Streckung), mit Matrizen rechnen, Umkehrmatrizen bestimmen und das Skalarprodukt nutzen.',
          ["P'(x' | y') mit M = (a  b; c  d): x' = a · x + b · y, y' = c · x + d · y.",
           'Die Spalten der Matrix sind die Bilder von (1 | 0) und (0 | 1).', 'Drehung um φ: (cos φ  −sin φ; sin φ  cos φ).',
           'A · B: Zeile mal Spalte; „erst B, dann A“. Meist A · B ≠ B · A.', 'Inverse existiert nur für det M ≠ 0.',
           'Skalarprodukt a₁b₁ + a₂b₂; null heißt senkrecht; cos φ = (a · b) : (|a| · |b|).'],
          [('Abbildungen mit Matrizen', ['bildpunkt', 'abbildungsmatrix', 'drehung']), ('Rechnen mit Matrizen', ['rechnen', 'inverse']),
           ('Skalarprodukt', ['skalarprodukt'])],
          ETAPPEN, GEN,
          offen=['Matrizen werden zeilenweise als (a  b; c  d) geschrieben; Lückenschablone (□ □; □ □). App-Wunsch: echte Matrixdarstellung (2×2-Klammer) im Text oder als Zeichnung.',
                 'IB MYP 4: Lösen linearer Gleichungssysteme mit der inversen Matrix nur als Urpunkt-Aufgabe enthalten; Parkettierungen nicht enthalten (bräuchten Zeichnungen).',
                 'Spiegelung an beliebigen Ursprungsgeraden (cos 2α, sin 2α) weggelassen; nur Achsen, y = x, Drehungen und zentrische Streckung.'])
    umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
