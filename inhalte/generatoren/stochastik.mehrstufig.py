#!/usr/bin/env python3
"""Thema stochastik.mehrstufig – Mehrstufige Zufallsexperimente (Klasse 10)."""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import *  # noqa: E402,F403

start(1007)

FARBEN = [('rote', 'rot', 'r'), ('blaue', 'blau', 'b'), ('grüne', 'grün', 'g'), ('gelbe', 'gelb', 'y'), ('weiße', 'weiß', 'w'), ('schwarze', 'schwarz', 's')]


def cf(x):
    x = Fr(x)
    return str(int(x)) if x.denominator == 1 else str(float(x)) if endlich(x) else f'({x.numerator}/{x.denominator})'


def frac_c(q):
    q = Fr(q)
    return [str(q.numerator), str(q.denominator)]


def baum2(t1, t2, p1, p2, q):
    """Zweistufiger Baum mit den Ergebnissen t1/t2; q = [[p(t1|t1), p(t2|t1)], [p(t1|t2), p(t2|t2)]] als Texte."""
    return {'typ': 'baum', 'aeste': [{'text': t1, 'p': p1, 'aeste': [{'text': t1, 'p': q[0][0]}, {'text': t2, 'p': q[0][1]}]},
                                     {'text': t2, 'p': p2, 'aeste': [{'text': t1, 'p': q[1][0]}, {'text': t2, 'p': q[1][1]}]}]}


def urne():
    (f1, n1, _), (f2, n2, _) = R.sample(FARBEN, 2)
    a, b = R.randint(2, 8), R.randint(2, 8)
    return f1, n1, a, f2, n2, b


def pfad_tabelle(stufen, probs, namen=('1. Stufe', '2. Stufe', 'Pfad-Wahrscheinlichkeit')):
    """Tabelle der Pfade (Ersatz für das Baumdiagramm)."""
    zeilen = [[a, b, p] for (a, b), p in zip(stufen, probs)]
    return tabelle(namen, zeilen)


ETAPPEN = [
    {'lernziel': 'pfad_mult', 'titel': 'Pfadregel: Multiplizieren',
     'regel': 'Bei einem mehrstufigen Zufallsexperiment ist die Wahrscheinlichkeit eines Pfades das ⟦Produkt der Wahrscheinlichkeiten entlang des Pfades⟧ (1. Pfadregel).',
     'schritte': ['Urne mit 3 roten und 2 blauen Kugeln, zweimal ziehen mit Zurücklegen. P(rot) = 3/5.', 'P(rot, rot) = 3/5 · 3/5 = ⟦9/25⟧.'],
     'probe': '9/25 = 0,36 < 3/5 ✓',
     'fehler': 'P(rot, rot) = 3/5 + 3/5 ist falsch: Entlang eines Pfades wird ⟦multipliziert⟧, nicht addiert (sonst käme mehr als 1 heraus).'},
    {'lernziel': 'pfad_add', 'titel': 'Pfadregel: Addieren',
     'regel': 'Gehören ⟦mehrere Pfade⟧ zu einem Ereignis, ⟦addiert⟧ man ihre Wahrscheinlichkeiten (2. Pfadregel).',
     'schritte': ['Zweimal Münzwurf, Ereignis „genau einmal Kopf“: Pfade (K, Z) und (Z, K).', 'P = ½ · ½ + ½ · ½ = ⟦½⟧.'],
     'probe': 'P(0 · K) + P(1 · K) + P(2 · K) = ¼ + ½ + ¼ = 1 ✓',
     'fehler': 'Bei „genau einmal Kopf“ nur den Pfad (K, Z) zu zählen ist falsch: Auch ⟦(Z, K)⟧ gehört dazu – die Reihenfolge ist egal.'},
    {'lernziel': 'ohne_zuruecklegen', 'titel': 'Ziehen ohne Zurücklegen',
     'regel': 'Ohne Zurücklegen ⟦ändern sich die Wahrscheinlichkeiten⟧ auf der zweiten Stufe: Eine Kugel weniger insgesamt und – falls gleiche Farbe – eine weniger dieser Farbe.',
     'schritte': ['3 rote, 2 blaue Kugeln, zweimal ohne Zurücklegen: P(rot, rot) = 3/5 · 2/4.', 'P = 6/20 = ⟦3/10⟧.'],
     'probe': 'P(blau, blau) = 2/5 · 1/4 = 1/10 ✓',
     'fehler': 'P(rot, rot) = 3/5 · 3/5 gilt nur ⟦mit⟧ Zurücklegen. Ohne Zurücklegen bleiben 2 rote von 4 Kugeln.'},
    {'lernziel': 'gegenereignis', 'titel': 'Mindestens einmal: Gegenereignis',
     'regel': 'Bei „⟦mindestens einmal⟧“ rechnet man meist über das ⟦Gegenereignis „keinmal“⟧: P(mindestens einmal) = 1 − P(keinmal).',
     'schritte': ['Dreimal würfeln, mindestens eine Sechs: P(keine Sechs) = (5/6)³ = 125/216.', 'P = 1 − 125/216 = ⟦91/216⟧ ≈ 0,42.'],
     'probe': '91 + 125 = 216 ✓',
     'fehler': 'P(mindestens eine Sechs) = 3 · 1/6 = ½ ist falsch: So werden Pfade mit mehreren Sechsen ⟦mehrfach gezählt⟧. Über das Gegenereignis rechnen.'},
    {'lernziel': 'baum_ergaenzen', 'titel': 'Baumdiagramm vervollständigen',
     'regel': 'Die Wahrscheinlichkeiten der Äste, die von ⟦einem Verzweigungspunkt⟧ ausgehen, ergeben zusammen ⟦1⟧. Kennt man eine Pfadwahrscheinlichkeit und den ersten Ast, findet man den zweiten durch ⟦Teilen⟧.',
     'schritte': ['Erster Ast P(A) = 0,4, Pfad P(A und B) = 0,1.', 'Zweiter Ast: 0,1 : 0,4 = ⟦0,25⟧; der Gegenast hat 0,75.'],
     'probe': '0,4 · 0,25 = 0,1 ✓',
     'fehler': 'Den zweiten Ast als 0,1 − 0,4 oder 0,1 + 0,4 zu berechnen ist falsch: Pfadwahrscheinlichkeit = Produkt, also ⟦teilen⟧.'},
    {'lernziel': 'simulation', 'titel': 'Simulation und Erwartung',
     'regel': 'Bei n Durchführungen erwartet man etwa ⟦n · p⟧ Treffer. Die ⟦relative Häufigkeit⟧ (Treffer : n) aus einer Simulation schwankt, nähert sich bei großem n aber der Wahrscheinlichkeit.',
     'schritte': ['P(Pasch bei zwei Würfeln) = 6/36 = 1/6. 600 Würfe mit zwei Würfeln.', 'Erwartet: 600 · 1/6 = ⟦100⟧ Pasche.'],
     'probe': 'Eine Simulation ergab 94 Pasche: relative Häufigkeit 94/600 ≈ 0,157 ≈ 1/6 ✓',
     'fehler': '„Nach 5 Würfen ohne Sechs kommt die Sechs jetzt wahrscheinlicher“ ist falsch: Würfel haben ⟦kein Gedächtnis⟧, P bleibt 1/6.'},
    {'lernziel': 'verstehen', 'titel': 'Aussagen prüfen',
     'regel': 'Prüfe: Wird ⟦entlang⟧ eines Pfades multipliziert und ⟦zwischen⟧ Pfaden addiert? Ändern sich die Wahrscheinlichkeiten ⟦ohne Zurücklegen⟧? Ergeben die Äste je Verzweigung 1?',
     'schritte': ['Behauptung: Bei zweimal Münzwurf ist P(zweimal Kopf) = ½ + ½ = 1.', 'Falsch: Entlang des Pfades ⟦multiplizieren⟧: ½ · ½ = ¼.'],
     'probe': 'P(1) würde „sicher“ bedeuten – zweimal Kopf ist aber nicht sicher ✓',
     'fehler': 'Wahrscheinlichkeiten über 1 sind immer ein Hinweis auf einen ⟦Rechenfehler⟧.'},
]
_E = {e['lernziel']: e for e in ETAPPEN}
_E['pfad_mult']['bild'] = {'typ': 'baum', 'aeste': [{'text': 'rot', 'p': '3/5', 'aeste': [{'text': 'rot', 'p': '3/5'}, {'text': 'blau', 'p': '2/5'}]},
                                                    {'text': 'blau', 'p': '2/5', 'aeste': [{'text': 'rot', 'p': '3/5'}, {'text': 'blau', 'p': '2/5'}]}]}
