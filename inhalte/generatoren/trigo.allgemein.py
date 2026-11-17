#!/usr/bin/env python3
"""Thema trigo.allgemein – Allgemeine Trigonometrie: Einheitskreis, Sinus- und Kosinussatz, Flächenformel (Klasse 9)."""
import sys
from math import isqrt, sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(912)
# ganzzahlige Dreiecke mit γ = 60° bzw. 120° (Kosinussatz geht glatt auf)
G60 = [(a, b, isqrt(a * a + b * b - a * b)) for a in range(2, 30) for b in range(a + 1, 30)
       if isqrt(a * a + b * b - a * b) ** 2 == a * a + b * b - a * b]
G120 = [(a, b, isqrt(a * a + b * b + a * b)) for a in range(2, 30) for b in range(a + 1, 30)
        if isqrt(a * a + b * b + a * b) ** 2 == a * a + b * b + a * b]
EXAKT = {0: (0, 1), 30: (Fr(1, 2), None), 90: (1, 0), 150: (Fr(1, 2), None), 180: (0, -1), 210: (Fr(-1, 2), None),
         270: (-1, 0), 330: (Fr(-1, 2), None), 60: (None, Fr(1, 2)), 120: (None, Fr(-1, 2)), 240: (None, Fr(-1, 2)), 300: (None, Fr(1, 2)), 360: (0, 1)}


def cf(x):
    return str(float(x)) if Fr(x).denominator != 1 else str(int(x))


ETAPPEN = [
    {'lernziel': 'einheitskreis', 'titel': 'Sinus und Kosinus am Einheitskreis',
     'regel': 'Am ⟦Einheitskreis⟧ (Radius 1) hat der Punkt zum Winkel α die Koordinaten ⟦(cos α | sin α)⟧. So sind sin und cos für alle Winkel von 0° bis 360° erklärt. Es gilt ⟦sin(180° − α) = sin α⟧ und ⟦cos(180° − α) = −cos α⟧.',
     'schritte': ['cos 120°: 120° = 180° − 60°.', 'cos 120° = −cos 60° = ⟦−0,5⟧ (der Punkt liegt links der y-Achse).'],
     'probe': 'sin 120° = sin 60° > 0: Punkt liegt oberhalb der x-Achse ✓',
     'bild': {'typ': 'figur', 'punkte': {'M': [0, 0], '_x1': [-1.3, 0], '_x2': [1.3, 0], '_y1': [0, -1.3], '_y2': [0, 1.3], 'P': [-0.5, 0.866], '_F': [-0.5, 0]}, 'kreise': [{'m': 'M', 'r': 1}], 'linien': [['_x1', '_x2'], ['_y1', '_y2'], ['M', 'P', '1'], ['P', '_F', 'sin 120°', 'gestrichelt'], ['_F', 'M', 'cos 120° = −0,5']], 'winkel': [['M', '_x2', 'P', '120°']]},
     'fehler': '„cos 120° = 0,5, weil cos 60° = 0,5“ ist falsch: Für Winkel zwischen 90° und 180° ist der Kosinus ⟦negativ⟧.'},
    {'lernziel': 'flaeche', 'titel': 'Flächeninhalt mit dem Sinus',
     'regel': 'Kennt man zwei Seiten und den ⟦eingeschlossenen⟧ Winkel, gilt ⟦A = ½ · a · b · sin γ⟧. Warum? Die Höhe auf b ist h = a · sin γ (rechtwinkliges Teildreieck), und A = ½ · b · h.',
     'bild': {'typ': 'figur', 'punkte': {'C': [0, 0], 'A': [9, 0], 'B': [5.196, 3], '_H': [5.196, 0]}, 'flaeche': ['A', 'B', 'C'], 'linien': [['C', 'A', 'b = 9 cm'], ['C', 'B', 'a = 6 cm'], ['A', 'B'], ['B', '_H', 'h', 'gestrichelt']], 'winkel': [['C', 'A', 'B', '30°']], 'rechter_winkel': [['_H', 'A', 'B']]},
     'schritte': ['a = 6 cm, b = 9 cm, γ = 30°: A = ½ · 6 · 9 · sin 30°.', 'A = 27 · 0,5 = ⟦13,5 cm²⟧.'],
     'probe': 'Höhe auf b: h = a · sin γ = 3 cm; A = ½ · 9 · 3 = 13,5 ✓',
     'fehler': 'A = ½ · a · b ohne sin γ gilt nur für γ = 90°. Sonst ist ⟦a · sin γ⟧ die Höhe, nicht a selbst.'},
    {'lernziel': 'sinussatz_seite', 'titel': 'Sinussatz: Seite berechnen',
     'regel': 'In jedem Dreieck gilt der ⟦Sinussatz⟧: ⟦a : sin α = b : sin β = c : sin γ⟧. Warum? Die Höhe h von C auf c lässt sich zweimal ausrechnen: h = b · sin α (links) und h = a · sin β (rechts). Also b · sin α = a · sin β, und daraus folgt a : sin α = b : sin β. Zu jeder Seite gehört der ⟦gegenüberliegende⟧ Winkel.',
     'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [7, 0], 'C': [2.2, 4], '_H': [2.2, 0]}, 'flaeche': ['A', 'B', 'C'], 'linien': [['A', 'B', 'c'], ['B', 'C', 'a'], ['C', 'A', 'b'], ['C', '_H', 'h', 'gestrichelt']], 'winkel': [['A', 'B', 'C', 'α'], ['B', 'C', 'A', 'β'], ['C', 'A', 'B', 'γ']], 'rechter_winkel': [['_H', 'B', 'C']]},
     'schritte': ['α = 40°, β = 75°, a = 8 cm. Gesucht b.', 'b = a · sin β : sin α = 8 · sin 75° : sin 40° ≈ ⟦12,0 cm⟧.'],
     'probe': 'Größerer Winkel β liegt gegenüber der größeren Seite b ✓',
     'fehler': 'b = 8 · sin 40° : sin 75° ist falsch: Zur Seite b gehört der ⟦gegenüberliegende⟧ Winkel β; er gehört in den Zähler.'},
    {'lernziel': 'sinussatz_winkel', 'titel': 'Sinussatz: Winkel berechnen',
     'regel': 'Aus ⟦sin β = b · sin α : a⟧ folgt β. Achtung: Zu einem Sinuswert gibt es zwei Winkel β und ⟦180° − β⟧. Ist die gegebene Gegenseite a die ⟦größere⟧ (a ≥ b), ist β eindeutig spitz.',
     'schritte': ['a = 10 cm, b = 7 cm, α = 50°: sin β = 7 · sin 50° : 10 ≈ 0,5362.', 'β ≈ 32,4° (180° − 32,4° = 147,6° ist zu groß, weil b < a): ⟦β ≈ 32,4°⟧.'],
     'probe': '50° + 32,4° < 180° ✓',
     'fehler': 'Immer nur den spitzen Winkel zu nehmen ist falsch: Ist b > a, kann auch ⟦180° − β⟧ passen – dann gibt es zwei Dreiecke.'},
    {'lernziel': 'kosinussatz_seite', 'titel': 'Kosinussatz: Seite berechnen',
     'regel': 'Kennt man zwei Seiten und den ⟦eingeschlossenen⟧ Winkel, gilt der ⟦Kosinussatz⟧: c² = a² + b² − 2ab · cos γ. Für γ = 90° ist das der Satz des Pythagoras.',
     'schritte': ['a = 5 cm, b = 8 cm, γ = 60°: c² = 25 + 64 − 2 · 5 · 8 · 0,5 = 49.', 'c = ⟦7 cm⟧.'],
     'probe': 'γ = 60° liegt zwischen den anderen Winkeln, c zwischen a und b ✓',
     'fehler': 'c² = 25 + 64 − 2 · 5 · 8 = 9 ist falsch: Der Faktor ⟦cos γ⟧ fehlt. Bei γ = 120° ist cos γ negativ, dann wird c² sogar größer.'},
    {'lernziel': 'kosinussatz_winkel', 'titel': 'Kosinussatz: Winkel berechnen',
     'regel': 'Sind ⟦alle drei Seiten⟧ bekannt, stellst du um: ⟦cos γ = (a² + b² − c²) : (2ab)⟧. Ein negativer Wert bedeutet einen ⟦stumpfen⟧ Winkel – hier ist die Lösung eindeutig.',
     'schritte': ['a = 3 cm, b = 5 cm, c = 7 cm: cos γ = (9 + 25 − 49) : 30 = −0,5.', 'γ = ⟦120°⟧ (stumpf).'],
     'probe': 'c ist die längste Seite, γ der größte Winkel ✓',
     'fehler': 'cos γ = (a² + b² + c²) : (2ab) ist falsch: Das Quadrat der ⟦gegenüberliegenden⟧ Seite wird ⟦subtrahiert⟧.'},
    {'lernziel': 'satz_waehlen', 'titel': 'Welcher Satz passt?',
     'regel': 'Gegeben ⟦SSS⟧ oder ⟦SWS⟧: Kosinussatz. Gegeben ⟦WSW/SWW⟧ oder ⟦SsW⟧ (Seite und Gegenwinkel bekannt): Sinussatz. Fehlt ein Winkel, hilft die ⟦Winkelsumme 180°⟧.',
     'schritte': ['Gegeben: a, b und γ (der Winkel zwischen a und b) – das ist SWS.', 'Erst c mit dem ⟦Kosinussatz⟧, danach die anderen Winkel.'],
     'probe': 'Für den Sinussatz bräuchte man ein Paar aus Seite und Gegenwinkel – das fehlt hier ✓',
     'fehler': 'Bei SWS den Sinussatz zu nehmen geht nicht: Zu keiner gegebenen Seite ist der ⟦gegenüberliegende⟧ Winkel bekannt.'},
]

# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'einheitskreis': {
  'einstieg': 'Der Zeiger einer Uhr ist 1 dm lang und dreht sich um die Mitte. Für jede Stellung kann man fragen: Wie weit ist die Zeigerspitze rechts oder links von der Mitte, wie weit oben oder unten? Diese beiden Abstände sind Kosinus und Sinus des Drehwinkels. Der Kreis mit Radius 1 heißt ⟦Einheitskreis⟧.',
  'woerter': [['Einheitskreis', 'ein Kreis um (0 | 0) mit dem Radius 1'],
              ['Radius', 'der Abstand von der Mitte zum Kreisrand'],
              ['(cos α | sin α)', 'die Koordinaten des Punkts auf dem Kreis zum Winkel α'],
              ['Drehwinkel α', 'gemessen ab der positiven x-Achse, gegen den Uhrzeigersinn'],
              ['180° − α', 'der Winkel, der α zu 180° ergänzt']],
  'bild': {'typ': 'figur', 'punkte': {'M': [0, 0], '_x1': [-1.3, 0], '_x2': [1.3, 0], '_y1': [0, -1.3], '_y2': [0, 1.3], 'P(cos 120° | sin 120°)': [-0.5, 0.866], '_F': [-0.5, 0]}, 'kreise': [{'m': 'M', 'r': 1}], 'linien': [['_x1', '_x2'], ['_y1', '_y2'], ['M', 'P(cos 120° | sin 120°)', 'Radius 1'], ['P(cos 120° | sin 120°)', '_F', 'sin 120° (Höhe)', 'gestrichelt'], ['_F', 'M', 'cos 120° = −0,5']], 'winkel': [['M', '_x2', 'P(cos 120° | sin 120°)', '120°']]},
  'schritte': ['Gesucht ist cos 120°. Der Zeiger ist um 120° gedreht, also über die y-Achse hinaus nach links.',
               '120° = 180° − 60°. Der Punkt liegt gespiegelt zum Punkt bei 60°, nur auf der linken Seite.',
               'Bei 60° ist der Abstand nach rechts cos 60° = 0,5. Links bekommt er ein Minus.',
               'Also cos 120° = −cos 60° = ⟦−0,5⟧.'],
  'regel': 'So liest du am ⟦Einheitskreis⟧ ab: Der Punkt zum Winkel α hat die Koordinaten ⟦(cos α | sin α)⟧. So sind sin und cos für alle Winkel von 0° bis 360° erklärt. Es gilt ⟦sin(180° − α) = sin α⟧ und ⟦cos(180° − α) = −cos α⟧.',
  'fehler': '„cos 120° = 0,5, weil cos 60° = 0,5“ ist falsch: Bei 120° steht der Zeiger links von der Mitte. Für Winkel zwischen 90° und 180° ist der Kosinus ⟦negativ⟧.'},
 'flaeche': {
  'einstieg': 'Ein Bauer hat ein dreieckiges Feld. Zwei Zäune sind 6 m und 9 m lang und treffen sich unter 30°. Wie groß ist das Feld? Für die Formel „½ · Grundseite · Höhe“ fehlt die Höhe. Mit dem Sinus lässt sie sich berechnen – so findet man den ⟦Flächeninhalt mit dem Sinus⟧.',
  'woerter': [['eingeschlossener Winkel', 'der Winkel zwischen den beiden bekannten Seiten'],
              ['Höhe h', 'der senkrechte Abstand von der Spitze zur Grundseite'],
              ['A', 'der Flächeninhalt'],
              ['½', 'ein halb, also 0,5']],
  'bild': {'typ': 'figur', 'punkte': {'C': [0, 0], 'A': [9, 0], 'B': [5.196, 3], '_H': [5.196, 0]}, 'flaeche': ['A', 'B', 'C'], 'linien': [['C', 'A', 'Zaun b = 9 m'], ['C', 'B', 'Zaun a = 6 m'], ['A', 'B'], ['B', '_H', 'Höhe h = a · sin 30°', 'gestrichelt']], 'winkel': [['C', 'A', 'B', '30°']], 'rechter_winkel': [['_H', 'A', 'B']]},
  'schritte': ['Gegeben: a = 6 m, b = 9 m und der eingeschlossene Winkel γ = 30°.',
               'Die Höhe auf b steckt in einem rechtwinkligen Teildreieck: h = a · sin 30° = 6 · 0,5 = 3.',
               'Fläche = ½ · Grundseite · Höhe = ½ · 9 · 3.',
               'Also A = ⟦13,5 m²⟧. Kurz: A = ½ · 6 · 9 · sin 30°.'],
  'probe': '½ · 6 · 9 = 27, und 27 · 0,5 = 13,5 ✓',
  'regel': 'So berechnest du die Fläche: Kennst du zwei Seiten und den ⟦eingeschlossenen⟧ Winkel, gilt ⟦A = ½ · a · b · sin γ⟧. Der Grund: Die Höhe auf b ist h = a · sin γ, und A = ½ · b · h.',
  'fehler': 'A = ½ · a · b ohne sin γ gilt nur für γ = 90°. Sonst steht der Zaun a schräg, und ⟦a · sin γ⟧ ist die Höhe, nicht a selbst.'},
 'sinussatz_seite': {
  'einstieg': 'Zwei Wanderer stehen an den Enden eines Sees und peilen dieselbe Insel an. Sie messen ihre Winkel, aber nicht jede Entfernung. In jedem Dreieck – auch ohne rechten Winkel – passen Seiten und gegenüberliegende Winkel nach einer festen Regel zusammen. Sie heißt ⟦Sinussatz⟧.',
  'woerter': [['Sinussatz', 'a : sin α = b : sin β = c : sin γ'],
              ['gegenüberliegender Winkel', 'der Winkel an der Ecke, die einer Seite gegenüberliegt; zu a gehört α'],
              ['Höhe h', 'der senkrechte Abstand von C zur Seite c'],
              ['allgemeines Dreieck', 'ein Dreieck ohne rechten Winkel']],
  'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [7, 0], 'C': [2.2, 4], '_H': [2.2, 0]}, 'flaeche': ['A', 'B', 'C'], 'linien': [['A', 'B', 'c'], ['B', 'C', 'a (gegenüber α)'], ['C', 'A', 'b (gegenüber β)'], ['C', '_H', 'Höhe h', 'gestrichelt']], 'winkel': [['A', 'B', 'C', 'α'], ['B', 'C', 'A', 'β'], ['C', 'A', 'B', 'γ']], 'rechter_winkel': [['_H', 'B', 'C']]},
  'schritte': ['Gegeben: α = 40°, β = 75°, a = 8 km. Gesucht ist b.',
               'Seite a gehört zu α, Seite b gehört zu β. Sinussatz: b : sin 75° = 8 : sin 40°.',
               'Mit sin 75° malnehmen: b = 8 · sin 75° : sin 40°.',
               'Taschenrechner: b ≈ 8 · 0,966 : 0,643 ≈ ⟦12,0⟧. Die Strecke b ist etwa 12,0 km lang.'],
  'probe': 'Größerer Winkel β liegt gegenüber der größeren Seite b ✓',
  'regel': 'So nutzt du den ⟦Sinussatz⟧: In jedem Dreieck gilt ⟦a : sin α = b : sin β = c : sin γ⟧. Zu jeder Seite gehört der ⟦gegenüberliegende⟧ Winkel. Der Grund: Die Höhe h von C lässt sich zweimal berechnen, h = b · sin α und h = a · sin β.',
  'fehler': 'b = 8 · sin 40° : sin 75° ist falsch: Zur Seite b gehört der ⟦gegenüberliegende⟧ Winkel β; er gehört in den Zähler. Sonst käme b kürzer als a heraus, obwohl β größer ist als α.'},
 'sinussatz_winkel': {
  'einstieg': 'Jetzt kennen die Wanderer zwei Entfernungen und einen Winkel und suchen einen anderen Winkel. Der Sinussatz liefert zuerst den Sinuswert. Aber zu einem Sinuswert gibt es zwei mögliche Winkel – wie zwei Zeigerstellungen auf gleicher Höhe. Man muss prüfen, welcher ⟦Winkel⟧ ins Dreieck passt.',
  'woerter': [['sin⁻¹', 'die Umkehrtaste: Sie macht aus einem Sinuswert einen Winkel zwischen 0° und 90°'],
              ['180° − β', 'der zweite Winkel mit demselben Sinuswert'],
              ['eindeutig', 'es gibt nur eine passende Lösung'],
              ['Winkelsumme', 'alle drei Winkel im Dreieck ergeben zusammen 180°']],
  'schritte': ['Gegeben: a = 10 km, b = 7 km, α = 50°. Gesucht ist β.',
               'Sinussatz umstellen: sin β = b · sin α : a = 7 · sin 50° : 10 ≈ 0,5362.',
               'Umkehrtaste: β ≈ 32,4°. Der zweite Kandidat wäre 180° − 32,4° = 147,6°.',
               'b ist kürzer als a, also muss β kleiner sein als α = 50°. Es bleibt ⟦β ≈ 32,4°⟧.'],
  'regel': 'So berechnest du einen Winkel mit dem Sinussatz: ⟦sin β = b · sin α : a⟧, dann sin⁻¹. Prüfe auch ⟦180° − β⟧. Ist die Seite zum bekannten Winkel die ⟦größere⟧ (a ≥ b), ist β eindeutig spitz.',
  'fehler': 'Immer nur den spitzen Winkel zu nehmen ist falsch: Ist b > a, kann auch ⟦180° − β⟧ passen – dann gibt es zwei verschiedene Dreiecke.'},
 'kosinussatz_seite': {
  'einstieg': 'Von einer Hütte gehen zwei Wege ab: einer 5 km, der andere 8 km lang, sie bilden einen Winkel von 60°. Wie weit liegen die beiden Wegenden auseinander? Pythagoras geht nicht, weil kein rechter Winkel da ist. Dafür gibt es eine erweiterte Regel, den ⟦Kosinussatz⟧.',
  'woerter': [['Kosinussatz', 'c² = a² + b² − 2ab · cos γ'],
              ['eingeschlossener Winkel γ', 'der Winkel zwischen den Seiten a und b'],
              ['2ab', '2 · a · b'],
              ['cos 60°', 'der Kosinuswert von 60°, genau 0,5']],
  'schritte': ['Gegeben: a = 5 km, b = 8 km und der eingeschlossene Winkel γ = 60°.',
               'Kosinussatz: c² = 5² + 8² − 2 · 5 · 8 · cos 60°.',
               'Ausrechnen: c² = 25 + 64 − 80 · 0,5 = 89 − 40 = 49.',
               'Die Wurzel ziehen: c = ⟦7⟧. Die Wegenden liegen 7 km auseinander.'],
  'regel': 'So berechnest du eine Seite: Kennst du zwei Seiten und den ⟦eingeschlossenen⟧ Winkel, nutze den ⟦Kosinussatz⟧: c² = a² + b² − 2ab · cos γ. Für γ = 90° ist cos γ = 0 – dann bleibt der Satz des Pythagoras.',
  'fehler': 'c² = 25 + 64 − 2 · 5 · 8 = 9 ist falsch: Der Faktor ⟦cos γ⟧ fehlt. Bei γ = 120° ist cos γ negativ, dann wird c² sogar größer als a² + b².'},
 'kosinussatz_winkel': {
  'einstieg': 'Drei Stangen von 3 m, 5 m und 7 m werden zu einem Dreieck zusammengesteckt. Welchen Winkel bilden die beiden kürzeren Stangen? Alle Seiten sind bekannt, kein Winkel. Man stellt den Kosinussatz nach dem Kosinus um und kann so den ⟦Winkel berechnen⟧.',
  'woerter': [['cos γ = (a² + b² − c²) : (2ab)', 'der umgestellte Kosinussatz'],
              ['stumpfer Winkel', 'ein Winkel zwischen 90° und 180°'],
              ['cos⁻¹', 'die Umkehrtaste zum Kosinus; sie liefert Winkel bis 180°']],
  'schritte': ['Gegeben: a = 3 m, b = 5 m, c = 7 m. Gesucht ist γ, der Winkel gegenüber von c.',
               'Einsetzen: cos γ = (3² + 5² − 7²) : (2 · 3 · 5) = (9 + 25 − 49) : 30.',
               'Ausrechnen: cos γ = −15 : 30 = −0,5.',
               'Umkehrtaste: γ = cos⁻¹(−0,5) = ⟦120°⟧. Der Winkel ist stumpf.'],
  'regel': 'So berechnest du einen Winkel: Sind ⟦alle drei Seiten⟧ bekannt, stellst du um: ⟦cos γ = (a² + b² − c²) : (2ab)⟧. Ein negativer Wert bedeutet einen ⟦stumpfen⟧ Winkel. Die Lösung ist hier immer eindeutig.',
  'fehler': 'cos γ = (a² + b² + c²) : (2ab) ist falsch: Das Quadrat der ⟦gegenüberliegenden⟧ Seite wird ⟦subtrahiert⟧. Sonst käme cos γ > 1 heraus, was unmöglich ist.'},
 'satz_waehlen': {
  'einstieg': 'Vor jeder Vermessung steht die Frage: Was weiß ich schon? Je nachdem, welche Seiten und Winkel bekannt sind, hilft der eine oder der andere Satz. Mit ein paar Kürzeln lässt sich das schnell entscheiden. So findet man heraus, ⟦welcher Satz passt⟧.',
  'woerter': [['SSS', 'drei Seiten bekannt'],
              ['SWS', 'zwei Seiten und der Winkel dazwischen bekannt'],
              ['WSW / SWW', 'eine Seite und zwei Winkel bekannt'],
              ['SsW', 'zwei Seiten und der Winkel gegenüber der größeren Seite bekannt'],
              ['Seite-Gegenwinkel-Paar', 'eine Seite und der Winkel gegenüber, beide bekannt']],
  'schritte': ['Gegeben sind a, b und γ. Der Winkel γ liegt zwischen a und b.',
               'Das ist der Fall SWS: zwei Seiten und der Winkel dazwischen.',
               'Für den Sinussatz fehlt ein Paar aus Seite und Gegenwinkel.',
               'Also erst c mit dem ⟦Kosinussatz⟧, danach die anderen Winkel.'],
  'regel': 'So wählst du den Satz: Bei ⟦SSS⟧ oder ⟦SWS⟧ den Kosinussatz. Bei ⟦WSW/SWW⟧ oder ⟦SsW⟧ (ein Seite-Gegenwinkel-Paar ist bekannt) den Sinussatz. Fehlt ein Winkel, hilft die ⟦Winkelsumme 180°⟧.',
  'fehler': 'Bei SWS den Sinussatz zu nehmen geht nicht: Zu keiner gegebenen Seite ist der ⟦gegenüberliegende⟧ Winkel bekannt – die Gleichung hätte zwei Unbekannte.'},
}
klar(ETAPPEN, KLAR)
# ---- KLAR ENDE ----
# ---- UMBAU (neues Muster, Runde 8, Vorgabe 16.11.) ----
_EK = {'M': [0, 0], '_x1': [-1.3, 0], '_x2': [1.3, 0], '_y1': [0, -1.3], '_y2': [0, 1.3], 'P': [-0.5, 0.866], '_F': [-0.5, 0], '_Q': [0.5, 0.866]}
_EKL = [['_x1', '_x2'], ['_y1', '_y2'], ['M', 'P', '1']]
_FL = {'C': [0, 0], 'A': [9, 0], 'B': [5.196, 3], '_H': [5.196, 0]}
def _fl(*extra): return [['C', 'A', 'b = 9 m'], ['C', 'B', 'a = 6 m'], ['A', 'B']] + list(extra)
_S = {'A': [0, 0], 'B': [11.28, 0], 'C': [9.21, 7.73]}
def _s(b): return [['A', 'B', 'c'], ['B', 'C', 'a = 8 km'], ['C', 'A', b]]
_W = {'A': [0, 0], 'B': [12.94, 0], 'C': [4.5, 5.36]}
_K1 = {'C': [0, 0], 'A': [8, 0], 'B': [2.5, 4.33]}
def _k1(c): return [['C', 'A', 'b = 8 km'], ['C', 'B', 'a = 5 km'], ['A', 'B', c]]
_K2 = {'C': [0, 0], 'A': [5, 0], 'B': [-1.5, 2.598]}
UMBAU = {
 'einheitskreis': {
  'einstieg': 'Ein 1 dm langer Uhrzeiger dreht sich um die Mitte. Wie weit ist die Spitze rechts oder links, oben oder unten? Das zeigt der ⟦Einheitskreis⟧.',
  'woerter': [['Einheitskreis', 'ein Kreis um (0 | 0) mit dem Radius 1'],
              ['(cos α | sin α)', 'die Koordinaten der Zeigerspitze beim Winkel α']],
  'bild': {'typ': 'figur', 'punkte': _EK, 'kreise': [{'m': 'M', 'r': 1}], 'linien': _EKL, 'winkel': [['M', '_x2', 'P', '120°']]},
  'schritte': [{'text': 'Die Spitze beim Winkel α hat die Koordinaten (cos α | sin α).'},
               {'text': 'Gesucht ist cos 120°. Der Zeiger steht links oben.'},
               {'text': '120° = 180° − 60°: das Spiegelbild der 60°-Stellung.',
                'bild': {'linien': _EKL + [['M', '_Q', '60°', 'gestrichelt']]}},
               {'text': 'Bei 60° ist der Abstand nach rechts 0,5. Links kommt ein Minus dazu.'},
               {'text': 'Also cos 120° = ⟦−0,5⟧.',
                'bild': {'linien': [['_x1', '_x2'], ['_y1', '_y2'], ['M', 'P', ''], ['P', '_F', 'sin 120°', 'gestrichelt'], ['_F', 'M', '−0,5']]}}],
  'fehler': 'cos 120° ist nicht 0,5. Bei 120° steht der Zeiger links von der Mitte. Dort ist der Kosinus negativ.',
  'regel': 'Der Punkt zum Winkel α ist ⟦(cos α | sin α)⟧. Dazu: sin(180° − α) = sin α, cos(180° − α) = −cos α.'},
 'flaeche': {
  'einstieg': 'Ein Feld ist dreieckig. Zwei Zäune sind 6 m und 9 m lang und treffen sich unter 30°. Mit dem Sinus findest du die Höhe und den ⟦Flächeninhalt⟧.',
  'woerter': [['eingeschlossener Winkel', 'der Winkel zwischen den beiden bekannten Seiten'],
              ['Höhe h', 'der senkrechte Abstand der Spitze von der Grundseite']],
  'bild': {'typ': 'figur', 'punkte': _FL, 'flaeche': ['A', 'B', 'C'], 'linien': _fl(), 'winkel': [['C', 'A', 'B', '30°']]},
  'schritte': [{'text': 'Zäune a = 6 m und b = 9 m, eingeschlossener Winkel 30°.'},
               {'text': 'Höhe h auf b: h = 6 · sin 30° = 3 m.',
                'bild': {'linien': _fl(['B', '_H', 'h = 3 m', 'gestrichelt']), 'rechter_winkel': [['_H', 'A', 'B']]}},
               {'text': 'Fläche: A = 1/2 · 9 · 3 = ⟦13,5 m²⟧.'}],
  'fehler': 'A = 1/2 · 6 · 9 = 27 m² stimmt nur bei 90°. Hier steht der Zaun schräg, die Höhe ist nur 3 m.',
  'regel': 'Es gilt ⟦A = 1/2 · a · b · sin γ⟧. Dabei ist γ der Winkel zwischen a und b.'},
 'sinussatz_seite': {
  'einstieg': 'Zwei Wanderer an den Enden eines Sees peilen dieselbe Insel an. Sie messen Winkel, aber nicht alle Entfernungen. Im Dreieck hilft der ⟦Sinussatz⟧.',
  'woerter': [['Sinussatz', 'a : sin α = b : sin β = c : sin γ'],
              ['gegenüberliegende Winkel', 'der Winkel an der Ecke gegenüber einer Seite; zu a gehört α']],
  'bild': {'typ': 'figur', 'punkte': _S, 'flaeche': ['A', 'B', 'C'], 'linien': _s('b = ?'),
           'winkel': [['A', 'B', 'C', '40°'], ['B', 'C', 'A', '75°']]},
  'schritte': [{'text': 'Gegeben: α = 40°, β = 75°, a = 8 km. Gesucht ist b.'},
               {'text': 'Zu a gehört der gegenüberliegende Winkel α, zu b gehört β.'},
               {'text': 'Sinussatz: b : sin 75° = 8 : sin 40°.'},
               {'text': 'b = 8 · sin 75° : sin 40° ≈ ⟦12,0 km⟧.', 'bild': {'linien': _s('b = 12,0 km')}}],
  'fehler': 'b = 8 · sin 40° : sin 75° vertauscht die Winkel. Zu b gehört β. Größerer Winkel heißt längere Seite.',
  'fehler_bild': {'linien': _s('b = 5,3?')},
  'regel': 'Es gilt ⟦a : sin α = b : sin β⟧. Zu jeder Seite gehört der gegenüberliegende Winkel.'},
 'sinussatz_winkel': {
  'einstieg': 'Jetzt kennst du zwei Entfernungen und einen Winkel. Der Sinussatz liefert einen Sinuswert. Dazu passen zwei Winkel: Du wählst den ⟦passenden Winkel⟧.',
  'woerter': [['sin⁻¹', 'die Umkehrtaste: Sie macht aus einem Sinuswert einen Winkel bis 90°'],
              ['180° − β', 'der zweite Winkel mit demselben Sinuswert']],
  'bild': {'typ': 'figur', 'punkte': _W, 'flaeche': ['A', 'B', 'C'],
           'linien': [['A', 'B', 'c'], ['B', 'C', 'a = 10 km'], ['C', 'A', 'b = 7 km']], 'winkel': [['A', 'B', 'C', '50°'], ['B', 'C', 'A', 'β = ?']]},
  'schritte': [{'text': 'Gegeben: a = 10 km, b = 7 km, α = 50°. Gesucht: β.'},
               {'text': 'sin β = 7 · sin 50° : 10 ≈ 0,536.'},
               {'text': 'sin⁻¹ liefert 32,4°. Auch 180° − β = 147,6° hat diesen Sinus.'},
               {'text': 'b ist kürzer als a, also β < 50°: ⟦β ≈ 32,4°⟧.',
                'bild': {'winkel': [['A', 'B', 'C', '50°'], ['B', 'C', 'A', '32,4°']]}}],
  'fehler': 'Nicht immer nur den spitzen Winkel nehmen. Ist b > a, kann auch 180° − β passen. Dann gibt es zwei Dreiecke.',
  'regel': 'sin β ausrechnen, dann ⟦180° − β prüfen⟧. Ist a ≥ b, ist β spitz.'},
 'kosinussatz_seite': {
  'einstieg': 'Von einer Hütte führen zwei Wege, 5 km und 8 km lang. Sie bilden einen Winkel von 60°. Wie weit liegen die Enden auseinander? Hier hilft der ⟦Kosinussatz⟧.',
  'woerter': [['Kosinussatz', 'c² = a² + b² − 2ab · cos γ'],
              ['eingeschlossener Winkel γ', 'der Winkel zwischen a und b'],
              ['Drehwinkel', 'um so viel Grad ändert ein Schiff am Wendepunkt seine Richtung']],
  'bild': {'typ': 'figur', 'punkte': _K1, 'flaeche': ['A', 'B', 'C'], 'linien': _k1('c = ?'), 'winkel': [['C', 'A', 'B', '60°']]},
  'schritte': [{'text': 'a = 5 km, b = 8 km, eingeschlossener Winkel γ = 60°.'},
               {'text': 'Kosinussatz: c² = 5² + 8² − 2 · 5 · 8 · cos 60°.'},
               {'text': 'Mit cos 60° = 0,5: c² = 25 + 64 − 40 = 49.'},
               {'text': 'Also ⟦c = 7 km⟧.', 'bild': {'linien': _k1('c = 7 km')}},
               # Fünfzehnte Runde: Kurs-/Schiff-Aufgaben – Dreieckswinkel = 180° − Drehwinkel
               {'text': 'Schiff: Drehwinkel 50°. Der Dreieckswinkel am Wendepunkt ist ⟦180° − 50° = 130°⟧.',
                'bild': {'punkte': {'Start': [0, 0], 'W': [5, 0], '_V': [8, 0], 'Ziel': [7.57, 3.06]}, 'flaeche': ['Start', 'W', 'Ziel'],
                         'linien': [['Start', 'W', '5 km'], ['W', '_V', '', 'gestrichelt'], ['W', 'Ziel', '4 km'], ['Start', 'Ziel', '?']],
                         'winkel': [['W', '_V', 'Ziel', '50°'], ['W', 'Ziel', 'Start', '130°']]}}],
  'fehler': 'c² = 25 + 64 − 80 = 9 ist falsch. Der Faktor cos 60° = 0,5 fehlt.',
  # vollständig angegeben, weil das Bild des letzten Schritts (Schiff) sonst mit übernommen würde; Anzeige wie bisher
  'fehler_bild': {'punkte': _K1, 'flaeche': ['A', 'B', 'C'], 'linien': _k1('c = 3? zu kurz'), 'winkel': [['C', 'A', 'B', '60°']]},
  'regel': 'Es gilt ⟦c² = a² + b² − 2ab · cos γ⟧. Bei γ = 90° ist das Pythagoras.'},
 'kosinussatz_winkel': {
  'einstieg': 'Drei Stangen von 3 m, 5 m und 7 m werden zum Dreieck gesteckt. Welchen Winkel bilden die kurzen Stangen? Du stellst um und ⟦berechnest den Winkel⟧.',
  'woerter': [['stumpf', 'größer als 90°'],
              ['cos⁻¹', 'die Umkehrtaste zum Kosinus; sie liefert Winkel bis 180°']],
  'bild': {'typ': 'figur', 'punkte': _K2, 'flaeche': ['A', 'B', 'C'],
           'linien': [['C', 'A', 'b = 5 m'], ['C', 'B', 'a = 3 m'], ['A', 'B', 'c = 7 m']], 'winkel': [['C', 'A', 'B', 'γ = ?']]},
  'schritte': [{'text': 'a = 3, b = 5, c = 7. Gesucht ist γ gegenüber von c.'},
               {'text': 'cos γ = (9 + 25 − 49) : 30.'},
               {'text': 'Also cos γ = −15 : 30 = −0,5.'},
               {'text': 'cos⁻¹(−0,5) = ⟦120°⟧, ein stumpfer Winkel.', 'bild': {'winkel': [['C', 'A', 'B', '120°']]}}],
  'fehler': 'Das c² wird nicht addiert. Mit + 49 käme cos γ größer als 1 heraus, und das gibt es nicht.',
  'regel': 'Drei Seiten: ⟦cos γ = (a² + b² − c²) : 2ab⟧. Ist cos γ negativ, ist γ stumpf.'},
 'satz_waehlen': {
  'einstieg': 'Vor jeder Vermessung fragst du: Was weiß ich schon? Je nach bekannten Seiten und Winkeln hilft ein anderer Satz. Kürzel helfen beim ⟦Wählen⟧.',
  'woerter': [['SSS', 'drei Seiten bekannt'],
              ['SWS', 'zwei Seiten und der Winkel dazwischen bekannt'],
              ['SsW', 'zwei Seiten und der Winkel gegenüber der größeren bekannt']],
  'bild': {'typ': 'tabelle', 'kopf': ['gegeben', 'Satz'], 'zeilen': [['SSS', '?'], ['SWS', '?'], ['SsW, WSW', '?']]},
  'schritte': [{'text': 'SSS oder SWS: Hier hilft der Kosinussatz.',
                'bild': {'zeilen': [['SSS', 'Kosinussatz'], ['SWS', 'Kosinussatz'], ['SsW, WSW', '?']]}},
               {'text': 'Ist eine Seite mit Gegenwinkel bekannt, etwa bei SsW: Sinussatz.',
                'bild': {'zeilen': [['SSS', 'Kosinussatz'], ['SWS', 'Kosinussatz'], ['SsW, WSW', 'Sinussatz']]}},
               {'text': 'Gegeben a, b und γ zwischen ihnen: SWS, also ⟦Kosinussatz⟧.'}],
  'fehler': 'Bei SWS geht der Sinussatz nicht. Zu keiner gegebenen Seite ist der Gegenwinkel bekannt.',
  'regel': 'SSS und SWS: ⟦Kosinussatz⟧. Ist eine Seite mit Gegenwinkel bekannt: Sinussatz.'},
}
umbau(ETAPPEN, UMBAU)
# ---- UMBAU ENDE ----


