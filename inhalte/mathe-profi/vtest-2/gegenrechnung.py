"""Unabhängige Gegenrechnung aller Sollwerte von VT2-001 … VT2-133.
Jede Aufgabe wird hier mit einem anderen Weg als beim Bauen nachgerechnet (Bruchrechnung, Aufzählen, Einsetzen,
Zeichenketten-Prüfung). Auswahlaufgaben: genau eine Möglichkeit muss das hier berechnete Merkmal haben, und das muss die
gespeicherte richtige sein. Ausgabe am Ende: „<n> Abweichungen“."""
import glob, json, itertools, re
from fractions import Fraction as F
from pathlib import Path

HIER = Path(__file__).resolve().parent
T = {}
for f in sorted(HIER.glob('*.json')):
    for t in json.loads(f.read_text(encoding='utf-8'))['aufgaben']:
        T[t['kennung']] = t
abw = []
GEPRUEFT = set()


def soll(k):
    a = T[k]['aufgabe']
    o = a['o']
    return o['werte'] if 'werte' in o else o['wert']


def pruefe(k, erwartet):
    GEPRUEFT.add(k)
    ist = soll(k)
    if isinstance(erwartet, (list, tuple)):
        erwartet = list(erwartet); ok = len(ist) == len(erwartet) and all(F(x) == F(y) for x, y in zip(ist, erwartet))
    else:
        ok = F(ist) == F(erwartet)
    if not ok: abw.append(f'{k}: gespeichert {ist}, gegengerechnet {erwartet}')


def waehle(k, pred):
    """genau eine Möglichkeit erfüllt pred, und sie ist die gespeicherte richtige"""
    GEPRUEFT.add(k)
    a = T[k]['aufgabe']
    treffer = [i for i, m in enumerate(a['a']) if pred(m)]
    if treffer != [a['o']['index']]: abw.append(f'{k}: Treffer {treffer}, gespeichert {a["o"]["index"]}')


def zins(K, p, monate=12): return F(K) * F(str(p)) / 100 * F(monate, 12)


# ---- finanzen.zinsen -------------------------------------------------------------------------------
assert zins(2000, 7.5) - zins(2000, 1.5) == 120
waehle('VT2-003', lambda m: m.startswith('Ben hat 2 000 € auf dem Sparbuch') and zins(2000, 2) == 40)
pruefe('VT2-004', [3, zins(6000, 5) - zins(5000, 1)])
pruefe('VT2-006', F(2000) * F(6, 100) / F(2, 100))
waehle('VT2-008', lambda m: m.startswith('In Zeile 2') and F(36) * F(5, 2) == 90)
waehle('VT2-010', lambda m: all(F(a.replace(',', '.')) / 100 == F(b.replace(',', '.')) for a, b in
       re.findall(r'([\d,]+) % → ([\d,]+)', m)) and len(re.findall(r'%', m)) == 3)
waehle('VT2-011', lambda m: m.startswith('6 €') and zins(1200, 0.5) == 6)
assert zins(1800, 3.5) == 63
waehle('VT2-016', lambda m: m.startswith('Das Kapital von A ist doppelt so groß, denn'))
waehle('VT2-017', lambda m: m == '□ · 0,04 = 52')
pruefe('VT2-018', [2, F(63) / F(42, 1000)])
waehle('VT2-019', lambda m: m.startswith('Anna,') and F(90) / F(25, 1000) > F(90) / F(3, 100) * 1 and F(90) * 100 / F(5, 2) > F(90) * 100 / 3)
pruefe('VT2-020', F(54) / F(3, 100) / F(6, 10))
waehle('VT2-021', lambda m: m.startswith('p ist doppelt so groß wie q') and 1000 * 2 * 1 == 2000)
# Bank-Vergleich: Zinsen in € je 1 000 €
bank = {'A': zins(1000, 6, 4), 'B': zins(1000, 3, 9), 'C': zins(1000, 2, 12), 'D': zins(1000, 8, 3)}
waehle('VT2-026', lambda m: m == 'K · p : 100 · 5 : 12')
waehle('VT2-028', lambda m: m.startswith('Sie sind 3-mal so hoch') and F(9, 3) == 3)

