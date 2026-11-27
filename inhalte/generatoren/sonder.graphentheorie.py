#!/usr/bin/env python3
"""Thema sonder.graphentheorie – Graphentheorie (IB MYP 4, etwa Klasse 9)."""
import heapq
import itertools
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403
from _rsib2 import PLAN2, art3  # noqa: E402

start(6504)

POS = {'A': (0, 0), 'B': (3, 1.2), 'C': (6, 0), 'D': (6, -3.5), 'E': (3, -4.7), 'F': (0, -3.5), 'G': (3.5, -1.4)}
# kreuzungsfreie Kandidaten-Kanten (Sechseck außen, Speichen zur Mitte G; ohne G zusätzlich Sehnen)
MIT_G = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'A'), ('G', 'A'), ('G', 'B'), ('G', 'C'), ('G', 'D'), ('G', 'E'), ('G', 'F')]
OHNE_G = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'A'), ('B', 'F'), ('B', 'E'), ('C', 'E')]


def zusammen(knoten, kanten):
    if not knoten: return False
    nb = {k: set() for k in knoten}
    for u, v in kanten: nb[u].add(v); nb[v].add(u)
    weg, stapel = set(), [next(iter(knoten))]
    while stapel:
        k = stapel.pop()
        if k in weg: continue
        weg.add(k); stapel += list(nb[k] - weg)
    return weg == set(knoten)


def zufallsgraph(m_min, m_max, mit_g=None):
    mit_g = R.random() < .5 if mit_g is None else mit_g
    kand = MIT_G if mit_g else OHNE_G
    knoten = list('ABCDEFG') if mit_g else list('ABCDEF')
    for _ in range(500):
        m = R.randint(m_min, min(m_max, len(kand)))
        kanten = sorted(tuple(sorted(e)) for e in R.sample(kand, m))
        if zusammen(knoten, kanten) and all(any(k in e for e in kanten) for k in knoten): return knoten, kanten
    return None


def grad(knoten, kanten):
    return {k: sum(k in e for e in kanten) for k in knoten}


def bild(knoten, kanten, gew=None):
    return netz({k: POS[k] for k in knoten}, [(u, v, gew[(u, v)] if gew else '') for u, v in kanten])


def dijkstra(knoten, kanten, gew, s):
    nb = {k: [] for k in knoten}
    for (u, v) in kanten: nb[u].append((v, gew[(u, v)])); nb[v].append((u, gew[(u, v)]))
    dist, vor = {s: 0}, {}
    h = [(0, s)]
    while h:
        d, k = heapq.heappop(h)
        if d > dist.get(k, 1e9): continue
        for v, w in nb[k]:
            if d + w < dist.get(v, 1e9): dist[v] = d + w; vor[v] = k; heapq.heappush(h, (d + w, v))
    return dist, vor


def alle_wege(knoten, kanten, gew, s, z):
    nb = {k: [] for k in knoten}
    for (u, v) in kanten: nb[u].append(v); nb[v].append(u)
    out = []
    def geh(k, weg):
        if k == z: out.append(list(weg)); return
        for v in nb[k]:
            if v not in weg: weg.append(v); geh(v, weg); weg.pop()
    geh(s, [s])
    return [(sum(gew[tuple(sorted((w[i], w[i + 1])))] for i in range(len(w) - 1)), w) for w in out]


def graphisch(grade):
    """Havel-Hakimi: Gibt es einen einfachen Graphen mit dieser Gradfolge?"""
    g = sorted(grade, reverse=True)
    while g and g[0] > 0:
        d = g.pop(0)
        if d > len(g): return False
        for i in range(d):
            g[i] -= 1
            if g[i] < 0: return False
        g.sort(reverse=True)
    return True


def kruskal(knoten, kanten, gew):
    teil = {k: k for k in knoten}
    def f(k):
        while teil[k] != k: k = teil[k]
        return k
    baum = []
    for e in sorted(kanten, key=lambda e: gew[e]):
        a, b = f(e[0]), f(e[1])
        if a != b: teil[a] = b; baum.append(e)
    return baum


ETAPPEN = [
    {'lernziel': 'grundbegriffe', 'titel': 'Knoten, Kanten und Grad',
     'regel': 'Ein ⟦Graph⟧ (graph) besteht aus ⟦Knoten⟧ (vertices, Punkte) und ⟦Kanten⟧ (edges, Verbindungslinien). Der ⟦Grad⟧ (degree) eines Knotens ist die Anzahl der Kanten, die ⟦an ihm enden⟧. Weil jede Kante zwei Enden hat, gilt: ⟦Summe aller Grade = 2 · Anzahl der Kanten⟧.',
     'schritte': ['Graph mit Knoten A, B, C, D und Kanten AB, AC, BC, CD.', 'Grade: A 2, B 2, C 3, D 1.', 'Summe 2 + 2 + 3 + 1 = 8 = 2 · ⟦4 Kanten⟧.'],
     'probe': 'Jede Kante wurde an beiden Enden gezählt ✓',
     'bild': netz({'A': (0, 0), 'B': (4, 0), 'C': (2, -3), 'D': (6, -3)}, [('A', 'B', ''), ('A', 'C', ''), ('B', 'C', ''), ('C', 'D', '')]),
     'fehler': 'Die Summe der Grade (8) als Anzahl der Kanten anzugeben ist falsch: Jede Kante wird ⟦an beiden Enden⟧ gezählt, also 8 : 2 = 4 Kanten.'},
    {'lernziel': 'euler', 'titel': 'Alle Kanten genau einmal',
     'regel': 'Ein ⟦Eulerweg⟧ (Eulerian trail) benutzt jede Kante genau einmal. Endet er am Start, heißt er ⟦Eulerkreis⟧ (Eulerian circuit). Bei einem zusammenhängenden Graphen gilt: ⟦alle Grade gerade⟧ → Eulerkreis; ⟦genau zwei ungerade⟧ → Eulerweg von einem ungeraden zum anderen ungeraden Knoten; sonst keiner.',
     'schritte': ['Grade: A 2, B 3, C 4, D 3.', 'Genau zwei ungerade Knoten (B und D).', '⟦Eulerweg möglich⟧, Start in B, Ende in D (oder umgekehrt), aber kein Eulerkreis.'],
     'probe': 'Wer an einem Knoten ankommt, muss ihn wieder verlassen – nur Start und Ende dürfen ungerade sein ✓',
     'fehler': 'Bei vier ungeraden Knoten einen Eulerweg zu suchen ist zwecklos: An jedem ungeraden Knoten, der nicht Start oder Ende ist, ⟦bleibt eine Kante übrig⟧.'},
    {'lernziel': 'kuerzester', 'titel': 'Kürzeste Wege finden',
     'regel': 'In einem ⟦gewichteten Graphen⟧ (weighted graph) stehen an den Kanten Längen, Zeiten oder Kosten. Für den ⟦kürzesten Weg⟧ (shortest path) gehst du vom Start aus und notierst an jedem Knoten die ⟦kleinste bisher bekannte Entfernung⟧ (Dijkstra-Idee). Ein Umweg kann kürzer sein als die direkte Kante.',
     'schritte': ['A–B: 7, A–C: 2, C–B: 3.', 'Direkt A → B: 7. Über C: 2 + 3 = 5.', 'Kürzester Weg ⟦A → C → B mit Länge 5⟧.'],
     'probe': 'Alle Möglichkeiten verglichen: 5 < 7 ✓',
     'bild': netz({'A': (0, 0), 'B': (6, 0), 'C': (3, -3)}, [('A', 'B', '7'), ('A', 'C', '2'), ('C', 'B', '3')]),
     'fehler': 'Immer die ⟦direkte Kante⟧ zu nehmen ist falsch: Hier ist A–B (7) länger als der Umweg über C (5).'},
    {'lernziel': 'spannbaum', 'titel': 'Minimaler Spannbaum',
     'regel': 'Ein ⟦Baum⟧ (tree) ist ein zusammenhängender Graph ⟦ohne Kreis⟧; mit n Knoten hat er ⟦n − 1 Kanten⟧. Ein ⟦minimaler Spannbaum⟧ (minimum spanning tree) verbindet alle Knoten mit ⟦kleinstem Gesamtgewicht⟧. Kruskal: Kanten der Größe nach nehmen und jede ⟦überspringen, die einen Kreis schließen würde⟧.',
     'schritte': ['Kanten: AB 4, BC 2, AC 3, CD 5, BD 6.', 'Nimm BC (2), AC (3); AB (4) würde Kreis A–B–C schließen → weglassen; CD (5) nehmen.', 'Gewicht 2 + 3 + 5 = ⟦10⟧ mit 3 Kanten für 4 Knoten.'],
     'probe': '4 Knoten → 3 Kanten ✓',
     'bild': netz({'A': (0, 0), 'B': (4, 0), 'C': (2, -3), 'D': (6, -3)}, [('A', 'B', '4'), ('B', 'C', '2'), ('A', 'C', '3'), ('C', 'D', '5'), ('B', 'D', '6')]),
     'fehler': 'Einfach die n − 1 kleinsten Kanten (2, 3, 4) zu nehmen ist falsch: Sie bilden den Kreis A–B–C, und D bleibt unverbunden. Kanten, die einen ⟦Kreis schließen⟧, werden übersprungen.'},
    {'lernziel': 'verstehen', 'titel': 'Aussagen über Graphen prüfen',
     'regel': 'Wichtige Tatsachen: Die ⟦Anzahl der Knoten mit ungeradem Grad ist immer gerade⟧ (wegen Summe der Grade = 2 · Kanten). Ein Baum mit n Knoten hat ⟦genau n − 1 Kanten⟧. Mit einer Gradliste kann man prüfen, ob ein Graph überhaupt möglich ist.',
     'schritte': ['Gibt es einen Graphen mit den Graden 3, 3, 3?', 'Summe 9 ist ungerade, müsste aber 2 · Kanten (gerade) sein. ⟦Unmöglich⟧.'],
     'probe': 'Drei ungerade Knoten – ungerade Anzahl, also nicht möglich ✓',
     'fehler': '„Ein Graph mit 5 Knoten und 4 Kanten ist immer ein Baum“ ist falsch: Er könnte einen Kreis enthalten und dafür ⟦nicht zusammenhängend⟧ sein.'},
]


