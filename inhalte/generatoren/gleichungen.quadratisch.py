#!/usr/bin/env python3
"""Thema gleichungen.quadratisch – Quadratische Gleichungen (allgemein), Klasse 9."""
import sys
from math import isqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(904)
L2 = 'x₁ = □; x₂ = □'
H2 = 'kleinere Lösung zuerst'


def nz(n):
    return R.choice([i for i in range(-n, n + 1) if i != 0])


def wurzel_c(a, b, c):
    """Rechenausdrücke der beiden Lösungen (kleinere zuerst) über die Lösungsformel."""
    D = b * b - 4 * a * c
    s = isqrt(D)
    assert s * s == D
    x1, x2 = Fr(-b - s, 2 * a), Fr(-b + s, 2 * a)
    e1, e2 = f'(-({b}) - {s}) / (2 * {a})', f'(-({b}) + {s}) / (2 * {a})'
    return (x1, x2, e1, e2) if x1 <= x2 else (x2, x1, e2, e1)


ETAPPEN = [
    {'lernziel': 'reinquadratisch', 'titel': 'Gleichungen ohne x-Glied lösen',
     'regel': 'Bei ax² + c = 0 stellst du nach ⟦x²⟧ um. Ist x² = d mit d > 0, gibt es ⟦zwei Lösungen ±√d⟧; bei d = 0 eine, bei d < 0 ⟦keine⟧.',
     'schritte': ['3x² − 75 = 0 | + 75, dann : 3 ergibt x² = 25.', 'x₁ = ⟦−5⟧ und x₂ = ⟦5⟧.'],
     'probe': '3 · (−5)² − 75 = 75 − 75 = 0 ✓',
     'fehler': 'x² = 25 ⇒ x = 5 ist unvollständig: Auch (−5)² = 25. Die Lösungsmenge ist ⟦{−5; 5}⟧.'},
    {'lernziel': 'ausklammern', 'titel': 'Gleichungen ohne Zahlglied lösen',
     'regel': 'Bei ax² + bx = 0 ⟦klammerst du x aus⟧: x(ax + b) = 0. Ein Produkt ist null, wenn ein ⟦Faktor null⟧ ist (Satz vom Nullprodukt).',
     'schritte': ['2x² − 12x = 0 ⇔ x(2x − 12) = 0.', 'x = 0 oder 2x − 12 = 0, also ⟦x₁ = 0, x₂ = 6⟧.'],
     'probe': '2 · 6² − 12 · 6 = 72 − 72 = 0 ✓',
     'fehler': '2x² = 12x | : x ergibt nur x = 6 – dabei geht die Lösung ⟦x = 0⟧ verloren. Nie durch x teilen, sondern ausklammern.'},
    {'lernziel': 'faktorisieren', 'titel': 'Faktorisieren und Nullprodukt',
     'regel': 'Steht die Gleichung als ⟦Produkt = 0⟧, liest du die Lösungen ab: (x − p)(x − q) = 0 ⇔ ⟦x = p oder x = q⟧. Binomische Formeln helfen beim Faktorisieren.',
     'schritte': ['x² − 8x + 16 = 0: 2. binomische Formel, also (x − 4)² = 0.', 'Nur x − 4 = 0, also eine Lösung: ⟦x = 4⟧.', 'Ohne binomische Formel, z. B. x² + 8x − 9 = 0: Suche zwei Zahlen mit ⟦Produkt −9⟧ und ⟦Summe 8⟧. Das sind 9 und −1. Also (x + 9)(x − 1) = 0 und ⟦x = −9 oder x = 1⟧.'],
     'probe': '(x + 9)(x − 1) = x² − x + 9x − 9 = x² + 8x − 9 ✓',
     'fehler': '(x + 3)(x − 2) = 0 ⇒ x = 3 oder x = −2 ist falsch: Die ⟦Vorzeichen drehen sich um⟧. Richtig: x = −3 oder x = 2.'},
    {'lernziel': 'ergaenzung', 'titel': 'Quadratische Ergänzung',
     'regel': 'Bei x² + bx + c = 0 ergänzt du ⟦(b/2)²⟧ auf beiden Seiten, sodass links ⟦(x + b/2)²⟧ steht. Warum genau (b/2)²? Leg x² + 6x als Fläche: ein Quadrat x mal x und zwei Streifen 3 mal x. Zum großen Quadrat (x + 3)² fehlt nur die ⟦Ecke 3 · 3 = 9⟧.',
     'bild': {'typ': 'figur', 'punkte': {'_a': [0, 0], '_b': [5, 0], '_c': [8, 0], '_d': [8, 5], '_e': [8, 8], '_f': [5, 8], '_g': [0, 8], '_h': [0, 5], '_m': [5, 5]}, 'flaeche': ['_m', '_d', '_e', '_f'], 'linien': [['_a', '_b', 'x'], ['_b', '_c', '3'], ['_c', '_d'], ['_d', '_e'], ['_e', '_f'], ['_f', '_g'], ['_g', '_h', '3'], ['_h', '_a', 'x'], ['_b', '_m'], ['_m', '_f'], ['_h', '_m'], ['_m', '_d']]},
     'schritte': ['x² + 6x − 7 = 0 ⇔ x² + 6x + 9 = 7 + 9.', '(x + 3)² = 16 ⇒ x + 3 = ±4 ⇒ ⟦x₁ = −7, x₂ = 1⟧.'],
     'probe': '1² + 6 · 1 − 7 = 0 ✓',
     'fehler': 'x² + 6x − 7 = 0 ⇒ (x + 6)² = 7 ist falsch: In die Klammer gehört die ⟦Hälfte⟧ von 6, und (b/2)² = 9 muss auf ⟦beiden Seiten⟧ ergänzt werden.'},
    {'lernziel': 'loesungsformel', 'titel': 'Die Lösungsformel anwenden',
     'regel': 'Für ax² + bx + c = 0 (a ≠ 0) gilt ⟦x₁,₂ = (−b ± √(b² − 4ac)) / (2a)⟧. Den Term ⟦D = b² − 4ac⟧ unter der Wurzel heißt Diskriminante.',
     'schritte': ['2x² − 5x − 3 = 0: a = 2, b = −5, c = −3. D = 25 + 24 = 49.', 'x₁,₂ = (5 ± 7) / 4, also ⟦x₁ = −0,5; x₂ = 3⟧.'],
     'probe': '2 · 3² − 5 · 3 − 3 = 18 − 15 − 3 = 0 ✓',
     'fehler': 'Bei b = −5 ist −b = −5 falsch: Minus mal Minus ergibt ⟦−b = 5⟧. Auch b² = (−5)² = 25, nicht −25.'},
    {'lernziel': 'diskriminante', 'titel': 'Wie viele Lösungen gibt es?',
     'regel': 'Die Diskriminante entscheidet: ⟦D > 0⟧ zwei Lösungen, ⟦D = 0⟧ genau eine, ⟦D < 0⟧ keine Lösung.',
     'schritte': ['x² − 4x + 7 = 0: D = (−4)² − 4 · 1 · 7 = 16 − 28 = −12.', 'D < 0, also ⟦keine Lösung⟧.'],
     'probe': 'Quadratische Ergänzung: (x − 2)² + 3 = 0 – links steht immer mindestens 3 ✓',
     'bild': {'typ': 'koordinaten', 'x': [-1, 5], 'y': [-1, 8], 'graphen': [{'art': 'poly', 'k': [7, -4, 1], 'name': 'y = x² − 4x + 7'}], 'punkte': [{'x': 2, 'y': 3, 'name': 'S(2 | 3)'}]},
     'fehler': '„D = −12, also zwei Lösungen, weil man ± rechnet“ ist falsch: Aus einer ⟦negativen⟧ Zahl gibt es keine Quadratwurzel.'},
    {'lernziel': 'sachaufgabe', 'titel': 'Sachaufgaben lösen',
     'regel': 'Variable festlegen, ⟦Gleichung aufstellen⟧, lösen und die Lösungen am ⟦Sachzusammenhang prüfen⟧ (z. B. keine negativen Längen).',
     'schritte': ['Ein Rechteck ist 4 cm länger als breit und hat 45 cm² Fläche: x(x + 4) = 45 ⇔ x² + 4x − 45 = 0.',
                  'Lösungen x = −9 und x = 5; nur ⟦x = 5⟧ ist eine Länge. Das Rechteck ist 5 cm breit und 9 cm lang.'],
     'probe': '5 cm · 9 cm = 45 cm² ✓',
     'fehler': 'Die Lösung x = −9 als Breite anzugeben ist falsch: Längen sind ⟦positiv⟧. Diese Lösung passt nicht zum Sachzusammenhang.'},
]

# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'reinquadratisch': {
  'einstieg': 'Drei gleich große quadratische Fliesen bedecken zusammen 75 dm². Wie lang ist die Seite einer Fliese? Eine Fliese hat 75 : 3 = 25 dm², also 5 dm Seite. Rechnerisch steckt dahinter eine Gleichung, in der die gesuchte Zahl nur mit sich selbst malgenommen vorkommt – eine ⟦quadratische Gleichung⟧.',
  'woerter': [['x', 'die gesuchte Zahl, hier die Fliesenseite in dm'],
              ['x²', 'x · x'],
              ['quadratische Gleichung', 'eine Gleichung, in der x² vorkommt (aber keine höhere Potenz)'],
              ['x-Glied', 'ein Teil mit x ohne Hochzahl, z. B. 4x – hier gibt es keins'],
              ['x₁, x₂', 'die erste und die zweite Lösung'],
              ['Lösungsmenge {−5; 5}', 'alle Lösungen in einer Mengenklammer']],
  'schritte': ['Die Gleichung heißt 3x² − 75 = 0. Ziel: x² allein auf eine Seite bringen.',
               'Auf beiden Seiten 75 addieren: 3x² = 75.',
               'Beide Seiten durch 3 teilen: x² = 25.',
               'Welche Zahlen ergeben mal sich selbst 25? ⟦x₁ = −5 und x₂ = 5⟧. Für die Fliese passt nur die positive Lösung: 5 dm.'],
  'regel': 'So löst du ax² + c = 0: Bring ⟦x² allein⟧ auf eine Seite, sodass x² = d dasteht. Ist d > 0, gibt es ⟦zwei Lösungen⟧ √d und −√d; ist d = 0, nur x = 0; ist d < 0, gibt es ⟦keine⟧ Lösung.',
  'fehler': 'x² = 25 ⇒ x = 5 ist unvollständig: Auch (−5) · (−5) = 25. Die Lösungsmenge ist ⟦{−5; 5}⟧ – erst der Sachzusammenhang (eine Seite ist nie negativ) streicht die −5.'},
 'ausklammern': {
  'einstieg': 'Ein Zahlenrätsel: „Nimmst du meine Zahl mal sich selbst und das Ergebnis mal 2, kommt dasselbe heraus wie zwölfmal meine Zahl.“ Probieren zeigt: 6 passt, denn 2 · 36 = 72 und 12 · 6 = 72. Aber auch 0 passt! Damit keine Lösung verloren geht, zieht man das x vor eine Klammer – das heißt ⟦ausklammern⟧.',
  'woerter': [['ausklammern', 'einen gemeinsamen Teil vor eine Klammer ziehen: 2x² − 12x = x · (2x − 12)'],
              ['Faktor', 'ein Teil, der malgenommen wird'],
              ['Zahlglied', 'eine Zahl ohne x, z. B. −7 – hier gibt es keins'],
              ['Satz vom Nullprodukt', 'ein Produkt ist 0, wenn mindestens ein Faktor 0 ist']],
  'schritte': ['Die Gleichung heißt 2x² − 12x = 0. In beiden Teilen steckt ein x.',
               'x ausklammern: x · (2x − 12) = 0. Das ist ein Produkt, das 0 ergeben soll.',
               'Ein Produkt ist 0, wenn ein Faktor 0 ist: Entweder ist x = 0 oder 2x − 12 = 0.',
               'Aus 2x − 12 = 0 folgt 2x = 12, also x = 6. Die Lösungen sind ⟦x₁ = 0 und x₂ = 6⟧.'],
  'regel': 'So löst du ax² + bx = 0: ⟦x ausklammern⟧, sodass x · (ax + b) = 0 dasteht. Dann jeden Faktor null setzen (⟦Satz vom Nullprodukt⟧). Eine Lösung ist immer ⟦x = 0⟧.',
  'fehler': '2x² = 12x | : x ergibt nur x = 6 – dabei geht die Lösung ⟦x = 0⟧ verloren, denn durch 0 darf man nicht teilen. Im Rätsel wäre die 0 vergessen. Nicht durch x teilen, sondern ausklammern.'},
 'faktorisieren': {
  'einstieg': 'Ist ein Produkt null, muss einer der Faktoren null sein. Wie beim Einkauf „Preis mal Menge“: Hast du 0 € bezahlt, war der Preis 0 € oder die Menge 0. Steht eine Gleichung als Produkt da, kann man die Lösungen deshalb direkt ablesen. Eine Summe in ein Produkt umzuschreiben heißt ⟦faktorisieren⟧.',
  'woerter': [['faktorisieren', 'eine Summe als Produkt schreiben, z. B. x² + 8x − 9 = (x + 9)(x − 1)'],
              ['(x + 9)(x − 1)', '(x + 9) mal (x − 1); der Malpunkt wird weggelassen'],
              ['(x − 4)²', '(x − 4) · (x − 4)'],
              ['binomische Formel', 'eine Merkformel, z. B. x² − 8x + 16 = (x − 4)²']],
  'schritte': ['Die Gleichung heißt x² + 8x − 9 = 0. Gesucht ist die Form (x + p)(x + q) = 0.',
               'Suche zwei Zahlen, deren Produkt −9 und deren Summe 8 ist: 9 und −1, denn 9 · (−1) = −9 und 9 + (−1) = 8.',
               'Also ist die Gleichung dasselbe wie (x + 9)(x − 1) = 0.',
               'Jeder Faktor kann null sein: x + 9 = 0 ergibt x = −9, x − 1 = 0 ergibt x = 1. Lösungen: ⟦x = −9 oder x = 1⟧.',
               'Mit binomischer Formel: x² − 8x + 16 = (x − 4)² = 0 hat nur die Lösung ⟦x = 4⟧.'],
  'regel': 'So liest du Lösungen ab: Steht da ⟦Produkt = 0⟧, setzt du jeden Faktor null: (x − p)(x − q) = 0 ⇔ ⟦x = p oder x = q⟧. Zum Faktorisieren suchst du zwei Zahlen mit passendem Produkt und passender Summe oder nutzt eine binomische Formel.',
  'fehler': '(x + 3)(x − 2) = 0 ⇒ x = 3 oder x = −2 ist falsch: Die ⟦Vorzeichen drehen sich um⟧. Probe: Mit x = 3 wird x + 3 = 6, nicht 0. Richtig: x = −3 oder x = 2.'},
 'ergaenzung': {
  'einstieg': 'Ein Stück Rasen besteht aus einem Quadrat und zwei Streifen, die an zwei Seiten anliegen. Hat das Quadrat die Seite x und ist jeder Streifen 3 breit, ist die Fläche x² + 6x. Zum großen Quadrat fehlt nur die Ecke 3 mal 3 = 9. Legt man sie dazu, entsteht ein volles Quadrat mit Seite x + 3. Das heißt ⟦quadratische Ergänzung⟧.',
  'woerter': [['ergänzen', 'etwas dazulegen, hier die fehlende Ecke'],
              ['(x + 3)²', 'ein Quadrat mit Seite x + 3; ausgerechnet x² + 6x + 9'],
              ['b/2', 'die Hälfte der Zahl vor x'],
              ['±4', '„plus oder minus 4“: 4 und −4']],
  'schritte': ['Die Gleichung heißt x² + 6x − 7 = 0. Zuerst die −7 nach rechts bringen: x² + 6x = 7.',
               'Die Hälfte von 6 ist 3, die fehlende Ecke ist 3 · 3 = 9. Auf beiden Seiten 9 dazuzählen: x² + 6x + 9 = 16.',
               'Links steht jetzt das volle Quadrat: (x + 3)² = 16.',
               'Wurzel ziehen, an beide Vorzeichen denken: x + 3 = 4 oder x + 3 = −4. Also ⟦x₁ = −7, x₂ = 1⟧.'],
  'regel': 'So ergänzt du bei x² + bx + c = 0: c nach rechts bringen, dann auf ⟦beiden Seiten (b/2)²⟧ dazuzählen. Links steht dann ⟦(x + b/2)²⟧. Danach die Wurzel ziehen und an ⟦beide Vorzeichen⟧ denken.',
  'fehler': 'x² + 6x − 7 = 0 ⇒ (x + 6)² = 7 ist falsch: In die Klammer gehört die ⟦Hälfte⟧ von 6, und die Ecke 9 muss auf ⟦beiden Seiten⟧ dazukommen – sonst ändert sich die Gleichung.'},
 'loesungsformel': {
  'einstieg': 'Faktorisieren und Ergänzen klappen nicht immer bequem. Für jede quadratische Gleichung gibt es eine fertige Formel, in die man nur drei Zahlen einsetzt – wie ein Rezept, das immer gelingt. Sie heißt ⟦Lösungsformel⟧, oft auch „Mitternachtsformel“.',
  'woerter': [['a, b, c', 'die Zahlen in ax² + bx + c = 0: vor x², vor x und ohne x'],
              ['a ≠ 0', 'a darf nicht 0 sein, sonst gäbe es kein x²'],
              ['±', 'einmal plus und einmal minus rechnen'],
              ['x₁,₂', 'beide Lösungen auf einmal'],
              ['Diskriminante D', 'die Zahl unter der Wurzel: D = b² − 4ac']],
  'schritte': ['Die Gleichung heißt 2x² − 5x − 3 = 0. Ablesen: a = 2, b = −5, c = −3.',
               'Unter der Wurzel: D = b² − 4ac = (−5)² − 4 · 2 · (−3) = 25 + 24 = 49, und √49 = 7.',
               'Einsetzen: x₁,₂ = (5 ± 7) / 4, denn −b = 5 und 2a = 4.',
               'Einmal minus, einmal plus: (5 − 7) : 4 = −0,5 und (5 + 7) : 4 = 3. Also ⟦x₁ = −0,5; x₂ = 3⟧.'],
  'regel': 'So wendest du die ⟦Lösungsformel⟧ an: Gleichung in die Form ax² + bx + c = 0 bringen, a, b und c mit Vorzeichen ablesen und einsetzen: ⟦x₁,₂ = (−b ± √(b² − 4ac)) / (2a)⟧. Der Teil unter der Wurzel heißt ⟦Diskriminante D⟧.',
  'fehler': 'Bei b = −5 ist −b = −5 falsch: Ein Minus vor einer negativen Zahl macht sie positiv, also ⟦−b = 5⟧. Auch b² = (−5)² = 25, nicht −25.'},
 'diskriminante': {
  'einstieg': 'Bevor man lange rechnet, lohnt ein Blick unter die Wurzel der Lösungsformel. Ist die Zahl dort negativ, kann man keine Wurzel ziehen – es gibt keine Lösung. Ist sie 0, liefern Plus und Minus dasselbe. Diese Zahl verrät also, wie viele Lösungen es gibt; sie heißt ⟦Diskriminante⟧ („die Unterscheidende“).',
  'woerter': [['D = b² − 4ac', 'die Diskriminante, berechnet aus a, b und c'],
              ['D > 0 / D < 0', 'D ist größer als 0 / kleiner als 0'],
              ['Parabel', 'die Kurve zu y = ax² + bx + c; die Lösungen sind die Stellen, an denen sie die x-Achse trifft']],
  'schritte': ['Die Gleichung heißt x² − 4x + 7 = 0. Ablesen: a = 1, b = −4, c = 7.',
               'D = (−4)² − 4 · 1 · 7 = 16 − 28 = −12.',
               'D ist negativ. Aus −12 gibt es keine Quadratwurzel.',
               'Also hat die Gleichung ⟦keine Lösung⟧. Im Bild liegt die Parabel ganz oberhalb der x-Achse.'],
  'regel': 'So entscheidest du mit ⟦D = b² − 4ac⟧: ⟦D > 0⟧ zwei Lösungen, ⟦D = 0⟧ genau eine, ⟦D < 0⟧ keine Lösung.',
  'fehler': '„D = −12, also zwei Lösungen, weil man ± rechnet“ ist falsch: Das ± hilft nichts, wenn es die Wurzel gar nicht gibt. Aus einer ⟦negativen⟧ Zahl gibt es keine Quadratwurzel.'},
 'sachaufgabe': {
  'einstieg': 'Für ein Gemüsebeet hast du 45 m² Platz. Es soll 4 m länger als breit sein. Wie breit wird es? Probieren dauert lange; schneller geht es mit einer Gleichung. Ein solches Problem aus dem Alltag heißt ⟦Sachaufgabe⟧.',
  'woerter': [['Variable festlegen', 'sagen, wofür x steht – hier die Breite in m'],
              ['x + 4', 'die Länge: 4 m mehr als die Breite'],
              ['Sachzusammenhang', 'die Situation, zu der die Lösung passen muss']],
  'schritte': ['Variable festlegen: x ist die Breite in m. Die Länge ist dann x + 4.',
               'Gleichung aufstellen: Breite mal Länge ist die Fläche, also x(x + 4) = 45. Ausmultipliziert und umgestellt: x² + 4x − 45 = 0.',
               'Lösen, zum Beispiel mit der Lösungsformel: x = −9 oder x = 5.',
               'Am Sachzusammenhang prüfen: Eine Breite ist nie negativ. Also ⟦x = 5⟧: Das Beet ist 5 m breit und 9 m lang.'],
  'probe': '5 m · 9 m = 45 m² ✓',
  'regel': 'So löst du eine Sachaufgabe: ⟦Variable festlegen⟧, ⟦Gleichung aufstellen⟧, lösen und jede Lösung am ⟦Sachzusammenhang prüfen⟧ (z. B. keine negativen Längen).',
  'fehler': 'Die Lösung x = −9 als Breite anzugeben ist falsch: Ein Beet kann nicht −9 m breit sein. Längen sind ⟦positiv⟧; diese Lösung passt nicht zum Sachzusammenhang.'},
}
klar(ETAPPEN, KLAR)
# ---- KLAR ENDE ----
# ---- UMBAU (neues Muster, Runde 8, Vorgabe 16.11.) ----
_FL_P = {'_a0': [0, 0], '_a1': [5, 0], '_a2': [10, 0], '_a3': [15, 0], '_b0': [0, 5], '_b1': [5, 5], '_b2': [10, 5], '_b3': [15, 5]}
def _fliesen(unten, oben='zusammen 75 dm²'):
    return [['_a0', '_a1', unten], ['_a1', '_a2', ''], ['_a2', '_a3', ''], ['_b0', '_b3', oben],
            ['_a0', '_b0', ''], ['_a1', '_b1', ''], ['_a2', '_b2', ''], ['_a3', '_b3', '']]
