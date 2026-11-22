#!/usr/bin/env python3
"""Thema zahlen.reell – Wurzeln und reelle Zahlen (Klasse 9). Schreibt inhalte/themen/zahlen.reell.json."""
import sys
from math import isqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(902)
QF = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15]          # quadratfreie Radikanden
NQ = [x for x in range(2, 120) if isqrt(x) ** 2 != x]  # keine Quadratzahlen


def wt(k, m):
    """k√m als Text"""
    if k == 1: return f'√{m}'
    if k == -1: return f'−√{m}'
    return f'{dz(k)}√{m}'


ETAPPEN = [
    {'lernziel': 'zahlarten', 'titel': 'Rational oder irrational?',
     'regel': '⟦Rationale Zahlen⟧ lassen sich als Bruch schreiben (endliche oder periodische Dezimalzahl). ⟦Irrationale Zahlen⟧ wie √2 haben unendlich viele Nachkommastellen ohne Periode. Beide zusammen bilden die ⟦reellen Zahlen ℝ⟧.',
     'schritte': ['√49 = 7 ist eine natürliche Zahl, also rational.', '√50 liegt zwischen 7 und 8, 50 ist keine Quadratzahl: √50 ist ⟦irrational⟧.'],
     'probe': 'Faustregel: √n (n natürlich) ist nur rational, wenn n eine Quadratzahl ist.',
     'fehler': '„0,333… ist irrational, weil es unendlich viele Stellen hat“ ist falsch: Die Ziffern wiederholen sich (Periode). 0,333… = ⟦1/3⟧ ist rational.'},
    {'lernziel': 'eingrenzen', 'titel': 'Wurzeln genauer eingrenzen',
     'regel': 'Mit der ⟦Intervallschachtelung⟧ grenzt du √a immer enger ein: Du quadrierst Zahlen mit einer, dann zwei Nachkommastellen und vergleichst mit a.',
     'schritte': ['√30: 5² = 25 < 30 < 36 = 6², also 5 < √30 < 6.', '5,4² = 29,16 < 30 < 30,25 = 5,5², also ⟦5,4 < √30 < 5,5⟧.'],
     'probe': '5,48² ≈ 30,03 – passt in das Intervall.',
     'fehler': '„√30 liegt zwischen 5,0 und 5,1, weil 30 näher an 25 liegt“ ist falsch: 5,1² = 26,01 < 30. Du musst ⟦quadrieren und vergleichen⟧, nicht schätzen.'},
    {'lernziel': 'wurzel_mal', 'titel': 'Wurzeln multiplizieren und dividieren',
     'regel': 'Für a, b ≥ 0 gilt: ⟦√a · √b = √(a · b)⟧ und für b > 0 ⟦√a : √b = √(a : b)⟧. Für Summen gibt es keine solche Regel.',
     'schritte': ['√3 · √27 = √(3 · 27) = √81.', '√81 = ⟦9⟧.'],
     'probe': 'Quadriere das Ergebnis: 9² = 81, und 3 · 27 = 81 ✓',
     'fehler': '√16 + √9 = √25 ist falsch: Bei der ⟦Summe⟧ darf man nicht zusammenfassen. 4 + 3 = 7, aber √25 = 5.'},
    {'lernziel': 'teilweise', 'titel': 'Teilweise die Wurzel ziehen',
     'regel': 'Zerlege den Radikanden in eine ⟦Quadratzahl mal Rest⟧: √(k² · m) = ⟦k√m⟧. Nimm die größte Quadratzahl, die passt.',
     'schritte': ['√72 = √(36 · 2), denn 36 ist die größte Quadratzahl, die in 72 steckt.', '√36 · √2 = ⟦6√2⟧.'],
     'probe': '(6√2)² = 36 · 2 = 72 ✓',
     'fehler': '√72 = √(4 · 18) = 2√18 ist nicht fertig: In 18 steckt noch die Quadratzahl 9. Mit der ⟦größten⟧ Quadratzahl 36 erhält man 6√2.'},
    {'lernziel': 'zusammenfassen', 'titel': 'Wurzelterme zusammenfassen',
     'regel': 'Behandle √m wie eine Variable: 3x + 5x = 8x, also auch ⟦3√2 + 5√2 = 8√2⟧. Aber 2x + 4y lässt sich nicht zusammenfassen – genauso wenig ⟦2√3 + 4√5⟧. Nur Wurzeln mit ⟦gleichem Radikanden⟧ kann man addieren. Vorher teilweise die Wurzel ziehen, dann zusammenfassen.',
     'schritte': ['√18 + √50 = 3√2 + 5√2 (teilweise radiziert).', '3√2 + 5√2 = ⟦8√2⟧.'],
     'probe': '√18 ≈ 4,24, √50 ≈ 7,07, Summe ≈ 11,31; 8√2 ≈ 11,31 ✓',
     'fehler': '2√3 + 4√5 = 6√8 ist falsch: Die Radikanden sind ⟦verschieden⟧, der Term lässt sich nicht zusammenfassen.'},
    {'lernziel': 'nenner_rational', 'titel': 'Nenner rational machen',
     'regel': 'Steht eine Wurzel im Nenner, ⟦erweitere⟧ mit dieser Wurzel: a/√m = a√m / m. Bei √m − n erweiterst du mit √m + n (⟦3. binomische Formel⟧).',
     'schritte': ['12/√3: mit √3 erweitern ergibt 12√3 / (√3 · √3) = 12√3 / 3.', '12√3 / 3 = ⟦4√3⟧.'],
     'probe': '4√3 · √3 = 4 · 3 = 12 ✓',
     'fehler': '12/√3 = 4 ist falsch: Man darf nicht einfach durch 3 teilen. √3 · √3 = 3, deshalb steht nach dem Erweitern ⟦√3 im Zähler⟧: 4√3.'},
]

# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'zahlarten': {
  'einstieg': 'Ein quadratisches Beet soll genau 2 m² groß werden. Seine Seite ist dann √2 m. Der Taschenrechner zeigt 1,41421356… – und egal wie viele Stellen man ausrechnet, es kommen immer neue Ziffern ohne Muster. So eine Zahl kann man nicht als Bruch schreiben; sie heißt ⟦irrational⟧.',
  'woerter': [['Bruch', 'eine ganze Zahl geteilt durch eine ganze Zahl, z. B. 3/4'],
              ['rational', 'als Bruch schreibbar: 7 = 7/1, 0,5 = 1/2, 0,333… = 1/3'],
              ['…', 'die Ziffern gehen immer weiter'],
              ['periodisch', 'die Ziffern wiederholen sich immer gleich, z. B. 0,333…; der wiederholte Teil heißt Periode'],
              ['irrational', 'nicht als Bruch schreibbar: unendlich viele Nachkommastellen ohne Wiederholung, z. B. √2, π'],
              ['reelle Zahlen ℝ', 'alle rationalen und irrationalen Zahlen zusammen'],
              ['natürliche Zahl', 'eine der Zahlen 1, 2, 3, …']],
  'schritte': ['Prüfe √49: 7 · 7 = 49, also ist √49 = 7. Das ist eine ganze Zahl und damit ⟦rational⟧, denn 7 = 7/1.',
               'Prüfe √50: 50 ist keine Quadratzahl, denn 7 · 7 = 49 und 8 · 8 = 64.',
               'Die Wurzel aus einer natürlichen Zahl, die keine Quadratzahl ist, geht nie glatt auf – auch nicht als Bruch.',
               'Also ist √50 ⟦irrational⟧: unendlich viele Nachkommastellen ohne Wiederholung.'],
  'regel': 'So entscheidest du: Lässt sich die Zahl als ⟦Bruch⟧ schreiben (die Dezimalzahl endet oder wiederholt sich), ist sie ⟦rational⟧. Geht das nicht (unendlich viele Stellen ohne Wiederholung, z. B. √2 oder π), ist sie ⟦irrational⟧. Beide zusammen bilden die ⟦reellen Zahlen ℝ⟧.',
  'fehler': '„0,333… ist irrational, weil es unendlich viele Stellen hat“ ist falsch: Die 3 wiederholt sich immer (Periode). 0,333… = ⟦1/3⟧ – ein Drittel, wie bei einer Pizza für drei. Das ist rational.'},
 'eingrenzen': {
  'einstieg': 'Ein anderes quadratisches Beet hat 30 m². Für den Zaun willst du die Seite genauer wissen als nur „zwischen 5 und 6 Meter“. Also probierst du Kommazahlen: Ist 5,4 m noch zu kurz oder schon zu lang? Mit jedem Schritt wird der Bereich enger. Das heißt ⟦Intervallschachtelung⟧.',
  'woerter': [['quadrieren', 'eine Zahl mit sich selbst malnehmen: 5,4² = 5,4 · 5,4'],
              ['Intervall', 'der Bereich zwischen zwei Zahlen, z. B. von 5,4 bis 5,5'],
              ['Intervallschachtelung', 'den Bereich Schritt für Schritt enger machen'],
              ['≈', '„ungefähr gleich“']],
  'schritte': ['Gesucht ist √30, die Seite des Beets. Zuerst ganze Zahlen: 5 · 5 = 25 ist zu klein, 6 · 6 = 36 ist zu groß. Also liegt √30 zwischen 5 und 6.',
               'Jetzt Zehntel probieren: 5,4 · 5,4 = 29,16. Das ist noch kleiner als 30.',
               'Die nächste Zahl: 5,5 · 5,5 = 30,25. Das ist schon größer als 30.',
               'Also gilt ⟦5,4 < √30 < 5,5⟧: Die Seite ist etwas länger als 5,4 m.'],
  'regel': 'So grenzt du √a genauer ein: Zahlen mit einer, dann mit zwei Nachkommastellen ⟦quadrieren⟧ und mit a vergleichen. Die größte Zahl, deren Quadrat noch unter a liegt, ist die ⟦untere Grenze⟧; die nächste ist die ⟦obere Grenze⟧.',
  'fehler': '„√30 liegt zwischen 5,0 und 5,1, weil 30 näher an 25 liegt“ ist falsch: 5,1 · 5,1 = 26,01 ist noch viel kleiner als 30. Ein Zaun nach dieser Schätzung wäre zu kurz. Du musst ⟦quadrieren und vergleichen⟧, nicht nach Gefühl schätzen.'},
 'wurzel_mal': {
  'einstieg': 'Zwei krumme Zahlen können zusammen eine glatte ergeben. Ein Beet ist √3 m breit und √27 m lang – beide Längen haben unendlich viele Nachkommastellen. Trotzdem ist seine Fläche genau 9 m². Der Trick: Beim Malnehmen darf man zwei Wurzeln ⟦unter eine Wurzel⟧ ziehen.',
  'woerter': [['Produkt', 'das Ergebnis beim Malnehmen'],
              ['Quotient', 'das Ergebnis beim Teilen'],
              ['Summe', 'das Ergebnis beim Zusammenzählen'],
              ['√a · √b = √(a · b)', 'zwei Wurzeln malnehmen = eine Wurzel aus dem Produkt'],
              ['a, b ≥ 0', 'a und b sind nicht negativ']],
  'schritte': ['Gesucht ist √3 · √27, die Fläche des Beets in m².',
               'Beide Wurzeln unter eine Wurzel ziehen: √3 · √27 = √(3 · 27).',
               'Unter der Wurzel rechnen: 3 · 27 = 81.',
               '√81 = ⟦9⟧, denn 9 · 9 = 81. Das Beet hat also 9 m².'],
  'regel': 'So rechnest du: Beim ⟦Malnehmen⟧ und ⟦Teilen⟧ darfst du zwei Wurzeln zu einer zusammenziehen: ⟦√a · √b = √(a · b)⟧ und ⟦√a : √b = √(a : b)⟧ (für a, b ≥ 0, beim Teilen b > 0). Beim ⟦Zusammenzählen⟧ gilt das nicht.',
  'fehler': '√16 + √9 = √25 ist falsch: Bei einer ⟦Summe⟧ darf man nicht zusammenziehen. √16 + √9 = 4 + 3 = 7, aber √25 = 5. Zwei Bretter mit 4 m und 3 m sind zusammen 7 m lang, nicht 5 m.'},
 'teilweise': {
  'einstieg': 'Manche Wurzeln lassen sich ein Stück weit kürzer schreiben – ähnlich wie man einen Bruch kürzt. In 72 steckt zum Beispiel die Quadratzahl 36, denn 72 = 36 · 2. Aus der 36 lässt sich die Wurzel glatt ziehen, nur die 2 bleibt unter der Wurzel. Das nennt man ⟦teilweise die Wurzel ziehen⟧.',
  'woerter': [['radizieren', 'die Wurzel ziehen'],
              ['Radikand', 'die Zahl unter dem Wurzelzeichen'],
              ['6√2', 'kurz für 6 · √2; der Malpunkt wird weggelassen'],
              ['k² · m', 'eine Quadratzahl mal einen Rest']],
  'schritte': ['Gesucht ist eine kürzere Schreibweise für √72.',
               'Suche die größte Quadratzahl, die in 72 steckt: 36, denn 72 = 36 · 2.',
               'Schreibe die Wurzel als Produkt: √72 = √(36 · 2) = √36 · √2.',
               'Ziehe die glatte Wurzel: √36 = 6. Also ist √72 = ⟦6√2⟧.'],
  'regel': 'So ziehst du teilweise die Wurzel: Zerlege den ⟦Radikanden⟧ in ⟦größte Quadratzahl mal Rest⟧. Aus der Quadratzahl ziehst du die Wurzel, der Rest bleibt darunter: √(k² · m) = ⟦k√m⟧.',
  'fehler': '√72 = √(4 · 18) = 2√18 ist nicht fertig: In 18 steckt noch die Quadratzahl 9 – wie ein Bruch, den man nur halb gekürzt hat. Mit der ⟦größten⟧ Quadratzahl 36 erhält man 6√2.'},
 'zusammenfassen': {
  'einstieg': 'Äpfel und Birnen: 3 Äpfel plus 5 Äpfel sind 8 Äpfel. Aber 2 Äpfel plus 4 Birnen kann man nicht zu einer einzigen Sorte machen. Mit Wurzeln ist es genauso: Gleiche Wurzeln lassen sich zusammenzählen, verschiedene nicht. Das heißt ⟦zusammenfassen⟧.',
  'woerter': [['3√2', '3 · √2, also dreimal die Zahl √2'],
              ['gleicher Radikand', 'dieselbe Zahl unter der Wurzel'],
              ['Variable', 'ein Buchstabe wie x, der für eine Zahl steht'],
              ['zusammenfassen', 'gleichartige Teile zusammenzählen']],
  'schritte': ['Gesucht ist √18 + √50. So, wie es dasteht, sind die Zahlen unter den Wurzeln verschieden.',
               'Erst teilweise die Wurzel ziehen: √18 = √(9 · 2) = 3√2.',
               'Genauso: √50 = √(25 · 2) = 5√2.',
               'Jetzt sind es gleiche Wurzeln, wie 3 Äpfel und 5 Äpfel: 3√2 + 5√2 = ⟦8√2⟧.'],
  'regel': 'So fasst du zusammen: Erst teilweise die Wurzel ziehen. Dann nur Wurzeln mit ⟦gleichem Radikanden⟧ zusammenzählen, wie bei 3x + 5x = 8x: ⟦3√2 + 5√2 = 8√2⟧. Verschiedene Radikanden wie bei ⟦2√3 + 4√5⟧ bleiben stehen.',
  'fehler': '2√3 + 4√5 = 6√8 ist falsch: Die Radikanden sind ⟦verschieden⟧ – wie 2 Äpfel und 4 Birnen, aus denen keine „6 Apfelbirnen“ werden. Der Term bleibt so stehen.'},
 'nenner_rational': {
  'einstieg': 'Durch eine krumme Zahl zu teilen ist unbequem: 12 geteilt durch 1,732… rechnet niemand gern im Kopf. Deshalb schreibt man solche Brüche so um, dass unten keine Wurzel mehr steht. Der Wert bleibt dabei gleich – wie beim Erweitern von 1/2 zu 2/4. Das heißt ⟦Nenner rational machen⟧.',
  'woerter': [['Zähler / Nenner', 'die Zahl über / unter dem Bruchstrich'],
              ['erweitern', 'Zähler und Nenner mit derselben Zahl malnehmen; der Wert bleibt gleich'],
              ['√3 · √3 = 3', 'eine Wurzel mal sich selbst ergibt die Zahl darunter'],
              ['3. binomische Formel', '(a + b) · (a − b) = a² − b²']],
  'schritte': ['Gesucht ist 12/√3 ohne Wurzel im Nenner.',
               'Erweitere mit √3, also oben und unten mal √3: 12√3 / (√3 · √3).',
               'Unten wird die Wurzel glatt: √3 · √3 = 3. Jetzt steht da 12√3 / 3.',
               '12 : 3 = 4, also ist ⟦12/√3 = 4√3⟧.'],
  'regel': 'So machst du den ⟦Nenner rational⟧: ⟦Erweitere⟧ mit der Wurzel aus dem Nenner: a/√m = a√m / m. Steht unten √m − n, erweiterst du mit √m + n (⟦3. binomische Formel⟧).',
  'fehler': '12/√3 = 4 ist falsch: Man darf √3 nicht wie 3 behandeln. Probe: 12 : 1,732 ≈ 6,93, nicht 4. Nach dem Erweitern steht ⟦√3 im Zähler⟧: 4√3 ≈ 6,93.'},
}
klar(ETAPPEN, KLAR)
# ---- KLAR ENDE ----
# ---- UMBAU (neues Muster, Runde 8, Vorgabe 16.11.) ----
UMBAU = {
 'zahlarten': {
  'einstieg': 'Ein quadratisches Beet hat 50 m². Seine Seite √50 m hat unendlich viele Nachkommastellen ohne Muster. So eine Zahl heißt ⟦irrational⟧.',
  'woerter': [['rational', 'als Bruch schreibbar, z. B. 7 = 7/1 oder 0,5 = 1/2'],
              ['irrational', 'nicht als Bruch schreibbar: unendlich viele Stellen ohne Wiederholung']],
  'bild': {'typ': 'zahlenstrahl', 'start': 6, 'ende': 8, 'abschnitte': 4, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': 'Ein Beet mit 49 m² hat die Seite √49 = 7 m.',
                'bild': {'punkte': [{'wert': 7, 'name': '√49'}]}},
               {'text': '7 = 7/1 ist ein Bruch. Also ist √49 ⟦rational⟧.'},
               {'text': '50 ist keine Quadratzahl, denn 7² = 49 und 8² = 64.',
                'bild': {'punkte': [{'wert': 7, 'name': '√49'}, {'wert': 7.07, 'name': '√50'}]}},
               {'text': 'Darum geht √50 nie glatt auf, auch nicht als Bruch: ⟦irrational⟧.'}],
  'fehler': '0,333… ist nicht irrational. Die 3 wiederholt sich immer: 0,333… = 1/3, ein Drittel. Das ist rational.',
  'fehler_bild': {'typ': 'bruchstreifen', 'teile': 3, 'gefaerbt': 1, 'teil_text': '1/3 = 0,333…'},
  'regel': 'Geht die Zahl als ⟦Bruch⟧, ist sie rational, sonst irrational. Beide zusammen bilden die reellen Zahlen ℝ.'},
 'eingrenzen': {
  'einstieg': 'Ein Beet hat 30 m². Seine Seite liegt zwischen 5 m und 6 m. Für den Zaun willst du es genauer: Du machst eine ⟦Intervallschachtelung⟧.',
  'woerter': [['Intervall', 'der Bereich zwischen zwei Zahlen, z. B. von 5,4 bis 5,5'],
              ['Intervallschachtelung', 'den Bereich Schritt für Schritt enger machen'],
              ['quadrieren', 'eine Zahl mit sich selbst malnehmen']],
  'bild': {'typ': 'zahlenstrahl', 'start': 5, 'ende': 6, 'abschnitte': 10, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': '√30 liegt zwischen 5 und 6, denn 5² = 25 und 6² = 36.',
                'bild': {'bereich': {'von': 5, 'bis': 6}}},
               {'text': 'Zehntel quadrieren: 5,4² = 29,16 ist noch kleiner als 30.',
                'bild': {'punkte': [{'wert': 5.4, 'name': '5,4'}]}},
               {'text': '5,5² = 30,25 ist schon größer als 30.',
                'bild': {'punkte': [{'wert': 5.4, 'name': '5,4'}, {'wert': 5.5, 'name': '5,5'}]}},
               {'text': 'Das Intervall wird enger: ⟦5,4 < √30 < 5,5⟧.',
                'bild': {'bereich': {'von': 5.4, 'bis': 5.5}, 'punkte': [{'wert': 5.477, 'name': '√30'}]}}],
  'fehler': '√30 liegt nicht zwischen 5,0 und 5,1. Denn 5,1² = 26,01 ist viel kleiner als 30. Der Zaun wäre zu kurz.',
  'fehler_bild': {'bereich': {'von': 5.0, 'bis': 5.1}, 'punkte': [{'wert': 5.477, 'name': '√30'}]},
  'regel': '⟦Quadriere⟧ Kommazahlen und vergleiche mit a. Die Grenzen sind die Zahlen direkt unter und über √a.'},
 'wurzel_mal': {
  'einstieg': 'Ein Beet ist √3 m breit und √27 m lang. Beide Längen sind krumm, die Fläche ist aber genau 9 m². Beim Malnehmen darfst du Wurzeln ⟦zusammenziehen⟧.',
  'woerter': [['zusammenziehen', 'zwei Wurzeln als eine Wurzel schreiben'],
              ['√a · √b = √(a · b)', 'zwei Wurzeln malnehmen ist eine Wurzel aus dem Produkt'],
              ['Produkt', 'das Ergebnis beim Malnehmen']],
  'bild': {'typ': 'figur', 'punkte': {'_A': [0, 0], '_B': [5.196, 0], '_C': [5.196, 1.732], '_D': [0, 1.732]},
           'flaeche': ['_A', '_B', '_C', '_D'],
           'linien': [['_A', '_B', '√27 m'], ['_B', '_C', '√3 m'], ['_C', '_D', 'Fläche = ?'], ['_D', '_A', '']],
           'rechter_winkel': [['_A', '_B', '_D']]},
  'schritte': [{'text': 'Die Fläche ist Breite mal Länge: √3 · √27.'},
               {'text': 'Regel √a · √b = √(a · b): √3 · √27 = √(3 · 27).'},
               {'text': 'Unter der Wurzel steht das Produkt 3 · 27 = 81.'},
               {'text': '√81 = ⟦9⟧. Das Beet hat also 9 m².',
                'bild': {'linien': [['_A', '_B', '√27 m'], ['_B', '_C', '√3 m'], ['_C', '_D', 'Fläche = 9 m²'], ['_D', '_A', '']]}}],
  'fehler': '√16 + √9 ist nicht √25. Bei Plus darfst du nicht zusammenziehen. 4 m und 3 m Zaun sind 7 m, nicht 5 m.',
  'fehler_bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 8, 'abschnitte': 8, 'beschriftet': 'anfang_ende',
                  'boegen': [{'von': 0, 'bis': 4, 'name': '√16'}, {'von': 4, 'bis': 7, 'name': '√9'}],
                  'punkte': [{'wert': 5, 'name': '√25?'}]},
  'regel': 'Beim ⟦Malnehmen⟧ und Teilen darfst du Wurzeln zusammenziehen. √a · √b = √(a · b), √a : √b = √(a : b). Bei Plus nicht.'},
 'teilweise': {
  'einstieg': 'Wie einen Bruch kann man auch √72 kürzer schreiben. In 72 steckt die Quadratzahl 36. Aus ihr ziehst du die Wurzel: ⟦teilweise die Wurzel ziehen⟧.',
  'woerter': [['Radikand', 'die Zahl unter dem Wurzelzeichen'],
              ['6√2', 'kurz für 6 · √2; der Malpunkt wird weggelassen'],
              ['teilweise die Wurzel ziehen', 'nur aus einem Teil des Radikanden die Wurzel ziehen']],
  'bild': {'typ': 'tabelle', 'kopf': ['Quadratzahl', '4', '9', '36', '49'], 'zeilen': [['steckt in 72?', '?', '?', '?', '?']]},
  'schritte': [{'text': 'Suche die größte Quadratzahl, die im Radikanden 72 steckt.'},
               {'text': '72 = 36 · 2. Die 49 passt nicht, also ist 36 die größte.',
                'bild': {'zeilen': [['steckt in 72?', 'ja: 4 · 18', 'ja: 9 · 8', 'ja: 36 · 2', 'nein']]}},
               {'text': 'Also √72 = √36 · √2 = 6 · √2.'},
               {'text': 'Kurz geschrieben: √72 = ⟦6√2⟧.'}],
  'fehler': '2√18 ist noch nicht fertig: In 18 steckt noch die 9. Das ist wie ein halb gekürzter Bruch. Nimm gleich 36.',
  'fehler_bild': {'zeilen': [['steckt in 72?', 'nur halb: 4 · 18', 'ja: 9 · 8', 'am besten: 36 · 2', 'nein']]},
  'regel': 'Zerlege den Radikanden in ⟦größte Quadratzahl mal Rest⟧. Aus der Quadratzahl ziehst du die Wurzel: √(k² · m) = k√m.'},
 'zusammenfassen': {
  'einstieg': '3 Äpfel plus 5 Äpfel sind 8 Äpfel. Äpfel und Birnen zählt man nicht zusammen. Bei Wurzeln ist es genauso: Gleiche Wurzeln kannst du ⟦zusammenfassen⟧.',
  'woerter': [['zusammenfassen', 'gleichartige Teile zusammenzählen'],
              ['3√2', '3 · √2, also dreimal die Zahl √2'],
              ['gleiche Radikanden', 'dieselbe Zahl unter der Wurzel']],
  'bild': {'typ': 'tabelle', 'kopf': ['Term', 'mit √2'], 'zeilen': [['√18', '?'], ['√50', '?'], ['Summe', '?']]},
  'schritte': [{'text': 'Gesucht ist √18 + √50. Die Radikanden 18 und 50 sind verschieden.'},
               {'text': 'Teilweise die Wurzel ziehen: √18 = √(9 · 2) = 3√2.',
                'bild': {'zeilen': [['√18', '3√2'], ['√50', '?'], ['Summe', '?']]}},
               {'text': 'Genauso: √50 = √(25 · 2) = 5√2. Jetzt gibt es gleiche Radikanden.',
                'bild': {'zeilen': [['√18', '3√2'], ['√50', '5√2'], ['Summe', '?']]}},
               {'text': 'Wie 3 Äpfel plus 5 Äpfel: 3√2 + 5√2 = ⟦8√2⟧.',
                'bild': {'zeilen': [['√18', '3√2'], ['√50', '5√2'], ['Summe', '8√2']]}}],
  'fehler': '2√3 + 4√5 ist nicht 6√8. Die Radikanden sind verschieden, wie 2 Äpfel und 4 Birnen. Der Term bleibt stehen.',
  'regel': 'Zähle nur Wurzeln mit ⟦gleichem Radikanden⟧ zusammen. Vorher teilweise die Wurzel ziehen: 3√2 + 5√2 = 8√2.'},
 'nenner_rational': {
  'einstieg': '12 durch 1,732… teilt niemand gern im Kopf. Darum schreibt man 12/√3 so um, dass unten keine Wurzel steht. Das heißt ⟦Nenner rational machen⟧.',
  'woerter': [['Nenner', 'die Zahl unter dem Bruchstrich'],
              ['erweitern', 'Zähler und Nenner mit derselben Zahl malnehmen; der Wert bleibt gleich'],
              ['√3 · √3 = 3', 'eine Wurzel mal sich selbst ergibt die Zahl darunter']],
  'bild': {'typ': 'tabelle', 'kopf': ['', 'Zähler', 'Nenner'], 'zeilen': [['vorher', '12', '√3']]},
  'schritte': [{'text': 'Erweitern mit √3: Zähler und Nenner mal √3.',
                'bild': {'zeilen': [['vorher', '12', '√3'], ['erweitert', '12√3', '√3 · √3']]}},
               {'text': 'Unten gilt √3 · √3 = 3. Jetzt steht da 12√3/3.',
                'bild': {'zeilen': [['vorher', '12', '√3'], ['erweitert', '12√3', '√3 · √3'], ['ausgerechnet', '12√3', '3']]}},
               {'text': '12 : 3 = 4, also ⟦12/√3 = 4√3⟧. Unten steht keine Wurzel mehr.',
                'bild': {'zeilen': [['vorher', '12', '√3'], ['erweitert', '12√3', '√3 · √3'], ['ausgerechnet', '12√3', '3'], ['gekürzt', '4√3', '1']]}}],
  'fehler': '12/√3 ist nicht 4, denn √3 ist nicht 3. Probe: 12 : 1,732 ≈ 6,93, und 4√3 ≈ 6,93 stimmt.',
  'regel': '⟦Erweitere⟧ mit der Wurzel aus dem Nenner: a/√m = a√m/m. Steht unten √m − n, erweiterst du mit √m + n.'},
}
umbau(ETAPPEN, UMBAU)
# ---- UMBAU ENDE ----


