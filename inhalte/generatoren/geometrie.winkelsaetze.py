#!/usr/bin/env python3
"""Thema geometrie.winkelsaetze – Winkelsätze (Gymnasium Bayern, Klasse 7, LehrplanPLUS M7 2.2 „Winkelbetrachtungen an Figuren“).

Vierzehnte Runde (Zweig daten-klassen-2). Baut auf geometrie.winkel (Klasse 5, „Mit Winkeln rechnen“) auf und wiederholt dessen Inhalte nicht:
Fachbegriffe Scheitel- und Nebenwinkel, Stufen- und Wechselwinkel an Parallelen, Parallelität prüfen, Innenwinkelsumme im Dreieck (Beweis mit
Wechselwinkeln), Außenwinkel, Winkelsumme im Vieleck, Winkel in Figuren mit mehreren Kreuzungen, Fundamentalsatz und abgeleiteter Satz.

Je Lernkarte: 18 Übungen (Stufe 1: 4, Stufe 2: 6, Stufe 3: 8; davon 2 nach Prüfungsvorbild und 1 Knobelaufgabe), 1 Test, 3 Korrektur, 6 Sicherung.
Prüfungsvorbilder (nur Typ und Niveau, eigene Zahlen und Einkleidung): Bayerischer Mathematik-Test 8 (ISB) 2019 B5 und B7, 2021 A8, 2022 A7,
2025 A8; Jahrgangsstufentest Realschule 8 (ISB) 2020 II und 2025 II Nr. 5/6; Vergleichsarbeit Jgst. 8 (Innenwinkel im n-Eck).

    python3 -I inhalte/generatoren/geometrie.winkelsaetze.py
    python3 -I tools/inhalt_pruefen.py inhalte/themen/geometrie.winkelsaetze.json
"""
import collections
import json
import math
import random
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.dont_write_bytecode = True
HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
from _bausatz import jw, rechne, zt  # noqa: E402

ZIEL = HIER.parent / 'themen' / 'geometrie.winkelsaetze.json'
META = {'thema_schluessel': 'geometrie.winkelsaetze', 'thema_id': 98, 'block_id': 80, 'klasse': {'gym_by': 7}}
P, K = 'pruefung', 'knobel'
POS_TEXT = {'ro': 'rechts oberhalb', 'lo': 'links oberhalb', 'lu': 'links unterhalb', 'ru': 'rechts unterhalb'}


# ---------- Bausteine für Aufgaben ----------
_POS = collections.Counter()


def Z(text, wert, c, w, h='', einheit='°', art=None, grafik=None):
    assert rechne(c) == Fr(wert), f'Nachrechnung falsch: {c} = {rechne(c)}, Lösung {wert} ({text})'
    a = {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': jw(Fr(wert))}, 'c': c, 'w': w, 'h': h}
    if einheit: a['o']['einheit'] = einheit
    if grafik: a['f']['grafik'] = grafik
    if art: a['_art'] = art
    return a


def A(R, text, richtig, falsche, w, h='', art=None, grafik=None):
    richtig = str(richtig)
    f = []
    for x in map(str, falsche):
        if x != richtig and x not in f: f.append(x)
    assert len(f) >= 2, (text, f)
    f = f[:3]
    R.shuffle(f)
    n = len(f) + 1
    frei = [i for i in range(n) if _POS[(n, i)] == min(_POS[(n, j)] for j in range(n))]
    i = R.choice(frei)
    _POS[(n, i)] += 1
    f.insert(i, richtig)
    a = {'y': 'auswahl', 'f': {'text': text}, 'a': f, 'o': {'index': i}, 'w': w, 'h': h}
    if grafik: a['f']['grafik'] = grafik
    if art: a['_art'] = art
    return a


def L(text, schablone, werte, c, w, h, hinweis, art=None):
    for ci, v in zip(c, werte): assert rechne(ci) == Fr(v), (ci, v)
    a = {'y': 'luecken', 'f': {'text': text, 'schablone': schablone, 'hinweis': hinweis}, 'o': {'werte': [int(v) for v in werte]}, 'c': list(c), 'w': w, 'h': h}
    if art: a['_art'] = art
    return a


def g(x):
    return f'{zt(x)}°'


# ---------- Zeichnungen ----------
def _r(v):
    return round(v, 2)


def _strahlen(name, x, y, a, l=1.6):
    ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
    return {name: [_r(x), _r(y)], f'_{name}R': [_r(x + l), _r(y)], f'_{name}L': [_r(x - l), _r(y)],
            f'_{name}U': [_r(x + l * ca), _r(y + l * sa)], f'_{name}D': [_r(x - l * ca), _r(y - l * sa)]}


_SCHENKEL = {'ro': ('R', 'U'), 'lo': ('U', 'L'), 'lu': ('L', 'D'), 'ru': ('D', 'R')}


def _w(name, pos, text):
    s1, s2 = _SCHENKEL[pos]
    return [name, f'_{name}{s1}', f'_{name}{s2}', text]


def doppel(a, marken, parallel=True, a2=None):
    """Zwei waagrechte Geraden g (oben, Punkt S) und h (unten, Punkt T), geschnitten von k. a = Winkel ro zwischen k und g (Zeichnung).
    marken: Liste (Punkt 'S'|'T', Lage 'ro'|'lo'|'lu'|'ru', Text). parallel=False zeichnet h leicht gekippt (nur Optik)."""
    a = min(max(a, 35), 145)
    t = (2.0, 0.0)
    ct = 3 * math.cos(math.radians(a)) / math.sin(math.radians(a))
    s = (t[0] + ct, 3.0)
    pk = {**_strahlen('S', *s, a), **_strahlen('T', *t, a)}
    d = (math.cos(math.radians(a)), math.sin(math.radians(a)))
    pk.update({'_g1': [_r(min(s[0], t[0]) - 3), 3], '_g2': [_r(max(s[0], t[0]) + 3), 3],
               '_h1': [_r(min(s[0], t[0]) - 3), 0 if parallel else -0.4], '_h2': [_r(max(s[0], t[0]) + 3), 0 if parallel else 0.4],
               '_k1': [_r(t[0] - 1.6 * d[0]), _r(-1.6 * d[1])], '_k2': [_r(s[0] + 1.6 * d[0]), _r(3 + 1.6 * d[1])]})
    return {'typ': 'figur', 'punkte': pk, 'linien': [['_g1', '_g2', 'g'], ['_h1', '_h2', 'h'], ['_k1', '_k2', 'k']],
            'winkel': [_w(p, lage, txt) for p, lage, txt in marken]}


def einfach(a, marken):
    """Eine Kreuzung zweier Geraden in S; a = Winkel ro (Zeichnung)."""
    a = min(max(a, 35), 145)
    pk = _strahlen('S', 0, 0, a, 3)
    return {'typ': 'figur', 'punkte': pk, 'linien': [['_SL', '_SR'], ['_SD', '_SU']], 'winkel': [_w('S', lage, txt) for lage, txt in marken]}


def dreieck(al, be, marken, aussen=None):
    """Dreieck ABC mit Winkeln al bei A und be bei B (Zeichnung). marken: Liste (Ecke, Text). aussen: (Ecke, Text) für einen Außenwinkel."""
    ga = 180 - al - be
    c = 6.0
    b = c * math.sin(math.radians(be)) / math.sin(math.radians(ga))
    C = (b * math.cos(math.radians(al)), b * math.sin(math.radians(al)))
    pk = {'A': [0, 0], 'B': [6, 0], 'C': [_r(C[0]), _r(C[1])]}
    win = {'A': ['A', 'B', 'C'], 'B': ['B', 'C', 'A'], 'C': ['C', 'A', 'B']}
    lin = [['A', 'B'], ['B', 'C'], ['C', 'A']]
    fig = {'typ': 'figur', 'punkte': pk, 'flaeche': ['A', 'B', 'C'], 'linien': lin, 'winkel': [win[e] + [t] for e, t in marken]}
    if aussen:
        e, t = aussen
        if e == 'B':
            pk['_X'] = [8.5, 0]
            lin.append(['B', '_X', '', 'gestrichelt'])
            fig['winkel'].append(['B', '_X', 'C', t])
        elif e == 'A':
            pk['_X'] = [-2.5, 0]
            lin.append(['A', '_X', '', 'gestrichelt'])
            fig['winkel'].append(['A', 'C', '_X', t])
        else:
            v = (C[0] - 0, C[1] - 0)
            n = math.hypot(*v)
            pk['_X'] = [_r(C[0] + 2.5 * v[0] / n), _r(C[1] + 2.5 * v[1] / n)]
            lin.append(['C', '_X', '', 'gestrichelt'])
            fig['winkel'].append(['C', 'B', '_X', t])
    return fig


# ---------- Lernkarten (neues Muster, Vorgabe 16.11.) ----------
B_SN = einfach(65, [('ro', 'α = 65°'), ('lo', 'β'), ('lu', 'γ'), ('ru', 'δ')])
B_SW = doppel(60, [('S', 'ro', 'α = 60°'), ('T', 'ro', 'β'), ('T', 'lu', 'γ')])
B_PP = doppel(70, [('S', 'ro', '70°'), ('T', 'ro', '70°')])
B_D = dreieck(50, 70, [('A', 'α'), ('B', 'β'), ('C', 'γ')])
B_DP = {**B_D, 'punkte': {**B_D['punkte'], '_p1': [-1.5, B_D['punkte']['C'][1]], '_p2': [7.5, B_D['punkte']['C'][1]]},
        'linien': B_D['linien'] + [['_p1', '_p2', 'p', 'gestrichelt']]}
B_AW = dreieck(50, 70, [('A', 'α = 50°'), ('B', 'β = 70°'), ('C', 'γ')], aussen=('C', 'γ\''))
B_VE = {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [6, 0], 'C': [7, 3.5], 'D': [3, 5.5], 'E': [-1, 3]},
        'flaeche': ['A', 'B', 'C', 'D', 'E'], 'linien': [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'A']]}
B_FI = {'typ': 'figur', 'punkte': {'_g1': [-1, 4.24], '_g2': [8, 4.24], '_h1': [-1, 0], '_h2': [8, 0], 'C': [4.05, 4.24], 'A': [0.5, 0], 'B': [6.5, 0],
                                    '_C1': [-0.5, 4.24], '_C2': [7.5, 4.24]},
        'linien': [['_g1', '_g2', 'g'], ['_h1', '_h2', 'h'], ['A', 'C'], ['B', 'C'], ['A', 'B']],
        'winkel': [['A', 'B', 'C', '50°'], ['B', 'C', 'A', '60°'], ['C', 'A', 'B', 'γ']]}

