#!/usr/bin/env python3
"""Thema sonder.optimierung – Lineare Optimierung (IB MYP 4, etwa Klasse 9)."""
import math
import sys
from math import gcd
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403
from _rsib2 import PLAN2, art3  # noqa: E402

start(6604)


def lin(a, b, vx='x', vy='y'):
    t = ''
    if a: t = ('' if a == 1 else '−' if a == -1 else dz(a)) + vx
    if b:
        bb = '' if abs(b) == 1 else dz(abs(b))
        t = (t + (' + ' if b > 0 else ' − ') + bb + vy) if t else (('−' if b < 0 else '') + bb + vy)
    return t or '0'


def kuerze(a, b, c):
    g = gcd(gcd(a, b), c)
    return a // g, b // g, c // g


def vieleck():
    """Zulässiger Bereich mit Ecken O(0|0), A(xa|0), P(px|py), B(0|yb); zwei Bedingungen plus x, y ≥ 0."""
    for _ in range(500):
        xa, yb = R.randint(4, 12), R.randint(4, 12)
        px, py = R.randint(1, xa - 1), R.randint(1, yb - 1)
        if px / xa + py / yb <= 1.15: continue
        g1 = kuerze(py, xa - px, py * xa)          # durch A und P
        g2 = kuerze(yb - py, px, px * yb)          # durch B und P
        if g1[0] <= 0 or g1[1] <= 0 or g2[0] <= 0 or g2[1] <= 0: continue
        if max(g1 + g2) > 60: continue
        return {'A': (xa, 0), 'P': (px, py), 'B': (0, yb), 'O': (0, 0), 'g1': g1, 'g2': g2}
    return None


def bild_v(v, punkte=True, zusatz=None):
    (a1, b1, c1), (a2, b2, c2) = v['g1'], v['g2']
    xm = max(v['A'][0], c2 / a2) + 1
    ym = max(v['B'][1], c1 / b1) + 1
    gr = [{'art': 'linear', 'm': -a1 / b1, 't': c1 / b1, 'bereich': [0, c1 / a1], 'name': 'I'},
          {'art': 'linear', 'm': -a2 / b2, 't': c2 / b2, 'bereich': [0, c2 / a2], 'name': 'II'}]
    for g in gr:
        g['m'], g['t'] = round(g['m'], 6), round(g['t'], 6)
        g['bereich'] = [0, round(g['bereich'][1], 6)]
        g['name_x'] = round(g['bereich'][1] * (0.8 if g['name'] == 'I' else 0.6), 3)
    b = {'typ': 'koordinaten', 'x': [0, int(xm) + 1], 'y': [0, int(ym) + 1], 'graphen': gr}
    if punkte:
        b['punkte'] = [{'x': v[k][0], 'y': v[k][1], 'name': k} for k in ('O', 'A', 'P', 'B')]
    if zusatz: b['punkte'] = b.get('punkte', []) + zusatz
    if xm > 14 or ym > 14: b['schritt_x'] = b['schritt_y'] = 2
    return b


def system_txt(v):
    (a1, b1, c1), (a2, b2, c2) = v['g1'], v['g2']
    return f'I: {lin(a1, b1)} ≤ {dz(c1)}, II: {lin(a2, b2)} ≤ {dz(c2)}, x ≥ 0, y ≥ 0'


def erfuellt(v, x, y):
    (a1, b1, c1), (a2, b2, c2) = v['g1'], v['g2']
    return a1 * x + b1 * y <= c1 and a2 * x + b2 * y <= c2 and x >= 0 and y >= 0


ETAPPEN = [
    {'lernziel': 'bereich', 'titel': 'Liegt ein Punkt im Bereich?',
     'regel': 'Eine lineare Ungleichung wie 2x + y ≤ 8 beschreibt eine ⟦Halbebene⟧: alle Punkte auf der Geraden 2x + y = 8 und auf ⟦einer⟧ Seite davon. Mehrere Ungleichungen zusammen ergeben den ⟦zulässigen Bereich⟧ (feasible region). Ein Punkt liegt darin, wenn er ⟦alle⟧ Ungleichungen erfüllt.',
     'schritte': ['Bedingungen: 2x + y ≤ 8, x + 2y ≤ 10, x ≥ 0, y ≥ 0. Prüfe Q(2 | 3).', '2 · 2 + 3 = 7 ≤ 8 ✓; 2 + 2 · 3 = 8 ≤ 10 ✓; beide ≥ 0 ✓.', '⟦Q liegt im zulässigen Bereich⟧.'],
     'probe': 'Ein Punkt außerhalb, z. B. (4 | 3): 2 · 4 + 3 = 11 > 8 ✗',
     'bild': {'typ': 'koordinaten', 'x': [0, 11], 'y': [0, 9], 'graphen': [{'art': 'linear', 'm': -2, 't': 8, 'bereich': [0, 4], 'name': 'I', 'name_x': 3.3}, {'art': 'linear', 'm': -0.5, 't': 5, 'bereich': [0, 10], 'name': 'II', 'name_x': 7}],
              'punkte': [{'x': 2, 'y': 3, 'name': 'Q'}]},
     'fehler': 'Nur die erste Ungleichung zu prüfen reicht nicht: Ein Punkt kann I erfüllen und ⟦II verletzen⟧. Zulässig heißt: ⟦alle⟧ Bedingungen gleichzeitig.'},
    {'lernziel': 'aufstellen', 'titel': 'Bedingungen aufstellen',
     'regel': 'Übersetze jede Einschränkung in eine Ungleichung: Lege fest, wofür x und y stehen (⟦Entscheidungsvariablen⟧). „Höchstens“ → ⟦≤⟧, „mindestens“ → ⟦≥⟧. Anzahlen sind nie negativ: ⟦x ≥ 0, y ≥ 0⟧. Was optimiert wird, ist die ⟦Zielfunktion⟧ (objective function), z. B. Gewinn G = 3x + 5y.',
     'schritte': ['Eine Bäckerei backt x Kuchen und y Torten. Ein Kuchen braucht 2 h, eine Torte 3 h; es gibt höchstens 30 h.', 'Zeit: ⟦2x + 3y ≤ 30⟧.', 'Gewinn 4 € pro Kuchen, 7 € pro Torte: Zielfunktion ⟦G = 4x + 7y⟧.'],
     'probe': '5 Kuchen und 6 Torten: 10 + 18 = 28 h ≤ 30 ✓',
     'fehler': '„Mindestens 4 Torten“ als y ≤ 4 zu schreiben ist falsch: „mindestens“ heißt ⟦y ≥ 4⟧ – 4 oder mehr.'},
    {'lernziel': 'ecken', 'titel': 'Eckpunkte berechnen',
     'regel': 'Die ⟦Eckpunkte⟧ (vertices) des Bereichs liegen dort, wo sich zwei Randgeraden schneiden. Man berechnet sie mit einem ⟦linearen Gleichungssystem⟧ (Gleichheitszeichen statt ≤). Schnittpunkte mit den Achsen: x = 0 bzw. y = 0 einsetzen.',
     'schritte': ['Ränder 2x + y = 8 und x + 2y = 10.', 'Erste Gleichung mal 2: 4x + 2y = 16. Minus zweite: 3x = 6, also x = 2.', 'y = 8 − 2 · 2 = 4. Eckpunkt ⟦(2 | 4)⟧.'],
     'probe': '2 + 2 · 4 = 10 ✓',
     'fehler': 'Den Schnittpunkt einfach im Bild „ungefähr“ abzulesen ist riskant: (2 | 4) und (2,2 | 3,8) sehen fast gleich aus. ⟦Rechne⟧ die Ecken aus.'},
    {'lernziel': 'optimum', 'titel': 'Das Optimum finden',
     'regel': 'Das Maximum (oder Minimum) der Zielfunktion liegt immer an einer ⟦Ecke⟧ des zulässigen Bereichs (⟦Eckenprinzip⟧). Also: Zielfunktion ⟦an allen Ecken ausrechnen⟧ und den größten (kleinsten) Wert nehmen.',
     'schritte': ['Ecken (0 | 0), (4 | 0), (2 | 4), (0 | 5). Zielfunktion G = 3x + 2y.', 'G: 0; 12; 3 · 2 + 2 · 4 = 14; 10.', 'Maximum ⟦G = 14 bei (2 | 4)⟧.'],
     'probe': 'Kein Eckpunkt liefert mehr als 14 ✓',
     'fehler': 'Den Punkt mit dem ⟦größten x⟧ zu nehmen ist falsch: Bei G = 3x + 2y liefert (4 | 0) nur 12, die Ecke (2 | 4) aber 14. ⟦Alle Ecken einsetzen⟧.'},
    {'lernziel': 'sach', 'titel': 'Optimierung im Sachzusammenhang',
     'regel': 'Vorgehen: ⟦1.⟧ Variablen festlegen, ⟦2.⟧ Bedingungen und Zielfunktion aufstellen, ⟦3.⟧ Bereich zeichnen und Ecken bestimmen, ⟦4.⟧ Zielfunktion an den Ecken vergleichen, ⟦5.⟧ Antwort im Sachzusammenhang (z. B. „6 Kuchen und 4 Torten“).',
     'schritte': ['Gewinn G = 4x + 7y, Ecken (0 | 0), (15 | 0), (6 | 6), (0 | 8).', 'G: 0; 60; 24 + 42 = 66; 56.', 'Größter Gewinn ⟦66 € mit 6 Kuchen und 6 Torten⟧.'],
     'probe': '66 > 60 > 56 ✓',
     'fehler': 'Nur „66“ zu antworten genügt nicht: Gefragt ist auch, ⟦wie viele⟧ von jedem Produkt man herstellen soll.'},
]


