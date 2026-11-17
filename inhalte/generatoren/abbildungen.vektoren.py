#!/usr/bin/env python3
"""Thema abbildungen.vektoren – Vektoren und Parallelverschiebung (Realschule Bayern, Klasse 7, WPF I)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _rs import *  # noqa: E402,F403

start(4801)
LV = 'Vektor = (□ | □)'
HV = 'x-Koordinate, y-Koordinate'


def nz(n, lo=1):
    return R.choice([i for i in range(-n, n + 1) if abs(i) >= lo])


def pz(g=6):
    return (R.randint(-g, g), R.randint(-g, g))


def vz(g=6):
    while True:
        v = (R.randint(-g, g), R.randint(-g, g))
        if v != (0, 0): return v


def add(p, v, k=1):
    return (p[0] + k * v[0], p[1] + k * v[1])


def ab(p, q):
    return (q[0] - p[0], q[1] - p[1])


def bild2(p, q, np_, nq, pfeil=True):
    xs, ys = [p[0], q[0], 0], [p[1], q[1], 0]
    return {'typ': 'koordinaten', 'x': [min(xs) - 1, max(xs) + 1], 'y': [min(ys) - 1, max(ys) + 1], 'schritt_x': 1, 'schritt_y': 1,
            'punkte': [{'x': p[0], 'y': p[1], 'name': np_}, {'x': q[0], 'y': q[1], 'name': nq}],
            'strecken': [[p[0], p[1], q[0], q[1]] + ([] if pfeil else ['gestrichelt'])]}


ETAPPEN = [
    {'lernziel': 'vektor_bestimmen', 'titel': 'Einen Vektor aus zwei Punkten',
     'regel': 'Ein ⟦Vektor⟧ beschreibt eine Verschiebung: so viel nach rechts (x) und so viel nach oben (y). Vom Punkt A zum Punkt B gilt: ⟦Vektor AB = (x_B − x_A | y_B − y_A)⟧ – „Spitze minus Fuß“. Wie bei einer Wegbeschreibung: „4 Schritte nach rechts, 3 nach oben.“',
     'bild': {'typ': 'koordinaten', 'x': [-1, 6], 'y': [-1, 5], 'schritt_x': 1, 'schritt_y': 1,
              'punkte': [{'x': 1, 'y': 1, 'name': 'A'}, {'x': 5, 'y': 4, 'name': 'B'}],
              'strecken': [[1, 1, 5, 4], [1, 1, 5, 1, 'gestrichelt'], [5, 1, 5, 4, 'gestrichelt']]},
     'schritte': ['A(1 | 1), B(5 | 4): x: 5 − 1 = 4, y: 4 − 1 = 3.', 'Also ⟦Vektor AB = (4 | 3)⟧: 4 nach rechts, 3 nach oben.'],
     'probe': 'A + Vektor: (1 + 4 | 1 + 3) = (5 | 4) = B ✓',
     'fehler': 'Fuß minus Spitze, also (1 − 5 | 1 − 4) = (−4 | −3), ist falsch: Das ist der Vektor ⟦BA⟧, er zeigt in die ⟦Gegenrichtung⟧.'},
    {'lernziel': 'bildpunkt', 'titel': 'Punkte verschieben',
     'regel': 'Bei einer ⟦Parallelverschiebung⟧ mit dem Vektor v = (v_x | v_y) wird jeder Punkt gleich weit und in die gleiche Richtung verschoben: ⟦P\' = (x + v_x | y + v_y)⟧. Wie ein Schiebepuzzle: Alle Teile rutschen gemeinsam.',
     'bild': {'typ': 'koordinaten', 'x': [-3, 4], 'y': [-2, 5], 'schritt_x': 1, 'schritt_y': 1,
              'punkte': [{'x': -2, 'y': 3, 'name': 'P'}, {'x': 3, 'y': 1, 'name': "P'"}], 'strecken': [[-2, 3, 3, 1]]},
     'schritte': ["P(−2 | 3) mit v = (5 | −2): x: −2 + 5 = 3, y: 3 + (−2) = 1.", "Bildpunkt ⟦P'(3 | 1)⟧."],
     'probe': "Vektor PP' = (3 − (−2) | 1 − 3) = (5 | −2) = v ✓",
     'fehler': "3 + (−2) = 5 ist falsch: Eine negative y-Koordinate im Vektor heißt ⟦nach unten⟧ – es wird kleiner: 3 + (−2) = 1."},
    {'lernziel': 'gegenvektor', 'titel': 'Gegenvektor und Rückweg',
     'regel': 'Der ⟦Gegenvektor⟧ von v = (a | b) ist ⟦−v = (−a | −b)⟧: gleich lang, entgegengesetzte Richtung. Die ⟦Umkehrabbildung⟧ einer Verschiebung ist die Verschiebung mit dem Gegenvektor – sie bringt jeden Bildpunkt zurück auf seinen Urpunkt: ⟦P = P\' − v⟧.',
     'schritte': ["v = (4 | −3), P'(1 | 2). Gegenvektor: −v = (−4 | 3).", "Urpunkt: P = (1 + (−4) | 2 + 3) = ⟦P(−3 | 5)⟧."],
     'probe': "P(−3 | 5) + v: (−3 + 4 | 5 − 3) = (1 | 2) = P' ✓",
     'fehler': "Zum Bildpunkt nochmal v addieren, also (1 + 4 | 2 − 3) = (5 | −1), ist falsch: Damit schiebst du ⟦weiter⟧ statt zurück. Für den Rückweg brauchst du den ⟦Gegenvektor⟧."},
    {'lernziel': 'addition', 'titel': 'Vektoren addieren',
     'regel': 'Zwei Verschiebungen nacheinander ergeben ⟦eine einzige Verschiebung⟧: ⟦(a | b) + (c | d) = (a + c | b + d)⟧. Bei einer Vektorkette gilt: ⟦Vektor AB + Vektor BC = Vektor AC⟧ – wie zwei Etappen einer Wanderung.',
     'schritte': ['v₁ = (3 | −1), v₂ = (−5 | 4).', 'v₁ + v₂ = (3 + (−5) | −1 + 4) = ⟦(−2 | 3)⟧.'],
     'probe': 'Erst 3 nach rechts, dann 5 nach links: insgesamt 2 nach links ✓',
     'fehler': 'Kreuzweise addieren, also (3 + 4 | −1 + (−5)), ist falsch: Es wird ⟦x mit x⟧ und ⟦y mit y⟧ addiert.'},
    {'lernziel': 'punkt_berechnen', 'titel': 'Punkte mit Vektoren berechnen',
     'regel': 'Mit Vektoren findest du fehlende Punkte ohne Zeichnung. Im ⟦Parallelogramm ABCD⟧ gilt ⟦Vektor AD = Vektor BC⟧ (gleich lang und gleich gerichtet). Also: ⟦D = A + Vektor BC⟧.',
     'bild': {'typ': 'koordinaten', 'x': [-1, 7], 'y': [-1, 5], 'schritt_x': 1, 'schritt_y': 1,
              'punkte': [{'x': 0, 'y': 0, 'name': 'A'}, {'x': 4, 'y': 1, 'name': 'B'}, {'x': 6, 'y': 4, 'name': 'C'}, {'x': 2, 'y': 3, 'name': 'D'}],
              'strecken': [[0, 0, 4, 1], [4, 1, 6, 4], [6, 4, 2, 3, 'gestrichelt'], [2, 3, 0, 0, 'gestrichelt']]},
     'schritte': ['A(0 | 0), B(4 | 1), C(6 | 4). Vektor BC = (6 − 4 | 4 − 1) = (2 | 3).', 'D = A + Vektor BC = (0 + 2 | 0 + 3) = ⟦D(2 | 3)⟧.'],
     'probe': 'Vektor DC = (6 − 2 | 4 − 3) = (4 | 1) = Vektor AB ✓',
     'fehler': 'D = B + Vektor AC zu rechnen ist falsch: Das liefert einen Punkt ⟦außerhalb⟧ des Parallelogramms. Die Ecken laufen der Reihe nach A, B, C, D – D liegt ⟦gegenüber von B⟧.'},
    {'lernziel': 'eigenschaften', 'titel': 'Was bleibt bei der Verschiebung?',
     'regel': 'Die Parallelverschiebung ist eine ⟦Kongruenzabbildung⟧: Bild und Urbild sind ⟦deckungsgleich⟧. Sie ist ⟦längentreu, winkeltreu, flächentreu⟧, jede Strecke bleibt ⟦parallel⟧ zu ihrem Bild, und der Umlaufsinn bleibt gleich.',
     'schritte': ["Dreieck ABC mit AB = 5 cm, Winkel α = 40°, Fläche 6 cm² wird mit v = (3 | 2) verschoben.",
                  "Dann gilt: A'B' = ⟦5 cm⟧, α' = ⟦40°⟧, Fläche ⟦6 cm²⟧, und A'B' ist parallel zu AB."],
     'fehler': '„Weil das Dreieck nach oben verschoben wird, wird es größer“ ist falsch: Eine Verschiebung ändert nur die ⟦Lage⟧, nie die Größe oder Form.'},
]


# ---------- Generatoren ----------
def g_vektor_bestimmen(s):
    if s == 1:
        A = (R.randint(0, 5), R.randint(0, 5))
        B = (R.randint(0, 8), R.randint(0, 8))
        if A == B: return None
        v = ab(A, B)
        a = luecken(f'Berechne den Vektor AB für {pkt("A", *A)} und {pkt("B", *B)}.', 'Vektor AB = (□ | □)', HV, v,
                    f'Spitze minus Fuß: ({dz(B[0])} − {dz(A[0])} | {dz(B[1])} − {dz(A[1])}) = {vek(*v)}.',
                    'Rechne für x und y getrennt: Koordinate von B minus Koordinate von A.', c=[f'{B[0]} - {A[0]}', f'{B[1]} - {A[1]}'])
        return bild(a, bild2(A, B, 'A', 'B')) if R.random() < 0.3 else a
    A, B = pz(7), pz(7)
    if A == B or A[0] * A[1] >= 0 and R.random() < 0.5: return None
    v = ab(A, B)
    w = f'Spitze minus Fuß: ({dz(B[0])} − {kl(A[0])} | {dz(B[1])} − {kl(A[1])}) = {vek(*v)}.'
    if s == 2:
        n1, n2 = R.choice([('A', 'B'), ('P', 'Q'), ('C', 'D'), ('R', 'S')])
        return luecken(f'Berechne den Vektor {n1}{n2} für {pkt(n1, *A)} und {pkt(n2, *B)}.', f'Vektor {n1}{n2} = (□ | □)', HV, v,
                       w.replace('Spitze', 'Spitze').replace('A', n1), 'Spitze minus Fuß. Minus einer negativen Zahl wird plus.',
                       c=[f'({B[0]}) - ({A[0]})', f'({B[1]}) - ({A[1]})'])
    art = R.random()
    if art < 0.4:
        return auswahl(f'Welcher Vektor führt von {pkt("A", *A)} nach {pkt("B", *B)}?', vek(*v),
                       [vek(-v[0], -v[1]), vek(B[0] + A[0], B[1] + A[1]), vek(v[1], v[0])], w,
                       'Von A nach B: Spitze B minus Fuß A.')
    if art < 0.7:
        a = luecken('Lies den Vektor PQ aus der Zeichnung ab.', 'Vektor PQ = (□ | □)', HV, v,
                    f'P{vek(*A)[0:]} und Q{vek(*B)}: ' + w.replace('Spitze minus Fuß: ', ''),
                    'Lies die Koordinaten von P und Q ab und rechne Q minus P.', c=[f'({B[0]}) - ({A[0]})', f'({B[1]}) - ({A[1]})'])
        return bild(a, bild2(A, B, 'P', 'Q'))
    # Umkehr: Vektor AB und B gegeben -> A
    return luecken(f'Es gilt Vektor AB = {vek(*v)} und {pkt("B", *B)}. Berechne den Fußpunkt A.', 'A(□ | □)', HV, A,
                   f'B = A + Vektor AB, also A = B − Vektor AB = ({dz(B[0])} − {kl(v[0])} | {dz(B[1])} − {kl(v[1])}) = {vek(*A)}.',
                   'Von B aus musst du den Vektor rückwärts gehen.', c=[f'({B[0]}) - ({v[0]})', f'({B[1]}) - ({v[1]})'])


def g_bildpunkt(s):
    L, H = "P'(□ | □)", 'Trage die x- und die y-Koordinate des Bildpunkts ein.'
    if s == 1:
        P, v = (R.randint(0, 6), R.randint(0, 6)), (R.randint(1, 5), R.randint(1, 5))
        Q = add(P, v)
        return luecken(f'Verschiebe {pkt("P", *P)} mit dem Vektor v = {vek(*v)}.', L, H, Q,
                       f"x: {dz(P[0])} + {dz(v[0])} = {dz(Q[0])}, y: {dz(P[1])} + {dz(v[1])} = {dz(Q[1])}. P'{vek(*Q)}.",
                       'Addiere die x-Koordinaten und die y-Koordinaten getrennt.', c=[f'{P[0]} + {v[0]}', f'{P[1]} + {v[1]}'])
    P, v = pz(7), vz(7)
    if 0 in v and R.random() < 0.7: return None
    Q = add(P, v)
    w = f"x: {dz(P[0])} + {kl(v[0])} = {dz(Q[0])}, y: {dz(P[1])} + {kl(v[1])} = {dz(Q[1])}. P'{vek(*Q)}."
    if s == 2:
        a = luecken(f'Verschiebe {pkt("P", *P)} mit dem Vektor v = {vek(*v)}.', L, H, Q, w,
                    'Negative Koordinaten im Vektor heißen: nach links bzw. nach unten.', c=[f'({P[0]}) + ({v[0]})', f'({P[1]}) + ({v[1]})'])
        return a
    art = R.random()
    if art < 0.45:
        # Dreieck: A und A' bekannt, B' gesucht
        A, B = pz(5), pz(5)
        if A == B: return None
        A2 = add(A, v)
        B2 = add(B, v)
        return luecken(f"Ein Dreieck ABC wird verschoben. {pkt('A', *A)} hat den Bildpunkt {pkt(chr(65) + chr(39), *A2)}. Berechne das Bild von {pkt('B', *B)}.",
                       "B'(□ | □)", 'x-Koordinate, y-Koordinate', B2,
                       f"Verschiebungsvektor v = Vektor AA' = {vek(*v)}. B' = ({dz(B[0])} + {kl(v[0])} | {dz(B[1])} + {kl(v[1])}) = {vek(*B2)}.",
                       "Bestimme zuerst den Verschiebungsvektor aus A und A'.", c=[f'({B[0]}) + ({A2[0]}) - ({A[0]})', f'({B[1]}) + ({A2[1]}) - ({A[1]})'])
    if art < 0.75:
        falsch1 = vek(P[0] + v[1], P[1] + v[0])
        falsch2 = vek(P[0] - v[0], P[1] - v[1])
        falsch3 = vek(P[0] + v[0], P[1] - v[1])
        return auswahl(f'Wohin kommt {pkt("P", *P)} bei der Verschiebung mit v = {vek(*v)}?', "P'" + vek(*Q),
                       ["P'" + falsch1, "P'" + falsch2, "P'" + falsch3], w, 'x zu x, y zu y – und auf die Vorzeichen achten.')
    k = R.choice([2, 3])
    Q = add(P, v, k)
    return luecken(f'{pkt("P", *P)} wird {k}-mal hintereinander mit v = {vek(*v)} verschoben. Wo landet P?', L, H, Q,
                   f'{k}-mal v ist ({k} · {kl(v[0])} | {k} · {kl(v[1])}) = {vek(k * v[0], k * v[1])}. P\' = {vek(*Q)}.',
                   f'{k} gleiche Verschiebungen ergeben den {k}-fachen Vektor.', c=[f'({P[0]}) + {k} * ({v[0]})', f'({P[1]}) + {k} * ({v[1]})'])


def g_gegenvektor(s):
    if s == 1:
        v = vz(9)
        return luecken(f'Gib den Gegenvektor zu v = {vek(*v)} an.', '−v = (□ | □)', HV, (-v[0], -v[1]),
                       f'Beide Koordinaten bekommen das andere Vorzeichen: −v = {vek(-v[0], -v[1])}.',
                       'Gleich lang, aber genau entgegengesetzt.', c=[f'-({v[0]})', f'-({v[1]})'])
    v, P = vz(7), pz(6)
    Q = add(P, v)
    w = f"Gegenvektor −v = {vek(-v[0], -v[1])}. P = ({dz(Q[0])} + {kl(-v[0])} | {dz(Q[1])} + {kl(-v[1])}) = {vek(*P)}."
    if s == 2:
        return luecken(f"Bei der Verschiebung mit v = {vek(*v)} entsteht der Bildpunkt {pkt(chr(80) + chr(39), *Q)}. Berechne den Urpunkt P.",
                       'P(□ | □)', HV, P, w, 'Gehe mit dem Gegenvektor zurück.', c=[f'({Q[0]}) - ({v[0]})', f'({Q[1]}) - ({v[1]})'])
    art = R.random()
    if art < 0.4:
        return auswahl(f"Bei einer Verschiebung mit v = {vek(*v)} ist {pkt(chr(80) + chr(39), *Q)} der Bildpunkt. Wo lag P?",
                       'P' + vek(*P), ['P' + vek(Q[0] + v[0], Q[1] + v[1]), 'P' + vek(-Q[0], -Q[1]), 'P' + vek(Q[0] - v[0], Q[1] + v[1])],
                       w, 'Nicht weiter schieben, sondern zurück: Gegenvektor.')
    if art < 0.7:
        return auswahl(f'Mit welchem Vektor macht man die Verschiebung mit v = {vek(*v)} wieder rückgängig?', vek(-v[0], -v[1]),
                       [vek(*v), vek(v[1], v[0]), vek(-v[0], v[1])],
                       f'Die Umkehrabbildung ist die Verschiebung mit dem Gegenvektor −v = {vek(-v[0], -v[1])}.',
                       'Welcher Vektor führt genau zurück?')
    # Hin- und Rückweg: P mit v, dann mit w verschoben -> wieder P? Welcher Vektor w fehlt noch zum Start?
    v2 = vz(6)
    S = add(add(P, v), v2)
    r = (P[0] - S[0], P[1] - S[1])
    return luecken(f'Ein Roboter fährt von {pkt("P", *P)} erst um {vek(*v)}, dann um {vek(*v2)}. Mit welchem Vektor kommt er auf direktem Weg zurück nach P?',
                   'Vektor = (□ | □)', HV, r,
                   f'Gesamtweg: {vek(*v)} + {vek(*v2)} = {vek(v[0] + v2[0], v[1] + v2[1])}. Zurück: Gegenvektor {vek(*r)}.',
                   'Fasse beide Fahrten zu einem Vektor zusammen und nimm dann den Gegenvektor.', c=[f'-(({v[0]}) + ({v2[0]}))', f'-(({v[1]}) + ({v2[1]}))'])


def g_addition(s):
    if s == 1:
        a, b = (R.randint(0, 7), R.randint(0, 7)), (R.randint(0, 7), R.randint(0, 7))
        if a == (0, 0) or b == (0, 0): return None
        return luecken(f'Berechne {vek(*a)} + {vek(*b)}.', '(□ | □)', HV, (a[0] + b[0], a[1] + b[1]),
                       f'x: {dz(a[0])} + {dz(b[0])} = {dz(a[0] + b[0])}, y: {dz(a[1])} + {dz(b[1])} = {dz(a[1] + b[1])}.',
                       'x mit x, y mit y.', c=[f'{a[0]} + {b[0]}', f'{a[1]} + {b[1]}'])
    a, b = vz(8), vz(8)
    sm = (a[0] + b[0], a[1] + b[1])
    w = f'x: {dz(a[0])} + {kl(b[0])} = {dz(sm[0])}, y: {dz(a[1])} + {kl(b[1])} = {dz(sm[1])}. Summe {vek(*sm)}.'
    if s == 2:
        if R.random() < 0.5:
            return luecken(f'Berechne {vek(*a)} + {vek(*b)}.', '(□ | □)', HV, sm, w, 'Addiere getrennt; negative Zahlen in Klammern.',
                           c=[f'({a[0]}) + ({b[0]})', f'({a[1]}) + ({b[1]})'])
        return luecken(f'Es gilt Vektor AB = {vek(*a)} und Vektor BC = {vek(*b)}. Berechne Vektor AC.', 'Vektor AC = (□ | □)', HV, sm,
                       'Vektorkette: Vektor AC = Vektor AB + Vektor BC. ' + w, 'Von A über B nach C: die Vektoren hintereinander.',
                       c=[f'({a[0]}) + ({b[0]})', f'({a[1]}) + ({b[1]})'])
    art = R.random()
    if art < 0.35:
        c3 = vz(6)
        t = (sm[0] + c3[0], sm[1] + c3[1])
        return luecken(f'Eine Figur wird nacheinander mit {vek(*a)}, {vek(*b)} und {vek(*c3)} verschoben. Durch welche einzige Verschiebung erreicht man dasselbe?',
                       'Vektor = (□ | □)', HV, t, f'Alle drei addieren: ({dz(a[0])} + {kl(b[0])} + {kl(c3[0])} | {dz(a[1])} + {kl(b[1])} + {kl(c3[1])}) = {vek(*t)}.',
                       'Nacheinander verschieben heißt Vektoren addieren.', c=[f'({a[0]}) + ({b[0]}) + ({c3[0]})', f'({a[1]}) + ({b[1]}) + ({c3[1]})'])
    if art < 0.7:
        return luecken(f'Ergänze: {vek(*a)} + v = {vek(*sm)}.', 'v = (□ | □)', HV, b,
                       f'v = {vek(*sm)} − {vek(*a)} = ({dz(sm[0])} − {kl(a[0])} | {dz(sm[1])} − {kl(a[1])}) = {vek(*b)}.',
                       'Welcher Vektor fehlt noch? Rechne Ergebnis minus bekannten Vektor.', c=[f'({sm[0]}) - ({a[0]})', f'({sm[1]}) - ({a[1]})'])
    return auswahl(f'Welche Summe stimmt für {vek(*a)} + {vek(*b)}?', vek(*sm),
                   [vek(a[0] + b[1], a[1] + b[0]), vek(a[0] - b[0], a[1] - b[1]), vek(a[0] * b[0], a[1] * b[1])], w,
                   'Addiert wird x mit x und y mit y.')


def g_punkt_berechnen(s):
    while True:
        A = pz(5)
        u, v = vz(5), vz(5)
        if det(u, v) > 0: break
    B, D = add(A, u), add(A, v)
    C = add(B, v)
    if s == 1:
        A = (0, 0)
        u, v = (R.randint(2, 6), R.randint(0, 2)), (R.randint(0, 3), R.randint(2, 6))
        B, D = u, v
        C = add(u, v)
        return luecken(f'Im Parallelogramm ABCD ist {pkt("A", *A)}, Vektor AB = {vek(*u)} und Vektor AD = {vek(*v)}. Berechne C.', 'C(□ | □)', HV, C,
                       f'C = A + Vektor AB + Vektor AD = (0 + {dz(u[0])} + {dz(v[0])} | 0 + {dz(u[1])} + {dz(v[1])}) = {vek(*C)}.',
                       'Von A aus erst AB entlang, dann ein Stück wie AD.', c=[f'{u[0]} + {v[0]}', f'{u[1]} + {v[1]}'])
    if s == 2:
        a = luecken(f'Im Parallelogramm ABCD sind {pkt("A", *A)}, {pkt("B", *B)} und {pkt("C", *C)} gegeben. Berechne D.', 'D(□ | □)', HV, D,
                    f'Vektor BC = {vek(*v)}. D = A + Vektor BC = ({dz(A[0])} + {kl(v[0])} | {dz(A[1])} + {kl(v[1])}) = {vek(*D)}.',
                    'Im Parallelogramm ist Vektor AD = Vektor BC.', c=[f'({A[0]}) + ({C[0]}) - ({B[0]})', f'({A[1]}) + ({C[1]}) - ({B[1]})'])
        return bild(a, koord_bild([A, B, C], ['A', 'B', 'C'], geschlossen=False)) if R.random() < 0.4 else a
    art = R.random()
    if art < 0.35:
        return luecken(f'Im Parallelogramm ABCD sind {pkt("A", *A)}, {pkt("C", *C)} und {pkt("D", *D)} gegeben. Berechne B.', 'B(□ | □)', HV, B,
                       f'Vektor DC = {vek(*u)} = Vektor AB. B = A + Vektor DC = ({dz(A[0])} + {kl(u[0])} | {dz(A[1])} + {kl(u[1])}) = {vek(*B)}.',
                       'Welche Seite ist parallel und gleich lang wie AB?', c=[f'({A[0]}) + ({C[0]}) - ({D[0]})', f'({A[1]}) + ({C[1]}) - ({D[1]})'])
    if art < 0.65:
        f1, f2, f3 = add(B, ab(A, C)), add(C, ab(B, A)), add(A, ab(C, B))
        return auswahl(f'Im Parallelogramm ABCD sind {pkt("A", *A)}, {pkt("B", *B)} und {pkt("C", *C)} gegeben. Wo liegt D?', 'D' + vek(*D),
                       ['D' + vek(*f1), 'D' + vek(*f3), 'D' + vek(B[0] + C[0] - A[0], B[1] + C[1] - A[1])],
                       f'Vektor BC = {vek(*v)}, D = A + Vektor BC = {vek(*D)}. Die anderen Punkte ergeben kein Parallelogramm ABCD (falsche Reihenfolge der Ecken).',
                       'D liegt gegenüber von B. Welcher Vektor führt von A nach D?')
    # Mittelpunkt mit halbem Vektor (gerade Koordinaten)
    P = pz(5)
    h = (R.randint(-4, 4), R.randint(-4, 4))
    if h == (0, 0): return None
    Q = add(P, h, 2)
    M = add(P, h)
    return luecken(f'Berechne den Mittelpunkt M der Strecke [PQ] mit {pkt("P", *P)} und {pkt("Q", *Q)} mithilfe des Vektors PQ.', 'M(□ | □)', HV, M,
                   f'Vektor PQ = {vek(2 * h[0], 2 * h[1])}, die Hälfte ist {vek(*h)}. M = P + {vek(*h)} = {vek(*M)}.',
                   'M liegt auf halbem Weg: P plus der halbe Vektor PQ.', c=[f'({P[0]}) + (({Q[0]}) - ({P[0]})) / 2', f'({P[1]}) + (({Q[1]}) - ({P[1]})) / 2'])


GROESSEN = [('Strecke [AB]', 'cm', 'A\'B\''), ('Seite [BC]', 'cm', 'B\'C\''), ('Seite [AC]', 'mm', 'A\'C\'')]


def g_eigenschaften(s):
    v = vz(6)
    if s == 1:
        art = R.random()
        if art < 0.35:
            l = R.choice([Fr(x, 2) for x in range(5, 30)])
            n, e, n2 = R.choice(GROESSEN)
            return zahl(f'Ein Dreieck ABC wird mit v = {vek(*v)} verschoben. Die {n} ist {dz(l)} {e} lang. Wie lang ist {n2}?',
                        f'Die Verschiebung ist längentreu: {n2} = {dz(l)} {e}.', 'Ändert eine Verschiebung Längen?', l, cz(l), einheit=e)
        if art < 0.7:
            g = R.randint(15, 140)
            wn = R.choice(['α', 'β', 'γ'])
            return zahl(f'Ein Dreieck wird mit v = {vek(*v)} verschoben. Der Winkel {wn} misst {g}°. Wie groß ist {wn}\'?',
                        f'Die Verschiebung ist winkeltreu: {wn}\' = {g}°.', 'Ändert eine Verschiebung Winkel?', g, str(g), einheit='°')
        F = R.randint(4, 60)
        return zahl(f'Ein Viereck mit {F} cm² Fläche wird mit v = {vek(*v)} verschoben. Wie groß ist die Fläche des Bildvierecks?',
                    f'Die Verschiebung ist flächentreu: {F} cm².', 'Bild und Urbild sind deckungsgleich.', F, str(F), einheit='cm²')
    aussagen_w = ['Bild und Urbild sind deckungsgleich.', 'Jede Strecke ist parallel zu ihrer Bildstrecke.',
                  'Der Umlaufsinn bleibt gleich.', 'Alle Punkte werden gleich weit verschoben.',
                  'Längen und Winkel bleiben erhalten.', 'Die Verbindungsstrecken von Punkt und Bildpunkt sind alle gleich lang und parallel.']
    aussagen_f = ['Die Fläche wird größer, wenn v nach oben zeigt.', 'Die Figur wird dabei gedreht.',
                  'Der Umlaufsinn kehrt sich um.', 'Punkte, die weiter weg vom Ursprung liegen, werden weiter verschoben.',
                  'Winkel ändern sich, Längen bleiben gleich.', 'Bildstrecken stehen senkrecht auf den Urstrecken.']
    if s == 2:
        if R.random() < 0.5:
            r = R.choice(aussagen_f)
            return auswahl('Welche Aussage über die Parallelverschiebung ist FALSCH?', r, R.sample(aussagen_w, 3),
                           f'„{r}“ ist falsch. Eine Verschiebung ändert nur die Lage – sie ist eine Kongruenzabbildung.',
                           'Was ändert sich bei einer Verschiebung überhaupt?')
        r = R.choice(aussagen_w)
        return auswahl('Welche Aussage über die Parallelverschiebung ist richtig?', r, R.sample(aussagen_f, 3),
                       f'„{r}“ stimmt: Die Verschiebung ist längen-, winkel- und flächentreu und parallelentreu.',
                       'Stell dir ein Schiebepuzzle vor: Was passiert mit einem Teil?')
    art = R.random()
    if art < 0.4:
        A, B = pz(5), pz(5)
        if A == B: return None
        A2, B2 = add(A, v), add(B, v)
        w1 = ab(A, B)
        return luecken(f"Zeige mit Vektoren, dass A'B' parallel und gleich lang wie AB ist: {pkt('A', *A)}, {pkt('B', *B)}, v = {vek(*v)}. Berechne Vektor A'B'.",
                       "Vektor A'B' = (□ | □)", HV, w1,
                       f"A'{vek(*A2)}, B'{vek(*B2)}. Vektor A'B' = {vek(*w1)} = Vektor AB. Gleicher Vektor heißt: parallel und gleich lang.",
                       "Berechne erst A' und B', dann den Vektor zwischen ihnen.", c=[f'({B2[0]}) - ({A2[0]})', f'({B2[1]}) - ({A2[1]})'])
    if art < 0.7:
        P = pz(5)
        Q = add(P, v)
        w2 = vz(6)
        X = pz(5)
        Y = add(X, v)
        Yf = add(X, w2)
        if Y == Yf: return None
        return auswahl(f"Bei einer Verschiebung wird {pkt('P', *P)} auf {pkt('P' + chr(39), *Q)} abgebildet. Kann {pkt('X', *X)} dabei auf {pkt('Y', *Yf)} abgebildet werden?",
                       f"Nein, X wird auf {pkt('X' + chr(39), *Y)} abgebildet.",
                       [f'Ja, jeder Punkt kann beliebig verschoben werden.', f"Nein, X bleibt bei einer Verschiebung liegen.",
                        f"Ja, weil Y genauso weit vom Ursprung entfernt ist."],
                       f"Alle Punkte werden mit demselben Vektor v = {vek(*v)} verschoben, also X' = {vek(*Y)} ≠ Y.",
                       'Bei einer Verschiebung bekommen alle Punkte denselben Vektor.')
    u = R.randint(8, 40)
    return zahl(f'Ein Dreieck mit dem Umfang {u} cm wird zuerst mit v = {vek(*v)} und danach mit dem Gegenvektor verschoben. Welchen Umfang hat das Ergebnis?',
                f'Beide Verschiebungen sind längentreu; außerdem landet das Dreieck wieder am Ausgangsort. Umfang {u} cm.',
                'Was bewirkt der Gegenvektor? Ändert sich irgendeine Länge?', u, str(u), einheit='cm')


GEN = {'vektor_bestimmen': g_vektor_bestimmen, 'bildpunkt': g_bildpunkt, 'gegenvektor': g_gegenvektor,
       'addition': g_addition, 'punkt_berechnen': g_punkt_berechnen, 'eigenschaften': g_eigenschaften}

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import ko, rand  # noqa: E402

_ABC = [(0, 0), (4, 0), (1, 3)]
_ABC2 = [(3, 2), (7, 2), (4, 5)]
UMBAU = {
    'vektor_bestimmen': {
        'einstieg': 'Auf einer Schatzkarte steht ein Weg: vom Baum 4 Schritte nach rechts und 3 nach oben. '
                    'So eine Wegbeschreibung schreibt man kurz als (4 | 3). Sie heißt ⟦Vektor⟧.',
        'woerter': [['Vektor', 'eine Verschiebung: so weit nach rechts | so weit nach oben'],
                    ['Spitze minus Fuß', 'Zielpunkt minus Startpunkt, getrennt für x und für y']],
        'bild': ko([-1, 6], [-1, 5], {'A': (1, 1), 'B': (5, 4)}),
        'schritte': [
            {'text': 'Start ist A(1 | 1), Ziel ist B(5 | 4).'},
            {'text': 'Nach rechts: 5 − 1 = 4.', 'bild': {'strecken': [[1, 1, 5, 1, 'gestrichelt']]}},
            {'text': 'Nach oben: 4 − 1 = 3.', 'bild': {'strecken': [[1, 1, 5, 1, 'gestrichelt'], [5, 1, 5, 4, 'gestrichelt']]}},
            {'text': 'Spitze minus Fuß ergibt ⟦Vektor AB = (4 | 3)⟧.', 'bild': {'pfeile': [[1, 1, 5, 4, 'AB']]}},
        ],
        'fehler': 'Fuß minus Spitze ergibt (−4 | −3). Das ist der Vektor ⟦BA⟧, er zeigt zurück zum Baum.',
        'fehler_bild': {'pfeile': [[5, 4, 1, 1, 'BA']]},
        'regel': 'Vektor AB = Spitze minus Fuß. Rechne ⟦x von B minus x von A⟧, ebenso für y.',
    },
    'bildpunkt': {
        'einstieg': 'Ein Spielstein steht auf P. Er rutscht 5 nach rechts und 2 nach unten. '
                    'Rutschen alle Steine so, ist das eine Parallelverschiebung. Der neue Platz heißt ⟦Bildpunkt⟧.',
        'woerter': [['Bildpunkt', 'der Punkt nach der Verschiebung, geschrieben P′ (gelesen „P Strich“)'],
                    ['Parallelverschiebung', 'alle Punkte rutschen mit demselben Vektor']],
        'bild': ko([-3, 4], [-2, 5], {'P': (-2, 3)}),
        'schritte': [
            {'text': 'P(−2 | 3) wird mit v = (5 | −2) verschoben.', 'bild': {'pfeile': [[-2, 3, 3, 1, 'v']]}},
            {'text': 'x: −2 + 5 = 3.'},
            {'text': 'y: 3 + (−2) = 1, denn −2 heißt nach unten.'},
            {'text': 'Der Bildpunkt ist ⟦P′(3 | 1)⟧.', 'bild': {'punkte': [{'x': -2, 'y': 3, 'name': 'P'}, {'x': 3, 'y': 1, 'name': 'P′'}]}},
        ],
        'fehler': '3 + (−2) = 5 ist falsch. Minus beim y heißt ⟦nach unten⟧, der Stein landet tiefer: 3 + (−2) = 1.',
        'fehler_bild': {'punkte': [{'x': -2, 'y': 3, 'name': 'P'}, {'x': 3, 'y': 1, 'name': 'P′'}, {'x': 3, 'y': 5, 'name': 'falsch'}]},
        'regel': 'Bildpunkt = Punkt plus Vektor: x plus x, y plus y. ⟦Alle Punkte⟧ rutschen mit demselben Vektor.',
    },
    'gegenvektor': {
        'einstieg': 'Der Spielstein soll zurück an seinen Start. Dafür geht er denselben Weg rückwärts: '
                    'nach links statt nach rechts, nach oben statt nach unten. Dieser Rückweg heißt ⟦Gegenvektor⟧.',
        'woerter': [['Gegenvektor', 'gleich lang, aber genau entgegengesetzt; zu v gehört −v'],
                    ['Urpunkt', 'der Punkt vor der Verschiebung']],
        'bild': ko([-4, 6], [-2, 6], {'P′': (1, 2)}),
        'schritte': [
            {'text': 'P′(1 | 2) entstand durch v = (4 | −3). Gesucht ist der Urpunkt P.'},
            {'text': 'Gegenvektor: Vorzeichen umdrehen, −v = (−4 | 3).', 'bild': {'pfeile': [[1, 2, -3, 5, '−v']]}},
            {'text': 'P = (1 + (−4) | 2 + 3) = ⟦P(−3 | 5)⟧.',
             'bild': {'punkte': [{'x': 1, 'y': 2, 'name': 'P′'}, {'x': -3, 'y': 5, 'name': 'P'}]}},
            {'text': 'Probe: P plus v ergibt wieder (1 | 2).', 'bild': {'pfeile': [[-3, 5, 1, 2, 'v']]}},
        ],
        'fehler': 'Nochmal v addieren schiebt weiter statt zurück: (5 | −1) ist falsch. Für den Rückweg brauchst du den ⟦Gegenvektor⟧.',
        'fehler_bild': {'punkte': [{'x': 1, 'y': 2, 'name': 'P′'}, {'x': 5, 'y': -1, 'name': 'falsch'}], 'pfeile': [[1, 2, 5, -1, 'v']]},
        'regel': 'Gegenvektor: beide Vorzeichen umdrehen. Mit ⟦−v⟧ kommt jeder Bildpunkt zurück zum Urpunkt.',
    },
    'addition': {
        'einstieg': 'Der Spielstein zieht zweimal: erst (3 | −1), dann (−5 | 4). Wo endet er insgesamt? '
                    'Beide Züge zusammen sind ein einziger Zug, die ⟦Summe⟧ der Vektoren.',
        'woerter': [['Summe', 'das Ergebnis beim Addieren; hier: beide Züge als ein einziger Zug']],
        'bild': ko([-3, 4], [-2, 4], {'Start': (0, 0)}),
        'schritte': [
            {'text': 'Erster Zug: v₁ = (3 | −1).', 'bild': {'pfeile': [[0, 0, 3, -1, 'v₁']]}},
            {'text': 'Zweiter Zug ab dort: v₂ = (−5 | 4).', 'bild': {'pfeile': [[0, 0, 3, -1, 'v₁'], [3, -1, -2, 3, 'v₂']]}},
            {'text': 'x: 3 + (−5) = −2. y: −1 + 4 = 3.'},
            {'text': 'Summe: ⟦(−2 | 3)⟧, der direkte Weg vom Start zum Ziel.',
             'bild': {'pfeile': [[0, 0, 3, -1, 'v₁'], [3, -1, -2, 3, 'v₂'], [0, 0, -2, 3, 'Summe']]}},
        ],
        'fehler': 'Über Kreuz addieren, also x mit y, ist falsch. Es gilt ⟦x mit x⟧ und y mit y.',
        'regel': 'Vektoren addieren: x mit x, y mit y. ⟦AB + BC = AC⟧: Zwei Züge ergeben einen.',
    },
    'punkt_berechnen': {
        'einstieg': 'Ein Spielfeld hat die Form eines Parallelogramms ABCD. Drei Ecken kennst du, die vierte fehlt. '
                    'Gegenüberliegende Seiten sind gleiche Vektoren. Damit findest du D ohne Zeichnung.',
        'woerter': [['Parallelogramm', 'Viereck mit den Ecken der Reihe nach A, B, C, D; Gegenseiten parallel und gleich lang']],
        'bild': ko([-1, 7], [-1, 5], {'A': (0, 0), 'B': (4, 1), 'C': (6, 4)}, [[0, 0, 4, 1], [4, 1, 6, 4]]),
        'schritte': [
            {'text': 'Vektor BC = (6 − 4 | 4 − 1) = (2 | 3).', 'bild': {'pfeile': [[4, 1, 6, 4, 'BC']]}},
            {'text': 'AD ist derselbe Vektor wie BC.', 'bild': {'pfeile': [[4, 1, 6, 4, 'BC'], [0, 0, 2, 3, 'AD']]}},
            {'text': 'D = (0 + 2 | 0 + 3) = ⟦D(2 | 3)⟧.',
             'bild': {'punkte': [{'x': 0, 'y': 0, 'name': 'A'}, {'x': 4, 'y': 1, 'name': 'B'}, {'x': 6, 'y': 4, 'name': 'C'}, {'x': 2, 'y': 3, 'name': 'D'}],
                      'strecken': [[0, 0, 4, 1], [4, 1, 6, 4], [6, 4, 2, 3, 'gestrichelt'], [2, 3, 0, 0, 'gestrichelt']]}},
        ],
        'fehler': 'D = B + AC ist falsch, das ergibt einen Punkt weit außerhalb. D liegt ⟦gegenüber von B⟧, die Ecken laufen der Reihe nach.',
        'regel': 'Im Parallelogramm ABCD gilt ⟦AD = BC⟧. Also ist D = A + Vektor BC.',
    },
    'eigenschaften': {
        'einstieg': 'Schiebst du ein Puzzleteil über den Tisch, bleibt es dasselbe Teil. Nur sein Platz ändert sich. '
                    'Abbildungen, bei denen Form und Größe bleiben, heißen ⟦Kongruenzabbildungen⟧.',
        'woerter': [['Kongruenzabbildung', 'Bild und Original sind deckungsgleich: gleiche Form, gleiche Größe'],
                    ['längentreu', 'jede Strecke ist im Bild genauso lang wie vorher']],
        'bild': ko([-1, 8], [-1, 6], {'A': _ABC[0], 'B': _ABC[1], 'C': _ABC[2]}, rand(*_ABC)),
        'schritte': [
            {'text': 'Das Dreieck ABC wird mit v = (3 | 2) verschoben.',
             'bild': {'pfeile': [[0, 0, 3, 2, 'v'], [4, 0, 7, 2], [1, 3, 4, 5]]}},
            {'text': 'Das Bild A′B′C′ liegt woanders, sieht aber gleich aus.',
             'bild': {'pfeile': None,
                      'punkte': [{'x': a, 'y': b, 'name': n} for n, (a, b) in zip(['A', 'B', 'C', 'A′', 'B′', 'C′'], _ABC + _ABC2)],
                      'strecken': rand(*_ABC) + rand(*_ABC2)}},
            {'text': 'Längentreu: A′B′ ist wie AB ⟦4 lang⟧ und parallel dazu.'},
            {'text': 'Auch Winkel und Fläche bleiben: beide Dreiecke sind ⟦6 Kästchen⟧ groß.'},
        ],
        'fehler': '„Nach oben geschoben heißt größer“ ist falsch. Eine Verschiebung ändert nur die ⟦Lage⟧, nie Größe oder Form.',
        'regel': 'Verschieben ändert nur die Lage. Längen, Winkel und Flächen bleiben, Strecken bleiben ⟦parallel⟧ zu ihrem Bild.',
    },
}
UMBAU_OFFEN = ['Umbau (Paket UR): Die Lernkarten zeigen Vektoren jetzt als Pfeile. Die Aufgaben-Grafiken zeigen sie weiter als Strecken, '
               'weil Aufgaben beim Umbau unverändert bleiben.']
UMBAU_WEG = ['App-Wunsch: Pfeilspitzen']
# ---------- Ende UMBAU ----------


if __name__ == '__main__':
    d = bauen('abbildungen.vektoren',
          'Vektoren als Verschiebungen verstehen, Bildpunkte, Gegenvektoren und Vektorsummen berechnen und Punkte mit Vektoren bestimmen.',
          ['Vektor AB = Spitze minus Fuß: (x_B − x_A | y_B − y_A).', "Bildpunkt: P' = P + v. Urpunkt: P = P' + (−v).",
           'Vektoren addieren: x mit x, y mit y. Vektor AB + Vektor BC = Vektor AC.',
           'Parallelogramm ABCD: Vektor AD = Vektor BC.', 'Die Verschiebung ist eine Kongruenzabbildung (längen-, winkel-, flächentreu).'],
          [('Vektoren und Verschiebung', ['vektor_bestimmen', 'bildpunkt', 'gegenvektor']),
           ('Rechnen mit Vektoren', ['addition', 'punkt_berechnen']), ('Eigenschaften', ['eigenschaften'])],
          ETAPPEN, GEN,
          offen=['Flächen mit Determinanten stehen im eigenen Thema abbildungen.determinanten2 (gleicher Block); hier nicht wiederholt.',
                 'Das Skalarprodukt (im Feld umfang genannt) ist Stoff der Realschule Klasse 10 und wurde weggelassen; es steht im Thema abbildungen.matrizen.',
                 'Kongruenzeigenschaften hier nur für die Parallelverschiebung; Drehung und Achsenspiegelung sind Gymnasium-Themen (abbildungen.kongruenz).',
                 'App-Wunsch: Pfeilspitzen für Vektoren im Koordinatensystem. Bis dahin erscheinen Verschiebungspfeile als Strecken.'])
    umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
