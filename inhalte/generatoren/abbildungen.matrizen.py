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


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-1) ----------
# Prüfungsvorbilder: Realschul-Abschlussprüfung Mathematik I (Bayern), Bereich „Abbildungen“ (Bildpunkte in Abhängigkeit von x,
# orthogonale Affinität und Drehung mit Matrix, Urpunkt rückwärts); IB-MYP-Aufgabenformate zu Matrizen und Skalarprodukt
# (rechter Winkel, Winkel zwischen Vektoren). Typ übernommen, Wortlaut und Zahlen eigen.
def durchsicht(d):
    import math
    from _rsib1 import Z, A, L, nachtrag, finde, rund
    T = lambda teil: finde(d, teil)
    MT, MH = '(□ □; □ □)', 'Trage die Einträge zeilenweise ein: oben links, oben rechts; unten links, unten rechts.'
    nachtrag(d,
        umstufen={
            T('Welcher Bildpunkt entsteht, wenn P(−2 | −2) mit M = (5  −4; 1  −4) abgebildet wird?'): 2,
            T('Welcher Bildpunkt entsteht, wenn P(−3 | −5) mit M = (−2  4; −3  −3) abgebildet wird?'): 2,
            T('Gib die Matrix der Spiegelung an der y-Achse an.'): 2,
            T('Gib die Matrix der Drehung um O um 270° (−90°) an.'): 2,
            T('Gib die Matrix der Punktspiegelung am Ursprung an.'): 2,
            T('Welche Matrix beschreibt die Drehung um O um 300°?'): 2,
            T('P(−5 | 5) wird um O um 40° gedreht. Berechne y\''): 2,
            T('Was ergibt A · B für A = (−1  −3; 3  −4)'): 2,
        },
        ersetzen={
            T('Welche Abbildung beschreibt die Matrix (0  1; −1  0)?'):
                L(3, 'Eine Abbildung bildet (1 | 0) auf (2 | 1) und (0 | 1) auf (−1 | 3) ab. Gib ihre Matrix an.', MT, [2, -1, 1, 3], ['2', '-1', '1', '3'],
                  'Die Bilder der Einheitspunkte sind die Spalten: erste Spalte (2 | 1), zweite Spalte (−1 | 3).', 'Welche Spalte gehört zu (1 | 0)?', hinweis=MH),
            T('Welche Abbildung beschreibt die Matrix (−1  0; 0  1)?'):
                L(3, 'Gib die Matrix der orthogonalen Affinität mit der x-Achse als Achse und dem Faktor k = 3 an (alle y-Werte werden verdreifacht, x bleibt).',
                  MT, [1, 0, 0, 3], ['1', '0', '0', '3'], '(1 | 0) bleibt (1 | 0). (0 | 1) wird (0 | 3). Spalten: (1 0; 0 3).',
                  'Bilde die beiden Einheitspunkte ab.', hinweis=MH),
            T('P(5 | 5) wird um O um 200° gedreht. Berechne y\''):
                Z(3, 'P(4 | 0) wird um O gedreht und landet bei P′(0 | 4). Um wie viel Grad wurde gedreht (zwischen 0° und 360°)?', 90, '90',
                  'Von der positiven x-Achse zur positiven y-Achse gegen den Uhrzeigersinn: 90°. Probe: (cos 90°  −sin 90°; sin 90°  cos 90°) · (4 | 0) = (0 | 4).',
                  'Zeichne P und P′ ein.', einheit='°'),
            T('P(1 | −5) wird um O um 150° gedreht. Berechne x\''):
                Z(3, 'P(2 | 0) wird um O um einen Winkel φ zwischen 0° und 180° gedreht und landet bei P′(1 | y′) mit y′ > 0. Wie groß ist φ?', 60, '60',
                  'x′ = 2 · cos φ = 1 ⇒ cos φ = 0,5 ⇒ φ = 60°.', 'Schreibe x′ mit der Drehmatrix auf.', einheit='°'),
            T('Jemand berechnet für a = (2 | 2) und b = (6 | −3)'):
                Z(3, 'Für welches t > 0 schließen a = (1 | t) und b = (1 | 0) einen Winkel von 45° ein?', 1, '1',
                  'a · b = 1, |a| = √(1 + t²), |b| = 1. cos 45° = 1 : √(1 + t²) ⇒ √(1 + t²) = √2 ⇒ t² = 1 ⇒ t = 1.',
                  'Setze in cos φ = (a · b) : (|a| · |b|) ein.'),
            T('Jemand berechnet für a = (−1 | −2) und b = (−4 | −4)'):
                Z(3, 'Gegeben sind A(0 | 0), B(4 | 2) und C(1 | y). Für welches y hat das Dreieck ABC bei A einen rechten Winkel?', -2, '-4/2',
                  'AB = (4 | 2), AC = (1 | y). Senkrecht: 4 · 1 + 2 · y = 0 ⇒ y = −2.', 'Rechter Winkel bei A heißt: AB · AC = 0.'),
        },
        neu={
            'bildpunkt': [
                L(3, 'Die Punkte P(x | x + 1) werden mit M = (2  1; 0  1) abgebildet. Gib die Bildpunkte P′ in Abhängigkeit von x an.',
                  'P′(□ · x + □ | x + □)', [3, 1, 1], ['2 + 1', '1', '1'],
                  'x′ = 2x + 1 · (x + 1) = 3x + 1. y′ = 0 · x + 1 · (x + 1) = x + 1.', 'Rechne Zeile mal Spalte mit den Termen.'),
                Z(3, 'Für welchen Wert k bildet M = (1  0; 0  k) den Punkt P(4 | 3) auf P′(4 | −1,5) ab?', -0.5, '-1.5/3',
                  'y′ = k · 3 = −1,5 ⇒ k = −0,5. x bleibt 4.', 'Rechne y′ mit k aus.'),
                L(3, 'Welcher Punkt wird von M = (2  1; 1  1) auf sich selbst abgebildet?', 'P(□ | □)', [0, 0], ['0', '0'],
                  '2x + y = x ⇒ x + y = 0. x + y = y ⇒ x = 0. Dann y = 0. Nur der Ursprung.', 'Setze P′ = P und löse das Gleichungssystem.'),
                L(3, 'Eine Matrix bildet (1 | 0) auf (3 | 1) und (0 | 1) auf (−1 | 2) ab. Berechne das Bild von P(2 | 5).', 'P′(□ | □)', [1, 12], ['2*3 + 5*(-1)', '2*1 + 5*2'],
                  'P = 2 · (1 | 0) + 5 · (0 | 1). Bild: 2 · (3 | 1) + 5 · (−1 | 2) = (1 | 12).', 'Zerlege P in 2-mal (1 | 0) und 5-mal (0 | 1).'),
            ],
            'abbildungsmatrix': [
                Z(3, 'Die Matrix (k  0; 0  k) bildet P(2 | −3) auf P′(−5 | 7,5) ab. Wie groß ist k?', -2.5, '-5/2',
                  'x′ = k · 2 = −5 ⇒ k = −2,5. Probe: −2,5 · (−3) = 7,5. Zentrische Streckung an O mit k = −2,5.', 'Rechne mit der x-Koordinate.'),
                A(3, 'Die Punktspiegelung am Ursprung wird zweimal hintereinander ausgeführt. Was entsteht?', 'Jeder Punkt bleibt an seinem Platz.',
                  ['Eine Drehung um 90°', 'Eine Spiegelung an der x-Achse', 'Eine Streckung mit k = 2'],
                  '(−1  0; 0  −1) · (−1  0; 0  −1) = (1  0; 0  1). Jeder Punkt kommt zurück.', 'Wende die Abbildung zweimal auf einen Punkt an.'),
                L(3, 'Gib die Matrix an, die jeden Punkt an seinem Platz lässt.', MT, [1, 0, 0, 1], ['1', '0', '0', '1'],
                  '(1 | 0) bleibt (1 | 0), (0 | 1) bleibt (0 | 1). Spalten: (1 0; 0 1), die Einheitsmatrix.', 'Wohin gehen die Einheitspunkte?', hinweis=MH),
                L(3, 'Gib die Matrix der Spiegelung an der Geraden y = −x an.', MT, [0, -1, -1, 0], ['0', '-1', '-1', '0'],
                  '(1 | 0) wird zu (0 | −1), (0 | 1) wird zu (−1 | 0). Als Spalten: (0 −1; −1 0).', 'Spiegle die beiden Einheitspunkte an y = −x.', hinweis=MH),
                A(3, 'Welche Abbildung hat dieselbe Matrix wie die Drehung um O um 180°?', 'die Punktspiegelung am Ursprung',
                  ['die Spiegelung an der x-Achse', 'die Spiegelung an der y-Achse', 'die Spiegelung an y = x'],
                  'cos 180° = −1, sin 180° = 0: (−1  0; 0  −1). Das ist die Matrix der Punktspiegelung am Ursprung.', 'Setze 180° in die Drehmatrix ein.'),
            ],
            'drehung': [
                Z(3, 'Eine Drehung um O um 60° wird zweimal hintereinander ausgeführt. Um wie viel Grad wird insgesamt gedreht?', 120, '2*60',
                  'Zwei Drehungen um denselben Punkt ergeben eine Drehung um die Summe der Winkel: 120°.', 'Drehe einen Punkt in Gedanken zweimal.', einheit='°'),
                L(3, 'P(3 | 4) wird um O um 90° gedreht. Gib P′ exakt an.', 'P′(□ | □)', [-4, 3], ['-4', '3'],
                  'cos 90° = 0, sin 90° = 1: x′ = 0 · 3 − 1 · 4 = −4, y′ = 1 · 3 + 0 · 4 = 3.', 'Setze cos 90° = 0 und sin 90° = 1 ein.'),
                Z(3, 'Ein Quadrat mit dem Mittelpunkt O wird um O gedreht. Um welchen kleinsten Winkel (größer als 0°) muss man drehen, damit es wieder genau auf sich liegt?',
                  90, '360/4', 'Ein Quadrat hat vier gleiche Ecken. Nach 360° : 4 = 90° liegt jede Ecke auf der nächsten.', 'Wie viele Ecken hat ein Quadrat?', einheit='°'),
                L(3, 'P(6 | 8) wird so um O gedreht, dass das Bild auf der positiven x-Achse liegt. Gib P′ an.', 'P′(□ | □)', [10, 0], ['(6**2 + 8**2)/10', '0'],
                  'Die Drehung ändert den Abstand zu O nicht: √(36 + 64) = 10. Also P′(10 | 0).', 'Was bleibt bei einer Drehung um O gleich?'),
            ],
            'rechnen': [
                L(3, 'Die Drehung um O um 90° hat die Matrix D = (0  −1; 1  0). Berechne D · D.', MT, [-1, 0, 0, -1], ['0*0 + (-1)*1', '0', '0', '-1'],
                  'D · D = (0 · 0 + (−1) · 1   0 · (−1) + (−1) · 0; 1 · 0 + 0 · 1   1 · (−1) + 0 · 0) = (−1 0; 0 −1): eine Drehung um 180°.',
                  'Zeile mal Spalte – das Ergebnis ist eine bekannte Abbildung.', hinweis=MH),
                A(3, 'Für welche x gilt A · B = B · A mit A = (1  x; 0  1) und B = (1  2; 0  1)?', 'für jedes x', ['nur für x = 2', 'nur für x = 0', 'für kein x'],
                  'A · B = (1  2 + x; 0  1) und B · A = (1  x + 2; 0  1). Beide sind gleich – für jedes x.', 'Rechne beide Produkte mit x aus.'),
                L(3, 'Berechne A · A für A = (0  1; 1  0).', MT, [1, 0, 0, 1], ['1', '0', '0', '1'],
                  '(0 · 0 + 1 · 1   0 · 1 + 1 · 0; 1 · 0 + 0 · 1   1 · 1 + 0 · 0) = (1 0; 0 1). Zweimal an y = x spiegeln bringt jeden Punkt zurück.',
                  'Welche Abbildung ist A?', hinweis=MH),
            ],
            'inverse': [
                Z(3, 'Für welches x hat M = (x  2; 3  4) die Determinante 1?', 1.75, '(1 + 6)/4', '4x − 6 = 1 ⇒ x = 1,75.', 'Stelle die Determinante mit x auf.'),
                A(3, 'Ist die inverse Matrix der Drehung um O um 90° die Matrix der Drehung um 270°?', 'Ja: Beide zusammen ergeben eine volle Umdrehung.',
                  ['Nein, die Inverse einer Drehung gibt es nicht.', 'Nein, es ist die Drehung um 90° selbst.', 'Nein, es ist die Spiegelung an der x-Achse.'],
                  'Die Umkehrung macht die Drehung rückgängig: −90° = 270°. (0 −1; 1 0)⁻¹ = (0 1; −1 0) ist die Drehmatrix für 270°.',
                  'Was macht eine Drehung um 90° rückgängig?'),
            ],
            'skalarprodukt': [
                Z(3, 'Für zwei Vektoren gilt |a| = 5, |b| = 2 und a · b = 10. Wie groß ist der Winkel zwischen ihnen?', 0, '0',
                  'cos φ = 10 : (5 · 2) = 1 ⇒ φ = 0°. Die Vektoren zeigen in dieselbe Richtung.', 'Setze in die Winkelformel ein.', einheit='°'),
                L(3, 'Gib den Vektor an, der auf (3 | −2) senkrecht steht und die x-Koordinate 4 hat.', '(□ | □)', [4, 6], ['4', '3*4/2'],
                  '(3 | −2) · (4 | y) = 12 − 2y = 0 ⇒ y = 6.', 'Skalarprodukt gleich 0 setzen.'),
            ],
        })


