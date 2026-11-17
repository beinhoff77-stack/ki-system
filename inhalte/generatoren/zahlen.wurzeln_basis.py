#!/usr/bin/env python3
"""Thema zahlen.wurzeln_basis – Elementare Wurzeln (Klasse 9). Schreibt inhalte/themen/zahlen.wurzeln_basis.json."""
import sys
from math import isqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(901)


def kw(r):
    """ganzzahlige dritte Wurzel"""
    n = round(r ** (1 / 3))
    assert n ** 3 == r
    return n


ETAPPEN = [
    {'lernziel': 'quadratwurzel', 'titel': 'Quadratwurzeln von Quadratzahlen',
     'regel': 'Die ⟦Quadratwurzel⟧ √a ist die Zahl ⟦ohne Minus⟧, die mit sich selbst multipliziert a ergibt. Anschaulich: Ein Quadrat hat die Fläche a – dann ist √a seine ⟦Seitenlänge⟧. Die Zahl unter dem Wurzelzeichen heißt ⟦Radikand⟧.',
     'schritte': ['Ein quadratischer Teppich hat 196 dm² Fläche. Wie lang ist eine Seite? Gesucht ist √196.', '196 liegt zwischen 100 = 10² und 225 = 15². Die Endziffer 6 entsteht nur bei 4 · 4 oder 6 · 6. Also kommt 14 oder 16 in Frage.', '14 · 14 = 196, also √196 = ⟦14⟧. Die Seite ist 14 dm lang.'],
     'probe': '14² = 196 ✓',
     'fehler': '√196 = 98 ist falsch: Wurzelziehen ist nicht halbieren. 98 · 98 = 9 604, nicht 196. Richtig ist ⟦14⟧.',
     'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [14, 0], 'C': [14, 14], 'D': [0, 14]}, 'flaeche': ['A', 'B', 'C', 'D'], 'linien': [['A', 'B', 'a = ?'], ['B', 'C'], ['C', 'D', 'A = 196 dm²'], ['D', 'A']], 'rechter_winkel': [['A', 'B', 'D']]}},
    {'lernziel': 'wurzel_dezimal', 'titel': 'Wurzeln aus Dezimalzahlen und Brüchen',
     'regel': 'Bei Dezimalzahlen hat die Wurzel ⟦halb so viele Nachkommastellen⟧ wie der Radikand. Warum? 0,64 = 64/100, und √(64/100) = 8/10 = 0,8 – aus Hundertsteln werden Zehntel. Bei Brüchen ziehst du aus ⟦Zähler und Nenner⟧ einzeln die Wurzel.',
     'schritte': ['√0,64: 0,64 hat 2 Nachkommastellen, √64 = 8, die Wurzel hat 1 Nachkommastelle.', '√0,64 = ⟦0,8⟧, denn 0,8 · 0,8 = 0,64.', '√(4/81) = √4 / √81 = ⟦2/9⟧.'],
     'probe': '0,8² = 0,64 ✓',
     'fehler': '√0,64 = 0,08 ist falsch: 0,08 · 0,08 = 0,0064. Die Wurzel hat ⟦halb so viele⟧ Nachkommastellen, also 0,8.'},
    {'lernziel': 'kubikwurzel', 'titel': 'Dritte Wurzeln (Kubikwurzeln)',
     'regel': 'Die ⟦dritte Wurzel⟧ ∛a (für a ≥ 0) ist die Zahl, die ⟦dreimal mit sich selbst⟧ multipliziert a ergibt. Sie macht das Hoch-3-Nehmen rückgängig.',
     'schritte': ['Gesucht ist ∛343: Welche Zahl hoch 3 ergibt 343?', '7 · 7 · 7 = 49 · 7 = 343, also ∛343 = ⟦7⟧.'],
     'probe': '7³ = 343 ✓',
     'fehler': '∛343 = 343 : 3 ≈ 114 ist falsch: Die dritte Wurzel ist ⟦nicht durch 3 teilen⟧. Richtig ist 7, denn 7³ = 343.'},
    {'lernziel': 'abschaetzen', 'titel': 'Zwischen welchen Zahlen liegt √a?',
     'regel': 'Ist a keine Quadratzahl, suchst du die ⟦Quadratzahlen direkt darunter und darüber⟧. Die Wurzel liegt zwischen deren Wurzeln.',
     'schritte': ['√90: Die Quadratzahlen um 90 sind 81 und 100.', '√81 = 9 und √100 = 10, also ⟦9 < √90 < 10⟧.'],
     'probe': '9² = 81 < 90 < 100 = 10² ✓',
     'fehler': '„√90 liegt zwischen 45 und 46“ ist falsch: Das ist die Hälfte von 90. Vergleiche mit ⟦Quadratzahlen⟧: 9² = 81, 10² = 100.'},
    {'lernziel': 'wurzel_deuten', 'titel': 'Wurzeln richtig deuten',
     'regel': '√a ist ⟦nie negativ⟧ und nur für ⟦a ≥ 0⟧ erklärt. Die Gleichung x² = a (a > 0) hat aber ⟦zwei Lösungen⟧: √a und −√a.',
     'schritte': ['x² = 25: Sowohl 5² als auch (−5)² ergeben 25.', 'Die Gleichung hat die Lösungen ⟦5 und −5⟧, aber √25 ist nur ⟦5⟧.'],
     'probe': '(−5)² = 25 ✓, 5² = 25 ✓',
     'fehler': '√(9 + 16) = √9 + √16 = 7 ist falsch: Erst den Radikanden berechnen. √(9 + 16) = √25 = ⟦5⟧.'},
    {'lernziel': 'wurzel_sache', 'titel': 'Seitenlänge aus Fläche und Volumen',
     'regel': 'Quadrat: Seitenlänge a = ⟦√A⟧. Würfel: Kantenlänge a = ⟦∛V⟧. Einheiten: aus cm² wird cm, aus cm³ wird cm.',
     'schritte': ['Ein Quadrat hat 169 cm² Flächeninhalt. a = √169 cm.', '13 · 13 = 169, also a = ⟦13 cm⟧.'],
     'probe': '13 cm · 13 cm = 169 cm² ✓',
     'fehler': 'Bei A = 169 cm² ist a = 169 : 4 cm falsch: Durch 4 teilt man den ⟦Umfang⟧, nicht die Fläche. Aus der Fläche zieht man die ⟦Wurzel⟧.'},
]

# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'quadratwurzel': {
  'einstieg': 'Du willst einen quadratischen Teppich kaufen. Im Prospekt steht nur seine Fläche: 196 dm². Wie lang ist eine Seite? Gesucht ist eine Zahl, die mit sich selbst malgenommen 196 ergibt. Diese Zahl heißt ⟦Quadratwurzel⟧ von 196.',
  'woerter': [['Quadratzahl', 'eine Zahl mal sich selbst: 1, 4, 9, 16, 25, … (zum Beispiel 4 · 4 = 16)'],
              ['14²', 'gelesen „14 hoch 2“: 14 · 14'],
              ['Quadratwurzel √196', 'gelesen „Wurzel aus 196“: die Zahl ohne Minus, die mal sich selbst 196 ergibt'],
              ['Radikand', 'die Zahl unter dem Wurzelzeichen, hier 196'],
              ['dm²', 'Quadratdezimeter: die Fläche eines Quadrats mit 1 dm = 10 cm Seitenlänge']],
  'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [14, 0], 'C': [14, 14], 'D': [0, 14]}, 'flaeche': ['A', 'B', 'C', 'D'],
           'linien': [['A', 'B', 'Seite = ?'], ['B', 'C'], ['C', 'D', 'Fläche 196 dm²'], ['D', 'A']], 'rechter_winkel': [['A', 'B', 'D']]},
  'schritte': ['Gesucht ist die Seitenlänge des Teppichs, also √196: eine Zahl, die mal sich selbst 196 ergibt.',
               'Grob eingrenzen: 10 · 10 = 100 ist zu klein, 15 · 15 = 225 ist zu groß. Die Zahl liegt also zwischen 10 und 15.',
               'Auf die letzte Ziffer schauen: Eine 6 am Ende entsteht nur bei 4 · 4 = 16 oder 6 · 6 = 36. Zwischen 10 und 15 passt also nur die 14.',
               'Nachrechnen: 14 · 14 = 196. Also ist √196 = ⟦14⟧, die Teppichseite ist 14 dm lang.'],
  'regel': 'So findest du √a: Suche die Zahl ⟦ohne Minus⟧, die ⟦mit sich selbst malgenommen⟧ a ergibt. Am Quadrat heißt das: √(Fläche) = ⟦Seitenlänge⟧.',
  'fehler': '√196 = 98 ist falsch: Das ist die Hälfte von 196. Ein Teppich mit 98 dm Seite hätte 98 · 98 = 9 604 dm² – viel zu groß. Wurzelziehen ist ⟦nicht halbieren⟧; richtig ist 14.'},
 'wurzel_dezimal': {
  'einstieg': 'Jetzt geht es um etwas Kleines: eine quadratische Fußmatte mit 0,64 m² Fläche. Wie lang ist eine Seite? Wieder suchst du eine Zahl, die mal sich selbst 0,64 ergibt – diesmal eine Kommazahl. Der Trick: erst ohne Komma rechnen, dann das Komma richtig setzen.',
  'woerter': [['Dezimalzahl', 'eine Kommazahl wie 0,64'],
              ['Nachkommastellen', 'die Ziffern hinter dem Komma; 0,64 hat zwei, 0,8 hat eine'],
              ['Zähler / Nenner', 'die Zahl über / unter dem Bruchstrich; bei 4/81 ist 4 der Zähler, 81 der Nenner'],
              ['√(4/81)', 'die Wurzel aus dem ganzen Bruch 4/81']],
  'schritte': ['Lass das Komma zuerst weg: √64 = 8, denn 8 · 8 = 64.',
               'Zähle die Nachkommastellen: 0,64 hat zwei. Die Wurzel bekommt halb so viele, also eine.',
               'Setze das Komma: √0,64 = ⟦0,8⟧. Probe: 0,8 · 0,8 = 0,64. Die Matte ist also 0,8 m = 80 cm breit.',
               'Bei einem Bruch ziehst du oben und unten einzeln die Wurzel: √(4/81) = √4 / √81 = ⟦2/9⟧.'],
  'regel': 'So ziehst du die Wurzel aus einer ⟦Dezimalzahl⟧: ohne Komma die Wurzel ziehen, dann ⟦halb so viele Nachkommastellen⟧ setzen (aus 2 wird 1, aus 4 wird 2). Bei einer ungeraden Zahl von Nachkommastellen (wie 0,9) geht es nicht glatt auf. Bei einem Bruch: Wurzel aus ⟦Zähler und Nenner einzeln⟧.',
  'fehler': '√0,64 = 0,08 ist falsch: 0,08 · 0,08 = 0,0064. Eine Matte mit 8 cm Seite wäre winzig, keine 0,64 m². Richtig sind ⟦halb so viele⟧ Nachkommastellen, also 0,8.'},
 'kubikwurzel': {
  'einstieg': 'Du hast 343 kleine Holzwürfel und willst daraus einen großen, vollen Würfel bauen. Wie viele kleine Würfel liegen dann an einer Kante? Gesucht ist eine Zahl, die dreimal mit sich selbst malgenommen 343 ergibt. Sie heißt ⟦dritte Wurzel⟧ oder Kubikwurzel.',
  'woerter': [['7³', 'gelesen „7 hoch 3“: 7 · 7 · 7'],
              ['∛343', 'gelesen „dritte Wurzel aus 343“: die Zahl, die hoch 3 genommen 343 ergibt'],
              ['Kubikzahl', 'eine Zahl hoch 3: 8, 27, 64, 125, …'],
              ['Kante', 'eine Seite des Würfels']],
  'schritte': ['Gesucht ist ∛343: Welche Zahl ergibt mal sich selbst und dann noch einmal mal sich selbst 343?',
               'Grob schätzen: 5 · 5 · 5 = 125 ist zu wenig, 10 · 10 · 10 = 1 000 ist zu viel. Die Zahl liegt zwischen 5 und 10.',
               'Probiere die 7: Erst 7 · 7 = 49, dann 49 · 7 = 343. Das passt.',
               'Also ist ∛343 = ⟦7⟧: An jeder Kante liegen 7 Würfel.'],
  'regel': 'So findest du ∛a (für a ≥ 0): Suche die Zahl, die ⟦dreimal mit sich selbst malgenommen⟧ a ergibt. Die dritte Wurzel macht das ⟦Hoch-3-Nehmen⟧ rückgängig.',
  'fehler': '∛343 = 343 : 3 ≈ 114 ist falsch. Ein Würfel mit 114 Klötzchen an jeder Kante hätte über eine Million Klötzchen. Die dritte Wurzel ist ⟦nicht durch 3 teilen⟧; richtig ist 7, denn 7³ = 343.'},
 'abschaetzen': {
  'einstieg': 'Nicht jede Fläche passt zu einer glatten Seitenlänge. Ein quadratisches Beet soll 90 m² groß sein. Mit 9 m Seite hätte es 81 m² – zu wenig. Mit 10 m Seite hätte es 100 m² – zu viel. Die Seite liegt also irgendwo zwischen 9 m und 10 m.',
  'woerter': [['<', '„kleiner als“: 9 < 10 heißt „9 ist kleiner als 10“'],
              ['9 < √90 < 10', '√90 liegt zwischen 9 und 10'],
              ['eingrenzen', 'eine Zahl darunter und eine Zahl darüber finden']],
  'schritte': ['Gesucht ist, zwischen welchen ganzen Zahlen √90 liegt.',
               'Suche die Quadratzahl direkt unter 90: Das ist 81, denn 9 · 9 = 81.',
               'Suche die Quadratzahl direkt über 90: Das ist 100, denn 10 · 10 = 100.',
               '90 liegt zwischen 81 und 100, also liegt die Wurzel zwischen 9 und 10: ⟦9 < √90 < 10⟧.'],
  'regel': 'So grenzt du √a ein: Suche die ⟦Quadratzahlen direkt unter und direkt über a⟧. Die Wurzel liegt zwischen deren Wurzeln.',
  'fehler': '„√90 liegt zwischen 45 und 46“ ist falsch – das ist die Hälfte von 90. Ein Beet mit 45 m Seite hätte über 2 000 m². Vergleiche mit ⟦Quadratzahlen⟧: 9² = 81, 10² = 100.'},
 'wurzel_deuten': {
  'einstieg': 'Ein Zahlenrätsel: „Ich denke mir eine Zahl und nehme sie mal sich selbst. Heraus kommt 25.“ Welche Zahl war es? 5 passt, denn 5 · 5 = 25. Aber auch −5 passt, denn minus mal minus ergibt plus. Das Wurzelzeichen meint dagegen immer nur die Zahl ⟦ohne Minus⟧.',
  'woerter': [['x', 'ein Platzhalter für die gesuchte Zahl'],
              ['x² = 25', 'die Frage: Welche Zahl mal sich selbst ergibt 25?'],
              ['Lösung', 'eine Zahl, für die die Gleichung stimmt'],
              ['(−5)²', '(−5) · (−5) = 25 – die Klammer zeigt, dass das Minus mit malgenommen wird']],
  'schritte': ['Die Gleichung x² = 25 fragt: Welche Zahlen ergeben mal sich selbst 25?',
               '5 · 5 = 25, also ist 5 eine Lösung.',
               '(−5) · (−5) = 25, denn minus mal minus ergibt plus. Also ist auch −5 eine Lösung.',
               'Die Gleichung hat die Lösungen ⟦5 und −5⟧. Das Zeichen √25 meint aber nur die Zahl ohne Minus: √25 = ⟦5⟧.'],
  'regel': '√a ist ⟦nie negativ⟧ und nur für ⟦a ≥ 0⟧ erklärt. Die Gleichung x² = a (mit a > 0) hat dagegen ⟦zwei Lösungen⟧: √a und −√a. Steht unter der Wurzel eine Rechnung, rechnest du sie zuerst aus.',
  'fehler': '√(9 + 16) = √9 + √16 = 7 ist falsch. Erst ausrechnen, was unter der Wurzel steht: 9 + 16 = 25, und √25 = ⟦5⟧. Probe: 7 · 7 = 49, nicht 25.'},
 'wurzel_sache': {
  'einstieg': 'Zwei Aufgaben aus dem Bastelzimmer: Ein quadratisches Bilderglas soll 169 cm² groß sein, und ein würfelförmiger Karton soll 1 000 cm³ fassen. In beiden Fällen kennst du die Größe und suchst die Seitenlänge. Beim Quadrat hilft die Quadratwurzel, beim Würfel die dritte Wurzel.',
  'woerter': [['Flächeninhalt A', 'wie viel Fläche etwas bedeckt, z. B. in cm²'],
              ['Volumen V', 'der Rauminhalt: wie viele 1-cm-Würfel hineinpassen, in cm³'],
              ['Umfang', 'die Länge einmal ringsherum']],
  'schritte': ['Das Glas ist ein Quadrat mit A = 169 cm². Für die Seite a gilt a · a = 169.',
               '13 · 13 = 169, also ist a = √169 cm = ⟦13 cm⟧.',
               'Der Karton ist ein Würfel mit V = 1 000 cm³. Für die Kante a gilt a · a · a = 1 000.',
               '10 · 10 · 10 = 1 000, also ist a = ∛1 000 cm = ⟦10 cm⟧.'],
  'probe': '13 cm · 13 cm = 169 cm² ✓; 10 cm · 10 cm · 10 cm = 1 000 cm³ ✓',
  'regel': 'Quadrat: Seitenlänge a = ⟦√A⟧. Würfel: Kantenlänge a = ⟦∛V⟧. Bei den Einheiten wird aus cm² und aus cm³ wieder cm.',
  'fehler': 'Bei A = 169 cm² ist a = 169 : 4 falsch. Durch 4 teilt man den ⟦Umfang⟧, also die Länge ringsum – nicht die Fläche. Aus der Fläche zieht man die ⟦Wurzel⟧.'},
}
klar(ETAPPEN, KLAR)
# ---- KLAR ENDE ----
# ---- UMBAU (neues Muster, Runde 8, Vorgabe 16.11.) ----
Q14 = {'_A': [0, 0], '_B': [14, 0], '_C': [14, 14], '_D': [0, 14]}
QUADRAT = lambda s, n: {f'_{n}1': [0, 0], f'_{n}2': [s, 0], f'_{n}3': [s, s], f'_{n}4': [0, s]}
RAND = lambda n, txt='', art=None: [[f'_{n}1', f'_{n}2', txt] + ([art] if art else []), [f'_{n}2', f'_{n}3', ''] + ([art] if art else []),
                                   [f'_{n}3', f'_{n}4', ''] + ([art] if art else []), [f'_{n}4', f'_{n}1', ''] + ([art] if art else [])]
