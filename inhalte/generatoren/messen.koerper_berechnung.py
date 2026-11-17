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

# Umbau U5 (Achte Runde, Vorgabe 16.11.): Lernkarten nach dem neuen Muster – einstieg, woerter (≤ 3), Kartenbild,
# Bildergeschichte (schritte mit bild), „Pass auf!“ (fehler + fehler_bild), MERKE (regel).
# Situationen: Schuhkarton, Geschenkpapier, Aquarium, Spielwürfel, Bauklötze. Rechentabellen füllen sich Schritt für Schritt.
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl5.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl5 import umbau  # noqa: E402

OBER = lambda a, b, c, s=None: {'zeilen': [['oben und unten', '2', '5 cm · 3 cm', a], ['vorne und hinten', '2', '5 cm · 2 cm', b], ['links und rechts', '2', '3 cm · 2 cm', c]]
                                + ([['alle 6', '', '', s]] if s else [])}
GLAS = lambda a, b, c, s: {'zeilen': [['Boden', '60 · 30', a], ['vorne, hinten', '2 · 60 · 40', b], ['links, rechts', '2 · 30 · 40', c], ['Deckel', 'fehlt', '0'], ['Glas', 'zusammen', s]]}
SCHICHT = lambda a, b, s: {'zeilen': [['1. Schicht', a], ['2. Schicht', b], ['zusammen', s]]}