# ---- geometrie.kreis -------------------------------------------------------------------------------
waehle('VT2-064', lambda m: m.startswith('MC = 5 cm') and F(10, 2) == 5)
# C(2|y), A(-2|0), B(6|0): rechter Winkel bei C  <=>  (A-C)·(B-C) = 0, y ganzzahlig probiert
pruefe('VT2-065', [y for y in range(1, 20) if (-2 - 2) * (6 - 2) + (0 - y) * (0 - y) == 0][0])
pruefe('VT2-067', [3, F(10, 2)])
assert [y for y in (2, 4, 6, 8) if (0 - 4) * (8 - 4) + y * y == 0] == [4]
pruefe('VT2-070', [40, 90 - 40, 180 - 2 * 40])
waehle('VT2-072', lambda m: m == 'r > 7 cm')
def pkt(r, d): return 2 if r > d else (1 if r == d else 0)
pruefe('VT2-076', [pkt(3, d) + pkt(7, d) for d in (3, 5, 7)])
# Umkreismittelpunkt: innen <=> alle Winkel < 90°, auf Seite <=> ein Winkel = 90°, außen <=> ein Winkel > 90°
def lage(w): return 1 if max(w) < 90 else (2 if max(w) == 90 else 3)
waehle('VT2-079', lambda m: m == 'Er ist der Schnittpunkt der Mittelsenkrechten, denn er muss von den drei Ecken gleich weit entfernt sein.')
for w in ((35, 75, 70), (30, 60, 90), (25, 40, 115)): assert sum(w) == 180
pruefe('VT2-080', [lage((35, 75, 70)), lage((30, 60, 90)), lage((25, 40, 115))])
waehle('VT2-084', lambda m: m.startswith('Sie fallen zusammen'))

# ---- terme.umformen --------------------------------------------------------------------------------
def ev(f, xs=(-3, -1, 0, 1, 2, 5, 7)): return [f(x) for x in xs]
pruefe('VT2-029', [3, 3 - 7])
assert ev(lambda x: 5*x*x + 3*x - 2*x*x - 7*x + 4) == ev(lambda x: 3*x*x - 4*x + 4)
pruefe('VT2-030', [k for k in range(-20, 21) if all(9*x*x + k*x - 4*x*x - 8*x == 5*x*x for x in (1, 2, 3))][0])
assert ev(lambda a: (3*a+2) + (5*a-1) + (a+4)) == ev(lambda a: 9*a + 5)
waehle('VT2-032', lambda m: m.startswith('In Zeile 3') and -4 + 5 == 1)
def term(s):
    s = s.replace('−', '-').replace('²', '**2').replace('·', '*')
    s = re.sub(r'(\d)([a-z(])', r'\1*\2', s)
    s = re.sub(r'([a-z)])\(', r'\1*(', s)
    s = re.sub(r'(\*\*2)([a-z(\d])', r'\1*\2', s)
    s = re.sub(r'([a-z])([a-z])', r'\1*\2', s)
    return lambda v: eval(s, {'x': v, 'a': v, 'y': v, 'b': v})