_E['pfad_add']['bild'] = {'typ': 'baum', 'aeste': [{'text': 'K', 'p': '1/2', 'aeste': [{'text': 'K', 'p': '1/2'}, {'text': 'Z', 'p': '1/2'}]},
                                                   {'text': 'Z', 'p': '1/2', 'aeste': [{'text': 'K', 'p': '1/2'}, {'text': 'Z', 'p': '1/2'}]}]}
_E['ohne_zuruecklegen']['bild'] = {'typ': 'baum', 'aeste': [{'text': 'rot', 'p': '3/5', 'aeste': [{'text': 'rot', 'p': '2/4'}, {'text': 'blau', 'p': '2/4'}]},
                                                            {'text': 'blau', 'p': '2/5', 'aeste': [{'text': 'rot', 'p': '3/4'}, {'text': 'blau', 'p': '1/4'}]}]}
_E['gegenereignis']['bild'] = {'typ': 'baum', 'aeste': [{'text': '6', 'p': '1/6'},
                                                        {'text': 'keine 6', 'p': '5/6', 'aeste': [{'text': '6', 'p': '1/6'},
                                                                                                  {'text': 'keine 6', 'p': '5/6', 'aeste': [{'text': '6', 'p': '1/6'}, {'text': 'keine 6', 'p': '5/6'}]}]}]}
_E['baum_ergaenzen']['bild'] = {'typ': 'baum', 'aeste': [{'text': 'A', 'p': '0,4', 'aeste': [{'text': 'B', 'p': '?'}, {'text': 'nicht B', 'p': '?'}]},
                                                         {'text': 'nicht A', 'p': '?'}]}
_E['simulation']['bild'] = {'typ': 'saeulen', 'einheit': 'Anzahl', 'werte': [{'name': 'Pasch', 'wert': 94}, {'name': 'kein Pasch', 'wert': 506}], 'zahlen': True}


def g_pfad_mult(s):
    f1, n1, a, f2, n2, b = urne()
    n = a + b
    p = Fr(a, n)
    if s == 1:
        q = p * p
        return mit_grafik(bruch_luecke(f'In einer Urne liegen {a} {f1} und {b} {f2} Kugeln. Es wird zweimal mit Zurücklegen gezogen (siehe Baumdiagramm). Berechne P({n1}, {n1}) als gekürzten Bruch.',
                                       q, f'P({n1}) = {a}/{n}; P({n1}, {n1}) = {a}/{n} · {a}/{n} = {br(q)}.', 'Multipliziere entlang des Pfades.',
                                       c=frac_c(q)),
                          baum2(n1, n2, f'{a}/{n}', f'{b}/{n}', [[f'{a}/{n}', f'{b}/{n}'], [f'{a}/{n}', f'{b}/{n}']]))
    if s == 2:
        if R.random() < 0.5:
            q = p * (1 - p)
            return bruch_luecke(f'In einer Urne liegen {a} {f1} und {b} {f2} Kugeln. Zweimal mit Zurücklegen: Wie groß ist P(zuerst {n1}, dann {n2})?',
                                q, f'{a}/{n} · {b}/{n} = {br(q)}.', 'Ein bestimmter Pfad: entlang multiplizieren.', c=frac_c(q))
        pt = Fr(R.choice([6, 7, 8, 9]), 10)   # Freiwurfquote realistisch 0,6 … 0,9
        k = R.randint(2, 4)
        q = pt ** k
        return zahl(f'Ein Basketballspieler trifft bei einem Freiwurf mit der Wahrscheinlichkeit {dz(pt)}. Mit welcher Wahrscheinlichkeit trifft er {k}-mal hintereinander (Würfe unabhängig)?',
                    f'P = {dz(pt)}^{k} = {dz(q)}.', 'Jeder Wurf ist eine Stufe; multipliziere.', q, f'{cf(pt)} ** {k}')
    k = 3
    q = p ** 2 * (1 - p)
    return bruch_luecke(f'In einer Urne liegen {a} {f1} und {b} {f2} Kugeln. Es wird dreimal mit Zurücklegen gezogen. Berechne P({n1}, {n1}, {n2}) in dieser Reihenfolge.',
                        q, f'{a}/{n} · {a}/{n} · {b}/{n} = {br(q)}.', 'Drei Stufen, ein Pfad: drei Faktoren.', c=frac_c(q))


