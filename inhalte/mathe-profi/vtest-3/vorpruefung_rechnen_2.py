#!/usr/bin/env python3
"""Vorprüfung VT3, Runde 2: unabhängige Gegenrechnung des NEUEN Standes (alle 126 Aufgaben).
Aufruf im Wurzelordner: python3 -I inhalte/mathe-profi/vtest-3/vorpruefung_rechnen_2.py
Liest nur die Aufgabendateien, verändert nichts. Benutzt NICHT die `loesung_rechnung` des Autors, sondern eigene
Formeln, exakte Brüche und Aufzählungen. Teil 1: Lösungen (Zahl/Lücken), Teil 2: Wahrheit jeder Auswahl-Option,
Teil 3: Fehlbilder (Wert der Rechnung = Antwort, Antwort ≠ richtig, Lücke gültig), Teil 4: Auswahl-Statistik."""
import json, os, re, itertools, collections
from fractions import Fraction as F

HIER = os.path.dirname(os.path.abspath(__file__))
T = {}
for u in ['messen.volumen', 'daten.darstellen', 'daten.kennwerte', 'funktionen.grundbegriffe', 'geometrie.winkel']:
    for a in json.load(open(os.path.join(HIER, u + '.json')))['aufgaben']:
        a['_u'] = u
        T[a['kennung']] = a
fehler = []; n_pruef = 0

def soll(k):
    o = T[k]['aufgabe']['o']
    if 'wert' in o: return F(str(o['wert']))
    if 'werte' in o: return [F(str(v)) for v in o['werte']]
    return o['index']

def pruef(k, erw):
    global n_pruef; n_pruef += 1
    e = [F(str(x)) for x in erw] if isinstance(erw, list) else F(str(erw))
    if soll(k) != e: fehler.append((k, soll(k), e))

def auswahl(k, wahr):
    """wahr: Liste von Wahrheitswerten je Option; genau eine muss wahr sein und dem gespeicherten Index entsprechen."""
    global n_pruef; n_pruef += 1
    n = len(T[k]['aufgabe']['a'])
    if len(wahr) != n or sum(bool(w) for w in wahr) != 1 or wahr.index(True) != T[k]['aufgabe']['o']['index']:
        fehler.append((k, 'auswahl', wahr, T[k]['aufgabe']['o']['index']))

def winkel(h, m):
    d = abs((30 * (h % 12) + F(m, 2)) - 6 * m) % 360
    return min(d, 360 - d)

