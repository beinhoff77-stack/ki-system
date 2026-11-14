#!/usr/bin/env python3
"""Thema geometrie.konstruktion – Konstruktionen, Kongruenz und Beweise (Gymnasium Bayern, Klasse 7)."""
import math
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl7 import A, Z, baue, figur, zt  # noqa: E402

META = {'thema_schluessel': 'geometrie.konstruktion', 'thema_id': 44, 'block_id': 80, 'klasse': {'gym_by': 7, 'rs_by': 6}}


def dreieck(al, be, c=6.0):
    """Punkte A, B, C eines Dreiecks mit den Winkeln α (bei A) und β (bei B), Seite c = AB (nur fürs Bild, gerundet)."""
    ga = 180 - al - be
    b = c * math.sin(math.radians(be)) / math.sin(math.radians(ga))
    C = (round(b * math.cos(math.radians(al)), 2), round(b * math.sin(math.radians(al)), 2))
    return {'A': [0, 0], 'B': [c, 0], 'C': list(C)}


def dreieck_bild(al, be, wtexte=('α', 'β', 'γ'), seiten=None):
    p = dreieck(al, be)
    lin = [['A', 'B', (seiten or {}).get('c', '')], ['B', 'C', (seiten or {}).get('a', '')], ['C', 'A', (seiten or {}).get('b', '')]]
    lin = [[u, v, t] if t else [u, v] for u, v, t in lin]
    w = [['A', 'B', 'C', wtexte[0]], ['B', 'C', 'A', wtexte[1]], ['C', 'A', 'B', wtexte[2]]]
    w = [x for x in w if x[3]]
    return figur(p, linien=lin, flaeche=['A', 'B', 'C'], winkel=w)


