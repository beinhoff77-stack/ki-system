#!/usr/bin/env python3
"""Thema geometrie.grundbegriffe – Grundbegriffe und Figuren (Klasse 5): Koordinatensystem, Lagebeziehungen, Kreis, Winkelarten, Vierecke."""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl5_rest import *  # noqa: E402,F403

R = random.Random(42)
E = eintrag_laden('geometrie.grundbegriffe')

ETAPPEN = [
    {'lernziel': 'koordinaten', 'titel': 'Punkte im Koordinatensystem',
     'regel': 'Im ⟦Koordinatensystem⟧ hat jeder Punkt zwei Koordinaten: P(x | y). Die ⟦x-Koordinate⟧ sagt, wie weit du nach rechts (+) oder links (−) gehst, die ⟦y-Koordinate⟧, wie weit nach oben (+) oder unten (−). O(0 | 0) heißt ⟦Ursprung⟧.',
     'schritte': ['P(3 | −2): vom Ursprung 3 nach rechts, dann 2 nach unten.', 'Verschiebe P um 4 nach links und 5 nach oben: x = 3 − 4 = −1, y = −2 + 5 = 3, also ⟦P′(−1 | 3)⟧.'],
     'bild': {'typ': 'koordinaten', 'x': [-3, 5], 'y': [-4, 5], 'punkte': [{'x': 3, 'y': -2, 'name': 'P'}, {'x': -1, 'y': 3, 'name': 'P′'}], 'strecken': [[3, -2, -1, -2, 'gestrichelt'], [-1, -2, -1, 3, 'gestrichelt']]},
     'fehler': 'P(3 | −2) und Q(−2 | 3) zu verwechseln ist falsch: Die ⟦x-Koordinate steht immer zuerst⟧ – erst rechts/links, dann oben/unten.'},
    {'lernziel': 'strecken', 'titel': 'Streckenlängen im Koordinatensystem',
     'regel': 'Haben zwei Punkte dieselbe ⟦y-Koordinate⟧, liegen sie auf einer waagrechten Linie: Die Länge der Strecke ist der ⟦Unterschied der x-Koordinaten⟧. Bei gleicher x-Koordinate (senkrecht) ist es der Unterschied der y-Koordinaten. Die Strecke von A nach B schreibt man [AB].',
     'schritte': ['A(−3 | 2) und B(4 | 2) haben dieselbe y-Koordinate 2.', 'Von −3 bis 0 sind es 3, von 0 bis 4 sind es 4: [AB] ist ⟦7⟧ Einheiten lang.'],
     'bild': {'typ': 'koordinaten', 'x': [-4, 5], 'y': [-1, 4], 'punkte': [{'x': -3, 'y': 2, 'name': 'A'}, {'x': 4, 'y': 2, 'name': 'B'}], 'strecken': [[-3, 2, 4, 2]]},
     'fehler': '„4 − 3 = 1“ ist falsch: Die Punkte liegen auf ⟦verschiedenen Seiten⟧ der 0. Richtig: 4 − (−3) = 4 + 3 = 7.'},
    {'lernziel': 'lagebeziehungen', 'titel': 'Parallel, senkrecht, Abstand',
     'regel': 'Zwei Geraden sind ⟦parallel⟧ (g ∥ h), wenn sie sich nie schneiden und überall gleich weit voneinander entfernt sind. Sie sind ⟦senkrecht⟧ zueinander (g ⊥ h), wenn sie sich im rechten Winkel schneiden. Die Senkrechte von P auf g heißt ⟦Lot⟧; ihre Länge ist der ⟦Abstand⟧ von P zu g.',
     'schritte': ['Die Gerade g geht waagrecht durch alle Punkte mit der y-Koordinate 1. P(4 | 6).', 'Das Lot von P auf g endet bei (4 | 1). Abstand: 6 − 1 = ⟦5⟧ Einheiten.'],
     'bild': {'typ': 'koordinaten', 'x': [-1, 7], 'y': [-1, 7], 'punkte': [{'x': 4, 'y': 6, 'name': 'P'}], 'waagrecht': [1], 'strecken': [[4, 6, 4, 1, 'gestrichelt']]},
     'fehler': 'Den Abstand von P zu g schräg zu messen ist falsch: Der Abstand ist die ⟦kürzeste⟧ Verbindung, also entlang des ⟦Lots⟧.'},
    {'lernziel': 'kreis_lage', 'titel': 'Kreis, Gerade und zwei Kreise',
     'regel': 'Ein ⟦Kreis⟧ um M mit Radius r besteht aus allen Punkten, die von M den Abstand r haben. Hat eine Gerade von M den Abstand d, ist sie bei d < r eine ⟦Sekante⟧ (2 Schnittpunkte), bei d = r eine ⟦Tangente⟧ (1 Berührpunkt), bei d > r eine ⟦Passante⟧ (kein gemeinsamer Punkt).',
     'schritte': ['Kreis um M mit r = 4 cm. Die Gerade g hat von M den Abstand 4 cm.', 'd = r, also ist g eine ⟦Tangente⟧: Sie berührt den Kreis in genau einem Punkt.'],
     'bild': {'typ': 'figur', 'punkte': {'M': [0, 0], '_T': [0, 4], '_A': [-6, 4], '_B': [6, 4], '_S1': [-6, 2], '_S2': [6, 2]},
              'kreise': [{'m': 'M', 'r': 4}], 'linien': [['M', '_T', 'r = 4 cm'], ['_A', '_B', 'Tangente'], ['_S1', '_S2', 'Sekante']]},
     'fehler': 'Eine Gerade, die den Kreis nur berührt, Sekante zu nennen ist falsch: Eine Sekante ⟦schneidet⟧ den Kreis in zwei Punkten, eine ⟦Tangente⟧ berührt ihn in genau einem.'},
    {'lernziel': 'winkelarten', 'titel': 'Winkelarten bis 360°',
     'regel': 'Ein ⟦Winkel⟧ besteht aus zwei ⟦Schenkeln⟧ mit gemeinsamem ⟦Scheitel⟧. Winkelarten: ⟦spitz⟧ (unter 90°), ⟦recht⟧ (90°), ⟦stumpf⟧ (zwischen 90° und 180°), ⟦gestreckt⟧ (180°), ⟦überstumpf⟧ (zwischen 180° und 360°), ⟦Vollwinkel⟧ (360°).',
     'schritte': ['α = 235° ist größer als 180° und kleiner als 360°.', 'Also ist α ⟦überstumpf⟧.'],
     'bild': {'typ': 'figur', 'punkte': {'S': [0, 0], '_A': [5, 0], '_B': [-3.536, 3.536]}, 'linien': [['S', '_A', 'Schenkel'], ['S', '_B', 'Schenkel']], 'winkel': [['S', '_A', '_B', '135°']]},
     'fehler': '135° spitz zu nennen ist falsch: Spitz sind nur Winkel ⟦unter 90°⟧. 135° liegt zwischen 90° und 180°, ist also ⟦stumpf⟧.'},
    {'lernziel': 'vierecke', 'titel': 'Besondere Vierecke',
     'regel': '⟦Quadrat⟧: 4 gleich lange Seiten, 4 rechte Winkel. ⟦Rechteck⟧: 4 rechte Winkel. ⟦Raute⟧: 4 gleich lange Seiten. ⟦Parallelogramm⟧: gegenüberliegende Seiten parallel. ⟦Trapez⟧: mindestens zwei Seiten parallel. ⟦Drachenviereck⟧: zwei Paare gleich langer ⟦benachbarter⟧ Seiten.',
     'schritte': ['Ein Viereck hat 4 gleich lange Seiten, aber keinen rechten Winkel.', 'Ohne rechte Winkel ist es kein Quadrat. Es ist eine ⟦Raute⟧.'],
     'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [4, 0], 'C': [6, 3], 'D': [2, 3]}, 'flaeche': ['A', 'B', 'C', 'D'],
              'linien': [['A', 'B', '4 cm'], ['B', 'C'], ['C', 'D'], ['D', 'A']]},
     'fehler': '„Ein Quadrat ist kein Rechteck“ ist falsch: Ein Quadrat hat 4 rechte Winkel, also alle Eigenschaften eines Rechtecks. Jedes Quadrat ist ⟦auch ein Rechteck⟧ – und auch eine Raute.'},
    {'lernziel': 'verstehen', 'titel': 'Aussagen zur Geometrie prüfen',
     'regel': 'Prüfe geometrische Aussagen mit einer ⟦Skizze⟧ oder einem ⟦Gegenbeispiel⟧. Achte auf genaue Fachbegriffe: Strecke, Gerade, Halbgerade, Lot, Abstand, Tangente.',
     'schritte': ['Aussage: „Jedes Rechteck ist ein Quadrat.“ Gegenbeispiel: ein Rechteck mit 6 cm und 3 cm Seitenlänge.', 'Seine Seiten sind nicht alle gleich lang. Die Aussage ist ⟦falsch⟧.'],
     'fehler': 'Eine Aussage mit nur einem passenden Beispiel für „immer richtig“ zu halten ist ein Fehler. ⟦Ein Gegenbeispiel⟧ genügt, um eine Allaussage zu widerlegen.'},
]

PRUEFUNG = pruefung_erklaerungen(ETAPPEN, 'geometrie.grundbegriffe')   # kreis_lage (Bild mit Passante, Probe), vierecke (Bild: Raute)

MERKE = ['P(x | y): erst x (rechts/links), dann y (oben/unten).', 'Waagrechte Strecke: Unterschied der x-Koordinaten.',
         'g ∥ h: parallel. g ⊥ h: senkrecht. Abstand = Länge des Lots.', 'd < r Sekante, d = r Tangente, d > r Passante.',
         'spitz < 90° = recht < stumpf < 180° = gestreckt < überstumpf < 360°.']


def ein(n): return f'{n} Einheit' if n == 1 else f'{n} Einheiten'


def p(x, y): return f'({zt(x)} | {zt(y)})'


def ks(punkte, strecken=(), waag=(), senk=(), rand=1):
    """Koordinatensystem-Grafik, Achsen passend zu den Punkten."""
    xs = [q[0] for q in punkte] + [v for s_ in strecken for v in (s_[0], s_[2])] + list(senk) + [0]
    ys = [q[1] for q in punkte] + [v for s_ in strecken for v in (s_[1], s_[3])] + list(waag) + [0]
    g = {'typ': 'koordinaten', 'x': [min(xs) - rand, max(xs) + rand], 'y': [min(ys) - rand, max(ys) + rand],
         'punkte': [{'x': q[0], 'y': q[1], 'name': q[2]} for q in punkte]}
    if strecken: g['strecken'] = [list(s_) for s_ in strecken]
    if waag: g['waagrecht'] = list(waag)
    if senk: g['senkrecht'] = list(senk)
    return g


def mit(a, grafik):
    a['f']['grafik'] = grafik
    return a


def winkelfigur(grad, text):
    import math
    w = math.radians(grad)
    return {'typ': 'figur', 'punkte': {'S': [0, 0], '_A': [5, 0], '_B': [round(5 * math.cos(w), 3), round(5 * math.sin(w), 3)]},
            'linien': [['S', '_A'], ['S', '_B']], 'winkel': [['S', '_A', '_B', text]]}


def richtung(dx, dy):
    t = []
    if dx: t.append(f'{abs(dx)} nach {"rechts" if dx > 0 else "links"}')
    if dy: t.append(f'{abs(dy)} nach {"oben" if dy > 0 else "unten"}')
    return ' und '.join(t)


# ---------- 1 Koordinaten ----------
def _welcher_punkt():
    x, y = R.choice([-1, 1]) * R.randint(1, 5), R.choice([-1, 1]) * R.randint(1, 5)
    if R.random() < .25: x, y = (0, y) if R.random() < .5 else (x, 0)
    kand = [(x, y), (y, x), (-x, y), (x, -y), (-x, -y)]
    pts = []
    for q in kand:
        if q not in pts: pts.append(q)
    if len(pts) < 4: return _welcher_punkt()
    pts = [pts[0]] + R.sample(pts[1:], 3)
    R.shuffle(pts)
    namen = 'ABCD'
    i = pts.index((x, y))
    return {'y': 'auswahl', 'a': list(namen), 'o': {'index': i},
            'f': {'text': f'Welcher Punkt hat die Koordinaten {p(x, y)}?', 'grafik': ks([(q[0], q[1], namen[k]) for k, q in enumerate(pts)])},
            'w': f'{p(x, y)}: x = {zt(x)} ({"rechts" if x > 0 else "links" if x < 0 else "auf der y-Achse"}), y = {zt(y)} ({"oben" if y > 0 else "unten" if y < 0 else "auf der x-Achse"}). Das ist Punkt {namen[i]}.',
            'h': 'Erst die x-Koordinate (rechts/links), dann die y-Koordinate (oben/unten).'}