# ---- STUFEN (Zwanzigste Runde, Zusatz RS/IB, Zweig stufen-rsib-1) ----
from _stufen_rsib1 import Stufen, stufen  # noqa: E402

ST = Stufen('abbildungen.matrizen', 20_101_9)
Z, A, L = ST.Z, ST.A, ST.L
_P = "P′(□ | □)"
_M = '(□  □; □  □)'

# bildpunkt
ST.stufenleiter('bildpunkt', 'Einen Punkt mit einer Matrix abbilden: Zeile mal Spalte; die richtige Rechnung erkennen.',
                'Urpunkt aus dem Bildpunkt, Matrix aus den Abbildungsgleichungen, Bild aus den Bildern der Einheitspunkte, zweimal abbilden, Spiel-Verzerrung.',
                'Parameter, Fixpunkt begründen, Fehler „Spalte statt Zeile“, Fläche des Bilds, Scherung als Modell, Abbilden und Verschieben rückwärts, Prüfungsaufgabe.')
ST.typ('bildpunkt', '/^(Bilde P|Welcher Bildpunkt)/', 'direkt')
ST.typ('bildpunkt', 'Die Abbildung mit M', 'umkehr')
ST.typ('bildpunkt', 'Die Abbildung hat die Gleichungen', 'darstellung')
ST.typ('bildpunkt', 'Eine Matrix bildet', 'mehrschritt')
ST.typ('bildpunkt', '/^(Die Punkte P\\(x|Für welchen Wert k)/', 'parameter')
ST.typ('bildpunkt', 'Welcher Punkt wird', 'begruenden')
ST.neu('bildpunkt', 'erkennen', A('Welche Rechnung liefert x′, wenn P(3 | 2) mit M = (4  1; 2  5) abgebildet wird?', '4 · 3 + 1 · 2', ['4 · 3 + 2 · 2', '4 · 2 + 1 · 3', '2 · 3 + 5 · 2'],
       'x′ = erste Zeile mal Punkt: 4 · 3 + 1 · 2 = 14. Die zweite Zeile liefert y′ = 2 · 3 + 5 · 2 = 16.', 'Welche Zeile gehört zu x′?'))