ETAPPEN = [
    {'lernziel': 'winkelsumme', 'titel': 'Winkel im Dreieck berechnen',
     'regel': 'In jedem Dreieck ist die ⟦Winkelsumme 180°⟧: α + β + γ = 180°. Ein ⟦Außenwinkel⟧ ist so groß wie die Summe der beiden ⟦nicht anliegenden⟧ Innenwinkel.',
     'schritte': ['α = 50°, β = 75°', 'γ = 180° − 50° − 75°', '⟦γ = 55°⟧'],
     'fehler': 'γ = 360° − 50° − 75° ist falsch: 360° ist die Winkelsumme im ⟦Viereck⟧. Im Dreieck sind es 180°.',
     'bild': dreieck_bild(50, 75, ('α = 50°', 'β = 75°', 'γ = ?')),
     '_verbot': ['α = 50°, β = 75°']},
    {'lernziel': 'gleichschenklig', 'titel': 'Gleichschenklige Dreiecke',
     'regel': 'Im ⟦gleichschenkligen Dreieck⟧ sind die beiden ⟦Basiswinkel⟧ gleich groß. Im ⟦gleichseitigen⟧ Dreieck sind alle Winkel 60°.',
     'schritte': ['Spitzenwinkel γ = 40°', 'Basiswinkel zusammen: 180° − 40° = 140°', 'Je Basiswinkel: 140° : 2 = ⟦70°⟧'],
     'fehler': 'Bei γ = 40° sind die Basiswinkel nicht je 40°: Nur die ⟦beiden Basiswinkel⟧ sind gleich, der Spitzenwinkel ist anders.',
     'bild': figur({'A': [0, 0], 'B': [4, 0], 'C': [2, 5.49]}, linien=[['A', 'B', 'Basis'], ['B', 'C', 'Schenkel'], ['C', 'A', 'Schenkel']], flaeche=['A', 'B', 'C'],
                   winkel=[['A', 'B', 'C', '70°'], ['B', 'C', 'A', '70°'], ['C', 'A', 'B', '40°']]),
     '_verbot': ['γ = 40°']},
    {'lernziel': 'kongruenzsatz', 'titel': 'Welcher Kongruenzsatz passt?',
     'regel': 'Dreiecke sind ⟦kongruent⟧ (deckungsgleich), wenn sie übereinstimmen in: ⟦SSS⟧ (drei Seiten), ⟦SWS⟧ (zwei Seiten und eingeschlossener Winkel), ⟦WSW⟧ (eine Seite, zwei Winkel) oder ⟦SsW⟧ (zwei Seiten und der Winkel gegenüber der ⟦größeren⟧ Seite).',
     'schritte': ['Gegeben: b = 5 cm, c = 7 cm, α = 40°', 'α liegt zwischen b und c (bei A).', 'Kongruenzsatz ⟦SWS⟧ – das Dreieck ist eindeutig.'],
     'fehler': 'Drei gleiche Winkel (WWW) reichen nicht: Die Dreiecke haben dann zwar dieselbe Form, können aber ⟦verschieden groß⟧ sein.',
     '_verbot': ['b = 5 cm, c = 7 cm, α = 40°']},
    {'lernziel': 'konstruierbar', 'titel': 'Ist das Dreieck konstruierbar?',
     'regel': 'Ein Dreieck aus drei Seiten gibt es nur, wenn ⟦je zwei Seiten zusammen länger⟧ sind als die dritte (Dreiecksungleichung). Zwei gegebene Winkel müssen zusammen ⟦weniger als 180°⟧ ergeben.',
     'schritte': ['a = 3 cm, b = 4 cm, c = 8 cm', '3 cm + 4 cm = 7 cm < 8 cm', 'Die Kreisbögen treffen sich nicht: ⟦nicht konstruierbar⟧.'],
     'fehler': 'Bei a = 3 cm, b = 5 cm, c = 8 cm entsteht kein Dreieck: 3 + 5 = 8 ist ⟦nicht größer⟧ als 8. Die Punkte lägen alle auf einer Linie.',
     '_verbot': ['a = 3 cm, b = 4 cm, c = 8 cm']},
    {'lernziel': 'vierecke', 'titel': 'Winkel in symmetrischen Vierecken',
     'regel': 'Winkelsumme im Viereck: ⟦360°⟧. ⟦Parallelogramm⟧: gegenüberliegende Winkel gleich, benachbarte zusammen 180°. ⟦Drachenviereck⟧: die beiden Winkel neben der Symmetrieachse sind gleich. ⟦Gleichschenkliges Trapez⟧: die Winkel an einer Grundseite sind gleich.',
     'schritte': ['Parallelogramm ABCD mit α = 65°', 'γ = α = 65°; β = 180° − 65° = ⟦115°⟧', 'δ = β = 115°. Probe: 65 + 115 + 65 + 115 = 360 ✓'],
     'fehler': 'Im Parallelogramm ist β nicht ebenfalls 65°: ⟦Benachbarte⟧ Winkel ergänzen sich zu 180°, nur ⟦gegenüberliegende⟧ sind gleich.',
     'bild': figur({'A': [0, 0], 'B': [5, 0], 'C': [6.27, 2.72], 'D': [1.27, 2.72]}, linien=[['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A']], flaeche=['A', 'B', 'C', 'D'],
                   winkel=[['A', 'B', 'D', '65°'], ['B', 'C', 'A', 'β']]),
     '_verbot': ['α = 65°']},
    {'lernziel': 'satz_kehrsatz', 'titel': 'Satz und Kehrsatz',
     'regel': 'Ein Satz hat die Form ⟦„Wenn A, dann B.“⟧ Beim ⟦Kehrsatz⟧ werden Voraussetzung und Behauptung vertauscht: „Wenn B, dann A.“ Ein Kehrsatz ist ⟦nicht automatisch wahr⟧ – ein Gegenbeispiel genügt, um ihn zu widerlegen.',
     'schritte': ['Satz: Wenn ein Viereck ein Quadrat ist, dann hat es vier rechte Winkel. (wahr)', 'Kehrsatz: Wenn ein Viereck vier rechte Winkel hat, dann ist es ein Quadrat.', 'Gegenbeispiel: Rechteck 2 cm × 5 cm. Der Kehrsatz ist ⟦falsch⟧.'],
     'fehler': 'Aus „der Satz ist wahr“ folgt nicht „der Kehrsatz ist wahr“. Jeder Kehrsatz muss ⟦eigens geprüft⟧ werden.'},
]


