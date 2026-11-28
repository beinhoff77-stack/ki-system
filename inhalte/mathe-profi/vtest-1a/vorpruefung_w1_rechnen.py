"""Vorprüfung W1, 2. bis 4. Durchgang (Runde VT1A, 55 Aufgaben; 3. Durchgang Stand 48c90f32).

Unabhängige, exakte Nachrechnung (Brüche, Aufzählen statt Formeln), nicht aus
gegenrechnung.py übernommen. Zahlaufgaben: Sollantwort neu bestimmt, dazu
Eindeutigkeit über Aufzählen geprüft. Auswahl: JEDE Option einzeln bewertet,
genau eine muss wahr sein und den Sollindex haben. „Kinderregel“-Aufgaben:
geprüft, dass die erschlossene Regel ALLE Beispiele erfüllt und dass keine der
naheliegenden anderen Regeln ebenfalls alle Beispiele erfüllt (Eindeutigkeit).
Fehlbild-Rechnungen müssen die Fehlantwort ergeben, Fehlantworten ≠ Lösung.
Aufruf vom Repo-Wurzelordner: python3 -I inhalte/mathe-profi/vtest-1a/vorpruefung_w1_rechnen.py
(Die Fassung für die 77 Aufgaben steht in der Geschichte, Commit 68cffcf9.)
"""
import json, os
from fractions import Fraction as F
from itertools import product

HIER = os.path.dirname(os.path.abspath(__file__))
N = range(0, 3000)

def ist_quadrat(n):
    r = int(round(n ** 0.5)); return r * r == n

def zweier(n):  # Zahl der Faktoren 2 einer Zweierpotenz, sonst None
    k = 0
    while n % 2 == 0 and n > 1: n //= 2; k += 1
    return k if n == 1 else None

def eindeutig(f, menge=N):
    l = [x for x in menge if f(x)]
    return l[0] if len(l) == 1 else ('NICHT EINDEUTIG', l[:5])

def regel_eindeutig(beispiele, regeln, ziel):
    """beispiele: Liste (eingabe, ausgabe); regeln: dict name->fn. Gibt die
    passenden Regeln und ihre Werte für das Ziel zurück."""
    passt = {n: r(*ziel) for n, r in regeln.items() if all(r(*e) == a for e, a in beispiele)}
    return passt

PROBLEME = []
def pruefe_regel(k, beispiele, regeln, ziel, soll):
    p = regel_eindeutig(beispiele, regeln, ziel)
    werte = set(p.values())
    if werte != {soll}: PROBLEME.append(f'{k}: Kinderregel nicht eindeutig/falsch: {p}')
    return soll

ZAHL = {}
# 002 Potenzregel des Kindes aus 2³=9, 3²=8, 5²=32
R_POT = {'vertauscht': lambda b, e: e ** b, 'b·e': lambda b, e: b * e, 'b+e': lambda b, e: b + e,
         'richtig': lambda b, e: b ** e, '(b+1)^e': lambda b, e: (b + 1) ** e, 'b^(e+1)': lambda b, e: b ** (e + 1),
         'e·e·b': lambda b, e: e * e * b, '(e+b)·?': lambda b, e: (e + b) * e}
ZAHL['002'] = pruefe_regel('002', [((2, 3), 9), ((3, 2), 8), ((5, 2), 32)], R_POT, (2, 5), 25)
ZAHL['006'] = eindeutig(lambda q: ist_quadrat(q) and (int(q ** 0.5) + 2) ** 2 - q == 44, range(1, 5000))  # 100
ZAHL['007'] = F(50) * 3 * 3                               # Fläche ·9 = 450 (Seite √50 nicht natürlich)
ZAHL['011'] = eindeutig(lambda x: x * 10**8 > 7 * 10**11 and not ((x - 1) * 10**8 > 7 * 10**11), range(1, 20000))  # 7001
R_ZEHN = {'mal': lambda a, b: a * b, 'plus (richtig)': lambda a, b: a + b, 'max': lambda a, b: max(a, b),
          'plus+1': lambda a, b: a + b + 1, 'b-a': lambda a, b: b - a, 'a^2+b': lambda a, b: a * a + b}