UMBAU = {
 'quadratwurzel': {
  'einstieg': 'Ein quadratischer Teppich hat 196 dm² Fläche. Wie lang ist eine Seite? Gesucht ist eine Zahl, die mal sich selbst 196 ergibt: die ⟦Quadratwurzel⟧.',
  'woerter': [['Quadratwurzel', 'die Zahl ohne Minus, die mal sich selbst die Zahl unter der Wurzel ergibt'],
              ['√196', 'gelesen „Wurzel aus 196“'],
              ['dm²', 'Quadratdezimeter: ein Quadrat mit 10 cm Seite']],
  'bild': {'typ': 'figur', 'punkte': {**QUADRAT(14, 'q')}, 'flaeche': ['_q1', '_q2', '_q3', '_q4'],
           'linien': [['_q1', '_q2', 'Seite = ?'], ['_q2', '_q3', ''], ['_q3', '_q4', '196 dm²'], ['_q4', '_q1', '']],
           'rechter_winkel': [['_q1', '_q2', '_q4']]},
  'schritte': [{'text': 'Gesucht ist √196: eine Zahl, die mal sich selbst 196 ergibt.'},
               {'text': '10 · 10 = 100 ist zu klein, 15 · 15 = 225 zu groß.',
                'bild': {'punkte': {**QUADRAT(14, 'q'), **QUADRAT(10, 'k'), **QUADRAT(15, 'g')},
                         'linien': [['_q1', '_q2', ''], ['_q2', '_q3', ''], ['_q3', '_q4', ''], ['_q4', '_q1', '']]
                                   + [['_k2', '_k3', '100', 'gestrichelt'], ['_k3', '_k4', '', 'gestrichelt'],
                                      ['_g2', '_g3', '225', 'gestrichelt'], ['_g3', '_g4', '', 'gestrichelt']]}},
               {'text': 'Probiere 14: 14 · 14 = 196. Das passt genau.',
                'bild': {'punkte': {**QUADRAT(14, 'q')},
                         'linien': [['_q1', '_q2', 'Seite = 14 dm'], ['_q2', '_q3', ''], ['_q3', '_q4', '196 dm²'], ['_q4', '_q1', '']]}},
               {'text': 'Also ist √196 = ⟦14⟧. Die Teppichseite ist 14 dm lang.'}],
  'fehler': '√196 ist nicht 98, die Hälfte von 196. Ein Teppich mit 98 dm Seite hätte 9 604 dm² – viel zu groß.',
  'fehler_bild': {'punkte': {**QUADRAT(14, 'q'), **QUADRAT(98, 'f')},
                  'linien': [['_q2', '_q3', '14 dm'], ['_q3', '_q4', '']] + [['_f1', '_f2', '98 dm: 9 604 dm²', 'gestrichelt'],
                             ['_f2', '_f3', '', 'gestrichelt'], ['_f3', '_f4', '', 'gestrichelt'], ['_f4', '_f1', '', 'gestrichelt']]},
  'regel': '√a ist die Zahl ohne Minus, die mal sich selbst a ergibt. Am Quadrat gilt: ⟦Seite = √Fläche⟧.'},
 'wurzel_dezimal': {
  'einstieg': 'Eine quadratische Fußmatte hat 0,64 m² Fläche. Wie lang ist eine Seite? Jetzt suchst du die Wurzel aus einer ⟦Dezimalzahl⟧.',
  'woerter': [['Dezimalzahl', 'eine Kommazahl wie 0,64'],
              ['Nachkommastellen', 'die Ziffern hinter dem Komma; 0,64 hat zwei'],
              ['Zähler und Nenner', 'die Zahl über und die Zahl unter dem Bruchstrich']],
  'bild': {'typ': 'figur', 'punkte': {**QUADRAT(0.8, 'q')}, 'flaeche': ['_q1', '_q2', '_q3', '_q4'],
           'linien': [['_q1', '_q2', 'Seite = ?'], ['_q2', '_q3', ''], ['_q3', '_q4', '0,64 m²'], ['_q4', '_q1', '']],
           'rechter_winkel': [['_q1', '_q2', '_q4']]},
  'schritte': [{'text': 'Lass das Komma zuerst weg: √64 = 8, denn 8 · 8 = 64.'},
               {'text': '0,64 hat zwei Nachkommastellen. Die Wurzel bekommt halb so viele, also eine.'},
               {'text': 'Also ist √0,64 = ⟦0,8⟧. Die Matte ist 0,8 m = 80 cm breit.',
                'bild': {'linien': [['_q1', '_q2', 'Seite = 0,8 m'], ['_q2', '_q3', ''], ['_q3', '_q4', '0,64 m²'], ['_q4', '_q1', '']]}},
               {'text': 'Bei einem Bruch ziehst du aus Zähler und Nenner einzeln die Wurzel: √(4/81) = ⟦2/9⟧.'}],
  'fehler': '√0,64 ist nicht 0,08, denn 0,08 · 0,08 = 0,0064. Die Matte hätte dann nur 8 cm Seite – winzig.',
  'fehler_bild': {'punkte': {**QUADRAT(0.8, 'q'), **QUADRAT(0.08, 'f')},
                  'linien': [['_q1', '_q2', '0,8 m'], ['_q2', '_q3', ''], ['_q3', '_q4', ''], ['_q4', '_q1', '']]
                            + [['_f2', '_f3', '0,08 m?', 'gestrichelt'], ['_f3', '_f4', '', 'gestrichelt']]},
  'regel': 'Erst ohne Komma die Wurzel ziehen, dann ⟦halb so viele Nachkommastellen⟧ setzen. Bei Brüchen: Wurzel aus Zähler und Nenner einzeln.'},
 'kubikwurzel': {
  'einstieg': 'Aus 343 kleinen Holzwürfeln soll ein großer, voller Würfel werden. Wie viele liegen an einer Kante? Gesucht ist die ⟦dritte Wurzel⟧ von 343.',
  'woerter': [['dritte Wurzel', 'die Zahl, die dreimal mit sich selbst malgenommen die Zahl ergibt; Zeichen ∛'],
              ['Kante', 'eine Seite des Würfels'],
              ['7³', 'gelesen „7 hoch 3“: 7 · 7 · 7']],
  'bild': {'typ': 'tabelle', 'kopf': ['Kante', '5', '7', '10'], 'zeilen': [['Würfel', '?', '?', '?']]},
  'schritte': [{'text': '5 Würfel je Kante sind zu wenig: 5 · 5 · 5 = 125.',
                'bild': {'zeilen': [['Würfel', '125', '?', '?']]}},
               {'text': '10 Würfel je Kante sind zu viel: 10 · 10 · 10 = 1 000.',
                'bild': {'zeilen': [['Würfel', '125', '?', '1 000']]}},
               {'text': 'Probiere 7: 7 · 7 · 7 = 343. Also gilt 7³ = 343.',
                'bild': {'zeilen': [['Würfel', '125', '343', '1 000']]}},
               {'text': 'Also ist ∛343 = ⟦7⟧. An jeder Kante liegen 7 Würfel.'}],
  'fehler': '∛343 ist nicht 343 : 3 ≈ 114. Mit 114 Würfeln an jeder Kante bräuchtest du über eine Million Würfel.',
  'fehler_bild': {'kopf': ['Kante', '7', '114'], 'zeilen': [['Würfel', '343', '1 481 544']]},
  'regel': '∛a ist die Zahl, die hoch 3 genau a ergibt. Die ⟦dritte Wurzel⟧ macht das Hoch-3-Nehmen rückgängig.'},
 'abschaetzen': {
  'einstieg': 'Ein quadratisches Beet soll 90 m² groß sein. Mit 9 m Seite sind es 81 m², mit 10 m schon 100 m². Die Seite kannst du ⟦eingrenzen⟧.',
  'woerter': [['eingrenzen', 'eine Zahl darunter und eine Zahl darüber finden'],
              ['Quadratzahl', 'eine ganze Zahl mal sich selbst: 81 = 9 · 9'],
              ['9 < √90 < 10', '√90 ist größer als 9 und kleiner als 10']],
  'bild': {'typ': 'zahlenstrahl', 'start': 70, 'ende': 110, 'abschnitte': 8, 'beschriftet': 'anfang_ende',
           'punkte': [{'wert': 90, 'name': '90'}]},
  'schritte': [{'text': 'Gesucht: Zwischen welchen ganzen Zahlen liegt √90?'},
               {'text': 'Die Quadratzahl direkt unter 90 ist 81 = 9 · 9.',
                'bild': {'punkte': [{'wert': 81, 'name': '9²'}, {'wert': 90, 'name': '90'}]}},
               {'text': 'Die Quadratzahl direkt über 90 ist 100 = 10 · 10.',
                'bild': {'punkte': [{'wert': 81, 'name': '9²'}, {'wert': 90, 'name': '90'}, {'wert': 100, 'name': '10²'}],
                         'bereich': {'von': 81, 'bis': 100}}},
               {'text': 'Also liegt die Wurzel zwischen 9 und 10: ⟦9 < √90 < 10⟧.',
                'bild': {'typ': 'zahlenstrahl', 'start': 8, 'ende': 11, 'abschnitte': 6, 'beschriftet': 'anfang_ende',
                         'bereich': {'von': 9, 'bis': 10}, 'punkte': [{'wert': 9.49, 'name': '√90'}]}}],
  'fehler': '√90 liegt nicht bei 45, der Hälfte von 90. Ein Beet mit 45 m Seite hätte 2 025 m².',
  'fehler_bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 50, 'abschnitte': 10, 'beschriftet': 'anfang_ende',
                  'punkte': [{'wert': 9.49, 'name': '√90'}, {'wert': 45, 'name': '45?'}]},
  'regel': 'Suche die ⟦Quadratzahlen⟧ direkt unter und über a. Die Wurzel liegt zwischen deren Wurzeln.'},
 'wurzel_deuten': {
  'einstieg': 'Ein Rätsel: Meine Zahl mal sich selbst ergibt 25. Das passt für 5 und für −5. Das Wurzelzeichen meint aber nur die Zahl ⟦ohne Minus⟧.',
  'woerter': [['x² = 25', 'die Frage: Welche Zahl mal sich selbst ergibt 25?'],
              ['Lösung', 'eine Zahl, für die die Gleichung stimmt'],
              ['(−5)²', '(−5) · (−5); die Klammer zeigt, dass das Minus mitgerechnet wird']],
  'bild': {'typ': 'koordinaten', 'x': [-6, 6], 'y': [0, 30], 'schritt_y': 5,
           'graphen': [{'art': 'potenz', 'a': 1, 'n': 2, 'name': 'Zahl mal sich selbst'}], 'waagrecht': [25]},
  'schritte': [{'text': 'Die Gleichung x² = 25 fragt: Welche Zahlen ergeben mal sich selbst 25?'},
               {'text': '5 · 5 = 25, also ist 5 eine Lösung.', 'bild': {'punkte': [{'x': 5, 'y': 25, 'name': '5'}]}},
               {'text': 'Auch (−5)² = (−5) · (−5) = 25. Minus mal Minus ergibt Plus.',
                'bild': {'punkte': [{'x': -5, 'y': 25, 'name': '−5'}, {'x': 5, 'y': 25, 'name': '5'}]}},
               {'text': 'Die Gleichung hat ⟦zwei Lösungen⟧: 5 und −5. Aber √25 meint nur ⟦5⟧.'}],
  'fehler': '√(9 + 16) ist nicht √9 + √16 = 7. Erst unter der Wurzel rechnen: √25 = 5. Probe: 7 · 7 = 49, nicht 25.',
  'regel': '√a ist ⟦nie negativ⟧ und nur für a ≥ 0 erklärt. x² = a mit a > 0 hat zwei Lösungen: √a und −√a.'},
 'wurzel_sache': {
  'einstieg': 'Ein quadratisches Bilderglas soll 169 cm² groß sein, ein Würfelkarton 1 000 cm³ fassen. Du kennst die Größe und suchst die ⟦Seitenlänge⟧.',
  'woerter': [['Flächeninhalt A', 'wie viel Fläche etwas bedeckt, in cm²'],
              ['Volumen V', 'der Rauminhalt: wie viele 1-cm-Würfel hineinpassen'],
              ['cm³', 'Kubikzentimeter: ein Würfel mit 1 cm Kante']],
  'bild': {'typ': 'figur', 'punkte': {**QUADRAT(13, 'q')}, 'flaeche': ['_q1', '_q2', '_q3', '_q4'],
           'linien': [['_q1', '_q2', 'a = ?'], ['_q2', '_q3', ''], ['_q3', '_q4', 'Glas 169 cm²'], ['_q4', '_q1', '']],
           'rechter_winkel': [['_q1', '_q2', '_q4']]},
  'schritte': [{'text': 'Das Glas hat den Flächeninhalt A = 169 cm².'},
               {'text': '13 · 13 = 169, also ist a = √169 cm = ⟦13 cm⟧.',
                'bild': {'linien': [['_q1', '_q2', 'a = 13 cm'], ['_q2', '_q3', ''], ['_q3', '_q4', 'Glas 169 cm²'], ['_q4', '_q1', '']]}},
               {'text': 'Der Karton hat das Volumen V = 1 000 cm³.',
                'bild': {'typ': 'tabelle', 'kopf': ['Kante a', '9 cm', '10 cm', '11 cm'], 'zeilen': [['Volumen V', '729 cm³', '?', '1 331 cm³']]}},
               {'text': 'Wegen 10³ = 1 000 ist a = ∛1 000 cm = ⟦10 cm⟧.',
                'bild': {'zeilen': [['Volumen V', '729 cm³', '1 000 cm³', '1 331 cm³']]}}],
  'fehler': 'Bei A = 169 cm² ist die Seite nicht 169 : 4. Durch 4 teilt man den Umfang, nicht die Fläche.',
  'regel': 'Seite = √Fläche, Kante = ∛Volumen. Aus ⟦cm² und cm³⟧ wird dabei wieder cm.'},
}
umbau(ETAPPEN, UMBAU)
# ---- UMBAU ENDE ----