ETAPPEN = [
    {'lernziel': 'scheitel_neben', 'titel': 'Scheitelwinkel und Nebenwinkel',
     'einstieg': 'Zwei Laserstrahlen kreuzen sich auf einer Bühne. Es entstehen vier Winkel. Die gegenüberliegenden nennt man ⟦Scheitelwinkel⟧, die nebeneinander liegenden Nebenwinkel.',
     'woerter': [['Scheitelwinkel', 'Winkel, die sich an einer Kreuzung gegenüberliegen'], ['Nebenwinkel', 'Winkel nebeneinander an einer Geraden; zusammen 180°']],
     'bild': B_SN,
     'schritte': [{'text': 'α = 65°. β ist Nebenwinkel von α: β = 180° − 65° = 115°.',
                   'bild': {'winkel': [_w('S', 'ro', 'α = 65°'), _w('S', 'lo', 'β = 115°'), _w('S', 'lu', 'γ'), _w('S', 'ru', 'δ')]}},
                  {'text': 'γ liegt α gegenüber: Scheitelwinkel, also ⟦γ = 65°⟧.',
                   'bild': {'winkel': [_w('S', 'ro', 'α = 65°'), _w('S', 'lo', 'β = 115°'), _w('S', 'lu', 'γ = 65°'), _w('S', 'ru', 'δ')]}},
                  {'text': 'δ liegt β gegenüber: δ = 115°.',
                   'bild': {'winkel': [_w('S', 'ro', 'α = 65°'), _w('S', 'lo', 'β = 115°'), _w('S', 'lu', 'γ = 65°'), _w('S', 'ru', 'δ = 115°')]}}],
     'probe': '65° + 115° + 65° + 115° = 360° ✓',
     'fehler': 'Nebenwinkel sind nicht gleich groß, sie ergänzen sich zu 180°. Gleich groß sind nur Scheitelwinkel.',
     'fehler_bild': {'winkel': [_w('S', 'ro', 'α = 65°'), _w('S', 'lo', 'nicht 65°!')]},
     'regel': 'Scheitelwinkel sind ⟦gleich groß⟧. Nebenwinkel ergeben zusammen 180°.'},
    {'lernziel': 'stufen_wechsel', 'titel': 'Stufen- und Wechselwinkel',
     'einstieg': 'Zwei parallele Gleise werden von einer Straße gekreuzt. An beiden Kreuzungen sieht es gleich aus. Gleich liegende Winkel heißen ⟦Stufenwinkel⟧, über Kreuz liegende Wechselwinkel.',
     'woerter': [['parallel', 'überall gleich weit voneinander entfernt; Zeichen ∥'], ['Stufenwinkel', 'Winkel an zwei Kreuzungen in gleicher Lage'],
                 ['Wechselwinkel', 'Winkel an zwei Kreuzungen, über Kreuz zwischen den Parallelen']],
     'bild': B_SW,
     'schritte': [{'text': 'g ∥ h. Bei S ist α = 60° (rechts oberhalb).'},
                  {'text': 'β liegt bei T genauso: Stufenwinkel, also ⟦β = 60°⟧.',
                   'bild': {'winkel': [_w('S', 'ro', 'α = 60°'), _w('T', 'ro', 'β = 60°'), _w('T', 'lu', 'γ')]}},
                  {'text': 'γ liegt bei T links unterhalb: Scheitelwinkel von β, also γ = 60°.',
                   'bild': {'winkel': [_w('S', 'ro', 'α = 60°'), _w('T', 'ro', 'β = 60°'), _w('T', 'lu', 'γ = 60°')]}},
                  {'text': 'Bei S links unterhalb liegt auch 60°: Wechselwinkel zu β.',
                   'bild': {'winkel': [_w('S', 'lu', '60°'), _w('T', 'ro', 'β = 60°')]}}],
     'fehler': 'Ohne Parallelen gilt das nicht. Laufen die Gleise schräg zueinander, sind Stufenwinkel verschieden groß.',
     'fehler_bild': doppel(60, [('S', 'ro', '60°'), ('T', 'ro', '≠ 60°')], parallel=False),
     'regel': 'An Parallelen sind ⟦Stufenwinkel und Wechselwinkel gleich groß⟧.'},
    {'lernziel': 'parallel_pruefen', 'titel': 'Sind die Geraden parallel?',
     'einstieg': 'Eine Schreinerin prüft, ob zwei Regalbretter parallel sind. Sie misst, wie schräg eine Leiste beide Bretter trifft. Gleiche Stufenwinkel bedeuten: die Bretter sind ⟦parallel⟧.',
     'woerter': [['Umkehrung', 'der Satz rückwärts gelesen: aus gleichen Winkeln folgt parallel']],
     'bild': B_PP,
     'schritte': [{'text': 'k trifft g bei S unter 70°, h bei T auch unter 70°.'},
                  {'text': 'Die beiden Winkel liegen gleich: Es sind Stufenwinkel.'},
                  {'text': 'Gleich große Stufenwinkel: Nach der Umkehrung ist ⟦g ∥ h⟧.'},
                  {'text': 'Bei 70° und 72° wären die Geraden nicht parallel.',
                   'bild': doppel(70, [('S', 'ro', '70°'), ('T', 'ro', '72°')], parallel=False)}],
     'fehler': 'Gleiche Scheitelwinkel an einer Kreuzung beweisen nichts. Vergleichen muss man Winkel an beiden Kreuzungen.',
     'fehler_bild': doppel(70, [('S', 'ro', '70°'), ('S', 'lu', '70°')]),
     'regel': 'Gleich große ⟦Stufen- oder Wechselwinkel⟧ zeigen: Die Geraden sind parallel.'},
    {'lernziel': 'innenwinkelsumme', 'titel': 'Winkelsumme im Dreieck begründen',
     'einstieg': 'Reiße die drei Ecken eines Papierdreiecks ab und lege sie nebeneinander. Sie bilden eine gerade Linie. Das gilt für jedes Dreieck: Die ⟦Innenwinkelsumme⟧ ist 180°.',
     'woerter': [['Innenwinkelsumme', 'alle Winkel innen in einer Figur zusammen'], ['Hilfslinie', 'eine Linie, die man extra einzeichnet, um etwas zu zeigen']],
     'bild': B_D,
     'schritte': [{'text': 'Zeichne durch C eine Hilfslinie p parallel zu [AB].', 'bild': B_DP},
                  {'text': 'Links von C entsteht α: Wechselwinkel an Parallelen.'},
                  {'text': 'Rechts von C entsteht β, ebenfalls ein Wechselwinkel.'},
                  {'text': 'Auf p liegen α, γ und β nebeneinander: ⟦α + β + γ = 180°⟧.'}],
     'fehler': 'Messen an einem Dreieck ist kein Beweis. Erst die Begründung mit Wechselwinkeln zeigt: Es gilt für jedes Dreieck.',
     'regel': 'In jedem Dreieck gilt ⟦α + β + γ = 180°⟧. Der Beweis nutzt Wechselwinkel an einer Parallelen.'},
    {'lernziel': 'aussenwinkel', 'titel': 'Außenwinkel am Dreieck',
     'einstieg': 'Ein Läufer rennt um ein dreieckiges Feld. An jeder Ecke biegt er ab. Der Winkel, um den er abbiegt, ist ein ⟦Außenwinkel⟧ des Dreiecks.',
     'woerter': [['Außenwinkel', 'Nebenwinkel eines Innenwinkels; außen an der verlängerten Seite']],
     'bild': B_AW,
     'schritte': [{'text': 'Der Außenwinkel γ\' ist Nebenwinkel von γ: γ\' = 180° − γ.'},
                  {'text': 'Mit der Winkelsumme gilt γ = 180° − 50° − 70° = 60°.'},
                  {'text': 'Also ist γ\' = 120° – das sind genau ⟦α + β⟧.',
                   'bild': dreieck(50, 70, [('A', 'α = 50°'), ('B', 'β = 70°'), ('C', 'γ = 60°')], aussen=('C', '120°'))}],
     'fehler': 'Der Außenwinkel bei C ist nicht γ. Er liegt außen und ergänzt γ zu 180°.',
     'fehler_bild': dreieck(50, 70, [('C', 'γ, nicht γ\'')], aussen=('C', 'γ\'')),
     'regel': 'Ein ⟦Außenwinkel⟧ ist so groß wie die zwei anderen Innenwinkel zusammen. Gemeint sind die beiden, die nicht an ihm liegen.'},
    {'lernziel': 'vieleck', 'titel': 'Winkelsumme im Vieleck',
     'einstieg': 'Ein Gärtner legt ein fünfeckiges Beet an. Er zieht von einer Ecke aus Schnüre zu den anderen Ecken. So zerfällt das Beet in Dreiecke – und die ⟦Winkelsumme⟧ lässt sich zählen.',
     'woerter': [['n-Eck', 'Vieleck mit n Ecken, z. B. Fünfeck: n = 5'], ['Diagonale', 'Strecke zwischen zwei Ecken, die nicht nebeneinander liegen']],
     'bild': B_VE,
     'schritte': [{'text': 'Von A aus zeichnest du die Diagonalen nach C und D.',
                   'bild': {'linien': B_VE['linien'] + [['A', 'C', '', 'gestrichelt'], ['A', 'D', '', 'gestrichelt']]}},
                  {'text': 'Es entstehen 3 Dreiecke. Beim n-Eck sind es n − 2.'},
                  {'text': 'Jedes Dreieck hat 180°: ⟦3 · 180° = 540°⟧.'}],
     'fehler': 'Nicht n · 180° rechnen: Ein Fünfeck zerfällt nur in 3 Dreiecke, nicht in 5.',
     'regel': 'Ein n-Eck hat die Winkelsumme ⟦(n − 2) · 180°⟧. Ein Viereck hat also 360°.'},
    {'lernziel': 'figuren', 'titel': 'Winkel in Figuren bestimmen',
     'einstieg': 'Ein Dachstuhl hat viele Balken, die sich kreuzen. Die Zimmerin kennt einen Winkel und sucht die anderen. Schritt für Schritt nutzt sie bekannte ⟦Winkelsätze⟧.',
     'woerter': [['Winkelsatz', 'bewiesene Regel über Winkel, z. B. „Nebenwinkel ergeben 180°“']],
     'bild': B_FI,
     'schritte': [{'text': 'g ∥ h. Im Dreieck ABC ist der Winkel bei A 50°, bei B 60°.'},
                  {'text': 'Winkelsumme im Dreieck: ⟦γ = 180° − 50° − 60° = 70°⟧.',
                   'bild': {'winkel': [['A', 'B', 'C', '50°'], ['B', 'C', 'A', '60°'], ['C', 'A', 'B', 'γ = 70°']]}},
                  {'text': 'Links bei C bilden [CA] und g 50°: Wechselwinkel zu A.',
                   'bild': {'winkel': [['A', 'B', 'C', '50°'], ['B', 'C', 'A', '60°'], ['C', 'A', 'B', 'γ = 70°'], ['C', '_C1', 'A', '50°']]}},
                  {'text': 'Schreibe zu jedem Schritt den passenden Winkelsatz dazu.'}],
     'fehler': 'Nicht nach Augenmaß schätzen. Jeder Wert braucht einen Grund: Nebenwinkel, Scheitelwinkel, Stufen-, Wechselwinkel oder Winkelsumme.',
     'regel': 'Gehe von bekannten Winkeln aus. Nenne bei jedem Schritt den ⟦Winkelsatz⟧, den du nutzt.'},
    {'lernziel': 'beweisen', 'titel': 'Begründen mit Winkelsätzen',
     'einstieg': 'In der Mathematik baut man Sätze aufeinander auf wie Bausteine. Ganz unten liegt ein Satz, den man annimmt. Er heißt ⟦Fundamentalsatz⟧.',
     'woerter': [['Fundamentalsatz', 'Grundsatz, der nicht bewiesen, sondern vorausgesetzt wird'], ['abgeleiteter Satz', 'Satz, der mit anderen Sätzen bewiesen wird']],
     'bild': B_DP,
     'schritte': [{'text': 'Fundamentalsatz: Wechselwinkel an Parallelen sind gleich groß.'},
                  {'text': 'Daraus folgt die Winkelsumme im Dreieck: ein abgeleiteter Satz.'},
                  {'text': 'Aus der Winkelsumme folgt der ⟦Außenwinkelsatz⟧.'},
                  {'text': 'Jeder Schritt nennt den Satz, auf den er sich stützt.'}],
     'fehler': 'Einen Satz mit sich selbst begründen ist ein Zirkelschluss. Der Beweis darf nur Sätze benutzen, die vorher feststehen.',
     'regel': 'Ein Beweis ist eine Kette. Jedes Glied stützt sich auf einen ⟦vorher bekannten Satz⟧.'},
]


