#!/usr/bin/env python3
"""Thema trigo.pythagoras – Satz des Pythagoras (Klasse 9)."""
import sys
from math import gcd, isqrt, sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(910)

# pythagoreische Tripel (a < b < c), c ≤ 100
TRIPEL = sorted({(a, b, c) for a in range(1, 100) for b in range(a + 1, 100)
                 for c in [isqrt(a * a + b * b)] if c * c == a * a + b * b and c <= 100})
KLEIN = [t for t in TRIPEL if t[2] <= 30]
# Quader mit ganzzahliger Raumdiagonale
QUADER = [(a, b, c, isqrt(a * a + b * b + c * c)) for a in range(1, 13) for b in range(a, 13) for c in range(b, 25)
          if isqrt(a * a + b * b + c * c) ** 2 == a * a + b * b + c * c]


GESEHEN = {}


def neu_trip(lz, t):
    """Ein Tripel (auch vertauscht) nur einmal je Lernkarte."""
    k = tuple(sorted(Fr(x) for x in t))
    g = GESEHEN.setdefault(lz, set())
    if k in g: return False
    g.add(k)
    return True


def dreieck(a, b, lab, rw='C', namen=('A', 'B', 'C')):
    """Rechtwinkliges Dreieck mit Katheten a (senkrecht) und b (waagrecht); lab = Beschriftungen [Kathete a, Kathete b, Hypotenuse]."""
    A_, B_, C_ = namen
    return {'typ': 'figur', 'punkte': {C_: [0, 0], A_: [float(b), 0], B_: [0, float(a)]},
            'linien': [[B_, C_, lab[0]], [C_, A_, lab[1]], [A_, B_, lab[2]]], 'rechter_winkel': [[C_, A_, B_]]}


def trip(s):
    pool = KLEIN if s == 1 else [t for t in TRIPEL if t[2] <= 60 and t != (3, 4, 5)] if s == 2 else [t for t in TRIPEL if t != (3, 4, 5)]
    t = R.choice(pool)
    if s == 3 and R.random() < 0.4:
        f = R.choice([Fr(1, 10), Fr(1, 2), Fr(3, 10)])
        return tuple(x * f for x in t)
    return tuple(Fr(x) for x in t)


def cf(x):
    return str(float(x)) if Fr(x).denominator != 1 else str(int(x))