def g_quadratwurzel(s):
    if s == 1:
        n = R.randint(2, 15)
    elif s == 2:
        typ = R.random()
        if typ < 0.35:
            n = R.choice([R.randint(16, 25), 10 * R.randint(2, 9)])
        elif typ < 0.7:
            n = R.randint(4, 25)
            return zahl(f'Für welche Zahl x gilt √x = {n}?', f'Quadrieren macht das Wurzelziehen rückgängig: x = {n}² = {dz(n * n)}.',
                        'Was musst du mit {n} tun, um den Radikanden zu bekommen?'.format(n=n), n * n, f'{n} ** 2')
        else:
            w_ = Fr(R.randint(11, 25), 10)
            if w_.denominator == 1: return None
            return zahl(f'Für welche Zahl x gilt √x = {dz(w_)}?', f'x = {dz(w_)}² = {dz(w_)} · {dz(w_)} = {dz(w_ * w_)}.',
                        'Quadriere die Zahl. Achte auf die Nachkommastellen.', w_ * w_, f'{float(w_)} ** 2')
    else:
        typ = R.random()
        if typ < 0.3:
            a, b = R.randint(2, 20), R.randint(2, 20)
            k = R.randint(2, 5)
            text = f'Berechne {k} · √{dz(a * a)} − √{dz(b * b)}.'
            return zahl(text, f'√{dz(a * a)} = {a} und √{dz(b * b)} = {b}, also {k} · {a} − {b} = {dz(k * a - b)}.',
                        'Ziehe zuerst beide Wurzeln, dann Punkt vor Strich.', k * a - b, f'{k} * ({a * a} / {a}) - ({b * b} / {b})')
        if typ < 0.55:
            a, b = R.choice([4, 9, 16, 25, 36]), R.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
            if a == b: return None
            r = isqrt(a * b)
            return zahl(f'Berechne √({a} · {b}).', f'{a} · {b} = {dz(a * b)}, und {r} · {r} = {dz(a * b)}, also √({a} · {b}) = {r}.',
                        'Rechne zuerst aus, was unter der Wurzel steht.', r, f'({a} * {b}) / {r}')
        if typ < 0.8:
            r = R.randint(3, 15)
            m = R.randint(r + 1, 40)
            d = m * m - r * r if R.random() < 0.5 else None
            if d is not None:
                g = m * m
                if isqrt(g - d) ** 2 != g - d or d <= 0: return None
                return zahl(f'Berechne √({dz(g)} − {dz(d)}).', f'Erst den Radikanden: {dz(g)} − {dz(d)} = {dz(r * r)}. √{dz(r * r)} = {r}.',
                            'Erst rechnen, was unter der Wurzel steht – nicht die Wurzel aus jeder Zahl einzeln ziehen.', r, f'({g} - {d}) / {r}')
            x, y = R.randint(1, r * r - 1), None
            y = r * r - x
            if isqrt(x) ** 2 == x and isqrt(y) ** 2 == y: return None
            return zahl(f'Berechne √({dz(x)} + {dz(y)}).', f'Erst den Radikanden: {dz(x)} + {dz(y)} = {dz(r * r)}. √{dz(r * r)} = {r}.',
                        'Erst rechnen, was unter der Wurzel steht.', r, f'({x} + {y}) / {r}')
        n = R.randint(11, 30)
        return zahl(f'Für welche Zahl x gilt √x = {n}?', f'x = {n}² = {dz(n * n)}.',
                    'Quadrieren macht das Wurzelziehen rückgängig.', n * n, f'{n} ** 2')
    r = n * n
    assert isqrt(r) == n
    return zahl(f'Berechne √{dz(r)}.', f'{n} · {n} = {dz(r)}, also √{dz(r)} = {n}.',
                'Welche Zahl ergibt mit sich selbst multipliziert den Radikanden?', n, f'{r} / {n}')