# ---------- Teil 1: Zahl- und Lückenaufgaben ----------
pruef('VT3-001', (F(3, 2) * F(4, 5) * 2 - 1) * 100)
pruef('VT3-003', (6 // 2) ** 3)
pruef('VT3-004', [3, 6 * 4 * 3])
b = next(b for b in range(1, 99) if 2 * b * b * F(b, 2) == 216); pruef('VT3-006', [b, F(b, 2)])
pruef('VT3-008', F(150 ** 3, 1000))
pruef('VT3-010', [2, F(50 * 30 * 40, 1000)])
k = next(k for k in range(1, 99) if k ** 3 == 64); pruef('VT3-011', k * 10)
pruef('VT3-014', F(150 * 120 * 100, 1000) / 9)
b = next(b for b in range(1, 99) if 10 * b * 3 * b == 270); pruef('VT3-015', b)
pruef('VT3-016', [3, F(308, 7 * 4)])
pruef('VT3-019', F(800 * 500) * F(1, 2) / 1000)
A = F(240 - 180, 3); pruef('VT3-020', [A, 180 / A])
pruef('VT3-021', F(192, 6 * 4))
pruef('VT3-022', (F(3) / F(24, 10) - 1) * 100)
pruef('VT3-024', [2, 4 * 3 * F(5, 2)])
pruef('VT3-025', F(1000 - 4 * 100, 1000) * 100)
pruef('VT3-027', (50 // 15) * (40 // 15) * (30 // 15))
pruef('VT3-029', F(25 * 100, 100) - 10)
pruef('VT3-031', [2, F(40, 250) * 100])
pruef('VT3-032', F(36) / F(15, 100))
pruef('VT3-035', F(6, 24 + 6) * 100)
pruef('VT3-036', 6 * 2 - 4 * 2)
pruef('VT3-037', [3, (F(9, 2) - 3) * 8])
pruef('VT3-038', 3 * F(20, 7 - 3))
pruef('VT3-042', [(3 + F(9, 2) + F(5, 2)) * 20, F(9, 2) / 10 * 100])
pruef('VT3-043', F(5040 - 4800, 4800) * 100)
pruef('VT3-044', F(80, 20))
pruef('VT3-046', [2, F(30 - 20, 20) * 100])
pruef('VT3-047', 3 ** 2)
for z in ([8] * 5, [6, 7, 8, 9, 10], [1, 2, 8, 14, 15]):      # Mittelwert 8, Probe mit Beispielzahlen
    assert F(sum(2 * x - 3 for x in z), 5) == 13
pruef('VT3-050', 2 * 8 - 3)
pruef('VT3-052', [3, F(12, 4)])
pruef('VT3-053', F(10 * 8 + 20 * 8, 30))
n0 = next(n for n in range(0, 99, 2) if sum(n + 2 * i for i in range(5)) == 100); pruef('VT3-055', n0 + 8)
pruef('VT3-057', F(6 * 12 - 4 * 10, 2))
pruef('VT3-058', 20 - (5 * 14 - 5 * 12))
pruef('VT3-059', [2, 5 * 48 - 4 * 50])
pruef('VT3-061', F(sum([98, 101, 103, 99, 104]), 5))
pruef('VT3-062', F(30 * 40 - 10 * 10, 20))
pruef('VT3-063', F(5 * 70 - 65 - 78, 3))
pruef('VT3-067', [3, len({x * x - 4 for x in range(-2, 3)})])
pruef('VT3-069', [0, F(6, 2)])
pruef('VT3-070', len({x for x in range(2, 11, 2)} & {x - 2 for x in range(2, 11, 2)}))
pruef('VT3-071', next(x for x in range(-50, 51) if x * x - 6 * x == -8 and x != 4))
pruef('VT3-072', F(8 - (-2), 2))
pruef('VT3-073', [2, F(15 - 6, 3)])
a_ = next(x for x in range(-50, 51) if x != 1 and F(20, x - 1) == 4); b_ = next(x for x in range(-50, 51) if x != 1 and F(20, x - 1) == -5)
pruef('VT3-075', [a_, b_])
pruef('VT3-077', F(17 - 5, F(6, 5)))
m = F(1 - 5, 3 - 1); pruef('VT3-079', 5 - m * 1)
pruef('VT3-080', [3, 4])
pruef('VT3-083', 5 - F(1, 2) * 6)
pruef('VT3-085', (lambda bb: bb * 9 - 5)(F(7 + 5, 4)))
pruef('VT3-087', [3, 3 ** 2 - 1])
c = 3 * 4 - 2; pruef('VT3-089', c - 2 * 4)
pruef('VT3-091', [F(47 - 12, 5), 12 + 5 * 3])
pruef('VT3-094', [2, 8 + F(1, 10) * 50])
pruef('VT3-098', next(x for x in range(1, 999) if 60 + F(3, 2) * x < 4 * x))
pruef('VT3-100', 180 - 50 - 70)
pruef('VT3-101', [2, 48])
pruef('VT3-102', [360 - 310, 180 - (360 - 310)])
pruef('VT3-104', 90 - 35)
pruef('VT3-106', next(h for h in range(1, 13) if h != 7 and winkel(h, 0) == 150)); assert [h for h in range(1, 13) if winkel(h, 0) == 150] == [5, 7]
pruef('VT3-107', F(180, 12))
pruef('VT3-108', [2, winkel(4, 30)])
pruef('VT3-112', winkel(3, 15))                              # 15:00 richtig = 3 Stunden * 5 min Vorgang = 3:15 angezeigt
pruef('VT3-113', [3, next(x for x in range(1, 90) if x + (x + 10) + (x + 20) == 90)])
pruef('VT3-115', F(360, 20) // 2)
pruef('VT3-117', F(90, 18) - 1)
au = next(x for x in range(1, 90) if 2 * x + 20 == 90); pruef('VT3-119', [au, au + 20])
pruef('VT3-122', next(a for a in range(1, 90) if (180 - a) - (180 - 2 * a) == 30))
pruef('VT3-123', [1, 180 - 65])
pruef('VT3-124', [900 // 360, 900 % 360])
x_ = next(x for x in range(1, 210) if x + (x + 30) == 210); pruef('VT3-126', [x_, x_ + 30])

# ---------- Teil 2: Wahrheit jeder Auswahl-Option ----------
auswahl('VT3-002', [F(1, 2) ** 3 == F(1, 2), F(1, 2) ** 3 == F(1, 8), F(1, 2) ** 3 == F(1, 4), F(1, 2) ** 3 == F(1, 6)])
auswahl('VT3-005', [20 * 3 * 5 == 300, False, False, False])        # 2 m = 20 dm, 30 cm = 3 dm, 5 dm; nur Option 0 rechnet alle Kanten in dm
auswahl('VT3-007', [4 * 4 * 4 == 3 * 4 * 5, 5 > 4 and 3 * 4 * 5 > 64, False, 4 ** 3 > 3 * 4 * 5]); assert 12 * 4 == 4 * (3 + 4 + 5) == 48
auswahl('VT3-009', [False, False, 100 ** 3 == 10 ** 6 and 10 ** 6 // 1000 == 1000, False])
auswahl('VT3-012', [40 * 20 * 10 > 20 ** 3, 40 * 20 * 10 == 20 ** 3 == 8000, 20 ** 3 > 40 * 20 * 10, False])
auswahl('VT3-013', [x != F(5, 2) for x in (F(1, 4) * 1000, F(2500, 1000), F(5, 2), F(2500, 1000))])  # 0,25 m³ = 250 l; die anderen drei sind 2,5 l; gefragt ist die, die NICHT passt
auswahl('VT3-017', [F(1200, 20) * 5 == 60, False, False, F(1200, 20 * 5) == 12])
auswahl('VT3-018', [F(120, 40) > F(120, 24), F(120, 24) == F(120, 40), F(120, 24) > F(120, 40), False])
auswahl('VT3-023', [False, True, False, False])                     # Zuwachs = 2 · L · B
auswahl('VT3-026', [10 * 4 * 6 == 10 * 6 * 4, 10 * 4 * 6 > 10 * 6 * 4, 10 * 6 * 4 > 10 * 4 * 6, False])
auswahl('VT3-028', [F(3, 2) ** 2 - 1 == F(1, 2), F(3, 2) ** 2 - 1 == 1, F(3, 2) ** 2 - 1 == F(9, 4), (F(3, 2) ** 2 - 1) * 100 == 125])
auswahl('VT3-030', [F(18, 24) == F(18, 100), F(18, 24) == F(4, 3), F(18, 24) == F(75, 100), F(18, 24) == F(24, 100)])
auswahl('VT3-033', [F(9, 30) > F(8, 25), F(8, 25) * 100 == 32 and F(9, 30) * 100 == 30, False, F(8, 25) == F(9, 30)])
auswahl('VT3-034', [True, False, False, False])                     # nur 0 ≤ h ≤ 1 gilt immer; (b) 20 von 120 ist ein möglicher Wert, nicht Pflicht; (c) 0 Sechsen möglich; (d) beliebig
auswahl('VT3-039', [False, False, False, F(6, 3) == 2])
auswahl('VT3-040', [[F(w, 6) for w in (18, 12, 6, 24)] == list(h) for h in ([6, 4, 2, 8], [4, 2, 1, 3], [3, 2, 1, 4], [18, 12, 6, 24])])  # Höhe = Kinder : 6 (1 cm = 6 Kinder)
auswahl('VT3-041', [False, 4 * 8 > 6 * 5 and 4 * 8 == 32 and 6 * 5 == 30, False, False])
auswahl('VT3-045', [220 - 200 > 6 - 4, False, False, False])
auswahl('VT3-048', [False, False, False, True])
auswahl('VT3-049', [False, False, F(60 - 40, 40) == F(1, 2), False])
auswahl('VT3-051', [False, F(8, 4) == 2, False, False])
a = [3, 5, 7, 9]
auswahl('VT3-054', [F(sum(a + [6]), 5) == 6, F(sum(a[1:]), 3) == 6, F(sum([4, 5, 7, 7]), 4) == 6, F(sum(a + [5, 8]), 6) == 6])
auswahl('VT3-056', [False, False, F(60 + 50, 6) < 10, F(110, 6) > 12 and round(float(F(110, 6))) == 18])
# 060 Modell: Mittelwert 10 für vier ganze Zahlen 0..20 durchsuchen
vier = [z for z in itertools.product(range(0, 21), repeat=4) if sum(z) == 40]
o0 = all(max(z) > 10 for z in vier); o1 = all(10 in z for z in vier); o2 = all(max(z) >= 10 for z in vier); o3 = all(sum(1 for x in z if x < 10) <= 2 for z in vier)
auswahl('VT3-060', [o0, o1, o2, o3])
# 064: Wertemenge hat höchstens 12 Elemente; Gegenbeispiele für die anderen
auswahl('VT3-064', [False, True, False, False])
auswahl('VT3-065', [(0 ** 2 - 9) == -9, any(x * x - 9 == -10 for x in range(-20, 21)), not (0 ** 2 - 9 == -9), not (3 * 3 - 9 == 0)])
auswahl('VT3-066', [{3 * x - 2 for x in (-5, 1, 7)} == {-5, 1, 7}, {3 * x - 2 for x in (-17, 1, 19)} == {-5, 1, 7}, {3 * x - 2 for x in (-9, 9, 27)} == {-5, 1, 7}, {3 * x - 2 for x in (-1, 1, 3)} == {-5, 1, 7}])
auswahl('VT3-068', [False, False, True, False])
auswahl('VT3-074', [False, True, False, False])                      # 12 + 1,5 t = 30
auswahl('VT3-076', [not any(-2 * x * x == 8 for x in range(-30, 31)), -2 * 2 ** 2 == 8, -2 * 2 ** 2 == 8 and -2 * (-2) ** 2 == 8, -2 * (-4) ** 2 == 8])
auswahl('VT3-078', [all(f(x) == y for x, y in ((0, -3), (2, 1))) for f in (lambda x: -3 * x + 2, lambda x: F(1, 2) * x - 3, lambda x: 2 * x + 1, lambda x: 2 * x - 3)])
auswahl('VT3-081', [False, False, True, False])
auswahl('VT3-082', [False, [3 - 1, 9 - 3, 27 - 9] != [2, 2, 2], False, False])
auswahl('VT3-084', [-3 < 0, False, False, False])
auswahl('VT3-086', [False, False, False, 3 - 2 * 4 == -5])
# 088: Stichproben über Brüche
S = [F(p, q) for p in range(-24, 25) for q in (1, 2, 4)]
o0 = all(F(2 * a + 1).denominator == 1 for a in S if F(2 * a + 1).denominator == 1 and a.denominator == 1)  # (b ganz ⇒ a ganz) falsch? siehe unten
o0 = all(a.denominator == 1 for a in S if (2 * a + 1).denominator == 1)
o1 = all(2 * a + 1 < 0 for a in S if a < 0); o2 = all((2 * a + 1).denominator == 1 for a in S if a.denominator == 1); o3 = all(2 * a + 1 < a for a in S if a > 0)
auswahl('VT3-088', [o0, o1, o2, o3])
auswahl('VT3-090', [False, all(a * 0 == 0 for a in range(-9, 10)), False, False])
auswahl('VT3-092', [120 - 15 * 8 == 0, 120 - 15 * 15 >= 0, 15 - 120 * 0 == 120, 120 + 15 * 0 == 120 and 120 + 15 * 8 <= 120])  # Term 0: leer nach 8 h; 1: bei t=15 negativ; 2: I(0)=15 statt 120; 3: wächst
auswahl('VT3-093', [3 + 2 * 8 == 2 * (3 + 2 * 4), (3 + 2 * 8) - (3 + 2 * 4) == 4, 3 + 2 * 8 > 2 * (3 + 2 * 4), 3 + 2 * 8 < 2 * (3 + 2 * 4)])
auswahl('VT3-095', [4 * 2 == 4 + 3, 3 * 2 == 4 + 3, 4 + 3 == 7 and 4 * 2 == 8 and all(4 + 3 * (n - 1) == 3 * n + 1 for n in range(1, 9)), 4 + 3 * 1 == 4])
auswahl('VT3-096', [12 + 6 == 6 + 6, True, False, False])
auswahl('VT3-097', [True, 40 - 8 * 8 == 0, False, False])
auswahl('VT3-099', [False, False, False, True])
auswahl('VT3-103', [False, False, True, False])
auswahl('VT3-105', [False, True, False, False])
# 099/103/105 Modell: Winkelfolgen an zwei Geraden (α, 180−α, α, 180−α) – 105: welche Folge kann vorkommen
def kreuz(al): return (al, 180 - al, al, 180 - al)
auswahl('VT3-105', [(72, 108, 108, 72) == kreuz(72), (72, 108, 72, 108) == kreuz(72), (72, 72, 108, 108) == kreuz(72), (72, 108, 72, 98) == kreuz(72)])
# 103: alle Optionen über Raster α = 1..179
W = [kreuz(a) for a in range(1, 180)]
auswahl('VT3-103', [all(w[0] + w[2] == 180 for w in W), all(min(w) < 90 for w in W), all(w[0] == w[2] for w in W), all(w[0] != w[1] for w in W)])
auswahl('VT3-109', [winkel(9, 0) == 90 and winkel(3, 0) == 90 and winkel(9, 15) != 90, False, False, False])
w = [winkel(h, 0) for h in range(1, 13)]
auswahl('VT3-110', [all(x > 90 for x in w), all(sum(1 for y in w if y == x) == 2 for x in w), all(x < 180 for x in w), all(x % 30 == 0 and x <= 180 for x in w)])
vals = [winkel(3, 0), winkel(6, 0), winkel(1, 5), winkel(12, 15)]
auswahl('VT3-111', [vals.index(min(vals)) == i for i in range(4)])
auswahl('VT3-114', [False, 1 + 3 == 4 and F(90, 4) == F(45, 2), False, False])
auswahl('VT3-116', [F(180, 4) > F(90, 3), F(90, 3) > F(180, 4), F(90, 3) == F(180, 4), False])
# 118: Zerlegungen (a,b,c) ganzzahlig, a+b+c = 90, alle > 0
Z = [(a, b, 90 - a - b) for a in range(1, 89) for b in range(1, 90 - a)]
auswahl('VT3-118', [all(min(z) >= 20 for z in Z), all(max(z) > 30 for z in Z), all(len(set(z)) == 3 for z in Z), all(min(z) <= 30 for z in Z)])
# 120: spitz (0,90) + stumpf (90,180), Summe in ganzen Grad
P = [(s, t) for s in range(1, 90) for t in range(91, 180)]
auswahl('VT3-120', [all(s + t == 180 for s, t in P), all(90 < s + t < 180 for s, t in P), all(s + t > 90 for s, t in P), all(s + t < 180 for s, t in P)])
auswahl('VT3-121', [False, 180 - 62 == 118 and 90 < 118 < 180, False, False])
auswahl('VT3-125', [60 > 40, False, False, False])

# ---------- Teil 3: Fehlbilder ----------
def rechne(s):
    t = s.replace('·', '*').replace(':', '/').replace('−', '-').replace('²', '**2').replace(',', '.').replace(' ', '')
    t = re.sub(r'(\d+(?:\.\d+)?)', r'F("\1")', t)
    if re.search(r'[A-Za-z]', re.sub(r'F\(', '', t)): return None
    return eval(t, {'F': F})

fb_zahl = fb_geprueft = 0
for kn, a in sorted(T.items()):
    o = a['aufgabe']['o']; y = a['aufgabe']['y']
    for f in a['fehlbilder']:
        fb_geprueft += 1
        if y == 'auswahl':
            if f['index'] == o['index'] or f['antwort'] != a['aufgabe']['a'][f['index']]: fehler.append((kn, 'FB-Index', f))
        else:
            n = len(o.get('werte', [0]))
            if y == 'luecken' and not 1 <= f['luecke'] <= n: fehler.append((kn, 'FB-Luecke', f))
            richtig = F(str(o['wert'])) if 'wert' in o else F(str(o['werte'][f['luecke'] - 1]))
            if F(str(f['antwort'])) == richtig: fehler.append((kn, 'FB gleich richtig', f))
            r = rechne(f['rechnung']) if f.get('rechnung') else None
            if r is not None:
                fb_zahl += 1
                if r != F(str(f['antwort'])): fehler.append((kn, 'FB-Rechnung', f['rechnung'], r, f['antwort']))

# ---------- Teil 4: Auswahl-Statistik ----------
aus = [T[k] for k in sorted(T) if T[k]['aufgabe']['y'] == 'auswahl']
platz = collections.Counter(a['aufgabe']['o']['index'] for a in aus)
laenge = collections.Counter()
for a in aus:
    L = [len(x) for x in a['aufgabe']['a']]; i = a['aufgabe']['o']['index']
    laenge[sorted(L, reverse=True).index(L[i]) + 1] += 1
folge = ''.join(str(a['aufgabe']['o']['index']) for a in aus)
print(f'{n_pruef} Prüfungen (Lösungen und Auswahl), {len(fehler)} Abweichungen')
for f in fehler: print('  ABWEICHUNG', f)
print(f'Fehlbilder: {fb_geprueft} geprüft, bei {fb_zahl} Rechnung ausgewertet')
print('Auswahl-Aufgaben:', len(aus), '| Platz', sorted(platz.items()), '| Rang der richtigen Option nach Länge (1 = längste)', sorted(laenge.items()))
print('Platzfolge in Kennungsreihenfolge:', folge)
print('Differenz zum Vorgänger (mod 4):', collections.Counter((int(folge[i]) - int(folge[i - 1])) % 4 for i in range(1, len(folge))))