def g_bereich(s):
    v = vieleck()
    if not v: return None
    art = R.choice({1: ['pruef', 'pruef'], 2: ['pruef', 'welche', 'zaehl_rand'], 3: ['welche', 'verletzt', 'pruef']}[s])
    if art in ('pruef', 'zaehl_rand'):
        x, y = R.randint(0, v['A'][0]), R.randint(0, v['B'][1])
        ok = erfuellt(v, x, y)
        (a1, b1, c1), (a2, b2, c2) = v['g1'], v['g2']
        return mit_grafik(ja_nein(f'Bedingungen {system_txt(v)}. Liegt der Punkt Q({x} | {y}) im zulässigen Bereich?', ok,
                                  f'I: {dz(a1 * x + b1 * y)} {"≤" if a1 * x + b1 * y <= c1 else ">"} {dz(c1)}; II: {dz(a2 * x + b2 * y)} {"≤" if a2 * x + b2 * y <= c2 else ">"} {dz(c2)}. '
                                  + ('Alle erfüllt.' if ok else 'Nicht alle erfüllt.'), 'Setze x und y in jede Ungleichung ein.'),
                          bild_v(v, punkte=False, zusatz=[{'x': x, 'y': y, 'name': 'Q'}]) if s > 1 else None)
    if art == 'welche':
        kand = [(x, y) for x in range(0, v['A'][0] + 2) for y in range(0, v['B'][1] + 2)]
        innen = [p for p in kand if erfuellt(v, *p) and p not in ((0, 0),)]
        aussen = [p for p in kand if not erfuellt(v, *p)]
        if len(innen) < 1 or len(aussen) < 3: return None
        r = R.choice(innen)
        fs = R.sample(aussen, 3)
        return auswahl(f'Bedingungen {system_txt(v)}. Welcher Punkt liegt im zulässigen Bereich?', f'({r[0]} | {r[1]})', [f'({x} | {y})' for x, y in fs],
                       f'Nur ({r[0]} | {r[1]}) erfüllt I und II; die anderen verletzen mindestens eine Bedingung.', 'Setze jeden Punkt in beide Ungleichungen ein.')
    (a1, b1, c1), (a2, b2, c2) = v['g1'], v['g2']
    kand = [(x, y) for x in range(0, 15) for y in range(0, 15) if (a1 * x + b1 * y <= c1) != (a2 * x + b2 * y <= c2)]
    if not kand: return None
    x, y = R.choice(kand)
    welche = 'I' if a1 * x + b1 * y > c1 else 'II'
    return auswahl(f'Bedingungen {system_txt(v)}. Der Punkt ({x} | {y}) liegt nicht im Bereich. Welche Bedingung verletzt er?', f'Bedingung {welche}',
                   ['Bedingung I', 'Bedingung II', 'x ≥ 0', 'keine – er liegt doch im Bereich'],
                   f'I: {dz(a1 * x + b1 * y)} {"≤" if a1 * x + b1 * y <= c1 else ">"} {dz(c1)}; II: {dz(a2 * x + b2 * y)} {"≤" if a2 * x + b2 * y <= c2 else ">"} {dz(c2)}. Verletzt: {welche}.',
                   'Prüfe beide Ungleichungen einzeln.')


SACH = [  # (x-Ding, y-Ding, Ressource, Einheit, Firma)
    ('Tische', 'Stühle', 'Holz', 'm²', 'Eine Schreinerei'),
    ('Kuchen', 'Torten', 'Backzeit', 'h', 'Eine Bäckerei'),
    ('T-Shirts', 'Pullover', 'Nähzeit', 'min', 'Eine Näherei'),
    ('Rucksäcke', 'Taschen', 'Stoff', 'm²', 'Eine Werkstatt'),
]


def g_aufstellen(s):
    X, Y, res, ein, firma = R.choice(SACH)
    a, b, c = R.randint(2, 6), R.randint(2, 6), R.randint(20, 60)
    art = R.choice({1: ['hoechstens', 'mindestens'], 2: ['hoechstens', 'ziel', 'mindestens', 'summe'], 3: ['doppelt', 'ziel', 'hoechstens', 'kombi']}[s])
    vor = f'{firma} stellt x {X} und y {Y} her.'
    if art == 'hoechstens':
        r = f'{lin(a, b)} ≤ {c}'
        return auswahl(vor + f' Je Stück braucht man {a} {ein} {res} ({X}) bzw. {b} {ein} {res} ({Y}). Es stehen höchstens {c} {ein} zur Verfügung. Welche Ungleichung passt?',
                       r, [f'{lin(a, b)} ≥ {c}', f'{lin(b, a)} ≤ {c}', f'x + y ≤ {c}'],
                       f'{res}: {a} {ein} je Stück x, {b} {ein} je Stück y, zusammen höchstens {c}: {r}.', '„Höchstens“ bedeutet ≤. Welche Zahl gehört zu x, welche zu y?')
    if art == 'mindestens':
        k = R.randint(2, 10)
        wer = R.choice([('x', X), ('y', Y)])
        r = f'{wer[0]} ≥ {k}'
        return auswahl(vor + f' Es müssen mindestens {k} {wer[1]} hergestellt werden. Welche Bedingung passt?', r, [f'{wer[0]} ≤ {k}', f'{wer[0]} > {k + 1}', f'x + y ≥ {k}'],
                       f'„Mindestens {k}“ heißt {k} oder mehr: {r}.', 'Mindestens → ≥, höchstens → ≤.')
    if art == 'summe':
        k = R.randint(10, 40)
        r = f'x + y ≤ {k}'
        return auswahl(vor + f' Insgesamt passen höchstens {k} Stück ins Lager. Welche Bedingung passt?', r, [f'x + y ≥ {k}', f'x ≤ {k} und y ≥ {k}', f'x · y ≤ {k}'],
                       f'Alle Stücke zusammen: x + y; höchstens {k}: {r}.', 'Wie viele Stücke sind es zusammen?')
    if art == 'ziel':
        g1, g2 = R.randint(3, 25), R.randint(3, 25)
        if g1 == g2: return None
        r = f'G = {lin(g1, g2)}'
        return auswahl(vor + f' Der Gewinn beträgt {g1} € pro Stück bei den {DAT[X]} und {g2} € pro Stück bei den {DAT[Y]}. Wie lautet die Zielfunktion?', r,
                       [f'G = {lin(g2, g1)}', f'G = {g1 + g2}x', f'G = {lin(g1, g2)} − {c}'],
                       f'Gewinn aus x {X}: {g1}x; aus y {Y}: {g2}y. Zusammen {r}.', 'Gewinn je Stück mal Anzahl, für beide Produkte addiert.')
    if art == 'doppelt':
        r = 'y ≥ 2x'
        return auswahl(vor + f' Es sollen mindestens doppelt so viele {Y} wie {X} hergestellt werden. Welche Bedingung passt?', r, ['x ≥ 2y', 'y ≤ 2x', 'y + 2 ≥ x'],
                       f'Die Anzahl der {Y} (y) soll mindestens das Doppelte von x sein: y ≥ 2x. Probe: x = 3, y = 7 erfüllt das (7 ≥ 6).',
                       'Teste mit Zahlen: x = 3 – wie viele y muss es mindestens geben?')
    k1, k2 = R.randint(2, 5), R.randint(2, 5)
    zeit = R.randint(30, 90)
    r = f'{lin(k1, k2)} ≤ {zeit} und x ≥ 0, y ≥ 0'
    return auswahl(vor + f' {EIN1[X][0].upper() + EIN1[X][1:]} braucht {k1} h, {EIN1[Y]} {k2} h; es gibt {zeit} Arbeitsstunden. Welches System beschreibt alle Bedingungen?', r,
                   [f'{lin(k1, k2)} ≤ {zeit}', f'{lin(k1, k2)} ≥ {zeit} und x ≥ 0, y ≥ 0', f'{lin(k2, k1)} ≤ {zeit} und x ≤ 0, y ≤ 0'],
                   'Zeitbedingung plus Nichtnegativität (Anzahlen können nicht negativ sein).', 'Vergiss die selbstverständlichen Bedingungen nicht.')


def g_ecken(s):
    v = vieleck()
    if not v: return None
    (a1, b1, c1), (a2, b2, c2) = v['g1'], v['g2']
    px, py = v['P']
    art = R.choice({1: ['achse_x', 'achse_y'], 2: ['schnitt', 'achse_x', 'schnitt'], 3: ['schnitt', 'schnitt', 'anzahl_ecken']}[s])
    if art == 'achse_x':
        xa = v['A'][0]
        return luecken(f'Wo schneidet die Randgerade {lin(a1, b1)} = {dz(c1)} die x-Achse?', '(□ | □)', 'x- und y-Koordinate', [xa, 0],
                       f'Auf der x-Achse ist y = 0: {dz(a1)}x = {dz(c1)} ⇒ x = {xa}. Punkt ({xa} | 0).', 'Setze y = 0 ein.', c=[f'{c1} / {a1}', '0'])
    if art == 'achse_y':
        yb = v['B'][1]
        return luecken(f'Wo schneidet die Randgerade {lin(a2, b2)} = {dz(c2)} die y-Achse?', '(□ | □)', 'x- und y-Koordinate', [0, yb],
                       f'Auf der y-Achse ist x = 0: {dz(b2)}y = {dz(c2)} ⇒ y = {yb}. Punkt (0 | {yb}).', 'Setze x = 0 ein.', c=['0', f'{c2} / {b2}'])
    if art == 'schnitt':
        return mit_grafik(luecken(f'Berechne den Eckpunkt P, in dem sich {lin(a1, b1)} = {dz(c1)} und {lin(a2, b2)} = {dz(c2)} schneiden.', 'P(□ | □)', 'Koordinaten des Punktes',
                                  [px, py], f'Gleichungssystem lösen (z. B. Additionsverfahren): x = {px}, y = {py}. Probe: {dz(a1 * px + b1 * py)} = {dz(c1)} ✓, {dz(a2 * px + b2 * py)} = {dz(c2)} ✓.',
                                  'Löse das Gleichungssystem, z. B. mit dem Additions- oder Einsetzungsverfahren.',
                                  c=[f'({c1} * {b2} - {c2} * {b1}) / ({a1} * {b2} - {a2} * {b1})', f'({a1} * {c2} - {a2} * {c1}) / ({a1} * {b2} - {a2} * {b1})']),
                          bild_v(v, punkte=False, zusatz=[{'x': px, 'y': py, 'name': 'P'}]) if s == 2 else None)
    return mit_grafik(zahl(f'Bedingungen {system_txt(v)}. Wie viele Eckpunkte hat der zulässige Bereich?',
                           f'Ecken: O(0 | 0), ({v["A"][0]} | 0), ({px} | {py}), (0 | {v["B"][1]}) – das sind 4.', 'Zähle die Knickstellen am Rand des Bereichs (Achsen mitzählen).',
                           4, '4'), bild_v(v, punkte=False))


