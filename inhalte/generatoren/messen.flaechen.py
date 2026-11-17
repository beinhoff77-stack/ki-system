#!/usr/bin/env python3
"""Thema messen.flaechen – Umfang und Flächeninhalt (Klasse 5): Einheitsquadrate, Rechteck und Quadrat, Flächeneinheiten,
Kommaschreibweise, Zerlegen und Ergänzen. Dreieck, Parallelogramm und Trapez sind Stoff späterer Jahrgangsstufen."""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl5_rest import *  # noqa: E402,F403

R = random.Random(50)
E = eintrag_laden('messen.flaechen')


def rechteck(a, b, ta=None, tb=None, name=True):
    pk = {'A': [0, 0], 'B': [a, 0], 'C': [a, b], 'D': [0, b]} if name else {'_A': [0, 0], '_B': [a, 0], '_C': [a, b], '_D': [0, b]}
    k = list(pk)
    return {'typ': 'figur', 'punkte': pk, 'flaeche': k, 'linien': [[k[0], k[1], ta or ''], [k[1], k[2], tb or ''], [k[2], k[3]], [k[3], k[0]]]}


def gitter(a, b):
    """Rechteck a × b mit Einheitsquadraten (Hilfslinien)."""
    pk = {'_A': [0, 0], '_B': [a, 0], '_C': [a, b], '_D': [0, b]}
    lin = [['_A', '_B', f'{a} cm'], ['_B', '_C', f'{b} cm'], ['_C', '_D'], ['_D', '_A']]
    for i in range(1, a):
        pk[f'_x{i}u'], pk[f'_x{i}o'] = [i, 0], [i, b]
        lin.append([f'_x{i}u', f'_x{i}o', '', 'gestrichelt'])
    for j in range(1, b):
        pk[f'_y{j}l'], pk[f'_y{j}r'] = [0, j], [a, j]
        lin.append([f'_y{j}l', f'_y{j}r', '', 'gestrichelt'])
    return {'typ': 'figur', 'punkte': pk, 'flaeche': ['_A', '_B', '_C', '_D'], 'linien': lin}


def uform(W, H, w, h):
    """Rechteck W × H, in der Mitte der oberen Seite fehlt ein Rechteck w × h (Prüfung: U-Form)."""
    l, r = (W - w) // 2, (W + w) // 2
    pk = {'_P0': [0, 0], '_P1': [W, 0], '_P2': [W, H], '_P3': [r, H], '_P4': [r, H - h], '_P5': [l, H - h], '_P6': [l, H], '_P7': [0, H]}
    lin = [['_P0', '_P1', f'{W} m'], ['_P1', '_P2', f'{H} m'], ['_P2', '_P3', f'{l} m'], ['_P3', '_P4', f'{h} m'], ['_P4', '_P5', f'{w} m'], ['_P5', '_P6'], ['_P6', '_P7', f'{l} m'], ['_P7', '_P0']]
    return {'typ': 'figur', 'punkte': pk, 'flaeche': list(pk), 'linien': lin}


def lform(W, H, w, h, einheit='m', fragezeichen=False):
    """Rechteck W × H, oben rechts fehlt ein Stück w × h."""
    pk = {'_P0': [0, 0], '_P1': [W, 0], '_P2': [W, H - h], '_P3': [W - w, H - h], '_P4': [W - w, H], '_P5': [0, H]}
    lin = [['_P0', '_P1', f'{W} {einheit}'], ['_P1', '_P2', f'{H - h} {einheit}' if not fragezeichen else '?'], ['_P2', '_P3', f'{w} {einheit}'],
           ['_P3', '_P4', f'{h} {einheit}'], ['_P4', '_P5', f'{W - w} {einheit}' if not fragezeichen else '?'], ['_P5', '_P0', f'{H} {einheit}']]
    return {'typ': 'figur', 'punkte': pk, 'flaeche': list(pk), 'linien': lin}


ETAPPEN = [
    {'lernziel': 'einheitsquadrate', 'titel': 'Fläche mit Einheitsquadraten',
     'regel': 'Der ⟦Flächeninhalt⟧ sagt, wie viele ⟦Einheitsquadrate⟧ in eine Fläche passen. Ein Quadrat mit 1 cm Seitenlänge hat den Flächeninhalt ⟦1 cm²⟧. In ein Rechteck mit 5 cm und 3 cm passen 3 Reihen zu je 5 Quadraten.',
     'schritte': ['Rechteck 5 cm lang, 3 cm breit: eine Reihe hat 5 Einheitsquadrate, es gibt 3 Reihen.', '3 · 5 = 15 Quadrate, also A = ⟦15 cm²⟧.'],
     'bild': gitter(5, 3),
     'fehler': '5 + 3 = 8 cm² ist falsch: Das ist die halbe Länge des Randes. Beim Flächeninhalt zählst du ⟦Quadrate⟧: Reihen ⟦mal⟧ Quadrate pro Reihe.'},
    {'lernziel': 'rechteck', 'titel': 'Rechteck und Quadrat berechnen',
     'regel': 'Rechteck mit Länge a und Breite b: Flächeninhalt ⟦A = a · b⟧, Umfang ⟦u = 2 · a + 2 · b⟧. Quadrat mit Seite a: ⟦A = a · a⟧, ⟦u = 4 · a⟧. Beide Größen brauchen die ⟦gleiche Längeneinheit⟧.',
     'schritte': ['Rechteck: a = 8 m, b = 5 m. A = 8 m · 5 m = 40 m².', 'u = 2 · 8 m + 2 · 5 m = ⟦26 m⟧.'],
     'bild': rechteck(8, 5, 'a = 8 m', 'b = 5 m'),
     'fehler': 'Umfang und Fläche zu verwechseln ist der häufigste Fehler: Der Umfang ist eine ⟦Länge⟧ (m), der Flächeninhalt eine ⟦Fläche⟧ (m²).'},
    {'lernziel': 'einheiten', 'titel': 'Flächeneinheiten umrechnen',
     'regel': 'Flächeneinheiten: km² –100– ha –100– a –100– m² –100– dm² –100– cm² –100– mm². Die ⟦Umrechnungszahl ist 100⟧, weil ein Quadrat mit 10-mal so langer Seite ⟦10 · 10 = 100⟧ kleine Quadrate enthält. ha heißt Hektar, a heißt Ar.',
     'schritte': ['1 m² ist ein Quadrat mit 10 dm Seite: 10 · 10 = 100 Quadrate zu 1 dm².', 'Also 1 m² = 100 dm², und 7 m² = ⟦700 dm²⟧.'],
     'bild': gitter(10, 10),
     'fehler': '1 m² = 10 dm² ist falsch: Die Seite ist 10-mal so lang, die Fläche aber ⟦100-mal⟧ so groß.'},
    {'lernziel': 'kommaschreibweise', 'titel': 'Flächen in Kommaschreibweise',
     'regel': 'Weil die Umrechnungszahl 100 ist, gehören zu jeder kleineren Einheit ⟦zwei Stellen⟧ nach dem Komma: 3,25 m² = 3 m² 25 dm². 4 a 7 m² = ⟦4,07 a⟧.',
     'schritte': ['Schreibe 6 m² 5 dm² in m². Zu dm² gehören zwei Stellen: 05.', '6 m² 5 dm² = ⟦6,05 m²⟧.'],
     'probe': '6,05 m² = 605 dm² = 6 m² 5 dm² ✓',
     'fehler': '6 m² 5 dm² = 6,5 m² ist falsch: 6,5 m² = 6 m² ⟦50⟧ dm². Bei Flächen braucht jede Einheit zwei Stellen: 6,05 m².'},
    {'lernziel': 'zerlegen', 'titel': 'Zerlegen und Ergänzen',
     'regel': 'Zusammengesetzte Flächen ⟦zerlegst⟧ du in Rechtecke und addierst ihre Flächeninhalte. Oder du ⟦ergänzt⟧ die Figur zu einem großen Rechteck und ziehst das fehlende Stück ab. Beide Wege ergeben dasselbe.',
     'schritte': ['L-Form: großes Rechteck 8 m × 6 m, oben rechts fehlt ein Stück 3 m × 2 m.', 'Ergänzen: 8 · 6 − 3 · 2 = 48 − 6 = ⟦42 m²⟧.'],
     'probe': 'Zerlegen: unten 8 · 4 = 32, oben links 5 · 2 = 10, zusammen 42 m² ✓',
     'bild': lform(8, 6, 3, 2),
     'fehler': 'Alle Seiten der L-Form malzunehmen ist falsch. Zerlege zuerst in ⟦Rechtecke⟧ – jedes Rechteck hat nur ⟦eine⟧ Länge und ⟦eine⟧ Breite.'},
    {'lernziel': 'sachaufgaben', 'titel': 'Flächen im Alltag',
     'regel': 'Überlege zuerst: Ist eine ⟦Länge⟧ gesucht (Zaun, Rand, Leiste → Umfang) oder eine ⟦Fläche⟧ (Rasen, Boden, Farbe → Flächeninhalt)? Rechne dann in ⟦einer⟧ Einheit.',
     'schritte': ['Ein Garten ist 12 m lang und 7 m breit. Er bekommt einen Zaun: gesucht ist eine Länge.', 'u = 2 · 12 m + 2 · 7 m = ⟦38 m⟧ Zaun.'],
     'fehler': 'Für einen Zaun den Flächeninhalt 12 · 7 = 84 auszurechnen ist falsch: Ein Zaun läuft am ⟦Rand⟧ entlang, gesucht ist der ⟦Umfang⟧.'},
    {'lernziel': 'verstehen', 'titel': 'Fläche und Umfang verstehen',
     'regel': 'Zwei Figuren mit ⟦gleichem Umfang⟧ können ⟦verschiedene Flächen⟧ haben – und umgekehrt. Verdoppelst du Länge ⟦und⟧ Breite, wird die Fläche ⟦viermal⟧ so groß. Prüfe Aussagen mit Beispielen.',
     'schritte': ['Rechteck 6 m × 2 m: u = 16 m, A = 12 m². Quadrat 4 m × 4 m: u = 16 m, A = 16 m².', 'Gleicher Umfang, aber ⟦verschiedene⟧ Flächen.'],
     'fehler': '„Doppelte Seiten, doppelte Fläche“ ist falsch: 2 m × 3 m = 6 m², aber 4 m × 6 m = 24 m² – das ist ⟦viermal⟧ so viel.'},
]

PRUEFUNG = pruefung_erklaerungen(ETAPPEN, 'messen.flaechen')   # einheiten: Bild passend beschriftet (1 m² = 100 dm²)

MERKE = ['Rechteck: A = a · b, u = 2a + 2b. Quadrat: A = a · a, u = 4a.', 'km² –100– ha –100– a –100– m² –100– dm² –100– cm² –100– mm²',
         'Kommaschreibweise: zwei Stellen je Einheit (3,05 m² = 3 m² 5 dm²).', 'Zusammengesetzte Flächen: zerlegen oder ergänzen.',
         'Umfang ist eine Länge (m), Flächeninhalt eine Fläche (m²).']

FL = ['km²', 'ha', 'a', 'm²', 'dm²', 'cm²', 'mm²']
NAME = {'km²': 'km²', 'ha': 'ha', 'a': 'a', 'm²': 'm²', 'dm²': 'dm²', 'cm²': 'cm²', 'mm²': 'mm²'}


def f100(von, nach):
    return Fr(100) ** (FL.index(nach) - FL.index(von))


