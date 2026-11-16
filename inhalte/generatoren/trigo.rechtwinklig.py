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

if __name__ == '__main__':
    bauen('trigo.rechtwinklig',
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
