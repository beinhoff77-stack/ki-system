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
               {'text': 'In (I): 1 − 2 + z = 2, also z = 3.'},
               {'text': 'Die Lösung: ⟦x = 1, y = −2, z = 3⟧.'}],
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

if __name__ == '__main__':
    bauen('gleichungen.lgs3',
          'Lineare Gleichungssysteme mit drei Unbekannten aufstellen und systematisch lösen, z. B. Parabel durch drei Punkte.',
          ['Lösung = Tripel, das alle drei Gleichungen erfüllt.', 'Additionsverfahren: Vielfache addieren/subtrahieren, bis eine Variable wegfällt.',
           'Zweimal dieselbe Variable eliminieren → System mit zwei Unbekannten.', 'Parabel durch drei Punkte: jeden Punkt in y = ax² + bx + c einsetzen.'],
          [('Grundlagen', ['pruefen', 'stufenform']), ('Lösungsverfahren', ['eliminieren', 'loesen']),
           ('Anwendungen', ['parabel', 'sachaufgabe'])],
          ETAPPEN, GEN,
          meiden={'parabel': ['(0 | 1), (1 | 2), (−1 | 4)']},
          offen=['Gleichungssysteme stehen im Fragetext in einer Zeile; bei „stufenform“ und „loesen“ zusätzlich untereinander als Tabelle (f.grafik). Bei den übrigen Karten noch einzeilig.',
                 'Sonderfälle (keine oder unendlich viele Lösungen) nur als Erkennen-Aufgabe in Stufe 3 von „loesen“ (Prüfvorschlag); die Erklärung der Karte nennt sie nicht ausdrücklich.'])