def g_optimum(s):
    v = vieleck()
    if not v: return None
    ecken = [v['O'], v['A'], v['P'], v['B']]
    for _ in range(50):
        k1, k2 = R.randint(1, 9), R.randint(1, 9)
        werte = [k1 * x + k2 * y for x, y in ecken]
        if sorted(werte)[-1] != sorted(werte)[-2]: break
    else:
        return None
    imax = max(range(4), key=lambda i: werte[i])
    et = ', '.join(f'({x} | {y})' for x, y in ecken)
    wt = '; '.join(f'({x} | {y}): {dz(w)}' for (x, y), w in zip(ecken, werte))
    art = R.choice({1: ['wert_ecke', 'max'], 2: ['max', 'max', 'wo'], 3: ['wo', 'min_ohne0', 'max_bild']}[s])
    if art == 'wert_ecke':
        i = R.randint(1, 3)
        x, y = ecken[i]
        return zahl(f'Zielfunktion Z = {lin(k1, k2)}. Berechne Z im Eckpunkt ({x} | {y}).', f'Z = {k1} · {x} + {k2} · {y} = {dz(werte[i])}.',
                    'Setze x und y in die Zielfunktion ein.', werte[i], f'{k1} * {x} + {k2} * {y}')
    if art in ('max', 'max_bild'):
        a = zahl(f'Der zulässige Bereich hat die Ecken {et}. Wie groß ist das Maximum von Z = {lin(k1, k2)}?', f'{wt}. Maximum: {dz(werte[imax])}.',
                 'Setze alle Ecken ein und nimm den größten Wert.', werte[imax], f'max({", ".join(f"{k1} * {x} + {k2} * {y}" for x, y in ecken)})')
        return mit_grafik(a, bild_v(v)) if art == 'max_bild' else a
    if art == 'wo':
        x, y = ecken[imax]
        return luecken(f'Der zulässige Bereich hat die Ecken {et}. In welchem Eckpunkt wird Z = {lin(k1, k2)} maximal?', '(□ | □)', 'Koordinaten der Ecke', [x, y],
                       f'{wt}. Am größten bei ({x} | {y}).', 'Alle Ecken in Z einsetzen und vergleichen.', c=[str(x), str(y)])
    # Minimum ohne Nullpunkt (z. B. Kosten, wenn mindestens etwas produziert wird)
    w3 = werte[1:]
    if sorted(w3)[0] == sorted(w3)[1]: return None
    i = 1 + min(range(3), key=lambda j: w3[j])
    return zahl(f'Die Ecken des Bereichs (ohne den Nullpunkt) sind {", ".join(f"({x} | {y})" for x, y in ecken[1:])}. Wie groß ist das Minimum von K = {lin(k1, k2)} an diesen Ecken?',
                f'{"; ".join(f"({x} | {y}): {dz(w)}" for (x, y), w in zip(ecken[1:], w3))}. Minimum: {dz(werte[i])}.', 'Auch das Minimum liegt an einer Ecke.',
                werte[i], f'min({", ".join(f"{k1} * {x} + {k2} * {y}" for x, y in ecken[1:])})')


def g_sach(s):
    v = vieleck()
    if not v: return None
    X, Y, res, ein, firma = R.choice(SACH)
    ecken = [v['O'], v['A'], v['P'], v['B']]
    for _ in range(50):
        k1, k2 = R.randint(2, 15), R.randint(2, 15)
        werte = [k1 * x + k2 * y for x, y in ecken]
        if sorted(werte)[-1] != sorted(werte)[-2]: break
    else:
        return None
    imax = max(range(4), key=lambda i: werte[i])
    (a1, b1, c1), (a2, b2, c2) = v['g1'], v['g2']
    vor = (f'{firma} stellt x {X} und y {Y} her. Bedingungen: {system_txt(v)}. Gewinn: G = {lin(k1, k2)} (in €). '
           f'Die Ecken des Bereichs sind (0 | 0), ({v["A"][0]} | 0), ({v["P"][0]} | {v["P"][1]}), (0 | {v["B"][1]}).')
    art = R.choice({1: ['gewinn'], 2: ['gewinn', 'plan'], 3: ['plan', 'vergleich', 'gewinn']}[s])
    wt = '; '.join(f'({x} | {y}): {dz(w)} €' for (x, y), w in zip(ecken, werte))
    if art == 'gewinn':
        return zahl(vor + ' Wie hoch ist der größtmögliche Gewinn?', f'{wt}. Größter Gewinn: {dz(werte[imax])} €.', 'Gewinn an allen Ecken berechnen und vergleichen.',
                    werte[imax], f'max({", ".join(f"{k1} * {x} + {k2} * {y}" for x, y in ecken)})', einheit='€')
    if art == 'plan':
        x, y = ecken[imax]
        return luecken(vor + f' Wie viele {X} und {Y} sollen hergestellt werden, damit der Gewinn am größten ist?', f'□ {X} und □ {Y}', 'zwei ganze Zahlen', [x, y],
                       f'{wt}. Am besten: {x} {X} und {y} {Y} ({dz(werte[imax])} €).', 'Erst den Gewinn an allen Ecken berechnen, dann die Ecke als Produktionsplan lesen.',
                       c=[str(x), str(y)])
    x, y = v['P']
    if imax == 2: return None
    xi, yi = ecken[imax]
    return zahl(vor + f' Ein Mitarbeiter schlägt vor, {x} {X} und {y} {Y} herzustellen. Um wie viel € ist der beste Plan besser?',
                f'Vorschlag: {k1} · {x} + {k2} · {y} = {dz(werte[2])} €. Bester Plan ({xi} | {yi}): {dz(werte[imax])} €. Unterschied: {dz(werte[imax] - werte[2])} €.',
                'Bestimme den besten Plan und vergleiche.', werte[imax] - werte[2], f'{werte[imax]} - ({k1} * {x} + {k2} * {y})', einheit='€')


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-2) ----------
# Prüfungsvorbilder: IB MYP Extended („Systems of inequalities“, lineare Optimierung im Verlagsinhalt): Punkt auf dem Rand,
# Bedingungen mit Anteil/Vergleich übersetzen, dritte Bedingung x ≤ k, Ecken selbst bestimmen und optimieren, Zielfunktion parallel zu einer Randgeraden.
DAT = {'Tische': 'Tischen', 'Stühle': 'Stühlen', 'Kuchen': 'Kuchen', 'Torten': 'Torten', 'T-Shirts': 'T-Shirts', 'Pullover': 'Pullovern', 'Rucksäcke': 'Rucksäcken', 'Taschen': 'Taschen'}
EIN1 = {'Tische': 'ein Tisch', 'Stühle': 'ein Stuhl', 'Kuchen': 'ein Kuchen', 'Torten': 'eine Torte', 'T-Shirts': 'ein T-Shirt', 'Pullover': 'ein Pullover', 'Rucksäcke': 'ein Rucksack', 'Taschen': 'eine Tasche'}


def bereich3(art):
    v = vieleck()
    if not v: return None
    (a1, b1, c1), (a2, b2, c2) = v['g1'], v['g2']
    if art == 'rand':
        kand = [(x, y) for x in range(0, v['A'][0] + 1) for y in range(0, v['B'][1] + 1) if a1 * x + b1 * y == c1 and a2 * x + b2 * y < c2 and x > 0 and y > 0]
        if not kand: return None
        x, y = R.choice(kand)
        return mit_grafik(ja_nein(f'Bedingungen {system_txt(v)}. Der Punkt Q({x} | {y}) liegt genau auf der Randgeraden I. Gehört er zum zulässigen Bereich?', True,
                                  f'I: {dz(a1 * x + b1 * y)} = {dz(c1)}, und „≤“ erlaubt auch „=“. II: {dz(a2 * x + b2 * y)} < {dz(c2)}. Also zulässig.',
                                  'Bedeutet „≤“ auch „gleich“?'), bild_v(v, punkte=False, zusatz=[{'x': x, 'y': y, 'name': 'Q'}]))
    # max_y: größtes ganzzahliges y bei festem x
    x = R.randint(1, v['A'][0] - 1)
    gr1, gr2 = Fr(c1 - a1 * x, b1), Fr(c2 - a2 * x, b2)
    ymax = math.floor(min(gr1, gr2))
    if ymax < 1: return None
    return zahl(f'Bedingungen {system_txt(v)}. Eine Firma stellt x = {x} Stück der ersten Sorte her. Wie viele Stück der zweiten Sorte (y, ganzzahlig) sind dann höchstens möglich?',
                f'I: {lin(0, b1)} ≤ {dz(c1)} − {dz(a1 * x)} ⇒ y ≤ {dz(gr1) if endlich(gr1) else br(gr1)}. II: {lin(0, b2)} ≤ {dz(c2)} − {dz(a2 * x)} ⇒ y ≤ {dz(gr2) if endlich(gr2) else br(gr2)}. '
                f'Beide gelten, also y ≤ {dz(min(gr1, gr2)) if endlich(min(gr1, gr2)) else br(min(gr1, gr2))}, ganzzahlig höchstens {ymax}.',
                'Setze x ein und forme jede Ungleichung nach y um. Die strengere Grenze zählt.', ymax, f'{ymax}')


