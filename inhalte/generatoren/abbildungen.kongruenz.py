#!/usr/bin/env python3
"""Thema abbildungen.kongruenz – Kongruenzabbildungen (Gymnasium Bayern, Klasse 7)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl7 import A, L, Z, baue, kl, zt  # noqa: E402

META = {'thema_schluessel': 'abbildungen.kongruenz', 'thema_id': 46, 'block_id': 82, 'klasse': {'gym_by': 7, 'rs_by': 6}}
HP = 'Trage die x- und die y-Koordinate des Bildpunkts ein.'

ETAPPEN = [
    {'lernziel': 'achsenspiegelung', 'titel': 'An einer Achse spiegeln',
     'regel': 'Bei der ⟦Achsenspiegelung⟧ liegt der Bildpunkt P\' auf der anderen Seite der Achse, ⟦gleich weit⟧ von ihr entfernt; PP\' steht ⟦senkrecht⟧ auf der Achse. An der x-Achse ändert sich das Vorzeichen von y, an der y-Achse das von x.',
     'schritte': ['P(4 | 3) an der Geraden x = 1 spiegeln', 'P ist 3 Einheiten rechts der Achse, P\' 3 Einheiten links: x = 1 − 3 = −2', 'y bleibt: ⟦P\'(−2 | 3)⟧'],
     'fehler': 'Spiegelt man P(4 | 3) an der x-Achse, ist das Bild nicht (−4 | 3): An der ⟦x-Achse⟧ ändert sich die ⟦y-Koordinate⟧, also P\'(4 | −3).',
     '_verbot': ['P(4 | 3) an der Geraden x = 1']},
    {'lernziel': 'punktspiegelung', 'titel': 'An einem Punkt spiegeln',
     'regel': 'Bei der ⟦Punktspiegelung⟧ an Z ist Z der ⟦Mittelpunkt⟧ der Strecke PP\'. Man geht von P zu Z und ⟦dieselbe Strecke noch einmal⟧ weiter.',
     'schritte': ['P(1 | 5) an Z(3 | 2) spiegeln', 'Von P nach Z: 2 nach rechts, 3 nach unten', 'Noch einmal: ⟦P\'(5 | −1)⟧'],
     'probe': 'Mittelpunkt von P und P\': ((1 + 5) : 2 | (5 − 1) : 2) = (3 | 2) = Z ✓',
     'fehler': 'Bei der Spiegelung an Z(3 | 2) geht man nicht nur bis Z, sondern ⟦doppelt so weit⟧. P\'(3 | 2) wäre Z selbst.',
     '_verbot': ['P(1 | 5) an Z(3 | 2)']},
    {'lernziel': 'verschiebung', 'titel': 'Figuren verschieben',
     'regel': 'Bei einer ⟦Verschiebung⟧ wandert jeder Punkt gleich weit in dieselbe Richtung. Der ⟦Verschiebungspfeil⟧ v = (a | b) heißt: a nach rechts (negativ: links), b nach oben (negativ: unten).',
     'schritte': ['A(2 | −1) wird mit v = (−3 | 4) verschoben.', 'x: 2 + (−3) = −1; y: −1 + 4 = 3', '⟦A\'(−1 | 3)⟧'],
     'fehler': 'Bei v = (−3 | 4) addiert man −3 zur ⟦x⟧- und 4 zur ⟦y⟧-Koordinate – nicht umgekehrt.',
     '_verbot': ['A(2 | −1)']},
    {'lernziel': 'drehung', 'titel': 'Um einen Punkt drehen',
     'regel': 'Bei einer ⟦Drehung⟧ um Z bleibt der Abstand zu Z gleich. Um den Ursprung gilt (gegen den Uhrzeigersinn): ⟦90°: (x | y) → (−y | x)⟧, 180°: (x | y) → (−x | −y), 270°: (x | y) → (y | −x).',
     'schritte': ['P(4 | 1) um O(0 | 0) um 90° gegen den Uhrzeigersinn drehen', '(x | y) → (−y | x)', '⟦P\'(−1 | 4)⟧'],
     'fehler': 'Bei 90° wird nicht einfach das Vorzeichen geändert: (4 | 1) → (−4 | −1) wäre eine Drehung um ⟦180°⟧.',
     '_verbot': ['P(4 | 1) um O(0 | 0)']},
    {'lernziel': 'symmetrie', 'titel': 'Symmetrische Figuren',
     'regel': 'Eine Figur ist ⟦achsensymmetrisch⟧, wenn sie bei einer Spiegelung an einer Achse auf sich selbst fällt; ⟦punktsymmetrisch⟧, wenn sie bei einer Drehung um 180° auf sich fällt. Ein regelmäßiges n-Eck hat ⟦n Symmetrieachsen⟧.',
     'schritte': ['Rechteck (kein Quadrat)', '2 Symmetrieachsen (durch die Seitenmitten)', 'Punktsymmetrisch zum Diagonalenschnittpunkt: ⟦ja⟧'],
     'fehler': 'Die Diagonalen eines Rechtecks sind ⟦keine⟧ Symmetrieachsen (außer beim Quadrat): Spiegelt man daran, fallen die Ecken nicht aufeinander.'},
    {'lernziel': 'eigenschaften', 'titel': 'Was bleibt bei Abbildungen gleich?',
     'regel': 'Kongruenzabbildungen erhalten ⟦Längen, Winkel und Flächeninhalte⟧: Bild und Urbild sind ⟦deckungsgleich⟧. Nur die Achsenspiegelung kehrt den ⟦Umlaufsinn⟧ um. Zwei Achsenspiegelungen nacheinander ergeben eine Verschiebung (parallele Achsen) oder eine Drehung (sich schneidende Achsen).',
     'schritte': ['Spiegeln an zwei parallelen Achsen mit Abstand 3 cm', 'Ergebnis: eine Verschiebung', 'um ⟦2 · 3 cm = 6 cm⟧ senkrecht zu den Achsen'],
     'fehler': 'Eine Drehung verändert nicht die Größe der Figur. Sie dreht sie nur – Seitenlängen und Winkel ⟦bleiben gleich⟧.'},
]


def nz(R, lo, hi): return R.choice([k for k in range(lo, hi + 1) if k])


def P(x, y, n='P'): return f'{n}({zt(x)} | {zt(y)})'


def LP(text, x, y, w, h, name="P'"):
    return L(text, f"{name}(□ | □)", [x, y], [str(x), str(y)], w, h, HP)


def g_achsenspiegelung(R, st):
    x, y = nz(R, -8, 8), nz(R, -8, 8)
    if st == 1:
        achse = R.choice(['x-Achse', 'y-Achse'])
        bx, by = (x, -y) if achse == 'x-Achse' else (-x, y)
        return LP(f'Spiegle {P(x, y)} an der {achse}.', bx, by, f'An der {achse} ändert sich das Vorzeichen der {"y" if achse == "x-Achse" else "x"}-Koordinate: {P(bx, by, chr(80) + chr(39))}.',
                  'Welche Koordinate ändert sich, welche bleibt?')
    if st == 2:
        a = nz(R, -5, 5)
        if a in (x, y): a = a + 1 if a + 1 not in (x, y, 0) else a - 1 if a - 1 not in (x, y, 0) else a + 2
        if R.random() < .5:
            bx, by = 2 * a - x, y
            return LP(f'Spiegle {P(x, y)} an der Geraden x = {zt(a)} (senkrecht zur x-Achse).', bx, by,
                      f'Abstand zur Achse: {zt(x)} − {kl(a)} = {zt(x - a)}. Auf der anderen Seite: {zt(a)} − {kl(x - a)} = {zt(bx)}. y bleibt {zt(y)}.', 'Wie weit ist P von der Achse entfernt? Gleich weit auf die andere Seite.')
        bx, by = x, 2 * a - y
        return LP(f'Spiegle {P(x, y)} an der Geraden y = {zt(a)} (parallel zur x-Achse).', bx, by,
                  f'Abstand zur Achse: {zt(y)} − {kl(a)} = {zt(y - a)}. Auf der anderen Seite: {zt(a)} − {kl(y - a)} = {zt(by)}. x bleibt {zt(x)}.', 'Wie weit ist P von der Achse entfernt? Gleich weit auf die andere Seite.')
    if R.random() < .5:
        if x == y: y += 1
        return LP(f'Spiegle {P(x, y)} an der Winkelhalbierenden y = x.', y, x, f'An y = x werden die Koordinaten vertauscht: {P(y, x, chr(80) + chr(39))}.',
                  'Bei y = x tauschen x- und y-Koordinate die Plätze.')
    d = nz(R, -5, 5)
    bx = x + 2 * d
    return Z(f'{P(x, y)} wird an einer Geraden senkrecht zur x-Achse auf {P(bx, y, chr(80) + chr(39))} gespiegelt. Gib die Achse an: x = □', Fr(x + bx, 2), f'({x} + {bx}) / 2',
             f'Die Achse geht durch die Mitte von P und P\': x = ({zt(x)} + {kl(bx)}) : 2 = {zt(Fr(x + bx, 2))}.', 'Die Achse liegt genau in der Mitte zwischen P und P\'.')


def g_punktspiegelung(R, st):
    x, y = nz(R, -7, 7), nz(R, -7, 7)
    if st == 1:
        return LP(f'Spiegle {P(x, y)} am Ursprung O(0 | 0).', -x, -y, f'Am Ursprung ändern beide Koordinaten ihr Vorzeichen: {P(-x, -y, chr(80) + chr(39))}.',
                  'Gehe von P zum Ursprung und noch einmal so weit.')
    zx, zy = R.choice([k for k in range(-4, 5) if k not in (0, x)]), R.choice([k for k in range(-4, 5) if k not in (0, y)])
    if st == 2 or R.random() < .5:
        bx, by = 2 * zx - x, 2 * zy - y
        return LP(f'Spiegle {P(x, y)} am Punkt {P(zx, zy, "Z")}.', bx, by,
                  f'Von P nach Z: x {"+" if zx - x >= 0 else "−"}{abs(zx - x)}, y {"+" if zy - y >= 0 else "−"}{abs(zy - y)}. Noch einmal: {P(bx, by, chr(80) + chr(39))}.',
                  'Rechne aus, wie weit es von P nach Z ist – und gehe von Z dieselbe Strecke weiter.')
    bx, by = 2 * zx - x, 2 * zy - y
    return L(f'Bei einer Punktspiegelung wird {P(x, y)} auf {P(bx, by, chr(80) + chr(39))} abgebildet. Gib das Zentrum an.', 'Z(□ | □)', [zx, zy], [f'({x} + {bx}) // 2', f'({y} + {by}) // 2'],
             f'Z ist der Mittelpunkt von PP\': (({zt(x)} + {kl(bx)}) : 2 | ({zt(y)} + {kl(by)}) : 2) = {P(zx, zy, "Z")}.', 'Das Zentrum liegt in der Mitte zwischen P und P\'.', HP)


def g_verschiebung(R, st):
    x, y = nz(R, -7, 7), nz(R, -7, 7)
    a, b = nz(R, -6, 6), nz(R, -6, 6)
    if st == 1:
        return LP(f'Verschiebe {P(x, y)} mit v = ({zt(a)} | {zt(b)}).', x + a, y + b,
                  f'x: {zt(x)} + {kl(a)} = {zt(x + a)}; y: {zt(y)} + {kl(b)} = {zt(y + b)}.', 'Addiere a zur x- und b zur y-Koordinate.')
    if st == 2:
        return L(f'{P(x, y)} wird auf {P(x + a, y + b, chr(80) + chr(39))} verschoben. Gib den Verschiebungspfeil an.', 'v = (□ | □)', [a, b],
                 [f'{x + a} - ({x})', f'{y + b} - ({y})'], f'a = {zt(x + a)} − {kl(x)} = {zt(a)}; b = {zt(y + b)} − {kl(y)} = {zt(b)}.',
                 'Wie weit nach rechts/links, wie weit nach oben/unten?', 'Trage ein, wie weit nach rechts (x) und nach oben (y) verschoben wird.')
    bx, by = nz(R, -7, 7), nz(R, -7, 7)
    return LP(f'Ein Dreieck ABC wird verschoben. {P(x, y, "A")} wird dabei auf A\'({zt(x + a)} | {zt(y + b)}) abgebildet. Wohin kommt {P(bx, by, "B")}?', bx + a, by + b,
              f'Pfeil: v = ({zt(a)} | {zt(b)}). B\' = ({zt(bx)} + {kl(a)} | {zt(by)} + {kl(b)}) = ({zt(bx + a)} | {zt(by + b)}).', 'Bestimme erst den Pfeil aus A und A\'.', name="B'")


def dreh(x, y, w):
    return {90: (-y, x), 180: (-x, -y), 270: (y, -x)}[w]


def g_drehung(R, st):
    x, y = nz(R, -7, 7), nz(R, -7, 7)
    if st == 1:
        w = R.choice([180, 90])
        bx, by = dreh(x, y, w)
        return LP(f'Drehe {P(x, y)} um O(0 | 0) um {w}° gegen den Uhrzeigersinn.', bx, by,
                  f'{w}°: (x | y) → {"(−y | x)" if w == 90 else "(−x | −y)"}. Also {P(bx, by, chr(80) + chr(39))}.', 'Merke die Regel für 90° und 180°.')
    if st == 2:
        w = R.choice([90, 270])
        uhr = R.random() < .4
        ww = 360 - w if uhr else w
        bx, by = dreh(x, y, ww)
        txt = f'um {w}° {"im" if uhr else "gegen den"} Uhrzeigersinn'
        return LP(f'Drehe {P(x, y)} um O(0 | 0) {txt}.', bx, by,
                  (f'{w}° im Uhrzeigersinn = {ww}° gegen den Uhrzeigersinn. ' if uhr else '') + f'{ww}°: (x | y) → {"(−y | x)" if ww == 90 else "(y | −x)"}. Also {P(bx, by, chr(80) + chr(39))}.',
                  'Im Uhrzeigersinn um 90° ist dasselbe wie gegen den Uhrzeigersinn um 270°.')
    zx, zy = nz(R, -3, 3), nz(R, -3, 3)
    w = R.choice([90, 180, 270])
    dx, dy = dreh(x - zx, y - zy, w)
    bx, by = zx + dx, zy + dy
    return LP(f'Drehe {P(x, y)} um {P(zx, zy, "Z")} um {w}° gegen den Uhrzeigersinn.', bx, by,
              f'P relativ zu Z: ({zt(x - zx)} | {zt(y - zy)}). Gedreht: ({zt(dx)} | {zt(dy)}). Wieder zu Z addieren: {P(bx, by, chr(80) + chr(39))}.',
              'Rechne erst, wie P von Z aus liegt. Drehe das, dann addiere Z wieder.')


FIG = [  # Name, Symmetrieachsen, punktsymmetrisch
    ('ein Quadrat', 4, True), ('ein Rechteck, das kein Quadrat ist', 2, True), ('eine Raute, die kein Quadrat ist', 2, True),
    ('ein Parallelogramm, das weder Rechteck noch Raute ist', 0, True), ('ein Drachenviereck, das keine Raute ist', 1, False),
    ('ein gleichschenkliges Trapez, das kein Rechteck ist', 1, False), ('ein gleichseitiges Dreieck', 3, False),
    ('ein gleichschenkliges Dreieck, das nicht gleichseitig ist', 1, False), ('ein Dreieck mit drei verschieden langen Seiten', 0, False),
    ('ein regelmäßiges Sechseck', 6, True), ('ein regelmäßiges Fünfeck', 5, False), ('ein regelmäßiges Achteck', 8, True),
]


def g_symmetrie(R, st):
    if st == 1:
        f, n, _ = R.choice(FIG)
        return Z(f'Wie viele Symmetrieachsen hat {f}?', n, f'{n}', f'{f[0].upper() + f[1:]}{"," if ", die" in f else ""} hat {n} Symmetrieachse{"n" if n != 1 else ""}.',
                 'Stell dir vor, du faltest die Figur: Wo fallen die Hälften genau aufeinander?')
    if st == 2:
        if R.random() < .5:
            f, n, p = R.choice(FIG)
            r = 'Ja' if p else 'Nein'
            return A(R, f'Ist {f} punktsymmetrisch?', f'{r}, ' + ('eine Drehung um 180° um den Mittelpunkt bildet die Figur auf sich ab.' if p else 'nach einer Drehung um 180° liegt die Figur anders.'),
                     ['Ja, eine Drehung um 180° um den Mittelpunkt bildet die Figur auf sich ab.' if not p else 'Nein, nach einer Drehung um 180° liegt die Figur anders.',
                      'Ja, weil die Figur eine Symmetrieachse hat.', 'Nein, nur Kreise sind punktsymmetrisch.'],
                     f'{f[0].upper() + f[1:]}{"," if ", die" in f else ""} ist {"" if p else "nicht "}punktsymmetrisch.', 'Drehe die Figur in Gedanken um 180°.')
        n = R.choice([3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20])
        return Z(f'Um welchen kleinsten Winkel (größer als 0°) muss man ein regelmäßiges {n}-Eck um seinen Mittelpunkt drehen, damit es auf sich selbst fällt?', Fr(360, n), f'360 / {n}',
                 f'360° : {n} = {zt(Fr(360, n))}°.', 'Ein voller Umlauf hat 360°, verteilt auf n gleiche Teile.', '°')
    n = R.choice([3, 4, 5, 6, 7, 8, 9, 10, 12])
    iw = Fr(180 * (n - 2), n)
    if R.random() < .5 and (360 / iw).denominator == 1:
        return Z(f'Ein regelmäßiges {n}-Eck hat Innenwinkel von {zt(iw)}°. Wie viele dieser {n}-Ecke treffen sich in einer Ecke, wenn man damit lückenlos parkettiert?', 360 / iw,
                 f'360 / {zt(iw).replace(",", ".")}', f'360° : {zt(iw)}° = {zt(360 / iw)}.', 'Rund um eine Ecke müssen die Winkel zusammen 360° ergeben.')
    geht = (360 / iw).denominator == 1
    r = 'Ja' if geht else 'Nein'
    return A(R, f'Ein regelmäßiges {n}-Eck hat Innenwinkel von {zt(iw)}°. Kann man mit lauter solchen {n}-Ecken die Ebene lückenlos parkettieren?',
             f'{r}, denn 360° : {zt(iw)}° ' + ('ist eine ganze Zahl.' if geht else 'ist keine ganze Zahl.'),
             [f'{"Nein" if geht else "Ja"}, denn 360° : {zt(iw)}° ' + ('ist keine ganze Zahl.' if geht else 'ist eine ganze Zahl.'), 'Ja, mit jedem regelmäßigen Vieleck geht das.',
              'Nein, das geht nur mit Quadraten.'], f'360° : {zt(iw)}° = {zt(360 / iw)}' + ('.' if geht else ' – keine ganze Zahl, es bleibt eine Lücke.'),
             'An jeder Ecke müssen die Innenwinkel zusammen genau 360° ergeben.')


ABB = ['Achsenspiegelung', 'Punktspiegelung', 'Verschiebung', 'Drehung']


def g_eigenschaften(R, st):
    if st == 3 and R.random() < .6:
        if R.random() < .5:
            d = Fr(R.randint(2, 30), R.choice([1, 2]))
            return Z(f'Eine Figur wird an zwei parallelen Achsen nacheinander gespiegelt. Die Achsen haben {zt(d)} cm Abstand. Um wie viel cm ist das Bild insgesamt verschoben?', 2 * d,
                     f'2 * {d}' if d.denominator == 1 else f'2 * {d.numerator} / {d.denominator}', f'Zwei Spiegelungen an parallelen Achsen = Verschiebung um den doppelten Abstand: 2 · {zt(d)} = {zt(2 * d)} cm.',
                     'Probiere es mit einem Punkt auf einer Achse aus.', 'cm')
        a = R.choice([15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90])
        return Z(f'Eine Figur wird an zwei Achsen gespiegelt, die sich unter {a}° schneiden. Um welchen Winkel ist das Bild gegenüber dem Original gedreht?', 2 * a, f'2 * {a}',
                 f'Zwei Spiegelungen an sich schneidenden Achsen = Drehung um den doppelten Schnittwinkel: 2 · {a}° = {2 * a}°.', 'Der Drehwinkel ist doppelt so groß wie der Winkel zwischen den Achsen.', '°')
    al = [('Bei einer Drehung bleiben alle Seitenlängen gleich.', True), ('Bei einer Achsenspiegelung ändert sich der Umlaufsinn.', True),
          ('Bei einer Verschiebung ändert sich der Umlaufsinn.', False), ('Eine Punktspiegelung ist dasselbe wie eine Drehung um 180°.', True),
          ('Bei einer Drehung um 90° wird der Flächeninhalt größer.', False), ('Bild und Urbild einer Kongruenzabbildung sind deckungsgleich.', True),
          ('Bei einer Punktspiegelung werden alle Winkel verdoppelt.', False), ('Eine Verschiebung hat einen Fixpunkt.', False),
          ('Bei einer Achsenspiegelung bleiben die Punkte auf der Achse fest.', True), ('Das Drehzentrum einer Drehung bewegt sich bei der Drehung mit.', False),
          ('Zwei Achsenspiegelungen an parallelen Achsen ergeben eine Verschiebung.', True), ('Zwei Achsenspiegelungen ergeben wieder eine Achsenspiegelung.', False),
          ('Eine Verschiebung bildet jede Gerade auf eine parallele Gerade ab.', True), ('Eine Achsenspiegelung verändert Winkelgrößen.', False)]
    wahr = [t for t, w in al if w]; falsch = [t for t, w in al if not w]
    if st == 1 or (st == 2 and R.random() < .5):
        t = R.choice(wahr)
        return A(R, 'Welche Aussage über Kongruenzabbildungen ist richtig?', t, R.sample(falsch, 3), f'Richtig: {t} Kongruenzabbildungen erhalten Längen, Winkel und Flächen.',
                 'Kongruent heißt deckungsgleich. Was kann sich dann überhaupt ändern?')
    t = R.choice(falsch)
    return A(R, 'Welche Aussage über Kongruenzabbildungen ist FALSCH?', t, R.sample(wahr, 3), f'Falsch: {t} Längen, Winkel und Flächen bleiben immer gleich; nur die Achsenspiegelung kehrt den Umlaufsinn um.',
             'Prüfe jede Aussage an einem einfachen Beispiel.')


GEN = {'achsenspiegelung': g_achsenspiegelung, 'punktspiegelung': g_punktspiegelung, 'verschiebung': g_verschiebung, 'drehung': g_drehung,
       'symmetrie': g_symmetrie, 'eigenschaften': g_eigenschaften}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Spiegeln', ['achsenspiegelung', 'punktspiegelung']), ('Verschieben und Drehen', ['verschiebung', 'drehung']), ('Symmetrie und Eigenschaften', ['symmetrie', 'eigenschaften'])],
         'Achsenspiegelung, Punktspiegelung, Verschiebung und Drehung im Koordinatensystem ausführen, Symmetrien von Figuren erkennen und die Eigenschaften von Kongruenzabbildungen begründen.',
         ['Achsenspiegelung: gleich weit auf die andere Seite, senkrecht zur Achse.', 'Punktspiegelung an Z: Z ist Mitte von P und P\'.',
          'Verschiebung v = (a | b): x + a, y + b. Drehung um O um 90°: (x | y) → (−y | x).', 'Längen, Winkel und Flächen bleiben erhalten.'],
         offen=['Alle Lernkarten arbeiten mit Koordinaten statt mit Zeichnungen. Ein Koordinatensystem, in dem das Kind Punkte und Figuren abbildet, fehlt der App; '
                'Konstruktionen mit Zirkel und Geodreieck (Achse, Zentrum, Drehwinkel zeichnen) sind deshalb nicht gebaut.',
                'Parkettierungen nur rechnerisch (Innenwinkel regelmäßiger Vielecke); Bilder von Parketten fehlen.',
                'Drehungen nur um Vielfache von 90°, weil andere Winkel im Koordinatensystem ohne Trigonometrie nicht exakt berechenbar sind.'])
