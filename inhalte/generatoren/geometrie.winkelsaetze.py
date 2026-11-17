#!/usr/bin/env python3
"""Thema geometrie.winkelsaetze – Winkelsätze (Gymnasium Bayern, Klasse 7, LehrplanPLUS M7 2.2 „Winkelbetrachtungen an Figuren“).

Vierzehnte Runde (Zweig daten-klassen-2), nachgebessert in der Sechzehnten Runde (Zweig winkelsaetze-2) nach den Prüfberichten
pruefung-winkelsaetze und pruefung-eltern. Baut auf geometrie.winkel (Klasse 5, „Mit Winkeln rechnen“) auf und wiederholt dessen Inhalte nicht:
Fachbegriffe Scheitel- und Nebenwinkel, Stufen- und Wechselwinkel an Parallelen, Parallelität prüfen, Innenwinkelsumme im Dreieck (Beweis mit
Wechselwinkeln), Außenwinkel (Vertiefung, nicht im LehrplanPLUS M7 2.2), Winkelsumme im Vieleck, Winkel in Figuren mit mehreren Kreuzungen, Fundamentalsatz und abgeleiteter Satz.

Je Lernkarte: 18 Übungen (Stufe 1: 4, Stufe 2: 6, Stufe 3: 8; davon 2 nach Prüfungsvorbild und 1 Knobelaufgabe), 1 Test, 3 Korrektur, 6 Sicherung.
Prüfungsvorbilder (nur Typ und Niveau, eigene Zahlen und Einkleidung): Bayerischer Mathematik-Test 8 (ISB) 2019 B5 und B7, 2021 A8, 2022 A7,
2025 A8; Jahrgangsstufentest Realschule 8 (ISB) 2020 II und 2025 II Nr. 5/6; Vergleichsarbeit Jgst. 8 (Innenwinkel im n-Eck).
Ohne lineare Gleichungen (M7 3) und ohne Basiswinkelsatz (M7 5) in den Pflicht-Etappen. Jede Zeichnung wird beim Erzeugen geprüft:
angeschriebene Winkel höchstens 3° neben dem gezeichneten Winkel, jeder Winkelbogen liegt an gezeichneten Linien.

    python3 -I inhalte/generatoren/geometrie.winkelsaetze.py
    python3 -I tools/inhalt_pruefen.py inhalte/themen/geometrie.winkelsaetze.json
"""
import collections
import json
import math
import random
import re
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
VERTIEFUNG = ('aussenwinkel',)  # nicht im LehrplanPLUS M7 2.2
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
# Alle Winkel werden exakt gezeichnet: Der angeschriebene Wert ist der gezeichnete Winkel (Prüfung in pruefe_figur).
def _r(v):
    return round(v, 2)


def _pol(p, w, l):
    """Punkt im Abstand l von p in Richtung w (Grad, mathematisch)."""
    return [_r(p[0] + l * math.cos(math.radians(w))), _r(p[1] + l * math.sin(math.radians(w)))]


def _strahlen(name, p, wr, wu, l=1.6):
    """Kreuzung in p: Gerade 1 in Richtung wr (Hilfspunkte R/L), Gerade 2 in Richtung wu (Hilfspunkte U/D)."""
    return {name: [_r(p[0]), _r(p[1])], f'_{name}R': _pol(p, wr, l), f'_{name}L': _pol(p, wr + 180, l),
            f'_{name}U': _pol(p, wu, l), f'_{name}D': _pol(p, wu + 180, l)}


_SCHENKEL = {'ro': ('R', 'U'), 'lo': ('U', 'L'), 'lu': ('L', 'D'), 'ru': ('D', 'R')}


def _w(name, pos, text):
    s1, s2 = _SCHENKEL[pos]
    return [name, f'_{name}{s1}', f'_{name}{s2}', text]


def doppel(a, marken, b=None):
    """g waagrecht (oben, Punkt S), h (unten, Punkt T), geschnitten von k. a = Winkel rechts oberhalb bei S.
    b = Winkel rechts oberhalb bei T. Ohne b ist h ∥ g; sonst ist h um a − b gekippt (sichtbar nicht parallel, Bögen liegen an h).
    marken: Liste (Punkt 'S'|'T', Lage 'ro'|'lo'|'lu'|'ru', Text)."""
    b = a if b is None else b
    th = a - b
    T = (2.0, 0.0)
    S = (T[0] + 3 / math.tan(math.radians(a)), 3.0)
    pk = {**_strahlen('S', S, 0, a), **_strahlen('T', T, th, a)}
    x1, x2 = min(S[0], T[0]) - 3, max(S[0], T[0]) + 3
    c = math.cos(math.radians(th))
    pk.update({'_g1': [_r(x1), 3], '_g2': [_r(x2), 3], '_h1': _pol(T, th, (x1 - T[0]) / c), '_h2': _pol(T, th, (x2 - T[0]) / c),
               '_k1': _pol(T, a + 180, 1.6), '_k2': _pol(S, a, 1.6)})
    return {'typ': 'figur', 'punkte': pk, 'linien': [['_g1', '_g2', 'g'], ['_h1', '_h2', 'h'], ['_k1', '_k2', 'k']],
            'winkel': [_w(p, lage, txt) for p, lage, txt in marken]}


def einfach(a, marken):
    """Eine Kreuzung zweier Geraden in S; a = Winkel rechts oberhalb."""
    pk = _strahlen('S', (0, 0), 0, a, 3)
    return {'typ': 'figur', 'punkte': pk, 'linien': [['_SL', '_SR'], ['_SD', '_SU']], 'winkel': [_w('S', lage, txt) for lage, txt in marken]}


def drei_geraden(w1, w2, marken):
    """Drei Geraden durch S. Die sechs Winkel 1–6 laufen gegen den Uhrzeigersinn: 1 = w1, 2 = w2, 3 = 180° − w1 − w2, 4 = w1, 5 = w2, 6 = 3.
    marken: {Nummer: Text}."""
    r = [0, w1, w1 + w2, 180, 180 + w1, 180 + w1 + w2]
    pk = {'S': [0, 0], **{f'_r{i}': _pol((0, 0), x, 3) for i, x in enumerate(r)}}
    win = [['S', f'_r{(k - 1) % 6}', f'_r{k % 6}', t] for k, t in sorted(marken.items())]
    return {'typ': 'figur', 'punkte': pk, 'linien': [['_r0', '_r3'], ['_r1', '_r4'], ['_r2', '_r5']], 'winkel': win}


def _dreieckspunkte(al, be, c=6.0):
    ga = 180 - al - be
    b = c * math.sin(math.radians(be)) / math.sin(math.radians(ga))
    return (0.0, 0.0), (c, 0.0), (b * math.cos(math.radians(al)), b * math.sin(math.radians(al)))


def dreieck(al, be, marken, aussen=None):
    """Dreieck ABC mit Winkeln al bei A und be bei B. marken: Liste (Ecke, Text). aussen: (Ecke, Text) für einen Außenwinkel."""
    _, _, C = _dreieckspunkte(al, be)
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
            n = math.hypot(*C)
            pk['_X'] = [_r(C[0] + 2.5 * C[0] / n), _r(C[1] + 2.5 * C[1] / n)]
            lin.append(['C', '_X', '', 'gestrichelt'])
            fig['winkel'].append(['C', 'B', '_X', t])
    return fig


def dreieck_par(al, be, marken):
    """Dreieck ABC zwischen den Parallelen g (durch C) und h (durch A und B).
    marken: Liste (Ort, Text); Ort A, B, C (Innenwinkel), Cl (zwischen [CA] und g links), Cr (zwischen [CB] und g rechts)."""
    _, _, C = _dreieckspunkte(al, be)
    x1, x2 = min(-1.5, C[0] - 2), max(7.5, C[0] + 2)
    pk = {'A': [0, 0], 'B': [6, 0], 'C': [_r(C[0]), _r(C[1])], '_g1': [_r(x1), _r(C[1])], '_g2': [_r(x2), _r(C[1])], '_h1': [_r(x1), 0], '_h2': [_r(x2), 0]}
    W = {'A': ['A', 'B', 'C'], 'B': ['B', 'C', 'A'], 'C': ['C', 'A', 'B'], 'Cl': ['C', '_g1', 'A'], 'Cr': ['C', 'B', '_g2']}
    return {'typ': 'figur', 'punkte': pk, 'flaeche': ['A', 'B', 'C'], 'linien': [['_g1', '_g2', 'g'], ['_h1', '_h2', 'h'], ['A', 'C'], ['B', 'C']],
            'winkel': [W[o] + [t] for o, t in marken]}


def parallelogramm(al, marken, p=5.0, q=3.0, diagonale=False):
    """Parallelogramm ABCD mit ∢BAD = al, |AB| = p, |AD| = q. Orte: A, B, C, D (Innenwinkel); mit Diagonale [AC] zusätzlich
    A_AB (∢BAC), A_AD (∢CAD), C_CD (∢ACD), C_CB (∢ACB)."""
    D = _pol((0, 0), al, q)
    pk = {'A': [0, 0], 'B': [p, 0], 'C': [_r(p + D[0]), D[1]], 'D': D}
    lin = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A']]
    if diagonale: lin.append(['A', 'C'])
    W = {'A': ['A', 'B', 'D'], 'B': ['B', 'C', 'A'], 'C': ['C', 'D', 'B'], 'D': ['D', 'A', 'C'],
         'A_AB': ['A', 'B', 'C'], 'A_AD': ['A', 'C', 'D'], 'C_CD': ['C', 'D', 'A'], 'C_CB': ['C', 'A', 'B']}
    return {'typ': 'figur', 'punkte': pk, 'flaeche': ['A', 'B', 'C', 'D'], 'linien': lin, 'winkel': [W[o] + [t] for o, t in marken]}


