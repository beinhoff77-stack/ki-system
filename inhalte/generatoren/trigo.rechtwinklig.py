#!/usr/bin/env python3
"""Thema trigo.rechtwinklig – Trigonometrie im rechtwinkligen Dreieck (Klasse 9)."""
import sys
from math import isqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(911)
TRIPEL = sorted({(a, b, c) for a in range(1, 80) for b in range(1, 80)
                 for c in [isqrt(a * a + b * b)] if c * c == a * a + b * b and c <= 100 and a != b})
FUNK = {'sin': sin, 'cos': cos, 'tan': tan}


def cf(x):
    return str(float(x)) if Fr(x).denominator != 1 else str(int(x))


ETAPPEN = [
    {'lernziel': 'seiten', 'titel': 'Ankathete, Gegenkathete, Hypotenuse',
     'regel': 'Im rechtwinkligen Dreieck liegt die ⟦Hypotenuse⟧ dem rechten Winkel gegenüber. Bezogen auf einen spitzen Winkel ist die ⟦Gegenkathete⟧ die Kathete gegenüber, die ⟦Ankathete⟧ die Kathete, die am Winkel anliegt.',
     'schritte': ['Dreieck ABC mit γ = 90°: Hypotenuse ist c (gegenüber C).', 'Für α (bei A): Gegenkathete ⟦a⟧, Ankathete ⟦b⟧.'],
     'probe': 'Für β tauschen An- und Gegenkathete: Gegenkathete b, Ankathete a ✓',
     'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [5, 3], 'C': [5, 0]}, 'flaeche': ['A', 'B', 'C'], 'linien': [['A', 'C', 'Ankathete b'], ['C', 'B', 'Gegenkathete a'], ['A', 'B', 'Hypotenuse c']], 'rechter_winkel': [['C', 'A', 'B']], 'winkel': [['A', 'C', 'B', 'α']]},
     'fehler': '„Die Ankathete von α ist c, weil c an A anliegt“ ist falsch: c liegt zwar an A, ist aber die ⟦Hypotenuse⟧. Ankathete ist nur eine ⟦Kathete⟧.'},
    {'lernziel': 'verhaeltnisse', 'titel': 'Sinus, Kosinus, Tangens als Verhältnis',
     'regel': '⟦sin α = Gegenkathete : Hypotenuse⟧, ⟦cos α = Ankathete : Hypotenuse⟧, ⟦tan α = Gegenkathete : Ankathete⟧. Warum hängen diese Verhältnisse ⟦nur vom Winkel⟧ ab? Alle rechtwinkligen Dreiecke mit demselben α sind ⟦ähnlich⟧ – ein großes ist nur ein vergrößertes kleines. Beim Vergrößern bleiben die Seitenverhältnisse gleich.',
     'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [15, 8], 'C': [15, 0]}, 'flaeche': ['A', 'B', 'C'], 'linien': [['A', 'C', 'b = 15 cm'], ['C', 'B', 'a = 8 cm'], ['A', 'B', 'c = 17 cm']], 'rechter_winkel': [['C', 'A', 'B']], 'winkel': [['A', 'C', 'B', 'α']]},
     'schritte': ['γ = 90°, a = 8 cm, b = 15 cm, c = 17 cm.', 'sin α = 8/17, cos α = 15/17, ⟦tan α = 8/15⟧.'],
     'probe': 'sin α und cos α sind kleiner als 1 (Hypotenuse ist am längsten) ✓',
     'fehler': 'sin α = b/c ist falsch, wenn γ = 90°: b ist die ⟦Ankathete⟧ von α. Richtig: sin α = a/c.'},
    {'lernziel': 'seite', 'titel': 'Seitenlängen berechnen',
     'regel': 'Wähle die Funktion, in der die ⟦gesuchte und die bekannte Seite⟧ vorkommen. Stelle um, z. B. ⟦a = c · sin α⟧ oder ⟦c = a : sin α⟧.',
     'schritte': ['γ = 90°, α = 35°, c = 10 cm, gesucht a (Gegenkathete von α).', 'a = 10 cm · sin 35° ≈ 10 · 0,5736 ≈ ⟦5,7 cm⟧.'],
     'probe': 'a < c ✓',
     'fehler': 'a = 10 : sin 35° ≈ 17,4 cm ist falsch: Aus sin α = a/c folgt a = ⟦c · sin α⟧. Eine Kathete kann nicht länger als die Hypotenuse sein.'},
    {'lernziel': 'winkel', 'titel': 'Winkel berechnen',
     'regel': 'Kennst du zwei Seiten, berechnest du das Verhältnis und benutzt die ⟦Umkehrtaste⟧: α = sin⁻¹(…), cos⁻¹(…) oder tan⁻¹(…). Der Taschenrechner muss auf ⟦DEG⟧ stehen.',
     'schritte': ['γ = 90°, a = 4 cm, b = 7 cm: tan α = 4/7 ≈ 0,5714.', 'α = tan⁻¹(4/7) ≈ ⟦29,7°⟧.'],
     'probe': 'β = 90° − 29,7° = 60,3°; tan 60,3° ≈ 1,75 = 7/4 ✓',
     'fehler': 'α = 4/7 ≈ 0,57° ist falsch: 4/7 ist der ⟦Tangenswert⟧, nicht der Winkel. Erst tan⁻¹ liefert den Winkel.'},
    {'lernziel': 'beziehungen', 'titel': 'Beziehungen zwischen sin, cos, tan',
     'regel': 'Für spitze Winkel gilt ⟦sin² α + cos² α = 1⟧. Warum? Das ist Pythagoras: a² + b² = c², geteilt durch c², ergibt (a/c)² + (b/c)² = 1. Außerdem: ⟦tan α = sin α : cos α⟧ und ⟦sin α = cos(90° − α)⟧. Besondere Werte: sin 30° = cos 60° = 0,5; tan 45° = 1.',
     'schritte': ['sin α = 0,28 (α spitz): cos² α = 1 − 0,0784 = 0,9216.', 'cos α = ⟦0,96⟧, tan α = 0,28 : 0,96 = 7/24.'],
     'probe': '0,28² + 0,96² = 0,0784 + 0,9216 = 1 ✓',
     'fehler': 'cos α = 1 − sin α = 0,72 ist falsch: Es gilt sin² α + cos² α = 1 – mit den ⟦Quadraten⟧.'},
    {'lernziel': 'anwendung', 'titel': 'Trigonometrie anwenden',
     'regel': 'Skizze, ⟦rechtwinkliges Dreieck⟧ finden, Winkel und Seiten zuordnen. ⟦Steigung in %⟧ = tan(Steigungswinkel) · 100. ⟦Höhenwinkel⟧ wird von der Waagrechten aus gemessen.',
     'schritte': ['Eine Straße steigt mit 8 %: tan α = 0,08.', 'α = tan⁻¹(0,08) ≈ ⟦4,6°⟧.'],
     'probe': '8 m Höhe auf 100 m waagrecht ✓',
     'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], '_C': [100, 0], '_B': [100, 8]}, 'flaeche': ['A', '_C', '_B'], 'linien': [['A', '_C', '100 m waagrecht'], ['_C', '_B', '8 m'], ['A', '_B']], 'rechter_winkel': [['_C', 'A', '_B']], 'winkel': [['A', '_C', '_B', 'α']]},
     'fehler': '8 % Steigung als Winkel 8° anzugeben ist falsch: 8 % bedeutet ⟦tan α = 0,08⟧, also etwa 4,6°.'},
]

# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'seiten': {
  'einstieg': 'Eine Rampe führt schräg auf eine Bühne. Von unten gesehen gibt es den Boden, die senkrechte Bühnenkante und die schräge Rampe selbst. Damit man über diese drei Seiten reden kann, bekommen sie Namen – je nachdem, von welchem Winkel aus man schaut. Die Namen ⟦Ankathete, Gegenkathete, Hypotenuse⟧ helfen dabei.',
  'woerter': [['Hypotenuse', 'die längste Seite, gegenüber dem rechten Winkel – hier die Rampe'],
              ['Gegenkathete von α', 'die Kathete, die dem Winkel α gegenüberliegt – hier die Bühnenkante'],
              ['Ankathete von α', 'die Kathete, die den Winkel α mitbildet – hier der Boden'],
              ['α, β, γ', 'griechische Buchstaben für die Winkel bei A, B und C'],
              ['spitzer Winkel', 'ein Winkel kleiner als 90°']],
  'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [5, 3], 'C': [5, 0]}, 'flaeche': ['A', 'B', 'C'], 'linien': [['A', 'C', 'Ankathete b (Boden)'], ['C', 'B', 'Gegenkathete a (Bühnenkante)'], ['A', 'B', 'Hypotenuse c (Rampe)']], 'rechter_winkel': [['C', 'A', 'B']], 'winkel': [['A', 'C', 'B', 'α']]},
  'schritte': ['Im Dreieck ABC ist der Winkel bei C ein rechter: γ = 90°.',
               'Dem rechten Winkel liegt c gegenüber. Also ist c die Hypotenuse.',
               'Vom Winkel α bei A aus gesehen liegt a gegenüber. Also ist ⟦a die Gegenkathete⟧.',
               'Die Kathete b bildet den Winkel α mit. Also ist ⟦b die Ankathete⟧.'],
  'regel': 'So benennst du die Seiten: Zuerst die ⟦Hypotenuse⟧ suchen, sie liegt dem rechten Winkel gegenüber. Dann vom gewählten spitzen Winkel aus: Die Kathete gegenüber ist die ⟦Gegenkathete⟧, die anliegende Kathete die ⟦Ankathete⟧. Wechselt der Winkel, tauschen die beiden Namen.',
  'fehler': '„Die Ankathete von α ist c, weil c an A anliegt“ ist falsch: c liegt zwar an A, ist aber die ⟦Hypotenuse⟧ (die Rampe). Ankathete ist nur eine ⟦Kathete⟧.'},
 'verhaeltnisse': {
  'einstieg': 'Zwei Rampen haben dieselbe Neigung, aber eine ist doppelt so lang. Dann ist auch ihre Höhe doppelt so groß – das Verhältnis Höhe zu Länge bleibt gleich. Es hängt also nur vom Winkel ab. Diese Verhältnisse heißen ⟦Sinus, Kosinus und Tangens⟧.',
  'woerter': [['sin α („Sinus“)', 'Gegenkathete geteilt durch Hypotenuse'],
              ['cos α („Kosinus“)', 'Ankathete geteilt durch Hypotenuse'],
              ['tan α („Tangens“)', 'Gegenkathete geteilt durch Ankathete'],
              ['8/17', 'der Bruch 8 geteilt durch 17'],
              ['ähnlich', 'gleiche Form, nur vergrößert oder verkleinert']],
  'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [15, 8], 'C': [15, 0]}, 'flaeche': ['A', 'B', 'C'], 'linien': [['A', 'C', 'Ankathete b = 15 cm'], ['C', 'B', 'Gegenkathete a = 8 cm'], ['A', 'B', 'Hypotenuse c = 17 cm']], 'rechter_winkel': [['C', 'A', 'B']], 'winkel': [['A', 'C', 'B', 'α']]},
  'schritte': ['Im Dreieck ist γ = 90°, a = 8 cm, b = 15 cm und c = 17 cm.',
               'Von α aus: Gegenkathete a = 8, Ankathete b = 15, Hypotenuse c = 17.',
               'sin α = Gegenkathete : Hypotenuse = 8/17; cos α = Ankathete : Hypotenuse = 15/17.',
               'tan α = Gegenkathete : Ankathete = ⟦8/15⟧.'],
  'regel': 'So bildest du die drei Verhältnisse: ⟦sin α = Gegenkathete : Hypotenuse⟧, ⟦cos α = Ankathete : Hypotenuse⟧, ⟦tan α = Gegenkathete : Ankathete⟧. Sie hängen ⟦nur vom Winkel⟧ ab, weil alle rechtwinkligen Dreiecke mit demselben α ⟦ähnlich⟧ sind: Beim Vergrößern bleiben die Seitenverhältnisse gleich.',
  'fehler': 'sin α = b/c ist falsch, wenn γ = 90°: b ist der Boden, also die ⟦Ankathete⟧ von α. Richtig: sin α = a/c.'},
 'seite': {
  'einstieg': 'Eine 10 m lange Rampe steigt mit 35° an. Wie hoch kommt man oben an? Winkel und schräge Länge sind bekannt, gesucht ist die Höhe. Mit dem passenden Verhältnis und dem Taschenrechner lassen sich ⟦Seitenlängen berechnen⟧.',
  'woerter': [['sin 35°', 'der Sinuswert von 35°, aus dem Taschenrechner: etwa 0,5736'],
              ['umstellen', 'die Gleichung so umformen, dass die gesuchte Seite allein steht'],
              ['≈', '„ungefähr gleich“ – nach dem Runden']],
  'schritte': ['Gegeben: γ = 90°, α = 35°, Hypotenuse c = 10 m. Gesucht ist die Höhe a, die Gegenkathete von α.',
               'Gegenkathete und Hypotenuse kommen im Sinus vor: sin 35° = a / 10.',
               'Mit 10 malnehmen: a = 10 · sin 35°.',
               'Taschenrechner: a ≈ 10 · 0,5736 ≈ ⟦5,7⟧. Die Rampe endet etwa 5,7 m hoch.'],
  'probe': 'a < c ✓',
  'regel': 'So berechnest du eine Seite: Wähle die Funktion, in der die ⟦gesuchte und die bekannte Seite⟧ vorkommen. Stelle um, z. B. ⟦a = c · sin α⟧ oder ⟦c = a : sin α⟧.',
  'fehler': 'a = 10 : sin 35° ≈ 17,4 ist falsch: Die Höhe wäre größer als die Rampe lang ist. Aus sin α = a/c folgt a = ⟦c · sin α⟧.'},
 'winkel': {
  'einstieg': 'Eine Rampe ist 7 m lang am Boden und 4 m hoch. Ist sie zu steil? Dafür braucht man ihren Winkel. Bekannt ist das Verhältnis 4 : 7, gesucht der passende Winkel. Diesen Rückweg vom Verhältnis zum Winkel macht die ⟦Umkehrtaste⟧ des Taschenrechners.',
  'woerter': [['tan⁻¹ („Arkustangens“)', 'die Umkehrtaste: Sie macht aus einem Tangenswert den Winkel'],
              ['sin⁻¹, cos⁻¹', 'die Umkehrtasten zu Sinus und Kosinus'],
              ['DEG', 'Einstellung des Taschenrechners für Winkel in Grad']],
  'schritte': ['Gegeben: γ = 90°, Gegenkathete a = 4 m, Ankathete b = 7 m. Gesucht ist α.',
               'Gegenkathete und Ankathete kommen im Tangens vor: tan α = 4/7 ≈ 0,5714.',
               'Den Taschenrechner auf DEG stellen und die Umkehrtaste nutzen: α = tan⁻¹(4/7).',
               'Ergebnis: α ≈ ⟦29,7°⟧.'],
  'regel': 'So berechnest du einen Winkel: Bilde aus zwei bekannten Seiten das passende Verhältnis. Dann die ⟦Umkehrtaste⟧ benutzen: α = sin⁻¹(…), cos⁻¹(…) oder tan⁻¹(…). Der Taschenrechner muss auf ⟦DEG⟧ stehen.',
  'fehler': 'α = 4/7 ≈ 0,57° ist falsch: Eine Rampe von 4 m Höhe auf 7 m wäre dann fast flach. 4/7 ist der ⟦Tangenswert⟧, nicht der Winkel. Erst tan⁻¹ liefert den Winkel.'},
 'beziehungen': {
  'einstieg': 'Sinus, Kosinus und Tangens hängen eng zusammen. Kennt man einen davon, kann man die anderen ausrechnen, ohne das Dreieck zu messen. Der Grund ist der Satz des Pythagoras. Diese Zusammenhänge heißen ⟦Beziehungen zwischen sin, cos und tan⟧.',
  'woerter': [['sin² α', '(sin α)², also sin α mal sin α'],
              ['sin² α + cos² α = 1', 'Pythagoras, geteilt durch c²'],
              ['90° − α', 'der andere spitze Winkel im rechtwinkligen Dreieck']],
  'schritte': ['Bekannt ist sin α = 0,28, α ist spitz. Gesucht sind cos α und tan α.',
               'Aus sin² α + cos² α = 1 folgt cos² α = 1 − 0,28² = 1 − 0,0784 = 0,9216.',
               'Die Wurzel ziehen: cos α = ⟦0,96⟧ (positiv, weil α spitz ist).',
               'tan α = sin α : cos α = 0,28 : 0,96 = 7/24.'],
  'regel': 'So nutzt du die Beziehungen für spitze Winkel: ⟦sin² α + cos² α = 1⟧ – das ist Pythagoras a² + b² = c², geteilt durch c². Außerdem gilt ⟦tan α = sin α : cos α⟧ und ⟦sin α = cos(90° − α)⟧. Besondere Werte: sin 30° = cos 60° = 0,5; tan 45° = 1.',
  'fehler': 'cos α = 1 − sin α = 0,72 ist falsch: Es gilt sin² α + cos² α = 1 – mit den ⟦Quadraten⟧. Probe: 0,28² + 0,72² ≈ 0,60, nicht 1.'},
 'anwendung': {
  'einstieg': 'Ein Verkehrsschild zeigt „8 %“ an einer Bergstraße. Das bedeutet: Auf 100 m waagrecht geht es 8 m nach oben. Wie steil ist das als Winkel? Höhe und waagrechter Weg bilden ein rechtwinkliges Dreieck. So kann man ⟦Trigonometrie anwenden⟧.',
  'woerter': [['Steigung in %', 'Höhenunterschied pro 100 m waagrecht'],
              ['Steigungswinkel', 'der Winkel zwischen Straße und Waagrechter'],
              ['Höhenwinkel', 'der Winkel, unter dem man nach oben schaut, gemessen von der Waagrechten'],
              ['Trigonometrie', 'das Rechnen mit Winkeln und Seiten im Dreieck']],
  'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], '_C': [100, 0], '_B': [100, 8]}, 'flaeche': ['A', '_C', '_B'], 'linien': [['A', '_C', '100 m waagrecht'], ['_C', '_B', '8 m hoch'], ['A', '_B', 'Straße']], 'rechter_winkel': [['_C', 'A', '_B']], 'winkel': [['A', '_C', '_B', 'α']]},
  'schritte': ['Die Straße steigt mit 8 %: 8 m Höhe auf 100 m waagrecht.',
               'Höhe ist die Gegenkathete, der waagrechte Weg die Ankathete: tan α = 8 : 100 = 0,08.',
               'Umkehrtaste: α = tan⁻¹(0,08).',
               'Ergebnis: α ≈ ⟦4,6°⟧.'],
  'regel': 'So wendest du Trigonometrie an: ⟦Skizze⟧ zeichnen, das ⟦rechtwinklige Dreieck⟧ finden, Winkel und Seiten zuordnen. Es gilt ⟦Steigung in %⟧ = tan(Steigungswinkel) · 100. Der ⟦Höhenwinkel⟧ wird von der Waagrechten aus gemessen.',
  'fehler': '8 % Steigung als Winkel 8° anzugeben ist falsch: 8 % bedeutet ⟦tan α = 0,08⟧, also etwa 4,6°. Prozent und Grad sind verschiedene Maße.'},
}
klar(ETAPPEN, KLAR)
# ---- KLAR ENDE ----
# ---- UMBAU (neues Muster, Runde 8, Vorgabe 16.11.) ----
def _dr(punkte, a, b, c, w='α'):
    return {'typ': 'figur', 'punkte': punkte, 'flaeche': ['A', 'B', 'C'],
            'linien': [['A', 'C', b], ['C', 'B', a], ['A', 'B', c]], 'rechter_winkel': [['C', 'A', 'B']], 'winkel': [['A', 'C', 'B', w]]}
