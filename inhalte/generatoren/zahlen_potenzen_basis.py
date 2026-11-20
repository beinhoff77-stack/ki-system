#!/usr/bin/env python3
"""Potenzen als Schreibweise (Gymnasium Kl. 5): Potenz lesen/schreiben, berechnen, Quadratzahlen bis 400,
Zehnerpotenzen für große Zahlen, negative Basis, Sachanwendungen. Keine Potenzgesetze (Kl. 6)."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl5 import baue, kl, mische, mische_rund, schreibe, zt  # noqa: E402

R = random.Random(67)
HOCH = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')
hoch = lambda b, e: f'{kl(b) if b < 0 else zt(b)}{str(e).translate(HOCH)}'
mal = lambda b, e: ' · '.join([kl(b)] * e)

# Erklärungen: Fassung der Prüfung (inhalte/pruefung/erklaerungen/zahlen.potenzen_basis.json) übernommen.
ETAPPEN = [
    {
        "lernziel": "schreibweise",
        "titel": "Was ist eine Potenz?",
        "regel": "Eine Potenz ist eine Kurzschreibweise für ⟦mehrmals dieselbe Zahl malnehmen⟧: 3 · 3 · 3 · 3 = 3⁴. Die ⟦Basis⟧ 3 ist der Faktor, der ⟦Exponent⟧ 4 sagt, wie oft er dasteht.",
        "schritte": [
            "5 · 5 · 5: Der Faktor 5 steht 3-mal da.",
            "Basis 5, Exponent 3: ⟦5³⟧. Man liest „5 hoch 3“."
        ],
        "fehler": "3⁴ ist nicht 3 · 4. Der Exponent zählt, ⟦wie oft⟧ die 3 als Faktor dasteht: 3 · 3 · 3 · 3."
    },
    {
        "lernziel": "berechnen",
        "titel": "Potenzen ausrechnen",
        "regel": "Schreibe die Potenz als Produkt und rechne ⟦Schritt für Schritt⟧ von links nach rechts.",
        "schritte": [
            "2⁵ = 2 · 2 · 2 · 2 · 2",
            "2 · 2 = 4, · 2 = 8, · 2 = 16, · 2 = ⟦32⟧"
        ],
        "probe": "32 : 2 = 16, : 2 = 8, : 2 = 4, : 2 = 2 ✓",
        "fehler": "2⁵ = 10 ist falsch: Das wäre 2 · 5. Richtig ist 2 · 2 · 2 · 2 · 2 = ⟦32⟧."
    },
    {
        "lernziel": "quadrat",
        "titel": "Quadratzahlen bis 400",
        "regel": "„Hoch 2“ heißt ⟦Quadrat⟧: die Zahl mal sich selbst. Der Name kommt vom Quadrat: Ein Quadrat mit 14 Fliesen pro Reihe und 14 Reihen hat 14 · 14 = 14² Fliesen. Die Quadratzahlen von 1² bis 20² solltest du auswendig können: … 11² = 121, 12² = 144, 13² = 169, 14² = 196, 15² = 225, 16² = 256, 17² = 289, 18² = 324, 19² = 361, 20² = 400.",
        "schritte": [
            "Ein quadratischer Badboden hat 14 Fliesen pro Reihe und 14 Reihen. Das sind 14² Fliesen.",
            "Zerlege: 14 · 10 = 140 und 14 · 4 = 56.",
            "Zusammen: 140 + 56 = ⟦196⟧ Fliesen."
        ],
        "fehler": "14² = 28 ist falsch: Das wäre 14 · 2. Quadrat heißt 14 · ⟦14⟧. Denk an die Fliesen: 14 Reihen mit je 14 Fliesen sind viel mehr als 28.",
        "probe": "Nachbar-Trick: 15² = 225. Vom Quadrat mit 14 · 14 Fliesen zum Quadrat mit 15 · 15 kommen eine Reihe und eine Spalte dazu, also 14 + 15 = 29 Fliesen. 196 + 29 = 225 ✓"
    },
    {
        "lernziel": "vertauschen",
        "titel": "Basis und Exponent nicht vertauschen",
        "regel": "Bei Potenzen darf man Basis und Exponent ⟦nicht vertauschen⟧: 2³ = 8, aber 3² = 9.",
        "schritte": [
            "2³ = 2 · 2 · 2 = 8",
            "3² = 3 · 3 = 9",
            "Also ist ⟦3² größer⟧ als 2³."
        ],
        "fehler": "Bei 3 · 4 = 4 · 3 darf man tauschen. Bei Potenzen nicht: 2⁵ = 32, aber 5² = ⟦25⟧."
    },
    {
        "lernziel": "zehner",
        "titel": "Zehnerpotenzen für große Zahlen",
        "regel": "Bei Zehnerpotenzen sagt der Exponent, ⟦wie viele Nullen⟧ die Zahl hat: 10³ = 1 000, 10⁶ = 1 000 000. Große Zahlen schreibt man kurz als Produkt: 3 · 10⁵ = 300 000.",
        "schritte": [
            "Ein großes Fußballstadion hat rund 7 · 10⁴ Plätze.",
            "10⁴ ist eine 1 mit 4 Nullen: 10 000.",
            "7 · 10 000 = ⟦70 000⟧ Plätze."
        ],
        "fehler": "7 · 10⁴ = 700 000 ist falsch: Hinter die 7 kommen genau ⟦4⟧ Nullen, also 70 000. Und 10⁴ ist nicht 40: 10⁴ = 10 · 10 · 10 · 10 = ⟦10 000⟧."
    },
    {
        "lernziel": "negativ",
        "titel": "Potenzen mit negativer Basis",
        "regel": "Steht eine negative Zahl ⟦in Klammern⟧, wird sie samt Minus malgenommen. Je zwei Minus-Faktoren ergeben zusammen Plus. Gerader Exponent: Alle Minus finden einen Partner, das Ergebnis ist ⟦positiv⟧. Ungerader Exponent: Ein Minus bleibt übrig, das Ergebnis ist ⟦negativ⟧.",
        "schritte": [
            "(−2)³ = (−2) · (−2) · (−2)",
            "(−2) · (−2) = 4, dann 4 · (−2) = ⟦−8⟧. Ein Minus ist übrig geblieben."
        ],
        "probe": "(−2)² = (−2) · (−2) = 4: zwei Minus, ein Paar, positiv ✓",
        "fehler": "−3² und (−3)² verwechseln. In (−3)² ist die −3 die Basis: (−3) · (−3) = ⟦9⟧. In −3² ohne Klammer gehört nur die 3 zur Basis: −3² = −(3 · 3) = ⟦−9⟧."
    },
    {
        "lernziel": "sach",
        "titel": "Potenzen im Alltag",
        "regel": "Wenn sich etwas immer wieder ⟦verdoppelt, verdreifacht oder verzehnfacht⟧, hilft eine Potenz: nach 5 Verdopplungen hat man 2⁵-mal so viel.",
        "schritte": [
            "Ein Blatt wird 4-mal gefaltet. Jedes Falten verdoppelt die Lagen.",
            "2 · 2 · 2 · 2 = 2⁴ = ⟦16⟧ Lagen"
        ],
        "fehler": "4-mal verdoppeln ist nicht „mal 8“ (4 · 2). Es ist 2 · 2 · 2 · 2 = ⟦16⟧-mal so viel."
    }
]


def _fliesen(n=14):
    """Fliesenquadrat n · n als Figur: Rand, Gitter gestrichelt, Seiten beschriftet (Hilfspunkte ohne Namen)."""
    P = {'_A': [0, 0], '_B': [n, 0], '_C': [n, n], '_D': [0, n]}
    L = [['_A', '_B', f'{n} Fliesen'], ['_B', '_C'], ['_C', '_D'], ['_D', '_A', f'{n} Fliesen']]
    for i in range(1, n):
        P[f'_x{i}u'], P[f'_x{i}o'], P[f'_y{i}l'], P[f'_y{i}r'] = [i, 0], [i, n], [0, i], [n, i]
        L += [[f'_x{i}u', f'_x{i}o', None, 'gestrichelt'], [f'_y{i}l', f'_y{i}r', None, 'gestrichelt']]
    return {'typ': 'figur', 'punkte': P, 'flaeche': ['_A', '_B', '_C', '_D'], 'linien': L}


next(e for e in ETAPPEN if e['lernziel'] == 'quadrat')['bild'] = _fliesen(14)   # Prüfung: Bild zum Fliesenquadrat fehlte
TEIL = {'schreibweise': 'begriff', 'berechnen': 'berechnen', 'quadrat': 'berechnen', 'vertauschen': 'begriff', 'zehner': 'zehner', 'negativ': 'negativ', 'sach': 'anwenden'}




def _ber_rechnen(s):
    b, e = R.choice({1: [(2, 3), (2, 4), (3, 3), (4, 3), (5, 3), (1, 5), (1, 8), (10, 3), (2, 5)],
                     2: [(2, 6), (2, 7), (3, 4), (4, 4), (5, 4), (6, 3), (7, 3), (8, 3), (9, 3), (2, 8), (3, 5), (10, 4), (1, 20), (10, 5), (30, 2), (40, 2), (25, 2), (50, 2), (3, 6), (20, 3)],
                     3: [(2, 9), (2, 10), (4, 5), (5, 5), (6, 4), (7, 4), (11, 3), (12, 3), (15, 3), (30, 3), (2, 11), (2, 12), (3, 7), (8, 4), (9, 4)]}[s])
    zw, t = b, []
    for _ in range(e - 1): t.append(f'{zt(zw)} · {b} = {zt(zw * b)}'); zw *= b
    return {'y': 'zahl', 'f': {'text': f'Berechne {hoch(b, e)}.'}, 'o': {'wert': b ** e}, 'c': f'{b}**{e}',
            'w': f'{hoch(b, e)} = {mal(b, e)}. Schritt für Schritt: {", ".join(t)}.', 'h': 'Schreibe die Potenz als Produkt und rechne von links nach rechts.'}












# ---------- Prüfung eingearbeitet (inhalte/pruefung/aufgaben/zahlen.potenzen_basis.json) ----------
def _rund(r, f): return mische_rund(R, r, f)


ZAEHL = {'benennen': 0}
PAARE = {1: [(2, 3), (2, 5), (3, 4), (2, 6), (3, 5)],
         2: [(2, 7), (2, 8), (3, 6), (4, 5), (2, 9), (3, 7)],
         3: [(4, 6), (3, 8), (5, 6), (4, 7), (3, 9)]}
BENUTZT = set()      # jedes Paar höchstens einmal als Vergleich/Unterschied (auch vertauscht)


def g_schreibweise(s):
    b, e = R.randint(2, 12), R.randint(2, 6)
    if s == 1:
        if R.random() < .3:
            n = R.randint(2, 40)
            return {'y': 'zahl', 'f': {'text': f'Berechne {hoch(n, 1)}.'}, 'o': {'wert': n}, 'c': f'{n}**1',
                    'w': f'Der Exponent 1 sagt: Die {n} steht einmal als Faktor da. Also {hoch(n, 1)} = {n}.', 'h': 'Wie oft steht die Basis als Faktor da?'}
        a, i = _rund(hoch(b, e), [hoch(e, b) if e != b else hoch(b, e + 1), f'{b} · {e}'])
        return {'y': 'auswahl', 'f': {'text': f'Schreibe als Potenz: {mal(b, e)}'}, 'a': a, 'o': {'index': i},
                'w': f'Der Faktor {b} steht {e}-mal da. Basis {b}, Exponent {e}: {hoch(b, e)}.', 'h': 'Zähle, wie oft der Faktor dasteht. Das ist der Exponent.'}
    if s == 2:
        art = R.choice(['benennen', 'eins', 'finden'])
        if art == 'benennen' and ZAEHL['benennen'] < 6:
            if e == b: return g_schreibweise(s)
            ZAEHL['benennen'] += 1
            was = R.choice(['Basis', 'Exponent'])
            return {'y': 'zahl', 'f': {'text': f'Wie heißt {"die Basis" if was == "Basis" else "der Exponent"} der Potenz {hoch(b, e)}?'}, 'o': {'wert': b if was == 'Basis' else e},
                    'c': str(b if was == 'Basis' else e), 'w': f'In {hoch(b, e)} ist {b} die Basis (unten, der Faktor) und {e} der Exponent (oben, die Anzahl).',
                    'h': 'Die Basis steht unten, der Exponent klein oben.'}
        if art == 'eins' or art == 'benennen':
            n = R.randint(3, 30)
            if n == 10: return g_schreibweise(s)
            a, i = _rund(hoch(n, 1), [hoch(n, 0), hoch(1, n)])
            return {'y': 'auswahl', 'f': {'text': f'Schreibe {n} als Potenz mit der Basis {n}.'}, 'a': a, 'o': {'index': i},
                    'w': f'Die {n} steht einmal als Faktor da: {n} = {hoch(n, 1)}. {hoch(1, n)} wäre 1 · 1 · … · 1 = 1.', 'h': 'Wie oft steht die Basis als Faktor da?'}
    b, e = R.choice([(2, R.randint(3, 8)), (3, R.randint(2, 5)), (4, R.randint(2, 4)), (5, R.randint(2, 4)), (10, R.randint(3, 7))])
    if s == 3 and R.random() < .5:
        if e == b: return g_schreibweise(s)
        a, i = _rund(mal(b, e), [mal(e, b), f'{b} · {e}', ' + '.join([str(b)] * e)])
        return {'y': 'auswahl', 'f': {'text': f'Was bedeutet {hoch(b, e)}?'}, 'a': a, 'o': {'index': i},
                'w': f'{hoch(b, e)} heißt: {b} steht {e}-mal als Faktor da, also {mal(b, e)}.', 'h': 'Der Exponent sagt, wie oft die Basis als Faktor dasteht.'}
    return {'y': 'zahl', 'f': {'text': f'{b} hoch wie viel ergibt {zt(b ** e)}?'}, 'o': {'wert': e}, 'c': str(e),
            'w': f'Immer wieder mal {b}: ' + ', '.join(zt(b ** k) for k in range(1, e + 1)) + f'. Das sind {e} Faktoren, also {hoch(b, e)} = {zt(b ** e)}.',
            'h': f'Nimm {b} so oft mal {b}, bis die Zahl erreicht ist. Zähle die Faktoren.'}


def _ber_fehler():
    b, e = R.choice([(4, 3), (5, 2), (3, 4), (2, 5), (6, 2), (5, 3), (2, 6), (3, 3), (7, 2), (10, 3), (8, 2), (9, 2), (2, 4), (4, 2)])
    falsch = b * e
    if falsch == b ** e: return _ber_fehler()
    r = f'Es wurde {b} · {e} gerechnet. Richtig ist {mal(b, e)} = {zt(b ** e)}.'
    f = ['Das ist richtig gerechnet.', f'Richtig ist {mal(e, b)} = {zt(e ** b)}.']
    if e ** b == b ** e or e ** b > 1000: f[1] = f'Richtig ist {b} + {e} = {b + e}.'
    aw, i = _rund(r, f)
    return {'y': 'auswahl', 'f': {'text': f'Jemand rechnet {hoch(b, e)} = {falsch}. Was ist falsch?'}, 'a': aw, 'o': {'index': i},
            'w': f'Der Exponent {e} zählt die Faktoren: {mal(b, e)} = {zt(b ** e)}. {b} · {e} = {falsch} ist etwas anderes.',
            'h': 'Was bedeutet der Exponent?'}


def g_berechnen(s):
    if s == 3 and R.random() < .4: return _ber_fehler()
    if s == 2 and R.random() < .2: return _ber_fehler()
    return _ber_rechnen(s)


def g_quadrat(s):
    n = R.randint(2, 12) if s == 1 else R.randint(11, 20)
    if s == 1 or (s == 2 and R.random() < .6):
        return {'y': 'zahl', 'f': {'text': f'Berechne {hoch(n, 2)}.'}, 'o': {'wert': n * n}, 'c': f'{n}**2',
                'w': f'{hoch(n, 2)} = {n} · {n} = {n * n}.', 'h': 'Hoch 2 heißt: die Zahl mal sich selbst.'}
    if s == 2:
        return {'y': 'zahl', 'f': {'text': f'Welche natürliche Zahl ergibt im Quadrat {n * n}?'}, 'o': {'wert': n}, 'c': str(n),
                'w': f'Gesucht ist die Zahl, die mit sich selbst malgenommen {n * n} ergibt: {n} · {n} = {n * n}.',
                'h': f'Welche Zahl mal sich selbst ergibt {n * n}? Beginne bei einer Zahl, deren Quadrat du kennst, und probiere weiter.'}
    art = R.choice(['zwischen', 'summe', 'ist', 'wieviele'])
    if art == 'wieviele':
        u = R.randint(2, 30) * 10; o = u + R.choice([50, 100, 150])
        if o > 400: return g_quadrat(s)
        q = [k * k for k in range(1, 21) if u < k * k < o]
        return {'y': 'zahl', 'f': {'text': f'Wie viele Quadratzahlen liegen zwischen {u} und {o}?'}, 'o': {'wert': len(q)}, 'c': str(len(q)),
                'w': f'Zwischen {u} und {o} liegen: {", ".join(map(str, q)) if q else "keine"}. Das sind {len(q)}.',
                'h': 'Schreibe die Quadratzahlen der Reihe nach auf und zähle, welche dazwischen liegen.'}
    if art == 'summe':
        m = R.randint(2, 12)
        return {'y': 'zahl', 'f': {'text': f'Berechne {hoch(n, 2)} − {hoch(m, 2)}.'}, 'o': {'wert': n * n - m * m}, 'c': f'{n}**2 - {m}**2',
                'w': f'Erst die Quadrate: {hoch(n, 2)} = {n * n} und {hoch(m, 2)} = {m * m}. Dann {n * n} − {m * m} = {n * n - m * m}.', 'h': 'Rechne zuerst beide Quadrate aus, dann die Differenz.'}
    if art == 'zwischen':
        return {'y': 'zahl', 'f': {'text': f'Welche Quadratzahl liegt zwischen {n * n - R.randint(3, 9)} und {n * n + R.randint(3, 9)}?'}, 'o': {'wert': n * n}, 'c': f'{n}**2',
                'w': f'In diesem Bereich liegt {n} · {n} = {n * n}. Die Nachbarn {(n - 1) ** 2} und {(n + 1) ** 2} liegen außerhalb.', 'h': 'Gehe die Quadratzahlen der Reihe nach durch.'}
    k = n * n
    ist_q = lambda x: int(round(x ** .5)) ** 2 == x
    falsch = [k + R.choice([-2, -1, 1, 2, 3]), 2 * k // n]          # Nachbar einer Quadratzahl, Doppeltes statt Quadrat (n · 2)
    if any(ist_q(f) for f in falsch) or len(set(falsch + [k])) < 3: return g_quadrat(s)
    a, i = _rund(zt(k), [zt(f) for f in falsch])
    return {'y': 'auswahl', 'f': {'text': 'Welche Zahl ist eine Quadratzahl?'}, 'a': a, 'o': {'index': i},
            'w': f'{k} = {n} · {n} = {hoch(n, 2)}. {2 * n} wäre {n} · 2, nicht {n} · {n}. {falsch[0]} liegt neben {k}, ist aber selbst kein Quadrat.', 'h': 'Eine Quadratzahl ist eine Zahl mal sich selbst.'}


def _vergleich(b, e):
    x, y = b ** e, e ** b
    if x == y: r, f = 'Beide sind gleich groß', [f'{hoch(b, e)} ist größer', f'{hoch(e, b)} ist größer']
    else:
        gr, kl_ = (hoch(b, e), hoch(e, b)) if x > y else (hoch(e, b), hoch(b, e))
        r, f = f'{gr} ist größer', [f'{kl_} ist größer', 'Beide sind gleich groß']
    a, i = _rund(r, f)
    return {'y': 'auswahl', 'f': {'text': f'Vergleiche {hoch(b, e)} und {hoch(e, b)}. Was stimmt?'}, 'a': a, 'o': {'index': i},
            'w': f'{hoch(b, e)} = {zt(x)} und {hoch(e, b)} = {zt(y)}. ' + ('Hier sind beide gleich – das ist ein seltener Sonderfall.' if x == y else f'Also: {r}.'),
            'h': 'Rechne beide Potenzen aus und vergleiche.'}


def _behauptung():
    k, m = R.randint(3, 10), R.randint(3, 8)
    x, y = 2 ** m, k * k
    if x == y: return _behauptung()
    text = f'Jemand sagt: {hoch(2, m)} ist größer als {hoch(k, 2)}, weil {m} der größere Exponent ist. Stimmt das?'
    if x < y: r, f = f'Nein: {hoch(2, m)} = {x}, aber {hoch(k, 2)} = {y}.', ['Ja, der größere Exponent ergibt immer die größere Zahl.', 'Man kann die beiden nicht vergleichen.']
    else: r, f = f'Die Aussage stimmt ({x} > {y}), aber die Begründung nicht: Es kommt auch auf die Basis an.', ['Ja, der größere Exponent ergibt immer die größere Zahl.', f'Nein, {hoch(k, 2)} ist größer.']
    a, i = _rund(r, f)
    return {'y': 'auswahl', 'f': {'text': text}, 'a': a, 'o': {'index': i},
            'w': f'{hoch(2, m)} = {x} und {hoch(k, 2)} = {y}. Ob eine Potenz größer ist, hängt von Basis und Exponent ab – nur ausrechnen hilft.',
            'h': 'Rechne beide Potenzen aus.'}


def _gleiches_paar():
    f = R.sample([f'{hoch(2, 3)} und {hoch(3, 2)}', f'{hoch(3, 4)} und {hoch(4, 3)}', f'{hoch(2, 5)} und {hoch(5, 2)}', f'{hoch(3, 5)} und {hoch(5, 3)}', f'{hoch(2, 6)} und {hoch(6, 2)}'], 2)
    a, i = _rund(f'{hoch(2, 4)} und {hoch(4, 2)}', f)
    return {'y': 'auswahl', 'f': {'text': 'Bei welchem Paar sind beide Potenzen gleich groß?'}, 'a': a, 'o': {'index': i},
            'w': f'{hoch(2, 4)} = 16 und {hoch(4, 2)} = 16. Bei den anderen Paaren kommt Verschiedenes heraus, z. B. {hoch(2, 3)} = 8, aber {hoch(3, 2)} = 9.',
            'h': 'Rechne jedes Paar aus.'}


def g_vertauschen(s):
    if (2, 4) not in BENUTZT and (s == 1 or R.random() < .3):
        BENUTZT.add((2, 4))
        return _vergleich(*R.choice([(2, 4), (4, 2)]))
    frei = [p for p in PAARE[s] if p not in BENUTZT]
    if s == 3 and R.random() < .4:
        if R.random() < .5: return _behauptung()
        aw, i = _rund('Nein, z. B. 2³ = 8, aber 3² = 9.', ['Ja, immer.', 'Nur bei geraden Zahlen.'])
        return {'y': 'auswahl', 'f': {'text': 'Gilt immer: Basis hoch Exponent = Exponent hoch Basis?'}, 'a': aw, 'o': {'index': i},
                'w': 'Ein Gegenbeispiel genügt: 2³ = 8, aber 3² = 9. Nur bei 2⁴ = 4² = 16 kommt zufällig dasselbe heraus.',
                'h': 'Suche ein Beispiel, bei dem es nicht stimmt.'}
    if not frei: return _behauptung() if R.random() < .7 else _gleiches_paar()
    b, e = R.choice(frei); BENUTZT.add((b, e))
    if R.random() < .5: b, e = e, b
    x, y = b ** e, e ** b
    if s == 1 or max(x, y) > 1000 or R.random() < .5: return _vergleich(b, e)
    return {'y': 'zahl', 'f': {'text': f'Um wie viel unterscheiden sich {hoch(b, e)} und {hoch(e, b)}? Gib den Unterschied als positive Zahl an.'}, 'o': {'wert': abs(x - y)}, 'c': f'abs({b}**{e} - {e}**{b})',
            'w': f'{hoch(b, e)} = {zt(x)} und {hoch(e, b)} = {zt(y)}. Unterschied: {zt(max(x, y))} − {zt(min(x, y))} = {zt(abs(x - y))}.', 'h': 'Rechne beide Potenzen aus. Ziehe die kleinere von der größeren ab.'}


GROSS = [('Deutschland hat etwa 84 Millionen Einwohner.', 84, 6, 'Einwohner'), ('Ein Jahr hat etwa 31 Millionen Sekunden.', 31, 6, 'Sekunden'),
         ('Bayern hat etwa 13 Millionen Einwohner.', 13, 6, 'Einwohner'), ('Die Sonne ist etwa 150 Millionen km von der Erde entfernt.', 150, 6, 'km'),
         ('Auf der Erde leben etwa 8 Milliarden Menschen.', 8, 9, 'Menschen'), ('Ein Herz schlägt an einem Tag etwa 100 Tausend Mal.', 100, 3, 'Schläge')]


def g_zehner(s):
    e = R.randint(2, 6) if s == 1 else R.randint(3, 9)
    k = R.randint(2, 9)
    if s == 1:
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Schreibe {hoch(10, e)} als Zahl.'}, 'o': {'wert': 10 ** e}, 'c': f'10**{e}',
                    'w': f'Der Exponent {e} sagt: eine 1 mit {e} Nullen, also {zt(10 ** e)}.', 'h': 'Der Exponent ist die Anzahl der Nullen.'}
        return {'y': 'zahl', 'f': {'text': f'Wie viele Nullen hat die Zahl {hoch(10, e + 3)}?'}, 'o': {'wert': e + 3}, 'c': str(e + 3),
                'w': f'Bei Zehnerpotenzen ist der Exponent die Anzahl der Nullen: {e + 3}.', 'h': 'Schau auf den Exponenten.'}
    if s == 2:
        art = R.choice(['schreibe', 'exp', 'exp2', 'sach'])
        if art == 'sach':
            satz, z, ex, wort = R.choice(GROSS)
            a, i = _rund(f'{z} · {hoch(10, ex)}', [f'{z} · {hoch(10, ex + 3)}', f'{z} · {hoch(10, ex - 3)}'])
            return {'y': 'auswahl', 'f': {'text': f'{satz} Welche Schreibweise passt?'}, 'a': a, 'o': {'index': i},
                    'w': f'Tausend = {hoch(10, 3)}, Million = {hoch(10, 6)}, Milliarde = {hoch(10, 9)}. Also {z} · {hoch(10, ex)} = {zt(z * 10 ** ex)}.',
                    'h': 'Tausend hat 3 Nullen, eine Million 6, eine Milliarde 9.'}
        if art == 'schreibe':
            return {'y': 'zahl', 'f': {'text': f'Schreibe {k} · {hoch(10, e)} als Zahl.'}, 'o': {'wert': k * 10 ** e}, 'c': f'{k} * 10**{e}',
                    'w': f'{hoch(10, e)} = {zt(10 ** e)}. {k} · {zt(10 ** e)} = {zt(k * 10 ** e)}.', 'h': 'Schreibe zuerst die Zehnerpotenz als Zahl, nimm dann mal.'}
        if art == 'exp2':
            k2 = R.randint(11, 99)
            if k2 % 10 == 0: return g_zehner(s)
            return {'y': 'zahl', 'f': {'text': f'{zt(k2 * 10 ** e)} = {k2} · 10 hoch … Welcher Exponent passt?'}, 'o': {'wert': e}, 'c': str(e),
                    'w': f'Hinter der {k2} stehen {e} Nullen. Also {zt(k2 * 10 ** e)} = {k2} · {hoch(10, e)}.', 'h': f'Zähle nur die Nullen hinter der {k2}.'}
        return {'y': 'zahl', 'f': {'text': f'{zt(k * 10 ** e)} = {k} · 10 hoch … Welcher Exponent passt?'}, 'o': {'wert': e}, 'c': str(e),
                'w': f'{zt(k * 10 ** e)} hat hinter der {k} genau {e} Nullen. Also {k} · {hoch(10, e)}.', 'h': 'Zähle die Nullen hinter der ersten Ziffer.'}
    art = R.choice(['schreibe', 'wort', 'exp3'])
    if art == 'exp3':
        k3 = R.randint(101, 999)
        if k3 % 10 == 0: return g_zehner(s)
        e = R.randint(3, 6)
        return {'y': 'zahl', 'f': {'text': f'{zt(k3 * 10 ** e)} = {k3} · 10 hoch … Welcher Exponent passt?'}, 'o': {'wert': e}, 'c': str(e),
                'w': f'Hinter der {k3} stehen {e} Nullen. Also {zt(k3 * 10 ** e)} = {k3} · {hoch(10, e)}.', 'h': f'Zähle nur die Nullen hinter der {k3}.'}
    if art == 'schreibe':
        k2 = R.randint(11, 99)
        if k2 % 10 == 0: return g_zehner(s)
        return {'y': 'zahl', 'f': {'text': f'Schreibe {k2} · {hoch(10, e)} als Zahl.'}, 'o': {'wert': k2 * 10 ** e}, 'c': f'{k2} * 10**{e}',
                'w': f'{hoch(10, e)} = {zt(10 ** e)}. An {k2} werden {e} Nullen angehängt: {zt(k2 * 10 ** e)}.', 'h': 'Mal 10 hoch n heißt: n Nullen anhängen.'}
    wort = {6: 'Millionen', 9: 'Milliarden'}; e = R.choice([6, 9])
    a, i = _rund(f'{k} · {hoch(10, e)}', [f'{k} · {hoch(10, e - 3)}', f'{k} · {hoch(10, e + 3 if e == 6 else 12)}', f'{hoch(k, e)}'])
    return {'y': 'auswahl', 'f': {'text': f'Wie schreibt man {k} {wort[e]} mit einer Zehnerpotenz?'}, 'a': a, 'o': {'index': i},
            'w': f'1 {"Million" if e == 6 else "Milliarde"} = {zt(10 ** e)} = {hoch(10, e)}. Also {k} {wort[e]} = {k} · {hoch(10, e)}.', 'h': 'Eine Million hat 6 Nullen, eine Milliarde 9.'}


def _ohne_klammer():
    b, e = R.randint(2, 9), R.choice([2, 2, 4])
    if b ** e > 2000: return _ohne_klammer()
    if R.random() < .6:
        a, i = _rund(zt(-(b ** e)), [zt(b ** e), zt(-b * e)])
        return {'y': 'auswahl', 'f': {'text': f'Was ist −{hoch(b, e)}?'}, 'a': a, 'o': {'index': i},
                'w': f'Ohne Klammer gehört das Hoch nur zur {b}: −{hoch(b, e)} = −({mal(b, e)}) = {zt(-(b ** e))}. Mit Klammer wäre ({zt(-b)}){str(e).translate(HOCH)} = {zt(b ** e)}.',
                'h': 'Gehört das Minus zur Basis? Achte auf die Klammer.'}
    return {'y': 'zahl', 'f': {'text': f'Berechne ({zt(-b)}){str(e).translate(HOCH)} + (−{hoch(b, e)}).'}, 'o': {'wert': 0}, 'c': f'(-{b})**{e} + (-({b}**{e}))',
            'w': f'({zt(-b)}){str(e).translate(HOCH)} = {zt(b ** e)} (gerader Exponent). −{hoch(b, e)} = {zt(-(b ** e))} (ohne Klammer). Zusammen {zt(b ** e)} + ({zt(-(b ** e))}) = 0.',
            'h': 'Rechne beide Teile einzeln aus. Achte auf die Klammer.'}


def g_negativ(s):
    if s == 3 and R.random() < .4: return _ohne_klammer()
    if s == 2 and R.random() < .25: return _ohne_klammer()
    b = -R.randint(1, 5) if s < 3 else -R.randint(2, 10)
    e = {1: R.choice([2, 3]), 2: R.choice([2, 3, 4, 5]), 3: R.choice([2, 3, 4, 5, 6])}[s]
    if abs(b) ** e > 100000 or (s == 3 and abs(b) ** e < 60) or (b == -1 and s > 1 and e < 4): return g_negativ(s)
    if s == 2 and R.random() < .4:
        e = R.randint(4, 15); b = -R.randint(2, 9)
        if e % 2 == 0: r, f = 'positiv', ['negativ, weil die Basis negativ ist', 'negativ, weil ein Minus übrig bleibt']
        else: r, f = 'negativ', [f'positiv, weil {e} positiv ist', 'positiv, weil Minus mal Minus Plus ist']
        a, i = _rund(r, f)
        return {'y': 'auswahl', 'f': {'text': f'Ist {hoch(b, e)} positiv oder negativ? (Du musst nicht ausrechnen.)'}, 'a': a, 'o': {'index': i},
                'w': f'Der Exponent {e} ist {"gerade" if e % 2 == 0 else "ungerade"}. Je zwei Minus ergeben Plus{"" if e % 2 == 0 else ", eines bleibt übrig"}: Das Ergebnis ist {r}.',
                'h': 'Bilde Paare aus den Minus-Faktoren. Bleibt eines übrig?'}
    return {'y': 'zahl', 'f': {'text': f'Berechne {hoch(b, e)}.'}, 'o': {'wert': b ** e}, 'c': f'({b})**{e}',
            'w': f'{hoch(b, e)} = {mal(b, e)}. Betrag: {abs(b)} hoch {e} = {zt(abs(b) ** e)}. Exponent {e} ist {"gerade" if e % 2 == 0 else "ungerade"}, also {zt(b ** e)}.',
            'h': 'Rechne erst ohne Vorzeichen. Dann: gerader Exponent positiv, ungerader negativ.'}


def g_sach(s):
    if s == 1:
        n = R.randint(2, 6)
        text = R.choice([f'Ein Blatt Papier wird {n}-mal gefaltet. Jedes Falten verdoppelt die Zahl der Lagen. Wie viele Lagen sind es dann?',
                         f'Eine Seerose bedeckt 1 m². Jede Woche verdoppelt sich die Fläche. Wie viele m² sind es nach {n} Wochen?',
                         f'Ein Gerücht: Zu Beginn weiß es 1 Kind. Jeden Tag verdoppelt sich die Zahl der Kinder, die es wissen. Wie viele sind es nach {n} Tagen?'])
        return {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': 2 ** n}, 'c': f'2**{n}',
                'w': f'{n}-mal verdoppeln: {mal(2, n)} = {hoch(2, n)} = {2 ** n}.', 'h': 'Jedes Verdoppeln ist ein Faktor 2.'}
    if s == 2:
        art = R.choice(['wuerfel', 'platz', 'wuerfel_rueck', 'platz_rueck'])
        k = R.randint(2, 10)
        if art == 'wuerfel':
            return {'y': 'zahl', 'f': {'text': f'Ein Würfel hat die Kantenlänge {k} cm. Er wird aus kleinen Würfeln mit 1 cm Kantenlänge gebaut. Wie viele kleine Würfel braucht man?'}, 'o': {'wert': k ** 3}, 'c': f'{k}**3',
                    'w': f'In jeder Richtung {k} Würfel: {k} · {k} · {k} = {hoch(k, 3)} = {zt(k ** 3)}.', 'h': 'Länge mal Breite mal Höhe, alle drei sind gleich.'}
        if art == 'wuerfel_rueck':
            return {'y': 'zahl', 'f': {'text': f'Ein großer Würfel besteht aus {zt(k ** 3)} kleinen Würfeln. Wie viele kleine Würfel liegen an einer Kante?'}, 'o': {'wert': k}, 'c': str(k),
                    'w': f'Gesucht ist die Zahl, die dreimal mit sich malgenommen {zt(k ** 3)} ergibt: {k} · {k} · {k} = {zt(k ** 3)}.',
                    'h': 'Welche Zahl hoch 3 ergibt die Anzahl? Probiere kleine Zahlen.'}
        m = R.randint(9, 20)
        if art == 'platz':
            return {'y': 'zahl', 'f': {'text': f'Ein quadratischer Platz ist {m} m lang und {m} m breit. Er wird mit Platten von 1 m² belegt. Wie viele Platten braucht man?'}, 'o': {'wert': m * m}, 'c': f'{m}**2',
                    'w': f'{m} Reihen mit je {m} Platten: {hoch(m, 2)} = {m * m}.', 'h': 'Reihen mal Platten pro Reihe. Beide Zahlen sind gleich.'}
        return {'y': 'zahl', 'f': {'text': f'Ein quadratischer Platz ist mit {m * m} Platten von 1 m² belegt. Wie lang ist eine Seite?'}, 'o': {'wert': m, 'einheit': 'm'}, 'c': str(m),
                'w': f'Seite mal Seite = {m * m}. Gesucht ist die Zahl mit {m} · {m} = {m * m}. Eine Seite ist {m} m lang.',
                'h': 'Welche Zahl mal sich selbst ergibt die Anzahl der Platten?'}
    if R.random() < .5:
        start, std = R.choice([1, 2, 3, 5]), R.randint(1, 3)
        n = 3 * std
        return {'y': 'zahl', 'f': {'text': f'In einer Schale {"ist 1 Bakterium" if start == 1 else f"sind {start} Bakterien"}. Alle 20 Minuten verdoppelt sich die Anzahl. Wie viele sind es nach {std} {"Stunde" if std == 1 else "Stunden"}?'},
                'o': {'wert': start * 2 ** n}, 'c': f'{start} * 2**{n}',
                'w': f'In {std} {"Stunde" if std == 1 else "Stunden"} gibt es {n}-mal 20 Minuten, also {n} Verdopplungen: {hoch(2, n)} = {zt(2 ** n)}.' + (f' Mal Startwert {start}: {zt(start * 2 ** n)}.' if start > 1 else ''),
                'h': 'Wie oft passen 20 Minuten in die Zeit? So oft wird verdoppelt. Vergiss den Startwert nicht.'}
    b, n = R.choice([(3, R.randint(3, 6)), (2, R.randint(7, 10)), (10, R.randint(3, 6)), (4, R.randint(3, 5)), (5, R.randint(3, 4))])
    wort = {2: 'verdoppelt', 3: 'verdreifacht', 4: 'vervierfacht', 5: 'verfünffacht', 10: 'verzehnfacht'}[b]
    start = R.choice([1, 1, 2, 3, 5])
    return {'y': 'zahl', 'f': {'text': f'Ein Kettenbrief startet mit {start} {"Brief" if start == 1 else "Briefen"}. In jeder Runde {wort} sich die Zahl der Briefe. Wie viele Briefe sind es nach {n} Runden?'},
            'o': {'wert': start * b ** n}, 'c': f'{start} * {b}**{n}',
            'w': f'{n}-mal mal {b}: {hoch(b, n)} = {zt(b ** n)}.' + (f' Mal Startwert {start}: {zt(start * b ** n)}.' if start > 1 else ''),
            'h': 'Jede Runde ist derselbe Faktor. Schreibe das als Potenz und vergiss den Startwert nicht.'}


GEN = {'schreibweise': g_schreibweise, 'berechnen': g_berechnen, 'quadrat': g_quadrat, 'vertauschen': g_vertauschen, 'zehner': g_zehner, 'negativ': g_negativ, 'sach': g_sach}
DATEI = {
    'thema_schluessel': 'zahlen.potenzen_basis', 'thema_id': 67, 'block_id': 49, 'klasse': {'gym_by': 5, 'rs_by': 5, 'ib_myp': 1},
    'autor': 'Claude (Generator zahlen_potenzen_basis.py)',
    'inhalt': {
        'ziel': 'Potenzen als Kurzschreibweise lesen, schreiben und berechnen; Quadratzahlen bis 400 kennen; große Zahlen mit Zehnerpotenzen schreiben.',
        'merke': ['Potenz = dieselbe Zahl mehrmals malnehmen. Exponent = wie oft.', 'Basis und Exponent nie vertauschen.',
                  '10 hoch n = eine 1 mit n Nullen.', 'Negative Basis: gerader Exponent positiv, ungerader negativ.'],
        'abschnitte': [{'titel': 'Potenzen verstehen', 'lernziele': ['schreibweise', 'berechnen', 'vertauschen']},
                       {'titel': 'Besondere Potenzen', 'lernziele': ['quadrat', 'zehner', 'negativ']},
                       {'titel': 'Anwenden', 'lernziele': ['sach']}],
        'etappen': ETAPPEN,
        'teilfaehigkeiten': [{'k': 'begriff', 'text': 'Potenzschreibweise deuten', 'lernziele': ['schreibweise', 'vertauschen']},
                             {'k': 'berechnen', 'text': 'Potenzen und Quadratzahlen berechnen', 'lernziele': ['berechnen', 'quadrat']},
                             {'k': 'zehner', 'text': 'Große Zahlen mit Zehnerpotenzen', 'lernziele': ['zehner']},
                             {'k': 'negativ', 'text': 'Potenzen mit ganzzahliger Basis', 'lernziele': ['negativ']},
                             {'k': 'anwenden', 'text': 'Sachanwendungen', 'lernziele': ['sach']}],
        'bewertung': {'lernziele_pflicht': [e['lernziel'] for e in ETAPPEN], 'lernziele_vertiefung': [], 'testaufgaben_je_lernziel': 1, 'hilfen_im_test': False},
        'quellen': {'erklaerungen': 'Eigene Fassung (Claude).', 'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern, Gymnasium Mathematik 5.'},
    },
    'aufgaben': baue(R, ETAPPEN, GEN, TEIL, je_stufe=5),
}

# Umbau U5 (Achte Runde, Vorgabe 16.11.): Lernkarten nach dem neuen Muster – einstieg, woerter (≤ 3), Kartenbild,
# Bildergeschichte (schritte mit bild), „Pass auf!“ (fehler + fehler_bild), MERKE (regel).
# Situationen: Geheimnis weitererzählen (Baumdiagramm), Bakterien, Fliesen, Stadion, Papier falten.
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl5.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl5 import umbau  # noqa: E402


def runden(n):
    """Baumdiagramm: jedes Kind erzählt es 2 Freunden weiter, n Runden."""
    return [{'text': 'Kind', 'aeste': runden(n - 1)} if n > 1 else {'text': 'Kind'} for _ in range(2)]


BAKTERIEN = lambda *w: {'typ': 'tabelle', 'kopf': ['Stunde', '0', '1', '2', '3', '4', '5'], 'zeilen': [['Bakterien', *w]]}
FLIESEN = lambda a, b, c: {'typ': 'tabelle', 'kopf': ['Reihen', 'Rechnung', 'Fliesen'], 'zeilen': [['10', '10 · 14', a], ['4', '4 · 14', b], ['14', 'zusammen', c]]}
FALTEN = lambda n: {'werte': [{'name': x, 'wert': w} for x, w in list(zip(['Start', '1.', '2.', '3.', '4.'], [1, 2, 4, 8, 16]))[:n]]}

KARTEN = {
 'schreibweise': {
  'einstieg': 'Ein Kind erzählt ein Geheimnis 2 Freunden. Jeder erzählt es wieder 2 Freunden, und die auch. In Runde 3 hören es 2 · 2 · 2 Kinder, kurz als ⟦Potenz⟧ 2³.',
  'woerter': [['Potenz', 'Kurzschrift für dieselbe Zahl mehrmals malgenommen, zum Beispiel 2³'], ['Basis', 'die Zahl, die malgenommen wird'],
              ['Exponent', 'die kleine Zahl oben: wie oft die Basis dasteht']],
  'bild': {'typ': 'baum', 'aeste': runden(1)},
  'schritte': [{'text': 'Runde 1: 2 Kinder hören es.'},
               {'text': 'Runde 2: Jedes erzählt es 2 weiter, also 2 · 2 = 4 Kinder.', 'bild': {'aeste': runden(2)}},
               {'text': 'Runde 3: 2 · 2 · 2 = 8 Kinder.', 'bild': {'aeste': runden(3)}},
               {'text': 'Die Basis 2 steht 3-mal da, also Exponent 3: ⟦2³⟧.'}],
  'fehler': '2³ ist nicht 2 · 3 = 6. Der Exponent zählt, wie oft die 2 dasteht: 2 · 2 · 2 = 8.',
  'regel': 'Die ⟦Basis⟧ wird so oft malgenommen, wie der Exponent sagt. 3 · 3 · 3 · 3 = 3⁴.'},
 'berechnen': {
  'einstieg': 'Ein Bakterium teilt sich jede Stunde in zwei. Nach 5 Stunden sind es 2⁵ Bakterien. Wie viele das sind, heißt ⟦Wert der Potenz⟧.',
  'woerter': [['2⁵', 'gelesen „2 hoch 5“: 2 · 2 · 2 · 2 · 2'], ['Wert der Potenz', 'das Ergebnis, wenn man die Potenz ausrechnet']],
  'bild': BAKTERIEN('1', '?', '?', '?', '?', '?'),
  'schritte': [{'text': 'Schreibe 2⁵ lang aus: 2 · 2 · 2 · 2 · 2.'},
               {'text': 'Von links: 2 · 2 = 4, dann 4 · 2 = 8.', 'bild': BAKTERIEN('1', '2', '4', '8', '?', '?')},
               {'text': 'Weiter: 8 · 2 = 16 und 16 · 2 = 32.', 'bild': BAKTERIEN('1', '2', '4', '8', '16', '32')},
               {'text': 'Also ist ⟦2⁵ = 32⟧. Nach 5 Stunden sind es 32 Bakterien.'}],
  'fehler': '2⁵ = 10 ist falsch: Das wäre 2 · 5. Nach 5 Stunden gäbe es dann nur 10 Bakterien statt 32.',
  'regel': 'Eine Potenz rechnest du aus: ⟦lang ausschreiben⟧, dann Schritt für Schritt malnehmen.'},
 'quadrat': {
  'einstieg': 'Ein quadratischer Badboden hat 14 Reihen mit je 14 Fliesen. Das sind 14 · 14 Fliesen, kurz 14². So ein Ergebnis heißt ⟦Quadratzahl⟧.',
  'woerter': [['14²', 'gelesen „14 hoch 2“ oder „14 zum Quadrat“: 14 · 14'], ['Quadratzahl', 'eine Zahl mal sich selbst: 1, 4, 9, 16 …']],
  'bild': 'BEHALTEN',
  'schritte': [{'text': 'Gesucht ist 14² = 14 · 14.'},
               {'text': 'Teile die 14 Reihen in 10 und 4 Reihen.', 'bild': FLIESEN('?', '?', '?')},
               {'text': '10 Reihen haben 140 Fliesen, 4 Reihen haben 56.', 'bild': FLIESEN('140', '56', '?')},
               {'text': 'Zusammen: 140 + 56 = ⟦196⟧. Also ist 14² = 196.', 'bild': FLIESEN('140', '56', '196')}],
  'fehler': '14² = 28 ist falsch: Das wäre 14 · 2. Der Boden hat aber 14 Reihen, nicht 2.',
  'regel': 'Hoch 2 heißt: ⟦Zahl mal sich selbst⟧. Lerne die Quadratzahlen bis 20² = 400 auswendig.'},
 'vertauschen': {
  'einstieg': 'Geht ein Geheimnis 3 Runden an je 2 Freunde, hören es zuletzt 8 Kinder. Bei 2 Runden an je 3 Freunde sind es 9. Basis und Exponent darf man ⟦nicht vertauschen⟧.',
  'woerter': [['vertauschen', 'zwei Zahlen ihre Plätze wechseln lassen'], ['3²', 'gelesen „3 hoch 2“: 3 · 3'], ['>', '„ist größer als“']],
  'bild': {'typ': 'saeulen', 'einheit': 'Kinder', 'werte': [{'name': '2³', 'wert': 8}, {'name': '3²', 'wert': 9}], 'zahlen': False},
  'schritte': [{'text': '2³ = 2 · 2 · 2 = 8.', 'bild': {'werte': [{'name': '2³', 'wert': 8}], 'zahlen': True, 'y_max': 10}},
               {'text': '3² = 3 · 3 = 9.', 'bild': {'werte': [{'name': '2³', 'wert': 8}, {'name': '3²', 'wert': 9}]}},
               {'text': '9 ist mehr als 8: ⟦3² > 2³⟧.'}],
  'fehler': '„2³ und 3² sind gleich, es sind ja dieselben Zahlen“ ist falsch. 8 Kinder sind nicht 9 Kinder.',
  'regel': 'Basis und Exponent darfst du ⟦nicht vertauschen⟧. Vergleiche Potenzen, indem du beide ausrechnest.'},
 'zehner': {
  'einstieg': 'Ein großes Fußballstadion hat rund 70 000 Plätze. Bei so vielen Nullen verzählt man sich leicht. Darum schreibt man 7 · 10⁴ – mit einer ⟦Zehnerpotenz⟧.',
  'woerter': [['Zehnerpotenz', 'eine Potenz mit der Basis 10: 10² = 100, 10³ = 1 000'], ['10⁴', '10 · 10 · 10 · 10 = 10 000: eine 1 mit 4 Nullen'],
              ['Zehntausender', 'die Stelle links von den Tausendern (ZT)']],
  'bild': {'typ': 'stellentafel', 'stellen': ['ZT', 'T', 'H', 'Z', 'E'], 'ziffern': ['', '', '', '', '']},
  'schritte': [{'text': '10⁴ ist eine 1 mit 4 Nullen: 10 000.', 'bild': {'ziffern': ['1', '0', '0', '0', '0']}},
               {'text': '7 · 10 000: Die 7 steht bei den Zehntausendern.', 'bild': {'ziffern': ['7', '0', '0', '0', '0'], 'markiert': 0}},
               {'text': 'Das Stadion hat rund ⟦70 000⟧ Plätze.'}],
  'fehler': 'Eine Null zu viel: 7 · 10⁴ ist nicht 700 000. Der Exponent 4 heißt genau 4 Nullen, also 70 000.',
  'regel': 'Der Exponent sagt, wie viele ⟦Nullen⟧ hinter der 1 stehen. 3 · 10⁵ = 300 000.'},
 'negativ': {
  'einstieg': 'Mal eine negative Zahl springt das Ergebnis auf die andere Seite der 0. Wie ein Lichtschalter: an, aus, an. So geht es bei einer ⟦negativen Basis⟧.',
  'woerter': [['negative Basis', 'die Basis hat ein Minus, zum Beispiel (−2)³'], ['(−2)³', '(−2) · (−2) · (−2); die Klammer zeigt: Das Minus gehört zur Basis']],
  'bild': {'typ': 'zahlenstrahl', 'start': -8, 'ende': 8, 'abschnitte': 16, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': '(−2)³ hat eine negative Basis: (−2) · (−2) · (−2). Start bei −2.', 'bild': {'punkte': [{'wert': -2, 'name': '1.'}]}},
               {'text': '(−2) · (−2) = 4: Das Ergebnis springt nach rechts.', 'bild': {'punkte': [{'wert': -2, 'name': '1.'}, {'wert': 4, 'name': '2.'}]}},
               {'text': '4 · (−2) = ⟦−8⟧: wieder auf die linke Seite.',
                'bild': {'punkte': [{'wert': -2, 'name': '1.'}, {'wert': 4, 'name': '2.'}, {'wert': -8, 'name': '3.'}]}}],
  'fehler': '−3² und (−3)² verwechseln. Ohne Klammer gehört das Minus nicht zur Basis: −3² = −9, aber (−3)² = 9.',
  'regel': 'Bei negativer Basis entscheidet der Exponent über das ⟦Vorzeichen⟧. Gerade: plus, ungerade: minus.'},
 'sach': {
  'einstieg': 'Faltest du ein Blatt einmal, hat es 2 Lagen. Noch einmal gefaltet sind es 4, dann 8. Jedes Falten ⟦verdoppelt⟧ die Lagen.',
  'woerter': [['Lage', 'eine Schicht Papier'], ['verdoppelt', 'mal 2 genommen']],
  'bild': {'typ': 'saeulen', 'einheit': 'Lagen', 'werte': [{'name': 'Start', 'wert': 1}], 'y_max': 16},
  'schritte': [{'text': 'Am Anfang hat das Blatt 1 Lage.'},
               {'text': 'Jedes Falten verdoppelt: 2, dann 4, dann 8 Lagen.', 'bild': FALTEN(4)},
               {'text': 'Nach 4-mal Falten: 2 · 2 · 2 · 2 = 2⁴.', 'bild': FALTEN(5)},
               {'text': 'Ausgerechnet: 2⁴ = ⟦16⟧ Lagen.'}],
  'fehler': '4-mal verdoppeln ist nicht „mal 8“. Falte nach: 2, 4, 8, 16 Lagen. Es ist 2⁴ = 16.',
  'regel': 'Immer wieder mit derselben Zahl malnehmen ist eine ⟦Potenz⟧. 5-mal verdoppeln heißt 2⁵-mal so viel.'},
}
umbau(DATEI, KARTEN)


# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl5) ----------
# Neue Übungen nach Prüfungsvorbild (Jahrgangsstufentest 6 Bayern: Quadratzahlen, Zahlenfolgen, Verdopplung; Bayerischer Mathematik-Test); eigene Zahlen.
from _schwer_kl5 import A, L, Z, de, einzig, ergaenze, rw, wahl  # noqa: E402

_HOCH = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')


def _p(term):
    """Wert eines Terms mit hochgestellten Exponenten, z. B. '2⁶' oder '(−2)³' oder '−2⁴' (Potenz vor Minus)."""
    import re
    rueck = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹', '0123456789')
    t = re.sub(r'([⁰¹²³⁴⁵⁶⁷⁸⁹]+)', lambda m: '**' + m.group(1).translate(rueck), term)
    return rw(t)


def _schwer():
    N = {}
    sechzig = [(b, e) for b in range(2, 65) for e in range(2, 7) if b ** e == 64]
    N['schreibweise'] = [
        wahl(2, 'Schreibe mit zwei Potenzen: 7 · 7 · 7 · 2 · 2', ['7³ · 2²', '7² · 2³', '14⁵', '7³ + 2²'], lambda o: o == '7³ · 2²',
             'Die 7 steht 3-mal da, die 2 steht 2-mal da: 7³ · 2².', 'Zähle für jede Basis, wie oft sie vorkommt.'),
        Z(2, 'Eine Potenz hat den Exponenten 3 und den Wert 1 000. Wie heißt die Basis?', str(einzig([b for b in range(1, 100) if b ** 3 == 1000])),
          '10 · 10 · 10 = 1 000. Die Basis ist 10.', 'Welche Zahl dreimal mit sich selbst malgenommen ergibt 1 000?'),
        Z(3, 'Die Zahlenfolge 3, 9, 27, 81, … geht immer nach derselben Regel weiter. Welche Zahl steht an der 6. Stelle?', '3 ** 6',
          'Jede Zahl ist das Dreifache der vorigen: 3¹, 3², 3³, 3⁴ … An 6. Stelle steht 3⁶ = 729.', 'Wie kommt man von einer Zahl zur nächsten? Schreibe die Zahlen als Potenzen von 3.'),
        wahl(3, 'Was ist größer: 2¹⁰ oder 1 000?', ['2¹⁰', '1 000', 'beide gleich groß'], lambda o: o == '2¹⁰',
             '2¹⁰ = 1 024. Das ist etwas mehr als 1 000.', 'Verdopple 10-mal: 2, 4, 8, 16, …'),
        Z(3, 'Wie viele Möglichkeiten gibt es, 64 als Potenz zu schreiben? Basis und Exponent sollen natürliche Zahlen größer als 1 sein.', str(len(sechzig)),
          '64 = 2⁶ = 4³ = 8². Das sind 3 Möglichkeiten.', 'Probiere die Basen 2, 4 und 8.'),
        A(3, 'Jemand schreibt 5 + 5 + 5 = 5³. Was ist falsch?', 'Dreimal 5 addieren ist 3 · 5 = 15. 5³ heißt 5 · 5 · 5 = 125.',
          ['Nichts, das stimmt.', 'Richtig wäre 3⁵.', 'Richtig wäre 5² + 5.'],
          'Eine Potenz steht für wiederholtes Malnehmen, nicht für wiederholtes Addieren.', 'Was bedeutet der Exponent: wie oft addieren oder wie oft malnehmen?'),
    ]
    welche = ['2⁶', '4³', '8²', '3⁴']
    N['berechnen'] = [
        Z(2, 'Berechne 2⁴ + 3².', '2**4 + 3**2', '2⁴ = 16 und 3² = 9. 16 + 9 = 25.', 'Rechne zuerst beide Potenzen aus.'),
        Z(2, 'Berechne 3 · 2³.', '3 * 2**3', 'Potenz zuerst: 2³ = 8. Dann 3 · 8 = 24.', 'Potenzen rechnest du vor dem Malnehmen.'),
        Z(3, 'Berechne 5 + 2 · 3³.', '5 + 2 * 3**3', 'Potenz vor Punkt vor Strich: 3³ = 27, 2 · 27 = 54, 5 + 54 = 59.', 'Reihenfolge: erst Potenz, dann mal, dann plus.'),
        A(3, 'Jemand rechnet 2 · 5² = 10² = 100. Was ist falsch?', 'Die Potenz kommt zuerst: 5² = 25, dann 2 · 25 = 50.',
          ['Nichts, 100 stimmt.', 'Richtig ist 2 · 5 · 2 = 20.', 'Richtig ist 2² · 5² = 100, also stimmt es.'],
          'Der Exponent 2 gehört nur zur 5. Erst 5² = 25, dann mal 2: 50.', 'Zu welcher Zahl gehört der Exponent?'),
        wahl(3, 'Welche Zahl ist am größten?', welche, lambda o: _p(o) == max(_p(x) for x in welche),
             '2⁶ = 64, 4³ = 64, 8² = 64, aber 3⁴ = 81. Am größten ist 3⁴.', 'Rechne alle vier aus.'),
        Z(3, 'Berechne (2 + 3)² − (2² + 3²).', '(2 + 3)**2 - (2**2 + 3**2)', '(2 + 3)² = 5² = 25. 2² + 3² = 4 + 9 = 13. 25 − 13 = 12.',
          'Bei (2 + 3)² zuerst die Klammer. Achtung: (2 + 3)² ist nicht 2² + 3².'),
    ]
    paar = einzig([n for n in range(1, 25) if (n + 1) ** 2 - n ** 2 == 31])
    N['quadrat'] = [
        Z(2, 'Berechne 15² − 14².', '15**2 - 14**2', '15² = 225 und 14² = 196. 225 − 196 = 29.', 'Rechne beide Quadratzahlen aus.'),
        Z(2, 'Welche Quadratzahl liegt zwischen 280 und 300?', str(einzig([n * n for n in range(1, 25) if 280 < n * n < 300])),
          '16² = 256 ist zu klein, 17² = 289 passt, 18² = 324 ist zu groß.', 'Probiere 16², 17², 18².'),
        Z(3, 'Die Folge 100, 121, 144, 169, … besteht aus Quadratzahlen. Welche Zahl kommt als nächste?', '14**2',
          '100 = 10², 121 = 11², 144 = 12², 169 = 13². Als nächste kommt 14² = 196.', 'Welche Zahlen werden hier quadriert?'),
        Z(3, 'Berechne 13² + 31.', '13**2 + 31', 'Potenz zuerst: 13² = 169. Dann 169 + 31 = 200.', 'Zuerst 13 · 13 ausrechnen.'),
        Z(3, 'Ein Quadrat ist aus Fliesen gelegt, 15 Fliesen je Seite. Wie viele Fliesen liegen am Rand?', '15**2 - 13**2',
          'Alle Fliesen: 15² = 225. Innen bleibt ein Quadrat mit 13 · 13 = 169. Am Rand: 225 − 169 = 56.',
          'Zieh von allen Fliesen die inneren ab. Wie viele Fliesen hat das innere Quadrat je Seite?'),
        L(3, 'Zwei Quadratzahlen, die direkt aufeinander folgen, unterscheiden sich um 31. Welche sind es?', 'kleinere: □; größere: □', 'Trage beide Quadratzahlen ein.',
          [f'{paar}**2', f'{paar + 1}**2'], f'{paar}² = {paar ** 2} und {paar + 1}² = {(paar + 1) ** 2}. Der Unterschied ist 31.',
          'Schau dir die Unterschiede an: 4 − 1 = 3, 9 − 4 = 5, 16 − 9 = 7 … Wie geht es weiter?'),
    ]
    kl3 = ['2⁵', '5²', '3³']
    gleich = ['a = 2, b = 4', 'a = 2, b = 3', 'a = 3, b = 4', 'a = 1, b = 2']
    def gl(o):
        a, b = (int(x.split('= ')[1]) for x in o.split(', '))
        return a ** b == b ** a
    N['vertauschen'] = [
        wahl(2, 'Welche der Potenzen 2⁵, 5² und 3³ ist am kleinsten?', kl3, lambda o: _p(o) == min(_p(x) for x in kl3),
             '2⁵ = 32, 5² = 25, 3³ = 27. Am kleinsten ist 5².', 'Rechne alle drei aus.'),
        Z(2, 'Berechne 2⁵ − 5².', '2**5 - 5**2', '2⁵ = 32 und 5² = 25. 32 − 25 = 7.', 'Erst beide Potenzen ausrechnen.'),
        wahl(3, 'Für welches Zahlenpaar gilt aᵇ = bᵃ, obwohl a und b verschieden sind?', gleich, gl,
             '2⁴ = 16 und 4² = 16. Bei den anderen Paaren: 2³ = 8 ≠ 9 = 3², 3⁴ = 81 ≠ 64 = 4³, 1² = 1 ≠ 2 = 2¹.', 'Rechne für jedes Paar beide Potenzen aus.'),
        Z(3, 'Wie viel größer ist 3⁴ als 4³?', '3**4 - 4**3', '3⁴ = 81 und 4³ = 64. Unterschied: 17.', 'Rechne beide Potenzen aus.'),
        A(3, 'Jemand behauptet: 10² = 2¹⁰, weil in beiden eine 10 und eine 2 vorkommen. Stimmt das?', 'Nein: 10² = 100, aber 2¹⁰ = 1 024.',
          ['Ja, Basis und Exponent darf man tauschen.', 'Nein: 10² = 20 und 2¹⁰ = 20, also doch gleich.', 'Ja, beide ergeben 100.'],
          '10² = 10 · 10 = 100. 2¹⁰ ist zehnmal die 2 malgenommen: 1 024.', 'Rechne beide Potenzen aus.'),
        Z(3, 'Wie heißt der kleinste Exponent n, für den 2ⁿ größer ist als 5²?', str(min(n for n in range(1, 20) if 2 ** n > 25)),
          '5² = 25. 2⁴ = 16 ist zu klein, 2⁵ = 32 ist größer. Also n = 5.', 'Verdopple so lange, bis du über 25 kommst.'),
    ]
    N['zehner'] = [
        Z(2, 'Schreibe 3 · 10⁵ + 4 · 10³ als Zahl.', '3 * 10**5 + 4 * 10**3', '3 · 10⁵ = 300 000 und 4 · 10³ = 4 000. Zusammen 304 000.', 'Schreibe beide Teile als Zahl und addiere.'),
        Z(2, 'Ein Jahr hat rund 3 · 10⁷ Sekunden. Schreibe die Zahl aus.', '3 * 10**7', '10⁷ ist eine 1 mit 7 Nullen. 3 · 10⁷ = 30 000 000.', 'Hänge an die 3 so viele Nullen an, wie der Exponent sagt.'),
        Z(3, 'Schreibe als Zahl: 2 · 10⁶ + 7 · 10⁴ + 5 · 10', '2 * 10**6 + 7 * 10**4 + 5 * 10',
          'Millionen: 2, Zehntausender: 7, Zehner: 5. Alle anderen Stellen sind 0: 2 070 050.', 'Trage die Ziffern in eine Stellenwerttafel ein. Leere Stellen bekommen eine 0.'),
        Z(3, 'Wie viele Nullen hat die Zahl 50 · 10⁴, wenn man sie ausschreibt?', str(str(50 * 10 ** 4).count('0')),
          '50 · 10⁴ = 500 000. Die 50 bringt schon eine Null mit, dazu kommen 4 Nullen: 5 Nullen.', 'Schreibe die Zahl aus. Achte auf die Null in der 50.'),
        Z(3, 'Wie oft passt 10³ in 10⁷?', '10**7 // 10**3', '10⁷ = 10 000 000, 10³ = 1 000. 10 000 000 : 1 000 = 10 000 = 10⁴.', 'Teile: Wie viele Nullen fallen weg?'),
        Z(3, 'In einem Tresor liegen 4 · 10³ Geldscheine zu je 50 €. Wie viel Euro sind das?', '4 * 10**3 * 50', '4 · 10³ = 4 000 Scheine. 4 000 · 50 € = 200 000 €.',
          'Schreibe zuerst die Anzahl der Scheine aus.', einheit='€'),
    ]
    klein = ['(−2)⁴', '−2⁴', '(−2)³', '−(−2)³']
    N['negativ'] = [
        Z(2, 'Berechne (−2)⁵.', '(-2)**5', '2⁵ = 32. Ungerader Exponent bei negativer Basis: −32.', 'Zähle die Minuszeichen: gerade oder ungerade?'),
        Z(2, 'Berechne (−10)⁴.', '(-10)**4', '10⁴ = 10 000. Gerader Exponent: positiv, also 10 000.', 'Gerader Exponent bei negativer Basis ergibt plus.'),
        Z(3, 'Berechne (−2)³ − (−3)².', '(-2)**3 - (-3)**2', '(−2)³ = −8 und (−3)² = 9. −8 − 9 = −17.', 'Rechne beide Potenzen mit Vorzeichen aus.'),
        wahl(3, 'Welche Zahl ist am kleinsten?', klein, lambda o: _p(o) == min(_p(x) for x in klein),
             '(−2)⁴ = 16, −2⁴ = −16 (nur die 2 wird potenziert), (−2)³ = −8, −(−2)³ = 8. Am kleinsten ist −2⁴.', 'Achte genau auf die Klammern.'),
        Z(3, 'Für wie viele Exponenten n von 1 bis 10 gilt (−1)ⁿ = 1?', str(sum(1 for n in range(1, 11) if (-1) ** n == 1)),
          'Bei geraden Exponenten ist (−1)ⁿ = 1: n = 2, 4, 6, 8, 10. Das sind 5.', 'Wann ist eine Potenz mit negativer Basis positiv?'),
        Z(3, '(−3)ⁿ ist negativ und größer als −100. Der Exponent n ist größer als 1. Wie heißt n?', str(einzig([n for n in range(2, 12) if -100 < (-3) ** n < 0])),
          'Negativ nur bei ungeradem n: (−3)³ = −27 liegt über −100, (−3)⁵ = −243 liegt darunter. Also n = 3.', 'Probiere die ungeraden Exponenten 3, 5, …'),
    ]
    N['sach'] = [
        Z(2, 'Ein Karton enthält 10 Packungen. In jeder Packung sind 10 Beutel mit je 10 Bonbons. Wie viele Bonbons sind im Karton?', '10**3',
          '10 · 10 · 10 = 10³ = 1 000 Bonbons.', 'Dreimal „je 10“: Welche Potenz ist das?'),
        Z(2, 'Ein quadratisches Beet hat eine Fläche von 64 m². Wie lang ist eine Seite?', str(einzig([n for n in range(1, 30) if n * n == 64])),
          '8 · 8 = 64. Eine Seite ist 8 m lang.', 'Welche Zahl mal sich selbst ergibt 64?', einheit='m'),
        Z(3, 'In einem Teich leben 300 Algenzellen. Alle 3 Stunden verdoppelt sich ihre Anzahl. Wie viele sind es nach 12 Stunden?', '300 * 2**(12 // 3)',
          '12 Stunden sind 4-mal 3 Stunden, also 4 Verdopplungen: 300 · 2⁴ = 300 · 16 = 4 800.', 'Wie oft wird in 12 Stunden verdoppelt?'),
        Z(3, 'Eine Seerose verdoppelt jede Woche ihre Fläche. Nach 10 Wochen ist der Teich ganz bedeckt. Nach wie vielen Wochen war er zur Hälfte bedeckt?', '10 - 1',
          'Von halb voll zu ganz voll ist genau eine Verdopplung, also eine Woche. Nach 9 Wochen war er halb bedeckt.', 'Denk rückwärts: Was war eine Woche vor dem vollen Teich?'),
        Z(3, 'Ein großer Würfel ist aus 4 · 4 · 4 kleinen Würfeln gebaut. Wie viele kleine Würfel liegen ganz innen und berühren keine Außenfläche?', '(4 - 2)**3',
          'Innen bleibt ein Würfel mit 2 · 2 · 2 = 2³ = 8 kleinen Würfeln.', 'Nimm von jeder Seite eine Schicht weg. Wie groß ist der Würfel innen?'),
        Z(3, 'Eine Zahl wird dreimal hintereinander verdoppelt. Das Ergebnis ist 200. Wie hieß die Zahl am Anfang?', '200 // 2**3',
          'Dreimal verdoppeln heißt mal 2³ = 8. Rückwärts: 200 : 8 = 25.', 'Dreimal verdoppeln heißt mal wie viel?'),
    ]
    return N


ergaenze(DATEI, _schwer(), 1067)

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('zahlen.potenzen_basis', 13_5_3)
# a) Grundform direkt nach der Erklärung
for _t in ['Was bedeutet 2⁷?', 'Was bedeutet 5⁴?', 'Was bedeutet 10⁴?', 'Was bedeutet 3²?']:
    BF.stufe('schreibweise', _t, 1)
# a) leicht → Stufe 2; c) Beinahe-Dublette (gleiche Antwort 121) → neue Aufgabe
BF.stufe('quadrat', 'Welche Zahl ist eine Quadratzahl?', 2, enthaelt='"122"')
BF.ersetze('quadrat', 'Welche Zahl ist eine Quadratzahl?', BF.A(
    'Welche Zahl liegt zwischen den Quadratzahlen 13² und 14²?', '180', ['160', '200', '150'],
    '13² = 169 und 14² = 196. Nur 180 liegt dazwischen.', 'Berechne zuerst 13 · 13 und 14 · 14.'), enthaelt='"124"')

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl5, siehe _durchsicht_kl5.py) ----
from _durchsicht_kl5 import Durchsicht, durchsicht_anwenden  # noqa: E402

DS = Durchsicht('zahlen.potenzen_basis', 19_5_7)
# a) Stufe 3 nur mit größeren Zahlen oder derselben Vorlage wie Stufe 2 → Stufe 2
for _lz, _t in [('schreibweise', '5 hoch wie viel ergibt 625?'),
        ('berechnen', 'Berechne 2¹².'),
        ('berechnen', 'Berechne 9⁴.'),
        ('quadrat', 'Berechne 20² − 2².'),
        ('quadrat', 'Welche Zahl ist eine Quadratzahl?'),
        ('quadrat', 'Berechne 13² + 31.'),
        ('vertauschen', 'Vergleiche 9³ und 3⁹. Was stimmt?'),
        ('vertauschen', 'Vergleiche 3⁸ und 8³. Was stimmt?'),
        ('zehner', 'Wie schreibt man 8 Milliarden mit einer Zehnerpotenz?'),
        ('zehner', 'Schreibe 44 · 10⁶ als Zahl.'),
        ('zehner', 'Wie schreibt man 2 Millionen mit einer Zehnerpotenz?'),
        ('zehner', 'Wie schreibt man 3 Milliarden mit einer Zehnerpotenz?'),
        ('negativ', 'Berechne (−5)⁵.')]:
    DS.stufe(_lz, _t, 2, enthaelt=lambda x: x['s'] == 3)
durchsicht_anwenden(DATEI, DS)
# ---- DURCHSICHT ENDE ----
# ---- STUFEN (Zwanzigste Runde, Zweig stufen-kl5, siehe _stufen_kl5.py und _st5_zahlen_potenzen_basis.py) ----
from _stufen_kl5 import stufen_anwenden  # noqa: E402
stufen_anwenden(DATEI, 'zahlen.potenzen_basis')
# ---- STUFEN ENDE ----

if __name__ == '__main__':
    schreibe(DATEI, 'zahlen.potenzen_basis.json')
