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

# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'hypotenuse': {
  'einstieg': 'Ein Gärtner legt ein Beet als Dreieck an: 9 m an der Hauswand entlang, 12 m am Zaun entlang, Hauswand und Zaun stehen im rechten Winkel. Wie lang wird die dritte, schräge Seite? Messen ist mühsam, rechnen geht schneller. Die Regel dafür heißt ⟦Satz des Pythagoras⟧.',
  'woerter': [['rechtwinkliges Dreieck', 'ein Dreieck mit einem 90°-Winkel'],
              ['Hypotenuse c', 'die längste Seite, sie liegt dem rechten Winkel gegenüber'],
              ['Katheten a, b', 'die beiden Seiten, die den rechten Winkel bilden'],
              ['a²', 'a · a, im Bild die Fläche des Quadrats über a'],
              ['√225', 'die Zahl, die mit sich selbst malgenommen 225 ergibt']],
  'schritte': ['Die Katheten sind 9 m und 12 m lang. Gesucht ist die Hypotenuse c.',
               'Beide Katheten quadrieren: 9² = 81 und 12² = 144.',
               'Die Quadrate addieren: c² = 81 + 144 = 225.',
               'Die Wurzel ziehen: c = √225 = ⟦15⟧. Die schräge Seite ist 15 m lang.'],
  'probe': '15 ist länger als beide Katheten ✓',
  'regel': 'So berechnest du die ⟦Hypotenuse⟧: Im ⟦rechtwinkligen⟧ Dreieck gilt ⟦a² + b² = c²⟧. Quadriere die ⟦Katheten⟧, addiere und zieh die Wurzel. Im Bild: Die beiden Quadrate über den Katheten haben ⟦zusammen genau so viel Fläche⟧ wie das Quadrat über der Hypotenuse.',
  'fehler': 'c = 9 + 12 = 21 ist falsch: Ein Umweg über zwei Seiten ist immer länger als der direkte Weg. Man addiert die ⟦Quadrate⟧ und zieht dann die Wurzel: √(81 + 144) = 15.'},
 'kathete': {
  'einstieg': 'Ein Brett von 13 dm Länge lehnt schräg an einer Kiste und ist am Boden 5 dm von ihr entfernt. Wie hoch reicht es an der Kiste? Jetzt ist die lange, schräge Seite bekannt und eine kurze gesucht. Man stellt den Satz des Pythagoras um und berechnet eine ⟦Kathete⟧.',
  'woerter': [['Kathete', 'eine der beiden Seiten am rechten Winkel'],
              ['umstellen', 'die Gleichung so umformen, dass das Gesuchte allein steht'],
              ['a² = c² − b²', 'Hypotenuse quadriert minus die bekannte Kathete quadriert']],
  'schritte': ['Die Hypotenuse ist 13 dm lang, eine Kathete 5 dm. Gesucht ist die andere Kathete a.',
               'Umstellen: a² = 13² − 5².',
               'Ausrechnen: a² = 169 − 25 = 144.',
               'Die Wurzel ziehen: a = √144 = ⟦12⟧. Das Brett reicht 12 dm hoch.'],
  'probe': '5² + 12² = 25 + 144 = 169 = 13² ✓',
  'regel': 'So berechnest du eine ⟦Kathete⟧: Ist die Hypotenuse bekannt, stellst du um: ⟦a² = c² − b²⟧. Die Kathete ist immer ⟦kürzer⟧ als die Hypotenuse.',
  'fehler': 'a² = 13² + 5² = 194 ist falsch: Dann wäre die Höhe länger als das Brett selbst. Gesucht ist eine ⟦Kathete⟧, also wird ⟦subtrahiert⟧. Das Ergebnis muss kleiner als 13 sein.'},
 'umkehrung': {
  'einstieg': 'Für ein Beet mit genauer Ecke spannt der Gärtner eine Schnur zu einem Dreieck mit 3 m, 4 m und 5 m. Weil 3² + 4² = 5² gilt, entsteht ein rechter Winkel. Der Satz des Pythagoras funktioniert also auch rückwärts. Das nennt man ⟦Umkehrung⟧.',
  'woerter': [['Umkehrung', 'der Satz rückwärts: Aus a² + b² = c² folgt der rechte Winkel'],
              ['längste Seite', 'sie muss die Rolle von c übernehmen'],
              ['gegenüber', 'auf der anderen Seite des Dreiecks']],
  'schritte': ['Ein Dreieck hat die Seiten 20 cm, 21 cm und 29 cm. Die längste Seite ist 29 cm, sie spielt die Rolle von c.',
               'Die kürzeren Seiten quadrieren und addieren: 20² + 21² = 400 + 441 = 841.',
               'Die längste Seite quadrieren: 29² = 841.',
               'Beide Zahlen sind gleich. Also ist das Dreieck ⟦rechtwinklig⟧; der rechte Winkel liegt gegenüber der 29-cm-Seite.'],
  'regel': 'So prüfst du mit der ⟦Umkehrung⟧: Nimm die ⟦längste⟧ Seite als c. Gilt a² + b² = c², ist das Dreieck rechtwinklig, und der rechte Winkel liegt ⟦gegenüber von c⟧.',
  'fehler': '6² + 10² = 136 ≠ 8² ⇒ „nicht rechtwinklig“ ist ein Fehlschluss: Man muss die ⟦längste⟧ Seite (10) als c nehmen: 6² + 8² = 100 = 10².'},
 'koordinaten': {
  'einstieg': 'Auf einem Stadtplan mit Kästchen liegt der Spielplatz bei P(1 | 2) und der Eisstand bei Q(7 | 10). Wie weit ist es Luftlinie? Man geht in Gedanken 6 Kästchen nach rechts und 8 nach oben – das ist ein rechtwinkliges Dreieck. Die Luftlinie ist der ⟦Abstand⟧ der beiden Punkte.',
  'woerter': [['Abstand d', 'die Länge der geraden Verbindung zwischen zwei Punkten'],
              ['Δx („Delta x“)', 'der Unterschied der x-Werte: x₂ − x₁'],
              ['Δy', 'der Unterschied der y-Werte: y₂ − y₁'],
              ['Steigungsdreieck', 'das rechtwinklige Dreieck aus waagrechtem und senkrechtem Weg']],
  'bild': {'typ': 'koordinaten', 'x': [0, 8], 'y': [0, 11], 'punkte': [{'x': 1, 'y': 2, 'name': 'Spielplatz P(1 | 2)'}, {'x': 7, 'y': 10, 'name': 'Eisstand Q(7 | 10)'}], 'strecken': [[1, 2, 7, 10], [1, 2, 7, 2, 'gestrichelt'], [7, 2, 7, 10, 'gestrichelt']]},
  'schritte': ['Gegeben: P(1 | 2) und Q(7 | 10).',
               'Waagrechter Weg: Δx = 7 − 1 = 6. Senkrechter Weg: Δy = 10 − 2 = 8. Das sind die Katheten.',
               'Pythagoras: d² = 6² + 8² = 36 + 64 = 100.',
               'Die Wurzel ziehen: d = √100 = ⟦10⟧ Kästchen.'],
  'regel': 'So berechnest du den ⟦Abstand⟧ von P(x₁ | y₁) und Q(x₂ | y₂): Bilde die Unterschiede Δx und Δy; sie sind die Katheten. Dann ⟦d = √((x₂ − x₁)² + (y₂ − y₁)²)⟧.',
  'fehler': 'd = √(7² + 10²) mit den Koordinaten von Q ist falsch: Das wäre der Weg vom Ursprung (0 | 0) zum Eisstand. Man braucht die ⟦Unterschiede⟧ der Koordinaten.'},
 'raum': {
  'einstieg': 'Passt ein 7 cm langer Stift schräg in eine Schachtel von 2 cm × 3 cm × 6 cm? Die längste Strecke geht von einer unteren Ecke zur gegenüberliegenden oberen Ecke quer durch den Raum. Sie heißt ⟦Raumdiagonale⟧ und lässt sich mit zweimal Pythagoras berechnen.',
  'woerter': [['Quader', 'ein Körper wie eine Schachtel mit rechteckigen Seiten'],
              ['Kanten a, b, c', 'Länge, Breite und Höhe'],
              ['Flächendiagonale', 'die schräge Linie über eine Seitenfläche, hier über den Boden'],
              ['Raumdiagonale', 'die Linie quer durch den Körper von Ecke zu gegenüberliegender Ecke']],
  'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [3, 0], 'C': [3.71, 0.71], 'D': [0.71, 0.71], 'E': [0, 6], 'F': [3, 6], 'G': [3.71, 6.71], 'H': [0.71, 6.71]}, 'linien': [['A', 'B', '3 cm'], ['B', 'F', '6 cm'], ['F', 'E'], ['E', 'A'], ['B', 'C', '2 cm'], ['C', 'G'], ['G', 'F'], ['E', 'H'], ['H', 'G'], ['A', 'D', '', 'gestrichelt'], ['D', 'C', '', 'gestrichelt'], ['D', 'H', '', 'gestrichelt'], ['A', 'G', 'Raumdiagonale d = ?'], ['A', 'C', 'Bodendiagonale √13', 'gestrichelt']]},
  'schritte': ['Die Schachtel ist 2 cm × 3 cm × 6 cm groß.',
               'Erst die Bodendiagonale: Ihr Quadrat ist 2² + 3² = 4 + 9 = 13.',
               'Bodendiagonale und Höhe bilden einen rechten Winkel: d² = 13 + 6² = 13 + 36 = 49.',
               'Die Wurzel ziehen: d = √49 = ⟦7 cm⟧. Der Stift passt genau.'],
  'probe': '2² + 3² + 6² = 4 + 9 + 36 = 49 = 7² ✓',
  'regel': 'So rechnest du im Quader mit Kanten a, b, c: Suche ein ⟦rechtwinkliges Dreieck⟧ im Körper. Die Flächendiagonale ist ⟦√(a² + b²)⟧, die Raumdiagonale ⟦√(a² + b² + c²)⟧.',
  'fehler': 'Raumdiagonale = √(2² + 3²) ist nur die ⟦Bodendiagonale⟧ – sie liegt flach am Boden. Die Höhe 6 cm muss auch quadriert und dazugezählt werden.'},
 'anwendung': {
  'einstieg': 'Zum Obstpflücken lehnt eine 5 m lange Leiter an der Hauswand, ihr Fuß steht 1,4 m von der Wand weg. Wie hoch reicht sie? Wand und Boden bilden einen rechten Winkel, die Leiter ist die schräge Seite. So hilft ⟦Pythagoras im Alltag⟧.',
  'woerter': [['Skizze', 'eine schnelle Zeichnung mit allen bekannten Längen'],
              ['h', 'die gesuchte Höhe an der Wand'],
              ['sinnvoll runden', 'so viele Stellen angeben, wie man im Alltag messen kann']],
  'schritte': ['Skizze: Wand und Boden bilden den rechten Winkel. Die Leiter (5 m) liegt ihm gegenüber, sie ist die Hypotenuse.',
               'Gesucht ist die Kathete h an der Wand: h² = 5² − 1,4².',
               'Ausrechnen: h² = 25 − 1,96 = 23,04.',
               'Die Wurzel ziehen: h = √23,04 = ⟦4,8 m⟧. So hoch reicht das obere Ende.'],
  'probe': '1,4² + 4,8² = 1,96 + 23,04 = 25 ✓',
  'regel': 'So gehst du im Alltag vor: ⟦Skizze⟧ machen, den ⟦rechten Winkel⟧ suchen, die Hypotenuse bestimmen (gegenüber vom rechten Winkel), dann a² + b² = c² passend umstellen. Am Ende ⟦sinnvoll runden⟧.',
  'fehler': 'h² = 5² + 1,4² ist falsch: Dann wäre die Höhe größer als die Leiter lang ist. Die ⟦Leiter⟧ liegt gegenüber dem rechten Winkel zwischen Wand und Boden, sie ist die Hypotenuse.'},
}
klar(ETAPPEN, KLAR)
# ---- KLAR ENDE ----
# ---- UMBAU (neues Muster, Runde 8, Vorgabe 16.11.) ----
_H = {"C": [0, 0], "A": [12, 0], "B": [0, 9], "_a1": [-9, 0], "_a2": [-9, 9], "_b1": [0, -12], "_b2": [12, -12], "_c1": [21, 12], "_c2": [9, 21]}
def _drei(c): return [["A", "B", c], ["B", "C", "a = 9"], ["C", "A", "b = 12"]]
_QA = [["C", "_a1"], ["_a1", "_a2", "a² = 81"], ["_a2", "B"], ["C", "_b1"], ["_b1", "_b2", "b² = 144"], ["_b2", "A"]]
_QC = [["A", "_c1"], ["_c1", "_c2", "c² = 225"], ["_c2", "B"]]
_K = {'_C': [0, 0], '_A': [5, 0], '_B': [0, 12]}
def _kist(a): return [['_C', '_A', 'Boden 5'], ['_C', '_B', a], ['_A', '_B', 'Brett 13']]
_U = {'_C': [0, 0], '_A': [21, 0], '_B': [0, 20]}
_UL = [['_C', '_A', '21 cm'], ['_C', '_B', '20 cm'], ['_A', '_B', '29 cm']]
_Q = {'A': [0, 0], 'B': [3, 0], 'C': [3.71, 0.71], 'D': [0.71, 0.71], 'E': [0, 6], 'F': [3, 6], 'G': [3.71, 6.71], 'H': [0.71, 6.71]}
_QL = [['A', 'B', '3 cm'], ['B', 'F', '6 cm'], ['F', 'E'], ['E', 'A'], ['B', 'C', '2 cm'], ['C', 'G'], ['G', 'F'], ['E', 'H'], ['H', 'G'],
       ['A', 'D', '', 'gestrichelt'], ['D', 'C', '', 'gestrichelt'], ['D', 'H', '', 'gestrichelt']]
