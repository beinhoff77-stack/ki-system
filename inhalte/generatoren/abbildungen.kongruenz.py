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

# Verständliche Fassung (Runde 7, Maßstab inhalte/README.md „Verständliche Erklärungen“):
# Alltagssituation zuerst (einstieg), jedes neue Wort erklärt (woerter), Beispiel in kleinen Schritten, Merksatz am Ende (regel).
# Durchgehende Situation: eine Figur auf Pauspapier, die geklappt, geschoben und gedreht wird.
KLAR = {
 'achsenspiegelung': {
  'einstieg': 'Mal einen nassen Farbklecks auf ein Blatt, falte es in der Mitte und klapp es wieder auf. Der Klecks ist jetzt auch auf der anderen Seite – genau gegenüber und gleich weit vom Knick entfernt. Der Knick ist die Achse, der neue Klecks ist das Spiegelbild. Das heißt ⟦Achsenspiegelung⟧.',
  'woerter': [['Achse', 'die Gerade, an der gespiegelt wird – wie der Knick im Papier'], ['Koordinaten', 'die zwei Zahlen, die die Lage eines Punktes angeben: erst nach rechts (x), dann nach oben (y)'], ['P(4 | 3)', 'Punkt P mit x-Koordinate 4 (4 nach rechts) und y-Koordinate 3 (3 nach oben)'],
              ["P'", 'gelesen „P Strich“: der Bildpunkt, also die Stelle, an die P beim Spiegeln kommt'], ['x = 1', 'die senkrechte Gerade, auf der alle Punkte die x-Koordinate 1 haben'],
              ['senkrecht', 'im rechten Winkel (90°) zueinander'], ['Vorzeichen', 'das Plus oder Minus vor einer Zahl'], ['x-Achse / y-Achse', 'die waagrechte / die senkrechte Achse im Koordinatensystem']],
  'schritte': ['Der Punkt P(4 | 3) soll an der senkrechten Geraden x = 1 gespiegelt werden.',
               'Wie weit ist P von der Achse entfernt? Von x = 1 bis x = 4 sind es 3 Einheiten nach rechts.',
               'Der Bildpunkt liegt auf der anderen Seite, genauso weit weg: 3 Einheiten links von der Achse, also bei x = 1 − 3 = −2.',
               "Die Höhe ändert sich beim Spiegeln an einer senkrechten Achse nicht, y bleibt 3: ⟦P'(−2 | 3)⟧."],
  'regel': "So spiegelst du an einer Achse: Miss, wie weit P von der Achse weg ist, und geh auf der ⟦anderen Seite gleich weit⟧. Die Verbindung PP' steht ⟦senkrecht⟧ auf der Achse. An der x-Achse ändert sich das Vorzeichen von y, an der y-Achse das von x.",
  'fehler': "Spiegelt man P(4 | 3) an der x-Achse, ist das Bild nicht (−4 | 3). Die x-Achse liegt waagrecht wie eine Wasseroberfläche: Das Spiegelbild liegt darunter, nicht daneben. Es ändert sich die ⟦y-Koordinate⟧, also P'(4 | −3)."},
 'punktspiegelung': {
  'einstieg': 'Auf dem Schulhof steht in der Mitte ein Pfosten. Du gehst geradewegs auf ihn zu und zählst deine Schritte. Am Pfosten gehst du in derselben Richtung weiter, genauso viele Schritte. Wo du dann stehst, ist dein Bild bei der ⟦Punktspiegelung⟧ am Pfosten.',
  'woerter': [['Zentrum Z', 'der Punkt, an dem gespiegelt wird – wie der Pfosten'], ["Strecke PP'", "die gerade Verbindung von P zu seinem Bildpunkt P'"],
              ['Mittelpunkt', 'der Punkt genau in der Mitte einer Strecke']],
  'schritte': ['P(1 | 5) soll am Zentrum Z(3 | 2) gespiegelt werden.',
               'Bestimme den Weg von P nach Z: von x = 1 nach x = 3 sind es 2 nach rechts, von y = 5 nach y = 2 sind es 3 nach unten.',
               'Geh von Z aus denselben Weg noch einmal: 2 nach rechts und 3 nach unten. Also x = 3 + 2 = 5 und y = 2 − 3 = −1.',
               "Der Bildpunkt ist ⟦P'(5 | −1)⟧."],
  'regel': "So spiegelst du an einem Punkt Z: Geh von P zu Z und von dort ⟦denselben Weg noch einmal⟧ weiter. Z ist dann der ⟦Mittelpunkt⟧ der Strecke PP'.",
  'fehler': "Bei der Spiegelung an Z(3 | 2) bleibt man nicht am Pfosten stehen: P'(3 | 2) wäre Z selbst. Man geht ⟦doppelt so weit⟧ – bis Z und dann noch einmal genauso weit."},
 'verschiebung': {
  'einstieg': 'Du zeichnest eine Figur auf Pauspapier ab und schiebst das Papier über den Tisch, ohne es zu drehen: 3 Kästchen nach links und 4 nach oben. Jeder Punkt der Figur wandert dabei genau gleich weit in dieselbe Richtung. Das heißt ⟦Verschiebung⟧.',
  'woerter': [['Pauspapier', 'durchsichtiges Papier, auf dem man eine Figur abzeichnen und dann bewegen kann'], ['Bildpunkt', "wo ein Punkt nach dem Bewegen liegt, zum Beispiel A'"],
              ['Verschiebungspfeil v', 'gibt an, wie weit und wohin verschoben wird'], ['v = (−3 | 4)', '3 nach links (Minus heißt links) und 4 nach oben (Plus heißt oben)']],
  'schritte': ['A(2 | −1) soll mit dem Pfeil v = (−3 | 4) verschoben werden.',
               'Die erste Zahl des Pfeils gehört zur x-Koordinate: 2 + (−3) = −1. Das heißt 3 nach links.',
               'Die zweite Zahl gehört zur y-Koordinate: −1 + 4 = 3. Das heißt 4 nach oben.',
               "Der Bildpunkt ist ⟦A'(−1 | 3)⟧."],
  'regel': 'So verschiebst du mit v = (a | b): Zähle a zur ⟦x-Koordinate⟧ und b zur ⟦y-Koordinate⟧ dazu. Negative Zahlen bedeuten links bzw. unten. Jeder Punkt der Figur wandert gleich weit.',
  'fehler': 'Bei v = (−3 | 4) zählt man −3 zur ⟦x⟧- und 4 zur ⟦y⟧-Koordinate – nicht umgekehrt. Sonst würde man das Pauspapier 4 nach links und 3 nach oben schieben, also an eine ganz andere Stelle.'},
 'drehung': {
  'einstieg': 'Steck eine Reißzwecke durch das Pauspapier und dreh das Papier um sie herum. Jeder Punkt der Figur bewegt sich dabei auf einem Kreis um die Reißzwecke und bleibt gleich weit von ihr entfernt. Das heißt ⟦Drehung⟧.',
  'woerter': [['Drehzentrum', 'der Punkt, um den gedreht wird – die Reißzwecke'], ['Ursprung O', 'der Punkt (0 | 0), an dem sich die beiden Achsen kreuzen'],
              ['90°', 'eine Vierteldrehung'], ['180°', 'eine halbe Drehung'], ['gegen den Uhrzeigersinn', 'andersherum, als sich die Zeiger einer Uhr drehen'],
              ['(x | y) → (−y | x)', 'Kurzschreibweise für die Regel: aus (4 | 1) wird (−1 | 4)']],
  'schritte': ['P(4 | 1) soll um den Ursprung O um 90° gegen den Uhrzeigersinn gedreht werden.',
               'Beschreibe den Weg von O zu P: 4 nach rechts, dann 1 nach oben.',
               'Dreh diesen Weg eine Vierteldrehung nach links mit: Aus „4 nach rechts“ wird „4 nach oben“, aus „1 nach oben“ wird „1 nach links“.',
               "Der neue Weg von O geht 1 nach links und 4 nach oben. Der Bildpunkt ist ⟦P'(−1 | 4)⟧."],
  'regel': 'So drehst du um O um 90° gegen den Uhrzeigersinn: Beschreibe den Weg von O zu P und dreh ihn eine Vierteldrehung mit. Als Regel: ⟦(x | y) → (−y | x)⟧. Um 180°: (x | y) → (−x | −y). Der ⟦Abstand zum Drehzentrum⟧ bleibt immer gleich.',
  'fehler': 'Bei 90° ändert man nicht bloß beide Vorzeichen: (4 | 1) → (−4 | −1) wäre eine ⟦halbe Drehung (180°)⟧ – als hätte man das Pauspapier ganz auf den Kopf gestellt statt nur eine Vierteldrehung gemacht.'},
 'symmetrie': {
  'einstieg': 'Viele Dinge sehen auf beiden Seiten gleich aus: ein Schmetterling, ein Fenster, ein Herz. Stellst du einen Spiegel genau in die Mitte, ergänzt er die eine Hälfte zur ganzen Figur. Eine Figur, die so aus zwei Spiegelhälften besteht, heißt ⟦achsensymmetrisch⟧.',
  'woerter': [['Symmetrieachse', 'Gerade, an der man die Figur falten kann, sodass beide Hälften genau aufeinanderliegen'], ['achsensymmetrisch', 'hat mindestens eine Symmetrieachse'],
              ['punktsymmetrisch', 'sieht nach einer halben Drehung (180°) um ihren Mittelpunkt genauso aus wie vorher'],
              ['regelmäßiges n-Eck', 'Vieleck mit n Ecken, bei dem alle Seiten und alle Winkel gleich groß sind'], ['Diagonale', 'Verbindungsstrecke zweier gegenüberliegender Ecken']],
  'schritte': ['Untersucht wird ein Rechteck, das kein Quadrat ist.',
               'Falte es in Gedanken senkrecht durch die Mitte: Die Hälften passen genau aufeinander. Waagrecht durch die Mitte geht es auch.',
               'Das sind ⟦2 Symmetrieachsen⟧. Beide gehen durch die Mitten gegenüberliegender Seiten.',
               'Dreh das Rechteck um seinen Mittelpunkt eine halbe Drehung: Es liegt wieder genau auf seinem alten Platz. Es ist also auch ⟦punktsymmetrisch⟧.'],
  'regel': 'So prüfst du Symmetrie: ⟦Achsensymmetrisch⟧ ist eine Figur, wenn du sie so falten kannst, dass beide Hälften aufeinanderfallen. ⟦Punktsymmetrisch⟧ ist sie, wenn sie nach einer halben Drehung (180°) genauso daliegt. Ein regelmäßiges n-Eck hat ⟦n Symmetrieachsen⟧.',
  'fehler': 'Die Diagonalen eines Rechtecks sind ⟦keine⟧ Symmetrieachsen (außer beim Quadrat). Faltet man ein rechteckiges Blatt entlang der Diagonale, stehen Zipfel über – die Ecken fallen nicht aufeinander.',
  'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [6, 0], 'C': [6, 3], 'D': [0, 3], '_1': [3, -0.7], '_2': [3, 3.7], '_3': [-0.7, 1.5], '_4': [6.7, 1.5]}, 'flaeche': ['A', 'B', 'C', 'D'],
           'linien': [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A'], ['_1', '_2', 'Symmetrieachse', 'gestrichelt'], ['_3', '_4', 'Symmetrieachse', 'gestrichelt']]}},
 'parkett': {
  'einstieg': 'Im Badezimmer liegen Fliesen dicht an dicht, ohne Lücke und ohne dass sich zwei überlappen. Mit quadratischen Fliesen geht das, mit sechseckigen auch – wie bei Bienenwaben. Mit fünfeckigen Fliesen klappt es nicht. Eine Fläche so lückenlos mit gleichen Vielecken auszulegen heißt ⟦Parkett⟧.',
  'woerter': [['Parkett', 'lückenlose Auslegung einer Fläche ohne Überlappung'], ['Innenwinkel', 'der Winkel innen an einer Ecke des Vielecks'],
              ['360°', 'eine volle Umdrehung – so viel Platz ist rund um eine Ecke'], ['gleichseitiges Dreieck', 'Dreieck mit drei gleich langen Seiten; jeder seiner Winkel ist 60°']],
  'schritte': ['An jeder Ecke des Parketts stoßen mehrere Fliesen zusammen. Ihre Winkel müssen zusammen genau 360° ergeben, sonst bleibt eine Lücke oder es wird zu eng.',
               'Gleichseitiges Dreieck: Innenwinkel 60°. 360° : 60° = 6, also passen genau sechs Dreiecke um eine Ecke. ✓',
               'Quadrat: 360° : 90° = 4 ✓. Regelmäßiges Sechseck: 360° : 120° = 3 ✓ – wie bei Bienenwaben.',
               'Regelmäßiges Fünfeck: Innenwinkel 108°. 360° : 108° = 3,33…, das geht nicht glatt auf: ⟦kein Parkett⟧.'],
  'regel': 'So prüfst du, ob gleiche regelmäßige Vielecke ein ⟦Parkett⟧ ergeben: Teile 360° durch den ⟦Innenwinkel⟧. Kommt eine ganze Zahl heraus, passen die Ecken lückenlos zusammen.',
  'fehler': '„Jedes regelmäßige Vieleck ergibt ein Parkett.“ Falsch: Von fünfeckigen Fliesen passen drei an eine Ecke (324°), und es bleibt ein Spalt von 36°; vier wären 432°, sie würden sich überlappen. Nur bei ⟦Dreieck, Quadrat und Sechseck⟧ geht 360° glatt auf.'},
 'eigenschaften': {
  'einstieg': 'Ob du das Pauspapier umklappst, verschiebst oder drehst – die abgezeichnete Figur bleibt dieselbe: gleich groß, gleiche Seiten, gleiche Winkel. Nur ihre Lage ändert sich. Bewegungen, bei denen die Figur so deckungsgleich bleibt, heißen ⟦Kongruenzabbildungen⟧.',
  'woerter': [['kongruent / deckungsgleich', 'passt genau aufeinander, wenn man es übereinanderlegt'], ['Urbild / Bild', 'die Figur vorher / nachher'],
              ['Umlaufsinn', 'die Reihenfolge der Ecken A → B → C: im oder gegen den Uhrzeigersinn'], ['parallel', 'überall gleich weit voneinander entfernt, wie Schienen']],
  'schritte': ['Eine Figur wird erst an einer Achse gespiegelt und dann an einer zweiten Achse, die parallel dazu im Abstand 3 cm liegt.',
               'Bei jeder Spiegelung kehrt sich der Umlaufsinn um. Nach zwei Spiegelungen ist er wieder wie am Anfang.',
               'Die Figur ist danach nicht gedreht, sondern nur zur Seite gerückt: Es ist eine Verschiebung.',
               'Sie ist um den doppelten Abstand verschoben, senkrecht zu den Achsen: ⟦2 · 3 cm = 6 cm⟧.'],
  'regel': 'So erkennst du ⟦Kongruenzabbildungen⟧: Sie erhalten ⟦Längen, Winkel und Flächeninhalte⟧. Nur die Achsenspiegelung kehrt den ⟦Umlaufsinn⟧ um. Zwei Spiegelungen nacheinander ergeben eine Verschiebung (parallele Achsen) oder eine Drehung (sich schneidende Achsen).',
  'fehler': 'Eine Drehung macht die Figur nicht größer oder kleiner. Das Pauspapier wird nur gedreht, nicht gedehnt – Seitenlängen und Winkel ⟦bleiben gleich⟧.'},
}
for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl7.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl7 import mit_umbau  # noqa: E402


def _pt(x, y, n): return {'x': x, 'y': y, 'name': n}


def _rechteck(achsen=(), diagonale=False):
    pk = {'A': [0, 0], 'B': [6, 0], 'C': [6, 3], 'D': [0, 3], '_1': [3, -0.7], '_2': [3, 3.7], '_3': [-0.7, 1.5], '_4': [6.7, 1.5]}
    li = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A']]
    if 's' in achsen: li.append(['_1', '_2', 'Achse', 'gestrichelt'])
    if 'w' in achsen: li.append(['_3', '_4', 'Achse', 'gestrichelt'])
    if diagonale: li.append(['A', 'C', 'keine Achse', 'gestrichelt'])
    return {'typ': 'figur', 'punkte': pk, 'flaeche': ['A', 'B', 'C', 'D'], 'linien': li}


def _dreiecke(k):
    """k gleichseitige Dreiecke um die Ecke O (Ausschnitt eines Dreiecksparketts)."""
    ecken = [[3.0, 0.0], [1.5, 2.6], [-1.5, 2.6], [-3.0, 0.0], [-1.5, -2.6], [1.5, -2.6]]
    pk = {'O': [0, 0]}
    li = []
    for i in range(k):
        a, b = f'_h{i}', f'_h{(i + 1) % 6}'
        pk[a] = ecken[i]; pk[b] = ecken[(i + 1) % 6]
        li += [['O', a], [a, b], ['O', b]]
    return {'typ': 'figur', 'punkte': pk, 'linien': li, 'winkel': [['O', '_h0', '_h1', '60°']]}


_D0 = [(1, 1), (2, 1), (1, 3)]
_D1 = [(6 - x, y) for x, y in _D0]
_D2 = [(12 - x, y) for x, y in _D1]


def _dreieck(P, stil=None):
    return [[P[i][0], P[i][1], P[(i + 1) % 3][0], P[(i + 1) % 3][1]] + ([stil] if stil else []) for i in range(3)]


UMBAU = {
 'achsenspiegelung': {
  'einstieg': 'Mal einen nassen Farbklecks auf ein Blatt, falte es und klapp es wieder auf. Der Klecks ist jetzt auch gegenüber, gleich weit vom Knick. Das heißt ⟦Achsenspiegelung⟧.',
  'woerter': [['Achse', 'die Gerade, an der gespiegelt wird – wie der Knick'], ['P(4 | 3)', 'Punkt mit x = 4 (nach rechts) und y = 3 (nach oben)'],
              ["P'", 'gelesen „P Strich“: der Bildpunkt von P']],
  'bild': {'typ': 'koordinaten', 'x': [-3, 5], 'y': [-1, 4], 'senkrecht': [1], 'punkte': [_pt(4, 3, 'P')]},
  'schritte': [{'text': 'P(4 | 3) wird an der Achse x = 1 gespiegelt.'},
               {'text': 'P liegt 3 Kästchen rechts von der Achse.', 'bild': {'strecken': [[1, 3, 4, 3, 'gestrichelt']]}},
               {'text': "Auf der anderen Seite 3 Kästchen nach links: ⟦P'(−2 | 3)⟧.",
                'bild': {'punkte': [_pt(4, 3, 'P'), _pt(-2, 3, "P'")], 'strecken': [[-2, 3, 4, 3, 'gestrichelt']]}}],
  'fehler': 'An der x-Achse ist das Bild von P(4 | 3) nicht (−4 | 3). Die x-Achse liegt waagrecht wie eine Wasseroberfläche. Das Bild liegt darunter: ⟦(4 | −3)⟧.',
  'fehler_bild': {'y': [-4, 4], 'senkrecht': [], 'punkte': [_pt(4, 3, 'P'), _pt(4, -3, "P'")], 'strecken': [[4, 3, 4, -3, 'gestrichelt']]},
  'regel': "Spiegeln heißt: ⟦gleich weit⟧ auf die andere Seite der Achse. Die Strecke PP' steht senkrecht auf der Achse."},
 'punktspiegelung': {
  'einstieg': 'Du gehst geradeaus auf einen Pfosten zu und zählst deine Schritte. Am Pfosten gehst du genauso viele Schritte weiter. Dort steht dein Bild bei der ⟦Punktspiegelung⟧.',
  'woerter': [['Zentrum Z', 'der Punkt, an dem gespiegelt wird – der Pfosten'], ['Mittelpunkt', 'der Punkt genau in der Mitte einer Strecke']],
  'bild': {'typ': 'koordinaten', 'x': [-1, 6], 'y': [-2, 6], 'punkte': [_pt(1, 5, 'P'), _pt(3, 2, 'Z')]},
  'schritte': [{'text': 'P(1 | 5) wird am Zentrum Z(3 | 2) gespiegelt.'},
               {'text': 'Von P nach Z sind es 2 nach rechts und 3 nach unten.', 'bild': {'strecken': [[1, 5, 3, 2, 'gestrichelt']]}},
               {'text': "Von Z aus denselben Weg noch einmal: ⟦P'(5 | −1)⟧.",
                'bild': {'punkte': [_pt(1, 5, 'P'), _pt(3, 2, 'Z'), _pt(5, -1, "P'")], 'strecken': [[1, 5, 5, -1, 'gestrichelt']]}},
               {'text': "Z ist jetzt der Mittelpunkt der Strecke von P nach P'."}],
  'fehler': "Nicht am Pfosten stehen bleiben: P'(3 | 2) wäre Z selbst. Man geht von P aus ⟦doppelt so weit⟧ wie bis Z.",
  'regel': "Geh von P zu Z und ⟦denselben Weg weiter⟧. Z ist dann die Mitte von PP'."},
 'verschiebung': {
  'einstieg': 'Du schiebst ein Pauspapier 3 Kästchen nach links und 4 nach oben. Gedreht wird es nicht. Jeder Punkt wandert gleich weit. Das heißt ⟦Verschiebung⟧.',
  'woerter': [['Pauspapier', 'durchsichtiges Papier zum Abzeichnen'], ['v = (−3 | 4)', 'der Verschiebungspfeil: 3 nach links, 4 nach oben']],
  'bild': {'typ': 'koordinaten', 'x': [-2, 3], 'y': [-2, 4], 'punkte': [_pt(2, -1, 'A')]},
  'schritte': [{'text': 'A(2 | −1) wird mit v = (−3 | 4) verschoben.'},
               {'text': 'Erste Zahl zu x: 2 + (−3) = −1. Das sind 3 nach links.', 'bild': {'strecken': [[2, -1, -1, -1, 'gestrichelt']]}},
               {'text': "Zweite Zahl zu y: −1 + 4 = 3. Ergebnis: ⟦A'(−1 | 3)⟧.",
                'bild': {'punkte': [_pt(2, -1, 'A'), _pt(-1, 3, "A'")], 'strecken': [[2, -1, -1, -1, 'gestrichelt'], [-1, -1, -1, 3, 'gestrichelt']], 'pfeile': [[2, -1, -1, 3, 'v']]}}],
  'fehler': 'Die Zahlen nicht vertauschen: −3 gehört zu x, 4 zu y. Vertauscht landet das Papier ganz woanders, bei ⟦(6 | −4)⟧.',
  'regel': 'Verschieben: erste Zahl zu ⟦x⟧, zweite Zahl zu ⟦y⟧. Minus heißt links bzw. unten.'},
 'drehung': {
  'einstieg': 'Steck eine Reißzwecke durch das Pauspapier und dreh es. Jeder Punkt läuft auf einem Kreis und bleibt gleich weit von der Zwecke. Das ist eine ⟦Drehung⟧.',
  'woerter': [['Ursprung O', 'der Punkt (0 | 0) – hier sitzt die Reißzwecke'], ['90°', 'eine Vierteldrehung'], ['gegen den Uhrzeigersinn', 'andersherum als die Uhrzeiger']],
  'bild': {'typ': 'koordinaten', 'x': [-2, 5], 'y': [-1, 5], 'punkte': [_pt(4, 1, 'P'), _pt(0, 0, 'O')]},
  'schritte': [{'text': 'P(4 | 1) wird um O um 90° gegen den Uhrzeigersinn gedreht.'},
               {'text': 'Weg vom Ursprung O zu P: 4 nach rechts, 1 nach oben.', 'bild': {'strecken': [[0, 0, 4, 0, 'gestrichelt'], [4, 0, 4, 1, 'gestrichelt']]}},
               {'text': 'Den Weg mitdrehen: 4 nach oben, dann 1 nach links.', 'bild': {'strecken': [[0, 0, 0, 4, 'gestrichelt'], [0, 4, -1, 4, 'gestrichelt']]}},
               {'text': "Der Bildpunkt ist ⟦P'(−1 | 4)⟧.", 'bild': {'punkte': [_pt(4, 1, 'P'), _pt(0, 0, 'O'), _pt(-1, 4, "P'")]}}],
  'fehler': 'Bei 90° nicht nur die Vorzeichen ändern. (−4 | −1) wäre eine ⟦halbe Drehung⟧, also 180°.',
  'fehler_bild': {'x': [-5, 5], 'y': [-2, 5], 'punkte': [_pt(4, 1, 'P'), _pt(0, 0, 'O'), _pt(-4, -1, '180°')],
                  'strecken': [[0, 0, 4, 1, 'gestrichelt'], [0, 0, -4, -1, 'gestrichelt']]},
  'regel': '90° links herum: aus ⟦(x | y) wird (−y | x)⟧. Der Abstand zu O bleibt gleich.'},
 'symmetrie': {
  'einstieg': 'Ein Schmetterling, ein Fenster, ein Herz: Beide Hälften sehen gleich aus. Faltet man in der Mitte, liegen sie genau aufeinander. Solche Figuren heißen ⟦achsensymmetrisch⟧.',
  'woerter': [['Symmetrieachse', 'Faltlinie, an der beide Hälften aufeinanderfallen'], ['punktsymmetrisch', 'sieht nach einer halben Drehung genauso aus']],
  'bild': _rechteck(),
  'schritte': [{'text': 'Untersucht wird ein Rechteck, das kein Quadrat ist.'},
               {'text': 'Senkrecht falten: Die Hälften passen. Das ist eine Symmetrieachse.', 'bild': _rechteck('s')},
               {'text': 'Waagrecht geht es auch. Es hat ⟦2 Symmetrieachsen⟧.', 'bild': _rechteck('sw')},
               {'text': 'Nach einer halben Drehung liegt es wieder gleich: ⟦punktsymmetrisch⟧.'}],
  'fehler': 'Die Diagonale ist keine Symmetrieachse. Faltet man ein rechteckiges Blatt diagonal, stehen ⟦Zipfel über⟧.',
  'fehler_bild': _rechteck(diagonale=True),
  'regel': 'Symmetrisch heißt: ⟦Falten⟧ oder halbe Drehung, und alles passt. Ein Quadrat hat 4 Achsen, ein Rechteck 2.'},
 'parkett': {
  'einstieg': 'Im Bad liegen Fliesen dicht an dicht, ohne Lücke. Mit Quadraten geht das, mit Sechsecken auch, mit Fünfecken nicht. So eine lückenlose Auslegung heißt ⟦Parkett⟧.',
  'woerter': [['Innenwinkel', 'der Winkel innen an einer Ecke'], ['360°', 'eine volle Umdrehung um eine Ecke']],
  'bild': _dreiecke(1),
  'schritte': [{'text': 'Ein gleichseitiges Dreieck hat an jeder Ecke einen Innenwinkel von 60°.'},
               {'text': 'Um eine Ecke ist Platz für 360°. 360° : 60° = 6.', 'bild': _dreiecke(6)},
               {'text': 'Sechs Dreiecke passen genau: ⟦ein Parkett⟧.'},
               {'text': 'Fünfeck: 360° : 108° = 3,33…, es bleibt eine ⟦Lücke⟧.'}],
  'fehler': 'Nicht jedes regelmäßige Vieleck passt. Drei Fünfecke sind 324°, es bleibt ein Spalt von 36°. Vier wären mit 432° zu viel.',
  'regel': '360° muss durch den ⟦Innenwinkel⟧ teilbar sein. Nur dann passen die Fliesen lückenlos.'},
 'eigenschaften': {
  'einstieg': 'Du klappst das Pauspapier um, schiebst oder drehst es. Die Figur bleibt gleich groß, mit gleichen Seiten und Winkeln. Solche Bewegungen heißen ⟦Kongruenzabbildungen⟧.',
  'woerter': [['kongruent', 'deckungsgleich: passt genau aufeinander'], ['parallel', 'überall gleich weit auseinander, wie Schienen'],
              ['Umlaufsinn', 'Reihenfolge der Ecken: im oder gegen den Uhrzeigersinn']],
  'bild': {'typ': 'koordinaten', 'x': [0, 9], 'y': [0, 4], 'senkrecht': [3, 6], 'strecken': _dreieck(_D0)},
  'schritte': [{'text': 'Das Dreieck wird an zwei parallelen Achsen gespiegelt, 3 Kästchen auseinander.'},
               {'text': 'Nach der ersten Spiegelung ist der Umlaufsinn umgekehrt.', 'bild': {'strecken': _dreieck(_D0) + _dreieck(_D1, 'gestrichelt')}},
               {'text': 'Nach der zweiten stimmt er wieder. Das Bild ist kongruent zum Original.',
                'bild': {'strecken': _dreieck(_D0) + _dreieck(_D1, 'gestrichelt') + _dreieck(_D2)}},
               {'text': 'Es ist nur verschoben, um ⟦2 · 3 = 6⟧ Kästchen.'}],
  'fehler': 'Eine Drehung macht die Figur nicht größer. Das Pauspapier wird gedreht, nicht gedehnt: Längen und Winkel ⟦bleiben gleich⟧.',
  'regel': 'Kongruenzabbildungen erhalten ⟦Längen und Winkel⟧. Nur das Achsenspiegeln dreht den Umlaufsinn um.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---------- Zehnte Runde (schwer-kl7): schwerere Übungen nach Prüfungsvorbild ----------
# Vorbilder (nur Typ und Niveau, eigene Zahlen und Einkleidung): Bayerischer Mathematik-Test 8 (ISB) 2023 A3 (Symmetrieachsen der Raute,
# Gegenbeispiel), 2025 A7 (Parallelogramm im Koordinatensystem); Jahrgangsstufentests Realschule 8 (ISB): 2014 I (kleinster Drehwinkel),
# 2019 I (Gerade bei Drehung um 180°), 2019 II (Drehwinkel eines Schildes), 2025 II Nr. 4, 7, 8 (Verschiebungspfeil, Mittelpunkt);
# ISB-Leistungsaufgaben Realschule 8 I (Drehwinkel in einem Bereich); Vergleichsarbeit Jgst. 8 (Innenwinkel im n-Eck, nach Uni Bayreuth SMART);
# Känguru der Mathematik 2023, Klassenstufen 7/8 (Parkett, als Knobelvorbild). Eigener Zufallsstart, alte Aufgaben bleiben gleich.
from _schwer_kl7 import Neu, anhaengen  # noqa: E402


def schwer():
    N = Neu(7046)
    P = 'pruefung'
    K = 'knobel'
    HP = 'Trage die x- und die y-Koordinate ein.'
    HV = 'Trage ein, wie weit nach rechts (x) und nach oben (y) verschoben wird.'
    # achsenspiegelung
    N.L('achsenspiegelung', 2, 'Spiegle P(3 | −2) an der Geraden x = −1 (senkrecht zur x-Achse).', "P'(□ | □)", [-5, -2], ['-1 - (3 - (-1))', '-2'],
        'P ist 4 rechts von der Achse x = −1. P\' liegt 4 links davon: x = −5. y bleibt −2.', 'Wie weit ist P von der Achse entfernt? Genauso weit auf die andere Seite.', HP,
        grafik=ksys([(3, -2, 'P')], senkrecht=[-1]))
    N.L('achsenspiegelung', 2, 'Spiegle P(0 | 5) an der Winkelhalbierenden y = x.', "P'(□ | □)", [5, 0], ['5', '0'],
        'Bei der Spiegelung an y = x tauschen x und y die Plätze: P\'(5 | 0).', 'An y = x werden die Koordinaten vertauscht.', HP,
        grafik=ksys([(0, 5, 'P')], graphen=[{'art': 'linear', 'm': 1, 't': 0, 'name': 'y = x'}]))
    N.L('achsenspiegelung', 3, 'Die Raute ABCD mit A(−3 | 1), B(1 | −1), C(5 | 1) und D(1 | 3) ist achsensymmetrisch. Eine Symmetrieachse ist parallel zur y-Achse. Gib sie an.', 'x = □', [1], ['(-3 + 5) // 2'],
        'Die Achse halbiert die Diagonale [AC]: Mitte von −3 und 5 ist 1. Sie geht durch B und D (beide x = 1). Achse: x = 1.',
        'Eine Symmetrieachse der Raute ist eine Diagonale. Welche Diagonale ist senkrecht?', 'Trage die Zahl ein.', art=P,
        grafik=ksys([(-3, 1, 'A'), (1, -1, 'B'), (5, 1, 'C'), (1, 3, 'D')], strecken=[(-3, 1, 1, -1), (1, -1, 5, 1), (5, 1, 1, 3), (1, 3, -3, 1)]))
    N.L('achsenspiegelung', 3, 'Bei einer Achsenspiegelung wird A(−2 | 3) auf A\'(4 | 3) abgebildet. Wohin wird B(−1 | 0) bei derselben Spiegelung abgebildet?', "B'(□ | □)", [3, 0], ['1 + (1 - (-1))', '0'],
        'Die Achse ist die Mittelsenkrechte von [AA\']: x = (−2 + 4) : 2 = 1. B ist 2 links von x = 1, B\' liegt 2 rechts: B\'(3 | 0).',
        'Bestimme zuerst die Achse: Sie liegt genau in der Mitte zwischen A und A\'.', HP, art=P, grafik=ksys([(-2, 3, 'A'), (4, 3, "A'"), (-1, 0, 'B')]))
    N.A('achsenspiegelung', 3, 'P(4 | −3) wird erst an der x-Achse und danach an der y-Achse gespiegelt. Welche einzelne Abbildung hat dieselbe Wirkung?', 'Punktspiegelung am Ursprung O',
        ['Achsenspiegelung an der Geraden y = x', 'Verschiebung mit v = (−8 | 6)', 'Drehung um O um 90°'],
        'x-Achse: (4 | −3) → (4 | 3). y-Achse: → (−4 | 3). Beide Vorzeichen sind umgedreht: Das ist die Punktspiegelung an O (Drehung um 180°) – für jeden Punkt.',
        'Verfolge den Punkt durch beide Spiegelungen. Was passiert mit den Vorzeichen?', art=K)
    N.Z('achsenspiegelung', 3, 'Ein Punkt P(x | 2) wird an der Geraden x = 4 gespiegelt und landet bei P\'(−1 | 2). Wie groß ist x?', 9, '4 + (4 - (-1))',
        'P\' liegt 5 links von der Achse (−1 bis 4). P liegt 5 rechts davon: x = 9.', 'Rückwärts denken: Wie weit ist P\' von der Achse entfernt?')
    # punktspiegelung
    N.L('punktspiegelung', 2, 'Spiegle P(3 | −5) am Punkt Z(0 | −2).', "P'(□ | □)", [-3, 1], ['2 * 0 - 3', '2 * (-2) - (-5)'],
        'Von P nach Z: 3 nach links, 3 nach oben. Denselben Weg weiter: P\'(−3 | 1).', 'Geh von P zu Z und dann denselben Weg noch einmal.', HP,
        grafik=ksys([(3, -5, 'P'), (0, -2, 'Z')]))
    N.L('punktspiegelung', 2, 'Spiegle P(−1 | 4) am Punkt Z(2 | 2).', "P'(□ | □)", [5, 0], ['2 * 2 - (-1)', '2 * 2 - 4'],
        'Von P nach Z: 3 nach rechts, 2 nach unten. Denselben Weg weiter: P\'(5 | 0).', 'Geh von P zu Z und dann denselben Weg noch einmal.', HP,
        grafik=ksys([(-1, 4, 'P'), (2, 2, 'Z')]))
    N.L('punktspiegelung', 3, 'Bei einer Punktspiegelung wird P(−3 | 5) auf Q(7 | −1) abgebildet. Gib das Zentrum Z an.', 'Z(□ | □)', [2, 2], ['(-3 + 7) // 2', '(5 + (-1)) // 2'],
        'Z ist der Mittelpunkt von [PQ]: x = (−3 + 7) : 2 = 2, y = (5 + (−1)) : 2 = 2. Z(2 | 2).', 'Das Zentrum liegt genau in der Mitte zwischen Punkt und Bildpunkt.', HP, art=P,
        grafik=ksys([(-3, 5, 'P'), (7, -1, 'Q')]))
    N.L('punktspiegelung', 3, 'Das Parallelogramm ABCD hat die Ecken A(−2 | −1), B(4 | −1) und C(6 | 3). Ein Parallelogramm ist punktsymmetrisch. Gib die vierte Ecke D an.', 'D(□ | □)', [0, 3],
        ['-2 + 6 - 4', '-1 + 3 - (-1)'],
        'Von B nach C geht es 2 nach rechts und 4 nach oben. Von A aus denselben Weg: D(0 | 3). Probe: Die Diagonalen [AC] und [BD] haben dieselbe Mitte (2 | 1).',
        '[AD] ist parallel und gleich lang wie [BC].', HP, art=P, grafik=ksys([(-2, -1, 'A'), (4, -1, 'B'), (6, 3, 'C')], strecken=[(-2, -1, 4, -1), (4, -1, 6, 3)]))
    N.L('punktspiegelung', 3, 'Das Parallelogramm ABCD hat die Ecken A(−2 | −1), B(4 | −1), C(6 | 3) und D(0 | 3). Gib sein Symmetriezentrum Z an.', 'Z(□ | □)', [2, 1],
        ['(-2 + 6) // 2', '(-1 + 3) // 2'],
        'Z ist der Schnittpunkt der Diagonalen, also die Mitte von [AC]: ((−2 + 6) : 2 | (−1 + 3) : 2) = (2 | 1).', 'Das Zentrum halbiert beide Diagonalen.', HP, art=P,
        grafik=ksys([(-2, -1, 'A'), (4, -1, 'B'), (6, 3, 'C'), (0, 3, 'D')], strecken=[(-2, -1, 4, -1), (4, -1, 6, 3), (6, 3, 0, 3), (0, 3, -2, -1)]))
    N.L('punktspiegelung', 3, 'Ein Punkt wird erst am Ursprung O(0 | 0) und danach am Punkt Z(3 | 1) gespiegelt. Welcher Verschiebungspfeil ersetzt beide Spiegelungen (für jeden Punkt)?', 'v = (□ | □)', [6, 2],
        ['2 * 3', '2 * 1'],
        'Beispiel P(1 | 2): an O → (−1 | −2), an Z → (7 | 4). Verschiebung von P nach P\'\': (6 | 2). Allgemein: doppelter Weg von O nach Z.',
        'Probiere es mit einem Punkt aus und vergleiche Anfang und Ende.', HV, art=K)
    # verschiebung
    N.L('verschiebung', 2, 'Das Dreieck A(1 | 1), B(4 | 1), C(2 | 3) wird mit v = (−3 | 2) verschoben. Wo liegt C\'?', "C'(□ | □)", [-1, 5], ['2 + (-3)', '3 + 2'],
        'C(2 | 3) + (−3 | 2) = C\'(−1 | 5).', 'Zur x-Koordinate −3, zur y-Koordinate +2.', HP)
    N.L('verschiebung', 2, 'Eine Verschiebung bildet A(2 | −3) auf A\'(−1 | 1) ab. Wohin wird B(5 | 0) abgebildet?', "B'(□ | □)", [2, 4], ['5 + (-1 - 2)', '0 + (1 - (-3))'],
        'Pfeil: v = (−1 − 2 | 1 − (−3)) = (−3 | 4). B\' = (5 − 3 | 0 + 4) = (2 | 4).', 'Bestimme zuerst den Pfeil aus A und A\'.', HP)
    N.A('verschiebung', 3, 'Der Verschiebungspfeil v führt von A(1 | 1) nach A\'(4 | 3). Welcher Pfeil gehört NICHT zu derselben Verschiebung?', 'von (4 | 3) nach (1 | 1)',
        ['von (0 | 0) nach (3 | 2)', 'von (2 | 5) nach (5 | 7)', 'von (−1 | −2) nach (2 | 0)'],
        'v = (3 | 2). Die Pfeile (0 | 0)→(3 | 2), (2 | 5)→(5 | 7), (−1 | −2)→(2 | 0) haben alle (3 | 2). Der Pfeil (4 | 3)→(1 | 1) ist (−3 | −2): gleich lang, aber entgegengesetzt.',
        'Berechne bei jedem Pfeil „Ende minus Anfang“. Auch die Richtung muss stimmen.', art=P)
    N.L('verschiebung', 3, 'Der Verschiebungspfeil v führt von P(−2 | 1) nach P\'(1 | −1). Ein anderer Pfeil derselben Verschiebung beginnt bei Q(3 | 4). Wo endet er?', "Q'(□ | □)", [6, 2],
        ['3 + (1 - (-2))', '4 + (-1 - 1)'],
        'v = (1 − (−2) | −1 − 1) = (3 | −2). Q\' = (3 + 3 | 4 − 2) = (6 | 2).', 'Alle Pfeile einer Verschiebung sind gleich lang, parallel und gleich gerichtet.', HP, art=P,
        grafik=ksys([(-2, 1, 'P'), (1, -1, "P'"), (3, 4, 'Q')], strecken=[(-2, 1, 1, -1)]))
    N.L('verschiebung', 3, 'P(1 | 1) wird erst mit einem unbekannten Pfeil v und danach mit (2 | −5) verschoben. Am Ende liegt P bei (0 | 0). Wie heißt v?', 'v = (□ | □)', [-3, 4],
        ['0 - 1 - 2', '0 - 1 - (-5)'],
        'Insgesamt: von (1 | 1) nach (0 | 0), also (−1 | −1). Davon kommt (2 | −5) vom zweiten Pfeil. v = (−1 − 2 | −1 + 5) = (−3 | 4).',
        'Rechne die Gesamtverschiebung aus und ziehe den bekannten Pfeil ab.', HV, art=K)
    N.L('verschiebung', 3, 'Das Quadrat A(0 | 0), B(2 | 0), C(2 | 2), D(0 | 2) wird so verschoben, dass C auf den Ursprung fällt. Wo liegt dann A?', "A'(□ | □)", [-2, -2], ['0 - 2', '0 - 2'],
        'Damit C(2 | 2) nach (0 | 0) kommt, ist v = (−2 | −2). A\' = (0 − 2 | 0 − 2) = (−2 | −2).', 'Bestimme den Pfeil, der C in den Ursprung bringt.', HP)
    # drehung
    N.L('drehung', 2, 'Drehe P(2 | 5) um O(0 | 0) um 180°.', "P'(□ | □)", [-2, -5], ['-2', '-5'],
        'Drehung um 180° um O: Beide Vorzeichen drehen sich um. P\'(−2 | −5).', 'Eine halbe Drehung um O: Was passiert mit den Vorzeichen?', HP, grafik=ksys([(2, 5, 'P')]))
    N.L('drehung', 2, 'Drehe P(0 | 4) um O(0 | 0) um 90° IM Uhrzeigersinn.', "P'(□ | □)", [4, 0], ['4', '0'],
        'P liegt oben auf der y-Achse. Eine Vierteldrehung im Uhrzeigersinn bringt ihn nach rechts auf die x-Achse: P\'(4 | 0).', 'Achte auf die Richtung: im Uhrzeigersinn, also wie die Zeiger einer Uhr.', HP,
        grafik=ksys([(0, 4, 'P')]))
    N.A('drehung', 3, 'Eine Gerade g geht nicht durch den Punkt Z. Sie wird um Z um 180° gedreht. Was gilt für die Bildgerade g\'?', 'g\' ist parallel zu g.',
        ['g\' fällt auf g.', 'g\' steht senkrecht auf g.', 'g\' geht durch Z.'],
        'Bei einer Drehung um 180° dreht sich jede Richtung um. Eine umgedrehte Richtung ist wieder dieselbe Gerade-Richtung: g\' ∥ g. Weil g nicht durch Z geht, liegt g\' auf der anderen Seite von Z.',
        'Denke an eine waagrechte Gerade über Z. Wo liegt sie nach einer halben Drehung?', art=P)
    N.A('drehung', 3, 'A(4 | 0) soll um O um 90° GEGEN den Uhrzeigersinn gedreht werden. Jemand gibt A\'(0 | −4) an. Was stimmt?', 'Falsch: Er hat im Uhrzeigersinn gedreht. Richtig ist A\'(0 | 4).',
        ['Richtig, der Abstand zu O ist 4.', 'Falsch: Richtig ist A\'(−4 | 0).', 'Falsch: Richtig ist A\'(4 | 4).'],
        'Gegen den Uhrzeigersinn geht A von rechts (x-Achse) nach oben (y-Achse): A\'(0 | 4). (0 | −4) liegt unten – das wäre im Uhrzeigersinn. Der Abstand allein reicht nicht.',
        'Gegen den Uhrzeigersinn: von rechts nach oben.', art=P)
    N.L('drehung', 3, 'Nach einer Drehung um O um 90° gegen den Uhrzeigersinn liegt der Bildpunkt bei P\'(−2 | 5). Wo lag P?', 'P(□ | □)', [5, 2], ['5', '-(-2)'],
        'Rückwärts: um 90° im Uhrzeigersinn drehen. (x | y) → (y | −x): (−2 | 5) → (5 | 2). Probe: (5 | 2) gegen den Uhrzeigersinn → (−2 | 5) ✓.',
        'Mache die Drehung rückgängig: in die andere Richtung drehen.', HP)
    N.L('drehung', 3, 'P(3 | 1) wird zweimal hintereinander um O um 90° gegen den Uhrzeigersinn gedreht und danach am Ursprung gespiegelt. Wo landet P?', "P'(□ | □)", [3, 1], ['3', '1'],
        'Zweimal 90° sind 180°. Die Punktspiegelung an O ist noch einmal eine Drehung um 180°. Zusammen 360°: P bleibt bei (3 | 1).',
        'Zähle alle Drehwinkel zusammen. Eine Punktspiegelung ist eine Drehung um 180°.', HP, art=K)
    # symmetrie
    N.Z('symmetrie', 2, 'Um welchen kleinsten Winkel (größer als 0°) muss man ein regelmäßiges Zehneck um seinen Mittelpunkt drehen, damit es auf sich selbst fällt?', 36, '360 / 10',
        '360° : 10 = 36°.', 'Eine volle Drehung (360°) gleichmäßig auf die Ecken verteilen.', einheit='°')
    N.Z('symmetrie', 2, 'Wie viele Symmetrieachsen hat ein Parallelogramm, das weder Rechteck noch Raute ist?', 0, '0',
        'Faltet man es entlang einer Diagonale oder einer Mittellinie, passen die Hälften nicht aufeinander. Es hat 0 Achsen, ist aber punktsymmetrisch.',
        'Probiere in Gedanken alle Faltlinien: Diagonalen und Mittellinien.', grafik=figur({'A': [0, 0], 'B': [4, 0], 'C': [5, 2], 'D': [1, 2]}, linien=[['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A']], flaeche=['A', 'B', 'C', 'D']))
    N.A('symmetrie', 3, 'Zwei Vierecke haben jeweils vier Seiten von 5 cm Länge. Sind die beiden Vierecke sicher deckungsgleich?', 'Nein: Ein Quadrat und eine Raute mit anderen Winkeln haben beide vier 5-cm-Seiten.',
        ['Ja: Gleiche Seiten bedeuten gleiche Vierecke.', 'Ja: Es sind beides Quadrate.', 'Nein: Nur Dreiecke können deckungsgleich sein.'],
        'Ein Gegenbeispiel genügt: Quadrat (alle Winkel 90°) und Raute mit 60° und 120°. Bei Vierecken legen die Seiten die Form nicht fest.',
        'Suche ein Gegenbeispiel: Kann man ein Viereck aus vier gleichen Stäben „zusammendrücken“?', art=P)
    N.A('symmetrie', 3, 'Ein Logo ist drehsymmetrisch. Der kleinste Drehwinkel, der es auf sich selbst abbildet, ist 72°. Welcher Winkel bildet es NICHT auf sich selbst ab?', '180°',
        ['144°', '216°', '288°'], 'Möglich sind nur Vielfache von 72°: 72°, 144°, 216°, 288°, 360°. 180° ist kein Vielfaches von 72°.',
        'Welche Winkel erhält man, wenn man mehrmals um 72° dreht?', art=P)
    N.Z('symmetrie', 3, 'Ein Verkehrsschild ist ein regelmäßiges Achteck. Gib den kleinsten Drehwinkel über 100° an, der das Schild auf sich selbst abbildet.', 135, '3 * 360 / 8',
        'Kleinster Drehwinkel: 360° : 8 = 45°. Vielfache: 45°, 90°, 135° … Der erste über 100° ist 135°.', 'Bestimme erst den kleinsten Drehwinkel, dann seine Vielfachen.', einheit='°', art=P)
    N.Z('symmetrie', 3, 'Zwei gleich große Quadrate berühren sich nur an einer Ecke; ihre Diagonalen liegen auf einer Geraden (siehe Bild). Wie viele Symmetrieachsen hat die ganze Figur?', 2, '2',
        'Achse 1: die Gerade durch beide Diagonalen. Achse 2: die Senkrechte dazu durch den Berührpunkt. Waagrecht oder senkrecht passt es nicht.',
        'Prüfe die Gerade durch die Diagonalen und die Gerade senkrecht dazu durch die gemeinsame Ecke.', art=K,
        grafik=figur({'A': [0, 0], 'B': [2, 0], 'C': [2, 2], 'D': [0, 2], 'E': [4, 2], 'F': [4, 4], 'G': [2, 4]},
                     linien=[['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A'], ['C', 'E'], ['E', 'F'], ['F', 'G'], ['G', 'C']]))
    # parkett
    N.Z('parkett', 2, 'Ein regelmäßiges Achteck hat Innenwinkel von 135°. Man legt 2 Achtecke an eine Ecke. Wie groß ist die Lücke?', 90, '360 - 2 * 135',
        '360° − 2 · 135° = 90°. Die Lücke ist genau ein Quadrat-Winkel.', 'Eine volle Ecke hat 360°.', einheit='°')
    N.A('parkett', 2, 'Mit welchen regelmäßigen Vielecken (nur eine Sorte) kann man die Ebene lückenlos auslegen?', 'Dreiecke, Quadrate und Sechsecke',
        ['Dreiecke, Quadrate und Fünfecke', 'Quadrate, Fünfecke und Sechsecke', 'nur Quadrate'],
        'Der Innenwinkel muss 360° teilen: 60° (3-Eck), 90° (4-Eck), 120° (6-Eck) passen. 108° (5-Eck) nicht: 360 : 108 ist keine ganze Zahl.', 'Prüfe, ob 360° durch den Innenwinkel teilbar ist.')
    N.Z('parkett', 3, 'In einem regelmäßigen Vieleck ist jeder Innenwinkel 140° groß. Wie viele Ecken hat es?', 9, '360 / (180 - 140)',
        'Winkelsumme (n − 2) · 180° = n · 140°. Also 180n − 360 = 140n, 40n = 360 und n = 9.',
        'Die Winkelsumme im n-Eck ist (n − 2) · 180°. Stelle eine Gleichung auf.', art=P)
    N.Z('parkett', 3, 'Zwei regelmäßige Zwölfecke liegen an einer Ecke. Welches regelmäßige Vieleck schließt die Lücke genau? Gib die Zahl seiner Ecken an.', 3, '3',
        'Innenwinkel Zwölfeck: (12 − 2) · 180° : 12 = 150°. Lücke: 360° − 300° = 60°. 60° hat das gleichseitige Dreieck: 3 Ecken.',
        'Berechne zuerst den Innenwinkel des Zwölfecks mit (n − 2) · 180° : n.', art=P)
    assert (12 - 2) * 180 // 12 == 150 and 360 - 300 == 60
    N.A('parkett', 3, 'An einer Ecke treffen ein Quadrat, ein regelmäßiges Sechseck und ein regelmäßiges Zwölfeck zusammen. Passt das lückenlos?', 'Ja: 90° + 120° + 150° = 360°.',
        ['Nein: Verschiedene Vielecke passen nie zusammen.', 'Nein: 90° + 120° + 150° = 330°.', 'Ja, weil es drei Vielecke sind.'],
        'Innenwinkel: Quadrat 90°, Sechseck 120°, Zwölfeck 150°. Summe 360°: Die Ecke ist genau voll.', 'Bestimme alle drei Innenwinkel und addiere.', art=K)
    N.A('parkett', 3, 'Warum kann man mit regelmäßigen Fünfecken allein die Ebene nicht lückenlos auslegen?', 'Weil 360° : 108° keine ganze Zahl ist.',
        ['Weil Fünfecke keine rechten Winkel haben.', 'Weil 5 eine ungerade Zahl ist.', 'Weil Fünfecke zu viele Ecken haben.'],
        'Der Innenwinkel ist 108°. 3 Fünfecke: 324° (Lücke), 4 Fünfecke: 432° (Überlappung). 360 : 108 ≈ 3,33.', 'Was muss für die Winkel an einer Ecke gelten?')
    # eigenschaften
    N.A('eigenschaften', 2, 'Was kann sich bei einer Kongruenzabbildung ändern?', 'die Lage der Figur', ['die Seitenlängen', 'die Winkelgrößen', 'der Flächeninhalt'],
        'Kongruenzabbildungen erhalten Längen, Winkel und Flächen. Nur die Lage (und beim Spiegeln der Umlaufsinn) ändert sich.', 'Was bedeutet „deckungsgleich“?')
    N.Z('eigenschaften', 2, 'Ein Dreieck hat einen Flächeninhalt von 12 cm². Es wird gedreht und danach verschoben. Wie groß ist der Flächeninhalt des Bilddreiecks?', 12, '12',
        'Drehung und Verschiebung sind Kongruenzabbildungen. Das Bild ist deckungsgleich, also wieder 12 cm².', 'Ändert sich die Größe beim Drehen oder Verschieben?', einheit='cm²')
    N.A('eigenschaften', 3, 'Ein Dreieck ABC soll auf ein deckungsgleiches Dreieck mit ENTGEGENGESETZTEM Umlaufsinn abgebildet werden. Welche Abbildung leistet das?', 'eine Achsenspiegelung',
        ['eine Verschiebung', 'eine Drehung', 'eine Punktspiegelung'],
        'Nur die Achsenspiegelung kehrt den Umlaufsinn um. Verschiebung, Drehung und Punktspiegelung (Drehung um 180°) erhalten ihn.', 'Welche Abbildung macht aus „links herum“ „rechts herum“?', art=P)
    N.A('eigenschaften', 3, 'Eine Gerade g schneidet die Spiegelachse a im Punkt S. Wo schneidet die Bildgerade g\' die Achse a?', 'ebenfalls in S',
        ['nirgends, g\' ist parallel zu a', 'im Spiegelpunkt von S', 'auf der anderen Seite von S'],
        'Punkte auf der Achse bleiben bei der Spiegelung liegen (Fixpunkte). S liegt auf g und auf a, also liegt S auch auf g\'.', 'Was passiert mit Punkten, die auf der Achse liegen?', art=P)
    N.A('eigenschaften', 3, 'Eine Figur wird an zwei Achsen gespiegelt, die sich in S unter 30° schneiden. Welche einzelne Abbildung hat dieselbe Wirkung?', 'eine Drehung um S um 60°',
        ['eine Drehung um S um 30°', 'eine Verschiebung', 'eine Achsenspiegelung'],
        'Zwei Spiegelungen erhalten den Umlaufsinn (zweimal umgedreht). Bei sich schneidenden Achsen entsteht eine Drehung um S um den doppelten Schnittwinkel: 2 · 30° = 60°.',
        'Wie bei parallelen Achsen die Verschiebung um den doppelten Abstand: Was wird hier verdoppelt?', art=K)
    N.A('eigenschaften', 3, 'Ein Dreieck wird erst an der x-Achse gespiegelt und dann um O um 180° gedreht. Welche einzelne Abbildung hat dieselbe Wirkung?', 'Spiegelung an der y-Achse',
        ['Spiegelung an der x-Achse', 'Drehung um O um 180°', 'Verschiebung'],
        '(x | y) → (x | −y) → (−x | y). Nur das Vorzeichen von x ist am Ende anders: Spiegelung an der y-Achse.', 'Verfolge einen Punkt wie (2 | 3) durch beide Abbildungen.')
    return N


if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Spiegeln', ['achsenspiegelung', 'punktspiegelung']), ('Verschieben und Drehen', ['verschiebung', 'drehung']), ('Symmetrie und Eigenschaften', ['symmetrie', 'parkett', 'eigenschaften'])],
         'Achsenspiegelung, Punktspiegelung, Verschiebung und Drehung im Koordinatensystem ausführen, Symmetrien von Figuren erkennen, Parkettierungen prüfen und die Eigenschaften von Kongruenzabbildungen begründen.',
         ['Achsenspiegelung: gleich weit auf die andere Seite, senkrecht zur Achse.', 'Punktspiegelung an Z: Z ist Mitte von P und P\'.',
          'Verschiebung v = (a | b): x + a, y + b. Drehung um O um 90°: (x | y) → (−y | x).', 'Längen, Winkel und Flächen bleiben erhalten.', 'Parkett: Die Winkel an einer Ecke ergeben 360°.'],
         vertiefung=('verschiebung', 'drehung', 'parkett'),  # Vierzehnte Runde: kein Beleg in LehrplanPLUS Gym 5–10, nicht Pflicht
         offen=['Aufgaben zu Spiegelung, Verschiebung und Drehung zeigen die gegebenen Punkte, Achsen und Zentren im Koordinatensystem; das Kind gibt den Bildpunkt als Koordinaten ein. '
                'Selbst zeichnen (Konstruktion mit Zirkel und Geodreieck) kann die App noch nicht – dafür bräuchte es Eingabe durch Zeichnen.',
                'Neue Lernkarte „parkett“ (aus der Prüfung): Bild einer Ecke mit sechs Dreiecken; Aufgaben rechnerisch. Ganze Parkettflächen als Bild wären möglich, sind aber nicht eingebaut.',
                'Annahme der Prüfung, nicht umgesetzt: Drehungen würden in Klasse 7 vor allem konstruierend behandelt. Die Koordinatenregeln bleiben, werden aber über das Mitdrehen des Weges (rechts/oben) begründet; Konstruieren durch das Kind kann die App nicht.',
                'lehrplan_gym ist für dieses Thema in themenliste.json leer (Hinweis der Prüfung); themenliste.json gehört nicht zu diesem Paket und bleibt unverändert.',
                'Drehungen nur um Vielfache von 90°, weil andere Winkel im Koordinatensystem ohne Trigonometrie nicht exakt berechenbar sind.'])
    anhaengen(META['thema_schluessel'], schwer())
