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


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('abbildungen.kongruenz', 13_7_4)
# c) Beinahe-Dublette (gleiche Frage, Antwort N zweimal) → andere Eigenschaft
BF.ersetze('symmetrie', 'Welcher Großbuchstabe (Blockschrift) ist punktsymmetrisch, hat aber keine Symmetrieachse?', BF.A(
    'Welcher Großbuchstabe (Blockschrift) ist punktsymmetrisch und hat genau zwei Symmetrieachsen?', 'H', ['N', 'A', 'E'],
    'H: eine senkrechte und eine waagrechte Symmetrieachse, und um 180° gedreht sieht es gleich aus. N ist nur punktsymmetrisch, A und E haben je eine Achse und sind nicht punktsymmetrisch.',
    'Prüfe bei jedem Buchstaben: falten? um 180° drehen?'), enthaelt='"X"')
# c) Ablenker widersprechen sich selbst („= 360° ≠ 360°“, „Ja: … = 330°“) → Aufgaben mit sinnvollen Ablenkern
_hp = 'Addiere alle Winkel an der Ecke und vergleiche mit 360°.'
BF.ersetze('parkett', 'Passen 4 gleichseitige Dreiecke und ein Quadrat lückenlos um eine Ecke?', BF.A(
    'Lässt sich eine Ecke lückenlos mit 4 gleichseitigen Dreiecken und einem Quadrat auslegen?', 'Nein: 4 · 60° + 90° = 330°, es bleibt eine Lücke von 30°.',
    ['Ja: 4 · 60° + 90° = 360°.', 'Nein: Verschiedene Vielecke kann man an einer Ecke nie kombinieren.', 'Ja: Dreiecke und Quadrate passen immer zusammen.'],
    '4 · 60° + 90° = 240° + 90° = 330°. Bis 360° fehlen 30°, die Ecke ist nicht lückenlos.', _hp))
BF.ersetze('parkett', 'Passen 3 gleichseitige Dreiecke und 2 Quadrate lückenlos um eine Ecke?', BF.A(
    'Lässt sich eine Ecke lückenlos mit 3 gleichseitigen Dreiecken und 2 Quadraten auslegen?', 'Ja: 3 · 60° + 2 · 90° = 360°.',
    ['Nein: 3 · 60° + 2 · 90° = 330°.', 'Nein: Verschiedene Vielecke kann man an einer Ecke nie kombinieren.', 'Nein: Es müssen immer gleich viele von jeder Sorte sein.'],
    '3 · 60° + 2 · 90° = 180° + 180° = 360°. Die Ecke ist genau voll – das Muster kommt in echten Parketten vor.', _hp))
# a) Verkettung zweier Spiegelungen ist für Stufe 1 anspruchsvoll
BF.stufe('eigenschaften', 'Welche Aussage über Kongruenzabbildungen ist richtig?', 2, enthaelt='"o": {"index": 1}, "w": "Richtig: Zwei Achsenspiegelungen an parallelen Achsen')

# ---- BEFUNDE ENDE ----

# ---------- Achtzehnte Runde, Teil B (luecken-kl7): neue Lernkarten laut LehrplanPLUS M7 2.1 ----------
# Lücken aus inhalte/pruefung/aufbau/klasse7.json („luecken“): Mittelsenkrechte, Lot, Winkelhalbierende (hoch) und
# symmetrische Vierecke ordnen (niedrig). LehrplanPLUS Gymnasium M7 2.1: „konstruieren Mittelsenkrechte, Lote und Winkelhalbierende
# und beschreiben ihr Vorgehen“; Abstandsprobleme; „ordnen … die Menge aller symmetrischen Vierecke anhand ihrer Symmetrieeigenschaften“.
# Vorbilder (nur Typ und Niveau, eigene Zahlen): Bayerischer Mathematik-Test 8 (ISB) 2024 A4b (Schiff gleich weit von zwei Leuchttürmen),
# 2019 A4 (Punkt gleich weit von drei Orten), 2022 A1 (Abstand von g und von C), 2014 B (Schnitt zweier Mittelsenkrechten), 2023 A3 (Raute, Gegenbeispiel).
# Eigener Zufallsstart; die Karten werden nach dem bisherigen Zusammenbau eingesetzt, alte Karten und Aufgaben bleiben gleich.
import math  # noqa: E402
from _luecken_kl7 import Karte, begrenzt, einfuegen, fig, koord, pk, pol, zf  # noqa: E402

_HP = 'Trage die x- und die y-Koordinate ein.'