_L = {'_F': [0, 0], 'W': [0, 4.8], 'B': [1.4, 0]}
def _leiter(h): return [['_F', 'B', '1,4 m'], ['_F', 'W', h], ['W', 'B', 'Leiter 5 m']]
UMBAU = {
 'hypotenuse': {
  'einstieg': 'Ein dreieckiges Beet hat eine rechte Ecke. Die Seiten daran sind 9 m und 12 m lang. Wie lang ist die schräge Seite? Das sagt der ⟦Satz des Pythagoras⟧.',
  'woerter': [['Hypotenuse', 'die längste Seite, gegenüber dem rechten Winkel'],
              ['Katheten', 'die beiden Seiten am rechten Winkel'],
              ['a²', 'a · a, im Bild die Fläche des Quadrats über a']],
  'bild': {'typ': 'figur', 'punkte': _H, 'flaeche': ['A', 'B', 'C'], 'linien': _drei('c = ?'), 'rechter_winkel': [['C', 'A', 'B']]},
  'schritte': [{'text': 'Die Katheten sind 9 m und 12 m. Gesucht ist die Hypotenuse c.'},
               {'text': 'Quadrate über den Katheten: a² = 81 und b² = 144.', 'bild': {'linien': _drei('c = ?') + _QA}},
               {'text': 'Zusammen ergeben sie das Quadrat über c: c² = 225.', 'bild': {'linien': _drei('c = ?') + _QA + _QC}},
               {'text': 'Wurzel ziehen: c = √225 = ⟦15 m⟧.', 'bild': {'linien': _drei('c = 15') + _QA + _QC}}],
  'fehler': 'c ist nicht 9 + 12 = 21 m. Der Umweg über zwei Seiten ist immer länger als der direkte Weg.',
  'regel': 'Im rechtwinkligen Dreieck gilt ⟦a² + b² = c²⟧. c ist die Hypotenuse, gegenüber dem rechten Winkel.'},
 'kathete': {
  'einstieg': 'Ein 13 dm langes Brett lehnt schräg an einer Kiste. Unten steht es 5 dm von ihr weg. Wie hoch reicht es? Jetzt suchst du eine ⟦Kathete⟧.',
  'woerter': [['Kathete', 'eine der beiden Seiten am rechten Winkel'],
              ['umstellen', 'die Gleichung so umformen, dass das Gesuchte allein steht']],
  'bild': {'typ': 'figur', 'punkte': _K, 'flaeche': ['_C', '_A', '_B'], 'linien': _kist('a = ?'), 'rechter_winkel': [['_C', '_A', '_B']]},
  'schritte': [{'text': 'Hypotenuse 13 dm, eine Kathete 5 dm. Gesucht ist die Höhe a.'},
               {'text': 'Umstellen: a² = 13² − 5² = 169 − 25 = 144.'},
               {'text': 'Wurzel ziehen: a = √144 = ⟦12 dm⟧.', 'bild': {'linien': _kist('a = 12')}}],
  'fehler': 'a² = 13² + 5² ist falsch. Dann wäre die Höhe größer als das Brett lang ist. Bei einer Kathete wird abgezogen.',
  'fehler_bild': {'linien': _kist('a = 13,9?')},
  'regel': 'Für eine Kathete gilt ⟦a² = c² − b²⟧. Die Kathete ist immer kürzer als die Hypotenuse.'},
 'umkehrung': {
  'einstieg': 'Ein Gärtner spannt eine Schnur zum Dreieck mit 3 m, 4 m und 5 m. Weil 3² + 4² = 5², entsteht ein rechter Winkel. Das ist die ⟦Umkehrung⟧.',
  'woerter': [['Umkehrung', 'der Satz rückwärts: aus a² + b² = c² folgt der rechte Winkel'],
              ['längste Seite', 'sie übernimmt die Rolle von c']],
  'bild': {'typ': 'figur', 'punkte': _U, 'flaeche': ['_C', '_A', '_B'], 'linien': _UL},
  'schritte': [{'text': 'Seiten 20 cm, 21 cm und 29 cm. Die längste Seite: 29 cm.'},
               {'text': '20² + 21² = 400 + 441 = 841.'},
               {'text': '29² = 841. Beide Zahlen sind gleich.'},
               {'text': 'Also ist das Dreieck ⟦rechtwinklig⟧, gegenüber von 29 cm.', 'bild': {'rechter_winkel': [['_C', '_A', '_B']]}}],
  'fehler': 'Bei 6, 8 und 10 cm nicht 6² + 10² mit 8² vergleichen. Die längste Seite 10 ist c: 36 + 64 = 100.',
  'regel': 'Gilt a² + b² = c² für die längste Seite c: ⟦rechtwinklig⟧. Der rechte Winkel liegt gegenüber von c.'},
 'koordinaten': {
  'einstieg': 'Auf dem Stadtplan liegt der Spielplatz bei P(1 | 2). Der Eisstand ist bei Q(7 | 10). Wie weit ist es Luftlinie? Das ist der ⟦Abstand⟧ der Punkte.',
  'woerter': [['Abstand', 'die Länge der geraden Verbindung zweier Punkte'],
              ['Δx', 'der Unterschied der x-Werte'],
              ['Δy', 'der Unterschied der y-Werte']],
  'bild': {'typ': 'koordinaten', 'x': [0, 8], 'y': [0, 11],
           'punkte': [{'x': 1, 'y': 2, 'name': 'P Spielplatz'}, {'x': 7, 'y': 10, 'name': 'Q Eis'}]},
  'schritte': [{'text': 'Waagrecht: Δx = 7 − 1 = 6 Kästchen.', 'bild': {'strecken': [[1, 2, 7, 2, 'gestrichelt']]}},
               {'text': 'Senkrecht: Δy = 10 − 2 = 8 Kästchen.', 'bild': {'strecken': [[1, 2, 7, 2, 'gestrichelt'], [7, 2, 7, 10, 'gestrichelt']]}},
               {'text': 'Pythagoras: d² = 6² + 8² = 36 + 64 = 100.',
                'bild': {'strecken': [[1, 2, 7, 2, 'gestrichelt'], [7, 2, 7, 10, 'gestrichelt'], [1, 2, 7, 10]]}},
               {'text': 'Also ⟦d = 10⟧ Kästchen Luftlinie.'}],
  'fehler': 'd = √(7² + 10²) ist falsch. Das wäre der Weg vom Nullpunkt zum Eisstand. Man braucht die Unterschiede.',
  'fehler_bild': {'strecken': [[0, 0, 7, 10, 'gestrichelt']]},
  'regel': 'Bilde ⟦Δx und Δy⟧, dann Pythagoras. d = √((x₂ − x₁)² + (y₂ − y₁)²).'},
 'raum': {
  'einstieg': 'Eine Schachtel ist 2 cm × 3 cm × 6 cm groß. Passt ein 7 cm langer Stift schräg hinein? Die längste Strecke ist die ⟦Raumdiagonale⟧.',
  'woerter': [['Raumdiagonale', 'die Strecke quer durch den Körper, von Ecke zu Ecke'],
              ['Bodendiagonale', 'die schräge Strecke über den Boden'],
              ['Quader', 'ein Körper wie eine Schachtel']],
  'bild': {'typ': 'figur', 'punkte': _Q, 'linien': _QL},
  'schritte': [{'text': 'Erst die Bodendiagonale: Ihr Quadrat ist 2² + 3² = 13.',
                'bild': {'linien': _QL + [['A', 'C', '√13', 'gestrichelt']]}},
               {'text': 'Bodendiagonale und Höhe 6 cm bilden einen rechten Winkel.'},
               {'text': 'd² = 13 + 6² = 49, also ⟦d = 7 cm⟧.',
                'bild': {'linien': _QL + [['A', 'C', '√13', 'gestrichelt'], ['A', 'G', 'd = 7']]}},
               {'text': 'Der Stift passt genau schräg in den Quader.'}],
  'fehler': '√(2² + 3²) ist nur die Bodendiagonale. Sie liegt flach am Boden. Die Höhe 6 cm fehlt noch.',
  'regel': 'Raumdiagonale: ⟦√(a² + b² + c²)⟧. Suche dafür ein rechtwinkliges Dreieck im Körper.'},
 'anwendung': {
  'einstieg': 'Zum Obstpflücken lehnt eine 5 m lange Leiter an der Hauswand. Ihr Fuß steht 1,4 m von der Wand weg. Wie hoch reicht sie? Das ist ⟦Pythagoras im Alltag⟧.',
  'woerter': [['Skizze', 'eine schnelle Zeichnung mit allen bekannten Längen'],
              ['h', 'die gesuchte Höhe an der Wand']],
  'bild': {'typ': 'figur', 'punkte': _L, 'linien': _leiter('h = ?'), 'rechter_winkel': [['_F', 'B', 'W']]},
  'schritte': [{'text': 'Skizze: Wand und Boden bilden den rechten Winkel. Die Leiter ist die Hypotenuse.'},
               {'text': 'h² = 5² − 1,4² = 25 − 1,96 = 23,04.'},
               {'text': 'h = √23,04 = ⟦4,8 m⟧.', 'bild': {'linien': _leiter('h = 4,8 m')}}],
  'fehler': 'h² = 5² + 1,4² ist falsch. Dann wäre die Höhe größer als die Leiter lang ist.',
  'fehler_bild': {'linien': _leiter('h = 5,2?')},
  'regel': 'Erst die ⟦Hypotenuse⟧ finden, dann passend umstellen. Am Ende sinnvoll runden.'},
}
umbau(ETAPPEN, UMBAU)
# ---- UMBAU ENDE ----


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