def aufst3(art):
    X, Y, res, ein, firma = R.choice(SACH)
    vor = f'{firma} stellt x {X} und y {Y} her.'
    if art == 'min_mehr':
        k = R.randint(2, 9)
        r = f'y ≥ x + {k}'
        return auswahl(vor + f' Es sollen mindestens {k} {Y} mehr als {X} hergestellt werden. Welche Bedingung passt?', r, [f'x ≥ y + {k}', f'y + {k} ≥ x', f'y ≥ {k}x'],
                       f'Die Anzahl der {Y} muss mindestens um {k} größer sein: y ≥ x + {k}. Probe: x = 3, y = {3 + k} erfüllt es genau.',
                       'Teste mit Zahlen: x = 3 – wie viele y braucht man mindestens?')
    # prozent: höchstens p % aller Stücke sind Y
    p, (zx, zy) = R.choice([(40, (2, 3)), (25, (1, 3)), (20, (1, 4)), (50, (1, 1)), (60, (3, 2))])
    r = f'{zy}y ≤ {zx}x' if (zx, zy) != (1, 1) else 'y ≤ x'
    r = r.replace('1y', 'y').replace('1x', 'x')
    return auswahl(vor + f' Höchstens {p} % aller hergestellten Stücke dürfen {Y} sein. Welche Bedingung passt?', r,
                   [f'y ≤ {p}', f'y ≤ {dz(Fr(p, 100))}x', (f'{zx}y ≤ {zy}x' if (zx, zy) != (1, 1) else 'x ≤ y').replace('1y', 'y').replace('1x', 'x')],
                   f'y ≤ {dz(Fr(p, 100))} · (x + y) ⇒ {dz(Fr(100 - p, 100))}y ≤ {dz(Fr(p, 100))}x ⇒ {r}. Probe: x = {zy}, y = {zx}: Anteil {zx} von {zx + zy} = {p} % ✓.',
                   'Alle Stücke zusammen sind x + y. Schreibe „y ist höchstens p % davon“ und vereinfache.')


def ecken3(art):
    v = vieleck()
    if not v: return None
    (a1, b1, c1), (a2, b2, c2) = v['g1'], v['g2']
    px, py = v['P']
    if art == 'vierte_ecke':
        return luecken(f'Bedingungen {system_txt(v)}. Drei Ecken des zulässigen Bereichs sind (0 | 0), ({v["A"][0]} | 0) und (0 | {v["B"][1]}). Berechne die vierte Ecke.', 'E(□ | □)',
                       'Koordinaten des Punktes', [px, py],
                       f'Die vierte Ecke ist der Schnitt der Randgeraden I und II: {lin(a1, b1)} = {dz(c1)} und {lin(a2, b2)} = {dz(c2)} ⇒ x = {px}, y = {py}.',
                       'Welche zwei Randgeraden treffen sich in der fehlenden Ecke? Löse ihr Gleichungssystem.',
                       c=[f'({c1} * {b2} - {c2} * {b1}) / ({a1} * {b2} - {a2} * {b1})', f'({a1} * {c2} - {a2} * {c1}) / ({a1} * {b2} - {a2} * {b1})'])
    if art == 'drei_bed':
        k = R.randint(1, v['A'][0] - 1)
        if k == px: return None
        # x = k schneidet die Randgerade, die bei x = k aktiv ist
        if k > px: a, b, c, nm = a1, b1, c1, 'I'
        else: a, b, c, nm = a2, b2, c2, 'II'
        y = Fr(c - a * k, b)
        if y.denominator != 1: return None
        return luecken(f'Bedingungen {system_txt(v)} und zusätzlich III: x ≤ {k}. In welchem Punkt trifft die neue Randgerade x = {k} den Rand des bisherigen Bereichs (oben)?', 'E(□ | □)',
                       'Koordinaten des Punktes', [k, int(y)],
                       f'Bei x = {k} begrenzt oben die Gerade {nm} ({lin(a, b)} = {dz(c)}): {lin(0, b)} = {dz(c)} − {dz(a * k)} ⇒ y = {dz(y)}. Neue Ecke ({k} | {dz(y)}).',
                       f'Welche der Geraden I und II liegt bei x = {k} tiefer? Dort setzt du x = {k} ein.', c=[str(k), f'({c} - {a} * {k}) / {b}'])
    # unzulaessig: Achsenschnitt einer Randgeraden, der keine Ecke ist (I trifft die y-Achse oberhalb von B, II die x-Achse rechts von A)
    yI, xII = Fr(c1, b1), Fr(c2, a2)
    opts = []
    if yI.denominator == 1 and yI > v['B'][1]: opts.append((f'(0 | {int(yI)})', 'I', f'II: {dz(b2 * yI)} > {dz(c2)}'))
    if xII.denominator == 1 and xII > v['A'][0]: opts.append((f'({int(xII)} | 0)', 'II', f'I: {dz(a1 * xII)} > {dz(c1)}'))
    if not opts: return None
    pt, wer, verl = R.choice(opts)
    return ja_nein(f'Bedingungen {system_txt(v)}. Die Randgerade {wer} schneidet eine Achse im Punkt {pt}. Ist dieser Punkt eine Ecke des zulässigen Bereichs?', False,
                   f'Er verletzt die andere Bedingung ({verl}). Eine Ecke muss alle Bedingungen erfüllen.', 'Prüfe den Punkt in der anderen Ungleichung.')


def opt3(art):
    v = vieleck()
    if not v: return None
    ecken = [v['O'], v['A'], v['P'], v['B']]
    (a1, b1, c1), (a2, b2, c2) = v['g1'], v['g2']
    et = ', '.join(f'({x} | {y})' for x, y in ecken)
    if art == 'rand_optimum':
        k1, k2 = a2, b2
        werte = [k1 * x + k2 * y for x, y in ecken]
        if werte[1] >= werte[2]: return None
        return auswahl(f'Bedingungen {system_txt(v)}, Ecken {et}. Wo wird Z = {lin(k1, k2)} maximal?',
                       f'in ({v["P"][0]} | {v["P"][1]}) und in (0 | {v["B"][1]}) gleich – und auf der ganzen Strecke dazwischen',
                       [f'nur in ({v["P"][0]} | {v["P"][1]})', f'nur in (0 | {v["B"][1]})', f'nur in ({v["A"][0]} | 0)'],
                       '; '.join(f'({x} | {y}): {dz(w)}' for (x, y), w in zip(ecken, werte)) + f'. Z hat dieselben Zahlen wie Randgerade II: Auf ihr ist Z überall {dz(c2)}.',
                       'Rechne Z an allen Ecken aus. Fällt dir etwas an der Zielfunktion auf?')
    # parameter: ab welchem a ist die Ecke A besser als P?
    k2 = R.randint(2, 9)
    xa = v['A'][0]
    px, py = v['P']
    gr = Fr(k2 * py, xa - px)
    a = math.floor(gr) + 1
    if a > 40: return None
    return zahl(f'Ecken des Bereichs: {et}. Zielfunktion Z = a · x + {k2}y. Ab welchem ganzzahligen Wert von a ist die Ecke ({xa} | 0) besser als ({px} | {py})?',
                f'Z({xa} | 0) = {xa}a, Z({px} | {py}) = {px}a + {k2 * py}. {xa}a > {px}a + {k2 * py} ⇒ {xa - px}a > {k2 * py} ⇒ a > {dz(gr) if endlich(gr) else br(gr)}. Kleinste ganze Zahl: {a}.',
                'Stelle Z an beiden Ecken mit a auf und vergleiche (Ungleichung).', a, f'{a}')


def sach3(art):
    v = vieleck()
    if not v: return None
    X, Y, res, ein, firma = R.choice(SACH)
    ecken = [v['O'], v['A'], v['P'], v['B']]
    for _ in range(50):
        k1, k2 = R.randint(2, 15), R.randint(2, 15)
        werte = [k1 * x + k2 * y for x, y in ecken]
        if sorted(werte)[-1] != sorted(werte)[-2]: break
    else:
        return None
    imax = max(range(4), key=lambda i: werte[i])
    wt = '; '.join(f'({x} | {y}): {dz(w)} €' for (x, y), w in zip(ecken, werte))
    if art == 'vollstaendig':
        x, y = ecken[imax]
        return luecken(f'{firma} stellt x {X} und y {Y} her. Bedingungen: {system_txt(v)}. Gewinn: G = {lin(k1, k2)} (in €). '
                       f'Bestimme zuerst die Ecken des Bereichs. Wie viele {X} und {Y} bringen den größten Gewinn?', f'□ {X} und □ {Y}', 'zwei ganze Zahlen', [x, y],
                       f'Ecken: (0 | 0), Achsenschnitt von I ({v["A"][0]} | 0), Achsenschnitt von II (0 | {v["B"][1]}), Schnitt I/II ({v["P"][0]} | {v["P"][1]}). {wt}. '
                       f'Am besten: {x} {X} und {y} {Y}.', 'Ecken: Achsenschnitte der Randgeraden und ihr Schnittpunkt. Dann G an allen Ecken vergleichen.', c=[str(x), str(y)])
    # gewinn_aendern
    for _ in range(50):
        n1 = R.randint(2, 20)
        w2 = [n1 * x + k2 * y for x, y in ecken]
        if n1 != k1 and sorted(w2)[-1] != sorted(w2)[-2]: break
    else:
        return None
    i2 = max(range(4), key=lambda i: w2[i])
    gleich = i2 == imax
    r = 'Nein, der beste Plan bleibt gleich.' if gleich else f'Ja, jetzt ist ({ecken[i2][0]} | {ecken[i2][1]}) am besten.'
    falsch = ['Nein, der beste Plan bleibt gleich.'] if not gleich else [f'Ja, jetzt ist ({ecken[i][0]} | {ecken[i][1]}) am besten.' for i in range(1, 4) if i != imax][:1]
    falsch += [f'Ja, jetzt ist ({ecken[i][0]} | {ecken[i][1]}) am besten.' for i in range(1, 4) if i not in (imax, i2)][:2]
    falsch.append('Das kann man ohne Zeichnung nicht sagen.')
    return auswahl(f'{firma} stellt x {X} und y {Y} her. Ecken des Bereichs: (0 | 0), ({v["A"][0]} | 0), ({v["P"][0]} | {v["P"][1]}), (0 | {v["B"][1]}). '
                   f'Bisher gilt G = {lin(k1, k2)}, bester Plan ({ecken[imax][0]} | {ecken[imax][1]}). Nun bringt {EIN1[X]} {n1} € statt {k1} €. Ändert sich der beste Plan?', r, falsch,
                   'Neuer Gewinn an den Ecken: ' + '; '.join(f'({x} | {y}): {dz(w)} €' for (x, y), w in zip(ecken, w2)) + '. ' + r,
                   'Rechne den neuen Gewinn an allen Ecken aus.')