KARTEN = {
 'quader': {
  'einstieg': 'Ein Schuhkarton, ein Ziegelstein, eine Milchpackung: Sie haben sechs rechteckige Seiten. Ein Spielwürfel ist ein besonders regelmäßiger Fall. Diese Form heißt ⟦Quader⟧.',
  'woerter': [['Kante', 'die Linie, an der zwei Flächen zusammenstoßen'], ['Ecke', 'der Punkt, an dem drei Kanten zusammenstoßen'],
              ['Würfel', 'ein Quader mit lauter gleich langen Kanten']],
  'bild': 'BEHALTEN',
  'schritte': [{'text': 'Ein Quader hat 12 Kanten, 8 Ecken und 6 Flächen.'},
               {'text': 'Je 4 Kanten sind gleich lang: hier 5 cm, 3 cm und 2 cm.'},
               {'text': 'Jede Länge viermal: 20 cm, 12 cm und 8 cm.'},
               {'text': 'Zusammen sind alle Kanten ⟦40 cm⟧ lang.'}],
  'fehler': '5 + 3 + 2 = 10 cm ist falsch. Jede Kantenlänge kommt viermal vor: 4 · 10 cm = 40 cm.',
  'regel': 'Ein ⟦Quader⟧ hat 6 Flächen, 12 Kanten und 8 Ecken. Je 4 Kanten sind gleich lang.'},
 'oberflaeche': {
  'einstieg': 'Du willst einen Schuhkarton ganz mit Geschenkpapier bekleben. Oben, unten, vorne, hinten, links und rechts: Alle sechs Flächen zusammen ergeben den ⟦Oberflächeninhalt⟧.',
  'woerter': [['Oberflächeninhalt', 'alle 6 Flächen zusammengezählt; abgekürzt O'], ['Flächenpaar', 'zwei gegenüberliegende, gleich große Flächen']],
  'bild': {'typ': 'tabelle', 'kopf': ['Flächenpaar', 'Anzahl', 'eine Fläche', 'zusammen'],
           'zeilen': [['oben und unten', '2', '5 cm · 3 cm', '?'], ['vorne und hinten', '2', '5 cm · 2 cm', '?'], ['links und rechts', '2', '3 cm · 2 cm', '?']]},
  'schritte': [{'text': 'Oben und unten: 2 · 5 cm · 3 cm = 30 cm².', 'bild': OBER('30 cm²', '?', '?')},
               {'text': 'Vorne und hinten: 2 · 5 cm · 2 cm = 20 cm².', 'bild': OBER('30 cm²', '20 cm²', '?')},
               {'text': 'Links und rechts: 2 · 3 cm · 2 cm = 12 cm².', 'bild': OBER('30 cm²', '20 cm²', '12 cm²')},
               {'text': 'Jedes Flächenpaar addiert: 30 + 20 + 12 = ⟦62 cm²⟧.', 'bild': OBER('30 cm²', '20 cm²', '12 cm²', '62 cm²')}],
  'fehler': 'Nur die drei sichtbaren Flächen addieren ergibt 31 cm². Auch der Boden will beklebt werden: Es ist doppelt so viel.',
  'regel': 'Addiere ⟦alle 6 Flächen⟧, je zwei sind gleich groß. Beim Würfel: O = 6 · a · a.'},
 'sachaufgaben': {
  'einstieg': 'Ein Aquarium ist oben offen, es hat keinen Deckel. Wer das Glas ausrechnet, darf den Deckel nicht mitzählen. Überlege zuerst, ⟦welche Flächen wirklich da sind⟧.',
  'woerter': [['Aquarium', 'ein Glasbehälter für Fische'], ['keinen Deckel', 'die obere Fläche fehlt']],
  'bild': {'typ': 'tabelle', 'kopf': ['Fläche', 'Rechnung', 'cm²'], **GLAS('?', '?', '?', '?')},
  'schritte': [{'text': 'Das Aquarium ist 60 cm lang, 30 cm breit und 40 cm hoch.'},
               {'text': 'Boden: 60 · 30 = 1 800 cm².', 'bild': GLAS('1 800', '?', '?', '?')},
               {'text': 'Wände: 4 800 cm² vorne und hinten, 2 400 cm² links und rechts.', 'bild': GLAS('1 800', '4 800', '2 400', '?')},
               {'text': 'Glas zusammen: 1 800 + 4 800 + 2 400 = ⟦9 000 cm²⟧.', 'bild': GLAS('1 800', '4 800', '2 400', '9 000')}],
  'fehler': 'Die volle Oberfläche nehmen, obwohl der Deckel fehlt, ist falsch. Zähle nur das Glas, das es wirklich gibt.',
  'regel': 'Zähle nur die Flächen, ⟦die wirklich da sind⟧. Aquarium ohne Deckel, Zimmer ohne Boden, Fenster abziehen.'},
 'zusammengesetzt': {
  'einstieg': 'Du klebst drei Spielwürfel zu einer Reihe zusammen und malst sie an. Die Klebeflächen kannst du nicht anmalen, sie liegen innen. Sie heißen ⟦Berührflächen⟧.',
  'woerter': [['Berührfläche', 'eine Fläche, an der zwei Körper aneinanderstoßen; sie liegt innen']],
  'bild': 'BEHALTEN',
  'schritte': [{'text': 'Jeder Würfel hat 6 Quadrate zu 1 cm²: zusammen 18.'},
               {'text': 'An 2 Klebestellen liegen je 2 Quadrate aufeinander: 4 fallen weg.'},
               {'text': '18 − 4 = 14. Die Oberfläche ist ⟦14 cm²⟧.'}],
  'fehler': '3 · 6 cm² = 18 cm² ist falsch. Die Berührflächen liegen innen und gehören nicht zur Oberfläche.',
  'regel': 'Einzeloberflächen addieren, dann ⟦jede Berührfläche zweimal⟧ abziehen.'},
 'volumen': {
  'einstieg': 'In einen Karton sollen Bauklötze mit 1 cm Kantenlänge. Du legst eine Schicht auf den Boden und stapelst Schicht auf Schicht. Wie viele hineinpassen, heißt ⟦Volumen⟧.',
  'woerter': [['Volumen', 'wie viele Einheitswürfel in einen Körper passen; abgekürzt V'], ['cm³', 'Kubikzentimeter: ein Würfel mit 1 cm Kante'],
              ['Schicht', 'eine Lage Würfel auf gleicher Höhe']],
  'bild': {'typ': 'tabelle', 'kopf': ['Schicht', 'Würfel'], **SCHICHT('?', '?', '?')},
  'schritte': [{'text': 'Der Quader ist 5 cm lang, 3 cm breit und 2 cm hoch.'},
               {'text': 'Eine Schicht auf dem Boden: 5 · 3 = 15 Würfel.', 'bild': SCHICHT('15', '?', '?')},
               {'text': 'Er ist 2 cm hoch: 2 Schichten, also 15 · 2 = 30.', 'bild': SCHICHT('15', '15', '30')},
               {'text': 'Das Volumen ist ⟦30 cm³⟧.'}],
  'fehler': 'Volumen und Oberfläche verwechseln. Das Volumen zählt Würfel (cm³), die Oberfläche zählt Quadrate (cm²).',
  'regel': 'Volumen = ⟦a · b · c⟧. Beim Würfel: a · a · a.'},
 'verstehen': {
  'einstieg': 'Zwei Geschenkkartons sind Würfel, der große hat doppelt so lange Kanten. Braucht er doppelt so viel Papier? Das prüfst du mit einem ⟦Zahlenbeispiel⟧.',
  'woerter': [['Zahlenbeispiel', 'eine Rechnung mit ausgedachten, bequemen Zahlen']],
  'bild': {'typ': 'saeulen', 'einheit': 'cm²', 'werte': [{'name': 'a = 1 cm', 'wert': 6}], 'y_max': 24},
  'schritte': [{'text': 'Kante 1 cm: O = 6 · 1 · 1 = 6 cm².'},
               {'text': 'Kante 2 cm: O = 6 · 2 · 2 = 24 cm².',
                'bild': {'werte': [{'name': 'a = 1 cm', 'wert': 6}, {'name': 'a = 2 cm', 'wert': 24}]}},
               {'text': '24 ist viermal 6. Doppelt so viel Papier stimmt also ⟦nicht⟧.'}],
  'fehler': 'Kanten, Oberfläche und Volumen wachsen verschieden. Bei doppelter Kante: Oberfläche vierfach, Volumen achtfach.',
  'regel': 'Prüfe Aussagen mit einem ⟦Zahlenbeispiel⟧. Achte darauf, ob cm, cm² oder cm³ gefragt ist.'},
}
umbau(DATEI, KARTEN)


# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl5) ----------
# Neue Übungen nach Prüfungsvorbild (Jahrgangsstufentest 6 Bayern: Körper mit 8 Ecken/12 Kanten, angemalter Würfel aus kleinen Würfeln,
# Netz und Höhe, Eigenschaften ankreuzen; Bayerischer Mathematik-Test 2000: Quaderoberfläche mit gemischten Einheiten; Känguru: Würfelbauten).
# Netze und Schrägbilder kann die App nicht zeichnen – solche Aufgaben sind in Worten gestellt.
from itertools import product  # noqa: E402
from _schwer_kl5 import A, L, Z, de, einzig, ergaenze, wahl  # noqa: E402


def _oberflaeche(wuerfel):
    """Oberfläche (in Einheitsquadraten) eines Baus aus Einheitswürfeln: 6 je Würfel minus 2 je Klebestelle."""
    s = set(wuerfel)
    kleben = sum(1 for (x, y, z) in s for d in ((1, 0, 0), (0, 1, 0), (0, 0, 1)) if (x + d[0], y + d[1], z + d[2]) in s)
    return 6 * len(s) - 2 * kleben


def _schwer():
    N = {}
    rote = {}
    for x, y, z in product(range(3), repeat=3):
        k = sum(1 for v in (x, y, z) if v in (0, 2))
        rote[k] = rote.get(k, 0) + 1
    N['quader'] = [
        Z(2, 'Alle Kanten eines Würfels sind zusammen 60 cm lang. Wie lang ist eine Kante?', '60 / 12', 'Ein Würfel hat 12 gleich lange Kanten: 60 cm : 12 = 5 cm.', 'Wie viele Kanten hat ein Würfel?', einheit='cm'),
        Z(2, 'Wie viele Flächen, Kanten und Ecken hat ein Quader zusammen?', '6 + 12 + 8', '6 Flächen + 12 Kanten + 8 Ecken = 26.', 'Zähle Flächen, Kanten und Ecken einzeln.'),
        wahl(3, 'Welcher Körper hat 8 Ecken, 12 Kanten und nur quadratische Flächen?', ['Würfel', 'Quader mit 5 cm, 3 cm, 2 cm', 'Pyramide', 'Zylinder'], lambda o: o == 'Würfel',
             'Ecken und Kanten passen zu Quader und Würfel. Nur beim Würfel sind alle 6 Flächen Quadrate.', 'Prüfe alle drei Bedingungen.'),
        Z(3, 'Ein Würfelnetz besteht aus 6 gleich großen Quadraten. Das ganze Netz hat den Flächeninhalt 150 cm². Wie lang ist eine Würfelkante?', str(einzig([a for a in range(1, 30) if 6 * a * a == 150])),
          'Ein Quadrat: 150 cm² : 6 = 25 cm². 5 cm · 5 cm = 25 cm², also ist die Kante 5 cm lang.', 'Wie groß ist ein Quadrat des Netzes?', einheit='cm'),
        Z(3, 'Ein großer Würfel ist aus 3 · 3 · 3 kleinen Würfeln gebaut und wird außen rot angemalt. Wie viele kleine Würfel haben genau zwei rote Flächen?', str(rote[2]),
          'Zwei rote Flächen haben die mittleren Würfel jeder Kante: 12 Kanten mit je 1 Würfel = 12.', 'Ecken-Würfel haben 3 rote Flächen. Wo liegen die Würfel mit genau 2?'),
        Z(3, 'Ein großer Würfel aus 3 · 3 · 3 kleinen Würfeln wird außen rot angemalt. Wie viele kleine Würfel haben genau eine rote Fläche?', str(rote[1]),
          'Genau eine rote Fläche hat der mittlere Würfel jeder Seitenfläche: 6 Flächen, also 6 Würfel.', 'Schau dir eine Seitenfläche mit 3 · 3 Würfeln an. Welcher hat nur diese eine rote Fläche?'),
    ]
    hoehe = einzig([h for h in range(1, 30) if 2 * (5 * 4 + 5 * h + 4 * h) == 94])
    N['oberflaeche'] = [
        Z(2, 'Berechne die Oberfläche eines Quaders, der 6 cm lang, 5 cm breit und 2 cm hoch ist.', '2 * (6 * 5 + 6 * 2 + 5 * 2)', '2 · 30 + 2 · 12 + 2 · 10 = 60 + 24 + 20 = 104 cm².',
          'Je zwei Flächen sind gleich groß.', einheit='cm²'),
        Z(2, 'Eine Seitenfläche eines Würfels hat 49 cm². Wie groß ist seine Oberfläche?', '6 * 49', 'Ein Würfel hat 6 gleiche Flächen: 6 · 49 cm² = 294 cm².', 'Wie viele gleiche Flächen hat ein Würfel?', einheit='cm²'),
        Z(3, 'Ein Quader ist 4 cm lang, 25 mm breit und 3 cm hoch. Berechne die Oberfläche in cm².', '2 * (4 * 2.5 + 4 * 3 + 2.5 * 3)',
          '25 mm = 2,5 cm. 2 · (4 · 2,5 + 4 · 3 + 2,5 · 3) = 2 · (10 + 12 + 7,5) = 59 cm².', 'Rechne zuerst alle Kanten in cm um.', einheit='cm²'),
        Z(3, 'Ein Würfel mit 4 cm Kantenlänge wird in der Mitte durchgeschnitten. Um wie viele cm² ist die Oberfläche der beiden Teile zusammen größer als die des Würfels?', '2 * 4 * 4',
          'Beim Schnitt entstehen zwei neue Schnittflächen mit je 4 cm · 4 cm = 16 cm². Zusammen 32 cm² mehr.', 'Welche Flächen kommen durch den Schnitt neu dazu?', einheit='cm²'),
        Z(3, 'Ein Quader hat die Oberfläche 94 cm². Er ist 5 cm lang und 4 cm breit. Wie hoch ist er?', str(hoehe),
          'Boden und Deckel: 2 · 20 = 40 cm². Für die vier Seiten bleiben 54 cm². Sie sind zusammen 2 · (5 + 4) = 18 cm breit: Höhe 54 : 18 = 3 cm.',
          'Ziehe zuerst Boden und Deckel ab.', einheit='cm'),
        A(3, 'Jemand berechnet die Oberfläche eines Quaders (6 cm × 4 cm × 2 cm) so: 6 · 4 · 2 = 48 cm². Was ist falsch?', 'Das ist das Volumen (48 cm³). Die Oberfläche ist 2 · (24 + 12 + 8) = 88 cm².',
          ['Nichts, 48 cm² stimmt.', 'Man muss 6 + 4 + 2 = 12 cm² rechnen.', 'Richtig ist 6 · 48 = 288 cm².'],
          'Für die Oberfläche addiert man die 6 Flächen: 2 · 6 · 4 + 2 · 6 · 2 + 2 · 4 · 2 = 88 cm².', 'Malnehmen aller drei Kanten ergibt das Volumen, nicht die Oberfläche.'),
    ]
    N['sachaufgaben'] = [
        Z(2, 'Ein Karton ohne Deckel ist 20 cm lang, 10 cm breit und 10 cm hoch. Wie viel cm² Pappe braucht man?', '20 * 10 + 2 * 20 * 10 + 2 * 10 * 10',
          'Boden 200 cm², vorne/hinten 2 · 200 cm², links/rechts 2 · 100 cm². Zusammen 800 cm².', 'Ohne Deckel: Es fehlt eine Fläche.', einheit='cm²'),
        Z(2, 'Eine würfelförmige Kiste mit 30 cm Kantenlänge wird nur an den vier Seiten bemalt, nicht oben und nicht unten. Wie viele cm² werden bemalt?', '4 * 30 * 30',
          'Vier Quadrate mit je 30 cm · 30 cm = 900 cm²: 4 · 900 = 3 600 cm².', 'Wie viele Flächen werden bemalt?', einheit='cm²'),
        Z(3, 'Ein Schwimmbecken ist 10 m lang, 5 m breit und 2 m tief. Boden und Wände werden gefliest. Wie viele m² sind das?', '10 * 5 + 2 * 10 * 2 + 2 * 5 * 2',
          'Boden: 50 m². Lange Wände: 2 · 20 m². Kurze Wände: 2 · 10 m². Zusammen 110 m².', 'Die Oberseite (Wasser) wird nicht gefliest.', einheit='m²'),
        Z(3, 'Ein Becken ist 4 m lang, 3 m breit und 1 m tief. Boden und Wände werden mit quadratischen Fliesen (50 cm Seitenlänge) belegt. Wie viele Fliesen braucht man?',
          '(4 * 3 + 2 * 4 * 1 + 2 * 3 * 1) / (0.5 * 0.5)', 'Fläche: 12 + 8 + 6 = 26 m². Eine Fliese: 0,5 m · 0,5 m = 0,25 m². 26 : 0,25 = 104 Fliesen.',
          'Auf 1 m² passen 4 solche Fliesen.'),
        Z(3, 'Ein Würfel mit 2 cm Kantenlänge steht mittig auf einem Würfel mit 4 cm Kantenlänge. Wie groß ist die Oberfläche des ganzen Körpers (Boden zählt mit)?', '6 * 4 * 4 + 6 * 2 * 2 - 2 * 2 * 2',
          'Großer Würfel 96 cm², kleiner 24 cm². Die Auflagefläche (4 cm²) ist doppelt verdeckt: 96 + 24 − 8 = 112 cm².', 'Welche Flächen verschwinden beim Aufeinanderstellen?', einheit='cm²'),
        Z(3, 'Für ein Aquarium ohne Deckel (60 cm × 30 cm × 40 cm) rechnet jemand die ganze Oberfläche aus. Um wie viele cm² zu viel ist das?', '60 * 30',
          'Der fehlende Deckel ist 60 cm · 30 cm = 1 800 cm² groß – genau so viel wurde zu viel gerechnet.', 'Welche Fläche gibt es gar nicht?', einheit='cm²'),
    ]
    L4 = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 0, 1)]
    reihe6 = [(i, 0, 0) for i in range(6)]
    block = [(x, y, 0) for x in range(3) for y in range(2)]
    N['zusammengesetzt'] = [
        Z(2, '3 Würfel mit 2 cm Kantenlänge werden in einer Reihe zusammengeklebt. Wie groß ist die Oberfläche des Körpers?', '3 * 6 * 4 - 2 * 2 * 4',
          '3 · 24 cm² = 72 cm². 2 Klebestellen verdecken je 2 Quadrate zu 4 cm²: 72 − 16 = 56 cm².', 'Wie viele Klebestellen gibt es?', einheit='cm²'),
        Z(2, '4 Würfel mit 1 cm Kantenlänge werden als 2 · 2-Quadrat auf den Tisch gelegt und verklebt. Wie groß ist die Oberfläche des Körpers?', str(_oberflaeche([(x, y, 0) for x in range(2) for y in range(2)])),
          'Es entsteht ein Quader 2 cm × 2 cm × 1 cm: 2 · (4 + 2 + 2) = 16 cm².', 'Welcher Quader entsteht?', einheit='cm²'),
        Z(3, '8 Würfel mit 1 cm Kantenlänge werden zu einem großen Würfel (2 · 2 · 2) zusammengesetzt. Wie groß ist seine Oberfläche?', str(_oberflaeche([(x, y, z) for x in range(2) for y in range(2) for z in range(2)])),
          'Der große Würfel hat 2 cm Kantenlänge: 6 · 2 · 2 = 24 cm². Die 8 einzelnen Würfel hatten zusammen 48 cm².', 'Rechne mit dem großen Würfel.', einheit='cm²'),
        Z(3, '4 Würfel mit 1 cm Kantenlänge: 3 liegen in einer Reihe, der vierte sitzt oben auf dem ersten. Wie groß ist die Oberfläche?', str(_oberflaeche(L4)),
          '4 · 6 = 24 Quadrate. Es gibt 3 Klebestellen mit je 2 verdeckten Quadraten: 24 − 6 = 18 cm².', 'Zähle die Klebestellen.', einheit='cm²'),
        Z(3, 'Aus 6 Würfeln mit 1 cm Kantenlänge baut man einmal eine Reihe und einmal einen Quader 3 · 2 · 1. Um wie viele cm² ist die Oberfläche der Reihe größer?',
          f'{_oberflaeche(reihe6)} - {_oberflaeche(block)}', f'Reihe: 6 · 6 − 2 · 5 = 26 cm². Quader 3 × 2 × 1: 2 · (6 + 3 + 2) = 22 cm². Unterschied 4 cm².',
          'Rechne beide Oberflächen aus. Je mehr Klebestellen, desto kleiner die Oberfläche.', einheit='cm²'),
        A(3, 'Jemand rechnet für zwei aneinandergeklebte Würfel (Kante 3 cm): 2 · 54 cm² = 108 cm². Was ist falsch?', 'Die beiden Klebeflächen (je 9 cm²) sind verdeckt: richtig ist 90 cm².',
          ['Nichts, 108 cm² stimmt.', 'Nur eine Klebefläche fällt weg: 99 cm².', 'Richtig ist 54 cm², weil es ein Körper ist.'],
          'Jeder Würfel hat 54 cm². Beim Kleben verschwinden zwei Quadrate zu je 9 cm²: 108 − 18 = 90 cm².', 'Wie viele Quadrate sind nach dem Kleben nicht mehr sichtbar?'),
    ]
    N['volumen'] = [
        Z(2, 'Berechne das Volumen eines Quaders, der 8 cm lang, 5 cm breit und 3 cm hoch ist.', '8 * 5 * 3', 'V = 8 cm · 5 cm · 3 cm = 120 cm³.', 'Volumen = Länge · Breite · Höhe.', einheit='cm³'),
        Z(2, 'Ein Würfel hat das Volumen 125 cm³. Wie lang ist eine Kante?', str(einzig([a for a in range(1, 20) if a ** 3 == 125])), '5 · 5 · 5 = 125. Die Kante ist 5 cm lang.',
          'Welche Zahl dreimal mit sich selbst malgenommen ergibt 125?', einheit='cm'),
        Z(3, 'Ein Aquarium ist 50 cm lang, 30 cm breit und 40 cm hoch. Es wird bis 5 cm unter den Rand gefüllt. Wie viele Liter Wasser sind darin? (1 Liter = 1 000 cm³)',
          '50 * 30 * (40 - 5) / 1000', 'Wasserhöhe: 35 cm. V = 50 · 30 · 35 = 52 500 cm³ = 52,5 Liter.', 'Wie hoch steht das Wasser?', einheit='l'),
        Z(3, 'Eine Schachtel ist innen 6 cm lang, 4 cm breit und 3 cm hoch. Wie viele Würfel mit 2 cm Kantenlänge passen höchstens hinein?', '(6 // 2) * (4 // 2) * (3 // 2)',
          'Längs passen 3, quer 2, in der Höhe nur 1 (3 cm reichen nicht für 2 Würfel). 3 · 2 · 1 = 6. Volumen geteilt (72 : 8 = 9) wäre falsch.',
          'Zähle in jeder Richtung, wie viele ganze Würfel passen.'),
        Z(3, 'Die Kantenlänge eines Würfels wird verdreifacht. Wie oft so groß wird sein Volumen?', '3 * 3 * 3', 'Länge, Breite und Höhe werden je verdreifacht: 3 · 3 · 3 = 27-mal.',
          'Probiere es aus: Kante 1 cm und Kante 3 cm.'),
        Z(3, 'Ein Quader hat das Volumen 360 cm³. Seine Grundfläche ist ein Quadrat mit 6 cm Seitenlänge. Wie hoch ist er?', '360 / (6 * 6)',
          'Grundfläche: 6 cm · 6 cm = 36 cm². Höhe: 360 : 36 = 10 cm.', 'Volumen = Grundfläche · Höhe.', einheit='cm'),
    ]
    N['verstehen'] = [
        wahl(2, 'Stimmt die Aussage? „Ein Würfel ist ein besonderer Quader.“', ['Ja: ein Quader, bei dem alle Kanten gleich lang sind.', 'Nein: Ein Würfel hat mehr Ecken.', 'Nein: Quader haben keine Quadrate.'],
             lambda o: o.startswith('Ja'), 'Ein Würfel hat alle Eigenschaften eines Quaders (6 Rechtecksflächen, 12 Kanten, 8 Ecken) – dazu gleich lange Kanten.', 'Vergleiche die Eigenschaften.'),
        wahl(2, 'Stimmt die Aussage? „Ein Quader mit 2 cm, 3 cm und 4 cm hat das Volumen 24 cm³.“', ['Ja: 2 · 3 · 4 = 24.', 'Nein: 2 + 3 + 4 = 9 cm³.', 'Nein: Das sind 52 cm³.'],
             lambda o: o.startswith('Ja'), 'V = 2 cm · 3 cm · 4 cm = 24 cm³.', 'Volumen = Länge · Breite · Höhe.'),
        wahl(3, 'Welche Aussage über jeden Quader ist falsch?', ['Gegenüberliegende Flächen sind gleich groß.', 'Alle Flächen sind Rechtecke.', 'Alle Kanten sind gleich lang.', 'Er hat 8 Ecken.'],
             lambda o: o == 'Alle Kanten sind gleich lang.', 'Gleich lange Kanten hat nur der Würfel. Ein Quader kann z. B. 5 cm, 3 cm und 2 cm haben.', 'Denk an einen Schuhkarton.'),
        Z(3, 'Bei welchem Würfel haben Oberfläche (in cm²) und Volumen (in cm³) dieselbe Maßzahl? Gib die Kantenlänge an.', str(einzig([a for a in range(1, 30) if 6 * a * a == a ** 3])),
          'Oberfläche 6 · a · a, Volumen a · a · a. Gleich, wenn a = 6: 6 · 36 = 216 und 6 · 6 · 6 = 216.', 'Probiere Kantenlängen aus und vergleiche.', einheit='cm'),
        wahl(3, 'Stimmt die Aussage? „Ein Quader mit größerem Volumen hat immer auch die größere Oberfläche.“',
             ['Nein: 3 × 3 × 3 hat V = 27 cm³ und O = 54 cm², 1 × 1 × 20 hat V = 20 cm³, aber O = 82 cm².', 'Ja, immer.', 'Ja, mehr Inhalt braucht mehr Hülle.', 'Nein, Volumen und Oberfläche sind immer gleich.'],
             lambda o: o.startswith('Nein: 3'), 'Ein Gegenbeispiel genügt: Der lange, dünne Quader hat weniger Volumen, aber mehr Oberfläche.', 'Vergleiche einen Würfel mit einer langen Stange.'),
        A(3, 'Jemand gibt das Volumen eines Würfels mit 3 cm Kantenlänge mit 9 cm³ an. Was ist falsch?', 'Es wurde nur a · a gerechnet. Richtig: 3 · 3 · 3 = 27 cm³.',
          ['Nichts, das stimmt.', 'Richtig ist 3 · 3 · 6 = 54 cm³.', 'Richtig ist 3 + 3 + 3 = 9 cm³.'], 'Beim Volumen braucht man alle drei Kanten: 3 · 3 · 3 = 27 cm³. 9 cm² ist eine Seitenfläche.',
          'Wie viele Faktoren braucht man beim Volumen?'),
    ]
    return N