_P1 = {'A': [0, 0], 'B': [5, 3], 'C': [5, 0]}
_P2 = {'A': [0, 0], 'B': [15, 8], 'C': [15, 0]}
_P3 = {'A': [0, 0], 'B': [8.19, 5.74], 'C': [8.19, 0]}
_P4 = {'A': [0, 0], 'B': [7, 4], 'C': [7, 0]}
_P5 = {'A': [0, 0], 'B': [24, 7], 'C': [24, 0]}
_P6 = {'A': [0, 0], 'B': [100, 8], 'C': [100, 0]}
L = lambda a, b, c: {'linien': [['A', 'C', b], ['C', 'B', a], ['A', 'B', c]]}
UMBAU = {
 'seiten': {
  'einstieg': 'Eine Rampe führt schräg auf eine Bühne. Boden, Bühnenkante und Rampe bilden ein rechtwinkliges Dreieck. Vom Winkel unten aus bekommen die Seiten Namen: ⟦Ankathete, Gegenkathete, Hypotenuse⟧.',
  'woerter': [['Hypotenuse', 'die längste Seite, gegenüber dem rechten Winkel'],
              ['Gegenkathete', 'die Kathete, die dem Winkel gegenüberliegt'],
              ['Ankathete', 'die Kathete, die den Winkel mitbildet']],
  'bild': _dr(_P1, 'a', 'b', 'c'),
  'schritte': [{'text': 'Dem rechten Winkel liegt die Rampe c gegenüber: die Hypotenuse.', 'bild': L('a', 'b', 'c: Hypotenuse')},
               {'text': 'Vom Winkel α aus liegt a gegenüber: die Gegenkathete.', 'bild': L('a: Gegenk.', 'b', 'c: Hypotenuse')},
               {'text': 'b bildet den Winkel α mit: ⟦b ist die Ankathete⟧.', 'bild': L('a: Gegenk.', 'b: Ankathete', 'c: Hypotenuse')},
               {'text': 'Für den anderen spitzen Winkel β tauschen die beiden Namen.'}],
  'fehler': 'c ist nicht die Ankathete, nur weil c am Winkel α liegt. c ist die Hypotenuse, die Rampe.',
  'fehler_bild': L('a', 'b', 'c: Ankathete? nein'),
  'regel': 'Erst die ⟦Hypotenuse⟧ suchen, dann vom Winkel aus benennen. Gegenüber liegt die Gegenkathete, daneben die Ankathete.'},
 'verhaeltnisse': {
  'einstieg': 'Zwei Rampen haben dieselbe Neigung, eine ist doppelt so lang. Dann ist sie auch doppelt so hoch. Das Verhältnis hängt nur vom Winkel ab: ⟦Sinus, Kosinus, Tangens⟧.',
  'woerter': [['sin α', 'Sinus: Gegenkathete geteilt durch Hypotenuse'],
              ['cos α', 'Kosinus: Ankathete geteilt durch Hypotenuse'],
              ['tan α', 'Tangens: Gegenkathete geteilt durch Ankathete']],
  'bild': _dr(_P2, 'a = 8', 'b = 15', 'c = 17'),
  'schritte': [{'text': 'Von α aus: Gegenkathete 8, Ankathete 15, Hypotenuse 17.'},
               {'text': 'sin α = Gegenkathete : Hypotenuse = 8/17.'},
               {'text': 'cos α = Ankathete : Hypotenuse = 15/17.'},
               {'text': 'tan α = Gegenkathete : Ankathete = ⟦8/15⟧.'}],
  'fehler': 'sin α ist nicht b/c. b ist der Boden, also die Ankathete von α. Richtig ist sin α = a/c.',
  'regel': 'sin = ⟦Gegenkathete : Hypotenuse⟧, cos = Ankathete : Hypotenuse. tan = Gegenkathete : Ankathete.'},
 'seite': {
  'einstieg': 'Eine 10 m lange Rampe steigt mit 35° an. Wie hoch kommt man oben an? Mit dem Sinus kannst du ⟦Seitenlängen berechnen⟧.',
  'woerter': [['sin 35°', 'der Sinuswert von 35°, etwa 0,574 (Taschenrechner)'],
              ['umstellen', 'die Gleichung so umformen, dass das Gesuchte allein steht']],
  'bild': _dr(_P3, 'a = ?', 'Boden', 'Rampe 10 m', '35°'),
  'schritte': [{'text': 'Gegeben: Hypotenuse 10 m und α = 35°. Gesucht: Gegenkathete a.'},
               {'text': 'Im Sinus stehen beide: sin 35° = a : 10.'},
               {'text': 'Umstellen: a = 10 · sin 35° ≈ 10 · 0,574.'},
               {'text': 'Also ⟦a ≈ 5,7 m⟧.', 'bild': L('a = 5,7 m', 'Boden', 'Rampe 10 m')}],
  'fehler': 'a = 10 : sin 35° ≈ 17,4 m ist falsch. Die Höhe wäre länger als die ganze Rampe.',
  'fehler_bild': L('a = 17,4?', 'Boden', 'Rampe 10 m'),
  'regel': 'Wähle die Funktion mit ⟦gesuchter und bekannter Seite⟧. Dann umstellen, z. B. a = c · sin α.'},
 'winkel': {
  'einstieg': 'Eine Rampe ist am Boden 7 m lang und 4 m hoch. Wie steil ist sie? Vom Verhältnis zum Winkel kommst du mit der ⟦Umkehrtaste⟧.',
  'woerter': [['tan⁻¹', 'die Umkehrtaste: Sie macht aus einem Tangenswert den Winkel'],
              ['DEG', 'Einstellung des Taschenrechners für Grad']],
  'bild': _dr(_P4, '4 m', '7 m', 'Rampe', 'α = ?'),
  'schritte': [{'text': 'Gegenkathete 4 m, Ankathete 7 m: tan α = 4 : 7 ≈ 0,571.'},
               {'text': 'Taschenrechner auf DEG, dann tan⁻¹(4 : 7).'},
               {'text': 'Ergebnis: ⟦α ≈ 29,7°⟧.', 'bild': {'winkel': [['A', 'C', 'B', '29,7°']]}}],
  'fehler': 'α ist nicht 0,57°. 4/7 ist der Tangenswert. Erst tan⁻¹ macht daraus den Winkel.',
  'regel': 'Verhältnis bilden, dann die ⟦Umkehrtaste⟧ sin⁻¹, cos⁻¹ oder tan⁻¹. Der Rechner muss auf DEG stehen.'},
 'beziehungen': {
  'einstieg': 'Sinus, Kosinus und Tangens hängen zusammen. Kennst du einen, rechnest du die anderen aus. Der Grund ist der Satz des Pythagoras: Das sind die ⟦Beziehungen⟧.',
  'woerter': [['sin² α', '(sin α)², also sin α mal sin α'],
              ['Beziehungen', 'Formeln, die sin, cos und tan verbinden']],
  'bild': _dr(_P5, 'a = 7', 'b = 24', 'c = 25'),
  'schritte': [{'text': 'Bekannt ist sin α = 0,28. Im Bild: 7 : 25 = 0,28.'},
               {'text': 'Pythagoras geteilt durch c²: sin² α + cos² α = 1.'},
               {'text': 'cos² α = 1 − 0,0784 = 0,9216, also ⟦cos α = 0,96⟧.'},
               {'text': 'tan α = 0,28 : 0,96 = 7/24.'}],
  'fehler': 'cos α ist nicht 1 − 0,28 = 0,72. Die Formel gilt mit den Quadraten: sin² α + cos² α = 1.',
  'regel': 'Es gilt ⟦sin² α + cos² α = 1⟧. Außerdem ist tan α = sin α : cos α.'},
 'anwendung': {
  'einstieg': 'Ein Schild zeigt 8 % an einer Bergstraße. Auf 100 m waagrecht geht es 8 m hoch. Wie steil ist das in Grad? Hier hilft ⟦Trigonometrie⟧.',
  'woerter': [['Steigung in %', 'Höhenunterschied auf 100 m waagrecht'],
              ['Trigonometrie', 'Rechnen mit Winkeln und Seiten im Dreieck']],
  'bild': _dr(_P6, '8 m', '100 m waagrecht', 'Straße', 'α = ?'),
  'schritte': [{'text': 'Die Steigung in % sagt: Gegenkathete 8 m, Ankathete 100 m.'},
               {'text': 'tan α = 8 : 100 = 0,08.'},
               {'text': 'α = tan⁻¹(0,08) ≈ ⟦4,6°⟧.', 'bild': {'winkel': [['A', 'C', 'B', '4,6°']]}}],
  'fehler': '8 % sind nicht 8°. 8 % heißt tan α = 0,08, also etwa 4,6°.',
  'fehler_bild': {'winkel': [['A', 'C', 'B', '8°? nein']]},
  'regel': 'Steigung in % = ⟦tan α · 100⟧. Mach eine Skizze und finde das rechtwinklige Dreieck.'},
}
umbau(ETAPPEN, UMBAU)
# ---- UMBAU ENDE ----