def g_koord(st):
    if st == 1:
        if R.random() < .3: return _welcher_punkt()
        if R.random() < .35:
            x, y = R.randint(-6, 6), R.randint(-5, 5)
            if x == 0 or y == 0: return g_koord(1)
            return mit(punkt('P', x, y, 'Lies die Koordinaten des Punktes P ab.', f'P liegt bei x = {zt(x)} und y = {zt(y)}: P{p(x, y)}.', 'Erst nach rechts/links schauen (x), dann nach oben/unten (y).'),
                       ks([(x, y, 'P')]))
        if R.random() < .5:
            x, y = R.randint(-8, 8), R.randint(-8, 8)
            if x == 0 or y == 0: return g_koord(1)
            return punkt('P', x, y, f'Ein Punkt P liegt {abs(x)} Einheiten {"rechts" if x > 0 else "links"} vom Ursprung und {abs(y)} Einheiten {"über" if y > 0 else "unter"} ihm. Welche Koordinaten hat P?',
                         f'{"Rechts" if x > 0 else "Links"} heißt x = {zt(x)}, {"oben" if y > 0 else "unten"} heißt y = {zt(y)}: P{p(x, y)}.', 'Rechts/links ist die x-Koordinate, oben/unten die y-Koordinate.')
        x, y = R.randint(0, 6), R.randint(0, 6)
        dx, dy = R.randint(1, 5), R.randint(1, 5)
        return punkt('A′', x + dx, y + dy, f'Verschiebe A{p(x, y)} um {richtung(dx, dy)}. Welche Koordinaten hat der neue Punkt A′?',
                     f'x: {x} + {dx} = {x + dx}, y: {y} + {dy} = {y + dy}. Also A′{p(x + dx, y + dy)}.', 'Nach rechts und oben wird addiert.', f'{x} + {dx}', f'{y} + {dy}')
    if st == 2:
        if R.random() < .7:
            x, y = R.randint(-6, 6), R.randint(-6, 6)
            dx, dy = R.choice([-1, 1]) * R.randint(1, 7), R.choice([-1, 1]) * R.randint(1, 7)
            return punkt('B′', x + dx, y + dy, f'Verschiebe B{p(x, y)} um {richtung(dx, dy)}. Welche Koordinaten hat B′?',
                         f'x: {kl(x)} {"+" if dx > 0 else "−"} {abs(dx)} = {zt(x + dx)}, y: {kl(y)} {"+" if dy > 0 else "−"} {abs(dy)} = {zt(y + dy)}. Also B′{p(x + dx, y + dy)}.',
                         'Rechts und oben: plus. Links und unten: minus.', f'({x}) + ({dx})', f'({y}) + ({dy})')
        x, y = R.choice([-1, 1]) * R.randint(1, 8), R.choice([-1, 1]) * R.randint(1, 8)
        lage = {(1, 1): 'rechts oben', (-1, 1): 'links oben', (-1, -1): 'links unten', (1, -1): 'rechts unten'}
        if R.random() < .3:      # auch Punkte auf einer Achse (Prüfung)
            x, y = (x, 0) if R.random() < .5 else (0, y)
            achse = {(1, 0): 'auf der x-Achse, rechts', (-1, 0): 'auf der x-Achse, links', (0, 1): 'auf der y-Achse, oben', (0, -1): 'auf der y-Achse, unten'}
            r = achse[((x > 0) - (x < 0), (y > 0) - (y < 0))]
            f = R.sample([v for v in achse.values() if v != r], 2) + R.sample(list(lage.values()), 1)
            return {**wahl_rund(R, r, f), 'f': {'text': f'Wo liegt der Punkt P{p(x, y)}, vom Ursprung aus gesehen?'},
                    'w': f'Eine Koordinate ist 0: Der Punkt liegt auf einer Achse. {r[0].upper() + r[1:]}.', 'h': 'Ist eine Koordinate 0? Dann liegt der Punkt auf einer Achse.'}
        r = lage[(1 if x > 0 else -1, 1 if y > 0 else -1)]
        return {**wahl_rund(R, r, [v for v in lage.values() if v != r]), 'f': {'text': f'Wo liegt der Punkt P{p(x, y)}, vom Ursprung aus gesehen?'},
                'w': f'x = {zt(x)}: {"rechts" if x > 0 else "links"}, y = {zt(y)}: {"oben" if y > 0 else "unten"}. Also {r}.', 'h': 'Das Vorzeichen von x sagt rechts/links, das von y oben/unten.'}
    art = R.randrange(3)
    if art == 0:
        x1, x2 = sorted(R.sample(range(-7, 8), 2))
        y1, y2 = sorted(R.sample(range(-7, 8), 2))
        return mit(punkt('D', x1, y2, f'Ein Rechteck ABCD hat die Ecken A{p(x1, y1)}, B{p(x2, y1)} und C{p(x2, y2)}. Seine Seiten sind parallel zu den Achsen. Welche Koordinaten hat D?',
                     f'D liegt senkrecht über A (x = {zt(x1)}) und waagrecht neben C (y = {zt(y2)}): D{p(x1, y2)}.', 'D hat die x-Koordinate von A und die y-Koordinate von C.', f'{x1}', f'{y2}'),
                   ks([(x1, y1, 'A'), (x2, y1, 'B'), (x2, y2, 'C')], [(x1, y1, x2, y1), (x2, y1, x2, y2)]))
    if art == 1:
        y = R.randint(-6, 6)
        x1 = R.randint(-8, 2)
        x2 = x1 + 2 * R.randint(1, 6)
        m = (x1 + x2) // 2
        return punkt('M', m, y, f'M ist der Mittelpunkt der Strecke [AB] mit A{p(x1, y)} und B{p(x2, y)}. Welche Koordinaten hat M?',
                     f'[AB] ist {x2 - x1} lang, die Hälfte ist {(x2 - x1) // 2}. Von A aus {(x2 - x1) // 2} nach rechts: M{p(m, y)}.', 'Die y-Koordinate bleibt gleich. Gehe von A die halbe Länge nach rechts.',
                     f'({x1} + {x2}) / 2', f'{y}')
    x, y = R.randint(-6, 6), R.randint(-6, 6)
    dx, dy = R.choice([-1, 1]) * R.randint(1, 5), R.choice([-1, 1]) * R.randint(1, 5)
    x2, y2 = x + dx, y + dy
    return luecke([dx, dy], f'Der Punkt P{p(x, y)} wurde verschoben und liegt jetzt bei P′{p(x2, y2)}. Um wie viel wurde er nach rechts und nach oben verschoben? (Nach links oder unten: negative Zahl.)',
                  'nach rechts □, nach oben □', 'Negative Zahl für links bzw. unten.', [f'({x2}) - ({x})', f'({y2}) - ({y})'],
                  f'x: {zt(x2)} − {kl(x)} = {zt(dx)}, y: {zt(y2)} − {kl(y)} = {zt(dy)}.', 'Rechne neue Koordinate minus alte Koordinate.')


# ---------- 2 Strecken ----------
def g_strecke(st):
    if st == 1:
        y = R.randint(0, 8)
        x1, x2 = sorted(R.sample(range(0, 12), 2))
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Wie lang ist die Strecke [AB] mit A{p(x1, y)} und B{p(x2, y)} (in Einheiten)?', 'grafik': ks([(x1, y, 'A'), (x2, y, 'B')], [(x1, y, x2, y)])}, 'o': {'wert': x2 - x1}, 'c': f'{x2} - {x1}',
                    'w': f'Gleiche y-Koordinate, also waagrecht: {x2} − {x1} = {ein(x2 - x1)}.', 'h': 'Vergleiche die x-Koordinaten.'}
        return {'y': 'zahl', 'f': {'text': f'Wie lang ist die Strecke [CD] mit C{p(y, x1)} und D{p(y, x2)} (in Einheiten)?'}, 'o': {'wert': x2 - x1}, 'c': f'{x2} - {x1}',
                'w': f'Gleiche x-Koordinate, also senkrecht: {x2} − {x1} = {ein(x2 - x1)}.', 'h': 'Vergleiche die y-Koordinaten.'}
    if st == 2:
        a, b = sorted(R.sample(range(-9, 10), 2))
        if a >= 0: a = -R.randint(1, 6)
        c = R.randint(-6, 6)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Wie lang ist [AB] mit A{p(a, c)} und B{p(b, c)} (in Einheiten)?', 'grafik': ks([(a, c, 'A'), (b, c, 'B')], [(a, c, b, c)])}, 'o': {'wert': b - a}, 'c': f'({b}) - ({a})',
                    'w': f'Waagrecht: {zt(b)} − {kl(a)} = {zt(b)} + {zt(-a)} = {ein(b - a)}.', 'h': 'Liegt die 0 dazwischen? Dann zähle die beiden Teilstücke zusammen.'}
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Welchen Abstand hat der Punkt P{p(c, a)} von der x-Achse (in Einheiten)?'}, 'o': {'wert': abs(a)}, 'c': f'abs({a})',
                    'w': f'Der Abstand zur x-Achse ist der Betrag der y-Koordinate: |{zt(a)}| = {abs(a)}.', 'h': 'Wie weit ist P von der waagrechten Achse entfernt? Schau auf y.'}
        return {'y': 'zahl', 'f': {'text': f'Wie lang ist [CD] mit C{p(c, a)} und D{p(c, b)} (in Einheiten)?'}, 'o': {'wert': b - a}, 'c': f'({b}) - ({a})',
                'w': f'Senkrecht: {zt(b)} − {kl(a)} = {ein(b - a)}.', 'h': 'Gleiche x-Koordinate: Unterschied der y-Koordinaten.'}
    art = R.randrange(3)
    x1, x2 = sorted(R.sample(range(-7, 8), 2))
    y1, y2 = sorted(R.sample(range(-6, 7), 2))
    if art == 0:
        u = 2 * (x2 - x1) + 2 * (y2 - y1)
        return {'y': 'zahl', 'f': {'text': f'Ein Rechteck hat die Ecken A{p(x1, y1)}, B{p(x2, y1)}, C{p(x2, y2)}, D{p(x1, y2)}. 1 Einheit = 1 cm. Wie lang ist der Umfang in cm?'},
                'o': {'wert': u, 'einheit': 'cm'}, 'c': f'2 * (({x2}) - ({x1})) + 2 * (({y2}) - ({y1}))',
                'w': f'[AB] = {x2 - x1} cm, [BC] = {y2 - y1} cm. Umfang: 2 · {x2 - x1} + 2 · {y2 - y1} = {u} cm.', 'h': 'Bestimme eine waagrechte und eine senkrechte Seite.'}
    if art == 1:
        d = R.randint(2, 9)
        x, y = R.randint(-5, 5), R.randint(-5, 5)
        return luecke([y - d, y + d], f'Auf der senkrechten Linie durch P{p(x, y)} liegen zwei Punkte, die von P den Abstand {d} haben. Welche y-Koordinaten haben sie? (kleinere zuerst)',
                      'y = □ und y = □', 'Die kleinere Zahl zuerst.', [f'({y}) - {d}', f'({y}) + {d}'], f'{d} nach unten: {zt(y)} − {d} = {zt(y - d)}. {d} nach oben: {zt(y)} + {d} = {zt(y + d)}.',
                      'Gehe vom Punkt aus nach oben und nach unten.')
    pts = [(R.randint(-6, 6), R.randint(-6, 6)) for _ in range(2)]
    (ax, ay) = pts[0]
    lang = [(R.randint(2, 8), 'rechts'), (R.randint(2, 8), 'oben'), (R.randint(2, 8), 'links')]
    x, y = ax, ay
    for l, r_ in lang:
        if r_ == 'rechts': x += l
        elif r_ == 'oben': y += l
        else: x -= l
    weg = sum(l for l, _ in lang)
    return {'y': 'zahl', 'f': {'text': f'Eine Ameise läuft von A{p(ax, ay)} {lang[0][0]} nach rechts, {lang[1][0]} nach oben und {lang[2][0]} nach links. Wie viele Einheiten ist sie insgesamt gelaufen?'},
            'o': {'wert': weg}, 'c': f'{lang[0][0]} + {lang[1][0]} + {lang[2][0]}', 'w': f'{lang[0][0]} + {lang[1][0]} + {lang[2][0]} = {ein(weg)}. Sie endet bei {p(x, y)}.',
            'h': 'Addiere alle Teilstrecken.'} if R.random() < .5 else \
        punkt('Z', x, y, f'Eine Ameise läuft von A{p(ax, ay)} {lang[0][0]} nach rechts, {lang[1][0]} nach oben und {lang[2][0]} nach links. An welchem Punkt Z kommt sie an?',
              f'x: {zt(ax)} + {lang[0][0]} − {lang[2][0]} = {zt(x)}, y: {zt(ay)} + {lang[1][0]} = {zt(y)}. Z{p(x, y)}.', 'Rechts/links ändert x, oben ändert y.',
              f'({ax}) + {lang[0][0]} - {lang[2][0]}', f'({ay}) + {lang[1][0]}')


# ---------- 3 Lagebeziehungen ----------
BEGRIFFE = [('Eine gerade Linie mit Anfangs- und Endpunkt heißt …', 'Strecke', ['Gerade', 'Halbgerade', 'Lot']),
            ('Eine gerade Linie ohne Anfang und Ende heißt …', 'Gerade', ['Strecke', 'Halbgerade', 'Kreis']),
            ('Eine gerade Linie mit Anfangspunkt, aber ohne Ende heißt …', 'Halbgerade', ['Strecke', 'Gerade', 'Tangente']),
            ('Zwei Geraden, die sich im rechten Winkel schneiden, sind …', 'senkrecht zueinander', ['parallel', 'gleich lang', 'Tangenten']),
            ('Zwei verschiedene Geraden, die sich nie schneiden, sind …', 'parallel', ['senkrecht zueinander', 'Lote', 'Strecken']),
            ('Die kürzeste Verbindung von einem Punkt zu einer Geraden heißt …', 'Lot', ['Halbgerade', 'Sekante', 'Diagonale']),
            ('Wie viele gemeinsame Punkte haben zwei verschiedene parallele Geraden?', 'keinen', ['genau einen', 'zwei', 'unendlich viele']),
            ('Wie viele Schnittpunkte haben zwei Geraden, die senkrecht zueinander sind?', 'genau einen', ['keinen', 'zwei', 'vier']),
            ('Wie viele Geraden gehen durch zwei verschiedene Punkte?', 'genau eine', ['keine', 'zwei', 'unendlich viele']),
            ('Wie viele Geraden gehen durch einen einzigen Punkt?', 'unendlich viele', ['genau eine', 'keine', 'zwei']),
            ('Das Zeichen g ∥ h bedeutet …', 'g ist parallel zu h', ['g ist senkrecht zu h', 'g ist gleich lang wie h', 'g schneidet h']),
            ('Das Zeichen g ⊥ h bedeutet …', 'g ist senkrecht zu h', ['g ist parallel zu h', 'g ist länger als h', 'g berührt h'])]


