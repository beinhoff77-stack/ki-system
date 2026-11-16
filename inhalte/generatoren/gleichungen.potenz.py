#!/usr/bin/env python3
"""Thema gleichungen.potenz – Potenzgleichungen xⁿ = c (Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(905)
HZ = HOCHZ
L2 = 'x₁ = □; x₂ = □'
H2 = 'kleinere Lösung zuerst'
GR = {2: 15, 3: 6, 4: 5, 5: 3, 6: 3, 7: 2, 8: 2}


def f2(x):
    """Zahl mit genau zwei Nachkommastellen (5,60)."""
    return format(float(x), '.2f').replace('-', '−').replace('.', ',')


def eur(x):
    """Geldbetrag mit zwei Nachkommastellen, Tausender gegliedert."""
    if Fr(x).denominator == 1: return dz(int(x))
    ganz, _, rest = format(float(x), '.2f').partition('.')
    return dz(int(ganz)) + ',' + rest


def xn(n, v='x'):
    return f'{v}{str(n).translate(HZ)}'


def wz(n, a):
    return f'√{a}' if n == 2 else f'{str(n).translate(HZ)}√{a}'


ETAPPEN = [
    {'lernziel': 'gerade', 'titel': 'xⁿ = c mit geradem Exponenten',
     'regel': 'n gerade: Für ⟦c > 0⟧ gibt es zwei Lösungen ⟦x = ±ⁿ√c⟧, für c = 0 nur x = 0, für ⟦c < 0 keine⟧ (gerade Potenzen sind nie negativ).',
     'schritte': ['x⁴ = 16: Welche Zahlen hoch 4 ergeben 16? 2⁴ = 16 und (−2)⁴ = 16.', 'Also ⟦x₁ = −2, x₂ = 2⟧.'],
     'probe': '(−2)⁴ = (−2)(−2)(−2)(−2) = 16 ✓',
     'fehler': 'x⁴ = 16 ⇒ x = 2 ist unvollständig: Bei geradem Exponenten ist auch ⟦−2⟧ eine Lösung.'},
    {'lernziel': 'ungerade', 'titel': 'xⁿ = c mit ungeradem Exponenten',
     'regel': 'n ungerade: Es gibt ⟦genau eine Lösung⟧. Für c ≥ 0 ist x = ⁿ√c, für ⟦c < 0⟧ ist x = ⟦−ⁿ√|c|⟧ (negativ).',
     'schritte': ['x³ = −125: Ungerader Exponent, c negativ.', 'x = −³√125 = ⟦−5⟧, denn (−5)³ = −125.'],
     'probe': '(−5) · (−5) · (−5) = 25 · (−5) = −125 ✓',
     'fehler': '„x³ = −125 hat keine Lösung“ ist falsch: Bei ⟦ungeradem⟧ Exponenten ergibt eine negative Zahl hoch n etwas Negatives. x = −5.'},
    {'lernziel': 'anzahl', 'titel': 'Lösungsanzahl begründen',
     'regel': 'Entscheidend sind ⟦n gerade oder ungerade⟧ und das ⟦Vorzeichen von c⟧. Zähle im Bild, wie oft die waagrechte Gerade y = c den Graphen trifft. y = x⁴ (gerade): Die Gerade y = 4 trifft ⟦zweimal⟧, die Gerade y = −2 ⟦nie⟧. y = x³ (ungerade): Jede waagrechte Gerade trifft ⟦genau einmal⟧.',
     'bild': {'typ': 'koordinaten', 'x': [-3, 3], 'y': [-4, 6], 'graphen': [{'art': 'potenz', 'a': 1, 'n': 4, 'name': 'x⁴'}, {'art': 'potenz', 'a': 1, 'n': 3, 'name': 'x³'}], 'waagrecht': [4, -2]},
     'schritte': ['x⁶ = −1: n = 6 ist gerade, x⁶ ist nie negativ.', 'Die Gerade y = −1 schneidet den Graphen von y = x⁶ nicht: ⟦keine Lösung⟧.'],
     'probe': 'x⁶ = (x³)² ≥ 0 für jedes x ✓',
     'fehler': '„x⁵ = 32 hat zwei Lösungen 2 und −2“ ist falsch: (−2)⁵ = ⟦−32⟧. Bei ungeradem Exponenten gibt es nur eine Lösung.'},
    {'lernziel': 'umformen', 'titel': 'Erst umformen, dann Wurzel ziehen',
     'regel': 'Bringe die Gleichung auf die Form ⟦(…)ⁿ = c⟧. Steht eine Klammer hoch n, löst du zuerst nach der ⟦Klammer⟧ auf.',
     'schritte': ['2x³ + 7 = 61 | − 7, : 2 ergibt x³ = 27.', 'x = ³√27 = ⟦3⟧.'],
     'probe': '2 · 27 + 7 = 61 ✓',
     'fehler': '2x³ = 54 ⇒ x³ = 54 − 2 ist falsch: Die 2 ist ein ⟦Faktor⟧, also wird ⟦geteilt⟧: x³ = 27.'},
    {'lernziel': 'naeherung', 'titel': 'Lösungen mit dem Taschenrechner',
     'regel': 'Ist c keine „glatte“ Potenz, bestimmst du ⁿ√c mit dem ⟦Taschenrechner⟧ und ⟦rundest⟧ sinnvoll. Vorzeichen-Regeln gelten wie sonst.',
     'schritte': ['x³ = 40: genau eine Lösung x = ³√40.', 'Taschenrechner: ³√40 ≈ 3,42 (auf zwei Nachkommastellen ⟦x ≈ 3,42⟧).'],
     'probe': '3,42³ ≈ 40,0 ✓',
     'fehler': 'x³ = 40 ⇒ x = 40 : 3 ≈ 13,33 ist falsch: Die Probe zeigt 13,33³ ≈ 2 370. Man muss die ⟦dritte Wurzel⟧ ziehen.'},
    {'lernziel': 'sachaufgabe', 'titel': 'Sachaufgaben mit Potenzgleichungen',
     'regel': 'Stelle eine Gleichung der Form ⟦xⁿ = c⟧ auf (Würfel: a³ = V, Wachstum: q² = Faktor) und prüfe, welche Lösung ⟦im Sachzusammenhang⟧ passt.',
     'schritte': ['Ein Würfel hat das Volumen 216 cm³: a³ = 216.', 'a = ³√216 = ⟦6⟧, die Kante ist 6 cm lang.'],
     'probe': '6 cm · 6 cm · 6 cm = 216 cm³ ✓',
     'fehler': 'Bei a² = 49 für eine Seitenlänge a = −7 cm anzugeben ist falsch: Längen sind ⟦positiv⟧, nur a = 7 cm passt.'},
]

# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'gerade': {
  'einstieg': 'Ein Zahlenautomat nimmt jede eingegebene Zahl viermal mit sich selbst mal. Heraus kommt 16. Welche Zahl wurde eingegeben? 2 passt, denn 2 · 2 · 2 · 2 = 16. Aber auch −2 passt, weil sich vier Minuszeichen paarweise aufheben. Eine Gleichung wie x⁴ = 16 heißt ⟦Potenzgleichung⟧.',
  'woerter': [['x⁴', 'x · x · x · x'],
              ['Exponent n', 'die Hochzahl: wie oft malgenommen wird'],
              ['gerade / ungerade', 'gerade: 2, 4, 6, …; ungerade: 1, 3, 5, …'],
              ['ⁿ√c', 'die n-te Wurzel: die Zahl ohne Minus, die hoch n genau c ergibt'],
              ['x₁, x₂', 'die erste und die zweite Lösung']],
  'schritte': ['Die Gleichung heißt x⁴ = 16. Der Exponent 4 ist gerade.',
               'Suche zuerst die Zahl ohne Minus: ⁴√16 = 2, denn 2 · 2 · 2 · 2 = 16.',
               'Bei geradem Exponenten passt auch die Gegenzahl: (−2) · (−2) · (−2) · (−2) = 16, weil sich die Minuszeichen paarweise aufheben.',
               'Also sind die Lösungen ⟦x₁ = −2 und x₂ = 2⟧.'],
  'regel': 'So löst du xⁿ = c mit ⟦geradem⟧ n: Ist ⟦c > 0⟧, gibt es zwei Lösungen ⟦x = ⁿ√c und x = −ⁿ√c⟧. Ist c = 0, nur x = 0. Ist ⟦c < 0⟧, gibt es ⟦keine⟧ Lösung, denn gerade Potenzen sind nie negativ.',
  'fehler': 'x⁴ = 16 ⇒ x = 2 ist unvollständig: Der Automat liefert auch für −2 die 16. Bei geradem Exponenten ist auch ⟦−2⟧ eine Lösung.'},
 'ungerade': {
  'einstieg': 'Ein zweiter Automat nimmt jede Zahl dreimal mit sich selbst mal. Heraus kommt −125. Mit einer positiven Zahl geht das nicht. Aber (−5) · (−5) · (−5) = −125: Zwei Minuszeichen heben sich auf, das dritte bleibt. Bei ⟦ungeradem Exponenten⟧ gibt es deshalb immer genau eine Lösung – auch bei negativen Ergebnissen.',
  'woerter': [['x³', 'x · x · x'],
              ['|c|', 'der Betrag: c ohne Vorzeichen, z. B. |−125| = 125'],
              ['−³√125', 'minus die dritte Wurzel aus 125, also −5']],
  'schritte': ['Die Gleichung heißt x³ = −125. Der Exponent 3 ist ungerade, rechts steht eine negative Zahl.',
               'Ohne das Minus gerechnet: ³√125 = 5, denn 5 · 5 · 5 = 125.',
               'Das Minus bleibt erhalten: (−5) · (−5) · (−5) = 25 · (−5) = −125.',
               'Also gibt es genau eine Lösung: ⟦x = −5⟧.'],
  'regel': 'So löst du xⁿ = c mit ⟦ungeradem⟧ n: Es gibt ⟦genau eine Lösung⟧. Für c ≥ 0 ist x = ⁿ√c; für ⟦c < 0⟧ ist x = ⟦−ⁿ√|c|⟧, also negativ.',
  'fehler': '„x³ = −125 hat keine Lösung“ ist falsch: Bei ⟦ungeradem⟧ Exponenten ergibt eine negative Zahl hoch n wieder etwas Negatives. Der Automat liefert −125 für x = −5.'},
 'anzahl': {
  'einstieg': 'Wie viele Zahlen passen zu einem Ergebnis? Das zeigt ein Bild. Man zeichnet die Kurve des Automaten und eine waagrechte Linie in der Höhe des Ergebnisses. Jeder Treffpunkt ist eine Lösung. So lässt sich die ⟦Anzahl der Lösungen⟧ abzählen.',
  'woerter': [['Graph von y = x⁴', 'die Kurve aller Punkte (x | x⁴)'],
              ['waagrechte Gerade y = c', 'eine Linie auf der Höhe c'],
              ['treffen / schneiden', 'Kurve und Linie haben dort einen gemeinsamen Punkt']],
  'bild': {'typ': 'koordinaten', 'x': [-3, 3], 'y': [-4, 6], 'graphen': [{'art': 'potenz', 'a': 1, 'n': 4, 'name': 'y = x⁴'}, {'art': 'potenz', 'a': 1, 'n': 3, 'name': 'y = x³'}], 'waagrecht': [4, -2]},
  'schritte': ['Die Gleichung heißt x⁶ = −1. Der Exponent 6 ist gerade.',
               'Eine gerade Potenz ist nie negativ: Auch (−1)⁶ = 1, weil sich die Minuszeichen paarweise aufheben.',
               'Im Bild heißt das: Die Kurve von y = x⁶ liegt nie unter der x-Achse, die Linie y = −1 aber schon.',
               'Die Linie trifft die Kurve nie: ⟦keine Lösung⟧.'],
  'regel': 'So bestimmst du die ⟦Anzahl der Lösungen⟧ von xⁿ = c: Achte auf ⟦n gerade oder ungerade⟧ und auf das ⟦Vorzeichen von c⟧. Im Bild zählst du, wie oft die Gerade y = c den Graphen trifft: bei geradem n und c > 0 ⟦zweimal⟧, bei c < 0 ⟦nie⟧, bei ungeradem n immer ⟦genau einmal⟧.',
  'fehler': '„x⁵ = 32 hat zwei Lösungen 2 und −2“ ist falsch: (−2)⁵ = ⟦−32⟧, denn bei fünf Minuszeichen bleibt eines übrig. Bei ungeradem Exponenten gibt es nur eine Lösung.'},
 'umformen': {
  'einstieg': 'Manchmal steckt die Potenz in einer längeren Rechnung: Der Automat nimmt die Zahl hoch 3, verdoppelt das Ergebnis und zählt 7 dazu. Heraus kommt 61. Um die Eingabe zu finden, geht man rückwärts: erst die 7 abziehen, dann halbieren, dann die dritte Wurzel ziehen. Das heißt ⟦umformen⟧.',
  'woerter': [['umformen', 'auf beiden Seiten dasselbe rechnen, damit die Gleichung wahr bleibt'],
              ['| − 7', 'Hinweis am Rand: auf beiden Seiten 7 abziehen'],
              ['Faktor', 'eine Zahl, mit der malgenommen wird, z. B. die 2 in 2x³'],
              ['(x − 1)³', 'die ganze Klammer hoch 3']],
  'schritte': ['Die Gleichung heißt 2x³ + 7 = 61.',
               'Auf beiden Seiten 7 abziehen: 2x³ = 54.',
               'Beide Seiten durch 2 teilen: x³ = 27.',
               'Die dritte Wurzel ziehen: x = ³√27 = ⟦3⟧, denn 3 · 3 · 3 = 27.'],
  'regel': 'So gehst du vor: Bring die Gleichung auf die Form ⟦(…)ⁿ = c⟧ – erst Zahlen abziehen oder dazuzählen, dann durch den Faktor teilen. Steht eine Klammer hoch n da, löst du zuerst nach der ⟦Klammer⟧ auf.',
  'fehler': '2x³ = 54 ⇒ x³ = 54 − 2 ist falsch: Die 2 ist ein ⟦Faktor⟧, also wird ⟦geteilt⟧: x³ = 27. Verdoppeln macht man durch Halbieren rückgängig, nicht durch Abziehen.'},
 'naeherung': {
  'einstieg': 'Nicht immer kommt eine glatte Zahl heraus. Ein würfelförmiger Behälter soll 40 Liter fassen. Mit 3 dm Kante fasst er 27 Liter, mit 4 dm schon 64 Liter. Die passende Kante liegt dazwischen; der Taschenrechner liefert sie auf ein paar Stellen genau. Das Ergebnis wird dann ⟦gerundet⟧.',
  'woerter': [['Liter', '1 Liter = 1 dm³, ein Würfel mit 10 cm Kante'],
              ['runden', 'auf weniger Stellen kürzen, z. B. 3,419… auf zwei Nachkommastellen: 3,42'],
              ['≈', '„ungefähr gleich“ – nach dem Runden'],
              ['³√-Taste', 'die Taste für die dritte Wurzel auf dem Taschenrechner']],
  'schritte': ['Die Gleichung heißt x³ = 40. Der Exponent ist ungerade, also gibt es genau eine Lösung: x = ³√40.',
               'Grob schätzen: 3³ = 27 und 4³ = 64, also liegt x zwischen 3 und 4.',
               'Taschenrechner: ³√40 = 3,419…',
               'Auf zwei Nachkommastellen gerundet: ⟦x ≈ 3,42⟧. Die Kante ist also etwa 3,42 dm lang.'],
  'regel': 'So gehst du vor, wenn es nicht glatt aufgeht: ⁿ√c mit dem ⟦Taschenrechner⟧ bestimmen und sinnvoll ⟦runden⟧. Die Vorzeichen-Regeln (gerade: zwei Lösungen ±, ungerade: eine Lösung) gelten wie sonst. Vorher grob schätzen hilft, Tippfehler zu erkennen.',
  'fehler': 'x³ = 40 ⇒ x = 40 : 3 ≈ 13,33 ist falsch: Die Probe zeigt 13,33³ ≈ 2 370 – ein Behälter mit über 2 000 Litern. Man muss die ⟦dritte Wurzel⟧ ziehen.'},
 'sachaufgabe': {
  'einstieg': 'Ein Geschenkkarton in Würfelform soll 216 cm³ fassen. Wie lang muss eine Kante sein? Das Volumen eines Würfels ist Kante mal Kante mal Kante. Gesucht ist also die Zahl, die hoch 3 genau 216 ergibt. Solche Fragen aus dem Alltag heißen ⟦Sachaufgaben⟧.',
  'woerter': [['Volumen V', 'der Rauminhalt, hier in cm³'],
              ['a³ = V', 'Kante hoch 3 ergibt das Volumen'],
              ['Wachstumsfaktor q', 'die Zahl, mit der in jedem Jahr malgenommen wird'],
              ['Sachzusammenhang', 'die Situation, zu der die Lösung passen muss']],
  'schritte': ['Variable festlegen: a ist die Kante in cm.',
               'Gleichung aufstellen: a · a · a = 216, also a³ = 216.',
               'Lösen: a = ³√216 = 6, denn 6 · 6 · 6 = 216.',
               'Prüfen: Eine Kante von ⟦6 cm⟧ ist positiv und passt zum Karton.'],
  'regel': 'So löst du eine Sachaufgabe mit Potenzen: Stelle eine Gleichung der Form ⟦xⁿ = c⟧ auf (Würfel: a³ = V; Wachstum über zwei Jahre: q² = Gesamtfaktor) und prüfe, welche Lösung ⟦zum Sachzusammenhang⟧ passt.',
  'fehler': 'Bei a² = 49 für eine Seitenlänge a = −7 cm anzugeben ist falsch: Längen sind ⟦positiv⟧, nur a = 7 cm passt.'},
}
klar(ETAPPEN, KLAR)
# ---- KLAR ENDE ----
# ---- UMBAU (neues Muster, Runde 8, Vorgabe 16.11.) ----
UMBAU = {
 'gerade': {
  'einstieg': 'Ein Zahlenautomat nimmt jede Zahl viermal mit sich selbst mal. Heraus kommt 16. Welche Zahl kam hinein? Das fragt eine ⟦Potenzgleichung⟧: x⁴ = 16.',
  'woerter': [['Potenzgleichung', 'eine Gleichung wie x⁴ = 16, in der x hoch eine Zahl steht'],
              ['Exponent', 'die Hochzahl, hier 4'],
              ['x⁴', 'x · x · x · x']],
  'bild': {'typ': 'koordinaten', 'x': [-3, 3], 'y': [-2, 20], 'schritt_y': 4,
           'graphen': [{'art': 'potenz', 'a': 1, 'n': 4, 'name': 'y = x⁴'}], 'waagrecht': [16]},
  'schritte': [{'text': 'Gesucht ist x mit x⁴ = 16. Der Exponent 4 ist gerade.'},
               {'text': '2 · 2 · 2 · 2 = 16, also passt 2.', 'bild': {'punkte': [{'x': 2, 'y': 16, 'name': '2'}]}},
               {'text': 'Auch (−2)⁴ = 16, denn die Minuszeichen heben sich paarweise auf.',
                'bild': {'punkte': [{'x': -2, 'y': 16, 'name': '−2'}, {'x': 2, 'y': 16, 'name': '2'}]}},
               {'text': 'Also ⟦x₁ = −2 und x₂ = 2⟧.'}],
  'fehler': 'x⁴ = 16 ⇒ x = 2 ist unvollständig. Der Automat liefert auch für −2 die 16.',
  'fehler_bild': {'punkte': [{'x': 2, 'y': 16, 'name': '2'}, {'x': -2, 'y': 16, 'name': '−2 vergessen', 'offen': True}]},
  'regel': 'Gerader Exponent, c > 0: ⟦zwei Lösungen⟧ ⁿ√c und −ⁿ√c. Für c < 0 gibt es keine Lösung.'},
 'ungerade': {
  'einstieg': 'Ein zweiter Automat nimmt jede Zahl dreimal mit sich selbst mal. Heraus kommt −125. Das geht mit einer negativen Zahl, weil der ⟦Exponent ungerade⟧ ist.',
  'woerter': [['ungerade', '1, 3, 5, 7, … – nicht durch 2 teilbar'],
              ['x³', 'x · x · x']],
  'bild': {'typ': 'koordinaten', 'x': [-6, 6], 'y': [-150, 150], 'schritt_y': 50,
           'graphen': [{'art': 'potenz', 'a': 1, 'n': 3, 'name': 'y = x³'}], 'waagrecht': [-125]},
  'schritte': [{'text': 'Die Gleichung heißt x³ = −125. Der Exponent 3 ist ungerade.'},
               {'text': 'Ohne Minus: ³√125 = 5, denn 5 · 5 · 5 = 125.'},
               {'text': 'Mit Minus: (−5) · (−5) · (−5) = −125. Ein Minus bleibt übrig.'},
               {'text': 'Es gibt genau eine Lösung: ⟦x = −5⟧.', 'bild': {'punkte': [{'x': -5, 'y': -125, 'name': '−5'}]}}],
  'fehler': '„x³ = −125 hat keine Lösung“ ist falsch. Bei ungeradem Exponenten bleibt das Minus erhalten: x = −5.',
  'regel': 'Ungerader Exponent: immer ⟦genau eine Lösung⟧. Für c < 0 ist sie negativ, hier −5.'},
 'anzahl': {
  'einstieg': 'Wie viele Zahlen passen zu einem Ergebnis? Zeichne die Kurve des Automaten und eine waagrechte Linie in Höhe des Ergebnisses. Jeder Treffpunkt ist eine ⟦Lösung⟧.',
  'woerter': [['Graph', 'die Kurve aller Punkte (x | x⁶)'],
              ['waagrechte Linie', 'eine Linie auf gleicher Höhe, hier y = −1']],
  'bild': {'typ': 'koordinaten', 'x': [-2, 2], 'y': [-3, 5], 'graphen': [{'art': 'potenz', 'a': 1, 'n': 6, 'name': 'y = x⁶'}]},
  'schritte': [{'text': 'Die Gleichung heißt x⁶ = −1. Der Exponent 6 ist gerade.'},
               {'text': 'Gerade Potenzen sind nie negativ. Der Graph bleibt oberhalb von −1.'},
               {'text': 'Die waagrechte Linie y = −1 trifft den Graph nie.', 'bild': {'waagrecht': [-1]}},
               {'text': 'Also hat x⁶ = −1 ⟦keine Lösung⟧.'}],
  'fehler': 'x⁵ = 32 hat nicht zwei Lösungen. (−2)⁵ = −32, denn ein Minus bleibt übrig. Nur x = 2 passt.',
  'fehler_bild': {'typ': 'koordinaten', 'x': [-3, 3], 'y': [-40, 40], 'schritt_y': 10,
                  'graphen': [{'art': 'potenz', 'a': 1, 'n': 5, 'name': 'y = x⁵'}], 'waagrecht': [32],
                  'punkte': [{'x': 2, 'y': 32, 'name': '2'}, {'x': -2, 'y': -32, 'name': '(−2)⁵ = −32'}]},
  'regel': 'Zähle die Treffer der Linie y = c mit dem Graph. Gerader Exponent: zwei, eine oder keine; ungerader: ⟦genau eine⟧.'},
 'umformen': {
  'einstieg': 'Ein Automat nimmt hoch 3, verdoppelt und zählt 7 dazu. Heraus kommt 61. Rückwärts rechnest du die Eingabe aus: Das heißt ⟦umformen⟧.',
  'woerter': [['umformen', 'auf beiden Seiten dasselbe rechnen, damit die Gleichung wahr bleibt'],
              ['Faktor', 'eine Zahl, mit der malgenommen wird, z. B. die 2 in 2x³']],
  'bild': {'typ': 'tabelle', 'kopf': ['Automat', 'rückwärts'], 'zeilen': [['plus 7', '?'], ['mal 2', '?'], ['hoch 3', '?']]},
  'schritte': [{'text': '2x³ + 7 = 61. Zuerst 7 abziehen: 2x³ = 54.',
                'bild': {'zeilen': [['plus 7', 'minus 7: 54'], ['mal 2', '?'], ['hoch 3', '?']]}},
               {'text': 'Die 2 ist ein Faktor. Also durch 2 teilen: x³ = 27.',
                'bild': {'zeilen': [['plus 7', 'minus 7: 54'], ['mal 2', 'durch 2: 27'], ['hoch 3', '?']]}},
               {'text': 'Dritte Wurzel ziehen: x = ³√27 = ⟦3⟧.',
                'bild': {'zeilen': [['plus 7', 'minus 7: 54'], ['mal 2', 'durch 2: 27'], ['hoch 3', '³√: 3']]}}],
  'fehler': '2x³ = 54 ⇒ x³ = 54 − 2 ist falsch. Verdoppeln macht man durch Halbieren rückgängig: x³ = 27.',
  'fehler_bild': {'zeilen': [['plus 7', 'minus 7: 54'], ['mal 2', 'minus 2? falsch'], ['hoch 3', '?']]},
  'regel': 'Rechne ⟦rückwärts⟧, bis xⁿ = c dasteht. Erst Zahlen abziehen, dann durch den Faktor teilen, dann die Wurzel ziehen.'},
 'naeherung': {
  'einstieg': 'Ein würfelförmiger Behälter soll 40 Liter fassen. 3 dm Kante ergeben 27 Liter, 4 dm schon 64 Liter. Die Kante liegt dazwischen und wird ⟦gerundet⟧.',
  'woerter': [['Liter', '1 Liter = 1 dm³, ein Würfel mit 10 cm Kante'],
              ['runden', 'auf weniger Stellen kürzen: 3,419… wird 3,42'],
              ['≈', 'ungefähr gleich']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 5, 'abschnitte': 10, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': 'x³ = 40 hat genau eine Lösung: x = ³√40.'},
               {'text': 'Schätzen: 3³ = 27 und 4³ = 64. Also liegt x zwischen 3 und 4.',
                'bild': {'bereich': {'von': 3, 'bis': 4}}},
               {'text': 'Der Taschenrechner zeigt ³√40 = 3,419… an.'},
               {'text': 'Auf zwei Stellen runden: ⟦x ≈ 3,42⟧. So viele dm ist die Kante lang.',
                'bild': {'punkte': [{'wert': 3.42, 'name': '3,42'}]}}],
  'fehler': 'x = 40 : 3 ≈ 13,33 ist falsch. Ein Behälter mit 13,33 dm Kante fasst rund 2 370 Liter.',
  'fehler_bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 15, 'abschnitte': 15, 'beschriftet': 'anfang_ende',
                  'punkte': [{'wert': 3.42, 'name': '3,42'}, {'wert': 13.33, 'name': '13,33?'}]},
  'regel': 'Bestimme ⁿ√c mit dem Taschenrechner und ⟦runde⟧ sinnvoll. Vorher grob schätzen, um Tippfehler zu erkennen.'},
 'sachaufgabe': {
  'einstieg': 'Ein würfelförmiger Geschenkkarton soll 216 cm³ fassen. Wie lang ist eine Kante? Das ist eine ⟦Sachaufgabe⟧ mit einer Potenzgleichung.',
  'woerter': [['Sachaufgabe', 'eine Rechenaufgabe aus dem Alltag'],
              ['Volumen', 'der Rauminhalt, hier in cm³'],
              ['Sachzusammenhang', 'die Situation, zu der die Lösung passen muss']],
  'bild': {'typ': 'tabelle', 'kopf': ['Kante a', '5 cm', '6 cm', '7 cm'], 'zeilen': [['Volumen', '125 cm³', '?', '343 cm³']]},
  'schritte': [{'text': 'a ist die Kante in cm. Das Volumen ist a · a · a.'},
               {'text': 'Die Gleichung heißt a³ = 216.'},
               {'text': '6 · 6 · 6 = 216, also ⟦a = 6 cm⟧.', 'bild': {'zeilen': [['Volumen', '125 cm³', '216 cm³', '343 cm³']]}},
               {'text': 'Sachzusammenhang: 6 cm ist positiv und passt zum Karton.'}],
  'fehler': 'Bei a² = 49 ist a = −7 cm falsch. Eine Kante ist nie negativ. Nur 7 cm passt.',
  'regel': 'Stelle eine Gleichung ⟦xⁿ = c⟧ auf und löse sie. Behalte nur Lösungen, die zum Sachzusammenhang passen.'},
}
umbau(ETAPPEN, UMBAU)
# ---- UMBAU ENDE ----


def g_gerade(s):
    if s == 1:
        n, r = 2, R.randint(1, 15)
    elif s == 2:
        if R.random() < 0.3:
            k, m = R.randint(2, 6), R.choice([2, 3, 5, 6, 7])
            c = k * k * m
            return auswahl(f'Löse x² = {c}. Gib die Lösungen exakt an.', f'x = ±{k}√{m}',
                           [f'x = {k}√{m}', f'x = ±{dz(Fr(c, 2)) if c % 2 == 0 else c}', f'x = ±√{k * m}'],
                           f'x = ±√{c} = ±√({k * k} · {m}) = ±{k}√{m}. Bei x² gibt es zwei Lösungen.',
                           'Ziehe teilweise die Wurzel und denke an beide Vorzeichen.')
        n = R.choice([4, 6])
        r = R.randint(2, GR[n])
    else:
        n = R.choice([2, 4, 6, 8])
        r = R.randint(2, GR[n])
        c = r ** n
        typ = R.random()
        if typ < 0.3:
            return auswahl(f'Welche Lösungsmenge hat {xn(n)} = −{dz(c)}?', 'L = { }', [f'L = {{−{r}}}', f'L = {{−{r}; {r}}}', f'L = {{{r}}}'],
                           f'n = {n} ist gerade, {xn(n)} ist nie negativ. Keine Lösung.', 'Kann eine gerade Potenz negativ sein?')
        if typ < 0.45:
            a = R.randint(2, 5)
            return auswahl(f'Welche Lösungsmenge hat {a}{xn(n)} = 0?', 'L = {0}', ['L = { }', f'L = {{−{a}; {a}}}', 'L = {0; 1}'],
                           f'{xn(n)} = 0, und nur 0 hoch {n} ergibt 0.', 'Welche Zahl hoch n ergibt 0?')
        if typ < 0.75:
            return auswahl(f'Jemand löst {xn(n)} = {dz(c)} mit x = {r}. Was stimmt?', f'Unvollständig: Auch −{r} ist Lösung, denn (−{r}){str(n).translate(HZ)} = {dz(c)}.',
                           ['Richtig, das ist die einzige Lösung.', f'Falsch: Richtig ist nur x = −{r}.', 'Falsch: Es gibt keine Lösung.'],
                           f'Gerader Exponent, c > 0: zwei Lösungen ±{r}.', 'Mache die Probe mit der Gegenzahl.')
        return auswahl(f'Jemand löst {xn(n)} = −{dz(c)} mit x = ±{r}. Was stimmt?', f'Falsch: Keine Lösung, denn {xn(n)} ist nie negativ; (±{r}){str(n).translate(HZ)} = {dz(c)}.',
                       ['Richtig, wie bei positiven Zahlen.', f'Falsch: Nur x = −{r} ist Lösung.', f'Falsch: Nur x = {r} ist Lösung.'],
                       f'Bei geradem Exponenten ist jede Potenz ≥ 0. Probe: (−{r}){str(n).translate(HZ)} = {dz(c)} ≠ −{dz(c)}.',
                       'Mache die Probe mit beiden Zahlen.')
    c = r ** n
    form = R.choice([f'Löse {xn(n)} = {dz(c)}.', f'Löse {xn(n)} − {dz(c)} = 0.', f'Bestimme alle Lösungen von {dz(c)} = {xn(n)}.'])
    return luecken(form, L2, H2, [-r, r], f'n = {n} gerade, c > 0: x = ±{wz(n, dz(c))} = ±{r}.',
                   'Gerader Exponent: Denke an beide Vorzeichen.', c=[f'-({c} / {r} ** {n - 1})', f'{c} / {r} ** {n - 1}'])


def g_ungerade(s):
    if s == 3:
        n = R.choice([3, 5])
        if R.random() < 0.5:
            z = -Fr(R.randint(1, 9), 10) if n == 3 else -Fr(R.randint(1, 5), 10)
            if R.random() < 0.4: z = -Fr(R.choice([1, 3]), 2)
            c = z ** n
            return zahl(f'Löse {xn(n)} = {dz(c)}.', f'n = {n} ungerade: genau eine Lösung, negativ: x = {dz(z)}, denn ({dz(z)}){str(n).translate(HZ)} = {dz(c)}.',
                        'Ungerader Exponent: Vorzeichen bleibt erhalten. Ziehe die Wurzel ohne Komma.', z, f'{float(c)} / ({float(z)}) ** {n - 1}')
        p, k = nz9(), R.choice([-4, -3, -2, 2, 3, 4])
        return zahl(f'Löse {minus_klammer(p)}{str(n).translate(HZ)} = {dz(k ** n)}.' if n == 3 or abs(k) <= 3 else None,
                    f'{minus_klammer(p)[1:-1]} = {dz(k)}, denn ({dz(k)}){str(n).translate(HZ)} = {dz(k ** n)}. Also x = {dz(p + k)}.',
                    'Löse zuerst nach der Klammer auf.', p + k, f'{p} + ({k ** n}) / ({k}) ** {n - 1}') if (n == 3 or abs(k) <= 3) else None
    n = 3 if s == 1 else R.choice([3, 5]) if s == 2 else R.choice([3, 5, 7])
    r = R.randint(1, 10 if n == 3 and s > 1 else GR[n])
    neg = s > 1 and R.random() < 0.6 or s == 1 and R.random() < 0.3
    c = -(r ** n) if neg else r ** n
    x = -r if neg else r
    if s > 1 and R.random() < 0.3:
        z = Fr(R.randint(1, 4), 10) * (-1 if neg else 1)
        c = z ** n
        return zahl(f'Löse {xn(n)} = {dz(c)}.', f'n = {n} ungerade: genau eine Lösung x = {dz(z)}, denn {kl(z)}{str(n).translate(HZ)} = {dz(c)}.',
                    'Ungerader Exponent: Vorzeichen bleibt erhalten. Achte auf die Nachkommastellen.', z, f'{float(c)} / ({float(z)}) ** {n - 1}')
    return zahl(f'Löse {xn(n)} = {dz(c)}.',
                f'n = {n} ungerade: genau eine Lösung x = {"−" if neg else ""}{wz(n, dz(abs(c)))} = {dz(x)}.',
                'Ungerader Exponent: Das Vorzeichen von c bleibt erhalten.', x, f'({c}) / ({x}) ** {n - 1}')


def g_anzahl(s):
    n = R.randint(2, 9)
    r = R.randint(1, 4 if n < 6 else 2)
    c = R.choice([r ** n, -(r ** n), 0]) if s > 1 else R.choice([r ** n, -(r ** n)])
    if n % 2 == 0:
        k = 2 if c > 0 else 1 if c == 0 else 0
    else:
        k = 1
    txt = {0: 'keine Lösung', 1: 'genau eine Lösung', 2: 'zwei Lösungen'}
    grund = (f'n = {n} ist {"gerade" if n % 2 == 0 else "ungerade"}' +
             (f' und c {"> 0" if c > 0 else "= 0" if c == 0 else "< 0"}' if n % 2 == 0 else '') + f': {txt[k]}.')
    if s < 3:
        if s == 2 and R.random() < 0.4:
            n = R.choice([2, 3, 4, 5])
            c = R.choice([v for v in range(-3, 5) if v])
            k = (2 if c > 0 else 0) if n % 2 == 0 else 1
            a_ = auswahl(f'Im Bild siehst du den Graphen von y = {xn(n)} und die Gerade y = {dz(c)}. Wie viele Lösungen hat {xn(n)} = {dz(c)}?',
                         txt[k], list(txt.values()),
                         f'Die Gerade y = {dz(c)} trifft den Graphen {"zweimal" if k == 2 else "einmal" if k == 1 else "nie"}: {txt[k]}.',
                         'Zähle die Schnittpunkte der Geraden mit dem Graphen.')
            return bild(a_, {'typ': 'koordinaten', 'x': [-3, 3], 'y': [-4, 6],
                             'graphen': [{'art': 'potenz', 'a': 1, 'n': n, 'name': f'y = {xn(n)}'}], 'waagrecht': [c]})
        return auswahl(f'Wie viele Lösungen hat {xn(n)} = {dz(c)}?', txt[k], list(txt.values()), grund,
                       'Ist der Exponent gerade oder ungerade? Welches Vorzeichen hat c?')
    typ = R.random()
    if typ < 0.35:
        n = R.choice([3, 5, 7])
        r = R.randint(2, GR[n])
        return auswahl(f'Jemand sagt: „{xn(n)} = {dz(r ** n)} hat die Lösungen {r} und −{r}.“ Was stimmt?',
                       f'Falsch: (−{r}){str(n).translate(HZ)} = −{dz(r ** n)}, nur x = {r} ist Lösung.',
                       ['Richtig, wie bei x² gibt es zwei Lösungen.', f'Falsch: Es gibt keine Lösung.', f'Falsch: Nur x = −{r} ist Lösung.'],
                       f'Bei ungeradem Exponenten wird eine negative Zahl hoch {n} negativ. Probe: (−{r}){str(n).translate(HZ)} = −{dz(r ** n)} ≠ {dz(r ** n)}.',
                       'Mache die Probe mit der negativen Zahl.')
    if typ < 0.7:
        n = R.choice([3, 5, 7])
        r = R.randint(2, GR[n])
        return auswahl(f'Jemand sagt: „{xn(n)} = −{dz(r ** n)} hat keine Lösung, weil man aus negativen Zahlen keine Wurzel ziehen kann.“ Was stimmt?',
                       f'Falsch: x = −{r} ist Lösung, denn (−{r}){str(n).translate(HZ)} = −{dz(r ** n)}.',
                       ['Richtig, negative Radikanden sind verboten.', f'Falsch: x = {r} ist Lösung.', f'Falsch: Es gibt zwei Lösungen ±{r}.'],
                       f'Bei ungeradem Exponenten gibt es immer genau eine Lösung. Hier x = −{wz(n, dz(r ** n))} = −{r}.',
                       'Prüfe, ob eine negative Zahl die Gleichung erfüllt.')
    n = R.choice([4, 6, 8])
    d = R.randint(1, 20)
    return auswahl(f'Für welche Werte von c hat {xn(n)} = c genau zwei Lösungen?', 'für alle c > 0',
                   ['für alle c', 'für alle c ≥ 0', 'für alle c < 0'],
                   f'n = {n} gerade: Für c > 0 schneidet y = c den Graphen zweimal (z. B. c = {d}), für c = 0 einmal, für c < 0 nie.',
                   'Denke an den Graphen von y = x' + str(n).translate(HZ) + ' und waagrechte Geraden.')


def g_umformen(s):
    if s == 1:
        n = R.choice([2, 3])
        a, r = R.randint(2, 6), R.randint(2, GR[n] if n == 3 else 10)
        if n == 2:
            return luecken(f'Löse {a}x² = {dz(a * r * r)}.', L2, H2, [-r, r], f'x² = {dz(a * r * r)} : {a} = {r * r}, x = ±{r}.',
                           'Teile zuerst durch den Faktor vor x².', c=[f'-({a * r * r} / {a}) / {r}', f'({a * r * r} / {a}) / {r}'])
        return zahl(f'Löse {a}x³ = {dz(a * r ** 3)}.', f'x³ = {dz(a * r ** 3)} : {a} = {r ** 3}, x = {r}.',
                    'Teile zuerst durch den Faktor vor x³.', r, f'({a * r ** 3} / {a}) / {r} ** 2')
    if s == 2:
        n = R.choice([3, 4, 5])
        r = R.randint(1, GR[n])
        a, b = R.randint(2, 5), nz9()
        neg = n % 2 == 1 and R.random() < 0.5
        x = -r if neg else r
        rechts = a * x ** n + b
        t = f'Löse {a}{xn(n)} {plus(b)} = {dz(rechts)}.'
        w = f'{a}{xn(n)} = {dz(rechts - b)} ⇒ {xn(n)} = {dz(x ** n)}'
        if n % 2 == 0:
            return luecken(t, L2, H2, [-r, r], w + f' ⇒ x = ±{r}.', 'Erst die Zahl, dann den Faktor auf die andere Seite bringen.',
                           c=[f'-(({rechts} - ({b})) / {a}) / {r} ** {n - 1}', f'(({rechts} - ({b})) / {a}) / {r} ** {n - 1}'])
        return zahl(t, w + f' ⇒ x = {dz(x)}.', 'Erst die Zahl, dann den Faktor auf die andere Seite bringen.', x,
                    f'(({rechts} - ({b})) / {a}) / ({x}) ** {n - 1}')
    n = R.choice([2, 3, 4])
    p, r = nz9(), R.randint(1, 4 if n > 2 else 9)
    if n == 3 and R.random() < 0.4:
        a, k = R.randint(2, 4), R.choice([-4, -3, -2, 2, 3, 4])
        return zahl(f'Löse {a}{minus_klammer(p)}³ = {dz(a * k ** 3)}.', f'Erst durch {a}: {minus_klammer(p)}³ = {dz(k ** 3)}. Klammer = {dz(k)}, also x = {dz(p + k)}.',
                    'Teile zuerst durch den Faktor, dann löse nach der Klammer auf.', p + k, f'{p} + ({a * k ** 3} / {a}) / ({k}) ** 2')
    if n == 3:
        neg = R.random() < 0.5
        k = -r if neg else r
        return zahl(f'Löse {minus_klammer(p)}³ = {dz(k ** 3)}.', f'{minus_klammer(p)[1:-1]} = {wz(3, dz(k ** 3)) if k > 0 else "−" + wz(3, dz(-k ** 3))} = {dz(k)}, also x = {dz(p + k)}.',
                    'Löse zuerst nach der Klammer auf, dann nach x.', p + k, f'{p} + ({k ** 3}) / ({k}) ** 2')
    return luecken(f'Löse {minus_klammer(p)}{str(n).translate(HZ)} = {dz(r ** n)}.', L2, H2, [p - r, p + r],
                   f'{minus_klammer(p)[1:-1]} = ±{r}, also x₁ = {dz(p - r)}, x₂ = {dz(p + r)}.',
                   'Gerader Exponent: Die Klammer ist ±' + wz(n, '…') + '.', c=[f'{p} - {r ** n} / {r} ** {n - 1}', f'{p} + {r ** n} / {r} ** {n - 1}'])


def nz9():
    return R.choice([i for i in range(-9, 10) if i != 0])


def g_naeherung(s):
    if s == 2 and R.random() < 0.3:
        n = R.choice([3, 4])
        c = R.randint(10, 400)
        k = int(c ** (1 / n))
        while (k + 1) ** n <= c: k += 1
        while k ** n > c: k -= 1
        if k ** n == c or k < 1: return None
        t = f'³√{c}' if n == 3 else f'die positive Lösung von x⁴ = {c}'
        return auswahl(f'Zwischen welchen ganzen Zahlen liegt {t}?', f'{k} und {k + 1}',
                       [f'{k - 1} und {k}', f'{k + 1} und {k + 2}', f'{c // n} und {c // n + 1}'],
                       f'{k}{str(n).translate(HZ)} = {dz(k ** n)} < {c} < {dz((k + 1) ** n)} = {k + 1}{str(n).translate(HZ)}.',
                       'Probiere ganze Zahlen hoch ' + str(n) + '.')
    n = R.choice([3, 3, 4, 5]) if s < 3 else R.choice([3, 4, 5, 6])
    c = R.randint(2, 300)
    if round(c ** (1 / n)) ** n == c: return None
    wahr = c ** (1 / n)
    v = gerundet(wahr, 2)
    if v is None: return None
    if s == 1:
        n = 3
        wahr = c ** (1 / 3)
        v = gerundet(wahr, 2)
        if v is None or round(wahr) ** 3 == c: return None
        return zahl(f'Löse x³ = {c}. Runde auf zwei Nachkommastellen.', f'x = ³√{c} ≈ {f2(v)}.', 'Nutze die Wurzeltaste des Taschenrechners.',
                    v, f'round({K(wahr)}, 2)')
    if s == 2:
        neg = n % 2 == 1 and R.random() < 0.5
        cc = -c if neg else c
        x = -v if neg else v
        if n % 2 == 0:
            return zahl(f'Löse {xn(n)} = {c}. Gib die positive Lösung auf zwei Nachkommastellen an.', f'x = ±{wz(n, c)} ≈ ±{f2(v)}; positiv: {f2(v)}.',
                        'Gerader Exponent: zwei Lösungen ±ⁿ√c.', v, f'round({K(wahr)}, 2)')
        return zahl(f'Löse {xn(n)} = {dz(cc)}. Runde auf zwei Nachkommastellen.',
                    f'Ungerader Exponent: x = {"−" if neg else ""}{wz(n, c)} ≈ {f2(x)}.', 'Vorzeichen von c beachten.', x,
                    f'round({"-" if neg else ""}{K(wahr)}, 2)')
    a = R.randint(2, 5)
    if n % 2:
        b = nz9()
        neg = R.random() < 0.5
        cc = -c if neg else c
        x = -v if neg else v
        return zahl(f'Löse {a}{xn(n)} {plus(b)} = {dz(a * cc + b)}. Runde auf zwei Nachkommastellen.',
                    f'{a}{xn(n)} = {dz(a * cc)} ⇒ {xn(n)} = {dz(cc)} ⇒ x = {"−" if neg else ""}{wz(n, c)} ≈ {f2(x)}.',
                    'Erst die Zahl, dann den Faktor auf die andere Seite bringen.', x, f'round({"-" if neg else ""}{K(wahr)}, 2)')
    return zahl(f'Löse {a}{xn(n)} = {a * c}. Gib die negative Lösung auf zwei Nachkommastellen an.',
                f'{xn(n)} = {c}, x = ±{wz(n, c)} ≈ ±{f2(v)}; negativ: −{f2(v)}.', 'Erst durch den Faktor teilen.', -v,
                f'round(-{K(wahr)}, 2)')


def g_sachaufgabe(s):
    typ = R.random()
    if s == 1:
        a = R.randint(2, 12)
        dinge = ['Ein würfelförmiger Karton', 'Ein Würfel aus Beton', 'Ein würfelförmiges Aquarium', 'Ein Holzwürfel']
        return zahl(f'{R.choice(dinge)} hat {dz(a ** 3)} dm³ Volumen. Wie lang ist eine Kante?', f'a³ = {dz(a ** 3)} ⇒ a = ³√{dz(a ** 3)} = {a} dm.',
                    'Stelle die Volumenformel des Würfels auf.', a, f'{a ** 3} / {a} ** 2', einheit='dm')
    if s == 2:
        if typ < 0.5:
            p = R.choice([2, 3, 4, 5, 6, 8, 10])
            q = 1 + Fr(p, 100)
            K0 = R.choice([1000, 2000, 4000, 5000, 10000, 20000])
            K2 = K0 * q * q
            return zahl(f'Ein Guthaben wächst in 2 Jahren bei gleichem Zinssatz (mit Zinseszins) von {eur(K0)} € auf {eur(K2)} €. Wie hoch ist der Zinssatz in Prozent?',
                        f'{eur(K0)} · q² = {eur(K2)} ⇒ q² = {dz(q * q)} ⇒ q = {dz(q)} (positiv). Zinssatz {p} %.',
                        'Wachstumsfaktor q pro Jahr: Anfangswert · q · q = Endwert.', p, f'(({float(q * q)}) / {float(q)} - 1) * 100')
        a = R.randint(6, 20)
        pl = R.choice([40, 50])
        L_ = Fr(a * pl, 100)
        return zahl(f'Eine quadratische Terrasse ist mit {dz(a * a)} quadratischen Platten mit {pl} cm Seitenlänge belegt. Wie lang ist eine Seite der Terrasse in m?',
                    f'Platten je Seite: n² = {dz(a * a)} ⇒ n = {a} (nur positiv). Seite: {a} · {dz(Fr(pl, 100))} m = {dz(L_)} m.',
                    'Wie viele Platten liegen an einer Seite? Stelle n² = … auf.', L_, f'({a * a} / {a}) * {pl} / 100', einheit='m')
    if typ < 0.35:
        if R.random() < 0.5:
            a = R.choice([1, 2, 3, 4, 5])
            return zahl(f'Ein würfelförmiger Wassertank soll {dz(a ** 3)} m³ fassen. Wie lang muss eine Innenkante sein?',
                        f'a³ = {dz(a ** 3)} ⇒ a = ³√{dz(a ** 3)} = {a} m.', 'Das Fassungsvermögen ist das Volumen a³.', a, f'{a ** 3} / {a} ** 2', einheit='m')
        a = R.choice([2, 4, 5, 6, 10])
        m = Fr(193, 10) * a ** 3
        return zahl(f'Ein Würfel aus Gold wiegt {dz(m / 1000)} kg (1 cm³ Gold wiegt 19,3 g). Wie lang ist seine Kante?',
                    f'Volumen: {dz(m)} g : 19,3 g = {dz(a ** 3)} cm³. a³ = {dz(a ** 3)} ⇒ a = {a} cm.',
                    'Berechne erst das Volumen aus der Masse, dann die Kante.', a, f'({float(m)} / 19.3) / {a} ** 2', einheit='cm')
    if typ < 0.65:
        l, b, h = R.choice([(2, 4, 8), (4, 4, 4 * 2 * 2), (3, 9, 8), (2, 9, 12), (4, 6, 9), (5, 5, 5), (2, 2, 16), (6, 9, 4), (8, 8, 1), (3, 6, 12)])
        a = round((l * b * h) ** (1 / 3))
        if a ** 3 != l * b * h: return None
        return zahl(f'Ein Quader ({l} cm × {b} cm × {h} cm) wird eingeschmolzen und zu einem Würfel mit gleichem Volumen gegossen. Wie lang ist eine Würfelkante?',
                    f'V = {l} · {b} · {h} = {l * b * h} cm³. a³ = {l * b * h} ⇒ a = {a} cm.', 'Das Volumen bleibt gleich.', a,
                    f'({l} * {b} * {h}) / {a} ** 2', einheit='cm')
    x = R.randint(2, 8)
    k = R.choice([2, 3, 4])
    V = k * x ** 3
    return zahl(f'Eine Kiste hat eine quadratische Grundfläche. Sie ist {k}-mal so hoch wie breit und hat {dz(V)} cm³ Volumen. Wie breit ist sie?',
                f'V = x · x · {k}x = {k}x³ = {dz(V)} ⇒ x³ = {dz(x ** 3)} ⇒ x = {x} cm.', 'Breite x, Höhe ' + str(k) + 'x. Stelle das Volumen auf.',
                x, f'({V} / {k}) / {x} ** 2', einheit='cm')


GEN = {'gerade': g_gerade, 'ungerade': g_ungerade, 'anzahl': g_anzahl, 'umformen': g_umformen, 'naeherung': g_naeherung,
       'sachaufgabe': g_sachaufgabe}

if __name__ == '__main__':
    bauen('gleichungen.potenz',
          'Gleichungen der Form xⁿ = c lösen und die Anzahl der Lösungen begründen.',
          ['n gerade, c > 0: zwei Lösungen ±ⁿ√c; c = 0: x = 0; c < 0: keine Lösung.', 'n ungerade: genau eine Lösung (bei c < 0 negativ).',
           'Erst auf die Form (…)ⁿ = c bringen, dann Wurzel ziehen.'],
          [('Grundform xⁿ = c', ['gerade', 'ungerade', 'anzahl']), ('Umformen und Runden', ['umformen', 'naeherung']),
           ('Anwenden', ['sachaufgabe'])],
          ETAPPEN, GEN,
          meiden={'gerade': ['x⁴ = 16.'], 'ungerade': ['x³ = −125.'], 'anzahl': ['x⁶ = −1?'], 'umformen': ['= 61.'],
                  'naeherung': ['x³ = 40.'], 'sachaufgabe': ['216 dm³']},
          offen=['Rechenausdruck c bei gerundeten Lösungen (Lernkarte „naeherung“): Das Prüfskript kann keine Wurzeln ziehen; der Wurzelwert steht als 12-stellige Konstante im Ausdruck.'])