ETAPPEN = [
    {'lernziel': 'hypotenuse', 'titel': 'Die Hypotenuse berechnen',
     'regel': 'Im ⟦rechtwinkligen⟧ Dreieck gilt ⟦a² + b² = c²⟧. Im Bild: Die beiden Quadrate über den Katheten haben ⟦zusammen genau so viel Fläche⟧ wie das Quadrat über der Hypotenuse. c ist die ⟦Hypotenuse⟧ (gegenüber dem rechten Winkel, längste Seite), a und b sind die ⟦Katheten⟧.',
     'bild': {'typ': 'figur', 'punkte': {'C': [0, 0], 'A': [12, 0], 'B': [0, 9], '_a1': [-9, 0], '_a2': [-9, 9], '_b1': [0, -12], '_b2': [12, -12], '_c1': [21, 12], '_c2': [9, 21]}, 'flaeche': ['A', 'B', 'C'], 'linien': [['A', 'B', 'c = 15'], ['B', 'C', 'a = 9'], ['C', 'A', 'b = 12'], ['C', '_a1'], ['_a1', '_a2', 'a² = 81'], ['_a2', 'B'], ['C', '_b1'], ['_b1', '_b2', 'b² = 144'], ['_b2', 'A'], ['A', '_c1'], ['_c1', '_c2', 'c² = 225'], ['_c2', 'B']], 'rechter_winkel': [['C', 'A', 'B']]},
     'schritte': ['Katheten 9 cm und 12 cm: c² = 9² + 12² = 81 + 144 = 225.', 'c = √225 cm = ⟦15 cm⟧.'],
     'probe': '15 ist länger als beide Katheten ✓',
     'fehler': 'c = 9 + 12 = 21 cm ist falsch: Man addiert die ⟦Quadrate⟧ und zieht dann die Wurzel: √(81 + 144) = 15.'},
    {'lernziel': 'kathete', 'titel': 'Eine Kathete berechnen',
     'regel': 'Ist die Hypotenuse bekannt, stellst du um: ⟦a² = c² − b²⟧. Die Kathete ist ⟦kürzer⟧ als die Hypotenuse.',
     'schritte': ['Hypotenuse 13 cm, Kathete 5 cm: a² = 13² − 5² = 169 − 25 = 144.', 'a = √144 cm = ⟦12 cm⟧.'],
     'probe': '5² + 12² = 25 + 144 = 169 = 13² ✓',
     'fehler': 'a² = 13² + 5² = 194 ist falsch: Gesucht ist eine ⟦Kathete⟧, also wird ⟦subtrahiert⟧. Das Ergebnis muss kleiner als 13 sein.'},
    {'lernziel': 'umkehrung', 'titel': 'Ist das Dreieck rechtwinklig?',
     'regel': '⟦Umkehrung⟧: Gilt für die ⟦längste⟧ Seite c, dass a² + b² = c², dann ist das Dreieck rechtwinklig, und der rechte Winkel liegt ⟦gegenüber von c⟧.',
     'schritte': ['Seiten 20 cm, 21 cm, 29 cm: längste Seite 29.', '20² + 21² = 400 + 441 = 841 = 29² ⇒ ⟦rechtwinklig⟧.'],
     'probe': 'Alltag: Wer einen rechten Winkel für ein Beet abstecken will, legt ein Dreieck mit 3 m, 4 m und 5 m. Weil 3² + 4² = 25 = 5², ist der Winkel gegenüber der 5-m-Seite ein rechter ✓',
     'fehler': '6² + 10² = 136 ≠ 8² ⇒ „nicht rechtwinklig“ ist ein Fehlschluss: Man muss die ⟦längste⟧ Seite (10) als c nehmen: 6² + 8² = 100 = 10².'},
    {'lernziel': 'koordinaten', 'titel': 'Abstand im Koordinatensystem',
     'regel': 'Der Abstand von P(x₁ | y₁) und Q(x₂ | y₂) ist die Hypotenuse eines Steigungsdreiecks: ⟦d = √((x₂ − x₁)² + (y₂ − y₁)²)⟧.',
     'schritte': ['P(1 | 2), Q(7 | 10): Δx = 6, Δy = 8.', 'd = √(36 + 64) = √100 = ⟦10⟧.'],
     'probe': 'Δx und Δy sind die Katheten ✓',
     'bild': {'typ': 'koordinaten', 'x': [0, 8], 'y': [0, 11], 'punkte': [{'x': 1, 'y': 2, 'name': 'P'}, {'x': 7, 'y': 10, 'name': 'Q'}], 'strecken': [[1, 2, 7, 10], [1, 2, 7, 2, 'gestrichelt'], [7, 2, 7, 10, 'gestrichelt']]},
     'fehler': 'd = √(7² + 10²) mit den Koordinaten von Q ist falsch: Man braucht die ⟦Differenzen⟧ der Koordinaten.'},
    {'lernziel': 'raum', 'titel': 'Längen im Raum',
     'regel': 'Im Quader mit Kanten a, b, c: Flächendiagonale ⟦√(a² + b²)⟧, Raumdiagonale ⟦√(a² + b² + c²)⟧. Suche im Körper ein ⟦rechtwinkliges Dreieck⟧.',
     'schritte': ['Quader 2 cm × 3 cm × 6 cm: d² = 4 + 9 + 36 = 49.', 'Raumdiagonale d = √49 cm = ⟦7 cm⟧.'],
     'probe': 'Erst Bodendiagonale √13, dann √(13 + 36) = 7 ✓',
     'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [3, 0], 'C': [3.71, 0.71], 'D': [0.71, 0.71], 'E': [0, 6], 'F': [3, 6], 'G': [3.71, 6.71], 'H': [0.71, 6.71]}, 'linien': [['A', 'B'], ['B', 'F'], ['F', 'E'], ['E', 'A'], ['B', 'C'], ['C', 'G'], ['G', 'F'], ['E', 'H'], ['H', 'G'], ['A', 'D', '', 'gestrichelt'], ['D', 'C', '', 'gestrichelt'], ['D', 'H', '', 'gestrichelt'], ['A', 'G', 'd = ?'], ['A', 'C', '√13', 'gestrichelt']]},
     'fehler': 'Raumdiagonale = √(2² + 3²) ist nur die ⟦Bodendiagonale⟧. Die Höhe 6 cm muss auch ins Quadrat und dazu.'},
    {'lernziel': 'anwendung', 'titel': 'Pythagoras im Alltag',
     'regel': 'Skizze machen, ⟦rechten Winkel⟧ suchen, Hypotenuse bestimmen, dann a² + b² = c² passend umstellen. Am Ende ⟦sinnvoll runden⟧.',
     'schritte': ['Eine 5 m lange Leiter lehnt an einer Wand, ihr Fuß steht 1,4 m von der Wand entfernt.', 'h² = 5² − 1,4² = 25 − 1,96 = 23,04 ⇒ h = ⟦4,8 m⟧ (Höhe des oberen Endes).'],
     'probe': '1,4² + 4,8² = 1,96 + 23,04 = 25 ✓',
     'bild': {'typ': 'figur', 'punkte': {'_F': [0, 0], 'W': [0, 4.8], 'B': [1.4, 0]}, 'linien': [['_F', 'B', '1,4 m'], ['_F', 'W', 'h = ?'], ['W', 'B', 'Leiter 5 m']], 'rechter_winkel': [['_F', 'B', 'W']]},
     'fehler': 'h² = 5² + 1,4² ist falsch: Die ⟦Leiter⟧ liegt gegenüber dem rechten Winkel zwischen Wand und Boden, sie ist die Hypotenuse.'},
]


