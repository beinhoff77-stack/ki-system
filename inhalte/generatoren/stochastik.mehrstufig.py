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



# ---------- KLAR: Lernkarten im neuen Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst nach dem Bauen der Aufgaben eingesetzt (bauen(..., klar=KLAR)), die Aufgaben bleiben wörtlich gleich.
# Muster: einstieg (≤ 35 Wörter) → Kartenbild → Schritte als {text, bild} (Bildergeschichte) → „Pass auf!“ (fehler + fehler_bild) → MERKE (regel).
# Ein Baum-Bild hat keine Markierung; die Bildergeschichte zeigt den Baum deshalb Stufe für Stufe oder nur mit den gemeinten Pfaden.
def _ast(t, p, *k):
    a = {'text': t, 'p': p}
    if k: a['aeste'] = list(k)
    return a
_RB = lambda p_rot, p_blau: [_ast('rot', p_rot), _ast('blau', p_blau)]
_SCHULFEST = {'typ': 'baum', 'aeste': [_ast('rot', '3/5', *_RB('3/5', '2/5')), _ast('blau', '2/5', *_RB('3/5', '2/5'))]}
_MUENZE = {'typ': 'baum', 'aeste': [_ast('K', '1/2', _ast('K', '1/2'), _ast('Z', '1/2')), _ast('Z', '1/2', _ast('K', '1/2'), _ast('Z', '1/2'))]}
_BONBON = {'typ': 'baum', 'aeste': [_ast('rot', '3/5', *_RB('2/4', '2/4')), _ast('blau', '2/5', *_RB('3/4', '1/4'))]}
_SECHS = {'typ': 'baum', 'aeste': [_ast('6', '1/6'), _ast('keine 6', '5/6', _ast('6', '1/6'), _ast('keine 6', '5/6', _ast('6', '1/6'), _ast('keine 6', '5/6')))]}
def _regen(b='?', nb='?', na='?'):
    return {'typ': 'baum', 'aeste': [_ast('A: Regen', '0,4', _ast('B: Stau', b), _ast('nicht B', nb)), _ast('nicht A', na)]}
_PASCH = {'typ': 'saeulen', 'einheit': 'Anzahl in 600 Würfen', 'werte': [{'name': 'Pasch', 'wert': 94}, {'name': 'kein Pasch', 'wert': 506}], 'zahlen': True}