ST.neu('bildpunkt', 'einkleidung', L('Ein Computerspiel verzerrt Figuren mit M = (2  0; 0  1). Wohin kommt die Ecke (3 | 4) einer Figur?', '(□ | □)', [6, 4], ['2 * 3 + 0 * 4', '0 * 3 + 1 * 4'],
       'x′ = 2 · 3 + 0 · 4 = 6, y′ = 0 · 3 + 1 · 4 = 4. Die Figur wird nur in x-Richtung doppelt so breit.', 'Zeile mal Spalte.'))
ST.neu('bildpunkt', 'mehrschritt', L('Bilde P(1 | 2) mit M = (1  1; 0  1) ab und das Ergebnis noch einmal mit M.', "P″(□ | □)", [5, 2], ['(1 + 2) + 2', '2'],
       'Erst: (1 + 2 | 2) = (3 | 2). Dann: (3 + 2 | 2) = (5 | 2).', 'Bilde zweimal nacheinander ab.'))
ST.neu('bildpunkt', 'fehler', A('Jemand bildet P(2 | 1) mit M = (3  1; 0  2) ab und rechnet x′ = 3 · 2 + 0 · 1 = 6. Was stimmt?', 'Falsch: Er hat die Spalte statt der Zeile genommen; x′ = 3 · 2 + 1 · 1 = 7.',
       ['Richtig.', 'Falsch: x′ = 3 + 2 = 5.', 'Falsch: x′ = 3 · 1 + 1 · 2 = 5.'], 'Für x′ nimmt man die erste Zeile (3  1): 3 · 2 + 1 · 1 = 7. y′ = 0 · 2 + 2 · 1 = 2.', 'Welche Zahlen stehen in der ersten Zeile?'))