def g_seiten(s):
    if s <= 2 and R.random() < (0.5 if s == 2 else 0.35):
        n = R.sample(['P', 'Q', 'R', 'K', 'L', 'M', 'D', 'E', 'F', 'A', 'B', 'C'], 3)
        rw, w, d = n  # rechter Winkel bei rw, markierter Winkel bei w
        bx, hy = R.randint(4, 8), R.randint(3, 6)
        lage = R.choice([0, 1])
        P_ = {w: [0, 0], rw: [bx, 0], d: [bx, hy]} if lage == 0 else {w: [bx, 0], rw: [0, 0], d: [0, hy]}
        art = R.choice(['Gegenkathete', 'Ankathete', 'Hypotenuse'])
        r = {'Gegenkathete': ''.join(sorted(rw + d)), 'Ankathete': ''.join(sorted(w + rw)), 'Hypotenuse': ''.join(sorted(w + d))}[art]
        g = {'typ': 'figur', 'punkte': P_, 'flaeche': [w, rw, d], 'linien': [[w, rw], [rw, d], [w, d]],
             'rechter_winkel': [[rw, w, d]], 'winkel': [[w, rw, d, '']]}
        frage = (f'Welche Strecke ist die {art} des markierten Winkels bei {w}?' if art != 'Hypotenuse' else 'Welche Strecke ist die Hypotenuse?')
        return bild(auswahl(frage, r, [''.join(sorted(rw + d)), ''.join(sorted(w + rw)), ''.join(sorted(w + d))],
                            f'Hypotenuse ist {"".join(sorted(w + d))} (gegenüber dem rechten Winkel bei {rw}). Am Winkel bei {w} liegt {"".join(sorted(w + rw))} an, gegenüber liegt {"".join(sorted(rw + d))}.',
                            'Suche zuerst den rechten Winkel: Gegenüber liegt die Hypotenuse.'), g)
    if s < 3:
        w = R.choice(['α', 'β'])
        art = R.choice(['Gegenkathete', 'Ankathete', 'Hypotenuse'])
        r = {('α', 'Gegenkathete'): 'a', ('α', 'Ankathete'): 'b', ('β', 'Gegenkathete'): 'b', ('β', 'Ankathete'): 'a'}.get((w, art), 'c')
        frage = f'Welche Seite ist die {art} von {w}?' if art != 'Hypotenuse' else 'Welche Seite ist die Hypotenuse?'
        if s == 1:
            return auswahl(f'Im Dreieck ABC ist γ = 90°. {frage}', r, ['a', 'b', 'c'],
                           f'Hypotenuse c liegt gegenüber dem rechten Winkel. Für {w}: Gegenkathete {"a" if w == "α" else "b"}, Ankathete {"b" if w == "α" else "a"}.',
                           'Welche Seite liegt dem Winkel gegenüber, welche liegt an ihm an?')
        rechts = R.choice(['α', 'β'])
        andere = 'β' if rechts == 'α' else 'α'
        hyp = 'a' if rechts == 'α' else 'b'
        w2 = R.choice([andere, 'γ'])
        tab = {('β', 'γ', 'Gegenkathete'): 'c', ('β', 'γ', 'Ankathete'): 'b', ('α', 'γ', 'Gegenkathete'): 'c', ('α', 'γ', 'Ankathete'): 'a'}
        if art == 'Hypotenuse':
            r = hyp
        elif w2 == 'γ':
            r = tab[(andere, 'γ', art)]
        else:
            r = {'Gegenkathete': 'b' if andere == 'β' else 'a', 'Ankathete': 'c'}[art]
        frage = f'Welche Seite ist die {art} von {w2}?' if art != 'Hypotenuse' else 'Welche Seite ist die Hypotenuse?'
        return auswahl(f'Im Dreieck ABC ist {rechts} = 90°. {frage}', r, ['a', 'b', 'c'],
                       f'Der rechte Winkel liegt bei {"A" if rechts == "α" else "B"}, also ist {hyp} die Hypotenuse.' + (f' Die {art} von {w2} ist {r}.' if art != 'Hypotenuse' else ''),
                       'Bestimme zuerst die Hypotenuse: Sie liegt dem rechten Winkel gegenüber.')
    pkt = R.sample(['P', 'Q', 'R', 'K', 'L', 'M', 'D', 'E', 'F'], 3)
    recht, w, dritt = pkt
    art = R.choice(['Gegenkathete', 'Ankathete'])
    r = f'{recht}{dritt}' if art == 'Gegenkathete' else f'{w}{recht}'
    return auswahl(f'Im Dreieck {"".join(sorted(pkt))} ist der Winkel bei {recht} ein rechter. Welche Strecke ist die {art} des Winkels bei {w}?', r,
                   [f'{w}{dritt}', f'{recht}{dritt}', f'{w}{recht}'],
                   f'Hypotenuse ist {w}{dritt} (gegenüber {recht}). Am Winkel bei {w} liegt die Kathete {w}{recht} an; gegenüber liegt {recht}{dritt}.',
                   'Hypotenuse zuerst: gegenüber dem rechten Winkel.')


def g_verhaeltnisse(s):
    if s == 1:
        f, w = R.choice(list(FUNK)), R.choice(['α', 'β'])
        gg, an = ('a', 'b') if w == 'α' else ('b', 'a')
        r = {'sin': f'{gg}/c', 'cos': f'{an}/c', 'tan': f'{gg}/{an}'}[f]
        return auswahl(f'Im Dreieck ABC ist γ = 90°. Welcher Term ist {f} {w}?', r, [f'{gg}/c', f'{an}/c', f'{gg}/{an}', f'{an}/{gg}'],
                       f'{f} = {"Gegenkathete : Hypotenuse" if f == "sin" else "Ankathete : Hypotenuse" if f == "cos" else "Gegenkathete : Ankathete"}; für {w} ist {gg} die Gegenkathete, {an} die Ankathete: {f} {w} = {r}.',
                       'Bestimme zu dem Winkel zuerst An- und Gegenkathete.')
    if s == 3 and R.random() < 0.35:
        rechts = R.choice(['α', 'β'])
        hyp = 'a' if rechts == 'α' else 'b'
        wi = R.choice([x for x in ['α', 'β', 'γ'] if x != rechts])
        ecke = {'α': 'a', 'β': 'b', 'γ': 'c'}
        gg = ecke[wi]
        an = ({'a', 'b', 'c'} - {hyp, gg}).pop()
        f = R.choice(list(FUNK))
        r = {'sin': f'{gg}/{hyp}', 'cos': f'{an}/{hyp}', 'tan': f'{gg}/{an}'}[f]
        return auswahl(f'Im Dreieck ABC ist {rechts} = 90°. Welcher Term ist {f} {wi}?', r,
                       [f'{gg}/{hyp}', f'{an}/{hyp}', f'{gg}/{an}', f'{an}/{gg}', f'{gg}/c' if hyp != 'c' else f'{hyp}/{gg}'],
                       f'Hypotenuse ist {hyp} (gegenüber dem rechten Winkel). Für {wi}: Gegenkathete {gg}, Ankathete {an}. Also {f} {wi} = {r}.',
                       'Achtung: Der rechte Winkel liegt nicht bei C. Bestimme zuerst die Hypotenuse.')
    a, b, c = R.choice(TRIPEL)
    f = R.choice(list(FUNK))
    w = R.choice(['α', 'β'])
    gg, an = (a, b) if w == 'α' else (b, a)
    q = {'sin': Fr(gg, c), 'cos': Fr(an, c), 'tan': Fr(gg, an)}[f]
    if not endlich(q) or q.denominator > 100: return None
    if s == 3 and R.random() < 0.5:
        k = R.choice([Fr(1, 10), Fr(1, 2), 2, 3])
        a, b, c = a * k, b * k, c * k
        if not all(endlich(x) for x in (a, b, c)): return None
        gg, an = (a, b) if w == 'α' else (b, a)
        return zahl(f'Im Dreieck ABC ist γ = 90°, a = {dz(a)} cm, b = {dz(b)} cm. Berechne zuerst c und dann {f} {w} als Dezimalzahl.',
                    f'c = √({dz(a * a)} + {dz(b * b)}) = {dz(c)} cm; {f} {w} = {dz(gg if f != "cos" else an)} : {dz(c if f != "tan" else an)} = {dz(q)}.',
                    'Erst Pythagoras, dann das passende Verhältnis.', q,
                    f'{cf(gg if f != "cos" else an)} / ({cf(a)} ** 2 + {cf(b)} ** 2) * {cf(c)}' if f != 'tan' else f'{cf(gg)} / {cf(an)}')
    return zahl(f'Im Dreieck ABC ist γ = 90°, a = {a} cm, b = {b} cm, c = {c} cm. Berechne {f} {w} als Dezimalzahl.',
                f'{f} {w} = {"Gegenkathete : Hypotenuse" if f == "sin" else "Ankathete : Hypotenuse" if f == "cos" else "Gegenkathete : Ankathete"} = {gg if f != "cos" else an} : {c if f != "tan" else an} = {dz(q)}.',
                'Welche Seiten gehören zu diesem Winkel und dieser Funktion?', q,
                f'{gg if f != "cos" else an} / {c if f != "tan" else an}')


def g_seite(s):
    al = R.randint(12, 78)
    if s == 1:
        c = R.randint(4, 20)
        f = R.choice(['sin', 'cos'])
        wahr = c * FUNK[f](al)
        v = gerundet(wahr, 1)
        if v is None: return None
        ziel = 'a' if f == 'sin' else 'b'
        return zahl(f'Im Dreieck ABC ist γ = 90°, α = {al}° und c = {c} cm. Berechne {ziel} (auf eine Nachkommastelle).',
                    f'{ziel} ist {"Gegen" if f == "sin" else "An"}kathete von α: {ziel} = c · {f} α = {c} · {f} {al}° ≈ {dz(v)} cm.',
                    f'Welche Funktion verbindet {ziel} und c?', v, f'round({c} * {K(FUNK[f](al))}, 1)', einheit='cm')
    if s == 2 and R.random() < 0.5:
        c = R.randint(5, 25)
        if R.random() < 0.5:
            wahr = c * cos(al)
            t, w, ce = f'α = {al}° und c = {c} cm. Berechne b', f'b ist Ankathete von α: b = c · cos α = {c} · cos {al}°', f'round({c} * {K(cos(al))}, 1)'
        else:
            be = 90 - al
            wahr = c * cos(be)
            t, w, ce = f'β = {be}° und c = {c} cm. Berechne a', f'a ist Ankathete von β: a = c · cos β = {c} · cos {be}°', f'round({c} * {K(cos(be))}, 1)'
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Im Dreieck ABC ist γ = 90°, {t} (auf eine Nachkommastelle).', f'{w} ≈ {dz(v)} cm.',
                    'Welche Funktion verbindet die bekannte und die gesuchte Seite?', v, ce, einheit='cm')
    if s == 2:
        b = R.randint(3, 20)
        wahr = b * tan(al)
        v = gerundet(wahr, 1)
        if v is None or wahr > 80: return None
        return zahl(f'Im Dreieck ABC ist γ = 90°, α = {al}° und b = {b} cm. Berechne a (auf eine Nachkommastelle).',
                    f'tan α = a/b ⇒ a = b · tan α = {b} · tan {al}° ≈ {dz(v)} cm.', 'a ist Gegenkathete, b Ankathete von α.', v,
                    f'round({b} * {K(tan(al))}, 1)', einheit='cm')
    a = R.randint(3, 15)
    f = R.choice(['sin', 'tan', 'cos'])
    if f == 'sin':
        wahr = a / sin(al)
        t, w = f'α = {al}° und a = {a} cm. Berechne c', f'sin α = a/c ⇒ c = a : sin α = {a} : sin {al}°'
        c_ = f'round({a} / {K(sin(al))}, 1)'
    elif f == 'tan':
        wahr = a / tan(al)
        t, w = f'α = {al}° und a = {a} cm. Berechne b', f'tan α = a/b ⇒ b = a : tan α = {a} : tan {al}°'
        c_ = f'round({a} / {K(tan(al))}, 1)'
    else:
        wahr = a / cos(al)
        t, w = f'β = {90 - al}° und a = {a} cm. Berechne c', f'a ist Ankathete von β: cos β = a/c ⇒ c = a : cos β = {a} : cos {90 - al}°'
        wahr = a / cos(90 - al)
        c_ = f'round({a} / {K(cos(90 - al))}, 1)'
    v = gerundet(wahr, 1)
    if v is None or wahr > 100: return None
    return zahl(f'Im Dreieck ABC ist γ = 90°, {t} (auf eine Nachkommastelle).', f'{w} ≈ {dz(v)} cm.',
                'Die gesuchte Seite steht im Nenner: Stelle die Gleichung durch Multiplizieren und Teilen um.', v, c_, einheit='cm')


def g_winkel(s):
    a, b = R.randint(2, 15), R.randint(2, 15)
    if a == b: return None
    if s == 1:
        f = 'tan'
        q = a / b
        wahr = atan(q)
        t = f'a = {a} cm und b = {b} cm. Berechne α'
        w = f'tan α = a/b = {a}/{b} ⇒ α = tan⁻¹({a}/{b})'
    elif s == 2:
        c = R.randint(max(a, b) + 1, max(a, b) + 10)
        if R.random() < 0.5:
            wahr = asin(a / c)
            t, w = f'a = {a} cm und c = {c} cm. Berechne α', f'sin α = a/c = {a}/{c} ⇒ α = sin⁻¹({a}/{c})'
        else:
            wahr = acos(b / c)
            t, w = f'b = {b} cm und c = {c} cm. Berechne α', f'cos α = b/c = {b}/{c} ⇒ α = cos⁻¹({b}/{c})'
    else:
        c = R.randint(max(a, b) + 1, max(a, b) + 10)
        wahr = 90 - asin(a / c)
        t, w = f'a = {a} cm und c = {c} cm. Berechne β', f'a ist Ankathete von β: cos β = a/c = {a}/{c} ⇒ β = cos⁻¹({a}/{c})'
    v = gerundet(wahr, 1)
    if v is None: return None
    return zahl(f'Im Dreieck ABC ist γ = 90°, {t} (in Grad, auf eine Nachkommastelle).', f'{w} ≈ {dz(v)}°.',
                'Bilde das passende Seitenverhältnis und benutze die Umkehrtaste (DEG-Modus).', v, f'round({K(wahr)}, 1)', einheit='°')