ergaenze(DATEI, _schwer(), 1053)

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('messen.koerper_berechnung', 13_5_10)
# a) vollständige Oberfläche mit großen Zahlen ist zu schwer für Stufe 1 → Stufe 2; dafür drei leichte Stufe-1-Aufgaben neu
for _m in ['45 cm lang, 33 cm breit und 14 cm hoch', '36 cm lang, 32 cm breit und 13 cm hoch', '36 cm lang, 24 cm breit und 24 cm hoch',
           '44 cm lang, 34 cm breit und 18 cm hoch', '31 cm lang, 26 cm breit und 29 cm hoch', '40 cm lang, 39 cm breit und 15 cm hoch']:
    BF.stufe('sachaufgaben', f'Ein Geschenkkarton ist {_m}. Wie viel cm² Papier braucht man mindestens, um ihn ganz zu bekleben?', 2)
_h1 = 'Ganz bekleben heißt: alle 6 Flächen.'
BF.neu('sachaufgaben', 1, BF.Z('Eine Schachtel ist 5 cm lang, 4 cm breit und 2 cm hoch. Wie viel cm² Papier braucht man, um sie ganz zu bekleben?', 76,
                               '2 * 5 * 4 + 2 * 5 * 2 + 2 * 4 * 2', 'Oberfläche: 2 · 20 + 2 · 10 + 2 · 8 = 40 + 20 + 16 = 76 cm².', _h1, einheit='cm²'))