ST.neu('bildpunkt', 'verknuepfen', Z('Das Dreieck A(0 | 0), B(2 | 0), C(0 | 1) wird mit M = (3  0; 0  2) abgebildet. Wie groß ist die Fläche des Bilddreiecks?', 6, '6 * 2 / 2',
       'B′(6 | 0), C′(0 | 2). Rechtwinkliges Dreieck mit Katheten 6 und 2: ½ · 6 · 2 = 6 FE. Das Original hatte 1 FE – die Fläche wurde mit 3 · 2 = 6 multipliziert.', 'Bilde B und C ab.', einheit='FE'))
ST.neu('bildpunkt', 'transfer', Z('Die Matrix (1  k; 0  1) schiebt Punkte waagrecht, umso weiter, je höher sie liegen (Scherung). Wie weit wird der Punkt (0 | 5) bei k = 0,4 nach rechts geschoben?', 2, '0.4 * 5',
       'x′ = 1 · 0 + 0,4 · 5 = 2, y′ = 5. Der Punkt wandert 2 nach rechts.', 'Bilde (0 | 5) ab.'))
ST.neu('bildpunkt', 'rueckwaerts', L('Ein Punkt P wird erst mit M = (2  0; 0  3) abgebildet und dann um (1 | 1) verschoben. Er landet bei (9 | −5). Wo lag P?', 'P(□ | □)', [4, -2], ['(9 - 1) // 2', '(-5 - 1) // 3'],
       'Rückwärts: Verschiebung rückgängig: (8 | −6). Dann die Matrix rückgängig: x durch 2, y durch 3: (4 | −2).', 'Mache die Schritte in umgekehrter Reihenfolge rückgängig.'))
ST.neu('bildpunkt', 'pruefung', L('Gegeben ist M = (1  2; −1  3). a) Bilde A(2 | 1) ab. b) Bilde B(−1 | 2) ab.', "A′(□ | □); B′(□ | □)", [4, 1, 3, 7], ['2 + 2', '-2 + 3', '-1 + 4', '1 + 6'],
       'a) (1 · 2 + 2 · 1 | −1 · 2 + 3 · 1) = (4 | 1). b) (−1 + 4 | 1 + 6) = (3 | 7).', 'Zeile mal Spalte.'))
ST.knobel('bildpunkt', L('Die Matrix M = (0  1; 1  0) wird 2 025-mal hintereinander auf P(3 | 7) angewendet. Wo landet P?', 'P(□ | □)', [7, 3], ['7', '3'],
          'M vertauscht x und y. Zweimal angewendet ist alles wie vorher. 2 025 ist ungerade, also wirkt es wie einmal: (7 | 3).', 'Was passiert nach zwei Anwendungen?'))
ST.knobel('bildpunkt', A('Für welche Punkte P gilt bei M = (2  1; 1  2), dass das Bild P′ genau das Dreifache von P ist?', 'für alle Punkte der Form (t | t)', ['nur für (1 | 1)', 'für alle Punkte (t | −t)', 'für keinen Punkt außer (0 | 0)'],
          '(2x + y | x + 2y) = (3x | 3y) ⇒ y = x und x = y. Also alle Punkte (t | t) auf der Geraden y = x. Probe: (1 | 1) ↦ (3 | 3).', 'Stelle zwei Gleichungen auf.'))

# abbildungsmatrix
ST.stufenleiter('abbildungsmatrix', 'Mit gegebener Matrix spiegeln oder drehen; die Matrix einer Standardabbildung angeben und erkennen.',
                'Streckungen und Affinitäten als Matrix, Matrix aus den Bildern von (1 | 0) und (0 | 1), Faktor aus einem Punktpaar, Bildvergrößerung.',
                'Fehler „90° statt −90°“ und „falsche Spiegelachse“, Doppelte Abbildungen begründen, Spiegelung an y = −x herleiten, Flächenfaktor, Verkleinerung als Bedingung, Prüfungsaufgabe.')
ST.typ('abbildungsmatrix', 'Bilde P(', 'direkt')
ST.typ('abbildungsmatrix', 'Welche Matrix beschreibt', 'erkennen')
ST.typ('abbildungsmatrix', '/^Gib die Matrix der (Spiegelung an der y-Achse|Drehung|Punktspiegelung)/', 'direkt')
ST.typ('abbildungsmatrix', '/^Gib die Matrix der (zentrischen|orthogonalen)/', 'mehrschritt')
ST.typ('abbildungsmatrix', 'Gib die Matrix der Spiegelung an der Geraden', 'transfer')
ST.typ('abbildungsmatrix', 'Eine Abbildung bildet', 'darstellung')
ST.typ('abbildungsmatrix', '/^(Die Matrix \\(k|Gib die Matrix an, die jeden)/', 'umkehr')
ST.typ('abbildungsmatrix', 'Jemand gibt', 'fehler')
ST.typ('abbildungsmatrix', '/^(Die Punktspiegelung am Ursprung wird|Welche Abbildung hat)/', 'begruenden')
ST.neu('abbildungsmatrix', 'einkleidung', L('Ein Grafikprogramm vergrößert ein Bild in beide Richtungen auf das Dreifache (Mitte im Ursprung). Gib die Matrix an.', _M, [3, 0, 0, 3], ['3', '0', '0', '3'],
       '(1 | 0) wird zu (3 | 0), (0 | 1) zu (0 | 3). Als Spalten: (3  0; 0  3).', 'Wohin gehen (1 | 0) und (0 | 1)?'))
ST.neu('abbildungsmatrix', 'fehler', A('Jemand sagt: „Die Matrix (0  1; 1  0) beschreibt die Spiegelung an der x-Achse.“ Was stimmt?', 'Falsch: Sie vertauscht x und y – das ist die Spiegelung an der Geraden y = x.',
       ['Richtig.', 'Falsch: Das ist die Spiegelung an der y-Achse.', 'Falsch: Das ist die Drehung um 90°.'], '(0  1; 1  0) bildet (3 | 2) auf (2 | 3) ab. Die Spiegelung an der x-Achse hätte (1  0; 0  −1) und ergäbe (3 | −2).', 'Bilde einen Punkt ab.'))
