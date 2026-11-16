#!/usr/bin/env python3
"""Thema messen.koerper_berechnung – Quader und Würfel (Klasse 5): Eigenschaften, Oberflächeninhalt, zusammengesetzte Körper;
Volumen als Vertiefung. Prisma, Zylinder, Pyramide, Kegel und Kugel sind Stoff späterer Jahrgangsstufen."""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl5_rest import *  # noqa: E402,F403

R = random.Random(53)
E = eintrag_laden('messen.koerper_berechnung')


def tab_o(a, b, c, e='cm', frage=False):
    zeilen = [['vorne und hinten', '2', f'{a} {e} · {c} {e}', '?' if frage else f'{2 * a * c} {e}²'],
              ['oben und unten', '2', f'{a} {e} · {b} {e}', '?' if frage else f'{2 * a * b} {e}²'],
              ['links und rechts', '2', f'{b} {e} · {c} {e}', '?' if frage else f'{2 * b * c} {e}²']]
    return {'typ': 'tabelle', 'kopf': ['Flächenpaar', 'Anzahl', 'Größe einer Fläche', 'zusammen'], 'zeilen': zeilen}


ETAPPEN = [
    {'lernziel': 'quader', 'titel': 'Quader und Würfel beschreiben',
     'regel': 'Ein ⟦Quader⟧ hat ⟦6 rechteckige Flächen⟧, ⟦12 Kanten⟧ und ⟦8 Ecken⟧. Gegenüberliegende Flächen sind gleich groß. Je 4 Kanten sind gleich lang (Länge a, Breite b, Höhe c). Beim ⟦Würfel⟧ sind alle 12 Kanten gleich lang, alle 6 Flächen sind Quadrate.',
     'schritte': ['Ein Quader ist 5 cm lang, 3 cm breit und 2 cm hoch. Je 4 Kanten haben dieselbe Länge.', 'Kantenlänge insgesamt: 4 · 5 + 4 · 3 + 4 · 2 = ⟦40 cm⟧.'],
     'fehler': '5 + 3 + 2 = 10 cm als Länge aller Kanten ist falsch: Jede Kantenlänge kommt ⟦viermal⟧ vor, also 4 · (5 + 3 + 2) = 40 cm.'},
    {'lernziel': 'oberflaeche', 'titel': 'Oberflächeninhalt des Quaders',
     'regel': 'Der ⟦Oberflächeninhalt⟧ O ist die Summe aller 6 Flächen. Beim Quader gibt es ⟦3 Paare⟧ gleich großer Rechtecke: ⟦O = 2 · a · b + 2 · a · c + 2 · b · c⟧. Beim Würfel: ⟦O = 6 · a · a⟧.',
     'schritte': ['Quader: a = 5 cm, b = 3 cm, c = 2 cm. Paare: 2 · 5 · 3 = 30, 2 · 5 · 2 = 20, 2 · 3 · 2 = 12.', 'O = 30 + 20 + 12 = ⟦62 cm²⟧.'],
     'bild': tab_o(5, 3, 2),
     'fehler': 'Nur die drei sichtbaren Flächen zu addieren (15 + 10 + 6 = 31 cm²) ist falsch: Jede Fläche hat ein ⟦Gegenüber⟧. Es sind ⟦6⟧ Flächen, also doppelt so viel.'},
    {'lernziel': 'sachaufgaben', 'titel': 'Oberflächen im Alltag',
     'regel': 'Überlege bei Sachaufgaben, ⟦welche Flächen wirklich gebraucht werden⟧: Ein Aquarium hat ⟦keinen Deckel⟧, ein Zimmer wird ⟦ohne Boden⟧ gestrichen, Fenster und Türen werden abgezogen.',
     'schritte': ['Ein Aquarium ohne Deckel: 60 cm lang, 30 cm breit, 40 cm hoch. Boden: 60 · 30 = 1 800 cm².', 'Wände: 2 · 60 · 40 + 2 · 30 · 40 = 4 800 + 2 400 = 7 200 cm². Glas: 1 800 + 7 200 = ⟦9 000 cm²⟧.'],
     'fehler': 'Die volle Oberfläche zu nehmen, obwohl der Deckel fehlt, ist falsch: Zieh die ⟦fehlenden Flächen⟧ ab oder addiere nur die vorhandenen.'},
    {'lernziel': 'zusammengesetzt', 'titel': 'Zusammengesetzte Körper',
     'regel': 'Setzt man Körper zusammen, verschwinden die ⟦Berührflächen⟧ – sie liegen innen. Oberfläche = Summe der Einzeloberflächen ⟦minus 2-mal jede Berührfläche⟧. Bei Würfelreihen kannst du auch die ⟦sichtbaren Quadrate zählen⟧.',
     'schritte': ['3 Würfel mit 1 cm Kantenlänge in einer Reihe. Einzeln: 3 · 6 = 18 Quadrate.', 'Zwei Berührstellen verdecken je 2 Quadrate: 18 − 4 = ⟦14 cm²⟧.'],
     'fehler': 'Einfach 3 · 6 cm² = 18 cm² zu rechnen ist falsch: Die Flächen, an denen die Würfel ⟦aneinanderstoßen⟧, gehören nicht mehr zur Oberfläche.'},
    {'lernziel': 'volumen', 'titel': 'Volumen von Quader und Würfel',
     'regel': 'Das ⟦Volumen⟧ (Rauminhalt) sagt, wie viele ⟦Einheitswürfel⟧ in einen Körper passen. Ein Würfel mit 1 cm Kantenlänge hat das Volumen ⟦1 cm³⟧. Quader: ⟦V = a · b · c⟧, Würfel: ⟦V = a · a · a⟧.',
     'schritte': ['Quader 5 cm × 3 cm × 2 cm: Eine Schicht hat 5 · 3 = 15 Würfel, es gibt 2 Schichten.', 'V = 15 · 2 = ⟦30 cm³⟧.'],
     'fehler': 'Volumen und Oberfläche zu verwechseln ist falsch: Das Volumen zählt ⟦Würfel⟧ (cm³), die Oberfläche zählt ⟦Quadrate⟧ (cm²).'},
    {'lernziel': 'verstehen', 'titel': 'Quader-Aussagen prüfen',
     'regel': 'Prüfe Aussagen über Körper mit einem ⟦Zahlenbeispiel⟧ oder durch ⟦Abzählen⟧ an einem Würfel. Achte darauf, ob nach Kanten (cm), Flächen (cm²) oder Volumen (cm³) gefragt ist.',
     'schritte': ['Aussage: „Ein Würfel mit doppelter Kantenlänge hat die doppelte Oberfläche.“ Beispiel: a = 1 cm, O = 6 cm².', 'a = 2 cm: O = 6 · 2 · 2 = 24 cm², also ⟦viermal⟧ so viel. Die Aussage ist falsch.'],
     'fehler': 'Kantenlänge, Oberfläche und Volumen wachsen ⟦verschieden⟧ schnell. Bei doppelter Kantenlänge: Kanten doppelt, Oberfläche ⟦vierfach⟧, Volumen ⟦achtfach⟧.'},
]