def _filter(g, s, teil, nicht=False):
    for _ in range(120):
        t = g(s)
        if t and ((teil in t['f']['text']) != nicht): return t
    return None


def g2_bereich(s):
    if s < 3: return g_bereich(s)
    art = art3('verletzt', 'rand', 'max_y', ['verletzt', 'rand', 'max_y', 'verletzt', 'max_y'])
    if art == 'verletzt': return _filter(g_bereich, 3, 'verletzt er')
    return bereich3(art)


def g2_aufstellen(s):
    if s == 1: return g_aufstellen(1)
    if s == 2:
        if R.random() < .3: return aufst3('min_mehr')
        for _ in range(50):
            t = g_aufstellen(2)
            if t and 'Je Stück' not in t['f']['text'] and 'mindestens' not in t['f']['text']: return t
        return None
    art = art3('doppelt', 'kombi', 'prozent', ['doppelt', 'kombi', 'prozent', 'kombi', 'prozent'])
    if art == 'doppelt': return _filter(g_aufstellen, 3, 'doppelt')
    if art == 'kombi': return _filter(g_aufstellen, 3, 'System')
    return aufst3(art)


def g2_ecken(s):
    if s < 3: return g_ecken(s)
    return ecken3(art3('vierte_ecke', 'drei_bed', 'unzulaessig', ['vierte_ecke', 'drei_bed', 'unzulaessig', 'drei_bed', 'unzulaessig']))


def g2_optimum(s):
    if s < 3: return g_optimum(s)
    art = art3('min_ohne0', 'rand_optimum', 'parameter', ['min_ohne0', 'rand_optimum', 'parameter', 'max_bild', 'parameter'])
    if art == 'min_ohne0': return _filter(g_optimum, 3, 'Minimum')
    if art == 'max_bild':
        for _ in range(120):
            t = g_optimum(3)
            if t and 'Maximum' in t['f']['text'] and t['f'].get('grafik'): return t
        return None
    return opt3(art)


def g2_sach(s):
    if s == 1: return _filter(g_sach, 1, 'größtmögliche')
    if s == 2: return _filter(g_sach, 3, 'Wie viele')
    art = art3('vollstaendig', 'vergleich', 'gewinn_aendern', ['vollstaendig', 'vergleich', 'gewinn_aendern', 'vollstaendig', 'gewinn_aendern'])
    if art == 'vergleich': return _filter(g_sach, 3, 'Mitarbeiter')
    return sach3(art)


GEN = {'bereich': g2_bereich, 'aufstellen': g2_aufstellen, 'ecken': g2_ecken, 'optimum': g2_optimum, 'sach': g2_sach}

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import ko, pkte, tab  # noqa: E402

_GI = {'art': 'linear', 'm': -2, 't': 8, 'bereich': [0, 4], 'name': 'I', 'name_x': 3.3}
_GII = {'art': 'linear', 'm': -0.5, 't': 5, 'bereich': [0, 10], 'name': 'II', 'name_x': 7}
_EK = [[0, 0], [4, 0], [2, 4], [0, 5]]


def _b(**kw):
    return ko([0, 11], [0, 9], schritt=0, schritt_x=1, schritt_y=1, graphen=[_GI, _GII], **kw)


def _ecken(namen):
    return pkte({n: tuple(p) for n, p in zip(namen, _EK)})


def _ab(*z):
    return tab(['', 'Kuchen (x)', 'Torte (y)', 'Grenze'], *z)


_GR = [[0, 0], [15, 0], [6, 6], [0, 8]]
UMBAU = {
    'bereich': {
        'einstieg': 'Eine kleine Bäckerei backt x Kuchen und y Torten. Ofenzeit und Teig reichen nicht für beliebig viele. '
                    'Alle machbaren Mengen bilden den ⟦zulässigen Bereich⟧.',
        'woerter': [['Halbebene', 'alle Punkte auf einer Seite einer Geraden, die Gerade eingeschlossen'],
                    ['zulässig', 'erfüllt jede Bedingung; der zulässige Bereich sind alle solchen Punkte']],
        'bild': _b(),
        'schritte': [
            {'text': 'I: 2x + y ≤ 8 ist eine Halbebene.', 'bild': {'flaechen': [{'punkte': [[0, 0], [4, 0], [0, 8]]}]}},
            {'text': 'Mit II: x + 2y ≤ 10 entsteht der zulässige Bereich.', 'bild': {'flaechen': [{'punkte': _EK}]}},
            {'text': 'Q(2 | 3) in I: 2 · 2 + 3 = 7 ≤ 8.', 'bild': {'punkte': pkte({'Q': (2, 3)})}},
            {'text': 'In II: 2 + 2 · 3 = 8 ≤ 10. ⟦Q liegt im Bereich⟧.'},
        ],
        'fehler': 'Nur I prüfen reicht nicht. Ein Punkt kann I erfüllen und ⟦II verletzen⟧. Zulässig heißt: alle Bedingungen.',
        'fehler_bild': {'punkte': pkte({'Q': (2, 3), 'nur I': (1, 5)})},
        'regel': 'Ein Punkt ist zulässig, wenn er ⟦alle⟧ Ungleichungen erfüllt. Jede Ungleichung ist eine Halbebene.',
    },
    'aufstellen': {
        'einstieg': 'Eine größere Bäckerei hat 30 Stunden Backzeit. Ein Kuchen braucht 2 h, eine Torte 3 h. '
                    'Das wird eine Ungleichung. Was möglichst groß werden soll, ist die ⟦Zielfunktion⟧.',
        'woerter': [['Entscheidungsvariablen', 'x und y: wie viele Kuchen und wie viele Torten'],
                    ['Zielfunktion', 'der Term, der möglichst groß oder klein werden soll'],
                    ['höchstens', 'heißt ≤; mindestens heißt ≥']],
        'bild': _ab(['Zeit in h', '?', '?', '?'], ['Gewinn in €', '?', '?', '?']),
        'schritte': [
            {'text': 'Entscheidungsvariablen: x Kuchen und y Torten.'},
            {'text': 'Zeit höchstens 30 h: ⟦2x + 3y ≤ 30⟧.', 'bild': _ab(['Zeit in h', '2', '3', '≤ 30'], ['Gewinn in €', '?', '?', '?'])},
            {'text': 'Anzahlen sind nie negativ: x ≥ 0 und y ≥ 0.'},
            {'text': 'Gewinn 4 € und 7 €: Zielfunktion ⟦G = 4x + 7y⟧.',
             'bild': _ab(['Zeit in h', '2', '3', '≤ 30'], ['Gewinn in €', '4', '7', 'möglichst groß'])},
        ],
        'fehler': '„Mindestens 4 Torten“ ist nicht y ≤ 4. Mindestens heißt ⟦y ≥ 4⟧, also 4 oder mehr.',
        'regel': 'Höchstens heißt ⟦≤⟧, mindestens heißt ≥. Dazu kommen immer x ≥ 0 und y ≥ 0.',
    },
    'ecken': {
        'einstieg': 'Der zulässige Bereich der kleinen Bäckerei ist ein Viereck. Seine Ecken sind besonders wichtig. '
                    'Wo sich zwei Ränder schneiden, liegt ein ⟦Eckpunkt⟧.',
        'woerter': [['Eckpunkt', 'Schnittpunkt zweier Randgeraden des Bereichs'],
                    ['Randgerade', 'die Gerade zu einer Ungleichung, mit = statt ≤']],
        'bild': _b(flaechen=[{'punkte': _EK}]),
        'schritte': [
            {'text': 'Randgeraden: 2x + y = 8 und x + 2y = 10.'},
            {'text': 'Erste mal 2: 4x + 2y = 16. Minus zweite: 3x = 6.'},
            {'text': 'Also x = 2 und y = 8 − 2 · 2 = 4.', 'bild': {'punkte': pkte({'(2|4)': (2, 4)})}},
            {'text': 'Eckpunkt ⟦(2 | 4)⟧. Dazu kommen (0 | 0), (4 | 0), (0 | 5).',
             'bild': {'punkte': _ecken(['(0|0)', '(4|0)', '(2|4)', '(0|5)'])}},
        ],
        'fehler': 'Nur im Bild ablesen ist riskant. (2 | 4) und (2,2 | 3,8) sehen fast gleich aus. ⟦Rechne⟧ die Ecken aus.',
        'regel': 'Eckpunkt = Schnitt zweier Randgeraden. Mit einem ⟦Gleichungssystem⟧ ausrechnen, nicht nur ablesen.',
    },
    'optimum': {
        'einstieg': 'Ein Kuchen bringt 3 € Gewinn, eine Torte 2 €. Welche machbare Menge bringt am meisten? '
                    'Der beste Wert liegt immer an einer Ecke. Das ist das ⟦Eckenprinzip⟧.',
        'woerter': [['Eckenprinzip', 'das Maximum oder Minimum liegt an einer Ecke des Bereichs'],
                    ['Optimum', 'der beste Wert: größter Gewinn oder kleinste Kosten']],
        'bild': _b(flaechen=[{'punkte': _EK}], punkte=_ecken(['A', 'B', 'C', 'D'])),
        'schritte': [
            {'text': 'Zielfunktion G = 3x + 2y an allen Ecken ausrechnen.'},
            {'text': '(0 | 0): 0. (4 | 0): 12. (0 | 5): 10.', 'bild': {'punkte': _ecken(['0', '12', 'C', '10'])}},
            {'text': '(2 | 4): 3 · 2 + 2 · 4 = 14.', 'bild': {'punkte': _ecken(['0', '12', '14', '10'])}},
            {'text': 'Das Optimum ist ⟦G = 14 bei (2 | 4)⟧.'},
        ],
        'fehler': 'Den Punkt mit dem ⟦größten x⟧ nehmen ist falsch. (4 | 0) liefert nur 12, (2 | 4) aber 14.',
        'regel': 'Das ⟦Optimum liegt an einer Ecke⟧. Zielfunktion an allen Ecken ausrechnen und vergleichen.',
    },
    'sach': {
        'einstieg': 'Die größere Bäckerei will wissen, wie viele Kuchen und Torten sie backen soll. Die Ecken ihres Bereichs kennt sie schon. '
                    'Jetzt fehlt die ⟦Antwort⟧.',
        'woerter': [['Sachzusammenhang', 'die Geschichte der Aufgabe: hier Kuchen, Torten und Euro']],
        'bild': ko([0, 16], [0, 10], schritt=0, schritt_x=3, schritt_y=2, flaechen=[{'punkte': _GR}],
                   punkte=pkte({'(0|0)': (0, 0), '(15|0)': (15, 0), '(6|6)': (6, 6), '(0|8)': (0, 8)})),
        'schritte': [
            {'text': 'Gewinn G = 4x + 7y an allen vier Ecken ausrechnen.'},
            {'text': 'G: 0 €, 60 €, 24 + 42 = 66 € und 56 €.',
             'bild': {'punkte': pkte({'0 €': (0, 0), '60 €': (15, 0), '66 €': (6, 6), '56 €': (0, 8)})}},
            {'text': 'Antwort im Sachzusammenhang: ⟦6 Kuchen und 6 Torten, 66 €⟧.'},
        ],
        'fehler': 'Nur „66“ antworten genügt nicht. Gefragt ist auch, ⟦wie viele⟧ Kuchen und Torten man backen soll.',
        'regel': 'Variablen, Bedingungen, Ecken, ⟦Zielfunktion vergleichen⟧. Dann im Sachzusammenhang antworten.',
    },
}
UMBAU_OFFEN = ['Umbau (Paket UR): Die Lernkarten füllen den zulässigen Bereich jetzt farbig (koordinaten.flaechen). '
               'Die Aufgaben-Grafiken zeigen weiter nur die Randgeraden, weil Aufgaben beim Umbau unverändert bleiben.']
