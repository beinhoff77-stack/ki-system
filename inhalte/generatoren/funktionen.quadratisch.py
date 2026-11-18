#!/usr/bin/env python3
"""Thema funktionen.quadratisch – Quadratische Funktionen (Klasse 9)."""
import sys
from math import isqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(907)
SCH = 'S(□ | □)'


def nz(n):
    return R.choice([i for i in range(-n, n + 1) if i != 0])


def kpoly(a, d, e):
    """Koeffizienten [c, b, a] von a(x − d)² + e für das Koordinatensystem."""
    return [wert(Fr(a) * d * d + e), wert(-2 * Fr(a) * d), wert(Fr(a))]


def kos(graphen, punkte=None, x=(-6, 6), y=(-6, 6)):
    g = {'typ': 'koordinaten', 'x': list(x), 'y': list(y), 'graphen': graphen}
    if punkte: g['punkte'] = punkte
    return g


def sform(a, d, e):
    """Scheitelform als Text: y = a(x − d)² + e"""
    af = '' if a == 1 else '−' if a == -1 else dz(a)
    t = f'y = {af}{minus_klammer(d)}²' if d != 0 else f'y = {af}x²'
    if e: t += f' {plus(e)}'
    return t


ETAPPEN = [
    {'lernziel': 'scheitel', 'titel': 'Scheitelpunkt ablesen',
     'regel': 'In der ⟦Scheitelform⟧ y = a(x − d)² + e liegt der Scheitel bei ⟦S(d | e)⟧. Warum? Die Klammer (x − d)² ist nie negativ und wird bei ⟦x = d⟧ null – dort ist der tiefste (oder höchste) Punkt. Bei (x + 3)² wird die Klammer bei x = −3 null.',
     'bild': {'typ': 'koordinaten', 'x': [-6, 1], 'y': [-6, 4], 'graphen': [{'art': 'poly', 'k': [13, 12, 2]}], 'punkte': [{'x': -3, 'y': -5, 'name': 'S(−3 | −5)'}]},
     'schritte': ['y = 2(x + 3)² − 5 = 2(x − (−3))² + (−5).', 'Also d = −3 und e = −5: ⟦S(−3 | −5)⟧.'],
     'probe': 'x = −3 eingesetzt: 2 · 0² − 5 = −5 ✓',
     'fehler': 'Bei y = (x + 3)² − 5 den Scheitel S(3 | −5) abzulesen ist falsch: x + 3 = x − (−3), also ⟦d = −3⟧.'},
    {'lernziel': 'parameter', 'titel': 'Was bewirken a, d und e?',
     'regel': '⟦a > 0⟧: nach oben geöffnet, ⟦a < 0⟧: nach unten. ⟦|a| > 1⟧ gestreckt (schmaler), ⟦|a| < 1⟧ gestaucht (breiter). d verschiebt nach rechts/links, e nach oben/unten.',
     'schritte': ['y = −0,5(x − 1)² + 4: a = −0,5 < 0 und |a| < 1.', 'Die Parabel ist ⟦nach unten geöffnet, gestaucht⟧ und hat den Scheitel S(1 | 4).'],
     'probe': 'Der Scheitel ist hier der höchste Punkt ✓',
     'bild': {'typ': 'koordinaten', 'x': [-4, 5], 'y': [-3, 6], 'graphen': [{'art': 'poly', 'k': [0, 0, 1], 'name': 'y = x²'}, {'art': 'poly', 'k': [3.5, 1, -0.5], 'name': 'f'}], 'punkte': [{'x': 1, 'y': 4, 'name': 'S(1 | 4)'}]},
     'fehler': '„y = −3x² ist gestaucht, weil −3 < 1“ ist falsch: Es kommt auf den ⟦Betrag⟧ an. |−3| = 3 > 1, die Parabel ist gestreckt.'},
    {'lernziel': 'umformen', 'titel': 'Von der allgemeinen zur Scheitelform',
     'regel': 'Aus y = ax² + bx + c wird mit ⟦quadratischer Ergänzung⟧ die Scheitelform: a ausklammern, (b/(2a))² ergänzen und wieder abziehen. Kurz: ⟦d = −b/(2a)⟧, e = y(d).',
     'schritte': ['y = x² − 6x + 5 = x² − 6x + 9 − 9 + 5.', '= (x − 3)² − 4, also ⟦S(3 | −4)⟧.'],
     'probe': 'Mitte der Nullstellen: x² − 6x + 5 = (x − 1)(x − 5), Nullstellen 1 und 5. Die Mitte ist 3, und y(3) = 9 − 18 + 5 = −4. Also S(3 | −4) ✓',
     'fehler': 'y = x² − 6x + 5 = (x − 6)² + 5 ist falsch: In die Klammer gehört die ⟦Hälfte⟧ von 6, und die Ergänzung 9 muss wieder ⟦abgezogen⟧ werden.'},
    {'lernziel': 'nullstellen', 'titel': 'Nullstellen bestimmen',
     'regel': 'Nullstellen: ⟦y = 0 setzen⟧ und die quadratische Gleichung lösen. Die ⟦Anzahl⟧ erkennst du an der Diskriminante oder an Scheitel und Öffnung.',
     'schritte': ['y = x² − 2x − 8: 0 = x² − 2x − 8, D = 4 + 32 = 36.', 'x₁,₂ = (2 ± 6)/2: ⟦x₁ = −2, x₂ = 4⟧.'],
     'probe': '(−2)² − 2 · (−2) − 8 = 4 + 4 − 8 = 0 ✓',
     'bild': {'typ': 'koordinaten', 'x': [-4, 6], 'y': [-10, 8], 'graphen': [{'art': 'poly', 'k': [-8, -2, 1]}], 'punkte': [{'x': -2, 'y': 0, 'name': '(−2 | 0)'}, {'x': 4, 'y': 0, 'name': '(4 | 0)'}]},
     'fehler': '„S(2 | 3), nach oben geöffnet, hat zwei Nullstellen“ ist falsch: Der tiefste Punkt liegt ⟦über⟧ der x-Achse, es gibt ⟦keine⟧ Nullstelle.'},
    {'lernziel': 'punkte', 'titel': 'Funktionswerte und Punktprobe',
     'regel': 'Für den ⟦Funktionswert⟧ x einsetzen und ausrechnen. ⟦Punktprobe⟧: Liegt P(u | v) auf dem Graphen, muss f(u) = v gelten.',
     'schritte': ['f(x) = −x² + 4x + 1, P(3 | 4): f(3) = −9 + 12 + 1.', 'f(3) = 4 = v, also ⟦P liegt auf dem Graphen⟧.'],
     'probe': 'Klammern beim Einsetzen: −(3)² = −9 ✓',
     'fehler': 'Bei f(x) = −x² ist f(−3) = 9 falsch: Erst quadrieren, dann das Minus davor: ⟦−(−3)² = −9⟧.'},
    {'lernziel': 'bestimmen', 'titel': 'Funktionsterm bestimmen',
     'regel': 'Scheitel bekannt: ⟦y = a(x − d)² + e⟧ ansetzen und a mit einem Punkt bestimmen. Nullstellen bekannt: ⟦y = a(x − x₁)(x − x₂)⟧. Drei Punkte: Gleichungssystem.',
     'schritte': ['Scheitel S(1 | −2), Punkt P(3 | 6): y = a(x − 1)² − 2.', '6 = a · 2² − 2 ⇒ 4a = 8 ⇒ ⟦a = 2⟧, also y = 2(x − 1)² − 2.'],
     'probe': 'x = 3: 2 · 4 − 2 = 6 ✓',
     'fehler': '6 = a(3 − 1)² − 2 ⇒ 6 = 2a − 2 ist falsch: Die Klammer wird ⟦quadriert⟧: (3 − 1)² = 4, also 6 = 4a − 2.'},
    {'lernziel': 'extremwert', 'titel': 'Extremwertprobleme lösen',
     'regel': 'Stelle die Größe, die maximal/minimal werden soll, als ⟦quadratische Funktion⟧ einer Variablen auf. Der ⟦Scheitel⟧ liefert das Maximum bzw. Minimum.',
     'schritte': ['Rechteck mit Umfang 20 m: Seiten x und 10 − x. Fläche A(x) = x · (10 − x).', 'A(x) ist null bei x = 0 und x = 10. Die Parabel ist symmetrisch, der Scheitel liegt genau in der Mitte: ⟦x = 5⟧.', 'A(5) = 5 · 5 = ⟦25 m²⟧. Das größte Rechteck ist ein Quadrat.'],
     'bild': {'typ': 'koordinaten', 'x': [0, 10], 'y': [0, 30], 'graphen': [{'art': 'poly', 'k': [0, 10, -1], 'name': 'A'}], 'punkte': [{'x': 5, 'y': 25, 'name': 'S(5 | 25)'}], 'name_x': 'x in m', 'name_y': 'A in m²'},
     'probe': 'x = 4: A = 24 < 25 ✓',
     'fehler': 'Beim Umfang 20 m die zweite Seite 20 − x zu nennen ist falsch: Der Umfang enthält ⟦jede Seite zweimal⟧, also 2x + 2y = 20 ⇒ y = 10 − x.'},
]

# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'scheitel': {
  'einstieg': 'Eine Skaterbahn ist im Querschnitt wie ein U geformt. Am wichtigsten ist der tiefste Punkt: Dort ist der Skater am schnellsten. Bei einer Parabel heißt dieser Umkehrpunkt ⟦Scheitelpunkt S⟧. In einer bestimmten Schreibweise kann man ihn direkt ablesen.',
  'woerter': [['Parabel', 'die U-förmige Kurve einer quadratischen Funktion'],
              ['Scheitelpunkt S(d | e)', 'der tiefste (oder höchste) Punkt der Parabel, bei x = d und y = e'],
              ['Scheitelform', 'y = a(x − d)² + e'],
              ['d, e', 'die Koordinaten des Scheitels: d nach rechts, e nach oben'],
              ['(x + 3)', 'dasselbe wie (x − (−3))']],
  'bild': {'typ': 'koordinaten', 'x': [-6, 1], 'y': [-6, 4], 'graphen': [{'art': 'poly', 'k': [13, 12, 2], 'name': 'Bahn y = 2(x + 3)² − 5'}], 'punkte': [{'x': -3, 'y': -5, 'name': 'tiefster Punkt S(−3 | −5)'}]},
  'schritte': ['Die Funktion heißt y = 2(x + 3)² − 5.',
               'Die Klammer (x + 3)² ist nie negativ. Am kleinsten, nämlich 0, wird sie bei x = −3.',
               'Dort ist y = 2 · 0 − 5 = −5. Das ist der kleinste y-Wert.',
               'Also liegt der Scheitel bei ⟦S(−3 | −5)⟧.'],
  'regel': 'So liest du den Scheitel ab: Bring die Gleichung in die ⟦Scheitelform⟧ y = a(x − d)² + e. Der Scheitel liegt bei ⟦S(d | e)⟧, denn bei ⟦x = d⟧ wird die Klammer null. Achtung: Bei (x + 3)² ist d = −3.',
  'fehler': 'Bei y = (x + 3)² − 5 den Scheitel S(3 | −5) abzulesen ist falsch: x + 3 = x − (−3), also ⟦d = −3⟧. Probe: Bei x = 3 ist die Klammer 36, nicht 0 – dort ist die Bahn nicht am tiefsten.'},
 'parameter': {
  'einstieg': 'Ein Springbrunnen spritzt einen Wasserstrahl im Bogen. Dreht man am Ventil, wird der Bogen höher, breiter oder wandert zur Seite. In der Scheitelform hat jede Zahl so eine Aufgabe. Diese einstellbaren Zahlen a, d und e heißen ⟦Parameter⟧.',
  'woerter': [['Parameter', 'eine Zahl in der Funktionsgleichung, die die Form oder Lage bestimmt'],
              ['|a|', 'der Betrag: a ohne Vorzeichen'],
              ['gestreckt', 'schmaler als die Normalparabel y = x²'],
              ['gestaucht', 'breiter als die Normalparabel'],
              ['nach unten geöffnet', 'wie ein umgedrehtes U; der Scheitel ist der höchste Punkt']],
  'bild': {'typ': 'koordinaten', 'x': [-4, 5], 'y': [-3, 6], 'graphen': [{'art': 'poly', 'k': [0, 0, 1], 'name': 'Normalparabel y = x²'}, {'art': 'poly', 'k': [3.5, 1, -0.5], 'name': 'Wasserstrahl'}], 'punkte': [{'x': 1, 'y': 4, 'name': 'höchster Punkt S(1 | 4)'}]},
  'schritte': ['Die Funktion heißt y = −0,5(x − 1)² + 4. Abgelesen: a = −0,5, d = 1, e = 4.',
               'a ist negativ. Also ist die Parabel nach unten geöffnet, wie ein Wasserstrahl.',
               '|a| = 0,5 ist kleiner als 1. Also ist die Parabel breiter als y = x², sie ist gestaucht.',
               'd und e geben den höchsten Punkt an. Ergebnis: ⟦nach unten geöffnet, gestaucht, S(1 | 4)⟧.'],
  'regel': 'So liest du die Parameter: Das Vorzeichen von a sagt die Öffnung (⟦a > 0⟧ nach oben, ⟦a < 0⟧ nach unten). Der Betrag sagt die Breite (⟦|a| > 1⟧ gestreckt, ⟦|a| < 1⟧ gestaucht). d verschiebt nach rechts oder links, e nach oben oder unten.',
  'fehler': '„y = −3x² ist gestaucht, weil −3 < 1“ ist falsch: Für die Breite zählt der ⟦Betrag⟧. |−3| = 3 > 1, der Strahl ist also schmaler, die Parabel gestreckt.'},
 'umformen': {
  'einstieg': 'Oft steht eine Funktion „ausmultipliziert“ da, etwa y = x² − 6x + 5. Den Scheitel sieht man so nicht. Mit dem Trick der fehlenden Ecke aus dem Quadrat bringt man sie in die Scheitelform. Dieser Trick heißt ⟦quadratische Ergänzung⟧.',
  'woerter': [['allgemeine Form', 'y = ax² + bx + c'],
              ['quadratische Ergänzung', 'eine Zahl dazuzählen und gleich wieder abziehen, damit ein volles Quadrat entsteht'],
              ['b/2', 'die Hälfte der Zahl vor x'],
              ['y(3)', 'der y-Wert bei x = 3']],
  'schritte': ['Die Funktion heißt y = x² − 6x + 5. Die Hälfte von 6 ist 3, und 3² = 9.',
               '9 dazuzählen und gleich wieder abziehen: y = x² − 6x + 9 − 9 + 5.',
               'Die ersten drei Teile sind ein volles Quadrat: x² − 6x + 9 = (x − 3)². Der Rest: −9 + 5 = −4.',
               'Also y = (x − 3)² − 4 mit dem Scheitel ⟦S(3 | −4)⟧.'],
  'regel': 'So formst du um: Bei y = x² + bx + c ⟦(b/2)² dazuzählen und wieder abziehen⟧. Dann die ersten drei Teile als Quadrat schreiben. Steht vor x² eine Zahl a, ⟦a zuerst ausklammern⟧. Kurz gilt: ⟦d = −b/(2a)⟧ und e = y(d).',
  'fehler': 'y = x² − 6x + 5 = (x − 6)² + 5 ist falsch: In die Klammer gehört die ⟦Hälfte⟧ von 6, und die Ergänzung 9 muss wieder ⟦abgezogen⟧ werden. Probe: (x − 6)² + 5 hat bei x = 0 den Wert 41, nicht 5.'},
 'nullstellen': {
  'einstieg': 'Ein Wasserstrahl startet am Boden und landet wieder am Boden. Wo er den Boden berührt, ist seine Höhe 0. Bei einer Parabel sind das die Stellen, an denen sie die x-Achse trifft. Sie heißen ⟦Nullstellen⟧.',
  'woerter': [['Nullstelle', 'ein x-Wert, an dem y = 0 ist'],
              ['x-Achse', 'die waagrechte Achse, auf der y = 0 gilt'],
              ['Diskriminante D', 'D = b² − 4ac; sie zeigt, wie viele Lösungen es gibt'],
              ['x₁,₂', 'beide Lösungen auf einmal']],
  'bild': {'typ': 'koordinaten', 'x': [-4, 6], 'y': [-10, 8], 'graphen': [{'art': 'poly', 'k': [-8, -2, 1], 'name': 'y = x² − 2x − 8'}], 'punkte': [{'x': -2, 'y': 0, 'name': 'Nullstelle (−2 | 0)'}, {'x': 4, 'y': 0, 'name': 'Nullstelle (4 | 0)'}]},
  'schritte': ['Die Funktion heißt y = x² − 2x − 8. Für die Nullstellen y = 0 setzen: x² − 2x − 8 = 0.',
               'Ablesen: a = 1, b = −2, c = −8. D = (−2)² − 4 · 1 · (−8) = 4 + 32 = 36, und √36 = 6.',
               'Lösungsformel: x₁,₂ = (2 ± 6) / 2.',
               'Einmal minus, einmal plus: ⟦x₁ = −2, x₂ = 4⟧.'],
  'regel': 'So findest du Nullstellen: ⟦y = 0 setzen⟧ und die quadratische Gleichung lösen. Wie ⟦viele⟧ es gibt, zeigt die Diskriminante – oder ein Blick auf Scheitel und Öffnung.',
  'fehler': '„S(2 | 3), nach oben geöffnet, hat zwei Nullstellen“ ist falsch: Der tiefste Punkt liegt schon ⟦über⟧ der x-Achse, die Parabel kommt nie herunter. Es gibt ⟦keine⟧ Nullstelle.'},
 'punkte': {
  'einstieg': 'Ein Ball fliegt nach der Regel f(x) = −x² + 4x + 1. Liegt der Punkt P(3 | 4) auf seiner Bahn? Dafür rechnet man aus, wie hoch der Ball bei x = 3 ist. Diese berechnete Höhe heißt ⟦Funktionswert⟧.',
  'woerter': [['f(x)', 'die Funktion f; f(3) ist ihr Wert bei x = 3'],
              ['Funktionswert', 'das Ergebnis, wenn man ein x einsetzt'],
              ['Punktprobe', 'prüfen, ob ein Punkt auf dem Graphen liegt'],
              ['P(u | v)', 'ein Punkt mit x = u und y = v'],
              ['−(3)²', 'erst 3 · 3 = 9, dann das Minus: −9']],
  'schritte': ['Die Funktion heißt f(x) = −x² + 4x + 1. Der Punkt ist P(3 | 4).',
               'x = 3 einsetzen, Klammer setzen: f(3) = −(3)² + 4 · 3 + 1.',
               'Ausrechnen: −9 + 12 + 1 = 4.',
               'Der Funktionswert 4 ist gleich dem y-Wert von P. Also ⟦liegt P auf dem Graphen⟧.'],
  'regel': 'So machst du die ⟦Punktprobe⟧: Setze das x von P in die Funktion ein und berechne den ⟦Funktionswert⟧. Ist er gleich dem y von P, liegt der Punkt auf dem Graphen, sonst nicht.',
  'fehler': 'Bei f(x) = −x² ist f(−3) = 9 falsch: Erst quadrieren, dann das Minus davor: ⟦−(−3)² = −9⟧. Ein Ball nach dieser Regel ist nie über dem Boden.'},
 'bestimmen': {
  'einstieg': 'Eine Rutsche soll im Profil eine Parabel sein. Ihr tiefster Punkt und ein weiterer Punkt sind vorgegeben. Wie lautet die Gleichung? Man setzt die bekannten Werte ein und rechnet die fehlende Zahl aus. Das heißt ⟦Funktionsterm bestimmen⟧.',
  'woerter': [['Funktionsterm', 'der Rechenausdruck der Funktion, z. B. 2(x − 1)² − 2'],
              ['ansetzen', 'die passende Form hinschreiben und bekannte Zahlen eintragen'],
              ['Nullstellenform', 'y = a(x − x₁)(x − x₂), wenn die Nullstellen x₁ und x₂ bekannt sind']],
  'schritte': ['Gegeben: Scheitel S(1 | −2) und Punkt P(3 | 6). Ansatz in Scheitelform: y = a(x − 1)² − 2.',
               'P einsetzen: 6 = a · (3 − 1)² − 2. Die Klammer ist 2, quadriert 4: 6 = 4a − 2.',
               '2 addieren: 8 = 4a. Durch 4 teilen: ⟦a = 2⟧.',
               'Der Funktionsterm lautet y = 2(x − 1)² − 2.'],
  'regel': 'So bestimmst du den Term: Ist der Scheitel bekannt, setze ⟦y = a(x − d)² + e⟧ an. Sind die Nullstellen bekannt, setze ⟦y = a(x − x₁)(x − x₂)⟧ an. Einen weiteren Punkt einsetzen und a ausrechnen. Bei drei beliebigen Punkten hilft ein Gleichungssystem.',
  'fehler': '6 = a(3 − 1)² − 2 ⇒ 6 = 2a − 2 ist falsch: Die Klammer wird ⟦quadriert⟧: (3 − 1)² = 4, also 6 = 4a − 2.'},
 'extremwert': {
  'einstieg': 'Mit 20 m Zaun soll ein rechteckiges Gehege möglichst groß werden. Ein langes schmales Gehege ist klein, ein ganz kurzes auch. Irgendwo dazwischen liegt das beste. Wo eine Größe am größten oder kleinsten ist, nennt man ⟦Extremwert⟧ – bei einer Parabel ist das der Scheitel.',
  'woerter': [['Extremwert', 'der größte (Maximum) oder kleinste (Minimum) Wert'],
              ['Umfang', 'die Länge des Zauns rundherum: jede Seite zählt zweimal'],
              ['A(x)', 'die Fläche, abhängig von der Seite x'],
              ['symmetrisch', 'links und rechts vom Scheitel spiegelgleich']],
  'bild': {'typ': 'koordinaten', 'x': [0, 10], 'y': [0, 30], 'graphen': [{'art': 'poly', 'k': [0, 10, -1], 'name': 'Fläche A'}], 'punkte': [{'x': 5, 'y': 25, 'name': 'größte Fläche S(5 | 25)'}], 'name_x': 'Seite x in m', 'name_y': 'Fläche A in m²'},
  'schritte': ['Eine Seite heißt x. Zwei Seiten zusammen sind der halbe Zaun, 10 m. Die andere Seite ist also 10 − x.',
               'Die Fläche ist Seite mal Seite: A(x) = x · (10 − x). Das ist eine nach unten geöffnete Parabel.',
               'A(x) ist null bei x = 0 und bei x = 10. Die Parabel ist symmetrisch, ihr Scheitel liegt genau in der Mitte: ⟦x = 5⟧.',
               'A(5) = 5 · 5 = ⟦25 m²⟧. Das größte Gehege ist ein Quadrat mit 5 m Seite.'],
  'regel': 'So löst du ein Extremwertproblem: Schreibe die Größe, die am größten oder kleinsten werden soll, als ⟦quadratische Funktion⟧ einer Variablen. Der ⟦Scheitel⟧ liefert das Maximum bzw. Minimum.',
  'fehler': 'Beim Umfang 20 m die zweite Seite 20 − x zu nennen ist falsch: Der Zaun läuft um ⟦jede Seite zweimal⟧, also 2x + 2y = 20 ⇒ y = 10 − x.'},
}
klar(ETAPPEN, KLAR)
# ---- KLAR ENDE ----
# ---- UMBAU (neues Muster, Runde 8, Vorgabe 16.11.) ----
UMBAU = {
 'scheitel': {
  'einstieg': 'Eine Skaterbahn ist im Querschnitt wie ein U geformt. Am tiefsten Punkt ist der Skater am schnellsten. Bei einer Parabel heißt dieser Punkt ⟦Scheitelpunkt⟧.',
  'woerter': [['Scheitelpunkt', 'der tiefste oder höchste Punkt der Parabel, geschrieben S(d | e)'],
              ['Scheitelform', 'y = a(x − d)² + e'],
              ['(x + 3)', 'dasselbe wie (x − (−3))']],
  'bild': {'typ': 'koordinaten', 'x': [-6, 1], 'y': [-6, 4], 'graphen': [{'art': 'poly', 'k': [13, 12, 2], 'name': 'Bahn'}]},
  'schritte': [{'text': 'Die Bahn heißt y = 2(x + 3)² − 5. Das ist die Scheitelform.'},
               {'text': '(x + 3)² ist nie negativ und wird 0 bei x = −3.', 'bild': {'senkrecht': [-3]}},
               {'text': 'Dort ist y = 2 · 0 − 5 = −5, der kleinste Wert.'},
               {'text': 'Der Scheitelpunkt ist ⟦S(−3 | −5)⟧.', 'bild': {'punkte': [{'x': -3, 'y': -5, 'name': 'S(−3 | −5)'}]}}],
  'fehler': 'Bei (x + 3)² − 5 ist der Scheitel nicht S(3 | −5). Bei x = 3 ist die Klammer 36, nicht 0.',
  'regel': 'Der Scheitel von a(x − d)² + e ist ⟦S(d | e)⟧. Achtung: Bei (x + 3)² ist d = −3.'},
 'parameter': {
  'einstieg': 'Dreht man am Ventil eines Springbrunnens, wird der Wasserbogen höher, breiter oder wandert zur Seite. In der Scheitelform haben die Zahlen solche Aufgaben: Sie heißen ⟦Parameter⟧.',
  'woerter': [['Parameter', 'eine Zahl in der Gleichung, die Form oder Lage bestimmt'],
              ['gestaucht', 'breiter als die Normalparabel y = x²'],
              ['nach unten geöffnet', 'wie ein umgedrehtes U']],
  'bild': {'typ': 'koordinaten', 'x': [-4, 5], 'y': [-3, 6], 'graphen': [{'art': 'poly', 'k': [3.5, 1, -0.5], 'name': 'y = −0,5(x − 1)² + 4'}]},
  'schritte': [{'text': 'Abgelesen aus der Gleichung: a = −0,5, d = 1, e = 4.'},
               {'text': 'a ist negativ: Die Parabel ist nach unten geöffnet.'},
               {'text': '|a| = 0,5 ist kleiner als 1: breiter als y = x², also gestaucht.',
                'bild': {'graphen': [{'art': 'poly', 'k': [3.5, 1, -0.5], 'name': 'Wasser'}, {'art': 'poly', 'k': [0, 0, 1], 'name': 'y = x²'}]}},
               {'text': 'Der höchste Punkt ist ⟦S(1 | 4)⟧.', 'bild': {'punkte': [{'x': 1, 'y': 4, 'name': 'S(1 | 4)'}]}}],
  'fehler': 'y = −3x² ist nicht gestaucht, weil −3 < 1. Für die Breite zählt |−3| = 3 > 1: gestreckt, also schmaler.',
  'fehler_bild': {'graphen': [{'art': 'poly', 'k': [0, 0, 1], 'name': 'y = x²'}, {'art': 'poly', 'k': [0, 0, -3], 'name': 'y = −3x²'}], 'punkte': []},
  'regel': 'a < 0 öffnet nach unten, |a| < 1 macht ⟦breiter⟧. d und e verschieben den Scheitel nach rechts und oben.'},
 'umformen': {
  'einstieg': 'Manchmal ist eine Parabel ausmultipliziert gegeben. Dann sieht man den Scheitel nicht. Mit der fehlenden Ecke wie beim Quadrat bekommst du die Scheitelform: ⟦quadratische Ergänzung⟧.',
  'woerter': [['ausmultipliziert', 'ohne Klammer geschrieben, z. B. x² − 6x + 5'],
              ['quadratische Ergänzung', 'eine Zahl dazuzählen und wieder abziehen, damit ein volles Quadrat entsteht']],
  'bild': {'typ': 'koordinaten', 'x': [-1, 7], 'y': [-5, 8], 'graphen': [{'art': 'poly', 'k': [5, -6, 1], 'name': 'y = x² − 6x + 5'}]},
  'schritte': [{'text': 'Die Hälfte von 6 ist 3, und 3² = 9.'},
               {'text': 'Plus 9 minus 9: y = x² − 6x + 9 − 9 + 5.'},
               {'text': 'Zusammengefasst: y = (x − 3)² − 4.'},
               {'text': 'Der Scheitel ist ⟦S(3 | −4)⟧.', 'bild': {'punkte': [{'x': 3, 'y': -4, 'name': 'S(3 | −4)'}]}}],
  'fehler': 'y = (x − 6)² + 5 ist falsch. In die Klammer gehört die Hälfte von 6, und die 9 muss wieder weg.',
  'fehler_bild': {'graphen': [{'art': 'poly', 'k': [5, -6, 1], 'name': 'richtig', 'name_x': 6.3}, {'art': 'poly', 'k': [41, -12, 1], 'name': 'falsch', 'name_x': 4.5}]},
  'regel': 'Ergänze ⟦(b/2)²⟧ und ziehe es wieder ab. Steht vor x² eine Zahl, klammerst du sie zuerst aus.'},
 'nullstellen': {
  'einstieg': 'Wo trifft eine Parabel die x-Achse? Dort ist die Höhe 0, wie beim Wasserstrahl am Boden. Diese Stellen heißen ⟦Nullstellen⟧.',
  'woerter': [['Nullstellen', 'die x-Werte, bei denen y = 0 ist'],
              ['x-Achse', 'die waagrechte Achse; auf ihr ist y = 0']],
  'bild': {'typ': 'koordinaten', 'x': [-4, 6], 'y': [-10, 8], 'graphen': [{'art': 'poly', 'k': [-8, -2, 1], 'name': 'y = x² − 2x − 8'}]},
  'schritte': [{'text': 'Für die Nullstellen y = 0 setzen: x² − 2x − 8 = 0.'},
               {'text': 'D = (−2)² − 4 · 1 · (−8) = 36, also √D = 6.'},
               {'text': 'x₁,₂ = (2 ± 6) : 2, also ⟦x₁ = −2, x₂ = 4⟧.',
                'bild': {'punkte': [{'x': -2, 'y': 0, 'name': '−2'}, {'x': 4, 'y': 0, 'name': '4'}]}}],
  'fehler': 'S(2 | 3) und nach oben geöffnet heißt: keine Nullstelle. Der tiefste Punkt liegt schon über der x-Achse.',
  'fehler_bild': {'graphen': [{'art': 'poly', 'k': [7, -4, 1], 'name': 'S(2 | 3)'}], 'punkte': [{'x': 2, 'y': 3, 'name': 'S'}]},
  'regel': 'Setze ⟦y = 0⟧ und löse die quadratische Gleichung. Die Diskriminante zeigt, wie viele Nullstellen es gibt.'},
 'punkte': {
  'einstieg': 'Ein Ball fliegt auf einer Parabelbahn. Liegt der Punkt P(3 | 4) auf dieser Bahn? Du prüfst es mit dem ⟦Funktionswert⟧.',
  'woerter': [['Funktionswert', 'das Ergebnis, wenn man ein x einsetzt'],
              ['f(3)', 'der Funktionswert bei x = 3'],
              ['Punktprobe', 'prüfen, ob ein Punkt auf dem Graphen liegt']],
  'bild': {'typ': 'koordinaten', 'x': [-1, 5], 'y': [-3, 6], 'graphen': [{'art': 'poly', 'k': [1, 4, -1], 'name': 'Bahn'}]},
  'schritte': [{'text': 'Die Bahn heißt f(x) = −x² + 4x + 1.'},
               {'text': 'x = 3 einsetzen: f(3) = −(3)² + 4 · 3 + 1.'},
               {'text': 'Ausrechnen: −9 + 12 + 1 = 4.'},
               {'text': 'Punktprobe: f(3) = 4 ist der y-Wert von P. ⟦P liegt auf der Bahn⟧.',
                'bild': {'punkte': [{'x': 3, 'y': 4, 'name': 'P(3 | 4)'}]}}],
  'fehler': 'Bei f(x) = −x² ist f(−3) nicht 9. Erst quadrieren, dann das Minus davor: −(−3)² = −9.',
  'regel': 'Setze x ein und ⟦rechne f(x) aus⟧. Ist f(u) = v, liegt P(u | v) auf dem Graphen.'},
 'bestimmen': {
  'einstieg': 'Eine Rutsche soll ein Parabelprofil haben. Der tiefste Punkt und ein weiterer Punkt sind vorgegeben. Daraus berechnest du die Gleichung: den ⟦Funktionsterm⟧.',
  'woerter': [['Funktionsterm', 'der Rechenausdruck der Funktion, z. B. 2(x − 1)² − 2'],
              ['Ansetzen', 'die passende Form hinschreiben und Bekanntes eintragen']],
  'bild': {'typ': 'koordinaten', 'x': [-1, 4], 'y': [-3, 8],
           'punkte': [{'x': 1, 'y': -2, 'name': 'S(1 | −2)'}, {'x': 3, 'y': 6, 'name': 'P(3 | 6)'}]},
  'schritte': [{'text': 'Ansetzen mit S(1 | −2): y = a(x − 1)² − 2.'},
               {'text': 'P(3 | 6) einsetzen: 6 = a · 2² − 2 = 4a − 2.'},
               {'text': 'Also 4a = 8 und ⟦a = 2⟧.'},
               {'text': 'Der Funktionsterm: y = 2(x − 1)² − 2.', 'bild': {'graphen': [{'art': 'poly', 'k': [0, -4, 2], 'name': 'Rutsche'}]}}],
  'fehler': '6 = a(3 − 1)² − 2 heißt nicht 6 = 2a − 2. Die Klammer wird quadriert: (3 − 1)² = 4.',
  'regel': 'Scheitel bekannt: ⟦y = a(x − d)² + e⟧ ansetzen. Mit einem weiteren Punkt rechnest du a aus.'},
 'extremwert': {
  'einstieg': 'Mit 20 m Zaun soll ein rechteckiges Gehege möglichst groß werden. Lang und schmal ist schlecht, kurz und breit auch. Das Beste liegt dazwischen: ein ⟦Extremwert⟧.',
  'woerter': [['Extremwert', 'der größte oder kleinste Wert'],
              ['Umfang', 'die Zaunlänge rundherum; jede Seite zählt zweimal'],
              ['A(x)', 'die Fläche, abhängig von der Seite x']],
  'bild': {'typ': 'koordinaten', 'x': [0, 10], 'y': [0, 30], 'graphen': [{'art': 'poly', 'k': [0, 10, -1], 'name': 'Fläche'}],
           'name_x': 'x in m', 'name_y': 'A in m²'},
  'schritte': [{'text': 'Zwei Seiten sind zusammen der halbe Umfang: x und 10 − x.'},
               {'text': 'Die Fläche ist A(x) = x · (10 − x).'},
               {'text': 'Nullstellen 0 und 10, der Scheitel liegt genau mittig: x = 5.', 'bild': {'senkrecht': [5]}},
               {'text': 'A(5) = 25: ⟦ein Quadrat mit 25 m²⟧.', 'bild': {'punkte': [{'x': 5, 'y': 25, 'name': 'S(5 | 25)'}]}}],
  'fehler': 'Die zweite Seite ist nicht 20 − x. Der Zaun läuft um jede Seite zweimal: 2x + 2y = 20.',
  'regel': 'Schreibe die Größe als ⟦quadratische Funktion⟧. Der Scheitel liefert den größten oder kleinsten Wert.'},
}
umbau(ETAPPEN, UMBAU)
# ---- UMBAU ENDE ----


def g_scheitel(s):
    d, e = R.randint(-9, 9), R.randint(-9, 9)
    if s == 1:
        a = 1
        if R.random() < 0.4:
            d, e = R.randint(-4, 4), R.randint(-4, 4)
            a = R.choice([1, -1])
            return bild(luecken(f'Lies den Scheitel der gezeichneten Parabel ab.', SCH, 'x-Wert, y-Wert', [d, e],
                                f'Der {"tiefste" if a > 0 else "höchste"} Punkt der Parabel ist S({dz(d)} | {dz(e)}). Gleichung: {sform(a, d, e)}.',
                                'Suche den tiefsten bzw. höchsten Punkt und lies beide Koordinaten ab.', c=[f'{d}', f'{e}']),
                        kos([{'art': 'poly', 'k': kpoly(a, d, e)}], x=(d - 5, d + 5), y=(min(e, 0) - 5 if a < 0 else min(e, 0) - 2, max(e, 0) + 2 if a < 0 else max(e, 0) + 6)))
        if R.random() < 0.3: d = 0
    else:
        a = R.choice([-3, -2, -1, 2, 3, 4, Fr(1, 2), Fr(-1, 2)])
    if s == 2 and R.random() < 0.4:
        a = R.choice([1, -1, 2, -2, 3])
        d, e = nz(6), nz(6)
        beschr = ('Normalparabel' if abs(a) == 1 else f'Mit a = {dz(abs(a))} gestreckte Parabel') + f', Scheitel S({dz(d)} | {dz(e)}), nach {"oben" if a > 0 else "unten"} geöffnet'
        return luecken(f'{beschr}. Gib die Gleichung in Scheitelform an.', '□(x − □)² + □', 'Tippe den Term ein, z. B. −2(x + 3)² + 1.', [a, d, e],
                       f'a = {dz(a)} ({"nach oben" if a > 0 else "nach unten"}), d = {dz(d)}, e = {dz(e)}: {sform(a, d, e)}.',
                       'Setze d und e aus dem Scheitel in y = a(x − d)² + e ein. Das Vorzeichen von a bestimmt die Öffnung.',
                       c=[f'{a}', f'{d}', f'{e}'])
    if s == 3:
        if R.random() < 0.6:
            if e == 0 or d == 0: return None
            txt = f'y = {dz(e)} {"+" if a > 0 else "−"} {"" if abs(a) == 1 else dz(abs(a))}{minus_klammer(d)}²'
            return luecken(f'Gib den Scheitel der Parabel {txt} an.', SCH, 'x-Wert, y-Wert', [d, e],
                           f'Umgestellt: {sform(a, d, e)}, also S({dz(d)} | {dz(e)}).', 'Ordne zuerst zur Scheitelform y = a(x − d)² + e.',
                           c=[f'{d}', f'{e}'])
        d, e = -R.randint(1, 9), 0
    return luecken(f'Gib den Scheitel der Parabel {sform(a, d, e)} an.', SCH, 'x-Wert, y-Wert', [d, e],
                   f'{sform(a, d, e)} ist Scheitelform mit d = {dz(d)} und e = {dz(e)}: S({dz(d)} | {dz(e)}).',
                   'Lies d aus der Klammer (x − d) mit umgedrehtem Vorzeichen ab. Für welches x wird die Klammer null?', c=[f'{d}', f'{e}'])