def ekreis(w):
    import math
    x, y = round(math.cos(math.radians(w)), 3), round(math.sin(math.radians(w)), 3)
    return {'typ': 'figur', 'punkte': {'M': [0, 0], '_x1': [-1.3, 0], '_x2': [1.3, 0], '_y1': [0, -1.3], '_y2': [0, 1.3], 'P': [x, y], '_F': [x, 0]},
            'kreise': [{'m': 'M', 'r': 1}], 'linien': [['_x1', '_x2'], ['_y1', '_y2'], ['M', 'P'], ['P', '_F', '', 'gestrichelt']],
            'winkel': [['M', '_x2', 'P', f'{w}°']]}


def g_einheitskreis(s):
    if s == 1:
        w = R.choice([0, 30, 90, 150, 180, 210, 270, 330, 60, 120, 240, 300, 360])
        sn, cs = EXAKT[w]
        f, v = ('sin', sn) if sn is not None else ('cos', cs)
        if sn is not None and cs is not None and R.random() < 0.5: f, v = 'cos', cs
        return zahl(f'Gib den exakten Wert von {f} {w}° an.', f'Am Einheitskreis: {f} {w}° = {dz(v)}.',
                    'Wo liegt der Punkt zum Winkel auf dem Einheitskreis? Nutze 30°, 60° und die Symmetrie.', v, cf(v))
    if s == 2:
        typ = R.random()
        al = R.randint(5, 85)
        if typ < 0.2:
            w = R.choice([0, 90, 180, 270, 360])
            x, y = EXAKT[w][1], EXAKT[w][0]
            return luecken(f'Gib den Punkt zum Winkel {w}° am Einheitskreis an.', 'P(□ | □)', 'x- und y-Koordinate', [x, y],
                           f'P(cos {w}° | sin {w}°) = P({dz(x)} | {dz(y)}).', 'Der Punkt hat die Koordinaten (cos α | sin α). Wo landet man nach einer Drehung um ' + str(w) + '°?',
                           c=[str(x), str(y)])
        if typ < 0.45:
            w = R.choice([x for x in range(100, 351, 10) if x % 90])
            f = R.choice(['sin', 'cos'])
            v = round((sin if f == 'sin' else cos)(w), 2)
            andere = round((cos if f == 'sin' else sin)(w), 2)
            if abs(abs(v) - abs(andere)) < 0.05 or abs(v) < 0.1: return None
            return bild(auswahl(f'Im Bild siehst du den Punkt P zum Winkel {w}° am Einheitskreis. Welcher Wert passt zu {f} {w}°?', dz(v),
                                [dz(-v), dz(andere), dz(round(-1.3 if v < 0 else 1.3, 1))],
                                f'{f} {w}° ist die {"y" if f == "sin" else "x"}-Koordinate von P. P liegt {"oberhalb" if sin(w) > 0 else "unterhalb"} der x-Achse und {"rechts" if cos(w) > 0 else "links"} der y-Achse; |{f} {w}°| ≈ {dz(abs(v))}.',
                                'sin = y-Koordinate, cos = x-Koordinate. Achte auf das Vorzeichen und darauf, dass die Werte zwischen −1 und 1 liegen.'), ekreis(w))
        if typ < 0.6:
            return zahl(f'Welcher zweite Winkel zwischen 0° und 180° hat denselben Sinuswert wie {al}°?', f'sin(180° − α) = sin α: 180° − {al}° = {180 - al}°.',
                        'Spiegle am Einheitskreis an der y-Achse.', 180 - al, f'180 - {al}', einheit='°')
        if typ < 0.8:
            w = 180 - al
            return luecken(f'Ergänze: cos {w}° = −cos □°.', 'cos ' + str(w) + '° = −cos □°', 'Winkel in Grad', [al],
                           f'cos(180° − α) = −cos α mit α = {al}°: cos {w}° = −cos {al}°.', 'Schreibe den Winkel als 180° − α.', c=[f'180 - {w}'])
        w = R.choice(range(0, 361, 5)) if R.random() < 0.25 else R.choice(range(5, 356, 5))
        f = R.choice(['sin', 'cos'])
        if w % 90 == 0:
            val = (EXAKT[w][0] if f == 'sin' else EXAKT[w][1])
            r = 'positiv' if val > 0 else 'negativ' if val < 0 else 'null'
            return auswahl(f'Welches Vorzeichen hat {f} {w}°?', r, ['positiv', 'negativ', 'null'],
                           f'Der Punkt zu {w}° liegt auf einer Achse: {f} {w}° = {dz(val)}.', 'sin = y-Koordinate, cos = x-Koordinate.')
        q = (w // 90) + 1
        pos = (f == 'sin' and q in (1, 2)) or (f == 'cos' and q in (1, 4))
        return auswahl(f'Welches Vorzeichen hat {f} {w}°?', 'positiv' if pos else 'negativ', ['positiv', 'negativ', 'null'],
                       f'{w}° liegt im {q}. Quadranten; dort ist {"die y-" if f == "sin" else "die x-"}Koordinate {"positiv" if pos else "negativ"}.',
                       'In welchem Quadranten liegt der Punkt? sin = y-Koordinate, cos = x-Koordinate.')
    typ = R.random()
    if typ < 0.45:
        al = R.randint(5, 85)
        art = R.choice(['180p', '180m', '360m'])
        f = R.choice(['sin', 'cos'])
        w = {'180p': 180 + al, '180m': 180 - al, '360m': 360 - al}[art]
        vz = {('sin', '180p'): -1, ('cos', '180p'): -1, ('sin', '180m'): 1, ('cos', '180m'): -1, ('sin', '360m'): -1, ('cos', '360m'): 1}[(f, art)]
        beh = R.choice([1, -1])
        richtig = beh == vz
        rel = f'{f} {w}° = {"" if beh == 1 else "−"}{f} {al}°'
        return auswahl(f'Stimmt die Aussage {rel}?', 'Ja.' if richtig else f'Nein, {f} {w}° = {"" if vz == 1 else "−"}{f} {al}°.',
                       ['Ja.' if not richtig else f'Nein, {f} {w}° = {"−" if vz == 1 else ""}{f} {al}°.', 'Das hängt vom Taschenrechner ab.', f'Nein, {f} {w}° = {f} {90 - al}°.'],
                       f'Der Punkt zu {w}° entsteht aus dem Punkt zu {al}° durch Spiegeln {"am Ursprung" if art == "180p" else "an der y-Achse" if art == "180m" else "an der x-Achse"}. '
                       f'Dabei {"bleibt" if vz == 1 else "wechselt"} das Vorzeichen der {"y" if f == "sin" else "x"}-Koordinate: {f} {w}° = {"" if vz == 1 else "−"}{f} {al}°.',
                       'Spiegle den Punkt am Einheitskreis und vergleiche die Koordinaten.')
    if typ < 0.75:
        al = R.randint(91, 179)
        return auswahl(f'Jemand sagt: „cos {al}° ist positiv, weil {al}° ein Winkel im Dreieck sein kann.“ Was stimmt?',
                       f'Falsch: {al}° ist stumpf, der Punkt liegt links der y-Achse, cos {al}° < 0.',
                       ['Richtig.', f'Falsch: cos {al}° = 0.', f'Falsch: cos {al}° ist nicht definiert.'],
                       f'Für 90° < α < 180° ist die x-Koordinate am Einheitskreis negativ: cos {al}° = −cos {180 - al}° < 0.',
                       'Wo liegt der Punkt zu einem stumpfen Winkel am Einheitskreis?')
    al = R.randint(5, 85)
    return zahl(f'Es gilt sin {al}° ≈ {dz(round(sin(al), 4))}. Wie groß ist sin {180 + al}° (vier Nachkommastellen)?',
                f'Der Punkt zu {180 + al}° ist der am Ursprung gespiegelte Punkt zu {al}°: sin {180 + al}° = −sin {al}° ≈ {dz(-round(sin(al), 4))}.',
                'Punktspiegelung am Ursprung ändert das Vorzeichen beider Koordinaten.', -round(sin(al), 4), f'-{round(sin(al), 4)}')


def g_flaeche(s):
    a, b = R.randint(3, 15), R.randint(3, 15)
    if s == 1:
        g = R.choice([30, 150, 90])
        A = Fr(a * b, 2) * (Fr(1, 2) if g != 90 else 1)
        return zahl(f'Ein Dreieck hat a = {a} cm, b = {b} cm und den eingeschlossenen Winkel γ = {g}°. Berechne den Flächeninhalt.',
                    f'A = ½ · {a} · {b} · sin {g}° = {dz(Fr(a * b, 2))} · {dz(Fr(1, 2) if g != 90 else 1)} = {dz(A)} cm².',
                    'Formel A = ½ · a · b · sin γ; sin 30° = sin 150° = 0,5.' if g != 90 else 'Formel A = ½ · a · b · sin γ; sin 90° = 1 – das ist die bekannte Formel ½ · Grundseite · Höhe.',
                    A, f'0.5 * {a} * {b} * {"0.5" if g != 90 else "1"}', einheit='cm²')
    g = R.randint(20, 160)
    if s == 2:
        wahr = 0.5 * a * b * sin(g)
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Ein Dreieck hat a = {a} cm, b = {b} cm und γ = {g}°. Berechne den Flächeninhalt (auf eine Nachkommastelle).',
                    f'A = ½ · {a} · {b} · sin {g}° ≈ {dz(v)} cm².', 'Zwei Seiten und der eingeschlossene Winkel.', v,
                    f'round(0.5 * {a} * {b} * {K(sin(g))}, 1)', einheit='cm²')
    typ = R.random()
    if typ < 0.3:
        if R.random() < 0.5:
            A = Fr(a * b, 4)
            if not endlich(A): return None
            return zahl(f'Ein Dreieck hat a = {a} cm, b = {b} cm und den Flächeninhalt {dz(A)} cm². Wie groß ist der spitze Winkel γ zwischen a und b?',
                        f'{dz(A)} = ½ · {a} · {b} · sin γ ⇒ sin γ = {dz(A)} : {dz(Fr(a * b, 2))} = 0,5 ⇒ γ = 30° (spitz).',
                        'Stelle die Flächenformel nach sin γ um.', 30, '30', einheit='°')
        A = Fr(a * b, 4)
        if not endlich(A): return None
        return zahl(f'Ein Dreieck hat a = {a} cm, γ = 30° und den Flächeninhalt {dz(A)} cm². Berechne b.',
                    f'{dz(A)} = ½ · {a} · b · 0,5 = {dz(Fr(a, 4))} · b ⇒ b = {b} cm.', 'Setze sin 30° = 0,5 ein und stelle nach b um.', b,
                    f'{float(A)} / ({a} / 4)', einheit='cm')
    if typ < 0.6:
        A = R.randint(10, 60)
        wahr = 2 * A / (a * sin(g))
        v = gerundet(wahr, 1)
        if v is None or wahr > 100: return None
        return zahl(f'Ein Dreieck hat den Flächeninhalt {A} cm², die Seite a = {a} cm und γ = {g}°. Wie lang ist b (auf eine Nachkommastelle)?',
                    f'{A} = ½ · {a} · b · sin {g}° ⇒ b = 2 · {A} : ({a} · sin {g}°) ≈ {dz(v)} cm.', 'Stelle die Flächenformel nach b um.', v,
                    f'round(2 * {A} / ({a} * {K(sin(g))}), 1)', einheit='cm')
    w = R.randint(30, 150)
    wahr = a * b * sin(w)
    v = gerundet(wahr, 1)
    if v is None: return None
    return zahl(f'Ein Parallelogramm hat die Seiten {a} cm und {b} cm, die einen Winkel von {w}° einschließen. Berechne den Flächeninhalt (auf eine Nachkommastelle).',
                f'Die Diagonale teilt es in zwei gleiche Dreiecke: A = 2 · ½ · {a} · {b} · sin {w}° ≈ {dz(v)} cm².', 'Ein Parallelogramm besteht aus zwei kongruenten Dreiecken.',
                v, f'round({a} * {b} * {K(sin(w))}, 1)', einheit='cm²')