# ---------- Aufgaben-Generatoren (zufällig, je Stufe) ----------
def _paar(R):
    a = R.choice([x for x in range(25, 156) if x != 90])
    return a


def gen_scheitel_neben(R, st):
    a = _paar(R)
    if st == 1:
        art = R.choice(['scheitel', 'neben'])
        if art == 'scheitel':
            return Z(f'Zwei Geraden schneiden sich. Ein Winkel ist {g(a)} groß. Wie groß ist sein Scheitelwinkel?', a, f'{a}',
                     f'Scheitelwinkel sind gleich groß: {g(a)}.', 'Der Scheitelwinkel liegt gegenüber.', grafik=einfach(a, [('ro', g(a)), ('lu', '?')]))
        return Z(f'Zwei Geraden schneiden sich. Ein Winkel ist {g(a)} groß. Wie groß ist sein Nebenwinkel?', 180 - a, f'180 - {a}',
                 f'Nebenwinkel ergänzen sich zu 180°: 180° − {g(a)} = {g(180 - a)}.', 'Nebenwinkel liegen an einer Geraden nebeneinander.',
                 grafik=einfach(a, [('ro', g(a)), ('lo', '?')]))
    if st == 2:
        art = R.choice(['lage', 'unterschied', 'benennen'])
        if art == 'lage':
            ziel = R.choice(['lo', 'lu', 'ru'])
            w = {'lo': 180 - a, 'lu': a, 'ru': 180 - a}[ziel]
            return Z(f'Zwei Geraden schneiden sich. Der Winkel rechts oberhalb ist {g(a)} groß. Wie groß ist der Winkel {POS_TEXT[ziel]}?', w,
                     f'{w}', f'{"Scheitelwinkel: gleich groß" if ziel == "lu" else "Nebenwinkel: 180° − " + g(a)} = {g(w)}.',
                     'Liegt der Winkel gegenüber oder daneben?', grafik=einfach(a, [('ro', g(a)), (ziel, '?')]))
        if art == 'unterschied':
            d = R.choice(range(10, 101, 10))
            if (180 + d) % 2: d += 10
            big = (180 + d) // 2
            return Z(f'Ein Winkel ist um {g(d)} größer als sein Nebenwinkel. Wie groß ist der größere Winkel?', big, f'(180 + {d}) / 2',
                     f'x + (x − {d}°) = 180°, also 2x = {g(180 + d)} und x = {g(big)}.', 'Beide zusammen ergeben 180°.')
        nr = R.randint(1, 4)
        gegen = {1: 3, 2: 4, 3: 1, 4: 2}[nr]
        art2 = R.choice(['scheitel', 'neben'])
        if art2 == 'scheitel':
            return A(R, f'Zwei Geraden schneiden sich in S. Die vier Winkel sind mit 1 bis 4 nummeriert. Welcher Winkel ist Scheitelwinkel zu Winkel {nr}?', f'Winkel {gegen}',
                     [f'Winkel {x}' for x in (1, 2, 3, 4) if x not in (nr, gegen)] + [f'Winkel {nr}'],
                     f'Der Scheitelwinkel liegt gegenüber: Winkel {gegen}. Die beiden anderen sind Nebenwinkel von Winkel {nr}.', 'Scheitelwinkel haben nur den Punkt S gemeinsam.',
                     grafik=einfach(a, [('ro', '1'), ('lo', '2'), ('lu', '3'), ('ru', '4')]))
        nb = sorted(x for x in (1, 2, 3, 4) if x not in (nr, gegen))
        return A(R, f'Zwei Geraden schneiden sich in S. Die vier Winkel sind mit 1 bis 4 nummeriert. Welche Winkel sind Nebenwinkel von Winkel {nr}?', f'Winkel {nb[0]} und Winkel {nb[1]}',
                 [f'nur Winkel {gegen}', f'Winkel {gegen} und Winkel {nb[0]}', 'alle drei anderen'],
                 f'Nebenwinkel liegen neben Winkel {nr} an einer Geraden: Winkel {nb[0]} und {nb[1]}. Winkel {gegen} ist der Scheitelwinkel.', 'Nebenwinkel teilen sich einen Schenkel.',
                 grafik=einfach(a, [('ro', '1'), ('lo', '2'), ('lu', '3'), ('ru', '4')]))
    art = R.choice(['verh', 'drei', 'summe'])
    if art == 'verh':
        p, q = R.choice([(1, 2), (2, 3), (1, 3), (1, 4), (4, 5), (2, 7), (3, 7), (1, 5), (7, 8)])
        if 180 * p % (p + q): return gen_scheitel_neben(R, st)
        k = 180 // (p + q)
        return Z(f'Zwei Nebenwinkel verhalten sich wie {p} : {q}. Wie groß ist der kleinere?', p * k, f'180 / ({p} + {q}) * {p}',
                 f'{p} + {q} = {p + q} Teile = 180°, ein Teil = {g(k)}. Kleinerer Winkel: {p} · {g(k)} = {g(p * k)}.', 'Wie viele Teile sind es zusammen?')
    if art == 'drei':
        x, y = R.randint(20, 80), R.randint(20, 80)
        if x + y >= 160: return gen_scheitel_neben(R, st)
        return Z(f'Drei Geraden schneiden sich in einem Punkt. Zwei nebeneinander liegende Winkel sind {g(x)} und {g(y)}. Der dritte Winkel liegt daneben und ergänzt sie zu einer Geraden. Wie groß ist er?',
                 180 - x - y, f'180 - {x} - {y}', f'Drei Winkel nebeneinander an einer Geraden: 180° − {g(x)} − {g(y)} = {g(180 - x - y)}.', 'Winkel an einer Geraden ergeben 180°.')
    s = R.choice(range(60, 300, 4))
    if s >= 360 or s <= 0: return gen_scheitel_neben(R, st)
    if s > 180: s = 360 - s
    if s % 2: return gen_scheitel_neben(R, st)
    return Z(f'Zwei Geraden schneiden sich. Zwei Scheitelwinkel ergeben zusammen {g(s)}. Wie groß ist einer der beiden anderen Winkel?', 180 - s // 2,
             f'180 - {s} / 2', f'Ein Scheitelwinkel: {g(s)} : 2 = {g(s // 2)}. Sein Nebenwinkel: 180° − {g(s // 2)} = {g(180 - s // 2)}.',
             'Scheitelwinkel sind gleich groß. Die anderen beiden sind ihre Nebenwinkel.')


def gen_stufen_wechsel(R, st):
    a = _paar(R)
    if st == 1:
        ziel = R.choice(['stufe', 'wechsel'])
        if ziel == 'stufe':
            pos = R.choice(list(POS_TEXT))
            return Z(f'g ∥ h. Bei S ist der Winkel {POS_TEXT[pos]} {g(a)} groß. Wie groß ist der Winkel bei T in derselben Lage?', a, f'{a}',
                     f'Stufenwinkel an Parallelen sind gleich groß: {g(a)}.', 'Gleiche Lage an beiden Kreuzungen: Stufenwinkel.',
                     grafik=doppel(a if pos in ('ro', 'lu') else 180 - a, [('S', pos, g(a)), ('T', pos, '?')]))
        return Z(f'g ∥ h. Bei S ist der Winkel links unterhalb {g(a)} groß. Wie groß ist sein Wechselwinkel bei T (rechts oberhalb)?', a, f'{a}',
                 f'Wechselwinkel an Parallelen sind gleich groß: {g(a)}.', 'Wechselwinkel liegen über Kreuz zwischen den Parallelen.',
                 grafik=doppel(a, [('S', 'lu', g(a)), ('T', 'ro', '?')]))
    if st == 2:
        art = R.choice(['neben', 'name', 'neben'])
        if art == 'neben':
            p1, p2 = R.choice([('ro', 'lo'), ('ro', 'ru'), ('lu', 'lo'), ('lo', 'ro'), ('ru', 'lu')])
            w1 = a
            gross = {'ro': 1, 'lu': 1, 'lo': 0, 'ru': 0}
            w2 = w1 if gross[p1] == gross[p2] else 180 - w1
            zeich = a if gross[p1] else 180 - a
            return Z(f'g ∥ h. Bei S ist der Winkel {POS_TEXT[p1]} {g(w1)} groß. Wie groß ist der Winkel bei T {POS_TEXT[p2]}?', w2, f'{w2}',
                     f'Stufenwinkel: Bei T {POS_TEXT[p1]} ist auch {g(w1)}. Der gesuchte Winkel ist dessen Nebenwinkel: 180° − {g(w1)} = {g(w2)}.',
                     'Übertrage den Winkel zuerst mit dem Stufenwinkel nach T.', grafik=doppel(zeich, [('S', p1, g(w1)), ('T', p2, '?')]))
        fall = R.choice([('ro', 'ro', 'Stufenwinkel'), ('lu', 'ro', 'Wechselwinkel'), ('ru', 'lo', 'Wechselwinkel'), ('lo', 'lo', 'Stufenwinkel'), ('ro', 'lu', 'weder noch')])
        return A(R, f'g ∥ h. Wie heißen der Winkel bei S {POS_TEXT[fall[0]]} und der Winkel bei T {POS_TEXT[fall[1]]}?', fall[2],
                 [x for x in ['Stufenwinkel', 'Wechselwinkel', 'Scheitelwinkel', 'weder noch'] if x != fall[2]],
                 'Gleiche Lage: Stufenwinkel. Über Kreuz zwischen den Parallelen: Wechselwinkel. Scheitelwinkel liegen an derselben Kreuzung.',
                 'Liegen beide in gleicher Lage oder über Kreuz zwischen g und h?', grafik=doppel(60, [('S', fall[0], '1'), ('T', fall[1], '2')]))
    art = R.choice(['term', 'term2', 'kette'])
    if art in ('term', 'term2'):
        for _ in range(100):
            m1, m2 = R.randint(2, 6), R.randint(2, 6)
            if m1 == m2: continue
            x = R.randint(5, 30)
            b1 = R.randint(-20, 30)
            w = m1 * x + b1
            b2 = w - m2 * x
            if 20 <= w <= 160 and w != 90 and -40 <= b2 <= 60: break
        t1 = f'{m1}x {"+" if b1 >= 0 else "−"} {abs(b1)}' if b1 else f'{m1}x'
        t2 = f'{m2}x {"+" if b2 >= 0 else "−"} {abs(b2)}' if b2 else f'{m2}x'
        name = 'Stufenwinkel' if art == 'term' else 'Wechselwinkel'
        return Z(f'g ∥ h. Zwei {name} sind ({t1})° und ({t2})° groß. Wie groß ist jeder der beiden Winkel?', w, f'{m1} * {x} + ({b1})',
                 f'{name} an Parallelen sind gleich: {t1} = {t2}, also x = {x}. Winkel: {m1} · {x} {"+" if b1 >= 0 else "−"} {abs(b1)} = {g(w)}.',
                 'Setze beide Terme gleich. Gefragt ist der Winkel, nicht x.')
    b = R.randint(25, 85)
    return Z(f'g ∥ h. Bei S ist der Winkel links oberhalb {g(180 - b)} groß. Wie groß ist der Winkel bei T rechts oberhalb?', b, f'180 - {180 - b}',
             f'Bei S rechts oberhalb: Nebenwinkel 180° − {g(180 - b)} = {g(b)}. Stufenwinkel bei T: {g(b)}.', 'Erst Nebenwinkel bei S, dann Stufenwinkel.',
             grafik=doppel(b, [('S', 'lo', g(180 - b)), ('T', 'ro', '?')]))