ST.neu('abbildungsmatrix', 'parameter', A('Für welche Zahlen k verkleinert die Matrix (k  0; 0  k) jede Figur (k ≠ 0)?', 'für −1 < k < 1', ['für k < 1', 'für k > −1', 'für 0 < k < 2'],
       'Alle Längen werden mit |k| multipliziert. Kleiner wird die Figur, wenn |k| < 1, also −1 < k < 1. Negatives k dreht dabei zusätzlich um 180°.', 'Was macht ein negatives k?'))
ST.neu('abbildungsmatrix', 'verknuepfen', Z('Die Streckung mit der Matrix (2  0; 0  2) bildet ein Quadrat mit 3 FE ab. Wie groß ist das Bild?', 12, '3 * 4',
       'Alle Längen werden verdoppelt, die Fläche also mit 2 · 2 = 4 multipliziert: 12 FE.', 'Was passiert mit der Fläche, wenn alle Längen doppelt so lang werden?', einheit='FE'))
ST.neu('abbildungsmatrix', 'pruefung', L('Die Drehung um O um 90° gegen den Uhrzeigersinn: a) Wohin geht (1 | 0)? b) Wohin geht (0 | 1)? c) Gib die Matrix an.', 'a) (□ | □); b) (□ | □); c) (□  □; □  □)', [0, 1, -1, 0, 0, -1, 1, 0],
       ['0', '1', '-1', '0', '0', '-1', '1', '0'], 'a) (1 | 0) ↦ (0 | 1). b) (0 | 1) ↦ (−1 | 0). c) Bilder als Spalten: (0  −1; 1  0).', 'Zeichne die beiden Einheitspfeile und drehe sie.'))
ST.knobel('abbildungsmatrix', Z('Wie viele verschiedene Matrizen gibt es, in denen in jeder Zeile und jeder Spalte genau ein Eintrag 1 oder −1 steht und sonst 0?', 8, '2 * 2 * 2',
          'Die Nicht-Null-Einträge stehen entweder auf der Hauptdiagonale oder auf der Nebendiagonale (2 Möglichkeiten), und jeder kann 1 oder −1 sein (2 · 2). Zusammen 8. '
          'Das sind genau die Drehungen um 0°, 90°, 180°, 270° und die vier Spiegelungen, die ein Quadrat um O auf sich selbst abbilden.', 'Wo können die beiden Einträge stehen?'))
ST.knobel('abbildungsmatrix', L('Eine Abbildung bildet (1 | 1) auf (3 | 3) und (1 | −1) auf (1 | −1) ab. Gib ihre Matrix an.', _M, [2, 1, 1, 2], ['2', '1', '1', '2'],
          'M = (a  b; c  d). Aus (1 | 1): a + b = 3, c + d = 3. Aus (1 | −1): a − b = 1, c − d = −1. Also a = 2, b = 1, c = 1, d = 2.', 'Stelle für jede Zeile zwei Gleichungen auf.'))

# drehung
ST.stufenleiter('drehung', 'Einen Punkt auf der x-Achse mit der Drehmatrix drehen und x′ oder y′ berechnen; die Drehmatrix erkennen.',
                'Beliebige Punkte drehen, exakt um 90° drehen, Drehwinkel aus Bild und Urbild, Gondel eines Riesenrads.',
                'Abstand bleibt – begründen und nutzen, Winkel rückwärts aus einer Koordinate, Drehsymmetrie, Fehler beim Drehsinn, Bereich der Drehwinkel, Prüfungsaufgabe.')
ST.typ('drehung', '/^P\\(\\d+ \\| 0\\) wird um O um \\d+° gedreht\\. Berechne/', 'direkt')
ST.typ('drehung', 'Welche Matrix beschreibt', 'erkennen')
ST.typ('drehung', '/^P\\([−\\d]+ \\| [−\\d]+\\) wird um O um \\d+° gedreht\\. Berechne/', 'mehrschritt')
ST.typ('drehung', 'P(3 | 4) wird um O um 90°', 'mehrschritt')
ST.typ('drehung', 'P(4 | 0) wird um O gedreht', 'umkehr')
ST.typ('drehung', '/(Wie weit ist P. vom Ursprung|^P\\(6 \\| 8\\))/', 'verknuepfen')
ST.typ('drehung', 'P(2 | 0) wird um O um einen Winkel', 'rueckwaerts')
ST.typ('drehung', 'Eine Drehung um O um 60°', 'begruenden')
ST.typ('drehung', 'Ein Quadrat', 'transfer')
ST.neu('drehung', 'einkleidung', Z('Ein Riesenrad hat 10 m Radius, seine Mitte liegt im Ursprung. Eine Gondel startet bei (10 | 0) und dreht sich um 30° gegen den Uhrzeigersinn. Wie hoch über der Mitte ist sie dann?', 5, '10 * 0.5',
       'y′ = 10 · sin 30° + 0 · cos 30° = 10 · 0,5 = 5 m.', 'Berechne y′ mit der Drehmatrix.', einheit='m'))
ST.neu('drehung', 'fehler', A('Jemand dreht P(4 | 0) um O um 90° gegen den Uhrzeigersinn und erhält P′(0 | −4). Was stimmt?', 'Falsch: Gegen den Uhrzeigersinn landet P bei (0 | 4).',
       ['Richtig.', 'Falsch: P′(−4 | 0).', 'Falsch: P′(4 | 4).'], 'Mit (0  −1; 1  0): x′ = 0, y′ = 4. (0 | −4) wäre die Drehung im Uhrzeigersinn (−90°).', 'In welche Richtung dreht „gegen den Uhrzeigersinn“?'))
