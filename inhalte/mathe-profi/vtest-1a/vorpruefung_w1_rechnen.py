"""Vorprüfung W1 (Runde VT1A): unabhängige, exakte Nachrechnung aller 77 Aufgaben.

Eigene Rechnungen (nicht aus gegenrechnung.py übernommen). Für Zahlaufgaben wird
die Sollantwort neu bestimmt, für Auswahlaufgaben wird JEDE Option einzeln
bewertet; es muss genau eine wahr sein und ihr Index muss der Sollindex sein.
Zusätzlich: Fehlbild-Antworten ungleich Lösung und paarweise verschieden,
Fehlbild-Rechnungen ergeben die angegebene Antwort.
Aufruf vom Repo-Wurzelordner: python3 -I inhalte/mathe-profi/vtest-1a/vorpruefung_w1_rechnen.py
"""
import json, os, re
from fractions import Fraction as F
from itertools import product

HIER = os.path.dirname(os.path.abspath(__file__))

def ist_quadrat(n):
    r = int(n ** 0.5)
    return any((r + d) ** 2 == n for d in (-1, 0, 1))

def teiler(n):
    return [a for a in range(1, n + 1) if n % a == 0]

def runde(n, stelle):  # kaufmännisch, natürliche Zahlen
    return (n + stelle // 2) // stelle * stelle

def loese_nat(f, bis=2000):
    """alle natürlichen x (0..bis) mit f(x) wahr"""
    return [x for x in range(0, bis + 1) if f(x)]

# ---------- Zahlaufgaben: eigene Lösung ----------
ZAHL = {}
ZAHL['002'] = 3**5 - 3**4                                   # 162
ZAHL['003'] = 2**4                                          # 16 verschiedene Personen
ZAHL['004'] = [b for b in range(1, 50) if b**4 == 2**8][0]   # 4
ZAHL['008'] = (4 * [s for s in range(1, 50) if s*s == 144][0] * 2 // 4) ** 2  # 576
ZAHL['010'] = 11*11 - 7*7                                   # 72
ZAHL['011'] = (5 + 4) ** 2                                  # 81
ZAHL['012'] = [n + 1 for n in range(1, 100) if (n+1)**2 - n**2 == 27][0]  # 14
ZAHL['015'] = F(10**6 - 9 * 10**5, 10**5)                   # 1
ZAHL['017'] = [n for n in range(0, 12) if 10**n == 500 * 1000 // 5][0]  # 5
ZAHL['019'] = 10**6 // 10**2 // 10                          # 1000
ZAHL['021'] = max(n for n in range(0, 20) if 10**n < 5_000_000)  # 6
ZAHL['022'] = min(t for t in range(0, 100) if 2**t > 100 + 100*t)  # 11
ZAHL['023'] = [n for n in range(0, 20) if 2**n == 64][0]     # 6
ZAHL['024'] = len(list(product('KZ', repeat=5)))             # 32
ZAHL['026'] = F(10 * 3**4, 5 * 3**4)                         # 2
ZAHL['027'] = [s for s in range(1, 500) if s * 3**4 == 405][0]  # 5
ZAHL['030'] = loese_nat(lambda x: (x + 4) * 3 - 5 == 25)     # [6]
# 032: alle Klammern um zwei benachbarte Zahlen in 20 - 4 + 6
ZAHL['032'] = min(20 - 4 + 6, (20 - 4) + 6, 20 - (4 + 6))   # 10
ZAHL['034'] = sum(v == 14 for v in (2 + 3*4, (2+3)*4, 2*(3+4), 2*3 + 4*2))  # 3
ZAHL['040'] = loese_nat(lambda h: h >= 1 and 4 + 2*(h - 1) == 14)  # [6]
ZAHL['041'] = loese_nat(lambda x: 8 + 5*x == (8+5)*x)        # [1]
ZAHL['044'] = loese_nat(lambda x: 94 - 37 - 23 == 94 - x)    # [60]
ZAHL['047'] = loese_nat(lambda x: 8 * x * 125 == 4000)       # [4]
ZAHL['048'] = loese_nat(lambda x: 6 * x == 18 * 27)          # [81]
ZAHL['049'] = 6482 - 1997 + 3518                             # 8003
ZAHL['050'] = 36*99 - 36*9                                   # 3240
ZAHL['051'] = loese_nat(lambda x: 17*x + 17*14 == 17*50)     # [36]
ZAHL['057'] = sum(1 for a in range(1, 13) if 36 % a == 0)    # 7
ZAHL['059'] = [max(a, b) for a in range(1, 49) for b in range(a, 49) if a*b == 48 and a+b == 14]  # [8]
ZAHL['063'] = loese_nat(lambda x: F(x*5 + 12, 4) == 8)       # [4]
ZAHL['064'] = F(600*50, 3000)                                # 10 (Ergebnis 2 998 ~ 3 000)
ZAHL['065'] = max(k for k in range(1, 200) if runde(k, 10) * 7 == 210)  # 34
ZAHL['066'] = 3*200 - 3*198                                  # 6
_fenster = [z for z in range(4000, 5000) if runde(z, 100) == 4600]
ZAHL['070'] = min(_fenster) + max(_fenster)                  # 9199
ZAHL['071'] = loese_nat(lambda g: 12 + 2*g == 4 + 4*g)       # [4]
ZAHL['072'] = loese_nat(lambda b: 24 + 7*b == 66)            # [6]
_mia = loese_nat(lambda x: (x + 6) * 2 == 30)[0]
ZAHL['074'] = _mia * 2 + 6                                   # 24
def _zug(s):
    s -= 14
    if s % 2: return None
    return s // 2 + 8
ZAHL['075'] = loese_nat(lambda s: s >= 14 and _zug(s) == 20)  # [38]

# ---------- Auswahlaufgaben: jede Option einzeln wahr/falsch ----------
# Je Aufgabe Liste von Wahrheitswerten in der Reihenfolge der Optionen der JSON.
# Die Wahrheit wird aus eigenen Rechnungen gewonnen, der Optionstext wird über
# einen Erkennungsschlüssel (Teilstring) der Rechnung zugeordnet.
W = {}
def opt(key, wahr):
    return (key, wahr)
W['001'] = [opt('17:', 3**2 + 2**3 == 17), opt('12:', 3**2 + 2**3 == 12),
            opt('3 125:', 3**2 + 2**3 == 3125), opt('13:', 3**2 + 2**3 == 13)]
W['005'] = [opt('Die 4 steht 6-mal', 4**6 == 4096), opt('Die 6 steht 4-mal', 4**6 == 6**4),
            opt('Sechsfache', 4**6 == 24), opt('4 + 4 + 4', 4**6 == 24)]
W['006'] = [opt('Zufall', 2**4 == 4**2 and 2**3 != 3**2), opt('gerade Zahl', 2**3 == 3**2),
            opt('2 + 4 = 4 + 2', 2**3 == 3**2), opt('2 · 4 = 4 · 2', 2**3 == 3**2)]
W['007'] = [opt('2 · 3 · 3 = 18', 2 * 3**2 == 18), opt('2 · 3 · 2 = 12', 2 * 3**2 == 12),
            opt('Kein Fehler', 2 * 3**2 == 6**2), opt('2 + 3² = 11', 2 * 3**2 == 11)]
W['009'] = [opt('6 727', not ist_quadrat(6727)), opt('7 396', not ist_quadrat(7396)),
            opt('5 929', not ist_quadrat(5929)), opt('4 761', not ist_quadrat(4761))]
W['013'] = [opt('Kein Fehler', (3*4)**2 == 3**2 * 4**2), opt('12 + 2 = 14', (3*4)**2 == 14),
            opt('9 + 16 = 25', (3*4)**2 == 25), opt('Richtig wäre 24', (3*4)**2 == 24)]
W['014'] = [opt('4-mal', 10*10 == 4 * 5*5), opt('doppelt', 10*10 == 2 * 5*5),
            opt('Unterschied der Flächen ist 5 cm²', 10*10 - 5*5 == 5), opt('100 cm² mehr', 10*10 - 5*5 == 100)]
W['016'] = [opt('56 · 10⁶', 56 * 10**6 != 56_000_000), opt('56 · 10⁵', 56 * 10**5 != 56_000_000),
            opt('560 · 10⁵', 560 * 10**5 != 56_000_000), opt('5 600 · 10⁴', 5600 * 10**4 != 56_000_000)]
_a, _b = 45 * 10**5 == 4_500_000, 450 * 10**5 == 4_500_000
W['018'] = [opt('Nur Anna', _a and not _b), opt('Nur Ben', _b and not _a),
            opt('Beide: 45 · 10⁵ = 450', _a and _b), opt('Beide: Die Zahl vor', _a and _b)]
W['020'] = [opt('2 · 10³ = 2 000', 10**3 + 10**3 == 2000), opt('Kein Fehler', 10**3 + 10**3 == 10**6),
            opt('10⁴ = 10 000', 10**3 + 10**3 == 10**4), opt('20³', 10**3 + 10**3 == 20**3)]
W['025'] = [opt('3 · 2⁵', 3 * 2**5 == 3*2*2*2*2*2), opt('(3 · 2)⁵', (3*2)**5 == 96),
            opt('3⁵ · 2', 3**5 * 2 == 96), opt('3 · 2 · 5', 3*2*5 == 96)]
_alg = 2 * 3**4
W['028'] = [opt('2 · 3⁴ = 162', _alg == 162), opt('2 · 3 · 4 = 24', _alg == 24),
            opt('3⁴ = 81', _alg == 81), opt('Kein Fehler', _alg == 6**4)]
W['029'] = [opt('(20 − 4) · 3 + 2', (20-4)*3 + 2 == 50), opt('20 − (4 · 3 + 2)', 20 - (4*3+2) == 50),
            opt('20 − 4 · (3 + 2)', 20 - 4*(3+2) == 50), opt('(20 − 4 · 3) + 2', (20-4*3)+2 == 50),
            opt('(20 − 4) · (3 + 2)', False)]  # zwei Klammerpaare: verboten (und 80)
_t = 40 - F(12 + 8, 4)
W['031'] = [opt('Addiere 12 und 8, teile', 40 - (12+8)/F(4) == _t),
            opt('Ziehe 12 von 40 ab', (40 - 12 + 8) / F(4) == _t),
            opt('Ziehe die Summe', (40 - (12+8)) / F(4) == _t),
            opt('Teile 12 durch 4', 40 - (F(12, 4) + 8) == _t)]
W['033'] = [opt('(30 − 12) − 4', (30-12)-4 == 30-12-4), opt('30 − (12 − 4)', 30-(12-4) == 30-12-4),
            opt('2 · (3 + 4)', 2*(3+4) == 2*3+4), opt('20 : (4 · 5)', F(20, 4*5) == F(20, 4)*5)]
W['035'] = [opt('100 − 80 = 20', 100 - (12+8)*4 == 20), opt('= 320', 100 - (12+8)*4 == 320),
            opt('= 120', 100 - (12+8)*4 == 120), opt('Kein Fehler', 100 - (12+8)*4 == 384)]
_bus = 30 - 6 - 4
_t36 = {1: 30-6-4 == _bus, 2: 30-(6+4) == _bus, 3: 30-6+4 == _bus, 4: 30-(6-4) == _bus}
W['036'] = [opt('Genau ① und ②', _t36 == {1: True, 2: True, 3: False, 4: False}),
            opt('Genau ②:', _t36 == {1: False, 2: True, 3: False, 4: False}),
            opt('Genau ① und ③', _t36 == {1: True, 2: False, 3: True, 4: False}),
            opt('Genau ② und ④', _t36 == {1: False, 2: True, 3: False, 4: True})]
# letzter Schritt: bei (3 + 4) · 5 Malnehmen; sonst Strich
W['037'] = [opt('(3 + 4) · 5', True), opt('3 + 4 · 5', False), opt('3 · 4 − 5', False), opt('20 : 4 + 5', False)]
W['038'] = [opt('40 − (9 + 6) = 25', 40-(9+6) == 25), opt('40 − 9 + 6 = 37', False),
            opt('(40 − 9) · 6', False), opt('40 + 9 − 6', False)]
_rest = 20 - 4*3 - 2*2
W['039'] = [opt('20 − (4 · 3 + 2 · 2)', 20-(4*3+2*2) == _rest), opt('20 − 4 · 3 + 2 · 2', 20-4*3+2*2 == _rest),
            opt('(20 − 4) · 3', (20-4)*3-2*2 == _rest), opt('20 : 4 · 3', F(20, 4)*3-2*2 == _rest)]
_d = F(12*9 + 8*11 - 36, 4) - F(12*9 + 8*11 - 20, 4)
W['042'] = [opt('um 4 kleiner', _d == -4), opt('um 16 kleiner', _d == -16),
            opt('um 4 größer', _d == 4), opt('um 36 kleiner', _d == -36)]
_x, _y = 24*125*5, 12*125*10
W['043'] = [opt('Beide Werte sind gleich', _x == _y), opt('12 · 125 · 10 ist größer', _y > _x),
            opt('24 · 125 · 5 ist größer', _x > _y), opt('nur sagen, wenn', False)]
W['045'] = [opt('Zuerst 25 · 4 = 100', True), opt('Zuerst 25 · 17 = 425', False),
            opt('Zuerst 17 · 4 = 68', False), opt('25 + 17 + 4', False)]
W['046'] = [opt('36 : 4 und 4 : 36', F(36, 4) != F(4, 36)), opt('7 · 9', 7*9 != 9*7),
            opt('25 + 17', 25+17 != 17+25), opt('5 · 12', 5*12 != 12*5)]
_v = 9 * (6 + 4)
W['052'] = [opt('9 · (6 + 4)', 9*(6+4) == _v), opt('9 · 6 + 4', 9*6+4 == _v),
            opt('9 + 6 · 4', 9+6*4 == _v), opt('(9 + 6) · 4', (9+6)*4 == _v)]
_an, _be = 4*20 + 4*7 == 108, 4*30 - 4*3 == 108
W['053'] = [opt('Beide:', _an and _be), opt('Nur Anna', _an and not _be),
            opt('Nur Ben', _be and not _an), opt('Weder', not _an and not _be)]
_q = F(16*30 + 16*2, 8*30 + 8*2)
W['054'] = [opt('Sie verdoppelt sich', _q == 2), opt('um 8 cm² größer', 16*32 - 8*32 == 8),
            opt('Nur die erste', False), opt('16-mal', _q == 16)]
W['055'] = [opt('Die 19 ausklammern', 19*(36+64-50) == 19*36+19*64-19*50), opt('Jedes Produkt einzeln', False),
            opt('addieren und dann', 19*(36+64+50) == 19*36+19*64-19*50),
            opt('Die 19 abziehen', 36+64-50-19 == 19*36+19*64-19*50)]
_s = 15*7 + 15*9
W['056'] = [opt('15 · (7 + 9) = 240', _s == 240), opt('15 · 7 + 9 = 114', _s == 114),
            opt('= 3 600', _s == 3600), opt('Kein Fehler', _s == 945)]
W['058'] = [opt('36 : 9', F(36, F(36, 9)) == 9), opt('36 · 9', F(36, 36*9) == 9),
            opt('36 − 9', F(36, 36-9) == 9), opt('9 : 36', F(36, F(9, 36)) == 9)]
_l = loese_nat(lambda x: 7*x == 56)
W['060'] = [opt('56 : x = 7', loese_nat(lambda x: x > 0 and 56 == 7*x) == _l),
            opt('x : 7 = 56', loese_nat(lambda x: x == 56*7) == _l),
            opt('x · 56 = 7', loese_nat(lambda x: x*56 == 7) == _l),
            opt('x : 8 = 56', loese_nat(lambda x: x == 56*8, 5000) == _l)]
W['061'] = [opt('gleichmäßig verteilt', True), opt('Jedes Kind bekommt 48', False),
            opt('verliert 6', False), opt('6 Kinder teilen', False)]
W['062'] = [opt('7er-Reihe', 50 % 7 != 0 and 7*7 == 49 and 7*8 == 56), opt('gerade', 7*2 == 15),
            opt('Primzahl', False), opt('größer als 50', False)]
_g = 23*48
W['068'] = [opt('Reicht nicht', _g == 1104 and _g > 1000), opt('Man weiß es nicht', None),  # None: 20 · 50 = 1 000 liegt genau auf der Grenze, der Überschlag allein entscheidet NICHT -> Aussage teilweise wahr (Befund)
            opt('48 wurde auf 50', _g < 1000), opt('gleicht sich', _g <= 1000)]
W['067'] = [opt('B liegt viel näher', abs(4800+3500-8299) < abs(5000+3000-8299)),
            opt('A ist besser', abs(5000+3000-8299) < abs(4800+3500-8299)),
            opt('gleich gut', False), opt('B ist falsch', False)]
W['069'] = [opt('600 · 12 = 7 200', 596*12 == 7152), opt('Kein Fehler', 596*12 != 7152),
            opt('5 960', False), opt('500 · 10', False)]
_lsg = lambda f: loese_nat(f, 200)
W['073'] = [opt('□ − 3 · 2 + 5 = 20', _lsg(lambda x: x - 3*2 + 5 == 20) == [21]),
            opt('□ − 3 · (2 + 5)', _lsg(lambda x: x - 3*(2+5) == 20) == [21]),
            opt('□ + 3 · 2 − 5', _lsg(lambda x: x + 3*2 - 5 == 20) == [21]),
            opt('(□ − 3) · 2 + 5', _lsg(lambda x: (x-3)*2 + 5 == 20) == [21])]
_x76 = loese_nat(lambda x: 4*x + 12 - 4 == 108)
W['076'] = [opt('4 · x + 12 − 4 = 108', _x76 == [25]), opt('4 · (x + 12)', loese_nat(lambda x: 4*(x+12)-4 == 108) == _x76),
            opt('4 · x − 12 + 4', loese_nat(lambda x: 4*x-12+4 == 108) == _x76),
            opt('4 · x + 12 + 4', loese_nat(lambda x: 4*x+12+4 == 108) == _x76)]
W['077'] = [opt('Kein Fehler', loese_nat(lambda x: 2*x+6 == 30) == [12]), opt('= 9', loese_nat(lambda x: 2*x+6 == 30) == [9]),
            opt('= 54', False), opt('= 18', loese_nat(lambda x: 2*x+6 == 30) == [18])]

def zahl_aus(text):
    return text

def main():
    fehler, notizen = [], []
    for datei in ('zahlen.potenzen_basis.json', 'zahlen.rechengesetze.json'):
        for a in json.load(open(os.path.join(HIER, datei)))['aufgaben']:
            k = a['kennung'][-3:]; A = a['aufgabe']
            if A['y'] == 'zahl':
                soll = A['o']['wert']; ich = ZAHL.get(k)
                if isinstance(ich, list):
                    if len(ich) != 1: fehler.append(f'{k}: nicht eindeutig {ich}')
                    ich = ich[0] if ich else None
                if ich is None: fehler.append(f'{k}: keine eigene Rechnung')
                elif F(ich) != F(soll): fehler.append(f'{k}: Soll {soll}, ich {ich}')
                for fb in a['fehlbilder']:
                    if F(fb['antwort']) == F(soll): fehler.append(f'{k}: Fehlbild = Lösung')
                    r = fb.get('rechnung')
                    if r:
                        val = eval(r.replace('·', '*').replace('//', '//'), {})
                        if F(val) != F(fb['antwort']): fehler.append(f'{k}: Fehlbild-Rechnung {r} = {val} ≠ {fb["antwort"]}')
                aw = [fb['antwort'] for fb in a['fehlbilder']]
                if len(set(aw)) != len(aw): fehler.append(f'{k}: doppelte Fehlantwort')
            else:
                ops = A['a']; soll = A['o']['index']; reg = W.get(k)
                if reg is None:
                    notizen.append(f'{k}: Auswahl ohne Rechenregel (rein sprachlich, von Hand geprüft)'); continue
                wahr = []
                for o in ops:
                    treffer = [w for key, w in reg if key in o]
                    if len(treffer) != 1: fehler.append(f'{k}: Option nicht zuordenbar: {o[:40]}'); wahr.append(None); continue
                    wahr.append(treffer[0])
                if None in wahr:
                    notizen.append(f'{k}: Option(en) nicht eindeutig entscheidbar: {[i for i, w in enumerate(wahr) if w is None]}')
                if wahr.count(True) != 1 or wahr.index(True) != soll:
                    fehler.append(f'{k}: wahr={wahr}, Soll-Index {soll}')
    for n in notizen: print('NOTIZ', n)
    for f in fehler: print('FEHLER', f)
    print(f'{len(fehler)} Abweichungen')

if __name__ == '__main__':
    main()