def g_parameter(s):
    typ = R.choice({1: 'ab', 2: 'abcgg', 3: 'cdee'}[s])
    if typ == 'g':
        while True:
            par = [(R.choice([Fr(1, 2), 1, 2, -1, -2, Fr(-1, 2)]), R.randint(-3, 3), R.randint(-3, 3)) for _ in range(3)]
            if len({p_[0] for p_ in par}) == 3 and len({(p_[1], p_[2]) for p_ in par}) >= 2: break
        namen = ['A', 'B', 'C']
        k = R.randrange(3)
        a, d, e = par[k]
        g = kos([{'art': 'poly', 'k': kpoly(*par[i]), 'name': namen[i]} for i in range(3)], x=(-6, 6), y=(-6, 6))
        if R.random() < 0.5:
            return bild(auswahl(f'Welcher Graph gehört zu {sform(a, d, e)}?', f'Graph {namen[k]}', [f'Graph {n}' for n in namen],
                                f'{sform(a, d, e)}: Scheitel S({dz(d)} | {dz(e)}), {"nach oben" if a > 0 else "nach unten"} geöffnet, '
                                f'{"gestreckt" if abs(a) > 1 else "gestaucht" if abs(a) < 1 else "so breit wie die Normalparabel"}. Das passt nur zu Graph {namen[k]}.',
                                'Prüfe Scheitel, Öffnung und Breite.'), g)
        return bild(auswahl(f'Welche Gleichung gehört zu Graph {namen[k]}?', sform(a, d, e),
                            [sform(-a, d, e), sform(a, -d, e) if d else sform(a, d, -e) if e else sform(2 * a, d, e), sform(Fr(1) / a if abs(a) != 1 else 2 * a, d, e)],
                            f'Graph {namen[k]} hat den Scheitel S({dz(d)} | {dz(e)}) und ist {"nach oben" if a > 0 else "nach unten"} geöffnet: {sform(a, d, e)}.',
                            'Lies Scheitel und Öffnung ab; vergleiche die Breite mit der Normalparabel.'), g)
    if typ == 'a':
        a = R.choice([-4, -3, -2, -1, Fr(-1, 2), Fr(-1, 4), Fr(1, 4), Fr(1, 2), 2, 3, 5])
        d, e = R.randint(-5, 5), R.randint(-5, 5)
        o = 'nach oben' if a > 0 else 'nach unten'
        f = 'gestreckt' if abs(a) > 1 else 'gestaucht' if abs(a) < 1 else 'weder gestreckt noch gestaucht'
        richtig = f'{o} geöffnet, {f}'
        andere = [f'{"nach unten" if a > 0 else "nach oben"} geöffnet, {f}', f'{o} geöffnet, {"gestaucht" if abs(a) > 1 else "gestreckt"}',
                  f'{"nach unten" if a > 0 else "nach oben"} geöffnet, {"gestaucht" if abs(a) > 1 else "gestreckt"}']
        return auswahl(f'Wie sieht die Parabel {sform(a, d, e)} im Vergleich zur Normalparabel aus?', richtig, andere,
                       f'a = {dz(a)}: {"positiv" if a > 0 else "negativ"} ⇒ {o} geöffnet; |a| = {dz(abs(a))} {">" if abs(a) > 1 else "<" if abs(a) < 1 else "="} 1 ⇒ {f}.',
                       'Vorzeichen von a: Öffnung. Betrag von a: Streckung oder Stauchung.')
    if typ == 'b':
        d, e = nz(6), nz(6)
        rl = f'{abs(d)} nach {"rechts" if d > 0 else "links"}'
        ou = f'{abs(e)} nach {"oben" if e > 0 else "unten"}'
        richtig = sform(1, d, e)
        andere = [sform(1, -d, e), sform(1, d, -e), sform(1, -d, -e)]
        return auswahl(f'Die Normalparabel wird um {rl} und um {ou} verschoben. Welche Gleichung hat die neue Parabel?', richtig, andere,
                       f'Verschiebung nach {"rechts" if d > 0 else "links"} um {abs(d)}: d = {dz(d)}; nach {"oben" if e > 0 else "unten"} um {abs(e)}: e = {dz(e)}. Also {richtig}.',
                       'Nach rechts verschieben: In der Klammer steht ein Minus.')
    if typ == 'c':
        d, e = nz(8), R.randint(-8, 8)
        return auswahl(f'Jemand liest bei {sform(1, d, e)} den Scheitel S({dz(-d)} | {dz(e)}) ab. Was stimmt?',
                       f'Falsch: S({dz(d)} | {dz(e)}), denn die Klammer ist (x − d).',
                       ['Richtig.', f'Falsch: S({dz(e)} | {dz(d)})', f'Falsch: S({dz(-d)} | {dz(-e)})'],
                       f'{minus_klammer(d)} = x − ({dz(d)}), also d = {dz(d)}. Bei x = {dz(d)} wird die Klammer null.',
                       'Für welches x wird die Klammer null?')
    if typ == 'd':
        a = R.choice([-3, -2, 2, 3])
        b = R.choice([Fr(-1, 2), Fr(1, 3), Fr(1, 2), Fr(-1, 3)])
        if R.random() < 0.5: a, b = b, a
        schmal = a if abs(a) > abs(b) else b
        return auswahl(f'Welche der Parabeln y = {dz(a) if endlich(a) else br(a)}x² und y = {dz(b) if endlich(b) else br(b)}x² ist schmaler?',
                       f'y = {dz(schmal) if endlich(schmal) else br(schmal)}x²', [f'y = {dz(a + b - schmal) if endlich(a + b - schmal) else br(a + b - schmal)}x²', 'beide gleich breit', 'Das hängt vom Vorzeichen ab.'],
                       f'Schmaler ist die Parabel mit dem größeren Betrag von a: |{br(schmal)}| > |{br(a + b - schmal)}|.',
                       'Vergleiche die Beträge von a.')
    a = R.choice([-2, -1, 1, 2])
    d = nz(5)
    art = R.choice(['zwei', 'eine', 'keine'])
    e = 0 if art == 'eine' else R.randint(1, 9) * (1 if (art == 'keine') == (a > 0) else -1)
    n = {'zwei': 'zwei Nullstellen', 'eine': 'genau eine Nullstelle', 'keine': 'keine Nullstelle'}[art]
    return auswahl(f'Ohne zu rechnen: Wie viele Nullstellen hat {sform(a, d, e)}?', n, ['zwei Nullstellen', 'genau eine Nullstelle', 'keine Nullstelle'],
                   (f'Scheitel S({dz(d)} | 0) liegt auf der x-Achse: {n}.' if e == 0 else
                    f'Scheitel S({dz(d)} | {dz(e)}) liegt {"über" if e > 0 else "unter"} der x-Achse, Parabel {"nach oben" if a > 0 else "nach unten"} geöffnet: {n}.'),
                   'Wo liegt der Scheitel, und in welche Richtung ist die Parabel geöffnet?')


def g_umformen(s):
    d, e = nz(7), R.randint(-9, 9)
    a = 1 if s < 3 else R.choice([-2, -1, 2, 3])
    if s == 2 and R.random() < 0.4: a = -1
    b, c = -2 * a * d, a * d * d + e
    allg = f'y = {poly(a, b, c)}'
    if s == 3 and R.random() < 0.35:
        if abs(a) == 1 or R.random() < 0.4:
            a, b, c = 1, -2 * d, d * d + e
            falsch_e = c + d * d
            if falsch_e == 0: return None
            return auswahl(f'Jemand formt um: y = {poly(1, b, c)} = {minus_klammer(d)}² {plus(c)} + {dz(d * d)}. Was ist falsch?',
                           f'Die Ergänzung {dz(d * d)} muss abgezogen werden: y = {minus_klammer(d)}² {plus(e)}.',
                           ['Nichts, die Umformung stimmt.', f'In die Klammer gehört {minus_klammer(2 * d)}.', f'Es muss y = {minus_klammer(-d)}² {plus(e)} heißen.'],
                           f'x² {plus_v(b)} = {minus_klammer(d)}² − {dz(d * d)}. Also y = {minus_klammer(d)}² − {dz(d * d)} {plus(c)} = {minus_klammer(d)}² {plus(e)}, nicht {plus(falsch_e)}.',
                           'Multipliziere die Klammer aus und vergleiche mit dem Ausgangsterm.')
        if a < 0: return None
        q = d * d
        falsch_e = c - q
        if falsch_e == e or falsch_e == 0: return None
        return auswahl(f'Jemand formt um: y = {poly(a, b, c)} = {dz(a)}(x² {plus_v(-2 * d)} + {dz(q)}) {plus(c)} − {dz(q)} = {dz(a)}{minus_klammer(d)}² {plus(falsch_e)}. Was ist falsch?',
                       f'Es muss {dz(a)} · {dz(q)} = {dz(a * q)} abgezogen werden: y = {dz(a)}{minus_klammer(d)}² {plus(e)}.',
                       ['Nichts, die Umformung stimmt.', f'Die Klammer muss {minus_klammer(2 * d)} heißen.', f'Der Faktor {dz(a)} darf nicht ausgeklammert werden.'],
                       f'In der Klammer steht {dz(q)}, wegen des Faktors {dz(a)} davor wurde {dz(a * q)} ergänzt. Also {plus(c)} − {dz(a * q)} = {plus(e)}.',
                       'Was wurde durch das Ergänzen in der Klammer wirklich addiert?')
    if s == 1 and R.random() < 0.5:
        return zahl(f'Bei {allg} liegt der Scheitel bei x = −b/(2a). Berechne die x-Koordinate des Scheitels.',
                    f'x = −({dz(b)})/(2 · {kl(a)}) = {dz(d)}.', 'Lies b und a mit Vorzeichen ab.', d, f'-({b}) / (2 * ({a}))')
    return luecken(f'Bestimme den Scheitel von {allg}.', SCH, 'x-Wert, y-Wert', [d, e],
                   f'Quadratische Ergänzung: {allg} = {sform(a, d, e)[4:]}, also S({dz(d)} | {dz(e)}).',
                   'Klammere a aus (falls nötig) und ergänze die Hälfte des x-Koeffizienten zum Quadrat.',
                   c=[f'-({b}) / (2 * ({a}))', f'({a}) * ({d}) ** 2 + ({b}) * ({d}) + ({c})'])


def g_nullstellen(s):
    if s == 1:
        p, q = sorted(R.sample([i for i in range(-6, 7)], 2))
        if R.random() < 0.4 and q - p >= 2:
            a = R.choice([1, -1])
            dm = Fr(p + q, 2)
            em = a * (dm - p) * (dm - q)
            k = [wert(Fr(a * p * q)), wert(Fr(-a * (p + q))), a]
            return bild(luecken('Lies die Nullstellen der gezeichneten Parabel ab.', 'x₁ = □; x₂ = □', 'kleinere zuerst', [p, q],
                                f'Die Parabel schneidet die x-Achse bei x = {dz(p)} und x = {dz(q)}.',
                                'Wo schneidet der Graph die x-Achse?', c=[f'{p}', f'{q}']),
                        kos([{'art': 'poly', 'k': k}], x=(p - 3, q + 3), y=(int(min(em, 0)) - 2, int(max(em, 0)) + 3)))
        return luecken(f'Bestimme die Nullstellen von y = {minus_klammer(p)} · {minus_klammer(q)}.',
                       'x₁ = □; x₂ = □', 'kleinere zuerst', [p, q],
                       f'Ein Produkt ist null, wenn ein Faktor null ist: x = {dz(p)} oder x = {dz(q)}.', 'Setze jeden Faktor gleich null.',
                       c=[f'min({p}, {q})', f'max({p}, {q})'])
    if s == 2:
        a = R.choice([1, 1, -1, 2])
        p, q = sorted(R.sample(range(-8, 9), 2))
        b, c = -a * (p + q), a * p * q
        D = b * b - 4 * a * c
        r = isqrt(D)
        return luecken(f'Bestimme die Nullstellen von y = {poly(a, b, c)}.', 'x₁ = □; x₂ = □', 'kleinere zuerst', [p, q],
                       f'0 = {poly(a, b, c)}; D = {dz(D)}; x₁,₂ = ({dz(-b)} ± {r}) / {dz(2 * a)}: {dz(p)} und {dz(q)}.',
                       'Setze y = 0 und löse die quadratische Gleichung.',
                       c=[f'min((-({b}) - {r}) / (2 * ({a})), (-({b}) + {r}) / (2 * ({a})))', f'max((-({b}) - {r}) / (2 * ({a})), (-({b}) + {r}) / (2 * ({a})))'])
    if R.random() < 0.45:
        a = R.choice([1, 1, -1, 2, -2])
        d, r = nz(5), R.randint(1, 5)
        e = -a * r * r
        return luecken(f'Bestimme die Nullstellen von {sform(a, d, e)}.', 'x₁ = □; x₂ = □', 'kleinere zuerst', [d - r, d + r],
                       f'0 = {sform(a, d, e)[4:]} ⇔ {minus_klammer(d)}² = {dz(r * r)} ⇔ {minus_klammer(d)[1:-1]} = ±{r}: x₁ = {dz(d - r)}, x₂ = {dz(d + r)}.',
                       'Setze y = 0, bringe e auf die andere Seite, teile durch a und ziehe die Wurzel.',
                       c=[f'{d} - ((-({e})) / ({a})) / {r}', f'{d} + ((-({e})) / ({a})) / {r}'])
    art = R.choice(['zwei', 'eine', 'keine'])
    a = nz(3)
    if art == 'zwei':
        p, q = R.sample(range(-6, 7), 2)
        b, c = -a * (p + q), a * p * q
        if R.random() < 0.4: b, c = nz(8), -abs(nz(9)) * (1 if a > 0 else -1)
    elif art == 'eine':
        k, r = R.choice([1, 1, 2, 3]), nz(5)
        a, b, c = k * k * (1 if a > 0 else -1), 2 * k * r * (1 if a > 0 else -1), r * r * (1 if a > 0 else -1)
    else:
        b = nz(6)
        c = ((b * b) // (4 * abs(a)) + R.randint(1, 5)) * (1 if a > 0 else -1)
    if c == 0 and art != 'zwei': return None
    D = b * b - 4 * a * c
    n = 'zwei Nullstellen' if D > 0 else 'genau eine Nullstelle' if D == 0 else 'keine Nullstelle'
    assert n.startswith({'zwei': 'zwei', 'eine': 'genau', 'keine': 'keine'}[art])
    return auswahl(f'Wie viele Nullstellen hat die Funktion f mit f(x) = {poly(a, b, c)}?', n, ['zwei Nullstellen', 'genau eine Nullstelle', 'keine Nullstelle'],
                   f'D = {kl(b)}² − 4 · {kl(a)} · {kl(c)} = {dz(D)}, also {n}.', 'Berechne die Diskriminante.')


def einsetz(a, b, c, u):
    """f(u) ausgeschrieben, ohne „+ 0“ und „1 ·“."""
    t = ('' if a == 1 else '−' if a == -1 else f'{kl(a)} · ') + f'{kl(u)}²'
    if b: t += f' {"+" if b > 0 else "−"} {"" if abs(b) == 1 else dz(abs(b)) + " · "}{kl(u)}'
    if c: t += f' {plus(c)}'
    return t


def g_punkte(s):
    a, b, c = nz(3), R.randint(-6, 6), R.randint(-9, 9)
    u = R.randint(-4, 4)
    fu = a * u * u + b * u + c
    if s == 1:
        return zahl(f'Berechne f({dz(u)}) für f(x) = {poly(a, b, c)}.', f'f({dz(u)}) = {einsetz(a, b, c, u)} = {dz(fu)}.',
                    'Setze die Zahl mit Klammern ein: erst Potenz, dann Punkt, dann Strich.', fu, f'({a}) * ({u}) ** 2 + ({b}) * ({u}) + ({c})')
    if s == 2:
        if u == 0: return None
        auf = R.random() < 0.5
        f_vz = -a * u * u + b * u + c        # (−u)² als −u² gerechnet
        f_b = a * u * u - b * u + c          # Vorzeichenfehler bei b · u
        f_c = a * u * u + b * u              # c vergessen
        kand = [x for x in dict.fromkeys([f_vz, f_b, f_c, fu + 2 * a, fu - 1]) if x != fu]
        if auf:
            v = fu
            richtig = 'Ja'
            falsch = [f'Nein, f({dz(u)}) = {dz(x)}' for x in kand[:3]]
        else:
            v = kand[0]
            richtig = f'Nein, f({dz(u)}) = {dz(fu)}'
            falsch = ['Ja'] + [f'Nein, f({dz(u)}) = {dz(x)}' for x in kand[1:3]]
        return auswahl(f'Liegt P({dz(u)} | {dz(v)}) auf dem Graphen von f(x) = {poly(a, b, c)}?', richtig, falsch,
                       f'f({dz(u)}) = {einsetz(a, b, c, u)} = {dz(fu)}. ' + (f'Das ist die y-Koordinate von P, also liegt P auf dem Graphen.' if auf else f'{dz(fu)} ≠ {dz(v)}, also liegt P nicht auf dem Graphen.'),
                       'Setze die x-Koordinate ein und vergleiche mit der y-Koordinate.')
    if R.random() < 0.45:
        if R.random() < 0.5:
            k, u_ = R.randint(1, 9), R.randint(2, 7)
            v = u_ * u_ - k
            return zahl(f'P(u | {dz(v)}) liegt auf dem Graphen von y = x² − {k}, und u > 0. Bestimme u.',
                        f'u² − {k} = {dz(v)} ⇔ u² = {dz(u_ * u_)} ⇔ u = ±{u_}; wegen u > 0: u = {u_}.',
                        'Setze die y-Koordinate ein und löse nach u. Beachte u > 0.', u_, f'{u_ * u_} / {u_}')
        b2 = nz(5)
        u_ = nz(4)
        v = -u_ * u_ + b2 * u_
        return zahl(f'Q({dz(u_)} | v) liegt auf dem Graphen von y = {poly(-1, b2, 0)}. Bestimme v.',
                    f'v = {einsetz(-1, b2, 0, u_)} = {dz(v)}.', 'Setze die x-Koordinate ein. Achtung: −x² mit x = ' + dz(u_) + ' ergibt −(' + dz(u_) + ')².',
                    v, f'-({u_}) ** 2 + ({b2}) * ({u_})')
    if u == 0: return None
    return zahl(f'Der Punkt P({dz(u)} | {dz(fu)}) liegt auf dem Graphen von f(x) = {poly(a, b, 0)} + c. Bestimme c.',
                f'{dz(fu)} = {einsetz(a, b, 0, u)} + c = {dz(a * u * u + b * u)} + c ⇒ c = {dz(c)}.',
                'Setze die Koordinaten von P ein und löse nach c auf.', c, f'({fu}) - (({a}) * ({u}) ** 2 + ({b}) * ({u}))')


def g_bestimmen(s):
    if s == 3 and R.random() < 0.4:
        a, b, c = nz(3), R.randint(-5, 5), R.randint(-6, 6)
        xs = [0, R.choice([1, 2]), R.choice([-1, -2])]
        pts = [(t, a * t * t + b * t + c) for t in xs]
        ptxt = ', '.join(f'({dz(t)} | {dz(y)})' for t, y in pts)
        M = [[t * t, t, 1] for t, _ in pts]
        det = lambda m: m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])  # noqa: E731
        rhs = [y for _, y in pts]
        cs = []
        for j in range(3):
            Mj = [[rhs[i] if k == j else M[i][k] for k in range(3)] for i in range(3)]
            cs.append(f'{det(Mj)} / {det(M)}')
        return luecken(f'Bestimme die Parabel y = ax² + bx + c durch {ptxt}.', 'a = □; b = □; c = □', 'Werte von a, b, c', [a, b, c],
                       f'Aus ({dz(xs[0])} | {dz(pts[0][1])}) folgt c = {dz(c)}; die anderen Punkte liefern a = {dz(a)}, b = {dz(b)}: y = {poly(a, b, c)}.',
                       'Setze die Punkte ein; der Punkt mit x = 0 liefert sofort c.', c=cs)
    if s == 1 or (s == 2 and R.random() < 0.5):
        d, e, a = R.randint(-5, 5), R.randint(-6, 6), nz(3)
        u = d + nz(3)
        v = a * (u - d) ** 2 + e
        return zahl(f'Eine Parabel hat den Scheitel S({dz(d)} | {dz(e)}) und geht durch P({dz(u)} | {dz(v)}). Bestimme a in y = a(x − d)² + e.',
                    f'{dz(v)} = a · ({dz(u)} − {kl(d)})² {plus(e)} = {"" if (u - d) ** 2 == 1 else dz((u - d) ** 2)}a{" " + plus(e) if e else ""} ⇒ a = {dz(a)}.',
                    'Setze Scheitel und Punkt in die Scheitelform ein.', a, f'(({v}) - ({e})) / (({u}) - ({d})) ** 2')
    p, q = sorted(R.sample(range(-6, 7), 2))
    a = nz(3)
    u = R.choice([t for t in range(-6, 7) if t not in (p, q)])
    v = a * (u - p) * (u - q)
    return zahl(f'Eine Parabel hat die Nullstellen x₁ = {dz(p)} und x₂ = {dz(q)} und geht durch P({dz(u)} | {dz(v)}). Bestimme a in y = a(x − x₁)(x − x₂).',
                f'{dz(v)} = a · ({dz(u)} − {kl(p)})({dz(u)} − {kl(q)}) = {"" if (u - p) * (u - q) == 1 else "−" if (u - p) * (u - q) == -1 else dz((u - p) * (u - q))}a ⇒ a = {dz(a)}.',
                'Setze die Nullstellen in die Produktform ein, dann den Punkt.', a, f'({v}) / ((({u}) - ({p})) * (({u}) - ({q})))')


