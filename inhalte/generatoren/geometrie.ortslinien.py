#!/usr/bin/env python3
"""Thema geometrie.ortslinien – Punkte mit Abstandsbedingungen (Klasse 5): Kreislinie und Kreisfläche, Parallelenpaar und Streifen,
Bedingungen verknüpfen. Mittelsenkrechte und Winkelhalbierende sind Stoff der Jahrgangsstufe 7 und fehlen bewusst."""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl5_rest import *  # noqa: E402,F403

R = random.Random(73)
E = eintrag_laden('geometrie.ortslinien')


def p(x, y): return f'({zt(x)} | {zt(y)})'


def fig_kreis(mx, my, r, extra=None, gerade=None, r2=None):
    pk = {'M': [mx, my]}
    kr = [{'m': 'M', 'r': r}]
    lin = []
    if extra:
        for n, (x, y) in extra.items(): pk[n] = [x, y]
    if gerade is not None:
        pk['_G1'], pk['_G2'] = [mx - r - 3, gerade], [mx + r + 3, gerade]
        lin.append(['_G1', '_G2', 'g'])
    if r2:
        pk['N'] = list(r2[0])
        kr.append({'m': 'N', 'r': r2[1]})
    g = {'typ': 'figur', 'punkte': pk, 'kreise': kr}
    if lin: g['linien'] = lin
    return g


ETAPPEN = [
    {'lernziel': 'kreislinie', 'titel': 'Punkte mit festem Abstand zu M',
     'regel': 'Alle Punkte, die von einem Punkt M den ⟦Abstand r⟧ haben, liegen auf der ⟦Kreislinie⟧ um M mit Radius r. Punkte mit ⟦weniger als r⟧ Abstand liegen ⟦innerhalb⟧, Punkte mit mehr als r ⟦außerhalb⟧. „Höchstens r“ bedeutet: Kreisfläche mit Rand.',
     'schritte': ['Kreis um M(0 | 0) mit r = 3. Prüfe P(2 | 0): P ist 2 von M entfernt.', '2 < 3, also liegt P ⟦innerhalb⟧ des Kreises.'],
     'bild': {'typ': 'figur', 'punkte': {'M': [0, 0], 'P': [2, 0], '_R': [0, 3]}, 'kreise': [{'m': 'M', 'r': 3}], 'linien': [['M', '_R', 'r = 3']]},
     'fehler': 'Einen Punkt mit Abstand 3 zu M als „innerhalb“ zu bezeichnen ist falsch, wenn r = 3 ist: Er liegt genau ⟦auf⟧ der Kreislinie.'},
    {'lernziel': 'parallelen', 'titel': 'Punkte mit festem Abstand zu g',
     'regel': 'Alle Punkte, die von einer Geraden g den ⟦Abstand d⟧ haben, liegen auf ⟦zwei Parallelen⟧ zu g – eine auf jeder Seite, jeweils im Abstand d. Punkte mit ⟦höchstens d⟧ Abstand bilden einen ⟦Streifen⟧ zwischen diesen Parallelen.',
     'schritte': ['g ist die waagrechte Gerade mit y = 1. Gesucht: alle Punkte mit Abstand 2 von g.', 'Sie liegen auf den Parallelen ⟦y = −1⟧ und ⟦y = 3⟧.'],
     'bild': {'typ': 'koordinaten', 'x': [-4, 4], 'y': [-2, 4], 'waagrecht': [1, -1, 3], 'punkte': [{'x': 0, 'y': 3, 'name': 'P'}], 'strecken': [[0, 1, 0, 3, 'gestrichelt']]},
     'fehler': 'Nur eine Parallele einzuzeichnen ist ein häufiger Fehler: Es gibt ⟦auf beiden Seiten⟧ von g Punkte mit Abstand d.'},
    {'lernziel': 'zwei_kreise', 'titel': 'Abstand zu zwei Punkten',
     'regel': 'Gesucht sind Punkte mit Abstand r₁ von A ⟦und⟧ Abstand r₂ von B. Sie liegen auf ⟦beiden⟧ Kreislinien, also in ihren ⟦Schnittpunkten⟧. Ist [AB] länger als r₁ + r₂, gibt es keinen; ist [AB] = r₁ + r₂, genau einen; sonst (meist) zwei.',
     'schritte': ['A und B sind 8 km voneinander entfernt. Gesucht: Orte 5 km von A und 4 km von B entfernt.', '5 + 4 = 9 > 8: Die Kreise schneiden sich, es gibt ⟦zwei⟧ solche Orte.'],
     'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [8, 0]}, 'kreise': [{'m': 'A', 'r': 5}, {'m': 'B', 'r': 4}], 'linien': [['A', 'B', '8 km', 'gestrichelt']]},
     'fehler': 'Nur einen Schnittpunkt anzugeben ist meistens falsch: Zwei Kreise schneiden sich ⟦oberhalb und unterhalb⟧ der Verbindungslinie, also in ⟦zwei⟧ Punkten.'},
    {'lernziel': 'verknuepfen', 'titel': 'Kreis und Parallelen verknüpfen',
     'regel': 'Bei zwei Bedingungen („und“) suchst du die Punkte, die auf ⟦beiden⟧ Ortslinien liegen. Abstand r von M ⟦und⟧ Abstand d von g: Schneide den Kreis um M mit den ⟦zwei Parallelen⟧ zu g. Jede Parallele schneidet den Kreis in 2, 1 oder 0 Punkten.',
     'schritte': ['M hat von g den Abstand 5. Gesucht: Punkte mit Abstand 3 von M und Abstand 2 von g. Die Parallelen zu g haben von M den Abstand 5 − 2 = 3 und 5 + 2 = 7.', 'Abstand 3 = r: Tangente, 1 Punkt. Abstand 7 > r: kein Punkt. Es gibt genau ⟦einen⟧ Punkt.'],
     'fehler': 'Nur die Parallele auf der Seite von M zu betrachten kann zu wenig Lösungen ergeben, wenn der Kreis über g hinausreicht. Prüfe ⟦beide⟧ Parallelen.'},
    {'lernziel': 'sachsituationen', 'titel': 'Abstände im Alltag',
     'regel': 'Viele Alltagsfragen sind Abstandsbedingungen: ⟦Reichweite⟧ eines Sprengers oder Funkmasts (Kreisfläche), ⟦Leine⟧ eines Hundes (Kreisfläche), ⟦Sicherheitsabstand⟧ zu einer Straße (Streifen). Übersetze die Bedingung in Kreis oder Parallelen.',
     'schritte': ['Ein Rasensprenger erreicht alles bis 4 m. Ein Beet liegt 3 m vom Sprenger entfernt.', '3 m ≤ 4 m: Das Beet liegt in der Kreisfläche, es wird ⟦gegossen⟧.'],
     'fehler': '„Höchstens 4 m“ als „genau 4 m“ zu lesen ist falsch: Gemeint ist die ganze ⟦Kreisfläche⟧, nicht nur die Kreislinie.'},
    {'lernziel': 'verstehen', 'titel': 'Ortslinien verstehen',
     'regel': 'Prüfe Aussagen über Punktmengen mit einer ⟦Skizze⟧: Kreis um M für „Abstand zu M“, Parallelenpaar für „Abstand zu g“. Achte auf ⟦genau⟧, ⟦höchstens⟧ und ⟦mindestens⟧.',
     'schritte': ['Aussage: „Es gibt genau einen Punkt mit Abstand 2 von g.“ Skizze: zwei Parallelen im Abstand 2.', 'Auf jeder Parallelen liegen unendlich viele Punkte. Die Aussage ist ⟦falsch⟧.'],
     'fehler': 'Ortslinien bestehen meist aus ⟦unendlich vielen⟧ Punkten. Erst durch eine zweite Bedingung bleiben oft nur einzelne Punkte übrig.'},
]