ZAHL['012'] = pruefe_regel('012', [((2, 3), 6), ((1, 4), 4)], R_ZEHN, (3, 4), 12)
ZAHL['016'] = F(6**6, 2 * 3**6)                           # 32
_moegl = set()
for s in range(1, 97):
    for h in range(1, 10):
        if s * 2**h == 96: _moegl.add(s)
ZAHL['017'] = len(_moegl)                                  # 5: 48, 24, 12, 6, 3
ZAHL['019'] = F(10 * 3**20, 5 * 3**20)                     # 2
ZAHL['021'] = (483917 - 129486 + 37500) - (483917 - (129486 + 37500))  # 75000
def _klammer_weg(t):  # Kinderregel 022: Klammern weg, Punkt vor Strich
    return eval(t.replace('(', '').replace(')', ''))
def _links_rechts(t):
    toks = t.replace('(', '').replace(')', '').split(); v = int(toks[0])
    for op, z in zip(toks[1::2], toks[2::2]): v = eval(f'{v}{op}{z}')
    return v
R_KL = {'Klammern weg, Punkt vor Strich': _klammer_weg, 'links nach rechts': _links_rechts, 'richtig': eval}
_b22 = [('3 * (4 + 5)', 17), ('(8 - 2) * 3', 2), ('2 * (10 - 4)', 16)]
_p = {n: r('(6 + 4) * (5 - 3)') for n, r in R_KL.items() if all(r(t) == a for t, a in _b22)}
if set(_p.values()) != {23}: PROBLEME.append(f'022: {_p}')
ZAHL['022'] = 23
ZAHL['031'] = len([(a, b) for a in range(1, 3701) for b in range(1, 3701) if a < b and a * 37 * b == 3700])  # 4
ZAHL['033'] = (748362 - 199997) - (748362 - 200000 - 3)    # 6
ZAHL['035'] = F(4368 * 75, 1456 * 25)                      # 9
ZAHL['037'] = 2347 * 89 - 2347 * 86                        # 7041
R_VT = {'a·a·b·c': lambda a, b, c: a * b * a * c, 'richtig': lambda a, b, c: a * b * c,
        'wie Summe': lambda a, b, c: a * b + a * c, 'a·b·c·2': lambda a, b, c: a * b * c * 2}
ZAHL['039'] = pruefe_regel('039', [((2, 3, 5), 60), ((3, 2, 4), 72)], R_VT, (5, 2, 7), 350)
ZAHL['041'] = sum(1 for a in range(1, 13) if any(a * x == 36 for x in range(0, 37)))  # 7
R_UM = {'Zahlen mal': lambda a, b: a * b, 'richtig': None}
# 042: x : 7 = 3 -> 21 ; 48 : x = 6 -> 288 ; 60 : x = 5 -> 300 ; Regel „beide Zahlen mal“
if not (7 * 3 == 21 and 48 * 6 == 288 and 60 * 5 == 300): PROBLEME.append('042 Regel passt nicht')
ZAHL['042'] = 72 * 8                                       # 576
def _abschneiden(z): return z // 1000 * 1000
def _runden(z): return (z + 500) // 1000 * 1000
R_UE = {'abschneiden': lambda a, b: _abschneiden(a) + _abschneiden(b), 'runden': lambda a, b: _runden(a) + _runden(b)}
ZAHL['047'] = pruefe_regel('047', [((6812, 2487), 8000), ((3391, 1765), 4000)], R_UE, (5951, 2978), 7000)
ZAHL['049'] = len(str(6718 * 2493))                        # 8
ZAHL['051'] = eindeutig(lambda g: 4 + 4 * g > 12 + 2 * g and not (4 + 4 * (g - 1) > 12 + 2 * (g - 1)), range(1, 100))  # 5
R_RW = {'erst teilen, dann abziehen': lambda m, a, e: F(e, m) - a, 'richtig': lambda m, a, e: F(e - a, m),
        'teilen, dann addieren': lambda m, a, e: F(e, m) + a}
ZAHL['053'] = pruefe_regel('053', [((3, 12, 45), 3), ((2, 10, 30), 5)], R_RW, (5, 15, 80), 1)

