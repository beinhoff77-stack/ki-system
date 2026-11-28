#!/usr/bin/env python3
"""Dritte Vorprüfung VT2: unabhängige Nachrechnung (nur Standardbibliothek, exakte Brüche).
Aufruf im Wurzelordner:  python3 -I inhalte/mathe-profi/vtest-2/vorpruefung_rechnen_3.py
Teil 1: allgemeine Prüfung aller 133 Aufgaben (Rechenausdrücke, Fehlbilder, Auswahlbau).
Teil 2: Sollwerte werden hier NEU aus den Aufgabentexten bestimmt (Parameter von Hand eingetragen, Rechnung durch Aufzählen,
        Einsetzen oder Brüche), nicht aus loesung_rechnung gelesen.
Teil 3: Auswahl-Statistik über alle Auswahlaufgaben."""
import json, os, re, itertools, math
from fractions import Fraction as F
from collections import Counter

D = os.path.dirname(os.path.abspath(__file__))
T = {}
for fn in sorted(os.listdir(D)):
    if fn.endswith('.json'):
        for t in json.load(open(os.path.join(D, fn), encoding='utf-8'))['aufgaben']:
            T[t['kennung']] = t
FEHLER = []
def fehler(k, msg): FEHLER.append(f'{k}: {msg}')

# ---------------------------------------------------------------- Ausdrücke
def ev(s):
    s = str(s).replace('−', '-').replace('·', '*').replace(':', '/').replace('²', '**2').replace('³', '**3')
    s = re.sub(r'(?<=\d) (?=\d{3}\b)', '', s)               # 5 150 -> 5150
    s = re.sub(r'(\d+(?:,\d+)?)', lambda m: f"F('{m.group(1).replace(',', '.')}')", s)
    return eval(s, {'F': F, 'abs': abs, '__builtins__': {}})

# ---------------------------------------------------------------- Teil 1
def sollwerte(t):
    o = t['aufgabe']['o']
    if t['antwortform'] == 'zahl': return [F(str(o['wert']))]
    if t['antwortform'] == 'luecken': return [F(str(w)) for w in o['werte']]
    return None

for k, t in T.items():
    soll = sollwerte(t)
    if t['antwortform'] in ('zahl', 'luecken'):
        r = t['loesung_rechnung']; r = r if isinstance(r, list) else [r]
        if len(r) != len(soll): fehler(k, 'Zahl der Rechenausdrücke != Zahl der Lösungswerte')
        for a, b in zip(r, soll):
            try:
                if ev(a) != b: fehler(k, f'loesung_rechnung {a!r} = {ev(a)} != Soll {b}')
            except Exception as e: fehler(k, f'loesung_rechnung {a!r} nicht auswertbar ({e})')
        seen = set()
        for fb in t['fehlbilder']:
            li = fb.get('luecke', 1)
            if not 1 <= li <= len(soll): fehler(k, f'Fehlbild mit Lücke {li} außerhalb'); continue
            if F(str(fb['antwort'])) == soll[li-1]: fehler(k, f'Fehlbild gleich Lösung: {fb["antwort"]}')
            if (li, fb['antwort']) in seen: fehler(k, f'Fehlbild doppelt: {fb["antwort"]}')
            seen.add((li, fb['antwort']))
            if fb.get('rechnung') not in (None, ''):
                try:
                    if ev(fb['rechnung']) != F(str(fb['antwort'])): fehler(k, f'Fehlbild-Rechnung {fb["rechnung"]} = {ev(fb["rechnung"])} != {fb["antwort"]}')
                except Exception as e: fehler(k, f'Fehlbild-Rechnung {fb["rechnung"]!r} ({e})')
        # Fehler-Detektiv: Fehlbild "Zeile ..." muss in Lücke 1 stehen
        for fb in t['fehlbilder']:
            if re.search(r'Zeile \d für falsch|Folgefehler|erst Zeile|Zeile \d genannt', fb['beschreibung']) and fb.get('luecke', 1) != 1:
                fehler(k, f'Fehlbild zur Zeilenwahl steht bei Lücke {fb["luecke"]}: {fb["beschreibung"][:60]}')
        if t['antwortform'] == 'luecken':
            lueck = {fb['luecke'] for fb in t['fehlbilder']}
            fehl = [i for i in range(1, len(soll)+1) if i not in lueck]
            if fehl: print(f'Hinweis {k}: Lücke(n) {fehl} ohne Fehlbild')
    else:
        a = t['aufgabe']['a']; idx = t['aufgabe']['o']['index']
        if len(a) != 4 or len(set(a)) != 4: fehler(k, 'nicht 4 verschiedene Möglichkeiten')
        fb = {f['index']: f for f in t['fehlbilder']}
        if idx in fb: fehler(k, 'Fehlbild zur richtigen Möglichkeit')
        for i in range(4):
            if i != idx:
                if i not in fb: fehler(k, f'Möglichkeit {i} ohne Fehlbild')
                elif fb[i]['antwort'] != a[i]: fehler(k, f'Fehlbild {i}: Antworttext weicht ab')