def g_pfad_add(s):
    f1, n1, a, f2, n2, b = urne()
    n = a + b
    p = Fr(a, n)
    if s == 1:
        q = 2 * p * (1 - p)
        return bruch_luecke(f'In einer Urne liegen {a} {f1} und {b} {f2} Kugeln. Es wird zweimal mit Zurücklegen gezogen. Wie groß ist P(zwei verschiedene Farben)?', q,
                            f'Pfade ({n1}, {n2}) und ({n2}, {n1}): {a}/{n} · {b}/{n} + {b}/{n} · {a}/{n} = {br(q)}.', 'Welche Pfade gehören dazu? Addiere sie.', c=frac_c(q))
    if s == 2:
        q = p * p + (1 - p) * (1 - p)
        return bruch_luecke(f'In einer Urne liegen {a} {f1} und {b} {f2} Kugeln. Es wird zweimal mit Zurücklegen gezogen. Wie groß ist P(zweimal dieselbe Farbe)?', q,
                            f'({a}/{n})² + ({b}/{n})² = {br(q)}.', 'Zwei Pfade: beide gleich ' + n1 + ' oder beide ' + n2 + '.', c=frac_c(q))
    pt = Fr(R.choice([2, 3, 4, 6, 7, 8]), 10)
    q = 3 * pt ** 2 * (1 - pt)
    return zahl(f'Ein Glücksrad zeigt mit der Wahrscheinlichkeit {dz(pt)} „Gewinn“. Es wird dreimal gedreht. Wie groß ist P(genau zweimal Gewinn)?',
                f'Drei Pfade (GGN, GNG, NGG), jeder {dz(pt)}² · {dz(1 - pt)} = {dz(pt ** 2 * (1 - pt))}; zusammen {dz(q)}.',
                'Wie viele Reihenfolgen gibt es für zwei Gewinne bei drei Drehungen?', q, f'3 * {cf(pt)} ** 2 * (1 - {cf(pt)})')


def g_ohne_zuruecklegen(s):
    f1, n1, a, f2, n2, b = urne()
    n = a + b
    if s == 1:
        q = Fr(a, n) * Fr(a - 1, n - 1)
        if q == 0: return None
        return bruch_luecke(f'In einer Urne liegen {a} {f1} und {b} {f2} Kugeln. Es werden zwei Kugeln ohne Zurücklegen gezogen. Berechne P({n1}, {n1}).', q,
                            f'{a}/{n} · {a - 1}/{n - 1} = {br(q)}.', 'Nach der ersten Kugel: eine Kugel weniger insgesamt und eine weniger dieser Farbe.',
                            c=frac_c(q))
    if s == 2:
        q = 2 * Fr(a, n) * Fr(b, n - 1)
        return mit_grafik(bruch_luecke(f'In einer Urne liegen {a} {f1} und {b} {f2} Kugeln. Es werden zwei Kugeln ohne Zurücklegen gezogen. Ergänze im Kopf die Äste der zweiten Stufe und berechne P(zwei verschiedene Farben).', q,
                                       f'Zweite Stufe nach {n1}: {a - 1}/{n - 1} und {b}/{n - 1}; nach {n2}: {a}/{n - 1} und {b - 1}/{n - 1}. '
                                       f'P = {a}/{n} · {b}/{n - 1} + {b}/{n} · {a}/{n - 1} = {br(q)}.', 'Zwei Pfade; auf der zweiten Stufe ist der Nenner um 1 kleiner.', c=frac_c(q)),
                          baum2(n1, n2, f'{a}/{n}', f'{b}/{n}', [['?', '?'], ['?', '?']]))
    if R.random() < 0.5:
        # mindestens ein Gewinn ohne Zurücklegen – über das Gegenereignis
        m, k, z = R.randint(8, 20), R.randint(2, 5), R.choice([2, 3])
        if m - k < z: return None
        nieten = Fr(1)
        teile = []
        for i in range(z):
            nieten *= Fr(m - k - i, m - i)
            teile.append(f'{m - k - i}/{m - i}')
        q = 1 - nieten
        return bruch_luecke(f'In einer Lostrommel sind {m} Lose, davon {k} Gewinne. Du ziehst {z} Lose (ohne Zurücklegen). Wie groß ist P(mindestens ein Gewinn)?', q,
                            f'Gegenereignis: nur Nieten. P(nur Nieten) = {" · ".join(teile)} = {br(nieten)}; P(mindestens ein Gewinn) = 1 − {br(nieten)} = {br(q)}.',
                            '„Mindestens ein“ – rechne über das Gegenereignis „nur Nieten“; bei jedem Zug ist eine Niete und ein Los weniger da.', c=frac_c(q))
    k = R.randint(4, 8)
    m = R.randint(12, 30)
    q = Fr(k, m) * Fr(k - 1, m - 1) * Fr(k - 2, m - 2)
    return bruch_luecke(f'In einer Lostrommel sind {m} Lose, davon {k} Gewinne. Jemand zieht drei Lose (ohne Zurücklegen). Wie groß ist P(drei Gewinne)?', q,
                        f'{k}/{m} · {k - 1}/{m - 1} · {k - 2}/{m - 2} = {br(q)}.', 'Bei jedem Zug fehlt ein Gewinnlos und ein Los insgesamt.', c=frac_c(q))