_R = {'_O': [0, 0], '_P': [4, 0], '_Q': [4, 4], '_R': [0, 4], '_S': [7, 0], '_T': [7, 4], '_U': [0, 7], '_V': [4, 7], '_W': [7, 7]}
_REC = {'_A': [0, 0], '_B': [9, 0], '_C': [9, 5], '_D': [0, 5]}
UMBAU = {
 'reinquadratisch': {
  'einstieg': 'Drei gleich große quadratische Fliesen bedecken zusammen 75 dm². Wie lang ist eine Seite? Das führt auf eine ⟦quadratische Gleichung⟧: 3x² = 75.',
  'woerter': [['quadratische Gleichung', 'eine Gleichung mit x², aber ohne höhere Hochzahl'],
              ['x²', 'x · x, hier die Fläche einer Fliese'],
              ['Lösungsmenge', 'alle Lösungen in einer Mengenklammer, z. B. {−5; 5}']],
  'bild': {'typ': 'figur', 'punkte': _FL_P, 'flaeche': ['_a0', '_a3', '_b3', '_b0'], 'linien': _fliesen('Seite = ?')},
  'schritte': [{'text': '3x² − 75 = 0. Auf beiden Seiten 75 addieren: 3x² = 75.'},
               {'text': 'Durch 3 teilen: x² = 25. Eine Fliese hat 25 dm².',
                'bild': {'linien': _fliesen('Seite = ?', 'je 25 dm²')}},
               {'text': 'x · x = 25 gilt für 5 und für −5. Lösungsmenge: ⟦{−5; 5}⟧.'},
               {'text': 'Eine Seite ist nie negativ. Die Fliese hat ⟦5 dm⟧ Seite.',
                'bild': {'linien': _fliesen('Seite = 5 dm', 'je 25 dm²')}}],
  'fehler': 'x² = 25 ⇒ x = 5 ist unvollständig: Auch (−5) · (−5) = 25. Erst die Fliese schließt die −5 aus.',
  'regel': 'Bring ⟦x² allein⟧ auf eine Seite, dann ziehst du die Wurzel. Bei x² = d > 0 gibt es zwei Lösungen: √d und −√d.'},
 'ausklammern': {
  'einstieg': 'Rätsel: Meine Zahl mal sich selbst, das Doppelte davon, ist zwölfmal meine Zahl. Die 6 passt, aber auch die 0. Damit keine Lösung verloren geht, hilft ⟦Ausklammern⟧.',
  'woerter': [['Ausklammern', 'einen gemeinsamen Teil vor eine Klammer ziehen: 2x² − 12x = x · (2x − 12)'],
              ['Faktor', 'ein Teil, der malgenommen wird'],
              ['Satz vom Nullprodukt', 'ein Produkt ist 0, wenn mindestens ein Faktor 0 ist']],
  'bild': {'typ': 'koordinaten', 'x': [-2, 8], 'y': [-20, 10], 'schritt_y': 5,
           'graphen': [{'art': 'poly', 'k': [0, -12, 2], 'name': 'y = 2x² − 12x'}]},
  'schritte': [{'text': 'Die Gleichung heißt 2x² − 12x = 0. Beide Teile enthalten x.'},
               {'text': 'Ausklammern: x · (2x − 12) = 0. Das ist ein Produkt aus zwei Faktoren.'},
               {'text': 'Satz vom Nullprodukt: x = 0 oder 2x − 12 = 0.'},
               {'text': '2x = 12 ergibt x = 6. Also ⟦x = 0 oder x = 6⟧.',
                'bild': {'punkte': [{'x': 0, 'y': 0, 'name': '0'}, {'x': 6, 'y': 0, 'name': '6'}]}}],
  'fehler': 'Durch x teilen ist falsch: 2x = 12 liefert nur die 6. Die Lösung 0 geht verloren – im Rätsel passt sie aber.',
  'fehler_bild': {'punkte': [{'x': 6, 'y': 0, 'name': '6'}, {'x': 0, 'y': 0, 'name': '0 vergessen', 'offen': True}]},
  'regel': '⟦x ausklammern⟧, dann jeden Faktor null setzen. Eine Lösung ist dann immer x = 0.'},
 'faktorisieren': {
  'einstieg': 'Hast du 0 € bezahlt, war der Preis oder die Menge 0. Ein Produkt ist nur 0, wenn ein Faktor 0 ist. Darum lohnt sich ⟦Faktorisieren⟧.',
  'woerter': [['Faktorisieren', 'eine Summe als Produkt schreiben'],
              ['(x + 9)(x − 1)', '(x + 9) mal (x − 1); der Malpunkt fehlt']],
  'bild': {'typ': 'koordinaten', 'x': [-11, 3], 'y': [-30, 10], 'schritt_y': 10, 'schritt_x': 2,
           'graphen': [{'art': 'poly', 'k': [-9, 8, 1], 'name': 'y = x² + 8x − 9'}]},
  'schritte': [{'text': 'Gesucht: zwei Zahlen mit Produkt −9 und Summe 8.'},
               {'text': '9 und −1 passen: 9 · (−1) = −9 und 9 + (−1) = 8.'},
               {'text': 'Faktorisieren ergibt: (x + 9)(x − 1) = 0.'},
               {'text': 'Ein Faktor muss 0 sein: ⟦x = −9 oder x = 1⟧.',
                'bild': {'punkte': [{'x': -9, 'y': 0, 'name': '−9'}, {'x': 1, 'y': 0, 'name': '1'}]}}],
  'fehler': '(x + 3)(x − 2) = 0 hat nicht die Lösungen 3 und −2. Die Vorzeichen drehen sich um: x = −3 oder x = 2.',
  'regel': 'Steht da Produkt = 0, setzt du ⟦jeden Faktor null⟧. (x − p)(x − q) = 0 heißt x = p oder x = q.'},
 'ergaenzung': {
  'einstieg': 'Ein Rasen besteht aus einem Quadrat mit Seite x und zwei Streifen der Breite 3. Zum vollen Quadrat fehlt nur die Ecke 3 · 3 = 9. Das heißt ⟦quadratische Ergänzung⟧.',
  'woerter': [['quadratische Ergänzung', 'die fehlende Ecke dazulegen, damit ein volles Quadrat entsteht'],
              ['(x + 3)²', 'ein Quadrat mit Seite x + 3'],
              ['±4', 'plus 4 oder minus 4']],
  'bild': {'typ': 'figur', 'punkte': _R, 'flaeche': ['_O', '_S', '_T', '_Q', '_V', '_U'],
           'linien': [['_O', '_P', 'x'], ['_P', '_S', '3'], ['_S', '_T', ''], ['_T', '_Q', ''], ['_Q', '_V', ''], ['_V', '_U', ''], ['_U', '_O', ''],
                      ['_P', '_Q', '', 'gestrichelt'], ['_R', '_Q', '', 'gestrichelt'], ['_T', '_W', 'Ecke 9', 'gestrichelt'], ['_W', '_V', '', 'gestrichelt']]},
  'schritte': [{'text': 'Aus x² + 6x − 7 = 0 wird x² + 6x = 7.'},
               {'text': 'Die Ecke 9 auf beiden Seiten dazu: x² + 6x + 9 = 16.',
                'bild': {'flaeche': ['_O', '_S', '_W', '_U'],
                         'linien': [['_O', '_P', 'x'], ['_P', '_S', '3'], ['_S', '_W', 'x + 3'], ['_W', '_U', ''], ['_U', '_O', ''],
                                    ['_P', '_Q', '', 'gestrichelt'], ['_R', '_Q', '', 'gestrichelt'], ['_T', '_Q', '', 'gestrichelt'], ['_V', '_Q', '', 'gestrichelt']]}},
               {'text': 'Links steht ein volles Quadrat: (x + 3)² = 16.'},
               {'text': 'Wurzel ziehen: x + 3 = ±4. Also ⟦x₁ = 1, x₂ = −7⟧.'}],
  'fehler': '(x + 6)² = 7 ist falsch. In die Klammer gehört die Hälfte von 6. Die Ecke 9 muss auf beide Seiten.',
  'regel': 'Ergänze auf beiden Seiten ⟦(b/2)²⟧. Dann steht links (x + b/2)². Wurzel ziehen und an beide Vorzeichen denken.'},
 'loesungsformel': {
  'einstieg': 'Faktorisieren und Ergänzen klappen nicht immer bequem. Die ⟦Lösungsformel⟧ ist wie ein Rezept: drei Zahlen einsetzen, fertig. Man nennt sie auch Mitternachtsformel.',
  'woerter': [['a, b und c', 'die Zahlen in ax² + bx + c = 0: vor x², vor x und ohne x'],
              ['Diskriminante D', 'die Zahl unter der Wurzel: D = b² − 4ac'],
              ['x₁,₂', 'beide Lösungen auf einmal']],
  'bild': {'typ': 'tabelle', 'kopf': ['a', 'b', 'c', 'D', 'x₁', 'x₂'], 'zeilen': [['?', '?', '?', '?', '?', '?']]},
  'schritte': [{'text': 'Die Gleichung heißt 2x² − 5x − 3 = 0.'},
               {'text': 'Abgelesen: a, b und c sind 2, −5 und −3.',
                'bild': {'zeilen': [['2', '−5', '−3', '?', '?', '?']]}},
               {'text': 'Diskriminante D = (−5)² − 4 · 2 · (−3) = 49.',
                'bild': {'zeilen': [['2', '−5', '−3', '49', '?', '?']]}},
               {'text': 'Zum Einsetzen: −b = 5, 2a = 4 und √49 = 7.'},
               {'text': 'x₁,₂ = (5 ± 7) : 4, also ⟦x₁ = −0,5⟧ und ⟦x₂ = 3⟧.',
                'bild': {'zeilen': [['2', '−5', '−3', '49', '−0,5', '3']]}}],
  'fehler': 'Bei b = −5 ist −b nicht −5. Ein Minus vor einer negativen Zahl macht sie positiv: −b = 5.',
  'regel': 'Setze a, b und c in die ⟦Lösungsformel⟧ ein. x₁,₂ = (−b ± √(b² − 4ac)) : (2a).'},
 'diskriminante': {
  'einstieg': 'Ein Blick unter die Wurzel der Lösungsformel spart Arbeit. Ist die Zahl dort negativ, gibt es keine Lösung. Diese Zahl heißt ⟦Diskriminante⟧.',
  'woerter': [['Diskriminante', 'D = b² − 4ac, die Zahl unter der Wurzel'],
              ['Parabel', 'die Kurve zu y = ax² + bx + c; Lösungen sind ihre Treffer mit der x-Achse']],
  'bild': {'typ': 'koordinaten', 'x': [-1, 5], 'y': [-2, 10], 'graphen': [{'art': 'poly', 'k': [7, -4, 1], 'name': 'y = x² − 4x + 7'}]},
  'schritte': [{'text': 'Die Gleichung heißt x² − 4x + 7 = 0.'},
               {'text': 'D = (−4)² − 4 · 1 · 7 = 16 − 28 = −12.'},
               {'text': 'Aus −12 gibt es keine Wurzel. Die Diskriminante sagt: ⟦keine Lösung⟧.'},
               {'text': 'Im Bild bleibt die Parabel ganz über der x-Achse.',
                'bild': {'punkte': [{'x': 2, 'y': 3, 'name': 'tiefster Punkt'}]}}],
  'fehler': 'D = −12 heißt nicht zwei Lösungen wegen ±. Das ± hilft nichts, wenn es die Wurzel gar nicht gibt.',
  'regel': 'D = b² − 4ac entscheidet über die Anzahl. ⟦D > 0⟧ zwei Lösungen, D = 0 eine, D < 0 keine.'},
 'sachaufgabe': {
  'einstieg': 'Ein Gemüsebeet soll 45 m² groß sein und 4 m länger als breit. Wie breit wird es? So eine Alltagsfrage heißt ⟦Sachaufgabe⟧.',
  'woerter': [['Sachaufgabe', 'eine Rechenaufgabe aus dem Alltag'],
              ['Variable', 'ein Buchstabe für die gesuchte Zahl, hier x'],
              ['Sachzusammenhang', 'die Situation, zu der die Lösung passen muss']],
  'bild': {'typ': 'figur', 'punkte': _REC, 'flaeche': ['_A', '_B', '_C', '_D'],
           'linien': [['_A', '_B', 'x + 4'], ['_B', '_C', 'x'], ['_C', '_D', '45 m²'], ['_D', '_A', '']], 'rechter_winkel': [['_A', '_B', '_D']]},
  'schritte': [{'text': 'Variable festlegen: x ist die Breite, x + 4 die Länge.'},
               {'text': 'Fläche: x(x + 4) = 45, also x² + 4x − 45 = 0.'},
               {'text': 'Mit der Lösungsformel: x = 5 oder x = −9.'},
               {'text': 'Sachzusammenhang: Eine Breite ist nie negativ. Also ⟦5 m breit, 9 m lang⟧.',
                'bild': {'linien': [['_A', '_B', '9 m'], ['_B', '_C', '5 m'], ['_C', '_D', '45 m²'], ['_D', '_A', '']]}}],
  'fehler': 'x = −9 als Breite ist falsch. Ein Beet kann nicht −9 m breit sein. Diese Lösung fällt weg.',
  'fehler_bild': {'linien': [['_A', '_B', 'x + 4'], ['_B', '_C', '−9 m?'], ['_C', '_D', '45 m²'], ['_D', '_A', '']]},
  'regel': 'Variable festlegen, Gleichung aufstellen, lösen, ⟦prüfen⟧. Lösungen, die nicht zum Sachzusammenhang passen, fallen weg.'},
}
umbau(ETAPPEN, UMBAU)
# ---- UMBAU ENDE ----


