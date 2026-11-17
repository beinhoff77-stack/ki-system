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
    return auswahl('Leo sagt: „Mein Graph ist zusammenhängend und hat genau zwei Knoten mit ungeradem Grad, also gibt es einen Eulerkreis.“ Stimmt das?', r,
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
    if art == 'fehler_euler': return _filter(g_verstehen, 3, 'Leo')
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
        'regel': 'Zähle die ⟦ungeraden Knoten⟧: 0 heißt Eulerkreis, 2 heißt Eulerweg, sonst keiner.',
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
