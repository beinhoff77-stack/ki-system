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


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('stochastik.mehrstufig', 13_10_7)
_bt = 'In einem zweistufigen Baumdiagramm ist P(A) = {} und die Wahrscheinlichkeit des Pfades „A, dann B“ = {}. Welche Wahrscheinlichkeit steht am Ast von A nach B?'
# c) alle drei Stufe-2-Übungen hatten die Lösung 0,9 (ratbar) → zwei davon mit anderen Zahlen
BF.ersetze('baum_ergaenzen', 'In einem zweistufigen Baumdiagramm ist P(A) = 0,5 und die Wahrscheinlichkeit des Pfades „A, dann B“ = 0,45. Welche Wahrscheinlichkeit steht am Ast von A nach B?', BF.Z(_bt.format('0,5', '0,3'), 0.6, '0.3 / 0.5', 'P(A) · x = 0,3 ⇒ x = 0,3 : 0,5 = 0,6.', 'Pfadwahrscheinlichkeit = Produkt der Äste; teile.', grafik={'typ': 'baum', 'aeste': [{'text': 'A', 'p': '0,5', 'aeste': [{'text': 'B', 'p': '?'}, {'text': 'nicht B'}]}, {'text': 'nicht A', 'p': '0,5'}]}))
BF.ersetze('baum_ergaenzen', 'In einem zweistufigen Baumdiagramm ist P(A) = 0,2 und die Wahrscheinlichkeit des Pfades „A, dann B“ = 0,18. Welche Wahrscheinlichkeit steht am Ast von A nach B?', BF.Z(_bt.format('0,2', '0,1'), 0.5, '0.1 / 0.2', 'P(A) · x = 0,1 ⇒ x = 0,1 : 0,2 = 0,5.', 'Pfadwahrscheinlichkeit = Produkt der Äste; teile.', grafik={'typ': 'baum', 'aeste': [{'text': 'A', 'p': '0,2', 'aeste': [{'text': 'B', 'p': '?'}, {'text': 'nicht B'}]}, {'text': 'nicht A', 'p': '0,8'}]}))
# c) inhaltlich dieselbe Aufgabe wie „mindestens eine Sechs“ (gleiche Lösung 11/36)
BF.ersetze('gegenereignis', 'Ein Würfel wird 2-mal geworfen. Wie groß ist P(mindestens eine Eins)?', BF.L(
    'Eine Münze wird 3-mal geworfen. Wie groß ist P(mindestens einmal Zahl)?', '□/□', [7, 8], ['7', '8'],
    'P(keinmal Zahl) = (1/2)³ = 1/8; 1 − 1/8 = 7/8.', 'Rechne über das Gegenereignis „keinmal“.', hinweis='Zähler und Nenner (gekürzt)'))
# a) sechsmal dasselbe Schema auf Stufe 3 → drei davon Stufe 2
_gl = 'Ein Glücksrad zeigt mit der Wahrscheinlichkeit {} „Gewinn“. Es wird dreimal gedreht. Wie groß ist P(genau zweimal Gewinn)?'
for _p in ('0,7', '0,6', '0,2'):
    BF.stufe('pfad_add', _gl.format(_p), 2)
# c) Ablenker „Falsch: richtig ist 1 − 1/6 · n“ unklar formuliert → „1 − n/6“; die Stufe-3-Aufgabe (4 Würfe) ist derselbe Typ wie Stufe 2 → Stufe 2
BF.ersetze('verstehen', 'Jemand sagt: „Bei 5 Würfen ist P(mindestens eine Sechs) = 5 · 1/6 = 5/6.“ Was stimmt?', BF.A('Jemand behauptet: „Bei 5 Würfen ist P(mindestens eine Sechs) = 5 · 1/6 = 5/6.“ Was stimmt?', 'Falsch: richtig ist 1 − (5/6)⁵ ≈ 0,598.', ['Richtig.', 'Falsch: richtig ist 1 − 5/6.', 'Falsch: richtig ist (1/6)⁵.'], 'Pfade mit zwei oder mehr Sechsen würden mehrfach gezählt; deshalb über das Gegenereignis rechnen.', 'Was wäre bei 6 Würfen? Kann P = 1 sein?'), s=2)
BF.ersetze('verstehen', 'Jemand sagt: „Bei 2 Würfen ist P(mindestens eine Sechs) = 2 · 1/6 = 1/3.“ Was stimmt?', BF.A('Jemand behauptet: „Bei 2 Würfen ist P(mindestens eine Sechs) = 2 · 1/6 = 1/3.“ Was stimmt?', 'Falsch: richtig ist 1 − (5/6)² ≈ 0,306.', ['Falsch: richtig ist (1/6)².', 'Richtig.', 'Falsch: richtig ist 1 − 2/6.'], 'Pfade mit zwei oder mehr Sechsen würden mehrfach gezählt; deshalb über das Gegenereignis rechnen.', 'Was wäre bei 6 Würfen? Kann P = 1 sein?'), s=2)
BF.ersetze('verstehen', 'Jemand sagt: „Bei 4 Würfen ist P(mindestens eine Sechs) = 4 · 1/6 = 2/3.“ Was stimmt?', BF.A('Jemand behauptet: „Bei 4 Würfen ist P(mindestens eine Sechs) = 4 · 1/6 = 2/3.“ Was stimmt?', 'Falsch: richtig ist 1 − (5/6)⁴ ≈ 0,518.', ['Richtig.', 'Falsch: richtig ist 1 − 4/6.', 'Falsch: richtig ist (1/6)⁴.'], 'Pfade mit zwei oder mehr Sechsen würden mehrfach gezählt; deshalb über das Gegenereignis rechnen.', 'Was wäre bei 6 Würfen? Kann P = 1 sein?'), s=2)
BF.nicht_umgesetzt('simulation S2 „Simulation 500-mal … relative Häufigkeit“ (reines Ablesen)', 'Lösungen richtig; die eigentliche Simulation (Zufallszahlen zuordnen) wurde in Runde 10 ergänzt.')

# ---- BEFUNDE ENDE ----

# ---------- Achtzehnte Runde (Zweig luecken-kl10): π schätzen – Monte-Carlo-Methode und Streifenmethode ----------
# Lücke laut Aufbau-Prüfung (inhalte/pruefung/aufbau/klasse10.json): LehrplanPLUS M10 2 verlangt, π zufallsbasiert zu nähern (Monte-Carlo)
# und das Verfahren mit einer nicht zufallsbasierten Methode zu vergleichen, z. B. der Streifenmethode. stochastik.simulation (seit D2
# Klasse 10) schätzt mit Zufallspunkten Flächen; π und der Vergleich fehlten. Neue Lernkarte „pi_schaetzen“ nach „simulation“.
# Läuft ganz am Ende mit eigenem Zufallsstart; alle alten Aufgaben bleiben gleich.
# Prüfungsvorbilder (Typ und Niveau, eigene Zahlen): Grundwissen M10 bayerischer Gymnasien (M10.5 „Näherungsweise Bestimmung von π“:
# Monte-Carlo-Methode beschreiben, weitere Methode angeben), Schulaufgaben-Typ „π mit Rechteckstreifen von oben und unten eingrenzen“.
import random as _random

_H = lambda x: math.sqrt(max(0.0, 1 - x * x))  # noqa: E731  Höhe des Viertelkreises (r = 1)


def _ober(n): return 4 / n * sum(_H(i / n) for i in range(n))
def _unter(n): return 4 / n * sum(_H(i / n) for i in range(1, n + 1))


def _bogen(k=24):
    return [[round(math.cos(math.pi / 2 * i / k), 4), round(math.sin(math.pi / 2 * i / k), 4)] for i in range(k + 1)]


def _streifen(n, oben=True):
    fl = []
    for i in range(n):
        x0, x1 = i / n, (i + 1) / n
        h = _H(x0) if oben else _H(x1)
        if h > 0: fl.append({'punkte': [[round(x0, 4), 0], [round(x1, 4), 0], [round(x1, 4), round(h, 4)], [round(x0, 4), round(h, 4)]]})
    return fl


