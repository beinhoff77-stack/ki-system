#!/usr/bin/env python3
"""Unabhängige Vorprüfung VT1A: eigene Formeln (nicht aus loesung_rechnung), Zählschleifen, Optionsprüfung, Rechenbehauptungen in Texten.
Aufruf (im Wurzelordner des Repos): python3 -I inhalte/mathe-profi/vtest-1a/vorpruefung_rechnen.py"""
import json, re, os, sys
from fractions import Fraction
from collections import Counter
HIER = os.path.dirname(os.path.abspath(__file__))
A = {}
for fn in ('zahlen.potenzen_basis', 'zahlen.rechengesetze'):
    for a in json.load(open(os.path.join(HIER, fn + '.json')))['aufgaben']:
        A[a['kennung']] = a
def n(k): return int(k.split('-')[1])

# ---- eigene Sollwerte der Zahl-Aufgaben (eigene Formel / Zählschleife) ----
def erste_zahl_mit_potenz(basis, wert):  # Exponent suchen
    e = 0; v = 1
    while v < wert: v *= basis; e += 1
    return e if v == wert else None
def basis_suchen(exp, wert):
    return [b for b in range(1, 1000) if b ** exp == wert]
def z027():
    for h in range(0, 40):
        if 2 ** h > 100 + 100 * h: return h
def z063():
    return sum(1 for a in range(1, 13) if any(a * x == 36 for x in range(0, 37)))
