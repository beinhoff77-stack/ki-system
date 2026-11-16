#!/usr/bin/env python3
"""Thema stochastik.mehrstufig – Mehrstufige Zufallsexperimente (Klasse 10)."""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import *  # noqa: E402,F403
from _schwer_kl10 import ergaenzen  # noqa: E402

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

# ---------- Zehnte Runde (Zweig schwer-kl10): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Zufallsstart (nur zum Mischen der Antworten); wird erst NACH bauen(...) aufgerufen, alte Aufgaben bleiben gleich.
# Vorbilder (Typ und Niveau, eigene Zahlen und Einkleidung): Abitur Bayern Prüfungsteil A Stochastik (2023: Ereignis zu einem Term wie (3/4)⁵
# angeben, ohne Zurücklegen; 2025: Produkt zweier Würfe – P(X = 10) = P(X = 15) begründen, Term für n Würfe; IlluPA A7: Augensumme dreier
# Würfel), Realschul-Abschlussprüfung Bayern 2024 A 2 (Ziehen bis zur ersten B-Kugel, „bei welchem Zug sicher?“), Bayerischer
# Mathematik-Test 10 (2010 Aufgabe 6: genau ein Treffer bei zwei verschiedenen Wahrscheinlichkeiten, Gegenereignis als Term; 2025 Aufgabe 2:
# Zahl der Ergebnisse, relative Häufigkeit), ZP10 NRW ohne Hilfsmittel (Urneninhalt aus dem Baumdiagramm), LehrplanPLUS M10 2 (Simulation, π).
def schwer():
    start(10016)
    N = []

    def neu(l, s, a):
        a['l'], a['s'] = l, s
        N.append(a)

    def bl(text, q, w, h):
        q = Fr(q)
        return bruch_luecke(text, q, w, h, c=frac_c(q))

    # --- pfad_mult ---
    neu('pfad_mult', 2, zahl('Zwei verschiedene Glücksräder werden je einmal gedreht. Das erste zeigt „rot“ mit 0,4, das zweite mit 0,25. Wie groß ist P(beide rot)?',
                             'Ein Pfad: 0,4 · 0,25 = 0,1.', 'Entlang des Pfades multiplizieren.', 0.1, '0.4 * 0.25'))
    neu('pfad_mult', 2, bl('Ein Würfel wird dreimal geworfen. Wie groß ist die Wahrscheinlichkeit, dass drei verschiedene Augenzahlen fallen?', Fr(5, 9),
                           'Der erste Wurf ist beliebig (6/6), der zweite muss anders sein (5/6), der dritte anders als beide (4/6): 1 · 5/6 · 4/6 = 20/36 = 5/9.',
                           'Wie viele „erlaubte“ Augenzahlen hat jeder Wurf noch?'))
    neu('pfad_mult', 3, auswahl('Ein Glücksrad hat 4 gleich große Felder, eines davon blau. Es wird 6-mal gedreht. Welches Ereignis hat die Wahrscheinlichkeit (3/4)⁶?',
                                'Blau erscheint kein einziges Mal.', ['Blau erscheint genau einmal.', 'Blau erscheint mindestens einmal.', 'Blau erscheint bei jeder Drehung.'],
                                '3/4 ist die Wahrscheinlichkeit für „nicht blau“. Sechsmal hintereinander „nicht blau“: (3/4)⁶.',
                                'Wofür steht 3/4 bei einer Drehung?'))
    neu('pfad_mult', 3, bruch_luecke('Ein Glücksrad mit den Ziffern 1, 2, 3, 4 (gleich große Felder) wird 6-mal gedreht; die Ziffern ergeben eine sechsstellige Zahl. Wie wahrscheinlich ist genau die Zahl 123 412?',
                                     Fr(1, 4096), 'Ein einziger Pfad mit sechs Ästen zu je 1/4: (1/4)⁶ = 1/4 096. Es gibt 4⁶ = 4 096 gleich wahrscheinliche Zahlen.',
                                     'Jede Stelle ist eine eigene Stufe.', c=['1', '4 ** 6']))
    neu('pfad_mult', 3, zahl('Eine Münze wird mehrmals geworfen. Wie oft muss man sie mindestens werfen, damit die Wahrscheinlichkeit für „jedes Mal Zahl“ kleiner als 1 % ist?',
                             '0,5ⁿ < 0,01: 0,5⁶ ≈ 0,0156, 0,5⁷ ≈ 0,0078. Also mindestens 7 Würfe.', 'Probiere 0,5⁵, 0,5⁶, 0,5⁷ …', 7, '7'))
    neu('pfad_mult', 3, zahl('A und B sind zwei unabhängige Stufen eines Zufallsexperiments. Es gilt P(A) = 0,3 und P(A, dann B) = 0,12. Wie groß ist P(B)?',
                             'Pfadregel rückwärts: 0,3 · P(B) = 0,12 ⇒ P(B) = 0,4.', 'Die Pfadwahrscheinlichkeit ist ein Produkt. Welcher Faktor fehlt?', 0.4, '0.12 / 0.3'))

    # --- pfad_add ---
    neu('pfad_add', 2, bl('Zwei Würfel werden geworfen. Wie groß ist die Wahrscheinlichkeit für die Augensumme 4?', Fr(1, 12),
                          'Pfade (1, 3), (2, 2), (3, 1): 3 · 1/36 = 3/36 = 1/12.', 'Schreibe alle Paare mit der Summe 4 auf.'))
    neu('pfad_add', 2, zahl('Bei einer Torwand trifft ein Kind oben mit 30 %, unten mit 60 %. Es schießt einmal oben und einmal unten. Wie groß ist P(genau ein Treffer)?',
                            'Treffer oben, unten nicht: 0,3 · 0,4 = 0,12. Oben nicht, unten Treffer: 0,7 · 0,6 = 0,42. Zusammen 0,54.',
                            'Genau ein Treffer: zwei Pfade. Jeden multiplizieren, dann addieren.', 0.54, '0.3 * 0.4 + 0.7 * 0.6'))
    neu('pfad_add', 3, bl('Zwei Würfel werden geworfen und die Augenzahlen multipliziert. Wie groß ist P(Produkt = 12)?', Fr(1, 9),
                          'Pfade (2, 6), (6, 2), (3, 4), (4, 3): 4 · 1/36 = 1/9.', 'Zerlege 12 in zwei Faktoren zwischen 1 und 6 – auf beide Reihenfolgen achten.'))
    neu('pfad_add', 3, auswahl('Zwei Würfel werden geworfen, X ist das Produkt der Augenzahlen. Warum gilt P(X = 10) = P(X = 15)?',
                               'Zu beiden gehören genau zwei Pfade: (2, 5), (5, 2) bzw. (3, 5), (5, 3).',
                               ['Weil 10 und 15 beide durch 5 teilbar sind.', 'Weil jedes Produkt gleich wahrscheinlich ist.', 'Weil 15 − 10 = 5 eine Augenzahl ist.'],
                               'Alle 36 Pfade sind gleich wahrscheinlich. Gleich viele Pfade bedeuten gleiche Wahrscheinlichkeit: je 2/36. (Nicht jedes Produkt ist gleich wahrscheinlich: X = 12 hat 4 Pfade.)',
                               'Zähle für beide Produkte die passenden Würfelpaare.'))
    neu('pfad_add', 3, bl('Drei Würfel werden geworfen. Wie groß ist die Wahrscheinlichkeit, dass die Augensumme mindestens 17 ist?', Fr(1, 54),
                          'Summe 18: nur (6, 6, 6). Summe 17: (5, 6, 6), (6, 5, 6), (6, 6, 5). Vier Pfade von 216: 4/216 = 1/54.',
                          'Welche Würfe ergeben 18, welche 17? Achte auf die Reihenfolge.'))
    neu('pfad_add', 3, bl('Eine Münze wird viermal geworfen. Wie groß ist P(genau zweimal Kopf)?', Fr(3, 8),
                          'Pfade mit genau zwei K: KKZZ, KZKZ, KZZK, ZKKZ, ZKZK, ZZKK – das sind 6, je (1/2)⁴ = 1/16. Also 6/16 = 3/8.',
                          'Zähle systematisch, an welchen zwei Stellen das K stehen kann.'))

    # --- ohne_zuruecklegen ---
    neu('ohne_zuruecklegen', 2, bl('In einer Urne liegen 4 rote und 6 grüne Kugeln. Zwei werden ohne Zurücklegen gezogen. Wie groß ist P(zuerst rot, dann grün)?', Fr(4, 15),
                                   '4/10 · 6/9 = 24/90 = 4/15. Nach einer roten Kugel sind noch 9 Kugeln da, alle 6 grünen.', 'Beim zweiten Zug ist eine Kugel weniger in der Urne.'))
    neu('ohne_zuruecklegen', 2, bl('In einer Lostrommel sind 10 Lose, davon 3 Gewinne. Du ziehst 2 Lose. Wie groß ist P(genau ein Gewinn)?', Fr(7, 15),
                                   'Gewinn, Niete: 3/10 · 7/9 = 21/90. Niete, Gewinn: 7/10 · 3/9 = 21/90. Zusammen 42/90 = 7/15.', 'Zwei Pfade: G N und N G.'))
    neu('ohne_zuruecklegen', 3, bl('In einer Urne liegen 5 rote und 3 blaue Kugeln. Zwei werden ohne Zurücklegen gezogen. Wie groß ist die Wahrscheinlichkeit, dass die zweite Kugel rot ist?', Fr(5, 8),
                                   'Rot, rot: 5/8 · 4/7 = 20/56. Blau, rot: 3/8 · 5/7 = 15/56. Zusammen 35/56 = 5/8 – genauso groß wie beim ersten Zug.',
                                   'Die erste Kugel ist unbekannt: Rechne beide Pfade, die mit „rot“ enden.'))
    neu('ohne_zuruecklegen', 3, bl('In einer Urne liegen 2 blaue und 6 weiße Kugeln. Man zieht ohne Zurücklegen, bis eine blaue Kugel kommt. Wie groß ist die Wahrscheinlichkeit, dass man genau nach dem 2. Zug aufhört?', Fr(3, 14),
                                   'Erst weiß, dann blau: 6/8 · 2/7 = 12/56 = 3/14.', 'Aufhören nach dem 2. Zug heißt: Der erste war nicht blau, der zweite schon.'))
    neu('ohne_zuruecklegen', 3, zahl('In einer Urne liegen 4 blaue und 11 weiße Kugeln. Man zieht ohne Zurücklegen. Bei welchem Zug hat man spätestens sicher eine blaue Kugel gezogen?',
                                     'Im ungünstigsten Fall kommen zuerst alle 11 weißen. Der 12. Zug ist dann sicher blau.', 'Denk an den ungünstigsten Fall.', 12, '11 + 1'))
    neu('ohne_zuruecklegen', 3, zahl('In einer Urne liegen n Kugeln, genau 2 davon sind rot. Zieht man 2 Kugeln ohne Zurücklegen, sind beide mit der Wahrscheinlichkeit 1/15 rot. Wie groß ist n?',
                                     '2/n · 1/(n − 1) = 1/15 ⇒ n · (n − 1) = 30 ⇒ n = 6 (6 · 5 = 30).', 'Stelle die Pfadwahrscheinlichkeit mit n auf und probiere.', 6, '6 + (6 * 5 - 30)'))

    # --- gegenereignis ---
    neu('gegenereignis', 2, bl('Ein Würfel wird dreimal geworfen. Wie groß ist P(mindestens eine gerade Zahl)?', Fr(7, 8),
                               'Gegenereignis „nur ungerade“: (1/2)³ = 1/8. Also 1 − 1/8 = 7/8.', 'Was ist das Gegenteil von „mindestens eine gerade Zahl“?'))
    neu('gegenereignis', 2, bl('Zwei Würfel werden geworfen. Wie groß ist die Wahrscheinlichkeit, dass die Augenzahlen verschieden sind?', Fr(5, 6),
                               'Gegenereignis „Pasch“: 6 von 36 = 1/6. Also 1 − 1/6 = 5/6.', 'Rechne zuerst die Wahrscheinlichkeit für zwei gleiche Augenzahlen.'))
    neu('gegenereignis', 3, auswahl('Ein Kind trifft die Torwand mit der Wahrscheinlichkeit 0,25 und schießt 10-mal. Welcher Term gibt P(mindestens ein Treffer) an?', '1 − 0,75¹⁰',
                                    ['0,75¹⁰', '1 − 0,25¹⁰', '10 · 0,25'],
                                    'Gegenereignis: kein Treffer, also 10-mal daneben: 0,75¹⁰. Davon das Gegenteil: 1 − 0,75¹⁰. (10 · 0,25 = 2,5 ist gar keine Wahrscheinlichkeit.)',
                                    'Wie lautet das Gegenereignis, und wie wahrscheinlich ist ein Fehlschuss?'))
    neu('gegenereignis', 3, zahl('Wie groß muss die Trefferwahrscheinlichkeit p mindestens sein, damit man bei 2 Versuchen mit mindestens 91 % Wahrscheinlichkeit wenigstens einmal trifft?',
                                 '1 − (1 − p)² ≥ 0,91 ⇔ (1 − p)² ≤ 0,09 ⇔ 1 − p ≤ 0,3 ⇔ p ≥ 0,7.', 'Rechne rückwärts über das Gegenereignis „zweimal daneben“.', 0.7, '1 - 0.3'))
    w = gerundet(1 - 0.96 ** 20, 3)
    neu('gegenereignis', 3, zahl('Jede Birne einer Lichterkette fällt im ersten Jahr mit 4 % Wahrscheinlichkeit aus (unabhängig). Die Kette hat 20 Birnen. Wie groß ist P(mindestens eine fällt aus)? Runde auf drei Nachkommastellen.',
                                 f'P(keine fällt aus) = 0,96²⁰ ≈ 0,442. Also 1 − 0,442 ≈ {dz(w)}.', 'Gegenereignis: Alle 20 Birnen halten.', w, f'round({K(1 - 0.96 ** 20)}, 3)', tol=0.001))
    neu('gegenereignis', 3, auswahl('Jemand rechnet: „Bei 3 Würfen ist P(mindestens eine Sechs) = 1 − (1/6)³.“ Was stimmt?', 'Falsch: richtig ist 1 − (5/6)³.',
                                    ['Richtig.', 'Falsch: richtig ist 3 · 1/6.', 'Falsch: richtig ist (5/6)³.'],
                                    'Das Gegenereignis ist „keine Sechs“, nicht „nur Sechsen“. P(keine Sechs) = (5/6)³, also 1 − (5/6)³ ≈ 0,42.',
                                    'Was genau ist das Gegenteil von „mindestens eine Sechs“?'))

    # --- baum_ergaenzen ---
    neu('baum_ergaenzen', 2, zahl('Im Baumdiagramm ist P(A) = 0,7 und die Pfadwahrscheinlichkeit „A, dann nicht B“ = 0,21. Welche Wahrscheinlichkeit steht am Ast von A nach B?',
                                  'Ast A → nicht B: 0,21 : 0,7 = 0,3. Die Äste nach A ergeben zusammen 1: A → B = 1 − 0,3 = 0,7.',
                                  'Erst den Ast zu „nicht B“ durch Teilen finden, dann die Ergänzung zu 1.', 0.7, '1 - 0.21 / 0.7'))
    neu('baum_ergaenzen', 2, zahl('In einer Klasse sind 40 % Mädchen. Von den Mädchen tragen 25 % eine Brille. Welcher Anteil der ganzen Klasse sind Mädchen mit Brille?',
                                  'Pfad „Mädchen, Brille“: 0,4 · 0,25 = 0,1, also 10 % der Klasse – das gehört in die Vierfeldertafel in das Feld „Mädchen und Brille“.',
                                  'Ein Pfad im Baumdiagramm – multiplizieren.', 0.1, '0.4 * 0.25'))
    baum = {'typ': 'baum', 'aeste': [{'text': 'A', 'p': '0,6', 'aeste': [{'text': 'B', 'p': '0,5'}, {'text': 'nicht B', 'p': '0,5'}]},
                                     {'text': 'nicht A', 'p': '0,4', 'aeste': [{'text': 'B', 'p': '?'}, {'text': 'nicht B', 'p': '?'}]}]}
    neu('baum_ergaenzen', 3, mit_grafik(zahl('Im Baumdiagramm fehlen zwei Äste. Bekannt ist: Insgesamt tritt B mit der Wahrscheinlichkeit 0,46 ein. Welche Wahrscheinlichkeit steht am Ast von „nicht A“ nach B?',
                                             'P(B) = 0,6 · 0,5 + 0,4 · x = 0,46 ⇒ 0,3 + 0,4x = 0,46 ⇒ x = 0,16 : 0,4 = 0,4.',
                                             'B wird über zwei Pfade erreicht. Stelle eine Gleichung für P(B) auf.', 0.4, '(0.46 - 0.6 * 0.5) / 0.4'), baum))
    neu('baum_ergaenzen', 3, zahl('Aus einer Urne mit roten und blauen Kugeln werden zwei ohne Zurücklegen gezogen. Im Baumdiagramm steht am ersten Ast „rot“ 2/5 und am Ast „rot → rot“ 1/4. Wie viele Kugeln sind in der Urne?',
                                  'Mit 5 Kugeln, davon 2 rot: erster Zug 2/5, nach einer roten noch 1 rote von 4: 1/4 ✓. (Mit 10 Kugeln, 4 rot, wäre es 3/9 = 1/3.)',
                                  'Probiere die kleinste Urne mit dem Anteil 2/5 und prüfe den zweiten Ast.', 5, '5'))
    neu('baum_ergaenzen', 3, zahl('Ein Experiment hat zwei gleiche, unabhängige Stufen mit den Ergebnissen A und nicht A. Es gilt P(A, A) = 0,49. Wie groß ist P(A, nicht A)?',
                                  'P(A)² = 0,49 ⇒ P(A) = 0,7, P(nicht A) = 0,3. Also P(A, nicht A) = 0,7 · 0,3 = 0,21.', 'Welche Zahl mal sich selbst ergibt 0,49?', 0.21, '0.7 * 0.3'))
    neu('baum_ergaenzen', 3, zahl('25 % der Kinder einer Schule tragen eine Brille. Von den Brillenträgern sind 60 % Mädchen, von den anderen Kindern 40 %. Welcher Anteil aller Kinder sind Mädchen?',
                                  'Zwei Pfade zu „Mädchen“: 0,25 · 0,6 + 0,75 · 0,4 = 0,15 + 0,3 = 0,45.', 'Zeichne den Baum: erste Stufe Brille ja/nein, zweite Stufe Mädchen/Junge.',
                                  0.45, '0.25 * 0.6 + 0.75 * 0.4'))

    # --- simulation ---
    neu('simulation', 2, auswahl('Ein Computer erzeugt zufällige ganze Zahlen von 1 bis 100. Damit soll ein Ereignis mit der Wahrscheinlichkeit 0,35 simuliert werden. Welche Zahlen zählen als „Treffer“?',
                                 'die Zahlen 1 bis 35', ['die Zahlen 1 bis 34', 'die Zahlen 0 bis 35', 'die Zahlen 35 bis 100'],
                                 '1 bis 35 sind genau 35 von 100 Zahlen, also Anteil 0,35. (35 bis 100 wären 66 Zahlen, 0 kommt nicht vor.)', 'Zähle, wie viele Zahlen jede Auswahl enthält.'))
    neu('simulation', 2, zahl('Zwei Würfel werden 360-mal geworfen. Wie oft erwartet man einen Pasch (zwei gleiche Augenzahlen)?', 'P(Pasch) = 6/36 = 1/6. Erwartet: 360 · 1/6 = 60.',
                              'Erst die Wahrscheinlichkeit für einen Pasch, dann n · p.', 60, '360 * 6 / 36'))
    neu('simulation', 3, zahl('In ein Quadrat mit der Seitenlänge 2 ist ein Kreis mit Radius 1 gezeichnet. 1 000 zufällige Punkte im Quadrat: 785 liegen im Kreis. Welchen Näherungswert für π liefert das?',
                              'Anteil im Kreis ≈ Kreisfläche : Quadratfläche = π · 1² : 4. Also π/4 ≈ 0,785 ⇒ π ≈ 3,14.', 'Vergleiche den Anteil der Treffer mit dem Flächenverhältnis.', 3.14, '4 * 785 / 1000'))
    w, c = gerundet(2000 * math.pi / 4, 0), f'round({K(2000 * math.pi / 4)}, 0)'
    neu('simulation', 3, zahl('Im Quadrat mit der Seitenlänge 2 liegt ein Kreis mit Radius 1. Wie viele von 2 000 zufälligen Punkten im Quadrat erwartet man im Kreis? Runde auf eine ganze Zahl.',
                              f'p = Kreisfläche : Quadratfläche = π : 4 ≈ 0,785. Erwartet: 2 000 · π/4 ≈ {dz(w)}.', 'Die Trefferwahrscheinlichkeit ist ein Flächenverhältnis.', w, c, tol=1))
    neu('simulation', 3, zahl('Nach 200 Würfen beträgt die relative Häufigkeit der Sechs 0,15. Wie viele Sechsen müssen bei den nächsten 100 Würfen fallen, damit die relative Häufigkeit nach 300 Würfen genau 1/6 ist?',
                              'Bisher 0,15 · 200 = 30 Sechsen. Nach 300 Würfen sollen es 300 : 6 = 50 sein. Also 50 − 30 = 20.', 'Rechne mit absoluten Häufigkeiten: wie viele bisher, wie viele am Ende?', 20, '300 / 6 - 0.15 * 200'))
    neu('simulation', 3, auswahl('Bei 10 Würfen kam 4-mal die Sechs (relative Häufigkeit 0,4). Jemand folgert: „Der Würfel ist gezinkt.“ Was stimmt?',
                                 'Nicht zwingend: Bei nur 10 Würfen schwankt die relative Häufigkeit stark um 1/6.',
                                 ['Richtig, denn 0,4 ist mehr als doppelt so groß wie 1/6.', 'Richtig, bei einem fairen Würfel wäre die Sechs genau 1- bis 2-mal gefallen.', 'Falsch, denn der Würfel ist sicher fair.'],
                                 'Erst bei sehr vielen Würfen nähert sich die relative Häufigkeit der Wahrscheinlichkeit (empirisches Gesetz der großen Zahlen). 4 Sechsen in 10 Würfen kommen auch bei fairen Würfeln vor.',
                                 'Wie stark schwankt eine relative Häufigkeit bei wenigen Versuchen?'))

    # --- verstehen ---
    neu('verstehen', 2, auswahl('Welche Aussage über ein Baumdiagramm ist falsch?', 'Ein Pfad kann wahrscheinlicher sein als sein erster Ast.',
                                ['Die Summe aller Pfadwahrscheinlichkeiten ist 1.', 'An jeder Verzweigung ergeben die Äste zusammen 1.', 'Jede Pfadwahrscheinlichkeit liegt zwischen 0 und 1.'],
                                'Entlang eines Pfades wird mit Zahlen ≤ 1 multipliziert – das Produkt wird nie größer als der erste Ast.', 'Was passiert, wenn man mit einer Zahl ≤ 1 multipliziert?'))
    neu('verstehen', 2, auswahl('Wann unterscheiden sich „mit Zurücklegen“ und „ohne Zurücklegen“ beim Ziehen von zwei Kugeln kaum?', 'wenn sehr viele Kugeln in der Urne liegen',
                                ['wenn nur wenige Kugeln in der Urne liegen', 'wenn genau zwei Farben vorkommen', 'nie, der Unterschied ist immer groß'],
                                'Bei 1 000 Kugeln ändert eine gezogene Kugel die Anteile kaum (z. B. 500/1 000 und 499/999).', 'Rechne ein Beispiel mit 10 und mit 1 000 Kugeln.'))
    neu('verstehen', 3, auswahl('Urne mit 3 roten und 2 blauen Kugeln, zwei Züge ohne Zurücklegen. Welches Ereignis hat die Wahrscheinlichkeit 3/5 · 2/4 + 2/5 · 3/4?',
                                'Die beiden Kugeln haben verschiedene Farben.', ['Zuerst rot, dann blau.', 'Mindestens eine Kugel ist rot.', 'Beide Kugeln haben dieselbe Farbe.'],
                                'Zwei Pfade werden addiert: rot → blau (3/5 · 2/4) und blau → rot (2/5 · 3/4). Das sind genau die Pfade mit zwei verschiedenen Farben.',
                                'Welche zwei Pfade stehen in der Summe?'))
    neu('verstehen', 3, auswahl('Ein Würfel wird n-mal geworfen. Welcher Term gibt die Wahrscheinlichkeit an, dass jedes Mal eine gerade Zahl fällt?', '(1/2)ⁿ',
                                ['n · 1/2', '1 − (1/2)ⁿ', '(1/6)ⁿ'],
                                'Pro Wurf ist P(gerade) = 3/6 = 1/2. n Würfe nacheinander: n-mal den Faktor 1/2. 1 − (1/2)ⁿ wäre „mindestens einmal ungerade“.',
                                'Wie groß ist P(gerade) bei einem Wurf? Wie viele Stufen hat der Pfad?'))
    a, b = 1 - (5 / 6) ** 4, 1 - (35 / 36) ** 24
    neu('verstehen', 3, auswahl('Was ist wahrscheinlicher: mit 4 Würfen eines Würfels mindestens eine Sechs – oder mit 24 Würfen von zwei Würfeln mindestens einmal zwei Sechsen?',
                                'mindestens eine Sechs bei 4 Würfen', ['mindestens ein Sechserpasch bei 24 Doppelwürfen', 'beide gleich wahrscheinlich, denn 4 : 6 = 24 : 36', 'Das lässt sich nicht berechnen.'],
                                f'1 − (5/6)⁴ ≈ {dz(round(a, 3))} und 1 − (35/36)²⁴ ≈ {dz(round(b, 3))}. Die erste Wahrscheinlichkeit ist größer, obwohl das Verhältnis 4 : 6 = 24 : 36 gleich ist.',
                                'Rechne beide über das Gegenereignis.'))
    neu('verstehen', 3, auswahl('Jemand sagt: „Beim Lotto 6 aus 49 ist die Zahlenreihe 1, 2, 3, 4, 5, 6 unwahrscheinlicher als eine gemischte Reihe wie 3, 17, 22, 30, 41, 48.“ Was stimmt?',
                                'Falsch: Jede bestimmte Sechserkombination ist gleich wahrscheinlich.', ['Richtig, Zahlen hintereinander kommen seltener.', 'Richtig, weil kleine Zahlen seltener gezogen werden.', 'Falsch: 1, 2, 3, 4, 5, 6 ist wahrscheinlicher.'],
                                'Jede bestimmte Kombination ist ein einziger Pfad mit derselben Wahrscheinlichkeit (6/49 · 5/48 · … · 1/44). „Gemischt“ wirkt nur häufiger, weil es sehr viele gemischte Reihen gibt.',
                                'Berechne die Wahrscheinlichkeit für eine ganz bestimmte Reihe. Hängt sie von den Zahlen ab?'))
    return N


if __name__ == '__main__':
    datei = bauen('stochastik.mehrstufig',
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
    ergaenzen(datei, schwer())