def trapez(al, be, marken):
    """Trapez ABCD mit AB ∥ CD, ∢BAD = al, ∢CBA = be, Höhe 3. Orte: A, B, C, D."""
    hh = 3.0
    D = _pol((0, 0), al, hh / math.sin(math.radians(al)))
    C = _pol((8, 0), 180 - be, hh / math.sin(math.radians(be)))
    assert C[0] - D[0] > 1.5
    pk = {'A': [0, 0], 'B': [8, 0], 'C': C, 'D': D}
    W = {'A': ['A', 'B', 'D'], 'B': ['B', 'C', 'A'], 'C': ['C', 'D', 'B'], 'D': ['D', 'A', 'C']}
    return {'typ': 'figur', 'punkte': pk, 'flaeche': ['A', 'B', 'C', 'D'], 'linien': [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A']],
            'winkel': [W[o] + [t] for o, t in marken]}


def weg(a, b, marken, hilfslinie=False):
    """g ∥ h (Abstand 4). Weg von A auf g zu P und weiter zu B auf h. a = Winkel bei A zwischen g (rechts) und [AP],
    b = Winkel bei B zwischen h (rechts) und [BP]; der Winkel bei P ist a + b. Orte: A, B, P, Pg (Hilfslinie oben), Ph (Hilfslinie unten)."""
    A = (0.0, 4.0)
    P = (2 / math.tan(math.radians(a)), 2.0)
    B = (P[0] - 2 / math.tan(math.radians(b)), 0.0)
    x1, x2 = min(A[0], B[0], P[0]) - 1.5, max(A[0], B[0], P[0]) + 2.5
    pk = {'A': [0, 4], 'P': [_r(P[0]), 2], 'B': [_r(B[0]), 0], '_g1': [_r(x1), 4], '_g2': [_r(x2), 4], '_h1': [_r(x1), 0], '_h2': [_r(x2), 0],
          '_p1': [_r(x1), 2], '_p2': [_r(x2), 2]}
    lin = [['_g1', '_g2', 'g'], ['_h1', '_h2', 'h'], ['A', 'P'], ['P', 'B']]
    if hilfslinie: lin.append(['_p1', '_p2', '', 'gestrichelt'])
    W = {'A': ['A', 'P', '_g2'], 'B': ['B', '_h2', 'P'], 'P': ['P', 'A', 'B'], 'Pg': ['P', 'A', '_p1'], 'Ph': ['P', '_p1', 'B']}
    return {'typ': 'figur', 'punkte': pk, 'linien': lin, 'winkel': [W[o] + [t] for o, t in marken]}


def vieleck_fig(winkel, marken=None, diagonalen=False):
    """Konvexes Vieleck mit den Innenwinkeln winkel (in Reihenfolge der Ecken, gegen den Uhrzeigersinn), exakt gezeichnet.
    marken: {Eckennummer: Text}. diagonalen: alle Diagonalen von Ecke 0 aus (gestrichelt)."""
    n = len(winkel)
    assert sum(winkel) == (n - 2) * 180 and all(0 < w < 180 for w in winkel)
    rich = [0.0]
    for k in range(1, n): rich.append(rich[-1] + 180 - winkel[k])
    e = [(math.cos(math.radians(r)), math.sin(math.radians(r))) for r in rich]
    for basis in (5, 4, 6, 3, 7):
        for s0 in (basis, basis + 1, basis - 1):
            s = [s0] + [basis] * (n - 3)
            rx = -sum(si * e[i][0] for i, si in enumerate(s))
            ry = -sum(si * e[i][1] for i, si in enumerate(s))
            a1, b1, a2, b2 = e[n - 2][0], e[n - 1][0], e[n - 2][1], e[n - 1][1]
            det = a1 * b2 - b1 * a2
            if abs(det) < 1e-9: continue
            u, v = (rx * b2 - b1 * ry) / det, (a1 * ry - rx * a2) / det
            if min(u, v) >= 0.4 * basis and max(u, v) <= 2.5 * basis: break
        else:
            continue
        break
    else:
        raise AssertionError(f'Vieleck nicht zeichenbar: {winkel}')
    s += [u, v]
    pts = [(0.0, 0.0)]
    for i in range(n - 1): pts.append((pts[-1][0] + s[i] * e[i][0], pts[-1][1] + s[i] * e[i][1]))
    nm = [f'_E{i}' for i in range(n)]
    pk = {nm[i]: [_r(p[0]), _r(p[1])] for i, p in enumerate(pts)}
    lin = [[nm[i], nm[(i + 1) % n]] for i in range(n)]
    if diagonalen: lin += [[nm[0], nm[i], '', 'gestrichelt'] for i in range(2, n - 1)]
    win = [[nm[k], nm[(k + 1) % n], nm[k - 1], t] for k, t in sorted((marken or {}).items())]
    return {'typ': 'figur', 'punkte': pk, 'flaeche': nm, 'linien': lin, 'winkel': win}


def regelmaessig(n, marken=None, diagonalen=False):
    w = Fr((n - 2) * 180, n)
    return vieleck_fig([w] * n, marken, diagonalen)


# ---------- Prüfung der Zeichnungen ----------
def _winkel_an(pk, s, q1, q2):
    a = math.atan2(pk[q1][1] - pk[s][1], pk[q1][0] - pk[s][0])
    b = math.atan2(pk[q2][1] - pk[s][1], pk[q2][0] - pk[s][0])
    d = abs(math.degrees(a - b)) % 360
    return min(d, 360 - d)


def _auf_linie(pk, lin, s, q):
    """Liegt der Strahl von s nach q auf einer gezeichneten Linie (s auf der Strecke, q auf derselben Geraden)?"""
    for l in lin:
        u, v = pk[l[0]], pk[l[1]]
        dx, dy = v[0] - u[0], v[1] - u[1]
        n = math.hypot(dx, dy)
        ab = lambda p: abs((p[0] - u[0]) * dy - (p[1] - u[1]) * dx) / n
        t = ((pk[s][0] - u[0]) * dx + (pk[s][1] - u[1]) * dy) / n ** 2
        if ab(pk[s]) < 0.03 and ab(pk[q]) < 0.03 and -0.01 <= t <= 1.01: return True
    return False


def pruefe_figur(f, wo):
    """Angeschriebene Gradzahlen höchstens 3° neben dem gezeichneten Winkel; Bogen-Schenkel auf gezeichneten Linien."""
    if not f or f.get('typ') != 'figur': return 0
    pk, lin = f['punkte'], f.get('linien', [])
    for s, q1, q2, t in f.get('winkel', []):
        for q in (q1, q2): assert _auf_linie(pk, lin, s, q), f'{wo}: Bogen bei {s} ({t}) liegt nicht an einer Linie ({q})'
        m = re.findall(r'(\d+(?:,\d+)?)°', t)
        if m and '≠' not in t and 'nicht' not in t:
            soll = float(m[-1].replace(',', '.'))
            ist = _winkel_an(pk, s, q1, q2)
            assert abs(ist - soll) <= 3, f'{wo}: „{t}“ gezeichnet {ist:.1f}°'
    return 1


# ---------- Lernkarten (neues Muster, Vorgabe 16.11.) ----------
B_SN = einfach(65, [('ro', 'α = 65°'), ('lo', 'β'), ('lu', 'γ'), ('ru', 'δ')])
B_SW = doppel(60, [('S', 'ro', 'α = 60°'), ('T', 'ro', 'β'), ('T', 'lu', 'γ')])
B_PP = doppel(70, [('S', 'ro', '70°'), ('T', 'ro', '70°')])
B_D = dreieck(50, 70, [('A', 'α'), ('B', 'β'), ('C', 'γ')])
_CY = B_D['punkte']['C'][1]
B_DP = {**B_D, 'punkte': {**B_D['punkte'], '_p1': [-1.5, _CY], '_p2': [7.5, _CY]}, 'linien': B_D['linien'] + [['_p1', '_p2', 'p', 'gestrichelt']]}
_W_ABC = [['A', 'B', 'C', 'α'], ['B', 'C', 'A', 'β'], ['C', 'A', 'B', 'γ']]
B_AW = dreieck(50, 70, [('A', 'α = 50°'), ('B', 'β = 70°'), ('C', 'γ')], aussen=('C', 'γ\''))
B_VE = {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [6, 0], 'C': [7, 3.5], 'D': [3, 5.5], 'E': [-1, 3]},
        'flaeche': ['A', 'B', 'C', 'D', 'E'], 'linien': [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'A']]}
B_V5 = regelmaessig(5, {k: '108°' for k in range(5)})
B_FI = dreieck_par(50, 60, [('A', '50°'), ('B', '60°'), ('C', 'γ')])

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
                 ['Wechselwinkel', 'Winkel an zwei Kreuzungen, über Kreuz zwischen den Parallelen. Manche Bücher nennen auch die äußeren Paare über Kreuz so.']],
     'bild': B_SW,
     'schritte': [{'text': 'g ∥ h. Bei S ist α = 60° (rechts oberhalb).'},
                  {'text': 'β liegt bei T genauso: Stufenwinkel, also ⟦β = 60°⟧.',
                   'bild': {'winkel': [_w('S', 'ro', 'α = 60°'), _w('T', 'ro', 'β = 60°'), _w('T', 'lu', 'γ')]}},
                  {'text': 'γ liegt bei T links unterhalb: Scheitelwinkel von β, also γ = 60°.',
                   'bild': {'winkel': [_w('S', 'ro', 'α = 60°'), _w('T', 'ro', 'β = 60°'), _w('T', 'lu', 'γ = 60°')]}},
                  {'text': 'Bei S links unterhalb liegt auch 60°: Wechselwinkel zu β.',
                   'bild': {'winkel': [_w('S', 'lu', '60°'), _w('T', 'ro', 'β = 60°')]}}],
     'fehler': 'Ohne Parallelen gilt das nicht. Laufen die Gleise schräg zueinander, sind Stufenwinkel verschieden groß.',
     'fehler_bild': doppel(60, [('S', 'ro', '60°'), ('T', 'ro', '≠ 60°')], b=75),
     'regel': 'An Parallelen sind ⟦Stufenwinkel und Wechselwinkel gleich groß⟧.'},
    {'lernziel': 'parallel_pruefen', 'titel': 'Sind die Geraden parallel?',
     'einstieg': 'Eine Schreinerin prüft, ob zwei Regalbretter parallel sind. Sie misst, wie schräg eine Leiste beide Bretter trifft. Gleiche Stufenwinkel bedeuten: die Bretter sind ⟦parallel⟧.',
     'woerter': [['Umkehrung', 'der Satz rückwärts gelesen: aus gleichen Winkeln folgt parallel']],
     'bild': B_PP,
     'schritte': [{'text': 'k trifft g bei S unter 70°, h bei T auch unter 70°.'},
                  {'text': 'Die beiden Winkel liegen gleich: Es sind Stufenwinkel.'},
                  {'text': 'Gleich große Stufenwinkel: Nach der Umkehrung ist ⟦g ∥ h⟧.'},
                  {'text': 'Bei 70° und 80° wären die Geraden nicht parallel.',
                   'bild': doppel(70, [('S', 'ro', '70°'), ('T', 'ro', '80°')], b=80)}],
     'fehler': 'Gleiche Scheitelwinkel an einer Kreuzung beweisen nichts. Vergleichen muss man Winkel an beiden Kreuzungen.',
     'fehler_bild': doppel(70, [('S', 'ro', '70°'), ('S', 'lu', '70°')]),
     'regel': 'Gleich große ⟦Stufen- oder Wechselwinkel⟧ zeigen: Die Geraden sind parallel.'},
    {'lernziel': 'innenwinkelsumme', 'titel': 'Winkelsumme im Dreieck begründen',
     'einstieg': 'Reiße die drei Ecken eines Papierdreiecks ab und lege sie nebeneinander. Sie bilden eine gerade Linie. Das gilt für jedes Dreieck: Die ⟦Innenwinkelsumme⟧ ist 180°.',
     'woerter': [['Innenwinkelsumme', 'alle Winkel innen in einer Figur zusammen'], ['Hilfslinie', 'eine Linie, die man extra einzeichnet, um etwas zu zeigen']],
     'bild': B_D,
     'schritte': [{'text': 'Zeichne durch C eine Hilfslinie p parallel zu [AB].', 'bild': B_DP},
                  {'text': 'Links von C entsteht ein Winkel so groß wie α: Wechselwinkel.',
                   'bild': {**B_DP, 'winkel': _W_ABC + [['C', '_p1', 'A', 'α']]}},
                  {'text': 'Rechts von C entsteht ein Winkel so groß wie β: Wechselwinkel.',
                   'bild': {**B_DP, 'winkel': _W_ABC + [['C', '_p1', 'A', 'α'], ['C', 'B', '_p2', 'β']]}},
                  {'text': 'Auf p liegen α, γ und β nebeneinander: ⟦α + β + γ = 180°⟧.',
                   'bild': {**B_DP, 'winkel': [['C', '_p1', 'A', 'α'], ['C', 'A', 'B', 'γ'], ['C', 'B', '_p2', 'β']]}}],
     'fehler': 'Messen an einem Dreieck ist kein Beweis. Erst die Begründung mit Wechselwinkeln zeigt: Es gilt für jedes Dreieck.',
     'regel': 'In jedem Dreieck gilt ⟦α + β + γ = 180°⟧. Der Beweis nutzt Wechselwinkel an einer Parallelen.'},
    {'lernziel': 'aussenwinkel', 'titel': 'Außenwinkel am Dreieck',
     'einstieg': 'Ein Läufer rennt um ein dreieckiges Feld. An jeder Ecke biegt er ab. Der Winkel, um den er abbiegt, ist ein ⟦Außenwinkel⟧ des Dreiecks.',
     'woerter': [['Außenwinkel', 'Nebenwinkel eines Innenwinkels; außen an der verlängerten Seite'],
                 ['Außenwinkelsatz', 'Ein Außenwinkel ist so groß wie die beiden nicht anliegenden Innenwinkel zusammen.']],
     'bild': B_AW,
     'schritte': [{'text': 'Der Außenwinkel γ\' ist Nebenwinkel von γ: γ\' = 180° − γ.'},
                  {'text': 'Mit der Winkelsumme gilt γ = 180° − 50° − 70° = 60°.'},
                  {'text': 'Also ist γ\' = 120° = ⟦α + β⟧. Das ist der Außenwinkelsatz.',
                   'bild': dreieck(50, 70, [('A', 'α = 50°'), ('B', 'β = 70°'), ('C', 'γ = 60°')], aussen=('C', '120°'))}],
     'fehler': 'Der Außenwinkel bei C ist nicht γ. Er liegt außen und ergänzt γ zu 180°.',
     'fehler_bild': dreieck(50, 70, [('C', 'γ, nicht γ\'')], aussen=('C', 'γ\'')),
     'regel': 'Ein ⟦Außenwinkel⟧ ist so groß wie die zwei anderen Innenwinkel zusammen. Gemeint sind die beiden, die nicht an ihm liegen.'},
    {'lernziel': 'vieleck', 'titel': 'Winkelsumme im Vieleck',
     'einstieg': 'Ein Gärtner legt ein fünfeckiges Beet an. Er zieht von einer Ecke aus Schnüre zu den anderen Ecken. So zerfällt das Beet in Dreiecke – und die ⟦Winkelsumme⟧ lässt sich zählen.',
     'woerter': [['Winkelsumme', 'alle Innenwinkel einer Figur zusammen'], ['n-Eck', 'Vieleck mit n Ecken, z. B. Fünfeck: n = 5'],
                 ['regelmäßig', 'alle Seiten gleich lang und alle Winkel gleich groß']],
     'bild': B_VE,
     'schritte': [{'text': 'Von A aus zeichnest du die Diagonalen nach C und D.',
                   'bild': {'linien': B_VE['linien'] + [['A', 'C', '', 'gestrichelt'], ['A', 'D', '', 'gestrichelt']]}},
                  {'text': 'Es entstehen 3 Dreiecke. Beim n-Eck sind es n − 2.'},
                  {'text': 'Jedes Dreieck hat 180°: ⟦3 · 180° = 540°⟧.'},
                  {'text': 'Im regelmäßigen Fünfeck ist jeder Winkel 540° : 5 = 108°.', 'bild': B_V5}],
     'fehler': 'Nicht n · 180° rechnen: Ein Fünfeck zerfällt nur in 3 Dreiecke, nicht in 5.',
     'regel': 'Ein n-Eck hat die Winkelsumme ⟦(n − 2) · 180°⟧. Ein Viereck hat also 360°.'},
    {'lernziel': 'figuren', 'titel': 'Winkel in Figuren bestimmen',
     'einstieg': 'Ein Dreieck klemmt zwischen zwei parallelen Schienen. Zwei Winkel sind bekannt. Jeden weiteren Winkel findest du mit einem ⟦Winkelsatz⟧ – Schritt für Schritt.',
     'woerter': [['Winkelsatz', 'bewiesene Regel über Winkel, z. B. „Nebenwinkel ergeben 180°“'],
                 ['∢BAC', 'Winkel bei A zwischen [AB] und [AC]; der Scheitel A steht in der Mitte']],
     'bild': B_FI,
     'schritte': [{'text': 'g ∥ h. Im Dreieck ABC ist ∢BAC = 50° und ∢CBA = 60°.'},
                  {'text': 'Winkelsumme im Dreieck: ⟦γ = 180° − 50° − 60° = 70°⟧.',
                   'bild': {'winkel': [['A', 'B', 'C', '50°'], ['B', 'C', 'A', '60°'], ['C', 'A', 'B', 'γ = 70°']]}},
                  {'text': 'Links bei C bilden [CA] und g 50°: Wechselwinkel zu ∢BAC.',
                   'bild': {'winkel': [['A', 'B', 'C', '50°'], ['B', 'C', 'A', '60°'], ['C', 'A', 'B', 'γ = 70°'], ['C', '_g1', 'A', '50°']]}},
                  {'text': 'Rechts bei C bilden [CB] und g 60°: Wechselwinkel zu ∢CBA.',
                   'bild': {'winkel': [['A', 'B', 'C', '50°'], ['B', 'C', 'A', '60°'], ['C', 'A', 'B', 'γ = 70°'], ['C', '_g1', 'A', '50°'], ['C', 'B', '_g2', '60°']]}}],
     'probe': 'Auf g liegen bei C 50° + 70° + 60° = 180° ✓',
     'fehler': 'Nicht nach Augenmaß schätzen. Jeder Wert braucht einen Grund: Nebenwinkel, Scheitelwinkel, Stufen-, Wechselwinkel oder Winkelsumme.',
     'regel': 'Gehe von bekannten Winkeln aus. Nenne bei jedem Schritt den ⟦Winkelsatz⟧, den du nutzt.'},
    {'lernziel': 'beweisen', 'titel': 'Begründen mit Winkelsätzen',
     'einstieg': 'In der Mathematik baut man Sätze aufeinander auf wie Bausteine. Ganz unten liegt ein Satz, den man annimmt. Er heißt ⟦Fundamentalsatz⟧.',
     'woerter': [['Fundamentalsatz', 'Grundsatz, der nicht bewiesen, sondern vorausgesetzt wird'], ['abgeleiteter Satz', 'Satz, der mit anderen Sätzen bewiesen wird'],
                 ['Zirkelschluss', 'ein Beweis, der den zu beweisenden Satz schon benutzt']],
     'bild': B_DP,
     'schritte': [{'text': 'Fundamentalsatz: Wechselwinkel an Parallelen sind gleich groß.'},
                  {'text': 'Daraus folgt die Winkelsumme im Dreieck: ein abgeleiteter Satz.'},
                  {'text': 'Aus der Winkelsumme im Dreieck folgt die ⟦Winkelsumme im Viereck⟧.'},
                  {'text': 'Rückwärts begründen wäre ein Zirkelschluss: Jeder Satz stützt sich nur auf frühere.'}],
     'fehler': 'Einen Satz mit sich selbst begründen ist ein Zirkelschluss. Der Beweis darf nur Sätze benutzen, die vorher feststehen.',
     'regel': 'Ein Beweis ist eine Kette. Jedes Glied stützt sich auf einen ⟦vorher bekannten Satz⟧.'},
]