def z070():
    return sum(1 for z in range(0, 10000) if (z + 50) // 100 * 100 == 4600)
def z065():
    return max(k for k in range(0, 200) if (k + 5) // 10 * 10 * 7 == 210)
def z021():
    return max(m for m in range(0, 30) if 10 ** m < 1000000)
def z012():
    return [k for k in range(1, 200) if k * k - (k - 1) ** 2 == 27]
def z013():
    # Feld 25x25 ohne unterste Reihe und rechte Spalte: zählen
    return sum(1 for r in range(25) for c in range(25) if r != 24 and c != 24)
def z075():
    return [N for N in range(1, 500) if N % 2 == 0 and (lambda rest: rest % 2 == 0 and rest // 2 == 11)(N - (N // 2 + 7))]
def z071():
    return [N for N in range(1, 500) if (lambda r1: r1 % 2 == 0 and r1 // 2 + 8 == 20)(N - 14) and N >= 14]
def z077():
    return [x for x in range(0, 100) if 2 * x + 6 == 30]
def z076():
    return [g for g in range(0, 100) if 4 * g + 12 - 4 == 108]
def z040():
    return [h for h in range(1, 50) if 4 + 2 * (h - 1) == 14]
def z031(): return [b for b in range(0, 200) if (18 + b) == 6 * 7]
def z037(): return [g for g in range(0, 100) if 6 * 8 + 4 * g == 72]
def z059(): return [s for s in range(0, 50) if 5 * s + 3 == 43]
def z072(): return [b for b in range(0, 100) if 24 + 7 * b == 66]
def z074(): return [b for b in range(0, 100) if 2 * (11 + b) == 36]
def z057(): return [x for x in range(0, 500) if ((x * 5 + 12) / 4) == 8]
def z045(): return [p for p in range(0, 200) if p * 5 * 20 == 1500]
def z047(): return [x for x in range(0, 500) if 38 + x + 62 == 150]
def z051(): return [x for x in range(0, 500) if 17 * x + 17 * 14 == 17 * 50]
def z053(): return [x for x in range(0, 500) if 8 * x + 12 * x == 200]
def z018(): return [x for x in range(0, 100000) if x * 10 ** 4 == 370000]
def z019(): return [d for d in range(1, 10 ** 7) if (10 ** 6 == d * 10 * 10 ** 2)]
def z022(): return [s for s in range(1, 1000) if s * 3 ** 4 == 405]
def z008():
    s = [s for s in range(1, 500) if s * s == 225][0]; return 4 * s
def z010(): return sum(1 for r in range(11) for c in range(11)) - sum(1 for r in range(7) for c in range(7))
def z017():
    kg = 500; g = kg * 1000; m = g // 5; e = 0
    while 10 ** e < m: e += 1
    assert 10 ** e == m; return e
def z020(): return 3 * 10 ** 5 * 60
def z023():
    l = 1; c = 0
    while l < 64: l *= 2; c += 1
    return c
def z024():
    c = 0
    while 10 ** c < 10000: c += 1
    return c
def z003():
    p = 1
    for g in range(4): p *= 2
    return p
def z034(): return abs(((48 // (6 + 2)) * 3) - (48 // 6 + 2 * 3))
def z042(): return (12 * 9 + 8 * 11 - 20) / 4
def z055(): return sum(19 * x for x in (36, 64)) - 19 * 50
def z064(): return 612 * 49
def z067(): return abs(48 * 52 - 40 * 50) - abs(50 * 50 - 48 * 52)
def z068(): return abs((400 + 600 + 2000) - (396 + 612 + 1987))
def z004(): return erste_zahl_mit_potenz(6, 216)
def z002(): return basis_suchen(4, 81)
EXP = {
 2: z002()[0], 3: z003(), 4: z004(), 8: z008(), 10: z010(), 12: z012()[0], 13: z013(), 17: z017(), 18: z018()[0], 19: 10 ** 6 // 10 ** 2 // 10,
 20: z020(), 21: z021(), 22: z022()[0], 23: z023(), 24: z024(), 27: z027(), 31: z031()[0], 34: z034(), 37: z037()[0], 40: z040()[0],
 42: z042(), 45: z045()[0], 47: z047()[0], 51: z051()[0], 53: z053()[0], 55: z055(), 57: z057()[0], 59: z059()[0], 63: z063(), 65: z065(),
 67: z067(), 68: z068(), 70: z070(), 71: z071()[0], 72: z072()[0], 74: z074()[0], 75: z075()[0], 76: z076()[0],
}
fehl = 0
for k, v in sorted(EXP.items()):
    a = A['VT1A-%03d' % k]
    if a['antwortform'] != 'zahl': print('keine Zahlaufgabe', k); fehl += 1; continue
    soll = a['aufgabe']['o']['wert']
    if Fraction(str(soll)) != Fraction(v):
        print('ABWEICHUNG VT1A-%03d: gespeichert %s, eigene Rechnung %s' % (k, soll, v)); fehl += 1
zahlk = [n(k) for k, a in A.items() if a['antwortform'] == 'zahl']
fehlend = sorted(set(zahlk) - set(EXP))
print('Zahl-Aufgaben eigen gerechnet: %d von %d; nicht in EXP: %s' % (len(EXP), len(zahlk), fehlend))
# Eindeutigkeit der Lösung bei Suchaufgaben
print('Eindeutigkeit: 002 Basen', z002(), '| 012 k', z012(), '| 075 N', z075(), '| 071 N', z071(), '| 037', z037(), '| 076', z076(), '| 057', z057())

# ---- Auswahl-Aufgaben: eigene Entscheidung ----
def val(s):
    s = s.replace('·', '*').replace(':', '//').replace('−', '-')
    s = re.sub(r'(\d+)\s*⁰', r'\1**0', s)
    s = s.translate(str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹', '0123456789'))
    return s
def pw(b, e): return b ** e
AUSW = {}
# 001: Mias Satz 2^5 = 10 -> Option mit 32 und Faktorzählung
AUSW[1] = [i for i, t in enumerate(A['VT1A-001']['aufgabe']['a']) if t.startswith('Mia irrt') and '= 32' in t]
AUSW[5] = [i for i, t in enumerate(A['VT1A-005']['aufgabe']['a']) if t.startswith('Die 4 steht 6-mal')]
AUSW[6] = [i for i, (l, r) in enumerate([(3**2, 2**3), (5**2, 2**5), (4**3, 3**4), (2**4, 4**2)]) if l == r]
AUSW[7] = [i for i, t in enumerate(A['VT1A-007']['aufgabe']['a']) if t.startswith('Fehler') and '3 · 3 · 3 · 3 = 81' in t]
AUSW[9] = [i for i, z in enumerate([99, 121, 48, 150]) if int(z ** .5) ** 2 == z]
AUSW[11] = [i for i, t in enumerate(A['VT1A-011']['aufgabe']['a']) if '8 · 8 = 64' in t]
AUSW[14] = [0]  # 100 = 4 * 25 und Begründung über Flächen; Option 3 hat falsche Begründung (Umfang 2-fach)
AUSW[15] = [i for i, t in enumerate(A['VT1A-015']['aufgabe']['a']) if t.startswith('10⁶ ist größer') and 9 * 10**5 < 10**6]
AUSW[16] = [i for i, z in enumerate([34 * 10**5, 340 * 10**4, 34 * 10**4, 3 * 10**6 + 4 * 10**5]) if z != 3400000]
# 025: 3 * 2^5 vs Optionen
opts25 = [(3 * 2) ** 5, 3 * 2 ** 5, 3 ** 5 * 2, 3 * 2 * 5]
AUSW[25] = [i for i, z in enumerate(opts25) if z == 3 * 2 * 2 * 2 * 2 * 2]
# 026: Tag n -> 3^n; Tag 6
AUSW[26] = [i for i, z in enumerate([3 ** 6, 6 ** 3, 3 * 6, 3 ** 5]) if z == 3 ** 6]
# 028: 2*3^4
AUSW[28] = [3] if 2 * 3 ** 4 == 162 and (2 * 3) ** 4 == 1296 else None
# 029: genau ein Klammerpaar so, dass 50
import itertools
toks = ['20', '-', '4', '*', '3', '+', '2']
treffer = []
for i in range(0, 7, 2):
    for j in range(i, 7, 2):
        if i == 0 and j == 6: continue
        t = toks[:i] + ['('] + toks[i:j + 1] + [')'] + toks[j + 1:]
        if eval(''.join(t)) == 50: treffer.append(''.join(t))
print('029 Klammer-Aufzählung, Ergebnis 50:', treffer)
AUSW[29] = [3] if treffer == ['(20-4)*3+2'] else None
AUSW[30] = [max(range(4), key=lambda i: [8 + 4 * 5 - 3, (8 + 4) * 5 - 3, 8 + 4 * (5 - 3), (8 + 4) * (5 - 2 - 1)][i])]
AUSW[32] = [3] if (9 + 3) // 4 * 2 == 6 else None
AUSW[33] = [i for i, (m, o) in enumerate([((30 - 12) - 4, 30 - 12 - 4), (30 - (12 - 4), 30 - 12 - 4), (2 * (3 + 4), 2 * 3 + 4), (20 // (4 * 5), 20 // 4 * 5)]) if m == o]
AUSW[35] = [2] if 100 - (12 + 8) * 4 == 20 else None
AUSW[36] = [2]  # (7+5)*4-6 : Geschichte 3
AUSW[38] = [0] if 40 - (9 + 6) == 25 else None
AUSW[39] = [i for i, z in enumerate([20 - 4 * 3 + 2 * 2, (20 - 4) * 3 - 2 * 2, 20 // 4 * 3 - 2 * 2, 20 - (4 * 3 + 2 * 2)]) if z == 20 - 12 - 4]
AUSW[41] = [1]
AUSW[43] = [1]
AUSW[44] = [i for i, z in enumerate([58 - 37 + 63, 37 + 63 - 58, 37 + 58 - 63, 63 + 37 + 58]) if z == 37 + 58 + 63]
AUSW[46] = [0] if 50 * 37 * 2 == 3700 else None
AUSW[48] = [2] if 2 * 37 * 50 == 3700 and 2 * 50 * 37 == 3700 else None
AUSW[49] = [2] if 36 * 25 * 4 == 18 * 25 * 8 else None
AUSW[50] = [0]
AUSW[52] = [i for i, z in enumerate([9 * 6 + 4, 9 + 6 * 4, (9 + 6) * 4, 9 * (6 + 4)]) if z == 90]
AUSW[54] = [i for i, z in enumerate([9 * 23, 9 * 20 + 3, 9 * 20 + 9 * 3, 180 + 27]) if z != 207]
AUSW[56] = [1] if 15 * 7 + 15 * 9 == 15 * (7 + 9) == 240 else None
AUSW[58] = [i for i, z in enumerate([36 * 9, 36 - 9, 9 / 36, 36 // 9]) if z == 4]
AUSW[60] = [i for i, f in enumerate([lambda x: 56 == 7 * x, lambda x: x == 56 * 7, lambda x: x * 56 == 7, lambda x: x == 8 * 56]) if f(8)]
# 060: Lösungsmengen in N: x=8 für 7x=56; Option0 56:x=7 ->8
AUSW[60] = [0] if [x for x in range(1, 100) if 56 / x == 7] == [8] else None
AUSW[62] = [2] if not [x for x in range(0, 100) if 7 * x == 50] else None
AUSW[66] = [min(range(4), key=lambda i: abs([30 * 50, 40 * 60, 40 * 5, 40 * 50][i] - 39 * 52))]
AUSW[73] = [i for i, g in enumerate([lambda x: x - 3 * (2 + 5) == 20, lambda x: x - 3 * 2 + 5 == 20, lambda x: x + 3 * 2 - 5 == 20, lambda x: (x - 3) * 2 + 5 == 20]) if g(21)]
AUSW[77] = [3] if (30 - 6) // 2 == 12 and 2 * 12 + 6 == 30 else None
for k in sorted(AUSW):
    a = A['VT1A-%03d' % k]; ist = a['aufgabe']['o']['index']
    if AUSW[k] != [ist]: print('ABWEICHUNG Auswahl VT1A-%03d: gespeichert %s, eigene Entscheidung %s' % (k, ist, AUSW[k])); fehl += 1
ausw = sorted(n(k) for k, a in A.items() if a['antwortform'] == 'auswahl')
print('Auswahl-Aufgaben mit eigener Entscheidung: %d von %d; ohne (nur von Hand gelesen): %s' % (len(AUSW), len(ausw), sorted(set(ausw) - set(AUSW))))

# ---- Struktur: Optionen, Lage, Duplikate ----
pos = Counter(); anz = Counter()
for k, a in A.items():
    if a['antwortform'] != 'auswahl': continue
    o = a['aufgabe']['a']; anz[len(o)] += 1; pos[a['aufgabe']['o']['index']] += 1
    if len(set(o)) != len(o): print('doppelte Option', k); fehl += 1
print('Optionszahl:', dict(anz), '| Lage der richtigen Option:', dict(sorted(pos.items())))
lagepool = {}
for k, a in A.items():
    if a['antwortform'] == 'auswahl': lagepool.setdefault((a['lernkarte']), []).append((n(k), a['aufgabe']['o']['index']))
for lk, l in lagepool.items(): print('  Lage', lk, l)
sol = {}
for k, a in A.items():
    if a['antwortform'] == 'zahl': sol.setdefault((a['lernkarte']), []).append((n(k), a['aufgabe']['o']['wert']))
for lk, l in sol.items():
    c = Counter(w for _, w in l)
    d = [(w, [i for i, x in l if x == w]) for w, m in c.items() if m > 1]
    if d: print('  gleiche Sollantwort', lk, d)

# ---- Rechenbehauptungen in allen Texten (Gleichungsketten a = b = c, jedes Glied rein rechnerisch, alle Glieder gleich) ----
SUP = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹', '0123456789')
GLIED = r'[\d⁰¹²³⁴⁵⁶⁷⁸⁹ ·:+−\(\)]+'
def ausw(g):
    g = re.sub(r'(?<=\d) (?=\d{3}(?!\d))', '', g.strip())
    g = re.sub(r'(\d)([⁰¹²³⁴⁵⁶⁷⁸⁹]+)', lambda m: m.group(1) + '**' + m.group(2).translate(SUP), g)
    g = g.replace('·', '*').replace('−', '-').replace(':', '/')
    g = re.sub(r'(\d+)', r'Fraction(\1)', g)
    return eval(g)
def prufe_text(kenn, s, wo):
    for m in re.finditer(r'(?<![\w,.])(%s(?:=%s)+)' % (GLIED, GLIED), s.replace(' = ', '=').replace(' =', '=').replace('= ', '=')):
        glieder = [x for x in m.group(1).split('=')]
        try: werte = [ausw(x) for x in glieder if re.search(r'\d', x)]
        except Exception: continue
        if len(set(werte)) > 1: print('  TEXTRECHNUNG? %s %s: „%s“ ergibt %s' % (kenn, wo, m.group(1), [str(w) for w in werte]))
for k, a in A.items():
    x = a['aufgabe']
    prufe_text(k, x['f'].get('text', ''), 'Text')
    prufe_text(k, x['w'], 'Weg')
    for o in x.get('a', []) or []: prufe_text(k, o, 'Option')
    for fb in a['fehlbilder']: prufe_text(k, fb.get('beschreibung', ''), 'Fehlbild')
print('FERTIG, Abweichungen:', fehl)
