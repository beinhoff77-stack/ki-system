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

# Umbau U5 (Achte Runde, Vorgabe 16.11.): Lernkarten nach dem neuen Muster – einstieg, woerter (≤ 3), Kartenbild,
# Bildergeschichte (schritte mit bild), „Pass auf!“ (fehler + fehler_bild), MERKE (regel).
# Situationen: Hund an der Leine, Hecke an der Straße, Funkmasten, Schatzsuche, Rasensprenger, Zaun.
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl5.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl5 import umbau  # noqa: E402

SCHATZ = {'M': [0, 0], '_g1': [-6, -5], '_g2': [6, -5], '_p1': [-6, -3], '_p2': [6, -3], '_q1': [-6, -7], '_q2': [6, -7], '_L': [0, -5]}
ZAUN = [['_g1', '_g2', 'g'], ['M', '_L', '5', 'gestrichelt']]
S_Y = round((25 - (73 / 16) ** 2) ** 0.5, 3)  # Schnittpunkte der Kreise um A(0|0), r = 5, und B(8|0), r = 4: x = 73/16

KARTEN = {
 'kreislinie': {
  'einstieg': 'Ein Hund ist an einer 3 m langen Leine an einem Pflock angebunden. Mit straffer Leine läuft er im Kreis. Alle Punkte mit genau 3 m Abstand bilden eine ⟦Kreislinie⟧.',
  'woerter': [['Kreislinie', 'alle Punkte mit genau dem Abstand r vom Mittelpunkt'], ['Radius r', 'der feste Abstand, hier die Länge der Leine'],
              ['innerhalb', 'näher am Mittelpunkt als r']],
  'bild': {'typ': 'figur', 'punkte': {'M': [0, 0], '_R': [0, 3]}, 'kreise': [{'m': 'M', 'r': 3}], 'linien': [['M', '_R', 'r = 3']]},
  'schritte': [{'text': 'Der Pflock ist der Mittelpunkt M, die Leine ist der Radius r = 3.'},
               {'text': 'Der Napf P ist 2 von M entfernt.', 'bild': {'punkte': {'M': [0, 0], 'P': [2, 0], '_R': [0, 3]}, 'linien': [['M', '_R', 'r = 3'], ['M', 'P', '2', 'gestrichelt']]}},
               {'text': '2 ist kleiner als 3: P liegt ⟦innerhalb⟧. Der Hund erreicht den Napf.'}],
  'fehler': 'Bei Abstand genau 3 „innerhalb“ sagen ist falsch. Dann liegt P genau auf der Kreislinie, die Leine ist straff.',
  'fehler_bild': {'punkte': {'M': [0, 0], 'P': [3, 0], '_R': [0, 3]}, 'linien': [['M', '_R', 'r = 3'], ['M', 'P', '3', 'gestrichelt']]},
  'regel': 'Vergleiche den ⟦Abstand zu M⟧ mit r. Kleiner: innerhalb, gleich: auf der Kreislinie, größer: außerhalb.'},
 'parallelen': {
  'einstieg': 'An einer geraden Straße soll auf beiden Seiten eine Hecke stehen, je 2 m entfernt. So entstehen zwei Reihen, links und rechts. Punkte mit festem Abstand zu einer Geraden liegen auf zwei ⟦Parallelen⟧.',
  'woerter': [['Parallele', 'eine Gerade, die überall gleich weit von g entfernt ist'], ['y = 1', 'die waagrechte Gerade durch alle Punkte mit der y-Koordinate 1']],
  'bild': {'typ': 'koordinaten', 'x': [-4, 4], 'y': [-2, 4], 'waagrecht': [1]},
  'schritte': [{'text': 'g ist die Gerade y = 1. Gesucht sind alle Punkte mit Abstand 2.'},
               {'text': '2 nach oben: 1 + 2 = 3. Das ist die Parallele ⟦y = 3⟧.', 'bild': {'waagrecht': [1, 3], 'strecken': [[0, 1, 0, 3, 'gestrichelt']]}},
               {'text': '2 nach unten: 1 − 2 = −1. Das ist die Parallele ⟦y = −1⟧.',
                'bild': {'waagrecht': [1, 3, -1], 'strecken': [[0, 1, 0, 3, 'gestrichelt'], [0, 1, 0, -1, 'gestrichelt']]}}],
  'fehler': 'Nur eine Parallele zeichnen ist ein häufiger Fehler. Wie eine Hecke nur auf einer Straßenseite: Die andere Seite fehlt.',
  'fehler_bild': {'waagrecht': [1, 3], 'strecken': [[0, 1, 0, 3, 'gestrichelt']]},
  'regel': 'Abstand d zu g: ⟦zwei Parallelen⟧, auf jeder Seite eine. Höchstens d Abstand: der Streifen dazwischen.'},
 'zwei_kreise': {
  'einstieg': 'Zwei Funkmasten A und B stehen 8 km auseinander. Ein Handy ist 5 km von A und 4 km von B entfernt. Es liegt dort, wo sich zwei Kreise treffen: in den ⟦Schnittpunkten⟧.',
  'woerter': [['Schnittpunkt', 'ein Punkt, der auf beiden Kreisen liegt']],
  'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [8, 0]}, 'linien': [['A', 'B', '8 km', 'gestrichelt']]},
  'schritte': [{'text': 'Kreis um A mit 5 km: Dort ist alles 5 km von A weg.', 'bild': {'kreise': [{'m': 'A', 'r': 5}]}},
               {'text': 'Dazu der Kreis um B mit 4 km.', 'bild': {'kreise': [{'m': 'A', 'r': 5}, {'m': 'B', 'r': 4}]}},
               {'text': '5 + 4 = 9 ist mehr als 8: Die Kreise überlappen.'},
               {'text': 'Sie schneiden sich oberhalb und unterhalb von AB: ⟦zwei⟧ Orte.',
                'bild': {'punkte': {'A': [0, 0], 'B': [8, 0], 'S₁': [73 / 16, S_Y], 'S₂': [73 / 16, -S_Y]}}}],
  'fehler': 'Immer zwei Orte erwarten ist falsch. Bei mehr als 9 km Abstand treffen sich die Kreise gar nicht.',
  'fehler_bild': {'punkte': {'A': [0, 0], 'B': [10, 0]}, 'linien': [['A', 'B', '10 km', 'gestrichelt']]},
  'regel': 'Die Orte liegen in den ⟦Schnittpunkten⟧ der Kreise. Meist sind es zwei. Berühren sich die Kreise nur, ist es einer.'},
 'verknuepfen': {
  'einstieg': 'Ein Schatz liegt 3 m vom alten Baum und 2 m vom Gartenzaun entfernt. Jede Angabe allein beschreibt eine ganze Linie. Der Schatz liegt auf beiden: Die Bedingungen werden ⟦verknüpft⟧.',
  'woerter': [['verknüpft', 'mit „und“ verbunden: Beide Bedingungen gelten'], ['Tangente', 'berührt den Kreis in genau einem Punkt']],
  'bild': 'BEHALTEN',
  'schritte': [{'text': 'Baum M ist 5 m vom Zaun g entfernt. Kreis um M: r = 3.', 'bild': {'punkte': SCHATZ, 'linien': ZAUN}},
               {'text': 'Abstand 2 vom Zaun: zwei Parallelen, 3 m und 7 m von M entfernt.',
                'bild': {'linien': ZAUN + [['_p1', '_p2', '', 'gestrichelt'], ['_q1', '_q2', '', 'gestrichelt']]}},
               {'text': 'Die nahe Parallele ist 3 m entfernt, genau r: eine Tangente.'},
               {'text': 'Die andere ist 7 m entfernt, zu weit. Es gibt genau ⟦einen⟧ Punkt.', 'bild': {'punkte': dict(SCHATZ, T=[0, -3])}}],
  'fehler': 'Nur die Parallele auf der Seite von M prüfen kann Punkte übersehen. Prüfe immer beide Parallelen.',
  'regel': 'Schneide den Kreis mit ⟦beiden Parallelen⟧. Jede trifft ihn in 2, 1 oder 0 Punkten.'},
 'sachsituationen': {
  'einstieg': 'Ein Rasensprenger erreicht alles bis 4 m, ein Beet liegt 3 m entfernt. Wird es gegossen? Das ist eine ⟦Abstandsbedingung⟧.',
  'woerter': [['Abstandsbedingung', 'eine Vorgabe wie „höchstens 4 m entfernt“'], ['≤', '„kleiner oder gleich“, also höchstens'],
              ['Kreisfläche', 'alle Punkte mit höchstens r Abstand: das Innere samt Rand']],
  'bild': {'typ': 'figur', 'punkte': {'Sprenger': [0, 0], '_R': [4, 0]}, 'kreise': [{'m': 'Sprenger', 'r': 4}], 'linien': [['Sprenger', '_R', '4 m']]},
  'schritte': [{'text': '„Bis 4 m“ heißt höchstens 4 m: die ganze Kreisfläche.'},
               {'text': 'Das Beet ist 3 m vom Sprenger entfernt.',
                'bild': {'punkte': {'Sprenger': [0, 0], '_R': [4, 0], 'Beet': [0, 3]}, 'linien': [['Sprenger', '_R', '4 m'], ['Sprenger', 'Beet', '3 m', 'gestrichelt']]}},
               {'text': '3 m ≤ 4 m: Das Beet liegt in der Kreisfläche und wird ⟦gegossen⟧.'}],
  'fehler': '„Höchstens 4 m“ als „genau 4 m“ lesen ist falsch. Gemeint ist die ganze Kreisfläche, nicht nur der Rand.',
  'regel': 'Reichweite und Leine: ⟦Kreisfläche⟧. Sicherheitsabstand zur Straße: Streifen zwischen zwei Parallelen.'},
 'verstehen': {
  'einstieg': 'Jemand meint, nur ein einziger Platz sei genau 2 m vom Zaun entfernt. Dabei kannst du an sehr vielen Stellen 2 m davor stehen. Solche Aussagen prüfst du mit einer ⟦Skizze⟧.',
  'woerter': [['Skizze', 'eine schnelle Zeichnung ohne genaue Maße'], ['unendlich viele', 'so viele, dass man nie mit dem Zählen fertig wird']],
  'bild': {'typ': 'koordinaten', 'x': [-4, 4], 'y': [-3, 3], 'waagrecht': [0]},
  'schritte': [{'text': 'Aussage: „Es gibt genau einen Punkt mit Abstand 2 von g.“'},
               {'text': 'Skizze: Alle diese Punkte liegen auf zwei Parallelen zu g.', 'bild': {'waagrecht': [0, 2, -2]}},
               {'text': 'Auf jeder liegen unendlich viele Punkte. Die Aussage ist ⟦falsch⟧.',
                'bild': {'punkte': [{'x': x, 'y': y} for y in (2, -2) for x in (-3, -1.5, 0, 1.5, 3)]}}],
  'fehler': 'Ortslinien haben meist unendlich viele Punkte. Erst eine zweite Bedingung lässt oft nur einzelne Punkte übrig.',
  'regel': 'Prüfe Aussagen über Punkte mit einer ⟦Skizze⟧. Achte auf genau, höchstens und mindestens.'},
}
umbau(DATEI, KARTEN)


# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl5) ----------
# Neue Übungen nach Vorbild von Klassenarbeiten Kl. 5 (Parallele mit Abstand, Punkte mit gleichem Abstand zu g und h),
# klassischen Ortslinien-Aufgaben („Punkte mit Abstand 3 von g und 6 von P“) und Sachaufgaben (Leine, Sender, Schatz).
# Nur Abstände entlang einer Linie – kein Satz des Pythagoras (Kl. 9). Eigene Zahlen und Einkleidung.
from _schwer_kl5 import A, L, Z, de, einzig, ergaenze, wahl  # noqa: E402


def _schnitt(d, r):
    """Gemeinsame Punkte von Gerade (Abstand d zum Mittelpunkt) und Kreis (Radius r)."""
    return 2 if d < r else (1 if d == r else 0)


def _kreise(a, r1, r2):
    """Gemeinsame Punkte zweier Kreise mit Mittelpunktsabstand a (a > 0)."""
    if a > r1 + r2 or a < abs(r1 - r2): return 0
    if a == r1 + r2 or a == abs(r1 - r2): return 1
    return 2


def _schwer():
    N = {}
    lage = {'(5 | 1)': (5, 1), '(2 | 3)': (2, 3), '(−1 | 1)': (-1, 1), '(2 | −3)': (2, -3)}
    auf = {'(0 | −5)': (0, -5), '(5 | 5)': (5, 5), '(2 | 3)': (2, 3), '(−4 | 0)': (-4, 0)}
    N['kreislinie'] = [
        wahl(2, 'Kreis um M(2 | 1) mit r = 3. Welcher Punkt liegt außerhalb des Kreises?', list(lage),
             lambda o: max(abs(lage[o][0] - 2), abs(lage[o][1] - 1)) > 3 and (lage[o][0] == 2 or lage[o][1] == 1),
             '(2 | −3) liegt 4 unter M: 4 > 3, also außerhalb. (5 | 1) und (−1 | 1) liegen genau 3 neben M (auf der Kreislinie), (2 | 3) liegt 2 über M (innen).',
             'Gehe von M aus waagrecht oder senkrecht und zähle die Einheiten.'),
        wahl(2, 'Kreis um M(0 | 0) mit r = 5. Welcher Punkt liegt sicher auf der Kreislinie?', list(auf), lambda o: auf[o] == (0, -5),
             '(0 | −5) liegt genau 5 Einheiten unter M. (−4 | 0) ist nur 4 entfernt, (2 | 3) liegt innen, (5 | 5) liegt schräg weiter weg als 5.',
             'Suche einen Punkt, der genau 5 Einheiten waagrecht oder senkrecht von M entfernt ist.'),
        Z(3, 'Ein Kreis um M hat den Radius 4 cm. P liegt auf der Kreislinie. Q liegt genau in der Mitte der Strecke [MP]. Wie weit ist Q von der Kreislinie entfernt (kürzester Weg)?',
          '4 - 4 / 2', 'Q ist 2 cm von M entfernt. Bis zur Kreislinie fehlen 4 cm − 2 cm = 2 cm.', 'Wie weit ist Q von M entfernt?', einheit='cm'),
        Z(3, 'A und B liegen beide auf einem Kreis mit dem Radius 5 cm. Wie weit können A und B höchstens voneinander entfernt sein?', '2 * 5',
          'Am weitesten auseinander liegen sie, wenn [AB] durch M geht: dann ist [AB] ein Durchmesser, 2 · 5 cm = 10 cm.', 'Welche Strecke im Kreis ist die längste?', einheit='cm'),
        Z(3, 'Eine Ziege ist mit einer 6 m langen Leine an einem Pflock angebunden. Ein Busch steht 9 m vom Pflock entfernt. Um wie viele Meter muss die Leine mindestens länger werden, damit die Ziege den Busch erreicht?',
          '9 - 6', 'Die Ziege erreicht alles bis 6 m. Zum Busch fehlen 9 m − 6 m = 3 m.', 'Die Leine ist der Radius des erreichbaren Kreises.', einheit='m'),
        A(3, 'Jemand sagt: „P ist 6 cm von M entfernt. Der Kreis um M hat den Durchmesser 10 cm. Also liegt P innerhalb.“ Stimmt das?',
          'Nein: Der Radius ist 5 cm. 6 cm > 5 cm, P liegt außerhalb.', ['Ja, 6 cm < 10 cm.', 'Nein, P liegt auf der Kreislinie.', 'Das kann man nicht entscheiden.'],
          'Verglichen wird mit dem Radius, nicht mit dem Durchmesser: r = 10 cm : 2 = 5 cm.', 'Womit musst du den Abstand vergleichen: Radius oder Durchmesser?'),
    ]
    streifen = {'(0 | 4)': 4, '(2 | −2)': -2, '(5 | −3)': -3, '(−4 | 0)': 0}
    zwischen = [y for y in range(-20, 30) if abs(y - 2) == 2 * abs(y - 8)]
    N['parallelen'] = [
        Z(2, 'Wie breit ist der Streifen aller Punkte, die von der Geraden g höchstens 2,5 cm entfernt sind?', '2 * 2.5', '2,5 cm auf jeder Seite von g: 2 · 2,5 cm = 5 cm.',
          'Der Streifen reicht auf beide Seiten von g.', einheit='cm'),
        wahl(2, 'g ist die waagrechte Gerade y = 1. Der Streifen enthält alle Punkte mit höchstens 3 Abstand zu g. Welcher Punkt liegt außerhalb?', list(streifen),
             lambda o: abs(streifen[o] - 1) > 3, 'Der Streifen reicht von y = −2 bis y = 4. (5 | −3) liegt darunter, also außerhalb. (0 | 4) und (2 | −2) liegen auf dem Rand.',
             'Bestimme zuerst die beiden Randlinien des Streifens.'),
        L(3, 'g ist die Gerade y = −5, h ist die Gerade y = 3. P liegt auf der y-Achse und ist von g und h gleich weit entfernt. Welche Koordinaten hat P?',
          'P(□ | □)', 'Trage x- und y-Koordinate ein.', ['0', '(-5 + 3) // 2'],
          'Gleich weit von g und h: die Mittelparallele in der Mitte zwischen −5 und 3, also y = −1. Auf der y-Achse ist x = 0: P(0 | −1).',
          'Wo liegt die Mitte zwischen y = −5 und y = 3?'),
        Z(3, 'Wie viele Punkte haben von der x-Achse den Abstand 2 und von der y-Achse den Abstand 3?', str(len({(x, y) for x in (-3, 3) for y in (-2, 2)})),
          'Abstand 2 zur x-Achse: y = 2 oder y = −2. Abstand 3 zur y-Achse: x = 3 oder x = −3. Jede Kombination passt: 4 Punkte.',
          'Jede Bedingung ergibt zwei Parallelen. Wie oft schneiden sie sich?'),
        Z(3, 'Die parallelen Geraden g und h haben den Abstand 6 cm. Wie viele Geraden gibt es, die zu beiden parallel sind und von g den Abstand 2 cm und von h den Abstand 4 cm haben?',
          '1', 'Zwischen g und h, 2 cm von g: Dann ist sie 4 cm von h entfernt – passt. Außerhalb, 2 cm von g, wäre sie 8 cm von h entfernt. Genau 1 Gerade.',
          'Zeichne g und h. Prüfe die beiden Parallelen zu g im Abstand 2 cm.'),
        L(3, 'g ist die Gerade y = 2, h die Gerade y = 8. Welche Punkte der y-Achse sind von g doppelt so weit entfernt wie von h? Gib die y-Werte an (kleinerer zuerst).',
          'y = □ und y = □', 'Trage beide y-Werte ein.', [str(zwischen[0]), str(zwischen[1])],
          'Zwischen g und h: bei y = 6 ist der Abstand zu g 4, zu h 2. Oberhalb von h: bei y = 14 ist der Abstand zu g 12, zu h 6. Zwei Lösungen.',
          'Denk auch an Punkte oberhalb von h. Probiere y-Werte aus.'),
    ]
    N['zwei_kreise'] = [
        Z(2, 'A und B sind 10 cm voneinander entfernt. Wie viele Punkte sind von A und von B jeweils genau 5 cm entfernt?', str(_kreise(10, 5, 5)),
          '5 cm + 5 cm = 10 cm: Die beiden Kreise berühren sich genau in der Mitte von [AB]. 1 Punkt.', 'Zeichne die Kreise um A und B mit r = 5 cm.'),
        Z(2, 'A und B sind 6 cm voneinander entfernt. Wie viele Punkte sind von A und von B jeweils genau 4 cm entfernt?', str(_kreise(6, 4, 4)),
          '4 cm + 4 cm = 8 cm ist mehr als 6 cm: Die Kreise schneiden sich, oberhalb und unterhalb von [AB]. 2 Punkte.', 'Vergleiche r₁ + r₂ mit dem Abstand von A und B.'),
        Z(3, 'Ein Kreis um A mit r = 4 cm und ein Kreis um B mit r = 7 cm sollen sich von außen in genau einem Punkt berühren. Wie weit sind A und B voneinander entfernt?',
          '4 + 7', 'Berühren von außen: Der Berührpunkt liegt auf [AB], also [AB] = 4 cm + 7 cm = 11 cm.', 'Zeichne die Kreise so, dass sie sich gerade noch berühren.', einheit='cm'),
        wahl(3, 'Ein Kreis um A mit r = 4 cm und ein Kreis um B mit r = 7 cm sollen sich in zwei Punkten schneiden. Welcher Abstand [AB] ist möglich?', ['2 cm', '3 cm', '8 cm', '11 cm'],
             lambda o: _kreise(int(o.split()[0]), 4, 7) == 2, 'Zwei Schnittpunkte gibt es, wenn [AB] zwischen 7 − 4 = 3 cm und 7 + 4 = 11 cm liegt (ohne die Grenzen). Nur 8 cm passt.',
             'Bei 11 cm berühren sie sich außen, bei 3 cm innen. Was liegt dazwischen?'),
        L(3, 'Welcher Punkt hat von A(−3 | 0) und von B(5 | 0) jeweils genau den Abstand 4?', 'P(□ | □)', 'Trage x- und y-Koordinate ein.', ['(-3 + 5) // 2', '0'],
          '[AB] = 8 = 4 + 4. Die Kreise berühren sich nur in der Mitte von [AB]: P(1 | 0).', 'Wie lang ist [AB]? Vergleiche mit 4 + 4.'),
        A(3, 'Jemand sagt: „Kreise mit r = 3 cm und r = 5 cm, deren Mittelpunkte 1 cm auseinander liegen, schneiden sich, weil 1 cm < 3 cm + 5 cm.“ Stimmt das?',
          'Nein: Der kleine Kreis liegt ganz im großen, weil 1 cm < 5 cm − 3 cm.', ['Ja, das stimmt.', 'Nein, sie berühren sich in einem Punkt.', 'Ja, in vier Punkten.'],
          'Der Unterschied der Radien ist 2 cm. Ist der Abstand kleiner als 2 cm, liegt der kleine Kreis innen und trifft den großen nicht.',
          'Zeichne beide Kreise mit fast gleichem Mittelpunkt.'),
    ]
    rr = [r for r in range(1, 10) if _schnitt(3 - 1, r) + _schnitt(3 + 1, r) == 3]
    N['verknuepfen'] = [
        Z(2, 'M hat von der Geraden g den Abstand 5 cm. Wie viele Punkte von g haben von M genau den Abstand 5 cm?', str(_schnitt(5, 5)),
          'Abstand gleich Radius: g ist Tangente des Kreises um M mit r = 5 cm. Genau 1 Punkt.', 'Vergleiche den Abstand mit dem Radius.'),
        Z(2, 'Kreis um M mit r = 2 cm. M hat von g den Abstand 6 cm. Wie viele Punkte von g haben von M höchstens 2 cm Abstand?', str(_schnitt(6, 2)),
          'Der nächste Punkt von g ist 6 cm von M entfernt, mehr als 2 cm. Kein Punkt.', 'Wie nah kommt g an M heran?'),
        Z(3, 'P hat von der Geraden g den Abstand 2 cm. Wie viele Punkte haben von g den Abstand 3 cm und von P den Abstand 4 cm?', str(_schnitt(1, 4) + _schnitt(5, 4)),
          'Die Parallele auf der Seite von P ist 1 cm von P entfernt: Der Kreis (r = 4 cm) schneidet sie zweimal. Die andere ist 5 cm entfernt: kein Schnitt. Zusammen 2.',
          'Zeichne beide Parallelen zu g im Abstand 3 cm. Wie weit ist jede von P entfernt?'),
        Z(3, 'M liegt auf der Geraden g. Wie viele Punkte haben von M den Abstand 3 cm und von g den Abstand 3 cm?', str(_schnitt(3, 3) * 2),
          'Die beiden Parallelen sind je 3 cm von M entfernt, genau r: Jede berührt den Kreis einmal. Zusammen 2 Punkte.', 'Wie weit sind die beiden Parallelen von M entfernt?'),
        Z(3, 'M hat von g den Abstand 3 cm. Die beiden Parallelen zu g im Abstand 1 cm und der Kreis um M sollen genau 3 gemeinsame Punkte haben. Wie groß ist der Radius in cm?',
          str(einzig(rr)), 'Die Parallelen sind 2 cm und 4 cm von M entfernt. Bei r = 4 cm schneidet der Kreis die nahe zweimal und berührt die ferne einmal: 3 Punkte.',
          'Eine Parallele muss Tangente sein, die andere Sekante.', einheit='cm'),
        Z(3, 'Ein Baum steht 4 m von einem geraden Zaun entfernt. Eine Bank soll genau 3 m vom Baum und genau 1 m vom Zaun entfernt stehen. Wie viele Plätze gibt es?',
          str(_schnitt(4 - 1, 3) + _schnitt(4 + 1, 3)), 'Die Linie 1 m vor dem Zaun (Baumseite) ist 3 m vom Baum entfernt: Sie berührt den Kreis einmal. Hinter dem Zaun wären es 5 m: kein Punkt. Genau 1 Platz.',
          'Zeichne den Kreis um den Baum und die beiden Linien 1 m neben dem Zaun.'),
    ]
    N['sachsituationen'] = [
        Z(2, 'Ein Rasensprenger reicht 6 m weit in jede Richtung. Wie breit ist die nasse Fläche an der breitesten Stelle?', '2 * 6', 'Die breiteste Stelle ist der Durchmesser: 2 · 6 m = 12 m.',
          'Die nasse Fläche ist ein Kreis.', einheit='m'),
        Z(2, 'Ein Spielplatz muss mindestens 20 m von einer geraden Straße entfernt sein. Ein Grundstück reicht von der Straße 35 m nach hinten. Wie tief ist der erlaubte Bereich?',
          '35 - 20', 'Die ersten 20 m sind gesperrt. Erlaubt: 35 m − 20 m = 15 m.', 'Zeichne die Straße und die Parallele im Abstand 20 m.', einheit='m'),
        Z(3, 'Zwei Rasensprenger stehen 10 m auseinander, jeder reicht 7 m weit. Wie lang ist auf der Verbindungslinie das Stück, das von beiden bewässert wird?', '7 + 7 - 10',
          'Der erste reicht bis 7 m, der zweite ab 10 m − 7 m = 3 m. Doppelt nass von 3 m bis 7 m: 4 m.', 'Zeichne eine Linie von 10 m und markiere, wie weit jeder Sprenger reicht.', einheit='m'),
        Z(3, 'Ein Schatz liegt genau 4 m von einem geraden Bach und genau 5 m von einer Eiche entfernt. Die Eiche steht 2 m vom Bach entfernt. Wie viele mögliche Orte gibt es?',
          str(_schnitt(4 - 2, 5) + _schnitt(4 + 2, 5)), 'Die Linie 4 m vom Bach auf der Eichenseite ist 2 m von der Eiche entfernt: 2 Schnittpunkte. Die andere ist 6 m entfernt: keiner. Zusammen 2.',
          'Zeichne die beiden Linien im Abstand 4 m vom Bach und den Kreis um die Eiche.'),
        Z(3, 'Ein Sender reicht 30 km weit. Wie weit darf eine gerade Autobahn höchstens vom Sender entfernt verlaufen, damit sie noch an mindestens einer Stelle Empfang hat?', '30',
          'Ist die Autobahn genau 30 km entfernt, berührt sie den Empfangskreis in einem Punkt. Weiter weg gibt es keinen Empfang. Also höchstens 30 km.',
          'Wann ist die Autobahn eine Tangente an den Empfangskreis?', einheit='km'),
        A(3, 'Ein Hund hat eine 5 m lange Leine. Der Pflock steht 3 m vor einem Zaun. Jemand sagt: „Der Hund erreicht den Zaun nicht, weil 5 m mehr ist als 3 m.“ Stimmt das?',
          'Nein: Gerade weil die Leine länger als 3 m ist, erreicht er den Zaun.', ['Ja, das stimmt.', 'Nein, er erreicht den Zaun nur bei 8 m Leine.', 'Nein, nur wenn die Leine genau 3 m lang ist.'],
          'Der Zaun ist 3 m vom Pflock entfernt, die Leine 5 m lang. 3 m < 5 m: Der Zaun liegt in Reichweite.', 'Vergleiche den Abstand zum Zaun mit der Leinenlänge.'),
    ]
    N['verstehen'] = [
        wahl(2, 'Stimmt die Aussage? „Alle Punkte mit höchstens 3 cm Abstand von M bilden eine Kreisfläche.“', ['Ja: die Kreislinie mit r = 3 cm und alles darin.', 'Nein: nur eine Kreislinie.', 'Nein: einen Streifen.'],
             lambda o: o.startswith('Ja'), '„Höchstens“ heißt: 3 cm oder weniger. Dazu gehören die Kreislinie und das ganze Innere.', 'Achte auf das Wort „höchstens“.'),
        wahl(2, 'Stimmt die Aussage? „Die Punkte mit genau 2 cm Abstand von g bilden einen Streifen.“', ['Nein: Sie bilden zwei Parallelen. Der Streifen gehört zu „höchstens 2 cm“.', 'Ja, einen Streifen der Breite 4 cm.', 'Ja, einen Streifen der Breite 2 cm.'],
             lambda o: o.startswith('Nein'), '„Genau 2 cm“ ergibt nur die zwei Randlinien. Alle Punkte dazwischen sind näher als 2 cm.', 'Was ist der Unterschied zwischen „genau“ und „höchstens“?'),
        wahl(3, 'g und h sind parallel. Welche Ortslinie besteht aus allen Punkten, die von g und h gleich weit entfernt sind?', ['die Mittelparallele', 'ein Kreis', 'ein Streifen', 'zwei Parallelen außerhalb'],
             lambda o: o == 'die Mittelparallele', 'Alle diese Punkte liegen auf der Parallelen genau in der Mitte zwischen g und h.', 'Zeichne g und h und markiere einige Punkte mit gleichem Abstand.'),
        Z(3, 'Wie viele Punkte haben von M den Abstand 3 cm und gleichzeitig von M den Abstand 5 cm?', '0',
          'Ein Punkt hat nur einen Abstand zu M. Er kann nicht gleichzeitig 3 cm und 5 cm entfernt sein: Die beiden Kreise um M haben keinen gemeinsamen Punkt.',
          'Zeichne die beiden Kreise um M. Schneiden sie sich?'),
        wahl(3, 'Stimmt die Aussage? „Die Punkte mit mindestens 2 cm und höchstens 4 cm Abstand von M bilden einen Ring.“', ['Ja: zwischen dem Kreis mit r = 2 cm und dem mit r = 4 cm.', 'Nein: eine Kreisfläche mit r = 4 cm.', 'Nein: zwei Kreislinien.', 'Nein: einen Streifen.'],
             lambda o: o.startswith('Ja'), '„Mindestens 2 cm“ schneidet die innere Kreisfläche heraus, „höchstens 4 cm“ begrenzt nach außen: Es bleibt ein Ring.',
             'Male erst „höchstens 4 cm“ aus und radiere dann „weniger als 2 cm“ weg.'),
        wahl(3, 'Stimmt die Aussage? „Ein Kreis kann eine Gerade in drei Punkten schneiden.“', ['Nein: höchstens in zwei Punkten.', 'Ja, wenn der Kreis groß ist.', 'Ja, wenn die Gerade durch M geht.'],
             lambda o: o.startswith('Nein'), 'Sekante: 2 Punkte, Tangente: 1, Passante: 0. Mehr gibt es nicht – auch nicht durch M.', 'Zeichne einen Kreis und probiere verschiedene Geraden.'),
    ]
    return N