def g_hypotenuse(s):
    a, b, c = trip(s)
    if R.random() < 0.5: a, b = b, a
    if s >= 2 and R.random() < (0.3 if s == 2 else 0.25):
        a, b = R.randint(2, 15), R.randint(2, 15)
        if isqrt(a * a + b * b) ** 2 == a * a + b * b: return None
        wahr = sqrt(a * a + b * b)
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Ein rechtwinkliges Dreieck hat die Katheten {a} cm und {b} cm. Berechne die Hypotenuse auf eine Nachkommastelle.',
                    f'c² = {a * a} + {b * b} = {a * a + b * b}, c = √{a * a + b * b} cm ≈ {dz(v)} cm.', 'Quadrieren, addieren, Wurzel ziehen (Taschenrechner).',
                    v, f'round({K(wahr)}, 1)', einheit='cm')
    if s == 3 and all(Fr(x).denominator == 1 for x in (a, b, c)) and R.random() < 0.5:
        f = R.choice([Fr(1, 10), Fr(1, 2), Fr(3, 10)])
        a, b, c = a * f, b * f, c * f
    if not neu_trip('hypotenuse', (a, b, c)): return None
    if s == 3 and R.random() < 0.6:
        if R.random() < 0.5:
            return bild(zahl(f'Im Dreieck ABC ist α = 90°, b = {dz(a)} cm und c = {dz(b)} cm. Berechne a.',
                             f'Der rechte Winkel liegt bei A, also ist a die Hypotenuse: a² = {dz(a * a)} + {dz(b * b)} = {dz(c * c)}, a = {dz(c)} cm.',
                             'Welche Seite liegt dem rechten Winkel gegenüber? Das ist die Hypotenuse.', c,
                             f'({cf(a)} ** 2 + {cf(b)} ** 2) / {cf(c)}', einheit='cm'),
                        dreieck(a, b, [f'b = {dz(a)}', f'c = {dz(b)}', 'a = ?'], namen=('B', 'C', 'A')))
        return zahl(f'Im Dreieck PQR ist der Winkel bei Q ein rechter, PQ = {dz(a)} cm, QR = {dz(b)} cm. Berechne PR.',
                    f'PR liegt gegenüber dem rechten Winkel bei Q: PR² = {dz(a * a)} + {dz(b * b)} = {dz(c * c)}, PR = {dz(c)} cm.',
                    'Die Seite gegenüber dem rechten Winkel ist die Hypotenuse.', c, f'({cf(a)} ** 2 + {cf(b)} ** 2) / {cf(c)}', einheit='cm')
    a_ = zahl(f'Ein rechtwinkliges Dreieck hat die Katheten a = {dz(a)} cm und b = {dz(b)} cm. Berechne die Hypotenuse c.',
              f'c² = {dz(a * a)} + {dz(b * b)} = {dz(c * c)}, c = {dz(c)} cm.', 'Beide Katheten quadrieren, addieren, dann die Wurzel ziehen.', c,
              f'({cf(a)} ** 2 + {cf(b)} ** 2) / {cf(c)}', einheit='cm')
    if s == 1: bild(a_, dreieck(a, b, [f'a = {dz(a)}', f'b = {dz(b)}', 'c = ?']))
    return a_