# ---------- 1 Einheitsquadrate ----------
def g_eq(st):
    if st == 1:
        a, b = R.randint(2, 9), R.randint(2, 6)
        return {'y': 'zahl', 'f': {'text': f'Wie viele Einheitsquadrate (1 cm²) passen in das Rechteck?', 'grafik': gitter(a, b)}, 'o': {'wert': a * b, 'einheit': 'cm²'}, 'c': f'{a} * {b}',
                'w': f'{b} Reihen zu je {a} Quadraten: {b} · {a} = {a * b} cm².', 'h': 'Zähle die Quadrate in einer Reihe und die Anzahl der Reihen.'}
    if st == 2:
        a, b = R.randint(3, 12), R.randint(2, 9)
        a, b = max(a, b), min(a, b)          # „lang“ ist die längere Seite (Prüfung)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Ein Rechteck ist {a} cm lang und {b} cm breit. Wie viele Quadrate mit 1 cm Seitenlänge passen hinein?'}, 'o': {'wert': a * b}, 'c': f'{a} * {b}',
                    'w': f'Eine Reihe: {a} Quadrate. {b} Reihen: {b} · {a} = {a * b}.', 'h': 'Reihen mal Quadrate pro Reihe.'}
        n = a * b
        return {'y': 'zahl', 'f': {'text': f'Ein Rechteck ist mit {n} Einheitsquadraten (1 cm²) ausgelegt. Eine Reihe hat {a} Quadrate. Wie viele Reihen sind es?'}, 'o': {'wert': b}, 'c': f'{n} / {a}',
                'w': f'{n} : {a} = {b} Reihen. Das Rechteck ist {b} cm breit.', 'h': 'Teile die Anzahl der Quadrate durch die Quadrate pro Reihe.'}
    art = R.randrange(2)
    if art == 0:
        a, b = R.randint(2, 6), R.randint(2, 6)
        return {'y': 'zahl', 'f': {'text': f'Ein Rechteck aus {a} · {b} Einheitsquadraten wird in beiden Richtungen doppelt so lang. Wie viele Einheitsquadrate passen jetzt hinein?'},
                'o': {'wert': 4 * a * b}, 'c': f'(2 * {a}) * (2 * {b})', 'w': f'Neu: {2 * a} · {2 * b} = {4 * a * b} Quadrate – viermal so viele wie {a * b}.', 'h': 'Rechne die neuen Seitenlängen aus.'}
    s = R.choice([2, 3, 4, 5])
    a, b = sorted([s * R.randint(2, 4), s * R.randint(2, 4)], reverse=True)
    return {'y': 'zahl', 'f': {'text': f'Ein Rechteck ist {a} cm lang und {b} cm breit. Wie viele quadratische Fliesen mit {s} cm Seitenlänge passen hinein?'}, 'o': {'wert': (a // s) * (b // s)},
            'c': f'({a} / {s}) * ({b} / {s})', 'w': f'In der Länge {a} : {s} = {a // s}, in der Breite {b} : {s} = {b // s}. {a // s} · {b // s} = {(a // s) * (b // s)} Fliesen.',
            'h': 'Wie viele Fliesen passen nebeneinander, wie viele hintereinander?'}


# ---------- 2 Rechteck ----------
def g_re(st):
    e = R.choice(['cm', 'm', 'dm'])
    if st == 1:
        a, b = R.randint(2, 15), R.randint(2, 12)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Berechne den Flächeninhalt des Rechtecks mit a = {a} {e} und b = {b} {e}.', 'grafik': rechteck(a, b, f'{a} {e}', f'{b} {e}')},
                    'o': {'wert': a * b, 'einheit': e + '²'}, 'c': f'{a} * {b}', 'w': f'A = {a} {e} · {b} {e} = {a * b} {e}².', 'h': 'A = Länge mal Breite.'}
        return {'y': 'zahl', 'f': {'text': f'Berechne den Umfang des Rechtecks mit a = {a} {e} und b = {b} {e}.', 'grafik': rechteck(a, b, f'{a} {e}', f'{b} {e}')},
                'o': {'wert': 2 * a + 2 * b, 'einheit': e}, 'c': f'2 * {a} + 2 * {b}', 'w': f'u = 2 · {a} {e} + 2 · {b} {e} = {2 * a + 2 * b} {e}.', 'h': 'Der Umfang ist der ganze Rand: alle vier Seiten.'}
    if st == 2 and R.random() < .3:          # Fläche und Umfang verwechseln (Prüfung)
        a, b = R.randint(3, 9), R.randint(2, 8)
        if a == b:
            frage, r = f'Ein Quadrat hat die Seitenlänge {a} cm. Welche Angabe ist sein Flächeninhalt?', f'{a * a} cm²'
            f = [f'{4 * a} cm', f'{a * a} cm', f'{4 * a} cm²']
            w = f'A = {a} cm · {a} cm = {a * a} cm². Ein Flächeninhalt hat die Einheit cm². {4 * a} cm wäre der Umfang.'
        else:
            a, b = max(a, b), min(a, b)
            if R.random() < .5:
                frage, r = f'Ein Rechteck ist {a} cm lang und {b} cm breit. Welche Angabe ist der Umfang?', f'{2 * a + 2 * b} cm'
                f = [f'{a * b} cm²', f'{a + b} cm', f'{a * b} cm']
                w = f'u = 2 · {a} cm + 2 · {b} cm = {2 * a + 2 * b} cm. Ein Umfang ist eine Länge (cm). {a * b} cm² wäre der Flächeninhalt.'
            else:
                frage, r = f'Ein Rechteck ist {a} cm lang und {b} cm breit. Welche Angabe ist der Flächeninhalt?', f'{a * b} cm²'
                f = [f'{2 * a + 2 * b} cm', f'{a * b} cm', f'{2 * a + 2 * b} cm²']
                w = f'A = {a} cm · {b} cm = {a * b} cm². Ein Flächeninhalt hat die Einheit cm². {2 * a + 2 * b} cm wäre der Umfang.'
        return {**wahl_rund(R, r, f), 'f': {'text': frage}, 'w': w, 'h': 'Umfang: Länge in cm. Flächeninhalt: in cm².'}
    if st == 2:
        art = R.randrange(3)
        if art == 0:
            s = R.randint(2, 20)
            if R.random() < .5:
                return {'y': 'zahl', 'f': {'text': f'Ein Quadrat hat den Flächeninhalt {s * s} {e}². Wie lang ist eine Seite?'}, 'o': {'wert': s, 'einheit': e}, 'c': f'{s}',
                        'w': f'Welche Zahl mal sich selbst ergibt {s * s}? {s} · {s} = {s * s}. Seite: {s} {e}.', 'h': 'Denke an die Quadratzahlen.'}
            return {'y': 'zahl', 'f': {'text': f'Ein Quadrat hat den Umfang {4 * s} {e}. Wie groß ist sein Flächeninhalt?'}, 'o': {'wert': s * s, 'einheit': e + '²'}, 'c': f'({4 * s} / 4) ** 2',
                    'w': f'Seite: {4 * s} : 4 = {s} {e}. A = {s} · {s} = {s * s} {e}².', 'h': 'Berechne zuerst die Seitenlänge.'}
        a, b = R.randint(3, 20), R.randint(2, 15)
        a, b = max(a, b), min(a, b)
        if a == b: a += 1
        if art == 1:
            return {'y': 'zahl', 'f': {'text': f'Ein Rechteck hat den Flächeninhalt {a * b} {e}² und ist {a} {e} lang. Wie breit ist es?'}, 'o': {'wert': b, 'einheit': e}, 'c': f'{a * b} / {a}',
                    'w': f'b = A : a = {a * b} : {a} = {b} {e}.', 'h': 'Umkehraufgabe: Fläche geteilt durch Länge.'}
        return {'y': 'zahl', 'f': {'text': f'Ein Rechteck hat den Umfang {2 * a + 2 * b} {e} und ist {a} {e} lang. Wie breit ist es?'}, 'o': {'wert': b, 'einheit': e}, 'c': f'({2 * a + 2 * b} - 2 * {a}) / 2',
                'w': f'Zwei Längen: 2 · {a} = {2 * a}. Rest für zwei Breiten: {2 * a + 2 * b} − {2 * a} = {2 * b}. Eine Breite: {b} {e}.', 'h': 'Ziehe zwei Längen vom Umfang ab und halbiere.'}
    art = R.randrange(2)
    if art == 0:
        a = R.randint(2, 9)
        b = R.randint(2, 9) * 10
        return {'y': 'zahl', 'f': {'text': f'Ein Rechteck ist {a} m lang und {b} cm breit. Wie groß ist der Flächeninhalt in dm²?'}, 'o': {'wert': a * 10 * b // 10, 'einheit': 'dm²'}, 'c': f'({a} * 10) * ({b} / 10)',
                'w': f'Gleiche Einheit: {a} m = {a * 10} dm, {b} cm = {b // 10} dm. A = {a * 10} · {b // 10} = {a * b} dm².', 'h': 'Erst beide Seiten in dm umrechnen.'}
    a, b = R.randint(3, 12), R.randint(2, 10)
    a, b = max(a, b), min(a, b)
    ra, rb = 2 * a, b
    return {'y': 'zahl', 'f': {'text': f'Ein Rechteck ist {a} m lang und {b} m breit. Die Länge wird verdoppelt. Um wie viel m² wächst der Flächeninhalt?'}, 'o': {'wert': a * b, 'einheit': 'm²'},
            'c': f'{ra} * {rb} - {a} * {b}', 'w': f'Vorher {a} · {b} = {a * b} m², nachher {ra} · {rb} = {ra * rb} m². Zuwachs: {ra * rb - a * b} m².', 'h': 'Rechne beide Flächen aus und vergleiche.'}


# ---------- 3 Einheiten ----------
def g_ein(st):
    if st == 1:
        i = R.randint(0, 5)
        a, b = FL[i], FL[i + 1]
        x = R.randint(2, 60)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Rechne um: {x} {a} = ? {b}'}, 'o': {'wert': x * 100, 'einheit': b}, 'c': f'{x} * 100', 'w': f'Umrechnungszahl 100: {x} · 100 = {zt(x * 100)} {b}.',
                    'h': 'In die kleinere Einheit: mal 100.'}
        return {'y': 'zahl', 'f': {'text': f'Rechne um: {zt(x * 100)} {b} = ? {a}'}, 'o': {'wert': x, 'einheit': a}, 'c': f'{x * 100} / 100', 'w': f'Umrechnungszahl 100: {zt(x * 100)} : 100 = {x} {a}.',
                'h': 'In die größere Einheit: durch 100.'}
    if st == 2 and R.random() < .3:          # Vorstellung von Flächengrößen (Prüfung)
        satz, z, e, f = R.choice([('Ein Fußballfeld hat ungefähr', 70, 'a', ['m²', 'ha', 'km²']), ('Ein Klassenzimmer hat ungefähr', 60, 'm²', ['dm²', 'a', 'cm²']),
                                  ('Ein Blatt Papier (DIN A4) hat ungefähr', 6, 'dm²', ['cm²', 'm²', 'mm²']), ('Bayern hat ungefähr', 70000, 'km²', ['ha', 'a', 'm²']),
                                  ('Ein Handydisplay hat ungefähr', 1, 'dm²', ['m²', 'mm²', 'a']), ('Eine Briefmarke hat ungefähr', 6, 'cm²', ['mm²', 'dm²', 'm²'])])
        return {**wahl_rund(R, f'{zt(z)} {e}', [f'{zt(z)} {x}' for x in f]), 'f': {'text': f'{satz} welche Fläche?'},
                'w': f'{satz} {zt(z)} {e}. Vergleiche: 1 m² ist ein Quadrat mit 1 m Seite, 1 a ein Quadrat mit 10 m Seite, 1 ha eines mit 100 m Seite.',
                'h': 'Stell dir Quadrate mit 1 cm, 10 cm, 1 m, 10 m und 100 m Seitenlänge vor.'}
    if st == 2:
        i = R.randint(0, 4)
        j = i + 2
        a, b = FL[i], FL[j]
        x = R.randint(2, 30)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Rechne um: {x} {a} = ? {b}'}, 'o': {'wert': x * 10000, 'einheit': b}, 'c': f'{x} * 100 * 100',
                    'w': f'Zwei Schritte, jeweils mal 100: {x} · 10 000 = {zt(x * 10000)} {b}.', 'h': f'Zwischen {a} und {b} liegt noch {FL[i + 1]}.'}
        y = R.randint(1, 99)
        return {'y': 'zahl', 'f': {'text': f'Schreibe in {FL[i + 1]}: {x} {a} {y} {FL[i + 1]}'}, 'o': {'wert': x * 100 + y, 'einheit': FL[i + 1]}, 'c': f'{x} * 100 + {y}',
                'w': f'{x} {a} = {zt(x * 100)} {FL[i + 1]}, dazu {y}: {zt(x * 100 + y)} {FL[i + 1]}.', 'h': 'Größere Einheit umrechnen, dann addieren.'}
    art = R.randrange(3)
    if art == 0:
        i = R.randint(0, 5)
        a, b = FL[i], FL[i + 1]
        x, y = R.randint(1, 40), R.randint(1, 99)
        return luecke([x, y], f'Zerlege: {zt(x * 100 + y)} {b} = □ {a} □ {b}', f'□ {a} □ {b}', f'Erst {a}, dann {b}.', [f'{x * 100 + y} // 100', f'{x * 100 + y} % 100'],
                      f'{zt(x * 100 + y)} : 100 = {x} Rest {y}: {x} {a} {y} {b}.', 'Die letzten beiden Ziffern bleiben in der kleineren Einheit.')
    if art == 1:
        x = R.choice([1, 2, 3, 5, 12, 25])
        return {'y': 'zahl', 'f': {'text': f'Ein Bauernhof hat {x} ha Ackerland. Wie viele m² sind das?'}, 'o': {'wert': x * 10000, 'einheit': 'm²'}, 'c': f'{x} * 100 * 100',
                'w': f'1 ha = 100 a = 10 000 m². {x} ha = {zt(x * 10000)} m².', 'h': 'ha → a → m²: zweimal mal 100.'}
    w = []
    while len(w) < 4:
        e2 = R.choice(['a', 'm²', 'ha'])
        v = R.choice([3, 5, 8, 12, 40, 250, 600, 3000, 70000])
        if all(f100(e2, 'm²') * v != f100(e3, 'm²') * v2 for v2, e3 in w): w.append((v, e2))
    g = max(w, key=lambda t: f100(t[1], 'm²') * t[0])
    return {**wahl(R, f'{zt(g[0])} {g[1]}', [f'{zt(v)} {e2}' for v, e2 in w]), 'f': {'text': 'Welche Fläche ist am größten: ' + ', '.join(f'{zt(v)} {e2}' for v, e2 in w) + '?'},
            'w': 'In m²: ' + ', '.join(f'{zt(v)} {e2} = {zt(f100(e2, "m²") * v)} m²' for v, e2 in w) + '.', 'h': 'Rechne alle in m² um. 1 a = 100 m², 1 ha = 10 000 m².'}