# ---------- Zehnte Runde (schwer-kl9): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Abschnitt mit eigenem festen Zufallsstart (anhaengen(..., 9910, ...)), läuft erst nach bauen():
# alle bisherigen Aufgaben bleiben unverändert. Vorbilder: Bayerischer Mathematik-Test 10 2009 (Strecke der Länge √n
# mit Pythagoras), Illustrierende Aufgaben Realschule 9 (I) (Tangentenabschnitt am Kreis, Drahtmodell einer Pyramide,
# Punkte mit Abstand 5 vom Ursprung), Abschlussprüfung Realschule Bayern Mathematik II 2024 (rechnerisch zeigen, dass ein
# Dreieck rechtwinklig ist, und den rechten Winkel angeben), MSA Berlin/Brandenburg 2011 (Fähre). Zahlen und Wortlaut eigen.
from _schwer_kl9 import anhaengen  # noqa: E402
from _kl9 import K as _K  # noqa: E402


def schwer():
    P, Kn, O = 'pruefung', 'knobel', ''
    zoll = (80 ** 2 + 45 ** 2) ** 0.5 / 2.54
    return [
        # hypotenuse
        ('hypotenuse', 3, P, luecken('Ein rechtwinkliges Dreieck mit ganzzahligen Katheten (in cm) soll eine Hypotenuse der Länge √13 cm haben. Welche Katheten passen?', '□ cm und □ cm',
                                     'kleinere Kathete zuerst', [2, 3], 'c² = 13 = 4 + 9 = 2² + 3². Also Katheten 2 cm und 3 cm.',
                                     'Zerlege 13 in eine Summe von zwei Quadratzahlen.', ['2', '3'])),
        ('hypotenuse', 3, P, zahl('Ein Fernseher hat ein 80 cm breites und 45 cm hohes Bild. Die Größe wird als Bilddiagonale in Zoll angegeben (1 Zoll = 2,54 cm). Wie viele Zoll sind es? Runde auf ganze Zoll.',
                                  'd = √(80² + 45²) = √8 425 ≈ 91,8 cm. 91,8 : 2,54 ≈ 36 Zoll.', 'Erst die Diagonale in cm, dann in Zoll umrechnen.', round(zoll), f'round({_K(zoll)}, 0)',
                                  einheit='Zoll')),
        ('hypotenuse', 3, Kn, zahl('In einem rechtwinkligen Dreieck stehen die Katheten im Verhältnis 3 : 4. Die Hypotenuse ist 35 cm lang. Wie lang ist die kürzere Kathete?',
                                   'Katheten 3k und 4k: (3k)² + (4k)² = 25k², Hypotenuse 5k = 35 ⇒ k = 7. Kürzere Kathete 3 · 7 = 21 cm.',
                                   'Setze die Katheten als 3k und 4k an. Was ergibt sich für die Hypotenuse?', 21, '3 * 35 / 5', einheit='cm')),
        ('hypotenuse', 3, O, zahl('Ein Rechteck hat 34 cm Umfang, eine Seite ist 5 cm lang. Wie lang ist die Diagonale?', 'Andere Seite: 34 : 2 − 5 = 12 cm. d = √(25 + 144) = √169 = 13 cm.',
                                  'Bestimme zuerst die zweite Seite aus dem Umfang.', 13, '(5 ** 2 + 12 ** 2) / 13', einheit='cm')),
        ('hypotenuse', 2, O, zahl('Ein rechtwinkliges Dreieck hat die Katheten 0,9 m und 1,2 m. Wie lang ist die Hypotenuse?', 'c² = 0,81 + 1,44 = 2,25, c = 1,5 m.',
                                  'Quadriere die Kommazahlen sorgfältig.', 1.5, '(0.81 + 1.44) / 1.5', einheit='m')),
        ('hypotenuse', 2, O, zahl('Ein rechtwinkliges Dreieck hat die Katheten 33 cm und 56 cm. Wie lang ist die Hypotenuse?', 'c² = 1 089 + 3 136 = 4 225, c = 65 cm.',
                                  'Quadrate addieren, dann Wurzel ziehen.', 65, '(33 ** 2 + 56 ** 2) / 65', einheit='cm')),
        # kathete
        ('kathete', 3, P, zahl('Ein Punkt P ist 25 cm vom Mittelpunkt M eines Kreises mit r = 7 cm entfernt. Von P aus verläuft eine Tangente, die den Kreis in B berührt. Wie lang ist PB?',
                               'Der Radius MB steht senkrecht auf der Tangente. Im Dreieck MBP ist PM die Hypotenuse: PB² = 25² − 7² = 576, PB = 24 cm.',
                               'Wo ist der rechte Winkel? Der Radius zum Berührpunkt steht senkrecht auf der Tangente.', 24, '(25 ** 2 - 7 ** 2) / 24', einheit='cm')),
        ('kathete', 3, P, zahl('Ein gleichschenkliges Dreieck hat die Basis 16 cm und zwei Schenkel von je 17 cm. Wie groß ist sein Flächeninhalt?',
                               'Die Höhe halbiert die Basis: h² = 17² − 8² = 289 − 64 = 225, h = 15 cm. A = 16 · 15 : 2 = 120 cm².',
                               'Zeichne die Höhe ein: Sie teilt das Dreieck in zwei rechtwinklige Dreiecke.', 120, '16 * 15 / 2', einheit='cm²')),
        ('kathete', 3, Kn, zahl('Eine 2,5 m lange Leiter lehnt an einer Wand; ihr Fuß steht 0,7 m von der Wand. Der Fuß rutscht 0,8 m weiter weg. Um wie viele Meter sinkt die Oberkante?',
                                'Vorher: h² = 6,25 − 0,49 = 5,76, h = 2,4 m. Nachher (Fuß 1,5 m): h² = 6,25 − 2,25 = 4, h = 2 m. Die Oberkante sinkt um 0,4 m.',
                                'Rechne die Höhe vorher und nachher aus.', 0.4, '(5.76 / 2.4) - (4 / 2)', einheit='m')),
        ('kathete', 3, O, zahl('Ein Rechteck hat eine 26 cm lange Diagonale und eine 10 cm lange Seite. Wie groß ist sein Flächeninhalt?', 'Andere Seite: √(676 − 100) = √576 = 24 cm. A = 10 · 24 = 240 cm².',
                               'Die Diagonale ist die Hypotenuse.', 240, '10 * ((26 ** 2 - 10 ** 2) / 24)', einheit='cm²')),
        ('kathete', 2, O, zahl('Hypotenuse 6,5 cm, eine Kathete 2,5 cm. Wie lang ist die andere Kathete?', 'a² = 42,25 − 6,25 = 36, a = 6 cm.', 'Bei der Kathete wird subtrahiert.', 6,
                               '(6.5 ** 2 - 2.5 ** 2) / 6', einheit='cm')),
        ('kathete', 2, O, zahl('Hypotenuse 41 cm, eine Kathete 9 cm. Wie lang ist die andere Kathete?', 'a² = 1 681 − 81 = 1 600, a = 40 cm.', 'c² − b², dann Wurzel.', 40,
                               '(41 ** 2 - 9 ** 2) / 40', einheit='cm')),
        # umkehrung
        ('umkehrung', 3, P, auswahl('Gegeben ist das Dreieck mit A(0 | 0), B(6 | 2) und C(4 | 8). Ist es rechtwinklig? Wenn ja: Wo liegt der rechte Winkel?', 'Ja, bei B.',
                                    ['Ja, bei A.', 'Ja, bei C.', 'Nein.'],
                                    'AB² = 36 + 4 = 40, BC² = 4 + 36 = 40, AC² = 16 + 64 = 80. 40 + 40 = 80: rechtwinklig, der rechte Winkel liegt gegenüber der längsten Seite AC, also bei B.',
                                    'Berechne die drei Seitenquadrate mit Δx und Δy.')),
        ('umkehrung', 3, P, auswahl('Ein Dreieck hat die Seiten 15 cm, 36 cm und 39 cm. Welche Begründung zeigt, dass es rechtwinklig ist?', '15² + 36² = 225 + 1 296 = 1 521 = 39²',
                                    ['15 + 36 > 39', 'Alle drei Zahlen sind durch 3 teilbar.', '39 − 36 = 15 − 12'],
                                    'Nach der Umkehrung des Satzes von Pythagoras genügt: Die Quadrate der beiden kürzeren Seiten ergeben zusammen das Quadrat der längsten.',
                                    'Welche Bedingung prüft man mit der Umkehrung des Pythagoras?')),
        ('umkehrung', 3, Kn, zahl('Wie viele rechtwinklige Dreiecke mit ganzzahligen Seiten gibt es, bei denen eine Kathete genau 5 cm lang ist?',
                                  'Mit der zweiten Kathete b und Hypotenuse c: 25 = c² − b² = (c − b)(c + b). Nur 1 · 25 passt (c > b): c − b = 1, c + b = 25 ⇒ b = 12, c = 13. Genau ein Dreieck (5, 12, 13).',
                                  'Schreibe 5² = c² − b² als Produkt (c − b)(c + b) und probiere die Teiler von 25.', 1, '(25 - 1) // 24')),
        ('umkehrung', 3, O, auswahl('Ist das Dreieck mit den Seiten 2,5 cm, 6 cm und 6,5 cm rechtwinklig?', 'Ja, der rechte Winkel liegt gegenüber der 6,5-cm-Seite.',
                                    ['Nein, 2,5² + 6² ≠ 6,5².', 'Ja, der rechte Winkel liegt gegenüber der 6-cm-Seite.', 'Das kann man nur durch Messen entscheiden.'],
                                    '2,5² + 6² = 6,25 + 36 = 42,25 = 6,5². Der rechte Winkel liegt gegenüber der längsten Seite.', 'Rechne die Quadrate mit Kommazahlen aus.')),
        ('umkehrung', 2, O, auswahl('Ist ein Dreieck mit den Seiten 8 cm, 15 cm und 17 cm rechtwinklig?', 'Ja, denn 8² + 15² = 289 = 17².', ['Nein, denn 8 + 15 ≠ 17.', 'Nein, denn 8² + 17² ≠ 15².'],
                                    '64 + 225 = 289 = 17².', 'Vergleiche mit dem Quadrat der längsten Seite.')),
        ('umkehrung', 2, O, auswahl('Ist ein Dreieck mit den Seiten 6 cm, 7 cm und 9 cm rechtwinklig?', 'Nein, denn 6² + 7² = 85 ≠ 81 = 9².', ['Ja, denn 6 + 7 > 9.', 'Ja, denn 6² + 9² = 117 > 49.'],
                                    '36 + 49 = 85 ≠ 81. Also nicht rechtwinklig.', 'Längste Seite ist 9 cm.')),
        # koordinaten
        ('koordinaten', 3, P, auswahl('Welcher Punkt hat vom Ursprung O(0 | 0) genau den Abstand 5?', '(3 | −4)', ['(2 | 3)', '(4 | 4)', '(5 | 5)'],
                                      '3² + (−4)² = 9 + 16 = 25, also Abstand 5. (2 | 3): √13; (4 | 4): √32; (5 | 5): √50.', 'Rechne x² + y² und vergleiche mit 25.')),
        ('koordinaten', 3, P, zahl('Ein Dreieck hat die Ecken A(−2 | 1), B(4 | 1) und C(1 | 5). Welchen Umfang hat es (Einheit 1 cm)?',
                                   'AB = 6 (waagrecht). AC = √(3² + 4²) = 5, BC = √(3² + 4²) = 5. Umfang 6 + 5 + 5 = 16 cm.', 'Jede Seite einzeln mit Δx und Δy berechnen.', 16, '6 + 5 + 5',
                                   einheit='cm')),
        ('koordinaten', 3, Kn, zahl('Wie viele Punkte mit ganzzahligen Koordinaten haben vom Ursprung genau den Abstand 5?',
                                    'x² + y² = 25: (±5 | 0), (0 | ±5) sind 4 Punkte; (±3 | ±4) und (±4 | ±3) sind 8 Punkte. Zusammen 12.',
                                    'Zerlege 25 in zwei Quadratzahlen und denke an alle Vorzeichen.', 12, '4 + 8')),
        ('koordinaten', 3, O, zahl('Der Punkt P(2 | y) ist 10 Einheiten von Q(−4 | 3) entfernt, und y > 3. Bestimme y.', 'Δx = 6. Δy² = 100 − 36 = 64, Δy = 8. y = 3 + 8 = 11.',
                                   'Stelle die Abstandsformel mit Δy als Unbekannter auf.', 11, '3 + 8')),
        ('koordinaten', 2, O, zahl('Berechne den Abstand von A(−1 | −1) und B(5 | 7).', 'Δx = 6, Δy = 8, d = √(36 + 64) = 10.', 'Δx und Δy, dann Pythagoras.', 10, '(36 + 64) / 10')),
        ('koordinaten', 2, O, zahl('Berechne den Abstand von O(0 | 0) und Q(5 | 12).', 'd = √(25 + 144) = √169 = 13.', 'Pythagoras mit den Koordinaten als Katheten.', 13, '(25 + 144) / 13')),
        # raum
        ('raum', 3, P, auswahl('Aus Draht soll ein Kantenmodell einer quadratischen Pyramide gebaut werden: Grundkante 6 cm, Höhe 4 cm. Reichen 45 cm Draht?', 'Nein, man braucht etwa 47,3 cm.',
                               ['Ja, man braucht nur 40 cm (4 · 6 + 4 · 4).', 'Ja, man braucht etwa 44 cm.', 'Nein, man braucht etwa 58 cm.'],
                               'Halbe Grunddiagonale: √(3² + 3²) = √18. Seitenkante: √(18 + 16) = √34 ≈ 5,83 cm. Draht: 4 · 6 + 4 · 5,83 ≈ 47,3 cm > 45 cm. Falle: Die Höhe ist keine Kante.',
                               'Die Seitenkanten sind länger als die Höhe. Finde ein rechtwinkliges Dreieck mit Höhe und halber Diagonale.')),
        ('raum', 3, P, zahl('Ein Quader ist 12 cm lang, 4 cm breit und 3 cm hoch. Wie lang ist seine Raumdiagonale?', 'd² = 144 + 16 + 9 = 169, d = 13 cm.',
                            'Erst die Bodendiagonale, dann mit der Höhe.', 13, '(144 + 16 + 9) / 13', einheit='cm')),
        ('raum', 3, Kn, zahl('Eine Ameise läuft auf der Oberfläche eines Würfels (Kante 10 cm) von einer Ecke zur gegenüberliegenden Ecke. Wie lang ist der kürzeste Weg? Runde auf eine Nachkommastelle.',
                             'Klappe zwei Seitenflächen in eine Ebene: Es entsteht ein Rechteck 20 cm × 10 cm. Kürzester Weg = Diagonale: √(400 + 100) = √500 ≈ 22,4 cm (kürzer als 10 + 14,1 über die Kante).',
                             'Denke dir den Würfel aufgeklappt (Netz). Die Ameise läuft dann geradeaus.', round(500 ** 0.5, 1), f'round({_K(500 ** 0.5)}, 1)', einheit='cm')),
        ('raum', 3, O, zahl('Ein zylinderförmiger Becher hat innen 6 cm Durchmesser und ist 8 cm hoch. Wie lang darf ein Strohhalm höchstens sein, damit er ganz im Becher liegt?',
                            'Längste Strecke: vom Rand unten schräg zum gegenüberliegenden Rand oben: √(6² + 8²) = 10 cm.', 'Schneide den Becher in Gedanken senkrecht durch die Mitte.', 10,
                            '(36 + 64) / 10', einheit='cm')),
        ('raum', 2, O, zahl('Wie lang ist die Raumdiagonale eines Quaders mit 1 cm, 4 cm und 8 cm Kantenlänge?', 'd² = 1 + 16 + 64 = 81, d = 9 cm.', 'd² = a² + b² + c².', 9, '81 / 9',
                            einheit='cm')),
        ('raum', 2, O, zahl('Wie lang ist die Diagonale einer Würfelfläche bei 5 cm Kantenlänge? Runde auf zwei Nachkommastellen.', 'd = √(25 + 25) = √50 ≈ 7,07 cm.', 'Die Fläche ist ein Quadrat.',
                            round(50 ** 0.5, 2), f'round({_K(50 ** 0.5)}, 2)', einheit='cm')),
        # anwendung
        ('anwendung', 3, P, zahl('Eine Fähre fährt quer über einen 300 m breiten Fluss und wird dabei 400 m flussabwärts getrieben. Wie lang ist ihr Weg (als gerade Strecke)?',
                                 'Flussbreite und Abdrift stehen senkrecht: s = √(300² + 400²) = 500 m.', 'Skizze: Wo ist der rechte Winkel?', 500, '(300 ** 2 + 400 ** 2) / 500', einheit='m')),
        ('anwendung', 3, P, zahl('In einem Kreis mit Radius 13 cm ist eine Sehne 24 cm lang. Wie weit ist sie vom Mittelpunkt entfernt?',
                                 'Das Lot vom Mittelpunkt halbiert die Sehne: d² = 13² − 12² = 25, d = 5 cm.', 'Verbinde M mit einem Sehnenende. Halbe Sehne, Abstand und Radius bilden ein rechtwinkliges Dreieck.',
                                 5, '(169 - 144) / 5', einheit='cm')),
        ('anwendung', 3, Kn, zahl('Ein 10 m hoher Baum knickt bei einem Sturm. Die Spitze berührt 4 m vom Stamm entfernt den Boden; der stehende Teil ist senkrecht. In welcher Höhe ist der Baum geknickt?',
                                  'Höhe h, abgeknickter Teil 10 − h: h² + 4² = (10 − h)² ⇒ 16 = 100 − 20h ⇒ h = 4,2 m.', 'Der umgeknickte Teil ist die Hypotenuse. Er ist 10 − h lang.', 4.2,
                                  '(100 - 16) / 20', einheit='m')),
        ('anwendung', 3, O, zahl('Eine Raute hat die Diagonalen 12 cm und 16 cm. Wie lang ist eine Seite?', 'Die Diagonalen halbieren sich senkrecht: s = √(6² + 8²) = 10 cm.',
                                 'In der Raute stehen die Diagonalen senkrecht aufeinander und halbieren sich.', 10, '(36 + 64) / 10', einheit='cm')),
        ('anwendung', 2, O, zahl('Eine 6,5 m lange Leiter steht unten 2,5 m von der Wand entfernt. Wie hoch reicht sie?', 'h² = 42,25 − 6,25 = 36, h = 6 m.', 'Die Leiter ist die Hypotenuse.', 6,
                                 '(6.5 ** 2 - 2.5 ** 2) / 6', einheit='m')),
        ('anwendung', 2, O, zahl('Ein Quadrat hat eine 10 cm lange Diagonale. Wie groß ist sein Flächeninhalt?', 'a² + a² = 100 ⇒ a² = 50. Der Flächeninhalt ist a² = 50 cm².',
                                 'Du brauchst a² – nicht a selbst.', 50, '10 ** 2 / 2', einheit='cm²')),
    ]


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('trigo.pythagoras', 13_9_10)
# c) Lösung 600 cm = waagrechte Länge – bestätigt die Fehlvorstellung „kein Unterschied“ → größere Steigung
BF.ersetze('anwendung', 'Eine Rampe steigt auf 600 cm waagrechter Länge um 17 cm an. Wie lang ist die Rampe? Runde auf ganze Zentimeter.', BF.Z(
    'Eine Rampe steigt auf 240 cm waagrechter Länge um 70 cm an. Wie lang ist die Rampe?', 250, '(240 ** 2 + 70 ** 2) / 250',
    'l² = 240² + 70² = 57 600 + 4 900 = 62 500, l = √62 500 = 250 cm. Die Rampe ist 10 cm länger als ihre waagrechte Länge.',
    'Waagrechte Länge und Höhe sind die Katheten.', einheit='cm'))