def g_reinquadratisch(s):
    if s == 1:
        r = R.randint(2, 15)
        if R.random() < 0.5:
            return luecken(f'Löse x² = {r * r}.', L2, H2, [-r, r], f'x = ±√{r * r}, also x₁ = −{r}, x₂ = {r}.',
                           'Denke an beide Vorzeichen.', c=[f'-{r * r} / {r}', f'{r * r} / {r}'])
        return luecken(f'Löse x² − {r * r} = 0.', L2, H2, [-r, r], f'x² = {r * r}, also x = ±{r}.',
                       'Bringe die Zahl auf die andere Seite.', c=[f'-{r * r} / {r}', f'{r * r} / {r}'])
    if s == 2:
        a, r = R.randint(2, 6), R.randint(1, 10)
        k = a * r * r
        if R.random() < 0.3:
            return auswahl(f'Welche Lösungsmenge hat {a}x² + {k} = 0?', 'L = { }', [f'L = {{−{r}; {r}}}', f'L = {{{r}}}', f'L = {{−{r}}}'],
                           f'{a}x² = −{k} ⇔ x² = −{r * r}. Ein Quadrat ist nie negativ, also keine Lösung.',
                           'Stelle nach x² um. Kann ein Quadrat negativ sein?')
        return luecken(f'Löse {a}x² − {k} = 0.', L2, H2, [-r, r], f'{a}x² = {k} ⇔ x² = {r * r}, also x = ±{r}.',
                       'Erst nach x² auflösen, dann die Wurzel ziehen.', c=[f'-({k} / {a}) / {r}', f'({k} / {a}) / {r}'])
    p, r = nz(9), R.randint(1, 8)
    x1, x2 = p - r, p + r
    if R.random() < 0.35:
        if R.random() < 0.5:
            return auswahl(f'Jemand löst {minus_klammer(p)}² = {r * r} so: {minus_klammer(p)[1:-1]} = {r}, also x = {dz(x2)}. Was stimmt?',
                           f'Unvollständig: Auch {minus_klammer(p)[1:-1]} = −{r}, also x = {dz(x1)}.',
                           ['Richtig, das ist die einzige Lösung.', f'Falsch: Richtig ist nur x = {dz(x1)}.', f'Falsch: x = {dz(r - p)}.'],
                           f'Die Klammer kann {r} oder −{r} sein: x = {dz(p)} + {r} = {dz(x2)} oder x = {dz(p)} − {r} = {dz(x1)}.',
                           'Welche Zahlen ergeben quadriert ' + str(r * r) + '?')
        a = R.randint(2, 6)
        if r * r == a * r * r // a and isqrt(a * r * r) ** 2 == a * r * r: return None
        return auswahl(f'Jemand löst {a}x² = {dz(a * r * r)} so: x = ±√{dz(a * r * r)}. Was stimmt?',
                       f'Falsch: Erst durch {a} teilen: x² = {r * r}, x = ±{r}.',
                       ['Richtig, man zieht direkt die Wurzel.', f'Falsch: x = ±{dz(Fr(a * r * r, 2)) if (a * r * r) % 2 == 0 else dz(a * r * r)}', f'Falsch: x = {r}, nur positiv.'],
                       f'Vor dem Wurzelziehen muss x² allein stehen: x² = {dz(a * r * r)} : {a} = {r * r}, also x = ±{r}.',
                       'Steht x² schon allein?')
    if R.random() < 0.3:
        return auswahl(f'Welche Lösungsmenge hat {minus_klammer(p)}² = {dz(-r * r)}?', 'L = { }',
                       [f'L = {{{dz(x1)}; {dz(x2)}}}', f'L = {{{dz(p)}}}', f'L = {{{dz(-r)}; {dz(r)}}}'],
                       f'Ein Quadrat kann nicht {dz(-r * r)} ergeben, also keine Lösung.', 'Kann ein Quadrat negativ sein?')
    return luecken(f'Löse {minus_klammer(p)}² = {r * r}.', L2, H2, [x1, x2],
                   f'{minus_klammer(p)[1:-1]} = ±{r}, also x₁ = {dz(p)} − {r} = {dz(x1)}, x₂ = {dz(p)} + {r} = {dz(x2)}.',
                   'Ziehe zuerst die Wurzel: Die Klammer ist ± die Wurzel.', c=[f'{p} - {r * r} / {r}', f'{p} + {r * r} / {r}'])