waehle('VT2-036', lambda m: m.startswith('In Zeile 2') and ev(lambda x: 9*x - (4*x - 3) - (2 - x)) == ev(lambda x: 6*x + 1))
waehle('VT2-039', lambda m: m.startswith('Nele hat unrecht: Für a = 2 ist 10 − (2 + 3) = 5') and 10 - (2 + 3) == 5 and 10 - 2 + 3 == 11)
assert ev(lambda x: 3*x - (2*x - 5) - (x + 4)) == ev(lambda x: 1)
pruefe('VT2-041', [2, 7, -4])
assert ev(lambda a: 4*a - (3 - 2*a) + (a - 1)) == ev(lambda a: 7*a - 4)
assert ev(lambda x: (6*x + 5) - (2*x - 1) - (x + 3)) == ev(lambda x: 3*x + 3)
waehle('VT2-046', lambda m: ev(term(m)) == ev(lambda x: 6*x - 2*(x - 3)))
gl = {'A': lambda x: 3*(x + 2) - x, 'B': lambda x: 2*(x + 3), 'C': lambda x: 4*x - (2*x - 6), 'D': lambda x: 4*x - (2*x + 6)}
aus = [n for n in gl if sum(ev(gl[n]) == ev(gl[m]) for m in gl) == 1]
waehle('VT2-048', lambda m: [m] == aus)
pruefe('VT2-049', [a for a in range(-20, 21) if ev(lambda x: 3*(x - 2) + a*x) == ev(lambda x: 7*x - 6)][0])

# ---- terme.umformen_teil2 --------------------------------------------------------------------------
def falsch(s):
    l, r = s.split(' = ')
    return ev(term(l)) != ev(term(r))
assert ev(lambda x: 5*x*(3*x + 2)) == ev(lambda x: 15*x*x + 10*x)
pruefe('VT2-052', [2, 3, 2])
assert ev(lambda x: 6*x*(3*x - 2)) == ev(lambda x: 18*x*x - 12*x)
pruefe('VT2-055', [k for k in range(1, 20) if k % 9 == 0 and __import__('math').gcd(18, k) == 9][0])
assert ev(lambda x: 4*x*5*x + 4*x*3) == ev(lambda x: 4*x*(5*x + 3))
pruefe('VT2-057', [2, 4, 20, 25])
assert ev(lambda x: (2*x - 5)**2) == ev(lambda x: 4*x*x - 20*x + 25)
assert ev(lambda x: (x + 7)**2) == ev(lambda x: x*x + 14*x + 49)
waehle('VT2-059', lambda m: m.startswith('Für a = 3, b = 4 ist (3 + 4)² = 49') and 7**2 == 49 and 9 + 16 == 25 and 2*3*4 == 24)
pruefe('VT2-060', [10, 25])
assert ev(lambda x: (x + 5)**2 - x*x) == ev(lambda x: 10*x + 25)
waehle('VT2-062', lambda m: m.startswith('In Zeile 2') and 4**2 == 16)
assert ev(lambda x: (2*x + 5)**2) == ev(lambda x: 4*x*x + 20*x + 25) and ev(lambda x: 4*(2*x + 5)) == ev(lambda x: 8*x + 20)