def gen_parallel_pruefen(R, st):
    a = _paar(R)
    if st == 1:
        gleich = R.random() < 0.5
        b = a if gleich else a + R.choice([-3, -2, 2, 3])
        typ = R.choice(['Stufenwinkel', 'Wechselwinkel'])
        return A(R, f'Eine Gerade k schneidet g und h. Zwei {typ} sind {g(a)} und {g(b)} groß. Sind g und h parallel?',
                 'Ja' if gleich else 'Nein', ['Ja' if not gleich else 'Nein', 'Das kann man nicht entscheiden'],
                 f'{typ} {"gleich groß: parallel" if gleich else "verschieden groß: nicht parallel"} ({g(a)} und {g(b)}).',
                 f'Sind die {typ} gleich groß?')
    if st == 2:
        art = R.choice(['neben', 'dreh'])
        if art == 'neben':
            ok = R.random() < 0.5
            b = 180 - a if ok else 180 - a + R.choice([-4, 4])
            return A(R, f'k schneidet g in S und h in T. Bei S ist der Winkel rechts oberhalb {g(a)}, bei T der Winkel rechts unterhalb {g(b)}. Sind g und h parallel?',
                     'Ja' if ok else 'Nein', ['Ja' if not ok else 'Nein', 'Nur wenn beide Winkel gleich groß sind'],
                     f'Bei T rechts oberhalb ist der Nebenwinkel 180° − {g(b)} = {g(180 - b)}. {"Gleich" if ok else "Verschieden"} wie bei S ({g(a)}): '
                     f'{"parallel" if ok else "nicht parallel"}.', 'Bilde bei T den Nebenwinkel und vergleiche dann Stufenwinkel.',
                     grafik=doppel(a, [('S', 'ro', g(a)), ('T', 'ru', g(b))]))
        d = R.randint(1, 9)
        return Z(f'k schneidet g unter {g(a)} und h unter {g(a + d)} (beide Winkel rechts oberhalb). Um wie viel Grad muss man h drehen, damit h ∥ g wird?', d,
                 f'{a + d} - {a}', f'Die Stufenwinkel müssen gleich werden: {g(a + d)} − {g(a)} = {g(d)}.', 'Welcher Unterschied muss verschwinden?')
    art = R.choice(['schnitt', 'drei'])
    if art == 'schnitt':
        b = a + R.choice([x for x in range(-15, 16) if abs(x) >= 3])
        if not 20 <= b <= 160: return gen_parallel_pruefen(R, st)
        return Z(f'k schneidet g unter {g(a)} und h unter {g(b)} (beide Winkel rechts oberhalb). Unter welchem Winkel schneiden sich g und h?', abs(a - b),
                 f'abs({a} - {b})', f'Die Stufenwinkel unterscheiden sich um {g(abs(a - b))}. Um genau diesen Winkel sind g und h gegeneinander geneigt.',
                 'Stell dir das Dreieck aus g, h und k vor. Der Außenwinkelsatz hilft.')
    x = R.randint(30, 80)
    return Z(f'Die Geraden a, b und c sind parallel. Eine Gerade k schneidet a unter {g(x)}. Unter welchem spitzen Winkel schneidet k die Gerade c?', x, f'{x}',
             f'a ∥ b und b ∥ c, also a ∥ c. Stufenwinkel: {g(x)}.', 'Was folgt aus a ∥ b und b ∥ c?')


def _drei(R):
    while True:
        a, b = R.randint(20, 120), R.randint(20, 120)
        if a + b <= 160: return a, b


def gen_innenwinkelsumme(R, st):
    a, b = _drei(R)
    c = 180 - a - b
    if st == 1:
        e = R.choice(['A', 'B', 'C'])
        gegeben = {'A': (b, c), 'B': (a, c), 'C': (a, b)}[e]
        namen = {'A': ('β', 'γ', 'α'), 'B': ('α', 'γ', 'β'), 'C': ('α', 'β', 'γ')}[e]
        w = {'A': a, 'B': b, 'C': c}[e]
        mark = [(x, f'{n} = {g(v)}') for x, n, v in zip([y for y in 'ABC' if y != e], namen[:2], gegeben)] + [(e, '?')]
        return Z(f'In einem Dreieck ist {namen[0]} = {g(gegeben[0])} und {namen[1]} = {g(gegeben[1])}. Wie groß ist {namen[2]}?', w,
                 f'180 - {gegeben[0]} - {gegeben[1]}', f'{namen[2]} = 180° − {g(gegeben[0])} − {g(gegeben[1])} = {g(w)}.', 'Die Winkelsumme ist 180°.',
                 grafik=dreieck(a, b, mark))
    if st == 2:
        art = R.choice(['doppelt', 'beweis', 'gleich'])
        if art == 'doppelt':
            k = R.choice([2, 3, 4])
            gg = R.choice(range(30, 120, 2))
            if (180 - gg) % (k + 1): return gen_innenwinkelsumme(R, st)
            x = (180 - gg) // (k + 1)
            return Z(f'In einem Dreieck ist β {k}-mal so groß wie α, und γ = {g(gg)}. Wie groß ist α?', x, f'(180 - {gg}) / ({k} + 1)',
                     f'α + {k}α + {g(gg)} = 180°, also {k + 1}α = {g(180 - gg)} und α = {g(x)}.', 'Schreibe β mit α und nutze die Winkelsumme.')
        if art == 'gleich':
            x = R.choice(range(20, 80, 2))
            return Z(f'Ein Dreieck hat zwei gleich große Winkel von je {g(x)}. Wie groß ist der dritte Winkel?', 180 - 2 * x, f'180 - 2 * {x}',
                     f'180° − 2 · {g(x)} = {g(180 - 2 * x)}.', 'Beide gleichen Winkel abziehen.')
        v = R.choice(['links', 'rechts', 'mitte', 'gerade', 'hilfslinie'])
        if v in ('links', 'rechts'):
            return A(R, f'Beweis der Winkelsumme: Durch C ist die Parallele p zu [AB] gezeichnet. Warum ist der Winkel {v} von C zwischen p und der Dreiecksseite so groß wie {"α" if v == "links" else "β"}?',
                     'Er ist Wechselwinkel an den Parallelen p und AB.', ['Er ist Scheitelwinkel.', 'Er ist Nebenwinkel.', 'Man sieht es in der Zeichnung.'],
                     f'p ∥ AB. Die Seite [{"AC" if v == "links" else "BC"}] schneidet beide Parallelen; der Winkel bei C und {"α" if v == "links" else "β"} liegen über Kreuz: Wechselwinkel.',
                     'Welche Winkel an Parallelen liegen über Kreuz?', grafik=B_DP)
        if v == 'mitte':
            return A(R, 'Beweis der Winkelsumme: Auf der Parallelen p durch C liegen drei Winkel nebeneinander. Welcher liegt in der Mitte?', 'γ',
                     ['α', 'β', 'ein rechter Winkel'], 'Links liegt der Wechselwinkel zu α, rechts der zu β, dazwischen der Dreieckswinkel γ.', 'Welcher Winkel gehört direkt zum Dreieck bei C?', grafik=B_DP)
        if v == 'gerade':
            return A(R, 'Beweis der Winkelsumme: Warum ergeben die drei Winkel an C auf der Parallelen p zusammen 180°?', 'Sie liegen nebeneinander auf einer Geraden.',
                     ['Weil jedes Dreieck 180° hat.', 'Weil es Scheitelwinkel sind.', 'Weil p parallel zu [AB] ist.'],
                     'Winkel, die auf einer Geraden nebeneinander liegen, bilden einen gestreckten Winkel: 180°. Die Winkelsumme darf man hier nicht benutzen – sie soll ja erst bewiesen werden.',
                     'Was ist ein gestreckter Winkel?', grafik=B_DP)
        return A(R, 'Welche Hilfslinie braucht man für den Beweis der Winkelsumme im Dreieck ABC?', 'die Parallele zu [AB] durch C',
                 ['die Mittelsenkrechte von [AB]', 'die Winkelhalbierende von γ', 'eine Senkrechte zu [AB] durch A'],
                 'Erst mit der Parallelen entstehen Wechselwinkel, die α und β nach C bringen.', 'Welche Winkelsätze brauchen Parallelen?')
    art = R.choice(['terme', 'rechtwinklig', 'verh'])
    if art == 'terme':
        for _ in range(200):
            x = R.randint(10, 40)
            m1, b1 = R.randint(1, 3), R.randint(-10, 30)
            m2, b2 = R.randint(1, 3), R.randint(-10, 30)
            w1, w2 = m1 * x + b1, m2 * x + b2
            w3 = 180 - w1 - w2
            if min(w1, w2, w3) >= 15: break
        f = lambda m, bb: (f'{m if m > 1 else ""}x' + (f' + {bb}' if bb > 0 else (f' − {-bb}' if bb < 0 else '')))
        return Z(f'Ein Dreieck hat die Winkel α = ({f(m1, b1)})°, β = ({f(m2, b2)})° und γ = {g(w3)}. Wie groß ist x?', x, f'(180 - {w3} - ({b1}) - ({b2})) / ({m1} + {m2})',
                 f'{f(m1, b1)} + {f(m2, b2)} + {w3} = 180, also {m1 + m2}x = {180 - w3 - b1 - b2} und x = {x}.', 'Alle drei Winkel zusammen ergeben 180°.')
    if art == 'rechtwinklig':
        d = R.choice(range(4, 60, 2))
        return Z(f'Ein Dreieck ist rechtwinklig. Ein spitzer Winkel ist um {g(d)} größer als der andere. Wie groß ist der größere spitze Winkel?', (90 + d) // 2,
                 f'(90 + {d}) / 2', f'Die spitzen Winkel ergeben 90°: x + (x − {d}°) = 90°, x = {g((90 + d) // 2)}.', 'Die beiden spitzen Winkel ergeben zusammen 90°.')
    p, q, r = R.choice([(1, 2, 3), (2, 3, 4), (1, 1, 4), (3, 4, 5), (1, 2, 6), (2, 3, 5), (1, 3, 5), (4, 5, 6)])
    k = Fr(180, p + q + r)
    if k.denominator != 1: return gen_innenwinkelsumme(R, st)
    return Z(f'Die Winkel eines Dreiecks verhalten sich wie {p} : {q} : {r}. Wie groß ist der größte Winkel?', r * k, f'180 / ({p} + {q} + {r}) * {r}',
             f'{p + q + r} Teile = 180°, ein Teil = {g(k)}. Größter Winkel: {r} · {g(k)} = {g(r * k)}.', 'Wie viele gleiche Teile sind es zusammen?')