def g_ausklammern(s):
    if s == 1:
        b = nz(12)
        return luecken(f'Löse x² {plus_v(b)} = 0.', L2, H2, sorted([0, -b]), f'x(x {plus(b)}) = 0, also x = 0 oder x = {dz(-b)}.',
                       'Klammere x aus.', c=[f'min(0, -({b}))', f'max(0, -({b}))'])
    a, x2 = R.randint(2, 7), nz(9)
    b = -a * x2
    if s == 2:
        return luecken(f'Löse {poly(a, b, 0)} = 0.', L2, H2, sorted([0, x2]),
                       f'x({a}x {plus(b)}) = 0, also x = 0 oder {a}x = {dz(-b)}, x = {dz(x2)}.',
                       'Klammere x aus und setze jeden Faktor gleich null.', c=[f'min(0, -({b}) / {a})', f'max(0, -({b}) / {a})'])
    if R.random() < 0.5:
        return luecken(f'Löse {a}x² = {poly(-b, 0)}.', L2, H2, sorted([0, x2]),
                       f'{poly(a, b, 0)} = 0 ⇔ x({a}x {plus(b)}) = 0, also x = 0 oder x = {dz(x2)}.',
                       'Bringe alles auf eine Seite – nicht durch x teilen!', c=[f'min(0, -({b}) / {a})', f'max(0, -({b}) / {a})'])
    return auswahl(f'Jemand löst {a}x² = {poly(-b, 0)}, indem er durch x teilt, und erhält x = {dz(x2)}. Was stimmt?',
                   f'Unvollständig: Auch x = 0 ist eine Lösung.',
                   ['Richtig, das ist die einzige Lösung.', f'Falsch: Die Lösung ist x = {dz(-x2)}.', f'Falsch: Die Lösung ist x = {dz(x2 * a)}.'],
                   f'Durch x teilen ist nur für x ≠ 0 erlaubt. Ausklammern: x({a}x {plus(b)}) = 0 liefert x = 0 und x = {dz(x2)}.',
                   'Was passiert beim Teilen durch x mit der Möglichkeit x = 0?')


def g_faktorisieren(s):
    if s == 1:
        p, q = nz(9), nz(9)
        if p == q: return None
        lo, hi = sorted([p, q])
        return luecken(f'Löse {minus_klammer(p)} · {minus_klammer(q)} = 0.', L2, H2, [lo, hi],
                       f'Satz vom Nullprodukt: {minus_klammer(p)[1:-1]} = 0 oder {minus_klammer(q)[1:-1]} = 0, also x = {dz(p)} oder x = {dz(q)}.',
                       'Wann ist ein Produkt null?', c=[f'min({p}, {q})', f'max({p}, {q})'])
    if s == 2:
        p = nz(12)
        if R.random() < 0.5:
            return luecken(f'Löse {poly(1, -2 * p, p * p)} = 0.', 'x = □', 'die einzige Lösung', [p],
                           f'Binomische Formel: {minus_klammer(p)}² = 0, also x = {dz(p)}.',
                           'Erkennst du eine binomische Formel?', c=[f'-({-2 * p}) / 2'])
        a, r = R.randint(1, 5), R.randint(1, 10)
        return luecken(f'Löse {poly(a * a, 0, -r * r)} = 0 durch Faktorisieren.', L2, H2, [Fr(-r, a), Fr(r, a)] if r % a == 0 else [0, 0],
                       f'3. binomische Formel: ({a if a > 1 else ""}x − {r})({a if a > 1 else ""}x + {r}) = 0, also x = ±{br(Fr(r, a))}.',
                       'Erkennst du die 3. binomische Formel?', c=[f'-{r} / {a}', f'{r} / {a}']) if r % a == 0 else None
    if R.random() < 0.35:
        a = R.randint(2, 5)
        z = nz(9)
        if Fr(z, a).denominator == 1: return None
        q = nz(9)
        x1 = Fr(z, a)
        k1 = f'({a}x − {z})' if z > 0 else f'({a}x + {-z})'
        return luecken(f'Löse {k1}{minus_klammer(q)} = 0.', 'x₁ = □/□; x₂ = □', 'x₁ aus der ersten Klammer als gekürzter Bruch (Minus in den Zähler), x₂ aus der zweiten',
                       [x1.numerator, x1.denominator, q],
                       f'{k1[1:-1]} = 0 ⇔ {a}x = {dz(z)} ⇔ x = {br(x1)}; {minus_klammer(q)[1:-1]} = 0 ⇔ x = {dz(q)}.',
                       'Setze jede Klammer einzeln gleich null und löse nach x.', c=[f'{x1.numerator}', f'{x1.denominator}', f'{q}'])
    p, q = nz(9), nz(9)
    if p == q: return None
    b, c = -(p + q), p * q
    lo, hi = sorted([p, q])
    return luecken(f'Löse {poly(1, b, c)} = 0 durch Faktorisieren.', L2, H2, [lo, hi],
                   f'Gesucht p, q mit p + q = {dz(p + q)} und p · q = {dz(c)}: p = {dz(lo)}, q = {dz(hi)}. ({minus_klammer(lo)[1:-1]})({minus_klammer(hi)[1:-1]}) = 0.',
                   'Faktorisiere in (x − p)(x − q): Suche zwei Zahlen p und q, deren Produkt das Zahlglied und deren Summe die Gegenzahl von b ist.',
                   c=[wurzel_c(1, b, c)[2], wurzel_c(1, b, c)[3]])


def g_ergaenzung(s):
    h = nz(8)
    b = 2 * h
    d = R.randint(1, 10)
    if s < 3:
        if s == 1:
            r = d
            d = r * r
        c = h * h - d
        if c == 0: return None
        rechts = d
        if h > 0:
            sch = '(x + □)² = □'
            werte = [h, rechts]
        else:
            sch = '(x − □)² = □'
            werte = [-h, rechts]
        return luecken(f'Bringe {poly(1, b, c)} = 0 mit quadratischer Ergänzung auf die Form {sch.replace("□", "…")}.', sch,
                       'Zahl in der Klammer, Zahl rechts', werte,
                       f'Hälfte von {dz(b)} ist {dz(h)}, ergänze {dz(h * h)}: {poly(1, b, h * h)} = {dz(-c)} + {dz(h * h)}, also {minus_klammer(-h)}² = {dz(rechts)}.',
                       'Halbiere den Koeffizienten von x und quadriere ihn.', c=[f'abs({b}) / 2', f'({b} / 2) ** 2 - ({c})'])
    r = R.randint(1, 9)
    c = h * h - r * r
    if c == 0: return None
    if R.random() < 0.35:
        a = R.choice([2, 3])
        x1, x2, e1, e2 = wurzel_c(a, a * b, a * c)
        return luecken(f'Löse {poly(a, a * b, a * c)} = 0 mit quadratischer Ergänzung.', L2, H2, [x1, x2],
                       f'Erst durch {a} teilen: {poly(1, b, c)} = 0. {minus_klammer(-h)}² = {dz(-c)} + {dz(h * h)} = {r * r}, also x {plus(h)} = ±{r}: x₁ = {dz(x1)}, x₂ = {dz(x2)}.',
                       'Teile zuerst durch den Faktor vor x², dann ergänzen.', c=[e1, e2])
    x1, x2, e1, e2 = wurzel_c(1, b, c)
    return luecken(f'Löse {poly(1, b, c)} = 0 mit quadratischer Ergänzung.', L2, H2, [x1, x2],
                   f'{minus_klammer(-h)}² = {dz(-c)} + {dz(h * h)} = {r * r}, also x {plus(h)} = ±{r}: x₁ = {dz(x1)}, x₂ = {dz(x2)}.',
                   'Ergänze (b/2)² auf beiden Seiten, dann Wurzel ziehen.', c=[e1, e2])


def g_loesungsformel(s):
    if s == 1:
        a, b, c = nz(5), nz(9), nz(12)
        D = b * b - 4 * a * c
        return zahl(f'Berechne die Diskriminante von {poly(a, b, c)} = 0.', f'D = b² − 4ac = {kl(b)}² − 4 · {kl(a)} · {kl(c)} = {dz(b * b)} {plus(-4 * a * c)} = {dz(D)}.',
                    'Lies a, b und c mit Vorzeichen ab und setze in b² − 4ac ein.', D, f'({b}) ** 2 - 4 * ({a}) * ({c})')
    if s == 2:
        a = R.choice([1, 1, 2, 3, -1, -2])
        p, q = nz(7), nz(7)
        if p == q: return None
        b, c = -a * (p + q), a * p * q
        x1, x2, e1, e2 = wurzel_c(a, b, c)
        D = b * b - 4 * a * c
        return luecken(f'Löse {poly(a, b, c)} = 0 mit der Lösungsformel.', L2, H2, [x1, x2],
                       f'a = {dz(a)}, b = {dz(b)}, c = {dz(c)}; D = {dz(D)}, √D = {isqrt(D)}; x₁,₂ = ({dz(-b)} ± {isqrt(D)}) / {dz(2 * a)}: {dz(x1)} und {dz(x2)}.',
                       'Erst a, b, c ablesen, dann D berechnen.', c=[e1, e2])
    if R.random() < 0.4:
        p, q = sorted(R.sample([i for i in range(-9, 10) if i], 2))
        b, c = -(p + q), p * q
        if R.random() < 0.5:
            if b == 0: return None
            return luecken(f'Löse x{minus_klammer(-b)} = {dz(-c)}.', L2, H2, [p, q],
                           f'Ausmultiplizieren und alles nach links: {poly(1, b, c)} = 0. D = {dz(b * b - 4 * c)}; Lösungen {dz(p)} und {dz(q)}.',
                           'Multipliziere aus und bringe die Gleichung auf die Form ax² + bx + c = 0.', c=list(wurzel_c(1, b, c)[2:]))
        k = nz(5)
        m, n = -2 * k - b, k * k - c
        if m == 0: return None
        rechts = poly(m, n)
        return luecken(f'Löse {minus_klammer(k)}² = {rechts}.', L2, H2, [p, q],
                       f'Links ausmultiplizieren: {poly(1, -2 * k, k * k)} = {rechts}. Alles nach links: {poly(1, b, c)} = 0. Lösungen {dz(p)} und {dz(q)}.',
                       'Erst ausmultiplizieren, dann alles auf eine Seite bringen.', c=list(wurzel_c(1, b, c)[2:]))
    a = R.choice([2, 4, -2])
    p = Fr(nz(9), 2)
    if p.denominator == 1: return None
    q = nz(6)
    b = -a * (p + q)
    c = a * p * q
    if b.denominator != 1 or c.denominator != 1: return None
    b, c = int(b), int(c)
    x1, x2, e1, e2 = wurzel_c(a, b, c)
    return zahl(f'Löse {poly(a, b, c)} = 0 mit der Lösungsformel. Gib die größere Lösung an.',
                f'D = {dz(b * b - 4 * a * c)}, √D = {isqrt(b * b - 4 * a * c)}; x₁ = {dz(x1)}, x₂ = {dz(x2)}. Größere Lösung: {dz(x2)}.',
                'Setze sorgfältig mit Vorzeichen in die Lösungsformel ein.', x2, e2)