PRUEFUNG = pruefung_erklaerungen(ETAPPEN, 'geometrie.ortslinien')   # verknuepfen: Bild Kreis mit Parallelenpaar

MERKE = ['Abstand r zu M: Kreislinie. Höchstens r: Kreisfläche.', 'Abstand d zu g: zwei Parallelen. Höchstens d: Streifen.',
         'Zwei Bedingungen mit „und“: Schnittpunkte der Ortslinien.', 'Kreise um A und B: [AB] > r₁ + r₂ keiner, = genau einer, sonst meist zwei.']

LAGEN = ['innerhalb des Kreises', 'auf der Kreislinie', 'außerhalb des Kreises']


ZAEHL = {'lage': 0, 'luecke': 0}


def lage(d, r): return LAGEN[0] if d < r else LAGEN[1] if d == r else LAGEN[2]


# ---------- 1 Kreislinie ----------
def g_kreis(st):
    if st == 1:
        r = R.randint(2, 9)
        d = [R.randint(1, r - 1), r, r + R.randint(1, 4)][ZAEHL['lage'] % 3]; ZAEHL['lage'] += 1     # je ein Drittel innen/auf/außen (Prüfung)
        l = lage(d, r)
        return {**wahl(R, l, [x for x in LAGEN if x != l]), 'f': {'text': f'Ein Kreis um M hat den Radius {r} cm. Der Punkt P ist {d} cm von M entfernt. Wo liegt P?'},
                'w': f'{d} cm {"<" if d < r else "=" if d == r else ">"} {r} cm: P liegt {l}.', 'h': 'Vergleiche den Abstand zu M mit dem Radius.'}
    if st == 2:
        mx, my, r = R.randint(-3, 3), R.randint(-3, 3), R.randint(2, 5)
        k = R.choice([-1, 1]) * ([R.randint(1, r - 1), r, R.randint(r + 1, r + 2)][ZAEHL['lage'] % 3]); ZAEHL['lage'] += 1
        senk = R.random() < .5
        px, py = (mx, my + k) if senk else (mx + k, my)
        l = lage(abs(k), r)
        return {**wahl(R, l, [x for x in LAGEN if x != l]), 'f': {'text': f'Kreis um M{p(mx, my)} mit r = {r}. Wo liegt der Punkt P{p(px, py)}?', 'grafik': fig_kreis(mx, my, r, {'P': (px, py)})},
                'w': f'P liegt {"senkrecht" if senk else "waagrecht"} neben M, Abstand {abs(k)}. {abs(k)} {"<" if abs(k) < r else "=" if abs(k) == r else ">"} {r}: {l}.',
                'h': 'P hat mit M eine Koordinate gemeinsam. Der Abstand ist der Unterschied der anderen Koordinate.'}
    art = R.randrange(2)
    mx, my, r = R.randint(-3, 3), R.randint(-3, 3), R.randint(2, 6)
    if art == 0:
        return luecke([my - r, my + r], f'Welche Punkte auf der senkrechten Linie durch M{p(mx, my)} haben von M den Abstand {r}? Gib ihre y-Koordinaten an (kleinere zuerst).',
                      'y = □ und y = □', 'Kleinere Zahl zuerst.', [f'({my}) - {r}', f'({my}) + {r}'], f'Von M aus {r} nach unten: {zt(my - r)}, {r} nach oben: {zt(my + r)}.',
                      'Gehe von M aus nach oben und nach unten.')
    n = 2 * r - 1
    return {'y': 'zahl', 'f': {'text': f'Wie viele Punkte mit ganzzahligen Koordinaten liegen auf der waagrechten Linie durch M{p(mx, my)} innerhalb des Kreises um M mit r = {r} (nicht auf dem Rand)?',
                               'grafik': fig_kreis(mx, my, r)},
            'o': {'wert': n}, 'c': f'2 * {r} - 1', 'w': f'Innerhalb heißt Abstand kleiner als {r}: x von {zt(mx - r + 1)} bis {zt(mx + r - 1)}. Das sind {n} Punkte (mit M).',
            'h': 'Zähle die x-Werte, die weniger als r von M entfernt sind – M selbst zählt mit.'}