# ---------- Aufgaben-Generatoren (zufällig, je Stufe) ----------
def _paar(R):
    return R.choice([x for x in range(25, 156) if x != 90])


def gen_scheitel_neben(R, st):
    a = _paar(R)
    if st == 1:
        if R.random() < 0.5:
            return Z(f'Zwei Geraden schneiden sich. Ein Winkel ist {g(a)} groß. Wie groß ist sein Scheitelwinkel?', a, f'{a}',
                     f'Scheitelwinkel sind gleich groß: {g(a)}.', 'Der Scheitelwinkel liegt gegenüber.', grafik=einfach(a, [('ro', g(a)), ('lu', '?')]))
        return Z(f'Zwei Geraden schneiden sich. Ein Winkel ist {g(a)} groß. Wie groß ist sein Nebenwinkel?', 180 - a, f'180 - {a}',
                 f'Nebenwinkel ergänzen sich zu 180°: 180° − {g(a)} = {g(180 - a)}.', 'Nebenwinkel liegen an einer Geraden nebeneinander.',
                 grafik=einfach(a, [('ro', g(a)), ('lo', '?')]))
    if st == 2:
        art = R.choice(['lage', 'lage', 'unterschied', 'benennen', 'benennen'])
        if art == 'lage':
            ziel = R.choice(['lo', 'lu', 'ru'])
            w = {'lo': 180 - a, 'lu': a, 'ru': 180 - a}[ziel]
            return Z(f'Zwei Geraden schneiden sich. Der Winkel rechts oberhalb ist {g(a)} groß. Wie groß ist der Winkel {POS_TEXT[ziel]}?', w,
                     f'{w}', f'Scheitelwinkel sind gleich groß: {g(w)}.' if ziel == 'lu' else f'Nebenwinkel ergänzen sich zu 180°: 180° − {g(a)} = {g(w)}.',
                     'Liegt der Winkel gegenüber oder daneben?', grafik=einfach(a, [('ro', g(a)), (ziel, '?')]))
        if art == 'unterschied':
            d = R.choice(range(10, 101, 10))
            big = (180 + d) // 2
            return Z(f'Ein Winkel ist um {g(d)} größer als sein Nebenwinkel. Wie groß ist der größere Winkel?', big, f'(180 + {d}) / 2',
                     f'Nimm den Unterschied weg: 180° − {g(d)} = {g(180 - d)} bleiben für zwei gleich große Winkel, je {g((180 - d) // 2)}. '
                     f'Der größere Winkel: {g((180 - d) // 2)} + {g(d)} = {g(big)}.', 'Beide zusammen ergeben 180°. Nimm zuerst den Unterschied weg.')
        nr = R.randint(1, 4)
        gegen = {1: 3, 2: 4, 3: 1, 4: 2}[nr]
        if R.random() < 0.5:
            return A(R, f'Zwei Geraden schneiden sich in S. Die vier Winkel sind mit 1 bis 4 nummeriert. Welcher Winkel ist Scheitelwinkel zu Winkel {nr}?', f'Winkel {gegen}',
                     [f'Winkel {x}' for x in (1, 2, 3, 4) if x not in (nr, gegen)] + [f'Winkel {nr}'],
                     f'Der Scheitelwinkel liegt gegenüber: Winkel {gegen}. Die beiden anderen sind Nebenwinkel von Winkel {nr}.', 'Scheitelwinkel haben nur den Punkt S gemeinsam.',
                     grafik=einfach(a, [('ro', '1'), ('lo', '2'), ('lu', '3'), ('ru', '4')]))
        nb = sorted(x for x in (1, 2, 3, 4) if x not in (nr, gegen))
        return A(R, f'Zwei Geraden schneiden sich in S. Die vier Winkel sind mit 1 bis 4 nummeriert. Welche Winkel sind Nebenwinkel von Winkel {nr}?', f'Winkel {nb[0]} und Winkel {nb[1]}',
                 [f'nur Winkel {gegen}', f'Winkel {gegen} und Winkel {nb[0]}', 'alle drei anderen'],
                 f'Nebenwinkel liegen neben Winkel {nr} an einer Geraden: Winkel {nb[0]} und {nb[1]}. Winkel {gegen} ist der Scheitelwinkel.', 'Nebenwinkel teilen sich einen Schenkel.',
                 grafik=einfach(a, [('ro', '1'), ('lo', '2'), ('lu', '3'), ('ru', '4')]))
    art = R.choice(['verh', 'sechs', 'sechs', 'summe'])
    if art == 'verh':
        p, q = R.choice([(1, 2), (2, 3), (1, 3), (1, 4), (4, 5), (2, 7), (3, 7), (1, 5), (7, 8)])
        if 180 * p % (p + q): return gen_scheitel_neben(R, st)
        k = 180 // (p + q)
        return Z(f'Zwei Nebenwinkel verhalten sich wie {p} : {q}. Wie groß ist der kleinere?', p * k, f'180 / ({p} + {q}) * {p}',
                 f'{p} + {q} = {p + q} Teile = 180°, ein Teil = {g(k)}. Kleinerer Winkel: {p} · {g(k)} = {g(p * k)}.', 'Wie viele Teile sind es zusammen?')
    if art == 'sechs':
        w1 = R.randint(30, 100)
        w2 = R.randint(30, 150 - w1)
        if len({w1, w2, 180 - w1 - w2}) < 3: return gen_scheitel_neben(R, st)
        val = {1: w1, 2: w2, 3: 180 - w1 - w2}
        val.update({4: val[1], 5: val[2], 6: val[3]})
        kl = [(1, 4), (2, 5), (3, 6)]
        R.shuffle(kl)
        for _ in range(50):
            i, j = R.choice(kl[0]), R.choice(kl[1])
            if (i - j) % 6 not in (1, 5): break
        else:
            return gen_scheitel_neben(R, st)
        t = R.choice(kl[2])
        x, y = sorted((val[i], val[j]))
        return Z(f'Drei Geraden schneiden sich in einem Punkt und bilden sechs Winkel. Zwei davon sind {g(x)} und {g(y)} groß (siehe Bild). '
                 'Wie groß ist der mit „?“ markierte Winkel?', val[t], f'180 - {x} - {y}',
                 f'Ersetze einen der beiden Winkel durch seinen Scheitelwinkel. Dann liegen {g(x)}, {g(y)} und „?“ nebeneinander an einer Geraden: '
                 f'180° − {g(x)} − {g(y)} = {g(val[t])}.', 'Drei nebeneinander liegende Winkel ergeben 180°. Scheitelwinkel helfen beim Verschieben.',
                 grafik=drei_geraden(w1, w2, {i: g(val[i]), j: g(val[j]), t: '?'}))
    s = R.choice(range(60, 300, 4))
    if s > 180: s = 360 - s
    return Z(f'Zwei Geraden schneiden sich. Zwei Scheitelwinkel ergeben zusammen {g(s)}. Wie groß ist einer der beiden anderen Winkel?', 180 - s // 2,
             f'180 - {s} / 2', f'Ein Scheitelwinkel: {g(s)} : 2 = {g(s // 2)}. Sein Nebenwinkel: 180° − {g(s // 2)} = {g(180 - s // 2)}.',
             'Scheitelwinkel sind gleich groß. Die anderen beiden sind ihre Nebenwinkel.')


# Paare (Lage bei S, Lage bei T, Name). „weder noch“ nur für Paare, die an Parallelen nie gleich groß sind (außer bei 90°).
# Die äußeren Paare (z. B. S rechts oberhalb / T links unterhalb) kommen nicht vor: Manche Bücher nennen sie Wechselwinkel, manche nicht.
NAMEN_PAARE = [('ro', 'ro', 'Stufenwinkel'), ('lo', 'lo', 'Stufenwinkel'), ('lu', 'lu', 'Stufenwinkel'), ('ru', 'ru', 'Stufenwinkel'),
               ('lu', 'ro', 'Wechselwinkel'), ('ru', 'lo', 'Wechselwinkel'), ('ro', 'lo', 'weder noch'), ('lu', 'ru', 'weder noch')]