def g_zahlarten(s):
    typ = R.choice({1: 'bcf', 2: 'abcdf', 3: 'adef'}[s])
    if typ == 'a':
        r = R.choice(NQ)
        n = R.randint(2, 12)
        p, q = R.randint(1, 9), R.choice([3, 7, 9, 11])
        if Fr(p, q).denominator != q: return None
        falsch = [f'√{n * n}', f'{p}/{q}', f'{dz(Fr(R.randint(1, 99), 100))}', f'−{n}']
        R.shuffle(falsch)
        return auswahl('Welche der Zahlen ist irrational?', f'√{r}', falsch[:3],
                       f'{r} ist keine Quadratzahl, also ist √{r} irrational. Die anderen Zahlen lassen sich als Bruch schreiben (z. B. √{n * n} = {n}).',
                       'Prüfe bei jeder Wurzel, ob der Radikand eine Quadratzahl ist.')
    if typ == 'b':
        if R.random() < 0.5:
            n = R.randint(2, 30)
            return auswahl(f'Ist √{dz(n * n)} rational oder irrational?', f'rational, denn √{dz(n * n)} = {n}',
                           [f'irrational, denn es ist eine Wurzel', f'irrational, denn √{dz(n * n)} ist nicht abbrechend', 'weder noch'],
                           f'{n} · {n} = {dz(n * n)}, also √{dz(n * n)} = {n}. Ganze Zahlen sind rational.', 'Ist der Radikand eine Quadratzahl?')
        r = R.choice(NQ)
        n = isqrt(r)
        return auswahl(f'Ist √{r} rational oder irrational?', f'irrational, denn {r} ist keine Quadratzahl',
                       [f'rational, denn √{r} ≈ {n},5', 'rational, denn jede Wurzel ist ein Bruch', 'weder noch'],
                       f'{n}² = {n * n} < {r} < {(n + 1) ** 2} = {n + 1}². {r} ist keine Quadratzahl, √{r} ist irrational.',
                       'Liegt der Radikand genau auf einer Quadratzahl?')
    if typ == 'c':
        n = R.randint(2, 15)
        r = R.choice(NQ)
        a, b = R.randint(1, 9), R.randint(2, 9)
        if Fr(a, b).denominator != b: return None
        x, richtig, grund = R.choice([
            (f'√{n * n}', 'ℕ (natürliche Zahlen)', f'√{n * n} = {n} ist eine natürliche Zahl.'),
            (f'−√{n * n}', 'ℤ (ganze Zahlen)', f'−√{n * n} = −{n} ist ganz, aber nicht natürlich.'),
            (f'√({a * a}/{b * b})', 'ℚ (rationale Zahlen)', f'√({a * a}/{b * b}) = {a}/{b} ist ein Bruch, aber keine ganze Zahl.'),
            (f'√{r}', 'ℝ (reelle Zahlen)', f'{r} ist keine Quadratzahl, √{r} ist irrational, also nur in ℝ.')])
        return auswahl(f'Zu welcher kleinsten Zahlenmenge gehört {x}?', richtig,
                       ['ℕ (natürliche Zahlen)', 'ℤ (ganze Zahlen)', 'ℚ (rationale Zahlen)', 'ℝ (reelle Zahlen)'],
                       grund, 'Vereinfache die Zahl zuerst so weit wie möglich.')
    if typ == 'd':
        p_, q_ = R.sample(range(0, 9), 2)
        g = R.randint(0, 9)
        per = f'{g},{p_}{q_}{p_}{q_}{p_}{q_}…'
        wert_ = g + Fr(10 * p_ + q_, 99)
        return auswahl(f'Jemand sagt: „{per} (die Ziffern {p_}{q_} wiederholen sich immer) ist irrational.“ Was stimmt?',
                       f'Falsch: Periodische Dezimalzahlen sind rational ({per} = {br(wert_)}).',
                       ['Richtig: Unendlich viele Nachkommastellen bedeuten irrational.', 'Richtig: Die Zahl ist keine ganze Zahl.',
                        'Falsch: Die Zahl ist eine natürliche Zahl.'],
                       f'Eine Periode lässt sich als Bruch schreiben: {per} = {br(wert_)}. Irrational sind nur Zahlen ohne Periode.',
                       'Wiederholen sich die Ziffern oder nicht?')
    if typ == 'f':
        if R.random() < 0.5:
            return auswahl('Welche Zahl ist irrational?', 'π', ['22/7', '3,14', R.choice(['3,141414… (14 wiederholt sich)', '3,1416'])],
                           'π hat unendlich viele Nachkommastellen ohne Periode. 22/7, 3,14 und 3,1416 sind nur Näherungen und als Bruch schreibbar; 3,1414… ist periodisch.',
                           'Welche Zahl lässt sich nicht als Bruch schreiben?')
        z = R.randint(1, 9)
        muster = f'0,{z}0{z}00{z}000{z}0000{z}…'
        per = f'0,{z}0{z}0{z}0{z}0…'
        if R.random() < 0.5:
            return auswahl(f'Ist {muster} (nach jeder {z} steht eine 0 mehr) rational oder irrational?',
                           'irrational, denn es gibt keine Periode',
                           ['rational, denn das Muster ist bekannt', 'rational, denn die Ziffern sind nur 0 und ' + str(z), 'weder noch'],
                           'Die Abstände zwischen den Ziffern ' + str(z) + ' werden immer größer – es wiederholt sich kein fester Ziffernblock. Ohne Periode ist die Zahl irrational.',
                           'Wiederholt sich ein fester Ziffernblock immer wieder?')
        return auswahl(f'Ist {per} (der Block {z}0 wiederholt sich immer) rational oder irrational?',
                       f'rational, denn {per} = {br(Fr(10 * z, 99))}',
                       ['irrational, denn es hat unendlich viele Nachkommastellen', 'irrational, denn es ist kein Bruch', 'weder noch'],
                       f'Der Block {z}0 wiederholt sich (Periode). Periodische Dezimalzahlen sind rational: {per} = {br(Fr(10 * z, 99))}.',
                       'Gibt es einen festen Ziffernblock, der sich wiederholt?')
    r = R.choice(QF)
    return auswahl(f'Welche Aussage ist richtig? (Denke an √{r}.)', f'√{r} · √{r} ist rational, obwohl √{r} irrational ist.',
                   [f'Das Produkt zweier irrationaler Zahlen ist immer irrational.', f'√{r} ist rational, weil man es auf dem Taschenrechner sieht.',
                    f'√{r} + √{r} = √{2 * r}.'],
                   f'√{r} · √{r} = {r}, das ist rational. Taschenrechner zeigen nur gerundete Werte; √{r} + √{r} = 2√{r} ≠ √{2 * r}.',
                   'Rechne jede Aussage an einem Beispiel nach.')


def g_eingrenzen(s):
    r = R.choice([x for x in range(3, 200) if isqrt(x) ** 2 != x])
    if s == 1:
        a = R.randint(11, 99)
        if a % 10 == 0: return None
        x = Fr(a, 10)
        return zahl(f'Berechne {dz(x)}² (für die Intervallschachtelung).', f'{dz(x)} · {dz(x)} = {dz(x * x)} (zwei Nachkommastellen).',
                    'Rechne ohne Komma und setze dann das Komma: 2 Nachkommastellen.', x * x, f'{float(x)} * {float(x)}')
    nd = 1 if s == 2 else 2
    f = 10 ** nd
    u = isqrt(r * f * f)
    lo, hi = Fr(u, f), Fr(u + 1, f)
    if lo * lo == r: return None

    def t(v):
        s_ = dz(v)
        if ',' not in s_: s_ += ',' + '0' * nd
        while len(s_.split(',')[1]) < nd: s_ += '0'
        return s_
    d = Fr(1, f)
    richtig = f'zwischen {t(lo)} und {t(hi)}'
    falsch = [f'zwischen {t(lo - d)} und {t(lo)}', f'zwischen {t(hi)} und {t(hi + d)}', f'zwischen {t(Fr(r, 2))} und {t(Fr(r, 2) + d)}']
    return auswahl(f'Zwischen welchen Zahlen mit {nd} Nachkommastelle{"n" if nd > 1 else ""} liegt √{r}?', richtig, falsch,
                   f'{t(lo)}² = {dz(lo * lo)} < {r} < {dz(hi * hi)} = {t(hi)}², also {t(lo)} < √{r} < {t(hi)}.',
                   'Quadriere die Kandidaten und vergleiche mit dem Radikanden.')


def g_wurzel_mal(s):
    if s == 1:
        m = R.choice(QF)
        k = R.randint(2, 6)
        a, b = m, m * k * k
        if R.random() < 0.5: a, b = b, a
        n = k * m
        return zahl(f'Berechne √{a} · √{b}.', f'√{a} · √{b} = √({a} · {b}) = √{dz(a * b)} = {n}.',
                    'Fasse zu einer Wurzel zusammen und ziehe dann die Wurzel.', n, f'({a} * {b}) / {n}')
    if s == 2 and R.random() < 0.3:
        a, b = R.choice([(9, 16), (16, 9), (36, 64), (9, 40), (25, 144), (4, 9), (16, 49), (36, 4)])
        if R.random() < 0.5:
            return auswahl(f'Ist √{a} · √{b} = √({a} · {b})?', f'Ja: {isqrt(a)} · {isqrt(b)} = {isqrt(a) * isqrt(b) if isqrt(b) ** 2 == b else "√" + str(a * b)} und √{dz(a * b)} ergibt dasselbe.' if isqrt(b) ** 2 == b else f'Ja, das Produktgesetz gilt für alle a, b ≥ 0.',
                           [f'Nein, man darf Wurzeln nie zusammenfassen.', f'Nein, richtig wäre √{a} · √{b} = √({a} + {b}).', 'Nur wenn beide Zahlen Quadratzahlen sind.'],
                           f'Für a, b ≥ 0 gilt √a · √b = √(a · b). Probe durch Quadrieren: (√{a} · √{b})² = {a} · {b} = {dz(a * b)}.',
                           'Quadriere beide Seiten und vergleiche.')
        if isqrt(b) ** 2 != b or isqrt(a + b) ** 2 == a + b: return None
        return auswahl(f'Ist √{a} + √{b} = √({a} + {b})?', f'Nein: √{a} + √{b} = {isqrt(a) + isqrt(b)}, aber √{a + b} ≈ {dz(round((a + b) ** 0.5, 1))}.',
                       ['Ja, wie beim Multiplizieren darf man zusammenfassen.', f'Ja, denn {isqrt(a)} + {isqrt(b)} = {isqrt(a) + isqrt(b)}.', 'Nur wenn beide Zahlen gerade sind.'],
                       f'√{a} + √{b} = {isqrt(a)} + {isqrt(b)} = {isqrt(a) + isqrt(b)}. Unter einer Wurzel: √{a + b} ≈ {dz(round((a + b) ** 0.5, 1))}. Für Summen gibt es keine Wurzelregel.',
                       'Rechne beide Seiten getrennt aus.')
    if s == 2:
        m = R.choice(QF)
        k = R.randint(2, 9)
        a = m * k * k
        return zahl(f'Berechne √{a} : √{m}.', f'√{a} : √{m} = √({a} : {m}) = √{k * k} = {k}.',
                    'Fasse zu einer Wurzel des Quotienten zusammen.', k, f'({a} / {m}) / {k}')
    typ = R.random()
    if typ < 0.5:
        m = R.choice(QF)
        p, q = R.randint(2, 6), R.randint(2, 6)
        if p == q: return None
        a, b = m * p * p, m * q * q
        n = p * q * m
        d = R.randint(2, 20)
        if d == n: return None
        if R.random() < 0.5:
            return zahl(f'Berechne √{a} · √{b} − √{dz(d * d)}.', f'√{a} · √{b} = √{dz(a * b)} = {n}; √{dz(d * d)} = {d}; {n} − {d} = {n - d}.',
                        'Berechne das Produkt der Wurzeln zuerst, dann die zweite Wurzel.', n - d, f'({a} * {b}) / {n} - {d * d} / {d}')
        k = R.randint(4, 12)
        A_ = m * k * k
        return zahl(f'Berechne √{dz(A_)} : √{m}.', f'√{dz(A_)} : √{m} = √({dz(A_)} : {m}) = √{k * k} = {k}.',
                    'Fasse zu einer Wurzel des Quotienten zusammen.', k, f'({A_} / {m}) / {k}')
    m = R.choice(QF)
    k = R.randint(2, 7)
    richtig = f'{k * m}x'
    return auswahl(f'Vereinfache √({m}x) · √({m * k * k}x) für x ≥ 0.', richtig,
                   [f'{k * m}x²', f'{m * m * k * k}x', f'{k}x'],
                   f'√({m}x · {m * k * k}x) = √({dz(m * m * k * k)}x²) = {k * m}x, denn ({k * m}x)² = {dz((k * m) ** 2)}x².',
                   'Multipliziere die Radikanden und ziehe dann die Wurzel aus Zahl und x² getrennt.')


def g_teilweise(s):
    m = R.choice(QF)
    k = R.randint(2, 5) if s == 1 else R.randint(3, 10)
    r = k * k * m
    if s == 3 and R.random() < 0.5:
        if R.random() < 0.5:
            return luecken(f'Schreibe {k}√{m} als eine einzige Wurzel.', '√□', 'Radikand', [r],
                           f'{k}√{m} = √{k * k} · √{m} = √({k * k} · {m}) = √{r}.',
                           'Schreibe den Faktor vor der Wurzel als Wurzel aus seinem Quadrat.', c=[f'{k} * {k} * {m}'])
        return luecken(f'Ziehe teilweise die Wurzel, so weit wie möglich: √({r}x²) für x ≥ 0.', '□x√□', 'Zahl vor x, Radikand', [k, m],
                       f'√({r}x²) = √({k * k} · {m} · x²) = {k}x√{m}.', 'Ziehe die Wurzel aus der Quadratzahl und aus x² getrennt.',
                       c=[f'{k}', f'{r} // {k * k}'])
    return luecken(f'Ziehe teilweise die Wurzel, so weit wie möglich: √{dz(r)}.', '□√□', 'Zahl vor der Wurzel, Radikand', [k, m],
                   f'√{dz(r)} = √({k * k} · {m}) = {k}√{m}.', 'Suche die größte Quadratzahl, die im Radikanden steckt.',
                   c=[f'{k}', f'{r} // {k * k}'])


def g_zusammenfassen(s):
    m = R.choice(QF[:6])
    if s <= 2 and R.random() < 0.25:
        a, b = sorted(R.sample([2, 3, 5, 6, 7, 10, 11], 2))
        return auswahl(f'Kann man √{a} + √{b} zusammenfassen?', 'Nein, die Radikanden sind verschieden.',
                       [f'Ja, zu √{a + b}.', f'Ja, zu 2√{a + b}.', f'Ja, zu √{a * b}.'],
                       f'√{a} und √{b} sind wie verschiedene Variablen x und y: x + y bleibt stehen. Probe: (√{a} + √{b})² = {a + b} + 2√{a * b} ≠ {a + b}.',
                       'Wie ist es bei 2x + 4y?')
    if s == 1:
        a, b = R.randint(2, 9), R.randint(-9, 9)
        if b in (0, -a): return None
        e = a + b
        t = f'{wt(a, m)} {"+" if b > 0 else "−"} {wt(abs(b), m)}'
        return luecken(f'Fasse zusammen: {t}.', '□√□', 'Zahl vor der Wurzel, Radikand', [e, m],
                       f'Gleicher Radikand {m}: ({a} {"+" if b > 0 else "−"} {abs(b)})√{m} = {wt(e, m)}.',
                       'Gleiche Radikanden: Zahlen vor der Wurzel zusammenrechnen.', c=[f'{a} + ({b})', f'{m}'])
    if s == 2:
        p, q = R.sample(range(1, 6), 2)
        sg = R.choice([1, -1])
        e = p + sg * q
        if e == 0: return None
        t = f'√{p * p * m} {"+" if sg > 0 else "−"} √{q * q * m}'
        return luecken(f'Fasse zusammen: {t}.', '□√□', 'Zahl vor der Wurzel, Radikand', [e, m],
                       f'√{p * p * m} = {wt(p, m)}, √{q * q * m} = {wt(q, m)}; zusammen {wt(e, m)}.',
                       'Ziehe zuerst teilweise die Wurzel, damit gleiche Radikanden entstehen.', c=[f'{p} + ({sg * q})', f'{m}'])
    typ = R.random()
    if typ < 0.4:
        a = R.randint(2, 9)
        b = R.choice(QF[:6])
        if a * a == b: return None
        return zahl(f'Berechne ({a} + √{b}) · ({a} − √{b}).', f'3. binomische Formel: {a}² − (√{b})² = {a * a} − {b} = {a * a - b}.',
                    'Welche binomische Formel steckt dahinter?', a * a - b, f'{a} * {a} - {b}')
    if typ < 0.7:
        a, b = R.randint(1, 5), R.choice(QF[:6])
        return luecken(f'Multipliziere aus und fasse zusammen: ({a} + √{b})².', '□ + □√□', 'Zahl, Zahl vor der Wurzel, Radikand',
                       [a * a + b, 2 * a, b], f'({a} + √{b})² = {a * a} + 2 · {a} · √{b} + {b} = {a * a + b} + {2 * a}√{b}.',
                       '1. binomische Formel: (x + y)² = x² + 2xy + y².', c=[f'{a} * {a} + {b}', f'2 * {a}', f'{b}'])
    p, q, r_ = R.randint(1, 4), R.randint(1, 4), R.randint(2, 5)
    e = p + q - r_
    if e == 0: return None
    t = f'√{p * p * m} + √{q * q * m} − {wt(r_, m)}'
    return luecken(f'Fasse zusammen: {t}.', '□√□', 'Zahl vor der Wurzel, Radikand', [e, m],
                   f'{wt(p, m)} + {wt(q, m)} − {wt(r_, m)} = ({p} + {q} − {r_})√{m} = {wt(e, m)}.',
                   'Erst alle Wurzeln teilweise ziehen, dann zusammenfassen.', c=[f'{p} + {q} - {r_}', f'{m}'])