PRUEFUNG = pruefung_erklaerungen(ETAPPEN, 'messen.koerper_berechnung')   # Schrägbilder in quader und zusammengesetzt

MERKE = ['Quader: 6 Flächen, 12 Kanten, 8 Ecken. Kantenlänge gesamt: 4 · (a + b + c).', 'Oberfläche Quader: O = 2ab + 2ac + 2bc. Würfel: O = 6a².',
         'Zusammengesetzt: Berührflächen fallen weg (je zweimal).', 'Volumen Quader: V = a · b · c (cm³). Würfel: V = a³.']


def schraeg(a, b, c, e='cm'):
    """Schrägbild eines Quaders (Tiefe halb so lang unter 45°, verdeckte Kanten gestrichelt) – wie das Bild der Prüfung."""
    import math
    t = round(b * .5 * math.cos(math.radians(45)), 3)
    pk = {'_A': [0, 0], '_B': [a, 0], '_C': [a + t, t], '_D': [t, t], '_E': [0, c], '_F': [a, c], '_G': [a + t, c + t], '_H': [t, c + t]}
    lin = [['_A', '_B', f'{a} {e}'], ['_B', '_F', f'{c} {e}'], ['_F', '_E'], ['_E', '_A'], ['_B', '_C', f'{b} {e}'], ['_C', '_G'], ['_G', '_F'], ['_E', '_H'], ['_H', '_G'],
           ['_A', '_D', '', 'gestrichelt'], ['_D', '_C', '', 'gestrichelt'], ['_D', '_H', '', 'gestrichelt']]
    return {'typ': 'figur', 'punkte': pk, 'linien': lin}


def sort2(a, b):
    """„lang“ ist die längere Seite (Prüfung)."""
    return (a, b) if a >= b else (b, a)


# ---------- Würfelnetze (Figur aus Linien; Prüfung: Würfelnetz prüfen) ----------
def _rolle(zellen):
    """Rollt einen Würfel über die Zellen: Netz genau dann, wenn dabei jede Würfelfläche einmal unten liegt."""
    zellen = set(zellen)
    start = min(zellen)
    lage = {start: {'u': 0, 'o': 1, 'n': 2, 's': 3, 'w': 4, 'e': 5}}
    stapel = [start]
    while stapel:
        x, y = stapel.pop(); f = lage[(x, y)]
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            z = (x + dx, y + dy)
            if z not in zellen or z in lage: continue
            if dx == 1: g = {'u': f['e'], 'e': f['o'], 'o': f['w'], 'w': f['u'], 'n': f['n'], 's': f['s']}
            elif dx == -1: g = {'u': f['w'], 'w': f['o'], 'o': f['e'], 'e': f['u'], 'n': f['n'], 's': f['s']}
            elif dy == 1: g = {'u': f['n'], 'n': f['o'], 'o': f['s'], 's': f['u'], 'e': f['e'], 'w': f['w']}
            else: g = {'u': f['s'], 's': f['o'], 'o': f['n'], 'n': f['u'], 'e': f['e'], 'w': f['w']}
            lage[z] = g; stapel.append(z)
    return len(lage) == 6 and len({v['u'] for v in lage.values()}) == 6


def _hexomino():
    zellen = {(0, 0)}
    while len(zellen) < 6:
        x, y = R.choice(sorted(zellen)); dx, dy = R.choice(((1, 0), (-1, 0), (0, 1), (0, -1)))
        zellen.add((x + dx, y + dy))
    mx, my = min(x for x, _ in zellen), min(y for _, y in zellen)
    return frozenset((x - mx, y - my) for x, y in zellen)


def netzbild(zellen):
    pk, lin, kanten = {}, [], set()
    for x, y in zellen:
        for (x1, y1), (x2, y2) in (((x, y), (x + 1, y)), ((x + 1, y), (x + 1, y + 1)), ((x, y + 1), (x + 1, y + 1)), ((x, y), (x, y + 1))):
            k = ((x1, y1), (x2, y2))
            if k in kanten: continue
            kanten.add(k)
            for q in k: pk.setdefault(f'_{q[0]}_{q[1]}', list(q))
            lin.append([f'_{x1}_{y1}', f'_{x2}_{y2}'])
    return {'typ': 'figur', 'punkte': pk, 'linien': lin}


NETZE = {'ja': 0}


def g_netz():
    soll = NETZE['ja'] % 2 == 0; NETZE['ja'] += 1          # abwechselnd Netz / kein Netz
    for _ in range(500):
        z = _hexomino()
        if _rolle(z) == soll and max(x for x, _ in z) <= 4 and max(y for _, y in z) <= 4: break
    r, f = ('Ja, beim Falten liegt jede Fläche an einer anderen Stelle.', ['Nein, zwei Flächen liegen beim Falten aufeinander.', 'Nein, ein Würfelnetz braucht 8 Quadrate.']) if soll else \
        ('Nein, beim Falten liegen zwei Quadrate aufeinander, eine Würfelfläche bleibt offen.', ['Ja, es sind 6 Quadrate, das reicht immer.', 'Ja, alle Quadrate hängen zusammen.'])
    return {**wahl_rund(R, r, f, 3), 'f': {'text': 'Ist das ein Würfelnetz? Stell dir vor, du faltest es zu einem Würfel.', 'grafik': netzbild(sorted(z))},
            'w': r + ' Sechs zusammenhängende Quadrate allein reichen nicht: Beim Falten muss jedes Quadrat eine eigene Würfelfläche werden.',
            'h': 'Wähle ein Quadrat als Boden und falte die anderen gedanklich hoch. Liegen zwei aufeinander?'}


def qtxt(a, b, c, e='cm'): return f'{a} {e} lang, {b} {e} breit und {c} {e} hoch'


def O(a, b, c): return 2 * (a * b + a * c + b * c)