# ---------- 2 Parallelen ----------
def g_par(st):
    c, d = R.randint(-3, 3), R.randint(1, 4)
    if st == 1:
        return luecke([c - d, c + d], f'g ist die waagrechte Gerade y = {zt(c)}. Alle Punkte mit Abstand {d} von g liegen auf zwei Parallelen. Welche y-Werte haben sie? (kleinerer zuerst)',
                      'y = □ und y = □', 'Kleinere Zahl zuerst.', [f'({c}) - {d}', f'({c}) + {d}'], f'{d} unter g: y = {zt(c - d)}, {d} über g: y = {zt(c + d)}.', 'Eine Parallele liegt über g, eine darunter.') \
            if R.random() < .6 else \
            {'y': 'zahl', 'f': {'text': f'Zwei Parallelen zu g haben beide den Abstand {d} cm von g. Wie weit sind die beiden Parallelen voneinander entfernt?'}, 'o': {'wert': 2 * d, 'einheit': 'cm'},
             'c': f'2 * {d}', 'w': f'Sie liegen auf verschiedenen Seiten von g: {d} + {d} = {2 * d} cm.', 'h': 'Mach eine Skizze mit g in der Mitte.'}
    if st == 2:
        x, y = R.randint(-4, 4), R.randint(c - d - 3, c + d + 3)
        a = abs(y - c)
        l = 'im Streifen' if a < d else 'auf dem Rand des Streifens' if a == d else 'außerhalb des Streifens'
        return {**wahl(R, l, [v for v in ['im Streifen', 'auf dem Rand des Streifens', 'außerhalb des Streifens'] if v != l]),
                'f': {'text': f'g ist die waagrechte Gerade y = {zt(c)}. Der Streifen enthält alle Punkte mit höchstens {d} Abstand zu g. Wo liegt P{p(x, y)}?',
                      'grafik': {'typ': 'koordinaten', 'x': [-6, 6], 'y': [min(c - d, y) - 1, max(c + d, y) + 1], 'waagrecht': [c, c - d, c + d], 'punkte': [{'x': x, 'y': y, 'name': 'P'}]}},
                'w': f'Abstand von P zu g: |{zt(y)} − {kl(c)}| = {a}. Vergleich mit {d}: {l}.', 'h': 'Berechne den Abstand von P zu g (Unterschied der y-Koordinaten).'}
    art = R.randrange(3)
    if art == 2:          # Mittelparallele (Prüfung)
        c1 = R.randint(-6, 2); c2 = c1 + 2 * R.randint(2, 5)
        m = (c1 + c2) // 2
        return luecke([m], f'g: y = {zt(c1)} und h: y = {zt(c2)} sind parallel. Welche Gerade enthält alle Punkte, die von g und h gleich weit entfernt sind?', 'y = □',
                      'Trage den y-Wert ein.', [f'(({c1}) + ({c2})) / 2'], f'Die Mittelparallele liegt genau in der Mitte: ({zt(c1)} + {kl(c2)}) : 2 = {zt(m)}. Sie hat von g und h je {c2 - m} Abstand.',
                      'Die gesuchte Gerade liegt genau in der Mitte zwischen g und h.')
    if art == 0:
        n = 2 * d + 1
        return {'y': 'zahl', 'f': {'text': f'g ist die waagrechte Gerade y = {zt(c)}. Wie viele Punkte mit ganzzahligen Koordinaten auf der senkrechten Linie x = 2 haben von g höchstens den Abstand {d}?'},
                'o': {'wert': n}, 'c': f'2 * {d} + 1', 'w': f'y von {zt(c - d)} bis {zt(c + d)}: Das sind {n} Werte.', 'h': 'Zähle alle y-Werte von c − d bis c + d.'}
    c2 = c + R.randint(3, 8)
    return {'y': 'zahl', 'f': {'text': f'Die waagrechten Geraden g: y = {zt(c)} und h: y = {zt(c2)} sind parallel. Welchen y-Wert haben alle Punkte, die von g und h gleich weit entfernt sind?'} if (c + c2) % 2 == 0 else
            {'text': f'Die waagrechten Geraden g: y = {zt(c)} und h: y = {zt(c2 + 1)} sind parallel. Wie weit sind sie voneinander entfernt?'},
            'o': {'wert': (c + c2) // 2} if (c + c2) % 2 == 0 else {'wert': c2 + 1 - c}, 'c': f'(({c}) + ({c2})) / 2' if (c + c2) % 2 == 0 else f'({c2 + 1}) - ({c})',
            'w': f'Die Mittelparallele liegt genau in der Mitte: ({zt(c)} + {zt(c2)}) : 2 = {zt(Fr(c + c2, 2))}.' if (c + c2) % 2 == 0 else f'Abstand: {zt(c2 + 1)} − {kl(c)} = {c2 + 1 - c}.',
            'h': 'Die Mitte zwischen zwei Zahlen: addieren und halbieren.' if (c + c2) % 2 == 0 else 'Unterschied der y-Werte.'}


# ---------- 3 Zwei Kreise ----------
def anzahl(e, r1, r2):
    if e > r1 + r2 or e < abs(r1 - r2): return 0
    if e == r1 + r2 or e == abs(r1 - r2): return 1
    return 2


def g_zwei(st):
    r1, r2 = R.randint(2, 8), R.randint(2, 8)
    e = R.choice([r1 + r2, r1 + r2 + R.randint(1, 4), R.randint(max(abs(r1 - r2) + 1, 2), r1 + r2 - 1) if r1 + r2 - 1 >= max(abs(r1 - r2) + 1, 2) else r1 + r2])
    n = anzahl(e, r1, r2)
    fig = {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [e, 0]}, 'kreise': [{'m': 'A', 'r': r1}, {'m': 'B', 'r': r2}], 'linien': [['A', 'B', f'{e} km', 'gestrichelt']]}
    if st == 1:
        return {'y': 'zahl', 'f': {'text': f'A und B sind {e} km voneinander entfernt. Wie viele Orte gibt es, die {r1} km von A und {r2} km von B entfernt sind?', 'grafik': fig},
                'o': {'wert': n}, 'c': f'{n}', 'w': f'r₁ + r₂ = {r1 + r2} km, Abstand {e} km. ' + ('Gleich: Die Kreise berühren sich, 1 Ort.' if n == 1 else 'Abstand größer: kein Ort.' if n == 0 else 'Abstand kleiner: 2 Orte.'),
                'h': 'Vergleiche den Abstand von A und B mit r₁ + r₂.'}
    if st == 2:
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Ein Ort soll {r1} km von A und {r2} km von B entfernt sein. Wie weit dürfen A und B höchstens auseinander liegen, damit es so einen Ort gibt?'},
                    'o': {'wert': r1 + r2, 'einheit': 'km'}, 'c': f'{r1} + {r2}', 'w': f'Die Kreise müssen sich mindestens berühren: höchstens {r1} + {r2} = {r1 + r2} km.', 'h': 'Wann berühren sich die beiden Kreise gerade noch?'}
        r = 'zwei' if n == 2 else 'einen' if n == 1 else 'keinen'
        return {**wahl(R, r, [x for x in ['zwei', 'einen', 'keinen', 'unendlich viele'] if x != r]), 'f': {'text': f'Kreis um A mit r = {r1} cm und Kreis um B mit r = {r2} cm. [AB] = {e} cm. Wie viele Schnittpunkte haben die Kreise?'},
                'w': f'{r1} + {r2} = {r1 + r2}, [AB] = {e}: ' + ('genau einen (Berührung).' if n == 1 else 'keinen.' if n == 0 else 'zwei.'), 'h': 'Vergleiche [AB] mit der Summe der Radien.'}
    art = R.randrange(3)
    if art == 2:          # Kreis im Kreis (Prüfung)
        rk = R.randint(5, 9); rs = R.randint(1, rk - 2)
        e2 = R.randint(1, rk - rs - 1) if R.random() < .6 and rk - rs > 1 else rk - rs
        n2 = anzahl(e2, rk, rs)
        r = 'keinen' if n2 == 0 else 'einen'
        return {**wahl_rund(R, r, [x for x in ['zwei', 'einen', 'keinen'] if x != r] + ['unendlich viele']),
                'f': {'text': f'Kreis um A mit r = {rs} cm, Kreis um B mit r = {rk} cm, [AB] = {e2} cm. Wie viele Schnittpunkte haben die Kreise?'},
                'w': f'Der kleine Kreis liegt im großen: {rk} − {rs} = {rk - rs} cm. ' + ('[AB] ist kleiner: Er liegt ganz innen, kein Schnittpunkt – obwohl [AB] kleiner als ' + str(rk + rs) + ' cm ist.' if n2 == 0 else '[AB] ist genau so groß: Er berührt den großen Kreis von innen, ein Punkt.'),
                'h': 'Liegt ein Kreis im anderen? Vergleiche [AB] auch mit dem Unterschied der Radien.'}
    if art == 0:
        ax = R.randint(-4, 0)
        rr1, rr2 = R.randint(2, 5), R.randint(2, 5)
        bx = ax + rr1 + rr2
        return punkt('T', ax + rr1, 0, f'Kreis um A{p(ax, 0)} mit r = {rr1} und Kreis um B{p(bx, 0)} mit r = {rr2} berühren sich. In welchem Punkt T?',
                     f'[AB] = {rr1 + rr2} = r₁ + r₂: Berührung auf der Strecke [AB], {rr1} rechts von A: T{p(ax + rr1, 0)}.', 'Der Berührpunkt liegt auf der Verbindungsstrecke, r₁ von A entfernt.',
                     f'({ax}) + {rr1}', '0')
    rk = R.randint(5, 9)
    rs = R.randint(1, rk - 2)
    e2 = rk - rs
    return {'y': 'zahl', 'f': {'text': f'Ein großer Kreis um A hat r = {rk} cm, ein kleiner Kreis um B hat r = {rs} cm. B liegt im großen Kreis, [AB] = {e2} cm. Wie viele gemeinsame Punkte haben die Kreise?'},
            'o': {'wert': 1}, 'c': f'1', 'w': f'{rk} − {rs} = {e2} = [AB]: Der kleine Kreis berührt den großen von innen – genau 1 Punkt.',
            'h': 'Wie weit reicht der kleine Kreis von A aus höchstens? [AB] + r₂.'}


