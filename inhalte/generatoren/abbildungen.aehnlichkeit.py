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

if __name__ == '__main__':
    bauen('abbildungen.aehnlichkeit',
          'Zentrische Streckung und Ähnlichkeit verstehen, Strahlensätze anwenden und die Wirkung auf Fläche und Volumen berechnen.',
          ['Zentrische Streckung: Längen · |k|, Flächen · k², Volumina · |k|³.', 'Ähnlich: gleiche Winkel, alle Seiten im gleichen Verhältnis.',
           '1. Strahlensatz: SA : SA\' = SB : SB\'.', '2. Strahlensatz: AB : A\'B\' = SA : SA\' (Strecken ab S!).'],
          [('Streckung und Ähnlichkeit', ['streckung', 'aehnlich']), ('Strahlensätze', ['strahlensatz1', 'strahlensatz2']),
           ('Anwenden', ['flaeche_volumen', 'anwendung'])],
          ETAPPEN, GEN,
          meiden={'streckung': ['P(4 | 3) zentrisch an Z(1 | 2) mit k = 2.'], 'strahlensatz1': ['SA = 3 cm, SA\' = 7,5 cm, SB = 4 cm'],
                  'strahlensatz2': ['SA = 5 cm, AA\' = 3 cm, AB = 4 cm'], 'anwendung': ['2 m langer Stab wirft einen 3 m langen Schatten. Zur gleichen Zeit wirft ein Baum einen 18']},
          offen=['Strahlensatzaufgaben zeigen die Figur jetzt als Zeichnung (f.grafik); der Fragetext nennt nur noch die Maße. Bitte in der App prüfen, ob die Beschriftungen bei spitzen Winkeln gut lesbar sind.'])