# ---------- 4 Kommaschreibweise ----------
def g_komma(st):
    i = R.randint(1, 5)
    a, b = FL[i], FL[i + 1]
    if st == 1:
        x, y = R.randint(1, 30), R.randint(1, 99)
        v = x + Fr(y, 100)
        return {'y': 'zahl', 'f': {'text': f'Schreibe in {a}: {x} {a} {y} {b}'}, 'o': {'wert': wert(v), 'einheit': a}, 'c': f'{x} + {y} / 100',
                'w': f'{y} {b} sind {str(y).rjust(2, "0")} Hundertstel {a}: {zt(v)} {a}.', 'h': 'Zu jeder kleineren Einheit gehören zwei Stellen nach dem Komma.'}
    if st == 2:
        v = Fr(R.randint(101, 4999), 100)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Rechne um: {zt(v)} {a} = ? {b}'}, 'o': {'wert': int(v * 100), 'einheit': b}, 'c': f'{float(v)} * 100',
                    'w': f'Mal 100: Komma zwei Stellen nach rechts. {zt(v)} {a} = {zt(v * 100)} {b}.', 'h': 'Mal 100 verschiebt das Komma um zwei Stellen.'}
        return {'y': 'zahl', 'f': {'text': f'Rechne um: {zt(v * 100)} {b} = ? {a}'}, 'o': {'wert': wert(v), 'einheit': a}, 'c': f'{int(v * 100)} / 100',
                'w': f'Durch 100: Komma zwei Stellen nach links. {zt(v * 100)} {b} = {zt(v)} {a}.', 'h': 'Durch 100 verschiebt das Komma um zwei Stellen nach links.'}
    art = R.randrange(2)
    if art == 0:
        x, y = R.randint(1, 9), R.randint(1, 9)
        r = zt(x + Fr(y, 100))
        return {**wahl(R, f'{r} {a}', [f'{zt(x + Fr(y, 10))} {a}', f'{zt(x + Fr(y, 1000))} {a}', f'{zt(x * 100 + y)} {a}']), 'f': {'text': f'Welche Schreibweise ist richtig für {x} {a} {y} {b}?'},
                'w': f'{y} {b} = 0,0{y} {a}. Also {r} {a}. {zt(x + Fr(y, 10))} {a} wäre {x} {a} {y * 10} {b}.', 'h': 'Zwei Stellen pro Einheit – fehlende Stelle mit 0 füllen.'}
    v1, v2 = Fr(R.randint(101, 999), 100), R.randint(20, 90)
    s = v1 * 100 + v2
    return {'y': 'zahl', 'f': {'text': f'Berechne {zt(v1)} m² + {v2} dm² und gib das Ergebnis in m² an.'}, 'o': {'wert': wert(s / 100), 'einheit': 'm²'}, 'c': f'{float(v1)} + {v2} / 100',
            'w': f'{v2} dm² = {zt(Fr(v2, 100))} m². {zt(v1)} + {zt(Fr(v2, 100))} = {zt(s / 100)} m².', 'h': 'Erst in dieselbe Einheit umrechnen.'}


# ---------- 5 Zerlegen ----------
def g_zer(st):
    W, H = R.randint(6, 14), R.randint(5, 12)
    w, h = R.randint(2, W - 2), R.randint(2, H - 2)
    A = W * H - w * h
    if st == 1:
        return {'y': 'zahl', 'f': {'text': f'Berechne den Flächeninhalt der Figur. Von einem Rechteck {W} m × {H} m fehlt oben rechts ein Rechteck {w} m × {h} m.', 'grafik': lform(W, H, w, h)},
                'o': {'wert': A, 'einheit': 'm²'}, 'c': f'{W} * {H} - {w} * {h}', 'w': f'Ergänzen: {W} · {H} − {w} · {h} = {W * H} − {w * h} = {A} m².', 'h': 'Großes Rechteck minus das fehlende Stück.'}
    if st == 2 and R.random() < .25: return _wohnung()          # Wohnung aus Räumen ist leichter: Stufe 2 (Prüfung)
    if st == 2:
        if R.random() < .5:
            u = 2 * W + 2 * H
            return {'y': 'zahl', 'f': {'text': 'Wie lang ist der Umfang der L-Form?', 'grafik': lform(W, H, w, h)},
                    'o': {'wert': u, 'einheit': 'm'}, 'c': f'{W} + ({H} - {h}) + {w} + {h} + ({W} - {w}) + {H}',
                    'w': f'Alle sechs Seiten: {W} + {H - h} + {w} + {h} + {W - w} + {H} = {u} m – genauso viel wie beim ganzen Rechteck.', 'h': 'Gehe einmal ganz um die Figur herum und addiere alle Seiten.'}
        return {'y': 'zahl', 'f': {'text': 'Zerlege die L-Form in zwei Rechtecke und berechne den Flächeninhalt.', 'grafik': lform(W, H, w, h)}, 'o': {'wert': A, 'einheit': 'm²'},
                'c': f'{W} * ({H} - {h}) + ({W} - {w}) * {h}', 'w': f'Unten: {W} · {H - h} = {W * (H - h)} m². Oben links: {W - w} · {h} = {(W - w) * h} m². Zusammen {A} m².',
                'h': 'Ziehe eine Linie, sodass zwei Rechtecke entstehen.'}
    art = R.randrange(3)
    if art == 1:          # U-Form (Prüfung)
        W2, H2 = R.randint(8, 14), R.randint(5, 9); w2 = R.randint(2, W2 - 4); h2 = R.randint(2, H2 - 2)
        if (W2 - w2) % 2: return g_zer(3)
        if R.random() < .5:
            A2 = W2 * H2 - w2 * h2
            return {'y': 'zahl', 'f': {'text': 'Berechne den Flächeninhalt der U-Form.', 'grafik': uform(W2, H2, w2, h2)}, 'o': {'wert': A2, 'einheit': 'm²'}, 'c': f'{W2} * {H2} - {w2} * {h2}',
                    'w': f'Ergänzen zum Rechteck: {W2} · {H2} = {W2 * H2} m². Die Lücke: {w2} · {h2} = {w2 * h2} m². {W2 * H2} − {w2 * h2} = {A2} m².', 'h': 'Großes Rechteck minus die Lücke in der Mitte.'}
        u2 = 2 * W2 + 2 * H2 + 2 * h2
        return {'y': 'zahl', 'f': {'text': 'Wie lang ist der Umfang der U-Form?', 'grafik': uform(W2, H2, w2, h2)}, 'o': {'wert': u2, 'einheit': 'm'}, 'c': f'2 * {W2} + 2 * {H2} + 2 * {h2}',
                'w': f'Außen wie beim Rechteck: 2 · {W2} + 2 · {H2} = {2 * W2 + 2 * H2} m. Die Lücke bringt zwei Kanten von je {h2} m dazu: {2 * W2 + 2 * H2} + 2 · {h2} = {u2} m.',
                'h': 'Gehe einmal ganz um die Figur herum. Die Lücke hat zwei zusätzliche Kanten.'}
    if art == 0:
        a, b = R.randint(8, 16), R.randint(6, 12)
        s = R.randint(1, 3)
        inn = (a - 2 * s) * (b - 2 * s)
        return {'y': 'zahl', 'f': {'text': f'Um ein rechteckiges Beet ({a - 2 * s} m × {b - 2 * s} m) führt ein {s} m breiter Weg. Wie groß ist die Fläche des Weges?',
                                   'grafik': {'typ': 'figur', 'punkte': {'_A': [0, 0], '_B': [a, 0], '_C': [a, b], '_D': [0, b], '_a': [s, s], '_b': [a - s, s], '_c': [a - s, b - s], '_d': [s, b - s]},
                                              'flaeche': ['_A', '_B', '_C', '_D'], 'linien': [['_A', '_B', f'{a} m'], ['_B', '_C', f'{b} m'], ['_C', '_D'], ['_D', '_A'], ['_a', '_b', f'{a - 2 * s} m'], ['_b', '_c', f'{b - 2 * s} m'], ['_c', '_d'], ['_d', '_a']]}},
                'o': {'wert': a * b - inn, 'einheit': 'm²'}, 'c': f'{a} * {b} - ({a} - 2 * {s}) * ({b} - 2 * {s})',
                'w': f'Außen: {a} · {b} = {a * b} m². Beet: {a - 2 * s} · {b - 2 * s} = {inn} m². Weg: {a * b - inn} m².', 'h': 'Gesamtfläche minus Beet.'}
    return _wohnung()