# ---------- 1 Quader ----------
def g_quader(st):
    if st == 1:
        fr = [('Wie viele Ecken hat ein Quader?', 8, 'Ein Quader hat 8 Ecken: 4 unten und 4 oben.'), ('Wie viele Kanten hat ein Quader?', 12, 'Ein Quader hat 12 Kanten: 4 unten, 4 oben, 4 senkrecht.'),
              ('Wie viele Flächen hat ein Quader?', 6, 'Ein Quader hat 6 Flächen: vorne, hinten, oben, unten, links, rechts.'),
              ('Wie viele Kanten treffen sich an einer Ecke eines Würfels?', 3, 'An jeder Ecke treffen sich 3 Kanten (Länge, Breite, Höhe).'),
              ('Wie viele Flächen eines Würfels sind Quadrate?', 6, 'Beim Würfel sind alle 6 Flächen Quadrate.')]
        if R.random() < .35:
            t, r, w = R.choice(fr)
            return {'y': 'zahl', 'f': {'text': t}, 'o': {'wert': r}, 'c': f'{r}', 'w': w, 'h': 'Stell dir eine Schachtel vor und zähle.'}
        if R.random() < .55:          # Ecken/Kanten/Flächen zählen am konkreten Quader (Prüfung)
            a, b = sort2(R.randint(3, 12), R.randint(2, 9)); c = R.randint(2, 15)
            if len({a, b, c}) < 3: return g_quader(st)
            t, r, w = R.choice([(f'Ein Quader ist {qtxt(a, b, c)}. Wie viele seiner Flächen sind {a} cm × {b} cm groß?', 2, f'Oben und unten sind {a} cm × {b} cm groß: 2 Flächen.'),
                                (f'Ein Quader ist {qtxt(a, b, c)}. Wie viele seiner Kanten sind {c} cm lang?', 4, f'Die 4 senkrechten Kanten sind {c} cm lang.'),
                                (f'Ein Quader ist {qtxt(a, b, c)}. Wie viele seiner Flächen sind {b} cm × {c} cm groß?', 2, f'Links und rechts sind {b} cm × {c} cm groß: 2 Flächen.')])
            return {'y': 'zahl', 'f': {'text': t, 'grafik': schraeg(a, b, c)}, 'o': {'wert': r}, 'c': f'{r}', 'w': w, 'h': 'Gegenüberliegende Flächen sind gleich groß. Je 4 Kanten sind gleich lang.'}
        a = R.randint(2, 15)
        return {'y': 'zahl', 'f': {'text': f'Ein Würfel hat die Kantenlänge {a} cm. Wie lang sind alle Kanten zusammen?'}, 'o': {'wert': 12 * a, 'einheit': 'cm'}, 'c': f'12 * {a}',
                'w': f'12 gleich lange Kanten: 12 · {a} = {12 * a} cm.', 'h': 'Ein Würfel hat 12 gleich lange Kanten.'}
    a, b, c = R.randint(2, 15), R.randint(2, 12), R.randint(2, 10)
    a, b = sort2(a, b)
    if st == 2:
        return {'y': 'zahl', 'f': {'text': f'Ein Quader ist {qtxt(a, b, c)}. Wie lang sind alle Kanten zusammen?', 'grafik': schraeg(a, b, c)}, 'o': {'wert': 4 * (a + b + c), 'einheit': 'cm'}, 'c': f'4 * ({a} + {b} + {c})',
                'w': f'Je 4 Kanten gleich: 4 · ({a} + {b} + {c}) = 4 · {a + b + c} = {4 * (a + b + c)} cm.', 'h': 'Jede der drei Kantenlängen kommt viermal vor.'}
    art = R.randrange(4)
    if art == 3: return g_netz()
    if art == 0:
        ges = 4 * (a + b + c)
        return {'y': 'zahl', 'f': {'text': f'Für ein Kantenmodell eines Quaders ({a} cm lang, {b} cm breit) braucht man {ges} cm Draht. Wie hoch ist der Quader?'},
                'o': {'wert': c, 'einheit': 'cm'}, 'c': f'{ges} / 4 - {a} - {b}', 'w': f'{ges} : 4 = {a + b + c} cm für a + b + c. Höhe: {a + b + c} − {a} − {b} = {c} cm.', 'h': 'Teile die Drahtlänge zuerst durch 4.'}
    if art == 1:
        return {'y': 'zahl', 'f': {'text': f'Ein Quader ist {qtxt(a, b, c)}. Wie groß ist die größte Seitenfläche?'}, 'o': {'wert': max(a * b, a * c, b * c), 'einheit': 'cm²'},
                'c': f'max({a} * {b}, {a} * {c}, {b} * {c})', 'w': f'Flächen: {a} · {b} = {a * b}, {a} · {c} = {a * c}, {b} · {c} = {b * c}. Am größten: {max(a * b, a * c, b * c)} cm².',
                'h': 'Es gibt drei verschiedene Rechtecke. Berechne alle drei.'}
    s = R.randint(2, 9)
    return {'y': 'zahl', 'f': {'text': f'Aus {12 * s} cm Draht wird das Kantenmodell eines Würfels gebogen. Wie lang ist eine Kante?'}, 'o': {'wert': s, 'einheit': 'cm'}, 'c': f'{12 * s} / 12',
            'w': f'12 gleiche Kanten: {12 * s} : 12 = {s} cm.', 'h': 'Ein Würfel hat 12 gleich lange Kanten.'}