# a) Routine (Katheten gegeben, Hypotenuse runden) → Stufe 2
for _a, _b in (('11', '5'), ('13', '14'), ('13', '13')):
    BF.stufe('hypotenuse', f'Ein rechtwinkliges Dreieck hat die Katheten {_a} cm und {_b} cm. Berechne die Hypotenuse auf eine Nachkommastelle.', 2)

# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    d = bauen('trigo.pythagoras',
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
    anhaengen(d, 9910, schwer)
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden


# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl9) ----
from _durchsicht_kl9 import Befunde as _DSB, durchsicht  # noqa: E402

DS = _DSB('trigo.pythagoras', 19_9_11)
# hypotenuse: ganzzahlige Katheten wie im Kartenbeispiel sind Stufe 1; Seiten mit anderen Namen (α = 90°) sind Stufe 2 nur bei PQR
for _t in ('Ein rechtwinkliges Dreieck hat die Katheten a = 24 cm und b = 7 cm. Berechne die Hypotenuse c.',
           'Ein rechtwinkliges Dreieck hat die Katheten a = 27 cm und b = 36 cm. Berechne die Hypotenuse c.',
           'Ein rechtwinkliges Dreieck hat die Katheten 33 cm und 56 cm. Wie lang ist die Hypotenuse?'):
    DS.stufe('hypotenuse', _t, 1)