def g_nenner_rational(s):
    m = R.choice(QF)
    if s == 1:
        k = R.randint(2, 6)
        a = k * m
        return luecken(f'Mache den Nenner rational: {a}/√{m}.', '□√□', 'Zahl vor der Wurzel, Radikand', [k, m],
                       f'{a}/√{m} = {a}√{m} / {m} = {wt(k, m)}.', 'Erweitere den Bruch mit der Wurzel aus dem Nenner.',
                       c=[f'{a} / {m}', f'{m}'])
    if s == 2:
        b, k = R.randint(2, 5), R.randint(2, 5)
        a = k * b * m
        return luecken(f'Mache den Nenner rational: {a}/({b}√{m}).', '□√□', 'Zahl vor der Wurzel, Radikand', [k, m],
                       f'{a}/({b}√{m}) = {a}√{m} / ({b} · {m}) = {a}√{m} / {b * m} = {wt(k, m)}.',
                       'Erweitere mit √' + str(m) + ' und kürze danach.', c=[f'{a} / ({b} * {m})', f'{m}'])
    mm = R.choice([x for x in QF if x > 2])
    n = R.randint(1, isqrt(mm))
    d = mm - n * n
    if d <= 0: return None
    k = R.randint(2, 4)
    z = k * d
    return luecken(f'Mache den Nenner rational: {z}/(√{mm} − {n}).', '□ · (√□ + □)', 'Faktor, Radikand, Zahl',
                   [k, mm, n], f'Mit √{mm} + {n} erweitern: Nenner (√{mm})² − {n}² = {mm} − {n * n} = {d}. {z}/{d} = {k}, also {k} · (√{mm} + {n}).',
                   'Erweitere mit √' + str(mm) + ' + ' + str(n) + ' und nutze die 3. binomische Formel.',
                   c=[f'{z} / ({mm} - {n} * {n})', f'{mm}', f'{n}'])


GEN = {'zahlarten': g_zahlarten, 'eingrenzen': g_eingrenzen, 'wurzel_mal': g_wurzel_mal, 'teilweise': g_teilweise,
       'zusammenfassen': g_zusammenfassen, 'nenner_rational': g_nenner_rational}

# ---------- Zehnte Runde (schwer-kl9): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Abschnitt mit eigenem festen Zufallsstart (anhaengen(..., 9902, ...)), läuft erst nach bauen():
# alle bisherigen Aufgaben bleiben unverändert. Vorbilder: Illustrierende Aufgaben Realschule Jgst. 9 (I), ISB
# (Fachbegriffe rational/irrational/reell, Behauptung zum Rationalmachen beurteilen, Lückentexte mit Wurzeln),
# Bayerischer Mathematik-Test 10 (Terme ohne Taschenrechner, Näherungswerte). Zahlen und Wortlaut eigen.
from _schwer_kl9 import anhaengen  # noqa: E402


def schwer():
    P, K, O = 'pruefung', 'knobel', ''
    L = 'Zahlen in die Felder eintragen'
    return [
        # zahlarten
        ('zahlarten', 3, P, auswahl('Welche Aussage ist wahr?', 'Jede rationale Zahl ist auch eine reelle Zahl.',
                                    ['Jede reelle Zahl ist rational.', '√2 ist rational, weil der Taschenrechner 1,414213562 anzeigt.', 'Jede Wurzel ist irrational.'],
                                    'ℚ ist ein Teil von ℝ. Umgekehrt nicht: √2 ist reell, aber irrational – der Taschenrechner zeigt nur eine Näherung. √9 = 3 ist eine rationale Wurzel.',
                                    'Prüfe jede Aussage mit einem Gegenbeispiel wie √9 oder √2.')),
        ('zahlarten', 3, P, auswahl('Welche der Zahlen ist rational?', '√0,09', ['√0,9', '√90', 'π/2'],
                                    '√0,09 = 0,3, denn 0,3² = 0,09. 0,9 und 90 sind keine Quadrate rationaler Zahlen, π/2 ist irrational.',
                                    'Achte auf die Nachkommastellen: Bei welcher Zahl geht die Wurzel glatt auf?')),
        ('zahlarten', 3, K, zahl('Wie viele der 50 Zahlen √1, √2, √3, …, √50 sind rational?',
                                 'Rational sind nur die Wurzeln aus Quadratzahlen: 1, 4, 9, 16, 25, 36, 49. Das sind 7 Zahlen.',
                                 'Eine Wurzel aus einer natürlichen Zahl ist nur rational, wenn die Zahl eine Quadratzahl ist.', 7, '1 + 1 + 1 + 1 + 1 + 1 + 1')),
        ('zahlarten', 3, O, auswahl('Ist √2 · √8 rational oder irrational?', 'rational, denn √2 · √8 = √16 = 4',
                                    ['irrational, weil beide Faktoren irrational sind', 'irrational, denn √2 · √8 = √10', 'rational, denn 2 · 8 = 16 ist gerade'],
                                    '√2 · √8 = √(2 · 8) = √16 = 4. Das Produkt zweier irrationaler Zahlen kann rational sein.',
                                    'Fasse zu einer Wurzel zusammen und rechne aus.')),
        ('zahlarten', 2, O, auswahl('Welche Zahl ist irrational?', '√12', ['√(4/9)', '0,555… (die 5 wiederholt sich)', '−√16'],
                                    '12 ist keine Quadratzahl, also ist √12 irrational. √(4/9) = 2/3, 0,555… = 5/9, −√16 = −4.',
                                    'Prüfe, welche Zahl sich als Bruch schreiben lässt.')),
        ('zahlarten', 2, O, auswahl('Zu welcher kleinsten Zahlenmenge gehört −√25?', 'ℤ (ganze Zahlen)',
                                    ['ℕ (natürliche Zahlen)', 'ℚ (rationale Zahlen)', 'ℝ (reelle Zahlen)'],
                                    '−√25 = −5 ist eine negative ganze Zahl, also nicht in ℕ, aber in ℤ.', 'Rechne zuerst aus und achte auf das Minus.')),
        # eingrenzen
        ('eingrenzen', 3, P, auswahl('Ein quadratischer Tisch soll mindestens 2 m² Fläche haben. Reicht eine Seitenlänge von 1,41 m?',
                                     'Nein, knapp nicht: 1,41² = 1,9881 < 2.', ['Ja, denn 1,41² = 2,82.', 'Ja, denn √2 ist genau 1,41.', 'Nein, man bräuchte mindestens 1,5 m.'],
                                     '1,41 · 1,41 = 1,9881 m², das ist etwas weniger als 2 m². √2 ≈ 1,4142 ist irrational, 1,41 ist nur eine Näherung. 1,42² = 2,0164 würde reichen.',
                                     'Quadriere 1,41 und vergleiche mit 2.')),
        ('eingrenzen', 3, P, auswahl('Welche Zahl liegt zwischen √5 und √6?', '2,3', ['2,5', '2,2', '5,5'],
                                     '2,3² = 5,29 liegt zwischen 5 und 6, also √5 < 2,3 < √6. 2,5² = 6,25 ist zu groß, 2,2² = 4,84 zu klein. 5,5 liegt zwischen 5 und 6, aber nicht zwischen den Wurzeln.',
                                     'Quadriere die Kandidaten und vergleiche mit 5 und 6.')),
        ('eingrenzen', 3, K, zahl('Wie viele ganze Zahlen liegen zwischen −√10 und √30?',
                                  '−√10 ≈ −3,16 und √30 ≈ 5,48. Dazwischen liegen die ganzen Zahlen −3, −2, …, 5: das sind 5 − (−3) + 1 = 9 Zahlen.',
                                  'Grenze beide Wurzeln zwischen ganzen Zahlen ein (3² = 9, 4² = 16, 5² = 25, 6² = 36). Vergiss die 0 nicht.', 9, '5 - (-3) + 1')),
        ('eingrenzen', 3, O, auswahl('Zwischen welchen Zahlen mit einer Nachkommastelle liegt √0,9?', '0,9 und 1,0',
                                     ['0,3 und 0,4', '0,4 und 0,5', '0,09 und 0,1'],
                                     '0,9² = 0,81 < 0,9 < 1 = 1,0². Also 0,9 < √0,9 < 1,0. Falle: 0,3² = 0,09 – das wäre √0,09.',
                                     'Bei Zahlen zwischen 0 und 1 ist die Wurzel größer als die Zahl. Quadriere 0,9 und 1,0.')),
        ('eingrenzen', 2, O, auswahl('Zwischen welchen Zahlen mit einer Nachkommastelle liegt √20?', '4,4 und 4,5', ['4,5 und 4,6', '10,0 und 10,1', '4,3 und 4,4'],
                                     '4,4² = 19,36 < 20 < 20,25 = 4,5², also 4,4 < √20 < 4,5.', 'Quadriere Zahlen wie 4,4 und 4,5.')),
        ('eingrenzen', 2, O, auswahl('Welche Zahl ist größer: √50 oder 7,1?', '7,1', ['√50', 'Beide sind gleich groß.'],
                                     '7,1² = 50,41 > 50, also ist 7,1 > √50.', 'Quadriere beide Zahlen und vergleiche.')),
        # wurzel_mal
        ('wurzel_mal', 3, P, zahl('Berechne ohne Taschenrechner √0,5 · √50.', '√0,5 · √50 = √(0,5 · 50) = √25 = 5.',
                                  'Fasse zu einer Wurzel zusammen.', 5, '(0.5 * 50) / 5')),
        ('wurzel_mal', 3, P, zahl('Berechne ohne Taschenrechner √(2/3) · √(27/2).', '√(2/3 · 27/2) = √(54/6) = √9 = 3.',
                                  'Fasse zu einer Wurzel zusammen und kürze den Bruch unter der Wurzel.', 3, '(2 / 3) * (27 / 2) / 3')),
        ('wurzel_mal', 3, K, zahl('Welche kleinste natürliche Zahl n > 0 macht √(12 · n) zu einer natürlichen Zahl?',
                                  '12 = 4 · 3. Damit 12 · n eine Quadratzahl wird, fehlt noch eine 3: 12 · 3 = 36 = 6². Also n = 3.',
                                  'Zerlege 12 in Faktoren. Welcher Faktor fehlt zur Quadratzahl?', 3, '36 / 12')),
        ('wurzel_mal', 3, O, auswahl('Vereinfache √(18a) · √(2a) für a ≥ 0.', '6a', ['36a²', '6a²', '√(20a)'],
                                     '√(18a · 2a) = √(36a²) = 6a (a ≥ 0). 36a² ist der Radikand, √(20a) entsteht durch falsches Addieren.',
                                     'Fasse zu einer Wurzel zusammen. Welche Zahl ergibt quadriert 36a²?')),
        ('wurzel_mal', 2, O, zahl('Berechne √72 : √2.', '√72 : √2 = √(72 : 2) = √36 = 6.', 'Fasse zu einer Wurzel zusammen.', 6, '(72 / 2) / 6')),
        ('wurzel_mal', 2, O, zahl('Berechne √3 · √12.', '√3 · √12 = √36 = 6.', 'Fasse zu einer Wurzel zusammen.', 6, '(3 * 12) / 6')),
        # teilweise
        ('teilweise', 3, P, luecken('Ergänze die Lücke: √□ = 5√3.', '√□', 'die Zahl unter der Wurzel eintragen', [75],
                                    '5√3 = √25 · √3 = √(25 · 3) = √75.', 'Bringe die 5 als √25 unter die Wurzel.', ['25 * 3'])),
        ('teilweise', 3, P, luecken('Ein Quadrat hat den Flächeninhalt 98 cm². Gib die Seitenlänge exakt an (teilweise Wurzel ziehen).', '□√□ cm', L, [7, 2],
                                    'a = √98 cm = √(49 · 2) cm = 7√2 cm.', 'Seite = √Fläche. Suche die größte Quadratzahl in 98.', ['49 // 7', '98 // 49'])),
        ('teilweise', 3, K, auswahl('Welche Zahl ist am größten?', '5√2', ['3√5', '2√11', '4√3'],
                                    'Unter eine Wurzel bringen: 3√5 = √45, 2√11 = √44, 4√3 = √48, 5√2 = √50. Am größten ist √50 = 5√2.',
                                    'Bringe jeweils den Faktor als Quadrat unter die Wurzel und vergleiche die Radikanden.')),
        ('teilweise', 3, O, luecken('Ziehe teilweise die Wurzel, so weit wie möglich: √(50x³) für x ≥ 0.', '□x√(□x)', L, [5, 2],
                                    '√(50x³) = √(25 · 2 · x² · x) = 5x√(2x).', 'Zerlege 50 = 25 · 2 und x³ = x² · x. Aus den Quadraten ziehst du die Wurzel.', ['25 // 5', '50 // 25'])),
        ('teilweise', 2, O, luecken('Ziehe teilweise die Wurzel, so weit wie möglich: √180.', '□√□', L, [6, 5],
                                    '√180 = √(36 · 5) = 6√5.', 'Suche die größte Quadratzahl, die in 180 steckt.', ['36 // 6', '180 // 36'])),
        ('teilweise', 2, O, luecken('Schreibe 3√7 als eine einzige Wurzel.', '√□', 'die Zahl unter der Wurzel eintragen', [63],
                                    '3√7 = √9 · √7 = √63.', 'Schreibe 3 als √9.', ['9 * 7'])),
        # zusammenfassen
        ('zusammenfassen', 3, P, luecken('Fasse zusammen: √12 + √27 − √48.', '□√□', L, [1, 3],
                                         '√12 = 2√3, √27 = 3√3, √48 = 4√3. Zusammen (2 + 3 − 4)√3 = 1√3 = √3.',
                                         'Ziehe bei jedem Summanden teilweise die Wurzel. Alle haben dann den Radikanden 3.', ['2 + 3 - 4', '3'])),
        ('zusammenfassen', 3, P, zahl('Berechne (√6 + √2) · (√6 − √2).', '3. binomische Formel: (√6)² − (√2)² = 6 − 2 = 4.',
                                      'Erkenne die Form (a + b)(a − b).', 4, '6 - 2')),
        ('zusammenfassen', 3, K, luecken('Berechne geschickt: (√3 + 1)² − (√3 − 1)².', '□√□', L, [4, 3],
                                         'Ausmultiplizieren: (3 + 2√3 + 1) − (3 − 2√3 + 1) = 4√3. Kürzer: (a + b)² − (a − b)² = 4ab = 4 · √3 · 1.',
                                         'Multipliziere beide Klammern aus. Was fällt beim Subtrahieren weg?', ['2 + 2', '3'])),
        ('zusammenfassen', 3, O, zahl('Multipliziere aus und vereinfache: √2 · (√8 + √18).', '√2 · √8 + √2 · √18 = √16 + √36 = 4 + 6 = 10.',
                                      'Jeden Summanden in der Klammer mit √2 malnehmen.', 10, '4 + 6')),
        ('zusammenfassen', 2, O, luecken('Fasse zusammen: 3√5 + √20.', '□√□', L, [5, 5], '√20 = 2√5, also 3√5 + 2√5 = 5√5.',
                                         'Ziehe bei √20 teilweise die Wurzel.', ['3 + 2', '5'])),
        ('zusammenfassen', 2, O, luecken('Fasse zusammen: √27 − √3.', '□√□', L, [2, 3], '√27 = 3√3, also 3√3 − √3 = 2√3.',
                                         'Ziehe bei √27 teilweise die Wurzel.', ['3 - 1', '3'])),
        # nenner_rational
        ('nenner_rational', 3, P, auswahl('Ein Schüler sagt: „Bei 5/√7 mache ich den Nenner rational, indem ich nur den Nenner mit √7 malnehme. Dann steht da 5/7.“ Was stimmt?',
                                          'Falsch: Er muss auch den Zähler mit √7 malnehmen (erweitern): 5√7/7.',
                                          ['Richtig, denn √7 · √7 = 7.', 'Falsch: Er muss mit 7 erweitern.', 'Richtig, der Wert bleibt so gleich.'],
                                          'Nimmt man nur den Nenner mal √7, ändert sich der Wert (5/√7 ≈ 1,89, aber 5/7 ≈ 0,71). Erweitern heißt Zähler und Nenner mit derselben Zahl malnehmen.',
                                          'Vergleiche die Werte vorher und nachher mit dem Taschenrechner.')),
        ('nenner_rational', 3, P, luecken('Mache den Nenner rational: 2/(√7 + √5).', '√□ − √□', 'die Radikanden eintragen', [7, 5],
                                          'Mit √7 − √5 erweitern: Nenner (√7)² − (√5)² = 7 − 5 = 2. Also 2(√7 − √5)/2 = √7 − √5.',
                                          'Erweitere mit √7 − √5 (3. binomische Formel).', ['7', '5'])),
        ('nenner_rational', 3, K, zahl('Berechne 1/(√2 − 1) − 1/(√2 + 1).',
                                       '1/(√2 − 1) = √2 + 1 und 1/(√2 + 1) = √2 − 1 (jeweils erweitern, Nenner 2 − 1 = 1). Differenz: (√2 + 1) − (√2 − 1) = 2.',
                                       'Mache bei beiden Brüchen den Nenner rational. Der Nenner wird jeweils 1.', 2, '(1) - (-1)')),
        ('nenner_rational', 3, O, luecken('Mache den Nenner rational: 6/(3 + √3).', '□ − √□', L, [3, 3],
                                          'Mit 3 − √3 erweitern: Nenner 9 − 3 = 6. Also 6(3 − √3)/6 = 3 − √3.', 'Erweitere mit 3 − √3.', ['6 // 2', '3'])),
        ('nenner_rational', 2, O, luecken('Mache den Nenner rational und vereinfache: √3/√6.', '√□/□', L, [2, 2],
                                          '√3/√6 = √(3/6) = √(1/2) = 1/√2 = √2/2.', 'Fasse erst zu einer Wurzel zusammen und kürze.', ['2', '2'])),
        ('nenner_rational', 2, O, luecken('Mache den Nenner rational: 15/√5.', '□√□', L, [3, 5], '15/√5 = 15√5/5 = 3√5.',
                                          'Erweitere mit √5.', ['15 // 5', '5'])),
    ]


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('zahlen.reell', 13_9_2)
# b) Lösungsweg nennt Zahlen, die in der Auswahl nicht vorkommen
BF.loesung('zahlarten', 'Welche Zahl ist irrational?', enthaelt='"3,1416"', pools=('uebung',),
           w='π hat unendlich viele Nachkommastellen ohne Periode. 22/7, 3,14 und 3,1416 sind nur Näherungen für π und lassen sich als Bruch schreiben.')
