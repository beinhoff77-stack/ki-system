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

MERKE = ['Quader: 6 Flächen, 12 Kanten, 8 Ecken. Kantenlänge gesamt: 4 · (a + b + c).', 'Oberfläche Quader: O = 2ab + 2ac + 2bc. Würfel: O = 6a².',
         'Zusammengesetzt: Berührflächen fallen weg (je zweimal).', 'Volumen Quader: V = a · b · c (cm³). Würfel: V = a³.']


def qtxt(a, b, c, e='cm'): return f'{a} {e} lang, {b} {e} breit und {c} {e} hoch'


def O(a, b, c): return 2 * (a * b + a * c + b * c)


# ---------- 1 Quader ----------
def g_quader(st):
    if st == 1:
        fr = [('Wie viele Ecken hat ein Quader?', 8, 'Ein Quader hat 8 Ecken: 4 unten und 4 oben.'), ('Wie viele Kanten hat ein Quader?', 12, 'Ein Quader hat 12 Kanten: 4 unten, 4 oben, 4 senkrecht.'),
              ('Wie viele Flächen hat ein Quader?', 6, 'Ein Quader hat 6 Flächen: vorne, hinten, oben, unten, links, rechts.'),
              ('Wie viele Kanten treffen sich an einer Ecke eines Würfels?', 3, 'An jeder Ecke treffen sich 3 Kanten (Länge, Breite, Höhe).'),
              ('Wie viele Flächen eines Würfels sind Quadrate?', 6, 'Beim Würfel sind alle 6 Flächen Quadrate.')]
        if R.random() < .5:
            t, r, w = R.choice(fr)
            return {'y': 'zahl', 'f': {'text': t}, 'o': {'wert': r}, 'c': f'{r}', 'w': w, 'h': 'Stell dir eine Schachtel vor und zähle.'}
        a = R.randint(2, 15)
        return {'y': 'zahl', 'f': {'text': f'Ein Würfel hat die Kantenlänge {a} cm. Wie lang sind alle Kanten zusammen?'}, 'o': {'wert': 12 * a, 'einheit': 'cm'}, 'c': f'12 * {a}',
                'w': f'12 gleich lange Kanten: 12 · {a} = {12 * a} cm.', 'h': 'Ein Würfel hat 12 gleich lange Kanten.'}
    a, b, c = R.randint(2, 15), R.randint(2, 12), R.randint(2, 10)
    if st == 2:
        return {'y': 'zahl', 'f': {'text': f'Ein Quader ist {qtxt(a, b, c)}. Wie lang sind alle Kanten zusammen?'}, 'o': {'wert': 4 * (a + b + c), 'einheit': 'cm'}, 'c': f'4 * ({a} + {b} + {c})',
                'w': f'Je 4 Kanten gleich: 4 · ({a} + {b} + {c}) = 4 · {a + b + c} = {4 * (a + b + c)} cm.', 'h': 'Jede der drei Kantenlängen kommt viermal vor.'}
    art = R.randrange(3)
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
def g_sach(st):
    if st == 1:
        a, b, c = R.randint(20, 60), R.randint(15, 40), R.randint(10, 30)
        return {'y': 'zahl', 'f': {'text': f'Ein Geschenkkarton ist {qtxt(a, b, c)}. Wie viel cm² Papier braucht man mindestens, um ihn ganz zu bekleben?'}, 'o': {'wert': O(a, b, c), 'einheit': 'cm²'},
                'c': f'2 * {a} * {b} + 2 * {a} * {c} + 2 * {b} * {c}', 'w': f'Oberfläche: {2 * a * b} + {2 * a * c} + {2 * b * c} = {zt(O(a, b, c))} cm².', 'h': 'Ganz bekleben heißt: alle 6 Flächen.'}
    if st == 2:
        a, b, c = R.choice([40, 50, 60, 80, 100]), R.choice([25, 30, 40, 50]), R.choice([30, 40, 50])
        ob = a * b + 2 * a * c + 2 * b * c
        return {'y': 'zahl', 'f': {'text': f'Ein Aquarium ohne Deckel ist {qtxt(a, b, c)}. Wie viel cm² Glas braucht man?'}, 'o': {'wert': ob, 'einheit': 'cm²'},
                'c': f'{a} * {b} + 2 * {a} * {c} + 2 * {b} * {c}', 'w': f'Boden {a * b}, vorne/hinten 2 · {a * c} = {2 * a * c}, Seiten 2 · {b * c} = {2 * b * c}. Zusammen {zt(ob)} cm².',
                'h': 'Alle Flächen außer dem Deckel.'}
    art = R.randrange(2)
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
        return {'y': 'zahl', 'f': {'text': f'Ein Quader wird aus Einheitswürfeln (1 cm³) gebaut: {a} Würfel lang, {b} Würfel breit, {c} Schichten hoch. Wie viele Würfel sind es?'},
                'o': {'wert': a * b * c, 'einheit': 'cm³'}, 'c': f'{a} * {b} * {c}', 'w': f'Eine Schicht: {a} · {b} = {a * b}. {c} Schichten: {a * b * c} Würfel, also {a * b * c} cm³.', 'h': 'Zähle zuerst die Würfel einer Schicht.'}
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
def g_vers(st):
    a, b, c = R.randint(2, 6), R.randint(2, 6), R.randint(2, 6)
    if st == 1:
        aussagen = [('Ein Quader hat 12 Kanten.', True, 'Ja, je 4 in Länge, Breite und Höhe.'), ('Ein Würfel hat 8 Flächen.', False, 'Nein, 6 Flächen – aber 8 Ecken.'),
                    (f'Ein Würfel mit {a} cm Kantenlänge hat die Oberfläche {6 * a * a} cm².', True, f'Ja, 6 · {a} · {a} = {6 * a * a} cm².'),
                    (f'Ein Würfel mit {a} cm Kantenlänge hat die Oberfläche {4 * a * a} cm².', False, f'Nein, er hat 6 Flächen: 6 · {a * a} = {6 * a * a} cm².')]
    elif st == 2:
        aussagen = [(f'Ein Quader {a} cm × {b} cm × {c} cm hat die Oberfläche {a * b + a * c + b * c} cm².', False, f'Nein, jede Fläche gibt es zweimal: {O(a, b, c)} cm².'),
                    (f'Ein Quader {a} cm × {b} cm × {c} cm hat die Oberfläche {O(a, b, c)} cm².', True, f'Ja, 2 · ({a * b} + {a * c} + {b * c}) = {O(a, b, c)} cm².'),
                    ('Klebt man zwei Würfel zusammen, ist die Oberfläche kleiner als bei beiden einzeln.', True, 'Ja, die Klebeflächen liegen innen und fallen weg.'),
                    ('Oberfläche misst man in cm³.', False, 'Nein, Flächen in cm², Volumen in cm³.')]
    else:
        aussagen = [('Verdoppelt man die Kantenlänge eines Würfels, verdoppelt sich die Oberfläche.', False, 'Nein, sie wird viermal so groß.'),
                    ('Verdoppelt man die Kantenlänge eines Würfels, wird das Volumen achtmal so groß.', True, 'Ja, 2 · 2 · 2 = 8.'),
                    ('Zwei Quader mit gleichem Volumen haben immer die gleiche Oberfläche.', False, 'Nein: 1 × 1 × 8 (O = 34) und 2 × 2 × 2 (O = 24) haben beide V = 8.'),
                    (f'Ein Quader {a} × {b} × {c} und ein Quader {c} × {a} × {b} haben dieselbe Oberfläche.', True, 'Ja, es ist derselbe Quader, nur gedreht.')]
    s, stimmt, grund = R.choice(aussagen)
    gegen = 'Ja, das stimmt.' if not stimmt else 'Nein, das ist falsch.'
    return {**wahl(R, grund, [gegen, 'Das kann man nicht entscheiden.'], 3), 'f': {'text': f'Stimmt die Aussage? „{s}“'}, 'w': grund, 'h': 'Rechne ein Beispiel oder stell dir eine Schachtel vor.'}