def _disk_beispiel(art, nur_a1=False):
    """Gleichung mit vorgegebener Lösungsanzahl: (a, b, c)."""
    if art == 'zwei':
        a = 1 if nur_a1 else R.choice([1, 1, 2, -1, 3])
        p, q = R.sample([i for i in range(-6, 7) if i], 2)
        if R.random() < 0.3:
            return a, nz(8), -R.randint(1, 9) * (1 if a > 0 else -1)  # D > 0 auch ohne ganzzahlige Lösungen
        return a, -a * (p + q), a * p * q
    if art == 'eine':
        k = 1 if nur_a1 else R.choice([1, 1, 2, 3])
        r = nz(5)
        return k * k, 2 * k * r, r * r  # (kx + r)²
    a = 1 if nur_a1 else R.randint(1, 4)
    b = nz(6)
    c = (b * b) // (4 * a) + R.randint(1, 6)
    return a, b, c


def g_diskriminante(s):
    if s == 1 or (s == 2 and R.random() < 0.55):
        art = R.choice(['zwei', 'eine', 'keine'])
        a, b, c = _disk_beispiel(art, nur_a1=(s == 1))
        D = b * b - 4 * a * c
        assert (D > 0, D == 0, D < 0) == (art == 'zwei', art == 'eine', art == 'keine')
        n = {'zwei': 'zwei Lösungen', 'eine': 'genau eine Lösung', 'keine': 'keine Lösung'}[art]
        a_ = auswahl(f'Wie viele Lösungen hat {poly(a, b, c)} = 0?', n, ['zwei Lösungen', 'genau eine Lösung', 'keine Lösung'],
                     f'D = {kl(b)}² − 4 · {kl(a)} · {kl(c)} = {dz(D)}{" > 0" if D > 0 else " < 0" if D < 0 else ""}, also {n}.',
                     'Berechne D = b² − 4ac und achte auf das Vorzeichen.')
        if s == 1 and a == 1 and R.random() < 0.5:
            xs = Fr(-b, 2)
            ys = c - xs * xs
            if abs(xs) <= 6 and -6 <= ys <= 6:
                lo_y = int(min(-2, ys - 1)); hi_y = int(max(4, ys + 5))
                a_['f']['text'] = f'Die Parabel zu y = {poly(1, b, c)} ist gezeichnet. Wie viele Lösungen hat {poly(1, b, c)} = 0?'
                a_['w'] = f'Die Lösungen sind die Schnittstellen mit der x-Achse. ' + a_['w']
                a_['h'] = 'Wie oft trifft die Parabel die x-Achse? Prüfe mit D = b² − 4ac.'
                bild(a_, {'typ': 'koordinaten', 'x': [int(xs) - 5, int(xs) + 5], 'y': [lo_y, hi_y],
                          'graphen': [{'art': 'poly', 'k': [c, b, 1]}]})
        return a_
    if s == 2 or R.random() < 0.3:
        h = R.randint(1, 10)
        b = 2 * h * R.choice([1, -1])
        return zahl(f'Für welche Zahl c hat x² {plus_v(b)} + c = 0 genau eine Lösung?', f'Genau eine Lösung bei D = 0: {dz(b * b)} − 4c = 0, also c = {dz(h * h)}.',
                    'Setze die Diskriminante gleich null.', h * h, f'({b}) ** 2 / 4')
    if R.random() < 0.55:
        h = R.randint(2, 9)
        c = h * h
        return zahl(f'Für welche positive Zahl k hat x² + kx + {c} = 0 genau eine Lösung?',
                    f'D = k² − 4 · {c} = 0 ⇔ k² = {4 * c} ⇔ k = ±{2 * h}; positiv: k = {2 * h}.',
                    'Setze D = 0 und löse nach k.', 2 * h, f'(4 * {c}) / ({2 * h})')
    a, b, c = R.randint(1, 4), nz(6), R.randint(1, 10)
    D = b * b - 4 * a * c
    if D >= 0: return None
    return auswahl(f'Jemand sagt: „{poly(a, b, c)} = 0 hat zwei Lösungen, weil die Lösungsformel ± enthält.“ Was stimmt?',
                   f'Falsch: D = {dz(D)} < 0, es gibt keine Lösung.',
                   ['Richtig: Wegen ± gibt es immer zwei Lösungen.', f'Falsch: Es gibt genau eine Lösung x = {br(Fr(-b, 2 * a))}.',
                    f'Richtig: D = {dz(-D)} > 0.'],
                   f'D = {kl(b)}² − 4 · {a} · {c} = {dz(D)}. Aus einer negativen Zahl gibt es keine Wurzel, also keine Lösung.',
                   'Berechne zuerst die Diskriminante.')


def g_sachaufgabe(s):
    typ = R.random()
    if s == 1:
        x = R.randint(4, 30)
        return zahl(f'Ein quadratischer Garten hat {dz(x * x)} m² Fläche. Wie viele Meter Zaun braucht man ringsum?',
                    f'x² = {dz(x * x)}, x = ±{x}; als Länge nur x = {x} m. Zaun: 4 · {x} m = {4 * x} m.',
                    'Stelle die Gleichung x² = … für die Seitenlänge auf. Der Zaun ist der Umfang.', 4 * x, f'4 * ({x * x} / {x})', einheit='m')
    if s == 2:
        x, d = R.randint(3, 15), R.randint(1, 8)
        A = x * (x + d)
        return zahl(f'Ein Rechteck ist {d} cm länger als breit und hat einen Flächeninhalt von {dz(A)} cm². Wie breit ist es?',
                    f'x(x + {d}) = {dz(A)} ⇔ {poly(1, d, -A)} = 0. Lösungen {dz(-x - d)} und {x}; Breite {x} cm.',
                    'Breite x, Länge x + ' + str(d) + '. Flächeninhalt = Länge · Breite.', x, wurzel_c(1, d, -A)[3], einheit='cm')
    if typ < 0.35:
        n = R.randint(3, 30)
        p = n * (n + 1)
        return zahl(f'Das Produkt zweier aufeinanderfolgender positiver ganzer Zahlen ist {dz(p)}. Wie heißt die kleinere Zahl?',
                    f'x(x + 1) = {dz(p)} ⇔ x² + x − {dz(p)} = 0. Lösungen {dz(-n - 1)} und {n}; positiv: {n}.',
                    'Nenne die kleinere Zahl x. Wie heißt die nächste Zahl?', n, wurzel_c(1, 1, -p)[3])
    if typ < 0.55:
        a, b = R.choice([(20, 30), (30, 40), (40, 50), (20, 25), (30, 45), (40, 60), (24, 30), (18, 24)])
        w = R.randint(2, 6)
        G = (a + 2 * w) * (b + 2 * w)
        return zahl(f'Ein Bild ist {a} cm × {b} cm groß. Es bekommt einen gleich breiten Rahmen; Bild und Rahmen haben zusammen {dz(G)} cm². Wie breit ist der Rahmen?',
                    f'({a} + 2x)({b} + 2x) = {dz(G)} ⇔ {poly(4, 2 * (a + b), a * b - G)} = 0. Positive Lösung x = {w}; die negative passt nicht zu einer Breite.',
                    'Der Rahmen kommt auf jeder Seite dazu: Breite und Höhe wachsen um 2x.', w, wurzel_c(4, 2 * (a + b), a * b - G)[3], einheit='cm')
    if typ < 0.75:
        a, b, w = R.randint(6, 20), R.randint(4, 15), R.randint(1, 4)
        A = (a + 2 * w) * (b + 2 * w) - a * b
        return zahl(f'Um ein rechteckiges Beet ({a} m × {b} m) wird ein gleich breiter Weg gelegt. Der Weg hat {dz(A)} m² Fläche. Wie breit ist er?',
                    f'({a} + 2x)({b} + 2x) − {a * b} = {dz(A)} ⇔ {poly(4, 2 * (a + b), -A)} = 0. Positive Lösung x = {w}.',
                    'Ganze Fläche mit Weg minus Beetfläche = Wegfläche.', w, wurzel_c(4, 2 * (a + b), -A)[3], einheit='m')
    t1, t2 = sorted(R.sample(range(1, 7), 2))
    v, h = 5 * (t1 + t2), 5 * t1 * t2
    return zahl(f'Ein Ball wird senkrecht nach oben geworfen. Seine Höhe über dem Abwurfpunkt ist h(t) = {v}t − 5t² (t in s, h in m). Nach wie vielen Sekunden ist er zum ersten Mal {dz(h)} m hoch?',
                f'{v}t − 5t² = {dz(h)} ⇔ 5t² − {v}t + {dz(h)} = 0. Lösungen t = {dz(wurzel_c(5, -v, h)[0])} und t = {dz(wurzel_c(5, -v, h)[1])}; zuerst bei {dz(wurzel_c(5, -v, h)[0])} s.',
                'Setze h(t) gleich der Höhe und bringe alles auf eine Seite. Zum ersten Mal = kleinere Lösung.',
                wurzel_c(5, -v, h)[0], wurzel_c(5, -v, h)[2], einheit='s')


GEN = {'reinquadratisch': g_reinquadratisch, 'ausklammern': g_ausklammern, 'faktorisieren': g_faktorisieren,
       'ergaenzung': g_ergaenzung, 'loesungsformel': g_loesungsformel, 'diskriminante': g_diskriminante, 'sachaufgabe': g_sachaufgabe}

# ---------- Zehnte Runde (schwer-kl9): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Abschnitt mit eigenem festen Zufallsstart (anhaengen(..., 9904, ...)), läuft erst nach bauen():
# alle bisherigen Aufgaben bleiben unverändert. Vorbilder: Bayerischer Mathematik-Test 10 (ISB; quadratische
# Gleichung lösen, Gleichung ohne Lösung angeben, Anhalteweg mit Faktor), Illustrierende Aufgaben Realschule 9 (I)
# (Gehege an der Hauswand, Bremsweg), MSA Berlin/Brandenburg (Nullstellen einer Parabel). Zahlen und Wortlaut eigen.
from _schwer_kl9 import anhaengen  # noqa: E402
from _kl9 import K as _K  # noqa: E402