def g_wurzel_dezimal(s):
    if s >= 2 and R.random() < 0.3:
        n = R.randint(2, 9)
        if R.random() < 0.5:
            r = Fr(n * n, 100)
            return auswahl(f'Was ergibt √{dz(r)}?', dz(Fr(n, 10)), [dz(Fr(n, 100)), dz(r * r), dz(Fr(n * n, 2 * 100)) if (n * n) % 2 == 0 else dz(Fr(n, 1))],
                           f'{dz(r)} hat 2 Nachkommastellen, die Wurzel also 1: {dz(Fr(n, 10))}² = {dz(r)}.',
                           'Mache die Probe durch Quadrieren.')
        if n in (4, 9): return None
        r = Fr(n * n, 10)
        return auswahl(f'Was ergibt √{dz(r)}?', f'keine endliche Dezimalzahl, ≈ {dz(round(float(r) ** 0.5, 2))}',
                       [dz(Fr(n, 10)), dz(Fr(n, 100)), dz(r * r)],
                       f'{dz(Fr(n, 10))}² = {dz(Fr(n * n, 100))}, nicht {dz(r)}. {dz(r)} hat eine (ungerade) Zahl von Nachkommastellen; seine Wurzel ist ≈ {dz(round(float(r) ** 0.5, 2))}.',
                       'Quadriere die Antworten zur Probe. Achte auf die Zahl der Nachkommastellen.')
    if s == 1 or (s == 2 and R.random() < 0.5):
        n = R.randint(2, 9) if s == 1 else R.randint(11, 19)
        k = R.choice([1, 2]) if s == 1 else R.choice([1, 2, 3])
        w_ = Fr(n, 10 ** k)
        r = w_ * w_
        return zahl(f'Berechne √{dz(r)}.', f'{dz(w_)} · {dz(w_)} = {dz(r)}, also √{dz(r)} = {dz(w_)}.',
                    'Ziehe die Wurzel ohne Komma und halbiere die Anzahl der Nachkommastellen.', w_, f'{float(r)} / {float(w_)}')
    a, b = R.randint(1, 12), R.randint(2, 15)
    if Fr(a, b).denominator != b: return None
    if s == 3 and R.random() < 0.5:
        k = R.randint(2, 4)
        text = f'Berechne {k} · √({a * a}/{b * b}). Gib das Ergebnis als gekürzten Bruch an.'
        e = Fr(k * a, b)
        return luecken(text, '□/□', 'Zähler / Nenner (gekürzt)', [e.numerator, e.denominator],
                       f'√({a * a}/{b * b}) = {a}/{b}, mal {k} ergibt {br(e)}.',
                       'Erst Zähler und Nenner einzeln radizieren, dann multiplizieren und kürzen.',
                       c=[f'{e.numerator}', f'{e.denominator}'])
    return luecken(f'Berechne √({a * a}/{b * b}).', '□/□', 'Zähler / Nenner', [a, b],
                   f'√{a * a} = {a} und √{b * b} = {b}, also √({a * a}/{b * b}) = {a}/{b}.',
                   'Ziehe die Wurzel aus Zähler und Nenner einzeln.', c=[f'{a * a} // {a}', f'{b * b} // {b}'])


def g_kubikwurzel(s):
    if s == 1:
        n = R.randint(2, 10)
        r = n ** 3
        return zahl(f'Berechne ∛{dz(r)}.', f'{n} · {n} · {n} = {dz(r)}, also ∛{dz(r)} = {n}.',
                    'Welche Zahl ergibt dreimal mit sich selbst multipliziert den Radikanden?', kw(r), f'{r} / ({n} * {n})')
    if s == 2:
        typ = R.random()
        if typ < 0.5:
            n = R.choice([7, 8, 9, 10])
            r = n ** 3
            return zahl(f'Berechne ∛{dz(r)}.', f'{n}³ = {dz(r)}, also ∛{dz(r)} = {n}.',
                        'Probiere Zahlen hoch 3. Endziffer des Radikanden hilft.', kw(r), f'{r} / ({n} * {n})')
        n, k = R.randint(1, 9), R.choice([1, 2])
        w_ = Fr(n, 10 ** k)
        r = w_ ** 3
        return zahl(f'Berechne ∛{dz(r)}.', f'{dz(w_)}³ = {dz(r)}, also ∛{dz(r)} = {dz(w_)}.',
                    'Die dritte Wurzel hat ein Drittel so viele Nachkommastellen wie der Radikand.', w_, f'{float(r)} / ({float(w_)} * {float(w_)})')
    if R.random() < 0.5:
        a, b = R.randint(1, 6), R.randint(2, 10)
        if Fr(a, b).denominator != b: return None
        return luecken(f'Berechne ∛({a ** 3}/{b ** 3}).', '□/□', 'Zähler / Nenner', [a, b],
                       f'∛{a ** 3} = {a} und ∛{b ** 3} = {b}, also {a}/{b}.',
                       'Ziehe die dritte Wurzel aus Zähler und Nenner einzeln.', c=[f'{a ** 3} // ({a} * {a})', f'{b ** 3} // ({b} * {b})'])
    a, b = R.randint(2, 6), R.randint(2, 10)
    return zahl(f'Berechne ∛{dz(a ** 3)} · √{dz(b * b)}.', f'∛{dz(a ** 3)} = {a}, √{dz(b * b)} = {b}, also {a} · {b} = {a * b}.',
                'Ziehe jede Wurzel einzeln, dann multiplizieren.', a * b, f'({a ** 3} / ({a} * {a})) * ({b * b} / {b})')


