#!/usr/bin/env python3
"""Thema abbildungen.aehnlichkeit – Ähnlichkeit und Strahlensätze (Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(909)
FIG = ('Zwei Strahlen mit gemeinsamem Anfangspunkt S werden von zwei parallelen Geraden geschnitten: '
       'die erste Parallele schneidet in A und B, die zweite in A\' und B\' (A, A\' auf dem einen, B, B\' auf dem anderen Strahl; A liegt näher an S).')


import math  # noqa: E402

KURZ = 'Es gilt AB ∥ A\'B\'.'


def sfig(sa, sa2, sb, sb2, lab, x=False, winkel=None):
    """Strahlensatzfigur. lab: {'SA': '3', 'AA': '?', 'SB': .., 'BB': .., 'AB': .., 'AB2': ..}. x=True: X-Figur."""
    th = math.radians(winkel or R.choice([30, 35, 40, 45]))
    c, s_ = math.cos(th), math.sin(th)
    v = -1 if x else 1
    P = {'S': [0, 0], 'A': [round(float(sa), 3), 0], "A'": [round(v * float(sa2), 3), 0],
         'B': [round(float(sb) * c, 3), round(float(sb) * s_, 3)], "B'": [round(v * float(sb2) * c, 3), round(v * float(sb2) * s_, 3)]}
    L = []
    if x:
        L += [['A', 'S', lab.get('SA', '')], ['S', "A'", lab.get('SA2', '')], ['B', 'S', lab.get('SB', '')], ['S', "B'", lab.get('SB2', '')]]
    else:
        L += [['S', 'A', lab.get('SA', '')], ['A', "A'", lab.get('AA', '')], ['S', 'B', lab.get('SB', '')], ['B', "B'", lab.get('BB', '')]]
    L += [['A', 'B', lab.get('AB', '')], ["A'", "B'", lab.get('AB2', '')]]
    return {'typ': 'figur', 'punkte': P, 'linien': L}


def kos(punkte, strecken=None, x=(-6, 8), y=(-6, 8)):
    g = {'typ': 'koordinaten', 'x': list(x), 'y': list(y), 'punkte': punkte}
    if strecken: g['strecken'] = strecken
    return g


def dec(lo, hi, nd=1):
    """zufällige Dezimalzahl mit nd Nachkommastellen"""
    f = 10 ** nd
    return Fr(R.randint(int(lo * f), int(hi * f)), f)


def ok(*xs):
    return all(endlich(x) and Fr(x).denominator in (1, 2, 4, 5, 10, 20, 25, 50, 100) for x in xs)


def cf(x):
    return str(float(x)) if Fr(x).denominator != 1 else str(int(x))


ETAPPEN = [
    {'lernziel': 'streckung', 'titel': 'Zentrische Streckung',
     'regel': 'Bei einer zentrischen Streckung mit Zentrum Z und ⟦Streckfaktor k⟧ gilt ⟦ZP\' = |k| · ZP⟧; alle Strecken werden mit |k| multipliziert. Bei k < 0 liegt P\' auf der ⟦anderen Seite⟧ von Z.',
     'schritte': ['Z(1 | 2), P(4 | 3), k = 2: Vektor von Z nach P ist (3 | 1).', 'Verdoppeln: (6 | 2), also P\' = (1 + 6 | 2 + 2) = ⟦P\'(7 | 4)⟧.'],
     'probe': 'P\' liegt auf dem Strahl ZP, doppelt so weit von Z entfernt ✓',
     'bild': {'typ': 'koordinaten', 'x': [0, 9], 'y': [0, 7], 'punkte': [{'x': 1, 'y': 2, 'name': 'Z'}, {'x': 4, 'y': 3, 'name': 'P'}, {'x': 7, 'y': 4, 'name': "P'"}, {'x': 8, 'y': 6, 'name': '2 · P (falsch)', 'offen': True}], 'strecken': [[1, 2, 7, 4]]},
     'fehler': 'P\' = 2 · P = (8 | 6) ist falsch, wenn Z nicht der Ursprung ist: Man streckt den ⟦Abstand von Z⟧, nicht die Koordinaten von P.'},
    {'lernziel': 'aehnlich', 'titel': 'Ähnliche Figuren',
     'regel': 'Zwei Figuren sind ⟦ähnlich⟧, wenn entsprechende Winkel gleich sind und ⟦alle Seiten im gleichen Verhältnis k⟧ stehen. Für Dreiecke genügen zwei gleiche Winkel.',
     'schritte': ['Dreieck 1: 4 cm, 6 cm, 7 cm. Dreieck 2 ist ähnlich, die kürzeste Seite misst 10 cm: k = 10 : 4 = 2,5.', 'Die anderen Seiten: 6 · 2,5 = ⟦15 cm⟧ und 7 · 2,5 = ⟦17,5 cm⟧.'],
     'probe': '15 : 6 = 2,5 ✓',
     'fehler': 'Zu jeder Seite 6 cm zu addieren (4 → 10, 6 → 12) ist falsch: Bei Ähnlichkeit wird ⟦multipliziert⟧, nicht addiert.'},
    {'lernziel': 'strahlensatz1', 'titel': '1. Strahlensatz (Abschnitte)',
     'regel': 'Werden zwei Strahlen von Parallelen geschnitten, stehen die ⟦Abschnitte auf einem Strahl⟧ im gleichen Verhältnis wie die entsprechenden auf dem anderen: ⟦SA : SA\' = SB : SB\'⟧.',
     'schritte': ['SA = 3 cm, SA\' = 7,5 cm, SB = 4 cm. Gesucht SB\'.', 'SB\' : 4 = 7,5 : 3 = 2,5 ⇒ ⟦SB\' = 10 cm⟧.'],
     'probe': '10 : 4 = 2,5 = 7,5 : 3 ✓',
     'bild': {'typ': 'figur', 'punkte': {'S': [0, 0], 'A': [3, 0], "A'": [7.5, 0], 'B': [3.277, 2.294], "B'": [8.192, 5.736]}, 'linien': [['S', 'A', '3'], ['A', "A'", '4,5'], ['S', 'B', '4'], ['B', "B'", '?'], ['A', 'B', ''], ["A'", "B'", '']]},
     'fehler': 'SB\' = SB + (SA\' − SA) = 8,5 cm ist falsch: Die Strecken stehen im gleichen ⟦Verhältnis⟧, nicht im gleichen Abstand.'},
    {'lernziel': 'strahlensatz2', 'titel': '2. Strahlensatz (Parallelen)',
     'regel': 'Die ⟦Parallelstrecken⟧ verhalten sich wie die zugehörigen Abschnitte ⟦ab S⟧: ⟦AB : A\'B\' = SA : SA\'⟧. Nicht mit dem Stück AA\' zwischen den Parallelen rechnen!',
     'schritte': ['SA = 5 cm, AA\' = 3 cm, AB = 4 cm. Gesucht A\'B\'. SA\' = 5 + 3 = 8 cm.', 'A\'B\' : 4 = 8 : 5 ⇒ A\'B\' = 4 · 1,6 = ⟦6,4 cm⟧.'],
     'probe': '6,4 : 4 = 1,6 = 8 : 5 ✓',
     'bild': {'typ': 'figur', 'punkte': {'S': [0, 0], 'A': [5, 0], "A'": [8, 0], 'B': [4.305, 3.939], "B'": [6.889, 6.303]}, 'linien': [['S', 'A', '5'], ['A', "A'", '3'], ['S', 'B', ''], ['B', "B'", ''], ['A', 'B', '4'], ["A'", "B'", '?']]},
     'fehler': 'A\'B\' : AB = AA\' : SA zu rechnen ist falsch: Beim 2. Strahlensatz braucht man Strecken ⟦ab S⟧, also SA\' = SA + AA\'.'},
    {'lernziel': 'flaeche_volumen', 'titel': 'Wirkung auf Fläche und Volumen',
     'regel': 'Werden alle Längen mit k multipliziert, wird der ⟦Flächeninhalt mit k²⟧ und das ⟦Volumen mit k³⟧ multipliziert. Im Bild: Verdoppelst du die Seite eines Quadrats, passen ⟦4 = 2²⟧ alte Quadrate hinein. Bei einem Würfel passen 8 = 2³ alte Würfel in den doppelt so großen.',
     'bild': {'typ': 'figur', 'punkte': {'_a': [0, 0], '_b': [1, 0], '_c': [2, 0], '_d': [2, 1], '_e': [2, 2], '_f': [1, 2], '_g': [0, 2], '_h': [0, 1], '_m': [1, 1]}, 'flaeche': ['_a', '_b', '_m', '_h'], 'linien': [['_a', '_c', '2 · Seite'], ['_c', '_e'], ['_e', '_g'], ['_g', '_a'], ['_b', '_f'], ['_h', '_d']]},
     'schritte': ['Ein Modell im Maßstab 1 : 20: k = 20. Das Modell hat 300 cm² Bodenfläche.', 'Original: 300 · 20² = 300 · 400 = ⟦120 000 cm²⟧ = 12 m².'],
     'probe': '1 m² = 10 000 cm² ✓',
     'fehler': 'Bei doppelter Seitenlänge auch die doppelte Fläche anzunehmen ist falsch: Die Fläche wächst mit ⟦k² = 4⟧, das Volumen mit k³ = 8.'},
    {'lernziel': 'anwendung', 'titel': 'Strahlensätze anwenden',
     'regel': 'Skizze anfertigen, ⟦Scheitel S und Parallelen⟧ erkennen, Gleichung aufstellen. Steht die Unbekannte in einer Summe, entsteht eine ⟦Bruchgleichung⟧: mit den Nennern multiplizieren.',
     'schritte': ['Ein 2 m hoher Stab wirft 3 m Schatten, ein Baum zur gleichen Zeit 18 m. Strahlen: Sonnenstrahl und Boden, S = Schattenende.', 'h : 2 = 18 : 3 ⇒ h = 2 · 6 = ⟦12 m⟧.'],
     'probe': '12 : 18 = 2 : 3 ✓',
     'bild': {'typ': 'figur', 'punkte': {'S': [0, 0], '_F1': [3, 0], '_T1': [3, 2], '_F2': [18, 0], '_T2': [18, 12]}, 'linien': [['S', '_F1', '3 m'], ['_F1', '_F2'], ['_F1', '_T1', '2 m'], ['_F2', '_T2', 'h = ?'], ['S', '_T2', '', 'gestrichelt']], 'rechter_winkel': [['_F2', 'S', '_T2'], ['_F1', 'S', '_T1']]},
     'fehler': 'h : 18 = 3 : 2 ist falsch zugeordnet: ⟦Höhe zu Höhe⟧ und ⟦Schatten zu Schatten⟧ (oder Höhe zu Schatten auf beiden Seiten gleich).'},
]

# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'streckung': {
  'einstieg': 'Beim Schattenspiel hält man eine Figur vor eine Lampe. An der Wand erscheint ein größerer Schatten. Jeder Punkt des Schattens liegt auf einem Lichtstrahl von der Lampe aus, nur weiter entfernt. Ist er überall doppelt so weit weg, ist der Schatten doppelt so groß. Diese Abbildung heißt ⟦zentrische Streckung⟧.',
  'woerter': [['Zentrum Z', 'der feste Punkt, von dem aus gestreckt wird – hier die Lampe'],
              ['Streckfaktor k', 'wie oft so weit vom Zentrum weg der Bildpunkt liegt'],
              ["P'", '„P Strich“: der Bildpunkt von P'],
              ['ZP', 'die Strecke von Z nach P bzw. ihre Länge'],
              ['|k|', 'k ohne Vorzeichen'],
              ['Vektor (3 | 1)', 'der Weg von Z nach P: 3 nach rechts, 1 nach oben']],
  'bild': {'typ': 'koordinaten', 'x': [0, 9], 'y': [0, 7], 'punkte': [{'x': 1, 'y': 2, 'name': 'Zentrum Z'}, {'x': 4, 'y': 3, 'name': 'Original P'}, {'x': 7, 'y': 4, 'name': "Bild P'"}, {'x': 8, 'y': 6, 'name': '2 · P (falsch)', 'offen': True}], 'strecken': [[1, 2, 7, 4]]},
  'schritte': ['Gegeben: Zentrum Z(1 | 2), Punkt P(4 | 3) und Streckfaktor k = 2.',
               'Den Weg von Z nach P bestimmen: 4 − 1 = 3 nach rechts, 3 − 2 = 1 nach oben, also (3 | 1).',
               'Diesen Weg mit k = 2 malnehmen: (6 | 2).',
               "Von Z aus diesen Weg gehen: P' = (1 + 6 | 2 + 2) = ⟦P'(7 | 4)⟧."],
  'regel': "So streckst du von einem ⟦Zentrum Z⟧ aus: Der Bildpunkt P' liegt auf dem Strahl von Z durch P, und es gilt ⟦ZP' = |k| · ZP⟧. Alle Strecken werden mit |k| malgenommen. Bei k < 0 liegt P' auf der ⟦anderen Seite⟧ von Z.",
  'fehler': "P' = 2 · P = (8 | 6) ist falsch, wenn Z nicht der Ursprung ist: Man streckt den ⟦Abstand von Z⟧, nicht die Koordinaten von P. Der Schatten hängt davon ab, wo die Lampe steht."},
 'aehnlich': {
  'einstieg': 'Ein Foto wird vergrößert. Damit niemand verzerrt aussieht, müssen Breite und Höhe mit derselben Zahl malgenommen werden, und alle Winkel bleiben gleich. Zwei Figuren, die so zusammenhängen, heißen ⟦ähnlich⟧.',
  'woerter': [['ähnlich', 'gleiche Form, eventuell andere Größe: gleiche Winkel, Seiten im gleichen Verhältnis'],
              ['entsprechende Seiten', 'Seiten, die in beiden Figuren an der gleichen Stelle liegen'],
              ['Verhältnis k', 'die Zahl, mit der jede Seite malgenommen wird'],
              ['10 : 4', '10 geteilt durch 4']],
  'schritte': ['Dreieck 1 hat die Seiten 4 cm, 6 cm und 7 cm. Im ähnlichen Dreieck 2 misst die kürzeste Seite 10 cm.',
               'Die kürzesten Seiten entsprechen sich. Der Faktor ist k = 10 : 4 = 2,5.',
               'Jede andere Seite wird mit 2,5 malgenommen: 6 · 2,5 = ⟦15 cm⟧.',
               'Ebenso 7 · 2,5 = ⟦17,5 cm⟧.'],
  'regel': 'So prüfst du ⟦Ähnlichkeit⟧: Entsprechende Winkel müssen gleich sein und ⟦alle Seiten im gleichen Verhältnis k⟧ stehen. Bei Dreiecken genügen zwei gleiche Winkel.',
  'fehler': 'Zu jeder Seite 6 cm zu addieren (4 → 10, 6 → 12) ist falsch: Das Foto wäre verzerrt. Bei Ähnlichkeit wird ⟦multipliziert⟧, nicht addiert.'},
 'strahlensatz1': {
  'einstieg': 'Zwei Lichtstrahlen gehen von der Lampe S aus. Eine kleine und eine große Figur stehen parallel zueinander und werden von beiden Strahlen getroffen. Wird der Weg auf dem einen Strahl 2,5-mal so lang, dann auch auf dem anderen. Diese Regel heißt ⟦1. Strahlensatz⟧.',
  'woerter': [['Scheitel S', 'der Punkt, von dem beide Strahlen ausgehen'],
              ['Strahl', 'eine Linie, die in S beginnt und in eine Richtung weitergeht'],
              ['parallel', 'überall gleich weit voneinander entfernt, sie schneiden sich nie'],
              ["SA : SA'", "die Länge SA geteilt durch die Länge SA'"],
              ['Abschnitt', 'ein Stück eines Strahls']],
  'bild': {'typ': 'figur', 'punkte': {'S': [0, 0], 'A': [3, 0], "A'": [7.5, 0], 'B': [3.277, 2.294], "B'": [8.192, 5.736]}, 'linien': [['S', 'A', 'SA = 3'], ['A', "A'", "AA' = 4,5"], ['S', 'B', 'SB = 4'], ['B', "B'", '?'], ['A', 'B', ''], ["A'", "B'", '']]},
  'schritte': ["Gegeben: SA = 3 cm, SA' = 7,5 cm und SB = 4 cm. Gesucht ist SB'.",
               "Auf dem ersten Strahl: SA' : SA = 7,5 : 3 = 2,5. Der Weg ab S ist 2,5-mal so lang.",
               "Auf dem zweiten Strahl gilt derselbe Faktor: SB' = 4 · 2,5.",
               "Also ⟦SB' = 10 cm⟧. Das Stück BB' ist 10 − 4 = 6 cm lang."],
  'regel': "So nutzt du den ⟦1. Strahlensatz⟧: Werden zwei Strahlen von Parallelen geschnitten, stehen die ⟦Abschnitte auf einem Strahl⟧ im gleichen Verhältnis wie die entsprechenden auf dem anderen: ⟦SA : SA' = SB : SB'⟧.",
  'fehler': "SB' = SB + (SA' − SA) = 8,5 cm ist falsch: Die Strecken stehen im gleichen ⟦Verhältnis⟧, nicht im gleichen Abstand. Man muss malnehmen, nicht dazuzählen."},
 'strahlensatz2': {
  'einstieg': 'Jetzt geht es um die Figuren selbst: Wie groß ist der Schatten an der Wand? Die Figur und ihr Schatten sind die parallelen Strecken zwischen den Strahlen. Sie wachsen im gleichen Verhältnis wie der Abstand zur Lampe. Diese Regel heißt ⟦2. Strahlensatz⟧.',
  'woerter': [['Parallelstrecken', "die Strecken AB und A'B', die parallel liegen"],
              ["SA' = SA + AA'", "die ganze Strecke ab S bis A'"],
              ["AA'", 'das Stück zwischen den beiden Parallelen']],
  'bild': {'typ': 'figur', 'punkte': {'S': [0, 0], 'A': [5, 0], "A'": [8, 0], 'B': [4.305, 3.939], "B'": [6.889, 6.303]}, 'linien': [['S', 'A', 'SA = 5'], ['A', "A'", "AA' = 3"], ['S', 'B', ''], ['B', "B'", ''], ['A', 'B', 'Figur AB = 4'], ["A'", "B'", 'Schatten ?']]},
  'schritte': ["Gegeben: SA = 5 cm, AA' = 3 cm, Figur AB = 4 cm. Gesucht ist der Schatten A'B'.",
               "Zuerst die ganze Strecke ab S: SA' = 5 + 3 = 8 cm.",
               "Der Faktor ist SA' : SA = 8 : 5 = 1,6.",
               "Der Schatten ist 1,6-mal so groß: A'B' = 4 · 1,6 = ⟦6,4 cm⟧."],
  'regel': "So nutzt du den ⟦2. Strahlensatz⟧: Die ⟦Parallelstrecken⟧ verhalten sich wie die zugehörigen Abschnitte ⟦ab S⟧: ⟦AB : A'B' = SA : SA'⟧. Rechne nicht mit dem Stück AA' zwischen den Parallelen.",
  'fehler': "A'B' : AB = AA' : SA zu rechnen ist falsch: Beim 2. Strahlensatz braucht man Strecken ⟦ab S⟧, also SA' = SA + AA'. Der Schatten hängt vom Abstand zur Lampe ab."},
 'flaeche_volumen': {
  'einstieg': 'Ein Bastler baut ein Puppenhaus im Maßstab 1 : 20. Jede Länge im echten Haus ist 20-mal so lang. Der Boden ist aber nicht nur 20-mal so groß: Er wird in Länge und Breite gestreckt. Wie sich Fläche und Volumen beim Strecken ändern, beschreibt der ⟦Streckfaktor hoch 2 bzw. hoch 3⟧.',
  'woerter': [['Maßstab 1 : 20', '1 cm im Modell sind 20 cm im Original'],
              ['k²', 'k · k – gilt für Flächen'],
              ['k³', 'k · k · k – gilt für Volumen'],
              ['cm², m²', 'Flächeneinheiten; 1 m² = 10 000 cm²']],
  'schritte': ['Das Modell hat 300 cm² Bodenfläche. Der Streckfaktor zum Original ist k = 20.',
               'Eine Fläche wird in zwei Richtungen gestreckt, also mit k² = 20 · 20 = 400 malgenommen.',
               'Original: 300 · 400 = ⟦120 000 cm²⟧.',
               'Umgerechnet: 120 000 : 10 000 = 12, also 12 m².'],
  'regel': 'So rechnest du Flächen und Volumen um: Werden alle Längen mit k malgenommen, wird der ⟦Flächeninhalt mit k²⟧ und das ⟦Volumen mit k³⟧ malgenommen. Im Bild: Bei doppelter Seite passen ⟦4 = 2²⟧ alte Quadrate hinein; bei einem Würfel passen 8 = 2³ alte Würfel in den doppelt so großen.',
  'fehler': 'Bei doppelter Seitenlänge auch die doppelte Fläche anzunehmen ist falsch: Im Bild passen 4 kleine Quadrate in das große. Die Fläche wächst mit ⟦k² = 4⟧, das Volumen mit k³ = 8.'},
 'anwendung': {
  'einstieg': 'Wie hoch ist ein Baum, auf den man nicht klettern kann? Man stellt einen Stab daneben und misst beide Schatten zur gleichen Zeit. Die Sonnenstrahlen fallen parallel ein, Stab und Baum stehen senkrecht. So entsteht eine Strahlensatz-Figur, mit der man ⟦Strahlensätze anwenden⟧ kann.',
  'woerter': [['Skizze', 'eine schnelle Zeichnung mit allen bekannten Längen'],
              ['h', 'die gesuchte Höhe des Baums'],
              ['Bruchgleichung', 'eine Gleichung, in der die Unbekannte im Nenner eines Bruchs steht'],
              ['h : 2', 'h geteilt durch 2']],
  'bild': {'typ': 'figur', 'punkte': {'S': [0, 0], '_F1': [3, 0], '_T1': [3, 2], '_F2': [18, 0], '_T2': [18, 12]}, 'linien': [['S', '_F1', 'Schatten Stab 3 m'], ['_F1', '_F2'], ['_F1', '_T1', 'Stab 2 m'], ['_F2', '_T2', 'Baum h = ?'], ['S', '_T2', 'Sonnenstrahl', 'gestrichelt']], 'rechter_winkel': [['_F2', 'S', '_T2'], ['_F1', 'S', '_T1']]},
  'schritte': ['Ein 2 m hoher Stab wirft 3 m Schatten, ein Baum zur gleichen Zeit 18 m.',
               'In der Skizze ist S das Ende beider Schatten. Stab und Baum sind die Parallelen.',
               'Höhe zu Schatten ist bei beiden gleich: h : 18 = 2 : 3. Der Baumschatten ist 18 : 3 = 6-mal so lang.',
               'Also ist auch der Baum 6-mal so hoch: h = 2 · 6 = ⟦12 m⟧.'],
  'regel': 'So wendest du die Strahlensätze an: ⟦Skizze⟧ zeichnen, ⟦Scheitel S und Parallelen⟧ erkennen, entsprechende Strecken zuordnen und eine Gleichung aufstellen. Steht die Unbekannte in einer Summe oder im Nenner, entsteht eine ⟦Bruchgleichung⟧: mit den Nennern malnehmen.',
  'fehler': 'h : 18 = 3 : 2 ist falsch zugeordnet – dann wäre der Baum 27 m hoch. Richtig: ⟦Höhe zu Höhe⟧ und ⟦Schatten zu Schatten⟧, oder auf beiden Seiten Höhe zu Schatten.'},
}
klar(ETAPPEN, KLAR)
# ---- KLAR ENDE ----
# ---- UMBAU (neues Muster, Runde 8, Vorgabe 16.11.) ----
_Z = {'x': 1, 'y': 2, 'name': 'Z (Lampe)'}
_P = {'x': 4, 'y': 3, 'name': 'P'}
_D = {'_A': [0, 0], '_B': [7, 0], '_C': [2.071, 3.422], '_A2': [9, 0], '_B2': [26.5, 0], '_C2': [14.179, 8.555]}
def _dreiecke(a, b, c):
    return [['_A', '_C', '4 cm'], ['_C', '_B', '6 cm'], ['_A', '_B', '7 cm'], ['_A2', '_C2', a], ['_C2', '_B2', b], ['_A2', '_B2', c]]
_S1 = {'S': [0, 0], 'A': [3, 0], "A'": [7.5, 0], 'B': [3.277, 2.294], "B'": [8.192, 5.736]}
def _s1(bb): return [['S', 'A', 'SA = 3'], ['A', "A'", "AA' = 4,5"], ['S', 'B', 'SB = 4'], ['B', "B'", bb], ['A', 'B', ''], ["A'", "B'", '']]
_S2 = {'S': [0, 0], 'A': [5, 0], "A'": [8, 0], 'B': [4.305, 3.939], "B'": [6.889, 6.303]}
def _s2(sch): return [['S', 'A', 'SA = 5'], ['A', "A'", "AA' = 3"], ['S', 'B', ''], ['B', "B'", ''], ['A', 'B', 'Figur 4'], ["A'", "B'", sch]]
_BP = {'S': [0, 0], '_F1': [3, 0], '_T1': [3, 2], '_F2': [18, 0], '_T2': [18, 12]}
def _baum(h): return [['S', '_F1', '3 m'], ['_F1', '_F2', ''], ['_F1', '_T1', 'Stab 2 m'], ['_F2', '_T2', h], ['S', '_T2', '', 'gestrichelt']]
UMBAU = {
 'streckung': {
  'einstieg': 'Beim Schattenspiel hält man eine Figur vor eine Lampe. Jeder Schattenpunkt liegt auf einem Lichtstrahl, nur weiter weg. Das ist eine ⟦zentrische Streckung⟧.',
  'woerter': [['Zentrum Z', 'der feste Punkt, von dem aus gestreckt wird, hier die Lampe'],
              ['Streckfaktor k', 'wie viel mal so weit vom Zentrum der Bildpunkt liegt'],
              ["P'", '„P Strich“: der Bildpunkt von P']],
  'bild': {'typ': 'koordinaten', 'x': [0, 9], 'y': [0, 7], 'punkte': [_Z, _P]},
  'schritte': [{'text': 'Das Zentrum Z(1 | 2) ist die Lampe. Gestreckt wird P(4 | 3).'},
               {'text': 'Von Z nach P: 3 nach rechts, 1 nach oben.', 'bild': {'strecken': [[1, 2, 4, 3]]}},
               {'text': 'Mit dem Streckfaktor k = 2 verdoppeln: 6 nach rechts, 2 nach oben.'},
               {'text': "Von Z aus gegangen landest du bei ⟦P'(7 | 4)⟧.",
                'bild': {'strecken': [[1, 2, 7, 4]], 'punkte': [_Z, _P, {'x': 7, 'y': 4, 'name': "P'"}]}}],
  'fehler': "P' ist nicht 2 · P = (8 | 6). Gestreckt wird der Abstand von der Lampe Z, nicht die Koordinaten.",
  'fehler_bild': {'punkte': [_Z, _P, {'x': 7, 'y': 4, 'name': "P'"}, {'x': 8, 'y': 6, 'name': '2 · P (falsch)', 'offen': True}]},
  'regel': "P' liegt auf dem Strahl von Z durch P. Der Abstand zu Z wird mit ⟦k⟧ malgenommen."},
 'aehnlich': {
  'einstieg': 'Ein Foto wird vergrößert. Damit niemand verzerrt aussieht, wird jede Länge mit derselben Zahl malgenommen. Die Winkel bleiben gleich. Original und Vergrößerung sind ⟦ähnlich⟧.',
  'woerter': [['ähnlich', 'gleiche Form, andere Größe: gleiche Winkel, alle Seiten mal k'],
              ['entsprechende Seiten', 'Seiten an der gleichen Stelle beider Figuren'],
              ['Faktor k', 'die Zahl, mit der jede Seite malgenommen wird']],
  'bild': {'typ': 'figur', 'punkte': _D, 'linien': _dreiecke('10 cm', '?', '?')},
  'schritte': [{'text': 'Dreieck 1 hat Seiten mit 4, 6 und 7 cm. Dreieck 2 ist ähnlich.'},
               {'text': 'Entsprechende Seiten: 4 cm wird zu 10 cm. Faktor k = 2,5.'},
               {'text': '6 · 2,5 = ⟦15 cm⟧ und 7 · 2,5 = ⟦17,5 cm⟧.',
                'bild': {'linien': _dreiecke('10 cm', '15 cm', '17,5 cm')}}],
  'fehler': 'Zu jeder Seite 6 cm addieren ist falsch. Aus 6 cm würden 12 cm, das Foto wäre verzerrt. Ähnlich heißt malnehmen.',
  'fehler_bild': {'linien': _dreiecke('10 cm', '12 cm?', '13 cm?')},
  'regel': 'Ähnlich: ⟦alle Seiten mal k⟧, Winkel bleiben gleich. Bei Dreiecken genügen zwei gleiche Winkel.'},
 'strahlensatz1': {
  'einstieg': 'Zwei Lichtstrahlen gehen von der Lampe S aus. Zwei parallele Figuren werden getroffen. Wird der Weg auf einem Strahl 2,5-mal so lang, dann auch auf dem anderen: ⟦1. Strahlensatz⟧.',
  'woerter': [['Scheitel S', 'der Punkt, von dem beide Strahlen ausgehen'],
              ['parallel', 'überall gleich weit voneinander entfernt'],
              ["SA' : SA", "die Länge SA' geteilt durch die Länge SA"]],
  'bild': {'typ': 'figur', 'punkte': _S1, 'linien': _s1('?')},
  'schritte': [{'text': "Scheitel S ist die Lampe. SA = 3, SA' = 7,5, SB = 4."},
               {'text': "Die Strecken AB und A'B' sind parallel."},
               {'text': "SA' : SA = 7,5 : 3 = 2,5. Das gilt auch für SB."},
               {'text': "SB' = 4 · 2,5 = ⟦10 cm⟧. Also ist BB' = 6 cm.", 'bild': {'linien': _s1("BB' = 6")}}],
  'fehler': "SB' ist nicht 4 + 4,5 = 8,5 cm. Die Strecken wachsen mit dem gleichen Faktor, nicht um die gleiche Länge.",
  'fehler_bild': {'linien': _s1("4,5?")},
  'regel': "Abschnitte ab S stehen im ⟦gleichen Verhältnis⟧. Es gilt SA : SA' = SB : SB'."},
 'strahlensatz2': {
  'einstieg': 'Wie groß wird der Schatten an der Wand? Figur und Schatten sind parallel. Sie wachsen wie der Abstand zur Lampe: ⟦2. Strahlensatz⟧.',
  'woerter': [['Parallelstrecken', "die parallelen Strecken AB (Figur) und A'B' (Schatten)"],
              ["SA' = SA + AA'", "die ganze Strecke von S bis A'"]],
  'bild': {'typ': 'figur', 'punkte': _S2, 'linien': _s2('Schatten ?')},
  'schritte': [{'text': "Figur AB = 4 cm, SA = 5 cm, AA' = 3 cm."},
               {'text': "Ganze Strecke ab S: SA' = SA + AA' = 8 cm."},
               {'text': 'Faktor 8 : 5 = 1,6 für die Parallelstrecken.'},
               {'text': "Schatten A'B' = 4 · 1,6 = ⟦6,4 cm⟧.", 'bild': {'linien': _s2('Schatten 6,4')}}],
  'fehler': "A'B' : AB = AA' : SA ist falsch. Der Schatten hängt vom ganzen Abstand zur Lampe ab, also von SA'.",
  'fehler_bild': {'linien': _s2('2,4?')},
  'regel': "Parallelstrecken wachsen wie die ⟦Abschnitte ab S⟧. AB : A'B' = SA : SA'."},
 'flaeche_volumen': {
  'einstieg': 'Ein Bild wird doppelt so breit und doppelt so hoch kopiert. Dafür braucht es viermal so viel Papier. Die Fläche wächst mit dem ⟦Streckfaktor hoch 2⟧.',
  'woerter': [['k²', 'k · k – damit wird jede Fläche malgenommen'],
              ['k³', 'k · k · k – damit wird jedes Volumen malgenommen']],
  'bild': {'typ': 'figur', 'punkte': {'_a': [0, 0], '_b': [1, 0], '_c': [2, 0], '_d': [2, 1], '_e': [2, 2], '_f': [1, 2], '_g': [0, 2], '_h': [0, 1], '_m': [1, 1]},
           'flaeche': ['_a', '_b', '_m', '_h'],
           'linien': [['_a', '_c', '2 · Seite'], ['_c', '_e'], ['_e', '_g'], ['_g', '_a'], ['_b', '_f'], ['_h', '_d']]},
  'schritte': [{'text': 'Alle Längen mal k = 2, die Fläche mal k² = 4.'},
               {'text': 'Im Bild passen 4 kleine Quadrate ins große.'},
               {'text': 'Ein Bild mit 300 cm² wird also ⟦1 200 cm²⟧ groß.'},
               {'text': 'Volumen: Ein Würfel mit doppelter Kante fasst k³ = 8-mal so viel.'}],
  'fehler': 'Doppelte Seite heißt nicht doppelte Fläche. Im Bild passen 4 kleine Quadrate ins große, denn k² = 4.',
  'regel': 'Fläche mal ⟦k²⟧, Volumen mal ⟦k³⟧. Dabei werden alle Längen mit k malgenommen.'},
 'anwendung': {
  'einstieg': 'Wie hoch ist ein Baum? Stell einen Stab daneben und miss beide Schatten zur gleichen Zeit. Die Sonnenstrahlen liefern eine Strahlensatz-Figur: Du ⟦wendest den Strahlensatz an⟧.',
  'woerter': [['Skizze', 'eine schnelle Zeichnung mit allen bekannten Längen'],
              ['h', 'die gesuchte Höhe des Baums']],
  'bild': {'typ': 'figur', 'punkte': _BP, 'linien': _baum('Baum h = ?'), 'rechter_winkel': [['_F2', 'S', '_T2'], ['_F1', 'S', '_T1']]},
  'schritte': [{'text': 'Skizze: Stab 2 m, sein Schatten 3 m. Baumschatten 18 m.'},
               {'text': 'Höhe zu Schatten ist gleich: h : 18 = 2 : 3.'},
               {'text': '18 : 3 = 6, also ist der Baum 6-mal so hoch.'},
               {'text': 'h = 2 · 6 = ⟦12 m⟧.', 'bild': {'linien': _baum('Baum 12 m')}}],
  'fehler': 'h : 18 = 3 : 2 ist falsch zugeordnet. Dann wäre der Baum 27 m hoch. Höhe zu Höhe, Schatten zu Schatten.',
  'fehler_bild': {'linien': _baum('27 m?')},
  'regel': 'Zeichne eine ⟦Skizze⟧ und ordne entsprechende Strecken zu. Dann stellst du eine Verhältnisgleichung auf.'},
}
umbau(ETAPPEN, UMBAU)
# ---- UMBAU ENDE ----


def g_streckung(s):
    if s == 1:
        k = R.choice([2, 3, 4, Fr(1, 2), Fr(3, 2), Fr(5, 2)])
        l = Fr(R.randint(2, 20))
        b = k * l
        if not ok(b): return None
        return zahl(f'Eine Strecke der Länge {dz(l)} cm wird zentrisch mit k = {dz(k)} gestreckt. Wie lang ist die Bildstrecke?',
                    f'Bildstrecke = |k| · Strecke = {dz(k)} · {dz(l)} cm = {dz(b)} cm.', 'Alle Längen werden mit |k| multipliziert.', b,
                    f'{cf(k)} * {cf(l)}', einheit='cm')
    if s == 3 and R.random() < 0.5:
        k = R.choice([-2, -3, Fr(-1, 2), Fr(1, 2), 2, 3])
        z = (R.randint(-3, 3), R.randint(-3, 3))
        d = (2 * R.randint(-2, 2), 2 * R.randint(-2, 2))
        if d == (0, 0): return None
        p = (z[0] + d[0], z[1] + d[1])
        q = (z[0] + k * d[0], z[1] + k * d[1])
        if any(Fr(c).denominator != 1 for c in q): return None
        T = lambda P_: f'({dz(P_[0])} | {dz(P_[1])})'  # noqa: E731
        if R.random() < 0.5:
            return zahl(f'Z{T(z)}, P{T(p)} und der Bildpunkt P\'{T(q)}. Bestimme den Streckfaktor k (mit Vorzeichen).',
                        f'Von Z nach P: ({dz(d[0])} | {dz(d[1])}); von Z nach P\': ({dz(q[0] - z[0])} | {dz(q[1] - z[1])}). Das ist das {dz(k)}-Fache, also k = {dz(k)}.'
                        + (' P\' liegt auf der anderen Seite von Z.' if k < 0 else ''),
                        'Vergleiche den Weg von Z nach P mit dem Weg von Z nach P\'. Zeigt er in die Gegenrichtung, ist k negativ.', k,
                        f'({q[0]} - ({z[0]})) / ({p[0]} - ({z[0]}))' if d[0] else f'({q[1]} - ({z[1]})) / ({p[1]} - ({z[1]}))')
        if k in (1,) or k < 0 and R.random() < 0.5: return None
        return luecken(f'P{T(p)} wird mit k = {dz(k)} auf P\'{T(q)} abgebildet. Wo liegt das Zentrum Z?', 'Z(□ | □)', 'x- und y-Koordinate',
                       [z[0], z[1]],
                       f'P\' − P = ({dz(q[0] - p[0])} | {dz(q[1] - p[1])}) = (k − 1) · (P − Z). Also P − Z = ({dz(d[0])} | {dz(d[1])}) und Z{T(z)}.',
                       'Z, P und P\' liegen auf einer Geraden; ZP\' ist das k-Fache von ZP. Setze Z(x | y) an.',
                       c=[f'({p[0]} * {cf(k)} - ({q[0]})) / ({cf(k)} - 1)', f'({p[1]} * {cf(k)} - ({q[1]})) / ({cf(k)} - 1)'])
    if s == 2 and R.random() < 0.4:
        zp = Fr(R.randint(2, 12))
        k = R.choice([Fr(3, 2), Fr(5, 2), 2, 3, Fr(1, 2), Fr(1, 4)])
        zpb = zp * k
        if not ok(zpb, k): return None
        return zahl(f'Bei einer zentrischen Streckung mit Zentrum Z ist ZP = {dz(zp)} cm und ZP\' = {dz(zpb)} cm (P\' auf dem Strahl ZP). Bestimme k.',
                    f'k = ZP\' : ZP = {dz(zpb)} : {dz(zp)} = {dz(k)}.', 'Teile die Bildlänge durch die Originallänge.', k, f'{cf(zpb)} / {cf(zp)}')
    if s == 2:
        k = R.choice([2, 3, -1, -2])
        z = (R.randint(-2, 2), R.randint(-2, 2))
        p = (z[0] + R.randint(-3, 3), z[1] + R.randint(-3, 3))
        if p == z: return None
    else:
        k = R.choice([-2, -3, Fr(-1, 2), Fr(3, 2), Fr(1, 2)])
        z = (R.randint(-4, 4), R.randint(-4, 4))
        p = (z[0] + 2 * R.randint(-3, 3), z[1] + 2 * R.randint(-3, 3))
        if p == z: return None
    q = (z[0] + k * (p[0] - z[0]), z[1] + k * (p[1] - z[1]))
    if any(Fr(c).denominator != 1 for c in q): return None
    a = luecken(f'Strecke den Punkt P({dz(p[0])} | {dz(p[1])}) zentrisch mit dem Zentrum Z({dz(z[0])} | {dz(z[1])}) und k = {dz(k)}. Gib den Bildpunkt P\' an.', "P'(□ | □)", 'x- und y-Koordinate',
                [q[0], q[1]], f'Von Z nach P: ({dz(p[0] - z[0])} | {dz(p[1] - z[1])}); mal {dz(k)}: ({dz(k * (p[0] - z[0]))} | {dz(k * (p[1] - z[1]))}); P\'({dz(q[0])} | {dz(q[1])}).',
                'Bestimme den Weg von Z nach P, multipliziere mit k und gehe ihn von Z aus.',
                c=[f'{z[0]} + {cf(k)} * ({p[0]} - ({z[0]}))', f'{z[1]} + {cf(k)} * ({p[1]} - ({z[1]}))'])
    if s == 2:
        xs = [z[0], p[0], int(q[0])]; ys = [z[1], p[1], int(q[1])]
        bild(a, kos([{'x': z[0], 'y': z[1], 'name': 'Z'}, {'x': p[0], 'y': p[1], 'name': 'P'}],
                    x=(min(xs) - 2, max(xs) + 2), y=(min(ys) - 2, max(ys) + 2)))
    return a


def g_aehnlich(s):
    if s == 1:
        a, b = R.randint(2, 9), R.randint(3, 12)
        k = R.choice([2, 3, Fr(3, 2), Fr(5, 2), 4])
        if not ok(k * b): return None
        return zahl(f'Zwei Dreiecke sind ähnlich mit k = {dz(k)}. Eine Seite des kleinen Dreiecks ist {b} cm lang. Wie lang ist die entsprechende Seite des großen?',
                    f'{b} cm · {dz(k)} = {dz(k * b)} cm.', 'Entsprechende Seiten: mit k multiplizieren.', k * b, f'{b} * {cf(k)}', einheit='cm')
    if s == 3 and R.random() < 0.4:
        sei = R.sample(range(3, 13), 3)
        a, b, c = sorted(sei)
        if a + b <= c: return None
        k = R.choice([Fr(3, 2), 2, Fr(5, 2), Fr(1, 2), Fr(2, 3)])
        if R.random() < 0.5:
            gross, frag, erg = k * c, 'kürzeste', k * a
            t = f'längste Seite ist {dz(k * c)} cm lang. Wie lang ist seine kürzeste Seite?'
            cexp = f'{a} * {cf(k * c)} / {c}'
        else:
            t = f'kürzeste Seite ist {dz(k * a)} cm lang. Wie lang ist seine längste Seite?'
            erg = k * c
            cexp = f'{c} * {cf(k * a)} / {a}'
        if not ok(k * a, k * c): return None
        return zahl(f'Dreieck 1 hat die Seiten {sei[0]} cm, {sei[1]} cm und {sei[2]} cm. Dreieck 2 ist ähnlich, seine {t}',
                    f'Sortieren: {a} < {b} < {c}. Längste zu längster, kürzeste zu kürzester: k = {dz(k)}; gesucht {dz(erg)} cm.',
                    'Ordne die Seiten zuerst der Größe nach; entsprechende Seiten haben den gleichen Rang.', erg, cexp, einheit='cm')
    if s == 2 and R.random() < 0.35:
        return g_aehnlich_winkel()
    if s == 2:
        a, b, c = sorted(R.sample(range(3, 13), 3))
        if a + b <= c: return None
        k = R.choice([Fr(3, 2), 2, Fr(5, 2), 3, Fr(5, 4)])
        a2 = k * a
        welche = R.choice([b, c])
        if not ok(a2, k * welche): return None
        return zahl(f'Ein Dreieck hat die Seiten {a} cm, {b} cm und {c} cm. In einem ähnlichen Dreieck ist die kürzeste Seite {dz(a2)} cm lang. Wie lang ist die Seite, die {welche} cm entspricht?',
                    f'k = {dz(a2)} : {a} = {dz(k)}; {welche} · {dz(k)} = {dz(k * welche)} cm.', 'Bestimme zuerst k aus den kürzesten Seiten.', k * welche,
                    f'{welche} * ({cf(a2)} / {a})', einheit='cm')
    typ = R.random()
    if typ < 0.5:
        a, b, c = sorted(R.sample(range(3, 13), 3))
        if a + b <= c: return None
        k = R.choice([2, 3, Fr(3, 2)])
        aehn = R.random() < 0.5
        d = 0 if aehn else R.choice([1, 2])
        s2 = (k * a, k * b, k * c + d)
        r = 'ja' if aehn else 'nein'
        return auswahl(f'Dreieck 1: {a} cm, {b} cm, {c} cm. Dreieck 2: {dz(s2[0])} cm, {dz(s2[1])} cm, {dz(s2[2])} cm. Sind sie ähnlich?',
                       f'{"Ja" if aehn else "Nein"}, {"alle" if aehn else "nicht alle"} Seitenverhältnisse sind gleich.',
                       ['Ja, alle Seitenverhältnisse sind gleich.', 'Nein, nicht alle Seitenverhältnisse sind gleich.',
                        'Ja, weil beide Dreiecke drei Seiten haben.', 'Nein, weil die Seiten verschieden lang sind.'],
                       f'{dz(s2[0])} : {a} = {dz(k)}, {dz(s2[1])} : {b} = {dz(k)}, {dz(s2[2])} : {c} = {dz(s2[2] / c) if ok(s2[2] / c) else br(s2[2] / c)}{" – gleich" if aehn else " – verschieden"}.',
                       'Bilde die Verhältnisse entsprechender Seiten (kurz zu kurz, lang zu lang).')
    return g_aehnlich_winkel()


def g_aehnlich_winkel():
    al, be = R.randint(25, 80), R.randint(25, 80)
    ga = 180 - al - be
    if ga <= 10: return None
    aehn = R.random() < 0.5
    if aehn:
        w2 = (be, ga)
    else:
        w2 = (be, ga + R.choice([-5, 5, 10]))
        if 180 - sum(w2) <= 0: return None
        if sorted([al, be, ga]) == sorted([w2[0], w2[1], 180 - sum(w2)]): return None
    return auswahl(f'Dreieck 1 hat die Winkel {al}° und {be}°. Dreieck 2 hat die Winkel {w2[0]}° und {w2[1]}°. Sind die Dreiecke ähnlich?',
                   f'{"Ja" if aehn else "Nein"}: Der dritte Winkel ist {180 - w2[0] - w2[1]}°{"." if aehn else ", die Winkel stimmen nicht überein."}',
                   [f'{"Nein" if aehn else "Ja"}: Der dritte Winkel ist {180 - w2[0] - w2[1]}°.', 'Das kann man ohne Seitenlängen nicht entscheiden.',
                    'Ja, alle Dreiecke mit spitzen Winkeln sind ähnlich.'],
                   f'Dreieck 1: dritter Winkel {ga}°. Dreieck 2: {180 - w2[0] - w2[1]}°. {"Alle drei Winkel stimmen überein" if aehn else "Die Winkel stimmen nicht überein"}.',
                   'Berechne jeweils den dritten Winkel mit der Winkelsumme 180°.')


ERG1 = set()


def g_strahlensatz1(s):
    sa = Fr(R.randint(2, 9))
    k = R.choice([Fr(3, 2), 2, Fr(5, 2), 3, Fr(5, 4), Fr(7, 4)])
    sb = Fr(R.randint(2, 10))
    sa2, sb2 = k * sa, k * sb
    if not ok(sa2, sb2): return None
    aa, bb = sa2 - sa, sb2 - sb
    if s == 1:
        if sb2 in ERG1 and len(ERG1) < 40: return None
        ERG1.add(sb2)
        return bild(zahl(f'{KURZ} SA = {dz(sa)} cm, SA\' = {dz(sa2)} cm, SB = {dz(sb)} cm. Berechne SB\'.',
                         f'SB\' : SB = SA\' : SA = {dz(k)} ⇒ SB\' = {dz(sb)} · {dz(k)} = {dz(sb2)} cm.', 'Setze das Verhältnis auf beiden Strahlen gleich.', sb2,
                         f'{cf(sb)} * {cf(sa2)} / {cf(sa)}', einheit='cm'),
                    sfig(sa, sa2, sb, sb2, {'SA': dz(sa), 'SB': dz(sb)}))
    if s == 2:
        if sa2 in ERG1 and len(ERG1) < 40: return None
        ERG1.add(sa2)
        if R.random() < 0.5:
            return bild(zahl(f'{KURZ} SA = {dz(sa)} cm, SB = {dz(sb)} cm, SB\' = {dz(sb2)} cm. Berechne SA\'.',
                             f'SA\' : SA = SB\' : SB = {dz(k)} ⇒ SA\' = {dz(sa)} · {dz(k)} = {dz(sa2)} cm.', 'Welches Verhältnis kennst du vollständig?', sa2,
                             f'{cf(sa)} * {cf(sb2)} / {cf(sb)}', einheit='cm'),
                        sfig(sa, sa2, sb, sb2, {'SA': dz(sa), 'SB': dz(sb)}))
        return bild(zahl(f'{KURZ} SA = {dz(sa)} cm, AA\' = {dz(aa)} cm, SB = {dz(sb)} cm. Berechne SB\'.',
                         f'SA\' = {dz(sa)} + {dz(aa)} = {dz(sa2)} cm. SB\' = {dz(sb)} · {dz(sa2)} : {dz(sa)} = {dz(sb2)} cm.',
                         'Berechne zuerst SA\' = SA + AA\'.', sb2, f'{cf(sb)} * ({cf(sa)} + {cf(aa)}) / {cf(sa)}', einheit='cm'),
                    sfig(sa, sa2, sb, sb2, {'SA': dz(sa), 'AA': dz(aa), 'SB': dz(sb), 'BB': '?'}))
    typ = R.random()
    if typ < 0.3:
        return bild(zahl(f'X-Figur: Die Geraden AA\' und BB\' schneiden sich in S, AB ∥ A\'B\'. SA = {dz(sa)} cm, SB = {dz(sb)} cm, SA\' = {dz(sa2)} cm. Berechne SB\'.',
                         f'Auch bei der X-Figur gilt SA : SA\' = SB : SB\' ⇒ SB\' = {dz(sb)} · {dz(sa2)} : {dz(sa)} = {dz(sb2)} cm.',
                         'Die Strahlensätze gelten auch, wenn S zwischen den Parallelen liegt. Strecken immer ab S messen.', sb2,
                         f'{cf(sb)} * {cf(sa2)} / {cf(sa)}', einheit='cm'),
                    sfig(sa, sa2, sb, sb2, {'SA': dz(sa), 'SB': dz(sb), 'SA2': dz(sa2), 'SB2': '?'}, x=True))
    if typ < 0.55:
        par = R.random() < 0.5
        bb_ = bb if par else bb + R.choice([-1, 1])
        if bb_ <= 0: return None
        q1, q2 = sa / sa2, sb / (sb + bb_)
        return bild(auswahl(f'SA = {dz(sa)} cm, AA\' = {dz(aa)} cm, SB = {dz(sb)} cm, BB\' = {dz(bb_)} cm. Sind AB und A\'B\' parallel?',
                            f'Ja, {dz(sa)} : {dz(sa2)} = {dz(sb)} : {dz(sb + bb_)}.' if par else f'Nein, {dz(sa)} : {dz(sa2)} ≠ {dz(sb)} : {dz(sb + bb_)}.',
                            ([f'Nein, {dz(sa)} : {dz(sa2)} ≠ {dz(sb)} : {dz(sb + bb_)}.'] if par else [f'Ja, {dz(sa)} : {dz(sa2)} = {dz(sb)} : {dz(sb + bb_)}.'])
                            + ['Ja, weil beide Strahlen bei S beginnen.', f'Nein, weil {dz(aa)} ≠ {dz(bb_)}.' if aa != bb_ else 'Ja, weil AA\' = BB\'.'],
                            f'Umkehrung des 1. Strahlensatzes: Parallel genau dann, wenn SA : SA\' = SB : SB\'. {dz(sa)} : {dz(sa2)} = {br(q1)}, {dz(sb)} : {dz(sb + bb_)} = {br(q2)}.',
                            'Berechne SA\' und SB\' und vergleiche die Verhältnisse ab S.'),
                    sfig(sa, sa2, sb, sb + bb_, {'SA': dz(sa), 'AA': dz(aa), 'SB': dz(sb), 'BB': dz(bb_)}))
    if typ < 0.8:
        return bild(zahl(f'{KURZ} SA = {dz(sa)} cm, AA\' = {dz(aa)} cm, SB = {dz(sb)} cm. Berechne BB\'.',
                         f'Auch die Abschnitte zwischen den Parallelen stehen im gleichen Verhältnis: BB\' : SB = AA\' : SA ⇒ BB\' = {dz(sb)} · {dz(aa)} : {dz(sa)} = {dz(bb)} cm.',
                         'Der 1. Strahlensatz gilt auch für die Teilstücke AA\' und BB\'.', bb, f'{cf(sb)} * {cf(aa)} / {cf(sa)}', einheit='cm'),
                    sfig(sa, sa2, sb, sb2, {'SA': dz(sa), 'AA': dz(aa), 'SB': dz(sb), 'BB': '?'}))
    return bild(zahl(f'{KURZ} SA\' = {dz(sa2)} cm, AA\' = {dz(aa)} cm, SB\' = {dz(sb2)} cm. Berechne SB.',
                     f'SA = {dz(sa2)} − {dz(aa)} = {dz(sa)} cm. SB = SB\' · SA : SA\' = {dz(sb)} cm.', 'Berechne zuerst SA.', sb,
                     f'{cf(sb2)} * ({cf(sa2)} - {cf(aa)}) / {cf(sa2)}', einheit='cm'),
                sfig(sa, sa2, sb, sb2, {'AA': dz(aa), 'SB': '?'}))


def g_strahlensatz2(s):
    sa = Fr(R.randint(2, 9))
    k = R.choice([Fr(3, 2), 2, Fr(5, 2), 3, Fr(5, 4), Fr(8, 5)])
    ab = Fr(R.randint(2, 10))
    sa2, ab2 = k * sa, k * ab
    if not ok(sa2, ab2): return None
    aa = sa2 - sa
    sb = Fr(R.randint(3, 9))
    F = lambda lab: sfig(sa, sa2, sb, k * sb, lab)  # noqa: E731
    if s == 1:
        return bild(zahl(f'{KURZ} SA = {dz(sa)} cm, SA\' = {dz(sa2)} cm, AB = {dz(ab)} cm. Berechne A\'B\'.',
                         f'A\'B\' : AB = SA\' : SA = {dz(k)} ⇒ A\'B\' = {dz(ab)} · {dz(k)} = {dz(ab2)} cm.', 'Parallelstrecken verhalten sich wie die Abschnitte ab S.',
                         ab2, f'{cf(ab)} * {cf(sa2)} / {cf(sa)}', einheit='cm'), F({'SA': dz(sa), 'AB': dz(ab), 'AB2': '?'}))
    if s == 2:
        if R.random() < 0.5:
            return bild(zahl(f'{KURZ} SA = {dz(sa)} cm, AA\' = {dz(aa)} cm, AB = {dz(ab)} cm. Berechne A\'B\'.',
                             f'SA\' = {dz(sa)} + {dz(aa)} = {dz(sa2)} cm. A\'B\' = {dz(ab)} · {dz(sa2)} : {dz(sa)} = {dz(ab2)} cm.',
                             'Rechne mit SA\' (ab S), nicht mit AA\'.', ab2, f'{cf(ab)} * ({cf(sa)} + {cf(aa)}) / {cf(sa)}', einheit='cm'),
                        F({'SA': dz(sa), 'AA': dz(aa), 'AB': dz(ab), 'AB2': '?'}))
        return bild(zahl(f'{KURZ} AB = {dz(ab)} cm, A\'B\' = {dz(ab2)} cm, SA\' = {dz(sa2)} cm. Berechne SA.',
                         f'SA : SA\' = AB : A\'B\' ⇒ SA = {dz(sa2)} · {dz(ab)} : {dz(ab2)} = {dz(sa)} cm.', 'Stelle das Verhältnis mit der Unbekannten auf.', sa,
                         f'{cf(sa2)} * {cf(ab)} / {cf(ab2)}', einheit='cm'), F({'SA': '?', 'AB': dz(ab), 'AB2': dz(ab2)}))
    typ = R.random()
    if typ < 0.25:
        falsch = ab * aa / sa
        if not ok(falsch) or falsch == ab2: return None
        return bild(auswahl(f'{KURZ} SA = {dz(sa)} cm, AA\' = {dz(aa)} cm, AB = {dz(ab)} cm. Jemand rechnet A\'B\' = {dz(ab)} · {dz(aa)} : {dz(sa)} = {dz(falsch)} cm. Was stimmt?',
                            f'Falsch: Man braucht SA\' = {dz(sa2)} cm, also A\'B\' = {dz(ab2)} cm.',
                            ['Richtig.', f'Falsch: A\'B\' = {dz(ab + aa)} cm.', f'Falsch: A\'B\' = {dz(ab * sa / sa2) if ok(ab * sa / sa2) else br(ab * sa / sa2)} cm.'],
                            f'Beim 2. Strahlensatz stehen die Parallelen im Verhältnis der Abschnitte ab S: A\'B\' = {dz(ab)} · {dz(sa2)} : {dz(sa)} = {dz(ab2)} cm.',
                            'Welche Strecken gehören beim 2. Strahlensatz zusammen?'), F({'SA': dz(sa), 'AA': dz(aa), 'AB': dz(ab), 'AB2': '?'}))
    if typ < 0.45:
        return bild(auswahl(f'{KURZ} Jemand rechnet AB : A\'B\' = SB : BB\'. Was stimmt?', 'Falsch: Richtig ist AB : A\'B\' = SB : SB\'.',
                            ['Richtig.', 'Falsch: Richtig ist AB : A\'B\' = SA : AA\'.', 'Falsch: Richtig ist AB : A\'B\' = BB\' : SB.'],
                            'Beim 2. Strahlensatz stehen die Parallelstrecken im Verhältnis der Strecken ab S – nicht der Teilstücke zwischen den Parallelen.',
                            'Wo beginnen die Strecken, die beim 2. Strahlensatz verwendet werden?'), F({}))
    if typ < 0.65:
        return bild(zahl(f'X-Figur: Die Geraden AA\' und BB\' schneiden sich in S, AB ∥ A\'B\'. SA = {dz(sa)} cm, SA\' = {dz(sa2)} cm, AB = {dz(ab)} cm. Berechne A\'B\'.',
                         f'A\'B\' : AB = SA\' : SA ⇒ A\'B\' = {dz(ab)} · {dz(sa2)} : {dz(sa)} = {dz(ab2)} cm.',
                         'Die Strahlensätze gelten auch bei der X-Figur; Strecken ab S messen.', ab2, f'{cf(ab)} * {cf(sa2)} / {cf(sa)}', einheit='cm'),
                    sfig(sa, sa2, sb, k * sb, {'SA': dz(sa), 'SA2': dz(sa2), 'AB': dz(ab), 'AB2': '?'}, x=True))
    return bild(zahl(f'{KURZ} SA = {dz(sa)} cm, AB = {dz(ab)} cm, A\'B\' = {dz(ab2)} cm. Berechne AA\'.',
                     f'(SA + x) : SA = A\'B\' : AB ⇒ ({dz(sa)} + x) : {dz(sa)} = {dz(k)} ⇒ x = {dz(sa)} · {dz(k)} − {dz(sa)} = {dz(aa)} cm.',
                     'Nenne AA\' = x; dann ist SA\' = SA + x.', aa, f'{cf(sa)} * {cf(ab2)} / {cf(ab)} - {cf(sa)}', einheit='cm'),
                F({'SA': dz(sa), 'AA': '?', 'AB': dz(ab), 'AB2': dz(ab2)}))


def g_flaeche_volumen(s):
    if s == 1:
        k = R.randint(2, 5)
        A = R.randint(2, 30)
        return zahl(f'Alle Längen einer Figur werden mit {k} multipliziert. Die Figur hatte {A} cm² Flächeninhalt. Wie groß ist er jetzt?',
                    f'Fläche · k² = {A} · {k * k} = {dz(A * k * k)} cm².', 'Fläche wächst mit dem Quadrat des Streckfaktors.', A * k * k, f'{A} * {k} ** 2', einheit='cm²')
    if s == 2:
        typ = R.random()
        if typ < 0.4:
            k = R.choice([2, 3, Fr(1, 2), Fr(3, 2)])
            V = R.choice([8, 16, 24, 40, 80])
            v2 = V * Fr(k) ** 3
            if not ok(v2): return None
            return zahl(f'Ein Körper hat {V} cm³ Volumen. Alle Kanten werden mit k = {dz(k)} multipliziert. Wie groß ist das neue Volumen?',
                        f'Volumen · k³ = {V} · {dz(Fr(k) ** 3)} = {dz(v2)} cm³.', 'Volumen wächst mit k³.', v2, f'{V} * {cf(k)} ** 3', einheit='cm³')
        if typ < 0.7:
            k = R.randint(2, 6)
            return zahl(f'Eine Figur wird so vergrößert, dass ihr Flächeninhalt {k * k}-mal so groß ist. Mit welchem Faktor wurden die Längen multipliziert?',
                        f'k² = {k * k} ⇒ k = {k}.', 'Fläche: k². Rückwärts: Wurzel ziehen.', k, f'{k * k} / {k}')
        k = R.randint(2, 4)
        return zahl(f'Ein Würfel wird so vergrößert, dass sein Volumen {k ** 3}-mal so groß ist. Wie oft so groß ist seine Oberfläche?',
                    f'k³ = {k ** 3} ⇒ k = {k}; Oberfläche · k² = {k * k}-mal so groß.', 'Bestimme zuerst k aus dem Volumen.', k * k, f'({k ** 3} / {k} ** 2) ** 2')
    m = R.choice([10, 20, 25, 50, 100])
    A = R.choice([2, 3, 4, 6, 8, 12])
    typ = R.random()
    if typ < 0.3:
        if R.random() < 0.5:
            b, h = R.choice([(9, 13), (10, 15), (13, 18), (15, 20)])
            k = R.choice([2, 3])
            return auswahl(f'Ein Foto {b} cm × {h} cm wird auf {b * k} cm × {h * k} cm vergrößert. Jemand sagt: „Es braucht {k}-mal so viel Papier.“ Was stimmt?',
                           f'Falsch: k = {k}, die Fläche wird {k * k}-mal so groß.',
                           ['Richtig, alle Längen sind ' + str(k) + '-mal so groß.', f'Falsch: Die Fläche wird {k ** 3}-mal so groß.', f'Falsch: Die Fläche wird {2 * k}-mal so groß.'],
                           f'{b} · {h} = {b * h} cm², {b * k} · {h * k} = {b * h * k * k} cm² – das ist das {k * k}-Fache (k² = {k * k}).',
                           'Berechne beide Flächeninhalte.')
        k = R.choice([2, 3])
        return auswahl(f'Jemand sagt: „Ein Würfel mit {"doppelter" if k == 2 else "dreifacher"} Kantenlänge aus demselben Material wiegt {"doppelt" if k == 2 else "dreimal"} so viel.“ Was stimmt?',
                       f'Falsch: Das Volumen wird {k ** 3}-mal so groß, also auch die Masse.',
                       ['Richtig, Masse und Kante wachsen gleich.', f'Falsch: Er wiegt {k * k}-mal so viel.', 'Falsch: Er wiegt gleich viel.'],
                       f'Volumen · k³ = · {k ** 3}. Bei gleichem Material wächst die Masse wie das Volumen.',
                       'Wie verändert sich das Volumen bei k = ' + str(k) + '?')
    if typ < 0.65:
        orig = A * m * m
        return zahl(f'Ein Modell im Maßstab 1 : {m} hat eine Grundfläche von {A} cm². Wie groß ist die Grundfläche des Originals in m²?',
                    f'{A} cm² · {m}² = {dz(orig)} cm² = {dz(Fr(orig, 10000))} m².', 'Fläche · k², dann cm² in m² umrechnen (1 m² = 10 000 cm²).',
                    Fr(orig, 10000), f'{A} * {m} ** 2 / 10000', einheit='m²')
    V = R.choice([1, 2, 3, 4, 5])
    m = R.choice([10, 20, 50])
    orig = V * m ** 3
    return zahl(f'Ein Modell im Maßstab 1 : {m} hat {V} cm³ Volumen. Wie groß ist das Volumen des Originals in m³?',
                f'{V} cm³ · {m}³ = {dz(orig)} cm³ = {dz(Fr(orig, 10 ** 6))} m³.', 'Volumen · k³, dann cm³ in m³ (1 m³ = 1 000 000 cm³).',
                Fr(orig, 10 ** 6), f'{V} * {m} ** 3 / 1000000', einheit='m³')


DINGE = [('ein Baum', 4, 30), ('ein Turm', 15, 60), ('ein Mast', 8, 40), ('ein Haus', 6, 30)]


def schatten_fig(st, sch, sch2, h_txt='h = ?'):
    f = 3 / float(sch)
    return {'typ': 'figur', 'punkte': {'S': [0, 0], '_F1': [3, 0], '_T1': [3, round(float(st) * f, 3)],
                                       '_F2': [round(float(sch2) * f, 3), 0], '_T2': [round(float(sch2) * f, 3), round(float(sch2 * st / sch) * f, 3)]},
            'linien': [['S', '_F1', f'{dz(sch)} m'], ['_F1', '_F2'], ['_F1', '_T1', f'{dz(st)} m'], ['_F2', '_T2', h_txt], ['S', '_T2', '', 'gestrichelt']],
            'rechter_winkel': [['_F2', 'S', '_T2'], ['_F1', 'S', '_T1']]}


def g_anwendung(s):
    typ = R.random()
    if s == 1 or (s == 2 and typ < 0.4):
        st, sch = R.choice([(1, 2), (2, 3), (Fr(3, 2), 2), (1, Fr(5, 4)), (2, 5), (Fr(1, 2), 1)])
        k = R.randint(3, 30)
        sch2 = sch * k
        h = st * k
        if not ok(h, sch2): return None
        moegl = [d for d, lo, hi in DINGE if lo <= h <= hi]
        if not moegl: return None
        ding = R.choice(moegl)
        return bild(zahl(f'Ein {dz(st)} m langer Stab wirft einen {dz(sch)} m langen Schatten. Zur gleichen Zeit wirft {ding} einen {dz(sch2)} m langen Schatten. Wie hoch ist er?',
                         f'h : {dz(st)} = {dz(sch2)} : {dz(sch)} ⇒ h = {dz(st)} · {dz(k)} = {dz(h)} m.', 'Höhe zu Höhe wie Schatten zu Schatten.', h,
                         f'{cf(st)} * {cf(sch2)} / {cf(sch)}', einheit='m'), schatten_fig(st, sch, sch2) if s == 1 else None)
    if s == 2:
        arm = R.choice([60, 65, 70])
        aug = Fr(arm, 10)
        sp = R.choice([20, 25, 30, 40, 50, 60])
        e = Fr(sp * arm) / aug
        if not ok(e): return None
        return zahl(f'Daumensprung: Dein Arm ist {arm} cm lang, deine Augen sind {dz(aug)} cm voneinander entfernt. Schließt du abwechselnd ein Auge, springt dein Daumen vor einem Haus um {sp} m hin und her. Wie weit ist das Haus entfernt?',
                    f'Entfernung : Sprung = Armlänge : Augenabstand ⇒ e = {sp} · {arm} : {dz(aug)} = {dz(e)} m.',
                    'Das Auge ist S; Augenabstand und Daumensprung sind die parallelen Strecken.', e, f'{sp} * {arm} / {cf(aug)}', einheit='m')
    if typ < 0.35:
        h1, h2 = R.choice([(2, 4), (2, 5), (Fr(3, 2), 6), (2, 6), (3, 9), (Fr(5, 2), 10)])
        d = R.randint(2, 12)
        x = h1 * d / (h2 - h1)
        if not ok(x): return None
        return zahl(f'Ein Baum steht {d} m hinter einer {dz(h1)} m hohen Mauer und ist {dz(h2)} m hoch. Von einem Punkt P auf dem Boden vor der Mauer sieht man die Oberkante der Mauer und die Baumspitze genau in einer Linie. Wie weit ist P von der Mauer entfernt?',
                    f'x : (x + {d}) = {dz(h1)} : {dz(h2)} ⇒ {dz(h2)}x = {dz(h1)}x + {dz(h1 * d)} ⇒ {dz(h2 - h1)}x = {dz(h1 * d)} ⇒ x = {dz(x)} m.',
                    'P ist der Scheitel. Mauer und Baum sind die Parallelen; die Entfernung zum Baum ist x + ' + str(d) + '.', x,
                    f'{cf(h1)} * {d} / ({cf(h2)} - {cf(h1)})', einheit='m')
    if typ < 0.7:
        ab = R.choice([20, 24, 30, 36, 40, 45, 50, 60])
        bc = R.choice([4, 5, 6, 8, 10])
        cd = R.choice([3, 4, 5, 6, 8])
        at = Fr(cd * ab, bc)
        if not ok(at) or at < 5: return None
        return bild(zahl(f'Flussbreite messen: Du stehst am Ufer bei A, genau gegenüber steht ein Baum T. Du gehst am Ufer {ab} m bis B und steckst einen Stab ein, dann weitere {bc} m bis C. Von C gehst du senkrecht vom Fluss weg, bis du bei D den Stab B und den Baum T in einer Linie siehst. CD = {cd} m. Wie breit ist der Fluss (AT)?',
                         f'X-Figur mit Scheitel B: AT : CD = AB : BC ⇒ AT = {cd} · {ab} : {bc} = {dz(at)} m.',
                         'Zeichne eine Skizze: Die Geraden TD und AC schneiden sich in B; AT und CD sind parallel.', at,
                         f'{cd} * {ab} / {bc}', einheit='m'),
                    {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [ab, 0], 'C': [ab + bc, 0], 'D': [ab + bc, -cd], 'T': [0, round(float(at), 3)]},
                     'linien': [['A', 'B', f'{ab} m'], ['B', 'C', f'{bc} m'], ['C', 'D', f'{cd} m'], ['A', 'T', '?'], ['T', 'D', '', 'gestrichelt']],
                     'rechter_winkel': [['A', 'B', 'T'], ['C', 'B', 'D']]})
    arm = R.choice([Fr(6, 10), Fr(65, 100), Fr(7, 10)])
    daumen = R.choice([Fr(2, 100), Fr(25, 1000), Fr(3, 100)])
    hb = R.choice([10, 15, 20, 25, 30, 40])
    e = hb * arm / daumen
    if not ok(e): return None
    return zahl(f'Mit ausgestrecktem Arm ({dz(arm)} m vom Auge) verdeckt ein {dz(daumen * 100)} cm breiter Daumen genau ein {hb} m hohes Gebäude. Wie weit ist das Gebäude entfernt?',
                f'e : {dz(arm)} = {hb} : {dz(daumen)} ⇒ e = {dz(arm)} · {hb} : {dz(daumen)} = {dz(e)} m.', 'S ist das Auge; Daumen und Gebäude sind die Parallelen.',
                e, f'{cf(arm)} * {hb} / {cf(daumen)}', einheit='m')


GEN = {'streckung': g_streckung, 'aehnlich': g_aehnlich, 'strahlensatz1': g_strahlensatz1, 'strahlensatz2': g_strahlensatz2,
       'flaeche_volumen': g_flaeche_volumen, 'anwendung': g_anwendung}

# ---------- Zehnte Runde (schwer-kl9): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Abschnitt mit eigenem festen Zufallsstart (anhaengen(..., 9909, ...)), läuft erst nach bauen():
# alle bisherigen Aufgaben bleiben unverändert. Vorbilder: Bayerischer Mathematik-Test 10 (ISB; 2009: Entfernung
# des Mondes mit einer Perle vor dem Auge schätzen; 2023: Ähnlichkeit bei DIN-Formaten; 2025: Strahlensatz führt auf
# eine Gleichung, deren Lösung zu zeigen ist), Illustrierende Aufgaben Realschule 9 (I) (zentrische Streckung: Z und k
# bestimmen, k = 1 als Falle; Schränke unter der Dachschräge; Kreisbogen bei doppeltem Radius), Musterschulaufgaben
# Kl. 9 (Straßensteigung mit Strahlensatz, ähnliche Figuren ja/nein). Zahlen und Wortlaut eigen.
from _schwer_kl9 import anhaengen  # noqa: E402
from _kl9 import K as _K  # noqa: E402


def schwer():
    P, Kn, O = 'pruefung', 'knobel', ''
    PT = 'Koordinaten eintragen (auch negativ)'
    return [
        # streckung
        ('streckung', 3, P, zahl('Ein Dreieck wird zentrisch gestreckt. Aus der Seite AB = 4 cm wird A\'B\' = 6 cm, und das Bilddreieck liegt auf der anderen Seite des Zentrums (es steht auf dem Kopf). Wie groß ist der Streckfaktor k?',
                                 '|k| = 6 : 4 = 1,5. Liegt das Bild auf der anderen Seite des Zentrums, ist k negativ: k = −1,5.',
                                 'Der Betrag kommt aus dem Längenverhältnis, das Vorzeichen aus der Lage zum Zentrum.', -1.5, '-6 / 4')),
        ('streckung', 3, P, luecken('Bei einer zentrischen Streckung mit Zentrum Z(0 | 0) wird A(2 | 1) auf A\'(6 | 3) abgebildet. Wohin wird B(−1 | 4) abgebildet?', "B'(□ | □)", PT, [-3, 12],
                                    'Aus A → A\' folgt k = 3. Mit Zentrum im Ursprung werden die Koordinaten mal 3 genommen: B\'(−3 | 12).',
                                    'Bestimme zuerst k aus A und A\'.', ['3 * (-1)', '3 * 4'])),
        ('streckung', 3, Kn, auswahl('Eine Figur wird mit demselben Zentrum Z zuerst mit k = −2 und dann mit k = −0,5 gestreckt. Was ist insgesamt passiert?',
                                     'Jeder Punkt liegt wieder an seiner alten Stelle (insgesamt k = 1).',
                                     ['Die Figur ist an Z gespiegelt (k = −1).', 'Die Figur ist doppelt so groß (k = 2).', 'Die Figur ist halb so groß (k = −2,5).'],
                                     'Hintereinander ausführen heißt Faktoren malnehmen: (−2) · (−0,5) = 1. Mit k = 1 bleibt alles, wie es war.',
                                     'Was passiert mit dem Abstand zu Z bei beiden Schritten zusammen?')),
        ('streckung', 3, O, luecken('Strecke P(1 | 2) zentrisch mit dem Zentrum Z(3 | 0) und k = −2.', "P'(□ | □)", PT, [7, -4],
                                    'Von Z nach P: (−2 | 2). Mal −2: (4 | −4). Von Z aus abtragen: P\'(3 + 4 | 0 − 4) = P\'(7 | −4).',
                                    'Erst den Weg von Z nach P bestimmen, dann mit k malnehmen, dann von Z aus abtragen.', ['3 + 4', '0 - 4'])),
        ('streckung', 2, O, luecken('Strecke P(8 | −6) mit Zentrum Z(0 | 0) und k = 0,5.', "P'(□ | □)", PT, [4, -3], 'Zentrum im Ursprung: Koordinaten mal 0,5: P\'(4 | −3).',
                                    'Bei Z im Ursprung werden beide Koordinaten mit k malgenommen.', ['8 // 2', '-6 // 2'])),
        ('streckung', 2, O, zahl('Bei einer zentrischen Streckung wird eine 5 cm lange Strecke auf 2 cm abgebildet. Wie groß ist |k|?', '|k| = 2 : 5 = 0,4.',
                                 'Bildlänge geteilt durch Originallänge.', 0.4, '2 / 5')),
        # aehnlich
        ('aehnlich', 3, P, zahl('Papierformate wie DIN A4 sind so gebaut, dass Länge : Breite = √2 gilt; deshalb ist ein halbiertes Blatt ähnlich zum ganzen. Ein Blatt ist 21 cm breit. Wie lang ist es? Runde auf eine Nachkommastelle.',
                                'Länge = 21 cm · √2 ≈ 21 · 1,4142 ≈ 29,7 cm.', 'Länge = Breite · √2.', round(21 * 2 ** 0.5, 1), f'round({_K(21 * 2 ** 0.5)}, 1)', einheit='cm')),
        ('aehnlich', 3, P, auswahl('Welche zwei Figuren sind auf jeden Fall zueinander ähnlich?', 'zwei Quadrate',
                                   ['zwei Rechtecke mit gleichem Umfang', 'zwei Rechtecke mit gleichem Flächeninhalt', 'zwei Rechtecke, die jeweils 2 cm länger als breit sind'],
                                   'Bei zwei Quadraten passt immer ein Faktor k für alle Seiten. Gegenbeispiel Rechtecke: 1 cm × 3 cm und 2 cm × 4 cm sind beide 2 cm länger als breit, aber 3 : 1 ≠ 4 : 2.',
                                   'Suche zu jeder Aussage ein Gegenbeispiel.')),
        ('aehnlich', 3, Kn, auswahl('Ein Bild (20 cm × 30 cm) bekommt ringsum einen 5 cm breiten Rand. Ist das äußere Rechteck ähnlich zum Bild?', 'Nein, denn 30 : 20 ≠ 40 : 30.',
                                    ['Ja, weil überall gleich viel dazukommt.', 'Ja, weil alle Winkel 90° sind.', 'Nein, weil das äußere Rechteck größer ist.'],
                                    'Außen: 30 cm × 40 cm. Verhältnisse: 30 : 20 = 1,5 und 40 : 30 ≈ 1,33. Ähnlich heißt gleicher Faktor für alle Seiten – gleicher Zuwachs reicht nicht.',
                                    'Berechne die Maße des äußeren Rechtecks und vergleiche die Faktoren.')),
        ('aehnlich', 3, O, zahl('Zwei Dreiecke sind ähnlich. Das kleine hat 18 cm Umfang, das große 45 cm. Die kürzeste Seite des großen ist 10 cm lang. Wie lang ist die kürzeste Seite des kleinen?',
                                'Auch der Umfang wächst mit k: k = 45 : 18 = 2,5. Kürzeste Seite klein: 10 : 2,5 = 4 cm.', 'Der Umfang wird mit demselben Faktor k malgenommen wie jede Seite.',
                                4, '10 / (45 / 18)', einheit='cm')),
        ('aehnlich', 2, O, zahl('Dreieck 1 hat die Seiten 3 cm, 4 cm und 5 cm. Dreieck 2 ist ähnlich mit k = 1,5. Welchen Umfang hat Dreieck 2?', 'Umfang 1: 12 cm. Umfang 2: 12 · 1,5 = 18 cm.',
                                'Alle Seiten mal 1,5 – also auch der Umfang.', 18, '(3 + 4 + 5) * 1.5', einheit='cm')),
        ('aehnlich', 2, O, auswahl('Ein Dreieck hat die Winkel 40° und 60°. Welches Dreieck ist dazu ähnlich?', 'eines mit den Winkeln 80° und 40°',
                                   ['eines mit den Winkeln 40° und 70°', 'eines mit den Winkeln 60° und 90°', 'eines mit den Winkeln 30° und 60°'],
                                   'Der dritte Winkel des ersten ist 80°. 80° und 40° gehören also zum selben Winkelsatz (40°, 60°, 80°).', 'Berechne zuerst jeweils den dritten Winkel.')),
        # strahlensatz1
        ('strahlensatz1', 3, P, zahl('Eine Dachschräge beginnt am Boden. 1 m von dieser Kante entfernt ist sie 60 cm hoch. Wie hoch ist sie 2,5 m von der Kante entfernt?',
                                     'Die Höhe wächst im gleichen Verhältnis wie der Abstand: 2,5 m : 1 m = 2,5. Höhe 60 cm · 2,5 = 150 cm.',
                                     'Die Kante ist der Scheitel S. Abstand und Höhe wachsen mit demselben Faktor.', 150, '60 * 2.5 / 1', einheit='cm')),
        ('strahlensatz1', 3, P, zahl('Es gilt AB ∥ A\'B\'. SA = x, AA\' = 4 cm, SB = 6 cm und BB\' = 8 cm. Berechne x.',
                                     '1. Strahlensatz: SA : AA\' = SB : BB\' ⇒ x : 4 = 6 : 8 ⇒ x = 3 cm. Probe: SA\' = 7, SB\' = 14, 3 : 7 = 6 : 14.',
                                     'Stelle eine Verhältnisgleichung mit x auf und löse sie.', 3, '4 * 6 / 8', einheit='cm')),
        ('strahlensatz1', 3, Kn, zahl('Zwei Strahlen mit Scheitel S werden von drei Parallelen geschnitten. Auf dem ersten Strahl sind die Abschnitte (von S aus) 2 cm, 3 cm und 5 cm lang. Auf dem zweiten Strahl ist der erste Abschnitt 3 cm lang. Wie lang ist der zweite Strahl von S bis zur dritten Parallele?',
                                      'Faktor 3 : 2 = 1,5 gilt für alle Abschnitte. Erster Strahl bis zur 3. Parallele: 2 + 3 + 5 = 10 cm. Zweiter Strahl: 10 · 1,5 = 15 cm.',
                                      'Alle Abschnitte des zweiten Strahls sind 1,5-mal so lang.', 15, '(2 + 3 + 5) * 1.5', einheit='cm')),
        ('strahlensatz1', 3, O, zahl('SA = 4 cm, AA\' = 6 cm, SB = 5 cm. Wie lang muss BB\' sein, damit AB und A\'B\' parallel sind?', 'Es muss SA : AA\' = SB : BB\' gelten: 4 : 6 = 5 : BB\' ⇒ BB\' = 7,5 cm.',
                                     'Umkehrung des Strahlensatzes: Die Verhältnisse müssen gleich sein.', 7.5, '6 * 5 / 4', einheit='cm')),
        ('strahlensatz1', 2, O, zahl('Es gilt AB ∥ A\'B\'. SA = 3 cm, SA\' = 9 cm, SB = 4 cm. Berechne SB\'.', 'Faktor 9 : 3 = 3, also SB\' = 12 cm.', 'Gleicher Faktor auf beiden Strahlen.', 12,
                                     '4 * 9 / 3', einheit='cm')),
        ('strahlensatz1', 2, O, zahl('Es gilt AB ∥ A\'B\'. SA = 2,5 cm, AA\' = 5 cm, SB = 3 cm. Berechne BB\'.', 'AA\' : SA = 2, also BB\' = 2 · 3 = 6 cm.', 'Auch die Abschnitte zwischen den Parallelen stehen im gleichen Verhältnis.',
                                     6, '5 * 3 / 2.5', einheit='cm')),
        # strahlensatz2
        ('strahlensatz2', 3, P, zahl('Eine Münze mit 2 cm Durchmesser verdeckt in 2 m Entfernung vom Auge genau den Vollmond. Der Mond hat etwa 3 500 km Durchmesser. Wie weit ist er ungefähr entfernt (in km)?',
                                     'Durchmesser : Entfernung gleich: 2 cm : 200 cm = 3 500 km : d ⇒ d = 3 500 · 100 = 350 000 km.',
                                     'Auge = Scheitel. Rechne beide Längen der Münze in cm.', 350000, '3500 * 200 / 2', einheit='km')),
        ('strahlensatz2', 3, P, zahl('Ein 1,8 m großer Mensch steht 3 m von einer Straßenlaterne entfernt. Sein Schatten ist 2 m lang. Wie hoch ist die Laterne?',
                                     'Scheitel = Schattenspitze. Abstand zur Laterne 3 + 2 = 5 m. h : 1,8 = 5 : 2 ⇒ h = 4,5 m.',
                                     'Der ganze Abstand von der Schattenspitze zur Laterne zählt, nicht nur 3 m.', 4.5, '1.8 * 5 / 2', einheit='m')),
        ('strahlensatz2', 3, Kn, zahl('Im Trapez ABCD ist AB ∥ CD, AB = 12 cm und CD = 4 cm. Die Verlängerungen von AD und BC schneiden sich in S, und SD = 3 cm. Wie lang ist SA?',
                                      'Mit S als Scheitel ist das eine Strahlensatzfigur: SD : SA = CD : AB = 4 : 12 ⇒ SA = 3 · 3 = 9 cm.',
                                      'Verlängere die Schenkel in Gedanken: Wo ist der Scheitel, wo sind die Parallelen?', 9, '3 * 12 / 4', einheit='cm')),
        ('strahlensatz2', 3, O, zahl('Es gilt AB ∥ A\'B\'. SA = 5 cm, AB = 4 cm, A\'B\' = 7 cm. Berechne AA\'.', 'SA\' = 5 · 7 : 4 = 8,75 cm. AA\' = 8,75 − 5 = 3,75 cm.',
                                     'Erst SA\' mit dem 2. Strahlensatz, dann die Differenz.', 3.75, '5 * 7 / 4 - 5', einheit='cm')),
        ('strahlensatz2', 2, O, zahl('Es gilt AB ∥ A\'B\'. SA = 4 cm, SA\' = 10 cm, AB = 3 cm. Berechne A\'B\'.', 'Faktor 10 : 4 = 2,5. A\'B\' = 3 · 2,5 = 7,5 cm.', 'AB : A\'B\' = SA : SA\'.',
                                     7.5, '3 * 10 / 4', einheit='cm')),
        ('strahlensatz2', 2, O, auswahl('Es gilt AB ∥ A\'B\' mit Scheitel S. Welche Gleichung ist richtig?', "AB : A'B' = SA : SA'", ["AB : A'B' = SA : AA'", "AB : A'B' = AA' : SA'", "AB : SA = A'B' : AA'"],
                                        'Beim 2. Strahlensatz gehören zu den Parallelen immer die ganzen Strecken ab S.', 'Parallelstrecken passen zu Strecken, die bei S beginnen.')),
        # flaeche_volumen
        ('flaeche_volumen', 3, P, auswahl('Ein Kreis wird mit k = 3 zentrisch gestreckt. Welche Aussage stimmt?', 'Der Umfang wird 3-mal, die Fläche 9-mal so groß.',
                                          ['Umfang und Fläche werden 3-mal so groß.', 'Umfang und Fläche werden 9-mal so groß.', 'Der Umfang wird 6-mal, die Fläche 9-mal so groß.'],
                                          'Der Umfang ist eine Länge (u = 2πr): mal k = 3. Die Fläche (A = πr²): mal k² = 9.', 'Länge oder Fläche? Längen mal k, Flächen mal k².')),
        ('flaeche_volumen', 3, P, zahl('Ein Foto (10 cm × 15 cm) wird auf 25 cm × 37,5 cm vergrößert. Wie viel Mal so groß ist die Fläche?', 'k = 25 : 10 = 2,5. Fläche mal k² = 6,25.',
                                       'Bestimme zuerst k, dann quadriere.', 6.25, '2.5 ** 2')),
        ('flaeche_volumen', 3, Kn, zahl('Ein Holzwürfel wiegt 64 g. Ein Würfel aus demselben Holz hat halb so lange Kanten. Wie schwer ist er?', 'k = 0,5, Volumen mal 0,5³ = 1/8: 64 g : 8 = 8 g.',
                                        'Das Gewicht hängt am Volumen.', 8, '64 / 2 ** 3', einheit='g')),
        ('flaeche_volumen', 3, O, zahl('Zwei Flaschen sind ähnlich. Die große ist 1,5-mal so hoch und fasst 1,35 Liter. Wie viel fasst die kleine?', 'Volumen mal 1,5³ = 3,375. Klein: 1,35 : 3,375 = 0,4 Liter.',
                                       'Volumen wächst mit k³.', 0.4, '1.35 / 1.5 ** 3', einheit='l')),
        ('flaeche_volumen', 2, O, zahl('Ein Quadrat mit 9 cm² wird mit k = 4 gestreckt. Welchen Flächeninhalt hat das Bild?', '9 · 4² = 144 cm².', 'Fläche mal k².', 144, '9 * 4 ** 2', einheit='cm²')),
        ('flaeche_volumen', 2, O, zahl('Bei einer Streckung wird die Fläche einer Figur 25-mal so groß. Wie groß ist k (k > 0)?', 'k² = 25, also k = 5.', 'Rückwärts: k² ist der Flächenfaktor.', 5, '25 / 5')),
        # anwendung
        ('anwendung', 3, P, zahl('Ein Verkehrsschild zeigt 12 % Steigung: Auf 100 m waagrechter Strecke steigt die Straße um 12 m. Um wie viele Meter steigt sie auf 350 m waagrechter Strecke?',
                                 'Strahlensatz (Steigungsdreiecke sind ähnlich): 12 : 100 = h : 350 ⇒ h = 42 m.', 'Höhe zu waagrechter Strecke ist überall gleich.', 42, '12 * 350 / 100', einheit='m')),
        ('anwendung', 3, P, zahl('Ein 10 cm langes Lineal wird senkrecht 60 cm vor das Auge gehalten und verdeckt genau einen Turm, der 90 m entfernt ist. Wie hoch ist der Turm? (Die Augenhöhe wird vernachlässigt.)',
                                 '10 cm : 60 cm = h : 90 m ⇒ h = 90 · 10 : 60 = 15 m.', 'Auge = Scheitel. Lineal und Turm sind die Parallelen.', 15, '10 * 90 / 60', einheit='m')),
        ('anwendung', 3, Kn, zahl('Eine 2 m hohe Stange und ein 17 m hoher Turm stehen 30 m auseinander; die Spitzen ihrer Schatten treffen sich in einem Punkt hinter der Stange. Wie lang ist der Schatten der Stange?',
                                  'Schatten der Stange x: 2 : x = 17 : (x + 30) ⇒ 2x + 60 = 17x ⇒ x = 4 m.', 'Die Unbekannte steht im Nenner. Multipliziere über Kreuz.', 4, '60 / 15', einheit='m')),
        ('anwendung', 3, O, zahl('Ein Kind (Augenhöhe 1,6 m) steht 2 m vor einem Spiegel, der auf dem Boden liegt. Darin sieht es genau die Turmspitze. Der Spiegel ist 30 m vom Turm entfernt. Wie hoch ist der Turm?',
                                 'Die beiden Dreiecke (Kind–Spiegel, Turm–Spiegel) sind ähnlich: 1,6 : 2 = h : 30 ⇒ h = 24 m.', 'Höhe zu Abstand vom Spiegel ist auf beiden Seiten gleich.', 24,
                                 '1.6 * 30 / 2', einheit='m')),
        ('anwendung', 2, O, zahl('Ein 1,2 m hoher Pfosten wirft 1,5 m Schatten. Zur selben Zeit wirft ein Haus 12 m Schatten. Wie hoch ist das Haus?', '1,2 : 1,5 = h : 12 ⇒ h = 9,6 m.',
                                 'Höhe zu Schatten ist gleich.', 9.6, '1.2 * 12 / 1.5', einheit='m')),
        ('anwendung', 2, O, zahl('Auf einer Karte im Maßstab 1 : 25 000 sind zwei Orte 8 cm voneinander entfernt. Wie weit ist das in Wirklichkeit (in km)?', '8 cm · 25 000 = 200 000 cm = 2 km.',
                                 '1 km = 100 000 cm.', 2, '8 * 25000 / 100000', einheit='km')),
    ]


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('abbildungen.aehnlichkeit', 13_9_9)
# a) „Strecke P mit Z und k“ ist Routine → Stufe 2 (Stufe 3 bleibt „Zentrum aus P und P' bestimmen“ u. a.)
for _p, _z, _k in [('P(−8 | −6)', 'Z(−2 | −4)', '−3'), ('P(−4 | 0)', 'Z(2 | 2)', '−0,5'), ('P(−6 | −2)', 'Z(−4 | 0)', '1,5'),
                   ('P(−2 | 2)', 'Z(4 | 2)', '−0,5'), ('P(−3 | 0)', 'Z(1 | −4)', '1,5')]:
    BF.stufe('streckung', f'Strecke den Punkt {_p} zentrisch mit dem Zentrum {_z} und k = {_k}. Gib den Bildpunkt P\' an.', 2)
# a) sechsmal derselbe Typ (Modell → Original) auf Stufe 3 → drei davon Stufe 2
for _m, _g in [('1 : 20', '8'), ('1 : 100', '3'), ('1 : 50', '4')]:
    BF.stufe('flaeche_volumen', f'Ein Modell im Maßstab {_m} hat eine Grundfläche von {_g} cm². Wie groß ist die Grundfläche des Originals in m²?', 2)

# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    d = bauen('abbildungen.aehnlichkeit',
          'Zentrische Streckung und Ähnlichkeit verstehen, Strahlensätze anwenden und die Wirkung auf Fläche und Volumen berechnen.',
          ['Zentrische Streckung: Längen · |k|, Flächen · k², Volumina · |k|³.', 'Ähnlich: gleiche Winkel, alle Seiten im gleichen Verhältnis.',
           '1. Strahlensatz: SA : SA\' = SB : SB\'.', '2. Strahlensatz: AB : A\'B\' = SA : SA\' (Strecken ab S!).'],
          [('Streckung und Ähnlichkeit', ['streckung', 'aehnlich']), ('Strahlensätze', ['strahlensatz1', 'strahlensatz2']),
           ('Anwenden', ['flaeche_volumen', 'anwendung'])],
          ETAPPEN, GEN,
          meiden={'streckung': ['P(4 | 3) zentrisch an Z(1 | 2) mit k = 2.'], 'strahlensatz1': ['SA = 3 cm, SA\' = 7,5 cm, SB = 4 cm'],
                  'strahlensatz2': ['SA = 5 cm, AA\' = 3 cm, AB = 4 cm'], 'anwendung': ['2 m langer Stab wirft einen 3 m langen Schatten. Zur gleichen Zeit wirft ein Baum einen 18']},
          offen=['Strahlensatzaufgaben zeigen die Figur jetzt als Zeichnung (f.grafik); der Fragetext nennt nur noch die Maße. Bitte in der App prüfen, ob die Beschriftungen bei spitzen Winkeln gut lesbar sind.'])
    anhaengen(d, 9909, schwer)
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden


# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl9) ----
from _durchsicht_kl9 import Befunde as _DSB, durchsicht  # noqa: E402

DS = _DSB('abbildungen.aehnlichkeit', 19_9_7)
# streckung: Bildpunkt mit k = 2 ist genau das Beispiel der Karte → Stufe 1 (negative und gebrochene k bleiben Stufe 2)
for _t in ('Strecke den Punkt P(5 | −1) zentrisch mit dem Zentrum Z(2 | 1) und k = 2. Gib den Bildpunkt P\' an.',
           'Strecke den Punkt P(−1 | 1) zentrisch mit dem Zentrum Z(−2 | 2) und k = 2. Gib den Bildpunkt P\' an.',
           'Strecke den Punkt P(−3 | 1) zentrisch mit dem Zentrum Z(0 | −1) und k = 2. Gib den Bildpunkt P\' an.'):
    DS.stufe('streckung', _t, 1)
# aehnlich: „ähnlich über Winkel?“ steht viermal auf Stufe 2; die drei gleichen Aufgaben auf Stufe 3 werden durch andere Gedanken ersetzt
DS.ersetze('aehnlich', 'Dreieck 1 hat die Winkel 71° und 30°. Dreieck 2 hat die Winkel 30° und 79°. Sind die Dreiecke ähnlich?',
           DS.A('Zwei gleichschenklige Dreiecke haben beide einen Winkel von 50°. Sind sie sicher ähnlich?', 'Nein: 50° kann Spitzen- oder Basiswinkel sein (50°, 50°, 80° oder 50°, 65°, 65°).',
                ['Ja, ein gleicher Winkel reicht bei gleichschenkligen Dreiecken.', 'Ja, denn alle gleichschenkligen Dreiecke sind ähnlich.', 'Nein, weil die Seitenlängen fehlen.'],
                'Ist 50° der Spitzenwinkel, sind die Basiswinkel je 65°. Ist 50° ein Basiswinkel, ist der Spitzenwinkel 80°. Die Winkel stimmen dann nicht überein.',
                'Wo kann der 50°-Winkel im gleichschenkligen Dreieck liegen?'))
DS.ersetze('aehnlich', 'Dreieck 1 hat die Winkel 25° und 55°. Dreieck 2 hat die Winkel 55° und 105°. Sind die Dreiecke ähnlich?',
           DS.A('Zwei rechtwinklige Dreiecke haben beide einen Winkel von 35°. Sind sie ähnlich?', 'Ja: Beide haben die Winkel 90°, 35° und 55°.',
                ['Nein, dazu bräuchte man drei gleiche Winkel.', 'Nur, wenn auch eine Seite gleich lang ist.', 'Nein, rechtwinklige Dreiecke sind nie ähnlich.'],
                'Neben 90° und 35° bleibt 180° − 90° − 35° = 55°. Zwei gleiche Winkel genügen, der dritte folgt aus der Winkelsumme.',
                'Welche Winkel hat jedes Dreieck insgesamt?'))
DS.ersetze('aehnlich', 'Dreieck 1 hat die Winkel 79° und 72°. Dreieck 2 hat die Winkel 72° und 29°. Sind die Dreiecke ähnlich?',
           DS.Z('Ein Dreieck wird so vergrößert, dass die Seite 8 cm zur Seite 12 cm wird. Um wie viel Prozent wächst der Umfang?', 50, '(12 - 8) / 8 * 100',
                'k = 12 : 8 = 1,5. Alle Seiten wachsen mit 1,5, also auch der Umfang: 1,5-fach heißt 50 % mehr.',
                'Der Umfang ist eine Summe von Seiten. Mit welchem Faktor wächst er?', einheit='%'))
# strahlensatz2: einmal Fehlerfinden auf Stufe 2 (dreimal dieselbe Aufgabe auf Stufe 3)
DS.stufe('strahlensatz2', 'Es gilt AB ∥ A\'B\'. SA = 2 cm, AA\' = 1 cm, AB = 2 cm. Jemand rechnet A\'B\' = 2 · 1 : 2 = 1 cm. Was stimmt?', 2)
# flaeche_volumen: Fläche mal k² ist Stufe 1; Modell im Maßstab wie auf Stufe 2
DS.stufe('flaeche_volumen', 'Ein Quadrat mit 9 cm² wird mit k = 4 gestreckt. Welchen Flächeninhalt hat das Bild?', 1)
DS.stufe('flaeche_volumen', 'Ein Modell im Maßstab 1 : 50 hat eine Grundfläche von 6 cm². Wie groß ist die Grundfläche des Originals in m²?', 2, anzahl=None or 1)
# anwendung: Stab und Schatten ist das Beispiel der Karte → Stufe 1
for _t in ('Ein 2 m langer Stab wirft einen 5 m langen Schatten. Zur gleichen Zeit wirft ein Turm einen 140 m langen Schatten. Wie hoch ist er?',
           'Ein 1 m langer Stab wirft einen 2 m langen Schatten. Zur gleichen Zeit wirft ein Baum einen 38 m langen Schatten. Wie hoch ist er?',
           'Ein 1 m langer Stab wirft einen 2 m langen Schatten. Zur gleichen Zeit wirft ein Mast einen 28 m langen Schatten. Wie hoch ist er?',
           'Ein 1,2 m hoher Pfosten wirft 1,5 m Schatten. Zur selben Zeit wirft ein Haus 12 m Schatten. Wie hoch ist das Haus?'):
    DS.stufe('anwendung', _t, 1)

if __name__ == '__main__':
    durchsicht('abbildungen.aehnlichkeit', DS)


# ---- STUFEN (Zwanzigste Runde, Zweig stufen-kl9) ----
from _stufen_kl9 import Stufen, stufen  # noqa: E402

ST = Stufen('abbildungen.aehnlichkeit', 20_9_7)
Z, A, L = ST.Z, ST.A, ST.L
_P = "P'(□ | □)"

# streckung
ST.stufenleiter('streckung', 'Eine Strecke mit k strecken und einen Bildpunkt mit positivem k bestimmen.',
                'Negatives oder gebrochenes k, k aus zwei Längen bestimmen, Projektor im Sachzusammenhang.',
                'Zentrum rückwärts finden, Streckungen hintereinander, Fehler „vom Ursprung aus“, Bedingung für k, Winkeltreue begründen, mehrteilige Aufgabe.')
ST.typ('streckung', 'Eine Strecke der Länge', 'direkt')
ST.typ('streckung', '/^Strecke den Punkt P\\(\\d+ \\| −?\\d+\\) zentrisch mit dem Zentrum Z\\(\\d+ \\| \\d+\\) und k = \\d+\\./', 'direkt')
ST.typ('streckung', '/^Bei einer zentrischen Streckung (mit Zentrum Z ist|wird eine)/', 'umkehr')
ST.typ('streckung', '/^Strecke /', 'mehrschritt')
ST.typ('streckung', 'P(−3 | −7) wird', 'rueckwaerts')
ST.typ('streckung', 'Ein Dreieck wird zentrisch', 'transfer')
ST.typ('streckung', '/^(Bei einer zentrischen Streckung mit Zentrum Z\\(0|Eine Figur wird)/', 'verknuepfen')
ST.neu('streckung', 'erkennen', A('Was bedeutet ein negativer Streckfaktor, zum Beispiel k = −2?', 'Das Bild liegt auf der anderen Seite des Zentrums, doppelt so weit weg.',
       ['Das Bild wird kleiner.', 'Das Bild wird an der x-Achse gespiegelt.', 'Die Streckung ist nicht erlaubt.'], 'Das Minus dreht die Richtung um, die 2 verdoppelt den Abstand vom Zentrum.', 'Wohin zeigt der Pfeil vom Zentrum aus?'))
ST.neu('streckung', 'einkleidung', Z('Ein Projektor wirft ein 3,6 cm breites Dia auf eine Leinwand. Das Bild ist dort 1,8 m breit. Wie groß ist der Streckfaktor?', 50, '180 / 3.6',
       '1,8 m = 180 cm. k = 180 : 3,6 = 50.', 'Rechne beide Längen in dieselbe Einheit um.'))
ST.neu('streckung', 'fehler', A("Jemand streckt P(5 | 1) mit dem Zentrum Z(1 | 3) und k = 2 und erhält P'(10 | 2). Was stimmt?", "Falsch: Er hat vom Ursprung aus gestreckt; richtig ist P'(9 | −1).",
       ['Richtig.', "Falsch: P'(11 | 5).", "Falsch: P'(6 | 4)."], "Von Z nach P: 4 nach rechts, 2 nach unten. Verdoppelt: 8 nach rechts, 4 nach unten. Von Z aus: (1 + 8 | 3 − 4) = (9 | −1).", 'Geh vom Zentrum aus, nicht vom Ursprung.'))
ST.neu('streckung', 'parameter', Z("Z(0 | 0), P(2 | 3). Für welchen Streckfaktor k liegt der Bildpunkt P' auf der Geraden x = −6?", -3, '-6 / 2',
       "P' = (2k | 3k). 2k = −6 ⇒ k = −3. Dann P'(−6 | −9).", 'Schreib die Koordinaten von P\' mit k.'))
ST.neu('streckung', 'begruenden', A('Stimmt: Bei einer zentrischen Streckung bleiben alle Winkel gleich groß?', 'Ja, Bild und Urbild sind ähnlich; Winkel bleiben gleich.', ['Nein, sie werden mit k malgenommen.', 'Nur bei positivem k.', 'Nein, rechte Winkel werden spitz.'],
       'Die zentrische Streckung ist winkeltreu und streckt alle Längen mit |k|. Deshalb ist das Bild ähnlich zum Urbild.', 'Denk an ein vergrößertes Foto.'))
ST.neu('streckung', 'pruefung', L("Das Dreieck A(1 | 1), B(3 | 1), C(1 | 4) wird mit Z(0 | 0) und k = 2 gestreckt. a) Gib C' an. b) Gib die Flächeninhalte von ABC und A'B'C' an (in Flächeneinheiten).", "a) C'(□ | □); b) □ und □", [2, 8, 3, 12],
       ['2 * 1', '2 * 4', '2 * 3 // 2', '4 * 3'], "a) C'(2 | 8). b) ABC ist rechtwinklig mit Katheten 2 und 3: Fläche 3. Das Bild hat k² = 4-mal so viel: 12.", 'Längen mal 2, Fläche mal 4.'))
ST.knobel('streckung', L('P(3 | 2) wird erst mit dem Zentrum Z₁(0 | 0) und k = 2 gestreckt, das Ergebnis dann mit dem Zentrum Z₂(4 | 0) und k = 0,5. Wo landet P?', _P, [5, 2], ['4 + (6 - 4) // 2', '(4 - 0) // 2'],
          "Erst: (6 | 4). Dann von Z₂(4 | 0): Vektor (2 | 4), halbiert (1 | 2), also (5 | 2). Bemerkenswert: Insgesamt ist P nur um 2 nach rechts verschoben worden. Das gilt für jeden Punkt (x | y): Aus (2x | 2y) wird (4 + 0,5 · (2x − 4) | 0,5 · 2y) = (x + 2 | y).",
          'Rechne beide Streckungen nacheinander.'))
ST.knobel('streckung', Z('Ein Quadrat ABCD mit 4 cm Seite wird mit dem Zentrum A und k = 0,5 gestreckt. Wie viel Prozent des großen Quadrats bedeckt das kleine?', 25, '0.5 ** 2 * 100',
          'Das kleine Quadrat hat die Ecke A gemeinsam und 2 cm Seite, liegt also ganz im großen. Fläche 4 cm² von 16 cm²: 25 %. Allgemein: Fläche mal k² = 0,25.',
          'Zeichne beide Quadrate. Wo liegt das kleine?', einheit='%'))

# aehnlich
ST.stufenleiter('aehnlich', 'Eine Seite einer ähnlichen Figur mit k berechnen und wissen, dass Winkel gleich bleiben.',
                'Winkel prüfen, k aus zwei entsprechenden Seiten bestimmen, Umfänge berechnen.',
                'Fallen bei gleichschenkligen und rechtwinkligen Dreiecken, Prozent beim Umfang, DIN-Format, Rahmen, Fehler „+2 cm“.')
ST.typ('aehnlich', 'Zwei Dreiecke sind ähnlich mit k', 'direkt')
ST.typ('aehnlich', '/^(Dreieck 1 hat die Winkel|Ein Dreieck hat die Seiten|Ein Dreieck hat die Winkel)/', 'mehrschritt')
ST.typ('aehnlich', 'Dreieck 1 hat die Seiten 3 cm', 'einkleidung')
ST.typ('aehnlich', '/^(Dreieck 1 hat die Seiten .* Dreieck 2 ist ähnlich, seine längste|Ein Dreieck wird so|Papierformate|Zwei Dreiecke sind ähnlich\\. Das kleine)/', 'transfer')
ST.typ('aehnlich', '/^Zwei (gleichschenklige|rechtwinklige)/', 'verknuepfen')
ST.typ('aehnlich', '/^(Dreieck 1: |Welche zwei Figuren|Ein Bild \\()/', 'begruenden')
ST.neu('aehnlich', 'erkennen', A('Welche Eigenschaft haben zwei ähnliche Dreiecke immer?', 'Sie haben gleich große Winkel.', ['Sie haben gleich lange Seiten.', 'Sie haben denselben Umfang.', 'Sie haben denselben Flächeninhalt.'],
       'Ähnlich heißt: Alle Längen mit demselben Faktor k, die Winkel bleiben gleich.', 'Denk an ein vergrößertes Foto.'))
ST.neu('aehnlich', 'erkennen', A('Sind zwei beliebige Quadrate immer zueinander ähnlich?', 'Ja, alle Winkel sind 90° und alle Seiten wachsen mit demselben Faktor.', ['Nein, nur gleich große.', 'Nur wenn die Seiten ganzzahlig sind.', 'Nein, nie.'],
       'Quadrat mit Seite a und Quadrat mit Seite b: Faktor k = b : a für alle Seiten.', 'Gibt es einen Faktor für alle Seiten?'))
ST.neu('aehnlich', 'umkehr', Z('Dreieck 2 ist ähnlich zu einem Dreieck mit den Seiten 3 cm, 4 cm und 5 cm und hat den Umfang 30 cm. Wie lang ist seine längste Seite?', 12.5, '5 * 30 / 12',
       'Umfang des ersten: 12 cm. k = 30 : 12 = 2,5. Längste Seite 5 · 2,5 = 12,5 cm.', 'Bestimme k aus den Umfängen.', einheit='cm'))
ST.neu('aehnlich', 'fehler', A('Jemand vergrößert ein Dreieck mit 4 cm, 6 cm und 7 cm, indem er zu jeder Seite 2 cm addiert. Ist das neue Dreieck ähnlich?', 'Nein: 6 : 4, 8 : 6 und 9 : 7 sind verschiedene Faktoren.',
       ['Ja, alle Seiten wurden gleich verändert.', 'Ja, die Winkel bleiben gleich.', 'Nur wenn das Dreieck gleichseitig ist.'], 'Ähnlich heißt malnehmen mit demselben k, nicht addieren. 1,5 ≠ 1,33… ≠ 1,29…', 'Berechne die Verhältnisse der Seiten.'))
ST.knobel('aehnlich', Z('Ein Rechteck ist 2 cm breit und 3 cm lang. Ein ähnliches Rechteck hat 54 cm² Flächeninhalt. Wie lang ist seine kürzere Seite?', 6, '2 * 3',
          'Die Fläche wächst mit k²: 54 : 6 = 9 = k², also k = 3. Kürzere Seite 2 · 3 = 6 cm (und 9 cm). Probe: 6 · 9 = 54.',
          'Wie verändert sich die Fläche, wenn alle Längen mit k malgenommen werden?', einheit='cm'))
ST.knobel('aehnlich', Z('Wie viele verschieden große Dreiecke sind ähnlich zum Dreieck mit den Seiten 3 cm, 4 cm und 5 cm und haben eine Seite der Länge 12 cm?', 3, '3',
          'Die 12 cm können der 3-cm-, der 4-cm- oder der 5-cm-Seite entsprechen: k = 4, k = 3 oder k = 2,4. Das ergibt drei verschieden große Dreiecke (12, 16, 20), (9, 12, 15) und (7,2; 9,6; 12).',
          'Welcher Seite kann die 12 cm entsprechen?'))

# strahlensatz1
ST.stufenleiter('strahlensatz1', 'Mit SA, SA\' und SB die Strecke SB\' berechnen.',
                'Mit AA\' statt SA\', rückwärts SA\' oder BB\', X-Figur, Sachsituation mit Wegen.',
                'Parallelität prüfen (Umkehrung), unbekanntes x, drei Parallelen, Dachschräge, Fehler „AA\' statt SA\'“.')
ST.typ('strahlensatz1', '/^Es gilt AB ∥ A\'B\'\\. SA = [\\d,]+ cm, SA\' = [\\d,]+ cm, SB = [\\d,]+ cm\\. Berechne SB\'/', 'direkt')
ST.typ('strahlensatz1', '/^Es gilt AB ∥ A\'B\'\\. SA = [\\d,]+ cm, AA\' = [\\d,]+ cm, SB = [\\d,]+ cm\\. Berechne (SB|BB)\'/', 'mehrschritt')
ST.typ('strahlensatz1', '/^Es gilt AB ∥ A\'B\'\\. SA = [\\d,]+ cm, SB = /', 'umkehr')
ST.typ('strahlensatz1', 'X-Figur', 'darstellung')
ST.typ('strahlensatz1', '/Sind AB und A\'B\' parallel/', 'begruenden')
ST.typ('strahlensatz1', "Es gilt AB ∥ A'B'. SA' =", 'rueckwaerts')
ST.typ('strahlensatz1', '/^(Eine Dachschräge|Zwei Strahlen)/', 'transfer')
ST.typ('strahlensatz1', '/^(Es gilt AB ∥ A\'B\'\\. SA = x|SA = 4 cm, AA\' = 6 cm)/', 'parameter')
ST.neu('strahlensatz1', 'erkennen', A('Welche Voraussetzung braucht man für den Strahlensatz?', "AB und A'B' sind parallel.", ["AB und A'B' sind gleich lang.", 'S liegt in der Mitte.', 'Die Strahlen stehen senkrecht.'],
       "Nur wenn die Geraden AB und A'B' parallel sind, stimmen die Verhältnisse auf beiden Strahlen überein.", 'Was muss für die beiden Querstrecken gelten?'))
ST.neu('strahlensatz1', 'erkennen', A("Welches Verhältnis ist nach dem 1. Strahlensatz gleich SA' : SA?", "SB' : SB", ["SB : SB'", "A'B' : SA", "BB' : SA"],
       "Auf beiden Strahlen gilt derselbe Faktor: SA' : SA = SB' : SB.", 'Gleiche Reihenfolge auf beiden Strahlen.'))
ST.neu('strahlensatz1', 'einkleidung', Z('Zwei gerade Straßen beginnen an einer Kreuzung. Zwei parallele Querwege verbinden sie. Auf der ersten Straße sind es 200 m bis zum ersten und 300 m bis zum zweiten Querweg, auf der zweiten Straße 240 m bis zum ersten Querweg. Wie weit ist es dort bis zum zweiten?', 360, '240 * 300 // 200',
       'Faktor 300 : 200 = 1,5. 240 · 1,5 = 360 m.', 'Die Kreuzung ist der Scheitel.', einheit='m'))
ST.neu('strahlensatz1', 'fehler', A("Bei SA = 4 cm, AA' = 2 cm, SB = 6 cm rechnet jemand SB' = 6 · 2 : 4 = 3 cm. Was stimmt?", "Falsch: Er hat AA' statt SA' = 6 cm benutzt; SB' = 6 · 6 : 4 = 9 cm.",
       ['Richtig.', "Falsch: SB' = 12 cm.", "Falsch: SB' = 8 cm."], "SA' = SA + AA' = 6 cm. Faktor 6 : 4 = 1,5, also SB' = 9 cm. SB' muss länger als SB sein.", "Was ist der Unterschied zwischen AA' und SA'?"))
ST.knobel('strahlensatz1', Z('Zwei Strahlen mit Scheitel S werden von drei Parallelen geschnitten. Auf dem ersten Strahl sind die Abschnitte (von S aus) 2 cm, 3 cm und x cm lang, auf dem zweiten 3 cm, y cm und 6 cm. Wie groß ist x + y?', 8.5, '4 + 4.5',
          'Alle Abschnitte des zweiten Strahls sind 1,5-mal so lang (3 : 2). Also y = 3 · 1,5 = 4,5 und x = 6 : 1,5 = 4. Summe 8,5.',
          'Vergleiche die ersten Abschnitte.'))
ST.knobel('strahlensatz1', Z('Ein 2 m hoher Zaun steht 1 m vor einer Hauswand. Eine Leiter berührt den Boden, die Oberkante des Zauns und die Wand in 6 m Höhe. Wie weit steht der Fuß der Leiter vom Zaun entfernt?', 0.5, '2 / 4',
          'Abstand x vom Fuß zum Zaun. Strahlensatz am Fußpunkt: 2 : 6 = x : (x + 1). Also 6x = 2x + 2 und x = 0,5 m.',
          'Der Fuß der Leiter ist der Scheitel.', einheit='m'))

# strahlensatz2
ST.stufenleiter('strahlensatz2', 'Mit SA, SA\' und AB die Parallelstrecke A\'B\' berechnen.',
                'SA rückwärts, mit AA\' rechnen, X-Figur, Lampe und Schatten.',
                'AA\' aus den Parallelen, Fehler „AA\' statt SA\'“ und falsche Verhältnisse finden, Mond, Laterne, Trapez.')
ST.typ('strahlensatz2', '/^Es gilt AB ∥ A\'B\'\\. SA = [\\d,]+ cm, SA\' = /', 'direkt')
ST.typ('strahlensatz2', '/Jemand rechnet/', 'fehler')
ST.typ('strahlensatz2', 'Es gilt AB ∥ A\'B\' mit Scheitel S. Welche', 'erkennen')
ST.typ('strahlensatz2', "/^Es gilt AB ∥ A'B'\\. AB = /", 'umkehr')
ST.typ('strahlensatz2', "/^Es gilt AB ∥ A'B'\\. SA = [\\d,]+ cm, AA' = /", 'mehrschritt')
ST.typ('strahlensatz2', "/^Es gilt AB ∥ A'B'\\. SA = [\\d,]+ cm, AB = /", 'rueckwaerts')
ST.typ('strahlensatz2', '/^(Eine Münze|Ein 1,8 m)/', 'transfer')
ST.typ('strahlensatz2', 'Im Trapez', 'verknuepfen')
ST.neu('strahlensatz2', 'erkennen', A("Darf man beim 2. Strahlensatz A'B' : AB = AA' : SA rechnen?", "Nein, es muss SA' : SA heißen.", ['Ja, das ist dasselbe.', 'Nur in der X-Figur.', "Ja, wenn AA' kürzer als SA ist."],
       "Die Parallelstrecken verhalten sich wie die Strecken ab dem Scheitel: A'B' : AB = SA' : SA. AA' beginnt nicht bei S.", 'Beginnen beide Strecken am Scheitel?'))
ST.neu('strahlensatz2', 'einkleidung', Z('Eine Lampe beleuchtet ein 30 cm breites Brett, das 1 m von ihr entfernt ist. Wie breit ist der Schatten an einer Wand 3 m von der Lampe?', 90, '30 * 3',
       'Faktor 3 : 1 = 3. Schatten 30 · 3 = 90 cm.', 'Die Lampe ist der Scheitel.', einheit='cm'))
ST.neu('strahlensatz2', 'darstellung', Z("X-Figur: S liegt zwischen AB und A'B', AB ∥ A'B'. SA = 3 cm, SA' = 6 cm, AB = 4 cm. Berechne A'B'.", 8, '4 * 6 // 3',
       "Auch in der X-Figur gilt A'B' : AB = SA' : SA = 2. A'B' = 8 cm.", 'Die Verhältnisse gelten auch, wenn S zwischen den Parallelen liegt.', einheit='cm'))
ST.neu('strahlensatz2', 'mehrschritt', Z("Es gilt AB ∥ A'B'. SA = 6 cm, AA' = 3 cm, A'B' = 12 cm. Berechne AB.", 8, '12 * 6 // 9',
       "SA' = 9 cm. AB : A'B' = SA : SA' = 6 : 9, also AB = 12 · 6 : 9 = 8 cm.", "Erst SA' bestimmen.", einheit='cm'))
ST.knobel('strahlensatz2', L('Im Trapez ABCD ist AB ∥ CD, AB = 10 cm und CD = 6 cm. Die Diagonalen schneiden sich in M. In welchem Verhältnis teilt M die Diagonale AC? AM : MC =', '□ : □', [5, 3], ['10 // 2', '6 // 2'],
          'Die Dreiecke ABM und CDM bilden eine X-Figur mit Scheitel M und den Parallelen AB und CD. Also AM : MC = AB : CD = 10 : 6 = 5 : 3.',
          'Such eine X-Figur in der Zeichnung.'))
ST.knobel('strahlensatz2', Z('Im Trapez ABCD ist AB ∥ CD, AB = 12 cm, CD = 6 cm. Durch den Schnittpunkt M der Diagonalen wird eine Strecke parallel zu AB von AD bis BC gezogen. Wie lang ist sie?', 8, '2 * 12 * 6 // 18',
          'AM : MC = 12 : 6 = 2 : 1, also AM = 2/3 · AC. Der Teil von AD bis M ist im Dreieck ACD parallel zu CD: Länge 2/3 · 6 = 4. Ebenso von M bis BC im Dreieck BCD: 4. Zusammen 8 cm.',
          'Teile die Strecke im Punkt M in zwei Stücke und nutze zweimal den Strahlensatz.', einheit='cm'))

# flaeche_volumen
ST.stufenleiter('flaeche_volumen', 'Fläche mit k² und Volumen mit k³ verändern.',
                'k aus dem Flächenfaktor finden, Maßstäbe für Flächen, Pizza-Vergleich, Oberfläche nach Volumen.',
                'Volumen im Maßstab umrechnen, Gewichte und Füllmengen ähnlicher Körper, Fehler „doppelt so viel Fläche“, Prozent, mehrteilige Aufgabe.')
ST.typ('flaeche_volumen', '/^(Alle Längen|Ein Quadrat mit|Ein Körper hat)/', 'direkt')
ST.typ('flaeche_volumen', '/^(Eine Figur wird so vergrößert|Bei einer Streckung wird die Fläche)/', 'umkehr')
ST.typ('flaeche_volumen', '/^Ein Modell im Maßstab 1 : \\d+ hat eine Grundfläche/', 'mehrschritt')
ST.typ('flaeche_volumen', 'Ein Modell im Maßstab 1 : 20 hat', 'verknuepfen')
ST.typ('flaeche_volumen', 'Ein Kreis wird', 'begruenden')
ST.typ('flaeche_volumen', '/^(Ein Foto|Ein Holzwürfel|Zwei Flaschen)/', 'transfer')
ST.neu('flaeche_volumen', 'erkennen', A('Mit welchem Faktor ändert sich das Volumen, wenn alle Längen verdreifacht werden?', '27', ['3', '9', '6'],
       'Volumen wächst mit k³ = 3 · 3 · 3 = 27.', 'Drei Richtungen werden verdreifacht.'))
ST.neu('flaeche_volumen', 'einkleidung', Z('Eine runde Pizza hat 30 cm Durchmesser, eine andere 20 cm. Wie viel Mal so viel Fläche hat die große?', 2.25, '1.5 ** 2',
       'Die Pizzen sind ähnlich mit k = 30 : 20 = 1,5. Fläche mal k² = 2,25.', 'Bestimme zuerst k.'))
ST.neu('flaeche_volumen', 'mehrschritt', Z('Ein Würfel wird so vergrößert, dass sein Volumen 27-mal so groß ist. Mit welchem Faktor wächst seine Oberfläche?', 9, '3 ** 2',
       'k³ = 27 heißt k = 3. Die Oberfläche ist eine Fläche: mal k² = 9.', 'Bestimme zuerst k.'))
ST.neu('flaeche_volumen', 'fehler', A('Jemand sagt: „Verdoppelt man alle Seiten eines Rechtecks, verdoppelt sich die Fläche.“ Was stimmt?', 'Falsch: Die Fläche wird 4-mal so groß.', ['Richtig.', 'Falsch: Sie wird 8-mal so groß.', 'Falsch: Sie bleibt gleich.'],
       'Fläche = Länge · Breite; beide werden verdoppelt: 2 · 2 = 4. Beispiel 2 × 3 = 6 wird 4 × 6 = 24.', 'Probiere ein Beispiel.'))
ST.neu('flaeche_volumen', 'parameter', Z('Ein Würfel wird mit dem Faktor k gestreckt. Seine Oberfläche wächst dabei um 300 %. Wie groß ist k?', 2, '2',
       'Um 300 % wachsen heißt auf 400 %, also das 4-Fache. k² = 4, k = 2.', 'Um 300 % mehr ist das Wievielfache?'))
ST.neu('flaeche_volumen', 'pruefung', L('Ein Haus hat 60 m² Grundfläche und 300 m³ Volumen. Ein Modell im Maßstab 1 : 10 wird gebaut. a) Grundfläche des Modells in dm²? b) Volumen des Modells in dm³?', 'a) □ dm²; b) □ dm³', [60, 300],
       ['60 * 100 // 100', '300 * 1000 // 1000'], 'a) Fläche : 100 = 0,6 m² = 60 dm². b) Volumen : 1 000 = 0,3 m³ = 300 dm³.', 'Flächen : k², Volumen : k³.'))
ST.knobel('flaeche_volumen', Z('Ein großer Würfel wird aus gleichen kleinen Würfeln gebaut. Seine Oberfläche ist 9-mal so groß wie die eines kleinen Würfels. Wie viele kleine Würfel sind es?', 27, '3 ** 3',
          'Oberfläche 9-fach heißt k² = 9, also k = 3. Das Volumen ist dann 27-fach: 27 kleine Würfel (3 · 3 · 3).', 'Von der Fläche auf k, dann auf das Volumen.'))
ST.knobel('flaeche_volumen', Z('Zwei ähnliche Kerzen aus demselben Wachs: Die große ist doppelt so hoch. Die kleine brennt 3 Stunden. Wie lange brennt die große, wenn beide pro Stunde gleich viel Wachs verbrauchen?', 24, '3 * 2 ** 3',
          'Die große hat k³ = 8-mal so viel Wachs. Bei gleichem Verbrauch pro Stunde brennt sie 8 · 3 = 24 Stunden.', 'Wie viel mehr Wachs hat die große Kerze?', einheit='h'))

# anwendung
ST.stufenleiter('anwendung', 'Höhe eines Gegenstands aus Stab und Schatten bestimmen.',
                'Daumensprung, Kartenmaßstab, Schatten rückwärts, Höhenunterschied.',
                'Gebäude über den Daumen schätzen, Flussbreite, Mauer und Baum, Spiegel, Schattenspitzen treffen sich, Fehler im Verhältnis.')
ST.typ('anwendung', '/^Ein [\\d,]+ m (langer Stab|hoher Pfosten)/', 'direkt')
ST.typ('anwendung', 'Daumensprung', 'einkleidung')
ST.typ('anwendung', '/^(Auf einer Karte|Ein Verkehrsschild)/', 'einkleidung')
ST.typ('anwendung', '/^(Mit ausgestrecktem Arm|Flussbreite|Ein 10 cm langes Lineal)/', 'transfer')
ST.typ('anwendung', 'Ein Baum steht', 'pruefung')
ST.typ('anwendung', '/^(Eine 2 m hohe Stange|Ein Kind)/', 'verknuepfen')
ST.neu('anwendung', 'erkennen', A('Ein Stab (2 m) wirft 3 m Schatten, ein Baum zur selben Zeit 18 m. Welche Gleichung gilt für die Baumhöhe h?', 'h : 18 = 2 : 3', ['h : 2 = 18 : 3 · 2', 'h : 3 = 18 : 2', 'h = 18 − 3 + 2'],
       'Höhe zu Schatten ist bei beiden gleich: h : 18 = 2 : 3, also h = 12 m.', 'Stelle Höhe zu Schatten gegenüber.'))
ST.neu('anwendung', 'umkehr', Z('Ein Baum ist 9 m hoch und wirft 12 m Schatten. Wie lang ist zur selben Zeit der Schatten eines 1,5 m großen Menschen?', 2, '1.5 * 12 / 9',
       'Schatten : Höhe = 12 : 9. Schatten = 1,5 · 12 : 9 = 2 m.', 'Gesucht ist diesmal der Schatten.', einheit='m'))
ST.neu('anwendung', 'mehrschritt', Z('Ein 1,5 m hoher Stab wirft 2 m Schatten, ein Haus zur selben Zeit 16 m. Wie viel höher als der Stab ist das Haus?', 10.5, '1.5 * 16 / 2 - 1.5',
       'Haushöhe: 1,5 · 16 : 2 = 12 m. Unterschied 12 − 1,5 = 10,5 m.', 'Erst die Haushöhe, dann den Unterschied.', einheit='m'))
ST.neu('anwendung', 'umkehr', Z('Ein Wanderweg ist in Wirklichkeit 6 km lang. Wie lang ist er auf einer Karte im Maßstab 1 : 50 000 (in cm)?', 12, '6 * 100000 // 50000',
       '6 km = 600 000 cm. 600 000 : 50 000 = 12 cm.', 'Rechne km in cm um.', einheit='cm'))
ST.neu('anwendung', 'fehler', A('Stab 2 m, Stabschatten 3 m, Baumschatten 18 m. Jemand rechnet h = 18 · 3 : 2 = 27 m. Was stimmt?', 'Falsch: Das Verhältnis ist vertauscht; h = 18 · 2 : 3 = 12 m.',
       ['Richtig.', 'Falsch: h = 18 − 3 + 2 = 17 m.', 'Falsch: h = 18 : 2 = 9 m.'], 'Der Baum ist höher als sein Schatten, wenn der Stab höher als sein Schatten ist – hier ist der Stab kürzer als sein Schatten, also ist auch h < 18 m.', 'Ist der Stab länger oder kürzer als sein Schatten?'))
ST.knobel('anwendung', Z('Zwei senkrechte Stäbe, 2 m und 3 m hoch, stehen 5 m auseinander. Man spannt Schnüre von der Spitze jedes Stabs zum Fuß des anderen. In welcher Höhe kreuzen sie sich?', 1.2, '2 * 3 / 5',
          'Kreuzung in Höhe h, waagrecht x vom 2-m-Stab. Strahlensatz vom Fuß des 3-m-Stabs: h : 2 = (5 − x) : 5. Vom Fuß des 2-m-Stabs: h : 3 = x : 5. Addiert: h/2 + h/3 = 1, also h = 6/5 = 1,2 m. Der Abstand der Stäbe spielt gar keine Rolle.',
          'Stelle zwei Strahlensätze auf, einen von jedem Fußpunkt aus.', einheit='m'))
ST.knobel('anwendung', Z('Ein 1,6 m großes Kind steht 3 m von einem 4 m hohen Baum entfernt, so dass die Spitzen ihrer Schatten genau zusammenfallen. Wie lang ist der Schatten des Kindes?', 2, '1.6 * 3 / (4 - 1.6)',
          'Schattenlänge s. Strahlensatz an der Schattenspitze: 1,6 : 4 = s : (s + 3). Also 4s = 1,6s + 4,8, 2,4s = 4,8, s = 2 m.', 'Die gemeinsame Schattenspitze ist der Scheitel.', einheit='m'))

if __name__ == '__main__':
    stufen('abbildungen.aehnlichkeit', ST)


# ---- AUFLOESEN (Vierundzwanzigste Runde, Zweig aufloesen, siehe _aufloesen.py und _af_plan.py) ----
if __name__ == '__main__':
    from _aufloesen import aufloesen_datei
    aufloesen_datei('abbildungen.aehnlichkeit')
# ---- AUFLOESEN ENDE ----