BF.loesung('zahlarten', 'Welche Zahl ist irrational?', enthaelt='3,141414…', pools=('uebung',),
           w='π hat unendlich viele Nachkommastellen ohne Periode. 22/7 und 3,14 sind nur Näherungen und als Bruch schreibbar; 3,141414… ist periodisch, also auch ein Bruch.')
# a) gleicher Typ wie Stufe 2 bzw. Standard
BF.stufe('zahlarten', 'Welche der Zahlen ist irrational?', 2, enthaelt='"√107"')
BF.stufe('wurzel_mal', 'Berechne √375 : √15.', 2)

# ---- BEFUNDE ENDE ----


# ---------- Achtzehnte Runde, Teil B (Zweig luecken-kl9) ----------
# 1) neue Lernkarte „heron“ nach „eingrenzen“ – LehrplanPLUS M9 1: „erläutern das Heron-Verfahren und bestimmen mithilfe dieses
#    Algorithmus Näherungswerte für Quadratwurzeln … Sie sind sich des iterativen Charakters dieses Verfahrens bewusst.“
#    Vorbilder (Typ, eigene Zahlen): Tabellen-Aufgaben „Heron-Verfahren mit Startwert …, Werte in die Tabelle eintragen“ (Arbeitsblätter
#    Uni Stuttgart, Schülerseminar Iteration; NRW-Materialdatenbank), Schulaufgaben Kl. 9.
# 2) Karte „wurzel_mal“ um einen Schritt √(a²) = |a| und Aufgaben dazu erweitert (Grundwissen M9: √(a²) = |a|).
# 3) Sachaufgaben (Modellieren) als Stufe-3-Gruppe an den passenden Karten.
# Eigene Zufallsstarts, alles Alte bleibt unverändert.
from fractions import Fraction as _Fr  # noqa: E402
from _luecken_kl9 import einbauen, erweitern  # noqa: E402

HE_L = 'heron'
_HE_KOPF = ['Schritt', 'Seite x', '10 : x', 'Mittelwert']
KARTE_HE = {
    'lernziel': HE_L, 'titel': 'Wurzeln mit dem Heron-Verfahren',
    'einstieg': 'Ein quadratisches Beet soll 10 m² groß sein. Wie lang ist eine Seite? Du startest mit einem Rechteck '
                'und machst es Schritt für Schritt quadratischer: das ⟦Heron-Verfahren⟧.',
    'woerter': [['Heron-Verfahren', 'Rechenweg, der eine Wurzel Schritt für Schritt genauer annähert'],
                ['Startwert', 'die erste Schätzung für die Seite, z. B. 3 m'],
                ['Mittelwert', '(x + y) : 2, die Zahl genau in der Mitte zwischen x und y']],
    'bild': {'typ': 'tabelle', 'kopf': _HE_KOPF, 'zeilen': [['0', '3', '?', '?']]},
    'schritte': [{'text': 'Startwert 3 m: Die andere Seite ist 10 : 3 ≈ 3,333 m.', 'bild': {'zeilen': [['0', '3', '3,333', '?']]}},
                 {'text': 'Mittelwert: (3 + 3,333) : 2 ≈ 3,167. Das ist die neue Seite.',
                  'bild': {'zeilen': [['0', '3', '3,333', '3,167'], ['1', '3,167', '?', '?']]}},
                 {'text': 'Wiederholen: 10 : 3,167 ≈ 3,158, Mittelwert ⟦≈ 3,16⟧.',
                  'bild': {'zeilen': [['0', '3', '3,333', '3,167'], ['1', '3,167', '3,158', '3,16']]}},
                 {'text': 'Probe: 3,16² ≈ 9,99. Die Seite ist also etwa ⟦3,16 m⟧ lang.'}],
    'fehler': 'Nicht 10 : 2 = 5 rechnen. Halbieren ist kein Wurzelziehen. Ein Beet mit 5 m Seite hätte 25 m², nicht 10 m².',
    'fehler_bild': {'typ': 'tabelle', 'kopf': ['Seite', 'Fläche'], 'zeilen': [['5 m', '25 m², zu groß'], ['3,16 m', '≈ 10 m²']]},
    'regel': 'Neue Seite = Mittelwert aus x und a : x. Wiederhole, bis sich die Ziffern nicht mehr ändern.',
    'probe': '3,162² ≈ 9,998, also fast genau 10.',
}


def _heron(a, x0, n):
    x = _Fr(x0)
    for _ in range(n):
        x = (x + _Fr(a) / x) / 2
    return x


def _he_rz(wert_, nd):
    w = gerundet(float(wert_), nd)
    assert w is not None, (wert_, nd)
    return w, f'round({K(float(wert_))}, {nd})'


def _he_schritt(a, x0, pool_vorn=''):
    w, c = _he_rz(_heron(a, x0, 1), 2)
    q = _Fr(a, x0)
    qt = f'= {dz(q)}' if endlich(q) else f'≈ {dz(round(a / x0, 3))}'
    mt = '=' if endlich(_heron(a, x0, 1)) and _heron(a, x0, 1) == _Fr(str(w)) else '≈'
    return zahl(f'{pool_vorn}Führe für √{a} einen Schritt des Heron-Verfahrens mit dem Startwert {x0} aus. Runde auf zwei Nachkommastellen.',
                f'Andere Seite: {a} : {x0} {qt}. Mittelwert: ({x0} + {qt[2:]}) : 2 {mt} {dz(w)}.',
                'Teile a durch den Startwert und bilde den Mittelwert aus beiden Seiten.', w, c)


def heron_aufgaben():
    L = []

    def neu(pool, s, art, a):
        a['l'] = HE_L
        L.append((pool, s, art, a))

    # Stufe 1
    neu('uebung', 1, '', zahl('Heron-Verfahren für √7 mit dem Startwert 2: Wie lang ist die andere Rechteckseite 7 : 2?',
                              'Das Rechteck hat die Fläche 7 und eine Seite 2. Die andere Seite ist 7 : 2 = 3,5.', 'Fläche durch bekannte Seite.', _Fr(7, 2), '7 / 2'))
    neu('uebung', 1, '', zahl('Heron-Verfahren für √7: Startwert 2, andere Seite 3,5. Wie groß ist der neue Wert, der Mittelwert der beiden Seiten?',
                              'Mittelwert: (2 + 3,5) : 2 = 2,75.', 'Mittelwert = (x + y) : 2.', _Fr(11, 4), '(2 + 7 / 2) / 2'))
    neu('uebung', 1, '', zahl('Berechne für √20 mit dem Startwert 4 den ersten Schritt des Heron-Verfahrens.',
                              'Andere Seite 20 : 4 = 5. Mittelwert (4 + 5) : 2 = 4,5.', 'Erst 20 : 4, dann der Mittelwert.', _Fr(9, 2), '(4 + 20 / 4) / 2'))
    w, c = _he_rz(_heron(13, 3, 1), 2)
    neu('uebung', 1, '', zahl('Berechne für √13 mit dem Startwert 3 den ersten Schritt des Heron-Verfahrens. Runde auf zwei Nachkommastellen.',
                              f'Andere Seite 13 : 3 ≈ 4,333. Mittelwert (3 + 4,333) : 2 ≈ {dz(w)}.', 'Erst 13 : 3, dann der Mittelwert.', w, c))
    # Stufe 2
    for a, x0 in ((5, 2), (30, 5), (2, 1)):
        x1 = _heron(a, x0, 1)
        w, c = _he_rz(_heron(a, x0, 2), 3)
        neu('uebung', 2, '', zahl(f'Berechne für √{a} mit dem Startwert {x0} zwei Schritte des Heron-Verfahrens. Gib x₂ auf drei Nachkommastellen an.',
                                  f'x₁ = ({x0} + {a} : {x0}) : 2 = {dz(x1) if endlich(x1) else dz(round(float(x1), 4))}. '
                                  f'x₂ = (x₁ + {a} : x₁) : 2 ≈ {dz(w)}.',
                                  'Mit dem Ergebnis des ersten Schritts rechnest du genauso weiter.', w, c))
    w, c = _he_rz(_heron(40, 6, 1), 2)
    neu('uebung', 2, '', zahl('Die Tabelle zeigt einen Schritt des Heron-Verfahrens für √40. Welcher Wert gehört in das Feld „?“? Runde auf zwei Nachkommastellen.',
                              f'Mittelwert aus 6 und 40 : 6 ≈ 6,667: (6 + 6,667) : 2 ≈ {dz(w)}.', 'In die letzte Spalte gehört der Mittelwert.', w, c,
                              grafik={'typ': 'tabelle', 'kopf': ['Seite x', '40 : x', 'Mittelwert'], 'zeilen': [['6', '6,67', '?']]}))
    neu('uebung', 2, '', auswahl('Welcher Startwert liegt am nächsten an √50?', '7', ['25 (die Hälfte von 50)', '5', '10'],
                                 '7 · 7 = 49 liegt sehr nah an 50. 5 · 5 = 25 und 10 · 10 = 100 sind weit weg; die Hälfte von 50 hat mit der Wurzel nichts zu tun.',
                                 'Welche Zahl mal sich selbst ergibt fast 50?'))
    w, c = _he_rz(_heron(11, 3, 1), 2)
    neu('uebung', 2, '', zahl('Ein quadratisches Fenster soll 11 dm² groß sein. Berechne die Seite mit einem Heron-Schritt, Startwert 3 dm. Runde auf zwei Nachkommastellen.',
                              f'Andere Seite 11 : 3 ≈ 3,667 dm. Mittelwert (3 + 3,667) : 2 ≈ {dz(w)} dm.', 'Fläche : Startwert, dann Mittelwert.', w, c, einheit='dm'))
    # Stufe 3
    w, c = _he_rz(_heron(17, 4, 2), 4)
    neu('uebung', 3, 'pruefung', zahl('Bestimme √17 mit dem Heron-Verfahren. Starte mit 4 und rechne zwei Schritte. Gib x₂ auf vier Nachkommastellen an.',
                                      f'x₁ = (4 + 17 : 4) : 2 = (4 + 4,25) : 2 = 4,125. x₂ = (4,125 + 17 : 4,125) : 2 ≈ (4,125 + 4,1212) : 2 ≈ {dz(w)}.',
                                      'Rechne mit möglichst vielen Stellen und runde erst am Ende.', w, c))
    neu('uebung', 3, 'knobel', zahl('Jemand rechnet einen Heron-Schritt mit dem Startwert 3 und erhält 3,5. Von welcher Zahl a wollte er die Wurzel bestimmen?',
                                    '(3 + a : 3) : 2 = 3,5 ⇒ 3 + a : 3 = 7 ⇒ a : 3 = 4 ⇒ a = 12.', 'Rechne den Heron-Schritt rückwärts.', 12, '(2 * 3.5 - 3) * 3'))
    w, c = _he_rz(_heron(27, 5, 2), 3)
    neu('uebung', 3, 'pruefung', zahl('Die Tabelle zeigt das Heron-Verfahren für √27. Berechne den Wert x₂ in der zweiten Zeile auf drei Nachkommastellen.',
                                      f'27 : 5,2 ≈ 5,1923. x₂ = (5,2 + 5,1923) : 2 ≈ {dz(w)}.', 'Die neue Seite 5,2 ist der Startwert der zweiten Zeile.', w, c,
                                      grafik={'typ': 'tabelle', 'kopf': ['Seite x', '27 : x', 'Mittelwert'], 'zeilen': [['5', '5,4', '5,2'], ['5,2', '?', 'x₂ = ?']]}))
    neu('uebung', 3, '', auswahl('Warum liegt √a immer zwischen x und a : x?', 'Ist x zu groß, ist a : x zu klein, denn x · (a : x) = a.',
                                 ['Weil x und a : x immer gleich groß sind.', 'Weil a : x immer kleiner als x ist.', 'Weil der Mittelwert immer genau √a ist.'],
                                 'Beide Seiten zusammen ergeben die Fläche a. Wäre jede größer als √a, wäre die Fläche zu groß; wäre jede kleiner, zu klein. '
                                 'Also liegt eine darüber, eine darunter.', 'Denke an das Rechteck mit der Fläche a.'))
    w, c = _he_rz(_heron(100, 1, 2), 1)
    neu('uebung', 3, '', zahl('Jemand bestimmt √100 mit dem Heron-Verfahren, aber mit dem schlechten Startwert 1. Wie groß ist x₂? Runde auf eine Nachkommastelle.',
                              f'x₁ = (1 + 100) : 2 = 50,5. x₂ = (50,5 + 100 : 50,5) : 2 ≈ (50,5 + 1,98) : 2 ≈ {dz(w)}. Ein schlechter Startwert braucht viele Schritte.',
                              'Rechne zwei Schritte. Wie weit ist x₂ noch von 10 entfernt?', w, c))
    w, c = _he_rz(_heron(200, 14, 2), 2)
    neu('uebung', 3, 'pruefung', zahl('Ein quadratischer Platz soll 200 m² groß sein. Bestimme die Seitenlänge mit zwei Heron-Schritten, Startwert 14 m. Runde auf zwei Nachkommastellen.',
                                      f'x₁ = (14 + 200 : 14) : 2 ≈ (14 + 14,2857) : 2 ≈ 14,1429. x₂ = (14,1429 + 200 : 14,1429) : 2 ≈ {dz(w)} m.',
                                      'Teile die Fläche durch die Seite und bilde den Mittelwert, zweimal.', w, c, einheit='m'))
    neu('uebung', 3, '', auswahl('Jemand rechnet für √8 mit dem Startwert 2: x₁ = (2 + 8) : 2 = 5. Was stimmt?', 'Falsch: Es heißt (2 + 8 : 2) : 2 = 3.',
                                 ['Richtig.', 'Falsch: Es heißt (2 + 8) : 8 = 1,25.', 'Falsch: Es heißt 8 : 2 = 4.'],
                                 'Gemittelt werden die beiden Rechteckseiten: 2 und 8 : 2 = 4. Mittelwert (2 + 4) : 2 = 3. 5 · 5 = 25 wäre viel zu groß.',
                                 'Welche zwei Seiten hat das Rechteck mit der Fläche 8?'))
    neu('uebung', 3, 'knobel', zahl('Nach wie vielen Heron-Schritten mit dem Startwert 2 stimmt √5 ≈ 2,236 auf drei Nachkommastellen?',
                                    'x₁ = 2,25 (gerundet 2,250, noch falsch). x₂ ≈ 2,2361 (gerundet 2,236, stimmt). Also nach 2 Schritten.',
                                    'Rechne Schritt für Schritt und vergleiche jeweils mit 2,236.', 2, '2'))
    # Test, Korrektur, Sicherung: je ein Heron-Schritt
    vorrat = [14, 15, 18, 19, 21, 22, 23, 24, 26, 28, 29, 31, 33, 35, 38, 39, 41, 42, 43, 44, 45, 47, 48, 52, 53, 55, 58, 59]
    gew = []
    while len(gew) < 10:
        a = R.choice(vorrat)
        x0 = isqrt(a)
        if a in gew or a % x0 == 0 or gerundet(float(_heron(a, x0, 1)), 2) is None: continue  # keine glatten Teilungen
        gew.append(a)
    pools = ['test'] + ['korrektur'] * 3 + ['sicherung'] * 6
    for p, a in zip(pools, gew):
        neu(p, 2, '', _he_schritt(a, isqrt(a)))
    return L