ergaenze(DATEI, _schwer(), 1073)

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('geometrie.ortslinien', 13_5_8)
_hs = 'Zeichne zwei Kreise und zähle die gemeinsamen Punkte.'
# c) viermal dieselbe Sender-Aufgabe, jedes Mal Antwort 2 → zwei davon mit Antwort 0 bzw. 1
BF.ersetze('sachsituationen', 'Zwei Sender A und B stehen 7 km auseinander. Ein Handy hat genau 8 km Abstand zu A und genau 4 km Abstand zu B. An wie vielen Stellen kann es sein?', BF.Z(
    'Zwei Sender A und B stehen 7 km auseinander. Ein Handy hat genau 2 km Abstand zu A und genau 4 km Abstand zu B. An wie vielen Stellen kann es sein?', 0, '0',
    'Kreise mit 2 km und 4 km um A und B. 2 + 4 = 6 km ist weniger als der Abstand 7 km: Die Kreise treffen sich nicht, 0 Stellen.', _hs))
BF.ersetze('sachsituationen', 'Zwei Sender A und B stehen 10 km auseinander. Ein Handy hat genau 5 km Abstand zu A und genau 6 km Abstand zu B. An wie vielen Stellen kann es sein?', BF.Z(
    'Zwei Sender A und B stehen 10 km auseinander. Ein Handy hat genau 4 km Abstand zu A und genau 6 km Abstand zu B. An wie vielen Stellen kann es sein?', 1, '1',
    'Kreise mit 4 km und 6 km um A und B. 4 + 6 = 10 km ist genau der Abstand: Die Kreise berühren sich auf der Strecke [AB], 1 Stelle.', _hs))