def g_kathete(s):
    a, b, c = trip(s)
    if R.random() < 0.5: a, b = b, a
    if s == 3 and R.random() < 0.3:
        a, b, c = (int(x) for x in R.choice(KLEIN))
        if R.random() < 0.5:
            falsch = c * c + b * b
            w_ = gerundet(sqrt(falsch), 1)
            if w_ is None: return None
            return auswahl(f'Hypotenuse {c} cm, Kathete {b} cm. Jemand rechnet a² = {c}² + {b}² = {falsch}, a ≈ {dz(w_)} cm. Was ist falsch?',
                           f'Bei einer Kathete wird subtrahiert: a² = {c * c} − {b * b} = {a * a}, a = {a} cm. Eine Kathete ist nie länger als die Hypotenuse.',
                           ['Nichts, die Rechnung stimmt.', f'Man muss die Längen subtrahieren: a = {c} − {b} = {c - b} cm.', f'Man muss halbieren: a = {dz(Fr(c, 2))} cm.'],
                           f'Gesucht ist eine Kathete: a² = c² − b² = {c * c} − {b * b} = {a * a}, a = {a} cm.',
                           'Ist die gesuchte Seite die Hypotenuse oder eine Kathete?')
        return auswahl(f'Hypotenuse {c} cm, Kathete {b} cm. Jemand rechnet a = {c} − {b} = {c - b} cm. Was ist falsch?',
                       f'Die Quadrate werden subtrahiert, nicht die Längen: a = √({c * c} − {b * b}) = {a} cm.',
                       ['Nichts, die Rechnung stimmt.', f'Man muss addieren: a = {c + b} cm.', f'Man muss die Quadrate addieren: a² = {c * c + b * b}.'],
                       f'a² = {c}² − {b}² = {c * c} − {b * b} = {a * a}, also a = {a} cm ≠ {c - b} cm.',
                       'Gilt der Satz für die Längen oder für ihre Quadrate?')
    if not neu_trip('kathete', (a, b, c)): return None
    if s == 3 and R.random() < 0.4:
        c, b = R.randint(8, 20), R.randint(2, 7)
        d = c * c - b * b
        if isqrt(d) ** 2 == d: return None
        wahr = sqrt(d)
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Ein rechtwinkliges Dreieck hat die Hypotenuse {c} cm und eine Kathete {b} cm. Berechne die andere Kathete auf eine Nachkommastelle.',
                    f'a² = {c * c} − {b * b} = {d}, a ≈ {dz(v)} cm.', 'Hypotenusenquadrat minus Kathetenquadrat.', v, f'round({K(wahr)}, 1)', einheit='cm')
    return zahl(f'Ein rechtwinkliges Dreieck hat die Hypotenuse c = {dz(c)} cm und die Kathete b = {dz(b)} cm. Berechne die Kathete a.',
                f'a² = {dz(c * c)} − {dz(b * b)} = {dz(a * a)}, a = {dz(a)} cm.', 'Gesucht ist eine Kathete: Subtrahiere.', a,
                f'({cf(c)} ** 2 - {cf(b)} ** 2) / {cf(a)}', einheit='cm')


FAST = [(6, 8, 11), (7, 24, 26), (5, 12, 14), (8, 15, 18), (9, 12, 16), (6, 8, 9), (10, 24, 25), (12, 16, 21), (7, 8, 10), (20, 21, 30)]


def g_umkehrung(s):
    if s == 3 and R.random() < 0.5:
        a, b, c = R.choice(FAST + [tuple(int(x) for x in t) for t in KLEIN[:8]])
        q = a * a + b * b
        art = 'ein rechter Winkel' if q == c * c else 'ein spitzer Winkel' if q > c * c else 'ein stumpfer Winkel'
        return auswahl(f'Ein Dreieck hat die Seiten {a} cm, {b} cm und {c} cm. Welcher Winkel liegt der {c}-cm-Seite gegenüber?', art,
                       ['ein spitzer Winkel', 'ein rechter Winkel', 'ein stumpfer Winkel'],
                       f'{a}² + {b}² = {q}, {c}² = {c * c}. ' + ('Gleich: rechter Winkel.' if q == c * c else
                                                              f'{q} > {c * c}: Die längste Seite ist zu kurz für einen rechten Winkel – spitz.' if q > c * c else
                                                              f'{q} < {c * c}: Die längste Seite ist zu lang für einen rechten Winkel – stumpf.'),
                       'Vergleiche a² + b² mit c² für die längste Seite.')
    if s < 3:
        recht = R.random() < 0.5
        if recht:
            a, b, c = (int(x) for x in R.choice(TRIPEL if s > 1 else KLEIN))
        else:
            a, b, c = R.choice(FAST) if R.random() < 0.6 else tuple(int(x) for x in R.choice(TRIPEL if s > 1 else KLEIN))
            if a * a + b * b == c * c:
                c += R.choice([-1, 1])
                if c <= b: return None
        seiten = [a, b, c]
        R.shuffle(seiten)
        return auswahl(f'Ein Dreieck hat die Seiten {seiten[0]} cm, {seiten[1]} cm und {seiten[2]} cm. Ist es rechtwinklig?',
                       'Ja, es ist rechtwinklig.' if recht else 'Nein, es ist nicht rechtwinklig.',
                       ['Nein, es ist nicht rechtwinklig.' if recht else 'Ja, es ist rechtwinklig.',
                        'Das kann man ohne Winkelmessung nicht entscheiden.', f'Ja, weil {a} + {b} > {c}.'],
                       (f'Längste Seite {c} cm: {a}² + {b}² = {dz(a * a)} + {dz(b * b)} = {dz(a * a + b * b)} = {c}². ' if recht else
                        f'Längste Seite {c} cm: {a}² + {b}² = {dz(a * a)} + {dz(b * b)} = {dz(a * a + b * b)}, aber {c}² = {dz(c * c)}. ')
                       + ('Also rechtwinklig.' if recht else 'Also nicht rechtwinklig.'),
                       'Prüfe a² + b² = c² mit der längsten Seite als c.')
    a, b, c = (int(x) for x in R.choice(TRIPEL))
    namen = ['a', 'b', 'c']
    R.shuffle(namen)
    werte = dict(zip(namen, [a, b, c]))
    gross = max(werte, key=werte.get)
    ecke = {'a': 'α (bei A)', 'b': 'β (bei B)', 'c': 'γ (bei C)'}
    return auswahl(f'Im Dreieck ABC ist a = {werte["a"]} cm, b = {werte["b"]} cm, c = {werte["c"]} cm. Welcher Winkel ist ein rechter Winkel?',
                   ecke[gross], list(ecke.values()),
                   f'Längste Seite {gross} = {werte[gross]} cm; die Summe der anderen Quadrate ist {dz(werte[gross] ** 2)} = {werte[gross]}². Der rechte Winkel liegt gegenüber von {gross}: {ecke[gross]}.',
                   'Der rechte Winkel liegt gegenüber der längsten Seite.')