def g_beziehungen(s):
    trip = [(3, 4, 5), (7, 24, 25), (44, 117, 125), (336, 527, 625)]
    if s == 1:
        typ = R.random()
        if typ < 0.5:
            w, wert, grund = R.choice([('sin 30°', Fr(1, 2), 'Im halben gleichseitigen Dreieck ist die Gegenkathete von 30° halb so lang wie die Hypotenuse.'),
                                       ('cos 60°', Fr(1, 2), 'Im halben gleichseitigen Dreieck ist die Ankathete von 60° halb so lang wie die Hypotenuse.'),
                                       ('tan 45°', Fr(1), 'Im gleichschenklig-rechtwinkligen Dreieck sind beide Katheten gleich lang.'),
                                       ('cos 45° · sin 45° · 2', Fr(1), 'cos 45° = sin 45°, und 2 · sin² 45° = sin² 45° + cos² 45° = 1.'),
                                       ('sin² 30° + cos² 30°', Fr(1), 'Für jeden spitzen Winkel gilt sin² α + cos² α = 1.'),
                                       ('sin 30° + cos 60°', Fr(1), 'Beide sind 0,5.'), ('tan 45° − sin 30°', Fr(1, 2), '1 − 0,5 = 0,5.')])
            return zahl(f'Gib den exakten Wert von {w} an.', f'{w} = {dz(wert)}. {grund}',
                        'Denke an das halbe gleichseitige Dreieck (30°/60°) und das gleichschenklig-rechtwinklige (45°).', wert, f'{cf(wert)}')
        al = R.choice([x for x in range(5, 86) if x != 45])
        return auswahl(f'Welcher Ausdruck ist gleich sin {al}°?', f'cos {90 - al}°', [f'cos {al}°', f'sin {90 - al}°', f'tan {al}°'],
                       f'Im rechtwinkligen Dreieck ist die Gegenkathete von α die Ankathete von 90° − α: sin {al}° = cos {90 - al}°.',
                       'Was ist der andere spitze Winkel im rechtwinkligen Dreieck?')
    p, q, r = R.choice(trip)
    if R.random() < 0.5: p, q = q, p
    sn, cs = Fr(p, r), Fr(q, r)
    if s == 2 and R.random() < 0.3:
        tn = sn / cs
        if endlich(tn):
            return zahl(f'Für einen spitzen Winkel gilt sin α = {dz(sn)} und cos α = {dz(cs)}. Berechne tan α.', f'tan α = sin α : cos α = {dz(sn)} : {dz(cs)} = {dz(tn)}.',
                        'Nutze tan α = sin α : cos α.', tn, f'{cf(sn)} / {cf(cs)}')
        v = gerundet(float(tn), 2)
        if v is None: return None
        return zahl(f'Für einen spitzen Winkel gilt sin α = {dz(sn)} und cos α = {dz(cs)}. Berechne tan α auf zwei Nachkommastellen.',
                    f'tan α = sin α : cos α = {dz(sn)} : {dz(cs)} ≈ {dz(v)}.', 'Nutze tan α = sin α : cos α.', v, f'round({cf(sn)} / {cf(cs)}, 2)')
    if not (endlich(sn) and endlich(cs)): return None
    if s == 2:
        typ = R.random()
        if typ < 0.3:
            return zahl(f'Für einen spitzen Winkel α gilt sin α = {dz(sn)}. Berechne cos α.', f'cos² α = 1 − {dz(sn)}² = {dz(1 - sn * sn)}, cos α = {dz(cs)} (positiv, da α spitz).',
                        'Nutze sin² α + cos² α = 1.', cs, f'(1 - {cf(sn)} ** 2) / {cf(cs)}')
        if typ < 0.55:
            return zahl(f'Für einen spitzen Winkel β gilt cos β = {dz(cs)}. Berechne sin β.', f'sin² β = 1 − {dz(cs)}² = {dz(1 - cs * cs)}, sin β = {dz(sn)} (positiv, da β spitz).',
                        'Nutze sin² β + cos² β = 1.', sn, f'(1 - {cf(cs)} ** 2) / {cf(sn)}')
        if typ < 0.75:
            return zahl(f'Für einen spitzen Winkel α gilt sin α = {dz(sn)}. Wie groß ist cos(90° − α)?', f'cos(90° − α) = sin α = {dz(sn)}.',
                        'Im rechtwinkligen Dreieck ist 90° − α der andere spitze Winkel.', sn, f'{cf(sn)}')
        al = R.choice([x for x in range(5, 86) if x != 45])
        return auswahl(f'Welcher Ausdruck ist gleich cos {al}°?', f'sin {90 - al}°', [f'sin {al}°', f'cos {90 - al}°', f'tan {90 - al}°'],
                       f'Die Ankathete von {al}° ist die Gegenkathete von {90 - al}°: cos {al}° = sin {90 - al}°.', 'Was ist der andere spitze Winkel?')
    if R.random() < 0.5:
        tn = sn / cs
        if endlich(tn):
            return zahl(f'Für einen spitzen Winkel α gilt cos α = {dz(cs)}. Berechne tan α.', f'sin α = √(1 − {dz(cs)}²) = {dz(sn)}; tan α = {dz(sn)} : {dz(cs)} = {dz(tn)}.',
                        'Erst sin α über sin² + cos² = 1, dann tan = sin : cos.', tn, f'{cf(sn)} / {cf(cs)}')
        v = gerundet(float(tn), 2)
        if v is None: return None
        return zahl(f'Für einen spitzen Winkel α gilt cos α = {dz(cs)}. Berechne tan α auf zwei Nachkommastellen.', f'sin α = √(1 − {dz(cs)}²) = {dz(sn)}; tan α = {dz(sn)} : {dz(cs)} ≈ {dz(v)}.',
                    'Erst sin α über sin² + cos² = 1, dann tan = sin : cos.', v, f'round({cf(sn)} / {cf(cs)}, 2)')
    return auswahl(f'Jemand behauptet: „Für einen spitzen Winkel gilt sin α = {dz(sn)} und cos α = {dz(1 - sn)}, weil sin α + cos α = 1.“ Was stimmt?',
                   f'Falsch: Es gilt sin² α + cos² α = 1, also cos α = {dz(cs)}.',
                   ['Richtig.', f'Falsch: cos α = {dz(sn)}, weil Sinus und Kosinus gleich sind.', f'Falsch: cos α = {dz(1 + sn)}.'],
                   f'{dz(sn)}² + {dz(cs)}² = {dz(sn * sn)} + {dz(cs * cs)} = 1. Mit {dz(1 - sn)} wäre {dz(sn)}² + {dz(1 - sn)}² = {dz(sn * sn + (1 - sn) ** 2)} ≠ 1.',
                   'Prüfe mit sin² α + cos² α = 1.')


def g_anwendung(s):
    typ = R.random()
    if s == 1:
        p = R.choice([2, 3, 4, 5, 6, 8, 10, 12, 15, 20])
        wahr = atan(p / 100)
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Eine Straße hat {p} % Steigung. Wie groß ist der Steigungswinkel (in Grad, auf eine Nachkommastelle)?',
                    f'tan α = {p}/100 = {dz(Fr(p, 100))} ⇒ α ≈ {dz(v)}°.', 'Steigung in % ist der Tangens des Steigungswinkels mal 100.', v,
                    f'round({K(wahr)}, 1)', einheit='°')
    if s == 2:
        if typ < 0.4:
            d, w = R.randint(20, 150), R.randint(15, 45)
            wahr = d * tan(w)
            v = gerundet(wahr, 1)
            if v is None or wahr > 120: return None
            return zahl(f'Aus {d} m Entfernung sieht man die Spitze eines Turms unter dem Höhenwinkel {w}° (Augenhöhe vernachlässigt). Wie hoch ist der Turm? Runde auf eine Nachkommastelle.',
                        f'tan {w}° = h/{d} ⇒ h = {d} · tan {w}° ≈ {dz(v)} m.', 'Entfernung ist die Ankathete, Turmhöhe die Gegenkathete.', v,
                        f'round({d} * {K(tan(w))}, 1)', einheit='m')
        if typ < 0.65:
            weg, w = R.randint(2, 20) * 100, R.randint(3, 15)
            wahr = weg * sin(w)
            v = gerundet(wahr, 0)
            if v is None: return None
            return zahl(f'Ein Wanderweg ist {dz(weg)} m lang und steigt gleichmäßig unter dem Winkel {w}° an. Wie viele Höhenmeter überwindet er? Runde auf ganze Meter.',
                        f'h = {dz(weg)} · sin {w}° ≈ {dz(v)} m.', 'Die Weglänge ist die Hypotenuse (schräg), die Höhe die Gegenkathete.', v,
                        f'round({weg} * {K(sin(w))}, 0)', einheit='m')
        if typ < 0.82:
            p_ = R.choice([4, 5, 6, 8, 10, 12])
            h = R.choice([30, 45, 60, 75, 90, 120])
            L = Fr(h * 100, p_) / 100
            if not endlich(L): return None
            return zahl(f'Eine Rampe soll {h} cm Höhe überwinden und höchstens {p_} % Steigung haben. Wie lang muss sie mindestens waagrecht sein (in m)?',
                        f'Steigung = Höhe : waagrechte Länge ⇒ L = {h} cm : {dz(Fr(p_, 100))} = {dz(L * 100)} cm = {dz(L)} m.',
                        f'{p_} % Steigung heißt: {p_} cm Höhe auf 100 cm waagrecht.', L, f'{h} / {p_}', einheit='m')
        l, w = R.randint(3, 8), R.randint(65, 75)
        wahr = l * sin(w)
        v = gerundet(wahr, 2)
        if v is None: return None
        return zahl(f'Eine {l} m lange Leiter lehnt unter einem Winkel von {w}° zum Boden an einer Wand. In welcher Höhe berührt sie die Wand? Runde auf cm (zwei Nachkommastellen in m).',
                    f'sin {w}° = h/{l} ⇒ h = {l} · sin {w}° ≈ {format(v, ".2f").replace(".", ",")} m.', 'Die Leiter ist die Hypotenuse, die Höhe die Gegenkathete zum Bodenwinkel.', v,
                    f'round({l} * {K(sin(w))}, 2)', einheit='m')
    if typ < 0.25:
        w1, w2 = R.choice([(30, 45), (25, 40), (20, 35), (35, 50), (30, 50), (40, 60)])
        d = R.choice([30, 40, 50, 60, 80, 100])
        wahr = d * tan(w1) * tan(w2) / (tan(w2) - tan(w1))
        v = gerundet(wahr, 0)
        if v is None: return None
        return zahl(f'Von einem Punkt sieht man die Spitze eines Turms unter {w1}°. Geht man {d} m näher heran, sieht man sie unter {w2}°. Wie hoch ist der Turm? Runde auf ganze Meter.',
                    f'x = Abstand vom näheren Punkt: h = x · tan {w2}° und h = (x + {d}) · tan {w1}°. Gleichsetzen: x = {d} · tan {w1}° : (tan {w2}° − tan {w1}°) ≈ {dz(round(wahr / tan(w2), 1))} m, h ≈ {dz(v)} m.',
                    'Zwei rechtwinklige Dreiecke mit derselben Höhe h: Stelle für jedes eine Gleichung auf.', v,
                    f'round({K(wahr)}, 0)', einheit='m')
    if typ < 0.35:
        h, w = R.choice([30, 40, 50, 60, 75, 80, 100, 120]), R.randint(4, 12)
        l = R.randint(5, 20) * 10
        wahr = atan(h / (l * 10))
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Eine Rampe überwindet {h} cm Höhe auf {l * 10} cm waagrechter Länge. Wie groß ist der Neigungswinkel (auf eine Nachkommastelle)?',
                    f'tan α = {h}/{l * 10} ⇒ α ≈ {dz(v)}°.', 'Höhe und waagrechte Länge sind Gegen- und Ankathete.', v, f'round({K(wahr)}, 1)', einheit='°')
    if typ < 0.7:
        weg, w = R.randint(2, 20) * 100, R.randint(3, 15)
        wahr = weg * sin(w)
        v = gerundet(wahr, 0)
        if v is None: return None
        return zahl(f'Ein Wanderweg ist {dz(weg)} m lang und steigt gleichmäßig unter dem Winkel {w}° an. Wie viele Höhenmeter überwindet er? Runde auf ganze Meter.',
                    f'h = {dz(weg)} · sin {w}° ≈ {dz(v)} m.', 'Die Weglänge ist die Hypotenuse (schräg), die Höhe die Gegenkathete.', v,
                    f'round({weg} * {K(sin(w))}, 0)', einheit='m')
    h, w1 = R.randint(20, 80), R.randint(20, 40)
    wahr = h / tan(w1)
    v = gerundet(wahr, 1)
    if v is None: return None
    return zahl(f'Von einem {h} m hohen Leuchtturm sieht man ein Boot unter dem Tiefenwinkel {w1}° (gemessen von der Waagrechten nach unten). Wie weit ist das Boot vom Fuß des Turms entfernt? Runde auf eine Nachkommastelle.',
                f'Der Tiefenwinkel ist gleich dem Höhenwinkel vom Boot aus (Wechselwinkel): tan {w1}° = {h}/e ⇒ e = {h} : tan {w1}° ≈ {dz(v)} m.',
                'Zeichne die Waagrechte am Turm; der Tiefenwinkel taucht unten am Boot als Wechselwinkel wieder auf.', v,
                f'round({h} / {K(tan(w1))}, 1)', einheit='m')


GEN = {'seiten': g_seiten, 'verhaeltnisse': g_verhaeltnisse, 'seite': g_seite, 'winkel': g_winkel,
       'beziehungen': g_beziehungen, 'anwendung': g_anwendung}

# ---------- Zehnte Runde (schwer-kl9): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Abschnitt mit eigenem festen Zufallsstart (anhaengen(..., 9911, ...)), läuft erst nach bauen():
# alle bisherigen Aufgaben bleiben unverändert. Vorbilder: Bayerischer Mathematik-Test 10 (ISB; 2023: Sinuswert aus
# einer Abbildung ablesen, begründen, dass in einem Dreieck kein Winkel 30° ist; 2024: Wert eines trigonometrischen
# Terms im Zylinder über ein rechtwinkliges Teildreieck; 2025: Flächeninhalt eines Parallelogramms als Term mit sin α),
# Abschlussprüfung Realschule Bayern Mathematik I 2023–2025 (Winkel im Quader und in Dreiecken mit tan, Strecken mit
# sin/cos, Neigungswinkel). Zahlen und Wortlaut eigen.
from _schwer_kl9 import anhaengen  # noqa: E402
from _kl9 import K as _K  # noqa: E402


