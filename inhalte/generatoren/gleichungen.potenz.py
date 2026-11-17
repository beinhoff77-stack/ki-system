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

# ---------- Zehnte Runde (schwer-kl9): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Abschnitt mit eigenem festen Zufallsstart (anhaengen(..., 9905, ...)), läuft erst nach bauen():
# alle bisherigen Aufgaben bleiben unverändert. Vorbilder: Bayerischer Mathematik-Test 10 (ISB; Gleichung zweier
# Potenzterme lösen und als Schnittpunkte der Graphen deuten, 2x³ − 15x = 0 durch Ausklammern), Abschlussprüfung
# Realschule Bayern (Ergebnisse auf zwei Stellen runden, Raumgeometrie), Illustrierende Aufgaben Realschule 9
# (proportionale Zusammenhänge mit Potenzen). Zahlen und Wortlaut eigen.
from _schwer_kl9 import anhaengen  # noqa: E402
from _kl9 import K as _K  # noqa: E402


def schwer():
    P, Kn, O = 'pruefung', 'knobel', ''
    L2, H = 'x₁ = □; x₂ = □', 'kleinere Lösung zuerst'
    g = lambda n, c, xs, ys: {'typ': 'koordinaten', 'x': xs, 'y': ys, 'graphen': [{'art': 'potenz', 'a': 1, 'n': n, 'name': f'y = x{"⁴" if n == 4 else "³"}'}],
                              'waagrecht': [c]}
    return [
        # gerade
        ('gerade', 3, P, luecken('Die Graphen von y = x⁴ und y = 16 schneiden sich in zwei Punkten. Gib die x-Koordinaten an.', L2, H, [-2, 2],
                                 'Gleichsetzen: x⁴ = 16, also x = 2 oder x = −2. Die Schnittpunkte sind (−2 | 16) und (2 | 16).',
                                 'Setze die beiden Terme gleich. Denke an beide Vorzeichen.', ['-2', '2'])),
        ('gerade', 3, P, luecken('Löse 2x⁴ − 30 = 132.', L2, H, [-3, 3], '2x⁴ = 162 ⇒ x⁴ = 81 ⇒ x = ±3.', 'Erst 30 addieren, dann durch 2 teilen.', ['-3', '3'])),
        ('gerade', 3, Kn, zahl('Wie viele Lösungen hat die Gleichung x⁴ = x²?', 'x⁴ − x² = 0 ⇔ x²(x² − 1) = 0. Also x = 0 oder x² = 1, d. h. x = 1 oder x = −1: drei Lösungen. Falle: Durch x² teilen verliert die 0.',
                               'Nicht durch x² teilen! Bringe alles auf eine Seite und klammere aus.', 3, '1 + 2')),
        ('gerade', 3, O, auswahl('Welche Lösungsmenge hat x⁶ = 0,000064?', 'L = {−0,2; 0,2}', ['L = {0,2}', 'L = {−0,02; 0,02}', 'L = { }'],
                                 '0,2⁶ = 0,000064 (2⁶ = 64, sechs Nachkommastellen). Gerader Exponent: auch −0,2 ist Lösung.',
                                 'Denke an 2⁶ = 64 und zähle die Nachkommastellen.')),
        ('gerade', 2, O, luecken('Löse x⁴ = 10 000.', L2, H, [-10, 10], 'x = ±⁴√10 000 = ±10, denn 10⁴ = 10 000.', 'Zähle die Nullen.', ['-10', '10'])),
        ('gerade', 2, O, auswahl('Welche Lösungsmenge hat x⁴ + 1 = 0?', 'L = { }', ['L = {−1; 1}', 'L = {−1}', 'L = {1}'],
                                 'x⁴ = −1, aber x⁴ ist nie negativ: keine Lösung.', 'Stelle x⁴ allein. Kann eine gerade Potenz negativ sein?')),
        # ungerade
        ('ungerade', 3, P, zahl('Die Graphen von y = x³ und y = −27 schneiden sich in genau einem Punkt. Welche x-Koordinate hat er?',
                                'x³ = −27 ⇒ x = −3, denn (−3)³ = −27. Ungerader Exponent: genau ein Schnittpunkt (−3 | −27).',
                                'Setze gleich und denke daran, dass ein Minus bei ungeradem Exponenten bleibt.', -3, '-27 / 9')),
        ('ungerade', 3, P, zahl('Löse 4x³ + 32 = 0.', '4x³ = −32 ⇒ x³ = −8 ⇒ x = −2.', 'Erst 32 abziehen, dann durch 4 teilen.', -2, '-8 / 4')),
        ('ungerade', 3, Kn, zahl('Für welche Zahl a hat die Gleichung x⁵ = a die Lösung x = −0,1?', 'Einsetzen: a = (−0,1)⁵ = −0,00001 (ungerader Exponent, Minus bleibt; fünf Nachkommastellen).',
                                 'Rückwärts: Setze x = −0,1 ein.', -0.00001, '(-0.1) ** 5')),
        ('ungerade', 3, O, zahl('Löse (2x − 1)³ = 125.', '2x − 1 = ³√125 = 5 ⇒ 2x = 6 ⇒ x = 3.', 'Erst die dritte Wurzel aus 125, dann die lineare Gleichung lösen.', 3, '(5 + 1) / 2')),
        ('ungerade', 2, O, zahl('Löse x³ = −1 000.', 'x = −10, denn (−10)³ = −1 000.', 'Ungerader Exponent: genau eine Lösung, hier negativ.', -10, '-1000 / 100')),
        ('ungerade', 2, O, zahl('Löse x⁷ = −1.', 'x = −1, denn (−1)⁷ = −1 (ungerade viele Minus).', 'Welche Zahl hoch 7 ergibt −1?', -1, '(-1) ** 7')),
        # anzahl
        ('anzahl', 3, P, bild(auswahl('Die Abbildung zeigt den Graphen von y = x⁴ und die Linie y = 3. Was folgt daraus für die Gleichung x⁴ = 3?',
                                      'Sie hat zwei Lösungen, eine positive und eine negative.',
                                      ['Sie hat genau eine Lösung.', 'Sie hat keine Lösung, weil 3 keine vierte Potenz einer ganzen Zahl ist.', 'Sie hat vier Lösungen, weil der Exponent 4 ist.'],
                                      'Die Linie y = 3 schneidet den Graphen zweimal, symmetrisch zur y-Achse: x = ±⁴√3 ≈ ±1,32.',
                                      'Zähle die Schnittpunkte der Linie mit dem Graphen.'), g(4, 3, [-2, 2], [-1, 5]))),
        ('anzahl', 3, P, bild(auswahl('Die Abbildung zeigt den Graphen von y = x³ und die Linie y = −2. Was folgt daraus für die Gleichung x³ = −2?',
                                      'Sie hat genau eine Lösung, und die ist negativ.', ['Sie hat keine Lösung.', 'Sie hat zwei Lösungen.', 'Sie hat genau eine Lösung, und die ist positiv.'],
                                      'Die Linie y = −2 schneidet den Graphen genau einmal, links von der y-Achse: x = −³√2 ≈ −1,26.',
                                      'Zähle die Schnittpunkte und schau, auf welcher Seite der y-Achse sie liegen.'), g(3, -2, [-2, 2], [-4, 4]))),
        ('anzahl', 3, Kn, zahl('Für wie viele ganze Zahlen c von −5 bis 5 hat die Gleichung x⁴ = c genau zwei Lösungen?',
                               'Zwei Lösungen gibt es nur für c > 0, also für c = 1, 2, 3, 4, 5: fünf Zahlen. (c = 0: eine Lösung, c < 0: keine.)',
                               'Überlege getrennt für c > 0, c = 0 und c < 0.', 5, '5 - 1 + 1')),
        ('anzahl', 3, O, auswahl('Wie viele Lösungen hat die Gleichung x³ = x?', 'drei', ['eine', 'zwei', 'keine'],
                                 'x³ − x = 0 ⇔ x(x² − 1) = 0: x = 0, x = 1, x = −1.', 'Nicht durch x teilen – ausklammern.')),
        ('anzahl', 2, O, auswahl('Wie viele Lösungen hat x¹⁰ = 0?', 'genau eine Lösung', ['zwei Lösungen', 'keine Lösung'],
                                 'Nur 0 hoch 10 ergibt 0, also genau eine Lösung x = 0.', 'Welche Zahl hoch 10 ergibt 0?')),
        ('anzahl', 2, O, auswahl('Wie viele Lösungen hat x⁷ = −5?', 'genau eine Lösung', ['zwei Lösungen', 'keine Lösung'],
                                 'Ungerader Exponent: immer genau eine Lösung, hier x = −⁷√5.', 'Ist der Exponent gerade oder ungerade?')),
        # umformen
        ('umformen', 3, P, luecken('Löse x⁵ − 16x = 0.', 'x₁ = □; x₂ = □; x₃ = □', 'der Größe nach', [-2, 0, 2],
                                   'x(x⁴ − 16) = 0. Also x = 0 oder x⁴ = 16, d. h. x = ±2.', 'Klammere x aus. Nicht durch x teilen.', ['-2', '0', '2'])),
        ('umformen', 3, P, zahl('Löse 0,5 · (x − 2)³ + 4 = 0.', '0,5(x − 2)³ = −4 ⇒ (x − 2)³ = −8 ⇒ x − 2 = −2 ⇒ x = 0.',
                                'Rückwärts: erst 4 abziehen, dann mal 2, dann dritte Wurzel.', 0, '2 + (-2)')),
        ('umformen', 3, Kn, luecken('Löse (x² − 5)² = 16.', 'x₁ = □; x₂ = □; x₃ = □; x₄ = □', 'der Größe nach', [-3, -1, 1, 3],
                                    'x² − 5 = 4 oder x² − 5 = −4. Also x² = 9 (x = ±3) oder x² = 1 (x = ±1): vier Lösungen.',
                                    'Die Klammer ist 4 oder −4. Löse dann beide Gleichungen.', ['-3', '-1', '1', '3'])),
        ('umformen', 3, O, zahl('Löse 2 − 3x³ = 26.', '−3x³ = 24 ⇒ x³ = −8 ⇒ x = −2.', 'Erst 2 abziehen, dann durch −3 teilen.', -2, '-8 / 4')),
        ('umformen', 2, O, luecken('Löse 5x⁴ = 80.', L2, H, [-2, 2], 'x⁴ = 16 ⇒ x = ±2.', 'Erst durch 5 teilen.', ['-2', '2'])),
        ('umformen', 2, O, zahl('Löse x³ − 4 = 60.', 'x³ = 64 ⇒ x = 4.', 'Erst 4 addieren.', 4, '64 / 16')),
        # naeherung
        ('naeherung', 3, P, zahl('Ein würfelförmiger Behälter soll innen genau 50 Liter fassen. Wie lang muss eine Innenkante sein? Gib das Ergebnis in cm auf eine Nachkommastelle an.',
                                 '50 Liter = 50 dm³. a = ³√50 dm ≈ 3,684 dm ≈ 36,8 cm.', 'Erst in dm³ rechnen (1 Liter = 1 dm³), dann in cm umrechnen.',
                                 round(50 ** (1 / 3) * 10, 1), f'round({_K(50 ** (1 / 3) * 10)}, 1)', einheit='cm')),
        ('naeherung', 3, P, zahl('Löse 3x⁴ − 5 = 70. Gib die positive Lösung auf zwei Nachkommastellen an.', '3x⁴ = 75 ⇒ x⁴ = 25 ⇒ x = ⁴√25 = √5 ≈ 2,24.',
                                 'Erst umformen bis x⁴ = … dasteht.', round(5 ** 0.5, 2), f'round({_K(5 ** 0.5)}, 2)')),
        ('naeherung', 3, Kn, zahl('Das Volumen eines Würfels wird verdoppelt. Um wie viel Prozent wird dabei seine Kante länger? Runde auf ganze Prozent.',
                                  'Neue Kante: ∛2 ≈ 1,26-mal so lang. Das ist ein Zuwachs von etwa 26 % – nicht 100 %.',
                                  'Nimm einen Würfel mit Kante 1. Welche Kante hat ein Würfel mit Volumen 2?', round((2 ** (1 / 3) - 1) * 100), f'round({_K((2 ** (1 / 3) - 1) * 100)}, 0)', einheit='%')),
        ('naeherung', 3, O, zahl('Löse x⁵ + 100 = 0. Runde auf zwei Nachkommastellen.', 'x⁵ = −100 ⇒ x = −⁵√100 ≈ −2,51.', 'Ungerader Exponent: Das Minus bleibt.',
                                 round(-(100 ** 0.2), 2), f'round({_K(-(100 ** 0.2))}, 2)')),
        ('naeherung', 2, O, zahl('Löse x³ = 500. Runde auf eine Nachkommastelle.', 'x = ³√500 ≈ 7,9. Schätzung: 7³ = 343, 8³ = 512.', 'Erst schätzen, dann Taschenrechner.',
                                 round(500 ** (1 / 3), 1), f'round({_K(500 ** (1 / 3))}, 1)')),
        ('naeherung', 2, O, zahl('Löse x⁴ = 50. Gib die positive Lösung auf zwei Nachkommastellen an.', 'x = ⁴√50 ≈ 2,66.', 'Vierte Wurzel mit dem Taschenrechner.',
                                 round(50 ** 0.25, 2), f'round({_K(50 ** 0.25)}, 2)')),
        # sachaufgabe
        ('sachaufgabe', 3, P, zahl('Ein Aquarium hat die Form eines Würfels und fasst 125 Liter. Wie viele cm² Glas braucht man für Boden und vier Seitenwände (ohne Deckel)?',
                                   '125 Liter = 125 dm³, Kante ∛125 dm = 5 dm = 50 cm. Eine Fläche: 50 · 50 = 2 500 cm². Fünf Flächen: 12 500 cm².',
                                   'Kante bestimmen, dann zählen: Wie viele Quadrate braucht man ohne Deckel?', 12500, '5 * 50 ** 2', einheit='cm²')),
        ('sachaufgabe', 3, P, zahl('Die Masse einer Metallkugel ist proportional zu r³. Eine Kugel mit 2 cm Radius wiegt 270 g. Welchen Radius hat eine Kugel aus demselben Metall mit 2 160 g?',
                                   '2 160 : 270 = 8. Die Masse ist 8-mal so groß, also r³ 8-mal so groß und r = ∛8 = 2-mal so groß: 4 cm.',
                                   'Um welchen Faktor ist die Masse größer? Welcher Faktor beim Radius gehört dazu?', 4, '2 * 2', einheit='cm')),
        ('sachaufgabe', 3, Kn, zahl('Jede Kante eines Würfels wird um 1 cm verlängert. Dadurch wächst sein Volumen um 61 cm³. Wie lang war eine Kante vorher?',
                                    '(a + 1)³ − a³ = 3a² + 3a + 1 = 61 ⇔ a² + a − 20 = 0 ⇔ a = 4 (oder −5, passt nicht). Probe: 5³ − 4³ = 125 − 64 = 61.',
                                    'Probieren geht auch: Vergleiche 2³ und 3³, 3³ und 4³, …', 4, '(-1 + 9) / 2', einheit='cm')),
        ('sachaufgabe', 3, O, zahl('Ein quaderförmiger Karton ist doppelt so lang wie breit und genauso hoch wie breit. Er fasst 16 Liter. Wie breit ist er in cm?',
                                   'Breite x (in dm): x · 2x · x = 2x³ = 16 ⇒ x³ = 8 ⇒ x = 2 dm = 20 cm.', 'Rechne in dm (1 Liter = 1 dm³).', 20, '2 * 10', einheit='cm')),
        ('sachaufgabe', 2, O, zahl('Ein Würfel hat 343 cm³ Volumen. Wie groß ist seine Oberfläche?', 'a = ³√343 = 7 cm. O = 6 · 7² = 294 cm².', 'Erst die Kante, dann sechs Quadrate.',
                                   294, '6 * 7 ** 2', einheit='cm²')),
        ('sachaufgabe', 2, O, zahl('Ein quadratisches Feld hat 2,25 ha Fläche (1 ha = 10 000 m²). Wie lang ist eine Seite?', '2,25 ha = 22 500 m². a = √22 500 m = 150 m.',
                                   'Erst in m² umrechnen.', 150, '22500 / 150', einheit='m')),
    ]


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('gleichungen.potenz', 13_9_5)
# a) Grundaufgabe bzw. gleicher Typ wie Stufe 2
BF.stufe('gerade', 'Welche Lösungsmenge hat 5x² = 0?', 2)
BF.stufe('gerade', 'Welche Lösungsmenge hat 4x⁸ = 0?', 2)
BF.stufe('ungerade', 'Löse x⁵ = −0,03125.', 2)
BF.nicht_umgesetzt('sachaufgabe S2 Zinseszins („Guthaben wächst in 2 Jahren …“)', 'Aufgaben richtig; mathematisch nur (1 + p)² = q, also eine Potenzgleichung. Ob der Sachkontext in Kl. 9 passt, ist eine Plan-Frage (siehe „für Sebastian“).')
BF.fuer_sebastian('gleichungen.potenz/sachaufgabe: Zinseszins-Aufgaben (Stufe 2, alle Pools) – Zinseszins ist laut Themenliste Zusatzstoff Kl. 10 (finanzen.zinseszins). In Kl. 9 belassen?')

# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    d = bauen('gleichungen.potenz',
          'Gleichungen der Form xⁿ = c lösen und die Anzahl der Lösungen begründen.',
          ['n gerade, c > 0: zwei Lösungen ±ⁿ√c; c = 0: x = 0; c < 0: keine Lösung.', 'n ungerade: genau eine Lösung (bei c < 0 negativ).',
           'Erst auf die Form (…)ⁿ = c bringen, dann Wurzel ziehen.'],
          [('Grundform xⁿ = c', ['gerade', 'ungerade', 'anzahl']), ('Umformen und Runden', ['umformen', 'naeherung']),
           ('Anwenden', ['sachaufgabe'])],
          ETAPPEN, GEN,
          meiden={'gerade': ['x⁴ = 16.'], 'ungerade': ['x³ = −125.'], 'anzahl': ['x⁶ = −1?'], 'umformen': ['= 61.'],
                  'naeherung': ['x³ = 40.'], 'sachaufgabe': ['216 dm³']},
          offen=['Rechenausdruck c bei gerundeten Lösungen (Lernkarte „naeherung“): Das Prüfskript kann keine Wurzeln ziehen; der Wurzelwert steht als 12-stellige Konstante im Ausdruck.'])
    anhaengen(d, 9905, schwer)
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden


# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl9) ----
from _durchsicht_kl9 import Befunde as _DSB, durchsicht  # noqa: E402

DS = _DSB('gleichungen.potenz', 19_9_9)
# gerade: xⁿ = c mit geradem n ist genau das Beispiel der Karte → Stufe 1
for _t in ('Löse x⁶ = 64.', 'Bestimme alle Lösungen von 81 = x⁴.', 'Löse x⁴ − 256 = 0.', 'Bestimme alle Lösungen von 729 = x⁶.', 'Löse x⁴ = 10 000.'):
    DS.stufe('gerade', _t, 1)
# ungerade: positive c sind der einfache Fall (Stufe 1); negative Dezimalzahlen wie Stufe 2
for _t in ('Löse x³ = 1.', 'Löse x⁵ = 32.', 'Löse x³ = 1 000.'):
    DS.stufe('ungerade', _t, 1)
for _t in ('Löse x³ = −3,375.', 'Löse x⁵ = −0,00243.'):
    DS.stufe('ungerade', _t, 2)
# anzahl: einmal Fehlerfinden auf Stufe 2
DS.stufe('anzahl', 'Jemand sagt: „x³ = −64 hat keine Lösung, weil man aus negativen Zahlen keine Wurzel ziehen kann.“ Was stimmt?', 2)
# naeherung: negative Lösung bei geradem Exponenten ist die Abwandlung (Stufe 2)
for _t in ('Löse 5x⁶ = 30. Gib die negative Lösung auf zwei Nachkommastellen an.', 'Löse 4x⁶ = 820. Gib die negative Lösung auf zwei Nachkommastellen an.'):
    DS.stufe('naeherung', _t, 2)