def kos_pq(x1, y1, x2, y2):
    lo_x, hi_x = min(x1, x2) - 1, max(x1, x2) + 1
    lo_y, hi_y = min(y1, y2) - 1, max(y1, y2) + 1
    return {'typ': 'koordinaten', 'x': [lo_x, hi_x], 'y': [lo_y, hi_y],
            'punkte': [{'x': x1, 'y': y1, 'name': 'P'}, {'x': x2, 'y': y2, 'name': 'Q'}],
            'strecken': [[x1, y1, x2, y2], [x1, y1, x2, y1, 'gestrichelt'], [x2, y1, x2, y2, 'gestrichelt']]}


def g_koordinaten(s):
    a, b, c = (int(x) for x in R.choice(KLEIN if s == 1 else [t for t in TRIPEL if t[2] <= 50 and t != (3, 4, 5)]))
    if R.random() < 0.5: a, b = b, a
    x1, y1 = R.randint(-6, 6), R.randint(-6, 6)
    sx, sy = R.choice([1, -1]), R.choice([1, -1])
    if s == 1:
        sx = sy = 1
        if c > 15: return None
    x2, y2 = x1 + sx * a, y1 + sy * b
    if s == 3:
        typ = R.random()
        if typ < 0.35:
            dx, dy = R.randint(1, 7), R.randint(1, 7)
            if isqrt(dx * dx + dy * dy) ** 2 == dx * dx + dy * dy: return None
            x2, y2 = x1 + dx * sx, y1 + dy * sy
            wahr = sqrt(dx * dx + dy * dy)
            v = gerundet(wahr, 2)
            if v is None: return None
            return zahl(f'Berechne den Abstand von P({dz(x1)} | {dz(y1)}) und Q({dz(x2)} | {dz(y2)}) auf zwei Nachkommastellen (Einheit 1 cm).',
                        f'Δx = {dz(x2 - x1)}, Δy = {dz(y2 - y1)}; d = √({dx * dx} + {dy * dy}) = √{dx * dx + dy * dy} ≈ {dz(v)} cm.',
                        'Differenzen der Koordinaten quadrieren, addieren, Wurzel ziehen.', v, f'round({K(wahr)}, 2)', einheit='cm')
        if typ < 0.7:
            if R.random() < 0.5:
                return zahl(f'P({dz(x1)} | {dz(y1)}) und Q(x | {dz(y2)}) haben den Abstand {c}, und x {">" if sx > 0 else "<"} {dz(x1)}. Bestimme x.',
                            f'Δy = {dz(y2 - y1)}; Δx² = {c}² − {dz((y2 - y1) ** 2)} = {a * a}, Δx = {"+" if sx > 0 else "−"}{a}; x = {dz(x1)} {"+" if sx > 0 else "−"} {a} = {dz(x2)}.',
                            'Stelle d² = Δx² + Δy² nach Δx² um. Beachte die Bedingung an x.', x2, f'{x1} + ({sx}) * ({c} ** 2 - ({y2} - ({y1})) ** 2) / {a}')
            return zahl(f'P({dz(x1)} | {dz(y1)}) und Q({dz(x2)} | y) haben den Abstand {c}, und y {">" if sy > 0 else "<"} {dz(y1)}. Bestimme y.',
                        f'Δx = {dz(x2 - x1)}; Δy² = {c}² − {dz((x2 - x1) ** 2)} = {b * b}, Δy = {"+" if sy > 0 else "−"}{b}; y = {dz(y1)} {"+" if sy > 0 else "−"} {b} = {dz(y2)}.',
                        'Stelle d² = Δx² + Δy² nach Δy² um. Beachte die Bedingung an y.', y2, f'{y1} + ({sy}) * ({c} ** 2 - ({x2} - ({x1})) ** 2) / {b}')
        # Dreieck im Koordinatensystem: Umfang
        p2, q2, r2 = (int(x) for x in R.choice(KLEIN))
        A_ = (x1, y1); B_ = (x1 + a * sx, y1); C_ = (x1 + a * sx, y1 + b * sy)
        u = a + b + c
        return zahl(f'Berechne den Umfang des Dreiecks A({dz(A_[0])} | {dz(A_[1])}), B({dz(B_[0])} | {dz(B_[1])}), C({dz(C_[0])} | {dz(C_[1])}) (Einheit 1 cm).',
                    f'AB = {a}, BC = {b} (waagrecht bzw. senkrecht), AC = √({a * a} + {b * b}) = {c}. Umfang {a} + {b} + {c} = {u} cm.',
                    'Zwei Seiten liegen parallel zu den Achsen; die dritte berechnest du mit Pythagoras.', u, f'{a} + {b} + ({a} ** 2 + {b} ** 2) / {c}', einheit='cm')
    a_ = zahl(f'Berechne den Abstand der Punkte P({dz(x1)} | {dz(y1)}) und Q({dz(x2)} | {dz(y2)}) (Einheit 1 cm).',
              f'Δx = {dz(x2 - x1)}, Δy = {dz(y2 - y1)}; d = √({dz(a * a)} + {dz(b * b)}) = √{dz(c * c)} = {c} cm.',
              'Bilde die Differenzen der x- und der y-Koordinaten.', c, f'(({x2} - ({x1})) ** 2 + ({y2} - ({y1})) ** 2) / {c}', einheit='cm')
    if s == 1: bild(a_, kos_pq(x1, y1, x2, y2))
    return a_