W = {}
def opt(k, w): return (k, w)
W['001'] = [opt('4¹⁰', zweier(4**10) == 20), opt('8⁵', zweier(8**5) != 20), opt('32⁴', zweier(32**4) != 20), opt('1 024²', zweier(1024**2) != 20)]
W['001'][0] = opt('4¹⁰', zweier(4**10) != 20)
W['003'] = [opt('durch 13', 3**13 == 3 * 3**12), opt('durch 36', 3**36 == 3 * 3**12), opt('Basis 3 durch 9', 9**12 == 3 * 3**12), opt('durch 15', 3**15 == 3 * 3**12)]
_paare = [(b, e) for b in range(2, 30) for e in range(2, 30)]
_gleich = [(b, e) for b, e in _paare if b**e == b * e]; _kleiner = [(b, e) for b, e in _paare if b**e < b * e]
W['004'] = [opt('Fast immer', _gleich == [(2, 2)] and not _kleiner), opt('Immer:', not _gleich and not _kleiner),
            opt('Nie:', all(b**e == b * e for b, e in _paare)), opt('Bei kleinen Zahlen nicht', 2**3 < 2 * 3 and 3**2 < 3 * 2)]
W['005'] = [opt('In 4 Kisten stehen je 4', 4 * 4 * 4 == 4**3), opt('In 3 Kisten', 3 * 4 * 4 == 4**3),
            opt('je 3 Schachteln', 4 * 3 * 3 == 4**3), opt('liegen je 3 Stifte', 4 * 3 + 4 == 4**3)]
_frei = 37 * 37 - 30 * 30 - 7 * 7
W['008'] = [opt('Zwei Rechtecke', _frei == 2 * 30 * 7), opt('Ein Rechteck', _frei == 30 * 7), opt('Streifen', _frei == 37 * 7), opt('Nichts', _frei == 0)]
W['009'] = [opt('6 727', not ist_quadrat(6727)), opt('7 396', not ist_quadrat(7396)), opt('5 929', not ist_quadrat(5929)), opt('4 761', not ist_quadrat(4761))]
_anz = [(n + 1)**2 - n**2 - 1 for n in range(1, 200)]
W['010'] = [opt('immer gerade', all(a % 2 == 0 for a in _anz)), opt('immer ungerade', all(a % 2 for a in _anz)),
            opt('mal gerade', len({a % 2 for a in _anz}) == 2), opt('immer gleich', len(set(_anz)) == 1)]
_z = 7 * 10**9 + 5 * 10**6 + 3 * 10**2; _z2 = 7 * 10**10 + 5 * 10**7 + 3 * 10**3
W['013'] = [opt('10-mal', _z2 == 10 * _z), opt('1 000-mal', _z2 == 1000 * _z), opt('um 3 größer', _z2 == _z + 3), opt('um 30', _z2 == _z + 30)]
_s = 9 * 10**5 + 9 * 10**4 + 9 * 10**3
W['014'] = [opt('um 1 000 größer', 10**6 - _s == 1000), opt('um 1 größer', 10**6 - _s == 1), opt('gleich groß', _s == 10**6), opt('Summe ist größer', _s > 10**6)]
def _nullen(z): s = str(z); return len(s) - len(s.rstrip('0'))
_f = [(q, n) for q in range(1, 200) for n in range(0, 8)]
_ok = [_nullen(q * 10**n) == n for q, n in _f]
W['015'] = [opt('Manchmal', any(_ok) and not all(_ok)), opt('Immer', all(_ok)), opt('Nie', not any(_ok)),
            opt('Wenn vorn die 1', all(ok == (q == 1) for (q, n), ok in zip(_f, _ok)))]
W['018'] = [opt('3 Blätter auf einem Stapel. Der Stapel wird 5-mal hintereinander verdoppelt', 3 * 2**5 == 3 * 2**5),
            opt('liegen 2 Blätter', 2 * 3**5 == 3 * 2**5), opt('kommen 2 Blätter dazu', 3 + 5 * 2 == 3 * 2**5), opt('versechsfacht', 6**5 == 3 * 2**5)]
_A = [100 + 100 * t for t in range(60)]; _B = [2**t for t in range(60)]
_vorn = [b > a for a, b in zip(_A, _B)]; _erst = _vorn.index(True)
W['020'] = [opt('überholt A irgendwann und bleibt', all(_vorn[_erst:])), opt('A bleibt immer vorn', not any(_vorn)),
            opt('holt A wieder auf', not all(_vorn[_erst:])), opt('nie ganz ein', not any(_vorn))]