SCHRITT_BETRAG = {'text': 'Achtung bei negativen Zahlen: √((−3)²) = √9 = 3. Also ⟦√(a²) = |a|⟧.',
                  'bild': {'typ': 'zahlenstrahl', 'start': -4, 'ende': 4, 'abschnitte': 8, 'beschriftet': 'anfang_ende',
                           'punkte': [{'wert': -3, 'name': '−3'}, {'wert': 3, 'name': '√9 = 3'}], 'boegen': [{'von': -3, 'bis': 0, 'name': '|−3|'}]}}


def betrag_aufgaben():
    L = []

    def neu(s, a):
        a['l'] = 'wurzel_mal'
        L.append(('uebung', s, '', a))
    neu(2, zahl('Berechne √((−5)²).', '(−5)² = 25 und √25 = 5. Die Wurzel ist nie negativ: √((−5)²) = |−5| = 5.', 'Rechne zuerst unter der Wurzel.', 5, '((-5) ** 2 + 0) // 5'))
    neu(2, zahl('Berechne √(x²) für x = −7.', 'x² = 49, √49 = 7 = |−7|.', 'Setze ein und rechne zuerst x².', 7, 'abs(-7)'))
    neu(3, auswahl('Für welche Zahlen x gilt √(x²) = x?', 'für x ≥ 0', ['für alle x', 'nur für x > 0', 'für x ≤ 0'],
                   '√(x²) = |x|. |x| = x gilt genau für x ≥ 0 (auch für 0). Für x = −2 wäre √4 = 2 ≠ −2.', 'Probiere x = −2, x = 0 und x = 2.'))
    neu(3, auswahl('Vereinfache √(49a²) für a < 0.', '−7a', ['7a', '49a', '−49a'],
                   '√(49a²) = 7 · |a|. Für a < 0 ist |a| = −a, also 7 · (−a) = −7a (positiv, weil a negativ ist).', 'Es gilt √(a²) = |a|. Was ist |a| bei negativem a?'))
    return L


def sach_reell():
    L = []

    def neu(l, a):
        a['l'] = l
        L.append(('uebung', 3, '', a))
    neu('eingrenzen', luecken('Ein Stein fällt aus 60 m Höhe. Für die Fallzeit gilt etwa t = √(60 : 5) s. Zwischen welchen ganzen Sekunden liegt t?',
                              '□ s < t < □ s', 'zwei ganze Zahlen', [3, 4], 't = √12. 3² = 9 < 12 < 16 = 4², also liegt t zwischen 3 s und 4 s.',
                              'Rechne 60 : 5 und suche die Quadratzahlen davor und danach.', c=['3', '4']))
    neu('wurzel_mal', zahl('Ein Rechteck ist √8 m breit und √18 m lang. Wie groß ist seine Fläche?', '√8 · √18 = √(8 · 18) = √144 = 12 m².',
                           'Zieh die Wurzeln zu einer zusammen.', 12, '(8 * 18) // 12', einheit='m²'))
    neu('wurzel_mal', zahl('Aus einer Bremsspur von s Metern schätzt man die Geschwindigkeit mit v = √(200 · s) (v in km/h). Wie schnell war ein Auto mit 8 m Bremsspur?',
                           'v = √(200 · 8) = √1600 = 40 km/h.', 'Rechne erst unter der Wurzel.', 40, '200 * 8 // 40', einheit='km/h'))
    neu('teilweise', luecken('Ein quadratischer Platz hat 50 m² Fläche. Gib die Seitenlänge exakt an (teilweise Wurzel ziehen).', '□√□ m', 'Zahl vor der Wurzel, Zahl unter der Wurzel',
                             [5, 2], '√50 = √(25 · 2) = 5√2 m.', 'Suche in 50 die größte Quadratzahl.', c=['5', '2']))
    neu('zusammenfassen', luecken('Zwei quadratische Beete haben 8 m² und 18 m². Jedes bekommt ringsum einen Zaun. Gib die gesamte Zaunlänge exakt an.', '□√□ m',
                                  'Zahl vor der Wurzel, Zahl unter der Wurzel', [20, 2], 'Seiten √8 = 2√2 und √18 = 3√2. Zaun: 4 · 2√2 + 4 · 3√2 = 8√2 + 12√2 = 20√2 m.',
                                  'Zieh teilweise die Wurzel, dann kannst du zusammenfassen.', c=['4 * 2 + 4 * 3', '2']))
    neu('nenner_rational', luecken('Ein Rechteck hat 6 m² Fläche und ist √3 m breit. Gib seine Länge exakt mit rationalem Nenner an.', '□√□ m',
                                   'Zahl vor der Wurzel, Zahl unter der Wurzel', [2, 3], 'Länge 6/√3 = 6√3/3 = 2√3 m.', 'Länge = Fläche : Breite. Erweitere mit √3.',
                                   c=['6 // 3', '3']))
    return L

if __name__ == '__main__':
    d = bauen('zahlen.reell',
          'Irrationale Zahlen erkennen, Wurzeln eingrenzen, Wurzelterme vereinfachen und Nenner rational machen.',
          ['ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ. Irrational: unendlich, nicht periodisch (z. B. √2).', '√a · √b = √(ab), √a : √b = √(a : b) – aber nicht für Summen.',
           'Teilweise radizieren: √(k²m) = k√m.', 'Wurzel im Nenner: erweitern (bei √m ± n mit der 3. binomischen Formel).'],
          [('Reelle Zahlen', ['zahlarten', 'eingrenzen']), ('Rechnen mit Wurzeln', ['wurzel_mal', 'teilweise', 'zusammenfassen']),
           ('Nenner rational machen', ['nenner_rational'])],
          ETAPPEN, GEN,
          meiden={'zahlarten': ['√50?'], 'eingrenzen': ['√30?'], 'wurzel_mal': ['√3 · √27.'], 'teilweise': ['√72.'],
                  'zusammenfassen': ['√18 + √50.'], 'nenner_rational': ['12/√3.']},
          offen=['Lückentext „□√□“: Die App zeigt das Wurzelzeichen nur als Text in der Schablone; bitte prüfen, ob die Darstellung im Eingabefeld gut lesbar ist.'])
    anhaengen(d, 9902, schwer)
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden
    # Achtzehnte Runde: Lehrplan-Lücken (Heron, √(a²) = |a|, Sachaufgaben)
    einbauen('zahlen.reell', KARTE_HE, 'eingrenzen', 18_9_3, heron_aufgaben)
    erweitern('zahlen.reell', 'wurzel_mal', 18_9_4, betrag_aufgaben, schritt=SCHRITT_BETRAG)
    erweitern('zahlen.reell', 'eingrenzen', 18_9_5, sach_reell)


# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl9) ----
from _durchsicht_kl9 import Befunde as _DSB, durchsicht  # noqa: E402

DS = _DSB('zahlen.reell', 19_9_2)
# zahlarten: „rational oder irrational?“ mit größerer Zahl = Stufe-1-Gedanke; „welche ist irrational?“ wie Stufe 2
for _t in ('Ist √576 rational oder irrational?', 'Ist √103 rational oder irrational?', 'Ist √289 rational oder irrational?'):
    DS.stufe('zahlarten', _t, 1)
DS.stufe('zahlarten', 'Welche der Zahlen ist irrational?', 2, enthaelt='√14')
# eingrenzen: Hundertstel statt Zehntel ist nur eine längere Rechnung → Stufe 2
for _z in ('√134', '√41', '√105', '√19', '√56', '√150'):
    DS.stufe('eingrenzen', f'Zwischen welchen Zahlen mit 2 Nachkommastellen liegt {_z}?', 2)
# wurzel_mal: √3 · √12 ist die Stufe-1-Aufgabe; Rechenketten auf Stufe 2
DS.stufe('wurzel_mal', 'Berechne √3 · √12.', 1)
DS.stufe('wurzel_mal', 'Berechne √52 · √468 − √256.', 2)
DS.stufe('wurzel_mal', 'Berechne √50 · √18 − √196.', 2)
# teilweise: dieselbe Aufgabe mit größeren Zahlen → Stufe 1; „als eine Wurzel schreiben“ (Umkehrung) → Stufe 2
for _z in ('√208', '√810', '√704', '√600', '√384', '√180', '√1 215', '√1 300', '√250'):
    DS.stufe('teilweise', f'Ziehe teilweise die Wurzel, so weit wie möglich: {_z}.', 1)
for _t in ('Schreibe 6√2 als eine einzige Wurzel.', 'Schreibe 10√2 als eine einzige Wurzel.', 'Ergänze die Lücke: √□ = 5√3.'):
    DS.stufe('teilweise', _t, 2)
# nenner_rational: 15/√5 ist die Stufe-1-Aufgabe; zwei der sechs Aufgaben „√m − n im Nenner“ auf Stufe 2 (Verfahren steht jetzt im Beispiel)
DS.stufe('nenner_rational', 'Mache den Nenner rational: 15/√5.', 1)
DS.stufe('nenner_rational', 'Mache den Nenner rational: 3/(√5 − 2).', 2)
DS.stufe('nenner_rational', 'Mache den Nenner rational: 9/(√7 − 2).', 2)

_NR_ZEILEN = [['vorher', '12', '√3'], ['erweitert', '12√3', '√3 · √3'], ['ausgerechnet', '12√3', '3'], ['gekürzt', '4√3', '1']]
DS_KARTEN = {
    'nenner_rational': {
        'schritte': [{'text': 'Erweitern mit √3: Zähler und Nenner mal √3.', 'bild': {'zeilen': _NR_ZEILEN[:2]}},
                     {'text': 'Unten gilt √3 · √3 = 3. Jetzt steht da 12√3/3.', 'bild': {'zeilen': _NR_ZEILEN[:3]}},
                     {'text': '12 : 3 = 4, also ⟦12/√3 = 4√3⟧. Unten steht keine Wurzel mehr.', 'bild': {'zeilen': _NR_ZEILEN}},
                     {'text': 'Bei 6/(√5 − 2) erweitere mit √5 + 2. Unten: 5 − 4 = 1.',
                      'bild': {'zeilen': [['vorher', '6', '√5 − 2'], ['mal (√5 + 2)', '6(√5 + 2)', '5 − 4 = 1'], ['Ergebnis', '6(√5 + 2)', '1']]}}],
    },
}

if __name__ == '__main__':
    durchsicht('zahlen.reell', DS, DS_KARTEN)


# ---- STUFEN (Zwanzigste Runde, Zweig stufen-kl9) ----
from _stufen_kl9 import Stufen, stufen  # noqa: E402

ST = Stufen('zahlen.reell', 20_9_2)
Z, A, L = ST.Z, ST.A, ST.L

# zahlarten
ST.stufenleiter('zahlarten', 'Eine einzelne Wurzel als rational oder irrational einordnen.',
                'Aus einer Liste die irrationale Zahl wählen, periodische Dezimalzahlen und negative Wurzeln einordnen.',
                'Aussagen über Zahlenmengen prüfen, Fehler bei periodischen Zahlen finden, zählen, wie viele Wurzeln rational sind, Produkte von Wurzeln einordnen.')
ST.typ('zahlarten', 'Ist √2 · √8', 'verknuepfen')
ST.typ('zahlarten', '/^(Zu welcher kleinsten Zahlenmenge gehört √|Ist √)/', 'erkennen')
ST.typ('zahlarten', 'Welche Zahl ist irrational?', 'erkennen', s=1)
ST.typ('zahlarten', 'Welche Zahl ist irrational?', 'mehrschritt', s=2)
ST.typ('zahlarten', 'Welche Zahl ist irrational?', 'verknuepfen', s=3)
ST.typ('zahlarten', '/^(Welche der Zahlen ist irrational|Zu welcher kleinsten Zahlenmenge gehört −)/', 'mehrschritt')
ST.typ('zahlarten', 'Ist 0,7', 'darstellung')
ST.typ('zahlarten', '/^(Ist 0,6|Welche Aussage)/', 'begruenden')
ST.typ('zahlarten', 'Jemand sagt', 'fehler')
ST.typ('zahlarten', 'Welche der Zahlen ist rational', 'verknuepfen')
ST.typ('zahlarten', 'Wie viele der 50 Zahlen', 'transfer')
ST.neu('zahlarten', 'direkt', L('Schreibe √0,25 als gekürzten Bruch.', '□/□', [1, 2], ['1', '2'],
       '√0,25 = 0,5 = 1/2. Weil sich die Wurzel als Bruch schreiben lässt, ist sie rational.', 'Erst die Wurzel als Dezimalzahl, dann als Bruch.'))
ST.neu('zahlarten', 'einkleidung', A('Ein quadratisches Beet hat 20 m² Fläche. Was gilt für seine Seitenlänge in Metern?', 'Sie ist irrational.', ['Sie ist rational, denn 20 ist eine natürliche Zahl.', 'Sie ist genau 4,5.', 'Sie ist genau 5.'],
       'Seite = √20. 20 liegt zwischen den Quadratzahlen 16 und 25, ist also keine Quadratzahl. √20 ≈ 4,47… ist irrational.', 'Ist 20 eine Quadratzahl?'))
ST.neu('zahlarten', 'umkehr', Z('Für welche natürliche Zahl n zwischen 40 und 50 ist √n rational?', 49, '7 ** 2',
       'Rational ist √n bei natürlichem n nur, wenn n eine Quadratzahl ist. Zwischen 40 und 50 liegt nur 49 = 7².', 'Welche Quadratzahl liegt zwischen 40 und 50?'))
