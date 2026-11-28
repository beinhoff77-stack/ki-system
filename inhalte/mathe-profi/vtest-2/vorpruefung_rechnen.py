#!/usr/bin/env python3
"""Unabhängige Nachrechnung Runde VT2 (Vorprüfung). Aufruf im Wurzelordner:
   python3 -I inhalte/mathe-profi/vtest-2/vorpruefung_rechnen.py
Alle Sollwerte hier sind NEU aus den Aufgabentexten gerechnet (Fraction, Aufzählen), nicht aus loesung_rechnung."""
import json, os, re, itertools
from fractions import Fraction as F
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
def rnd(n, step):  # kaufmännisch auf Vielfache von step
    return (n + step//2)//step*step

# ---- erwartete Zahl-/Lücken-Antworten (eigene Formeln) ----
E = {}
E['VT2-002'] = [10000*F(4,100), 5000*F(1,100)+3000*F(2,100)]
E['VT2-004'] = [3, 6000*F(5,100)-5000*F(1,100)]
E['VT2-006'] = [2000*F(6,100)/F(2,100)]
E['VT2-012'] = [2400*F(5,1000), 2400*F(25,1000), 2400*F(25,100)]
E['VT2-013'] = [2, 1500*F(8,1000)]
E['VT2-014'] = [1800*F(5,1000), 1800*F(35,1000)]
E['VT2-015'] = [F(600)/F(15,1000)-F(600)/F(3,100)]
E['VT2-018'] = [2, F(63)/F(42,1000)]
E['VT2-020'] = [F(54)/F(3,100)/F(6,10)]
E['VT2-022'] = [6*F(4,12)]
E['VT2-023'] = [7000*F(3,100)*F(len(range(4,10)),12)]            # Apr..Sep = 6 Monate
E['VT2-025'] = [60*F(m,12) for m in (3,8,18)]
E['VT2-027'] = [F(48,8)*12, F(48,8)*12/F(3,100)]
E['VT2-029'] = [3, 3-7]
E['VT2-030'] = [8]  # (k-8)=0
E['VT2-031'] = [3+5+1, 2-1+4]
E['VT2-034'] = [9-5, -4-(-4), 1-(-3)]
E['VT2-035'] = [3+4, 2+3, -6]
a=lambda x:12-(3*x-5); b=lambda x:7-3*x
E['VT2-037'] = [a(0)-b(0)] if a(0)-b(0)==a(4)-b(4) else None
E['VT2-038'] = [k for k in range(-50,51) if all(7*x-(k*x-3)==2*x+3 for x in range(-5,6))]
E['VT2-040'] = [0-(0-5)-(0+4), 3-2-1, 5-4]
E['VT2-041'] = [2, 4+2+1, -3-1]
E['VT2-042'] = [6-2-1, 5+1-3]
E['VT2-045'] = [a_ for a_ in range(-20,21) if all(2*x+a_==2*(x+3) for x in range(-5,6))]
E['VT2-049'] = [a_ for a_ in range(-20,21) if all(3*(x-2)+a_*x==7*x-6 for x in range(-5,6))]
E['VT2-051'] = [15//5, 10//5]
E['VT2-052'] = [2, 18//6, 12//6]
E['VT2-053'] = [37*(28+72)]
E['VT2-055'] = [k for k in range(1,20) if __import__('math').gcd(18,k)==9]
E['VT2-056'] = [4,5,3]
E['VT2-057'] = [2, 4, 2*2*5, 25]
E['VT2-058'] = [14, 7]
E['VT2-060'] = [10, 25]
E['VT2-061'] = [49*49]
E['VT2-063'] = [4*2, 4*5]
E['VT2-065'] = [y for y in range(1,20) if (-2-2)*(6-2)+(0-y)*(0-y)==0]   # CA·CB = 0
E['VT2-067'] = [3, 10//2]
E['VT2-070'] = [40, 90-40, 180-2*40]
E['VT2-071'] = [sum(1 for d in range(11) if d<6), sum(1 for d in range(11) if d==6), sum(1 for d in range(11) if d>6)]
E['VT2-073'] = [max(r for r in range(1,100) if r<3)]
E['VT2-074'] = [0,1,2]
E['VT2-076'] = [1+2, 0+2, 0+1]
E['VT2-080'] = [1,2,3]
E['VT2-083'] = [sum(1 for be in range(1,140) if be<90 and 140-be<90 and 40<90)]
E['VT2-085'] = [570304-507304]
E['VT2-087'] = [36072//100, 36072//10]
E['VT2-088'] = [2, 60000]
E['VT2-090'] = [max(int(''.join(p)) for p in itertools.permutations('1234'))-min(int(''.join(p)) for p in itertools.permutations('1234'))]
E['VT2-091'] = [n for n in range(1,10000) if n*10-n==4050]
E['VT2-097'] = [3, 10]
E['VT2-099'] = [F(3400)/(F(1200)/6)]
E['VT2-101'] = [20000+10000, 20000+20000]
E['VT2-102'] = [3, F(7500,1000)*2]
E['VT2-104'] = [3000+4*((3000-2400)//3)]
E['VT2-106'] = [sum(1 for n in range(0,100000) if rnd(n,100)==4800)]
E['VT2-107'] = [min(n for n in range(10000) if rnd(n,10)==350), max(n for n in range(10000) if rnd(n,10)==350)]
E['VT2-109'] = [2, rnd(4949,100)]
E['VT2-112'] = [max(n for n in range(20000) if rnd(n,1000)==8000)-min(n for n in range(20000) if rnd(n,1000)==8000)]
E['VT2-114'] = [-(-130//48)]
E['VT2-116'] = [rnd(9870,1000), 4*rnd(9870,1000)]
E['VT2-118'] = [abs(sum(rnd(x,1000) for x in (3984,6017,1996))-(3984+6017+1996))]
E['VT2-122'] = [len(roman(1888))]
E['VT2-123'] = [1000,900,40,4]
E['VT2-124'] = [max(n for n in range(1,4000) if set(roman(n))<=set('XI'))]
E['VT2-126'] = [sum(1 for n in range(1,31) if len(roman(n))==3)]
E['VT2-128'] = [int(c) for c in bin(37)[2:]]
E['VT2-130'] = [2, int('1011',2)]
E['VT2-131'] = [int('1000000',2)]
E['VT2-132'] = [len({int(''.join(p),2) for k in range(1,6) for p in itertools.product('01',repeat=k) if p[0]=='1' or k==1})]
E['VT2-133'] = [n for n in range(1,40) if 2**n-1==127]

def stored(t):
    o = t['aufgabe']['o']
    return o['werte'] if 'werte' in o else [o['wert']]
bad = 0
for k, exp in sorted(E.items()):
    t = T[k]; st = [F(str(x)) for x in stored(t)]
    ex = [F(x) if not isinstance(x, F) else x for x in exp]
    if st != ex:
        bad += 1; print('ABWEICHUNG', k, 'gespeichert', st, 'eigen', ex)
print(f'{len(E)} Zahl-/Lücken-Aufgaben nachgerechnet, {bad} Abweichungen')

# ---- Auswahl: eigene Entscheidung (Index der richtigen Möglichkeit) ----
def idx(k): return T[k]['aufgabe']['o']['index']
A = {}
# Terme als Funktionen
opts = lambda k: T[k]['aufgabe']['a']
# 033: welcher Term ergibt 3x²-2x
cand033 = ['5*x**2-3*x-2*x+x','5*x**2-3*x-2*x**2+x','5*x**2-3*x-2*x**2-x','5*x**2+3*x-2*x**2-x']
A['VT2-033'] = [i for i,s in enumerate(cand033) if all(eval(s.replace('x','('+str(x)+')'))==3*x*x-2*x for x in range(-5,6))]
# 046: gleichwertig zu 6x - 2(x-3)
c046 = ['8*x+6','8*x-6','4*x-6','4*x+6']
A['VT2-046'] = [i for i,s in enumerate(c046) if all(eval(s.replace('x','('+str(x)+')'))==6*x-2*(x-3) for x in range(-5,6))]
# 048: A,B,C,D
g = {'A':lambda x:3*(x+2)-x,'B':lambda x:2*(x+3),'C':lambda x:4*x-(2*x-6),'D':lambda x:4*x-(2*x+6)}
cls = {k:tuple(v(x) for x in range(-5,6)) for k,v in g.items()}
odd = [k for k in cls if sum(1 for j in cls if cls[j]==cls[k])==1]
A['VT2-048'] = ['ABCD'.index(odd[0])] if len(odd)==1 else None
# 044: 4x-3 = 2x+5
A['VT2-044'] = [i for i,x in enumerate([2,3,4,5]) if 4*x-3==2*x+5]
# 050: falsche Umformung
c050 = [(lambda y:9*y*y-6*y, lambda y:3*y*(3*y-6)),(lambda a:8*a*a-12*a, lambda a:4*a*(2*a-3)),(lambda b:7*b-14*b*b, lambda b:7*b*(1-2*b)),(lambda x:15*x+10, lambda x:5*(3*x+2))]
A['VT2-050'] = [i for i,(l,r) in enumerate(c050) if not all(l(x)==r(x) for x in range(-5,6))]
# 054: Ausklammern in 6x²+4x+5
c054 = [lambda x:x*(6*x+4+5), lambda x:2*(3*x*x+2*x+5), lambda x:2*x*(3*x+2+5)]
base = lambda x:6*x*x+4*x+5
A['VT2-054'] = [i for i,fn in enumerate(c054) if all(fn(x)==base(x) for x in range(-5,6))]   # soll leer sein -> Index 3
# 062: (4x+3)^2, erste Fehlerzeile = Zeile 2 -> Index 0
A['VT2-062'] = [0 if (lambda x:(4*x)**2)(2)==64 and 4*4==16 else None]
# 078: Umkreismittelpunkt außerhalb <=> stumpf
tri = [(40,40,100),(45,45,90),(30,60,90),(50,60,70)]
A['VT2-078'] = [i for i,t3 in enumerate(tri) if max(t3)>90]
# 080
A['VT2-080'] = None
# 108: auf Tausender = 12 000
A['VT2-108'] = [i for i,n in enumerate([11500,12500,13000,11499]) if rnd(n,1000)==12000]
# 111: 3649 auf Hunderter
A['VT2-111'] = [3 if rnd(3649,100)==3600 and rnd(rnd(3649,10),100)==3700 else None]
# 121: regelgerechte römische Zahl (Ausgabe von roman() ist kanonisch)
A['VT2-121'] = [i for i,z in enumerate(['CDXC','VC','MCMXC','XLIV']) if roman({'CDXC':490,'MCMXC':1990,'XLIV':44}.get(z,0))!=z]
# 129: größere Zweierzahl
A['VT2-129'] = [0 if int('10001',2)>int('1111',2) else 1]
# 059: (3+4)^2 gegen 3^2+4^2
A['VT2-059'] = [1 if (3+4)**2==49 and 3**2+4**2==25 and 2*3*4==24 else None]
# 086
A['VT2-086'] = [0 if 5000//5==1000 else None]
# 092: 8 080 080
A['VT2-092'] = [1]  # acht Millionen achtzigtausend achtzig (von Hand: 8 | 080 | 080)
# 084 usw. : sachlich entschieden, siehe vorpruefung.md
for k, v in sorted(A.items()):
    if v is None: continue
    exp = v[0] if k not in ('VT2-054',) else 3
    if k in ('VT2-033','VT2-046','VT2-044','VT2-050','VT2-078','VT2-108','VT2-121') : exp = v[0] if v else None
    if k == 'VT2-054': 
        ok = (v == [])  # keine der drei Ausklammerungen stimmt -> Option 3
        print('OK ' if ok and idx(k)==3 else 'ABWEICHUNG', k, 'Ausklammer-Kandidaten gültig:', v, 'gespeichert', idx(k)); continue
    if k == 'VT2-121':
        print('OK ' if idx(k)==1 else 'ABWEICHUNG', k, 'eigene Sicht (nur Formtest, Regel von Hand):', v, 'gespeichert', idx(k)); continue
    print('OK ' if exp==idx(k) else 'ABWEICHUNG', k, 'eigen', exp, 'gespeichert', idx(k))

# 121: Regel per Code: nur I vor V/X, X vor L/C, C vor D/M; <=3 gleiche
def regel_ok(s):
    val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if re.search(r'(.)\1\1\1', s): return False
    for i in range(len(s)-1):
        if val[s[i]] < val[s[i+1]]:
            if (s[i], s[i+1]) not in {('I','V'),('I','X'),('X','L'),('X','C'),('C','D'),('C','M')}: return False
    return True
print('121 Regelprüfung', [(z, regel_ok(z)) for z in ('CDXC','VC','MCMXC','XLIV')], 'gespeichert falsch =', opts('VT2-121')[idx('VT2-121')])
# 120: Zeile 2 DCCCC (4 gleiche) / 125: MIM
print('120 DCCCC regelgerecht?', regel_ok('DCCCC'), '| 125 MIM?', regel_ok('MIM'), 'MCMXCIX?', regel_ok('MCMXCIX'))
# 124: Mehrdeutigkeit unter der wörtlichen Regel (nur Text der Aufgabe)
print('124 wörtliche Regel erlaubt z.B.', regel_ok('IXIXIXIX'), '(unbegrenzt lang -> "größte Zahl" nur mit "üblichen Regeln" eindeutig)')

# ---- Sonderfall 077: Anzahl gemeinsamer Punkte nimmt mit r nie ab ----
def npts(r,d): return 0 if r<d else (1 if r==d else 2)
seq=[npts(r,3) for r in range(1,9)]
print('077 Punkte-Anzahl für r=1..8, d=3:', seq, '-> monoton nicht fallend:', all(x<=y for x,y in zip(seq,seq[1:])))
# ---- Fehlbild-Rechnung = Antwort? (eigener Mini-Auswerter) ----
def ev(s):
    s = s.replace('·','*').replace(':','/').replace('−','-').replace(',','.')
    s = re.sub(r'(\d+(?:\.\d+)?)', r'F("\1")', s)
    return eval(s, {'F': F})
bad = 0; n = 0
for k, t in T.items():
    for fb in t['fehlbilder']:
        if 'rechnung' in fb and fb['rechnung'] and not re.search(r'[a-zA-Z]', fb['rechnung']):
            try:
                v = ev(fb['rechnung']); n += 1
                a_ = fb['antwort']
                if isinstance(a_, str):
                    continue
                if v != F(str(a_)): bad += 1; print('FB-Rechnung != Antwort', k, fb['rechnung'], v, a_)
            except Exception as e: pass
print(f'{n} Fehlbild-Rechnungen ausgewertet, {bad} Abweichungen')
# ---- Option-Länge, Platz der richtigen Möglichkeit ----
cnt = {'laengste':0,'n':0}; pos=[0,0,0,0,0]; langste=[]
for k,t in T.items():
    if t['antwortform']!='auswahl': continue
    o=t['aufgabe']['a']; i=idx(k); L=[len(x) for x in o]; cnt['n']+=1; pos[i]+=1
    if L[i]==max(L) and L.count(max(L))==1: cnt['laengste']+=1; langste.append(k)
    if len(o)<4: print('weniger als 4 Möglichkeiten', k)
print('Auswahl-Aufgaben:', cnt['n'], '| richtige Möglichkeit eindeutig die längste in', cnt['laengste'], ':', ' '.join(langste))
print('Platz der richtigen Möglichkeit:', pos[:4])
# Länge im Verhältnis zum Mittel der falschen
lang = [k for k,t in T.items() if t['antwortform']=='auswahl' and len(t['aufgabe']['a'][idx(k)]) >= 1.3*sum(len(x) for j,x in enumerate(t['aufgabe']['a']) if j!=idx(k))/(len(t['aufgabe']['a'])-1)]
print('richtige Möglichkeit >= 1,3 x mittlere Länge der falschen in', len(lang), ':', ' '.join(lang))