def g_sinussatz_seite(s):
    al, be = R.randint(20, 100), R.randint(20, 100)
    ga = 180 - al - be
    if ga < 10: return None
    a = R.randint(3, 15)
    if s == 1:
        wahr = a * sin(be) / sin(al)
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Im Dreieck ABC ist α = {al}°, β = {be}° und a = {a} cm. Berechne b (auf eine Nachkommastelle).',
                    f'b : sin β = a : sin α ⇒ b = {a} · sin {be}° : sin {al}° ≈ {dz(v)} cm.', 'Sinussatz: Seite und Gegenwinkel bilden ein Paar.', v,
                    f'round({a} * {K(sin(be))} / {K(sin(al))}, 1)', einheit='cm')
    wahr = a * sin(ga) / sin(al)
    v = gerundet(wahr, 1)
    if v is None: return None
    if s == 2:
        return zahl(f'Im Dreieck ABC ist α = {al}°, β = {be}° und a = {a} cm. Berechne c (auf eine Nachkommastelle).',
                    f'γ = 180° − {al}° − {be}° = {ga}°. c = {a} · sin {ga}° : sin {al}° ≈ {dz(v)} cm.', 'Berechne zuerst γ mit der Winkelsumme.', v,
                    f'round({a} * {K(sin(ga))} / {K(sin(al))}, 1)', einheit='cm')
    if R.random() < 0.35:
        al, be = R.randint(25, 60), R.randint(65, 100)
        ga = 180 - al - be
        r_ = a * sin(be) / sin(al)
        f_ = a * sin(al) / sin(be)
        if gerundet(r_, 1) is None or gerundet(f_, 1) is None or ga < 10: return None
        return auswahl(f'α = {al}°, β = {be}°, a = {a} cm. Jemand rechnet b = {a} · sin {al}° : sin {be}° ≈ {dz(gerundet(f_, 1))} cm. Was ist falsch?',
                       f'Die Winkel sind vertauscht; richtig ist b = {a} · sin {be}° : sin {al}° ≈ {dz(gerundet(r_, 1))} cm.',
                       ['Nichts, die Rechnung stimmt.', f'Man braucht γ = {ga}°: b = {a} · sin {ga}° : sin {al}°.', 'Man muss den Kosinussatz nehmen.'],
                       f'b : sin β = a : sin α ⇒ b = a · sin β : sin α. Probe: β > α, also muss b > a sein; {dz(gerundet(f_, 1))} < {a}.',
                       'Welcher Winkel liegt b gegenüber? Er gehört zu b.')
    d = R.randint(50, 400)
    wahr = d * sin(be) / sin(ga)
    v = gerundet(wahr, 0)
    if v is None: return None
    return zahl(f'Zwei Beobachter A und B stehen {d} m voneinander entfernt. Sie sehen einen Baum C auf der anderen Seite eines Sees unter den Winkeln α = {al}° (bei A) und β = {be}° (bei B) zur Strecke AB. Wie weit ist der Baum von A entfernt (auf ganze Meter)?',
                f'γ = 180° − {al}° − {be}° = {ga}°. AC = b = {d} · sin {be}° : sin {ga}° ≈ {dz(v)} m.', 'AC liegt gegenüber von β; AB liegt gegenüber von γ.', v,
                f'round({d} * {K(sin(be))} / {K(sin(ga))}, 0)', einheit='m')


def g_sinussatz_winkel(s):
    al = R.randint(25, 70)
    a = R.randint(6, 15)
    if s == 1:
        b = R.randint(3, a - 1)
        x = Fr(b, 2 * a)
        wahr = asin(float(x))
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Im Dreieck ABC ist a = {a} cm, b = {b} cm und α = 30°. Berechne β (auf eine Nachkommastelle).',
                    f'sin β = {b} · sin 30° : {a} = {b} · 0,5 : {a} = {dz(x) if endlich(x) else br(x)}; β ≈ {dz(v)}° (eindeutig, weil b < a).',
                    'Sinussatz nach sin β umstellen; sin 30° = 0,5.', v, f'round({K(wahr)}, 1)', einheit='°')
    if s == 2:
        b = R.randint(3, a - 1)
        x = b * sin(al) / a
        wahr = asin(x)
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Im Dreieck ABC ist a = {a} cm, b = {b} cm und α = {al}°. Berechne β (auf eine Nachkommastelle).',
                    f'sin β = {b} · sin {al}° : {a} ≈ {dz(round(x, 4))}; β ≈ {dz(v)}° (eindeutig, weil b < a).', 'Sinussatz nach sin β umstellen, dann sin⁻¹.', v,
                    f'round({K(wahr)}, 1)', einheit='°')
    typ = R.random()
    if typ < 0.15:
        a = R.randint(3, 9)
        return zahl(f'Gegeben a = {a} cm, b = {2 * a} cm, α = 30°. Berechne β.',
                    f'sin β = {2 * a} · 0,5 : {a} = 1 ⇒ β = 90°. Es gibt genau ein Dreieck – es ist rechtwinklig.',
                    'Berechne sin β. Was bedeutet sin β = 1?', 90, '90', einheit='°')
    b = R.randint(a + 1, a + 8)
    x = b * sin(al) / a
    if typ < 0.5:
        n = 'zwei Dreiecke' if x < 1 else 'kein Dreieck'
        if abs(x - 1) < 1e-6: return None
        return auswahl(f'Gegeben a = {a} cm, b = {b} cm, α = {al}°. Wie viele Dreiecke gibt es?', n, ['zwei Dreiecke', 'genau ein Dreieck', 'kein Dreieck'],
                       f'sin β = {b} · sin {al}° : {a} ≈ {dz(round(x, 4))}' + (f' < 1, und weil b > a passen β und 180° − β: zwei Dreiecke.' if x < 1 else ' > 1: kein Winkel möglich, kein Dreieck.'),
                       'Berechne sin β. Ist der Wert kleiner als 1? Ist die gegebene Gegenseite a die kleinere?')
    if x >= 1: return None
    b1 = asin(x)
    b2 = 180 - b1
    if al + b2 >= 180: return None
    v1, v2 = gerundet(b1, 0), gerundet(b2, 0)
    if v1 is None or v2 is None: return None
    return luecken(f'Gegeben a = {a} cm, b = {b} cm, α = {al}°. Gib alle möglichen Winkel β auf ganze Grad an.', 'β₁ ≈ □°; β₂ ≈ □°', 'spitzer Winkel zuerst',
                   [v1, v2],
                   f'sin β = {b} · sin {al}° : {a} ≈ {dz(round(x, 4))}: β₁ ≈ {v1}°, β₂ = 180° − β₁ ≈ {v2}°. Beide passen, denn {al}° + {v2}° < 180°.',
                   'Zu einem Sinuswert gibt es β und 180° − β. Prüfe, ob beide ins Dreieck passen.', c=[f'round({K(b1)}, 0)', f'round(180 - {K(b1)}, 0)'])


def g_kosinussatz_seite(s):
    if s < 3 and R.random() < 0.7:
        g, (a, b, c) = (60, R.choice(G60)) if s == 1 or R.random() < 0.5 else (120, R.choice(G120))
        if R.random() < 0.5: a, b = b, a
        cs = Fr(1, 2) if g == 60 else Fr(-1, 2)
        return zahl(f'Im Dreieck ABC ist a = {a} cm, b = {b} cm und γ = {g}°. Berechne c.',
                    f'c² = {a}² + {b}² − 2 · {a} · {b} · cos {g}° = {a * a} + {b * b} {"−" if g == 60 else "+"} {a * b} = {c * c}, c = {c} cm.',
                    f'Kosinussatz; cos {g}° = {dz(cs)}.', c, f'({a} ** 2 + {b} ** 2 - 2 * {a} * {b} * ({cf(cs)})) / {c}', einheit='cm')
    a, b, g = R.randint(3, 15), R.randint(3, 15), R.randint(20, 160)
    wahr = sqrt(a * a + b * b - 2 * a * b * cos(g))
    v = gerundet(wahr, 1)
    if v is None: return None
    if s == 3 and R.random() < 0.5:
        return zahl(f'Ein Schiff fährt {a} km nach Osten, dreht dann um {180 - g}° nach links und fährt {b} km weiter. Wie weit ist es vom Start entfernt (auf eine Nachkommastelle)?',
                    f'Der Winkel im Dreieck am Wendepunkt ist 180° − {180 - g}° = {g}°. d² = {a}² + {b}² − 2 · {a} · {b} · cos {g}°, d ≈ {dz(v)} km.',
                    'Skizze! Der Innenwinkel am Wendepunkt ist 180° minus Drehwinkel.', v,
                    f'round({K(wahr)}, 1)', einheit='km')
    return zahl(f'Im Dreieck ABC ist a = {a} cm, b = {b} cm und γ = {g}°. Berechne c (auf eine Nachkommastelle).',
                f'c² = {a * a} + {b * b} − 2 · {a} · {b} · cos {g}° ≈ {dz(round(wahr * wahr, 2))}, c ≈ {dz(v)} cm.', 'Kosinussatz mit dem eingeschlossenen Winkel γ.', v,
                f'round({K(wahr)}, 1)', einheit='cm')


def g_kosinussatz_winkel(s):
    if s == 1 and R.random() < 0.25:
        p_, q_, r_ = R.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (7, 24, 25), (9, 12, 15)])
        return zahl(f'Ein Dreieck hat die Seiten a = {p_} cm, b = {q_} cm, c = {r_} cm. Berechne γ.',
                    f'cos γ = ({p_ * p_} + {q_ * q_} − {r_ * r_}) : (2 · {p_} · {q_}) = 0 ⇒ γ = 90°.',
                    'Das Quadrat der Gegenseite von γ wird subtrahiert.', 90, f'90 - 60 * (({p_} ** 2 + {q_} ** 2 - {r_} ** 2) / (2 * {p_} * {q_}))', einheit='°')
    if s == 3 and R.random() < 0.3:
        if R.random() < 0.5:
            a, b = R.randint(2, 6), R.randint(2, 6)
            c = a + b + R.randint(1, 4)
            x = Fr(a * a + b * b - c * c, 2 * a * b)
            return auswahl(f'Ein Dreieck soll die Seiten {a} cm, {b} cm und {c} cm haben. Was ergibt der Kosinussatz für den größten Winkel?',
                           'cos γ < −1: Es gibt kein solches Dreieck.', ['γ ist stumpf, aber berechenbar.', 'γ = 180°.', 'cos γ > 1: γ ist spitz.'],
                           f'cos γ = ({dz(a * a)} + {dz(b * b)} − {dz(c * c)}) : {2 * a * b} = {br(x)} < −1. Kein Winkel hat diesen Kosinus: {a} + {b} < {c}, die Seiten schließen sich nicht.',
                           'Rechne cos γ aus. Welche Werte kann ein Kosinus annehmen?')
        a, b = R.randint(2, 8), R.randint(2, 8)
        c = a + b
        return auswahl(f'Ein Dreieck soll die Seiten {a} cm, {b} cm und {c} cm haben. Was ergibt der Kosinussatz für den größten Winkel?',
                       'cos γ = −1: Die Punkte liegen auf einer Geraden, kein Dreieck.', ['γ = 90°.', 'cos γ < −1: γ ist sehr stumpf.', 'γ = 120°.'],
                       f'cos γ = ({dz(a * a)} + {dz(b * b)} − {dz(c * c)}) : {2 * a * b} = −1, also γ = 180°. Wegen {a} + {b} = {c} liegt C auf der Strecke AB.',
                       'Rechne cos γ aus. Was bedeutet γ = 180°?')
    if s == 1 or (s == 2 and R.random() < 0.3):
        g, (a, b, c) = (60, R.choice(G60)) if R.random() < 0.5 else (120, R.choice(G120))
        if R.random() < 0.5: a, b = b, a
        return zahl(f'Ein Dreieck hat die Seiten a = {a} cm, b = {b} cm, c = {c} cm. Berechne γ.',
                    f'cos γ = ({dz(a * a)} + {dz(b * b)} − {dz(c * c)}) : (2 · {a} · {b}) = {dz(Fr(a * a + b * b - c * c, 2 * a * b))} ⇒ γ = {g}°.',
                    'Das Quadrat der Gegenseite von γ wird subtrahiert.', g,
                    f'90 - 60 * (({a} ** 2 + {b} ** 2 - {c} ** 2) / (2 * {a} * {b}))', einheit='°')
    a, b = R.randint(3, 15), R.randint(3, 15)
    c = R.randint(abs(a - b) + 1, a + b - 1)
    x = (a * a + b * b - c * c) / (2 * a * b)
    wahr = acos(x)
    v = gerundet(wahr, 1)
    if v is None: return None
    if s == 3 and R.random() < 0.5:
        return zahl(f'Ein dreieckiges Grundstück hat die Seiten {a * 10} m, {b * 10} m und {c * 10} m. Wie groß ist der Winkel gegenüber der {c * 10}-m-Seite (auf eine Nachkommastelle)?',
                    f'cos γ = ({a * 10}² + {b * 10}² − {c * 10}²) : (2 · {a * 10} · {b * 10}) ≈ {dz(round(x, 4))} ⇒ γ ≈ {dz(v)}°.',
                    'Kosinussatz nach cos γ umstellen; γ liegt gegenüber der genannten Seite.', v, f'round({K(wahr)}, 1)', einheit='°')
    return zahl(f'Ein Dreieck hat die Seiten a = {a} cm, b = {b} cm, c = {c} cm. Berechne γ (auf eine Nachkommastelle).',
                f'cos γ = ({dz(a * a)} + {dz(b * b)} − {dz(c * c)}) : {2 * a * b} ≈ {dz(round(x, 4))} ⇒ γ ≈ {dz(v)}°.', 'Kosinussatz nach cos γ umstellen, dann cos⁻¹.', v,
                f'round({K(wahr)}, 1)', einheit='°')


