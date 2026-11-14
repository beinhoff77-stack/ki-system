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


def trip(s):
    pool = KLEIN if s == 1 else [t for t in TRIPEL if t[2] <= 60] if s == 2 else TRIPEL
    t = R.choice(pool)
    if s == 3 and R.random() < 0.4:
        f = R.choice([Fr(1, 10), Fr(1, 2), Fr(3, 10)])
        return tuple(x * f for x in t)
    return tuple(Fr(x) for x in t)


def cf(x):
    return str(float(x)) if Fr(x).denominator != 1 else str(int(x))


ETAPPEN = [
    {'lernziel': 'hypotenuse', 'titel': 'Die Hypotenuse berechnen',
     'regel': 'Im ⟦rechtwinkligen⟧ Dreieck gilt ⟦a² + b² = c²⟧. c ist die ⟦Hypotenuse⟧ (gegenüber dem rechten Winkel, längste Seite), a und b sind die ⟦Katheten⟧.',
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
     'probe': '29² = 841 ✓',
     'fehler': '6² + 10² = 136 ≠ 8² ⇒ „nicht rechtwinklig“ ist ein Fehlschluss: Man muss die ⟦längste⟧ Seite (10) als c nehmen: 6² + 8² = 100 = 10².'},
    {'lernziel': 'koordinaten', 'titel': 'Abstand im Koordinatensystem',
     'regel': 'Der Abstand von P(x₁ | y₁) und Q(x₂ | y₂) ist die Hypotenuse eines Steigungsdreiecks: ⟦d = √((x₂ − x₁)² + (y₂ − y₁)²)⟧.',
     'schritte': ['P(1 | 2), Q(7 | 10): Δx = 6, Δy = 8.', 'd = √(36 + 64) = √100 = ⟦10⟧.'],
     'probe': 'Δx und Δy sind die Katheten ✓',
     'fehler': 'd = √(7² + 10²) mit den Koordinaten von Q ist falsch: Man braucht die ⟦Differenzen⟧ der Koordinaten.'},
    {'lernziel': 'raum', 'titel': 'Längen im Raum',
     'regel': 'Im Quader mit Kanten a, b, c: Flächendiagonale ⟦√(a² + b²)⟧, Raumdiagonale ⟦√(a² + b² + c²)⟧. Suche im Körper ein ⟦rechtwinkliges Dreieck⟧.',
     'schritte': ['Quader 2 cm × 3 cm × 6 cm: d² = 4 + 9 + 36 = 49.', 'Raumdiagonale d = √49 cm = ⟦7 cm⟧.'],
     'probe': 'Erst Bodendiagonale √13, dann √(13 + 36) = 7 ✓',
     'fehler': 'Raumdiagonale = √(2² + 3²) ist nur die ⟦Bodendiagonale⟧. Die Höhe 6 cm muss auch ins Quadrat und dazu.'},
    {'lernziel': 'anwendung', 'titel': 'Pythagoras im Alltag',
     'regel': 'Skizze machen, ⟦rechten Winkel⟧ suchen, Hypotenuse bestimmen, dann a² + b² = c² passend umstellen. Am Ende ⟦sinnvoll runden⟧.',
     'schritte': ['Eine 5 m lange Leiter lehnt an einer Wand, ihr Fuß steht 1,4 m von der Wand entfernt.', 'h² = 5² − 1,4² = 25 − 1,96 = 23,04 ⇒ h = ⟦4,8 m⟧ (Höhe des oberen Endes).'],
     'probe': '1,4² + 4,8² = 1,96 + 23,04 = 25 ✓',
     'fehler': 'h² = 5² + 1,4² ist falsch: Die ⟦Leiter⟧ liegt gegenüber dem rechten Winkel zwischen Wand und Boden, sie ist die Hypotenuse.'},
]