# sachaufgabe: je eine Wiederholung von Kiste und Quader auf Stufe 2
DS.stufe('sachaufgabe', 'Eine Kiste hat eine quadratische Grundfläche. Sie ist 2-mal so hoch wie breit und hat 54 cm³ Volumen. Wie breit ist sie?', 2)
DS.stufe('sachaufgabe', 'Ein Quader (2 cm × 2 cm × 16 cm) wird eingeschmolzen und zu einem Würfel mit gleichem Volumen gegossen. Wie lang ist eine Würfelkante?', 2)

if __name__ == '__main__':
    durchsicht('gleichungen.potenz', DS)


# ---- STUFEN (Zwanzigste Runde, Zweig stufen-kl9) ----
from _stufen_kl9 import Stufen, stufen  # noqa: E402

ST = Stufen('gleichungen.potenz', 20_9_9)
Z, A, L = ST.Z, ST.A, ST.L
_X2 = 'x₁ = □; x₂ = □'

# gerade
ST.stufenleiter('gerade', 'xⁿ = c mit geradem n und c > 0: beide Lösungen angeben.',
                'Exakte Wurzel-Lösungen, c = 0 und c < 0, c rückwärts aus einer Lösung, Schnitt mit einer Waagrechten.',
                'Fehler bei negativem c und vergessener negativer Lösung finden, Symmetrie begründen, Bedingung für eine Lösung, Flächenfaktor.')
ST.typ('gerade', '/^(Löse x[²⁴⁶] [−=]|Bestimme alle Lösungen)/', 'direkt')
ST.typ('gerade', '/^(Löse x² = 125|Welche Lösungsmenge hat (\\dx|x⁴ \\+))/', 'mehrschritt')
ST.typ('gerade', 'Löse 2x⁴', 'mehrschritt')
ST.typ('gerade', 'Die Graphen von', 'darstellung')
ST.typ('gerade', 'Jemand löst', 'fehler')
ST.typ('gerade', '/^(Wie viele Lösungen hat|Welche Lösungsmenge hat x⁶ = 0)/', 'verknuepfen')
ST.neu('gerade', 'erkennen', A('Welche Zahl ist eine Lösung von x⁴ = 81?', '−3', ['9', '20,25', '−9'],
       '(−3)⁴ = 81, denn die vier Minuszeichen heben sich paarweise auf. 9⁴ wäre 6 561.', 'Probiere, welche Zahl hoch 4 genau 81 ergibt.'))
ST.neu('gerade', 'umkehr', Z('Die Gleichung x⁴ = c hat die Lösung x = −3. Wie groß ist c?', 81, '(-3) ** 4',
       'c = (−3)⁴ = 81. Dann ist auch 3 eine Lösung.', 'Setze die Lösung ein.'))
ST.neu('gerade', 'darstellung', L('Der Graph von y = x⁶ und die Gerade y = 1 schneiden sich. Gib die x-Werte an.', _X2, [-1, 1], ['-1', '1'],
       'x⁶ = 1 hat die Lösungen −1 und 1.', 'Welche Gleichung beschreibt die Schnittpunkte?'))
ST.neu('gerade', 'begruenden', A('Stimmt: Ist x₁ eine Lösung von xⁿ = c mit geradem n, dann ist auch −x₁ eine Lösung?', 'Ja, denn (−x₁)ⁿ = x₁ⁿ bei geradem n.', ['Nein, nur bei c > 100.', 'Nur bei n = 2.', 'Nein, nie.'],
       'Bei geradem Exponenten heben sich die Minuszeichen paarweise auf. Darum kommen Lösungen (außer 0) immer als Paar ±x₁.', 'Was passiert mit dem Minus bei einer geraden Potenz?'))