def schwer():
    P, Kn, O = 'pruefung', 'knobel', ''
    r1 = lambda x: round(x, 1)
    c1 = lambda x: f'round({_K(x)}, 1)'
    sinbild = {'typ': 'koordinaten', 'x': [0, 90], 'y': [0, 1.1], 'grad': True, 'schritt_x': 10, 'schritt_y': 0.2,
               'graphen': [{'art': 'sin', 'a': 1, 'b': 1, 'c': 0, 'd': 0}], 'waagrecht': [0.8]}
    return [
        # seiten
        ('seiten', 3, P, auswahl('Ein Zylinder hat 3 cm Radius und 8 cm Höhe. M ist der Mittelpunkt der Grundfläche, R der Mittelpunkt der Deckfläche, Q ein Punkt auf dem Rand der Grundfläche. Im Dreieck QMR: Welche Strecke ist die Gegenkathete des Winkels bei R?',
                                 'QM (der Radius, 3 cm)', ['MR (die Höhe, 8 cm)', 'QR', 'Keine – das Dreieck ist nicht rechtwinklig.'],
                                 'Die Höhe MR steht senkrecht auf der Grundfläche, also ist bei M ein rechter Winkel. QR ist die Hypotenuse. Gegenüber dem Winkel bei R liegt QM.',
                                 'Suche zuerst den rechten Winkel: Die Höhe steht senkrecht auf jedem Radius der Grundfläche.')),
        ('seiten', 3, P, auswahl('Im Quader ABCDEFGH (Grundfläche ABCD, darüber EFGH, G über C) betrachtet man das Dreieck ACG. Wo liegt der rechte Winkel?', 'bei C',
                                 ['bei A', 'bei G', 'Das Dreieck hat keinen rechten Winkel.'],
                                 'Die Kante CG steht senkrecht auf der Grundfläche und damit auf der Diagonale AC. Der rechte Winkel liegt bei C, AG ist die Hypotenuse.',
                                 'Welche Kante steht senkrecht auf der Grundfläche?')),
        ('seiten', 3, Kn, auswahl('In einem rechtwinkligen Dreieck mit den spitzen Winkeln α und β: Was ist die Gegenkathete von α für den Winkel β?', 'die Ankathete von β',
                                  ['die Gegenkathete von β', 'die Hypotenuse', 'Das hängt vom Dreieck ab.'],
                                  'Die Seite gegenüber α liegt am Winkel β an (sie bildet mit der Hypotenuse den Winkel β). Darum gilt sin α = cos β.',
                                  'Zeichne ein rechtwinkliges Dreieck und markiere die Seite gegenüber α. Wo liegt sie von β aus?')),
        ('seiten', 3, O, auswahl('Im Dreieck XYZ liegt der rechte Winkel bei Y. Welches Verhältnis ist der Kosinus des Winkels bei Z?', 'YZ : XZ', ['XY : XZ', 'XY : YZ', 'XZ : YZ'],
                                 'Hypotenuse XZ (gegenüber Y). Am Winkel bei Z liegt YZ an: cos = Ankathete : Hypotenuse = YZ : XZ.', 'Erst die Hypotenuse, dann die Ankathete am Winkel bei Z.')),
        ('seiten', 2, O, auswahl('Im Dreieck ABC liegt der rechte Winkel bei C. Welche Seite ist die Hypotenuse?', 'AB', ['BC', 'AC'],
                                 'Die Hypotenuse liegt dem rechten Winkel gegenüber: Seite AB (= c).', 'Gegenüber dem rechten Winkel.')),
        ('seiten', 2, O, auswahl('Was gilt in jedem rechtwinkligen Dreieck für die Hypotenuse?', 'Sie ist die längste Seite.', ['Sie ist die kürzeste Seite.', 'Sie liegt immer am Winkel α.', 'Sie ist so lang wie beide Katheten zusammen.'],
                                 'Aus c² = a² + b² folgt c > a und c > b. Aber c < a + b (Dreiecksungleichung).', 'Denke an den Satz des Pythagoras.')),
        # verhaeltnisse
        ('verhaeltnisse', 3, P, auswahl('Ein rechtwinkliges Dreieck hat die Seiten 7 cm, 24 cm und 25 cm. Kann einer seiner spitzen Winkel 30° groß sein? (sin 30° = 0,5)',
                                        'Nein: Die Sinuswerte sind 7/25 = 0,28 und 24/25 = 0,96, keiner ist 0,5.',
                                        ['Ja, der kleinere spitze Winkel.', 'Ja, weil 7 + 24 > 25.', 'Das kann man ohne Winkelmesser nicht entscheiden.'],
                                        'Für die spitzen Winkel gilt sin = Gegenkathete : Hypotenuse = 7/25 bzw. 24/25. Ein 30°-Winkel bräuchte eine Gegenkathete von 12,5 cm.',
                                        'Berechne für beide spitzen Winkel den Sinus und vergleiche mit 0,5.')),
        ('verhaeltnisse', 3, P, luecken('Ein Zylinder hat 3 cm Radius und 8 cm Höhe. Die Höhe MR, ein Radius MQ der Grundfläche und die Strecke QR bilden ein Dreieck; φ ist der Winkel bei R. Gib tan φ als Bruch an.',
                                        '□/□', 'Zähler und Nenner eintragen', [3, 8], 'Rechter Winkel bei M. Von R aus: Gegenkathete MQ = 3 cm, Ankathete MR = 8 cm. tan φ = 3/8.',
                                        'tan = Gegenkathete : Ankathete. Welche Seite liegt φ gegenüber?', ['3', '8'])),
        ('verhaeltnisse', 3, Kn, zahl('Für einen spitzen Winkel α gilt tan α = 0,75. Berechne sin α.', 'tan α = 3/4: Zeichne ein Dreieck mit Gegenkathete 3 und Ankathete 4. Hypotenuse √(9 + 16) = 5. sin α = 3/5 = 0,6.',
                                      'Baue dir ein passendes rechtwinkliges Dreieck mit einfachen Zahlen.', 0.6, '3 / 5')),
        ('verhaeltnisse', 3, O, zahl('Im Dreieck ABC ist γ = 90°, c = 25 cm und a = 7 cm. Berechne cos α als Dezimalzahl.', 'b = √(625 − 49) = 24 cm. cos α = b : c = 24 : 25 = 0,96.',
                                     'Für cos α brauchst du die Ankathete b – erst mit Pythagoras.', 0.96, '24 / 25')),
        ('verhaeltnisse', 2, O, zahl('Im Dreieck ABC ist γ = 90°, a = 6 cm und c = 10 cm. Berechne sin α.', 'sin α = a : c = 6 : 10 = 0,6.', 'Gegenkathete durch Hypotenuse.', 0.6, '6 / 10')),
        ('verhaeltnisse', 2, O, luecken('Im Dreieck ABC ist γ = 90°, a = 5 cm, b = 12 cm, c = 13 cm. Gib tan β als Bruch an.', '□/□', 'Zähler und Nenner eintragen', [12, 5],
                                        'Für β: Gegenkathete b = 12, Ankathete a = 5. tan β = 12/5.', 'Vom Winkel β aus schauen.', ['12', '5'])),
        # seite
        ('seite', 3, P, auswahl('Ein Parallelogramm hat die Seiten 6 cm und 3 cm; sie schließen den Winkel α ein. Welcher Term gibt den Flächeninhalt (in cm²) an?', '18 · sin α',
                                ['18 · cos α', '9 · sin α', '18 · tan α'],
                                'Höhe auf die 6-cm-Seite: h = 3 · sin α. Fläche = Grundseite · Höhe = 6 · 3 · sin α = 18 · sin α.', 'Zeichne die Höhe ein. Sie ist Gegenkathete von α.')),
        ('seite', 3, P, zahl('Im Dreieck ABC ist γ = 90°, c = 8 cm und β = 60°. Berechne a ohne Taschenrechner (cos 60° = 0,5).', 'a ist Ankathete von β: a = c · cos β = 8 · 0,5 = 4 cm.',
                             'Welche Seite liegt an β an?', 4, '8 * 0.5', einheit='cm')),
        ('seite', 3, Kn, zahl('In einem rechtwinkligen Dreieck ist eine Kathete genau halb so lang wie die Hypotenuse. Wie groß ist der Winkel, der dieser Kathete gegenüberliegt?',
                              'sin α = Gegenkathete : Hypotenuse = 1/2 = 0,5. Der Winkel mit sin α = 0,5 ist 30°.', 'Bilde das Verhältnis – die Längen selbst brauchst du nicht.', 30, '180 / 6',
                              einheit='°')),
        ('seite', 3, O, zahl('Im Dreieck ABC ist γ = 90°, α = 35° und b = 9 cm. Berechne c (auf eine Nachkommastelle).', 'b ist Ankathete von α: cos α = b/c ⇒ c = 9 : cos 35° ≈ 11,0 cm.',
                             'Ankathete und Hypotenuse: Kosinus. Dann nach c umstellen.', r1(9 / cos(35)), c1(9 / cos(35)), einheit='cm')),
        ('seite', 2, O, zahl('Im Dreieck ABC ist γ = 90°, α = 40° und c = 12 cm. Berechne a (auf eine Nachkommastelle).', 'a = c · sin α = 12 · sin 40° ≈ 7,7 cm.', 'Gegenkathete und Hypotenuse: Sinus.',
                             r1(12 * sin(40)), c1(12 * sin(40)), einheit='cm')),
        ('seite', 2, O, zahl('Im Dreieck ABC ist γ = 90°, α = 25° und b = 20 cm. Berechne a (auf eine Nachkommastelle).', 'a = b · tan α = 20 · tan 25° ≈ 9,3 cm.', 'Gegenkathete und Ankathete: Tangens.',
                             r1(20 * tan(25)), c1(20 * tan(25)), einheit='cm')),
        # winkel
        ('winkel', 3, P, zahl('Ein Quader hat die Grundfläche 6 cm × 8 cm und die Höhe 5 cm. Unter welchem Winkel ist die Raumdiagonale gegen die Grundfläche geneigt? Runde auf eine Nachkommastelle.',
                              'Bodendiagonale √(36 + 64) = 10 cm. Mit der Höhe: tan φ = 5 : 10 = 0,5, φ ≈ 26,6°.', 'Das Dreieck aus Bodendiagonale, Kante und Raumdiagonale hat bei der Kante einen rechten Winkel.',
                              r1(atan(0.5)), c1(atan(0.5)), einheit='°')),
        ('winkel', 3, P, bild(auswahl('Die Abbildung zeigt den Graphen von y = sin x für 0° ≤ x ≤ 90° und die Linie y = 0,8. Für welchen Winkel ist sin x ungefähr 0,8?', 'etwa 53°',
                                      ['etwa 80°', 'etwa 37°', 'etwa 0,8°'],
                                      'Die Linie y = 0,8 schneidet den Graphen bei x ≈ 53°. Kontrolle: sin 53° ≈ 0,799.', 'Lies am Schnittpunkt den x-Wert ab.'), sinbild)),
        ('winkel', 3, Kn, zahl('In einem rechtwinkligen Dreieck ist eine Kathete doppelt so lang wie die andere. Wie groß ist der kleinere spitze Winkel? Runde auf eine Nachkommastelle.',
                               'Katheten k und 2k: tan α = k : 2k = 0,5, α ≈ 26,6°. Die Länge k spielt keine Rolle.', 'Gegenüber dem kleineren Winkel liegt die kürzere Kathete.',
                               r1(atan(0.5)), c1(atan(0.5)), einheit='°')),
        ('winkel', 3, O, zahl('Eine 12 m lange Rampe führt 1 m in die Höhe. Unter welchem Winkel steigt sie an? Runde auf eine Nachkommastelle.', 'Die Rampe ist die Hypotenuse: sin α = 1 : 12, α ≈ 4,8°.',
                              'Ist 12 m die waagrechte Strecke oder die Rampe selbst?', r1(asin(1 / 12)), c1(asin(1 / 12)), einheit='°')),
        ('winkel', 2, O, zahl('Im Dreieck ABC ist γ = 90° und a = b = 5 cm. Wie groß ist α?', 'tan α = 5 : 5 = 1, also α = 45° (gleichschenklig-rechtwinklig).', 'tan α = a : b.', 45, '90 / 2', einheit='°')),
        ('winkel', 2, O, zahl('Im Dreieck ABC ist γ = 90°, b = 4 cm und c = 8 cm. Wie groß ist α?', 'cos α = 4 : 8 = 0,5, also α = 60°.', 'Ankathete b und Hypotenuse c.', 60, '180 / 3', einheit='°')),
        # beziehungen
        ('beziehungen', 3, P, auswahl('Für einen spitzen Winkel α gilt sin α = 0,6. Welchen Wert hat cos(90° − α)?', '0,6', ['0,8', '0,4', '0,36'],
                                      'Im rechtwinkligen Dreieck ist 90° − α der andere spitze Winkel. Die Gegenkathete von α ist seine Ankathete: cos(90° − α) = sin α = 0,6.',
                                      'Zeichne beide spitzen Winkel in ein Dreieck.')),
        ('beziehungen', 3, P, zahl('Für einen spitzen Winkel α gilt sin α = 0,6. Berechne tan α ohne Taschenrechner.', 'cos α = √(1 − 0,36) = √0,64 = 0,8. tan α = 0,6 : 0,8 = 0,75.',
                                   'Erst cos α mit sin² α + cos² α = 1, dann tan α = sin α : cos α.', 0.75, '0.6 / 0.8')),
        ('beziehungen', 3, Kn, luecken('Ein gleichseitiges Dreieck hat die Seitenlänge 2. Die Höhe teilt es in zwei rechtwinklige Dreiecke mit den Winkeln 30°, 60° und 90°. Gib cos 30° exakt an.', '√□/□',
                                       'Zahl unter der Wurzel, dann Nenner', [3, 2],
                                       'Halbe Seite 1, Hypotenuse 2, Höhe √(4 − 1) = √3. Am 30°-Winkel (oben) liegt die Höhe an: cos 30° = √3/2.',
                                       'Berechne die Höhe mit Pythagoras. Welche Seite liegt am 30°-Winkel an?', ['4 - 1', '2'])),
        ('beziehungen', 3, O, zahl('Für einen spitzen Winkel gilt tan α = 1. Berechne sin² α.', 'tan α = 1 heißt sin α = cos α. Mit sin² α + cos² α = 1: 2 sin² α = 1, sin² α = 0,5.',
                                   'Was folgt aus tan α = 1 für sin α und cos α?', 0.5, '1 / 2')),
        ('beziehungen', 2, O, zahl('Berechne sin² 37° + cos² 37°.', 'Für jeden Winkel gilt sin² α + cos² α = 1.', 'Du brauchst keinen Taschenrechner.', 1, '0.5 + 0.5')),
        ('beziehungen', 2, O, zahl('Für einen spitzen Winkel gilt cos α = 0,8. Berechne sin α.', 'sin² α = 1 − 0,64 = 0,36, sin α = 0,6.', 'sin² α + cos² α = 1.', 0.6, '(1 - 0.64) / 0.6')),
        # anwendung
        ('anwendung', 3, P, zahl('Ein 6 m langes Brett wird als Rampe an eine 1,5 m hohe Ladekante gelegt. Unter welchem Winkel steigt die Rampe an? Runde auf eine Nachkommastelle.',
                                 'Brett = Hypotenuse, Höhe = Gegenkathete: sin α = 1,5 : 6 = 0,25, α ≈ 14,5°.', 'Skizze: Wo ist der rechte Winkel, welche Seite ist das Brett?',
                                 r1(asin(0.25)), c1(asin(0.25)), einheit='°')),
        ('anwendung', 3, P, zahl('Ein Flugzeug steigt nach dem Start unter 12° geradlinig auf und legt dabei 5 km Flugstrecke zurück. In welcher Höhe ist es dann? Runde auf ganze Meter.',
                                 'Flugstrecke = Hypotenuse: h = 5 000 m · sin 12° ≈ 1 040 m.', 'Rechne in Metern. Gegenkathete gesucht, Hypotenuse bekannt.', round(5000 * sin(12)),
                                 f'round({_K(5000 * sin(12))}, 0)', einheit='m')),
        ('anwendung', 3, Kn, zahl('Ein gleichschenkliges Dreieck hat zwei 10 cm lange Schenkel, die den Winkel 40° einschließen. Wie lang ist die Basis? Runde auf eine Nachkommastelle.',
                                  'Die Höhe auf die Basis halbiert den 40°-Winkel und die Basis: halbe Basis = 10 · sin 20° ≈ 3,42 cm, Basis ≈ 6,8 cm.',
                                  'Es gibt keinen rechten Winkel – erzeuge ihn mit der Höhe auf die Basis.', r1(20 * sin(20)), c1(20 * sin(20)), einheit='cm')),
        ('anwendung', 3, O, zahl('Ein Drachen hängt an einer 50 m langen, straff gespannten Schnur, die mit dem Boden 55° einschließt. Die Hand ist 1,2 m über dem Boden. Wie hoch fliegt der Drachen? Runde auf eine Nachkommastelle.',
                                 'Höhe über der Hand: 50 · sin 55° ≈ 40,96 m. Dazu 1,2 m: ≈ 42,2 m.', 'Vergiss die Höhe der Hand nicht.', r1(50 * sin(55) + 1.2), c1(50 * sin(55) + 1.2), einheit='m')),
        ('anwendung', 2, O, zahl('Eine Straße hat 15 % Steigung. Welchem Steigungswinkel entspricht das? Runde auf eine Nachkommastelle.', 'tan α = 0,15, α ≈ 8,5°.', '15 % heißt tan α = 0,15.',
                                 r1(atan(0.15)), c1(atan(0.15)), einheit='°')),
        ('anwendung', 2, O, zahl('Ein Baum wirft bei 40° Sonnenhöhe einen 18 m langen Schatten. Wie hoch ist der Baum? Runde auf eine Nachkommastelle.', 'h = 18 · tan 40° ≈ 15,1 m.',
                                 'Schatten = Ankathete, Baum = Gegenkathete.', r1(18 * tan(40)), c1(18 * tan(40)), einheit='m')),
    ]


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('trigo.rechtwinklig', 13_9_11)
# a) Grundaufgabe mit anderen Buchstaben bzw. Routine → Stufe 2
for _d, _r, _w in [('DFM', 'F', 'M'), ('ELR', 'R', 'E'), ('DMR', 'R', 'D'), ('DKQ', 'Q', 'K'), ('KMQ', 'K', 'Q'), ('DEK', 'K', 'D')]:
    BF.stufe('seiten', f'Im Dreieck {_d} ist der Winkel bei {_r} ein rechter. Welche Strecke ist die Ankathete des Winkels bei {_w}?', 2)