SAETZE = ['Sinussatz', 'Kosinussatz', 'Winkelsumme im Dreieck', 'Satz des Pythagoras']


def g_satz_waehlen(s):
    typen = [  # (gegeben, Ziel, Satz, Begründung)
        ('a, b und c', 'einen Winkel', 'Kosinussatz', 'SSS: Alle drei Seiten sind bekannt, aber kein Winkel – Kosinussatz nach dem Winkel umstellen.'),
        ('a, b und γ', 'die Seite c', 'Kosinussatz', 'SWS: γ liegt zwischen a und b; zu keiner Seite ist der Gegenwinkel bekannt – Kosinussatz.'),
        ('b, c und α', 'die Seite a', 'Kosinussatz', 'SWS: α liegt zwischen b und c – Kosinussatz.'),
        ('a, c und β', 'die Seite b', 'Kosinussatz', 'SWS: β liegt zwischen a und c – Kosinussatz.'),
        ('a, α und β', 'die Seite b', 'Sinussatz', 'Seite a mit Gegenwinkel α bekannt, β gegeben – Sinussatz.'),
        ('a, α und β', 'den Winkel γ', 'Winkelsumme im Dreieck', 'Zwei Winkel sind bekannt: γ = 180° − α − β. Dafür brauchst du keinen der beiden Sätze.'),
        ('c, α und β', 'den Winkel γ', 'Winkelsumme im Dreieck', 'Zwei Winkel sind bekannt: γ = 180° − α − β.'),
        ('a, b und α', 'den Winkel β', 'Sinussatz', 'SsW: Seite a mit Gegenwinkel α bekannt – Sinussatz (auf Mehrdeutigkeit achten).'),
        ('b, c und β', 'den Winkel γ', 'Sinussatz', 'SsW: b mit Gegenwinkel β bekannt – Sinussatz.'),
        ('b, α und γ', 'den Winkel β', 'Winkelsumme im Dreieck', 'Zwei Winkel sind bekannt: β = 180° − α − γ.'),
        ('a, γ = 90° und b', 'die Seite c', 'Satz des Pythagoras', 'γ = 90°: c ist die Hypotenuse, c² = a² + b² (der Kosinussatz liefert dasselbe).'),
    ]
    if s < 3:
        pool = typen if s == 2 else [t for t in typen if t[2] in ('Kosinussatz', 'Sinussatz')]
        geg, ziel, r, w = R.choice(pool)
        if R.random() < 0.6:
            teile = [t.strip() for t in geg.replace(' und ', ', ').split(',')]
            werte = []
            for t in teile:
                if '=' in t: werte.append(t)
                elif t in 'abc': werte.append(f'{t} = {R.randint(3, 15)} cm')
                else: werte.append(f'{t} = {R.randint(20, 80)}°')
            txt = ', '.join(werte[:-1]) + ' und ' + werte[-1]
            return auswahl(f'Im Dreieck ABC ist {txt}. Womit berechnest du {ziel}?', r, SAETZE, w,
                           'Gibt es ein bekanntes Paar aus Seite und gegenüberliegendem Winkel? Sind schon zwei Winkel bekannt?')
        return auswahl(f'Im Dreieck ABC sind {geg} gegeben. Womit berechnest du {ziel}?', r, SAETZE, w,
                       'Gibt es ein bekanntes Paar aus Seite und gegenüberliegendem Winkel? Sind schon zwei Winkel bekannt?')
    typ = R.random()
    if typ < 0.35:
        a, b, g = R.randint(3, 12), R.randint(3, 12), R.randint(30, 150)
        return auswahl(f'Gegeben a = {a} cm, b = {b} cm, γ = {g}°. Jemand will c mit dem Sinussatz berechnen. Was stimmt?',
                       'Das geht nicht direkt: Es fehlt ein Paar Seite/Gegenwinkel. Erst c mit dem Kosinussatz.',
                       ['Das geht: c = a · sin γ : sin α.', 'Das geht nur, wenn γ = 90° ist.', 'Man braucht dafür die Flächenformel.'],
                       f'Bekannt sind a, b und der eingeschlossene Winkel γ (SWS). Zu a und b fehlen α und β – der Sinussatz lässt sich nicht ansetzen.',
                       'Welche Größen braucht der Sinussatz?')
    if typ < 0.7:
        if R.random() < 0.5:
            a, b, g = R.randint(4, 12), R.randint(3, 10), R.randint(30, 120)
            return auswahl(f'Gegeben a = {a} cm, b = {b} cm, γ = {g}°. Gesucht ist α. Welcher Weg ist richtig?',
                           '1. c mit dem Kosinussatz, 2. α mit dem Kosinussatz (oder Sinussatz).',
                           ['α direkt mit dem Sinussatz.', 'α mit der Winkelsumme.', '1. α mit dem Satz des Pythagoras, 2. c mit dem Sinussatz.'],
                           'SWS: Zuerst fehlt die dritte Seite c (Kosinussatz). Danach sind alle Seiten bekannt, und α folgt mit dem Kosinussatz.',
                           'Was fehlt dir, bevor du einen Satz für α ansetzen kannst?')
        return auswahl('Gegeben sind a, b und α mit a > b. Gesucht ist c. Welcher Weg ist richtig?',
                       '1. β mit dem Sinussatz, 2. γ mit der Winkelsumme, 3. c mit dem Sinussatz.',
                       ['c direkt mit dem Kosinussatz aus a, b und α.', '1. γ mit der Winkelsumme, 2. c mit dem Sinussatz.', 'c mit dem Satz des Pythagoras.'],
                       'Zu a ist der Gegenwinkel α bekannt: Sinussatz liefert β (eindeutig, weil a > b). Dann γ = 180° − α − β und c = a · sin γ : sin α.',
                       'Welches Paar aus Seite und Gegenwinkel kennst du?')
    a, b, c = sorted(R.sample(range(3, 15), 3))
    if a + b <= c: return None
    x = (a * a + b * b - c * c) / (2 * a * b)
    stumpf = x < 0
    return auswahl(f'Ein Dreieck hat die Seiten {a} cm, {b} cm und {c} cm. Ist der größte Winkel spitz, recht oder stumpf?',
                   'stumpf' if stumpf else 'recht' if x == 0 else 'spitz', ['spitz', 'recht', 'stumpf'],
                   f'Der größte Winkel liegt gegenüber {c} cm: cos γ = ({dz(a * a)} + {dz(b * b)} − {dz(c * c)}) : {2 * a * b} = {br(Fr(a * a + b * b - c * c, 2 * a * b))}'
                   + (' < 0: stumpf.' if stumpf else ' = 0: recht.' if x == 0 else ' > 0: spitz.'),
                   'Vorzeichen von a² + b² − c² für die längste Seite c entscheidet.')


GEN = {'einheitskreis': g_einheitskreis, 'flaeche': g_flaeche, 'sinussatz_seite': g_sinussatz_seite, 'sinussatz_winkel': g_sinussatz_winkel,
       'kosinussatz_seite': g_kosinussatz_seite, 'kosinussatz_winkel': g_kosinussatz_winkel, 'satz_waehlen': g_satz_waehlen}

# ---------- Zehnte Runde (schwer-kl9): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Abschnitt mit eigenem festen Zufallsstart (anhaengen(..., 9912, ...)), läuft erst nach bauen():
# alle bisherigen Aufgaben bleiben unverändert. Vorbilder: Bayerischer Mathematik-Test 10 2025 (Einheitskreis:
# sin(α + 90°); Flächeninhalt als Term mit sin α), Abschlussprüfung Realschule Bayern Mathematik I (2023: Kosinussatz
# und anschließend Flächeninhalt mit der Sinusformel, Gleichung sin x = Wert mit zwei Lösungen in [0°; 180°];
# 2024: Sinussatz in einer Figur, Winkel aus einer Streckenlänge). Zahlen und Wortlaut eigen.
from _schwer_kl9 import anhaengen  # noqa: E402
from _kl9 import K as _K  # noqa: E402


