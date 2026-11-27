#!/usr/bin/env python3
"""Thema gleichungen.lgs3 – Lineare Gleichungssysteme mit 3 Unbekannten (Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(906)
V = ('x', 'y', 'z')
NR = ('I', 'II', 'III')
LX = 'x = □; y = □; z = □'


def lin(k, rechts, vs=V):
    """Linke Seite aus Koeffizienten, z. B. 2x − y + 3z = 5"""
    teile = []
    for c, v in zip(k, vs):
        if c == 0: continue
        b = '' if abs(c) == 1 else dz(abs(c))
        if not teile: teile.append(('−' if c < 0 else '') + b + v)
        else: teile.append(('− ' if c < 0 else '+ ') + b + v)
    return ' '.join(teile) + f' = {dz(rechts)}'


def tab(M, b, vs=V):
    """Gleichungssystem untereinander als Tabelle."""
    return {'typ': 'tabelle', 'kopf': ['', 'Gleichung'], 'zeilen': [[f'({NR[i]})', lin(M[i], b[i], vs)] for i in range(len(M))]}


def kreuz(u, v):
    from math import gcd
    d = [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]
    g = gcd(gcd(abs(d[0]), abs(d[1])), abs(d[2])) or 1
    return [c // g for c in d]


def system(M, b, vs=V):
    return '; '.join(f'({NR[i]}) {lin(M[i], b[i], vs)}' for i in range(len(M)))


def det3(M):
    (a, b_, c), (d, e, f), (g, h, i) = M
    return a * (e * i - f * h) - b_ * (d * i - f * g) + c * (d * h - e * g)


def det3_c(M):
    (a, b_, c), (d, e, f), (g, h, i) = M
    return f'({a})*(({e})*({i}) - ({f})*({h})) - ({b_})*(({d})*({i}) - ({f})*({g})) + ({c})*(({d})*({h}) - ({e})*({g}))'


def cramer_c(M, b):
    """Rechenausdrücke für die Lösung nach der Cramerschen Regel (unabhängige Nachrechnung)."""
    out = []
    for j in range(3):
        Mj = [[b[i] if k == j else M[i][k] for k in range(3)] for i in range(3)]
        out.append(f'({det3_c(Mj)}) / ({det3_c(M)})')
    return out


def zufall_lgs(gr=3, lsg=5, eins=True):
    while True:
        M = [[R.randint(-gr, gr) for _ in range(3)] for _ in range(3)]
        if det3(M) == 0: continue
        if eins and not all(any(abs(c) == 1 for c in row) for row in M): continue
        if any(sum(1 for c in row if c) < 2 for row in M): continue
        x = [R.randint(-lsg, lsg) for _ in range(3)]
        b = [sum(M[i][k] * x[k] for k in range(3)) for i in range(3)]
        return M, b, x


ETAPPEN = [
    {'lernziel': 'pruefen', 'titel': 'Ist das Zahlentripel eine Lösung?',
     'regel': 'Ein Zahlentripel (x | y | z) ist ⟦Lösung⟧ des Systems, wenn es ⟦alle drei Gleichungen⟧ erfüllt. Setze ein und vergleiche jede Gleichung.',
     'schritte': ['System (I) x + y + z = 6; (II) 2x − y = 0; (III) x − z = −2. Prüfe (1 | 2 | 3).',
                  '(I) 1 + 2 + 3 = 6 ✓; (II) 2 − 2 = 0 ✓; (III) 1 − 3 = −2 ✓: ⟦(1 | 2 | 3) ist Lösung⟧.'],
     'probe': 'Eine einzige falsche Gleichung genügt, damit das Tripel keine Lösung ist.',
     'fehler': 'Nur Gleichung (I) zu prüfen genügt nicht: (2 | 2 | 2) erfüllt (I), aber (II) ergibt 2 ≠ 0. Es müssen ⟦alle⟧ Gleichungen stimmen.'},
    {'lernziel': 'stufenform', 'titel': 'Stufenform von unten lösen',
     'regel': 'In der ⟦Stufenform⟧ hat die letzte Gleichung nur noch eine Variable. Löse sie, setze ⟦von unten nach oben⟧ ein.',
     'schritte': ['(III) 2z = 6 ⇒ z = 3. (II) y + z = 5 ⇒ y = 2.', '(I) x + y − z = 1 ⇒ x + 2 − 3 = 1 ⇒ ⟦x = 2, y = 2, z = 3⟧.'],
     'probe': '(I) 2 + 2 − 3 = 1 ✓',
     'fehler': 'In (II) y + z = 5 mit z = 3 auf y = 8 zu kommen ist falsch: 3 wird ⟦abgezogen⟧, nicht addiert: y = 5 − 3 = 2.'},
    {'lernziel': 'eliminieren', 'titel': 'Eine Variable eliminieren',
     'regel': 'Mit dem ⟦Additionsverfahren⟧ addierst oder subtrahierst du Vielfache zweier Gleichungen so, dass eine ⟦Variable wegfällt⟧. Auch die rechte Seite mitrechnen!',
     'schritte': ['(I) x + 2y − z = 3; (II) 2x − y + z = 4. Berechne (II) − 2 · (I).',
                  '2x − 2x = 0, −y − 4y = −5y, z + 2z = 3z, 4 − 6 = −2: ⟦−5y + 3z = −2⟧.'],
     'probe': 'Das x ist verschwunden ✓',
     'fehler': 'Bei (II) − 2 · (I) nur die x-Glieder zu verdoppeln ist falsch: ⟦Jedes Glied⟧ von (I), auch die rechte Seite, wird mit 2 multipliziert.'},
    {'lernziel': 'loesen', 'titel': 'LGS mit drei Unbekannten lösen',
     'regel': 'Eliminiere mit zwei Gleichungspaaren ⟦dieselbe Variable⟧. So entsteht ein System mit ⟦zwei Unbekannten⟧. Löse es und setze zurück ein.',
     'schritte': ['(I) x + y + z = 2; (II) x − y + z = 6; (III) 2x + y − z = −3. (I) − (II): 2y = −4 ⇒ y = −2.',
                  '(I) + (III): 3x + 2y = −1 ⇒ 3x − 4 = −1 ⇒ x = 1. Aus (I): 1 − 2 + z = 2 ⇒ ⟦x = 1, y = −2, z = 3⟧.'],
     'probe': '(II) 1 + 2 + 3 = 6 ✓; (III) 2 − 2 − 3 = −3 ✓',
     'fehler': 'Mit (I) und (II) x zu eliminieren, mit (II) und (III) aber y, führt nicht weiter: Beide neuen Gleichungen müssen ⟦dieselbe Variable⟧ verlieren.'},
    {'lernziel': 'parabel', 'titel': 'Parabel durch drei Punkte',
     'regel': 'Setze jeden Punkt (x | y) in ⟦y = ax² + bx + c⟧ ein. Das ergibt drei Gleichungen für ⟦a, b und c⟧.',
     'schritte': ['Punkte (0 | 1), (1 | 2), (−1 | 4): Aus (0 | 1) folgt c = 1.',
                  'a + b + 1 = 2 und a − b + 1 = 4 ⇒ 2a = 4 ⇒ a = 2, b = −1: ⟦y = 2x² − x + 1⟧.'],
     'probe': 'x = −1: 2 · 1 + 1 + 1 = 4 ✓',
     'bild': {'typ': 'koordinaten', 'x': [-2, 2], 'y': [0, 8], 'graphen': [{'art': 'poly', 'k': [1, -1, 2], 'name': 'y = 2x² − x + 1'}], 'punkte': [{'x': 0, 'y': 1, 'name': '(0 | 1)'}, {'x': 1, 'y': 2, 'name': '(1 | 2)'}, {'x': -1, 'y': 4, 'name': '(−1 | 4)'}]},
     'fehler': 'Den Punkt (−1 | 4) als a − b + c = −4 einzusetzen ist falsch: Der ⟦y-Wert⟧ steht rechts, (−1)² = ⟦+1⟧, also a − b + c = 4.'},
    {'lernziel': 'sachaufgabe', 'titel': 'Sachaufgaben mit drei Unbekannten',
     'regel': 'Lege ⟦drei Variablen⟧ fest, übersetze jede Angabe in eine Gleichung und löse das System. Antworte im ⟦Sachzusammenhang⟧.',
     'schritte': ['Drei Zahlen: Summe 12, die zweite ist doppelt so groß wie die erste, die dritte ist um 4 größer als die erste.',
                  'x + y + z = 12, y = 2x, z = x + 4 ⇒ 4x + 4 = 12 ⇒ ⟦x = 2, y = 4, z = 6⟧.'],
     'probe': '2 + 4 + 6 = 12 ✓',
     'fehler': '„Doppelt so groß wie die erste“ als x = 2y zu schreiben ist falsch: Die ⟦zweite⟧ Zahl ist das Doppelte, also y = 2x.'},
]

# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'pruefen': {
  'einstieg': 'Am Kiosk kosten ein Brötchen, ein Saft und ein Stück Kuchen zusammen 6 €. Der Saft kostet doppelt so viel wie das Brötchen, der Kuchen 2 € mehr als das Brötchen. Ein Freund behauptet: „1 €, 2 € und 3 €.“ Stimmt das? Es muss zu allen drei Angaben passen. Drei solche Gleichungen zusammen heißen ⟦lineares Gleichungssystem (LGS) mit drei Unbekannten⟧.',
  'woerter': [['x, y, z', 'die drei gesuchten Zahlen, hier die Preise von Brötchen, Saft und Kuchen in €'],
              ['(I), (II), (III)', 'Nummern für die erste, zweite und dritte Gleichung'],
              ['linear', 'x, y und z kommen nur ohne Hochzahl vor'],
              ['Zahlentripel (1 | 2 | 3)', 'drei Zahlen in fester Reihenfolge: x = 1, y = 2, z = 3'],
              ['Lösung des Systems', 'ein Tripel, das alle Gleichungen zugleich erfüllt']],
  'schritte': ['Das System: (I) x + y + z = 6; (II) 2x − y = 0; (III) x − z = −2. Zu prüfen ist (1 | 2 | 3).',
               'In (I) einsetzen: 1 + 2 + 3 = 6. Stimmt.',
               'In (II) einsetzen: 2 · 1 − 2 = 0. Stimmt.',
               'In (III) einsetzen: 1 − 3 = −2. Stimmt. Alle drei passen, also ist ⟦(1 | 2 | 3) eine Lösung⟧.'],
  'regel': 'So prüfst du ein ⟦Zahlentripel⟧: Setze x, y und z in ⟦jede⟧ Gleichung ein. Nur wenn ⟦alle drei⟧ stimmen, ist es eine Lösung des Systems.',
  'fehler': 'Nur Gleichung (I) zu prüfen genügt nicht: (2 | 2 | 2) ergibt zwar zusammen 6 €, aber in (II) kommt 2 · 2 − 2 = 2 heraus, nicht 0 – der Saft wäre nicht doppelt so teuer. Es müssen ⟦alle⟧ Gleichungen stimmen.'},
 'stufenform': {
  'einstieg': 'Bei einem anderen Einkauf sind die Angaben schon günstig sortiert: Eine Angabe nennt nur den Kuchenpreis, die nächste Saft und Kuchen, die letzte alle drei. Man beginnt bei der Angabe mit nur einem Preis und arbeitet sich nach oben vor – wie eine Treppe. Diese Anordnung heißt ⟦Stufenform⟧.',
  'woerter': [['Stufenform', 'jede Gleichung weiter unten hat eine Unbekannte weniger'],
              ['einsetzen', 'eine schon bekannte Zahl statt des Buchstabens schreiben'],
              ['von unten nach oben', 'mit der letzten Gleichung anfangen']],
  'schritte': ['Das System: (I) x + y − z = 1; (II) y + z = 5; (III) 2z = 6.',
               'Unten anfangen: Aus (III) 2z = 6 folgt z = 3.',
               'z = 3 in (II) einsetzen: y + 3 = 5, also y = 2.',
               'y = 2 und z = 3 in (I) einsetzen: x + 2 − 3 = 1, also x = 2. Lösung: ⟦x = 2, y = 2, z = 3⟧.'],
  'regel': 'So löst du ein System in ⟦Stufenform⟧: Löse die letzte Gleichung, die nur noch eine Unbekannte hat. Setze das Ergebnis ⟦von unten nach oben⟧ in die anderen Gleichungen ein.',
  'fehler': 'In (II) y + z = 5 mit z = 3 auf y = 8 zu kommen ist falsch: Die 3 wird ⟦abgezogen⟧, nicht addiert: y = 5 − 3 = 2. Probe: 8 + 3 = 11, nicht 5.'},
 'eliminieren': {
  'einstieg': 'Zwei Kassenzettel: Auf dem zweiten stehen genau doppelt so viele Brötchen wie auf dem ersten. Verdoppelt man den ersten Zettel und zieht ihn vom zweiten ab, fallen die Brötchen weg. Übrig bleibt eine Angabe nur über Saft und Kuchen. Eine Unbekannte so verschwinden zu lassen heißt ⟦eliminieren⟧.',
  'woerter': [['eliminieren', 'eine Unbekannte durch geschicktes Rechnen wegfallen lassen'],
              ['Additionsverfahren', 'Gleichungen (oder ihre Vielfachen) addieren oder abziehen'],
              ['(II) − 2 · (I)', 'Gleichung (I) mal 2 nehmen und von Gleichung (II) abziehen'],
              ['Glied', 'ein Teil einer Summe, z. B. 2y oder −z']],
  'schritte': ['Gegeben: (I) x + 2y − z = 3; (II) 2x − y + z = 4. In (II) steht 2x, in (I) nur x.',
               'Gleichung (I) mal 2, und zwar jedes Glied: 2x + 4y − 2z = 6.',
               'Das von (II) abziehen, Glied für Glied: 2x − 2x = 0, −y − 4y = −5y, z − (−2z) = 3z, 4 − 6 = −2.',
               'Ergebnis: ⟦−5y + 3z = −2⟧. Das x ist weggefallen.'],
  'regel': 'So eliminierst du mit dem ⟦Additionsverfahren⟧: Nimm eine Gleichung so oft mal, dass vor der Unbekannten dieselbe Zahl steht. Dann addieren oder abziehen, sodass die ⟦Unbekannte wegfällt⟧. Die ⟦rechte Seite⟧ wird immer mitgerechnet.',
  'fehler': 'Bei (II) − 2 · (I) nur die x-Glieder zu verdoppeln ist falsch: ⟦Jedes Glied⟧ von (I), auch die rechte Seite, wird mit 2 multipliziert – sonst würde man den Kassenzettel nur halb verdoppeln.'},
 'loesen': {
  'einstieg': 'Jetzt werden alle Werkzeuge zusammengesetzt. Aus drei Angaben mit drei Unbekannten macht man durch Eliminieren zwei Angaben mit zwei Unbekannten. Daraus wird eine Angabe mit einer Unbekannten. Rückwärts eingesetzt ergeben sich alle drei Werte. So wird das ⟦LGS gelöst⟧.',
  'woerter': [['dieselbe Variable', 'in beiden neuen Gleichungen muss die gleiche Unbekannte wegfallen'],
              ['(I) − (II)', 'Gleichung (II) von Gleichung (I) abziehen'],
              ['(I) + (III)', 'Gleichung (I) und Gleichung (III) addieren']],
  'schritte': ['Das System: (I) x + y + z = 2; (II) x − y + z = 6; (III) 2x + y − z = −3.',
               '(I) − (II): x und z fallen weg, es bleibt 2y = −4, also y = −2.',
               '(I) + (III): z fällt weg, es bleibt 3x + 2y = −1. Mit y = −2: 3x − 4 = −1, also x = 1.',
               'In (I) einsetzen: 1 + (−2) + z = 2, also z = 3. Lösung: ⟦x = 1, y = −2, z = 3⟧.'],
  'regel': 'So löst du ein LGS mit drei Unbekannten: Eliminiere mit zwei verschiedenen Gleichungspaaren ⟦dieselbe Unbekannte⟧. So entsteht ein System mit ⟦zwei Unbekannten⟧. Löse es und setze die Werte zurück ein. Zum Schluss die Probe in allen drei Gleichungen.',
  'fehler': 'Mit (I) und (II) x zu eliminieren, mit (II) und (III) aber y, führt nicht weiter: Dann hat jede neue Gleichung wieder andere Unbekannte. Beide neuen Gleichungen müssen ⟦dieselbe Unbekannte⟧ verlieren.'},
 'parabel': {
  'einstieg': 'Ein Ball fliegt in einem Bogen. Drei Punkte seiner Flugbahn sind gemessen. Die Bahn ist eine Parabel mit der Form y = ax² + bx + c, nur a, b und c sind unbekannt. Jeder Punkt liefert eine Gleichung – zusammen ein LGS. So findet man die ⟦Parabel durch drei Punkte⟧.',
  'woerter': [['Parabel', 'die Kurve zu y = ax² + bx + c'],
              ['a, b, c', 'die drei unbekannten Zahlen der Parabel'],
              ['Punkt (1 | 2)', 'x = 1 und y = 2'],
              ['(−1)²', '(−1) · (−1) = 1']],
  'bild': {'typ': 'koordinaten', 'x': [-2, 2], 'y': [0, 8], 'graphen': [{'art': 'poly', 'k': [1, -1, 2], 'name': 'Flugbahn y = 2x² − x + 1'}], 'punkte': [{'x': 0, 'y': 1, 'name': 'Messpunkt (0 | 1)'}, {'x': 1, 'y': 2, 'name': 'Messpunkt (1 | 2)'}, {'x': -1, 'y': 4, 'name': 'Messpunkt (−1 | 4)'}]},
  'schritte': ['Die Punkte sind (0 | 1), (1 | 2) und (−1 | 4). Jeder wird in y = ax² + bx + c eingesetzt.',
               '(0 | 1): a · 0 + b · 0 + c = 1, also c = 1.',
               '(1 | 2): a + b + 1 = 2, also a + b = 1. (−1 | 4): a − b + 1 = 4, also a − b = 3.',
               'Beide Gleichungen addieren: 2a = 4, also a = 2 und b = −1. Die Parabel: ⟦y = 2x² − x + 1⟧.'],
  'regel': 'So findest du die Parabel: Setze jeden Punkt (x | y) in ⟦y = ax² + bx + c⟧ ein. Das ergibt drei Gleichungen für ⟦a, b und c⟧. Löse dieses LGS.',
  'fehler': 'Den Punkt (−1 | 4) als a − b + c = −4 einzusetzen ist falsch: Der ⟦y-Wert⟧ 4 steht rechts, und (−1)² = ⟦+1⟧, also a − b + c = 4. Sonst läge der Messpunkt unter der x-Achse.'},
 'sachaufgabe': {
  'einstieg': 'Drei Geschwister teilen 12 Bonbons. Das zweite bekommt doppelt so viele wie das erste, das dritte 4 mehr als das erste. Wie viele bekommt jedes? Jede Angabe wird zu einer Gleichung. Solche Probleme aus dem Alltag heißen ⟦Sachaufgaben⟧.',
  'woerter': [['Variablen festlegen', 'sagen, wofür x, y und z stehen'],
              ['„doppelt so viele wie das erste“', 'y = 2x'],
              ['„4 mehr als das erste“', 'z = x + 4'],
              ['Sachzusammenhang', 'die Situation, zu der die Lösung passen muss']],
  'schritte': ['Variablen festlegen: x, y und z sind die Bonbons des ersten, zweiten und dritten Kindes.',
               'Angaben übersetzen: x + y + z = 12, y = 2x und z = x + 4.',
               'y und z in die erste Gleichung einsetzen: x + 2x + x + 4 = 12, also 4x + 4 = 12 und x = 2.',
               'Zurück einsetzen: y = 4 und z = 6. Antwort: ⟦2, 4 und 6 Bonbons⟧.'],
  'regel': 'So löst du eine Sachaufgabe: Lege ⟦drei Variablen⟧ fest, übersetze jede Angabe in eine Gleichung und löse das System. Antworte in einem Satz im ⟦Sachzusammenhang⟧.',
  'fehler': '„Doppelt so viele wie das erste“ als x = 2y zu schreiben ist falsch: Das ⟦zweite⟧ Kind bekommt das Doppelte, also y = 2x. Probe: Mit x = 2y bekäme das erste Kind mehr.'},
}
klar(ETAPPEN, KLAR)
# ---- KLAR ENDE ----
# ---- UMBAU (neues Muster, Runde 8, Vorgabe 16.11.) ----
_K = ['', 'x', 'y', 'z', 'rechts']
UMBAU = {
 'pruefen': {
  'einstieg': 'Brötchen, Saft und Kuchen kosten zusammen 6 €. Der Saft kostet doppelt so viel wie das Brötchen, der Kuchen 2 € mehr. Das ergibt ein ⟦lineares Gleichungssystem⟧.',
  'woerter': [['lineares Gleichungssystem', 'mehrere Gleichungen, die zugleich gelten; x, y, z ohne Hochzahl'],
              ['Zahlentripel', 'drei Zahlen in fester Reihenfolge: (1 | 2 | 3) heißt x = 1, y = 2, z = 3']],
  'bild': {'typ': 'tabelle', 'kopf': ['Gleichung', 'eingesetzt', 'stimmt?'],
           'zeilen': [['(I) x + y + z = 6', '?', '?'], ['(II) 2x − y = 0', '?', '?'], ['(III) x − z = −2', '?', '?']]},
  'schritte': [{'text': 'Prüfe das Zahlentripel (1 | 2 | 3) in jeder Gleichung.'},
               {'text': '(I): 1 + 2 + 3 = 6 stimmt.',
                'bild': {'zeilen': [['(I) x + y + z = 6', '1 + 2 + 3 = 6', 'ja'], ['(II) 2x − y = 0', '?', '?'], ['(III) x − z = −2', '?', '?']]}},
               {'text': '(II): 2 · 1 − 2 = 0 stimmt.',
                'bild': {'zeilen': [['(I) x + y + z = 6', '1 + 2 + 3 = 6', 'ja'], ['(II) 2x − y = 0', '2 − 2 = 0', 'ja'], ['(III) x − z = −2', '?', '?']]}},
               {'text': '(III): 1 − 3 = −2 stimmt.',
                'bild': {'zeilen': [['(I) x + y + z = 6', '1 + 2 + 3 = 6', 'ja'], ['(II) 2x − y = 0', '2 − 2 = 0', 'ja'], ['(III) x − z = −2', '1 − 3 = −2', 'ja']]}},
               {'text': 'Alle drei passen: ⟦(1 | 2 | 3) ist eine Lösung⟧.'}],
  'fehler': 'Nur (I) prüfen genügt nicht. (2 | 2 | 2) ergibt zwar 6 €, aber der Saft wäre nicht doppelt so teuer.',
  'fehler_bild': {'zeilen': [['(I) x + y + z = 6', '2 + 2 + 2 = 6', 'ja'], ['(II) 2x − y = 0', '4 − 2 = 2', 'nein'], ['(III) x − z = −2', '2 − 2 = 0', 'nein']]},
  'regel': 'Ein Tripel ist Lösung, wenn ⟦alle drei Gleichungen⟧ stimmen. Setze darum in jede Gleichung ein.'},
 'stufenform': {
  'einstieg': 'Bei einem anderen Einkauf nennt eine Angabe nur den Kuchenpreis. Von dort arbeitest du dich wie auf einer Treppe nach oben. Diese Anordnung heißt ⟦Stufenform⟧.',
  'woerter': [['Stufenform', 'jede Gleichung weiter unten hat eine Unbekannte weniger'],
              ['einsetzen', 'eine schon bekannte Zahl statt des Buchstabens schreiben']],
  'bild': {'typ': 'tabelle', 'kopf': ['Gleichung', 'ergibt'],
           'zeilen': [['(I) x + y − z = 1', '?'], ['(II) y + z = 5', '?'], ['(III) 2z = 6', '?']]},
  'schritte': [{'text': 'Unten anfangen: 2z = 6, also z = 3.',
                'bild': {'zeilen': [['(I) x + y − z = 1', '?'], ['(II) y + z = 5', '?'], ['(III) 2z = 6', 'z = 3']]}},
               {'text': 'z = 3 einsetzen in y + z = 5: y = 2.',
                'bild': {'zeilen': [['(I) x + y − z = 1', '?'], ['(II) y + z = 5', 'y = 2'], ['(III) 2z = 6', 'z = 3']]}},
               {'text': 'In (I): x + 2 − 3 = 1, also x = 2.',
                'bild': {'zeilen': [['(I) x + y − z = 1', 'x = 2'], ['(II) y + z = 5', 'y = 2'], ['(III) 2z = 6', 'z = 3']]}},
               {'text': 'Die Lösung: ⟦x = 2, y = 2, z = 3⟧.'}],
  'fehler': 'y + 3 = 5 ergibt nicht y = 8. Die 3 wird abgezogen: y = 5 − 3 = 2.',
  'fehler_bild': {'zeilen': [['(I) x + y − z = 1', '?'], ['(II) y + z = 5', 'y = 8? falsch'], ['(III) 2z = 6', 'z = 3']]},
  'regel': 'Löse die ⟦unterste Gleichung⟧ zuerst. Setze dann von unten nach oben ein.'},
 'eliminieren': {
  'einstieg': 'Auf Kassenzettel 2 stehen doppelt so viele Brötchen wie auf Zettel 1. Verdoppelst du Zettel 1 und ziehst ihn ab, fallen die Brötchen weg. Das heißt ⟦eliminieren⟧.',
  'woerter': [['eliminieren', 'eine Unbekannte durch Rechnen wegfallen lassen'],
              ['Additionsverfahren', 'Gleichungen oder ihre Vielfachen addieren oder abziehen'],
              ['Glied', 'ein Teil einer Summe, z. B. 2y oder −z']],
  'bild': {'typ': 'tabelle', 'kopf': _K, 'zeilen': [['(I)', '1', '2', '−1', '3'], ['(II)', '2', '−1', '1', '4']]},
  'schritte': [{'text': 'In (II) steht 2x, in (I) nur x.'},
               {'text': '(I) mal 2, und zwar jedes Glied: 2x + 4y − 2z = 6.',
                'bild': {'zeilen': [['(I)', '1', '2', '−1', '3'], ['(II)', '2', '−1', '1', '4'], ['2 · (I)', '2', '4', '−2', '6']]}},
               {'text': 'Additionsverfahren: (II) − 2 · (I), Spalte für Spalte.',
                'bild': {'zeilen': [['(I)', '1', '2', '−1', '3'], ['(II)', '2', '−1', '1', '4'], ['2 · (I)', '2', '4', '−2', '6'], ['(II) − 2 · (I)', '0', '−5', '3', '−2']]}},
               {'text': 'Das x fällt weg: ⟦−5y + 3z = −2⟧.'}],
  'fehler': 'Nur die x-Glieder zu verdoppeln ist falsch. Jedes Glied von (I), auch die rechte Seite, wird mal 2 genommen.',
  'fehler_bild': {'zeilen': [['(I)', '1', '2', '−1', '3'], ['(II)', '2', '−1', '1', '4'], ['2 · (I)?', '2', '2', '−1', '3']]},
  'regel': 'Vervielfache eine Gleichung so, dass beim Abziehen eine Unbekannte ⟦wegfällt⟧. Die rechte Seite rechnest du immer mit.'},
 'loesen': {
  'einstieg': 'Drei Angaben mit drei Unbekannten sind viel. Durch Eliminieren werden es zwei, dann eine. Rückwärts eingesetzt hast du alle Werte: Das ⟦LGS⟧ ist gelöst.',
  'woerter': [['LGS', 'kurz für lineares Gleichungssystem'],
              ['(I) − (II)', 'Gleichung (II) von Gleichung (I) abziehen']],
  'bild': {'typ': 'tabelle', 'kopf': _K, 'zeilen': [['(I)', '1', '1', '1', '2'], ['(II)', '1', '−1', '1', '6'], ['(III)', '2', '1', '−1', '−3']]},
  'schritte': [{'text': '(I) − (II): x und z fallen weg, 2y = −4, also y = −2.',
                'bild': {'zeilen': [['(I)', '1', '1', '1', '2'], ['(II)', '1', '−1', '1', '6'], ['(III)', '2', '1', '−1', '−3'], ['(I) − (II)', '0', '2', '0', '−4']]}},
               {'text': '(I) + (III): z fällt weg, es bleibt 3x + 2y = −1.',
                'bild': {'zeilen': [['(I)', '1', '1', '1', '2'], ['(II)', '1', '−1', '1', '6'], ['(III)', '2', '1', '−1', '−3'], ['(I) − (II)', '0', '2', '0', '−4'], ['(I) + (III)', '3', '2', '0', '−1']]}},
               {'text': 'Mit y = −2: 3x − 4 = −1, also x = 1.'},
               {'text': 'In (I): 1 − 2 + z = 2. Lösung: ⟦(1 | −2 | 3)⟧.'},
               # Fünfzehnte Runde: Sonderfälle keine / unendlich viele Lösungen (passend zu den Stufe-3-Aufgaben)
               {'text': 'Kommt 0 = −5 heraus: ⟦keine⟧ Lösung. Bei 0 = 0: unendlich viele.',
                'bild': {'zeilen': [['(I)', '1', '1', '1', '1'], ['(II)', '1', '1', '1', '6'], ['(I) − (II)', '0', '0', '0', '−5']]}}],
  'fehler': 'Einmal x und einmal y zu eliminieren führt nicht weiter. Dann haben die neuen Gleichungen wieder verschiedene Unbekannte.',
  'regel': 'Eliminiere zweimal ⟦dieselbe Unbekannte⟧. Löse das kleinere System und setze zurück ein.'},
 'parabel': {
  'einstieg': 'Drei Punkte einer Ballflugbahn sind gemessen. Die Bahn ist eine Parabel y = ax² + bx + c. Jeder Punkt liefert eine Gleichung: So findest du die ⟦Parabel durch drei Punkte⟧.',
  'woerter': [['Parabel', 'die Kurve zu y = ax² + bx + c'],
              ['a, b und c', 'die drei unbekannten Zahlen der Parabel']],
  'bild': {'typ': 'koordinaten', 'x': [-2, 2], 'y': [-5, 8],
           'punkte': [{'x': 0, 'y': 1, 'name': '(0 | 1)'}, {'x': 1, 'y': 2, 'name': '(1 | 2)'}, {'x': -1, 'y': 4, 'name': '(−1 | 4)'}]},
  'schritte': [{'text': 'Gesucht sind a, b und c. Aus (0 | 1) folgt c = 1.'},
               {'text': 'Aus (1 | 2) folgt a + b + 1 = 2.'},
               {'text': 'Aus (−1 | 4) folgt a − b + 1 = 4.'},
               {'text': 'Addieren: 2a + 2 = 6, also a = 2 und b = −1.'},
               {'text': 'Die Flugbahn: ⟦y = 2x² − x + 1⟧.',
                'bild': {'graphen': [{'art': 'poly', 'k': [1, -1, 2], 'name': 'Flugbahn'}]}}],
  'fehler': '(−1 | 4) ergibt nicht a − b + c = −4. Der y-Wert 4 steht rechts, und (−1)² ist +1.',
  'fehler_bild': {'punkte': [{'x': 0, 'y': 1, 'name': '(0 | 1)'}, {'x': 1, 'y': 2, 'name': '(1 | 2)'}, {'x': -1, 'y': 4, 'name': '(−1 | 4)'},
                             {'x': -1, 'y': -4, 'name': 'nicht −4', 'offen': True}]},
  'regel': 'Setze jeden Punkt in ⟦y = ax² + bx + c⟧ ein. Löse dann das LGS für a, b und c.'},
 'sachaufgabe': {
  'einstieg': 'Drei Geschwister teilen 12 Bonbons. Das zweite bekommt doppelt so viele wie das erste, das dritte 4 mehr. Jede Angabe wird eine Gleichung: eine ⟦Sachaufgabe⟧.',
  'woerter': [['Sachaufgabe', 'eine Rechenaufgabe aus dem Alltag'],
              ['Variablen', 'Buchstaben für die gesuchten Zahlen'],
              ['Sachzusammenhang', 'die Situation, zu der die Lösung passen muss']],
  'bild': {'typ': 'tabelle', 'kopf': ['Kind', '1.', '2.', '3.'], 'zeilen': [['Bonbons', 'x', 'y', 'z']]},
  'schritte': [{'text': 'Variablen: x, y, z sind die Bonbons des 1., 2. und 3. Kindes.'},
               {'text': 'Zusammen 12: x + y + z = 12.'},
               {'text': 'Dazu y = 2x und z = x + 4.', 'bild': {'zeilen': [['Bonbons', 'x', '2x', 'x + 4']]}},
               {'text': 'Einsetzen: x + 2x + x + 4 = 12, also x = 2.'},
               {'text': 'Antwort: ⟦2, 4 und 6 Bonbons⟧. Das passt zum Sachzusammenhang.',
                'bild': {'zeilen': [['Bonbons', '2', '4', '6']]}}],
  'fehler': '„Doppelt so viele wie das erste“ heißt nicht x = 2y. Das zweite Kind bekommt das Doppelte: y = 2x.',
  'regel': 'Lege ⟦drei Variablen⟧ fest und übersetze jede Angabe. Löse das LGS und antworte im Sachzusammenhang.'},
}
umbau(ETAPPEN, UMBAU)
# ---- UMBAU ENDE ----


def g_pruefen(s):
    M, b, x = zufall_lgs()
    if s == 1:
        i = R.randrange(3)
        lhs = sum(M[i][k] * x[k] for k in range(3))
        return zahl(f'Setze (x | y | z) = ({dz(x[0])} | {dz(x[1])} | {dz(x[2])}) in die linke Seite von {lin(M[i], b[i])} ein. Welcher Wert ergibt sich?',
                    f'{" + ".join(f"{kl(M[i][k])} · {kl(x[k])}" for k in range(3))} = {dz(lhs)}.',
                    'Ersetze x, y und z durch die Zahlen und achte auf die Vorzeichen.', lhs,
                    ' + '.join(f'({M[i][k]}) * ({x[k]})' for k in range(3)))
    falsch = R.random() < 0.65
    t = list(x)
    if falsch:
        k = R.randrange(3)  # diese Gleichung wird verletzt, die anderen beiden bleiben erfüllt
        i1, i2 = [i for i in range(3) if i != k]
        d = kreuz(M[i1], M[i2])
        if max(abs(c) for c in d) > 5: return None
        f = R.choice([-1, 1])
        t = [x[q] + f * d[q] for q in range(3)]
    erf = [sum(M[i][q] * t[q] for q in range(3)) == b[i] for i in range(3)]
    if falsch: assert erf.count(False) == 1
    if falsch:
        nr = erf.index(False)
        lhs = sum(M[nr][q] * t[q] for q in range(3))
        richtig = f'Nein, Gleichung ({NR[nr]}) ist nicht erfüllt ({dz(lhs)} ≠ {dz(b[nr])}).'
        andere = ['Ja, alle drei Gleichungen sind erfüllt.'] + [f'Nein, Gleichung ({n}) ist nicht erfüllt.' for n in NR if n != NR[nr]]
    else:
        richtig = 'Ja, alle drei Gleichungen sind erfüllt.'
        andere = [f'Nein, Gleichung ({n}) ist nicht erfüllt.' for n in NR]
    w = 'Einsetzen: ' + '; '.join(f'({NR[i]}) {dz(sum(M[i][q] * t[q] for q in range(3)))} {"=" if erf[i] else "≠"} {dz(b[i])}' for i in range(3))
    return auswahl(f'Ist ({dz(t[0])} | {dz(t[1])} | {dz(t[2])}) Lösung des Systems {system(M, b)}?', richtig, andere, w,
                   'Setze das Tripel in jede Gleichung ein – auch die letzte.')


def g_stufenform(s):
    x = [R.randint(-6, 6) for _ in range(3)]
    if s == 1:
        a, d, h = 1, 1, R.randint(1, 4)
        bb, cc, f = R.randint(-3, 3), R.randint(-3, 3), R.randint(-3, 3)
    else:
        a, d, h = R.randint(1, 4), R.randint(1, 3), R.randint(1, 5) * R.choice([1, -1])
        bb, cc, f = R.randint(-4, 4), R.randint(-4, 4), R.randint(-4, 4)
    M = [[a, bb, cc], [0, d, f], [0, 0, h]]
    b = [sum(M[i][k] * x[k] for k in range(3)) for i in range(3)]
    if s == 3:
        text = f'Löse das System: (I) {lin([0, 0, h], b[2])}; (II) {lin([a, bb, cc], b[0])}; (III) {lin([0, d, f], b[1])}.'
        M_ = [[0, 0, h], [a, bb, cc], [0, d, f]]
        b_ = [b[2], b[0], b[1]]
        return luecken(text, LX, 'Werte von x, y, z', x,
                       f'Aus {lin([0, 0, h], b[2])}: z = {dz(x[2])}. Dann {lin([0, d, f], b[1])}: y = {dz(x[1])}. Dann x = {dz(x[0])}.',
                       'Suche die Gleichung mit nur einer Variablen und arbeite dich weiter.', c=cramer_c(M_, b_))
    return bild(luecken(f'Löse das System in Stufenform: {system(M, b)}.', LX, 'Werte von x, y, z', x,
                   f'(III) z = {dz(b[2])} : {kl(h)} = {dz(x[2])}; (II) y = {dz(x[1])}; (I) x = {dz(x[0])}.',
                   'Beginne mit (III) und setze nach oben ein.', c=cramer_c(M, b)), tab(M, b))


def g_eliminieren(s):
    M, b, x = zufall_lgs(gr=4 if s > 1 else 3)
    if s == 3 and R.random() < 0.4:
        r1, r2 = M[0], M[1]
        v = R.randrange(3)
        p_, q_ = r1[v], r2[v]
        if p_ == 0 or q_ == 0 or abs(p_) == abs(q_): return None
        from math import gcd
        g = gcd(abs(p_), abs(q_))
        f1, f2 = q_ // g, p_ // g  # f1·(I) − f2·(II) eliminiert v
        if f1 < 0: f1, f2 = -f1, -f2
        neu = [f1 * r1[t] - f2 * r2[t] for t in range(3)] + [f1 * b[0] - f2 * b[1]]
        assert neu[v] == 0
        def kombi(a_, b2):
            t1 = '(I)' if a_ == 1 else f'{a_} · (I)'
            return f'{t1} {"−" if b2 > 0 else "+"} {"" if abs(b2) == 1 else str(abs(b2)) + " · "}(II)'
        richtig = kombi(f1, f2)
        falsch = [kombi(f1, -f2), '(I) − (II)' if richtig != '(I) − (II)' else '(I) + (II)', kombi(f2 if f2 > 0 else -f2, f1 if f2 > 0 else -f1)]
        return auswahl(f'(I) {lin(r1, b[0])}; (II) {lin(r2, b[1])}. Welche Rechnung eliminiert {V[v]}?', richtig, falsch,
                       f'Die {V[v]}-Koeffizienten sind {dz(p_)} und {dz(q_)}. {richtig} ergibt {lin(neu[:3], neu[3])} – {V[v]} fällt weg.',
                       f'Mache die {V[v]}-Koeffizienten durch Vervielfachen gleich groß und subtrahiere (bzw. addiere).')
    i, j = sorted(R.sample(range(3), 2))
    a1, a2 = M[i][0], M[j][0]
    if a1 == 0 or a2 == 0: return None
    if s == 1:
        if a1 != a2 and a1 != -a2: return None
        k = 1 if a1 == a2 else -1
        op = '−' if k == 1 else '+'
        neu = [M[j][t] - k * M[i][t] for t in range(3)] + [b[j] - k * b[i]]
        anw = f'({NR[j]}) {op} ({NR[i]})'
    else:
        if a2 % a1 == 0:
            k = a2 // a1
            neu = [M[j][t] - k * M[i][t] for t in range(3)] + [b[j] - k * b[i]]
            anw = (f'({NR[j]}) − ({NR[i]})' if k == 1 else f'({NR[j]}) + ({NR[i]})' if k == -1 else
                   f'({NR[j]}) − {k} · ({NR[i]})' if k > 0 else f'({NR[j]}) + {-k} · ({NR[i]})')
        else:
            if a1 < 0: a1, a2 = -a1, -a2
            neu = [a1 * M[j][t] - a2 * M[i][t] for t in range(3)] + [a1 * b[j] - a2 * b[i]]
            f1 = '' if a1 == 1 else f'{a1} · '
            f2 = '' if abs(a2) == 1 else f'{abs(a2)} · '
            anw = f'{f1}({NR[j]}) {"−" if a2 > 0 else "+"} {f2}({NR[i]})'
            k = None
    assert neu[0] == 0
    if s == 3 and R.random() < 0.5:
        k2 = a2 // a1 if a2 % a1 == 0 else None
        if k2 is None or k2 in (0, 1, -1): return None
        falsch_rechts = b[j] - b[i]
        if falsch_rechts == neu[3]: return None
        return auswahl(f'Gegeben: ({NR[i]}) {lin(M[i], b[i])}; ({NR[j]}) {lin(M[j], b[j])}. Jemand berechnet ({NR[j]}) − {kl(k2)} · ({NR[i]}) und erhält {lin(neu[:3], falsch_rechts)}. Was stimmt?',
                       f'Falsch: Die rechte Seite muss {dz(b[j])} − {kl(k2)} · {kl(b[i])} = {dz(neu[3])} sein.',
                       ['Richtig, das ist die neue Gleichung.', f'Falsch: Das x hätte stehen bleiben müssen.',
                        f'Falsch: Die rechte Seite muss {dz(b[j] + b[i])} sein.'],
                       f'Auch die rechte Seite von ({NR[i]}) wird mit {kl(k2)} multipliziert: {dz(b[j])} − {kl(k2 * b[i])} = {dz(neu[3])}.',
                       'Wurde jedes Glied mit dem Faktor multipliziert?')
    return luecken(f'Gegeben: ({NR[i]}) {lin(M[i], b[i])}; ({NR[j]}) {lin(M[j], b[j])}. Berechne {anw}.', '□y + □z = □',
                   'Koeffizient von y, von z, rechte Seite (mit Vorzeichen)', neu[1:],
                   f'{anw}: x fällt weg, es bleibt {lin([0] + neu[1:3], neu[3])}.',
                   'Rechne Glied für Glied, auch auf der rechten Seite.',
                   c=([f'({M[j][t]}) - ({k}) * ({M[i][t]})' for t in (1, 2)] + [f'({b[j]}) - ({k}) * ({b[i]})'] if k is not None else
                      [f'({a1}) * ({M[j][t]}) - ({a2}) * ({M[i][t]})' for t in (1, 2)] + [f'({a1}) * ({b[j]}) - ({a2}) * ({b[i]})']))


def g_loesen(s):
    if s == 3 and R.random() < 0.3:
        while True:
            r1 = [R.randint(-3, 3) for _ in range(3)]
            r2 = [R.randint(-3, 3) for _ in range(3)]
            if all(r1) and all(r2) and kreuz(r1, r2) != [0, 0, 0]: break
        p_, q_ = R.choice([(1, 1), (1, -1), (2, 1), (1, 2)])
        x = [R.randint(-4, 4) for _ in range(3)]
        b1, b2 = sum(r1[k] * x[k] for k in range(3)), sum(r2[k] * x[k] for k in range(3))
        r3 = [p_ * r1[k] + q_ * r2[k] for k in range(3)]
        if not any(r3): return None
        art = R.choice(['keine', 'unendlich'])
        b3 = p_ * b1 + q_ * b2 + (0 if art == 'unendlich' else R.choice([-3, -2, -1, 1, 2, 3]))
        komb = ('(I)' if p_ == 1 else f'{p_} · (I)') + (' + ' if q_ > 0 else ' − ') + ('(II)' if abs(q_) == 1 else f'{abs(q_)} · (II)')
        rich = 'keine Lösung' if art == 'keine' else 'unendlich viele Lösungen'
        M, b = [r1, r2, r3], [b1, b2, b3]
        return bild(auswahl(f'Wie viele Lösungen hat das System {system(M, b)}?', rich,
                            ['genau eine Lösung', 'keine Lösung', 'unendlich viele Lösungen'],
                            f'{komb} ergibt {lin(r3, p_ * b1 + q_ * b2)}. (III) hat dieselbe linke Seite und rechts {dz(b3)}: '
                            + ('Widerspruch, also keine Lösung.' if art == 'keine' else 'dieselbe Gleichung – (III) bringt nichts Neues, also unendlich viele Lösungen.'),
                            'Vergleiche (III) mit einer Kombination aus (I) und (II).'), tab(M, b))
    gr, lsg = {1: (1, 5), 2: (2, 6), 3: (3, 8)}[s]
    M, b, x = zufall_lgs(gr=gr, lsg=lsg)
    if s == 1 and not any(0 in row for row in M): return None
    if s == 1 and sum(1 for row in M for c in row if c == 0) > 3: return None
    if s == 3 and any(0 in row for row in M): return None
    return bild(luecken(f'Löse das Gleichungssystem: {system(M, b)}.', LX, 'Werte von x, y, z', x,
                        f'Eliminieren und Einsetzen ergibt x = {dz(x[0])}, y = {dz(x[1])}, z = {dz(x[2])}. Probe in allen drei Gleichungen.',
                        'Eliminiere mit zwei Gleichungspaaren dieselbe Variable.', c=cramer_c(M, b)), tab(M, b))


def g_parabel(s):
    a, bb, c = R.randint(-3, 3), R.randint(-5, 5), R.randint(-6, 6)
    if a == 0: return None
    if s == 1:
        xs = [0, 1, -1]
    elif s == 2:
        xs = R.choice([[0, 1, 2], [0, -1, 2], [0, 2, -2], [-1, 0, 1], [0, 1, 3]])
    else:
        xs = sorted(R.sample([-3, -2, -1, 1, 2, 3], 3))
    pts = [(t, a * t * t + bb * t + c) for t in xs]
    M = [[t * t, t, 1] for t, _ in pts]
    rhs = [y for _, y in pts]
    ptxt = ', '.join(f'({dz(t)} | {dz(y)})' for t, y in pts)
    return luecken(f'Die Parabel y = ax² + bx + c geht durch {ptxt}. Bestimme a, b und c.', 'a = □; b = □; c = □', 'Werte von a, b, c',
                   [a, bb, c], f'Einsetzen ergibt {system(M, rhs, ("a", "b", "c"))}. Lösung a = {dz(a)}, b = {dz(bb)}, c = {dz(c)}: y = {poly(a, bb, c)}.',
                   'Setze jeden Punkt ein: y-Wert links, x² vor a, x vor b.', c=cramer_c(M, rhs))


def anz(n, ein, mehr):
    return f'{n} {ein if n == 1 else mehr}'


def g_sachaufgabe(s):
    typ = R.random()
    if s == 1:
        x = R.randint(1, 15)
        k, d = R.randint(2, 4), R.randint(1, 9)
        y, z = k * x, x + d
        return luecken(f'Drei Zahlen haben die Summe {x + y + z}. Die zweite ist {k}-mal so groß wie die erste, die dritte ist um {d} größer als die erste. Bestimme die Zahlen.',
                       'erste = □; zweite = □; dritte = □', 'erste, zweite, dritte Zahl', [x, y, z],
                       f'x + y + z = {x + y + z}, y = {k}x, z = x + {d} ⇒ {k + 2}x + {d} = {x + y + z} ⇒ x = {x}, y = {y}, z = {z}.',
                       'Drücke y und z durch x aus und setze in die Summe ein.',
                       c=cramer_c([[1, 1, 1], [-k, 1, 0], [-1, 0, 1]], [x + y + z, 0, d]))
    if typ < 0.3:
        e, k, r_ = R.randint(14, 22), R.randint(6, 10), R.randint(10, 15)
        if not (k < r_ < e): return None
        M = [[R.randint(1, 4), R.randint(1, 4), R.randint(1, 3)] for _ in range(3)]
        if det3(M) == 0: return None
        b = [M[i][0] * e + M[i][1] * k + M[i][2] * r_ for i in range(3)]
        gruppen = [f'{anz(M[i][0], "Erwachsener", "Erwachsene")}, {anz(M[i][1], "Kind", "Kinder")} und {anz(M[i][2], "Senior", "Senioren")} zahlen {b[i]} €' for i in range(3)]
        return luecken(f'Im Zoo gilt: {"; ".join(gruppen)}. Wie viel kostet je eine Karte für Erwachsene, Kinder und Senioren?',
                       'Erwachsene □ €; Kinder □ €; Senioren □ €', 'Preise in Euro', [e, k, r_],
                       f'System {system(M, b, ("e", "k", "s"))} ergibt e = {e}, k = {k}, s = {r_}.',
                       'Eine Variable je Kartenart, eine Gleichung je Gruppe.', c=cramer_c(M, b))
    if typ < 0.5:
        a_, b_, c_ = R.randint(1, 30), R.randint(1, 30), R.randint(1, 30)
        if len({a_, b_, c_}) < 3: return None
        s1, s2, s3 = a_ + b_, b_ + c_, a_ + c_
        return luecken(f'Drei Kisten A, B, C wiegen paarweise: A und B zusammen {s1} kg, B und C {s2} kg, A und C {s3} kg. Wie schwer ist jede Kiste?',
                       'A = □ kg; B = □ kg; C = □ kg', 'Massen von A, B, C', [a_, b_, c_],
                       f'Alle drei Gleichungen addieren: 2(A + B + C) = {s1 + s2 + s3} ⇒ A + B + C = {(s1 + s2 + s3) // 2}. Dann A = {a_}, B = {b_}, C = {c_}.',
                       'Addiere alle drei Gleichungen.', c=cramer_c([[1, 1, 0], [0, 1, 1], [1, 0, 1]], [s1, s2, s3]))
    if typ < 0.75:
        z = R.randint(2, 8)
        k = R.choice([2, 3])
        e = k * z
        f_ = R.randint(4, 16)
        n = f_ + e + z
        cent = 50 * f_ + 100 * e + 200 * z
        if cent % 100: return None
        M = [[1, 1, 1], [0, 1, -k], [50, 100, 200]]
        return luecken(f'In einer Spardose sind {n} Münzen zu 50 ct, 1 € und 2 €, zusammen {cent // 100} €. Es gibt {k}-mal so viele 1-€-Münzen wie 2-€-Münzen. Wie viele Münzen jeder Sorte sind es?',
                       '50 ct: □; 1 €: □; 2 €: □', 'Anzahl der Münzen jeder Sorte', [f_, e, z],
                       f'a + b + c = {n}; b = {k}c; 0,5a + b + 2c = {cent // 100}. Lösung: {f_} · 50 ct, {e} · 1 €, {z} · 2 €.',
                       'Eine Variable je Münzsorte. Rechne den Wert in Euro (50 ct = 0,5 €).', c=cramer_c(M, [n, 0, cent]))
    t = R.randint(10, 40)
    k, d = R.choice([2, 3]), R.randint(5, 20)
    f_, sw = k * t, t + d
    n = f_ + t + sw
    M = [[1, 1, 1], [1, -k, 0], [0, -1, 1]]
    return luecken(f'Ein Sportverein hat {n} Mitglieder in den Abteilungen Fußball, Tennis und Schwimmen (jedes Mitglied in genau einer). Fußball hat {k}-mal so viele Mitglieder wie Tennis, Schwimmen {d} mehr als Tennis. Wie viele sind es je Abteilung?',
                   'Fußball: □; Tennis: □; Schwimmen: □', 'Mitglieder je Abteilung', [f_, t, sw],
                   f'f + t + s = {n}; f = {k}t; s = t + {d} ⇒ {k + 2}t + {d} = {n} ⇒ t = {t}, f = {f_}, s = {sw}.',
                   'Drücke Fußball und Schwimmen durch Tennis aus.', c=cramer_c(M, [n, 0, d]))


GEN = {'pruefen': g_pruefen, 'stufenform': g_stufenform, 'eliminieren': g_eliminieren, 'loesen': g_loesen,
       'parabel': g_parabel, 'sachaufgabe': g_sachaufgabe}

# ---------- Zehnte Runde (schwer-kl9): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Abschnitt mit eigenem festen Zufallsstart (anhaengen(..., 9906, ...)), läuft erst nach bauen():
# alle bisherigen Aufgaben bleiben unverändert. Vorbilder: 65. Mathematik-Olympiade, 1. Runde, Kl. 9/10 (Aufgabe
# 651013: Gleichungssysteme mit zyklischen Summen – erst die Gesamtsumme bestimmen, Unlösbarkeit zeigen),
# Illustrierende Aufgaben Realschule 9 (I) (Lösungen zweier Schüler beurteilen, Tarif-Sachaufgabe),
# LehrplanPLUS-Beispiel „Parabel durch drei Punkte“, BMT10 2025 (Punkte auf einer Parabel). Zahlen und Wortlaut eigen.
# Echte Prüfungsaufgaben speziell zu LGS mit drei Unbekannten (Gymnasium Bayern, frei zugänglich) wurden nicht gefunden.
from _schwer_kl9 import anhaengen  # noqa: E402


def schwer():
    P, Kn, O = 'pruefung', 'knobel', ''
    X3 = 'x = □; y = □; z = □'
    Hz = 'ganze Zahlen eintragen'
    return [
        # pruefen
        ('pruefen', 3, P, auswahl('Zwei Schüler lösen (I) x + y + z = 6; (II) x − y = 1; (III) y + z = 3. A erhält (3 | 2 | 1), B erhält (2 | 1 | 3). Wer hat recht?',
                                  'nur A', ['nur B', 'beide', 'keiner'],
                                  'A: 3 + 2 + 1 = 6, 3 − 2 = 1, 2 + 1 = 3 – alles stimmt. B: (I) und (II) stimmen, aber (III): 1 + 3 = 4 ≠ 3.',
                                  'Setze jedes Tripel in alle drei Gleichungen ein.')),
        ('pruefen', 3, P, zahl('Für welche Zahl a ist (2 | −1 | 3) eine Lösung von (I) x + y + z = 4; (II) ax − y + z = 8; (III) x + 2y − z = −3?',
                               '(I): 2 − 1 + 3 = 4 und (III): 2 − 2 − 3 = −3 stimmen. (II): 2a + 1 + 3 = 8 ⇒ 2a = 4 ⇒ a = 2.',
                               'Setze das Tripel in (II) ein und löse nach a auf. Prüfe auch (I) und (III).', 2, '(8 - 1 - 3) / 2')),
        ('pruefen', 3, Kn, auswahl('Was gilt für das System (I) x − y = 1; (II) y − z = 1; (III) z − x = 1?', 'Keine Lösung: Addiert man alle drei Gleichungen, entsteht 0 = 3.',
                                   ['Genau eine Lösung: (1 | 0 | −1).', 'Unendlich viele Lösungen.', 'Genau eine Lösung: (2 | 1 | 0).'],
                                   'Links: (x − y) + (y − z) + (z − x) = 0, rechts 1 + 1 + 1 = 3. 0 = 3 ist falsch, also gibt es kein Tripel. (2 | 1 | 0) erfüllt (I) und (II), aber (III): 0 − 2 = −2.',
                                   'Addiere alle drei Gleichungen. Was bleibt links übrig?')),
        ('pruefen', 3, O, auswahl('Welches Tripel löst (I) x + y + z = 0; (II) x = 2y; (III) z = y − 4?', '(2 | 1 | −3)', ['(1 | 2 | −3)', '(2 | 1 | 3)', '(−2 | −1 | 3)'],
                                  'Einsetzen: 2y + y + (y − 4) = 0 ⇒ 4y = 4 ⇒ y = 1, x = 2, z = −3. Probe: 2 + 1 − 3 = 0.',
                                  'Drücke x und z durch y aus und setze in (I) ein.')),
        ('pruefen', 2, O, auswahl('Ist (1 | 1 | 1) Lösung von (I) x + y + z = 3; (II) 2x − y = 1; (III) x + 3z = 5?', 'Nein, (III) ist nicht erfüllt.',
                                  ['Ja, alle drei Gleichungen sind erfüllt.', 'Nein, (I) ist nicht erfüllt.', 'Nein, (II) ist nicht erfüllt.'],
                                  '(I): 3 ✓, (II): 2 − 1 = 1 ✓, (III): 1 + 3 = 4 ≠ 5.', 'Setze in jede Gleichung ein.')),
        ('pruefen', 2, O, auswahl('Ist (0 | 2 | −1) Lösung von (I) x + y + z = 1; (II) 3x + y = 2; (III) y + 2z = 0?', 'Ja, alle drei Gleichungen sind erfüllt.',
                                  ['Nein, (I) ist nicht erfüllt.', 'Nein, (II) ist nicht erfüllt.', 'Nein, (III) ist nicht erfüllt.'],
                                  '(I): 0 + 2 − 1 = 1 ✓, (II): 0 + 2 = 2 ✓, (III): 2 − 2 = 0 ✓.', 'Setze in jede Gleichung ein; achte auf z = −1.')),
        # stufenform
        ('stufenform', 3, P, luecken('Löse: (I) x + y + z = 2; (II) 2y − z = 7; (III) 3z = −3.', X3, Hz, [0, 3, -1],
                                     'Aus (III): z = −1. In (II): 2y + 1 = 7 ⇒ y = 3. In (I): x + 3 − 1 = 2 ⇒ x = 0.', 'Von unten nach oben einsetzen.', ['2 - 3 + 1', '(7 - 1) // 2', '-3 // 3'])),
        ('stufenform', 3, P, luecken('Löse: (I) 2x − y + z = 9; (II) 4y + z = −5; (III) 0,5z = 1,5.', X3, Hz, [2, -2, 3],
                                     'Aus (III): z = 3. In (II): 4y = −8 ⇒ y = −2. In (I): 2x + 2 + 3 = 9 ⇒ x = 2.', 'Bei (III) mit 2 malnehmen.', ['(9 - 2 - 3) // 2', '-8 // 4', '3'])),
        ('stufenform', 3, Kn, zahl('Im System (I) x + y + z = 6; (II) y + z = ?; (III) z = 1 ist die Zahl in (II) verdeckt. Die Lösung hat x = 2. Welche Zahl ist verdeckt?',
                                   'Aus (I): y + z = 6 − x = 6 − 2 = 4. Genau das steht in (II): Die verdeckte Zahl ist 4 (dann y = 3, z = 1).',
                                   'Rückwärts: Was folgt aus (I) für y + z, wenn x = 2 ist?', 4, '6 - 2')),
        ('stufenform', 3, O, luecken('Löse: (I) x − 2y + 3z = 13; (II) −y + 4z = 11; (III) −2z = −6.', X3, Hz, [6, 1, 3],
                                     'z = 3. (II): −y + 12 = 11 ⇒ y = 1. (I): x − 2 + 9 = 13 ⇒ x = 6.', 'Achte auf die Minuszeichen.', ['13 + 2 - 9', '12 - 11', '3'])),
        ('stufenform', 2, O, luecken('Löse: (I) x + y + z = 9; (II) y + z = 5; (III) z = 2.', X3, Hz, [4, 3, 2], 'z = 2, y = 3, x = 9 − 5 = 4.', 'Von unten nach oben.', ['9 - 5', '5 - 2', '2'])),
        ('stufenform', 2, O, luecken('Löse: (I) x − y = 1; (II) y − z = 2; (III) z = 4.', X3, Hz, [7, 6, 4], 'z = 4, y = 6, x = 7.', 'Von unten nach oben.', ['6 + 1', '4 + 2', '4'])),
        # eliminieren
        ('eliminieren', 3, P, zahl('Für das System (I) x + y = 9; (II) y + z = 13; (III) x + z = 12 gilt: Wie groß ist x + y + z?',
                                   'Alle drei Gleichungen addieren: 2x + 2y + 2z = 34, also x + y + z = 17. (Daraus: z = 17 − 9 = 8, x = 4, y = 5.)',
                                   'Addiere alle drei Gleichungen. Jede Unbekannte kommt zweimal vor.', 17, '(9 + 13 + 12) / 2')),
        ('eliminieren', 3, P, zahl('(I) x + y + z = 10; (II) x + y − z = 4. Bestimme z, ohne x und y einzeln zu kennen.',
                                   '(I) − (II): x und y fallen weg, 2z = 6, also z = 3.', 'Welche Rechnung lässt x und y gleichzeitig verschwinden?', 3, '(10 - 4) / 2')),
        ('eliminieren', 3, Kn, zahl('(I) x + 2y + 3z = 14; (II) 3x + 2y + z = 10. Wie groß ist x + y + z?',
                                    '(I) + (II): 4x + 4y + 4z = 24, also x + y + z = 6. x, y, z einzeln sind gar nicht nötig.',
                                    'Addiere die beiden Gleichungen und schau auf die Koeffizienten.', 6, '(14 + 10) / 4')),
        ('eliminieren', 3, O, luecken('(I) x + y + z = 6; (II) 2x − y + 3z = 9. Berechne (II) − 2 · (I).', '□y + □z = □', 'Zahlen eintragen (auch negativ)', [-3, 1, -3],
                                      '2 · (I): 2x + 2y + 2z = 12. (II) − 2 · (I): (−1 − 2)y + (3 − 2)z = 9 − 12, also −3y + z = −3.',
                                      'Erst jedes Glied von (I) verdoppeln, dann spaltenweise subtrahieren.', ['-1 - 2', '3 - 2', '9 - 12'])),
        ('eliminieren', 2, O, luecken('(I) x + y − z = 2; (II) x − y + 2z = 7. Berechne (I) + (II).', '□x + □z = □', 'Zahlen eintragen', [2, 1, 9],
                                      'y fällt weg: 2x + z = 9.', 'Spaltenweise addieren.', ['1 + 1', '-1 + 2', '2 + 7'])),
        ('eliminieren', 2, O, auswahl('(I) x + 3y − z = 4; (II) 2x + y + z = 1. Welche Rechnung eliminiert z?', '(I) + (II)', ['(I) − (II)', '2 · (I) − (II)', '(I) − 2 · (II)'],
                                      'Die z-Koeffizienten sind −1 und +1: Addieren ergibt 0.', 'Schau nur auf die z-Glieder.')),
        # loesen
        ('loesen', 3, P, luecken('Löse: (I) x + y + z = 6; (II) x − y + z = 2; (III) x + y − z = 0.', X3, Hz, [1, 2, 3],
                                 '(I) − (II): 2y = 4 ⇒ y = 2. (I) − (III): 2z = 6 ⇒ z = 3. Dann x = 6 − 2 − 3 = 1.', 'Subtrahiere geschickt, sodass gleich zwei Unbekannte wegfallen.',
                                 ['6 - 2 - 3', '4 // 2', '6 // 2'])),
        ('loesen', 3, P, luecken('Löse: (I) 2x + y + z = 5; (II) x + 2y + z = 6; (III) x + y + 2z = 9.', X3, Hz, [0, 1, 4],
                                 'Alle addieren: 4(x + y + z) = 20 ⇒ x + y + z = 5. (I) − Summe: x = 0; (II): y = 1; (III): z = 4.',
                                 'Addiere alle drei Gleichungen und nutze die Summe x + y + z.', ['5 - 5', '6 - 5', '9 - 5'])),
        ('loesen', 3, Kn, zahl('Drei Zahlen haben die Summe 30. Die erste ist um 4 größer als die zweite, die dritte so groß wie die beiden anderen zusammen. Wie heißt die erste Zahl?',
                               'z = x + y ⇒ 2(x + y) = 30 ⇒ x + y = 15. Mit x = y + 4: 2y + 4 = 15 ⇒ y = 5,5 und x = 9,5 (z = 15).',
                               'Setze die dritte Bedingung in die Summe ein – dann kennst du x + y.', 9.5, '(15 + 4) / 2')),
        ('loesen', 3, O, luecken('Löse: (I) x + 2y − z = 3; (II) 2x − y + z = 4; (III) x + y + z = 4.', X3, Hz, [2, 1, 1],
                                 '(I) + (II): 3x + y = 7. (I) + (III): 2x + 3y = 7. Daraus 7x = 14 ⇒ x = 2, y = 1; aus (III) z = 1.',
                                 'Eliminiere z zweimal, dann bleibt ein System mit x und y.', ['14 // 7', '7 - 6', '4 - 2 - 1'])),
        ('loesen', 2, O, luecken('Löse: (I) x + y = 5; (II) y + z = 7; (III) x + z = 6.', X3, Hz, [2, 3, 4],
                                 'Addieren: 2(x + y + z) = 18 ⇒ Summe 9. z = 9 − 5 = 4, x = 9 − 7 = 2, y = 9 − 6 = 3.', 'Addiere alle drei Gleichungen.', ['9 - 7', '9 - 6', '9 - 5'])),
        ('loesen', 2, O, auswahl('Welche Unbekannte eliminierst du in (I) x + y + 2z = 5; (II) x − y + z = 1; (III) 2x + y − z = 3 am geschicktesten zuerst?', 'y',
                                 ['x', 'z', 'Keine – man muss mit Brüchen rechnen.'],
                                 'y hat die Koeffizienten 1, −1, 1: (I) + (II) und (II) + (III) eliminieren y ohne Vervielfachen.', 'Suche Koeffizienten, die sich direkt zu 0 addieren.')),
        # parabel
        ('parabel', 3, P, luecken('Eine Parabel y = ax² + bx + c geht durch A(0 | 3), B(1 | 4) und C(2 | 3). Bestimme a, b und c.', 'a = □; b = □; c = □', Hz, [-1, 2, 3],
                                  'A: c = 3. B: a + b = 1. C: 4a + 2b = 0 ⇒ b = −2a ⇒ −a = 1 ⇒ a = −1, b = 2.', 'Beginne mit dem Punkt auf der y-Achse.', ['-1', '1 + 1', '3'])),
        ('parabel', 3, P, zahl('Ein Brückenbogen hat die Form einer Parabel y = ax² + bx + c durch (0 | 0), (40 | 0) und (20 | 10) (alles in m). Bestimme a.',
                               '(0 | 0): c = 0. (40 | 0): 1 600a + 40b = 0 ⇒ b = −40a. (20 | 10): 400a + 20b = 10 ⇒ 400a − 800a = 10 ⇒ a = −0,025 (b = 1).',
                               'Setze die drei Punkte ein; c ist sofort klar.', -0.025, '-10 / 400')),
        ('parabel', 3, Kn, zahl('Die Parabel y = x² + bx + c geht durch (1 | 0) und (5 | 0). In welchem Punkt (0 | c) schneidet sie die y-Achse? Gib c an.',
                                'Mit den Nullstellen gilt y = (x − 1)(x − 5) = x² − 6x + 5. Also c = 1 · 5 = 5 – ganz ohne Gleichungssystem.',
                                'Denke an die Produktform mit den Nullstellen.', 5, '1 * 5')),
        ('parabel', 3, O, luecken('Die Parabel y = ax² + bx + c geht durch (−1 | 6), (1 | 2) und (2 | 3). Bestimme a, b und c.', 'a = □; b = □; c = □', Hz, [1, -2, 3],
                                  '(I) a − b + c = 6; (II) a + b + c = 2; (III) 4a + 2b + c = 3. (II) − (I): 2b = −4 ⇒ b = −2. Dann a + c = 4 und 4a + c = 7 ⇒ a = 1, c = 3.',
                                  'Subtrahiere (I) von (II), dann fällt a und c weg.', ['1', '-4 // 2', '4 - 1'])),
        ('parabel', 2, O, luecken('Eine Parabel y = ax² + c geht durch (0 | −4) und (2 | 0). Bestimme a und c.', 'a = □; c = □', Hz, [1, -4],
                                  '(0 | −4): c = −4. (2 | 0): 4a − 4 = 0 ⇒ a = 1.', 'Erst c aus dem Punkt auf der y-Achse.', ['4 // 4', '-4'])),
        ('parabel', 2, O, luecken('Setze P(3 | 10) in y = ax² + bx + c ein. Welche Gleichung entsteht?', '□a + □b + c = □', 'Zahlen eintragen', [9, 3, 10],
                                  'x = 3, y = 10: a · 3² + b · 3 + c = 10, also 9a + 3b + c = 10.', 'x = 3 für x einsetzen, y = 10 nach rechts.', ['3 ** 2', '3', '10'])),
        # sachaufgabe
        ('sachaufgabe', 3, P, luecken('Ein Kino hat Preise für Erwachsene (E), Jugendliche (J) und Kinder (K). Montag: 2 E, 1 J und 3 K kosten 61 €. Dienstag: 1 E, 2 J und 1 K kosten 40 €. Mittwoch: 3 E und 1 K kosten 50 €. Was kostet je eine Karte?',
                                      'E = □ €; J = □ €; K = □ €', Hz, [14, 9, 8],
                                      '(III): K = 50 − 3E. In (I): 2E + J + 150 − 9E = 61 ⇒ J = 7E − 89. In (II): E + 14E − 178 + 50 − 3E = 40 ⇒ 12E = 168 ⇒ E = 14, J = 9, K = 8.',
                                      'Stelle drei Gleichungen auf. (III) hat nur zwei Unbekannte – damit anfangen.', ['168 // 12', '7 * 14 - 89', '50 - 42'])),
        ('sachaufgabe', 3, P, luecken('Von 26 Kindern einer Klasse fahren einige mit dem Bus, einige mit dem Rad, der Rest geht zu Fuß. Mit dem Rad kommen doppelt so viele wie zu Fuß, mit dem Bus 6 mehr als mit dem Rad. Wie viele sind es jeweils?',
                                      'Bus: □; Rad: □; zu Fuß: □', Hz, [14, 8, 4],
                                      'Zu Fuß z, Rad 2z, Bus 2z + 6. Summe: 5z + 6 = 26 ⇒ z = 4, Rad 8, Bus 14.', 'Drücke alles durch die Zahl der Fußgänger aus.', ['2 * 4 + 6', '2 * 4', '(26 - 6) // 5'])),
        ('sachaufgabe', 3, Kn, zahl('Eine dreistellige Zahl hat die Quersumme 13. Die Hunderterziffer ist doppelt so groß wie die Einerziffer, die Zehnerziffer um 1 größer als die Einerziffer. Wie heißt die Zahl?',
                                    'Einer e, Hunderter 2e, Zehner e + 1. Quersumme: 2e + (e + 1) + e = 13 ⇒ 4e = 12 ⇒ e = 3. Zahl: 643.',
                                    'Nimm die drei Ziffern als Unbekannte, nicht die Zahl selbst.', 643, '6 * 100 + 4 * 10 + 3')),
        ('sachaufgabe', 3, O, luecken('1 kg Nussmischung besteht aus Mandeln (12 €/kg), Haselnüssen (8 €/kg) und Cashews (16 €/kg) und kostet 11,20 €. Es sind doppelt so viele Haselnüsse wie Cashews (nach Gewicht). Wie viel Gramm von jeder Sorte?',
                                      'Mandeln □ g; Haselnüsse □ g; Cashews □ g', Hz, [400, 400, 200],
                                      'm + h + c = 1 000; 12m + 8h + 16c = 11 200 (in €/1 000); h = 2c. Dann m = 1 000 − 3c und 12 000 − 36c + 32c = 11 200 ⇒ c = 200, h = 400, m = 400.',
                                      'Rechne mit Gramm; der Preis für 1 kg: 12 · m/1 000 + … = 11,20.', ['1000 - 600', '2 * 200', '800 // 4'])),
        ('sachaufgabe', 2, O, luecken('Drei Zahlen haben die Summe 20. Die zweite ist doppelt so groß wie die erste, die dritte um 4 größer als die erste. Wie heißen die Zahlen?',
                                      '1. Zahl: □; 2. Zahl: □; 3. Zahl: □', Hz, [4, 8, 8], 'x + 2x + (x + 4) = 20 ⇒ 4x = 16 ⇒ x = 4; dann 8 und 8.', 'Drücke alle durch die erste Zahl aus.',
                                      ['16 // 4', '2 * 4', '4 + 4'])),
        ('sachaufgabe', 2, O, luecken('In einem Dreieck ist β doppelt so groß wie α, und γ ist um 20° größer als β. Wie groß sind die Winkel?', 'α = □°; β = □°; γ = □°', Hz, [32, 64, 84],
                                      'α + 2α + (2α + 20°) = 180° ⇒ 5α = 160° ⇒ α = 32°, β = 64°, γ = 84°.', 'Die Winkelsumme im Dreieck ist 180°.', ['160 // 5', '2 * 32', '64 + 20'])),
    ]


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('gleichungen.lgs3', 13_9_6)
# a) Einsetzen wie Stufe 2
for _t in ['(−8 | 5 | 3) Lösung des Systems (I) −x − y + 2z = 9; (II) −2x + 2y − z = 9; (III) −x − 3y + z = −4',
           '(2 | 1 | 4) Lösung des Systems (I) −x + 2y + 3z = 17; (II) y + z = 5; (III) x − y + 3z = 13',
           '(1 | −2 | −1) Lösung des Systems (I) −x + 3y − 2z = −5; (II) −x − 3z = 2; (III) −3x + y + 3z = −8',
           '(−7 | 4 | 3) Lösung des Systems (I) −x + y − 2z = 5; (II) −3x − y + 2z = 3; (III) 3x + y + 3z = −8',
           '(−2 | 0 | −2) Lösung des Systems (I) −y − 2z = 9; (II) y − 3z = 6; (III) −2x + y − z = 6',
           '(3 | 10 | 5) Lösung des Systems (I) −3x + y − z = −4; (II) −2x + z = −1; (III) −2x + 3y − z = 8']:
    BF.stufe('pruefen', f'Ist {_t}?', 2)
# c) Schablone „□y + □z = □“ mit Lösung 0y + 1z = 0 ist eine ungewöhnliche Schreibweise → nach z fragen
BF.ersetze('eliminieren', 'Gegeben: (I) −x − 2y − z = −10; (III) −2x − 4y − z = −20. Berechne (III) − 2 · (I).', BF.Z(
    'Gegeben: (I) −x − 2y − z = −10; (III) −2x − 4y − z = −20. Berechne (III) − 2 · (I). Welchen Wert hat z?', 0, '(-20) - (2) * (-10)',
    '(III) − 2 · (I): −2x − (−2x) = 0, −4y − (−4y) = 0, −z − (−2z) = z; rechts −20 − (−20) = 0. Es bleibt z = 0 – hier fallen x und y zugleich weg.',
    'Rechne Glied für Glied, auch auf der rechten Seite.'))
BF.nicht_umgesetzt('loesen S3 „Wie viele Lösungen hat das System …?“ (unendlich viele)', 'Lösungen richtig; als Vertiefung vertretbar. Die Lernkarte bleibt unverändert (siehe „für den Nutzer“).')
BF.fuer_sebastian('gleichungen.lgs3/loesen: Stufe-3-Aufgaben „Wie viele Lösungen hat das System …?“ (keine/unendlich viele) gehen über den LehrplanPLUS-Text hinaus und werden auf der Lernkarte nicht erklärt – Erklärung ergänzen oder als Vertiefung kennzeichnen?')

# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    d = bauen('gleichungen.lgs3',
          'Lineare Gleichungssysteme mit drei Unbekannten aufstellen und systematisch lösen, z. B. Parabel durch drei Punkte.',
          ['Lösung = Tripel, das alle drei Gleichungen erfüllt.', 'Additionsverfahren: Vielfache addieren/subtrahieren, bis eine Variable wegfällt.',
           'Zweimal dieselbe Variable eliminieren → System mit zwei Unbekannten.', 'Parabel durch drei Punkte: jeden Punkt in y = ax² + bx + c einsetzen.'],
          [('Grundlagen', ['pruefen', 'stufenform']), ('Lösungsverfahren', ['eliminieren', 'loesen']),
           ('Anwendungen', ['parabel', 'sachaufgabe'])],
          ETAPPEN, GEN,
          meiden={'parabel': ['(0 | 1), (1 | 2), (−1 | 4)']},
          offen=['Gleichungssysteme stehen im Fragetext in einer Zeile; bei „stufenform“ und „loesen“ zusätzlich untereinander als Tabelle (f.grafik). Bei den übrigen Karten noch einzeilig.',
                 'Sonderfälle (keine oder unendlich viele Lösungen) nur als Erkennen-Aufgabe in Stufe 3 von „loesen“ (Prüfvorschlag); die Erklärung der Karte nennt sie nicht ausdrücklich.'])
    anhaengen(d, 9906, schwer)
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden


# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl9) ----
from _durchsicht_kl9 import Befunde as _DSB, durchsicht  # noqa: E402

DS = _DSB('gleichungen.lgs3', 19_9_5)
# stufenform: gewöhnliche Stufenform ist Stufe 2; auf Stufe 3 bleiben die vertauschten Systeme und die verdeckte Zahl
for _t in ('Löse: (I) x + y + z = 2; (II) 2y − z = 7; (III) 3z = −3.', 'Löse: (I) 2x − y + z = 9; (II) 4y + z = −5; (III) 0,5z = 1,5.',
           'Löse: (I) x − 2y + 3z = 13; (II) −y + 4z = 11; (III) −2z = −6.'):
    DS.stufe('stufenform', _t, 2)
# eliminieren: Vielfache abziehen wie auf Stufe 2
for _t in ('Gegeben: (I) −2x + y + 3z = 16; (III) −x + 3y + 2z = 9. Berechne 2 · (III) − (I).',
           'Gegeben: (II) −x + 3z = −3; (III) 3x − 3y − z = −10. Berechne (III) + 3 · (II).',
           '(I) x + y + z = 6; (II) 2x − y + 3z = 9. Berechne (II) − 2 · (I).'):
    DS.stufe('eliminieren', _t, 2)
# loesen: dieselbe Aufgabe mit größeren Zahlen → Stufe 2
for _t in ('Löse das Gleichungssystem: (I) −x − 2y − 3z = 25; (II) x + 3y + z = −21; (III) x − 2y − z = 19.',
           'Löse das Gleichungssystem: (I) −x − 3y + 2z = 17; (II) 2x − 3y + z = −4; (III) 3x + y − 2z = −23.',
           'Löse das Gleichungssystem: (I) x − 3y + 2z = −2; (II) 2x + 2y − z = 6; (III) x + 3y − 3z = 8.',
           'Löse das Gleichungssystem: (I) −3x + y + z = −15; (II) −3x − y + z = −29; (III) −2x − 2y − z = −27.'):
    DS.stufe('loesen', _t, 2)
# parabel: drei beliebige Punkte sind die Abwandlung (Stufe 2); dazu zwei Aufgaben mit anderem Gedanken
for _t in ('Die Parabel y = ax² + bx + c geht durch (−3 | −37), (2 | −2), (3 | −13). Bestimme a, b und c.',
           'Die Parabel y = ax² + bx + c geht durch (−3 | 30), (−1 | 6), (2 | 0). Bestimme a, b und c.',
           'Die Parabel y = ax² + bx + c geht durch (−2 | −7), (1 | −1), (3 | −27). Bestimme a, b und c.',
           'Die Parabel y = ax² + bx + c geht durch (−1 | −8), (1 | −2), (2 | 4). Bestimme a, b und c.',
           'Eine Parabel y = ax² + bx + c geht durch A(0 | 3), B(1 | 4) und C(2 | 3). Bestimme a, b und c.',
           'Die Parabel y = ax² + bx + c geht durch (−1 | 6), (1 | 2) und (2 | 3). Bestimme a, b und c.'):
    DS.stufe('parabel', _t, 2)
DS.neu('parabel', 3, DS.Z('Eine Parabel ist symmetrisch zur y-Achse und geht durch (2 | 1) und (4 | 7). Bestimme c in y = ax² + bx + c.', -1, '1 - 4 * 1 / 2',
                          'Symmetrisch zur y-Achse heißt b = 0: y = ax² + c. (2 | 1): 4a + c = 1; (4 | 7): 16a + c = 7. Abziehen: 12a = 6, a = 0,5; c = 1 − 2 = −1.',
                          'Was bedeutet „symmetrisch zur y-Achse“ für b? Dann reichen zwei Gleichungen.'))
DS.neu('parabel', 3, DS.A('Jemand setzt den Punkt (−2 | 5) in y = ax² + bx + c ein und schreibt −4a − 2b + c = 5. Was stimmt?', 'Falsch: (−2)² = 4, richtig ist 4a − 2b + c = 5.',
                          ['Richtig.', 'Falsch: richtig ist 4a + 2b + c = 5.', 'Falsch: richtig ist −4a − 2b + c = −5.'],
                          'x = −2 einsetzen: a · (−2)² + b · (−2) + c = 4a − 2b + c. Das Quadrat einer negativen Zahl ist positiv.',
                          'Rechne (−2)² und b · (−2) einzeln aus.'))
# sachaufgabe: Zahlenrätsel wie Stufe 1; Sportverein wie Stufe 2
DS.stufe('sachaufgabe', 'Drei Zahlen haben die Summe 20. Die zweite ist doppelt so groß wie die erste, die dritte um 4 größer als die erste. Wie heißen die Zahlen?', 1)
DS.stufe('sachaufgabe', 'Ein Sportverein hat 75 Mitglieder in den Abteilungen Fußball, Tennis und Schwimmen (jedes Mitglied in genau einer). Fußball hat 3-mal so viele Mitglieder wie Tennis, Schwimmen 20 mehr als Tennis. Wie viele sind es je Abteilung?', 2)
DS.fuer_sebastian('gleichungen.lgs3: Der LehrplanPLUS M9 2.2 verlangt LGS mit drei Unbekannten nur für Parabelpunkte; die ISB-Schwerpunktsetzung erlaubt „wenige, einfache Beispiele“. Sechs Lernkarten (Prüfen, Stufenform, Eliminieren, Lösen, Parabel, Sachaufgaben) sind dafür viel – Vorschlag: pruefen, stufenform, eliminieren als Vertiefung oder zusammenfassen.')

if __name__ == '__main__':
    durchsicht('gleichungen.lgs3', DS)


# ---- STUFEN (Zwanzigste Runde, Zweig stufen-kl9) ----
from _stufen_kl9 import Stufen, stufen  # noqa: E402

ST = Stufen('gleichungen.lgs3', 20_9_5)
Z, A, L = ST.Z, ST.A, ST.L
_T = '(□ | □ | □)'

# pruefen
ST.stufenleiter('pruefen', 'Ein Zahlentripel in eine Gleichung einsetzen.',
                'Ein Tripel in allen drei Gleichungen prüfen, eine fehlende Koordinate bestimmen, Preise im Sachzusammenhang prüfen.',
                'Zwei Lösungsvorschläge beurteilen, Parameter bestimmen, widersprüchliche Systeme erkennen, unvollständige Probe finden, mehrteilige Aufgabe.')
ST.typ('pruefen', 'Setze (x | y | z)', 'direkt')
ST.typ('pruefen', 'Ist (', 'mehrschritt')
ST.typ('pruefen', '/^(Zwei Schüler|Was gilt für das System)/', 'begruenden')
ST.typ('pruefen', 'Für welche Zahl a', 'parameter')
ST.typ('pruefen', 'Welches Tripel', 'verknuepfen')
ST.neu('pruefen', 'erkennen', A('Was bedeutet: „(1 | 2 | 3) ist eine Lösung des Gleichungssystems“?', 'Das Tripel erfüllt alle drei Gleichungen.', ['Es erfüllt mindestens eine Gleichung.', 'Es erfüllt genau zwei Gleichungen.', 'Die Summe 1 + 2 + 3 steht in jeder Gleichung.'],
       'Eine Lösung muss jede Gleichung des Systems erfüllen. Schon eine falsche Gleichung reicht, damit es keine Lösung ist.', 'Wie viele Gleichungen müssen stimmen?'))
ST.neu('pruefen', 'einkleidung', A('Ein Kiosk: Brezel, Saft und Apfel kosten zusammen 3 €; zwei Brezeln und ein Saft 3,50 €; ein Saft und zwei Äpfel 2,50 €. Passen die Preise Brezel 1 €, Saft 1,50 €, Apfel 0,50 €?', 'Ja, alle drei Angaben stimmen.',
       ['Nein, die erste Angabe stimmt nicht.', 'Nein, die zweite Angabe stimmt nicht.', 'Nein, die dritte Angabe stimmt nicht.'],
       '1 + 1,5 + 0,5 = 3 €; 2 · 1 + 1,5 = 3,50 €; 1,5 + 2 · 0,5 = 2,50 €. Alle drei stimmen.', 'Prüfe jede Angabe einzeln.'))
ST.neu('pruefen', 'umkehr', Z('Das Tripel (2 | y | 1) erfüllt die Gleichung x + 2y + z = 9. Bestimme y.', 3, '(9 - 2 - 1) // 2',
       '2 + 2y + 1 = 9 ⇒ 2y = 6 ⇒ y = 3.', 'Setze x und z ein.'))
ST.neu('pruefen', 'fehler', A('Jemand prüft (1 | 1 | 1) für (I) x + y + z = 3; (II) x − y = 0; (III) x + 2z = 4. Er rechnet (I) und (II) nach und sagt: „Lösung.“ Was stimmt?', 'Falsch: In (III) ergibt sich 3, nicht 4. Keine Lösung.',
       ['Richtig, zwei Gleichungen reichen.', 'Falsch: Schon (I) stimmt nicht.', 'Falsch: (II) stimmt nicht.'], '(III): 1 + 2 · 1 = 3 ≠ 4. Eine Lösung muss alle Gleichungen erfüllen.', 'Prüfe auch die dritte Gleichung.'))
ST.neu('pruefen', 'parameter', Z('Für welche Zahl a ist (a | a | a) eine Lösung der Gleichung x + 2y + 3z = 18?', 3, '18 // 6',
       'a + 2a + 3a = 6a = 18 ⇒ a = 3.', 'Setze dreimal a ein.'))
ST.neu('pruefen', 'transfer', A('Drei Zahlen: Ihre Summe ist 10, die erste ist doppelt so groß wie die zweite, die dritte ist um 1 kleiner als die erste. Ist (4 | 2 | 3) die Lösung?', 'Nein, die Summe ist 9 statt 10.',
       ['Ja.', 'Nein, die erste ist nicht doppelt so groß wie die zweite.', 'Nein, die dritte passt nicht.'], 'Bedingungen 2 und 3 stimmen (4 = 2 · 2, 3 = 4 − 1), aber 4 + 2 + 3 = 9 ≠ 10.', 'Übersetze jede Bedingung in eine Gleichung und prüfe.'))
ST.neu('pruefen', 'pruefung', L('Gegeben ist (I) x + y + z = 4; (II) 2x − y = 1; (III) y + z = 3. Setze (1 | 1 | 2) ein und gib die linken Seiten an.', '(I) □; (II) □; (III) □', [4, 1, 3], ['1 + 1 + 2', '2 - 1', '1 + 2'],
       '(I) 1 + 1 + 2 = 4, (II) 2 − 1 = 1, (III) 1 + 2 = 3. Alle rechten Seiten stimmen: (1 | 1 | 2) ist eine Lösung.', 'Setze x = 1, y = 1, z = 2 in jede linke Seite ein.'))
ST.knobel('pruefen', A('Wie viele Lösungen hat das System aus nur zwei Gleichungen (I) x + y − z = 0; (II) 2x − y = 0?', 'unendlich viele, z. B. (t | 2t | 3t) für jede Zahl t',
          ['genau eine', 'keine', 'genau drei'],
          'Aus (II) folgt y = 2x, aus (I) dann z = x + y = 3x. Für jedes x = t passt (t | 2t | 3t). Zwei Gleichungen reichen nicht, um drei Unbekannte festzulegen.',
          'Drücke y und z mit x aus.'))
ST.knobel('pruefen', L('Von drei Zahlen x, y, z ist jede um 2 kleiner als die Summe der beiden anderen. Bestimme die Zahlen.', _T, [2, 2, 2], ['2', '2', '2'],
          'x = y + z − 2, y = x + z − 2, z = x + y − 2. Alle drei addieren: S = 2S − 6 mit S = x + y + z, also S = 6. Dann x = (S − x) − 2, also 2x = 4 und x = 2; ebenso y = z = 2.',
          'Addiere alle drei Gleichungen.'))

# stufenform
ST.stufenleiter('stufenform', 'Ein System in Stufenform mit Koeffizient 1 von unten lösen.',
                'Andere Koeffizienten und vertauschte Reihenfolge, ein Sachrätsel in Stufenform, ein System zur Lösung ergänzen.',
                'Verdeckte Zahl rückwärts, Fehler beim Einsetzen, 0 · z = 5 oder 0 = 0 deuten, Parameter, Dezimalzahlen, mehrteilige Aufgabe.')
ST.typ('stufenform', '/^Löse das System in Stufenform: \\(I\\) x [+−]/', 'direkt', s=1)
ST.typ('stufenform', '/^(Löse das System in Stufenform|Löse: |Löse das System:)/', 'mehrschritt')
ST.typ('stufenform', 'Im System', 'rueckwaerts')
ST.neu('stufenform', 'erkennen', A('Welche Unbekannte bestimmst du bei (I) x + y + z = 6; (II) y + z = 4; (III) z = 1 zuerst?', 'z', ['x', 'y', 'alle gleichzeitig'],
       'Die unterste Gleichung enthält nur z. Danach y aus (II), zuletzt x aus (I).', 'Welche Gleichung hat nur eine Unbekannte?'))
ST.neu('stufenform', 'einkleidung', Z('Drei Kinder haben Murmeln. Das dritte hat 4. Das zweite hat 3 mehr als das dritte. Alle zusammen haben 20. Wie viele hat das erste?', 9, '20 - 7 - 4',
       'Stufenform: z = 4; y = z + 3 = 7; x + y + z = 20 ⇒ x = 9.', 'Fang beim dritten Kind an.'))
ST.neu('stufenform', 'umkehr', L('Ein System in Stufenform hat die Lösung (1 | 2 | 3). Ergänze: (I) x + y + z = □; (II) y − z = □; (III) 2z = □.', '□; □; □', [6, -1, 6], ['1 + 2 + 3', '2 - 3', '2 * 3'],
       'Lösung einsetzen: (I) 1 + 2 + 3 = 6, (II) 2 − 3 = −1, (III) 2 · 3 = 6.', 'Setze die Lösung in die linken Seiten ein.'))
ST.neu('stufenform', 'fehler', A('Jemand löst (I) x + y + z = 6; (II) y + z = 5; (III) z = 2 und erhält y = 7. Was stimmt?', 'Falsch: y = 5 − 2 = 3.', ['Richtig.', 'Falsch: y = 5.', 'Falsch: y = 2.'],
       'Aus (II): y = 5 − z = 3. Wer 5 + 2 rechnet, hat das Minus vergessen. Dann x = 6 − 3 − 2 = 1.', 'Stelle (II) nach y um.'))
ST.neu('stufenform', 'begruenden', A('Ein System in Stufenform endet mit (III) 0 · z = 5. Was folgt?', 'Es hat keine Lösung.', ['Es hat genau eine Lösung, z = 5.', 'Es hat unendlich viele Lösungen.', 'z = 0.'],
       '0 · z ist immer 0, nie 5. Damit ist schon (III) nie erfüllt.', 'Was ergibt 0 mal eine Zahl?'))
ST.neu('stufenform', 'begruenden', A('Wie viele Lösungen hat (I) x + y + z = 3; (II) y + z = 2; (III) 0 · z = 0?', 'unendlich viele', ['keine', 'genau eine', 'genau zwei'],
       '(III) gilt für jedes z. Dann y = 2 − z und x = 3 − y − z = 1. Für jedes z gibt es eine Lösung (1 | 2 − z | z).', 'Gilt (III) für ein bestimmtes oder für jedes z?'))
ST.neu('stufenform', 'parameter', Z('Für welche Zahl a hat (I) x + y + z = 4; (II) y + a · z = 3; (III) 2z = 2 eine Lösung mit y = 1?', 2, '3 - 1',
       'Aus (III): z = 1. In (II): 1 + a · 1 = 3, also a = 2.', 'Bestimme zuerst z.'))
ST.neu('stufenform', 'transfer', Z('Ein Kuchen braucht Mehl, Zucker und Butter, zusammen 900 g. Zucker und Butter wiegen zusammen 400 g, die Butter allein 150 g. Wie viel Mehl ist es?', 500, '900 - 400',
       'Stufenform: b = 150; z + b = 400 ⇒ z = 250; m + z + b = 900 ⇒ m = 500 g.', 'Ordne die Angaben wie ein System in Stufenform.', einheit='g'))
ST.neu('stufenform', 'verknuepfen', Z('Löse (I) x + y + z = 2; (II) 2y + z = 1,5; (III) 4z = 2. Bestimme x.', 1, '2 - 0.5 - 0.5',
       'z = 0,5; 2y = 1,5 − 0,5 = 1 ⇒ y = 0,5; x = 2 − 0,5 − 0,5 = 1.', 'Rechne mit Dezimalzahlen von unten nach oben.'))
ST.neu('stufenform', 'pruefung', L('Löse (I) x − 2y + z = 3; (II) 3y − z = 2; (III) 2z = 8.', 'z = □; y = □; x = □', [4, 2, 3], ['8 // 2', '(2 + 4) // 3', '3 + 2 * 2 - 4'],
       '(III) z = 4. (II) 3y = 6, y = 2. (I) x − 4 + 4 = 3, x = 3.', 'Von unten nach oben.'))
ST.knobel('stufenform', Z('Es gilt z = 1, y = z + 1, x = y + z + 1 und w = x + y + z + 1. Wie groß ist w?', 8, '4 + 2 + 1 + 1',
          'Von unten: z = 1, y = 2, x = 2 + 1 + 1 = 4, w = 4 + 2 + 1 + 1 = 8. Jede neue Zahl ist doppelt so groß wie die vorige (1, 2, 4, 8): Zum Beispiel ist x = y + (z + 1), und z + 1 ist gerade y; also x = y + y.',
          'Rechne von unten. Fällt dir ein Muster auf?'))

# eliminieren
ST.stufenleiter('eliminieren', 'Zwei Gleichungen addieren oder subtrahieren, wenn eine Variable dabei sofort wegfällt.',
                'Vorher eine Gleichung mit einer Zahl malnehmen, die passende Rechnung auswählen, den Faktor k rückwärts finden, Preise vergleichen.',
                'Summen wie x + y + z ohne Einzelwerte, Fehler beim Malnehmen, Parameter für zwei wegfallende Variablen, Widerspruch 0 = 3, mehrteilige Aufgabe.')
ST.typ('eliminieren', '/^Gegeben: .* Berechne \\(I+\\) [+−] \\(I+\\)\\.$/', 'direkt', s=1)
ST.typ('eliminieren', '/Jemand/', 'fehler')
ST.typ('eliminieren', '/^\\(I\\) x \\+ y \\+ z = 10/', 'begruenden')
ST.typ('eliminieren', '/^Für das System|^\\(I\\) x \\+ 2y \\+ 3z/', 'transfer')
ST.typ('eliminieren', '/^(Gegeben:|\\(I\\))/', 'mehrschritt')
ST.neu('eliminieren', 'erkennen', A('Welche Rechnung lässt bei (I) x + 2y − z = 4; (II) x − y + z = 1 die Variable z wegfallen?', '(I) + (II)', ['(I) − (II)', '2 · (I) + (II)', '(II) − (I)'],
       '−z + z = 0. Bei (I) − (II) bliebe −2z.', 'Vergleiche die Vorzeichen von z.'))
ST.neu('eliminieren', 'einkleidung', Z('2 Äpfel, 1 Birne und 1 Kiwi kosten 2,30 €. 1 Apfel, 1 Birne und 1 Kiwi kosten 1,80 €. Wie viel kostet ein Apfel?', 0.5, '2.3 - 1.8',
       'Zweite Angabe von der ersten abziehen: Birne und Kiwi fallen weg, es bleibt 1 Apfel = 0,50 €.', 'Ziehe die Angaben voneinander ab.', einheit='€'))
ST.neu('eliminieren', 'umkehr', Z('Bei (I) x + y + z = 3 und (II) 4x − y + 2z = 5 fällt bei (II) − k · (I) die Variable x weg. Wie groß ist k?', 4, '4 // 1',
       '(II) hat 4x, (I) hat x. 4x − k · x = 0 ⇒ k = 4.', 'Vergleiche die Zahlen vor x.'))
ST.neu('eliminieren', 'begruenden', A('Was ergibt das Eliminieren bei (I) x + y + z = 1; (II) 2x + 2y + 2z = 5?', '2 · (I) − (II) ergibt 0 = −3: keine Lösung.', ['Eine eindeutige Lösung.', 'x = 3.', 'Unendlich viele Lösungen.'],
       '2 · (I): 2x + 2y + 2z = 2. Minus (II): 0 = 2 − 5 = −3. Ein Widerspruch: Das System hat keine Lösung.', 'Nimm (I) mit 2 mal.'))
ST.neu('eliminieren', 'parameter', Z('Für welche Zahl a fallen bei (II) − (I) mit (I) x + 3y + az = 2 und (II) x − y + 5z = 7 die Variablen x und z gleichzeitig weg?', 5, '5',
       'x fällt bei (II) − (I) immer weg. z fällt weg, wenn 5z − az = 0, also a = 5. Dann bleibt −4y = 5.', 'Was muss vor z stehen?'))
ST.neu('eliminieren', 'pruefung', L('Gegeben: (I) x + y + z = 6; (II) x − y + z = 2; (III) 2x + y − z = 1. Berechne (I) − (II) und bestimme y.', '□y = □; y = □', [2, 4, 2], ['1 + 1', '6 - 2', '4 // 2'],
       '(I) − (II): x − x + y − (−y) + z − z = 6 − 2, also 2y = 4 und y = 2.', 'Rechne Spalte für Spalte.'))
ST.neu('eliminieren', 'verknuepfen', Z('Eliminiere y aus (I) 2x + y = 7 und (II) x − y = −1 (wie bei zwei Unbekannten). Welchen Wert hat x?', 2, '(7 - 1) // 3',
       '(I) + (II): 3x = 6, also x = 2 (und y = 3).', 'Addieren lässt y wegfallen.'))
ST.knobel('eliminieren', Z('Es gilt a + b = 3, b + c = 5, c + d = 7 und d + a = 5. Wie groß ist a + b + c + d?', 10, '(3 + 5 + 7 + 5) // 2',
          'Alle vier Gleichungen addieren: Jede Variable kommt genau zweimal vor. 2(a + b + c + d) = 20, also a + b + c + d = 10. Einzeln lassen sich a, b, c, d hier gar nicht bestimmen.',
          'Addiere alle Gleichungen.'))
ST.knobel('eliminieren', Z('Es gilt x + y + z = 15 und x + 2y + 3z = 32. Wie groß ist y + 2z?', 17, '32 - 15',
          'Zweite minus erste Gleichung: (x − x) + (2y − y) + (3z − z) = 32 − 15, also y + 2z = 17. x, y und z einzeln kennt man nicht.',
          'Welche Rechnung lässt x verschwinden?'))

# loesen
ST.stufenleiter('loesen', 'Ein einfaches System lösen, in dem sich Variablen schnell eliminieren lassen.',
                'Allgemeine Systeme, den geschicktesten Weg wählen, Tieraufgaben, fehlende Zahl aus der Lösung bestimmen.',
                'Lösungsanzahl begründen, Summen-Trick, Parameter für unendlich viele Lösungen, Winkel im Dreieck, Fehler beim Teilen, mehrteilige Aufgabe.')
ST.typ('loesen', 'Löse das Gleichungssystem', 'direkt', s=1)
ST.typ('loesen', 'Wie viele Lösungen hat', 'begruenden')
ST.typ('loesen', 'Löse: (I) 2x + y + z = 5', 'transfer')
ST.typ('loesen', 'Drei Zahlen haben', 'einkleidung')
ST.typ('loesen', '/^(Löse|Welche Unbekannte)/', 'mehrschritt')
ST.neu('loesen', 'erkennen', A('Beim Lösen kommt 0 = 4 heraus. Was bedeutet das?', 'Das System hat keine Lösung.', ['Die Lösung ist x = 4.', 'Es hat unendlich viele Lösungen.', 'Man hat sich sicher verrechnet.'],
       'Eine falsche Aussage wie 0 = 4 zeigt einen Widerspruch: Keine Zahlen erfüllen alle Gleichungen.', 'Kann 0 = 4 jemals stimmen?'))
ST.neu('loesen', 'einkleidung', Z('In einem Stall sind Hühner, Kaninchen und Kühe, zusammen 10 Tiere mit 32 Beinen. Es gibt doppelt so viele Hühner wie Kühe. Wie viele Kaninchen sind es?', 4, '4',
       'h + k + c = 10; 2h + 4k + 4c = 32; h = 2c. Einsetzen: 3c + k = 10 und 8c + 4k = 32, also 2c + k = 8. Abziehen: c = 2, k = 4, h = 4.', 'Hühner haben 2, Kaninchen und Kühe 4 Beine.'))
ST.neu('loesen', 'umkehr', Z('Das System (I) x + y + z = 6; (II) x − y = 0; (III) z = c hat eine Lösung mit x = 2. Bestimme c.', 2, '6 - 2 - 2',
       'Aus (II): y = x = 2. Aus (I): z = 6 − 4 = 2. Also c = 2.', 'Bestimme erst y, dann z.'))
ST.neu('loesen', 'fehler', A('Jemand berechnet bei (I) x + 2y + z = 8; (II) x − y + z = 2 die Differenz (I) − (II) = 3y = 6 und schreibt dann y = 18. Was stimmt?', 'Falsch: Aus 3y = 6 folgt y = 2.', ['Richtig.', 'Falsch: 3y = 10.', 'Falsch: y = 3.'],
       'Bei 3y = 6 wird durch 3 geteilt, nicht malgenommen: y = 2.', 'Wie löst man 3y = 6?'))
ST.neu('loesen', 'parameter', Z('Für welche Zahl a hat (I) x + y + z = 1; (II) x − y + z = 1; (III) 2x + 2z = a unendlich viele Lösungen?', 2, '1 + 1',
       '(I) + (II): 2x + 2z = 2. Ist a = 2, sagt (III) dasselbe; dann bleiben nur zwei verschiedene Gleichungen: unendlich viele Lösungen. Für a ≠ 2 gibt es keine.', 'Addiere (I) und (II) und vergleiche mit (III).'))
ST.neu('loesen', 'pruefung', L('Löse (I) x + y + z = 9; (II) x − y = 1; (III) y − z = 1. a) Setze x = y + 1 und z = y − 1 in (I) ein. b) Gib die Lösung an.', 'a) □y = □; b) (□ | □ | □)', [3, 9, 4, 3, 2],
       ['3', '9', '3 + 1', '9 // 3', '3 - 1'], 'a) y + 1 + y + y − 1 = 3y = 9. b) y = 3, x = 4, z = 2.', 'Drücke x und z mit y aus.'))
ST.neu('loesen', 'verknuepfen', Z('In einem Dreieck ist α + β = 110° und β + γ = 130°. Wie groß ist β?', 60, '110 + 130 - 180',
       'Winkelsumme: α + β + γ = 180°. Addiert man die beiden Angaben, ist β doppelt dabei: 240° = 180° + β, also β = 60°.', 'Denk an die Winkelsumme im Dreieck.', einheit='°'))
ST.neu('loesen', 'rueckwaerts', Z('Ein System hat die Lösung (2 | −1 | 3). Seine dritte Gleichung lautet x + y + c · z = 7. Bestimme c.', 2, '(7 - 2 + 1) // 3',
       'Einsetzen: 2 − 1 + 3c = 7 ⇒ 3c = 6 ⇒ c = 2.', 'Setze die Lösung ein.'))
ST.knobel('loesen', Z('Von vier Zahlen lässt man jeweils eine weg und addiert die anderen drei. Die vier Summen sind 22, 24, 27 und 20. Wie heißt die größte der vier Zahlen?', 11, '31 - 20',
          'Jede Zahl wird in drei der vier Summen mitgezählt: 22 + 24 + 27 + 20 = 93 = 3 · (Summe aller vier). Summe aller vier: 31. Die Zahlen sind 31 − 22 = 9, 31 − 24 = 7, 31 − 27 = 4 und 31 − 20 = 11.',
          'Wie oft kommt jede Zahl in den vier Summen vor?'))
ST.knobel('loesen', Z('Es gilt x + 2y + 3z = 14, 2x + 3y + z = 11 und 3x + y + 2z = 11. Wie groß ist x + y + z?', 6, '(14 + 11 + 11) // 6',
          'Alle drei Gleichungen addieren: 6x + 6y + 6z = 36, also x + y + z = 6. Einzeln: x = 1, y = 2, z = 3.',
          'Addiere alle Gleichungen. Was steht dann vor x, y und z?'))

# parabel
ST.stufenleiter('parabel', 'Drei Punkte mit x = 0, 1, −1 einsetzen und a, b, c bestimmen.',
                'Beliebige Punkte, Werte aus einer Tabelle, Scheitel als Bedingung, ein Wasserstrahl im Sachzusammenhang.',
                'Symmetrie nutzen, Brückenbogen, c aus Nullstellen, Fehler beim Einsetzen negativer x, Parameter, mehrteilige Wurfaufgabe.')
ST.typ('parabel', '/^Die Parabel y = ax² \\+ bx \\+ c geht durch \\(0 \\| −?\\d+\\), \\(1 \\| −?\\d+\\), \\(−1/', 'direkt')
ST.typ('parabel', 'Setze P(', 'erkennen')
ST.typ('parabel', '/^Die Parabel y = ax² \\+ bx \\+ c geht durch \\(−3/', 'verknuepfen')
ST.typ('parabel', '/^(Die Parabel y = ax²|Eine Parabel y = ax²)/', 'mehrschritt')
ST.typ('parabel', 'Ein Brückenbogen', 'transfer')
ST.typ('parabel', 'Die Parabel y = x² + bx + c geht durch (1 | 0)', 'rueckwaerts')
ST.typ('parabel', 'Eine Parabel ist symmetrisch', 'verknuepfen')
ST.typ('parabel', 'Jemand', 'fehler')
ST.neu('parabel', 'erkennen', A('Die Parabel y = ax² + bx + c geht durch (0 | 7). Was folgt daraus sofort?', 'c = 7', ['a = 7', 'b = 7', 'a + b + c = 7'],
       'Bei x = 0 fallen ax² und bx weg: y = c = 7.', 'Setze x = 0 ein.'))
ST.neu('parabel', 'einkleidung', Z('Ein Wasserstrahl kommt aus 1 m Höhe (x = 0), ist bei x = 1 m genau 2 m hoch und bei x = 2 m wieder 1 m hoch. Er folgt einer Parabel. Wie hoch ist er bei x = 1,5 m?', 1.75, '-(1.5 ** 2) + 2 * 1.5 + 1',
       'c = 1; a + b + 1 = 2; 4a + 2b + 1 = 1. Aus a + b = 1 und 2a + b = 0 folgt a = −1, b = 2. y(1,5) = −2,25 + 3 + 1 = 1,75 m.', 'Setze die drei Punkte ein.', einheit='m'))
ST.neu('parabel', 'umkehr', L('Die Parabel y = x² + bx + c hat den Scheitel S(2 | 1). Bestimme b und c.', 'b = □; c = □', [-4, 5], ['-2 * 2', '2 ** 2 + 1'],
       'Scheitelform y = (x − 2)² + 1 = x² − 4x + 5. Also b = −4, c = 5.', 'Schreib zuerst die Scheitelform.'))
ST.neu('parabel', 'darstellung', L('Eine Parabel y = ax² + bx + c hat die Wertetabelle x = −1, 0, 1 mit y = 6, 3, 2. Bestimme a, b und c.', 'a = □; b = □; c = □', [1, -2, 3], ['(6 + 2 - 6) // 2', '(2 - 6) // 2', '3'],
       'c = 3. a − b + 3 = 6 und a + b + 3 = 2. Addieren: 2a = 2, a = 1; dann b = −2.', 'Lies c bei x = 0 ab.'))
ST.neu('parabel', 'parameter', Z('Für welche Zahl a geht die Parabel y = ax² + 2x + 1 durch (2 | 1)?', -1, '(1 - 4 - 1) // 4',
       '1 = 4a + 4 + 1 ⇒ 4a = −4 ⇒ a = −1.', 'Setze den Punkt ein.'))
ST.neu('parabel', 'pruefung', L('Ein Ball wird bei x = 0 aus 1 m Höhe geworfen. Bei x = 1 m ist er 4 m hoch, bei x = 2 m 5 m hoch. a) Bestimme a, b, c. b) Bei welchem x ist er am höchsten?', 'a) a = □; b = □; c = □; b) x = □', [-1, 4, 1, 2],
       ['-1', '4', '1', '4 // 2'], 'a) c = 1; a + b = 3; 4a + 2b = 4. Also 2a = −2, a = −1, b = 4: y = −x² + 4x + 1. b) Scheitelform: −x² + 4x + 1 = −(x − 2)² + 5, der höchste Punkt liegt bei x = 2.', 'Erst c, dann zwei Gleichungen für a und b.'))
ST.knobel('parabel', Z('Eine Parabel y = ax² + bx + c geht durch (1 | 3), (2 | 7) und (3 | 13). Welchen Wert hat sie bei x = 10?', 111, '100 + 10 + 1',
          'Einsetzen: (I) a + b + c = 3, (II) 4a + 2b + c = 7, (III) 9a + 3b + c = 13. (II) − (I): 3a + b = 4. (III) − (II): 5a + b = 6. Diese beiden voneinander abziehen: 2a = 2, a = 1. Dann b = 1 und c = 1. y = x² + x + 1, bei x = 10: 100 + 10 + 1 = 111.',
          'Ziehe die Gleichungen nacheinander voneinander ab, dann fällt c weg.'))
ST.knobel('parabel', A('Wie viele Parabeln y = ax² + bx + c mit a ≠ 0 gehen durch (0 | 0), (1 | 1) und (2 | 2)?', 'keine', ['genau eine', 'unendlich viele', 'genau zwei'],
          'c = 0; a + b = 1; 4a + 2b = 2, also 2a + b = 1. Abziehen: a = 0. Dann wäre es die Gerade y = x, keine Parabel. Die drei Punkte liegen auf einer Geraden.',
          'Liegen die drei Punkte vielleicht auf einer Geraden?'))

# sachaufgabe
ST.stufenleiter('sachaufgabe', 'Zahlenrätsel mit drei Zahlen in Gleichungen übersetzen und lösen.',
                'Vereine, Eintrittspreise und Einkäufe mit drei Unbekannten, Gleichungen selbst aufstellen.',
                'Münzen, Ziffern, Winkel, Mischungen und paarweise Summen modellieren, Fehler beim Aufstellen finden, mehrteilige Aufgabe.')
ST.typ('sachaufgabe', 'Drei Zahlen haben', 'direkt')
ST.typ('sachaufgabe', '/^(Ein Sportverein|Im Zoo|Ein Kino)/', 'einkleidung')
ST.typ('sachaufgabe', 'In einer Spardose', 'pruefung')
ST.typ('sachaufgabe', '/^(Drei Kisten|1 kg Nussmischung)/', 'transfer')
ST.typ('sachaufgabe', '/^(In einem Dreieck|Von 26|Eine dreistellige)/', 'verknuepfen')
ST.neu('sachaufgabe', 'erkennen', A('Welche Gleichung passt zu: „Die zweite Zahl y ist um 3 größer als die erste Zahl x.“?', 'y = x + 3', ['x = y + 3', 'y = 3x', 'x + y = 3'],
       'Um 3 größer: Zur ersten Zahl kommt 3 dazu. Also y = x + 3.', 'Wer ist größer?'))
ST.neu('sachaufgabe', 'mehrschritt', Z('Für drei Zahlen gilt x + y + z = 15, x = 2y und z = y + 3. Wie groß ist z?', 6, '3 + 3',
       'Einsetzen: 2y + y + y + 3 = 15 ⇒ 4y = 12 ⇒ y = 3. Dann x = 6 und z = 6.', 'Drücke alles mit y aus.'))
ST.neu('sachaufgabe', 'umkehr', Z('Heft, Stift und Lineal kosten zusammen 6 €. Das Heft kostet 2 €, Stift und Lineal kosten gleich viel. Wie viel kostet der Stift?', 2, '(6 - 2) // 2',
       'h + s + l = 6, h = 2, s = l ⇒ 2s = 4 ⇒ s = 2 €.', 'Setze die bekannten Werte ein.', einheit='€'))
ST.neu('sachaufgabe', 'fehler', A('Jemand übersetzt „Die zweite Zahl y ist doppelt so groß wie die erste Zahl x“ mit x = 2y. Was stimmt?', 'Falsch: Es heißt y = 2x.', ['Richtig.', 'Falsch: Es heißt y = x + 2.', 'Falsch: Es heißt x + y = 2.'],
       'Die größere Zahl ist y. Doppelt so groß wie x heißt y = 2 · x. Probe mit x = 3: y = 6.', 'Probiere ein Zahlenbeispiel.'))
ST.knobel('sachaufgabe', Z('Drei Geschwister sind zusammen 30 Jahre alt. Vor 2 Jahren war die Älteste so alt wie die beiden anderen damals zusammen. Der Mittlere ist 4 Jahre älter als der Jüngste. Wie alt ist der Jüngste?', 6, '(16 - 4) // 2',
          'a + b + c = 30. Vor 2 Jahren: a − 2 = (b − 2) + (c − 2), also a = b + c − 2. Einsetzen: a = 30 − a − 2, a = 14. Dann b + c = 16 und b = c + 4, also c = 6.',
          'Achte darauf, dass vor 2 Jahren alle drei 2 Jahre jünger waren.'))
ST.knobel('sachaufgabe', Z('Für genau 100 € werden genau 100 Tiere gekauft: Kühe zu 10 €, Schweine zu 3 € und Hühner zu 0,50 €, von jeder Art mindestens eins. Wie viele Kühe sind es?', 5, '5',
          'k + s + h = 100 und 10k + 3s + 0,5h = 100, also 20k + 6s + h = 200. Abziehen: 19k + 5s = 100. 5s = 100 − 19k muss durch 5 teilbar sein, also auch 19k – das geht nur, wenn k durch 5 teilbar ist. k = 5 gibt 5s = 5, s = 1. k = 10 ist schon zu groß (190 > 100). Also k = 5, s = 1, h = 94. Probe: 50 + 3 + 47 = 100 €.',
          'Zwei Gleichungen, drei Unbekannte – aber nur ganze Zahlen sind erlaubt.'))

if __name__ == '__main__':
    stufen('gleichungen.lgs3', ST)


# ---- BEREINIGEN (Einundzwanzigste Runde) ----
if __name__ == '__main__':
    from _bereinigen import bereinigen_datei
    bereinigen_datei('gleichungen.lgs3')
# ---- BEREINIGEN ENDE ----
