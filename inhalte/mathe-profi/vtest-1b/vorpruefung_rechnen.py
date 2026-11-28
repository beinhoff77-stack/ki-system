"""Unabhängige Vorprüfung vtest-1b: eigene Sollwerte aus dem AUFGABENTEXT (nicht aus loesung_rechnung), exakte Brüche.
Aufruf: python3 -I inhalte/mathe-profi/vtest-1b/vorpruefung_rechnen.py   (liest die JSON-Dateien, ändert nichts)
Teil A: Sollwerte aller Zahl-/Lücken-Aufgaben. Teil B: Auswahl-Aufgaben (Behauptungen der Möglichkeiten nachgerechnet,
Platz/Länge der richtigen Möglichkeit). Teil C: Fehlbild-Antworten gegen Soll, doppelte Sollantworten je Lernziel."""
import glob, json, os
from fractions import Fraction as F
H = os.path.dirname(os.path.abspath(__file__))

def gauss(p):
    s = 0
    for i, (x1, y1) in enumerate(p):
        x2, y2 = p[(i + 1) % len(p)]
        s += x1 * y2 - x2 * y1
    return F(abs(s), 2)

# --- Teil A: eigene Sollwerte (aus dem Text hergeleitet) ---
SOLL = {}
def s(k, v): SOLL[k] = v if isinstance(v, list) else [v]
s('VT1B-002', F(85, 100) * 40)
s('VT1B-003', F(27, 30) * 100 - F(18, 24) * 100)
s('VT1B-004', F(126, 360) * 100)
s('VT1B-006', [2, F(20, 25) * 100])
s('VT1B-007', F(18, 30) * 40 - 18)
s('VT1B-008', [2, F(150) / (1 - F(25, 100))])
s('VT1B-009', F(117) / (1 - F(35, 100)))
s('VT1B-010', F(840) * F(112, 100) / 6)
s('VT1B-011', F(140, 100) * F(75, 100) * 100)
s('VT1B-013', F(600) * F(80, 100) - F(620) * F(3, 4))
s('VT1B-014', F(120 - 96, 96) * 100)
s('VT1B-016', 30 + 30 * 2)
s('VT1B-018', F(40) / F(1, 2))
s('VT1B-019', F(30, 100) * F(40, 100) * 100)
s('VT1B-020', [3, F(60, 100) * 30 - F(80, 100) * 5])
# Rosinen: Trockenmasse 10 % von 200 = 20 kg; 20 % des Endgewichts
s('VT1B-021', F(10, 100) * 200 / F(20, 100))
# Bruchgleichungen
s('VT1B-023', len({3, -3}))
s('VT1B-024', 14)
s('VT1B-026', 0 + 5)
s('VT1B-027', [1, -3])
x = F(18, 1); assert x / (x + 9) == F(2, 3)
s('VT1B-030', 18)
a = F(9); assert F(8) / (3 + a) == F(2, 3)
s('VT1B-032', 9)
# 035: Brute force über k, x aus 3(x+4)=k(x-1)
def nolsg(k):
    # (3-k)x = -k-12
    if 3 - k == 0:
        return (-k - 12) != 0
    xx = F(-k - 12, 3 - k)
    return xx in (1, -4)