_VIERTEL = {'punkte': [[0, 0]] + _bogen()}
_R40 = _random.Random(1850)  # Startwert so gewählt, dass die 40 Punkte einen typischen Anteil zeigen (31 Treffer)
_TROPFEN = [(round(_R40.random(), 2), round(_R40.random(), 2)) for _ in range(40)]
_TREFFER = sum(1 for x, y in _TROPFEN if x * x + y * y <= 1)
_KS_PI = {'typ': 'koordinaten', 'x': [0, 1], 'y': [0, 1], 'schritt_x': 0.25, 'schritt_y': 0.25, 'flaechen': [_VIERTEL]}
KARTE_PI = {
    'lernziel': 'pi_schaetzen', 'titel': 'π schätzen: Zufall oder Streifen?',
    'einstieg': 'Regentropfen fallen zufällig auf eine quadratische Platte. Darauf ist ein Viertelkreis gemalt. '
                'Aus dem Anteil der Tropfen darin kann man π schätzen: die ⟦Monte-Carlo-Methode⟧.',
    'woerter': [['Monte-Carlo-Methode', 'mit vielen Zufallspunkten eine Fläche oder eine Zahl wie π schätzen'],
                ['Streifenmethode', 'eine Fläche in schmale Rechtecke zerlegen und deren Flächen addieren; ganz ohne Zufall']],
    'bild': _KS_PI,
    'schritte': [
        {'text': 'Seitenlänge 1: Das Quadrat hat die Fläche 1, der Viertelkreis π/4.'},
        {'text': f'{_TREFFER} von 40 Zufallspunkten liegen im Viertelkreis: Anteil {_TREFFER} : 40 = {dz(Fr(_TREFFER, 40))}.',
         'bild': {'punkte': [{'x': x, 'y': y} for x, y in _TROPFEN]}},
        {'text': f'Also π/4 ≈ {dz(Fr(_TREFFER, 40))} und ⟦π ≈ 4 · {dz(Fr(_TREFFER, 40))} = {dz(Fr(_TREFFER, 10))}⟧.'},
        {'text': f'Streifenmethode: Vier Rechtecke über dem Bogen ergeben π ≈ {dz(round(_ober(4), 2))}, sicher zu groß.',
         'bild': {'punkte': [], 'flaechen': [_VIERTEL] + _streifen(4, True)}},
        {'text': f'Rechtecke unter dem Bogen ergeben {dz(round(_unter(4), 2))}. π liegt also ⟦sicher dazwischen⟧.',
         'bild': {'flaechen': [_VIERTEL] + _streifen(4, False)}}],
    'fehler': f'π ≈ {dz(Fr(_TREFFER, 40))} ist falsch. Der Anteil der Punkte ist nur π/4, also ein Viertel von π. Erst ⟦mal 4⟧ ergibt π ≈ {dz(Fr(_TREFFER, 10))}.',
    'regel': 'π ≈ 4 · Anteil der Treffer im Viertelkreis. ⟦Streifen geben sichere Grenzen⟧, der Zufall nur eine Schätzung.'}


def luecken_kl10():
    start(18030)
    V = []

    def neu(p, s, a):
        assert a is not None, 'zu wenige verschiedene Antworten'
        a['p'], a['s'] = p, s
        V.append(a)

    def mc(text, n, k, kontext, h='Der Anteil der Treffer schätzt π/4. Was musst du noch tun?'):
        q = Fr(4 * k, n)
        if endlich(q):
            return zahl(text, f'Anteil {dz(k)} : {dz(n)} = {dz(Fr(k, n)) if endlich(Fr(k, n)) else "…"} ≈ π/4{kontext}. π ≈ 4 · {dz(k)} : {dz(n)} = {dz(q)}.',
                        h, q, f'4 * {k} / {n}')
        w = gerundet(4 * k / n, 2)
        return zahl(text + ' Runde auf zwei Nachkommastellen.', f'Anteil {dz(k)} : {dz(n)} ≈ π/4{kontext}. π ≈ 4 · {dz(k)} : {dz(n)} ≈ {dz(w)}.', h, w,
                    f'round(4 * {k} / {n}, 2)', tol=0.01)

    def punkt(x, y):
        X, Y = Fr(str(x)), Fr(str(y))
        s = X ** 2 + Y ** 2
        drin = s <= 1
        richtig = f'{"Ja" if drin else "Nein"}, denn {dz(x)}² + {dz(y)}² = {dz(s)} {"≤" if drin else ">"} 1.'
        if drin:
            falsch = [f'Nein, denn {dz(x)} + {dz(y)} = {dz(X + Y)} > 1.', f'Nein, denn {dz(max(x, y))} liegt näher an 1 als an 0.']
        else:
            falsch = ['Ja, denn beide Koordinaten sind kleiner als 1.', f'Ja, denn {dz(x)} · {dz(y)} = {dz(X * Y)} ≤ 1.']
        return auswahl(f'Ein Zufallspunkt im Einheitsquadrat hat die Koordinaten ({dz(x)} | {dz(y)}). Liegt er im Viertelkreis mit Radius 1 um (0 | 0)?', richtig, falsch,
                       f'Abstand zum Ursprung nach Pythagoras: {dz(x)}² + {dz(y)}² = {dz(s)}. Im Viertelkreis liegt der Punkt, wenn das höchstens 1 ist: {"ja" if drin else "nein"}.',
                       'Der Abstand zu (0 | 0) folgt aus dem Satz des Pythagoras. Vergleiche x² + y² mit 1.')

    def streifen(n, oben, s):
        wahr = _ober(n) if oben else _unter(n)
        w = gerundet(wahr, 2)
        assert w is not None
        xs = [Fr(i, n) for i in (range(n) if oben else range(1, n + 1))]
        hs = ', '.join(f'√(1 − {dz(x)}²)' if x not in (0, 1) else ('1' if x == 0 else '0') for x in xs)
        return zahl(f'Der Viertelkreis (Radius 1) wird in {n} gleich breite Streifen geteilt. Auf jeden Streifen kommt ein Rechteck, das {"bis über den Bogen reicht (Höhe am linken Rand)" if oben else "ganz unter dem Bogen bleibt (Höhe am rechten Rand)"}. '
                    f'Welchen Näherungswert für π liefert 4 · (Summe der Rechteckflächen)? Runde auf zwei Nachkommastellen.',
                    f'Breite je Streifen {dz(Fr(1, n))}; Höhen {hs}. Summe der Flächen ≈ {dz(round(wahr / 4, 4))}; mal 4 ≈ {dz(w)} ({"zu groß" if oben else "zu klein"}).',
                    'Die Höhe an der Stelle x ist √(1 − x²) (Pythagoras). Fläche = Breite · Höhe.', w, f'round({K(wahr)}, 2)', tol=0.01)

    # ---- Stufe 1 ----
    neu('uebung', 1, mc('Auf eine quadratische Platte mit einem Viertelkreis fallen 200 Regentropfen, 156 davon im Viertelkreis. Welchen Näherungswert für π liefert das?', 200, 156, ''))
    neu('uebung', 1, punkt(0.6, 0.7))
    neu('uebung', 1, zahl('Welcher Anteil des Einheitsquadrats wird vom Viertelkreis mit Radius 1 bedeckt? Runde auf drei Nachkommastellen.',
                          f'Viertelkreis: π · 1² : 4 = π/4 ≈ {dz(gerundet(math.pi / 4, 3))}; Quadrat: 1. Anteil ≈ {dz(gerundet(math.pi / 4, 3))}.',
                          'Fläche des Viertelkreises: ein Viertel von π · r².', gerundet(math.pi / 4, 3), f'round({K(math.pi)} / 4, 3)', tol=0.001))
    neu('uebung', 1, zahl('Wie viele von 400 Zufallspunkten im Einheitsquadrat erwartest du ungefähr im Viertelkreis (Radius 1)? Runde auf ganze Punkte.',
                          f'Anteil π/4 ≈ 0,785; 400 · π/4 = 100π ≈ {dz(gerundet(100 * math.pi, 0))}.', 'Erwartete Anzahl = Anzahl der Punkte · Anteil π/4.',
                          gerundet(100 * math.pi, 0), f'round(400 * {K(math.pi)} / 4)', tol=1))
    # ---- Stufe 2 ----
    neu('uebung', 2, mc('In einer Tabellenkalkulation wurden 500 Zufallspunkte (x | y) erzeugt. Eine Spalte enthält WENN(x² + y² ≤ 1; 1; 0), ihre Summe ist 397. Welchen Näherungswert für π liefert das?',
                        500, 397, ' (die Summe zählt die Punkte im Viertelkreis)'))
    neu('uebung', 2, streifen(2, True, 2))
    neu('uebung', 2, streifen(2, False, 2))
    neu('uebung', 2, auswahl('Warum ergibt die Monte-Carlo-Methode bei jedem neuen Durchgang einen etwas anderen Näherungswert für π?',
                             'Weil die Punkte zufällig fallen und der Anteil im Viertelkreis deshalb schwankt.',
                             ['Weil sich der Wert von π ändert.', 'Weil das Quadrat jedes Mal anders groß ist.', 'Weil die Formel π ≈ 4 · Anteil nur manchmal gilt.'],
                             'π ist fest, die Formel auch. Zufällig ist nur, wie viele Punkte gerade im Viertelkreis landen. Deshalb schwankt der Schätzwert um π.',
                             'Was ist bei jedem Durchgang anders?'))
    neu('uebung', 2, zahl('Eine Monte-Carlo-Simulation mit 800 Zufallspunkten ergab den Näherungswert π ≈ 3,15. Wie viele Punkte lagen im Viertelkreis?',
                          '4 · k : 800 = 3,15 ⇒ k = 3,15 · 800 : 4 = 630.', 'Stelle π ≈ 4 · k : n nach k um.', 630, '3.15 * 800 / 4'))
    neu('uebung', 2, mc('Ein Kreis mit Radius 1 liegt genau in einem Quadrat mit der Seitenlänge 2. Von 300 Zufallspunkten im Quadrat liegen 236 im Kreis. Welchen Näherungswert für π liefert das?',
                        300, 236, ' – hier: Kreisfläche π geteilt durch Quadratfläche 4', 'Kreisfläche π · 1² und Quadratfläche 2² = 4: Der Anteil schätzt π/4.'))
    # ---- Stufe 3 ----
    neu('uebung', 3, streifen(4, True, 3))   # Prüfungsvorbild: π von oben eingrenzen
    neu('uebung', 3, streifen(4, False, 3))  # Prüfungsvorbild: π von unten eingrenzen
    neu('uebung', 3, zahl('Bei der Streifenmethode mit n Streifen wird π von oben (Rechtecke über dem Bogen) und von unten (Rechtecke unter dem Bogen) eingegrenzt. '
                          'Wie viele Streifen braucht man mindestens, damit beide Näherungswerte (jeweils mal 4) höchstens 0,1 auseinanderliegen?',
                          'Die oberen Rechtecke sind die unteren, eins nach links gerückt; dazu kommt nur das erste mit Höhe 1. Unterschied: 4 · (1/n) · 1 = 4/n. '
                          '4/n ≤ 0,1 ⇒ n ≥ 40.',
                          'Vergleiche die beiden Rechteck-Reihen: Welche Rechtecke kommen in beiden vor?', 40, '4 / 0.1', einheit='Streifen'))
    neu('uebung', 3, auswahl('Welche Aussage über die beiden Verfahren zur Näherung von π stimmt?',
                             'Die Streifenmethode liefert sichere Grenzen für π, die Monte-Carlo-Methode nur einen Schätzwert, der schwanken kann.',
                             ['Die Monte-Carlo-Methode liefert mit 100 Punkten immer genau π.', 'Die Streifenmethode liefert bei jeder Wiederholung einen anderen Wert.',
                              'Beide Verfahren liefern nur Werte, die größer als π sind.'],
                             'Rechtecke über dem Bogen sind sicher zu groß, unter dem Bogen sicher zu klein: π liegt dazwischen, jedes Mal gleich. Zufallspunkte geben nur einen Schätzwert, der um π schwankt.',
                             'Was ist bei der Streifenmethode zufällig – und was bei der Monte-Carlo-Methode?'))
    neu('uebung', 3, auswahl('Jemand zählt 156 von 200 Zufallspunkten im Viertelkreis und schreibt: „π ≈ 156 : 200 = 0,78.“ Was stimmt?',
                             'Falsch: 0,78 schätzt nur π/4; π ≈ 4 · 0,78 = 3,12.',
                             ['Richtig.', 'Falsch: π ≈ 200 : 156 ≈ 1,28.', 'Falsch: π ≈ 2 · 0,78 = 1,56.'],
                             'Der Anteil der Punkte schätzt den Anteil der Fläche: Viertelkreis : Quadrat = π/4 : 1. Also π ≈ 4 · 0,78 = 3,12.',
                             'Welchen Flächenanteil schätzt der Anteil der Punkte?'))
    pts = [(0.2, 0.9), (0.7, 0.8), (0.5, 0.5), (0.9, 0.3), (0.6, 0.85)]
    k = sum(1 for x, y in pts if Fr(str(x)) ** 2 + Fr(str(y)) ** 2 <= 1)
    neu('uebung', 3, zahl('Eine Simulation erzeugt die fünf Zufallspunkte ' + ', '.join(f'({dz(x)} | {dz(y)})' for x, y in pts) + '. Welchen Näherungswert für π liefern diese fünf Punkte?',
                          'x² + y²: ' + ', '.join(f'{dz(Fr(str(x)) ** 2 + Fr(str(y)) ** 2)}' for x, y in pts) + f'. Höchstens 1 sind {k} Werte. π ≈ 4 · {k} : 5 = {dz(Fr(4 * k, 5))} – mit 5 Punkten sehr ungenau.',
                          'Prüfe für jeden Punkt x² + y² ≤ 1. Dann π ≈ 4 · Treffer : Anzahl.', Fr(4 * k, 5), f'4 * {k} / 5'))
    neu('uebung', 3, auswahl('Ein Programm schätzt π mit genau 100 Zufallspunkten (π ≈ 4 · Treffer : 100). Welcher Schätzwert kann dabei gar nicht herauskommen?', '3,14',
                             ['3,12', '3,16', '3,20'],
                             '4 · k : 100 = k : 25. Möglich sind nur Vielfache von 0,04: 3,12 (k = 78), 3,16 (k = 79), 3,20 (k = 80). Für 3,14 wäre k = 78,5 – keine ganze Zahl.',
                             'Treffer k sind ganze Zahlen. In welchen Schritten kann 4 · k : 100 nur wachsen?'))
    neu('uebung', 3, zahl('Bei 1 000 Zufallspunkten soll der Schätzwert für π größer als 3,2 sein. Wie viele Punkte müssen dafür mindestens im Viertelkreis liegen?',
                          '4 · k : 1 000 > 3,2 ⇒ k > 800. Die kleinste ganze Zahl darüber ist 801.', 'Stelle 4 · k : 1 000 > 3,2 nach k um. k ist ganzzahlig.', 801, '800 + 1'))
    # ---- Test, Korrektur, Sicherung ----
    neu('test', 2, mc('Von 250 Zufallspunkten im Einheitsquadrat liegen 197 im Viertelkreis mit Radius 1. Welchen Näherungswert für π liefert das?', 250, 197, ''))
    neu('korrektur', 2, punkt(0.8, 0.7))
    neu('korrektur', 2, mc('Von 600 Zufallspunkten im Einheitsquadrat liegen 470 im Viertelkreis mit Radius 1. Welchen Näherungswert für π liefert das?', 600, 470, ''))
    neu('korrektur', 2, zahl('Wie viele von 2 000 Zufallspunkten im Einheitsquadrat erwartest du ungefähr im Viertelkreis (Radius 1)? Runde auf ganze Punkte.',
                             f'2 000 · π/4 = 500π ≈ {dz(gerundet(500 * math.pi, 0))}.', 'x', gerundet(500 * math.pi, 0), f'round(2000 * {K(math.pi)} / 4)', tol=1))
    neu('sicherung', 2, mc('Beim Reiswerfen landen 500 Körner auf einem quadratischen Brett mit Viertelkreis, 392 davon im Viertelkreis. Welchen Näherungswert für π liefert das?', 500, 392, ''))
    neu('sicherung', 2, punkt(0.5, 0.8))
    neu('sicherung', 2, zahl('Eine Monte-Carlo-Simulation mit 1 000 Zufallspunkten ergab π ≈ 3,16. Wie viele Punkte lagen im Viertelkreis?',
                             '4 · k : 1 000 = 3,16 ⇒ k = 3,16 · 1 000 : 4 = 790.', 'x', 790, '3.16 * 1000 / 4'))
    neu('sicherung', 2, mc('In einer Tabellenkalkulation ergibt die Spalte WENN(x² + y² ≤ 1; 1; 0) bei 800 Zufallspunkten die Summe 631. Welchen Näherungswert für π liefert das?',
                           800, 631, ' (die Summe zählt die Punkte im Viertelkreis)'))
    neu('sicherung', 2, auswahl('Welches Verfahren liefert bei jeder Wiederholung genau denselben Näherungswert für π?', 'die Streifenmethode',
                                ['die Monte-Carlo-Methode', 'beide Verfahren', 'keines der beiden Verfahren'],
                                'Die Streifenmethode rechnet immer mit denselben Rechtecken, ohne Zufall. Bei der Monte-Carlo-Methode fallen die Punkte jedes Mal anders.', 'x'))
    neu('sicherung', 2, streifen(5, True, 2))
    return V