ST.knobel('zahlarten', A('Kann die Summe von zwei irrationalen Zahlen rational sein?', 'Ja, zum Beispiel (5 + √2) + (5 − √2) = 10.',
          ['Nein, irrational plus irrational ist immer irrational.', 'Nur wenn beide Zahlen gleich sind.', 'Nein, außer eine der Zahlen ist 0.'],
          '5 + √2 und 5 − √2 sind beide irrational (√2 geht nie glatt auf). Addiert heben sich +√2 und −√2 auf: Es bleibt 10, eine rationale Zahl. Also kann die Summe rational sein.',
          'Probiere zwei Zahlen, in denen dieselbe Wurzel einmal mit Plus und einmal mit Minus steht.'))
ST.knobel('zahlarten', L('Die Zahl x = 0,121212… (der Block 12 wiederholt sich immer) ist rational. Schreibe sie als gekürzten Bruch.', '□/□', [4, 33], ['4', '33'],
          'Rechne 100 · x = 12,121212… Davon x = 0,121212… abziehen: 99 · x = 12. Also x = 12/99 = 4/33. Probe: 4 : 33 = 0,1212…',
          'Was passiert, wenn du x mit 100 malnimmst und dann x abziehst?'))

# eingrenzen
ST.stufenleiter('eingrenzen', 'Zehntel quadrieren und eine Wurzel auf Zehntel genau eingrenzen.',
                'Auf Hundertstel eingrenzen, Wurzel mit Dezimalzahl vergleichen, rückwärts passende Zahlen n finden.',
                'Zahlen zwischen zwei Wurzeln finden, Sachfragen mit Mindestmaß, Fehler „1,4 ist √2“, Bedingungen für eine Ziffer, mehrteilige Aufgabe.')
ST.typ('eingrenzen', 'Berechne', 'direkt')
ST.typ('eingrenzen', '/^(Zwischen welchen Zahlen mit|Welche Zahl ist größer)/', 'mehrschritt', s=2)
ST.typ('eingrenzen', 'Zwischen welchen Zahlen mit einer Nachkommastelle liegt √0,9', 'verknuepfen')
ST.typ('eingrenzen', '/^(Welche Zahl liegt zwischen|Wie viele ganze Zahlen)/', 'verknuepfen')
ST.typ('eingrenzen', '/^(Ein quadratischer Tisch|Ein Stein fällt)/', 'transfer')
ST.neu('eingrenzen', 'erkennen', A('Welche Rechnung zeigt, dass √30 größer als 5,4 ist?', '5,4² = 29,16 < 30', ['5,4 · 2 = 10,8 < 30', '30 : 5,4 ≈ 5,6', '5,4 + 5,4 = 10,8'],
       'Eine Zahl ist kleiner als √30, wenn ihr Quadrat kleiner als 30 ist. 5,4² = 29,16 < 30.', 'Vergleiche Quadrate.'))
ST.neu('eingrenzen', 'direkt', A('Es gilt 4,5² = 20,25. Was folgt daraus für √20?', '√20 ist kleiner als 4,5.', ['√20 ist größer als 4,5.', '√20 = 4,5.', 'Daraus folgt nichts.'],
       '20 < 20,25 = 4,5². Also ist √20 < 4,5.', 'Liegt 20 über oder unter 20,25?'))
ST.neu('eingrenzen', 'einkleidung', Z('Ein quadratischer Teppich soll höchstens 7 m² groß sein. Seine Seite soll ganze Dezimeter lang sein. Wie viele dm darf sie höchstens haben?', 26, '26',
       '2,6² = 6,76 ≤ 7, aber 2,7² = 7,29 > 7. Also höchstens 2,6 m = 26 dm.', 'Grenze √7 auf Zehntel ein.', einheit='dm'))
ST.neu('eingrenzen', 'umkehr', Z('Für welche natürliche Zahl n gilt 7,1 < √n < 7,2?', 51, '51',
       '7,1² = 50,41 und 7,2² = 51,84. Gesucht ist n mit 50,41 < n < 51,84: nur n = 51.', 'Quadriere die Grenzen.'))
ST.neu('eingrenzen', 'fehler', A('Jemand sagt: „1,4² = 1,96, also ist √2 = 1,4.“ Was stimmt?', 'Falsch: 1,96 ist nicht 2, also ist 1,4 nur eine Näherung (√2 liegt zwischen 1,41 und 1,42).',
       ['Richtig.', 'Falsch: √2 = 1,5.', 'Falsch: √2 = 1,96.'], '1,4² = 1,96 < 2 < 2,25 = 1,5². Genauer: 1,41² = 1,9881 und 1,42² = 2,0164. √2 ist irrational und hat keinen genauen Dezimalwert.',
       'Ist 1,96 genau 2?'))
ST.neu('eingrenzen', 'parameter', Z('Die zweistellige Zahl mit der Zehnerziffer z und der Einerziffer 0 heißt „z0“. Für welche Ziffer z liegt √(z0) zwischen 7 und 7,5?', 5, '50 // 10',
       '7² = 49 und 7,5² = 56,25. Die Zahl z0 muss zwischen 49 und 56,25 liegen. Von 10, 20, …, 90 passt nur 50, also z = 5.', 'Quadriere 7 und 7,5.'))
ST.neu('eingrenzen', 'pruefung', L('a) Zwischen welchen aufeinanderfolgenden ganzen Zahlen liegt √75? b) Grenze √75 auf Zehntel ein und gib die Grenzen in Zehnteln an (z. B. 8,1 als 81).',
       'a) □ bis □; b) □ bis □ Zehntel', [8, 9, 86, 87], ['8', '9', '86', '87'],
       'a) 64 < 75 < 81, also 8 < √75 < 9. b) 8,6² = 73,96 < 75 < 75,69 = 8,7², also 8,6 < √75 < 8,7.', 'In b) probiere 8,6 und 8,7.'))
ST.knobel('eingrenzen', Z('Die Wurzel aus einer natürlichen Zahl beginnt mit 3,1… Welche Zahl ist es?', 10, '10',
          '√n beginnt mit 3,1 heißt 3,1 ≤ √n < 3,2, also 3,1² = 9,61 ≤ n < 10,24 = 3,2². Die einzige natürliche Zahl dazwischen ist 10. Probe: √10 ≈ 3,16.',
          'Übersetze „beginnt mit 3,1“ in zwei Ungleichungen.'))
ST.knobel('eingrenzen', Z('Wie viele natürliche Zahlen n erfüllen 9,9 < √n < 10,1?', 4, '102 - 99 + 1',
          'Quadrieren: 9,9² = 98,01 < n < 102,01 = 10,1². Also n = 99, 100, 101, 102. Das sind 4 Zahlen.',
          'Quadriere die Grenzen.'))

# wurzel_mal
ST.stufenleiter('wurzel_mal', 'Zwei Wurzeln mit √a · √b = √(a · b) malnehmen und erkennen, wann die Regel passt.',
                'Wurzeln teilen, Rechenketten, Quadrate unter der Wurzel mit Betrag, Flächen von Rechtecken.',
                'Terme mit Variablen, Bedingung √(x²) = x, kleinstes n für eine natürliche Wurzel, Fehler √a · √b = √(a + b), Sachformeln.')
ST.typ('wurzel_mal', '/^Berechne √\\d+ · √\\d+\\.$/', 'direkt')
ST.typ('wurzel_mal', 'Ist √4 · √9', 'erkennen')
ST.typ('wurzel_mal', '/^Berechne √[\\d ]+ : √/', 'umkehr')
ST.typ('wurzel_mal', '/^(Berechne √\\d+ · √\\d+ − |Berechne √\\(\\(|Berechne √\\(x²\\)|Berechne ohne Taschenrechner)/', 'mehrschritt')
ST.typ('wurzel_mal', '/^Vereinfache √\\(\\d+[xa]\\) ·/', 'verknuepfen')
ST.typ('wurzel_mal', 'Vereinfache √(49a²)', 'begruenden')
ST.typ('wurzel_mal', '/^(Welche kleinste natürliche Zahl|Für welche Zahlen x)/', 'parameter')
ST.typ('wurzel_mal', 'Ein Rechteck ist √8', 'einkleidung')
ST.typ('wurzel_mal', 'Aus einer Bremsspur', 'transfer')
ST.neu('wurzel_mal', 'erkennen', A('Welcher Term ist gleich √(5 · 7)?', '√5 · √7', ['√5 + √7', '5 · √7', '√5 · 7'],
       'Die Regel √a · √b = √(a · b) gilt für a, b ≥ 0: √(5 · 7) = √5 · √7. Für Summen gibt es keine solche Regel.', 'Lies die Regel von rechts nach links.'))
ST.neu('wurzel_mal', 'einkleidung', Z('Ein Rechteck ist √5 cm breit und √20 cm lang. Wie groß ist sein Flächeninhalt?', 10, '100 // 10',
       'A = √5 · √20 = √100 = 10 cm².', 'Fläche = Breite · Länge, dann die Regel benutzen.', einheit='cm²'))
ST.neu('wurzel_mal', 'fehler', A('Jemand rechnet: √9 · √16 = √25 = 5. Was stimmt?', 'Falsch: Unter der Wurzel wird malgenommen: √(9 · 16) = √144 = 12.',
       ['Richtig.', 'Falsch: Das Ergebnis ist 25.', 'Falsch: Das Ergebnis ist 7.'], '√9 · √16 = 3 · 4 = 12 = √144. Addiert wird bei dieser Regel nicht.', 'Rechne zur Probe √9 und √16 einzeln aus.'))
ST.knobel('wurzel_mal', Z('Berechne √2 · √8 · √32 · √128.', 256, '2 ** 8',
          'Alles unter eine Wurzel: √(2 · 8 · 32 · 128). Das sind Zweierpotenzen: 2¹ · 2³ · 2⁵ · 2⁷ = 2¹⁶. √(2¹⁶) = 2⁸ = 256, denn 2⁸ · 2⁸ = 2¹⁶.',
          'Schreibe alle Zahlen als Zweierpotenzen.'))
ST.knobel('wurzel_mal', Z('Für wie viele natürliche Zahlen n von 1 bis 100 ist √(2n) · √8 eine natürliche Zahl?', 10, '100 // 10',
          '√(2n) · √8 = √(16n) = 4 · √n. Das ist genau dann natürlich, wenn √n natürlich ist, also n eine Quadratzahl. Quadratzahlen von 1 bis 100: 1, 4, …, 100 – zehn Stück.',
          'Fasse zuerst zu einer Wurzel zusammen und ziehe heraus, was geht.'))

# teilweise
ST.stufenleiter('teilweise', 'Die größte Quadratzahl im Radikanden finden und teilweise die Wurzel ziehen.',
                'Umgekehrt a√b als eine Wurzel schreiben, Seitenlängen exakt angeben, Produkte unter der Wurzel vereinfachen.',
                'Terme mit Variablen, Zahlen mit Wurzeln vergleichen, Fehler √50 = 25√2 finden, besondere Zahlen suchen, mehrteilige Aufgabe.')
ST.typ('teilweise', '/^Ziehe teilweise die Wurzel, so weit wie möglich: √\\d/', 'direkt')
ST.typ('teilweise', '/^(Schreibe \\d+√|Ergänze die Lücke)/', 'umkehr')
ST.typ('teilweise', '/^(Ein Quadrat hat den|Ein quadratischer Platz)/', 'einkleidung')
ST.typ('teilweise', '/^Ziehe teilweise die Wurzel, so weit wie möglich: √\\(/', 'verknuepfen')
ST.typ('teilweise', 'Welche Zahl ist am größten', 'begruenden')
ST.neu('teilweise', 'erkennen', A('Welche größte Quadratzahl steckt als Faktor in 48?', '16', ['4', '8', '24'],
       '48 = 16 · 3. 4 steckt auch drin, ist aber nicht die größte; 8 und 24 sind keine Quadratzahlen.', 'Teste 4, 9, 16, 25, …'))
ST.neu('teilweise', 'erkennen', A('Welcher Term ist schon so weit wie möglich vereinfacht?', '3√5', ['√20', '2√12', '√45'],
       '√20 = 2√5, 2√12 = 4√3 und √45 = 3√5 lassen sich noch vereinfachen. In 3√5 steckt unter der Wurzel keine Quadratzahl mehr.', 'Steckt unter der Wurzel noch eine Quadratzahl?'))
ST.neu('teilweise', 'mehrschritt', L('Vereinfache √(3 · 75 · 2).', '□√□', [15, 2], ['15', '2'],
       '3 · 75 · 2 = 450 = 225 · 2. Also √450 = 15√2.', 'Erst das Produkt, dann die größte Quadratzahl suchen.'))
ST.neu('teilweise', 'fehler', A('Jemand vereinfacht: √50 = 25√2. Was stimmt?', 'Falsch: √50 = √25 · √2 = 5√2.', ['Richtig.', 'Falsch: √50 = 2√25.', 'Falsch: √50 = 10√5.'],
       'Aus 25 wird die Wurzel gezogen: √25 = 5. Probe: (5√2)² = 25 · 2 = 50, aber (25√2)² = 1 250.', 'Mach die Probe durch Quadrieren.'))
ST.neu('teilweise', 'parameter', Z('Welche kleinste natürliche Zahl m > 1 ist keine Quadratzahl, aber bei √m kann man trotzdem teilweise die Wurzel ziehen?', 8, '4 * 2',
       '2, 3, 5, 6, 7 enthalten keine Quadratzahl größer als 1. 4 ist selbst Quadratzahl. 8 = 4 · 2: √8 = 2√2.', 'In m muss eine Quadratzahl größer als 1 als Faktor stecken.'))
ST.neu('teilweise', 'transfer', L('Ein Quadrat hat dreimal so viel Fläche wie ein Quadrat mit 4 cm Seitenlänge. Gib seine Seitenlänge exakt an.', '□√□ cm', [4, 3], ['4', '3'],
       'Fläche: 3 · 16 = 48 cm². Seite √48 = √(16 · 3) = 4√3 cm.', 'Erst die Fläche, dann die Wurzel teilweise ziehen.'))
ST.neu('teilweise', 'pruefung', L('Ein quadratisches Stück Stoff hat 288 cm² Fläche. a) Gib die Seitenlänge exakt an. b) Gib den Umfang exakt an.', 'a) □√□ cm; b) □√□ cm', [12, 2, 48, 2], ['12', '2', '4 * 12', '2'],
       'a) 288 = 144 · 2, also √288 = 12√2 cm. b) Umfang 4 · 12√2 = 48√2 cm.', 'Größte Quadratzahl in 288?'))
ST.knobel('teilweise', L('Vereinfache √(2 · 2 · 3 · 3 · 3 · 5 · 5 · 5 · 5).', '□√□', [150, 3], ['2 * 3 * 25', '3'],
          'Paare gleicher Faktoren kommen vor die Wurzel: 2 · 2 → 2, 3 · 3 → 3, 5 · 5 · 5 · 5 → 25. Übrig bleibt eine 3. Ergebnis: 2 · 3 · 25 · √3 = 150√3.',
          'Du musst das Produkt nicht ausrechnen. Was passiert mit Paaren?'))
ST.knobel('teilweise', Z('Bei wie vielen natürlichen Zahlen n von 2 bis 50 lässt sich √n weder ganz noch teilweise ziehen?', 30, '49 - 19',
          'Ziehen lässt sich etwas, wenn eine Quadratzahl 4, 9, 25 oder 49 als Faktor steckt. Vielfache von 4 bis 50: 12; von 9: 5; von 25: 2; von 49: 1; doppelt gezählt ist 36 (Vielfaches von 4 und 9): 12 + 5 + 2 + 1 − 1 = 19. Von den 49 Zahlen 2 bis 50 bleiben 49 − 19 = 30.',
          'Zähle lieber die Zahlen, bei denen es geht. Achtung, keine Zahl doppelt zählen.'))

