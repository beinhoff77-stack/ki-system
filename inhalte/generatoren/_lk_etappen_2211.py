"""Neue Etappen für die Lücken aus LP-RS (Bau-Auftrag LK, LK-D, 22.11.2026).

Hängt an bestehende Themen je eine neue Lernkarte mit Übungen an (alle Lösungen hier berechnet, Texte selbst formuliert):
  46 abbildungen.kongruenz   · vektor_koordinaten (RS 7 I/II 2/K4)  · vektor_drehen (RS 8 I 2/K5)
  47 abbildungen.aehnlichkeit · streckung_vektor (RS 9 I 2/K5)
  44 geometrie.konstruktion   · vierecke_konstruieren (RS 8 I 1/K2, RS 8 II/III 1/K5)
  99 messen.flaechen_vielecke · drachen_raute (RS 6 3/k2)
  91 raum.schraegbilder       · wahre_groesse (RS 7 I 4/K3, RS 8 II/III 2/K2)
Die neuen Lernkarten sind Vertiefung (nicht Pflicht): Flug, Test und Stempel bestehender Themen ändern sich nicht.
Ob sie je Klasse Pflicht werden, regelt LK-S über zuordnung.etappen. Zweiter Lauf hängt nichts doppelt an.
"""
import json
from fractions import Fraction as Fr
from pathlib import Path

THEMEN = Path(__file__).resolve().parent.parent / 'themen'
KANN = Path(__file__).resolve().parent.parent / 'kann'


def z(n):
    if isinstance(n, Fr):
        n = int(n) if n.denominator == 1 else float(n)
    if isinstance(n, float) and n.is_integer():
        n = int(n)
    return str(n).replace('.', ',').replace('-', '−')


def k(n):
    return f'({z(n)})' if n < 0 else z(n)


def V(x, y):
    return f'({z(x)} | {z(y)})'


def auf(l, p, s, g, y, text, w, h=None, **x):
    a = {'l': l, 't': l, 'p': p, 's': s, 'y': y, 'f': {'text': text}, 'w': w}
    if p == 'uebung':
        a['g'] = g
        a['h'] = h
    a.update(x)
    return a


def wahl(richtig, falsch, pos):
    o = list(falsch)
    o.insert(pos, richtig)
    assert len(set(o)) == len(o), o
    return {'a': o, 'o': {'index': pos}}