BF.neu('sachaufgaben', 1, BF.Z('Ein würfelförmiges Geschenk hat 3 cm Kantenlänge. Wie viel cm² Papier braucht man, um es ganz zu bekleben?', 54,
                               '6 * 3 * 3', 'Ein Würfel hat 6 gleiche Quadrate: 6 · 3 · 3 = 6 · 9 = 54 cm².', _h1, einheit='cm²'))
BF.neu('sachaufgaben', 1, BF.Z('Ein Karton mit Deckel ist 10 cm lang, 10 cm breit und 5 cm hoch. Wie viel cm² Pappe braucht man für ihn?', 400,
                               '2 * 10 * 10 + 2 * 10 * 5 + 2 * 10 * 5', 'Oberfläche: 2 · 100 + 2 · 50 + 2 · 50 = 200 + 100 + 100 = 400 cm².', 'Mit Deckel heißt: alle 6 Flächen.', einheit='cm²'))
# c) viermal „Oberfläche → Kante“ → zwei davon mit anderem Gedanken
BF.ersetze('oberflaeche', 'Ein Würfel hat die Oberfläche 486 cm². Wie lang ist eine Kante?', BF.Z(
    'Ein Würfel hat die Oberfläche 216 cm². Wie groß ist sein Volumen?', 216, '6 * 6 * 6',
    'Eine Fläche: 216 : 6 = 36 cm². 6 · 6 = 36, also a = 6 cm. Volumen: 6 · 6 · 6 = 216 cm³.', 'Bestimme zuerst die Kantenlänge, dann das Volumen.', einheit='cm³'))