# zusammenfassen
ST.stufenleiter('zusammenfassen', 'Vielfache derselben Wurzel addieren und subtrahieren, erkennen, wann es nicht geht.',
                'Erst teilweise die Wurzel ziehen, dann zusammenfassen; eine fehlende Wurzel ergänzen; Zaunlängen exakt.',
                'Binomische Formeln mit Wurzeln, Fehler √2 + √8 = √10, Aussagen prüfen, Bedingung für a, mehrteilige Aufgabe.')
ST.typ('zusammenfassen', '/^Fasse zusammen: \\d+√/', 'direkt')
ST.typ('zusammenfassen', 'Kann man √2 + √7', 'erkennen')
ST.typ('zusammenfassen', '/^Fasse zusammen: √/', 'mehrschritt')
ST.typ('zusammenfassen', '/^Berechne \\(√6|^Multipliziere aus und vereinfache/', 'mehrschritt')
ST.typ('zusammenfassen', 'Zwei quadratische Beete', 'einkleidung')
ST.typ('zusammenfassen', '/^(Berechne \\(\\d+ \\+ √|Multipliziere aus und fasse)/', 'verknuepfen')
ST.typ('zusammenfassen', 'Berechne geschickt', 'transfer')
ST.neu('zusammenfassen', 'umkehr', Z('Ergänze die Lücke: √□ + √12 = 5√3.', 27, '9 * 3',
       '√12 = 2√3. Es fehlen 5√3 − 2√3 = 3√3 = √(9 · 3) = √27.', 'Schreibe √12 als Vielfaches von √3.'))
ST.neu('zusammenfassen', 'fehler', A('Jemand rechnet: √2 + √8 = √10. Was stimmt?', 'Falsch: √8 = 2√2, also √2 + √8 = 3√2.', ['Richtig.', 'Falsch: √2 + √8 = 4.', 'Falsch: √2 + √8 = √16.'],
       'Wurzeln darf man nicht einfach addieren. √8 = 2√2, also √2 + 2√2 = 3√2 ≈ 4,24, aber √10 ≈ 3,16.', 'Ziehe bei √8 teilweise die Wurzel.'))
ST.neu('zusammenfassen', 'begruenden', A('Stimmt für alle Zahlen a > 0 und b > 0: √a + √b ist größer als √(a + b)?', 'Ja: (√a + √b)² = a + b + 2√a√b ist größer als a + b.',
       ['Nein, beide sind immer gleich.', 'Nein, √(a + b) ist immer größer.', 'Nur wenn a = b.'],
       'Beide Seiten sind positiv. Quadriert: (√a + √b)² = a + 2√(ab) + b > a + b. Beispiel: √9 + √16 = 7 > 5 = √25.', 'Vergleiche die Quadrate beider Seiten.'))
ST.neu('zusammenfassen', 'parameter', Z('Für welche Zahl a gilt √a + √12 = 3√3?', 3, '3',
       '√12 = 2√3. Dann muss √a = 3√3 − 2√3 = √3 sein, also a = 3.', 'Schreibe √12 als Vielfaches von √3.'))
ST.neu('zusammenfassen', 'pruefung', L('Ein Rechteck hat die Seiten √50 cm und √8 cm. a) Gib den Umfang exakt an. b) Berechne den Flächeninhalt.', 'a) □√□ cm; b) □ cm²', [14, 2, 20], ['2 * (5 + 2)', '2', '5 * 2 * 2'],
       'a) √50 = 5√2, √8 = 2√2. Umfang 2 · (5√2 + 2√2) = 14√2 cm. b) √50 · √8 = √400 = 20 cm².', 'Erst teilweise die Wurzeln ziehen.'))
ST.knobel('zusammenfassen', A('Welche Zahl ist √(3 + 2√2)?', '1 + √2', ['√5', '3 + √2', '√3 + √2'],
          'Probiere ein Quadrat: (1 + √2)² = 1 + 2√2 + 2 = 3 + 2√2. Weil 1 + √2 positiv ist, gilt √(3 + 2√2) = 1 + √2. Die anderen: (√3 + √2)² = 5 + 2√6, (3 + √2)² = 11 + 6√2.',
          'Der Term unter der Wurzel sieht aus wie ein ausmultipliziertes Quadrat.'))
ST.knobel('zusammenfassen', Z('Berechne (√2 + √3)² + (√2 − √3)².', 10, '2 * (2 + 3)',
          'Ausmultiplizieren: (√2 + √3)² = 2 + 2√6 + 3 und (√2 − √3)² = 2 − 2√6 + 3. Die Terme mit √6 heben sich auf: 5 + 5 = 10.',
          'Schreib beide Quadrate aus, ohne sie auszurechnen. Was fällt weg?'))

# nenner_rational
ST.stufenleiter('nenner_rational', 'Bei a/√b mit √b erweitern und kürzen.',
                'Nenner wie 4√7 oder √m − n, Brüche aus zwei Wurzeln, rückwärts zum alten Bruch.',
                'Summen mit zwei Wurzeln im Nenner, Fehler „nur den Nenner malnehmen“, Vergleich mit Dezimalzahl, Bedingung für a, mehrteilige Aufgabe.')
ST.typ('nenner_rational', '/^Mache den Nenner rational: \\d+\\/√\\d+\\.$/', 'direkt')
ST.typ('nenner_rational', '/^Mache den Nenner rational: \\d+\\/\\(\\d+√/', 'mehrschritt')
ST.typ('nenner_rational', '/^Mache den Nenner rational: \\d+\\/\\(√\\d+ − \\d+\\)/', 'mehrschritt')
ST.typ('nenner_rational', 'Mache den Nenner rational und vereinfache', 'mehrschritt')
ST.typ('nenner_rational', 'Ein Rechteck hat 6 m²', 'einkleidung')
ST.typ('nenner_rational', 'Ein Schüler sagt', 'fehler')
ST.typ('nenner_rational', '/^(Mache den Nenner rational: \\d+\\/\\(√\\d+ \\+|Berechne 1\\/|Mache den Nenner rational: \\d+\\/\\(\\d+ \\+)/', 'verknuepfen')
ST.neu('nenner_rational', 'erkennen', A('Womit erweiterst du 5/√2, damit im Nenner keine Wurzel mehr steht?', 'mit √2', ['mit 2', 'mit 5', 'mit √5'],
       '√2 · √2 = 2. Also 5/√2 = 5√2/2.', 'Was ergibt √2 · √2?'))
ST.neu('nenner_rational', 'direkt', L('Schreibe 10/√5 ohne Wurzel im Nenner.', '□√□', [2, 5], ['2', '5'],
       '10/√5 = 10√5/5 = 2√5.', 'Erweitere mit √5 und kürze.'))
ST.neu('nenner_rational', 'umkehr', Z('Der Bruch 2/√a (a natürliche Zahl) wird mit √a erweitert, damit im Nenner keine Wurzel mehr steht. Heraus kommt 2√5/5. Wie groß ist a?', 5, '5',
       'Erweitern mit √a: 2/√a = 2√a/(√a · √a) = 2√a/a. Vergleich mit 2√5/5: a = 5. Der Bruch war 2/√5.', 'Mach das Erweitern rückgängig.'))
ST.neu('nenner_rational', 'begruenden', A('Welche Zahl ist größer: 1/√2 oder 0,7?', '1/√2', ['0,7', 'Beide sind gleich.', 'Das lässt sich nicht entscheiden.'],
       '1/√2 = √2/2. Wegen 1,4² = 1,96 < 2 ist √2 > 1,4, also √2/2 > 0,7.', 'Mache den Nenner rational und schätze √2.'))
ST.neu('nenner_rational', 'parameter', Z('Für welche natürliche Zahl a gilt 6/√a = 2√3?', 3, '36 // 12',
       '6/√a = 2√3 heißt √a = 6/(2√3) = 3/√3 = √3. Also a = 3. Probe: 6/√3 = 6√3/3 = 2√3.', 'Löse nach √a auf.'))
ST.neu('nenner_rational', 'rueckwaerts', Z('Nach dem Rationalmachen von 6/(□ − √3) steht da 3 + √3. Welche Zahl gehört in das Kästchen?', 3, '(6 + 6) // 4',
       'Mit □ = 3: 6/(3 − √3) · (3 + √3)/(3 + √3) = 6(3 + √3)/(9 − 3) = 3 + √3. Rückwärts: Aus 6/(□ − √3) = 3 + √3 folgt □ − √3 = 6/(3 + √3) = 6(3 − √3)/(9 − 3) = 3 − √3, also □ = 3.',
       'Was ergibt (□ − √3)(□ + √3)?'))
ST.neu('nenner_rational', 'pruefung', L('Gegeben ist 8/(√5 + 1). a) Womit erweiterst du? b) Gib das Ergebnis an.', 'a) √5 − □; b) □√5 − □', [1, 2, 2], ['1', '8 // 4', '8 // 4'],
       'a) Mit √5 − 1, dann steht unten (√5 + 1)(√5 − 1) = 5 − 1 = 4. b) 8(√5 − 1)/4 = 2√5 − 2.', 'Dritte binomische Formel im Nenner.'))
ST.knobel('nenner_rational', Z('Berechne 1/(1 + √2) + 1/(√2 + √3) + 1/(√3 + 2).', 1, '2 - 1',
          'Jeden Nenner rational machen: 1/(1 + √2) = √2 − 1, 1/(√2 + √3) = √3 − √2, 1/(√3 + 2) = 2 − √3 (die Nenner werden jeweils 1). Summe: √2 − 1 + √3 − √2 + 2 − √3 = 2 − 1 = 1.',
          'Mache jeden Bruch einzeln rational und schau, was übrig bleibt.'))
ST.knobel('nenner_rational', Z('Berechne (√3 + √2)/(√3 − √2) + (√3 − √2)/(√3 + √2).', 10, '(5 + 5) // 1',
          'Gemeinsamer Nenner (√3 − √2)(√3 + √2) = 3 − 2 = 1. Zähler: (√3 + √2)² + (√3 − √2)² = (5 + 2√6) + (5 − 2√6) = 10. Ergebnis 10.',
          'Bring beide Brüche auf einen gemeinsamen Nenner.'))

# heron
ST.stufenleiter('heron', 'Einen Heron-Schritt ausführen: a : x und den Mittelwert bilden.',
                'Zwei Schritte nacheinander, Tabellen lesen, aus einem Ergebnis die Zahl a zurückgewinnen.',
                'Aus einem Schritt rückwärts schließen, Fehler im Verfahren finden, begründen, warum es funktioniert, Startwerte deuten, mehrteilige Aufgabe.')
ST.typ('heron', '/^(Heron-Verfahren für √7|Berechne für √\\d+ mit dem Startwert)/', 'direkt')
ST.typ('heron', 'Welcher Startwert liegt am nächsten', 'erkennen')
ST.typ('heron', '/^(Berechne für √5 mit dem Startwert 2 zwei|Bestimme √17)/', 'mehrschritt')
ST.typ('heron', '/^Die Tabelle zeigt/', 'darstellung')
ST.typ('heron', 'Ein quadratisches Fenster', 'einkleidung')
ST.typ('heron', 'Jemand rechnet einen Heron-Schritt mit dem Startwert 3', 'rueckwaerts')
ST.typ('heron', 'Warum liegt', 'begruenden')
ST.typ('heron', '/^(Jemand bestimmt √100|Ein quadratischer Platz)/', 'transfer')
ST.typ('heron', 'Jemand rechnet für √8', 'fehler')
ST.typ('heron', 'Nach wie vielen Heron-Schritten', 'verknuepfen')
ST.neu('heron', 'erkennen', A('Was rechnet man in jedem Schritt des Heron-Verfahrens für √a?', 'den Mittelwert aus x und a : x', ['x · x', 'a : 2', 'den Mittelwert aus x und a'],
       'x und a : x sind die Seiten eines Rechtecks mit Fläche a. Ihr Mittelwert ist die neue, bessere Seite.', 'Denk an das Rechteck mit der Fläche a.'))
ST.neu('heron', 'umkehr', Z('Ein Heron-Schritt mit dem Startwert 5 liefert x₁ = 5,1. Aus welcher Zahl a sollte die Wurzel bestimmt werden?', 26, '(5.1 * 2 - 5) * 5',
       '(5 + a : 5) : 2 = 5,1 ⇒ 5 + a : 5 = 10,2 ⇒ a : 5 = 5,2 ⇒ a = 26.', 'Rechne den Mittelwert rückwärts.'))
ST.neu('heron', 'mehrschritt', L('Heron-Verfahren für √2 mit dem Startwert 1: Rechne zwei Schritte und gib x₂ als Bruch an.', '□/□', [17, 12], ['17', '12'],
       'x₁ = (1 + 2 : 1) : 2 = 3/2. x₂ = (3/2 + 2 : (3/2)) : 2 = (3/2 + 4/3) : 2 = (17/6) : 2 = 17/12.', 'Rechne mit Brüchen, nicht gerundet.'))
ST.neu('heron', 'parameter', Z('Jemand nimmt bei √a als Startwert x₀ = a. Für welches a liefert der erste Heron-Schritt x₁ = 5?', 9, '5 * 2 - 1',
       'x₁ = (a + a : a) : 2 = (a + 1) : 2 = 5 ⇒ a = 9. (Dann ist √9 = 3, x₁ = 5 ist also noch weit weg.)', 'Was ist a : a?'))
ST.neu('heron', 'pruefung', L('Heron-Verfahren für √60 mit dem Startwert 8. a) Wie lang ist die andere Rechteckseite 60 : 8? b) Wie groß ist x₁?', 'a) □,□; b) □,□', [7, 5, 7, 75], ['60 // 8', '(600 // 8) % 10', '(8 * 8 + 60) // 16', '(8 * 8 + 60) * 100 // 16 % 100'],
       'a) 60 : 8 = 7,5. b) x₁ = (8 + 7,5) : 2 = 7,75. Probe: 7,75² ≈ 60,06.', 'Erst teilen, dann den Mittelwert.'))
ST.knobel('heron', L('Heron für √2 mit dem Startwert 1 liefert 3/2, dann 17/12. Welcher Bruch kommt als nächster (x₃)?', '□/□', [577, 408], ['577', '408'],
          'x₃ = (17/12 + 2 : (17/12)) : 2 = (17/12 + 24/17) : 2. Gemeinsamer Nenner 204: 17/12 = 289/204, 24/17 = 288/204. Summe 577/204, halbiert 577/408. Probe: 577/408 ≈ 1,414216, √2 ≈ 1,414214.',
          'Ein gemeinsamer Nenner hilft; 12 · 17 = 204.'))
ST.knobel('heron', A('Ist der Wert x₁ nach einem Heron-Schritt immer mindestens so groß wie √a (bei positivem Startwert)?', 'Ja: Der Mittelwert von x und a : x ist nie kleiner als √a.',
          ['Nein, nur wenn der Startwert zu groß war.', 'Nein, x₁ ist immer kleiner als √a.', 'Das hängt von a ab.'],
          'Mit y = a : x gilt x · y = a. Es ist (x − y)² ≥ 0, also x² + y² ≥ 2xy. Auf beiden Seiten 2xy addieren: (x + y)² ≥ 4xy = 4a. Beide Seiten sind positiv, Wurzel ziehen: x + y ≥ 2√a, also (x + y) : 2 ≥ √a. Ab dem ersten Schritt nähert sich das Verfahren also von oben.',
          'Nenne die zweite Seite y. Was weißt du über (x − y)²?'))

if __name__ == '__main__':
    stufen('zahlen.reell', ST)

# ---- LK (22.11., LK-D 4, siehe _lk_etappen_2211.py): zuletzt, hängt nur an ----
if __name__ == '__main__':
    from _lk_etappen_2211 import lk_anhaengen
    lk_anhaengen('zahlen.reell')
# ---- LK ENDE ----