# ------------------------------------------------------------------ 46 · vektor_koordinaten
def vektor_koordinaten():
    L = 'vektor_koordinaten'
    karte = {
        'lernziel': L, 'titel': 'Vektoren in Koordinaten',
        'einstieg': 'Ein Lieferroboter fährt auf einem Gitterplan von der Halle A zur Tür B. Sein Weg lässt sich als Pfeil angeben: so weit nach rechts und so weit nach oben. Diesen Pfeil nennt man ⟦Vektor⟧.',
        'woerter': [['Vektor', 'Pfeil mit Richtung und Länge, geschrieben als (nach rechts | nach oben)'],
                    ['Ortsvektor', 'Vektor vom Ursprung O zu einem Punkt; er hat dieselben Zahlen wie der Punkt']],
        'regel': 'Vektor von A nach B: ⟦Ende minus Anfang⟧, also (xB − xA | yB − yA). Punkt plus Vektor gibt den Bildpunkt. Vektoren addiert man Zahl für Zahl.',
        'schritte': [{'text': 'A(1 | 2) und B(6 | 5). Rechts: 6 − 1 = 5. Oben: 5 − 2 = 3.'},
                     {'text': 'Also ist der Vektor von A nach B gleich ⟦(5 | 3)⟧.'},
                     {'text': 'Probe: A(1 | 2) plus (5 | 3) ergibt (1 + 5 | 2 + 3) = (6 | 5). Das ist B.'}],
        'fehler': 'Anfang minus Ende rechnen: 1 − 6 = −5 ist falsch herum. Der Vektor zeigt dann von B nach A. Immer ⟦Ende minus Anfang⟧.',
    }
    A = []
    # Übungen Stufe 1
    A.append(auf(L, 'uebung', 1, 'direkt', 'zahl', 'A(2 | 1) und B(7 | 4). Wie viele Einheiten nach rechts zeigt der Vektor von A nach B?',
                 'Rechts: xB − xA = 7 − 2 = 5.', 'Ende minus Anfang, nur die erste Zahl.', o={'wert': 5}, c='7 - 2'))
    A.append(auf(L, 'uebung', 1, 'direkt', 'zahl', 'C(−3 | 5) und D(1 | −2). Berechne die zweite Zahl (nach oben) des Vektors von C nach D.',
                 'Oben: yD − yC = −2 − 5 = −7. Der Pfeil geht 7 nach unten.', 'Ende minus Anfang bei der zweiten Zahl.', o={'wert': -7}, c='-2 - 5'))
    A.append(auf(L, 'uebung', 1, 'erkennen', 'auswahl', 'Welcher Vektor führt von P(0 | 0) zu Q(4 | −3)?',
                 'Ende minus Anfang: (4 − 0 | −3 − 0) = (4 | −3).', 'Vom Ursprung aus hat der Vektor dieselben Zahlen wie der Zielpunkt.',
                 **wahl('(4 | −3)', ['(−4 | 3)', '(−3 | 4)', '(3 | −4)'], 1)))
    A.append(auf(L, 'uebung', 1, 'erkennen', 'auswahl', 'Der Vektor von A nach B ist (2 | 6). Welcher Vektor führt von B zurück nach A?',
                 'Der Rückweg ist der Gegenvektor: beide Zahlen mit umgekehrtem Vorzeichen, also (−2 | −6).', 'Zurück heißt: alles in die Gegenrichtung.',
                 **wahl('(−2 | −6)', ['(2 | 6)', '(6 | 2)', '(−2 | 6)'], 2)))
    # Stufe 2
    A.append(auf(L, 'uebung', 2, 'mehrschritt', 'luecken', 'A(3 | −1) wird mit dem Vektor (−5 | 4) verschoben. Gib die Koordinaten des Bildpunkts A′ an.',
                 'A′ = (3 + (−5) | −1 + 4) = (−2 | 3).', 'Punkt plus Vektor, Zahl für Zahl.',
                 f={'text': 'A(3 | −1) wird mit dem Vektor (−5 | 4) verschoben. Gib die Koordinaten des Bildpunkts A′ an.', 'schablone': 'A′(□ | □)', 'hinweis': 'Trage x und y ein.'},
                 o={'werte': [-2, 3]}, c=['3 + (-5)', '-1 + 4']))
    A.append(auf(L, 'uebung', 2, 'einkleidung', 'zahl', 'Ein Roboter steht bei (2 | 3). Er fährt erst (4 | 1), dann (−1 | 5). Bei welcher x-Koordinate steht er danach?',
                 'Vektoren addieren: (4 + (−1) | 1 + 5) = (3 | 6). Von (2 | 3) aus: x = 2 + 3 = 5.', 'Addiere zuerst die beiden Fahrten.', o={'wert': 5}, c='2 + 4 + (-1)'))
    A.append(auf(L, 'uebung', 2, 'umkehr', 'luecken', 'Nach der Verschiebung mit (3 | −2) liegt der Bildpunkt bei P′(1 | 4). Wo lag P?',
                 'Rückwärts: P = P′ minus Vektor = (1 − 3 | 4 − (−2)) = (−2 | 6).', 'Ziehe den Vektor vom Bildpunkt ab.',
                 f={'text': 'Nach der Verschiebung mit (3 | −2) liegt der Bildpunkt bei P′(1 | 4). Wo lag P?', 'schablone': 'P(□ | □)', 'hinweis': 'Trage x und y ein.'},
                 o={'werte': [-2, 6]}, c=['1 - 3', '4 - (-2)']))
    A.append(auf(L, 'uebung', 2, 'darstellung', 'luecken', 'Die Strecke AB hat A(−2 | 1) und B(4 | 7). Berechne den Mittelpunkt M der Strecke.',
                 'M = ((−2 + 4) : 2 | (1 + 7) : 2) = (1 | 4).', 'Mittelwert der x-Werte und der y-Werte.',
                 f={'text': 'Die Strecke AB hat A(−2 | 1) und B(4 | 7). Berechne den Mittelpunkt M der Strecke.', 'schablone': 'M(□ | □)', 'hinweis': 'Trage x und y ein.'},
                 o={'werte': [1, 4]}, c=['(-2 + 4) / 2', '(1 + 7) / 2']))
    # Stufe 3
    A.append(auf(L, 'uebung', 3, 'rueckwaerts', 'luecken', 'ABCD ist ein Parallelogramm mit A(1 | 1), B(6 | 2) und C(7 | 5). Berechne die vierte Ecke D.',
                 'Im Parallelogramm gilt: Vektor AD = Vektor BC = (7 − 6 | 5 − 2) = (1 | 3). D = A + (1 | 3) = (2 | 4).', 'Gegenüberliegende Seiten sind gleiche Vektoren.',
                 f={'text': 'ABCD ist ein Parallelogramm mit A(1 | 1), B(6 | 2) und C(7 | 5). Berechne die vierte Ecke D.', 'schablone': 'D(□ | □)', 'hinweis': 'Trage x und y ein.'},
                 o={'werte': [2, 4]}, c=['1 + (7 - 6)', '1 + (5 - 2)']))
    A.append(auf(L, 'uebung', 3, 'begruenden', 'auswahl', 'Die Vektoren von A nach B und von D nach C sind beide (5 | 2). Was folgt daraus für das Viereck ABCD?',
                 'Gleiche Vektoren heißen gleich lang und parallel. Zwei Seiten gleich lang und parallel: ABCD ist ein Parallelogramm.',
                 'Was haben gleiche Pfeile gemeinsam?',
                 **wahl('Es ist ein Parallelogramm.', ['Es ist ein Quadrat.', 'Es ist ein Drachenviereck.', 'Es ist ein Trapez, aber kein Parallelogramm.'], 0)))
    A.append(auf(L, 'uebung', 3, 'fehler', 'auswahl', 'Lina rechnet den Vektor von A(4 | 2) nach B(1 | 6) so: (4 − 1 | 2 − 6) = (3 | −4). Was stimmt?',
                 'Sie hat Anfang minus Ende gerechnet. Richtig: (1 − 4 | 6 − 2) = (−3 | 4).', 'Welche Reihenfolge gilt beim Vektor?',
                 **wahl('Falsch herum: richtig ist (−3 | 4).', ['Alles richtig.', 'Nur die erste Zahl ist falsch.', 'Richtig ist (5 | 8).'], 0)))
    A.append(auf(L, 'uebung', 3, 'transfer', 'zahl', 'Ein Schiff fährt von (0 | 0) dreimal hintereinander den Vektor (2 | 5). Welche y-Koordinate hat es danach?',
                 'Dreimal derselbe Vektor: 3 · (2 | 5) = (6 | 15). y = 15.', 'Dreimal addieren ist dreimal so viel.', o={'wert': 15}, c='3 * 5'))
    # Test, Korrektur, Sicherung
    A.append(auf(L, 'test', 2, None, 'luecken', 'Bestimme den Vektor von A(−1 | 4) nach B(3 | −2).', 'Ende minus Anfang: (3 − (−1) | −2 − 4) = (4 | −6).',
                 f={'text': 'Bestimme den Vektor von A(−1 | 4) nach B(3 | −2).', 'schablone': '(□ | □)', 'hinweis': 'Trage beide Zahlen ein.'}, o={'werte': [4, -6]}, c=['3 - (-1)', '-2 - 4']))
    for (ax, ay, bx, by) in ((2, 5, 8, 1), (-4, 0, 1, 3), (0, -3, -5, 2)):
        A.append(auf(L, 'korrektur', 2, None, 'luecken', f'Berechne den Vektor von A{V(ax, ay)} nach B{V(bx, by)}.', f'Ende minus Anfang: ({z(bx)} − {k(ax)} | {z(by)} − {k(ay)}) = {V(bx - ax, by - ay)}.',
                     f={'text': f'Berechne den Vektor von A{V(ax, ay)} nach B{V(bx, by)}.', 'schablone': '(□ | □)', 'hinweis': 'Trage beide Zahlen ein.'},
                     o={'werte': [bx - ax, by - ay]}, c=[f'{bx} - ({ax})', f'{by} - ({ay})']))
    for (px, py, vx, vy) in ((1, 1, 3, 4), (-2, 5, 6, -1), (4, -3, -4, 2), (0, 2, 5, 5), (-1, -1, 2, -3), (3, 0, -2, 6)):
        A.append(auf(L, 'sicherung', 2, None, 'luecken', f'Verschiebe P{V(px, py)} mit dem Vektor {V(vx, vy)}. Wo liegt P′?', f'P′ = ({z(px)} + {k(vx)} | {z(py)} + {k(vy)}) = {V(px + vx, py + vy)}.',
                     f={'text': f'Verschiebe P{V(px, py)} mit dem Vektor {V(vx, vy)}. Wo liegt P′?', 'schablone': 'P′(□ | □)', 'hinweis': 'Trage x und y ein.'},
                     o={'werte': [px + vx, py + vy]}, c=[f'{px} + ({vx})', f'{py} + ({vy})']))
    kann = 'aus zwei Punkten den Vektor berechnen, Punkte verschieben und die vierte Ecke eines Parallelogramms bestimmen'
    return karte, kann, A


# ------------------------------------------------------------------ 46 · vektor_drehen
def dreh(x, y, w):
    return {90: (-y, x), -90: (y, -x), 180: (-x, -y)}[w]