def g_extremwert(s):
    typ = R.random()
    if s == 1:
        a, d, e = R.choice([-1, -2, 1, 2]), R.randint(-6, 6), R.randint(-9, 9)
        art = 'größten' if a < 0 else 'kleinsten'
        b, c = -2 * a * d, a * d * d + e
        return zahl(f'Welchen {art} Wert nimmt f(x) = {poly(a, b, c)} an?',
                    f'f(x) = {sform(a, d, e)[4:]}; Scheitel S({dz(d)} | {dz(e)}), {"höchster" if a < 0 else "tiefster"} Punkt: {dz(e)}.',
                    'Bestimme den Scheitel; sein y-Wert ist der Extremwert.', e, f'({a}) * ({d}) ** 2 + ({b}) * ({d}) + ({c})')
    if s == 2:
        if typ < 0.5:
            U = 4 * R.randint(3, 30)
            h = U // 4
            return zahl(f'Ein rechteckiges Gehege soll mit {dz(U)} m Zaun umgeben werden. Welchen größten Flächeninhalt kann es haben?',
                        f'Seiten x und {dz(U // 2)} − x: A(x) = −x² + {dz(U // 2)}x = −(x − {dz(h)})² + {dz(h * h)}. Maximum {dz(h * h)} m² (Quadrat).',
                        'Drücke die zweite Seite durch x aus und bestimme den Scheitel von A(x).', h * h, f'({U} / 4) * ({U} / 2 - {U} / 4)', einheit='m²')
        S = 2 * R.randint(5, 40)
        return zahl(f'Zwei Zahlen haben die Summe {S}. Wie groß ist ihr Produkt höchstens?',
                    f'P(x) = x({S} − x) = −(x − {S // 2})² + {dz((S // 2) ** 2)}: höchstens {dz((S // 2) ** 2)} (bei x = {S // 2}).',
                    'Nenne eine Zahl x und drücke die andere durch x aus.', (S // 2) ** 2, f'({S} / 2) * ({S} - {S} / 2)')
    if typ < 0.35:
        L = 4 * R.randint(5, 30)
        x = L // 4
        return zahl(f'An einer Hauswand soll ein rechteckiger Auslauf mit {dz(L)} m Zaun abgegrenzt werden (die Wand ersetzt eine Seite). Welche Fläche ist höchstens möglich?',
                    f'Seiten x, x und {dz(L)} − 2x: A(x) = x({dz(L)} − 2x) = −2(x − {dz(x)})² + {dz(2 * x * x)}. Maximum {dz(2 * x * x)} m².',
                    'Zwei Seiten senkrecht zur Wand heißen x; die dritte Seite ist der Rest des Zauns.', 2 * x * x,
                    f'({L} / 4) * ({L} - 2 * ({L} / 4))', einheit='m²')
    if typ < 0.55:
        k, xs = R.choice([(Fr(1, 10), 10), (Fr(1, 20), 10), (Fr(1, 10), 5), (Fr(1, 20), 20), (Fr(1, 40), 20), (Fr(1, 5), 5)])
        bb = 2 * k * xs
        h0 = Fr(R.randint(3, 4), 2)
        hm = -k * xs * xs + bb * xs + h0
        return zahl(f'Ein Ball fliegt auf der Bahn h(x) = −{dz(k)}x² + {dz(bb)}x + {dz(h0)} (x und h in m). Wie hoch fliegt er höchstens?',
                    f'Scheitel bei x = −{dz(bb)}/(2 · (−{dz(k)})) = {xs}; h({xs}) = −{dz(k)} · {xs * xs} + {dz(bb)} · {xs} + {dz(h0)} = {dz(hm)} m.',
                    'Die größte Höhe ist der y-Wert des Scheitels. Nutze x = −b/(2a).', hm,
                    f'-{float(k)} * {xs} ** 2 + {float(bb)} * {xs} + {float(h0)}', einheit='m')
    if typ < 0.75:
        v, t = R.choice([(10, 1), (20, 2), (15, Fr(3, 2)), (25, Fr(5, 2)), (30, 3), (5, Fr(1, 2))])
        h0 = R.randint(0, 3) * Fr(1, 2)
        # h(t) = −5t² + v t + h0, Scheitel bei t = v/10
        hmax = -5 * t * t + v * t + h0
        return zahl(f'Ein Ball fliegt nach h(t) = −5t² + {v}t {plus(h0) if h0 else ""}'.rstrip() + ' (t in s, h in m). Wie hoch fliegt er höchstens?',
                    f'Scheitel bei t = −{v}/(2 · (−5)) = {dz(t)} s; h({dz(t)}) = {dz(hmax)} m.',
                    'Die größte Höhe ist der y-Wert des Scheitels. Nutze t = −b/(2a).', hmax,
                    f'-5 * ({v} / 10) ** 2 + {v} * ({v} / 10) + {float(h0)}', einheit='m')
    p0, n0, dp, dn = R.choice([(10, 200, 1, 10), (20, 300, 2, 10), (8, 400, 1, 20), (12, 120, 1, 5), (30, 600, 5, 50)])
    # Preis p = p0 + k·dp, Absatz n = n0 − k·dn, Einnahmen E(k) = (p0 + k dp)(n0 − k dn)
    kopt = Fr(n0 * dp - p0 * dn, 2 * dp * dn)
    if kopt.denominator != 1 or kopt <= 0: return None
    E = (p0 + kopt * dp) * (n0 - kopt * dn)
    return zahl(f'Ein Verein verkauft {n0} Karten zu je {p0} €. Je {dp} € Preiserhöhung werden {dn} Karten weniger verkauft. Welcher Preis bringt die höchsten Einnahmen?',
                f'E(k) = ({p0} + {dp}k)({n0} − {dn}k), Scheitel bei k = {dz(kopt)}: Preis {dz(p0 + kopt * dp)} €, Einnahmen {dz(E)} €.',
                'k = Anzahl der Erhöhungen. Einnahmen = Preis · Anzahl; Scheitel von E(k) bestimmen.', p0 + kopt * dp,
                f'{p0} + (({n0}) * ({dp}) - ({p0}) * ({dn})) / (2 * {dp} * {dn}) * {dp}', einheit='€')


GEN = {'scheitel': g_scheitel, 'parameter': g_parameter, 'umformen': g_umformen, 'nullstellen': g_nullstellen,
       'punkte': g_punkte, 'bestimmen': g_bestimmen, 'extremwert': g_extremwert}

# ---------- Zehnte Runde (schwer-kl9): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Abschnitt mit eigenem festen Zufallsstart (anhaengen(..., 9907, ...)), läuft erst nach bauen():
# alle bisherigen Aufgaben bleiben unverändert. Vorbilder: Bayerischer Mathematik-Test 10 (ISB; Nullstellen,
# Entstehung aus der Normalparabel, Wertemenge, Bremsweg bei doppelter Geschwindigkeit, Funktionswert im Sachzusammenhang,
# Punkt auf y = x), Illustrierende Aufgaben Realschule 9 (I) (Parabel aus Eigenschaften, Gehege mit Rundung beim
# Ergebnis, Bremsweg), Abschlussprüfung Realschule Bayern 2024 (Rechtecke mit Eckpunkt auf einer Geraden, Extremwert),
# MSA Berlin/Brandenburg (Nullstellen und Scheitel einer Parabel). Zahlen und Wortlaut eigen.
from _schwer_kl9 import anhaengen  # noqa: E402


def schwer():
    P, Kn, O = 'pruefung', 'knobel', ''
    S, HS = 'S(□ | □)', 'Koordinaten eintragen'
    L2, H2 = 'x₁ = □; x₂ = □', 'kleinere Lösung zuerst'
    return [
        # scheitel
        ('scheitel', 3, P, auswahl('Welche Wertemenge hat die Funktion f mit f(x) = −2(x − 1)² + 3?', 'W = {y | y ≤ 3}',
                                   ['W = {y | y ≥ 3}', 'W = {y | y ≤ 1}', 'W = ℝ'],
                                   'Scheitel S(1 | 3), a = −2 < 0: nach unten geöffnet, 3 ist der größte Funktionswert. Alle y ≤ 3 kommen vor.',
                                   'Lies den Scheitel ab und überlege, ob er höchster oder tiefster Punkt ist.')),
        ('scheitel', 3, P, luecken('Eine Parabel y = (x − x₁)(x − x₂) hat die Nullstellen −1 und 5. Gib ihren Scheitel an.', S, HS, [2, -9],
                                   'Der Scheitel liegt mittig zwischen den Nullstellen: x = (−1 + 5)/2 = 2. y = (2 + 1)(2 − 5) = 3 · (−3) = −9.',
                                   'Die Parabel ist symmetrisch: Der Scheitel liegt genau in der Mitte der Nullstellen.', ['(-1 + 5) // 2', '3 * (-3)'])),
        ('scheitel', 3, Kn, luecken('Die Parabel y = (x − d)² + e geht durch (0 | 5) und (4 | 5). Ihr kleinster Funktionswert ist 1. Gib den Scheitel an.', S, HS, [2, 1],
                                    'Gleiche y-Werte liegen symmetrisch zur Achse, also d = (0 + 4)/2 = 2. Der kleinste Wert ist e = 1. Probe: (0 − 2)² + 1 = 5.',
                                    'Zwei Punkte mit gleichem y-Wert liegen spiegelbildlich zur Symmetrieachse.', ['(0 + 4) // 2', '1'])),
        ('scheitel', 3, O, luecken('Gib den Scheitel von y = (x − 3)(x + 7) an.', S, HS, [-2, -25],
                                   'Nullstellen 3 und −7, Mitte x = −2. y = (−2 − 3)(−2 + 7) = (−5) · 5 = −25.', 'Erst die Nullstellen ablesen, dann die Mitte.', ['(3 - 7) // 2', '(-5) * 5'])),
        ('scheitel', 2, O, luecken('Gib den Scheitel der Parabel y = 0,5(x − 4)² − 1 an.', S, HS, [4, -1], 'Scheitelform a(x − d)² + e mit d = 4, e = −1: S(4 | −1).',
                                   'Lies d und e ab. Achte auf das Vorzeichen in der Klammer.', ['4', '-1'])),
        ('scheitel', 2, O, luecken('Wo liegt der höchste Punkt des Graphen von y = −(x + 6)² + 2?', 'H(□ | □)', HS, [-6, 2],
                                   'Nach unten geöffnet, Scheitel bei x = −6, y = 2: H(−6 | 2).', '(x + 6) heißt d = −6.', ['-6', '2'])),
        # parameter
        ('parameter', 3, P, auswahl('Wie entsteht der Graph von g mit g(x) = (x + 2)² − 3 aus der Normalparabel?', 'um 2 nach links und um 3 nach unten verschoben',
                                    ['um 2 nach rechts und um 3 nach unten verschoben', 'um 2 nach links und um 3 nach oben verschoben', 'mit Faktor 2 gestreckt und um 3 nach unten verschoben'],
                                    'g(x) = (x − (−2))² − 3: Scheitel S(−2 | −3). Die Normalparabel wird also 2 nach links und 3 nach unten verschoben, ihre Form bleibt.',
                                    'Bestimme den Scheitel und vergleiche mit S(0 | 0).')),
        ('parameter', 3, P, auswahl('Für den Bremsweg gilt näherungsweise s(v) = v²/200 (v in km/h, s in m). Wie ändert sich der Bremsweg, wenn die Geschwindigkeit verdoppelt wird?',
                                    'Er wird viermal so lang.', ['Er wird doppelt so lang.', 'Er wird um 2 m länger.', 'Er wird achtmal so lang.'],
                                    's(2v) = (2v)²/200 = 4v²/200 = 4 · s(v). Beispiel: 50 km/h → 12,5 m, 100 km/h → 50 m.',
                                    'Setze 2v ein oder rechne ein Beispiel mit 50 und 100 km/h.')),
        ('parameter', 3, Kn, auswahl('Die Parabeln y = x² + e und y = −x² + 8 haben genau einen gemeinsamen Punkt. Wie groß ist e?', 'e = 8', ['e = 0', 'e = 4', 'e = −8'],
                                     'Gleichsetzen: x² + e = −x² + 8 ⇔ 2x² = 8 − e. Genau eine Lösung nur bei 8 − e = 0, also e = 8. Die Scheitel berühren sich dann in (0 | 8).',
                                     'Setze gleich. Wann hat 2x² = Zahl genau eine Lösung?')),
        ('parameter', 3, O, auswahl('Welcher Graph ist am schmalsten?', 'y = −3x²', ['y = 2x²', 'y = 0,5x² + 7', 'y = −x² + 4'],
                                    'Die Breite hängt nur von |a| ab: |−3| = 3 ist am größten. Verschieben (+7, +4) und Öffnungsrichtung ändern die Breite nicht.',
                                    'Vergleiche die Beträge der Zahlen vor x².')),
        ('parameter', 2, O, auswahl('Welche Parabel ist nach unten geöffnet und gestaucht (breiter als die Normalparabel)?', 'y = −0,4x² + 1',
                                    ['y = 0,4x² − 1', 'y = −4x² + 1', 'y = 4x² − 1'],
                                    'Nach unten: a < 0. Gestaucht: |a| < 1. Beides gilt nur für a = −0,4.', 'Prüfe Vorzeichen und Betrag von a.')),
        ('parameter', 2, O, auswahl('Die Normalparabel wird um 5 nach rechts verschoben. Welche Gleichung gehört zum neuen Graphen?', 'y = (x − 5)²',
                                    ['y = (x + 5)²', 'y = x² + 5', 'y = x² − 5'],
                                    'Der Scheitel wandert nach S(5 | 0): y = (x − 5)². Probe: Bei x = 5 ist y = 0.', 'Wo liegt der neue Scheitel?')),
        # umformen
        ('umformen', 3, P, luecken('Bestimme den Scheitel von y = 0,5x² − 4x + 5.', S, HS, [4, -3],
                                   '0,5 ausklammern: y = 0,5(x² − 8x) + 5 = 0,5[(x − 4)² − 16] + 5 = 0,5(x − 4)² − 8 + 5 = 0,5(x − 4)² − 3.',
                                   'Klammere 0,5 aus den x-Gliedern aus, dann quadratische Ergänzung.', ['8 // 2', '-8 + 5'])),
        ('umformen', 3, P, luecken('Bringe y = −x² + 6x − 5 in Scheitelform.', 'y = −(x − □)² + □', 'Zahlen eintragen', [3, 4],
                                   'y = −(x² − 6x) − 5 = −[(x − 3)² − 9] − 5 = −(x − 3)² + 9 − 5 = −(x − 3)² + 4.',
                                   'Klammere −1 aus. Achte auf das Vorzeichen beim Auflösen der eckigen Klammer.', ['6 // 2', '9 - 5'])),
        ('umformen', 3, Kn, zahl('Für welche Zahl c liegt der Scheitel von y = x² − 6x + c genau auf der x-Achse?',
                                 'y = (x − 3)² − 9 + c. Der Scheitel S(3 | c − 9) liegt auf der x-Achse, wenn c − 9 = 0, also c = 9.',
                                 'Bestimme den Scheitel mit c als Platzhalter.', 9, '(6 / 2) ** 2')),
        ('umformen', 3, O, luecken('Bestimme den Scheitel von y = 2x² + 4x + 7.', S, HS, [-1, 5], 'y = 2(x² + 2x) + 7 = 2(x + 1)² − 2 + 7 = 2(x + 1)² + 5.',
                                   'Klammere zuerst 2 aus.', ['-2 // 2', '-2 + 7'])),
        ('umformen', 2, O, luecken('Bringe y = x² − 2x + 3 in Scheitelform und gib den Scheitel an.', S, HS, [1, 2], 'y = (x − 1)² − 1 + 3 = (x − 1)² + 2.',
                                   'Ergänze (2/2)² = 1 und ziehe es wieder ab.', ['1', '3 - 1'])),
        ('umformen', 2, O, luecken('Multipliziere y = (x − 2)² + 1 aus.', 'y = x² + □x + □', 'Zahlen eintragen (auch negativ)', [-4, 5],
                                   '(x − 2)² = x² − 4x + 4, plus 1: y = x² − 4x + 5.', 'Binomische Formel für (x − 2)².', ['-2 * 2', '4 + 1'])),
        # nullstellen
        ('nullstellen', 3, P, luecken('Bestimme die Nullstellen von f(x) = 2x² − 8x − 10.', L2, H2, [-1, 5],
                                      'f(x) = 0 ⇔ x² − 4x − 5 = 0 ⇔ (x − 5)(x + 1) = 0. Nullstellen −1 und 5.', 'Erst durch 2 teilen.', ['-1', '5'])),
        ('nullstellen', 3, P, auswahl('Welche Funktion hat genau eine Nullstelle?', 'y = (x − 3)²', ['y = x² − 3', 'y = x² + 3', 'y = (x − 3)(x + 3)'],
                                      '(x − 3)² = 0 nur für x = 3. x² − 3: zwei (±√3); x² + 3: keine; (x − 3)(x + 3): zwei.',
                                      'Löse jeweils f(x) = 0 im Kopf.')),
        ('nullstellen', 3, Kn, zahl('Die Parabel y = x² + bx + 12 hat die Nullstelle 3. Wo liegt die zweite Nullstelle?',
                                    'Mit den Nullstellen gilt y = (x − 3)(x − n). Das Zahlglied ist 3 · n = 12, also n = 4. (Dann b = −7.)',
                                    'Denke an die Produktform: Was ergibt das Produkt der Nullstellen?', 4, '12 / 3')),
        ('nullstellen', 3, O, luecken('Die Parabel y = x² − 2x − 3 und die Gerade y = x + 1 schneiden sich zweimal. Bestimme die x-Koordinaten der Schnittpunkte.', L2, H2, [-1, 4],
                                      'Gleichsetzen: x² − 2x − 3 = x + 1 ⇔ x² − 3x − 4 = 0 ⇔ (x − 4)(x + 1) = 0.', 'Gleichsetzen und alles auf eine Seite bringen.', ['-1', '4'])),
        ('nullstellen', 2, O, luecken('Bestimme die Nullstellen von y = x² − 6x + 8.', L2, H2, [2, 4], '(x − 2)(x − 4) = 0, also 2 und 4.', 'Produkt 8, Summe 6.', ['2', '4'])),
        ('nullstellen', 2, O, auswahl('Wie viele Nullstellen hat y = 2(x + 1)² + 3?', 'keine Nullstelle', ['genau eine Nullstelle', 'zwei Nullstellen'],
                                      'Scheitel S(−1 | 3) liegt über der x-Achse, nach oben geöffnet: keine Nullstelle.', 'Lage des Scheitels und Öffnung betrachten.')),
        # punkte
        ('punkte', 3, P, zahl('Die Bahn einer Kugel beim Kugelstoßen: h(x) = −0,1x² + 0,9x + 2 (x waagrechte Entfernung, h Höhe, beides in m). In welcher Höhe ist die Kugel 5 m vom Abstoß entfernt?',
                              'h(5) = −0,1 · 25 + 0,9 · 5 + 2 = −2,5 + 4,5 + 2 = 4. Die Kugel ist dort 4 m hoch.', 'Setze x = 5 ein. Erst quadrieren.', 4,
                              '-0.1 * 5 ** 2 + 0.9 * 5 + 2', einheit='m')),
        ('punkte', 3, P, zahl('Der Punkt P(u | u) liegt auf der Parabel y = x² − 6, und u > 0. Bestimme u.',
                              'u = u² − 6 ⇔ u² − u − 6 = 0 ⇔ (u − 3)(u + 2) = 0. Wegen u > 0: u = 3. Probe: 3² − 6 = 3.', 'x- und y-Wert sind gleich: setze beide als u ein.', 3,
                              '(1 + 5) / 2')),
        ('punkte', 3, Kn, zahl('A(−2 | 7) und B(6 | 7) liegen auf derselben Parabel y = x² + bx + c. Bei welchem x liegt ihr Scheitel?',
                               'Gleiche y-Werte liegen symmetrisch zur Symmetrieachse. Die Achse liegt mittig: x = (−2 + 6)/2 = 2.', 'Rechnen ist nicht nötig – denke an die Symmetrie.', 2,
                               '(-2 + 6) / 2')),
        ('punkte', 3, O, zahl('Der Punkt P(2 | 5) liegt auf dem Graphen von y = ax² − 3. Bestimme a.', '5 = a · 4 − 3 ⇔ 4a = 8 ⇔ a = 2.', 'Punkt einsetzen, nach a auflösen.', 2,
                              '(5 + 3) / 4')),
        ('punkte', 2, O, zahl('Berechne f(−2) für f(x) = −x² + 3x + 1.', 'f(−2) = −(−2)² + 3 · (−2) + 1 = −4 − 6 + 1 = −9.', 'Erst (−2)² = 4, dann das Minus davor.', -9,
                              '-(-2) ** 2 + 3 * (-2) + 1')),
        ('punkte', 2, O, auswahl('Liegt P(−3 | 4) auf dem Graphen von y = x² + 2x + 1?', 'Ja, denn (−3)² + 2 · (−3) + 1 = 4.', ['Nein, denn es kommt 16 heraus.', 'Nein, denn es kommt −2 heraus.'],
                                 '9 − 6 + 1 = 4 = y-Wert von P.', 'Setze x = −3 ein und vergleiche mit 4.')),
        # bestimmen
        ('bestimmen', 3, P, zahl('Eine Parabel hat den Scheitel S(2 | −8) und geht durch den Ursprung O(0 | 0). Bestimme a in y = a(x − 2)² − 8.',
                                 'O einsetzen: 0 = a · (0 − 2)² − 8 = 4a − 8 ⇒ a = 2.', 'Setze den Ursprung in die Scheitelform ein.', 2, '8 / 4')),
        ('bestimmen', 3, P, luecken('Eine nach unten geöffnete Normalparabel (a = −1) hat die Nullstellen 1 und 7. Gib die Gleichung in allgemeiner Form an.', 'y = −x² + □x + □',
                                    'Zahlen eintragen (auch negativ)', [8, -7],
                                    'y = −(x − 1)(x − 7) = −(x² − 8x + 7) = −x² + 8x − 7.', 'Produktform mit a = −1 ansetzen und ausmultiplizieren.', ['1 + 7', '-(1 * 7)'])),
        ('bestimmen', 3, Kn, zahl('Eine Parabel y = ax² + c schneidet die y-Achse bei 8 und die x-Achse bei −4 und 4. Bestimme a.',
                                  'c = 8. Nullstelle 4: 16a + 8 = 0 ⇒ a = −0,5. Die zweite Nullstelle −4 liefert dasselbe (Symmetrie).', 'c liest du direkt ab. Setze dann eine Nullstelle ein.',
                                  -0.5, '-8 / 16')),
        ('bestimmen', 3, O, zahl('Eine Parabel hat den Scheitel S(−1 | 4) und schneidet die y-Achse bei 2. Bestimme a in y = a(x + 1)² + 4.',
                                 'Bei x = 0: a · 1² + 4 = 2 ⇒ a = −2.', 'Der y-Achsenabschnitt ist der Punkt (0 | 2).', -2, '2 - 4')),
        ('bestimmen', 2, O, luecken('Gib die Scheitelform der Normalparabel (a = 1) mit dem Scheitel S(−3 | 2) an.', 'y = (x + □)² + □', 'Zahlen eintragen', [3, 2],
                                    'y = (x − (−3))² + 2 = (x + 3)² + 2.', 'In der Klammer steht x − d.', ['3', '2'])),
        ('bestimmen', 2, O, zahl('Die Parabel y = a(x − 1)² + 3 geht durch P(3 | 11). Bestimme a.', '11 = a · 4 + 3 ⇒ a = 2.', 'Punkt einsetzen.', 2, '(11 - 3) / 4')),
        # extremwert
        ('extremwert', 3, P, zahl('Rechtecke liegen mit zwei Seiten auf den Koordinatenachsen; die Ecke gegenüber dem Ursprung liegt auf der Geraden y = −0,5x + 6 (x > 0). Wie groß ist der größte Flächeninhalt?',
                                  'A(x) = x · (−0,5x + 6) = −0,5x² + 6x. Scheitel bei x = 6 (Mitte der Nullstellen 0 und 12). A(6) = −18 + 36 = 18.',
                                  'Breite x, Höhe ist der y-Wert der Geraden. Stelle A(x) auf.', 18, '-0.5 * 6 ** 2 + 6 * 6', einheit='FE')),
        ('extremwert', 3, P, zahl('Mit 16 m Zaun wird an einer Mauer ein rechteckiges Gehege gebaut (die Mauer ist eine Seite). Jedes Huhn braucht mindestens 3 m². Wie viele Hühner passen höchstens hinein?',
                                  'A(x) = x(16 − 2x), größter Wert bei x = 4: A = 4 · 8 = 32 m². 32 : 3 ≈ 10,7 – also höchstens 10 Hühner (abrunden, sonst fehlt Platz).',
                                  'Erst die größte Fläche bestimmen. Überlege dann, ob du auf- oder abrunden musst.', 10, '32 // 3')),
        ('extremwert', 3, Kn, zahl('Die Differenz zweier Zahlen ist 10. Wie klein kann ihr Produkt höchstens werden?',
                                   'Zahlen x und x + 10: P(x) = x² + 10x = (x + 5)² − 25. Kleinster Wert −25 bei x = −5 (die Zahlen −5 und 5).',
                                   'Das Produkt kann negativ werden. Stelle P(x) auf und bestimme den Scheitel.', -25, '-5 * 5')),
        ('extremwert', 3, O, zahl('Ein Händler verkauft 200 Kappen zu je 10 €. Jede Preiserhöhung um 1 € kostet ihn 10 Verkäufe. Bei welchem Preis nimmt er am meisten ein?',
                                  'Erhöhung x: E(x) = (10 + x)(200 − 10x) = −10x² + 100x + 2 000. Scheitel bei x = 5. Preis 15 € (Einnahme 15 · 150 = 2 250 €).',
                                  'Stelle die Einnahme als Preis mal Stückzahl in Abhängigkeit von der Erhöhung x auf.', 15, '10 + 5', einheit='€')),
        ('extremwert', 2, O, zahl('Wie groß ist der kleinste Funktionswert von y = (x − 3)² + 7?', 'Scheitel S(3 | 7), nach oben geöffnet: kleinster Wert 7.', 'Lies den Scheitel ab.', 7, '0 + 7')),
        ('extremwert', 2, O, zahl('Wie groß ist der größte Funktionswert von f(x) = −x² + 8x?', 'Nullstellen 0 und 8, Scheitel bei x = 4: f(4) = −16 + 32 = 16.',
                                  'Der Scheitel liegt mittig zwischen den Nullstellen.', 16, '-4 ** 2 + 8 * 4')),
    ]


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('funktionen.quadratisch', 13_9_7)
# c) Formatierungsfehler „1x“ statt „x“
BF.ersetze('extremwert', 'Ein Ball fliegt auf der Bahn h(x) = −0,05x² + 1x + 2 (x und h in m). Wie hoch fliegt er höchstens?', BF.Z(
    'Ein Ball fliegt auf der Bahn h(x) = −0,05x² + x + 2 (x und h in m). Wie hoch fliegt er höchstens?', 7, '-0.05 * 10 ** 2 + 1.0 * 10 + 2.0',
    'Scheitel bei x = −1/(2 · (−0,05)) = 10; h(10) = −0,05 · 100 + 10 + 2 = 7 m.',
    'Die größte Höhe ist der y-Wert des Scheitels. Nutze x = −b/(2a).', einheit='m'))
# a) reines Ablesen → Stufe 2
BF.stufe('scheitel', 'Gib den Scheitel der Parabel y = −3(x + 3)² an.', 2)
BF.stufe('scheitel', 'Gib den Scheitel der Parabel y = −0,5(x + 7)² an.', 2)
# a) fünfmal derselbe Typ „Ohne zu rechnen: Wie viele Nullstellen …?“ auf Stufe 3 → drei davon Stufe 2
for _f in ('(x + 4)² + 3', '−(x + 2)² − 6', '−(x + 5)² + 8'):
    BF.stufe('parameter', f'Ohne zu rechnen: Wie viele Nullstellen hat y = {_f}?', 2)
BF.nicht_umgesetzt('bestimmen S3 „Parabel durch drei Punkte“ überschneidet sich mit gleichungen.lgs3/parabel', 'Laut Befund kein Fehler; Überschneidung betrifft den Plan.')

# ---- BEFUNDE ENDE ----


# ---------- Achtzehnte Runde, Teil B (Zweig luecken-kl9): neue Lernkarte „schnittpunkte“ nach „bestimmen“ ----------
# Lehrplan: LehrplanPLUS M9 2.2 Quadratische Funktionen in Anwendungen – Schnittprobleme verschiedener Funktionstypen,
# rechnerisch und graphisch. Prüfungsvorbilder: Abschlussprüfung Realschule Bayern Mathematik I/II (Aufgaben „Die Gerade g
# schneidet die Parabel p in den Punkten P und Q. Berechnen Sie die Koordinaten …“; „Für welchen Wert … ist g Tangente?“).
# Eigene Zahlen und Einkleidungen. Eigener Zufallsstart, alles Alte bleibt unverändert.
from _luecken_kl9 import einbauen  # noqa: E402

SP_L = 'schnittpunkte'
SP2 = 'S₁(□ | □); S₂(□ | □)'
X2 = 'x₁ = □; x₂ = □'

KARTE_SP = {
    'lernziel': SP_L, 'titel': 'Schnittpunkte von Parabel und Gerade',
    'einstieg': 'Ein Ball fliegt im Bogen, daneben ist ein Seil schräg gespannt. Wo trifft der Ball das Seil? '
                'Punkte, die auf beiden Linien liegen, heißen ⟦Schnittpunkte⟧.',
    'woerter': [['Schnittpunkte', 'Punkte, die auf beiden Graphen liegen'],
                ['gleichsetzen', 'beide Terme gleich setzen, weil dort beide y-Werte gleich sind'],
                ['Tangente', 'Gerade, die die Parabel nur berührt: genau ein gemeinsamer Punkt']],
    'bild': {'typ': 'koordinaten', 'x': [-3, 6], 'y': [-3, 9],
             'graphen': [{'art': 'poly', 'k': [-1, -2, 1], 'name': 'Ball'}, {'art': 'linear', 'm': 1, 't': 3, 'name': 'Seil'}]},
    'schritte': [{'text': 'Ball y = x² − 2x − 1, Seil y = x + 3: gleichsetzen.'},
                 {'text': 'x² − 2x − 1 = x + 3. Alles nach links bringen.'},
                 {'text': 'x² − 3x − 4 = 0, also ⟦x = −1 oder x = 4⟧.', 'bild': {'senkrecht': [-1, 4]}},
                 {'text': 'Einsetzen in y = x + 3 gibt ⟦(−1 | 2) und (4 | 7)⟧.',
                  'bild': {'senkrecht': [], 'punkte': [{'x': -1, 'y': 2, 'name': '(−1 | 2)'}, {'x': 4, 'y': 7, 'name': '(4 | 7)'}]}},
                 {'text': 'Hat die Gleichung nur eine Lösung, ist die Gerade eine Tangente.',
                  'bild': {'graphen': [{'art': 'poly', 'k': [-1, -2, 1], 'name': 'Ball'}, {'art': 'linear', 'm': 2, 't': -5, 'name': 'Tangente'}],
                           'punkte': [{'x': 2, 'y': -1, 'name': '(2 | −1)'}]}}],
    'fehler': 'Nicht x² − 2x − 1 = 0 lösen. Das sind die Nullstellen des Balls, nicht die Treffpunkte mit dem Seil. Erst gleichsetzen!',
    'fehler_bild': {'graphen': [{'art': 'poly', 'k': [-1, -2, 1], 'name': 'Ball'}, {'art': 'linear', 'm': 1, 't': 3, 'name': 'Seil'}],
                    'punkte': [{'x': -0.414, 'y': 0, 'name': 'Nullstelle?'}, {'x': 2.414, 'y': 0, 'name': 'Nullstelle?'}]},
    'regel': 'Gleichsetzen, auf null bringen, lösen. Zwei Lösungen: zwei Schnittpunkte; eine: ⟦Tangente⟧; keine: kein gemeinsamer Punkt.',
    'probe': '(4 | 7) liegt auch auf dem Ball: 4² − 2 · 4 − 1 = 7.',
}


def _sp_lage(r1, r2, m=None, t=None, a=1):
    """Parabel y = a·x² + b·x + c und Gerade y = m·x + t mit den Schnittstellen r1 < r2 (a·(x − r1)(x − r2) = Parabel − Gerade)."""
    m = R.choice([-3, -2, -1, 1, 2, 3]) if m is None else m
    t = R.choice([-4, -3, -2, -1, 1, 2, 3, 4]) if t is None else t
    b = m - a * (r1 + r2)
    c = t + a * r1 * r2
    return b, c, m, t


def _sp_wurzeln():
    r1, r2 = sorted(R.sample([x for x in range(-4, 6) if x != 0], 2))
    return r1, r2


def _sp_punkte_aufgabe(text_vor='', a=1):
    r1, r2 = _sp_wurzeln()
    b, c, m, t = _sp_lage(r1, r2, a=a)
    p, g = poly(a, b, c), poly(m, t)
    y1, y2 = m * r1 + t, m * r2 + t
    links = poly(a, b - m, c - t)
    return luecken(f'{text_vor}Berechne die Schnittpunkte der Parabel y = {p} mit der Geraden y = {g} (kleineres x zuerst).', SP2,
                   'x und y des ersten, dann des zweiten Punkts',
                   [r1, y1, r2, y2],
                   f'Gleichsetzen: {p} = {g}, also {links} = 0. Lösungen x = {dz(r1)} und x = {dz(r2)}. '
                   f'In die Gerade: y = {dz(y1)} und y = {dz(y2)}. S₁({dz(r1)} | {dz(y1)}), S₂({dz(r2)} | {dz(y2)}).',
                   'Setze die Terme gleich und bringe alles auf eine Seite. Die y-Werte bekommst du aus der Geraden.',
                   c=[str(r1), f'{m} * ({r1}) + ({t})', str(r2), f'{m} * ({r2}) + ({t})'])


def _sp_anzahl(soll):
    """Parabel y = x² + bx + c, Gerade y = mx + t, Differenz x² + px + q mit D = p² − 4q passend zu soll."""
    while True:
        p = R.choice([-4, -2, 2, 4, -6, 6])
        q = {2: R.choice([-3, -2, -1, 0]), 1: (p * p) // 4, 0: (p * p) // 4 + R.choice([1, 2, 3])}[soll]
        m, t = R.choice([-2, -1, 1, 2, 3]), R.choice([-3, -2, -1, 1, 2, 3])
        b, c = p + m, q + t
        if b != 0: break
    D = p * p - 4 * q
    return poly(1, b, c), poly(m, t), poly(1, p, q), D


def schnitt_aufgaben():
    L = []

    def neu(pool, s, art, a):
        a['l'] = SP_L
        L.append((pool, s, art, a))

    # Stufe 1: Normalparabel y = x² und Gerade, x-Werte; Gleichung aufstellen
    for _ in range(2):
        r1, r2 = _sp_wurzeln()
        m, t = r1 + r2, -r1 * r2
        while m == 0:
            r1, r2 = _sp_wurzeln(); m, t = r1 + r2, -r1 * r2
        g = poly(m, t)
        neu('uebung', 1, '', luecken(f'An welchen Stellen x schneidet die Gerade y = {g} die Parabel y = x²? (kleinere zuerst)', X2, 'zwei ganze Zahlen',
                                     [r1, r2], f'x² = {g}, also {poly(1, -m, -t)} = 0. Lösungen: x = {dz(r1)} und x = {dz(r2)}.',
                                     'Setze x² gleich dem Geradenterm und bringe alles auf eine Seite.', c=[str(r1), str(r2)]))
    for (pb, pc, m, t) in [(0, 1, 3, -1), (0, -2, -2, 1)]:
        p, g = poly(1, pb, pc), poly(m, t)
        richtig = poly(1, pb - m, pc - t) + ' = 0'
        falsch = [poly(1, pb + m, pc - t) + ' = 0', poly(1, pb - m, pc + t) + ' = 0', poly(1, pb, pc) + ' = 0']
        neu('uebung', 1, '', auswahl(f'Welche Gleichung löst du, um die Schnittstellen von y = {p} und y = {g} zu finden?', richtig, falsch,
                                     f'Gleichsetzen: {p} = {g}. Alles nach links: {richtig}.',
                                     'Setze beide Terme gleich. Was rechts steht, kommt mit umgekehrtem Vorzeichen nach links.'))
    # Stufe 2
    neu('uebung', 2, '', _sp_punkte_aufgabe())
    neu('uebung', 2, '', _sp_punkte_aufgabe())
    pp, gg, dd, D = _sp_anzahl(0)
    neu('uebung', 2, '', zahl(f'Wie viele gemeinsame Punkte haben die Parabel y = {pp} und die Gerade y = {gg}?',
                              f'Gleichsetzen ergibt {dd} = 0. Diskriminante D = {dz(D)} < 0: keine Lösung, also 0 gemeinsame Punkte.',
                              'Gleichsetzen, auf null bringen und die Diskriminante berechnen.', 0, '0'))
    pp, gg, dd, D = _sp_anzahl(1)
    neu('uebung', 2, '', zahl(f'Wie viele gemeinsame Punkte haben die Parabel y = {pp} und die Gerade y = {gg}?',
                              f'Gleichsetzen ergibt {dd} = 0. Diskriminante D = 0: genau eine Lösung. Die Gerade ist eine Tangente, 1 gemeinsamer Punkt.',
                              'Gleichsetzen, auf null bringen und die Diskriminante berechnen.', 1, '1'))
    neu('uebung', 2, '', luecken('Berechne die Schnittpunkte der Parabeln y = x² − 4 und y = −x² + 2x + 8 (kleineres x zuerst).', SP2,
                                 'x und y des ersten, dann des zweiten Punkts', [-2, 0, 3, 5],
                                 'Gleichsetzen: x² − 4 = −x² + 2x + 8, also 2x² − 2x − 12 = 0 bzw. x² − x − 6 = 0. x = −2 oder x = 3. '
                                 'In y = x² − 4: y = 0 und y = 5.',
                                 'Auch zwei Parabeln schneidest du durch Gleichsetzen.', c=['-2', '(-2) ** 2 - 4', '3', '3 ** 2 - 4']))
    neu('uebung', 2, '', auswahl('Gleichsetzen von Parabel und Gerade ergibt x² − 6x + 9 = 0. Was bedeutet das?',
                                 'Die Gerade berührt die Parabel in genau einem Punkt.',
                                 ['Die Gerade schneidet die Parabel in zwei Punkten.', 'Gerade und Parabel haben keinen gemeinsamen Punkt.',
                                  'Der gemeinsame Punkt liegt auf der x-Achse bei x = 9.'],
                                 'D = 36 − 36 = 0: genau eine Lösung x = 3. Die Gerade ist eine Tangente.', 'Berechne die Diskriminante.'))
    # Stufe 3
    neu('uebung', 3, 'pruefung', zahl('Die Gerade g: y = 0,5x + 1 schneidet die Parabel p: y = 0,5x² − 2x + 1 im Punkt P(0 | 1) und in einem zweiten Punkt Q. '
                                      'Berechne die y-Koordinate von Q.',
                                      'Gleichsetzen: 0,5x² − 2x + 1 = 0,5x + 1, also 0,5x² − 2,5x = 0, x(0,5x − 2,5) = 0. '
                                      'x = 0 (das ist P) oder x = 5. y = 0,5 · 5 + 1 = 3,5.',
                                      'Nach dem Gleichsetzen fehlt das Zahlglied: Klammere x aus.', Fr(7, 2), '0.5 * 5 + 1'))
    neu('uebung', 3, 'pruefung', zahl('Für welchen Wert von t ist die Gerade y = 2x + t eine Tangente an die Parabel y = x²?',
                                      'x² = 2x + t, also x² − 2x − t = 0. Tangente heißt genau eine Lösung: D = 4 + 4t = 0, also t = −1.',
                                      'Tangente: Die Gleichung nach dem Gleichsetzen hat genau eine Lösung. Wann ist D = 0?', -1, '-4 / 4'))
    neu('uebung', 3, 'pruefung', zahl('Die Gerade y = x + 1 schneidet die Parabel y = x² − 1 in zwei Punkten P und Q. '
                                      'Berechne die y-Koordinate des Mittelpunkts M der Strecke [PQ].',
                                      'x² − 1 = x + 1 ⇒ x² − x − 2 = 0 ⇒ x = −1 oder x = 2. P(−1 | 0), Q(2 | 3). '
                                      'Der Mittelpunkt hat die Mittelwerte der Koordinaten: y = (0 + 3) : 2 = 1,5.',
                                      'Erst P und Q berechnen. Der Mittelpunkt liegt genau in der Mitte: Mittelwert der y-Werte.', Fr(3, 2), '(0 + 3) / 2'))
    neu('uebung', 3, 'knobel', zahl('Eine Ursprungsgerade y = m · x mit m > 0 berührt die Parabel y = x² + 1. Bestimme m.',
                                    'x² + 1 = mx ⇒ x² − mx + 1 = 0. Berühren: D = m² − 4 = 0 ⇒ m = 2 (m > 0).',
                                    'Berühren heißt: genau eine Lösung. Stelle D in Abhängigkeit von m auf.', 2, '4 // 2'))
    neu('uebung', 3, '', zahl('Ein Wasserstrahl folgt der Kurve y = −0,2x² + 2x (x und y in m). Er trifft eine schräge Böschung y = 0,4x. '
                              'In welcher Höhe trifft der Strahl die Böschung (außer am Startpunkt)?',
                              '−0,2x² + 2x = 0,4x ⇒ −0,2x² + 1,6x = 0 ⇒ x(−0,2x + 1,6) = 0 ⇒ x = 0 oder x = 8. Höhe y = 0,4 · 8 = 3,2 m.',
                              'Gleichsetzen und x ausklammern. Die Höhe liest du an der Böschung ab.', Fr(16, 5), '0.4 * 8', einheit='m'))
    neu('uebung', 3, '', auswahl('Für welche Werte von t hat die Gerade y = 2x + t zwei Schnittpunkte mit der Parabel y = x²?', 't > −1',
                                 ['t < −1', 't = −1', 't > 1'],
                                 'x² − 2x − t = 0 hat zwei Lösungen, wenn D = 4 + 4t > 0, also t > −1. Bei t = −1 berührt die Gerade nur.',
                                 'Stelle D in Abhängigkeit von t auf. Wann ist D > 0?'))
    neu('uebung', 3, '', luecken('Berechne die Schnittpunkte der Parabeln y = x² − 2x − 3 und y = −x² + 4x + 5 (kleineres x zuerst).', SP2,
                                 'x und y des ersten, dann des zweiten Punkts', [-1, 0, 4, 5],
                                 'Gleichsetzen: 2x² − 6x − 8 = 0 ⇒ x² − 3x − 4 = 0 ⇒ x = −1 oder x = 4. In y = x² − 2x − 3: y = 0 und y = 5.',
                                 'Gleichsetzen, auf null bringen und durch den Faktor vor x² teilen.',
                                 c=['-1', '(-1) ** 2 - 2 * (-1) - 3', '4', '4 ** 2 - 2 * 4 - 3']))
    neu('uebung', 3, '', auswahl('Jemand setzt y = x² + 2x und y = 4x + 3 gleich und schreibt: x² + 2x − 4x + 3 = 0. Was stimmt?',
                                 'Falsch: Es muss x² − 2x − 3 = 0 heißen, die 3 wechselt das Vorzeichen.',
                                 ['Richtig.', 'Falsch: Es muss x² + 6x + 3 = 0 heißen.', 'Falsch: Man darf nicht gleichsetzen, sondern muss y = 0 setzen.'],
                                 'Von x² + 2x = 4x + 3 auf beiden Seiten 4x und 3 abziehen: x² − 2x − 3 = 0.',
                                 'Was passiert mit + 3, wenn es auf die linke Seite kommt?'))
    # Test, Korrektur, Sicherung (Stufe 2, ohne Tipp)
    neu('test', 2, '', _sp_punkte_aufgabe())
    for _ in range(3): neu('korrektur', 2, '', _sp_punkte_aufgabe())
    for _ in range(3): neu('sicherung', 2, '', _sp_punkte_aufgabe())
    for soll in (0, 1, 2):
        pp, gg, dd, D = _sp_anzahl(soll)
        n = {0: 'keine Lösung, 0 gemeinsame Punkte', 1: 'genau eine Lösung (Tangente), 1 gemeinsamer Punkt', 2: 'zwei Lösungen, 2 Schnittpunkte'}[soll]
        rel = {0: '< 0', 1: '= 0', 2: '> 0'}[soll]
        neu('sicherung', 2, '', zahl(f'Wie viele gemeinsame Punkte haben die Parabel y = {pp} und die Gerade y = {gg}?',
                                     f'Gleichsetzen ergibt {dd} = 0. D = {dz(D)} {rel.split()[0]} 0: {n}.' if soll != 1 else f'Gleichsetzen ergibt {dd} = 0. D = 0: {n}.',
                                     'Gleichsetzen, D berechnen.', soll, str(soll)))
    return L

if __name__ == '__main__':
    d = bauen('funktionen.quadratisch',
          'Parabeln in Scheitelform und allgemeiner Form deuten, Nullstellen bestimmen, Terme aufstellen und Extremwertprobleme lösen.',
          ['Scheitelform y = a(x − d)² + e: Scheitel S(d | e).', 'a > 0 nach oben, a < 0 nach unten; |a| > 1 gestreckt, |a| < 1 gestaucht.',
           'Nullstellen: y = 0 setzen. Anzahl über D oder Scheitel und Öffnung.', 'Extremwert = y-Wert des Scheitels.'],
          [('Parabeln lesen', ['scheitel', 'parameter', 'umformen']), ('Rechnen mit dem Term', ['nullstellen', 'punkte', 'bestimmen']),
           ('Anwenden', ['extremwert'])],
          ETAPPEN, GEN,
          meiden={'scheitel': ['y = 2(x + 3)² − 5 '], 'umformen': ['y = x² − 6x + 5.'], 'nullstellen': ['y = x² − 2x − 8.'],
                  'bestimmen': ['S(1 | −2) und geht durch P(3 | 6)'], 'extremwert': ['mit 20 m Zaun']},
          offen=['Parabel durch drei Punkte kommt auch im Thema gleichungen.lgs3 vor (dort ausführlich), hier nur als Stufe-3-Variante.'])
    anhaengen(d, 9907, schwer)
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden
    einbauen('funktionen.quadratisch', KARTE_SP, 'bestimmen', 18_9_1, schnitt_aufgaben)  # Achtzehnte Runde: Lehrplan-Lücke


# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl9) ----
from _durchsicht_kl9 import Befunde as _DSB, durchsicht  # noqa: E402

DS = _DSB('funktionen.quadratisch', 19_9_3)
# scheitel: a(x − d)² + e ablesen ist genau das Beispiel der Karte → Stufe 1; umgestellte Terme (7 − 3(x − 8)²) sind die Abwandlung → Stufe 2
for _f in ('2(x + 6)² − 1', '2(x + 2)² − 2', '4(x + 2)² − 1', '2(x + 8)² − 2', '−3(x + 3)² − 1', '0,5(x − 4)² − 1'):
    DS.stufe('scheitel', f'Gib den Scheitel der Parabel y = {_f} an.', 1)
for _f in ('7 − 3(x − 8)²', '−5 + 2(x − 4)²', '−8 + 4(x − 1)²', '−5 + 4(x + 6)²'):
    DS.stufe('scheitel', f'Gib den Scheitel der Parabel y = {_f} an.', 2)
# parameter: Verschieben ist Stufe 1; Nullstellenzahl am Scheitel ist Stufe 2
DS.stufe('parameter', 'Die Normalparabel wird um 5 nach rechts und um 3 nach oben verschoben. Welche Gleichung hat die neue Parabel?', 1)
DS.stufe('parameter', 'Die Normalparabel wird um 5 nach rechts verschoben. Welche Gleichung gehört zum neuen Graphen?', 1)
DS.stufe('parameter', 'Wie entsteht der Graph von g mit g(x) = (x + 2)² − 3 aus der Normalparabel?', 1)
DS.stufe('parameter', 'Ohne zu rechnen: Wie viele Nullstellen hat y = −2(x − 4)²?', 2)
DS.stufe('parameter', 'Ohne zu rechnen: Wie viele Nullstellen hat y = −2(x + 2)²?', 2)
# umformen: a = 1 ist Stufe 1, a = −1 Stufe 2; a ≠ ±1 (ausklammern) zeigt die Karte jetzt in Schritt 5; dazu zwei Aufgaben mit anderem Gedanken
for _t in ('Bestimme den Scheitel von y = x² − 4x + 4.', 'Bestimme den Scheitel von y = x² − 14x + 42.', 'Bringe y = x² − 2x + 3 in Scheitelform und gib den Scheitel an.'):
    DS.stufe('umformen', _t, 1)
for _t in ('Bestimme den Scheitel von y = −x² + 2x + 5.', 'Bestimme den Scheitel von y = −x² + 2x − 10.', 'Bringe y = −x² + 6x − 5 in Scheitelform.'):
    DS.stufe('umformen', _t, 2)
DS.neu('umformen', 3, DS.A('Jemand rechnet: y = x² + 8x + 10 = (x + 8)² − 54. Was stimmt?', 'Falsch: In die Klammer gehört die Hälfte von 8: y = (x + 4)² − 6.',
                           ['Richtig, denn 8² = 64 und 64 − 54 = 10.', 'Falsch: y = (x + 4)² + 10.', 'Falsch: y = (x − 4)² − 6.'],
                           '(x + 8)² = x² + 16x + 64 – das hat 16x, nicht 8x. Richtig: x² + 8x + 16 − 16 + 10 = (x + 4)² − 6.',
                           'Multipliziere (x + 8)² zur Probe aus. Stimmt das x-Glied?'))
DS.neu('umformen', 3, DS.Z('Die Parabel y = x² + bx + 5 hat ihren Scheitel bei x = 3. Bestimme b.', -6, '-2 * 3',
                           'Scheitelform (x − 3)² + e = x² − 6x + 9 + e. Das x-Glied muss −6x sein, also b = −6.',
                           'Rückwärts: Welche Klammer (x − d)² gehört zu x = 3? Multipliziere sie aus.'))
# nullstellen: Lösungsformel und Diskriminante sind Stufe 2
DS.stufe('nullstellen', 'Bestimme die Nullstellen von f(x) = 2x² − 8x − 10.', 2)
DS.stufe('nullstellen', 'Wie viele Nullstellen hat die Funktion f mit f(x) = −x² − 8x − 16?', 2)
DS.stufe('nullstellen', 'Wie viele Nullstellen hat die Funktion f mit f(x) = −4x² − 16x − 16?', 2)
DS.fuer_sebastian('funktionen.quadratisch/nullstellen: die Stufe-3-Aufgabe „Parabel und Gerade schneiden sich zweimal“ überschneidet sich mit der neuen Karte „schnittpunkte“ (bleibt, kein Fehler).')
# punkte: Funktionswert berechnen ist Stufe 1 (auch als Q(−3 | v)); Kugelstoßen = Einsetzen mit Einkleidung → Stufe 2
DS.stufe('punkte', 'Berechne f(−2) für f(x) = −x² + 3x + 1.', 1)
DS.stufe('punkte', 'Q(−3 | v) liegt auf dem Graphen von y = −x² − 2x. Bestimme v.', 1)
DS.stufe('punkte', 'Die Bahn einer Kugel beim Kugelstoßen: h(x) = −0,1x² + 0,9x + 2 (x waagrechte Entfernung, h Höhe, beides in m). In welcher Höhe ist die Kugel 5 m vom Abstoß entfernt?', 2)
# bestimmen: Scheitel + Punkt ist das Beispiel (Stufe 1); Nullstellen + Punkt ist die Abwandlung (Stufe 2)
for _t in ('Eine Parabel hat den Scheitel S(−4 | −4) und geht durch P(−5 | −7). Bestimme a in y = a(x − d)² + e.',
           'Eine Parabel hat den Scheitel S(−1 | 3) und geht durch P(2 | 30). Bestimme a in y = a(x − d)² + e.',
           'Eine Parabel hat den Scheitel S(2 | 2) und geht durch P(−1 | −16). Bestimme a in y = a(x − d)² + e.',
           'Die Parabel y = a(x − 1)² + 3 geht durch P(3 | 11). Bestimme a.'):
    DS.stufe('bestimmen', _t, 1)
for _t in ('Eine Parabel hat die Nullstellen x₁ = −6 und x₂ = 3 und geht durch P(0 | 54). Bestimme a in y = a(x − x₁)(x − x₂).',
           'Eine Parabel hat die Nullstellen x₁ = −2 und x₂ = 0 und geht durch P(4 | −48). Bestimme a in y = a(x − x₁)(x − x₂).',
           'Eine Parabel hat die Nullstellen x₁ = −3 und x₂ = −1 und geht durch P(3 | −72). Bestimme a in y = a(x − x₁)(x − x₂).',
           'Eine Parabel hat die Nullstellen x₁ = −4 und x₂ = 4 und geht durch P(0 | 32). Bestimme a in y = a(x − x₁)(x − x₂).'):
    DS.stufe('bestimmen', _t, 2)

# extremwert: kleinster/größter Wert einer gegebenen Funktion ist Stufe 1; zwei der vier Hauswand-Aufgaben auf Stufe 2; unklare Frage ersetzt
DS.stufe('extremwert', 'Wie groß ist der kleinste Funktionswert von y = (x − 3)² + 7?', 1)
DS.stufe('extremwert', 'Wie groß ist der größte Funktionswert von f(x) = −x² + 8x?', 1)
DS.stufe('extremwert', 'An einer Hauswand soll ein rechteckiger Auslauf mit 108 m Zaun abgegrenzt werden (die Wand ersetzt eine Seite). Welche Fläche ist höchstens möglich?', 2)
DS.stufe('extremwert', 'An einer Hauswand soll ein rechteckiger Auslauf mit 76 m Zaun abgegrenzt werden (die Wand ersetzt eine Seite). Welche Fläche ist höchstens möglich?', 2)
DS.ersetze('extremwert', 'Die Differenz zweier Zahlen ist 10. Wie klein kann ihr Produkt höchstens werden?',
           DS.Z('Die Differenz zweier Zahlen ist 10. Welchen kleinsten Wert kann ihr Produkt annehmen?', -25, '(-5) * 5',
                'Zahlen x und x + 10: P(x) = x² + 10x = (x + 5)² − 25. Kleinster Wert −25 bei x = −5 (die Zahlen −5 und 5).',
                'Nenne die kleinere Zahl x. Wie heißt die größere? Bilde das Produkt und suche den Scheitel.'))

DS_KARTEN = {
    'umformen': {
        'schritte': [{'text': 'Die Hälfte von 6 ist 3, und 3² = 9.'},
                     {'text': 'Plus 9 minus 9: y = x² − 6x + 9 − 9 + 5.'},
                     {'text': 'Zusammengefasst: y = (x − 3)² − 4.'},
                     {'text': 'Der Scheitel ist ⟦S(3 | −4)⟧.', 'bild': {'punkte': [{'x': 3, 'y': -4, 'name': 'S(3 | −4)'}]}},
                     {'text': 'Bei 2x² − 8x + 3 zuerst 2 ausklammern: 2(x² − 4x) + 3.'}],
    },
}

if __name__ == '__main__':
    durchsicht('funktionen.quadratisch', DS, DS_KARTEN)


# ---- STUFEN (Zwanzigste Runde, Zweig stufen-kl9) ----
from _stufen_kl9 import Stufen, stufen  # noqa: E402

ST = Stufen('funktionen.quadratisch', 20_9_3)
Z, A, L = ST.Z, ST.A, ST.L
_S = 'S(□ | □)'

# scheitel
ST.stufenleiter('scheitel', 'Den Scheitel aus der Scheitelform oder einem Graphen ablesen.',
                'Umgestellte Terme (−5 + 2(x − 4)²) lesen, aus Scheitel und Öffnung die Gleichung aufstellen.',
                'Wertemenge, Scheitel aus Nullstellen oder gleich hohen Punkten, Fehler beim Vorzeichen, Bedingung für e, mehrteilige Sachaufgabe.')
ST.typ('scheitel', 'Lies den Scheitel', 'erkennen')
ST.typ('scheitel', '/^Gib den Scheitel der Parabel y = (x²|\\(x|\\d|0,5)/', 'direkt')
ST.typ('scheitel', 'Normalparabel, Scheitel', 'umkehr')
ST.typ('scheitel', '/^Gib den Scheitel der Parabel y = (−|7)/', 'mehrschritt')
ST.typ('scheitel', 'Wo liegt der höchste Punkt', 'darstellung')
ST.typ('scheitel', '/^(Welche Wertemenge|Eine Parabel y = \\(x − x₁\\)|Gib den Scheitel von y = \\(x)/', 'verknuepfen')
ST.typ('scheitel', 'Die Parabel y = (x − d)² + e geht durch', 'rueckwaerts')
ST.neu('scheitel', 'fehler', A('Jemand liest bei y = 2(x − 1)² + 3 den Scheitel S(2 | 3) ab. Was stimmt?', 'Falsch: Die 2 ist der Streckfaktor; S(1 | 3).', ['Richtig.', 'Falsch: S(−1 | 3).', 'Falsch: S(1 | 6).'],
       'In y = a(x − d)² + e ist S(d | e). Hier a = 2, d = 1, e = 3. Der Faktor a ändert die Lage des Scheitels nicht.', 'Welche Zahl in der Klammer steht hinter x?'))
ST.neu('scheitel', 'begruenden', A('Stimmt: Jede Parabel y = a(x − 2)² + 1 mit a > 0 hat keine Nullstelle?', 'Ja: Der tiefste Punkt S(2 | 1) liegt über der x-Achse.',
       ['Nein, für großes a hat sie zwei Nullstellen.', 'Nein, sie hat immer genau eine Nullstelle bei x = 2.', 'Das hängt von a ab.'],
       'Mit a > 0 ist die Parabel nach oben geöffnet, ihr kleinster Wert ist e = 1 > 0. Sie erreicht die x-Achse nie.', 'Wo liegt der tiefste Punkt?'))
ST.neu('scheitel', 'parameter', Z('Für welche Zahl e geht die Parabel y = (x − 2)² + e durch den Ursprung?', -4, '0 - (0 - 2) ** 2',
       'Ursprung einsetzen: 0 = (0 − 2)² + e = 4 + e, also e = −4. Der Scheitel ist S(2 | −4).', 'Setze den Punkt (0 | 0) ein.'))
ST.neu('scheitel', 'pruefung', L('Ein Wasserstrahl folgt der Kurve y = −0,5(x − 4)² + 8 (x, y in m). a) Gib den höchsten Punkt an. b) Wie hoch ist der Strahl bei x = 2?', 'a) S(□ | □); b) □ m', [4, 8, 6], ['4', '8', '-0.5 * (2 - 4) ** 2 + 8'],
       'a) Scheitelform: S(4 | 8). b) y = −0,5 · (−2)² + 8 = −2 + 8 = 6 m.', 'a) ablesen, b) einsetzen.'))
ST.knobel('scheitel', Z('Die Scheitel aller Parabeln y = (x − t)² + 2t (für jede Zahl t) liegen auf einer Geraden. Welche Steigung hat diese Gerade?', 2, '2',
          'Der Scheitel ist S(t | 2t). Für t = 0, 1, 2 erhältst du (0 | 0), (1 | 2), (2 | 4). Immer ist y = 2x. Die Gerade y = 2x hat die Steigung 2.',
          'Schreib den Scheitel für einige t auf.'))
ST.knobel('scheitel', L('Die Parabel y = (x − 3)² − 4 wird erst an der x-Achse gespiegelt und dann um 6 nach oben verschoben. Wo liegt der neue Scheitel?', _S, [3, 10], ['3', '4 + 6'],
          'Spiegeln an der x-Achse ändert das Vorzeichen jedes y-Werts: Scheitel (3 | −4) wird (3 | 4). Verschieben um 6 nach oben: (3 | 10).', 'Verfolge nur den Scheitelpunkt.'))

# parameter
ST.stufenleiter('parameter', 'Verschiebung und Öffnung einer Parabel aus a, d, e erkennen.',
                'Graphen zuordnen, Nullstellenzahl ohne Rechnen, Streckung im Sachzusammenhang.',
                'Bedingungen an a, rückwärts verschieben, Bremsweg verdoppeln, Aussagen prüfen, Fehler beim Vorzeichen, mehrteilige Aufgabe.')
ST.typ('parameter', '/^(Wie sieht die Parabel|Die Normalparabel wird|Wie entsteht)/', 'erkennen')
ST.typ('parameter', '/^(Welche Gleichung gehört zu Graph|Welcher Graph gehört)/', 'darstellung')
ST.typ('parameter', '/^(Ohne zu rechnen|Welche Parabel ist nach unten)/', 'mehrschritt')
ST.typ('parameter', 'Jemand liest', 'fehler')
ST.typ('parameter', 'Für den Bremsweg', 'transfer')
ST.typ('parameter', 'Die Parabeln y = x² + e', 'verknuepfen')
ST.typ('parameter', 'Welcher Graph ist am schmalsten', 'begruenden')
ST.neu('parameter', 'direkt', L('Lies a, d und e aus y = 3(x + 2)² − 7 ab (Form y = a(x − d)² + e).', 'a = □; d = □; e = □', [3, -2, -7], ['3', '-2', '-7'],
       'x + 2 = x − (−2), also d = −2. a = 3, e = −7.', 'Achte auf das Vorzeichen in der Klammer.'))
ST.neu('parameter', 'einkleidung', A('Eine Rutsche hat im Querschnitt die Form y = 0,25(x − 4)² (in m). Wie ist sie im Vergleich zur Normalparabel?', 'breiter, nach oben geöffnet', ['schmaler, nach oben geöffnet', 'breiter, nach unten geöffnet', 'genauso breit'],
       'a = 0,25 ist positiv und kleiner als 1: nach oben geöffnet und gestaucht (breiter).', 'Schau auf den Faktor a.'))
ST.neu('parameter', 'parameter', A('Für welche Werte von a ist y = a(x − 1)² + 2 nach unten geöffnet und schmaler als die Normalparabel?', 'a < −1', ['a > 1', '−1 < a < 0', 'a < 0'],
       'Nach unten: a < 0. Schmaler: |a| > 1. Beides zusammen: a < −1.', 'Zwei Bedingungen müssen gleichzeitig gelten.'))
ST.neu('parameter', 'rueckwaerts', L('Eine Parabel wird um 2 nach links und um 3 nach oben verschoben. Danach hat sie den Scheitel S(1 | 5). Wo lag ihr Scheitel vorher?', _S, [3, 2], ['1 + 2', '5 - 3'],
       'Rückwärts: 2 nach rechts und 3 nach unten. Aus (1 | 5) wird (3 | 2).', 'Mache die Verschiebung rückgängig.'))
ST.neu('parameter', 'begruenden', A('Stimmt: Verschiebt man eine Parabel nach oben, bleibt die Zahl ihrer Nullstellen immer gleich?', 'Nein: y = x² − 1 hat zwei Nullstellen, um 2 nach oben verschoben (y = x² + 1) keine.',
       ['Ja, verschieben ändert nur die Lage.', 'Ja, aber nur bei nach oben geöffneten Parabeln.', 'Nein, sie wird immer größer.'],
       'Gegenbeispiel genügt: Der Scheitel (0 | −1) wandert über die x-Achse, die Nullstellen verschwinden.', 'Probiere ein Beispiel mit dem Scheitel knapp unter der x-Achse.'))
ST.neu('parameter', 'pruefung', L('Gegeben ist f(x) = −2(x + 1)² + 8. a) Gib den Scheitel an. b) In welchem Punkt schneidet der Graph die y-Achse?', 'a) S(□ | □); b) (0 | □)', [-1, 8, 6], ['-1', '8', '-2 * (0 + 1) ** 2 + 8'],
       'a) S(−1 | 8). b) f(0) = −2 · 1 + 8 = 6, Punkt (0 | 6).', 'Für die y-Achse x = 0 einsetzen.'))
ST.knobel('parameter', L('Die Normalparabel wird um d nach rechts verschoben (d > 0). Die neue Parabel geht durch (5 | 9). Welche Werte kann d haben? (kleineres zuerst)', 'd₁ = □; d₂ = □', [2, 8], ['5 - 3', '5 + 3'],
          'Neue Parabel y = (x − d)². Einsetzen: 9 = (5 − d)², also 5 − d = 3 oder 5 − d = −3. Daraus d = 2 oder d = 8. Beide sind positiv, beide passen.',
          'Eine Zahl, deren Quadrat 9 ist, kann zwei Werte haben.'))
ST.knobel('parameter', Z('Wie viele der Parabeln y = (x − d)² + e mit d und e aus {−1; 0; 1} gehen durch den Ursprung?', 3, '1 + 2',
          'Ursprung einsetzen: 0 = d² + e, also e = −d². d = 0 verlangt e = 0 (eine Parabel). d = 1 oder d = −1 verlangt e = −1 (zwei Parabeln). Zusammen 3.',
          'Setze (0 | 0) ein und überlege, welche Paare passen.'))

# umformen
ST.stufenleiter('umformen', 'Bei a = 1 quadratisch ergänzen oder x = −b/(2a) nutzen.',
                'Bei a = −1 oder a ≠ 1 erst ausklammern, ausmultiplizieren rückwärts, höchster Punkt einer Bahn.',
                'Bedingungen für b und c, Fehler bei der Ergänzung, halbe Zahlen, Aussagen über Nullstellen, Gewinn maximieren, mehrteilige Aufgabe.')
ST.typ('umformen', '/^(Bei y = x²|Bestimme den Scheitel von y = x²|Bringe y = x²)/', 'direkt')
ST.typ('umformen', '/^(Bestimme den Scheitel von y = −?[\\d,]*x²|Bringe y = −x²|Bestimme den Scheitel von y = −x²)/', 'mehrschritt')
ST.typ('umformen', 'Multipliziere', 'umkehr')
ST.typ('umformen', 'Für welche Zahl c', 'parameter')
ST.typ('umformen', 'Jemand rechnet', 'fehler')
ST.typ('umformen', 'Die Parabel y = x² + bx + 5', 'rueckwaerts')
ST.neu('umformen', 'erkennen', A('Welche Zahl brauchst du als quadratische Ergänzung bei x² − 10x?', '25', ['100', '10', '5'],
       'Hälfte von 10 ist 5, und 5² = 25: x² − 10x + 25 = (x − 5)².', 'Halbiere die Zahl vor x und quadriere.'))
ST.neu('umformen', 'einkleidung', Z('Die Flugbahn eines Balls ist h(x) = −x² + 4x + 1 (x und h in m). Wie hoch fliegt er höchstens?', 5, '-(2 ** 2) + 4 * 2 + 1',
       'h(x) = −(x² − 4x) + 1 = −(x − 2)² + 4 + 1 = −(x − 2)² + 5. Höchster Punkt bei x = 2, Höhe 5 m.', 'Bring den Term in Scheitelform.', einheit='m'))
ST.neu('umformen', 'begruenden', A('Stimmt: y = x² + 6x + 10 hat keine Nullstelle?', 'Ja, denn y = (x + 3)² + 1 ist immer mindestens 1.', ['Nein, x = −3 ist Nullstelle.', 'Nein, sie hat zwei Nullstellen.', 'Das kann man ohne Formel nicht sagen.'],
       'Quadratische Ergänzung: x² + 6x + 9 + 1 = (x + 3)² + 1. Ein Quadrat ist nie negativ, also ist y ≥ 1.', 'Ergänze quadratisch.'))
ST.neu('umformen', 'transfer', Z('Für den Gewinn eines Kiosks gilt G(x) = −2x² + 40x − 150 (x Preis eines Artikels in €, G in €). Bei welchem Preis ist der Gewinn am größten?', 10, '40 // 4',
       'G(x) = −2(x² − 20x) − 150 = −2(x − 10)² + 200 − 150. Der Scheitel liegt bei x = 10: Preis 10 €, Gewinn 50 €.', 'Klammere −2 aus und ergänze.', einheit='€'))
ST.neu('umformen', 'pruefung', L('Gegeben ist f(x) = 0,5x² − 4x + 5. a) Bringe f in Scheitelform. b) Gib den Scheitel an.', 'a) f(x) = 0,5(x − □)² − □; b) S(□ | □)', [4, 3, 4, -3], ['4', '3', '4', '0.5 * 16 - 16 + 5'],
       'a) 0,5(x² − 8x) + 5 = 0,5(x² − 8x + 16) − 8 + 5 = 0,5(x − 4)² − 3. b) S(4 | −3).', 'Klammere zuerst 0,5 aus.'))
ST.neu('umformen', 'verknuepfen', Z('Bestimme die y-Koordinate des Scheitels von y = x² − 5x + 4.', -2.25, '2.5 ** 2 - 5 * 2.5 + 4',
       'Halbe Zahl: 5 : 2 = 2,5, Ergänzung 6,25. y = (x − 2,5)² − 6,25 + 4 = (x − 2,5)² − 2,25.', 'Die Ergänzung ist hier eine Dezimalzahl.'))
ST.neu('umformen', 'parameter', Z('Für welche positive Zahl b liegt der Scheitel von y = x² + bx + 13 auf der Höhe y = 4?', 6, '6',
       'Ergänzen: y = (x + b/2)² + 13 − b²/4. Also 13 − b²/4 = 4, b²/4 = 9, b² = 36, b = 6 (positiv).', 'Schreib die y-Koordinate des Scheitels mit b auf.'))
ST.knobel('umformen', Z('Für welche Zahl c haben y = x² − 6x + c und y = −x² + 6x − c denselben Scheitel?', 9, '9',
          'Erste Parabel: (x − 3)² + c − 9, Scheitel (3 | c − 9). Zweite: −(x − 3)² + 9 − c, Scheitel (3 | 9 − c). Gleich, wenn c − 9 = 9 − c, also c = 9. Dann liegt der gemeinsame Scheitel auf der x-Achse.',
          'Die zweite Parabel ist das Spiegelbild der ersten an der x-Achse.'))
ST.knobel('umformen', Z('Für wie viele ganze Zahlen b liegt der Scheitel von y = x² + bx + 10 oberhalb der x-Achse?', 13, '2 * 6 + 1',
          'Scheitelhöhe: 10 − b²/4 > 0, also b² < 40. Ganze b mit b² < 40: −6, −5, …, 5, 6 (6² = 36 < 40, 7² = 49). Das sind 13 Zahlen.',
          'Schreib die Höhe des Scheitels als Term mit b.'))

# nullstellen
ST.stufenleiter('nullstellen', 'Nullstellen aus der Produktform oder einem Graphen ablesen.',
                'Mit der Lösungsformel oder der Scheitelform rechnen, Nullstellenzahl bestimmen, Gleichung zu gegebenen Nullstellen, Landepunkt.',
                'Zweite Nullstelle aus einer bekannten, Bedingung für c, Fehler beim Ablesen, Tor-Breite, mehrteilige Aufgabe.')
ST.typ('nullstellen', 'Lies die Nullstellen', 'erkennen')
ST.typ('nullstellen', '/^Bestimme die Nullstellen von y = \\(x [+−] \\d+\\) ·/', 'direkt')
ST.typ('nullstellen', '/^Bestimme die Nullstellen von y = −?\\(x/', 'mehrschritt')
ST.typ('nullstellen', 'Wie viele Nullstellen hat die Funktion f mit f(x) = x² + x + 3', 'verknuepfen')
ST.typ('nullstellen', '/^(Bestimme die Nullstellen|Wie viele Nullstellen)/', 'mehrschritt')
ST.typ('nullstellen', 'Welche Funktion hat genau eine', 'begruenden')
ST.typ('nullstellen', 'Die Parabel y = x² + bx + 12', 'rueckwaerts')
ST.typ('nullstellen', 'Die Parabel y = x² − 2x − 3 und', 'verknuepfen')
ST.neu('nullstellen', 'einkleidung', Z('Ein Ball fliegt auf der Bahn h(x) = −0,25x² + x + 3 (x und h in m). In welcher Entfernung x > 0 landet er (h = 0)?', 6, '6',
       '−0,25x² + x + 3 = 0, mal (−4): x² − 4x − 12 = 0. D = 16 + 48 = 64, x = (4 ± 8) : 2, also x = 6 oder x = −2. Positiv: x = 6 m. Probe: −9 + 6 + 3 = 0.', 'Setze h = 0 und mache den Faktor vor x² zu 1.', einheit='m'))
ST.neu('nullstellen', 'umkehr', L('Eine Parabel y = x² + bx + c hat die Nullstellen 2 und 7. Bestimme b und c.', 'b = □; c = □', [-9, 14], ['-(2 + 7)', '2 * 7'],
       'y = (x − 2)(x − 7) = x² − 9x + 14. Also b = −9 und c = 14.', 'Schreib die Produktform und multipliziere aus.'))
ST.neu('nullstellen', 'fehler', A('Jemand liest bei y = (x − 3)(x + 2) die Nullstellen −3 und 2 ab. Was stimmt?', 'Falsch: Die Nullstellen sind 3 und −2.', ['Richtig.', 'Falsch: Die Nullstellen sind 3 und 2.', 'Falsch: Es gibt nur die Nullstelle −6.'],
       'Ein Produkt ist 0, wenn ein Faktor 0 ist: x − 3 = 0 bei x = 3, x + 2 = 0 bei x = −2.', 'Setze jeden Faktor gleich 0.'))
ST.neu('nullstellen', 'parameter', A('Für welche Werte von c hat y = x² + 6x + c zwei Nullstellen?', 'c < 9', ['c > 9', 'c = 9', 'c < 3'],
       'D = 36 − 4c > 0 heißt c < 9. Bei c = 9 ist y = (x + 3)², eine Nullstelle.', 'Die Diskriminante muss positiv sein.'))
ST.neu('nullstellen', 'transfer', Z('Ein Torbogen hat die Form y = −0,5x² + 2x (x, y in m, der Boden ist y = 0). Wie breit ist das Tor am Boden?', 4, '2 / 0.5',
       'Nullstellen: x(−0,5x + 2) = 0, also x = 0 und x = 4. Breite 4 m.', 'Klammere x aus.', einheit='m'))
ST.neu('nullstellen', 'pruefung', L('Gegeben ist f(x) = x² − 2x − 15. a) Bestimme die Nullstellen (kleinere zuerst). b) Gib den Scheitel an.', 'a) x₁ = □; x₂ = □; b) S(□ | □)', [-3, 5, 1, -16], ['-3', '5', '(-3 + 5) // 2', '1 - 2 - 15'],
       'a) D = 4 + 60 = 64, x = (2 ± 8) : 2, also x = −3 und x = 5. b) Der Scheitel liegt mittig: x = 1, f(1) = 1 − 2 − 15 = −16.', 'Der Scheitel liegt in der Mitte zwischen den Nullstellen.'))
ST.knobel('nullstellen', L('Die Parabel y = x² + bx + c hat die Nullstellen 2 und 5. Welche Nullstellen hat dann y = x² − bx + c? (kleinere zuerst)', 'x₁ = □; x₂ = □', [-5, -2], ['-5', '-2'],
          'Aus (x − 2)(x − 5) = x² − 7x + 10 folgt b = −7, c = 10. Dann y = x² + 7x + 10 = (x + 2)(x + 5) mit den Nullstellen −5 und −2. Allgemein: b umdrehen spiegelt die Parabel an der y-Achse.',
          'Bestimme zuerst b und c.'))
ST.knobel('nullstellen', Z('Eine Parabel y = x² + px + q hat zwei Nullstellen mit der Summe 10 und dem Produkt 21. Welches ist ihr kleinster Funktionswert?', -4, '25 - 50 + 21',
          'Nullstellen mit Summe 10 und Produkt 21 sind 3 und 7. Also y = (x − 3)(x − 7) = x² − 10x + 21. Der Scheitel liegt in der Mitte bei x = 5: y = 25 − 50 + 21 = −4.',
          'Welche zwei Zahlen haben Summe 10 und Produkt 21?'))

# punkte
ST.stufenleiter('punkte', 'Funktionswerte berechnen und die Punktprobe machen.',
                'Werte im Sachzusammenhang, Differenzen von Funktionswerten, rückwärts f(x) = 5 lösen, Tabelle zuordnen.',
                'Unbekannte Koordinate oder Parameter c bestimmen, gleich hohe Punkte deuten, Fehler mit dem Minus vor x² finden.')
ST.typ('punkte', '/^(Berechne f\\(|Q\\(|Liegt P)/', 'direkt')
ST.typ('punkte', 'Die Bahn einer Kugel', 'einkleidung')
ST.typ('punkte', '/^P\\(u \\| \\d/', 'rueckwaerts')
ST.typ('punkte', '/^Der Punkt P\\(.*Bestimme [ca]/', 'parameter')
ST.typ('punkte', '/^(Der Punkt P\\(u \\| u\\)|A\\()/', 'verknuepfen')
ST.neu('punkte', 'erkennen', A('Welcher Punkt liegt auf der Parabel y = x² − 1?', '(2 | 3)', ['(2 | 5)', '(3 | 9)', '(−1 | 2)'],
       '2² − 1 = 3. Bei den anderen: 2² − 1 ≠ 5, 3² − 1 = 8 ≠ 9, (−1)² − 1 = 0 ≠ 2.', 'Setze die x-Werte ein.'))
ST.neu('punkte', 'mehrschritt', Z('Berechne f(2) − f(−2) für f(x) = x² + 3x − 1.', 12, '(4 + 6 - 1) - (4 - 6 - 1)',
       'f(2) = 4 + 6 − 1 = 9, f(−2) = 4 − 6 − 1 = −3. Differenz 9 − (−3) = 12.', 'Berechne beide Werte einzeln.'))
ST.neu('punkte', 'mehrschritt', Z('Berechne f(0,5) für f(x) = 4x² − 2x + 3.', 3, '4 * 0.25 - 1 + 3',
       '0,5² = 0,25. f(0,5) = 4 · 0,25 − 2 · 0,5 + 3 = 1 − 1 + 3 = 3.', 'Erst quadrieren, dann malnehmen.'))
ST.neu('punkte', 'umkehr', L('Für welche x gilt f(x) = 5 bei f(x) = x² − 4? (kleineres zuerst)', 'x₁ = □; x₂ = □', [-3, 3], ['-3', '3'],
       'x² − 4 = 5 heißt x² = 9, also x = −3 oder x = 3.', 'Setze f(x) = 5 und löse.'))
ST.neu('punkte', 'darstellung', A('Eine Tabelle zeigt: x = 0, 1, 2 gehört zu y = 3, 4, 7. Welche Funktion passt?', 'y = x² + 3', ['y = x + 3', 'y = 2x² + 3', 'y = x² + x + 3'],
       'x² + 3 gibt 3, 4, 7. x + 3 gibt 3, 4, 5; 2x² + 3 gibt 3, 5, 11; x² + x + 3 gibt 3, 5, 9.', 'Prüfe alle drei Werte.'))
ST.neu('punkte', 'einkleidung', Z('Ein Wasserstrahl folgt h(x) = −0,5x² + 2x + 1 (x und h in m). Wie hoch ist er 3 m von der Düse entfernt?', 2.5, '-0.5 * 9 + 6 + 1',
       'h(3) = −0,5 · 9 + 2 · 3 + 1 = −4,5 + 6 + 1 = 2,5 m.', 'Setze x = 3 ein.', einheit='m'))
ST.neu('punkte', 'fehler', A('Jemand rechnet für f(x) = −x² + 2 so: f(−3) = −(−3)² + 2 = 9 + 2 = 11. Was stimmt?', 'Falsch: −(−3)² = −9, also f(−3) = −7.', ['Richtig.', 'Falsch: f(−3) = −11.', 'Falsch: f(−3) = 5.'],
       'Erst quadrieren: (−3)² = 9. Das Minus davor bleibt: −9 + 2 = −7.', 'Was wird zuerst gerechnet: das Quadrat oder das Minus davor?'))
ST.knobel('punkte', Z('Eine Parabel y = x² + bx + c geht durch (1 | 3) und (2 | 9). Welchen Wert hat sie bei x = 3?', 17, '9 + 3 * 3 - 1',
          'Einsetzen: 1 + b + c = 3 und 4 + 2b + c = 9. Zweite minus erste: 3 + b = 6, also b = 3, dann c = −1. f(3) = 9 + 9 − 1 = 17.',
          'Zwei Punkte, zwei Unbekannte. Ziehe die Gleichungen voneinander ab.'))
ST.knobel('punkte', Z('Für f(x) = x² − 6x + 10: Für wie viele ganze Zahlen x ist f(x) < 5?', 3, '4 - 2 + 1',
          'Scheitelform: f(x) = (x − 3)² + 1. f(x) < 5 heißt (x − 3)² < 4. Bei ganzen x ist x − 3 dann −1, 0 oder 1 (bei ±2 wäre das Quadrat schon 4). Also x = 2, 3, 4: drei Zahlen.',
          'Bringe f in Scheitelform.'))

# bestimmen
ST.stufenleiter('bestimmen', 'Mit Scheitel und einem Punkt den Faktor a bestimmen.',
                'Mit Nullstellen ansetzen, aus Bogenmaßen oder Tabellen den Term finden, d aus einem Punkt bestimmen.',
                'Drei Punkte, Ansatz-Fehler finden, Aussagen über Eindeutigkeit, Bedingung für a, Wurfbahn modellieren, mehrteilige Aufgabe.')
ST.typ('bestimmen', '/^(Eine Parabel hat den Scheitel S\\(−?\\d+ \\| −?\\d+\\) und geht durch P|Die Parabel y = a\\(x − 1\\)|Gib die Scheitelform|Eine Parabel hat den Scheitel S\\(2 \\| −8\\)|Eine Parabel hat den Scheitel S\\(−1)/', 'direkt')
ST.typ('bestimmen', 'Eine Parabel hat die Nullstellen', 'mehrschritt')
ST.typ('bestimmen', 'Eine nach unten geöffnete Normalparabel', 'mehrschritt')
ST.typ('bestimmen', '/^(Bestimme die Parabel|Eine Parabel y = ax² \\+ c)/', 'verknuepfen')
ST.neu('bestimmen', 'erkennen', A('Welcher Ansatz passt, wenn der Scheitel S(2 | −1) bekannt ist?', 'y = a(x − 2)² − 1', ['y = a(x + 2)² − 1', 'y = a(x − 2)² + 1', 'y = ax² + 2x − 1'],
       'Scheitelform y = a(x − d)² + e mit d = 2 und e = −1.', 'Setze d und e in die Scheitelform ein.'))
ST.neu('bestimmen', 'einkleidung', Z('Ein Brückenbogen ist am Boden 40 m breit (Nullstellen bei x = 0 und x = 40) und in der Mitte 10 m hoch. Bestimme a in y = a(x − 20)² + 10.', -0.025, '-10 / 400',
       'Nullstelle (0 | 0) einsetzen: 0 = a · 400 + 10, also a = −10 : 400 = −0,025.', 'Setze eine Nullstelle ein.'))
ST.neu('bestimmen', 'umkehr', Z('Die Parabel y = 2(x − d)² + 1 geht durch (5 | 3), und es gilt d < 5. Bestimme d.', 4, '5 - 1',
       '3 = 2(5 − d)² + 1 ⇒ (5 − d)² = 1 ⇒ 5 − d = 1 (weil d < 5) ⇒ d = 4.', 'Löse nach (5 − d)² auf.'))
ST.neu('bestimmen', 'darstellung', Z('Eine Parabel y = ax² + bx + c hat die Wertetabelle x = −1, 0, 1 mit y = 6, 3, 2. Bestimme a.', 1, '(6 + 2 - 2 * 3) // 2',
       'x = 0: c = 3. x = −1: a − b + 3 = 6. x = 1: a + b + 3 = 2. Addieren: 2a + 6 = 8, a = 1.', 'Lies c direkt ab und addiere die anderen beiden Gleichungen.'))
ST.neu('bestimmen', 'mehrschritt', Z('Eine Parabel hat die Nullstellen 1 und 5, ihr Scheitel liegt auf der Höhe y = −8. Bestimme a in y = a(x − 1)(x − 5).', 2, '-8 // ((3 - 1) * (3 - 5))',
       'Der Scheitel liegt mittig bei x = 3. Dort: a · 2 · (−2) = −4a = −8, also a = 2.', 'Wo liegt der Scheitel zwischen den Nullstellen?'))
ST.neu('bestimmen', 'fehler', A('Jemand setzt für den Scheitel S(3 | 2) an: y = a(x + 3)² + 2. Was stimmt?', 'Falsch: Es heißt y = a(x − 3)² + 2.', ['Richtig.', 'Falsch: y = a(x + 3)² − 2.', 'Falsch: y = a(x − 2)² + 3.'],
       'In y = a(x − d)² + e steht d mit Minus. Bei d = 3: (x − 3).', 'Wo ist die Klammer null?'))
ST.neu('bestimmen', 'begruenden', A('Stimmt: Durch zwei Punkte mit verschiedenen x-Werten geht genau eine Parabel y = ax² + bx + c?', 'Nein, es gibt unendlich viele; man braucht drei Punkte.', ['Ja, genau eine.', 'Ja, aber nur, wenn die Punkte gleich hoch liegen.', 'Nein, es gibt keine.'],
       'Drei Unbekannte a, b, c brauchen drei Bedingungen. Durch (0 | 0) und (1 | 1) gehen z. B. y = x² und y = 2x² − x.', 'Zähle die Unbekannten.'))
ST.neu('bestimmen', 'parameter', Z('Die Parabeln y = a(x − 2)(x − 6) haben alle dieselben Nullstellen. Für welches a geht die Parabel durch (4 | 8)?', -2, '8 // ((4 - 2) * (4 - 6))',
       'Einsetzen: 8 = a · 2 · (−2) = −4a, also a = −2.', 'Setze den Punkt ein.'))
ST.neu('bestimmen', 'transfer', Z('Ein Ball wird bei x = 0 aus 2 m Höhe geworfen. Bei x = 4 m erreicht er die größte Höhe 6 m. In welcher Höhe ist er bei x = 6 m?', 5, '-0.25 * 4 + 6',
       'Scheitel S(4 | 6): y = a(x − 4)² + 6. (0 | 2): 2 = 16a + 6, a = −0,25. y(6) = −0,25 · 4 + 6 = 5 m.', 'Der höchste Punkt ist der Scheitel.', einheit='m'))
ST.neu('bestimmen', 'pruefung', L('Eine Parabel y = a(x − 1)² − 4 geht durch den Punkt P(3 | 0). a) Bestimme a. b) Schreibe die Parabel in der Form y = x² + bx + c.', 'a) a = □; b) y = x² + □x + □', [1, -2, -3], ['4 // 4', '-2', '1 - 4'],
       'a) 0 = a · 2² − 4, also a = 1. b) (x − 1)² − 4 = x² − 2x + 1 − 4 = x² − 2x − 3.', 'Binomische Formel für (x − 1)².'))
ST.knobel('bestimmen', Z('Eine Parabel hat die Nullstellen −2 und 6 und geht durch (2 | 8). Welchen Wert hat sie bei x = 4?', 6, '-0.5 * (4 + 2) * (4 - 6)',
          'Ansatz y = a(x + 2)(x − 6). (2 | 8): 8 = a · 4 · (−4) = −16a, a = −0,5. Bei x = 4: −0,5 · 6 · (−2) = 6.',
          'Setze mit den Nullstellen an.'))
ST.knobel('bestimmen', Z('Wie viele Parabeln y = ax² + bx + c mit ganzen Zahlen a, b, c, a ≠ 0 und −3 ≤ a ≤ 3 gehen durch (0 | 0) und (1 | 2)?', 6, '7 - 1',
          '(0 | 0) liefert c = 0, (1 | 2) liefert a + b = 2, also b = 2 − a. Zu jedem a gibt es genau ein b. Erlaubt sind a = −3, −2, −1, 1, 2, 3: sechs Parabeln.',
          'Was sagen die beiden Punkte über a, b und c?'))

# extremwert
ST.stufenleiter('extremwert', 'Den größten oder kleinsten Wert einer quadratischen Funktion angeben.',
                'Zielfunktion im Sachzusammenhang aufstellen (Zaun, Summe, Hauswand), rückwärts den Umfang finden.',
                'Bahnen und Preise modellieren, Fehler beim Aufstellen der Zielfunktion, Aussagen begründen, Rundung im Sachzusammenhang.')
ST.typ('extremwert', '/^Welchen (kleinsten|größten) Wert nimmt/', 'erkennen')
ST.typ('extremwert', '/^Wie groß ist der (kleinste|größte)/', 'direkt')
ST.typ('extremwert', '/^(Ein rechteckiges Gehege|An einer Hauswand)/', 'einkleidung')
ST.typ('extremwert', 'Zwei Zahlen haben die Summe', 'mehrschritt')
ST.typ('extremwert', '/^(Ein Ball fliegt|Mit 16 m Zaun)/', 'transfer')
ST.typ('extremwert', '/^(Rechtecke liegen|Die Differenz zweier)/', 'verknuepfen')
ST.typ('extremwert', 'Ein Händler', 'pruefung')
ST.neu('extremwert', 'umkehr', Z('Unter allen Rechtecken mit demselben Umfang hat das größte 49 cm² Flächeninhalt. Wie groß ist dieser Umfang?', 28, '4 * 7',
       'Die größte Fläche hat das Quadrat. 49 cm² heißt Seite 7 cm, Umfang 4 · 7 = 28 cm.', 'Welches Rechteck hat bei festem Umfang die größte Fläche?', einheit='cm'))
ST.neu('extremwert', 'fehler', A('Jemand sucht das größte Rechteck mit 40 m Umfang: A(x) = x · (40 − x), größte Fläche bei x = 20. Was stimmt?', 'Falsch: Die zweite Seite ist 20 − x; größte Fläche bei x = 10 mit 100 m².',
       ['Richtig, 400 m².', 'Falsch: größte Fläche bei x = 40.', 'Falsch: Die zweite Seite ist 40 − 2x.'],
       'Zwei Seiten zusammen sind der halbe Umfang 20 m. A(x) = x(20 − x), Scheitel bei x = 10, A = 100 m². Mit 40 − x wäre der Umfang 80 m.', 'Wie lang sind zwei Seiten zusammen?'))
ST.neu('extremwert', 'begruenden', A('Stimmt: Von allen Rechtecken mit gleichem Umfang hat das Quadrat den größten Flächeninhalt?', 'Ja: A(x) = x · (u/2 − x) hat den Scheitel bei x = u/4.',
       ['Nein, ein sehr langes Rechteck hat mehr Fläche.', 'Nur bei ganzzahligen Seiten.', 'Nein, alle haben die gleiche Fläche.'],
       'Der Scheitel liegt mittig zwischen den Nullstellen 0 und u/2, also bei x = u/4. Dann ist auch die andere Seite u/4: ein Quadrat.', 'Stelle A(x) mit dem Umfang u auf.'))
ST.knobel('extremwert', Z('Aus 60 cm Draht wird ein Rechteck gebogen, das zusätzlich eine Mittelstrebe parallel zu einer Seite bekommt. Wie groß ist die Fläche des Rechtecks höchstens?', 150, '10 * 15',
          'Drei Stücke der Länge x (zwei Seiten und die Strebe) und zwei Stücke der Länge y: 3x + 2y = 60, also y = 30 − 1,5x. A(x) = x(30 − 1,5x), Nullstellen 0 und 20, Scheitel bei x = 10. y = 15, A = 150 cm².',
          'Die Strebe ist so lang wie die Seiten, zu denen sie parallel ist.', einheit='cm²'))
ST.knobel('extremwert', Z('Zwei Zahlen haben die Summe 10. Wie groß ist die Summe ihrer Quadrate mindestens?', 50, '5 ** 2 + 5 ** 2',
          'Zahlen x und 10 − x: S(x) = x² + (10 − x)² = 2x² − 20x + 100 = 2(x − 5)² + 50. Kleinster Wert 50 bei x = 5.',
          'Schreib die Summe der Quadrate mit einer Unbekannten.'))

# schnittpunkte
ST.stufenleiter('schnittpunkte', 'Parabel und Gerade gleichsetzen, wenn beide einfach sind.',
                'Gleichung umformen und lösen, Zahl der gemeinsamen Punkte, Geraden durch den Scheitel, Ball trifft Rampe.',
                'Tangenten-Bedingungen, Mittelpunkt einer Sehne, Ursprungsgerade als Tangente, Sachmodelle, Fehler beim Umformen.')
ST.typ('schnittpunkte', 'An welchen Stellen', 'direkt')
ST.typ('schnittpunkte', '/^(Welche Gleichung löst du|Gleichsetzen von Parabel)/', 'erkennen')
ST.typ('schnittpunkte', '/^(Berechne die Schnittpunkte der Parabel |Wie viele gemeinsame|Berechne die Schnittpunkte der Parabeln y = x² − 4)/', 'mehrschritt')
ST.typ('schnittpunkte', '/^(Die Gerade g:|Eine Ursprungsgerade|Ein Wasserstrahl)/', 'transfer')
ST.typ('schnittpunkte', 'Für welche', 'parameter')
ST.typ('schnittpunkte', '/^(Die Gerade y = x \\+ 1|Berechne die Schnittpunkte der Parabeln)/', 'verknuepfen')
ST.typ('schnittpunkte', 'Jemand setzt', 'fehler')
ST.neu('schnittpunkte', 'einkleidung', Z('Ein Ball fliegt auf der Bahn y = −0,1x² + x + 1, eine Rampe verläuft auf y = 0,2x + 1 (in m). Bei welchem x > 0 trifft der Ball die Rampe?', 8, '0.8 / 0.1',
       'Gleichsetzen: −0,1x² + x + 1 = 0,2x + 1 ⇒ −0,1x² + 0,8x = 0 ⇒ x(−0,1x + 0,8) = 0. x = 0 ist der Abwurf, x = 8 m der Treffpunkt.', 'Gleichsetzen und x ausklammern.', einheit='m'))
ST.neu('schnittpunkte', 'umkehr', Z('Die Gerade y = 2x + t geht durch den Scheitel der Parabel y = x² − 4x + 7. Bestimme t.', -1, '3 - 4',
       'y = (x − 2)² + 3, Scheitel (2 | 3). Einsetzen: 3 = 2 · 2 + t, also t = −1.', 'Bestimme zuerst den Scheitel.'))
ST.knobel('schnittpunkte', Z('Für wie viele ganze Zahlen m hat die Gerade y = mx keinen gemeinsamen Punkt mit der Parabel y = x² + 4?', 7, '2 * 3 + 1',
          'Gleichsetzen: x² − mx + 4 = 0. Keine Lösung, wenn D = m² − 16 < 0, also −4 < m < 4. Ganze Zahlen: −3, −2, …, 3, das sind 7.',
          'Wann hat eine quadratische Gleichung keine Lösung?'))
ST.knobel('schnittpunkte', Z('Die Gerade y = 4 schneidet die Parabel y = x² in A und B, die Gerade y = 16 schneidet sie in C und D. Wie groß ist das Trapez mit den Ecken A, B, D, C?', 72, '(4 + 8) * 12 // 2',
          'y = 4: x = ±2, also AB = 4. y = 16: x = ±4, also CD = 8. Abstand der Parallelen: 16 − 4 = 12. Fläche (4 + 8) : 2 · 12 = 72.',
          'Bestimme die Schnittpunkte und zeichne das Trapez.'))

if __name__ == '__main__':
    stufen('funktionen.quadratisch', ST)


# ---- BEREINIGEN (Einundzwanzigste Runde) ----
if __name__ == '__main__':
    from _bereinigen import bereinigen_datei
    bereinigen_datei('funktionen.quadratisch')
# ---- BEREINIGEN ENDE ----