def g_gegenereignis(s):
    if s == 1:
        was, p, k = R.choice([('Ein Würfel wird {k}-mal geworfen. Wie groß ist P(mindestens eine Sechs)?', Fr(1, 6), R.randint(2, 3)),
                              ('Ein Würfel wird {k}-mal geworfen. Wie groß ist P(mindestens eine Eins)?', Fr(1, 6), R.randint(2, 3)),
                              ('Eine Münze wird {k}-mal geworfen. Wie groß ist P(mindestens einmal Kopf)?', Fr(1, 2), R.randint(2, 6)),
                              ('Ein Glücksrad mit 4 gleich großen Feldern (1 rot, 3 weiß) wird {k}-mal gedreht. Wie groß ist P(mindestens einmal rot)?', Fr(1, 4), R.randint(2, 4)),
                              ('Ein Glücksrad mit 5 gleich großen Feldern (2 rot, 3 weiß) wird {k}-mal gedreht. Wie groß ist P(mindestens einmal rot)?', Fr(2, 5), R.randint(2, 3))])
        q = 1 - (1 - p) ** k
        return bruch_luecke(was.format(k=k), q, f'P(keinmal) = ({br(1 - p)})^{k} = {br((1 - p) ** k)}; 1 − {br((1 - p) ** k)} = {br(q)}.',
                            'Rechne über das Gegenereignis „keinmal“.', c=frac_c(q))
    if s == 2:
        k = R.randint(2, 4)
        ding, pt = R.choice([(('Ein Bauteil ist mit der Wahrscheinlichkeit', 'defekt', 'mindestens ein defektes Bauteil', 'Bauteile werden geprüft'), Fr(R.choice([1, 2, 5]), 100)),
                             (('Ein Los ist mit der Wahrscheinlichkeit', 'ein Gewinn', 'mindestens einen Gewinn', 'Lose werden gekauft'), Fr(R.choice([1, 2, 3]), 10)),
                             (('Ein Elfmeter wird mit der Wahrscheinlichkeit', 'gehalten', 'mindestens einen gehaltenen Elfmeter', 'Elfmeter werden geschossen'), Fr(R.choice([1, 2, 3]), 10))])
        q = 1 - (1 - pt) ** k
        return zahl(f'{ding[0]} {dz(pt)} {ding[1]}. {k} {ding[3]} (unabhängig). Wie groß ist die Wahrscheinlichkeit für {ding[2]}?',
                    f'P(keinmal) = {dz(1 - pt)}^{k} = {dz((1 - pt) ** k)}; 1 − {dz((1 - pt) ** k)} = {dz(q)}.', 'Gegenereignis: keinmal.', q,
                    f'1 - (1 - {cf(pt)}) ** {k}')
    pt = Fr(R.choice([1, 2, 3, 5]), 10)
    ziel = R.choice([Fr(9, 10), Fr(95, 100), Fr(99, 100)])
    n = 1
    while 1 - (1 - pt) ** n < ziel: n += 1
    return zahl(f'Ein Spiel wird mit der Wahrscheinlichkeit {dz(pt)} gewonnen. Wie oft muss man mindestens spielen, um mit einer Wahrscheinlichkeit von mindestens {dz(ziel * 100)} % wenigstens einmal zu gewinnen?',
                f'1 − {dz(1 - pt)}ⁿ ≥ {dz(ziel)} ⇔ {dz(1 - pt)}ⁿ ≤ {dz(1 - ziel)}. Probieren oder logarithmieren: n = {n} ({dz(1 - pt)}^{n} ≈ {dz(round(float((1 - pt) ** n), 4))}).',
                'Stelle die Ungleichung über das Gegenereignis auf; n muss ganzzahlig sein.', n,
                f'-(-{K(math.log(float(1 - ziel)) / math.log(float(1 - pt)))} // 1)')


def g_baum_ergaenzen(s):
    if s == 1:
        p = Fr(R.randint(1, 19), 20)
        return zahl(f'Von einem Verzweigungspunkt gehen zwei Äste aus. Einer hat die Wahrscheinlichkeit {dz(p)}. Welche Wahrscheinlichkeit hat der andere?',
                    f'Beide Äste zusammen ergeben 1: 1 − {dz(p)} = {dz(1 - p)}.', 'Die Äste einer Verzweigung ergeben zusammen 1.', 1 - p, f'1 - {cf(p)}')
    pa = Fr(R.choice([2, 4, 5, 6, 8]), 10)
    pb = Fr(R.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]), 10)
    pab = pa * pb
    if s == 2:
        return mit_grafik(zahl(f'In einem zweistufigen Baumdiagramm ist P(A) = {dz(pa)} und die Wahrscheinlichkeit des Pfades „A, dann B“ = {dz(pab)}. Welche Wahrscheinlichkeit steht am Ast von A nach B?',
                               f'P(A) · x = {dz(pab)} ⇒ x = {dz(pab)} : {dz(pa)} = {dz(pb)}.', 'Pfadwahrscheinlichkeit = Produkt der Äste; teile.', pb,
                               f'{cf(pab)} / {cf(pa)}'),
                          {'typ': 'baum', 'aeste': [{'text': 'A', 'p': dz(pa), 'aeste': [{'text': 'B', 'p': '?'}, {'text': 'nicht B'}]},
                                                    {'text': 'nicht A', 'p': dz(1 - pa)}]})
    pa = Fr(R.choice([5, 10, 20]), 100)
    pb = Fr(R.choice([90, 95, 98]), 100)
    pc = Fr(R.choice([2, 5, 10]), 100)
    gesamt = pa * pb + (1 - pa) * pc
    return mit_grafik(zahl(f'Eine Krankheit ist bei {dz(pa * 100)} % der getesteten Tiere vorhanden. Ein Test zeigt bei kranken Tieren mit {dz(pb * 100)} % „positiv“, bei gesunden mit {dz(pc * 100)} %. Wie groß ist die Wahrscheinlichkeit für einen positiven Test?',
                           f'Zwei Pfade zu „positiv“: {dz(pa)} · {dz(pb)} + {dz(1 - pa)} · {dz(pc)} = {dz(gesamt)}.', 'Im Baum: erst krank/gesund, dann positiv/negativ. Welche Pfade enden bei „positiv“? Addiere sie.',
                           gesamt, f'{cf(pa)} * {cf(pb)} + (1 - {cf(pa)}) * {cf(pc)}'),
                      {'typ': 'baum', 'aeste': [{'text': 'krank', 'p': dz(pa), 'aeste': [{'text': 'positiv', 'p': dz(pb)}, {'text': 'negativ', 'p': dz(1 - pb)}]},
                                                {'text': 'gesund', 'p': dz(1 - pa), 'aeste': [{'text': 'positiv', 'p': dz(pc)}, {'text': 'negativ', 'p': dz(1 - pc)}]}]})