# ---------- 2 Oberfläche ----------
def g_ober(st):
    if st == 1:
        if R.random() < .5:
            a = R.randint(2, 12)
            return {'y': 'zahl', 'f': {'text': f'Berechne die Oberfläche eines Würfels mit der Kantenlänge {a} cm.'}, 'o': {'wert': 6 * a * a, 'einheit': 'cm²'}, 'c': f'6 * {a} * {a}',
                    'w': f'Eine Fläche: {a} · {a} = {a * a} cm². Sechs Flächen: 6 · {a * a} = {6 * a * a} cm².', 'h': 'Ein Würfel hat 6 gleich große Quadrate.'}
        a, b, c = R.randint(2, 8), R.randint(2, 6), R.randint(1, 5)
        return {'y': 'zahl', 'f': {'text': f'Ein Quader ist {qtxt(a, b, c)}. Berechne die Oberfläche. Die Tabelle hilft.', 'grafik': tab_o(a, b, c, frage=True)},
                'o': {'wert': O(a, b, c), 'einheit': 'cm²'}, 'c': f'2 * {a} * {b} + 2 * {a} * {c} + 2 * {b} * {c}',
                'w': f'2 · {a * c} + 2 · {a * b} + 2 · {b * c} = {2 * a * c} + {2 * a * b} + {2 * b * c} = {O(a, b, c)} cm².', 'h': 'Berechne die drei Flächenpaare und addiere.'}
    a, b, c = R.randint(3, 20), R.randint(2, 15), R.randint(2, 12)
    a, b = sort2(a, b)
    if st == 2:
        e = R.choice(['cm', 'dm', 'm'])
        return {'y': 'zahl', 'f': {'text': f'Ein Quader ist {qtxt(a, b, c, e)}. Berechne den Oberflächeninhalt.'}, 'o': {'wert': O(a, b, c), 'einheit': e + '²'},
                'c': f'2 * {a} * {b} + 2 * {a} * {c} + 2 * {b} * {c}', 'w': f'O = 2 · {a} · {b} + 2 · {a} · {c} + 2 · {b} · {c} = {2 * a * b} + {2 * a * c} + {2 * b * c} = {O(a, b, c)} {e}².',
                'h': 'O = 2ab + 2ac + 2bc.'}
    art = R.randrange(3)
    if art == 0:
        s = R.randint(2, 15)
        return {'y': 'zahl', 'f': {'text': f'Ein Würfel hat die Oberfläche {6 * s * s} cm². Wie lang ist eine Kante?'}, 'o': {'wert': s, 'einheit': 'cm'}, 'c': f'{s}',
                'w': f'Eine Fläche: {6 * s * s} : 6 = {s * s} cm². {s} · {s} = {s * s}, also a = {s} cm.', 'h': 'Teile durch 6 und überlege, welche Quadratzahl herauskommt.'}
    if art == 1:
        a2, b2 = R.randint(1, 9), R.randint(1, 9)
        c2 = R.randint(10, 40)
        return {'y': 'zahl', 'f': {'text': f'Ein Quader ist {a2} dm lang, {b2} dm breit und {c2} cm hoch. Berechne die Oberfläche in cm².'}, 'o': {'wert': O(a2 * 10, b2 * 10, c2), 'einheit': 'cm²'},
                'c': f'2 * {a2 * 10} * {b2 * 10} + 2 * {a2 * 10} * {c2} + 2 * {b2 * 10} * {c2}', 'w': f'In cm: {a2 * 10}, {b2 * 10}, {c2}. O = {2 * a2 * b2 * 100} + {2 * a2 * 10 * c2} + {2 * b2 * 10 * c2} = {zt(O(a2 * 10, b2 * 10, c2))} cm².',
                'h': 'Rechne zuerst alle Kanten in cm um.'}
    x = R.randint(2, 6)
    return {'y': 'zahl', 'f': {'text': f'Die Kantenlänge eines Würfels wird von {x} cm auf {2 * x} cm verdoppelt. Wie viel Mal so groß wird die Oberfläche?'}, 'o': {'wert': 4}, 'c': f'(6 * {2 * x} * {2 * x}) / (6 * {x} * {x})',
            'w': f'Vorher 6 · {x * x} = {6 * x * x} cm², nachher 6 · {4 * x * x} = {24 * x * x} cm²: viermal so groß.', 'h': 'Berechne beide Oberflächen.'}


# ---------- 3 Sachaufgaben ----------
SACH = {'aquarium': 0}