# c) Beinahe-Dublette (zweimal „höchstens Abstand 3“, Ergebnis 7)
BF.ersetze('parallelen', 'g ist die waagrechte Gerade y = −1. Wie viele Punkte mit ganzzahligen Koordinaten auf der senkrechten Linie x = 2 haben von g höchstens den Abstand 3?', BF.Z(
    'g ist die waagrechte Gerade y = −1. Wie viele Punkte mit ganzzahligen Koordinaten auf der senkrechten Linie x = 2 haben von g mehr als 1, aber höchstens 3 Abstand?', 4, '2 * 2',
    'Abstand 2 oder 3: oberhalb y = 1 und y = 2, unterhalb y = −3 und y = −4. Das sind 4 Punkte.', 'Zähle oberhalb und unterhalb von g getrennt; der Abstand 1 gehört nicht dazu.'))
# d) Lage „Kreis im Kreis“ wird in der Lernkarte nicht erklärt (nur sich schneidende/berührende Kreise) → Aufgaben zur erklärten Regel
_hk = 'Vergleiche [AB] mit der Summe der Radien.'
BF.ersetze('zwei_kreise', 'Kreis um A mit r = 2 cm, Kreis um B mit r = 9 cm, [AB] = 6 cm. Wie viele Schnittpunkte haben die Kreise?', BF.A(
    'Kreis um A mit r = 2 cm, Kreis um B mit r = 3 cm, [AB] = 7 cm. Wie viele Schnittpunkte haben die Kreise?', 'keinen', ['unendlich viele', 'einen', 'zwei'],
    '2 + 3 = 5 cm ist weniger als [AB] = 7 cm: Die Kreise erreichen sich nicht, kein Schnittpunkt.', _hk))