DS.stufe('hypotenuse', 'Im Dreieck PQR ist der Winkel bei Q ein rechter, PQ = 2 cm, QR = 2,1 cm. Berechne PR.', 2)
# kathete: ganzzahlige Werte wie im Beispiel → Stufe 1; Dezimalzahl → Stufe 2; dazu zwei neue Stufe-2-Aufgaben
for _t in ('Ein rechtwinkliges Dreieck hat die Hypotenuse c = 51 cm und die Kathete b = 45 cm. Berechne die Kathete a.',
           'Ein rechtwinkliges Dreieck hat die Hypotenuse c = 40 cm und die Kathete b = 32 cm. Berechne die Kathete a.',
           'Ein rechtwinkliges Dreieck hat die Hypotenuse c = 52 cm und die Kathete b = 20 cm. Berechne die Kathete a.'):
    DS.stufe('kathete', _t, 1)
DS.stufe('kathete', 'Ein rechtwinkliges Dreieck hat die Hypotenuse c = 70 cm und die Kathete b = 42 cm. Berechne die Kathete a.', 1)
DS.stufe('kathete', 'Ein rechtwinkliges Dreieck hat die Hypotenuse c = 9 cm und die Kathete b = 5,4 cm. Berechne die Kathete a.', 2)
DS.neu('kathete', 2, DS.Z('Hypotenuse 12 cm, eine Kathete 7 cm. Wie lang ist die andere Kathete? Runde auf eine Nachkommastelle.', 9.7, '9.746794344809',
                         'a² = 144 − 49 = 95, a = √95 cm ≈ 9,7 cm.', 'Bei einer Kathete: Quadrate abziehen.', einheit='cm', toleranz=0.1))