def g_simulation(s):
    if s == 1:
        n = R.choice([60, 120, 300, 600, 1200])
        satz, p = R.choice([('Ein Würfel wird {n}-mal geworfen. Wie oft erwartet man eine Sechs?', Fr(1, 6)),
                            ('Eine Münze wird {n}-mal geworfen. Wie oft erwartet man Kopf?', Fr(1, 2)),
                            ('Zwei Münzen werden {n}-mal gleichzeitig geworfen. Wie oft erwartet man zweimal Kopf?', Fr(1, 4)),
                            ('Ein Würfel wird {n}-mal geworfen. Wie oft erwartet man eine Zahl unter 3?', Fr(1, 3))])
        e = n * p
        if e.denominator != 1: return None
        return zahl(satz.format(n=dz(n)), f'Die Wahrscheinlichkeit ist {br(p)}. Erwartete Anzahl = n · p = {dz(n)} · {br(p)} = {dz(e)}.',
                    'Bestimme zuerst die Wahrscheinlichkeit für einen Wurf. Erwartete Anzahl = n · p.', e, f'{n} * {p.numerator} / {p.denominator}')
    if s == 2:
        n = R.choice([200, 250, 400, 500, 1000])
        t = R.randint(n // 10, n // 2)
        if not endlich(Fr(t, n)): return None
        return mit_grafik(zahl(f'Eine Simulation wurde {dz(n)}-mal durchgeführt; das Diagramm zeigt die Ergebnisse. Berechne die relative Häufigkeit von „Treffer“.',
                               f'{t} : {n} = {dz(Fr(t, n))}.', 'Relative Häufigkeit = Anzahl der Treffer : Anzahl aller Durchführungen.', Fr(t, n), f'{t} / {n}'),
                          {'typ': 'saeulen', 'einheit': 'Anzahl', 'werte': [{'name': 'Treffer', 'wert': t}, {'name': 'kein Treffer', 'wert': n - t}], 'zahlen': True})
    typ = R.random()
    if typ < 0.5:
        p = Fr(R.choice([1, 2, 3]), 10)
        k = 2
        e_einzel = p * p
        n = R.choice([100, 200, 500, 1000])
        e = n * e_einzel
        return zahl(f'Ein Zufallsgerät liefert mit der Wahrscheinlichkeit {dz(p)} einen Treffer. Es wird immer zweimal hintereinander gestartet; das wird {dz(n)}-mal wiederholt. Wie oft erwartet man „zwei Treffer“?',
                    f'P(zwei Treffer) = {dz(p)}² = {dz(e_einzel)}; erwartet {n} · {dz(e_einzel)} = {dz(e)}.', 'Erst die Pfadwahrscheinlichkeit, dann mal n.', e,
                    f'{n} * {cf(p)} ** 2')
    k = R.randint(3, 8)
    return auswahl(f'Bei einem Würfel kam {k}-mal hintereinander keine Sechs. Was gilt für den nächsten Wurf?', 'P(Sechs) ist weiterhin 1/6.',
                   ['Eine Sechs ist jetzt unwahrscheinlicher – der Würfel „liegt schlecht“.',
                    f'P(Sechs) = 1/6 + {k} · 1/36 = {br(Fr(1, 6) + Fr(k, 36))} – die Chance steigt mit jedem Fehlwurf.',
                    'Eine Sechs ist jetzt fällig, weil sie so lange nicht kam.'],
                   'Die Würfe sind unabhängig: Der Würfel „merkt“ sich nichts. Erst bei sehr vielen Würfen gleicht sich die relative Häufigkeit aus.',
                   'Hängt der nächste Wurf von den vorigen ab?')


PAARE = set()


def g_verstehen(s):
    typ = R.choice({1: 'ab', 2: 'abcd', 3: 'cde'}[s])
    if typ == 'a':
        f1, n1, a, f2, n2, b = urne()
        n = a + b
        q = Fr(a * a, n * n)
        return auswahl(f'In einer Urne liegen {a} {f1} und {b} {f2} Kugeln; es wird zweimal mit Zurücklegen gezogen. Jemand rechnet P({n1}, {n1}) = {a}/{n} + {a}/{n}. Was stimmt?',
                       f'Falsch: entlang des Pfades multiplizieren, P = {br(q)}.', ['Richtig.', f'Falsch: P = {a}/{n}.', f'Falsch: P = {br(Fr(a, n) * Fr(a - 1, n - 1))}.'],
                       f'Ein Pfad – Wahrscheinlichkeiten multiplizieren: {a}/{n} · {a}/{n} = {br(q)}.', 'Addieren oder multiplizieren entlang eines Pfades?')
    if typ == 'b':
        p = Fr(R.randint(1, 9), 10)
        q = Fr(R.randint(1, 9), 10)
        if p + q == 1 or frozenset((p, q)) in PAARE: return None
        PAARE.add(frozenset((p, q)))
        return auswahl(f'An einer Verzweigung stehen die Äste {dz(p)} und {dz(q)} (nur diese zwei). Was stimmt?', f'Das ist falsch, die Äste müssen zusammen 1 ergeben ({dz(p + q)} ≠ 1).',
                       ['Das ist möglich.', 'Das ist nur ohne Zurücklegen möglich.', 'Das ist nur mit Zurücklegen möglich.'],
                       'Von jedem Verzweigungspunkt aus ergeben die Äste zusammen 1 – eines der Ergebnisse tritt sicher ein.', 'Was ergibt die Summe aller Äste einer Verzweigung?')
    if typ == 'c':
        f1, n1, a, f2, n2, b = urne()
        n = a + b
        q = Fr(a, n) * Fr(a - 1, n - 1)
        return auswahl(f'{a} {f1} und {b} {f2} Kugeln, zwei Kugeln ohne Zurücklegen. Jemand rechnet P({n1}, {n1}) = {a}/{n} · {a}/{n}. Was stimmt?',
                       f'Falsch: Beim zweiten Zug sind es {a - 1} von {n - 1}, also P = {br(q)}.', ['Richtig.', f'Falsch: P = {a}/{n} + {a - 1}/{n - 1}.', f'Falsch: P = {a}/{n}.'],
                       f'Ohne Zurücklegen ändern sich Zähler und Nenner: {a}/{n} · {a - 1}/{n - 1} = {br(q)}.', 'Was ändert sich nach dem ersten Zug?')
    if typ == 'd':
        k = R.randint(2, 5)
        return auswahl(f'Jemand sagt: „Bei {k} Würfen ist P(mindestens eine Sechs) = {k} · 1/6 = {br(Fr(k, 6))}.“ Was stimmt?',
                       f'Falsch: richtig ist 1 − (5/6)^{k} ≈ {dz(round(1 - (5 / 6) ** k, 3))}.', ['Richtig.', f'Falsch: richtig ist (1/6)^{k}.', f'Falsch: richtig ist 1 − 1/6 · {k}.'],
                       'Pfade mit zwei oder mehr Sechsen würden mehrfach gezählt; deshalb über das Gegenereignis rechnen.', 'Was wäre bei 6 Würfen? Kann P = 1 sein?')
    p = Fr(R.choice([1, 2, 3]), 10)
    # Trefferzahl nahe am Erwartungswert 20 · p (nicht gleich), also gut möglich – kein starkes Indiz gegen p
    t = 20 * p + R.choice([-2, -1, 1, 2])
    if t < 0: return None
    return auswahl(f'Ein Zufallsgerät liefert mit {dz(p)} einen Treffer. In 20 Simulationen gab es {dz(t)} Treffer. Was folgt daraus?',
                   f'Nichts Sicheres: Bei wenigen Durchführungen schwankt die relative Häufigkeit stark ({dz(t / 20)} statt {dz(p)} ist gut möglich).',
                   ['Das Gerät ist sicher defekt.', f'Die Wahrscheinlichkeit ist nicht {dz(p)}.', 'Beim nächsten Mal gibt es sicher mehr Treffer.'],
                   'Erst bei vielen Durchführungen nähert sich die relative Häufigkeit der Wahrscheinlichkeit (Gesetz der großen Zahlen).', 'Wie zuverlässig sind 20 Versuche?')



# ---------- KLAR: verständliche Fassung der Lernkarten (Runde 7) ----------
# Wird erst nach dem Bauen der Aufgaben eingesetzt (bauen(..., klar=KLAR)), die Aufgaben bleiben wörtlich gleich.
KLAR = {
 'pfad_mult': {
  'einstieg': 'Beim Schulfest steht ein Säckchen mit 3 roten und 2 blauen Kugeln. Du ziehst ohne hinzusehen eine Kugel, merkst dir die Farbe '
              'und legst sie zurück. Dann ziehst du ein zweites Mal. Einen Preis gibt es nur für zweimal Rot. '
              'Den Ablauf zeichnet man als ⟦Baumdiagramm⟧: Jede Ziehung ist eine Stufe, jede mögliche Farbe ein Ast.',
  'woerter': [['Wahrscheinlichkeit P', 'wie wahrscheinlich ein Ergebnis ist, als Zahl von 0 (nie) bis 1 (sicher)'],
              ['P(rot) = 3/5', '3 von 5 Kugeln sind rot'],
              ['P(rot, rot)', 'die Wahrscheinlichkeit, erst Rot und dann wieder Rot zu ziehen'],
              ['mehrstufiges Zufallsexperiment', 'mehrere Zufallsschritte nacheinander, hier zweimal ziehen'],
              ['Baumdiagramm', 'eine Zeichnung, in der sich Äste verzweigen; an jedem Ast steht seine Wahrscheinlichkeit'],
              ['Pfad', 'ein Weg durch den Baum vom Anfang bis zum Ende, z. B. rot – rot'],
              ['mit Zurücklegen', 'die Kugel kommt wieder ins Säckchen; die Wahrscheinlichkeiten bleiben gleich']],
  'schritte': ['Beim ersten Ziehen sind 3 von 5 Kugeln rot: P(rot) = 3/5.',
               'Die Kugel wird zurückgelegt. Beim zweiten Ziehen ist P(rot) deshalb wieder 3/5.',
               'Im Baum führt der Pfad rot – rot über zwei Äste mit je 3/5. Zuerst ist in 3/5 der Fälle Rot dabei, und davon in 3/5 der Fälle noch einmal.',
               'Deshalb wird entlang des Pfades malgenommen: P(rot, rot) = 3/5 · 3/5 = ⟦9/25⟧.'],
  'regel': 'So berechnest du einen Pfad (1. Pfadregel): Die Wahrscheinlichkeit eines Pfades ist das ⟦Produkt der Wahrscheinlichkeiten entlang des Pfades⟧.',
  'fehler': 'P(rot, rot) = 3/5 + 3/5 = 6/5 ist falsch: Eine Wahrscheinlichkeit über 1 gibt es nicht. Zweimal Rot ist seltener als einmal Rot, '
            'deshalb wird entlang eines Pfades ⟦multipliziert⟧, nicht addiert.'},
 'pfad_add': {
  'einstieg': 'Zwei Freunde werfen eine Münze zweimal. Wer auf „genau einmal Kopf“ tippt, gewinnt. Das kann auf zwei Wegen passieren: '
              'erst Kopf, dann Zahl – oder erst Zahl, dann Kopf. Weil beide Wege zählen, werden ihre Wahrscheinlichkeiten zusammengezählt. '
              'Das ist die ⟦2. Pfadregel⟧.',
  'woerter': [['K, Z', 'Kopf und Zahl'],
              ['Ereignis', 'eine Beschreibung, zu der mehrere Ergebnisse gehören können, z. B. „genau einmal Kopf“'],
              ['(K, Z)', 'der Pfad: erster Wurf Kopf, zweiter Wurf Zahl'],
              ['½, ¼', 'ein Halb und ein Viertel'],
              ['2. Pfadregel', 'gehören mehrere Pfade zu einem Ereignis, addiert man ihre Wahrscheinlichkeiten']],
  'schritte': ['Zum Ereignis „genau einmal Kopf“ gehören zwei Pfade: (K, Z) und (Z, K).',
               'Pfad (K, Z): ½ · ½ = ¼. Pfad (Z, K): ebenfalls ½ · ½ = ¼.',
               'Beide Pfade führen zum Gewinn, deshalb werden sie addiert: ¼ + ¼.',
               'Ergebnis: P(genau einmal Kopf) = ⟦½⟧.'],
  'regel': 'So berechnest du ein Ereignis (2. Pfadregel): Alle ⟦Pfade suchen⟧, die dazugehören, jeden Pfad wie gewohnt multiplizieren und die Ergebnisse ⟦addieren⟧.',
  'fehler': 'Bei „genau einmal Kopf“ nur den Pfad (K, Z) zu zählen ist falsch: Auch ⟦(Z, K)⟧ gehört dazu – für den Tipp ist die Reihenfolge egal.'},
 'ohne_zuruecklegen': {
  'einstieg': 'In einer Tüte sind 3 rote und 2 blaue Bonbons. Du nimmst eins, isst es auf und nimmst dann noch eins. '
              'Beim zweiten Mal sind nur noch 4 Bonbons in der Tüte – und wenn das erste rot war, nur noch 2 rote. '
              'Dieses Vorgehen heißt ⟦Ziehen ohne Zurücklegen⟧.',
  'woerter': [['ohne Zurücklegen', 'was gezogen ist, kommt nicht zurück; beim nächsten Ziehen sind es weniger'],
              ['erste und zweite Stufe', 'das erste und das zweite Ziehen im Baum'],
              ['Zähler, Nenner', 'die Zahl über und die Zahl unter dem Bruchstrich'],
              ['2/4', 'nach einem roten Bonbon: noch 2 rote von 4 Bonbons']],
  'schritte': ['Beim ersten Griff sind 3 von 5 Bonbons rot: P(rot) = 3/5.',
               'Das rote Bonbon ist gegessen. Jetzt sind noch 4 Bonbons da, davon 2 rote: Der zweite Ast hat 2/4.',
               'Entlang des Pfades malnehmen: P(rot, rot) = 3/5 · 2/4 = 6/20.',
               'Kürzen ergibt ⟦3/10⟧.'],
  'regel': 'So rechnest du ohne Zurücklegen: Auf der zweiten Stufe ⟦ändern sich die Wahrscheinlichkeiten⟧. Im Nenner steht eins weniger, '
           'und ist dieselbe Sorte gemeint, auch im Zähler eins weniger.',
  'fehler': 'P(rot, rot) = 3/5 · 3/5 gilt nur ⟦mit⟧ Zurücklegen. Das erste rote Bonbon ist aber schon gegessen: Es bleiben 2 rote von 4.'},
 'gegenereignis': {
  'einstieg': 'Bei einem Brettspiel darfst du erst losziehen, wenn du eine Sechs würfelst, und du hast drei Versuche. Wie wahrscheinlich ist mindestens eine Sechs? '
              'Dazu gehören viele Pfade: Sechs im ersten Wurf, im zweiten, im dritten, zweimal … Viel kürzer ist die Gegenfrage: '
              'Wie wahrscheinlich ist gar keine Sechs? Diese Gegenfrage heißt ⟦Gegenereignis⟧.',
  'woerter': [['mindestens einmal', 'einmal oder öfter'],
              ['Gegenereignis', 'genau das Gegenteil, hier „keinmal eine Sechs“'],
              ['P(keinmal)', 'die Wahrscheinlichkeit, dass es nie eintritt'],
              ['(5/6)³', '5/6 · 5/6 · 5/6: dreimal keine Sechs'],
              ['1 − P', 'Ereignis und Gegenereignis ergeben zusammen 1, denn eines von beiden tritt sicher ein'],
              ['≈', '„ungefähr gleich“']],
  'schritte': ['Bei einem Wurf kommt mit der Wahrscheinlichkeit 5/6 keine Sechs.',
               'Dreimal keine Sechs ist ein einziger Pfad: (5/6)³ = 125/216.',
               '„Mindestens eine Sechs“ ist alles andere. Zusammen ergeben beide 1.',
               'Also ist P(mindestens eine Sechs) = 1 − 125/216 = ⟦91/216⟧ ≈ 0,42.'],
  'regel': 'So rechnest du bei „⟦mindestens einmal⟧“: über das ⟦Gegenereignis „keinmal“⟧. P(mindestens einmal) = 1 − P(keinmal).',
  'fehler': 'P(mindestens eine Sechs) = 3 · 1/6 = ½ ist falsch: So werden Pfade mit mehreren Sechsen ⟦mehrfach gezählt⟧. '
            'Bei sechs Würfen käme sogar 1 heraus – als wäre eine Sechs dann sicher. Über das Gegenereignis rechnen.'},
 'baum_ergaenzen': {
  'einstieg': 'In einer Stadt regnet es an 40 % aller Tage. An 10 % aller Tage regnet es und es gibt zugleich Stau. '
              'An welchem Anteil der Regentage gibt es also Stau? Diese Zahl gehört an einen Ast, der im Baum noch leer ist. '
              'Fehlende Zahlen findet man beim ⟦Baumdiagramm vervollständigen⟧.',
  'woerter': [['A, B', 'Namen für Ereignisse, hier A: Regen, B: Stau'],
              ['nicht A', 'das Gegenereignis: kein Regen'],
              ['Verzweigungspunkt', 'eine Stelle im Baum, an der sich Äste teilen'],
              ['P(A und B)', 'die Wahrscheinlichkeit des Pfades „A, dann B“'],
              ['Gegenast', 'der andere Ast an derselben Verzweigung'],
              ['0,4', '40 % als Dezimalzahl']],
  'schritte': ['Bekannt sind der erste Ast P(A) = 0,4 und der Pfad P(A und B) = 0,1.',
               'Für den Pfad gilt: 0,4 mal der zweite Ast ergibt 0,1.',
               'Also ist der zweite Ast 0,1 : 0,4 = ⟦0,25⟧. An einem Viertel der Regentage gibt es Stau.',
               'Die Äste an einer Verzweigung ergeben zusammen 1: Der Gegenast „nicht B“ hat 1 − 0,25 = 0,75, der Ast „nicht A“ hat 1 − 0,4 = 0,6.'],
  'regel': 'So vervollständigst du: Die Äste von ⟦einem Verzweigungspunkt⟧ ergeben zusammen ⟦1⟧. Kennst du einen Pfad und seinen ersten Ast, '
           'findest du den zweiten Ast durch ⟦Teilen⟧.',
  'fehler': 'Den zweiten Ast als 0,1 − 0,4 oder 0,1 + 0,4 zu berechnen ist falsch: Der Pfad ist das Produkt der Äste, also muss man ⟦teilen⟧: 0,1 : 0,4 = 0,25.'},
 'simulation': {
  'einstieg': 'Wirfst du zwei Würfel, zeigen sie manchmal dieselbe Zahl – das heißt Pasch. Von 36 möglichen Ergebnissen sind 6 ein Pasch, also ein Sechstel. '
              'Würfelst du 600-mal, erwartest du etwa 100 Pasche, aber selten genau 100. Wie oft etwas tatsächlich vorkam, '
              'geteilt durch die Zahl aller Versuche, heißt ⟦relative Häufigkeit⟧.',
  'woerter': [['Pasch', 'beide Würfel zeigen dieselbe Zahl'],
              ['n', 'die Anzahl der Durchführungen, hier 600'],
              ['p', 'die Wahrscheinlichkeit für einen Treffer, hier 1/6'],
              ['n · p', 'die erwartete Anzahl der Treffer'],
              ['relative Häufigkeit', 'Treffer geteilt durch alle Versuche'],
              ['Simulation', 'den Zufallsversuch nachspielen, z. B. mit Würfeln oder am Computer']],
  'bild': {'typ': 'saeulen', 'einheit': 'Anzahl in 600 Würfen', 'werte': [{'name': 'Pasch', 'wert': 94}, {'name': 'kein Pasch', 'wert': 506}], 'zahlen': True},
  'schritte': ['Bei zwei Würfeln gibt es 6 · 6 = 36 Ergebnisse, davon sind 6 ein Pasch (1-1, 2-2, …, 6-6). Also ist p = 6/36 = 1/6.',
               'Es wird n = 600-mal gewürfelt.',
               'Erwartet werden n · p = 600 · 1/6 = ⟦100⟧ Pasche.',
               'Eine Simulation ergab 94 Pasche. Die relative Häufigkeit 94 : 600 ≈ 0,157 liegt nah bei 1/6 ≈ 0,167.'],
  'regel': 'So schätzt du ab: Bei n Durchführungen erwartest du etwa ⟦n · p⟧ Treffer. Die ⟦relative Häufigkeit⟧ schwankt, '
           'nähert sich aber bei vielen Durchführungen der Wahrscheinlichkeit.',
  'fehler': '„Nach 5 Würfen ohne Sechs kommt die Sechs jetzt wahrscheinlicher“ ist falsch: Der Würfel weiß nicht, was vorher kam – er hat ⟦kein Gedächtnis⟧. P bleibt 1/6.'},
 'verstehen': {
  'einstieg': 'Jemand sagt: „Wenn ich zweimal eine Münze werfe, kommt sicher zweimal Kopf – ein Halb plus ein Halb ist ja 1.“ Stimmt das? '
              'Bei Wahrscheinlichkeiten hilft eine Prüfliste: Wird richtig malgenommen und zusammengezählt? Bleiben die Zahlen zwischen 0 und 1? '
              'Mit ihr kann man ⟦Aussagen prüfen⟧.',
  'woerter': [['entlang eines Pfades', 'auf einem Weg durch den Baum: malnehmen'],
              ['zwischen Pfaden', 'mehrere Wege zum selben Ereignis: addieren'],
              ['P = 1', 'das Ereignis ist sicher'],
              ['Prüfliste', 'die Fragen aus dem Merksatz unten']],
  'schritte': ['Behauptung: Bei zweimal Münzwurf ist P(zweimal Kopf) = ½ + ½ = 1.',
               'Zweimal Kopf ist ein einziger Pfad: erst Kopf, dann Kopf.',
               'Entlang eines Pfades wird malgenommen: ½ · ½ = ¼.',
               'Die Behauptung ist ⟦falsch⟧. P = 1 hieße „sicher“, aber zweimal Kopf ist nicht sicher.'],
  'regel': 'So prüfst du: Wird ⟦entlang⟧ eines Pfades multipliziert und ⟦zwischen⟧ Pfaden addiert? Ändern sich die Wahrscheinlichkeiten ⟦ohne Zurücklegen⟧? '
           'Ergeben die Äste an jeder Verzweigung 1?',
  'fehler': 'Wahrscheinlichkeiten über 1 gibt es nicht. Sie sind immer ein Hinweis auf einen ⟦Rechenfehler⟧ – meistens wurde addiert statt multipliziert.'},
}

GEN = schoen({'pfad_mult': g_pfad_mult, 'pfad_add': g_pfad_add, 'ohne_zuruecklegen': g_ohne_zuruecklegen, 'gegenereignis': g_gegenereignis,
              'baum_ergaenzen': g_baum_ergaenzen, 'simulation': g_simulation, 'verstehen': g_verstehen})

if __name__ == '__main__':
    bauen('stochastik.mehrstufig',
          'Mehrstufige Zufallsexperimente mit Pfadregeln berechnen (mit und ohne Zurücklegen), über das Gegenereignis rechnen und Simulationen deuten.',
          ['1. Pfadregel: entlang eines Pfades multiplizieren.', '2. Pfadregel: Pfade eines Ereignisses addieren.',
           'Ohne Zurücklegen ändern sich die Wahrscheinlichkeiten der zweiten Stufe.', 'P(mindestens einmal) = 1 − P(keinmal); erwartete Anzahl = n · p.'],
          [('Pfadregeln', ['pfad_mult', 'pfad_add', 'ohne_zuruecklegen']), ('Strategien', ['gegenereignis', 'baum_ergaenzen']), ('Simulation und Verstehen', ['simulation', 'verstehen'])],
          ETAPPEN, GEN, klar=KLAR,
          meiden={'pfad_mult': ['3 rote und 2 blaue Kugeln. Es wird zweimal mit Zurücklegen'], 'ohne_zuruecklegen': ['3 rote und 2 blaue Kugeln. Es werden zwei'],
                  'gegenereignis': ['3-mal geworfen'], 'simulation': ['Pasch']},
          offen=['Prüfung eingearbeitet (Runde 3): Baumdiagramme (Bildtyp „baum“) in den Lernkarten pfad_mult, pfad_add, ohne_zuruecklegen, gegenereignis, baum_ergaenzen sowie in Aufgaben (Pfadregel Stufe 1, ohne Zurücklegen mit „?“ auf der 2. Stufe, Baum ergänzen, Test bei Tieren); die Pfad-Tabellen entfallen. Neu: „mindestens ein Gewinn“ ohne Zurücklegen; Freiwurfquoten 0,6–0,9; keine Ablenker über 1; Ast-Paare nicht nur vertauscht; Simulationsergebnisse nahe am Erwartungswert.',
                 'Simulation: nur Auswertung (relative Häufigkeit, erwartete Anzahl, Gesetz der großen Zahlen). Selbst simulieren (Zufallszahlen erzeugen) kann das Kind in der App nicht.',
                 'Brüche als Antwort über Lücken „□/□“ (gekürzt).'])
