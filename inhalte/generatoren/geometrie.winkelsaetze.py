#!/usr/bin/env python3
"""Thema geometrie.winkelsaetze – Winkelsätze (Gymnasium Bayern, Klasse 7, LehrplanPLUS M7 2.2 „Winkelbetrachtungen an Figuren“).

Vierzehnte Runde (Zweig daten-klassen-2), nachgebessert in der Sechzehnten Runde (Zweig winkelsaetze-2) nach zwei Prüfberichten:
Außenwinkel ist Vertiefung (nicht im LehrplanPLUS M7 2.2); keine linearen Gleichungen (M7 3) und keine Basiswinkel (M7 5) in Pflicht-Etappen;
Zeichnungen maßstäblich (angeschriebene Winkel weichen höchstens 3° ab), „nicht parallel“ sichtbar gekippt. Baut auf geometrie.winkel (Klasse 5, „Mit Winkeln rechnen“) auf und wiederholt dessen Inhalte nicht:
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
    return f'{zahl(x)}°'


def zahl(x):
    """Wie zt, aber schon ab 1 000 mit Leerzeichen (einheitlich: 1 440°, 2 340°)."""
    t = zt(x)
    if isinstance(x, (int, Fr)) and Fr(x).denominator == 1 and abs(x) >= 1000 and ' ' not in t:
        t = f'{int(x):,}'.replace(',', ' ').replace('-', '−')
    return t


_WAHL = collections.Counter()


def wahl(R, schluessel, arten):
    """Abwechslung: wählt zufällig unter den bisher am seltensten gewählten Arten."""
    m = min(_WAHL[(schluessel, x)] for x in arten)
    art = R.choice([x for x in arten if _WAHL[(schluessel, x)] == m])
    _WAHL[(schluessel, art)] += 1
    return art


# ---------- Zeichnungen (maßstäblich: gezeichnete Winkel = angeschriebene Winkel) ----------
def _r(v):
    return round(v, 3)


def _pol(p, winkel, l):
    return (p[0] + l * math.cos(math.radians(winkel)), p[1] + l * math.sin(math.radians(winkel)))


def _strahlen(name, p, k_richtung, h_richtung=0.0, l=1.6):
    """Hilfspunkte um den Kreuzungspunkt: R/L entlang der Geraden (Richtung h_richtung), U/D entlang k."""
    pk = {name: [_r(p[0]), _r(p[1])]}
    for nm, w in (('R', h_richtung), ('L', h_richtung + 180), ('U', k_richtung), ('D', k_richtung + 180)):
        q = _pol(p, w, l)
        pk[f'_{name}{nm}'] = [_r(q[0]), _r(q[1])]
    return pk


_SCHENKEL = {'ro': ('R', 'U'), 'lo': ('U', 'L'), 'lu': ('L', 'D'), 'ru': ('D', 'R')}


def _w(name, pos, text):
    s1, s2 = _SCHENKEL[pos]
    return [name, f'_{name}{s1}', f'_{name}{s2}', text]


def doppel(ro_s, marken, ro_t=None):
    """g (oben, waagrecht, Punkt S) und h (unten, Punkt T), geschnitten von k.
    ro_s = Winkel rechts oberhalb bei S, ro_t = Winkel rechts oberhalb bei T (None: g ∥ h).
    Bei ro_t ≠ ro_s ist h um ro_s − ro_t gekippt; die Winkelbögen bei T liegen auf h."""
    assert 15 <= ro_s <= 165, ro_s
    phi = 0.0 if ro_t is None else ro_s - ro_t
    t = (2.0, 0.0)
    s = (t[0] + 3 * math.cos(math.radians(ro_s)) / math.sin(math.radians(ro_s)), 3.0)
    pk = {**_strahlen('S', s, ro_s), **_strahlen('T', t, ro_s, phi)}
    x0, x1 = min(s[0], t[0]) - 3, max(s[0], t[0]) + 3
    h1, h2 = _pol(t, phi + 180, t[0] - x0), _pol(t, phi, x1 - t[0])
    k1, k2 = _pol(t, ro_s + 180, 1.6), _pol(s, ro_s, 1.6)
    pk.update({'_g1': [_r(x0), 3], '_g2': [_r(x1), 3], '_h1': [_r(h1[0]), _r(h1[1])], '_h2': [_r(h2[0]), _r(h2[1])],
               '_k1': [_r(k1[0]), _r(k1[1])], '_k2': [_r(k2[0]), _r(k2[1])]})
    return {'typ': 'figur', 'punkte': pk, 'linien': [['_g1', '_g2', 'g'], ['_h1', '_h2', 'h'], ['_k1', '_k2', 'k']],
            'winkel': [_w(p, lage, txt) for p, lage, txt in marken]}


def einfach(ro, marken):
    """Eine Kreuzung zweier Geraden in S; ro = Winkel rechts oberhalb."""
    assert 15 <= ro <= 165, ro
    pk = _strahlen('S', (0, 0), ro, 0, 3)
    return {'typ': 'figur', 'punkte': pk, 'linien': [['_SL', '_SR'], ['_SD', '_SU']], 'winkel': [_w('S', lage, txt) for lage, txt in marken]}


def _dreieck_c(al, be, c=6.0):
    ga = 180 - al - be
    b = c * math.sin(math.radians(be)) / math.sin(math.radians(ga))
    return (b * math.cos(math.radians(al)), b * math.sin(math.radians(al)))


def dreieck(al, be, marken, aussen=None):
    """Dreieck ABC mit α = al bei A und β = be bei B. marken: Liste (Ecke, Text). aussen: (Ecke, Text) für einen Außenwinkel."""
    C = _dreieck_c(al, be)
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


def zwischen(al, be, marken):
    """Dreieck ABC zwischen Parallelen: A, B auf h (unten), C auf g (oben). α = al, β = be.
    marken: Liste (Name, Text) mit Namen 'A', 'B', 'C' (Innenwinkel), 'CL' (links bei C zwischen g und [CA]), 'CR' (rechts bei C zwischen [CB] und g)."""
    C = _dreieck_c(al, be)
    x0, x1 = min(0, C[0]) - 1.5, max(6, C[0]) + 1.5
    pk = {'A': [0, 0], 'B': [6, 0], 'C': [_r(C[0]), _r(C[1])], '_g1': [_r(x0), _r(C[1])], '_g2': [_r(x1), _r(C[1])], '_h1': [_r(x0), 0], '_h2': [_r(x1), 0],
          '_CL': [_r(C[0] - 1.5), _r(C[1])], '_CR': [_r(C[0] + 1.5), _r(C[1])]}
    win = {'A': ['A', 'B', 'C'], 'B': ['B', 'C', 'A'], 'C': ['C', 'A', 'B'], 'CL': ['C', '_CL', 'A'], 'CR': ['C', 'B', '_CR']}
    return {'typ': 'figur', 'punkte': pk, 'flaeche': ['A', 'B', 'C'], 'linien': [['_g1', '_g2', 'g'], ['_h1', '_h2', 'h'], ['A', 'B'], ['B', 'C'], ['C', 'A']],
            'winkel': [win[e] + [t] for e, t in marken]}


def parallelogramm(al, marken, a1=None, q=4.0):
    """Parallelogramm ABCD, α = al bei A. Mit a1 (Winkel zwischen [AC] und [AB]) wird die Diagonale [AC] gezeichnet; die Seitenlängen passen dazu.
    marken: Liste ([Scheitel, Schenkel1, Schenkel2], Text)."""
    p = q * math.sin(math.radians(al - a1)) / math.sin(math.radians(a1)) if a1 else 6.0
    D = _pol((0, 0), al, q)
    pk = {'A': [0, 0], 'B': [_r(p), 0], 'C': [_r(p + D[0]), _r(D[1])], 'D': [_r(D[0]), _r(D[1])]}
    lin = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A']] + ([['A', 'C', '', 'gestrichelt']] if a1 else [])
    return {'typ': 'figur', 'punkte': pk, 'flaeche': ['A', 'B', 'C', 'D'], 'linien': lin, 'winkel': [list(s) + [t] for s, t in marken]}


def trapez(al, be, marken):
    """Trapez ABCD mit AB ∥ CD, α = al, β = be."""
    hoehe = 3.0
    D = (hoehe / math.tan(math.radians(al)), hoehe)
    C = (7 - hoehe / math.tan(math.radians(be)), hoehe)
    assert C[0] - D[0] > 1, (al, be)
    pk = {'A': [0, 0], 'B': [7, 0], 'C': [_r(C[0]), _r(C[1])], 'D': [_r(D[0]), _r(D[1])]}
    win = {'A': ['A', 'B', 'D'], 'B': ['B', 'C', 'A'], 'C': ['C', 'D', 'B'], 'D': ['D', 'A', 'C']}
    return {'typ': 'figur', 'punkte': pk, 'flaeche': ['A', 'B', 'C', 'D'], 'linien': [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A']],
            'winkel': [win[e] + [t] for e, t in marken]}


def raute(al, marken):
    """Raute ABCD mit α = al bei A und Diagonale [AC]."""
    D = _pol((0, 0), al, 5)
    pk = {'A': [0, 0], 'B': [5, 0], 'C': [_r(5 + D[0]), _r(D[1])], 'D': [_r(D[0]), _r(D[1])]}
    return {'typ': 'figur', 'punkte': pk, 'flaeche': ['A', 'B', 'C', 'D'], 'linien': [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A'], ['A', 'C', '', 'gestrichelt']],
            'winkel': [list(s) + [t] for s, t in marken]}


def zickzack(a, b, marken):
    """g ∥ h; Weg von A (auf g) zu P zwischen den Geraden und weiter zu B (auf h). a: Winkel bei A zwischen g (rechts) und [AP], b bei B zwischen h (rechts) und [BP]."""
    A_ = (0.0, 4.0)
    P_ = _pol(A_, -a, 2 / math.sin(math.radians(a)))
    B_ = _pol(P_, 180 + b, 2 / math.sin(math.radians(b)))
    x0, x1 = min(A_[0], B_[0], P_[0]) - 1.5, max(A_[0], B_[0], P_[0]) + 2
    pk = {'A': [0, 4], 'P': [_r(P_[0]), _r(P_[1])], 'B': [_r(B_[0]), _r(B_[1])], '_g1': [_r(x0), 4], '_g2': [_r(x1), 4], '_h1': [_r(x0), 0], '_h2': [_r(x1), 0],
          '_AR': [_r(A_[0] + 1.5), 4], '_BR': [_r(B_[0] + 1.5), 0]}
    win = {'A': ['A', '_AR', 'P'], 'B': ['B', '_BR', 'P'], 'P': ['P', 'A', 'B']}
    return {'typ': 'figur', 'punkte': pk, 'linien': [['_g1', '_g2', 'g'], ['_h1', '_h2', 'h'], ['A', 'P'], ['P', 'B']], 'winkel': [win[e] + [t] for e, t in marken]}


def vieleck_fig(winkel, marken=None, diagonalen=False, namen='ABCDEFGHIJKL', seed=0):
    """Konvexes Vieleck mit den Innenwinkeln winkel (Ecke 0, 1, …). Seitenlängen so gewählt, dass es sich schließt.
    marken: Liste (Eckennummer, Text). diagonalen: alle Diagonalen von Ecke 0 gestrichelt."""
    n = len(winkel)
    assert sum(winkel) == (n - 2) * 180
    rr = random.Random(seed)
    for _ in range(5000):
        kurs, richt = 0.0, []
        for i in range(n):
            richt.append(kurs)
            kurs += 180 - winkel[(i + 1) % n]
        ls = [rr.uniform(3, 6) for _ in range(n - 2)]
        sx = sum(l * math.cos(math.radians(r)) for l, r in zip(ls, richt))
        sy = sum(l * math.sin(math.radians(r)) for l, r in zip(ls, richt))
        (a1, a2), (b1, b2) = [(math.cos(math.radians(richt[n - 2])), math.cos(math.radians(richt[n - 1]))),
                              (math.sin(math.radians(richt[n - 2])), math.sin(math.radians(richt[n - 1])))]
        det = a1 * b2 - a2 * b1
        if abs(det) < 1e-6: continue
        l1 = (-sx * b2 + a2 * sy) / det
        l2 = (-a1 * sy + b1 * sx) / det
        if 2.5 <= l1 <= 8 and 2.5 <= l2 <= 8: break
    else:
        raise SystemExit(f'Vieleck nicht zeichenbar: {winkel}')
    ls += [l1, l2]
    pk, p = {}, (0.0, 0.0)
    for i in range(n):
        pk[namen[i]] = [_r(p[0]), _r(p[1])]
        p = _pol(p, richt[i], ls[i])
    N = [namen[i] for i in range(n)]
    lin = [[N[i], N[(i + 1) % n]] for i in range(n)]
    if diagonalen: lin += [[N[0], N[i], '', 'gestrichelt'] for i in range(2, n - 1)]
    win = [[N[i], N[(i + 1) % n], N[i - 1], t] for i, t in (marken or [])]
    return {'typ': 'figur', 'punkte': pk, 'flaeche': N, 'linien': lin, 'winkel': win}


def regelmaessig(n, marke=None, diagonalen=False):
    """Regelmäßiges n-Eck; marke: Text am Winkel der Ecke A."""
    pk, N = {}, []
    for i in range(n):
        q = _pol((0, 0), -90 - 180 / n + 360 * i / n, 4)
        nm = 'ABCDEFGHIJKLMNOPQRSTUVWX'[i] if n <= 8 else ('A' if i == 0 else f'_E{i}')
        pk[nm] = [_r(q[0]), _r(q[1])]
        N.append(nm)
    lin = [[N[i], N[(i + 1) % n]] for i in range(n)]
    if diagonalen: lin += [[N[0], N[i], '', 'gestrichelt'] for i in range(2, n - 1)]
    fig = {'typ': 'figur', 'punkte': pk, 'flaeche': N, 'linien': lin, 'winkel': []}
    if marke: fig['winkel'].append([N[0], N[1], N[-1], marke])
    return fig


def kreis_aussen(a):
    """Kreis um M mit Durchmesser [AB] und C auf dem Kreis; ∢BAC = a, ∢BMC = 2a."""
    r = 3.0
    C = _pol((0, 0), 2 * a, r)
    return {'typ': 'figur', 'punkte': {'A': [-r, 0], 'B': [r, 0], 'M': [0, 0], 'C': [_r(C[0]), _r(C[1])]}, 'kreise': [{'m': 'M', 'r': r}],
            'linien': [['A', 'B'], ['A', 'C'], ['M', 'C']], 'winkel': [['A', 'B', 'C', g(a)], ['M', 'B', 'C', '?']]}


def drei_geraden(a, b):
    """k waagrecht; g durch S, h durch T schneiden sich in X oberhalb von k. a: Winkel bei S zwischen k (rechts) und g, b bei T zwischen h und k (links)."""
    X = _dreieck_c(a, b)
    S, T = (0.0, 0.0), (6.0, 0.0)
    gx, hx = _pol(S, a, math.hypot(*X) + 1.5), _pol(T, 180 - b, math.hypot(X[0] - 6, X[1]) + 1.5)
    pk = {'_S': [0, 0], '_T': [6, 0], '_X': [_r(X[0]), _r(X[1])], '_k1': [-1.5, 0], '_k2': [7.5, 0], '_ge': [_r(gx[0]), _r(gx[1])], '_he': [_r(hx[0]), _r(hx[1])]}
    return {'typ': 'figur', 'punkte': pk, 'linien': [['_k1', '_k2', 'k'], ['_S', '_ge', 'g'], ['_T', '_he', 'h']],
            'winkel': [['_S', '_T', '_X', g(a)], ['_T', '_X', '_S', g(b)], ['_X', '_S', '_T', '?']]}


def spiegel(a):
    """Zwei parallele Spiegel (unten u, oben o); Strahl trifft unten in P unter a und läuft zu Q oben."""
    P = (3.0, 0.0)
    E = _pol(P, 180 - a, 2.5)
    Q = _pol(P, a, 3 / math.sin(math.radians(a)))
    x0, x1 = min(E[0], P[0]) - 1, max(Q[0], P[0]) + 1.5
    pk = {'P': [3, 0], 'Q': [_r(Q[0]), 3], '_E': [_r(E[0]), _r(E[1])], '_u1': [_r(x0), 0], '_u2': [_r(x1), 0], '_o1': [_r(x0), 3], '_o2': [_r(x1), 3],
          '_PL': [1.5, 0], '_PR': [4.5, 0], '_QL': [_r(Q[0] - 1.5), 3]}
    return {'typ': 'figur', 'punkte': pk, 'linien': [['_u1', '_u2', 'Sp. 1'], ['_o1', '_o2', 'Sp. 2'], ['_E', 'P'], ['P', 'Q']],
            'winkel': [['P', '_PL', '_E', g(a)], ['P', 'Q', '_PR', g(a)], ['Q', '_QL', 'P', '?']]}


# ---------- Lernkarten (neues Muster, Vorgabe 16.11.) ----------
B_SN = einfach(65, [('ro', 'α = 65°'), ('lo', 'β'), ('lu', 'γ'), ('ru', 'δ')])
B_SW = doppel(60, [('S', 'ro', 'α = 60°'), ('T', 'ro', 'β'), ('T', 'lu', 'γ')])
B_PP = doppel(70, [('S', 'ro', '70°'), ('T', 'ro', '70°')])
B_D = dreieck(50, 70, [('A', 'α'), ('B', 'β'), ('C', 'γ')])
_CY = B_D['punkte']['C'][1]
B_DP = {**B_D, 'punkte': {**B_D['punkte'], '_p1': [-1.5, _CY], '_p2': [7.5, _CY]}, 'linien': B_D['linien'] + [['_p1', '_p2', 'p', 'gestrichelt']]}
_DPW = [['A', 'B', 'C', 'α'], ['B', 'C', 'A', 'β'], ['C', 'A', 'B', 'γ']]
B_AW = dreieck(50, 70, [('A', 'α = 50°'), ('B', 'β = 70°'), ('C', 'γ')], aussen=('C', 'γ\''))
B_VE = vieleck_fig([100, 110, 105, 120, 105], seed=5)
B_FI = zwischen(50, 60, [('A', '50°'), ('B', '60°'), ('C', 'γ')])
_M = [sum(p[0] for p in B_VE['punkte'].values()) / 5, sum(p[1] for p in B_VE['punkte'].values()) / 5]

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
     'fehler_bild': {'winkel': [_w('S', 'ro', 'α = 65°'), _w('S', 'lo', 'β = 115°, nicht 65°')]},
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
     'fehler_bild': doppel(60, [('S', 'ro', '60°'), ('T', 'ro', '75°')], ro_t=75),
     'regel': 'An Parallelen sind ⟦Stufenwinkel und Wechselwinkel gleich groß⟧.'},
    {'lernziel': 'parallel_pruefen', 'titel': 'Sind die Geraden parallel?',
     'einstieg': 'Eine Schreinerin prüft, ob zwei Regalbretter parallel sind. Sie misst, wie schräg eine Leiste beide Bretter trifft. Gleiche Stufenwinkel bedeuten: die Bretter sind ⟦parallel⟧.',
     'woerter': [['Umkehrung', 'der Satz rückwärts gelesen: aus gleichen Winkeln folgt parallel']],
     'bild': B_PP,
     'schritte': [{'text': 'k trifft g bei S unter 70°, h bei T auch unter 70°.'},
                  {'text': 'Die beiden Winkel liegen gleich: Es sind Stufenwinkel.'},
                  {'text': 'Gleich große Stufenwinkel: Nach der Umkehrung ist ⟦g ∥ h⟧.'},
                  {'text': 'Bei 70° und 80° wären die Geraden nicht parallel.',
                   'bild': doppel(70, [('S', 'ro', '70°'), ('T', 'ro', '80°')], ro_t=80)}],
     'fehler': 'Gleiche Scheitelwinkel an einer Kreuzung beweisen nichts. Vergleichen muss man Winkel an beiden Kreuzungen.',
     'fehler_bild': doppel(70, [('S', 'ro', '70°'), ('S', 'lu', '70°')]),
     'regel': 'Gleich große ⟦Stufen- oder Wechselwinkel⟧ zeigen: Die Geraden sind parallel.'},
    {'lernziel': 'innenwinkelsumme', 'titel': 'Winkelsumme im Dreieck begründen',
     'einstieg': 'Reiße die drei Ecken eines Papierdreiecks ab und lege sie nebeneinander. Sie bilden eine gerade Linie. Das gilt für jedes Dreieck: Die ⟦Winkelsumme⟧ ist 180°.',
     'woerter': [['Winkelsumme', 'alle Winkel innen in einer Figur zusammengezählt'], ['Hilfslinie', 'eine Linie, die man extra einzeichnet, um etwas zu zeigen']],
     'bild': B_D,
     'schritte': [{'text': 'Zeichne durch C eine Hilfslinie p parallel zu [AB].', 'bild': {**B_DP, 'winkel': _DPW}},
                  {'text': 'Links von C entsteht ein Winkel so groß wie α: Wechselwinkel.',
                   'bild': {**B_DP, 'winkel': _DPW + [['C', '_p1', 'A', 'α']]}},
                  {'text': 'Rechts von C entsteht ein Winkel so groß wie β: Wechselwinkel.',
                   'bild': {**B_DP, 'winkel': _DPW + [['C', '_p1', 'A', 'α'], ['C', 'B', '_p2', 'β']]}},
                  {'text': 'Auf p liegen α, γ und β nebeneinander: ⟦α + β + γ = 180°⟧.',
                   'bild': {**B_DP, 'linien': B_D['linien'] + [['_p1', '_p2', 'p: 180°', 'gestrichelt']],
                            'winkel': [['A', 'B', 'C', 'α'], ['B', 'C', 'A', 'β'], ['C', '_p1', 'A', 'α'], ['C', 'A', 'B', 'γ'], ['C', 'B', '_p2', 'β']]}}],
     'fehler': 'Messen an einem Dreieck ist kein Beweis. Erst die Begründung mit Wechselwinkeln zeigt: Es gilt für jedes Dreieck.',
     'regel': 'In jedem Dreieck gilt ⟦α + β + γ = 180°⟧. Der Beweis nutzt Wechselwinkel an einer Parallelen.'},
    {'lernziel': 'aussenwinkel', 'titel': 'Außenwinkel am Dreieck',
     'einstieg': 'Ein Läufer rennt um ein dreieckiges Feld. An jeder Ecke biegt er ab. Der Winkel, um den er abbiegt, ist ein ⟦Außenwinkel⟧ des Dreiecks.',
     'woerter': [['Außenwinkel', 'Nebenwinkel eines Innenwinkels; außen an der verlängerten Seite']],
     'bild': B_AW,
     'schritte': [{'text': 'Der Außenwinkel γ\' ist Nebenwinkel von γ: γ\' = 180° − γ.'},
                  {'text': 'Mit der Winkelsumme gilt γ = 180° − 50° − 70° = 60°.',
                   'bild': dreieck(50, 70, [('A', 'α = 50°'), ('B', 'β = 70°'), ('C', 'γ = 60°')], aussen=('C', 'γ\''))},
                  {'text': 'Also ist γ\' = 120° – das sind genau ⟦α + β⟧.',
                   'bild': dreieck(50, 70, [('A', 'α = 50°'), ('B', 'β = 70°'), ('C', 'γ = 60°')], aussen=('C', '120°'))}],
     'fehler': 'Der Außenwinkel bei C ist nicht γ. Er liegt außen und ergänzt γ zu 180°.',
     'fehler_bild': dreieck(50, 70, [('C', 'γ, nicht γ\'')], aussen=('C', 'γ\'')),
     'regel': 'Ein ⟦Außenwinkel⟧ ist so groß wie die zwei anderen Innenwinkel zusammen. Gemeint sind die beiden, die nicht an ihm liegen.'},
    {'lernziel': 'vieleck', 'titel': 'Winkelsumme im Vieleck',
     'einstieg': 'Ein Gärtner legt ein fünfeckiges Beet an. Er zieht von einer Ecke aus Schnüre zu den anderen Ecken. So zerfällt das Beet in Dreiecke – und die ⟦Winkelsumme⟧ lässt sich zählen.',
     'woerter': [['n-Eck', 'Vieleck mit n Ecken, z. B. Fünfeck: n = 5'], ['Diagonale', 'Strecke zwischen zwei Ecken, die nicht nebeneinander liegen'],
                 ['regelmäßig', 'alle Seiten gleich lang und alle Winkel gleich groß']],
     'bild': B_VE,
     'schritte': [{'text': 'Von A aus zeichnest du die Diagonalen nach C und D.',
                   'bild': {'linien': B_VE['linien'] + [['A', 'C', '', 'gestrichelt'], ['A', 'D', '', 'gestrichelt']]}},
                  {'text': 'Es entstehen 3 Dreiecke. Beim n-Eck sind es n − 2.'},
                  {'text': 'Jedes Dreieck hat 180°: ⟦3 · 180° = 540°⟧.'},
                  {'text': 'Im regelmäßigen Fünfeck ist jeder Winkel 540° : 5 = 108°.', 'bild': regelmaessig(5, '108°')}],
     'fehler': 'Nicht n · 180° rechnen. Von einem Punkt innen entstehen zwar 5 Dreiecke, aber 360° liegen in der Mitte und gehören nicht dazu.',
     'fehler_bild': {**B_VE, 'punkte': {**B_VE['punkte'], 'M': [_r(_M[0]), _r(_M[1])]},
                     'linien': B_VE['linien'] + [['M', e, '', 'gestrichelt'] for e in 'ABCDE']},
     'regel': 'Ein n-Eck hat die Winkelsumme ⟦(n − 2) · 180°⟧. Ein Viereck hat also 360°.'},
    {'lernziel': 'figuren', 'titel': 'Winkel in Figuren bestimmen',
     'einstieg': 'Zwischen zwei parallelen Regalbrettern steht eine dreieckige Stütze. Zwei ihrer Winkel sind bekannt. Bei jedem Schritt hilft dir ein ⟦Winkelsatz⟧.',
     'woerter': [['Winkelsatz', 'bewiesene Regel über Winkel, z. B. „Nebenwinkel ergeben 180°“'],
                 ['∢CAB', 'der Winkel bei A zwischen [AC] und [AB]; der mittlere Buchstabe ist der Scheitel']],
     'bild': B_FI,
     'schritte': [{'text': 'g ∥ h. Im Dreieck ist ∢CAB = 50° und ∢ABC = 60°.'},
                  {'text': 'Winkelsumme im Dreieck: ⟦∢BCA = 180° − 50° − 60° = 70°⟧.',
                   'bild': {'winkel': [['A', 'B', 'C', '50°'], ['B', 'C', 'A', '60°'], ['C', 'A', 'B', '70°']]}},
                  {'text': 'Links bei C bilden g und [CA] 50°: Wechselwinkel zu ∢CAB.',
                   'bild': {'winkel': [['A', 'B', 'C', '50°'], ['B', 'C', 'A', '60°'], ['C', 'A', 'B', '70°'], ['C', '_CL', 'A', '50°']]}},
                  {'text': 'Rechts bei C bilden [CB] und g 60°: Wechselwinkel zu ∢ABC.',
                   'bild': {'winkel': [['A', 'B', 'C', '50°'], ['B', 'C', 'A', '60°'], ['C', 'A', 'B', '70°'], ['C', '_CL', 'A', '50°'], ['C', 'B', '_CR', '60°']]}}],
     'probe': '50° + 70° + 60° = 180°: Die drei Winkel an g bilden eine Gerade ✓',
     'fehler': 'Nicht nach Augenmaß schätzen. Jeder Wert braucht einen Grund: Nebenwinkel, Scheitelwinkel, Stufen-, Wechselwinkel oder Winkelsumme.',
     'regel': 'Gehe von bekannten Winkeln aus. Nenne bei jedem Schritt den ⟦Winkelsatz⟧, den du nutzt.'},
    {'lernziel': 'beweisen', 'titel': 'Begründen mit Winkelsätzen',
     'einstieg': 'In der Mathematik baut man Sätze aufeinander auf wie Bausteine. Ganz unten liegt ein Satz, den man annimmt. Er heißt ⟦Fundamentalsatz⟧.',
     'woerter': [['Fundamentalsatz', 'Grundsatz, der nicht bewiesen, sondern vorausgesetzt wird'], ['abgeleiteter Satz', 'Satz, der mit anderen Sätzen bewiesen wird']],
     'bild': B_DP,
     'schritte': [{'text': 'Fundamentalsatz: Wechselwinkel an Parallelen sind gleich groß.'},
                  {'text': 'Daraus folgt die Winkelsumme im Dreieck: ein abgeleiteter Satz.'},
                  {'text': 'Aus der Winkelsumme im Dreieck folgt die ⟦Winkelsumme im Viereck⟧.'},
                  {'text': 'Jeder Schritt nennt den Satz, auf den er sich stützt.'}],
     'fehler': 'Einen Satz mit sich selbst begründen ist ein Zirkelschluss. Der Beweis darf nur Sätze benutzen, die vorher feststehen.',
     'regel': 'Ein Beweis ist eine Kette. Jedes Glied stützt sich auf einen ⟦vorher bekannten Satz⟧.'},
]


# ---------- Aufgaben-Generatoren (zufällig, je Stufe) ----------
def _paar(R):
    return R.choice([x for x in range(25, 156) if x != 90])


def gen_scheitel_neben(R, st):
    a = _paar(R)
    if st == 1:
        art = wahl(R, 'sn1', ['scheitel', 'neben'])
        if art == 'scheitel':
            return Z(f'Zwei Geraden schneiden sich. Ein Winkel ist {g(a)} groß. Wie groß ist sein Scheitelwinkel?', a, f'{a}',
                     f'Scheitelwinkel sind gleich groß: {g(a)}.', 'Der Scheitelwinkel liegt gegenüber.', grafik=einfach(a, [('ro', g(a)), ('lu', '?')]))
        return Z(f'Zwei Geraden schneiden sich. Ein Winkel ist {g(a)} groß. Wie groß ist sein Nebenwinkel?', 180 - a, f'180 - {a}',
                 f'Nebenwinkel ergänzen sich zu 180°: 180° − {g(a)} = {g(180 - a)}.', 'Nebenwinkel liegen an einer Geraden nebeneinander.',
                 grafik=einfach(a, [('ro', g(a)), ('lo', '?')]))
    if st == 2:
        art = wahl(R, 'sn2', ['lage', 'unterschied', 'benennen', 'drei'])
        if art == 'lage':
            ziel = R.choice(['lo', 'lu', 'ru'])
            w = {'lo': 180 - a, 'lu': a, 'ru': 180 - a}[ziel]
            return Z(f'Zwei Geraden schneiden sich. Der Winkel rechts oberhalb ist {g(a)} groß. Wie groß ist der Winkel {POS_TEXT[ziel]}?', w,
                     f'{w}', (f'Scheitelwinkel sind gleich groß: {g(w)}.' if ziel == 'lu' else f'Nebenwinkel: 180° − {g(a)} = {g(w)}.'),
                     'Liegt der Winkel gegenüber oder daneben?', grafik=einfach(a, [('ro', g(a)), (ziel, '?')]))
        if art == 'unterschied':
            d = R.choice(range(10, 101, 10))
            big = (180 + d) // 2
            return Z(f'Ein Winkel ist um {g(d)} größer als sein Nebenwinkel. Wie groß ist der größere Winkel?', big, f'(180 + {d}) / 2',
                     f'Nimm den Unterschied weg: 180° − {g(d)} = {g(180 - d)} bleiben für zwei gleich große Teile, also je {g((180 - d) // 2)}. '
                     f'Der größere Winkel: {g((180 - d) // 2)} + {g(d)} = {g(big)}.', 'Beide zusammen ergeben 180°. Nimm zuerst den Unterschied weg.')
        if art == 'drei':
            x, y = R.randint(20, 80), R.randint(20, 80)
            if x + y >= 160: return gen_scheitel_neben(R, st)
            return Z(f'Drei Geraden schneiden sich in einem Punkt. Drei der sechs Winkel liegen nebeneinander an einer Geraden: {g(x)}, {g(y)} und ein dritter. Wie groß ist der dritte?',
                     180 - x - y, f'180 - {x} - {y}', f'Winkel nebeneinander an einer Geraden ergeben 180°: 180° − {g(x)} − {g(y)} = {g(180 - x - y)}.', 'Winkel an einer Geraden ergeben 180°.')
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
    art = wahl(R, 'sn3', ['verh', 'summe', 'drei_vier', 'verh_trick'])
    if art in ('verh', 'verh_trick'):
        p, q = R.choice([(1, 2), (2, 3), (1, 3), (1, 4), (4, 5), (2, 7), (3, 7), (1, 5), (7, 8), (5, 7), (1, 8), (3, 5), (5, 13)])
        if 180 % (p + q): return gen_scheitel_neben(R, st)
        k = 180 // (p + q)
        if art == 'verh':
            return Z(f'Zwei Nebenwinkel verhalten sich wie {p} : {q}. Wie groß ist der kleinere?', p * k, f'180 / ({p} + {q}) * {p}',
                     f'{p} + {q} = {p + q} Teile = 180°, ein Teil = {g(k)}. Kleinerer Winkel: {p} · {g(k)} = {g(p * k)}.', 'Wie viele Teile sind es zusammen?')
        return Z(f'Zwei Geraden schneiden sich. Ein Winkel und der Nebenwinkel seines Scheitelwinkels verhalten sich wie {p} : {q}. Wie groß ist der größere der beiden?', q * k,
                 f'180 / ({p} + {q}) * {q}', f'Der Nebenwinkel des Scheitelwinkels ist auch ein Nebenwinkel des Winkels selbst. Also: {p + q} Teile = 180°, '
                 f'ein Teil = {g(k)}, größerer Winkel {q} · {g(k)} = {g(q * k)}.', 'Zeichne die Kreuzung. Wo liegt der Nebenwinkel des Scheitelwinkels?')
    if art == 'drei_vier':
        x = _paar(R)
        return Z(f'Zwei Geraden schneiden sich. Drei der vier Winkel ergeben zusammen {g(360 - x)}. Wie groß ist der vierte Winkel, und wie groß ist dann sein Nebenwinkel? Gib den Nebenwinkel an.',
                 180 - x, f'180 - (360 - {360 - x})', f'Alle vier Winkel ergeben 360°: Der vierte ist 360° − {g(360 - x)} = {g(x)}. Sein Nebenwinkel: 180° − {g(x)} = {g(180 - x)}.',
                 'Alle vier Winkel an einer Kreuzung ergeben zusammen 360°.')
    s = R.choice(range(60, 300, 4))
    if s > 180: s = 360 - s
    if s % 2: return gen_scheitel_neben(R, st)
    return Z(f'Zwei Geraden schneiden sich. Zwei Scheitelwinkel ergeben zusammen {g(s)}. Wie groß ist einer der beiden anderen Winkel?', 180 - s // 2,
             f'180 - {s} / 2', f'Ein Scheitelwinkel: {g(s)} : 2 = {g(s // 2)}. Sein Nebenwinkel: 180° − {g(s // 2)} = {g(180 - s // 2)}.',
             'Scheitelwinkel sind gleich groß. Die anderen beiden sind ihre Nebenwinkel.')


# Paare an zwei Kreuzungen (Lage bei S, Lage bei T): nur eindeutige Fälle. „weder noch“ nur für Paare, die an Parallelen nie gleich groß sind.
NAMEN_PAARE = [('ro', 'ro', 'Stufenwinkel'), ('lo', 'lo', 'Stufenwinkel'), ('lu', 'lu', 'Stufenwinkel'), ('ru', 'ru', 'Stufenwinkel'),
               ('lu', 'ro', 'Wechselwinkel'), ('ru', 'lo', 'Wechselwinkel'),
               ('ro', 'lo', 'weder noch'), ('lo', 'ro', 'weder noch'), ('lu', 'ru', 'weder noch'), ('ru', 'lu', 'weder noch')]


def gen_stufen_wechsel(R, st):
    a = _paar(R)
    if st == 1:
        if wahl(R, 'sw1', ['stufe', 'wechsel']) == 'stufe':
            pos = R.choice(list(POS_TEXT))
            return Z(f'g ∥ h. Bei S ist der Winkel {POS_TEXT[pos]} {g(a)} groß. Wie groß ist der Winkel bei T in derselben Lage?', a, f'{a}',
                     f'Stufenwinkel an Parallelen sind gleich groß: {g(a)}.', 'Gleiche Lage an beiden Kreuzungen: Stufenwinkel.',
                     grafik=doppel(a if pos in ('ro', 'lu') else 180 - a, [('S', pos, g(a)), ('T', pos, '?')]))
        return Z(f'g ∥ h. Bei S ist der Winkel links unterhalb {g(a)} groß. Wie groß ist sein Wechselwinkel bei T (rechts oberhalb)?', a, f'{a}',
                 f'Wechselwinkel an Parallelen sind gleich groß: {g(a)}.', 'Wechselwinkel liegen über Kreuz zwischen den Parallelen.',
                 grafik=doppel(a, [('S', 'lu', g(a)), ('T', 'ro', '?')]))
    if st == 2:
        art = wahl(R, 'sw2', ['neben', 'name', 'wechsel_neben'])
        gross = {'ro': 1, 'lu': 1, 'lo': 0, 'ru': 0}
        if art == 'neben':
            p1, p2 = R.choice([('ro', 'lo'), ('ro', 'ru'), ('lu', 'lo'), ('lo', 'ro'), ('ru', 'lu')])
            w2 = a if gross[p1] == gross[p2] else 180 - a
            zeich = a if gross[p1] else 180 - a
            return Z(f'g ∥ h. Bei S ist der Winkel {POS_TEXT[p1]} {g(a)} groß. Wie groß ist der Winkel bei T {POS_TEXT[p2]}?', w2, f'{w2}',
                     f'Stufenwinkel: Bei T {POS_TEXT[p1]} ist auch {g(a)}. Der gesuchte Winkel ist dessen Nebenwinkel: 180° − {g(a)} = {g(w2)}.',
                     'Übertrage den Winkel zuerst mit dem Stufenwinkel nach T.', grafik=doppel(zeich, [('S', p1, g(a)), ('T', p2, '?')]))
        if art == 'wechsel_neben':
            return Z(f'g ∥ h. Bei S ist der Winkel links unterhalb {g(a)} groß. Wie groß ist der Winkel bei T rechts unterhalb?', 180 - a, f'180 - {a}',
                     f'Wechselwinkel: Bei T rechts oberhalb ist auch {g(a)}. Rechts unterhalb liegt sein Nebenwinkel: 180° − {g(a)} = {g(180 - a)}.',
                     'Erst mit dem Wechselwinkel nach T, dann der Nebenwinkel.', grafik=doppel(a, [('S', 'lu', g(a)), ('T', 'ru', '?')]))
        p1, p2, name = R.choice(NAMEN_PAARE)
        w = 'Gleiche Lage an beiden Kreuzungen: Stufenwinkel. Über Kreuz zwischen den Parallelen: Wechselwinkel. Scheitelwinkel liegen an derselben Kreuzung.'
        if name == 'weder noch':
            w += ' Hier liegt ein Winkel außerhalb, der andere zwischen den Parallelen, auf verschiedenen Seiten von k: Sie ergänzen sich zu 180° – kein Paar mit gleichen Winkeln.'
        return A(R, f'g ∥ h. Wie heißen der Winkel bei S {POS_TEXT[p1]} und der Winkel bei T {POS_TEXT[p2]}?', name,
                 [x for x in ['Stufenwinkel', 'Wechselwinkel', 'Scheitelwinkel', 'weder noch'] if x != name], w,
                 'Liegen beide in gleicher Lage oder über Kreuz zwischen g und h?', grafik=doppel(60, [('S', p1, '1'), ('T', p2, '2')]))
    art = wahl(R, 'sw3', ['verh', 'kette'])
    if art == 'verh':
        k = R.choice([2, 3, 4, 5, 8])
        klein = 180 // (k + 1)
        ziel = R.choice(['ru', 'lu'])
        w = klein if ziel == 'ru' else k * klein
        return Z(f'g ∥ h. Bei S ist der Winkel rechts oberhalb {k}-mal so groß wie der Winkel links oberhalb. Wie groß ist der Winkel bei T {POS_TEXT[ziel]}?', w,
                 f'180 / ({k} + 1) * {k if ziel == "lu" else 1}',
                 f'Die beiden Winkel bei S sind Nebenwinkel: {k + 1} gleiche Teile = 180°, ein Teil = {g(klein)}. Rechts oberhalb also {g(k * klein)}, links oberhalb {g(klein)}. '
                 f'Bei T {POS_TEXT[ziel]} liegt der Stufenwinkel zu S {POS_TEXT[ziel]}. Dieser ist Scheitelwinkel von {"links oberhalb" if ziel == "ru" else "rechts oberhalb"}: {g(w)}.',
                 'Teile 180° im Verhältnis auf. Dann mit Stufen- und Scheitel- oder Nebenwinkeln nach T.', grafik=doppel(k * klein, [('S', 'ro', f'{k}-mal'), ('S', 'lo', '1-mal'), ('T', ziel, '?')]))
    if art == 'kette':
        b = R.randint(25, 85)
        return Z(f'g ∥ h. Bei S ist der Winkel links oberhalb {g(180 - b)} groß. Wie groß ist der Winkel bei T rechts oberhalb?', b, f'180 - {180 - b}',
                 f'Bei S rechts oberhalb: Nebenwinkel 180° − {g(180 - b)} = {g(b)}. Stufenwinkel bei T: {g(b)}.', 'Erst Nebenwinkel bei S, dann Stufenwinkel.',
                 grafik=doppel(b, [('S', 'lo', g(180 - b)), ('T', 'ro', '?')]))


def gen_parallel_pruefen(R, st):
    a = _paar(R)
    if st == 1:
        gleich = wahl(R, 'pp1j', [True, False])
        b = a if gleich else a + R.choice([-12, -9, -6, 6, 9, 12])
        typ = wahl(R, 'pp1', ['Stufenwinkel', 'Wechselwinkel'])
        return A(R, f'Eine Gerade k schneidet g und h. Zwei {typ} sind {g(a)} und {g(b)} groß. Sind g und h parallel?',
                 'Ja' if gleich else 'Nein', ['Ja' if not gleich else 'Nein', 'Das kann man nicht entscheiden'],
                 f'{typ} {"gleich groß: parallel" if gleich else "verschieden groß: nicht parallel"} ({g(a)} und {g(b)}).', f'Sind die {typ} gleich groß?')
    if st == 2:
        art = wahl(R, 'pp2', ['neben', 'dreh', 'wechsel'])
        if art == 'neben':
            ok = wahl(R, 'pp2j', [True, False])
            ro_t = a if ok else a + R.choice([-10, -8, 8, 10])
            b = 180 - ro_t
            return A(R, f'k schneidet g in S und h in T. Bei S ist der Winkel rechts oberhalb {g(a)}, bei T der Winkel rechts unterhalb {g(b)}. Sind g und h parallel?',
                     'Ja' if ok else 'Nein', ['Ja' if not ok else 'Nein', 'Nur wenn beide Winkel gleich groß sind'],
                     f'Bei T rechts oberhalb ist der Nebenwinkel 180° − {g(b)} = {g(ro_t)}. {"Gleich wie" if ok else "Anders als"} bei S ({g(a)}): '
                     f'{"parallel" if ok else "nicht parallel"}.', 'Bilde bei T den Nebenwinkel und vergleiche dann Stufenwinkel.',
                     grafik=doppel(a, [('S', 'ro', g(a)), ('T', 'ru', g(b))], ro_t=None if ok else ro_t))
        if art == 'wechsel':
            ok = wahl(R, 'pp2j', [True, False])
            ro_t = a if ok else a + R.choice([-10, -8, 8, 10])
            return A(R, f'k schneidet g in S und h in T. Bei S ist der Winkel links unterhalb {g(a)}, bei T der Winkel rechts oberhalb {g(ro_t)}. Sind g und h parallel?',
                     'Ja' if ok else 'Nein', ['Ja' if not ok else 'Nein', 'Das kann man ohne Messen der Längen nicht sagen'],
                     f'Die beiden Winkel sind Wechselwinkel. {"Gleich groß: Nach der Umkehrung ist g ∥ h." if ok else f"{g(a)} ≠ {g(ro_t)}: nicht parallel."}',
                     'Liegen die Winkel über Kreuz zwischen g und h?', grafik=doppel(a, [('S', 'lu', g(a)), ('T', 'ro', g(ro_t))], ro_t=None if ok else ro_t))
        d = R.randint(1, 9)
        return Z(f'k schneidet g unter {g(a)} und h unter {g(a + d)} (beide Winkel rechts oberhalb). Um wie viel Grad muss man h drehen, damit h ∥ g wird?', d,
                 f'{a + d} - {a}', f'Die Stufenwinkel müssen gleich werden: {g(a + d)} − {g(a)} = {g(d)}.', 'Welcher Unterschied muss verschwinden?')
    art = wahl(R, 'pp3', ['drei', 'welche'])
    if art == 'drei':
        x = _paar(R)
        return Z(f'Es gilt a ∥ b und b ∥ c. Eine Gerade k schneidet a, b und c. Bei a ist der Winkel rechts oberhalb {g(x)}. Wie groß ist bei c der Winkel links oberhalb?', 180 - x,
                 f'180 - {x}', f'a ∥ b und b ∥ c, also a ∥ c. Stufenwinkel: Bei c rechts oberhalb ist auch {g(x)}. Links oberhalb liegt der Nebenwinkel: 180° − {g(x)} = {g(180 - x)}.',
                 'Was folgt aus a ∥ b und b ∥ c? Dann Stufen- und Nebenwinkel.')
    # Drei Geraden a, b, c, von k geschnitten; genau zwei davon sind parallel. Ein Winkel ist als Nebenwinkel angegeben.
    x = _paar(R)
    y = x + R.choice([-11, -7, 7, 11])
    namen = ['a', 'b', 'c']
    R.shuffle(namen)
    p1, p2, anders = namen
    lagen = {p1: f'rechts oberhalb {g(x)}', p2: f'links oberhalb {g(180 - x)}', anders: f'rechts oberhalb {g(y)}'}
    text = ', '.join(f'bei {n} {lagen[n]}' for n in 'abc')
    paar = ' und '.join(sorted([p1, p2]))
    falsch = [' und '.join(sorted(z)) for z in ([p1, anders], [p2, anders])] + ['keine zwei']
    return A(R, f'Eine Gerade k schneidet die Geraden a, b und c. Die Winkel sind: {text}. Welche zwei Geraden sind parallel?', f'{paar}', falsch,
             f'Links oberhalb {g(180 - x)} heißt: rechts oberhalb liegt der Nebenwinkel {g(x)}. Gleiche Stufenwinkel ({g(x)}) haben nur {paar}. Bei {anders} sind es {g(y)}.',
             'Rechne alle Winkel auf dieselbe Lage um und vergleiche dann die Stufenwinkel.')


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
        art = wahl(R, 'iw2', ['doppelt', 'beweis', 'gleich', 'rechtw', 'moeglich'])
        if art == 'doppelt':
            k = R.choice([2, 3, 4])
            gg = R.choice(range(30, 120, 2))
            if (180 - gg) % (k + 1): return gen_innenwinkelsumme(R, st)
            x = (180 - gg) // (k + 1)
            return Z(f'In einem Dreieck ist β {k}-mal so groß wie α, und γ = {g(gg)}. Wie groß ist α?', x, f'(180 - {gg}) / ({k} + 1)',
                     f'Für α und β bleiben 180° − {g(gg)} = {g(180 - gg)}. α ist 1 Teil, β sind {k} Teile: {k + 1} Teile = {g(180 - gg)}, also α = {g(x)}.',
                     'Für α und β zusammen bleibt 180° − γ. Teile das passend auf.')
        if art == 'gleich':
            y = R.choice(range(20, 140, 2))
            return Z(f'In einem Dreieck ist γ = {g(y)}, und α und β sind gleich groß. Wie groß ist α?', (180 - y) // 2, f'(180 - {y}) / 2',
                     f'Für α und β bleiben 180° − {g(y)} = {g(180 - y)}, je die Hälfte: {g((180 - y) // 2)}.', 'Was bleibt für α und β zusammen?')
        if art == 'rechtw':
            x = R.randint(15, 75)
            return Z(f'Ein Dreieck hat einen rechten Winkel und einen Winkel von {g(x)}. Wie groß ist der dritte Winkel?', 90 - x, f'180 - 90 - {x}',
                     f'180° − 90° − {g(x)} = {g(90 - x)}.', 'Ein rechter Winkel hat 90°.', grafik=dreieck(90, x, [('A', '90°'), ('B', g(x)), ('C', '?')]))
        if art == 'moeglich':
            x, y = R.randint(50, 110), R.randint(50, 110)
            ok = x + y < 180
            return A(R, f'Gibt es ein Dreieck mit den Winkeln α = {g(x)} und β = {g(y)}?', f'Ja, dann ist γ = {g(180 - x - y)}.' if ok else f'Nein, schon α + β = {g(x + y)}.',
                     ([f'Nein, schon α + β = {g(x + y)}.'] if ok else [f'Ja, dann ist γ = {g(abs(180 - x - y))}.']) + ['Das hängt von der Länge der Seiten ab.', 'Ja, jedes Paar von Winkeln geht.'],
                     f'α + β = {g(x + y)}. {"Für γ bleiben " + g(180 - x - y) + "." if ok else "Für γ bleibt nichts – das Dreieck gibt es nicht."}',
                     'Für γ muss etwas übrig bleiben.')
        v = R.choice(['links', 'rechts', 'mitte', 'gerade', 'hilfslinie'])
        if v in ('links', 'rechts'):
            return A(R, f'Beweis der Winkelsumme: Durch C ist die Parallele p zu [AB] gezeichnet. Warum ist der Winkel {v} von C zwischen p und der Dreiecksseite so groß wie {"α" if v == "links" else "β"}?',
                     'Er ist Wechselwinkel an den Parallelen p und AB.', ['Er ist Scheitelwinkel.', 'Er ist Nebenwinkel.', 'Man sieht es in der Zeichnung.'],
                     f'p ∥ AB. Die Seite [{"AC" if v == "links" else "BC"}] schneidet beide Parallelen; der Winkel bei C und {"α" if v == "links" else "β"} liegen über Kreuz: Wechselwinkel.',
                     'Welche Winkel an Parallelen liegen über Kreuz?', grafik={**B_DP, 'winkel': _DPW + ([['C', '_p1', 'A', '?']] if v == 'links' else [['C', 'B', '_p2', '?']])})
        if v == 'mitte':
            return A(R, 'Beweis der Winkelsumme: Auf der Parallelen p durch C liegen drei Winkel nebeneinander. Welcher liegt in der Mitte?', 'γ',
                     ['α', 'β', 'ein rechter Winkel'], 'Links liegt der Wechselwinkel zu α, rechts der zu β, dazwischen der Dreieckswinkel γ.', 'Welcher Winkel gehört direkt zum Dreieck bei C?',
                     grafik={**B_DP, 'winkel': [['A', 'B', 'C', 'α'], ['B', 'C', 'A', 'β']]})
        if v == 'gerade':
            return A(R, 'Beweis der Winkelsumme: Warum ergeben die drei Winkel an C auf der Parallelen p zusammen 180°?', 'Sie liegen nebeneinander auf einer Geraden.',
                     ['Weil jedes Dreieck 180° hat.', 'Weil es Scheitelwinkel sind.', 'Weil p parallel zu [AB] ist.'],
                     'Winkel, die auf einer Geraden nebeneinander liegen, bilden einen gestreckten Winkel: 180°. Die Winkelsumme darf man hier nicht benutzen – sie soll ja erst bewiesen werden.',
                     'Was ist ein gestreckter Winkel?', grafik={**B_DP, 'winkel': _DPW + [['C', '_p1', 'A', 'α'], ['C', 'B', '_p2', 'β']]})
        return A(R, 'Welche Hilfslinie braucht man für den Beweis der Winkelsumme im Dreieck ABC?', 'die Parallele zu [AB] durch C',
                 ['die Mittelsenkrechte von [AB]', 'die Winkelhalbierende von γ', 'eine Senkrechte zu [AB] durch A'],
                 'Erst mit der Parallelen entstehen Wechselwinkel, die α und β nach C bringen.', 'Welche Winkelsätze brauchen Parallelen?', grafik=B_D)
    art = wahl(R, 'iw3', ['rechtwinklig', 'verh', 'mehr'])
    if art == 'rechtwinklig':
        d = R.choice(range(4, 60, 2))
        gr = (90 + d) // 2
        return Z(f'Ein Dreieck ist rechtwinklig. Ein spitzer Winkel ist um {g(d)} größer als der andere. Wie groß ist der größere spitze Winkel?', gr,
                 f'(90 + {d}) / 2', f'Die spitzen Winkel ergeben zusammen 90°. Nimm den Unterschied weg: 90° − {g(d)} = {g(90 - d)}, je Winkel {g((90 - d) // 2)}. '
                 f'Der größere: {g((90 - d) // 2)} + {g(d)} = {g(gr)}.', 'Die beiden spitzen Winkel ergeben zusammen 90°.')
    if art == 'mehr':
        y = R.choice(range(30, 110, 2))
        d = R.choice(range(4, 40, 2))
        if (180 - y - d) <= 20: return gen_innenwinkelsumme(R, st)
        gr = (180 - y + d) // 2
        return Z(f'In einem Dreieck ist γ = {g(y)}. α ist um {g(d)} größer als β. Wie groß ist α?', gr, f'(180 - {y} + {d}) / 2',
                 f'Für α und β bleiben {g(180 - y)}. Ohne den Unterschied: {g(180 - y)} − {g(d)} = {g(180 - y - d)}, je {g((180 - y - d) // 2)}. '
                 f'α = {g((180 - y - d) // 2)} + {g(d)} = {g(gr)}.', 'Was bleibt für α und β? Nimm dann den Unterschied weg.')
    p, q, r = R.choice([(1, 2, 3), (2, 3, 4), (1, 1, 4), (3, 4, 5), (1, 2, 6), (2, 3, 5), (1, 3, 5), (4, 5, 6), (1, 4, 7), (2, 2, 5), (5, 6, 7)])
    k = Fr(180, p + q + r)
    if k.denominator != 1: return gen_innenwinkelsumme(R, st)
    return Z(f'Die Winkel eines Dreiecks verhalten sich wie {p} : {q} : {r}. Wie groß ist der größte Winkel?', r * k, f'180 / ({p} + {q} + {r}) * {r}',
             f'{p + q + r} Teile = 180°, ein Teil = {g(k)}. Größter Winkel: {r} · {g(k)} = {g(r * k)}.', 'Wie viele gleiche Teile sind es zusammen?')


def gen_aussenwinkel(R, st):
    a, b = _drei(R)
    c = 180 - a - b
    if st == 1:
        if wahl(R, 'aw1', ['neben', 'satz']) == 'neben':
            return Z(f'In einem Dreieck ist γ = {g(c)}. Wie groß ist der Außenwinkel bei C?', 180 - c, f'180 - {c}',
                     f'Der Außenwinkel ist Nebenwinkel von γ: 180° − {g(c)} = {g(180 - c)}.', 'Außenwinkel und Innenwinkel liegen nebeneinander.',
                     grafik=dreieck(a, b, [('C', f'γ = {g(c)}')], aussen=('C', '?')))
        return Z(f'In einem Dreieck ist α = {g(a)} und β = {g(b)}. Wie groß ist der Außenwinkel bei C?', a + b, f'{a} + {b}',
                 f'Außenwinkelsatz: Außenwinkel bei C = α + β = {g(a + b)}.', 'Welche Innenwinkel liegen nicht bei C?',
                 grafik=dreieck(a, b, [('A', g(a)), ('B', g(b))], aussen=('C', '?')))
    if st == 2:
        art = wahl(R, 'aw2', ['B', 'A', 'innen'])
        if art == 'B':
            return Z(f'Der Außenwinkel bei B ist {g(180 - b)}, und α = {g(a)}. Wie groß ist γ?', c, f'(180 - {b}) - {a}',
                     f'Außenwinkel bei B = α + γ. Also γ = {g(180 - b)} − {g(a)} = {g(c)}.', 'Der Außenwinkel bei B ist so groß wie α und γ zusammen.',
                     grafik=dreieck(a, b, [('A', g(a)), ('C', '?')], aussen=('B', g(180 - b))))
        if art == 'A':
            return Z(f'Der Außenwinkel bei A ist {g(180 - a)}, und β = {g(b)}. Wie groß ist γ?', c, f'(180 - {a}) - {b}',
                     f'Außenwinkel bei A = β + γ. Also γ = {g(180 - a)} − {g(b)} = {g(c)}.', 'Der Außenwinkel bei A ist so groß wie β und γ zusammen.',
                     grafik=dreieck(a, b, [('B', g(b)), ('C', '?')], aussen=('A', g(180 - a))))
        return Z(f'Der Außenwinkel bei C ist {g(a + b)}, und α = {g(a)}. Wie groß ist β?', b, f'{a + b} - {a}',
                 f'Außenwinkel bei C = α + β. Also β = {g(a + b)} − {g(a)} = {g(b)}.', 'Welche zwei Innenwinkel ergeben zusammen den Außenwinkel bei C?',
                 grafik=dreieck(a, b, [('A', g(a)), ('B', '?')], aussen=('C', g(a + b))))
    art = wahl(R, 'aw3', ['summe', 'zwei', 'teile'])
    if art == 'summe':
        return Z(f'Bei einem Dreieck sind zwei Außenwinkel {g(180 - a)} und {g(180 - b)}. Wie groß ist der dritte Außenwinkel?', 180 - c,
                 f'360 - {180 - a} - {180 - b}', f'Die drei Außenwinkel ergeben 360°: 360° − {g(180 - a)} − {g(180 - b)} = {g(180 - c)}.',
                 'Rechne mit den Innenwinkeln nach oder nutze die Summe der Außenwinkel.')
    if art == 'zwei':
        return Z(f'Die Außenwinkel bei A und B sind {g(180 - a)} und {g(180 - b)}. Wie groß ist γ?', c, f'180 - (180 - {180 - a}) - (180 - {180 - b})',
                 f'α = 180° − {g(180 - a)} = {g(a)}, β = 180° − {g(180 - b)} = {g(b)}. γ = 180° − {g(a)} − {g(b)} = {g(c)}.', 'Bestimme erst die Innenwinkel bei A und B.')
    k = R.choice([2, 3, 4])
    x = R.randint(12, 140 // (k + 1))
    e = (k + 1) * x
    return Z(f'Der Außenwinkel bei C ist {g(e)}. α ist {k}-mal so groß wie β. Wie groß ist α?', k * x, f'{e} / ({k} + 1) * {k}',
             f'Außenwinkel bei C = α + β = {g(e)}. β ist 1 Teil, α {k} Teile: {k + 1} Teile = {g(e)}, ein Teil {g(x)}. α = {k} · {g(x)} = {g(k * x)}.',
             'Außenwinkelsatz, dann im Verhältnis aufteilen.')


def _viereck_winkel(R):
    for _ in range(200):
        ws = [R.randint(60, 130) for _ in range(3)]
        d = 360 - sum(ws)
        if 60 <= d <= 140: return ws + [d]


def gen_vieleck(R, st):
    if st == 1:
        if wahl(R, 'vi1', ['viereck', 'summe']) == 'viereck':
            ws = _viereck_winkel(R)
            a, b, c, d = ws
            return Z(f'In einem Viereck ist α = {g(a)}, β = {g(b)} und γ = {g(c)}. Wie groß ist δ?', d, f'360 - {a} - {b} - {c}',
                     f'Winkelsumme im Viereck 360°: 360° − {g(a)} − {g(b)} − {g(c)} = {g(d)}.', 'Ein Viereck zerfällt in zwei Dreiecke.',
                     grafik=vieleck_fig(ws, [(0, g(a)), (1, g(b)), (2, g(c)), (3, '?')], seed=a * b))
        n = R.randint(5, 8)
        return Z(f'Wie groß ist die Winkelsumme in einem {n}-Eck?', (n - 2) * 180, f'({n} - 2) * 180', f'({n} − 2) · 180° = {g((n - 2) * 180)}.',
                 'Wie viele Dreiecke entstehen von einer Ecke aus?', grafik=regelmaessig(n, diagonalen=True))
    if st == 2:
        art = wahl(R, 'vi2', ['regel', 'dreiecke', 'fehlend5', 'sechs'])
        if art == 'regel':
            n = R.choice([5, 6, 8, 9, 10, 12, 15, 18, 20])
            w = Fr((n - 2) * 180, n)
            return Z(f'Wie groß ist jeder Innenwinkel eines regelmäßigen {n}-Ecks?', w, f'({n} - 2) * 180 / {n}',
                     f'Winkelsumme ({n} − 2) · 180° = {g((n - 2) * 180)}, verteilt auf {n} gleiche Winkel: {g(w)}.', 'Erst die Winkelsumme, dann gleichmäßig verteilen.',
                     grafik=regelmaessig(n, '?'))
        if art == 'dreiecke':
            n = R.randint(6, 14)
            return Z(f'Von einer Ecke eines {n}-Ecks zieht man alle Diagonalen. In wie viele Dreiecke wird das {n}-Eck zerlegt?', n - 2, f'{n} - 2',
                     f'Die Ecke selbst und ihre beiden Nachbarn liefern keine Diagonale: {n} − 3 Diagonalen, {n} − 2 Dreiecke.', 'Probiere es mit einem Fünfeck aus.', einheit=None,
                     grafik=regelmaessig(n))
        if art == 'sechs':
            ws = [R.randint(100, 140) for _ in range(5)]
            f = 720 - sum(ws)
            if not 95 <= f <= 160: return gen_vieleck(R, st)
            return Z(f'Ein Sechseck hat die Winkel {", ".join(g(x) for x in ws)} und einen sechsten Winkel. Wie groß ist er?', f, f'720 - {" - ".join(map(str, ws))}',
                     f'Winkelsumme im Sechseck: 4 · 180° = 720°. 720° − {g(sum(ws))} = {g(f)}.', 'Winkelsumme im Sechseck: (6 − 2) · 180°.',
                     grafik=vieleck_fig(ws + [f], [(i, g(x)) for i, x in enumerate(ws)] + [(5, '?')], seed=sum(ws)))
        ws = [R.randint(85, 140) for _ in range(4)]
        f = 540 - sum(ws)
        if not 70 <= f <= 160: return gen_vieleck(R, st)
        return Z(f'Ein Fünfeck hat die Winkel {", ".join(g(x) for x in ws)} und einen fünften Winkel. Wie groß ist er?', f, f'540 - {" - ".join(map(str, ws))}',
                 f'Winkelsumme im Fünfeck: 3 · 180° = 540°. 540° − {g(sum(ws))} = {g(f)}.', 'Winkelsumme im Fünfeck: (5 − 2) · 180°.',
                 grafik=vieleck_fig(ws + [f], [(i, g(x)) for i, x in enumerate(ws)] + [(4, '?')], seed=sum(ws)))
    art = wahl(R, 'vi3', ['rueck', 'summe_n', 'viereck_teile'])
    if art == 'rueck':
        n = R.choice([5, 6, 8, 9, 12, 15, 18, 20, 24, 30, 36])
        w = Fr((n - 2) * 180, n)
        if w.denominator != 1: return gen_vieleck(R, st)
        um = str(round((n - 3) * 180 / (n - 1), 1)).replace('.', ',').removesuffix(',0')
        probe = f'{n - 1}-Eck: etwa {um}° (zu klein), {n}-Eck: {g(w)}'
        return Z(f'Jeder Innenwinkel eines regelmäßigen Vielecks ist {g(w)} groß. Wie viele Ecken hat es?', n, f'360 / (180 - {w})',
                 f'Probieren mit (n − 2) · 180° : n: {probe}. Also hat es {n} Ecken. (Kontrolle: {n} · {g(w)} = {g(n * w)} = ({n} − 2) · 180°.)',
                 'Probiere: Für welches n ergibt (n − 2) · 180° : n genau diesen Winkel? Je mehr Ecken, desto größer der Winkel.', einheit=None)
    if art == 'summe_n':
        n = R.randint(6, 20)
        return Z(f'Ein Vieleck hat die Winkelsumme {g((n - 2) * 180)}. Wie viele Ecken hat es?', n, f'{(n - 2) * 180} / 180 + 2',
                 f'{g((n - 2) * 180)} : 180° = {n - 2} Dreiecke. Es sind immer 2 Ecken mehr als Dreiecke: n = {n}.', 'Teile durch 180° und denke an das „− 2“.', einheit=None)
    x = R.randint(20, 50)
    d = 360 - 6 * x
    if d <= 20 or d >= 180: return gen_vieleck(R, st)
    return Z(f'In einem Viereck ist β doppelt so groß wie α, γ dreimal so groß wie α, und δ = {g(d)}. Wie groß ist α?', x, f'(360 - {d}) / 6',
             f'Für α, β und γ bleiben 360° − {g(d)} = {g(360 - d)}. α ist 1 Teil, β 2 Teile, γ 3 Teile: 6 Teile = {g(360 - d)}, also α = {g(x)}.',
             'Was bleibt für α, β und γ? Wie viele gleiche Teile sind das?')


def gen_figuren(R, st):
    if st == 1:
        if wahl(R, 'fi1', ['dreieck', 'parallelogramm']) == 'dreieck':
            a, b = R.randint(35, 80), R.randint(35, 80)
            return Z(f'g ∥ h. Die Ecke C des Dreiecks liegt auf g, A und B auf h. Der Innenwinkel ∢CAB ist {g(a)}. Welchen Winkel bilden [CA] und g links von C?', a, f'{a}',
                     f'Wechselwinkel an Parallelen: {g(a)}.', 'Die Seite [CA] schneidet beide Parallelen.', grafik=zwischen(a, b, [('A', g(a)), ('CL', '?')]))
        x = R.randint(45, 135)
        if x == 90: x = 95
        return Z(f'Im Parallelogramm ABCD ist ∢DAB = {g(x)}. Wie groß ist ∢ABC?', 180 - x, f'180 - {x}',
                 f'Verlängere [AB] über B hinaus. Dort bildet [BC] mit der Verlängerung den Stufenwinkel zu ∢DAB (AD ∥ BC): {g(x)}. ∢ABC ist sein Nebenwinkel: 180° − {g(x)} = {g(180 - x)}.',
                 'Verlängere [AB] über B hinaus: Stufenwinkel und Nebenwinkel.', grafik=parallelogramm(x, [(('A', 'B', 'D'), g(x)), (('B', 'C', 'A'), '?')]))
    if st == 2:
        art = wahl(R, 'fi2', ['trapez', 'raute', 'dreieck_par', 'parallelogramm_c'])
        if art == 'trapez':
            a, b = R.randint(45, 85), R.randint(45, 85)
            ziel = R.choice(['D', 'C'])
            w = 180 - (a if ziel == 'D' else b)
            return Z(f'Im Trapez ABCD ist AB ∥ CD, ∢DAB = {g(a)} und ∢ABC = {g(b)}. Wie groß ist der Winkel bei {ziel}?', w, f'180 - {a if ziel == "D" else b}',
                     f'Verlängere [DC] über {ziel} hinaus. Der Winkel zwischen Verlängerung und [{"DA" if ziel == "D" else "CB"}] ist Wechselwinkel zu ∢{"DAB" if ziel == "D" else "ABC"} (AB ∥ CD): {g(180 - w)}. '
                     f'Der Winkel bei {ziel} ist sein Nebenwinkel: 180° − {g(180 - w)} = {g(w)}.',
                     'Verlängere [AB] und nutze Stufen- und Nebenwinkel.', grafik=trapez(a, b, [('A', g(a)), ('B', g(b)), (ziel, '?')]))
        if art == 'raute':
            a = R.choice(range(40, 140, 2))
            if a == 90: a = 92
            return Z(f'In der Raute ABCD ist ∢DAB = {g(a)}. Wie groß ist ∢CAB zwischen der Diagonalen [AC] und der Seite [AB]?', a // 2, f'{a} / 2',
                     f'Die Diagonale ist Symmetrieachse der Raute und halbiert den Winkel: {g(a)} : 2 = {g(a // 2)}.', 'Was macht eine Symmetrieachse mit dem Eckwinkel?',
                     grafik=raute(a, [(('A', 'B', 'D'), g(a)), (('A', 'B', 'C'), '?')]))
        if art == 'parallelogramm_c':
            x = R.randint(45, 135)
            if x == 90: x = 100
            return Z(f'Im Parallelogramm ABCD ist ∢DAB = {g(x)}. Wie groß ist ∢BCD?', x, f'180 - (180 - {x})',
                     f'∢ABC = 180° − {g(x)} = {g(180 - x)} (Stufenwinkel an AD ∥ BC, dann Nebenwinkel). Genauso an AB ∥ DC: ∢BCD = 180° − {g(180 - x)} = {g(x)}. '
                     f'Gegenüberliegende Winkel sind gleich groß.', 'Gehe über den Winkel bei B.', grafik=parallelogramm(x, [(('A', 'B', 'D'), g(x)), (('C', 'D', 'B'), '?')]))
        a, b = R.randint(35, 80), R.randint(35, 80)
        return Z(f'g ∥ h. Die Ecke C des Dreiecks liegt auf g, A und B auf h. Bei C bilden g und [CA] links {g(a)}, [CB] und g rechts {g(b)}. Wie groß ist ∢BCA?',
                 180 - a - b, f'180 - {a} - {b}', f'An C liegen auf g drei Winkel nebeneinander: 180° − {g(a)} − {g(b)} = {g(180 - a - b)}.', 'Winkel an einer Geraden ergeben 180°.',
                 grafik=zwischen(a, b, [('CL', g(a)), ('CR', g(b)), ('C', '?')]))
    art = wahl(R, 'fi3', ['kette', 'dia', 'zwei_par', 'kette_rueck'])
    if art == 'kette_rueck':
        a, b = R.randint(25, 65), R.randint(25, 65)
        return Z(f'g ∥ h. Ein Weg geht von A auf g zu einem Punkt P zwischen den Geraden und weiter zu B auf h. Bei A bildet der Weg mit g den Winkel {g(a)}, und ∢APB = {g(a + b)}. '
                 f'Welchen Winkel bildet der Weg bei B mit h?', b, f'{a + b} - {a}',
                 f'Hilfslinie durch P parallel zu g (und h): Der obere Teil von ∢APB ist Wechselwinkel zum Winkel bei A, also {g(a)}. '
                 f'Der untere Teil ist {g(a + b)} − {g(a)} = {g(b)} und Wechselwinkel zum Winkel bei B.', 'Zeichne durch P eine Parallele zu g und teile ∢APB auf.',
                 grafik=zickzack(a, b, [('A', g(a)), ('P', g(a + b)), ('B', '?')]))
    if art == 'kette':
        a, b = R.randint(25, 65), R.randint(25, 65)
        return Z(f'g ∥ h. Ein Weg geht von A auf g zu einem Punkt P zwischen den Geraden und weiter zu B auf h. Bei A bildet der Weg mit g den Winkel {g(a)}, bei B mit h den Winkel {g(b)}. Wie groß ist ∢APB?',
                 a + b, f'{a} + {b}', f'Hilfslinie durch P parallel zu g: Sie teilt ∢APB in zwei Wechselwinkel {g(a)} und {g(b)}. Zusammen {g(a + b)}.',
                 'Zeichne durch P eine Parallele zu g.', grafik=zickzack(a, b, [('A', g(a)), ('B', g(b)), ('P', '?')]))
    if art == 'dia':
        a, b = R.randint(20, 60), R.randint(20, 60)
        frage = R.choice(['ACD', 'ACB'])
        w = a if frage == 'ACD' else b
        return Z(f'Im Parallelogramm ABCD bildet die Diagonale [AC] mit [AB] den Winkel {g(a)} und mit [AD] den Winkel {g(b)}. Wie groß ist ∢{frage}?', w, f'{w}',
                 f'{"AB ∥ DC" if frage == "ACD" else "AD ∥ BC"} und [AC] schneidet beide: ∢{frage} ist Wechselwinkel zu ∢{"CAB" if frage == "ACD" else "CAD"} = {g(w)}.',
                 'Welche Seiten sind parallel, und welche Linie schneidet sie?',
                 grafik=parallelogramm(a + b, [(('A', 'B', 'C'), g(a)), (('A', 'C', 'D'), g(b)), ((('C', 'D', 'A') if frage == 'ACD' else ('C', 'A', 'B')), '?')], a1=a))
    a, c = R.randint(35, 75), R.randint(40, 80)
    b = 180 - a - c
    if not 30 <= b <= 90: return gen_figuren(R, st)
    return Z(f'g ∥ h. Die Ecke C des Dreiecks liegt auf g, A und B auf h. Links von C bilden g und [CA] den Winkel {g(a)}, und ∢BCA = {g(c)}. Wie groß ist ∢ABC?', b,
             f'180 - {a} - {c}', f'Rechts von C bilden [CB] und g den Winkel 180° − {g(a)} − {g(c)} = {g(b)} (Winkel an g). Wechselwinkel dazu ist ∢ABC = {g(b)}.',
             'Erst die drei Winkel an g bei C, dann ein Wechselwinkel.', grafik=zwischen(a, b, [('CL', g(a)), ('C', g(c)), ('B', '?')]))


BEGR = [('Nebenwinkel ergänzen sich zu 180°.', 'Zwei Winkel liegen an einer Geraden nebeneinander.'),
        ('Scheitelwinkel sind gleich groß.', 'Zwei Winkel liegen sich an einer Kreuzung gegenüber.'),
        ('Stufenwinkel an Parallelen sind gleich groß.', 'Zwei Winkel liegen an zwei Kreuzungen mit Parallelen in gleicher Lage.'),
        ('Wechselwinkel an Parallelen sind gleich groß.', 'Zwei Winkel liegen an Parallelen über Kreuz zwischen den Geraden.'),
        ('Die Winkelsumme im Dreieck ist 180°.', 'Die drei Innenwinkel eines Dreiecks werden addiert.')]
SAETZE = {'W': 'Wechselwinkel an Parallelen sind gleich groß.', 'D': 'Die Winkelsumme im Dreieck ist 180°.', 'V': 'Die Winkelsumme im Viereck ist 360°.',
          'F': 'Die Winkelsumme im Fünfeck ist 540°.', 'S': 'Die Winkelsumme im Sechseck ist 720°.', 'St': 'Stufenwinkel an Parallelen sind gleich groß.'}


def gen_beweisen(R, st):
    if st == 1:
        if wahl(R, 'bw1', ['lage', 'begruendung']) == 'lage':
            i = R.randrange(len(BEGR))
            satz, lage = BEGR[i]
            return A(R, f'Welcher Winkelsatz passt zu dieser Lage? {lage}', satz, R.sample([s for j, (s, _) in enumerate(BEGR) if j != i], 3),
                     f'Passend ist: {satz}', 'Wo liegen die Winkel: an einer oder an zwei Kreuzungen?')
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
        return A(R, f'Jemand schreibt: „Der Winkel links oberhalb ist {g(180 - a)}, weil der Winkel rechts oberhalb an derselben Kreuzung {g(a)} ist.“ Welche Begründung muss genannt werden?',
                 'Nebenwinkel ergänzen sich zu 180°.', ['Scheitelwinkel sind gleich groß.', 'Stufenwinkel an Parallelen sind gleich groß.', 'Die Winkelsumme im Dreieck ist 180°.'],
                 f'Beide liegen an derselben Kreuzung nebeneinander an einer Geraden: {g(a)} + {g(180 - a)} = 180°.', 'Liegen die Winkel nebeneinander oder gegenüber?',
                 grafik=einfach(a, [('ro', g(a)), ('lo', g(180 - a))]))
    if st == 2:
        art = wahl(R, 'bw2', ['art', 'stuetzt', 'zirkel', 'kette'])
        if art == 'art':
            k = R.choice(['W', 'D', 'V', 'F', 'S', 'St'])
            fund = k == 'W'
            w = ('Er steht ganz unten in der Kette und wird vorausgesetzt.' if fund else
                 {'D': 'Er wird mit Wechselwinkeln an der Parallelen durch C bewiesen.', 'V': 'Er folgt aus der Winkelsumme im Dreieck (eine Diagonale, zwei Dreiecke).',
                  'F': 'Er folgt aus der Winkelsumme im Dreieck (drei Dreiecke).', 'S': 'Er folgt aus der Winkelsumme im Dreieck (vier Dreiecke).',
                  'St': 'Er folgt aus Wechselwinkeln und Scheitelwinkeln: Der Stufenwinkel ist Scheitelwinkel eines Wechselwinkels.'}[k])
            return A(R, f'In unserem Aufbau der Winkelsätze: Ist „{SAETZE[k][:-1]}“ der Fundamentalsatz oder ein abgeleiteter Satz?',
                     'der Fundamentalsatz' if fund else 'ein abgeleiteter Satz', ['ein abgeleiteter Satz' if fund else 'der Fundamentalsatz', 'keins von beiden, nur eine Messung'],
                     w, 'Was steht ganz unten in der Kette?')
        if art == 'stuetzt':
            k = R.choice(['D', 'V', 'F', 'S', 'St'])
            richtig = {'D': SAETZE['W'], 'V': SAETZE['D'], 'F': SAETZE['D'], 'S': SAETZE['D'], 'St': SAETZE['W']}[k]
            # Nachprüfung 17.11.: Ein Vieleck lässt sich auch in kleinere Vielecke zerlegen (Sechseck = zwei Vierecke). Sätze über Vielecke mit weniger Ecken
            # wären deshalb als Antwort ebenfalls vertretbar und dürfen nicht als falsche Auswahl erscheinen.
            # Ebenso beim Stufenwinkel-Satz: Sein Beweis braucht Wechselwinkel UND Scheitelwinkel – „Scheitelwinkel“ ist dort keine falsche Antwort.
            kleiner = {'F': [SAETZE['V']], 'S': [SAETZE['V'], SAETZE['F']], 'St': ['Scheitelwinkel sind gleich groß.']}.get(k, [])
            falsch = [x for x in [SAETZE['W'], SAETZE['D'], SAETZE['V'], 'Scheitelwinkel sind gleich groß.', SAETZE['F'], 'Nebenwinkel ergänzen sich zu 180°.', SAETZE['St']]
                      if x != richtig and x != SAETZE[k] and x not in kleiner]
            return A(R, f'Auf welchen Satz stützt sich der Beweis von „{SAETZE[k][:-1]}“ direkt?', richtig, R.sample(falsch, 3),
                     {'D': 'Die Parallele durch C bringt α und β als Wechselwinkel nach C.', 'V': 'Eine Diagonale teilt das Viereck in zwei Dreiecke mit je 180°.',
                      'F': 'Die Diagonalen von einer Ecke teilen das Fünfeck in drei Dreiecke mit je 180°.', 'S': 'Die Diagonalen von einer Ecke teilen das Sechseck in vier Dreiecke mit je 180°.',
                      'St': 'Der Stufenwinkel ist Scheitelwinkel eines Wechselwinkels; dazu braucht man den Satz über Wechselwinkel (und Scheitelwinkel).'}[k],
                     'Welcher Satz wird im Beweis als Werkzeug benutzt?')
        if art == 'zirkel':
            k = R.choice(['V', 'F', 'S'])
            n = {'V': 'Viereck', 'F': 'Fünfeck', 'S': 'Sechseck'}[k]
            return A(R, f'Jemand begründet „Die Winkelsumme im Dreieck ist 180°“ mit der Winkelsumme im {n}. Was ist das Problem?',
                     f'Die Winkelsumme im {n} wird selbst mit der im Dreieck bewiesen – ein Zirkelschluss.',
                     ['Kein Problem, das ist ein gültiger Beweis.', f'Die Winkelsumme im {n} ist falsch.', 'Man muss die Winkel zuerst messen.'],
                     f'Der Satz über das {n} folgt aus der Winkelsumme im Dreieck. Man darf ihn nicht benutzen, um die Winkelsumme im Dreieck zu beweisen.',
                     f'Woraus wurde der Satz über das {n} bewiesen?')
        ziel = R.choice(['V', 'F', 'S'])
        n = {'V': 'Viereck', 'F': 'Fünfeck', 'S': 'Sechseck'}[ziel]
        r = f'Wechselwinkel → Winkelsumme im Dreieck → Winkelsumme im {n}'
        return A(R, f'Welche Reihenfolge der Beweiskette bis zur „Winkelsumme im {n}“ ist richtig?', r,
                 [f'Winkelsumme im Dreieck → Wechselwinkel → Winkelsumme im {n}', f'Winkelsumme im {n} → Winkelsumme im Dreieck → Wechselwinkel',
                  f'Wechselwinkel → Winkelsumme im {n} → Winkelsumme im Dreieck'],
                 f'Ganz unten steht der Fundamentalsatz (Wechselwinkel). Daraus folgt die Winkelsumme im Dreieck, daraus die im {n}.', 'Was steht ganz unten in der Kette?')
    art = wahl(R, 'bw3', ['gegen', 'stumpf', 'viereck', 'fuenfeck', 'umkehr', 'messung'])
    if art == 'gegen':
        return A(R, 'Behauptung: „Wenn zwei Winkel zusammen 180° ergeben, sind sie Nebenwinkel.“ Was stimmt?', 'Falsch: Auch zwei Winkel an verschiedenen Stellen können zusammen 180° ergeben.',
                 ['Richtig, das ist die Definition.', 'Richtig, denn Nebenwinkel ergeben 180°.', 'Falsch: Nebenwinkel ergeben 360°.'],
                 'Gegenbeispiel: Im Parallelogramm ergeben die Winkel bei A und B zusammen 180°, liegen aber an verschiedenen Ecken. Die Umkehrung eines Satzes muss eigens geprüft werden.',
                 'Suche ein Gegenbeispiel.')
    if art == 'stumpf':
        return A(R, 'Warum kann ein Dreieck höchstens einen stumpfen Winkel haben?', 'Zwei stumpfe Winkel wären zusammen schon mehr als 180°.',
                 ['Weil stumpfe Winkel immer bei C liegen.', 'Weil man es so zeichnet.', 'Das stimmt nicht, es können zwei sein.'],
                 'Ein stumpfer Winkel ist größer als 90°. Zwei davon ergäben mehr als 180° – mehr als die ganze Winkelsumme.', 'Denke an die Winkelsumme.')
    if art == 'viereck':
        return A(R, 'Wie beweist man, dass die Winkelsumme im Viereck 360° ist?', 'Eine Diagonale teilt das Viereck in zwei Dreiecke: 2 · 180° = 360°.',
                 ['Man misst vier Winkel und addiert.', 'Ein Viereck hat 4 rechte Winkel.', 'Man nimmt an, dass alle Vierecke gleich sind.'],
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


def fest(R):
    F = {}
    F['scheitel_neben'] = [
        Z('Drei Geraden schneiden sich in einem Punkt und bilden sechs Winkel. Zwei benachbarte Winkel sind 40° und 65° groß. Wie groß ist der größte der sechs Winkel?',
          75, '180 - 40 - 65', 'Drei benachbarte Winkel füllen eine Gerade: 180° − 40° − 65° = 75°. Die anderen drei sind Scheitelwinkel (40°, 65°, 75°). Größter: 75°.',
          'Drei nebeneinander liegende Winkel ergeben 180°. Die übrigen drei sind Scheitelwinkel.', art=P),
        A(R, 'Warum sind Scheitelwinkel immer gleich groß?', 'Beide ergänzen denselben Nebenwinkel zu 180°.',
          ['Weil sie gegenüberliegen und deshalb gleich aussehen.', 'Weil alle Winkel an einer Kreuzung gleich groß sind.', 'Weil man es messen kann.'],
          'α + β = 180° und γ + β = 180° (β ist Nebenwinkel von beiden). Also α = 180° − β = γ.', 'Suche einen Winkel, der neben beiden liegt.', art=P,
          grafik=einfach(60, [('ro', 'α'), ('lo', 'β'), ('lu', 'γ')])),
        Z('Ein Winkel an einer Kreuzung ist viermal so groß wie sein Nebenwinkel. Wie groß ist sein Scheitelwinkel?', 144, '4 * 180 / 5',
          'Der Nebenwinkel ist 1 Teil, der Winkel 4 Teile: 5 Teile = 180°, ein Teil = 36°. Der Winkel ist 4 · 36° = 144°; sein Scheitelwinkel ebenfalls 144°.',
          'Wie viele gleiche Teile ergeben zusammen 180°? Dann der Scheitelwinkel.', art=K)]
    F['stufen_wechsel'] = [
        Z('Eine Rampe steigt um 38° gegen die Waagrechte an. Der Handlauf ist parallel zur Rampe, die Pfosten stehen senkrecht. Wie groß ist der spitze Winkel zwischen Pfosten und Handlauf?',
          52, '90 - 38', 'Pfosten und Waagrechte bilden 90°. Der Handlauf ist um 38° geneigt (Stufenwinkel zur Rampe). Spitzer Winkel zum Pfosten: 90° − 38° = 52°.',
          'Der Pfosten steht senkrecht auf der Waagrechten.', art=P),
        Z('g ∥ h. Ein Dreieck hat die Ecke C auf g und die Ecken A und B auf h. Der Innenwinkel bei A ist 55°, bei B 70°. Welchen Winkel bildet [CB] rechts von C mit g (siehe Bild)?', 70, '70',
          '[CB] schneidet die Parallelen g und h. Der Winkel rechts von C und β = 70° liegen über Kreuz zwischen den Parallelen: Wechselwinkel.', 'Welche Seite schneidet beide Parallelen?',
          art=P, grafik=zwischen(55, 70, [('A', '55°'), ('B', '70°'), ('CR', '?')])),
        Z('g ∥ h. Ein Weg führt von A auf g zu einem Punkt P zwischen den Geraden und weiter zu B auf h. Bei A ist der Winkel 32°, bei B 51° (siehe Bild). Wie groß ist der Winkel bei P?',
          83, '32 + 51', 'Hilfslinie durch P parallel zu g: Sie teilt den Winkel bei P in die Wechselwinkel 32° und 51°. Zusammen 83°.',
          'Zeichne durch P eine dritte Parallele.', art=K, grafik=zickzack(32, 51, [('A', '32°'), ('B', '51°'), ('P', '?')]))]
    F['parallel_pruefen'] = [
        A(R, 'k schneidet g in S und h in T. Bei S ist der Winkel rechts oberhalb 72°, bei T der Winkel links unterhalb 64°. Welche Aussage ist richtig begründet?',
          'g und h sind nicht parallel, denn die Wechselwinkel wären sonst gleich groß.',
          ['g und h sind parallel, denn beide Winkel sind spitz.', 'g und h sind parallel, denn die Winkel liegen sich gegenüber.', 'Das lässt sich ohne Längen nicht entscheiden.'],
          'Bei S links unterhalb ist der Scheitelwinkel 72°. Bei T rechts oberhalb ist der Scheitelwinkel 64°. Diese beiden sind Wechselwinkel. 72° ≠ 64°: nicht parallel.',
          'Bringe beide Winkel mit Scheitelwinkeln in die Lage von Wechselwinkeln.', art=P, grafik=doppel(72, [('S', 'ro', '72°'), ('T', 'lu', '64°')], ro_t=64)),
        Z('Die Geraden g und h schneiden sich außerhalb des Blattes. Eine Gerade k schneidet g in S unter 75° und h in T unter 68° (beide Winkel rechts oberhalb). Unter welchem Winkel schneiden sich g und h?',
          7, '75 - 68', 'Zeichne durch T eine Parallele g′ zu g. Stufenwinkel: g′ bildet mit k rechts oberhalb auch 75°. h bildet mit k nur 68°. '
          'Also liegen zwischen g′ und h 75° − 68° = 7°. Weil g′ ∥ g, schneiden sich auch g und h unter 7°.',
          'Zeichne durch T eine Parallele zu g und vergleiche.', art=P, grafik=doppel(75, [('S', 'ro', '75°'), ('T', 'ro', '68°')], ro_t=68)),
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
        Z('Im Kreis um M ist [AB] ein Durchmesser, C liegt auf dem Kreis, und ∢BAC = 34°. Das Dreieck AMC ist gleichschenklig, denn MA und MC sind Radien. '
          'Im gleichschenkligen Dreieck sind die beiden Basiswinkel gleich groß. Wie groß ist ∢BMC?', 68, '2 * 34',
          'Die Basiswinkel im Dreieck AMC sind gleich: ∢MCA = ∢MAC = 34°. ∢BMC ist Außenwinkel des Dreiecks AMC bei M: 34° + 34° = 68°.',
          'Welche zwei Innenwinkel des Dreiecks AMC liegen nicht bei M?', art=P, grafik=kreis_aussen(34)),
        Z('Bei einem Dreieck ABC ist der Außenwinkel bei B 128° und der Außenwinkel bei C 117°. Wie groß ist α?', 65, '180 - (180 - 128) - (180 - 117)',
          'β = 180° − 128° = 52°, γ = 180° − 117° = 63°. α = 180° − 52° − 63° = 65°.', 'Bestimme erst β und γ.', art=P),
        A(R, 'Kann ein Dreieck drei spitze Außenwinkel haben?', 'Nein: Die Außenwinkel ergeben zusammen 360°, drei spitze aber weniger als 270°.',
          ['Ja, bei einem gleichseitigen Dreieck.', 'Ja, wenn alle Innenwinkel stumpf sind.', 'Nein, weil Außenwinkel immer 90° sind.'],
          'Jeder Außenwinkel ist 180° minus Innenwinkel; zusammen 3 · 180° − 180° = 360°. Drei Winkel unter 90° ergeben höchstens 270°.',
          'Was ergeben die drei Außenwinkel zusammen?', art=K)]
    F['vieleck'] = [
        Z('In welchem regelmäßigen Vieleck ist jeder Innenwinkel 144° groß? Gib die Zahl der Ecken an.', 10, '360 / (180 - 144)',
          'Probieren mit (n − 2) · 180° : n: Achteck 135°, Neuneck 140°, Zehneck 1 440° : 10 = 144°. Also 10 Ecken.',
          'Je mehr Ecken, desto größer jeder Winkel. Probiere 8, 9, 10 Ecken.', einheit=None, art=P, grafik=regelmaessig(10, '144°')),
        A(R, 'Warum hat ein n-Eck die Winkelsumme (n − 2) · 180°?', 'Von einer Ecke aus zerlegen die Diagonalen das n-Eck in n − 2 Dreiecke.',
          ['Weil jedes n-Eck n Dreiecke enthält.', 'Weil man 2 Ecken nicht mitzählt.', 'Weil jeder Winkel 180° − 2° hat.'],
          'Von einer Ecke gibt es n − 3 Diagonalen; sie zerlegen das n-Eck in n − 2 Dreiecke mit je 180°.', 'Zeichne ein Sechseck und zähle die Dreiecke.', art=P,
          grafik=regelmaessig(6, diagonalen=True)),
        Z('Ein Vieleck hat die Winkelsumme 1 440°. Wie viele Diagonalen gehen von einer Ecke aus?', 7, '1440 / 180 + 2 - 3',
          '1 440° : 180° = 8 Dreiecke, also n = 8 + 2 = 10 Ecken. Von einer Ecke gehen n − 3 = 7 Diagonalen aus.', 'Bestimme zuerst die Zahl der Ecken.', einheit=None, art=K)]
    F['figuren'] = [
        Z('Die Geraden g und h schneiden sich in einem Punkt X. Eine Gerade k schneidet g unter 64° und h unter 81° (siehe Bild). Unter welchem Winkel schneiden sich g und h?',
          35, '180 - 64 - 81', 'g, h und k bilden ein Dreieck mit den Winkeln 64° und 81°. Der dritte Winkel bei X ist 180° − 64° − 81° = 35°.',
          'Die drei Geraden bilden ein Dreieck.', art=P, grafik=drei_geraden(64, 81)),
        Z('Im Parallelogramm ABCD bildet die Diagonale [AC] mit [AB] den Winkel 35° und mit [AD] den Winkel 40°. Wie groß ist ∢ACB?', 40, '40',
          'AD ∥ BC, und [AC] schneidet beide: ∢ACB ist Wechselwinkel zu ∢CAD = 40°.', 'Welche Seite ist parallel zu [AD]?', art=P,
          grafik=parallelogramm(75, [(('A', 'B', 'C'), '35°'), (('A', 'C', 'D'), '40°'), (('C', 'A', 'B'), '?')], a1=35)),
        Z('Zwei Spiegel sind parallel. Ein Lichtstrahl trifft Spiegel 1 unter 35° und wird unter 35° zurückgeworfen. Unter welchem Winkel trifft er auf Spiegel 2?',
          35, '35', 'Der zurückgeworfene Strahl bildet mit Spiegel 1 den Winkel 35°. Er schneidet beide Spiegel; am parallelen Spiegel 2 entsteht der Wechselwinkel: wieder 35°.',
          'Der Strahl schneidet beide Spiegel – die Spiegel sind parallel.', art=K, grafik=spiegel(35))]
    F['beweisen'] = [
        L('Beweis der Winkelsumme. Bringe die Kärtchen in die richtige Reihenfolge. Kärtchen 1: „Die drei Winkel an C auf p ergeben 180°. Setzt man α und β ein: α + γ + β = 180°.“ '
          'Kärtchen 2: „Zeichne durch C die Parallele p zu [AB].“ Kärtchen 3: „Das gilt für jedes Dreieck: Die Winkelsumme ist 180°.“ '
          'Kärtchen 4: „Die Winkel links und rechts von C auf p sind so groß wie α und β (Wechselwinkel).“',
          '1. □; 2. □; 3. □; 4. □', [2, 4, 1, 3], ['2', '4', '1', '3'],
          'Zuerst die Hilfslinie (2). Dann die Wechselwinkel (4) – erst danach darf man α und β einsetzen (1). Am Schluss steht der Satz (3).',
          'Was muss zuerst gezeichnet sein, bevor man über Winkel an p reden kann?', 'Trage die Nummern der Kärtchen ein.', art=P),
        A(R, 'Warum hat jedes Dreieck mindestens zwei spitze Winkel?', 'Zwei Winkel von je mindestens 90° ergäben schon 180°, für den dritten bliebe nichts.',
          ['Weil spitze Winkel häufiger sind.', 'Weil ein Dreieck drei Ecken hat.', 'Weil jedes Dreieck einen rechten Winkel hat.'],
          'Wären zwei Winkel 90° oder größer, wäre ihre Summe mindestens 180°. Dann bliebe für den dritten Winkel 0° oder weniger.', 'Nutze die Winkelsumme.', art=P),
        A(R, 'Lisa beweist die Winkelsumme im Viereck mit einer Diagonale. Tom sagt: „Dafür braucht man den Satz über Wechselwinkel gar nicht.“ Was stimmt?',
          'Nicht direkt, aber indirekt: Die Winkelsumme im Dreieck, die Lisa benutzt, wurde mit Wechselwinkeln bewiesen.',
          ['Tom hat recht: Wechselwinkel haben mit Vierecken nichts zu tun.', 'Lisa muss im Viereck vier Wechselwinkel einzeichnen.', 'Die Winkelsumme im Viereck ist ein Fundamentalsatz.'],
          'Die Beweiskette lautet: Wechselwinkel → Winkelsumme im Dreieck → Winkelsumme im Viereck. Ohne das unterste Glied fehlt die Grundlage.',
          'Woraus wurde die Winkelsumme im Dreieck bewiesen?', art=K)]
    return F


PLAN = [('uebung', 1)] * 4 + [('uebung', 2)] * 6 + [('uebung', 3)] * 8 + [('test', 2)] + [('korrektur', 2)] * 3 + [('sicherung', 2)] * 6


def _schl(a):
    """Dubletten über den Aufgabentext – gleiche Frage mit nur anders gemischten Antworten zählt als doppelt."""
    return a['f']['text']
def aufgaben():
    R = random.Random(7098)
    feste = fest(R)
    out, gesehen = [], set()
    beispiele = {s['text'] for e in ETAPPEN for s in e['schritte']}
    anz = collections.Counter()
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
            if art: anz[(lz, art)] += 1
            assert len(a['w']) >= 15 and a['h'], a
            if pool != 'uebung': a.pop('h')
            out.append({'l': lz, 't': lz, 'p': pool, 's': st, **a})
    return out, anz




def datei():
    auf, anz = aufgaben()
    lz = [e['lernziel'] for e in ETAPPEN]
    return {
        **META, 'autor': 'Claude (Vierzehnte Runde, nachgebessert in der Sechzehnten Runde; Generator geometrie.winkelsaetze.py)',
        'inhalt': {
            'ziel': 'Winkel an Geradenkreuzungen und Doppelkreuzungen benennen und berechnen, Parallelität prüfen, die Winkelsumme im Dreieck begründen, '
                    'Winkelsummen im Vieleck nutzen und Winkel in Figuren schrittweise mit Begründung bestimmen. Vertiefung: Außenwinkel am Dreieck.',
            'merke': ['Scheitelwinkel sind gleich groß, Nebenwinkel ergeben 180°.', 'An Parallelen: Stufen- und Wechselwinkel sind gleich groß – und umgekehrt.',
                      'Dreieck: α + β + γ = 180°. Vertiefung: Ein Außenwinkel ist so groß wie die beiden nicht anliegenden Innenwinkel zusammen.',
                      'n-Eck: Winkelsumme (n − 2) · 180°.', 'Jeder Schritt einer Begründung nennt seinen Winkelsatz.'],
            'abschnitte': [{'titel': 'Winkel an Kreuzungen', 'lernziele': ['scheitel_neben', 'stufen_wechsel', 'parallel_pruefen']},
                           {'titel': 'Winkelsummen', 'lernziele': ['innenwinkelsumme', 'aussenwinkel', 'vieleck']},
                           {'titel': 'Begründen in Figuren', 'lernziele': ['figuren', 'beweisen']}],
            'etappen': ETAPPEN,
            'teilfaehigkeiten': [{'k': e['lernziel'], 'text': e['titel'], 'lernziele': [e['lernziel']]} for e in ETAPPEN],
            'bewertung': {'lernziele_pflicht': [x for x in lz if x != 'aussenwinkel'], 'lernziele_vertiefung': ['aussenwinkel'],
                          'testaufgaben_je_lernziel': 1, 'hilfen_im_test': False},
            'quellen': {'erklaerungen': 'Eigene Fassung (Claude).',
                        'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern, Gymnasium M7 2.2 „Winkelbetrachtungen an Figuren“ (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik). '
                                    'Der Außenwinkelsatz steht dort nicht und ist deshalb Vertiefung.',
                        'pruefungsvorbilder': 'Typ und Niveau nach: Bayerischer Mathematik-Test 8 (ISB) 2019 B5/B7, 2021 A8, 2025 A8; Jahrgangsstufentest Realschule 8 (ISB) 2020 II, 2025 II Nr. 5/6; '
                                              'Vergleichsarbeit Jgst. 8 (Innenwinkel im n-Eck). Eigene Zahlen und Einkleidung.'},
        },
        'aufgaben': auf,
        'offen': ['Überschneidung: geometrie.konstruktion (gleicher Ort Addis Abeba) hat schon die Lernkarten „parallelen“, „winkelsumme“ und „vierecke“. '
                  'Liste der überlappenden Karten in inhalte/postfach/winkelsaetze-2.md – Entscheidung Sebastian.',
                  'Winkel werden vom Kind nicht gemessen oder gezeichnet (kann die App nicht). Die Zeichnungen sind maßstäblich: angeschriebene Winkel weichen höchstens 3° ab.',
                  'Der Begriff „Nachbarwinkel“ (E-Winkel) steht nicht im LehrplanPLUS M7 2.2 und wird nicht eingeführt; solche Winkel werden über Stufen- und Nebenwinkel berechnet.'],
    }, anz


# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Klasse 7, siehe _durchsicht_kl7.py) ----
from _durchsicht_kl7 import Durchsicht, durchsicht_datei  # noqa: E402

DS = Durchsicht('geometrie.winkelsaetze', 19_7_4)
# stufen_wechsel: „Nebenwinkel + Stufenwinkel“ ist in Stufe 2 schon da; dreimal derselbe Typ in Stufe 3 → Stufe 2
for _grad in (135, 124, 154):
    DS.stufe('stufen_wechsel', f'g ∥ h. Bei S ist der Winkel links oberhalb {_grad}° groß. Wie groß ist der Winkel bei T rechts oberhalb?', 2)
# parallel_pruefen: dreimal „a ∥ b ∥ c, Winkel bei c“ in Stufe 3 → zwei davon Stufe 2 (eine bleibt als Stufe-3-Aufgabe)
for _grad in (128, 64):
    DS.stufe('parallel_pruefen', f'Es gilt a ∥ b und b ∥ c. Eine Gerade k schneidet a, b und c. Bei a ist der Winkel rechts oberhalb {_grad}°. Wie groß ist bei c der Winkel links oberhalb?', 2)
# ---- DURCHSICHT ENDE ----


if __name__ == '__main__':
    d, anz = datei()
    ZIEL.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{ZIEL.name}: {len(d["inhalt"]["etappen"])} Lernkarten, {len(d["aufgaben"])} Aufgaben')
    for e in d['inhalt']['etappen']:
        l = e['lernziel']
        print(f'  {l:18} Prüfungsvorbild: {anz[(l, P)]}  Knobel: {anz[(l, K)]}')
    durchsicht_datei(META['thema_schluessel'], DS)  # Neunzehnte Runde: zuletzt