# ---------------------------------------------------------------- Teil 2
def roman(n):
    s = ''
    for v, r in [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]:
        while n >= v: s += r; n -= v
    return s
def roman_wert(s):
    w = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}; n = 0
    for i, c in enumerate(s):
        n += -w[c] if i+1 < len(s) and w[c] < w[s[i+1]] else w[c]
    return n
def rund(n, schritt): return (n + schritt//2) // schritt * schritt     # kaufmännisch, natürliche Zahlen

E = {}
# Zinsen
E['001'] = [6000*F(5,100) - 6000*F(1,100), (6000*F(5,100) - 6000*F(1,100)) / 6000 * 100]
E['002'] = [2, 9000*F(1,100) + 6000*F(2,100) - 4000*F(3,100)]
E['004'] = [3, 6000*F(5,100) - 5000*F(1,100)]
E['005'] = [next(K for K in range(1, 10**5) if K + K*F(3,100) == 5150)]
E['006'] = [3000*F(8,100) / F(2,100)]
E['007'] = [200000*F(5,1000), 150000*F(5,100)]
E['008'] = [2, 3600 + 3600*F(25,10)/100]                      # Zeile 2: 2,5 % sind 2,5 mal 1 %, nicht 25 mal
E['009'] = [80*F(25,100)/1, 80*F(25,10), 80*F(5,100)]         # Faktor zu 1 %: 0,25 / 2,5 / 0,05
E['013'] = [2400*F(15,1000), 1500*F(26,1000)]
E['015'] = [next(K for K in range(1, 10**5) if K*F(4,100) - K*F(25,1000) == 45)]
E['018'] = [2, next(K for K in range(1, 10**5) if K*F(42,1000) == 63)]
E['020'] = [next(G for G in range(1, 10**5) if G*F(6,10)*F(3,100) == 54)]
E['022'] = [2400*F(3,100)*F(10,12), next(m for m in range(1, 40) if 4500*F(2,100)*F(m,12) == 2400*F(3,100)*F(10,12))]
E['023'] = [4000*F(5,100)*F(3,12), 4000*F(3,100)*F(5,12)]
E['024'] = [next(p for p in range(1, 60) if F(p,100)*F(8,12) == F(2,100))]
E['025'] = [1200*F(5,100)*F(m,12) for m in (3, 8, 9)]
E['027'] = [next(z for z in range(1, 1000) if F(z, 4) == F(75, 10))]
# Terme
def terme_koeff(f, grad=3):
    """Koeffizienten durch Auswerten an Stützstellen (Polynom bis Grad 3)."""
    xs = range(0, grad+1)
    import fractions
    M = [[F(x)**j for j in range(grad+1)] for x in xs]; v = [F(f(x)) for x in xs]
    n = grad+1
    for i in range(n):
        p = next(r for r in range(i, n) if M[r][i] != 0); M[i], M[p] = M[p], M[i]; v[i], v[p] = v[p], v[i]
        for r in range(n):
            if r != i and M[r][i] != 0:
                q = M[r][i]/M[i][i]; M[r] = [a-q*b for a, b in zip(M[r], M[i])]; v[r] -= q*v[i]
    return [v[i]/M[i][i] for i in range(n)]
c = terme_koeff(lambda x: 3*x*x+2*x-x*x+4+5*x-3*x*x+7)
E['030'] = [sum(1 for z in c if z != 0), c[2]]
E['031'] = [7*2**3 - (3*2 + 4*2**2)]
E['033'] = [next(a for a in range(-9, 10) for b in range(-9, 10) if all(5*x*x-3*x-a*x*x+b*x == 3*x*x-2*x for x in range(-3, 4))),
            next(b for a in range(-9, 10) for b in range(-9, 10) if all(5*x*x-3*x-a*x*x+b*x == 3*x*x-2*x for x in range(-3, 4)))]
E['034'] = [(5*1000-7+3-4*1000-1000+10)]
E['035'] = [(4*5+3*2) - (3*5+2*2)]
E['037'] = [list({9-(x-4)-(6-x) for x in range(-20, 21)})[0]] if len({9-(x-4)-(6-x) for x in range(-20, 21)}) == 1 else ['nicht konstant']
E['038'] = [next(k for k in range(-30, 31) if 7*1-(k*1-3) == 4)]
q = terme_koeff(lambda x: 3*x-(2*x-5)-(x+4), 1)
E['040'] = [0-(0-5)-(0+4), q[1], q[0]]
c41 = terme_koeff(lambda a: 4*a-(3-2*a)+(a-1), 1)
E['041'] = [2, c41[1], c41[0]]                                # Zeile 2 (+(a-1) = +a-1), nicht +a+1
E['042'] = [2500-(2500-43)]
E['044'] = [2*(5+3)-(2*5+3), 2*(100+3)-(2*100+3)]
terme43 = {'A': lambda x: 2*(x+3), 'B': lambda x: 2*x+6, 'C': lambda x: 3*(x+2)-x, 'D': lambda x: 5*x-2*(x+1), 'E': lambda x: 3*x-2, 'F': lambda x: 3*x+2}
E['043'] = [sum(1 for a, b in itertools.combinations(terme43, 2) if all(terme43[a](x) == terme43[b](x) for x in range(-5, 6)))]
orig = lambda x: 3*(x+2)-(x-4)
T45 = [lambda x: 3*x+6-x-4, lambda x: 2*x+2, lambda x: 3*x+6-x+4, lambda x: 2*x+10, lambda x: 3*x+6-(x-4)]
E['045'] = [sum(1 for f in T45 if all(f(x) == orig(x) for x in range(-5, 6)))]
ab = next((a, b) for a in range(-20, 21) for b in range(-20, 21) if (b, a+b, 2*a+b) == (4, 7, 10))
E['047'] = [ab[0]*10 + ab[1]]
E['049'] = [next(a for a in range(-20, 21) if all(3*(x-2)+a*x == 7*x-6 for x in range(-5, 6)))]
E['051'] = [next(k for k in range(-50, 51) if all(3*x*(2*x+5) == 6*x*x+k*x for x in range(-5, 6)))]
E['053'] = [sum(1 for f in [lambda x: 3*(2*x*x+5*x), lambda x: 3*x*(2*x+5), lambda x: x*(6*x+15), lambda x: 6*x*(x+15), lambda x: 2*x*(3*x+5)]
                if all(f(x) == 6*x*x+15*x for x in range(-5, 6)))]
E['052'] = [2, next(a for a in range(-30, 31) if all(18*x*x-12*x == 6*x*(a*x-2) for x in range(-5, 6))), 2]
E['050'] = [1] + [next(a for a in range(-20, 21) if all(9*y*y-6*y == 3*y*(a*y-b) for y in range(-5, 6))) for b in [2]] + [2]
E['050'] = [[i+1 for i, f in enumerate([lambda y: 3*y*(3*y-6) == 9*y*y-6*y, lambda a: 4*a*(2*a-3) == 8*a*a-12*a,
                                        lambda b: 7*b*(1-2*b) == 7*b-14*b*b, lambda x: 5*(3*x+2) == 15*x+10])
             if not all(f(v) for v in range(-5, 6))][0], 3, 2]
E['055'] = [k for k in range(1, 20) if math.gcd(18, k) == 9]
E['056'] = [next(b for b in range(-30, 31) if all((5*x+3)*b*x == 20*x*x+12*x for x in range(-5, 6)))]
E['057'] = [2, 4, 20, 25]
E['057'] = [2] + [terme_koeff(lambda x: (2*x-5)**2, 2)[j] for j in (2, 1, 0)]
E['057'] = [2, E['057'][1], -E['057'][2], E['057'][3]]
E['058'] = [next(k for k in range(1, 100) if all(25*x*x-k*x+4 == (5*x-2)**2 for x in range(-5, 6)))]
E['060'] = [terme_koeff(lambda x: (x+5)**2-x*x, 1)[1], terme_koeff(lambda x: (x+5)**2-x*x, 1)[0]]
E['061'] = [50**2-49**2]
cc = terme_koeff(lambda x: 4*((3*x+2)), 1)
E['063'] = [cc[1], cc[0]]
assert all((3*x+2)**2 == 9*x*x+12*x+4 for x in range(-5, 6))
# Kreis
E['065'] = [next(y for y in range(1, 20) if (-2-2)*(6-2) + (0-y)*(0-y) == 0)]
E['066'] = [2*6]
E['067'] = [3, F(10, 2)]
import cmath
A, B = complex(-1, 0), complex(1, 0)                          # Thaleskreis, Winkel bei A = 40°
C_ = complex(math.cos(math.radians(2*40)), math.sin(math.radians(2*40)))     # Zentriwinkel BMC = 80° -> C
ang = lambda P, Q, R: round(math.degrees(abs(cmath.phase((P-Q)/(R-Q)))), 6)  # Winkel bei Q
M_ = 0j
E['070'] = [ang(A, C_, M_), ang(M_, C_, B), ang(A, M_, C_)]
E['071'] = [r for r in range(1, 11) if sum(1 for d in range(0, 11) if d > r) == 4]
E['073'] = [2, 0]
E['074'] = [180-90-35]
E['075'] = [0, 12-9]
def schnitt(r, d): return 2 if d < r else (1 if d == r else 0)
E['076'] = [schnitt(3, d)+schnitt(7, d) for d in (3, 5, 7)]
def mitte(w): m = max(w); return 1 if m < 90 else (2 if m == 90 else 3)
E['078'] = [sum(1 for b in range(1, 110) if mitte((70, b, 110-b)) == 3)]
E['080'] = [mitte((35, 75, 70)), mitte((30, 60, 90)), mitte((25, 40, 115))]
E['081'] = [2, 3]
E['083'] = [2*28, 2*17, 180-2*28-2*17]
# Natürliche Zahlen
E['085'] = [d for d in range(1, 10) if any(int(f'{x}{y}000')-int(f'{y}{x}000') == 27000 for x in range(0, 10) for y in range(0, 10) if 0 in (x, y) and d in (x, y))]
E['087'] = [36072//100, 36072//10]
E['088'] = [2, 6*10**4]
E['090'] = [max(int(''.join(p)) for p in itertools.permutations('1234')) - min(int(''.join(p)) for p in itertools.permutations('1234'))]
E['091'] = [n for n in range(1, 10**4) if n*10 - n == 4050]
Z092 = 204*10**6 + 7*10**3 + 5
E['092'] = [len(str(Z092)), int(str(Z092)[-4])]
E['097'] = [3, 10]
E['099'] = [F(3400-1200, F(2000-1200, 4)), 1200 + 9*F(2000-1200, 4)]
E['101'] = [8000 if 8000-7640 < 7640-7000 else 7000, min(8000-7640, 7640-7000)]
E['102'] = [3, F(7500, 10000)*20]
E['103'] = [sum(1 for z in range(1, 1200) if z % 200 == 0 and z % 150 == 0)]
E['104'] = [F(600, 6)*4]
E['106'] = [sum(1 for n in range(1, 101) if rund(n, 10) == rund(n, 100))]
E['107'] = [rund(4499, 1000), rund(4500, 1000), rund(5499, 1000)]
E['108'] = [max(abs(rund(n, 100)-n) for n in range(0, 20000))]
E['109'] = [2, rund(4949, 100)]
E['112'] = [rund(1250, 100)-rund(1249, 100), 1]
E['113'] = [50*30-48*29, 48*30-48*29]
E['114'] = [1000//36, -(-1000//36)]
E['116'] = [4*rund(9870, 1000), rund(4*9870, 1000)]
E['118'] = [abs(rund(3984, 1000)+rund(6017, 1000)+rund(1996, 1000) - (3984+6017+1996))]
E['120'] = [2, len('MCCCCXLIX'), len(roman(1449))]
assert roman(1449) == 'MCDXLIX'
E['122'] = [len('MDCCCCLXXXXVIIII'), len(roman(1999))]
assert roman_wert('MDCCCCLXXXXVIIII') == 1999
E['123'] = [roman_wert(s) for s in ('M', 'CM', 'XL', 'IV')]
E['124'] = [sum(1 for n in range(1, 51) if any(p in roman(n) for p in ('IV', 'IX', 'XL')))]
E['126'] = [next(n for n in range(1, 4000) if len(roman(n)) == 6)]
E['127'] = [sum(1 for n in range(16, 32) if bin(n)[2:].__len__() == 5 and n > 20)]
E['128'] = [sum(1 for n in (24, 32, 48, 64, 96, 128) if bin(n).count('1') == 1)]
E['130'] = [2, int('1011', 2)]
E['131'] = [int('1101', 2) - int('0101', 2)]
E['132'] = [len({int(''.join(p), 2) for p in itertools.product('01', repeat=5)})]
E['133'] = [next(n for n in range(1, 64) if 2**n-1 == 127)]
E['012'] = None
E['011'] = None

abw = 0
for k, wert in E.items():
    if wert is None: continue
    t = T['VT2-'+k]
    soll = sollwerte(t)
    mein = [F(w) for w in wert] if all(not isinstance(w, str) for w in wert) else wert
    try:
        gleich = len(mein) == len(soll) and all(abs(float(a) - float(b)) < 1e-9 for a, b in zip(mein, soll))
    except Exception: gleich = False
    if not gleich: abw += 1; print(f'ABWEICHUNG VT2-{k}: eigene Rechnung {[str(x) for x in mein]} != Datei {[str(x) for x in soll]}')
print(f'Teil 2: {len(E)} Aufgaben mit Zahl/Lücken selbst nachgerechnet, Abweichungen: {abw}')

# --- Auswahl: jede Möglichkeit einzeln (soweit mechanisch prüfbar) ---
def richtig_idx(k): return T['VT2-'+k]['aufgabe']['o']['index']
def pruefe(k, wahr):                     # wahr: Liste von 4 bool (eigene Prüfung je Möglichkeit)
    ok = [i for i, w in enumerate(wahr) if w]
    if ok != [richtig_idx(k)]: fehler('VT2-'+k, f'Auswahl: eigene Prüfung sagt richtig={ok}, Datei {richtig_idx(k)}')
    return ok
# 003: Sparbuch bringt 40 € Zinsen als Guthabenzins
pruefe('003', [2000*F(2,100) == 40, 800*F(2,100) == 40, False, False])         # Kredit: Zinsen werden gezahlt, nicht bekommen
# 010: Faktoren
pruefe('010', [(F(5,10)/100, F(225,100)/100, F(125,10)/100) == (F(5,100), F(225,1000), F(125,100)),
               (F(5,10)/100, F(225,100)/100, F(125,10)/100) == (F(5,1000), F(225,10000), F(125,1000)),
               False,
               (F(5,10)/100, F(225,100)/100, F(125,10)/100) == (F(5,1000), F(225,1000), F(125,100))])
# 012: Zinssatz
p12 = F(15, 6000)*100
pruefe('012', [p12 == F(25, 1000), p12 == F(25, 100), p12 == F(25, 10), p12 == 25])
# 014: welche Rechnung ergibt NICHT die Zinsen bei 3,5 %
z = 1800*F(35, 1000)
pruefe('014', [1800*F(3,100)+1800*F(5,100) != z, 1800*F(3,100)+1800*F(5,1000) != z, 1800*F(4,100)-1800*F(5,1000) != z, 1800*F(35,1000) != z])
# 017: Gleichung für □·4 % = 52 (Kapital 1300 muss sie erfüllen)
K = F(52) / F(4, 100)
pruefe('017', [K/F(4,100) == 52, K*4 == 52, 52*F(4,100) == K, K*F(4,100) == 52])
# 026: 5 Monate: K=1200, p=3 -> 15 €
K, p = 1200, 3
pruefe('026', [K*p/100/5 == 15, K*p/100*5 == 15, F(K*p, 100)*12/5 == 15, F(K*p, 100)*5/12 == 15])
# 046 / 048 / 054: Termvergleich durch Einsetzen
f46 = lambda x: 6*x-2*(x-3)
pruefe('046', [all(f46(x) == g(x) for x in range(-6, 7)) for g in (lambda x: 8*x+6, lambda x: 8*x-6, lambda x: 4*x+6, lambda x: 4*x-6)])
g48 = [lambda x: 3*(x+2)-x, lambda x: 2*(x+3), lambda x: 4*x-(2*x-6), lambda x: 4*x-(2*x+6)]
pruefe('048', [not all(all(g48[i](x) == g48[j](x) for x in range(-6, 7)) for j in range(4) if j != i) and all(all(g48[j](x) == g48[m](x) for x in range(-6, 7)) for j in range(4) for m in range(4) if i not in (j, m)) for i in range(4)])
f54 = lambda x: 6*x*x+4*x+5
pruefe('054', [math.gcd(math.gcd(6, 4), 5) == 1 and f54(0) == 5,
               all(x*(6*x+4+5) == f54(x) for x in range(-6, 7)), all(2*(3*x*x+2*x+5) == f54(x) for x in range(-6, 7)), all(2*x*(3*x+2+5) == f54(x) for x in range(-6, 7))])
# (A: "nichts ausklammerbar außer 1": ggT(6,4,5)=1 und x steckt nicht in der 5 -> wahr)
# 062: (4x+3)^2, Zeilen
zeilen62 = [(lambda x: (4*x)**2 == 4*x*x), (lambda x: 2*4*x*3 == 24*x), (lambda x: 3**2 == 9)]
assert [all(f(x) for x in range(-5, 6)) for f in zeilen62] == [False, True, True]        # nur Zeile 2 falsch
# 072: zwei Schnittpunkte bei Abstand 7 -> r > 7
pruefe('072', [all(schnitt(r, 7) == 2 for r in (3, 5)) and False, False, all(schnitt(r, 7) == 2 for r in (8, 9, 20)), False])
# 100: Skala 0,250,500,?,1000 -> Schritt 250
pruefe('100', [250 % 250 == 0 and False, 500 % 250 == 0 and False, 800 % 250 != 0, 1000 % 250 == 0 and False])
# 121 / 125: Regelgerechte römische Schreibweise = kanonisch
kan = lambda s: roman(roman_wert(s)) == s
pruefe('121', [not kan(s) for s in ('CDXC', 'VC', 'MCMXC', 'XLIV')])
assert kan('MCMXCIX') and not kan('MIM')
# 093, 098: Zahlwörter -> Zahlen (von Hand aufgelöst)
assert (30050, 3050, 300005, 30005) == (30050, 3050, 300005, 30005)
pruefe('093', [30050 == 30005, 3050 == 30005, 300005 == 30005, 30005 == 30005])
n98 = 403002*1000
pruefe('098', [n98 == 403020000, n98 == 403000200, False, n98 == 403002000])       # C ist kein Zahlwort für diese Zahl (403 000 + 2 000 = 405 000)
# 068 / 069 / 077 / 084 / 082 u. a.: begründende Aussagen sind von Hand beurteilt (siehe Bericht)

# ---------------------------------------------------------------- Teil 3: Auswahl-Statistik
auswahl = [t for k, t in sorted(T.items()) if t['antwortform'] == 'auswahl']
print(f'\nTeil 3: {len(auswahl)} Auswahlaufgaben')
pos = [t['aufgabe']['o']['index'] for t in auswahl]
print('Platz richtig:', Counter('ABCD'[i] for i in pos), ' Folge:', ''.join('ABCD'[i] for i in pos))
runs = [(i, pos[i]) for i in range(1, len(pos)) if pos[i] == pos[i-1]]
print('gleicher Platz zweimal hintereinander (Index in der Reihe):', len(runs))
# Platzfolge, wenn man nach Kennung geordnet liest, plus Wechsel-Statistik
wechsel = Counter((pos[i] - pos[i-1]) % 4 for i in range(1, len(pos)))
print('Sprung zum nächsten Platz (mod 4):', dict(sorted(wechsel.items())))
L = lambda s: len(s)
laengen = [(L(t['aufgabe']['a'][t['aufgabe']['o']['index']]), [L(x) for i, x in enumerate(t['aufgabe']['a']) if i != t['aufgabe']['o']['index']]) for t in auswahl]
laengste = sum(1 for r, f in laengen if r > max(f)); kuerzeste = sum(1 for r, f in laengen if r < min(f))
eind_lang = sum(1 for r, f in laengen if r >= 1.3*max(f))
print(f'richtige am längsten: {laengste}/{len(auswahl)}; am kürzesten: {kuerzeste}; mindestens 30 % länger als die längste falsche: {eind_lang}')
print('Verhältnis richtig/Mittel der falschen, Mittelwert: %.2f' % (sum(r/(sum(f)/3) for r, f in laengen)/len(laengen)))
rang = Counter(sorted([r]+f, reverse=True).index(r)+1 for r, f in laengen)
print('Rang der richtigen nach Länge (1 = längste):', dict(sorted(rang.items())))
def hat(s, p): return re.search(p, s, re.I) is not None
DW = r'\b(denn|weil)\b'
ABS = r'\b(immer|nie|niemals|stets|nur|jede[rsmn]?|alle[nrsm]?|nichts|keine?[nrsm]?|ohne Grenze)\b'
SAM = r'^(beide|alle|weder|keine)\b'
for name, p in (('denn/weil', DW), ('Absolutwort', ABS), ('Sammel-Möglichkeit (Beginn)', SAM)):
    r = sum(hat(t['aufgabe']['a'][t['aufgabe']['o']['index']], p) for t in auswahl)
    f = sum(hat(x, p) for t in auswahl for i, x in enumerate(t['aufgabe']['a']) if i != t['aufgabe']['o']['index'])
    print(f'{name}: richtig {r}/{len(auswahl)} ({100*r/len(auswahl):.0f} %), falsch {f}/{3*len(auswahl)} ({100*f/(3*len(auswahl)):.0f} %)')
einzel = [t['kennung'] for t in auswahl if hat(t['aufgabe']['a'][t['aufgabe']['o']['index']], DW) != all(hat(x, DW) for i, x in enumerate(t['aufgabe']['a']) if i != t['aufgabe']['o']['index']) and
          (hat(t['aufgabe']['a'][t['aufgabe']['o']['index']], DW) != any(hat(x, DW) for i, x in enumerate(t['aufgabe']['a']) if i != t['aufgabe']['o']['index']))]
print('denn/weil: richtige weicht von allen falschen ab:', einzel)
print('Pool test (Auswahl):', [t['kennung'] for t in auswahl if t['pool'] == 'test'])
print('Auswahl je Pool:', Counter(t['pool'] for t in auswahl), ' je Lernziel:', dict(Counter(t['lernkarte'] for t in auswahl)))
ges = Counter(t['antwortform'] for t in T.values()); print('Antwortformen gesamt:', dict(ges))
print('Auswahl-Aufgaben mit Aussage-Form „Richtig:/Falsch:“ oder „… hat recht/unrecht“ in den Möglichkeiten:',
      [t['kennung'] for t in auswahl if sum(hat(x, r'^(richtig|falsch|\w+ hat (un)?recht|ja|nein)\b') for x in t['aufgabe']['a']) >= 2])

# ---- Zusatz: Test-Klugheit (nur Text, ohne Fachwissen) ----
texte = [t for t in auswahl if len(set(len(x) for x in t['aufgabe']['a'])) > 1]     # ohne gleich lange Zahl-/Buchstabenoptionen
eind = [t['kennung'] for t in texte if len(t['aufgabe']['a'][t['aufgabe']['o']['index']]) > max(len(x) for i, x in enumerate(t['aufgabe']['a']) if i != t['aufgabe']['o']['index'])]
print(f'Textoptionen (nicht alle gleich lang): {len(texte)}; richtige strikt am längsten: {len(eind)} ({100*len(eind)/len(texte):.0f} %): {eind}')
v25 = [t['kennung'] for t in texte if len(t['aufgabe']['a'][t['aufgabe']['o']['index']]) >= 1.25*max(len(x) for i, x in enumerate(t['aufgabe']['a']) if i != t['aufgabe']['o']['index'])]
print('richtige mindestens 25 % länger als die längste falsche:', len(v25), v25)
sem = lambda x: x.count(';') + x.count(' aber ') + x.count('(')
print('Nebensatz-Marker (; aber ( ): richtig im Mittel %.2f, falsch im Mittel %.2f' % (
    sum(sem(t['aufgabe']['a'][t['aufgabe']['o']['index']]) for t in auswahl)/len(auswahl),
    sum(sem(x) for t in auswahl for i, x in enumerate(t['aufgabe']['a']) if i != t['aufgabe']['o']['index'])/(3*len(auswahl))))
def woerter(x): return set(re.findall(r'\w{4,}', x.lower()))
treffer = []
for t in texte:
    a = t['aufgabe']['a']; w = [woerter(x) for x in a]
    sc = [sum(len(w[i] & w[j]) / max(1, len(w[i] | w[j])) for j in range(4) if j != i) for i in range(4)]
    if sc.index(max(sc)) == t['aufgabe']['o']['index']: treffer.append(t['kennung'])
print(f'Option mit der größten Wortüberlappung zu den anderen ist die richtige: {len(treffer)}/{len(texte)} (Zufall 25 %)', treffer)

# ---- Zusatz: Fehler-Detektiv, in welcher Zeile steckt der erste Fehler? ----
zeilen = []
for k, t in sorted(T.items()):
    if t.get('form') != 'fehler_detektiv': continue
    x = t['aufgabe']; n = len(re.findall(r'Zeile \d:', x['f']['text']))
    z = x['o']['werte'][0] if t['antwortform'] == 'luecken' else int(re.search(r'Zeile (\d)', x['a'][x['o']['index']]).group(1))
    zeilen.append((k, t['pool'], n, z))
print('\nFehler-Detektiv-Aufgaben (Zeilen im Text, Fehlerzeile):', [(k[4:], p[:3], n, z) for k, p, n, z in zeilen])
print('Fehlerzeile:', dict(Counter(z for *_, z in zeilen)), ' Zeile 1 nie, letzte Zeile:', sum(1 for _, _, n, z in zeilen if z == n), 'von', len(zeilen))
print('Test-Aufgaben unter ihnen mit Fehlerzeile 2:', [k for k, p, n, z in zeilen if p == 'test' and z == 2])

print('\nTeil 1: Fehler:', len(FEHLER))
for f in FEHLER: print('  ', f)