def g_winkelsumme(R, st):
    while True:
        al, be = R.randint(20, 120), R.randint(20, 120)
        if al + be < 160: break
    ga = 180 - al - be
    if st == 1:
        a = Z(f'In einem Dreieck ist α = {al}° und β = {be}°. Berechne γ.', ga, f'180 - {al} - {be}', f'γ = 180° − {al}° − {be}° = {ga}°.',
              'Die drei Winkel ergeben zusammen 180°.', '°')
        a['f']['grafik'] = dreieck_bild(al, be, (f'{al}°', f'{be}°', 'γ'))
        return a
    if st == 2:
        if R.random() < .5:
            return Z(f'Ein Außenwinkel bei C ist der Nebenwinkel von γ. Berechne ihn für α = {al}° und β = {be}°.', al + be, f'{al} + {be}',
                     f'Außenwinkel bei C = α + β = {al}° + {be}° = {al + be}°. (Probe: 180° − γ = 180° − {ga}° = {al + be}°)', 'Außenwinkel = 180° − Innenwinkel, oder Summe der beiden anderen Innenwinkel.', '°')
        # rechtwinklig
        a2 = R.randint(15, 75)
        a = Z(f'Ein Dreieck ist bei C rechtwinklig, α = {a2}°. Berechne β.', 90 - a2, f'180 - 90 - {a2}', f'β = 180° − 90° − {a2}° = {90 - a2}°.',
              'Ein rechter Winkel hat 90°.', '°')
        a['f']['grafik'] = figur(dreieck(a2, 90 - a2), linien=[['A', 'B'], ['B', 'C'], ['C', 'A']], flaeche=['A', 'B', 'C'],
                                 rechter_winkel=[['C', 'A', 'B']], winkel=[['A', 'B', 'C', f'{a2}°'], ['B', 'C', 'A', 'β']])
        return a
    # Stufe 3: Winkel im Verhältnis oder mit Variable
    k = R.choice([2, 3, 4])
    while True:
        x = R.randint(10, 50)
        d = R.randint(5, 30)
        rest = 180 - x - k * x
        if rest > 0 and rest != x: break
    return Z(f'In einem Dreieck ist β {k}-mal so groß wie α, und γ = {rest}°. Wie groß ist α?', x, f'(180 - {rest}) / ({k} + 1)',
             f'α + {k}α + {rest}° = 180° → {k + 1}α = {180 - rest}° → α = {x}°.', 'Schreibe β mit α und stelle eine Gleichung auf.', '°')