for _a, _c in [('3', '21'), ('13', '17'), ('6', '22'), ('5', '13'), ('2', '22'), ('14', '20')]:
    BF.stufe('winkel', f'Im Dreieck ABC ist γ = 90°, a = {_a} cm und c = {_c} cm. Berechne β (in Grad, auf eine Nachkommastelle).', 2)
for _t in ['α = 53° und a = 14 cm. Berechne c', 'α = 38° und a = 12 cm. Berechne b', 'β = 55° und a = 7 cm. Berechne c',
           'α = 20° und a = 15 cm. Berechne b', 'β = 51° und a = 8 cm. Berechne c', 'β = 57° und a = 6 cm. Berechne c']:
    BF.stufe('seite', f'Im Dreieck ABC ist γ = 90°, {_t} (auf eine Nachkommastelle).', 2)

# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    d = bauen('trigo.rechtwinklig',
          'Sinus, Kosinus und Tangens als Seitenverhältnisse im rechtwinkligen Dreieck nutzen, um Seiten und Winkel zu berechnen.',
          ['sin α = Gegenkathete : Hypotenuse; cos α = Ankathete : Hypotenuse; tan α = Gegenkathete : Ankathete.',
           'Seite gesucht: Gleichung nach der Seite umstellen. Winkel gesucht: Umkehrtaste (DEG).', 'sin² α + cos² α = 1; tan α = sin α : cos α; sin α = cos(90° − α).',
           'Steigung in % = tan α · 100.'],
          [('Grundbegriffe', ['seiten', 'verhaeltnisse']), ('Berechnen', ['seite', 'winkel', 'beziehungen']), ('Anwenden', ['anwendung'])],
          ETAPPEN, GEN,
          meiden={'verhaeltnisse': ['a = 8 cm, b = 15 cm, c = 17 cm'], 'seite': ['α = 35° und c = 10 cm'], 'winkel': ['a = 4 cm und b = 7 cm. Berechne α'],
                  'beziehungen': ['sin α = 0,28'], 'anwendung': ['8 % Steigung']},
          offen=['Skizzen: Lernkarten haben jetzt Bilder; Aufgaben mit Figur gibt es bei „seiten“ (Stufe 2). Die übrigen Aufgaben nennen das Dreieck weiter in Worten („Dreieck ABC mit γ = 90°“).',
                 'Rechenausdruck c: sin/cos/tan-Werte stehen als 12-stellige Konstanten, weil das Prüfskript keine Winkelfunktionen kennt. Werte nahe an Rundungsgrenzen werden vom Generator verworfen.'])
    anhaengen(d, 9911, schwer)
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden


# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl9) ----
from _durchsicht_kl9 import Befunde as _DSB, durchsicht  # noqa: E402

DS = _DSB('trigo.rechtwinklig', 19_9_12)
# verhaeltnisse: Verhältnis aus drei gegebenen Seiten ist Stufe 2; anders liegender rechter Winkel einmal auf Stufe 2
for _t in ('Im Dreieck ABC ist γ = 90°, a = 12 cm, b = 16 cm, c = 20 cm. Berechne tan α als Dezimalzahl.',
           'Im Dreieck ABC ist γ = 90°, a = 21 cm, b = 28 cm, c = 35 cm. Berechne sin α als Dezimalzahl.',
           'Im Dreieck ABC ist α = 90°. Welcher Term ist sin β?'):
    DS.stufe('verhaeltnisse', _t, 2)
# seite: Die Karte rechnet a = c · sin α vor; Kosinus statt Sinus ist die Abwandlung (Stufe 2), c = b : cos α ebenso
for _t in ('Im Dreieck ABC ist γ = 90°, α = 15° und c = 17 cm. Berechne b (auf eine Nachkommastelle).',
           'Im Dreieck ABC ist γ = 90°, α = 25° und c = 16 cm. Berechne b (auf eine Nachkommastelle).'):
    DS.stufe('seite', _t, 2)
DS.stufe('seite', 'Im Dreieck ABC ist γ = 90°, α = 40° und c = 12 cm. Berechne a (auf eine Nachkommastelle).', 1)
DS.stufe('seite', 'Im Dreieck ABC ist γ = 90°, α = 35° und b = 9 cm. Berechne c (auf eine Nachkommastelle).', 2)
DS.neu('seite', 3, DS.Z('Im Dreieck ABC ist γ = 90°, α = 30° und c = 12 cm. Berechne den Flächeninhalt (auf eine Nachkommastelle).', 31.2, '6 * 10.392304845413 / 2',
                       'a = 12 · sin 30° = 6 cm, b = 12 · cos 30° ≈ 10,39 cm. A = a · b : 2 ≈ 31,2 cm².',
                       'Berechne erst beide Katheten.', einheit='cm²', toleranz=0.1))
DS.neu('seite', 3, DS.Z('Eine Leiter soll 4 m hoch an eine Wand reichen. Mit dem Boden darf sie höchstens 75° einschließen. Wie lang muss sie mindestens sein? Runde auf eine Nachkommastelle.', 4.2, '4.141104721640 + 0.05',
                       'Leiter = Hypotenuse: L = 4 : sin 75° ≈ 4,14 m. Bei kleinerem Winkel wird sie länger, also mindestens etwa 4,2 m (aufgerundet).',
                       'Leiter = Hypotenuse, Höhe = Gegenkathete. Beim Runden: Sie darf nicht zu kurz sein.', einheit='m', toleranz=0.1))
# winkel: zwei neue Stufe-3-Aufgaben (Winkel in Figuren)
DS.neu('winkel', 3, DS.Z('Ein Rechteck ist 12 cm lang und 5 cm breit. Unter welchem spitzen Winkel schneiden sich seine Diagonalen? Runde auf eine Nachkommastelle.', 45.2, '2 * 22.619864948040',
                        'Die Diagonale bildet mit der langen Seite den Winkel tan⁻¹(5 : 12) ≈ 22,6°. Die Diagonalen schneiden sich unter 2 · 22,6° ≈ 45,2°.',
                        'Zeichne eine Diagonale und das rechtwinklige Dreieck mit den Rechteckseiten.', einheit='°', toleranz=0.1))
DS.neu('winkel', 3, DS.Z('Ein gleichschenkliges Dreieck hat die Basis 10 cm und zwei 13 cm lange Schenkel. Wie groß ist ein Basiswinkel? Runde auf eine Nachkommastelle.', 67.4, '67.380135051960',
                        'Die Höhe halbiert die Basis: cos α = 5 : 13, α = cos⁻¹(5/13) ≈ 67,4°.',
                        'Die Höhe teilt das Dreieck in zwei rechtwinklige Dreiecke.', einheit='°', toleranz=0.1))
# beziehungen: cos aus sin (wie die Karte) ist Stufe 1; sin α = cos(90° − α) ist Stufe 2 und kommt jetzt auf der Karte vor
for _t in ('Für einen spitzen Winkel α gilt sin α = 0,8432. Berechne cos α.', 'Für einen spitzen Winkel α gilt sin α = 0,936. Berechne cos α.',
           'Für einen spitzen Winkel β gilt cos β = 0,5376. Berechne sin β.', 'Für einen spitzen Winkel gilt cos α = 0,8. Berechne sin α.'):
    DS.stufe('beziehungen', _t, 1)
for _g in (26, 10, 81, 61, 13):
    DS.stufe('beziehungen', f'Welcher Ausdruck ist gleich sin {_g}°?', 2)
DS.stufe('beziehungen', 'Gib den exakten Wert von cos 45° · sin 45° · 2 an.', 3)

DS_KARTEN = {
    'beziehungen': {
        'schritte': [{'text': 'Bekannt ist sin α = 0,28. Im Bild: 7 : 25 = 0,28.'},
                     {'text': 'Pythagoras geteilt durch c²: sin² α + cos² α = 1.'},
                     {'text': 'cos² α = 1 − 0,0784 = 0,9216, also ⟦cos α = 0,96⟧.'},
                     {'text': 'tan α = 0,28 : 0,96 = 7/24.'},
                     {'text': 'Am anderen Winkel 90° − α liegt 7 an: ⟦cos(90° − α) = sin α⟧.'}],
        'regel': 'Es gilt ⟦sin² α + cos² α = 1⟧. Dazu: tan α = sin α : cos α, sin α = cos(90° − α).',
    },
}

if __name__ == '__main__':
    durchsicht('trigo.rechtwinklig', DS, DS_KARTEN)


# ---- STUFEN (Zwanzigste Runde, Zweig stufen-kl9) ----
from _stufen_kl9 import Stufen, stufen  # noqa: E402

ST = Stufen('trigo.rechtwinklig', 20_9_12)
Z, A, L = ST.Z, ST.A, ST.L

# seiten
ST.stufenleiter('seiten', 'Bei γ = 90° Hypotenuse, Gegen- und Ankathete benennen.',
                'Andere Lage des rechten Winkels und andere Buchstaben, Figuren lesen, Seiten an einer Rampe benennen.',
                'Dreiecke in Körpern finden, Rollentausch für α und β, Fehler bei der Hypotenuse, Bedingungen für „a ist Hypotenuse“, mehrteilige Aufgabe.')
ST.typ('seiten', 'Im Dreieck ABC ist γ = 90°', 'erkennen')
ST.typ('seiten', '/des markierten Winkels bei [AD]\\?$/', 'erkennen')
ST.typ('seiten', 'Was gilt in jedem', 'erkennen')
ST.typ('seiten', '/^Welche Strecke ist (die Gegenkathete|die Ankathete|die Hypotenuse)/', 'darstellung')
ST.typ('seiten', '/^Im Dreieck (ABC ist [αβ] = 90°|[A-Z]{3} ist der Winkel|ABC liegt der rechte Winkel bei C)/', 'mehrschritt')
ST.typ('seiten', 'Ein Zylinder', 'transfer')
ST.typ('seiten', '/^(Im Quader|Im Dreieck XYZ)/', 'verknuepfen')
ST.typ('seiten', 'In einem rechtwinkligen Dreieck mit den spitzen', 'begruenden')
ST.neu('seiten', 'direkt', Z('Im Dreieck ABC ist γ = 90°, a = 3 cm, b = 4 cm, c = 5 cm. Wie lang ist die Ankathete von α?', 4, '4',
       'Die Ankathete von α liegt am Winkel α und ist nicht die Hypotenuse: b = 4 cm.', 'Welche Kathete berührt den Winkel α?', einheit='cm'))