UMBAU_WEG = ['App-Wunsch: Halbebenen bzw. den zulässigen Bereich farbig füllen']
# ---------- Ende UMBAU ----------


d = bauen('sonder.optimierung',
      'Bedingungen als lineare Ungleichungen aufstellen, den zulässigen Bereich und seine Ecken bestimmen und die Zielfunktion optimieren.',
      ['Zulässiger Bereich (feasible region): alle Punkte, die jede Ungleichung erfüllen.',
       'Höchstens → ≤, mindestens → ≥; Anzahlen: x ≥ 0, y ≥ 0.',
       'Ecken: Schnittpunkte der Randgeraden (Gleichungssystem lösen).',
       'Eckenprinzip: Maximum und Minimum der Zielfunktion (objective function) liegen an Ecken.'],
      [('Bedingungen', ['bereich', 'aufstellen']), ('Ecken und Optimum', ['ecken', 'optimum']), ('Anwenden', ['sach'])],
      ETAPPEN, GEN,
      offen=['App-Wunsch: Halbebenen bzw. den zulässigen Bereich farbig füllen. Bisher werden nur die Randgeraden (I, II) gezeichnet; der Bereich wird in Worten beschrieben.',
             'Lehrplan-Feld leer („IB-Verlagsinhalt“): gebaut mit zwei Bedingungen plus x, y ≥ 0 und vier Ecken; Isogewinngeraden (Verschieben der Zielgeraden) nicht enthalten. Annahme MYP 4.',
             'Lineare Gleichungssysteme (für die Ecken) werden vorausgesetzt (gleichungen.lgs2).'],
      vertiefung=['sach'], plan=PLAN2)
umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)


# ---- STUFEN (Zwanzigste Runde, Zusatz Realschule/IB, Zweig stufen-rsib-2) ----
from _stufen_rsib2 import Stufen, stufen  # noqa: E402

ST = Stufen('sonder.optimierung', 20_2_8)
Z, A, L = ST.Z, ST.A, ST.L
ST.vorbild += ['Hamburg, Bildungsserver: Handreichung „V4 Lineare Optimierung“ (mehrteilige Produktionsaufgabe: Ecke berechnen, maximalen Gewinn bestimmen, Änderung des Gewinns) – https://bildungsserver.hamburg.de/resource/blob/714596/440a414b5ff37a1ddbe6fd53aa24a601/pdf-v4-data.pdf',
               'Österreich, Übungen Lineare Optimierung (HLFS, Angewandte Mathematik; Art der Teilaufgaben a/b) – https://m.schule.at/fileadmin/DAM/Gegenstandsportale/HLFS/Angewandte_Mathematik/UEbungen_Lin.Opt.pdf']

# bereich
ST.stufenleiter('bereich', 'Einen Punkt in beide Bedingungen einsetzen und entscheiden.',
                'Aus mehreren Punkten den zulässigen finden, Bedingungen in einer Sachsituation prüfen.',
                'Verletzte Bedingung finden, Punkte auf dem Rand, größtes y zu festem x, Fehler „nur eine Bedingung geprüft“, Parameter einer Bedingung, Gitterpunkte zählen.')
ST.typ('bereich', '/^/', 'erkennen', s=1)
ST.typ('bereich', '/Welcher Punkt liegt/', 'mehrschritt')
ST.typ('bereich', '/^/', 'darstellung', s=2)
ST.typ('bereich', '/verletzt er/', 'verknuepfen')
ST.typ('bereich', '/Randgeraden/', 'begruenden')
ST.typ('bereich', '/^/', 'rueckwaerts', s=3)
ST.neu('bereich', 'direkt', Z('Setze den Punkt Q(3 | 2) in die Bedingung 4x + 5y ≤ 25 ein. Welcher Wert steht dann links?', 22, '4*3 + 5*2',
       '4 · 3 + 5 · 2 = 12 + 10 = 22. Da 22 ≤ 25, erfüllt Q diese Bedingung.', 'x = 3 und y = 2 einsetzen.'))
ST.neu('bereich', 'einkleidung', A('Ein Kiosk backt x Brötchen und y Brezeln. Teig: 2x + y ≤ 40, Ofenplätze: x + y ≤ 25. Geht der Plan 12 Brötchen und 14 Brezeln?', 'Nein, die Ofenplätze reichen nicht (26 > 25).',
       ['Ja, beide Bedingungen sind erfüllt.', 'Nein, der Teig reicht nicht (38 > 40).', 'Nein, beide Bedingungen sind verletzt.'],
       'Teig: 2 · 12 + 14 = 38 ≤ 40 erfüllt. Ofen: 12 + 14 = 26 > 25 verletzt.', 'Setze in beide Bedingungen ein.'))
ST.neu('bereich', 'fehler', A('Bedingungen I: 3x + 2y ≤ 18, II: x + y ≤ 7, x ≥ 0, y ≥ 0. Jemand prüft P(2 | 6) nur in I: 6 + 12 = 18 ≤ 18, und sagt: „P liegt im Bereich.“ Was stimmt?',
       'Falsch: II ist verletzt (2 + 6 = 8 > 7).', ['Richtig.', 'Falsch: I ist verletzt, weil 18 nicht kleiner als 18 ist.', 'Falsch: P liegt nicht im Bereich, weil x < y ist.'],
       'Ein Punkt liegt nur im Bereich, wenn er alle Bedingungen erfüllt. I stimmt (Gleichheit ist erlaubt), II nicht.', 'Prüfe auch die zweite Bedingung.'))
ST.neu('bereich', 'parameter', Z('Bedingungen I: x + y ≤ 10, II: 2x + y ≤ c, x ≥ 0, y ≥ 0. Wie groß muss c mindestens sein, damit (3 | 6) im Bereich liegt?', 12, '2*3 + 6',
       'I: 3 + 6 = 9 ≤ 10 erfüllt. II: 2 · 3 + 6 = 12 ≤ c, also c ≥ 12.', 'Setze den Punkt in II ein.'))