ST.neu('gerade', 'parameter', A('Für welche Zahl c hat x⁴ = c genau eine Lösung?', 'c = 0', ['c = 1', 'für alle c < 0', 'für alle c > 0'],
       'Für c > 0 gibt es zwei Lösungen, für c < 0 keine, für c = 0 nur x = 0.', 'Denk an die waagrechte Linie y = c.'))
ST.neu('gerade', 'transfer', Z('Ein quadratisches Grundstück wird so vergrößert, dass seine Fläche 2,56-mal so groß ist. Mit welchem Faktor wächst seine Seite?', 1.6, '1.6',
       'Faktor k mit k² = 2,56, positiv: k = 1,6, denn 1,6 · 1,6 = 2,56.', 'Fläche wächst mit dem Quadrat des Faktors.'))
ST.knobel('gerade', Z('Wie viele ganze Zahlen x erfüllen x⁴ ≤ 100?', 7, '2 * 3 + 1',
          'x⁴ ≤ 100 heißt x² ≤ 10. Ganze Zahlen: 0, ±1, ±2, ±3 (3⁴ = 81 ≤ 100, 4⁴ = 256). Das sind 7.', 'Auch negative Zahlen zählen.'))
ST.knobel('gerade', Z('Die Gleichung (x − 2)⁴ = 16 hat zwei Lösungen. Wie groß ist ihre Summe?', 4, '0 + 4',
          'x − 2 = 2 oder x − 2 = −2, also x = 4 oder x = 0. Summe 4 – das ist doppelt die Mitte 2, um die die Lösungen symmetrisch liegen.',
          'Löse zuerst nach x − 2 auf.'))

# ungerade
ST.stufenleiter('ungerade', 'xⁿ = c mit ungeradem n: genau eine Lösung, auch für negatives c.',
                'Negative Dezimalzahlen, rückwärts c aus der Lösung, Kühlschrank-Volumen, Klammern umformen.',
                'Fehler ±3 bei x³ finden, „immer genau eine Lösung“ begründen, Bedingung für gleiche Lösungen, Wachstumsfaktor, mehrteilige Aufgabe.')
ST.typ('ungerade', '/^Löse x[³⁵] = [\\d ]+\\.$/', 'direkt')
ST.typ('ungerade', '/^Löse (x[³⁵⁷] = −|4x³)/', 'mehrschritt')
ST.typ('ungerade', 'Die Graphen von', 'darstellung')
ST.typ('ungerade', 'Für welche Zahl a', 'umkehr')
ST.typ('ungerade', '/^Löse \\(/', 'verknuepfen')
ST.neu('ungerade', 'erkennen', A('Welche Zahl löst x³ = −8?', '−2', ['2', '−2 und 2', 'keine Zahl'],
       '(−2) · (−2) · (−2) = −8. Bei ungeradem Exponenten bleibt ein Minus übrig, also genau eine Lösung.', 'Wie viele Minuszeichen bleiben bei drei Faktoren?'))
ST.neu('ungerade', 'einkleidung', Z('Der Innenraum eines würfelförmigen Kühlschranks fasst 0,125 m³. Wie lang ist eine Innenkante in cm?', 50, '0.5 * 100',
       '∛0,125 = 0,5 m, denn 0,5³ = 0,125. 0,5 m = 50 cm.', 'Erst die Kante in m.', einheit='cm'))
ST.neu('ungerade', 'fehler', A('Jemand löst x³ = −27 mit x = ±3. Was stimmt?', 'Falsch: Nur x = −3 ist Lösung, denn 3³ = 27.', ['Richtig.', 'Falsch: Es gibt keine Lösung.', 'Falsch: x = −9.'],
       '(−3)³ = −27, aber 3³ = +27. Bei ungeradem Exponenten gibt es genau eine Lösung.', 'Mach die Probe mit +3.'))
ST.neu('ungerade', 'begruenden', A('Stimmt: x³ = c hat für jede Zahl c genau eine Lösung?', 'Ja: Der Graph von x³ steigt von links unten nach rechts oben und trifft jede Waagrechte genau einmal.', ['Nein, für c < 0 gibt es keine.', 'Nein, für c > 0 gibt es zwei.', 'Nur für c = 0.'],
       'y = x³ nimmt jeden Wert genau einmal an. Darum hat x³ = c immer genau eine Lösung.', 'Denk an den Graphen von y = x³.'))
ST.neu('ungerade', 'parameter', A('Für welche Werte von k haben x³ = k und x⁵ = k dieselbe Lösung?', 'für k = −1, k = 0 und k = 1', ['nur für k = 0', 'für jedes k', 'für k = 1 und k = 8'],
       'Dieselbe Lösung x heißt x³ = x⁵, also x³(x² − 1) = 0: x = 0, 1 oder −1. Dazu gehören k = 0, 1, −1.', 'Setze die beiden Potenzen gleich.'))
ST.neu('ungerade', 'transfer', Z('Eine Geldanlage wächst in 3 Jahren auf das 1,331-Fache, jedes Jahr mit demselben Faktor. Wie groß ist der Faktor pro Jahr?', 1.1, '1.1',
       'q³ = 1,331. 1,1³ = 1,331, also q = 1,1: 10 % pro Jahr.', 'Probiere 1,1.'))
ST.neu('ungerade', 'pruefung', L('Löse a) x³ = −125, b) x⁵ = 243, c) (x + 1)³ = 8.', 'a) □; b) □; c) □', [-5, 3, 1], ['-5', '3', '2 - 1'],
       'a) (−5)³ = −125. b) 3⁵ = 243. c) x + 1 = 2, x = 1.', 'Bei c) zuerst die Klammer.'))
ST.knobel('ungerade', Z('Für welche ganze Zahl x gilt x³ + x = −10?', -2, '-2',
          'Probiere negative Zahlen: x = −2 ergibt −8 − 2 = −10. Weil x³ + x immer steigt, wenn x wächst, gibt es keine weitere Lösung.', 'Die Lösung ist klein und negativ.'))
ST.knobel('ungerade', Z('Welche natürliche Zahl n erfüllt n³ < 2 000 < (n + 1)³?', 12, '12',
          '10³ = 1 000, 12³ = 1 728, 13³ = 2 197. Also liegt 2 000 zwischen 12³ und 13³, n = 12. Das heißt: ∛2 000 liegt zwischen 12 und 13.', 'Rechne einige Kubikzahlen aus.'))