def g_gleichschenklig(R, st):
    if st == 1:
        g = R.choice(range(20, 161, 2))
        b = (180 - g) // 2
        a = Z(f'Ein gleichschenkliges Dreieck hat den Spitzenwinkel γ = {g}°. Wie groß ist ein Basiswinkel?', b, f'(180 - {g}) / 2', f'(180° − {g}°) : 2 = {b}°.',
              'Die beiden Basiswinkel sind gleich groß.', '°')
        a['f']['grafik'] = figur(dreieck(b, b), linien=[['A', 'B'], ['B', 'C'], ['C', 'A']], flaeche=['A', 'B', 'C'], winkel=[['C', 'A', 'B', f'{g}°'], ['A', 'B', 'C', '?']])
        return a
    if st == 2:
        b = R.randint(20, 85)
        a = Z(f'Ein gleichschenkliges Dreieck hat den Basiswinkel {b}°. Wie groß ist der Spitzenwinkel?', 180 - 2 * b, f'180 - 2 * {b}',
              f'Zwei Basiswinkel: 2 · {b}° = {2 * b}°. Spitzenwinkel: 180° − {2 * b}° = {180 - 2 * b}°.', 'Es gibt zwei gleich große Basiswinkel.', '°')
        a['f']['grafik'] = figur(dreieck(b, b), linien=[['A', 'B'], ['B', 'C'], ['C', 'A']], flaeche=['A', 'B', 'C'], winkel=[['A', 'B', 'C', f'{b}°'], ['C', 'A', 'B', '?']])
        return a
    art = R.choice(['aussen', 'zwei', 'gleichseitig'])
    if art == 'aussen':
        w = R.choice(range(100, 171, 2))
        return Z(f'Bei einem gleichschenkligen Dreieck ist der Außenwinkel an einem Basiswinkel {w}°. Wie groß ist der Spitzenwinkel?', 180 - 2 * (180 - w),
                 f'180 - 2 * (180 - {w})', f'Basiswinkel = 180° − {w}° = {180 - w}°. Spitzenwinkel = 180° − 2 · {180 - w}° = {180 - 2 * (180 - w)}°.',
                 'Erst den Basiswinkel aus dem Nebenwinkel bestimmen.', '°')
    if art == 'zwei':
        g = R.choice([20, 30, 36, 40, 44, 50, 60, 70, 80, 100])
        return Z(f'Ein Dach ist im Querschnitt ein gleichschenkliges Dreieck. Der Winkel am First beträgt {g}°. Wie steil ist das Dach (Winkel zwischen Dachfläche und waagrechtem Boden)?',
                 Fr(180 - g, 2), f'(180 - {g}) / 2', f'Die Dachneigung ist ein Basiswinkel: (180° − {g}°) : 2 = {zt(Fr(180 - g, 2))}°.', 'Der Winkel am First ist der Spitzenwinkel.', '°')
    n = R.choice([2, 3, 4])
    return Z(f'Wie groß ist die Summe aller Innenwinkel in einer Figur aus {n} gleichseitigen Dreiecken, die zu einem Streifen aneinandergelegt sind? (Zähle jedes Dreieck einzeln.)',
             180 * n, f'180 * {n}', f'Jedes Dreieck hat 180°: {n} · 180° = {180 * n}°. Jeder einzelne Winkel ist 60°.', 'Jedes Dreieck hat die Winkelsumme 180°.', '°')


SAETZE = ['SSS', 'SWS', 'WSW', 'SsW', 'nicht eindeutig']


def g_kongruenzsatz(R, st):
    a, b, c = sorted(R.sample(range(3, 12), 3))
    w1, w2 = R.sample(range(25, 80, 5), 2)
    art = R.choice(SAETZE if st > 1 else SAETZE[:3])
    seiten = R.sample(['a', 'b', 'c'], 3)
    win = {'a': 'α', 'b': 'β', 'c': 'γ'}
    if art == 'SSS':
        if a + b <= c: c = a + b - 1
        txt, gr = f'a = {a} cm, b = {b} cm, c = {c} cm', 'Drei Seiten gegeben.'
    elif art == 'SWS':
        s1, s2 = seiten[0], seiten[1]; zw = [x for x in 'abc' if x not in (s1, s2)][0]
        txt, gr = f'{s1} = {a} cm, {s2} = {b} cm, {win[zw]} = {w1}°', f'{win[zw]} liegt zwischen {s1} und {s2} (eingeschlossener Winkel).'
    elif art == 'WSW':
        s = seiten[0]; andere = [x for x in 'abc' if x != s]
        txt, gr = f'{s} = {a} cm, {win[andere[0]]} = {w1}°, {win[andere[1]]} = {w2}°', 'Eine Seite und zwei Winkel gegeben (der dritte Winkel folgt aus der Winkelsumme).'
    elif art == 'SsW':
        gross, klein = 'c', 'a'
        txt, gr = f'a = {a} cm, c = {c} cm, γ = {w1}°', f'γ liegt gegenüber der größeren Seite c = {c} cm.'
    else:
        if R.random() < .5:
            txt, gr = f'α = {w1}°, β = {w2}°, γ = {180 - w1 - w2}°', 'Nur drei Winkel: Form fest, Größe nicht.'
        else:
            txt, gr = f'a = {a} cm, c = {c} cm, α = {w1}°', f'α liegt gegenüber der kleineren Seite a – es kann zwei verschiedene Dreiecke geben.'
    return A(R, f'Gegeben: {txt}. Welcher Kongruenzsatz garantiert ein eindeutiges Dreieck?', art if art != 'nicht eindeutig' else 'keiner – das Dreieck ist nicht eindeutig',
             [s if s != 'nicht eindeutig' else 'keiner – das Dreieck ist nicht eindeutig' for s in SAETZE if s != art][:3], gr,
             'Zähle Seiten und Winkel. Liegt der Winkel zwischen den Seiten oder gegenüber?')