# ---------- 4 Verknüpfen ----------
def g_verk(st):
    r = R.randint(2, 6)
    e = R.randint(1, 9)
    d = R.randint(1, 5)
    abst = [abs(e - d), e + d]
    n = sum(2 if a < r else 1 if a == r else 0 for a in abst)
    if st == 1:
        e = R.randint(0, r + 2)
        n1 = 2 if e < r else 1 if e == r else 0
        return {'y': 'zahl', 'f': {'text': f'Kreis um M mit r = {r} cm. Die Gerade g hat von M den Abstand {e} cm. Wie viele Punkte liegen auf dem Kreis und gleichzeitig auf g?',
                                   'grafik': fig_kreis(0, 0, r, gerade=e)}, 'o': {'wert': n1}, 'c': f'{n1}',
                'w': f'{e} cm {"<" if e < r else "=" if e == r else ">"} {r} cm: ' + ('Sekante, 2 Punkte.' if n1 == 2 else 'Tangente, 1 Punkt.' if n1 == 1 else 'Passante, kein Punkt.'), 'h': 'Vergleiche den Abstand von M zu g mit r.'}
    if st == 2 and ZAEHL['luecke'] < 6:          # höchstens 6 dieser Lückenaufgaben (Prüfung)
        ZAEHL['luecke'] += 1
        return luecke(abst if abst[0] <= abst[1] else abst[::-1], f'M ist {e} cm von der Geraden g entfernt. Zwei Parallelen zu g haben von g jeweils den Abstand {d} cm. Wie weit sind die beiden Parallelen von M entfernt? (kleineren Wert zuerst)',
                      '□ cm und □ cm', 'Kleineren Abstand zuerst.', [f'abs({e} - {d})', f'{e} + {d}'], f'Eine Parallele liegt zwischen M und g oder jenseits: |{e} − {d}| = {abs(e - d)} cm. Die andere: {e} + {d} = {e + d} cm.',
                      'Eine Parallele liegt näher an M, die andere weiter weg.')
    fig = {'typ': 'figur', 'punkte': {'M': [0, 0], '_G1': [-r - 3, -e], '_G2': [r + 3, -e], '_P1': [-r - 3, -e + d], '_P2': [r + 3, -e + d], '_Q1': [-r - 3, -e - d], '_Q2': [r + 3, -e - d]},
           'kreise': [{'m': 'M', 'r': r}], 'linien': [['_G1', '_G2', 'g'], ['_P1', '_P2', '', 'gestrichelt'], ['_Q1', '_Q2', '', 'gestrichelt']]}
    return {'y': 'zahl', 'f': {'text': f'M hat von g den Abstand {e} cm. Wie viele Punkte haben von M den Abstand {r} cm und von g den Abstand {d} cm?', 'grafik': fig},
            'o': {'wert': n}, 'c': f'{n}', 'w': f'Die Parallelen haben von M den Abstand {abst[0]} cm und {abst[1]} cm. Mit r = {r} cm: ' +
            ', '.join(f'{a} cm → {2 if a < r else 1 if a == r else 0}' for a in abst) + f'. Zusammen {n} {"Punkt" if n == 1 else "Punkte"}.',
            'h': 'Bestimme die Abstände der beiden Parallelen von M und vergleiche jeweils mit r.'}