def schwer():
    P, Kn, O = 'pruefung', 'knobel', ''
    r1 = lambda x: round(x, 1)
    c1 = lambda x: f'round({_K(x)}, 1)'
    kreis = {'typ': 'koordinaten', 'x': [-1.2, 1.2], 'y': [-1.2, 1.2], 'schritt_x': 0.5, 'schritt_y': 0.5, 'kreise': [{'m': [0, 0], 'r': 1}],
             'punkte': [{'x': -0.8, 'y': 0.6, 'name': 'P'}], 'strecken': [[0, 0, -0.8, 0.6]]}
    cosw = lambda a, b, c: acos((a * a + b * b - c * c) / (2 * a * b))
    return [
        # einheitskreis
        ('einheitskreis', 3, P, auswahl('Für einen spitzen Winkel α gilt cos α = 0,6. Welchen Wert hat sin(α + 90°)?', '0,6', ['0,8', '−0,6', '−0,8'],
                                        'Dreht man den Zeiger um 90° weiter, wird aus (cos α | sin α) der Punkt (−sin α | cos α). Also sin(α + 90°) = cos α = 0,6.',
                                        'Zeichne den Zeiger zu α und drehe ihn um 90° weiter. Welche Länge wird jetzt zur y-Koordinate?')),
        ('einheitskreis', 3, P, bild(auswahl('Der Punkt P(−0,8 | 0,6) liegt auf dem Einheitskreis und gehört zum Winkel α. Welche Aussage stimmt?',
                                             'sin α = 0,6 und cos α = −0,8; α liegt zwischen 90° und 180°.',
                                             ['sin α = −0,8 und cos α = 0,6.', 'α liegt zwischen 0° und 90°, denn sin α ist positiv.', 'sin α = 0,8 und cos α = 0,6.'],
                                             'Der Punkt ist (cos α | sin α). x = −0,8 < 0 und y = 0,6 > 0: links oben, also 90° < α < 180° (α ≈ 143°).',
                                             'x-Koordinate = cos α, y-Koordinate = sin α.'), kreis)),
        ('einheitskreis', 3, Kn, zahl('Für wie viele Winkel α mit 0° ≤ α < 360° gilt sin α = cos α?', 'Der Punkt auf dem Einheitskreis braucht gleiche Koordinaten: bei 45° (beide positiv) und bei 225° (beide negativ). Also 2 Winkel.',
                                      'Wo auf dem Einheitskreis sind x- und y-Koordinate gleich? Denke an die Winkelhalbierende.', 2, '1 + 1')),
        ('einheitskreis', 3, O, auswahl('Welcher Wert ist am größten? (Ohne Taschenrechner)', 'cos 5°', ['sin 110°', 'sin 170°', 'cos 100°'],
                                        'sin 110° = sin 70° = cos 20°, sin 170° = sin 10° (klein), cos 100° ist negativ. cos 5° liegt am nächsten an 1.',
                                        'Führe alles auf Winkel zwischen 0° und 90° zurück und vergleiche.')),
        ('einheitskreis', 2, O, zahl('Es gilt cos 50° ≈ 0,6428. Wie groß ist cos 130° (vier Nachkommastellen)?', '130° = 180° − 50°: Spiegelung an der y-Achse, der Kosinus wechselt das Vorzeichen: −0,6428.',
                                     'cos(180° − α) = −cos α.', -0.6428, '-0.6428')),
        ('einheitskreis', 2, O, auswahl('Zwischen welchen Winkeln sind sin α und cos α beide negativ?', 'zwischen 180° und 270°',
                                        ['zwischen 90° und 180°', 'zwischen 270° und 360°', 'zwischen 0° und 90°'],
                                        'Beide Koordinaten negativ: links unten, also im 3. Viertel des Kreises.', 'Wo sind x und y beide negativ?')),
        # flaeche
        ('flaeche', 3, P, zahl('Ein Dreieck hat a = 8 cm, b = 5 cm und den eingeschlossenen Winkel γ = 150°. Berechne den Flächeninhalt ohne Taschenrechner (sin 150° = 0,5).',
                               'A = 1/2 · 8 · 5 · sin 150° = 20 · 0,5 = 10 cm².', 'Flächenformel mit dem eingeschlossenen Winkel.', 10, '0.5 * 8 * 5 * 0.5', einheit='cm²')),
        ('flaeche', 3, P, auswahl('Ein Dreieck hat die Seiten 4 cm und 10 cm, die den Winkel γ einschließen. Welcher Term gibt seinen Flächeninhalt (in cm²) an?', '20 · sin γ',
                                  ['40 · sin γ', '20 · cos γ', '14 · sin γ'], 'A = 1/2 · 4 · 10 · sin γ = 20 · sin γ.', 'Vergiss den Faktor 1/2 nicht.')),
        ('flaeche', 3, Kn, auswahl('Zwei Seiten eines Dreiecks sind fest 6 cm und 9 cm lang. Bei welchem Winkel zwischen ihnen ist der Flächeninhalt am größten?', '90°', ['60°', '120°', '180°'],
                                   'A = 27 · sin γ. sin γ ist bei 90° am größten (= 1). Bei 180° wäre das Dreieck flach (A = 0).', 'Wann ist sin γ am größten?')),
        ('flaeche', 3, O, zahl('Ein Parallelogramm hat die Seiten 12 cm und 7 cm und den Flächeninhalt 42 cm². Wie groß ist sein spitzer Winkel?', 'A = 12 · 7 · sin α = 84 · sin α = 42 ⇒ sin α = 0,5 ⇒ α = 30°.',
                               'Parallelogramm: A = a · b · sin α (ohne 1/2).', 30, '180 / 6', einheit='°')),
        ('flaeche', 2, O, zahl('Ein Dreieck hat a = 6 cm, b = 10 cm und γ = 40°. Berechne den Flächeninhalt (auf eine Nachkommastelle).', 'A = 1/2 · 6 · 10 · sin 40° ≈ 19,3 cm².',
                               'A = 1/2 · a · b · sin γ.', r1(30 * sin(40)), c1(30 * sin(40)), einheit='cm²')),
        ('flaeche', 2, O, zahl('Berechne den Flächeninhalt eines gleichseitigen Dreiecks mit 10 cm Seitenlänge mit A = 1/2 · a · b · sin γ (auf eine Nachkommastelle).', 'Alle Winkel 60°: A = 1/2 · 10 · 10 · sin 60° ≈ 43,3 cm².',
                               'Im gleichseitigen Dreieck ist jeder Winkel 60°.', r1(50 * sin(60)), c1(50 * sin(60)), einheit='cm²')),
        # sinussatz_seite
        ('sinussatz_seite', 3, P, zahl('Im Dreieck ABC ist c = 10 cm, α = 45° und γ = 30°. Berechne a (sin 45° ≈ 0,7071; sin 30° = 0,5). Runde auf eine Nachkommastelle.',
                                       'a : sin α = c : sin γ ⇒ a = 10 · 0,7071 : 0,5 ≈ 14,1 cm.', 'Zu a gehört α, zu c gehört γ.', r1(10 * sin(45) / 0.5), c1(10 * sin(45) / 0.5), einheit='cm')),
        ('sinussatz_seite', 3, P, zahl('Im Dreieck ABC ist a = 9 cm, β = 48° und γ = 77°. Berechne b (auf eine Nachkommastelle).', 'α = 180° − 48° − 77° = 55°. b = 9 · sin 48° : sin 55° ≈ 8,2 cm.',
                                       'Zu a fehlt der Gegenwinkel – erst α mit der Winkelsumme.', r1(9 * sin(48) / sin(55)), c1(9 * sin(48) / sin(55)), einheit='cm')),
        ('sinussatz_seite', 3, Kn, zahl('In einem Dreieck ist α = 30° und β = 60°. Die längste Seite ist 12 cm lang. Wie lang ist die kürzeste Seite?',
                                        'γ = 90°, die längste Seite ist c = 12 cm. Die kürzeste liegt 30° gegenüber: a = 12 · sin 30° : sin 90° = 6 cm.',
                                        'Bestimme zuerst den dritten Winkel. Größter Winkel – längste Seite.', 6, '12 * 0.5', einheit='cm')),
        ('sinussatz_seite', 3, O, zahl('Ein Grundstück ABC hat die Seite AB = 50 m; bei A ist der Winkel 70°, bei B 65°. Wie lang ist AC? Runde auf ganze Meter.',
                                       'γ = 45°. AC = b = 50 · sin 65° : sin 45° ≈ 64 m.', 'AC liegt dem Winkel bei B gegenüber.', round(50 * sin(65) / sin(45)), f'round({_K(50 * sin(65) / sin(45))}, 0)',
                                       einheit='m')),
        ('sinussatz_seite', 2, O, zahl('Im Dreieck ABC ist a = 7 cm, α = 40° und β = 75°. Berechne b (auf eine Nachkommastelle).', 'b = 7 · sin 75° : sin 40° ≈ 10,5 cm.',
                                       'b : sin β = a : sin α.', r1(7 * sin(75) / sin(40)), c1(7 * sin(75) / sin(40)), einheit='cm')),
        ('sinussatz_seite', 2, O, auswahl('In einem Dreieck ist α = 70° und β = 50°. Welche Seite ist die längste?', 'a', ['b', 'c', 'Alle sind gleich lang.'],
                                          'γ = 60°. Der größte Winkel ist α = 70°, also ist die gegenüberliegende Seite a die längste.', 'Größter Winkel – längste Seite. Berechne γ.')),
        # sinussatz_winkel
        ('sinussatz_winkel', 3, P, luecken('In einem Dreieck gilt sin β = 0,8. Welche Werte kann β haben? Runde auf ganze Grad.', 'β₁ ≈ □°; β₂ ≈ □°', 'kleineren Winkel zuerst',
                                           [round(asin(0.8)), 180 - round(asin(0.8))],
                                           'sin⁻¹(0,8) ≈ 53°. Auch 180° − 53° = 127° hat den Sinus 0,8. Beide sind als Dreieckswinkel möglich.',
                                           'Der Taschenrechner liefert nur den spitzen Winkel. Denke an sin(180° − β) = sin β.',
                                           [f'round({_K(asin(0.8))}, 0)', f'180 - round({_K(asin(0.8))}, 0)'])),
        ('sinussatz_winkel', 3, P, zahl('Im Dreieck ABC ist a = 8 cm, b = 5 cm und α = 70°. Berechne β (auf eine Nachkommastelle).',
                                        'sin β = 5 · sin 70° : 8 ≈ 0,587, β ≈ 36,0°. Wegen b < a ist β < α, also nur der spitze Winkel.',
                                        'Sinussatz nach sin β umstellen. Prüfe, ob auch 180° − β passt.', r1(asin(5 * sin(70) / 8)), c1(asin(5 * sin(70) / 8)), einheit='°')),
        ('sinussatz_winkel', 3, Kn, auswahl('Gegeben sind a = 4 cm, b = 10 cm und α = 30°. Wie viele Dreiecke gibt es?', 'kein Dreieck', ['genau ein Dreieck', 'zwei Dreiecke', 'unendlich viele'],
                                            'sin β = 10 · 0,5 : 4 = 1,25 > 1. Einen solchen Winkel gibt es nicht: Die Seite a ist zu kurz, um die Gegenseite zu erreichen.',
                                            'Berechne sin β. Kann ein Sinuswert größer als 1 sein?')),
        ('sinussatz_winkel', 3, O, zahl('Im Dreieck ABC ist a = 12 cm, c = 9 cm und α = 100°. Berechne γ (auf eine Nachkommastelle).', 'sin γ = 9 · sin 100° : 12 ≈ 0,739, γ ≈ 47,6° (nur spitz, da α schon stumpf ist).',
                                        'Ist α stumpf, müssen die anderen Winkel spitz sein.', r1(asin(9 * sin(100) / 12)), c1(asin(9 * sin(100) / 12)), einheit='°')),
        ('sinussatz_winkel', 2, O, zahl('Im Dreieck ABC ist a = 10 cm, b = 6 cm und α = 50°. Berechne β (auf eine Nachkommastelle).', 'sin β = 6 · sin 50° : 10 ≈ 0,460, β ≈ 27,4°.',
                                        'sin β = b · sin α : a.', r1(asin(6 * sin(50) / 10)), c1(asin(6 * sin(50) / 10)), einheit='°')),
        ('sinussatz_winkel', 2, O, auswahl('Im Dreieck ist a = 10 cm, b = 6 cm, α = 50°. Kommt für β auch der stumpfe Winkel 180° − 27,4° in Frage?', 'Nein, denn b < a, also muss β kleiner als α sein.',
                                           ['Ja, es gibt immer zwei Lösungen.', 'Ja, weil sin β positiv ist.'],
                                           'Der kürzeren Seite liegt der kleinere Winkel gegenüber. Außerdem wäre 50° + 152,6° > 180°.', 'Vergleiche a und b.')),
        # kosinussatz_seite
        ('kosinussatz_seite', 3, P, zahl('Im Dreieck ABC ist b = 6 cm, c = 10 cm und α = 120°. Berechne a ohne Taschenrechner (cos 120° = −0,5).',
                                         'a² = 36 + 100 − 2 · 6 · 10 · (−0,5) = 136 + 60 = 196, a = 14 cm.', 'Achte auf das Vorzeichen: minus mal minus.', 14, '(36 + 100 + 60) / 14', einheit='cm')),
        ('kosinussatz_seite', 3, P, zahl('Zwei Wanderer starten am selben Punkt. Einer geht 3 km nach Norden, der andere 5 km in eine Richtung, die mit der Nordrichtung 60° einschließt. Wie weit sind sie dann voneinander entfernt? Runde auf eine Nachkommastelle.',
                                         'd² = 9 + 25 − 2 · 3 · 5 · cos 60° = 34 − 15 = 19, d ≈ 4,4 km.', 'Skizze: zwei Seiten und der eingeschlossene Winkel (SWS).', r1(19 ** 0.5), c1(19 ** 0.5),
                                         einheit='km')),
        ('kosinussatz_seite', 3, Kn, zahl('In einem Dreieck gilt c² = a² + b² + a · b. Wie groß ist der Winkel γ?', 'Vergleich mit c² = a² + b² − 2ab · cos γ: −2 cos γ = 1 ⇒ cos γ = −0,5 ⇒ γ = 120°.',
                                          'Vergleiche mit dem Kosinussatz. Was muss cos γ sein?', 120, '180 - 60', einheit='°')),
        ('kosinussatz_seite', 3, O, zahl('Eine Raute hat 10 cm Seitenlänge und einen Innenwinkel von 70°. Wie lang ist die längere Diagonale? Runde auf eine Nachkommastelle.',
                                         'Die längere Diagonale liegt dem stumpfen Winkel 110° gegenüber: d² = 100 + 100 − 200 · cos 110° ≈ 268,4, d ≈ 16,4 cm.',
                                         'Benachbarte Winkel in der Raute ergeben 180°. Welcher Winkel liegt der längeren Diagonale gegenüber?',
                                         r1((200 - 200 * cos(110)) ** 0.5), c1((200 - 200 * cos(110)) ** 0.5), einheit='cm')),
        ('kosinussatz_seite', 2, O, zahl('Im Dreieck ABC ist a = 6 cm, b = 9 cm und γ = 50°. Berechne c (auf eine Nachkommastelle).', 'c² = 36 + 81 − 108 · cos 50° ≈ 47,6, c ≈ 6,9 cm.',
                                         'c² = a² + b² − 2ab · cos γ.', r1((117 - 108 * cos(50)) ** 0.5), c1((117 - 108 * cos(50)) ** 0.5), einheit='cm')),
        ('kosinussatz_seite', 2, O, zahl('Im Dreieck ABC ist a = 3 cm, b = 4 cm und γ = 90°. Berechne c mit dem Kosinussatz.', 'cos 90° = 0: c² = 9 + 16 = 25, c = 5 cm – der Satz des Pythagoras.',
                                         'Was ist cos 90°?', 5, '(9 + 16) / 5', einheit='cm')),
        # kosinussatz_winkel
        ('kosinussatz_winkel', 3, P, zahl('Ein Dreieck hat die Seiten 5 cm, 7 cm und 8 cm. Berechne den Winkel gegenüber der 7-cm-Seite ohne Taschenrechner.',
                                          'cos φ = (25 + 64 − 49) : (2 · 5 · 8) = 40 : 80 = 0,5 ⇒ φ = 60°.', 'Die 7-cm-Seite steht im Kosinussatz mit Minus.', 60, '180 / 3', einheit='°')),
        ('kosinussatz_winkel', 3, P, zahl('Ein Dachgiebel hat zwei 5 m lange Sparren und eine Spannweite von 8 m. Wie groß ist der Winkel am First? Runde auf eine Nachkommastelle.',
                                          'cos φ = (25 + 25 − 64) : 50 = −0,28 ⇒ φ ≈ 106,3°.', 'Der Winkel am First liegt der Spannweite gegenüber.', r1(cosw(5, 5, 8)), c1(cosw(5, 5, 8)), einheit='°')),
        ('kosinussatz_winkel', 3, Kn, auswahl('Ohne zu rechnen: Ein Dreieck hat die Seiten 4 cm, 5 cm und 7 cm. Was gilt für seinen größten Winkel?', 'Er ist stumpf.', ['Er ist spitz.', 'Er ist genau 90°.', 'Das kann man ohne Taschenrechner nicht sagen.'],
                                              '4² + 5² = 41 < 49 = 7². Im Kosinussatz wird cos γ = (41 − 49) : 40 negativ, also γ > 90°.', 'Vergleiche a² + b² mit c² der längsten Seite.')),
        ('kosinussatz_winkel', 3, O, zahl('Ein Dreieck hat die Seiten 6 cm, 8 cm und 11 cm. Berechne seinen größten Winkel (auf eine Nachkommastelle).',
                                          'Der größte Winkel liegt der 11-cm-Seite gegenüber: cos γ = (36 + 64 − 121) : 96 ≈ −0,219, γ ≈ 102,6°.', 'Größter Winkel – gegenüber der längsten Seite.',
                                          r1(cosw(6, 8, 11)), c1(cosw(6, 8, 11)), einheit='°')),
        ('kosinussatz_winkel', 2, O, zahl('Ein Dreieck hat a = 4 cm, b = 6 cm und c = 5 cm. Berechne γ (auf eine Nachkommastelle).', 'cos γ = (16 + 36 − 25) : 48 = 0,5625, γ ≈ 55,8°.',
                                          'cos γ = (a² + b² − c²) : 2ab.', r1(cosw(4, 6, 5)), c1(cosw(4, 6, 5)), einheit='°')),
        ('kosinussatz_winkel', 2, O, auswahl('Der Kosinussatz liefert cos γ = −0,3. Was folgt für γ?', 'γ ist stumpf.', ['γ ist spitz.', 'γ = 90°.'],
                                             'Ein negativer Kosinus gehört zu einem Winkel zwischen 90° und 180°.', 'Wo ist der Kosinus negativ?')),
        # satz_waehlen
        ('satz_waehlen', 3, P, auswahl('Gegeben sind a, b und der eingeschlossene Winkel γ. Gesucht ist der Flächeninhalt. Was ist der kürzeste Weg?', 'A = 1/2 · a · b · sin γ direkt',
                                       ['erst c mit dem Kosinussatz, dann eine Höhe', 'erst α mit dem Sinussatz, dann A', 'Das geht nur mit einer gegebenen Höhe.'],
                                       'Die Flächenformel braucht genau zwei Seiten und den Winkel zwischen ihnen – das ist gegeben.', 'Welche Formel passt genau zu SWS?')),
        ('satz_waehlen', 3, P, auswahl('Gegeben sind c = 9 cm, α = 50° und β = 70° (WSW). Wie berechnet man a?', 'Erst γ = 60° mit der Winkelsumme, dann Sinussatz: a = c · sin α : sin γ.',
                                       ['Mit dem Kosinussatz.', 'Mit dem Satz des Pythagoras.', 'Sinussatz: a = c · sin α : sin β.'],
                                       'Zu c gehört der Gegenwinkel γ. Den liefert die Winkelsumme, dann passt der Sinussatz.', 'Welcher Winkel liegt c gegenüber?')),
        ('satz_waehlen', 3, Kn, auswahl('Von einem Dreieck kennt man nur die drei Winkel 40°, 60° und 80°. Was lässt sich berechnen?', 'Nur die Verhältnisse der Seiten, keine Längen.',
                                        ['Alle Seiten mit dem Sinussatz.', 'Alle Seiten mit dem Kosinussatz.', 'Gar nichts, auch keine Verhältnisse.'],
                                        'Alle ähnlichen Dreiecke haben dieselben Winkel. Der Sinussatz liefert a : b : c = sin 40° : sin 60° : sin 80°, aber keine Längen.',
                                        'Denke an ähnliche Dreiecke: Gibt es nur eines mit diesen Winkeln?')),
        ('satz_waehlen', 3, O, auswahl('Gegeben a = 7 cm, b = 9 cm, c = 12 cm. Gesucht ist der Flächeninhalt. Was ist ein sinnvoller erster Schritt?', 'einen Winkel mit dem Kosinussatz berechnen',
                                       ['einen Winkel mit dem Sinussatz berechnen', 'die Höhe mit dem Satz des Pythagoras berechnen', 'A = 1/2 · a · b'],
                                       'Bei SSS fehlt jeder Winkel; der Kosinussatz liefert einen. Danach A = 1/2 · a · b · sin γ.', 'Für die Flächenformel fehlt ein Winkel.')),
        ('satz_waehlen', 2, O, auswahl('Gegeben sind alle drei Seiten. Welcher Satz liefert einen Winkel?', 'Kosinussatz', ['Sinussatz', 'Satz des Pythagoras'],
                                       'Der Sinussatz braucht schon einen Winkel. Mit drei Seiten hilft nur der Kosinussatz.', 'Welcher Satz kommt ohne bekannten Winkel aus?')),
        ('satz_waehlen', 2, O, auswahl('Gegeben sind a, α und β. Welcher Satz liefert b direkt?', 'Sinussatz', ['Kosinussatz', 'Satz des Pythagoras'],
                                       'a und α bilden ein Paar, β gehört zu b: b = a · sin β : sin α.', 'Seite mit Gegenwinkel bekannt?')),
    ]


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('trigo.allgemein', 13_9_12)
# a) nur Vorzeichenwechsel, „vier Nachkommastellen“ ist Abschreiben → Stufe 2
for _w, _s, _w2 in [('17', '0,2924', '197'), ('85', '0,9962', '265'), ('40', '0,6428', '220'), ('5', '0,0872', '185'), ('45', '0,7071', '225')]:
    BF.stufe('einheitskreis', f'Es gilt sin {_w}° ≈ {_s}. Wie groß ist sin {_w2}° (vier Nachkommastellen)?', 2)