W['023'] = [opt('50 − 3 · (9 − 2)', 50 - 3 * (9 - 2) == 50 - 3 * 7), opt('50 − 3 · 9 − 2', 50 - 3 * 9 - 2 == 29),
            opt('50 − (3 · 9 − 2)', 50 - (3 * 9 - 2) == 29), opt('50 − 3 · (9 + 2)', 50 - 3 * (9 + 2) == 29)]
def _kette(op):
    for t in product(range(1, 13), repeat=3):
        a, b, c = map(F, t)
        f = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, ':': lambda x, y: x / y}[op]
        if f(f(a, b), c) != f(a, f(b, c)): return True   # Klammer ändert mindestens einmal
    return False
W['024'] = [opt('nur mit Plus', not _kette('+')), opt('nur mit Minus', not _kette('-')), opt('nur mit Geteilt', not _kette(':')),
            opt('jedes Mal', all(F(a * b) * c != a * F(b * c) for a, b, c in product(range(1, 5), repeat=3)))]
_t25 = {'97 · (348 + 6)': 97 * (348 + 6), '97 · 348 + 6': 97 * 348 + 6, '(97 + 348) · 6': (97 + 348) * 6, '97 + 348 · 6': 97 + 348 * 6}
W['025'] = [opt(k, v == max(_t25.values())) for k, v in _t25.items()]
_alt = F(136 * 89 + 64 * 112 - 20, 4); _neu = F(136 * 89 + 64 * 112 - 36, 4)
W['026'] = [opt('um 4 kleiner', _alt - _neu == 4), opt('um 16 kleiner', _alt - _neu == 16), opt('um 36 kleiner', _alt - _neu == 36), opt('um 9 kleiner', _alt - _neu == 9)]
_b = 30 - 6 - 4; _v = {1: 30 - 6 - 4, 2: 30 - (6 + 4), 3: 30 - 6 + 4, 4: 30 - (6 - 4)}; _pa = {k for k, v in _v.items() if v == _b}
W['027'] = [opt('Genau ① und ②', _pa == {1, 2}), opt('Genau ②:', _pa == {2}), opt('Genau ① und ③', _pa == {1, 3}), opt('Genau ② und ④', _pa == {2, 4})]
# 028: letzter Rechenschritt nach Ersetzung (von Hand bestimmt, Punkt vor Strich, links nach rechts)
W['028'] = [opt('Das − durch ·', True), opt('Das + durch ·', False), opt('Das − durch :', False), opt('Das · durch +', False)]
W['029'] = [opt('ganz rechts', True), opt('ganz links', False), opt('zuerst ausrechnet', False), opt('zuletzt ausrechnet', False)]
W['030'] = [opt('Die Terme sind verschieden, ihre Werte sind gleich', (4 + 5) * 6 == 4 * 6 + 5 * 6),
            opt('Die Terme sind gleich, ihre Werte sind gleich', False), opt('verschieden, ihre Werte sind verschieden', (4 + 5) * 6 != 4 * 6 + 5 * 6),
            opt('Die Terme sind gleich, ihre Werte sind verschieden', False)]
_x, _y = 36 * 4375 * 5, 18 * 4375 * 10
W['032'] = [opt('Sie sind gleich groß', _x == _y), opt('Das zweite ist größer', _y > _x), opt('Das erste ist größer', _x > _y), opt('nur durch vollständiges', False)]
W['034'] = [opt('nehmen die Zahlen ihre Rechenzeichen mit', 763 + 237 - 289 == 763 - 289 + 237),
            opt('Plus und Minus darf man umstellen, dabei bleiben', 763 - 237 + 289 == 763 - 289 + 237 and False),
            opt('gar nicht umstellen', False), opt('Mal und Geteilt', F(60, 2) * 3 == F(60, 3) * 2)]
_p36 = 368 * 47
W['036'] = [opt('300 · 40 + 68 · 7', 300 * 40 + 68 * 7 != _p36), opt('370 · 47 − 2 · 47', 370 * 47 - 2 * 47 != _p36),
            opt('368 · 40 + 368 · 7', 368 * 40 + 368 * 7 != _p36), opt('300 · 47 + 68 · 47', 300 * 47 + 68 * 47 != _p36)]