# ---------- 5 Sachsituationen ----------
def g_sach(st):
    if st == 1:
        r = R.randint(2, 12)
        d = R.choice([r - 1, r + 1, r + 2, max(1, r - 3)])          # nie genau auf der Grenze (Prüfung)
        ding = R.choice([('Ein Rasensprenger erreicht alles bis', 'Ein Beet ist', 'vom Sprenger entfernt. Wird es gegossen?', 'm', 'Nur wenn der Sprenger doppelt so weit reicht wie der Abstand.'),
                         ('Ein Hund ist an einer Leine von', 'Sein Napf steht', 'vom Pflock entfernt. Erreicht der Hund den Napf?', 'm', 'Nur wenn die Leine doppelt so lang ist wie der Abstand.'),
                         ('Ein Funkmast reicht', 'Ein Haus steht', 'vom Mast entfernt. Hat das Haus Empfang?', 'km', 'Nur wenn der Mast doppelt so weit reicht wie der Abstand.')])
        ja = d <= r
        rr = 'Ja.' if ja else 'Nein.'
        return {**wahl_rund(R, rr, ['Nein.' if ja else 'Ja.', ding[4]], 3),
                'f': {'text': f'{ding[0]} {r} {ding[3]}{" angebunden" if "Leine" in ding[0] else ""}. {ding[1]} {d} {ding[3]} {ding[2]}'},
                'w': f'Erreichbar ist die Kreisfläche mit Radius {r} {ding[3]}. {d} {ding[3]} {"≤" if ja else ">"} {r} {ding[3]}: {rr}', 'h': 'Gilt Abstand ≤ Reichweite?'}
    if st == 2 and R.random() < .5:
        if R.random() < .5:
            r = R.randint(2, 9)
            return {'y': 'zahl', 'f': {'text': f'Ein Rasensprenger erreicht alles bis {r} m Entfernung. Wie breit ist die nasse Kreisfläche (Durchmesser)?'}, 'o': {'wert': 2 * r, 'einheit': 'm'},
                    'c': f'2 * {r}', 'w': f'{r} m ist der Radius. Der Durchmesser ist doppelt so lang: 2 · {r} m = {2 * r} m.', 'h': 'Die Reichweite ist der Radius.'}
        r = R.randint(2, 6); e = 2 * r + R.randint(1, 6)
        return {'y': 'zahl', 'f': {'text': f'Zwei Rasensprenger stehen {e} m auseinander, jeder reicht {r} m weit. Wie lang ist auf der Verbindungslinie das Stück, das trocken bleibt?'},
                'o': {'wert': e - 2 * r, 'einheit': 'm'}, 'c': f'{e} - 2 * {r}', 'w': f'Jeder Sprenger macht {r} m nass: zusammen {2 * r} m. Trocken bleiben {e} m − {2 * r} m = {e - 2 * r} m.',
                'h': 'Zeichne die Verbindungslinie und markiere, wie weit jeder Sprenger reicht.'}
    if st == 2:
        b = R.randint(6, 20)
        s = R.randint(1, 4)
        return {'y': 'zahl', 'f': {'text': f'Eine Straße ist {b} m breit. Auf beiden Seiten soll ein Sicherheitsstreifen von {s} m frei bleiben. Wie breit ist der Bereich insgesamt, in dem nichts gebaut werden darf?'},
                'o': {'wert': b + 2 * s, 'einheit': 'm'}, 'c': f'{b} + 2 * {s}', 'w': f'{s} m + {b} m + {s} m = {b + 2 * s} m.', 'h': 'Der Streifen liegt auf beiden Seiten.'}
    art = R.randrange(3)
    if art == 2:          # Weide am Zaun (Prüfung)
        l = R.randint(3, 8); pf = l + R.randint(1, 5)
        tier = R.choice(['Eine Ziege', 'Ein Schaf', 'Ein Pony'])
        return {'y': 'zahl', 'f': {'text': f'{tier} ist mit einer {l} m langen Leine an einem Pflock angebunden. Der Pflock steht {pf} m von einem geraden Zaun entfernt. Wie nah kommt das Tier an den Zaun heran?'},
                'o': {'wert': pf - l, 'einheit': 'm'}, 'c': f'{pf} - {l}', 'w': f'Das Tier erreicht einen Kreis mit r = {l} m. Am nächsten am Zaun ist es senkrecht zum Zaun: {pf} m − {l} m = {pf - l} m.',
                'h': 'Der kürzeste Weg zum Zaun ist senkrecht. Wie weit kommt das Tier auf diesem Weg?'}
    if art == 0:
        r, e = R.randint(2, 5), R.randint(1, 8)
        d = R.randint(1, 3)
        abst = [abs(e - d), e + d]
        n = sum(2 if a < r else 1 if a == r else 0 for a in abst)
        return {'y': 'zahl', 'f': {'text': f'Ein Schatz liegt {r} m von einer alten Eiche und {d} m von einem geraden Zaun entfernt. Die Eiche steht {e} m vom Zaun entfernt. An wie vielen Stellen kann der Schatz liegen?'},
                'o': {'wert': n}, 'c': f'{n}', 'w': f'Kreis um die Eiche (r = {r} m) und zwei Parallelen zum Zaun ({d} m). Abstände der Parallelen von der Eiche: {abst[0]} m und {abst[1]} m. Zusammen {n} Stellen.',
                'h': 'Kreis um die Eiche, zwei Parallelen zum Zaun – zähle die Schnittpunkte.'}
    a, b = R.randint(3, 8), R.randint(3, 8)
    e = R.randint(max(abs(a - b) + 1, 2), a + b + 3)
    n = anzahl(e, a, b)
    return {'y': 'zahl', 'f': {'text': f'Zwei Sender A und B stehen {e} km auseinander. Ein Handy hat genau {a} km Abstand zu A und genau {b} km Abstand zu B. An wie vielen Stellen kann es sein?'},
            'o': {'wert': n}, 'c': f'{n}', 'w': f'Kreise mit {a} km und {b} km um A und B. {a} + {b} = {a + b} km, Abstand {e} km: {n} {"Stelle" if n == 1 else "Stellen"}.',
            'h': 'Zeichne zwei Kreise und zähle die gemeinsamen Punkte.'}