BF.nicht_umgesetzt('kosinussatz_seite S3 viermal „Schiff fährt … dreht um … nach links“; Lernkarte erklärt „180° − Drehwinkel“ nicht',
                   'Aufgaben richtig; der Tipp nennt den Schritt („Der Innenwinkel am Wendepunkt ist 180° minus Drehwinkel“), der Lösungsweg rechnet ihn vor. Seit Runde 10 gibt es auf Stufe 3 weitere Typen. Lernkarte siehe „für Sebastian“.')
BF.nicht_umgesetzt('sinussatz_seite S3 viermal „Zwei Beobachter … Baum auf der anderen Seite eines Sees“', 'Kein Fehler; seit Runde 10 gibt es auf Stufe 3 vier andere Typen.')
BF.fuer_sebastian('trigo.allgemein/kosinussatz_seite: Lernkarte erklärt nicht, dass der Dreieckswinkel 180° minus Drehwinkel ist (Schiff-Aufgaben). Ergänzen? Karten-Text nicht geändert.')

# ---- BEFUNDE ENDE ----


# ---------- Achtzehnte Runde, Teil B (Zweig luecken-kl9) ----------
# LehrplanPLUS M9 7.2: „vollziehen den Beweis des Sinussatzes nach und interpretieren den Satz des Pythagoras als Spezialfall des
# Kosinussatzes. Sie lösen mithilfe von Sinus- und Kosinussatz nun auch rechnerisch Anwendungsaufgaben“ (Wortlaut nach ISB,
# Schwerpunktsetzungen Jgst. 9). Prüfungsvorbilder (Typ und Niveau, eigene Zahlen und Einkleidung): Abschlussprüfung Realschule
# Bayern Mathematik II (Vermessung mit Sinussatz, z. B. AP 2015 A 1; Kurs- und Entfernungsaufgaben mit dem Kosinussatz).
# 1) neue Lernkarte „anwendung“ am Ende; 2) Karte „sinussatz_seite“ um den Schritt „Warum? Höhe h = b · sin α = a · sin β“ erweitert.
# Alle Zeichnungen werden aus den Maßen berechnet (maßstäblich, Prüfung mit _massstab). Eigene Zufallsstarts.
import math as _m  # noqa: E402
from _luecken_kl9 import einbauen, erweitern  # noqa: E402

AN_L = 'anwendung'


def _r(p): return [round(p[0], 3), round(p[1], 3)]


def _massstab(fig, soll):
    """soll: Liste (P, Q, Länge in echter Einheit). Prüft, dass alle Strecken im selben Maßstab gezeichnet sind."""
    P = fig['punkte']
    q = [_m.dist(P[a], P[b]) / l for a, b, l in soll]
    assert max(q) - min(q) < 0.01 * max(q), ('nicht maßstäblich', soll, q)
    return fig


def _wsw(c, al, be, lab_c, lab_b='', lab_a='', w_a=None, w_b=None, w_c=None, ziel=8.0, namen=('A', 'B', 'C')):
    """Dreieck mit Grundseite c (A links, B rechts), α bei A, β bei B. Gibt Figur und b, a zurück."""
    ga = 180 - al - be
    b, a = c * sin(be) / sin(ga), c * sin(al) / sin(ga)
    s = ziel / c
    A, B, C = namen
    P = {A: [0, 0], B: _r((c * s, 0)), C: _r((b * s * cos(al), b * s * sin(al)))}
    lin = [[A, B, lab_c], [A, C, lab_b] if lab_b else [A, C], [B, C, lab_a] if lab_a else [B, C]]
    win = [x for x in ([A, B, C, w_a] if w_a else None, [B, C, A, w_b] if w_b else None, [C, A, B, w_c] if w_c else None) if x]
    fig = {'typ': 'figur', 'punkte': P, 'flaeche': [A, B, C], 'linien': lin}
    if win: fig['winkel'] = win
    return _massstab(fig, [(A, B, c), (A, C, b), (B, C, a)]), b, a


def _sws(a, b, ga, lab_a, lab_b, lab_c, w_c, ziel=8.0):
    """Dreieck mit Ecke C, Seiten CA = b, CB = a und Winkel γ bei C."""
    c = _m.sqrt(a * a + b * b - 2 * a * b * cos(ga))
    s = ziel / max(a, b)
    P = {'C': [0, 0], 'A': _r((b * s, 0)), 'B': _r((a * s * cos(ga), a * s * sin(ga)))}
    fig = {'typ': 'figur', 'punkte': P, 'flaeche': ['A', 'B', 'C'],
           'linien': [['C', 'A', lab_b], ['C', 'B', lab_a], ['A', 'B', lab_c, 'gestrichelt']], 'winkel': [['C', 'A', 'B', w_c]]}
    return _massstab(fig, [('C', 'A', b), ('C', 'B', a), ('A', 'B', c)]), c


KARTE_AN = {
    'lernziel': AN_L, 'titel': 'Vermessen und navigieren',
    'einstieg': 'Zwei Vermesser stehen am Ufer, 200 m voneinander entfernt. Beide peilen einen Baum auf der anderen Seite an. '
                'So bestimmen sie die Entfernung, ohne über den Fluss zu gehen.',
    'woerter': [['peilen', 'mit einem Messgerät den Winkel zu einem Ziel messen'],
                ['Standlinie', 'die bekannte Strecke zwischen den beiden Messpunkten'],
                ['Planfigur', 'eine Skizze, in die man alle bekannten Größen einträgt']],
    'bild': None,  # wird unten berechnet
    'schritte': [{'text': 'Planfigur: Standlinie c = 200 m, Winkel 70° bei A und 60° bei B.'},
                 {'text': 'Winkel beim Baum: 180° − 70° − 60° = ⟦50°⟧.'},
                 {'text': 'Gesucht ist b = AC. Gegenüber von b liegt der Winkel 60°.'},
                 {'text': 'Sinussatz: b = 200 m · sin 60° : sin 50° ≈ ⟦226 m⟧.'}],
    'fehler': 'Nicht 200 m · sin 70° : sin 50° rechnen. Der Winkel 70° liegt bei A, gegenüber von a. Zu b gehört der Winkel 60° bei B.',
    'regel': 'Erst eine Planfigur zeichnen, dann den Satz wählen. Paar aus Seite und Gegenwinkel bekannt: ⟦Sinussatz⟧; sonst Kosinussatz.',
    'probe': 'Der Winkel 60° ist kleiner als 70°, also ist b ≈ 226 m kürzer als a ≈ 245 m. Passt.',
}
_AN_FIG, _AN_B, _AN_A = _wsw(200, 70, 60, 'c = 200 m', w_a='70°', w_b='60°', namen=('A', 'B', 'Baum'))
KARTE_AN['bild'] = _AN_FIG
KARTE_AN['schritte'][1]['bild'] = {'winkel': [['A', 'B', 'Baum', '70°'], ['B', 'Baum', 'A', '60°'], ['Baum', 'A', 'B', '50°']]}
KARTE_AN['schritte'][2]['bild'] = {'linien': [['A', 'B', 'c = 200 m'], ['A', 'Baum', 'b = ?'], ['B', 'Baum']]}
KARTE_AN['schritte'][3]['bild'] = {'linien': [['A', 'B', 'c = 200 m'], ['A', 'Baum', 'b ≈ 226 m'], ['B', 'Baum']]}
KARTE_AN['fehler_bild'] = {'linien': [['A', 'B', 'c = 200 m'], ['A', 'Baum', 'b'], ['B', 'Baum', 'a']],
                           'winkel': [['A', 'B', 'Baum', '70° gehört zu a'], ['B', 'Baum', 'A', '60° gehört zu b']]}
assert round(_AN_B) == 226 and round(_AN_A) == 245


def _rz(w, nd):
    v = gerundet(w, nd)
    assert v is not None, (w, nd)
    return v


def _fluss(pool_vorn=''):
    while True:
        c = R.choice([120, 150, 180, 200, 240, 250, 300])
        al, be = R.choice(range(40, 85, 5)), R.choice(range(40, 85, 5))
        ga = 180 - al - be
        if ga >= 30 and al != be and (c, al, be) not in _FLUSS_GENUTZT:
            fig, b, a = _wsw(c, al, be, f'c = {c} m', 'b = ?', w_a=f'{al}°', w_b=f'{be}°')
            if gerundet(b, 1) is not None: break
    _FLUSS_GENUTZT.add((c, al, be))
    w = _rz(b, 1)
    return zahl(f'{pool_vorn}Vermessung über einen Fluss: Standlinie AB = {c} m, gepeilt werden α = {al}° bei A und β = {be}° bei B zum Punkt C. '
                f'Wie weit ist C von A entfernt? Runde auf eine Nachkommastelle.',
                f'γ = 180° − {al}° − {be}° = {ga}°. Sinussatz: b = {c} · sin {be}° : sin {ga}° ≈ {dz(w)} m.',
                'Berechne zuerst den dritten Winkel. Welcher Winkel liegt b gegenüber?', w, f'round({c} * {K(sin(be))} / {K(sin(ga))}, 1)', einheit='m',
                grafik=fig)


def _tunnel(pool_vorn=''):
    while True:
        a, b = R.choice(range(300, 950, 50)), R.choice(range(300, 950, 50))
        ga = R.choice(range(50, 125, 5))
        if a != b and ga != 90 and (a, b, ga) not in _TUNNEL_GENUTZT:
            fig, c = _sws(a, b, ga, f'{a} m', f'{b} m', '?', f'{ga}°')
            if gerundet(c, 0) is not None: break
    _TUNNEL_GENUTZT.add((a, b, ga))
    w = _rz(c, 0)
    return zahl(f'{pool_vorn}Ein Tunnel soll von A nach B durch einen Berg führen. Von einem Punkt C aus misst man CA = {b} m, CB = {a} m und '
                f'den Winkel ACB = {ga}°. Wie lang wird der Tunnel? Runde auf ganze Meter.',
                f'Zwei Seiten und der Winkel dazwischen: Kosinussatz. c² = {a}² + {b}² − 2 · {a} · {b} · cos {ga}°, c ≈ {dz(w)} m.',
                'Zwei Seiten und der Winkel dazwischen sind bekannt. Welcher Satz passt?', w,
                f'round({K(c)}, 0)', einheit='m', grafik=fig)


_FLUSS_GENUTZT, _TUNNEL_GENUTZT = {(200, 70, 60)}, set()