def _ms_karte():
    oft = begrenzt()
    A, B = (0, 0), (6, 0)
    h = math.sqrt(16 - 9)
    P, Q, M = (3, h), (3, -h), (3, 0)
    basis = {'A': A, 'B': B}
    kreise = [{'m': 'A', 'r': 4}, {'m': 'B', 'r': 4}]
    ab = ['A', 'B', 'AB = 6 cm']
    s1 = fig(basis, linien=[ab], kreise=kreise)
    s2 = fig({**basis, 'P': P, 'Q': Q}, linien=[ab], kreise=kreise)
    s3 = fig({**basis, 'P': P, 'Q': Q, 'M': M, '_m1': (3, -3.6), '_m2': (3, 3.6)}, linien=[ab, ['_m1', '_m2', 'm']], kreise=kreise,
             rechter_winkel=[['M', 'B', '_m2']])
    X = (3, 2)
    s4 = fig({**basis, 'M': M, 'X': X, '_m1': (3, -3.6), '_m2': (3, 3.6)}, linien=[ab, ['_m1', '_m2', 'm'], ['X', 'A', '', 'gestrichelt'], ['X', 'B', '', 'gestrichelt']],
             rechter_winkel=[['M', 'B', '_m2']])
    w7 = math.sqrt(7)
    s5 = fig({'C': (3, 3), 'P': (3 - w7, 0), 'Q': (3 + w7, 0), 'F': (3, 0), '_g1': (-1, 0), '_g2': (7, 0)},
             linien=[['_g1', '_g2', 'g'], ['C', 'F', 'Lot', 'gestrichelt']], kreise=[{'m': 'C', 'r': 4}], rechter_winkel=[['F', '_g2', 'C']])
    e = {
        'lernziel': 'mittelsenkrechte',
        'titel': 'Mittelsenkrechte und Lot',
        'einstieg': 'Zwei Freundinnen wohnen in den Häusern A und B. Sie suchen Treffpunkte, die von beiden Häusern gleich weit weg sind. '
                    'Alle diese Punkte liegen auf einer Geraden: der ⟦Mittelsenkrechten⟧.',
        'woerter': [['Mittelsenkrechte', 'Gerade durch die Mitte von [AB], senkrecht zu [AB]'],
                    ['Abstand', 'Länge des kürzesten Wegs; zu einer Geraden immer senkrecht gemessen'],
                    ['Lot', 'Gerade durch einen Punkt, die senkrecht auf einer anderen Geraden steht']],
        'bild': fig(basis, linien=[ab]),
        'schritte': [
            {'text': 'Zeichne um A und um B Kreise mit gleichem Radius, hier 4 cm.', 'bild': s1},
            {'text': 'Die beiden Kreise schneiden sich in P und Q.', 'bild': s2},
            {'text': 'Die Gerade PQ ist die ⟦Mittelsenkrechte m⟧ von [AB].', 'bild': s3},
            {'text': 'Jeder Punkt X auf m hat von A und B den gleichen Abstand.', 'bild': s4},
            {'text': 'Für das ⟦Lot⟧ von C auf g: Kreis um C, dann Mittelsenkrechte der Schnittpunkte.', 'bild': s5},
        ],
        'probe': 'P liegt auf beiden Kreisen: PA = PB = 4 cm ✓',
        'fehler': 'Zu kleine Kreise schneiden sich nicht – wie Freundinnen, die nicht weit genug laufen. Bei AB = 6 cm braucht man mehr als 3 cm.',
        'fehler_bild': fig(basis, linien=[ab], kreise=[{'m': 'A', 'r': 2.5}, {'m': 'B', 'r': 2.5}]),
        'regel': 'Auf der Mittelsenkrechten liegen alle Punkte gleich weit von A und B. Sie steht ⟦senkrecht⟧ auf [AB] und halbiert die Strecke.',
    }

    def m_waag(R, B_):
        y, a, k = R.randint(-3, 5), R.randint(-6, 3), R.randint(1, 5)
        b = a + 2 * k
        return B_.L(f'Die Punkte {pk("A", a, y)} und {pk("B", b, y)} liegen auf einer waagrechten Linie. Ihre Mittelsenkrechte ist senkrecht. Wo schneidet sie die x-Achse?',
                    'S(□ | □)', [a + k, 0], [f'({a} + {b}) / 2', '0'],
                    f'Die Mittelsenkrechte geht senkrecht durch die Mitte von [AB]. Der x-Wert der Mitte ist ({zf(a)} + {zf(b)}) : 2 = {zf(a + k)}. Sie schneidet die x-Achse in S({zf(a + k)} | 0).',
                    'Die Mittelsenkrechte geht durch die Mitte der Strecke – senkrecht nach oben und unten.', _HP, grafik=koord([(a, y, 'A'), (b, y, 'B')]))

    def m_senk(R, B_):
        x, a, k = R.randint(-4, 5), R.randint(-5, 2), R.randint(1, 4)
        b = a + 2 * k
        return B_.L(f'Die Punkte {pk("A", x, a)} und {pk("B", x, b)} liegen übereinander. Ihre Mittelsenkrechte ist waagrecht. Wo schneidet sie die y-Achse?',
                    'S(□ | □)', [0, a + k], ['0', f'({a} + {b}) / 2'],
                    f'Die Mittelsenkrechte geht waagrecht durch die Mitte von [AB]. Der y-Wert der Mitte ist ({zf(a)} + {zf(b)}) : 2 = {zf(a + k)}. Sie schneidet die y-Achse in S(0 | {zf(a + k)}).',
                    'Die Mittelsenkrechte geht durch die Mitte der Strecke und steht senkrecht auf ihr.', _HP, grafik=koord([(x, a, 'A'), (x, b, 'B')]))

    def m_mitte(R, B_):
        a, b = R.randint(-5, 3), R.randint(-4, 4)
        dx, dy = 2 * R.randint(1, 4), 2 * R.randint(-3, 3)
        if dy == 0: dy = 2
        return B_.L(f'Durch welchen Punkt M geht die Mittelsenkrechte von [AB] mit {pk("A", a, b)} und {pk("B", a + dx, b + dy)}?', 'M(□ | □)',
                    [a + dx // 2, b + dy // 2], [f'({a} + {a + dx}) / 2', f'({b} + {b + dy}) / 2'],
                    f'M ist die Mitte von [AB]: x-Wert ({zf(a)} + {zf(a + dx)}) : 2 = {zf(a + dx // 2)}, y-Wert ({zf(b)} + {zf(b + dy)}) : 2 = {zf(b + dy // 2)}.',
                    'Die Mittelsenkrechte geht durch den Mittelpunkt der Strecke.', _HP, grafik=koord([(a, b, 'A'), (a + dx, b + dy, 'B')]))

    def m_eig(R, B_):
        oft('eig')
        p, (a, b) = R.choice('PQRX'), R.choice([('A', 'B'), ('C', 'D'), ('E', 'F'), ('K', 'L')])
        richtig = f'{p} ist von {a} und {b} gleich weit entfernt.'
        return B_.A(f'Der Punkt {p} liegt auf der Mittelsenkrechten von [{a}{b}]. Was gilt sicher?', richtig,
                    [f'{p} ist der Mittelpunkt von [{a}{b}].', f'{p} liegt auf der Strecke [{a}{b}].', f'{p} ist von {a} doppelt so weit entfernt wie von {b}.'],
                    f'Alle Punkte der Mittelsenkrechten sind von {a} und {b} gleich weit entfernt. Der Mittelpunkt ist nur einer davon.',
                    'Was haben alle Punkte der Mittelsenkrechten gemeinsam?')

    def m_achse(R, B_):
        x, y = R.choice([v for v in range(-5, 6) if v]), R.choice([v for v in range(-5, 6) if v])
        p = R.choice('PQR')
        if R.random() < 0.5:
            return B_.Z(f'Wie weit ist {pk(p, x, y)} von der x-Achse entfernt? (1 Einheit = 1 cm)', abs(y), f'abs({y})',
                        f'Das Lot von {p} auf die x-Achse ist senkrecht und {zf(abs(y))} Einheiten lang: Abstand {zf(abs(y))} cm.',
                        'Der Abstand wird auf dem Lot gemessen – senkrecht zur x-Achse.', einheit='cm', grafik=koord([(x, y, p)]))
        return B_.Z(f'Wie weit ist {pk(p, x, y)} von der y-Achse entfernt? (1 Einheit = 1 cm)', abs(x), f'abs({x})',
                    f'Das Lot von {p} auf die y-Achse ist waagrecht und {zf(abs(x))} Einheiten lang: Abstand {zf(abs(x))} cm.',
                    'Der Abstand wird auf dem Lot gemessen – senkrecht zur y-Achse.', einheit='cm', grafik=koord([(x, y, p)]))

    def m_gleich(R, B_):
        d = R.choice([Fr(x, 2) for x in range(5, 25)])
        p = R.choice('PQRT')
        return B_.Z(f'{p} liegt auf der Mittelsenkrechten von [AB] und ist {zf(d)} cm von A entfernt. Wie weit ist {p} von B entfernt?', d, str(d),
                    f'Punkte der Mittelsenkrechten sind von A und B gleich weit entfernt: ebenfalls {zf(d)} cm.',
                    'Was bedeutet es, auf der Mittelsenkrechten zu liegen?', einheit='cm')

    def m_radius(R, B_):
        n = R.randint(5, 12)
        halb = Fr(n, 2)
        gross = [halb + Fr(k, 2) for k in (1, 2, 3)]
        klein = [halb, halb - Fr(1, 2), halb - 1, halb - Fr(3, 2)]
        r = R.choice(gross)
        f = R.sample([x for x in klein if x > 0], 3)
        return B_.A(f'AB = {n} cm. Die Kreise um A und um B mit gleichem Radius sollen sich in zwei Punkten schneiden. Welcher Radius passt?',
                    f'{zf(r)} cm', [f'{zf(x)} cm' for x in f],
                    f'Der Radius muss größer als die halbe Strecke sein: größer als {zf(halb)} cm. Nur {zf(r)} cm ist größer.',
                    'Die Kreise müssen weiter reichen als bis zur Mitte von [AB].',
                    pruef=lambda t: Fr(t.split()[0].replace(',', '.')) > halb)

    def m_fuss(R, B_):
        x, y = R.randint(-4, 6), R.randint(-3, 6)
        c = R.choice([v for v in range(-3, 6) if v != y])
        p = R.choice('PQC')
        if R.random() < 0.5:
            return B_.L(f'Fälle das Lot von {pk(p, x, y)} auf die waagrechte Gerade g durch {pk("", 0, c)}. Wo ist der Lotfußpunkt F?', 'F(□ | □)', [x, c], [str(x), str(c)],
                        f'Das Lot auf eine waagrechte Gerade ist senkrecht: Der x-Wert bleibt {zf(x)}. F liegt auf g, also ist der y-Wert {zf(c)}.',
                        'Das Lot auf eine waagrechte Gerade geht senkrecht nach oben oder unten.', _HP, grafik=koord([(x, y, p)], y=[c], waagrecht=[c]))
        return B_.L(f'Fälle das Lot von {pk(p, y, x)} auf die senkrechte Gerade g durch {pk("", c, 0)}. Wo ist der Lotfußpunkt F?', 'F(□ | □)', [c, x], [str(c), str(x)],
                    f'Das Lot auf eine senkrechte Gerade ist waagrecht: Der y-Wert bleibt {zf(x)}. F liegt auf g, also ist der x-Wert {zf(c)}.',
                    'Das Lot auf eine senkrechte Gerade geht waagrecht nach links oder rechts.', _HP, grafik=koord([(y, x, p)], x=[c], senkrecht=[c]))

    def m_abst(R, B_):
        x, y = R.randint(-4, 6), R.randint(-3, 7)
        c = R.choice([v for v in range(-3, 7) if v != y])
        p = R.choice('PQC')
        return B_.Z(f'Wie weit ist {pk(p, x, y)} von der waagrechten Geraden g durch {pk("", 0, c)} entfernt? (1 Einheit = 1 cm)', abs(y - c), f'abs({y} - ({c}))',
                    f'Gemessen wird auf dem Lot (senkrecht): vom y-Wert {zf(y)} bis zum y-Wert {zf(c)} sind es {zf(abs(y - c))} cm.',
                    'Der Abstand zu einer Geraden wird senkrecht gemessen.', einheit='cm', grafik=koord([(x, y, p)], y=[c], waagrecht=[c]))

    def m_spiel(R, B_):
        oft('spiel', 3)
        h, a, k = R.randint(3, 7), R.randint(-3, 3), R.randint(2, 4)
        b = a + 2 * k
        ding = R.choice(['ein Spielplatz', 'eine Bushaltestelle', 'ein Briefkasten', 'eine Bank'])
        return B_.L(f'Zwei Häuser stehen bei {pk("A", a, h)} und {pk("B", b, h)}. An der Straße (x-Achse) soll {ding} S hin, von beiden Häusern gleich weit entfernt.',
                    'S(□ | □)', [a + k, 0], [f'({a} + {b}) / 2', '0'],
                    f'S liegt auf der Mittelsenkrechten von [AB] – sie geht senkrecht durch die Mitte {pk("", a + k, h)} – und auf der x-Achse: S({zf(a + k)} | 0).',
                    'Gleich weit von A und B: Mittelsenkrechte. Dann mit der Straße schneiden.', _HP, grafik=koord([(a, h, 'A'), (b, h, 'B')]))

    def m_spiegel(R, B_):
        oft('spiegel')
        p = R.choice(['A', 'P', 'Q', 'R'])
        return B_.A(f"{p}' ist das Bild von {p} bei einer Achsenspiegelung. Wo liegt die Spiegelachse?", f"Sie ist die Mittelsenkrechte von [{p}{p}'].",
                    [f"Sie ist die Gerade durch {p} und {p}'.", f"Sie geht durch {p} und steht senkrecht auf [{p}{p}'].", f"Sie ist parallel zu [{p}{p}']."],
                    f"Bei der Achsenspiegelung ist {p}' gleich weit von der Achse entfernt wie {p}, und [{p}{p}'] steht senkrecht auf ihr: die Mittelsenkrechte.",
                    'Denk an die Achsenspiegelung: senkrecht zur Achse, gleich weit auf die andere Seite.')

    def m_schritt(R, B_):
        v = R.randint(0, 2)
        oft(('schritt', v))
        if v == 0:
            return B_.A('Du hast um A und um B Kreise mit gleichem Radius gezeichnet. Sie schneiden sich in P und Q. Was ist der nächste Schritt?',
                        'Die Gerade durch P und Q zeichnen.', ['Die Gerade durch A und P zeichnen.', 'Einen Kreis um P zeichnen.', 'Die Strecke [AP] halbieren.'],
                        'Die Schnittpunkte P und Q sind gleich weit von A und B entfernt. Die Gerade PQ ist die Mittelsenkrechte.',
                        'Welche Punkte kennst du jetzt, die gleich weit von A und B entfernt sind?')
        if v == 1:
            return B_.A('Du willst das Lot von C auf die Gerade g konstruieren. Was ist der erste Schritt?',
                        'Einen Kreis um C zeichnen, der g zweimal schneidet.', ['Einen Kreis um einen beliebigen Punkt von g zeichnen.', 'Die Gerade durch C parallel zu g zeichnen.', 'C mit einem beliebigen Punkt von g verbinden.'],
                        'Der Kreis um C liefert zwei Punkte auf g, die gleich weit von C entfernt sind. Ihre Mittelsenkrechte ist das Lot durch C.',
                        'Du brauchst zwei Punkte auf g, die von C gleich weit entfernt sind.')
        return B_.A('Für die Mittelsenkrechte von [AB] zeichnest du Kreise um A und um B. Was muss für ihre Radien gelten?',
                    'Beide gleich groß und größer als die Hälfte von AB.', ['Beide genau so groß wie AB.', 'Beide kleiner als die Hälfte von AB.', 'Die Radien dürfen verschieden sein.'],
                    'Gleiche Radien geben Punkte gleich weit von A und B. Größer als die halbe Strecke, sonst schneiden sich die Kreise nicht. AB selbst geht auch, ist aber keine Bedingung.',
                    'Die Schnittpunkte sollen gleich weit von A und B entfernt sein – und es soll sie geben.')

    def m_diag(R, B_):
        a, b, k = R.randint(-3, 2), R.randint(-3, 2), R.randint(2, 5)
        A_, B2 = (a, b), (a + k, b + k)
        r = R.choice([(a + k, b), (a, b + k)])
        d2 = lambda p, q: (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
        auf = lambda p: d2(p, A_) == d2(p, B2)
        kand = [(a + k, b + k - 1), (a + k + 1, b), (a + k - 1, b), (a, b + k + 1), (a + 1, b + 1), (a + k, b - 1), (a - 1, b + k)]
        f = R.sample([p for p in kand if not auf(p)], 3)
        nm = lambda p: pk('P', p[0], p[1])
        return B_.A(f'Gegeben sind {pk("A", *A_)} und {pk("B", *B2)}. Welcher Punkt liegt auf der Mittelsenkrechten von [AB]?', nm(r), [nm(p) for p in f],
                    f'{nm(r)} ist von A und von B jeweils {zf(k)} Einheiten entfernt (einmal waagrecht, einmal senkrecht gezählt). Die anderen Punkte sind von A und B verschieden weit entfernt.',
                    'Zähle Kästchen: Suche einen Punkt, der von A und B gleich weit weg ist, ohne schräg messen zu müssen.',
                    grafik=koord([(a, b, 'A'), (a + k, b + k, 'B')]),
                    pruef=lambda t: t == nm(r))

    def m_zwei(R, B_):
        h, d = R.randint(1, 5), R.randint(1, 4)
        r = R.randint(1, 6)
        n = lambda dist: 2 if dist < r else (1 if dist == r else 0)
        anz = n(abs(d - h)) + n(d + h)
        return B_.Z(f'Der Punkt C liegt {h} cm über der Geraden g. Wie viele Punkte sind von g genau {d} cm und von C genau {r} cm entfernt?', anz, str(anz),
                    f'Punkte mit Abstand {d} cm von g liegen auf zwei Parallelen ({d} cm über und unter g). Der Kreis um C mit {r} cm trifft die obere '
                    f'{n(abs(d - h))}-mal (Abstand {abs(d - h)} cm) und die untere {n(d + h)}-mal (Abstand {d + h} cm). Zusammen {anz}.',
                    'Zeichne die zwei Parallelen zu g und den Kreis um C. Zähle die Schnittpunkte.', art='pruefung',
                    grafik=koord([(0, h, 'C')], x=[-r, r], y=[-d, h + r], graphen=[{'art': 'linear', 'm': 0, 't': 0, 'name': 'g'}]))

    def m_drei(R, B_):
        a, b, p, q = R.randint(-2, 2), R.randint(-2, 2), R.randint(2, 4), R.randint(2, 4)
        if p == q: q += 1
        orte = R.choice([('Ahorn', 'Birk', 'Celle'), ('Au', 'Berg', 'Chiem'), ('Alm', 'Bach', 'Ried')])
        return B_.L(f'Drei Orte liegen bei {pk("A", a, b)}, {pk("B", a + 2 * p, b)} und {pk("C", a, b + 2 * q)}. Ein Funkmast soll von allen drei Orten gleich weit entfernt sein. Wo steht er?',
                    'M(□ | □)', [a + p, b + q], [f'({a} + {a + 2 * p}) / 2', f'({b} + {b + 2 * q}) / 2'],
                    f'M liegt auf der Mittelsenkrechten von [AB] (senkrecht durch die Mitte {pk("", a + p, b)}) und auf der von [AC] (waagrecht durch die Mitte {pk("", a, b + q)}). Schnittpunkt: M({zf(a + p)} | {zf(b + q)}).',
                    'Gleich weit von A und B: eine Mittelsenkrechte. Gleich weit von A und C: noch eine. Wo schneiden sie sich?', _HP, art='pruefung',
                    grafik=koord([(a, b, 'A'), (a + 2 * p, b, 'B'), (a, b + 2 * q, 'C')]))

    def m_lot_diag(R, B_):
        s = 2 * R.randint(1, 4)
        x = R.randint(s // 2 + 1, s + 3)
        y = s - x
        if x == y: x, y = x + 1, y - 1
        return B_.L(f'Die Gerade w geht durch (0 | 0) und (1 | 1). Fälle das Lot von {pk("P", x, y)} auf w. Wo ist der Lotfußpunkt F?', 'F(□ | □)', [s // 2, s // 2], [f'({x} + {y}) / 2', f'({x} + {y}) / 2'],
                    f"Spiegle P an w – dabei tauschen x und y: P'({zf(y)} | {zf(x)}). w ist die Mittelsenkrechte von [PP'], F ist die Mitte: F({zf(s // 2)} | {zf(s // 2)}).",
                    "Spiegle P an w (x und y tauschen). Der Fußpunkt ist die Mitte von P und P'.", _HP,
                    grafik=koord([(x, y, 'P')], graphen=[{'art': 'linear', 'm': 1, 't': 0, 'name': 'w'}]))

    def m_knobel(R, B_):
        ab = R.randint(4, 10)
        d = R.choice([Fr(ab, 2) - 1, Fr(ab, 2), Fr(ab, 2) + 1, Fr(ab, 2) + 2, Fr(ab, 2) - Fr(1, 2)])
        anz = 0 if d < Fr(ab, 2) else (1 if d == Fr(ab, 2) else 2)
        return B_.Z(f'AB = {ab} cm. Wie viele Punkte sind von A und B gleich weit entfernt und zugleich genau {zf(d)} cm von A entfernt?', anz, str(anz),
                    f'Die Punkte liegen auf der Mittelsenkrechten und auf dem Kreis um A mit {zf(d)} cm. Der nächste Punkt der Mittelsenkrechten ist die Mitte '
                    f'({zf(Fr(ab, 2))} cm von A). Darum gibt es {anz} solche Punkte.',
                    'Mittelsenkrechte und Kreis um A schneiden – wie nah kommt die Mittelsenkrechte an A heran?', art='knobel')

    # feste Stufe-3-Aufgaben (2 nach Prüfungsvorbild, 1 Knobel)
    def f_leucht(R, B_):
        return B_.L('Zwei Leuchttürme stehen bei L₁(1 | 6) und L₂(7 | 6). Ein Schiff fährt auf der Route durch (0 | 1) und (8 | 5). An welchem Punkt P der Route ist es von beiden Leuchttürmen gleich weit entfernt?',
                    'P(□ | □)', [4, 3], ['(1 + 7) / 2', '1 + 4 / 2'],
                    'P liegt auf der Mittelsenkrechten von [L₁L₂]; sie geht senkrecht durch die Mitte (4 | 6). Die Route steigt je 2 nach rechts um 1: beim x-Wert 4 ist der y-Wert 1 + 2 = 3. P(4 | 3).',
                    'Gleich weit von beiden Türmen: Mittelsenkrechte. Wo schneidet sie die Route?', _HP, art='pruefung',
                    grafik=koord([(1, 6, 'L₁'), (7, 6, 'L₂')], x=[8], graphen=[{'art': 'linear', 'm': 0.5, 't': 1, 'name': 'Route'}]))

    def f_drei(R, B_):
        return B_.L('Die Häuser A(−1 | 0), B(7 | 0) und C(−1 | 6) sollen einen gemeinsamen Spielplatz bekommen, der von allen drei Häusern gleich weit entfernt ist. Wo liegt er?',
                    'S(□ | □)', [3, 3], ['(-1 + 7) / 2', '(0 + 6) / 2'],
                    'Mittelsenkrechte von [AB]: senkrecht durch die Mitte (3 | 0). Mittelsenkrechte von [AC]: waagrecht durch die Mitte (−1 | 3). Sie schneiden sich in S(3 | 3); S ist von A, B und C je 5 Einheiten entfernt.',
                    'Zwei Mittelsenkrechten reichen: eine für A und B, eine für A und C.', _HP, art='pruefung',
                    grafik=koord([(-1, 0, 'A'), (7, 0, 'B'), (-1, 6, 'C')]))

    def f_knobel(R, B_):
        return B_.Z('Die Punkte A und B sind 8 cm voneinander entfernt. Wie viele Punkte gibt es, die von A und B gleich weit entfernt sind und von A genau 3 cm?', 0, '0',
                    'Solche Punkte müssten auf der Mittelsenkrechten liegen. Ihr nächster Punkt zu A ist die Mitte, 4 cm von A. 3 cm ist zu wenig: kein Punkt.',
                    'Wie nah kommt die Mittelsenkrechte an A heran?', art='knobel')

    return Karte(e, 'punktspiegelung', 'Spiegeln', 'Mittelsenkrechte und Lot',
                 {1: [m_waag, m_mitte, m_eig, m_achse, m_senk], 2: [m_gleich, m_radius, m_fuss, m_spiel, m_spiegel, m_schritt, m_abst],
                  3: [m_diag, m_zwei, m_drei, m_lot_diag, m_knobel]},
                 fest3=[f_leucht, f_drei, f_knobel])


def _wf(alpha, marken=(), w=False, punkte=()):
    """Winkel mit Scheitel S zwischen Schenkel nach rechts und Schenkel unter alpha (maßstäblich)."""
    P1, P2 = pol(5, 0), pol(5, alpha)
    pu = {'S': (0, 0), '_a': P1, '_b': P2}
    li = [['S', '_a'], ['S', '_b']]
    wk = []
    if w:
        pu['_w'] = pol(5.5, alpha / 2)
        li.append(['S', '_w', 'w', 'gestrichelt'])
    for von, bis, txt in marken:
        wk.append(['S', von, bis, txt])
    for k, v in punkte: pu[k] = v
    return fig(pu, linien=li, winkel=wk)


def _wh_karte():
    oft = begrenzt()
    al = 70
    S = (0, 0)
    a1, a2 = pol(6, 0), pol(6, al)
    P, Q = pol(3, 0), pol(3, al)
    # W auf der Winkelhalbierenden mit |WP| = 2.5
    u = (math.cos(math.radians(al / 2)), math.sin(math.radians(al / 2)))
    pu_ = u[0] * P[0] + u[1] * P[1]
    t = pu_ + math.sqrt(pu_ ** 2 - (9 - 2.5 ** 2))
    W = (t * u[0], t * u[1])
    grund = {'S': S, '_a1': a1, '_a2': a2}
    li = [['S', '_a1'], ['S', '_a2']]
    s1 = fig({**grund, 'P': P, 'Q': Q}, linien=li, kreise=[{'m': 'S', 'r': 3}])
    s2 = fig({**grund, 'P': P, 'Q': Q, 'W': W}, linien=li, kreise=[{'m': 'P', 'r': 2.5}, {'m': 'Q', 'r': 2.5}])
    wend = (6.5 * u[0], 6.5 * u[1])
    s3 = fig({**grund, 'W': W, '_w': wend}, linien=li + [['S', '_w', 'w']], winkel=[['S', '_a1', 'W', '35°'], ['S', 'W', '_a2', '35°']])
    X = (4 * u[0], 4 * u[1])
    v = (math.cos(math.radians(al)), math.sin(math.radians(al)))
    F1 = (X[0], 0)
    F2 = ((X[0] * v[0] + X[1] * v[1]) * v[0], (X[0] * v[0] + X[1] * v[1]) * v[1])
    s4 = fig({**grund, 'X': X, '_w': wend, '_F1': F1, '_F2': F2}, linien=li + [['S', '_w', 'w'], ['X', '_F1', '', 'gestrichelt'], ['X', '_F2', '', 'gestrichelt']],
             rechter_winkel=[['_F1', '_a1', 'X'], ['_F2', 'S', 'X']])
    e = {
        'lernziel': 'winkelhalbierende',
        'titel': 'Die Winkelhalbierende',
        'einstieg': 'Zwei Zäune treffen sich an einer Ecke. Ein Weg soll genau mittendrin verlaufen, also von beiden Zäunen gleich weit weg. '
                    'Dieser Weg ist die ⟦Winkelhalbierende⟧.',
        'woerter': [['Winkelhalbierende', 'Halbgerade vom Scheitel aus, die den Winkel in zwei gleich große Teile teilt']],
        'bild': fig(grund, linien=li, winkel=[['S', '_a1', '_a2', '70°']]),
        'schritte': [
            {'text': 'Zeichne einen Kreis um den Scheitel S. Er schneidet die Schenkel in P und Q.', 'bild': s1},
            {'text': 'Zeichne um P und um Q Kreise mit gleichem Radius. Sie schneiden sich in W.', 'bild': s2},
            {'text': 'Die Halbgerade von S durch W ist die ⟦Winkelhalbierende w⟧: 35° und 35°.', 'bild': s3},
            {'text': 'Jeder Punkt X auf w hat von beiden Schenkeln den gleichen ⟦Abstand⟧.', 'bild': s4},
        ],
        'probe': '35° + 35° = 70° ✓',
        'fehler': 'Abstand schräg gemessen: Der Weg zum Zaun zählt nur auf dem kürzesten, senkrechten Stück. Schräg gemessen wirkt X ungleich weit weg.',
        'fehler_bild': fig({**grund, 'X': X, '_w': wend, '_F1': F1, '_s': (1.2, 0)}, linien=li + [['S', '_w', 'w'], ['X', '_s', 'schräg', 'gestrichelt'], ['X', '_F1', 'Lot', 'gestrichelt']],
                           rechter_winkel=[['_F1', '_a1', 'X']]),
        'regel': 'Auf der Winkelhalbierenden liegen alle Punkte gleich weit von beiden Schenkeln. Sie teilt den Winkel in zwei ⟦gleich große⟧ Teile.',
    }

    def w_halb(R, B_):
        a = 2 * R.randint(10, 85)
        return B_.Z(f'Die Winkelhalbierende teilt den Winkel α = {a}°. Wie groß ist jeder der beiden Teile?', a // 2, f'{a} / 2',
                    f'Halbieren: {a}° : 2 = {a // 2}°.', 'Halbierende heißt: zwei gleich große Teile.', einheit='°',
                    grafik=_wf(a, [('_a', '_b', f'{a}°')], w=True))

    def w_abst(R, B_):
        d = R.choice([Fr(x, 2) for x in range(3, 19)])
        p = R.choice('PXY')
        return B_.Z(f'{p} liegt auf der Winkelhalbierenden des Winkels mit den Schenkeln s und t. {p} ist {zf(d)} cm von s entfernt. Wie weit ist {p} von t entfernt?', d, str(d),
                    f'Punkte der Winkelhalbierenden sind von beiden Schenkeln gleich weit entfernt: {zf(d)} cm.',
                    'Was haben alle Punkte der Winkelhalbierenden gemeinsam?', einheit='cm')

    def w_achsen(R, B_):
        k = R.randint(2, 6)
        r = (k, k)
        kand = [(k, k + 1), (k + 1, k - 1), (k, 0), (0, k), (k - 1, k + 1), (2 * k, k), (k, 2 * k)]
        f = R.sample([p for p in kand if abs(p[0]) != abs(p[1])], 3)
        nm = lambda p: pk('P', p[0], p[1])
        return B_.A('Welcher Punkt ist von der x-Achse und von der y-Achse gleich weit entfernt?', nm(r), [nm(p) for p in f],
                    f'Abstand zur x-Achse ist der y-Wert, Abstand zur y-Achse der x-Wert. Bei {nm(r)} sind beide {k}: Der Punkt liegt auf der Winkelhalbierenden der beiden Achsen.',
                    'Der Abstand zur x-Achse ist |y|, zur y-Achse |x|.', pruef=lambda t: t == nm(r))

    def w_eig(R, B_):
        oft('eig')
        p = R.choice('PQX')
        return B_.A(f'{p} liegt auf der Winkelhalbierenden von α. Was gilt sicher?', f'{p} ist von beiden Schenkeln gleich weit entfernt.',
                    [f'{p} ist vom Scheitel genau so weit entfernt wie von jedem Schenkel.', f'{p} ist von beiden Schenkeln doppelt so weit entfernt wie vom Scheitel.',
                     f'{p} liegt auf einem der beiden Schenkel.'],
                    'Alle Punkte der Winkelhalbierenden haben von beiden Schenkeln den gleichen (senkrecht gemessenen) Abstand.',
                    'Woran erkennt man einen Punkt auf der Winkelhalbierenden?')

    def w_ganz(R, B_):
        oft('ganz', 3)
        h = R.randint(8, 85)
        return B_.Z(f'Die Winkelhalbierende teilt α in zwei Teile. Jeder Teil ist {h}° groß. Wie groß ist α?', 2 * h, f'2 * {h}',
                    f'Zwei gleiche Teile: α = 2 · {h}° = {2 * h}°.', 'Die beiden Teile sind gleich groß.', einheit='°',
                    grafik=_wf(2 * h, [('_a', '_w', f'{h}°'), ('_w', '_b', '?')], w=True))

    def w_neben(R, B_):
        a = 2 * R.randint(15, 75)
        b = 180 - a
        oft('neben', 2)
        return B_.Z(f'α = {a}° und β = {b}° sind Nebenwinkel. Wie groß ist der Winkel zwischen den Winkelhalbierenden von α und β?', 90, f'{a} / 2 + {b} / 2',
                    f'{a}° : 2 + {b}° : 2 = {a // 2}° + {b // 2}° = 90°.', 'Addiere die beiden Hälften.', einheit='°')

    def w_auf(R, B_):
        oft('auf', 2)
        d = R.randint(2, 7)
        ach = R.choice(['x-Achse', 'y-Achse'])
        return B_.L(f'P liegt im 1. Quadranten auf der Winkelhalbierenden von x-Achse und y-Achse und hat von der {ach} den Abstand {d}. Gib P an.', 'P(□ | □)', [d, d], [str(d), str(d)],
                    f'Auf dieser Winkelhalbierenden sind beide Abstände gleich, x-Wert und y-Wert also auch: P({d} | {d}).', 'Von beiden Achsen gleich weit entfernt.', _HP)

    def w_schritt(R, B_):
        v = R.random() < 0.5
        oft(('schritt', v))
        if v:
            return B_.A('Für die Winkelhalbierende hast du einen Kreis um den Scheitel S gezeichnet. Er schneidet die Schenkel in P und Q. Was folgt?',
                        'Kreise mit gleichem Radius um P und um Q zeichnen.', ['Die Strecke [PQ] zeichnen und fertig.', 'Einen zweiten Kreis um S zeichnen.', 'Die Gerade durch P und Q verlängern.'],
                        'Die Kreise um P und Q schneiden sich in einem Punkt W, der gleich weit von P und Q ist. Die Halbgerade SW halbiert den Winkel.',
                        'Du brauchst noch einen zweiten Punkt auf der Winkelhalbierenden.')
        return B_.A('Die Kreise um P und Q haben sich im Punkt W geschnitten. Was ist der letzte Schritt für die Winkelhalbierende?',
                    'Die Halbgerade von S durch W zeichnen.', ['Die Strecke [PW] zeichnen.', 'Die Gerade durch P und Q zeichnen.', 'Einen Kreis um W zeichnen.'],
                    'S und W liegen beide auf der Winkelhalbierenden; die Halbgerade von S durch W ist sie.', 'Welche zwei Punkte liegen sicher auf der Winkelhalbierenden?')

    def w_rest(R, B_):
        h = R.randint(15, 80)
        return B_.Z(f'Die Winkelhalbierende von α bildet mit einem Schenkel {h}°. Wie groß ist der Nebenwinkel von α?', 180 - 2 * h, f'180 - 2 * {h}',
                    f'α = 2 · {h}° = {2 * h}°. Nebenwinkel: 180° − {2 * h}° = {180 - 2 * h}°.', 'Erst α bestimmen, dann zu 180° ergänzen.', einheit='°')

    def w_gerad(R, B_):
        c, e0, k = R.randint(-2, 3), R.randint(-3, 2), R.randint(2, 4)
        r = (e0 + k, c + k)
        auf = lambda p: abs(p[0] - e0) == abs(p[1] - c)
        kand = [(e0 + k, c + k + 1), (e0 + k + 1, c), (e0, c + k), (e0 + k, c), (e0 + 2 * k, c + k), (e0 + 1, c + k)]
        f = R.sample([p for p in kand if not auf(p)], 3)
        nm = lambda p: pk('P', p[0], p[1])
        return B_.A(f'Gegeben sind die waagrechte Gerade g durch {pk("", 0, c)} und die senkrechte Gerade h durch {pk("", e0, 0)}. Welcher Punkt ist von g und h gleich weit entfernt?', nm(r), [nm(p) for p in f],
                    f'Abstand zu g: senkrecht bis g gezählt. Abstand zu h: waagrecht bis h gezählt. Bei {nm(r)} sind beide {k}.',
                    'Zähle die Kästchen senkrecht bis g und waagrecht bis h.', pruef=lambda t: t == nm(r),
                    grafik=koord([], x=[e0, e0 + 2 * k + 1] + [p[0] for p in [r] + f], y=[c, c + k + 2] + [p[1] for p in [r] + f], waagrecht=[c], senkrecht=[e0]))  # g, h und alle Auswahlpunkte sichtbar (Prüfung 17.11.)

    def w_brunnen(R, B_):
        k = R.choice([2, 3, 4, 6, 7])
        return B_.L(f'Zwei Straßen verlaufen entlang der x-Achse und der y-Achse. Ein Brunnen soll von beiden Straßen gleich weit entfernt sein und am Weg von (0 | {2 * k}) nach ({2 * k} | 0) liegen.',
                    'B(□ | □)', [k, k], [f'{2 * k} / 2', f'{2 * k} / 2'],
                    f'Gleich weit von beiden Straßen heißt: x-Wert und y-Wert sind gleich (Winkelhalbierende der Achsen). Auf dem Weg von (0 | {2 * k}) nach ({2 * k} | 0) ist das nur in der Mitte so: B({k} | {k}).',
                    'Gleich weit von beiden Achsen heißt: x und y sind gleich.', _HP, art='pruefung',
                    grafik=koord([(0, 2 * k), (2 * k, 0)], strecken=[[0, 2 * k, 2 * k, 0]]))

    def w_ecke(R, B_):
        c, e0, m = R.randint(-2, 2), R.randint(-3, 1), R.randint(3, 6)
        return B_.L(f'Die waagrechte Gerade g durch {pk("", 0, c)} und die senkrechte Gerade h durch {pk("", e0, 0)} kreuzen sich. Gesucht ist der Punkt rechts von h und oberhalb von g, der von g und h gleich weit entfernt ist und den y-Wert {zf(c + m)} hat.',
                    'P(□ | □)', [e0 + m, c + m], [f'{e0} + {m}', f'{c} + {m}'],
                    f'Beim y-Wert {zf(c + m)} ist der Abstand zu g gleich {m}. Also ist auch der Abstand zu h gleich {m}: x-Wert {zf(e0)} + {m} = {zf(e0 + m)}.',
                    'Bestimme zuerst den Abstand zu g; derselbe Abstand gilt für h.', _HP,
                    grafik=koord([], x=[e0, e0 + m + 1], y=[c, c + m + 1], waagrecht=[c, c + m], senkrecht=[e0]))  # g und h sichtbar (Prüfung 17.11.)

    def w_aussen(R, B_):
        h = R.randint(20, 80)
        return B_.Z(f'α = {2 * h}° wird halbiert. Wie groß ist der Winkel zwischen der Winkelhalbierenden und der Verlängerung eines Schenkels über den Scheitel hinaus?',
                    180 - h, f'180 - {h}', f'Halbgerade und Verlängerung bilden mit dem Schenkel eine Gerade: 180° − {h}° = {180 - h}°.',
                    'Schenkel und seine Verlängerung bilden eine Gerade (180°).', einheit='°')

    def w_knobel(R, B_):
        d = R.randint(2, 6)
        ach = R.choice(['x-Achse', 'y-Achse'])
        return B_.Z(f'Wie viele Punkte sind von beiden Koordinatenachsen gleich weit entfernt und haben von der {ach} den Abstand {d}?', 4, '4',
                    f'Es gilt |x| = |y| = {d}: ({d} | {d}), (−{d} | {d}), (−{d} | −{d}), ({d} | −{d}) – in jedem Quadranten einer, also 4.',
                    'Die Achsen bilden vier Winkel. Jeder hat eine Winkelhalbierende.', art='knobel')

    def f_brunnen(R, B_):
        return B_.L('Ein Feld wird von zwei geraden Wegen begrenzt: der x-Achse und der y-Achse. Ein Baum soll von beiden Wegen gleich weit entfernt sein und am Bach von (0 | 10) nach (10 | 0) stehen.',
                    'B(□ | □)', [5, 5], ['10 / 2', '10 / 2'],
                    'Gleich weit von beiden Wegen heißt: x-Wert und y-Wert sind gleich (Winkelhalbierende der Achsen). Auf dem Bach von (0 | 10) nach (10 | 0) ist das nur in der Mitte so: B(5 | 5).',
                    'Gleich weit von beiden Achsen heißt: x und y sind gleich.', _HP, art='pruefung',
                    grafik=koord([(0, 10), (10, 0)], strecken=[[0, 10, 10, 0]]))

    def f_senk(R, B_):
        return B_.A('Warum stehen die Winkelhalbierenden zweier Nebenwinkel immer senkrecht aufeinander?', 'Die beiden Hälften ergeben zusammen 180° : 2 = 90°.',
                    ['Weil Nebenwinkel immer gleich groß sind.', 'Weil Nebenwinkel immer 90° groß sind.', 'Weil eine Winkelhalbierende immer senkrecht auf einem Schenkel steht.'],
                    'Nebenwinkel ergeben zusammen 180°. Ihre Hälften ergeben zusammen die Hälfte davon, also 90°.',
                    'Wie viel ergeben Nebenwinkel zusammen? Und ihre Hälften?', art='pruefung')

    def f_knobel(R, B_):
        return B_.Z('Wie viele Punkte sind von der x-Achse und von der y-Achse jeweils genau 3 Einheiten entfernt?', 4, '4',
                    'Es muss |x| = 3 und |y| = 3 gelten: (3 | 3), (−3 | 3), (−3 | −3), (3 | −3). Das sind 4 Punkte – auf den beiden Winkelhalbierenden der Achsen.',
                    'Denk an alle vier Quadranten.', art='knobel')

    return Karte(e, 'mittelsenkrechte', 'Spiegeln', 'Winkelhalbierende',
                 {1: [w_halb, w_abst, w_achsen, w_eig], 2: [w_ganz, w_neben, w_auf, w_schritt, w_rest, w_gerad], 3: [w_brunnen, w_ecke, w_aussen, w_knobel, w_gerad]},
                 fest3=[f_brunnen, f_senk, f_knobel])


_VI = ['Quadrat', 'Rechteck', 'Raute', 'Parallelogramm', 'Drachenviereck', 'gleichschenkliges Trapez']
_ART = {'Raute': 'eine'}
_JEDE = {'Quadrat': 'Jedes Quadrat', 'Rechteck': 'Jedes Rechteck', 'Raute': 'Jede Raute', 'Parallelogramm': 'Jedes Parallelogramm',
         'Drachenviereck': 'Jedes Drachenviereck', 'gleichschenkliges Trapez': 'Jedes gleichschenklige Trapez'}
_ACHSEN = {'Quadrat': 4, 'Rechteck': 2, 'Raute': 2, 'Parallelogramm': 0, 'Drachenviereck': 1, 'gleichschenkliges Trapez': 1}
_PUNKT = {'Quadrat': True, 'Rechteck': True, 'Raute': True, 'Parallelogramm': True, 'Drachenviereck': False, 'gleichschenkliges Trapez': False}
_UNTER = {'Quadrat': {'Rechteck', 'Raute', 'Parallelogramm', 'Drachenviereck', 'gleichschenkliges Trapez'},
          'Rechteck': {'Parallelogramm', 'gleichschenkliges Trapez'}, 'Raute': {'Parallelogramm', 'Drachenviereck'},
          'Parallelogramm': set(), 'Drachenviereck': set(), 'gleichschenkliges Trapez': set()}
_BESCHR = {'Quadrat': 'vier Symmetrieachsen', 'Rechteck': 'genau zwei Symmetrieachsen, die durch Seitenmitten gehen',
           'Raute': 'genau zwei Symmetrieachsen, die durch Ecken gehen', 'Drachenviereck': 'genau eine Symmetrieachse, die durch zwei Ecken geht',
           'gleichschenkliges Trapez': 'genau eine Symmetrieachse, die durch zwei Seitenmitten geht', 'Parallelogramm': 'keine Symmetrieachse, ist aber punktsymmetrisch'}


def _ein(x):
    return f"{_ART.get(x, 'ein')} {x}"


def _ist(x, y):
    return x == y or y in _UNTER[x]


def _treffen(x, y):
    """speziellstes Viereck, das sicher sowohl x als auch y ist (Haus der Vierecke)."""
    gem = [v for v in _VI if _ist(v, x) and _ist(v, y)]
    allg = [v for v in gem if all(_ist(w, v) for w in gem)]
    return allg[0] if len(allg) == 1 else None


def _vo_karte():
    oft = begrenzt()
    raute = {'A': (0, 2), 'B': (3, 0), 'C': (6, 2), 'D': (3, 4)}
    quad = {'A': (0, 0), 'B': (4, 0), 'C': (4, 4), 'D': (0, 4)}
    rl = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A']]
    s1 = fig({**raute, '_l': (-1, 2), '_r': (7, 2), '_o': (3, 5), '_u': (3, -1)}, flaeche=['A', 'B', 'C', 'D'],
             linien=rl + [['_l', '_r', '', 'gestrichelt'], ['_u', '_o', '', 'gestrichelt']])
    s2 = fig({**quad, '_1': (-1, -1), '_2': (5, 5), '_3': (-1, 5), '_4': (5, -1), '_5': (2, -1), '_6': (2, 5), '_7': (-1, 2), '_8': (5, 2)},
             flaeche=['A', 'B', 'C', 'D'], linien=rl + [['_1', '_2', '', 'gestrichelt'], ['_4', '_3', '', 'gestrichelt'], ['_5', '_6', '', 'gestrichelt'], ['_7', '_8', '', 'gestrichelt']],
             rechter_winkel=[['A', 'B', 'D']])
    tab = {'typ': 'tabelle', 'kopf': ['Viereck', 'Achsen', 'Punktsymmetrie'],
           'zeilen': [['Quadrat', '4', 'ja'], ['Rechteck', '2', 'ja'], ['Raute', '2', 'ja'], ['Parallelogramm', '0', 'ja'],
                      ['Drachenviereck', '1', 'nein'], ['gleichschenkl. Trapez', '1', 'nein']]}
    D50 = pol(4, 50)
    e = {
        'lernziel': 'vierecke_ordnen',
        'titel': 'Symmetrische Vierecke ordnen',
        'einstieg': 'Ein Fliesenleger sortiert Fliesen nach ihrer Symmetrie. Dabei merkt er: Jede quadratische Fliese passt auch in die Kiste der Rauten. '
                    'So entsteht das ⟦Haus der Vierecke⟧.',
        'woerter': [['Haus der Vierecke', 'Schema: oben die allgemeinen, unten die besonderen Vierecke'],
                    ['Drachenviereck', 'Viereck mit einer Symmetrieachse durch zwei gegenüberliegende Ecken'],
                    ['gleichschenkliges Trapez', 'Viereck mit einer Symmetrieachse durch die Mitten zweier Seiten']],
        'bild': tab,
        'schritte': [
            {'text': 'Eine Raute hat zwei Symmetrieachsen: ihre beiden Diagonalen.', 'bild': s1},
            {'text': 'Ein Quadrat hat diese zwei Achsen auch – und noch zwei dazu.', 'bild': s2},
            {'text': 'Also ist ⟦jedes Quadrat eine Raute⟧, aber nicht jede Raute ein Quadrat.'},
            {'text': 'Ebenso ist jede Raute ein Drachenviereck, jedes Rechteck ein gleichschenkliges Trapez.', 'bild': tab},
        ],
        'probe': 'Quadrat: 4 Achsen und punktsymmetrisch – es hat alles, was Raute und Rechteck haben ✓',
        'fehler': '„Jede Raute ist ein Quadrat“ stimmt nicht: Eine schiefe Raute hat keinen rechten Winkel. Nur umgekehrt stimmt es: Jedes Quadrat ist eine Raute.',
        'fehler_bild': fig({'A': (0, 0), 'B': (4, 0), 'C': (4 + D50[0], D50[1]), 'D': D50}, flaeche=['A', 'B', 'C', 'D'], linien=rl,
                           winkel=[['A', 'B', 'D', '50°']]),
        'regel': 'Je mehr Symmetrie, desto weiter unten im Haus der Vierecke. Ein Viereck unten hat alle ⟦Eigenschaften⟧ der Vierecke darüber.',
    }

    def v_wahr(R, B_):
        x = R.choice([v for v in _VI if _UNTER[v]])
        y = R.choice(sorted(_UNTER[x]))
        paare = [(a, b) for a in _VI for b in _VI if a != b and not _ist(a, b)]
        f = R.sample(paare, 3)
        satz = lambda a, b: f'{_JEDE[a]} ist {_ein(b)}.'
        return B_.A('Welche Aussage ist wahr?', satz(x, y), [satz(a, b) for a, b in f],
                    f'Im Haus der Vierecke führt ein Weg von „{x}“ nach oben zu „{y}“: {satz(x, y)} Die anderen Sätze gelten nur umgekehrt oder gar nicht.',
                    'Im Haus der Vierecke: Ein Viereck weiter unten ist auch jedes Viereck darüber, mit dem es verbunden ist.',
                    pruef=lambda t: any(t == satz(a, b) for a in _VI for b in _VI if a != b and _ist(a, b)))

    def v_beschr(R, B_):
        x = R.choice(_VI)
        oft(('beschr', x))
        andere = R.sample([v for v in _VI if v != x], 3)
        frage = R.choice(['Welches Viereck hat {}?', 'Ein Viereck hat {}. Welches ist es?'])
        return B_.A(frage.format(_BESCHR[x]), x, andere,
                    f'{x}: {_BESCHR[x]}. Die anderen Vierecke haben andere Achsen.', 'Zähle die Achsen und schau, wo sie verlaufen: durch Ecken oder durch Seitenmitten?',
                    pruef=lambda t: t == x)

    def v_zahl(R, B_):
        aus = R.sample([v for v in _VI if v != 'Parallelogramm'], R.randint(4, 5))
        eig = R.choice(['punktsymmetrisch', 'achsensymmetrisch'])
        test = (lambda v: _PUNKT[v]) if eig == 'punktsymmetrisch' else (lambda v: _ACHSEN[v] > 0)
        anz = sum(1 for v in aus if test(v))
        return B_.Z(f'Wie viele dieser Vierecke sind {eig}: {", ".join(aus)}?', anz, str(anz),
                    f'{eig}: ' + ', '.join(v for v in aus if test(v)) + f' – das sind {anz}.',
                    'Geh die Liste einzeln durch.' + (' Punktsymmetrisch: nach halber Drehung gleich.' if eig == 'punktsymmetrisch' else ' Achsensymmetrisch: mindestens eine Faltachse.'))

    def v_bild(R, B_):
        x = R.choice(['Rechteck', 'Raute', 'Parallelogramm', 'Drachenviereck', 'gleichschenkliges Trapez'])
        if x == 'Rechteck':
            a, b = R.sample([3, 4, 5, 6], 2)
            pu = {'A': (0, 0), 'B': (a, 0), 'C': (a, b), 'D': (0, b)}
        elif x == 'Raute':
            d1, d2 = R.sample([4, 5, 6, 7, 8], 2)
            pu = {'A': (0, d2 / 2), 'B': (d1 / 2, 0), 'C': (d1, d2 / 2), 'D': (d1 / 2, d2)}
        elif x == 'Parallelogramm':
            a, o, h = R.choice([5, 6]), R.choice([1, 2]), R.choice([2, 3])
            pu = {'A': (0, 0), 'B': (a, 0), 'C': (a + o, h), 'D': (o, h)}
        elif x == 'Drachenviereck':
            p, q, L = R.choice([2, 2.5, 3]), R.choice([1.5, 2]), R.choice([6, 7])
            pu = {'A': (0, 0), 'B': (p, L - q), 'C': (0, L), 'D': (-p, L - q)}
        else:
            a, o, h = R.choice([6, 7]), R.choice([1, 1.5, 2]), R.choice([2, 3])
            pu = {'A': (0, 0), 'B': (a, 0), 'C': (a - o, h), 'D': (o, h)}
        f = R.sample([v for v in _VI if v != x and not _ist(x, v)], 3)
        return B_.A('Welches Viereck ist abgebildet (maßstäblich gezeichnet)? Wähle die genaueste Bezeichnung.', x, f,
                    f'Das Bild zeigt {_ein(x)}: {_BESCHR[x]}.', 'Prüfe Seitenlängen, rechte Winkel und mögliche Faltachsen.',
                    grafik=fig(pu, flaeche=['A', 'B', 'C', 'D'], linien=[['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A']]), pruef=lambda t: t == x)

    def v_ort(R, B_):
        x = R.choice(['Raute', 'Rechteck', 'Drachenviereck', 'gleichschenkliges Trapez'])
        oft(('ort', x))
        ort = {'Raute': 'durch je zwei gegenüberliegende Ecken (die Diagonalen)', 'Rechteck': 'durch die Mitten je zweier gegenüberliegender Seiten',
               'Drachenviereck': 'nur eine Achse, durch zwei gegenüberliegende Ecken', 'gleichschenkliges Trapez': 'nur eine Achse, durch die Mitten der beiden parallelen Seiten'}
        return B_.A(f'Wo verlaufen die Symmetrieachsen {"einer" if x == "Raute" else "eines"} {x.replace("gleichschenkliges Trapez", "gleichschenkligen Trapezes").replace("Rechteck", "Rechtecks").replace("Drachenviereck", "Drachenvierecks")}?',
                    ort[x], [v for k, v in ort.items() if k != x], f'{x}: {_BESCHR[x]}.', 'Falte in Gedanken: Wo liegen die Hälften genau aufeinander?')

    def v_falsch(R, B_):
        wahr = [(a, b) for a in _VI for b in _VI if a != b and _ist(a, b)]
        falsch = [(a, b) for a in _VI for b in _VI if a != b and not _ist(a, b) and _ist(b, a)]
        x = R.choice(falsch)
        w = R.sample(wahr, 3)
        satz = lambda a, b: f'{_JEDE[a]} ist {_ein(b)}.'
        return B_.A('Welche Aussage ist falsch?', satz(*x), [satz(a, b) for a, b in w],
                    f'{satz(*x)} stimmt nicht. Umgekehrt stimmt es: {_JEDE[x[1]]} ist {_ein(x[0])}.',
                    'Prüfe bei jedem Satz die Richtung: Ist das erste Viereck ein Spezialfall des zweiten?',
                    pruef=lambda t: t in [satz(a, b) for a, b in falsch])

    def v_ueber(R, B_):
        x, r, f = R.choice([('dem Quadrat', 'Rechteck und Raute', ['Raute und Drachenviereck', 'Rechteck und Parallelogramm', 'Drachenviereck und gleichschenkliges Trapez']),
                            ('dem Rechteck', 'Parallelogramm und gleichschenkliges Trapez', ['Quadrat und Raute', 'Raute und Drachenviereck', 'Parallelogramm und Drachenviereck']),
                            ('der Raute', 'Parallelogramm und Drachenviereck', ['Rechteck und Quadrat', 'Parallelogramm und gleichschenkliges Trapez', 'Rechteck und Drachenviereck'])])
        return B_.A(f'Im Haus der Vierecke stehen direkt über {x} zwei Vierecke. Welche?', r, f,
                    f'Direkt darüber stehen die nächst allgemeineren Vierecke: {r}.', 'Welche Symmetrie verliert das Viereck, wenn man eine Bedingung weglässt?')

    def v_treff(R, B_, art=None):
        paare = [(a, b) for a in _VI for b in _VI if a < b and not _ist(a, b) and not _ist(b, a) and _treffen(a, b)
                 and {a, b} not in ({'Drachenviereck', 'Parallelogramm'}, {'Drachenviereck', 'gleichschenkliges Trapez'})]
        a, b = R.choice(paare)
        oft(('treffen', a, b))
        t = _treffen(a, b)
        f = R.sample([v for v in _VI if v != t and v not in (a, b)], 3)
        return B_.A(f'Ein Viereck ist {_ein(a)} und zugleich {_ein(b)}. Welches Viereck ist es sicher?', t, f,
                    f'Es hat die Symmetrien beider Vierecke. Im Haus der Vierecke steht darunter als allgemeinstes Viereck {_ein(t)}.',
                    'Suche das Viereck, das unter beiden steht – das höchste davon.', art=art, pruef=lambda x: x == t)

    def v_treff3(R, B_):
        return v_treff(R, B_, art='pruefung')

    def v_nur(R, B_):
        x, y, r, f = R.choice([
            ('jede Raute', 'jedes Parallelogramm', 'mindestens zwei Symmetrieachsen', ['Punktsymmetrie', 'gegenüberliegende Seiten parallel', 'vier rechte Winkel']),
            ('jedes Rechteck', 'jedes Parallelogramm', 'vier rechte Winkel', ['Punktsymmetrie', 'gegenüberliegende Seiten gleich lang', 'vier gleich lange Seiten']),
            ('jedes Quadrat', 'jedes Rechteck', 'vier gleich lange Seiten', ['vier rechte Winkel', 'Punktsymmetrie', 'gegenüberliegende Seiten parallel'])])
        return B_.A(f'Welche Eigenschaft hat {x}, aber nicht {y}?', r, f,
                    f'{r[0].upper() + r[1:]}: Das gilt für {x}, aber nicht für {y}. Die anderen Eigenschaften haben entweder beide oder keines sicher.',
                    'Prüfe jede Eigenschaft für beide Vierecke.')

    def v_zahl3(R, B_):
        frage, anz, liste = R.choice([('zugleich achsensymmetrisch und punktsymmetrisch', 3, 'Quadrat, Rechteck, Raute'),
                                      ('achsensymmetrisch, aber nicht punktsymmetrisch', 2, 'Drachenviereck, gleichschenkliges Trapez'),
                                      ('punktsymmetrisch, aber nicht achsensymmetrisch', 1, 'Parallelogramm (wenn es weder Rechteck noch Raute ist)')])
        return B_.Z(f'Quadrat, Rechteck, Raute, Parallelogramm, Drachenviereck, gleichschenkliges Trapez (jeweils ohne Spezialfälle): Wie viele davon sind {frage}?', anz, str(anz),
                    f'{liste} – also {anz}.', 'Nutze die Tabelle: Achsen und Punktsymmetrie je Viereck.')

    def f_gegen(R, B_):
        return B_.A('Tim behauptet: „Jedes Viereck mit genau zwei Symmetrieachsen ist ein Rechteck.“ Welches Viereck zeigt, dass Tim nicht recht hat?',
                    'eine Raute, die kein Quadrat ist', ['ein Quadrat', 'ein Parallelogramm, das kein Rechteck ist', 'ein Drachenviereck, das keine Raute ist'],
                    'Eine Raute (kein Quadrat) hat genau zwei Symmetrieachsen – die Diagonalen – ist aber kein Rechteck. Ein Quadrat hat vier Achsen.',
                    'Suche ein Viereck mit genau zwei Achsen, das keine rechten Winkel hat.', art='pruefung')

    def f_dp(R, B_):
        return B_.A('Ein Viereck ist ein Drachenviereck und zugleich ein Parallelogramm. Welches Viereck ist es sicher?', 'Raute',
                    ['Quadrat', 'Rechteck', 'gleichschenkliges Trapez'],
                    'Im Haus der Vierecke steht unter Drachenviereck und Parallelogramm die Raute. Ein Quadrat wäre möglich, ist aber nicht sicher.',
                    'Welches Viereck steht direkt unter beiden?', art='pruefung')

    def f_knobel(R, B_):
        return B_.A('Ein Viereck ist ein gleichschenkliges Trapez und zugleich ein Drachenviereck. Welches Viereck ist es?', 'Quadrat',
                    ['Raute', 'Rechteck', 'Parallelogramm'],
                    'Es braucht eine Achse durch zwei Ecken (Drachen) und eine durch zwei Seitenmitten (Trapez). Unter beiden steht im Haus der Vierecke nur das Quadrat.',
                    'Verfolge im Haus der Vierecke beide Vierecke nach unten, bis sie sich treffen.', art='knobel')

    return Karte(e, 'symmetrie', 'Symmetrie und Eigenschaften', 'Symmetrische Vierecke ordnen',
                 {1: [v_beschr, v_wahr, v_zahl], 2: [v_falsch, v_bild, v_ueber, v_wahr, v_ort, v_beschr, v_treff], 3: [v_treff3, v_nur, v_zahl3, v_falsch]},
                 fest3=[f_gegen, f_dp, f_knobel])


def luecken():
    return [_ms_karte(), _wh_karte(), _vo_karte()]


_LUECKEN_QUELLE = ('LehrplanPLUS Gymnasium Bayern, M7 2.1 (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik): Mittelsenkrechte, Lote und '
                   'Winkelhalbierende konstruieren und das Vorgehen beschreiben; Abstandsprobleme; symmetrische Vierecke ordnen. Prüfungsvorbilder (Typ und Niveau, '
                   'eigene Zahlen): Bayerischer Mathematik-Test 8 (ISB) 2024 A4b, 2019 A4, 2022 A1, 2014 B, 2023 A3.')
_LUECKEN_OFFEN = ['Achtzehnte Runde (luecken-kl7): neue Lernkarten mittelsenkrechte, winkelhalbierende (nach punktspiegelung) und vierecke_ordnen (nach symmetrie), alle Pflicht '
                  '(LehrplanPLUS M7 2.1). Konstruieren mit Zirkel und Lineal kann das Kind in der App nicht; geprüft werden Eigenschaften, Konstruktionsschritte (Auswahl) '
                  'und Abstandsprobleme im Koordinatensystem ohne schräge Längen (Pythagoras kommt erst später).']


# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Klasse 7, siehe _durchsicht_kl7.py) ----
from _durchsicht_kl7 import Durchsicht, durchsicht_datei  # noqa: E402

DS = Durchsicht('abbildungen.kongruenz', 19_7_3)
# achsenspiegelung: Aufgaben spiegeln an y = x und y = −x; die Karte zeigte nur senkrechte Achsen → Schritt ergänzt
DS.karte('achsenspiegelung', 'Schritt „Spiegeln an y = x: x und y tauschen“ ergänzt (Aufgaben ab Stufe 2 nutzen ihn).',
         schritte=lambda alt: alt + [{'text': "An der Geraden y = x tauschen x und y die Plätze: P'(3 | 4).",
                                      'bild': {'typ': 'koordinaten', 'x': [-1, 5], 'y': [-1, 5], 'graphen': [{'art': 'linear', 'm': 1, 't': 0, 'name': 'y = x'}],
                                               'punkte': [{'x': 4, 'y': 3, 'name': 'P'}, {'x': 3, 'y': 4, 'name': "P'"}], 'strecken': [[4, 3, 3, 4, 'gestrichelt']]}}])
DS.stufe('achsenspiegelung', 'Spiegle P(−5 | 1) an der Winkelhalbierenden y = x.', 2)   # gleicher Gedanke wie die Stufe-2-Aufgabe zu y = x
# punktspiegelung: zwei Stufe-3-Aufgaben sind „Spiegle P an Z“ wie Stufe 2
DS.stufe('punktspiegelung', 'Spiegle P(−1 | −6) am Punkt Z(1 | 3).', 2)
DS.stufe('punktspiegelung', 'Spiegle P(−7 | 2) am Punkt Z(−2 | 1).', 2)
# verschiebung: „erst …, dann … – wohin kommt P?“ ist zweimal derselbe Schritt (Stufe 2), dreimal in Stufe 3
for _t in ['P(−4 | −7) wird erst mit (1 | −2), dann mit (−2 | −6) verschoben. Wohin kommt P?',
           'P(−1 | 3) wird erst mit (−5 | 2), dann mit (6 | −2) verschoben. Wohin kommt P?',
           'P(−4 | 4) wird erst mit (5 | 2), dann mit (6 | 1) verschoben. Wohin kommt P?']:
    DS.stufe('verschiebung', _t, 2)
# symmetrie: Aufgaben fragen nach dem kleinsten Drehwinkel (360° : n); die Karte erklärte Drehsymmetrie nicht → Schritt und Wort ergänzt
_sechs = {f'_{i}': [round(2 * math.cos(math.radians(60 * i)), 3), round(2 * math.sin(math.radians(60 * i)), 3)] for i in range(6)}
DS.karte('symmetrie', 'Schritt zur Drehsymmetrie (kleinster Drehwinkel 360° : n) mit Sechseck ergänzt; Wort „drehsymmetrisch“ erklärt.',
         woerter=lambda alt: alt + [['drehsymmetrisch', 'passt nach einer Drehung um weniger als 360° wieder auf sich']],
         schritte=lambda alt: alt + [{'text': 'Ein regelmäßiges Sechseck passt schon nach 360° : 6 = 60° wieder: ⟦drehsymmetrisch⟧.',
                                      'bild': {'typ': 'figur', 'punkte': {**_sechs, 'M': [0, 0]}, 'flaeche': [f'_{i}' for i in range(6)],
                                               'linien': [[f'_{i}', f'_{(i + 1) % 6}'] for i in range(6)] + [['M', '_0', '', 'gestrichelt'], ['M', '_1', '', 'gestrichelt']],
                                               'winkel': [['M', '_0', '_1', '60°']]}}])
# eigenschaften: „Welche Abbildung ist es?“ steht dreimal in Stufe 3 genauso wie in Stufe 2 → Stufe 2
DS.stufe('eigenschaften', "Das Dreieck ABC wird auf A'B'C' (gestrichelt) abgebildet. Welche Abbildung ist es?", 2, enthaelt='"s": 3', anzahl=3)
# ---- DURCHSICHT ENDE ----


# ---- STUFEN (Zwanzigste Runde: echte Stufe 3 und Knobel-Bordkarten, siehe _stufen_kl7.py) ----
# Vorbilder (Typ und Niveau, eigene Zahlen): Jahrgangsstufentest/BMT8 (ISB) – Bildpunkt einer Figur nach Spiegelung/Verschiebung angeben,
# Viereck aus Koordinaten bestimmen, Punkt gleich weit von drei Punkten; Knobel nach der Art von Känguru 7/8 und Mathematik-Olympiade (Billard, Springer, Zeigerwinkel).
from _stufen_kl7 import Stufen, stufen_datei  # noqa: E402

ST = Stufen('abbildungen.kongruenz', 20_7_3)
_HP = 'Trage die x- und die y-Koordinate ein.'
def _P(text, name, xy, c, w, h):
    return ST.L(text, name + '(□ | □)', xy, c, w, h, _HP)
# achsenspiegelung
ST.leiter('achsenspiegelung', 'An x- oder y-Achse spiegeln; erkennen, welche Koordinate das Vorzeichen wechselt.',
          'An waagrechten und senkrechten Achsen sowie der Winkelhalbierenden spiegeln; Urbild zurückrechnen; Sachsituation.',
          'Achse aus Punkt und Bild finden, Achse einer Raute, Bild eines zweiten Punkts, Hintereinanderausführung, Fehler deuten, Prüfungsaufgabe mit Dreieck.')
ST.regel('achsenspiegelung', 1, 'y-Achse', 'direkt')
ST.regel('achsenspiegelung', 1, 'x-Achse', 'direkt')
ST.regel('achsenspiegelung', 2, 'Winkelhalbierenden', 'mehrschritt')
ST.regel('achsenspiegelung', 2, 'parallel zur x-Achse)', 'mehrschritt')
ST.regel('achsenspiegelung', 2, 'senkrecht zur x-Achse)', 'mehrschritt')
ST.regel('achsenspiegelung', 3, 'y = −x', 'transfer')
ST.regel('achsenspiegelung', 3, 'senkrecht zur x-Achse auf', 'rueckwaerts')
ST.regel('achsenspiegelung', 3, 'parallel zur x-Achse auf', 'rueckwaerts')
ST.regel('achsenspiegelung', 3, 'Raute', 'verknuepfen')
ST.regel('achsenspiegelung', 3, 'Wohin wird B', 'transfer')
ST.regel('achsenspiegelung', 3, 'erst an der x-Achse', 'verknuepfen')
ST.regel('achsenspiegelung', 3, 'P(x |', 'rueckwaerts')
ST.neu('achsenspiegelung', 1, 'erkennen', ST.A('Ein Punkt wird an der x-Achse gespiegelt. Welche Koordinate ändert ihr Vorzeichen?', 'die y-Koordinate',
                                               ['die x-Koordinate', 'beide Koordinaten', 'keine von beiden'],
                                               'Die x-Achse ist waagrecht. Der Bildpunkt liegt genau gegenüber, also gleich weit rechts, aber auf der anderen Seite der Achse: Nur die y-Koordinate wechselt das Vorzeichen.',
                                               'Wohin wandert ein Punkt, wenn man an einer waagrechten Linie spiegelt?'))
ST.neu('achsenspiegelung', 2, 'einkleidung', _P('Auf einer Karte fließt ein gerader Fluss entlang der y-Achse. Ein Haus steht bei H(3 | 5). Genau gegenüber, gleich weit vom Fluss entfernt, steht eine Scheune. Wo?',
                                                'S', [-3, 5], ['-3', '5'], 'Die Scheune ist das Spiegelbild des Hauses an der y-Achse: S(−3 | 5).', 'An welcher Achse wird gespiegelt?'))
ST.neu('achsenspiegelung', 2, 'umkehr', _P('Nach einer Spiegelung an der y-Achse liegt der Bildpunkt bei P\'(−2 | 7). Wo lag P?', 'P', [2, 7], ['2', '7'],
                                           'Spiegelt man P\' zurück an der y-Achse, erhält man P(2 | 7). Probe: P(2 | 7) an der y-Achse ergibt (−2 | 7) ✓.', 'Spiegle einfach zurück.'))
ST.neu('achsenspiegelung', 3, 'fehler', ST.A('Jemand spiegelt P(4 | −3) an der x-Achse und erhält P\'(−4 | −3). Was stimmt?', 'Falsch: Er hat an der y-Achse gespiegelt; richtig ist P\'(4 | 3).',
                                             ['Richtig gespiegelt.', 'Falsch: Richtig ist P\'(−4 | 3).', 'Falsch: Richtig ist P\'(3 | −4).'],
                                             'An der x-Achse bleibt x gleich und y wechselt das Vorzeichen: P\'(4 | 3). Wechselt x das Vorzeichen, ist an der y-Achse gespiegelt worden.',
                                             'Welche Koordinate darf sich bei der x-Achse ändern?'))
ST.neu('achsenspiegelung', 3, 'pruefung', _P('Das Dreieck A(1 | 1), B(5 | 1), C(2 | 4) wird an der senkrechten Geraden durch (6 | 0) gespiegelt. Gib C\' an.', 'C\'', [10, 4], ['6 + (6 - 2)', '4'],
                                             'C liegt 4 Einheiten links von der Achse (6 − 2 = 4). C\' liegt 4 Einheiten rechts davon: x = 10. Die y-Koordinate bleibt 4. C\'(10 | 4).',
                                             'Wie weit ist C von der Achse entfernt?'))
ST.knobel('achsenspiegelung', _P('P(1 | 2) wird abwechselnd gespiegelt: zuerst an der x-Achse, dann an der y-Achse, dann wieder an der x-Achse usw. Insgesamt sind es 2025 Spiegelungen. Wo liegt der Punkt am Ende?',
                                 'P', [1, -2], ['1', '-2'],
                                 'Verfolge die ersten Schritte: (1 | 2) → x-Achse (1 | −2) → y-Achse (−1 | −2) → x-Achse (−1 | 2) → y-Achse (1 | 2). '
                                 'Nach 4 Spiegelungen ist der Punkt wieder am Start. 2025 = 4 · 506 + 1. Nach 2024 Spiegelungen ist er also bei (1 | 2), die 2025. ist eine Spiegelung an der x-Achse: (1 | −2).',
                                 'Rechne die ersten Spiegelungen aus und suche eine Regelmäßigkeit.'))
ST.knobel('achsenspiegelung', ST.Z('Eine Billardkugel liegt bei A(1 | 3) und soll über die Bande (die x-Achse) genau zur Kugel B(7 | 1) rollen. Sie prallt so ab wie ein Lichtstrahl an einem Spiegel. An welcher x-Stelle trifft sie die Bande?',
                                   5.5, '1 + 6 * 3 / 4',
                                   'Denke den Weg nach dem Abprallen hinter der Bande weiter: Er führt dann geradlinig zum Spiegelbild B\'(7 | −1). '
                                   'Von A(1 | 3) nach B\'(7 | −1) geht es 6 nach rechts und 4 nach unten. Bis zur Bande (y = 0) sind es 3 der 4 Einheiten nach unten, also 3/4 des Weges: 6 · 3/4 = 4,5 nach rechts. 1 + 4,5 = 5,5.',
                                   'Einfallswinkel gleich Ausfallswinkel. Wie sieht der Weg aus, wenn man ihn hinter der Bande weiterdenkt?'))
# punktspiegelung
ST.leiter('punktspiegelung', 'Am Ursprung spiegeln: beide Vorzeichen wechseln.',
          'An einem beliebigen Zentrum spiegeln, Urbild zurückrechnen, Dreieck spiegeln, Sachsituation Drehkreuz.',
          'Zentrum aus Punkt und Bild, vierte Ecke und Zentrum eines Parallelogramms, zwei Spiegelungen, Begründung, Fehler, Prüfungsaufgabe mit Fläche.')
ST.regel('punktspiegelung', 1, 'Ursprung', 'direkt')
ST.regel('punktspiegelung', 2, 'am Punkt Z', 'mehrschritt')
ST.regel('punktspiegelung', 3, 'Gib das Zentrum an', 'rueckwaerts')
ST.regel('punktspiegelung', 3, 'Gib das Zentrum Z an', 'rueckwaerts')
ST.regel('punktspiegelung', 3, 'vierte Ecke', 'verknuepfen')
ST.regel('punktspiegelung', 3, 'Symmetriezentrum', 'verknuepfen')
ST.regel('punktspiegelung', 3, 'Verschiebungspfeil', 'transfer')
ST.neu('punktspiegelung', 1, 'erkennen', ST.A('Was passiert mit den Koordinaten bei einer Punktspiegelung am Ursprung?', 'Beide wechseln das Vorzeichen.',
                                              ['Nur x wechselt das Vorzeichen.', 'Nur y wechselt das Vorzeichen.', 'x und y werden vertauscht.'],
                                              'Der Bildpunkt liegt genau gegenüber: gleich weit vom Ursprung, aber in der Gegenrichtung. Aus (x | y) wird (−x | −y).', 'Probiere es mit P(2 | 1).'))
ST.neu('punktspiegelung', 1, 'direkt', _P('Spiegle Q(−3 | 0) am Ursprung.', 'Q\'', [3, 0], ['3', '0'], 'Beide Vorzeichen wechseln: Q\'(3 | 0). Die 0 bleibt 0.', 'Was passiert mit −3, was mit 0?'))
ST.neu('punktspiegelung', 2, 'umkehr', _P('Nach einer Spiegelung am Punkt Z(1 | 2) liegt der Bildpunkt bei P\'(4 | −1). Wo lag P?', 'P', [-2, 5], ['2 * 1 - 4', '2 * 2 - (-1)'],
                                          'Von P\' nach Z: 3 nach links, 3 nach oben. Denselben Weg noch einmal: P(−2 | 5). Probe: Z ist die Mitte von (−2 | 5) und (4 | −1) ✓.',
                                          'Spiegle P\' an Z zurück.'))
ST.neu('punktspiegelung', 2, 'einkleidung', _P('Ein Drehkreuz hat die Mitte M(3 | 3). Ein Arm endet bei (5 | 6). Der gegenüberliegende Arm ist gleich lang und zeigt genau in die Gegenrichtung. Wo endet er?',
                                               'E', [1, 0], ['2 * 3 - 5', '2 * 3 - 6'],
                                               'Von M zum Armende: 2 nach rechts, 3 nach oben. Gegenrichtung: 2 nach links, 3 nach unten: E(1 | 0).', 'Das ist eine Punktspiegelung an M.'))
ST.neu('punktspiegelung', 2, 'mehrschritt', _P('Das Dreieck A(1 | 1), B(3 | 1), C(1 | 4) wird am Punkt Z(4 | 2) gespiegelt. Gib B\' an.', 'B\'', [5, 3], ['2 * 4 - 3', '2 * 2 - 1'],
                                               'Von B nach Z: 1 nach rechts, 1 nach oben. Noch einmal: B\'(5 | 3).', 'Gehe von B zu Z und denselben Weg weiter.'))
ST.neu('punktspiegelung', 2, 'umkehr', _P('Ein Punkt wird am Ursprung gespiegelt und landet bei (−6 | 2). Wo lag er vorher?', 'P', [6, -2], ['6', '-2'],
                                          'Am Ursprung zurückspiegeln: beide Vorzeichen wechseln. P(6 | −2).', 'Spiegle zurück.'))
ST.neu('punktspiegelung', 3, 'begruenden', ST.A('Warum ist jedes Parallelogramm punktsymmetrisch?', 'Seine Diagonalen halbieren sich; am Schnittpunkt gespiegelt fällt jede Ecke auf die gegenüberliegende.',
                                                ['Weil es vier Ecken hat.', 'Weil benachbarte Seiten senkrecht aufeinander stehen.', 'Weil es eine Symmetrieachse hat.'],
                                                'Im Parallelogramm halbieren sich die Diagonalen gegenseitig. Der Schnittpunkt ist also die Mitte von [AC] und von [BD]: A geht auf C, B auf D – und damit die ganze Figur auf sich selbst.',
                                                'Was ist der Schnittpunkt der Diagonalen für die Strecken [AC] und [BD]?'))
ST.neu('punktspiegelung', 3, 'fehler', ST.A('Jemand spiegelt P(5 | 1) am Punkt Z(2 | 3) und rechnet: P\'(2 − 5 | 3 − 1) = P\'(−3 | 2). Was stimmt?',
                                            'Falsch: Von Z aus muss es noch einmal den Weg von P nach Z gehen; richtig ist P\'(−1 | 5).',
                                            ['Richtig gerechnet.', 'Falsch: Richtig ist P\'(7 | 4).', 'Falsch: Richtig ist P\'(−3 | −2).'],
                                            'Von P(5 | 1) nach Z(2 | 3): 3 nach links, 2 nach oben. Von Z aus noch einmal: (−1 | 5). Die Rechnung „Z − P“ ergibt nur den Weg, nicht den Bildpunkt.',
                                            'Ist Z die Mitte von P und (−3 | 2)?'))
ST.neu('punktspiegelung', 3, 'pruefung', ST.Z('Das Dreieck A(1 | 0), B(3 | 0), C(3 | 2) wird am Punkt Z(4 | 1) gespiegelt. Wie groß ist der Flächeninhalt des Vierecks ABA\'B\' (in Flächeneinheiten)?',
                                              4, '2 * 2',
                                              'A\'(7 | 2) und B\'(5 | 2). Das Viereck A(1 | 0), B(3 | 0), A\'(7 | 2), B\'(5 | 2) ist ein Parallelogramm: [AB] und [A\'B\'] sind waagrecht und je 2 lang, der Abstand ist 2. Fläche 2 · 2 = 4.',
                                              'Bestimme zuerst A\' und B\'.'))
ST.knobel('punktspiegelung', _P('Der Punkt P(0 | 0) wird abwechselnd an A(1 | 0) und an B(1 | 1) gespiegelt: zuerst an A, dann an B, dann wieder an A usw. Wo liegt er nach 10 Spiegelungen?',
                                'P', [0, 10], ['0', '5 * 2'],
                                'Schrittweise: (0 | 0) → an A (2 | 0) → an B (0 | 2) → an A (2 | −2) → an B (0 | 4). '
                                'Nach je zwei Spiegelungen ist der Punkt um 2 nach oben gewandert (zwei Punktspiegelungen ergeben eine Verschiebung um den doppelten Weg von A nach B). 10 Spiegelungen = 5 Paare: (0 | 10).',
                                'Rechne vier Spiegelungen aus und vergleiche die Lage nach der 2. und der 4.'))
ST.knobel('punktspiegelung', _P('Ein Punkt X wird an A(1 | 2) gespiegelt, sein Bild an B(4 | 2) und dieses Bild an C(4 | 5). Danach liegt der Punkt wieder genau bei X. Wo liegt X?',
                                'X', [1, 5], ['1', '5'],
                                'Die Spiegelungen an A und dann an B wirken zusammen wie eine Verschiebung um den doppelten Weg von A nach B, also um (6 | 0). '
                                'X + (6 | 0) muss an C auf X zurückgehen, also ist C die Mitte von X und X + (6 | 0): X liegt 3 links von C, also X(1 | 5). '
                                'Probe: (1 | 5) → an A (1 | −1) → an B (7 | 5) → an C (1 | 5) ✓.',
                                'Was bewirken die ersten beiden Spiegelungen zusammen?'))
# verschiebung
ST.leiter('verschiebung', 'Einen Punkt mit einem Pfeil verschieben; Eigenschaft der Verschiebung erkennen.',
          'Pfeil aus Punkt und Bild, zwei Verschiebungen nacheinander, Dreieck verschieben, Sachsituation Schiff.',
          'Ersatzpfeil, falscher Pfeil, Pfeil an anderem Punkt, unbekannter Pfeil rückwärts, Quadrat verschieben, Fehler, Parameter, Prüfungsaufgabe.')
ST.regel('verschiebung', 1, 'Verschiebe', 'direkt')
ST.regel('verschiebung', 2, 'Gib den Verschiebungspfeil an', 'umkehr')
ST.regel('verschiebung', 2, 'Wohin kommt P', 'mehrschritt')
ST.regel('verschiebung', 2, 'Dreieck', 'mehrschritt')
ST.regel('verschiebung', 2, 'Wohin wird B', 'mehrschritt')
ST.regel('verschiebung', 3, 'Welcher Pfeil ersetzt', 'verknuepfen')
ST.regel('verschiebung', 3, 'NICHT', 'begruenden')
ST.regel('verschiebung', 3, 'Ein anderer Pfeil', 'transfer')
ST.regel('verschiebung', 3, 'unbekannten Pfeil', 'rueckwaerts')
ST.regel('verschiebung', 3, 'Quadrat', 'verknuepfen')
ST.neu('verschiebung', 1, 'erkennen', ST.A('Welche Aussage passt zu einer Verschiebung?', 'Alle Punkte wandern mit demselben Pfeil.',
                                           ['Ein Punkt bleibt an seinem Platz.', 'Die Figur wird umgeklappt.', 'Die Figur wird um einen Punkt gedreht.'],
                                           'Bei einer Verschiebung bewegt sich jeder Punkt gleich weit in dieselbe Richtung. Kein Punkt bleibt fest (außer beim Nullpfeil).',
                                           'Denke an ein Buch, das über den Tisch geschoben wird.'))
ST.neu('verschiebung', 1, 'direkt', _P('Verschiebe Q(−2 | 5) um 4 nach rechts und 3 nach unten.', 'Q\'', [2, 2], ['-2 + 4', '5 - 3'],
                                       'x: −2 + 4 = 2, y: 5 − 3 = 2. Q\'(2 | 2).', 'Rechts heißt x größer, unten heißt y kleiner.'))
ST.neu('verschiebung', 2, 'einkleidung', _P('Ein Schiff startet im Hafen H(2 | 1) und fährt 5 km nach Osten und 3 km nach Norden (1 Einheit = 1 km, Osten = rechts, Norden = oben). Wo ist es dann?',
                                            'S', [7, 4], ['2 + 5', '1 + 3'], 'Verschiebung mit (5 | 3): S(7 | 4).', 'Schreibe die Fahrt als Pfeil.'))
ST.neu('verschiebung', 3, 'fehler', ST.A('Jemand soll P(2 | 5) mit v = (−3 | 1) verschieben und erhält P\'(5 | 4). Was stimmt?', 'Falsch: Er hat den Pfeil umgedreht; richtig ist P\'(−1 | 6).',
                                         ['Richtig verschoben.', 'Falsch: Richtig ist P\'(−6 | 5).', 'Falsch: Richtig ist P\'(−1 | 4).'],
                                         'Richtig: x: 2 + (−3) = −1, y: 5 + 1 = 6. Er hat stattdessen 3 addiert und 1 abgezogen – das ist der Gegenpfeil (3 | −1).', 'Rechne selbst nach.'))
ST.neu('verschiebung', 3, 'parameter', ST.Z('Der Punkt P(a | 3) wird mit v = (4 | −1) verschoben und landet auf der y-Achse. Wie groß ist a?', -4, '0 - 4',
                                            'Auf der y-Achse ist x = 0. Also a + 4 = 0 und a = −4. Probe: P(−4 | 3) → (0 | 2) ✓.', 'Welche x-Koordinate haben Punkte auf der y-Achse?'))
ST.neu('verschiebung', 3, 'pruefung', _P('Das Dreieck A(0 | 0), B(4 | 0), C(1 | 3) wird so verschoben, dass B auf B\'(6 | 2) fällt. Gib C\' an.', 'C\'', [3, 5], ['1 + 2', '3 + 2'],
                                         'Der Pfeil von B nach B\' ist (2 | 2). Derselbe Pfeil verschiebt C: C\'(3 | 5).', 'Bestimme zuerst den Verschiebungspfeil.'))
ST.knobel('verschiebung', ST.Z('Ein Springer im Schach zieht mit einem der Pfeile (±2 | ±1) oder (±1 | ±2). Wie viele Züge braucht er mindestens, um von (0 | 0) nach (4 | 4) zu kommen?', 4, '4',
                               'Jeder Zug ändert x + y um 1 oder 3, also um eine ungerade Zahl. Von 0 bis 8 braucht man eine gerade Anzahl ungerader Schritte. '
                               'Zwei Züge reichen nicht: Sie ändern x + y um höchstens 6. Also mindestens 4 Züge. Es geht mit 4: (2 | 1) + (1 | 2) + (2 | −1) + (−1 | 2) = (4 | 4).',
                               'Beobachte, wie sich die Summe x + y bei jedem Zug ändert.'))
ST.knobel('verschiebung', ST.L('Ein Roboter fährt nur mit den Pfeilen u = (2 | 1) und w = (−1 | 3), jeden beliebig oft, aber nie rückwärts. Er startet bei (0 | 0) und will nach (7 | 14). Wie oft fährt er u, wie oft w?',
                               '□-mal u und □-mal w', [5, 3], ['5', '3'],
                               'Fährt er a-mal u und b-mal w, landet er bei (2a − b | a + 3b). Es muss 2a − b = 7 sein, also b = 2a − 7. Probiere: a = 4 → b = 1, y = 4 + 3 = 7 (zu wenig); '
                               'a = 5 → b = 3, y = 5 + 9 = 14 ✓; a = 6 → b = 5, y = 21 (zu viel). Also 5-mal u und 3-mal w: (10 | 5) + (−3 | 9) = (7 | 14).',
                               'Schreibe auf, wo er nach a Fahrten mit u und b Fahrten mit w ist, und probiere.'))
# drehung
ST.leiter('drehung', 'Um O um 90°, 180°, 270° drehen; die Koordinatenregel für 90° erkennen.',
          'Drehwinkel aus Punkt und Bild, Drehung im Uhrzeigersinn, Sachsituation Riesenrad.',
          'Drehen um ein anderes Zentrum, Bild einer Geraden, Fehler mit der Drehrichtung, Urbild, Mehrfachdrehung, Parameter, Prüfungsaufgabe mit Quadrat.')
ST.regel('drehung', 1, 'Drehe', 'direkt')
ST.regel('drehung', 2, 'Um welchen Winkel', 'umkehr')
ST.regel('drehung', 2, 'Drehe', 'mehrschritt')
ST.regel('drehung', 3, 'Drehe', 'verknuepfen')
ST.regel('drehung', 3, 'Gerade g', 'begruenden')
ST.regel('drehung', 3, 'Jemand gibt', 'fehler')
ST.regel('drehung', 3, 'Wo lag P', 'rueckwaerts')
ST.regel('drehung', 3, 'zweimal', 'verknuepfen')
ST.neu('drehung', 1, 'erkennen', ST.A('Bei einer Drehung um O um 90° gegen den Uhrzeigersinn wird aus P(x | y) der Punkt …', 'P\'(−y | x)', ['P\'(y | −x)', 'P\'(−x | −y)', 'P\'(y | x)'],
                                      'Probe mit (1 | 0): Er wandert auf die positive y-Achse nach (0 | 1). Das passt nur zu (−y | x).', 'Teste die Regeln mit dem Punkt (1 | 0).'))
ST.neu('drehung', 1, 'direkt', _P('Drehe P(4 | 0) um O um 180°.', 'P\'', [-4, 0], ['-4', '0'], 'Eine halbe Drehung bringt P genau auf die Gegenseite: P\'(−4 | 0).', 'Wo ist die Gegenseite?'))
ST.neu('drehung', 2, 'einkleidung', _P('Ein Riesenrad dreht sich um seine Mitte M(0 | 0) (1 Einheit = 1 m). Eine Gondel ist ganz unten bei G(0 | −10). Wo ist sie nach einer Vierteldrehung gegen den Uhrzeigersinn?',
                                       'G\'', [10, 0], ['10', '0'], 'Von ganz unten gegen den Uhrzeigersinn um 90° kommt die Gondel nach ganz rechts: G\'(10 | 0).',
                                       'Stell dir die Bewegung vor: unten → rechts → oben → links.'))
ST.neu('drehung', 3, 'parameter', ST.Z('P(a | 2) wird um O um 90° gegen den Uhrzeigersinn gedreht. Der Bildpunkt liegt auf der waagrechten Geraden durch (0 | 5). Wie groß ist a?', 5, '5',
                                       'Bei 90° gegen den Uhrzeigersinn wird aus (a | 2) der Punkt (−2 | a). Er soll die y-Koordinate 5 haben: a = 5.', 'Wende die Regel für 90° an.'))
ST.neu('drehung', 3, 'pruefung', _P('Das Quadrat A(1 | 1), B(4 | 1), C(4 | 4), D(1 | 4) wird um A um 90° gegen den Uhrzeigersinn gedreht. Gib C\' an.', 'C\'', [-2, 4], ['1 - 3', '1 + 3'],
                                    'Von A nach C: 3 nach rechts, 3 nach oben. Um 90° gedreht: 3 nach links, 3 nach oben. C\'(−2 | 4).', 'Drehe den Weg von A nach C.'))
ST.knobel('drehung', ST.Z('Wie groß ist der kleinere Winkel zwischen Stunden- und Minutenzeiger einer Uhr um 4:20 Uhr (in Grad)?', 10, '4 * 30 + 20 * 0.5 - 20 * 6',
                          'Der Minutenzeiger dreht sich in 60 Minuten um 360°, also 6° pro Minute: Bei 20 Minuten steht er bei 120° (auf der 4). '
                          'Der Stundenzeiger dreht sich in 60 Minuten um 30°, also 0,5° pro Minute. Um 4:00 steht er bei 120°, 20 Minuten später bei 130°. Unterschied: 10°.',
                          'Der Stundenzeiger steht nicht genau auf der 4.'))
ST.knobel('drehung', _P('P(5 | 1) wird 2026-mal hintereinander um O um 90° gegen den Uhrzeigersinn gedreht. Wo liegt P am Ende?', 'P', [-5, -1], ['-5', '-1'],
                        'Vier Vierteldrehungen sind eine volle Umdrehung, danach ist P wieder am Start. 2026 = 4 · 506 + 2. Es bleiben 2 Vierteldrehungen, also 180°: P(−5 | −1).',
                        'Nach wie vielen Drehungen ist P wieder am Start?'))
# symmetrie
ST.leiter('symmetrie', 'Symmetrieachsen bekannter Vierecke und des Sechsecks zählen.',
          'Buchstaben, Punktsymmetrie von Rechteck und Trapez, kleinster Drehwinkel regelmäßiger Vielecke, Eckenzahl aus dem Drehwinkel, Windrad.',
          'Buchstaben mit Symmetrie-Kombinationen, Figur aus Eigenschaften, Gegenbeispiel deckungsgleich, Drehwinkel-Vielfache, Verkehrsschild, zusammengesetzte Figur.')
ST.regel('symmetrie', 1, 'hat ein Quadrat', 'direkt')
ST.regel('symmetrie', 1, 'Sechseck', 'direkt')
ST.regel('symmetrie', 1, 'Trapez', 'erkennen')
ST.regel('symmetrie', 1, 'Raute', 'erkennen')
ST.regel('symmetrie', 2, 'Großbuchstabe', 'darstellung')
ST.regel('symmetrie', 2, 'punktsymmetrisch', 'mehrschritt')
ST.regel('symmetrie', 2, 'kleinsten Winkel', 'mehrschritt')
ST.regel('symmetrie', 2, 'Parallelogramm', 'darstellung')
ST.regel('symmetrie', 3, 'Großbuchstabe', 'verknuepfen')
ST.regel('symmetrie', 3, 'Welche Figur', 'rueckwaerts')
ST.regel('symmetrie', 3, 'Zwei Vierecke', 'begruenden')
ST.regel('symmetrie', 3, 'Logo', 'begruenden')
ST.regel('symmetrie', 3, 'Verkehrsschild', 'transfer')
ST.regel('symmetrie', 3, 'Zwei gleich große Quadrate', 'transfer')
ST.neu('symmetrie', 2, 'umkehr', ST.Z('Ein regelmäßiges Vieleck fällt nach einer Drehung um 40° um seinen Mittelpunkt zum ersten Mal auf sich selbst. Wie viele Ecken hat es?', 9, '360 / 40',
                                     'Beim kleinsten Drehwinkel rückt jede Ecke auf die nächste. 360° : 40° = 9 Ecken.', 'Wie oft passt 40° in eine volle Drehung?'))
ST.neu('symmetrie', 2, 'einkleidung', ST.Z('Ein Windrad hat drei gleiche Flügel. Um welchen kleinsten Winkel muss es sich drehen, damit es wieder genau gleich aussieht?', 120, '360 / 3',
                                          'Drei gleiche Flügel teilen die volle Drehung in drei gleiche Teile: 360° : 3 = 120°.', 'Ein Flügel muss auf den nächsten rücken.'))
ST.knobel('symmetrie', ST.Z('In einem 4 × 4-Quadrat aus 16 Kästchen ist nur das Kästchen links oben schwarz. Wie viele Kästchen musst du mindestens zusätzlich schwarz färben, damit das Muster genau 4 Symmetrieachsen hat?',
                            3, '4 - 1',
                            'Mit 4 Achsen muss das Muster alle Symmetrien des Quadrats haben: die beiden Mittellinien und die beiden Diagonalen. '
                            'Spiegelt man die Ecke links oben an diesen Achsen, erhält man alle vier Ecken. Alle vier Eckkästchen müssen also schwarz sein – 3 zusätzlich. '
                            'Das Muster aus den vier Ecken hat tatsächlich alle 4 Achsen.',
                            'Wohin wandert das schwarze Kästchen bei jeder Spiegelung, die das Muster haben soll?'))
ST.knobel('symmetrie', ST.Z('Der kleinste Drehwinkel, der eine Figur auf sich selbst abbildet, ist 72°. Außerdem hat sie mindestens eine Symmetrieachse. Wie viele Symmetrieachsen hat sie genau?', 5, '360 / 72',
                            'Dreht man die Figur um 72°, wird auch ihre Achse mitgedreht – und muss wieder eine Achse sein. So entstehen Achsen im Abstand von 72°: 0°, 72°, 144°, 216° (= 36°), 288° (= 108°) – fünf verschiedene Geraden. '
                            'Mehr gibt es nicht: Zwei Achsen, die einen Winkel θ bilden, ergeben zusammen eine Drehung um 2θ, und die muss ein Vielfaches von 72° sein. '
                            'Also liegen alle Achsen im Abstand von Vielfachen von 36° – genau diese fünf. Beispiel: das regelmäßige Fünfeck.',
                            'Was passiert mit einer Symmetrieachse, wenn man die Figur um 72° dreht?'))
# parkett
ST.leiter('parkett', 'Winkel an einer Ecke addieren; Innenwinkel regelmäßiger Vielecke erkennen.',
          'Lücke an einer Ecke berechnen, Innenwinkel aus der Anzahl, Fliesen im Bad.',
          'Fehlende Vielecke ergänzen, Eckenzahl aus dem Innenwinkel, gemischte Ecken prüfen und begründen, Fußball als Anwendung.')
ST.regel('parkett', 1, 'An einer Ecke', 'direkt')
ST.regel('parkett', 2, 'Um eine Ecke passen', 'umkehr')
ST.regel('parkett', 2, '', 'mehrschritt')
ST.regel('parkett', 3, 'Wie viele gleichseitige Dreiecke', 'verknuepfen')
ST.regel('parkett', 3, 'ein weiteres', 'rueckwaerts')
ST.regel('parkett', 3, 'Lässt sich', 'begruenden')
ST.regel('parkett', 3, 'Wie viele Ecken hat es', 'rueckwaerts')
ST.regel('parkett', 3, 'Zwölfecke', 'verknuepfen')
ST.regel('parkett', 3, 'Zwölfeck zusammen', 'verknuepfen')
ST.regel('parkett', 3, 'Warum', 'begruenden')
ST.neu('parkett', 1, 'erkennen', ST.A('Welches regelmäßige Vieleck hat Innenwinkel von 120°?', 'das Sechseck', ['das Fünfeck', 'das Achteck', 'das Quadrat'],
                                     'Regelmäßiges Sechseck: 120°. Fünfeck 108°, Achteck 135°, Quadrat 90°.', 'Drei davon passen genau um eine Ecke.'))
ST.neu('parkett', 2, 'einkleidung', ST.Z('Ein Bad wird mit regelmäßigen sechseckigen Fliesen (Innenwinkel 120°) lückenlos gefliest. Wie viele Fliesen treffen an jeder inneren Ecke zusammen?', 3, '360 / 120',
                                        'Um eine Ecke sind 360°. 360° : 120° = 3 Fliesen.', 'Wie oft passt 120° in 360°?'))
ST.neu('parkett', 3, 'transfer', ST.Z('Ein Fußball ist aus regelmäßigen Fünfecken (108°) und Sechsecken (120°) genäht. An jeder Ecke treffen ein Fünfeck und zwei Sechsecke zusammen. Wie groß ist die Winkelsumme an einer Ecke?',
                                      348, '108 + 2 * 120',
                                      '108° + 2 · 120° = 348°. Das sind 12° weniger als 360° – deshalb lassen sich die Flicken nicht flach legen, sondern wölben sich zu einer Kugel.',
                                      'Addiere die drei Winkel.'))
ST.knobel('parkett', ST.Z('Der Innenwinkel eines regelmäßigen n-Ecks ist 180° − 360° : n. An einer Ecke kommen genau drei regelmäßige Vielecke lückenlos zusammen: ein Dreieck, ein Zehneck und ein drittes. Wie viele Ecken hat das dritte?',
                          15, '360 / (180 - (360 - 60 - 144))',
                          'Dreieck 60°, Zehneck 180° − 36° = 144°. Zusammen 204°. Für das dritte bleiben 360° − 204° = 156°. '
                          'Es muss gelten 180° − 360° : n = 156°, also 360° : n = 24° und n = 15. Probe: 180° − 24° = 156° ✓.',
                          'Berechne zuerst, wie viel Grad für das dritte Vieleck übrig bleiben.'))
ST.knobel('parkett', ST.Z('Auf wie viele verschiedene Arten kann man eine Ecke lückenlos nur mit gleichseitigen Dreiecken (60°) und Quadraten (90°) auslegen, wenn es nur auf die Anzahlen ankommt?',
                          3, '3',
                          'Gesucht sind Anzahlen a (Dreiecke) und b (Quadrate) mit 60a + 90b = 360. Probiere b: b = 0 → a = 6; b = 1 → 60a = 270, keine ganze Zahl; '
                          'b = 2 → a = 3; b = 3 → 60a = 90, keine ganze Zahl; b = 4 → a = 0. Also drei Möglichkeiten: 6 + 0, 3 + 2, 0 + 4.',
                          'Gehe die möglichen Anzahlen von Quadraten der Reihe nach durch.'))
# eigenschaften
ST.leiter('eigenschaften', 'Längen und Winkel bleiben erhalten; richtige Aussage erkennen.',
          'Abbildung aus Bild und Urbild bestimmen, Umlaufsinn bei Drehung und Spiegelung, Flächeninhalt bleibt.',
          'Zwei Spiegelungen als Verschiebung oder Drehung, Umlaufsinn umkehren, Fixpunkte, Fehler, Spiegeluhr, Prüfungsaufgabe mit zwei Abbildungen.')
ST.regel('eigenschaften', 1, 'Welche Aussage', 'erkennen')
ST.regel('eigenschaften', 2, 'Welche Aussage', 'mehrschritt')
ST.regel('eigenschaften', 2, 'Welche Abbildung ist es', 'darstellung')
ST.regel('eigenschaften', 2, 'Uhrzeigersinn beschriftet. Es wird um', 'mehrschritt')
ST.regel('eigenschaften', 2, 'gespiegelt. Wie ist', 'mehrschritt')
ST.regel('eigenschaften', 2, 'Was kann sich', 'erkennen', neu_s=1)
ST.regel('eigenschaften', 2, 'Flächeninhalt', 'einkleidung')
ST.regel('eigenschaften', 3, 'parallelen Achsen', 'verknuepfen')
ST.regel('eigenschaften', 3, 'ENTGEGENGESETZTEM', 'begruenden')
ST.regel('eigenschaften', 3, 'schneidet die Spiegelachse', 'begruenden')
ST.regel('eigenschaften', 3, 'unter', 'verknuepfen')
ST.regel('eigenschaften', 3, 'erst an der x-Achse', 'verknuepfen')
ST.neu('eigenschaften', 1, 'direkt', ST.Z('Eine Strecke [AB] ist 6,5 cm lang. Sie wird an einer Achse gespiegelt. Wie lang ist [A\'B\']?', 6.5, '6.5',
                                         'Kongruenzabbildungen ändern keine Längen: [A\'B\'] ist 6,5 cm lang.', 'Was bleibt bei einer Spiegelung gleich?', einheit='cm'))
ST.neu('eigenschaften', 1, 'direkt', ST.Z('Ein Winkel von 37° wird um einen Punkt um 90° gedreht. Wie groß ist der Bildwinkel?', 37, '37',
                                         'Drehungen ändern keine Winkelgrößen: Der Bildwinkel ist 37° groß.', 'Ändert die Drehung die Größe des Winkels?', einheit='°'))
ST.neu('eigenschaften', 3, 'fehler', ST.A('Jemand behauptet: „Bei einer Drehung bleibt kein Punkt an seinem Platz.“ Was stimmt?', 'Falsch: Das Drehzentrum bleibt an seinem Platz.',
                                          ['Richtig.', 'Falsch: Alle Punkte auf der x-Achse bleiben fest.', 'Falsch: Bei 90° bleiben vier Punkte fest.'],
                                          'Das Drehzentrum hat den Abstand 0 zu sich selbst und bewegt sich nicht. Bei einer Drehung um 360° bleiben sogar alle Punkte fest.',
                                          'Was passiert mit dem Zentrum?'))
ST.neu('eigenschaften', 3, 'transfer', ST.Z('Im Spiegel siehst du eine Uhr ohne Ziffern: Der Minutenzeiger zeigt nach oben, der Stundenzeiger dorthin, wo sonst die 2 ist. Wie viel Uhr ist es wirklich (volle Stunde)?',
                                            10, '12 - 2',
                                            'Der Spiegel spiegelt links und rechts an einer senkrechten Achse. Die 2 liegt rechts oben, ihr Spiegelbild ist links oben – dort steht sonst die 10. Es ist 10 Uhr.',
                                            'Wo liegt das Spiegelbild der 2 auf dem Zifferblatt?', einheit='Uhr'))
ST.neu('eigenschaften', 3, 'pruefung', _P('Das Dreieck A(1 | 1), B(4 | 1), C(1 | 3) wird an der y-Achse gespiegelt und das Bild danach mit v = (2 | −3) verschoben. Gib den Endpunkt C\'\' an.',
                                          'C\'\'', [1, 0], ['-1 + 2', '3 - 3'], 'Spiegeln: C\'(−1 | 3). Verschieben: C\'\'(1 | 0).', 'Erst spiegeln, dann verschieben.'))
ST.knobel('eigenschaften', ST.Z('Zwei Spiegelachsen schneiden sich in S unter 40°. Eine Figur wird abwechselnd an der ersten und der zweiten Achse gespiegelt. Nach wie vielen Spiegelungen liegt sie zum ersten Mal wieder genau an ihrem Platz?',
                                18, '2 * 720 / 80',
                                'Zwei Spiegelungen an Achsen mit 40° ergeben zusammen eine Drehung um S um 80°. Nach k solchen Paaren ist die Figur um 80° · k gedreht. '
                                'Das erste Vielfache von 80°, das ein Vielfaches von 360° ist, ist 720° (k = 9). '
                                'Nach einer ungeraden Zahl von Spiegelungen ist der Umlaufsinn umgekehrt, die Figur kann also nicht an ihrem Platz liegen. Ergebnis: 9 · 2 = 18 Spiegelungen.',
                                'Was bewirken zwei Spiegelungen nacheinander?'))
ST.knobel('eigenschaften', ST.A('Ein Dreieck ABC wird nacheinander 7-mal an verschiedenen Achsen gespiegelt, 4-mal gedreht und 3-mal verschoben. Hat das Bilddreieck denselben Umlaufsinn wie ABC?',
                                'Nein: Der Umlaufsinn kehrt sich 7-mal um.', ['Ja: 7 + 4 + 3 = 14 ist gerade.', 'Ja: Kongruenzabbildungen ändern nichts.', 'Das hängt von den Achsen ab.'],
                                'Nur Achsenspiegelungen kehren den Umlaufsinn um, Drehungen und Verschiebungen nicht. Nach 7 Umkehrungen (ungerade Anzahl) ist der Umlaufsinn umgekehrt – egal in welcher Reihenfolge und an welchen Achsen.',
                                'Welche der Abbildungen ändern den Umlaufsinn überhaupt?'))
# mittelsenkrechte
ST.leiter('mittelsenkrechte', 'Mittelpunkt einer Strecke, Lage der Mittelsenkrechten, Eigenschaft „gleich weit“.',
          'Lot fällen, Abstand zu einer Geraden, Spielplatz an der Straße, Konstruktionsschritte deuten.',
          'Ortslinien schneiden (Leuchttürme, Funkmast, drei Häuser), Anzahl von Punkten begründen, Lot auf schräge Gerade, Fehler, Prüfungsaufgabe.')
ST.regel('mittelsenkrechte', 1, 'Was gilt sicher', 'erkennen')
ST.regel('mittelsenkrechte', 1, '', 'direkt')
ST.regel('mittelsenkrechte', 2, 'Fälle das Lot', 'mehrschritt')
ST.regel('mittelsenkrechte', 2, 'Häuser', 'einkleidung')
ST.regel('mittelsenkrechte', 2, 'Spiegelachse', 'darstellung')
ST.regel('mittelsenkrechte', 2, 'erste Schritt', 'darstellung')
ST.regel('mittelsenkrechte', 2, '', 'mehrschritt')
ST.regel('mittelsenkrechte', 3, 'Leuchttürme', 'transfer')
ST.regel('mittelsenkrechte', 3, 'Funkmast', 'transfer')
ST.regel('mittelsenkrechte', 3, 'Häuser', 'verknuepfen')
ST.regel('mittelsenkrechte', 3, 'über der Geraden', 'verknuepfen')
ST.regel('mittelsenkrechte', 3, 'Fälle das Lot', 'verknuepfen')
ST.regel('mittelsenkrechte', 3, '', 'begruenden')
ST.neu('mittelsenkrechte', 3, 'fehler', ST.A('A(1 | 2) und B(5 | 2). Jemand sagt: „Die Mittelsenkrechte von [AB] geht durch (3 | 2) und ist waagrecht.“ Was stimmt?',
                                            'Falsch: [AB] ist waagrecht, die Mittelsenkrechte steht senkrecht darauf.',
                                            ['Richtig.', 'Falsch: Sie geht durch (2 | 2).', 'Falsch: Sie geht durch (3 | 0) und ist waagrecht.'],
                                            'Der Mittelpunkt (3 | 2) stimmt. Aber die Mittelsenkrechte steht senkrecht auf [AB]. Da [AB] waagrecht ist, ist sie senkrecht (alle Punkte mit x = 3).',
                                            'Wie steht die Mittelsenkrechte zur Strecke?'))
ST.neu('mittelsenkrechte', 3, 'pruefung', _P('Ein Dreieck hat die Ecken A(0 | 0), B(8 | 0) und C(0 | 6). Welcher Punkt ist von allen drei Ecken gleich weit entfernt?', 'M', [4, 3], ['8 / 2', '6 / 2'],
                                             'Die Mittelsenkrechte von [AB] ist senkrecht durch (4 | 0), die von [AC] waagrecht durch (0 | 3). Sie schneiden sich in M(4 | 3). '
                                             'M ist zugleich die Mitte von [BC] – beim rechtwinkligen Dreieck liegt der Punkt immer dort.',
                                             'Schneide zwei Mittelsenkrechte.'))
ST.knobel('mittelsenkrechte', ST.Z('A, B und C sind drei verschiedene Punkte auf einer Geraden. Wie viele Punkte gibt es, die von A und B gleich weit entfernt sind und zugleich von A und C gleich weit?', 0, '0',
                                   'Gesucht sind Punkte, die auf der Mittelsenkrechten von [AB] und auf der von [AC] liegen. Beide stehen senkrecht auf derselben Geraden, sind also parallel. '
                                   'Sie sind verschieden, weil die Mitten von [AB] und [AC] verschieden sind (B ≠ C). Parallele verschiedene Geraden schneiden sich nicht: 0 Punkte.',
                                   'Auf welchen Linien liegen die gesuchten Punkte, und wie liegen diese Linien zueinander?'))
ST.knobel('mittelsenkrechte', _P('Drei Dörfer liegen bei A(0 | 0), B(10 | 0) und C(4 | 6). Ein Brunnen soll von allen drei Dörfern gleich weit entfernt sein. Wo steht er?', 'Br', [5, 1], ['10 / 2', '5 - 4'],
                                 'Mittelsenkrechte von [AB]: senkrecht durch (5 | 0). Mittelsenkrechte von [BC]: Die Mitte von [BC] ist (7 | 3). [BC] geht 6 nach links und 6 nach oben, '
                                 'senkrecht dazu geht es in gleich großen Schritten nach links und nach unten: (7 | 3), (6 | 2), (5 | 1). Bei x = 5 treffen sich beide: Br(5 | 1). '
                                 'Probe auf Kästchenpapier: Zu A, B und C sind es jeweils 5 und 1 Kästchen in die beiden Richtungen – gleich lange Strecken.',
                                 'Zwei Mittelsenkrechte genügen. Eine davon ist besonders einfach.'))
# winkelhalbierende
ST.leiter('winkelhalbierende', 'Winkel halbieren; Punkte auf der Winkelhalbierenden sind von beiden Schenkeln gleich weit entfernt.',
          'Winkel aus der Hälfte, Nebenwinkel, Punkte gleich weit von zwei Achsen, Konstruktionsschritt.',
          'Ortslinie mit Weg schneiden, Nebenwinkel-Halbierende begründen, Anzahl von Punkten, Fehler mit dem Winkelfeld, Parameter.')
ST.regel('winkelhalbierende', 1, 'Was gilt sicher', 'erkennen')
ST.regel('winkelhalbierende', 1, 'Welcher Punkt', 'erkennen')
ST.regel('winkelhalbierende', 1, '', 'direkt')
ST.regel('winkelhalbierende', 2, 'Jeder Teil ist', 'umkehr')
ST.regel('winkelhalbierende', 2, 'Kreise', 'darstellung')
ST.regel('winkelhalbierende', 2, '', 'mehrschritt')
ST.regel('winkelhalbierende', 3, 'Feld', 'transfer')
ST.regel('winkelhalbierende', 3, 'Straßen', 'transfer')
ST.regel('winkelhalbierende', 3, 'Welcher Punkt ist von g und h', 'transfer')
ST.regel('winkelhalbierende', 3, 'Warum', 'begruenden')
ST.regel('winkelhalbierende', 3, 'den Abstand', 'begruenden')
ST.regel('winkelhalbierende', 3, '', 'verknuepfen')
ST.neu('winkelhalbierende', 3, 'fehler', ST.A('Jemand sagt: „P(−3 | 3) ist von beiden Achsen 3 entfernt, also liegt P auf der Winkelhalbierenden des Winkels zwischen positiver x-Achse und positiver y-Achse.“ Was stimmt?',
                                              'Falsch: P liegt nicht in diesem Winkel, sondern auf der Halbierenden des Nebenwinkels.',
                                              ['Richtig.', 'Falsch: P ist von den Achsen verschieden weit entfernt.', 'Falsch: Kein Punkt mit negativer Koordinate ist von beiden Achsen gleich weit entfernt.'],
                                              'Gleich weit von beiden Achsen sind die Punkte auf zwei Geraden (Kreuz). Der Winkel zwischen positiver x- und y-Achse ist der 1. Quadrant – P(−3 | 3) liegt im 2. Quadranten, also auf der Halbierenden des Nebenwinkels.',
                                              'In welchem Quadranten liegt P?'))
ST.neu('winkelhalbierende', 3, 'parameter', ST.Z('P(a | 6) ist von der x-Achse und der y-Achse gleich weit entfernt und liegt links von der y-Achse. Wie groß ist a?', -6, '-6',
                                                 'Abstand zur x-Achse: 6. Also auch 6 zur y-Achse: a = 6 oder a = −6. Links von der y-Achse: a = −6.', 'Wie weit ist P von der x-Achse entfernt?'))
ST.knobel('winkelhalbierende', ST.Z('Drei Strahlen gehen von einem Punkt S aus und teilen den Vollwinkel in drei Winkel α, β und γ. Die Winkelhalbierenden von α und β bilden einen Winkel von 100°. Wie groß ist γ?',
                                    160, '360 - 2 * 100',
                                    'α und β liegen nebeneinander. Der Winkel zwischen ihren Halbierenden besteht aus der halben α und der halben β: α/2 + β/2 = 100°, also α + β = 200°. '
                                    'Für γ bleibt 360° − 200° = 160°.',
                                    'Aus welchen Teilwinkeln setzt sich der Winkel zwischen den beiden Halbierenden zusammen?'))
ST.knobel('winkelhalbierende', ST.Z('Wie viele Punkte sind von der x-Achse, der y-Achse und der senkrechten Geraden durch (8 | 0) gleich weit entfernt?', 2, '2',
                                    'Gleich weit von der y-Achse und der senkrechten Geraden durch (8 | 0): Der Punkt liegt genau in der Mitte, x = 4. Sein Abstand zu beiden ist 4. '
                                    'Auch zur x-Achse muss er 4 betragen: y = 4 oder y = −4. Also zwei Punkte: (4 | 4) und (4 | −4).',
                                    'Beginne mit den beiden senkrechten Geraden.'))
# vierecke_ordnen
ST.leiter('vierecke_ordnen', 'Vierecke an Symmetrieachsen erkennen; wahre Aussagen im Haus der Vierecke.',
          'Falsche Aussagen finden, Vierecke in Bildern benennen, Nachbarn im Haus der Vierecke, Tischplatte.',
          'Gegenbeispiel, Viereck aus zwei Eigenschaften, Anzahlen begründen, unterscheidende Eigenschaft, Fehler, Prüfungsaufgabe mit Koordinaten.')
ST.regel('vierecke_ordnen', 1, 'Wie viele dieser', 'direkt')
ST.regel('vierecke_ordnen', 1, '', 'erkennen')
ST.regel('vierecke_ordnen', 2, 'abgebildet', 'darstellung')
ST.regel('vierecke_ordnen', 2, 'Haus der Vierecke', 'darstellung')
ST.regel('vierecke_ordnen', 2, '', 'mehrschritt')
ST.regel('vierecke_ordnen', 3, 'Tim', 'begruenden')
ST.regel('vierecke_ordnen', 3, 'Welche Eigenschaft', 'begruenden')
ST.regel('vierecke_ordnen', 3, 'Wie viele davon', 'transfer')
ST.regel('vierecke_ordnen', 3, '', 'verknuepfen')
ST.neu('vierecke_ordnen', 2, 'einkleidung', ST.A('Eine Tischplatte hat vier gleich lange Seiten, aber keinen rechten Winkel. Welches Viereck ist sie?', 'eine Raute',
                                                 ['ein Quadrat', 'ein Rechteck', 'ein gleichschenkliges Trapez'],
                                                 'Vier gleich lange Seiten: Raute oder Quadrat. Ohne rechten Winkel ist es kein Quadrat – also eine Raute.', 'Welche Vierecke haben vier gleich lange Seiten?'))
ST.neu('vierecke_ordnen', 3, 'fehler', ST.A('Jemand sagt: „Ein Viereck mit zwei Paaren gleich langer Seiten ist immer ein Parallelogramm.“ Was stimmt?',
                                            'Falsch: Beim Drachenviereck sind die gleich langen Seiten benachbart, es ist meist kein Parallelogramm.',
                                            ['Richtig.', 'Falsch: Es ist immer ein Rechteck.', 'Falsch: Es ist immer eine Raute.'],
                                            'Im Parallelogramm sind gegenüberliegende Seiten gleich lang. Ein Drachenviereck hat zwei Paare gleich langer Nachbarseiten – ein Gegenbeispiel.',
                                            'Denke an ein Viereck, bei dem die gleich langen Seiten nebeneinander liegen.'))
ST.neu('vierecke_ordnen', 3, 'pruefung', ST.A('Das Viereck hat die Ecken A(0 | 0), B(4 | 1), C(5 | 5) und D(1 | 4). Welches Viereck ist ABCD? Wähle die genaueste Bezeichnung.', 'Raute',
                                              ['Quadrat', 'Rechteck', 'gleichschenkliges Trapez'],
                                              'Die vier Seiten gehen 4 nach rechts und 1 hoch, 1 nach rechts und 4 hoch, 4 nach links und 1 runter, 1 nach links und 4 runter: gleiche Steigungsdreiecke, also vier gleich lange Seiten. '
                                              'Ein rechter Winkel bei B bräuchte als zweite Seite 1 nach links und 4 hoch – es geht aber 1 nach rechts. Also Raute, kein Quadrat.',
                                              'Vergleiche die Kästchenwege der vier Seiten.'))
ST.knobel('vierecke_ordnen', ST.Z('Wie viele der Bezeichnungen Quadrat, Rechteck, Raute, Parallelogramm, Drachenviereck, gleichschenkliges Trapez, Trapez, Viereck treffen auf ein Quadrat zu?', 8, '8',
                                  'Ein Quadrat hat vier rechte Winkel (Rechteck), vier gleich lange Seiten (Raute), parallele Gegenseiten (Parallelogramm, Trapez), '
                                  'eine Symmetrieachse durch zwei Ecken (Drachenviereck) und eine durch die Mitten zweier Gegenseiten (gleichschenkliges Trapez). Alle 8 Bezeichnungen passen.',
                                  'Prüfe jede Bezeichnung einzeln an ihrer Eigenschaft.'))
ST.knobel('vierecke_ordnen', ST.A('Ein Viereck hat genau zwei Symmetrieachsen, und keine davon geht durch eine Ecke. Welches Viereck ist es sicher?', 'ein Rechteck, das kein Quadrat ist',
                                  ['eine Raute, die kein Quadrat ist', 'ein Quadrat', 'ein Drachenviereck'],
                                  'Die Raute hat zwei Achsen durch die Ecken, das Quadrat vier, das Drachenviereck eine durch Ecken. Zwei Achsen durch die Seitenmitten hat nur das Rechteck (ohne Quadrat).',
                                  'Wo verlaufen die Achsen bei Raute und Rechteck?'))
# ---- STUFEN ENDE ----


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
    befunde_datei(META['thema_schluessel'], BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden
    einfuegen(META['thema_schluessel'], luecken(), 7180, quelle=_LUECKEN_QUELLE, offen=_LUECKEN_OFFEN)  # Achtzehnte Runde: zuletzt
    durchsicht_datei(META['thema_schluessel'], DS)  # Neunzehnte Runde: zuletzt
    stufen_datei(META['thema_schluessel'], ST)  # Zwanzigste Runde: zuletzt


# ---- BEREINIGEN (Einundzwanzigste Runde) ----
if __name__ == '__main__':
    from _bereinigen import bereinigen_datei
    bereinigen_datei('abbildungen.kongruenz')
# ---- BEREINIGEN ENDE ----
