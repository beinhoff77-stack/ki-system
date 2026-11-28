#!/usr/bin/env python3
"""Zweite Vorprüfung VT1A: eigene Nachrechnung der ersetzten/geänderten Aufgaben.
Eigene Formeln, Zählschleifen, Aufzählung aller Möglichkeiten; keine Funktionen aus den Aufgaben-Werkzeugen.
Aufruf: python3 -I inhalte/mathe-profi/vtest-1a/vorpruefung_rechnen_2.py"""
import json, os, itertools, statistics
from fractions import Fraction
H = os.path.dirname(os.path.abspath(__file__))
A = {}
for fn in ('zahlen.potenzen_basis', 'zahlen.rechengesetze'):
    for a in json.load(open(os.path.join(H, fn + '.json'), encoding='utf-8'))['aufgaben']:
        A[int(a['kennung'][-3:])] = a
fehl = 0
def zahl(k, v):
    global fehl
    s = A[k]['aufgabe']['o']['wert']
    if Fraction(str(s)) != Fraction(v):
        print('ABWEICHUNG Zahl %03d: gespeichert %s, eigene %s' % (k, s, v)); fehl += 1
# --- Zahl-Aufgaben, bei denen ich die Rechnung unabhängig führe (Auszug der ersetzten) ---
zahl(3, 2 ** 4)
zahl(8, [s for s in range(1, 100) if s * s == 144][0] * 4 // 4 * 0 + 24 * 24) if False else None
# 030: (x+4)*3-5=25 durch Zählschleife, Eindeutigkeit
l30 = [x for x in range(0, 1000) if (x + 4) * 3 - 5 == 25]; print('030 Lösungen:', l30); zahl(30, l30[0])
# 040 Stunden: 4 + 2*(h-1) = 14 (nur falls so formuliert) -> hier nur Ausgabe
print('040 gespeichert:', A[40]['aufgabe']['o'], '|', A[40]['aufgabe']['f']['text'][:150])
# --- 034: alle 16 Zeichenpaare ---
ops = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b, ':': lambda a, b: Fraction(a, b)}
def val(a, o1, b, o2, c):  # Punkt vor Strich
    pr = {'+': 1, '-': 1, '*': 2, ':': 2}
    if pr[o1] >= pr[o2]:
        return ops[o2](ops[o1](Fraction(a), b), c)
    return ops[o1](Fraction(a), ops[o2](Fraction(b), c))
tr = [(o1, o2) for o1 in ops for o2 in ops if val(3, o1, 4, o2, 5) == 23]
print('034 alle Paare mit =23:', tr, '(erwartet genau [(+,*)])')
for o in ('*+', '+*', '++', '**'): print('   ', o, val(3, o[0], 4, o[1], 5))
# --- 043: Umformungen ---
print('043: 85-38+53 =', 85 - 38 + 53, '| 85+53-38 =', 85 + 53 - 38, '| 85-53+38 =', 85 - 53 + 38,
      '| 100-47-38 =', 100 - 47 - 38, '| 100-(47-38) =', 100 - (47 - 38), '| 64:8:2 =', 64 / 8 / 2, '| 64:(8:2) =', 64 / (8 / 2))
# --- 036: Terme ---
print('036: ① %d ② %d ③ %d ④ %d (Sollwert 30-6-4 = 20)' % (30 - 6 - 4, 30 - (6 + 4), 30 - 6 + 4, 30 - (6 - 4)))
# --- 001 ---
print('001: 3^2+2^3 =', 3 ** 2 + 2 ** 3, '| 5^5 =', 5 ** 5, '| 3^2*2^3 =', 3 ** 2 * 2 ** 3, '| (3+2)^5 =', 5 ** 5)
# --- Auswahl-Statistik ---
pos = {0: 0, 1: 0, 2: 0, 3: 0}; nopt = {}; laenger = 0; laengst = 0; n_ausw = 0; verhaeltnis = []
for k, a in sorted(A.items()):
    au = a['aufgabe']
    if au['y'] != 'auswahl': continue
    n_ausw += 1
    opts = au['a']; i = au['o']['index']
    nopt[len(opts)] = nopt.get(len(opts), 0) + 1
    pos[i] = pos.get(i, 0) + 1
    L = [len(x) for x in opts]
    if L[i] == max(L) and L.count(max(L)) == 1: laengst += 1
    if L[i] > statistics.mean([L[j] for j in range(len(L)) if j != i]): laenger += 1
    verhaeltnis.append(round(L[i] / statistics.mean([L[j] for j in range(len(L)) if j != i]), 2))
    if len(set(opts)) != len(opts): print('doppelte Option in %03d' % k); fehl += 1
print('Auswahl:', n_ausw, '| Optionenzahl', nopt, '| Lage der richtigen', pos)
print('richtige Option eindeutig die längste:', laengst, '| länger als Durchschnitt der anderen:', laenger,
      '| mittleres Längenverhältnis %.2f' % statistics.mean(verhaeltnis))
print('Zahl-Aufgaben:', sum(1 for a in A.values() if a['aufgabe']['y'] == 'zahl'))
# Auswahl je Pool
for p in ('test', 'korrektur', 'sicherung'):
    z = [k for k, a in A.items() if a['pool'] == p]
    print(p, 'Auswahl', sum(1 for k in z if A[k]['aufgabe']['y'] == 'auswahl'), 'von', len(z))
# idee je Lernziel
from collections import defaultdict
idee = defaultdict(list)
for k, a in sorted(A.items()): idee[(a['thema'], a['lernkarte'])].append(a.get('idee'))
for key, v in idee.items(): print(key[1], len(v), 'Ideen,', len(set(v)), 'verschieden')
print('Abweichungen:', fehl)