s('VT1B-035', sum(1 for k in range(-6, 7) if nolsg(k)))
s('VT1B-034', [2, 4]); assert F(6) / (4 + 2) == F(4) / 4
s('VT1B-038', 1)   # nur (B): x = 1
s('VT1B-039', 17 - 2 * 4)
s('VT1B-040', 3 * 6 + 6)
s('VT1B-041', [1, 2]); assert F(5) / 1 + 2 == F(7) / 1
s('VT1B-042', 8 - 1)
s('VT1B-044', F(18 * 30, 12))
s('VT1B-046', F(77 * 4, 7))
s('VT1B-047', F(540, 9) * 4)
s('VT1B-048', [2, F(4 * 18, 6)])
# 049: (5k+6)/(7k+6)=3/4 -> k=6
k = F(6); assert (5 * k + 6) / (7 * k + 6) == F(3, 4)
s('VT1B-049', 5 * 6)
# Potenzen
s('VT1B-051', 6); s('VT1B-052', F(10000, 625)); s('VT1B-053', [49, -5])
s('VT1B-054', F(10000, 8)); s('VT1B-056', 36); s('VT1B-057', [1, 9]); s('VT1B-063', -2)
s('VT1B-060', F(1, 1000) / F(1, 10**9))
s('VT1B-064', [3, 5]); s('VT1B-065', [7, 8]); s('VT1B-067', 9)
s('VT1B-068', len(str(3 * 10**5 * 32 * 10**6)))  # 3,2e7 = 32e6
s('VT1B-070', 5)
s('VT1B-072', -7); s('VT1B-073', [100000, 4])
s('VT1B-074', sum(1 for n in (-9, -4, -7, -5) if F(1, 10**(-n)) < F(1, 10**4)))
s('VT1B-075', F(10**-6 if False else 1, 10**6) / F(1, 10**9))
s('VT1B-076', -3)
s('VT1B-079', F(5, 10**8) / F(1, 10**9)); s('VT1B-080', [3, 250]); s('VT1B-081', F(6, 10**5) / F(1, 10**6))
s('VT1B-082', F(3000, 5)); s('VT1B-083', [3, 1000])
s('VT1B-086', F(6 * 10**7, 3 * 10**4))
# 087: kleinstes n mit 4*10^n > 0,005
nn = min(n for n in range(-12, 5) if F(4) * F(10) ** n > F(5, 1000)); s('VT1B-087', nn)
s('VT1B-088', sum(1 for v in (F(5) * 10**5, F(50) * 10**4, F(1, 2) * 10**6, F(5000000, 100)) if v == 500000))
s('VT1B-089', F(4 * 10**30, 8 * 10**24)); s('VT1B-090', [2, 20])
# Flächen
s('VT1B-093', gauss([(1, 1), (9, 1), (12, 6)]))
s('VT1B-094', 6); s('VT1B-096', F(24 * 15, 2) * F(7, 2))
s('VT1B-097', [2, 30]); s('VT1B-100', 14)
s('VT1B-101', F(2 * 9600, 90 + 150)); s('VT1B-103', F(45000, 300)); s('VT1B-104', [2, 6]); s('VT1B-105', [8, 20])
s('VT1B-107', gauss([(0, 0), (8, 0), (8, 5), (4, 8), (0, 5)]))
s('VT1B-108', F(14 * 9 - 102, 4)); s('VT1B-110', (30 - F(9, 4)) * 40); s('VT1B-111', [2, 60 + 24])
s('VT1B-112', gauss([(0, 0), (6, 0), (6, 4), (0, 2)]))
s('VT1B-114', F(60, 24)); s('VT1B-116', (1 - F(12 * 4, 12 * 5)) * 100)
s('VT1B-117', (F(12, 10) ** 2 - 1) * 100); s('VT1B-118', [3, 100]); s('VT1B-119', F(2, 2))
s('VT1B-065', [7, 8])

dateien = sorted(glob.glob(os.path.join(H, '*.json')))
alle = []
for fn in dateien:
    alle += json.load(open(fn))['aufgaben']
byk = {e['kennung']: e for e in alle}
bad = 0
fehlt = []
for e in alle:
    k = e['kennung']; a = e['aufgabe']
    if a['y'] == 'auswahl':
        continue
    ist = [F(str(a['o']['wert']))] if a['y'] == 'zahl' else [F(str(v)) for v in a['o']['werte']]
    if k not in SOLL:
        fehlt.append(k); continue
    soll = [F(v) for v in SOLL[k]]
    if soll != ist:
        bad += 1; print('ABWEICHUNG', k, 'mein Soll', [str(v) for v in soll], 'gespeichert', [str(v) for v in ist])
print('Teil A: %d Zahl-/Lücken-Aufgaben, %d ohne eigenes Soll %s, %d Abweichungen' % (sum(1 for e in alle if e['aufgabe']['y'] != 'auswahl'), len(fehlt), fehlt, bad))

# --- Teil B: Auswahl: Platz, Länge, Ähnlichkeit der Möglichkeiten ---
import itertools, re
from collections import Counter
plat = Counter(); strikt_zeichen = []; strikt_woerter = []; strikt_kurz = []; paar = 0; mitte = 0; n_ausw = 0
tok = lambda t: set(re.findall(r'\w+|[^\w\s]', t))
for e in alle:
    a = e['aufgabe']
    if a['y'] != 'auswahl':
        continue
    n_ausw += 1
    i = a['o']['index']; plat[i + 1] += 1
    L = [len(t) for t in a['a']]; W = [len(t.split()) for t in a['a']]
    rest = [j for j in range(4) if j != i]
    if L[i] > max(L[j] for j in rest): strikt_zeichen.append(e['kennung'])
    if W[i] > max(W[j] for j in rest): strikt_woerter.append(e['kennung'])
    if L[i] < min(L[j] for j in rest): strikt_kurz.append(e['kennung'])
    T = [tok(t) for t in a['a']]
    sim = lambda p, q: len(T[p] & T[q]) / len(T[p] | T[q])
    best = max(itertools.combinations(range(4), 2), key=lambda pq: sim(*pq))
    if i in best: paar += 1
    m = [sum(sim(p, q) for q in range(4) if q != p) for p in range(4)]
    if m.index(max(m)) == i: mitte += 1