WARUM = {'Strecke': 'Eine Strecke hat einen Anfangs- und einen Endpunkt, deshalb kann man ihre Länge messen.',
         'Gerade': 'Eine Gerade hat keinen Anfang und kein Ende, sie geht in beide Richtungen unendlich weiter.',
         'Halbgerade': 'Eine Halbgerade hat einen Anfangspunkt, geht aber auf einer Seite unendlich weiter.',
         'senkrecht zueinander': 'Senkrecht heißt: Die Geraden bilden einen rechten Winkel (90°).',
         'parallel': 'Parallele Geraden haben überall denselben Abstand, deshalb schneiden sie sich nie.',
         'Lot': 'Das Lot steht senkrecht auf der Geraden – das ist der kürzeste Weg.',
         'keinen': 'Parallele Geraden haben überall denselben Abstand und treffen sich deshalb nie.',
         'genau einen': None, 'genau eine': 'Durch zwei verschiedene Punkte kann man genau eine Gerade legen – mit dem Lineal gibt es nur eine Möglichkeit.',
         'unendlich viele': 'Um einen einzigen Punkt kann man das Lineal in jede Richtung drehen: unendlich viele Geraden.',
         'g ist parallel zu h': 'Das Zeichen ∥ sieht aus wie zwei parallele Striche: g und h schneiden sich nie und haben überall denselben Abstand.',
         'g ist senkrecht zu h': 'Das Zeichen ⊥ zeigt einen rechten Winkel: g und h schneiden sich im 90°-Winkel.'}


def _linienbild():
    arten = ['Strecke', 'Halbgerade', 'Gerade']
    R.shuffle(arten)
    P, L = {}, []
    for k, a in enumerate(arten):
        y = 4 - 2 * k
        if a == 'Strecke': P['A'], P['B'] = [2, y], [6, y]; L.append(['A', 'B', f'Linie {k + 1}'])
        elif a == 'Halbgerade': P['C'], P[f'_E{k}'] = [2, y], [10, y]; L.append(['C', f'_E{k}', f'Linie {k + 1}'])
        else: P[f'_G{k}a'], P[f'_G{k}b'] = [0, y], [10, y]; L.append([f'_G{k}a', f'_G{k}b', f'Linie {k + 1}'])
    frage, ziel = R.choice([('Welche Linie ist eine Halbgerade?', 'Halbgerade'), ('Welche Linie ist eine Strecke?', 'Strecke'),
                            ('Welche Linie ist eine Gerade?', 'Gerade'), ('Welche Linie hat eine messbare Länge?', 'Strecke')])
    i = arten.index(ziel)
    return {'y': 'auswahl', 'a': ['Linie 1', 'Linie 2', 'Linie 3'], 'o': {'index': i},
            'f': {'text': f'Die Punkte markieren Anfangs- und Endpunkte. Wo kein Punkt ist, geht die Linie bis zum Bildrand und weiter. {frage}',
                  'grafik': {'typ': 'figur', 'punkte': P, 'linien': L}},
            'w': f'Linie {i + 1} ist eine {ziel}: {WARUM[ziel]}', 'h': 'Zähle die Endpunkte: zwei, einer oder keiner?'}


def g_lage(st):
    if st == 1:
        if R.random() < .4: return _linienbild()
        t, r, f = R.choice(BEGRIFFE)
        warum = WARUM.get(r) or 'Zwei Geraden, die senkrecht zueinander sind, kreuzen sich an genau einer Stelle.'
        return {**wahl_rund(R, r, f), 'f': {'text': t}, 'w': f'Richtig ist: {r}. {warum}', 'h': 'Denke an die Fachbegriffe aus der Erklärung.'}
    if st == 2:
        c = R.randint(-6, 6)
        x, y = R.randint(-8, 8), R.randint(-8, 8)
        if y == c: y += 3
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Die Gerade g verläuft waagrecht durch alle Punkte mit y = {zt(c)}. Welchen Abstand hat P{p(x, y)} von g (in Einheiten)?', 'grafik': ks([(x, y, 'P')], waag=[c])},
                    'o': {'wert': abs(y - c)}, 'c': f'abs(({y}) - ({c}))', 'w': f'Das Lot von P auf g ist senkrecht. Abstand: Unterschied der y-Koordinaten, |{zt(y)} − {kl(c)}| = {abs(y - c)}.',
                    'h': 'Das Lot auf eine waagrechte Gerade ist senkrecht – nur y ändert sich.'}
        if x == c: x += 3
        return {'y': 'zahl', 'f': {'text': f'Die Gerade h verläuft senkrecht durch alle Punkte mit x = {zt(c)}. Welchen Abstand hat P{p(x, y)} von h (in Einheiten)?', 'grafik': ks([(x, y, 'P')], senk=[c])},
                'o': {'wert': abs(x - c)}, 'c': f'abs(({x}) - ({c}))', 'w': f'Das Lot auf h ist waagrecht. Abstand: |{zt(x)} − {kl(c)}| = {abs(x - c)}.',
                'h': 'Das Lot auf eine senkrechte Gerade ist waagrecht – nur x ändert sich.'}
    art = R.randrange(3)
    if art == 0:
        a, b = R.sample(range(-6, 7), 2)
        y1, y2 = sorted(R.sample(range(-6, 7), 2))
        typ = R.choice(['par', 'senk'])
        if typ == 'par':
            t = f'g geht durch A{p(a, y1)} und B{p(a, y2)}, h geht durch C{p(b, y1 + 1)} und D{p(b, y2 + 3)}.'
            r, w = 'g ∥ h', f'Beide Geraden sind senkrecht zur x-Achse (x = {zt(a)} bzw. x = {zt(b)}), also parallel.'
        else:
            t = f'g geht durch A{p(a, y1)} und B{p(a, y2)}, h geht durch C{p(b, y1)} und D{p(b + 4, y1)}.'
            r, w = 'g ⊥ h', 'g ist senkrecht (gleiches x), h ist waagrecht (gleiches y). Sie schneiden sich im rechten Winkel.'
        return {**wahl(R, r, ['g ∥ h', 'g ⊥ h', 'g und h sind gleich'] if r != 'g und h sind gleich' else []), 'f': {'text': f'{t} Wie liegen g und h zueinander?'},
                'w': w, 'h': 'Gleiche x-Koordinaten: senkrechte Linie. Gleiche y-Koordinaten: waagrechte Linie.'}
    if art == 1:
        c, d = R.randint(-4, 4), R.randint(2, 6)
        return luecke([c - d, c + d], f'g ist die waagrechte Gerade mit y = {zt(c)}. Die Geraden h₁ und h₂ sind parallel zu g und haben von g den Abstand {d}. Welche y-Werte haben h₁ und h₂? (kleinerer zuerst)',
                      'y = □ und y = □', 'Kleinere Zahl zuerst.', [f'({c}) - {d}', f'({c}) + {d}'], f'{d} unter g: {zt(c - d)}, {d} über g: {zt(c + d)}.', 'Es gibt eine Parallele darüber und eine darunter.')
    w1 = R.choice([3, 4, 5, 6, 8])
    w2 = R.choice([2, 3, 4, 5])
    return {'y': 'zahl', 'f': {'text': f'Die Geraden g und h sind parallel und haben den Abstand {w1} cm. Die Gerade k ist parallel zu h und hat von h den Abstand {w2} cm, liegt aber auf der anderen Seite als g. Welchen Abstand haben g und k?'},
            'o': {'wert': w1 + w2, 'einheit': 'cm'}, 'c': f'{w1} + {w2}', 'w': f'h liegt zwischen g und k: {w1} + {w2} = {w1 + w2} cm.', 'h': 'Mach eine Skizze mit drei parallelen Linien.'}


# ---------- 4 Kreis und Lage ----------
TYP = {-1: 'Sekante (2 Schnittpunkte)', 0: 'Tangente (1 Berührpunkt)', 1: 'Passante (kein gemeinsamer Punkt)'}


KR = set()


def vgl(d, r): return (d > r) - (d < r)


def g_kreis(st):
    if st == 1:
        r = R.randint(2, 9)
        d = R.choice([r, r - R.randint(1, r - 1) if r > 1 else r, r + R.randint(1, 4)])
        t = TYP[vgl(d, r)]
        return {**wahl(R, t, [v for v in TYP.values() if v != t]), 'f': {'text': f'Ein Kreis hat den Radius {r} cm. Eine Gerade hat vom Mittelpunkt den Abstand {d} cm. Was ist die Gerade?'},
                'w': f'd = {d} cm, r = {r} cm: ' + ('d < r, Sekante.' if d < r else 'd = r, Tangente.' if d == r else 'd > r, Passante.'), 'h': 'Vergleiche den Abstand d mit dem Radius r.'}
    if st == 2:
        mx, my, r = R.randint(-4, 4), R.randint(-4, 4), R.randint(2, 6)
        c = my + R.randint(-r - 2, r + 2)
        d = abs(c - my)
        n = 2 if d < r else 1 if d == r else 0
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Kreis um M{p(mx, my)} mit r = {r}. Die Gerade g ist waagrecht mit y = {zt(c)}. Wie viele gemeinsame Punkte haben Kreis und g?',
                                       'grafik': {'typ': 'figur', 'punkte': {'M': [mx, my], '_A': [mx - r - 2, c], '_B': [mx + r + 2, c]}, 'kreise': [{'m': 'M', 'r': r}], 'linien': [['_A', '_B', 'g']]}},
                    'o': {'wert': n}, 'c': f'{n}', 'w': f'Abstand von M zu g: |{zt(c)} − {kl(my)}| = {d}. ' + ('d < r: 2 Punkte.' if n == 2 else 'd = r: 1 Punkt.' if n == 1 else 'd > r: kein Punkt.'),
                    'h': 'Berechne den Abstand von M zur Geraden und vergleiche mit r.'}
        k = R.randint(2, 12)
        return {'y': 'zahl', 'f': {'text': f'Ein Kreis hat den Durchmesser {2 * k} cm. Wie groß ist sein Radius?' if R.random() < .5 else f'Ein Kreis hat den Radius {k} cm. Wie groß ist sein Durchmesser?'},
                'o': {'wert': k if 'Durchmesser ' + str(2 * k) in f'Ein Kreis hat den Durchmesser {2 * k}' else 2 * k, 'einheit': 'cm'}, 'c': f'{k}', 'w': f'Durchmesser = 2 · Radius.', 'h': 'Der Durchmesser ist doppelt so lang wie der Radius.'} if False else \
            {'y': 'zahl', 'f': {'text': f'Ein Kreis um M{p(mx, my)} hat den Radius {r}. Wie heißt die größte y-Koordinate, die ein Punkt auf dem Kreis haben kann?'},
             'o': {'wert': my + r}, 'c': f'({my}) + {r}', 'w': f'Der höchste Kreispunkt liegt {r} über M: {zt(my)} + {r} = {zt(my + r)}.', 'h': 'Gehe vom Mittelpunkt aus um den Radius nach oben.'}
    art = R.randrange(3)
    if art == 0:
        r1, r2 = R.randint(2, 7), R.randint(2, 7)
        e = R.choice([r1 + r2, r1 + r2 + R.randint(1, 4), R.randint(abs(r1 - r2) + 1, r1 + r2 - 1) if r1 + r2 - 1 > abs(r1 - r2) else r1 + r2])
        if r1 != r2 and R.random() < .4:      # ein Kreis im anderen (Prüfung): innen berührend oder ganz innen
            r1, r2 = max(r1, r2), min(r1, r2)
            e = r1 - r2 if R.random() < .5 or r1 - r2 == 1 else R.randint(1, r1 - r2 - 1)
            n = 1 if e == r1 - r2 else 0
            return {'y': 'zahl', 'f': {'text': f'Zwei Kreise haben die Radien {r1} cm und {r2} cm. Ihre Mittelpunkte sind {e} cm voneinander entfernt. Wie viele gemeinsame Punkte haben sie?'},
                    'o': {'wert': n}, 'c': f'{n}',
                    'w': f'r₁ − r₂ = {r1 - r2} cm. ' + ('Der Abstand ist gleich dem Unterschied: Der kleine Kreis berührt den großen von innen (1 Punkt).' if n == 1 else 'Der Abstand ist kleiner als der Unterschied: Der kleine Kreis liegt ganz im großen, kein gemeinsamer Punkt.'),
                    'h': 'Liegt ein Kreis im anderen? Vergleiche den Abstand der Mittelpunkte auch mit r₁ − r₂.'}
        n = 2 if abs(r1 - r2) < e < r1 + r2 else 1 if e == r1 + r2 else 0
        return {'y': 'zahl', 'f': {'text': f'Zwei Kreise haben die Radien {r1} cm und {r2} cm. Ihre Mittelpunkte sind {e} cm voneinander entfernt. Wie viele gemeinsame Punkte haben sie?'},
                'o': {'wert': n}, 'c': f'{n}', 'w': f'r₁ + r₂ = {r1 + r2} cm. ' + ('Abstand gleich der Summe: Sie berühren sich (1 Punkt).' if n == 1 else 'Abstand größer als die Summe: kein gemeinsamer Punkt.' if n == 0 else 'Abstand kleiner als die Summe (und größer als der Unterschied): 2 Schnittpunkte.'),
                'h': 'Vergleiche den Abstand der Mittelpunkte mit r₁ + r₂.'}
    if art == 1:
        r = R.choice([3, 4, 5, 8, 10, 12, 15])
        d = R.choice([r - 2, r + 1, r + 3, r - 1])          # nie genau auf der Grenze (Prüfung)
        ja = d <= r
        rr = 'Ja, der Ort liegt innerhalb der Reichweite.' if ja else 'Nein, der Ort liegt außerhalb der Reichweite.'
        return {**wahl(R, rr, ['Nein, der Ort liegt außerhalb der Reichweite.' if ja else 'Ja, der Ort liegt innerhalb der Reichweite.', 'Das hängt von der Richtung ab.'], 3),
                'f': {'text': f'Ein Funkmast reicht {r} km weit in jede Richtung. Ein Dorf ist {d} km vom Mast entfernt. Hat das Dorf Empfang?'},
                'w': f'Der Empfangsbereich ist ein Kreis mit Radius {r} km. {d} km {"≤" if ja else ">"} {r} km.', 'h': 'Alle Punkte bis zum Abstand r liegen im Kreis – in jede Richtung gleich weit.'}
    mx, my, r = R.randint(-3, 3), R.randint(-3, 3), R.randint(2, 6)
    if (mx, r) in KR: return g_kreis(3)          # keine zwei Aufgaben mit derselben Lösung (Prüfung)
    KR.add((mx, r))
    return luecke([mx - r, mx + r], f'Ein Kreis um M{p(mx, my)} mit r = {r} schneidet die waagrechte Linie durch M in zwei Punkten. Welche x-Koordinaten haben sie? (kleinere zuerst)',
                  'x = □ und x = □', 'Kleinere Zahl zuerst.', [f'({mx}) - {r}', f'({mx}) + {r}'], f'Von M aus {r} nach links: {zt(mx - r)}, {r} nach rechts: {zt(mx + r)}.',
                  'Alle Kreispunkte sind r von M entfernt.')