def luecken_einbauen():
    from _luecken_kl10 import karte_einfuegen, offen_ergaenzen
    karte_einfuegen('stochastik.mehrstufig', KARTE_PI, 'simulation', luecken_kl10())
    offen_ergaenzen('stochastik.mehrstufig', 'Achtzehnte Runde (luecken-kl10): neue Lernkarte „pi_schaetzen“ nach „simulation“ (LehrplanPLUS M10 2: π mit der '
                    'Monte-Carlo-Methode nähern und mit der Streifenmethode vergleichen). Viertelkreis als gefüllte Fläche (Vieleck mit 24 Ecken), '
                    'Zufallspunkte und Streifen im Koordinatensystem. Selbst simulieren kann das Kind weiter nicht (App-Wunsch Simulationsknopf).')


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
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden
    luecken_einbauen()  # Achtzehnte Runde (luecken-kl10): neue Karte pi_schaetzen – ganz am Ende


# ---------- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl10) ----------
# Gesamtdurchsicht: jede Lernkarte und jede Aufgabe gelesen und nachgerechnet. Läuft ganz am Ende auf der fertigen Datei.
def durchsicht():
    from _durchsicht_kl10 import Durchsicht
    D = Durchsicht('stochastik.mehrstufig', 19030)
    # pfad_mult: dreistufiger Pfad in fester Reihenfolge = Stufe-2-Rechnung mit einer Stufe mehr
    D.stufe(range(12, 18), 2, 'In einer Urne liegen')
    # pfad_add: „genau zweimal Gewinn“ steht gleich auf Stufe 2 und 3
    D.stufe([43, 44, 45], 2, 'Ein Glücksrad zeigt mit der Wahrscheinlichkeit')
    # ohne_zuruecklegen: „drei Gewinne“ = Stufe-1-Pfad mit einer Stufe mehr
    D.stufe(range(69, 74), 2, 'In einer Lostrommel sind')
    # gegenereignis: sechsmal „Wie oft muss man mindestens spielen?“ – zwei davon durch andere Stufe-3-Gedanken ersetzt
    D.ersetze(98, 'Ein Spiel wird mit der Wahrscheinlichkeit 0,1 gewonnen. Wie oft muss man mindestens spielen, um mit einer Wahrscheinlichkeit von mindestens 95 %',
              D.L('Ein Würfel wird zweimal geworfen. Um wie viel ist P(mindestens eine Sechs) größer als P(genau eine Sechs)? Gib die Differenz als gekürzten Bruch an.',
                  '□/□', [1, 36], ['1', '36'],
                  'P(mindestens eine) = 1 − 25/36 = 11/36, P(genau eine) = 2 · 1/6 · 5/6 = 10/36. Der Unterschied ist der Pfad „zwei Sechsen“: 1/36.',
                  'Welche Pfade gehören zu „mindestens eine“, aber nicht zu „genau eine“?', hinweis='Zähler und Nenner (gekürzt)'))
    D.ersetze(100, 'Ein Spiel wird mit der Wahrscheinlichkeit 0,2 gewonnen. Wie oft muss man mindestens spielen, um mit einer Wahrscheinlichkeit von mindestens 95 %',
              D.Z('Lea trifft beim Basketball mit 60 %, Tom mit 50 %. Jeder wirft einmal (unabhängig). Wie groß ist die Wahrscheinlichkeit, dass mindestens einer trifft?',
                  0.8, '1 - 0.4 * 0.5', 'Gegenereignis „keiner trifft“: 0,4 · 0,5 = 0,2. Also P(mindestens einer) = 1 − 0,2 = 0,8.',
                  'Rechne über das Gegenereignis: Beide verfehlen – mit unterschiedlichen Wahrscheinlichkeiten.'))
    # baum_ergaenzen: Gesamtwahrscheinlichkeit „positiver Test“ (zwei Pfade addieren) = 2. Pfadregel in Einkleidung → Stufe 2
    D.stufe(range(124, 130), 2, 'Eine Krankheit ist bei')
    # simulation: relative Häufigkeit ablesen ist eine Division (Stufe 1); „zwei Treffer“ erwarten = Pfad · n (Stufe 2); „kein Gedächtnis“ dreimal gleich
    D.stufe(range(146, 152), 1, 'Eine Simulation wurde')
    D.stufe([152, 153, 155], 2, 'Ein Zufallsgerät liefert')
    D.stufe([156, 157], 2, 'Bei einem Würfel kam')
    # verstehen: „Addieren statt multiplizieren“ gehört zu Stufe 1, „ohne Zurücklegen falsch“ steht schon auf Stufe 2;
    # zweimal „Äste ergeben nicht 1“ auf Stufe 2 = Stufe 1 → durch andere Prüf-Aufgaben ersetzt
    D.stufe(178, 1, 'In einer Urne liegen 2 weiße')
    D.stufe([181, 182, 183], 2, '')
    D.ersetze(176, 'An einer Verzweigung stehen die Äste 0,1 und 0,8',
              D.A('Jemand sagt: „Ohne Zurücklegen sind P(rot, blau) und P(blau, rot) verschieden, weil sich beim zweiten Zug der Nenner ändert.“ Was stimmt?',
                  'Falsch: Beide Pfade ergeben dasselbe Produkt, z. B. 3/5 · 2/4 = 2/5 · 3/4.',
                  ['Richtig.', 'Falsch: Sie sind nur mit Zurücklegen verschieden.', 'Falsch: P(rot, blau) ist immer doppelt so groß.'],
                  'Bei r roten und b blauen Kugeln (n zusammen): r/n · b/(n − 1) und b/n · r/(n − 1) – dieselben Faktoren in anderer Reihenfolge.',
                  'Rechne beide Pfade für 3 rote und 2 blaue Kugeln aus.'))
    D.ersetze(177, 'An einer Verzweigung stehen die Äste 0,3 und 0,2',
              D.A('Jemand sagt: „Bei zwei Münzwürfen gilt P(zweimal Kopf) + P(zweimal Zahl) = 1.“ Was stimmt?',
                  'Falsch: Das ergibt 1/4 + 1/4 = 1/2; es fehlen die Pfade (K, Z) und (Z, K).',
                  ['Richtig.', 'Falsch: Das ergibt 1/4.', 'Falsch: Das ergibt 2.'],
                  'Der Baum hat vier Pfade mit je 1/4. „Zweimal gleich“ sind nur zwei davon: 1/2. Erst alle vier zusammen ergeben 1.',
                  'Zeichne alle Pfade des Baums. Welche fehlen?'))
    D.fuer_sebastian('stochastik.mehrstufig/simulation (Übungen Stufe 3, π aus Zufallspunkten im Kreis) überschneidet sich mit der neuen Karte pi_schaetzen (Runde 18) '
                     'und mit stochastik.simulation/monte_carlo – alle drei im Block Darwin. Die beiden π-Übungen in simulation könnten dort entfallen (Sperren ist Sache des Haupt-Chats).')
    D.anwenden()


