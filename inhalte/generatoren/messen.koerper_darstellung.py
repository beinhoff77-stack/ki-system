#!/usr/bin/env python3
"""Thema messen.koerper_darstellung – Körper darstellen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, Z, baue, cz, zt  # noqa: E402

META = {'thema_schluessel': 'messen.koerper_darstellung', 'thema_id': 52, 'block_id': 86, 'klasse': {'gym_by': 8, 'rs_by': 5}}

ETAPPEN = [
    {'lernziel': 'prisma', 'titel': 'Prismen: Ecken, Kanten, Flächen',
     'regel': 'Ein ⟦Prisma⟧ hat zwei deckungsgleiche, parallele ⟦Grundflächen⟧ (n-Ecke) und n Rechtecke als ⟦Mantel⟧. Es hat 2n Ecken, 3n Kanten und n + 2 Flächen.',
     'schritte': ['Fünfseitiges Prisma: n = 5', 'Ecken: 2 · 5 = 10, Kanten: 3 · 5 = 15', 'Flächen: 5 + 2 = ⟦7⟧'],
     'probe': 'Eulerscher Polyedersatz: E + F − K = 10 + 7 − 15 = 2 ✓',
     'fehler': 'Ein dreiseitiges Prisma hat nicht 3 Flächen: Zu den 3 Rechtecken kommen die ⟦2 Grundflächen⟧ dazu, also 5.',
     '_verbot': ['Fünfseitiges Prisma']},
    {'lernziel': 'netz', 'titel': 'Netze von Prismen',
     'regel': 'Schneidet man ein Prisma an Kanten auf und klappt es in die Ebene, entsteht ein ⟦Netz⟧: 2 Grundflächen und n Rechtecke. Die Rechtecke sind so hoch wie das Prisma; zusammen sind sie so breit wie der ⟦Umfang der Grundfläche⟧.',
     'schritte': ['Quader 5 cm × 3 cm × 4 cm (Höhe 4 cm)', 'Grundflächen: 2 · 5 · 3 = 30 cm²; Mantel: (5 + 3 + 5 + 3) · 4 = 64 cm²', 'Fläche des Netzes = Oberfläche = ⟦94 cm²⟧'],
     'fehler': 'Die Netzfläche eines Quaders ist nicht 5 · 3 · 4 = 60. Das wäre das ⟦Volumen⟧. Für das Netz werden die Flächen der 6 Rechtecke ⟦addiert⟧.',
     '_verbot': ['5 cm × 3 cm × 4 cm']},
    {'lernziel': 'zylinder', 'titel': 'Zylinder und sein Netz',
     'regel': 'Ein ⟦Zylinder⟧ hat zwei Kreise als Grundflächen. Sein Mantel ist abgewickelt ein ⟦Rechteck⟧: so hoch wie der Zylinder und so lang wie der ⟦Umfang⟧ des Grundkreises.',
     'schritte': ['Zylinder: Kreisumfang u = 18,8 cm, Höhe h = 10 cm', 'Mantelrechteck: 18,8 cm lang, 10 cm hoch', 'Mantelfläche: 18,8 · 10 = ⟦188 cm²⟧'],
     'fehler': 'Das Mantelrechteck ist nicht so lang wie der ⟦Durchmesser⟧. Es muss einmal ganz um den Kreis herum reichen – also so lang wie der Umfang.',
     '_verbot': ['u = 18,8 cm']},
    {'lernziel': 'schraegbild', 'titel': 'Schrägbilder: Längen nach hinten',
     'regel': 'Im ⟦Schrägbild⟧ zeichnet man die Vorderfläche in ⟦wahrer Größe⟧. Kanten, die nach hinten gehen, zeichnet man unter dem ⟦Winkel 45°⟧ und ⟦verkürzt⟧, meist auf die Hälfte (Verkürzungsfaktor q = 1/2).',
     'schritte': ['Quader: 6 cm breit, 4 cm hoch, 8 cm tief', 'Breite und Höhe: wahre Größe (6 cm, 4 cm)', 'Tiefe: 8 cm · 1/2 = ⟦4 cm⟧ schräg nach hinten'],
     'fehler': 'Auch senkrechte Kanten werden nicht verkürzt: Nur die Kanten ⟦nach hinten⟧ werden mit q multipliziert.',
     '_verbot': ['8 cm tief']},
    {'lernziel': 'ansichten', 'titel': 'Ansichten von Körpern',
     'regel': 'Die ⟦Vorderansicht⟧ zeigt den Körper von vorn, die ⟦Seitenansicht⟧ von der Seite und die ⟦Draufsicht⟧ von oben. Jede Ansicht ist eine ebene Figur.',
     'schritte': ['Ein Zylinder steht auf seiner Grundfläche.', 'Von vorn und von der Seite: ⟦Rechteck⟧', 'Von oben: ⟦Kreis⟧'],
     'fehler': 'Die Draufsicht eines stehenden Zylinders ist kein Rechteck. Von oben sieht man nur die ⟦Deckfläche⟧, einen Kreis.'},
    {'lernziel': 'beurteilen', 'titel': 'Aussagen über Körper prüfen',
     'regel': 'Prüfe Aussagen mit den Eigenschaften: Ein Prisma braucht ⟦zwei deckungsgleiche parallele Grundflächen⟧ und Rechtecke als Seitenflächen. Pyramide, Kegel und Kugel sind ⟦keine⟧ Prismen.',
     'schritte': ['Aussage: „Ein Würfel ist ein Prisma.“', 'Grund- und Deckfläche sind gleich große Quadrate, die Seiten sind Rechtecke (Quadrate).', 'Die Aussage ist ⟦richtig⟧.'],
     'fehler': 'Eine Pyramide ist kein Prisma, obwohl sie eine Grundfläche hat: Ihr fehlt die ⟦zweite⟧, parallele Grundfläche.'},
]

N_ECK = {3: 'dreiseitiges', 4: 'vierseitiges', 5: 'fünfseitiges', 6: 'sechsseitiges', 7: 'siebenseitiges', 8: 'achtseitiges', 9: 'neunseitiges',
         10: 'zehnseitiges', 12: 'zwölfseitiges'}


def g_prisma(R, st):
    n = R.choice(list(N_ECK))
    if st == 1:
        was, f, c = R.choice([('Ecken', 2 * n, f'2 * {n}'), ('Kanten', 3 * n, f'3 * {n}'), ('Flächen', n + 2, f'{n} + 2')])
        return Z(f'Wie viele {was} hat ein {N_ECK[n]} Prisma?', f, c,
                 f'Grundfläche ist ein {n}-Eck. {was}: ' + {'Ecken': f'2 · {n} = {2 * n}', 'Kanten': f'3 · {n} = {3 * n} ({n} unten, {n} oben, {n} senkrecht)',
                                                           'Flächen': f'{n} Rechtecke + 2 Grundflächen = {n + 2}'}[was] + '.',
                 'Zähle oben, unten und dazwischen.')
    if st == 2:
        was, wert = R.choice([('Ecken', 2 * n), ('Kanten', 3 * n), ('Flächen', n + 2)])
        return Z(f'Ein Prisma hat {wert} {was}. Wie viele Ecken hat seine Grundfläche?', n,
                 {'Ecken': f'{wert} / 2', 'Kanten': f'{wert} / 3', 'Flächen': f'{wert} - 2'}[was],
                 {'Ecken': f'2n = {wert} → n = {n}', 'Kanten': f'3n = {wert} → n = {n}', 'Flächen': f'n + 2 = {wert} → n = {n}'}[was] + '. Die Grundfläche ist ein ' + str(n) + '-Eck.',
                 'Stelle eine Gleichung mit n auf (Ecken 2n, Kanten 3n, Flächen n + 2).')
    # Stufe 3: Gesamtkantenlänge regelmäßiger Prismen
    a, h = R.randint(2, 12), R.randint(3, 20)
    return Z(f'Ein gerades {N_ECK[n]} Prisma hat als Grundfläche ein regelmäßiges {n}-Eck mit Seitenlänge {a} cm und ist {h} cm hoch. Wie lang sind alle Kanten zusammen?',
             2 * n * a + n * h, f'2 * {n} * {a} + {n} * {h}', f'{2 * n} Grundkanten zu {a} cm: {2 * n * a} cm. {n} Seitenkanten zu {h} cm: {n * h} cm. Zusammen {2 * n * a + n * h} cm.',
             'Unterscheide Kanten der Grundflächen und senkrechte Kanten.', einheit='cm')


def g_netz(R, st):
    if st == 1:
        a, b, c = R.randint(2, 12), R.randint(2, 10), R.randint(2, 15)
        if R.random() < .5:
            return Z(f'Ein Quader ist {a} cm lang, {b} cm breit und {c} cm hoch. Wie groß ist die Fläche seines Netzes?', 2 * (a * b + a * c + b * c),
                     f'2 * ({a} * {b} + {a} * {c} + {b} * {c})', f'2 · ({a} · {b} + {a} · {c} + {b} · {c}) = 2 · {a * b + a * c + b * c} = {2 * (a * b + a * c + b * c)} cm².',
                     'Das Netz besteht aus 3 Paaren gleicher Rechtecke.', einheit='cm²')
        return Z(f'Ein Würfel hat die Kantenlänge {a} cm. Wie groß ist die Fläche seines Netzes?', 6 * a * a, f'6 * {a} * {a}',
                 f'6 Quadrate zu {a} · {a} = {a * a} cm²: 6 · {a * a} = {6 * a * a} cm².', 'Ein Würfelnetz besteht aus 6 gleichen Quadraten.', einheit='cm²')
    if st == 2:
        k = R.randint(1, 4); a, b, c = 3 * k, 4 * k, 5 * k
        h = R.randint(3, 15)
        if R.random() < .5:
            return Z(f'Ein Prisma hat als Grundfläche ein rechtwinkliges Dreieck mit den Seiten {a} cm, {b} cm und {c} cm (Katheten {a} cm und {b} cm). Es ist {h} cm hoch. Wie lang ist das Mantelrechteck im Netz insgesamt?',
                     a + b + c, f'{a} + {b} + {c}', f'Der Mantel ist so breit wie der Umfang der Grundfläche: {a} + {b} + {c} = {a + b + c} cm.',
                     'Der abgewickelte Mantel ist so lang wie der Umfang der Grundfläche.', einheit='cm')
        return Z(f'Ein Prisma hat als Grundfläche ein rechtwinkliges Dreieck mit den Katheten {a} cm und {b} cm und der Hypotenuse {c} cm. Es ist {h} cm hoch. Wie groß ist die Fläche seines Netzes?',
                 a * b + (a + b + c) * h, f'2 * {a} * {b} / 2 + ({a} + {b} + {c}) * {h}',
                 f'Grundflächen: 2 · {a} · {b} : 2 = {a * b} cm². Mantel: ({a} + {b} + {c}) · {h} = {(a + b + c) * h} cm². Zusammen {a * b + (a + b + c) * h} cm².',
                 'Netzfläche = 2 · Grundfläche + Umfang der Grundfläche · Höhe.', einheit='cm²')
    # Stufe 3: fehlende Höhe aus Netzfläche
    a, b, c = R.randint(2, 10), R.randint(2, 10), R.randint(2, 15)
    O = 2 * (a * b + a * c + b * c)
    return Z(f'Das Netz eines Quaders hat die Fläche {O} cm². Die Grundfläche ist {a} cm × {b} cm. Wie hoch ist der Quader?', c, f'({O} - 2 * {a} * {b}) / (2 * ({a} + {b}))',
             f'{O} = 2 · {a * b} + 2 · ({a} + {b}) · h → {O - 2 * a * b} = {2 * (a + b)} · h → h = {c} cm.',
             'Ziehe die beiden Grundflächen ab. Der Rest ist der Mantel: Umfang · Höhe.', einheit='cm')


def g_zylinder(R, st):
    if st == 1:
        teile = ['zwei Kreise und ein Rechteck', 'zwei Kreise und zwei Rechtecke', 'ein Kreis und ein Rechteck', 'zwei Rechtecke und ein Kreis']
        if R.random() < .5:
            return A(R, f'Aus welchen Flächen besteht das Netz eines Zylinders ({R.choice(["stehend", "liegend", "aus Pappe", "aus Blech"])})?', teile[0], teile[1:],
                     'Grund- und Deckfläche sind Kreise, der Mantel wird zu einem Rechteck abgewickelt.', 'Denke an eine Konservendose: Deckel, Boden, Etikett.')
        h, u = R.randint(4, 20), Fr(R.randint(60, 400), 10)
        return Z(f'Ein Zylinder ist {h} cm hoch, sein Grundkreis hat den Umfang {zt(u)} cm. Wie lang ist das Mantelrechteck im Netz?', u, cz(u),
                 f'Das Mantelrechteck reicht einmal um den Kreis: Länge = Umfang = {zt(u)} cm (Höhe {h} cm).', 'Das Etikett einer Dose reicht genau einmal herum.', einheit='cm')
    if st == 2:
        h, u = R.randint(4, 25), Fr(R.randint(60, 400), 10)
        return Z(f'Ein Zylinder ist {h} cm hoch, sein Grundkreis hat den Umfang {zt(u)} cm. Wie groß ist die Mantelfläche?', u * h, f'{cz(u)} * {h}',
                 f'Mantelrechteck: {zt(u)} cm · {h} cm = {zt(u * h)} cm².', 'Mantelfläche = Umfang · Höhe.', einheit='cm²')
    h = R.randint(4, 25); M = Fr(R.randint(60, 400), 10) * h
    u = M / h
    if R.random() < .5:
        return Z(f'Die Mantelfläche eines {h} cm hohen Zylinders ist {zt(M)} cm². Welchen Umfang hat der Grundkreis?', u, f'{cz(M)} / {h}',
                 f'M = u · h → u = M : h = {zt(M)} : {h} = {zt(u)} cm.', 'Stelle M = u · h nach u um.', einheit='cm')
    G = Fr(R.randint(100, 900), 10)
    return Z(f'Ein Zylinder hat einen Grundkreis mit {zt(G)} cm² Fläche und {zt(u)} cm Umfang, er ist {h} cm hoch. Wie groß ist die gesamte Netzfläche?', 2 * G + u * h,
             f'2 * {cz(G)} + {cz(u)} * {h}', f'2 · {zt(G)} + {zt(u)} · {h} = {zt(2 * G)} + {zt(u * h)} = {zt(2 * G + u * h)} cm².',
             'Netz: 2 Kreise + Mantelrechteck.', einheit='cm²')


def g_schraegbild(R, st):
    q = Fr(1, 2) if st < 3 else R.choice([Fr(1, 2), Fr(1, 2), Fr(1, 3), Fr(3, 4)])
    qt = '1/2' if q == Fr(1, 2) else ('1/3' if q == Fr(1, 3) else '3/4')
    if st == 1:
        t = Fr(R.randint(2, 20))
        if R.random() < .5:
            b, h = R.randint(2, 12), R.randint(2, 12)
            w = R.choice(['Breite', 'Höhe'])
            wert = b if w == 'Breite' else h
            return Z(f'Ein Quader ist {b} cm breit, {h} cm hoch und {zt(t)} cm tief. Wie lang zeichnest du im Schrägbild (q = 1/2, ω = 45°) die {w}?', wert, f'{wert}',
                     f'Die {w} liegt in der Vorderfläche und wird in wahrer Größe gezeichnet: {wert} cm.', 'Nur Kanten nach hinten werden verkürzt.', einheit='cm')
        return Z(f'Eine Kante führt {zt(t)} cm nach hinten. Wie lang zeichnest du sie im Schrägbild mit q = 1/2?', t / 2, f'{cz(t)} / 2',
                 f'{zt(t)} cm · 1/2 = {zt(t / 2)} cm.', 'Nach hinten: mit dem Verkürzungsfaktor multiplizieren.', einheit='cm')
    if st == 2:
        t = Fr(R.randint(2, 30))
        return Z(f'Im Schrägbild (q = 1/2) ist eine nach hinten laufende Kante {zt(t / 2)} cm lang. Wie lang ist sie in Wirklichkeit?', t, f'{cz(t / 2)} * 2',
                 f'Gezeichnet = wahr · 1/2 → wahr = {zt(t / 2)} · 2 = {zt(t)} cm.', 'Rechne rückwärts: durch q teilen.', einheit='cm')
    t = Fr(R.randint(1, 10) * q.denominator)
    if R.random() < .5:
        return Z(f'Eine Kante ist {zt(t)} cm lang und führt nach hinten. Wie lang wird sie im Schrägbild mit dem Verkürzungsfaktor q = {qt} gezeichnet?', t * q, f'{cz(t)} * {cz(q)}',
                 f'{zt(t)} · {qt} = {zt(t * q)} cm.', 'Multipliziere die wahre Länge mit q.', einheit='cm')
    # welche Strecke in wahrer Größe
    opts = ['die senkrechte Kante vorne rechts', 'die Kante, die von vorne nach hinten führt', 'die Raumdiagonale', 'die Diagonale der rechten Seitenfläche']
    r = opts[0]
    return A(R, f'Ein Quader wird im Schrägbild (q = {qt}, ω = 45°) gezeichnet, Vorderfläche parallel zur Zeichenebene. Welche Strecke erscheint in wahrer Länge?', r, opts[1:],
             'Alle Strecken in der Vorderfläche (oder parallel dazu) erscheinen in wahrer Länge. Kanten und Diagonalen mit Anteil nach hinten werden verzerrt.',
             'Was liegt parallel zur Zeichenebene?')


ANSICHT = {  # Körper (Lage): (Vorderansicht, Seitenansicht, Draufsicht)
    'ein stehender Zylinder': ('Rechteck', 'Rechteck', 'Kreis'),
    'ein liegender Zylinder (Achse von links nach rechts)': ('Rechteck', 'Kreis', 'Rechteck'),
    'ein Würfel': ('Quadrat', 'Quadrat', 'Quadrat'),
    'ein stehender Quader mit quadratischer Grundfläche (höher als breit)': ('Rechteck', 'Rechteck', 'Quadrat'),
    'ein dreiseitiges Prisma, das auf einer Rechteckfläche liegt (Dreieck vorne)': ('Dreieck', 'Rechteck', 'Rechteck'),
    'ein stehendes dreiseitiges Prisma (Dreieck oben)': ('Rechteck', 'Rechteck', 'Dreieck'),
    'eine quadratische Pyramide (Spitze oben)': ('Dreieck', 'Dreieck', 'Quadrat'),
    'ein stehender Kegel (Spitze oben)': ('Dreieck', 'Dreieck', 'Kreis'),
    'eine Kugel': ('Kreis', 'Kreis', 'Kreis'),
}
FORMEN = ['Rechteck', 'Quadrat', 'Kreis', 'Dreieck']


def g_ansichten(R, st):
    if st == 3 or (st == 2 and R.random() < .4):
        while True:
            k, (v, s, d) = R.choice(list(ANSICHT.items()))
            gleich = [kk for kk, vv in ANSICHT.items() if vv[0] == v and vv[2] == d]
            if len(gleich) == 1: break
        passt = lambda soll, ist: ist == soll or (soll == 'Rechteck' and ist == 'Quadrat')
        andere = R.sample([kk for kk, vv in ANSICHT.items() if kk != k and not (passt(v, vv[0]) and passt(d, vv[2]))], 3)
        return A(R, f'Welcher Körper hat die Vorderansicht „{v}“ und die Draufsicht „{d}“?', k[0].upper() + k[1:], [a[0].upper() + a[1:] for a in andere],
                 f'{k[0].upper() + k[1:]}: von vorn {v}, von oben {d}.', 'Stell dir vor, du schaust von vorn und von oben auf den Körper.')
    k, ans = R.choice(list(ANSICHT.items()))
    i = R.randrange(3)
    name = ['Vorderansicht', 'Seitenansicht', 'Draufsicht'][i]
    r = ans[i]
    return A(R, f'Welche Form hat die {name} – betrachtet wird {k}?', r, [f for f in FORMEN if f != r and not (r == 'Quadrat' and f == 'Rechteck')],
             f'{name}: {r}. (Vorderansicht {ans[0]}, Seitenansicht {ans[1]}, Draufsicht {ans[2]}.)', 'Von vorn – von der Seite – von oben.')


def g_beurteilen(R, st):
    n = R.choice(list(N_ECK)); m = n + R.choice([1, -1, 2])
    al = [
        ('Ein Würfel ist ein Prisma.', True), ('Ein Quader ist ein Prisma.', True), ('Eine Pyramide ist ein Prisma.', False),
        ('Ein Zylinder hat genau zwei Kanten.', True), ('Ein Zylinder hat keine Ecken.', True), ('Ein Kegel ist ein Prisma.', False),
        (f'Ein {N_ECK[n]} Prisma hat {3 * n} Kanten.', True), (f'Ein {N_ECK[n]} Prisma hat {2 * n} Ecken.', True),
        (f'Ein {N_ECK[n]} Prisma hat {n} Flächen.', False), (f'Ein {N_ECK[n]} Prisma hat {2 * m} Ecken.', m == n),
        (f'Das Netz eines {N_ECK[n][:-2]}en Prismas enthält {n} Rechtecke.', True),
        ('Im Schrägbild werden Kanten nach hinten in wahrer Länge gezeichnet.', False),
        ('Im Schrägbild erscheint die Vorderfläche in wahrer Größe.', True),
        ('Das Mantelrechteck eines Zylinders ist so lang wie der Durchmesser des Grundkreises.', False),
        ('Jedes Netz eines Würfels besteht aus 6 Quadraten.', True),
        ('Die Grundflächen eines Prismas sind parallel und deckungsgleich.', True),
        ('Bei einem Prisma können die Grundflächen verschieden groß sein.', False),
    ]
    wahr = [t for t, w in al if w]; falsch = [t for t, w in al if not w]
    if st == 1 or (st == 2 and R.random() < .5):
        t = R.choice(wahr)
        return A(R, 'Welche Aussage ist richtig?', t, R.sample(falsch, 3), f'Richtig: {t}',
                 'Prüfe die Eigenschaften: zwei parallele, deckungsgleiche Grundflächen; Rechtecke als Seiten.')
    t = R.choice(falsch)
    return A(R, 'Welche Aussage ist FALSCH?', t, R.sample(wahr, 3), f'Falsch: {t}', 'Suche ein Gegenbeispiel oder zähle nach.')


GEN = {'prisma': g_prisma, 'netz': g_netz, 'zylinder': g_zylinder, 'schraegbild': g_schraegbild, 'ansichten': g_ansichten, 'beurteilen': g_beurteilen}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Körper und Netze', ['prisma', 'netz', 'zylinder']), ('Darstellen', ['schraegbild', 'ansichten']), ('Verstehen', ['beurteilen'])],
         'Prismen und Zylinder erkennen, ihre Netze verstehen und berechnen, Schrägbilder nach den Regeln anlegen und Ansichten zuordnen.',
         ['Prisma: 2 deckungsgleiche parallele Grundflächen, Mantel aus Rechtecken. n-seitig: 2n Ecken, 3n Kanten, n + 2 Flächen.',
          'Zylindermantel abgewickelt: Rechteck mit Länge = Kreisumfang.', 'Schrägbild: Vorderfläche wahr, nach hinten unter 45° und mit q (meist 1/2) verkürzt.'],
         offen=['Lernkarten „netz“, „zylinder“, „schraegbild“, „ansichten“: Netze erkennen („Welches Netz ergibt einen Würfel?“), Schrägbilder zeichnen und '
                'Ansichten zeichnen brauchen Zeichnungen. Gebaut wurde nur, was sich in Worten und mit Maßen eindeutig beschreiben lässt.',
                'Zylinder: Der Kreisumfang wird in den Aufgaben gegeben, weil Kreisberechnungen (π) erst im Thema messen.kreisberechnung folgen.'])