def vektor_drehen():
    L = 'vektor_drehen'
    karte = {
        'lernziel': L, 'titel': 'Vektoren um 90° und 180° drehen',
        'einstieg': 'Ein Kran schwenkt seinen Ausleger um eine Vierteldrehung. Die Spitze bewegt sich auf einem Kreis. Mit den Koordinaten des Auslegers kann man ihre neue Lage genau ausrechnen.',
        'woerter': [['Drehung um 90°', 'Vierteldrehung gegen den Uhrzeigersinn'], ['Drehung um −90°', 'Vierteldrehung im Uhrzeigersinn']],
        'regel': 'Um +90°: (x | y) wird ⟦(−y | x)⟧. Um −90°: (x | y) wird (y | −x). Um 180°: (x | y) wird (−x | −y).',
        'schritte': [{'text': 'Der Vektor (4 | 1) soll um +90° gedreht werden.'},
                     {'text': 'Zahlen tauschen und die neue erste Zahl umdrehen: (−1 | 4).'},
                     {'text': 'Punkt drehen um Z: erst den Vektor von Z zum Punkt drehen, dann an Z anhängen.'}],
        'fehler': 'Nur tauschen ohne Vorzeichen: (4 | 1) wird nicht (1 | 4). Bei +90° bekommt die ⟦neue erste Zahl ein Minus⟧.',
    }
    A = []
    A.append(auf(L, 'uebung', 1, 'direkt', 'luecken', 'Drehe den Vektor (3 | 2) um +90°.', '(x | y) → (−y | x): (−2 | 3).', 'Tauschen, dann vorne das Vorzeichen umdrehen.',
                 f={'text': 'Drehe den Vektor (3 | 2) um +90°.', 'schablone': '(□ | □)', 'hinweis': 'Trage beide Zahlen ein.'}, o={'werte': [-2, 3]}, c=['-2', '3']))
    A.append(auf(L, 'uebung', 1, 'direkt', 'luecken', 'Drehe den Vektor (−4 | 5) um 180°.', 'Bei 180° wechseln beide Vorzeichen: (4 | −5).', 'Halbe Drehung: der Pfeil zeigt genau zurück.',
                 f={'text': 'Drehe den Vektor (−4 | 5) um 180°.', 'schablone': '(□ | □)', 'hinweis': 'Trage beide Zahlen ein.'}, o={'werte': [4, -5]}, c=['4', '-5']))
    A.append(auf(L, 'uebung', 1, 'erkennen', 'auswahl', 'Welcher Vektor entsteht, wenn (6 | 1) um −90° gedreht wird?', '(x | y) → (y | −x): (1 | −6).', 'Im Uhrzeigersinn: tauschen, hinten das Vorzeichen umdrehen.',
                 **wahl('(1 | −6)', ['(−1 | 6)', '(−6 | −1)', '(1 | 6)'], 0)))
    A.append(auf(L, 'uebung', 1, 'erkennen', 'auswahl', 'Bei welcher Drehung bleibt die Länge eines Vektors gleich?', 'Drehungen ändern die Länge nie, nur die Richtung.', 'Denke an den Kranausleger.',
                 **wahl('Bei jeder Drehung', ['Nur bei 180°', 'Nur bei 90°', 'Bei keiner Drehung'], 0)))
    A.append(auf(L, 'uebung', 2, 'mehrschritt', 'luecken', 'Drehe P(5 | 3) um Z(2 | 1) um +90°. Gib P′ an.',
                 'Vektor ZP = (3 | 2). Gedreht: (−2 | 3). P′ = Z + (−2 | 3) = (0 | 4).', 'Erst Vektor ZP, dann drehen, dann an Z anhängen.',
                 f={'text': 'Drehe P(5 | 3) um Z(2 | 1) um +90°. Gib P′ an.', 'schablone': 'P′(□ | □)', 'hinweis': 'Trage x und y ein.'}, o={'werte': [0, 4]}, c=['2 + (-2)', '1 + 3']))
    A.append(auf(L, 'uebung', 2, 'einkleidung', 'luecken', 'Ein Zeiger zeigt vom Mittelpunkt aus (0 | 4). Nach einer Vierteldrehung im Uhrzeigersinn: Wohin zeigt er?',
                 'Um −90°: (x | y) → (y | −x) = (4 | 0). Er zeigt nach rechts.', 'Im Uhrzeigersinn heißt −90°.',
                 f={'text': 'Ein Zeiger zeigt vom Mittelpunkt aus (0 | 4). Nach einer Vierteldrehung im Uhrzeigersinn: Wohin zeigt er?', 'schablone': '(□ | □)', 'hinweis': 'Trage beide Zahlen ein.'}, o={'werte': [4, 0]}, c=['4', '0']))
    A.append(auf(L, 'uebung', 2, 'umkehr', 'luecken', 'Nach einer Drehung um +90° ist ein Vektor (−3 | 1). Wie lautete er vorher?',
                 'Zurückdrehen um −90°: (x | y) → (y | −x) = (1 | 3). Probe: (1 | 3) um +90° gibt (−3 | 1).', 'Drehe in die Gegenrichtung zurück.',
                 f={'text': 'Nach einer Drehung um +90° ist ein Vektor (−3 | 1). Wie lautete er vorher?', 'schablone': '(□ | □)', 'hinweis': 'Trage beide Zahlen ein.'}, o={'werte': [1, 3]}, c=['1', '3']))
    A.append(auf(L, 'uebung', 2, 'darstellung', 'auswahl', 'Der Vektor (2 | 0) zeigt nach rechts. Wohin zeigt er nach einer Drehung um 180°?', '(2 | 0) → (−2 | 0): nach links.', 'Halbe Drehung.',
                 **wahl('nach links', ['nach rechts', 'nach oben', 'nach unten'], 0)))
    A.append(auf(L, 'uebung', 3, 'rueckwaerts', 'luecken', 'Das Quadrat ABCD hat A(1 | 1) und B(4 | 2). Die Ecken laufen gegen den Uhrzeigersinn. Berechne D.',
                 'Vektor AB = (3 | 1). AD ist AB um +90° gedreht: (−1 | 3). D = A + (−1 | 3) = (0 | 4).', 'AD steht senkrecht auf AB und ist gleich lang.',
                 f={'text': 'Das Quadrat ABCD hat A(1 | 1) und B(4 | 2). Die Ecken laufen gegen den Uhrzeigersinn. Berechne D.', 'schablone': 'D(□ | □)', 'hinweis': 'Trage x und y ein.'}, o={'werte': [0, 4]}, c=['1 + (-1)', '1 + 3']))
    A.append(auf(L, 'uebung', 3, 'begruenden', 'auswahl', 'Warum ist (−y | x) senkrecht zu (x | y)?', 'Die Determinante bzw. das Produkt x · (−y) + y · x ist 0. Senkrechte Vektoren haben dieses Produkt 0.', 'Rechne x · (−y) + y · x.',
                 **wahl('Weil x · (−y) + y · x = 0 ist.', ['Weil beide gleich lang sind.', 'Weil beide Zahlen getauscht sind.', 'Weil x und y positiv sind.'], 0)))
    A.append(auf(L, 'uebung', 3, 'fehler', 'auswahl', 'Tom dreht (5 | 2) um +90° und erhält (2 | −5). Was stimmt?', 'Das ist die Drehung um −90°. Richtig für +90°: (−2 | 5).', 'Wo steht bei +90° das Minus?',
                 **wahl('Das ist −90°; richtig ist (−2 | 5).', ['Alles richtig.', 'Richtig ist (2 | 5).', 'Richtig ist (−5 | −2).'], 0)))
    A.append(auf(L, 'uebung', 3, 'transfer', 'zahl', 'Ein Vektor wird viermal nacheinander um +90° gedreht. Um wie viel Grad hat er sich insgesamt gedreht?', '4 · 90° = 360°: Er zeigt wieder in die alte Richtung.', 'Vier Vierteldrehungen.', o={'wert': 360}, c='4 * 90'))
    A.append(auf(L, 'test', 2, None, 'luecken', 'Drehe P(4 | 1) um Z(1 | 1) um +90°.', 'ZP = (3 | 0), gedreht (0 | 3), P′ = (1 | 4).',
                 f={'text': 'Drehe P(4 | 1) um Z(1 | 1) um +90°.', 'schablone': 'P′(□ | □)', 'hinweis': 'Trage x und y ein.'}, o={'werte': [1, 4]}, c=['1 + 0', '1 + 3']))
    for (x, y, w) in ((2, 5, 90), (-3, 4, -90), (6, -1, 180)):
        rx, ry = dreh(x, y, w)
        A.append(auf(L, 'korrektur', 2, None, 'luecken', f'Drehe den Vektor {V(x, y)} um {z(w)}°.', f'Ergebnis: {V(rx, ry)}.',
                     f={'text': f'Drehe den Vektor {V(x, y)} um {z(w)}°.', 'schablone': '(□ | □)', 'hinweis': 'Trage beide Zahlen ein.'}, o={'werte': [rx, ry]}, c=[str(rx), str(ry)]))
    for (x, y, w) in ((1, 4, 90), (5, 0, -90), (-2, -3, 180), (3, -2, 90), (-4, 1, -90), (0, -5, 180)):
        rx, ry = dreh(x, y, w)
        A.append(auf(L, 'sicherung', 2, None, 'luecken', f'Welcher Vektor entsteht aus {V(x, y)} bei einer Drehung um {z(w)}°?', f'Ergebnis: {V(rx, ry)}.',
                     f={'text': f'Welcher Vektor entsteht aus {V(x, y)} bei einer Drehung um {z(w)}°?', 'schablone': '(□ | □)', 'hinweis': 'Trage beide Zahlen ein.'}, o={'werte': [rx, ry]}, c=[str(rx), str(ry)]))
    kann = 'Vektoren und Punkte um 90°, −90° und 180° drehen und die neuen Koordinaten berechnen'
    return karte, kann, A