BF.ersetze('oberflaeche', 'Ein Würfel hat die Oberfläche 1014 cm². Wie lang ist eine Kante?', BF.Z(
    'Jede Kante eines Würfels wird doppelt so lang. Wie viel mal so groß wird seine Oberfläche?', 4, '2 * 2',
    'Jede Seitenfläche ist doppelt so lang und doppelt so breit, also 2 · 2 = 4-mal so groß. Damit ist auch die ganze Oberfläche 4-mal so groß (z. B. a = 1 cm: 6 cm², a = 2 cm: 24 cm²).',
    'Probiere es mit a = 1 cm und a = 2 cm aus.'))
# c) viermal „zwei Quader aneinandergeklebt“ → zwei davon mit anderem Gedanken
BF.ersetze('zusammengesetzt', 'Zwei gleiche Quader (7 cm lang, 3 cm breit und 5 cm hoch) werden mit den 3 cm × 5 cm großen Flächen aneinandergeklebt. Wie groß ist die Oberfläche des neuen Quaders?', BF.Z(
    'Drei gleiche Würfel mit 2 cm Kantenlänge werden in einer Reihe aneinandergeklebt. Wie groß ist die Oberfläche des neuen Körpers?', 56, '3 * 6 * 2 * 2 - 4 * 2 * 2',
    'Einzeln: 3 · 24 = 72 cm². Es gibt 2 Klebestellen, an jeder verschwinden 2 Flächen zu 4 cm²: 72 − 4 · 4 = 56 cm². (Probe: Quader 6 × 2 × 2.)',
    'Wie viele Flächen werden beim Kleben verdeckt?', einheit='cm²'))