# anzahl
ST.stufenleiter('anzahl', 'Am Exponenten und am Vorzeichen von c die Lösungsanzahl angeben.',
                'Mit Graph und Waagrechter begründen, Sonderfall c = 0, Sachfrage „hoch 6 ergibt 0“.',
                'Parameter c für genau zwei Lösungen, Fehler „aus Negativem keine Wurzel“, Folgerungen aus Bildern, Anzahl bei x³ = x.')
ST.typ('anzahl', 'Wie viele Lösungen hat x', 'erkennen', s=1)
ST.typ('anzahl', 'Im Bild siehst du', 'darstellung')
ST.typ('anzahl', 'Jemand sagt', 'fehler')
ST.typ('anzahl', 'Wie viele Lösungen hat die Gleichung x³ = x', 'verknuepfen')
ST.typ('anzahl', 'Wie viele Lösungen hat', 'mehrschritt')
ST.typ('anzahl', '/^(Für welche Werte|Für wie viele ganze)/', 'parameter')
ST.typ('anzahl', 'Die Abbildung zeigt', 'begruenden')
ST.neu('anzahl', 'direkt', L('Gleichung x⁴ = 81: Wie viele Lösungen hat sie, und welche sind es?', 'Anzahl □; x₁ = □; x₂ = □', [2, -3, 3], ['2', '-3', '3'],
       'Gerader Exponent, c > 0: zwei Lösungen, ±3, denn 3⁴ = 81.', 'Gerade oder ungerade?'))
ST.neu('anzahl', 'einkleidung', A('Eine Zahl hoch 6 soll genau 0 ergeben. Wie viele solche Zahlen gibt es?', 'genau eine (die 0)', ['keine', 'zwei', 'sechs'],
       'Ein Produkt ist nur 0, wenn ein Faktor 0 ist. x⁶ = 0 nur für x = 0.', 'Wann ist ein Produkt null?'))
ST.knobel('anzahl', Z('Wie viele Lösungen hat x⁴ − 5x² + 4 = 0?', 4, '2 + 2',
          'Mit u = x²: u² − 5u + 4 = 0, also (u − 1)(u − 4) = 0. x² = 1 liefert ±1, x² = 4 liefert ±2. Vier Lösungen.', 'Gib x² einen eigenen Namen.'))
ST.knobel('anzahl', Z('Wie viele Lösungen hat x⁶ = x²?', 3, '1 + 2',
          'x⁶ − x² = 0 ⇒ x²(x⁴ − 1) = 0 ⇒ x = 0 oder x⁴ = 1, also x = ±1. Drei Lösungen. Wer durch x² teilt, verliert die 0.', 'Nicht teilen – ausklammern.'))

# umformen
ST.stufenleiter('umformen', 'Bei a · xⁿ = c durch a teilen und die Wurzel ziehen.',
                'Erst eine Zahl abziehen, dann teilen; negative Faktoren; Würfelsumme; c rückwärts.',
                'Klammern, Vorgänge rückwärts machen, ausklammern, Ersetzen bei (x² − 5)², Fehler „minus statt teilen“, Parameter a.')
ST.typ('umformen', '/^Löse \\dx[²³] = \\d+\\.$/', 'direkt')
ST.typ('umformen', '/^Löse (\\dx[³⁴] [+−]|\\dx⁴ =|x³ −|2 − 3x³)/', 'mehrschritt')
ST.typ('umformen', '/^Löse (3\\(x|0,5)/', 'rueckwaerts')
ST.typ('umformen', 'Löse (x² − 5)²', 'transfer')
ST.typ('umformen', '/^Löse (\\(x|x⁵)/', 'verknuepfen')
ST.neu('umformen', 'erkennen', A('Was ist bei 2x³ + 7 = 61 der erste Schritt?', '7 auf beiden Seiten abziehen', ['durch 2 teilen', 'die dritte Wurzel ziehen', '61 durch 7 teilen'],
       'Zuerst muss 2x³ allein stehen: 2x³ = 54. Dann durch 2 teilen, dann die Wurzel.', 'Rückwärts rechnen: Was wurde zuletzt gemacht?'))
ST.neu('umformen', 'einkleidung', Z('Fünf gleiche Würfel haben zusammen 40 cm³ Volumen. Wie lang ist eine Kante?', 2, '2',
       '5x³ = 40 ⇒ x³ = 8 ⇒ x = 2 cm.', 'Stelle die Gleichung für ein Würfelvolumen x³ auf.', einheit='cm'))
ST.neu('umformen', 'umkehr', Z('Bei 2x³ + c = 61 ist x = 3 eine Lösung. Wie groß ist c?', 7, '61 - 2 * 27',
       '2 · 27 + c = 61 ⇒ c = 7.', 'Setze die Lösung ein.'))
ST.neu('umformen', 'fehler', A('Jemand löst 2x³ + 7 = 61 so: x³ = 61 − 7 − 2 = 52. Was stimmt?', 'Falsch: Die 2 ist ein Faktor, also teilen: x³ = 27, x = 3.', ['Richtig.', 'Falsch: x³ = 68.', 'Falsch: x³ = 54.'],
       '2x³ = 54, dann durch 2: x³ = 27. Ein Faktor wird durch Teilen entfernt, nicht durch Abziehen.', 'Wie entfernt man einen Faktor?'))
ST.neu('umformen', 'parameter', Z('Für welche Zahl a hat a · x⁴ − 32 = 0 die Lösungen −2 und 2?', 2, '32 // 16',
       'Einsetzen von 2: 16a − 32 = 0 ⇒ a = 2.', 'Setze x = 2 ein.'))
ST.knobel('umformen', Z('Löse (x³ − 7)² = 400. Gib die positive Lösung an.', 3, '3',
          'x³ − 7 = 20 oder x³ − 7 = −20. Also x³ = 27 (x = 3) oder x³ = −13 (x negativ). Positiv: x = 3.', 'Welche Zahlen ergeben quadriert 400?'))