ST.neu('seiten', 'einkleidung', A('Eine Rampe führt auf eine Bühne. Vom Winkel unten am Boden aus: Welche Strecke ist die Gegenkathete?', 'die Höhe der Bühnenkante', ['die Rampe', 'der Boden unter der Rampe', 'keine'],
       'Die Rampe ist die Hypotenuse, der Boden liegt am Winkel an (Ankathete). Gegenüber liegt die Bühnenhöhe.', 'Was liegt dem Winkel gegenüber?'))
ST.neu('seiten', 'fehler', A('Im Dreieck ABC ist β = 90°. Jemand nennt a die Hypotenuse. Was stimmt?', 'Falsch: Die Hypotenuse liegt β gegenüber, also b.', ['Richtig.', 'Falsch: c ist die Hypotenuse.', 'Falsch: Es gibt keine Hypotenuse.'],
       'Die Hypotenuse liegt dem rechten Winkel gegenüber. Gegenüber von B liegt die Seite b.', 'Welche Seite liegt B gegenüber?'))
ST.neu('seiten', 'parameter', A('Für welchen rechten Winkel ist im Dreieck ABC die Seite a die Hypotenuse?', 'für α = 90°', ['für β = 90°', 'für γ = 90°', 'immer'],
       'a liegt A gegenüber. Ist der Winkel bei A der rechte, ist a die Hypotenuse.', 'Welcher Winkel liegt a gegenüber?'))
ST.neu('seiten', 'transfer', A('Eine Leiter lehnt an einer Wand, α ist der Winkel zwischen Leiter und Boden. Was ist die Ankathete von α?', 'der Abstand vom Fuß der Leiter zur Wand', ['die Leiter', 'die Höhe an der Wand', 'die Wand bis zur Decke'],
       'Die Leiter ist die Hypotenuse. Am Winkel α am Boden liegt der Bodenabschnitt an, die Wandhöhe liegt gegenüber.', 'Zeichne eine Skizze.'))
ST.neu('seiten', 'pruefung', L('Im Dreieck ABC liegt der rechte Winkel bei C, a = 6 cm, b = 8 cm, c = 10 cm. Gib die Längen an: a) Gegenkathete von α, b) Ankathete von β, c) Hypotenuse.', 'a) □ cm; b) □ cm; c) □ cm', [6, 6, 10],
       ['6', '6', '10'], 'a) Gegenüber α liegt a = 6. b) An β liegt a = 6 an. c) c = 10. Dieselbe Seite a spielt für α und β verschiedene Rollen.', 'Für β tauschen Gegen- und Ankathete.'))
ST.knobel('seiten', Z('In einem rechtwinkligen Dreieck ist die Gegenkathete von α genauso lang wie die Ankathete von α. Wie groß ist α?', 45, '90 // 2',
          'Gleich lange Katheten heißt: Das Dreieck ist gleichschenklig-rechtwinklig. Die beiden spitzen Winkel sind gleich groß: (180° − 90°) : 2 = 45°.',
          'Was für ein Dreieck ist das?', einheit='°'))
ST.knobel('seiten', Z('In einem rechtwinkligen Dreieck ist die Gegenkathete von α genau 3 cm lang. Wie lang ist die Ankathete des anderen spitzen Winkels β?', 3, '3',
          'Die Seite gegenüber α liegt am Winkel β an. Es ist dieselbe Strecke: 3 cm.', 'Zeichne die Seite und schau sie von β aus an.', einheit='cm'))

# verhaeltnisse
ST.stufenleiter('verhaeltnisse', 'sin, cos und tan als Seitenverhältnis bei γ = 90° aufschreiben.',
                'Verhältnisse als Zahl ausrechnen, anderer rechter Winkel, Rampen-Sinus.',
                'Erst eine Seite mit Pythagoras, Winkel ausschließen, Zylinder, sin aus tan, Fehler „Ankathete durch Hypotenuse“, Parameter, mehrteilige Aufgabe.')
ST.typ('verhaeltnisse', 'Im Dreieck ABC ist γ = 90°. Welcher Term', 'erkennen')
ST.typ('verhaeltnisse', '/^Im Dreieck ABC ist α = 90°\\. Welcher Term/', 'darstellung')
ST.typ('verhaeltnisse', '/Berechne zuerst c/', 'verknuepfen')
ST.typ('verhaeltnisse', '/^Im Dreieck ABC ist γ = 90°/', 'mehrschritt')
ST.typ('verhaeltnisse', 'Ein rechtwinkliges Dreieck hat die Seiten 7', 'begruenden')
ST.typ('verhaeltnisse', 'Ein Zylinder', 'transfer')
ST.typ('verhaeltnisse', 'Für einen spitzen Winkel', 'verknuepfen')
ST.neu('verhaeltnisse', 'direkt', L('Von α aus ist die Gegenkathete 9 cm und die Hypotenuse 41 cm. Gib sin α als Bruch an.', '□/□', [9, 41], ['9', '41'],
       'sin α = Gegenkathete : Hypotenuse = 9/41.', 'Gegenkathete durch Hypotenuse.'))
ST.neu('verhaeltnisse', 'einkleidung', Z('Eine Rampe ist 5 m lang und führt 3 m hoch. Wie groß ist der Sinus des Steigungswinkels?', 0.6, '3 / 5',
       'Die Rampe ist die Hypotenuse, die Höhe die Gegenkathete: sin α = 3 : 5 = 0,6.', 'Welche Strecke ist die Hypotenuse?'))
ST.neu('verhaeltnisse', 'fehler', A('Jemand schreibt: sin α = Ankathete : Hypotenuse. Was stimmt?', 'Falsch: Das ist cos α; sin α = Gegenkathete : Hypotenuse.', ['Richtig.', 'Falsch: sin α = Gegenkathete : Ankathete.', 'Falsch: sin α = Hypotenuse : Gegenkathete.'],
       'sin: Gegenkathete/Hypotenuse, cos: Ankathete/Hypotenuse, tan: Gegenkathete/Ankathete.', 'Denk an die Merkregel der Lernkarte.'))
ST.neu('verhaeltnisse', 'parameter', Z('Im Dreieck ABC ist γ = 90° und a = 7 cm. Für welche Länge b gilt tan α = 1?', 7, '7',
       'tan α = a : b = 1 heißt a = b = 7 cm.', 'Wann ist ein Bruch gleich 1?', einheit='cm'))
ST.neu('verhaeltnisse', 'pruefung', L('Im Dreieck ABC ist γ = 90°, a = 8 cm, b = 6 cm. Berechne a) c, b) sin α als gekürzten Bruch, c) tan β als gekürzten Bruch.', 'a) □ cm; b) □/□; c) □/□', [10, 4, 5, 3, 4],
       ['10', '4', '5', '3', '4'], 'a) c = √(64 + 36) = 10. b) sin α = 8/10 = 4/5. c) tan β = b : a = 6/8 = 3/4.', 'Erst c, dann die Verhältnisse.'))
ST.knobel('verhaeltnisse', A('Stimmt für jeden spitzen Winkel α im rechtwinkligen Dreieck: sin α + cos α > 1?', 'Ja, denn (a + b) : c > 1, weil a + b > c.', ['Nein, die Summe ist immer genau 1.', 'Nur für α = 45°.', 'Nein, sie ist immer kleiner als 1.'],
          'sin α + cos α = a/c + b/c = (a + b)/c. Im Dreieck sind zwei Seiten zusammen länger als die dritte: a + b > c. Gleich 1 ist nur sin² α + cos² α.',
          'Schreibe beide als Bruch mit dem Nenner c.'))
ST.knobel('verhaeltnisse', L('Für einen spitzen Winkel gilt tan α = 5/12. Wie groß ist sin α + cos α?', '□/□', [17, 13], ['17', '13'],
          'Dreieck mit Gegenkathete 5, Ankathete 12, Hypotenuse √(25 + 144) = 13. sin α = 5/13, cos α = 12/13, Summe 17/13.',
          'Zeichne ein passendes Dreieck.'))

# seite
ST.stufenleiter('seite', 'Mit a = c · sin α die Gegenkathete berechnen.',
                'Kosinus und Tangens wählen, durch sin oder cos teilen, Drachenschnur, Hypotenuse rückwärts.',
                'Fläche aus Winkel, exakte Werte, Mindestlänge einer Leiter, Fehler „sin statt cos“, Bedingung a > c/2, mehrteilige Aufgabe.')
ST.typ('seite', '/^Im Dreieck ABC ist γ = 90°, α = 30° und c = 14/', 'direkt')
ST.typ('seite', '/^Im Dreieck ABC ist γ = 90°, α = \\d+° und c = \\d+ cm\\. Berechne a/', 'direkt')
ST.typ('seite', 'Im Dreieck ABC ist γ = 90°, α = 30° und c = 12 cm. Berechne den', 'transfer')
ST.typ('seite', '/^Im Dreieck ABC ist γ = 90°, (α|β) = \\d+°/', 'mehrschritt')
ST.typ('seite', '/^(Ein Parallelogramm|Im Dreieck ABC ist γ = 90°, c = 8|In einem rechtwinkligen)/', 'verknuepfen')
ST.typ('seite', 'Eine Leiter soll', 'transfer')
ST.neu('seite', 'erkennen', A('Welche Funktion verbindet die Hypotenuse und die Gegenkathete von α?', 'sin α', ['cos α', 'tan α', 'keine'],
       'sin α = Gegenkathete : Hypotenuse.', 'Welches Verhältnis enthält genau diese zwei Seiten?'))
ST.neu('seite', 'direkt', Z('Eine 10 m lange Rampe steigt mit 30° an. Wie hoch führt sie? (sin 30° = 0,5)', 5, '10 * 0.5',
       'Höhe = 10 · sin 30° = 10 · 0,5 = 5 m.', 'Höhe = Rampenlänge · sin α.', einheit='m'))
ST.neu('seite', 'einkleidung', Z('Ein Drachen hängt an einer 40 m langen, straff gespannten Schnur, die mit dem Boden 50° einschließt. Wie hoch ist der Drachen über der Hand? Runde auf eine Nachkommastelle.', 30.6, '30.64177772475912',
       'h = 40 · sin 50° ≈ 30,6 m.', 'Die Schnur ist die Hypotenuse.', einheit='m', toleranz=0.1))
ST.neu('seite', 'umkehr', Z('Bei α = 30° ist die Gegenkathete 6 cm. Wie lang ist die Hypotenuse? (sin 30° = 0,5)', 12, '6 / 0.5',
       'sin 30° = 6 : c ⇒ c = 6 : 0,5 = 12 cm.', 'Stelle sin α = a : c nach c um.', einheit='cm'))
ST.neu('seite', 'fehler', A('Im Dreieck mit γ = 90°, c = 10 cm, α = 40° rechnet jemand b = 10 · sin 40°. Was stimmt?', 'Falsch: b ist Ankathete von α, also b = 10 · cos 40°.', ['Richtig.', 'Falsch: b = 10 · tan 40°.', 'Falsch: b = 10 : sin 40°.'],
       'b liegt am Winkel α an: cos α = b : c, also b = c · cos α ≈ 7,66 cm.', 'Liegt b gegenüber oder an α?'))
ST.neu('seite', 'parameter', A('Für welche spitzen Winkel α ist die Gegenkathete a = c · sin α länger als die Hälfte der Hypotenuse?', 'für α > 30°', ['für α < 30°', 'für α > 60°', 'für alle α'],
       'a > c/2 heißt sin α > 0,5, und sin 30° = 0,5. Der Sinus wächst mit dem Winkel, also α > 30°.', 'Wann ist sin α = 0,5?'))
ST.neu('seite', 'pruefung', L('Eine 5 m lange gerade Rampe steigt mit 6° an. a) Wie hoch führt sie (ganze cm)? b) Wie lang ist sie waagrecht gemessen (ganze cm)?', 'a) □ cm; b) □ cm', [52, 497], ['52', '497'],
       'a) 500 · sin 6° ≈ 52,3 cm ≈ 52 cm. b) 500 · cos 6° ≈ 497,3 cm ≈ 497 cm.', 'Rechne in cm: 5 m = 500 cm.'))
ST.knobel('seite', Z('Ein gleichschenkliges Dreieck hat zwei 10 cm lange Schenkel, die an der Spitze 120° einschließen. Wie groß ist sein Flächeninhalt? Runde auf eine Nachkommastelle.', 43.3, '43.301270189221924',
          'Die Höhe halbiert den Spitzenwinkel: zwei rechtwinklige Dreiecke mit 60° an der Spitze. Höhe h = 10 · cos 60° = 5 cm, halbe Basis 10 · sin 60° ≈ 8,66 cm. Fläche ≈ 8,66 · 5 = 43,3 cm².',
          'Teile das Dreieck mit der Höhe in zwei rechtwinklige Dreiecke.', einheit='cm²', toleranz=0.1))
ST.knobel('seite', Z('Ein regelmäßiges Achteck hat alle Ecken auf einem Kreis mit Radius 5 cm. Wie lang ist eine Seite? Runde auf zwei Nachkommastellen.', 3.83, '3.826834323650898',
          'Von der Mitte aus sieht man jede Seite unter 360° : 8 = 45°. Das gleichschenklige Dreieck (Schenkel 5 cm) wird von der Höhe halbiert: halbe Seite = 5 · sin 22,5° ≈ 1,913 cm. Seite ≈ 3,83 cm.',
          'Verbinde zwei Nachbarecken mit dem Mittelpunkt.', einheit='cm', toleranz=0.01))

# winkel
ST.stufenleiter('winkel', 'Mit tan⁻¹ einen Winkel aus zwei Katheten bestimmen.',
                'sin⁻¹ und cos⁻¹ wählen, besondere Werte, Rampe, Winkel zu sin α = 0,5.',
                'Raumdiagonale im Quader, Diagonalen im Rechteck, Basiswinkel, Graph lesen, Fehler „Katheten vertauscht“, Grenze bei 100 %, mehrteilige Aufgabe.')