# ---------- 6 Verstehen ----------
# Prüfung: alle Antworten mit gleich gebauter Begründung
def g_vers(st):
    r, d = R.randint(2, 7), R.randint(1, 5)
    if st == 1:
        aussagen = [(f'Alle Punkte mit Abstand {r} cm von M liegen auf einem Kreis.', f'Ja, auf dem Kreis um M mit r = {r} cm.', ['Nein, sie liegen auf einer Geraden durch M.', f'Nein, sie liegen auf einem Kreis mit r = {2 * r} cm.']),
                    (f'Es gibt genau einen Punkt mit Abstand {d} cm von der Geraden g.', 'Nein, es sind unendlich viele – auf zwei Parallelen zu g.', [f'Ja, nämlich den Punkt {d} cm senkrecht über g.', 'Nein, es sind genau zwei Punkte, einer auf jeder Seite.']),
                    (f'Ein Punkt mit Abstand {r} cm von M liegt innerhalb des Kreises mit r = {r} cm.', 'Nein, er liegt genau auf der Kreislinie.', [f'Ja, {r} cm ist nicht mehr als {r} cm.', 'Nein, er liegt außerhalb des Kreises.']),
                    (f'Ein Punkt mit Abstand {r - 1} cm von M liegt innerhalb des Kreises mit r = {r} cm.', f'Ja, {r - 1} cm < {r} cm.', [f'Nein, {r - 1} cm < {r} cm heißt außerhalb.', 'Nein, er liegt auf der Kreislinie.'])]
    elif st == 2:
        aussagen = [(f'Die Punkte mit höchstens {d} cm Abstand von g bilden einen Streifen der Breite {2 * d} cm.', f'Ja, {d} cm auf jeder Seite: {2 * d} cm.', [f'Nein, der Streifen ist nur {d} cm breit.', f'Nein, er ist {4 * d} cm breit.']),
                    (f'Die Punkte mit höchstens {d} cm Abstand von g bilden einen Streifen der Breite {d} cm.', f'Nein, der Streifen geht nach beiden Seiten: {2 * d} cm breit.', [f'Ja, der Abstand {d} cm ist die Breite.', f'Nein, er ist {4 * d} cm breit.']),
                    (f'Zwei Kreise mit r = {r} cm, deren Mittelpunkte {2 * r} cm auseinander liegen, berühren sich.', f'Ja, {r} cm + {r} cm = {2 * r} cm.', ['Nein, sie schneiden sich in zwei Punkten.', f'Nein, dafür müssten sie {r} cm auseinander liegen.']),
                    (f'Zwei Kreise mit r = {r} cm, deren Mittelpunkte {2 * r + 1} cm auseinander liegen, schneiden sich.', f'Nein, {2 * r + 1} cm > {r} cm + {r} cm: kein gemeinsamer Punkt.', [f'Ja, {2 * r + 1} cm ist weniger als 3 · {r} cm.', 'Ja, zwei gleich große Kreise schneiden sich immer.'])]
    else:
        aussagen = [('Ein Kreis und zwei Parallelen können zusammen 4 Schnittpunkte haben.', 'Ja, wenn beide Parallelen den Kreis schneiden (je 2 Punkte).', ['Nein, höchstens 2 Schnittpunkte.', 'Nein, höchstens 3 Schnittpunkte.']),
                    ('Ein Kreis und zwei Parallelen können 5 Schnittpunkte haben.', 'Nein, jede Gerade schneidet einen Kreis höchstens zweimal: höchstens 4.', ['Ja, wenn der Kreis groß genug ist.', 'Ja, 2 + 2 + 1 = 5.']),
                    ('Zwei Kreise können sich in drei Punkten schneiden.', 'Nein, zwei verschiedene Kreise haben höchstens 2 gemeinsame Punkte.', ['Ja, wenn sie sich stark überlappen.', 'Ja, wenn ein Kreis im anderen liegt.']),
                    (f'Ein Hund an einer {r} m langen Leine kann eine Kreisfläche mit Durchmesser {2 * r} m erreichen.', f'Ja, Radius {r} m, also Durchmesser {2 * r} m.', [f'Nein, der Durchmesser ist {r} m.', f'Nein, der Durchmesser ist {4 * r} m.'])]
    s_, grund, f = R.choice(aussagen)
    return {**wahl_rund(R, grund, f, 3), 'f': {'text': f'Stimmt die Aussage? „{s_}“'}, 'w': grund, 'h': 'Mach eine Skizze: Kreis für „Abstand zu M“, Parallelen für „Abstand zu g“.'}


GEN = {'kreislinie': g_kreis, 'parallelen': g_par, 'zwei_kreise': g_zwei, 'verknuepfen': g_verk, 'sachsituationen': g_sach, 'verstehen': g_vers}