# ------------------------------------------------------------------ 47 · streckung_vektor
def streckung_vektor():
    L = 'streckung_vektor'
    karte = {
        'lernziel': L, 'titel': 'Strecken mit Vektoren rechnen',
        'einstieg': 'Ein Beamer vergrößert ein Bild von der Linse aus. Jeder Punkt wandert auf einem Strahl weg vom Zentrum, und zwar k-mal so weit. Mit Vektoren kann man die neue Lage genau berechnen.',
        'regel': 'Bildpunkt: ⟦P′ = Z + k · (Vektor ZP)⟧. Den Faktor findet man aus k = (Vektor ZP′) : (Vektor ZP), Zahl für Zahl.',
        'schritte': [{'text': 'Z(1 | 2), P(4 | 3), k = 2. Vektor ZP = (3 | 1).'},
                     {'text': 'k · ZP = (6 | 2). P′ = Z + (6 | 2) = ⟦(7 | 4)⟧.'}],
        'fehler': 'k · P statt k · ZP rechnen: 2 · (4 | 3) = (8 | 6) stimmt nur, wenn Z der Ursprung ist. Immer erst den ⟦Vektor vom Zentrum⟧ bilden.',
    }
    A = []
    A.append(auf(L, 'uebung', 1, 'direkt', 'luecken', 'Strecke den Vektor (2 | −3) mit k = 3.', '3 · (2 | −3) = (6 | −9).', 'Jede Zahl mal k.',
                 f={'text': 'Strecke den Vektor (2 | −3) mit k = 3.', 'schablone': '(□ | □)', 'hinweis': 'Trage beide Zahlen ein.'}, o={'werte': [6, -9]}, c=['3 * 2', '3 * (-3)']))
    A.append(auf(L, 'uebung', 1, 'direkt', 'luecken', 'Z ist der Ursprung, P(4 | 6), k = 0,5. Gib P′ an.', 'P′ = 0,5 · (4 | 6) = (2 | 3).', 'Vom Ursprung aus: Punkt mal k.',
                 f={'text': 'Z ist der Ursprung, P(4 | 6), k = 0,5. Gib P′ an.', 'schablone': 'P′(□ | □)', 'hinweis': 'Trage x und y ein.'}, o={'werte': [2, 3]}, c=['0.5 * 4', '0.5 * 6']))
    A.append(auf(L, 'uebung', 1, 'erkennen', 'auswahl', 'Was bewirkt der Faktor k = −1 bei einer zentrischen Streckung?', 'k = −1: gleich lang, entgegengesetzt – das ist die Punktspiegelung an Z.', 'Negatives k: der Bildpunkt liegt auf der anderen Seite von Z.',
                 **wahl('eine Punktspiegelung an Z', ['nichts', 'eine Verdopplung', 'eine Achsenspiegelung'], 0)))
    A.append(auf(L, 'uebung', 1, 'erkennen', 'auswahl', 'Bei welchem Faktor k wird eine Figur verkleinert?', 'Verkleinerung bei −1 < k < 1 (k ≠ 0), z. B. k = 0,4.', 'Vergleiche den Betrag von k mit 1.',
                 **wahl('k = 0,4', ['k = 2', 'k = −3', 'k = 1'], 0)))
    A.append(auf(L, 'uebung', 2, 'mehrschritt', 'luecken', 'Z(2 | 1), P(5 | 3), k = 2. Berechne P′.', 'ZP = (3 | 2), 2 · ZP = (6 | 4), P′ = (2 + 6 | 1 + 4) = (8 | 5).', 'Erst ZP, dann mal k, dann an Z anhängen.',
                 f={'text': 'Z(2 | 1), P(5 | 3), k = 2. Berechne P′.', 'schablone': 'P′(□ | □)', 'hinweis': 'Trage x und y ein.'}, o={'werte': [8, 5]}, c=['2 + 2 * 3', '1 + 2 * 2']))
    A.append(auf(L, 'uebung', 2, 'einkleidung', 'zahl', 'Eine Lampe steht bei Z(0 | 0). Eine Kante eines Gegenstands geht bis P(3 | 2). Ihr Schatten an der Wand ist 4-mal so weit von der Lampe entfernt. Welche x-Koordinate hat der Schattenpunkt?',
                 'P′ = 4 · (3 | 2) = (12 | 8). x = 12.', 'Vom Zentrum aus: mal k.', o={'wert': 12}, c='4 * 3'))
    A.append(auf(L, 'uebung', 2, 'umkehr', 'zahl', 'Z(1 | 1), P(3 | 2) und P′(7 | 4). Berechne den Faktor k.', 'ZP = (2 | 1), ZP′ = (6 | 3). k = 6 : 2 = 3 (und 3 : 1 = 3).', 'Teile die Zahlen von ZP′ durch die von ZP.', o={'wert': 3}, c='(7 - 1) / (3 - 1)'))
    A.append(auf(L, 'uebung', 2, 'darstellung', 'luecken', 'Z(0 | 2), P(4 | 2), k = −0,5. Gib P′ an.', 'ZP = (4 | 0), −0,5 · ZP = (−2 | 0), P′ = (−2 | 2).', 'Negatives k: auf die andere Seite von Z.',
                 f={'text': 'Z(0 | 2), P(4 | 2), k = −0,5. Gib P′ an.', 'schablone': 'P′(□ | □)', 'hinweis': 'Trage x und y ein.'}, o={'werte': [-2, 2]}, c=['0 + (-0.5) * 4', '2 + (-0.5) * 0']))
    A.append(auf(L, 'uebung', 3, 'rueckwaerts', 'luecken', 'Bei einer Streckung mit Z(1 | 0) und k = 3 entsteht P′(10 | 6). Wo lag P?', 'ZP′ = (9 | 6). ZP = ZP′ : 3 = (3 | 2). P = Z + (3 | 2) = (4 | 2).', 'Teile ZP′ durch k.',
                 f={'text': 'Bei einer Streckung mit Z(1 | 0) und k = 3 entsteht P′(10 | 6). Wo lag P?', 'schablone': 'P(□ | □)', 'hinweis': 'Trage x und y ein.'}, o={'werte': [4, 2]}, c=['1 + 9 / 3', '0 + 6 / 3']))
    A.append(auf(L, 'uebung', 3, 'begruenden', 'auswahl', 'Z(0 | 0), P(2 | 1) und Q(6 | 4). Kann Q ein Bildpunkt von P bei einer Streckung an Z sein?', '6 : 2 = 3, aber 4 : 1 = 4. Die Faktoren sind verschieden, also liegt Q nicht auf dem Strahl ZP.', 'Ein einziges k muss für beide Zahlen passen.',
                 **wahl('Nein, die Faktoren 3 und 4 sind verschieden.', ['Ja, mit k = 3.', 'Ja, mit k = 4.', 'Ja, mit k = 3,5.'], 0)))
    A.append(auf(L, 'uebung', 3, 'fehler', 'auswahl', 'Mia rechnet für Z(2 | 2), P(3 | 4), k = 2: P′ = 2 · (3 | 4) = (6 | 8). Was stimmt?', 'Sie hat den Punkt statt ZP gestreckt. Richtig: ZP = (1 | 2), 2 · ZP = (2 | 4), P′ = (4 | 6).', 'Liegt Z im Ursprung?',
                 **wahl('Falsch: richtig ist P′(4 | 6).', ['Alles richtig.', 'Richtig ist P′(5 | 6).', 'Richtig ist P′(8 | 10).'], 0)))
    A.append(auf(L, 'uebung', 3, 'transfer', 'zahl', 'Ein Dreieck wird mit k = 3 gestreckt. Sein Flächeninhalt war 4 cm². Wie groß ist er danach?', 'Flächen wachsen mit k²: 4 cm² · 9 = 36 cm².', 'Längen mal k, Flächen mal k².', o={'wert': 36, 'einheit': 'cm²'}, c='4 * 3 * 3'))
    A.append(auf(L, 'test', 2, None, 'luecken', 'Z(1 | 2), P(3 | 3), k = 3. Berechne P′.', 'ZP = (2 | 1), 3 · ZP = (6 | 3), P′ = (7 | 5).',
                 f={'text': 'Z(1 | 2), P(3 | 3), k = 3. Berechne P′.', 'schablone': 'P′(□ | □)', 'hinweis': 'Trage x und y ein.'}, o={'werte': [7, 5]}, c=['1 + 3 * 2', '2 + 3 * 1']))
    for (zx, zy, px, py, kk) in ((0, 1, 2, 3, 2), (2, -1, 4, 0, 3), (-1, 0, 1, 4, Fr(1, 2))):
        bx, by = zx + kk * (px - zx), zy + kk * (py - zy)
        A.append(auf(L, 'korrektur', 2, None, 'luecken', f'Z{V(zx, zy)}, P{V(px, py)}, k = {z(kk)}. Berechne P′.', f'ZP = {V(px - zx, py - zy)}, P′ = {V(bx, by)}.',
                     f={'text': f'Z{V(zx, zy)}, P{V(px, py)}, k = {z(kk)}. Berechne P′.', 'schablone': 'P′(□ | □)', 'hinweis': 'Trage x und y ein.'},
                     o={'werte': [float(bx) if isinstance(bx, Fr) else bx, float(by) if isinstance(by, Fr) else by]}, c=[f'{zx} + {float(kk)} * ({px} - ({zx}))', f'{zy} + {float(kk)} * ({py} - ({zy}))']))
    for (zx, zy, px, py, kk) in ((0, 0, 3, -1, 2), (1, 1, 2, 3, 3), (-2, 0, 0, 2, 2), (0, 2, 4, 4, Fr(1, 2)), (3, 1, 1, 2, -1), (1, -2, 3, -1, -2)):
        bx, by = zx + kk * (px - zx), zy + kk * (py - zy)
        A.append(auf(L, 'sicherung', 2, None, 'luecken', f'Strecke P{V(px, py)} an Z{V(zx, zy)} mit k = {z(kk)}. Wo liegt P′?', f'ZP = {V(px - zx, py - zy)}, k · ZP an Z anhängen: P′ = {V(bx, by)}.',
                     f={'text': f'Strecke P{V(px, py)} an Z{V(zx, zy)} mit k = {z(kk)}. Wo liegt P′?', 'schablone': 'P′(□ | □)', 'hinweis': 'Trage x und y ein.'},
                     o={'werte': [float(bx) if isinstance(bx, Fr) else bx, float(by) if isinstance(by, Fr) else by]}, c=[f'{zx} + {float(kk)} * ({px} - ({zx}))', f'{zy} + {float(kk)} * ({py} - ({zy}))']))
    kann = 'Bildpunkte einer zentrischen Streckung mit Vektoren berechnen und den Streckungsfaktor bestimmen'
    return karte, kann, A