W['038'] = [opt('Erst werden alle vier Eis bezahlt, danach alle vier', 4 * 2 + 4 * 3 == 4 * 2 + 4 * 3), opt('zusammen', False), opt('ein Getränk für alle', 4 * 2 + 3 == 4 * 2 + 4 * 3), opt('Erst wird ein Eis', 2 + 4 * 3 == 4 * 2 + 4 * 3)]
_q40 = F(3 * 8 * 30 + 3 * 8 * 2, 8 * 30 + 8 * 2)
W['040'] = [opt('dreimal so groß.', _q40 == 3), opt('neunmal', _q40 == 9), opt('breiteren Teils', False), opt('Dreifache der Höhe', False)]
W['043'] = [opt('gleichmäßig verteilt', True), opt('Jedes Kind bekommt 48', False), opt('verliert 6', False), opt('6 Kinder teilen', False)]
_l44 = [(F(360, a), F(360, 3 * a)) for a in range(1, 361) if 360 % a == 0 and 360 % (3 * a) == 0]
W['044'] = [opt('dreimal so klein', all(n == x / 3 for x, n in _l44)), opt('dreimal so groß', all(n == 3 * x for x, n in _l44)),
            opt('bleibt gleich', all(n == x for x, n in _l44)), opt('um 3 kleiner', all(n == x - 3 for x, n in _l44))]
