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

# Verständliche Fassung (Siebte Runde, 15.11.): Alltagssituation zuerst (einstieg), jedes neue Wort erklärt (woerter),
# Beispiel in kleinen Schritten, Merksatz am Ende (regel). Durchgehende Situationen: Zimmer (Teppich, Fußleiste) und Garten (Zaun, Rasen).
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _klar_kl5.py) – die Aufgaben bleiben wörtlich gleich.
from _klar_kl5 import klar  # noqa: E402

KLAR = {
 'einheitsquadrate': {
  'einstieg': 'Du willst den Boden eines kleinen Spielhauses mit quadratischen Fliesen auslegen. Wie groß der Boden ist, sagst du am besten mit der Zahl der Fliesen, die hineinpassen. In Mathe nimmt man dafür kleine Quadrate mit 1 cm, 1 m oder 1 km Seitenlänge. Wie viele davon in eine Fläche passen, heißt ⟦Flächeninhalt⟧.',
  'woerter': [['Flächeninhalt A', 'wie viele Einheitsquadrate in eine Fläche passen; abgekürzt A'], ['Einheitsquadrat', 'ein Quadrat mit der Seitenlänge 1, zum Beispiel 1 cm'],
              ['cm²', 'Quadratzentimeter: die Fläche eines Quadrats mit 1 cm Seitenlänge'], ['Reihe', 'eine Zeile von Quadraten nebeneinander']],
  'schritte': ['Ein Rechteck ist 5 cm lang und 3 cm breit. Lege in Gedanken Quadrate mit 1 cm Seitenlänge hinein.',
               'In eine Reihe passen 5 Quadrate, denn das Rechteck ist 5 cm lang.',
               'Es gibt 3 Reihen, denn es ist 3 cm breit. Zusammen sind das 3 · 5 = 15 Quadrate.',
               'Jedes Quadrat ist 1 cm² groß. Also ist ⟦A = 15 cm²⟧.'],
  'regel': 'So bestimmst du den ⟦Flächeninhalt⟧: Zähle, wie viele ⟦Einheitsquadrate⟧ hineinpassen. Beim Rechteck rechnest du ⟦Reihen mal Quadrate pro Reihe⟧.',
  'fehler': '5 + 3 = 8 cm² ist falsch: Das ist nur die halbe Länge des Randes. Beim Flächeninhalt zählst du ⟦Quadrate⟧ – Reihen ⟦mal⟧ Quadrate pro Reihe, wie Fliesen auf dem Boden.'},
 'rechteck': {
  'einstieg': 'Ein Zimmer bekommt einen neuen Teppichboden und eine Fußleiste am Rand entlang. Für den Teppich brauchst du die Fläche des Bodens, für die Leiste die Länge des ganzen Randes. Die Fläche heißt Flächeninhalt, die Länge des Randes heißt ⟦Umfang⟧.',
  'woerter': [['Umfang u', 'die Länge des ganzen Randes einer Figur'], ['a, b', 'Länge und Breite des Rechtecks'], ['m²', 'Quadratmeter: die Fläche eines Quadrats mit 1 m Seitenlänge'],
              ['Formel', 'eine Rechenvorschrift mit Buchstaben'], ['A = a · b', 'Formel: Flächeninhalt = Länge mal Breite'], ['Fußleiste', 'eine Leiste unten an der Wand, am Rand des Bodens entlang']],
  'schritte': ['Das Zimmer ist ein Rechteck mit a = 8 m und b = 5 m. Zuerst der Flächeninhalt für den Teppich.',
               'A = a · b = 8 m · 5 m = 40 m². Der Teppich muss ⟦40 m²⟧ groß sein.',
               'Jetzt der Umfang für die Leiste: Der Rand hat zwei lange Seiten mit 8 m und zwei kurze mit 5 m.',
               'u = 2 · 8 m + 2 · 5 m = 16 m + 10 m = ⟦26 m⟧.'],
  'regel': 'So rechnest du beim Rechteck: ⟦A = a · b⟧ und ⟦u = 2 · a + 2 · b⟧. Beim Quadrat mit der Seite a: ⟦A = a · a⟧ und ⟦u = 4 · a⟧. Vorher beide Seiten in ⟦dieselbe Längeneinheit⟧ bringen.',
  'fehler': 'Umfang und Fläche verwechseln ist der häufigste Fehler. Der Umfang ist eine ⟦Länge⟧ (m) – die Fußleiste kaufst du in Metern. Der Flächeninhalt ist eine ⟦Fläche⟧ (m²) – den Teppich kaufst du in Quadratmetern.'},
 'einheiten': {
  'einstieg': 'Ein Quadrat mit 1 m Seitenlänge kannst du mit kleinen Quadraten von 1 dm Seitenlänge auslegen. In eine Reihe passen 10 kleine, und es gibt 10 Reihen – zusammen 100 kleine Quadrate. Darum ist bei allen ⟦Flächeneinheiten⟧ die Umrechnungszahl 100.',
  'woerter': [['Flächeneinheit', 'eine Einheit für Flächen, zum Beispiel cm² oder m²'], ['dm², mm²', 'Quadratdezimeter, Quadratmillimeter'],
              ['a', 'Ar: 100 m², etwa ein großer Garten'], ['ha', 'Hektar: 100 a = 10 000 m², etwa anderthalb Fußballfelder'], ['km²', 'Quadratkilometer: 100 ha'],
              ['Umrechnungszahl', 'die Zahl, mit der man beim Umrechnen malnimmt oder teilt']],
  'schritte': ['Rechne 7 m² in dm² um. Ein Quadrat mit 1 m Seite ist 10 dm lang und 10 dm breit.',
               'Darin liegen 10 Reihen mit je 10 kleinen Quadraten: 10 · 10 = 100. Also ist 1 m² = 100 dm².',
               '7 m² sind 7-mal so viel: 7 · 100 = 700. Also ist ⟦7 m² = 700 dm²⟧.'],
  'regel': 'So rechnest du Flächen um: km² → ha → a → m² → dm² → cm² → mm², bei jedem Schritt ist die ⟦Umrechnungszahl 100⟧. In die ⟦kleinere⟧ Einheit: mal 100. In die ⟦größere⟧: durch 100.'},
 'kommaschreibweise': {
  'einstieg': 'Beim Geld weißt du: 4,07 € sind 4 € und 7 ct. Für die Cent gibt es zwei Stellen hinter dem Komma, weil 1 € = 100 ct sind. Bei Flächen ist es genauso, denn auch hier ist die Umrechnungszahl 100. So schreibst du Flächen in ⟦Kommaschreibweise⟧.',
  'woerter': [['Kommaschreibweise', 'eine Fläche mit Komma in einer Einheit: 6,05 m² statt 6 m² 5 dm²'],
              ['zwei Stellen', 'bei Flächen bekommt jede kleinere Einheit zwei Ziffern hinter dem Komma']],
  'schritte': ['Schreibe 6 m² 5 dm² in m². Vor das Komma kommen die 6 m².',
               'Die dm² bekommen zwei Stellen hinter dem Komma, weil 1 m² = 100 dm² sind.',
               '5 dm² schreibst du mit zwei Stellen als 05.',
               'Ergebnis: ⟦6 m² 5 dm² = 6,05 m²⟧.'],
  'regel': 'So schreibst du Flächen mit Komma: Vor dem Komma steht die ⟦große Einheit⟧, dahinter bekommt jede kleinere Einheit ⟦zwei Stellen⟧: 3,25 m² = 3 m² 25 dm² und 4 a 7 m² = ⟦4,07 a⟧.',
  'fehler': '6 m² 5 dm² = 6,5 m² ist falsch: 6,5 m² sind 6 m² ⟦50⟧ dm² – so wie 6,50 € etwas anderes sind als 6,05 €. Bei Flächen braucht jede Einheit zwei Stellen: 6,05 m².'},
 'zerlegen': {
  'einstieg': 'In einem Zimmer fehlt eine Ecke, weil dort ein Schrank eingebaut ist. Der Boden hat dann die Form eines L. Für so eine Fläche gibt es keine eigene Formel. Du teilst sie in Rechtecke auf oder denkst dir das fehlende Stück dazu. Das heißt ⟦zerlegen⟧ oder ⟦ergänzen⟧.',
  'woerter': [['zusammengesetzte Fläche', 'eine Fläche, die aus mehreren Rechtecken besteht, zum Beispiel eine L-Form'],
              ['zerlegen', 'die Fläche in Rechtecke aufteilen und deren Flächen addieren'], ['ergänzen', 'das fehlende Stück dazudenken: großes Rechteck minus fehlendes Stück'],
              ['8 m × 6 m', 'gelesen „8 m mal 6 m“: ein Rechteck, 8 m lang und 6 m breit']],
  'schritte': ['Die L-Form im Bild passt in ein großes Rechteck von 8 m × 6 m. Oben rechts fehlt ein Stück von 3 m × 2 m.',
               'Ergänzen: Das große Rechteck hat 8 · 6 = 48 m².',
               'Das fehlende Stück hat 3 · 2 = 6 m². Ziehe es ab: 48 − 6 = ⟦42 m²⟧.'],
  'regel': 'So berechnest du eine ⟦zusammengesetzte Fläche⟧: ⟦Zerlegen⟧ – in Rechtecke aufteilen und die Flächen addieren. Oder ⟦ergänzen⟧ – zu einem großen Rechteck vervollständigen und das fehlende Stück abziehen. Beide Wege ergeben dasselbe.'},
 'sachaufgaben': {
  'einstieg': 'Ein Garten soll einen Zaun bekommen und neuen Rasen. Für den Zaun gehst du am Rand entlang – du brauchst eine Länge. Für den Rasen bedeckst du den ganzen Boden – du brauchst eine Fläche. Bei jeder ⟦Sachaufgabe⟧ zu Flächen klärst du deshalb zuerst: Rand oder Fläche?',
  'woerter': [['Sachaufgabe', 'eine Rechenaufgabe, die als kleine Geschichte erzählt wird'], ['ringsherum', 'einmal ganz um den Rand herum']],
  'schritte': ['Ein Garten ist 12 m lang und 7 m breit und bekommt einen Zaun ringsherum. Ein Zaun läuft am Rand entlang, gesucht ist also der Umfang.',
               'Der Rand hat zwei Seiten mit 12 m und zwei Seiten mit 7 m.',
               'u = 2 · 12 m + 2 · 7 m = 24 m + 14 m = ⟦38 m⟧. So viel Zaun brauchst du.'],
  'regel': 'So löst du Flächen-Sachaufgaben: Frage zuerst, ob eine ⟦Länge⟧ gesucht ist (Zaun, Rand, Leiste → ⟦Umfang⟧) oder eine ⟦Fläche⟧ (Rasen, Boden, Farbe → ⟦Flächeninhalt⟧). Dann rechnest du in ⟦einer⟧ Einheit.'},
 'verstehen': {
  'einstieg': 'Zwei Gärten haben beide einen Zaun von 16 m Länge. Ist dann in beiden gleich viel Platz zum Spielen? Nicht unbedingt! Ein langer, schmaler Garten kann bei gleich langem Zaun kleiner sein als ein quadratischer. Solche Behauptungen über ⟦Fläche und Umfang⟧ prüfst du mit Beispielen.',
  'woerter': [['Behauptung', 'eine Aussage, die richtig oder falsch sein kann'], ['verdoppeln', 'mal 2 nehmen'], ['Gegenbeispiel', 'ein Fall, der eine Behauptung widerlegt']],
  'schritte': ['Garten 1 ist ein Rechteck mit 6 m × 2 m. Umfang: 2 · 6 m + 2 · 2 m = 16 m. Fläche: 6 · 2 = 12 m².',
               'Garten 2 ist ein Quadrat mit 4 m × 4 m. Umfang: 4 · 4 m = 16 m. Fläche: 4 · 4 = 16 m².',
               'Beide haben 16 m Zaun, aber ⟦verschiedene Flächen⟧: 12 m² und 16 m².'],
  'regel': 'Merke: ⟦Gleicher Umfang⟧ heißt nicht gleiche Fläche – und umgekehrt. Verdoppelst du ⟦Länge und Breite⟧, wird die Fläche ⟦viermal⟧ so groß. So prüfst du Behauptungen: mit einem ⟦Zahlenbeispiel⟧ nachrechnen.'},
}
klar(DATEI, KLAR)


if __name__ == '__main__':
    schreibe(DATEI)
