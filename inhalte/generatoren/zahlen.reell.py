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

if __name__ == '__main__':
    bauen('zahlen.reell',
          'Irrationale Zahlen erkennen, Wurzeln eingrenzen, Wurzelterme vereinfachen und Nenner rational machen.',
          ['ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ. Irrational: unendlich, nicht periodisch (z. B. √2).', '√a · √b = √(ab), √a : √b = √(a : b) – aber nicht für Summen.',
           'Teilweise radizieren: √(k²m) = k√m.', 'Wurzel im Nenner: erweitern (bei √m ± n mit der 3. binomischen Formel).'],
          [('Reelle Zahlen', ['zahlarten', 'eingrenzen']), ('Rechnen mit Wurzeln', ['wurzel_mal', 'teilweise', 'zusammenfassen']),
           ('Nenner rational machen', ['nenner_rational'])],
          ETAPPEN, GEN,
          meiden={'zahlarten': ['√50?'], 'eingrenzen': ['√30?'], 'wurzel_mal': ['√3 · √27.'], 'teilweise': ['√72.'],
                  'zusammenfassen': ['√18 + √50.'], 'nenner_rational': ['12/√3.']},
          offen=['Lückentext „□√□“: Die App zeigt das Wurzelzeichen nur als Text in der Schablone; bitte prüfen, ob die Darstellung im Eingabefeld gut lesbar ist.'])