def g_konstruierbar(R, st):
    if st == 1:
        a, b = R.randint(2, 9), R.randint(2, 9)
        c = R.choice([a + b + R.randint(0, 3), max(a, b) + R.randint(1, min(a, b) - 1) if min(a, b) > 1 else a + b + 1])
        ok = a + b > c and a + c > b and b + c > a
        r = 'Ja, je zwei Seiten sind zusammen länger als die dritte.' if ok else 'Nein, zwei Seiten sind zusammen nicht länger als die dritte.'
        return A(R, f'Kann man ein Dreieck mit a = {a} cm, b = {b} cm und c = {c} cm konstruieren?', r,
                 ['Nein, zwei Seiten sind zusammen nicht länger als die dritte.' if ok else 'Ja, je zwei Seiten sind zusammen länger als die dritte.',
                  'Ja, mit drei Seiten geht es immer.', 'Nein, alle Seiten müssen gleich lang sein.'],
                 f'{min(a, b)} + {max(a, b)} = {a + b} {">" if a + b > c else "≤"} {c}.' + ('' if ok else ' Die Kreisbögen schneiden sich nicht.'),
                 'Prüfe: Sind die beiden kürzeren Seiten zusammen länger als die längste?')
    if st == 2:
        a, b = R.randint(2, 12), R.randint(2, 12)
        if R.random() < .5:
            return Z(f'Zwei Seiten eines Dreiecks sind {a} cm und {b} cm lang. Die dritte Seite ist ganzzahlig. Wie lang kann sie höchstens sein?', a + b - 1, f'{a} + {b} - 1',
                     f'Die dritte Seite muss kürzer als {a} + {b} = {a + b} cm sein. Größte ganze Zahl: {a + b - 1} cm.', 'Dreiecksungleichung: c < a + b.', 'cm')
        if a == b: b += 1
        return Z(f'Zwei Seiten eines Dreiecks sind {a} cm und {b} cm lang. Die dritte Seite ist ganzzahlig. Wie lang muss sie mindestens sein?', abs(a - b) + 1, f'abs({a} - {b}) + 1',
                 f'Die dritte Seite muss länger als {max(a, b)} − {min(a, b)} = {abs(a - b)} cm sein. Kleinste ganze Zahl: {abs(a - b) + 1} cm.', 'Auch die längere der beiden gegebenen Seiten muss kürzer sein als die anderen beiden zusammen.', 'cm')
    a, b = R.randint(3, 10), R.randint(3, 10)
    lo, hi = abs(a - b) + 1, a + b - 1
    return Z(f'Zwei Seiten eines Dreiecks sind {a} cm und {b} cm lang. Wie viele verschiedene ganzzahlige Längen (in cm) sind für die dritte Seite möglich?', hi - lo + 1,
             f'({a} + {b} - 1) - (abs({a} - {b}) + 1) + 1', f'Möglich: {abs(a - b)} < c < {a + b}, also c = {lo}, …, {hi}. Das sind {hi - lo + 1} Längen.',
             'Bestimme die kleinste und die größte mögliche ganze Länge.')


