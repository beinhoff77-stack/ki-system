#!/usr/bin/env python3
"""Thema sonder.optimierung – Lineare Optimierung (IB MYP 4, etwa Klasse 9)."""
import sys
from math import gcd
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403

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
        return auswahl(vor + f' Der Gewinn beträgt {g1} € pro Stück bei den {X} und {g2} € pro Stück bei den {Y}. Wie lautet die Zielfunktion?', r,
                       [f'G = {lin(g2, g1)}', f'G = {g1 + g2}x', f'G = {lin(g1, g2)} − {c}'],
                       f'Gewinn aus x Stück {X}: {g1}x; aus y Stück {Y}: {g2}y. Zusammen {r}.', 'Gewinn je Stück mal Anzahl, für beide Produkte addiert.')
    if art == 'doppelt':
        r = 'y ≥ 2x'
        return auswahl(vor + f' Es sollen mindestens doppelt so viele {Y} wie {X} hergestellt werden. Welche Bedingung passt?', r, ['x ≥ 2y', 'y ≤ 2x', 'y + 2 ≥ x'],
                       f'Die Anzahl der {Y} (y) soll mindestens das Doppelte von x sein: y ≥ 2x. Probe: x = 3, y = 7 erfüllt das (7 ≥ 6).',
                       'Teste mit Zahlen: x = 3 – wie viele y muss es mindestens geben?')
    k1, k2 = R.randint(2, 5), R.randint(2, 5)
    zeit = R.randint(30, 90)
    r = f'{lin(k1, k2)} ≤ {zeit} und x ≥ 0, y ≥ 0'
    return auswahl(vor + f' Ein Stück {X} braucht {k1} h, ein Stück {Y} {k2} h; es gibt {zeit} Arbeitsstunden. Welches System beschreibt alle Bedingungen?', r,
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


GEN = {'bereich': g_bereich, 'aufstellen': g_aufstellen, 'ecken': g_ecken, 'optimum': g_optimum, 'sach': g_sach}

bauen('sonder.optimierung',
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
      vertiefung=['sach'])
