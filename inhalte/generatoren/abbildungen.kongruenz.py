#!/usr/bin/env python3
"""Thema abbildungen.kongruenz – Kongruenzabbildungen (Gymnasium Bayern, Klasse 7)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import re
from _kl7 import A, L, Z, baue, figur, kl, ksys, zt  # noqa: E402

META = {'thema_schluessel': 'abbildungen.kongruenz', 'thema_id': 46, 'block_id': 82, 'klasse': {'gym_by': 7, 'rs_by': 6}}
HP = 'Trage die x- und die y-Koordinate des Bildpunkts ein.'

ETAPPEN = [
    {'lernziel': 'achsenspiegelung', 'titel': 'An einer Achse spiegeln',
     'regel': 'Bei der ⟦Achsenspiegelung⟧ liegt der Bildpunkt P\' auf der anderen Seite der Achse, ⟦gleich weit⟧ von ihr entfernt; PP\' steht ⟦senkrecht⟧ auf der Achse. An der x-Achse ändert sich das Vorzeichen von y, an der y-Achse das von x.',
     'schritte': ['P(4 | 3) an der Geraden x = 1 spiegeln', 'P ist 3 Einheiten rechts der Achse, P\' 3 Einheiten links: x = 1 − 3 = −2', 'y bleibt: ⟦P\'(−2 | 3)⟧'],
     'fehler': 'Spiegelt man P(4 | 3) an der x-Achse, ist das Bild nicht (−4 | 3): An der ⟦x-Achse⟧ ändert sich die ⟦y-Koordinate⟧, also P\'(4 | −3).',
     'bild': ksys([(4, 3, 'P'), (-2, 3, "P'")], senkrecht=[1], strecken=[(4, 3, -2, 3, 'gestrichelt')]),
     '_verbot': ['P(4 | 3) an der Geraden x = 1']},
    {'lernziel': 'punktspiegelung', 'titel': 'An einem Punkt spiegeln',
     'regel': 'Bei der ⟦Punktspiegelung⟧ an Z ist Z der ⟦Mittelpunkt⟧ der Strecke PP\'. Man geht von P zu Z und ⟦dieselbe Strecke noch einmal⟧ weiter.',
     'schritte': ['P(1 | 5) an Z(3 | 2) spiegeln', 'Von P nach Z: 2 nach rechts, 3 nach unten', 'Noch einmal: ⟦P\'(5 | −1)⟧'],
     'probe': 'Mittelpunkt von P und P\': ((1 + 5) : 2 | (5 − 1) : 2) = (3 | 2) = Z ✓',
     'fehler': 'Bei der Spiegelung an Z(3 | 2) geht man nicht nur bis Z, sondern ⟦doppelt so weit⟧. P\'(3 | 2) wäre Z selbst.',
     'bild': ksys([(1, 5, 'P'), (3, 2, 'Z'), (5, -1, "P'")], strecken=[(1, 5, 5, -1, 'gestrichelt')]),
     '_verbot': ['P(1 | 5) an Z(3 | 2)']},
    {'lernziel': 'verschiebung', 'titel': 'Figuren verschieben',
     'regel': 'Bei einer ⟦Verschiebung⟧ wandert jeder Punkt gleich weit in dieselbe Richtung. Der ⟦Verschiebungspfeil⟧ v = (a | b) heißt: a nach rechts (negativ: links), b nach oben (negativ: unten).',
     'schritte': ['A(2 | −1) wird mit v = (−3 | 4) verschoben.', 'x: 2 + (−3) = −1; y: −1 + 4 = 3', '⟦A\'(−1 | 3)⟧'],
     'fehler': 'Bei v = (−3 | 4) addiert man −3 zur ⟦x⟧- und 4 zur ⟦y⟧-Koordinate – nicht umgekehrt.',
     'bild': ksys([(2, -1, 'A'), (-1, 3, "A'")], strecken=[(2, -1, -1, 3)]),
     '_verbot': ['A(2 | −1)']},
    {'lernziel': 'drehung', 'titel': 'Um einen Punkt drehen',
     'regel': 'Bei einer ⟦Drehung⟧ um Z bleibt der Abstand zu Z gleich. Drehung um den Ursprung um 90° gegen den Uhrzeigersinn: Der Weg zu P(4 | 1) ist „4 nach rechts, 1 nach oben“. Gedreht wird daraus „4 nach oben, 1 nach links“. Also ⟦(x | y) → (−y | x)⟧. Um 180°: (x | y) → (−x | −y).',
     'schritte': ['P(4 | 1): Von O aus 4 nach rechts und 1 nach oben.', 'Um 90° gedreht: Aus „4 nach rechts“ wird „4 nach oben“, aus „1 nach oben“ wird „1 nach links“.', "⟦P'(−1 | 4)⟧"],
     'fehler': 'Bei 90° wird nicht einfach das Vorzeichen geändert: (4 | 1) → (−4 | −1) wäre eine Drehung um ⟦180°⟧.',
     'bild': ksys([(4, 1, 'P'), (-1, 4, "P'"), (0, 0, 'O')], strecken=[(0, 0, 4, 1, 'gestrichelt'), (0, 0, -1, 4, 'gestrichelt')]),
     '_verbot': ['P(4 | 1) um O(0 | 0)', 'P(4 | 1)']},
    {'lernziel': 'symmetrie', 'titel': 'Symmetrische Figuren',
     'regel': 'Eine Figur ist ⟦achsensymmetrisch⟧, wenn sie bei einer Spiegelung an einer Achse auf sich selbst fällt; ⟦punktsymmetrisch⟧, wenn sie bei einer Drehung um 180° auf sich fällt. Ein regelmäßiges n-Eck hat ⟦n Symmetrieachsen⟧.',
     'schritte': ['Rechteck (kein Quadrat)', '2 Symmetrieachsen (durch die Seitenmitten)', 'Punktsymmetrisch zum Diagonalenschnittpunkt: ⟦ja⟧'],
     'bild': figur({'A': [0, 0], 'B': [6, 0], 'C': [6, 3], 'D': [0, 3], '_1': [3, -0.7], '_2': [3, 3.7], '_3': [-0.7, 1.5], '_4': [6.7, 1.5]}, flaeche=['A', 'B', 'C', 'D'],
                   linien=[['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A'], ['_1', '_2', 'Achse', 'gestrichelt'], ['_3', '_4', 'Achse', 'gestrichelt']]),
     'fehler': 'Die Diagonalen eines Rechtecks sind ⟦keine⟧ Symmetrieachsen (außer beim Quadrat): Spiegelt man daran, fallen die Ecken nicht aufeinander.'},
    {'lernziel': 'parkett', 'titel': 'Lückenlos auslegen (Parkett)',
     'regel': 'Mit lauter gleichen regelmäßigen Vielecken kann man eine Fläche nur dann ⟦lückenlos⟧ auslegen, wenn die Winkel, die an einer Ecke zusammenstoßen, genau ⟦360°⟧ ergeben. Der Innenwinkel muss also in 360° ⟦aufgehen⟧.',
     'schritte': ['Gleichseitiges Dreieck: Innenwinkel 60°. 360° : 60° = 6 – sechs Dreiecke passen um eine Ecke ✓', 'Quadrat: 360° : 90° = 4 ✓. Regelmäßiges Sechseck: 360° : 120° = 3 ✓ (wie bei Bienenwaben).', 'Regelmäßiges Fünfeck: Innenwinkel 108°. 360° : 108° = 3,33… – es bleibt eine Lücke: ⟦kein Parkett⟧.'],
     'fehler': '„Jedes regelmäßige Vieleck ergibt ein Parkett.“ Falsch: Beim Fünfeck passen drei Ecken (324°) und es bleibt eine Lücke von 36°; vier wären 432°, zu viel. Nur bei ⟦Dreieck, Quadrat und Sechseck⟧ geht 360° glatt auf.',
     'bild': {'typ': 'figur', 'punkte': {'O': [0, 0], '_h0': [3.0, 0.0], '_h1': [1.5, 2.6], '_h2': [-1.5, 2.6], '_h3': [-3.0, 0.0], '_h4': [-1.5, -2.6], '_h5': [1.5, -2.6]}, 'linien': [['O', '_h0'], ['_h0', '_h1'], ['O', '_h1'], ['_h1', '_h2'], ['O', '_h2'], ['_h2', '_h3'], ['O', '_h3'], ['_h3', '_h4'], ['O', '_h4'], ['_h4', '_h5'], ['O', '_h5'], ['_h5', '_h0']], 'winkel': [['O', '_h0', '_h1', '60°']]}},
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
    ZAEHL['achse'] = ZAEHL.get('achse', -1) + 1
    art = ['ymx', 'achse_x', 'yx', 'achse_y'][ZAEHL['achse'] % 4]
    if art == 'yx':
        if x == y: y += 1
        return LP(f'Spiegle {P(x, y)} an der Winkelhalbierenden y = x.', y, x, f'An y = x werden die Koordinaten vertauscht: {P(y, x, chr(80) + chr(39))}.',
                  'Bei y = x tauschen x- und y-Koordinate die Plätze.')
    if art == 'ymx':
        if x == -y: y += 1
        return LP(f'Spiegle {P(x, y)} an der Geraden y = −x.', -y, -x, f'An y = −x werden die Koordinaten vertauscht und beide Vorzeichen geändert: {P(-y, -x, chr(80) + chr(39))}.',
                  'Wie bei y = x tauschen die Koordinaten – zusätzlich ändern sich beide Vorzeichen.')
    d = nz(R, -5, 5)
    if art == 'achse_x':
        bx = x + 2 * d
        return L(f'{P(x, y)} wird an einer Geraden senkrecht zur x-Achse auf {P(bx, y, chr(80) + chr(39))} gespiegelt. Gib die Achse an.', 'x = □', [x + d], [f'({x} + {bx}) // 2'],
                 f'Die Achse geht durch die Mitte von P und P\': x = ({zt(x)} + {kl(bx)}) : 2 = {zt(x + d)}.', 'Die Achse liegt genau in der Mitte zwischen P und P\'.',
                 'Trage die Zahl ein.')
    by = y + 2 * d
    return L(f'{P(x, y)} wird an einer Geraden parallel zur x-Achse auf {P(x, by, chr(80) + chr(39))} gespiegelt. Gib die Achse an.', 'y = □', [y + d], [f'({y} + {by}) // 2'],
             f'Die Achse geht durch die Mitte von P und P\': y = ({zt(y)} + {kl(by)}) : 2 = {zt(y + d)}.', 'Die Achse liegt genau in der Mitte zwischen P und P\'.',
             'Trage die Zahl ein.')


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
    if R.random() < .5:
        c, d = nz(R, -6, 6), nz(R, -6, 6)
        if R.random() < .5:
            return L(f'{P(x, y)} wird erst mit ({zt(a)} | {zt(b)}), dann mit ({zt(c)} | {zt(d)}) verschoben. Welcher Pfeil ersetzt beide Verschiebungen?', 'v = (□ | □)',
                     [a + c, b + d], [f'{a} + ({c})', f'{b} + ({d})'], f'Pfeile addieren: ({zt(a)} + {kl(c)} | {zt(b)} + {kl(d)}) = ({zt(a + c)} | {zt(b + d)}).',
                     'Zwei Verschiebungen hintereinander sind wieder eine Verschiebung. Addiere die Pfeile.', 'Trage ein, wie weit nach rechts (x) und nach oben (y) insgesamt verschoben wird.')
        return LP(f'{P(x, y)} wird erst mit ({zt(a)} | {zt(b)}), dann mit ({zt(c)} | {zt(d)}) verschoben. Wohin kommt P?', x + a + c, y + b + d,
                  f'Gesamtpfeil ({zt(a + c)} | {zt(b + d)}). P\' = ({zt(x)} + {kl(a + c)} | {zt(y)} + {kl(b + d)}) = ({zt(x + a + c)} | {zt(y + b + d)}).', 'Addiere erst die beiden Pfeile.')
    bx, by = nz(R, -7, 7), nz(R, -7, 7)
    return LP(f'Ein Dreieck ABC wird verschoben. {P(x, y, "A")} wird dabei auf A\'({zt(x + a)} | {zt(y + b)}) abgebildet. Wohin kommt {P(bx, by, "B")}?', bx + a, by + b,
              f'Pfeil: v = ({zt(a)} | {zt(b)}). B\' = ({zt(bx)} + {kl(a)} | {zt(by)} + {kl(b)}) = ({zt(bx + a)} | {zt(by + b)}).', 'Bestimme erst den Pfeil aus A und A\'.', name="B'")


ZAEHL = {'270': 0, 'aussage': 0}


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
        art = R.choice(['gegen90', 'im90', 'erkennen', 'erkennen', 'gegen270'])
        if art == 'gegen270':
            if ZAEHL['270'] >= 3: art = 'gegen90'
            else: ZAEHL['270'] += 1
        if art == 'erkennen':
            if x == 0 or y == 0: x, y = x or 2, y or 1
            w = R.choice([90, 180, 270])
            bx, by = dreh(x, y, w)
            return A(R, f'{P(x, y)} wurde um O(0 | 0) gedreht und liegt jetzt bei {P(bx, by, chr(80) + chr(39))}. Um welchen Winkel gegen den Uhrzeigersinn wurde gedreht?',
                     f'{w}°', ['90°', '180°', '270°', '45°'],
                     f'Der Weg von O zu P ({"rechts" if x > 0 else "links"} {abs(x)}, {"oben" if y > 0 else "unten"} {abs(y)}) wurde um {w}° gegen den Uhrzeigersinn mitgedreht: {P(bx, by, chr(80) + chr(39))}.',
                     'Schau, in welchem Viertel P und P\' liegen. Eine Vierteldrehung sind 90°.')
        if art == 'im90':
            bx, by = dreh(x, y, 270)
            return LP(f'Drehe {P(x, y)} um O(0 | 0) um 90° im Uhrzeigersinn.', bx, by,
                      f'Im Uhrzeigersinn: aus „rechts“ wird „unten“, aus „oben“ wird „rechts“. (x | y) → (y | −x). Also {P(bx, by, chr(80) + chr(39))}.',
                      'Drehe den Weg von O zu P (rechts/oben) eine Vierteldrehung mit dem Uhrzeiger.')
        w = 270 if art == 'gegen270' else 90
        bx, by = dreh(x, y, w)
        return LP(f'Drehe {P(x, y)} um O(0 | 0) um {w}° gegen den Uhrzeigersinn.', bx, by,
                  f'{w}°: (x | y) → {"(−y | x)" if w == 90 else "(y | −x)"}. Also {P(bx, by, chr(80) + chr(39))}.',
                  'Drehe den Weg von O zu P (rechts/oben) mit – gegen den Uhrzeigersinn.')
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


def regel_n(n, r=3):
    import math
    return [(round(r * math.cos(math.radians(90 + 360 * k / n)), 2), round(r * math.sin(math.radians(90 + 360 * k / n)), 2)) for k in range(n)]


FORM = {'ein Quadrat': [(0, 0), (4, 0), (4, 4), (0, 4)], 'ein Rechteck, das kein Quadrat ist': [(0, 0), (6, 0), (6, 3), (0, 3)],
        'eine Raute, die kein Quadrat ist': [(0, 0), (3, -2), (6, 0), (3, 2)], 'ein Parallelogramm, das weder Rechteck noch Raute ist': [(0, 0), (5, 0), (7, 3), (2, 3)],
        'ein Drachenviereck, das keine Raute ist': [(0, 0), (2, -2), (6, 0), (2, 2)], 'ein gleichschenkliges Trapez, das kein Rechteck ist': [(0, 0), (6, 0), (4.5, 3), (1.5, 3)],
        'ein gleichseitiges Dreieck': regel_n(3), 'ein gleichschenkliges Dreieck, das nicht gleichseitig ist': [(0, 0), (4, 0), (2, 5)],
        'ein Dreieck mit drei verschieden langen Seiten': [(0, 0), (6, 0), (1.5, 3.5)], 'ein regelmäßiges Sechseck': regel_n(6),
        'ein regelmäßiges Fünfeck': regel_n(5), 'ein regelmäßiges Achteck': regel_n(8)}


def fig_von(name):
    pk = FORM[name]
    namen = [chr(65 + i) for i in range(len(pk))]
    return figur(dict(zip(namen, pk)), linien=[[namen[i], namen[(i + 1) % len(namen)]] for i in range(len(namen))], flaeche=namen)


def g_symmetrie(R, st):
    a = _g_symmetrie(R, st)
    for name in FORM:
        if name in a['f']['text']: a['f']['grafik'] = fig_von(name)
    return a


def gross(f):
    """Satzanfang groß; Relativsatz mit Komma schließen."""
    return f[0].upper() + f[1:]


def mit_komma(f):
    return f + ',' if ', d' in f else f


BUCHSTABEN = {'A': (1, False), 'H': (2, True), 'N': (0, True), 'S': (0, True), 'T': (1, False), 'X': (2, True), 'Z': (0, True), 'M': (1, False),
              'E': (1, False), 'U': (1, False), 'V': (1, False), 'W': (1, False), 'I': (2, True), 'K': (1, False)}


def _g_symmetrie(R, st):
    if st == 1:
        f, n, _ = R.choice(FIG)
        return Z(f'Wie viele Symmetrieachsen hat {f}?', n, f'{n}', f'{gross(mit_komma(f))} hat {n} Symmetrieachse{"n" if n != 1 else ""}.',
                 'Stell dir vor, du faltest die Figur: Wo fallen die Hälften genau aufeinander?')
    if st == 2:
        art = R.choice(['punkt', 'drehwinkel', 'buchstabe'])
        if art == 'punkt':
            f, n, p = R.choice(FIG)
            r = 'Ja' if p else 'Nein'
            ja = 'Ja, eine Drehung um 180° um den Mittelpunkt bildet die Figur auf sich ab.'
            nein = 'Nein, nach einer Drehung um 180° liegt die Figur anders.'
            return A(R, f'Ist {mit_komma(f)} punktsymmetrisch?', ja if p else nein,
                     [nein if p else ja, 'Ja, weil die Figur eine Symmetrieachse hat.', 'Ja, weil die Figur zwei gleich lange Seiten hat.'],
                     f'{gross(mit_komma(f))} ist {"" if p else "nicht "}punktsymmetrisch.', 'Drehe die Figur in Gedanken um 180°.')
        if art == 'buchstabe':
            b = R.choice(list(BUCHSTABEN)); n, _ = BUCHSTABEN[b]
            return Z(f'Wie viele Symmetrieachsen hat der Großbuchstabe {b} in Blockschrift?', n, f'{n}',
                     f'{b} hat {n} Symmetrieachse{"n" if n != 1 else ""}' + (' – senkrecht und waagrecht.' if n == 2 else '.' if n else ' (er ist aber punktsymmetrisch).' if BUCHSTABEN[b][1] else '.'),
                     'Schreibe den Buchstaben auf und prüfe: Wo kannst du falten, sodass beide Hälften aufeinanderfallen?')
        n = R.choice([3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20])
        return Z(f'Um welchen kleinsten Winkel (größer als 0°) muss man ein regelmäßiges {n}-Eck um seinen Mittelpunkt drehen, damit es auf sich selbst fällt?', Fr(360, n), f'360 / {n}',
                 f'360° : {n} = {zt(Fr(360, n))}°.', 'Ein voller Umlauf hat 360°, verteilt auf n gleiche Teile.', '°')
    if R.random() < .5:
        f, n, p = R.choice(FIG)
        andere = [g for g, m, q in FIG if (m, q) != (n, p)]
        return A(R, f'Welche Figur hat genau {n} Symmetrieachse{"n" if n != 1 else ""} und ist {"" if p else "nicht "}punktsymmetrisch?', gross(f), [gross(g) for g in R.sample(andere, 3)],
                 f'{gross(mit_komma(f))} hat {n} Symmetrieachse{"n" if n != 1 else ""} und ist {"" if p else "nicht "}punktsymmetrisch.', 'Prüfe beide Eigenschaften: Falten und um 180° drehen.')
    gesucht = R.choice(['nur_punkt', 'nur_achse', 'beides'])
    pool = {'nur_punkt': [b for b, (n, q) in BUCHSTABEN.items() if q and n == 0], 'nur_achse': [b for b, (n, q) in BUCHSTABEN.items() if not q and n > 0],
            'beides': [b for b, (n, q) in BUCHSTABEN.items() if q and n > 0]}
    r = R.choice(pool[gesucht]); f = [R.choice(pool[k]) for k in pool if k != gesucht]
    f.append(R.choice([b for b in pool[[k for k in pool if k != gesucht][0]] if b not in f] or ['O']))
    frage = {'nur_punkt': 'punktsymmetrisch, hat aber keine Symmetrieachse', 'nur_achse': 'achsensymmetrisch, aber nicht punktsymmetrisch',
             'beides': 'achsensymmetrisch und punktsymmetrisch'}[gesucht]
    return A(R, f'Welcher Großbuchstabe (Blockschrift) ist {frage}?', r, f,
             f'{r}: {BUCHSTABEN[r][0]} Symmetrieachse{"n" if BUCHSTABEN[r][0] != 1 else ""}, {"" if BUCHSTABEN[r][1] else "nicht "}punktsymmetrisch.',
             'Prüfe bei jedem Buchstaben: falten? um 180° drehen?')


IW = {3: 60, 4: 90, 5: 108, 6: 120, 8: 135, 9: 140, 10: 144, 12: 150}
ECK = {3: 'gleichseitiges Dreieck', 4: 'Quadrat', 5: 'regelmäßiges Fünfeck', 6: 'regelmäßiges Sechseck', 8: 'regelmäßiges Achteck', 9: 'regelmäßiges Neuneck',
       10: 'regelmäßiges Zehneck', 12: 'regelmäßiges Zwölfeck'}


SING = {3: 'gleichseitiges Dreieck', 4: 'Quadrat', 5: 'regelmäßiges Fünfeck', 6: 'regelmäßiges Sechseck', 8: 'regelmäßiges Achteck', 12: 'regelmäßiges Zwölfeck'}
PLUR = {3: 'gleichseitige Dreiecke', 4: 'Quadrate', 5: 'regelmäßige Fünfecke', 6: 'regelmäßige Sechsecke', 8: 'regelmäßige Achtecke', 12: 'regelmäßige Zwölfecke'}
GENI = {3: 'gleichseitiger Dreiecke', 4: 'von Quadraten', 5: 'regelmäßiger Fünfecke', 6: 'regelmäßiger Sechsecke', 8: 'regelmäßiger Achtecke', 12: 'regelmäßiger Zwölfecke'}


def g_parkett(R, st):
    if st == 1:
        n = R.choice([3, 4, 6]); k = R.choice(['wie_viele', 'summe'])
        if k == 'wie_viele':
            return Z(f'Ein {ECK[n]} hat Innenwinkel von {IW[n]}°. Wie viele davon passen lückenlos um eine Ecke?', 360 // IW[n], f'360 / {IW[n]}',
                     f'360° : {IW[n]}° = {360 // IW[n]}.', 'Um eine Ecke herum müssen die Winkel zusammen 360° ergeben.')
        m = R.choice([2, 3, 4, 5])
        return Z(f'An einer Ecke liegen {m} Ecken {GENI[n]} (je {IW[n]}°). Wie groß ist der Winkel zusammen?',
                 m * IW[n], f'{m} * {IW[n]}', f'{m} · {IW[n]}° = {m * IW[n]}°' + (' – genau 360°.' if m * IW[n] == 360 else '.'), 'Multipliziere die Anzahl mit dem Innenwinkel.', '°')
    if st == 2:
        n = R.choice([5, 8, 9, 10, 12, 3, 4, 6])
        x = R.random()
        if x < .2:
            k = R.choice([3, 4, 6])
            return Z(f'Um eine Ecke passen genau {k} gleiche regelmäßige Vielecke ohne Lücke. Wie groß ist ihr Innenwinkel?', 360 // k, f'360 / {k}',
                     f'360° : {k} = {360 // k}°. Das ist das {ECK[{3: 6, 4: 4, 6: 3}[k]]}.', 'Die Winkel an der Ecke ergeben zusammen 360°.', '°')
        if x < .4 and 360 % IW[n]:
            k = 360 // IW[n] + 1
            return Z(f'Ein {ECK[n]} hat Innenwinkel von {IW[n]}°. Jemand legt {k} davon um eine Ecke. Um wie viel Grad ist das zu viel?', k * IW[n] - 360, f'{k} * {IW[n]} - 360',
                     f'{k} · {IW[n]}° = {k * IW[n]}° – das sind {k * IW[n] - 360}° mehr als 360°. Die Vielecke würden sich überlappen.', 'Vergleiche die Summe der Winkel mit 360°.', '°')
        if x < .7 and 360 % IW[n]:
            k = 360 // IW[n]
            return Z(f'Ein {ECK[n]} hat Innenwinkel von {IW[n]}°. Man legt {k} davon um eine Ecke. Wie groß ist die Lücke, die bleibt?', 360 - k * IW[n], f'360 - {k} * {IW[n]}',
                     f'{k} · {IW[n]}° = {k * IW[n]}°. Lücke: 360° − {k * IW[n]}° = {360 - k * IW[n]}°. Ein weiteres passt nicht mehr ({(k + 1) * IW[n]}° > 360°).',
                     'Rechne aus, wie viel Winkel die Ecken zusammen belegen.', '°')
        geht = 360 % IW[n] == 0
        return A(R, f'Ein {ECK[n]} hat Innenwinkel von {IW[n]}°. Kann man mit lauter solchen Vielecken die Ebene lückenlos auslegen?',
                 ('Ja' if geht else 'Nein') + f', denn 360° : {IW[n]}° ' + ('ist eine ganze Zahl.' if geht else 'ist keine ganze Zahl.'),
                 [('Nein' if geht else 'Ja') + f', denn 360° : {IW[n]}° ' + ('ist keine ganze Zahl.' if geht else 'ist eine ganze Zahl.'), 'Ja, mit jedem regelmäßigen Vieleck geht das.',
                  'Nein, das geht nur mit Quadraten.'], f'360° : {IW[n]}° = {zt(Fr(360, IW[n]))}' + ('.' if geht else ' – keine ganze Zahl, es bleibt eine Lücke.'),
                 'An jeder Ecke müssen die Innenwinkel zusammen genau 360° ergeben.')
    # Stufe 3: verschiedene Vielecke an einer Ecke
    art = R.choice(['fehlt', 'anzahl', 'pruefen'])
    if art == 'fehlt':
        a, m = R.choice([(8, 2), (12, 2), (6, 2), (3, 3), (4, 2), (3, 4), (6, 1)])
        rest = 360 - m * IW[a]
        b = [k for k, v in IW.items() if v == rest]
        if b and R.random() < .6:
            return Z(f'An einer Ecke liegen {m} Ecken {GENI[a]} (je {IW[a]}°) und ein weiteres regelmäßiges Vieleck. Welchen Innenwinkel muss es haben?',
                     rest, f'360 - {m} * {IW[a]}', f'360° − {m} · {IW[a]}° = {rest}°. Das ist das {ECK[b[0]]}.', 'Was fehlt noch bis 360°?', '°')
        a = 6
        return Z(f'An einer Ecke liegen 2 Ecken regelmäßiger Sechsecke (je 120°). Wie viele gleichseitige Dreiecke (60°) passen noch dazu?', 2, '(360 - 2 * 120) / 60',
                 '360° − 240° = 120°; 120° : 60° = 2 Dreiecke.', 'Erst den Rest bis 360°, dann durch 60° teilen.')
    if art == 'anzahl':
        a, ma = R.choice([(6, 2), (4, 2), (4, 1), (6, 1)])
        rest = 360 - ma * IW[a]
        if rest % 60: a, ma, rest = 6, 1, 240
        return Z(f'An einer Ecke liegen {ma} Ecke{"n" if ma > 1 else ""} {GENI[a]} (je {IW[a]}°). Wie viele gleichseitige Dreiecke (60°) braucht man noch, damit die Ecke lückenlos ist?',
                 rest // 60, f'(360 - {ma} * {IW[a]}) / 60', f'360° − {ma * IW[a]}° = {rest}°; {rest}° : 60° = {rest // 60}.', 'Erst den Rest bis 360°, dann durch 60° teilen.')
    kombi = R.choice([((3, 3), (4, 2)), ((3, 2), (6, 2)), ((8, 2), (4, 1)), ((12, 2), (3, 1)), ((5, 2), (4, 1)), ((3, 4), (4, 1)), ((6, 2), (4, 1)), ((5, 3), (3, 1))])
    (a, ma), (b, mb) = kombi
    summe = ma * IW[a] + mb * IW[b]
    ok = summe == 360
    r = ('Ja' if ok else 'Nein') + f': {ma} · {IW[a]}° + {mb} · {IW[b]}° = {summe}°' + ('.' if ok else ' ≠ 360°.')
    return A(R, f'Passen {ma} {PLUR[a]} und {mb if mb > 1 else "ein"} {PLUR[b] if mb > 1 else SING[b]} lückenlos um eine Ecke?', r,
             [('Nein' if ok else 'Ja') + f': {ma} · {IW[a]}° + {mb} · {IW[b]}° = {summe}°' + (' ≠ 360°.' if ok else '.'),
              'Nein: Verschiedene Vielecke kann man an einer Ecke nie kombinieren.', 'Nein: Es müssen immer gleich viele von jeder Sorte sein.'],
             r, 'Addiere alle Winkel an der Ecke und vergleiche mit 360°.')


ABB = ['Achsenspiegelung', 'Punktspiegelung', 'Verschiebung', 'Drehung']

AUSSAGEN = [('Bei einer Drehung bleiben alle Seitenlängen gleich.', True), ('Bei einer Achsenspiegelung ändert sich der Umlaufsinn.', True),
            ('Bei einer Drehung bleibt der Umlaufsinn erhalten.', True), ('Bei einer Punktspiegelung ist nur das Zentrum ein Fixpunkt.', True),
            ('Eine Punktspiegelung ist dasselbe wie eine Drehung um 180°.', True), ('Bild und Urbild einer Kongruenzabbildung sind deckungsgleich.', True),
            ('Bei einer Achsenspiegelung bleiben die Punkte auf der Achse fest (die Achse ist eine Fixpunktgerade).', True),
            ('Zwei Achsenspiegelungen an parallelen Achsen ergeben eine Verschiebung.', True), ('Eine Verschiebung bildet jede Gerade auf eine parallele Gerade ab.', True),
            ('Bei einer Verschiebung ändert sich der Umlaufsinn.', False), ('Bei einer Drehung um 90° wird der Flächeninhalt größer.', False),
            ('Eine Verschiebung hat einen Fixpunkt.', False), ('Das Drehzentrum bewegt sich bei der Drehung mit.', False),
            ('Zwei Achsenspiegelungen ergeben wieder eine Achsenspiegelung.', False), ('Eine Achsenspiegelung verändert Winkelgrößen.', False),
            ('Bei einer Drehung kehrt sich der Umlaufsinn um.', False), ('Bei einer Punktspiegelung bleiben alle Punkte auf einer Geraden durch das Zentrum fest.', False)]

UMLAUF = [('an der y-Achse gespiegelt', True), ('an einer schräg liegenden Achse gespiegelt', True), ('um 90° um einen Punkt gedreht', False),
          ('um 180° um einen Punkt gedreht', False), ('an einem Punkt Z gespiegelt', False), ('verschoben', False), ('nacheinander an zwei verschiedenen Achsen gespiegelt', False)]

DREIECKE = [[(1, 1), (4, 1), (2, 3)], [(1, 2), (3, 1), (4, 4)], [(2, 1), (5, 2), (3, 4)], [(1, 1), (3, 1), (1, 4)]]


def _abbildung_bestimmen(R):
    D = R.choice(DREIECKE)
    art = R.choice(['y', 'x', 'punkt', 'verschiebung', 'drehung'])
    if art == 'y': B = [(-x, y) for x, y in D]; r = 'Achsenspiegelung an der y-Achse'
    elif art == 'x': B = [(x, -y) for x, y in D]; r = 'Achsenspiegelung an der x-Achse'
    elif art == 'punkt': B = [(-x, -y) for x, y in D]; r = 'Punktspiegelung an O'
    elif art == 'drehung': B = [(-y, x) for x, y in D]; r = 'Drehung um O um 90° gegen den Uhrzeigersinn'
    else:
        a, b = R.choice([(-5, 1), (-6, -2), (1, -5), (-4, -5), (2, -6)])
        B = [(x + a, y + b) for x, y in D]; r = f'Verschiebung mit v = ({zt(a)} | {zt(b)})'
    alle = ['Achsenspiegelung an der y-Achse', 'Achsenspiegelung an der x-Achse', 'Punktspiegelung an O', 'Drehung um O um 90° gegen den Uhrzeigersinn', 'Verschiebung']
    falsch = [x for x in alle if not r.startswith(x)]
    n = 'ABC'
    pk = [(x, y, n[i]) for i, (x, y) in enumerate(D)] + [(x, y, n[i] + "'") for i, (x, y) in enumerate(B)]
    st = [(D[i][0], D[i][1], D[(i + 1) % 3][0], D[(i + 1) % 3][1]) for i in range(3)] + [(B[i][0], B[i][1], B[(i + 1) % 3][0], B[(i + 1) % 3][1], 'gestrichelt') for i in range(3)]
    a = A(R, 'Das Dreieck ABC wird auf A\'B\'C\' (gestrichelt) abgebildet. Welche Abbildung ist es?', r, R.sample(falsch, 3),
          f'{r}: ' + {'y': 'x wechselt das Vorzeichen, y bleibt; der Umlaufsinn kehrt sich um.', 'x': 'y wechselt das Vorzeichen, x bleibt; der Umlaufsinn kehrt sich um.',
                     'punkt': 'beide Koordinaten wechseln das Vorzeichen; O ist die Mitte von AA\'.', 'drehung': '(x | y) → (−y | x), der Umlaufsinn bleibt.',
                     'verschiebung': 'alle Punkte wandern gleich weit in dieselbe Richtung.'}[art],
          'Vergleiche einen Punkt mit seinem Bildpunkt. Ist die Beschriftung im gleichen Umlaufsinn?')
    a['f']['grafik'] = ksys(pk, strecken=st)
    return a


def _umlauf(R):
    abb, kehrt = R.choice(UMLAUF)
    start = R.choice(['gegen den Uhrzeigersinn', 'im Uhrzeigersinn'])
    andere = 'im Uhrzeigersinn' if start == 'gegen den Uhrzeigersinn' else 'gegen den Uhrzeigersinn'
    r = andere if kehrt else start
    return A(R, f'Ein Dreieck ABC ist {start} beschriftet. Es wird {abb}. Wie ist das Bilddreieck A\'B\'C\' beschriftet?', r,
             [andere if not kehrt else start, 'Das hängt davon ab, wie groß das Dreieck ist.', 'Das Bild hat keinen Umlaufsinn mehr.'],
             f'{"Eine Achsenspiegelung kehrt den Umlaufsinn um" if kehrt else "Diese Abbildung erhält den Umlaufsinn"}' + (' (zwei Umkehrungen heben sich auf)' if 'zwei' in abb else '') + f': {r}.',
             'Nur eine einzelne Achsenspiegelung dreht die Reihenfolge der Ecken um.')


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
    if st == 3: return _abbildung_bestimmen(R)
    x = R.random()
    if st == 1 or (x < .25 and ZAEHL['aussage'] < 8):
        ZAEHL['aussage'] += 1
        wahr = [t for t, w in AUSSAGEN if w]; falsch = [t for t, w in AUSSAGEN if not w]
        t = R.choice(wahr)
        return A(R, 'Welche Aussage über Kongruenzabbildungen ist richtig?', t, R.sample(falsch, 3), f'Richtig: {t} Kongruenzabbildungen erhalten Längen, Winkel und Flächen.',
                 'Kongruent heißt deckungsgleich. Was kann sich dann überhaupt ändern?')
    return _abbildung_bestimmen(R) if x < .65 else _umlauf(R)


PUNKT = re.compile(r"([A-Z]'?)\((−?\d+) \| (−?\d+)\)")


def zahl(t): return int(t.replace('−', '-'))


def mit_koordinaten(gen):
    """Zeichnet die im Aufgabentext genannten Punkte, Achsen und den Ursprung ins Koordinatensystem (Lösung nicht)."""
    def neu(R, st):
        a = gen(R, st)
        t = a['f']['text']
        pkt = [(zahl(x), zahl(y), n) for n, x, y in PUNKT.findall(t)]
        if 'O(0 | 0)' in t and not any(n == 'O' for *_, n in pkt): pass
        senk = [zahl(m) for m in re.findall(r'Geraden x = (−?\d+)', t)]
        waag = [zahl(m) for m in re.findall(r'Geraden y = (−?\d+)', t)]
        graphen = [{'art': 'linear', 'm': 1, 't': 0, 'name': 'y = x'}] if 'y = x' in t else [{'art': 'linear', 'm': -1, 't': 0, 'name': 'y = −x'}] if 'y = −x' in t else []
        auch = []
        if a['y'] == 'luecken' and re.match(r"^[A-Z]'?\(", a['f']['schablone']): auch.append(tuple(a['o']['werte']))
        a['f']['grafik'] = ksys(pkt, senkrecht=senk, waagrecht=waag, graphen=graphen, auch=auch)
        return a
    return neu


GEN = {'achsenspiegelung': mit_koordinaten(g_achsenspiegelung), 'punktspiegelung': mit_koordinaten(g_punktspiegelung),
       'verschiebung': mit_koordinaten(g_verschiebung), 'drehung': mit_koordinaten(g_drehung),
       'symmetrie': g_symmetrie, 'parkett': g_parkett, 'eigenschaften': g_eigenschaften}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Spiegeln', ['achsenspiegelung', 'punktspiegelung']), ('Verschieben und Drehen', ['verschiebung', 'drehung']), ('Symmetrie und Eigenschaften', ['symmetrie', 'parkett', 'eigenschaften'])],
         'Achsenspiegelung, Punktspiegelung, Verschiebung und Drehung im Koordinatensystem ausführen, Symmetrien von Figuren erkennen, Parkettierungen prüfen und die Eigenschaften von Kongruenzabbildungen begründen.',
         ['Achsenspiegelung: gleich weit auf die andere Seite, senkrecht zur Achse.', 'Punktspiegelung an Z: Z ist Mitte von P und P\'.',
          'Verschiebung v = (a | b): x + a, y + b. Drehung um O um 90°: (x | y) → (−y | x).', 'Längen, Winkel und Flächen bleiben erhalten.', 'Parkett: Die Winkel an einer Ecke ergeben 360°.'],
         offen=['Aufgaben zu Spiegelung, Verschiebung und Drehung zeigen die gegebenen Punkte, Achsen und Zentren im Koordinatensystem; das Kind gibt den Bildpunkt als Koordinaten ein. '
                'Selbst zeichnen (Konstruktion mit Zirkel und Geodreieck) kann die App noch nicht – dafür bräuchte es Eingabe durch Zeichnen.',
                'Neue Lernkarte „parkett“ (aus der Prüfung): Bild einer Ecke mit sechs Dreiecken; Aufgaben rechnerisch. Ganze Parkettflächen als Bild wären möglich, sind aber nicht eingebaut.',
                'Annahme der Prüfung, nicht umgesetzt: Drehungen würden in Klasse 7 vor allem konstruierend behandelt. Die Koordinatenregeln bleiben, werden aber über das Mitdrehen des Weges (rechts/oben) begründet; Konstruieren durch das Kind kann die App nicht.',
                'lehrplan_gym ist für dieses Thema in themenliste.json leer (Hinweis der Prüfung); themenliste.json gehört nicht zu diesem Paket und bleibt unverändert.',
                'Drehungen nur um Vielfache von 90°, weil andere Winkel im Koordinatensystem ohne Trigonometrie nicht exakt berechenbar sind.'])