# ---- zahlen.natuerlich -----------------------------------------------------------------------------
waehle('VT2-086', lambda m: m.startswith('Die vordere 5 ist 1 000-mal') and 5000 // 5 == 1000)
pruefe('VT2-087', [36072 // 100, 36072 // 10])
pruefe('VT2-088', [2, 60000])
waehle('VT2-089', lambda m: m.startswith('Die Nullen halten'))
pruefe('VT2-090', max(int(''.join(p)) for p in itertools.permutations('1234')) - min(int(''.join(p)) for p in itertools.permutations('1234')))
pruefe('VT2-091', [n for n in range(1, 10000) if n * 10 - n == 4050][0])
waehle('VT2-093', lambda m: m == 'dreißigtausendfünf')
waehle('VT2-094', lambda m: m.startswith('In Zeile 3'))
waehle('VT2-095', lambda m: m.startswith('Weil die vordere 300 in der Tausenderklasse'))
waehle('VT2-096', lambda m: m.startswith('Die erste ist größer') and 2000300 > 200300)
pruefe('VT2-097', [3, 10])
waehle('VT2-098', lambda m: m == 'vierhundertdrei Millionen zweitausend' and 403002 * 1000 == 403002000)
pruefe('VT2-099', F(3400) * 6 / 1200)
pruefe('VT2-102', [3, F(7500) * 20 / 10000])
waehle('VT2-103', lambda m: int(m.replace(' ', '')) == (4000 + 4500) // 2)
waehle('VT2-105', lambda m: m.startswith('Weil 100 bis 1 000 ein neunmal') and (1000 - 100) // (100 - 0) == 9)
pruefe('VT2-106', len([n for n in range(0, 10000) if round(F(n, 100)) * 100 == 4800 and F(n, 100) % 1 != F(1, 2) or (F(n, 100) % 1 == F(1, 2) and (n // 100 + 1) * 100 == 4800)]))
def rund(n, st): return (n + st // 2) // st * st
pruefe('VT2-106', len([n for n in range(10000) if rund(n, 100) == 4800]))
ns = [n for n in range(1000) if rund(n, 10) == 350]
pruefe('VT2-107', [min(ns), max(ns)])
pruefe('VT2-109', [2, rund(4949, 100)])
waehle('VT2-110', lambda m: m.startswith('manchmal größer') and rund(16000, 10000) > 16000 and rund(14000, 10000) < 14000 and rund(30000, 10000) == 30000)
waehle('VT2-115', lambda m: m.startswith('Beide sind richtig gerundet') and rund(22817, 1000) == 23000 and rund(22817, 10000) == 20000)
waehle('VT2-117', lambda m: m.startswith('Mia hat unrecht: Ob das Geld reicht') and 237 < 249)
pruefe('VT2-118', abs(sum(rund(z, 1000) for z in (3984, 6017, 1996)) - (3984 + 6017 + 1996)))
waehle('VT2-119', lambda m: m.startswith('Jede Zahl wurde um 440 bis 480') and 1480 + 1460 + 1440 + 1450 == 5830 and 5830 - 4000 == 1830)

def roem(n):
    s = ''
    for w, z in ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= w: s += z; n -= w
    return s
def roem_wert(s):
    v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return sum(v[c] if i + 1 == len(s) or v[c] >= v[s[i + 1]] else -v[c] for i, c in enumerate(s))
assert roem(1949) == 'MCMXLIX'
waehle('VT2-121', lambda m: roem(roem_wert(m)) != m)
pruefe('VT2-123', [roem_wert('M'), roem_wert('CM'), roem_wert('XL'), roem_wert('IV')])
assert roem_wert('MCMXLIV') == 1944
pruefe('VT2-124', max(n for n in range(1, 100) if set(roem(n)) <= {'X', 'I'}))
waehle('VT2-125', lambda m: m.startswith('Nur Annas') and roem(1999) == 'MCMXCIX' and roem(1999) != 'MIM')
pruefe('VT2-126', sum(1 for n in range(1, 31) if len(roem(n)) == 3))
waehle('VT2-129', lambda m: m.startswith('10001 ist größer') and (int('1111', 2), int('10001', 2)) == (15, 17))
pruefe('VT2-130', [2, int('1011', 2)])
pruefe('VT2-132', len({int(format(n, 'b'), 2) for n in range(32)}) )


# ---- nach der Vorprüfung ersetzte oder umgebaute Aufgaben ---------------------------------------------------------------
pruefe('VT2-001', [zins(6000, 5) - zins(6000, 1), 5 - 1])
pruefe('VT2-002', [2, zins(9000, 1) + zins(6000, 2) - zins(4000, 3)])
assert zins(4000, 3) == 120 and zins(9000, 1) == 90 and zins(6000, 2) == 120
pruefe('VT2-005', [k for k in range(1, 20000) if F(k) * F(103, 100) == 5150][0])
pruefe('VT2-007', [zins(200000, 1), zins(150000, 6)])
pruefe('VT2-009', [zins(6000, 1), zins(6000, '0.5'), zins(6000, '0.05')])
waehle('VT2-012', lambda m: zins(6000, m.replace(' %', '').replace(',', '.')) == 15)
pruefe('VT2-013', [zins(2400, '1.5'), zins(1500, '2.4')])
waehle('VT2-014', lambda m: abs(eval(m.replace('·', '*').replace('−', '-').replace(',', '.').replace(' ', '')) - 63) > 1e-6)
pruefe('VT2-015', F(600) / F(25, 1000) - F(600) / F(4, 100))
pruefe('VT2-022', [m for m in range(1, 13) if zins(3600, 4, m) == 60][0])
pruefe('VT2-023', [zins(4000, 5, 3), zins(4000, 3, 5)])
pruefe('VT2-024', [p for p in range(1, 30) if F(p, 100) * F(8, 12) == F(2, 100)][0])
pruefe('VT2-025', [zins(1200, 5, 3), zins(1200, 5, 8), zins(1200, 5, 9)])
pruefe('VT2-027', F(75) * 4 / 10)
pruefe('VT2-031', (7 * 8) - (3 * 2 + 4 * 4))
pruefe('VT2-033', [5 - 3, -2 + 3])
assert ev(lambda x: 5*x*x - 3*x - 2*x*x + 1*x) == ev(lambda x: 3*x*x - 2*x)
pruefe('VT2-034', [9 - 5, 0, 4])
werte37 = {9 - (x - 4) - (6 - x) for x in range(-5, 6)}
assert len(werte37) == 1
pruefe('VT2-037', werte37.pop())
pruefe('VT2-040', [3*0 - (2*0 - 5) - (0 + 4), 0, 1])
assert ev(lambda x: 3*x - (2*x - 5) - (x + 4)) == ev(lambda x: 1)
pruefe('VT2-042', 2500 - (2500 - 43))
waehle('VT2-043', lambda m: m.startswith('Paul hat unrecht: Gleichwertig') and (5*0 - 4, 3*0 + 2) == (-4, 2))
pruefe('VT2-044', [{2*(x + 3) - (2*x + 3) for x in (5,)}.pop(), {2*(x + 3) - (2*x + 3) for x in (100,)}.pop()])
pruefe('VT2-045', sum(1 for x in range(-5, 6) if x*x + 3*x == 2*x*x + 2*x))
ab = [(a, b) for a in range(-9, 10) for b in range(-9, 10) if (b, a + b, 2*a + b) == (4, 7, 10)]
assert ab == [(3, 4)]
pruefe('VT2-047', 3 * 10 + 4)
pruefe('VT2-050', [[i + 1 for i, m in enumerate(['9y² − 6y = 3y(3y − 6)', '8a² − 12a = 4a(2a − 3)', '7b − 14b² = 7b(1 − 2b)', '15x + 10 = 5(3x + 2)']) if falsch(m)][0], 9 // 3, 6 // 3])
pruefe('VT2-051', [k for k in range(-30, 31) if ev(lambda x: 3*x*(2*x + 5)) == ev(lambda x: 6*x*x + k*x)][0])
pruefe('VT2-053', [__import__('math').gcd(12, 18), 12 // 6, 18 // 6])
assert ev(lambda x: 6 * (2*x + 3)) == ev(lambda x: 12*x + 18)
pruefe('VT2-056', [[b for b in range(1, 30) if ev(lambda x: (5*x + 3) * b * x) == ev(lambda x: 20*x*x + 12*x)][0]])
pruefe('VT2-058', [k for k in range(1, 100) if ev(lambda x: (3*x + 4)**2) == ev(lambda x: 9*x*x + k*x + 16)][0])
pruefe('VT2-061', 50**2 - 49**2)
pruefe('VT2-063', [4 * 3, 4 * 2])
assert ev(lambda x: (3*x + 2)**2) == ev(lambda x: 9*x*x + 12*x + 4)
pruefe('VT2-066', 2 * 6)
waehle('VT2-068', lambda m: m.startswith('Ein Kreis um die Mitte M von AB mit Radius 3 cm'))
waehle('VT2-069', lambda m: m.startswith('Richtig, denn C liegt auf dem Kreis über AB'))
pruefe('VT2-071', [r for r in range(1, 11) if sum(1 for d in range(11) if d > r) == 4][0])
pruefe('VT2-073', [pkt(2, 1), pkt(1, 2)])
pruefe('VT2-074', 180 - 90 - 35)
pruefe('VT2-075', [0, 12 - 9])
waehle('VT2-077', lambda m: m.startswith('Falsch: Mehr als 2 Punkte') and max(pkt(r, 3) for r in range(1, 20)) == 2)
pruefe('VT2-078', sum(1 for b in range(1, 130) if lage((50, b, 130 - b)) == 3))
pruefe('VT2-081', [3, 2])
waehle('VT2-082', lambda m: m.startswith('Richtig, denn der Inkreis liegt im Dreieck'))
pruefe('VT2-083', [50 // 2, 70 // 2, 180 - 25 - 35])
pruefe('VT2-085', [d for d in range(1, 10) if d * 10000 - d * 1000 == 27000][0])
pruefe('VT2-092', len([c for c in '40300070' if c == '0']))
waehle('VT2-100', lambda m: int(m.replace(' ', '')) not in range(0, 1001, 250))
pruefe('VT2-101', [8000, 8000 - 7640] if abs(7640 - 8000) < abs(7640 - 7000) else None)
pruefe('VT2-104', F(600, 6) * 4)
pruefe('VT2-108', max(abs(n - rund(n, 100)) for n in range(0, 20000)))
pruefe('VT2-112', len([n for n in range(2000) if rund(n, 10) == 350 and rund(n, 100) == 400]))
pruefe('VT2-113', abs(1234 * 6 - rund(1234, 100) * 6))
assert roem(1449) == 'MCDXLIX'
pruefe('VT2-120', [2, len(roem(1449))])
pruefe('VT2-122', len(roem(3888)))
assert max(len(roem(n)) for n in range(1, 4000)) == len(roem(3888))
pruefe('VT2-127', int('11011', 2))
pruefe('VT2-128', sum(1 for n in range(1, 64) if format(n, 'b').count('1') == 1))
pruefe('VT2-131', int('1000000', 2))
pruefe('VT2-133', len(format(127, 'b')) if set(format(127, 'b')) == {'1'} else -1)
waehle('VT2-111', lambda m: m.startswith('Mia hat recht: 3 600') and rund(3649, 100) == 3600 and rund(rund(3649, 10), 100) == 3700)
waehle('VT2-054', lambda m: m.startswith('Kein ganzzahliger'))

pruefe('VT2-035', (4*5 + 3*2) - (3*5 + 2*2))
pruefe('VT2-038', [k for k in range(-20, 21) if 7*1 - (k*1 - 3) == 5][0])
pruefe('VT2-114', max(n for n in range(1, 100) if n * 36 <= 1000))
pruefe('VT2-116', [4 * rund(9870, 1000), rund(4 * 9870, 1000)])
for k in T:
    if k not in GEPRUEFT: abw.append(f'{k}: nicht gegengerechnet')
import collections
gleich = collections.defaultdict(list)
for k, t in T.items():
    a = t['aufgabe']; o = a['o']
    gleich[(t['lernkarte'], t['pool'], json.dumps(o.get('werte', o.get('wert', a['a'][o['index']] if 'index' in o else None)), ensure_ascii=False))].append(k)
for key, ks in gleich.items():
    if len(ks) > 1: abw.append(f'gleiche Sollantwort im selben Pool und Lernziel: {ks}')
print(f'{len(T)} Aufgaben gelesen')
print(f'{len(abw)} Abweichungen')
for a_ in abw: print('  ', a_)