def gen_stufen_wechsel(R, st):
    a = _paar(R)
    if st == 1:
        if R.random() < 0.5:
            pos = R.choice(list(POS_TEXT))
            return Z(f'g ∥ h. Bei S ist der Winkel {POS_TEXT[pos]} {g(a)} groß. Wie groß ist der Winkel bei T in derselben Lage?', a, f'{a}',
                     f'Stufenwinkel an Parallelen sind gleich groß: {g(a)}.', 'Gleiche Lage an beiden Kreuzungen: Stufenwinkel.',
                     grafik=doppel(a if pos in ('ro', 'lu') else 180 - a, [('S', pos, g(a)), ('T', pos, '?')]))
        return Z(f'g ∥ h. Bei S ist der Winkel links unterhalb {g(a)} groß. Wie groß ist sein Wechselwinkel bei T (rechts oberhalb)?', a, f'{a}',
                 f'Wechselwinkel an Parallelen sind gleich groß: {g(a)}.', 'Wechselwinkel liegen über Kreuz zwischen den Parallelen.',
                 grafik=doppel(a, [('S', 'lu', g(a)), ('T', 'ro', '?')]))
    if st == 2:
        if R.random() < 0.5:
            p1, p2 = R.choice([('ro', 'lo'), ('ro', 'ru'), ('lu', 'lo'), ('lo', 'ro'), ('ru', 'lu')])
            gross = {'ro': 1, 'lu': 1, 'lo': 0, 'ru': 0}
            w2 = a if gross[p1] == gross[p2] else 180 - a
            zeich = a if gross[p1] else 180 - a
            return Z(f'g ∥ h. Bei S ist der Winkel {POS_TEXT[p1]} {g(a)} groß. Wie groß ist der Winkel bei T {POS_TEXT[p2]}?', w2, f'{w2}',
                     f'Stufenwinkel: Bei T {POS_TEXT[p1]} ist auch {g(a)}. Der gesuchte Winkel ist dessen Nebenwinkel: 180° − {g(a)} = {g(w2)}.',
                     'Übertrage den Winkel zuerst mit dem Stufenwinkel nach T.', grafik=doppel(zeich, [('S', p1, g(a)), ('T', p2, '?')]))
        s, t, name = R.choice(NAMEN_PAARE)
        return A(R, f'g ∥ h. Wie heißen der Winkel bei S {POS_TEXT[s]} (1) und der Winkel bei T {POS_TEXT[t]} (2)?', name,
                 [x for x in ['Stufenwinkel', 'Wechselwinkel', 'Scheitelwinkel', 'weder noch'] if x != name],
                 'Gleiche Lage: Stufenwinkel. Über Kreuz zwischen den Parallelen: Wechselwinkel. Scheitelwinkel liegen an derselben Kreuzung. '
                 + ('Diese beiden Winkel sind an Parallelen nie gleich groß (außer bei 90°): weder noch.' if name == 'weder noch' else f'Hier: {name}.'),
                 'Liegen beide in gleicher Lage oder über Kreuz zwischen g und h?', grafik=doppel(60, [('S', s, '1'), ('T', t, '2')]))
    art = R.choice(['kette', 'wechsel_neben', 'scheitel_stufe'])
    if art == 'kette':
        b = R.randint(25, 85)
        return Z(f'g ∥ h. Bei S ist der Winkel links oberhalb {g(180 - b)} groß. Wie groß ist der Winkel bei T rechts oberhalb?', b, f'180 - {180 - b}',
                 f'Bei S rechts oberhalb: Nebenwinkel 180° − {g(180 - b)} = {g(b)}. Stufenwinkel bei T: {g(b)}.', 'Erst Nebenwinkel bei S, dann Stufenwinkel.',
                 grafik=doppel(b, [('S', 'lo', g(180 - b)), ('T', 'ro', '?')]))
    if art == 'wechsel_neben':
        x = R.randint(95, 155)
        return Z(f'g ∥ h. Bei T ist der Winkel rechts unterhalb {g(x)} groß. Wie groß ist der Winkel bei S links unterhalb?', 180 - x, f'180 - {x}',
                 f'Bei T rechts oberhalb liegt der Nebenwinkel: 180° − {g(x)} = {g(180 - x)}. Bei S links unterhalb liegt sein Wechselwinkel: {g(180 - x)}.',
                 'Erst Nebenwinkel bei T, dann Wechselwinkel.', grafik=doppel(180 - x, [('T', 'ru', g(x)), ('S', 'lu', '?')]))
    w = 180 - a
    return Z(f'g ∥ h. Bei S ist der Winkel links oberhalb {g(w)} groß. Wie groß ist der Winkel bei T rechts unterhalb?', w, f'{w}',
             f'Bei S rechts unterhalb liegt der Scheitelwinkel: {g(w)}. Bei T rechts unterhalb liegt dazu der Stufenwinkel: {g(w)}.',
             'Erst Scheitelwinkel bei S, dann Stufenwinkel.', grafik=doppel(a, [('S', 'lo', g(w)), ('T', 'ru', '?')]))


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
        if R.random() < 0.6:
            ok = R.random() < 0.5
            b = 180 - a if ok else 180 - a + R.choice([-12, -10, -8, 8, 10, 12])
            if not 15 <= b <= 165: return gen_parallel_pruefen(R, st)
            return A(R, f'k schneidet g in S und h in T. Bei S ist der Winkel rechts oberhalb {g(a)}, bei T der Winkel rechts unterhalb {g(b)}. Sind g und h parallel?',
                     'Ja' if ok else 'Nein', ['Ja' if not ok else 'Nein', 'Nur wenn beide Winkel gleich groß sind'],
                     f'Bei T rechts oberhalb ist der Nebenwinkel 180° − {g(b)} = {g(180 - b)}. Er ist {"gleich groß wie" if ok else "anders als"} der Stufenwinkel bei S ({g(a)}): '
                     f'{"parallel" if ok else "nicht parallel"}.', 'Bilde bei T den Nebenwinkel und vergleiche dann Stufenwinkel.',
                     grafik=doppel(a, [('S', 'ro', g(a)), ('T', 'ru', g(b))], b=180 - b))
        d = R.randint(1, 9)
        return Z(f'k schneidet g unter {g(a)} und h unter {g(a + d)} (beide Winkel rechts oberhalb). Um wie viel Grad muss man h drehen, damit h ∥ g wird?', d,
                 f'{a + d} - {a}', f'Die Stufenwinkel müssen gleich werden: {g(a + d)} − {g(a)} = {g(d)}.', 'Welcher Unterschied muss verschwinden?')
    if R.random() < 0.6:
        b = a + R.choice([x for x in range(-15, 16) if abs(x) >= 6])
        if not 25 <= b <= 155 or b == 90: return gen_parallel_pruefen(R, st)
        return Z(f'k schneidet g unter {g(a)} und h unter {g(b)} (beide Winkel rechts oberhalb, siehe Bild). Unter welchem Winkel schneiden sich g und h?', abs(a - b),
                 f'abs({a} - {b})', f'Zeichne durch T die Parallele zu g. Sie bildet mit k den Stufenwinkel {g(a)}, h bildet mit k {g(b)}. '
                 f'Also ist h gegen diese Parallele – und damit gegen g – um {g(a)} − {g(b)} = {g(abs(a - b))} geneigt.' if a > b else
                 f'Zeichne durch T die Parallele zu g. Sie bildet mit k den Stufenwinkel {g(a)}, h bildet mit k {g(b)}. '
                 f'Also ist h gegen diese Parallele – und damit gegen g – um {g(b)} − {g(a)} = {g(abs(a - b))} geneigt.',
                 'Zeichne durch T eine Parallele zu g und vergleiche die Stufenwinkel.', grafik=doppel(a, [('S', 'ro', g(a)), ('T', 'ro', g(b))], b=b))
    if R.random() < 0.6:
        x = R.randint(35, 145)
        d = R.choice([-5, -4, -3, 3, 4, 5])
        namen = ['g', 'h', 'i']
        anders = R.randrange(3)
        w = [x + d if j == anders else x for j in range(3)]
        paar = ' und '.join(n for j, n in enumerate(namen) if j != anders)
        return A(R, f'Eine Gerade k schneidet die Geraden g, h und i. Die Winkel rechts oberhalb sind bei g {g(w[0])}, bei h {g(w[1])} und bei i {g(w[2])}. '
                 'Welche Geraden sind sicher parallel?', paar, [x for x in ('g und h', 'g und i', 'h und i', 'alle drei') if x != paar],
                 f'Nur gleich große Stufenwinkel zeigen Parallelität: {paar} (je {g(x)}). Die dritte Gerade hat {g(x + d)} und ist zu beiden nicht parallel.',
                 'Vergleiche die Stufenwinkel paarweise.')
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
        art = R.choice(['doppelt', 'beweis', 'beweis', 'rechter'])
        if art == 'doppelt':
            k = R.choice([2, 3, 4])
            gg = R.choice(range(30, 120, 2))
            if (180 - gg) % (k + 1): return gen_innenwinkelsumme(R, st)
            x = (180 - gg) // (k + 1)
            return Z(f'In einem Dreieck ist β {k}-mal so groß wie α, und γ = {g(gg)}. Wie groß ist α?', x, f'(180 - {gg}) / ({k} + 1)',
                     f'Für α und β bleiben 180° − {g(gg)} = {g(180 - gg)}. Das sind 1 + {k} = {k + 1} gleiche Teile: α = {g(180 - gg)} : {k + 1} = {g(x)}.',
                     'α ist ein Teil, β sind so viele Teile, wie es mal so groß ist.')
        if art == 'rechter':
            x = R.randint(15, 75)
            return Z(f'Ein Dreieck hat einen rechten Winkel und einen Winkel von {g(x)}. Wie groß ist der dritte Winkel?', 90 - x, f'180 - 90 - {x}',
                     f'180° − 90° − {g(x)} = {g(90 - x)}.', 'Ein rechter Winkel hat 90°.', grafik=dreieck(90, x, [('A', '90°'), ('B', g(x)), ('C', '?')]))
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
    art = R.choice(['rechtwinklig', 'verh', 'verlaengert'])
    if art == 'rechtwinklig':
        d = R.choice(range(4, 60, 2))
        return Z(f'Ein Dreieck ist rechtwinklig. Ein spitzer Winkel ist um {g(d)} größer als der andere. Wie groß ist der größere spitze Winkel?', (90 + d) // 2,
                 f'(90 + {d}) / 2', f'Die spitzen Winkel ergeben zusammen 90°. Ohne den Unterschied bleiben 90° − {g(d)} = {g(90 - d)} für zwei gleiche Winkel, '
                 f'je {g((90 - d) // 2)}. Der größere: {g((90 - d) // 2)} + {g(d)} = {g((90 + d) // 2)}.', 'Die beiden spitzen Winkel ergeben zusammen 90°.')
    if art == 'verlaengert':
        return Z(f'Im Dreieck ABC ist α = {g(a)}. Die Seite [AB] ist über B hinaus verlängert. Dort bildet sie mit [BC] den Winkel {g(180 - b)}. Wie groß ist γ?', c,
                 f'180 - {a} - (180 - {180 - b})', f'Der Winkel {g(180 - b)} ist Nebenwinkel von β: β = 180° − {g(180 - b)} = {g(b)}. γ = 180° − {g(a)} − {g(b)} = {g(c)}.',
                 'Bestimme zuerst β mit dem Nebenwinkel.', grafik=dreieck(a, b, [('A', f'α = {g(a)}'), ('C', '?')], aussen=('B', g(180 - b))))
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
        art = R.choice(['B', 'C', 'welcher'])
        if art == 'B':
            return Z(f'Der Außenwinkel bei B ist {g(180 - b)}, und α = {g(a)}. Wie groß ist γ?', c, f'(180 - {b}) - {a}',
                     f'Außenwinkel bei B = α + γ. Also γ = {g(180 - b)} − {g(a)} = {g(c)}.', 'Der Außenwinkel bei B ist so groß wie α und γ zusammen.',
                     grafik=dreieck(a, b, [('A', g(a)), ('C', '?')], aussen=('B', g(180 - b))))
        if art == 'C':
            return Z(f'In einem Dreieck ist α = {g(a)}, und der Außenwinkel bei C ist {g(a + b)}. Wie groß ist β?', b, f'{a + b} - {a}',
                     f'Außenwinkel bei C = α + β. Also β = {g(a + b)} − {g(a)} = {g(b)}.', 'Welche zwei Innenwinkel ergeben zusammen den Außenwinkel bei C?',
                     grafik=dreieck(a, b, [('A', g(a)), ('B', '?')], aussen=('C', g(a + b))))
        e = R.choice('ABC')
        rest = {'A': 'β und γ', 'B': 'α und γ', 'C': 'α und β'}
        namen = {'A': 'α', 'B': 'β', 'C': 'γ'}
        return A(R, f'Welche Innenwinkel des Dreiecks ABC ergeben zusammen genau den Außenwinkel bei {e}?', rest[e],
                 [f'{namen[e]} allein', f'{namen[e]} und {rest[e].split(" und ")[0]}', 'alle drei Innenwinkel'],
                 f'Der Außenwinkel bei {e} ist so groß wie die beiden Innenwinkel, die nicht bei {e} liegen: {rest[e]}.', 'Welche Innenwinkel liegen nicht an dieser Ecke?',
                 grafik=dreieck(55, 65, [], aussen=(e, '?')))
    art = R.choice(['summe', 'zwei', 'verh'])
    if art == 'summe':
        return Z(f'Bei einem Dreieck sind zwei Außenwinkel {g(180 - a)} und {g(180 - b)}. Wie groß ist der dritte Außenwinkel?', 180 - c,
                 f'360 - {180 - a} - {180 - b}', f'Die drei Außenwinkel ergeben 360°: 360° − {g(180 - a)} − {g(180 - b)} = {g(180 - c)}.',
                 'Rechne mit den Innenwinkeln nach oder nutze die Summe der Außenwinkel.')
    if art == 'zwei':
        return Z(f'Die Außenwinkel bei A und B sind {g(180 - a)} und {g(180 - b)}. Wie groß ist γ?', c, f'180 - (180 - {180 - a}) - (180 - {180 - b})',
                 f'α = 180° − {g(180 - a)} = {g(a)}, β = 180° − {g(180 - b)} = {g(b)}. γ = 180° − {g(a)} − {g(b)} = {g(c)}.', 'Bestimme erst die Innenwinkel bei A und B.')
    p, q = R.choice([(1, 2), (2, 3), (1, 3), (3, 4), (2, 5), (3, 5), (4, 5)])
    y = R.choice([x for x in range(60, 165) if x % (p + q) == 0])
    k = y // (p + q)
    return Z(f'Der Außenwinkel bei C eines Dreiecks ist {g(y)}. Die Innenwinkel α und β verhalten sich wie {p} : {q}. Wie groß ist α?', p * k, f'{y} / ({p} + {q}) * {p}',
             f'Außenwinkel bei C = α + β = {g(y)}. Das sind {p} + {q} = {p + q} Teile, ein Teil = {g(k)}. α = {p} · {g(k)} = {g(p * k)}.',
             'Erst den Außenwinkelsatz, dann in Teile aufteilen.')