def g_vierecke(R, st):
    if st == 1:
        al = R.choice(range(40, 141, 5))
        if al == 90: al = 75
        a = Z(f'In einem Parallelogramm ABCD ist α = {al}°. Wie groß ist β?', 180 - al, f'180 - {al}', f'Benachbarte Winkel ergänzen sich zu 180°: β = 180° − {al}° = {180 - al}°.',
              'Benachbarte Winkel im Parallelogramm ergeben zusammen 180°.', '°')
        dx = round(3 / math.tan(math.radians(al)), 2)
        a['f']['grafik'] = figur({'A': [0, 0], 'B': [5, 0], 'C': [5 + dx, 3], 'D': [dx, 3]}, linien=[['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A']], flaeche=['A', 'B', 'C', 'D'],
                                 winkel=[['A', 'B', 'D', f'{al}°'], ['B', 'C', 'A', 'β']])
        return a
    if st == 2:
        art = R.choice(['drachen', 'trapez', 'raute'])
        if art == 'drachen':
            a_, c_ = R.choice(range(50, 131, 5)), R.choice(range(30, 101, 5))
            b = Fr(360 - a_ - c_, 2)
            return Z(f'Ein Drachenviereck ABCD ist symmetrisch zur Diagonalen AC. Es ist α = {a_}° und γ = {c_}°. Wie groß ist β (= δ)?', b, f'(360 - {a_} - {c_}) / 2',
                     f'β = δ (liegen symmetrisch). 2β = 360° − {a_}° − {c_}° = {360 - a_ - c_}° → β = {zt(b)}°.', 'Winkelsumme im Viereck 360°, β und δ sind gleich.', '°')
        if art == 'trapez':
            al = R.choice(range(40, 86, 5))
            return Z(f'In einem gleichschenkligen Trapez ABCD (AB ∥ CD) ist α = {al}°. Wie groß ist γ?', 180 - al, f'180 - {al}',
                     f'β = α = {al}° (gleiche Winkel an der Grundseite AB). γ = 180° − β = {180 - al}° (Winkel an derselben Schenkelseite ergänzen sich zu 180°).', 'Winkel an einem Schenkel ergänzen sich zu 180°.', '°')
        al = R.choice(range(40, 141, 5))
        return Z(f'In einer Raute ABCD ist α = {al}°. Die Diagonale AC halbiert α. Wie groß ist der Winkel zwischen AC und der Seite AB?', Fr(al, 2), f'{al} / 2',
                 f'Die Diagonalen einer Raute sind Symmetrieachsen und halbieren die Winkel: {al}° : 2 = {zt(Fr(al, 2))}°.', 'Diagonalen einer Raute sind Winkelhalbierende.', '°')
    a_, b_, c_ = R.randint(60, 120), R.randint(60, 120), R.randint(60, 120)
    d = 360 - a_ - b_ - c_
    if d <= 0: return g_vierecke(R, st)
    return Z(f'In einem Viereck ist α = {a_}°, β = {b_}° und γ = {c_}°. Berechne δ.', d, f'360 - {a_} - {b_} - {c_}', f'δ = 360° − {a_}° − {b_}° − {c_}° = {d}°.',
             'Ein Viereck lässt sich in zwei Dreiecke zerlegen: 2 · 180° = 360°.', '°')