# ------------------------------------------------------------------ 44 · vierecke_konstruieren
def vierecke_konstruieren():
    L = 'vierecke_konstruieren'
    karte = {
        'lernziel': L, 'titel': 'Vierecke konstruieren',
        'einstieg': 'Für ein Gartenbeet in Form eines Parallelogramms misst Ole zwei Seiten und einen Winkel. Reicht das, damit seine Schwester das Beet genau gleich nachbauen kann? Bei Vierecken hängt das von ihrer Art ab.',
        'regel': 'Ein beliebiges Viereck braucht ⟦5 Bestimmungsstücke⟧, ein Parallelogramm 3, ein Rechteck 2, eine Raute 2, ein Quadrat 1. Fehlende Winkel folgen aus der Winkelsumme 360° und den Eigenschaften.',
        'schritte': [{'text': 'Parallelogramm mit a = 5 cm, b = 3 cm, α = 70°.'},
                     {'text': 'Nachbarwinkel ergänzen sich zu 180°: β = 110°. Gegenüber gleich: γ = 70°, δ = 110°.'},
                     {'text': 'Konstruieren: a zeichnen, Winkel α antragen, b abtragen, Parallelen ziehen.'}],
        'fehler': 'Im Parallelogramm sind ⟦gegenüberliegende⟧ Winkel gleich, nicht benachbarte. Bei α = 70° ist β = 110°, nicht 70°.',
    }
    A = []
    A.append(auf(L, 'uebung', 1, 'direkt', 'zahl', 'Im Parallelogramm ABCD ist α = 65°. Wie groß ist β?', 'Benachbarte Winkel: α + β = 180°, also β = 115°.', 'Nachbarwinkel im Parallelogramm.', o={'wert': 115, 'einheit': '°'}, c='180 - 65'))
    A.append(auf(L, 'uebung', 1, 'direkt', 'zahl', 'Ein Viereck hat die Winkel 80°, 95° und 110°. Wie groß ist der vierte Winkel?', '360° − 80° − 95° − 110° = 75°.', 'Winkelsumme im Viereck.', o={'wert': 75, 'einheit': '°'}, c='360 - 80 - 95 - 110'))
    A.append(auf(L, 'uebung', 1, 'erkennen', 'auswahl', 'Wie viele Bestimmungsstücke braucht man mindestens für ein Rechteck?', 'Zwei Seitenlängen genügen, die Winkel sind alle 90°.', 'Welche Größen sind beim Rechteck schon festgelegt?',
                 **wahl('2', ['1', '3', '5'], 0)))
    A.append(auf(L, 'uebung', 1, 'erkennen', 'auswahl', 'Welche Angabe legt ein Quadrat eindeutig fest?', 'Eine Seitenlänge reicht, alles andere ist durch die Quadrat-Eigenschaften festgelegt.', 'Wie viele Stücke braucht ein Quadrat?',
                 **wahl('eine Seitenlänge', ['ein Winkel', 'die Winkelsumme', 'zwei Winkel'], 0)))
    A.append(auf(L, 'uebung', 2, 'mehrschritt', 'zahl', 'Im Drachenviereck ABCD (Symmetrieachse AC) sind α = 70° und γ = 110°. Wie groß ist β?', 'β und δ sind gleich: (360° − 70° − 110°) : 2 = 90°.', 'Im Drachen sind die Winkel neben der Symmetrieachse gleich.', o={'wert': 90, 'einheit': '°'}, c='(360 - 70 - 110) / 2'))
    A.append(auf(L, 'uebung', 2, 'einkleidung', 'zahl', 'Ein Fenster hat die Form eines gleichschenkligen Trapezes. Die Winkel an der langen Seite sind je 72°. Wie groß ist jeder Winkel an der kurzen Seite?', 'Nachbarwinkel an einem Schenkel: 180° − 72° = 108°.', 'Benachbarte Winkel an einem Schenkel ergänzen sich zu 180°.', o={'wert': 108, 'einheit': '°'}, c='180 - 72'))
    A.append(auf(L, 'uebung', 2, 'umkehr', 'zahl', 'In einer Raute ist ein Winkel doppelt so groß wie sein Nachbarwinkel. Wie groß ist der kleinere Winkel?', 'x + 2x = 180° ⇒ x = 60°.', 'Nachbarwinkel ergeben zusammen 180°.', o={'wert': 60, 'einheit': '°'}, c='180 / 3'))
    A.append(auf(L, 'uebung', 2, 'darstellung', 'auswahl', 'Ein Parallelogramm ist durch a = 6 cm, b = 4 cm und α = 50° gegeben. Was zeichnest du zuerst?', 'Man beginnt mit der Seite a, an deren Anfang α angetragen wird.', 'Mit einer gegebenen Seite beginnen.',
                 **wahl('die Seite a', ['die Diagonale', 'den Winkel γ', 'die Höhe'], 0)))
    A.append(auf(L, 'uebung', 3, 'rueckwaerts', 'zahl', 'In einem Viereck sind die Winkel im Verhältnis 1 : 2 : 3 : 4. Wie groß ist der größte Winkel?', '1 + 2 + 3 + 4 = 10 Teile = 360°, ein Teil 36°. Größter: 4 · 36° = 144°.', 'Verteile 360° auf 10 Teile.', o={'wert': 144, 'einheit': '°'}, c='4 * 360 / 10'))
    A.append(auf(L, 'uebung', 3, 'begruenden', 'auswahl', 'Reichen a = 5 cm, b = 3 cm und c = 5 cm, um ein Parallelogramm eindeutig zu konstruieren?', 'Nein: Es fehlt ein Winkel oder eine Diagonale. Mit nur Seiten kann man das Parallelogramm noch „kippen“.', 'Ist die Form schon starr?',
                 **wahl('Nein, es fehlt ein Winkel.', ['Ja, drei Stücke reichen immer.', 'Ja, weil c = a ist.', 'Nein, es fehlen zwei Seiten.'], 0)))
    A.append(auf(L, 'uebung', 3, 'fehler', 'auswahl', 'Jan sagt: „Im Drachenviereck sind alle vier Seiten gleich lang.“ Was stimmt?', 'Im Drachen sind nur je zwei benachbarte Seiten gleich lang. Alle vier gleich: das ist eine Raute.', 'Zeichne einen Drachen.',
                 **wahl('Falsch: das gilt nur für die Raute.', ['Richtig.', 'Falsch: das gilt nur für das Trapez.', 'Richtig, wenn die Diagonalen senkrecht sind.'], 0)))
    A.append(auf(L, 'uebung', 3, 'transfer', 'zahl', 'Ein Bauplatz ist ein Parallelogramm mit α = 80°. Ein Zaun soll den Winkel β halbieren. Wie groß ist jeder der beiden Teilwinkel?', 'β = 180° − 80° = 100°, halbiert: 50°.', 'Erst β, dann halbieren.', o={'wert': 50, 'einheit': '°'}, c='(180 - 80) / 2'))
    A.append(auf(L, 'test', 2, None, 'zahl', 'Im Parallelogramm ist α = 48°. Wie groß ist δ?', 'δ ist Nachbarwinkel von α: 180° − 48° = 132°.', o={'wert': 132, 'einheit': '°'}, c='180 - 48'))
    for w in (35, 102, 76):
        A.append(auf(L, 'korrektur', 2, None, 'zahl', f'Im Parallelogramm ABCD ist α = {w}°. Wie groß ist β?', f'β = 180° − {w}° = {180 - w}°.', o={'wert': 180 - w, 'einheit': '°'}, c=f'180 - {w}'))
    for (a, b, c) in ((90, 85, 100), (70, 120, 95), (60, 60, 120), (110, 80, 75), (95, 95, 85), (130, 50, 90)):
        A.append(auf(L, 'sicherung', 2, None, 'zahl', f'Ein Viereck hat die Winkel {a}°, {b}° und {c}°. Berechne den vierten Winkel.', f'360° − {a}° − {b}° − {c}° = {360 - a - b - c}°.', o={'wert': 360 - a - b - c, 'einheit': '°'}, c=f'360 - {a} - {b} - {c}'))
    kann = 'entscheiden, welche Angaben ein Viereck festlegen, und fehlende Winkel in Vierecken berechnen'
    return karte, kann, A


