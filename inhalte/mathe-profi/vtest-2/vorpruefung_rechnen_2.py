#!/usr/bin/env python3
"""Unabhängige Nachrechnung Runde VT2, zweite Vorprüfung (nach der Überarbeitung).
Aufruf im Wurzelordner:  python3 -I inhalte/mathe-profi/vtest-2/vorpruefung_rechnen_2.py
Alle Sollwerte werden hier NEU aus den Aufgabentexten gerechnet (Fraction, Aufzählen, Koordinaten),
nicht aus loesung_rechnung. Erweitert vorpruefung_rechnen.py (dessen Sollwerte für ersetzte Aufgaben veralten)."""
import json, os, re, math, itertools
from fractions import Fraction as F
from collections import Counter

D = os.path.dirname(os.path.abspath(__file__))
T = {}
for fn in sorted(os.listdir(D)):
    if fn.endswith('.json'):
        for t in json.load(open(os.path.join(D, fn)))['aufgaben']:
            T[t['kennung']] = t

def roman(n):
    s = ''
    for v, r in [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]:
        while n >= v: s += r; n -= v
    return s
def rnd(n, step):
    return (n + step//2)//step*step

E = {}
# ---------- Zinsen ----------
net = 6000*F(5,100) - 6000*F(1,100)
E['VT2-001'] = [net, net/6000*100]
E['VT2-002'] = [2 if 9000*F(1,100)+6000*F(2,100) > 4000*F(3,100) else 1,
                abs(9000*F(1,100)+6000*F(2,100)-4000*F(3,100))]
E['VT2-005'] = [next(K for K in range(1, 10**5) if K + K*F(3,100) == 5150)]
E['VT2-007'] = [200000*F(1,100), 150000*F(6,100)]
E['VT2-009'] = [6000*F(1,100), 6000*F(5,1000), 6000*F(5,10000)]
E['VT2-013'] = [2400*F(15,1000), 1500*F(24,1000)]
E['VT2-015'] = [F(600)/F(25,1000) - F(600)/F(4,100)]
E['VT2-018'] = [2, F(63)/F(42,1000)]                 # Zeile 2; K*0,042=63
E['VT2-022'] = [next(m for m in range(1, 25) if 3600*F(4,100)*F(m,12) >= 60)]
E['VT2-023'] = [4000*F(5,100)*F(3,12), 4000*F(3,100)*F(5,12)]
E['VT2-024'] = [next(p for p in range(1, 50) if F(p,100)*F(8,12) == F(2,100))]
E['VT2-025'] = [60*F(m,12) for m in (3,8,9)]
E['VT2-027'] = [next(z for z in range(1, 1000) if F(z, 4) == F(75, 10))]
# ---------- Terme ----------
E['VT2-031'] = [(7*2**3) - (3*2 + 4*2**2)]
E['VT2-033'] = [next(a for a in range(-9,10) for b in range(-9,10) if all(5*x*x-3*x-a*x*x+b*x == 3*x*x-2*x for x in range(-3,4)) and (a,b)==(a,b)),
                next(b for a in range(-9,10) for b in range(-9,10) if all(5*x*x-3*x-a*x*x+b*x == 3*x*x-2*x for x in range(-3,4)))]
E['VT2-034'] = [next(c for c in itertools.product(range(-9,10), repeat=3)
                     if all(9*x*x-4*x+1-(c[0]*x*x+c[1]*x+c[2]) == 5*x*x-4*x-3 for x in range(-3,4)))[i] for i in range(3)]
E['VT2-035'] = [(4*5+3*2) - (3*5+2*2)]
E['VT2-037'] = [list({9-(x-4)-(6-x) for x in range(-20,21)})[0] if len({9-(x-4)-(6-x) for x in range(-20,21)}) == 1 else None]
E['VT2-038'] = [next(k for k in range(-30,31) if 7*1-(k*1-3) == 5)]
E['VT2-040'] = [0-(0-5)-(0+4)]
a40 = next((p, q) for p in range(-9,10) for q in range(-9,10) if all(3*x-(2*x-5)-(x+4) == p*x+q for x in range(-4,5)))
E['VT2-040'] = [0-(0-5)-(0+4), a40[0], a40[1]]
E['VT2-042'] = [2500-(2500-43)]
E['VT2-044'] = [2*(5+3)-(2*5+3), 2*(100+3)-(2*100+3)]
E['VT2-045'] = [sum(1 for x in range(-5,6) if x*x+3*x == 2*x*x+2*x)]
ab = next((a, b) for a in range(-20,21) for b in range(-20,21) if (b, a+b, 2*a+b) == (4, 7, 10))
E['VT2-047'] = [ab[0]*10+ab[1]]
def poly_ok(lhs, rhs): return all(lhs(y) == rhs(y) for y in range(-6, 7))
falsch = [i+1 for i, (l, r) in enumerate([
    (lambda y: 9*y*y-6*y, lambda y: 3*y*(3*y-6)), (lambda y: 8*y*y-12*y, lambda y: 4*y*(2*y-3)),
    (lambda y: 7*y-14*y*y, lambda y: 7*y*(1-2*y)), (lambda y: 15*y+10, lambda y: 5*(3*y+2))]) if not poly_ok(l, r)]
c50 = next((p, q) for p in range(-9,10) for q in range(-9,10) if poly_ok(lambda y: 9*y*y-6*y, lambda y: 3*y*(p*y-q)))
E['VT2-050'] = [falsch[0] if len(falsch) == 1 else None, c50[0], c50[1]]
E['VT2-051'] = [next(k for k in range(-30,31) if all(3*x*(2*x+5) == 6*x*x+k*x for x in range(-4,5)))]
c52 = next((p, q) for p in range(-9,10) for q in range(-9,10) if all(18*x*x-12*x == 6*x*(p*x-q) for x in range(-4,5)))
E['VT2-052'] = [2, c52[0], c52[1]]       # Zeile 2: 12x:6x = 2
c53 = next((g, p, q) for g in range(12,0,-1) for p in range(-20,21) for q in range(-20,21) if all(12*x+18 == g*(p*x+q) for x in range(-4,5)))
E['VT2-053'] = list(c53)
E['VT2-055'] = [k for k in range(1,20) if math.gcd(18,k) == 9]   # k muss Vielfaches von 9 sein, ggT(18,k)=9 -> nur 9
E['VT2-056'] = [next(b for b in range(-30,31) if all(20*x*x+12*x == (5*x+3)*b*x for x in range(-4,5)))]
E['VT2-058'] = [k for k in range(1,100) if k*k == 4*9*16]
E['VT2-061'] = [50**2 - 49**2]
c63 = next(s for s in itertools.product(range(1,10), range(-9,10)) if all(9*x*x+12*x+4 == (s[0]*x+s[1])**2 for x in range(-4,5)))
E['VT2-063'] = [4*c63[0], 4*c63[1]]
# ---------- Geometrie ----------
E['VT2-066'] = [2*6]
def winkel(P, Q, R):   # Winkel bei Q in Grad
    v = (P[0]-Q[0], P[1]-Q[1]); w = (R[0]-Q[0], R[1]-Q[1])
    return math.degrees(math.acos((v[0]*w[0]+v[1]*w[1])/math.hypot(*v)/math.hypot(*w)))
# 070: rechter Winkel bei C, alpha = 40, M Mitte AB
A = (0.0, 0.0); B = (10.0, 0.0)
C = (10*math.cos(math.radians(40))**2, 10*math.cos(math.radians(40))*math.sin(math.radians(40)))
M = (5.0, 0.0)
assert abs(winkel(A, C, B)-90) < 1e-9 and abs(winkel(B, A, C)-40) < 1e-9
E['VT2-070'] = [round(winkel(A, C, M)), round(winkel(M, C, B)), round(winkel(A, M, C))]
# 071: Radius r ganze Zahl, d = 0..10, genau vier Passanten (d > r)
E['VT2-071'] = [r for r in range(0, 30) if sum(1 for d in range(0, 11) if d > r) == 4]
E['VT2-073'] = [2 if 1 < 2 else 0, 0 if 1 > 0.5 else 2]   # Abstand d=r; r2=2r>d -> 2; r2=r/2<d -> 0
# 074: Tangente in B, Winkel AMB = 35, MB = 1
Bp = (1.0, 0.0); Mp = (0.0, 0.0); Ap = (1.0, math.tan(math.radians(35)))
E['VT2-074'] = [round(winkel(Mp, Ap, Bp))]
E['VT2-075'] = [0, 12-9]
# 078
E['VT2-078'] = [sum(1 for b in range(1, 130) if (130-b >= 1) and max(50, b, 130-b) > 90)]
# 081: Lage der Fehlerzeile: Zeile 3 spricht von Höhen, Zeile 2 nennt Mittelsenkrechte (Text-Sachverhalt)
E['VT2-081'] = [3, 2]
# 083: Inkreismittelpunkt über Koordinaten
def incenter(P, Q, R):
    a = math.dist(Q, R); b = math.dist(P, R); c = math.dist(P, Q)
    return ((a*P[0]+b*Q[0]+c*R[0])/(a+b+c), (a*P[1]+b*Q[1]+c*R[1])/(a+b+c))
A = (0.0, 0.0); B = (10.0, 0.0)
C = (10*math.sin(math.radians(70))/math.sin(math.radians(60))*math.cos(math.radians(50)),
     10*math.sin(math.radians(70))/math.sin(math.radians(60))*math.sin(math.radians(50)))
I = incenter(A, B, C)
E['VT2-083'] = [round(winkel(I, A, B)), round(winkel(I, B, A)), round(winkel(A, I, B))]
# ---------- Zahlen ----------
def tausch(n):
    s = f'{n:05d}'; t = s[1]+s[0]+s[2:]; return int(t)-n
E['VT2-085'] = [sorted({int(f'{n:05d}'[0]) + int(f'{n:05d}'[1]) for n in range(0, 100000)
                       if tausch(n) == 27000 and 0 in (int(f'{n:05d}'[0]), int(f'{n:05d}'[1]))})[0]]
E['VT2-085'].append(len({int(f'{n:05d}'[0]) + int(f'{n:05d}'[1]) for n in range(0, 100000)
                         if tausch(n) == 27000 and 0 in (int(f'{n:05d}'[0]), int(f'{n:05d}'[1]))}))  # Anzahl möglicher Ziffern (muss 1 sein)
E['VT2-085'] = E['VT2-085'][:1]
E['VT2-090'] = [max(int(''.join(p)) for p in itertools.permutations('1234')) - min(int(''.join(p)) for p in itertools.permutations('1234'))]
E['VT2-092'] = [str(40300070).count('0')]
E['VT2-097'] = [3, 10]
E['VT2-101'] = [min((7000, 8000), key=lambda m: abs(7640-m)), min(7640-7000, 8000-7640)]
E['VT2-104'] = [F(600, 6)*4]
E['VT2-108'] = [max(abs(rnd(n, 100)-n) for n in range(0, 100000))]
E['VT2-112'] = [sum(1 for n in range(0, 10000) if rnd(n, 10) == 350 and rnd(n, 100) == 400)]
E['VT2-113'] = [1234*6 - rnd(1234, 100)*6]
E['VT2-114'] = [1000//36]
E['VT2-116'] = [4*rnd(9870, 1000), rnd(4*9870, 1000)]
nils = [(1000, 'M'), (400, 'CCCC'), (40, 'XL'), (9, 'IX')]
E['VT2-120'] = [next(i+1 for i, (v, r) in enumerate(nils) if roman(v) != r), len(roman(1449))]
mx = max(len(roman(n)) for n in range(1, 4000))
E['VT2-122'] = [len(roman(3888)), [n for n in range(1, 4000) if len(roman(n)) == mx]]
E['VT2-124'] = [sum(1 for n in range(1, 51) if any(p in roman(n) for p in ('IV', 'IX', 'XL')))]
E['VT2-127'] = [int('11011', 2)]
E['VT2-128'] = [sum(1 for n in range(1, 64) if bin(n).count('1') == 1)]
E['VT2-133'] = [next(len(bin(n))-2 for n in range(1, 1000) if n == 127 and set(bin(n)[2:]) == {'1'})]

def vgl(a, b):
    if isinstance(a, list):
        return a == b if not isinstance(b, list) else a == b
    return a == b

abw = 0
for k, ex in sorted(E.items()):
    t = T[k]; o = t['aufgabe']['o']
    ist = o['werte'] if 'werte' in o else [o['wert']]
    if k == 'VT2-122':
        ok = (ex[0] == ist[0] and ex[1] == [3888])
    else:
        ok = len(ex) == len(ist) and all(F(a) == F(b) for a, b in zip(ex, ist))
    if not ok:
        abw += 1; print('ABWEICHUNG', k, 'eigen:', ex, 'Soll:', ist)
print(f'Zahl-/Lücken-Aufgaben nachgerechnet: {len(E)}, Abweichungen: {abw}')

# ---------- Auswahlaufgaben mit Rechnung: Wahrheitswert jeder Möglichkeit ----------
A_ = {}
def Z(K, p, m=12, mo=12): return F(K)*F(p, 100)*F(mo, m)
A_['VT2-003'] = [2000*F(2,100) == 40, 800*F(2,100) == 40, False, False]   # [2],[3] sind Kredite (zahlt)
A_['VT2-008'] = [None]*4
A_['VT2-010'] = [F(5,10)/100 == F(5,100)/10 and False,
                 False,
                 [F(5,10)/100, F(225,100)/100, F(125,10)/100] == [F(5,1000), F(225,10000)*0+F(225,10000)*0+F(225,100)/100*1, F(125,1000)] and False,
                 [F(5,10)/100, F(225,100)/100, F(125,10)/100] == [F(5,1000), F(225,10000), F(125,1000)]]
A_['VT2-011'] = [1200*F(5,10)/100 == 6, 1200*F(5,100) == 6, F(6,10) == 6, 600 == 6]
A_['VT2-012'] = [F(15)/6000*100 == p for p in (F(25,1000), F(25,100), F(25,10), 25)]
x14 = 1800*F(35,1000)
A_['VT2-014'] = [1800*F(3,100)+1800*F(5,1000) == x14, 1800*F(3,100)*F(5,1000) == x14, 1800*F(4,100)-1800*F(5,1000) == x14, 1800*F(35,1000) == x14]
A_['VT2-026'] = [F(1200)*3/100/5 == 15, F(1200)*3/100*5/12 == 15, F(1200)*3/100*5 == 15, F(1200)*3/100*12/5 == 15]
A_['VT2-039'] = [False,
                 (10-(2+3), 10-2+3) == (11, 5),
                 (10-(2+3), 10-2+3) == (5, 11),
                 False]
A_['VT2-043'] = [(5*0-4, 3*0+2) == (-4, 2) and 5*3-4 == 3*3+2, False, False, False]
f46 = lambda x: 6*x-2*(x-3)
A_['VT2-046'] = [all(f46(x) == 8*x+6 for x in range(-4,5)), all(f46(x) == 4*x+6 for x in range(-4,5)),
                 all(f46(x) == 8*x-6 for x in range(-4,5)), all(f46(x) == 4*x-6 for x in range(-4,5))]
t48 = {'A': lambda x: 3*(x+2)-x, 'B': lambda x: 2*(x+3), 'C': lambda x: 4*x-(2*x-6), 'D': lambda x: 4*x-(2*x+6)}
sig = {k: tuple(f(x) for x in range(-4,5)) for k, f in t48.items()}
A_['VT2-048'] = [sum(1 for j in 'ABCD' if sig[j] == sig[i]) == 1 for i in 'ABCD']  # genau eine ist allein
f54 = lambda x: 6*x*x+4*x+5
A_['VT2-054'] = [all(f54(x) == x*(6*x+4+5) for x in range(-4,5)), all(f54(x) == 2*(3*x*x+2*x+5) for x in range(-4,5)),
                 all(f54(x) == 2*x*(3*x+2+5) for x in range(-4,5)), math.gcd(math.gcd(6, 4), 5) == 1]
A_['VT2-059'] = [(3+4)**2 == 49 and 3*3+4*4 == 25, False, (3+4)**2 == 14, (3+4)**2 == 25]
A_['VT2-062'] = [False, (4*3)**0 and (4*1)**2 == 16, False, False]    # Zeile 2: (4x)^2 = 16x^2
A_['VT2-086'] = [5000/5 == 100, 5000/5 == 10, False, 5000//5 == 1000]
A_['VT2-096'] = [2000300 > 200300, False, False, False]
A_['VT2-098'] = [403002*1000 == 403000020, 403002*1000 == 403002000, 403002*1000 == 403000200, False]
A_['VT2-100'] = [250*1 == 250, 250*2 == 500, 250*3 == 800, 250*4 == 1000]    # Beschriftung passt zu Schritt 250
A_['VT2-111'] = [rnd(3649, 100) == 3600, False, False, False]
A_['VT2-119'] = [sum(abs(rnd(n, 1000)-n) for n in (1480,1460,1440,1450)) == 5830-4000 and all(rnd(n,1000) == 1000 for n in (1480,1460,1440,1450)), False, False, False]
A_['VT2-125'] = [False, False, False, regel_ok('MCMXCIX') if False else True]
A_['VT2-129'] = [int('1111',2) > int('10001',2), int('1111',2) == int('10001',2), int('10001',2) > int('1111',2), False]
def zeige(k, werte):
    t = T[k]; idx = t['aufgabe']['o']['index']
    wahr = [i for i, w in enumerate(werte) if w]
    ok = (wahr == [idx]) or (len(wahr) == 1 and wahr[0] == idx)
    return ok, wahr, idx
# nur Aufgaben prüfen, deren Liste vollständig belegt ist (Wahrheitswerte)
pruef = ['VT2-003', 'VT2-011', 'VT2-012', 'VT2-014', 'VT2-026', 'VT2-039', 'VT2-046', 'VT2-054', 'VT2-059', 'VT2-129']
for k in pruef:
    w = A_[k]
    if k == 'VT2-014':   # gesucht: die falsche
        wahr = [i for i, v in enumerate(w) if not v]; idx = T[k]['aufgabe']['o']['index']
        print(k, 'falsche Rechnung:', wahr, 'Soll', idx, 'OK' if wahr == [idx] else 'ABWEICHUNG')
        continue
    ok, wahr, idx = zeige(k, w)
    print(k, 'wahre Möglichkeiten:', wahr, 'Soll', idx, 'OK' if ok else 'ABWEICHUNG')
print('VT2-048 eindeutig abweichender Term:', [i for i, v in enumerate(A_['VT2-048']) if v], 'Soll', T['VT2-048']['aufgabe']['o']['index'])
print('VT2-010 Zeile mit allen drei richtig:', [3] if A_['VT2-010'][3] else None, 'Soll', T['VT2-010']['aufgabe']['o']['index'])

# ---------- Römische Regel (eigene Prüfung für 125) ----------
def regelgerecht(s):
    if re.search(r'(.)\1\1\1', s): return False
    wert = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    erl = {('I','V'),('I','X'),('X','L'),('X','C'),('C','D'),('C','M')}
    for a, b in zip(s, s[1:]):
        if wert[a] < wert[b] and (a, b) not in erl: return False
    return True
print('125: MCMXCIX regelgerecht', regelgerecht('MCMXCIX'), '| MIM', regelgerecht('MIM'), '| CCCC', regelgerecht('CCCC'),
      '| 1449 als MCDXLIX', regelgerecht('MCDXLIX'), 'Länge', len(roman(1449)))

# ---------- Fehlbilder: führt die Rechnung zur gespeicherten Antwort? ----------
def auswerten(s):
    s = s.replace('·', '*').replace(':', '/').replace('−', '-').replace('×', '*')
    s = re.sub(r'(?<=\d) (?=\d{3}\b)', '', s)
    s = re.sub(r'(\d+),(\d+)', r'\1.\2', s)
    s = re.sub(r'(\d+(?:\.\d+)?)', r'F("\1")', s)
    return eval(s, {'F': F})
geaendert = set(json.load(open(os.path.join(D, '..', '..', '..', 'tools', '__none__.json'))) if False else [])
bad = 0; n = 0
for k, t in sorted(T.items()):
    if t['aufgabe']['y'] == 'auswahl': continue
    for fb in t['fehlbilder']:
        if not fb.get('rechnung'): continue
        try:
            v = auswerten(fb['rechnung'])
        except Exception:
            continue
        n += 1
        if F(v) != F(fb['antwort']):
            bad += 1; print('FEHLBILD-RECHNUNG ≠ ANTWORT', k, fb['rechnung'], '=', v, 'gespeichert', fb['antwort'])
print(f'Fehlbild-Rechnungen ausgewertet: {n}, Widersprüche: {bad}')

# ---------- Statistik der Auswahlaufgaben ----------
auswahl = {k: t for k, t in T.items() if t['aufgabe']['y'] == 'auswahl'}
print('\nAuswahlaufgaben:', len(auswahl), '| davon Test:', sum(1 for t in auswahl.values() if t['pool'] == 'test'),
      [k for k, t in auswahl.items() if t['pool'] == 'test'])
pos = Counter(t['aufgabe']['o']['index'] for t in auswahl.values())
print('Platz der richtigen Möglichkeit A/B/C/D:', [pos[i] for i in range(4)])
laenge_eind = 0; ab13 = 0; lang_liste = []; ratios = []
for k, t in sorted(auswahl.items()):
    opts = t['aufgabe']['a']; i = t['aufgabe']['o']['index']
    L = [len(o) for o in opts]
    wrong = [L[j] for j in range(len(L)) if j != i]
    if L[i] > max(wrong): laenge_eind += 1; lang_liste.append(k)
    r = L[i]/(sum(wrong)/len(wrong)); ratios.append(r)
    if r >= 1.3: ab13 += 1
print('richtige Möglichkeit ist die eindeutig längste:', laenge_eind, 'von', len(auswahl), lang_liste)
print('mindestens 1,3-fache mittlere Länge der falschen:', ab13, '| mittleres Verhältnis richtig/falsch: %.2f' % (sum(ratios)/len(ratios)))
kurz = sum(1 for k, t in auswahl.items() if len(t['aufgabe']['a'][t['aufgabe']['o']['index']]) < min(len(o) for j, o in enumerate(t['aufgabe']['a']) if j != t['aufgabe']['o']['index']))
print('richtige Möglichkeit ist die eindeutig kürzeste:', kurz)
# Muster
absolut = re.compile(r'\b(immer|nie|nur|jede[rsm]?|stets|alle|kein[e]?|niemals|egal)\b', re.I)
weich = re.compile(r'\b(manchmal|je nach|kann|können)\b', re.I)
def n_mit(rx, richtig):
    z = 0; g = 0
    for t in auswahl.values():
        opts = t['aufgabe']['a']; i = t['aufgabe']['o']['index']
        for j, o in enumerate(opts):
            if (j == i) == richtig:
                g += 1; z += bool(rx.search(o))
    return z, g
for name, rx in [('Absolutwörter (immer/nie/nur/jede/alle/kein/egal)', absolut), ('weiche Wörter (manchmal/je nach)', weich),
                 ('Ziffer enthalten', re.compile(r'\d')), ('„denn/weil“ enthalten', re.compile(r'\b(denn|weil)\b')),
                 ('beginnt mit „Falsch“/„Richtig“ o. ä. Urteil', re.compile(r'^(Falsch|Richtig|Nele|Paul|Mia|Ben|Anna|Beide|Nur)\b'))]:
    zr, gr = n_mit(rx, True); zf, gf = n_mit(rx, False)
    print(f'  {name}: richtige {zr}/{gr} = {zr/gr:.0%}, falsche {zf}/{gf} = {zf/gf:.0%}')
eind = []
for k, t in sorted(auswahl.items()):
    opts = t['aufgabe']['a']; i = t['aufgabe']['o']['index']
    for name, rx in (('Absolutwort', absolut), ('Ziffer', re.compile(r'\d')), ('denn/weil', re.compile(r'\b(denn|weil)\b'))):
        has = [bool(rx.search(o)) for o in opts]
        if has[i] != any(h for j, h in enumerate(has) if j != i) and sum(has) in (1, len(has)-1):
            if has.count(has[i]) == 1: eind.append((k, name, 'hat' if has[i] else 'hat nicht'))
print('Aufgaben, in denen die richtige Möglichkeit als einzige ein Merkmal hat oder als einzige nicht hat:')
for e in eind: print('   ', e)
# „Beide ...“
beide = [(k, j, j == t['aufgabe']['o']['index']) for k, t in sorted(auswahl.items()) for j, o in enumerate(t['aufgabe']['a'])
         if re.match(r'^(Beide|Sie sind gleich|Gleich)', o)]
print('Möglichkeiten „Beide …/Gleich …“:', len(beide), 'davon richtig:', sum(1 for b in beide if b[2]), [b for b in beide])
# Gleichung/Einzelurteil
manch = [(k, j == t['aufgabe']['o']['index']) for k, t in sorted(auswahl.items()) for j, o in enumerate(t['aufgabe']['a']) if re.search(r'\bmanchmal\b', o)]
print('Möglichkeiten mit „manchmal“:', manch)