DATEI = datei(E, 'Punkte bestimmen, die Abstandsbedingungen zu Punkten oder Geraden erfüllen, und Bedingungen verknüpfen – mit der Grundeigenschaft der Kreislinie.', MERKE,
              [('Einzelne Bedingungen', ['kreislinie', 'parallelen']),
               ('Bedingungen verknüpfen', ['zwei_kreise', 'verknuepfen']),
               ('Anwenden und verstehen', ['sachsituationen', 'verstehen'])],
              ETAPPEN, GEN,
              offen=['themenliste.json nennt keinen lehrplan_gym-Wortlaut. Gebaut nach LehrplanPLUS Gymnasium Kl. 5, Lernbereich 2: „Punkte bestimmen, die Bedingungen erfüllen (Abstand zu Punkten oder Geraden), Grundeigenschaft der Kreislinie“.',
                     'Mittelsenkrechte („gleich weit von A und B“) und Winkelhalbierende sind Stoff der Jahrgangsstufe 7 und wurden weggelassen.',
                     'Abstände im Koordinatensystem nur waagrecht/senkrecht, weil schräge Abstände den Satz des Pythagoras (Kl. 9) bräuchten.',
                     'Zeichnungen: Kreise, Parallelen, Streifen und Schnittfiguren als Figur bzw. Koordinatensystem. Eine Kreisfläche oder einen Streifen farbig zu füllen kann die App nicht; das Kind kann auch nicht selbst konstruieren.'])

# Verständliche Fassung (Siebte Runde, 15.11.): Alltagssituation zuerst (einstieg), jedes neue Wort erklärt (woerter),
# Beispiel in kleinen Schritten, Merksatz am Ende (regel). Situationen: Hund an der Leine, Hecke an der Straße, Funkmasten, Schatzsuche.
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _klar_kl5.py) – die Aufgaben bleiben wörtlich gleich.
from _klar_kl5 import klar  # noqa: E402