ST.neu('bereich', 'transfer', Z('Bereich: x + y ≤ 6, x ≥ 0, y ≥ 0. Wie viele Punkte mit ganzzahligen Koordinaten liegen darin (auch auf dem Rand)?', 28, '7+6+5+4+3+2+1',
       'Für x = 0 gibt es 7 Werte für y (0 bis 6), für x = 1 sechs, …, für x = 6 einen: 7 + 6 + … + 1 = 28.', 'Zähle Spalte für Spalte.'))
ST.knobel('bereich', Z('Bereich: x ≥ 0, y ≥ 0, x + y ≤ 4 und x − y ≥ 2. Wie viele Punkte mit ganzzahligen Koordinaten liegen darin?', 4, '1 + 2 + 1',
          'x − y ≥ 2 heißt y ≤ x − 2. x = 2: y = 0. x = 3: y = 0 oder 1 (x + y ≤ 4). x = 4: y = 0. Also 4 Punkte.', 'Gehe die möglichen x-Werte einzeln durch.'))
ST.knobel('bereich', Z('Bereich: x ≥ 0, y ≥ 0, x + 2y ≤ 8 und zusätzlich x + y ≥ c. Ab welchem ganzzahligen c ist der Bereich leer?', 9, '8 + 1',
          'Ohne die Zusatzbedingung ist x + y am größten im Punkt (8 | 0): 8 (an (0 | 4) nur 4). Für c ≤ 8 bleibt (8 | 0) erlaubt, für c = 9 gibt es keinen Punkt mehr.',
          'Wie groß kann x + y in x + 2y ≤ 8 höchstens werden?'))

# aufstellen
ST.stufenleiter('aufstellen', 'Aus einem Satz eine einzelne Bedingung ablesen (Mindestzahl, Materialverbrauch).',
                'Bedingungen mit „mehr als“ und „insgesamt“, Zielfunktion aufstellen, eine Bedingung zurückübersetzen.',
                'Vielfaches und Prozentanteil als Bedingung, ganzes System, Fehler „Faktor auf der falschen Seite“, Prozentbedingung umformen, Kapazität aus einem Plan.')
ST.typ('aufstellen', '/Es müssen mindestens/', 'erkennen')
ST.typ('aufstellen', '/^/', 'direkt', s=1)
ST.typ('aufstellen', '/mehr als/', 'mehrschritt')
ST.typ('aufstellen', '/Insgesamt passen/', 'einkleidung')
ST.typ('aufstellen', '/^/', 'darstellung', s=2)
ST.typ('aufstellen', '/Welches System/', 'verknuepfen')
ST.typ('aufstellen', '/^/', 'transfer', s=3)
ST.neu('aufstellen', 'umkehr', A('Eine Schreinerei stellt x Tische und y Stühle her. Was bedeutet die Bedingung x + y ≤ 30?', 'Insgesamt werden höchstens 30 Möbelstücke hergestellt.',
       ['Es werden höchstens 30 Tische hergestellt.', 'Es werden mindestens 30 Möbelstücke hergestellt.', 'Es werden höchstens 30 Stühle mehr als Tische hergestellt.'],
       'x + y ist die Gesamtzahl, ≤ heißt „höchstens“.', 'Was zählt x + y?'))
ST.neu('aufstellen', 'fehler', A('Eine Bäckerei stellt x Kuchen und y Torten her. „Mindestens doppelt so viele Torten wie Kuchen“. Jemand schreibt 2y ≥ x. Was stimmt?', 'Falsch: richtig ist y ≥ 2x.',
       ['Richtig.', 'Falsch: richtig ist x ≥ 2y.', 'Falsch: richtig ist y ≤ 2x.'],
       'Test mit 2 Kuchen: Es müssen mindestens 4 Torten sein. y ≥ 2x verlangt y ≥ 4; 2y ≥ x würde schon 1 Torte erlauben.', 'Prüfe mit einem Zahlenbeispiel.'))
ST.neu('aufstellen', 'begruenden', A('„Höchstens 40 % aller Stücke sind Torten“: y ≤ 0,4 · (x + y). Stimmt die Umformung zu 3y ≤ 2x?', 'Ja.',
       ['Nein, richtig ist y ≤ 0,4x.', 'Nein, richtig ist 2y ≤ 3x.', 'Nein, richtig ist 3y ≥ 2x.'],
       'y ≤ 0,4x + 0,4y ⇒ 0,6y ≤ 0,4x ⇒ (mal 5) 3y ≤ 2x.', 'Bringe alle y auf eine Seite.'))
ST.neu('aufstellen', 'parameter', Z('Ein Kuchen braucht 1 h, eine Torte 3 h; es stehen T Stunden zur Verfügung. Der Plan 4 Kuchen und 6 Torten soll gerade noch möglich sein. Wie groß ist T?', 22, '4*1 + 6*3',
       'Bedingung x + 3y ≤ T. Gerade noch möglich: T = 4 + 18 = 22.', 'Stelle die Zeitbedingung auf.', einheit='h'))
ST.knobel('aufstellen', L('Die Randgerade einer Bedingung geht durch (0 | 6) und (9 | 0); der Nullpunkt erfüllt die Bedingung. Wie lautet sie (kleinste ganze Zahlen)?', '□x + □y ≤ □', [2, 3, 18], ['2', '3', '18'],
          'Ansatz ax + by = c: (0 | 6) gibt 6b = c, (9 | 0) gibt 9a = c. Mit c = 18: a = 2, b = 3. Der Nullpunkt (0 ≤ 18) liegt auf der „≤“-Seite.', 'Setze beide Achsenpunkte in ax + by = c ein.'))
ST.knobel('aufstellen', Z('Eine Bäckerei: mindestens 3 Torten (y), mindestens so viele Kuchen (x) wie Torten, insgesamt höchstens 10 Stück. Wie viele ganzzahlige Pläne (x | y) gibt es?', 9, '5 + 3 + 1',
          'y = 3: x = 3 bis 7 (5 Pläne). y = 4: x = 4 bis 6 (3). y = 5: x = 5 (1). y = 6 ginge nur mit x ≥ 6, dann x + y ≥ 12. Zusammen 9.', 'Gehe die möglichen Tortenzahlen einzeln durch.'))

# ecken
ST.stufenleiter('ecken', 'Achsenschnittpunkte einer Randgeraden berechnen.',
                'Schnittpunkt zweier Randgeraden mit dem Additionsverfahren, Ecke in einer Sachsituation, Konstante aus einer Ecke.',
                'Vierte Ecke, neue Bedingung schneidet den Rand, Achsenpunkt als Scheinecke, Fehler „Ecke verletzt eine Bedingung“, Parameter für einen Schnittpunkt.')
ST.typ('ecken', '/^/', 'direkt', s=1)
ST.typ('ecken', '/^/', 'mehrschritt', s=2)
ST.typ('ecken', '/vierte Ecke/', 'verknuepfen')
ST.typ('ecken', '/neue Randgerade/', 'transfer')
ST.typ('ecken', '/^/', 'begruenden', s=3)
ST.neu('ecken', 'erkennen', A('Bei den Bedingungen x ≥ 0 und y ≥ 0: Welcher Punkt ist eine Ecke, wenn er zum Bereich gehört?', '(0 | 0)', ['(1 | 1)', 'der Schnittpunkt der beiden anderen Randgeraden, immer', '(0 | 1)'],
       'x = 0 und y = 0 sind zwei Randgeraden; sie schneiden sich im Nullpunkt.', 'Wo schneiden sich die beiden Achsen?'))
ST.neu('ecken', 'einkleidung', L('Lager: x + y ≤ 10, Maschinenzeit: 2x + y ≤ 14. Bei welchem Plan sind Lager und Maschine genau ausgelastet?', '(□ | □)', [4, 6], ['14 - 10', '10 - 4'],
       '2x + y = 14 minus x + y = 10 ergibt x = 4, dann y = 6.', 'Setze beide Bedingungen als Gleichungen an.'))
ST.neu('ecken', 'umkehr', Z('Der Eckpunkt (3 | 4) liegt auf der Randgeraden 2x + y = c. Wie groß ist c?', 10, '2*3 + 4', '2 · 3 + 4 = 10.', 'Setze den Punkt ein.'))
ST.neu('ecken', 'fehler', A('Bedingungen I: x + y ≤ 8, II: x + 3y ≤ 12, x ≥ 0, y ≥ 0. Jemand nennt die Ecken (0 | 0), (8 | 0), (6 | 2) und (0 | 8). Was stimmt?', 'Falsch: (0 | 8) verletzt II; richtig ist (0 | 4).',
       ['Richtig.', 'Falsch: (6 | 2) verletzt I.', 'Falsch: (8 | 0) verletzt II.'],
       '(0 | 8): 0 + 24 = 24 > 12. Auf der y-Achse begrenzt II stärker: 3y = 12 ⇒ (0 | 4). (6 | 2) erfüllt beide mit Gleichheit.', 'Setze jede Ecke in beide Bedingungen ein.'))
ST.neu('ecken', 'parameter', Z('Für welches c schneiden sich die Randgeraden x + 2y = 12 und 2x + y = c im Punkt mit x = 2?', 9, '2*2 + 5',
       'x = 2 in die erste: 2y = 10 ⇒ y = 5. Dann c = 2 · 2 + 5 = 9.', 'Bestimme zuerst y.'))
ST.knobel('ecken', Z('Wie viele Ecken hat der Bereich x ≥ 0, y ≥ 0, x + y ≤ 6, x ≤ 4, y ≤ 4?', 5, '5',
          'Ecken: (0 | 0), (4 | 0), (4 | 2), (2 | 4), (0 | 4). Die Gerade x + y = 6 schneidet die Ecke bei (4 | 4) ab – aus einer Ecke werden zwei.', 'Zeichne zuerst das Quadrat x ≤ 4, y ≤ 4.'))
