#!/usr/bin/env python3
"""Thema messen.koerper_darstellung – Körper darstellen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, Z, baue, cz, mit_bild, runde, zt  # noqa: E402

META = {'thema_schluessel': 'messen.koerper_darstellung', 'thema_id': 52, 'block_id': 86, 'klasse': {'gym_by': 8, 'rs_by': 5}}

ETAPPEN = [
    {'lernziel': 'prisma', 'titel': 'Prismen: Ecken, Kanten, Flächen',
     'regel': 'Ein ⟦Prisma⟧ hat zwei deckungsgleiche, parallele ⟦Grundflächen⟧ (n-Ecke) und n Rechtecke als ⟦Mantel⟧. Zählen statt auswendig lernen: Ecken – n unten und n oben, also ⟦2n⟧. Kanten – n unten, n oben, n senkrecht, also ⟦3n⟧. Flächen – n Rechtecke und 2 Grundflächen, also ⟦n + 2⟧.',
     'schritte': ['Ein Bleistift ohne Spitze ist ein sechsseitiges Prisma: n = 6.', 'Ecken: 6 unten + 6 oben = 12. Kanten: 6 + 6 + 6 = 18.', 'Flächen: 6 Rechtecke + 2 Sechsecke = ⟦8⟧.'],
     'probe': 'Eulerscher Polyedersatz: E + F − K = 12 + 8 − 18 = 2 ✓',
     'fehler': 'Ein dreiseitiges Prisma hat nicht 3 Flächen: Zu den 3 Rechtecken kommen die ⟦2 Grundflächen⟧ dazu, also 5.',
     '_verbot': ['Bleistift ohne Spitze']},
    {'lernziel': 'netz', 'titel': 'Netze von Prismen',
     'regel': 'Schneidest du eine Schachtel an einigen Kanten auf und klappst sie flach auf den Tisch, entsteht ein ⟦Netz⟧: 2 Grundflächen und n Rechtecke. Die Rechtecke sind so hoch wie das Prisma; nebeneinander sind sie so breit wie der ⟦Umfang der Grundfläche⟧.',
     'schritte': ['Schachtel (Quader) 5 cm × 3 cm, Höhe 4 cm.', 'Boden und Deckel: 2 · 5 · 3 = 30 cm². Die vier Seiten bilden zusammen einen Streifen: (5 + 3 + 5 + 3) · 4 = 16 · 4 = 64 cm².',
                  'Fläche des Netzes = Oberfläche = 30 + 64 = ⟦94 cm²⟧.'],
     'fehler': 'Die Netzfläche eines Quaders ist nicht 5 · 3 · 4 = 60. Das wäre das ⟦Volumen⟧. Für das Netz werden die Flächen der 6 Rechtecke ⟦addiert⟧.',
     'bild': {'typ': 'figur', 'punkte': {'_a': [0, 0], '_b': [5, 0], '_c': [8, 0], '_d': [13, 0], '_e': [16, 0], '_f': [16, 4], '_g': [13, 4], '_h': [8, 4], '_i': [5, 4], '_j': [0, 4],
                                         '_k': [0, 7], '_l': [5, 7], '_m': [0, -3], '_n': [5, -3]},
              'linien': [['_a', '_b'], ['_b', '_c', '3 cm'], ['_c', '_d', '5 cm'], ['_d', '_e', '3 cm'], ['_e', '_f', '4 cm'], ['_f', '_g'], ['_g', '_h'], ['_h', '_i'], ['_i', '_j'],
                         ['_j', '_a'], ['_b', '_i'], ['_c', '_h'], ['_d', '_g'], ['_j', '_k'], ['_k', '_l', '5 cm'], ['_l', '_i'], ['_a', '_m'], ['_m', '_n'], ['_n', '_b', '3 cm']]},
     '_verbot': ['5 cm × 3 cm, Höhe 4 cm']},
    {'lernziel': 'zylinder', 'titel': 'Zylinder und sein Netz',
     'regel': 'Ein ⟦Zylinder⟧ hat zwei Kreise als Grundflächen. Ziehst du das Etikett einer Konservendose ab, siehst du den ⟦Mantel⟧: ein Rechteck, so hoch wie die Dose und so lang wie der ⟦Umfang⟧ des Grundkreises.',
     'schritte': ['Dose: Umfang des Grundkreises u = 18,8 cm, Höhe h = 10 cm.', 'Das Etikett ist ein Rechteck: 18,8 cm lang, 10 cm hoch.', 'Mantelfläche: 18,8 cm · 10 cm = ⟦188 cm²⟧.'],
     'fehler': 'Das Mantelrechteck so lang wie den ⟦Durchmesser⟧ nehmen. Das Etikett muss aber einmal ganz um die Dose herum reichen – also so lang wie der ⟦Umfang⟧. Der Umfang ist gut dreimal so lang wie der Durchmesser.',
     'bild': {'typ': 'figur', 'punkte': {'_a': [0, 0], '_b': [18.8, 0], '_c': [18.8, 10], '_d': [0, 10], 'M': [3, 13], 'N': [3, -3]},
              'linien': [['_a', '_b', 'u ≈ 18,8 cm'], ['_b', '_c', 'h = 10 cm'], ['_c', '_d'], ['_d', '_a']], 'kreise': [{'m': 'M', 'r': 3}, {'m': 'N', 'r': 3}]},
     '_verbot': ['u = 18,8 cm']},
    {'lernziel': 'schraegbild', 'titel': 'Schrägbilder: Längen nach hinten',
     'regel': 'Im ⟦Schrägbild⟧ zeichnet man die Vorderfläche in ⟦wahrer Größe⟧. Kanten, die nach hinten gehen, zeichnet man unter dem ⟦Winkel 45°⟧ und ⟦verkürzt⟧, meist auf die Hälfte (Verkürzungsfaktor q = 1/2).',
     'schritte': ['Quader: 6 cm breit, 4 cm hoch, 8 cm tief.', 'Vorderfläche in wahrer Größe: Rechteck 6 cm × 4 cm.', 'Kanten nach hinten: unter 45° und halb so lang: 8 cm · 1/2 = ⟦4 cm⟧.',
                  'Unsichtbare Kanten (hinten links unten) zeichnest du ⟦gestrichelt⟧.'],
     'fehler': 'Die Kante nach hinten in voller Länge zeichnen: 8 cm statt 4 cm. Dann wirkt der Quader viel zu tief. Verkürzt werden ⟦nur⟧ die Kanten nach hinten – Breite und Höhe bleiben in wahrer Größe.',
     'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [6, 0], 'C': [8.83, 2.83], 'D': [2.83, 2.83], 'E': [0, 4], 'F': [6, 4], 'G': [8.83, 6.83], 'H': [2.83, 6.83], '_X': [8.5, 0]},
              'linien': [['A', 'B', '6 cm'], ['B', 'F', '4 cm'], ['F', 'E'], ['E', 'A'], ['B', 'C', '4 cm'], ['C', 'G'], ['G', 'F'], ['E', 'H'], ['H', 'G'],
                         ['A', 'D', '', 'gestrichelt'], ['D', 'C', '', 'gestrichelt'], ['D', 'H', '', 'gestrichelt'], ['B', '_X', '', 'gestrichelt']],
              'winkel': [['B', '_X', 'C', '45°']]},
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


# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'prisma': {
  'einstieg': 'Ein Bleistift ohne Spitze, eine dreieckige Schokoladenpackung, ein Schuhkarton: Alle haben oben und unten dieselbe Form, und ihre Seiten sind Rechtecke. Solche Körper heißen ⟦Prismen⟧. Wie viele Ecken, Kanten und Flächen sie haben, kann man zählen – oder geschickt ausrechnen.',
  'woerter': [['Prisma', 'Körper mit zwei gleichen, parallelen Grundflächen und Rechtecken als Seiten'], ['Grundfläche', 'die Fläche unten (die gleiche liegt oben)'],
              ['n-Eck', 'Vieleck mit n Ecken, z. B. Sechseck: n = 6'], ['Mantel', 'alle Seitenrechtecke zusammen'], ['Kante', 'Linie, an der zwei Flächen zusammenstoßen'],
              ['Eulerscher Polyedersatz', 'Ecken + Flächen − Kanten = 2; gilt für solche Körper ohne Rundungen']],
  'schritte': ['Ein Bleistift ohne Spitze ist ein sechsseitiges Prisma: Die Grundfläche ist ein Sechseck, also n = 6.', 'Ecken: 6 unten und 6 oben, also 12.',
               'Kanten: 6 unten, 6 oben und 6 senkrechte, also 18.', 'Flächen: 6 Rechtecke und 2 Sechsecke, zusammen ⟦8⟧.']},
 'netz': {
  'einstieg': 'Schneide eine leere Müslischachtel an einigen Kanten auf und klappe sie flach auf den Tisch. Die flache Figur, die dabei entsteht, heißt ⟦Netz⟧. Ihre Fläche zeigt, wie viel Pappe man für die Schachtel braucht.',
  'woerter': [['Netz', 'die flach ausgebreitete Hülle eines Körpers'], ['Oberfläche', 'die Fläche aller Seiten zusammen – gleich der Fläche des Netzes'],
              ['Quader', 'ein Prisma mit Rechtecken als Grundflächen, z. B. eine Schachtel'], ['cm²', 'Quadratzentimeter, Einheit für Flächen']],
  'schritte': ['Schachtel (Quader): 5 cm lang, 3 cm breit, 4 cm hoch.', 'Boden und Deckel sind je 5 · 3 = 15 cm² groß, zusammen 30 cm².',
               'Die vier Seiten bilden einen Streifen: 5 + 3 + 5 + 3 = 16 cm lang und 4 cm hoch, also 64 cm².', 'Fläche des Netzes = Oberfläche = 30 + 64 = ⟦94 cm²⟧.']},
 'zylinder': {
  'einstieg': 'Eine Konservendose hat oben und unten einen Kreis. Ziehst du das Papier-Etikett ab und legst es flach hin, ist es ein Rechteck. So ein Körper heißt ⟦Zylinder⟧, das Etikett zeigt seinen ⟦Mantel⟧.',
  'woerter': [['Zylinder', 'Körper mit zwei gleichen Kreisen als Grund- und Deckfläche'], ['Umfang u', 'die Länge einmal um den Kreis herum'],
              ['Durchmesser', 'die Strecke quer durch den Kreis, durch die Mitte'], ['Mantelfläche', 'die Fläche des abgewickelten Rechtecks']],
  'schritte': ['Dose: Umfang des Grundkreises u = 18,8 cm, Höhe h = 10 cm.', 'Das Etikett reicht einmal um die Dose: Es ist so lang wie der Umfang, also 18,8 cm.',
               'Es ist so hoch wie die Dose, also 10 cm.', 'Mantelfläche: 18,8 cm · 10 cm = ⟦188 cm²⟧.']},
 'schraegbild': {
  'einstieg': 'Eine Schachtel ist ein räumlicher Körper, dein Heft aber ist flach. Damit die Zeichnung trotzdem räumlich wirkt, zeichnet man Kanten, die nach hinten gehen, schräg und kürzer. So eine Zeichnung heißt ⟦Schrägbild⟧.',
  'woerter': [['Schrägbild', 'räumlich wirkende Zeichnung eines Körpers auf Papier'], ['wahre Größe', 'in der echten Länge gezeichnet'],
              ['Verkürzungsfaktor q', 'damit werden Kanten nach hinten verkürzt; q = 1/2 heißt: halb so lang'], ['45°', 'ein halber rechter Winkel – die Richtung „schräg nach hinten“'],
              ['gestrichelt', 'mit kurzen Strichen: diese Kante sieht man von vorn nicht']]},
 'ansichten': {
  'einstieg': 'Wer ein Haus plant, zeichnet es dreimal flach: von vorn, von der Seite und von oben. Aus diesen drei Blickrichtungen erkennt man die Form genau. Die drei Zeichnungen heißen ⟦Ansichten⟧.',
  'woerter': [['Vorderansicht', 'was man von vorn sieht'], ['Seitenansicht', 'was man von der Seite sieht'], ['Draufsicht', 'was man von oben sieht'],
              ['ebene Figur', 'eine flache Form wie Rechteck oder Kreis']],
  'schritte': ['Eine Dose (Zylinder) steht auf ihrem Boden.', 'Von vorn siehst du ihre Höhe und ihre Breite: ein ⟦Rechteck⟧.', 'Von der Seite sieht sie genauso aus: wieder ein Rechteck.',
               'Von oben siehst du nur den Deckel: einen ⟦Kreis⟧.']},
 'beurteilen': {
  'einstieg': 'Ist ein Würfel ein Prisma? Und eine Pyramide? Um das zu entscheiden, vergleichst du den Körper mit den Merkmalen eines Prismas. Fehlt auch nur ein Merkmal, ist er kein Prisma – der Körper ist dann ein ⟦Gegenbeispiel⟧ zur Behauptung.',
  'woerter': [['Merkmal', 'eine Eigenschaft, die erfüllt sein muss'], ['deckungsgleich', 'genau gleich groß und gleich geformt'],
              ['Pyramide', 'Körper mit einer Grundfläche und einer Spitze'], ['Kegel', 'wie eine Pyramide, aber mit einem Kreis als Grundfläche'],
              ['Gegenbeispiel', 'ein Fall, für den die Behauptung nicht stimmt']],
  'schritte': ['Aussage: „Ein Würfel ist ein Prisma.“', 'Merkmal 1: zwei gleiche, parallele Grundflächen. Beim Würfel sind Boden und Deckel gleich große Quadrate – erfüllt.',
               'Merkmal 2: Die Seiten sind Rechtecke. Beim Würfel sind es Quadrate, und Quadrate sind besondere Rechtecke – erfüllt.', 'Die Aussage ist ⟦richtig⟧.']},
}

for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))
# ---- KLAR ENDE ----

N_ECK = {3: 'dreiseitiges', 4: 'vierseitiges', 5: 'fünfseitiges', 6: 'sechsseitiges', 7: 'siebenseitiges', 8: 'achtseitiges', 9: 'neunseitiges',
         10: 'zehnseitiges', 12: 'zwölfseitiges'}


# ---------- Würfelnetze (Sechslinge) ----------
def falten(zellen):
    """Würfel über das Netz rollen. Liefert {Zelle: Fläche} oder None, wenn zwei Zellen auf dieselbe Fläche fallen."""
    zellen = list(zellen)
    start = zellen[0]
    lage = {start: {'unten': 'U', 'oben': 'O', 'n': 'N', 's': 'S', 'o': 'E', 'w': 'W'}}
    offen = [start]
    while offen:
        z = offen.pop()
        l = lage[z]
        for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nb = (z[0] + dx, z[1] + dy)
            if nb not in zellen or nb in lage: continue
            k = dict(l)
            if dx == 1: k.update(unten=l['o'], o=l['oben'], oben=l['w'], w=l['unten'])
            if dx == -1: k.update(unten=l['w'], w=l['oben'], oben=l['o'], o=l['unten'])
            if dy == 1: k.update(unten=l['n'], n=l['oben'], oben=l['s'], s=l['unten'])
            if dy == -1: k.update(unten=l['s'], s=l['oben'], oben=l['n'], n=l['unten'])
            lage[nb] = k
            offen.append(nb)
    flaechen = {z: l['unten'] for z, l in lage.items()}
    if len(flaechen) != 6 or len(set(flaechen.values())) != 6: return None
    for (x, y) in zellen:      # 2×2-Block ist nie ein Würfelnetz
        if {(x + 1, y), (x, y + 1), (x + 1, y + 1)} <= set(zellen): return None
    return flaechen


GEGEN = {'U': 'O', 'O': 'U', 'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}


def sechsling(R):
    while True:
        zellen = {(0, 0)}
        while len(zellen) < 6:
            x, y = R.choice(sorted(zellen))
            dx, dy = R.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            zellen.add((x + dx, y + dy))
        xs = [x for x, _ in zellen]; ys = [y for _, y in zellen]
        if max(xs) - min(xs) <= 4 and max(ys) - min(ys) <= 4:
            mx, my = min(xs), min(ys)
            return sorted((x - mx, y - my) for x, y in zellen)


def netz_bild(zellen, namen=None):
    P, L = {}, []
    kanten = set()
    for (x, y) in zellen:
        ecken = [(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1)]
        for a, b in zip(ecken, ecken[1:] + ecken[:1]):
            kanten.add(tuple(sorted((a, b))))
    for a, b in sorted(kanten):
        for q in (a, b): P[f'_{q[0]}_{q[1]}'] = [q[0], q[1]]
        L.append([f'_{a[0]}_{a[1]}', f'_{b[0]}_{b[1]}'])
    if namen:
        for (x, y), n in zip(zellen, namen): P[n] = [x + 0.5, y + 0.5]
    return {'typ': 'figur', 'punkte': P, 'linien': L}


def quader_schraeg(b, h, t, q):
    """Schrägbild eines Quaders (ω = 45°): Vorderfläche b × h, Tiefe t · q."""
    d = float(t * q) / 2 ** .5
    rr = lambda v: round(v, 2)
    P = {'A': [0, 0], 'B': [b, 0], 'C': [rr(b + d), rr(d)], 'D': [rr(d), rr(d)], 'E': [0, h], 'F': [b, h], 'G': [rr(b + d), rr(h + d)], 'H': [rr(d), rr(h + d)]}
    L = [['A', 'B', f'{b} cm'], ['B', 'F', f'{h} cm'], ['F', 'E'], ['E', 'A'], ['B', 'C', f'{zt(t * q)} cm'], ['C', 'G'], ['G', 'F'], ['E', 'H'], ['H', 'G'],
         ['A', 'D', '', 'gestrichelt'], ['D', 'C', '', 'gestrichelt'], ['D', 'H', '', 'gestrichelt']]
    return {'typ': 'figur', 'punkte': P, 'linien': L}


def g_prisma(R, st):
    if st == 3 and R.random() < .35:
        art = R.choice(['kanten', 'ecken', 'flaechen'])
        if art == 'kanten':
            k = R.choice([k for k in range(8, 40) if k % 3])
            return A(R, f'Kann ein Prisma {k} Kanten haben?', 'Nein, die Kantenzahl ist immer durch 3 teilbar.', [f'Ja, ein {k}-seitiges.', f'Ja, ein {k // 2}-seitiges.', 'Ja, jede Zahl ab 9 ist möglich.'],
                     f'Ein n-seitiges Prisma hat 3n Kanten. {k} ist nicht durch 3 teilbar, also gibt es kein solches Prisma.', 'Wie viele Kanten hat ein n-seitiges Prisma?')
        if art == 'ecken':
            k = R.choice([k for k in range(7, 30) if k % 2])
            return A(R, f'Kann ein Prisma {k} Ecken haben?', 'Nein, die Eckenzahl ist immer gerade.', [f'Ja, ein {k}-seitiges.', f'Ja, ein {(k + 1) // 2}-seitiges.', 'Ja, wenn die Grundfläche unregelmäßig ist.'],
                     f'Ein n-seitiges Prisma hat 2n Ecken – immer eine gerade Zahl. {k} ist ungerade.', 'Ecken: n unten und n oben.')
        k = R.choice([3, 4])
        return A(R, f'Kann ein Prisma {k} Flächen haben?', 'Nein, ein Prisma hat mindestens 5 Flächen.', [f'Ja, ein {k - 2}-seitiges.', f'Ja, ein {k}-seitiges.', 'Ja, ein Würfel.'],
                 f'n + 2 Flächen, und die Grundfläche braucht mindestens 3 Ecken: mindestens 3 + 2 = 5 Flächen.', 'Wie viele Ecken hat die kleinste mögliche Grundfläche?')
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
    if st == 1 and R.random() < .3:
        z = R.randint(1, 6)
        return Z(f'Auf einem Spielwürfel ergeben gegenüberliegende Augenzahlen zusammen 7. Welche Zahl liegt der {z} gegenüber?', 7 - z, f'7 - {z}',
                 f'{z} + □ = 7 → □ = {7 - z}.', 'Gegenüberliegende Zahlen ergeben zusammen 7.')
    if st >= 2 and R.random() < .4:
        if st == 3 and R.random() < .5:
            while True:
                zellen = sechsling(R)
                f = falten(zellen)
                if f: break
            namen = list('ABCDEF')
            R.shuffle(namen)
            k = R.randrange(6)
            gegen = next(namen[i] for i, z in enumerate(zellen) if f[z] == GEGEN[f[zellen[k]]])
            andere = [namen[i] for i in range(6) if i != k and namen[i] != gegen]
            return mit_bild(A(R, f'Aus dem Netz wird ein Würfel gefaltet. Welche Fläche liegt der Fläche {namen[k]} gegenüber?', gegen, R.sample(andere, 3),
                              f'Beim Falten liegen {namen[k]} und {gegen} gegenüber; alle anderen Flächen grenzen an {namen[k]} an. Tipp: In einer Reihe aus drei Flächen liegen die beiden äußeren einander gegenüber.',
                              'Benachbarte Flächen im Netz liegen nie gegenüber. Suche eine Fläche, die eine Fläche Abstand hat.'), netz_bild(zellen, namen))
        while True:
            zellen = sechsling(R)
            ok_ = falten(zellen) is not None
            if R.random() < .5 or ok_: break
        block = any({(x + 1, y), (x, y + 1), (x + 1, y + 1)} <= set(zellen) for x, y in zellen)
        if ok_:
            ri = 'Ja, beim Falten wird jede Würfelfläche genau einmal bedeckt.'
        elif block:
            ri = 'Nein, vier Quadrate bilden einen Block – sie können nicht alle um eine Ecke herum liegen.'
        else:
            ri = 'Nein, beim Falten überlappen zwei Quadrate, und eine Würfelfläche bleibt offen.'
        opts = ['Ja, beim Falten wird jede Würfelfläche genau einmal bedeckt.', 'Nein, beim Falten überlappen zwei Quadrate, und eine Würfelfläche bleibt offen.',
                'Nein, vier Quadrate bilden einen Block – sie können nicht alle um eine Ecke herum liegen.', 'Nein, ein Würfelnetz muss genau vier Quadrate in einer Reihe haben.']
        return mit_bild(A(R, 'Lässt sich das Netz aus 6 Quadraten zu einem Würfel falten?', ri, [o for o in opts if o != ri],
                          ri + ' Probe: Falte in Gedanken – lege ein Quadrat als Boden fest und klappe die Nachbarn hoch.',
                          'Lege ein Quadrat als Boden fest und klappe die anderen in Gedanken hoch.'), netz_bild(zellen))
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


ZYL = __import__('collections').Counter()


def g_zylinder(R, st):
    if st == 1:
        teile = ['zwei Kreise und ein Rechteck', 'zwei Kreise und zwei Rechtecke', 'ein Kreis und ein Rechteck', 'zwei Rechtecke und ein Kreis']
        if ZYL['netzfrage'] == 0:
            ZYL['netzfrage'] += 1
            return A(R, 'Aus welchen Flächen besteht das Netz eines Zylinders?', teile[0], teile[1:],
                     'Grund- und Deckfläche sind Kreise, der Mantel wird zu einem Rechteck abgewickelt.', 'Denke an eine Konservendose: Deckel, Boden, Etikett.')
        if ZYL['teile'] == 0 and R.random() < .5:
            ZYL['teile'] += 1
            return Z('Ein Zylinder wird aufgeschnitten und flach gelegt. Wie viele Teilflächen hat das Netz?', 3, '2 + 1',
                     'Zwei Kreise (Boden, Deckel) und ein Rechteck (Mantel): 3 Teilflächen.', 'Denke an eine Konservendose: Deckel, Boden, Etikett.')
        h, u = R.randint(4, 20), Fr(R.randint(60, 400), 10)
        return Z(f'Ein Zylinder ist {h} cm hoch, sein Grundkreis hat den Umfang {zt(u)} cm. Wie lang ist das Mantelrechteck im Netz?', u, cz(u),
                 f'Das Mantelrechteck reicht einmal um den Kreis: Länge = Umfang = {zt(u)} cm (Höhe {h} cm).', 'Das Etikett einer Dose reicht genau einmal herum.', einheit='cm')
    if st == 3 and R.random() < .4:
        d, h, ue = R.choice([(Fr(15, 2), 11, 1), (Fr(10), 12, 2), (Fr(8), 10, 1), (Fr(13, 2), 9, Fr(3, 2))])
        L_ = Fr(314, 100) * d + ue
        return Z(f'Eine Dose hat den Durchmesser {zt(d)} cm und ist {h} cm hoch. Das Etikett überlappt {zt(ue)} cm. Wie lang muss es sein? (π ≈ 3,14, auf eine Nachkommastelle runden)',
                 runde(L_, 1), f'round(3.14 * {cz(d)} + {cz(ue)}, 1)', f'Umfang u = π · d ≈ 3,14 · {zt(d)} = {zt(Fr(314, 100) * d)} cm. Dazu die Überlappung: {zt(Fr(314, 100) * d)} + {zt(ue)} ≈ {zt(runde(L_, 1))} cm.',
                 'Das Etikett reicht einmal um die Dose (Umfang) und ein Stück weiter.', einheit='cm', toleranz=0.1)
    if st == 2 and ZYL['mantel'] < 8:
        ZYL['mantel'] += 1
        h, u = R.randint(4, 25), Fr(R.randint(60, 400), 10)
        return Z(f'Ein Zylinder ist {h} cm hoch, sein Grundkreis hat den Umfang {zt(u)} cm. Wie groß ist die Mantelfläche?', u * h, f'{cz(u)} * {h}',
                 f'Mantelrechteck: {zt(u)} cm · {h} cm = {zt(u * h)} cm².', 'Mantelfläche = Umfang · Höhe.', einheit='cm²')
    h = R.randint(4, 25); M = Fr(R.randint(60, 400), 10) * h
    u = M / h
    if st == 2 or R.random() < .5:
        return Z(f'Die Mantelfläche eines {h} cm hohen Zylinders ist {zt(M)} cm². Welchen Umfang hat der Grundkreis?', u, f'{cz(M)} / {h}',
                 f'M = u · h → u = M : h = {zt(M)} : {h} = {zt(u)} cm.', 'Stelle M = u · h nach u um.', einheit='cm')
    from _bausatz import PIF
    G = runde(u * u / (4 * PIF), 1)     # passend zum Umfang (gerundet)
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
    if st >= 2 and R.random() < .3:
        frage, ri, fa, w = R.choice([
            ('Welche Flächen eines Quaders erscheinen im Schrägbild (Vorderfläche parallel zur Zeichenebene) als Parallelogramm?', 'die Seitenflächen und die Deckfläche',
             ['nur die Vorderfläche', 'keine', 'alle sechs Flächen'], 'Vorder- und Rückfläche bleiben Rechtecke. Alle Flächen, die nach hinten laufen (Seiten, Deck- und Bodenfläche), werden schräg verzerrt.'),
            ('Welche Kanten eines liegenden dreiseitigen Prismas (Dreieck vorne) werden im Schrägbild verkürzt gezeichnet?', 'die Kanten, die nach hinten laufen',
             ['die Dreiecksseiten vorne', 'alle Kanten', 'keine Kante'], 'Das vordere Dreieck liegt parallel zur Zeichenebene: wahre Größe. Nur die drei Kanten nach hinten werden mit q verkürzt.'),
            ('Welche Strecke eines Würfels erscheint im Schrägbild (q = 1/2, ω = 45°) in wahrer Länge?', 'die Diagonale der Vorderfläche',
             ['die Raumdiagonale', 'die Diagonale der Deckfläche', 'die Kante nach hinten'], 'Die Vorderfläche liegt in der Zeichenebene, also auch ihre Diagonale. Alles mit Anteil nach hinten wird verzerrt.')])
        return A(R, frage, ri, fa, w, 'Was liegt parallel zur Zeichenebene?')
    if st >= 2 and R.random() < .35:
        b, h, t = R.randint(3, 8), R.randint(2, 6), R.choice([2, 4, 6, 8, 10])
        return mit_bild(Z(f'Das Schrägbild (q = 1/2, ω = 45°) zeigt einen Quader. Wie tief ist der Quader in Wirklichkeit?', t, f'{cz(Fr(t, 2))} * 2',
                          f'Die Kante nach hinten ist gezeichnet {zt(Fr(t, 2))} cm lang. Wahre Tiefe = {zt(Fr(t, 2))} cm : 1/2 = {t} cm.',
                          'Die schräge Kante ist verkürzt gezeichnet. Rechne rückwärts.', einheit='cm'), quader_schraeg(b, h, Fr(t), Fr(1, 2)))
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


ZUSAMMEN = [
    ('Ein Würfel trägt oben eine quadratische Pyramide mit derselben Grundfläche.', 'Vorderansicht', 'Quadrat mit Dreieck darauf (wie ein Haus)', ['Dreieck', 'Quadrat', 'Kreis mit Dreieck darauf']),
    ('Ein stehender Bleistift: Zylinder mit Kegel oben.', 'Vorderansicht', 'Rechteck mit Dreieck darauf', ['Dreieck', 'Rechteck', 'Kreis']),
    ('Ein stehender Bleistift: Zylinder mit Kegel oben.', 'Draufsicht', 'Kreis (mit der Spitze als Punkt in der Mitte)', ['Rechteck mit Dreieck darauf', 'Dreieck', 'Quadrat']),
    ('Ein Würfel trägt oben eine quadratische Pyramide mit derselben Grundfläche.', 'Draufsicht', 'Quadrat mit seinen beiden Diagonalen', ['Dreieck', 'Quadrat mit Dreieck darauf', 'Kreis']),
    ('Ein Zylinder liegt quer (Achse von links nach rechts) auf einem Quader, der genauso breit ist.', 'Seitenansicht', 'Rechteck mit Kreis darauf', ['Rechteck mit Rechteck darauf', 'Kreis', 'Dreieck']),
]


def g_ansichten(R, st):
    if st == 3 and R.random() < .45:
        k, ans, ri, fa = R.choice(ZUSAMMEN)
        return A(R, f'{k} Welche Form hat die {ans}?', ri, fa, f'{ans}: {ri}. Betrachte jeden Teilkörper einzeln und setze die Ansichten zusammen.',
                 'Zeichne die Ansicht jedes Teilkörpers und setze sie aufeinander.')
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
        (f'Der Mantel eines geraden {N_ECK[n][:-2]}en Prismas besteht aus {n} Rechtecken.', True),
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


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl8.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl8 import mit_umbau  # noqa: E402

_TRI = {'_A': [0, 0], '_B': [4, 0], '_C': [2, 3], '_D': [3, 2], '_E': [7, 2], '_F': [5, 5]}
_TRI_L = [['_A', '_B'], ['_B', '_C'], ['_C', '_A'], ['_B', '_E'], ['_C', '_F'], ['_E', '_F'],
          ['_A', '_D', '', 'gestrichelt'], ['_D', '_E', '', 'gestrichelt'], ['_D', '_F', '', 'gestrichelt']]
_NETZ = {"_a": [0, 0], "_b": [5, 0], "_c": [8, 0], "_d": [13, 0], "_e": [16, 0], "_f": [16, 4], "_g": [13, 4], "_h": [8, 4], "_i": [5, 4], "_j": [0, 4],
         "_k": [0, 7], "_l": [5, 7], "_m": [0, -3], "_n": [5, -3]}
_NETZ_L = [["_a", "_b"], ["_b", "_c", "3 cm"], ["_c", "_d", "5 cm"], ["_d", "_e", "3 cm"], ["_e", "_f", "4 cm"], ["_f", "_g"], ["_g", "_h"], ["_h", "_i"], ["_i", "_j"],
           ["_j", "_a"], ["_b", "_i"], ["_c", "_h"], ["_d", "_g"], ["_j", "_k"], ["_k", "_l", "5 cm"], ["_l", "_i"], ["_a", "_m"], ["_m", "_n"], ["_n", "_b", "3 cm"]]
_Q = {"A": [0, 0], "B": [6, 0], "C": [8.83, 2.83], "D": [2.83, 2.83], "E": [0, 4], "F": [6, 4], "G": [8.83, 6.83], "H": [2.83, 6.83], "_X": [8.5, 0]}
_Q_L = [["A", "B", "6 cm"], ["B", "F", "4 cm"], ["F", "E"], ["E", "A"], ["B", "C", "4 cm (45°)"], ["C", "G"], ["G", "F"], ["E", "H"], ["H", "G"],
        ["A", "D", "", "gestrichelt"], ["D", "C", "", "gestrichelt"], ["D", "H", "", "gestrichelt"], ["B", "_X", "", "gestrichelt"]]
_W = {'_A': [0, 0], '_B': [3, 0], '_C': [4.5, 1.5], '_D': [1.5, 1.5], '_E': [0, 3], '_F': [3, 3], '_G': [4.5, 4.5], '_H': [1.5, 4.5]}
_W_L = [['_A', '_B'], ['_B', '_F'], ['_F', '_E'], ['_E', '_A'], ['_B', '_C'], ['_C', '_G'], ['_G', '_F'], ['_E', '_H'], ['_H', '_G'],
        ['_A', '_D', '', 'gestrichelt'], ['_D', '_C', '', 'gestrichelt'], ['_D', '_H', '', 'gestrichelt']]
UMBAU = {
 'prisma': {
  'einstieg': 'Eine dreieckige Schokopackung, ein Bleistift ohne Spitze, ein Schuhkarton. Vorne und hinten haben sie dieselbe Form, die Seiten sind Rechtecke. Solche Körper heißen ⟦Prismen⟧.',
  'woerter': [['Prisma', 'Körper mit zwei gleichen, parallelen Grundflächen und Rechtecken als Seiten'], ['Grundfläche', 'die Form vorne und hinten, hier ein Dreieck'], ['n', 'die Anzahl der Ecken der Grundfläche']],
  'bild': {'typ': 'figur', 'punkte': _TRI, 'linien': _TRI_L},
  'schritte': [{'text': 'Die Schokopackung ist ein Prisma. Die Grundfläche ist ein Dreieck, also n = 3.', 'bild': {'flaeche': ['_A', '_B', '_C']}},
               {'text': 'Ecken: 3 vorn und 3 hinten, also 6.'},
               {'text': 'Kanten: 3 vorn, 3 hinten und 3 dazwischen, also 9.'},
               {'text': 'Flächen: 3 Rechtecke und 2 Dreiecke, zusammen ⟦5⟧.'}],
  'fehler': 'Ein Bleistift ohne Spitze hat nicht 6 Flächen. Zu den 6 Rechtecken kommen ⟦2 Grundflächen⟧, also 8.',
  'regel': 'n-Eck-Prisma: ⟦2n Ecken, 3n Kanten, n + 2 Flächen⟧. Die 2 steht für die beiden Grundflächen.'},
 'netz': {
  'einstieg': 'Schneide eine leere Müslischachtel an einigen Kanten auf und klappe sie flach. Die flache Figur heißt ⟦Netz⟧. Ihre Fläche zeigt, wie viel Pappe du brauchst.',
  'woerter': [['Netz', 'der aufgeklappte, flache Körper'], ['Oberfläche', 'alle Flächen des Körpers zusammen']],
  'bild': {'typ': 'figur', 'punkte': _NETZ, 'linien': _NETZ_L},
  'schritte': [{'text': 'Die Schachtel ist 5 cm lang, 3 cm breit und 4 cm hoch.'},
               {'text': 'Boden und Deckel: je 5 · 3 = 15 cm², zusammen 30 cm².', 'bild': {'flaeche': ['_m', '_n', '_b', '_a']}},
               {'text': 'Die vier Seiten bilden einen Streifen: 16 cm lang, 4 cm hoch: 64 cm².', 'bild': {'flaeche': ['_a', '_e', '_f', '_j']}},
               {'text': 'Oberfläche: 30 + 64 = ⟦94 cm²⟧.'}],
  'fehler': '5 · 3 · 4 = 60 ist das ⟦Volumen⟧, nicht die Netzfläche. Für das Netz addierst du die sechs Rechtecke.',
  'regel': 'Das ⟦Netz⟧ besteht aus 2 Grundflächen und einem Streifen. Der Streifen ist so lang wie der Umfang der Grundfläche.'},
 'zylinder': {
  'einstieg': 'Eine Konservendose hat oben und unten einen Kreis. Ziehst du das Etikett ab und legst es flach hin, ist es ein Rechteck. Der Körper heißt ⟦Zylinder⟧, das Etikett ist sein Mantel.',
  'woerter': [['Zylinder', 'Körper mit zwei Kreisen als Grundflächen'], ['Mantel', 'die gebogene Seitenfläche – flach ist sie ein Rechteck'], ['u', 'der Umfang des Kreises: einmal ringsum']],
  'bild': {"typ": "figur", "punkte": {"_a": [0, 0], "_b": [18.8, 0], "_c": [18.8, 10], "_d": [0, 10], "_M": [3, 13], "_N": [3, -3]},
           "linien": [["_a", "_b", "u ≈ 18,8 cm"], ["_b", "_c", "h = 10 cm"], ["_c", "_d"], ["_d", "_a"]], "kreise": [{"m": "_M", "r": 3}, {"m": "_N", "r": 3}]},
  'schritte': [{'text': 'Die Dose hat u = 18,8 cm Umfang und h = 10 cm Höhe.'},
               {'text': 'Das Etikett reicht einmal herum: Es ist 18,8 cm lang.'},
               {'text': 'Es ist so hoch wie die Dose: 10 cm.'},
               {'text': 'Mantelfläche: 18,8 cm · 10 cm = ⟦188 cm²⟧.', 'bild': {'flaeche': ['_a', '_b', '_c', '_d']}}],
  'fehler': 'Den ⟦Durchmesser⟧ statt des Umfangs nehmen ist falsch. Dann reicht das Etikett nur etwa ein Drittel herum.',
  'fehler_bild': {"punkte": {"_a": [0, 0], "_b": [6, 0], "_c": [6, 10], "_d": [0, 10], "_M": [3, 13], "_N": [3, -3]},
                  "linien": [["_a", "_b", "6 cm?"], ["_b", "_c", "h = 10 cm"], ["_c", "_d"], ["_d", "_a"]]},
  'regel': 'Der ⟦Mantel⟧ ist ein Rechteck aus Umfang mal Höhe. Dazu kommen zwei Kreise als Grundflächen.'},
 'schraegbild': {
  'einstieg': 'Eine Schachtel ist räumlich, dein Heft aber flach. Damit die Zeichnung räumlich wirkt, zeichnest du Kanten nach hinten schräg und kürzer. Das ist ein ⟦Schrägbild⟧.',
  'woerter': [['Schrägbild', 'räumlich wirkende Zeichnung eines Körpers'], ['wahrer Größe', 'genau so lang wie in echt'], ['gestrichelt', 'mit kurzen Strichen: Diese Kante ist verdeckt']],
  'bild': {'typ': 'figur', 'punkte': _Q, 'linien': _Q_L},
  'schritte': [{'text': 'Der Quader ist 6 cm breit, 4 cm hoch und 8 cm tief.'},
               {'text': 'Die Vorderfläche zeichnest du in wahrer Größe: 6 cm × 4 cm.', 'bild': {'punkte': {k: _Q[k] for k in 'ABFE'}, 'linien': _Q_L[:4]}},
               {'text': 'Nach hinten: unter 45° und halb so lang, also ⟦4 cm⟧.', 'bild': {'punkte': _Q, 'linien': _Q_L[:9] + [_Q_L[12]]}},
               {'text': 'Verdeckte Kanten zeichnest du gestrichelt.', 'bild': {'linien': _Q_L}}],
  'fehler': 'Die Kante nach hinten voll lang zeichnen ist falsch. Mit 8 statt 4 cm wirkt der Quader viel zu tief. Nur Kanten ⟦nach hinten⟧ werden verkürzt.',
  'fehler_bild': {'punkte': {**_Q, "C": [11.66, 5.66], "D": [5.66, 5.66], "G": [11.66, 9.66], "H": [5.66, 9.66]},
                  'linien': [["B", "C", "8 cm?"] if l[:2] == ["B", "C"] else (["B", "F"] if l[:2] == ["B", "F"] else l) for l in _Q_L]},
  'regel': 'Vorne ⟦wahre Größe⟧, nach hinten 45° und halb so lang. Verdeckte Kanten zeichnest du gestrichelt.'},
 'ansichten': {
  'einstieg': 'Wer ein Haus plant, zeichnet es flach von vorn, von der Seite und von oben. So erkennt man die Form genau. Diese Zeichnungen heißen ⟦Ansichten⟧.',
  'woerter': [['Ansicht', 'eine flache Zeichnung aus einer Blickrichtung'], ['Vorderansicht', 'die Ansicht von vorn'], ['Draufsicht', 'die Ansicht von oben']],
  'bild': {'typ': 'figur', 'punkte': {'_a': [0, 0], '_b': [4, 0], '_c': [4, 6], '_d': [0, 6], '_M': [8, 3]},
           'linien': [['_a', '_b', 'vorn'], ['_b', '_c'], ['_c', '_d'], ['_d', '_a']], 'kreise': [{'m': '_M', 'r': 2}]},
  'schritte': [{'text': 'Eine Dose steht auf ihrem Boden.'},
               {'text': 'Von vorn siehst du Höhe und Breite: Die Vorderansicht ist ein ⟦Rechteck⟧.',
                'bild': {'typ': 'figur', 'punkte': {'_a': [0, 0], '_b': [4, 0], '_c': [4, 6], '_d': [0, 6]}, 'flaeche': ['_a', '_b', '_c', '_d'], 'kreise': [], 'linien': [['_a', '_b', '8 cm'], ['_b', '_c', '12 cm'], ['_c', '_d'], ['_d', '_a']]}},
               {'text': 'Von der Seite sieht sie genauso aus.'},
               {'text': 'Von oben siehst du den Deckel: Die Draufsicht ist ein ⟦Kreis⟧.',
                'bild': {'typ': 'figur', 'punkte': {'_M': [0, 0], '_R': [2, 0]}, 'flaeche': [], 'linien': [['_M', '_R', 'r = 4 cm']], 'kreise': [{'m': '_M', 'r': 2}]}}],
  'fehler': 'Die Draufsicht einer stehenden Dose ist kein Rechteck. Von oben siehst du nur den ⟦Deckel⟧, einen Kreis.',
  'regel': 'Ansichten sind ⟦flache Figuren⟧. Jede zeigt den Körper aus einer Richtung: vorn, Seite, oben.'},
 'beurteilen': {
  'einstieg': 'Ist ein Würfel ein Prisma? Dafür vergleichst du ihn mit den Merkmalen eines Prismas. Fehlt ein Merkmal, ist der Körper ein ⟦Gegenbeispiel⟧.',
  'woerter': [['Merkmal', 'eine Eigenschaft, die erfüllt sein muss'], ['Gegenbeispiel', 'ein Fall, bei dem die Aussage nicht stimmt']],
  'bild': {'typ': 'figur', 'punkte': _W, 'linien': _W_L},
  'schritte': [{'text': 'Aussage: „Ein Würfel ist ein Prisma.“'},
               {'text': 'Merkmal 1: Boden und Deckel sind gleiche, parallele Quadrate. Erfüllt.', 'bild': {'flaeche': ['_E', '_F', '_G', '_H']}},
               {'text': 'Merkmal 2: Die Seiten sind Quadrate, also besondere Rechtecke. Erfüllt.', 'bild': {'flaeche': ['_A', '_B', '_F', '_E']}},
               {'text': 'Kein Merkmal fehlt. Die Aussage ist ⟦richtig⟧.'}],
  'fehler': 'Eine Pyramide ist kein Prisma, obwohl sie eine Grundfläche hat. Ihr fehlt die ⟦zweite⟧, parallele Grundfläche.',
  'fehler_bild': {'punkte': {'_A': [0, 0], '_B': [3, 0], '_C': [4.5, 1.5], '_D': [1.5, 1.5], '_S': [2.25, 4.5]}, 'flaeche': ['_A', '_B', '_C', '_D'],
                  'linien': [['_A', '_B'], ['_B', '_C'], ['_A', '_D', '', 'gestrichelt'], ['_D', '_C', '', 'gestrichelt'], ['_A', '_S'], ['_B', '_S'], ['_C', '_S'], ['_D', '_S', '', 'gestrichelt']]},
  'regel': 'Ein Prisma braucht ⟦zwei gleiche, parallele Grundflächen⟧. Die Seiten sind Rechtecke; Pyramide, Kegel und Kugel sind keine Prismen.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---- SCHWER (Zehnte Runde: schwerere Aufgaben nach Prüfungsvorbild, siehe _schwer_kl8.py) ----
# Vorbilder (Typ und Niveau, nicht Wortlaut/Zahlen): VERA-8 2025 (Ecken und Kanten eines Prismas; an welche Kante passt das letzte Quadrat eines Würfelnetzes;
# Augenzahlen am Spielwürfel), BMT8 2025 (Volumen aus einem Schrägbild; Modell im Maßstab 1 : 10 – Volumenverhältnis), BMT8 2015 (Netz und Würfel zuordnen),
# BMT8 2008 (Quader mit herausgeschnittenem Würfel), Känguru Kl. 7/8 (angemalte Würfel aus kleinen Würfeln, Würfelgebäude).
from _schwer_kl8 import Neu, mit_schwer  # noqa: E402

SW = Neu(10_8_11)

# prisma
SW.z('prisma', 2, 'Ein Prisma hat 9 Flächen. Wie viele Kanten hat es?', 21, '3 * (9 - 2)', 'n + 2 = 9 ⇔ n = 7 (siebenseitiges Prisma). Kanten: 3 · 7 = 21.',
     'Bestimme zuerst n aus der Flächenzahl n + 2.')
SW.z('prisma', 2, 'Ein Prisma hat 15 Kanten. Wie viele Ecken hat es?', 10, '2 * 15 / 3', '3n = 15 ⇔ n = 5. Ecken: 2 · 5 = 10.', 'Bestimme n aus 3n Kanten.')
SW.z('prisma', 3, 'Für ein sechsseitiges Prisma: Berechne Ecken + Flächen − Kanten.', 2, '2 * 6 + (6 + 2) - 3 * 6',
     'Ecken 12, Flächen 8, Kanten 18: 12 + 8 − 18 = 2. (Das gilt sogar für jedes Prisma: 2n + n + 2 − 3n = 2.)', 'Zähle mit den Formeln 2n, n + 2 und 3n.', art='P')
SW.z('prisma', 3, 'Ein Kantenmodell aus Draht hat die Form eines Prismas: Grundfläche ein gleichseitiges Dreieck mit 6 cm Seitenlänge, Länge 10 cm. Wie viel Draht braucht man?', 66,
     '2 * 3 * 6 + 3 * 10', 'Zwei Dreiecke: 2 · 3 · 6 cm = 36 cm. Drei Längskanten: 3 · 10 cm = 30 cm. Zusammen 66 cm.', 'Zähle die Kanten nach Sorten: Dreieckskanten und Längskanten.',
     einheit='cm', art='P')
SW.z('prisma', 3, 'Bei einem Prisma ist die Summe aus Ecken, Kanten und Flächen 62. Wie viele Ecken hat seine Grundfläche?', 10, '(62 - 2) / 6',
     '2n + 3n + (n + 2) = 6n + 2 = 62 ⇔ n = 10. Es ist ein zehnseitiges Prisma.', 'Stelle mit den drei Formeln eine Gleichung für n auf.', art='K')
SW.z('prisma', 3, 'Von einem Würfel wird eine Ecke gerade abgeschnitten, sodass dort ein kleines Dreieck entsteht. Wie viele Ecken hat der neue Körper?', 10, '8 - 1 + 3',
     'Eine Ecke fällt weg, das neue Dreieck bringt 3 neue Ecken: 8 − 1 + 3 = 10.', 'Stell dir die Schnittfläche vor: Wie viele Ecken hat sie?', art='K')

# netz
_fuenf = [(0, 0), (1, 0), (2, 0), (3, 0), (1, 1)]
_frei = sorted({(x + dx, y + dy) for x, y in _fuenf for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))} - set(_fuenf))
_passt = [z for z in _frei if falten(_fuenf + [z])]
assert len(_passt) == 4
_kreuz = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (1, 3)]
_fl = falten(_kreuz)
_zahlen = {(1, 1): 1, (0, 1): 2, (1, 0): 3}
_gegen = {_fl[z]: z for z in _kreuz}
_x = _gegen[GEGEN[_fl[(0, 1)]]]
assert _x == (2, 1)
SW.z('netz', 2, 'Ein Würfel hat die Kantenlänge 3 cm. Wie groß ist die Fläche seines Netzes?', 54, '6 * 3 * 3', 'Sechs Quadrate mit je 9 cm²: 54 cm².', 'Das Netz besteht aus 6 gleichen Quadraten.',
     einheit='cm²')
SW.z('netz', 2, 'Aus wie vielen Teilflächen besteht das Netz eines sechsseitigen Prismas?', 8, '6 + 2', '6 Rechtecke im Mantel und 2 Sechsecke als Grundflächen: 8.',
     'Mantel und Grundflächen zählen.')
SW.z('netz', 3, 'Fünf Quadrate eines Würfelnetzes sind gezeichnet. An wie viele verschiedene Stellen kann man das sechste Quadrat anlegen, sodass ein Würfelnetz entsteht?',
     len(_passt), '1 + 1 + 1 + 1',
     'Es passt nur unter die Viererreihe – an jede der 4 Stellen (Form „1-4-1“). Oben würde es mit dem schon vorhandenen Quadrat dieselbe Würfelfläche bedecken, an den Enden entsteht eine Fünferreihe.',
     'Die Viererreihe bildet den Mantel. Oben ist schon ein Deckel. Wo fehlt noch einer?', grafik=netz_bild(_fuenf), art='P')
SW.z('netz', 3, 'Aus dem Netz wird ein Spielwürfel gefaltet. Gegenüberliegende Seiten ergeben zusammen 7. Welche Zahl gehört auf das Feld X?', 7 - 2, '7 - 2',
     'Das Feld X liegt beim Falten der 2 gegenüber (links und rechts vom Mittelfeld 1). Also X = 7 − 2 = 5.', 'Welches Feld liegt dem X im Würfel gegenüber?',
     grafik=netz_bild([(1, 1), (0, 1), (1, 0), (2, 1)] + [(1, 2), (1, 3)], ['1', '2', '3', 'X', '_a', '_b']), art='P')
SW.z('netz', 3, 'Ein großer Würfel wird aus 27 kleinen Würfeln (3 × 3 × 3) gebaut und außen rot angemalt. Wie viele kleine Würfel haben genau zwei rote Flächen?', 12, '12 * 1',
     'Genau zwei rote Flächen haben die Würfel in der Mitte jeder Kante (nicht die Ecken). Ein Würfel hat 12 Kanten, an jeder liegt 1 solcher Würfel: 12.', 'Wo liegen Würfel mit zwei bemalten Seiten?', art='K')
SW.z('netz', 3, 'Ein großer Würfel aus 4 × 4 × 4 kleinen Würfeln wird außen angemalt. Wie viele kleine Würfel haben gar keine Farbe?', 8, '2**3',
     'Ungefärbt ist nur der innere Würfel, der nirgends an die Oberfläche stößt: 2 × 2 × 2 = 8.', 'Nimm von jeder Seite eine Schicht weg. Was bleibt innen?', art='K')

# zylinder
SW.z('zylinder', 2, 'Ein Zylinder hat den Radius 5 cm und die Höhe 10 cm. Wie lang ist das Mantelrechteck im Netz? (π ≈ 3,14)', 31.4, '2 * 3.14 * 5', 'Länge = Umfang = 2 · 3,14 · 5 = 31,4 cm.',
     'Das Mantelrechteck ist so lang wie der Umfang des Grundkreises.', einheit='cm')
SW.z('zylinder', 2, 'Das Mantelrechteck eines 12 cm hohen Zylinders ist 31,4 cm lang. Welchen Radius hat der Grundkreis? (π ≈ 3,14)', 5, '31.4 / (2 * 3.14)', 'u = 2πr ⇔ r = 31,4 : 6,28 = 5 cm.',
     'Die Länge des Mantels ist der Umfang.', einheit='cm')
SW.z('zylinder', 3, 'Ein Rechteck (22 cm × 15 cm) wird zu einem Zylindermantel gerollt, die 22-cm-Seite wird zum Umfang. Welchen Radius müssen die Deckel haben? (π ≈ 3,14, auf eine Nachkommastelle)',
     3.5, '22 / (2 * 3.14)', 'r = u : (2π) = 22 : 6,28 ≈ 3,5 cm.', 'Der Umfang des Deckels muss 22 cm sein.', einheit='cm', toleranz=0.1, art='P')
SW.a('zylinder', 3, 'Welches Rechteck kann der Mantel eines 7 cm hohen Zylinders mit 4 cm Durchmesser sein? (π ≈ 3,14)', '12,56 cm × 7 cm', ['4 cm × 7 cm', '25,12 cm × 7 cm', '6,28 cm × 7 cm'],
     'Länge = π · d = 3,14 · 4 = 12,56 cm, Breite = Höhe = 7 cm. 25,12 entsteht, wenn man 2π · d rechnet, 6,28 mit π · r.', 'Umfang = π · Durchmesser.', art='P')
SW.a('zylinder', 3, 'Ein Zylinder und ein Quader sind beide 10 cm hoch. Der Umfang der quadratischen Quader-Grundfläche ist so lang wie der Umfang des Zylinder-Grundkreises. Welcher Mantel ist größer?',
     'Beide Mäntel sind gleich groß.', ['der Mantel des Zylinders', 'der Mantel des Quaders', 'Das kann man ohne Zahlen nicht sagen.'],
     'Beide Mäntel sind aufgerollt Rechtecke: Umfang · Höhe. Umfang und Höhe sind gleich, also auch die Mantelflächen.', 'Wie berechnet man jeweils die Mantelfläche?', art='K')
SW.z('zylinder', 3, 'Ein Etikett liegt ohne Überlappung genau einmal um eine Dose und ist 25,12 cm lang. Die Dose ist doppelt so hoch wie breit. Wie hoch ist sie? (π ≈ 3,14)', 16, '2 * 25.12 / 3.14',
     'd = 25,12 : 3,14 = 8 cm. Doppelt so hoch wie breit: h = 16 cm.', 'Bestimme zuerst den Durchmesser aus der Etikettlänge.', einheit='cm', art='K')

# schraegbild
SW.z('schraegbild', 2, 'Ein Würfel mit 4 cm Kantenlänge wird im Schrägbild (q = 1/2, ω = 45°) gezeichnet. Wie lang zeichnest du die Kanten, die nach hinten führen?', 2, '4 / 2',
     'Nach hinten wird mit q = 1/2 verkürzt: 4 cm · 1/2 = 2 cm.', 'Nur die Kanten nach hinten werden verkürzt.', einheit='cm')
SW.z('schraegbild', 2, 'Wie viele Kanten eines Würfels werden im üblichen Schrägbild gestrichelt (verdeckt) gezeichnet?', 3, '3',
     'Verdeckt ist die hintere untere linke Ecke. Von ihr gehen 3 Kanten aus – diese werden gestrichelt.', 'Welche Ecke sieht man nicht?')
SW.z('schraegbild', 3, 'Das Schrägbild (q = 1/2, ω = 45°) zeigt einen Quader mit den gezeichneten Längen. Berechne sein wirkliches Volumen.', 192, '6 * 4 * (4 * 2)',
     'Vorne wahre Größe: 6 cm breit, 4 cm hoch. Die schräge Kante ist 4 cm gezeichnet, also 8 cm tief. V = 6 · 4 · 8 = 192 cm³ (nicht 96 cm³).',
     'Die schräge Kante ist verkürzt gezeichnet. Wie lang ist sie wirklich?', einheit='cm³', grafik=quader_schraeg(6, 4, 8, Fr(1, 2)), art='P')
SW.a('schraegbild', 3, 'Ein Schrägbild zeigt ein Modell eines Bauteils im Maßstab 1 : 10. Wie viel Mal so groß ist das Volumen des echten Bauteils?', '1 000-mal', ['10-mal', '100-mal', '30-mal'],
     'Länge, Breite und Höhe sind je 10-mal so groß: 10 · 10 · 10 = 1 000.', 'Wie viele Längen gehen in das Volumen ein?', art='P')
SW.a('schraegbild', 3, 'Jemand zeichnet einen Quader im Schrägbild mit q = 1 statt q = 1/2. Wie wirkt der gezeichnete Quader?', 'tiefer, als er wirklich ist',
     ['flacher, als er wirklich ist', 'genauso wie mit q = 1/2', 'breiter, als er wirklich ist'],
     'Mit q = 1/2 sieht die verkürzte Tiefe natürlich aus. Mit q = 1 wird die Tiefe voll gezeichnet – durch die Schräge wirkt der Körper dann zu tief.',
     'Was macht q mit den Kanten nach hinten?', art='K')
SW.z('schraegbild', 3, 'Im Schrägbild (q = 1/2, ω = 45°) eines Würfels ist eine nach hinten führende Kante 3 cm lang gezeichnet. Wie groß ist die Oberfläche des Würfels?', 216, '6 * (3 * 2)**2',
     'Wirkliche Kante: 3 cm · 2 = 6 cm. Oberfläche: 6 · 6² = 216 cm².', 'Rechne zuerst die wahre Kantenlänge aus.', einheit='cm²', art='K')

# ansichten
SW.a('ansichten', 2, 'Welche Form hat die Draufsicht eines liegenden Zylinders (Achse von links nach rechts)?', 'Rechteck', ['Kreis', 'Quadrat mit Kreis', 'Dreieck'],
     'Von oben sieht man den Zylinder der Länge nach: ein Rechteck (Länge × Durchmesser).', 'Stell dir eine liegende Dose von oben vor.')
SW.a('ansichten', 2, 'Welcher Körper hat in allen drei Ansichten (vorn, Seite, oben) einen Kreis?', 'eine Kugel', ['ein Zylinder', 'ein Kegel', 'ein Würfel'],
     'Eine Kugel sieht aus jeder Richtung gleich aus: als Kreis.', 'Welcher Körper sieht von überall gleich aus?')
SW.a('ansichten', 3, 'Ein Körper hat die Vorderansicht Rechteck, die Seitenansicht Rechteck und die Draufsicht Dreieck. Welcher Körper ist es?', 'ein stehendes dreiseitiges Prisma',
     ['eine dreiseitige Pyramide', 'ein liegendes dreiseitiges Prisma (Dreieck vorne)', 'ein Quader'],
     'Von oben ein Dreieck: Die Grundfläche ist ein Dreieck, der Körper steht. Von vorn und von der Seite sieht man Rechtecke – die Mantelflächen. Eine Pyramide hätte dort Dreiecke.',
     'Was sieht man von oben, wenn das Dreieck die Grundfläche ist?', art='P')
SW.z('ansichten', 3, 'Drei gleiche Würfel stehen in einer Reihe nebeneinander, auf dem mittleren steht ein vierter. Wie viele Quadrate siehst du in der Vorderansicht?', 4, '3 + 1',
     'Unten 3 Quadrate nebeneinander, darüber in der Mitte 1 Quadrat: 4.', 'Zeichne die Ansicht von vorn.', art='P')
SW.z('ansichten', 3, 'Ein Würfelgebäude hat in der Vorderansicht und in der Seitenansicht jeweils nur 2 Quadrate nebeneinander (eine Etage). Wie viele Würfel kann es höchstens haben?', 4, '2 * 2',
     'Eine Etage, 2 Würfel breit und 2 Würfel tief: höchstens 2 · 2 = 4 Würfel. (Mindestens 2 Würfel, schräg versetzt.)', 'Wie groß kann die Grundfläche höchstens sein?', art='K')
SW.a('ansichten', 3, 'Welcher Körper hat die Vorderansicht „Kreis“ und die Draufsicht „Quadrat“?', 'ein liegender Zylinder (Achse nach hinten), so lang wie dick',
     ['eine Kugel', 'ein stehender Zylinder', 'ein Würfel mit Kugel darin'],
     'Von vorn sieht man die runde Deckfläche. Von oben sieht man ein Rechteck aus Länge und Durchmesser – ein Quadrat, wenn beide gleich sind.',
     'Welcher Körper zeigt von vorn einen Kreis, von oben aber Ecken?', art='K')

# beurteilen
SW.a('beurteilen', 2, 'Welche Aussage ist richtig?', 'Jedes Prisma hat eine gerade Anzahl Ecken.', ['Jedes Prisma hat eine gerade Anzahl Kanten.', 'Jedes Prisma hat mindestens 6 Flächen.',
     'Ein Prisma kann 7 Ecken haben.'],
     'Ecken: 2n – immer gerade. Kanten: 3n, beim dreiseitigen Prisma 9 (ungerade). Flächen: n + 2, beim dreiseitigen nur 5.', 'Prüfe jede Aussage mit dem dreiseitigen Prisma.')
SW.a('beurteilen', 2, 'Stimmt die Aussage: „Ein Würfel ist ein besonderer Quader.“?', 'Ja, bei ihm sind alle Kanten gleich lang.', ['Nein, ein Quader hat Rechtecke als Flächen.',
     'Nein, ein Würfel hat mehr Ecken.'], 'Ein Quader hat rechteckige Flächen; Quadrate sind besondere Rechtecke. Also ist der Würfel ein Quader mit gleich langen Kanten.',
     'Ist ein Quadrat ein Rechteck?')
SW.a('beurteilen', 3, 'Lea sagt: „Jedes Netz aus 6 Quadraten lässt sich zu einem Würfel falten.“ Was stimmt?', 'Falsch: Sechs Quadrate in einer Reihe ergeben keinen Würfel.',
     ['Richtig: Ein Würfel hat 6 Flächen.', 'Richtig, wenn die Quadrate gleich groß sind.', 'Falsch: Ein Würfelnetz hat 8 Quadrate.'],
     'Ein Gegenbeispiel genügt: Bei 6 Quadraten in einer Reihe überlappen sich zwei Flächen, zwei Würfelflächen bleiben offen.', 'Suche ein Gegenbeispiel.', art='P')
SW.a('beurteilen', 3, 'Tom sagt: „Verdoppelt man alle Kanten eines Quaders, verdoppelt sich das Volumen.“ Was stimmt?', 'Falsch: Das Volumen wird 8-mal so groß.',
     ['Richtig.', 'Falsch: Das Volumen wird 4-mal so groß.', 'Falsch: Das Volumen bleibt gleich.'],
     'Länge, Breite und Höhe werden je verdoppelt: 2 · 2 · 2 = 8. Beispiel: 1 · 1 · 1 = 1, 2 · 2 · 2 = 8.', 'Probiere mit einem Würfel der Kante 1 cm.', art='P')
SW.a('beurteilen', 3, 'Gibt es ein Prisma mit genau 2 026 Kanten?', 'Nein, 2 026 ist nicht durch 3 teilbar.', ['Ja, ein 2 026-seitiges.', 'Ja, ein 1 013-seitiges.', 'Nein, so viele Kanten gibt es nicht.'],
     'Ein n-seitiges Prisma hat 3n Kanten. Die Quersumme von 2 026 ist 10 – nicht durch 3 teilbar. 2 025 oder 2 028 Kanten wären möglich.', 'Prüfe die Teilbarkeit durch 3.', art='K')
SW.a('beurteilen', 3, 'Welche Aussage über Prismen ist FALSCH?', 'Ein Prisma mit 10 Ecken hat 12 Kanten.', ['Ein Prisma mit 12 Ecken hat 18 Kanten.', 'Ein Prisma mit 8 Flächen hat 12 Ecken.',
     'Ein Prisma mit 15 Kanten hat 7 Flächen.'],
     '10 Ecken: n = 5, also 15 Kanten, nicht 12. Die anderen stimmen: n = 6 (18 Kanten, 8 Flächen, 12 Ecken) und n = 5 (15 Kanten, 7 Flächen).',
     'Bestimme in jeder Aussage zuerst n.', art='K')

baue = mit_schwer(baue, SW)
# ---- SCHWER ENDE ----

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, mit_befunden  # noqa: E402

BF = Befunde('messen.koerper_darstellung', 13_8_11)
# c) „Ein Zylinder hat genau zwei Kanten“ ist fachlich umstritten (Schulbücher: zwei gekrümmte Kanten oder keine) → Aussage vermeiden
BF.ersetze('beurteilen', 'Welche Aussage ist richtig?', BF.A(
    'Welche Aussage über Körper ist richtig?', 'Ein Zylinder hat keine Ecken.',
    ['Eine Pyramide ist ein Prisma.', 'Ein sechsseitiges Prisma hat 6 Flächen.', 'Im Schrägbild werden Kanten nach hinten in wahrer Länge gezeichnet.'],
    'Richtig: Ein Zylinder hat keine Ecken. Eine Pyramide hat keine zwei deckungsgleichen Grundflächen, ein sechsseitiges Prisma hat 6 + 2 = 8 Flächen, nach hinten laufende Kanten werden verkürzt gezeichnet.',
    'Prüfe die Eigenschaften: zwei parallele, deckungsgleiche Grundflächen; Rechtecke als Seiten.'), enthaelt='Zylinder hat genau zwei Kanten')
BF.ersetze('beurteilen', 'Welche Aussage ist FALSCH?', BF.A(
    'Welche Aussage über Prismen und Pyramiden ist FALSCH?', 'Eine Pyramide ist ein Prisma.',
    ['Der Mantel eines geraden siebenseitigen Prismas besteht aus 7 Rechtecken.', 'Ein Zylinder hat keine Ecken.', 'Ein sechsseitiges Prisma hat 12 Ecken.'],
    'Falsch: Eine Pyramide ist ein Prisma. Eine Pyramide hat nur eine Grundfläche und läuft in einer Spitze zusammen. (Sechsseitiges Prisma: 2 · 6 = 12 Ecken – richtig.)',
    'Suche ein Gegenbeispiel oder zähle nach.'), enthaelt='7 Rechtecken.", "Eine Pyramide ist ein Prisma.", "Ein Zylinder hat keine Ecken.", "Ein Zylinder hat genau zwei Kanten')
BF.ersetze('beurteilen', 'Welche Aussage ist FALSCH?', BF.A(
    'Welche Aussage über Zylinder und Prismen ist FALSCH?', 'Das Mantelrechteck eines Zylinders ist so lang wie der Durchmesser des Grundkreises.',
    ['Der Mantel eines geraden zwölfseitigen Prismas besteht aus 12 Rechtecken.', 'Ein Zylinder hat keine Ecken.', 'Ein Zylinder hat zwei kreisförmige Grundflächen.'],
    'Falsch: Das Mantelrechteck ist so lang wie der Umfang des Grundkreises (u = 2 · π · r), nicht wie der Durchmesser.',
    'Suche ein Gegenbeispiel oder zähle nach.'), enthaelt='12 Rechtecken.", "Ein Zylinder hat keine Ecken.", "Ein Zylinder hat genau zwei Kanten')
BF.nicht_umgesetzt('zylinder S2 Mantelfläche aus Umfang · Höhe (6×)', 'Kein Fehler; Übungsreihe mit verschiedenen Zahlen.')
BF.nicht_umgesetzt('netz S3 „Netz 442 cm², Grundfläche 7 × 8 cm, Höhe?“ (3×)', 'Kein Fehler; Übungsreihe (Rückwärtsrechnen) mit verschiedenen Zahlen.')
BF.nicht_umgesetzt('Überschneidung der Karten „schraegbild“ mit raum.schraegbilder', 'Betrifft den Plan (Haupt-Chat), keine einzelne Aufgabe.')

baue = mit_befunden(baue, BF)
# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Kl. 8, siehe _durchsicht_kl8.py) ----
from _durchsicht_kl8 import Durchsicht, mit_durchsicht  # noqa: E402

DSX = Durchsicht('messen.koerper_darstellung', 19_8_13)
# Gleiche Aufgabenart wie die Stufe darunter → umgestuft
DSX.stufe('schraegbild', 'Das Schrägbild (q = 1/2, ω = 45°) zeigt einen Quader. Wie tief ist der Quader in Wirklichkeit?', 2, anzahl=3)
DSX.stufe('ansichten', 'Welche Form hat die Vorderansicht – betrachtet wird ein stehender Quader mit quadratischer Grundfläche (höher als breit)?', 1)
DSX.stufe('ansichten', 'Welcher Körper hat die Vorderansicht „Dreieck“ und die Draufsicht „Quadrat“?', 2)
DSX.stufe('beurteilen', 'Welche Aussage über Zylinder und Prismen ist FALSCH?', 2)
DSX.stufe('beurteilen', 'Welche Aussage über Körper ist richtig?', 1)

DSX.stufe('beurteilen', 'Welche Aussage ist richtig?', 1, enthaelt='siebenseitiges Prisma hat 7 Flächen')
DSX.stufe('beurteilen', 'Welche Aussage ist richtig?', 1, enthaelt='Ein Würfel ist ein Prisma.', anzahl=2)
# Wiederholungen ersetzt
DSX.ersetze('prisma', 'Kann ein Prisma 37 Kanten haben?', DSX.A(
    'Ein Körper hat 12 Ecken, 18 Kanten und 8 Flächen. Kann er ein Prisma sein?',
    'Ja, ein sechsseitiges Prisma: 2 · 6 = 12 Ecken, 3 · 6 = 18 Kanten, 6 + 2 = 8 Flächen.',
    ['Nein, ein Prisma hat immer 6 Flächen.', 'Nein, 18 Kanten sind für ein Prisma zu viele.', 'Ja, ein achtseitiges Prisma.'],
    'Aus 12 Ecken folgt n = 6. Dann müssen es 3 · 6 = 18 Kanten und 6 + 2 = 8 Flächen sein – beides stimmt.',
    'Bestimme n aus den Ecken und prüfe dann Kanten und Flächen.'))
DSX.ersetze('netz', 'Das Netz eines Quaders hat die Fläche 318 cm². Die Grundfläche ist 3 cm × 9 cm. Wie hoch ist der Quader?', DSX.Z(
    'Eine Schachtel ohne Deckel hat die Form eines Quaders: 10 cm lang, 6 cm breit, 4 cm hoch. Wie viel Pappe braucht man ohne Klebelaschen?', 188, '10 * 6 + 2 * 10 * 4 + 2 * 6 * 4',
    'Boden 10 · 6 = 60 cm². Zwei lange Seiten 2 · 10 · 4 = 80 cm², zwei kurze 2 · 6 · 4 = 48 cm². Ohne Deckel: 60 + 80 + 48 = 188 cm².',
    'Zähle nur die Flächen, die es wirklich gibt – der Deckel fehlt.', einheit='cm²'))
DSX.ersetze('zylinder', 'Eine Dose hat den Durchmesser 7,5 cm und ist 11 cm hoch. Das Etikett überlappt 1 cm. Wie lang muss es sein? (π ≈ 3,14, auf eine Nachkommastelle runden)', DSX.A(
    'Dose B hat den doppelten Durchmesser von Dose A, ist aber nur halb so hoch. Was gilt für ihre Etiketten (Mantelflächen)?',
    'Beide sind gleich groß.', ['Das Etikett von B ist doppelt so groß.', 'Das Etikett von B ist halb so groß.', 'Das Etikett von B ist viermal so groß.'],
    'Doppelter Durchmesser heißt doppelter Umfang, also doppelt so langes Rechteck. Halbe Höhe heißt halb so hoch. 2 · ½ = 1: gleich groß.',
    'Mantel = Umfang mal Höhe. Wie ändern sich beide Faktoren?'))
DSX.ersetze('ansichten', 'Welcher Körper hat die Vorderansicht „Rechteck“ und die Draufsicht „Kreis“?', DSX.A(
    'Welche Form hat die Seitenansicht eines liegenden Zylinders (Achse von links nach rechts)?',
    'Kreis', ['Rechteck', 'Dreieck', 'Quadrat'],
    'Von der Seite schaust du genau auf einen der beiden Grundkreise.', 'Wohin zeigt die Achse, wenn du von der Seite schaust?'),
    enthaelt='Ein dreiseitiges Prisma, das auf einer R')
DSX.ersetze('beurteilen', 'Welche Aussage ist FALSCH?', DSX.A(
    'Stimmt die Aussage: „Ein Zylinder ist ein Prisma.“?',
    'Nein: Seine Grundflächen sind Kreise, keine Vielecke.',
    ['Ja, er hat zwei gleiche, parallele Grundflächen.', 'Ja, weil sein Mantel ein Rechteck ist.', 'Nein, weil er gar keine Grundfläche hat.'],
    'Ein Prisma hat zwei gleiche, parallele Vielecke als Grundflächen und Rechtecke als Seiten. Der Zylinder hat Kreise und keine Kanten an der Seite.',
    'Vergleiche mit allen Merkmalen eines Prismas.'), enthaelt='dreiseitigen Prismas besteht aus 3')
DSX.stufen('prisma', 'S3 zweimal dieselbe Frage „Kann ein Prisma … Kanten haben?“', 'S1 Anzahl berechnen; S2 rückwärts von Kanten/Ecken auf n; S3 unmögliche Zahlen begründen, Zahlen prüfen, Kantenlänge, Euler, abgeschnittene Ecke')
DSX.stufen('netz', 'S3 dreimal Höhe aus der Netzfläche', 'S1 Netzfläche Quader, Spielwürfel; S2 Würfelnetze prüfen, Prisma-Netz; S3 Höhe rückwärts, Schachtel ohne Deckel, Gegenfläche, angemalte Würfel')
DSX.stufen('zylinder', 'S3 zweimal Etikett mit Überlappung', 'S1 Teile des Netzes; S2 Mantel = U · h, Radius rückwärts; S3 ganze Netzfläche, Überlappung, Rechteck rollen, Durchmesser und Höhe gegeneinander')
DSX.stufen('schraegbild', 'S2 und S3 dieselbe Rückwärtsrechnung', 'S1 Länge zeichnen; S2 wahre Länge rückwärts, auch aus dem Bild, verdeckte Kanten; S3 anderes q, Volumen und Oberfläche aus dem Bild, Maßstab, Fehler q = 1')
DSX.stufen('ansichten', 'S1/S2 und S2/S3 teils dieselbe Frage; zweimal dieselbe Frage in Folge', 'S1 Ansicht eines Körpers; S2 Körper aus zwei Ansichten, liegender Zylinder; S3 zusammengesetzte Körper, Würfelgebäude, Kreis-über-Quadrat-Rätsel')
DSX.stufen('beurteilen', 'S1 und S2 dieselbe Frage „Welche Aussage ist richtig?“; S2 zweimal dieselbe Falsch-Aussage', 'S1 richtige Aussage wählen; S2 Falsch-Aussage finden, Zylinder als Prisma, Würfel als Quader; S3 Behauptungen anderer prüfen, 2 026 Kanten, verdoppelte Kanten')
baue = mit_durchsicht(baue, DSX)
# ---- DURCHSICHT ENDE ----

# ---- STUFEN (Zwanzigste Runde: echte Stufe 3 und Knobel-Bordkarten, siehe _stufen_kl8.py) ----
from _stufen_kl8 import Stufen, mit_stufen  # noqa: E402

ST = Stufen('messen.koerper_darstellung', 20_8_10)
SA, SZ, SL = ST.A, ST.Z, ST.L
def T(lz, *regeln):
    for m, g in regeln: ST.typ(lz, m, g)

# --- prisma ---
ST.leiter('prisma', 'Ecken, Kanten und Flächen eines n-seitigen Prismas zählen',
          'rückwärts von Kanten/Ecken auf n, Kanten aus Flächen, Sachkörper (Zelt)',
          'unmögliche Zahlen begründen, Zahlen prüfen, Kantenlängen verknüpfen, Euler, abgeschnittene Ecke, n aus einer Summe')
T('prisma', (r'Summe', 'pruefung'), (r'^Wie viele (Kanten|Flächen) hat ein', 'direkt'), (r'Wie viele Ecken hat seine Grundfläche\?$', 'umkehr'), (r'^Ein Prisma hat \d+ (Flächen|Kanten)\. Wie viele (Kanten|Ecken) hat es', 'mehrschritt'),
  (r'^Kann ein Prisma', 'begruenden'), (r'12 Ecken, 18 Kanten', 'rueckwaerts'), (r'Seitenlänge|Draht', 'verknuepfen'), (r'Ecken \+ Flächen − Kanten|abgeschnitten', 'transfer'),
  (r'Summe', 'pruefung'))
ST.neu('prisma', 'erkennen', SA('Welcher Körper ist ein Prisma?', 'eine quaderförmige Schachtel', ['ein Kegel', 'eine Pyramide', 'eine Kugel'], 'Ein Quader hat zwei gleiche, parallele Grundflächen und Rechtecke als Seiten.', 'Ein Prisma hat zwei gleiche, parallele Grundflächen.'))
ST.neu('prisma', 'einkleidung', SZ('Ein Zelt hat die Form eines dreiseitigen Prismas. Jede Kante ist eine Stange. Wie viele Stangen braucht man?', 9, '3 * 3', 'Ein dreiseitiges Prisma hat 3 · 3 = 9 Kanten.', 'Kanten eines n-seitigen Prismas: 3n.'))
ST.knobel('prisma', SZ('Ein Prisma hat Ecken und Flächen zusammen 50. Wie viele Kanten hat es?', 48, '3 * 16',
    'Für ein n-seitiges Prisma: Ecken 2n, Flächen n + 2. 2n + n + 2 = 50 ⇒ n = 16. Kanten 3n = 48.', 'Schreibe Ecken und Flächen mit n.'))
ST.knobel('prisma', SZ('Von jeder der 8 Ecken eines Würfels wird eine kleine Ecke gerade abgeschnitten. Wie viele Kanten hat der neue Körper?', 36, '12 + 8 * 3',
    'Die 12 alten Kanten bleiben (kürzer) erhalten. An jeder abgeschnittenen Ecke entsteht ein Dreieck mit 3 neuen Kanten: 12 + 8 · 3 = 36.', 'Was entsteht an jeder abgeschnittenen Ecke?'))

# --- netz ---
ST.leiter('netz', 'Netzfläche eines Quaders berechnen, Gegenflächen am Spielwürfel',
          'Würfelnetze prüfen, Prismen-Netz mit Dreieck, Geschenkpapier, Kante aus der Netzfläche',
          'Höhe rückwärts, Schachtel ohne Deckel, Gegenflächen im Netz, sechstes Quadrat, angemalte Würfel')
T('netz', (r'Spielwürfel ergeben|Teilflächen', 'erkennen'), (r'^Ein Quader ist|^Ein Würfel hat die Kantenlänge', 'direkt'), (r'Lässt sich das Netz', 'darstellung'),
  (r'rechtwinkliges Dreieck', 'mehrschritt'), (r'Das Netz eines Quaders hat die Fläche', 'rueckwaerts'), (r'ohne Deckel|gegenüber\?|27 kleinen', 'transfer'),
  (r'sechste Quadrat', 'begruenden'), (r'Feld X', 'pruefung'), (r'4 × 4 × 4', 'verknuepfen'))
ST.neu('netz', 'einkleidung', SZ('Ein Geschenkkarton (Quader 30 cm × 20 cm × 10 cm) wird vollständig mit Papier beklebt. Wie viel Papier braucht man ohne Überlappung?', 2200, '2 * (30 * 20 + 30 * 10 + 20 * 10)',
    '2 · (600 + 300 + 200) = 2 200 cm².', 'Je zwei gleiche Rechtecke.', einheit='cm²'))
ST.neu('netz', 'umkehr', SZ('Ein Würfelnetz hat die Fläche 96 cm². Wie lang ist eine Kante?', 4, '4', '6 Quadrate: 96 : 6 = 16 cm² je Quadrat, Kante 4 cm.', 'Teile durch die Anzahl der Quadrate.', einheit='cm'))
ST.knobel('netz', SZ('Ein Würfel aus 5 × 5 × 5 kleinen Würfeln wird außen angemalt. Wie viele kleine Würfel haben genau eine bemalte Fläche?', 54, '6 * 3 * 3',
    'Genau eine Fläche bemalt haben die Würfel in der Mitte jeder Außenfläche, ohne Rand: 3 × 3 = 9 je Fläche. 6 Flächen: 54.', 'Welche Würfel einer Außenfläche liegen nicht an einer Kante?'))
ST.knobel('netz', SZ('Ein Quader hat die Kanten 1 cm, 3 cm und c cm; seine Netzfläche ist 62 cm². Bestimme c.', 7, '(62 / 2 - 3) / 4',
    'Netzfläche 2 · (1 · 3 + 1 · c + 3 · c) = 2 · (3 + 4c) = 62 ⇒ 3 + 4c = 31 ⇒ c = 7.', 'Stelle die Netzfläche mit c auf.', einheit='cm'))

# --- zylinder ---
ST.leiter('zylinder', 'die Teile eines Zylindernetzes benennen, Länge des Mantelrechtecks angeben',
          'Mantelfläche = Umfang · Höhe, Radius aus der Mantellänge, Litfaßsäule',
          'ganze Netzfläche, Überlappung, Rechteck rollen, Mantel-Vergleiche begründen, Fehler (Durchmesser statt Umfang), Prüfungsaufgabe')
T('zylinder', (r'Aus welchen Flächen|Teilflächen', 'erkennen'), (r'Wie lang ist das Mantelrechteck im Netz\?$', 'direkt'), (r'Wie groß ist die Mantelfläche', 'mehrschritt'),
  (r'Radius 5 cm und die Höhe 10', 'mehrschritt'), (r'Welchen Radius hat der Grundkreis|Welchen Umfang hat', 'umkehr'), (r'gesamte Netzfläche', 'verknuepfen'),
  (r'überlappt', 'transfer'), (r'Dose B|Quader sind beide', 'begruenden'), (r'gerollt|doppelt so hoch', 'rueckwaerts'), (r'Welches Rechteck', 'pruefung'))
ST.neu('zylinder', 'einkleidung', SZ('Eine Litfaßsäule ist 3 m hoch, ihr Umfang ist 4 m. Wie viel m² Werbefläche bietet ihr Mantel?', 12, '4 * 3', 'Mantel = Umfang · Höhe = 4 · 3 = 12 m².', 'Das abgerollte Plakat ist ein Rechteck.', einheit='m²'))
ST.neu('zylinder', 'fehler', SA('Jemand berechnet die Mantelfläche eines Zylinders mit d = 4 cm und h = 10 cm als 4 · 10 = 40 cm². Was ist falsch?', 'Er hat den Durchmesser statt des Umfangs genommen; richtig ist etwa 12,56 · 10 = 125,6 cm².',
    ['Nichts.', 'Er hätte den Radius nehmen müssen: 20 cm².', 'Er hätte 4 · 4 · 10 rechnen müssen.'], 'Die Länge des Mantelrechtecks ist der Umfang u = π · d ≈ 12,56 cm.', 'Wie lang ist das Rechteck, das um die Dose reicht?'))
ST.knobel('zylinder', SZ('Ein Blatt (21 cm × 29,7 cm) wird einmal zu einer hohen, einmal zu einer flachen Röhre gerollt (ohne Überlappung). Wie viel Mal so groß ist die Mantelfläche der hohen Röhre wie die der flachen?', 1, '1',
    'In beiden Fällen ist der Mantel genau das Blatt: 21 · 29,7 cm². Die Mantelflächen sind gleich, der Faktor ist 1 – nur die Volumen unterscheiden sich.', 'Woraus besteht der Mantel?'))
ST.knobel('zylinder', SZ('Ein Etikett von 18,84 cm Länge passt genau einmal um eine Dose (π ≈ 3,14). Wie viele solche Dosen passen nebeneinander in eine Reihe auf ein 60 cm langes Brett?', 10, '60 / (1884/100 / (314/100))',
    'u = π · d ⇒ d = 18,84 : 3,14 = 6 cm. 60 : 6 = 10 Dosen.', 'Bestimme aus dem Umfang den Durchmesser.'))

# --- schraegbild ---
ST.leiter('schraegbild', 'Kanten nach hinten mit q = 1/2 verkürzt zeichnen, wahre Längen vorne erkennen',
          'wahre Länge rückwärts, Parallelogramme und verdeckte Kanten erkennen, Würfel zeichnen',
          'anderes q, Volumen/Oberfläche aus dem Bild, Maßstab, Fehler q = 1, Verkürzung begründen, q bestimmen')
T('schraegbild', (r'die Breite\?$', 'erkennen'), (r'^Eine Kante führt', 'direkt'), (r'Wie lang ist sie in Wirklichkeit|Wie tief ist der Quader in Wirklichkeit', 'umkehr'),
  (r'Parallelogramm|verkürzt gezeichnet|gestrichelt', 'darstellung'), (r'Würfel mit 4 cm', 'mehrschritt'), (r'q = 3/4', 'transfer'), (r'Volumen|Maßstab', 'verknuepfen'),
  (r'q = 1 statt', 'fehler'), (r'Oberfläche', 'pruefung'))
ST.neu('schraegbild', 'erkennen', SA('Welche Kanten eines Quaders zeichnet man im Schrägbild in wahrer Länge?', 'die Kanten der Vorderfläche', ['die Kanten nach hinten', 'alle Kanten', 'keine Kante'],
    'Die Vorderfläche liegt parallel zur Zeichenebene und wird unverändert gezeichnet. Nur Kanten nach hinten werden verkürzt.', 'Welche Fläche liegt parallel zum Blatt?'))
ST.neu('schraegbild', 'begruenden', SA('Warum zeichnet man im Schrägbild die Kanten nach hinten verkürzt?', 'Damit die Zeichnung räumlich wirkt – voll lang sähe der Körper zu tief aus.',
    ['Damit die Zeichnung aufs Blatt passt.', 'Weil Kanten nach hinten wirklich kürzer sind.', 'Das ist nur bei Würfeln so.'], 'Das Auge schätzt nach hinten führende Strecken kürzer ein. Die echte Länge ändert sich nicht.', 'Sind die Kanten in Wirklichkeit kürzer?'))
ST.neu('schraegbild', 'parameter', SZ('Eine 12 cm lange Kante nach hinten ist im Schrägbild 9 cm lang gezeichnet. Welcher Verkürzungsfaktor q wurde benutzt? Gib ihn als Dezimalzahl an.', 0.75, '9 / 12', 'q = gezeichnet : wirklich = 9 : 12 = 0,75.', 'Teile die gezeichnete durch die wirkliche Länge.'))
ST.neu('schraegbild', 'rueckwaerts', SZ('Im Schrägbild (q = 1/2) eines Quaders sind Breite 6 cm, Höhe 4 cm und die Kante nach hinten 1,5 cm gezeichnet. Wie groß ist die Oberfläche des echten Quaders?', 108, '2 * (6 * 4 + 6 * 3 + 4 * 3)',
    'Echte Tiefe 3 cm. O = 2 · (24 + 18 + 12) = 108 cm².', 'Rechne zuerst die echte Tiefe aus.', einheit='cm²'))
ST.knobel('schraegbild', SZ('Ein Würfel wird mit q = 1/2 gezeichnet, die Kanten nach hinten sind 2,5 cm lang. Wie viele solche Würfel passen in einen Karton von 50 cm × 50 cm × 50 cm?', 1000, '(50 / 5)**3',
    'Echte Kante 5 cm. In jede Richtung passen 50 : 5 = 10 Würfel: 10 · 10 · 10 = 1 000.', 'Wie lang ist die Würfelkante wirklich?'))
ST.knobel('schraegbild', SZ('Im Schrägbild (q = 1/2) sind alle 12 Kanten eines Quaders zusammen 34 cm lang gezeichnet. Er ist 4 cm breit und 3 cm hoch. Wie tief ist er wirklich?', 3, '(34 - 16 - 12) / 2',
    'Gezeichnet: 4 Breiten (16 cm) + 4 Höhen (12 cm) + 4 halbe Tiefen = 2t. 28 + 2t = 34 ⇒ t = 3 cm.', 'Welche Kanten sind verkürzt, welche nicht?', einheit='cm'))

# --- ansichten ---
ST.leiter('ansichten', 'die Vorder- oder Draufsicht eines einfachen Körpers nennen',
          'aus zwei Ansichten auf den Körper schließen, liegende Körper, Sachkörper (Turm)',
          'zusammengesetzte Körper verknüpfen, Körper aus drei Ansichten, Würfelgebäude zählen, Ansichten verwechseln als Fehler')
T('ansichten', (r'^Welche Form hat die (Vorderansicht|Draufsicht) –', 'erkennen'), (r'^Welcher Körper hat die Vorderansicht „Kreis“', 'transfer'), (r'^Welcher Körper hat', 'umkehr'),
  (r'liegenden Zylinders', 'darstellung'), (r'Bleistift|Pyramide mit derselben|liegt quer', 'verknuepfen'), (r'Seitenansicht Rechteck und die Draufsicht Dreieck', 'rueckwaerts'),
  (r'in einer Reihe', 'transfer'), (r'Würfelgebäude', 'pruefung'))
ST.neu('ansichten', 'direkt', SA('Welche Form hat die Draufsicht eines Würfels?', 'Quadrat', ['Rechteck', 'Kreis', 'Dreieck'], 'Von oben sieht man eine Würfelfläche – ein Quadrat.', 'Welche Fläche sieht man von oben?'))
ST.neu('ansichten', 'einkleidung', SA('Ein runder Turm hat ein kegelförmiges Dach. Wie sieht er von oben aus?', 'ein Kreis (die Spitze in der Mitte)', ['ein Dreieck', 'ein Rechteck mit Dreieck', 'ein Quadrat'],
    'Von oben sieht man nur den kreisförmigen Umriss; die Dachspitze liegt über der Mitte.', 'Welche Form hat der Turm im Querschnitt?'))
ST.neu('ansichten', 'fehler', SA('Jemand zeichnet als Vorderansicht einer stehenden Dose einen Kreis. Was ist falsch?', 'Von vorn sieht man ein Rechteck; der Kreis ist die Draufsicht.',
    ['Nichts.', 'Von vorn sieht man ein Dreieck.', 'Von vorn sieht man zwei Kreise.'], 'Eine stehende Dose sieht man von vorn als Rechteck (Höhe × Durchmesser).', 'Von wo sieht man die Kreisfläche?'))
ST.knobel('ansichten', SZ('Ein einstöckiges Würfelgebäude zeigt von vorn 3 Quadrate nebeneinander und von der Seite 2 Quadrate nebeneinander. Wie viele Würfel hat es mindestens?', 3, '3',
    'Die Würfel stehen in einem 3 × 2-Raster. Jede der 3 Spalten (Vorderansicht) und jede der 2 Reihen (Seitenansicht) braucht mindestens einen Würfel. Mit 3 Würfeln geht es, etwa diagonal versetzt: Spalten 1, 2, 3 in den Reihen 1, 2, 2.',
    'Welche Stellen müssen von vorn und von der Seite besetzt sein?'))
ST.knobel('ansichten', SZ('Ein Körper aus Einheitswürfeln passt in ein 2 × 2 × 2-Raster und sieht von vorn, von der Seite und von oben jeweils wie ein volles 2 × 2-Quadrat aus. Wie viele Würfel hat er mindestens?', 4, '4',
    'Jede Ansicht braucht 4 besetzte Felder; ein Würfel deckt in jeder Ansicht genau ein Feld. Mit 4 Würfeln geht es: unten links-vorn und rechts-hinten, oben rechts-vorn und links-hinten. Mit 3 Würfeln wären in der Draufsicht höchstens 3 Felder voll.',
    'Wie viele Felder kann ein Würfel in einer Ansicht abdecken?'))

# --- beurteilen ---
ST.leiter('beurteilen', 'eine richtige Aussage über Körper erkennen',
          'die falsche Aussage finden, Aussagen zu Netz, Verpackung und Kantenlängen prüfen',
          'Prisma-Definition begründen, Behauptungen anderer widerlegen, Volumen bei verdoppelten Kanten, 2 026 Kanten, falsche Aussagen in Prüfungsform')
T('beurteilen', (r'Welche Aussage (über Körper )?ist richtig\?$', 'erkennen'), (r'besonderer Quader', 'direkt'), (r'Zylinder und Prismen ist FALSCH|^Welche Aussage ist FALSCH\?$', 'umkehr'),
  (r'Zylinder ist ein Prisma|^Lea', 'begruenden'), (r'Prismen und Pyramiden ist FALSCH|^Welche Aussage über Prismen ist FALSCH', 'fehler'), (r'^Tom', 'verknuepfen'), (r'2 026', 'transfer'))
ST.neu('beurteilen', 'einkleidung', SA('Ein Schokoriegel hat die Form eines dreiseitigen Prismas. Welche Aussage über seine Verpackung stimmt?', 'Sie besteht aus 2 Dreiecken und 3 Rechtecken.',
    ['Sie besteht aus 3 Dreiecken und 2 Rechtecken.', 'Sie besteht aus 6 Rechtecken.', 'Sie besteht aus 2 Dreiecken und 2 Rechtecken.'], 'Zwei dreieckige Grundflächen, für jede Dreiecksseite ein Rechteck.', 'Wie viele Seitenflächen hat ein dreiseitiges Prisma?'))
ST.neu('beurteilen', 'darstellung', SA('Ein Netz besteht aus 2 Sechsecken und 6 Rechtecken. Welche Aussage über den gefalteten Körper stimmt?', 'Es ist ein sechsseitiges Prisma mit 12 Ecken.',
    ['Es ist eine sechsseitige Pyramide.', 'Es ist ein Prisma mit 6 Ecken.', 'Es ist ein Würfel.'], 'Zwei gleiche Grundflächen und Rechtecke: Prisma. n = 6, also 2n = 12 Ecken.', 'Welche Körper haben zwei gleiche Grundflächen?'))
ST.neu('beurteilen', 'mehrschritt', SA('Welche Aussage über ein fünfseitiges Prisma ist richtig?', 'Es hat 10 Ecken, 15 Kanten und 7 Flächen.',
    ['Es hat 5 Ecken, 10 Kanten und 7 Flächen.', 'Es hat 10 Ecken, 10 Kanten und 7 Flächen.', 'Es hat 10 Ecken, 15 Kanten und 5 Flächen.'], 'n = 5: 2n = 10 Ecken, 3n = 15 Kanten, n + 2 = 7 Flächen.', 'Prüfe alle drei Zahlen.'))
ST.neu('beurteilen', 'mehrschritt', SA('Welche Aussage über einen Würfel mit 3 cm Kantenlänge stimmt?', 'Seine Kanten sind zusammen 36 cm lang.', ['Seine Kanten sind zusammen 18 cm lang.', 'Seine Oberfläche ist 27 cm².', 'Er hat 6 Ecken.'],
    '12 Kanten · 3 cm = 36 cm. Oberfläche 6 · 9 = 54 cm², 8 Ecken.', 'Wie viele Kanten hat ein Würfel?'))
ST.neu('beurteilen', 'pruefung', SA('Ein Prisma hat 21 Kanten. Welche Aussage stimmt?', 'Es hat 14 Ecken und 9 Flächen.', ['Es hat 7 Ecken und 9 Flächen.', 'Es hat 14 Ecken und 7 Flächen.', 'Es hat 21 Ecken und 9 Flächen.'],
    '3n = 21 ⇒ n = 7. Ecken 2n = 14, Flächen n + 2 = 9.', 'Bestimme zuerst n aus der Kantenzahl.'))
ST.neu('beurteilen', 'parameter', SA('Für welche n stimmt: „Ein n-seitiges Prisma hat mehr Kanten als eine n-seitige Pyramide Ecken“?', 'für alle n ≥ 3', ['nur für n > 5', 'für kein n', 'nur für gerade n'],
    'Prisma: 3n Kanten, Pyramide: n + 1 Ecken. 3n > n + 1 gilt für alle n ≥ 1, also für jedes Prisma.', 'Vergleiche 3n mit n + 1.'))
ST.knobel('beurteilen', SA('Welche Zahl kann die Kantenzahl einer Pyramide, aber nicht die eines Prismas sein?', '8', ['9', '15', '12'],
    'Prismen haben 3n Kanten (9, 12, 15 …), Pyramiden 2n Kanten (6, 8, 10, 12 …). 8 ist gerade, aber nicht durch 3 teilbar. 12 geht bei beiden, 9 und 15 nur beim Prisma.', 'Stelle beide Kantenformeln auf.'))
ST.knobel('beurteilen', SZ('Ein Prisma und eine Pyramide haben dieselbe n-eckige Grundfläche und zusammen 35 Kanten. Bestimme n.', 7, '35 / 5',
    'Prisma 3n Kanten, Pyramide 2n Kanten: 5n = 35 ⇒ n = 7.', 'Addiere die Kantenformeln.'))
baue = mit_stufen(baue, ST)
# ---- STUFEN ENDE ----

# ---------- TEXT: Zweiundzwanzigste Runde (18.11., Auftrag des Lehrers) – mehr Textaufgaben, siehe _text_kl8.py ----------
from _text_kl8 import Text, mit_text, text_auf_datei  # noqa: E402
TX = Text('messen.koerper_darstellung', 22_8_10)
TZ, TA, TL, TW = TX.Z, TX.A, TX.L, TX.W

TX.huerde_alt('netz', r'Eine Schachtel ohne Deckel hat die Form eines Quaders', 'fehlend')

# --- prisma ---
TX.u('prisma', 'direkt', TZ('Ein Zelt hat die Form eines dreiseitigen Prismas, auch der Boden ist aus Stoff. Aus wie vielen Stoffflächen besteht das Zelt?', '3 + 2',
    TW('dreiseitiges Prisma, n = 3.', 'Anzahl der Flächen.', 'n Seitenflächen + 2 Grundflächen.', '3 + 2 = 5.', 'Das Zelt hat 5 Stoffflächen.'), 'Zähle die Seitenflächen und die beiden Dreiecke.'))
TX.u('prisma', 'einkleidung', TZ('Ein Bleistift ohne Spitze ist ein sechsseitiges Prisma. Wie viele Kanten hat er?', '3 * 6',
    TW('n = 6.', 'Anzahl der Kanten.', 'Kanten = 3 · n (vorn, hinten, dazwischen).', '3 · 6 = 18.', 'Er hat 18 Kanten.'), 'Wie viele Kanten liegen vorn, hinten und dazwischen?'))
TX.u('prisma', 'mehrschritt', TZ('Für ein Kantenmodell eines achtseitigen Prismas braucht man für jede Kante einen Holzstab und für jede Ecke eine Knetkugel. Wie viele Teile braucht man zusammen?', '3 * 8 + 2 * 8',
    TW('n = 8.', 'Stäbe + Kugeln.', 'Kanten = 3n, Ecken = 2n.', '24 + 16 = 40.', 'Man braucht 40 Teile.'), 'Wie viele Kanten und wie viele Ecken hat das Prisma?'))
TX.u('prisma', 'pruefung', TZ('Ein Pavillon ist ein sechsseitiges Prisma: sechseckiger Boden und flaches sechseckiges Dach, jede Kante am Boden ist 2 m lang, er ist 3 m hoch und kostet 1 200 €. An alle Kanten kommt eine Lichterkette. Wie viele Meter braucht man?',
    '6 * 2 + 6 * 2 + 6 * 3', TW('n = 6, Kanten am Boden und am Dach je 2 m, senkrechte Kanten 3 m. Der Preis spielt keine Rolle.', 'Gesamtlänge aller Kanten.', '6 Kanten unten + 6 oben + 6 senkrecht.',
    '12 + 12 + 18 = 42.', 'Man braucht 42 m Lichterkette.'), 'Welche Kanten gibt es, und wie lang ist jede Sorte?', einheit='m'), huerde='ueberfluessig')
TX.u('prisma', 'begruenden', TX.A('Ein Bastelset enthält 15 Holzstäbe für die Kanten und 10 Knetkugeln für die Ecken. Reicht es für ein Kantenmodell eines fünfseitigen Prismas?',
    'Ja, genau: 15 Kanten und 10 Ecken.', ['Nein, es fehlen 5 Stäbe.', 'Nein, es fehlen 2 Kugeln für die Grundflächen.', 'Ja, und es bleiben 5 Stäbe übrig.'],
    TW('15 Stäbe, 10 Kugeln, n = 5.', 'Reicht das Set?', 'Kanten = 3n, Ecken = 2n vergleichen.', '3 · 5 = 15, 2 · 5 = 10.', 'Es reicht genau.'), 'Berechne Kanten und Ecken des Prismas.'), huerde='entscheidung')
TX.s('prisma', TZ('Eine Geschenkverpackung hat die Form eines vierseitigen Prismas. Wie viele Ecken hat sie?', '2 * 4',
    TW('n = 4.', 'Ecken.', 'Ecken = 2n.', '2 · 4 = 8.', 'Sie hat 8 Ecken.')))
TX.s('prisma', TZ('Eine Säule auf einem Spielplatz ist ein achtseitiges Prisma. Wie viele Seitenflächen hat sie ohne Boden und Deckel?', '8',
    TW('n = 8.', 'Seitenflächen.', 'Je Kante der Grundfläche eine Seitenfläche.', 'n = 8.', 'Sie hat 8 Seitenflächen.')))
TX.k('prisma', TZ('Ein Turm aus Pappe ist ein fünfseitiges Prisma. Alle Kanten sollen mit Farbe nachgezogen werden. Wie viele Kanten sind das?', '3 * 5',
    TW('n = 5.', 'Kanten.', 'Kanten = 3n.', '3 · 5 = 15.', 'Es sind 15 Kanten.')))

# --- netz ---
TX.u('netz', 'direkt', TZ('Ein würfelförmiger Karton mit 5 cm Kantenlänge wird aufgeschnitten und flach gelegt. Wie groß ist die Fläche seines Netzes?', '6 * 5**2',
    TW('Würfel a = 5 cm.', 'Fläche des Netzes.', '6 gleiche Quadrate.', '6 · 25 = 150.', 'Das Netz hat 150 cm².'), 'Aus welchen Flächen besteht das Netz eines Würfels?', einheit='cm²'))
TX.u('netz', 'einkleidung', TZ('Eine Müslischachtel ist 20 cm breit, 7 cm tief und 30 cm hoch. Wie viel cm² Karton hat ihr Netz ohne Klebelaschen?', '2 * (20 * 7 + 20 * 30 + 7 * 30)',
    TW('Quader 20 · 7 · 30 cm.', 'Fläche des Netzes.', 'Je zwei gleiche Rechtecke: 2 · (ab + ac + bc).', '2 · (140 + 600 + 210) = 1 900.', 'Das Netz hat 1 900 cm².'), 'Welche drei Rechtecke kommen je zweimal vor?', einheit='cm²'))
TX.u('netz', 'umkehr', TZ('Das Netz eines würfelförmigen Geschenkkartons hat 216 cm². Wie lang ist eine Kante?', '6',
    TW('Netzfläche 216 cm², Würfel.', 'Kantenlänge a.', '216 : 6 = Fläche eines Quadrats, dann die Seite.', '216 : 6 = 36 cm²; 6 · 6 = 36.', 'Eine Kante ist 6 cm lang.'), 'Wie groß ist eine der sechs Flächen?', einheit='cm'))
TX.u('netz', 'pruefung', TZ('Für 30 würfelförmige Geschenkboxen mit 8 cm Kantenlänge wird Karton gekauft. Ein Bogen hat 0,25 m², für Klebelaschen rechnet man 10 % dazu. Wie viele Bögen muss man kaufen?', '-(-(30 * 6 * 8**2 * 11 / 10) // 2500)',
    TW('30 Würfel, a = 8 cm, +10 %, Bogen 0,25 m² = 2 500 cm².', 'Anzahl der Bögen.', 'Netzfläche · 30 · 1,1, durch 2 500, aufrunden.', '6 · 64 = 384 cm². · 30 = 11 520 cm². · 1,1 = 12 672 cm². : 2 500 ≈ 5,07.', 'Man muss 6 Bögen kaufen.'),
    'Rechne erst eine Box, dann alle, dann die Bögen – und was machst du mit 5,07?'), huerde='deuten')
TX.s('netz', TZ('Ein Umzugskarton (Quader 40 cm × 30 cm × 20 cm) wird ringsum mit Folie beklebt. Wie viel cm² Folie braucht man ohne Überlappung?', '2 * (40 * 30 + 40 * 20 + 30 * 20)',
    TW('Quader 40 · 30 · 20 cm.', 'Folienfläche.', 'O = 2 · (ab + ac + bc).', '2 · (1 200 + 800 + 600) = 5 200.', 'Man braucht 5 200 cm².'), einheit='cm²'))
TX.s('netz', TZ('Eine oben offene Holzkiste ist 50 cm lang, 40 cm breit und 30 cm hoch. Wie viel cm² Holz hat sie?', '50 * 40 + 2 * 50 * 30 + 2 * 40 * 30',
    TW('50 · 40 · 30 cm, ohne Deckel.', 'Holzfläche.', 'Boden + vier Seiten.', '2 000 + 3 000 + 2 400 = 7 400.', 'Die Kiste hat 7 400 cm² Holz.'), einheit='cm²'))
TX.k('netz', TZ('Ein würfelförmiger Hocker mit 40 cm Kante wird ringsum gepolstert, nur die Unterseite nicht. Wie viel cm² Stoff braucht man?', '5 * 40**2',
    TW('Würfel a = 40 cm, 5 Flächen.', 'Stofffläche.', '5 · a².', '5 · 1 600 = 8 000.', 'Man braucht 8 000 cm² Stoff.'), einheit='cm²'))

# --- zylinder ---
TX.u('zylinder', 'direkt', TZ('Eine Dose ist 11 cm hoch, ihr Umfang ist 25 cm. Wie groß ist ein Etikett, das den Mantel genau bedeckt?', '25 * 11',
    TW('u = 25 cm, h = 11 cm.', 'Etikettfläche (Mantel).', 'Mantel = Rechteck u · h.', '25 · 11 = 275.', 'Das Etikett ist 275 cm² groß.'), 'Welche Form hat der Mantel, wenn man ihn flach legt?', einheit='cm²'))
TX.u('zylinder', 'einkleidung', TZ('Eine Papprolle für ein Poster ist 60 cm lang, ihr Umfang beträgt 22 cm. Wie viel cm² Pappe hat ihr Mantel?', '60 * 22',
    TW('Länge 60 cm, u = 22 cm.', 'Mantelfläche.', 'Mantel = u · Länge.', '22 · 60 = 1 320.', 'Der Mantel hat 1 320 cm².'), 'Die Länge der Rolle ist die Höhe des Zylinders.', einheit='cm²'))
TX.u('zylinder', 'umkehr', TZ('Ein Etikett ist 31,4 cm lang und liegt genau einmal um eine Dose. Welchen Durchmesser hat die Dose? Rechne mit π ≈ 3,14.', '31.4 / 3.14',
    TW('Etikettlänge = Umfang = 31,4 cm.', 'Durchmesser d.', 'u = π · d ⇒ d = u : π.', 'd = 31,4 : 3,14 = 10.', 'Die Dose hat 10 cm Durchmesser.'), 'Welche Länge der Dose ist die Etikettlänge?', einheit='cm'))
TX.u('zylinder', 'pruefung', TZ('Für 200 Dosen (Umfang 25 cm, Höhe 11 cm) werden Etiketten gedruckt. Auf einen Druckbogen passen 6 Etiketten. Wie viele Bögen braucht man?', '-(-200 // 6)',
    TW('200 Etiketten, 6 pro Bogen. Umfang und Höhe braucht man hier nicht.', 'Anzahl der Bögen.', '200 : 6, dann aufrunden.', '200 : 6 ≈ 33,3.', 'Man braucht 34 Bögen.'), 'Was passiert mit den restlichen Etiketten?'), huerde='deuten')
TX.u('zylinder', 'fehler', TX.A('Für das Etikett einer Dose mit 8 cm Durchmesser und 12 cm Höhe rechnet jemand: 8 · 12 = 96 cm². Was ist falsch?',
    'Er hat den Durchmesser statt des Umfangs genommen: richtig π · 8 · 12 ≈ 301 cm².', ['Nichts, das stimmt.', 'Er hätte durch 2 teilen müssen: 48 cm².', 'Er hat die Deckel vergessen: 96 + 2 · 64 = 224 cm².'],
    TW('d = 8 cm, h = 12 cm.', 'Fehler und richtige Etikettfläche.', 'Mantel = Umfang · Höhe, Umfang = π · d.', 'u ≈ 25,1 cm; 25,1 · 12 ≈ 301 cm².', 'Falsch war der Durchmesser statt des Umfangs; richtig sind etwa 301 cm².'),
    'Welche Seite des Mantelrechtecks ist der Umfang?'), huerde='entscheidung')
TX.s('zylinder', TZ('Eine Säule im Garten ist 2 m hoch und hat 1,5 m Umfang. Sie wird ganz mit Efeu-Matten verkleidet. Wie viel m² Matten braucht man für den Mantel?', '2 * 1.5',
    TW('h = 2 m, u = 1,5 m.', 'Mantelfläche.', 'u · h.', '1,5 · 2 = 3.', 'Man braucht 3 m².'), einheit='m²'))
TX.s('zylinder', TZ('Ein zylinderförmiger Stifteköcher ist 10 cm hoch, sein Umfang ist 24 cm. Wie viel cm² Papier braucht man, um den Mantel zu bekleben?', '10 * 24',
    TW('h = 10 cm, u = 24 cm.', 'Mantelfläche.', 'u · h.', '24 · 10 = 240.', 'Man braucht 240 cm².'), einheit='cm²'))
TX.k('zylinder', TZ('Ein Rohr ist 3 m lang, sein Umfang beträgt 0,5 m. Wie viel m² müssen außen gestrichen werden?', '3 * 0.5',
    TW('Länge 3 m, u = 0,5 m.', 'Mantelfläche.', 'u · Länge.', '0,5 · 3 = 1,5.', 'Es müssen 1,5 m² gestrichen werden.'), einheit='m²'))

# --- schraegbild ---
TX.u('schraegbild', 'direkt', TZ('Ein Gartenhaus ist 4 m tief. Im Plan steht 1 cm für 1 m. Wie lang zeichnest du die Tiefe im Schrägbild mit q = 1/2?', '4 / 2',
    TW('Tiefe 4 m → 4 cm im Plan, q = 1/2.', 'gezeichnete Tiefe.', 'Kanten nach hinten mal q.', '4 cm · 1/2 = 2 cm.', 'Du zeichnest 2 cm.'), 'Erst in Plan-Zentimeter umrechnen, dann verkürzen.', einheit='cm'))
TX.u('schraegbild', 'einkleidung', TZ('Ein Schuhkarton ist 30 cm breit, 12 cm hoch und 18 cm tief. Er wird in Originalgröße im Schrägbild (q = 1/2, ω = 45°) gezeichnet, die Breite vorn. Wie lang wird die Tiefe gezeichnet?', '18 / 2',
    TW('Tiefe 18 cm, q = 1/2.', 'gezeichnete Tiefe.', 'Nur die Kanten nach hinten werden verkürzt.', '18 · 1/2 = 9.', 'Die Tiefe wird 9 cm lang gezeichnet.'), 'Welche Kante läuft nach hinten?', einheit='cm'))
TX.u('schraegbild', 'umkehr', TZ('In einem Prospekt ist ein Regal im Maßstab 1 : 20 als Schrägbild (q = 1/2) gezeichnet. Die nach hinten laufende Kante ist dort 2,5 cm lang. Wie tief ist das Regal in Wirklichkeit?', '2.5 * 2 * 20',
    TW('gezeichnet 2,5 cm, q = 1/2, Maßstab 1 : 20.', 'wirkliche Tiefe.', 'Erst die Verkürzung rückgängig (· 2), dann den Maßstab (· 20).', '2,5 · 2 = 5 cm; 5 · 20 = 100 cm.', 'Das Regal ist 100 cm tief.'), 'Welche zwei Verkleinerungen musst du rückgängig machen?', einheit='cm'))
TX.u('schraegbild', 'mehrschritt', TZ('Ein Aquarium ist 80 cm breit, 40 cm hoch und 35 cm tief. Es wird im Maßstab 1 : 10 als Schrägbild (q = 1/2) gezeichnet. Wie lang wird die Tiefe gezeichnet?', '35 / 10 / 2',
    TW('Tiefe 35 cm, Maßstab 1 : 10, q = 1/2.', 'gezeichnete Tiefe.', 'Maßstab, dann Verkürzung.', '35 : 10 = 3,5 cm; 3,5 · 1/2 = 1,75 cm.', 'Die Tiefe wird 1,75 cm lang.'), 'Erst verkleinern, dann verkürzen.', einheit='cm'))
TX.u('schraegbild', 'pruefung', TZ('Ein Pool ist 8 m lang, 4 m breit und 1,5 m tief und fasst 48 000 l. Er wird im Maßstab 1 : 100 als Schrägbild (q = 1/2, ω = 45°) gezeichnet, die Länge vorn. Wie lang wird die Breite gezeichnet, die nach hinten läuft?', '400 / 100 / 2',
    TW('Breite 4 m nach hinten, Maßstab 1 : 100, q = 1/2. Die Literzahl spielt keine Rolle.', 'gezeichnete Breite.', 'Maßstab, dann Verkürzung.', '400 cm : 100 = 4 cm; · 1/2 = 2 cm.', 'Die Breite wird 2 cm lang gezeichnet.'),
    'Welche Kante läuft nach hinten, welche Angabe brauchst du nicht?', einheit='cm'), huerde='ueberfluessig')
TX.u('schraegbild', 'begruenden', TX.A('Für einen Bastelbogen soll ein Würfel mit 6 cm Kante als Schrägbild (q = 1/2) gezeichnet werden. Kind A zeichnet die Kante nach hinten 6 cm lang, Kind B 3 cm. Wer hat recht?',
    'Kind B: Nach hinten wird mit q = 1/2 verkürzt.', ['Kind A: Alle Würfelkanten sind gleich lang.', 'Beide, das ist Geschmackssache.', 'Keins: Es müssten 12 cm sein.'],
    TW('a = 6 cm, q = 1/2.', 'richtige Länge nach hinten.', 'Nur Kanten nach hinten werden mit q verkürzt.', '6 · 1/2 = 3 cm.', 'Kind B hat recht.'), 'Was bedeutet q = 1/2?'), huerde='entscheidung')
TX.s('schraegbild', TZ('Ein Paket ist 50 cm breit, 30 cm hoch und 40 cm tief. Es wird im Maßstab 1 : 10 als Schrägbild (q = 1/2) gezeichnet. Wie lang wird die Tiefe gezeichnet?', '40 / 10 / 2',
    TW('Tiefe 40 cm, 1 : 10, q = 1/2.', 'gezeichnete Tiefe.', 'Maßstab, dann Verkürzung.', '4 cm · 1/2 = 2 cm.', 'Die Tiefe wird 2 cm lang.'), einheit='cm'))
TX.s('schraegbild', TZ('Im Schrägbild (q = 1/2) eines Bettes im Maßstab 1 : 20 ist die Kante nach hinten 5 cm lang. Wie lang ist das Bett in dieser Richtung wirklich?', '5 * 2 * 20',
    TW('gezeichnet 5 cm, q = 1/2, 1 : 20.', 'wirkliche Länge.', 'Verkürzung und Maßstab rückgängig machen.', '5 · 2 = 10 cm; 10 · 20 = 200 cm.', 'Das Bett ist 200 cm lang.'), einheit='cm'))
TX.k('schraegbild', TZ('Ein Kasten ist 60 cm tief. Wie lang zeichnest du die Tiefe im Schrägbild mit q = 1/2 im Maßstab 1 : 10?', '60 / 10 / 2',
    TW('Tiefe 60 cm, 1 : 10, q = 1/2.', 'gezeichnete Tiefe.', 'Maßstab, dann Verkürzung.', '6 cm · 1/2 = 3 cm.', 'Du zeichnest 3 cm.'), einheit='cm'))

# --- ansichten ---
TX.u('ansichten', 'erkennen', TX.A('Eine Konservendose steht auf dem Tisch. Was siehst du, wenn du genau von oben auf sie schaust?', 'einen Kreis', ['ein Rechteck', 'ein Quadrat', 'ein Dreieck'],
    TW('stehende Dose (Zylinder).', 'Draufsicht.', 'Von oben sieht man den Deckel.', 'Der Deckel ist ein Kreis.', 'Die Draufsicht ist ein Kreis.'), 'Was liegt oben auf der Dose?'))
TX.u('ansichten', 'einkleidung', TZ('Ein Kind baut aus gleichen Holzwürfeln eine Treppe: unten 3 Würfel nebeneinander, darauf 2, ganz oben 1, alle linksbündig. Wie viele Quadrate siehst du in der Vorderansicht?', '3 + 2 + 1',
    TW('Reihen mit 3, 2 und 1 Würfel.', 'Quadrate in der Vorderansicht.', 'Jeder Würfel zeigt vorn ein Quadrat.', '3 + 2 + 1 = 6.', 'Man sieht 6 Quadrate.'), 'Stell dir vor, du stehst genau vor der Treppe.'))
TX.u('ansichten', 'darstellung', TX.A('Ein liegendes Zelt hat die Form eines dreiseitigen Prismas; du schaust genau auf die dreieckige Öffnung. Welche Formen haben Vorderansicht und Draufsicht?',
    'Vorderansicht Dreieck, Draufsicht Rechteck', ['Vorderansicht Rechteck, Draufsicht Dreieck', 'beide Dreiecke', 'beide Rechtecke'],
    TW('liegendes Dreiecksprisma, Öffnung vorn.', 'Vorder- und Draufsicht.', 'Von vorn die Grundfläche, von oben die beiden Dachflächen als ein Rechteck.', 'Dreieck / Rechteck.', 'Vorderansicht Dreieck, Draufsicht Rechteck.'),
    'Was siehst du von vorn, was von oben?'))
TX.u('ansichten', 'pruefung', TZ('Ein Kind baut aus Holzwürfeln ein Haus. Die Draufsicht zeigt 2 × 3 Quadrate, die Vorderansicht ein Rechteck aus 3 Quadraten Breite und 2 Quadraten Höhe. Wie viele Würfel sind es höchstens?', '2 * 3 * 2',
    TW('Draufsicht 2 × 3, Vorderansicht 3 breit und 2 hoch.', 'größtmögliche Zahl der Würfel.', 'Höchstens überall 2 Würfel übereinander.', '6 Felder · 2 = 12.', 'Es sind höchstens 12 Würfel (es könnten auch weniger sein).'),
    'Wie hoch kann jeder Stapel höchstens sein?'), huerde='deuten')
TX.u('ansichten', 'begruenden', TX.A('Ein Händler beschreibt eine Verpackung so: „Von vorn ein Rechteck, von der Seite ein Rechteck, von oben ein Kreis.“ Welcher Körper ist das?',
    'ein stehender Zylinder', ['ein Quader', 'ein Kegel', 'eine Kugel'],
    TW('Vorder- und Seitenansicht Rechteck, Draufsicht Kreis.', 'passender Körper.', 'Alle drei Ansichten prüfen.', 'Quader: von oben Rechteck; Kegel: von vorn Dreieck; Kugel: überall Kreis.', 'Es ist ein stehender Zylinder.'),
    'Prüfe für jeden Körper alle drei Ansichten.'), huerde='entscheidung')
TX.s('ansichten', TX.A('Ein runder Turm hat ein flaches Dach. Welche Form hat seine Vorderansicht?', 'ein Rechteck', ['ein Kreis', 'ein Dreieck', 'ein Quadrat mit Kreis'],
    TW('Zylinder mit flachem Dach.', 'Vorderansicht.', 'Von vorn sieht man Höhe und Breite.', 'Rechteck.', 'Die Vorderansicht ist ein Rechteck.')))
TX.s('ansichten', TX.A('Ein Kleiderschrank (Quader) steht an der Wand. Welche Form hat seine Draufsicht?', 'ein Rechteck', ['ein Kreis', 'ein Dreieck', 'ein Trapez'],
    TW('Quader.', 'Draufsicht.', 'Von oben sieht man die Deckfläche.', 'Rechteck.', 'Die Draufsicht ist ein Rechteck.')))
TX.k('ansichten', TX.A('Ein Gartenpavillon ist ein sechsseitiges Prisma mit flachem Dach. Welche Form hat seine Draufsicht?', 'ein Sechseck', ['ein Rechteck', 'ein Kreis', 'ein Dreieck'],
    TW('sechsseitiges Prisma, stehend.', 'Draufsicht.', 'Von oben sieht man die Grundfläche.', 'Sechseck.', 'Die Draufsicht ist ein Sechseck.')))

# --- beurteilen ---
TX.u('beurteilen', 'erkennen', TX.A('Ein Stück Würfelzucker hat sechs gleiche quadratische Flächen. Ist es ein Prisma?', 'Ja, ein Würfel ist ein besonderes Prisma.', ['Nein, ein Prisma braucht Dreiecke.', 'Nein, ein Prisma ist immer länger als breit.'],
    TW('Würfel.', 'Ist er ein Prisma?', 'Zwei gleiche parallele Grundflächen, Rechtecke als Seiten.', 'Quadrate sind besondere Rechtecke.', 'Ja, der Würfel ist ein Prisma.'), 'Prüfe die Merkmale eines Prismas.'))
TX.u('beurteilen', 'einkleidung', TZ('Ein Hersteller schreibt: „Unsere Verpackung ist ein Prisma mit 12 Ecken.“ Wie viele Kanten hat sie?', '3 * 12 // 2',
    TW('12 Ecken.', 'Kanten.', 'Ecken = 2n ⇒ n = 6; Kanten = 3n.', 'n = 6, Kanten = 18.', 'Die Verpackung hat 18 Kanten.'), 'Welches n gehört zu 12 Ecken?'))
TX.u('beurteilen', 'mehrschritt', TZ('Ein Bastler verbaut genau 24 Holzstäbe als Kanten eines Prismas. Wie viele Ecken hat das Prisma?', '2 * (24 // 3)',
    TW('24 Kanten.', 'Ecken.', 'Kanten = 3n ⇒ n = 8; Ecken = 2n.', 'n = 8, Ecken = 16.', 'Das Prisma hat 16 Ecken.'), 'Wie viele Ecken hat die Grundfläche?'))
TX.u('beurteilen', 'pruefung', TZ('Eine Verpackung soll ein Prisma mit 10 Flächen sein und höchstens 25 Kanten haben. Wie viele Kanten hat sie?', '3 * (10 - 2)',
    TW('10 Flächen, höchstens 25 Kanten.', 'Kantenzahl (und ob die Bedingung erfüllt ist).', 'Flächen = n + 2 ⇒ n = 8; Kanten = 3n.', 'n = 8, Kanten = 24 ≤ 25.', 'Sie hat 24 Kanten – das ist erlaubt.'),
    'Welches n folgt aus 10 Flächen? Passt dann die zweite Bedingung?'), huerde='zwei')
TX.u('beurteilen', 'begruenden', TX.A('Jemand sagt: „Eine Dose ist ein Prisma, weil sie zwei gleiche, parallele Grundflächen hat.“ Was stimmt?',
    'Falsch: Ihr Mantel ist gekrümmt; ein Prisma hat Vielecke als Grundflächen und Rechtecke als Seiten.', ['Richtig, das reicht als Merkmal.', 'Richtig, ein Kreis ist ein Vieleck.', 'Falsch, weil eine Dose keine Kanten hat und Prismen nur 2 Grundflächen haben dürfen.'],
    TW('Dose = Zylinder.', 'Ist die Begründung richtig?', 'Alle Merkmale eines Prismas prüfen.', 'Grundfläche Kreis (kein Vieleck), Mantel gekrümmt.', 'Die Aussage ist falsch: Ein Zylinder ist kein Prisma.'),
    'Reicht ein Merkmal oder müssen alle stimmen?'), huerde='entscheidung')
TX.u('beurteilen', 'transfer', TZ('Eine Laterne hat die Form eines Prismas mit 18 Kanten. An jeder Ecke wird gelötet, jede Lötstelle dauert 2 Minuten. Wie lange dauert das Löten?', '2 * (2 * 18 // 3)',
    TW('18 Kanten, 2 min pro Ecke.', 'Lötzeit.', 'Kanten = 3n ⇒ n = 6; Ecken = 2n = 12; Zeit = 12 · 2 min.', 'n = 6, 12 Ecken, 24 min.', 'Das Löten dauert 24 Minuten.'), 'Wie viele Ecken hat ein Prisma mit 18 Kanten?', einheit='min'))
TX.s('beurteilen', TZ('Ein Zelt hat für jede Kante eine Stange, insgesamt 9 Stangen, und ist ein Prisma. Wie viele Ecken hat es?', '2 * (9 // 3)',
    TW('9 Kanten.', 'Ecken.', 'n = 9 : 3 = 3; Ecken = 2n.', '2 · 3 = 6.', 'Das Zelt hat 6 Ecken.')))
TX.s('beurteilen', TX.A('Eine Geschenkbox ist ein Prisma mit 7 Flächen. Welche Form hat ihre Grundfläche?', 'ein Fünfeck', ['ein Siebeneck', 'ein Viereck', 'ein Sechseck'],
    TW('7 Flächen.', 'Form der Grundfläche.', 'Flächen = n + 2 ⇒ n = 5.', 'n = 5.', 'Die Grundfläche ist ein Fünfeck.')))
TX.k('beurteilen', TZ('Ein Turm ist ein Prisma mit 10 Ecken. Wie viele Seitenflächen hat er ohne Boden und Dach?', '10 // 2',
    TW('10 Ecken.', 'Seitenflächen.', 'Ecken = 2n ⇒ n = 5; Seitenflächen = n.', 'n = 5.', 'Er hat 5 Seitenflächen.')))
baue = mit_text(baue, TX)
# ---- TEXT ENDE ----

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Körper und Netze', ['prisma', 'netz', 'zylinder']), ('Darstellen', ['schraegbild', 'ansichten']), ('Verstehen', ['beurteilen'])],
         'Prismen und Zylinder erkennen, ihre Netze verstehen und berechnen, Schrägbilder nach den Regeln anlegen und Ansichten zuordnen.',
         ['Prisma: 2 deckungsgleiche parallele Grundflächen, Mantel aus Rechtecken. n-seitig: 2n Ecken, 3n Kanten, n + 2 Flächen.',
          'Zylindermantel abgewickelt: Rechteck mit Länge = Kreisumfang.', 'Schrägbild: Vorderfläche wahr, nach hinten unter 45° und mit q (meist 1/2) verkürzt.'],
         offen=['Netze und Schrägbilder werden mit dem Bildtyp „figur“ gezeigt (Würfelnetze aus Quadraten, Quader im Schrägbild). Selbst zeichnen lassen kann die App noch nicht; '
                'Ansichten werden weiter nur in Worten abgefragt.',
                'Überschneidung mit raum.schraegbilder: Die Schrägbild-Regeln für Prismen stehen hier; raum.schraegbilder konzentriert sich auf Pyramiden.',
                'Zylinder: Der Kreisumfang wird in den Aufgaben gegeben, weil Kreisberechnungen (π) erst im Thema messen.kreisberechnung folgen.'])