KEHR = [  # Satz, Kehrsatz, Kehrsatz wahr?, Gegenbeispiel
    ('Wenn ein Viereck ein Quadrat ist, dann hat es vier gleich lange Seiten.', 'Wenn ein Viereck vier gleich lange Seiten hat, dann ist es ein Quadrat.', False, 'eine Raute mit 60°-Winkel'),
    ('Wenn ein Dreieck gleichseitig ist, dann sind alle Winkel 60°.', 'Wenn in einem Dreieck alle Winkel 60° sind, dann ist es gleichseitig.', True, ''),
    ('Wenn ein Dreieck gleichschenklig ist, dann hat es zwei gleich große Winkel.', 'Wenn ein Dreieck zwei gleich große Winkel hat, dann ist es gleichschenklig.', True, ''),
    ('Wenn ein Viereck ein Rechteck ist, dann sind seine Diagonalen gleich lang.', 'Wenn die Diagonalen eines Vierecks gleich lang sind, dann ist es ein Rechteck.', False, 'ein gleichschenkliges Trapez'),
    ('Wenn ein Viereck eine Raute ist, dann stehen die Diagonalen senkrecht aufeinander.', 'Wenn die Diagonalen eines Vierecks senkrecht aufeinander stehen, dann ist es eine Raute.', False, 'ein Drachenviereck'),
    ('Wenn ein Viereck ein Parallelogramm ist, dann halbieren sich seine Diagonalen.', 'Wenn sich die Diagonalen eines Vierecks halbieren, dann ist es ein Parallelogramm.', True, ''),
    ('Wenn zwei Dreiecke kongruent sind, dann haben sie gleich große Winkel.', 'Wenn zwei Dreiecke gleich große Winkel haben, dann sind sie kongruent.', False, 'zwei verschieden große gleichseitige Dreiecke'),
    ('Wenn eine Zahl durch 4 teilbar ist, dann ist sie gerade.', 'Wenn eine Zahl gerade ist, dann ist sie durch 4 teilbar.', False, 'die Zahl 6'),
    ('Wenn ein Dreieck einen rechten Winkel hat, dann sind die beiden anderen Winkel zusammen 90°.', 'Wenn in einem Dreieck zwei Winkel zusammen 90° sind, dann hat es einen rechten Winkel.', True, ''),
    ('Wenn ein Viereck ein Rechteck ist, dann hat es vier rechte Winkel.', 'Wenn ein Viereck vier rechte Winkel hat, dann ist es ein Rechteck.', True, ''),
    ('Wenn eine Zahl durch 6 teilbar ist, dann ist sie durch 3 teilbar.', 'Wenn eine Zahl durch 3 teilbar ist, dann ist sie durch 6 teilbar.', False, 'die Zahl 9'),
    ('Wenn ein Viereck eine Raute ist, dann ist es ein Parallelogramm.', 'Wenn ein Viereck ein Parallelogramm ist, dann ist es eine Raute.', False, 'ein Parallelogramm mit den Seiten 3 cm und 6 cm'),
    ('Wenn ein Dreieck gleichseitig ist, dann ist es gleichschenklig.', 'Wenn ein Dreieck gleichschenklig ist, dann ist es gleichseitig.', False, 'ein Dreieck mit den Seiten 5 cm, 5 cm und 3 cm'),
    ('Wenn ein Viereck ein Quadrat ist, dann ist es ein Rechteck.', 'Wenn ein Viereck ein Rechteck ist, dann ist es ein Quadrat.', False, 'ein Rechteck 2 cm × 5 cm'),
]