def g_grundbegriffe(s):
    g = zufallsgraph(6, 10)
    if not g: return None
    kn, ka = g
    gr = grad(kn, ka)
    bi = bild(kn, ka)
    art = R.choice({1: ['kanten', 'grad', 'knoten'], 2: ['grad', 'summe', 'max', 'ungerade'], 3: ['handschlag', 'matrix', 'handschlag_r']}[s])
    if art == 'kanten':
        return mit_grafik(zahl('Wie viele Kanten hat der Graph?', f'Kanten: {", ".join(u + v for u, v in ka)} – das sind {len(ka)}.', 'Zähle die Verbindungslinien.', len(ka), f'{len(ka)}'), bi)
    if art == 'knoten':
        return mit_grafik(zahl('Wie viele Knoten hat der Graph?',
                               f'Knoten: {", ".join(kn)} – das sind {len(kn)}.', 'Zähle die beschrifteten Punkte.', len(kn), f'{len(kn)}'), bi)
    if art == 'grad':
        k = R.choice(kn)
        return mit_grafik(zahl(f'Welchen Grad hat der Knoten {k}?', f'An {k} enden die Kanten {", ".join(u + v for u, v in ka if k in (u, v))}: Grad {gr[k]}.',
                               'Zähle die Linien, die an diesem Punkt enden.', gr[k], f'{gr[k]}'), bi)
    if art == 'summe':
        return mit_grafik(zahl('Wie groß ist die Summe aller Grade?', f'Grade: {", ".join(f"{k} {gr[k]}" for k in kn)}. Summe {sum(gr.values())} = 2 · {len(ka)} Kanten.',
                               'Tipp: Summe der Grade = 2 · Anzahl der Kanten.', sum(gr.values()), f'2 * {len(ka)}'), bi)
    if art == 'max':
        mx = max(gr.values())
        if list(gr.values()).count(mx) > 1: return None
        k = max(gr, key=gr.get)
        return mit_grafik(auswahl('Welcher Knoten hat den größten Grad?', k, [x for x in kn if x != k][:3] if len(kn) > 3 else kn,
                                  f'Grade: {", ".join(f"{x} {gr[x]}" for x in kn)}. Am größten: {k} mit {mx}.', 'Bestimme für jeden Knoten den Grad.'), bi)
    if art == 'ungerade':
        u = sum(1 for v in gr.values() if v % 2)
        return mit_grafik(zahl('Wie viele Knoten haben einen ungeraden Grad?', f'Grade: {", ".join(f"{x} {gr[x]}" for x in kn)}. Ungerade: {u}.',
                               'Bestimme alle Grade und zähle die ungeraden.', u, f'{u}'), bi)
    if art == 'handschlag':
        n = R.randint(5, 12)
        gr_ = R.randint(2, n - 1)
        if n * gr_ % 2: return None
        return zahl(f'In einem Graphen hat jeder der {n} Knoten den Grad {gr_}. Wie viele Kanten hat der Graph?', f'Summe der Grade: {n} · {gr_} = {n * gr_}. Kanten: {n * gr_} : 2 = {n * gr_ // 2}.',
                    'Summe der Grade = 2 · Anzahl der Kanten.', n * gr_ // 2, f'{n} * {gr_} / 2')
    if art == 'handschlag_r':
        n = R.randint(4, 12)
        return zahl(f'{n} Personen geben sich gegenseitig je einmal die Hand. Wie viele Handschläge gibt es? (Jede Person ist ein Knoten, jeder Handschlag eine Kante.)',
                    f'Jeder Knoten hat Grad {n - 1}. Summe {n} · {n - 1} = {n * (n - 1)}; Kanten: {n * (n - 1)} : 2 = {n * (n - 1) // 2}.',
                    'Jede Person schüttelt allen anderen die Hand.', n * (n - 1) // 2, f'{n} * ({n} - 1) / 2')
    # Adjazenzmatrix als Tabelle
    tab = tabelle([''] + kn, [[k] + [1 if (min(k, j), max(k, j)) in ka else 0 for j in kn] for k in kn])
    k = R.choice(kn)
    return mit_grafik(zahl(f'Die Tabelle (Adjazenzmatrix, adjacency matrix) zeigt mit 1, welche Knoten durch eine Kante verbunden sind. Welchen Grad hat {k}?',
                           f'In der Zeile {k} stehen {gr[k]} Einsen: Grad {gr[k]}.', 'Zähle die Einsen in der Zeile des Knotens.', gr[k], f'{gr[k]}'), tab)


def g_euler(s):
    g = zufallsgraph(6, 11)
    if not g: return None
    kn, ka = g
    gr = grad(kn, ka)
    ung = [k for k in kn if gr[k] % 2]
    art = R.choice({1: ['art', 'art'], 2: ['art', 'start', 'ungerade'], 3: ['art', 'start', 'ergaenzen', 'koenigsberg']}[s])
    erg = 'Eulerkreis' if not ung else ('Eulerweg, aber kein Eulerkreis' if len(ung) == 2 else 'weder Eulerweg noch Eulerkreis')
    w_grad = f'Grade: {", ".join(f"{k} {gr[k]}" for k in kn)}. Ungerade: {len(ung)}' + (f' ({", ".join(ung)})' if ung else '') + '.'
    if art == 'art':
        if s == 1 and len(ung) not in (0, 2): return None
        return mit_grafik(auswahl('Hat der Graph einen Eulerweg oder einen Eulerkreis?', erg, ['Eulerkreis', 'Eulerweg, aber kein Eulerkreis', 'weder Eulerweg noch Eulerkreis'],
                                  w_grad + f' Also: {erg}.', 'Bestimme alle Grade und zähle die ungeraden.'), bild(kn, ka))
    if art == 'ungerade':
        return mit_grafik(zahl('Wie viele Knoten mit ungeradem Grad hat der Graph?', w_grad, 'Bestimme jeden Grad.', len(ung), f'{len(ung)}'), bild(kn, ka))
    if art == 'start':
        if len(ung) != 2: return None
        r = f'in {ung[0]} oder in {ung[1]}'
        andere = [k for k in kn if k not in ung]
        return mit_grafik(auswahl('Der Graph hat einen Eulerweg. Wo muss er beginnen?', r,
                                  [f'in {andere[0]} oder in {andere[1]}', f'in jedem beliebigen Knoten', f'nur in {andere[0]}'],
                                  w_grad + ' Ein Eulerweg beginnt und endet an den beiden ungeraden Knoten.', 'Start und Ende sind die Knoten mit ungeradem Grad.'), bild(kn, ka))
    if art == 'ergaenzen':
        if len(ung) != 2: return None
        u, v = ung
        return mit_grafik(auswahl(f'Der Graph hat einen Eulerweg, aber keinen Eulerkreis. Welche zusätzliche Kante macht daraus einen Graphen mit Eulerkreis?',
                                  f'eine Kante {u}{v}', [f'eine Kante {a}{b}' for a, b in itertools.combinations([k for k in kn if k not in ung][:3], 2)][:3],
                                  f'Die ungeraden Knoten sind {u} und {v}. Eine Kante {u}{v} macht beide gerade: Dann haben alle Knoten geraden Grad.',
                                  'Welche Knoten müssen einen Grad mehr bekommen?'), bild(kn, ka))
    r = 'Nein: Alle vier Ufer- und Inselknoten haben einen ungeraden Grad.'
    return auswahl('Königsberger Brückenproblem: Zwei Ufer und zwei Inseln sind durch 7 Brücken verbunden; die Grade der vier Landstücke sind 3, 3, 3 und 5. Gibt es einen Spaziergang, der jede Brücke genau einmal benutzt?', r,
                   ['Ja, wenn man auf einer Insel startet.', 'Ja, weil 7 Brücken eine ungerade Zahl sind.', 'Nein, weil es mehr als 6 Brücken sind.'],
                   'Für einen Eulerweg dürfen höchstens zwei Knoten ungerade sein. Hier sind es vier. (Leonhard Euler, 1736)', 'Zähle die Knoten mit ungeradem Grad.')


def g_kuerzester(s):
    g = zufallsgraph(7, 10)
    if not g: return None
    kn, ka = g
    gew = {e: R.randint(1, 9) for e in ka}
    st = 'A'
    dist, vor = dijkstra(kn, ka, gew, st)
    ziel = R.choice([k for k in kn if k != st and len(alle_wege(kn, ka, gew, st, k)) > 1])
    wege = sorted(alle_wege(kn, ka, gew, st, ziel))
    if len(wege) < 2 or wege[0][0] == wege[1][0]: return None
    best = wege[0]
    bi = bild(kn, ka, gew)
    weg_txt = lambda w: ' → '.join(w)  # noqa: E731
    art = R.choice({1: ['laenge', 'laenge'], 2: ['laenge', 'weg', 'weg'], 3: ['weg', 'umweg', 'laenge']}[s])  # Durchsicht 19
    if s == 1 and len(best[1]) > 4: return None
    if art == 'laenge':
        return mit_grafik(zahl(f'Die Zahlen an den Kanten sind Fahrzeiten in Minuten. Wie lange dauert der schnellste Weg von {st} nach {ziel}?',
                               f'Schnellster Weg: {weg_txt(best[1])} mit {best[0]} Minuten' + (f' (zweitbester: {weg_txt(wege[1][1])} mit {wege[1][0]}).' if len(wege) > 1 else '.'),
                               'Vergleiche mehrere Wege. Notiere an jedem Knoten die kleinste Zeit vom Start.', best[0], ' + '.join(str(gew[tuple(sorted((best[1][i], best[1][i + 1])))]) for i in range(len(best[1]) - 1)),
                               einheit='min'), bi)
    if art == 'weg':
        falsch = [weg_txt(w) for _, w in wege[1:4]]
        if len(falsch) < 2: return None
        return mit_grafik(auswahl(f'Welcher Weg von {st} nach {ziel} ist am kürzesten (Kantenzahlen = Längen in km)?', weg_txt(best[1]), falsch,
                                  f'{weg_txt(best[1])}: {best[0]} km. Andere: ' + '; '.join(f'{weg_txt(w)}: {d} km' for d, w in wege[1:4]) + '.',
                                  'Rechne für jeden Weg die Summe der Kantenzahlen aus.'), bi)
    direkt = (min(st, ziel), max(st, ziel))
    if direkt not in gew or best[1] == [st, ziel]: return None
    return mit_grafik(zahl(f'Zwischen {st} und {ziel} gibt es eine direkte Kante mit Länge {gew[direkt]}. Um wie viel ist der kürzeste Weg kürzer als diese direkte Kante?',
                           f'Kürzester Weg {weg_txt(best[1])}: {best[0]}. Unterschied: {gew[direkt]} − {best[0]} = {gew[direkt] - best[0]}.',
                           'Ein Umweg kann kürzer sein – suche den kürzesten Weg.', gew[direkt] - best[0], f'{gew[direkt]} - {best[0]}'), bi)


def g_spannbaum(s):
    art = R.choice({1: ['kanten_n', 'gewicht', 'erste'], 2: ['ersparnis', 'ausgelassen'], 3: ['gewicht', 'ausgelassen', 'ersparnis']}[s])  # Durchsicht 19: Stufe 2 = Ersparnis, übersprungene Kante
    if art == 'kanten_n':
        n = R.randint(5, 30)
        return zahl(f'Ein Spannbaum verbindet {n} Knoten. Wie viele Kanten hat er?', f'Ein Baum mit n Knoten hat n − 1 Kanten: {n} − 1 = {n - 1}.',
                    'Jede neue Kante verbindet genau einen neuen Knoten.', n - 1, f'{n} - 1')
    g = zufallsgraph(7, 10)
    if not g: return None
    kn, ka = g
    ws = R.sample(range(1, 15), len(ka))
    gew = dict(zip(ka, ws))
    baum = kruskal(kn, ka, gew)
    W = sum(gew[e] for e in baum)
    bi = bild(kn, ka, gew)
    if art == 'gewicht':
        return mit_grafik(zahl('Die Zahlen sind Kosten (in Tausend €) für Leitungen zwischen Häusern. Alle Häuser sollen möglichst günstig verbunden werden. Wie hoch sind die Kosten des minimalen Spannbaums?',
                               f'Kruskal: {", ".join(f"{u}{v} ({gew[(u, v)]})" for u, v in sorted(baum, key=lambda e: gew[e]))}. Summe: {W}.',
                               f'Kanten nach Größe sortieren; jede nehmen, die keinen Kreis schließt, bis {len(kn) - 1} Kanten da sind.', W,
                               ' + '.join(str(gew[e]) for e in baum)), bi)
    if art == 'erste':
        e = min(ka, key=lambda e: gew[e])
        return mit_grafik(auswahl('Mit welcher Kante beginnt das Kruskal-Verfahren?', f'{e[0]}{e[1]}', [f'{u}{v}' for u, v in R.sample([x for x in ka if x != e], 3)],
                                  f'Kruskal beginnt mit der leichtesten Kante: {e[0]}{e[1]} mit {gew[e]}.', 'Welche Kante hat das kleinste Gewicht?'), bi)
    if art == 'ausgelassen':
        sortiert = sorted(ka, key=lambda e: gew[e])
        weg = [e for e in sortiert if e not in baum]
        if not weg: return None
        e = weg[0]
        r = f'{e[0]}{e[1]}'
        return mit_grafik(auswahl('Welche Kante überspringt Kruskal als erste, weil sie einen Kreis schließen würde?', r,
                                  [f'{u}{v}' for u, v in R.sample([x for x in baum], min(3, len(baum)))],
                                  f'Reihenfolge: {", ".join(f"{u}{v} ({gew[(u, v)]})" for u, v in sortiert)}. {e[0]}{e[1]} ({gew[e]}) würde einen Kreis schließen.',
                                  'Gehe die Kanten nach Größe durch und prüfe jedes Mal: Sind die beiden Enden schon verbunden?'), bi)
    alle = sum(gew.values())
    return mit_grafik(zahl('Statt alle Leitungen zu bauen, baut man nur den minimalen Spannbaum (Zahlen = Kosten in Tausend €). Wie viel spart man?',
                           f'Alle Kanten: {alle}. Spannbaum: {W}. Ersparnis: {alle} − {W} = {alle - W}.', 'Bestimme erst den minimalen Spannbaum.', alle - W, f'{alle} - {W}'), bi)


def g_verstehen(s):
    art = R.choice({1: ['moeglich', 'baum_kanten'], 2: ['ungerade_anzahl', 'baum_kreis', 'moeglich'], 3: ['moeglich', 'baum_kreis', 'fehler_euler', 'ungerade_anzahl']}[s])
    if art == 'moeglich':
        n = R.randint(4, 6)
        grade = sorted((R.randint(1, 4) for _ in range(n)), reverse=True)
        if max(grade) >= n: return None
        ok = sum(grade) % 2 == 0
        if ok and not graphisch(grade): return None
        return ja_nein(f'Kann es einen Graphen (ohne Mehrfachkanten und Schleifen) mit den Graden {", ".join(map(str, grade))} geben?',
                       ok, f'Summe {sum(grade)} ist ' + ('gerade, und ein solcher Graph lässt sich tatsächlich zeichnen.' if ok else 'ungerade, müsste aber 2 · Kanten sein: unmöglich.'),
                       'Prüfe zuerst die Summe aller Grade.')
    if art == 'baum_kanten':
        n = R.randint(4, 15)
        return zahl(f'Ein Baum hat {n} Kanten. Wie viele Knoten hat er?', f'Knoten = Kanten + 1 = {n + 1}.', 'Bei einem Baum gilt: Kanten = Knoten − 1.', n + 1, f'{n} + 1')
    if art == 'ungerade_anzahl':
        k = R.choice([1, 3, 5])
        return ja_nein(f'Kann ein Graph genau {k} Knoten mit ungeradem Grad haben?', False,
                       f'Die Summe aller Grade ist gerade. Mit {k} ungeraden Summanden (und sonst geraden) wäre sie ungerade – unmöglich.', 'Was weißt du über die Summe aller Grade?')
    if art == 'baum_kreis':
        n = R.randint(5, 10)
        r = f'Nein – es hat {n} Kanten, ein Baum mit {n} Knoten hat aber nur {n - 1}.'
        return auswahl(f'Ein Straßennetz verbindet {n} Orte zusammenhängend mit {n} Straßen. Ist es ein Baum?', r,
                       ['Ja – es ist zusammenhängend.', f'Ja – {n} Straßen für {n} Orte ist genau richtig.', 'Das hängt von den Längen der Straßen ab.'],
                       f'Ein zusammenhängender Graph mit n Knoten und mehr als n − 1 Kanten enthält einen Kreis.', 'Wie viele Kanten hat ein Baum mit n Knoten?')
    r = 'Falsch: Mit genau zwei ungeraden Knoten gibt es einen Eulerweg, aber keinen Eulerkreis.'
    return auswahl('Kim sagt: „Mein Graph ist zusammenhängend und hat genau zwei Knoten mit ungeradem Grad, also gibt es einen Eulerkreis.“ Stimmt das?', r,
                   ['Richtig.', 'Falsch: Es gibt dann gar keinen Eulerweg.', 'Falsch: Man braucht dafür genau vier ungerade Knoten.'],
                   'Eulerkreis: alle Grade gerade. Zwei ungerade Knoten: nur ein Eulerweg von einem zum anderen.', 'Wie war die Regel für Eulerkreis und Eulerweg?')


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-2) ----------
# Prüfungsvorbilder: IB MYP (Verlagsinhalt Graphentheorie: Handschlag-Aufgaben, Adjazenzmatrix, Königsberg/„Haus vom Nikolaus“,
# kürzeste Wege mit Sperrung oder Zwischenhalt, Kruskal), Wettbewerbe (Känguru: Gradfolgen, Kantenzahl). Eigene Zahlen.
def grund3(art):
    # fehlender_grad
    m = R.randint(6, 12)
    for _ in range(100):
        grade = [R.randint(1, 4) for _ in range(R.randint(4, 6))]
        rest = 2 * m - sum(grade)
        if 1 <= rest <= 4 and graphisch(grade + [rest]): break
    else:
        return None
    return zahl(f'Ein Graph hat {m} Kanten und {len(grade) + 1} Knoten. {len(grade)} Knoten haben die Grade {", ".join(map(str, grade))}. Welchen Grad hat der letzte Knoten?',
                f'Summe aller Grade = 2 · {m} = {2 * m}. Bekannt: {" + ".join(map(str, grade))} = {sum(grade)}. Letzter Grad: {2 * m} − {sum(grade)} = {rest}.',
                'Wie groß muss die Summe aller Grade sein?', rest, f'2 * {m} - {sum(grade)}')


def euler3(art):
    if art == 'nikolaus':
        r = 'Ja, aber nur, wenn man unten links oder unten rechts anfängt.'
        bi = netz({'A': (0, 0), 'B': (4, 0), 'C': (4, 4), 'D': (0, 4), 'E': (2, 6.5)},
                  [('A', 'B', ''), ('B', 'C', ''), ('C', 'D', ''), ('D', 'A', ''), ('A', 'C', ''), ('B', 'D', ''), ('C', 'E', ''), ('D', 'E', '')])
        return mit_grafik(auswahl('„Das ist das Haus vom Ni-ko-laus“: Kann man die Figur in einem Zug zeichnen, ohne eine Linie doppelt zu ziehen?', r,
                                  ['Ja, von jeder Ecke aus.', 'Nein, das geht nicht.', 'Ja, aber nur, wenn man an der Dachspitze anfängt.'],
                                  'Grade: A 3, B 3, C 4, D 4, E 2. Genau zwei ungerade Knoten (A und B): Es gibt einen Eulerweg, der in A oder B beginnt und im anderen endet.',
                                  'Bestimme die Grade der fünf Ecken.'), bi)
    # wie_viele_neu
    k = R.choice([4, 6, 8])
    return zahl(f'Ein zusammenhängender Graph hat genau {k} Knoten mit ungeradem Grad. Wie viele Kanten muss man mindestens hinzufügen, damit ein Eulerkreis möglich wird?',
                f'Jede neue Kante macht höchstens zwei ungerade Knoten gerade. Für {k} ungerade Knoten braucht man mindestens {k} : 2 = {k // 2} Kanten (je zwei ungerade Knoten verbinden).',
                'Wie viele ungerade Knoten kann eine neue Kante „reparieren“?', k // 2, f'{k} / 2')


def kurz3(art):
    g = zufallsgraph(8, 11)
    if not g: return None
    kn, ka = g
    gew = {e: R.randint(1, 9) for e in ka}
    bi = bild(kn, ka, gew)
    dist, _ = dijkstra(kn, ka, gew, 'A')
    if art == 'sperrung':
        ziel = R.choice([k for k in kn if k != 'A'])
        wege = sorted(alle_wege(kn, ka, gew, 'A', ziel))
        if len(wege) < 2 or len(wege[0][1]) < 3 or wege[0][0] == wege[1][0]: return None
        w = wege[0][1]
        e = tuple(sorted((w[1], w[2])))
        rest = [x for x in wege if not any(tuple(sorted((x[1][i], x[1][i + 1]))) == e for i in range(len(x[1]) - 1))]
        if not rest: return None
        neu = rest[0]
        return mit_grafik(zahl(f'Die Zahlen sind Fahrzeiten in Minuten. Die Straße {e[0]}–{e[1]} ist gesperrt. Wie lange dauert jetzt der schnellste Weg von A nach {ziel}?',
                               f'Ohne Sperrung: {" → ".join(w)} mit {wege[0][0]} min. Er benutzt {e[0]}–{e[1]}. Bester Weg ohne diese Straße: {" → ".join(neu[1])} mit {neu[0]} min.',
                               'Streiche die gesperrte Kante und suche dann den schnellsten Weg.', neu[0], f'{neu[0]}', einheit='min'), bi)
    if art == 'zwischenhalt':
        ziel, h = R.sample([k for k in kn if k != 'A'], 2)
        d2, _ = dijkstra(kn, ka, gew, h)
        gesamt = dist[h] + d2[ziel]
        if gesamt == dist[ziel]: return None
        return mit_grafik(zahl(f'Die Zahlen sind Fahrzeiten in Minuten. Ein Bus muss von A nach {ziel} und unterwegs in {h} halten. Wie lange dauert die schnellste Fahrt?',
                               f'Schnellster Weg A → {h}: {dist[h]} min. Schnellster Weg {h} → {ziel}: {d2[ziel]} min. Zusammen {gesamt} min (ohne Halt wären es {dist[ziel]} min).',
                               f'Teile die Fahrt in zwei Teile: A bis {h} und {h} bis {ziel}.', gesamt, f'{dist[h]} + {d2[ziel]}', einheit='min'), bi)
    # erreichbar
    T = R.randint(6, 12)
    k = sum(1 for x in kn if x != 'A' and dist[x] <= T)
    if k in (0, len(kn) - 1): return None
    return mit_grafik(zahl(f'Die Zahlen sind Fahrzeiten in Minuten. Wie viele Orte (außer A) erreicht man von A aus in höchstens {T} Minuten?',
                           'Schnellste Zeiten ab A: ' + ', '.join(f'{x} {dist[x]}' for x in kn if x != 'A') + f'. Höchstens {T} min: {k} Orte.',
                           'Bestimme für jeden Ort die schnellste Zeit ab A (Dijkstra-Idee).', k, f'{k}'), bi)


def span3(art):
    g = zufallsgraph(7, 10)
    if not g: return None
    kn, ka = g
    gr = grad(kn, ka)
    if art == 'pflichtkante':
        blatt = [k for k in kn if gr[k] == 1]
        if not blatt: return None
        b = blatt[0]
        e = next(x for x in ka if b in x)
        ws = R.sample(range(1, 15), len(ka))
        gew = dict(zip(ka, ws))
        gew[e] = max(w for x, w in gew.items() if x != e) + 1  # wirklich die teuerste Leitung
        return mit_grafik(auswahl(f'Haus {b} ist nur über die Leitung {e[0]}{e[1]} erreichbar. Sie ist die teuerste Leitung ({gew[e]}). Gehört sie zum minimalen Spannbaum?',
                                  'Ja, sonst wäre Haus ' + b + ' nicht angeschlossen.', ['Nein, Kruskal nimmt die teuerste Kante nie.', 'Nur wenn sie keinen Kreis schließt – das kann man nicht wissen.', 'Nein, man nimmt immer nur die n − 1 billigsten Kanten.'],
                                  f'Ein Spannbaum verbindet alle Knoten. {b} hat nur eine Kante – ohne sie bliebe {b} allein. Sie kann auch keinen Kreis schließen, weil {b} sonst unverbunden ist.',
                                  'Was muss ein Spannbaum auf jeden Fall leisten?'), bild(kn, ka, gew))
    if art == 'neue_leitung':
        mit_g = 'G' in kn
        kand = [e for e in (MIT_G if mit_g else OHNE_G) if tuple(sorted(e)) not in ka]
        if not kand: return None
        ws = R.sample(range(3, 16), len(ka))
        gew = dict(zip(ka, ws))
        alt = sum(gew[e] for e in kruskal(kn, ka, gew))
        e = tuple(sorted(R.choice(kand)))
        k = R.randint(1, 4)
        gew2 = dict(gew); gew2[e] = k
        neu = sum(gew2[x] for x in kruskal(kn, ka + [e], gew2))
        if neu >= alt: return None
        bi = bild(kn, ka, gew)
        bi['linien'].append([e[0], e[1], f'{k} neu', 'gestrichelt'])
        return mit_grafik(zahl(f'Die Zahlen sind Kosten in Tausend €. Eine neue Leitung {e[0]}{e[1]} (gestrichelt) würde {k} kosten. Um wie viel wird der minimale Spannbaum billiger, wenn man sie zulässt?',
                               f'Ohne neue Leitung: {alt}. Mit ihr: {neu} (Kruskal neu durchführen). Ersparnis: {alt} − {neu} = {alt - neu}.',
                               'Führe Kruskal zweimal durch: ohne und mit der neuen Leitung.', alt - neu, f'{alt} - {neu}'), bi)
    # teuerste im Baum
    ws = R.sample(range(1, 15), len(ka))
    gew = dict(zip(ka, ws))
    baum = kruskal(kn, ka, gew)
    e = max(baum, key=lambda x: gew[x])
    return mit_grafik(zahl('Die Zahlen sind Kosten in Tausend €. Wie teuer ist die teuerste Leitung, die im minimalen Spannbaum vorkommt?',
                           f'Kruskal: {", ".join(f"{u}{v} ({gew[(u, v)]})" for u, v in sorted(baum, key=lambda x: gew[x]))}. Die letzte genommene Leitung ist {e[0]}{e[1]} mit {gew[e]}.',
                           'Führe Kruskal durch: Die zuletzt genommene Kante ist die teuerste im Baum.', gew[e], f'{gew[e]}'), bild(kn, ka, gew))


def verst3(art):
    if art == 'max_kanten':
        n = R.randint(4, 10)
        return zahl(f'Wie viele Kanten kann ein Graph mit {n} Knoten höchstens haben (ohne Mehrfachkanten und Schleifen)?',
                    f'Jeder Knoten ist mit jedem anderen verbunden: Grad {n - 1}. Kanten: {n} · {n - 1} : 2 = {n * (n - 1) // 2}.',
                    'Wie viele Nachbarn kann ein Knoten höchstens haben?', n * (n - 1) // 2, f'{n} * ({n} - 1) / 2')
    # gerade_reicht_nicht: Summe gerade, aber trotzdem unmöglich (Havel-Hakimi)
    for _ in range(200):
        n = R.randint(4, 6)
        grade = sorted((R.randint(1, n - 1) for _ in range(n)), reverse=True)
        if sum(grade) % 2 == 0 and not graphisch(grade): break
    else:
        return None
    return ja_nein(f'Die Summe der Grade {", ".join(map(str, grade))} ist gerade. Gibt es einen Graphen (ohne Mehrfachkanten und Schleifen) mit genau diesen {n} Graden?', False,
                   f'Die gerade Summe ist nötig, aber nicht genug. Die {grade.count(n - 1)} Knoten mit Grad {n - 1} müssten mit allen anderen verbunden sein. Dann hätte jeder andere Knoten schon mindestens Grad {grade.count(n - 1)} – '
                   f'der kleinste Grad {grade[-1]} ist aber kleiner.' if grade[-1] < grade.count(n - 1) else
                   f'Die gerade Summe ist nötig, aber nicht genug. Versucht man die Kanten zu verteilen (größter Grad zuerst), bleibt ein Knoten mit zu vielen offenen Kanten übrig.',
                   'Eine gerade Summe reicht nicht immer. Prüfe, ob die großen Grade überhaupt genug Partner finden.')


def _filter(g, s, teil, nicht=False):
    for _ in range(120):
        t = g(s)
        if t and ((teil in t['f']['text']) != nicht): return t
    return None


def g2_grundbegriffe(s):
    if s < 3: return g_grundbegriffe(s)
    art = art3('handschlag_r', 'matrix', 'handschlag', ['handschlag_r', 'matrix', 'fehlender_grad', 'handschlag', 'fehlender_grad'])
    if art == 'fehlender_grad': return grund3(art)
    teil = {'handschlag_r': 'Hand', 'matrix': 'Adjazenzmatrix', 'handschlag': 'jeder der'}[art]
    return _filter(g_grundbegriffe, 3, teil)


def g2_euler(s):
    if s == 1: return g_euler(1)
    if s == 2:  # Stufe 2: Anzahl ungerader Knoten, Startknoten, Art mit beliebig vielen ungeraden Knoten
        return g_euler(2)
    art = art3('koenigsberg', 'nikolaus', 'ergaenzen', ['ergaenzen', 'wie_viele_neu', 'ergaenzen', 'wie_viele_neu', 'ergaenzen'])
    if art == 'koenigsberg': return _filter(g_euler, 3, 'Königsberg')
    if art == 'ergaenzen': return _filter(g_euler, 3, 'zusätzliche Kante')
    return euler3(art)


def g2_kuerzester(s):
    if s < 3: return g_kuerzester(s)
    art = art3('sperrung', 'zwischenhalt', 'erreichbar', ['umweg', 'sperrung', 'zwischenhalt', 'erreichbar', 'umweg'])
    if art == 'umweg': return _filter(g_kuerzester, 3, 'direkte Kante')
    return kurz3(art)


def g2_spannbaum(s):
    if s < 3: return g_spannbaum(s)
    art = art3('teuerste', 'neue_leitung', 'pflichtkante', ['teuerste', 'neue_leitung', 'pflichtkante', 'teuerste', 'neue_leitung'])
    return span3(art)


def g2_verstehen(s):
    if s < 3: return g_verstehen(s)
    art = art3('fehler_euler', 'max_kanten', 'gerade_reicht_nicht', ['baum_kreis', 'max_kanten', 'gerade_reicht_nicht', 'max_kanten', 'gerade_reicht_nicht'])
    if art == 'fehler_euler': return _filter(g_verstehen, 3, 'Kim')
    if art == 'baum_kreis': return _filter(g_verstehen, 3, 'Straßennetz')
    return verst3(art)


GEN = {'grundbegriffe': g2_grundbegriffe, 'euler': g2_euler, 'kuerzester': g2_kuerzester, 'spannbaum': g2_spannbaum, 'verstehen': g2_verstehen}

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

_P4 = {'A': [0, 0], 'B': [4, 0], 'C': [2, -3], 'D': [6, -3]}
_P5 = {'A': [0, 0], 'B': [4, 0], 'C': [2, -3], 'D': [6, -3], 'E': [4, -6]}
_P3 = {'A': [0, 0], 'B': [6, 0], 'C': [3, -3]}


def _fig(punkte, linien, namen=None):
    """Graph als figur; namen = {Knoten: neuer Name} (z. B. mit Grad)."""
    namen = namen or {}
    p = {namen.get(k, k): v for k, v in punkte.items()}
    li = [[namen.get(l[0], l[0]), namen.get(l[1], l[1]), *l[2:]] for l in linien]
    return {'typ': 'figur', 'punkte': p, 'linien': li}


def _g(*ks):
    return {k: f'{k}: {g}' for k, g in zip('ABCDE', ks)}


_L4 = [['A', 'B'], ['A', 'C'], ['B', 'C'], ['C', 'D']]
_L5 = [['A', 'B'], ['A', 'C'], ['B', 'C'], ['B', 'D'], ['C', 'D'], ['C', 'E'], ['D', 'E']]
_EU = [['B', 'A', '1'], ['A', 'C', '2'], ['C', 'B', '3'], ['B', 'D', '4'], ['D', 'C', '5'], ['C', 'E', '6'], ['E', 'D', '7']]


def _k3(ab, ac, cb):
    return _fig(_P3, [['A', 'B', '7', *ab], ['A', 'C', '2', *ac], ['C', 'B', '3', *cb]])




def _sb(fest):
    kanten = [['A', 'B', '4'], ['B', 'C', '2'], ['A', 'C', '3'], ['C', 'D', '5'], ['B', 'D', '6']]
    return _fig(_P4, [k if k[0] + k[1] in fest else k + ['gestrichelt'] for k in kanten])


UMBAU = {
    'grundbegriffe': {
        'einstieg': 'Vier Dörfer A, B, C, D sind durch Straßen verbunden. Auf einer Karte zeichnet man Dörfer als Punkte und Straßen als Linien. '
                    'So ein Bild heißt ⟦Graph⟧.',
        'woerter': [['Knoten', 'ein Punkt im Graphen, hier ein Dorf'],
                    ['Kante', 'eine Linie zwischen zwei Knoten, hier eine Straße'],
                    ['Grad', 'wie viele Kanten an einem Knoten enden']],
        'bild': _fig(_P4, _L4),
        'schritte': [
            {'text': 'Die Kanten sind AB, AC, BC und CD.'},
            {'text': 'Grad jedes Knotens: A 2, B 2, C 3, D 1.', 'bild': _fig(_P4, _L4, _g(2, 2, 3, 1))},
            {'text': 'Summe 2 + 2 + 3 + 1 = 8 = 2 · ⟦4 Kanten⟧.'},
        ],
        'fehler': '8 Kanten ist falsch. Jede Straße wird ⟦an beiden Enden⟧ gezählt, also 8 : 2 = 4.',
        'regel': 'Grad = Kanten an einem Knoten. Die ⟦Summe aller Grade⟧ ist doppelt so groß wie die Zahl der Kanten.',
    },
    'euler': {
        'einstieg': 'Ein Postbote will jede Straße genau einmal entlanggehen. Geht das? Es hängt nur von den Graden ab. '
                    'So ein Weg heißt ⟦Eulerweg⟧.',
        'woerter': [['Eulerweg', 'ein Weg, der jede Kante genau einmal benutzt'],
                    ['Eulerkreis', 'ein Eulerweg, der wieder am Start endet']],
        'bild': _fig(_P5, _L5),
        'schritte': [
            {'text': 'Grade: A 2, B 3, C 4, D 3, E 2.', 'bild': _fig(_P5, _L5, _g(2, 3, 4, 3, 2))},
            {'text': 'Genau zwei Knoten sind ungerade: B und D.'},
            {'text': '⟦Eulerweg möglich⟧ von B nach D: B, A, C, B, D, C, E, D.', 'bild': _fig(_P5, _EU)},
            {'text': 'Ein Eulerkreis geht nicht, weil B und D ungerade sind.'},
        ],
        'fehler': 'Bei vier ungeraden Knoten gibt es keinen Eulerweg. An einem ungeraden Zwischenknoten ⟦bleibt eine Kante übrig⟧.',
        'regel': 'Ist der Graph ⟦zusammenhängend⟧, zähle die ⟦ungeraden Knoten⟧: 0 heißt Eulerkreis, 2 heißt Eulerweg, sonst keiner.',  # Prüfung neu 2: Bedingung ergänzt
    },
    'kuerzester': {
        'einstieg': 'Von Dorf A nach Dorf B sind es direkt 7 km. Über Dorf C sind es 2 km und 3 km. Welcher Weg ist kürzer? '
                    'Die Zahlen an den Kanten heißen ⟦Gewichte⟧.',
        'woerter': [['Gewicht', 'die Zahl an einer Kante: Länge, Zeit oder Kosten'],
                    ['kürzester Weg', 'der Weg mit der kleinsten Summe der Gewichte']],
        'bild': _k3([], [], []),
        'schritte': [
            {'text': 'Direkt A → B: 7 km.', 'bild': _k3([], ['gestrichelt'], ['gestrichelt'])},
            {'text': 'Über C: 2 + 3 = 5 km.', 'bild': _k3(['gestrichelt'], [], [])},
            {'text': 'Kürzester Weg: ⟦A → C → B mit 5 km⟧.'},
        ],
        'fehler': 'Immer die ⟦direkte Kante⟧ zu nehmen ist falsch. Hier ist der Umweg über C kürzer: 5 < 7.',
        'regel': 'Vom Start aus an jedem Knoten die ⟦kleinste bekannte Entfernung⟧ notieren. Umwege können kürzer sein.',
    },
    'spannbaum': {
        'einstieg': 'Vier Dörfer sollen Glasfaser bekommen. Jedes Dorf muss angeschlossen sein, aber Kabel sind teuer. '
                    'Gesucht ist das billigste Netz: ein ⟦minimaler Spannbaum⟧.',
        'woerter': [['minimaler Spannbaum', 'verbindet alle Knoten mit dem kleinsten Gesamtgewicht, ohne Kreis'],
                    ['Kreis', 'ein Weg, der zu seinem Start zurückführt'],
                    ['Baum', 'ein Graph ohne Kreis; bei n Knoten hat er n − 1 Kanten']],
        'bild': _sb({'AB', 'BC', 'AC', 'CD', 'BD'}),
        'schritte': [
            {'text': 'Kleinste Kante zuerst: BC (2), dann AC (3).', 'bild': _sb({'BC', 'AC'})},
            {'text': 'AB (4) würde den Kreis A–B–C schließen: weglassen.'},
            {'text': 'CD (5) nehmen. Jetzt ist jedes Dorf angeschlossen.', 'bild': _sb({'BC', 'AC', 'CD'})},
            {'text': 'Gewicht 2 + 3 + 5 = ⟦10⟧. 4 Knoten, 3 Kanten.'},
        ],
        'fehler': 'Die drei kleinsten Kanten 2, 3, 4 bilden einen ⟦Kreis⟧, D bleibt allein. Kanten, die einen Kreis schließen, überspringen.',
        'fehler_bild': _sb({'BC', 'AC', 'AB'}),
        'regel': 'Kanten der Größe nach nehmen, ⟦Kreise überspringen⟧. Bei n Knoten hat der Baum n − 1 Kanten.',
    },
    'verstehen': {
        'einstieg': 'Ein Rätsel: Drei Dörfer sollen jeweils 3 Straßen haben. Geht das? Ohne Probieren hilft eine Regel: '
                    'Die Summe der Grade muss ⟦gerade⟧ sein.',
        'woerter': [['Gradliste', 'die Grade aller Knoten nacheinander, z. B. 3, 3, 3']],
        'bild': _fig(_P3, []),
        'schritte': [
            {'text': 'Gradliste 3, 3, 3: Die Summe ist 9.'},
            {'text': 'Die Summe der Grade ist 2 · Anzahl der Kanten, also gerade.'},
            {'text': 'Selbst mit allen Straßen hat jedes Dorf nur Grad 2.',
             'bild': _fig(_P3, [['A', 'B'], ['A', 'C'], ['B', 'C']], {'A': 'A: 2', 'B': 'B: 2', 'C': 'C: 2'})},
            {'text': '9 ist ungerade: ⟦unmöglich⟧.'},
        ],
        'fehler': '„5 Knoten, 4 Kanten ist immer ein Baum“ ist falsch. Der Graph kann einen Kreis haben und ⟦nicht zusammenhängend⟧ sein.',
        'fehler_bild': _fig({'A': [0, 0], 'B': [4, 0], 'C': [2, -3], 'D': [6, -1], 'E': [7, -3]},
                            [['A', 'B'], ['A', 'C'], ['B', 'C'], ['D', 'E']]),
        'regel': 'Die Anzahl ⟦ungerader Knoten⟧ ist immer gerade. Prüfe eine Gradliste zuerst mit der Summe.',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


d = bauen('sonder.graphentheorie',
      'Graphen mit Knoten, Kanten und Graden beschreiben, Eulerwege erkennen, kürzeste Wege suchen und minimale Spannbäume bestimmen.',
      ['Graph (graph): Knoten (vertices) und Kanten (edges). Grad (degree) = Anzahl der Kanten an einem Knoten.',
       'Summe aller Grade = 2 · Anzahl der Kanten.',
       'Eulerkreis: alle Grade gerade. Eulerweg: genau zwei ungerade (Start und Ende).',
       'Kürzester Weg: Umwege prüfen, kleinste Entfernung an jedem Knoten merken (Dijkstra).',
       'Baum: zusammenhängend, ohne Kreis, n − 1 Kanten. Minimaler Spannbaum: Kruskal.'],
      [('Grundbegriffe', ['grundbegriffe']), ('Wege', ['euler', 'kuerzester']), ('Bäume und Aussagen', ['spannbaum', 'verstehen'])],
      ETAPPEN, GEN,
      offen=['Lehrplan-Feld: „Graphentheorie, Graphenalgorithmen (IB-Verlagsinhalt)“ – Auswahl: Grundbegriffe, Adjazenzmatrix (nur ablesen), Euler, Dijkstra-Idee, Kruskal. Hamiltonkreise und Zahlentheorie nicht enthalten.',
             'Graphen werden als figur gezeichnet (Knoten = beschriftete Punkte, Kanten = Linien mit Gewicht). Die App beschriftet Kantengewichte nach außen – bei Kanten zur Mitte kann die Zahl nah an einer anderen Linie stehen. Bitte in der Ansicht prüfen.'],
      vertiefung=['spannbaum'], plan=PLAN2)
umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)


# ---- STUFEN (Zwanzigste Runde, Zusatz Realschule/IB, Zweig stufen-rsib-2) ----
from _stufen_rsib2 import Stufen, stufen  # noqa: E402

ST = Stufen('sonder.graphentheorie', 20_2_7)
Z, A, L = ST.Z, ST.A, ST.L
ST.vorbild += ['IB MYP eAssessment Mathematics (Diskrete Mathematik, Extended/Projekt): Netzwerke, Eulerwege, kürzeste Wege, Spannbäume',
               'Känguru der Mathematik / Mathematik-Olympiade: Graphen- und Handschlag-Aufgaben als Vorbild für die Knobel-Bordkarten (nur Art)']

# grundbegriffe
ST.stufenleiter('grundbegriffe', 'Grad eines Knotens und Zahl der Kanten am Graphen ablesen.',
                'Gradsumme, Knoten mit ungeradem Grad, Graph aus einer Beschreibung, Kanten aus der Gradsumme.',
                'Handschläge, Adjazenzmatrix, fehlender Grad rückwärts, Kanten bei gleichen Graden, Fehler „Gradsumme = Kantenzahl“.')
ST.typ('grundbegriffe', '/^Welchen Grad|^Wie viele Kanten hat der Graph/', 'erkennen')
ST.typ('grundbegriffe', '/^/', 'mehrschritt', s=2)
ST.typ('grundbegriffe', '/Hand/', 'transfer')
ST.typ('grundbegriffe', '/Adjazenzmatrix/', 'verknuepfen')
ST.typ('grundbegriffe', '/Welchen Grad hat der letzte/', 'rueckwaerts')
ST.typ('grundbegriffe', '/^/', 'verknuepfen', s=3)
ST.neu('grundbegriffe', 'direkt', Z('Ein Graph hat die Kanten AB, AC, AD und BC. Welchen Grad hat A?', 3, '3', 'A liegt an AB, AC und AD: Grad 3.', 'Zähle die Kanten, in denen A vorkommt.'))
ST.neu('grundbegriffe', 'einkleidung', Z('Anna kennt Ben und Cem, Ben kennt außerdem Cem und Dora, Ella kennt niemanden aus der Gruppe. Jede Bekanntschaft ist eine Kante. Wie viele Kanten hat der Graph?', 4, '4',
       'Kanten: Anna–Ben, Anna–Cem, Ben–Cem, Ben–Dora. Ella ist ein Knoten ohne Kante.', 'Schreibe jede Bekanntschaft nur einmal auf.'))
ST.neu('grundbegriffe', 'umkehr', Z('Die Summe aller Grade eines Graphen ist 18. Wie viele Kanten hat er?', 9, '18/2', 'Jede Kante zählt bei zwei Knoten: 18 : 2 = 9.', 'Wie oft wird jede Kante in der Gradsumme gezählt?'))
ST.neu('grundbegriffe', 'fehler', A('Ein Graph hat die Kanten AB, BC, CA und CD. Jemand zählt die Grade 2 + 2 + 3 + 1 = 8 und sagt: „Der Graph hat 8 Kanten.“ Was stimmt?',
       'Falsch: Die Gradsumme ist doppelt so groß wie die Kantenzahl, es sind 4 Kanten.', ['Richtig.', 'Falsch: Es sind 3 Kanten.', 'Falsch: Es sind 16 Kanten.'],
       'Jede Kante hat zwei Enden und wird darum zweimal gezählt: 8 : 2 = 4.', 'Zähle die Kanten direkt.'))
ST.knobel('grundbegriffe', A('In einer Klasse sind 25 Kinder. Kann jedes Kind mit genau 3 anderen Kindern der Klasse befreundet sein?', 'Nein, die Gradsumme 25 · 3 = 75 wäre ungerade.',
          ['Ja, z. B. im Kreis.', 'Ja, wenn alle in drei Gruppen sitzen.', 'Das hängt von den Kindern ab.'],
          'Kinder sind Knoten, Freundschaften Kanten. Die Gradsumme ist immer doppelt so groß wie die Kantenzahl, also gerade. 25 · 3 = 75 ist ungerade – unmöglich.',
          'Was weißt du über die Summe aller Grade?'))
ST.knobel('grundbegriffe', A('Kann es einen Graphen mit 7 Knoten (ohne Mehrfachkanten und Schleifen) geben, in dem alle Knoten verschiedene Grade haben?', 'Nein.',
          ['Ja, mit den Graden 0 bis 6.', 'Ja, mit den Graden 1 bis 7.', 'Nur, wenn er zusammenhängend ist.'],
          'Mögliche Grade sind 0 bis 6 – sieben Werte. Grad 6 heißt: mit allen verbunden; dann kann kein Knoten Grad 0 haben. Also bleiben nur 6 verschiedene Werte für 7 Knoten.',
          'Können Grad 0 und Grad 6 gleichzeitig vorkommen?'))

# euler
ST.stufenleiter('euler', 'Mit der Zahl der ungeraden Knoten entscheiden: Eulerkreis, Eulerweg oder keins.',
                'Ungerade Knoten aus einer Kantenliste bestimmen, Sachsituationen (Briefträger, Museum), Endknoten eines Eulerwegs.',
                'Königsberger Brücken, Haus vom Nikolaus, fehlende Kante ergänzen, Mindestzahl neuer Kanten, Fehler „4 ungerade genügen“, vollständige Graphen als Parameter.')
ST.typ('euler', '/^Hat der Graph/', 'erkennen')
ST.typ('euler', '/^Wie viele Knoten mit ungeradem/', 'mehrschritt')
ST.typ('euler', '/Königsberg/', 'transfer')
ST.typ('euler', '/Ni-ko-laus/', 'begruenden')
ST.typ('euler', '/zusätzliche Kante/', 'verknuepfen')
ST.typ('euler', '/^/', 'rueckwaerts', s=3)
ST.neu('euler', 'direkt', A('Ein zusammenhängender Graph hat die Grade 2, 2, 4, 2. Was gibt es?', 'einen Eulerkreis', ['nur einen Eulerweg', 'weder noch', 'Das kann man nicht sagen.'],
       'Alle Grade sind gerade: Eulerkreis.', 'Zähle die ungeraden Grade.'))
ST.neu('euler', 'direkt', A('Ein zusammenhängender Graph hat die Grade 3, 2, 3, 2. Was gibt es?', 'einen Eulerweg, aber keinen Eulerkreis', ['einen Eulerkreis', 'weder noch', 'zwei Eulerkreise'],
       'Genau zwei ungerade Grade: Eulerweg von einem ungeraden Knoten zum anderen.', 'Zähle die ungeraden Grade.'))
ST.neu('euler', 'einkleidung', A('Ein Briefträger will jede Straße eines Viertels genau einmal ablaufen und zum Start zurückkehren. An jeder Kreuzung treffen 2 oder 4 Straßen zusammen (Netz zusammenhängend). Geht das?',
       'Ja, alle Grade sind gerade.', ['Nein, er muss Straßen doppelt gehen.', 'Nur, wenn er an einer Ecke startet.', 'Das hängt von der Länge ab.'],
       'Kreuzungen sind Knoten, Straßen Kanten. Alle Grade gerade: Es gibt einen Eulerkreis.', 'Welche Grade haben die Kreuzungen?'))
ST.neu('euler', 'einkleidung', A('Ein Museum: Räume sind Knoten, Türen Kanten. Die Räume haben 2, 3, 2, 3 und 2 Türen (zusammenhängend). Kann man jede Tür genau einmal durchschreiten?',
       'Ja, wenn man in einem Raum mit 3 Türen beginnt und im anderen endet.', ['Ja, von jedem Raum aus und zurück.', 'Nein.', 'Nur mit einer Tür doppelt.'],
       'Genau zwei ungerade Grade: Eulerweg zwischen den beiden Räumen mit 3 Türen.', 'Zähle die ungeraden Grade.'))
ST.neu('euler', 'umkehr', A('In einem Graphen haben nur A und D einen ungeraden Grad. Ein Eulerweg beginnt in A. Wo endet er?', 'in D', ['in A', 'in einem Knoten mit geradem Grad', 'Das ist beliebig.'],
       'Ein Eulerweg beginnt und endet in den beiden ungeraden Knoten.', 'Wo muss ein Eulerweg starten und enden?'))
ST.neu('euler', 'mehrschritt', A('Ein Graph hat die Kanten AB, BC, CA, CD und DA. Welche Knoten haben einen ungeraden Grad?', 'A und C', ['B und D', 'alle', 'keiner'],
       'Grade: A 3 (AB, CA, DA), B 2, C 3 (BC, CA, CD), D 2. Ungerade: A und C – es gibt einen Eulerweg von A nach C.', 'Zähle für jeden Knoten seine Kanten.'))
ST.neu('euler', 'fehler', A('Jemand sagt: „Mein Graph hat 4 Knoten mit ungeradem Grad, also gibt es einen Eulerweg.“ Was stimmt?', 'Falsch: Ein Eulerweg braucht 0 oder 2 ungerade Knoten.',
       ['Richtig.', 'Falsch: Es gibt dann sogar einen Eulerkreis.', 'Richtig, wenn der Graph zusammenhängend ist.'],
       'Jeder Knoten außer Start und Ziel wird gleich oft betreten und verlassen – gerader Grad. Mit 4 ungeraden Knoten geht es nicht.', 'Welche Knoten dürfen ungerade sein?'))
ST.neu('euler', 'parameter', A('Im vollständigen Graphen mit n Knoten ist jeder Knoten mit jedem verbunden. Für welche n zwischen 3 und 8 hat er einen Eulerkreis?', 'n = 3, 5, 7',
       ['n = 4, 6, 8', 'für alle n', 'nur n = 3'], 'Jeder Knoten hat den Grad n − 1. Gerade ist er für ungerade n: 3, 5, 7.', 'Welchen Grad hat jeder Knoten?'))
ST.knobel('euler', Z('Die 12 Kanten eines Würfels (8 Ecken) sollen alle abgelaufen werden, mit Rückkehr zum Start. Wie viele Kanten muss man dabei mindestens doppelt ablaufen?', 4, '8/2',
          'Jede Ecke hat Grad 3 (ungerade). Jede doppelt gelaufene Kante macht zwei Ecken gerade. Für 8 ungerade Ecken braucht man mindestens 4 Kanten – und 4 gegenüberliegende parallele Kanten reichen.',
          'Wie viele ungerade Ecken gibt es, und wie viele davon „repariert“ eine doppelte Kante?'))
ST.knobel('euler', A('Ein Oktaeder hat 6 Ecken; an jeder Ecke treffen 4 Kanten zusammen. Kann man alle Kanten in einem Zug ablaufen und zum Start zurückkehren?', 'Ja, alle Grade sind gerade.',
          ['Nein, 6 Ecken sind zu viele.', 'Nur ohne Rückkehr.', 'Nein, 4 ist zu groß.'],
          'Der Kantengraph ist zusammenhängend, jeder Knoten hat Grad 4: Eulerkreis.', 'Welche Grade haben die Ecken?'))

# kuerzester
ST.stufenleiter('kuerzester', 'Schnellsten Weg in einem kleinen Netz ablesen.',
                'Den kürzesten Weg als Knotenfolge angeben, Wege vergleichen, Netz aus einer Beschreibung.',
                'Gesperrte Straße, Zwischenhalt, Erreichbarkeit in einer Zeitgrenze, Umweg kürzer als Direktweg, Fehler „immer die kürzeste nächste Kante“.')
ST.typ('kuerzester', '/^Die Zahlen an den Kanten/', 'direkt')
ST.typ('kuerzester', '/^/', 'darstellung', s=2)
ST.typ('kuerzester', '/gesperrt/', 'transfer')
ST.typ('kuerzester', '/halten|Wie viele Orte/', 'verknuepfen')
ST.typ('kuerzester', '/^/', 'begruenden', s=3)
ST.neu('kuerzester', 'erkennen', A('Kanten: A–B 4, B–C 3, A–C 9. Welcher Weg von A nach C ist kürzer?', 'über B (7)', ['direkt (9)', 'beide gleich', 'über C'],
       'Über B: 4 + 3 = 7 < 9.', 'Rechne beide Wege aus.'))
ST.neu('kuerzester', 'einkleidung', Z('Ein Bote fährt von Lager L zu Kunde K. Straßen: L–M 5 km, M–K 6 km, L–N 4 km, N–K 8 km, M–N 2 km. Wie lang ist die kürzeste Strecke?', 11, '5 + 6',
       'L–M–K: 11. L–N–K: 12. L–N–M–K: 12. L–M–N–K: 15. Kürzeste: 11 km.', 'Gehe alle Wege durch.', einheit='km'))
ST.neu('kuerzester', 'mehrschritt', Z('Kanten: A–B 2, B–C 2, C–D 2, A–D 7, B–D 5. Wie lang ist der kürzeste Weg von A nach D?', 6, '2 + 2 + 2',
       'A–B–C–D: 6. A–B–D: 7. A–D: 7. Kürzester: 6.', 'Mehr Kanten kann kürzer sein.'))
ST.neu('kuerzester', 'fehler', A('Kanten: A–B 1, B–D 10, A–C 3, C–D 3. Jemand nimmt immer die kürzeste nächste Kante: A–B–D, also 11. Was stimmt?',
       'Falsch: A–C–D ist mit 6 kürzer; die kürzeste erste Kante führt nicht immer zum kürzesten Weg.', ['Richtig.', 'Falsch: A–D direkt mit 4.', 'Falsch: A–C–B–D mit 14.'],
       'Man muss ganze Wege vergleichen (z. B. mit dem Dijkstra-Verfahren), nicht nur den ersten Schritt.', 'Rechne auch den Weg über C.'))
ST.knobel('kuerzester', Z('Ein Stadtplan ist ein Gitter aus 3 mal 3 Häuserblöcken. Man geht nur nach rechts oder nach oben. Wie viele kürzeste Wege gibt es von der Ecke links unten zur Ecke rechts oben?', 20, '20',
          'Jeder kürzeste Weg hat 3 Schritte nach rechts und 3 nach oben, zusammen 6. Zählt man an jeder Kreuzung die Wege dorthin (Summe der Werte links und unten), erhält man rechts oben 20.',
          'Schreibe an jede Kreuzung, auf wie vielen Wegen man sie erreicht.'))
ST.knobel('kuerzester', A('In einem Netz wird jede Kantenlänge um 1 erhöht. Bleibt der kürzeste Weg von A nach B immer derselbe?', 'Nein, Wege mit vielen Kanten werden stärker verlängert.',
          ['Ja, immer.', 'Ja, die Reihenfolge der Wege ändert sich nie.', 'Nein, er wird immer kürzer.'],
          'Beispiel: A–C–D–B mit 1 + 1 + 1 = 3 gegen A–B direkt mit 4. Nach +1: 6 gegen 5 – jetzt ist der direkte Weg kürzer.', 'Vergleiche einen Weg mit vielen kurzen und einen mit einer langen Kante.'))

# spannbaum
ST.stufenleiter('spannbaum', 'Kruskal-Start (kleinste Kante), Kanten eines Spannbaums = Knoten − 1.',
                'Ersparnis gegenüber allen Leitungen, Kanten, die einen Kreis schließen, Spannbaum aus einer Kostenliste, Knoten aus Kanten.',
                'Teuerste Leitung im Spannbaum, neue billige Leitung, unverzichtbare Leitung, Fehler „Kreis mitnehmen“.')
ST.typ('spannbaum', '/Kruskal-Verfahren/', 'erkennen')
ST.typ('spannbaum', '/^/', 'direkt', s=1)
ST.typ('spannbaum', '/Wie viel spart man/', 'mehrschritt')
ST.typ('spannbaum', '/^/', 'darstellung', s=2)
ST.typ('spannbaum', '/teuerste Leitung, die/', 'verknuepfen')
ST.typ('spannbaum', '/Eine neue Leitung/', 'transfer')
ST.typ('spannbaum', '/^/', 'begruenden', s=3)
ST.neu('spannbaum', 'einkleidung', Z('Vier Inseln sollen mit Brücken verbunden werden. Kosten in Mio €: A–B 3, A–C 5, B–C 4, B–D 6, C–D 2. Wie viel kostet die günstigste Verbindung aller Inseln?', 9, '2 + 3 + 4',
       'Kruskal: C–D (2), A–B (3), B–C (4) – jetzt hängen alle zusammen. 2 + 3 + 4 = 9 Mio €.', 'Nimm die Brücken der Größe nach.', einheit='Mio €'))
ST.neu('spannbaum', 'umkehr', Z('Ein Spannbaum hat 15 Kanten. Wie viele Knoten hat der Graph?', 16, '15 + 1', 'Spannbaum: Kanten = Knoten − 1, also 16 Knoten.', 'Wie hängen Kanten und Knoten bei einem Baum zusammen?'))
ST.neu('spannbaum', 'fehler', A('Jemand nimmt beim Kruskal-Verfahren auch eine billige Kante, die einen Kreis schließt. Was ist falsch daran?', 'Die Kante verbindet nichts Neues und kostet nur zusätzlich.',
       ['Nichts, billige Kanten sind immer gut.', 'Dann fehlt ein Knoten.', 'Kreise sind nur bei teuren Kanten verboten.'],
       'Schließt eine Kante einen Kreis, sind ihre Enden schon verbunden. Sie bringt keinen Nutzen, aber Kosten – ein Spannbaum hat keine Kreise.', 'Was verbindet diese Kante?'))
ST.knobel('spannbaum', A('Alle Leitungen eines Netzes haben verschiedene Kosten. Gehört die billigste Leitung immer zum minimalen Spannbaum?', 'Ja.',
          ['Nein, nur wenn sie an einem Randknoten liegt.', 'Nur bei Kruskal, nicht bei anderen Verfahren.', 'Nein, nie.'],
          'Angenommen, sie fehlt. Fügt man sie hinzu, entsteht ein Kreis; nimmt man dafür eine andere (teurere) Kante dieses Kreises heraus, bleibt alles verbunden und wird billiger – Widerspruch.',
          'Was passiert, wenn man sie in einen Spannbaum ohne sie einfügt?'))
ST.knobel('spannbaum', Z('Ein Graph mit 5 Knoten ist ein einziger Kreis (5 Kanten). Wie viele verschiedene Spannbäume hat er?', 5, '5',
          'Ein Spannbaum braucht 4 Kanten ohne Kreis. Man muss genau eine der 5 Kanten weglassen – jede Wahl ergibt einen anderen Spannbaum: 5.', 'Wie viele Kanten muss man weglassen?'))

# verstehen
ST.stufenleiter('verstehen', 'Gradfolgen mit ungerader Summe als unmöglich erkennen; Baum: Knoten = Kanten + 1.',
                'Gradfolgen prüfen, „genau 3 ungerade Knoten“, Straßennetz als Baum, überflüssige Kanten.',
                'Gerade Gradsumme reicht nicht immer, höchste Kantenzahl, Eulerkreis-Fehlschluss, gleicher Grad rückwärts.')
ST.typ('verstehen', '/^Kann es einen Graphen/', 'erkennen', s=1)
ST.typ('verstehen', '/^/', 'direkt', s=1)
ST.typ('verstehen', '/Ist es ein Baum/', 'einkleidung', s=2)
ST.typ('verstehen', '/^/', 'mehrschritt', s=2)
ST.typ('verstehen', '/^Kim/', 'fehler')
ST.typ('verstehen', '/höchstens/', 'verknuepfen')
ST.typ('verstehen', '/Ist es ein Baum/', 'transfer')
ST.typ('verstehen', '/^/', 'begruenden', s=3)
ST.neu('verstehen', 'umkehr', Z('Ein zusammenhängender Graph mit 10 Knoten hat 12 Kanten. Wie viele Kanten muss man mindestens entfernen, damit ein Baum entsteht?', 3, '12 - (10 - 1)',
       'Ein Baum mit 10 Knoten hat 9 Kanten. 12 − 9 = 3 Kanten müssen weg (je eine aus einem Kreis).', 'Wie viele Kanten hat ein Baum mit 10 Knoten?'))
ST.neu('verstehen', 'rueckwaerts', Z('Ein Graph hat 6 Knoten, alle mit demselben Grad, und 9 Kanten. Welchen Grad hat jeder Knoten?', 3, '2*9/6',
       'Gradsumme 2 · 9 = 18, verteilt auf 6 Knoten: 18 : 6 = 3.', 'Wie groß ist die Gradsumme?'))
ST.knobel('verstehen', A('Stimmt: In jeder Gruppe von mindestens 2 Personen gibt es zwei, die gleich viele Bekannte in der Gruppe haben?', 'Ja.',
          ['Nein, man kann es immer verschieden machen.', 'Nur bei geraden Gruppengrößen.', 'Nur, wenn jeder jemanden kennt.'],
          'Bei n Personen sind 0 bis n − 1 Bekannte möglich. 0 und n − 1 schließen sich aus (wer alle kennt, wird von jedem gekannt). Also nur n − 1 Werte für n Personen: Zwei müssen gleich sein.',
          'Können „kennt niemanden“ und „kennt alle“ gleichzeitig vorkommen?'))
ST.knobel('verstehen', Z('Ein Graph ohne Kreise besteht aus mehreren Bäumen (ein „Wald“). Er hat 20 Knoten und 16 Kanten. Aus wie vielen Bäumen besteht er?', 4, '20 - 16',
          'Jeder Baum hat eine Kante weniger als Knoten. Bei k Bäumen fehlen also k Kanten: 20 − k = 16 ⇒ k = 4.', 'Wie viele Kanten fehlen pro Baum gegenüber den Knoten?'))

if __name__ == '__main__':
    stufen('sonder.graphentheorie', ST)