def g_abschaetzen(s):
    if s >= 2 and R.random() < (0.3 if s == 2 else 0.5):
        r = R.choice([x for x in range(2, 99) if isqrt(x) ** 2 != x])
        z = int((r * 100) ** 0.5)  # Zehntel: z/10 < √r < (z+1)/10
        while (z + 1) ** 2 <= r * 100: z += 1
        while z * z > r * 100: z -= 1
        if R.random() < 0.6:
            u, o = Fr(z, 10), Fr(z + 1, 10)
            return auswahl(f'Zwischen welchen Zehnteln liegt √{r}?', f'{dz(u)} und {dz(o)}',
                           [f'{dz(u - Fr(1, 10))} und {dz(u)}', f'{dz(o)} und {dz(o + Fr(1, 10))}', f'{dz(Fr(r, 2))} und {dz(Fr(r, 2) + Fr(1, 10))}'],
                           f'{dz(u)}² = {dz(u * u)} < {r} < {dz(o * o)} = {dz(o)}², also {dz(u)} < √{r} < {dz(o)}.',
                           'Grenze erst ganzzahlig ein, dann quadriere Zehntel wie 2,5; 2,6; …')
        k = Fr(R.randint(10 * z, 10 * z + 9), 100)
        gut = abs(k * k - r) <= Fr(5, 100)
        if gut:
            richtig = f'Ja, denn {dz(k)}² = {dz(k * k)} liegt sehr nah bei {r}.'
            falsch = [f'Nein, denn {dz(k)}² = {dz(k * k)} ist nicht genau {r}.', f'Nein, denn {dz(k)} · 2 ≠ {r}.', 'Nein, √' + str(r) + ' ist negativ.']
        else:
            richtig = f'Nein, denn {dz(k)}² = {dz(k * k)} weicht deutlich von {r} ab.'
            falsch = [f'Ja, denn {dz(k)}² = {dz(k * k)} liegt sehr nah bei {r}.', f'Ja, denn {dz(k)} · 2 ≈ {r}.', 'Ja, jede Zahl mit zwei Nachkommastellen ist gut genug.']
        return auswahl(f'Ist {dz(k)} eine gute Näherung für √{r} (Abweichung des Quadrats höchstens 0,05)?', richtig, falsch,
                       f'{dz(k)}² = {dz(k * k)}; der Unterschied zu {r} ist {dz(abs(k * k - r))}.',
                       'Quadriere die Näherung und vergleiche mit dem Radikanden.')
    if s == 3 and R.random() < 0.5:
        n = R.randint(2, 9)
        r = R.randint(n ** 3 + 1, (n + 1) ** 3 - 1)
        return luecken(f'Zwischen welchen aufeinanderfolgenden natürlichen Zahlen liegt ∛{dz(r)}?', '□ < ∛' + dz(r) + ' < □',
                       'kleinere Zahl, größere Zahl', [n, n + 1],
                       f'{n}³ = {n ** 3} < {dz(r)} < {(n + 1) ** 3} = {n + 1}³, also {n} < ∛{dz(r)} < {n + 1}.',
                       'Suche die Kubikzahlen direkt unter und über dem Radikanden.', c=[f'{n}', f'{n} + 1'])
    g = {1: (2, 9), 2: (10, 20), 3: (21, 40)}[s]
    n = R.randint(*g)
    r = R.randint(n * n + 1, (n + 1) ** 2 - 1)
    if isqrt(r) != n: return None
    return luecken(f'Zwischen welchen aufeinanderfolgenden natürlichen Zahlen liegt √{dz(r)}?', '□ < √' + dz(r) + ' < □',
                   'kleinere Zahl, größere Zahl', [n, n + 1],
                   f'{n}² = {dz(n * n)} < {dz(r)} < {dz((n + 1) ** 2)} = {n + 1}², also {n} < √{dz(r)} < {n + 1}.',
                   'Suche die Quadratzahlen direkt unter und über dem Radikanden.', c=[f'{n}', f'{n} + 1'])


def g_wurzel_deuten(s):
    typ = R.choice({1: 'abdf', 2: 'abcdef', 3: 'ce'}[s])
    n = R.randint(3, 20)
    q = n * n
    if typ == 'a':
        return auswahl(f'Welche Aussage über √{dz(q)} stimmt?', f'√{dz(q)} = {n}',
                       [f'√{dz(q)} = ±{n}', f'√{dz(q)} = {dz(q // 2) if q % 2 == 0 else dz(Fr(q, 2))}', f'√{dz(q)} = −{n}'],
                       f'Die Wurzel ist immer die nicht-negative Zahl: {n} · {n} = {dz(q)}, also √{dz(q)} = {n}.',
                       'Kann eine Quadratwurzel negativ sein?')
    if typ == 'b':
        return auswahl(f'Welche Lösungen hat die Gleichung x² = {dz(q)}?', f'x = {n} und x = −{n}',
                       [f'nur x = {n}', f'nur x = −{n}', 'keine Lösung'],
                       f'{n}² = {dz(q)} und ({"−"}{n})² = {dz(q)}. Beide Zahlen lösen die Gleichung.',
                       'Prüfe auch die negative Zahl: Was ergibt (−x)²?')
    if typ == 'c':
        a, b = R.randint(2, 12), R.randint(2, 12)
        s_ = a * a + b * b
        if isqrt(s_) ** 2 == s_: return None
        nah = dz(round(s_ ** 0.5, 1))
        richtig = f'Falsch: Erst addieren, dann Wurzel ziehen: √{dz(s_)} ≈ {nah}. Probe: {a + b}² = {dz((a + b) ** 2)} ≠ {dz(s_)}.'
        return auswahl(f'Jemand rechnet: √({a * a} + {b * b}) = √{a * a} + √{b * b} = {a + b}. Was stimmt?', richtig,
                       ['Richtig, man darf die Wurzel aus jedem Summanden einzeln ziehen', f'Falsch: Das Ergebnis ist {a * b}',
                        f'Richtig, denn {a} + {b} = {a + b}'],
                       f'Erst den Radikanden berechnen: {a * a} + {b * b} = {dz(s_)}, √{dz(s_)} ≈ {nah}. Probe: {a + b}² = {dz((a + b) ** 2)} ≠ {dz(s_)}. Die Wurzel aus einer Summe ist nicht die Summe der Wurzeln.',
                       'Rechne zuerst aus, was unter der Wurzel steht, und mache die Probe durch Quadrieren.')
    if typ == 'd':
        return auswahl(f'Was gilt für √(−{dz(q)})?', 'Sie ist nicht definiert (keine reelle Zahl).',
                       [f'√(−{dz(q)}) = −{n}', f'√(−{dz(q)}) = {n}', f'√(−{dz(q)}) = 0'],
                       f'Jede Zahl mal sich selbst ist nie negativ ({n} · {n} = {dz(q)}, (−{n}) · (−{n}) = {dz(q)}). Für −{dz(q)} gibt es keine Quadratwurzel.',
                       'Kann eine Zahl mal sich selbst eine negative Zahl ergeben?')
    if typ == 'e':
        m = R.randint(3, 14)
        r = m * m
        if r % 2 or r // 4 == m: return None
        return auswahl(f'Jemand sagt: „√{dz(r)} = {dz(r // 2)}, denn Wurzelziehen heißt halbieren.“ Was stimmt?',
                       f'Falsch: {dz(r // 2)}² = {dz((r // 2) ** 2)}. Richtig ist √{dz(r)} = {m}.',
                       ['Richtig, Wurzelziehen ist halbieren', f'Falsch: Richtig ist √{dz(r)} = {dz(r // 4) if r % 4 == 0 else r * 2}',
                        f'Falsch: Richtig ist √{dz(r)} = −{m}'],
                       f'Probe durch Quadrieren: {dz(r // 2)} · {dz(r // 2)} = {dz((r // 2) ** 2)} ≠ {dz(r)}. Aber {m} · {m} = {dz(r)}.',
                       'Mache die Probe: Quadriere das behauptete Ergebnis.')
    r = R.choice([x for x in range(2, 99) if isqrt(x) ** 2 != x])
    return auswahl(f'Welchen Wert hat (√{r})²?', dz(r), [f'√{r}', dz(2 * r), dz(r * r)],
                   f'(√{r})² = √{r} · √{r} = {r}, denn √{r} ist genau die Zahl, deren Quadrat {r} ist.',
                   'Was bedeutet √a? Welche Zahl entsteht beim Quadrieren?')