def _vier(R, n, lo, hi):
    """n − 1 zufällige Innenwinkel eines n-Ecks und der fehlende."""
    ws = [R.randint(lo, hi) for _ in range(n - 1)]
    return ws, (n - 2) * 180 - sum(ws)


def gen_vieleck(R, st):
    if st == 1:
        if R.random() < 0.5:
            ws, d = _vier(R, 4, 55, 130)
            if not 40 <= d <= 165: return gen_vieleck(R, st)
            a, b, c = ws
            return Z(f'In einem Viereck ist α = {g(a)}, β = {g(b)} und γ = {g(c)}. Wie groß ist δ?', d, f'360 - {a} - {b} - {c}',
                     f'Winkelsumme im Viereck 360°: 360° − {g(a)} − {g(b)} − {g(c)} = {g(d)}.', 'Ein Viereck zerfällt in zwei Dreiecke.',
                     grafik=vieleck_fig([a, b, c, d], {0: f'α = {g(a)}', 1: f'β = {g(b)}', 2: f'γ = {g(c)}', 3: 'δ = ?'}))
        n = R.randint(5, 12)
        return Z(f'Wie groß ist die Winkelsumme in einem {n}-Eck?', (n - 2) * 180, f'({n} - 2) * 180', f'Von einer Ecke aus entstehen {n} − 2 = {n - 2} Dreiecke: '
                 f'{n - 2} · 180° = {g((n - 2) * 180)}.', 'Wie viele Dreiecke entstehen von einer Ecke aus?', grafik=regelmaessig(n, diagonalen=True))
    if st == 2:
        art = R.choice(['regel', 'dreiecke', 'fehlend5'])
        if art == 'regel':
            n = R.choice([5, 6, 8, 9, 10, 12, 15, 18, 20])
            w = Fr((n - 2) * 180, n)
            return Z(f'Wie groß ist jeder Innenwinkel eines regelmäßigen {n}-Ecks?', w, f'({n} - 2) * 180 / {n}',
                     f'Winkelsumme ({n} − 2) · 180° = {g((n - 2) * 180)}, verteilt auf {n} gleiche Winkel: {g((n - 2) * 180)} : {n} = {g(w)}.',
                     'Erst die Winkelsumme, dann gleichmäßig verteilen.', grafik=regelmaessig(n, {0: '?'}))
        if art == 'dreiecke':
            n = R.randint(6, 14)
            return Z(f'Von einer Ecke eines {n}-Ecks zieht man alle Diagonalen. In wie viele Dreiecke wird das {n}-Eck zerlegt?', n - 2, f'{n} - 2',
                     f'Die Ecke selbst und ihre beiden Nachbarn liefern keine Diagonale: {n} − 3 Diagonalen, {n} − 2 Dreiecke.', 'Probiere es mit einem Fünfeck aus.',
                     einheit=None, grafik=regelmaessig(n))
        ws, f = _vier(R, 5, 90, 135)
        if not 60 <= f <= 170: return gen_vieleck(R, st)
        return Z(f'Ein Fünfeck hat die Winkel {", ".join(g(x) for x in ws)} und einen fünften Winkel. Wie groß ist er?', f, f'540 - {" - ".join(map(str, ws))}',
                 f'Winkelsumme im Fünfeck: 3 · 180° = 540°. 540° − {g(sum(ws))} = {g(f)}.', 'Winkelsumme im Fünfeck: (5 − 2) · 180°.',
                 grafik=vieleck_fig(ws + [f], {**{i: g(x) for i, x in enumerate(ws)}, 4: '?'}))
    art = R.choice(['summe_n', 'viereck_teile', 'sechseck'])
    if art == 'summe_n':
        n = R.randint(6, 20)
        s = (n - 2) * 180
        return Z(f'Ein Vieleck hat die Winkelsumme {g(s)}. Wie viele Ecken hat es?', n, f'{s} / 180 + 2',
                 f'{g(s)} : 180° = {n - 2} Dreiecke. Ein Vieleck mit {n - 2} Dreiecken hat 2 Ecken mehr: {n} Ecken.', 'Teile durch 180° und denke an das „− 2“.', einheit=None)
    if art == 'viereck_teile':
        x = R.randint(20, 50)
        d = 360 - 6 * x
        if not 20 < d < 180: return gen_vieleck(R, st)
        return Z(f'In einem Viereck ist β doppelt so groß wie α, γ dreimal so groß wie α, und δ = {g(d)}. Wie groß ist α?', x, f'(360 - {d}) / 6',
                 f'Für α, β und γ bleiben 360° − {g(d)} = {g(360 - d)}. Das sind 1 + 2 + 3 = 6 gleiche Teile: α = {g(360 - d)} : 6 = {g(x)}.',
                 'α ist ein Teil. Wie viele Teile sind β und γ?')
    x = R.randint(92, 148)
    r = 360 - 2 * x
    return Z(f'Ein Sechseck hat vier Winkel von je {g(x)}. Die beiden anderen Winkel sind gleich groß. Wie groß ist einer davon?', r, f'(720 - 4 * {x}) / 2',
             f'Winkelsumme im Sechseck: 4 · 180° = 720°. 720° − 4 · {g(x)} = {g(720 - 4 * x)}, davon die Hälfte: {g(r)}.', 'Erst die Winkelsumme des Sechsecks.')


def gen_figuren(R, st):
    if st == 1:
        a, b = _drei(R)
        if R.random() < 0.5:
            return Z(f'g ∥ h. Die Ecke C eines Dreiecks liegt auf g, A und B liegen auf h. ∢BAC = {g(a)}. Welchen Winkel bildet [CA] links von C mit g?', a, f'{a}',
                     f'[CA] schneidet die Parallelen g und h. Der Winkel links bei C und ∢BAC sind Wechselwinkel: {g(a)}.', 'Die Seite [CA] schneidet beide Parallelen.',
                     grafik=dreieck_par(a, b, [('A', g(a)), ('Cl', '?')]))
        x = R.choice([y for y in range(40, 141) if y != 90])
        return Z(f'In einem Parallelogramm ABCD ist ∢BAD = {g(x)}. Wie groß ist ∢CBA?', 180 - x, f'180 - {x}',
                 f'[AD] ∥ [BC], und [AB] schneidet beide. ∢BAD und ∢CBA liegen an derselben Seite [AB] zwischen den Parallelen: Sie ergänzen sich zu 180°. '
                 f'180° − {g(x)} = {g(180 - x)}.', 'Verlängere [AB] über B hinaus: Stufenwinkel, dann Nebenwinkel.',
                 grafik=parallelogramm(x, [('A', g(x)), ('B', '?')]))
    if st == 2:
        art = R.choice(['trapez', 'raute', 'dreieck_par'])
        if art == 'trapez':
            a = R.randint(40, 85)
            return Z(f'Ein Trapez ABCD hat [AB] ∥ [CD]. ∢BAD = {g(a)}. Wie groß ist ∢ADC?', 180 - a, f'180 - {a}',
                     f'[AD] schneidet die Parallelen AB und CD. ∢BAD und ∢ADC liegen an derselben Seite [AD] zwischen den Parallelen: 180° − {g(a)} = {g(180 - a)}.',
                     'Verlängere [AB] über A hinaus: Stufenwinkel und Nebenwinkel.', grafik=trapez(a, 65, [('A', g(a)), ('D', '?')]))
        if art == 'raute':
            a = R.choice([x for x in range(40, 141, 2) if x != 90])
            return Z(f'In einer Raute ABCD ist ∢BAD = {g(a)}. Die Diagonale [AC] ist eingezeichnet. Wie groß ist ∢BAC?', a // 2, f'{a} / 2',
                     f'Die Diagonale [AC] ist Symmetrieachse der Raute und halbiert den Winkel bei A: {g(a)} : 2 = {g(a // 2)}.', 'Was macht eine Symmetrieachse mit dem Eckwinkel?',
                     grafik=parallelogramm(a, [('A', g(a)), ('A_AB', '?')], p=4, q=4, diagonale=True))
        a, b = _drei(R)
        return Z(f'g ∥ h. Die Ecke C eines Dreiecks liegt auf g, A und B liegen auf h. Bei C bildet [CA] mit g links den Winkel {g(a)}, [CB] mit g rechts den Winkel {g(b)}. '
                 'Wie groß ist der Innenwinkel bei C?', 180 - a - b, f'180 - {a} - {b}',
                 f'An C liegen auf g drei Winkel nebeneinander: 180° − {g(a)} − {g(b)} = {g(180 - a - b)}.', 'Winkel an einer Geraden ergeben 180°.',
                 grafik=dreieck_par(a, b, [('Cl', g(a)), ('Cr', g(b)), ('C', '?')]))
    art = R.choice(['kette', 'zwei_par', 'dia'])
    if art == 'kette':
        a, b = R.randint(25, 70), R.randint(25, 70)
        return Z(f'g ∥ h. Ein Weg geht von A auf g zu einem Punkt P zwischen den Geraden und weiter zu B auf h. Bei A bildet der Weg mit g den Winkel {g(a)}, '
                 f'bei B mit h den Winkel {g(b)} (siehe Bild). Wie groß ist ∢APB?', a + b, f'{a} + {b}',
                 f'Hilfslinie durch P parallel zu g: Sie teilt ∢APB in zwei Wechselwinkel {g(a)} und {g(b)}. Zusammen {g(a + b)}.',
                 'Zeichne durch P eine Parallele zu g.', grafik=weg(a, b, [('A', g(a)), ('B', g(b)), ('P', '?')]))
    if art == 'zwei_par':
        a, b = _drei(R)
        return Z(f'g ∥ h. Die Ecke C eines Dreiecks liegt auf g, A und B liegen auf h. ∢BAC = {g(a)}, und [CB] bildet mit g rechts von C den Winkel {g(b)}. '
                 'Wie groß ist ∢ACB?', 180 - a - b, f'180 - {a} - {b}',
                 f'Links bei C bilden [CA] und g den Wechselwinkel zu ∢BAC: {g(a)}. Auf g liegen bei C drei Winkel nebeneinander: ∢ACB = 180° − {g(a)} − {g(b)} = {g(180 - a - b)}.',
                 'Bringe ∢BAC mit einem Wechselwinkel nach C.', grafik=dreieck_par(a, b, [('A', g(a)), ('Cr', g(b)), ('C', '?')]))
    a, b = R.randint(20, 60), R.randint(20, 60)
    p = 4 * math.sin(math.radians(b)) / math.sin(math.radians(a))
    if not 2.5 <= p <= 7: return gen_figuren(R, st)
    ziel = R.choice(['ACD', 'ACB', 'ABC'])
    wert = {'ACD': a, 'ACB': b, 'ABC': 180 - a - b}[ziel]
    weg_ = {'ACD': f'[AB] ∥ [DC], und [AC] schneidet beide: ∢ACD ist Wechselwinkel zu ∢BAC = {g(a)}.',
            'ACB': f'[AD] ∥ [BC], und [AC] schneidet beide: ∢ACB ist Wechselwinkel zu ∢CAD = {g(b)}.',
            'ABC': f'∢BAD = {g(a)} + {g(b)} = {g(a + b)}. ∢ABC liegt mit ∢BAD an derselben Seite [AB] zwischen den Parallelen [AD] und [BC]: '
                   f'180° − {g(a + b)} = {g(180 - a - b)}.'}[ziel]
    ort = {'ACD': 'C_CD', 'ACB': 'C_CB', 'ABC': 'B'}[ziel]
    return Z(f'Im Parallelogramm ABCD bildet die Diagonale [AC] mit [AB] den Winkel {g(a)} und mit [AD] den Winkel {g(b)}. Wie groß ist ∢{ziel}?', wert,
             {'ACD': f'{a}', 'ACB': f'{b}', 'ABC': f'180 - ({a} + {b})'}[ziel], weg_, 'Welche Seiten sind parallel, und welche Linie schneidet sie?',
             grafik=parallelogramm(a + b, [('A_AB', g(a)), ('A_AD', g(b)), (ort, '?')], p=p, q=4, diagonale=True))