GEN = {'quader': g_quader, 'oberflaeche': g_ober, 'sachaufgaben': g_sach, 'zusammengesetzt': g_zus, 'volumen': g_vol, 'verstehen': g_vers}

DATEI = datei(E, 'Quader und Würfel beschreiben, ihren Oberflächeninhalt berechnen – auch bei zusammengesetzten Körpern und im Alltag – und ihr Volumen bestimmen.', MERKE,
              [('Quader und Würfel', ['quader', 'oberflaeche']),
               ('Anwenden', ['sachaufgaben', 'zusammengesetzt']),
               ('Volumen und Verstehen', ['volumen', 'verstehen'])],
              ETAPPEN, GEN, vertiefung=['volumen'],
              offen=['Prisma, Zylinder, Pyramide, Kegel und Kugel aus „umfang“ weggelassen: Stoff späterer Jahrgangsstufen.',
                     'lehrplan_gym nennt „Volumen“, der LehrplanPLUS Gymnasium Kl. 5 aber nur Oberflächeninhalte von Quadern und zusammengesetzten Körpern (Volumen ab Kl. 6). Deshalb Volumen (nur Quader/Würfel in cm³, ohne Raumeinheiten-Umrechnung) als Vertiefung, nicht Pflicht. Bitte entscheiden.',
                     'Braucht Zeichnung: Schrägbilder und Netze von Quader und Würfel (Lehrplan „auch mit Netzen und Schrägbildern“) kann die App noch nicht zeichnen. Bisher nur Tabelle der Flächenpaare.'])

if __name__ == '__main__':
    schreibe(DATEI)