ST.neu('drehung', 'parameter', A('Für welche Drehwinkel φ mit 0° ≤ φ < 360° landet P(5 | 0) unterhalb der x-Achse?', 'für 180° < φ < 360°', ['für 0° < φ < 180°', 'für 90° < φ < 270°', 'für φ > 90°'],
       'y′ = 5 · sin φ. Das ist negativ für 180° < φ < 360°.', 'Wann ist sin φ negativ?'))
ST.neu('drehung', 'pruefung', L('P(2 | 0) wird um O um 60° gedreht. a) Berechne x′ (cos 60° = 0,5). b) Wie weit ist P′ vom Ursprung entfernt? c) Um wie viel Grad muss man noch weiterdrehen, bis P wieder bei (2 | 0) ist?',
       'a) □; b) □; c) □°', [1, 2, 300], ['2 * 0.5', '2', '360 - 60'], 'a) x′ = 2 · cos 60° = 1. b) Drehen ändert den Abstand nicht: 2. c) 360° − 60° = 300°.', 'Ein Kreis hat 360°.'))
ST.knobel('drehung', L('Ein regelmäßiges Sechseck mit dem Mittelpunkt O hat eine Ecke bei (4 | 0). Gib die gegenüberliegende Ecke an.', '(□ | □)', [-4, 0], ['-4', '0'],
          'Die gegenüberliegende Ecke erreicht man durch drei Drehungen um 60°, also um 180°: (4 | 0) ↦ (−4 | 0).', 'Um wie viel Grad liegen gegenüberliegende Ecken auseinander?'))
ST.knobel('drehung', Z('Ein Punkt wird immer wieder um 135° gedreht. Nach wie vielen Drehungen ist er zum ersten Mal wieder an seiner Stelle?', 8, '1080 // 135',
          'Gesucht ist das kleinste n mit n · 135° = Vielfaches von 360°. 135 · 8 = 1 080 = 3 · 360. Kleinere n gehen nicht (135 · 4 = 540 = 1,5 · 360). Also 8.', 'Wann ist n · 135 durch 360 teilbar?'))

# rechnen
ST.stufenleiter('rechnen', 'Matrizen addieren und mit einer Zahl multiplizieren; den Eintrag eines Produkts erkennen.',
                'Matrizen multiplizieren, fehlende Matrix bei einer Summe, Einkaufskosten als Matrix mal Vektor.',
                'Vertauschbarkeit prüfen, Verkettung von Abbildungen, Drehung zweimal, Parameter für AB = BA, Fehler „eintragsweise multipliziert“, Prüfungsaufgabe.')
ST.typ('rechnen', '/^Berechne (\\(−\\d\\)|\\d+) · A/', 'direkt')
ST.typ('rechnen', 'Berechne A + B', 'direkt')
ST.typ('rechnen', '/^(Berechne A · B|Was ergibt A · B|Berechne A · A)/', 'mehrschritt')
ST.typ('rechnen', '/^(Gilt A · B|Die Drehung um O um 90° hat)/', 'begruenden')
ST.typ('rechnen', 'Erst wird', 'verknuepfen')
ST.typ('rechnen', 'Für welche x gilt', 'parameter')
ST.neu('rechnen', 'erkennen', A('Welche Rechnung liefert den Eintrag oben links in A · B mit A = (1  2; 3  4) und B = (5  6; 7  8)?', '1 · 5 + 2 · 7 = 19', ['1 · 5 = 5', '1 · 5 + 3 · 6 = 23', '1 · 6 + 2 · 8 = 22'],
       'Oben links: erste Zeile von A mal erste Spalte von B: 1 · 5 + 2 · 7 = 19.', 'Zeile mal Spalte.'))
ST.neu('rechnen', 'einkleidung', L('Klasse A kauft 10 Hefte und 4 Stifte, Klasse B 6 Hefte und 8 Stifte. Ein Heft kostet 2 €, ein Stift 1 €. Berechne (10  4; 6  8) · (2 | 1): die Kosten beider Klassen.', 'A: □ €; B: □ €', [24, 20],
       ['10 * 2 + 4 * 1', '6 * 2 + 8 * 1'], 'Zeile mal Preise: A: 10 · 2 + 4 · 1 = 24 €. B: 6 · 2 + 8 · 1 = 20 €.', 'Jede Zeile gehört zu einer Klasse.'))
ST.neu('rechnen', 'umkehr', L('Ergänze: (2  1; 0  3) + X = (5  1; 2  3). Gib X an.', _M, [3, 0, 2, 0], ['5 - 2', '1 - 1', '2 - 0', '3 - 3'],
       'X = (5  1; 2  3) − (2  1; 0  3) = (3  0; 2  0), Eintrag für Eintrag.', 'Ziehe ab.'))
ST.neu('rechnen', 'fehler', A('Jemand rechnet (1  2; 3  4) · (1  0; 0  1), indem er nur Einträge an gleicher Stelle multipliziert: (1  0; 0  4). Was stimmt?',
       'Falsch: Zeile mal Spalte ergibt wieder (1  2; 3  4), denn (1  0; 0  1) ändert nichts.', ['Richtig.', 'Falsch: (2  2; 3  5).', 'Falsch: (1  2; 0  4).'],
       '(1  0; 0  1) ist die Einheitsmatrix. Zeile mal Spalte: oben links 1 · 1 + 2 · 0 = 1, oben rechts 1 · 0 + 2 · 1 = 2 usw. Ergebnis (1  2; 3  4).', 'Rechne einen Eintrag Zeile mal Spalte nach.'))
ST.neu('rechnen', 'pruefung', L('A = (1  2; 0  1), B = (3  0; 1  1). a) Berechne A + B. b) Berechne A · B.', 'a) (□  □; □  □); b) (□  □; □  □)', [4, 2, 1, 2, 5, 2, 1, 1],
       ['1 + 3', '2 + 0', '0 + 1', '1 + 1', '1 * 3 + 2 * 1', '1 * 0 + 2 * 1', '0 * 3 + 1 * 1', '0 * 0 + 1 * 1'],
       'a) Eintragsweise: (4  2; 1  2). b) Zeile mal Spalte: (1 · 3 + 2 · 1  1 · 0 + 2 · 1; 0 · 3 + 1 · 1  0 + 1) = (5  2; 1  1).', 'Addition eintragsweise, Multiplikation Zeile mal Spalte.'))
