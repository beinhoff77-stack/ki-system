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

if __name__ == '__main__':
    schreibe(DATEI, 'zahlen.potenzen_basis.json')