def g_hypotenuse(s):
    a, b, c = trip(s)
    if R.random() < 0.5: a, b = b, a
    if s == 3 and R.random() < 0.4:
        a, b = R.randint(2, 15), R.randint(2, 15)
        if isqrt(a * a + b * b) ** 2 == a * a + b * b: return None
        wahr = sqrt(a * a + b * b)
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Ein rechtwinkliges Dreieck hat die Katheten {a} cm und {b} cm. Berechne die Hypotenuse auf eine Nachkommastelle.',
                    f'c² = {a * a} + {b * b} = {a * a + b * b}, c = √{a * a + b * b} cm ≈ {dz(v)} cm.', 'Quadrieren, addieren, Wurzel ziehen (Taschenrechner).',
                    v, f'round({K(wahr)}, 1)', einheit='cm')
    return zahl(f'Ein rechtwinkliges Dreieck hat die Katheten a = {dz(a)} cm und b = {dz(b)} cm. Berechne die Hypotenuse c.',
                f'c² = {dz(a * a)} + {dz(b * b)} = {dz(c * c)}, c = {dz(c)} cm.', 'Beide Katheten quadrieren, addieren, dann die Wurzel ziehen.', c,
                f'({cf(a)} ** 2 + {cf(b)} ** 2) / {cf(c)}', einheit='cm')


def g_kathete(s):
    a, b, c = trip(s)
    if R.random() < 0.5: a, b = b, a
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


def g_umkehrung(s):
    a, b, c = (int(x) for x in R.choice(TRIPEL if s > 1 else KLEIN))
    recht = R.random() < 0.5
    if not recht:
        c = c + R.choice([-1, 1])
        if c <= b: return None
    seiten = [a, b, c]
    R.shuffle(seiten)
    if s < 3:
        return auswahl(f'Ein Dreieck hat die Seiten {seiten[0]} cm, {seiten[1]} cm und {seiten[2]} cm. Ist es rechtwinklig?',
                       f'{"Ja" if recht else "Nein"}, denn {a}² + {b}² = {a * a + b * b} {"=" if recht else "≠"} {c * c} = {c}².',
                       [f'{"Nein" if recht else "Ja"}, denn {a}² + {b}² = {a * a + b * b} {"=" if recht else "≠"} {c * c} = {c}².',
                        'Das kann man ohne Winkelmessung nicht entscheiden.', f'Ja, denn {a} + {b} > {c}.'],
                       f'Längste Seite c = {c}: {a}² + {b}² = {a * a + b * b}, {c}² = {c * c}. {"Gleich: rechtwinklig." if recht else "Verschieden: nicht rechtwinklig."}',
                       'Prüfe a² + b² = c² mit der längsten Seite als c.')
    if not recht: return None
    p, q, r = R.sample(['A', 'B', 'C'], 3)
    # Seiten benannt nach gegenüberliegenden Ecken
    sei = {'a': a, 'b': b, 'c': c}
    namen = list(sei)
    R.shuffle(namen)
    werte = dict(zip(namen, [a, b, c]))
    gross = max(werte, key=werte.get)
    ecke = {'a': 'α (bei A)', 'b': 'β (bei B)', 'c': 'γ (bei C)'}
    return auswahl(f'Im Dreieck ABC ist a = {werte["a"]} cm, b = {werte["b"]} cm, c = {werte["c"]} cm. Welcher Winkel ist ein rechter Winkel?',
                   ecke[gross], list(ecke.values()),
                   f'Längste Seite {gross} = {werte[gross]} cm; die Summe der anderen Quadrate ist {werte[gross] ** 2}. Der rechte Winkel liegt gegenüber von {gross}: {ecke[gross]}.',
                   'Der rechte Winkel liegt gegenüber der längsten Seite.')