KLAR = {
 'pfad_mult': {
  'einstieg': 'Beim Schulfest ziehst du aus 3 roten und 2 blauen Kugeln. Du legst die Kugel zurück und ziehst noch einmal. '
              'Den Ablauf zeigt ein ⟦Baumdiagramm⟧.',
  'woerter': [['Baumdiagramm', 'jede Ziehung ist eine Stufe, jede mögliche Farbe ein Ast'],
              ['Ast', 'eine Linie im Baum mit ihrer Wahrscheinlichkeit'],
              ['Pfad', 'ein Weg durch den Baum bis zu einem Ende']],
  'bild': _SCHULFEST,
  'schritte': [{'text': 'Erster Zug: 3 von 5 Kugeln sind rot. Der Ast „rot“ hat 3/5.',
                'bild': {'aeste': [_ast('rot', '3/5'), _ast('blau', '2/5')]}},
               {'text': 'Die Kugel kommt zurück. Beim zweiten Zug gilt wieder 3/5.', 'bild': {'aeste': _SCHULFEST['aeste']}},
               {'text': 'Der Pfad rot – rot führt über zwei Äste mit je 3/5.',
                'bild': {'aeste': [_ast('rot', '3/5', _ast('rot', '3/5'))]}},
               {'text': 'Entlang des Pfades malnehmen: 3/5 · 3/5 = ⟦9/25⟧.'}],
  'fehler': '3/5 + 3/5 = 6/5 ist falsch. Über 1 gibt es nicht. Zweimal Rot ist seltener als einmal Rot. Also ⟦multiplizieren⟧.',
  'fehler_bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 1.2, 'abschnitte': 6, 'beschriftet': 'alle', 'bereich': {'von': 0, 'bis': 1},
                  'punkte': [{'wert': 0.36, 'name': '9/25'}, {'wert': 1.2, 'name': '6/5: unmöglich'}]},
  'regel': 'Entlang eines Pfades wird multipliziert. Das ist die ⟦1. Pfadregel⟧.'},
 'pfad_add': {
  'einstieg': 'Zwei Freunde werfen eine Münze zweimal. Wer auf „genau einmal Kopf“ tippt, gewinnt. Das klappt auf zwei Wegen. '
              'Dafür gibt es die ⟦2. Pfadregel⟧.',
  'woerter': [['K, Z', 'Kopf und Zahl'],
              ['Ereignis', 'alles, worauf man tippt; oft mehrere Pfade']],
  'bild': _MUENZE,
  'schritte': [{'text': 'Zum Ereignis „genau einmal Kopf“ gehören zwei Pfade: (K, Z) und (Z, K).',
                'bild': {'aeste': [_ast('K', '1/2', _ast('Z', '1/2')), _ast('Z', '1/2', _ast('K', '1/2'))]}},
               {'text': 'Jeder Pfad hat 1/2 · 1/2 = 1/4.'},
               {'text': 'Beide Pfade zählen. Also addieren: 1/4 + 1/4 = ⟦1/2⟧.'}],
  'fehler': 'Nur (K, Z) zu zählen ist falsch. Auch ⟦(Z, K)⟧ ist genau einmal Kopf. Für den Tipp ist die Reihenfolge egal.',
  'fehler_bild': {'typ': 'tabelle', 'kopf': ['Pfad', 'genau einmal Kopf?'],
                  'zeilen': [['(K, K)', 'nein'], ['(K, Z)', 'ja'], ['(Z, K)', 'ja'], ['(Z, Z)', 'nein']]},
  'regel': 'Die Pfade eines Ereignisses werden addiert. Jeden Pfad vorher ⟦multiplizieren⟧.'},
 'ohne_zuruecklegen': {
  'einstieg': 'In einer Tüte sind 3 rote und 2 blaue Bonbons. Du isst eins und nimmst dann noch eins. '
              'Das ist ⟦Ziehen ohne Zurücklegen⟧.',
  'woerter': [['ohne Zurücklegen', 'was gezogen ist, kommt nicht zurück'],
              ['Nenner', 'die Zahl unter dem Bruchstrich: wie viele noch da sind']],
  'bild': _BONBON,
  'schritte': [{'text': 'Erster Griff: 3 von 5 Bonbons sind rot. Der Ast hat 3/5.',
                'bild': {'aeste': [_ast('rot', '3/5'), _ast('blau', '2/5')]}},
               {'text': 'Das rote ist gegessen. Übrig sind 2 rote von 4. Der Nenner ist jetzt 4.',
                'bild': {'aeste': [_ast('rot', '3/5', *_RB('2/4', '2/4')), _ast('blau', '2/5')]}},
               {'text': 'Pfad rot – rot: 3/5 · 2/4 = 6/20 = ⟦3/10⟧.', 'bild': {'aeste': _BONBON['aeste']}}],
  'fehler': '3/5 · 3/5 gilt nur ⟦mit⟧ Zurücklegen. Das erste rote Bonbon ist schon gegessen. Es bleiben 2 rote von 4.',
  'fehler_bild': {'typ': 'tabelle', 'kopf': ['', '1. Griff', '2. Griff (nach Rot)'], 'zeilen': [['rote', '3', '2'], ['alle', '5', '4']]},
  'regel': 'Ohne Zurücklegen ändern sich die Äste der zweiten Stufe. ⟦Im Nenner eins weniger⟧, bei gleicher Sorte auch im Zähler.'},
 'gegenereignis': {
  'einstieg': 'Beim Brettspiel brauchst du eine Sechs und hast drei Versuche. Wie wahrscheinlich ist mindestens eine Sechs? '
              'Kürzer ist die Gegenfrage: gar keine Sechs. Sie heißt ⟦Gegenereignis⟧.',
  'woerter': [['Gegenereignis', 'alles, was nicht zum Ereignis gehört'],
              ['mindestens eine', 'eine oder mehr']],
  'bild': _SECHS,
  'schritte': [{'text': 'Zu „mindestens eine Sechs“ gehören viele Pfade.'},
               {'text': 'Das Gegenereignis „keine Sechs“ ist nur ein Pfad.',
                'bild': {'aeste': [_ast('keine 6', '5/6', _ast('keine 6', '5/6', _ast('keine 6', '5/6')))]}},
               {'text': 'Dieser Pfad: 5/6 · 5/6 · 5/6 = 125/216.'},
               {'text': 'Beide zusammen ergeben 1. Also 1 − 125/216 = ⟦91/216⟧ ≈ 0,42.', 'bild': {'aeste': _SECHS['aeste']}}],
  'fehler': '3 · 1/6 = 1/2 ist falsch. So zählt man Pfade mit mehreren Sechsen ⟦mehrfach⟧. Bei sechs Würfen käme sonst 1 heraus.',
  'fehler_bild': {'typ': 'tabelle', 'kopf': ['Würfe', 'falsch: Anzahl · 1/6', 'richtig: 1 − (5/6)^Anzahl'],
                  'zeilen': [['3', '0,5', '≈ 0,42'], ['6', '1 (sicher?)', '≈ 0,67']]},
  'regel': 'Bei „mindestens einmal“ über das Gegenereignis rechnen. ⟦P = 1 − P(keinmal)⟧.'},
 'baum_ergaenzen': {
  'einstieg': 'In einer Stadt regnet es an 40 % der Tage. An 10 % der Tage gibt es Regen und Stau. '
              'Fehlende Äste findet man beim ⟦Baumdiagramm vervollständigen⟧.',
  'woerter': [['Verzweigung', 'ein Punkt, an dem sich der Baum teilt'],
              ['Pfad', 'ein Weg durch den Baum; seine Wahrscheinlichkeit ist das Produkt der Äste']],
  'bild': _regen(),
  'schritte': [{'text': 'Bekannt: P(A) = 0,4. Der Pfad Regen und Stau hat 0,1.'},
               {'text': 'Pfad: 0,4 · Ast = 0,1. Also Ast = 0,1 : 0,4 = 0,25.', 'bild': _regen('0,25')},
               {'text': 'Die Äste einer Verzweigung ergeben 1. „Nicht B“ hat 0,75.', 'bild': _regen('0,25', '0,75')},
               {'text': 'Ebenso hat „nicht A“ 1 − 0,4 = ⟦0,6⟧.', 'bild': _regen('0,25', '0,75', '0,6')}],
  'fehler': '0,1 − 0,4 oder 0,1 + 0,4 ist falsch. Der Pfad ist ein Produkt. Also wird ⟦geteilt⟧: 0,1 : 0,4 = 0,25.',
  'fehler_bild': _regen('0,1 : 0,4 = 0,25'),
  'regel': 'Äste an einer Verzweigung ergeben zusammen 1. Einen fehlenden Ast findest du durch ⟦Teilen⟧.'},
 'simulation': {
  'einstieg': 'Zeigen zwei Würfel dieselbe Zahl, heißt das Pasch. Bei 600 Würfen erwartest du etwa 100 Pasche. '
              'Wie oft es wirklich passiert, zeigt die ⟦relative Häufigkeit⟧.',
  'woerter': [['Pasch', 'beide Würfel zeigen dieselbe Zahl'],
              ['relative Häufigkeit', 'Anzahl der Treffer geteilt durch die Anzahl der Versuche'],
              ['Simulation', 'den Versuch oft durchführen oder nachspielen und zählen']],
  'bild': _PASCH,
  'schritte': [{'text': 'Zwei Würfel haben 36 Ergebnisse, davon 6 Pasche. Also p = 1/6.'},
               {'text': 'Bei n = 600 Würfen erwartet man 600 · 1/6 = ⟦100⟧ Pasche.',
                'bild': {'einheit': 'erwartet in 600 Würfen', 'werte': [{'name': 'Pasch', 'wert': 100}, {'name': 'kein Pasch', 'wert': 500}]}},
               {'text': 'Die Simulation ergab 94 Pasche. Relative Häufigkeit: 94 : 600 ≈ 0,157.', 'bild': _PASCH},
               {'text': 'Das liegt nah bei 1/6 ≈ 0,167. Mit mehr Würfen wird es meist genauer.'}],
  'fehler': '„Nach 5 Würfen ohne Sechs kommt sie eher“ ist falsch. Der Würfel hat ⟦kein Gedächtnis⟧. P bleibt 1/6.',
  'regel': 'Bei n Versuchen erwartest du etwa ⟦n · p⟧ Treffer. Die relative Häufigkeit schwankt um p.'},
 'verstehen': {
  'einstieg': 'Jemand sagt: „Bei zwei Münzwürfen kommt sicher zweimal Kopf. 1/2 plus 1/2 ist ja 1.“ Stimmt das? '
              'Mit einer Prüfliste kann man ⟦Aussagen prüfen⟧.',
  'woerter': [['entlang eines Pfades', 'auf einem Weg durch den Baum: malnehmen'],
              ['Behauptung', 'eine Aussage, die man prüfen will']],
  'bild': _MUENZE,
  'schritte': [{'text': 'Behauptung: P(zweimal Kopf) = 1/2 + 1/2 = 1.'},
               {'text': 'Zweimal Kopf ist ein einziger Pfad: erst Kopf, dann Kopf.', 'bild': {'aeste': [_ast('K', '1/2', _ast('K', '1/2'))]}},
               {'text': 'Entlang eines Pfades wird malgenommen: 1/2 · 1/2 = 1/4.'},
               {'text': 'Die Behauptung ist ⟦falsch⟧. P = 1 hieße sicher.', 'bild': {'aeste': _MUENZE['aeste']}}],
  'fehler': 'Wahrscheinlichkeiten über 1 gibt es nicht. Sie zeigen einen ⟦Rechenfehler⟧. Meist wurde addiert statt multipliziert.',
  'regel': 'Prüfe: Entlang eines Pfades multiplizieren, zwischen Pfaden addieren. ⟦Ergebnis zwischen 0 und 1⟧?'},
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