BF.ersetze('zwei_kreise', 'Ein großer Kreis um A hat r = 9 cm, ein kleiner Kreis um B hat r = 4 cm. B liegt im großen Kreis, [AB] = 5 cm. Wie viele gemeinsame Punkte haben die Kreise?', BF.Z(
    'Ein Kreis um A hat r = 6 cm, ein Kreis um B hat r = 4 cm, [AB] = 10 cm. Wie viele gemeinsame Punkte haben die Kreise?', 1, '1',
    '6 + 4 = 10 = [AB]: Die Kreise berühren sich auf der Strecke [AB] – genau 1 Punkt.', _hk))
BF.ersetze('zwei_kreise', 'Kreis um A mit r = 4 cm, Kreis um B mit r = 8 cm, [AB] = 4 cm. Wie viele Schnittpunkte haben die Kreise?', BF.A(
    'Kreis um A mit r = 5 cm, Kreis um B mit r = 4 cm, [AB] = 7 cm. Wie viele Schnittpunkte haben die Kreise?', 'zwei', ['unendlich viele', 'einen', 'keinen'],
    '5 + 4 = 9 cm ist mehr als [AB] = 7 cm: Die Kreise überlappen und schneiden sich oberhalb und unterhalb von AB – zwei Schnittpunkte.', _hk))