# ---------- 5 Winkelarten ----------
ARTEN = ['spitz', 'recht', 'stumpf', 'gestreckt', 'überstumpf', 'Vollwinkel']


def art(a):
    if a < 90: return 'spitz'
    if a == 90: return 'recht'
    if a < 180: return 'stumpf'
    if a == 180: return 'gestreckt'
    if a < 360: return 'überstumpf'
    return 'Vollwinkel'


def g_wart(st):
    if st == 1:
        a = R.choice([R.randint(5, 89), 90, R.randint(91, 179), 180, R.randint(181, 359)])
        r = art(a)
        fr = {'text': f'Welche Winkelart ist α = {a}°?'}
        if a <= 180: fr['grafik'] = winkelfigur(a, 'α')
        return {**wahl(R, r, [x for x in ARTEN if x != r]), 'f': fr,
                'w': f'{a}° ' + {'spitz': 'ist kleiner als 90°: spitz.', 'recht': 'ist genau 90°: rechter Winkel.', 'stumpf': 'liegt zwischen 90° und 180°: stumpf.',
                                 'gestreckt': 'ist genau 180°: gestreckt.', 'überstumpf': 'liegt zwischen 180° und 360°: überstumpf.'}[r], 'h': 'Vergleiche mit 90°, 180° und 360°.'}
    if st == 2:
        if R.random() < .3:          # Winkel schätzen am Bild (Prüfung)
            a = R.choice([20, 30, 40, 50, 60, 70, 110, 120, 130, 140, 150, 160])
            f = [180 - a, 360 - a, 90 if abs(a - 90) >= 40 else (a + 60 if a < 90 else a - 60)]
            return {**wahl_rund(R, f'{a}°', [f'{x}°' for x in f]), 'f': {'text': 'Schätze: Wie groß ist der Winkel α ungefähr?', 'grafik': winkelfigur(a, 'α')},
                    'w': f'α ist {"kleiner" if a < 90 else "größer"} als ein rechter Winkel und kleiner als 180°: etwa {a}°. {180 - a}° wäre der Winkel auf der anderen Seite des gestreckten Winkels.',
                    'h': 'Vergleiche mit einem rechten Winkel (90°) und einem gestreckten Winkel (180°).'}
        a = R.randint(10, 170)
        if a == 90: a = 95
        return {'y': 'zahl', 'f': {'text': f'Zwei Schenkel bilden einen Winkel von {a}°. Wie groß ist der überstumpfe Winkel zwischen denselben Schenkeln (auf der anderen Seite)?'},
                'o': {'wert': 360 - a, 'einheit': '°'}, 'c': f'360 - {a}', 'w': f'Beide Winkel zusammen ergeben den Vollwinkel: 360° − {a}° = {360 - a}°.', 'h': 'Beide Winkel zusammen ergeben 360°.'} if R.random() < .5 else \
            {**wahl(R, art(a), [x for x in ARTEN if x != art(a)]), 'f': {'text': f'Ein Winkel ist halb so groß wie ein Winkel von {2 * a}°. Welche Winkelart ist er?' if a % 2 == 0 else f'Ein Winkel ist 10° kleiner als ein Winkel von {a + 10}°. Welche Winkelart ist er?'},
             'w': f'Der Winkel ist {a}°, also {art(a)}.', 'h': 'Rechne zuerst die Größe des Winkels aus.'}
    k = R.randrange(3)
    if k == 0:
        a = R.randint(185, 350)
        return {'y': 'zahl', 'f': {'text': f'Ein Geodreieck misst nur bis 180°. Um α = {a}° zu zeichnen, zeichnest du zuerst den Winkel auf der anderen Seite. Wie groß ist er?'},
                'o': {'wert': 360 - a, 'einheit': '°'}, 'c': f'360 - {a}', 'w': f'360° − {a}° = {360 - a}°. Diesen zeichnest du, der Rest bis zum Vollwinkel ist α.', 'h': 'α und der andere Winkel ergeben zusammen 360°.'}
    if k == 1:
        teile = R.choice([2, 3, 4, 5, 6, 8, 9, 10, 12])
        return {'y': 'zahl', 'f': {'text': f'Ein Vollwinkel wird in {teile} gleich große Winkel geteilt. Wie groß ist ein Winkel?'}, 'o': {'wert': wert(Fr(360, teile)), 'einheit': '°'}, 'c': f'360 / {teile}',
                'w': f'360° : {teile} = {zt(Fr(360, teile))}°.', 'h': 'Ein Vollwinkel hat 360°.'}
    a, b = R.randint(20, 160), R.randint(20, 160)
    s = a + b
    r = art(s)
    return {**wahl(R, r, [x for x in ARTEN if x != r]), 'f': {'text': f'Zwei Winkel {a}° und {b}° liegen direkt nebeneinander (gemeinsamer Schenkel). Welche Art hat der zusammengesetzte Winkel?'},
            'w': f'{a}° + {b}° = {s}°, also {r}.', 'h': 'Addiere die beiden Winkel.'}


# ---------- 6 Vierecke ----------
ART = {'Quadrat': 'ein', 'Rechteck': 'ein', 'Raute': 'eine', 'Parallelogramm': 'ein', 'Trapez': 'ein', 'Drachenviereck': 'ein'}


def vfigur(typ, a, c):
    import math
    if typ == 'Quadrat': pk = {'A': [0, 0], 'B': [a, 0], 'C': [a, a], 'D': [0, a]}
    elif typ == 'Rechteck': pk = {'A': [0, 0], 'B': [c, 0], 'C': [c, a], 'D': [0, a]}
    elif typ == 'Raute':
        w = math.radians(60 + a)
        pk = {'A': [0, 0], 'B': [a, 0], 'C': [round(a + a * math.cos(w), 3), round(a * math.sin(w), 3)], 'D': [round(a * math.cos(w), 3), round(a * math.sin(w), 3)]}
    else:
        wd = 0.6 * a
        pk = {'A': [-wd, 0], 'B': [0, round(0.8 * a, 3)], 'C': [wd, 0], 'D': [0, -round(math.sqrt(c * c - wd * wd), 3)]}
        pk['A'][0] = round(pk['A'][0], 3); pk['C'][0] = round(pk['C'][0], 3)
    g = {'typ': 'figur', 'punkte': pk, 'flaeche': ['A', 'B', 'C', 'D'], 'linien': [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A']]}
    if typ in ('Quadrat', 'Rechteck'): g['rechter_winkel'] = [['A', 'B', 'D'], ['B', 'C', 'A'], ['C', 'D', 'B'], ['D', 'A', 'C']]
    return g


BESCHR = [('4 gleich lange Seiten und 4 rechte Winkel', 'Quadrat', ['Raute', 'Rechteck', 'Drachenviereck']),
          ('4 rechte Winkel, aber nicht alle Seiten gleich lang', 'Rechteck', ['Quadrat', 'Raute', 'Trapez']),
          ('4 gleich lange Seiten, aber keinen rechten Winkel', 'Raute', ['Quadrat', 'Rechteck', 'Drachenviereck']),
          ('zwei Paare paralleler Seiten, keine rechten Winkel, nicht alle Seiten gleich lang', 'Parallelogramm', ['Rechteck', 'Raute', 'Drachenviereck']),
          ('genau ein Paar paralleler Seiten', 'Trapez', ['Parallelogramm', 'Rechteck', 'Drachenviereck']),
          ('zwei Paare gleich langer benachbarter Seiten, aber nicht alle vier gleich lang', 'Drachenviereck', ['Raute', 'Parallelogramm', 'Trapez'])]


def g_viereck(st):
    if st == 1:
        b, r, f = R.choice(BESCHR)
        if R.random() < .5:
            return {**wahl(R, r, f), 'f': {'text': f'Ein Viereck hat {b}. Wie heißt es?'}, 'w': f'Das ist {ART[r]} {r}.', 'h': 'Prüfe Seitenlängen, rechte Winkel und parallele Seiten.'}
        a = R.randint(3, 12)
        c = a + R.randint(1, 6)
        typ = R.choice(['Quadrat', 'Rechteck', 'Raute', 'Drachen'])
        if typ == 'Quadrat': t, r = f'Alle Seiten sind {a} cm lang, alle Winkel sind 90°.', 'Quadrat'
        elif typ == 'Rechteck': t, r = f'Die Seiten sind {a} cm, {c} cm, {a} cm und {c} cm lang, alle Winkel sind 90°.', 'Rechteck'
        elif typ == 'Raute': t, r = f'Alle Seiten sind {a} cm lang, die Winkel sind {60 + a}° und {120 - a}°.', 'Raute'
        else: t, r = f'Die Seiten sind der Reihe nach {a} cm, {a} cm, {c} cm und {c} cm lang.', 'Drachenviereck'
        return {**wahl(R, r, [x for x in ['Quadrat', 'Rechteck', 'Raute', 'Drachenviereck', 'Trapez'] if x != r][:3]), 'f': {'text': f'{t} Welches Viereck ist das (genauester Name)?', 'grafik': vfigur(typ, a, c)},
                'w': f'Das ist {ART[r]} {r}.', 'h': 'Welche Eigenschaften hat es genau? Nimm den genauesten Namen.'}
    if st == 2 and R.random() < .45:      # Viereck aus Koordinaten erkennen (Prüfung)
        typ = R.choice(['Quadrat', 'Rechteck', 'Parallelogramm', 'Trapez', 'Raute', 'Drachenviereck'])
        a, b = R.sample(range(2, 7), 2)
        if typ == 'Quadrat': pts = [(0, 0), (a, 0), (a, a), (0, a)]
        elif typ == 'Rechteck': pts = [(0, 0), (a, 0), (a, b), (0, b)]
        elif typ == 'Parallelogramm':
            s_ = R.randint(1, 3); pts = [(0, 0), (a, 0), (a + s_, b), (s_, b)]
            if s_ * s_ + b * b == a * a: return g_viereck(st)          # wäre eine Raute
        elif typ == 'Trapez': s_ = R.randint(1, 2); pts = [(0, 0), (a + 2 * s_ + 1, 0), (a + s_ + 1, b), (s_, b)]
        elif typ == 'Raute': pts = [(0, -b), (a, 0), (0, b), (-a, 0)]
        else:
            c = b + R.randint(1, 3); pts = [(0, -c), (a, 0), (0, b), (-a, 0)]
        dx, dy = R.randint(-3, 2), R.randint(-3, 2)
        pts = [(x + dx, y + dy) for x, y in pts]
        namen = 'ABCD'
        nahe = {'Quadrat': ['Rechteck', 'Raute', 'Parallelogramm'], 'Rechteck': ['Quadrat', 'Parallelogramm', 'Trapez'], 'Parallelogramm': ['Rechteck', 'Trapez', 'Raute'],
                'Trapez': ['Parallelogramm', 'Drachenviereck', 'Rechteck'], 'Raute': ['Quadrat', 'Drachenviereck', 'Parallelogramm'], 'Drachenviereck': ['Raute', 'Trapez', 'Parallelogramm']}[typ]
        warum = {'Quadrat': 'alle Seiten gleich lang und alle Winkel 90°', 'Rechteck': 'alle Winkel 90°, aber zwei verschiedene Seitenlängen',
                 'Parallelogramm': 'zwei Paare paralleler Seiten, aber keine rechten Winkel', 'Trapez': 'nur die untere und die obere Seite sind parallel',
                 'Raute': 'alle vier Seiten sind gleich lang, aber es gibt keine rechten Winkel', 'Drachenviereck': 'je zwei benachbarte Seiten sind gleich lang, aber nicht alle vier'}[typ]
        return {**wahl_rund(R, typ, nahe), 'f': {'text': 'Das Viereck ABCD hat die Ecken ' + ', '.join(f'{namen[k]}{p(*q)}' for k, q in enumerate(pts)) + '. Wie heißt es (genauester Name)?',
                                                 'grafik': ks([(q[0], q[1], namen[k]) for k, q in enumerate(pts)], [(*pts[k], *pts[(k + 1) % 4]) for k in range(4)])},
                'w': f'Es ist {ART[typ]} {typ}: {warum}.', 'h': 'Prüfe: parallele Seiten, gleich lange Seiten, rechte Winkel.'}
    if st == 2:
        x1, y1 = R.randint(-6, 2), R.randint(-6, 2)
        a, h, s = R.randint(3, 6), R.randint(2, 5), R.randint(1, 3)
        A, B, C = (x1, y1), (x1 + a, y1), (x1 + a + s, y1 + h)
        D = (x1 + s, y1 + h)
        return mit(punkt('D', D[0], D[1], f'ABCD ist ein Parallelogramm mit A{p(*A)}, B{p(*B)} und C{p(*C)}. Welche Koordinaten hat D?',
                     f'Von B nach C geht es {s} nach rechts und {h} nach oben. Dasselbe von A aus: D{p(*D)}.', 'Die Seite [AD] ist parallel und gleich lang wie [BC]: gleiche Verschiebung.',
                     f'({x1}) + {s}', f'({y1}) + {h}'), ks([(A[0], A[1], 'A'), (B[0], B[1], 'B'), (C[0], C[1], 'C')], [(A[0], A[1], B[0], B[1]), (B[0], B[1], C[0], C[1])]))
    aussagen = [  # Prüfung: konkrete Lösungswege, Ablenker aus Denkfehlern
        ('Jedes Quadrat ist ein Rechteck.', 'Ja: Ein Quadrat hat vier rechte Winkel wie jedes Rechteck.', ['Nein: Ein Rechteck muss zwei verschiedene Seitenlängen haben.', 'Nein: Ein Quadrat hat keine rechten Winkel.']),
        ('Jedes Rechteck ist ein Quadrat.', 'Nein: Ein Rechteck mit 3 cm und 5 cm langen Seiten ist kein Quadrat.', ['Ja: Beide haben vier rechte Winkel.', 'Ja: Beide haben vier gleich lange Seiten.']),
        ('Jede Raute ist ein Parallelogramm.', 'Ja: Jede Raute hat zwei Paare paralleler Seiten.', ['Nein, nur wenn alle Winkel 90° sind.', 'Nein: Eine Raute hat keine parallelen Seiten.']),
        ('Jedes Parallelogramm ist ein Trapez.', 'Ja: Ein Trapez braucht ein Paar paralleler Seiten, ein Parallelogramm hat sogar zwei.', ['Nein: Ein Parallelogramm hat keine parallelen Seiten.', 'Nein, nur wenn alle Winkel 90° sind.']),
        ('Jedes Trapez ist ein Parallelogramm.', 'Nein: Ein Trapez mit nur einem Paar paralleler Seiten ist kein Parallelogramm.', ['Ja: Beide haben parallele Seiten.', 'Ja, aber nur wenn alle Winkel 90° sind.']),
        ('Jedes Quadrat ist eine Raute.', 'Ja: Ein Quadrat hat vier gleich lange Seiten wie jede Raute.', ['Nein: Eine Raute darf keine rechten Winkel haben.', 'Nein: Ein Quadrat hat nur zwei gleich lange Seiten.']),
        ('Jede Raute ist ein Quadrat.', 'Nein: Eine Raute ohne rechte Winkel ist kein Quadrat.', ['Ja: Beide haben vier gleich lange Seiten.', 'Ja: Jede Raute hat vier rechte Winkel.']),
        ('Jedes Rechteck ist ein Parallelogramm.', 'Ja: Gegenüberliegende Seiten eines Rechtecks sind parallel.', ['Nein: Ein Parallelogramm darf keine rechten Winkel haben.', 'Nein, nur wenn alle Seiten gleich lang sind.']),
        ('Jede Raute ist ein Drachenviereck.', 'Ja: Bei einer Raute sind auch je zwei benachbarte Seiten gleich lang.', ['Nein: Ein Drachenviereck hat keine gleich langen Seiten.', 'Nein, nur wenn alle Winkel 90° sind.']),
        ('Jedes Drachenviereck ist eine Raute.', 'Nein: Ein Drachenviereck mit den Seiten 3 cm, 3 cm, 5 cm, 5 cm ist keine Raute.', ['Ja: Beide haben gleich lange benachbarte Seiten.', 'Ja, aber nur wenn alle Winkel 90° sind.'])]
    s_, r, f = R.choice(aussagen)
    return {**wahl_rund(R, r, f, 3), 'f': {'text': f'Stimmt die Aussage? „{s_}“'}, 'w': r,
            'h': 'Hat das erste Viereck immer alle Eigenschaften des zweiten? Suche ein Gegenbeispiel.'}


# ---------- 7 Verstehen ----------
# Prüfung: jede Antwort mit gleich gebauter Begründung; höchstens 4 Aufgaben je Muster
MUSTER = {}


def g_vers(st):
    x, y = R.randint(1, 8), R.randint(1, 8)
    if x == y: y += 1
    r = R.randint(2, 6)
    if st == 1:
        aussagen = [('tausch', f'Der Punkt ({x} | {y}) ist derselbe wie ({y} | {x}).', f'Nein: ({x} | {y}) liegt {x} rechts und {y} oben, ({y} | {x}) umgekehrt.', [f'Ja: Beide Punkte haben die Zahlen {x} und {y}.', 'Ja: Die Reihenfolge der Koordinaten ist egal.']),
                    ('messen', 'Eine Strecke kann man messen, eine Gerade nicht.', 'Ja: Eine Strecke hat zwei Endpunkte, eine Gerade ist unendlich lang.', ['Nein: Beide kann man mit dem Lineal messen.', 'Nein: Nur eine Gerade hat eine Länge.']),
                    ('spitz', f'Ein Winkel von {90 + x}° ist spitz.', f'Nein: {90 + x}° ist größer als 90°, also stumpf.', [f'Ja: {90 + x}° ist kleiner als 180°.', f'Nein: {90 + x}° ist überstumpf.']),
                    ('kreis', f'Ein Kreis mit Radius {r} cm hat den Durchmesser {2 * r} cm.', f'Ja: Der Durchmesser ist doppelt so lang: 2 · {r} cm = {2 * r} cm.', [f'Nein: Der Durchmesser ist halb so lang: {zt(Fr(r, 2))} cm.', f'Nein: Der Durchmesser ist so lang wie der Radius: {r} cm.'])]
    elif st == 2:
        aussagen = [('links', f'Der Punkt (−{x} | {y}) liegt links von der y-Achse.', 'Ja: Eine negative x-Koordinate heißt links.', ['Nein: Er liegt rechts, weil y positiv ist.', 'Nein: Er liegt unter der x-Achse.']),
                    ('unten', f'Der Punkt ({x} | −{y}) liegt unter der x-Achse.', 'Ja: Eine negative y-Koordinate heißt unten.', ['Nein: Er liegt links, weil eine Koordinate negativ ist.', 'Nein: Er liegt oben, weil x positiv ist.']),
                    ('strecke', f'Die Strecke von (−{x} | 0) bis ({y} | 0) ist {abs(y - x)} lang.', f'Nein: Sie ist {x} + {y} = {x + y} lang.', [f'Ja: denn {max(x, y)} − {min(x, y)} = {abs(y - x)}.', f'Nein: Sie ist {max(x, y)} lang, man zählt nur bis zur größeren Zahl.']),
                    ('tangente', f'Eine Gerade mit Abstand {r} cm vom Mittelpunkt eines Kreises mit r = {r} cm ist eine Sekante.', 'Nein: d = r, das ist eine Tangente mit genau einem Berührpunkt.', ['Ja: Jede Gerade, die den Kreis trifft, ist eine Sekante.', 'Nein: d = r, das ist eine Passante.']),
                    ('abstand', f'Der Punkt P({x} | {y}) hat von der x-Achse den Abstand {x}.', f'Nein: Der Abstand zur x-Achse ist die y-Koordinate, also {y}.', [f'Ja: Der Abstand ist immer die erste Koordinate, also {x}.', f'Nein: Der Abstand ist {x} + {y} = {x + y}.']),
                    ('lot', 'Zwei Geraden, die beide senkrecht zu einer dritten sind, sind parallel zueinander.', 'Ja: Beide stehen im rechten Winkel auf derselben Geraden.', ['Nein: Sie stehen senkrecht zueinander.', 'Nein: Sie schneiden sich auf der dritten Geraden.'])]
    else:
        aussagen = [('drei', 'Zwei Kreise können genau drei gemeinsame Punkte haben.', 'Nein: Möglich sind nur 0, 1 oder 2 gemeinsame Punkte (oder alle, wenn die Kreise gleich sind).', ['Ja: wenn sich die Kreise oft genug überlappen.', 'Ja: wenn ein Kreis im anderen liegt.']),
                    ('raute', 'Jedes Viereck mit vier gleich langen Seiten ist ein Quadrat.', 'Nein: Eine Raute ohne rechte Winkel hat auch vier gleich lange Seiten.', ['Ja: Vier gleich lange Seiten reichen für ein Quadrat.', 'Ja, wenn die Seiten länger als 1 cm sind.']),
                    ('senkrecht', 'Der Abstand eines Punktes zu einer Geraden wird senkrecht gemessen.', 'Ja: entlang des Lots – das ist die kürzeste Verbindung.', ['Nein: Man misst immer waagrecht.', 'Nein: Man darf in jede Richtung messen.']),
                    ('ueber', f'Ein Winkel von {180 + x * 10}° ist stumpf.', f'Nein: {180 + x * 10}° liegt zwischen 180° und 360°, also überstumpf.', [f'Ja: {180 + x * 10}° ist größer als 90°.', f'Nein: {180 + x * 10}° ist ein gestreckter Winkel.']),
                    ('tangente2', 'Eine Tangente schneidet den Kreis in zwei Punkten.', 'Nein: Eine Tangente berührt den Kreis in genau einem Punkt.', ['Ja: Jede Gerade durch einen Kreis hat zwei Schnittpunkte.', 'Nein: Eine Tangente hat keinen gemeinsamen Punkt mit dem Kreis.'])]
    frei = [a for a in aussagen if MUSTER.get(a[0], 0) < 4]
    k, s_, r_, f = R.choice(frei)
    MUSTER[k] = MUSTER.get(k, 0) + 1
    return {**wahl_rund(R, r_, f, 3), 'f': {'text': f'Stimmt die Aussage? „{s_}“'}, 'w': r_, 'h': 'Mach eine Skizze oder suche ein Gegenbeispiel.'}


GEN = {'koordinaten': g_koord, 'strecken': g_strecke, 'lagebeziehungen': g_lage, 'kreis_lage': g_kreis, 'winkelarten': g_wart, 'vierecke': g_viereck, 'verstehen': g_vers}

DATEI = datei(E, 'Punkte, Strecken, Geraden und Kreise im Koordinatensystem beschreiben, Lagebeziehungen erkennen, Winkelarten bis 360° und besondere Vierecke unterscheiden.', MERKE,
              [('Koordinatensystem', ['koordinaten', 'strecken']),
               ('Lagebeziehungen', ['lagebeziehungen', 'kreis_lage']),
               ('Winkel und Vierecke', ['winkelarten', 'vierecke', 'verstehen'])],
              ETAPPEN, GEN,
              offen=['Zeichnungen (neu ab 14.11.) eingebaut: Koordinatensystem in koordinaten, strecken, lagebeziehungen, vierecke; Figuren für Kreis/Gerade, Winkel und Vierecke. Überstumpfe Winkel werden nicht gezeichnet (unklar, auf welcher Seite die App den Bogen zeichnet).',
                     'Lehrplan „Winkel bis 360° messen und zeichnen“: Messen mit dem Geodreieck und Zeichnen durch das Kind geht in der App nicht; enthalten sind Winkelarten und Rechnen mit Winkelgrößen.',
                     'Dreiecksarten aus „umfang“ weggelassen: LehrplanPLUS Kl. 5 nennt nur die Vierecke Quadrat, Rechteck, Parallelogramm, Raute, Drachenviereck und Trapez.'])

# Umbau U5 (Achte Runde, Vorgabe 16.11.): Lernkarten nach dem neuen Muster – einstieg, woerter (≤ 3), Kartenbild,
# Bildergeschichte (schritte mit bild), „Pass auf!“ (fehler + fehler_bild), MERKE (regel).
# Situationen: Schatzkarte, Häuser am Marktplatz, Schienen und Laternenpfahl, Rasensprenger, Schere, Fliesen, Pinguin.
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl5.py) – die Aufgaben bleiben wörtlich gleich.
import math  # noqa: E402

from _umbau_kl5 import umbau  # noqa: E402

P, P2 = {'x': 3, 'y': -2, 'name': 'P'}, {'x': -1, 'y': 3, 'name': 'P′'}
SCHERE = lambda g: [round(5 * math.cos(math.radians(g)), 3), round(5 * math.sin(math.radians(g)), 3)]
RAUTE = {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [4, 0], 'C': [6.4, 3.2], 'D': [2.4, 3.2]}, 'flaeche': ['A', 'B', 'C', 'D'],
         'linien': [['A', 'B', '4 cm'], ['B', 'C', '4 cm'], ['C', 'D', '4 cm'], ['D', 'A', '4 cm']]}
KREIS = {'typ': 'figur', 'punkte': {'M': [0, 0], '_T': [0, 4], '_A': [-6, 4], '_B': [6, 4], '_S1': [-6, 2], '_S2': [6, 2], '_P1': [-6, 6], '_P2': [6, 6]},
         'kreise': [{'m': 'M', 'r': 4}], 'linien': [['M', '_T', 'r = 4 cm']]}

KARTEN = {
 'koordinaten': {
  'einstieg': 'Auf einer Schatzkarte steht: 3 Schritte nach rechts, dann 2 nach unten. Zwei Angaben genügen für jeden Ort. Mathe nutzt dafür ein Gitter mit zwei Achsen: das ⟦Koordinatensystem⟧.',
  'woerter': [['Koordinatensystem', 'zwei Zahlengeraden, die sich rechtwinklig kreuzen: x-Achse waagrecht, y-Achse senkrecht'],
              ['Ursprung', 'der Kreuzungspunkt O(0 | 0); dort startest du'], ['P(3 | −2)', 'Punkt P: erste Zahl x (rechts/links), zweite Zahl y (oben/unten)']],
  'bild': {'typ': 'koordinaten', 'x': [-3, 5], 'y': [-4, 5]},
  'schritte': [{'text': 'P(3 | −2): Vom Ursprung 3 nach rechts.', 'bild': {'strecken': [[0, 0, 3, 0, 'gestrichelt']]}},
               {'text': 'Dann 2 nach unten. Dort liegt P.', 'bild': {'strecken': [[0, 0, 3, 0, 'gestrichelt'], [3, 0, 3, -2, 'gestrichelt']], 'punkte': [P]}},
               {'text': 'Verschieben: 4 nach links heißt x − 4, 5 nach oben y + 5.',
                'bild': {'strecken': [[3, -2, -1, -2, 'gestrichelt'], [-1, -2, -1, 3, 'gestrichelt']], 'punkte': [P, P2]}},
               {'text': 'Also x = −1 und y = 3: ⟦P′(−1 | 3)⟧.'}],
  'fehler': 'P(3 | −2) und Q(−2 | 3) verwechseln. Das sind zwei verschiedene Orte. Die x-Zahl steht immer zuerst.',
  'fehler_bild': {'strecken': [], 'punkte': [P, {'x': -2, 'y': 3, 'name': 'Q'}]},
  'regel': 'Erste Zahl: nach rechts (+) oder links (−). Zweite Zahl: nach oben (+) oder unten (−). Start ist der ⟦Ursprung⟧.'},
 'strecken': {
  'einstieg': 'Ein Haus steht 3 Häuser links vom Marktplatz, ein anderes 4 Häuser rechts davon. Wie weit sind sie auseinander? Über den Platz hinweg: 3 + 4 = 7, die Länge der ⟦Strecke⟧.',
  'woerter': [['Strecke [AB]', 'die gerade Verbindung von A nach B'], ['Einheit', 'hier: ein Kästchen im Koordinatensystem']],
  'bild': {'typ': 'koordinaten', 'x': [-4, 5], 'y': [-1, 4], 'punkte': [{'x': -3, 'y': 2, 'name': 'A'}, {'x': 4, 'y': 2, 'name': 'B'}]},
  'schritte': [{'text': 'A(−3 | 2) und B(4 | 2) liegen auf gleicher Höhe, bei y = 2.'},
               {'text': 'Von −3 bis 0 sind es 3 Einheiten.', 'bild': {'strecken': [[-3, 2, 0, 2]]}},
               {'text': 'Von 0 bis 4 sind es noch 4 Einheiten.', 'bild': {'strecken': [[-3, 2, 0, 2], [0, 2, 4, 2]]}},
               {'text': 'Zusammen ist die Strecke [AB] ⟦7⟧ Einheiten lang.'}],
  'fehler': '4 − 3 = 1 ist falsch. A und B liegen auf verschiedenen Seiten der 0, wie die Häuser am Marktplatz.',
  'regel': 'Liegt die 0 zwischen den Punkten, ⟦addierst⟧ du die beiden Teile. Sonst ziehst du die Koordinaten voneinander ab.'},
 'lagebeziehungen': {
  'einstieg': 'Eisenbahnschienen laufen parallel: Sie treffen sich nie. Ein Laternenpfahl steht senkrecht auf der Straße. Wie zwei Linien zueinander liegen, heißt ⟦Lagebeziehung⟧.',
  'woerter': [['parallel', 'schneiden sich nie, überall gleich weit voneinander – wie Schienen'], ['senkrecht', 'schneiden sich im rechten Winkel – wie Pfahl und Straße'],
              ['Lot', 'die senkrechte Linie von einem Punkt auf eine Gerade; ihre Länge ist der Abstand']],
  'bild': {'typ': 'koordinaten', 'x': [-1, 7], 'y': [-1, 7], 'punkte': [{'x': 4, 'y': 6, 'name': 'P'}], 'waagrecht': [1]},
  'schritte': [{'text': 'Die Gerade g läuft waagrecht bei y = 1. Gesucht: Abstand von P(4 | 6).'},
               {'text': 'Fälle das Lot: senkrecht von P nach unten bis zu g.', 'bild': {'strecken': [[4, 6, 4, 1, 'gestrichelt']]}},
               {'text': 'Das Lot ist 6 − 1 = ⟦5⟧ Einheiten lang. Das ist der Abstand.'}],
  'fehler': 'Den Abstand schräg messen ist falsch. Schräg ist der Weg länger. Der Abstand ist der kürzeste Weg: das Lot.',
  'fehler_bild': {'strecken': [[4, 6, 4, 1, 'gestrichelt'], [4, 6, 1, 1]]},
  'regel': 'Der ⟦Abstand⟧ ist die Länge des Lots. Parallel heißt: nie schneiden. Senkrecht heißt: Schnitt im rechten Winkel.'},
 'kreis_lage': {
  'einstieg': 'Ein Rasensprenger erreicht alles bis 4 m, das ist der Radius. Ein gerader Weg kann den nassen Kreis queren, berühren oder verfehlen. Es kommt auf seinen Abstand zum ⟦Mittelpunkt⟧ an.',
  'woerter': [['Tangente', 'berührt den Kreis in genau 1 Punkt; Abstand gleich Radius'], ['Sekante', 'schneidet den Kreis in 2 Punkten; Abstand kleiner als der Radius'],
              ['Passante', 'verfehlt den Kreis; Abstand größer als der Radius']],
  'bild': KREIS,
  'schritte': [{'text': 'Radius r = 4 cm. Ein Weg ist 4 cm vom Mittelpunkt M entfernt.'},
               {'text': 'Abstand gleich Radius: Er berührt den Kreis genau einmal. Das ist eine ⟦Tangente⟧.',
                'bild': {'linien': [['M', '_T', 'r = 4 cm'], ['_A', '_B', 'Tangente']]}},
               {'text': 'Näher als 4 cm: Die Sekante schneidet zweimal. Weiter weg: Die Passante verfehlt ihn.',
                'bild': {'linien': [['M', '_T', 'r = 4 cm'], ['_A', '_B', 'Tangente'], ['_S1', '_S2', 'Sekante'], ['_P1', '_P2', 'Passante']]}},
               # Fünfzehnte Runde: zwei Kreise (passend zu den Stufe-3-Aufgaben) – Abstand der Mittelpunkte mit r₁ + r₂ vergleichen
               {'text': 'Radius 3 m und 2 m, Mittelpunkte 5 m entfernt: Die Kreise ⟦berühren sich⟧.',
                'bild': {'punkte': {'M₁': [0, 0], 'M₂': [5, 0], '_R1': [0, 3], '_R2': [5, 2]}, 'kreise': [{'m': 'M₁', 'r': 3}, {'m': 'M₂', 'r': 2}],
                         'linien': [['M₁', '_R1', '3 m'], ['M₂', '_R2', '2 m'], ['M₁', 'M₂', '5 m', 'gestrichelt']]}},
               {'text': 'Mittelpunkte 7 m entfernt, mehr als 3 + 2 = 5: Die Kreise liegen ⟦getrennt⟧.',
                'bild': {'punkte': {'M₁': [0, 0], 'M₂': [7, 0], '_R1': [0, 3], '_R2': [7, 2]}, 'kreise': [{'m': 'M₁', 'r': 3}, {'m': 'M₂', 'r': 2}],
                         'linien': [['M₁', '_R1', '3 m'], ['M₂', '_R2', '2 m'], ['M₁', 'M₂', '7 m', 'gestrichelt']]}}],
  'fehler': 'Bei Abstand gleich Radius von zwei Schnittpunkten sprechen ist falsch. Der Weg streift den nassen Kreis nur an einer Stelle.',
  'regel': 'Vergleiche den Abstand ⟦d⟧ mit dem Radius r. Kleiner: Sekante, gleich: Tangente, größer: Passante.'},
 'winkelarten': {
  'einstieg': 'Öffnest du eine Schere ein wenig, entsteht eine schmale Spitze. Weiter geöffnet wird sie breiter. Die Öffnung zwischen zwei Linien heißt ⟦Winkel⟧, gemessen in Grad.',
  'woerter': [['Winkel', 'die Öffnung zwischen zwei Linien mit gemeinsamem Anfangspunkt'], ['Schenkel', 'die beiden Linien, wie die Klingen der Schere'],
              ['°', 'Grad: eine ganze Drehung hat 360°']],
  'bild': {'typ': 'figur', 'punkte': {'S': [0, 0], '_A': [5, 0], '_B': SCHERE(45)}, 'linien': [['S', '_A', 'Schenkel'], ['S', '_B', 'Schenkel']], 'winkel': [['S', '_A', '_B', '45°']]},
  'schritte': [{'text': 'Die Schenkel sind wenig geöffnet: 45°. Unter 90° heißt der Winkel spitz.'},
               {'text': 'Genau 90° ist ein rechter Winkel, wie eine Heftecke.',
                'bild': {'punkte': {'S': [0, 0], '_A': [5, 0], '_B': SCHERE(90)}, 'winkel': [], 'rechter_winkel': [['S', '_A', '_B']]}},
               {'text': '135° ist mehr als 90° und weniger als 180°: ⟦stumpf⟧.',
                'bild': {'punkte': {'S': [0, 0], '_A': [5, 0], '_B': SCHERE(135)}, 'winkel': [['S', '_A', '_B', '135°']], 'rechter_winkel': []}}],
  'fehler': 'Einen Winkel von 235° stumpf nennen ist falsch. Größer als 180° heißt er überstumpf.',
  'regel': 'Spitz unter 90°, ⟦recht⟧ genau 90°, stumpf bis 180°. Genau 180° gestreckt, darüber überstumpf, 360° Vollwinkel.'},
 'vierecke': {
  'einstieg': 'Fenster, Drachen, Rautenfliese: Alle haben vier Ecken, sehen aber verschieden aus. Den Unterschied machen Seiten und Winkel. Danach bekommen ⟦besondere Vierecke⟧ eigene Namen.',
  'woerter': [['Raute', '4 gleich lange Seiten'], ['Quadrat', '4 gleich lange Seiten und 4 rechte Winkel'], ['rechter Winkel', 'eine Ecke wie beim Blatt Papier: 90°']],
  'bild': {'typ': 'tabelle', 'kopf': ['Viereck', 'Seiten', 'Winkel'],
           'zeilen': [['Quadrat', '4 gleich lang', '4 rechte'], ['Rechteck', 'Gegenseiten gleich', '4 rechte'], ['Raute', '4 gleich lang', 'beliebig'],
                      ['Parallelogramm', 'Gegenseiten parallel', 'beliebig'], ['Trapez', '2 Seiten parallel', 'beliebig'],
                      ['Drachen', '2 Paare gleicher Nachbarseiten', 'beliebig']]},
  'schritte': [{'text': 'Alle vier Seiten dieses Vierecks sind 4 cm lang.', 'bild': RAUTE},
               {'text': 'Das passt zu Quadrat und Raute.'},
               {'text': 'Ein Quadrat braucht 4 rechte Winkel. Hier ist kein rechter Winkel: also eine ⟦Raute⟧.'}],
  'fehler': '„Ein Quadrat ist keine Raute“ ist falsch. Ein Quadrat hat 4 gleich lange Seiten, also ist es auch eine Raute.',
  'fehler_bild': {'punkte': {'A': [0, 0], 'B': [4, 0], 'C': [4, 4], 'D': [0, 4]}, 'rechter_winkel': [['A', 'B', 'D'], ['B', 'C', 'A'], ['C', 'D', 'B'], ['D', 'A', 'C']]},
  'regel': 'Prüfe ⟦Seiten⟧, parallele Seiten und rechte Winkel. Nimm den genauesten Namen, der passt.'},
 'verstehen': {
  'einstieg': 'Ein Freund sagt: „Alle Vögel können fliegen.“ Ein einziger Pinguin zeigt, dass das nicht stimmt. So ein Fall heißt ⟦Gegenbeispiel⟧.',
  'woerter': [['Gegenbeispiel', 'ein Fall, bei dem eine „immer“-Aussage nicht stimmt'], ['Aussage', 'ein Satz, der richtig oder falsch ist']],
  'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [6, 0], 'C': [6, 3], 'D': [0, 3]}, 'flaeche': ['A', 'B', 'C', 'D'],
           'linien': [['A', 'B', '6 cm'], ['B', 'C', '3 cm'], ['C', 'D'], ['D', 'A']], 'rechter_winkel': [['A', 'B', 'D'], ['B', 'C', 'A'], ['C', 'D', 'B'], ['D', 'A', 'C']]},
  'schritte': [{'text': 'Aussage: „Jedes Rechteck ist ein Quadrat.“'},
               {'text': 'Gegenbeispiel: Dieses Rechteck mit 6 cm und 3 cm hat 4 rechte Winkel.'},
               {'text': 'Seine Seiten sind aber nicht gleich lang. Die Aussage ist ⟦falsch⟧.'}],
  'fehler': 'Eine „immer“-Aussage mit einem passenden Beispiel beweisen wollen reicht nicht. Ein Gegenbeispiel genügt aber, um sie zu widerlegen.',
  'regel': 'Ein einziges ⟦Gegenbeispiel⟧ widerlegt eine „immer“-Aussage. Mach dir dazu eine Skizze.'},
}
umbau(DATEI, KARTEN)


# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl5) ----------
# Neue Übungen nach Prüfungsvorbild (Jahrgangsstufentest 6 Bayern: Koordinaten vertauscht, Symbolschreibweise D ∈ [EG],
# Zaun im Abstand um ein Becken, Leiter-Winkel, Quadrat mit Umfang/Fläche, Lage von Geraden a, b, c, d); eigene Zahlen.
from itertools import combinations  # noqa: E402
from _schwer_kl5 import A, L, Z, de, einzig, ergaenze, wahl  # noqa: E402


def _schwer():
    N = {}
    rob = (0, 0)
    for i in range(10):
        rob = (rob[0] + 1, rob[1]) if i % 2 == 0 else (rob[0], rob[1] + 2)
    N['koordinaten'] = [
        wahl(2, 'Welcher Punkt liegt auf der y-Achse?', ['(0 | −3)', '(−3 | 0)', '(3 | 3)', '(−3 | 3)'], lambda o: o.startswith('(0 |'),
             'Auf der y-Achse ist die erste Zahl (x-Koordinate) 0: (0 | −3).', 'Welche Koordinate ist auf der y-Achse immer 0?'),
        L(2, 'Wo liegt der Mittelpunkt M der Strecke [AB] mit A(−4 | 2) und B(6 | 2)?', 'M(□ | □)', 'Trage x- und y-Koordinate ein.', ['(-4 + 6) // 2', '2'],
          'Von −4 bis 6 sind es 10 Einheiten, die Hälfte ist 5: −4 + 5 = 1. Die Höhe bleibt 2: M(1 | 2).', 'Beide Punkte liegen auf derselben Höhe. Wo ist die Mitte zwischen −4 und 6?'),
        A(3, 'Jemand soll A(−1 | 3) eintragen. Er geht vom Ursprung 3 nach links und 1 nach oben. Was ist falsch?',
          'x und y sind vertauscht: erst 1 nach links, dann 3 nach oben.',
          ['Nichts, das ist richtig.', 'Er hätte 1 nach rechts gehen müssen.', 'Er hätte 3 nach unten gehen müssen.'],
          'Die erste Zahl (−1) sagt rechts/links, die zweite (3) sagt oben/unten. Richtig: 1 nach links, 3 nach oben.', 'Welche Zahl gehört zur Bewegung nach rechts/links?'),
        L(3, 'Ein Quadrat ABCD hat die Ecken A(1 | 1) und B(4 | 1). Die Ecken C und D liegen unterhalb von [AB]. Welche Koordinaten haben C und D?',
          'C(□ | □), D(□ | □)', 'Trage alle vier Koordinaten ein.', ['4', '1 - (4 - 1)', '1', '1 - (4 - 1)'],
          'Die Seite [AB] ist 3 lang. C liegt 3 unter B: C(4 | −2). D liegt 3 unter A: D(1 | −2).', 'Wie lang ist die Seite [AB]? Geh von B und von A gleich weit nach unten.'),
        Z(3, 'Wie viele Punkte mit ganzzahligen Koordinaten liegen auf der Strecke von (−3 | 2) bis (4 | 2)? Die Endpunkte zählen mit.', str(len(range(-3, 5))),
          'x läuft von −3 bis 4: −3, −2, −1, 0, 1, 2, 3, 4. Das sind 8 Punkte.', 'Zähle die x-Werte auf. Vergiss die 0 nicht.'),
        L(3, 'Ein Roboter startet im Ursprung. Er geht abwechselnd 1 Schritt nach rechts und 2 Schritte nach oben, beginnend mit rechts. Wo steht er nach 10 solchen Zügen?',
          'R(□ | □)', 'Trage x- und y-Koordinate ein.', [str(rob[0]), str(rob[1])],
          '10 Züge sind 5-mal „rechts“ und 5-mal „oben“: x = 5 · 1 = 5, y = 5 · 2 = 10. R(5 | 10).', 'Wie viele der 10 Züge gehen nach rechts, wie viele nach oben?'),
    ]
    N['strecken'] = [
        Z(2, 'Wie lang ist die Strecke [AB] mit A(−4 | −1) und B(−4 | 6) (in Einheiten)?', '6 - (-1)', 'Senkrechte Strecke: von −1 bis 6 sind es 1 + 6 = 7 Einheiten.', 'Die 0 liegt zwischen den y-Werten.'),
        Z(2, 'Eine Seite eines Quadrats geht von (−2 | −2) bis (3 | −2). Wie groß ist der Umfang des Quadrats (in Einheiten)?', '4 * (3 - (-2))',
          'Seitenlänge: von −2 bis 3 sind es 5. Umfang: 4 · 5 = 20.', 'Bestimme zuerst eine Seitenlänge.'),
        Z(3, 'Ein rechteckiges Beet ist 6 m lang und 2 m breit. Im Abstand von 2 m wird ringsum ein Zaun gezogen, parallel zu den Beetseiten. Wie lang ist der Zaun?',
          '2 * ((6 + 2 * 2) + (2 + 2 * 2))', 'Das Zaun-Rechteck ist auf jeder Seite 2 m größer: 10 m lang, 6 m breit. Umfang: 2 · (10 + 6) = 32 m.',
          'Mach eine Skizze. Wie lang und breit ist das Rechteck, das der Zaun bildet?', einheit='m'),
        L(3, 'A(−3 | 1). B liegt auf derselben waagrechten Linie wie A, 8 Einheiten von A entfernt und rechts von der y-Achse. Welche Koordinaten hat B?',
          'B(□ | □)', 'Trage x- und y-Koordinate ein.', ['-3 + 8', '1'],
          'Nach links (−11) wäre B links der y-Achse. Also nach rechts: −3 + 8 = 5. B(5 | 1).', 'Prüfe beide Richtungen: 8 nach rechts und 8 nach links.'),
        Z(3, 'Die Strecke von A(−5 | 3) bis B(7 | 3) wird in 4 gleich lange Teile geteilt. Welche x-Koordinate hat der erste Teilungspunkt nach A?', '-5 + (7 - (-5)) // 4',
          'Länge: 12. Ein Teil: 12 : 4 = 3. Erster Teilungspunkt: −5 + 3 = −2.', 'Wie lang ist die Strecke, wie lang ein Teil?'),
        L(3, 'Ein Rechteck ABCD mit A(−3 | −2) ist 6 Einheiten breit (nach rechts) und hat den Umfang 20. C liegt rechts oberhalb von A. Welche Koordinaten hat C?',
          'C(□ | □)', 'Trage x- und y-Koordinate ein.', ['-3 + 6', '-2 + (20 // 2 - 6)'],
          'Länge + Breite = 20 : 2 = 10, also ist die Höhe 10 − 6 = 4. C = (−3 + 6 | −2 + 4) = (3 | 2).', 'Umfang : 2 ergibt Breite + Höhe.'),
    ]
    a_d = ['a ∥ d', 'a ⊥ d', 'a und d schneiden sich schräg', 'Das kann man nicht sagen.']
    N['lagebeziehungen'] = [
        Z(2, 'g ist die waagrechte Gerade durch alle Punkte mit y = 4, h die waagrechte Gerade durch alle Punkte mit y = −3. Welchen Abstand haben g und h (in Einheiten)?',
          '4 - (-3)', 'Von −3 bis 4: 3 + 4 = 7 Einheiten.', 'Die 0 liegt zwischen den beiden Geraden.'),
        wahl(2, 'Wie viele Geraden durch einen Punkt P stehen senkrecht auf einer Geraden g?', ['genau eine', 'zwei', 'keine', 'unendlich viele'], lambda o: o == 'genau eine',
             'Durch P gibt es genau ein Lot auf g.', 'Denk an das Geodreieck: Wie oft kannst du es an g und P anlegen?'),
        wahl(3, 'Welche Schreibweise bedeutet: „Die Gerade g steht senkrecht auf der Geraden h“?', ['g ⊥ h', 'g ∥ h', 'g ∈ h', '[gh]'], lambda o: o == 'g ⊥ h',
             '⊥ heißt „senkrecht zu“, ∥ heißt „parallel zu“, ∈ heißt „liegt auf / ist Element von“.', 'Das Zeichen sieht selbst aus wie ein rechter Winkel.'),
        wahl(3, 'Für vier Geraden gilt: a ⊥ b, b ⊥ c und c ∥ d. Wie liegen a und d zueinander?', a_d, lambda o: o == 'a ∥ d',
             'a und c stehen beide senkrecht auf b, also a ∥ c. Weil c ∥ d, ist auch a ∥ d.', 'Mach eine Skizze: Zeichne b waagrecht.'),
        Z(3, 'Vier Geraden liegen in einer Ebene. Keine zwei sind parallel, und keine drei gehen durch denselben Punkt. Wie viele Schnittpunkte gibt es?', str(len(list(combinations(range(4), 2)))),
          'Jedes Paar schneidet sich genau einmal. Paare aus 4 Geraden: 3 + 2 + 1 = 6 Schnittpunkte.', 'Zähle alle Paare von Geraden.'),
        Z(3, 'Die Geraden g und h sind parallel. Ein Punkt P hat von g den Abstand 7 cm und von h den Abstand 3 cm. P liegt nicht zwischen g und h. Welchen Abstand haben g und h?',
          '7 - 3', 'P liegt außerhalb, h ist näher an P. Abstand g zu h: 7 cm − 3 cm = 4 cm.', 'Zeichne g, h und P untereinander.', einheit='cm'),
    ]
    punkte = {'(5 | 1)': (5, 1), '(4 | 4)': (4, 4), '(1 | 4)': (1, 4), '(−4 | 1)': (-4, 1)}
    N['kreis_lage'] = [
        wahl(2, 'Ein Kreis hat den Durchmesser 10 cm. Eine Gerade hat vom Mittelpunkt den Abstand 4 cm. Was ist die Gerade?',
             ['Sekante (2 Schnittpunkte)', 'Tangente (1 Berührpunkt)', 'Passante (kein gemeinsamer Punkt)'], lambda o: o.startswith('Sekante'),
             'Radius = 10 cm : 2 = 5 cm. Abstand 4 cm ist kleiner als 5 cm: Sekante.', 'Achtung: Gegeben ist der Durchmesser, nicht der Radius.'),
        wahl(2, 'Ein Kreis um M(1 | 1) hat den Radius 4. Welcher Punkt liegt auf dem Kreis?', list(punkte),
             lambda o: (punkte[o][0] - 1) ** 2 + (punkte[o][1] - 1) ** 2 == 16,
             '(5 | 1) liegt 4 nach rechts von M, also genau im Abstand 4. (1 | 4) ist nur 3 entfernt, (−4 | 1) 5, (4 | 4) liegt schräg und nicht im Abstand 4.',
             'Gehe von M aus 4 Einheiten waagrecht oder senkrecht.'),
        wahl(3, 'Zwei Funkmasten stehen 10 km voneinander entfernt. Jeder sendet 6 km weit in jede Richtung. Gibt es Orte mit Empfang von beiden Masten?',
             ['Ja, denn 6 km + 6 km sind mehr als 10 km.', 'Nein, denn 6 km sind weniger als 10 km.', 'Nur genau in der Mitte.', 'Das kann man nicht sagen.'],
             lambda o: o.startswith('Ja'), 'Die beiden Empfangskreise überlappen, weil die Radien zusammen (12 km) größer sind als der Abstand (10 km).',
             'Zeichne um jeden Mast einen Kreis. Überschneiden sie sich?'),
        Z(3, 'Ein Kreis berührt die x-Achse und die y-Achse je in einem Punkt. Sein Mittelpunkt M liegt rechts der y-Achse und hat die y-Koordinate 4. Welche x-Koordinate hat M?', '4',
          'Berührt der Kreis die x-Achse, ist der Radius 4 (Abstand von M zur x-Achse). Zur y-Achse ist der Abstand auch 4, also x = 4.', 'Wie groß ist der Radius, wenn der Kreis die x-Achse berührt?'),
        wahl(3, 'Wie viele gemeinsame Punkte können zwei verschiedene Kreise höchstens haben?', ['1', '2', '3', 'unendlich viele'], lambda o: o == '2',
             'Zwei verschiedene Kreise schneiden sich in höchstens 2 Punkten. Unendlich viele nur, wenn die Kreise gleich sind.', 'Probiere mit einer Skizze verschiedene Lagen aus.'),
        Z(3, 'Kreis k₁ hat den Mittelpunkt M₁(0 | 0) und den Radius 3. Kreis k₂ hat den Mittelpunkt M₂(8 | 0). Wie groß muss der Radius von k₂ sein, damit sich die Kreise von außen in genau einem Punkt berühren?',
          '8 - 3', 'Der Berührpunkt liegt auf der Verbindung bei (3 | 0). Von dort bis M₂ sind es 8 − 3 = 5.', 'Wo liegt der Berührpunkt auf der x-Achse?'),
    ]
    zahl_stumpf = sum(1 for w in (17, 90, 135, 180, 200, 359) if 90 < w < 180)
    N['winkelarten'] = [
        Z(2, 'Wie groß ist ein Viertel eines Vollwinkels?', '360 / 4', 'Vollwinkel: 360°. 360° : 4 = 90°.', 'Ein Vollwinkel ist eine ganze Drehung.', einheit='°'),
        wahl(2, 'Ein Winkel ist um 30° größer als ein rechter Winkel. Welche Winkelart ist er?', ['stumpf', 'spitz', 'gestreckt', 'überstumpf'], lambda o: o == 'stumpf',
             '90° + 30° = 120°. Zwischen 90° und 180°: stumpf.', 'Rechne zuerst die Größe aus.'),
        wahl(3, 'Eine Leiter lehnt an einer Wand. Außen zwischen Leiter und Boden misst man 108°. Sicher steht sie, wenn der Winkel innen zwischen Boden und Leiter 68° bis 75° beträgt. Steht sie sicher?',
             ['Ja, der Winkel innen ist 72°.', 'Nein, der Winkel innen ist 108°.', 'Nein, der Winkel innen ist 18°.', 'Ja, der Winkel innen ist 108°.'],
             lambda o: o == f'Ja, der Winkel innen ist {180 - 108}°.', 'Innen und außen ergeben zusammen einen gestreckten Winkel: 180° − 108° = 72°. 72° liegt zwischen 68° und 75°.',
             'Innen und außen liegen zusammen auf dem Boden – wie viel Grad ist das?'),
        wahl(3, 'Welche Winkelart überstreicht der Minutenzeiger in 40 Minuten?', ['überstumpf', 'stumpf', 'gestreckt', 'spitz'], lambda o: o == 'überstumpf',
             'In 60 Minuten 360°, also 6° pro Minute. 40 · 6° = 240°: zwischen 180° und 360°, überstumpf.', 'Wie viel Grad dreht sich der Minutenzeiger in einer Minute?'),
        Z(3, 'Wie viele der Winkel 17°, 90°, 135°, 180°, 200°, 359° sind stumpf?', str(zahl_stumpf),
          'Stumpf heißt größer als 90° und kleiner als 180°. Das trifft nur auf 135° zu.', 'Prüfe jeden Winkel. 90° und 180° sind nicht stumpf.'),
        Z(3, 'Ein Winkel ist dreimal so groß wie der Winkel, der ihn zum Vollwinkel ergänzt. Wie groß ist er?', '360 * 3 // 4',
          'Zusammen 360°, aufgeteilt im Verhältnis 3 : 1. Ein Teil: 360° : 4 = 90°. Der Winkel ist 3 · 90° = 270°.', 'Der Winkel hat 3 Teile, die Ergänzung 1 Teil.', einheit='°'),
    ]
    gitter = sum(1 for _ in combinations(range(3), 2)) ** 2
    aussagen = ['Jedes Quadrat ist eine Raute.', 'Jede Raute ist ein Rechteck.', 'Jedes Parallelogramm ist ein Rechteck.', 'Jedes Trapez ist ein Drachenviereck.']
    N['vierecke'] = [
        wahl(2, 'Welches Viereck hat genau ein Paar paralleler Seiten?', ['Trapez', 'Parallelogramm', 'Rechteck', 'Raute'], lambda o: o == 'Trapez',
             'Parallelogramm, Rechteck und Raute haben zwei Paare paralleler Seiten. Ein (allgemeines) Trapez hat genau eins.', 'Wie viele Paare paralleler Seiten hat ein Rechteck?'),
        Z(2, 'Ein Rechteck hat den Umfang 18 cm. Eine Seite ist 5 cm lang. Wie lang ist die andere Seite?', '18 / 2 - 5',
          'Zwei Seiten zusammen: 18 cm : 2 = 9 cm. Die andere Seite: 9 cm − 5 cm = 4 cm.', 'Eine lange und eine kurze Seite zusammen sind der halbe Umfang.', einheit='cm'),
        Z(3, 'Ein Quadrat hat den Umfang 28 cm. Welchen Flächeninhalt hat es?', '(28 // 4) ** 2', 'Seite: 28 cm : 4 = 7 cm. Fläche: 7 cm · 7 cm = 49 cm².',
          'Bestimme zuerst die Seitenlänge.', einheit='cm²'),
        Z(3, 'Ein Rechteck ist 3 cm breit. Umfang (in cm) und Flächeninhalt (in cm²) haben dieselbe Maßzahl. Wie lang ist das Rechteck?',
          str(einzig([l for l in range(1, 100) if 2 * (l + 3) == 3 * l])), 'Probieren: Länge 6 cm ergibt Umfang 2 · (6 + 3) = 18 und Fläche 6 · 3 = 18.',
          'Probiere Längen aus und vergleiche Umfang und Fläche.', einheit='cm'),
        Z(3, 'Ein Gitter besteht aus 2 · 2 gleich großen Kästchen. Wie viele Rechtecke (Quadrate mitgezählt) kann man entlang der Linien finden?', str(gitter),
          '4 kleine Quadrate, 2 waagrechte und 2 senkrechte Rechtecke aus je 2 Kästchen, 1 großes Quadrat: 4 + 4 + 1 = 9.', 'Zähle geordnet: erst 1 Kästchen, dann 2, dann 4.'),
        wahl(3, 'Welche Aussage stimmt?', aussagen, lambda o: o == 'Jedes Quadrat ist eine Raute.',
             'Ein Quadrat hat vier gleich lange Seiten, also ist es eine Raute. Eine Raute ohne rechte Winkel ist kein Rechteck.',
             'Prüfe jede Aussage: Hat jedes Viereck der ersten Art alle Eigenschaften der zweiten Art?'),
    ]
    N['verstehen'] = [
        wahl(2, 'Stimmt die Aussage? „Eine Strecke hat zwei Endpunkte.“', ['Ja: Eine Strecke hat einen Anfangs- und einen Endpunkt.', 'Nein: Eine Strecke hat keinen Endpunkt.', 'Nein: nur einen.'],
             lambda o: o.startswith('Ja'), 'Eine Strecke [AB] beginnt bei A und endet bei B.', 'Vergleiche Strecke, Halbgerade und Gerade.'),
        wahl(2, 'Stimmt die Aussage? „Zwei Strecken, die sich nicht schneiden, sind parallel.“',
             ['Nein: Kurze Strecken können sich verfehlen, obwohl sie schräg zueinander liegen.', 'Ja: Wer sich nicht schneidet, ist parallel.', 'Ja, aber nur bei gleich langen Strecken.'],
             lambda o: o.startswith('Nein'), 'Verlängert man die Strecken, können sie sich schneiden. Parallel sind sie nur, wenn ihre Geraden sich nie schneiden.',
             'Zeichne zwei kurze schräge Strecken, die sich nicht treffen.'),
        wahl(3, 'Welche Aussage über ein Rechteck ist falsch?', ['Die Diagonalen sind gleich lang.', 'Gegenüberliegende Seiten sind parallel.', 'Alle Seiten sind gleich lang.', 'Alle Winkel sind 90°.'],
             lambda o: o == 'Alle Seiten sind gleich lang.', 'Gleich lange Seiten hat nur ein Quadrat. Die anderen drei Aussagen gelten für jedes Rechteck.',
             'Denk an ein Rechteck mit 6 cm und 3 cm.'),
        wahl(3, 'Der Punkt D liegt auf der Strecke [EG]. Welche Schreibweise passt?', ['D ∈ [EG]', 'D ⊥ [EG]', 'D ∥ [EG]', '[ED] = G'], lambda o: o == 'D ∈ [EG]',
             '„∈“ heißt „liegt auf“ bzw. „ist Element von“. ⊥ und ∥ beschreiben die Lage von Linien zueinander.', 'Welches Zeichen sagt, dass ein Punkt zu einer Menge von Punkten gehört?'),
        wahl(3, 'Jemand behauptet: „Ein Viereck mit zwei rechten Winkeln ist immer ein Rechteck.“ Welches Gegenbeispiel widerlegt das?',
             ['Ein Trapez mit zwei rechten Winkeln an derselben Seite', 'Ein Quadrat', 'Ein Rechteck mit 6 cm und 3 cm', 'Ein Kreis'], lambda o: o.startswith('Ein Trapez'),
             'Ein rechtwinkliges Trapez hat zwei rechte Winkel, aber die anderen beiden sind nicht 90°. Es ist kein Rechteck.', 'Ein Gegenbeispiel erfüllt die Bedingung, ist aber kein Rechteck.'),
        wahl(3, 'Stimmt die Aussage? „Durch drei Punkte kann man immer eine Gerade zeichnen.“',
             ['Nein, nur wenn die drei Punkte auf einer Linie liegen.', 'Ja, durch jeden Punkt geht eine Gerade.', 'Ja, sogar drei verschiedene.', 'Nein, durch drei Punkte geht nie eine Gerade.'],
             lambda o: o.startswith('Nein, nur'), 'Durch zwei Punkte geht genau eine Gerade. Der dritte Punkt liegt nur zufällig darauf.', 'Zeichne drei Punkte als Dreieck.'),
    ]
    return N