BF.ersetze('zusammengesetzt', 'Zwei gleiche Quader (4 cm lang, 7 cm breit und 4 cm hoch) werden mit den 7 cm × 4 cm großen Flächen aneinandergeklebt. Wie groß ist die Oberfläche des neuen Quaders?', BF.Z(
    'Zwei gleiche Quader (6 cm × 4 cm × 2 cm) werden einmal mit den 6 cm × 4 cm großen Flächen und einmal mit den 4 cm × 2 cm großen Flächen aneinandergeklebt. Um wie viele cm² ist die Oberfläche im zweiten Fall größer?',
    32, '(2 * 2 * (6 * 4 + 6 * 2 + 4 * 2) - 2 * 4 * 2) - (2 * 2 * (6 * 4 + 6 * 2 + 4 * 2) - 2 * 6 * 4)',
    'Zusammen 2 · 88 = 176 cm². Fall 1: 176 − 2 · 24 = 128 cm². Fall 2: 176 − 2 · 8 = 160 cm². Unterschied: 32 cm².',
    'Je kleiner die Klebefläche, desto weniger Oberfläche verschwindet.', einheit='cm²'))
BF.nicht_umgesetzt('sachaufgaben S2 Aquarium ohne Deckel „anspruchsvoller als manche Stufe-3-Aufgabe“', 'Passt auf Stufe 2 (fünf Flächen, ein Gedanke); Stufe 3 enthält Zusatzschritte (Abzüge, Fliesen, Umrechnung).')

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl5, siehe _durchsicht_kl5.py) ----
from _durchsicht_kl5 import Durchsicht, durchsicht_anwenden  # noqa: E402

