#!/usr/bin/env python3
"""Thema funktionen.linear – Lineare Funktionen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, L, Z, baue, cz, eur, ist_endlich, kl, lin, zt  # noqa: E402

META = {'thema_schluessel': 'funktionen.linear', 'thema_id': 33, 'block_id': 72, 'klasse': {'gym_by': 8, 'rs_by': 8}}

ETAPPEN = [
    {'lernziel': 'ablesen', 'titel': 'Steigung m und Achsenabschnitt t',
     'regel': 'Der Graph von y = m · x + t ist eine ⟦Gerade⟧. ⟦m⟧ ist die Steigung: Gehst du 1 nach rechts, geht es m nach oben. ⟦t⟧ ist der y-Achsenabschnitt: Dort schneidet die Gerade die y-Achse.',
     'schritte': ['y = 5 − 2x umsortieren: y = −2x + 5', 'Steigung ⟦m = −2⟧ (fällt), y-Achsenabschnitt ⟦t = 5⟧', 'Schnittpunkt mit der y-Achse: (0 | 5)'],
     'fehler': 'Bei y = 5 − 2x ist m nicht 5. Die Steigung ist die Zahl ⟦vor dem x⟧, mit Vorzeichen: m = −2.',
     '_verbot': ['y = 5 − 2x']},
    {'lernziel': 'zwei_punkte', 'titel': 'Steigung aus zwei Punkten',
     'regel': 'Durch zwei Punkte P(x₁ | y₁) und Q(x₂ | y₂) geht genau eine Gerade. Ihre Steigung ist ⟦m = (y₂ − y₁) : (x₂ − x₁)⟧ („Höhenunterschied durch Längenunterschied“).',
     'schritte': ['P(1 | 3), Q(4 | 9)', 'm = (9 − 3) : (4 − 1) = 6 : 3', '⟦m = 2⟧'],
     'fehler': 'm = (4 − 1) : (9 − 3) = 0,5 ist falsch: Die ⟦y-Differenz⟧ gehört nach oben (in den Zähler), die x-Differenz nach unten.',
     '_verbot': ['P(1 | 3), Q(4 | 9)']},
    {'lernziel': 'aufstellen', 'titel': 'Geradengleichung aufstellen',
     'regel': 'Kennst du m und einen Punkt P(a | b), setzt du P in y = m · x + t ein und berechnest ⟦t = b − m · a⟧. Bei zwei Punkten berechnest du ⟦zuerst m⟧.',
     'schritte': ['m = 3, Punkt P(2 | 1)', '1 = 3 · 2 + t → t = 1 − 6 = −5', '⟦y = 3x − 5⟧'],
     'probe': '3 · 2 − 5 = 1 ✓',
     'fehler': 'Bei P(2 | 1) setzt man x = 2 und y = 1 ein – nicht umgekehrt. 2 = 3 · 1 + t führt zu ⟦t = −1⟧ und einer falschen Geraden.',
     '_verbot': ['P(2 | 1)']},
    {'lernziel': 'proportional', 'titel': 'Proportionalität: Ursprungsgerade',
     'regel': 'Bei einer ⟦direkten Proportionalität⟧ gilt y = k · x. Der Graph ist eine Gerade durch den ⟦Ursprung⟧ (t = 0). k ist der Proportionalitätsfaktor, z. B. der Preis pro Stück.',
     'schritte': ['3 kg Äpfel kosten 7,50 €.', 'k = 7,50 € : 3 kg = 2,50 € pro kg', '⟦y = 2,5 · x⟧, also kosten 8 kg 20 €.'],
     'fehler': 'y = 2x + 1 ist ⟦keine⟧ Proportionalität: Für x = 0 ist y = 1, die Gerade geht nicht durch den Ursprung. Verdoppelt man x, verdoppelt sich y nicht.',
     '_verbot': ['3 kg Äpfel kosten 7,50 €']},
    {'lernziel': 'schnittpunkte', 'titel': 'Schnittpunkte berechnen',
     'regel': 'Schnitt mit der ⟦x-Achse⟧: y = 0 setzen (Nullstelle). Schnitt mit der ⟦y-Achse⟧: x = 0, also (0 | t). Schnitt zweier Geraden: Terme ⟦gleichsetzen⟧.',
     'schritte': ['g: y = 2x − 1, h: y = −x + 5', '2x − 1 = −x + 5 → 3x = 6 → x = 2', 'y = 2 · 2 − 1 = 3: ⟦S(2 | 3)⟧'],
     'fehler': 'Der Schnittpunkt mit der x-Achse von y = 2x − 1 ist nicht (0 | −1). Das ist der Schnitt mit der ⟦y-Achse⟧. Für die x-Achse gilt y = 0: x = 0,5.',
     '_verbot': ['y = 2x − 1, h']},
    {'lernziel': 'lage', 'titel': 'Parallel oder senkrecht?',
     'regel': 'Gleiche Steigung (m₁ = m₂): Die Geraden sind ⟦parallel⟧. Ist ⟦m₁ · m₂ = −1⟧, stehen sie ⟦senkrecht⟧ aufeinander. Sonst schneiden sie sich schräg.',
     'schritte': ['g: y = 2x + 1, h: y = −0,5x + 3', 'm₁ · m₂ = 2 · (−0,5) = −1', '⟦g und h sind senkrecht zueinander.⟧'],
     'fehler': 'y = 2x + 1 und y = −2x + 1 stehen nicht senkrecht: 2 · (−2) = −4 ≠ −1. Für senkrecht braucht man den ⟦negativen Kehrwert⟧: −1/2.',
     '_verbot': ['y = −0,5x + 3']},
    {'lernziel': 'deuten', 'titel': 'Lineare Funktionen im Sachzusammenhang',
     'regel': 'In Anwendungen ist ⟦t der Startwert⟧ (bei x = 0) und ⟦m die Änderung pro Einheit⟧ von x. Ein negatives m heißt: Die Größe nimmt ab.',
     'schritte': ['Eine Kerze: h(x) = −1,5x + 20 (h in cm, x in Stunden)', 't = 20: Anfangs ist die Kerze 20 cm hoch. m = −1,5: Pro Stunde wird sie 1,5 cm kürzer.',
                  'Abgebrannt bei h = 0: 1,5x = 20 → ⟦x ≈ 13,3 h⟧'],
     'fehler': 'm = −1,5 heißt nicht, dass die Kerze 1,5 cm hoch ist. m ist eine ⟦Änderung⟧ pro Stunde, keine Höhe.',
     '_verbot': ['Kerze: h(x) = −1,5x + 20']},
]


def nz(R, lo=-6, hi=6):
    return R.choice([k for k in range(lo, hi + 1) if k])


def zufall_m(R, st):
    if st == 1: return Fr(nz(R, -6, 6))
    if st == 2: return Fr(nz(R, -8, 8), R.choice([1, 1, 2]))
    return Fr(nz(R, -9, 9), R.choice([2, 3, 4, 5]))


def g_ablesen(R, st):
    m = zufall_m(R, st)
    t = Fr(R.randint(-9, 9)) if st < 3 else Fr(R.randint(-20, 20), R.choice([1, 2]))
    if st == 1:
        G = f'y = {lin(m, t)}'
    elif st == 2:
        G = R.choice([f'y = {zt(t)} {"+" if m > 0 else "−"} {lin(abs(m), 0)}' if t else f'y = {lin(m, 0)}', f'y = {lin(m, t)}'])
    else:
        k = R.choice([2, 3, 4, -2])
        G = f'{zt(k) if k != -1 else "−"}y = {lin(k * m, k * t)}' if (k * m).denominator == 1 and (k * t).denominator == 1 else f'y = {lin(m, t)}'
    if not ist_endlich(m):
        frage = 't'
    else:
        frage = R.choice(['m', 't'])
    if frage == 'm':
        return Z(f'Gib die Steigung m der Geraden {G} an.', m, cz(m),
                 f'In der Form y = m · x + t: y = {lin(m, t)}. Steigung m = {zt(m)}.', 'Bringe die Gleichung in die Form y = m · x + t. m steht vor dem x.')
    return Z(f'Gib den y-Achsenabschnitt t der Geraden {G} an.', t, cz(t),
             f'In der Form y = m · x + t: y = {lin(m, t)}. y-Achsenabschnitt t = {zt(t)}.', 'Bringe die Gleichung in die Form y = m · x + t. t ist die Zahl ohne x.')


def g_zwei_punkte(R, st):
    while True:
        x1, x2 = R.sample(range(-6, 9), 2)
        if st == 1: m = Fr(nz(R, -5, 5))
        else: m = Fr(nz(R, -12, 12), R.choice([1, 2, 4, 5]))
        y1 = Fr(R.randint(-8, 8)); y2 = y1 + m * (x2 - x1)
        if st == 3: x1, x2 = Fr(x1, 2), Fr(x2, 2); y2 = y1 + m * (x2 - x1)
        if ist_endlich(m) and ist_endlich(y2) and len(zt(y2)) <= 6: break
    P, Q = f'P({zt(x1)} | {zt(y1)})', f'Q({zt(x2)} | {zt(y2)})'
    return Z(f'Berechne die Steigung der Geraden durch {P} und {Q}.', m, f'({cz(y2)} - ({cz(y1)})) / ({cz(x2)} - ({cz(x1)}))',
             f'm = ({zt(y2)} − {kl(y1)}) : ({zt(x2)} − {kl(x1)}) = {zt(y2 - y1)} : {kl(x2 - x1)} = {zt(m)}.',
             'm = (y₂ − y₁) : (x₂ − x₁). Achte auf negative Zahlen.')


def g_aufstellen(R, st):
    h = 'Bestimme m und t und tippe die Gerade als Term ein, z. B. 3x − 5.'
    m, t = nz(R, -5, 5), R.randint(-9, 9)
    if st == 1:
        text = f'Eine Gerade hat die Steigung {zt(m)} und schneidet die y-Achse bei {zt(t)}. Gib den Funktionsterm an.'
        weg = f'm = {zt(m)}, t = {zt(t)}: y = {lin(m, t)}.'
    elif st == 2:
        a = nz(R, -5, 5); b = m * a + t
        text = f'Eine Gerade hat die Steigung {zt(m)} und geht durch P({zt(a)} | {zt(b)}). Gib den Funktionsterm an.'
        weg = f'{zt(b)} = {zt(m)} · {kl(a)} + t → t = {zt(b)} − {kl(m * a)} = {zt(t)}. y = {lin(m, t)}.'
    else:
        a, c = R.sample(range(-5, 7), 2)
        b, d = m * a + t, m * c + t
        text = f'Eine Gerade geht durch P({zt(a)} | {zt(b)}) und Q({zt(c)} | {zt(d)}). Gib den Funktionsterm an.'
        weg = f'm = ({zt(d)} − {kl(b)}) : ({zt(c)} − {kl(a)}) = {zt(m)}. t = {zt(b)} − {kl(m)} · {kl(a)} = {zt(t)}. y = {lin(m, t)}.'
    return L(text, '□x + □', [m, t], [str(m), str(t)], weg, h, 'Tippe den Term ein, z. B. 3x − 5 oder −x + 2.')


def g_proportional(R, st):
    if st == 1:
        ware, einheit, k = R.choice([('Äpfel', 'kg', Fr(5, 2)), ('Kartoffeln', 'kg', Fr(6, 5)), ('Benzin', 'l', Fr(18, 10)), ('Stoff', 'm', Fr(8)),
                                     ('Kirschen', 'kg', Fr(9, 2)), ('Käse', 'kg', Fr(16)), ('Saft', 'l', Fr(3, 2))])
        x1 = R.choice([2, 3, 4, 5, 6]); x2 = R.choice([j for j in (1, 7, 8, 10, 12, 15, 20) if j != x1])
        return Z(f'{x1} {einheit} {ware} kosten {eur(k * x1)} €. Wie viel kosten {x2} {einheit}?', k * x2, f'{cz(k * x1)} / {x1} * {x2}',
                 f'k = {eur(k * x1)} : {x1} = {eur(k)} € pro {einheit}. y = {zt(k)} · {x2} = {eur(k * x2)} €.', 'Berechne zuerst den Preis für 1 Einheit (k).', einheit='€')
    if st == 2:
        k = Fr(nz(R, -9, 9), R.choice([1, 2, 4]))
        a = nz(R, -6, 6); b = k * a
        x2 = R.choice([j for j in range(-8, 13) if j not in (0, a)])
        return Z(f'Die Gerade y = k · x geht durch P({zt(a)} | {zt(b)}). Berechne y für x = {zt(x2)}.', k * x2, f'{cz(b)} / ({a}) * ({x2})',
                 f'k = {zt(b)} : {kl(a)} = {zt(k)}. y = {zt(k)} · {kl(x2)} = {zt(k * x2)}.', 'Berechne zuerst k = y : x.')
    # Stufe 3: Erkennen
    k = Fr(nz(R, 2, 9)); t = R.choice([0, 0, nz(R, -5, 5)])
    xs = sorted(R.sample(range(1, 10), 3))
    ps = ', '.join(f'({x} | {zt(k * x + t)})' for x in xs)
    if t == 0:
        r, f = f'Ja, y = {zt(k)} · x.', [f'Nein, die Gerade geht nicht durch den Ursprung.', f'Ja, y = {zt(k)} · x + {zt(k)}.', 'Nein, die Quotienten y : x sind verschieden.']
        w = f'Alle Quotienten y : x sind gleich {zt(k)}. Also proportional mit k = {zt(k)}.'
    else:
        r = 'Nein, die Quotienten y : x sind verschieden.'
        f = [f'Ja, y = {zt(k)} · x.', f'Ja, y = {zt(Fr(k * xs[0] + t, xs[0]))} · x.', 'Ja, weil y mit x wächst.']
        w = f'{zt(k * xs[0] + t)} : {xs[0]} = {zt(Fr(k * xs[0] + t, xs[0]))}, aber {zt(k * xs[1] + t)} : {xs[1]} = {zt(Fr(k * xs[1] + t, xs[1]))}. Nicht proportional (es gilt y = {lin(k, t)}).'
    return A(R, f'Ist die Zuordnung {ps} proportional?', r, f, w, 'Berechne für jedes Paar den Quotienten y : x.')


def g_schnittpunkte(R, st):
    if st == 1:
        while True:
            m = Fr(nz(R, -8, 8)); x0 = Fr(R.randint(-10, 10), R.choice([1, 2]))
            t = -m * x0
            if t.denominator == 1 and x0: break
        if R.random() < .4:
            return Z(f'An welcher Stelle schneidet y = {lin(m, t)} die y-Achse? Gib den y-Wert an.', t, cz(t),
                     f'Auf der y-Achse ist x = 0: y = {zt(m)} · 0 {"+" if t >= 0 else "−"} {abs(t)} = {zt(t)}.', 'Auf der y-Achse ist x = 0.')
        return Z(f'Berechne die Nullstelle von y = {lin(m, t)} (Schnitt mit der x-Achse).', x0, f'-({cz(t)}) / {cz(m)}',
                 f'{lin(m, t)} = 0 → x = {zt(x0)}.', 'Auf der x-Achse ist y = 0.')
    while True:
        m1, m2 = Fr(nz(R, -5, 5)), Fr(nz(R, -5, 5))
        if st == 3: m1, m2 = m1 / R.choice([1, 2]), m2 / R.choice([1, 2])
        if m1 == m2: continue
        x = Fr(R.randint(-6, 6)); t1 = Fr(R.randint(-8, 8)); y = m1 * x + t1; t2 = y - m2 * x
        if t2.denominator == 1 and abs(t2) <= 20: break
    g, h = f'g: y = {lin(m1, t1)}', f'h: y = {lin(m2, t2)}'
    weg = f'{lin(m1, t1)} = {lin(m2, t2)} → {lin(m1 - m2, 0)} = {zt(t2 - t1)} → x = {zt(x)}; y = {zt(y)}. S({zt(x)} | {zt(y)}).'
    if R.random() < .5:
        return Z(f'Berechne den Schnittpunkt S von {g} und {h}. Gib die x-Koordinate an.', x, f'({cz(t2)} - ({cz(t1)})) / ({cz(m1)} - ({cz(m2)}))', weg,
                 'Setze die beiden Terme gleich.')
    return Z(f'Berechne den Schnittpunkt S von {g} und {h}. Gib die y-Koordinate an.', y,
             f'{cz(m1)} * ({cz(t2)} - ({cz(t1)})) / ({cz(m1)} - ({cz(m2)})) + ({cz(t1)})', weg, 'Setze gleich, berechne x und setze x in eine der Gleichungen ein.')


LAGE = ['parallel', 'senkrecht zueinander', 'schneiden sich, aber nicht senkrecht', 'identisch (dieselbe Gerade)']


def g_lage(R, st):
    if st == 3 and R.random() < .55:
        m = Fr(nz(R, -6, 6), R.choice([1, 2, 4, 5]))
        if not ist_endlich(-1 / m): m = Fr(nz(R, -5, 5))
        welche = R.choice(['senkrecht', 'parallel'])
        if welche == 'parallel':
            return Z(f'Gib die Steigung einer Geraden an, die parallel zu y = {lin(m, R.randint(-9, 9))} ist.', m, cz(m),
                     f'Parallele Geraden haben dieselbe Steigung: m = {zt(m)}.', 'Parallel heißt: gleiche Steigung.')
        return Z(f'Gib die Steigung einer Geraden an, die senkrecht auf y = {lin(m, R.randint(-9, 9))} steht.', -1 / m, f'-1 / {cz(m)}',
                 f'm₂ = −1 : m₁ = −1 : {kl(m)} = {zt(-1 / m)}. Probe: {zt(m)} · {kl(-1 / m)} = −1.', 'Senkrecht: m₁ · m₂ = −1. Nimm den negativen Kehrwert.')
    art = R.choice(LAGE[:3] + ([LAGE[3]] if st >= 2 else []))
    m1 = Fr(nz(R, -5, 5), R.choice([1, 2])) if st > 1 else Fr(nz(R, -5, 5))
    t1 = R.randint(-6, 6)
    if art == 'parallel': m2, t2 = m1, t1 + nz(R, -5, 5)
    elif art.startswith('senkrecht'): m2, t2 = -1 / m1, R.randint(-6, 6)
    elif art.startswith('identisch'): m2, t2 = m1, t1
    else:
        m2 = R.choice([x for x in (-m1, m1 + 1, 2 * m1, Fr(1) / m1) if x != m1 and x * m1 != -1])
        t2 = R.randint(-6, 6)
    if not ist_endlich(m2): return g_lage(R, st)
    G2 = f'y = {lin(m2, t2)}'
    if art.startswith('identisch'):
        G2 = f'{2}y = {lin(2 * m2, 2 * t2)}' if (2 * m2).denominator == 1 else f'y − {lin(m2, 0)} = {zt(t2)}'
    grund = {'parallel': f'Gleiche Steigung {zt(m1)}, verschiedene y-Achsenabschnitte.', 'senkrecht zueinander': f'Produkt der Steigungen: {zt(m1)} · {kl(m2)} = −1.',
             'schneiden sich, aber nicht senkrecht': f'Verschiedene Steigungen, und {zt(m1)} · {kl(m2)} = {zt(m1 * m2)} ≠ −1.',
             'identisch (dieselbe Gerade)': f'Umgeformt ist die zweite Gleichung y = {lin(m2, t2)} – genau die erste Gerade.'}[art]
    return A(R, f'Wie liegen die Geraden g: y = {lin(m1, t1)} und h: {G2} zueinander?', art, [x for x in LAGE if x != art][:3] if st >= 2 else [x for x in LAGE[:3] if x != art] + [LAGE[3]],
             grund, 'Bringe beide Gleichungen in die Form y = m · x + t und vergleiche die Steigungen.')


def g_deuten(R, st):
    kontext = R.choice(['kerze', 'tank', 'handy', 'taxi', 'pool'])
    if kontext == 'kerze':
        intro = 'Eine Kerze brennt ab:'
        h0, r = R.choice([15, 18, 20, 24, 25, 30]), Fr(R.choice([5, 10, 15, 20, 25, 30]), 10)
        f, x, y = f'h(x) = −{zt(r)}x + {h0}', 'x in Stunden', 'h in cm'
        bed_m, bed_t = f'Die Kerze wird pro Stunde {zt(r)} cm kürzer.', f'Die Kerze ist am Anfang {h0} cm hoch.'
        frage_null, null = 'Nach wie vielen Stunden ist die Kerze abgebrannt?', Fr(h0) / r
        m, t = -r, h0
    elif kontext == 'tank':
        intro = 'Ein Auto fährt, der Tankinhalt sinkt:'
        h0, r = R.choice([40, 45, 50, 60]), Fr(R.choice([5, 6, 8, 10, 15]), 2)
        f, x, y = f'V(x) = −{zt(r)}x + {h0}', 'x in Stunden Fahrt', 'V in Litern'
        bed_m, bed_t = f'Pro Stunde Fahrt werden {zt(r)} Liter verbraucht.', f'Am Anfang sind {h0} Liter im Tank.'
        frage_null, null = 'Nach wie vielen Stunden ist der Tank leer?', Fr(h0) / r
        m, t = -r, h0
    elif kontext == 'handy':
        intro = 'Ein Handytarif:'
        g, p = R.choice([5, 8, 10, 12]), Fr(R.choice([5, 9, 10, 15, 20]), 100)
        f, x, y = f'K(x) = {zt(p)}x + {g}', 'x in Minuten', 'K in €'
        bed_m, bed_t = f'Jede Minute kostet {eur(p)} €.', f'Die Grundgebühr beträgt {g} €.'
        B = g + p * R.choice([20, 40, 50, 60, 100])
        frage_null, null = f'Wie viele Minuten wurde telefoniert, wenn {eur(B)} € zu zahlen sind?', (B - g) / p
        m, t = p, g
    elif kontext == 'taxi':
        intro = 'Eine Taxifahrt:'
        g, p = Fr(R.choice([7, 8, 9]), 2), Fr(R.choice([18, 20, 22, 24, 25]), 10)
        f, x, y = f'P(x) = {zt(p)}x + {zt(g)}', 'x in km', 'P in €'
        bed_m, bed_t = f'Jeder Kilometer kostet {eur(p)} €.', f'Der Grundpreis beträgt {eur(g)} €.'
        km = R.choice([4, 5, 8, 10, 12, 15])
        frage_null, null = f'Wie weit ist man gefahren, wenn {eur(g + p * km)} € zu zahlen sind?', Fr(km)
        m, t = p, g
    else:
        intro = 'Ein Pool wird befüllt:'
        h0, r = R.choice([10, 20, 30, 40]), Fr(R.choice([2, 4, 5, 8, 10]), 10)
        f, x, y = f'h(x) = {zt(r)}x + {h0}', 'x in Minuten', 'h in cm'
        bed_m, bed_t = f'Der Wasserstand steigt pro Minute um {zt(r)} cm.', f'Am Anfang steht das Wasser {h0} cm hoch.'
        Ziel = h0 + r * R.choice([50, 100, 150, 200])
        frage_null, null = f'Nach wie vielen Minuten steht das Wasser {zt(Ziel)} cm hoch?', (Ziel - h0) / r
        m, t = r, h0
    if st == 1:
        welche = R.choice(['m', 't'])
        if welche == 'm':
            return A(R, f'{intro} {f} ({x}, {y}). Was bedeutet die Steigung {zt(m)}?', bed_m, [bed_t, f'Nach {zt(abs(m))} Stunden ist der Vorgang vorbei.' if kontext in ('kerze', 'tank') else f'Man muss mindestens {zt(abs(m))} bezahlen.', 'Die Steigung hat hier keine Bedeutung.'],
                     f'm = {zt(m)} ist die Änderung von y, wenn x um 1 wächst. {bed_m}', 'Die Steigung ist die Änderung pro Einheit von x.')
        return A(R, f'{intro} {f} ({x}, {y}). Was bedeutet die Zahl {zt(t)}?', bed_t, [bed_m, 'Es ist der Wert am Ende.', 'Es ist die Nullstelle.'],
                 f't = {zt(t)} ist der Wert für x = 0, also zu Beginn. {bed_t}', 't ist der Wert bei x = 0.')
    if st == 2 or ist_endlich(null) and R.random() < .6:
        if not ist_endlich(null):
            return Z(f'{intro} {f} ({x}, {y}). Berechne den Wert für x = 4.', m * 4 + t, f'{cz(m)} * 4 + {cz(t)}',
                     f'{zt(m)} · 4 + {zt(t)} = {zt(m * 4 + t)}.', 'Setze x = 4 ein.')
        return Z(f'{intro} {f} ({x}, {y}). {frage_null}', null, f'({cz(null * m + t)} - {cz(t)}) / {cz(m)}',
                 f'{lin(m, t)} = {zt(m * null + t)} → {lin(m, 0)} = {zt(m * null)} → x = {zt(null)}.', 'Setze den Funktionsterm gleich dem gesuchten Wert und löse nach x.')
    aussagen_w = [bed_m, bed_t]
    aussagen_f = [f'Der Graph ist eine Ursprungsgerade.', f'Die Steigung ist {zt(t)}.', f'Für x = 1 ist der Wert {zt(t)}.', f'Der Wert ändert sich pro Einheit von x um {zt(t)}.']
    r_ = R.choice(aussagen_w)
    return A(R, f'{intro} {f} ({x}, {y}). Welche Aussage ist richtig?', r_, R.sample(aussagen_f, 3),
             f'{r_} Denn m = {zt(m)} ist die Änderung pro Einheit, t = {zt(t)} der Anfangswert.', 'Ordne m und t ihre Bedeutung zu.')


GEN = {'ablesen': g_ablesen, 'zwei_punkte': g_zwei_punkte, 'aufstellen': g_aufstellen, 'proportional': g_proportional,
       'schnittpunkte': g_schnittpunkte, 'lage': g_lage, 'deuten': g_deuten}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Steigung und Achsenabschnitt', ['ablesen', 'zwei_punkte', 'proportional']), ('Geraden bestimmen', ['aufstellen', 'schnittpunkte', 'lage']),
          ('Anwenden', ['deuten'])],
         'Lineare Funktionen y = m · x + t deuten, Geradengleichungen aufstellen, Schnittpunkte und Lage von Geraden bestimmen.',
         ['m = Steigung (Änderung pro 1 nach rechts), t = y-Achsenabschnitt.', 'm = (y₂ − y₁) : (x₂ − x₁).',
          'Parallel: m₁ = m₂. Senkrecht: m₁ · m₂ = −1.', 'Proportional: y = k · x, Gerade durch den Ursprung.'],
         offen=['Lehrplan: Graphen zeichnen und Parameter am Graphen ablesen (Steigungsdreieck). Die App kann noch kein Koordinatensystem mit Geraden zeichnen; '
                'alle Aufgaben arbeiten mit Termen und Punkten.'])