KLAR = {
 'kreislinie': {
  'einstieg': 'Ein Hund ist mit einer 3 m langen Leine an einem Pflock angebunden. Läuft er mit straffer Leine herum, läuft er im Kreis – jeder Punkt dieses Weges ist genau 3 m vom Pflock entfernt. Alle Punkte mit genau demselben Abstand zu einem festen Punkt bilden eine ⟦Kreislinie⟧.',
  'woerter': [['M(0 | 0)', 'der Punkt in der Mitte des Koordinatensystems, wo sich x-Achse (waagrecht) und y-Achse (senkrecht) kreuzen'], ['Einheit', 'ein Kästchenabstand im Koordinatensystem'],
              ['Kreislinie', 'alle Punkte, die vom Mittelpunkt genau den Abstand r haben – der Rand des Kreises'], ['Mittelpunkt M', 'der feste Punkt in der Mitte – hier der Pflock'],
              ['Radius r', 'der feste Abstand – hier die Länge der Leine'], ['innerhalb, außerhalb', 'näher am Mittelpunkt als r, weiter weg als r'],
              ['höchstens', 'so viel oder weniger'], ['Kreisfläche', 'alle Punkte mit höchstens r Abstand: das Innere samt Rand']],
  'schritte': ['Ein Kreis um M(0 | 0) hat den Radius r = 3. Liegt P(2 | 0) innerhalb, auf oder außerhalb?',
               'P liegt auf der x-Achse, 2 Einheiten rechts von M. Also ist P 2 von M entfernt.',
               'Vergleiche mit dem Radius: 2 ist kleiner als 3. P liegt ⟦innerhalb⟧ des Kreises.'],
  'regel': 'So prüfst du die Lage eines Punktes: Bestimme seinen ⟦Abstand zu M⟧ und vergleiche ihn mit ⟦r⟧. Kleiner als r: ⟦innerhalb⟧. Genau r: ⟦auf der Kreislinie⟧. Größer als r: ⟦außerhalb⟧. „Höchstens r“ heißt: Kreisfläche mit Rand.',
  'fehler': 'Einen Punkt mit Abstand 3 zu M „innerhalb“ nennen, wenn r = 3 ist, ist falsch: Er liegt genau ⟦auf⟧ der Kreislinie – wie der Hund, wenn die Leine gerade straff ist.'},
 'parallelen': {
  'einstieg': 'Entlang einer geraden Straße soll auf beiden Seiten eine Hecke gepflanzt werden, jeweils genau 2 m vom Straßenrand entfernt. Dann entstehen zwei Heckenreihen, links und rechts, und jede läuft gleich weit neben der Straße her. Alle Punkte mit festem Abstand zu einer Geraden liegen auf so einem ⟦Parallelenpaar⟧.',
  'woerter': [['senkrecht', 'im rechten Winkel, wie ein Laternenpfahl auf der Straße'], ['Parallele', 'eine Gerade, die überall gleich weit von g entfernt ist'], ['Parallelenpaar', 'die zwei Parallelen auf beiden Seiten von g'],
              ['y = 1', 'die waagrechte Gerade durch alle Punkte mit der y-Koordinate 1'], ['Abstand von g', 'die Länge des senkrechten Wegs zu g'],
              ['Streifen', 'der Bereich zwischen den beiden Parallelen']],
  'schritte': ['g ist die waagrechte Gerade y = 1. Gesucht sind alle Punkte mit dem Abstand 2 von g.',
               'Gehe von g senkrecht 2 nach oben: 1 + 2 = 3. Dort liegt die eine Parallele, ⟦y = 3⟧.',
               'Gehe von g senkrecht 2 nach unten: 1 − 2 = −1. Dort liegt die andere Parallele, ⟦y = −1⟧.'],
  'regel': 'So findest du alle Punkte mit Abstand d von einer Geraden g: Zeichne ⟦zwei Parallelen⟧ zu g, ⟦auf jeder Seite eine⟧, jeweils im Abstand d. Punkte mit ⟦höchstens d⟧ Abstand bilden den ⟦Streifen⟧ dazwischen.',
  'fehler': 'Nur eine Parallele einzeichnen ist ein häufiger Fehler – wie eine Hecke nur auf einer Straßenseite. Es gibt ⟦auf beiden Seiten⟧ von g Punkte mit Abstand d.'},
 'zwei_kreise': {
  'einstieg': 'Zwei Funkmasten A und B stehen 8 km voneinander entfernt. Ein Handy ist 5 km von A und 4 km von B entfernt. Wo kann es sein? Es liegt auf dem Kreis um A mit 5 km und zugleich auf dem Kreis um B mit 4 km – also dort, wo sich die Kreise treffen. Diese Stellen heißen ⟦Schnittpunkte⟧.',
  'woerter': [['Schnittpunkt', 'ein Punkt, der auf beiden Linien zugleich liegt'], ['r₁, r₂', 'die Radien der beiden Kreise (gelesen „r eins“, „r zwei“)'],
              ['[AB]', 'hier: die Länge der Strecke von A nach B'], ['und', 'beide Bedingungen müssen gleichzeitig erfüllt sein']],
  'schritte': ['A und B sind 8 km voneinander entfernt. Gesucht sind Orte, die 5 km von A und 4 km von B entfernt sind.',
               'Stell dir den Kreis um A mit 5 km und den Kreis um B mit 4 km vor. Zusammen reichen die Radien 5 + 4 = 9 km weit.',
               '9 km sind mehr als 8 km. Die Kreise überlappen also ein Stück und schneiden sich oberhalb und unterhalb der Strecke [AB].',
               'Es gibt ⟦zwei⟧ solche Orte.'],
  'regel': 'So zählst du die Orte: Sie liegen in den ⟦Schnittpunkten⟧ der beiden Kreise. [AB] ⟦größer als r₁ + r₂⟧: kein Punkt. [AB] ⟦gleich r₁ + r₂⟧: genau einer. Sonst meist zwei – außer ein Kreis liegt ganz im anderen: Ist der ⟦Unterschied der Radien⟧ größer als [AB], gibt es keinen Punkt, ist er gleich [AB], genau einen.'},
 'verknuepfen': {
  'einstieg': 'Ein Schatz liegt 3 m vom alten Baum entfernt und 2 m vom Gartenzaun. Jede Angabe allein beschreibt eine ganze Linie: einen Kreis um den Baum und zwei Parallelen zum Zaun. Der Schatz muss auf beiden zugleich liegen. Zwei Bedingungen so zusammenzunehmen heißt, sie zu ⟦verknüpfen⟧.',
  'woerter': [['Ortslinie', 'die Linie, auf der alle Punkte mit einer bestimmten Eigenschaft liegen (Kreis oder Parallelen)'],
              ['verknüpfen', 'zwei Bedingungen mit „und“ verbinden: beide müssen gelten'], ['Tangente', 'eine Gerade, die den Kreis in genau einem Punkt berührt']],
  'schritte': ['M hat von der Geraden g den Abstand 5. Gesucht sind Punkte mit Abstand 3 von M und Abstand 2 von g.',
               'Die Punkte mit Abstand 2 von g liegen auf zwei Parallelen. Die eine ist M näher: 5 − 2 = 3 von M entfernt. Die andere ist 5 + 2 = 7 von M entfernt.',
               'Die nähere Parallele hat von M den Abstand 3, genau so viel wie der Radius. Sie berührt den Kreis als Tangente in einem Punkt.',
               'Die andere ist 7 entfernt, mehr als der Radius 3: kein Treffer. Es gibt genau ⟦einen⟧ Punkt.'],
  'regel': 'So verknüpfst du „Abstand r von M ⟦und⟧ Abstand d von g“: Schneide den ⟦Kreis um M⟧ mit den ⟦beiden Parallelen⟧ zu g. Jede Parallele trifft den Kreis in 2, 1 oder 0 Punkten – zähle für ⟦beide⟧ Parallelen.'},
 'sachsituationen': {
  'einstieg': 'Ein Rasensprenger erreicht alles bis 4 m Entfernung. Ein Funkmast hat eine bestimmte Reichweite. Neben einer Straße soll ein Sicherheitsstreifen frei bleiben. All das sind Fragen nach Abständen. Du übersetzt sie in Kreise oder Parallelen – in eine ⟦Abstandsbedingung⟧.',
  'woerter': [['Abstandsbedingung', 'eine Vorgabe wie „höchstens 4 m vom Sprenger entfernt“'], ['Reichweite', 'die größte Entfernung, die etwas erreicht'],
              ['≤', '„kleiner oder gleich“, also höchstens'], ['Sicherheitsabstand', 'ein Abstand, der aus Sicherheitsgründen frei bleiben muss']],
  'schritte': ['Ein Rasensprenger erreicht alles bis 4 m. Ein Beet liegt 3 m vom Sprenger entfernt. Wird es gegossen?',
               '„Bis 4 m“ heißt höchstens 4 m. Das ist die ganze Kreisfläche um den Sprenger mit r = 4 m.',
               'Das Beet ist 3 m entfernt, und 3 m ≤ 4 m. Es liegt in der Kreisfläche und wird ⟦gegossen⟧.'],
  'regel': 'So löst du Abstandsfragen im Alltag: Übersetze die Bedingung. ⟦Reichweite⟧ von Sprenger oder Funkmast und Länge einer ⟦Leine⟧: Kreisfläche. ⟦Sicherheitsabstand⟧ zu einer Straße: Streifen zwischen Parallelen. Dann prüfst du, ob der Punkt darin liegt.'},
 'verstehen': {
  'einstieg': 'Jemand sagt: „Es gibt nur einen Platz, der genau 2 m vom Zaun entfernt ist.“ Stell dir den Zaun vor: Du kannst an sehr vielen Stellen 2 m davor stehen – und auch auf der anderen Seite. Solche Aussagen prüfst du am besten mit einer kleinen ⟦Skizze⟧.',
  'woerter': [['Skizze', 'eine schnelle Zeichnung ohne genaue Maße'], ['Punktmenge', 'alle Punkte, die eine Bedingung erfüllen'],
              ['genau, höchstens, mindestens', 'genau gleich viel / so viel oder weniger / so viel oder mehr'], ['unendlich viele', 'so viele, dass man nie mit dem Zählen fertig wird']],
  'schritte': ['Die Aussage: „Es gibt genau einen Punkt mit Abstand 2 von g.“',
               'Skizze: Alle Punkte mit Abstand 2 von g liegen auf zwei Parallelen zu g, eine auf jeder Seite.',
               'Auf jeder Parallele liegen unendlich viele Punkte. Die Aussage ist ⟦falsch⟧.'],
  'regel': 'So prüfst du Aussagen über Punktmengen: Zeichne eine ⟦Skizze⟧ – Kreis um M für „Abstand zu M“, Parallelenpaar für „Abstand zu g“. Achte genau auf die Wörter ⟦genau⟧, ⟦höchstens⟧ und ⟦mindestens⟧.'},
}
klar(DATEI, KLAR)


if __name__ == '__main__':
    schreibe(DATEI)