def schwer():
    P, K, O = 'pruefung', 'knobel', ''
    L2 = 'x₁ = □; x₂ = □'
    H = 'kleinere Lösung zuerst'
    return [
        # reinquadratisch
        ('reinquadratisch', 3, P, auswahl('Welche Gleichung hat keine reelle Lösung?', '3x² + 12 = 0', ['3x² − 12 = 0', '−3x² + 12 = 0', '3x² = 0'],
                                          '3x² + 12 = 0 ⇔ x² = −4: Ein Quadrat ist nie negativ. Die anderen: x² = 4 (zwei Lösungen), x² = 4 (zwei), x² = 0 (eine).',
                                          'Stelle jeweils x² allein und schau auf das Vorzeichen.')),
        ('reinquadratisch', 3, P, zahl('Für den Bremsweg eines Autos gilt näherungsweise s = v²/100 (s in m, v in km/h). Bei welcher Geschwindigkeit ist der Bremsweg 36 m lang?',
                                       '36 = v²/100 ⇔ v² = 3 600 ⇔ v = 60 (die Lösung −60 passt nicht zu einer Geschwindigkeit).',
                                       'Setze s = 36 ein und stelle v² allein.', 60, '(36 * 100) / 60', einheit='km/h')),
        ('reinquadratisch', 3, K, zahl('Die Gleichung x² = d hat die Lösungen −0,3 und 0,3. Wie groß ist d?', 'd = 0,3² = 0,09. Probe: (−0,3)² = 0,09 auch.',
                                       'Rückwärts denken: Setze eine Lösung ein.', 0.09, '0.3 ** 2')),
        ('reinquadratisch', 3, O, luecken('Löse (2x − 3)² = 49.', L2, H, [-2, 5],
                                          '2x − 3 = 7 oder 2x − 3 = −7. Also 2x = 10, x = 5, oder 2x = −4, x = −2.',
                                          'Die Klammer ist 7 oder −7. Löse dann beide linearen Gleichungen.', ['(3 - 7) // 2', '(3 + 7) // 2'])),
        ('reinquadratisch', 2, O, luecken('Löse 0,5x² = 8.', L2, H, [-4, 4], 'x² = 16, also x = −4 oder x = 4.', 'Erst mal 2 nehmen.', ['-4', '4'])),
        ('reinquadratisch', 2, O, auswahl('Welche Lösungsmenge hat x² + 9 = 9?', 'L = {0}', ['L = {−3; 3}', 'L = { }', 'L = {9}'],
                                          'x² = 0, also nur x = 0.', 'Subtrahiere 9 auf beiden Seiten.')),
        # ausklammern
        ('ausklammern', 3, P, zahl('Löse 3x² = 7,5x. Gib die Lösung an, die nicht 0 ist.', '3x² − 7,5x = 0 ⇔ x(3x − 7,5) = 0. Also x = 0 oder x = 7,5 : 3 = 2,5.',
                                   'Alles auf eine Seite bringen und x ausklammern – nicht durch x teilen.', 2.5, '7.5 / 3')),
        ('ausklammern', 3, P, luecken('Löse x³ − 9x = 0.', 'x₁ = □; x₂ = □; x₃ = □', 'der Größe nach', [-3, 0, 3],
                                      'x(x² − 9) = 0. Also x = 0 oder x² = 9, d. h. x = −3 oder x = 3.', 'Klammere x aus. Der Rest ist eine reinquadratische Gleichung.', ['-3', '0', '3'])),
        ('ausklammern', 3, K, zahl('Für welche Zahl b hat die Gleichung x² + bx = 0 die Lösungen 0 und 6?', 'x(x + b) = 0 hat die Lösungen 0 und −b. Also −b = 6, b = −6. Probe: x² − 6x = x(x − 6).',
                                   'Klammere aus und vergleiche die zweite Lösung mit 6.', -6, '0 - 6')),
        ('ausklammern', 3, O, luecken('Löse x(x − 5) = 3x.', L2, H, [0, 8], 'x² − 5x = 3x ⇔ x² − 8x = 0 ⇔ x(x − 8) = 0. Also x = 0 oder x = 8.',
                                      'Ausmultiplizieren, alles nach links bringen, dann x ausklammern.', ['0', '5 + 3'])),
        ('ausklammern', 2, O, luecken('Löse −x² + 6x = 0.', L2, H, [0, 6], 'x(−x + 6) = 0, also x = 0 oder x = 6.', 'Klammere x aus.', ['0', '6'])),
        ('ausklammern', 2, O, zahl('Löse 4x² + 10x = 0. Gib die negative Lösung an.', 'x(4x + 10) = 0, also x = 0 oder 4x = −10, x = −2,5.',
                                   'Klammere x aus und setze beide Faktoren null.', -2.5, '-10 / 4')),
        # faktorisieren
        ('faktorisieren', 3, P, luecken('Die Funktion f mit f(x) = x² − 10x + 21 hat zwei Nullstellen. Bestimme sie durch Faktorisieren.', L2, H, [3, 7],
                                        'Zwei Zahlen mit Produkt 21 und Summe 10: 3 und 7. f(x) = (x − 3)(x − 7), Nullstellen 3 und 7.',
                                        'Nullstellen: f(x) = 0 setzen. Suche zwei Zahlen mit Produkt 21 und Summe 10.', ['3', '7'])),
        ('faktorisieren', 3, P, luecken('Gib eine Gleichung der Form x² + bx + c = 0 an, die genau die Lösungen −2 und 5 hat.', 'x² + □x + □ = 0', 'b und c eintragen (auch negativ)', [-3, -10],
                                        '(x + 2)(x − 5) = 0 ausmultiplizieren: x² − 5x + 2x − 10 = x² − 3x − 10. Also b = −3, c = −10.',
                                        'Schreibe zuerst die Produktform mit den Lösungen und multipliziere aus.', ['2 - 5', '2 * (-5)'])),
        ('faktorisieren', 3, K, zahl('Für wie viele ganze Zahlen b hat x² + bx + 6 = 0 zwei verschiedene ganzzahlige Lösungen?',
                                     'Die Lösungen p, q müssen Produkt 6 haben: (1; 6), (2; 3), (−1; −6), (−2; −3). Dann ist b = −(p + q) = −7, −5, 7 oder 5. Also 4 Werte.',
                                     'Aus (x − p)(x − q) folgt p · q = 6. Liste alle ganzzahligen Paare auf.', 4, '2 * 2')),
        ('faktorisieren', 3, O, luecken('Löse (x − 3)(x + 4) = 8.', L2, H, [-5, 4],
                                        'Rechts steht nicht 0! Ausmultiplizieren: x² + x − 12 = 8 ⇔ x² + x − 20 = 0 ⇔ (x + 5)(x − 4) = 0. Also −5 und 4.',
                                        'Der Satz vom Nullprodukt gilt nur, wenn rechts 0 steht. Erst umformen.', ['-5', '4'])),
        ('faktorisieren', 2, O, luecken('Löse x² − x − 12 = 0 durch Faktorisieren.', L2, H, [-3, 4], 'Produkt −12, Summe 1: −3 und 4. (x + 3)(x − 4) = 0.',
                                        'Suche zwei Zahlen mit Produkt −12.', ['-3', '4'])),
        ('faktorisieren', 2, O, luecken('Löse (2x − 6)(x + 5) = 0.', L2, H, [-5, 3], '2x − 6 = 0 ⇔ x = 3; x + 5 = 0 ⇔ x = −5.', 'Setze jeden Faktor null.', ['-5', '6 // 2'])),
        # ergaenzung
        ('ergaenzung', 3, P, luecken('Löse x² + 3x − 10 = 0 mit quadratischer Ergänzung.', L2, H, [-5, 2],
                                     'x² + 3x = 10. Ergänze 1,5² = 2,25: (x + 1,5)² = 12,25. x + 1,5 = ±3,5, also x = 2 oder x = −5.',
                                     'Die Hälfte von 3 ist 1,5. Ergänze 1,5² auf beiden Seiten.', ['-1.5 - 3.5', '-1.5 + 3.5'])),
        ('ergaenzung', 3, P, luecken('Bringe 2x² − 12x + 10 = 0 mit quadratischer Ergänzung auf die Form (x − …)² = ….', '(x − □)² = □', 'Zahlen eintragen', [3, 4],
                                     'Erst durch 2 teilen: x² − 6x + 5 = 0. Ergänze 9: x² − 6x + 9 = −5 + 9, also (x − 3)² = 4.',
                                     'Vor dem Ergänzen muss vor x² eine 1 stehen.', ['6 // 2', '9 - 5'])),
        ('ergaenzung', 3, K, zahl('Bei x² + 8x + c = 0 führt die quadratische Ergänzung auf (x + 4)² = 9. Wie groß ist c?',
                                  'x² + 8x = −c, ergänzt: (x + 4)² = 16 − c. Also 16 − c = 9 und c = 7. Probe: x² + 8x + 7 = 0.',
                                  'Rechne die Ergänzung rückwärts: Was steht rechts, wenn du 16 ergänzt?', 7, '16 - 9')),
        ('ergaenzung', 3, O, luecken('Löse x² − 8x + 13 = 0 mit quadratischer Ergänzung. Die Lösungen haben die Form 4 ± √d.', 'x = 4 ± √□', 'd eintragen', [3],
                                     'x² − 8x = −13. Ergänze 16: (x − 4)² = 3. Also x − 4 = ±√3 und x = 4 ± √3.', 'Ergänze (8/2)² = 16.', ['16 - 13'])),
        ('ergaenzung', 2, O, zahl('Welche Zahl musst du zu x² + 18x addieren, damit ein vollständiges Quadrat entsteht?', 'Hälfte von 18 ist 9, ergänze 9² = 81: x² + 18x + 81 = (x + 9)².',
                                  'Halbiere die Zahl vor x und quadriere.', 81, '(18 / 2) ** 2')),
        ('ergaenzung', 2, O, luecken('Bringe x² − 2x − 8 = 0 auf die Form (x − …)² = ….', '(x − □)² = □', 'Zahlen eintragen', [1, 9],
                                     'x² − 2x = 8, ergänze 1: (x − 1)² = 9.', 'Hälfte von 2 ist 1, ergänze 1² = 1.', ['2 // 2', '8 + 1'])),
        # loesungsformel
        ('loesungsformel', 3, P, luecken('Löse 3x² + x − 2 = 0.', 'x₁ = □; x₂ = □/□', 'erst die ganze Zahl, dann den Bruch', [-1, 2, 3],
                                         'a = 3, b = 1, c = −2. D = 1 + 24 = 25, √D = 5. x = (−1 ± 5)/6: x₁ = −6/6 = −1, x₂ = 4/6 = 2/3.',
                                         'Lösungsformel mit a = 3, b = 1, c = −2. Kürze am Ende.', ['(-1 - 5) // 6', '2', '3'])),
        ('loesungsformel', 3, P, zahl('Löse ohne Taschenrechner 0,5x² − x − 4 = 0. Gib die positive Lösung an.',
                                      'Mal 2: x² − 2x − 8 = 0. D = 4 + 32 = 36, x = (2 ± 6)/2: 4 oder −2. Positive Lösung: 4.',
                                      'Multipliziere zuerst mit 2, dann wird es einfacher.', 4, '(2 + 6) / 2')),
        ('loesungsformel', 3, K, zahl('Die Gleichung x² + bx − 12 = 0 hat die Lösung x = 2. Wie heißt die andere Lösung?',
                                      'Einsetzen: 4 + 2b − 12 = 0, also b = 4. x² + 4x − 12 = (x − 2)(x + 6) = 0. Die andere Lösung ist −6. (Kurz: Produkt der Lösungen = −12.)',
                                      'Setze x = 2 ein und bestimme zuerst b.', -6, '-12 / 2')),
        ('loesungsformel', 3, O, luecken('Löse (2x + 1)² = 3x + 4.', 'x₁ = □; x₂ = □/□', 'erst die ganze Zahl, dann den Bruch', [-1, 3, 4],
                                         '4x² + 4x + 1 = 3x + 4 ⇔ 4x² + x − 3 = 0. D = 1 + 48 = 49. x = (−1 ± 7)/8: −1 oder 3/4.',
                                         'Ausmultiplizieren, alles nach links, dann Lösungsformel.', ['(-1 - 7) // 8', '3', '4'])),
        ('loesungsformel', 2, O, zahl('Löse x² + 2x − 15 = 0 mit der Lösungsformel. Gib die größere Lösung an.', 'D = 4 + 60 = 64, x = (−2 ± 8)/2: 3 oder −5. Größere: 3.',
                                      'a = 1, b = 2, c = −15.', 3, '(-2 + 8) / 2')),
        ('loesungsformel', 2, O, zahl('Berechne die Diskriminante von 5x² − 2x − 3 = 0.', 'D = (−2)² − 4 · 5 · (−3) = 4 + 60 = 64.', 'D = b² − 4ac. Achte auf die Vorzeichen.',
                                      64, '(-2)**2 - 4*5*(-3)')),
        # diskriminante
        ('diskriminante', 3, P, auswahl('Für welchen Term f(x) hat die Gleichung f(x) = 0 keine reelle Lösung?', 'x² − 2x + 3', ['x² − 2x − 3', 'x² − 2x + 1', '−x² − 2x + 3'],
                                        'x² − 2x + 3: D = 4 − 12 = −8 < 0. Die anderen: D = 16, D = 0, D = 16.', 'Berechne für jeden Term die Diskriminante.')),
        ('diskriminante', 3, P, auswahl('Für welche Zahlen c hat x² + 6x + c = 0 zwei Lösungen?', 'c < 9', ['c > 9', 'c = 9', 'c < 3'],
                                        'D = 36 − 4c > 0 ⇔ 4c < 36 ⇔ c < 9.', 'Zwei Lösungen bei D > 0. Stelle die Ungleichung für c auf.')),
        ('diskriminante', 3, K, auswahl('In ax² + bx + c = 0 ist a positiv und c negativ. Wie viele Lösungen hat die Gleichung?', 'immer zwei',
                                        ['immer keine', 'immer genau eine', 'Das hängt von b ab.'],
                                        'D = b² − 4ac. Weil a und c verschiedene Vorzeichen haben, ist −4ac > 0. b² ist nie negativ, also D > 0: immer zwei Lösungen.',
                                        'Welches Vorzeichen hat −4ac, wenn a > 0 und c < 0?')),
        ('diskriminante', 3, O, zahl('Für welche Zahl a hat ax² − 12x + 4 = 0 genau eine Lösung?', 'D = 144 − 16a = 0 ⇔ a = 9. Probe: 9x² − 12x + 4 = (3x − 2)².',
                                     'Genau eine Lösung bei D = 0.', 9, '144 / 16')),
        ('diskriminante', 2, O, auswahl('Wie viele Lösungen hat 4x² − 12x + 9 = 0?', 'genau eine Lösung', ['zwei Lösungen', 'keine Lösung'],
                                        'D = 144 − 144 = 0, also genau eine Lösung (x = 1,5).', 'Berechne D = b² − 4ac.')),
        ('diskriminante', 2, O, auswahl('Wie viele Lösungen hat −x² + 4x − 5 = 0?', 'keine Lösung', ['zwei Lösungen', 'genau eine Lösung'],
                                        'D = 16 − 4 · (−1) · (−5) = 16 − 20 = −4 < 0, also keine Lösung.', 'Achte auf a = −1 und c = −5.')),
        # sachaufgabe
        ('sachaufgabe', 3, P, zahl('Mit 20 m Zaun wird an einer Hauswand ein rechteckiges Gehege abgegrenzt; die Hauswand bildet die vierte Seite. Das Gehege soll 48 m² groß sein, die Seite entlang der Wand länger als 10 m. Wie lang ist eine Seite senkrecht zur Wand?',
                                   'Senkrechte Seite x, Seite an der Wand 20 − 2x. x(20 − 2x) = 48 ⇔ x² − 10x + 24 = 0: x = 4 oder x = 6. Bei x = 6 wäre die Wandseite nur 8 m, also x = 4 m (Wandseite 12 m).',
                                   'Der Zaun bildet nur drei Seiten: zweimal x und einmal die Seite an der Wand.', 4, '(10 - 2) / 2', einheit='m')),
        ('sachaufgabe', 3, P, zahl('Der Anhalteweg eines Autos ist Reaktionsweg plus Bremsweg: 0,3 · v + 0,01 · v² (v in km/h, Weg in m). Bei welcher Geschwindigkeit ist der Anhalteweg 40 m lang?',
                                   '0,01v² + 0,3v = 40 ⇔ v² + 30v − 4 000 = 0. D = 900 + 16 000 = 16 900, √D = 130. v = (−30 + 130)/2 = 50 (die negative Lösung fällt weg).',
                                   'Gleichung aufstellen, mit 100 malnehmen, Lösungsformel.', 50, '(-30 + 130) / 2', einheit='km/h')),
        ('sachaufgabe', 3, K, zahl('Eine Zahl plus ihr Kehrwert ergibt 2,5. Wie heißt die größere der beiden möglichen Zahlen?',
                                   'x + 1/x = 2,5 ⇔ x² − 2,5x + 1 = 0 ⇔ 2x² − 5x + 2 = 0. D = 9, x = (5 ± 3)/4: 2 oder 0,5. Größere: 2 (Probe: 2 + 0,5 = 2,5).',
                                   'Mit x malnehmen, dann entsteht eine quadratische Gleichung.', 2, '(5 + 3) / 4')),
        ('sachaufgabe', 3, O, zahl('Ein Ball wird geworfen. Seine Höhe ist h(t) = 2 + 15t − 5t² (t in s, h in m). Nach wie vielen Sekunden landet er auf dem Boden? Runde auf eine Nachkommastelle.',
                                   'h(t) = 0 ⇔ 5t² − 15t − 2 = 0. D = 225 + 40 = 265, √265 ≈ 16,28. t = (15 + 16,28)/10 ≈ 3,1 s (die negative Lösung fällt weg).',
                                   'Am Boden ist die Höhe 0.', round((15 + math.sqrt(265)) / 10, 1), f'round({_K((15 + math.sqrt(265)) / 10)}, 1)', einheit='s')),
        ('sachaufgabe', 2, O, zahl('Das Quadrat einer positiven Zahl ist um 30 größer als die Zahl selbst. Wie heißt die Zahl?', 'x² = x + 30 ⇔ x² − x − 30 = 0: x = 6 oder x = −5. Positiv: 6.',
                                   'Stelle die Gleichung x² = x + 30 auf.', 6, '(1 + 11) / 2')),
        ('sachaufgabe', 2, O, zahl('Ein Rechteck hat 26 cm Umfang und 40 cm² Flächeninhalt. Wie lang ist die längere Seite?',
                                   'Seiten x und 13 − x. x(13 − x) = 40 ⇔ x² − 13x + 40 = 0: x = 5 oder 8. Längere Seite 8 cm.',
                                   'Die Hälfte des Umfangs ist die Summe der beiden Seiten.', 8, '(13 + 3) / 2', einheit='cm')),
    ]


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('gleichungen.quadratisch', 13_9_4)
# a) derselbe Typ steht auf Stufe 2
BF.stufe('diskriminante', 'Für welche Zahl c hat x² − 14x + c = 0 genau eine Lösung?', 2)
BF.stufe('diskriminante', 'Für welche Zahl c hat x² + 4x + c = 0 genau eine Lösung?', 2)
# a) nur ein Umstellschritt mehr als Stufe 2
BF.stufe('ausklammern', 'Löse 7x² = 14x.', 2)
BF.stufe('ausklammern', 'Löse 5x² = 30x.', 2)

# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    d = bauen('gleichungen.quadratisch',
          'Quadratische Gleichungen mit der passenden Methode lösen und die Anzahl der Lösungen mit der Diskriminante begründen.',
          ['Ohne x-Glied: nach x² umstellen, ± Wurzel. Ohne Zahlglied: x ausklammern.', 'Produkt = 0: Satz vom Nullprodukt.',
           'Lösungsformel: x₁,₂ = (−b ± √(b² − 4ac)) / (2a).', 'D > 0: zwei, D = 0: eine, D < 0: keine Lösung.'],
          [('Sonderfälle', ['reinquadratisch', 'ausklammern', 'faktorisieren']), ('Allgemeine Verfahren', ['ergaenzung', 'loesungsformel']),
           ('Lösbarkeit und Anwendung', ['diskriminante', 'sachaufgabe'])],
          ETAPPEN, GEN,
          meiden={'reinquadratisch': ['3x² − 75 = 0'], 'ausklammern': ['2x² − 12x = 0'], 'faktorisieren': ['x² − 8x + 16 = 0'],
                  'ergaenzung': ['x² + 6x − 7 = 0'], 'loesungsformel': ['2x² − 5x − 3 = 0'], 'diskriminante': ['x² − 4x + 7 = 0'],
                  'sachaufgabe': ['4 cm länger als breit und hat einen Flächeninhalt von 45']},
          offen=['Lösungen werden als Lücken „x₁ = □; x₂ = □“ (kleinere zuerst) abgefragt; Lösungen mit Wurzeln (irrational) sind bewusst ausgelassen, weil Lücken nur ganze Zahlen erlauben. Im Unterricht kommen sie vor – ggf. Antworttyp „Wurzelterm“ nachrüsten.',
                 'Grafische Deutung (Nullstellen der Parabel) steht im Thema funktionen.quadratisch.'])
    anhaengen(d, 9904, schwer)
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden
