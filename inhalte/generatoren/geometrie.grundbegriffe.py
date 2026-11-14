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

MERKE = ['P(x | y): erst x (rechts/links), dann y (oben/unten).', 'Waagrechte Strecke: Unterschied der x-Koordinaten.',
         'g ∥ h: parallel. g ⊥ h: senkrecht. Abstand = Länge des Lots.', 'd < r Sekante, d = r Tangente, d > r Passante.',
         'spitz < 90° = recht < stumpf < 180° = gestreckt < überstumpf < 360°.']


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
def g_koord(st):
    if st == 1:
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
        r = lage[(1 if x > 0 else -1, 1 if y > 0 else -1)]
        return {**wahl(R, r, [v for v in lage.values() if v != r]), 'f': {'text': f'Wo liegt der Punkt P{p(x, y)}, vom Ursprung aus gesehen?'},
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
                    'w': f'Gleiche y-Koordinate, also waagrecht: {x2} − {x1} = {x2 - x1} Einheiten.', 'h': 'Vergleiche die x-Koordinaten.'}
        return {'y': 'zahl', 'f': {'text': f'Wie lang ist die Strecke [CD] mit C{p(y, x1)} und D{p(y, x2)} (in Einheiten)?'}, 'o': {'wert': x2 - x1}, 'c': f'{x2} - {x1}',
                'w': f'Gleiche x-Koordinate, also senkrecht: {x2} − {x1} = {x2 - x1} Einheiten.', 'h': 'Vergleiche die y-Koordinaten.'}
    if st == 2:
        a, b = sorted(R.sample(range(-9, 10), 2))
        if a >= 0: a = -R.randint(1, 6)
        c = R.randint(-6, 6)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Wie lang ist [AB] mit A{p(a, c)} und B{p(b, c)} (in Einheiten)?', 'grafik': ks([(a, c, 'A'), (b, c, 'B')], [(a, c, b, c)])}, 'o': {'wert': b - a}, 'c': f'({b}) - ({a})',
                    'w': f'Waagrecht: {zt(b)} − {kl(a)} = {zt(b)} + {zt(-a)} = {b - a} Einheiten.', 'h': 'Liegt die 0 dazwischen? Dann zähle die beiden Teilstücke zusammen.'}
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Welchen Abstand hat der Punkt P{p(c, a)} von der x-Achse (in Einheiten)?'}, 'o': {'wert': abs(a)}, 'c': f'abs({a})',
                    'w': f'Der Abstand zur x-Achse ist der Betrag der y-Koordinate: |{zt(a)}| = {abs(a)}.', 'h': 'Wie weit ist P von der waagrechten Achse entfernt? Schau auf y.'}
        return {'y': 'zahl', 'f': {'text': f'Wie lang ist [CD] mit C{p(c, a)} und D{p(c, b)} (in Einheiten)?'}, 'o': {'wert': b - a}, 'c': f'({b}) - ({a})',
                'w': f'Senkrecht: {zt(b)} − {kl(a)} = {b - a} Einheiten.', 'h': 'Gleiche x-Koordinate: Unterschied der y-Koordinaten.'}
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
            'o': {'wert': weg}, 'c': f'{lang[0][0]} + {lang[1][0]} + {lang[2][0]}', 'w': f'{lang[0][0]} + {lang[1][0]} + {lang[2][0]} = {weg} Einheiten. Sie endet bei {p(x, y)}.',
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


def g_lage(st):
    if st == 1:
        t, r, f = R.choice(BEGRIFFE)
        return {**wahl(R, r, f), 'f': {'text': t}, 'w': f'Richtig ist: {r}. So steht es in der Erklärung.', 'h': 'Denke an die Fachbegriffe aus der Erklärung.'}
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
        n = 2 if abs(r1 - r2) < e < r1 + r2 else 1 if e == r1 + r2 else 0
        return {'y': 'zahl', 'f': {'text': f'Zwei Kreise haben die Radien {r1} cm und {r2} cm. Ihre Mittelpunkte sind {e} cm voneinander entfernt. Wie viele gemeinsame Punkte haben sie?'},
                'o': {'wert': n}, 'c': f'{n}', 'w': f'r₁ + r₂ = {r1 + r2} cm. ' + ('Abstand gleich der Summe: Sie berühren sich (1 Punkt).' if n == 1 else 'Abstand größer als die Summe: kein gemeinsamer Punkt.' if n == 0 else 'Abstand kleiner als die Summe (und größer als der Unterschied): 2 Schnittpunkte.'),
                'h': 'Vergleiche den Abstand der Mittelpunkte mit r₁ + r₂.'}
    if art == 1:
        r = R.choice([3, 4, 5, 8, 10, 12, 15])
        d = R.choice([r - 2, r, r + 3, r - 1])
        ja = d <= r
        rr = 'Ja, der Ort liegt innerhalb der Reichweite.' if ja else 'Nein, der Ort liegt außerhalb der Reichweite.'
        return {**wahl(R, rr, ['Nein, der Ort liegt außerhalb der Reichweite.' if ja else 'Ja, der Ort liegt innerhalb der Reichweite.', 'Das hängt von der Richtung ab.'], 3),
                'f': {'text': f'Ein Funkmast reicht {r} km weit in jede Richtung. Ein Dorf ist {d} km vom Mast entfernt. Hat das Dorf Empfang?'},
                'w': f'Der Empfangsbereich ist ein Kreis mit Radius {r} km. {d} km {"≤" if ja else ">"} {r} km.', 'h': 'Alle Punkte bis zum Abstand r liegen im Kreis – in jede Richtung gleich weit.'}
    mx, my, r = R.randint(-3, 3), R.randint(-3, 3), R.randint(2, 6)
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
        a = R.randint(10, 170)
        if a == 90: a = 95
        return {'y': 'zahl', 'f': {'text': f'Zwei Schenkel bilden einen Winkel von {a}°. Wie groß ist der überstumpfe Winkel zwischen denselben Schenkeln (auf der anderen Seite)?'},
                'o': {'wert': 360 - a, 'einheit': '°'}, 'c': f'360 - {a}', 'w': f'Beide Winkel zusammen ergeben den Vollwinkel: 360° − {a}° = {360 - a}°.', 'h': 'Beide Winkel zusammen ergeben 360°.'} if R.random() < .5 else \
            {**wahl(R, art(a), [x for x in ARTEN if x != art(a)]), 'f': {'text': f'Ein Winkel ist {"halb" if a % 2 == 0 else "um 10° kleiner als"} {"so groß wie " + str(2 * a) + "°" if a % 2 == 0 else str(a + 10) + "°"}. Welche Winkelart ist er?'},
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
    if st == 2:
        x1, y1 = R.randint(-6, 2), R.randint(-6, 2)
        a, h, s = R.randint(3, 6), R.randint(2, 5), R.randint(1, 3)
        A, B, C = (x1, y1), (x1 + a, y1), (x1 + a + s, y1 + h)
        D = (x1 + s, y1 + h)
        return mit(punkt('D', D[0], D[1], f'ABCD ist ein Parallelogramm mit A{p(*A)}, B{p(*B)} und C{p(*C)}. Welche Koordinaten hat D?',
                     f'Von B nach C geht es {s} nach rechts und {h} nach oben. Dasselbe von A aus: D{p(*D)}.', 'Die Seite [AD] ist parallel und gleich lang wie [BC]: gleiche Verschiebung.',
                     f'({x1}) + {s}', f'({y1}) + {h}'), ks([(A[0], A[1], 'A'), (B[0], B[1], 'B'), (C[0], C[1], 'C')], [(A[0], A[1], B[0], B[1]), (B[0], B[1], C[0], C[1])]))
    aussagen = [('Jedes Quadrat ist ein Rechteck.', True), ('Jedes Rechteck ist ein Quadrat.', False), ('Jede Raute ist ein Parallelogramm.', True),
                ('Jedes Parallelogramm ist ein Trapez.', True), ('Jedes Trapez ist ein Parallelogramm.', False), ('Jedes Quadrat ist eine Raute.', True),
                ('Jede Raute ist ein Quadrat.', False), ('Jedes Rechteck ist ein Parallelogramm.', True), ('Jede Raute ist ein Drachenviereck.', True),
                ('Jedes Drachenviereck ist eine Raute.', False)]
    s, stimmt = R.choice(aussagen)
    r = 'Ja, das stimmt immer.' if stimmt else 'Nein, es gibt Gegenbeispiele.'
    return {**wahl(R, r, ['Nein, es gibt Gegenbeispiele.' if stimmt else 'Ja, das stimmt immer.', 'Nur manchmal, das hängt von der Größe ab.'], 3), 'f': {'text': f'Stimmt die Aussage? „{s}“'},
            'w': ('Ja: Das erste Viereck hat alle Eigenschaften des zweiten.' if stimmt else 'Nein: Das zweite Viereck verlangt Eigenschaften, die das erste nicht immer hat.') + ' Vergleiche die Eigenschaften aus der Erklärung.',
            'h': 'Hat das erste Viereck immer alle Eigenschaften des zweiten?'}


# ---------- 7 Verstehen ----------
def g_vers(st):
    x, y = R.randint(1, 8), R.randint(1, 8)
    if x == y: y += 1
    r = R.randint(2, 6)
    if st == 1:
        aussagen = [(f'Der Punkt ({x} | {y}) ist derselbe wie ({y} | {x}).', False, f'Nein, zuerst steht x: ({x} | {y}) liegt {x} rechts und {y} oben, ({y} | {x}) umgekehrt.'),
                    ('Eine Strecke kann man messen, eine Gerade nicht.', True, 'Ja, eine Gerade ist unendlich lang.'),
                    (f'Ein Winkel von {90 + x}° ist spitz.', False, f'Nein, {90 + x}° ist größer als 90°, also stumpf.'),
                    (f'Ein Kreis mit Radius {r} cm hat den Durchmesser {2 * r} cm.', True, f'Ja, der Durchmesser ist doppelt so lang: 2 · {r} = {2 * r}.')]
    elif st == 2:
        aussagen = [(f'Der Punkt (−{x} | {y}) liegt links von der y-Achse.', True, 'Ja, eine negative x-Koordinate heißt links.'),
                    (f'Die Strecke von (−{x} | 0) bis ({y} | 0) ist {abs(y - x)} lang.', False, f'Nein, sie ist {x} + {y} = {x + y} lang.'),
                    (f'Eine Gerade mit Abstand {r} cm vom Mittelpunkt eines Kreises mit r = {r} cm ist eine Sekante.', False, 'Nein, d = r: Das ist eine Tangente.'),
                    ('Zwei Geraden, die beide senkrecht zu einer dritten sind, sind parallel zueinander.', True, 'Ja, beide stehen im rechten Winkel auf derselben Geraden.')]
    else:
        aussagen = [('Zwei Kreise können genau drei gemeinsame Punkte haben.', False, 'Nein, möglich sind nur 0, 1 oder 2 gemeinsame Punkte (oder alle, wenn sie gleich sind).'),
                    ('Jedes Viereck mit vier gleich langen Seiten ist ein Quadrat.', False, 'Nein, Gegenbeispiel: eine Raute ohne rechte Winkel.'),
                    ('Der Abstand eines Punktes zu einer Geraden wird senkrecht gemessen.', True, 'Ja, entlang des Lots – das ist die kürzeste Verbindung.'),
                    (f'Ein Winkel von {180 + x * 10}° ist stumpf.', False, f'Nein, {180 + x * 10}° liegt zwischen 180° und 360°: überstumpf.'),
                    ('Eine Tangente schneidet den Kreis in zwei Punkten.', False, 'Nein, eine Tangente berührt den Kreis in genau einem Punkt.')]
    s, stimmt, grund = R.choice(aussagen)
    gegen = 'Ja, das stimmt.' if not stimmt else 'Nein, das ist falsch.'
    return {**wahl(R, grund, [gegen, 'Das kann man nicht entscheiden.'], 3), 'f': {'text': f'Stimmt die Aussage? „{s}“'}, 'w': grund, 'h': 'Mach eine Skizze oder suche ein Gegenbeispiel.'}


GEN = {'koordinaten': g_koord, 'strecken': g_strecke, 'lagebeziehungen': g_lage, 'kreis_lage': g_kreis, 'winkelarten': g_wart, 'vierecke': g_viereck, 'verstehen': g_vers}

DATEI = datei(E, 'Punkte, Strecken, Geraden und Kreise im Koordinatensystem beschreiben, Lagebeziehungen erkennen, Winkelarten bis 360° und besondere Vierecke unterscheiden.', MERKE,
              [('Koordinatensystem', ['koordinaten', 'strecken']),
               ('Lagebeziehungen', ['lagebeziehungen', 'kreis_lage']),
               ('Winkel und Vierecke', ['winkelarten', 'vierecke', 'verstehen'])],
              ETAPPEN, GEN,
              offen=['Zeichnungen (neu ab 14.11.) eingebaut: Koordinatensystem in koordinaten, strecken, lagebeziehungen, vierecke; Figuren für Kreis/Gerade, Winkel und Vierecke. Überstumpfe Winkel werden nicht gezeichnet (unklar, auf welcher Seite die App den Bogen zeichnet).',
                     'Lehrplan „Winkel bis 360° messen und zeichnen“: Messen mit dem Geodreieck und Zeichnen durch das Kind geht in der App nicht; enthalten sind Winkelarten und Rechnen mit Winkelgrößen.',
                     'Dreiecksarten aus „umfang“ weggelassen: LehrplanPLUS Kl. 5 nennt nur die Vierecke Quadrat, Rechteck, Parallelogramm, Raute, Drachenviereck und Trapez.'])

if __name__ == '__main__':
    schreibe(DATEI)