DS = Durchsicht('messen.koerper_berechnung', 19_5_14)
# a) Stufe 3 wiederholt eine Stufe-2-Aufgabe wörtlich (3 Würfel, 2 cm, Reihe) → Stufe 2
DS.stufe('zusammengesetzt', 'Drei gleiche Würfel mit 2 cm Kantenlänge werden in einer Reihe aneinandergeklebt. Wie groß ist die Oberfläche des neuen Körpers?', 2,
         enthaelt=lambda x: x['s'] == 3)
# c) Pflichtkarte Oberfläche fragt nach dem Volumen (Volumen ist nicht Stoff von M5, nur Vertiefung) – gleicher Rückwärts-Gedanke ohne Volumen:
DS.ersetze('oberflaeche', 'Ein Würfel hat die Oberfläche 216 cm². Wie groß ist sein Volumen?',
           DS.Z('Ein Würfel hat die Oberfläche 216 cm². Wie lang sind alle seine Kanten zusammen?',
                72, '216 / 6 / 6 * 12',
                'Eine Fläche: 216 cm² : 6 = 36 cm² = 6 cm · 6 cm. Kante 6 cm. Alle 12 Kanten: 12 · 6 cm = 72 cm.',
                'Teile die Oberfläche auf 6 gleiche Quadrate auf. Welche Seitenlänge hat ein Quadrat?', einheit='cm'))
# d) sachaufgaben hatte nur 3 Übungen auf Stufe 1
DS.neu('sachaufgaben', 1, DS.Z('Eine Kiste ist 6 cm lang, 5 cm breit und 4 cm hoch. Wie viel cm² Papier braucht man, um sie ganz zu bekleben?',
                               148, '2 * 6 * 5 + 2 * 6 * 4 + 2 * 5 * 4',
                               'Oberfläche: 2 · 30 + 2 · 24 + 2 · 20 = 60 + 48 + 40 = 148 cm².',
                               'Ganz bekleben heißt: alle 6 Flächen.', einheit='cm²'))
durchsicht_anwenden(DATEI, DS)
# ---- DURCHSICHT ENDE ----
# ---- STUFEN (Zwanzigste Runde, Zweig stufen-kl5, siehe _stufen_kl5.py und _st5_messen_koerper_berechnung.py) ----
from _stufen_kl5 import stufen_anwenden  # noqa: E402
stufen_anwenden(DATEI, 'messen.koerper_berechnung')
# ---- STUFEN ENDE ----

if __name__ == '__main__':
    schreibe(DATEI)