def g_wurzel_sache(s):
    typ = R.random()
    if s == 1:
        n = R.randint(4, 20)
        return zahl(f'Ein quadratisches Beet hat einen Flächeninhalt von {dz(n * n)} m². Wie lang ist eine Seite?',
                    f'a = √{dz(n * n)} m = {n} m, denn {n} · {n} = {dz(n * n)}.', 'Beim Quadrat gilt A = a · a.', n,
                    f'{n * n} / {n}', einheit='m')
    if s == 2:
        if typ < 0.5:
            n = R.randint(2, 12)
            ding = R.choice(['Ein Würfel aus Holz', 'Ein würfelförmiger Behälter', 'Ein Spielwürfel aus Kunststoff', 'Ein Würfel aus Ton'])
            return zahl(f'{ding} hat ein Volumen von {dz(n ** 3)} cm³. Wie lang ist eine Kante?',
                        f'a = ∛{dz(n ** 3)} cm = {n} cm, denn {n}³ = {dz(n ** 3)}.', 'Beim Würfel gilt V = a · a · a.', n,
                        f'{n ** 3} / ({n} * {n})', einheit='cm')
        n = R.randint(5, 30)
        return zahl(f'Ein quadratischer Platz hat {dz(n * n)} m² Fläche. Wie lang ist sein Umfang?',
                    f'Seite a = √{dz(n * n)} m = {n} m. Umfang u = 4 · {n} m = {4 * n} m.',
                    'Bestimme zuerst die Seitenlänge, dann den Umfang.', 4 * n, f'4 * ({n * n} / {n})', einheit='m')
    if typ < 0.4:
        n = R.randint(2, 15)
        o = 6 * n * n
        return zahl(f'Ein Würfel hat eine Oberfläche von {dz(o)} cm². Wie lang ist eine Kante?',
                    f'Eine Seitenfläche: {dz(o)} : 6 = {dz(n * n)} cm². a = √{dz(n * n)} cm = {n} cm.',
                    'Ein Würfel hat 6 gleiche quadratische Seitenflächen.', n, f'({o} / 6) / {n}', einheit='cm')
    if typ < 0.7:
        n = R.randint(2, 10)
        return zahl(f'Ein Würfel hat ein Volumen von {dz(n ** 3)} dm³. Wie groß ist seine Oberfläche?',
                    f'a = ∛{dz(n ** 3)} dm = {n} dm. O = 6 · {n}² dm² = {dz(6 * n * n)} dm².',
                    'Bestimme zuerst die Kantenlänge aus dem Volumen.', 6 * n * n, f'6 * ({n ** 3} / ({n} * {n})) ** 2', einheit='dm²')
    if typ < 0.85:
        if R.random() < 0.5:
            A_ = R.choice([x for x in range(50, 900, 10) if isqrt(x) ** 2 != x])
            w_ = gerundet(A_ ** 0.5, 1)
            if w_ is None: return None
            return zahl(f'Ein quadratischer Garten hat {dz(A_)} m² Fläche. Wie lang ist eine Seite? Runde auf eine Nachkommastelle.',
                        f'a = √{dz(A_)} m ≈ {dz(w_)} m. Probe: {dz(w_)}² ≈ {dz(round(w_ * w_, 2))}.',
                        'Ziehe die Wurzel mit dem Taschenrechner und runde.', w_, f'round({K(A_ ** 0.5)}, 1)', einheit='m')
        V = R.choice([x for x in range(100, 2000, 50) if round(x ** (1 / 3)) ** 3 != x])
        w_ = gerundet(V ** (1 / 3), 1)
        if w_ is None: return None
        return zahl(f'Ein würfelförmiger Behälter fasst {dz(V)} cm³. Wie lang ist eine Kante? Runde auf eine Nachkommastelle.',
                    f'a = ∛{dz(V)} cm ≈ {dz(w_)} cm. Probe: {dz(w_)}³ ≈ {dz(round(w_ ** 3, 1))}.',
                    'Beim Würfel gilt V = a³. Nutze die ∛-Taste des Taschenrechners.', w_, f'round({K(V ** (1 / 3))}, 1)', einheit='cm')
    n = R.randint(3, 6)
    k = R.randint(2, 6)
    return zahl(f'{k} gleich große quadratische Fliesen bedecken zusammen {dz(k * n * n)} dm². Wie lang ist eine Fliesenseite?',
                f'Eine Fliese: {dz(k * n * n)} : {k} = {dz(n * n)} dm². Seite = √{dz(n * n)} dm = {n} dm.',
                'Berechne zuerst die Fläche einer einzelnen Fliese.', n, f'({k * n * n} / {k}) / {n}', einheit='dm')


GEN = {'quadratwurzel': g_quadratwurzel, 'wurzel_dezimal': g_wurzel_dezimal, 'kubikwurzel': g_kubikwurzel,
       'abschaetzen': g_abschaetzen, 'wurzel_deuten': g_wurzel_deuten, 'wurzel_sache': g_wurzel_sache}

# ---------- Zehnte Runde (schwer-kl9): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Abschnitt mit eigenem festen Zufallsstart (anhaengen(..., 9901, ...)), läuft erst nach bauen():
# alle bisherigen Aufgaben bleiben unverändert. Vorbilder: Bayerischer Mathematik-Test 10 (ISB, Terme ohne
# Taschenrechner, Näherungswert einer Wurzel am Graphen von y = x²), Illustrierende Aufgaben Realschule 9 (I)
# (Fachbegriffe, Behauptungen beurteilen), Känguru (Würfel-Knobelei). Zahlen und Wortlaut eigen.
from _schwer_kl9 import anhaengen  # noqa: E402


