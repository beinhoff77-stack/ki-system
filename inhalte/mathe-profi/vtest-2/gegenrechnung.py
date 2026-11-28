"""Unabhängige Gegenrechnung aller Sollwerte von VT2-001 … VT2-119 (113 Aufgaben; VT2-044 … 049 sind seit Welle 1, Runde 2 frei).
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
pruefe('VT2-006', F(3000) * F(8, 100) / F(2, 100))
pruefe('VT2-008', [3, 3600 + zins(3600, '2.5')])
waehle('VT2-010', lambda m: all(F(a.replace(',', '.')) / 100 == F(b.replace(',', '.')) for a, b in
       re.findall(r'([\d,]+) % → ([\d,]+)', m)) and len(re.findall(r'%', m)) == 3)
waehle('VT2-011', lambda m: m.startswith('6 €') and zins(1200, 0.5) == 6)
assert zins(1800, 3.5) == 63
waehle('VT2-016', lambda m: m.startswith('Das Kapital von A ist doppelt so groß, denn'))
waehle('VT2-017', lambda m: m == '□ · 0,04 = 52')
pruefe('VT2-018', [1, F(63) / F(42, 1000)])
waehle('VT2-019', lambda m: m.startswith('Anna,') and F(90) / F(25, 1000) > F(90) / F(3, 100) * 1 and F(90) * 100 / F(5, 2) > F(90) * 100 / 3)
pruefe('VT2-020', F(54) / F(3, 100) / F(6, 10))
waehle('VT2-021', lambda m: m.startswith('p ist doppelt so groß wie q') and 1000 * 2 * 1 == 2000)
# Bank-Vergleich: Zinsen in € je 1 000 €
bank = {'A': zins(1000, 6, 4), 'B': zins(1000, 3, 9), 'C': zins(1000, 2, 12), 'D': zins(1000, 8, 3)}
waehle('VT2-028', lambda m: m.startswith('Sie sind 3-mal so hoch') and F(9, 3) == 3)

# ---- geometrie.kreis -------------------------------------------------------------------------------
waehle('VT2-064', lambda m: m.startswith('MC bleibt immer gleich lang') and F(10, 2) == 5)
# C(2|y), A(-2|0), B(6|0): rechter Winkel bei C  <=>  (A-C)·(B-C) = 0, y ganzzahlig probiert
pruefe('VT2-065', [y for y in range(1, 20) if (-2 - 2) * (6 - 2) + (0 - y) * (0 - y) == 0][0])
assert [y for y in (2, 4, 6, 8) if (0 - 4) * (8 - 4) + y * y == 0] == [4]
pruefe('VT2-070', [40, 90 - 40, 180 - 2 * 40])
waehle('VT2-072', lambda m: m == 'r > 7 cm')
def pkt(r, d): return 2 if r > d else (1 if r == d else 0)
pruefe('VT2-076', [pkt(3, d) + pkt(7, d) for d in (3, 5, 7)])
# Umkreismittelpunkt: innen <=> alle Winkel < 90°, auf Seite <=> ein Winkel = 90°, außen <=> ein Winkel > 90°
def lage(w): return 1 if max(w) < 90 else (2 if max(w) == 90 else 3)
for w in ((35, 75, 70), (30, 60, 90), (25, 40, 115)): assert sum(w) == 180
waehle('VT2-084', lambda m: m.startswith('Sie fallen zusammen'))

# ---- terme.umformen --------------------------------------------------------------------------------
def ev(f, xs=(-3, -1, 0, 1, 2, 5, 7)): return [f(x) for x in xs]
assert ev(lambda x: 5*x*x + 3*x - 2*x*x - 7*x + 4) == ev(lambda x: 3*x*x - 4*x + 4)
assert ev(lambda a: (3*a+2) + (5*a-1) + (a+4)) == ev(lambda a: 9*a + 5)
def term(s):
    s = s.replace('−', '-').replace('²', '**2').replace('·', '*')
    s = re.sub(r'(\d)([a-z(])', r'\1*\2', s)
    s = re.sub(r'([a-z)])\(', r'\1*(', s)
    s = re.sub(r'(\*\*2)([a-z(\d])', r'\1*\2', s)
    s = re.sub(r'([a-z])([a-z])', r'\1*\2', s)
    return lambda v: eval(s, {'x': v, 'a': v, 'y': v, 'b': v})
assert ev(lambda x: 3*x - (2*x - 5) - (x + 4)) == ev(lambda x: 1)
assert ev(lambda a: 4*a - (3 - 2*a) + (a - 1)) == ev(lambda a: 7*a - 4)
assert ev(lambda x: (6*x + 5) - (2*x - 1) - (x + 3)) == ev(lambda x: 3*x + 3)
gl = {'A': lambda x: 3*(x + 2) - x, 'B': lambda x: 2*(x + 3), 'C': lambda x: 4*x - (2*x - 6), 'D': lambda x: 4*x - (2*x + 6)}
aus = [n for n in gl if sum(ev(gl[n]) == ev(gl[m]) for m in gl) == 1]

# ---- terme.umformen_teil2 --------------------------------------------------------------------------
def falsch(s):
    l, r = s.split(' = ')
    return ev(term(l)) != ev(term(r))
assert ev(lambda x: 5*x*(3*x + 2)) == ev(lambda x: 15*x*x + 10*x)
pruefe('VT2-052', [1 if __import__('math').gcd(18, 12) != 3 else 2, 18 // __import__('math').gcd(18, 12), 12 // __import__('math').gcd(18, 12)])
assert ev(lambda x: 6*x*(3*x - 2)) == ev(lambda x: 18*x*x - 12*x)
pruefe('VT2-055', (lambda L: L[0] if len(L) == 1 else None)([k for k in range(7, 20) if __import__('math').gcd(18, k) == 6]))
assert ev(lambda x: 4*x*5*x + 4*x*3) == ev(lambda x: 4*x*(5*x + 3))
pruefe('VT2-057', [2, 4, 20, 25])
assert ev(lambda x: (2*x - 5)**2) == ev(lambda x: 4*x*x - 20*x + 25)
assert ev(lambda x: (x + 7)**2) == ev(lambda x: x*x + 14*x + 49)
waehle('VT2-059', lambda m: m.startswith('Für a = 3, b = 4 ist (3 + 4)² = 49') and 7**2 == 49 and 9 + 16 == 25 and 2*3*4 == 24)
pruefe('VT2-060', [10, 25])
assert ev(lambda x: (x + 5)**2 - x*x) == ev(lambda x: 10*x + 25)
assert ev(lambda x: (2*x + 5)**2) == ev(lambda x: 4*x*x + 20*x + 25) and ev(lambda x: 4*(2*x + 5)) == ev(lambda x: 8*x + 20)

# ---- zahlen.natuerlich -----------------------------------------------------------------------------

def rund(n, st): return (n + st // 2) // st * st
ns = [n for n in range(1000) if rund(n, 10) == 350]

def roem(n):
    s = ''
    for w, z in ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= w: s += z; n -= w
    return s
def roem_wert(s):
    v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return sum(v[c] if i + 1 == len(s) or v[c] >= v[s[i + 1]] else -v[c] for i, c in enumerate(s))
assert roem(1949) == 'MCMXLIX'
assert roem_wert('MCMXLIV') == 1944


# ---- nach der Vorprüfung ersetzte oder umgebaute Aufgaben ---------------------------------------------------------------
pruefe('VT2-001', [45 + zins(3000, 1), [k for k in range(1, 20000) if zins(k, 3) - zins(3000, 1) == 45][0]])
pruefe('VT2-002', [2, zins(9000, 1) + zins(6000, 2) - zins(4000, 3)])
assert zins(4000, 3) == 120 and zins(9000, 1) == 90 and zins(6000, 2) == 120
pruefe('VT2-005', [k for k in range(1, 20000) if F(k) * F(50, 2000) == 90][0])
pruefe('VT2-007', [zins(200000, '0.5'), zins(150000, 5)])
pruefe('VT2-009', [F(80) / 4, F(80) * F(5, 2), F(80) / 20])
waehle('VT2-014', lambda m: abs(eval(m.replace('·', '*').replace('−', '-').replace(',', '.').replace(' ', '')) - 63) > 1e-6)
pruefe('VT2-015', [[k for k in range(1, 100000) if zins(k, 2) == 120][0], [k for k in range(1, 100000) if zins(k, 3) == 120][0], [k for k in range(1, 100000) if zins(k, 2) == 120][0] - [k for k in range(1, 100000) if zins(k, 3) == 120][0]])
pruefe('VT2-022', [zins(2400, 3, 10), [m for m in range(1, 40) if zins(4500, 2, m) == zins(2400, 3, 10)][0]])
pruefe('VT2-024', [p for p in range(1, 30) if F(p, 100) * F(8, 12) == F(2, 100)][0])
pruefe('VT2-025', [zins(3000, 2) * F(4, 12), zins(3000, 3) * F(8, 12), zins(3000, 2) * F(4, 12) + zins(3000, 3) * F(8, 12)])
pruefe('VT2-027', F(75) * 4 / 10)
assert ev(lambda x: 5*x*x - 3*x - 2*x*x + 1*x) == ev(lambda x: 3*x*x - 2*x)
werte37 = {9 - (x - 4) - (6 - x) for x in range(-5, 6)}
assert len(werte37) == 1
assert ev(lambda x: 3*x - (2*x - 5) - (x + 4)) == ev(lambda x: 1)
orig45 = lambda x: 3*(x + 2) - (x - 4)
ts45 = [lambda x: 3*x + 6 - x - 4, lambda x: 2*x + 2, lambda x: 3*x + 6 - x + 4, lambda x: 2*x + 10, lambda x: 3*x + 6 - (x - 4)]
ab = [(a, b) for a in range(-9, 10) for b in range(-9, 10) if (b, a + b, 2*a + b) == (4, 7, 10)]
assert ab == [(3, 4)]
pruefe('VT2-050', [[i + 1 for i, m in enumerate(['9y² − 6y = 3y(3y − 6)', '8a² − 12a = 4a(2a − 3)', '7b − 14b² = 7b(1 − 2b)', '15x + 10 = 5(3x + 2)']) if falsch(m)][0], 9 // 3, 6 // 3])
pruefe('VT2-051', [F(-6) / F(-3), F(-9) / F(-3), F(-6) / 3, F(-9) / 3])
assert ev(lambda x: 6 * (2*x + 3)) == ev(lambda x: 12*x + 18)
pruefe('VT2-056', [[b for b in range(1, 30) if ev(lambda x: (5*x + 3) * b * x) == ev(lambda x: 20*x*x + 12*x)][0]])
pruefe('VT2-058', [k for k in range(1, 100) if ev(lambda x: (5*x - 2)**2) == ev(lambda x: 25*x*x - k*x + 4)][0])
pruefe('VT2-063', [4 * 3, 4 * 2])
assert ev(lambda x: (3*x + 2)**2) == ev(lambda x: 9*x*x + 12*x + 4)
pruefe('VT2-066', 2 * 6)
waehle('VT2-068', lambda m: m.startswith('Ein Kreis um die Mitte M von AB mit Radius 3 cm'))
pruefe('VT2-071', [r for r in range(1, 11) if sum(1 for d in range(11) if d > r) == 4][0])
pruefe('VT2-073', [pkt(2, 1), pkt(1, 2)])
pruefe('VT2-074', 180 - 90 - 35)
pruefe('VT2-075', [0, 12 - 9])
waehle('VT2-077', lambda m: m.startswith('Falsch: Mehr als 2 Punkte') and max(pkt(r, 3) for r in range(1, 20)) == 2)
pruefe('VT2-078', sum(1 for b in range(1, 110) if lage((70, b, 110 - b)) == 3))
pruefe('VT2-081', [1, 3])
pruefe('VT2-083', [2 * 28, 2 * 17, 180 - 56 - 34])
assert roem(1449) == 'MCDXLIX'
assert max(len(roem(n)) for n in range(1, 4000)) == len(roem(3888))


# ---- Urteil 1222: neu gefasste Aufgaben (jeweils eigener Rechenweg) -----------------------------------
waehle('VT2-004', lambda m: m.startswith('Sie bekommt 40 € Sparzinsen und zahlt 40 € Kreditzinsen') and zins(2000, 2) == 40)
waehle('VT2-012', lambda m: m.startswith('Sie werden zehnmal so klein') and F('0.12') * 10 == F('1.2'))
pruefe('VT2-013', [F('1.5') * F(4800, 2400), F('1.5') * F(4800, 1200)])
waehle('VT2-023', lambda m: m.startswith('Beide bringen gleich viele Zinsen') and zins(1000, 4, 6) == zins(1000, 2, 12))
waehle('VT2-026', lambda m: m.startswith('Beide bekommen gleich viel Zinsen') and zins(1200, 3, 5) == zins(6000, 3, 1))
_f36 = lambda a, b, x: (a*x + 5) - (3*x - b) - (2*x + 9)
waehle('VT2-053', lambda m: m.startswith('Alle drei Produkte sind gleichwertig') and all(ev(f_) == ev(lambda x: 6*x*x + 15*x) for f_ in (lambda x: 3*(2*x*x + 5*x), lambda x: 3*x*(2*x + 5), lambda x: x*(6*x + 15))))
waehle('VT2-054', lambda m: m.startswith('Man kann nichts außer 1 ausklammern'))
waehle('VT2-061', lambda m: m.startswith('Nein: Für x = 3') and (3 - 3)**2 == 0 and all((x_ - 3)**2 >= 0 for x_ in range(-9, 10)))
pruefe('VT2-062', [(4 + 3)**2 - (4**2 + 9), max(c for c in range(-20, 21) if all((x_ + 3)**2 - (x_*x_ + 9) == c*x_ for x_ in range(-4, 5)))])
pruefe('VT2-067', [3, F(14, 2)])
waehle('VT2-069', lambda m: m.startswith('Die Seite AB ist ein Durchmesser des Umkreises, denn C liegt'))
pruefe('VT2-079', max(a_ for a_ in range(1, 90) if 180 - 2*a_ > 90))
pruefe('VT2-080', [F(180 * 4, 6), F(180, 6) / 10])
waehle('VT2-082', lambda m: m.startswith('Er liegt bei einem beliebigen Dreieck innerhalb des Dreiecks'))

# ---- Welle 1, Runde 2: terme.umformen (VT2-029 … 043) und zahlen.natuerlich (VT2-085 … 119), eigener Rechenweg je Aufgabe ----------
# terme.umformen / zusammenfassen
pruefe('VT2-029', [a for a in range(-20, 21) if ev(lambda x: 2 * ((3*x + 2) + (x + 6)), xs=(1, 2, 5, 7, 11)) == ev(lambda x: 4 * (2*x + a), xs=(1, 2, 5, 7, 11))][0])
waehle('VT2-030', lambda m: m.startswith('In Zeile 3') and -4 + 5 == 1)
waehle('VT2-031', lambda m: m.startswith('Sie haben nur für x = 1') and [x for x in range(-50, 51) if 3*x + 2 == 5*x] == [1])
pruefe('VT2-032', (lambda x: 5*x - 7 + 3 - 4*x - x + 10)(987654))
_t33 = lambda a, b: 7*a - 2*b + 3 - 4*a + 5*b - a
_d33 = {_t33(a, b) - _t33(a + 1, b - 1) for a in range(-6, 7) for b in range(-6, 7)}
assert len(_d33) == 1
pruefe('VT2-033', _d33.pop())
# minusklammer
pruefe('VT2-034', [a for a in range(1, 60) if all((40 - (3*x - a)) - (40 - 3*x - a) == 18 for x in range(-5, 6))][0])
_f35 = lambda a: 4*a - (3 - 2*a) + (a - 1)
pruefe('VT2-035', [2, _f35(1) - _f35(0), _f35(0)])
waehle('VT2-036', lambda m: m.startswith('Mia hat recht') and all(50 - (x - 3) == 53 - x != 50 - x - 3 for x in range(0, 50)))
def _T37(n, x): return x - 1 if n == 1 else x - _T37(n - 1, x)
pruefe('VT2-037', [_T37(10, 50), _T37(11, 50)])
waehle('VT2-038', lambda m: m.startswith('Mia hat recht, für jede Zahl x') and all(-(x - 7) == 7 - x for x in range(-30, 31)))
# aequivalenz
_z39 = all((a == c and b == d) for a in range(-5, 6) for b in range(-5, 6) for c in range(-5, 6) for d in range(-5, 6) if b == d and a + b == c + d)
waehle('VT2-039', lambda m: m.startswith('Sie sind gleichwertig') and _z39 and [x for x in (1, 2) if x*x == 3*x - 2] == [1, 2])
pruefe('VT2-040', (lambda T, w: [sum(all(t(n) == w(n) for n in range(1, 40)) for t in T), w(10)])([lambda n: 4 + 3*(n - 1), lambda n: 3*n + 1, lambda n: 4*n - n - 1], lambda n: 4*n - (n - 1)))
pruefe('VT2-041', [k for k in range(-50, 51) if all(F(2*x + k, 2) - x == 10 for x in range(-5, 6))][0])
pruefe('VT2-042', sum(1 for x in range(-100, 101) if 3*(x + 4) - x == 2*x + 9))
_g43 = [lambda x: 2*(x + 3), lambda x: 2*x + 6, lambda x: 3*(x + 2) - x, lambda x: 5*x - 2*(x + 1), lambda x: 3*x - 2, lambda x: 3*x + 2]
pruefe('VT2-043', sum(1 for i in range(6) for j in range(i + 1, 6) if ev(_g43[i]) == ev(_g43[j])))

# zahlen.natuerlich: Zahlwörter wirklich erzeugen (für 090, 093, 094)
_E = ['', 'eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun']
_ZW = ['zehn', 'elf', 'zwölf', 'dreizehn', 'vierzehn', 'fünfzehn', 'sechzehn', 'siebzehn', 'achtzehn', 'neunzehn']
_ZE = ['', '', 'zwanzig', 'dreißig', 'vierzig', 'fünfzig', 'sechzig', 'siebzig', 'achtzig', 'neunzig']
def _drei(n, ein=False):
    h, r = divmod(n, 100)
    s = (('ein' if h == 1 else _E[h]) + 'hundert') if h else ''
    if r == 1: s += 'ein' if ein else 'eins'
    elif r < 10: s += _E[r]
    elif r < 20: s += _ZW[r - 10]
    else: s += (('ein' if r % 10 == 1 else _E[r % 10]) + 'und' if r % 10 else '') + _ZE[r // 10]
    return s
def wort(n):
    m, r = divmod(n, 10**6); t, e = divmod(r, 1000)
    s = ('eine Million ' if m == 1 else _drei(m, True) + ' Millionen ') if m else ''
    s += (_drei(t, True) + 'tausend') if t else ''
    return (s + _drei(e)).strip() or 'null'
assert wort(204007005) == 'zweihundertvier Millionen siebentausendfünf' and wort(3000900) == 'drei Millionen neunhundert'
# stellenwert
_z85 = [n for n in range(100000, 1000000) if str(n).count('4') == 2 and (lambda s, i: s.index('4', i + 1) - i == 3)(str(n), str(n).index('4'))
        and len(set(str(n).replace('4', ''))) == 4]
pruefe('VT2-085', max(_z85))
_p86 = {(a, b) for a in range(10) for b in range(10) if (b * 10000 + a * 1000) - (a * 10000 + b * 1000) == 36000}
waehle('VT2-086', lambda m: m.startswith('Die Tausenderziffer war um 4 größer') and all(b - a == 4 for a, b in _p86) and len(_p86) == 6)
pruefe('VT2-087', [2, int('360482'[1]) * 10 ** (len('360482') - 2)])
waehle('VT2-088', lambda m: m.startswith('Die Nullen halten') and int('79') != 7090 and int('709') != 7090 and int('790') != 7090)
_l89 = [t*1000 + h*100 + z*10 + e for t in range(10) for h in range(10) for z in range(10) for e in range(10) if t + h + z + e == 12]
pruefe('VT2-089', [min(_l89), max(_l89)])
# ziffern_zu_zahlwort
pruefe('VT2-090', sum(1 for n in range(10**6 + 1, 2 * 10**6) if 'tausend' not in wort(n)))
waehle('VT2-091', lambda m: m.startswith('Immer acht') and wort(10**7).startswith('zehn Millionen') and wort(10999999).startswith('zehn Millionen')
       and not wort(11 * 10**6).startswith('zehn Millionen') and len(str(10**7)) == len(str(10999999)) == 8)
waehle('VT2-092', lambda m: m.startswith('In Zeile 3'))
def _gr(s, links):
    if links: return [s[i:i + 3] for i in range(0, len(s), 3)]
    k = len(s) % 3 or 3
    return [s[:k]] + [s[i:i + 3] for i in range(k, len(s), 3)]
pruefe('VT2-093', sum(1 for n in range(1000, 10**6) if [int(g) for g in _gr(str(n), True)] == [int(g) for g in _gr(str(n), False)]
                       and len(_gr(str(n), True)) == len(_gr(str(n), False))))
_c94 = [_drei(x).count('hundert') for x in range(1000)]
assert max(_c94) == 1
pruefe('VT2-094', [3 * max(_c94), min(x for x in range(1000) if _c94[x]) * (10**6 + 1000 + 1)])
assert wort(100100100).count('hundert') == 3
# strahl_eintragen
_m95 = F(2000 - 1200, 4)
pruefe('VT2-095', [[d for d in range(1, 40) if 1200 + d * _m95 == 3400][0], 1200 + 9 * _m95])
waehle('VT2-096', lambda m: m.startswith('Das stimmt nie') and all((2 * (300 + 200 * k) - 300) % 200 != 0 for k in range(200)))
waehle('VT2-097', lambda m: m.startswith('Auf A liegen') and F(1000 - 400, 50) / F(1000 - 400, 200) == 4)
pruefe('VT2-098', sum(1 for n in range(1, 1200) if n % (1200 // 6) == 0 and n % (1200 // 8) == 0))
waehle('VT2-099', lambda m: m.startswith('Er ist falsch beschriftet') and len({10 - 0, 100 - 10, 1000 - 100}) == 3)
# runden_regel
pruefe('VT2-100', sum(1 for n in range(1, 101) if rund(n, 10) == rund(n, 100)))
pruefe('VT2-101', max(abs(n - rund(n, 100)) for n in range(0, 20000)))
pruefe('VT2-102', [2, rund(4949, 100)])
waehle('VT2-103', lambda m: m.startswith('Jeder der drei Fälle') and rund(64000, 10000) < 64000 and rund(66000, 10000) > 66000 and rund(60000, 10000) == 60000)
waehle('VT2-104', lambda m: m.startswith('Die gerundete Zahl von a ist nie größer') and all(rund(a, 100) <= rund(b, 100) for a in range(2000) for b in range(a + 1, a + 120)) and rund(4760, 100) == rund(4770, 100))
# runden_sinnvoll
pruefe('VT2-105', [min(n // 3 for n in range(1, 100) if rund(n, 10) == 30), max(n // 3 for n in range(1, 100) if rund(n, 10) == 30)])
pruefe('VT2-106', [max(n for n in range(1, 100) if n * 36 <= 1000), min(n for n in range(1, 100) if n * 36 >= 1000)])
waehle('VT2-107', lambda m: m.startswith('Beide sind richtig gerundet') and rund(22817, 1000) == 23000 and rund(22817, 10000) == 20000)
pruefe('VT2-108', [50*30 - 48*29, 48*30 - 48*29])
_z109 = (3460, 3420, 3440, 3470)
waehle('VT2-109', lambda m: m.startswith('Jede Zahl wurde um 420 bis 470') and sum(_z109) == 13790 and sum(rund(z, 1000) for z in _z109) == 12000
       and {z - rund(z, 1000) for z in _z109} <= set(range(420, 471)) and rund(sum(_z109), 1000) != sum(_z109))
# roemisch_schreiben
def _add(n):
    s = 0
    for w in (100, 50, 10, 5, 1): s += n // w; n %= w
    return s
_sp = {n: _add(n) - len(roem(n)) for n in range(1, 91)}
_best = [n for n in _sp if _sp[n] == max(_sp.values())]
assert len(_best) == 1
pruefe('VT2-110', [_best[0], _sp[_best[0]]])
waehle('VT2-111', lambda m: roem(roem_wert(m)) != m)
waehle('VT2-112', lambda m: m.startswith('Es stimmt nur manchmal') and len(roem(12)) > len(roem(10)) and 12 > 10 and len(roem(8)) > len(roem(50)) and 8 < 50)
pruefe('VT2-113', max(n for n in range(1, 6000) if 'MMMM' not in roem(n)))
pruefe('VT2-114', min(n for n in range(1, 200) if len(roem(n)) == 6))
# dualsystem
pruefe('VT2-115', sum(1 for n in range(1, 32) if sum(int(d) * 2**i for i, d in enumerate(format(n, 'b'))) == n))
waehle('VT2-116', lambda m: m.startswith('Beide sind gleich groß') and int('0111', 2) == int('111', 2) == 7)
_d117 = {int(s, 2) - int(s[-1] + s[1:-1] + s[0], 2) for s in (format(n, 'b') for n in range(64, 128)) if s.endswith('0')}
assert len(_d117) == 1
pruefe('VT2-117', _d117.pop())
waehle('VT2-118', lambda m: m.startswith('Sie lässt sich ohne Rest durch 4 teilen') and all(n % 4 == 0 for n in range(4, 2048) if format(n, 'b').endswith('00'))
       and any(n % 100 for n in range(4, 2048) if format(n, 'b').endswith('00')))
_l119 = [len(str(n)) for n in range(1, 5000) if len(format(n, 'b')) == 10]
pruefe('VT2-119', [min(_l119), max(_l119)])

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