BEGR = [('Nebenwinkel ergänzen sich zu 180°.', 'Zwei Winkel liegen an derselben Kreuzung nebeneinander an einer Geraden.'),
        ('Scheitelwinkel sind gleich groß.', 'Zwei Winkel liegen sich an derselben Kreuzung gegenüber.'),
        ('Stufenwinkel an Parallelen sind gleich groß.', 'Zwei Winkel liegen an zwei Kreuzungen mit Parallelen in gleicher Lage.'),
        ('Wechselwinkel an Parallelen sind gleich groß.', 'Zwei Winkel liegen an Parallelen über Kreuz zwischen den Geraden.'),
        ('Die Winkelsumme im Dreieck ist 180°.', 'Die drei Innenwinkel eines Dreiecks werden addiert.')]

# Stufe 2 (auch Test, Korrektur, Sicherung): Lernziel der Etappe – Fundamentalsatz/abgeleiteter Satz, Zirkelschluss, Reihenfolge einer Beweiskette.
WW, WS3, WS4 = 'Wechselwinkel an Parallelen sind gleich groß.', 'Die Winkelsumme im Dreieck ist 180°.', 'Die Winkelsumme im Viereck ist 360°.'
BEWEIS2 = [
    ('Welcher Satz ist in diesem Flug der Fundamentalsatz, also vorausgesetzt und nicht bewiesen?', WW,
     [WS3, WS4, 'Jedes n-Eck hat die Winkelsumme (n − 2) · 180°.'],
     'Am Anfang der Kette steht: Wechselwinkel an Parallelen sind gleich groß. Alle Winkelsummen werden daraus bewiesen.', 'Was steht ganz unten in der Kette?'),
    ('Ist der Satz „Die Winkelsumme im Dreieck ist 180°“ ein Fundamentalsatz oder ein abgeleiteter Satz?', 'ein abgeleiteter Satz',
     ['ein Fundamentalsatz', 'keins von beiden, eine Messregel', 'eine Definition'],
     'Er wird mit der Parallelen durch C und Wechselwinkeln bewiesen. Also ist er ein abgeleiteter Satz.', 'Wird der Satz bewiesen oder vorausgesetzt?'),
    ('Ist der Satz „Die Winkelsumme im Viereck ist 360°“ ein Fundamentalsatz oder ein abgeleiteter Satz?', 'ein abgeleiteter Satz',
     ['ein Fundamentalsatz', 'keins von beiden, eine Messregel', 'eine Definition'],
     'Er wird mit einer Diagonale aus der Winkelsumme im Dreieck bewiesen. Also ist er ein abgeleiteter Satz.', 'Wird der Satz bewiesen oder vorausgesetzt?'),
    ('Was unterscheidet einen Fundamentalsatz von einem abgeleiteten Satz?', 'Der Fundamentalsatz wird vorausgesetzt, der abgeleitete Satz wird bewiesen.',
     ['Der Fundamentalsatz ist länger.', 'Der abgeleitete Satz wird vorausgesetzt, der Fundamentalsatz bewiesen.', 'Es gibt keinen Unterschied.'],
     'Ein Fundamentalsatz ist der Anfang der Kette und wird angenommen. Abgeleitete Sätze werden mit früheren Sätzen bewiesen.', 'Welcher Satz braucht keinen Beweis?'),
    ('Aus welchem Satz wird die Winkelsumme im Viereck bewiesen?', 'aus der Winkelsumme im Dreieck',
     ['aus der Winkelsumme im Fünfeck', 'aus dem Satz über Scheitelwinkel allein', 'aus gar keinem, sie wird vorausgesetzt'],
     'Eine Diagonale teilt das Viereck in zwei Dreiecke mit je 180°.', 'Welche Hilfslinie zerlegt das Viereck?'),
    ('Aus welchem Satz wird die Winkelsumme im n-Eck bewiesen?', 'aus der Winkelsumme im Dreieck',
     ['aus der Winkelsumme im (n + 1)-Eck', 'aus dem Satz über Nebenwinkel allein', 'aus gar keinem, sie wird vorausgesetzt'],
     'Die Diagonalen von einer Ecke zerlegen das n-Eck in n − 2 Dreiecke mit je 180°.', 'In welche Figuren zerlegt man das n-Eck?'),
    ('Der Satz über Wechselwinkel ist vorausgesetzt. Womit beweist man daraus „Stufenwinkel an Parallelen sind gleich groß“?', 'mit dem Satz über Wechselwinkel und dem Satz über Scheitelwinkel',
     ['mit der Winkelsumme im Dreieck', 'mit der Winkelsumme im Viereck', 'gar nicht, das ist ein zweiter Fundamentalsatz'],
     'Beispiel: Der Winkel bei S links unterhalb ist so groß wie sein Wechselwinkel bei T rechts oberhalb. Dessen Scheitelwinkel ist der Winkel bei T links unterhalb. '
     'Also sind die Stufenwinkel bei S und T links unterhalb gleich groß.',
     'Wie liegen Stufenwinkel und Wechselwinkel an derselben Kreuzung zueinander?'),
    ('Jemand begründet die Winkelsumme im Dreieck so: „Ein Viereck hat 360°, und eine Diagonale teilt es in zwei Dreiecke.“ Was ist das Problem?',
     'Ein Zirkelschluss: Die Winkelsumme im Viereck wurde selbst mit der im Dreieck bewiesen.',
     ['Kein Problem, das ist ein gültiger Beweis.', 'Die Winkelsumme im Viereck ist falsch.', 'Man muss die Winkel zuerst messen.'],
     'Der Viereck-Satz folgt aus dem Dreieck-Satz. Ihn zum Beweis des Dreieck-Satzes zu nutzen, ist ein Zirkelschluss.', 'Woraus wurde der Viereck-Satz bewiesen?'),
    ('Jemand beweist den Satz über Wechselwinkel mit der Winkelsumme im Dreieck und die Winkelsumme mit dem Satz über Wechselwinkel. Was ist das Problem?',
     'Ein Zirkelschluss: Einer der beiden Sätze muss vorausgesetzt werden.',
     ['Kein Problem, beide Sätze sind ja richtig.', 'Der Satz über Wechselwinkel gilt nur ohne Parallelen.', 'Man braucht noch einen dritten Beweis mit Messen.'],
     'Stützen sich zwei Sätze gegenseitig, ist keiner bewiesen. Einer muss als Fundamentalsatz am Anfang stehen.', 'Womit fängt die Kette an?'),
    ('Was ist ein Zirkelschluss?', 'ein Beweis, der den Satz benutzt, den er erst beweisen soll',
     ['ein Beweis mit einem Zirkel', 'ein Beweis, der mit einem Fundamentalsatz beginnt', 'ein Beweis mit einer Zeichnung'],
     'Beim Zirkelschluss dreht sich die Begründung im Kreis: Das Ergebnis wird schon vorausgesetzt.', 'Wo dreht sich die Begründung im Kreis?'),
    ('Welche Reihenfolge der Sätze ist richtig, wenn jeder Satz aus dem vorigen bewiesen wird?',
     'Wechselwinkel-Satz → Winkelsumme im Dreieck → Winkelsumme im Viereck',
     ['Winkelsumme im Viereck → Winkelsumme im Dreieck → Wechselwinkel-Satz', 'Winkelsumme im Dreieck → Wechselwinkel-Satz → Winkelsumme im Viereck',
      'Winkelsumme im Viereck → Wechselwinkel-Satz → Winkelsumme im Dreieck'],
     'Der Wechselwinkel-Satz (Wechselwinkel an Parallelen sind gleich groß) ist der Fundamentalsatz. Aus ihm folgt die Winkelsumme im Dreieck, daraus die im Viereck.', 'Was steht am Anfang?'),
    ('Beweis der Winkelsumme im Dreieck. Was ist der nächste Schritt, nachdem die Parallele p durch C gezeichnet ist?',
     'Die Winkel links und rechts von C auf p sind so groß wie α und β (Wechselwinkel).',
     ['Die drei Winkel an C ergeben zusammen 180°.', 'α, β und γ werden gemessen.', 'Das Dreieck wird an p gespiegelt.'],
     'Erst müssen α und β mit Wechselwinkeln nach C gebracht werden. Danach liegen alle drei Winkel auf p nebeneinander.', 'Was braucht man, bevor man über die drei Winkel auf p reden kann?', B_DP),
    ('Beweis der Winkelsumme im Dreieck. Welcher Schritt kommt zuletzt?', 'α, γ und β liegen auf p nebeneinander und ergeben zusammen 180°.',
     ['Zeichne durch C die Parallele p zu [AB].', 'Die Winkel links und rechts von C sind Wechselwinkel zu α und β.', 'Wähle ein beliebiges Dreieck ABC.'],
     'Die Kette: Dreieck wählen, Parallele zeichnen, Wechselwinkel, zuletzt der gestreckte Winkel auf p.', 'Was folgt aus allen anderen Schritten?', B_DP),
    ('Beweis der Winkelsumme. Schritt 1: Zeichne durch C die Parallele p zu [AB]. Schritt 3: Auf p liegen α, γ und β nebeneinander: 180°. Was ist Schritt 2?',
     'Die Winkel an C links und rechts sind so groß wie α und β (Wechselwinkel).',
     ['Die Winkelsumme im Dreieck ist 180°.', 'Scheitelwinkel an C sind gleich groß.', 'p und [AB] schneiden sich in C.'],
     'Zwischen Hilfslinie und gestrecktem Winkel fehlt der Grund, warum α und β an C auftauchen: Wechselwinkel an p ∥ [AB].', 'Wie kommen α und β nach C?', B_DP),
    ('Beweis der Winkelsumme im Viereck ABCD. Schritt 1: Zeichne die Diagonale [AC]. Schritt 3: Also ist die Winkelsumme 360°. Was ist Schritt 2?',
     'Beide Dreiecke ABC und ACD haben je 180°, ihre Winkel bilden zusammen die vier Viereckswinkel.',
     ['Jeder Winkel im Viereck ist 90°.', 'Die Diagonale halbiert jeden Winkel.', 'Die Winkelsumme im Fünfeck ist 540°.'],
     'Die Diagonale zerlegt das Viereck in zwei Dreiecke. Ihre sechs Winkel ergeben zusammen genau die vier Winkel des Vierecks.', 'Was weißt du über die beiden Dreiecke?'),
    ('Darf man im Beweis der Winkelsumme im Dreieck den Satz „Winkel nebeneinander auf einer Geraden ergeben 180°“ benutzen?',
     'Ja, er steht vorher fest und hängt nicht von der Winkelsumme ab.',
     ['Nein, das wäre ein Zirkelschluss.', 'Nein, im Beweis darf man gar keinen Satz benutzen.', 'Nur, wenn man die Winkel vorher misst.'],
     'Der gestreckte Winkel (180°) ist vorher bekannt. Er stützt sich nicht auf die Winkelsumme im Dreieck – also kein Zirkelschluss.', 'Wurde dieser Satz mit der Winkelsumme bewiesen?'),
    ('Darf man im Beweis der Winkelsumme im Dreieck die Winkelsumme im Fünfeck (540°) benutzen?', 'Nein: Sie wird selbst aus der Winkelsumme im Dreieck bewiesen.',
     ['Ja, sie ist ja richtig.', 'Ja, weil 540° mehr als 180° ist.', 'Ja, wenn man ein Fünfeck zeichnet.'],
     'Der Fünfeck-Satz folgt aus dem Dreieck-Satz (3 · 180°). Ihn zu benutzen, wäre ein Zirkelschluss.', 'Woraus folgt der Fünfeck-Satz?'),
]