def gen_aussenwinkel(R, st):
    a, b = _drei(R)
    c = 180 - a - b
    if st == 1:
        if R.random() < 0.5:
            return Z(f'In einem Dreieck ist γ = {g(c)}. Wie groß ist der Außenwinkel bei C?', 180 - c, f'180 - {c}',
                     f'Der Außenwinkel ist Nebenwinkel von γ: 180° − {g(c)} = {g(180 - c)}.', 'Außenwinkel und Innenwinkel liegen nebeneinander.',
                     grafik=dreieck(a, b, [('C', f'γ = {g(c)}')], aussen=('C', '?')))
        return Z(f'In einem Dreieck ist α = {g(a)} und β = {g(b)}. Wie groß ist der Außenwinkel bei C?', a + b, f'{a} + {b}',
                 f'Außenwinkelsatz: Außenwinkel bei C = α + β = {g(a + b)}.', 'Welche Innenwinkel liegen nicht bei C?',
                 grafik=dreieck(a, b, [('A', g(a)), ('B', g(b))], aussen=('C', '?')))
    if st == 2:
        if R.random() < 0.5:
            return Z(f'Der Außenwinkel bei B ist {g(180 - b)}, und α = {g(a)}. Wie groß ist γ?', c, f'(180 - {b}) - {a}',
                     f'Außenwinkel bei B = α + γ. Also γ = {g(180 - b)} − {g(a)} = {g(c)}.', 'Der Außenwinkel bei B ist so groß wie α und γ zusammen.',
                     grafik=dreieck(a, b, [('A', g(a)), ('C', '?')], aussen=('B', g(180 - b))))
        x = R.randint(20, 75)
        return Z(f'Ein gleichschenkliges Dreieck hat an der Spitze den Außenwinkel {g(2 * x)}. Wie groß ist ein Basiswinkel?', x, f'2 * {x} / 2',
                 f'Der Außenwinkel an der Spitze ist die Summe der beiden gleichen Basiswinkel: {g(2 * x)} : 2 = {g(x)}.', 'Außenwinkelsatz und gleiche Basiswinkel.')
    art = R.choice(['summe', 'zwei', 'term'])
    if art == 'summe':
        return Z(f'Bei einem Dreieck sind zwei Außenwinkel {g(180 - a)} und {g(180 - b)}. Wie groß ist der dritte Außenwinkel?', 180 - c,
                 f'360 - {180 - a} - {180 - b}', f'Die drei Außenwinkel ergeben 360°: 360° − {g(180 - a)} − {g(180 - b)} = {g(180 - c)}.',
                 'Rechne mit den Innenwinkeln nach oder nutze die Summe der Außenwinkel.')
    if art == 'zwei':
        return Z(f'Die Außenwinkel bei A und B sind {g(180 - a)} und {g(180 - b)}. Wie groß ist γ?', c, f'180 - (180 - {180 - a}) - (180 - {180 - b})',
                 f'α = 180° − {g(180 - a)} = {g(a)}, β = 180° − {g(180 - b)} = {g(b)}. γ = 180° − {g(a)} − {g(b)} = {g(c)}.', 'Bestimme erst die Innenwinkel bei A und B.')
    x = R.randint(10, 35)
    w1, w2 = 2 * x, x + 20
    return Z(f'Im Dreieck ist α = ({"2x"})° und β = (x + 20)°. Der Außenwinkel bei C ist {g(w1 + w2)}. Wie groß ist α?', w1, f'2 * ({w1 + w2} - 20) / 3',
             f'Außenwinkel bei C = α + β: 2x + x + 20 = {w1 + w2}, also 3x = {w1 + w2 - 20}, x = {x}. α = {g(w1)}.', 'Außenwinkelsatz, dann Gleichung lösen.')


def gen_vieleck(R, st):
    if st == 1:
        if R.random() < 0.5:
            a, b, c = R.randint(50, 130), R.randint(50, 130), R.randint(50, 130)
            d = 360 - a - b - c
            if not 30 <= d <= 170: return gen_vieleck(R, st)
            return Z(f'In einem Viereck ist α = {g(a)}, β = {g(b)} und γ = {g(c)}. Wie groß ist δ?', d, f'360 - {a} - {b} - {c}',
                     f'Winkelsumme im Viereck 360°: 360° − {g(a)} − {g(b)} − {g(c)} = {g(d)}.', 'Ein Viereck zerfällt in zwei Dreiecke.')
        n = R.randint(5, 12)
        return Z(f'Wie groß ist die Winkelsumme in einem {n}-Eck?', (n - 2) * 180, f'({n} - 2) * 180', f'({n} − 2) · 180° = {g((n - 2) * 180)}.',
                 'Wie viele Dreiecke entstehen von einer Ecke aus?')
    if st == 2:
        art = R.choice(['regel', 'dreiecke', 'fehlend5'])
        if art == 'regel':
            n = R.choice([5, 6, 8, 9, 10, 12, 15, 18, 20])
            w = Fr((n - 2) * 180, n)
            return Z(f'Wie groß ist jeder Innenwinkel eines regelmäßigen {n}-Ecks?', w, f'({n} - 2) * 180 / {n}',
                     f'Winkelsumme ({n} − 2) · 180° = {g((n - 2) * 180)}, verteilt auf {n} gleiche Winkel: {g(w)}.', 'Erst die Winkelsumme, dann gleichmäßig verteilen.')
        if art == 'dreiecke':
            n = R.randint(6, 14)
            return Z(f'Von einer Ecke eines {n}-Ecks zieht man alle Diagonalen. In wie viele Dreiecke wird das {n}-Eck zerlegt?', n - 2, f'{n} - 2',
                     f'Die Ecke selbst und ihre beiden Nachbarn liefern keine Diagonale: {n} − 3 Diagonalen, {n} − 2 Dreiecke.', 'Probiere es mit einem Fünfeck aus.', einheit=None)
        ws = [R.randint(85, 140) for _ in range(4)]
        f = 540 - sum(ws)
        if not 60 <= f <= 170: return gen_vieleck(R, st)
        return Z(f'Ein Fünfeck hat die Winkel {", ".join(g(x) for x in ws)} und einen fünften Winkel. Wie groß ist er?', f, f'540 - {" - ".join(map(str, ws))}',
                 f'Winkelsumme im Fünfeck: 3 · 180° = 540°. 540° − {g(sum(ws))} = {g(f)}.', 'Winkelsumme im Fünfeck: (5 − 2) · 180°.')
    art = R.choice(['rueck', 'summe_n', 'viereck_term'])
    if art == 'rueck':
        n = R.choice([5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36])
        w = Fr((n - 2) * 180, n)
        if w.denominator != 1: return gen_vieleck(R, st)
        return Z(f'Jeder Innenwinkel eines regelmäßigen Vielecks ist {g(w)} groß. Wie viele Ecken hat es?', n, f'360 / (180 - {w})',
                 f'(n − 2) · 180° = n · {g(w)}, also 180n − 360 = {w}n, {180 - w}n = 360 und n = {n}.', 'Stelle eine Gleichung mit der Winkelsumme auf.', einheit=None)
    if art == 'summe_n':
        n = R.randint(6, 20)
        return Z(f'Ein Vieleck hat die Winkelsumme {g((n - 2) * 180)}. Wie viele Ecken hat es?', n, f'{(n - 2) * 180} / 180 + 2',
                 f'(n − 2) · 180° = {g((n - 2) * 180)}, also n − 2 = {n - 2} und n = {n}.', 'Teile durch 180° und denke an das „− 2“.', einheit=None)
    x = R.randint(20, 50)
    a, b, c = x, 2 * x, 3 * x
    d = 360 - a - b - c
    if d <= 20: return gen_vieleck(R, st)
    return Z(f'In einem Viereck ist β doppelt so groß wie α, γ dreimal so groß wie α, und δ = {g(d)}. Wie groß ist α?', x, f'(360 - {d}) / 6',
             f'α + 2α + 3α + {g(d)} = 360°, also 6α = {g(360 - d)} und α = {g(x)}.', 'Schreibe alle Winkel mit α.')