def _wohnung():
    k = R.randint(2, 4)
    teile = [(R.randint(3, 8), R.randint(2, 6)) for _ in range(k)]
    s = sum(x * y for x, y in teile)
    return {'y': 'zahl', 'f': {'text': 'Eine Wohnung besteht aus ' + ', '.join(f'einem Raum mit {x} m × {y} m' for x, y in teile[:-1]) + f' und einem Raum mit {teile[-1][0]} m × {teile[-1][1]} m. Wie groß ist die Wohnfläche?'},
            'o': {'wert': s, 'einheit': 'm²'}, 'c': ' + '.join(f'{x} * {y}' for x, y in teile), 'w': ' + '.join(f'{x} · {y}' for x, y in teile) + f' = {s} m².', 'h': 'Berechne jeden Raum einzeln und addiere.'}


# ---------- 6 Sachaufgaben ----------
def g_sach(st):
    a, b = R.randint(6, 25), R.randint(4, 15)
    a, b = max(a, b), min(a, b)
    if a == b: a += 1
    if st == 1:
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Ein Garten ist {a} m lang und {b} m breit. Wie viele Meter Zaun braucht man ringsherum?', 'grafik': rechteck(a, b, f'{a} m', f'{b} m', False)},
                    'o': {'wert': 2 * a + 2 * b, 'einheit': 'm'}, 'c': f'2 * {a} + 2 * {b}', 'w': f'Zaun = Umfang: 2 · {a} + 2 · {b} = {2 * a + 2 * b} m.', 'h': 'Ein Zaun läuft am Rand entlang.'}
        return {'y': 'zahl', 'f': {'text': f'Ein Rasen ist {a} m lang und {b} m breit. Wie viele m² Rasen sind das?', 'grafik': rechteck(a, b, f'{a} m', f'{b} m', False)},
                'o': {'wert': a * b, 'einheit': 'm²'}, 'c': f'{a} * {b}', 'w': f'Fläche: {a} · {b} = {a * b} m².', 'h': 'Rasen bedeckt eine Fläche.'}
    if st == 2:
        art = R.randrange(3)
        if art == 2:
            g = R.choice([20, 25, 30])
            return {'y': 'zahl', 'f': {'text': f'Ein Rasen ist {a} m lang und {b} m breit. Für 1 m² braucht man {g} g Samen. Wie viele g Samen braucht man?'},
                    'o': {'wert': a * b * g, 'einheit': 'g'}, 'c': f'{a} * {b} * {g}', 'w': f'Fläche: {a} · {b} = {a * b} m². Samen: {a * b} · {g} g = {zt(a * b * g)} g.',
                    'h': 'Zuerst die Fläche, dann mal die Menge pro m².'}
        if art == 0:
            l, bb = R.randint(3, 6), R.randint(3, 5)
            p = R.choice([20, 25, 30, 35, 40])
            return {'y': 'zahl', 'f': {'text': f'Ein Zimmer ist {l} m lang und {bb} m breit. Der Boden wird mit Teppich ausgelegt, 1 m² kostet {p} €. Was kostet der Teppich?'},
                    'o': {'wert': l * bb * p, 'einheit': '€'}, 'c': f'{l} * {bb} * {p}', 'w': f'Fläche {l} · {bb} = {l * bb} m². Preis: {l * bb} · {p} € = {l * bb * p} €.', 'h': 'Zuerst die Fläche, dann den Preis.'}
        l, bb = R.randint(3, 6), R.randint(3, 5)
        return {'y': 'zahl', 'f': {'text': f'Ein Zimmer ist {l} m lang und {bb} m breit. Es bekommt eine Fußleiste ringsherum, die Tür (1 m breit) bleibt frei. Wie viele Meter Leiste braucht man?'},
                'o': {'wert': 2 * l + 2 * bb - 1, 'einheit': 'm'}, 'c': f'2 * {l} + 2 * {bb} - 1', 'w': f'Umfang {2 * l + 2 * bb} m, minus Tür: {2 * l + 2 * bb - 1} m.', 'h': 'Die Leiste läuft am Rand – ohne die Tür.'}
    art = R.randrange(2)
    if art == 0:
        f = R.choice([20, 25, 50])
        l, bb = f * R.randint(200 // f, 400 // f), f * R.randint(150 // f, 300 // f)
        l, bb = max(l, bb), min(l, bb)
        return {'y': 'zahl', 'f': {'text': f'Ein Bad ist {zt(Fr(l, 100))} m lang und {zt(Fr(bb, 100))} m breit. Wie viele quadratische Fliesen mit {f} cm Seitenlänge braucht man für den Boden?'},
                'o': {'wert': (l // f) * (bb // f)}, 'c': f'({l} / {f}) * ({bb} / {f})', 'w': f'In cm: {l} : {f} = {l // f} Fliesen in der Länge, {bb} : {f} = {bb // f} in der Breite. {l // f} · {bb // f} = {(l // f) * (bb // f)} Fliesen.',
                'h': 'Rechne in cm und bestimme, wie viele Fliesen in jede Richtung passen.'}
    if R.random() < .5:          # Streichen mit Fenster oder Tür (Prüfung)
        l, h = R.choice([4, 5, 6, Fr(9, 2)]), R.choice([Fr(5, 2), 3])
        loch, lb, lh, rel, kurz = R.choice([('ein Fenster', 2, 1, 'das', 'Fenster'), ('ein Fenster', Fr(3, 2), 1, 'das', 'Fenster'), ('eine Tür', 1, 2, 'die', 'Tür')])
        A = l * h - lb * lh
        return {'y': 'zahl', 'f': {'text': f'Eine Wand ist {zt(l)} m lang und {zt(h)} m hoch. Darin ist {loch} ({zt(lb)} m × {zt(lh)} m), {rel} nicht gestrichen wird. Wie viele m² werden gestrichen?'},
                'o': {'wert': wert(A), 'einheit': 'm²'}, 'c': f'{float(l)} * {float(h)} - {float(lb)} * {float(lh)}',
                'w': f'Wand: {zt(l)} · {zt(h)} = {zt(l * h)} m². {kurz}: {zt(lb)} · {zt(lh)} = {zt(lb * lh)} m². Gestrichen: {zt(l * h)} − {zt(lb * lh)} = {zt(A)} m².',
                'h': 'Ganze Wand minus die Fläche, die frei bleibt.'}
    f = R.choice([2, 3, Fr(5, 2)])          # realistisch: 2–3 kg Samen je Ar (Prüfung)
    ha = R.choice([2, 3, 4, 5, 6])
    return {'y': 'zahl', 'f': {'text': f'Für 1 a Rasen braucht man {zt(f)} kg Samen. Wie viele kg braucht man für {ha} ha?'}, 'o': {'wert': wert(f * ha * 100), 'einheit': 'kg'}, 'c': f'{ha} * 100 * {float(f)}',
            'w': f'{ha} ha = {ha * 100} a. {ha * 100} · {zt(f)} kg = {zt(f * ha * 100)} kg.', 'h': '1 ha = 100 a.'}


# ---------- 7 Verstehen ----------
# Prüfung: alle Antworten mit Begründung
def g_vers(st):
    a, b = R.randint(2, 9), R.randint(2, 9)
    if a == b: b += 1
    if st == 1:
        aussagen = [('1 m² = 100 dm²', 'Ja, 10 dm · 10 dm = 100 dm².', ['Nein, 1 m = 10 dm, also 1 m² = 10 dm².', 'Nein, 1 m² = 1 000 dm² wie bei Volumen.']),
                    ('1 m² = 10 dm²', 'Nein, 10 dm · 10 dm = 100 dm².', ['Ja, 1 m = 10 dm, also 1 m² = 10 dm².', 'Nein, 1 m² = 1 000 dm².']),
                    (f'Ein Rechteck mit {a} cm und {b} cm hat den Flächeninhalt {a + b} cm².', f'Nein, A = {a} cm · {b} cm = {a * b} cm².', [f'Ja, man addiert die Seiten: {a} + {b} = {a + b}.', f'Nein, A = 2 · {a} + 2 · {b} = {2 * a + 2 * b} cm².']),
                    (f'Ein Quadrat mit {a} cm Seitenlänge hat den Umfang {4 * a} cm.', f'Ja, u = 4 · {a} cm = {4 * a} cm.', [f'Nein, u = {a} · {a} = {a * a} cm.', f'Nein, u = 2 · {a} cm = {2 * a} cm.'])]
    elif st == 2:
        aussagen = [('Verdoppelt man Länge und Breite eines Rechtecks, wird die Fläche doppelt so groß.', f'Nein, viermal so groß: z. B. {a} · {b} = {a * b}, {2 * a} · {2 * b} = {4 * a * b}.', ['Ja, doppelte Seiten, doppelte Fläche.', 'Nein, die Fläche bleibt gleich.']),
                    ('1 ha = 100 a', 'Ja, die Umrechnungszahl bei Flächen ist 100.', ['Nein, 1 ha = 10 a.', 'Nein, 1 ha = 1 000 a.']),
                    ('1 km² = 1 000 m²', 'Nein, 1 km² = 1 000 m · 1 000 m = 1 000 000 m².', ['Ja, 1 km = 1 000 m.', 'Nein, 1 km² = 10 000 m².']),
                    (f'{a} m² {b} dm² = {a},{b} m²', f'Nein, {b} dm² = 0,0{b} m², also {a},0{b} m².', ['Ja, die dm² stehen direkt hinter dem Komma.', f'Nein, richtig ist {a},00{b} m².']),
                    (f'{a} m² {b} dm² = {a},0{b} m²', 'Ja, zu dm² gehören zwei Stellen nach dem Komma.', [f'Nein, richtig ist {a},{b} m².', f'Nein, richtig ist {a},00{b} m².']),
                    (f'{a} a = {a * 100} m²', 'Ja, 1 a = 100 m².', [f'Nein, 1 a = 10 m², also {a * 10} m².', f'Nein, 1 a = 1 000 m², also {zt(a * 1000)} m².']),
                    (f'{a} a = {a * 10} m²', f'Nein, 1 a = 100 m², also {a} a = {a * 100} m².', ['Ja, 1 a = 10 m².', f'Nein, 1 a = 1 000 m², also {zt(a * 1000)} m².']),
                    (f'{a * 100} cm² = {a} dm²', 'Ja, 10 cm · 10 cm = 100 cm² = 1 dm².', [f'Nein, {a * 100} cm² = {a * 10} dm².', f'Nein, {a * 100} cm² = {zt(Fr(a, 10))} dm².'])]
    else:
        aussagen = [('Zwei Rechtecke mit gleichem Umfang haben immer den gleichen Flächeninhalt.', 'Nein, z. B. 6 × 2 (A = 12) und 4 × 4 (A = 16) haben beide u = 16.', ['Ja, gleicher Rand heißt gleiche Fläche.', 'Ja, wenn beide Figuren Rechtecke sind.']),
                    ('Schneidet man aus einem Rechteck an einer Ecke ein kleines Rechteck aus, bleibt der Umfang gleich.', 'Ja, die beiden fehlenden Randstücke werden durch zwei gleich lange neue Kanten ersetzt.', ['Nein, der Umfang wird kleiner, weil ein Stück fehlt.', 'Nein, der Umfang wird um den ganzen Rand des Stücks größer.']),
                    ('Beim Zerlegen und beim Ergänzen kommt derselbe Flächeninhalt heraus.', 'Ja, es ist dieselbe Figur – nur anders gerechnet.', ['Nein, beim Ergänzen kommt mehr heraus.', 'Nein, beim Zerlegen kommt mehr heraus.']),
                    (f'Ein Quadrat mit Umfang {4 * a} cm hat einen größeren Flächeninhalt als ein Rechteck {a + 1} cm × {a - 1} cm.', f'Ja, {a * a} cm² > {(a + 1) * (a - 1)} cm² (gleicher Umfang).', [f'Nein, beide haben {a * a} cm², weil der Umfang gleich ist.', f'Nein, das Rechteck ist größer, weil {a + 1} > {a} ist.'])]
    s_, grund, f = R.choice(aussagen)
    return {**wahl_rund(R, grund, f, 3), 'f': {'text': f'Stimmt die Aussage? „{s_}“'}, 'w': grund, 'h': 'Rechne ein Beispiel durch.'}


GEN = {'einheitsquadrate': g_eq, 'rechteck': g_re, 'einheiten': g_ein, 'kommaschreibweise': g_komma, 'zerlegen': g_zer, 'sachaufgaben': g_sach, 'verstehen': g_vers}

DATEI = datei(E, 'Flächeninhalt und Umfang von Rechteck, Quadrat und zusammengesetzten Figuren berechnen und Flächeneinheiten umrechnen.', MERKE,
              [('Flächeninhalt verstehen', ['einheitsquadrate', 'rechteck']),
               ('Flächeneinheiten', ['einheiten', 'kommaschreibweise']),
               ('Zusammengesetzte Flächen', ['zerlegen', 'sachaufgaben', 'verstehen'])],
              ETAPPEN, GEN,
              offen=['Dreieck, Parallelogramm, Trapez und allgemeine Vielecke aus „umfang“ weggelassen: lehrplan_gym Kl. 5 nennt nur Zerlegen/Ergänzen, Flächeneinheiten und die Rechteckformel. Die Formeln für diese Figuren sind Stoff späterer Jahrgangsstufen.',
                     'Lehrplan „Näherungswerte durch Modellierung mit Rechtecken“ nur indirekt (Zerlegen in Rechtecke). Die Prüfung schlägt dafür eine spätere eigene Lernkarte vor (krumme Fläche, z. B. ein See, im Kästchengitter innen und außen abschätzen); noch nicht gebaut – braucht eine gezeichnete krumme Figur und eine Zählregel für angeschnittene Kästchen.',
                     'Zeichnungen: Rechtecke, Einheitsquadrate (gestrichelte Hilfslinien), L-Formen und Rahmen als Figur. Das Kind kann Flächen nicht selbst färben oder zerlegen.'])

# Umbau U5 (Achte Runde, Vorgabe 16.11.): Lernkarten nach dem neuen Muster – einstieg, woerter (≤ 3), Kartenbild,
# Bildergeschichte (schritte mit bild), „Pass auf!“ (fehler + fehler_bild), MERKE (regel).
# Situationen: Spielhaus mit Fliesen, Zimmer (Teppich, Fußleiste, Schrank-Ecke), Garten (Zaun, Rasen), Preisschild.
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl5.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl5 import umbau  # noqa: E402

L_FORM = [['_P0', '_P1', '8 m'], ['_P1', '_P2', '4 m'], ['_P2', '_P3', '3 m'], ['_P3', '_P4', '2 m'], ['_P4', '_P5', '5 m'], ['_P5', '_P0', '6 m']]
L_PUNKTE = {'_P0': [0, 0], '_P1': [8, 0], '_P2': [8, 4], '_P3': [5, 4], '_P4': [5, 6], '_P5': [0, 6]}
RECHTECK = lambda a, b, ta, tb, tc='', td='': {'typ': 'figur', 'punkte': {'_A': [0, 0], '_B': [a, 0], '_C': [a, b], '_D': [0, b]}, 'flaeche': ['_A', '_B', '_C', '_D'],
                                                'linien': [['_A', '_B', ta], ['_B', '_C', tb], ['_C', '_D', tc], ['_D', '_A', td]]}

# Beide Gärten im selben Maßstab: Garten 1 (6 m × 2 m) links, Garten 2 (4 m × 4 m) rechts daneben
GAERTEN = {'_A': [0, 0], '_B': [6, 0], '_C': [6, 2], '_D': [0, 2], '_E': [8, 0], '_F': [12, 0], '_G': [12, 4], '_H': [8, 4]}
GARTEN1 = [['_A', '_B', '6 m'], ['_B', '_C', '2 m'], ['_C', '_D'], ['_D', '_A']]
GARTEN2 = [['_E', '_F', '4 m'], ['_F', '_G', '4 m'], ['_G', '_H'], ['_H', '_E']]

KARTEN = {
 'einheitsquadrate': {
  'einstieg': 'Du legst den Boden eines Spielhauses mit quadratischen Fliesen aus. Wie groß der Boden ist, sagt die Zahl der Fliesen. Das heißt ⟦Flächeninhalt⟧.',
  'woerter': [['Flächeninhalt', 'wie viele Einheitsquadrate in eine Fläche passen'], ['Einheitsquadrat', 'ein Quadrat mit der Seitenlänge 1, zum Beispiel 1 cm'],
              ['cm²', 'Quadratzentimeter: die Fläche eines Quadrats mit 1 cm Seite']],
  'bild': 'BEHALTEN',
  'schritte': [{'text': 'Das Rechteck ist 5 cm lang: In eine Reihe passen 5 Einheitsquadrate.'},
               {'text': 'Es ist 3 cm breit: Es gibt 3 Reihen.'},
               {'text': '3 · 5 = 15 Quadrate. Also ist der Flächeninhalt ⟦A = 15 cm²⟧.'}],
  'fehler': '5 + 3 = 8 cm² ist falsch. Beim Flächeninhalt zählst du Fliesen: Reihen mal Fliesen pro Reihe.',
  'regel': 'Flächeninhalt = ⟦Reihen mal Quadrate pro Reihe⟧. Zähle, wie viele Einheitsquadrate hineinpassen.'},
 'rechteck': {
  'einstieg': 'Ein Zimmer bekommt neuen Teppich und eine Fußleiste am Rand. Für den Teppich brauchst du die Fläche, für die Leiste die Länge des Randes. Diese Länge heißt ⟦Umfang⟧.',
  'woerter': [['A = a · b', 'Flächeninhalt = Länge mal Breite'], ['m²', 'Quadratmeter: die Fläche eines Quadrats mit 1 m Seite'], ['Umfang u', 'die Länge des ganzen Randes']],
  'bild': 'BEHALTEN',
  'schritte': [{'text': 'Teppich: A = a · b = 8 m · 5 m = ⟦40 m²⟧.'},
               {'text': 'Leiste: Der Rand hat zwei Seiten mit 8 m und zwei mit 5 m.',
                'bild': {'linien': [['A', 'B', '8 m'], ['B', 'C', '5 m'], ['C', 'D', '8 m'], ['D', 'A', '5 m']]}},
               {'text': 'Umfang u = 2 · 8 m + 2 · 5 m = ⟦26 m⟧.'}],
  'fehler': 'Umfang und Fläche verwechseln ist der häufigste Fehler. Die Leiste kaufst du in Metern, den Teppich in Quadratmetern.',
  'regel': 'Fläche ist Länge mal Breite: ⟦A = a · b⟧. Umfang: u = 2 · a + 2 · b.'},
 'einheiten': {
  'einstieg': 'Ein Quadrat mit 1 m Seite legst du mit Quadraten von 1 dm aus. 10 Reihen zu je 10 sind 100 Stück. Darum ist bei ⟦Flächeneinheiten⟧ die Umrechnungszahl 100.',
  'woerter': [['Flächeneinheit', 'eine Einheit für Flächen, zum Beispiel cm² oder m²'], ['dm²', 'Quadratdezimeter: Fläche eines Quadrats mit 10 cm Seite']],
  'bild': 'BEHALTEN',
  'schritte': [{'text': 'Rechne 7 m² in dm² um. 1 m² sind 10 · 10 = 100 dm².'},
               {'text': '7 m² sind 7-mal so viel: 7 · 100 = ⟦700 dm²⟧.'}],
  'fehler': '1 m² = 10 dm² ist falsch. Die Seite ist 10-mal so lang, die Fläche aber 100-mal so groß.',
  'regel': 'Bei Flächen ist die ⟦Umrechnungszahl 100⟧. km², ha, a, m², dm², cm², mm²: jeder Schritt mal oder durch 100.'},
 'kommaschreibweise': {
  'einstieg': 'Für Cent gibt es zwei Stellen hinter dem Komma: 4,07 €. Denn 1 € sind 100 ct, und bei Flächen ist es genauso. So schreibst du Flächen in ⟦Kommaschreibweise⟧.',
  'woerter': [['Kommaschreibweise', 'eine Fläche mit Komma in einer Einheit: 6,05 m² statt 6 m² 5 dm²']],
  'bild': {'typ': 'tabelle', 'kopf': ['m²', 'dm²'], 'zeilen': [['6', '5']]},
  'schritte': [{'text': 'Schreibe 6 m² 5 dm² in m². Vor das Komma kommen die 6.'},
               {'text': 'dm² bekommen zwei Stellen: Aus 5 wird 05.', 'bild': {'zeilen': [['6', '05']]}},
               {'text': 'Ergebnis: ⟦6,05 m²⟧.'}],
  'fehler': '6 m² 5 dm² = 6,5 m² ist falsch. 6,5 m² sind 6 m² 50 dm², so wie 6,50 € nicht 6,05 € sind.',
  'fehler_bild': {'zeilen': [['6', '50']]},
  'regel': 'Bei Flächen bekommt jede kleinere Einheit ⟦zwei Stellen⟧. 3,25 m² = 3 m² 25 dm² und 4,07 a = 4 a 7 m².'},
 'zerlegen': {
  'einstieg': 'In einem Zimmer fehlt eine Ecke, dort ist ein Schrank eingebaut. Der Boden hat die Form eines L. Du denkst dir die Ecke dazu: Das heißt ⟦ergänzen⟧.',
  'woerter': [['ergänzen', 'das fehlende Stück dazudenken und am Ende abziehen'], ['zerlegen', 'die Fläche in Rechtecke aufteilen und addieren'],
              ['8 m × 6 m', 'gelesen „8 m mal 6 m“: ein Rechteck, 8 m lang und 6 m breit']],
  'bild': 'BEHALTEN',
  'schritte': [{'text': 'Ergänze zum großen Rechteck 8 m × 6 m. Es hat 48 m².',
                'bild': {'punkte': dict(L_PUNKTE, _E=[8, 6]), 'linien': L_FORM + [['_P2', '_E', '', 'gestrichelt'], ['_E', '_P4', '', 'gestrichelt']]}},
               {'text': 'Das fehlende Stück ist 3 m × 2 m = 6 m².'},
               {'text': 'Ziehe es ab: 48 − 6 = ⟦42 m²⟧.'},
               {'text': 'Probe durch zerlegen: 32 m² + 10 m² = 42 m².',
                'bild': {'punkte': dict(L_PUNKTE, _Z=[0, 4]), 'linien': L_FORM + [['_P3', '_Z', '', 'gestrichelt']]}}],
  'fehler': 'Alle Seiten der L-Form malnehmen ist falsch. Jedes Rechteck hat nur eine Länge und eine Breite.',
  'regel': '⟦Zerlegen⟧ in Rechtecke und addieren oder ergänzen und abziehen. Beide Wege ergeben dasselbe.'},
 'sachaufgaben': {
  'einstieg': 'Ein Garten bekommt einen Zaun und neuen Rasen. Der Zaun läuft am Rand entlang, der Rasen bedeckt den Boden. Frag dich deshalb zuerst: ⟦Rand oder Fläche⟧?',
  'woerter': [['ringsherum', 'einmal ganz um den Rand herum']],
  'bild': RECHTECK(12, 7, '12 m', '7 m'),
  'schritte': [{'text': 'Der Garten ist 12 m lang und 7 m breit. Gesucht ist der Zaun ringsherum.'},
               {'text': 'Ein Zaun läuft am Rand. Gesucht ist also der Umfang.', 'bild': RECHTECK(12, 7, '12 m', '7 m', '12 m', '7 m')},
               {'text': 'u = 2 · 12 m + 2 · 7 m = ⟦38 m⟧ Zaun.'}],
  'fehler': 'Für den Zaun 12 · 7 = 84 rechnen ist falsch. Das ist die Rasenfläche in m², kein Zaun in Metern.',
  'regel': 'Zaun, Rand, Leiste: ⟦Umfang⟧. Rasen, Boden, Farbe: Flächeninhalt. Rechne in einer Einheit.'},
 'verstehen': {
  'einstieg': 'Zwei Gärten haben beide 16 m Zaun. Ist in beiden gleich viel Platz zum Spielen? Nicht unbedingt: ⟦Gleicher Umfang⟧ heißt nicht gleiche Fläche.',
  'woerter': [['Gegenbeispiel', 'ein Fall, der eine Behauptung widerlegt']],
  'bild': {'typ': 'figur', 'punkte': GAERTEN, 'flaeche': ['_A', '_B', '_C', '_D'], 'linien': GARTEN1},
  'schritte': [{'text': 'Garten 1: 6 m × 2 m. Umfang 16 m, Fläche 12 m².'},
               {'text': 'Garten 2: 4 m × 4 m. Umfang 16 m, Fläche 16 m².', 'bild': {'linien': GARTEN1 + GARTEN2}},
               {'text': 'Gleicher Umfang, aber ⟦verschiedene Flächen⟧. Das ist ein Gegenbeispiel.'}],
  'fehler': '„Doppelte Seiten, doppelte Fläche“ ist falsch. 2 m × 3 m sind 6 m². 4 m × 6 m sind 24 m², viermal so viel.',
  'regel': 'Gleicher Umfang heißt ⟦nicht gleiche Fläche⟧. Doppelte Länge und Breite ergeben die vierfache Fläche.'},
}
umbau(DATEI, KARTEN)


# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl5) ----------
# Neue Übungen nach Prüfungsvorbild (Jahrgangsstufentest 6 Bayern: 1 ha ≈ Fußballfeld, Plakat mit Passfotos, Rechteck mit
# vorgegebenem Umfang, Quadrat aus Umfang/Fläche, Fläche zwischen zwei Quadraten, Zaun im Abstand; Känguru: Umfang zusammengesetzter Figuren).
from _schwer_kl5 import A, L, Z, de, einzig, ergaenze, wahl  # noqa: E402


def _schwer():
    N = {}
    zerl = [(l, b) for b in range(1, 25) for l in range(b, 25) if l * b == 24]
    N['einheitsquadrate'] = [
        Z(2, 'Ein Rechteck ist mit 48 Einheitsquadraten (1 cm²) ausgelegt. Es hat 6 Reihen. Wie lang ist es?', '48 / 6', '48 Quadrate in 6 Reihen: 48 : 6 = 8 Quadrate pro Reihe, also 8 cm lang.',
          'Wie viele Quadrate liegen in einer Reihe?', einheit='cm'),
        Z(2, 'Ein Quadrat ist aus 49 Einheitsquadraten (1 cm²) gelegt. Wie lang ist eine Seite?', str(einzig([n for n in range(1, 20) if n * n == 49])),
          '7 Reihen mit je 7 Quadraten: 7 · 7 = 49. Die Seite ist 7 cm lang.', 'Welche Zahl mal sich selbst ergibt 49?', einheit='cm'),
        Z(3, 'Aus 24 Einheitsquadraten soll ein Rechteck gelegt werden. Wie viele verschieden geformte Rechtecke gibt es? (Gedreht zählt nicht als neu.)', str(len(zerl)),
          '24 = 1 · 24 = 2 · 12 = 3 · 8 = 4 · 6. Das sind 4 Rechtecke.', 'Suche alle Zahlenpaare, deren Produkt 24 ist.'),
        Z(3, 'Auf ein Plakat sollen 24 Fotos geklebt werden, jedes 4 cm breit und 5 cm hoch, ohne Überlappung. Wie groß muss das Plakat mindestens sein (in cm²)?', '24 * 4 * 5',
          'Ein Foto: 4 cm · 5 cm = 20 cm². 24 Fotos: 24 · 20 cm² = 480 cm².', 'Rechne zuerst die Fläche eines Fotos aus.', einheit='cm²'),
        Z(3, 'Ein Quadrat mit 4 cm Seitenlänge wird aus Einheitsquadraten (1 cm²) gelegt. Wie viele Einheitsquadrate liegen am Rand?', '4 * 4 - 2 * 2',
          'Alle: 4 · 4 = 16. Innen bleiben 2 · 2 = 4. Am Rand: 16 − 4 = 12.', 'Zähle nicht jede Ecke doppelt. Tipp: alle minus die inneren.'),
        Z(3, 'Ein Rechteck aus Einheitsquadraten ist 3-mal so lang wie breit und enthält 75 Quadrate. Wie viele Quadrate breit ist es?', str(einzig([b for b in range(1, 20) if 3 * b * b == 75])),
          'Breite b, Länge 3 · b: 3 · b · b = 75, also b · b = 25 und b = 5.', 'Probiere Breiten aus: 3 · 4 · 4 = 48, 3 · 5 · 5 = ?'),
    ]
    u14 = max(l * (7 - l) for l in range(1, 7))
    vorher = einzig([(l, b) for b in range(1, 13) for l in range(b, 13) if l * b == 12 and (l + 1) * (b + 1) == 20])
    N['rechteck'] = [
        Z(2, 'Ein Rechteck ist 12 cm lang und hat den Umfang 34 cm. Wie breit ist es?', '34 / 2 - 12', 'Länge + Breite = 34 cm : 2 = 17 cm. Breite: 17 cm − 12 cm = 5 cm.',
          'Der halbe Umfang ist Länge plus Breite.', einheit='cm'),
        Z(2, 'Ein Rechteck hat den Flächeninhalt 72 cm² und ist 6 cm breit. Wie groß ist sein Umfang?', '2 * (72 / 6) + 2 * 6', 'Länge: 72 : 6 = 12 cm. Umfang: 2 · 12 cm + 2 · 6 cm = 36 cm.',
          'Bestimme zuerst die Länge.', einheit='cm'),
        Z(3, 'Rechtecke mit ganzzahligen Seitenlängen (in cm) sollen den Umfang 14 cm haben. Wie groß ist der größte mögliche Flächeninhalt?', str(u14),
          'Länge + Breite = 7 cm: 1 · 6 = 6, 2 · 5 = 10, 3 · 4 = 12. Am größten: 12 cm².', 'Länge plus Breite ist der halbe Umfang. Probiere alle Möglichkeiten.', einheit='cm²'),
        Z(3, 'Ein Quadrat hat den Flächeninhalt 81 cm². Wie groß ist sein Umfang?', '4 * 9', 'Seite: 9 cm, weil 9 · 9 = 81. Umfang: 4 · 9 cm = 36 cm.', 'Bestimme zuerst die Seitenlänge.', einheit='cm'),
        Z(3, 'Ein Rechteck ist 8 cm lang und 3 cm breit. Ein Quadrat hat denselben Umfang. Wie groß ist der Flächeninhalt des Quadrats?', '((2 * 8 + 2 * 3) / 4) ** 2',
          'Umfang: 22 cm. Quadratseite: 22 cm : 4 = 5,5 cm. Fläche: 5,5 cm · 5,5 cm = 30,25 cm².', 'Berechne den Umfang und teile ihn auf 4 gleiche Seiten.', einheit='cm²'),
        L(3, 'Ein Rechteck hat den Flächeninhalt 12 cm². Werden Länge und Breite je um 1 cm größer, hat es 20 cm². Wie lang und wie breit war es? (ganze cm)',
          'Länge □ cm, Breite □ cm', 'Trage zuerst die längere Seite ein.', [str(vorher[0]), str(vorher[1])],
          'Mögliche Rechtecke mit 12 cm²: 12 · 1, 6 · 2, 4 · 3. Nur 4 · 3 wird zu 5 · 4 = 20 cm².', 'Probiere alle Rechtecke mit 12 cm² aus.'),
    ]
    fussball = ['etwa 70 a', 'etwa 70 m²', 'etwa 70 ha', 'etwa 70 km²']
    flaech = {'3 ha': 30000, '290 a': 29000, '31 000 m²': 31000, '0,03 km²': 30000}
    N['einheiten'] = [
        Z(2, 'Rechne um: 5 ha = ? m²', '5 * 100 * 100', '1 ha = 100 a = 10 000 m². 5 ha = 50 000 m².', 'Von ha zu m² sind es zwei Schritte mit je mal 100.', einheit='m²'),
        Z(2, 'Rechne um: 30 000 cm² = ? m²', '30000 / 100 / 100', 'cm² → dm²: durch 100 (300 dm²). dm² → m²: durch 100 (3 m²).', 'Zwei Schritte mit je durch 100.', einheit='m²'),
        wahl(3, 'Welche Fläche hat ein Fußballfeld ungefähr?', fussball, lambda o: o == 'etwa 70 a',
             'Ein Fußballfeld ist etwa 105 m lang und 68 m breit: rund 7 000 m² = 70 a. Das ist knapp 1 ha.', 'Schätze Länge und Breite in Metern und rechne um.'),
        wahl(3, 'Welche Fläche ist am kleinsten: 3 ha; 290 a; 31 000 m²; 0,03 km²?', list(flaech), lambda o: flaech[o] == min(flaech.values()),
             'In m²: 3 ha = 30 000 m², 290 a = 29 000 m², 31 000 m², 0,03 km² = 30 000 m². Am kleinsten: 290 a.', 'Rechne alle Angaben in m² um.'),
        A(3, 'Jemand rechnet: 4 m² = 40 dm². Was ist falsch?', 'Bei Flächen ist die Umrechnungszahl 100: 4 m² = 400 dm².',
          ['Nichts, das stimmt.', 'Richtig ist 4 000 dm².', 'Richtig ist 0,4 dm².'],
          '1 m² ist ein Quadrat mit 10 dm · 10 dm = 100 dm². Also 4 m² = 400 dm².', 'Zeichne 1 m² als Quadrat mit 10 dm Seitenlänge.'),
        Z(3, 'Wie viele Quadrate mit 1 cm Seitenlänge passen in 1 m²?', '100 * 100', '1 m = 100 cm. In 1 m² passen 100 Reihen mit je 100 Quadraten: 10 000.', 'Wie viele cm-Quadrate liegen in einer Reihe von 1 m?'),
    ]
    klein = {'4,5 a': 450, '445 m²': 445, '4 a 60 m²': 460, '4,6 a': 460}
    N['kommaschreibweise'] = [
        Z(2, 'Schreibe in m²: 5 m² 3 dm²', '5 + 3 / 100', 'dm² bekommen zwei Stellen: 3 dm² = 0,03 m². Also 5,03 m².', 'Zwei Stellen nach dem Komma für dm².', einheit='m²'),
        Z(2, 'Rechne um: 2,5 ha = ? a', '2.5 * 100', '1 ha = 100 a. 2,5 ha = 250 a.', 'Von ha zu a: mal 100.', einheit='a'),
        wahl(3, 'Welche Fläche ist am kleinsten: 4,5 a; 445 m²; 4 a 60 m²; 4,6 a?', list(klein), lambda o: klein[o] == min(klein.values()),
             'In m²: 4,5 a = 450 m², 445 m², 4 a 60 m² = 460 m², 4,6 a = 460 m². Am kleinsten: 445 m².', 'Rechne alle Angaben in m² um.'),
        Z(3, 'Berechne 2,4 a − 75 m². Gib das Ergebnis in m² an.', '240 - 75', '2,4 a = 240 m². 240 m² − 75 m² = 165 m².', 'Rechne zuerst in dieselbe Einheit um.', einheit='m²'),
        A(3, 'Jemand schreibt: 7 m² 5 dm² = 7,5 m². Was ist falsch?', 'dm² brauchen zwei Stellen: richtig ist 7,05 m².',
          ['Nichts, das stimmt.', 'Richtig ist 7,005 m².', 'Richtig ist 75 m².'], '7,5 m² wären 7 m² 50 dm². 5 dm² sind 0,05 m², also 7,05 m².', 'Wie viele Stellen bekommen dm² nach dem Komma?'),
        Z(3, 'Wie viele dm² fehlen 0,75 m² bis zu 1 m²?', '100 - 75', '0,75 m² = 75 dm², 1 m² = 100 dm². Es fehlen 25 dm².', 'Rechne beide Flächen in dm² um.', einheit='dm²'),
    ]
    N['zerlegen'] = [
        Z(2, 'Aus einem Quadrat mit 10 m Seitenlänge wird in einer Ecke ein Quadrat mit 4 m Seitenlänge herausgeschnitten. Wie groß ist die Restfläche?', '10 * 10 - 4 * 4',
          'Großes Quadrat: 100 m². Ausschnitt: 16 m². Rest: 84 m².', 'Ergänzen und abziehen.', einheit='m²'),
        Z(2, 'Ein Bilderrahmen ist außen 30 cm × 20 cm groß, das Bild darin 26 cm × 16 cm. Wie groß ist die Fläche des Rahmens?', '30 * 20 - 26 * 16',
          'Außen: 600 cm². Bild: 416 cm². Rahmen: 600 − 416 = 184 cm².', 'Große Fläche minus Bildfläche.', einheit='cm²'),
        Z(3, 'Ein großes Quadrat hat 8 cm Seitenlänge. Darin liegt ein kleines Quadrat mit 3 cm Seitenlänge. Wie groß ist die Fläche zwischen den beiden Quadraten?', '8 * 8 - 3 * 3',
          'Großes Quadrat: 64 cm². Kleines: 9 cm². Dazwischen: 55 cm².', 'Die Lage des kleinen Quadrats spielt keine Rolle.', einheit='cm²'),
        Z(3, 'Aus einem Quadrat mit 10 m Seitenlänge wird in einer Ecke ein Quadrat mit 4 m Seitenlänge herausgeschnitten. Wie lang ist der Umfang der Restfigur?', '4 * 10',
          'Die zwei weggeschnittenen Randstücke (je 4 m) werden durch zwei neue Kanten (je 4 m) ersetzt. Der Umfang bleibt 4 · 10 m = 40 m.',
          'Zeichne die Figur und gehe den Rand ab. Vergleiche mit dem ganzen Quadrat.', einheit='m'),
        Z(3, 'Eine Treppenfigur besteht aus Quadraten mit 1 cm Seitenlänge: unten 4, darüber 3, dann 2, ganz oben 1, alle links bündig. Wie lang ist ihr Umfang?', '2 * (4 + 4)',
          'Schiebt man die Stufenkanten nach außen, entsteht ein Quadrat mit 4 cm Seitenlänge – gleicher Umfang: 16 cm.', 'Die waagrechten Stufen zusammen sind so lang wie die Grundseite.', einheit='cm'),
        Z(3, 'Zwei gleiche Quadrate mit 5 cm Seitenlänge werden so aneinandergelegt, dass sie eine ganze Seite gemeinsam haben. Wie lang ist der Umfang der neuen Figur?', '2 * 4 * 5 - 2 * 5',
          'Es entsteht ein Rechteck 10 cm × 5 cm: Umfang 30 cm. Die gemeinsame Seite liegt innen und zählt nicht mehr.', 'Welche Figur entsteht?', einheit='cm'),
    ]
    N['sachaufgaben'] = [
        Z(2, 'Ein Garten ist 15 m lang und 8 m breit. 1 m² Rollrasen kostet 3 €. Was kostet der Rasen für den ganzen Garten?', '15 * 8 * 3', 'Fläche: 120 m². Kosten: 120 · 3 € = 360 €.',
          'Rasen braucht man für die Fläche, nicht für den Rand.', einheit='€'),
        Z(2, 'Ein Bild ist 40 cm breit und 30 cm hoch. Ringsherum wird eine Leiste geklebt. Wie viele cm Leiste braucht man?', '2 * 40 + 2 * 30', 'Rand = Umfang: 2 · 40 cm + 2 · 30 cm = 140 cm.',
          'Leiste am Rand: Umfang oder Fläche?', einheit='cm'),
        Z(3, 'Ein Sandkasten ist 3 m × 2 m groß. Im Abstand von 1 m wird ringsum ein Zaun gebaut. Alle 1 m steht ein Pfosten, auch an jeder Ecke. Wie viele Pfosten braucht man?',
          '2 * (3 + 2) + 2 * (2 + 2)', 'Der Zaun bildet ein Rechteck 5 m × 4 m mit Umfang 18 m. Bei einem geschlossenen Zaun gibt es so viele Pfosten wie Meter: 18.',
          'Wie groß ist das Zaun-Rechteck? Bei einem geschlossenen Zaun: Pfosten = Abstände.'),
        Z(3, 'Ein Zimmer ist 4 m lang, 3 m breit und 2,5 m hoch. Alle vier Wände werden gestrichen. Eine Tür (1 m × 2 m) und ein Fenster (1,5 m × 1 m) bleiben frei. Wie viele m² werden gestrichen?',
          '2 * (4 + 3) * 2.5 - 1 * 2 - 1.5 * 1', 'Wände: (4 + 3 + 4 + 3) m · 2,5 m = 35 m². Abzüglich 2 m² und 1,5 m²: 31,5 m².',
          'Lege die vier Wände nebeneinander: ein langes Rechteck.', einheit='m²'),
        Z(3, 'Ein Eimer Farbe reicht für 10 m² Wand. Eine Wand hat 45 m². Wie viele Eimer muss man kaufen?', '-(-45 // 10)',
          '45 : 10 = 4 Rest 5. 4 Eimer reichen nur für 40 m², also braucht man 5 Eimer.', 'Reichen 4 Eimer?'),
        A(3, 'Jemand berechnet den Zaun für einen Garten (12 m × 8 m): 12 · 8 = 96 m. Was ist falsch?', 'Für den Zaun braucht man den Umfang: 2 · 12 m + 2 · 8 m = 40 m.',
          ['Nichts, 96 m stimmt.', 'Richtig ist 12 + 8 = 20 m.', 'Richtig ist 96 m².'], '12 · 8 = 96 ist die Fläche in m². Der Zaun läuft am Rand: Umfang 40 m.', 'Läuft ein Zaun am Rand oder über die Fläche?'),
    ]
    beste = {'5 cm × 5 cm': 25, '6 cm × 4 cm': 24, '8 cm × 2 cm': 16, '9 cm × 1 cm': 9}
    N['verstehen'] = [
        wahl(2, 'Stimmt die Aussage? „Ein Quadrat mit 3 cm Seitenlänge hat den Flächeninhalt 9 cm² und den Umfang 12 cm.“', ['Ja, beides stimmt.', 'Nein, die Fläche ist 12 cm².', 'Nein, der Umfang ist 9 cm.'],
             lambda o: o.startswith('Ja'), 'A = 3 cm · 3 cm = 9 cm², u = 4 · 3 cm = 12 cm.', 'Rechne Fläche und Umfang einzeln nach.'),
        wahl(2, 'Stimmt die Aussage? „1 km² = 100 ha“', ['Ja, die Umrechnungszahl ist 100.', 'Nein, 1 km² = 1 000 ha.', 'Nein, 1 km² = 10 ha.'], lambda o: o.startswith('Ja'),
             'km² → ha ist ein Schritt mit mal 100: 1 km² = 100 ha.', 'Zwischen km² und ha liegt keine andere Einheit.'),
        wahl(3, 'Ein Rechteck wird in beiden Richtungen halbiert (halbe Länge, halbe Breite). Was passiert mit dem Flächeninhalt?', ['Er wird ein Viertel so groß.', 'Er wird halb so groß.', 'Er bleibt gleich.', 'Er wird doppelt so groß.'],
             lambda o: o.startswith('Er wird ein Viertel'), 'Beispiel: 8 cm × 4 cm = 32 cm². Halbiert: 4 cm × 2 cm = 8 cm², ein Viertel von 32 cm².', 'Probiere es mit einem Beispiel aus.'),
        wahl(3, 'Zwei Rechtecke haben beide den Flächeninhalt 36 cm². Haben sie auch denselben Umfang?', ['Nicht unbedingt: 6 × 6 hat 24 cm Umfang, 9 × 4 hat 26 cm.', 'Ja, immer.', 'Ja, weil die Fläche gleich ist.', 'Nein, nie.'],
             lambda o: o.startswith('Nicht unbedingt'), 'Gleiche Fläche heißt nicht gleicher Umfang. Ein Gegenbeispiel genügt: 6 cm × 6 cm (24 cm) und 9 cm × 4 cm (26 cm).',
             'Suche zwei verschiedene Rechtecke mit 36 cm².'),
        wahl(3, 'Welches Rechteck mit dem Umfang 20 cm hat den größten Flächeninhalt?', list(beste), lambda o: beste[o] == max(beste.values()),
             'Alle haben den Umfang 20 cm. Flächen: 25, 24, 16 und 9 cm². Das Quadrat 5 cm × 5 cm ist am größten.', 'Rechne für jedes Rechteck die Fläche aus.'),
        A(3, 'Jemand sagt: „Verdreifache ich die Seiten eines Quadrats, verdreifacht sich der Flächeninhalt.“ Stimmt das?', 'Nein, er wird neunmal so groß.',
          ['Ja, das stimmt.', 'Nein, er wird sechsmal so groß.', 'Nein, er bleibt gleich.'], 'Beispiel: 2 cm → 4 cm². 6 cm → 36 cm². 36 : 4 = 9. Länge und Breite werden je verdreifacht: 3 · 3 = 9.',
          'Rechne mit einem Beispiel: Seite 2 cm und Seite 6 cm.'),
    ]
    return N


ergaenze(DATEI, _schwer(), 1050)

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('messen.flaechen', 13_5_9)
# b) gefragt ist die ANZAHL der Einheitsquadrate, Lösung hatte die Einheit cm² → Anzahl ohne Einheit, Weg nennt beides
for _c, _a, _b in [('9 * 4', 4, 9), ('7 * 3', 3, 7), ('3 * 6', 6, 3), ('3 * 3', 3, 3), ('7 * 2', 2, 7), ('7 * 4', 4, 7)]:
    _n = _a * _b
    BF.loesung('einheitsquadrate', 'Wie viele Einheitsquadrate (1 cm²) passen in das Rechteck?', enthaelt=f'"c": "{_c}"',
               o={'wert': _n}, w=f'{_a} Reihen zu je {_b} Quadraten: {_a} · {_b} = {_n} Einheitsquadrate. Der Flächeninhalt ist also {_n} cm².')
# c) Beinahe-Dublette (5 · 6 und 6 · 5) → andere Vergrößerung
BF.ersetze('einheitsquadrate', 'Ein Rechteck aus 6 · 5 Einheitsquadraten wird in beiden Richtungen doppelt so lang. Wie viele Einheitsquadrate passen jetzt hinein?', BF.Z(
    'Ein Rechteck aus 4 · 3 Einheitsquadraten wird doppelt so lang und dreimal so breit. Wie viele Einheitsquadrate passen jetzt hinein?', 72, '(2 * 4) * (3 * 3)',
    'Neu: 8 · 9 = 72 Quadrate – sechsmal so viele wie 12 (2 · 3 = 6).', 'Rechne die neuen Seitenlängen aus.'))
# a) dreimal derselbe Gedanke auf Stufe 3 (m und cm → dm²) → zwei davon Stufe 2
BF.stufe('rechteck', 'Ein Rechteck ist 5 m lang und 50 cm breit. Wie groß ist der Flächeninhalt in dm²?', 2)
BF.stufe('rechteck', 'Ein Rechteck ist 3 m lang und 60 cm breit. Wie groß ist der Flächeninhalt in dm²?', 2)

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----

# ---- LÜCKEN (Achtzehnte Runde, Teil B, Zweig luecken-kl5): Näherungswerte mit Rechtecken (LehrplanPLUS M5 4.2) ----
# Die Karte „sachaufgaben“ bekommt vier Stufe-3-Übungen: krumm begrenzte Fläche (See) über einem Kästchengitter und ein Teich
# zwischen einem inneren und einem äußeren Rechteck. Karte und alle bisherigen Aufgaben bleiben unverändert (_luecken_kl5_nachweis.py).
from _luecken_kl5 import ergaenze_karte  # noqa: E402


def _drin(p, poly):
    x, y = p; c = False
    for i in range(len(poly)):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % len(poly)]
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1): c = not c
    return c


def _kaestchen(poly, b, h, n=30):
    """(ganz innen, angeschnitten) – gezählt über n·n Probepunkte je Kästchen."""
    voll = teil = 0
    for i in range(b):
        for j in range(h):
            k = sum(_drin((i + (u + .5) / n, j + (v + .5) / n), poly) for u in range(n) for v in range(n))
            voll += k == n * n; teil += 0 < k < n * n
    return voll, teil


def _gitter(b, h, poly):
    pk = {'_A': [0, 0], '_B': [b, 0], '_C': [b, h], '_D': [0, h]}
    pk.update({f'_s{i}': list(p) for i, p in enumerate(poly)})
    li = [['_A', '_B', ''], ['_B', '_C', ''], ['_C', '_D', ''], ['_D', '_A', '']]
    for x in range(1, b):
        pk[f'_xu{x}'], pk[f'_xo{x}'] = [x, 0], [x, h]; li.append([f'_xu{x}', f'_xo{x}', '', 'gestrichelt'])
    for y in range(1, h):
        pk[f'_yl{y}'], pk[f'_yr{y}'] = [0, y], [b, y]; li.append([f'_yl{y}', f'_yr{y}', '', 'gestrichelt'])
    return {'typ': 'figur', 'punkte': pk, 'flaeche': [f'_s{i}' for i in range(len(poly))], 'linien': li}


SEE = [(0.5, 3), (1.5, 1), (4, 0.5), (6.5, 1), (7.5, 3), (6.5, 5), (4, 5.5), (1.5, 5)]
SEE_VOLL, SEE_TEIL = _kaestchen(SEE, 8, 6)
SEE_AUSSEN = SEE_VOLL + SEE_TEIL
_fl = abs(sum(SEE[i][0] * SEE[(i + 1) % 8][1] - SEE[(i + 1) % 8][0] * SEE[i][1] for i in range(8))) / 2
assert (SEE_VOLL, SEE_AUSSEN) == (20, 40) and SEE_VOLL < _fl < SEE_AUSSEN
SEE_BILD = _gitter(8, 6, SEE)
TEICH = [(0, 3), (1, 1), (3, 0), (6, 0), (8.5, 1.5), (9, 3.5), (7.5, 5.5), (4, 6), (1, 5)]
assert all(_drin(p, TEICH) for p in [(2, 1.5), (7, 1.5), (7, 4.5), (2, 4.5)])
TEICH_BILD = {'typ': 'figur',
              'punkte': {**{f'_t{i}': list(p) for i, p in enumerate(TEICH)}, '_A': [0, 0], '_B': [9, 0], '_C': [9, 6], '_D': [0, 6],
                         '_E': [2, 1.5], '_F': [7, 1.5], '_G': [7, 4.5], '_H': [2, 4.5]},
              'flaeche': [f'_t{i}' for i in range(len(TEICH))],
              'linien': [['_A', '_B', '9 m', 'gestrichelt'], ['_B', '_C', '6 m', 'gestrichelt'], ['_C', '_D', '', 'gestrichelt'], ['_D', '_A', '', 'gestrichelt'],
                         ['_E', '_F', '5 m', 'gestrichelt'], ['_F', '_G', '3 m', 'gestrichelt'], ['_G', '_H', '', 'gestrichelt'], ['_H', '_E', '', 'gestrichelt']]}
NAEHERUNG = [
    Z(3, 'Ein See auf einer Karte. Jedes Kästchen steht für 1 km Länge und 1 km Breite, also 1 km². Wie viele Kästchen liegen ganz im See?',
      str(SEE_VOLL), f'Zeile für Zeile zählen: 0 + 4 + 6 + 6 + 4 + 0 = {SEE_VOLL} Kästchen liegen ganz im See. Der See ist also größer als {SEE_VOLL} km².',
      'Zähle Zeile für Zeile nur die Kästchen, die ganz gefärbt sind.', grafik=SEE_BILD),
    wahl(3, 'Die Kästchen sind 1 km². Was kannst du über die Fläche des Sees sicher sagen?',
         [f'Sie ist größer als {SEE_VOLL} km² und kleiner als {SEE_AUSSEN} km².', f'Sie ist kleiner als {SEE_VOLL} km².', f'Sie ist größer als {SEE_AUSSEN} km².', 'Sie ist genau 48 km².'],
         lambda o: o.startswith('Sie ist größer als') and 'kleiner' in o,
         f'Innen liegen {SEE_VOLL} ganze Kästchen, also mehr als {SEE_VOLL} km². Alle Kästchen, die der See berührt, sind {SEE_VOLL} + {SEE_TEIL} = {SEE_AUSSEN}. '
         f'Sie decken den See ganz ab, also weniger als {SEE_AUSSEN} km². 48 km² ist die ganze Karte (8 · 6).',
         'Zähle die ganzen Kästchen im See. Zähle dann alle Kästchen, die der See berührt.', grafik=SEE_BILD),
    wahl(3, 'Jedes Kästchen ist 1 km². Welcher dieser Werte kommt als Fläche des Sees in Frage?',
         [f'etwa {(SEE_VOLL + SEE_AUSSEN) // 2} km²', f'etwa {SEE_VOLL // 2} km²', f'etwa {SEE_AUSSEN + 5} km²', 'etwa 48 km²'],
         lambda o: SEE_VOLL < int(o.split()[1]) < SEE_AUSSEN,
         f'Die Fläche liegt zwischen {SEE_VOLL} km² (ganze Kästchen) und {SEE_AUSSEN} km² (alle berührten Kästchen). '
         f'Nur {(SEE_VOLL + SEE_AUSSEN) // 2} km² liegt dazwischen. Angeschnittene Kästchen zählen etwa halb: {SEE_VOLL} + {SEE_TEIL} : 2 = {SEE_VOLL + SEE_TEIL // 2}.',
         'Suche erst eine untere und eine obere Grenze mit den Kästchen.', grafik=SEE_BILD),
    L(3, 'Ein Teich liegt ganz im großen Rechteck (9 m mal 6 m). Das kleine Rechteck (5 m mal 3 m) liegt ganz im Teich. Zwischen welchen Werten liegt die Fläche des Teichs?',
      'mehr als □ m², weniger als □ m²', 'Trage die beiden Grenzen ein.', ['5 * 3', '9 * 6'],
      'Das kleine Rechteck liegt im Teich: Der Teich ist größer als 5 · 3 = 15 m². Das große Rechteck umschließt ihn: Er ist kleiner als 9 · 6 = 54 m².',
      'Rechne die Fläche beider Rechtecke aus. Welches liegt innen, welches außen?', grafik=TEICH_BILD),
]
ergaenze_karte(DATEI, 'sachaufgaben', NAEHERUNG, 18_5_8)
# ---- LÜCKEN ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl5, siehe _durchsicht_kl5.py) ----
from _durchsicht_kl5 import Durchsicht, durchsicht_anwenden  # noqa: E402

DS = Durchsicht('messen.flaechen', 19_5_13)
# a) Stufe 3 mit dem Gedanken von Stufe 2 (m · cm in dm², Zerlegen in zwei Einheiten, Räume addieren, Rahmen) → Stufe 2
for _lz, _t in [('rechteck', 'Ein Rechteck ist 3 m lang und 30 cm breit. Wie groß ist der Flächeninhalt in dm²?'),
        ('rechteck', 'Ein Rechteck ist 6 m lang und 90 cm breit. Wie groß ist der Flächeninhalt in dm²?'),
        ('rechteck', 'Ein Rechteck ist 2 m lang und 90 cm breit. Wie groß ist der Flächeninhalt in dm²?'),
        ('einheiten', 'Zerlege: 3 569 mm² = □ cm² □ mm²'),
        ('einheiten', 'Ein Bauernhof hat 12 ha Ackerland. Wie viele m² sind das?'),
        ('einheiten', 'Zerlege: 1 621 m² = □ a □ m²'),
        ('einheiten', 'Zerlege: 2 301 cm² = □ dm² □ cm²'),
        ('zerlegen', 'Eine Wohnung besteht aus einem Raum mit 3 m × 5 m, einem Raum mit 6 m × 6 m, einem Raum mit 5 m × 2 m und einem Raum mit 7 m × 5 m. Wie groß ist die Wohnfläche?'),
        ('zerlegen', 'Eine Wohnung besteht aus einem Raum mit 3 m × 6 m, einem Raum mit 5 m × 2 m, einem Raum mit 5 m × 6 m und einem Raum mit 8 m × 3 m. Wie groß ist die Wohnfläche?'),
        ('zerlegen', 'Ein großes Quadrat hat 8 cm Seitenlänge. Darin liegt ein kleines Quadrat mit 3 cm Seitenlänge. Wie groß ist die Fläche zwischen den beiden Quadraten?')]:
    DS.stufe(_lz, _t, 2, enthaelt=lambda x: x['s'] == 3)
# c) Lösung 30,25 cm² verlangt Kommazahl mal Kommazahl (5,5 · 5,5) – das ist Kl. 6. Gleicher Gedanke mit ganzen Zahlen:
DS.ersetze('rechteck', 'Ein Rechteck ist 8 cm lang und 3 cm breit. Ein Quadrat hat denselben Umfang. Wie groß ist der Flächeninhalt des Quadrats?',
           DS.Z('Ein Rechteck ist 9 cm lang und 5 cm breit. Ein Quadrat hat denselben Umfang. Wie groß ist der Flächeninhalt des Quadrats?',
                49, '((2 * 9 + 2 * 5) / 4) ** 2',
                'Umfang: 2 · 9 cm + 2 · 5 cm = 28 cm. Quadratseite: 28 cm : 4 = 7 cm. Fläche: 7 cm · 7 cm = 49 cm².',
                'Berechne den Umfang und teile ihn auf 4 gleiche Seiten.', einheit='cm²'))
durchsicht_anwenden(DATEI, DS)
# ---- DURCHSICHT ENDE ----
# ---- STUFEN (Zwanzigste Runde, Zweig stufen-kl5, siehe _stufen_kl5.py und _st5_messen_flaechen.py) ----
from _stufen_kl5 import stufen_anwenden  # noqa: E402
stufen_anwenden(DATEI, 'messen.flaechen')
# ---- STUFEN ENDE ----

if __name__ == '__main__':
    schreibe(DATEI)