def gen_beweisen(R, st):
    if st == 1:
        i = R.randrange(len(BEGR))
        satz, lage = BEGR[i]
        return A(R, f'Welcher Winkelsatz passt zu dieser Lage? {lage}', satz, R.sample([s for j, (s, _) in enumerate(BEGR) if j != i], 3),
                 f'Passend ist: {satz}', 'Wo liegen die Winkel: an einer oder an zwei Kreuzungen?')
    if st == 2:
        t, r, f, w, h, *bild = R.choice(BEWEIS2)
        return A(R, t, r, f, w, h, grafik=bild[0] if bild else None)
    art = R.choice(['gegen', 'stumpf', 'viereck', 'fuenfeck', 'umkehr', 'messung'])
    if art == 'gegen':
        return A(R, 'Behauptung: „Wenn zwei Winkel zusammen 180° ergeben, sind sie Nebenwinkel.“ Was stimmt?', 'Falsch: Auch zwei Winkel an verschiedenen Stellen können zusammen 180° ergeben.',
                 ['Richtig, das ist die Definition.', 'Richtig, denn Nebenwinkel ergeben 180°.', 'Falsch: Nebenwinkel ergeben 360°.'],
                 'Gegenbeispiel: Im Parallelogramm ergeben die beiden Winkel an derselben Seite zusammen 180°, liegen aber an verschiedenen Ecken. '
                 'Die Umkehrung eines Satzes muss eigens geprüft werden.', 'Suche ein Gegenbeispiel.')
    if art == 'stumpf':
        return A(R, 'Warum kann ein Dreieck höchstens einen stumpfen Winkel haben?', 'Zwei stumpfe Winkel wären zusammen schon mehr als 180°.',
                 ['Weil stumpfe Winkel immer bei C liegen.', 'Weil man es so zeichnet.', 'Das stimmt nicht, es können zwei sein.'],
                 'Ein stumpfer Winkel ist größer als 90°. Zwei davon ergäben mehr als 180° – mehr als die ganze Winkelsumme.', 'Denke an die Winkelsumme.')
    if art == 'viereck':
        return A(R, 'Wie beweist man, dass die Winkelsumme im Viereck 360° ist?', 'Eine Diagonale teilt das Viereck in zwei Dreiecke: 2 · 180° = 360°.',
                 ['Man misst vier Winkel und addiert.', 'Ein Viereck hat 4 rechte Winkel.', 'Jeder Winkel ist Nebenwinkel eines anderen: 4 · 90°.'],
                 'Mit der Diagonale entstehen zwei Dreiecke. Ihre Winkel bilden zusammen genau die vier Viereckswinkel.', 'Welche Hilfslinie zerlegt das Viereck?')
    if art == 'fuenfeck':
        return A(R, 'Wie viele Dreiecke braucht man, um die Winkelsumme 540° im Fünfeck zu begründen, wenn man alle Diagonalen von einer Ecke aus zieht?', '3',
                 ['5', '2', '4'], 'Von einer Ecke gehen 2 Diagonalen aus; sie zerlegen das Fünfeck in 3 Dreiecke: 3 · 180° = 540°.', 'Zeichne ein Fünfeck und zähle.')
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
def _schnitt_figur():
    """g und h schneiden sich in X; k schneidet g in S und h in T. Innenwinkel S 64°, T 81°, X 35°; bei S ist der Nebenwinkel 116° markiert."""
    f = dreieck(64, 81, [])
    S, T, X = f['punkte']['A'], f['punkte']['B'], f['punkte']['C']
    v = lambda p, q, t: [_r(p[0] + t * (q[0] - p[0])), _r(p[1] + t * (q[1] - p[1]))]
    pk = {'S': S, 'T': T, 'X': X, '_g1': v(X, S, 1.4), '_g2': v(S, X, 1.25), '_h1': v(X, T, 1.4), '_h2': v(T, X, 1.25), '_k1': v(T, S, 1.35), '_k2': v(S, T, 1.35)}
    return {'typ': 'figur', 'punkte': pk, 'linien': [['_g1', '_g2', 'g'], ['_h1', '_h2', 'h'], ['_k1', '_k2', 'k']],
            'winkel': [['S', '_g1', 'T', '116°'], ['T', 'X', 'S', '81°'], ['X', 'S', 'T', '?']]}


def _licht_figur():
    """Zwei parallele Spiegel (unten u, oben o). Der Strahl trifft u in P unter 35°, wird unter 35° zurückgeworfen und trifft o in Q."""
    P = (2.0, 0.0)
    Q = (P[0] + 3 / math.tan(math.radians(35)), 3.0)
    pk = {'P': [2, 0], 'Q': [_r(Q[0]), 3], '_E': _pol(P, 145, 2.4), '_u1': [-1.5, 0], '_u2': [_r(Q[0] + 2), 0], '_o1': [-1.5, 3], '_o2': [_r(Q[0] + 2), 3]}
    return {'typ': 'figur', 'punkte': pk, 'linien': [['_u1', '_u2', 'Spiegel 1'], ['_o1', '_o2', 'Spiegel 2'], ['_E', 'P'], ['P', 'Q']],
            'winkel': [['P', '_E', '_u1', '35°'], ['P', 'Q', '_u2', '35°'], ['Q', '_o1', 'P', '?']]}


def _kreis_figur():
    """Kreis um M, Durchmesser [AB], C auf dem Kreis mit dem Winkel 34° bei A."""
    C = _pol((0, 0), 68, 3)
    return {'typ': 'figur', 'punkte': {'A': [-3, 0], 'B': [3, 0], 'M': [0, 0], 'C': C}, 'kreise': [{'m': 'M', 'r': 3}],
            'linien': [['A', 'B'], ['A', 'C'], ['M', 'C']], 'winkel': [['A', 'B', 'C', '34°'], ['M', 'B', 'C', '?']]}