def gen_figuren(R, st):
    if st == 1:
        a, b = _drei(R)
        if R.random() < 0.5:
            return Z(f'g ∥ h. Die Ecke C eines Dreiecks liegt auf g, A und B auf h. Bei A ist der Innenwinkel {g(a)}. Welchen Winkel bildet [CA] links bei C mit g?', a, f'{a}',
                     f'Wechselwinkel an Parallelen: {g(a)}.', 'Die Seite [CA] schneidet beide Parallelen.')
        x = R.randint(40, 140)
        return Z(f'In einem Parallelogramm ist ein Winkel {g(x)} groß. Wie groß ist der Nachbarwinkel an derselben Seite?', 180 - x, f'180 - {x}',
                 f'Gegenüberliegende Seiten sind parallel. Winkel an derselben Seite ergänzen sich zu 180°: {g(180 - x)}.', 'Stufenwinkel und Nebenwinkel.')
    if st == 2:
        art = R.choice(['trapez', 'rauten', 'dreieck_par'])
        if art == 'trapez':
            a = R.randint(40, 85)
            return Z(f'Ein Trapez ABCD hat AB ∥ CD. Der Winkel bei A ist {g(a)}. Wie groß ist der Winkel bei D?', 180 - a, f'180 - {a}',
                     f'[AD] schneidet die Parallelen AB und CD. α und δ ergänzen sich zu 180°: {g(180 - a)}.', 'Verlängere [AB] über A hinaus: Stufenwinkel und Nebenwinkel.')
        if art == 'rauten':
            a = R.choice(range(40, 140, 2))
            return Z(f'In einer Raute ist ein Winkel {g(a)} groß. Welchen Winkel bildet die Diagonale durch diese Ecke mit einer Seite?', a // 2, f'{a} / 2',
                     f'Die Diagonale ist Symmetrieachse und halbiert den Winkel: {g(a // 2)}.', 'Was macht eine Symmetrieachse mit dem Eckwinkel?')
        a, b = _drei(R)
        return Z(f'g ∥ h. Die Ecke C eines Dreiecks liegt auf g, A und B auf h. Bei C bildet [CA] mit g den Winkel {g(a)} (links), [CB] mit g den Winkel {g(b)} (rechts). Wie groß ist der Innenwinkel bei C?',
                 180 - a - b, f'180 - {a} - {b}', f'An C liegen auf g drei Winkel nebeneinander: 180° − {g(a)} − {g(b)} = {g(180 - a - b)}.', 'Winkel an einer Geraden ergeben 180°.')
    art = R.choice(['kette', 'gleichsch', 'dia'])
    if art == 'kette':
        a, b = R.randint(25, 70), R.randint(25, 70)
        return Z(f'g ∥ h. Ein Weg geht von A auf g zu einem Punkt P zwischen den Geraden und weiter zu B auf h. Bei A bildet der Weg mit g den Winkel {g(a)}, bei B mit h den Winkel {g(b)} (beide auf der Seite von P). Wie groß ist der Winkel bei P?',
                 a + b, f'{a} + {b}', f'Hilfslinie durch P parallel zu g: Sie teilt den Winkel bei P in zwei Wechselwinkel {g(a)} und {g(b)}. Zusammen {g(a + b)}.',
                 'Zeichne durch P eine Parallele zu g.')
    if art == 'gleichsch':
        x = R.choice(range(30, 80, 2))
        return Z(f'Im gleichschenkligen Dreieck ABC (AC = BC) ist der Basiswinkel {g(x)}. Durch C geht die Parallele zu [AB]. Welchen Winkel bildet [CB] mit dieser Parallelen (rechts von C)?',
                 x, f'{x}', f'Wechselwinkel zu β an den Parallelen: {g(x)}.', 'Die Seite [CB] schneidet beide Parallelen.')
    a, b = R.randint(20, 60), R.randint(20, 60)
    return Z(f'Im Parallelogramm ABCD bildet die Diagonale [AC] mit [AB] den Winkel {g(a)} und mit [AD] den Winkel {g(b)}. Wie groß ist der Winkel ∠ACD?', a,
             f'{a}', f'AB ∥ DC und [AC] schneidet beide: ∠ACD ist Wechselwinkel zu ∠CAB = {g(a)}.', 'Welche Seiten sind parallel, und welche Linie schneidet sie?')


BEGR = [('Nebenwinkel ergänzen sich zu 180°.', 'Zwei Winkel liegen an einer Geraden nebeneinander.'),
        ('Scheitelwinkel sind gleich groß.', 'Zwei Winkel liegen sich an einer Kreuzung gegenüber.'),
        ('Stufenwinkel an Parallelen sind gleich groß.', 'Zwei Winkel liegen an zwei Kreuzungen mit Parallelen in gleicher Lage.'),
        ('Wechselwinkel an Parallelen sind gleich groß.', 'Zwei Winkel liegen an Parallelen über Kreuz zwischen den Geraden.'),
        ('Die Winkelsumme im Dreieck ist 180°.', 'Die drei Innenwinkel eines Dreiecks werden addiert.'),
        ('Ein Außenwinkel ist so groß wie die beiden nicht anliegenden Innenwinkel.', 'Der Außenwinkel eines Dreiecks wird mit zwei Innenwinkeln verglichen.')]


def gen_beweisen(R, st):
    if st == 1:
        i = R.randrange(len(BEGR))
        satz, lage = BEGR[i]
        return A(R, f'Welcher Winkelsatz passt zu dieser Lage? {lage}', satz, [s for j, (s, _) in enumerate(BEGR) if j != i][:3] if R.random() < 0.5 else
                 R.sample([s for j, (s, _) in enumerate(BEGR) if j != i], 3), f'Passend ist: {satz}', 'Wo liegen die Winkel: an einer oder an zwei Kreuzungen?')
    if st == 2:
        art = R.choice(['grund', 'begruendung', 'zirkel'])
        if art == 'grund':
            return A(R, 'Welche Aussage wird beim Beweis der Winkelsumme im Dreieck vorausgesetzt (Fundamentalsatz)?', 'Wechselwinkel an Parallelen sind gleich groß.',
                     R.sample(['Die Winkelsumme im Dreieck ist 180°.', 'Ein Außenwinkel ist so groß wie die beiden nicht anliegenden Innenwinkel.',
                               'Die Winkelsumme im Viereck ist 360°.', 'Jedes n-Eck hat (n − 2) · 180°.'], 3),
                     'Der Beweis der Winkelsumme stützt sich auf Wechselwinkel an Parallelen. Die anderen Sätze werden erst daraus abgeleitet.', 'Was steht am Anfang der Kette?')
        if art == 'zirkel':
            return A(R, 'Jemand begründet „Die Winkelsumme im Dreieck ist 180°“ so: „Weil der Außenwinkel so groß ist wie die beiden anderen Innenwinkel.“ Was ist das Problem?',
                     'Der Außenwinkelsatz wird selbst mit der Winkelsumme bewiesen – ein Zirkelschluss.',
                     ['Kein Problem, das ist ein gültiger Beweis.', 'Der Außenwinkelsatz ist falsch.', 'Man muss die Winkel zuerst messen.'],
                     'Der Außenwinkelsatz folgt aus der Winkelsumme. Man darf ihn nicht benutzen, um die Winkelsumme zu beweisen.', 'Woraus wurde der Außenwinkelsatz bewiesen?')
        a = _paar(R)
        v = R.choice(['stufe', 'scheitel', 'neben'])
        if v == 'stufe':
            return A(R, f'g ∥ h. Jemand schreibt: „Der Winkel bei T rechts oberhalb ist {g(a)}, weil bei S rechts oberhalb {g(a)} steht.“ Welche Begründung muss genannt werden?',
                     'Stufenwinkel an Parallelen sind gleich groß.', ['Scheitelwinkel sind gleich groß.', 'Nebenwinkel ergänzen sich zu 180°.', 'Das sieht man in der Zeichnung.'],
                     'Beide Winkel liegen an zwei Kreuzungen in gleicher Lage: Stufenwinkel. Das gilt nur, weil g ∥ h.', 'Liegen die Winkel an einer oder an zwei Kreuzungen?',
                     grafik=doppel(a, [('S', 'ro', g(a)), ('T', 'ro', g(a))]))
        if v == 'scheitel':
            return A(R, f'Jemand schreibt: „Der Winkel links unterhalb ist {g(a)}, weil der Winkel rechts oberhalb an derselben Kreuzung {g(a)} ist.“ Welche Begründung muss genannt werden?',
                     'Scheitelwinkel sind gleich groß.', ['Stufenwinkel an Parallelen sind gleich groß.', 'Nebenwinkel ergänzen sich zu 180°.', 'Wechselwinkel an Parallelen sind gleich groß.'],
                     'Beide Winkel liegen sich an derselben Kreuzung gegenüber: Scheitelwinkel.', 'Wie viele Kreuzungen sind beteiligt?', grafik=einfach(a, [('ro', g(a)), ('lu', g(a))]))
        return A(R, f'Jemand schreibt: „Der Winkel links oberhalb ist {g(180 - a)}, weil der Winkel rechts oberhalb {g(a)} ist.“ Welche Begründung muss genannt werden?',
                 'Nebenwinkel ergänzen sich zu 180°.', ['Scheitelwinkel sind gleich groß.', 'Stufenwinkel an Parallelen sind gleich groß.', 'Die Winkelsumme im Dreieck ist 180°.'],
                 f'Beide liegen an einer Geraden nebeneinander: {g(a)} + {g(180 - a)} = 180°.', 'Liegen die Winkel nebeneinander oder gegenüber?', grafik=einfach(a, [('ro', g(a)), ('lo', g(180 - a))]))
    art = R.choice(['gegen', 'stumpf', 'viereck', 'fuenfeck', 'aussen', 'umkehr', 'messung'])
    if art == 'gegen':
        return A(R, 'Behauptung: „Wenn zwei Winkel zusammen 180° ergeben, sind sie Nebenwinkel.“ Was stimmt?', 'Falsch: Auch zwei Winkel an verschiedenen Stellen können zusammen 180° ergeben.',
                 ['Richtig, das ist die Definition.', 'Richtig, denn Nebenwinkel ergeben 180°.', 'Falsch: Nebenwinkel ergeben 360°.'],
                 'Gegenbeispiel: Im Parallelogramm ergeben zwei Nachbarwinkel 180°, liegen aber an verschiedenen Ecken. Die Umkehrung eines Satzes muss eigens geprüft werden.',
                 'Suche ein Gegenbeispiel.')
    if art == 'stumpf':
        return A(R, 'Warum kann ein Dreieck höchstens einen stumpfen Winkel haben?', 'Zwei stumpfe Winkel wären zusammen schon mehr als 180°.',
                 ['Weil stumpfe Winkel immer bei C liegen.', 'Weil man es so zeichnet.', 'Das stimmt nicht, es können zwei sein.'],
                 'Ein stumpfer Winkel ist größer als 90°. Zwei davon ergäben mehr als 180° – mehr als die ganze Winkelsumme.', 'Denke an die Winkelsumme.')
    if art == 'viereck':
        return A(R, 'Wie beweist man, dass die Winkelsumme im Viereck 360° ist?', 'Eine Diagonale teilt das Viereck in zwei Dreiecke: 2 · 180° = 360°.',
                 ['Man misst vier Winkel und addiert.', 'Ein Viereck hat 4 rechte Winkel.', 'Mit dem Außenwinkelsatz: 4 · 90°.'],
                 'Mit der Diagonale entstehen zwei Dreiecke. Ihre Winkel bilden zusammen genau die vier Viereckswinkel.', 'Welche Hilfslinie zerlegt das Viereck?')
    if art == 'fuenfeck':
        return A(R, 'Wie viele Dreiecke braucht man, um die Winkelsumme 540° im Fünfeck zu begründen, wenn man alle Diagonalen von einer Ecke aus zieht?', '3',
                 ['5', '2', '4'], 'Von einer Ecke gehen 2 Diagonalen aus; sie zerlegen das Fünfeck in 3 Dreiecke: 3 · 180° = 540°.', 'Zeichne ein Fünfeck und zähle.')
    if art == 'aussen':
        return A(R, 'Aus welchen Sätzen folgt der Außenwinkelsatz („Außenwinkel = Summe der beiden nicht anliegenden Innenwinkel“)?', 'aus der Winkelsumme im Dreieck und dem Satz über Nebenwinkel',
                 ['nur aus dem Satz über Scheitelwinkel', 'aus dem Satz über Stufenwinkel allein', 'aus gar keinem, er wird vorausgesetzt'],
                 'Außenwinkel = 180° − γ (Nebenwinkel) und 180° − γ = α + β (Winkelsumme). Also Außenwinkel = α + β.', 'Schreibe den Außenwinkel zuerst als Nebenwinkel.')
    if art == 'umkehr':
        return A(R, 'Wozu braucht man die Umkehrung „Sind Stufenwinkel gleich groß, dann sind die Geraden parallel“?', 'um nachzuweisen, dass zwei Geraden parallel sind',
                 ['um Winkel an Parallelen zu berechnen', 'um zu zeigen, dass Scheitelwinkel gleich sind', 'gar nicht, sie ist dasselbe wie der Satz'],
                 'Der Satz schließt von „parallel“ auf „gleiche Winkel“. Die Umkehrung schließt von „gleiche Winkel“ auf „parallel“ – damit prüft man Parallelität.',
                 'In welche Richtung schließt die Umkehrung?')
    return A(R, 'Jemand misst in einem gezeichneten Dreieck die Winkelsumme 179°. Widerlegt das den Satz über die Winkelsumme?', 'Nein: Messungen sind ungenau, der Satz ist bewiesen.',
             ['Ja: Ein Gegenbeispiel genügt.', 'Ja: Dann gilt der Satz nur für manche Dreiecke.', 'Nein: Die Winkelsumme ist ohnehin 179°.'],
             'Zeichnen und Messen haben kleine Fehler. Ein bewiesener Satz gilt für jedes Dreieck; ein Gegenbeispiel müsste exakt sein, nicht gemessen.', 'Wie genau ist eine Messung mit dem Geodreieck?')