if __name__ == '__main__':
    durchsicht()  # Neunzehnte Runde (durchsicht-kl10) – ganz am Ende


# ---------- STUFEN (Zwanzigste Runde, Zweig stufen-kl10) ----------
def stufen():
    import math
    import sys as _sys
    from fractions import Fraction as _F
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _stufen_kl10 import Stufen
    S = Stufen('stochastik.mehrstufig', 2030)
    Z, A, ZR = S.Z, S.A, S.ZR

    def B(text, zaehler, nenner, w, h):
        f = _F(zaehler, nenner)
        assert (f.numerator, f.denominator) == (zaehler, nenner), (text, f)
        return S.L(text, '□/□', [zaehler, nenner], [str(zaehler), str(nenner)], w, h, hinweis='Zähler und Nenner (gekürzt)')

    # --- pfad_mult ---
    S.stufenleiter('pfad_mult', 'Pfade im Baumdiagramm erkennen und entlang eines Pfades malnehmen (zwei gleiche Züge).',
                   'Verschiedene Äste in fester Reihenfolge, drei Stufen, Sachsituationen wie Freiwürfe, Ereignisse mit Gegenrechnung.',
                   'Vom Term zum Ereignis, unbekannter Ast, Anzahl der Kugeln als Parameter, Fehler „addieren statt malnehmen“, Aussagen prüfen, Prüfungsaufgabe.')
    S.g('pfad_mult', direkt=[0, 1, 2, 3, 4, 5], einkleidung=[6, 8, 10, 196], mehrschritt=[7, 11, 9, 12, 13, 14, 17, 15, 16], umkehr=[197],
        rueckwaerts=[198, 201], pruefung=[199], transfer=[200])
    S.ueberzaehlig(3, 4, 5, 14, 15, 16, 17)
    S.neu('pfad_mult', 'erkennen', A('Ein Glücksrad zeigt Rot mit 1/3 und Blau mit 2/3. Es wird zweimal gedreht. Welcher Term gehört zum Pfad (blau, rot)?', '2/3 · 1/3',
                                     ['2/3 + 1/3', '1/3 · 1/3', '2/3 · 2/3'], 'Erst der Ast „blau“ mit 2/3, dann „rot“ mit 1/3; entlang des Pfades malnehmen.', 'Welche zwei Äste liegen auf diesem Pfad?'))
    S.neu('pfad_mult', 'erkennen', A('Bei zwei Zügen mit Zurücklegen hat jede Verzweigung die Äste „rot“ (0,6) und „weiß“ (0,4). Wie viele Pfade hat das Baumdiagramm?', '4', ['2', '3', '6'],
                                     'Erste Stufe 2 Äste, an jedem wieder 2: 2 · 2 = 4 Pfade (rr, rw, wr, ww).', 'Zähle die Enden ganz rechts.'))
    S.neu('pfad_mult', 'fehler', A('Jemand rechnet beim zweimaligen Würfeln: „P(zwei Sechsen) = 1/6 + 1/6 = 1/3.“ Was stimmt?', 'Falsch: Entlang eines Pfades wird malgenommen: 1/6 · 1/6 = 1/36.',
                                   ['Richtig.', 'Falsch: 2/6 · 2/6 = 1/9.', 'Falsch: 1/6 − 1/6 = 0.'],
                                   'Zwei Sechsen ist ein einziger Pfad. Addieren macht man nur über verschiedene Pfade. 1/3 wäre viel zu groß: Nur in 1 von 36 Fällen fallen zwei Sechsen.', 'Ist das ein Pfad oder sind es zwei?'))
    S.neu('pfad_mult', 'begruenden', A('Stimmt: „Je mehr Stufen ein Pfad hat, desto kleiner oder gleich ist seine Wahrscheinlichkeit“?', 'Ja: Jeder weitere Ast ist eine Zahl zwischen 0 und 1, Malnehmen damit vergrößert nicht.',
                                       ['Nein: Bei Ästen über 0,5 wird das Produkt größer.', 'Nein: Malnehmen vergrößert immer.', 'Ja, aber nur beim Würfel.'],
                                       'Für 0 ≤ p ≤ 1 gilt a · p ≤ a. Beispiel: 0,9 · 0,9 = 0,81 < 0,9.', 'Was passiert, wenn man mit einer Zahl zwischen 0 und 1 malnimmt?'))
    S.neu('pfad_mult', 'verknuepfen', Z('Eine Münze wird zehnmal geworfen. P(jedes Mal Kopf) = 1/n. Wie groß ist n?', 1024, '2 ** 10',
                                        '(1/2)¹⁰ = 1/2¹⁰ = 1/1 024, also n = 1 024.', 'Schreibe das Produkt von zehn gleichen Faktoren als Potenz.'))
    S.neu('pfad_mult', 'parameter', Z('In einer Urne liegen 3 rote und x weiße Kugeln. Es wird zweimal mit Zurücklegen gezogen; P(rot, rot) = 1/4. Wie groß ist x?', 3, '6 - 3',
                                      '(3/(3 + x))² = 1/4 ⇒ 3/(3 + x) = 1/2 ⇒ 3 + x = 6 ⇒ x = 3.', 'Welcher Ast ergibt mit sich selbst malgenommen 1/4?'))
    S.bonus('pfad_mult', B('Drei Personen werfen gleichzeitig je eine Münze. Wer als Einzige(r) ein anderes Ergebnis hat als die beiden anderen, scheidet aus. Wie groß ist die Wahrscheinlichkeit, dass in einer Runde jemand ausscheidet?', 3, 4,
                           'Niemand scheidet nur aus, wenn alle dasselbe werfen: KKK oder ZZZ, zusammen 2 · 1/8 = 1/4. Sonst zeigen genau zwei dasselbe, und der Dritte scheidet aus: 1 − 1/4 = 3/4.',
                           'Wann scheidet niemand aus?'))
    S.bonus('pfad_mult', B('Ein Würfel wird so lange geworfen, bis zum ersten Mal eine Sechs fällt. Wie groß ist die Wahrscheinlichkeit, dass das beim 1., 3., 5., … Wurf (also bei einem ungeraden Wurf) passiert?', 6, 11,
                           'Sei p die gesuchte Wahrscheinlichkeit. Entweder Sechs im 1. Wurf (1/6), oder zwei Würfe ohne Sechs (25/36) – dann beginnt alles von vorn: p = 1/6 + 25/36 · p. '
                           'Also p · 11/36 = 1/6 und p = 6/11.', 'Was ist nach zwei Würfen ohne Sechs anders als am Anfang?'))

    # --- pfad_add ---
    S.stufenleiter('pfad_add', 'Die Pfade eines Ereignisses finden und ihre Wahrscheinlichkeiten addieren.',
                   'Ereignisse mit mehreren Pfaden („dieselbe Farbe“, „genau zweimal“), Augensummen, verschiedene Glücksräder.',
                   'Produkte und Summen über drei Würfel, Wahrscheinlichkeit rückwärts, p als Parameter, Fehler „nur ein Pfad“, Vergleich zweier Räder, Prüfungsaufgabe.')
    S.g('pfad_add', direkt=[28, 29, 30, 31, 32, 33], mehrschritt=[34, 35, 36, 37, 38, 39, 207], einkleidung=[40, 41, 42, 43, 44, 45, 203], darstellung=[202],
        transfer=[204], begruenden=[205], verknuepfen=[206])
    S.ueberzaehlig(31, 32, 33, 36, 37, 38, 39)
    S.neu('pfad_add', 'erkennen', A('Eine Münze wird zweimal geworfen. Welche Pfade gehören zum Ereignis „genau einmal Kopf“?', '(K, Z) und (Z, K)', ['nur (K, Z)', '(K, K) und (Z, Z)', '(K, Z), (Z, K) und (K, K)'],
                                    'Genau einmal Kopf: entweder zuerst Kopf und dann Zahl oder umgekehrt.', 'Die Reihenfolge zählt mit.'))
    S.neu('pfad_add', 'erkennen', A('Zu einem Ereignis gehören zwei Pfade mit 0,12 und 0,28. Wie berechnet man seine Wahrscheinlichkeit?', '0,12 + 0,28', ['0,12 · 0,28', '0,28 − 0,12', '(0,12 + 0,28) : 2'],
                                    'Verschiedene Pfade eines Ereignisses werden addiert: 0,40.', 'Malnehmen gilt entlang eines Pfades – und über mehrere Pfade?'))
    S.neu('pfad_add', 'fehler', A('Jemand rechnet bei zwei Münzwürfen: „P(genau einmal Kopf) = 1/2 · 1/2 = 1/4.“ Was stimmt?', 'Falsch: Es gibt zwei Pfade (K, Z) und (Z, K): 1/4 + 1/4 = 1/2.',
                                  ['Richtig.', 'Falsch: 1/2 + 1/2 = 1.', 'Falsch: 1/2 · 1/2 · 2 = 1.'], 'Der Pfad (Z, K) wurde vergessen. Beide zusammen ergeben 1/2.', 'Wie viele Pfade gehören zu „genau einmal“?'))
    S.neu('pfad_add', 'parameter', Z('Ein Spiel wird zweimal gespielt, jedes Mal gewinnt man mit der Wahrscheinlichkeit p. Für welches p ist P(genau ein Gewinn) am größten?', 0.5, '1 / 2',
                                     'P(genau ein Gewinn) = 2 · p · (1 − p). Werte: p = 0,3: 0,42; p = 0,5: 0,5; p = 0,7: 0,42. Das Maximum liegt bei p = 0,5 (Scheitel der Parabel 2p − 2p²).',
                                     'Stelle den Term mit p auf und denke an eine Parabel.'))
    S.neu('pfad_add', 'pruefung', B('Ein Glücksrad zeigt 1 mit 1/2, 2 mit 1/3 und 3 mit 1/6. Es wird zweimal gedreht, die Zahlen werden addiert. Wie groß ist P(Summe = 4)?', 5, 18,
                                    'Pfade (1, 3), (3, 1), (2, 2): 1/12 + 1/12 + 1/9 = 3/36 + 3/36 + 4/36 = 10/36 = 5/18.', 'Welche Paare ergeben die Summe 4?'))
    S.neu('pfad_add', 'rueckwaerts', Z('Bei zwei unabhängigen Runden eines Spiels ist P(beide gewonnen) = 0,09. Wie groß ist P(genau einmal gewonnen)?', 0.42, '2 * 0.3 * 0.7',
                                       'p² = 0,09 ⇒ p = 0,3. P(genau einmal) = 0,3 · 0,7 + 0,7 · 0,3 = 0,42.', 'Bestimme zuerst die Gewinnwahrscheinlichkeit einer Runde.'))
    S.neu('pfad_add', 'transfer', B('Glücksrad A zeigt 1, 2 oder 3, Glücksrad B zeigt 2 oder 4 (jeweils gleich wahrscheinlich). Beide werden gedreht. Wie groß ist P(A zeigt die größere Zahl)?', 1, 6,
                                    'Nur bei A = 3 und B = 2 ist A größer: 1/3 · 1/2 = 1/6.', 'Gehe alle 6 Paare durch.'))
    S.bonus('pfad_add', B('Zwei Würfel werden geworfen. Wie groß ist die Wahrscheinlichkeit, dass die Augensumme eine Primzahl ist?', 5, 12,
                          'Primzahlen 2, 3, 5, 7, 11 mit 1, 2, 4, 6, 2 Pfaden: zusammen 15 von 36 = 5/12.', 'Zähle für jede mögliche Primzahl die Paare.'))
    S.bonus('pfad_add', B('Anna und Ben werfen abwechselnd eine Münze, Anna beginnt. Wer zuerst Kopf wirft, gewinnt. Wie groß ist Annas Gewinnwahrscheinlichkeit?', 2, 3,
                          'Annas Gewinnwahrscheinlichkeit sei p. Wirft Anna im 1. Wurf Zahl (Wahrscheinlichkeit 1/2), ist Ben genau in Annas Anfangslage und gewinnt dann mit p. '
                          'Ben gewinnt also mit 1/2 · p. Einer von beiden gewinnt sicher: p + p/2 = 1 ⇒ p = 2/3.', 'Vergleiche Annas und Bens Lage: Was muss passieren, bevor Ben überhaupt werfen darf?'))

    # --- ohne_zuruecklegen ---
    S.stufenleiter('ohne_zuruecklegen', 'Die Äste der zweiten Stufe anpassen (Nenner und Zähler werden kleiner) und gleiche Farben berechnen.',
                   'Verschiedene Farben, drei Züge, Lostrommeln, feste Reihenfolge.',
                   'Zweite Kugel, „spätestens sicher“, Anzahl rückwärts aus einem Ast, n als Parameter, Fehler „mit Zurücklegen gerechnet“, Kartenspiel, Prüfungsaufgabe.')
    S.g('ohne_zuruecklegen', direkt=[56, 57, 58, 59, 60, 61], mehrschritt=[62, 63, 64, 65, 66, 67, 211], einkleidung=[69, 70, 71, 72, 73, 209], umkehr=[208],
        verknuepfen=[68], transfer=[210], begruenden=[212], parameter=[213])
    S.ueberzaehlig(59, 60, 61, 64, 65, 66, 67)
    S.neu('ohne_zuruecklegen', 'erkennen', A('In einer Urne liegen 4 rote und 6 blaue Kugeln. Die erste gezogene Kugel ist rot und wird nicht zurückgelegt. Welche Äste stehen an der zweiten Stufe?',
                                             'rot 3/9, blau 6/9', ['rot 4/10, blau 6/10', 'rot 3/10, blau 6/10', 'rot 4/9, blau 5/9'],
                                             'Es fehlt eine rote Kugel: 3 rote und 6 blaue, zusammen 9.', 'Wie viele Kugeln welcher Farbe sind noch drin?'))
    S.neu('ohne_zuruecklegen', 'erkennen', A('Bei welchem Vorgang zieht man ohne Zurücklegen?', 'Lose aus einer Lostrommel ziehen und behalten',
                                             ['Einen Würfel dreimal werfen', 'Ein Glücksrad zweimal drehen', 'Eine Münze zweimal werfen'],
                                             'Nur bei den Losen ändert sich der Inhalt: Ein gezogenes Los fehlt beim nächsten Zug.', 'Wo ändert sich nach dem ersten Mal etwas?'))
    S.neu('ohne_zuruecklegen', 'fehler', A('5 Lose, davon 2 Gewinne; man zieht 2 Lose. Jemand rechnet: „P(zwei Gewinne) = 2/5 · 2/5 = 4/25.“ Was stimmt?',
                                           'Falsch: Nach dem ersten Gewinn ist noch 1 Gewinn unter 4 Losen: 2/5 · 1/4 = 1/10.', ['Richtig.', 'Falsch: 2/5 · 1/5 = 2/25.', 'Falsch: 2/5 + 1/4 = 13/20.'],
                                           'Das gezogene Los kommt nicht zurück. Zweiter Ast: 1 von 4.', 'Was ist beim zweiten Zug anders?'))
    S.neu('ohne_zuruecklegen', 'pruefung', Z('In einem Beutel liegen 6 Äpfel und 4 Birnen. Man nimmt ohne hinzusehen nacheinander Früchte heraus (ohne Zurücklegen). Wie viele Früchte muss man herausnehmen, damit auf jeden Fall zwei Birnen dabei sind?',
                                             8, '6 + 2', 'Schlimmster Fall: erst alle 6 Äpfel. Danach sind nur noch Birnen drin: 6 + 2 = 8 Früchte.', 'Denke an den ungünstigsten Fall.'))
    S.neu('ohne_zuruecklegen', 'rueckwaerts', Z('Aus einer Urne mit 3 roten und einigen blauen Kugeln wird zweimal ohne Zurücklegen gezogen. Am Ast „rot, dann rot“ steht beim zweiten Zug 2/7. Wie viele blaue Kugeln liegen in der Urne?',
                                                5, '7 + 1 - 3', 'Nach einer roten Kugel sind noch 2 rote von 7 Kugeln da. Also waren es 8 Kugeln, davon 3 rot: 5 blaue.', 'Wie viele Kugeln waren vor dem ersten Zug drin?'))
    S.neu('ohne_zuruecklegen', 'transfer', B('Ein Skatspiel hat 32 Karten, darunter 4 Buben. Zwei Karten werden zufällig gezogen. Wie groß ist P(beide sind Buben)?', 3, 248,
                                             '4/32 · 3/31 = 12/992 = 3/248.', 'Wie viele Buben und Karten sind nach dem ersten Buben übrig?'))
    S.bonus('ohne_zuruecklegen', B('In einer Schublade liegen 4 rote und 4 blaue Socken. Man nimmt im Dunkeln zwei heraus. Wie groß ist die Wahrscheinlichkeit, dass sie dieselbe Farbe haben?', 3, 7,
                                   'Nach der ersten Socke (egal welche Farbe) passen noch 3 der restlichen 7 Socken: 3/7. Über den Baum: 4/8 · 3/7 + 4/8 · 3/7 = 3/7.',
                                   'Die erste Socke ist egal – worauf kommt es dann an?'))
    S.bonus('ohne_zuruecklegen', B('In einer Urne liegen 2 rote und 2 blaue Kugeln. Man zieht alle vier nacheinander ohne Zurücklegen. Wie groß ist die Wahrscheinlichkeit, dass sich die Farben abwechseln?', 1, 3,
                                   'Abwechselnd heißt rbrb oder brbr. P(rbrb) = 2/4 · 2/3 · 1/2 · 1 = 1/6, ebenso brbr. Zusammen 1/3. (Es gibt 6 gleich wahrscheinliche Farbfolgen, 2 davon passen.)',
                                   'Schreibe alle möglichen Farbfolgen auf.'))

    # --- gegenereignis ---
    S.stufenleiter('gegenereignis', 'Das Gegenereignis von „mindestens einmal“ benennen und P = 1 − P(keinmal) rechnen.',
                   'Sachsituationen (Lose, Bauteile), gerade Zahlen, verschiedene Augenzahlen, der passende Term im Baumdiagramm.',
                   'Mindestanzahl Versuche, Treffer-Wahrscheinlichkeit als Parameter, „mindestens“ − „genau“, zwei Personen, Fehler, Term wie in der Prüfung.')
    S.g('gegenereignis', direkt=[84, 87, 85, 86, 88, 89], einkleidung=[90, 92, 91, 93, 94, 95], mehrschritt=[214, 215],
        rueckwaerts=[96, 97, 99, 101], verknuepfen=[98], transfer=[100, 218], pruefung=[216], parameter=[217], fehler=[219])
    S.ueberzaehlig(87, 88, 89, 92, 94, 95)
    S.neu('gegenereignis', 'erkennen', A('Was ist das Gegenereignis von „mindestens eine Sechs“ bei drei Würfen?', 'keine Sechs', ['genau eine Sechs', 'höchstens eine Sechs', 'drei Sechsen'],
                                         'Das Gegenteil von „mindestens eine“ ist „gar keine“. Zusammen ergeben beide alle Möglichkeiten.', 'Was bleibt übrig, wenn „mindestens eine“ nicht eintritt?'))
    S.neu('gegenereignis', 'erkennen', A('Bei 4 Würfen ist P(keine Sechs) ≈ 0,48. Wie groß ist P(mindestens eine Sechs)?', '1 − 0,48 = 0,52', ['0,48', '4 · 1/6 ≈ 0,67', '(1/6)⁴'],
                                         'Ereignis und Gegenereignis ergeben zusammen 1.', 'Ereignis plus Gegenereignis ergibt …?'))
    S.neu('gegenereignis', 'darstellung', A('Im Baumdiagramm für drei Versuche ist nur der Pfad „nie Treffer“ markiert, jeder seiner Äste hat 0,7. Welcher Term liefert P(mindestens ein Treffer)?', '1 − 0,7³',
                                            ['0,7³', '3 · 0,3', '1 − 0,3³'], 'Der markierte Pfad ist das Gegenereignis: 0,7³ = 0,343. Also P = 1 − 0,343 = 0,657.', 'Welches Ereignis zeigt der markierte Pfad?'))
    S.bonus('gegenereignis', Z('Wie oft muss man mindestens würfeln, damit die Wahrscheinlichkeit für mindestens eine Sechs größer als 1/2 ist?', 4, '4',
                               '(5/6)ⁿ < 1/2: (5/6)³ ≈ 0,579, (5/6)⁴ ≈ 0,482. Also 4 Würfe. (Viele schätzen 3, weil 3 · 1/6 = 1/2 – aber Wahrscheinlichkeiten addiert man hier nicht.)',
                               'Rechne mit dem Gegenereignis und probiere n = 3 und n = 4.', einheit='Würfe'))
    S.bonus('gegenereignis', B('4 Personen treffen sich. Wie groß ist die Wahrscheinlichkeit, dass mindestens zwei im selben Monat Geburtstag haben (alle Monate gleich wahrscheinlich)?', 41, 96,
                               'Gegenereignis: alle in verschiedenen Monaten: 12/12 · 11/12 · 10/12 · 9/12 = 11 880/20 736 = 55/96. Also 1 − 55/96 = 41/96 ≈ 0,43.',
                               'Rechne die Wahrscheinlichkeit aus, dass alle Monate verschieden sind.'))

    # --- baum_ergaenzen ---
    S.stufenleiter('baum_ergaenzen', 'Den Gegenast ergänzen (Äste einer Verzweigung ergeben 1) und Pfadwahrscheinlichkeiten deuten.',
                   'Einen Ast durch Teilen bestimmen, Gesamtwahrscheinlichkeit über zwei Pfade, Sachsituationen wie Tests und Anteile.',
                   'Fehlende Äste aus P(B), Kugelzahl aus Ästen, Wurzel aus einem Pfad, p als Parameter, Fehler, Unmögliches begründen, Vierfeldertafel wie im BMT.')
    S.g('baum_ergaenzen', direkt=[112, 113, 114, 115, 116, 117], umkehr=[118, 119, 120, 121, 122, 123, 220], einkleidung=[124, 125, 126, 127, 128, 129, 221], mehrschritt=[225],
        rueckwaerts=[222], transfer=[223], verknuepfen=[224])
    S.neu('baum_ergaenzen', 'erkennen', A('Welche zwei Zahlen können an den beiden Ästen einer Verzweigung stehen?', '0,35 und 0,65', ['0,35 und 0,75', '0,5 und 0,6', '0,2 und 0,2'],
                                          'Die Äste einer Verzweigung ergeben zusammen 1: 0,35 + 0,65 = 1.', 'Rechne jeweils die Summe aus.'))
    S.neu('baum_ergaenzen', 'erkennen', A('Im Baumdiagramm ist P(A) = 0,3, am Ast von A nach B steht 0,5. Was bedeutet 0,3 · 0,5 = 0,15?', 'die Wahrscheinlichkeit des Pfades „A, dann B“',
                                          ['P(B) insgesamt', 'die Wahrscheinlichkeit von „nicht A“', 'der Ast von B nach A'],
                                          'Entlang eines Pfades wird malgenommen; das Produkt ist die Pfadwahrscheinlichkeit, nicht P(B) insgesamt.', 'Was liefert das Malnehmen entlang eines Pfades?'))
    S.neu('baum_ergaenzen', 'mehrschritt', Z('Im Baumdiagramm ist P(A) = 0,6, der Ast A → B hat 0,5 und der Ast „nicht A“ → B hat 0,25. Berechne P(B).', 0.4, '0.6 * 0.5 + 0.4 * 0.25',
                                             'Zwei Pfade enden bei B: 0,6 · 0,5 + 0,4 · 0,25 = 0,3 + 0,1 = 0,4.', 'Welche Pfade führen zu B? Vergiss P(nicht A) = 0,4 nicht.'))
    S.neu('baum_ergaenzen', 'fehler', A('P(A) = 0,4; die Äste A → B und „nicht A“ → B haben beide 0,5. Jemand rechnet P(B) = 0,5 + 0,5 = 1. Was stimmt?',
                                        'Falsch: P(B) = 0,4 · 0,5 + 0,6 · 0,5 = 0,5.', ['Richtig.', 'Falsch: P(B) = 0,4 · 0,5 = 0,2.', 'Falsch: P(B) = 0,25.'],
                                        'Zu B führen zwei Pfade; erst entlang jedes Pfades malnehmen, dann addieren.', 'Rechne zuerst die beiden Pfade aus.'))
    S.neu('baum_ergaenzen', 'begruenden', A('Kann in einem Baumdiagramm P(A) = 0,3 und die Pfadwahrscheinlichkeit „A, dann B“ = 0,4 sein?', 'Nein: Ein Pfad ist nie wahrscheinlicher als sein erster Ast.',
                                            ['Ja, das ist möglich.', 'Nein, weil 0,3 + 0,4 ≠ 1.', 'Ja, wenn P(B) = 0,7 ist.'],
                                            'Der Ast A → B wäre 0,4 : 0,3 ≈ 1,33 – größer als 1, also unmöglich.', 'Rechne den Ast von A nach B aus.'))
    S.neu('baum_ergaenzen', 'parameter', Z('Im Baumdiagramm ist P(A) = p, der Ast A → B hat 0,5 und der Ast „nicht A“ → B hat 0,2. Für welches p ist P(B) = 0,32?', 0.4, '(0.32 - 0.2) / (0.5 - 0.2)',
                                           '0,5p + 0,2(1 − p) = 0,32 ⇒ 0,3p + 0,2 = 0,32 ⇒ p = 0,4.', 'Stelle P(B) als Term mit p auf.'))
    S.neu('baum_ergaenzen', 'pruefung', Z('Von 800 untersuchten Bäumen haben 240 Käferbefall; 96 davon haben auch Trockenschäden. Von den Bäumen ohne Käferbefall haben 112 Trockenschäden. '
                                          'Wie groß ist die Wahrscheinlichkeit, dass ein zufällig gewählter Baum mindestens einen der beiden Schäden hat?', 0.44, '(240 + 112) / 800',
                                          'Mindestens ein Schaden: alle 240 mit Käferbefall plus die 112 nur mit Trockenschaden = 352. 352 : 800 = 0,44.', 'Zähle jeden Baum nur einmal.'))
    S.neu('baum_ergaenzen', 'rueckwaerts', Z('In einer Klasse tragen 30 % eine Brille. Die Hälfte der Klasse sind Jungen, von ihnen tragen 20 % eine Brille. Wie viel Prozent der Mädchen tragen eine Brille?', 40,
                                             '(0.3 - 0.5 * 0.2) / 0.5 * 100', '0,5 · 0,2 + 0,5 · x = 0,3 ⇒ 0,5x = 0,2 ⇒ x = 0,4, also 40 %.', 'Stelle P(Brille) über beide Pfade auf.', einheit='%'))
    S.bonus('baum_ergaenzen', A('1 % der Menschen haben eine Krankheit. Ein Test erkennt sie bei 99 % der Kranken; bei 1 % der Gesunden zeigt er fälschlich „positiv“. Jemand wird positiv getestet. Wie groß ist die Wahrscheinlichkeit, dass er krank ist?',
                                'etwa 50 %', ['etwa 99 %', 'etwa 1 %', 'etwa 90 %'],
                                'Pfad krank & positiv: 0,01 · 0,99 = 0,0099. Pfad gesund & positiv: 0,99 · 0,01 = 0,0099. Beide gleich groß, also ist von den Positiven genau die Hälfte krank.',
                                'Vergleiche die beiden Pfade, die zu „positiv“ führen.'))
    S.bonus('baum_ergaenzen', B('Urne A enthält 2 rote und 1 blaue Kugel, Urne B 1 rote und 2 blaue. Eine Münze entscheidet über die Urne, dann wird eine Kugel gezogen. Sie ist rot. Mit welcher Wahrscheinlichkeit stammt sie aus Urne A?', 2, 3,
                                'P(A, rot) = 1/2 · 2/3 = 1/3, P(B, rot) = 1/2 · 1/3 = 1/6. Unter den roten Fällen hat A den Anteil (1/3) : (1/3 + 1/6) = 2/3.',
                                'Welche beiden Pfade enden bei „rot“? Welchen Anteil hat der Pfad über A?'))

    # --- simulation ---
    S.stufenleiter('simulation', 'Erwartete Anzahl n · p berechnen und relative Häufigkeiten ablesen.',
                   'Mehrstufige Ereignisse hochrechnen, p aus einer erwarteten Anzahl, Zufallszahlen einem Ereignis zuordnen.',
                   'Schwankungen begründen, Gedächtnis-Irrtum, π schätzen, rückwärts zur nötigen Trefferzahl, erwarteter Gewinn, Fehler „genau 100-mal“.')
    S.g('simulation', direkt=[140, 142, 144, 141, 143, 145], erkennen=[146, 147, 148, 149, 150, 151], einkleidung=[152, 153, 155], darstellung=[226], mehrschritt=[227],
        begruenden=[154, 156, 157, 231], verknuepfen=[228, 229], rueckwaerts=[230])
    S.ueberzaehlig(142, 145)
    S.neu('simulation', 'umkehr', Z('Bei 400 Durchführungen erwartet man 100-mal ein bestimmtes Ergebnis. Wie groß ist seine Wahrscheinlichkeit?', 0.25, '100 / 400',
                                    'n · p = 100 mit n = 400 ⇒ p = 100 : 400 = 0,25.', 'Erwartete Anzahl = n · p – rückwärts.'))
    S.neu('simulation', 'mehrschritt', Z('Ein Glücksrad hat 8 gleich große Felder, 3 davon gelb. Es wird zweimal gedreht; das Ganze wird 320-mal wiederholt. Wie oft erwartet man „zweimal gelb“?', 45, '320 * 3 * 3 / 64',
                                         'P(zweimal gelb) = 3/8 · 3/8 = 9/64. 320 · 9/64 = 45.', 'Erst die Pfadwahrscheinlichkeit, dann mal 320.'))
    S.neu('simulation', 'fehler', A('Jemand sagt: „Bei 600 Würfen fällt die Sechs genau 100-mal.“ Was stimmt?', 'Falsch: 100 ist nur der Erwartungswert; die tatsächliche Zahl schwankt.',
                                    ['Richtig.', 'Falsch: Sie fällt genau 60-mal.', 'Falsch: Sie fällt höchstens 100-mal.'],
                                    '600 · 1/6 = 100 ist ein Mittelwert, keine Vorhersage. 93 oder 108 Sechsen sind ganz normal.', 'Was bedeutet „erwarten“?'))
    S.neu('simulation', 'transfer', Z('Ein Spiel: Man wirft zwei Münzen. Bei zweimal Kopf bekommt man 3 €, sonst nichts. Ein Spiel kostet 1 €. Mit welchem Gewinn rechnet ein Spieler bei 100 Spielen? (Verlust negativ angeben)',
                                      -25, '100 * (3 * 1 / 4 - 1)', 'Zweimal Kopf hat 1/4: in 100 Spielen etwa 25-mal, also 75 € Auszahlung. Einsatz 100 €. Ergebnis 75 − 100 = −25 €.',
                                      'Wie oft gewinnt man in 100 Spielen etwa?', einheit='€'))
    S.bonus('simulation', Z('Ein Würfel wird 60-mal geworfen. Welche Augensumme aller 60 Würfe erwartet man?', 210, '60 * 21 / 6',
                            'Jede Augenzahl erwartet man 10-mal: 10 · (1 + 2 + 3 + 4 + 5 + 6) = 10 · 21 = 210. Oder: Der mittlere Wurf hat 3,5 Augen, 60 · 3,5 = 210.',
                            'Wie oft erwartet man jede einzelne Augenzahl?'))
    S.bonus('simulation', Z('Aus einer Urne mit 1 roten und 2 blauen Kugeln wird mit Zurücklegen gezogen, bis Rot kommt. Wie viele Züge braucht man im Mittel (rote Kugel mitgezählt)?', 3, '1 / (1 / 3)',
                            'Bei sehr vielen Zügen ist jeder dritte rot. Bei 300 Zügen kommen etwa 100 rote – die 300 Züge zerfallen also in etwa 100 Abschnitte „bis Rot“, je im Mittel 3 Züge lang.',
                            'Denke an eine lange Folge von Zügen: Wie viele Rote kommen darin vor?'))

    # --- pi_schaetzen ---
    S.stufenleiter('pi_schaetzen', 'Aus dem Anteil der Punkte im Viertelkreis π schätzen; prüfen, ob ein Punkt im Viertelkreis liegt.',
                   'Tabellenkalkulation, Streifen über und unter dem Bogen, Treffer rückwärts, Kreis im Quadrat mit Seite 2.',
                   'Grenzen der Verfahren begründen, Streifenzahl als Parameter, Fehler „π/4 statt π“, Punkte mit Pythagoras prüfen, rückwärts zur Mindestzahl, Ring zwischen zwei Viertelkreisen.')
    S.g('pi_schaetzen', direkt=[238, 240, 241], erkennen=[239], darstellung=[242], mehrschritt=[243, 244, 248, 249], umkehr=[246], einkleidung=[247],
        begruenden=[245, 251, 254], parameter=[250], fehler=[252], verknuepfen=[253], rueckwaerts=[255])
    S.neu('pi_schaetzen', 'erkennen', A('Welcher Punkt liegt NICHT im Viertelkreis mit Radius 1 um (0 | 0)?', '(0,8 | 0,7)', ['(0,5 | 0,5)', '(0,6 | 0,7)', '(0,1 | 0,9)'],
                                        'Prüfe x² + y² ≤ 1: 0,64 + 0,49 = 1,13 > 1. Die anderen: 0,5; 0,85; 0,82 – alle kleiner als 1.', 'Rechne x² + y² aus.'))
    S.neu('pi_schaetzen', 'einkleidung', ZR('Auf ein quadratisches Brett (Seite 40 cm) mit aufgemaltem Kreis (Durchmesser 40 cm) werfen Kinder blind Erbsen. 250 landen auf dem Brett, 193 davon im Kreis. '
                                            'Welchen Näherungswert für π ergibt das? Runde auf zwei Nachkommastellen.', 4 * 193 / 250, 2,
                                            'Kreis : Quadrat = π · 20² : 40² = π/4. Also π ≈ 4 · 193 : 250 = 3,088 ≈ 3,09.', 'Welchen Anteil des Quadrats bedeckt der Kreis?'))
    S.neu('pi_schaetzen', 'transfer', ZR('Im Einheitsquadrat liegen um die Ecke (0 | 0) ein Viertelkreis mit Radius 1 und ein Viertelkreis mit Radius 0,5. Wie groß ist die Wahrscheinlichkeit, dass ein Zufallspunkt im großen, '
                                         'aber nicht im kleinen Viertelkreis liegt? Runde auf drei Nachkommastellen.', math.pi / 4 - math.pi / 16, 3,
                                         'Fläche groß: π/4, klein: π · 0,25/4 = π/16. Differenz 3π/16 ≈ 0,589. Das Quadrat hat die Fläche 1.', 'Wahrscheinlichkeit = Fläche : Fläche des Quadrats.'))
    S.bonus('pi_schaetzen', ZR('Im Einheitsquadrat liegen zwei Viertelkreise mit Radius 1: einer um (0 | 0), einer um (1 | 1). Wie groß ist die Wahrscheinlichkeit, dass ein Zufallspunkt in beiden liegt? Runde auf drei Nachkommastellen.',
                               math.pi / 2 - 1, 3, 'Jeder Viertelkreis hat π/4. Zusammen bedecken sie das ganze Quadrat (jeder Punkt liegt in mindestens einem), also gilt π/4 + π/4 − Überlappung = 1. '
                               'Überlappung = π/2 − 1 ≈ 0,571.', 'Liegt jeder Punkt des Quadrats in mindestens einem der beiden Viertelkreise?'))
    S.bonus('pi_schaetzen', Z('Wie viele Zufallspunkte braucht man mindestens, damit der Schätzwert 4 · Treffer : Anzahl genau 3,14 sein kann?', 200, '200',
                              '4 · T/n = 3,14 ⇒ T/n = 0,785 = 157/200. 157/200 lässt sich nicht kürzen (157 ist eine Primzahl). Also muss die Anzahl n ein Vielfaches von 200 sein; die kleinste ist n = 200 (mit T = 157).',
                              'Schreibe 3,14 : 4 als gekürzten Bruch.', einheit='Punkte'))

    # --- verstehen ---
    S.stufenleiter('verstehen', 'Erkennen, dass Äste einer Verzweigung zusammen 1 ergeben und entlang eines Pfades malgenommen wird.',
                   'Einfache Aufgaben selbst richtig rechnen: mehrere Pfade, ohne Zurücklegen, ein Ast aus einem Pfad, Sachsituationen.',
                   'Fehler finden und deuten, Aussagen prüfen, Simulationsergebnisse beurteilen, Term rückwärts deuten, de Méré und Lotto.')
    S.g('verstehen', erkennen=[168, 169, 171, 173, 170, 172, 178], fehler=[174, 175, 180, 177, 179, 181, 182, 183], begruenden=[176, 232, 237],
        verknuepfen=[184, 185], rueckwaerts=[234], parameter=[235], transfer=[236, 233])
    S.ueberzaehlig(172, 178, 175, 181, 182, 183)
    S.neu('verstehen', 'direkt', B('Eine Münze wird zweimal geworfen. Berechne P(zweimal Kopf).', 1, 4, 'Ein Pfad: 1/2 · 1/2 = 1/4.', 'Entlang des Pfades malnehmen.'))
    S.neu('verstehen', 'direkt', B('Ein Würfel wird zweimal geworfen. Berechne P(zweimal eine Eins).', 1, 36, 'Ein Pfad: 1/6 · 1/6 = 1/36.', 'Entlang des Pfades malnehmen.'))
    S.neu('verstehen', 'mehrschritt', B('Eine Münze wird dreimal geworfen. Berechne P(genau zweimal Kopf).', 3, 8, 'Pfade KKZ, KZK, ZKK mit je 1/8: zusammen 3/8.', 'Welche Pfade haben genau zweimal Kopf?'))
    S.neu('verstehen', 'mehrschritt', B('In einer Urne liegen 2 rote und 3 blaue Kugeln. Zwei werden ohne Zurücklegen gezogen. Wie groß ist P(beide haben dieselbe Farbe)?', 2, 5,
                                        'rot-rot: 2/5 · 1/4 = 2/20; blau-blau: 3/5 · 2/4 = 6/20. Zusammen 8/20 = 2/5.', 'Zwei Pfade, beim zweiten Zug ändert sich die Urne.'))
    S.neu('verstehen', 'einkleidung', Z('Ein Bus ist mit der Wahrscheinlichkeit 0,9 pünktlich, die Bahn mit 0,8 (unabhängig). Wie groß ist die Wahrscheinlichkeit, dass beide pünktlich sind?', 0.72, '0.9 * 0.8',
                                        'Ein Pfad: 0,9 · 0,8 = 0,72.', 'Beide pünktlich ist ein Pfad.'))
    S.neu('verstehen', 'einkleidung', B('Bei einem Quiz rät jemand zwei Fragen mit je 4 Antworten (eine richtig). Wie groß ist die Wahrscheinlichkeit, dass beide Antworten richtig sind?', 1, 16,
                                        'Je Frage 1/4: 1/4 · 1/4 = 1/16.', 'Wie wahrscheinlich ist eine richtige Antwort beim Raten?'))
    S.neu('verstehen', 'umkehr', Z('Ein Pfad aus zwei gleichen Ästen hat die Wahrscheinlichkeit 0,36. Welche Wahrscheinlichkeit hat ein Ast?', 0.6, '6 / 10',
                                   'p · p = 0,36 ⇒ p = 0,6.', 'Welche Zahl mit sich selbst malgenommen ergibt 0,36?'))
    S.neu('verstehen', 'darstellung', B('Ein Baumdiagramm hat an der ersten Verzweigung die Äste 1/4 und 3/4, an jeder Verzweigung der zweiten Stufe die Äste 1/3 und 2/3. Wie groß ist die kleinste Pfadwahrscheinlichkeit?', 1, 12,
                                        'Kleinste Äste malnehmen: 1/4 · 1/3 = 1/12.', 'Welche Äste sind am kleinsten?'))
    S.bonus('verstehen', B('Eine Familie hat zwei Kinder (Junge und Mädchen je mit 1/2, unabhängig). Man weiß: Mindestens eines ist ein Mädchen. Wie groß ist dann die Wahrscheinlichkeit, dass beide Mädchen sind?', 1, 3,
                           'Gleich wahrscheinliche Fälle: JJ, JM, MJ, MM. „Mindestens ein Mädchen“ lässt JM, MJ, MM übrig. Nur MM passt: 1 von 3.',
                           'Schreibe alle vier Fälle auf und streiche die, die nicht mehr möglich sind.'))
    S.bonus('verstehen', B('Jemand sagt: „Von drei Münzen zeigen zwei sicher dasselbe, die dritte passt mit 50 % dazu – also zeigen alle drei mit 1/2 dasselbe.“ Wie groß ist P(alle drei gleich) wirklich?', 1, 4,
                           'KKK und ZZZ: 2 von 8 gleich wahrscheinlichen Fällen = 1/4. Der Fehler: Welche zwei Münzen gleich sind, steht vorher nicht fest – die „dritte Münze“ ist keine feste Münze.',
                           'Zähle alle 8 Möglichkeiten.'))
    S.anwenden()


if __name__ == '__main__':
    stufen()  # Zwanzigste Runde (stufen-kl10) – ganz am Ende


# ---- BEREINIGEN (Einundzwanzigste Runde) ----
if __name__ == '__main__':
    from _bereinigen import bereinigen_datei
    bereinigen_datei('stochastik.mehrstufig')
# ---- BEREINIGEN ENDE ----