def schwer():
    P, K, O = 'pruefung', 'knobel', ''
    parabel = lambda y: {'typ': 'koordinaten', 'x': [0, 3], 'y': [0, 7], 'graphen': [{'art': 'poly', 'k': [0, 0, 1], 'name': 'y = x²'}],
                         'waagrecht': [y], 'schritt_x': 0.5}
    return [
        # quadratwurzel
        ('quadratwurzel', 3, P, zahl('Berechne ohne Taschenrechner √(13² − 12²).',
                                     'Erst unter der Wurzel rechnen: 13² − 12² = 169 − 144 = 25. Dann √25 = 5. Falle: 13 − 12 = 1 ist falsch.',
                                     'Rechne zuerst aus, was unter der Wurzel steht. Die Wurzel wirkt nicht auf jede Zahl einzeln.', 5, '(13**2 - 12**2) / 5')),
        ('quadratwurzel', 3, P, zahl('Berechne ohne Taschenrechner √(25² − 7²).',
                                     'Erst unter der Wurzel: 625 − 49 = 576. Dann √576 = 24, denn 24 · 24 = 576. Falle: 25 − 7 = 18 ist falsch.',
                                     'Erst die beiden Quadrate ausrechnen und subtrahieren, dann die Wurzel ziehen.', 24, '(25**2 - 7**2) / 24')),
        ('quadratwurzel', 3, K, zahl('Wie viele natürliche Zahlen n gibt es, für die 10 < √n < 11 gilt?',
                                     '10 < √n < 11 bedeutet 10² < n < 11², also 100 < n < 121. Das sind die Zahlen 101 bis 120: 20 Stück.',
                                     'Quadriere die beiden Grenzen. Zwischen welchen Zahlen muss n dann liegen?', 20, '11**2 - 10**2 - 1')),
        ('quadratwurzel', 3, O, zahl('Für welche Zahl x gilt √x = √36 + √64?',
                                     'Rechte Seite: √36 + √64 = 6 + 8 = 14. Also √x = 14 und x = 14² = 196. Falle: 36 + 64 = 100 ist falsch, denn √100 = 10.',
                                     'Rechne zuerst die rechte Seite aus. Dann rückwärts: Welche Zahl hat diese Wurzel?', 196, '(6 + 8) ** 2')),
        ('quadratwurzel', 2, O, zahl('Berechne √(2 · 98).', '2 · 98 = 196 und 14 · 14 = 196, also √(2 · 98) = 14.',
                                     'Rechne erst das Produkt unter der Wurzel aus.', 14, '(2 * 98) / 14')),
        ('quadratwurzel', 2, O, zahl('Berechne √900 − √9.', '√900 = 30 und √9 = 3, also 30 − 3 = 27.',
                                     'Ziehe beide Wurzeln einzeln, dann subtrahiere.', 27, '900 / 30 - 9 / 3')),
        # wurzel_dezimal
        ('wurzel_dezimal', 3, P, zahl('Ein quadratisches Solarmodul hat einen Flächeninhalt von 2,56 m². Wie lang ist eine Seite in Zentimetern?',
                                      '√2,56 = 1,6, denn 1,6 · 1,6 = 2,56. Die Seite ist 1,6 m = 160 cm lang.',
                                      'Zuerst die Seite in Metern bestimmen (halb so viele Nachkommastellen), dann in cm umrechnen.', 160,
                                      '(2.56 / 1.6) * 100', einheit='cm')),
        ('wurzel_dezimal', 3, P, zahl('Berechne ohne Taschenrechner √(1 − 0,36).',
                                      'Erst unter der Wurzel: 1 − 0,36 = 0,64. Dann √0,64 = 0,8. Falle: 1 − √0,36 = 1 − 0,6 = 0,4 ist etwas anderes.',
                                      'Erst die Differenz unter der Wurzel ausrechnen, dann die Wurzel ziehen.', 0.8, '(1 - 0.36) / 0.8')),
        ('wurzel_dezimal', 3, K, auswahl('Bei welcher Zahl hat die Quadratwurzel genau eine Nachkommastelle?', '0,04',
                                         ['0,4', '0,004', '0,0004'],
                                         '√0,04 = 0,2. Bei 0,0004 kommt 0,02 heraus (zwei Nachkommastellen). 0,4 und 0,004 haben eine ungerade Zahl von Nachkommastellen – ihre Wurzeln gehen nicht auf (√0,4 ≈ 0,632).',
                                         'Die Wurzel hat halb so viele Nachkommastellen wie die Zahl. Das klappt nur bei einer geraden Anzahl.')),
        ('wurzel_dezimal', 3, O, zahl('Berechne √(49/100) + √0,81. Gib das Ergebnis als Dezimalzahl an.',
                                      '√(49/100) = 7/10 = 0,7 und √0,81 = 0,9. Zusammen 0,7 + 0,9 = 1,6.',
                                      'Ziehe beide Wurzeln einzeln und schreibe den Bruch als Dezimalzahl.', 1.6, '7 / 10 + 0.81 / 0.9')),
        ('wurzel_dezimal', 2, O, zahl('Für welche Zahl x gilt √x = 0,03?', 'Quadrieren: x = 0,03 · 0,03 = 0,0009 (doppelt so viele Nachkommastellen).',
                                      'Rückwärts: Quadriere 0,03. Achte auf die Nachkommastellen.', 0.0009, '0.03 ** 2')),
        ('wurzel_dezimal', 2, O, luecken('Berechne √(144/25).', '□/□', 'Zähler und Nenner eintragen', [12, 5],
                                         '√144 = 12 und √25 = 5, also √(144/25) = 12/5.', 'Ziehe aus Zähler und Nenner einzeln die Wurzel.', ['144 / 12', '25 / 5'])),
        # kubikwurzel
        ('kubikwurzel', 3, P, zahl('Ein Würfel hat das Volumen 64 cm³. Ein zweiter Würfel hat das 8-fache Volumen. Wie lang ist eine Kante des zweiten Würfels?',
                                   'Volumen des zweiten Würfels: 8 · 64 cm³ = 512 cm³. Kante: ∛512 cm = 8 cm, denn 8³ = 512. Falle: 8 · 4 cm = 32 cm.',
                                   'Berechne zuerst das neue Volumen, dann die dritte Wurzel.', 8, '(8 * 64) / 8 ** 2', einheit='cm')),
        ('kubikwurzel', 3, P, zahl('Berechne ohne Taschenrechner ∛1 000 − ∛0,125.',
                                   '∛1 000 = 10, denn 10³ = 1 000. ∛0,125 = 0,5, denn 0,5³ = 0,125. Also 10 − 0,5 = 9,5.',
                                   'Ziehe beide dritten Wurzeln einzeln. Tipp: 5³ = 125.', 9.5, '1000 / 100 - 0.125 / 0.25')),
        ('kubikwurzel', 3, K, zahl('125 gleich große Würfelchen werden zu einem großen Würfel zusammengesetzt. Dann wird der große Würfel außen rot angemalt. Wie viele Würfelchen haben gar keine rote Fläche?',
                                   'Kante: ∛125 = 5 Würfelchen. Unbemalt bleibt der innere Würfel mit 5 − 2 = 3 Würfelchen je Kante: 3³ = 27.',
                                   'Wie viele Würfelchen liegen an einer Kante? Innen fehlt an jeder Seite eine Schicht.', 27, '(5 - 2) ** 3')),
        ('kubikwurzel', 3, O, zahl('Für welche Zahl x gilt ∛x = 1,5?', 'Rückwärts: x = 1,5³ = 1,5 · 1,5 · 1,5 = 2,25 · 1,5 = 3,375.',
                                   'Die dritte Wurzel machst du mit „hoch 3“ rückgängig.', 3.375, '1.5 ** 3')),
        ('kubikwurzel', 2, O, luecken('Berechne ∛(8/125).', '□/□', 'Zähler und Nenner eintragen', [2, 5],
                                      '∛8 = 2 und ∛125 = 5, also ∛(8/125) = 2/5.', 'Ziehe aus Zähler und Nenner einzeln die dritte Wurzel.', ['8 / 4', '125 / 25'])),
        ('kubikwurzel', 2, O, zahl('Berechne ∛8 000.', '20³ = 20 · 20 · 20 = 8 000, also ∛8 000 = 20.', 'Denke an 2³ = 8 und 10³ = 1 000.', 20, '8000 / 400')),
        # abschaetzen
        ('abschaetzen', 3, P, bild(auswahl('Die Abbildung zeigt die Parabel y = x² und die waagrechte Linie y = 3,2. Welcher Wert liegt am nächsten an √3,2?', '1,8',
                                           ['1,6', '1,2', '10,24'],
                                           'Die Linie schneidet die Parabel bei x ≈ 1,8. Kontrolle: 1,8² = 3,24 liegt nahe an 3,2. 1,6 ist nur die Hälfte von 3,2; 10,24 = 3,2².',
                                           'Lies ab, bei welchem x die Parabel die Höhe 3,2 erreicht. Prüfe mit Quadrieren.'), parabel(3.2))),
        ('abschaetzen', 3, P, bild(auswahl('Die Abbildung zeigt die Parabel y = x² und die waagrechte Linie y = 5,5. Welcher Wert liegt am nächsten an √5,5?', '2,3',
                                           ['2,75', '1,5', '30,25'],
                                           'Die Linie schneidet die Parabel bei x ≈ 2,3. Kontrolle: 2,3² = 5,29 liegt nahe an 5,5. 2,75 ist die Hälfte, 30,25 = 5,5².',
                                           'Lies ab, bei welchem x die Parabel die Höhe 5,5 erreicht. Prüfe mit Quadrieren.'), parabel(5.5))),
        ('abschaetzen', 3, K, auswahl('Welche natürliche Zahl liegt am nächsten an √156?', '12', ['13', '78', '12,5'],
                                      '12² = 144 und 13² = 169. Die Mitte 12,5 hat 12,5² = 156,25 > 156. Also ist √156 kleiner als 12,5 und liegt näher an 12.',
                                      'Grenze zuerst zwischen zwei Quadratzahlen ein. Dann quadriere die Mitte 12,5.')),
        ('abschaetzen', 3, O, luecken('Zwischen welchen aufeinanderfolgenden natürlichen Zahlen liegt ∛100?', '□ < ∛100 < □', 'die beiden Zahlen eintragen', [4, 5],
                                      '4³ = 64 < 100 < 125 = 5³, also 4 < ∛100 < 5.', 'Suche Kubikzahlen (Zahlen hoch 3) unter und über 100.', ['64 / 16', '125 / 25'])),
        ('abschaetzen', 2, O, auswahl('Zwischen welchen Zehnteln liegt √0,5?', '0,7 und 0,8', ['0,2 und 0,3', '0,07 und 0,08', '0,4 und 0,5'],
                                      '0,7² = 0,49 < 0,5 < 0,64 = 0,8², also 0,7 < √0,5 < 0,8.',
                                      'Quadriere Zehntel wie 0,7 und 0,8 und vergleiche mit 0,5. Die Wurzel aus einer Zahl unter 1 ist größer als die Zahl.')),
        ('abschaetzen', 2, O, luecken('Zwischen welchen aufeinanderfolgenden natürlichen Zahlen liegt √200?', '□ < √200 < □', 'die beiden Zahlen eintragen', [14, 15],
                                      '14² = 196 < 200 < 225 = 15², also 14 < √200 < 15.', 'Welche Quadratzahlen liegen direkt unter und über 200?', ['196 / 14', '225 / 15'])),
        # wurzel_deuten
        ('wurzel_deuten', 3, P, auswahl('Welcher Satz verwendet die Fachbegriffe richtig?', 'Beim Radizieren von 49 erhält man 7; die Zahl 49 heißt Radikand.',
                                        ['Beim Quadrieren von 49 erhält man 7.', 'Der Radikand von √49 ist 7.', 'Beim Radizieren von 49 erhält man 7 und −7.'],
                                        'Radizieren heißt Wurzelziehen: √49 = 7. Die Zahl unter der Wurzel (49) ist der Radikand. Quadrieren wäre 49² = 2 401. Die Wurzel ist nie negativ.',
                                        'Radizieren = Wurzel ziehen, Radikand = Zahl unter der Wurzel.')),
        ('wurzel_deuten', 3, P, zahl('Wie viele Lösungen haben die drei Gleichungen x² = 16, x² = 0 und x² = −16 zusammen?',
                                     'x² = 16: zwei Lösungen (4 und −4). x² = 0: nur x = 0. x² = −16: keine, denn ein Quadrat ist nie negativ. Zusammen 2 + 1 + 0 = 3.',
                                     'Untersuche jede Gleichung einzeln. Kann ein Quadrat negativ sein?', 3, '2 + 1 + 0')),
        ('wurzel_deuten', 3, K, auswahl('Für welche Zahlen a gilt √a = a?', 'für a = 0 und a = 1', ['nur für a = 1', 'für jede Zahl a ≥ 0', 'für keine Zahl'],
                                        '√0 = 0 und √1 = 1. Für andere Zahlen nicht: √4 = 2 ≠ 4 und √0,25 = 0,5 ≠ 0,25.',
                                        'Quadriere beide Seiten: a = a². Welche Zahlen ändern sich beim Quadrieren nicht?')),
        ('wurzel_deuten', 3, O, auswahl('Jemand behauptet: „√(a²) = a gilt für jede Zahl a.“ Prüfe mit a = −3.', 'Falsch: √((−3)²) = √9 = 3, nicht −3.',
                                        ['Richtig: Wurzel und Quadrat heben sich immer auf.', 'Falsch: √((−3)²) ist nicht definiert.', 'Richtig: √((−3)²) = −3.'],
                                        '(−3)² = 9 und √9 = 3. Die Wurzel ist nie negativ, darum kommt 3 heraus und nicht −3.',
                                        'Rechne von innen nach außen: erst (−3)², dann die Wurzel.')),
        ('wurzel_deuten', 2, O, auswahl('Welche Zahlen lösen die Gleichung x² = 0,25?', '0,5 und −0,5', ['nur 0,5', '0,125 und −0,125', '0,05 und −0,05'],
                                        '0,5² = 0,25 und (−0,5)² = 0,25. Beide Zahlen lösen die Gleichung.', 'Welche Zahl ergibt mal sich selbst 0,25? Denke auch an Minus.')),
        ('wurzel_deuten', 2, O, zahl('Berechne (√5)² + (√11)².', '(√5)² = 5 und (√11)² = 11, also 5 + 11 = 16.',
                                     'Quadrieren hebt die Wurzel auf.', 16, '5 + 11')),
        # wurzel_sache
        ('wurzel_sache', 3, P, zahl('Ein würfelförmiger Wassertank fasst 8 000 Liter. Wie lang ist eine Innenkante in Metern?',
                                    '8 000 Liter = 8 000 dm³ = 8 m³. Kante: ∛8 m = 2 m, denn 2³ = 8. Falle: ∛8 000 = 20 wären Dezimeter.',
                                    'Rechne zuerst in m³ um: 1 m³ = 1 000 Liter.', 2, '8 / (2 * 2)', einheit='m')),
        ('wurzel_sache', 3, P, zahl('Ein quadratisches Grundstück hat 1 600 m² Fläche. Es bekommt ringsum einen Zaun, nur eine 4 m breite Einfahrt bleibt frei. Wie viele Meter Zaun braucht man?',
                                    'Seite: √1 600 m = 40 m. Umfang: 4 · 40 m = 160 m. Ohne Einfahrt: 160 m − 4 m = 156 m.',
                                    'Erst die Seitenlänge, dann den Umfang. Denke an die Einfahrt.', 156, '4 * (1600 / 40) - 4', einheit='m')),
        ('wurzel_sache', 3, K, zahl('Ein Quadrat wird vergrößert, bis seine Fläche 9-mal so groß ist. Wie viel Mal so lang ist dann seine Seite?',
                                    'Fläche = Seite · Seite. Wird die Seite k-mal so lang, wird die Fläche k²-mal so groß. k² = 9, also k = 3. Beispiel: 1 cm → 3 cm, 1 cm² → 9 cm².',
                                    'Probiere mit einem Quadrat der Seite 1 cm. Welche Seite hat ein Quadrat mit 9 cm²?', 3, '9 / 3')),
        ('wurzel_sache', 3, O, zahl('Ein Würfel hat eine Oberfläche von 150 cm². Wie groß ist sein Volumen?',
                                    'Eine Seitenfläche: 150 : 6 = 25 cm². Kante: √25 cm = 5 cm. Volumen: 5³ cm³ = 125 cm³.',
                                    'Oberfläche → eine Seitenfläche → Kante → Volumen.', 125, '(150 / 6 / 5) ** 3', einheit='cm³')),
        ('wurzel_sache', 2, O, zahl('Ein quadratischer Bilderrahmen hat innen 0,49 m² Fläche. Wie lang ist eine Innenseite in Zentimetern?',
                                    '√0,49 = 0,7, also 0,7 m = 70 cm.', 'Erst die Seite in m, dann in cm umrechnen.', 70, '(0.49 / 0.7) * 100', einheit='cm')),
        ('wurzel_sache', 2, O, zahl('Ein Würfel hat ein Volumen von 1 331 cm³. Wie lang ist eine Kante?', '11³ = 11 · 11 · 11 = 1 331, also ist die Kante 11 cm lang.',
                                    'Probiere Zahlen hoch 3. Die Endziffer 1 hilft.', 11, '1331 / 121', einheit='cm')),
    ]


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('zahlen.wurzeln_basis', 13_9_1)
# c) Ergebnis ist eine ganze Zahl, „gekürzter Bruch“ mit Nenner 1 verwirrt → Zahl-Aufgabe
BF.ersetze('wurzel_dezimal', 'Berechne 4 · √(25/4). Gib das Ergebnis als gekürzten Bruch an.', BF.Z(
    'Berechne 4 · √(25/4).', 10, '4 * 5 / 2', '√(25/4) = √25 : √4 = 5/2. 4 · 5/2 = 20/2 = 10.',
    'Ziehe die Wurzel aus Zähler und Nenner einzeln.'))
