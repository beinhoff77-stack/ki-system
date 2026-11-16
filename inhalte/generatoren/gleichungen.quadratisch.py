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

if __name__ == '__main__':
    bauen('gleichungen.quadratisch',
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