ergaenze(DATEI, _schwer(), 1042)

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('geometrie.grundbegriffe', 13_5_6)
# a) reine Begriffsabfrage wie Stufe 1 → Stufe 2
BF.stufe('verstehen', 'Stimmt die Aussage? „Ein Winkel von 220° ist stumpf.“', 2)
BF.stufe('verstehen', 'Stimmt die Aussage? „Eine Tangente schneidet den Kreis in zwei Punkten.“', 2)
# c) Beinahe-Dublette (zweimal „g ⊥ h“ mit gleichem Aufbau) → einmal parallel
BF.ersetze('lagebeziehungen', 'g geht durch A(−6 | −3) und B(−6 | 0), h geht durch C(4 | −3) und D(8 | −3). Wie liegen g und h zueinander?', BF.A(
    'g geht durch A(−6 | −3) und B(−6 | 0), h geht durch C(4 | −3) und D(4 | 5). Wie liegen g und h zueinander?', 'g ∥ h',
    ['g und h sind gleich', 'g ⊥ h'],
    'g und h sind beide senkrecht (bei g ist x immer −6, bei h immer 4). Sie haben dieselbe Richtung und keinen gemeinsamen Punkt: g ∥ h.',
    'Gleiche x-Koordinaten: senkrechte Linie. Gleiche y-Koordinaten: waagrechte Linie.'))
# d) Lage zweier Kreise „Kreis im Kreis“ wird in der Lernkarte nicht erklärt → Aufgabe zu Kreis und Gerade
BF.ersetze('kreis_lage', 'Zwei Kreise haben die Radien 7 cm und 4 cm. Ihre Mittelpunkte sind 3 cm voneinander entfernt. Wie viele gemeinsame Punkte haben sie?', BF.Z(
    'Ein Kreis um M(2 | 1) hat den Radius 4. Die waagrechte Gerade g geht durch alle Punkte mit y = −3. Wie viele gemeinsame Punkte haben Kreis und g?', 1, '1',
    'Abstand von M zu g: 1 − (−3) = 4. Das ist genau der Radius. g berührt den Kreis in einem Punkt (2 | −3): g ist eine Tangente.',
    'Berechne den Abstand des Mittelpunkts von der Geraden und vergleiche ihn mit dem Radius.'))
BF.fuer_sebastian('geometrie.grundbegriffe/kreis_lage: Die Lernkarte erklärt nur Kreis und Gerade; die übrigen Stufe-3-Aufgaben zu zwei Kreisen (von außen berühren, getrennt) setzen r₁ + r₂ voraus. Erklärung ergänzen oder Aufgaben belassen? Karten-Text nicht geändert.')

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl5, siehe _durchsicht_kl5.py) ----
from _durchsicht_kl5 import Durchsicht, durchsicht_anwenden  # noqa: E402

DS = Durchsicht('geometrie.grundbegriffe', 19_5_3)
_s3 = lambda x: x['s'] == 3
# a) Stufe 3 ohne neuen Gedanken (Ablesen, Einkleidung des Grundfalls, viermal dieselbe Vorlage) → Stufe 2
for _lz, _t in [
        ('koordinaten', 'Ein Rechteck ABCD hat die Ecken A(−5 | −4), B(−3 | −4) und C(−3 | 4). Seine Seiten sind parallel zu den Achsen. Welche Koordinaten hat D?'),
        ('koordinaten', 'Ein Rechteck ABCD hat die Ecken A(3 | −1), B(5 | −1) und C(5 | 2). Seine Seiten sind parallel zu den Achsen. Welche Koordinaten hat D?'),
        ('lagebeziehungen', 'g geht durch A(1 | −3) und B(1 | 1), h geht durch C(−3 | −3) und D(1 | −3). Wie liegen g und h zueinander?'),
        ('lagebeziehungen', 'g geht durch A(−6 | −3) und B(−6 | 0), h geht durch C(4 | −3) und D(4 | 5). Wie liegen g und h zueinander?'),
        ('lagebeziehungen', 'g geht durch A(−5 | −4) und B(−5 | 3), h geht durch C(−2 | −4) und D(2 | −4). Wie liegen g und h zueinander?'),
        ('kreis_lage', 'Ein Funkmast reicht 4 km weit in jede Richtung. Ein Dorf ist 7 km vom Mast entfernt. Hat das Dorf Empfang?'),
        ('kreis_lage', 'Ein Funkmast reicht 10 km weit in jede Richtung. Ein Dorf ist 9 km vom Mast entfernt. Hat das Dorf Empfang?'),
        ('winkelarten', 'Zwei Winkel 22° und 152° liegen direkt nebeneinander (gemeinsamer Schenkel). Welche Art hat der zusammengesetzte Winkel?'),
        ('winkelarten', 'Zwei Winkel 124° und 145° liegen direkt nebeneinander (gemeinsamer Schenkel). Welche Art hat der zusammengesetzte Winkel?'),
        ('winkelarten', 'Zwei Winkel 145° und 134° liegen direkt nebeneinander (gemeinsamer Schenkel). Welche Art hat der zusammengesetzte Winkel?'),
        ('winkelarten', 'Zwei Winkel 82° und 98° liegen direkt nebeneinander (gemeinsamer Schenkel). Welche Art hat der zusammengesetzte Winkel?')]:
    DS.stufe(_lz, _t, 2, enthaelt=_s3)
# c) Aufgaben mit Flächeninhalt (kommt erst im Flug messen.flaechen, Reihenfolge 13) → Aufgaben zu Vierecken
DS.ersetze('vierecke', 'Ein Quadrat hat den Umfang 28 cm. Welchen Flächeninhalt hat es?', DS.L(
    'ABCD ist ein Parallelogramm mit A(1 | 1), B(5 | 1) und C(6 | 4). Welche Koordinaten hat D?', 'D(□ | □)', [2, 4], ['6 - (5 - 1)', '4 - (1 - 1)'],
    'Im Parallelogramm ist [AD] parallel und gleich lang wie [BC]. Von B nach C geht es 1 nach rechts und 3 nach oben. Von A aus genauso: D(2 | 4).',
    'Gegenüberliegende Seiten sind parallel und gleich lang. Wie kommt man von B nach C?',
    grafik={'typ': 'koordinaten', 'x': [-1, 7], 'y': [-1, 6], 'punkte': [{'x': 1, 'y': 1, 'name': 'A'}, {'x': 5, 'y': 1, 'name': 'B'}, {'x': 6, 'y': 4, 'name': 'C'}]}))
DS.ersetze('vierecke', 'Ein Rechteck ist 3 cm breit. Umfang (in cm) und Flächeninhalt (in cm²) haben dieselbe Maßzahl. Wie lang ist das Rechteck?', DS.A(
    'Ein Viereck hat vier gleich lange Seiten, aber keinen rechten Winkel. Welcher Name passt am genauesten?', 'Raute',
    ['Quadrat', 'Parallelogramm', 'Rechteck'],
    'Vier gleich lange Seiten: Quadrat oder Raute. Ohne rechten Winkel ist es kein Quadrat, also eine Raute. „Parallelogramm“ stimmt auch, ist aber weniger genau.',
    'Welche Vierecke haben vier gleich lange Seiten? Welches davon braucht rechte Winkel?'))
durchsicht_anwenden(DATEI, DS)
# ---- DURCHSICHT ENDE ----

if __name__ == '__main__':
    schreibe(DATEI)
