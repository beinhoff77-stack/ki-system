#!/usr/bin/env python3
"""Potenzen als Schreibweise (Gymnasium Kl. 5): Potenz lesen/schreiben, berechnen, Quadratzahlen bis 400,
Zehnerpotenzen für große Zahlen, negative Basis, Sachanwendungen. Keine Potenzgesetze (Kl. 6)."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl5 import baue, kl, mische, schreibe, zt  # noqa: E402

R = random.Random(67)
HOCH = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')
hoch = lambda b, e: f'{kl(b) if b < 0 else zt(b)}{str(e).translate(HOCH)}'
mal = lambda b, e: ' · '.join([kl(b)] * e)

ETAPPEN = [
    {'lernziel': 'schreibweise', 'titel': 'Was ist eine Potenz?',
     'regel': 'Eine Potenz ist eine Kurzschreibweise für ⟦mehrmals dieselbe Zahl malnehmen⟧: 3 · 3 · 3 · 3 = 3⁴. Die ⟦Basis⟧ 3 ist der Faktor, der ⟦Exponent⟧ 4 sagt, wie oft er dasteht.',
     'schritte': ['5 · 5 · 5: Der Faktor 5 steht 3-mal da.', 'Basis 5, Exponent 3: ⟦5³⟧. Man liest „5 hoch 3“.'],
     'fehler': '3⁴ ist nicht 3 · 4. Der Exponent zählt, ⟦wie oft⟧ die 3 als Faktor dasteht: 3 · 3 · 3 · 3.'},
    {'lernziel': 'berechnen', 'titel': 'Potenzen ausrechnen',
     'regel': 'Schreibe die Potenz als Produkt und rechne ⟦Schritt für Schritt⟧ von links nach rechts.',
     'schritte': ['2⁵ = 2 · 2 · 2 · 2 · 2', '2 · 2 = 4, · 2 = 8, · 2 = 16, · 2 = ⟦32⟧'],
     'probe': '32 : 2 = 16, : 2 = 8, : 2 = 4, : 2 = 2 ✓',
     'fehler': '2⁵ = 10 ist falsch: Das wäre 2 · 5. Richtig ist 2 · 2 · 2 · 2 · 2 = ⟦32⟧.'},
    {'lernziel': 'quadrat', 'titel': 'Quadratzahlen bis 400',
     'regel': '„Hoch 2“ heißt ⟦Quadrat⟧: die Zahl mal sich selbst. Die Quadratzahlen von 1² bis 20² solltest du auswendig können: … 11² = 121, 12² = 144, 13² = 169, 14² = 196, 15² = 225, 16² = 256, 17² = 289, 18² = 324, 19² = 361, 20² = 400.',
     'schritte': ['14² = 14 · 14', '14 · 10 = 140 und 14 · 4 = 56, zusammen ⟦196⟧'],
     'fehler': '14² = 28 ist falsch: Das wäre 14 · 2. Quadrat heißt 14 · ⟦14⟧.'},
    {'lernziel': 'vertauschen', 'titel': 'Basis und Exponent nicht vertauschen',
     'regel': 'Bei Potenzen darf man Basis und Exponent ⟦nicht vertauschen⟧: 2³ = 8, aber 3² = 9.',
     'schritte': ['2³ = 2 · 2 · 2 = 8', '3² = 3 · 3 = 9', 'Also ist ⟦3² größer⟧ als 2³.'],
     'fehler': 'Bei 3 · 4 = 4 · 3 darf man tauschen. Bei Potenzen nicht: 2⁵ = 32, aber 5² = ⟦25⟧.'},
    {'lernziel': 'zehner', 'titel': 'Zehnerpotenzen für große Zahlen',
     'regel': 'Bei Zehnerpotenzen sagt der Exponent, ⟦wie viele Nullen⟧ die Zahl hat: 10³ = 1 000, 10⁶ = 1 000 000. Große Zahlen schreibt man kurz als Produkt: 3 · 10⁵ = 300 000.',
     'schritte': ['7 · 10⁴: 10⁴ hat 4 Nullen, also 10 000.', '7 · 10 000 = ⟦70 000⟧'],
     'fehler': '10⁴ = 40 ist falsch. 10⁴ = 10 · 10 · 10 · 10 = ⟦10 000⟧, eine 1 mit 4 Nullen.'},
    {'lernziel': 'negativ', 'titel': 'Potenzen mit negativer Basis',
     'regel': 'Steht eine negative Zahl in Klammern, wird sie ⟦samt Minus⟧ malgenommen. Gerader Exponent: Ergebnis ⟦positiv⟧. Ungerader Exponent: Ergebnis ⟦negativ⟧.',
     'schritte': ['(−2)³ = (−2) · (−2) · (−2)', '(−2) · (−2) = 4, dann 4 · (−2) = ⟦−8⟧'],
     'probe': '(−2)² = 4 ist positiv (gerader Exponent), (−2)³ = −8 negativ (ungerader Exponent) ✓',
     'fehler': '(−3)² = −9 ist falsch: (−3) · (−3) = ⟦9⟧, denn Minus mal Minus ergibt Plus.'},
    {'lernziel': 'sach', 'titel': 'Potenzen im Alltag',
     'regel': 'Wenn sich etwas immer wieder ⟦verdoppelt, verdreifacht oder verzehnfacht⟧, hilft eine Potenz: nach 5 Verdopplungen hat man 2⁵-mal so viel.',
     'schritte': ['Ein Blatt wird 4-mal gefaltet. Jedes Falten verdoppelt die Lagen.', '2 · 2 · 2 · 2 = 2⁴ = ⟦16⟧ Lagen'],
     'fehler': '4-mal verdoppeln ist nicht „mal 8“ (4 · 2). Es ist 2 · 2 · 2 · 2 = ⟦16⟧-mal so viel.'},
]
TEIL = {'schreibweise': 'begriff', 'berechnen': 'berechnen', 'quadrat': 'berechnen', 'vertauschen': 'begriff', 'zehner': 'zehner', 'negativ': 'negativ', 'sach': 'anwenden'}


def g_schreibweise(s):
    b, e = R.randint(2, 12), R.randint(2, 6)
    if s == 1:
        a, i = mische(R, hoch(b, e), [hoch(e, b) if e != b else hoch(b, e + 1), f'{b} · {e}'])
        return {'y': 'auswahl', 'f': {'text': f'Schreibe als Potenz: {mal(b, e)}'}, 'a': a, 'o': {'index': i},
                'w': f'Der Faktor {b} steht {e}-mal da. Basis {b}, Exponent {e}: {hoch(b, e)}.', 'h': 'Zähle, wie oft der Faktor dasteht. Das ist der Exponent.'}
    if s == 2:
        if e == b: return g_schreibweise(s)
        was = R.choice(['Basis', 'Exponent'])
        return {'y': 'zahl', 'f': {'text': f'Wie heißt {"die Basis" if was == "Basis" else "der Exponent"} der Potenz {hoch(b, e)}?'}, 'o': {'wert': b if was == 'Basis' else e},
                'c': str(b if was == 'Basis' else e), 'w': f'In {hoch(b, e)} ist {b} die Basis (unten, der Faktor) und {e} der Exponent (oben, die Anzahl).',
                'h': 'Die Basis steht unten, der Exponent klein oben.'}
    if e == b: return g_schreibweise(s)
    a, i = mische(R, mal(b, e), [mal(e, b), f'{b} · {e}', ' + '.join([str(b)] * e)])
    return {'y': 'auswahl', 'f': {'text': f'Was bedeutet {hoch(b, e)}?'}, 'a': a, 'o': {'index': i},
            'w': f'{hoch(b, e)} heißt: {b} steht {e}-mal als Faktor da, also {mal(b, e)}.', 'h': 'Der Exponent sagt, wie oft die Basis als Faktor dasteht.'}


def g_berechnen(s):
    b, e = R.choice({1: [(2, 3), (2, 4), (3, 3), (4, 3), (5, 3), (1, 5), (1, 8), (10, 3), (2, 5)],
                     2: [(2, 6), (2, 7), (3, 4), (4, 4), (5, 4), (6, 3), (7, 3), (8, 3), (9, 3), (2, 8), (3, 5), (10, 4), (1, 20), (10, 5), (30, 2), (40, 2), (25, 2), (50, 2), (3, 6), (20, 3)],
                     3: [(2, 9), (2, 10), (4, 5), (5, 5), (6, 4), (7, 4), (11, 3), (12, 3), (15, 3), (30, 3), (2, 11), (2, 12), (3, 7), (8, 4), (9, 4)]}[s])
    zw, t = b, []
    for _ in range(e - 1): t.append(f'{zt(zw)} · {b} = {zt(zw * b)}'); zw *= b
    return {'y': 'zahl', 'f': {'text': f'Berechne {hoch(b, e)}.'}, 'o': {'wert': b ** e}, 'c': f'{b}**{e}',
            'w': f'{hoch(b, e)} = {mal(b, e)}. Schritt für Schritt: {", ".join(t)}.', 'h': 'Schreibe die Potenz als Produkt und rechne von links nach rechts.'}


def g_quadrat(s):
    n = R.randint(2, 12) if s == 1 else R.randint(11, 20)
    if s == 1 or (s == 2 and R.random() < .6):
        return {'y': 'zahl', 'f': {'text': f'Berechne {hoch(n, 2)}.'}, 'o': {'wert': n * n}, 'c': f'{n}**2',
                'w': f'{hoch(n, 2)} = {n} · {n} = {n * n}.', 'h': 'Hoch 2 heißt: die Zahl mal sich selbst.'}
    if s == 2:
        return {'y': 'zahl', 'f': {'text': f'Welche natürliche Zahl ergibt im Quadrat {n * n}?'}, 'o': {'wert': n}, 'c': str(n),
                'w': f'Gesucht ist die Zahl, die mit sich selbst malgenommen {n * n} ergibt: {n} · {n} = {n * n}.', 'h': 'Probiere mit den Quadratzahlen, die du kennst: 10² = 100, 15² = 225, 20² = 400.'}
    art = R.choice(['zwischen', 'summe', 'ist'])
    if art == 'summe':
        m = R.randint(2, 12)
        return {'y': 'zahl', 'f': {'text': f'Berechne {hoch(n, 2)} − {hoch(m, 2)}.'}, 'o': {'wert': n * n - m * m}, 'c': f'{n}**2 - {m}**2',
                'w': f'Erst die Quadrate: {hoch(n, 2)} = {n * n} und {hoch(m, 2)} = {m * m}. Dann {n * n} − {m * m} = {n * n - m * m}.', 'h': 'Rechne zuerst beide Quadrate aus, dann die Differenz.'}
    if art == 'zwischen':
        return {'y': 'zahl', 'f': {'text': f'Welche Quadratzahl liegt zwischen {n * n - R.randint(3, 9)} und {n * n + R.randint(3, 9)}?'}, 'o': {'wert': n * n}, 'c': f'{n}**2',
                'w': f'In diesem Bereich liegt {n} · {n} = {n * n}. Die Nachbarn {(n - 1) ** 2} und {(n + 1) ** 2} liegen außerhalb.', 'h': 'Gehe die Quadratzahlen der Reihe nach durch.'}
    k = n * n
    falsch = [k + R.choice([-2, -1, 1, 2, 3]), n * 2 * R.randint(3, 6) + 1]
    falsch = [f for f in falsch if int(f ** .5) ** 2 != f and f != k]
    if len(set(falsch)) < 2: return g_quadrat(s)
    a, i = mische(R, zt(k), [zt(f) for f in falsch])
    return {'y': 'auswahl', 'f': {'text': 'Welche Zahl ist eine Quadratzahl?'}, 'a': a, 'o': {'index': i},
            'w': f'{k} = {n} · {n} = {hoch(n, 2)}. Die anderen Zahlen sind kein Quadrat einer natürlichen Zahl.', 'h': 'Eine Quadratzahl ist eine Zahl mal sich selbst.'}


def g_vertauschen(s):
    paare = {1: [(2, 3), (2, 5), (3, 4), (2, 6), (3, 5), (5, 3), (4, 3), (6, 2), (5, 2), (3, 2)], 2: [(2, 7), (3, 6), (4, 5), (2, 8), (5, 4), (6, 3), (7, 2), (8, 2), (7, 3), (3, 7), (2, 9), (9, 2), (6, 4), (4, 6)],
             3: [(2, 10), (10, 2), (3, 8), (8, 3), (2, 11), (5, 6), (6, 5), (4, 7), (7, 4), (9, 3), (3, 9), (10, 3), (3, 10)]}[s]
    b, e = R.choice(paare)
    x, y = b ** e, e ** b
    if s == 1 or R.random() < .5:
        gr = hoch(b, e) if x > y else hoch(e, b)
        a, i = mische(R, f'{gr} ist größer', [f'{hoch(e, b) if x > y else hoch(b, e)} ist größer', 'Beide sind gleich groß'])
        return {'y': 'auswahl', 'f': {'text': f'Vergleiche {hoch(b, e)} und {hoch(e, b)}. Was stimmt?'}, 'a': a, 'o': {'index': i},
                'w': f'{hoch(b, e)} = {zt(x)} und {hoch(e, b)} = {zt(y)}. Also ist {gr} größer.', 'h': 'Rechne beide Potenzen aus und vergleiche.'}
    return {'y': 'zahl', 'f': {'text': f'Um wie viel unterscheiden sich {hoch(b, e)} und {hoch(e, b)}? Gib den Unterschied als positive Zahl an.'}, 'o': {'wert': abs(x - y)}, 'c': f'abs({b}**{e} - {e}**{b})',
            'w': f'{hoch(b, e)} = {zt(x)} und {hoch(e, b)} = {zt(y)}. Unterschied: {zt(max(x, y))} − {zt(min(x, y))} = {zt(abs(x - y))}.', 'h': 'Rechne beide Potenzen aus. Ziehe die kleinere von der größeren ab.'}


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
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Schreibe {k} · {hoch(10, e)} als Zahl.'}, 'o': {'wert': k * 10 ** e}, 'c': f'{k} * 10**{e}',
                    'w': f'{hoch(10, e)} = {zt(10 ** e)}. {k} · {zt(10 ** e)} = {zt(k * 10 ** e)}.', 'h': 'Schreibe zuerst die Zehnerpotenz als Zahl, nimm dann mal.'}
        return {'y': 'zahl', 'f': {'text': f'{zt(k * 10 ** e)} = {k} · 10 hoch … Welcher Exponent passt?'}, 'o': {'wert': e}, 'c': str(e),
                'w': f'{zt(k * 10 ** e)} hat hinter der {k} genau {e} Nullen. Also {k} · {hoch(10, e)}.', 'h': 'Zähle die Nullen hinter der ersten Ziffer.'}
    if R.random() < .5:
        k2 = R.randint(11, 99)
        if k2 % 10 == 0: return g_zehner(s)
        return {'y': 'zahl', 'f': {'text': f'Schreibe {k2} · {hoch(10, e)} als Zahl.'}, 'o': {'wert': k2 * 10 ** e}, 'c': f'{k2} * 10**{e}',
                'w': f'{hoch(10, e)} = {zt(10 ** e)}. An {k2} werden {e} Nullen angehängt: {zt(k2 * 10 ** e)}.', 'h': 'Mal 10 hoch n heißt: n Nullen anhängen.'}
    wort = {6: 'Millionen', 9: 'Milliarden'}; e = R.choice([6, 9])
    a, i = mische(R, f'{k} · {hoch(10, e)}', [f'{k} · {hoch(10, e - 3)}', f'{k} · {hoch(10, e + 3 if e == 6 else 12)}', f'{hoch(k, e)}'])
    return {'y': 'auswahl', 'f': {'text': f'Wie schreibt man {k} {wort[e]} mit einer Zehnerpotenz?'}, 'a': a, 'o': {'index': i},
            'w': f'1 {wort[e][:-2] if e == 6 else "Milliarde"} = {zt(10 ** e)} = {hoch(10, e)}. Also {k} {wort[e]} = {k} · {hoch(10, e)}.', 'h': 'Eine Million hat 6 Nullen, eine Milliarde 9.'}


def g_negativ(s):
    b = -R.randint(1, 5) if s < 3 else -R.randint(2, 10)
    e = {1: R.choice([2, 3]), 2: R.choice([2, 3, 4, 5]), 3: R.choice([2, 3, 4, 5, 6])}[s]
    if abs(b) ** e > 100000 or (s == 3 and abs(b) ** e < 60) or (b == -1 and s > 1 and e < 4): return g_negativ(s)
    if s == 2 and R.random() < .4:
        e = R.randint(4, 15); b = -R.randint(2, 9)
        a, i = mische(R, 'positiv' if e % 2 == 0 else 'negativ', ['negativ' if e % 2 == 0 else 'positiv', 'null'])
        return {'y': 'auswahl', 'f': {'text': f'Ist {hoch(b, e)} positiv oder negativ? (Du musst nicht ausrechnen.)'}, 'a': a, 'o': {'index': i},
                'w': f'Der Exponent {e} ist {"gerade" if e % 2 == 0 else "ungerade"}. Je zwei Minus ergeben Plus{"" if e % 2 == 0 else ", eines bleibt übrig"}: Das Ergebnis ist {"positiv" if e % 2 == 0 else "negativ"}.',
                'h': 'Gerader Exponent: positiv. Ungerader Exponent: negativ.'}
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
        k = R.randint(2, 12)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Ein Würfel hat die Kantenlänge {k} cm. Er wird aus kleinen Würfeln mit 1 cm Kantenlänge gebaut. Wie viele kleine Würfel braucht man?'}, 'o': {'wert': k ** 3}, 'c': f'{k}**3',
                    'w': f'In jeder Richtung {k} Würfel: {k} · {k} · {k} = {hoch(k, 3)} = {zt(k ** 3)}.', 'h': 'Länge mal Breite mal Höhe, alle drei sind gleich.'}
        return {'y': 'zahl', 'f': {'text': f'Ein quadratischer Platz ist {k + 8} m lang und {k + 8} m breit. Er wird mit Platten von 1 m² belegt. Wie viele Platten braucht man?'}, 'o': {'wert': (k + 8) ** 2}, 'c': f'{k + 8}**2',
                'w': f'{k + 8} Reihen mit je {k + 8} Platten: {hoch(k + 8, 2)} = {(k + 8) ** 2}.', 'h': 'Reihen mal Platten pro Reihe. Beide Zahlen sind gleich.'}
    b, n = R.choice([(3, R.randint(3, 6)), (2, R.randint(7, 10)), (10, R.randint(3, 6)), (4, R.randint(3, 5)), (5, R.randint(3, 4))])
    wort = {2: 'verdoppelt', 3: 'verdreifacht', 4: 'vervierfacht', 5: 'verfünffacht', 10: 'verzehnfacht'}[b]
    start = R.choice([1, 1, 2, 3, 5])
    text = R.choice([f'In einer Schale {"ist 1 Bakterium" if start == 1 else f"sind {start} Bakterien"}. Jede Stunde {wort} sich die Anzahl. Wie viele sind es nach {n} Stunden?',
                     f'Ein Kettenbrief startet mit {start} {"Brief" if start == 1 else "Briefen"}. In jeder Runde {wort} sich die Zahl der Briefe. Wie viele Briefe sind es nach {n} Runden?'])
    return {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': start * b ** n}, 'c': f'{start} * {b}**{n}',
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