def g_raum(s):
    if s == 1:
        a, b, c = (int(x) for x in R.choice(KLEIN))
        return zahl(f'Ein Quader hat die Grundfläche {a} cm × {b} cm. Wie lang ist die Diagonale der Grundfläche?',
                    f'd² = {a}² + {b}² = {c * c}, d = {c} cm.', 'Die Diagonale teilt das Rechteck in zwei rechtwinklige Dreiecke.', c,
                    f'({a} ** 2 + {b} ** 2) / {c}', einheit='cm')
    if s == 2:
        a, b, c, d = R.choice(QUADER)
        return zahl(f'Ein Quader hat die Kanten {a} cm, {b} cm und {c} cm. Wie lang ist die Raumdiagonale?',
                    f'd² = {a}² + {b}² + {c}² = {a * a} + {b * b} + {c * c} = {d * d}, d = {d} cm.', 'Raumdiagonale: alle drei Kantenquadrate addieren.', d,
                    f'({a} ** 2 + {b} ** 2 + {c} ** 2) / {d}', einheit='cm')
    typ = R.random()
    if typ < 0.3:
        l, b, h = R.choice([(60, 40, 30), (50, 30, 20), (80, 50, 40), (40, 30, 25), (100, 60, 50), (70, 40, 20), (45, 35, 30)])
        d = sqrt(l * l + b * b + h * h)
        stab = int(d) + R.choice([-6, -4, -3, 3, 4, 6])
        passt = stab < d
        return auswahl(f'Eine Kiste ist innen {l} cm × {b} cm × {h} cm groß. Passt ein {stab} cm langer Stab hinein?',
                       f'{"Ja" if passt else "Nein"}, die Raumdiagonale ist {"etwa" if passt else "nur etwa"} {round(d)} cm.',
                       [f'{"Nein" if passt else "Ja"}, die Raumdiagonale ist etwa {round(d)} cm.', f'Nein, die längste Kante ist nur {l} cm.' if passt else f'Ja, weil {l} + {b} > {stab}.',
                        f'Ja, die Bodendiagonale ist etwa {round(sqrt(l * l + b * b))} cm.' if not passt else f'Nein, die Bodendiagonale ist nur etwa {round(sqrt(l * l + b * b))} cm.'],
                       f'Der längste Stab liegt auf der Raumdiagonale: d = √({dz(l * l)} + {dz(b * b)} + {dz(h * h)}) = √{dz(l * l + b * b + h * h)} ≈ {dz(round(d, 1))} cm. {stab} cm {"<" if passt else ">"} {dz(round(d, 1))} cm.',
                       'Der längste Weg in der Kiste ist die Raumdiagonale.')
    if typ < 0.6:
        a = R.randint(1, 12)
        # Würfel: Raumdiagonale a√3 – gerundet
        wahr = a * sqrt(3)
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Wie lang ist die Raumdiagonale eines Würfels mit {a} cm Kantenlänge? Runde auf eine Nachkommastelle.',
                    f'd² = 3 · {a}² = {3 * a * a}, d = √{3 * a * a} ≈ {dz(v)} cm.', 'Beim Würfel sind alle drei Kanten gleich lang.', v,
                    f'round({K(wahr)}, 1)', einheit='cm')
    # quadratische Pyramide: Höhe aus Seitenhöhe und halber Grundkante
    p, q, r = (int(x) for x in R.choice(KLEIN))
    halb, h = (p, q) if R.random() < 0.5 else (q, p)
    return zahl(f'Eine quadratische Pyramide hat die Grundkante {2 * halb} cm und die Seitenhöhe (Höhe einer Seitenfläche) {r} cm. Wie hoch ist die Pyramide?',
                f'Rechtwinkliges Dreieck aus Höhe h, halber Grundkante {halb} cm und Seitenhöhe {r} cm: h² = {r * r} − {halb * halb} = {h * h}, h = {h} cm.',
                'Suche ein rechtwinkliges Dreieck im Inneren: Spitze, Mittelpunkt der Grundfläche, Mitte einer Grundkante.', h,
                f'({r} ** 2 - {halb} ** 2) / {h}', einheit='cm')