def g_koordinaten(s):
    a, b, c = (int(x) for x in R.choice(KLEIN if s < 3 else [t for t in TRIPEL if t[2] <= 50]))
    if R.random() < 0.5: a, b = b, a
    x1, y1 = R.randint(-6, 6), R.randint(-6, 6)
    sx, sy = R.choice([1, -1]), R.choice([1, -1])
    if s == 1: sx = sy = 1
    x2, y2 = x1 + sx * a, y1 + sy * b
    if s == 3 and R.random() < 0.4:
        dx, dy = R.randint(1, 7), R.randint(1, 7)
        if isqrt(dx * dx + dy * dy) ** 2 == dx * dx + dy * dy: return None
        x2, y2 = x1 + dx * sx, y1 + dy * sy
        wahr = sqrt(dx * dx + dy * dy)
        v = gerundet(wahr, 2)
        if v is None: return None
        return zahl(f'Berechne den Abstand von P({dz(x1)} | {dz(y1)}) und Q({dz(x2)} | {dz(y2)}) auf zwei Nachkommastellen (Einheit 1 cm).',
                    f'Δx = {dz(x2 - x1)}, Δy = {dz(y2 - y1)}; d = √({dx * dx} + {dy * dy}) = √{dx * dx + dy * dy} ≈ {dz(v)} cm.',
                    'Differenzen der Koordinaten quadrieren, addieren, Wurzel ziehen.', v, f'round({K(wahr)}, 2)', einheit='cm')
    return zahl(f'Berechne den Abstand der Punkte P({dz(x1)} | {dz(y1)}) und Q({dz(x2)} | {dz(y2)}) (Einheit 1 cm).',
                f'Δx = {dz(x2 - x1)}, Δy = {dz(y2 - y1)}; d = √({dz(a * a)} + {dz(b * b)}) = √{dz(c * c)} = {c} cm.',
                'Bilde die Differenzen der x- und der y-Koordinaten.', c, f'(({x2} - ({x1})) ** 2 + ({y2} - ({y1})) ** 2) / {c}', einheit='cm')


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
    if typ < 0.4:
        a = R.randint(1, 12)
        k = R.randint(2, 5)
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
        t = R.choice(KLEIN)
        f = R.choice([Fr(1, 10), Fr(1, 5), Fr(1, 4), Fr(1, 2), Fr(1)])
        a, b, c = (x * f for x in t)
        if not (2 <= c <= 10) or not all(endlich(x) and Fr(x).denominator <= 20 for x in (a, b, c)): return None
        if R.random() < 0.5: a, b = b, a
        l, w, h = c, a, b
        return zahl(f'Eine {dz(l)} m lange Leiter lehnt an einer senkrechten Wand. Ihr Fuß steht {dz(w)} m von der Wand entfernt. In welcher Höhe berührt sie die Wand?',
                    f'h² = {dz(l)}² − {dz(w)}² = {dz(l * l)} − {dz(w * w)} = {dz(h * h)}, h = {dz(h)} m.', 'Die Leiter ist die Hypotenuse.', h,
                    f'({cf(l)} ** 2 - {cf(w)} ** 2) / {cf(h)}', einheit='m')
    if s == 2:
        a, b, c = (int(x) for x in R.choice(KLEIN))
        if R.random() < 0.5:
            return zahl(f'Ein Fernseher hat einen {a * 4} cm breiten und {b * 4} cm hohen Bildschirm. Wie lang ist die Bildschirmdiagonale?',
                        f'd² = {a * 4}² + {b * 4}² = {dz((c * 4) ** 2)}, d = {c * 4} cm.', 'Breite und Höhe sind die Katheten.', c * 4,
                        f'({4 * a} ** 2 + {4 * b} ** 2) / {4 * c}', einheit='cm')
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
        a, b, c = (int(x) for x in R.choice(KLEIN))
        lang = R.choice([10, 20, 50])
        return zahl(f'Eine Rampe steigt auf {a * lang} cm waagrechter Länge um {b * lang} cm an. Wie lang ist die Rampe?',
                    f'l² = {a * lang}² + {b * lang}² = {dz((c * lang) ** 2)}, l = {c * lang} cm.', 'Waagrechte Länge und Höhe sind die Katheten.', c * lang,
                    f'({a * lang} ** 2 + {b * lang} ** 2) / {c * lang}', einheit='cm')
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
          offen=['Alle Lernkarten profitieren von einer Skizze des rechtwinkligen Dreiecks (rechter Winkel markiert, Hypotenuse hervorgehoben); Lernkarte „raum“ braucht ein Schrägbild von Quader/Pyramide mit eingezeichneter Diagonale bzw. Höhe. Bisher alle Maße in Worten.',
                 'Gerundete Ergebnisse: Der Wurzelwert steht als 12-stellige Konstante im Rechenausdruck c, weil das Prüfskript keine Wurzeln kennt.'])