ST.knobel('umformen', Z('Löse x⁴ − 13x² + 36 = 0. Gib die größte Lösung an.', 3, '3',
          'Mit u = x²: u² − 13u + 36 = 0 ⇒ (u − 4)(u − 9) = 0. x² = 4 oder x² = 9: Lösungen ±2 und ±3. Größte: 3.', 'Gib x² einen eigenen Namen.'))

# naeherung
ST.stufenleiter('naeherung', 'ⁿ√c mit dem Taschenrechner bestimmen und sinnvoll runden.',
                'Erst umformen, negative Lösungen, zwischen ganzen Zahlen eingrenzen, Tank in cm, c rückwärts.',
                'Fehler „nur eine Lösung“, Schätzungen begründen, Bedingung für k, vom gerundeten Wert zurückschließen, Wachstum, mehrteilige Aufgabe.')
ST.typ('naeherung', 'Löse x³ = 83', 'direkt')
ST.typ('naeherung', '/^Löse x³ = \\d+\\. Runde auf zwei/', 'direkt')
ST.typ('naeherung', '/^(Löse|Zwischen welchen)/', 'mehrschritt')
ST.typ('naeherung', 'Ein würfelförmiger Behälter', 'transfer')
ST.typ('naeherung', 'Das Volumen eines Würfels', 'verknuepfen')
ST.neu('naeherung', 'erkennen', A('Welche Eingabe liefert die positive Lösung von x⁴ = 50?', '⁴√50', ['50 : 4', '50⁴', '4 · √50'],
       'x⁴ = 50 heißt x = ⁴√50 ≈ 2,66 (und −2,66). 50 : 4 = 12,5 wäre viel zu groß.', 'Was macht hoch 4 rückgängig?'))
ST.neu('naeherung', 'erkennen', A('Ist ³√40 eher 3,1 oder 3,4?', '3,4', ['3,1', 'genau 3,5', 'größer als 4'],
       '3³ = 27 und 4³ = 64. 40 liegt näher an 27, aber ³√40 ≈ 3,42. 3,1³ ≈ 29,8 wäre zu klein.', 'Rechne 3,1³ und 3,4³ grob.'))
ST.neu('naeherung', 'einkleidung', Z('Ein würfelförmiger Tank soll 2 m³ fassen. Wie lang ist eine Kante, auf ganze cm gerundet?', 126, '125.99210498949',
       '∛2 ≈ 1,2599 m ≈ 126 cm.', 'Erst in m, dann in cm.', einheit='cm', toleranz=1))
ST.neu('naeherung', 'umkehr', Z('Für welche Zahl c hat x⁴ = c die positive Lösung 1,5?', 5.0625, '1.5 ** 4',
       'c = 1,5⁴ = 2,25 · 2,25 = 5,0625.', 'Rechne rückwärts: hoch 4.'))
ST.neu('naeherung', 'fehler', A('Jemand löst x⁴ = 20 mit dem Taschenrechner: x ≈ 2,11 und sagt: „Das ist die einzige Lösung.“ Was stimmt?', 'Falsch: Auch x ≈ −2,11 ist Lösung.',
       ['Richtig.', 'Falsch: x ≈ 5.', 'Falsch: Es gibt vier Lösungen.'], 'Gerader Exponent, c > 0: zwei Lösungen ±⁴√20 ≈ ±2,11.', 'Gerader oder ungerader Exponent?'))
ST.neu('naeherung', 'begruenden', A('Stimmt: ³√2 liegt näher an 1 als an 2?', 'Ja, denn 1,5³ = 3,375 > 2, also ist ³√2 < 1,5.', ['Nein, ³√2 ≈ 1,7.', 'Nein, genau in der Mitte.', 'Das kann man ohne Taschenrechner nicht sagen.'],
       'Die Mitte zwischen 1 und 2 ist 1,5. 1,5³ = 3,375 ist schon größer als 2, also liegt ³√2 ≈ 1,26 unter 1,5.', 'Prüfe die Mitte 1,5.'))
ST.neu('naeherung', 'parameter', Z('Die positive Lösung von x⁴ = k soll zwischen 2 und 2,1 liegen. Welches ist die kleinste ganze Zahl k, für die das gilt?', 17, '2 ** 4 + 1',
       '2⁴ = 16 und 2,1⁴ = 19,4481. Also 16 < k < 19,45: k = 17, 18, 19. Kleinste: 17.', 'Rechne 2⁴ und 2,1⁴.'))
ST.neu('naeherung', 'rueckwaerts', L('Die Kante eines Würfels ist auf eine Nachkommastelle gerundet 2,2 cm. Welche ganzzahligen Werte (in cm³) kann sein Volumen haben?', '□ oder □', [10, 11], ['10', '11'],
       'Die Kante liegt zwischen 2,15 und 2,25 cm. 2,15³ ≈ 9,94 und 2,25³ ≈ 11,39. Ganze Zahlen dazwischen: 10 und 11.', 'Welche Kanten werden auf 2,2 gerundet?'))
ST.neu('naeherung', 'pruefung', L('x⁵ = 200. a) Zwischen welchen ganzen Zahlen liegt x? b) Gib x auf eine Nachkommastelle in Zehnteln an (2,9 schreibst du als 29).', 'a) □ bis □; b) □', [2, 3, 29], ['2', '3', '29'],
       'a) 2⁵ = 32 < 200 < 243 = 3⁵. b) ⁵√200 ≈ 2,885 ≈ 2,9.', 'a) ohne, b) mit Taschenrechner.'))
ST.neu('naeherung', 'transfer', Z('Bakterien werden pro Stunde mit demselben Faktor mehr. Nach 4 Stunden sind es 5-mal so viele. Wie groß ist der Faktor pro Stunde? Runde auf zwei Nachkommastellen.', 1.5, '1.4953487812212',
       'q⁴ = 5 ⇒ q = ⁴√5 ≈ 1,495 ≈ 1,50.', 'Stelle q⁴ = 5 auf.', toleranz=0.01))
