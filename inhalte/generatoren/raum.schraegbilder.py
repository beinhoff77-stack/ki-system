#!/usr/bin/env python3
"""Thema raum.schraegbilder – Schrägbilder und Raumdarstellung (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, Z, baue, cz, mit_bild, zt  # noqa: E402

META = {'thema_schluessel': 'raum.schraegbilder', 'thema_id': 91, 'block_id': 109, 'klasse': {'gym_by': 10, 'rs_by': 7, 'ib_myp': 4}}

ETAPPEN = [
    {'lernziel': 'pyramide', 'titel': 'Pyramiden: Ecken, Kanten, Flächen',
     'regel': 'Eine ⟦Pyramide⟧ hat ein n-Eck als Grundfläche und eine ⟦Spitze⟧. Sie hat n + 1 Ecken, ⟦2n Kanten⟧ (n unten, n zur Spitze) und n + 1 Flächen (n Dreiecke + Grundfläche).',
     'schritte': ['Sechsseitige Pyramide: n = 6', 'Ecken: 6 + 1 = 7, Kanten: 2 · 6 = 12', 'Flächen: 6 Dreiecke + 1 Sechseck = ⟦7⟧'],
     'probe': 'E + F − K = 7 + 7 − 12 = 2 ✓',
     'fehler': 'Eine vierseitige Pyramide hat nicht 4 Flächen: Zu den 4 Dreiecken kommt die ⟦quadratische Grundfläche⟧ dazu, also 5.',
     '_verbot': ['Sechsseitige Pyramide']},
    {'lernziel': 'laengen', 'titel': 'Schrägbilder von Prismen und Pyramiden',
     'regel': 'Schrägbild: Strecken ⟦parallel zur Zeichenebene⟧ (Breite, Höhe) in wahrer Länge; Strecken ⟦nach hinten⟧ unter dem Winkel ω (meist 45°) mit dem ⟦Verkürzungsfaktor q⟧ (meist 1/2). Die Höhe einer Pyramide zeichnest du senkrecht in wahrer Länge über dem Fußpunkt.',
     'schritte': ['Quadratische Pyramide: Grundkante 6 cm, Höhe 8 cm, q = 1/2.', 'Grundfläche: vordere Kante 6 cm in wahrer Länge, Kanten nach hinten 6 · 1/2 = 3 cm unter 45°.',
                  'Diagonalen der Grundfläche zeichnen. Ihr Schnittpunkt F ist der Fußpunkt der Höhe.', 'Von F aus ⟦8 cm⟧ senkrecht nach oben zur Spitze S. Verdeckte Kanten gestrichelt.'],
     'fehler': 'Die Höhe einer Pyramide wird nicht verkürzt: Sie steht ⟦senkrecht⟧ und liegt damit parallel zur Zeichenebene.',
     'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [6, 0], 'C': [8.12, 2.12], 'D': [2.12, 2.12], 'F': [4.06, 1.06], 'S': [4.06, 9.06]},
              'linien': [['A', 'B', '6 cm'], ['B', 'C', '3 cm'], ['A', 'D', '', 'gestrichelt'], ['D', 'C', '', 'gestrichelt'], ['S', 'A'], ['S', 'B'], ['S', 'C'], ['S', 'D', '', 'gestrichelt'],
                         ['F', 'S', 'h = 8 cm', 'gestrichelt'], ['A', 'C', '', 'gestrichelt'], ['B', 'D', '', 'gestrichelt']]},
     '_verbot': ['Grundkante 6 cm, Höhe 8 cm']},
    {'lernziel': 'lage', 'titel': 'Parallel, schneidend oder windschief?',
     'regel': 'Zwei Geraden im Raum sind ⟦parallel⟧ (gleiche Richtung), ⟦schneiden sich⟧ (ein gemeinsamer Punkt) oder sind ⟦windschief⟧: nicht parallel und trotzdem ohne gemeinsamen Punkt. Beispiel: Eine Autobahn und eine Straße, die auf einer Brücke quer darüber führt.',
     'schritte': ['Quader ABCDEFGH wie im Bild.', 'AB läuft unten vorne nach rechts. CG läuft hinten rechts senkrecht nach oben.', 'Sie haben verschiedene Richtungen und treffen sich nie: ⟦windschief⟧.'],
     'fehler': 'Geraden ohne Schnittpunkt sind im Raum nicht automatisch parallel. Parallel heißt ⟦gleiche Richtung⟧ – sonst sind sie windschief.',
     'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [5, 0], 'C': [6.06, 1.06], 'D': [1.06, 1.06], 'E': [0, 2], 'F': [5, 2], 'G': [6.06, 3.06], 'H': [1.06, 3.06]}, 'linien': [['A', 'B'], ['B', 'F'], ['F', 'E'], ['E', 'A'], ['B', 'C'], ['C', 'G'], ['G', 'F'], ['E', 'H'], ['H', 'G'], ['A', 'D', '', 'gestrichelt'], ['D', 'C', '', 'gestrichelt'], ['D', 'H', '', 'gestrichelt']]},
     '_verbot': ['AB und CG']},
    {'lernziel': 'koordinaten', 'titel': 'Punkte im Raum mit Koordinaten',
     'regel': 'Im Raum hat ein Punkt ⟦drei Koordinaten⟧ P(x | y | z). Liegt ein Quader mit A im ⟦Ursprung⟧ so, dass AB auf der x-Achse, AD auf der y-Achse und AE auf der z-Achse (nach oben) liegt, liest du die Koordinaten aus den ⟦Kantenlängen⟧ ab.',
     'schritte': ['Quader: A(0 | 0 | 0), Länge 5 in x-, Breite 3 in y-, Höhe 2 in z-Richtung', 'B(5 | 0 | 0), C(5 | 3 | 0), E(0 | 0 | 2)', 'G liegt über C: ⟦G(5 | 3 | 2)⟧'],
     'fehler': 'H liegt nicht bei (0 | 0 | 2) – das ist E. H liegt über D, also H(0 | 3 | 2). Achte darauf, ⟦welche Ecke über welcher⟧ liegt.',
     'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [5, 0], 'C': [6.06, 1.06], 'D': [1.06, 1.06], 'E': [0, 2], 'F': [5, 2], 'G': [6.06, 3.06], 'H': [1.06, 3.06]},
              'linien': [['A', 'B', '5'], ['B', 'F'], ['F', 'E'], ['E', 'A'], ['B', 'C'], ['C', 'G'], ['G', 'F'], ['E', 'H'], ['H', 'G'], ['A', 'D', '3', 'gestrichelt'], ['D', 'C', '', 'gestrichelt'], ['D', 'H', '', 'gestrichelt']]},
     '_verbot': ['Länge 5 in x-, Breite 3 in y-, Höhe 2 in z']},
    {'lernziel': 'rotation', 'titel': 'Rotationskörper',
     'regel': 'Dreht man eine ebene Figur um eine ⟦Achse⟧, entsteht ein ⟦Rotationskörper⟧. Rechteck um eine Seite → ⟦Zylinder⟧; rechtwinkliges Dreieck um eine Kathete → ⟦Kegel⟧; Halbkreis um den Durchmesser → ⟦Kugel⟧.',
     'schritte': ['Rechteck 4 cm × 7 cm dreht sich um die 7-cm-Seite.', 'Die Achse ist 7 cm lang: Höhe 7 cm.', 'Die andere Seite wird zum Radius: ⟦Zylinder mit r = 4 cm, h = 7 cm⟧'],
     'fehler': 'Dreht sich das Rechteck 4 cm × 7 cm um die 7-cm-Seite, ist der Radius nicht 7 cm. Die Seite ⟦auf der Achse⟧ wird zur Höhe, die andere zum Radius.',
     'bild': {'typ': 'figur', 'punkte': {'_a': [0, -1], '_b': [0, 8], 'A': [0, 0], 'B': [4, 0], 'C': [4, 7], 'D': [0, 7], '_l': [-4, 0], '_m': [-4, 7]}, 'flaeche': ['A', 'B', 'C', 'D'],
              'linien': [['_a', '_b', '', 'gestrichelt'], ['A', 'B', '4 cm'], ['B', 'C'], ['C', 'D'], ['D', 'A', '7 cm (Achse)'], ['_l', 'A', '', 'gestrichelt'], ['_l', '_m', '', 'gestrichelt'], ['_m', 'D', '', 'gestrichelt']]},
     '_verbot': ['4 cm × 7 cm']},
    {'lernziel': 'axialschnitt', 'titel': 'Axialschnitte berechnen',
     'regel': 'Ein ⟦Axialschnitt⟧ schneidet einen Rotationskörper ⟦entlang der Achse⟧. Beim Zylinder entsteht ein Rechteck (2r breit, h hoch), beim Kegel ein gleichschenkliges Dreieck (Grundseite 2r, Höhe h), bei der Kugel ein Kreis.',
     'schritte': ['Zylinder r = 3 cm, h = 10 cm', 'Axialschnitt: Rechteck 6 cm × 10 cm', 'Flächeninhalt: ⟦60 cm²⟧'],
     'fehler': 'Der Axialschnitt eines Zylinders ist nicht r breit, sondern ⟦2r⟧: Der Schnitt geht durch die Mitte und erfasst den ganzen Durchmesser.',
     '_verbot': ['r = 3 cm, h = 10 cm']},
]


# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'pyramide': {
  'einstieg': 'Die berühmten Pyramiden in Ägypten haben einen quadratischen Boden und laufen nach oben in einer Spitze zusammen. Auch manche Kirchturmspitzen sehen so aus. Ein Körper mit einem Vieleck als Boden und einer Spitze heißt ⟦Pyramide⟧.',
  'woerter': [['Pyramide', 'Körper mit einem n-Eck als Grundfläche und Dreiecken, die in einer Spitze zusammenlaufen'], ['Spitze', 'die oberste Ecke, in der alle Seitenkanten zusammenlaufen'],
              ['n', 'Anzahl der Ecken der Grundfläche'], ['Seitenkante', 'Kante von einer Ecke der Grundfläche zur Spitze'],
              ['E + F − K = 2', 'Ecken + Flächen − Kanten = 2 (Eulerscher Polyedersatz) – eine Kontrolle fürs Zählen']],
  'schritte': ['Eine sechsseitige Pyramide hat als Grundfläche ein Sechseck: n = 6.', 'Ecken: 6 Ecken unten und die Spitze, also 7.',
               'Kanten: 6 Kanten am Boden und 6 Seitenkanten zur Spitze, also 12.', 'Flächen: 6 Dreiecke und das Sechseck unten, zusammen ⟦7⟧.'],
  'regel': 'So zählst du bei einer ⟦Pyramide⟧ mit n-Eck als Grundfläche: n + 1 Ecken, ⟦2n Kanten⟧ (n unten, n zur ⟦Spitze⟧) und n + 1 Flächen (n Dreiecke und die Grundfläche).'},
 'laengen': {
  'einstieg': 'Wie zeichnet man ein Zelt so ins Heft, dass es räumlich aussieht? Die Front zeichnest du in echter Größe. Was nach hinten geht, zeichnest du schräg und kürzer. Die Zeltstange in der Mitte steht senkrecht – die zeichnest du in voller Länge. So entsteht das ⟦Schrägbild⟧ einer Pyramide.',
  'woerter': [['Zeichenebene', 'die Fläche deines Hefts'], ['parallel zur Zeichenebene', 'die Strecke liegt „flach“ vor dir und geht nicht nach hinten'],
              ['ω (Omega)', 'griechischer Buchstabe für den Winkel der Kanten nach hinten, meist 45°'], ['q (Verkürzungsfaktor)', 'Kanten nach hinten werden mit q malgenommen, meist q = 1/2'],
              ['Fußpunkt F', 'der Punkt unter der Spitze, hier die Mitte der Grundfläche'], ['Höhe', 'der senkrechte Abstand von der Spitze zur Grundfläche']]},
 'lage': {
  'einstieg': 'Unten eine Autobahn, oben eine Straße, die auf einer Brücke quer darüber führt: Die beiden laufen nicht in dieselbe Richtung und treffen sich trotzdem nie. So etwas gibt es nur im Raum, nicht auf einem flachen Blatt. Solche Geraden heißen ⟦windschief⟧.',
  'woerter': [['Quader ABCDEFGH', 'A, B, C, D sind die Ecken unten; E liegt über A, F über B, G über C, H über D'], ['AB', 'die Gerade durch die Punkte A und B'],
              ['parallel', 'gleiche Richtung, kein gemeinsamer Punkt'], ['schneiden sich', 'genau ein gemeinsamer Punkt'], ['windschief', 'nicht parallel und trotzdem ohne gemeinsamen Punkt']],
  'schritte': ['Quader ABCDEFGH wie im Bild.', 'AB läuft unten vorne nach rechts. CG läuft hinten rechts senkrecht nach oben.', 'Die Richtungen sind verschieden, also sind sie nicht parallel.',
               'Sie treffen sich auch nirgends: AB und CG sind ⟦windschief⟧.'],
  'regel': 'So entscheidest du: gleiche Richtung → ⟦parallel⟧. Ein gemeinsamer Punkt → ⟦schneiden sich⟧. Weder das eine noch das andere → ⟦windschief⟧.'},
 'koordinaten': {
  'einstieg': 'In einem großen Gebäude findest du einen Raum mit drei Angaben: wie weit den Gang entlang, wie weit nach rechts und in welchem Stockwerk. Genauso beschreibt man einen Punkt im Raum mit drei Zahlen. Sie heißen ⟦Koordinaten im Raum⟧.',
  'woerter': [['P(x | y | z)', 'ein Punkt mit drei Koordinaten: x, y und z'], ['x-, y-, z-Achse', 'die drei Richtungen: hier entlang AB, entlang AD und nach oben'],
              ['Ursprung', 'der Punkt (0 | 0 | 0), hier die Ecke A']],
  'schritte': ['Quader: A liegt im Ursprung (0 | 0 | 0). Er ist 5 lang (x-Richtung), 3 breit (y-Richtung) und 2 hoch (z-Richtung).',
               'B liegt 5 weit in x-Richtung: B(5 | 0 | 0). C liegt zusätzlich 3 weit in y-Richtung: C(5 | 3 | 0).', 'E liegt 2 über A: E(0 | 0 | 2).',
               'G liegt 2 über C, also ⟦G(5 | 3 | 2)⟧.']},
 'rotation': {
  'einstieg': 'Drehst du ein Fähnchen an seinem Stab schnell zwischen den Händen, siehst du plötzlich einen runden Körper. Aus einem rechteckigen Fähnchen wird so etwas wie eine Dose. Ein Körper, der durch Drehen einer flachen Figur entsteht, heißt ⟦Rotationskörper⟧.',
  'woerter': [['Achse', 'die Linie, um die gedreht wird (der Stab)'], ['Rotationskörper', 'ein Körper, der durch Drehen einer Figur um eine Achse entsteht'],
              ['Kathete', 'eine der beiden Seiten am rechten Winkel eines Dreiecks'], ['Radius r', 'Abstand vom Mittelpunkt bis zum Rand des Kreises']],
  'schritte': ['Ein Rechteck 4 cm × 7 cm dreht sich um seine 7-cm-Seite.', 'Diese Seite liegt auf der Achse. Sie wird zur Höhe: h = 7 cm.',
               'Die 4-cm-Seite dreht sich im Kreis um die Achse. Sie wird zum Radius: r = 4 cm.', 'Es entsteht ein ⟦Zylinder mit r = 4 cm und h = 7 cm⟧.']},
 'axialschnitt': {
  'einstieg': 'Schneidest du eine Möhre der Länge nach genau durch die Mitte, siehst du eine Schnittfläche. Bei einer Dose wäre sie ein Rechteck, bei einer Eistüte ein Dreieck. Ein Schnitt genau entlang der Drehachse heißt ⟦Axialschnitt⟧.',
  'woerter': [['Axialschnitt', 'Schnitt durch einen Rotationskörper genau entlang der Achse'], ['2r', 'der Durchmesser: zweimal der Radius'],
              ['gleichschenklig', 'ein Dreieck mit zwei gleich langen Seiten']],
  'schritte': ['Ein Zylinder hat r = 3 cm und h = 10 cm.', 'Der Schnitt geht durch die Mitte und erfasst den ganzen Durchmesser: 2 · 3 cm = 6 cm breit.',
               'Er ist so hoch wie der Zylinder, also 10 cm. Der Axialschnitt ist ein Rechteck 6 cm × 10 cm.', 'Flächeninhalt: 6 cm · 10 cm = ⟦60 cm²⟧.']},
}

for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))
# ---- KLAR ENDE ----

N_ECK = {3: 'dreiseitige', 4: 'vierseitige', 5: 'fünfseitige', 6: 'sechsseitige', 7: 'siebenseitige', 8: 'achtseitige', 10: 'zehnseitige', 12: 'zwölfseitige'}


def g_pyramide(R, st):
    n = R.choice(list(N_ECK))
    if st >= 2 and R.random() < .3:
        pyr = R.random() < .5
        F, K = (n + 1, 2 * n) if pyr else (n + 2, 3 * n)
        ri = f'{N_ECK[n]} Pyramide' if pyr else f'{N_ECK[n]}s Prisma'
        fa = [f'{N_ECK[n]}s Prisma' if pyr else f'{N_ECK[n]} Pyramide', f'{N_ECK.get(F - 2, str(F - 2) + "-seitige")}s Prisma' if pyr and F - 2 in N_ECK else f'{N_ECK.get(F - 1, "")} Pyramide' if not pyr and F - 1 in N_ECK else 'Würfel',
              f'{N_ECK.get(K // 2, "")} Pyramide' if not pyr and K // 2 in N_ECK and K // 2 != n else 'Kegel']
        w = (f'Pyramide: n + 1 = {F} → n = {n}, Kanten 2 · {n} = {K} ✓.' if pyr else f'Prisma: n + 2 = {F} → n = {n}, Kanten 3 · {n} = {K} ✓.') + \
            (f' Prisma mit {F} Flächen hätte n = {F - 2} und 3 · {F - 2} = {3 * (F - 2)} Kanten ✗.' if pyr else f' Pyramide mit {F} Flächen hätte n = {F - 1} und 2 · {F - 1} = {2 * (F - 1)} Kanten ✗.')
        return A(R, f'Ein Körper hat {F} Flächen und {K} Kanten. Was ist er?', ri[0].upper() + ri[1:], [x[0].upper() + x[1:] for x in fa if x], w,
                 'Prüfe beide Möglichkeiten: Pyramide (n + 1 Flächen, 2n Kanten) und Prisma (n + 2 Flächen, 3n Kanten).')
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
    return Z(f'Wie viele Kanten haben ein {N_ECK[n]}s Prisma und eine {N_ECK[m]} Pyramide zusammen?', 3 * n + 2 * m, f'3 * {n} + 2 * {m}',
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


QUADER_BILD = {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [5, 0], 'C': [6.06, 1.06], 'D': [1.06, 1.06], 'E': [0, 2], 'F': [5, 2], 'G': [6.06, 3.06], 'H': [1.06, 3.06]},
               'linien': [['A', 'B'], ['B', 'F'], ['F', 'E'], ['E', 'A'], ['B', 'C'], ['C', 'G'], ['G', 'F'], ['E', 'H'], ['H', 'G'], ['A', 'D', '', 'gestrichelt'], ['D', 'C', '', 'gestrichelt'],
                          ['D', 'H', '', 'gestrichelt']]}


def g_lage(R, st):
    mass = (R.randint(3, 9), R.randint(2, 7), R.randint(2, 8))
    if st == 3 and R.random() < .5:
        # Partner finden
        g = R.choice(KANTEN)
        art = R.choice(['windschief', 'schneiden sich', 'parallel'])
        lagen = {h: lage_von(g, h, mass) for h in KANTEN if h != g}
        treffer = [h for h, l in lagen.items() if l == art]
        andere = [h for h, l in lagen.items() if l != art and l != 'identisch']
        h = R.choice(treffer)
        wort = {'windschief': 'ist windschief zu', 'schneiden sich': 'schneidet', 'parallel': 'ist parallel zu'}[art]
        fa = R.sample(andere, 3)
        return mit_bild(A(R, f'Welche Kante {wort} {g}?', h, fa,
                          f'{h}: {art}. ' + '; '.join(f'{x}: {lagen[x]}' for x in fa) + '.',
                          'Prüfe für jede Kante: gleiche Richtung? gemeinsamer Punkt?'), QUADER_BILD)
    pool = KANTEN if st < 3 else DIAG
    while True:
        g, h = R.sample(KANTEN + DIAG if st == 3 else pool, 2)
        if st == 3 and g in KANTEN and h in KANTEN: continue
        l = lage_von(g, h, mass)
        if l != 'identisch': break
    a_ = A(R, f'Quader ABCDEFGH (ABCD Grundfläche, E über A, F über B, G über C, H über D). Wie liegen die Geraden {g} und {h} zueinander?', l, [x for x in LAGEN if x != l] + ['identisch'],
             {'parallel': f'{g} und {h} haben dieselbe Richtung, aber keinen gemeinsamen Punkt.',
              'schneiden sich': f'{g} und {h} haben einen gemeinsamen Punkt' + (f' ({"".join(sorted(set(g) & set(h)))})' if set(g) & set(h) else ' im Inneren einer Fläche oder des Quaders') + '.',
              'windschief': f'{g} und {h} sind nicht parallel und treffen sich nirgends: Sie liegen in keiner gemeinsamen Ebene.'}[l],
             'Stell dir den Quader vor (z. B. eine Schachtel). Haben die Geraden dieselbe Richtung? Gibt es einen gemeinsamen Punkt?')
    return mit_bild(a_, QUADER_BILD)


def g_rotation(R, st):
    if st == 1:
        fig = R.choice([('ein Rechteck', 'um eine seiner Seiten', 'Zylinder'), ('ein rechtwinkliges Dreieck', 'um eine Kathete', 'Kegel'),
                        ('ein Halbkreis', 'um seinen Durchmesser', 'Kugel'), ('ein Quadrat', 'um eine seiner Seiten', 'Zylinder')])
        r = fig[2]
        akk = {'Zylinder': 'einen Zylinder', 'Kegel': 'einen Kegel', 'Kugel': 'eine Kugel'}[r]
        return A(R, f'Welcher Körper entsteht, wenn sich {fig[0]} {fig[1]} dreht?', r, [k for k in ['Zylinder', 'Kegel', 'Kugel', 'Pyramide'] if k != r],
                 f'{fig[0][0].upper() + fig[0][1:]} {fig[1]} gedreht ergibt {akk}.', 'Stell dir vor, die Figur ist eine Fahne, die sich schnell um die Achse dreht.')
    if st == 2:
        a, b = R.sample(range(2, 15), 2)
        if R.random() < .5:
            return Z(f'Ein Rechteck mit den Seiten {a} cm und {b} cm dreht sich um die {a}-cm-Seite. Wie groß ist der Radius des entstehenden Zylinders?', b, f'{b}',
                     f'Die {a}-cm-Seite liegt auf der Achse und wird zur Höhe. Die {b}-cm-Seite steht senkrecht dazu und wird zum Radius: r = {b} cm.',
                     'Welche Seite liegt auf der Achse? Die andere wird zum Radius.', einheit='cm')
        return Z(f'Ein rechtwinkliges Dreieck mit den Katheten {a} cm und {b} cm dreht sich um die {a}-cm-Kathete. Wie hoch ist der entstehende Kegel?', a, f'{a}',
                 f'Die Kathete auf der Achse ({a} cm) wird zur Höhe, die andere ({b} cm) zum Radius.', 'Die Seite auf der Drehachse wird zur Höhe.', einheit='cm')
    if R.random() < .35:
        frage, ri, fa, w = R.choice([
            ('Ein rechtwinkliges Dreieck dreht sich um seine Hypotenuse. Was entsteht?', 'zwei Kegel, Boden an Boden', ['ein Kegel', 'ein Zylinder', 'eine Kugel'],
             'Die Höhe auf die Hypotenuse wird zum gemeinsamen Radius. Beide Teildreiecke ergeben je einen Kegel; sie stoßen mit ihren Grundkreisen aneinander.'),
            ('Ein Rechteck dreht sich um seine Mittellinie (parallel zu einer Seite). Was entsteht?', 'ein Zylinder mit halb so großem Radius wie bei Drehung um die Seite',
             ['ein Zylinder mit doppeltem Radius', 'zwei Zylinder', 'ein Kegel'], 'Jede Hälfte überstreicht denselben Zylinder. Der Radius ist der Abstand von der Mittellinie zur Seite: die halbe Breite.'),
            ('Ein gleichschenkliges Dreieck dreht sich um seine Symmetrieachse. Was entsteht?', 'ein Kegel', ['zwei Kegel', 'ein Zylinder', 'eine Pyramide'],
             'Jede Hälfte ist ein rechtwinkliges Dreieck, das sich um eine Kathete dreht: Beide ergeben denselben Kegel.')])
        return A(R, frage, ri, fa, w, 'Stell dir vor, wie jeder Punkt der Figur einen Kreis um die Achse beschreibt.')
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


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl8.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl8 import mit_umbau  # noqa: E402

_P = {"A": [0, 0], "B": [6, 0], "C": [8.12, 2.12], "D": [2.12, 2.12], "F": [4.06, 1.06], "S": [4.06, 9.06]}
_P_BASIS = [["A", "B", "6 cm"], ["B", "C", "3 cm"], ["A", "D", "", "gestrichelt"], ["D", "C", "", "gestrichelt"]]
_P_DIAG = [["A", "C", "", "gestrichelt"], ["B", "D", "", "gestrichelt"]]
_P_ALLE = _P_BASIS + [["S", "A"], ["S", "B"], ["S", "C"], ["S", "D", "", "gestrichelt"], ["F", "S", "h = 8 cm", "gestrichelt"]] + _P_DIAG
_PU = {'_A': [0, 0], '_B': [6, 0], '_C': [8.12, 2.12], '_D': [2.12, 2.12], '_S': [4.06, 9.06]}
_PU_L = [['_A', '_B'], ['_B', '_C'], ['_A', '_D', '', 'gestrichelt'], ['_D', '_C', '', 'gestrichelt'], ['_S', '_A'], ['_S', '_B'], ['_S', '_C'], ['_S', '_D', '', 'gestrichelt']]
_Q = {"A": [0, 0], "B": [5, 0], "C": [6.06, 1.06], "D": [1.06, 1.06], "E": [0, 2], "F": [5, 2], "G": [6.06, 3.06], "H": [1.06, 3.06]}
_Q_L = [["A", "B"], ["B", "F"], ["F", "E"], ["E", "A"], ["B", "C"], ["C", "G"], ["G", "F"], ["E", "H"], ["H", "G"], ["A", "D", "", "gestrichelt"], ["D", "C", "", "gestrichelt"], ["D", "H", "", "gestrichelt"]]
_AX = {'_a': [0, 0], '_b': [6, 0], '_c': [6, 10], '_d': [0, 10], '_m': [3, 0], '_o': [3, -1], '_p': [3, 11]}
UMBAU = {
 'pyramide': {
  'einstieg': 'Die Pyramiden in Ägypten haben einen quadratischen Boden. Nach oben laufen sie in einer Spitze zusammen. So ein Körper heißt ⟦Pyramide⟧.',
  'woerter': [['Pyramide', 'Körper mit einem Vieleck als Boden und einer Spitze'], ['Spitze', 'der oberste Punkt, in dem sich die Seitenkanten treffen'], ['Seitenkante', 'eine Kante vom Boden zur Spitze']],
  'bild': {'typ': 'figur', 'punkte': _PU, 'linien': _PU_L},
  'schritte': [{'text': 'Die Grundfläche ist ein Quadrat, also n = 4.', 'bild': {'flaeche': ['_A', '_B', '_C', '_D']}},
               {'text': 'Ecken: 4 unten und die Spitze, also 5.'},
               {'text': 'Kanten: 4 am Boden und 4 Seitenkanten zur Spitze, also 8.'},
               {'text': 'Flächen: 4 Dreiecke und das Quadrat, zusammen ⟦5⟧.', 'bild': {'flaeche': ['_A', '_B', '_S']}}],
  'fehler': 'Eine sechsseitige Pyramide hat nicht 6 Flächen. Zu den 6 Dreiecken kommt die ⟦Grundfläche⟧ dazu, also 7.',
  'regel': 'n-Eck-Pyramide: ⟦n + 1 Ecken, 2n Kanten, n + 1 Flächen⟧. Die 1 ist die Spitze bzw. die Grundfläche.'},
 'laengen': {
  'einstieg': 'Ein Zelt soll räumlich ins Heft. Vorne echte Größe, nach hinten schräg und kürzer, die Stange senkrecht. So entsteht ein ⟦Schrägbild⟧.',
  'woerter': [['q', 'der Verkürzungsfaktor: Kanten nach hinten werden mal q gezeichnet, meist 1/2'], ['Fußpunkt F', 'dort steht die Höhe auf der Grundfläche'], ['Diagonale', 'Strecke zwischen gegenüberliegenden Ecken']],
  'bild': {'typ': 'figur', 'punkte': _P, 'linien': _P_ALLE},
  'schritte': [{'text': 'Die Pyramide hat Grundkante 6 cm, Höhe 8 cm und q = 1/2.'},
               {'text': 'Vorne 6 cm, nach hinten 6 · 1/2 = 3 cm unter 45°.', 'bild': {'punkte': {k: _P[k] for k in 'ABCD'}, 'linien': _P_BASIS}},
               {'text': 'Die Diagonalen schneiden sich im Fußpunkt F.', 'bild': {'punkte': {k: _P[k] for k in 'ABCDF'}, 'linien': _P_BASIS + _P_DIAG}},
               {'text': 'Von F ⟦8 cm⟧ senkrecht hoch zur Spitze S.', 'bild': {'punkte': _P, 'linien': _P_ALLE}}],
  'fehler': 'Die Höhe wird nicht verkürzt. Sie steht ⟦senkrecht⟧ und bleibt in wahrer Länge: 8 cm.',
  'fehler_bild': {'punkte': {**_P, 'S': [4.06, 5.06]}, 'linien': _P_ALLE[:-3] + [["F", "S", "4 cm?", "gestrichelt"]] + _P_DIAG},
  'regel': 'Nur Kanten ⟦nach hinten⟧ werden verkürzt, meist auf die Hälfte. Breite und Höhe bleiben in wahrer Länge.'},
 'lage': {
  'einstieg': 'Unten eine Autobahn, oben eine Brücke quer darüber. Die Straßen haben verschiedene Richtungen und treffen sich nie. Solche Geraden heißen ⟦windschief⟧.',
  'woerter': [['windschief', 'nicht parallel und ohne Schnittpunkt – das geht nur im Raum'], ['parallel', 'gleiche Richtung, ohne Schnittpunkt']],
  'bild': {'typ': 'figur', 'punkte': _Q, 'linien': _Q_L},
  'schritte': [{'text': 'Im Quader läuft AB unten vorne nach rechts.', 'bild': {'linien': [["A", "B", "AB"]] + _Q_L[1:]}},
               {'text': 'CG läuft hinten rechts senkrecht nach oben.', 'bild': {'linien': [["A", "B", "AB"]] + _Q_L[1:5] + [["C", "G", "CG"]] + _Q_L[6:]}},
               {'text': 'Verschiedene Richtungen: nicht parallel. Sie treffen sich auch nicht.'},
               {'text': 'Also sind AB und CG ⟦windschief⟧.'}],
  'fehler': 'Ohne Schnittpunkt heißt im Raum nicht automatisch parallel. Parallel verlangt die ⟦gleiche Richtung⟧.',
  'regel': 'Gleiche Richtung: ⟦parallel⟧. Gemeinsamer Punkt: ⟦schneidend⟧. Sonst sind sie windschief.'},
 'koordinaten': {
  'einstieg': 'In einem großen Gebäude findest du einen Raum mit drei Angaben: Gang, Seite, Stockwerk. Einen Punkt im Raum beschreibst du genauso mit drei Zahlen, den ⟦Koordinaten⟧.',
  'woerter': [['(5 | 3 | 2)', 'x = 5 nach rechts, y = 3 nach hinten, z = 2 nach oben'], ['Ursprung', 'der Punkt (0 | 0 | 0)']],
  'bild': {'typ': 'figur', 'punkte': _Q, 'linien': [["A", "B", "5"]] + _Q_L[1:9] + [["A", "D", "3", "gestrichelt"]] + _Q_L[10:]},
  'schritte': [{'text': 'A liegt im Ursprung. Der Quader ist 5 lang, 3 breit, 2 hoch.'},
               {'text': 'Also B(5 | 0 | 0), C(5 | 3 | 0).'},
               {'text': 'E liegt 2 über A: E(0 | 0 | 2).'},
               {'text': 'G liegt 2 über C: ⟦G(5 | 3 | 2)⟧.'}],
  'fehler': 'H ist nicht (0 | 0 | 2) – das ist E. H liegt über D: ⟦H(0 | 3 | 2)⟧.',
  'regel': 'Ein Punkt im Raum hat ⟦drei Koordinaten⟧ (x | y | z). Die Kantenlängen sagen, wie weit du in jede Richtung gehst.'},
 'rotation': {
  'einstieg': 'Drehst du ein Fähnchen schnell an seinem Stab, siehst du einen runden Körper. Aus einem Rechteck wird so etwas wie eine Dose. So entsteht ein ⟦Rotationskörper⟧.',
  'woerter': [['Rotationskörper', 'Körper, der durch Drehen einer flachen Figur entsteht'], ['Achse', 'die Linie, um die gedreht wird – hier der Stab'], ['Radius r', 'Abstand von der Achse zum Rand']],
  'bild': {"typ": "figur", "punkte": {"_a": [0, -1], "_b": [0, 8], "A": [0, 0], "B": [4, 0], "C": [4, 7], "D": [0, 7], "_l": [-4, 0], "_m": [-4, 7]}, "flaeche": ["A", "B", "C", "D"],
           "linien": [["_a", "_b", "", "gestrichelt"], ["A", "B", "4 cm"], ["B", "C"], ["C", "D"], ["D", "A", "7 cm"], ["_l", "A", "", "gestrichelt"], ["_l", "_m", "", "gestrichelt"], ["_m", "D", "", "gestrichelt"]]},
  'schritte': [{'text': 'Ein Rechteck 4 cm × 7 cm dreht sich um die 7-cm-Seite.'},
               {'text': 'Die Seite auf der Achse wird zur Höhe: h = 7 cm.'},
               {'text': 'Die 4-cm-Seite dreht sich im Kreis: Radius r = 4 cm.'},
               {'text': 'Es entsteht ein ⟦Zylinder⟧ mit r = 4 cm und h = 7 cm.'}],
  'fehler': 'Der Radius ist nicht 7 cm. Die Seite ⟦auf der Achse⟧ wird zur Höhe, die andere zum Radius.',
  'regel': 'Rechteck um eine Seite: ⟦Zylinder⟧. Dreieck um eine Kathete: Kegel. Halbkreis um den Durchmesser: Kugel.'},
 'axialschnitt': {
  'einstieg': 'Schneidest du eine Möhre der Länge nach durch die Mitte, siehst du eine Schnittfläche. Bei einer Dose ist sie ein Rechteck. Dieser Schnitt heißt ⟦Axialschnitt⟧.',
  'woerter': [['Axialschnitt', 'ein Schnitt genau entlang der Drehachse'], ['Durchmesser', '2 · r: einmal quer durch die Mitte']],
  'bild': {'typ': 'figur', 'punkte': _AX, 'linien': [['_o', '_p', '', 'gestrichelt'], ['_m', '_b', 'r = 3 cm'], ['_b', '_c', 'h = 10 cm'], ['_c', '_d'], ['_d', '_a'], ['_a', '_m']]},
  'schritte': [{'text': 'Ein Zylinder hat r = 3 cm und h = 10 cm.'},
               {'text': 'Der Schnitt erfasst den ganzen Durchmesser: 2 · 3 cm = 6 cm.', 'bild': {'linien': [['_o', '_p', '', 'gestrichelt'], ['_a', '_b', '6 cm'], ['_b', '_c', 'h = 10 cm'], ['_c', '_d'], ['_d', '_a']]}},
               {'text': 'Er ist 10 cm hoch. Das Rechteck misst 6 cm × 10 cm.'},
               {'text': 'Fläche: 6 · 10 = ⟦60 cm²⟧.', 'bild': {'flaeche': ['_a', '_b', '_c', '_d']}}],
  'fehler': 'Der Schnitt ist nicht r breit, sondern ⟦2r⟧. Er geht durch die Mitte und erfasst den Durchmesser.',
  'fehler_bild': {'flaeche': ['_m', '_b', '_c', '_d'], 'punkte': {**_AX, '_d': [3, 10]}, 'linien': [['_o', '_p', '', 'gestrichelt'], ['_m', '_b', '3 cm?'], ['_b', '_c', 'h = 10 cm'], ['_c', '_d'], ['_d', '_m']]},
  'regel': 'Ein ⟦Axialschnitt⟧ geht durch die Achse. Zylinder: Rechteck 2r × h. Kegel: Dreieck. Kugel: Kreis.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---- SCHWER (Zehnte Runde: schwerere Aufgaben nach Prüfungsvorbild, siehe _schwer_kl8.py) ----
# Vorbilder (Typ und Niveau, nicht Wortlaut/Zahlen): Realschule Bayern, Leistungsaufgaben Jgst. 8 (I) (ISB): Axialschnitt eines Rotationskörpers,
# Teilkörper nennen; RS-Leistungsaufgaben Jgst. 9: Kantenmodell einer Pyramide aus Draht; RS-Abschlussprüfungen 2022/2024 (Axialschnitt von Kerzenhalter/Spielfigur,
# auf Kl.-8-Niveau ohne Kegelvolumen); BMT8 2025 und 2008 (Volumen aus Schrägbild; Quader mit herausgeschnittenem Würfel); RS-Jahrgangsstufentest 8 2023
# (Mittelpunkt-Fehler finden, hier übertragen auf Raumkoordinaten); VERA-8 2025 (Ecken und Kanten). Für Raumkoordinaten und windschiefe Geraden gibt es
# auf Kl.-8-Niveau keine Prüfungsaufgaben (Stoff späterer Jahrgangsstufen); dort sind die P-Aufgaben übertragene Typen.
from _schwer_kl8 import Neu, mit_schwer  # noqa: E402

SW = Neu(10_8_12)
_M = (4, 6, 2)
for _g, _h, _soll in (('AC', 'BF', 'windschief'), ('AC', 'BG', 'windschief'), ('AB', 'GH', 'parallel'), ('AE', 'CG', 'parallel'), ('AE', 'FG', 'windschief'), ('AE', 'GH', 'windschief'),
                      ('AE', 'EF', 'schneiden sich'), ('AC', 'EG', 'parallel'), ('AC', 'CG', 'schneiden sich')):
    assert lage_von(_g, _h, _M) == _soll, (_g, _h)
assert sum(lage_von('AB', k, _M) == 'windschief' for k in KANTEN) == 4

# pyramide
SW.z('pyramide', 2, 'Eine Pyramide hat 12 Kanten. Wie viele Flächen hat sie?', 7, '12 / 2 + 1', '2n = 12 ⇔ n = 6. Flächen: n + 1 = 7.', 'Bestimme n aus der Kantenzahl 2n.')
SW.a('pyramide', 2, 'Welcher Körper hat 6 Ecken und 6 Flächen?', 'eine fünfseitige Pyramide', ['ein Würfel', 'ein dreiseitiges Prisma', 'eine sechsseitige Pyramide'],
     'Fünfseitige Pyramide: 5 + 1 = 6 Ecken, 5 + 1 = 6 Flächen. Der Würfel hat 8 Ecken, das dreiseitige Prisma 5 Flächen.', 'Bei einer Pyramide ist Ecken = Flächen = n + 1.')
SW.z('pyramide', 3, 'Berechne für eine siebenseitige Pyramide: Ecken + Flächen − Kanten.', 2, '(7 + 1) + (7 + 1) - 2 * 7', '8 Ecken, 8 Flächen, 14 Kanten: 8 + 8 − 14 = 2.',
     'Nutze n + 1, n + 1 und 2n.', art='P')
SW.z('pyramide', 3, 'Ein Kantenmodell einer quadratischen Pyramide aus Draht: Grundkante 8 cm, jede Seitenkante 12 cm. Man hat 1 m Draht. Wie viele cm bleiben übrig?', 20, '100 - (4 * 8 + 4 * 12)',
     'Kanten: 4 · 8 cm + 4 · 12 cm = 80 cm. Übrig: 100 cm − 80 cm = 20 cm.', 'Zähle Grundkanten und Seitenkanten getrennt. 1 m = 100 cm.', einheit='cm', art='P')
SW.z('pyramide', 3, 'Auf jede der 6 Flächen eines Würfels wird eine quadratische Pyramide geklebt (Grundfläche = Würfelfläche). Wie viele Ecken hat der neue Körper?', 14, '8 + 6',
     'Die 8 Würfelecken bleiben Ecken. Jede Pyramide bringt eine neue Spitze: 8 + 6 = 14.', 'Was kommt pro Pyramide an Ecken dazu?', art='K')
SW.z('pyramide', 3, 'Eine Pyramide und ein Prisma haben dieselbe n-eckige Grundfläche. Zusammen haben sie 45 Kanten. Wie groß ist n?', 9, '45 / 5',
     'Pyramide 2n Kanten, Prisma 3n Kanten: 5n = 45 ⇔ n = 9.', 'Stelle eine Gleichung mit 2n und 3n auf.', art='K')

# laengen
SW.z('laengen', 2, 'Ein Würfel mit 6 cm Kantenlänge wird im Schrägbild (q = 1/2) gezeichnet. Wie lang sind alle 12 gezeichneten Kanten zusammen?', 60, '8 * 6 + 4 * 3',
     '8 Kanten in wahrer Länge (6 cm), 4 Kanten nach hinten verkürzt (3 cm): 48 + 12 = 60 cm.', 'Wie viele Kanten führen nach hinten?', einheit='cm')
SW.z('laengen', 2, 'Im Schrägbild mit q = 2/3 ist eine nach hinten führende Kante 4 cm lang gezeichnet. Wie lang ist sie in Wirklichkeit?', 6, '4 * 3 / 2',
     'Gezeichnet = wahr · 2/3. Wahre Länge = 4 : 2/3 = 4 · 3/2 = 6 cm.', 'Rückwärts: durch q teilen.', einheit='cm')
SW.z('laengen', 3, 'Ein Prisma hat als Vorderfläche ein rechtwinkliges Dreieck mit den Katheten 4 cm und 3 cm. Im Schrägbild (q = 1/2) ist die Kante nach hinten 5 cm lang gezeichnet. Berechne das Volumen.',
     60, '4 * 3 / 2 * (5 * 2)', 'Grundfläche: 4 · 3 : 2 = 6 cm². Wahre Tiefe: 5 cm · 2 = 10 cm. V = 6 · 10 = 60 cm³ (nicht 30 cm³).', 'Die gezeichnete Tiefe ist verkürzt.',
     einheit='cm³', art='P')
SW.z('laengen', 3, 'Aus einem Quader (8 cm × 5 cm × 6 cm) wird an einer Ecke ein Würfel mit 2 cm Kantenlänge herausgeschnitten. Wie groß ist das Volumen des Restkörpers?', 232, '8 * 5 * 6 - 2**3',
     'Quader: 240 cm³. Würfel: 8 cm³. Rest: 232 cm³.', 'Ganzer Quader minus Würfel.', einheit='cm³', art='P')
SW.a('laengen', 3, 'Aus einer Ecke eines Quaders wird ein kleiner Würfel herausgeschnitten. Wie ändert sich die Oberfläche?', 'Sie bleibt gleich groß.', ['Sie wird kleiner.', 'Sie wird größer.',
     'Das hängt von der Größe des Würfels ab.'],
     'Drei kleine Quadrate fallen außen weg, drei gleich große Quadrate kommen innen in der Ecke dazu. Die Oberfläche bleibt gleich – das Volumen nicht.', 'Zähle, welche Flächen weg- und welche dazukommen.', art='K')
SW.z('laengen', 3, 'Im Schrägbild (q = 1/2) ist ein Quader 5 cm breit, 3 cm hoch und nach hinten 2 cm tief gezeichnet. Wie viele Würfel mit 1 cm Kantenlänge passen genau hinein?', 60, '5 * 3 * (2 * 2)',
     'Wahre Tiefe: 4 cm. Also 5 · 3 · 4 = 60 Würfel.', 'Erst die wahre Tiefe bestimmen.', einheit='Würfel', art='K')

# lage
SW.a('lage', 2, 'Welche Kante des Quaders ist parallel zu AE?', 'CG', ['AB', 'EF', 'GH'], 'AE ist eine senkrechte Kante. Parallel dazu sind BF, CG und DH.', 'Welche Kanten zeigen in dieselbe Richtung?',
     grafik=QUADER_BILD)
SW.a('lage', 2, 'Wie liegen die Geraden AB und GH zueinander?', 'parallel', ['schneiden sich', 'windschief', 'identisch'], 'AB und GH zeigen beide von links nach rechts (wie DC). Sie sind parallel.',
     'Verschiebe GH in Gedanken nach unten.', grafik=QUADER_BILD)
SW.a('lage', 3, 'Welche Gerade ist windschief zur Flächendiagonale AC der Grundfläche?', 'BF', ['CG', 'EG', 'AE'],
     'BF trifft die Grundfläche nur in B, und B liegt nicht auf AC. Parallel sind sie auch nicht: windschief. CG und AE schneiden AC in C bzw. A, EG ist parallel zu AC.',
     'Prüfe für jede Gerade: gemeinsamer Punkt? gleiche Richtung?', grafik=QUADER_BILD, art='P')
SW.z('lage', 3, 'In einem Zimmer (Quader) steht ein Stab genau an der Kante AE. Wie viele der vier Kanten der Decke EFGH sind zu diesem Stab windschief?', 2, '1 + 1',
     'EF und HE gehen durch E und schneiden AE. FG und GH berühren AE nicht und sind nicht parallel: 2 windschiefe Kanten.', 'Welche Deckenkanten gehen durch E?', grafik=QUADER_BILD, art='P')
SW.z('lage', 3, 'Wie viele der 12 Kanten eines Quaders sind windschief zur Kante AB?', 4, '12 - 1 - 3 - 4',
     'Parallel zu AB: CD, EF, GH (3). Schneiden AB (in A oder B): AD, AE, BC, BF (4). Übrig: 12 − 1 − 3 − 4 = 4 windschiefe Kanten (CG, DH, FG, HE).', 'Zähle erst die parallelen und die schneidenden.',
     grafik=QUADER_BILD, art='K')
SW.a('lage', 3, 'Gibt es im Quader zwei Flächendiagonalen, die windschief zueinander sind?', 'Ja, zum Beispiel AC und BG.', ['Nein, Diagonalen schneiden sich immer.',
     'Ja, zum Beispiel AC und EG.', 'Nein, Diagonalen sind immer parallel.'],
     'AC liegt in der Grundfläche, BG trifft die Grundfläche nur in B (nicht auf AC). Sie sind nicht parallel: windschief. AC und EG sind parallel.', 'Nimm eine Diagonale unten und eine in einer Seitenfläche.',
     grafik=QUADER_BILD, art='K')

# koordinaten
SW.a('koordinaten', 2, 'Ein Quader ABCDEFGH hat A(0 | 0 | 0), B(4 | 0 | 0), D(0 | 6 | 0) und E(0 | 0 | 3). Welche Koordinaten hat C?', 'C(4 | 6 | 0)', ['C(6 | 4 | 0)', 'C(4 | 6 | 3)', 'C(4 | 0 | 6)'],
     'C liegt in der Grundfläche (z = 0), über B hinaus in Richtung D: x wie B, y wie D.', 'C liegt B gegenüber in der Grundfläche.')
SW.z('koordinaten', 2, 'Ein Quader hat A(0 | 0 | 0), B(4 | 0 | 0), D(0 | 6 | 0) und E(0 | 0 | 3). Wie lang ist die Kante CG?', 3, '3', 'CG ist senkrecht, so lang wie AE: 3.',
     'Welche Kante ist genauso lang?')
SW.a('koordinaten', 3, 'Ein Quader hat A(0 | 0 | 0) und G(6 | 4 | 8). Tom gibt als Mittelpunkt der Raumdiagonale AG den Punkt M(6 | 4 | 8) an. Was stimmt?', 'Falsch: Man muss die Koordinaten halbieren. M(3 | 2 | 4).',
     ['Richtig gerechnet.', 'Falsch: M(12 | 8 | 16).', 'Falsch: M(6 | 4 | 0).'],
     'Mittelpunkt: je Koordinate (Anfang + Ende) : 2 = (0 + 6) : 2 = 3, (0 + 4) : 2 = 2, (0 + 8) : 2 = 4. Tom hat nur addiert.', 'Wie berechnet man in der Ebene den Mittelpunkt einer Strecke?', art='P')
SW.z('koordinaten', 3, 'Ein Quader hat A(0 | 0 | 0), B(5 | 0 | 0), D(0 | 4 | 0) und E(0 | 0 | 3). Berechne sein Volumen.', 60, '5 * 4 * 3', 'Länge 5, Breite 4, Höhe 3: V = 60 (Volumeneinheiten).',
     'Lies die Kantenlängen an den Koordinaten ab.', art='P')
SW.z('koordinaten', 3, 'Bei einem Würfel ist A(0 | 0 | 0). Der Mittelpunkt der Raumdiagonale AG ist M(3 | 3 | 3). Wie lang ist eine Kante?', 6, '3 * 2', 'M liegt in der Mitte: G(6 | 6 | 6). Kantenlänge 6.',
     'Von A bis M ist es die halbe Diagonale.', art='K')
SW.a('koordinaten', 3, 'Ein Quader hat A(0 | 0 | 0) und G(4 | 6 | 2). Welcher Punkt liegt NICHT auf einer Kante des Quaders?', '(2 | 3 | 0)', ['(4 | 3 | 0)', '(0 | 6 | 1)', '(2 | 0 | 2)'],
     '(4 | 3 | 0) liegt auf BC, (0 | 6 | 1) auf DH, (2 | 0 | 2) auf EF. (2 | 3 | 0) liegt mitten in der Grundfläche, auf keiner Kante.', 'Auf einer Kante sind zwei Koordinaten „Randwerte“ (0 oder Maximum).', art='K')

# rotation
_haus = {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [6, 0], 'C': [6, 4], 'D': [0, 4], 'S': [3, 7], '_o': [3, -1], '_p': [3, 8]}, 'flaeche': ['A', 'B', 'C', 'S', 'D'],
         'linien': [['A', 'B', '6 cm'], ['B', 'C', '4 cm'], ['C', 'S'], ['S', 'D'], ['D', 'A'], ['_o', '_p', 'Achse', 'gestrichelt']]}
SW.z('rotation', 2, 'Ein Rechteck mit den Seiten 5 cm und 2 cm dreht sich um die 2-cm-Seite. Wie hoch ist der entstehende Zylinder?', 2, '2',
     'Die Seite, um die gedreht wird, ist die Achse: Höhe 2 cm. Die andere Seite wird zum Radius (5 cm) – ein flacher Zylinder.', 'Die Drehachse wird zur Höhe.', einheit='cm')
SW.a('rotation', 2, 'Welcher Körper entsteht, wenn sich ein gleichschenkliges Dreieck um seine Symmetrieachse dreht?', 'ein Kegel', ['ein Zylinder', 'eine Pyramide', 'eine Kugel'],
     'Jede Hälfte ist ein rechtwinkliges Dreieck, das sich um eine Kathete dreht: ein Kegel.', 'Was überstreicht die halbe Grundseite?')
SW.a('rotation', 3, 'Die Figur dreht sich um die gestrichelte Achse. Welcher Körper entsteht?', 'ein Zylinder mit einem Kegel darauf', ['ein Zylinder', 'eine Pyramide auf einem Würfel', 'zwei Kegel'],
     'Das Rechteck wird zum Zylinder (r = 3 cm, h = 4 cm), das Dreieck darüber zum Kegel (r = 3 cm, h = 3 cm).', 'Zerlege die Figur in Teile und drehe jedes einzeln.', grafik=_haus, art='P')
SW.a('rotation', 3, 'Ein rechtwinkliges Trapez dreht sich um die Seite, die auf beiden parallelen Seiten senkrecht steht. Welcher Körper entsteht?',
     'ein Kegel, dem die Spitze abgeschnitten wurde (Kegelstumpf)', ['ein Zylinder', 'ein Kegel', 'eine Kugel'],
     'Die parallelen Seiten werden zu zwei verschieden großen Kreisen (oben und unten). Die schräge Seite bildet den Mantel: ein Kegelstumpf – wie ein Lampenschirm.',
     'Was wird aus den beiden parallelen Seiten beim Drehen?', art='P')
SW.a('rotation', 3, 'Ein Rechteck (6 cm × 4 cm) dreht sich um eine Achse, die parallel zur 4-cm-Seite liegt, aber 2 cm außerhalb des Rechtecks. Was entsteht?', 'ein Rohr (Hohlzylinder)',
     ['ein Zylinder mit 6 cm Radius', 'ein Kegel', 'zwei Zylinder'],
     'Zwischen Achse und Rechteck bleibt eine Lücke von 2 cm: Innen entsteht ein Loch mit 2 cm Radius, außen ist der Radius 8 cm. Das ist ein Rohr.', 'Berührt das Rechteck die Achse?', art='K')
SW.a('rotation', 3, 'Ein Quadrat dreht sich um eine seiner Diagonalen. Welcher Körper entsteht?', 'ein Doppelkegel (zwei Kegel mit gemeinsamer Grundfläche)', ['ein Zylinder', 'eine Kugel', 'ein Würfel'],
     'Die Diagonale teilt das Quadrat in zwei gleichschenklige Dreiecke. Jedes dreht sich um seine Grundseite, die Diagonale. So entstehen zwei Kegel, die mit ihren Grundflächen aneinanderliegen.',
     'Zerlege das Quadrat an der Diagonale in zwei Dreiecke.', art='K')

# axialschnitt
_fig = {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [6, 0], 'C': [6, 2], 'D': [0, 2], 'S': [3, 7]}, 'flaeche': ['A', 'B', 'C', 'S', 'D'],
        'linien': [['A', 'B', '6 cm'], ['B', 'C', '2 cm'], ['C', 'D', '', 'gestrichelt'], ['C', 'S'], ['S', 'D'], ['D', 'A']]}
SW.z('axialschnitt', 2, 'Ein Zylinder hat den Durchmesser 10 cm und die Höhe 4 cm. Wie groß ist der Flächeninhalt seines Axialschnitts?', 40, '10 * 4', 'Der Axialschnitt ist ein Rechteck d × h = 10 cm × 4 cm = 40 cm².',
     'Achtung: Hier ist schon der Durchmesser gegeben.', einheit='cm²')
SW.z('axialschnitt', 2, 'Eine Kugel hat den Radius 5 cm. Wie lang ist der Umfang ihres Axialschnitts? (π ≈ 3,14)', 31.4, '2 * 3.14 * 5', 'Der Axialschnitt einer Kugel ist ein Kreis mit r = 5 cm: u = 2 · 3,14 · 5 = 31,4 cm.',
     'Welche Figur ist der Axialschnitt einer Kugel?', einheit='cm')
SW.z('axialschnitt', 3, 'Der Axialschnitt einer Spielfigur besteht aus einem Rechteck (6 cm breit, 2 cm hoch) und einem daraufgesetzten gleichschenkligen Dreieck (Grundseite 6 cm, Höhe 5 cm). Wie groß ist der Axialschnitt?',
     27, '6 * 2 + 6 * 5 / 2', 'Rechteck: 12 cm². Dreieck: 6 · 5 : 2 = 15 cm². Zusammen 27 cm².', 'Zerlege in Rechteck und Dreieck.', einheit='cm²', grafik=_fig, art='P')
SW.z('axialschnitt', 3, 'Dieselbe Spielfigur entsteht durch Drehung des Axialschnitts um seine Symmetrieachse. Welchen Radius hat der kegelförmige obere Teil?', 3, '6 / 2',
     'Der Kegel hat als Axialschnitt das Dreieck mit Grundseite 6 cm. Der Radius ist die halbe Grundseite: 3 cm.', 'Die Grundseite des Dreiecks ist der Durchmesser.', einheit='cm', grafik=_fig, art='P')
SW.z('axialschnitt', 3, 'Der Axialschnitt eines Kegels ist ein gleichseitiges Dreieck mit dem Umfang 18 cm. Wie groß ist der Radius des Kegels?', 3, '18 / 3 / 2',
     'Jede Seite ist 6 cm lang, also auch die Grundseite (der Durchmesser). Radius 3 cm.', 'Die Grundseite des Dreiecks ist der Durchmesser.', einheit='cm', art='K')
SW.z('axialschnitt', 3, 'Der Axialschnitt eines Zylinders ist ein Quadrat mit dem Umfang 24 cm. Berechne das Volumen des Zylinders. (π ≈ 3,14)', 169.56, '3.14 * 3**2 * 6',
     'Quadratseite 6 cm: Durchmesser 6 cm (r = 3 cm) und Höhe 6 cm. V = 3,14 · 9 · 6 = 169,56 cm³.', 'Was bedeuten die Quadratseiten für den Zylinder?', einheit='cm³', art='K')

baue = mit_schwer(baue, SW)
# ---- SCHWER ENDE ----

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, mit_befunden  # noqa: E402

BF = Befunde('raum.schraegbilder', 13_8_12)
# a) reine Verkürzung: q = 1/2 ist Stufe-1-Typ, q = 1/3 und 2/3 Stufe 2
BF.stufe('laengen', 'Eine Kante führt 2 cm nach hinten. Wie lang wird sie im Schrägbild mit q = 1/2 gezeichnet?', 1)
BF.stufe('laengen', 'Eine Kante führt 8 cm nach hinten. Wie lang wird sie im Schrägbild mit q = 1/2 gezeichnet?', 1)
BF.stufe('laengen', 'Eine Kante führt 6 cm nach hinten. Wie lang wird sie im Schrägbild mit q = 1/3 gezeichnet?', 2)
BF.stufe('laengen', 'Eine Kante führt 15 cm nach hinten. Wie lang wird sie im Schrägbild mit q = 2/3 gezeichnet?', 2)
# a) windschief → Stufe 2; dafür eine neue Stufe-1-Aufgabe (parallel), damit Stufe 1 mindestens 3 Übungen behält
_q = 'Quader ABCDEFGH (ABCD Grundfläche, E über A, F über B, G über C, H über D). '
BF.stufe('lage', _q + 'Wie liegen die Geraden BF und GH zueinander?', 2)
BF.stufe('lage', _q + 'Wie liegen die Geraden BF und DA zueinander?', 2)
_quader = {"typ": "figur", "punkte": {"A": [0, 0], "B": [5, 0], "C": [6.06, 1.06], "D": [1.06, 1.06], "E": [0, 2], "F": [5, 2], "G": [6.06, 3.06], "H": [1.06, 3.06]},
           "linien": [["A", "B"], ["B", "F"], ["F", "E"], ["E", "A"], ["B", "C"], ["C", "G"], ["G", "F"], ["E", "H"], ["H", "G"],
                      ["A", "D", "", "gestrichelt"], ["D", "C", "", "gestrichelt"], ["D", "H", "", "gestrichelt"]]}
BF.neu('lage', 1, BF.A(_q + 'Wie liegen die Geraden AB und DC zueinander?', 'parallel', ['identisch', 'windschief', 'schneiden sich'],
                       'AB und DC sind gegenüberliegende Kanten der Grundfläche ABCD: gleiche Richtung, kein gemeinsamer Punkt. Also parallel.',
                       'Stell dir den Quader vor (z. B. eine Schachtel). Haben die Geraden dieselbe Richtung? Gibt es einen gemeinsamen Punkt?', grafik=_quader))
BF.nicht_umgesetzt('koordinaten S2 „Gib die z-Koordinate von C an“ (3× gleicher Typ)', 'Laut Befund in Ordnung; Lösungen richtig.')
BF.nicht_umgesetzt('Karte „laengen“ ≈ messen.koerper_darstellung/„schraegbild“', 'Doppelung im Plan (Haupt-Chat), keine einzelne fehlerhafte Aufgabe.')
BF.fuer_sebastian('raum.schraegbilder: lehrplan_gym leer; Raumkoordinaten und windschiefe Geraden stehen im LehrplanPLUS Gymnasium nicht in Jgst. 8 – Thema im Plan als Vertiefung markieren? Karten-Texte nicht geändert.')

baue = mit_befunden(baue, BF)
# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Prismen und Pyramiden', ['pyramide', 'laengen']), ('Lage im Raum', ['lage', 'koordinaten']), ('Rotationskörper', ['rotation', 'axialschnitt'])],
         'Schrägbilder von Prismen und Pyramiden verstehen, Lagebeziehungen im Raum erkennen, Rotationskörper und Axialschnitte beschreiben und Punkte im Raum mit Koordinaten angeben.',
         ['Pyramide: n + 1 Ecken, 2n Kanten, n + 1 Flächen.', 'Schrägbild: parallel zur Zeichenebene wahr, nach hinten mit q verkürzt.',
          'Raum: parallel, schneidend oder windschief.', 'Rechteck → Zylinder, rechtwinkliges Dreieck → Kegel, Halbkreis → Kugel.'],
         vertiefung=('lage', 'koordinaten'),  # Vierzehnte Runde: windschiefe Geraden und Raumkoordinaten ohne Beleg in Gym 5–10, nicht Pflicht
         offen=['Schrägbilder werden jetzt mit dem Bildtyp „figur“ gezeigt (Pyramide, Quader, Rechteck an der Drehachse). Selbst zeichnen lassen kann die App noch nicht.',
                'Lehrplan: lehrplan_gym ist für dieses Thema leer. Laut Prüfung stehen Raumkoordinaten, windschiefe Geraden und Kegel/Axialschnitte eher in späteren Jahrgangsstufen – '
                'bitte im Aufbau klären, ob die Karten „lage“, „koordinaten“ und „axialschnitt“ bleiben.',
                'Prüfvorschlag „x-Achse schräg nach vorn, y nach rechts“ (Karte koordinaten) nicht umgesetzt: Er lohnt sich nur, wenn die Karte nach der Lehrplan-Klärung bleibt; '
                'das Bild der Prüfung zeigt selbst x nach rechts. Entscheidung beim Haupt-Chat.',
                'Überschneidung mit messen.koerper_darstellung: Schrägbild-Regeln für Prismen stehen dort, hier liegt der Schwerpunkt auf Pyramiden.'])


# ---------- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl10) ----------
# Gesamtdurchsicht (seit D2 Klasse 10): jede Lernkarte und jede Aufgabe gelesen und nachgerechnet. Läuft ganz am Ende auf der fertigen Datei.
# Stufe 1 = vorgerechnetes Beispiel mit anderen Zahlen, Stufe 2 = Abwandlung/Umkehrung, Stufe 3 = anderer Gedanke.
def durchsicht():
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _durchsicht_kl10 import Durchsicht
    D = Durchsicht('raum.schraegbilder', 19080)
    # pyramide: Kantensummen und Kantenzahl zweier Körper sind Anwendung der Kartenformel (Stufe 2)
    D.stufe([10, 12], 2, 'Eine ')
    D.stufe([11, 13], 2, 'Wie viele Kanten haben')
    # lage: Stufe 1 hatte nur 3 Übungen; zwei Kanten mit gemeinsamer Ecke sind der einfachste Fall → Stufe 1;
    # zwei Diagonalen durch dieselbe Ecke sind keine neue Idee → Stufe 2
    D.stufe([64, 68, 69], 1, 'Quader ABCDEFGH')
    D.stufe([70, 71], 2, 'Quader ABCDEFGH')
    # koordinaten: eine Koordinate ablesen ist leichter als Stufe 1 → Stufe 1; Mittelpunkt (Mittelwert der Koordinaten) → Stufe 2
    D.stufe(range(95, 101), 1, 'Ein Quader ABCDEFGH liegt so')
    D.stufe(range(101, 105), 2, 'Ein Quader ABCDEFGH liegt so')
    # rotation: Radius/Höhe aus dem Rechteck bzw. Dreieck ist das vorgerechnete Beispiel → Stufe 1;
    # Halbkreis-Radius und Durchmesser-Unterschied sind kleine Abwandlungen → Stufe 2
    D.stufe(range(125, 131), 1, 'Ein ')
    D.stufe(132, 2, 'Ein Rechteck 4 cm × 8 cm')
    D.stufe([133, 134], 2, 'Ein Halbkreis')
    # axialschnitt: Fläche beim Zylinder = Beispiel der Karte → Stufe 1; Umfang und Radius rückwärts = Abwandlung/Umkehrung → Stufe 2
    D.stufe([155, 157, 158], 1, 'Ein Zylinder hat')
    D.stufe([161, 162, 164], 2, 'Ein Zylinder hat')
    D.stufe(163, 2, 'Der Axialschnitt eines Zylinders')
    D.fuer_sebastian('raum.schraegbilder (seit D2 Klasse 10): Ecken/Kanten zählen, Schrägbild-Längen und Axialschnitte sind Klasse-5-bis-8-Niveau; '
                     'M10 5 verlangt Schrägbilder und Netze von Pyramide und Kegel (Kegel kann die App nicht zeichnen). In der Themendatei steht weiter klasse gym_by 8. '
                     'Überschneidung: Schrägbild der Pyramide auch in raum.pyramide_kegel_kugel/pyr_volumen.')
    D.anwenden()


if __name__ == '__main__':
    durchsicht()  # Neunzehnte Runde (durchsicht-kl10) – ganz am Ende


# ---------- STUFEN (Zwanzigste Runde, Zweig stufen-kl10) ----------
def stufen():
    import math
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _stufen_kl10 import Stufen
    S = Stufen('raum.schraegbilder', 2080)
    Z, A, L, ZR = S.Z, S.A, S.L, S.ZR

    # --- pyramide ---
    S.stufenleiter('pyramide', 'Ecken, Kanten und Flächen einer n-seitigen Pyramide zählen; Pyramiden erkennen.',
                   'Rückwärts zur Eckenzahl der Grundfläche, Körper aus Kennzahlen, Kantensummen, Prisma und Pyramide zusammen.',
                   'Eulersche Zahl, Drahtmodell, zusammengesetzte Körper, n als Parameter, Fehler beim Zählen, gerade Kantenzahl begründen, Seitenkante wie in der Prüfung.')
    S.g('pyramide', direkt=[0, 1, 2, 3], umkehr=[4, 6, 5, 8, 24], darstellung=[7, 9, 25], mehrschritt=[10, 12, 11, 13],
        verknuepfen=[26], transfer=[27, 28], parameter=[29])
    S.ueberzaehlig(2, 6, 8, 9, 13)
    S.neu('pyramide', 'erkennen', A('Welcher Körper hat genau eine Spitze und ein Vieleck als Grundfläche?', 'Pyramide', ['Prisma', 'Kegel', 'Zylinder'],
                                    'Ein Kegel hat eine Spitze, aber einen Kreis als Grundfläche. Prisma und Zylinder haben keine Spitze.', 'Achte auf Spitze und Grundfläche.'))
    S.neu('pyramide', 'erkennen', A('Was gilt für jede Pyramide?', 'Ihre Seitenflächen sind Dreiecke.', ['Ihre Grundfläche ist ein Quadrat.', 'Alle Kanten sind gleich lang.', 'Sie hat 5 Ecken.'],
                                    'Jede Seitenfläche verbindet eine Grundkante mit der Spitze: ein Dreieck. Die Grundfläche kann jedes Vieleck sein.', 'Denke an eine dreiseitige und eine sechsseitige Pyramide.'))
    S.neu('pyramide', 'fehler', A('Jemand sagt: „Eine sechsseitige Pyramide hat 6 Ecken, 6 Kanten und 6 Flächen.“ Was stimmt?', 'Falsch: Sie hat 7 Ecken, 12 Kanten und 7 Flächen.',
                                  ['Richtig.', 'Falsch: 6 Ecken, 12 Kanten, 6 Flächen.', 'Falsch: 7 Ecken, 6 Kanten, 7 Flächen.'],
                                  'Ecken: 6 + Spitze = 7. Kanten: 6 unten + 6 zur Spitze = 12. Flächen: 6 Dreiecke + Grundfläche = 7.', 'Vergiss Spitze, Seitenkanten und Grundfläche nicht.'))
    S.neu('pyramide', 'begruenden', A('Kann eine Pyramide 15 Kanten haben?', 'Nein: Eine n-seitige Pyramide hat 2n Kanten, also immer eine gerade Anzahl.',
                                      ['Ja, eine 15-seitige Pyramide.', 'Ja, eine 7,5-seitige Pyramide.', 'Nein, Pyramiden haben höchstens 12 Kanten.'],
                                      'n Grundkanten und n Seitenkanten: 2n. 15 ist ungerade.', 'Stelle die Kantenzahl mit n auf.'))
    S.neu('pyramide', 'rueckwaerts', Z('Bei einer Pyramide ergeben Ecken + Kanten + Flächen zusammen 50. Wie viele Ecken hat ihre Grundfläche?', 12, '(50 - 2) // 4',
                                       'Ecken n + 1, Kanten 2n, Flächen n + 1: zusammen 4n + 2 = 50 ⇒ n = 12.', 'Stelle alle drei Zahlen mit n auf.'))
    S.neu('pyramide', 'pruefung', ZR('Eine quadratische Pyramide hat die Grundkante 6 cm und die Höhe 4 cm. Wie lang ist eine Seitenkante? Runde auf eine Nachkommastelle.', math.sqrt(16 + 18), 1,
                                     'Halbe Diagonale der Grundfläche: 6 · √2 : 2 ≈ 4,24 cm. Seitenkante = √(4² + 4,24²) = √34 ≈ 5,8 cm.', 'Rechtwinkliges Dreieck aus Höhe, halber Diagonale und Seitenkante.', einheit='cm'))
    S.bonus('pyramide', Z('An allen 8 Ecken eines Würfels wird eine kleine Ecke so abgeschnitten, dass jeweils ein Dreieck als neue Fläche entsteht. Wie viele Kanten hat der neue Körper?', 36, '12 + 8 * 3',
                          'Die 12 Würfelkanten bleiben (gekürzt) erhalten. Jedes der 8 neuen Dreiecke bringt 3 neue Kanten: 12 + 24 = 36.', 'Welche Kanten bleiben, welche kommen dazu?'))
    S.bonus('pyramide', Z('Zwei gleiche quadratische Pyramiden werden mit ihren Grundflächen genau aufeinandergeklebt. Wie viele Kanten hat der neue Körper?', 12, '4 + 4 + 4',
                          'Die 4 Grundkanten werden gemeinsam genutzt, dazu je 4 Seitenkanten oben und unten: 4 + 4 + 4 = 12 (ein Oktaeder).', 'Welche Kanten fallen beim Kleben zusammen?'))

    # --- laengen ---
    S.stufenleiter('laengen', 'Im Schrägbild nach hinten führende Kanten mit q verkürzen, alle anderen in wahrer Länge zeichnen.',
                   'Wahre Tiefe aus der gezeichneten Länge, Summen gezeichneter Kanten, andere q, Maßstab.',
                   'Volumen aus dem Schrägbild, Restkörper und Oberfläche begründen, q als Parameter, Fehler bei senkrechten Kanten, gezeichnete Diagonale und Fläche mit Trigonometrie.')
    S.g('laengen', direkt=[30, 31, 33, 32, 40, 43, 41, 42], mehrschritt=[34, 37, 54], umkehr=[35, 36, 38, 39, 55],
        rueckwaerts=[56], verknuepfen=[57], begruenden=[58], transfer=[59])
    S.ueberzaehlig(33, 32, 43, 41, 42, 37)
    S.neu('laengen', 'erkennen', A('Welche Kanten zeichnet man im Schrägbild verkürzt?', 'nur die Kanten, die nach hinten führen', ['alle Kanten', 'nur die senkrechten Kanten', 'keine Kante'],
                                   'Breite und Höhe erscheinen in wahrer Länge; nur die Tiefe wird mit q verkürzt.', 'Was soll den räumlichen Eindruck erzeugen?'))
    S.neu('laengen', 'erkennen', A('Unter welchem Winkel ω zeichnet man im Schrägbild üblicherweise die nach hinten führenden Kanten?', '45°', ['90°', '30°', '60°'],
                                   'Üblich sind q = 1/2 und ω = 45°.', 'Denke an die Zeichnung auf Karopapier.'))
    S.neu('laengen', 'einkleidung', Z('Ein Schuhkarton (30 cm breit, 12 cm hoch, 18 cm tief) wird im Maßstab 1 : 3 als Schrägbild mit q = 1/2 gezeichnet. Wie lang zeichnest du die Tiefe?', 3, '18 / 3 / 2',
                                      'Maßstab: 18 cm : 3 = 6 cm; verkürzt mit q = 1/2: 3 cm.', 'Erst den Maßstab, dann q.', einheit='cm'))
    S.neu('laengen', 'fehler', A('Jemand zeichnet einen Würfel (Kante 4 cm) im Schrägbild mit q = 1/2 und zeichnet auch die senkrechten Kanten 2 cm lang. Was stimmt?',
                                 'Falsch: Nur die nach hinten führenden Kanten werden verkürzt; die senkrechten bleiben 4 cm.', ['Richtig.', 'Falsch: Alle Kanten müssen 2 cm lang sein.', 'Falsch: Die senkrechten Kanten müssen 8 cm lang sein.'],
                                 'Die Vorderfläche erscheint unverzerrt als Quadrat 4 cm × 4 cm.', 'Welche Richtung wird verkürzt?'))
    S.neu('laengen', 'parameter', L('Im Schrägbild eines Würfels mit 6 cm Kantenlänge sind die nach hinten führenden Kanten 4 cm lang gezeichnet. Welcher Verkürzungsfaktor q wurde verwendet?', 'q = □/□', [2, 3], ['2', '3'],
                                    'q = 4 : 6 = 2/3.', 'q = gezeichnete Länge : wahre Länge.', hinweis='gekürzter Bruch'))
    S.neu('laengen', 'pruefung', ZR('Ein Würfel mit 4 cm Kantenlänge wird im Schrägbild (q = 1/2, ω = 45°) gezeichnet. Wie lang ist im Bild die Diagonale AC der Grundfläche (A vorne links, C hinten rechts)? Runde auf eine Nachkommastelle.',
                                    math.hypot(4 + math.sqrt(2), math.sqrt(2)), 1,
                                    'Gezeichnet: AB = 4 cm waagrecht, BC = 2 cm unter 45°, also um √2 ≈ 1,41 cm nach rechts und nach oben. AC = √((4 + 1,41)² + 1,41²) ≈ √31,3 ≈ 5,6 cm (wahre Länge 5,66 cm).',
                                    'Zerlege die schräge Kante in einen waagrechten und einen senkrechten Anteil.', einheit='cm'))
    S.neu('laengen', 'verknuepfen', ZR('Ein Quader (6 cm breit, 4 cm tief) wird im Schrägbild mit q = 1/2 und ω = 45° gezeichnet. Wie groß ist die gezeichnete Grundfläche (ein Parallelogramm)? Runde auf eine Nachkommastelle.',
                                       6 * 2 * math.sin(math.radians(45)), 1, 'Seiten 6 cm und 2 cm, Winkel 45°: Höhe 2 · sin 45° ≈ 1,41 cm. Fläche 6 · 1,41 ≈ 8,5 cm² (wahre Fläche 24 cm²).',
                                       'Parallelogramm: Grundseite mal Höhe; die Höhe liefert der Sinus.', einheit='cm²'))
    S.bonus('laengen', ZR('Ein Würfel wird im Schrägbild mit q = 1/2 gezeichnet. Wie viel Prozent der Gesamtlänge aller 12 Kanten spart man beim Zeichnen? Runde auf eine Nachkommastelle.', 100 / 6, 1,
                          'Von 12 gleich langen Kanten führen 4 nach hinten und werden halb so lang. Gespart: 4 · 1/2 = 2 Kantenlängen von 12, also 1/6 ≈ 16,7 %.', 'Wie viele Kanten führen nach hinten?', einheit='%'))
    S.bonus('laengen', Z('Ein Quader ist 4 cm breit und 4 cm hoch. Im Schrägbild mit q = 1/2 sind alle gezeichneten Kanten gleich lang. Wie tief ist der Quader in Wirklichkeit?', 8, '4 * 2',
                         'Die Tiefe wird halbiert gezeichnet und soll 4 cm lang erscheinen: wahre Tiefe 8 cm. Das Bild sieht aus wie ein Würfel – ist aber keiner.', 'Rechne rückwärts mit q.', einheit='cm'))

    # --- lage ---
    S.stufenleiter('lage', 'Lage zweier Würfelkanten erkennen: schneidend, parallel oder windschief.',
                   'Diagonalen einbeziehen, gesuchte Kanten mit vorgegebener Lage finden, Gegenkanten.',
                   'Windschiefe Diagonalen, Anzahlen zählen, Fehler „nicht in einer Fläche“, Raumdiagonale berechnen, Winkel im Würfel wie in der Prüfung.')
    S.g('lage', erkennen=[62, 63, 64, 68, 69, 90, 65], direkt=[60, 61, 66, 67], mehrschritt=[70, 71], umkehr=[84, 72, 73], darstellung=[85],
        transfer=[86, 87, 88], begruenden=[89])
    S.ueberzaehlig(64, 68, 69, 65, 66, 67)
    S.neu('lage', 'fehler', A('Quader ABCDEFGH (ABCD unten, E über A, …). Jemand sagt: „AB und GH sind windschief, weil sie nicht in derselben Seitenfläche liegen.“ Was stimmt?',
                              'Falsch: AB und GH sind parallel; sie liegen in der Ebene durch A, B, G und H.', ['Richtig.', 'Falsch: Sie schneiden sich.', 'Falsch: Sie sind senkrecht zueinander.'],
                              'Beide verlaufen in Längsrichtung. Parallele Geraden liegen immer in einer gemeinsamen Ebene, auch wenn das keine Seitenfläche ist.', 'In welche Richtung verlaufen AB und GH?'))
    S.neu('lage', 'rueckwaerts', A('Quader ABCDEFGH (ABCD unten, E über A, F über B, G über C, H über D). Eine Strecke beginnt in E und ist windschief zu AB und zu BC. Welche kann es sein?', 'EG',
                                   ['EF', 'EH', 'EA'], 'EF ∥ AB, EH ∥ BC, EA schneidet AB. Die Flächendiagonale EG liegt oben, ist zu keiner der beiden parallel und trifft sie nicht.', 'Prüfe jede Strecke gegen AB und BC.'))
    S.neu('lage', 'verknuepfen', Z('Ein Quader hat die Kanten 3 cm, 4 cm und 12 cm. Wie lang ist eine Raumdiagonale?', 13, '13',
                                   'Grundflächendiagonale √(3² + 4²) = 5; Raumdiagonale √(5² + 12²) = √169 = 13 cm.', 'Zweimal Pythagoras.', einheit='cm'))
    S.neu('lage', 'pruefung', ZR('In einem Würfel ABCDEFGH: Wie groß ist der Winkel zwischen der Raumdiagonale AG und der Flächendiagonale AC? Runde auf eine Nachkommastelle.',
                                 math.degrees(math.atan(1 / math.sqrt(2))), 1, 'Dreieck ACG ist rechtwinklig bei C. Mit Kante a: AC = a√2, CG = a. tan α = a : (a√2) = 1/√2 ⇒ α ≈ 35,3°.',
                                 'Welches rechtwinklige Dreieck enthält beide Diagonalen?', einheit='°'))
    S.bonus('lage', Z('Wie viele Paare zueinander windschiefer Kanten hat ein Würfel?', 24, '12 * 4 // 2',
                      'Jede der 12 Kanten ist zu genau 4 Kanten windschief. 12 · 4 = 48 zählt jedes Paar doppelt: 24 Paare.', 'Zähle für eine Kante und achte auf doppelt gezählte Paare.'))
    S.bonus('lage', Z('Wie viele Paare zueinander paralleler Kanten hat ein Würfel?', 18, '3 * 6',
                      'Je 4 Kanten zeigen in dieselbe von 3 Richtungen. Aus 4 Kanten lassen sich 6 Paare bilden: 3 · 6 = 18.', 'Ordne die Kanten nach ihrer Richtung.'))

    # --- koordinaten ---
    S.stufenleiter('koordinaten', 'Ecken eines achsenparallelen Quaders ablesen und einzelne Koordinaten erkennen.',
                   'Mittelpunkte, Kantenlängen und Volumen aus Koordinaten, Punkte im Zimmer, Punkte auf Achsen.',
                   'Fehler beim Mittelpunkt, Würfel aus dem Mittelpunkt, Lage von Punkten begründen, Parameter auf einer Kante, Abstände, Winkel wie in der Prüfung.')
    S.g('koordinaten', direkt=[91, 92, 93, 94, 115], erkennen=[95, 96, 97, 100, 98, 99], mehrschritt=[101, 102, 103, 104, 118], umkehr=[116],
        fehler=[117], rueckwaerts=[119], transfer=[120])
    S.ueberzaehlig(92, 94, 96, 99, 100, 103, 104)
    S.neu('koordinaten', 'einkleidung', Z('Ein Zimmer ist 5 m lang, 4 m breit und 2,5 m hoch; eine Bodenecke ist der Ursprung. Eine Lampe hängt genau in der Mitte der Decke. Welche z-Koordinate hat sie?', 2.5, '2.5',
                                          'Die Decke liegt in der Höhe 2,5 m, also z = 2,5 (die Lampe hat die Koordinaten (2,5 | 2 | 2,5)).', 'z gibt die Höhe an.', einheit='m'))
    S.neu('koordinaten', 'darstellung', A('Welcher Punkt liegt auf der z-Achse?', '(0 | 0 | 4)', ['(4 | 0 | 0)', '(0 | 4 | 0)', '(4 | 4 | 4)'],
                                          'Auf der z-Achse sind x- und y-Koordinate 0.', 'Welche Koordinaten sind auf der z-Achse null?'))
    S.neu('koordinaten', 'parameter', Z('Quader mit A(0 | 0 | 0), B(4 | 0 | 0), D(0 | 6 | 0), E(0 | 0 | 3). Der Punkt P(4 | 3 | k) liegt auf der Kante FG. Bestimme k.', 3, '3',
                                        'F(4 | 0 | 3), G(4 | 6 | 3): Auf FG ist z immer 3. Also k = 3.', 'Bestimme zuerst F und G.'))
    S.neu('koordinaten', 'verknuepfen', Z('Wie lang ist die Strecke von A(0 | 0 | 0) zu G(2 | 3 | 6)?', 7, '7', '√(2² + 3² + 6²) = √49 = 7.', 'Raumdiagonale: zweimal Pythagoras.'))
    S.neu('koordinaten', 'pruefung', ZR('Ein Quader hat A(0 | 0 | 0) und G(8 | 6 | 5). Wie groß ist der Winkel zwischen der Raumdiagonale AG und der Grundfläche? Runde auf eine Nachkommastelle.',
                                        math.degrees(math.atan(5 / 10)), 1, 'AC = √(8² + 6²) = 10, CG = 5. tan α = 5 : 10 ⇒ α ≈ 26,6°.', 'Rechtwinkliges Dreieck ACG.', einheit='°'))
    S.neu('koordinaten', 'begruenden', A('Kann ein Punkt mit einer negativen Koordinate im Quader mit A(0 | 0 | 0) und G(4 | 6 | 2) liegen?', 'Nein: Alle Punkte dieses Quaders haben Koordinaten zwischen 0 und den Werten von G.',
                                         ['Ja, wenn die anderen Koordinaten klein genug sind.', 'Ja, auf der Kante AB.', 'Nur die z-Koordinate darf negativ sein.'],
                                         'Der Quader reicht in x von 0 bis 4, in y von 0 bis 6, in z von 0 bis 2.', 'Zwischen welchen Werten liegen x, y und z?'))
    S.neu('koordinaten', 'rueckwaerts', Z('M(2 | 5 | 1,5) ist der Mittelpunkt der Raumdiagonale AG eines Quaders mit A(0 | 0 | 0). Welches Volumen hat der Quader?', 120, '4 * 10 * 3',
                                          'G = 2 · M = (4 | 10 | 3). Volumen 4 · 10 · 3 = 120.', 'Verdopple die Koordinaten von M.'))
    S.bonus('koordinaten', Z('Wie viele Punkte mit ganzzahligen Koordinaten liegen im Würfel mit A(0 | 0 | 0) und G(2 | 2 | 2), Rand mitgezählt?', 27, '3 ** 3',
                             'Jede Koordinate kann 0, 1 oder 2 sein: 3 · 3 · 3 = 27 Punkte.', 'Wie viele Werte kann jede Koordinate annehmen?'))
    S.bonus('koordinaten', Z('Im Würfel mit A(0 | 0 | 0) und G(4 | 4 | 4): Wie viele Punkte mit ganzzahligen Koordinaten liegen auf der Oberfläche (Rand)?', 98, '5 ** 3 - 3 ** 3',
                             'Insgesamt 5³ = 125 Gitterpunkte (Werte 0 bis 4). Im Inneren liegen die mit Werten 1 bis 3: 3³ = 27. Auf dem Rand: 125 − 27 = 98.', 'Zähle alle und ziehe die inneren ab.'))

    # --- rotation ---
    S.stufenleiter('rotation', 'Erkennen, welcher Körper bei einer Drehung entsteht, und Radius und Höhe ablesen.',
                   'Unterschiede bei verschiedenen Drehachsen, Radius aus Durchmesser, Volumen und Grundfläche, Figur zu einem Körper.',
                   'Drehung um Mittellinie, Diagonale oder eine Achse außerhalb, Fehler „Kegel statt Doppelkegel“, Rechteck rückwärts, Kegelvolumen wie in der Prüfung.')
    S.g('rotation', erkennen=[121, 122, 123, 124, 146], direkt=[125, 128, 129, 126, 127, 130, 145], mehrschritt=[132], umkehr=[133, 134],
        begruenden=[131], transfer=[147, 148, 149], verknuepfen=[150])
    S.ueberzaehlig(124, 128, 127, 134)
    S.neu('rotation', 'einkleidung', ZR('Eine Vase entsteht, wenn sich ein Rechteck (12 cm hoch, 5 cm breit) um seine 12-cm-Seite dreht. Wie viel Wasser fasst sie höchstens? Runde auf ganze cm³.', math.pi * 25 * 12, 0,
                                        'Zylinder mit r = 5 cm und h = 12 cm: V = π · 5² · 12 ≈ 942 cm³.', 'Welche Seite wird zum Radius?', einheit='cm³'))
    S.neu('rotation', 'einkleidung', Z('Ein Kreisel entsteht, wenn sich ein rechtwinkliges Dreieck (Katheten 3 cm und 5 cm) um die 5-cm-Kathete dreht. Wie breit ist der Kreisel an der breitesten Stelle?', 6, '2 * 3',
                                       'Die 3-cm-Kathete wird zum Radius; der Durchmesser ist 6 cm.', 'Breite = Durchmesser.', einheit='cm'))
    S.neu('rotation', 'darstellung', A('Welche Figur muss man drehen, um einen Kegel mit r = 4 cm und h = 9 cm zu erhalten?', 'ein rechtwinkliges Dreieck mit den Katheten 4 cm und 9 cm, gedreht um die 9-cm-Kathete',
                                       ['dasselbe Dreieck, gedreht um die 4-cm-Kathete', 'ein Rechteck 4 cm × 9 cm, gedreht um die 9-cm-Seite', 'ein Halbkreis mit Radius 4 cm'],
                                       'Die Drehachse wird zur Höhe (9 cm), die andere Kathete zum Radius (4 cm).', 'Welche Seite liegt auf der Achse?'))
    S.neu('rotation', 'mehrschritt', ZR('Ein Rechteck 3 cm × 7 cm dreht sich um die 7-cm-Seite. Wie groß ist die Grundfläche des Zylinders? Runde auf eine Nachkommastelle.', math.pi * 9, 1,
                                        'r = 3 cm: G = π · 3² ≈ 28,3 cm².', 'Bestimme zuerst den Radius.', einheit='cm²'))
    S.neu('rotation', 'fehler', A('Jemand sagt: „Dreht sich ein rechtwinkliges Dreieck um seine Hypotenuse, entsteht ein Kegel.“ Was stimmt?', 'Falsch: Es entsteht ein Doppelkegel (zwei Kegel mit gemeinsamer Grundfläche).',
                                  ['Richtig.', 'Falsch: Es entsteht ein Zylinder.', 'Falsch: Es entsteht eine Kugel.'],
                                  'Die Ecke mit dem rechten Winkel liegt nicht auf der Achse; sie beschreibt einen Kreis – auf beiden Seiten entsteht eine Kegelspitze.', 'Welche Ecken liegen auf der Achse?'))
    S.neu('rotation', 'rueckwaerts', Z('Ein Zylinder mit r = 3 cm und h = 8 cm entstand durch Drehung eines Rechtecks um eine Seite. Welchen Flächeninhalt hatte das Rechteck?', 24, '3 * 8',
                                       'Das Rechteck hatte die Seiten r = 3 cm und h = 8 cm: 24 cm².', 'Welche Seiten hatte das Rechteck?', einheit='cm²'))
    S.neu('rotation', 'pruefung', Z('Ein rechtwinkliges Dreieck mit den Katheten 6 cm und 8 cm dreht sich um die 8-cm-Kathete. Wie weit ist die Spitze des entstehenden Kegels vom Rand seiner Grundfläche entfernt?',
                                    10, '10', 'Die Strecke von der Spitze zum Rand ist die Hypotenuse des gedrehten Dreiecks: √(6² + 8²) = √100 = 10 cm.',
                                    'Welche Seite des Dreiecks verbindet die Spitze mit dem Rand?', einheit='cm'))
    S.bonus('rotation', Z('Ein Quadrat (Seite 2 cm) dreht sich einmal um eine Seite und einmal um eine Mittellinie (parallel zu einer Seite). Wievielmal so groß ist das Volumen im ersten Fall?', 4, '(2 ** 2 * 2) // (1 ** 2 * 2)',
                          'Erster Fall: r = 2, h = 2, V = 8π. Zweiter Fall: r = 1, h = 2, V = 2π. Verhältnis 4 – halber Radius, Viertel Volumen.', 'Bestimme jeweils r und h.'))
    S.bonus('rotation', L('Ein Rechteck (3 cm × 4 cm) dreht sich einmal um die 3-cm-Seite und einmal um die 4-cm-Seite. In welchem Verhältnis stehen die Volumina der beiden Zylinder (erster : zweiter)?', '□ : □', [4, 3], ['4', '3'],
                          'Um die 3-cm-Seite: r = 4, h = 3, V = π · 16 · 3 = 48π. Um die 4-cm-Seite: r = 3, h = 4, V = π · 9 · 4 = 36π. 48π : 36π = 4 : 3. Der Radius zählt quadratisch, deshalb gewinnt der größere Radius.',
                          'Bestimme jeweils r und h.', hinweis='gekürztes Verhältnis'))

    # --- axialschnitt ---
    S.stufenleiter('axialschnitt', 'Die Form des Axialschnitts erkennen und Breite und Fläche beim Zylinder angeben.',
                   'Kegelfläche, Umfang, Radius rückwärts aus der Fläche, Kugel.',
                   'Zusammengesetzte Spielfigur, gleichseitiger und quadratischer Axialschnitt, Fehler „Radius statt Durchmesser“, rechtwinkliges Dreieck begründen, Mantellinie wie in der Prüfung.')
    S.g('axialschnitt', erkennen=[151, 152], direkt=[153, 154, 155, 157, 158], mehrschritt=[156, 159, 160, 175], umkehr=[161, 162, 164, 163], darstellung=[176],
        transfer=[177, 178], rueckwaerts=[179], verknuepfen=[180])
    S.ueberzaehlig(154, 158)
    S.neu('axialschnitt', 'fehler', A('Jemand berechnet den Axialschnitt eines Zylinders (r = 4 cm, h = 10 cm) als 4 · 10 = 40 cm². Was stimmt?', 'Falsch: Die Breite ist der Durchmesser 8 cm, also 80 cm².',
                                      ['Richtig.', 'Falsch: π · 4² · 10 ≈ 503 cm².', 'Falsch: 4 + 10 = 14 cm².'], 'Der Schnitt geht durch die Achse und erfasst den ganzen Durchmesser.', 'Wie breit ist der Schnitt?'))
    S.neu('axialschnitt', 'begruenden', A('Kann der Axialschnitt eines Kegels ein rechtwinkliges Dreieck sein?', 'Ja, wenn h = r ist; dann hat die Spitze einen rechten Winkel.',
                                          ['Nein, er ist immer gleichseitig.', 'Nein, er ist immer stumpfwinklig.', 'Ja, wenn h = 2r ist.'],
                                          'Halber Spitzenwinkel: tan φ = r : h. Für h = r ist φ = 45°, also der Spitzenwinkel 90°.', 'Betrachte das halbe Dreieck aus h, r und Mantellinie.'))
    S.neu('axialschnitt', 'parameter', Z('Der Axialschnitt eines Zylinders mit r = 5 cm ist ein Quadrat. Wie hoch ist der Zylinder?', 10, '2 * 5', 'Quadrat: Höhe = Breite = Durchmesser = 10 cm.', 'Wie breit ist der Axialschnitt?', einheit='cm'))
    S.neu('axialschnitt', 'pruefung', Z('Der Axialschnitt eines Kegels hat den Flächeninhalt 48 cm² und die Breite 12 cm. Wie lang ist eine Mantellinie?', 10, '10',
                                        'Dreieck: 1/2 · 12 · h = 48 ⇒ h = 8 cm. r = 6 cm. Mantellinie s = √(6² + 8²) = 10 cm.', 'Bestimme zuerst die Höhe aus der Dreiecksfläche.', einheit='cm'))
    S.bonus('axialschnitt', Z('Der Axialschnitt eines Zylinders hat den Umfang 40 cm. Bei welcher Höhe ist seine Fläche am größten?', 10, '40 / 4',
                              'Umfang 2 · (2r + h) = 40 ⇒ 2r + h = 20. Schreibe 2r = 10 + d und h = 10 − d. Dann ist die Fläche 2r · h = (10 + d)(10 − d) = 100 − d². '
                              'Sie ist am größten für d = 0: 2r = h = 10 cm (ein Quadrat).',
                              'Probiere einige Paare (Breite, Höhe) mit Summe 20.', einheit='cm'))
    S.bonus('axialschnitt', Z('Ein Kegel und ein Zylinder haben denselben Radius und dieselbe Höhe. Wievielmal so groß ist der Axialschnitt des Zylinders wie der des Kegels?', 2, '2',
                              'Zylinder: Rechteck 2r · h. Kegel: Dreieck 1/2 · 2r · h = r · h. Verhältnis 2.', 'Vergleiche Rechteck und Dreieck mit gleicher Grundseite und Höhe.'))
    S.anwenden()


if __name__ == '__main__':
    stufen()  # Zwanzigste Runde (stufen-kl10) – ganz am Ende


# ---- BEREINIGEN (Einundzwanzigste Runde) ----
if __name__ == '__main__':
    from _bereinigen import bereinigen_datei
    bereinigen_datei('raum.schraegbilder')
# ---- BEREINIGEN ENDE ----

# ---- LK (22.11., Lücken aus LP-RS, siehe _lk_etappen_2211.py): zuletzt, hängt nur an ----
if __name__ == '__main__':
    from _lk_etappen_2211 import lk_anhaengen
    lk_anhaengen('raum.schraegbilder')
# ---- LK ENDE ----

# ---- NT-D (22.11., siehe _nt_2211.py): zuletzt, hängt nur Aufgaben an ----
if __name__ == '__main__':
    from _nt_2211 import nt_anhaengen
    nt_anhaengen('raum.schraegbilder')
# ---- NT ENDE ----

# ---- NT-D 3 (23.11., siehe _nt_2311.py): zuletzt, hängt nur Aufgaben an ----
if __name__ == '__main__':
    from _nt_2311 import nt_anhaengen as nt3_anhaengen
    nt3_anhaengen('raum.schraegbilder')
# ---- NT-D 3 ENDE ----