GEN = {'scheitel_neben': gen_scheitel_neben, 'stufen_wechsel': gen_stufen_wechsel, 'parallel_pruefen': gen_parallel_pruefen,
       'innenwinkelsumme': gen_innenwinkelsumme, 'aussenwinkel': gen_aussenwinkel, 'vieleck': gen_vieleck, 'figuren': gen_figuren, 'beweisen': gen_beweisen}


# ---------- Feste Stufe-3-Aufgaben: je Lernkarte 2 nach Prüfungsvorbild, 1 Knobelaufgabe ----------
def fest(R):
    F = {}
    F['scheitel_neben'] = [
        Z('Drei Geraden schneiden sich in einem Punkt und bilden sechs Winkel. Zwei benachbarte Winkel sind 40° und 65° groß. Wie groß ist der größte der sechs Winkel?',
          75, '180 - 40 - 65', 'Drei benachbarte Winkel füllen eine Gerade: 180° − 40° − 65° = 75°. Die anderen drei sind Scheitelwinkel (40°, 65°, 75°). Größter: 75°.',
          'Drei nebeneinander liegende Winkel ergeben 180°. Die übrigen drei sind Scheitelwinkel.', art=P),
        A(R, 'Warum sind Scheitelwinkel immer gleich groß?', 'Beide ergänzen denselben Nebenwinkel zu 180°.',
          ['Weil sie gegenüberliegen und deshalb gleich aussehen.', 'Weil alle Winkel an einer Kreuzung gleich groß sind.', 'Weil man es messen kann.'],
          'α + β = 180° und γ + β = 180° (β ist Nebenwinkel von beiden). Also α = 180° − β = γ.', 'Suche einen Winkel, der neben beiden liegt.', art=P),
        Z('Ein Winkel an einer Kreuzung ist viermal so groß wie sein Nebenwinkel. Wie groß ist sein Scheitelwinkel?', 144, '4 * 180 / 5',
          'x + 4x = 180°, also x = 36°. Der große Winkel ist 144°; sein Scheitelwinkel ist ebenfalls 144°.', 'Erst die Gleichung mit dem Nebenwinkel, dann den Scheitelwinkel.', art=K)]
    F['stufen_wechsel'] = [
        Z('Eine Rampe steigt um 38° gegen die Waagrechte an. Der Handlauf ist parallel zur Rampe, die Pfosten stehen senkrecht. Wie groß ist der spitze Winkel zwischen Pfosten und Handlauf?',
          52, '90 - 38', 'Pfosten und Waagrechte bilden 90°. Der Handlauf ist um 38° geneigt (Stufenwinkel zur Rampe). Spitzer Winkel zum Pfosten: 90° − 38° = 52°.',
          'Der Pfosten steht senkrecht auf der Waagrechten.', art=P),
        Z('g ∥ h. Ein Dreieck hat die Ecke C auf g und die Ecken A und B auf h. Der Innenwinkel bei A ist 55°, bei B 70°. Welchen Winkel bildet [CB] rechts bei C mit g?', 70, '70',
          '[CB] schneidet die Parallelen g und h. Der Winkel rechts bei C und β = 70° sind Wechselwinkel.', 'Welche Seite schneidet beide Parallelen?', art=P),
        Z('g ∥ h. Ein Weg führt von A auf g zu einem Punkt P zwischen den Geraden und weiter zu B auf h. Bei A ist der Winkel 32°, bei B 51° (siehe Bild). Wie groß ist der Winkel bei P?',
          83, '32 + 51', 'Hilfslinie durch P parallel zu g: Sie teilt den Winkel bei P in die Wechselwinkel 32° und 51°. Zusammen 83°.',
          'Zeichne durch P eine dritte Parallele.', art=K,
          grafik={'typ': 'figur', 'punkte': {'_g1': [-1, 4], '_g2': [6, 4], '_h1': [-1, 0], '_h2': [6, 0], 'A': [0, 4], 'P': [3, 2], 'B': [0, 0]},
                  'linien': [['_g1', '_g2', 'g'], ['_h1', '_h2', 'h'], ['A', 'P'], ['P', 'B']],
                  'winkel': [['A', 'P', '_g2', '32°'], ['B', '_h2', 'P', '51°'], ['P', 'A', 'B', '?']]})]
    F['parallel_pruefen'] = [
        A(R, 'k schneidet g in S und h in T. Bei S ist der Winkel rechts oberhalb 68°, bei T der Winkel links unterhalb 66°. Welche Aussage ist richtig begründet?',
          'g und h sind nicht parallel, denn die Wechselwinkel wären sonst gleich groß.',
          ['g und h sind parallel, denn 68° und 66° sind fast gleich.', 'g und h sind parallel, denn beide Winkel sind spitz.', 'Das lässt sich ohne Längen nicht entscheiden.'],
          'Bei S links unterhalb ist der Scheitelwinkel 68°. Mit dem Winkel bei T rechts oberhalb (66°, Scheitelwinkel) bildet er ein Wechselwinkelpaar. 68° ≠ 66°: nicht parallel.',
          'Bringe beide Winkel mit Scheitelwinkeln in die Lage von Wechselwinkeln.', art=P, grafik=doppel(68, [('S', 'ro', '68°'), ('T', 'lu', '66°')], parallel=False)),
        Z('Die Geraden g und h schneiden sich außerhalb des Blattes. Eine Gerade k schneidet g unter 75° und h unter 68° (beide Winkel rechts oberhalb). Unter welchem Winkel schneiden sich g und h?',
          7, '75 - 68', 'Wären g und h parallel, wären die Stufenwinkel gleich. Der Unterschied 75° − 68° = 7° ist der Winkel, unter dem sich g und h schneiden (Außenwinkelsatz).',
          'Denke dir das Dreieck aus g, h und k.', art=P),
        Z('Es gilt a ∥ b, b steht senkrecht auf c, und c ∥ d. Eine Gerade k schneidet a unter 35°. Unter welchem spitzen Winkel schneidet k die Gerade d?', 55, '90 - 35',
          'Aus a ∥ b und b ⟂ c folgt a ⟂ c, also a ⟂ d. Steht d senkrecht auf a, trifft k die Gerade d unter 90° − 35° = 55°.',
          'Was gilt für a und d? Zeichne eine Skizze.', art=K)]
    F['innenwinkelsumme'] = [
        A(R, 'Kann der größte Innenwinkel eines Dreiecks 58° groß sein?', 'Nein: Alle Winkel wären höchstens 58°, zusammen höchstens 174°.',
          ['Ja, zum Beispiel 58°, 58° und 64°.', 'Ja, jeder spitze Winkel ist möglich.', 'Nein, der größte Winkel muss stumpf sein.'],
          'Wenn 58° der größte Winkel ist, sind alle höchstens 58°: 3 · 58° = 174° < 180°. Der größte Winkel ist immer mindestens 60°.',
          'Was ist die größtmögliche Summe, wenn kein Winkel über 58° liegt?', art=P),
        A(R, 'Im Dreieck ABC teilt die Strecke [CM] den Winkel γ in δ und ε. Es gilt α = δ und β = ε. Welche Rechnung zeigt γ = 90°?',
          'α + β + γ = 180° und α + β = δ + ε = γ, also 2γ = 180°.', ['α + β = 90°, weil zwei Winkel immer 90° ergeben.', 'δ + ε = 180°, also γ = 180°.', 'γ = δ · ε = 90°.'],
          'Ersetzt man α + β durch δ + ε, also durch γ, ergibt die Winkelsumme γ + γ = 180°, also γ = 90°.', 'Ersetze in der Winkelsumme α + β.', art=P),
        A(R, 'Ein Dreieck wird durch eine Strecke von einer Ecke zur Gegenseite in zwei Dreiecke geteilt. Jemand sagt: „Dann hat das große Dreieck 2 · 180° = 360°.“ Was ist falsch?',
          'Die zwei neuen Winkel an der Gegenseite (zusammen 180°) gehören nicht zum großen Dreieck: 360° − 180° = 180°.',
          ['Nichts, große Dreiecke haben mehr Winkelsumme.', 'Man muss 3 · 180° rechnen.', 'Die Teildreiecke haben je 90°.'],
          'Die beiden Teildreiecke haben zusammen 360°. Davon liegen 180° als Nebenwinkel auf der Gegenseite und zählen nicht zum großen Dreieck.',
          'Welche Winkel gehören zu den Teildreiecken, aber nicht zum großen Dreieck?', art=K)]
    F['aussenwinkel'] = [
        Z('Im Kreis um M ist [AB] ein Durchmesser, C liegt auf dem Kreis. ∠BAC = 34°. Wie groß ist ∠BMC?', 68, '2 * 34',
          'MA = MC (Radien): Dreieck AMC ist gleichschenklig, also ∠MCA = 34°. ∠BMC ist Außenwinkel des Dreiecks AMC: 34° + 34° = 68°.',
          'Welches Dreieck ist gleichschenklig? ∠BMC ist dort ein Außenwinkel.', art=P),
        Z('Bei einem Dreieck ABC ist der Außenwinkel bei B 128° und der Außenwinkel bei C 117°. Wie groß ist α?', 65, '180 - (180 - 128) - (180 - 117)',
          'β = 180° − 128° = 52°, γ = 180° − 117° = 63°. α = 180° − 52° − 63° = 65°.', 'Bestimme erst β und γ.', art=P),
        A(R, 'Kann ein Dreieck drei spitze Außenwinkel haben?', 'Nein: Die Außenwinkel ergeben zusammen 360°, drei spitze aber weniger als 270°.',
          ['Ja, bei einem gleichseitigen Dreieck.', 'Ja, wenn alle Innenwinkel stumpf sind.', 'Nein, weil Außenwinkel immer 90° sind.'],
          'Jeder Außenwinkel ist 180° minus Innenwinkel; zusammen 3 · 180° − 180° = 360°. Drei Winkel unter 90° ergeben höchstens 270°.',
          'Was ergeben die drei Außenwinkel zusammen?', art=K)]
    F['vieleck'] = [
        Z('In welchem regelmäßigen Vieleck ist jeder Innenwinkel 144° groß? Gib die Zahl der Ecken an.', 10, '360 / (180 - 144)',
          '(n − 2) · 180° = n · 144°, also 180n − 360 = 144n, 36n = 360 und n = 10.', 'Stelle eine Gleichung mit der Winkelsumme auf.', einheit=None, art=P),
        A(R, 'Warum hat ein n-Eck die Winkelsumme (n − 2) · 180°?', 'Von einer Ecke aus zerlegen die Diagonalen das n-Eck in n − 2 Dreiecke.',
          ['Weil jedes n-Eck n Dreiecke enthält.', 'Weil man 2 Ecken nicht mitzählt.', 'Weil jeder Winkel 180° − 2° hat.'],
          'Von einer Ecke gibt es n − 3 Diagonalen; sie zerlegen das n-Eck in n − 2 Dreiecke mit je 180°.', 'Zeichne ein Sechseck und zähle die Dreiecke.', art=P),
        Z('Ein Vieleck hat die Winkelsumme 1 440°. Wie viele Diagonalen gehen von einer Ecke aus?', 7, '1440 / 180 + 2 - 3',
          '(n − 2) · 180° = 1 440°, also n − 2 = 8 und n = 10. Von einer Ecke gehen n − 3 = 7 Diagonalen aus.', 'Bestimme zuerst die Zahl der Ecken.', einheit=None, art=K)]
    F['figuren'] = [
        Z('Die Geraden g und h schneiden sich außerhalb des Blattes. Eine Hilfsgerade k schneidet g unter 64° und h unter 81° (beide Winkel liegen zwischen g und h, auf der Seite des Schnittpunkts). Unter welchem Winkel schneiden sich g und h?',
          35, '180 - 64 - 81', 'g, h und k bilden ein Dreieck mit den Winkeln 64° und 81°. Der dritte Winkel ist 180° − 64° − 81° = 35°.',
          'Die drei Geraden bilden ein Dreieck.', art=P),
        Z('Im Parallelogramm ABCD bildet die Diagonale [AC] mit [AB] den Winkel 35° und mit [AD] den Winkel 40°. Wie groß ist der Winkel ∠ACB?', 40, '40',
          'AD ∥ BC, und [AC] schneidet beide: ∠ACB ist Wechselwinkel zu ∠CAD = 40°.', 'Welche Seiten sind parallel zu [AD]?', art=P),
        Z('Ein Lichtstrahl trifft unter 35° auf einen Spiegel und wird unter 35° zurückgeworfen. Er trifft dann auf einen zweiten, zum ersten parallelen Spiegel. Unter welchem Winkel trifft er dort auf?',
          35, '35', 'Der zurückgeworfene Strahl bildet mit dem ersten Spiegel 35°. Am parallelen zweiten Spiegel ist das ein Wechselwinkel: wieder 35°.',
          'Der Strahl schneidet beide Spiegel – die Spiegel sind parallel.', art=K)]
    F['beweisen'] = [
        L('Beweis der Winkelsumme. Bringe die Kärtchen in die richtige Reihenfolge. Kärtchen 1: „Auf p liegen α′, γ und β′ nebeneinander: α′ + γ + β′ = 180°.“ '
          'Kärtchen 2: „Zeichne durch C die Parallele p zu [AB].“ Kärtchen 3: „Also gilt α + β + γ = 180°.“ Kärtchen 4: „α′ = α und β′ = β (Wechselwinkel).“',
          '1. □; 2. □; 3. □; 4. □', [2, 4, 1, 3], ['2', '4', '1', '3'],
          'Zuerst die Hilfslinie (2), dann die Wechselwinkel (4). Danach die Winkel auf p (1), daraus der Satz (3).',
          'Was muss zuerst gezeichnet sein, bevor man über Winkel an p reden kann?', 'Trage die Nummern der Kärtchen ein.', art=P),
        A(R, 'Warum hat jedes Dreieck mindestens zwei spitze Winkel?', 'Zwei Winkel von je mindestens 90° ergäben schon 180°, für den dritten bliebe nichts.',
          ['Weil spitze Winkel häufiger sind.', 'Weil ein Dreieck drei Ecken hat.', 'Weil jedes Dreieck einen rechten Winkel hat.'],
          'Wären zwei Winkel 90° oder größer, wäre ihre Summe mindestens 180°. Dann bliebe für den dritten Winkel 0° oder weniger.', 'Nutze die Winkelsumme.', art=P),
        A(R, 'Welcher Satz wird im Beweis „Winkelsumme im Viereck = 360°“ benutzt, und wie oft?', 'die Winkelsumme im Dreieck, zweimal',
          ['der Außenwinkelsatz, viermal', 'der Satz über Scheitelwinkel, einmal', 'die Winkelsumme im Dreieck, viermal'],
          'Eine Diagonale teilt das Viereck in zwei Dreiecke. Für jedes nutzt man die Winkelsumme 180°: zusammen 360°.', 'Welche Hilfslinie braucht man?', art=K)]
    return F