DS.neu('kathete', 2, DS.Z('Ein rechtwinkliges Dreieck hat die Hypotenuse 2,6 m und eine Kathete von 1 m. Wie lang ist die andere Kathete?', 2.4, '2.4',
                         'a² = 6,76 − 1 = 5,76, a = 2,4 m.', 'Rechne 2,6² − 1².', einheit='m'))
# umkehrung: „Welcher Winkel ist ein rechter?“ einmal auf Stufe 3 lassen; Dezimalzahlen sind Stufe 2
for _t in ('Im Dreieck ABC ist a = 12 cm, b = 13 cm, c = 5 cm. Welcher Winkel ist ein rechter Winkel?',
           'Im Dreieck ABC ist a = 48 cm, b = 36 cm, c = 60 cm. Welcher Winkel ist ein rechter Winkel?',
           'Ist das Dreieck mit den Seiten 2,5 cm, 6 cm und 6,5 cm rechtwinklig?'):
    DS.stufe('umkehrung', _t, 2)
# koordinaten: nur runden ist Stufe 2
for _t in ('Berechne den Abstand von P(1 | −5) und Q(7 | −12) auf zwei Nachkommastellen (Einheit 1 cm).',
           'Berechne den Abstand von P(5 | −5) und Q(0 | −1) auf zwei Nachkommastellen (Einheit 1 cm).',
           'Berechne den Abstand von P(6 | 0) und Q(9 | −6) auf zwei Nachkommastellen (Einheit 1 cm).'):
    DS.stufe('koordinaten', _t, 2)