# a) Grundaufgaben
BF.stufe('wurzel_dezimal', 'Was ergibt √0,49?', 1)
BF.stufe('kubikwurzel', 'Berechne ∛8 · √4.', 2)
BF.stufe('kubikwurzel', 'Berechne ∛27 · √9.', 2)
# a) gleicher Typ wie Stufe 1, nur größere Zahlen
for _z in ('√1 605', '√788', '√1 291'):
    BF.stufe('abschaetzen', f'Zwischen welchen aufeinanderfolgenden natürlichen Zahlen liegt {_z}?', 2)

# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    d = bauen('zahlen.wurzeln_basis',
          'Quadratwurzeln und dritte Wurzeln als Umkehrung des Quadrierens bzw. Hoch-3-Nehmens bestimmen, abschätzen und anwenden.',
          ['√a ist die nicht-negative Zahl, deren Quadrat a ist (a ≥ 0).', '∛a ist die Zahl, deren dritte Potenz a ist.',
           'x² = a (a > 0) hat zwei Lösungen: √a und −√a.', 'Keine Quadratzahl? Zwischen die benachbarten Quadratzahlen einordnen.'],
          [('Quadratwurzeln', ['quadratwurzel', 'wurzel_dezimal']), ('Dritte Wurzeln und Abschätzen', ['kubikwurzel', 'abschaetzen']),
           ('Verstehen und Anwenden', ['wurzel_deuten', 'wurzel_sache'])],
          ETAPPEN, GEN,
          meiden={'quadratwurzel': ['√196.'], 'wurzel_dezimal': ['√0,64.', '√(4/81)'], 'kubikwurzel': ['∛343.'],
                  'abschaetzen': ['√90?'], 'wurzel_deuten': ['x² = 25?'], 'wurzel_sache': [' 169 m²']},
          offen=['Kubikwurzel aus negativen Zahlen (Prüfvorschlag ∛(−8) = −2) nicht umgesetzt: Die Lernkarte definiert ∛a wie der LehrplanPLUS nur für a ≥ 0; eine Aufgabe mit −2 als richtiger Antwort widerspräche der Erklärung.',
                 'Rechenausdruck c bei Wurzeln: Das Prüfskript kann keine Wurzeln rechnen. c prüft deshalb die Umkehrung (z. B. 196 / 14 = 14 bzw. 343 / (7 · 7) = 7).'])
    anhaengen(d, 9901, schwer)
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden


# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl9) ----
# Stufen im Gedanken statt in der Zahlengröße: S1 = Beispiel mit anderen Zahlen, S2 = Umkehrung/mehrere Schritte, S3 = anderer Gedanke.
from _durchsicht_kl9 import Befunde as _DSB, durchsicht  # noqa: E402

DS = _DSB('zahlen.wurzeln_basis', 19_9_1)
# quadratwurzel: reine Rechenketten sind kein anderer Gedanke → Stufe 2
for _t in ('Berechne 2 · √25 − √169.', 'Berechne 3 · √9 − √100.', 'Berechne 4 · √169 − √16.', 'Berechne √(62 + 19).'):
    DS.stufe('quadratwurzel', _t, 2)
# wurzel_dezimal: Bruchwurzel wie auf Stufe 2
DS.stufe('wurzel_dezimal', 'Berechne √(9/169).', 2)
# kubikwurzel: Bruch- und Produktaufgaben wie auf Stufe 2; dafür eine neue Knobelaufgabe
for _t in ('Berechne ∛(1/343).', 'Berechne ∛(27/343).', 'Berechne ∛(216/343).', 'Berechne ∛64 · √25.'):
    DS.stufe('kubikwurzel', _t, 2)
DS.neu('kubikwurzel', 3, DS.Z('Ein voller Würfel besteht aus 64 Würfelchen. Er soll zu einem vollen Würfel ergänzt werden, dessen Kante 1 Würfelchen länger ist. '
                              'Wie viele Würfelchen kommen dazu?', 61, '5 ** 3 - 4 ** 3',
                              'Kante jetzt ∛64 = 4, später 5. Der neue Würfel hat 5³ = 125 Würfelchen. Dazu kommen 125 − 64 = 61.',
                              'Bestimme zuerst die Kantenlänge des alten Würfels.'))
# abschaetzen: „natürliche Zahlen, nur größer“ ist derselbe Gedanke wie Stufe 1 → Stufe 1; Zehntel-Aufgabe auf Stufe 2
for _z in ('√285', '√323', '√103', '√404', '√788', '√200', '√1 605', '√1 291'):
    DS.stufe('abschaetzen', f'Zwischen welchen aufeinanderfolgenden natürlichen Zahlen liegt {_z}?', 1)
DS.stufe('abschaetzen', 'Zwischen welchen aufeinanderfolgenden natürlichen Zahlen liegt √648?', 1)
DS.stufe('abschaetzen', 'Zwischen welchen Zehnteln liegt √82?', 2)
# wurzel_deuten: Wiederholungen der Stufe-1-Muster → Stufe 1; Fehlerfinden einmal auf Stufe 2; zwei Wiederholungen auf Stufe 3 ersetzt
for _t in ('Was gilt für √(−169)?', 'Was gilt für √(−121)?', 'Was gilt für √(−289)?', 'Welchen Wert hat (√88)²?', 'Welchen Wert hat (√79)²?'):
    DS.stufe('wurzel_deuten', _t, 1)
DS.stufe('wurzel_deuten', 'Jemand rechnet: √(36 + 49) = √36 + √49 = 13. Was stimmt?', 2)
DS.ersetze('wurzel_deuten', 'Jemand rechnet: √(36 + 9) = √36 + √9 = 9. Was stimmt?',
           DS.A('Für welche Zahlen x ist √(x − 4) erklärt?', 'für x ≥ 4', ['für x > 4', 'für x ≥ 0', 'für alle x'],
                'Unter der Wurzel darf nichts Negatives stehen: x − 4 ≥ 0, also x ≥ 4. Auch x = 4 geht: √0 = 0.',
                'Wann ist x − 4 nicht negativ?'))
DS.ersetze('wurzel_deuten', 'Jemand rechnet: √(81 + 16) = √81 + √16 = 13. Was stimmt?',
           DS.Z('Berechne (−√7)².', 7, '7', '(−√7)² = (−√7) · (−√7) = √7 · √7 = 7. Minus mal Minus ergibt Plus.',
                'Schreibe das Quadrat als Produkt. Was ergibt Minus mal Minus?'))
# wurzel_sache: Oberfläche → Kante ist zweischrittig (Stufe 2); nur zwei solcher Aufgaben bleiben auf Stufe 3; Beinahe-Dublette (512 cm³ zweimal) ersetzt
for _t in ('Ein Würfel hat eine Oberfläche von 384 cm². Wie lang ist eine Kante?', 'Ein Würfel hat eine Oberfläche von 486 cm². Wie lang ist eine Kante?',
           'Ein Würfel hat eine Oberfläche von 1 350 cm². Wie lang ist eine Kante?'):
    DS.stufe('wurzel_sache', _t, 2)
DS.ersetze('wurzel_sache', 'Ein Spielwürfel aus Kunststoff hat ein Volumen von 512 cm³. Wie lang ist eine Kante?',
           DS.Z('Ein Würfel hat ein Volumen von 0,027 m³. Wie lang ist eine Kante in Zentimetern?', 30, '3 * 10',
                '∛0,027 = 0,3, denn 0,3 · 0,3 · 0,3 = 0,027. Die Kante ist 0,3 m = 30 cm lang.', 'Ziehe die dritte Wurzel und rechne m in cm um.', einheit='cm'),
           pools=('uebung',))
DS_KARTEN = {
    'wurzel_deuten': {
        'fehler': '√25 ist nicht −5 und nicht ±5. Die Wurzel ist nie negativ. Nur die Gleichung x² = 25 hat zwei Lösungen.',
        'fehler_bild': {'punkte': [{'x': -5, 'y': 25, 'name': '−5 ≠ √25'}, {'x': 5, 'y': 25, 'name': '√25 = 5'}]},
    },
}

if __name__ == '__main__':
    durchsicht('zahlen.wurzeln_basis', DS, DS_KARTEN)