def anwendung_aufgaben():
    L = []

    def neu(pool, s, art, a):
        a['l'] = AN_L
        L.append((pool, s, art, a))

    # Stufe 1
    for c, al, be in ((150, 55, 65), (80, 70, 45)):
        fig, _, _ = _wsw(c, al, be, f'{c} m', w_a=f'{al}°', w_b=f'{be}°', w_c='?')
        neu('uebung', 1, '', zahl(f'Von zwei Punkten A und B ({c} m auseinander) wird ein Baum C angepeilt: α = {al}° bei A, β = {be}° bei B. Wie groß ist der Winkel beim Baum?',
                                  f'Winkelsumme im Dreieck: 180° − {al}° − {be}° = {180 - al - be}°.', 'Die drei Winkel im Dreieck ergeben zusammen 180°.',
                                  180 - al - be, f'180 - {al} - {be}', einheit='°', grafik=fig))
    fig, _ = _sws(600, 450, 75, '600 m', '450 m', '?', '75°')
    neu('uebung', 1, '', bild(auswahl('Für einen Tunnel von A nach B kennt man CA, CB und den Winkel bei C (siehe Planfigur). Welcher Satz liefert die Tunnellänge?',
                                      'Kosinussatz', ['Sinussatz', 'Satz des Pythagoras', 'Flächenformel mit dem Sinus'],
                                      'Zwei Seiten und der Winkel dazwischen (SWS): Kosinussatz. Pythagoras geht nur mit rechtem Winkel.',
                                      'Liegt der bekannte Winkel zwischen den beiden bekannten Seiten?'), fig))
    fig, _, _ = _wsw(120, 50, 75, 'c = 120 m', 'b = ?', w_a='50°', w_b='75°')
    neu('uebung', 1, '', bild(auswahl('Bekannt sind die Standlinie AB und die beiden Peilwinkel bei A und B (siehe Planfigur). Welcher Satz liefert die Entfernung AC?',
                                      'Sinussatz', ['Kosinussatz', 'Satz des Pythagoras', 'Tangens im rechtwinkligen Dreieck'],
                                      'Den Winkel bei C bekommst du aus der Winkelsumme. Dann ist ein Paar aus Seite c und Gegenwinkel γ bekannt: Sinussatz.',
                                      'Welcher Winkel liegt der Standlinie gegenüber?'), fig))
    # Stufe 2
    neu('uebung', 2, '', _fluss())
    neu('uebung', 2, '', _fluss())
    neu('uebung', 2, '', _tunnel())
    neu('uebung', 2, '', _tunnel())
    neu('uebung', 2, '', auswahl('Was wird aus dem Kosinussatz c² = a² + b² − 2ab · cos γ, wenn γ = 90° ist?', 'c² = a² + b², der Satz des Pythagoras',
                                 ['c² = a² + b² − 2ab', 'c = a + b', 'c² = a² − b²'],
                                 'cos 90° = 0, also fällt − 2ab · cos γ weg: c² = a² + b². Der Satz des Pythagoras ist ein Spezialfall des Kosinussatzes.',
                                 'Welchen Wert hat cos 90°?'))
    fig, d = _sws(8, 12, 110, '8 km', '12 km', '?', '110°')
    w = _rz(d, 1)
    neu('uebung', 2, '', zahl('Ein Schiff fährt 12 km weit, dann 8 km in eine andere Richtung. Der Winkel zwischen beiden Strecken beträgt 110°. '
                              'Wie weit ist das Schiff vom Start entfernt? Runde auf eine Nachkommastelle.',
                              f'Kosinussatz: d² = 12² + 8² − 2 · 12 · 8 · cos 110° ≈ 208 + 65,7 = 273,7, d ≈ {dz(w)} km.',
                              'Zwei Seiten und der Winkel dazwischen: Kosinussatz. cos 110° ist negativ.', w,
                              f'round({K(d)}, 1)', einheit='km', grafik=fig))
    # Stufe 3
    h = 50 * sin(30) / sin(15) * sin(45)
    s = 8 / (h / tan(30))
    F = h / tan(30)
    turm = {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': _r((50 * s, 0)), 'F': _r((F * s, 0)), 'S': _r((F * s, h * s))},
            'linien': [['A', 'B', '50 m'], ['B', 'F'], ['F', 'S', 'h = ?'], ['A', 'S'], ['B', 'S']],
            'winkel': [['A', 'F', 'S', '30°'], ['B', 'F', 'S', '45°']], 'rechter_winkel': [['F', 'A', 'S']]}
    _massstab(turm, [('A', 'B', 50), ('F', 'S', h), ('A', 'F', F)])
    w = _rz(h, 1)
    neu('uebung', 3, 'pruefung', zahl('Von Punkt A sieht man die Spitze S eines Turms unter 30° Steigung. Geht man 50 m auf den Turm zu bis B, sind es 45°. '
                                      'Wie hoch ist der Turm? Runde auf eine Nachkommastelle.',
                                      'Im Dreieck ABS: Winkel bei B = 180° − 45° = 135°, bei S = 180° − 30° − 135° = 15°. '
                                      f'Sinussatz: BS = 50 · sin 30° : sin 15° ≈ 96,6 m. Höhe h = BS · sin 45° ≈ {dz(w)} m.',
                                      'Arbeite im schiefen Dreieck ABS: Welche Winkel hat es? Danach hilft das rechtwinklige Dreieck BFS.', w,
                                      f'round(50 * {K(sin(30))} / {K(sin(15))} * {K(sin(45))}, 1)', einheit='m', grafik=turm))
    sch = 8 / 10
    Z = (10 + 6 * cos(40), 6 * sin(40))
    nav = {'typ': 'figur', 'punkte': {'Start': [0, 0], 'W': _r((10 * sch, 0)), '_V': _r((13 * sch, 0)), 'Ziel': _r((Z[0] * sch, Z[1] * sch))},
           'linien': [['Start', 'W', '10 km'], ['W', '_V', '', 'gestrichelt'], ['W', 'Ziel', '6 km'], ['Start', 'Ziel', '?', 'gestrichelt']],
           'winkel': [['W', '_V', 'Ziel', '40°']]}
    _massstab(nav, [('Start', 'W', 10), ('W', 'Ziel', 6)])
    d = _m.sqrt(100 + 36 - 120 * cos(140))
    w = _rz(d, 1)
    neu('uebung', 3, 'pruefung', zahl('Ein Schiff fährt 10 km nach Osten. Am Wendepunkt W dreht es um 40° nach links und fährt 6 km weiter. '
                                      'Wie weit ist es dann vom Start entfernt? Runde auf eine Nachkommastelle.',
                                      f'Der Dreieckswinkel bei W ist 180° − 40° = 140°. Kosinussatz: d² = 10² + 6² − 2 · 10 · 6 · cos 140° ≈ 227,9, d ≈ {dz(w)} km.',
                                      'Der Drehwinkel ist nicht der Winkel im Dreieck. Zeichne die Verlängerung des ersten Kurses.', w,
                                      f'round({K(d)}, 1)', einheit='km', grafik=nav))
    al = _m.degrees(_m.acos((40 ** 2 + 70 ** 2 - 55 ** 2) / (2 * 40 * 70)))
    gs = 8 / 70
    grund = {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': _r((70 * gs, 0)), 'C': _r((40 * gs * cos(al), 40 * gs * sin(al)))}, 'flaeche': ['A', 'B', 'C'],
             'linien': [['A', 'B', '70 m'], ['A', 'C', '40 m'], ['B', 'C', '55 m']], 'winkel': [['C', 'A', 'B', '?']]}
    _massstab(grund, [('A', 'B', 70), ('A', 'C', 40), ('B', 'C', 55)])
    gam = _m.degrees(_m.acos((40 ** 2 + 55 ** 2 - 70 ** 2) / (2 * 40 * 55)))
    w = _rz(gam, 1)
    neu('uebung', 3, 'pruefung', zahl('Ein dreieckiges Grundstück hat die Seiten 40 m, 55 m und 70 m. Wie groß ist sein größter Winkel? Runde auf eine Nachkommastelle.',
                                      f'Der größte Winkel liegt der längsten Seite (70 m) gegenüber. cos γ = (40² + 55² − 70²) : (2 · 40 · 55) = −275 : 4 400 = −0,0625, γ ≈ {dz(w)}°.',
                                      'Drei Seiten bekannt: Kosinussatz nach dem Winkel umstellen. Welcher Winkel ist der größte?', w,
                                      f'round({K(gam)}, 1)', einheit='°', grafik=grund))
    fl = 0.5 * 40 * 55 * sin(gam)
    w = _rz(fl, 0)
    neu('uebung', 3, '', zahl('Das dreieckige Grundstück mit den Seiten 40 m, 55 m und 70 m hat zwischen den Seiten 40 m und 55 m einen Winkel von etwa 93,6°. '
                              'Wie groß ist seine Fläche? Runde auf ganze m².',
                              f'A = ½ · 40 · 55 · sin 93,6° ≈ 1 100 · 0,998 ≈ {dz(w)} m².', 'Flächenformel: A = ½ · a · b · sin γ mit dem Winkel zwischen a und b.', w,
                              f'round(0.5 * 40 * 55 * {K(sin(gam))}, 0)', einheit='m²', grafik=grund))
    neu('uebung', 3, 'knobel', auswahl('Gibt es ein Dreieck mit den Seiten a = 3 cm, b = 4 cm und c = 8 cm?', 'Nein: cos γ wäre −1,625, das ist kleiner als −1.',
                                       ['Ja, γ ist dann stumpf.', 'Ja, aber es ist nicht eindeutig.', 'Nein, weil kein Winkel 90° groß ist.'],
                                       'Kosinussatz: cos γ = (9 + 16 − 64) : 24 = −1,625. Einen solchen Winkel gibt es nicht. Auch anschaulich: 3 cm + 4 cm reichen nicht für 8 cm.',
                                       'Stelle den Kosinussatz nach cos γ um. Welche Werte kann cos γ haben?'))
    fig, _, _ = _wsw(200, 70, 60, 'c = 200 m', 'b = ?', w_a='70°', w_b='60°')
    neu('uebung', 3, '', bild(auswahl('Bei einer Flussvermessung ist c = 200 m, α = 70°, β = 60° und γ = 50°. Jemand rechnet b = 200 m · sin 70° : sin 50°. Was stimmt?',
                                      'Falsch: Zu b gehört β = 60°, also b = 200 m · sin 60° : sin 50°.',
                                      ['Richtig.', 'Falsch: Es muss b = 200 m · sin 50° : sin 70° heißen.', 'Falsch: Hier braucht man den Kosinussatz.'],
                                      'Im Sinussatz stehen Seite und Gegenwinkel zusammen. b liegt gegenüber von B, also gehört β = 60° dazu. Mit 70° erhält man a.',
                                      'Welcher Winkel liegt der Seite b gegenüber?'), fig))
    fig, d = _sws(2.0, 1.2, 75, '2 km', '1,2 km', '?', '75°')
    w = _rz(d, 2)
    neu('uebung', 3, '', zahl('Von einem Aussichtspunkt sieht man zwei Hütten. Die eine ist 1,2 km entfernt, die andere 2 km. Zwischen beiden Blickrichtungen liegt ein Winkel von 75°. '
                              'Wie weit sind die Hütten voneinander entfernt? Runde auf zwei Nachkommastellen.',
                              f'Kosinussatz: d² = 1,2² + 2² − 2 · 1,2 · 2 · cos 75° ≈ 5,44 − 1,24 = 4,20, d ≈ {dz(w)} km.',
                              'Zwei Entfernungen und der Winkel dazwischen sind bekannt.', w,
                              f'round({K(d)}, 2)', einheit='km', grafik=fig))
    x = _m.degrees(_m.asin(4 * sin(70) / 5))
    third = 180 - 70 - x
    ac = 5 * sin(third) / sin(70)
    ss = 8 / 5
    segel = {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': _r((5 * ss, 0)), 'C': _r((ac * ss * cos(x), ac * ss * sin(x)))}, 'flaeche': ['A', 'B', 'C'],
             'linien': [['A', 'B', 'unten 5 m'], ['B', 'C', 'Mast 4 m'], ['A', 'C']], 'winkel': [['C', 'A', 'B', '70°'], ['A', 'B', 'C', '?']]}
    _massstab(segel, [('A', 'B', 5), ('B', 'C', 4), ('A', 'C', ac)])
    w = _rz(x, 1)
    neu('uebung', 3, '', zahl('Ein dreieckiges Segel hat unten eine 5 m lange Kante und am Mast eine 4 m lange Kante. Der Winkel gegenüber der unteren Kante beträgt 70°. '
                              'Wie groß ist der Winkel gegenüber der Mastkante? Runde auf eine Nachkommastelle.',
                              f'Sinussatz: sin x : 4 = sin 70° : 5 ⇒ sin x = 4 · sin 70° : 5 ≈ 0,752, x ≈ {dz(w)}°. Eindeutig, weil der Winkel 70° der längeren Seite gegenüberliegt.',
                              'Paar aus Seite und Gegenwinkel: 5 m und 70°. Stelle den Sinussatz nach sin x um.', w,
                              f'round({K(x)}, 1)', einheit='°', grafik=segel))
    # Test, Korrektur, Sicherung
    neu('test', 2, '', _fluss())
    neu('korrektur', 2, '', _tunnel())
    neu('korrektur', 2, '', _fluss())
    neu('korrektur', 2, '', _tunnel())
    for f in (_fluss, _tunnel, _fluss, _tunnel, _fluss, _tunnel):
        neu('sicherung', 2, '', f())
    return L


# Erweiterung „sinussatz_seite“: Herleitung über die Höhe (LehrplanPLUS: „vollziehen den Beweis des Sinussatzes nach“)
SCHRITT_SIN = {'text': 'Warum? Die Höhe ist h = b · sin α = a · sin β.',
               'bild': {'punkte': {'A': [0, 0], 'B': [11.28, 0], 'C': [9.21, 7.73], '_H': [9.21, 0]},
                        'linien': [['A', 'B', 'c'], ['B', 'C', 'a = 8 km'], ['C', 'A', 'b = 12,0 km'], ['C', '_H', 'h', 'gestrichelt']],
                        'rechter_winkel': [['_H', 'B', 'C']]}}
FEHLERBILD_SIN = {'punkte': {'A': [0, 0], 'B': [11.28, 0], 'C': [9.21, 7.73]},
                  'linien': [['A', 'B', 'c'], ['B', 'C', 'a = 8 km'], ['C', 'A', 'b = 5,3?']], 'rechter_winkel': []}


def sinussatz_aufgaben():
    L = []

    def neu(s, art, a):
        a['l'] = 'sinussatz_seite'
        L.append(('uebung', s, art, a))
    neu(2, '', auswahl('Im Dreieck ABC gilt für die Höhe h auf c: h = b · sin α und h = a · sin β. Was folgt daraus?', 'a : sin α = b : sin β',
                       ['a · sin α = b · sin β', 'a : b = sin β : sin α', 'a + b = sin α + sin β'],
                       'b · sin α = a · sin β. Teilt man beide Seiten durch sin α · sin β, erhält man b : sin β = a : sin α. Das ist der Sinussatz.',
                       'Setze beide Ausdrücke für h gleich und teile durch sin α · sin β.'))
    neu(2, '', zahl('Im Dreieck ABC ist b = 10 cm und α = 30°. Wie lang ist die Höhe h von C auf die Seite c?', 'Im rechtwinkligen Teildreieck mit der Hypotenuse b: h = b · sin α = 10 · 0,5 = 5 cm.',
                    'Die Höhe teilt das Dreieck in zwei rechtwinklige Dreiecke.', 5, '10 * 1 / 2', einheit='cm'))
    h = 9 * sin(40)
    w = gerundet(h / sin(65), 1)
    neu(3, '', zahl('Im Dreieck ABC ist b = 9 cm, α = 40° und β = 65°. Berechne zuerst die Höhe h = b · sin α und daraus a. Gib a auf eine Nachkommastelle an.',
                    f'h = 9 · sin 40° ≈ 5,79 cm. Im anderen Teildreieck gilt h = a · sin β, also a = h : sin 65° ≈ {dz(w)} cm. Der Sinussatz liefert dasselbe.',
                    'Die Höhe gehört zu beiden rechtwinkligen Teildreiecken.', w, f'round(9 * {K(sin(40))} / {K(sin(65))}, 1)', einheit='cm'))
    return L

if __name__ == '__main__':
    d = bauen('trigo.allgemein',
          'Sinus und Kosinus am Einheitskreis deuten und in beliebigen Dreiecken mit Sinussatz, Kosinussatz und Flächenformel rechnen.',
          ['Einheitskreis: Punkt (cos α | sin α); sin(180° − α) = sin α, cos(180° − α) = −cos α.', 'A = ½ · a · b · sin γ.',
           'Sinussatz: a : sin α = b : sin β = c : sin γ (Seite mit Gegenwinkel).', 'Kosinussatz: c² = a² + b² − 2ab · cos γ (SSS, SWS).'],
          [('Einheitskreis und Fläche', ['einheitskreis', 'flaeche']), ('Sinussatz', ['sinussatz_seite', 'sinussatz_winkel']),
           ('Kosinussatz', ['kosinussatz_seite', 'kosinussatz_winkel']), ('Strategie', ['satz_waehlen'])],
          ETAPPEN, GEN,
          meiden={'einheitskreis': ['cos 120°'], 'flaeche': ['a = 6 cm, b = 9 cm und den eingeschlossenen Winkel γ = 30°'],
                  'sinussatz_seite': ['α = 40°, β = 75° und a = 8 cm'], 'sinussatz_winkel': ['a = 10 cm, b = 7 cm und α = 50°'],
                  'kosinussatz_seite': ['a = 5 cm, b = 8 cm und γ = 60°'], 'kosinussatz_winkel': ['a = 3 cm, b = 5 cm, c = 7 cm']},
          offen=['Einheitskreis-Aufgaben mit Bild nutzen „figur“ mit Kreis (Koordinatensystem kann keine Kreise). Dreieckskizzen gibt es auf den Lernkarten; die Aufgaben nennen die Maße weiter in Worten.',
                 'Additionstheoreme (im „umfang“ der Themenliste genannt) sind bewusst weggelassen: Der LehrplanPLUS-Eintrag dieses Themas nennt nur Sinus- und Kosinussatz; Additionstheoreme gehören nicht zum Stoff der 9. Klasse. Bitte bei der Prüfung bestätigen.',
                 'Gleichungen wie sin α = −0,5 stehen jetzt nur noch im Thema gleichungen.trig (Prüfvorschlag); Stufe 3 von „einheitskreis“ beurteilt Aussagen.',
                 'Rechenausdruck c: Winkelfunktionswerte als 12-stellige Konstanten (Prüfskript kennt sin/cos nicht).'])
    anhaengen(d, 9912, schwer)
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden
    # Achtzehnte Runde: Lehrplan-Lücken (Anwendungen, Herleitung des Sinussatzes)
    einbauen('trigo.allgemein', KARTE_AN, None, 18_9_6, anwendung_aufgaben)
    erweitern('trigo.allgemein', 'sinussatz_seite', 18_9_7, sinussatz_aufgaben, schritt=SCHRITT_SIN, felder={'fehler_bild': FEHLERBILD_SIN})
