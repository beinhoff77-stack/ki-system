#!/usr/bin/env python3
"""Thema raum.schraegbilder – Schrägbilder und Raumdarstellung (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, Z, baue, cz, zt  # noqa: E402

META = {'thema_schluessel': 'raum.schraegbilder', 'thema_id': 91, 'block_id': 109, 'klasse': {'gym_by': 8, 'rs_by': 5}}

ETAPPEN = [
    {'lernziel': 'pyramide', 'titel': 'Pyramiden: Ecken, Kanten, Flächen',
     'regel': 'Eine ⟦Pyramide⟧ hat ein n-Eck als Grundfläche und eine ⟦Spitze⟧. Sie hat n + 1 Ecken, ⟦2n Kanten⟧ (n unten, n zur Spitze) und n + 1 Flächen (n Dreiecke + Grundfläche).',
     'schritte': ['Sechsseitige Pyramide: n = 6', 'Ecken: 6 + 1 = 7, Kanten: 2 · 6 = 12', 'Flächen: 6 Dreiecke + 1 Sechseck = ⟦7⟧'],
     'probe': 'E + F − K = 7 + 7 − 12 = 2 ✓',
     'fehler': 'Eine vierseitige Pyramide hat nicht 4 Flächen: Zu den 4 Dreiecken kommt die ⟦quadratische Grundfläche⟧ dazu, also 5.',
     '_verbot': ['Sechsseitige Pyramide']},
    {'lernziel': 'laengen', 'titel': 'Schrägbilder von Prismen und Pyramiden',
     'regel': 'Schrägbild: Strecken ⟦parallel zur Zeichenebene⟧ (Breite, Höhe) in wahrer Länge; Strecken ⟦nach hinten⟧ unter dem Winkel ω (meist 45°) mit dem ⟦Verkürzungsfaktor q⟧ (meist 1/2). Die Höhe einer Pyramide zeichnest du senkrecht in wahrer Länge über dem Fußpunkt.',
     'schritte': ['Quadratische Pyramide: Grundkante 6 cm, Höhe 8 cm, q = 1/2', 'Vorderkante 6 cm, Kante nach hinten 6 · 1/2 = 3 cm', 'Höhe: ⟦8 cm⟧ senkrecht über dem Diagonalenschnittpunkt'],
     'fehler': 'Die Höhe einer Pyramide wird nicht verkürzt: Sie steht ⟦senkrecht⟧ und liegt damit parallel zur Zeichenebene.',
     '_verbot': ['Grundkante 6 cm, Höhe 8 cm']},
    {'lernziel': 'lage', 'titel': 'Parallel, schneidend oder windschief?',
     'regel': 'Zwei Geraden im Raum sind ⟦parallel⟧ (gleiche Richtung), ⟦schneiden sich⟧ (ein gemeinsamer Punkt) oder sind ⟦windschief⟧: nicht parallel und ohne gemeinsamen Punkt. Windschiefe Geraden liegen in keiner gemeinsamen Ebene.',
     'schritte': ['Quader ABCDEFGH (ABCD unten, E über A, F über B, …)', 'AB verläuft unten vorne nach rechts, CG senkrecht hinten rechts.', 'Nicht parallel und kein gemeinsamer Punkt: ⟦windschief⟧'],
     'fehler': 'Geraden ohne Schnittpunkt sind im Raum nicht automatisch parallel. Parallel heißt ⟦gleiche Richtung⟧ – sonst sind sie windschief.'},
    {'lernziel': 'rotation', 'titel': 'Rotationskörper',
     'regel': 'Dreht man eine ebene Figur um eine ⟦Achse⟧, entsteht ein ⟦Rotationskörper⟧. Rechteck um eine Seite → ⟦Zylinder⟧; rechtwinkliges Dreieck um eine Kathete → ⟦Kegel⟧; Halbkreis um den Durchmesser → ⟦Kugel⟧.',
     'schritte': ['Rechteck 4 cm × 7 cm dreht sich um die 7-cm-Seite.', 'Die Achse ist 7 cm lang: Höhe 7 cm.', 'Die andere Seite wird zum Radius: ⟦Zylinder mit r = 4 cm, h = 7 cm⟧'],
     'fehler': 'Dreht sich das Rechteck 4 cm × 7 cm um die 7-cm-Seite, ist der Radius nicht 7 cm. Die Seite ⟦auf der Achse⟧ wird zur Höhe, die andere zum Radius.',
     '_verbot': ['4 cm × 7 cm']},
    {'lernziel': 'axialschnitt', 'titel': 'Axialschnitte berechnen',
     'regel': 'Ein ⟦Axialschnitt⟧ schneidet einen Rotationskörper ⟦entlang der Achse⟧. Beim Zylinder entsteht ein Rechteck (2r breit, h hoch), beim Kegel ein gleichschenkliges Dreieck (Grundseite 2r, Höhe h), bei der Kugel ein Kreis.',
     'schritte': ['Zylinder r = 3 cm, h = 10 cm', 'Axialschnitt: Rechteck 6 cm × 10 cm', 'Flächeninhalt: ⟦60 cm²⟧'],
     'fehler': 'Der Axialschnitt eines Zylinders ist nicht r breit, sondern ⟦2r⟧: Der Schnitt geht durch die Mitte und erfasst den ganzen Durchmesser.',
     '_verbot': ['r = 3 cm, h = 10 cm']},
    {'lernziel': 'koordinaten', 'titel': 'Punkte im Raum mit Koordinaten',
     'regel': 'Im Raum hat ein Punkt ⟦drei Koordinaten⟧ P(x | y | z). Liegt ein Quader mit A im ⟦Ursprung⟧ so, dass AB auf der x-Achse, AD auf der y-Achse und AE auf der z-Achse (nach oben) liegt, liest du die Koordinaten aus den ⟦Kantenlängen⟧ ab.',
     'schritte': ['Quader: A(0 | 0 | 0), Länge 5 in x-, Breite 3 in y-, Höhe 2 in z-Richtung', 'B(5 | 0 | 0), C(5 | 3 | 0), E(0 | 0 | 2)', 'G liegt über C: ⟦G(5 | 3 | 2)⟧'],
     'fehler': 'H liegt nicht bei (0 | 0 | 2) – das ist E. H liegt über D, also H(0 | 3 | 2). Achte darauf, ⟦welche Ecke über welcher⟧ liegt.',
     '_verbot': ['Länge 5 in x-, Breite 3 in y-, Höhe 2 in z']},
]

N_ECK = {3: 'dreiseitige', 4: 'vierseitige', 5: 'fünfseitige', 6: 'sechsseitige', 7: 'siebenseitige', 8: 'achtseitige', 10: 'zehnseitige', 12: 'zwölfseitige'}


def g_pyramide(R, st):
    n = R.choice(list(N_ECK))
    if st == 1:
        was, f, c = R.choice([('Ecken', n + 1, f'{n} + 1'), ('Kanten', 2 * n, f'2 * {n}'), ('Flächen', n + 1, f'{n} + 1')])
        return Z(f'Wie viele {was} hat eine {N_ECK[n]} Pyramide?', f, c,
                 {'Ecken': f'{n} Ecken unten + 1 Spitze = {n + 1}', 'Kanten': f'{n} Grundkanten + {n} Seitenkanten = {2 * n}',
                  'Flächen': f'{n} Dreiecke + 1 Grundfläche = {n + 1}'}[was] + '.', 'Zähle Grundfläche und Spitze getrennt.')
    if st == 2:
        was, wert = R.choice([('Kanten', 2 * n), ('Ecken', n + 1), ('Flächen', n + 1)])
        return Z(f'Eine Pyramide hat {wert} {was}. Wie viele Ecken hat ihre Grundfläche?', n, {'Kanten': f'{wert} / 2', 'Ecken': f'{wert} - 1', 'Flächen': f'{wert} - 1'}[was],
                 {'Kanten': f'2n = {wert} → n = {n}', 'Ecken': f'n + 1 = {wert} → n = {n}', 'Flächen': f'n + 1 = {wert} → n = {n}'}[was] + '.',
                 'Kanten 2n, Ecken n + 1, Flächen n + 1.')
    a, s = R.randint(2, 12), R.randint(5, 20)
    if R.random() < .5:
        return Z(f'Eine {N_ECK[n]} Pyramide hat als Grundfläche ein regelmäßiges {n}-Eck mit Seitenlänge {a} cm, jede Seitenkante ist {s} cm lang. Wie lang sind alle Kanten zusammen?',
                 n * a + n * s, f'{n} * {a} + {n} * {s}', f'{n} Grundkanten: {n * a} cm, {n} Seitenkanten: {n * s} cm. Zusammen {n * (a + s)} cm.',
                 'Grundkanten und Seitenkanten getrennt zählen.', einheit='cm')
    m = R.choice([k for k in N_ECK if k != n])
    return Z(f'Ein {N_ECK[n][:-1]}s Prisma und eine {N_ECK[m]} Pyramide werden verglichen. Wie viele Kanten haben beide zusammen?', 3 * n + 2 * m, f'3 * {n} + 2 * {m}',
             f'Prisma: 3 · {n} = {3 * n} Kanten. Pyramide: 2 · {m} = {2 * m} Kanten. Zusammen {3 * n + 2 * m}.', 'Prisma 3n Kanten, Pyramide 2n Kanten.')


def g_laengen(R, st):
    q = Fr(1, 2) if st < 3 else R.choice([Fr(1, 2), Fr(1, 3), Fr(2, 3)])
    qt = {Fr(1, 2): '1/2', Fr(1, 3): '1/3', Fr(2, 3): '2/3'}[q]
    if st == 1:
        a, h = R.randint(2, 12) * 2, R.randint(3, 15)
        w = R.choice(['vorne', 'hinten', 'hoch'])
        if w == 'vorne':
            return Z(f'Eine quadratische Pyramide (Grundkante {a} cm, Höhe {h} cm) wird im Schrägbild mit q = 1/2 gezeichnet. Wie lang zeichnest du die vordere Grundkante?', a, f'{a}',
                     f'Die vordere Kante liegt parallel zur Zeichenebene: wahre Länge {a} cm.', 'Parallel zur Zeichenebene: wahre Länge.', einheit='cm')
        if w == 'hinten':
            return Z(f'Eine quadratische Pyramide (Grundkante {a} cm, Höhe {h} cm) wird im Schrägbild mit q = 1/2 gezeichnet. Wie lang zeichnest du eine Grundkante, die nach hinten führt?', Fr(a, 2), f'{a} / 2',
                     f'Nach hinten: {a} · 1/2 = {zt(Fr(a, 2))} cm.', 'Nach hinten: mit q multiplizieren.', einheit='cm')
        return Z(f'Eine quadratische Pyramide (Grundkante {a} cm, Höhe {h} cm) wird im Schrägbild mit q = 1/2 gezeichnet. Wie lang zeichnest du die Höhe?', h, f'{h}',
                 f'Die Höhe steht senkrecht, also parallel zur Zeichenebene: {h} cm.', 'Senkrechte Strecken werden nicht verkürzt.', einheit='cm')
    if st == 2:
        b, t, h = R.randint(2, 15), R.randint(2, 20), R.randint(2, 15)
        frage = R.choice(['tiefe', 'summe'])
        if frage == 'tiefe':
            return Z(f'Im Schrägbild (q = 1/2, ω = 45°) eines Prismas ist die nach hinten laufende Kante {zt(Fr(t, 2))} cm lang. Wie tief ist das Prisma wirklich?', t, f'{cz(Fr(t, 2))} * 2',
                     f'wahr = gezeichnet : q = {zt(Fr(t, 2))} : 1/2 = {t} cm.', 'Rechne rückwärts: durch q teilen.', einheit='cm')
        return Z(f'Ein Quader ist {b} cm breit, {h} cm hoch und {t} cm tief. Im Schrägbild (q = 1/2) zeichnest du alle 12 Kanten. Wie lang sind die gezeichneten Kanten zusammen?',
                 4 * b + 4 * h + 4 * Fr(t, 2), f'4 * {b} + 4 * {h} + 4 * {t} / 2',
                 f'4 Breiten ({4 * b} cm) und 4 Höhen ({4 * h} cm) in wahrer Länge, 4 Tiefen zu {zt(Fr(t, 2))} cm ({2 * t} cm). Zusammen {zt(4 * b + 4 * h + 2 * t)} cm.',
                 'Nur die 4 Kanten nach hinten werden verkürzt.', einheit='cm')
    if R.random() < .6:
        t = R.randint(1, 8) * q.denominator
        return Z(f'Eine Kante führt {t} cm nach hinten. Wie lang wird sie im Schrägbild mit q = {qt} gezeichnet?', t * q, f'{t} * {cz(q)}',
                 f'{t} · {qt} = {zt(t * q)} cm.', 'Multipliziere die wahre Länge mit q.', einheit='cm')
    opts = ['die Höhe der Pyramide', 'eine Seitenkante der Pyramide', 'die Grundkante, die nach hinten führt', 'eine Diagonale der Grundfläche']
    return A(R, f'Eine quadratische Pyramide wird im Schrägbild (q = {qt}, ω = 45°) gezeichnet, eine Grundkante liegt vorne parallel zur Zeichenebene. Welche Strecke erscheint sicher in wahrer Länge?',
             opts[0], opts[1:], 'Die Höhe steht senkrecht und liegt parallel zur Zeichenebene. Seitenkanten, Kanten nach hinten und Diagonalen der Grundfläche haben einen Anteil nach hinten und werden verzerrt.',
             'Welche Strecke liegt parallel zur Zeichenebene?')


ECKE = {'A': (0, 0, 0), 'B': (1, 0, 0), 'C': (1, 1, 0), 'D': (0, 1, 0), 'E': (0, 0, 1), 'F': (1, 0, 1), 'G': (1, 1, 1), 'H': (0, 1, 1)}
KANTEN = ['AB', 'BC', 'CD', 'DA', 'EF', 'FG', 'GH', 'HE', 'AE', 'BF', 'CG', 'DH']
DIAG = ['AC', 'BD', 'EG', 'FH', 'AF', 'BE', 'CH', 'DG', 'AH', 'DE', 'BG', 'CF', 'AG', 'CE', 'BH', 'DF']


def lage_von(g, h, mass):
    P = [ECKE[g[0]][i] * mass[i] for i in range(3)]; P2 = [ECKE[g[1]][i] * mass[i] for i in range(3)]
    Q = [ECKE[h[0]][i] * mass[i] for i in range(3)]; Q2 = [ECKE[h[1]][i] * mass[i] for i in range(3)]
    u = [P2[i] - P[i] for i in range(3)]; v = [Q2[i] - Q[i] for i in range(3)]
    kreuz = [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]
    if kreuz == [0, 0, 0]:
        w = [Q[i] - P[i] for i in range(3)]
        k2 = [u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0]]
        return 'identisch' if k2 == [0, 0, 0] else 'parallel'
    w = [Q[i] - P[i] for i in range(3)]
    spat = sum(w[i] * kreuz[i] for i in range(3))
    return 'schneiden sich' if spat == 0 else 'windschief'


LAGEN = ['parallel', 'schneiden sich', 'windschief']


def g_lage(R, st):
    mass = (R.randint(3, 9), R.randint(2, 7), R.randint(2, 8))
    pool = KANTEN if st < 3 else KANTEN + DIAG
    while True:
        g, h = R.sample(pool, 2)
        if st == 3 and g in KANTEN and h in KANTEN: continue
        l = lage_von(g, h, mass)
        if l != 'identisch': break
    return A(R, f'Quader ABCDEFGH (ABCD Grundfläche, E über A, F über B, G über C, H über D). Wie liegen die Geraden {g} und {h} zueinander?', l, [x for x in LAGEN if x != l] + ['identisch'],
             {'parallel': f'{g} und {h} haben dieselbe Richtung, aber keinen gemeinsamen Punkt.',
              'schneiden sich': f'{g} und {h} haben einen gemeinsamen Punkt' + (f' ({"".join(sorted(set(g) & set(h)))})' if set(g) & set(h) else ' im Inneren einer Fläche oder des Quaders') + '.',
              'windschief': f'{g} und {h} sind nicht parallel und treffen sich nirgends: Sie liegen in keiner gemeinsamen Ebene.'}[l],
             'Stell dir den Quader vor (z. B. eine Schachtel). Haben die Geraden dieselbe Richtung? Gibt es einen gemeinsamen Punkt?')


def g_rotation(R, st):
    if st == 1:
        fig = R.choice([('ein Rechteck', 'um eine seiner Seiten', 'Zylinder'), ('ein rechtwinkliges Dreieck', 'um eine Kathete', 'Kegel'),
                        ('ein Halbkreis', 'um seinen Durchmesser', 'Kugel'), ('ein Quadrat', 'um eine seiner Seiten', 'Zylinder')])
        r = fig[2]
        return A(R, f'Welcher Körper entsteht, wenn sich {fig[0]} {fig[1]} dreht?', r, [k for k in ['Zylinder', 'Kegel', 'Kugel', 'Pyramide'] if k != r],
                 f'{fig[0][0].upper() + fig[0][1:]} {fig[1]} gedreht ergibt einen {r}.', 'Stell dir vor, die Figur ist eine Fahne, die sich schnell um die Achse dreht.')
    if st == 2:
        a, b = R.sample(range(2, 15), 2)
        if R.random() < .5:
            return Z(f'Ein Rechteck mit den Seiten {a} cm und {b} cm dreht sich um die {a}-cm-Seite. Wie groß ist der Radius des entstehenden Zylinders?', b, f'{b}',
                     f'Die {a}-cm-Seite liegt auf der Achse und wird zur Höhe. Die {b}-cm-Seite steht senkrecht dazu und wird zum Radius: r = {b} cm.',
                     'Welche Seite liegt auf der Achse? Die andere wird zum Radius.', einheit='cm')
        return Z(f'Ein rechtwinkliges Dreieck mit den Katheten {a} cm und {b} cm dreht sich um die {a}-cm-Kathete. Wie hoch ist der entstehende Kegel?', a, f'{a}',
                 f'Die Kathete auf der Achse ({a} cm) wird zur Höhe, die andere ({b} cm) zum Radius.', 'Die Seite auf der Drehachse wird zur Höhe.', einheit='cm')
    a, b = R.sample(range(2, 15), 2)
    if R.random() < .5:
        return Z(f'Ein Rechteck {a} cm × {b} cm dreht sich einmal um die {a}-cm-Seite, einmal um die {b}-cm-Seite. Um wie viel cm unterscheiden sich die Durchmesser der beiden Zylinder?',
                 2 * abs(a - b), f'2 * abs({a} - {b})', f'Durchmesser 2 · {b} = {2 * b} cm bzw. 2 · {a} = {2 * a} cm. Unterschied {2 * abs(a - b)} cm.',
                 'Der Radius ist jeweils die andere Seite, der Durchmesser das Doppelte.', einheit='cm')
    d = 2 * a
    return Z(f'Ein Halbkreis mit dem Durchmesser {d} cm dreht sich um seinen Durchmesser. Welchen Radius hat die entstehende Kugel?', a, f'{d} / 2',
             f'Der Durchmesser liegt auf der Achse, die Kugel hat denselben Durchmesser {d} cm, also r = {a} cm.', 'Der Halbkreis-Durchmesser wird zum Kugel-Durchmesser.', einheit='cm')


def g_axialschnitt(R, st):
    r, h = R.randint(2, 12), R.randint(2, 20)
    if st == 1:
        k = R.choice(['zyl', 'kegel', 'kugel'])
        form = {'zyl': 'ein Rechteck', 'kegel': 'ein gleichschenkliges Dreieck', 'kugel': 'ein Kreis'}[k]
        name = {'zyl': 'eines Zylinders', 'kegel': 'eines geraden Kegels', 'kugel': 'einer Kugel'}[k]
        akk = {'zyl': 'einen Zylinder', 'kegel': 'einen geraden Kegel', 'kugel': 'eine Kugel'}[k]
        if R.random() < .5:
            return A(R, f'Welche Figur ist der Axialschnitt {name} (r = {r} cm{", h = " + str(h) + " cm" if k != "kugel" else ""})?', form,
                     [f for f in ['ein Rechteck', 'ein gleichschenkliges Dreieck', 'ein Kreis', 'ein Trapez'] if f != form],
                     f'Schneidet man {akk} längs der Achse, entsteht {form}.', 'Stell dir vor, du schneidest den Körper genau durch die Mitte von oben nach unten.')
        return Z(f'Ein Zylinder hat r = {r} cm und h = {h} cm. Wie breit ist sein Axialschnitt?', 2 * r, f'2 * {r}',
                 f'Der Axialschnitt ist ein Rechteck mit der Breite 2r = {2 * r} cm (und Höhe {h} cm).', 'Der Schnitt geht durch die Mitte: ganzer Durchmesser.', einheit='cm')
    if st == 2:
        if R.random() < .5:
            return Z(f'Ein Zylinder hat r = {r} cm und h = {h} cm. Wie groß ist der Flächeninhalt seines Axialschnitts?', 2 * r * h, f'2 * {r} * {h}',
                     f'Rechteck {2 * r} cm × {h} cm: A = {2 * r * h} cm².', 'Rechteck: Breite 2r, Höhe h.', einheit='cm²')
        return Z(f'Ein gerader Kegel hat r = {r} cm und h = {h} cm. Wie groß ist der Flächeninhalt seines Axialschnitts?', r * h, f'2 * {r} * {h} / 2',
                 f'Dreieck mit Grundseite {2 * r} cm und Höhe {h} cm: A = {2 * r} · {h} : 2 = {r * h} cm².', 'Dreieck: Grundseite 2r, Höhe h.', einheit='cm²')
    if R.random() < .5:
        A_ = 2 * r * h
        return Z(f'Der Axialschnitt eines Zylinders ist ein Rechteck mit {A_} cm² Flächeninhalt. Der Zylinder ist {h} cm hoch. Wie groß ist sein Radius?', r, f'{A_} / (2 * {h})',
                 f'2r · {h} = {A_} → 2r = {Fr(A_, h)} → r = {r} cm.', 'Rechteck: A = 2r · h. Stelle nach r um.', einheit='cm')
    return Z(f'Ein Zylinder hat r = {r} cm und h = {h} cm. Welchen Umfang hat sein Axialschnitt?', 2 * (2 * r + h), f'2 * (2 * {r} + {h})',
             f'Rechteck {2 * r} cm × {h} cm: u = 2 · ({2 * r} + {h}) = {2 * (2 * r + h)} cm.', 'Umfang eines Rechtecks: 2 · (Breite + Höhe).', einheit='cm')


def g_koordinaten(R, st):
    a, b, c = R.randint(2, 9), R.randint(2, 9), R.randint(2, 9)
    pts = {k: (v[0] * a, v[1] * b, v[2] * c) for k, v in ECKE.items()}
    intro = f'Ein Quader ABCDEFGH liegt so, dass A(0 | 0 | 0), B({a} | 0 | 0), D(0 | {b} | 0) und E(0 | 0 | {c}) sind.'
    if st == 1:
        p = R.choice(['C', 'F', 'G', 'H'])
        x, y, z = pts[p]
        r = f'{p}({x} | {y} | {z})'
        f = [f'{p}({y} | {x} | {z})', f'{p}({x} | {y} | 0)' if z else f'{p}({x} | {y} | {c})', f'{p}({x} | 0 | {z})' if y else f'{p}({x} | {b} | {z})']
        f = [t for t in f if t != r]
        if len(set(f)) < 2: f.append(f'{p}({x + 1} | {y} | {z})')
        return A(R, f'{intro} Welche Koordinaten hat {p}?', r, f, f'{p} liegt ' + {'C': 'unten, rechts hinten', 'F': 'über B', 'G': 'über C', 'H': 'über D'}[p] + f': {r}.',
                 'Überlege, über welcher Ecke der Grundfläche der Punkt liegt.')
    if st == 2:
        p = R.choice(['C', 'F', 'G', 'H'])
        i = R.randrange(3)
        return Z(f'{intro} Gib die {"xyz"[i]}-Koordinate von {p} an.', pts[p][i], f'{pts[p][i]}',
                 f'{p}({pts[p][0]} | {pts[p][1]} | {pts[p][2]}), also {"xyz"[i]} = {pts[p][i]}.', 'Bestimme erst alle drei Koordinaten des Punktes.')
    p1, p2 = R.choice([('A', 'G'), ('B', 'H'), ('C', 'E'), ('D', 'F'), ('A', 'C'), ('E', 'G'), ('B', 'G'), ('A', 'F')])
    i = R.randrange(3)
    m = Fr(pts[p1][i] + pts[p2][i], 2)
    return Z(f'{intro} M ist der Mittelpunkt der Strecke {p1}{p2}. Gib die {"xyz"[i]}-Koordinate von M an.', m, f'({pts[p1][i]} + {pts[p2][i]}) / 2',
             f'{p1}({pts[p1][0]} | {pts[p1][1]} | {pts[p1][2]}), {p2}({pts[p2][0]} | {pts[p2][1]} | {pts[p2][2]}). Mittelwert der {"xyz"[i]}-Koordinaten: ({pts[p1][i]} + {pts[p2][i]}) : 2 = {zt(m)}.',
             'Der Mittelpunkt hat in jeder Koordinate den Mittelwert der beiden Endpunkte.')


GEN = {'pyramide': g_pyramide, 'laengen': g_laengen, 'lage': g_lage, 'rotation': g_rotation, 'axialschnitt': g_axialschnitt, 'koordinaten': g_koordinaten}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Prismen und Pyramiden', ['pyramide', 'laengen']), ('Lage im Raum', ['lage', 'koordinaten']), ('Rotationskörper', ['rotation', 'axialschnitt'])],
         'Schrägbilder von Prismen und Pyramiden verstehen, Lagebeziehungen im Raum erkennen, Rotationskörper und Axialschnitte beschreiben und Punkte im Raum mit Koordinaten angeben.',
         ['Pyramide: n + 1 Ecken, 2n Kanten, n + 1 Flächen.', 'Schrägbild: parallel zur Zeichenebene wahr, nach hinten mit q verkürzt.',
          'Raum: parallel, schneidend oder windschief.', 'Rechteck → Zylinder, rechtwinkliges Dreieck → Kegel, Halbkreis → Kugel.'],
         offen=['Schrägbilder selbst zeichnen und ein 3D-Koordinatensystem mit Quader brauchen eine Zeichenfunktion in der App; nicht gebaut. '
                'Lernkarte „lage“ beschreibt den Quader deshalb nur in Worten (Beschriftung ABCDEFGH).',
                'Lernkarte „koordinaten“: Achsenrichtungen werden in der Lernkarte beschrieben; ein Bild des Quaders im Koordinatensystem wäre wichtig.'])