ST.knobel('rechnen', Z('A = (1  1; 0  1). Man multipliziert A zehnmal mit sich selbst (A¹⁰). Welche Zahl steht oben rechts?', 10, '10',
          'A · A = (1  2; 0  1), A³ = (1  3; 0  1). Jedes weitere A erhöht den Eintrag oben rechts um 1. Also A¹⁰ = (1  10; 0  1).', 'Rechne A², A³ und erkenne das Muster.'))
ST.knobel('rechnen', A('Welche Matrix X ist nicht die Nullmatrix, aber X · X ergibt die Nullmatrix (0  0; 0  0)?', '(0  1; 0  0)', ['(1  0; 0  0)', '(0  1; 1  0)', '(1  1; 1  1)'],
          '(0  1; 0  0) · (0  1; 0  0): oben links 0 · 0 + 1 · 0 = 0, oben rechts 0 · 1 + 1 · 0 = 0, unten beide 0. Bei Matrizen kann ein Produkt 0 sein, obwohl kein Faktor 0 ist.', 'Rechne jede Möglichkeit aus.'))

# inverse
ST.stufenleiter('inverse', 'Die Determinante einer Matrix berechnen; erkennen, wann es keine Inverse gibt.',
                'Inverse Matrix berechnen, Urpunkt mit der Inversen, einfacher Code entschlüsseln.',
                'Parameter ohne Inverse und mit Determinante 1, Drehung rückgängig begründen, Fehler beim Bilden der Inversen, Flächenfaktor, zweimal abgebildet rückwärts, Prüfungsaufgabe.')
ST.typ('inverse', 'Berechne die Determinante', 'direkt')
ST.typ('inverse', 'Berechne die inverse Matrix', 'mehrschritt')
ST.typ('inverse', '/^Für welches x hat M/', 'parameter')
ST.typ('inverse', '/Berechne P mit der inversen Matrix/', 'umkehr')
ST.typ('inverse', 'Hat M =', 'erkennen')
ST.typ('inverse', 'Ist die inverse Matrix', 'begruenden')
ST.neu('inverse', 'erkennen', A('Welche Matrix hat keine inverse Matrix?', '(2  4; 1  2)', ['(2  1; 1  2)', '(1  0; 0  1)', '(0  1; 1  0)'],
       'Determinante von (2  4; 1  2): 2 · 2 − 4 · 1 = 0. Ohne Determinante ≠ 0 gibt es keine Inverse. Die anderen haben 3, 1 und −1.', 'Berechne die Determinanten.'))
ST.neu('inverse', 'mehrschritt', L('Berechne M⁻¹ für M = (2  3; 1  2).', _M, [2, -3, -1, 2], ['2', '-3', '-1', '2'],
       'det M = 4 − 3 = 1. a und d tauschen, b und c mit Minus: (2  −3; −1  2), durch 1 geteilt.', 'Erst die Determinante.'))
ST.neu('inverse', 'einkleidung', L('Ein Code verschlüsselt Zahlenpaare mit M = (2  1; 1  1). Aus einem Paar (a | b) wurde (5 | 3). Wie lautete das Paar?', '(□ | □)', [2, 1], ['5 - 3', '-5 + 2 * 3'],
       'M⁻¹ = (1  −1; −1  2), da det M = 1. (1 · 5 − 1 · 3 | −1 · 5 + 2 · 3) = (2 | 1). Probe: (2 · 2 + 1 | 2 + 1) = (5 | 3).', 'Entschlüsseln heißt: mit der Inversen abbilden.'))
ST.neu('inverse', 'fehler', A('Jemand bildet die Inverse von (3  1; 2  1) so: a und d tauschen und vor alle Einträge ein Minus: (−1  −1; −2  −3). Was stimmt?', 'Falsch: Nur b und c bekommen ein Minus: (1  −1; −2  3), denn det = 1.',
       ['Richtig.', 'Falsch: (1  1; 2  3).', 'Falsch: (−3  −1; −2  −1).'], 'det = 3 − 2 = 1. Inverse: (d  −b; −c  a) : det = (1  −1; −2  3). Probe: (3  1; 2  1) · (1  −1; −2  3) = (1  0; 0  1).', 'Mach die Probe M · M⁻¹.'))
ST.neu('inverse', 'verknuepfen', Z('Ein Dreieck mit 5 FE wird mit M = (2  1; 1  3) abgebildet. Die Fläche wird dabei mit det M multipliziert. Wie groß ist das Bilddreieck?', 25, '5 * (2 * 3 - 1 * 1)',
       'det M = 2 · 3 − 1 · 1 = 5. Bildfläche 5 · 5 = 25 FE.', 'Berechne die Determinante.', einheit='FE'))
ST.neu('inverse', 'rueckwaerts', L('Ein Punkt wird mit M = (1  1; 0  2) abgebildet und das Ergebnis noch einmal mit M. Er landet bei (7 | 8). Wo lag er?', 'P(□ | □)', [1, 2], ['7 - 3 * 2', '8 // 4'],
       'M · M = (1  3; 0  4). Also x + 3y = 7 und 4y = 8 ⇒ y = 2, x = 1. Probe: (1 | 2) ↦ (3 | 4) ↦ (7 | 8).', 'Berechne zuerst M · M – oder rechne zweimal mit der Inversen zurück.'))