def fest(R):
    F = {}
    F['scheitel_neben'] = [
        Z('Drei Geraden schneiden sich in einem Punkt und bilden sechs Winkel. Zwei benachbarte Winkel sind 40° und 65° groß. Wie groß ist der größte der sechs Winkel?',
          75, '180 - 40 - 65', 'Drei benachbarte Winkel füllen eine Gerade: 180° − 40° − 65° = 75°. Die anderen drei sind Scheitelwinkel (40°, 65°, 75°). Größter: 75°.',
          'Drei nebeneinander liegende Winkel ergeben 180°. Die übrigen drei sind Scheitelwinkel.', art=P, grafik=drei_geraden(40, 65, {1: '40°', 2: '65°'})),
        A(R, 'Warum sind Scheitelwinkel immer gleich groß?', 'Beide ergänzen denselben Nebenwinkel zu 180°.',
          ['Weil sie gegenüberliegen und deshalb gleich aussehen.', 'Weil alle Winkel an einer Kreuzung gleich groß sind.', 'Weil man es messen kann.'],
          'α + β = 180° und γ + β = 180° (β ist Nebenwinkel von beiden). Also α = 180° − β = γ.', 'Suche einen Winkel, der neben beiden liegt.', art=P),
        Z('Ein Winkel an einer Kreuzung ist viermal so groß wie sein Nebenwinkel. Wie groß ist sein Scheitelwinkel?', 144, '4 * 180 / 5',
          'Nebenwinkel 1 Teil, großer Winkel 4 Teile: 5 Teile = 180°, ein Teil = 36°. Der große Winkel ist 4 · 36° = 144°; sein Scheitelwinkel ist ebenfalls 144°.',
          'Erst in Teile aufteilen, dann den Scheitelwinkel.', art=K)]
    F['stufen_wechsel'] = [
        Z('Eine Rampe steigt um 38° gegen die Waagrechte an. Der Handlauf ist parallel zur Rampe, die Pfosten stehen senkrecht. Wie groß ist der spitze Winkel zwischen Pfosten und Handlauf?',
          52, '90 - 38', 'Pfosten und Waagrechte bilden 90°. Der Handlauf ist um 38° geneigt (Stufenwinkel zur Rampe). Spitzer Winkel zum Pfosten: 90° − 38° = 52°.',
          'Der Pfosten steht senkrecht auf der Waagrechten.', art=P),
        Z('g ∥ h. Ein Dreieck hat die Ecke C auf g und die Ecken A und B auf h. Der Innenwinkel bei A ist 55°, bei B 70°. '
          'Welchen Winkel bildet [CB] rechts von C mit g (siehe Bild)?', 70, '70',
          '[CB] schneidet die Parallelen g und h. Der Winkel rechts bei C und der Innenwinkel bei B = 70° sind Wechselwinkel.', 'Welche Seite schneidet beide Parallelen?', art=P,
          grafik=dreieck_par(55, 70, [('A', '55°'), ('B', '70°'), ('Cr', '?')])),
        Z('g ∥ h. Ein Weg führt von A auf g zu einem Punkt P zwischen den Geraden und weiter zu B auf h. Bei A ist der Winkel 32°, bei B 51° (siehe Bild). Wie groß ist der Winkel bei P?',
          83, '32 + 51', 'Hilfslinie durch P parallel zu g: Sie teilt den Winkel bei P in die Wechselwinkel 32° und 51°. Zusammen 83°.',
          'Zeichne durch P eine dritte Parallele.', art=K, grafik=weg(32, 51, [('A', '32°'), ('B', '51°'), ('P', '?')]))]
    F['parallel_pruefen'] = [
        A(R, 'k schneidet g in S und h in T. Bei S ist der Winkel rechts oberhalb 68°, bei T der Winkel links unterhalb 62°. Welche Aussage ist richtig begründet?',
          'g und h sind nicht parallel, denn die Wechselwinkel wären sonst gleich groß.',
          ['g und h sind parallel, denn beide Winkel sind spitz.', 'g und h sind parallel, denn die Winkel liegen über Kreuz.', 'Das lässt sich ohne Längen nicht entscheiden.'],
          'Bei S links unterhalb ist der Scheitelwinkel 68°. Mit dem Winkel bei T rechts oberhalb (62°, Scheitelwinkel) bildet er ein Wechselwinkelpaar. 68° ≠ 62°: nicht parallel.',
          'Bringe beide Winkel mit Scheitelwinkeln in die Lage von Wechselwinkeln.', art=P, grafik=doppel(68, [('S', 'ro', '68°'), ('T', 'lu', '62°')], b=62)),
        Z('Die Geraden g und h schneiden sich weit rechts außerhalb des Bildes. Eine Gerade k schneidet g unter 75° und h unter 68° (beide Winkel rechts oberhalb). '
          'Unter welchem Winkel schneiden sich g und h?', 7, '75 - 68',
          'Zeichne durch T die Parallele zu g. Sie bildet mit k den Stufenwinkel 75°, h bildet mit k nur 68°. '
          'Also ist h gegen diese Parallele – und damit gegen g – um 75° − 68° = 7° geneigt.', 'Zeichne durch T eine Parallele zu g und vergleiche die Stufenwinkel.', art=P,
          grafik=doppel(75, [('S', 'ro', '75°'), ('T', 'ro', '68°')], b=68)),
        Z('Es gilt a ∥ b, b steht senkrecht auf c, und c ∥ d. Eine Gerade k schneidet a unter 35°. Unter welchem spitzen Winkel schneidet k die Gerade d?', 55, '90 - 35',
          'Aus a ∥ b und b ⟂ c folgt a ⟂ c, also a ⟂ d. Steht d senkrecht auf a, trifft k die Gerade d unter 90° − 35° = 55°.',
          'Was gilt für a und d? Zeichne eine Skizze.', art=K)]
    F['innenwinkelsumme'] = [
        A(R, 'Kann der größte Innenwinkel eines Dreiecks 58° groß sein?', 'Nein: Alle Winkel wären höchstens 58°, zusammen höchstens 174°.',
          ['Ja, zum Beispiel 58°, 58° und 64°.', 'Ja, jeder spitze Winkel ist möglich.', 'Nein, der größte Winkel muss stumpf sein.'],
          'Wenn 58° der größte Winkel ist, sind alle höchstens 58°: 3 · 58° = 174° < 180°. Der größte Winkel ist immer mindestens 60°.',
          'Was ist die größtmögliche Summe, wenn kein Winkel über 58° liegt?', art=P),
        A(R, 'Im Dreieck ABC teilt die Strecke [CM] den Winkel γ in δ und ε. Es gilt α = δ und β = ε. Welche Rechnung zeigt γ = 90°?',
          'α + β + γ = 180° und α + β = δ + ε = γ, also γ + γ = 180°.', ['α + β = 90°, weil zwei Winkel immer 90° ergeben.', 'δ + ε = 180°, also γ = 180°.', 'γ = δ · ε = 90°.'],
          'Ersetzt man α + β durch δ + ε, also durch γ, ergibt die Winkelsumme γ + γ = 180°, also γ = 90°.', 'Ersetze in der Winkelsumme α + β.', art=P),
        A(R, 'Ein Dreieck wird durch eine Strecke von einer Ecke zur Gegenseite in zwei Dreiecke geteilt. Jemand sagt: „Dann hat das große Dreieck 2 · 180° = 360°.“ Was ist falsch?',
          'Die zwei neuen Winkel an der Gegenseite (zusammen 180°) gehören nicht zum großen Dreieck: 360° − 180° = 180°.',
          ['Nichts, große Dreiecke haben mehr Winkelsumme.', 'Man muss 3 · 180° rechnen.', 'Die Teildreiecke haben je 90°.'],
          'Die beiden Teildreiecke haben zusammen 360°. Davon liegen 180° als Nebenwinkel auf der Gegenseite und zählen nicht zum großen Dreieck.',
          'Welche Winkel gehören zu den Teildreiecken, aber nicht zum großen Dreieck?', art=K)]
    F['aussenwinkel'] = [
        Z('Im Kreis um M ist [AB] ein Durchmesser, C liegt auf dem Kreis. Bei A bilden [AB] und [AC] den Winkel 34°. '
          'Im gleichschenkligen Dreieck sind die beiden Basiswinkel gleich groß. Wie groß ist der Winkel bei M zwischen [MB] und [MC]?', 68, '2 * 34',
          'MA = MC (Radien): Das Dreieck AMC ist gleichschenklig, also ist auch sein Winkel bei C 34°. Der gesuchte Winkel ist Außenwinkel des Dreiecks AMC bei M: 34° + 34° = 68°.',
          'Welches Dreieck ist gleichschenklig? Der gesuchte Winkel ist dort ein Außenwinkel.', art=P, grafik=_kreis_figur()),
        Z('Bei einem Dreieck ABC ist der Außenwinkel bei B 128° und der Außenwinkel bei C 117°. Wie groß ist α?', 65, '180 - (180 - 128) - (180 - 117)',
          'β = 180° − 128° = 52°, γ = 180° − 117° = 63°. α = 180° − 52° − 63° = 65°.', 'Bestimme erst β und γ.', art=P),
        A(R, 'Kann ein Dreieck drei spitze Außenwinkel haben?', 'Nein: Die Außenwinkel ergeben zusammen 360°, drei spitze aber weniger als 270°.',
          ['Ja, bei einem gleichseitigen Dreieck.', 'Ja, wenn alle Innenwinkel stumpf sind.', 'Nein, weil Außenwinkel immer 90° sind.'],
          'Jeder Außenwinkel ist 180° minus Innenwinkel; zusammen 3 · 180° − 180° = 360°. Drei Winkel unter 90° ergeben höchstens 270°.',
          'Was ergeben die drei Außenwinkel zusammen?', art=K)]
    F['vieleck'] = [
        Z('Auf einem Fußball treffen an jeder Ecke ein regelmäßiges Fünfeck und zwei regelmäßige Sechsecke zusammen. Wie groß ist die Summe der drei Winkel an einer Ecke?',
          348, '(5 - 2) * 180 / 5 + 2 * (6 - 2) * 180 / 6',
          'Fünfeck: 540° : 5 = 108°. Sechseck: 720° : 6 = 120°. Summe: 108° + 120° + 120° = 348°. (Weil es weniger als 360° sind, wölbt sich die Fläche zur Kugel.)',
          'Berechne zuerst einen Innenwinkel des Fünfecks und des Sechsecks.', art=P),
        A(R, 'Warum hat ein n-Eck die Winkelsumme (n − 2) · 180°?', 'Von einer Ecke aus zerlegen die Diagonalen das n-Eck in n − 2 Dreiecke.',
          ['Weil jedes n-Eck n Dreiecke enthält.', 'Weil man 2 Ecken nicht mitzählt.', 'Weil jeder Winkel 180° − 2° hat.'],
          'Von einer Ecke gibt es n − 3 Diagonalen; sie zerlegen das n-Eck in n − 2 Dreiecke mit je 180°.', 'Zeichne ein Sechseck und zähle die Dreiecke.', art=P),
        Z('Ein Vieleck hat die Winkelsumme 1440°. Wie viele Diagonalen gehen von einer Ecke aus?', 7, '1440 / 180 + 2 - 3',
          '1440° : 180° = 8 Dreiecke, also hat das Vieleck 8 + 2 = 10 Ecken. Von einer Ecke gehen 10 − 3 = 7 Diagonalen aus.', 'Bestimme zuerst die Zahl der Ecken.',
          einheit=None, art=K)]
    F['figuren'] = [
        Z('Die Geraden g und h schneiden sich in X. Eine Gerade k schneidet g in S und h in T. Bei S bildet k mit g auf der von X abgewandten Seite 116°, '
          'bei T ist der Winkel im Dreieck STX 81° (siehe Bild). Wie groß ist der Winkel bei X?', 35, '180 - (180 - 116) - 81',
          'Bei S ist der Winkel im Dreieck der Nebenwinkel von 116°: 64°. Winkelsumme im Dreieck STX: 180° − 64° − 81° = 35°.',
          'Bestimme zuerst den Dreieckswinkel bei S.', art=P, grafik=_schnitt_figur()),
        Z('Im Parallelogramm ABCD bildet die Diagonale [AC] mit [AB] den Winkel 35° und mit [AD] den Winkel 40°. Wie groß ist ∢ACB?', 40, '40',
          '[AD] ∥ [BC], und [AC] schneidet beide: ∢ACB ist Wechselwinkel zu ∢CAD = 40°.', 'Welche Seiten sind parallel zu [AD]?', art=P,
          grafik=parallelogramm(75, [('A_AB', '35°'), ('A_AD', '40°'), ('C_CB', '?')], p=4 * math.sin(math.radians(40)) / math.sin(math.radians(35)), q=4, diagonale=True)),
        Z('Ein Lichtstrahl trifft unter 35° auf Spiegel 1 und wird unter 35° zurückgeworfen. Er trifft dann auf Spiegel 2, der zu Spiegel 1 parallel ist (siehe Bild). '
          'Unter welchem Winkel trifft er dort auf?', 35, '35',
          'Der zurückgeworfene Strahl bildet mit Spiegel 1 den Winkel 35°. Am parallelen Spiegel 2 ist das ein Wechselwinkel: wieder 35°.',
          'Der Strahl schneidet beide Spiegel – die Spiegel sind parallel.', art=K, grafik=_licht_figur())]
    F['beweisen'] = [
        L('Beweis der Winkelsumme. Bringe die Kärtchen in die richtige Reihenfolge. Kärtchen 1: „Also liegen α, γ und β nebeneinander auf p: α + γ + β = 180°.“ '
          'Kärtchen 2: „Zeichne durch C die Parallele p zu [AB].“ Kärtchen 3: „Damit ist der Satz für jedes Dreieck bewiesen.“ '
          'Kärtchen 4: „Die Winkel links und rechts von C auf p sind so groß wie α und β (Wechselwinkel).“',
          '1. □; 2. □; 3. □; 4. □', [2, 4, 1, 3], ['2', '4', '1', '3'],
          'Zuerst die Hilfslinie p (2). Erst dann gibt es Winkel an p, die so groß sind wie α und β (4). Daraus folgt, dass α, γ und β auf p nebeneinander liegen (1). '
          'Zuletzt der Schluss (3).', 'Kärtchen 1 beginnt mit „Also“: Was muss vorher feststehen?', 'Trage die Nummern der Kärtchen ein.', art=P),
        A(R, 'Warum hat jedes Dreieck mindestens zwei spitze Winkel?', 'Zwei Winkel von je mindestens 90° ergäben schon 180°, für den dritten bliebe nichts.',
          ['Weil spitze Winkel häufiger sind.', 'Weil ein Dreieck drei Ecken hat.', 'Weil jedes Dreieck einen rechten Winkel hat.'],
          'Wären zwei Winkel 90° oder größer, wäre ihre Summe mindestens 180°. Dann bliebe für den dritten Winkel 0° oder weniger.', 'Nutze die Winkelsumme.', art=P),
        A(R, 'Welcher Satz wird im Beweis „Winkelsumme im Viereck = 360°“ benutzt, und wie oft?', 'die Winkelsumme im Dreieck, zweimal',
          ['der Satz über Nebenwinkel, viermal', 'der Satz über Scheitelwinkel, einmal', 'die Winkelsumme im Dreieck, viermal'],
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
    lz = [e['lernziel'] for e in ETAPPEN if e['lernziel'] not in VERTIEFUNG]
    return {
        **META, 'autor': 'Claude (Vierzehnte Runde; Sechzehnte Runde nachgebessert, Zweig winkelsaetze-2; Generator geometrie.winkelsaetze.py)',
        'inhalt': {
            'ziel': 'Winkel an Geradenkreuzungen und Doppelkreuzungen benennen und berechnen, Parallelität prüfen, die Innenwinkelsumme im Dreieck begründen, '
                    'Winkelsummen im Vieleck nutzen (Vertiefung: Außenwinkel) und Winkel in Figuren schrittweise mit Begründung bestimmen.',
            'merke': ['Scheitelwinkel sind gleich groß, Nebenwinkel ergeben 180°.', 'An Parallelen: Stufen- und Wechselwinkel sind gleich groß – und umgekehrt.',
                      'Dreieck: α + β + γ = 180°.', 'Vertiefung: Ein Außenwinkel ist so groß wie die beiden nicht anliegenden Innenwinkel zusammen.', 'n-Eck: Winkelsumme (n − 2) · 180°.',
                      'Jeder Schritt einer Begründung nennt seinen Winkelsatz.'],
            'abschnitte': [{'titel': 'Winkel an Kreuzungen', 'lernziele': ['scheitel_neben', 'stufen_wechsel', 'parallel_pruefen']},
                           {'titel': 'Winkelsummen', 'lernziele': ['innenwinkelsumme', 'aussenwinkel', 'vieleck']},
                           {'titel': 'Begründen in Figuren', 'lernziele': ['figuren', 'beweisen']}],
            'etappen': ETAPPEN,
            'teilfaehigkeiten': [{'k': e['lernziel'], 'text': e['titel'], 'lernziele': [e['lernziel']]} for e in ETAPPEN],
            'bewertung': {'lernziele_pflicht': lz, 'lernziele_vertiefung': list(VERTIEFUNG), 'testaufgaben_je_lernziel': 1, 'hilfen_im_test': False},
            'quellen': {'erklaerungen': 'Eigene Fassung (Claude).',
                        'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern, Gymnasium M7 2.2 „Winkelbetrachtungen an Figuren“ (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik).',
                        'pruefungsvorbilder': 'Typ und Niveau nach: Bayerischer Mathematik-Test 8 (ISB) 2019 B5/B7, 2021 A8, 2025 A8; Jahrgangsstufentest Realschule 8 (ISB) 2020 II, 2025 II Nr. 5/6; '
                                              'Vergleichsarbeit Jgst. 8 (Innenwinkel im n-Eck). Eigene Zahlen und Einkleidung.'},
        },
        'aufgaben': auf,
        'offen': ['Überschneidung: geometrie.konstruktion (gleicher Ort Addis Abeba) hat schon die Lernkarten „parallelen“, „winkelsumme“ und „vierecke“. '
                  'Vorschlag: dort als Wiederholung lassen oder in einer späteren Runde auf Konstruktion und Kongruenz kürzen – Entscheidung Sebastian (Liste in inhalte/postfach/winkelsaetze-2.md).',
                  'Die Lernkarte „aussenwinkel“ ist Vertiefung: Außenwinkel stehen nicht im LehrplanPLUS M7 2.2. Andere Etappen brauchen den Außenwinkelsatz nicht.',
                  'Winkel werden vom Kind nicht gemessen oder gezeichnet (kann die App nicht). Seitenlängen in Zeichnungen sind frei gewählt; '
                  'angeschriebene Winkel weichen höchstens 3° vom gezeichneten Winkel ab (beim Erzeugen geprüft).',
                  'Der Begriff „Nachbarwinkel“ (E-Winkel) steht nicht im LehrplanPLUS M7 2.2 und wird nicht eingeführt; solche Winkel heißen „Winkel an derselben Seite“ '
                  'und werden über Stufen- und Nebenwinkel berechnet.',
                  'Wechselwinkel: abgefragt werden nur die inneren Paare (über Kreuz zwischen den Parallelen). Die äußeren Paare werden nicht benannt, weil die Schulbücher sie '
                  'unterschiedlich nennen; die Lernkarte erwähnt das.'],
    }, zahl


def pruefe_zeichnungen(d):
    n = 0
    for e in d['inhalt']['etappen']:
        lz, bild = e['lernziel'], e.get('bild')
        n += pruefe_figur(bild, f'{lz} Kartenbild')
        stand = bild
        for i, s in enumerate(e['schritte']):
            if s.get('bild'):
                stand = s['bild'] if s['bild'].get('typ') not in (None, bild.get('typ')) else {**bild, **s['bild']}
                n += pruefe_figur(stand, f'{lz} Schritt {i + 1}')
        if e.get('fehler_bild'):
            fb = e['fehler_bild']
            n += pruefe_figur(fb if fb.get('typ') else {**bild, **fb}, f'{lz} fehler_bild')
    for i, a in enumerate(d['aufgaben']):
        n += pruefe_figur(a['f'].get('grafik'), f'Aufgabe {i} ({a["l"]})')
    return n


if __name__ == '__main__':
    d, zahl = datei()
    nz = pruefe_zeichnungen(d)
    for e in d['inhalt']['etappen']:
        if e['lernziel'] in ('figuren',):
            assert all(a['f'].get('grafik') for a in d['aufgaben'] if a['l'] == e['lernziel']), 'figuren: jede Bordkarte braucht eine Zeichnung'
    assert all(a['f'].get('grafik') for a in d['aufgaben'] if a['l'] == 'vieleck' and a['p'] == 'uebung' and a['s'] < 3), 'vieleck: Stufe 1/2 mit Zeichnung'
    assert all(a['f'].get('grafik') for a in d['aufgaben'] if a['l'] == 'vieleck' and a['p'] != 'uebung'), 'vieleck: Test/Korrektur/Sicherung (Stufe 2) mit Zeichnung'
    text = json.dumps(d, ensure_ascii=False)
    for verboten in ('Nachbarwinkel an', 'zwei Nachbarwinkel', '∠', '+ 0 ', 'Verschieden wie'):
        assert verboten not in text, verboten
    print(f'Zeichnungen geprüft: {nz}')
    ZIEL.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{ZIEL.name}: {len(d["inhalt"]["etappen"])} Lernkarten, {len(d["aufgaben"])} Aufgaben')
    for e in d['inhalt']['etappen']:
        l = e['lernziel']
        print(f'  {l:18} Prüfungsvorbild: {zahl[(l, P)]}  Knobel: {zahl[(l, K)]}')
