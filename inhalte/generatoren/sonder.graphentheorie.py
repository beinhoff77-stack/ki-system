#!/usr/bin/env python3
"""Thema sonder.graphentheorie – Graphentheorie (IB MYP 4, etwa Klasse 9)."""
import heapq
import itertools
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403

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
    art = R.choice({1: ['laenge', 'laenge'], 2: ['laenge', 'weg', 'laenge'], 3: ['weg', 'umweg', 'laenge']}[s])
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
    art = R.choice({1: ['kanten_n', 'gewicht'], 2: ['gewicht', 'gewicht', 'erste'], 3: ['gewicht', 'ausgelassen', 'ersparnis']}[s])
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
    art = R.choice({1: ['moeglich', 'baum_kanten'], 2: ['moeglich', 'ungerade_anzahl', 'baum_kreis'], 3: ['moeglich', 'baum_kreis', 'fehler_euler', 'ungerade_anzahl']}[s])
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


GEN = {'grundbegriffe': g_grundbegriffe, 'euler': g_euler, 'kuerzester': g_kuerzester, 'spannbaum': g_spannbaum, 'verstehen': g_verstehen}

bauen('sonder.graphentheorie',
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
      vertiefung=['spannbaum'])