ST.neu('inverse', 'pruefung', L('M = (4  3; 1  1). a) Berechne det M. b) Gib M⁻¹ an. c) P′(10 | 3) ist das Bild von P. Berechne P.', 'a) □; b) (□  □; □  □); c) P(□ | □)', [1, 1, -3, -1, 4, 1, 2],
       ['4 - 3', '1', '-3', '-1', '4', '10 - 9', '-10 + 12'], 'a) 4 − 3 = 1. b) (1  −3; −1  4). c) (10 − 9 | −10 + 12) = (1 | 2).', 'Die Inverse bildet P′ zurück auf P.'))
ST.knobel('inverse', A('Für welche ganzen Zahlen a hat M = (a  2; 2  a) eine inverse Matrix, deren Einträge alle ganze Zahlen sind?', 'für kein a', ['für a = 3', 'für a = ±1', 'für alle a ≠ ±2'],
          'M⁻¹ = (a  −2; −2  a) : (a² − 4). Damit −2 : (a² − 4) ganz ist, muss a² − 4 einer der Werte ±1 oder ±2 sein, also a² = 5, 3, 6 oder 2. Keine davon ist eine Quadratzahl. Für a = ±2 gibt es gar keine Inverse.',
          'Wann ist 2 : (a² − 4) eine ganze Zahl?'))
ST.knobel('inverse', L('M = (0  1; −1  0) beschreibt eine Drehung. Gib M⁻¹ an, ohne die Formel zu benutzen.', _M, [0, -1, 1, 0], ['0', '-1', '1', '0'],
          'M bildet (1 | 0) auf (0 | −1) ab: Drehung um −90°. Rückgängig macht das die Drehung um +90° mit der Matrix (0  −1; 1  0). Probe: M · M⁻¹ = (1  0; 0  1).', 'Welche Drehung ist M? Was macht sie rückgängig?'))

# skalarprodukt
ST.stufenleiter('skalarprodukt', 'Das Skalarprodukt zweier Vektoren berechnen und damit „senkrecht“ erkennen.',
                'Parameter für senkrecht, Winkel aus dem Skalarprodukt, Betrag eines Vektors, Arbeit einer Kraft.',
                'Fehler „Vektor statt Zahl“, rechter Winkel im Dreieck, Winkel aus Beträgen, senkrechter Vektor mit Vorgabe, Vorzeichen deuten, Prüfungsaufgabe.')
ST.typ('skalarprodukt', 'Berechne das Skalarprodukt', 'direkt')
ST.typ('skalarprodukt', 'Stehen a', 'erkennen')
ST.typ('skalarprodukt', 'Für welches t stehen', 'umkehr')
ST.typ('skalarprodukt', 'Berechne den Winkel', 'mehrschritt')
ST.typ('skalarprodukt', 'Jemand berechnet', 'fehler')
ST.typ('skalarprodukt', '/^(Für welches t > 0|Gib den Vektor an)/', 'parameter')
ST.typ('skalarprodukt', 'Gegeben sind A(0', 'verknuepfen')
ST.typ('skalarprodukt', 'Für zwei Vektoren gilt', 'rueckwaerts')
ST.neu('skalarprodukt', 'einkleidung', Z('Eine Kraft F = (3 | 4) (in N) zieht einen Wagen den Weg s = (10 | 0) (in m). Die Arbeit ist das Skalarprodukt F · s (in J). Wie groß ist sie?', 30, '3 * 10 + 4 * 0',
       'F · s = 3 · 10 + 4 · 0 = 30 J. Nur der Teil der Kraft in Wegrichtung zählt.', 'Skalarprodukt ausrechnen.', einheit='J'))
ST.neu('skalarprodukt', 'mehrschritt', Z('Berechne den Betrag (die Länge) von a = (6 | 8).', 10, '10', '|a| = √(6² + 8²) = √100 = 10.', 'Satz des Pythagoras.'))
ST.neu('skalarprodukt', 'begruenden', A('Stimmt: Ist das Skalarprodukt zweier Vektoren negativ, ist der Winkel zwischen ihnen größer als 90°?', 'Ja: a · b = |a| · |b| · cos φ, und cos φ ist dann negativ.',
       ['Nein, dann sind sie senkrecht.', 'Nein, dann ist der Winkel kleiner als 90°.', 'Das hat mit dem Winkel nichts zu tun.'],
       'Die Beträge sind positiv. Das Vorzeichen kommt nur von cos φ, und cos φ < 0 für 90° < φ ≤ 180°.', 'Woher kommt das Vorzeichen?'))
ST.neu('skalarprodukt', 'pruefung', L('a = (2 | 1), b = (−1 | 2), c = (3 | 4). a) Berechne a · b. b) Berechne a · c. c) Welcher Vektor steht senkrecht auf a? (1 = b, 2 = c)', 'a) □; b) □; c) □', [0, 10, 1],
       ['2 * (-1) + 1 * 2', '2 * 3 + 1 * 4', '1'], 'a) −2 + 2 = 0. b) 6 + 4 = 10. c) b, weil a · b = 0.', 'Senkrecht heißt Skalarprodukt 0.'))
ST.knobel('skalarprodukt', Z('Wie viele Vektoren (x | y) ≠ (0 | 0) mit ganzen Zahlen x, y zwischen −3 und 3 stehen senkrecht auf (1 | 2)?', 2, '2',
          'x + 2y = 0 ⇒ x = −2y. y = 1 gibt (−2 | 1), y = −1 gibt (2 | −1). Für |y| ≥ 2 wäre |x| ≥ 4 – zu groß. y = 0 gibt den Nullvektor. Also 2.', 'Stelle die Bedingung als Gleichung auf.'))
ST.knobel('skalarprodukt', Z('a = (2 | 1). Für welche Zahl x gilt für b = (x | 0): a · b = |a|²?', 2.5, '5 / 2',
          '|a|² = 2² + 1² = 5. a · b = 2 · x + 1 · 0 = 2x. Also 2x = 5 ⇒ x = 2,5. Probe: (2 | 1) · (2,5 | 0) = 5.', 'Berechne beide Seiten.'))


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
    durchsicht(d)
    stufen('abbildungen.matrizen', ST)