ST.typ('winkel', 'Im Dreieck ABC ist γ = 90°, a = 10 cm und b = 14', 'direkt')
ST.typ('winkel', '/^Im Dreieck ABC ist γ = 90°, a = \\d+ cm und b = \\d+ cm\\. Berechne α/', 'direkt')
ST.typ('winkel', '/^Im Dreieck ABC ist γ = 90°/', 'mehrschritt')
ST.typ('winkel', 'Die Abbildung zeigt', 'darstellung')
ST.typ('winkel', '/^(Ein Quader|In einem rechtwinkligen)/', 'verknuepfen')
ST.typ('winkel', '/^(Eine 12 m|Ein Rechteck|Ein gleichschenkliges)/', 'transfer')
ST.neu('winkel', 'erkennen', A('Welche Taste liefert den Winkel α, wenn tan α bekannt ist?', 'tan⁻¹', ['tan', '1 : tan', 'sin⁻¹'],
       'Die Umkehrtaste tan⁻¹ macht aus dem Tangenswert den Winkel (Rechner auf DEG).', 'Vom Verhältnis zum Winkel.'))
ST.neu('winkel', 'direkt', Z('Für einen spitzen Winkel gilt tan α = 1. Wie groß ist α?', 45, '45',
       'tan⁻¹(1) = 45°: Gegenkathete und Ankathete sind gleich lang.', 'Wann sind beide Katheten gleich?', einheit='°'))
ST.neu('winkel', 'einkleidung', Z('Eine 3 m lange Rampe überwindet 0,5 m Höhe. Unter welchem Winkel steigt sie an? Runde auf eine Nachkommastelle.', 9.6, '9.594068226860461',
       'Rampe = Hypotenuse: sin α = 0,5 : 3, α ≈ 9,6°.', 'Welche Funktion verbindet Höhe und Rampe?', einheit='°', toleranz=0.1))
ST.neu('winkel', 'umkehr', Z('Für welchen spitzen Winkel α gilt sin α = 0,5?', 30, '30',
       'sin⁻¹(0,5) = 30°. Im halben gleichseitigen Dreieck ist die kurze Kathete halb so lang wie die Hypotenuse.', 'Denk an das halbe gleichseitige Dreieck.', einheit='°'))
ST.neu('winkel', 'fehler', A('Gegenkathete 4 m, Ankathete 7 m. Jemand rechnet α = tan⁻¹(7 : 4) ≈ 60,3°. Was stimmt?', 'Falsch: Vertauscht; α = tan⁻¹(4 : 7) ≈ 29,7°.', ['Richtig.', 'Falsch: α = sin⁻¹(4 : 7).', 'Falsch: α = 4 : 7 ≈ 0,57°.'],
       'tan α = Gegenkathete : Ankathete = 4 : 7. 60,3° ist der andere spitze Winkel.', 'Was steht im Zähler?'))
ST.neu('winkel', 'parameter', Z('Ab welcher Steigung in Prozent ist der Steigungswinkel größer als 45°?', 100, '100',
       'Bei 45° ist tan α = 1, also 100 % (Höhe gleich waagrechte Länge). Mehr als 100 % heißt mehr als 45°.', 'tan 45° = ?', einheit='%'))
ST.neu('winkel', 'pruefung', L('Ein rechtwinkliges Dreieck hat die Katheten a = 6 cm und b = 8 cm (γ = 90°). Berechne a) c, b) α und c) β auf ganze Grad.', 'a) □ cm; b) □°; c) □°', [10, 37, 53],
       ['10', '37', '53'], 'a) c = 10 cm. b) tan α = 6 : 8, α ≈ 36,9° ≈ 37°. c) β = 90° − α ≈ 53°.', 'Für β genügt die Winkelsumme.'))
ST.knobel('winkel', Z('In einem rechtwinkligen Dreieck ist α doppelt so groß wie β. Wie viel Mal so lang wie die kürzere Kathete ist die Hypotenuse?', 2, '2',
          'α + β = 90° und α = 2β, also β = 30°, α = 60°. Die kürzere Kathete liegt β gegenüber: sin 30° = Kathete : Hypotenuse = 0,5. Die Hypotenuse ist doppelt so lang.',
          'Bestimme zuerst die Winkel.'))
ST.knobel('winkel', Z('Bei welcher Sonnenhöhe ist der Schatten eines senkrechten Mastes doppelt so lang wie der Mast hoch ist? Runde auf eine Nachkommastelle.', 26.6, '26.56505117707799',
          'Mast h, Schatten 2h. tan α = h : 2h = 0,5, α = tan⁻¹(0,5) ≈ 26,6°. Die Höhe des Mastes spielt keine Rolle.',
          'Nenne die Masthöhe h.', einheit='°', toleranz=0.1))

# beziehungen
ST.stufenleiter('beziehungen', 'Mit sin² α + cos² α = 1 aus sin α den Kosinus berechnen.',
                'tan aus sin und cos, Rampe waagrecht, 90° − α, Werte ohne Taschenrechner.',
                'Exakte Werte im halben gleichseitigen Dreieck, unmögliche Wertepaare, Fehler „sin + cos = 1“, sin = cos, mehrteilige Aufgabe.')
ST.typ('beziehungen', '/^Für einen spitzen Winkel .*Berechne/', 'direkt', s=1)
ST.typ('beziehungen', '/^Welcher Ausdruck ist gleich/', 'erkennen')
ST.typ('beziehungen', '/^(Für einen spitzen Winkel gilt sin α = 0,96|Für einen spitzen Winkel α gilt sin α = 0,5376|Berechne sin²|Für einen spitzen Winkel α gilt cos α = 0,8432|Für einen spitzen Winkel α gilt sin α = 0,6|Für einen spitzen Winkel α gilt cos α = 0,96)/', 'mehrschritt')
ST.typ('beziehungen', '/^(Gib den exakten|Für einen spitzen Winkel gilt tan α = 1)/', 'verknuepfen')
ST.typ('beziehungen', 'Jemand behauptet', 'fehler')
ST.typ('beziehungen', 'Ein gleichseitiges Dreieck', 'transfer')
ST.neu('beziehungen', 'erkennen', A('Welche Gleichung gilt für jeden spitzen Winkel α?', 'sin² α + cos² α = 1', ['sin α + cos α = 1', 'sin α = cos α', 'tan α = sin α · cos α'],
       'Aus a² + b² = c² folgt geteilt durch c²: (a/c)² + (b/c)² = 1.', 'Pythagoras geteilt durch c².'))
ST.neu('beziehungen', 'einkleidung', Z('Eine 10 m lange Rampe hat einen Steigungswinkel mit sin α = 0,6. Wie lang ist sie waagrecht gemessen?', 8, '10 * 0.8',
       'cos α = √(1 − 0,36) = 0,8. Waagrecht: 10 · 0,8 = 8 m.', 'Berechne zuerst cos α.', einheit='m'))
ST.neu('beziehungen', 'umkehr', Z('Für einen spitzen Winkel gilt sin² α = 0,36. Wie groß ist cos α?', 0.8, '0.8',
       'cos² α = 1 − 0,36 = 0,64, cos α = 0,8 (positiv, α spitz).', 'Setze in sin² α + cos² α = 1 ein.'))
ST.neu('beziehungen', 'begruenden', A('Kann für einen spitzen Winkel sin α = 0,8 und cos α = 0,8 gelten?', 'Nein, 0,64 + 0,64 = 1,28 ≠ 1.', ['Ja, bei α = 45°.', 'Ja, immer.', 'Nur bei stumpfen Winkeln.'],
       'Es muss sin² α + cos² α = 1 gelten. Bei 45° wären beide ≈ 0,707.', 'Prüfe mit sin² α + cos² α.'))
ST.neu('beziehungen', 'parameter', Z('Für welchen spitzen Winkel α gilt sin α = cos α?', 45, '45',
       'sin α = cos α heißt tan α = 1, also α = 45°.', 'Teile durch cos α.', einheit='°'))
ST.neu('beziehungen', 'pruefung', L('Für einen spitzen Winkel gilt sin α = 0,6. Gib an: a) cos α als Dezimalzahl, b) tan α als gekürzten Bruch, c) sin(90° − α) als Dezimalzahl.', 'a) 0,□; b) □/□; c) 0,□', [8, 3, 4, 8], ['8', '3', '4', '8'],
       'a) cos α = √(1 − 0,36) = 0,8. b) tan α = 0,6 : 0,8 = 3/4. c) sin(90° − α) = cos α = 0,8.', 'Erst cos α.'))
ST.knobel('beziehungen', Z('Berechne sin² 10° + sin² 80°.', 1, '1',
          'sin 80° = cos 10°, denn 80° = 90° − 10°. Also sin² 10° + cos² 10° = 1. Ganz ohne Taschenrechner.', 'Was hat 80° mit 10° zu tun?'))
ST.knobel('beziehungen', Z('Berechne tan 20° · tan 70°.', 1, '1',
          'tan 70° = sin 70° : cos 70° = cos 20° : sin 20° = 1 : tan 20°. Das Produkt ist also 1.', 'Schreibe tan 70° mit Sinus und Kosinus von 20°.'))

# anwendung
ST.stufenleiter('anwendung', 'Aus einer Steigung in Prozent den Steigungswinkel berechnen.',
                'Höhenwinkel, Schatten, Wanderwege, Rampen mit vorgegebener Steigung, Weglänge rückwärts.',
                'Tiefenwinkel, zwei Höhenwinkel, Drachen über der Hand, Basis aus Winkel, Fehler „sin statt tan“, Prozent und Winkel nicht proportional, Seilbahn.')
ST.typ('anwendung', '/^Eine Straße hat \\d+ % Steigung/', 'direkt')
ST.typ('anwendung', 'Eine Rampe soll', 'umkehr')
ST.typ('anwendung', '/^(Ein Wanderweg|Aus \\d+ m Entfernung|Ein Baum|Ein \\d+ m langes Brett|Ein Flugzeug)/', 'einkleidung')
ST.typ('anwendung', '/^(Von einem \\d+ m hohen Leuchtturm|Ein gleichschenkliges)/', 'verknuepfen')
ST.typ('anwendung', '/^(Von einem Punkt|Ein Drachen)/', 'transfer')
ST.neu('anwendung', 'erkennen', A('Was bedeutet „12 % Steigung“?', 'Auf 100 m waagrecht steigt die Straße 12 m.', ['Der Steigungswinkel ist 12°.', 'Auf 100 m Straße steigt sie 100 m.', 'Die Straße ist 12 % länger.'],
       'Steigung in % = Höhe : waagrechte Länge · 100. 12 % heißt tan α = 0,12.', 'Prozent bezieht sich auf die waagrechte Strecke.'))
ST.neu('anwendung', 'direkt', Z('Eine Straße steigt auf 100 m waagrechter Strecke um 5 m. Wie groß ist der Steigungswinkel? Runde auf eine Nachkommastelle.', 2.9, '2.862405226111748',
       'tan α = 5 : 100 = 0,05, α ≈ 2,9°.', 'tan α = Höhe : waagrechte Strecke.', einheit='°', toleranz=0.1))
ST.neu('anwendung', 'mehrschritt', Z('Ein Wanderweg steigt gleichmäßig unter 5° an und überwindet 100 Höhenmeter. Wie lang ist er? Runde auf ganze Meter.', 1147, '1147.3713245669855',
       'Weg = Hypotenuse: sin 5° = 100 : s, s = 100 : sin 5° ≈ 1 147 m.', 'Stelle sin α = Höhe : Weg nach dem Weg um.', einheit='m', toleranz=1))
ST.neu('anwendung', 'fehler', A('Ein Turm wird aus 50 m Abstand unter 40° Höhenwinkel gesehen. Jemand rechnet h = 50 · sin 40°. Was stimmt?', 'Falsch: 50 m ist die Ankathete, also h = 50 · tan 40°.', ['Richtig.', 'Falsch: h = 50 · cos 40°.', 'Falsch: h = 50 : sin 40°.'],
       'Gegeben sind Ankathete (Abstand) und Winkel, gesucht die Gegenkathete (Höhe): tan α = h : 50.', 'Welche Seiten sind bekannt und gesucht?'))
ST.neu('anwendung', 'begruenden', A('Stimmt: Doppelte Steigung in Prozent heißt doppelter Steigungswinkel?', 'Nein: 50 % sind etwa 26,6°, 100 % aber 45°.', ['Ja, immer.', 'Ja, bis 100 %.', 'Nein, der Winkel halbiert sich.'],
       'Prozent ist tan α · 100, und der Tangens wächst nicht gleichmäßig mit dem Winkel.', 'Probiere 50 % und 100 %.'))
ST.neu('anwendung', 'pruefung', L('Eine Seilbahn fährt auf einem 1 200 m langen geraden Seil unter 25° nach oben. a) Wie groß ist der Höhenunterschied? b) Wie weit ist es waagrecht? (jeweils ganze Meter)', 'a) □ m; b) □ m', [507, 1088],
       ['507', '1088'], 'a) 1 200 · sin 25° ≈ 507 m. b) 1 200 · cos 25° ≈ 1 088 m.', 'Das Seil ist die Hypotenuse.'))
ST.knobel('anwendung', Z('Ein Turm wirft bei 30° Sonnenhöhe einen Schatten, der 20 m länger ist als bei 60° Sonnenhöhe. Wie hoch ist der Turm? Runde auf eine Nachkommastelle.', 17.3, '17.32050807568877',
          'Schatten s = h : tan α (tan α = h : s). Also h : tan 30° − h : tan 60° = 20. Es ist 1 : tan 30° ≈ 1 : 0,577 ≈ 1,732 und 1 : tan 60° ≈ 1 : 1,732 ≈ 0,577. Damit h · 1,732 − h · 0,577 = 20, also h · 1,155 = 20 und h ≈ 17,3 m.',
          'Schreibe beide Schattenlängen mit h.', einheit='m', toleranz=0.1))
ST.knobel('anwendung', Z('Eine Straße mit 10 % Steigung ist (entlang der Straße gemessen) 1 km lang. Um wie viele Meter steigt sie? Runde auf eine Nachkommastelle.', 99.5, '99.50371902099893',
          '10 % heißt tan α = 0,1, α ≈ 5,71°. Entlang der Straße ist der Weg die Hypotenuse: h = 1 000 · sin α ≈ 99,5 m – also nicht ganz 100 m.',
          'Prozent bezieht sich auf die waagrechte Strecke, nicht auf die Straße.', einheit='m', toleranz=0.1))

if __name__ == '__main__':
    stufen('trigo.rechtwinklig', ST)