# ------------------------------------------------------------------ 99 · drachen_raute
def drachen_raute():
    L = 'drachen_raute'
    karte = {
        'lernziel': L, 'titel': 'Drachenviereck und Raute',
        'einstieg': 'Ein Papierdrachen wird aus zwei Leisten gebaut, die sich senkrecht kreuzen. Spannt man Papier darum, entsteht ein Drachenviereck. Wie viel Papier braucht man? Die beiden Leisten verraten es.',
        'woerter': [['Diagonale', 'Verbindungsstrecke zweier gegenüberliegender Ecken'], ['Raute', 'Viereck mit vier gleich langen Seiten']],
        'regel': 'Drachen und Raute: Die Diagonalen e und f stehen senkrecht. ⟦A = e · f : 2⟧.',
        'schritte': [{'text': 'Ein Drachen hat die Diagonalen e = 8 cm und f = 5 cm.'},
                     {'text': 'Rechteck um den Drachen: 8 cm · 5 cm = 40 cm². Der Drachen ist genau die Hälfte: ⟦20 cm²⟧.'}],
        'fehler': 'e · f ohne Halbieren: 8 · 5 = 40 cm² ist das umgebende Rechteck. Der Drachen ist nur ⟦die Hälfte⟧.',
    }
    A = []
    A.append(auf(L, 'uebung', 1, 'direkt', 'zahl', 'Ein Drachenviereck hat die Diagonalen e = 6 cm und f = 4 cm. Berechne den Flächeninhalt.', 'A = 6 cm · 4 cm : 2 = 12 cm².', 'Diagonalen malnehmen, dann halbieren.', o={'wert': 12, 'einheit': 'cm²'}, c='6 * 4 / 2'))
    A.append(auf(L, 'uebung', 1, 'direkt', 'zahl', 'Eine Raute hat die Diagonalen 10 cm und 7 cm. Wie groß ist ihr Flächeninhalt?', 'A = 10 cm · 7 cm : 2 = 35 cm².', 'Gleiche Formel wie beim Drachen.', o={'wert': 35, 'einheit': 'cm²'}, c='10 * 7 / 2'))
    A.append(auf(L, 'uebung', 1, 'erkennen', 'auswahl', 'Welche Eigenschaft haben Drachenviereck und Raute gemeinsam?', 'Bei beiden stehen die Diagonalen senkrecht aufeinander.', 'Denke an die gekreuzten Leisten.',
                 **wahl('Die Diagonalen stehen senkrecht.', ['Alle Seiten sind gleich lang.', 'Alle Winkel sind 90°.', 'Gegenüberliegende Seiten sind parallel.'], 0)))
    A.append(auf(L, 'uebung', 1, 'erkennen', 'auswahl', 'Welche Formel gilt für den Flächeninhalt eines Drachenvierecks?', 'A = e · f : 2, mit den Diagonalen e und f.', 'Die Hälfte des umgebenden Rechtecks.',
                 **wahl('A = e · f : 2', ['A = e · f', 'A = (e + f) : 2', 'A = 2 · (e + f)'], 0)))
    A.append(auf(L, 'uebung', 2, 'mehrschritt', 'zahl', 'Eine Raute hat die Diagonalen 1,2 m und 50 cm. Gib den Flächeninhalt in cm² an.', '1,2 m = 120 cm. A = 120 cm · 50 cm : 2 = 3 000 cm².', 'Erst in eine Einheit umrechnen.', o={'wert': 3000, 'einheit': 'cm²'}, c='120 * 50 / 2'))
    A.append(auf(L, 'uebung', 2, 'einkleidung', 'zahl', 'Für einen Drachen sind die Leisten 90 cm und 60 cm lang. Wie viel cm² Papier bedeckt der Drachen?', 'A = 90 cm · 60 cm : 2 = 2 700 cm².', 'Die Leisten sind die Diagonalen.', o={'wert': 2700, 'einheit': 'cm²'}, c='90 * 60 / 2'))
    A.append(auf(L, 'uebung', 2, 'umkehr', 'zahl', 'Ein Drachen hat 24 cm² Fläche und die Diagonale e = 8 cm. Wie lang ist f?', '24 = 8 · f : 2 ⇒ 48 = 8 · f ⇒ f = 6 cm.', 'Rechne rückwärts: mal 2, dann durch e.', o={'wert': 6, 'einheit': 'cm'}, c='2 * 24 / 8'))
    A.append(auf(L, 'uebung', 2, 'darstellung', 'zahl', 'Ein Quadrat hat die Diagonale 6 cm. Berechne seine Fläche mit der Drachenformel.', 'Ein Quadrat ist eine besondere Raute: e = f = 6 cm. A = 6 · 6 : 2 = 18 cm².', 'Beide Diagonalen sind gleich lang.', o={'wert': 18, 'einheit': 'cm²'}, c='6 * 6 / 2'))
    A.append(auf(L, 'uebung', 3, 'rueckwaerts', 'zahl', 'Eine Raute hat 54 cm² Fläche. Eine Diagonale ist 3-mal so lang wie die andere. Wie lang ist die kürzere Diagonale?', 'x · 3x : 2 = 54 ⇒ 3x² = 108 ⇒ x² = 36 ⇒ x = 6 cm.', 'Setze für die längere 3x ein.', o={'wert': 6, 'einheit': 'cm'}, c='2 * 54 / 3 / 6'))
    A.append(auf(L, 'uebung', 3, 'begruenden', 'auswahl', 'Warum ist die Fläche eines Drachens genau die Hälfte des umgebenden Rechtecks?', 'Die Diagonalen teilen das Rechteck in acht rechtwinklige Dreiecke; der Drachen besteht aus vier davon, das Rechteck aus allen acht.', 'Zeichne das Rechteck um den Drachen.',
                 **wahl('Der Drachen besteht aus 4 von 8 gleich großen Dreieckspaaren.', ['Weil der Drachen symmetrisch ist.', 'Weil alle Seiten halb so lang sind.', 'Weil die Winkel halb so groß sind.'], 0)))
    A.append(auf(L, 'uebung', 3, 'fehler', 'auswahl', 'Eva berechnet für eine Raute mit e = 9 cm und f = 4 cm: A = 9 · 4 = 36 cm². Was stimmt?', 'Sie hat vergessen zu halbieren. Richtig: 36 : 2 = 18 cm².', 'Vergleiche mit der Formel.',
                 **wahl('Falsch: richtig sind 18 cm².', ['Alles richtig.', 'Richtig sind 26 cm².', 'Richtig sind 72 cm².'], 0)))
    A.append(auf(L, 'uebung', 3, 'transfer', 'zahl', 'Ein Fliesenmuster besteht aus 20 Rauten mit den Diagonalen 30 cm und 20 cm. Wie viele m² bedecken sie?', 'Eine Raute: 30 · 20 : 2 = 300 cm². 20 Rauten: 6 000 cm² = 0,6 m².', 'Erst eine Raute, dann alle; zum Schluss in m².', o={'wert': 0.6, 'einheit': 'm²'}, c='20 * 30 * 20 / 2 / 10000'))
    A.append(auf(L, 'test', 2, None, 'zahl', 'Ein Drachenviereck hat die Diagonalen 12 cm und 5 cm. Berechne den Flächeninhalt.', 'A = 12 · 5 : 2 = 30 cm².', o={'wert': 30, 'einheit': 'cm²'}, c='12 * 5 / 2'))
    for (e, f) in ((14, 6), (9, 8), (11, 4)):
        A.append(auf(L, 'korrektur', 2, None, 'zahl', f'Eine Raute hat die Diagonalen e = {e} cm und f = {f} cm. Wie groß ist ihre Fläche?', f'A = {e} · {f} : 2 = {z(Fr(e * f, 2))} cm².', o={'wert': e * f / 2, 'einheit': 'cm²'}, c=f'{e} * {f} / 2'))
    for (e, f) in ((7, 4), (16, 3), (5, 5), (13, 6), (20, 9), (15, 8)):
        A.append(auf(L, 'sicherung', 2, None, 'zahl', f'Berechne den Flächeninhalt eines Drachenvierecks mit e = {e} cm und f = {f} cm.', f'A = {e} · {f} : 2 = {z(Fr(e * f, 2))} cm².', o={'wert': e * f / 2, 'einheit': 'cm²'}, c=f'{e} * {f} / 2'))
    kann = 'den Flächeninhalt von Drachenviereck und Raute aus den Diagonalen berechnen'
    return karte, kann, A