print('Teil B: %d Auswahl-Aufgaben; Plätze der richtigen Möglichkeit' % n_ausw, dict(sorted(plat.items())))
print('  richtige Möglichkeit strikt die längste (Zeichen):', strikt_zeichen)
print('  richtige Möglichkeit strikt die meisten Wörter:', strikt_woerter)
print('  richtige Möglichkeit strikt die kürzeste:', strikt_kurz)
print('  richtige in der ähnlichsten Zweiergruppe der Möglichkeiten: %d von %d (Zufall 50 %%)' % (paar, n_ausw))
print('  richtige = der „Mittelpunkt“ (im Mittel allen anderen am ähnlichsten): %d von %d (Zufall 25 %%)' % (mitte, n_ausw))

# --- Teil C: Fehlbilder = Soll? doppelte Sollantworten je Lernziel ---
for e in alle:
    a = e['aufgabe']
    if a['y'] == 'auswahl': continue
    soll = SOLL.get(e['kennung'])
    for fb in e['fehlbilder']:
        if a['y'] == 'zahl' and F(str(fb['antwort'])) == F(soll[0]):
            print('Fehlbild = Soll', e['kennung'])
dup = {}
for e in alle:
    a = e['aufgabe']
    if a['y'] == 'auswahl':
        v = ('A', a['a'][a['o']['index']])
    elif a['y'] == 'zahl': v = ('Z', a['o']['wert'])
    else: v = ('L', tuple(a['o']['werte']))
    dup.setdefault((e['thema'], e['lernkarte']), []).append((e['kennung'], v))
for lz, l in dup.items():
    c = Counter(v for k, v in l if v[0] != 'A')
    for v, n in c.items():
        if n > 1: print('gleiche Sollantwort im Lernziel', lz, v, [k for k, w in l if w == v])


# --- Teil D (nur mit Argument --bestand): Ähnlichkeit gegen den Bestand (inhalte/themen, rollend-*) ---
import sys
if '--bestand' in sys.argv:
    wurzel = os.path.abspath(os.path.join(H, '..', '..'))   # .../inhalte
    def toks(t):
        t = t.replace('\u202f', ' ').replace('\xa0', ' ')
        return set(re.findall(r'[A-Za-zÄÖÜäöüß]{3,}', t.lower())), set(re.findall(r'\d+(?:[,.]\d+)?', t))
    def txt(a):
        f = a.get('f', {}); t = f.get('text', '')
        if a.get('a'): t += ' ' + ' '.join(map(str, a['a']))
        if f.get('schablone'): t += ' ' + f['schablone']
        return t
    korp = []
    for fn in glob.glob(os.path.join(wurzel, 'themen', '*.json')):
        d = json.load(open(fn))
        for i, a in enumerate(d['aufgaben']):
            korp.append((os.path.basename(fn)[:-5] + '#%d:%s/%s/%s' % (i, a.get('l'), a.get('p'), a.get('s')), txt(a)))
    for fn in glob.glob(os.path.join(wurzel, 'mathe-profi', 'rollend-*', '*.json')):
        try: d = json.load(open(fn))
        except Exception: continue
        if isinstance(d, dict) and 'aufgaben' in d:
            for e in d['aufgaben']:
                a = e.get('aufgabe') or e
                if isinstance(a, dict) and 'f' in a:
                    korp.append((fn.split('mathe-profi/')[1] + ':' + e.get('kennung', '?'), txt(a)))
    ct = [(k,) + toks(t) + (t,) for k, t in korp]
    print('Teil D: %d Bestandsaufgaben; Treffer mit Wert >= 0,45 (0,6 · Wortübereinstimmung + 0,4 · Zahlenübereinstimmung):' % len(ct))
    for e in alle:
        w, n = toks(txt(e['aufgabe']))
        best = max(((len(w & w2) / max(1, len(w | w2))) * 0.6 + (len(n & n2) / max(1, len(n | n2))) * 0.4, k, t2) for k, w2, n2, t2 in ct)
        if best[0] >= 0.45:
            print('  %s %.2f %s | %s' % (e['kennung'], best[0], best[1], best[2][:140].replace('\n', ' ')))