ST.knobel('naeherung', A('Welche Zahl ist größer: ⁴√5 oder ³√3?', '⁴√5', ['³√3', 'Beide sind gleich.', 'Das kann man nicht entscheiden.'],
          'Beide hoch 12 nehmen: (⁴√5)¹² = 5³ = 125 und (³√3)¹² = 3⁴ = 81. Wegen 125 > 81 ist ⁴√5 größer (≈ 1,495 gegen ≈ 1,442).', 'Mit welcher Potenz verschwinden beide Wurzeln?'))
ST.knobel('naeherung', Z('Die Kante eines Würfels wird um 10 % länger. Um wie viel Prozent wächst sein Volumen? Gib eine Nachkommastelle an.', 33.1, '(1.1 ** 3 - 1) * 100',
          'Neue Kante 1,1a, neues Volumen 1,1³ · a³ = 1,331 · a³. Das Volumen wächst um 33,1 %, nicht um 30 %.', 'Rechne mit dem Faktor 1,1.', einheit='%'))

# sachaufgabe
ST.stufenleiter('sachaufgabe', 'Die Kante eines Würfels aus dem Volumen bestimmen.',
                'Zinsfaktor über zwei Jahre, Platten zählen, Kisten und Quader umschmelzen, Endbetrag mit Zinseszins.',
                'Glasfläche, Kugelmasse, wachsende Kanten, Fehler V : 3, Unmöglichkeit begründen, Quader mit Kanten a, 2a, 4a, mehrteilige Aufgabe.')
ST.typ('sachaufgabe', '/^(Ein Würfel aus Beton|Ein würfelförmiger Karton|Ein Holzwürfel)/', 'direkt')
ST.typ('sachaufgabe', '/^(Ein Guthaben|Ein Würfel hat)/', 'mehrschritt')
ST.typ('sachaufgabe', '/^(Eine quadratische Terrasse|Eine Kiste|Ein Quader \\(|Ein quadratisches Feld)/', 'einkleidung')
ST.typ('sachaufgabe', '/^(Ein Aquarium|Die Masse|Ein quaderförmiger)/', 'transfer')
ST.typ('sachaufgabe', 'Jede Kante', 'verknuepfen')
ST.neu('sachaufgabe', 'erkennen', A('Ein Würfel hat 343 cm³ Volumen. Welche Gleichung gilt für die Kante a?', 'a³ = 343', ['3a = 343', 'a² = 343', '6a² = 343'],
       'Volumen eines Würfels: a · a · a = a³.', 'Wie berechnet man das Volumen eines Würfels?'))
ST.neu('sachaufgabe', 'umkehr', Z('Ein Kapital von 2 000 € wird 2 Jahre mit 5 % Zinseszins angelegt. Wie groß ist es danach?', 2205, '2000 * 1.05 ** 2',
       '2 000 · 1,05² = 2 000 · 1,1025 = 2 205 €.', 'Jedes Jahr mal 1,05.', einheit='€'))
ST.neu('sachaufgabe', 'fehler', A('Jemand berechnet die Kante eines Würfels mit 27 dm³ Volumen als 27 : 3 = 9 dm. Was stimmt?', 'Falsch: a³ = 27 ⇒ a = 3 dm.', ['Richtig.', 'Falsch: a = 27 : 6 = 4,5 dm.', 'Falsch: a = √27 dm.'],
       'Kante hoch 3 ergibt das Volumen: 3 · 3 · 3 = 27. 9 · 9 · 9 = 729.', 'Mach die Probe mit a³.'))
ST.neu('sachaufgabe', 'begruenden', A('Kann ein Würfel mit ganzzahliger Kante (in cm) genau 100 cm³ Volumen haben?', 'Nein, 4³ = 64 und 5³ = 125; 100 ist keine Kubikzahl.', ['Ja, mit 10 cm Kante.', 'Ja, mit 5 cm Kante.', 'Ja, mit 4 cm Kante.'],
       'Kubikzahlen in der Nähe: 64 und 125. Dazwischen gibt es keine ganzzahlige Kante.', 'Rechne 4³ und 5³.'))
ST.neu('sachaufgabe', 'parameter', Z('Ein Quader hat die Kanten a, 2a und 4a. Für welches a ist sein Volumen 64 cm³?', 2, '2',
       'V = a · 2a · 4a = 8a³ = 64 ⇒ a³ = 8 ⇒ a = 2 cm.', 'Multipliziere die drei Kanten.', einheit='cm'))
ST.neu('sachaufgabe', 'pruefung', L('Ein würfelförmiger Wassertank fasst 1 000 Liter. a) Wie lang ist eine Innenkante in cm? b) Wie viele Liter fasst ein Tank mit doppelt so langer Kante?', 'a) □ cm; b) □ Liter', [100, 8000],
       ['10 * 10', '1000 * 2 ** 3'], 'a) 1 000 Liter = 1 000 dm³, Kante 10 dm = 100 cm. b) Doppelte Kante: Volumen mal 8 = 8 000 Liter.', '1 Liter = 1 dm³.'))
ST.knobel('sachaufgabe', Z('Ein Würfel wird in 64 gleich große kleine Würfel zersägt. Um wie viel Prozent ist die Oberfläche aller kleinen Würfel zusammen größer als die des großen?', 300, '(64 * 6 / 16 / 6 - 1) * 100',
          'Kante a; kleine Kante a/4 (4 · 4 · 4 = 64). Eine kleine Oberfläche: 6 · (a/4)² = 6a²/16. Alle 64: 64 · 6a²/16 = 4 · 6a². Das ist 4-mal so viel, also 300 % mehr.',
          'Wie lang ist die Kante eines kleinen Würfels?', einheit='%'))
ST.knobel('sachaufgabe', Z('Drei Würfel mit 3 cm, 4 cm und 5 cm Kante werden eingeschmolzen und zu einem einzigen Würfel gegossen. Wie lang ist seine Kante?', 6, '6',
          'Volumen: 27 + 64 + 125 = 216 cm³. ∛216 = 6 cm. (Eine schöne Eigenschaft: 3³ + 4³ + 5³ = 6³.)', 'Addiere die Volumen, nicht die Kanten.', einheit='cm'))

if __name__ == '__main__':
    stufen('gleichungen.potenz', ST)