# ------------------------------------------------------------------ 91 · wahre_groesse
def wahre_groesse():
    L = 'wahre_groesse'
    karte = {
        'lernziel': L, 'titel': 'Wahre Größe im Schrägbild',
        'einstieg': 'Auf einem Bauplan ist eine Kiste im Schrägbild gezeichnet. Die Kanten nach hinten sehen kürzer aus, als sie sind. Wer die Kiste bauen will, muss die wahren Längen zurückrechnen.',
        'woerter': [['Verkürzungsfaktor q', 'Kanten nach hinten werden mit q gezeichnet, z. B. q = 0,5'], ['wahre Größe', 'die echte Länge oder Form am Körper']],
        'regel': 'Kanten ⟦nach hinten⟧: gezeichnete Länge = wahre Länge · q, also wahre Länge = gezeichnet : q. Flächen parallel zur Zeichenebene erscheinen in wahrer Größe.',
        'schritte': [{'text': 'Eine Kante nach hinten ist mit q = 0,5 als 2,5 cm gezeichnet.'},
                     {'text': 'Wahre Länge: 2,5 cm : 0,5 = ⟦5 cm⟧.'},
                     {'text': 'Die Vorderfläche wird nicht verkürzt: Ihre Kanten und Winkel sind echt.'}],
        'fehler': 'Mit q malnehmen statt teilen: 2,5 · 0,5 = 1,25 cm wäre noch kürzer. Beim Zurückrechnen ⟦teilt⟧ man durch q.',
    }
    A = []
    A.append(auf(L, 'uebung', 1, 'direkt', 'zahl', 'Im Schrägbild (q = 0,5) ist eine Kante nach hinten 3 cm lang gezeichnet. Wie lang ist sie wirklich?', '3 cm : 0,5 = 6 cm.', 'Durch q teilen.', o={'wert': 6, 'einheit': 'cm'}, c='3 / 0.5'))
    A.append(auf(L, 'uebung', 1, 'direkt', 'zahl', 'Eine Kante nach hinten ist 8 cm lang. Wie lang zeichnest du sie mit q = 0,5?', '8 cm · 0,5 = 4 cm.', 'Beim Zeichnen mit q malnehmen.', o={'wert': 4, 'einheit': 'cm'}, c='8 * 0.5'))
    A.append(auf(L, 'uebung', 1, 'erkennen', 'auswahl', 'Welche Fläche eines Quaders erscheint im üblichen Schrägbild in wahrer Größe?', 'Die Vorderfläche liegt parallel zur Zeichenebene und wird nicht verzerrt.', 'Welche Fläche schaut dich direkt an?',
                 **wahl('die Vorderfläche', ['die Grundfläche', 'die rechte Seitenfläche', 'keine Fläche'], 0)))
    A.append(auf(L, 'uebung', 1, 'erkennen', 'auswahl', 'Ein rechter Winkel der Grundfläche wird im Schrägbild gezeichnet. Wie sieht er aus?', 'Die Grundfläche ist verzerrt: der rechte Winkel erscheint z. B. als 45° oder 135°.', 'Die Grundfläche liegt nach hinten.',
                 **wahl('verzerrt, nicht als 90°', ['immer als 90°', 'als 180°', 'gar nicht'], 0)))
    A.append(auf(L, 'uebung', 2, 'mehrschritt', 'zahl', 'Ein Quader ist 6 cm breit, 4 cm hoch und 5 cm tief. Im Schrägbild (q = 0,5) wird er gezeichnet. Wie lang zeichnest du alle 4 Tiefenkanten zusammen?', 'Eine Tiefenkante: 5 cm · 0,5 = 2,5 cm. Vier Stück: 10 cm.', 'Erst eine Kante, dann alle vier.', o={'wert': 10, 'einheit': 'cm'}, c='4 * 5 * 0.5'))
    A.append(auf(L, 'uebung', 2, 'einkleidung', 'zahl', 'Auf dem Bauplan einer Kiste (q = 0,5, Maßstab 1 : 10) ist die Tiefe 2 cm lang gezeichnet. Wie tief ist die Kiste in Wirklichkeit in cm?', 'Wahre Länge im Plan: 2 cm : 0,5 = 4 cm. Maßstab 1 : 10: 40 cm.', 'Erst q, dann den Maßstab.', o={'wert': 40, 'einheit': 'cm'}, c='2 / 0.5 * 10'))
    A.append(auf(L, 'uebung', 2, 'umkehr', 'zahl', 'Eine Kante ist 6 cm lang und wurde nach hinten als 4 cm gezeichnet. Welcher Verkürzungsfaktor q wurde benutzt? Gib q als Dezimalzahl auf zwei Stellen an.', 'q = 4 : 6 ≈ 0,67.', 'gezeichnet : wahr.', o={'wert': 0.67}, c='round(4 / 6, 2)'))
    A.append(auf(L, 'uebung', 2, 'darstellung', 'auswahl', 'Im Schrägbild eines Würfels sind alle Kanten nach hinten halb so lang gezeichnet. Was gilt für den echten Würfel?', 'Am echten Würfel sind alle Kanten gleich lang; nur die Zeichnung verkürzt die Tiefe.', 'Unterscheide Zeichnung und Körper.',
                 **wahl('Alle Kanten sind gleich lang.', ['Die hinteren Kanten sind kürzer.', 'Der Würfel ist ein Quader.', 'Die Vorderfläche ist kleiner.'], 0)))
    A.append(auf(L, 'uebung', 3, 'rueckwaerts', 'zahl', 'Im Schrägbild (q = 0,5) einer quadratischen Säule ist die Tiefenkante 2 cm lang. Die Grundfläche ist ein Quadrat. Wie groß ist die echte Grundfläche in cm²?', 'Wahre Tiefe 2 : 0,5 = 4 cm. Quadrat: 4 cm · 4 cm = 16 cm².', 'Erst die wahre Länge, dann die Fläche.', o={'wert': 16, 'einheit': 'cm²'}, c='(2 / 0.5) * (2 / 0.5)'))
    A.append(auf(L, 'uebung', 3, 'begruenden', 'auswahl', 'Warum kann man im Schrägbild die Länge einer Raumdiagonale nicht direkt messen?', 'Sie verläuft schräg nach hinten und wird verzerrt dargestellt; nur Strecken parallel zur Zeichenebene sind in wahrer Länge.', 'Welche Strecken sind unverzerrt?',
                 **wahl('Weil sie verzerrt gezeichnet wird.', ['Weil sie zu lang ist.', 'Weil sie unsichtbar ist.', 'Weil Diagonalen keine Länge haben.'], 0)))
    A.append(auf(L, 'uebung', 3, 'fehler', 'auswahl', 'Max misst im Schrägbild (q = 0,5) eine Tiefenkante von 3,5 cm und sagt: „Die Kiste ist 1,75 cm tief.“ Was stimmt?', 'Er hat mit q multipliziert. Richtig: 3,5 : 0,5 = 7 cm.', 'Zurückrechnen heißt teilen.',
                 **wahl('Falsch: sie ist 7 cm tief.', ['Richtig.', 'Falsch: sie ist 3,5 cm tief.', 'Falsch: sie ist 5 cm tief.'], 0)))
    A.append(auf(L, 'uebung', 3, 'transfer', 'zahl', 'Ein Schrank (Breite 80 cm, Höhe 180 cm, Tiefe 60 cm) wird im Maßstab 1 : 20 mit q = 0,5 gezeichnet. Wie lang wird die Tiefenkante gezeichnet (in cm)?', '60 cm : 20 = 3 cm, mal q = 0,5: 1,5 cm.', 'Erst verkleinern, dann verkürzen.', o={'wert': 1.5, 'einheit': 'cm'}, c='60 / 20 * 0.5'))
    A.append(auf(L, 'test', 2, None, 'zahl', 'Im Schrägbild mit q = 0,5 ist eine Tiefenkante 4,5 cm lang. Wie lang ist sie wirklich?', '4,5 cm : 0,5 = 9 cm.', o={'wert': 9, 'einheit': 'cm'}, c='4.5 / 0.5'))
    for g in (1.5, 3.2, 6):
        A.append(auf(L, 'korrektur', 2, None, 'zahl', f'Eine Tiefenkante ist mit q = 0,5 als {z(g)} cm gezeichnet. Berechne die wahre Länge.', f'{z(g)} cm : 0,5 = {z(g * 2)} cm.', o={'wert': g * 2, 'einheit': 'cm'}, c=f'{g} / 0.5'))
    for (w, q) in ((10, 0.5), (7, 0.5), (12, 0.5), (9, 0.5), (4, 0.5), (15, 0.5)):
        A.append(auf(L, 'sicherung', 2, None, 'zahl', f'Eine Kante nach hinten ist {z(w)} cm lang. Wie lang wird sie mit q = {z(q)} gezeichnet?', f'{z(w)} cm · {z(q)} = {z(w * q)} cm.', o={'wert': w * q, 'einheit': 'cm'}, c=f'{w} * {q}'))
    kann = 'im Schrägbild verkürzte Tiefenkanten in wahre Längen zurückrechnen und Flächen in wahrer Größe erkennen'
    return karte, kann, A


NEU = {'abbildungen.kongruenz': [vektor_koordinaten, vektor_drehen], 'abbildungen.aehnlichkeit': [streckung_vektor],
       'geometrie.konstruktion': [vierecke_konstruieren], 'messen.flaechen_vielecke': [drachen_raute], 'raum.schraegbilder': [wahre_groesse]}
ABSCHNITT = 'Lehrplan-Ergänzung (LK)'


def _schluessel(a):
    return (a['l'], a['p'], a['f']['text'], json.dumps(a.get('a'), ensure_ascii=False), json.dumps(a['f'].get('schablone'), ensure_ascii=False))


def lk_anhaengen(thema):
    pfad = THEMEN / f'{thema}.json'
    roh = pfad.read_text(encoding='utf-8')
    d = json.loads(roh)
    inh = d['inhalt']
    da = {_schluessel(a) for a in d['aufgaben']}
    neu_k = neu_a = 0
    kann_neu = {}
    for fn in NEU[thema]:
        karte, kann, auf_ = fn()
        L = karte['lernziel']
        if L not in [e['lernziel'] for e in inh['etappen']]:
            inh['etappen'].append(karte)
            ab = next((x for x in inh['abschnitte'] if x['titel'] == ABSCHNITT), None)
            if ab is None:
                ab = {'titel': ABSCHNITT, 'lernziele': []}
                inh['abschnitte'].append(ab)
            ab['lernziele'].append(L)
            inh['teilfaehigkeiten'].append({'k': L, 'lernziele': [L]})
            inh['bewertung'].setdefault('lernziele_vertiefung', []).append(L)
            neu_k += 1
        kann_neu[L] = kann
        for a in auf_:
            if _schluessel(a) in da:
                continue
            d['aufgaben'].append(a)
            da.add(_schluessel(a))
            neu_a += 1
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')
    kp = KANN / f'{thema}.json'
    if kp.exists():
        kr = kp.read_text(encoding='utf-8')
        kd = json.loads(kr)
        for L, s in kann_neu.items():
            kd['etappen'].setdefault(L, s)
        kp.write_text(json.dumps(kd, ensure_ascii=False, indent=1) + ('\n' if kr.endswith('\n') else ''), encoding='utf-8')
    print(f'  LK {thema}: {neu_k} neue Lernkarten, {neu_a} neue Aufgaben')


if __name__ == '__main__':
    import sys
    for t in (sys.argv[1:] or list(NEU)):
        lk_anhaengen(t)