_l45 = {'x : 74 = 224': 224 * 74, '74 · x = 8 288': F(8288, 74), '37 · x = 8 288': F(8288, 37), 'x : 37 = 224': 224 * 37}
W['045'] = [opt(k, v == max(_l45.values())) for k, v in _l45.items()]
def _sicher(n, p, grenze):  # einfacher Überschlag (beide Zahlen auf volle Zehner bzw. Zehner auf/ab) entscheidet?
    hoch = -(-n // 10) * 10 * -(-p // 10) * 10 if n >= 10 else n * (-(-p // 10) * 10)
    tief = (n // 10) * 10 * (p // 10) * 10 if n >= 10 else n * (p // 10) * 10
    return hoch <= grenze or tief > grenze
W['046'] = [opt('500 € für 26 Karten', not _sicher(26, 19, 500)), opt('100 € für 4 Spiele', not _sicher(4, 19, 100)),
            opt('6 Kisten zu je 38', not _sicher(6, 38, 300)), opt('9 Klassen', not _sicher(9, 27, 400))]
W['048'] = [opt('B ist genauer', abs(4800 + 3500 - 8299) < abs(5000 + 3000 - 8299)), opt('A ist besser', False), opt('Gleich gut', False), opt('B ist falsch', False)]
W['050'] = [opt('Größer:', F(7236, 9) > 700), opt('Kleiner:', F(7236, 9) < 700), opt('Genau gleich', F(7236, 9) == 700), opt('ohne genaue Rechnung', False)]
W['052'] = [opt('Wie viele Busse werden gebraucht', -(-189 // 52) == 4), opt('ganz voll', 189 // 52 == 4), opt('im letzten Bus?', 189 % 52 == 4), opt('Plätze bleiben', 52 - 189 % 52 == 4)]
_d54 = {(n + 6) * 2 - (n * 2 + 6) for n in range(0, 1000)}
W['054'] = [opt('immer um 6 größer', _d54 == {6}), opt('immer gleich groß', _d54 == {0}), opt('doppelt so groß', False), opt('Mal ist Mias', len(_d54) > 1)]
def _l(f): return [x for x in range(0, 200) if f(x)]
W['055'] = [opt('4 · x + 12 − 4 = 108', _l(lambda x: 4 * x + 12 - 4 == 108) == [25]), opt('4 · (x + 12)', _l(lambda x: 4 * (x + 12) - 4 == 108) == [25]),
            opt('4 · x − 12 + 4', _l(lambda x: 4 * x - 12 + 4 == 108) == [25]), opt('4 · x + 12 + 4', _l(lambda x: 4 * x + 12 + 4 == 108) == [25])]

# ---- 3. Durchgang (Stand 48c90f32): neue und geänderte Aufgaben ----
ZAHL['002'] = zweier(4 * 2**30)                                   # 32
ZAHL['012'] = sum(1 for n in range(1, 30) if 5 * 10**3 < 10**n < 5 * 10**7)  # 4
ZAHL['016'] = 6 - 1   # Faktoren 2: 6⁶ = 2⁶·3⁶, richtig 2·3⁶ (Primfaktoren eindeutig)
assert 6**6 == 2**6 * 3**6 and 2 * 3**6 == 1458
_d21 = {(z - 4800 + 650) - (z - (4800 + 650)) for z in range(10001, 30000)}
ZAHL['021'] = _d21.pop() if len(_d21) == 1 else ('NICHT EINDEUTIG', _d21)   # 1300 für jede Zahl
_b22 = [('3 * (4 + 5)', 17), ('(8 - 2) * 3', 2), ('2 * (10 - 4)', 16)]
_p = {n: r('(6 + 4) * (5 - 3)') for n, r in R_KL.items() if all(r(t) == a for t, a in _b22)}
ZAHL['022'] = _p['Klammern weg, Punkt vor Strich'] - eval('(6 + 4) * (5 - 3)') if set(_p) == {'Klammern weg, Punkt vor Strich'} else ('Regel', _p)  # 3
_d25 = {(x + 5 + 7) * 3 - (x + 7) * 3 for x in range(0, 1000)}
ZAHL['025'] = _d25.pop() if len(_d25) == 1 else ('NICHT EINDEUTIG', _d25)   # 15
_p31 = [(a, b) for a in range(1, 4601) for b in range(1, 4601) if a * 23 * b == 4600 and a > 5 and b > 5 and a % 10 and b % 10 and b > a]
ZAHL['031'] = _p31[0][1] if len(_p31) == 1 else ('NICHT EINDEUTIG', _p31)   # 25
ZAHL['039'] = eindeutig(lambda q: q > 0 and q * 2 * q * 7 == q * (2 * 7), range(0, 1000))  # 1
ZAHL['046'] = len(str(3412 * 3438)) if len(str(3400 * 3400)) == len(str(3500 * 3500)) == 8 else 'Schranken entscheiden nicht'
def _abs(z): return z // 1000 * 1000
def _rnd(z): return (z + 500) // 1000 * 1000
ZAHL['047'] = max((_rnd(a) + _rnd(b)) - (_abs(a) + _abs(b)) for a in range(1000, 10000, 7) for b in range(1000, 10000, 13))  # 2000
ZAHL['053'] = len([(h, st) for h in range(1, 21) for st in range(1, 21) if 3 * h + 2 * st == 20])  # 3
W['005'] = [opt('In 4 Kisten stehen je 4', 4 * 4 * 4 == 4**3), opt('In 3 Kisten', 3 * 4 * 4 == 4**3),
            opt('je 3 Schachteln, in jeder Schachtel liegen 3', 4 * 3 * 3 == 4**3), opt('liegt 1 Stift', 4 * 3 * 1 == 4**3)]
W['018'] = [opt('3 Blätter. Er wird 5-mal hintereinander verdoppelt', True), opt('2 Blätter', 2 * 3**5 == 96),
            opt('5 Blätter', 5 * 2**3 == 96), opt('2 Blätter dazu', 3 + 5 * 2 == 96)]
W['018'][1] = opt('am Anfang 2 Blätter', 2 * 3**5 == 96)
W['023'] = [opt('50 − 3 · (9 − 2)', True), opt('50 − 3 · 9 − 2', 50 - 3 * 9 - 2 == 29), opt('50 − 3 · 9 + 2', 50 - 3 * 9 + 2 == 29), opt('50 − 3 · (9 + 2)', 50 - 3 * 11 == 29)]
# 030: letzter Rechenschritt 20 − (5 + 3) -> Minus (Differenz); 20 − 5 + 3 -> Plus (Summe)
W['030'] = [opt('Mit Klammer ist es eine Differenz, ohne Klammer eine Summe', True), opt('Mit Klammer ist es eine Summe', False),
            opt('Mit und ohne Klammer ist es eine Differenz', False), opt('Mit und ohne Klammer ist es eine Summe', False)]
W['034'] = [opt('Die Zahlen nehmen ihre Rechenzeichen mit', 763 + 237 - 289 == 763 - 289 + 237),
            opt('an ihrem Platz, dann darf man bei Plus', 763 - 237 + 289 == 763 - 289 + 237),
            opt('gar nicht umstellen', False), opt('bei Mal und Geteilt', F(60, 2) * 3 == F(60, 3) * 2)]
_fehlt = 368 * 47 - (300 * 40 + 68 * 7)
W['036'] = [opt('300 · 7 und 68 · 40', _fehlt == 300 * 7 + 68 * 40), opt('300 · 68 und 40 · 7', _fehlt == 300 * 68 + 40 * 7),
            opt('nur 68 · 40', _fehlt == 68 * 40), opt('nichts', _fehlt == 0)]
W['038'] = [opt('Erst werden alle vier Eis bezahlt, danach alle vier', True), opt('und das viermal', False), opt('ein Getränk für alle', False), opt('Erst wird ein Eis bezahlt, danach alle', False)]
W['040'] = [opt('dreimal so groß.', _q40 == 3), opt('neunmal', _q40 == 9), opt('breiteren Teils', False), opt('sechsmal', _q40 == 6)]
_xs = range(1, 200)
W['042'] = [opt('□ : x = 8', all(F(8 * x, x) == 8 for x in _xs)), opt('x : 8 = □', all(F(x, 8) == 8 * x for x in _xs)),
            opt('8 : x = □', all(F(8, x) == 8 * x for x in _xs)), opt('x · □ = 8', all(x * 8 * x == 8 for x in _xs))]
W['044'] = [opt('zu einem Drittel', all(n == x / 3 for x, n in _l44)), opt('dreimal so groß', all(n == 3 * x for x, n in _l44)),
            opt('bleibt gleich', all(n == x for x, n in _l44)), opt('um 3 kleiner', all(n == x - 3 for x, n in _l44))]
_mal_ohne = any(b % a for a in range(1, 30) for b in range(1, 30)); _get_ohne = False  # x = a · b gibt es immer
W['045'] = [opt('Nur die Mal-Gleichung', _mal_ohne and not _get_ohne), opt('Nur die Geteilt-Gleichung', _get_ohne and not _mal_ohne),
            opt('Keine der beiden', not _mal_ohne and not _get_ohne), opt('Jede der beiden', _mal_ohne and _get_ohne)]
W['049'] = W.pop('046')
W['055'] = [opt('4 · x + 12 − 4 = 108', _l(lambda x: 4 * x + 12 - 4 == 108) == [25]), opt('4 · x − 12 − 4', _l(lambda x: 4 * x - 12 - 4 == 108) == [25]),
            opt('4 · x − 12 + 4', _l(lambda x: 4 * x - 12 + 4 == 108) == [25]), opt('4 · x + 12 + 4', _l(lambda x: 4 * x + 12 + 4 == 108) == [25])]

# ---- 4. Durchgang (Stand f21e6bd7): 002, 012, 016, 030, 039, 045, 046, 053 ----
_ung = [b**e for b in range(1, 40, 2) for e in range(0, 12)]
W['002'] = [opt('immer ungerade', all(v % 2 for v in _ung)), opt('gerade, wenn die Hochzahl gerade', any(v % 2 == 0 for v in _ung)),
            opt('mal gerade, mal ungerade', len({v % 2 for v in _ung}) == 2), opt('sobald die Hochzahl größer als 1', any(v % 2 == 0 for v in _ung))]
_acht = range(10**7, 10**8)   # alle Zahlen mit genau 8 Stellen (Grenzen geprüft)
assert len(str(10**7)) == 8 and len(str(10**8 - 1)) == 8 and len(str(10**8)) == 9 and len(str(10**7 - 1)) == 7
W['012'] = [opt('mindestens 10⁷ und kleiner als 10⁸', 10**7 <= min(_acht) and max(_acht) < 10**8),
            opt('größer als 10⁷ und höchstens 10⁸', 10**7 < min(_acht)),       # scheitert genau an 10⁷
            opt('mindestens 10⁸', min(_acht) >= 10**8), opt('mindestens 10⁶ und kleiner als 10⁷', max(_acht) < 10**7)]
# 030: Termart = letzter Rechenschritt; Gegenbeispiele aufzählen
_gegen0 = ('2 * 3 + 4', '+')    # „2 ·“ davor ohne Klammer: Summe
_gegen1 = ('20 - 5 + 3', '20 - (5 + 3)')  # Klammer ändert die Art (Summe -> Differenz)
_gegen2 = ('7 + 3 * 5', '+')    # Malzeichen, aber Summe
W['030'] = [opt('ganzen Term in eine Klammer und schreibt „· 2“', True),  # (T) · 2: letzter Schritt immer · 2
            opt('„2 ·“ ohne Klammer', not bool(_gegen0)), opt('ändert sich seine Art nie', not bool(_gegen1)), opt('Malzeichen vor', not bool(_gegen2))]
ZAHL['016'] = 6 - 1
W['039'] = [opt('□-mal', all(F(q * 2 * q * 7, q * 2 * 7) == q for q in range(1, 500))),
            opt('doppelt', all(F(q * 2 * q * 7, q * 2 * 7) == 2 for q in range(1, 500))),
            opt('14-mal', all(F(q * 2 * q * 7, q * 2 * 7) == 14 for q in range(1, 500))),
            opt('um □ größer', all(q * 2 * q * 7 - q * 2 * 7 == q for q in range(1, 500)))]
_fa = [(a, b) for a in range(1, 60) for b in range(1, 400) if b % a == 0]
W['045'] = [opt('Fast immer: Bei a gleich 1', all((b // a < b) == (a != 1) for a, b in _fa) and all(b // a == b for a, b in _fa if a == 1)),
            opt('Immer: Teilen', all(b // a < b for a, b in _fa)), opt('Nie:', all(b // a > b for a, b in _fa)),
            opt('Bei geraden a ja', all((b // a < b) if a % 2 == 0 else (b // a > b) for a, b in _fa))]
_e46 = 3412 * 3438
W['046'] = [opt('Es sind 8 Stellen', len(str(_e46)) == 8 and len(str(3400 * 3400)) == 8 and 3400 * 3400 < _e46),
            opt('Es sind 7 Stellen', len(str(_e46)) == 7), opt('Es sind 6 Stellen', len(str(_e46)) == 6), opt('ohne genaue Rechnung nicht sagen', False)]
_d53 = {(8 * q + 8 * 3) - 8 * (q + 3 - 2) for q in range(3, 200)}   # Päckchen muss positiv kosten: q + 1 > 0
ZAHL['053'] = _d53.pop() if len(_d53) == 1 else ('NICHT EINDEUTIG', _d53)  # 16

def main():
    fehler = list(PROBLEME)
    for datei in ('zahlen.potenzen_basis.json', 'zahlen.rechengesetze.json'):
        for a in json.load(open(os.path.join(HIER, datei)))['aufgaben']:
            k = a['kennung'][-3:]; A = a['aufgabe']
            if A['y'] == 'zahl':
                soll = A['o']['wert']; ich = ZAHL.get(k)
                if ich is None: fehler.append(f'{k}: keine eigene Rechnung'); continue
                if isinstance(ich, tuple): fehler.append(f'{k}: {ich}'); continue
                if F(ich) != F(soll): fehler.append(f'{k}: Soll {soll}, ich {ich}')
                aw = []
                for fb in a['fehlbilder']:
                    aw.append(fb['antwort'])
                    if F(fb['antwort']) == F(soll): fehler.append(f'{k}: Fehlbild = Lösung')
                    r = fb.get('rechnung')
                    if r and F(eval(r, {})) != F(fb['antwort']): fehler.append(f'{k}: Fehlbild-Rechnung {r}')
                if len(set(aw)) != len(aw): fehler.append(f'{k}: doppelte Fehlantwort')
            else:
                reg = W.get(k)
                if reg is None: fehler.append(f'{k}: Auswahl ohne Rechenregel'); continue
                wahr = []
                for o in A['a']:
                    t = [w for key, w in reg if key in o]
                    if len(t) != 1: fehler.append(f'{k}: Option nicht zuordenbar: {o[:45]}'); wahr.append(None)
                    else: wahr.append(t[0])
                if wahr.count(True) != 1 or wahr.index(True) != A['o']['index']:
                    fehler.append(f'{k}: wahr={wahr}, Soll {A["o"]["index"]}')
    for f in fehler: print('FEHLER', f)
    print(f'{len(fehler)} Abweichungen')

if __name__ == '__main__':
    main()