PLAN = [('uebung', 1)] * 4 + [('uebung', 2)] * 6 + [('uebung', 3)] * 8 + [('test', 2)] + [('korrektur', 2)] * 3 + [('sicherung', 2)] * 6


def _schl(a):
    """Dubletten über den Aufgabentext (mit Zeichnung) – gleiche Frage mit nur anders gemischten Antworten zählt als doppelt."""
    f = a['f']
    return f['text']


def aufgaben():
    R = random.Random(7098)
    feste = fest(R)
    out, gesehen = [], set()
    beispiele = {s['text'] for e in ETAPPEN for s in e['schritte']}
    zahl = collections.Counter()
    for e in ETAPPEN:
        lz = e['lernziel']
        f = list(feste[lz])
        assert sum(1 for a in f if a['_art'] == P) == 2 and sum(1 for a in f if a['_art'] == K) == 1
        for pool, st in PLAN:
            if pool == 'uebung' and st == 3 and f:
                a = f.pop(0)
            else:
                for _ in range(4000):
                    a = GEN[lz](R, st)
                    if a['f']['text'] not in beispiele and _schl(a) not in gesehen: break
                else:
                    raise SystemExit(f'zu wenige Varianten: {lz} Stufe {st}')
            k = _schl(a)
            assert k not in gesehen, a['f']['text']
            gesehen.add(k)
            art = a.pop('_art', None)
            if art: zahl[(lz, art)] += 1
            assert len(a['w']) >= 15 and a['h'], a
            if pool != 'uebung': a.pop('h')
            out.append({'l': lz, 't': lz, 'p': pool, 's': st, **a})
    return out, zahl


def datei():
    auf, zahl = aufgaben()
    lz = [e['lernziel'] for e in ETAPPEN]
    return {
        **META, 'autor': 'Claude (Vierzehnte Runde, Generator geometrie.winkelsaetze.py)',
        'inhalt': {
            'ziel': 'Winkel an Geradenkreuzungen und Doppelkreuzungen benennen und berechnen, Parallelität prüfen, die Innenwinkelsumme im Dreieck begründen, '
                    'Außenwinkel und Winkelsummen im Vieleck nutzen und Winkel in Figuren schrittweise mit Begründung bestimmen.',
            'merke': ['Scheitelwinkel sind gleich groß, Nebenwinkel ergeben 180°.', 'An Parallelen: Stufen- und Wechselwinkel sind gleich groß – und umgekehrt.',
                      'Dreieck: α + β + γ = 180°. Außenwinkel = Summe der beiden nicht anliegenden Innenwinkel.', 'n-Eck: Winkelsumme (n − 2) · 180°.',
                      'Jeder Schritt einer Begründung nennt seinen Winkelsatz.'],
            'abschnitte': [{'titel': 'Winkel an Kreuzungen', 'lernziele': ['scheitel_neben', 'stufen_wechsel', 'parallel_pruefen']},
                           {'titel': 'Winkelsummen', 'lernziele': ['innenwinkelsumme', 'aussenwinkel', 'vieleck']},
                           {'titel': 'Begründen in Figuren', 'lernziele': ['figuren', 'beweisen']}],
            'etappen': ETAPPEN,
            'teilfaehigkeiten': [{'k': e['lernziel'], 'text': e['titel'], 'lernziele': [e['lernziel']]} for e in ETAPPEN],
            'bewertung': {'lernziele_pflicht': lz, 'lernziele_vertiefung': [], 'testaufgaben_je_lernziel': 1, 'hilfen_im_test': False},
            'quellen': {'erklaerungen': 'Eigene Fassung (Claude).',
                        'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern, Gymnasium M7 2.2 „Winkelbetrachtungen an Figuren“ (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik).',
                        'pruefungsvorbilder': 'Typ und Niveau nach: Bayerischer Mathematik-Test 8 (ISB) 2019 B5/B7, 2021 A8, 2025 A8; Jahrgangsstufentest Realschule 8 (ISB) 2020 II, 2025 II Nr. 5/6; '
                                              'Vergleichsarbeit Jgst. 8 (Innenwinkel im n-Eck). Eigene Zahlen und Einkleidung.'},
        },
        'aufgaben': auf,
        'offen': ['Überschneidung: geometrie.konstruktion (gleicher Ort Addis Abeba) hat schon die Lernkarten „parallelen“, „winkelsumme“ und „vierecke“. '
                  'Vorschlag: dort als Wiederholung lassen oder in einer späteren Runde auf Konstruktion und Kongruenz kürzen – Entscheidung Sebastian.',
                  'Winkel werden vom Kind nicht gemessen oder gezeichnet (kann die App nicht); Zeichnungen sind nicht maßstäblich, Werte stehen im Text.',
                  'Der Begriff „Nachbarwinkel“ (E-Winkel) steht nicht im LehrplanPLUS M7 2.2 und wird nicht eingeführt; solche Winkel werden über Stufen- und Nebenwinkel berechnet.'],
    }, zahl


if __name__ == '__main__':
    d, zahl = datei()
    ZIEL.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{ZIEL.name}: {len(d["inhalt"]["etappen"])} Lernkarten, {len(d["aufgaben"])} Aufgaben')
    for e in d['inhalt']['etappen']:
        l = e['lernziel']
        print(f'  {l:18} Prüfungsvorbild: {zahl[(l, P)]}  Knobel: {zahl[(l, K)]}')