BF.ersetze('zwei_kreise', 'Ein großer Kreis um A hat r = 8 cm, ein kleiner Kreis um B hat r = 3 cm. B liegt im großen Kreis, [AB] = 5 cm. Wie viele gemeinsame Punkte haben die Kreise?', BF.Z(
    'Ein Kreis um A hat r = 3 cm, ein Kreis um B hat ebenfalls r = 3 cm, [AB] = 7 cm. Wie viele gemeinsame Punkte haben die Kreise?', 0, '0',
    '3 + 3 = 6 cm ist weniger als [AB] = 7 cm: Zwischen den Kreisen bleibt eine Lücke von 1 cm, kein gemeinsamer Punkt.', _hk))
BF.ersetze('zwei_kreise', 'Jemand sagt: „Kreise mit r = 3 cm und r = 5 cm, deren Mittelpunkte 1 cm auseinander liegen, schneiden sich, weil 1 cm < 3 cm + 5 cm.“ Stimmt das?', BF.A(
    'Jemand sagt: „Kreise mit r = 3 cm und r = 5 cm, deren Mittelpunkte 9 cm auseinander liegen, schneiden sich, weil 9 cm > 5 cm.“ Stimmt das?',
    'Nein: 3 cm + 5 cm = 8 cm ist weniger als 9 cm, die Kreise treffen sich nicht.',
    ['Ja, das stimmt.', 'Ja, in vier Punkten.', 'Nein, sie berühren sich in einem Punkt.'],
    'Entscheidend ist die Summe der Radien: 3 + 5 = 8 cm. Der Abstand 9 cm ist größer, also bleibt 1 cm Lücke – kein gemeinsamer Punkt.',
    'Zeichne beide Kreise: Wie weit reichen sie zusammen?'))
BF.fuer_sebastian('geometrie.ortslinien/zwei_kreise: Die Lernkarte erklärt nur sich schneidende/berührende Kreise; „Kreis im Kreis“ (r₁ − r₂) ist aus den älteren Übungen genommen; die Aufgabe „Welcher Abstand [AB] ist möglich?“ (Runde 10) nutzt die Grenze r₁ − r₂ noch (im Lösungsweg erklärt). Soll die Lernkarte das ergänzen? Außerdem: lehrplan_gym leer, Ortslinien stehen im LehrplanPLUS Gym erst in Jgst. 7 (laut D2 inzwischen Kairo/Kl. 7). Karten-Text nicht geändert.')

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    schreibe(DATEI)