# raum: Raumdiagonale von Quader und Würfel ist das Kartenbeispiel → Stufe 2
for _t in ('Wie lang ist die Raumdiagonale eines Würfels mit 7 cm Kantenlänge? Runde auf eine Nachkommastelle.',
           'Wie lang ist die Raumdiagonale eines Würfels mit 6 cm Kantenlänge? Runde auf eine Nachkommastelle.',
           'Ein Quader ist 12 cm lang, 4 cm breit und 3 cm hoch. Wie lang ist seine Raumdiagonale?'):
    DS.stufe('raum', _t, 2)
# anwendung: Höhe im gleichseitigen Dreieck wie die gleichschenklige Aufgabe (Stufe 2); Rampe ist ein Schritt
for _t in ('Wie hoch ist ein gleichseitiges Dreieck mit 14 cm Seitenlänge? Runde auf zwei Nachkommastellen.',
           'Wie hoch ist ein gleichseitiges Dreieck mit 4 cm Seitenlänge? Runde auf zwei Nachkommastellen.',
           'Eine Rampe steigt auf 800 cm waagrechter Länge um 67 cm an. Wie lang ist die Rampe? Runde auf ganze Zentimeter.',
           'Eine Rampe steigt auf 240 cm waagrechter Länge um 70 cm an. Wie lang ist die Rampe?'):
    DS.stufe('anwendung', _t, 2)

if __name__ == '__main__':
    durchsicht('trigo.pythagoras', DS)