def g_sach(st):
    if st == 1:
        a, b, c = R.randint(20, 60), R.randint(15, 40), R.randint(10, 30)
        a, b = sort2(a, b)
        return {'y': 'zahl', 'f': {'text': f'Ein Geschenkkarton ist {qtxt(a, b, c)}. Wie viel cm² Papier braucht man mindestens, um ihn ganz zu bekleben?'}, 'o': {'wert': O(a, b, c), 'einheit': 'cm²'},
                'c': f'2 * {a} * {b} + 2 * {a} * {c} + 2 * {b} * {c}', 'w': f'Oberfläche: {2 * a * b} + {2 * a * c} + {2 * b * c} = {zt(O(a, b, c))} cm².', 'h': 'Ganz bekleben heißt: alle 6 Flächen.'}
    if st == 2 and (SACH['aquarium'] >= 5 or R.random() < .5):          # höchstens 5 Aquarium-Aufgaben, weitere Kontexte (Prüfung)
        art = R.randrange(2)
        if art == 0:
            a, b, c = sort2(R.choice([28, 30, 32, 35]), R.choice([18, 20, 22])) + (R.choice([10, 12, 14]),)
            ob = a * b + 2 * a * c + 2 * b * c
            return {'y': 'zahl', 'f': {'text': f'Ein Schuhkarton ohne Deckel ist {qtxt(a, b, c)}. Er wird innen mit Stoff ausgekleidet. Wie viel cm² Stoff braucht man?'},
                    'o': {'wert': ob, 'einheit': 'cm²'}, 'c': f'{a} * {b} + 2 * {a} * {c} + 2 * {b} * {c}',
                    'w': f'Boden {a} · {b} = {a * b}, vorne/hinten 2 · {a * c} = {2 * a * c}, Seiten 2 · {b * c} = {2 * b * c}. Zusammen {zt(ob)} cm².', 'h': 'Alle Flächen außer dem Deckel.'}
        a, b, c = R.choice([(12, 6, 20), (10, 6, 18), (14, 6, 20), (8, 5, 20)])          # Schrank in dm
        ob = 2 * a * c + 2 * b * c + a * b
        return {'y': 'zahl', 'f': {'text': f'Ein Schrank ist {qtxt(a, b, c, "dm")}. Er wird außen gestrichen, aber nicht auf der Rückseite und nicht unten. Wie viele dm² werden gestrichen?'},
                'o': {'wert': a * c + 2 * b * c + a * b, 'einheit': 'dm²'}, 'c': f'{a} * {c} + 2 * {b} * {c} + {a} * {b}',
                'w': f'Vorne {a} · {c} = {a * c}, zwei Seiten 2 · {b} · {c} = {2 * b * c}, oben {a} · {b} = {a * b}. Zusammen {zt(a * c + 2 * b * c + a * b)} dm².',
                'h': 'Welche Flächen werden gestrichen? Vorne, zwei Seiten, oben.'}
    if st == 2:
        SACH['aquarium'] += 1
        a, b, c = R.choice([40, 50, 60, 80, 100]), R.choice([25, 30, 40, 50]), R.choice([30, 40, 50])
        a, b = sort2(a, b)
        ob = a * b + 2 * a * c + 2 * b * c
        return {'y': 'zahl', 'f': {'text': f'Ein Aquarium ohne Deckel ist {qtxt(a, b, c)}. Wie viel cm² Glas braucht man?'}, 'o': {'wert': ob, 'einheit': 'cm²'},
                'c': f'{a} * {b} + 2 * {a} * {c} + 2 * {b} * {c}', 'w': f'Boden {a * b}, vorne/hinten 2 · {a * c} = {2 * a * c}, Seiten 2 · {b * c} = {2 * b * c}. Zusammen {zt(ob)} cm².',
                'h': 'Alle Flächen außer dem Deckel.'}
    art = R.randrange(3)
    if art == 2:          # Verpackung mit Überlappung (Prüfung)
        a, b, c = R.choice([(30, 20, 10), (40, 30, 10), (20, 20, 10), (50, 30, 20), (40, 20, 20)])
        o = O(a, b, c)
        return {'y': 'zahl', 'f': {'text': f'Ein Karton {a} cm × {b} cm × {c} cm wird ganz beklebt. Für Überlappungen rechnet man ein Zehntel der Oberfläche dazu. Wie viel cm² Papier braucht man?'},
                'o': {'wert': o + o // 10, 'einheit': 'cm²'}, 'c': f'2 * ({a} * {b} + {a} * {c} + {b} * {c}) * 11 / 10',
                'w': f'Oberfläche: 2 · ({a * b} + {a * c} + {b * c}) = {zt(o)} cm². Ein Zehntel: {zt(o // 10)} cm². Zusammen {zt(o + o // 10)} cm².',
                'h': 'Erst die Oberfläche, dann ein Zehntel davon dazurechnen.'}
    if art == 0:
        l, b, h = R.randint(4, 7), R.randint(3, 5), R.choice([Fr(5, 2), 3])
        t = 2
        w = 2 * l * h + 2 * b * h - t + l * b
        return {'y': 'zahl', 'f': {'text': f'Ein Zimmer ist {l} m lang, {b} m breit und {zt(h)} m hoch. Wände und Decke werden gestrichen, Boden nicht. Tür und Fenster ({t} m² zusammen) bleiben frei. Wie viele m² werden gestrichen?'},
                'o': {'wert': wert(w), 'einheit': 'm²'}, 'c': f'2 * {l} * {float(h)} + 2 * {b} * {float(h)} + {l} * {b} - {t}',
                'w': f'Wände: 2 · {l} · {zt(h)} + 2 · {b} · {zt(h)} = {zt(2 * l * h + 2 * b * h)} m². Decke: {l * b} m². Minus {t} m²: {zt(w)} m².', 'h': 'Welche Flächen werden gestrichen, welche nicht?'}
    a = R.randint(3, 8)
    n = R.randint(4, 10)
    return {'y': 'zahl', 'f': {'text': f'{n} Holzwürfel mit {a} cm Kantenlänge werden einzeln ganz rot angemalt. Wie viel cm² werden angemalt?'}, 'o': {'wert': n * 6 * a * a, 'einheit': 'cm²'},
            'c': f'{n} * 6 * {a} * {a}', 'w': f'Ein Würfel: 6 · {a * a} = {6 * a * a} cm². {n} Würfel: {n} · {6 * a * a} = {zt(n * 6 * a * a)} cm².', 'h': 'Erst die Oberfläche eines Würfels.'}


# ---------- 4 Zusammengesetzt ----------
def g_zus(st):
    if st == 1:
        n = R.randint(2, 8)
        return {'y': 'zahl', 'f': {'text': f'{n} Würfel mit 1 cm Kantenlänge werden in einer Reihe zusammengeklebt. Wie groß ist die Oberfläche des Körpers in cm²?'}, 'o': {'wert': 4 * n + 2, 'einheit': 'cm²'},
                'c': f'{n} * 6 - 2 * ({n} - 1)', 'w': f'Einzeln {6 * n} Quadrate. {n - 1} Klebestellen verdecken je 2: {6 * n} − {2 * (n - 1)} = {4 * n + 2} cm².', 'h': 'Jede Klebestelle verdeckt zwei Quadrate.'}
    if st == 2:
        n, a = R.randint(2, 6), R.randint(2, 5)
        o = (4 * n + 2) * a * a
        return {'y': 'zahl', 'f': {'text': f'{n} Würfel mit {a} cm Kantenlänge werden zu einem Turm aufeinandergestapelt. Wie groß ist die Oberfläche des Turms?'}, 'o': {'wert': o, 'einheit': 'cm²'},
                'c': f'({n} * 6 - 2 * ({n} - 1)) * {a} * {a}', 'w': f'{4 * n + 2} sichtbare Quadrate zu je {a * a} cm²: {zt(o)} cm².', 'h': 'Zähle die sichtbaren Quadrate und nimm mal die Fläche eines Quadrats.'}
    art = R.randrange(2)
    if art == 0:
        a, b, c = R.randint(4, 10), R.randint(3, 8), R.randint(2, 6)
        s = R.randint(2, min(a, b) - 1)
        o = O(a, b, c) + O(s, s, s) - 2 * s * s
        return {'y': 'zahl', 'f': {'text': f'Auf einen Quader ({qtxt(a, b, c)}) wird mittig ein Würfel mit {s} cm Kantenlänge geklebt. Wie groß ist die Oberfläche des neuen Körpers?'},
                'o': {'wert': o, 'einheit': 'cm²'}, 'c': f'2 * ({a} * {b} + {a} * {c} + {b} * {c}) + 6 * {s} * {s} - 2 * {s} * {s}',
                'w': f'Quader {O(a, b, c)} cm², Würfel {6 * s * s} cm². Berührfläche {s * s} cm² fällt zweimal weg: {O(a, b, c)} + {6 * s * s} − {2 * s * s} = {o} cm².',
                'h': 'Addiere beide Oberflächen und ziehe die Berührfläche zweimal ab.'}
    a, b, c = R.randint(3, 8), R.randint(3, 8), R.randint(2, 6)
    o = O(2 * a, b, c)
    return {'y': 'zahl', 'f': {'text': f'Zwei gleiche Quader ({qtxt(a, b, c)}) werden mit den {b} cm × {c} cm großen Flächen aneinandergeklebt. Wie groß ist die Oberfläche des neuen Quaders?'},
            'o': {'wert': o, 'einheit': 'cm²'}, 'c': f'2 * (2 * ({a} * {b} + {a} * {c} + {b} * {c})) - 2 * {b} * {c}',
            'w': f'Einzeln je {O(a, b, c)} cm², zusammen {2 * O(a, b, c)} cm². Minus 2 · {b * c}: {o} cm². (Probe: neuer Quader {2 * a} × {b} × {c}.)', 'h': 'Die Klebefläche verschwindet auf beiden Quadern.'}


# ---------- 5 Volumen ----------
def g_vol(st):
    if st == 1:
        a, b, c = R.randint(2, 6), R.randint(2, 5), R.randint(1, 4)
        a, b = sort2(a, b)
        return {'y': 'zahl', 'f': {'text': f'Ein Quader wird aus Einheitswürfeln (1 cm³) gebaut: {a} Würfel lang, {b} Würfel breit, {c} {"Schicht" if c == 1 else "Schichten"} hoch. Wie viele Würfel sind es?'},
                'o': {'wert': a * b * c}, 'c': f'{a} * {b} * {c}', 'w': f'Eine Schicht: {a} · {b} = {a * b}. {c} {"Schicht" if c == 1 else "Schichten"}: {a * b * c} Würfel. Das Volumen ist also {a * b * c} cm³.', 'h': 'Zähle zuerst die Würfel einer Schicht.'}
    if st == 2:
        if R.random() < .5:
            a, b, c = R.randint(3, 15), R.randint(2, 10), R.randint(2, 10)
            return {'y': 'zahl', 'f': {'text': f'Berechne das Volumen eines Quaders, der {qtxt(a, b, c)} ist.'}, 'o': {'wert': a * b * c, 'einheit': 'cm³'}, 'c': f'{a} * {b} * {c}',
                    'w': f'V = {a} · {b} · {c} = {a * b * c} cm³.', 'h': 'V = Länge · Breite · Höhe.'}
        a = R.randint(2, 10)
        return {'y': 'zahl', 'f': {'text': f'Berechne das Volumen eines Würfels mit der Kantenlänge {a} cm.'}, 'o': {'wert': a ** 3, 'einheit': 'cm³'}, 'c': f'{a} ** 3',
                'w': f'V = {a} · {a} · {a} = {a ** 3} cm³.', 'h': 'Dreimal die Kantenlänge malnehmen.'}
    art = R.randrange(2)
    if art == 0:
        a, b, c = R.randint(3, 12), R.randint(2, 10), R.randint(2, 9)
        return {'y': 'zahl', 'f': {'text': f'Ein Quader hat das Volumen {a * b * c} cm³. Er ist {a} cm lang und {b} cm breit. Wie hoch ist er?'}, 'o': {'wert': c, 'einheit': 'cm'}, 'c': f'{a * b * c} / ({a} * {b})',
                'w': f'Grundfläche {a} · {b} = {a * b} cm². Höhe: {a * b * c} : {a * b} = {c} cm.', 'h': 'Teile das Volumen durch die Grundfläche.'}
    k = R.randint(2, 5)
    s = R.choice([2, 3, 4, 5])
    return {'y': 'zahl', 'f': {'text': f'Ein Würfel mit {k * s} cm Kantenlänge wird in kleine Würfel mit {s} cm Kantenlänge zerlegt. Wie viele kleine Würfel entstehen?'}, 'o': {'wert': k ** 3},
            'c': f'({k * s} / {s}) ** 3', 'w': f'In jeder Richtung {k * s} : {s} = {k} Würfel: {k} · {k} · {k} = {k ** 3}.', 'h': 'Wie viele kleine Würfel passen in jede Richtung?'}


# ---------- 6 Verstehen ----------
# Prüfung: alle Antworten mit Begründung; höchstens 6 Oberflächen-Behauptungen
VERS = {'ober': 0}


def g_vers(st):
    a, b, c = R.randint(2, 6), R.randint(2, 6), R.randint(2, 6)
    if a == 6: a = 5
    if st == 1:
        aussagen = [('', 'Ein Quader hat 12 Kanten.', 'Ja, je 4 in Länge, Breite und Höhe.', ['Nein, er hat 8 Kanten, eine an jeder Ecke.', 'Nein, er hat 6 Kanten, eine je Fläche.']),
                    ('', 'Ein Würfel hat 8 Flächen.', 'Nein, 6 Flächen – aber 8 Ecken.', ['Ja, 4 Seitenflächen und je 2 oben und unten.', 'Nein, er hat 12 Flächen.']),
                    ('ober', f'Ein Würfel mit {a} cm Kantenlänge hat die Oberfläche {6 * a * a} cm².', f'Ja, 6 · {a} · {a} = {6 * a * a} cm².', [f'Nein, {a} · {a} · {a} = {a ** 3} cm².', f'Nein, {a} · {a} = {a * a} cm².']),
                    ('ober', f'Ein Würfel mit {a} cm Kantenlänge hat die Oberfläche {4 * a * a} cm².', f'Nein, er hat 6 Flächen: 6 · {a * a} = {6 * a * a} cm².', [f'Ja, 4 Seitenflächen zu je {a * a} cm².', f'Nein, {a} · {a} · {a} = {a ** 3} cm².'])]
    elif st == 2:
        su = a * b + a * c + b * c
        aussagen = [('ober', f'Ein Quader {a} cm × {b} cm × {c} cm hat die Oberfläche {su} cm².', f'Nein, jede Fläche gibt es zweimal: {O(a, b, c)} cm².', ['Ja, man addiert die drei verschiedenen Flächen.', f'Nein, {a} · {b} · {c} = {a * b * c} cm².']),
                    ('ober', f'Ein Quader {a} cm × {b} cm × {c} cm hat die Oberfläche {O(a, b, c)} cm².', f'Ja, 2 · ({a * b} + {a * c} + {b * c}) = {O(a, b, c)} cm².', [f'Nein, {a * b} + {a * c} + {b * c} = {su} cm², jede Fläche einmal.', f'Nein, {a} · {b} · {c} = {a * b * c} cm².']),
                    ('', 'Klebt man zwei Würfel zusammen, ist die Oberfläche kleiner als bei beiden einzeln.', 'Ja, die Klebeflächen liegen innen und fallen weg.', ['Nein, die Oberfläche bleibt gleich.', 'Nein, sie wird größer, weil der Körper größer ist.']),
                    ('', 'Oberfläche misst man in cm³.', 'Nein, Flächen in cm², Volumen in cm³.', ['Ja, weil ein Körper drei Kantenlängen hat.', 'Nein, Oberfläche misst man in cm.']),
                    ('', f'Bei einem Würfel mit {a} cm Kantenlänge sind alle Kanten zusammen {12 * a} cm lang.', f'Ja, 12 · {a} cm = {12 * a} cm.', [f'Nein, 6 · {a} cm = {6 * a} cm.', f'Nein, 8 · {a} cm = {8 * a} cm.']),
                    ('', f'Bei einem Quader {a} cm × {b} cm × {c} cm sind alle Kanten zusammen {a + b + c} cm lang.', f'Nein, jede Länge kommt viermal vor: 4 · {a + b + c} = {4 * (a + b + c)} cm.', ['Ja, man addiert Länge, Breite und Höhe.', f'Nein, 2 · {a + b + c} = {2 * (a + b + c)} cm.'])]
        if a * b * c == O(a, b, c): return g_vers(st)
    else:
        aussagen = [('', 'Verdoppelt man die Kantenlänge eines Würfels, verdoppelt sich die Oberfläche.', 'Nein, sie wird viermal so groß (2 · 2 = 4).', ['Ja, doppelte Kante, doppelte Oberfläche.', 'Nein, sie wird achtmal so groß.']),
                    ('', 'Verdoppelt man die Kantenlänge eines Würfels, wird das Volumen achtmal so groß.', 'Ja, 2 · 2 · 2 = 8.', ['Nein, doppelt so groß.', 'Nein, viermal so groß.']),
                    ('', 'Zwei Quader mit gleichem Volumen haben immer die gleiche Oberfläche.', 'Nein: 1 × 1 × 8 (O = 34) und 2 × 2 × 2 (O = 24) haben beide V = 8.', ['Ja, gleich viel Inhalt heißt gleich viel Fläche.', 'Ja, wenn beide Körper Quader sind.']),
                    ('', f'Ein Quader {a} × {b} × {c} und ein Quader {c} × {a} × {b} haben dieselbe Oberfläche.', 'Ja, es ist derselbe Quader, nur gedreht.', ['Nein, die Höhe ist eine andere, also auch die Oberfläche.', 'Nein, nur das Volumen bleibt gleich.'])]
    frei = [x for x in aussagen if x[0] != 'ober' or VERS['ober'] < 6]
    k, s_, grund, f = R.choice(frei)
    if k == 'ober': VERS['ober'] += 1
    return {**wahl_rund(R, grund, f, 3), 'f': {'text': f'Stimmt die Aussage? „{s_}“'}, 'w': grund, 'h': 'Rechne ein Beispiel oder stell dir eine Schachtel vor.'}


GEN = {'quader': g_quader, 'oberflaeche': g_ober, 'sachaufgaben': g_sach, 'zusammengesetzt': g_zus, 'volumen': g_vol, 'verstehen': g_vers}

DATEI = datei(E, 'Quader und Würfel beschreiben, ihren Oberflächeninhalt berechnen – auch bei zusammengesetzten Körpern und im Alltag – und ihr Volumen bestimmen.', MERKE,
              [('Quader und Würfel', ['quader', 'oberflaeche']),
               ('Anwenden', ['sachaufgaben', 'zusammengesetzt']),
               ('Volumen und Verstehen', ['volumen', 'verstehen'])],
              ETAPPEN, GEN, vertiefung=['volumen'],
              offen=['Prisma, Zylinder, Pyramide, Kegel und Kugel aus „umfang“ weggelassen: Stoff späterer Jahrgangsstufen.',
                     'lehrplan_gym nennt „Volumen“, der LehrplanPLUS Gymnasium Kl. 5 aber nur Oberflächeninhalte von Quadern und zusammengesetzten Körpern (Volumen ab Kl. 6). Deshalb Volumen (nur Quader/Würfel in cm³, ohne Raumeinheiten-Umrechnung) als Vertiefung, nicht Pflicht. Bitte entscheiden.',
                     'Zeichnungen: Schrägbilder von Quadern (verdeckte Kanten gestrichelt) und Würfelnetze werden als Figur aus Linien gezeichnet (Lernkarten quader, zusammengesetzt; Aufgaben „Ist das ein Würfelnetz?“). Netze von Quadern mit Maßen und das Falten durch das Kind gehen nicht.',
                     'Prüfpunkt nicht umgesetzt: Volumeneinheiten (1 dm³ = 1 000 cm³, Liter). Raumeinheiten sind laut LehrplanPLUS Stoff der Jahrgangsstufe 6; die Karte volumen ist hier nur Vertiefung und bleibt bei cm³ ohne Umrechnung.'])

# Verständliche Fassung (Siebte Runde, 15.11.): Alltagssituation zuerst (einstieg), jedes neue Wort erklärt (woerter),
# Beispiel in kleinen Schritten, Merksatz am Ende (regel). Durchgehende Situationen: Schuhkarton, Geschenkpapier, Aquarium, Spielwürfel, Bauklötze.
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _klar_kl5.py) – die Aufgaben bleiben wörtlich gleich.
from _klar_kl5 import klar  # noqa: E402