def g_anwendung(s):
    typ = R.random()
    if s == 1 or (s == 2 and typ < 0.4):
        if R.random() < 0.4:
            l = R.choice([3, Fr(7, 2), 4, Fr(9, 2), 5, 6, 7, 8])
            w = Fr(R.randint(5, int(l * 10 / 3)), 10)
            wahr = sqrt(float(l * l - w * w))
            v = gerundet(wahr, 2)
            if v is None: return None
            return zahl(f'Eine {dz(l)} m lange Leiter lehnt an einer senkrechten Wand. Ihr Fuß steht {dz(w)} m von der Wand entfernt. In welcher Höhe berührt sie die Wand? Runde auf zwei Nachkommastellen.',
                        f'h² = {dz(l)}² − {dz(w)}² = {dz(l * l)} − {dz(w * w)} = {dz(l * l - w * w)}, h ≈ {dz(v)} m.', 'Die Leiter ist die Hypotenuse.', v,
                        f'round({K(wahr)}, 2)', einheit='m')
        t = R.choice(TRIPEL)
        f = R.choice([Fr(1, 10), Fr(1, 5), Fr(1, 4), Fr(1, 2), Fr(1), Fr(3, 10), Fr(2, 5), Fr(1, 20)])
        a, b, c = (x * f for x in t)
        if not (2 <= c <= 10) or not all(endlich(x) and Fr(x).denominator <= 20 for x in (a, b, c)): return None
        if a > b: a, b = b, a
        if a > c / 3: return None
        l, w, h = c, a, b
        return zahl(f'Eine {dz(l)} m lange Leiter lehnt an einer senkrechten Wand. Ihr Fuß steht {dz(w)} m von der Wand entfernt. In welcher Höhe berührt sie die Wand?',
                    f'h² = {dz(l)}² − {dz(w)}² = {dz(l * l)} − {dz(w * w)} = {dz(h * h)}, h = {dz(h)} m.', 'Die Leiter ist die Hypotenuse.', h,
                    f'({cf(l)} ** 2 - {cf(w)} ** 2) / {cf(h)}', einheit='m')
    if s == 2:
        a, b, c = (int(x) for x in R.choice(KLEIN))
        if R.random() < 0.5:
            br_, ho = R.choice([(80, 60), (96, 54), (64, 48), (120, 90), (112, 63), (88, 66), (144, 81)])
            wahr = sqrt(br_ * br_ + ho * ho)
            if isqrt(br_ * br_ + ho * ho) ** 2 == br_ * br_ + ho * ho:
                d = isqrt(br_ * br_ + ho * ho)
                return zahl(f'Ein Fernseher hat einen {br_} cm breiten und {ho} cm hohen Bildschirm. Wie lang ist die Bildschirmdiagonale?',
                            f'd² = {br_}² + {ho}² = {dz(d * d)}, d = {d} cm.', 'Breite und Höhe sind die Katheten.', d,
                            f'({br_} ** 2 + {ho} ** 2) / {d}', einheit='cm')
            v = gerundet(wahr, 1)
            if v is None: return None
            return zahl(f'Ein Fernseher hat einen {br_} cm breiten und {ho} cm hohen Bildschirm. Wie lang ist die Bildschirmdiagonale? Runde auf eine Nachkommastelle.',
                        f'd² = {br_}² + {ho}² = {dz(br_ * br_ + ho * ho)}, d ≈ {dz(v)} cm.', 'Breite und Höhe sind die Katheten.', v,
                        f'round({K(wahr)}, 1)', einheit='cm')
        return zahl(f'Ein gleichschenkliges Dreieck hat die Basis {2 * a} cm und Schenkel von {c} cm. Wie hoch ist es (Höhe auf die Basis)?',
                    f'Die Höhe halbiert die Basis: h² = {c}² − {a}² = {b * b}, h = {b} cm.', 'Die Höhe teilt das Dreieck in zwei rechtwinklige Dreiecke.', b,
                    f'({c} ** 2 - {a} ** 2) / {b}', einheit='cm')
    if typ < 0.35:
        a = R.randint(2, 20)
        wahr = a * sqrt(3) / 2
        v = gerundet(wahr, 2)
        if v is None: return None
        return zahl(f'Wie hoch ist ein gleichseitiges Dreieck mit {a} cm Seitenlänge? Runde auf zwei Nachkommastellen.',
                    f'h² = {a}² − {dz(Fr(a, 2))}² = {dz(Fr(3 * a * a, 4))}, h ≈ {dz(v)} cm.', 'Die Höhe halbiert die Grundseite.', v,
                    f'round({K(wahr)}, 2)', einheit='cm')
    if typ < 0.7:
        L_ = R.choice([300, 400, 450, 500, 600, 800, 1000])
        h = R.randint(L_ // 40, L_ // 10)
        wahr = sqrt(L_ * L_ + h * h)
        v = gerundet(wahr, 0)
        if v is None: return None
        return zahl(f'Eine Rampe steigt auf {dz(L_)} cm waagrechter Länge um {h} cm an. Wie lang ist die Rampe? Runde auf ganze Zentimeter.',
                    f'l² = {dz(L_)}² + {h}² = {dz(L_ * L_ + h * h)}, l ≈ {dz(round(wahr, 1))} cm ≈ {dz(v)} cm.', 'Waagrechte Länge und Höhe sind die Katheten.', v,
                    f'round({K(wahr)}, 0)', einheit='cm')
    a, b, c = (int(x) for x in R.choice(KLEIN))
    k = R.choice([10, 20, 50, 100])
    gespart = (a + b - c) * k
    return zahl(f'Ein rechteckiger Platz ist {a * k} m lang und {b * k} m breit. Wie viele Meter spart man, wenn man diagonal statt an zwei Seiten entlang geht?',
                f'Diagonale: √({a * k}² + {b * k}²) = {c * k} m. Ersparnis: {a * k} + {b * k} − {c * k} = {gespart} m.',
                'Berechne die Diagonale und vergleiche mit dem Weg entlang der Seiten.', gespart,
                f'{a * k} + {b * k} - ({a * k} ** 2 + {b * k} ** 2) / {c * k}', einheit='m')


GEN = {'hypotenuse': g_hypotenuse, 'kathete': g_kathete, 'umkehrung': g_umkehrung, 'koordinaten': g_koordinaten,
       'raum': g_raum, 'anwendung': g_anwendung}

if __name__ == '__main__':
    bauen('trigo.pythagoras',
          'Den Satz des Pythagoras und seine Umkehrung anwenden: Längen in der Ebene, im Raum und im Koordinatensystem berechnen.',
          ['Im rechtwinkligen Dreieck: a² + b² = c² (c = Hypotenuse, gegenüber dem rechten Winkel).', 'Kathete gesucht: a² = c² − b².',
           'Umkehrung: a² + b² = c² für die längste Seite ⇒ rechtwinklig.', 'Abstand: d = √(Δx² + Δy²); Raumdiagonale: √(a² + b² + c²).'],
          [('Der Satz', ['hypotenuse', 'kathete', 'umkehrung']), ('Koordinaten und Raum', ['koordinaten', 'raum']),
           ('Anwenden', ['anwendung'])],
          ETAPPEN, GEN,
          meiden={'hypotenuse': ['a = 9 cm und b = 12 cm', 'a = 12 cm und b = 9 cm'], 'kathete': ['c = 13 cm und die Kathete b = 5 cm'],
                  'umkehrung': ['20 cm, 21 cm und 29 cm'], 'koordinaten': ['P(1 | 2) und Q(7 | 10)'], 'raum': ['Kanten 2 cm, 3 cm und 6 cm'],
                  'anwendung': ['5 m lange Leiter', 'Fuß steht 1,4 m']},
          offen=['Lernkarte „raum“: Das Bild ist ein mit „figur“ nachgebautes Schrägbild (echte Schrägbilder kann die App noch nicht); in den Aufgaben stehen die Quadermaße weiter in Worten.',
                 'Gerundete Ergebnisse: Der Wurzelwert steht als 12-stellige Konstante im Rechenausdruck c, weil das Prüfskript keine Wurzeln kennt.'])