def g_satz_kehrsatz(R, st):
    satz, kehr, wahr, gegen = R.choice(KEHR)
    if st == 2: st = R.choice([1, 2, 2, 3])
    if st == 1:
        andere = [k for s, k, _, _ in KEHR if k != kehr]
        return A(R, f'Wie lautet der Kehrsatz zu: „{satz}“', kehr, [satz] + R.sample(andere, 2), f'Voraussetzung und Behauptung werden vertauscht: „{kehr}“',
                 'Tausche den Wenn-Teil und den Dann-Teil.')
    if st == 2:
        r = 'Der Kehrsatz ist wahr.' if wahr else f'Der Kehrsatz ist falsch, Gegenbeispiel: {gegen}.'
        f = ['Der Kehrsatz ist wahr.'] if not wahr else []
        f += [f'Der Kehrsatz ist falsch, Gegenbeispiel: {g}.' for _, _, w, g in KEHR if g and g != gegen][:3 - len(f)]
        return A(R, f'Satz: „{satz}“ Ist der Kehrsatz „{kehr}“ wahr?', r, f, r, 'Suche ein Gegenbeispiel. Findest du keins, ist der Kehrsatz vermutlich wahr.')
    r = f'Nein: Bei {gegen} ist die Voraussetzung erfüllt, die Behauptung aber nicht.' if not wahr else 'Ja, der Kehrsatz gilt (ohne Gegenbeispiel).'
    if wahr:
        return A(R, f'Ein Schüler sagt: „Der Satz ‚{satz}‘ ist wahr, also ist auch der Kehrsatz wahr.“ Ist die Begründung richtig?', 'Nein: Die Begründung ist falsch, auch wenn der Kehrsatz hier zufällig stimmt.',
                 ['Ja, ein Kehrsatz ist immer wahr, wenn der Satz wahr ist.', 'Ja, weil man den Satz nur umdrehen muss.', 'Nein, denn der Satz selbst ist falsch.'],
                 'Aus der Wahrheit eines Satzes folgt nichts über den Kehrsatz; er muss eigens bewiesen werden.', 'Gibt es Sätze, deren Kehrsatz falsch ist?')
    return A(R, f'Widerlege den Kehrsatz: „{kehr}“ Welches Gegenbeispiel passt?', gegen[0].upper() + gegen[1:],
             [g[0].upper() + g[1:] for _, _, w, g in KEHR if g and g != gegen][:2] + ['ein Quadrat'] if 'Quadrat' not in kehr else [g[0].upper() + g[1:] for _, _, w, g in KEHR if g and g != gegen][:3],
             f'{gegen[0].upper() + gegen[1:]} erfüllt die Voraussetzung, aber nicht die Behauptung.', 'Das Gegenbeispiel muss den Wenn-Teil erfüllen, den Dann-Teil nicht.')


GEN = {'winkelsumme': g_winkelsumme, 'gleichschenklig': g_gleichschenklig, 'kongruenzsatz': g_kongruenzsatz, 'konstruierbar': g_konstruierbar,
       'vierecke': g_vierecke, 'satz_kehrsatz': g_satz_kehrsatz}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Winkel', ['winkelsumme', 'gleichschenklig', 'vierecke']), ('Kongruenz und Konstruktion', ['kongruenzsatz', 'konstruierbar']), ('Beweisen', ['satz_kehrsatz'])],
         'Winkel in Dreiecken und symmetrischen Vierecken berechnen, Kongruenzsätze anwenden, Konstruierbarkeit prüfen und zwischen Satz und Kehrsatz unterscheiden.',
         ['Winkelsumme: Dreieck 180°, Viereck 360°.', 'Gleichschenklig: Basiswinkel gleich.', 'Kongruenzsätze: SSS, SWS, WSW, SsW. WWW reicht nicht.',
          'Dreiecksungleichung: je zwei Seiten zusammen länger als die dritte.'],
         offen=['Konstruieren mit Zirkel und Lineal (Konstruktionsschritte, Planfigur, Ortslinien) kann die App nicht abfragen, weil das Kind nicht zeichnen kann. '
                'Gebaut wurden Winkelberechnungen mit Zeichnung, Kongruenzsätze, Konstruierbarkeit und Satz/Kehrsatz.',
                'Mittelsenkrechte und Winkelhalbierende als Ortslinien sind Stoff von geometrie.ortslinien (Klasse 5) und hier nicht wiederholt.'])