ST.knobel('ecken', A('Bedingungen I: x + y ≤ 6, II: 2x + y ≤ 10, III: x ≤ 5, x ≥ 0, y ≥ 0. Eine Bedingung ändert den Bereich nicht. Welche?', 'III', ['I', 'II', 'keine'],
          'Ohne III hat der Bereich die Ecken (0 | 0), (5 | 0), (4 | 2), (0 | 6): Überall ist x ≤ 5. Ohne I käme z. B. (0 | 10) dazu, ohne II z. B. (5 | 1) (2 · 5 + 1 = 11).',
          'Prüfe, ob der Bereich ohne die Bedingung Punkte enthält, die sie verletzen.'))

# optimum
ST.stufenleiter('optimum', 'Zielfunktion in einer Ecke ausrechnen, Maximum an gegebenen Ecken.',
                'Alle Ecken vergleichen, Werte tabellieren, Optimum in einer Sachsituation.',
                'Minimum statt Maximum, ganze Kante optimal, Parameter der Zielfunktion, Fehler „größtes x ist am besten“, Koeffizient rückwärts.')
ST.typ('optimum', '/^/', 'direkt', s=1)
ST.typ('optimum', '/^/', 'mehrschritt', s=2)
ST.typ('optimum', '/Minimum/', 'transfer')
ST.typ('optimum', '/Wo wird Z/', 'begruenden')
ST.typ('optimum', '/Ab welchem ganzzahligen Wert/', 'parameter')
ST.typ('optimum', '/^/', 'mehrschritt', s=3)
ST.neu('optimum', 'erkennen', A('Der zulässige Bereich ist ein Vieleck. Wo nimmt eine lineare Zielfunktion ihr Maximum an?', 'in einer Ecke (manchmal zusätzlich auf einer ganzen Kante)',
       ['immer in der Mitte des Bereichs', 'immer im Nullpunkt', 'immer auf der x-Achse'], 'Verschiebt man die Zielgerade, verlässt sie den Bereich zuletzt an einer Ecke.', 'Denke an das Verschieben der Zielgeraden.'))
ST.neu('optimum', 'darstellung', L('Ecken (0 | 0), (6 | 0), (4 | 3), (0 | 5). Berechne Z = 2x + 3y in dieser Reihenfolge.', '□; □; □; □', [0, 12, 17, 15], ['0', '2*6', '2*4 + 3*3', '3*5'],
       '0; 12; 8 + 9 = 17; 15. Maximum 17 bei (4 | 3).', 'Setze jede Ecke ein.'))
ST.neu('optimum', 'einkleidung', Z('Ein Händler hat den Bereich mit den Ecken (0 | 0), (8 | 0), (5 | 4), (0 | 6). Gewinn G = 3x + 4y (in €). Wie groß ist der größte Gewinn?', 31, '3*5 + 4*4',
       '0; 24; 15 + 16 = 31; 24. Größter Gewinn 31 € bei (5 | 4).', 'Setze alle Ecken ein.', einheit='€'))
ST.neu('optimum', 'fehler', A('Ecken (0 | 0), (7 | 0), (4 | 4), (0 | 5), Z = 2x + 3y. Jemand sagt: „Das Maximum liegt bei (7 | 0), weil x dort am größten ist.“ Was stimmt?', 'Falsch: Z(4 | 4) = 20 ist größer als Z(7 | 0) = 14.',
       ['Richtig.', 'Falsch: Das Maximum liegt bei (0 | 5).', 'Falsch: Das Maximum liegt bei (0 | 0).'],
       'Werte: 0; 14; 8 + 12 = 20; 15. Man muss alle Ecken einsetzen.', 'Setze alle Ecken ein.'))
ST.neu('optimum', 'rueckwaerts', Z('Ecken (0 | 0), (6 | 0), (4 | 3), (0 | 5). Z = a · x + 2y hat in (4 | 3) den Wert 18. Wie groß ist a?', 3, '(18 - 6)/4',
       '4a + 2 · 3 = 18 ⇒ 4a = 12 ⇒ a = 3.', 'Setze die Ecke in Z ein.'))
ST.knobel('optimum', A('Ecken (0 | 0), (5 | 0), (4 | 2), (0 | 5), Z = 2x + y. Wie viele Punkte des Bereichs liefern das Maximum?', 'unendlich viele (die ganze Kante von (5 | 0) bis (4 | 2))',
          ['genau einer', 'genau zwei', 'keiner'],
          'Z(5 | 0) = 10, Z(4 | 2) = 10, Z(0 | 5) = 5. Die Zielgerade 2x + y = 10 liegt genau auf der Kante zwischen beiden Ecken – jeder Punkt dieser Strecke ist optimal.',
          'Vergleiche die Werte der beiden besten Ecken.'))
ST.knobel('optimum', A('Ecken (0 | 0), (4 | 0), (3 | 3), (0 | 4), Z = x + a · y mit a > 0. Für welche a ist (3 | 3) die einzige beste Ecke?', 'für 1/3 < a < 3',
          ['für alle a > 0', 'nur für a = 1', 'für a > 3'],
          'Z: 4; 3 + 3a; 4a. (3 | 3) schlägt (4 | 0), wenn 3 + 3a > 4, also a > 1/3, und (0 | 4), wenn 3 + 3a > 4a, also a < 3.', 'Stelle zwei Ungleichungen für a auf.'))

# sach
ST.stufenleiter('sach', 'Gewinn an gegebenen Ecken ausrechnen und den besten Plan nennen.',
                'Gewinn an allen Ecken vergleichen, Werte tabellieren, Stückzahl aus einem Gewinn.',
                'Ecken selbst bestimmen, Vorschlag bewerten, Preisänderung, mehrteilige Prüfungsaufgabe.')
ST.typ('sach', '/^/', 'direkt', s=1)
ST.typ('sach', '/^/', 'mehrschritt', s=2)
ST.typ('sach', '/Bestimme zuerst/', 'verknuepfen')
ST.typ('sach', '/schlägt vor/', 'begruenden')
ST.typ('sach', '/^/', 'parameter', s=3)
ST.neu('sach', 'erkennen', A('Eine Bäckerei hat den Gewinn G = 6x + 15y (x Kuchen, y Torten, in €). Was bedeutet die 15?', 'Jede Torte bringt 15 € Gewinn.',
       ['Es werden 15 Torten hergestellt.', 'Jeder Kuchen bringt 15 € Gewinn.', 'Der Gewinn ist höchstens 15 €.'], 'Der Faktor vor y ist der Gewinn je Torte.', 'Zu welcher Variablen gehört die 15?'))
ST.neu('sach', 'umkehr', Z('Bei G = 5x + 8y (in €) bringt ein Plan mit 6 Kuchen insgesamt 70 €. Wie viele Torten (y) enthält er?', 5, '(70 - 5*6)/8',
       '30 + 8y = 70 ⇒ 8y = 40 ⇒ y = 5.', 'Setze x = 6 ein.'))
ST.neu('sach', 'darstellung', L('Ecken (0 | 0), (9 | 0), (6 | 4), (0 | 7), Gewinn G = 4x + 5y. Trage den Gewinn in € in dieser Reihenfolge ein.', '□ €; □ €; □ €; □ €', [0, 36, 44, 35],
       ['0', '4*9', '4*6 + 5*4', '5*7'], '0; 36; 24 + 20 = 44; 35. Bester Plan (6 | 4).', 'Setze jede Ecke ein.'))
ST.neu('sach', 'pruefung', L('Ein Betrieb fertigt x Regale und y Schränke. Montage: 2 h je Regal, 4 h je Schrank, höchstens 40 h. Lackieren: 2 h je Regal, 1 h je Schrank, höchstens 22 h. Gewinn 30 € je Regal, 50 € je Schrank. a) In welcher Ecke sind beide Zeiten voll ausgelastet? b) Wie groß ist der größte Gewinn?',
       'a) (□ | □); b) □ €', [8, 6, 540], ['(40 - 4*6)/2', '(40 - 22)/3', '30*8 + 50*6'],
       'a) 2x + 4y = 40 minus 2x + y = 22: 3y = 18 ⇒ y = 6, x = 8. b) Ecken (0 | 0), (11 | 0), (8 | 6), (0 | 10): G = 0; 330; 540; 500. Größter Gewinn 540 € bei 8 Regalen und 6 Schränken.',
       'Stelle die beiden Zeitbedingungen auf und setze sie gleich.'))
ST.knobel('sach', Z('Bedingungen 2x + 3y ≤ 13, 2x + y ≤ 9, x ≥ 0, y ≥ 0, x und y ganzzahlig. Gewinn G = 3x + 4y. Wie groß ist der größte Gewinn?', 18, '3*2 + 4*3',
          'Die Ecke (3,5 | 2) ist nicht ganzzahlig. Abrunden auf (3 | 2) gibt 17. Prüft man die ganzzahligen Punkte am Rand: (2 | 3) erfüllt 4 + 9 = 13 und 4 + 3 = 7 und bringt 6 + 12 = 18; (4 | 1) bringt 16, (0 | 4) 16. Bester Plan (2 | 3) mit 18.',
          'Abrunden der Ecke ist nicht immer am besten – prüfe ganzzahlige Punkte nahe am Rand.'))
ST.knobel('sach', Z('Die Pläne (4 | 4) und (6 | 1) bringen beide den gleichen größten Gewinn G = a · x + 4y. Wie groß ist a?', 6, '(16 - 4)/2',
          'Gleicher Gewinn heißt G(4 | 4) = G(6 | 1): 4a + 16 = 6a + 4 ⇒ 2a = 12 ⇒ a = 6. Probe: 24 + 16 = 40 und 36 + 4 = 40.', 'Setze beide Pläne gleich.'))

if __name__ == '__main__':
    stufen('sonder.optimierung', ST)