KLAR = {
 'quader': {
  'einstieg': 'Ein Schuhkarton, ein Ziegelstein, eine Milchpackung – sie alle haben dieselbe Form: sechs rechteckige Seiten, die gerade aneinanderstoßen. Ein Spielwürfel ist ein besonders regelmäßiger Fall davon. Diese Form heißt ⟦Quader⟧.',
  'woerter': [['Körper', 'ein Ding mit Länge, Breite und Höhe, das Platz im Raum einnimmt'], ['Quader', 'ein Körper mit 6 rechteckigen Flächen, zum Beispiel ein Schuhkarton'],
              ['Würfel', 'ein Quader, bei dem alle Kanten gleich lang sind'], ['Fläche', 'eine Seite des Körpers'],
              ['Kante', 'die Linie, an der zwei Flächen zusammenstoßen'], ['Ecke', 'der Punkt, an dem drei Kanten zusammenstoßen'],
              ['a, b, c', 'Länge, Breite und Höhe des Quaders'], ['gestrichelte Linie', 'im Bild eine Kante, die hinten liegt und eigentlich verdeckt ist']],
  'schritte': ['Ein Quader ist 5 cm lang, 3 cm breit und 2 cm hoch. Wie lang sind alle 12 Kanten zusammen?',
               'Je 4 Kanten sind gleich lang: 4 Kanten mit 5 cm, 4 mit 3 cm und 4 mit 2 cm.',
               'Rechne: 4 · 5 cm + 4 · 3 cm + 4 · 2 cm = 20 cm + 12 cm + 8 cm.',
               'Alle Kanten zusammen sind ⟦40 cm⟧ lang.'],
  'regel': 'So beschreibst du einen ⟦Quader⟧: ⟦6 rechteckige Flächen⟧, ⟦12 Kanten⟧, ⟦8 Ecken⟧. Gegenüberliegende Flächen sind gleich groß, je 4 Kanten gleich lang. Beim ⟦Würfel⟧ sind alle 12 Kanten gleich lang und alle 6 Flächen Quadrate.',
  'fehler': '5 + 3 + 2 = 10 cm als Länge aller Kanten ist falsch: Jede Kantenlänge kommt ⟦viermal⟧ vor, also 4 · (5 + 3 + 2) = 40 cm. Für ein Kantenmodell aus Draht wären 10 cm viel zu wenig.'},
 'oberflaeche': {
  'einstieg': 'Du willst einen Schuhkarton ganz mit Geschenkpapier bekleben. Wie viel Papier brauchst du? Du musst alle sechs Seiten bedecken: oben und unten, vorne und hinten, links und rechts. Alle Flächen zusammen ergeben den ⟦Oberflächeninhalt⟧.',
  'woerter': [['Oberflächeninhalt O', 'die Flächeninhalte aller 6 Flächen zusammengezählt'], ['Flächenpaar', 'zwei gegenüberliegende Flächen, die gleich groß sind']],
  'schritte': ['Ein Quader hat a = 5 cm, b = 3 cm, c = 2 cm. Seine 6 Flächen bilden 3 Paare.',
               'Oben und unten: 2 · 5 · 3 = 30 cm². Vorne und hinten: 2 · 5 · 2 = 20 cm².',
               'Links und rechts: 2 · 3 · 2 = 12 cm².',
               'Alles zusammen: O = 30 + 20 + 12 = ⟦62 cm²⟧.'],
  'regel': 'So berechnest du den ⟦Oberflächeninhalt⟧: Die 6 Flächen bilden ⟦3 Paare⟧ gleich großer Rechtecke. ⟦O = 2 · a · b + 2 · a · c + 2 · b · c⟧. Beim Würfel sind alle 6 Flächen gleich: ⟦O = 6 · a · a⟧.',
  'fehler': 'Nur die drei sichtbaren Flächen addieren (15 + 10 + 6 = 31 cm²) ist falsch: Jede Fläche hat ein ⟦Gegenüber⟧ – auch der Boden des Kartons will beklebt werden. Es sind ⟦6⟧ Flächen, also doppelt so viel.'},
 'sachaufgaben': {
  'einstieg': 'Ein Aquarium ist aus Glas, aber oben offen – es hat keinen Deckel. Wer ausrechnet, wie viel Glas man braucht, darf den Deckel nicht mitzählen. Bei Aufgaben aus dem Alltag ist das oft so: Nicht immer werden alle sechs Flächen gebraucht. Du überlegst zuerst, ⟦welche Flächen wirklich da sind⟧.',
  'woerter': [['Aquarium', 'ein Glasbehälter für Fische'], ['ohne Deckel', 'die obere Fläche fehlt'], ['Wände', 'die vier Flächen ringsherum, ohne Boden und Deckel'],
              ['mindestens', 'so viel oder mehr; hier: nicht weniger, als nötig ist']],
  'schritte': ['Ein Aquarium ohne Deckel ist 60 cm lang, 30 cm breit und 40 cm hoch. Gebraucht werden der Boden und vier Wände.',
               'Boden: 60 · 30 = 1 800 cm².',
               'Vorne und hinten: 2 · 60 · 40 = 4 800 cm². Links und rechts: 2 · 30 · 40 = 2 400 cm².',
               'Glas zusammen: 1 800 + 4 800 + 2 400 = ⟦9 000 cm²⟧.'],
  'regel': 'So löst du Oberflächen-Sachaufgaben: Überlege zuerst, ⟦welche Flächen gebraucht werden⟧. Ein Aquarium hat ⟦keinen Deckel⟧, ein Zimmer wird ⟦ohne Boden⟧ gestrichen, Fenster und Türen ziehst du ab. Dann addierst du nur diese Flächen.'},
 'zusammengesetzt': {
  'einstieg': 'Du klebst drei Spielwürfel zu einer Reihe zusammen und willst die Reihe danach anmalen. Die Seiten, an denen die Würfel aneinanderkleben, kannst du nicht mehr anmalen – sie liegen innen. Bei ⟦zusammengesetzten Körpern⟧ gehören diese Klebeflächen nicht mehr zur Oberfläche.',
  'woerter': [['zusammengesetzter Körper', 'ein Körper aus mehreren Würfeln oder Quadern'], ['Berührfläche', 'die Fläche, an der zwei Körper aneinanderstoßen; sie liegt innen'],
              ['Einzeloberfläche', 'die Oberfläche eines einzelnen Würfels oder Quaders, bevor er angeklebt wird']],
  'schritte': ['3 Würfel mit 1 cm Kantenlänge liegen in einer Reihe. Jeder einzelne hat 6 Quadrate zu 1 cm², zusammen sind das 3 · 6 = 18 Quadrate.',
               'Zwischen den Würfeln gibt es 2 Klebestellen. An jeder liegen 2 Quadrate aufeinander: eins vom linken und eins vom rechten Würfel.',
               'Diese 2 · 2 = 4 Quadrate liegen innen und fallen weg: 18 − 4 = 14.',
               'Die Oberfläche der Reihe ist ⟦14 cm²⟧.'],
  'regel': 'So berechnest du die Oberfläche eines ⟦zusammengesetzten Körpers⟧: Einzeloberflächen addieren, dann ⟦jede Berührfläche zweimal abziehen⟧ – sie fehlt bei beiden Körpern. Bei Würfelreihen kannst du auch die ⟦sichtbaren Quadrate zählen⟧.',
  'fehler': '3 · 6 cm² = 18 cm² ist falsch: Die Flächen, an denen die Würfel ⟦aneinanderkleben⟧, kannst du nicht anmalen. Sie gehören nicht mehr zur Oberfläche.'},
 'volumen': {
  'einstieg': 'In einen Karton sollen Bauklötze mit 1 cm Kantenlänge. Wie viele passen hinein? Du legst eine Schicht auf den Boden und stapelst dann Schicht auf Schicht. Wie viele solcher kleinen Würfel in einen Körper passen, heißt ⟦Volumen⟧.',
  'woerter': [['Volumen V', 'wie viele Einheitswürfel in einen Körper passen (auch: Rauminhalt)'], ['Einheitswürfel', 'ein Würfel mit der Kantenlänge 1, zum Beispiel 1 cm'],
              ['cm³', 'Kubikzentimeter: das Volumen eines Würfels mit 1 cm Kantenlänge'], ['Schicht', 'eine Lage Würfel auf gleicher Höhe']],
  'schritte': ['Ein Quader ist 5 cm lang, 3 cm breit und 2 cm hoch. Fülle ihn in Gedanken mit Würfeln von 1 cm Kantenlänge.',
               'Auf den Boden passt eine Schicht von 5 · 3 = 15 Würfeln.',
               'Der Quader ist 2 cm hoch, also passen 2 Schichten übereinander: 15 · 2 = 30 Würfel.',
               'Das Volumen ist ⟦V = 30 cm³⟧.'],
  'regel': 'So berechnest du das ⟦Volumen⟧: Zähle die ⟦Einheitswürfel⟧ – Würfel pro Schicht mal Zahl der Schichten. Als Formel: Quader ⟦V = a · b · c⟧, Würfel ⟦V = a · a · a⟧.'},
 'verstehen': {
  'einstieg': 'Zwei Geschenkkartons sind Würfel; der große hat doppelt so lange Kanten wie der kleine. Braucht er dann doppelt so viel Geschenkpapier? Das Gefühl sagt ja – Nachrechnen sagt etwas anderes. Behauptungen über Körper prüfst du mit einem ⟦Zahlenbeispiel⟧.',
  'woerter': [['Behauptung', 'eine Aussage, die richtig oder falsch sein kann'], ['Zahlenbeispiel', 'eine Rechnung mit ausgedachten, bequemen Zahlen'],
              ['vierfach, achtfach', '4-mal so viel, 8-mal so viel']],
  'schritte': ['Die Aussage: „Ein Würfel mit doppelter Kantenlänge hat die doppelte Oberfläche.“ Nimm ein Zahlenbeispiel.',
               'Kleiner Würfel: a = 1 cm, also O = 6 · 1 · 1 = 6 cm².',
               'Großer Würfel: a = 2 cm, also O = 6 · 2 · 2 = 24 cm². Das ist ⟦viermal⟧ so viel, nicht doppelt so viel.',
               'Die Aussage ist ⟦falsch⟧.'],
  'regel': 'So prüfst du Aussagen über Körper: mit einem ⟦Zahlenbeispiel⟧ nachrechnen oder an einem Würfel ⟦abzählen⟧. Achte darauf, ob nach ⟦Kanten (cm)⟧, ⟦Flächen (cm²)⟧ oder ⟦Volumen (cm³)⟧ gefragt ist.'},
}
klar(DATEI, KLAR)


if __name__ == '__main__':
    schreibe(DATEI)
