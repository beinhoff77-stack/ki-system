#!/usr/bin/env python3
"""Thema gleichungen.lgs3 – Lineare Gleichungssysteme mit 3 Unbekannten (Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(906)
V = ('x', 'y', 'z')
NR = ('I', 'II', 'III')
LX = 'x = □; y = □; z = □'


def lin(k, rechts, vs=V):
    """Linke Seite aus Koeffizienten, z. B. 2x − y + 3z = 5"""
    teile = []
    for c, v in zip(k, vs):
        if c == 0: continue
        b = '' if abs(c) == 1 else dz(abs(c))
        if not teile: teile.append(('−' if c < 0 else '') + b + v)
        else: teile.append(('− ' if c < 0 else '+ ') + b + v)
    return ' '.join(teile) + f' = {dz(rechts)}'


def system(M, b, vs=V):
    return '; '.join(f'({NR[i]}) {lin(M[i], b[i], vs)}' for i in range(len(M)))


def det3(M):
    (a, b_, c), (d, e, f), (g, h, i) = M
    return a * (e * i - f * h) - b_ * (d * i - f * g) + c * (d * h - e * g)


def det3_c(M):
    (a, b_, c), (d, e, f), (g, h, i) = M
    return f'({a})*(({e})*({i}) - ({f})*({h})) - ({b_})*(({d})*({i}) - ({f})*({g})) + ({c})*(({d})*({h}) - ({e})*({g}))'


def cramer_c(M, b):
    """Rechenausdrücke für die Lösung nach der Cramerschen Regel (unabhängige Nachrechnung)."""
    out = []
    for j in range(3):
        Mj = [[b[i] if k == j else M[i][k] for k in range(3)] for i in range(3)]
        out.append(f'({det3_c(Mj)}) / ({det3_c(M)})')
    return out


def zufall_lgs(gr=3, lsg=5, eins=True):
    while True:
        M = [[R.randint(-gr, gr) for _ in range(3)] for _ in range(3)]
        if det3(M) == 0: continue
        if eins and not all(any(abs(c) == 1 for c in row) for row in M): continue
        if any(sum(1 for c in row if c) < 2 for row in M): continue
        x = [R.randint(-lsg, lsg) for _ in range(3)]
        b = [sum(M[i][k] * x[k] for k in range(3)) for i in range(3)]
        return M, b, x


ETAPPEN = [
    {'lernziel': 'pruefen', 'titel': 'Ist das Zahlentripel eine Lösung?',
     'regel': 'Ein Zahlentripel (x | y | z) ist ⟦Lösung⟧ des Systems, wenn es ⟦alle drei Gleichungen⟧ erfüllt. Setze ein und vergleiche jede Gleichung.',
     'schritte': ['System (I) x + y + z = 6; (II) 2x − y = 0; (III) x − z = −2. Prüfe (1 | 2 | 3).',
                  '(I) 1 + 2 + 3 = 6 ✓; (II) 2 − 2 = 0 ✓; (III) 1 − 3 = −2 ✓: ⟦(1 | 2 | 3) ist Lösung⟧.'],
     'probe': 'Eine einzige falsche Gleichung genügt, damit das Tripel keine Lösung ist.',
     'fehler': 'Nur Gleichung (I) zu prüfen genügt nicht: (2 | 2 | 2) erfüllt (I), aber (II) ergibt 2 ≠ 0. Es müssen ⟦alle⟧ Gleichungen stimmen.'},
    {'lernziel': 'stufenform', 'titel': 'Stufenform von unten lösen',
     'regel': 'In der ⟦Stufenform⟧ hat die letzte Gleichung nur noch eine Variable. Löse sie, setze ⟦von unten nach oben⟧ ein.',
     'schritte': ['(III) 2z = 6 ⇒ z = 3. (II) y + z = 5 ⇒ y = 2.', '(I) x + y − z = 1 ⇒ x + 2 − 3 = 1 ⇒ ⟦x = 2, y = 2, z = 3⟧.'],
     'probe': '(I) 2 + 2 − 3 = 1 ✓',
     'fehler': 'In (II) y + z = 5 mit z = 3 auf y = 8 zu kommen ist falsch: 3 wird ⟦abgezogen⟧, nicht addiert: y = 5 − 3 = 2.'},
    {'lernziel': 'eliminieren', 'titel': 'Eine Variable eliminieren',
     'regel': 'Mit dem ⟦Additionsverfahren⟧ addierst oder subtrahierst du Vielfache zweier Gleichungen so, dass eine ⟦Variable wegfällt⟧. Auch die rechte Seite mitrechnen!',
     'schritte': ['(I) x + 2y − z = 3; (II) 2x − y + z = 4. Berechne (II) − 2 · (I).',
                  '2x − 2x = 0, −y − 4y = −5y, z + 2z = 3z, 4 − 6 = −2: ⟦−5y + 3z = −2⟧.'],
     'probe': 'Das x ist verschwunden ✓',
     'fehler': 'Bei (II) − 2 · (I) nur die x-Glieder zu verdoppeln ist falsch: ⟦Jedes Glied⟧ von (I), auch die rechte Seite, wird mit 2 multipliziert.'},
    {'lernziel': 'loesen', 'titel': 'LGS mit drei Unbekannten lösen',
     'regel': 'Eliminiere mit zwei Gleichungspaaren ⟦dieselbe Variable⟧. So entsteht ein System mit ⟦zwei Unbekannten⟧. Löse es und setze zurück ein.',
     'schritte': ['(I) x + y + z = 2; (II) x − y + z = 6; (III) 2x + y − z = −3. (I) − (II): 2y = −4 ⇒ y = −2.',
                  '(I) + (III): 3x + 2y = −1 ⇒ 3x − 4 = −1 ⇒ x = 1. Aus (I): 1 − 2 + z = 2 ⇒ ⟦x = 1, y = −2, z = 3⟧.'],
     'probe': '(II) 1 + 2 + 3 = 6 ✓; (III) 2 − 2 − 3 = −3 ✓',
     'fehler': 'Mit (I) und (II) x zu eliminieren, mit (II) und (III) aber y, führt nicht weiter: Beide neuen Gleichungen müssen ⟦dieselbe Variable⟧ verlieren.'},
    {'lernziel': 'parabel', 'titel': 'Parabel durch drei Punkte',
     'regel': 'Setze jeden Punkt (x | y) in ⟦y = ax² + bx + c⟧ ein. Das ergibt drei Gleichungen für ⟦a, b und c⟧.',
     'schritte': ['Punkte (0 | 1), (1 | 2), (−1 | 4): Aus (0 | 1) folgt c = 1.',
                  'a + b + 1 = 2 und a − b + 1 = 4 ⇒ 2a = 4 ⇒ a = 2, b = −1: ⟦y = 2x² − x + 1⟧.'],
     'probe': 'x = −1: 2 · 1 + 1 + 1 = 4 ✓',
     'fehler': 'Den Punkt (−1 | 4) als a − b + c = −4 einzusetzen ist falsch: Der ⟦y-Wert⟧ steht rechts, (−1)² = ⟦+1⟧, also a − b + c = 4.'},
    {'lernziel': 'sachaufgabe', 'titel': 'Sachaufgaben mit drei Unbekannten',
     'regel': 'Lege ⟦drei Variablen⟧ fest, übersetze jede Angabe in eine Gleichung und löse das System. Antworte im ⟦Sachzusammenhang⟧.',
     'schritte': ['Drei Zahlen: Summe 12, die zweite ist doppelt so groß wie die erste, die dritte ist um 4 größer als die erste.',
                  'x + y + z = 12, y = 2x, z = x + 4 ⇒ 4x + 4 = 12 ⇒ ⟦x = 2, y = 4, z = 6⟧.'],
     'probe': '2 + 4 + 6 = 12 ✓',
     'fehler': '„Doppelt so groß wie die erste“ als x = 2y zu schreiben ist falsch: Die ⟦zweite⟧ Zahl ist das Doppelte, also y = 2x.'},
]


def g_pruefen(s):
    M, b, x = zufall_lgs()
    if s == 1:
        i = R.randrange(3)
        lhs = sum(M[i][k] * x[k] for k in range(3))
        return zahl(f'Setze (x | y | z) = ({dz(x[0])} | {dz(x[1])} | {dz(x[2])}) in die linke Seite von {lin(M[i], b[i])} ein. Welcher Wert ergibt sich?',
                    f'{" + ".join(f"{kl(M[i][k])} · {kl(x[k])}" for k in range(3))} = {dz(lhs)}.',
                    'Ersetze x, y und z durch die Zahlen und achte auf die Vorzeichen.', lhs,
                    ' + '.join(f'({M[i][k]}) * ({x[k]})' for k in range(3)))
    falsch = R.random() < 0.6
    t = list(x)
    if falsch:
        k = R.randrange(3)
        t[k] += R.choice([-2, -1, 1, 2])
    erf = [sum(M[i][k] * t[k] for k in range(3)) == b[i] for i in range(3)]
    if falsch and all(erf): return None
    if falsch:
        erste = NR[erf.index(False)]
        richtig = f'Nein, Gleichung ({erste}) ist nicht erfüllt.'
    else:
        richtig = 'Ja, alle drei Gleichungen sind erfüllt.'
    andere = ['Ja, alle drei Gleichungen sind erfüllt.'] + [f'Nein, Gleichung ({n}) ist nicht erfüllt.' for n in NR]
    if not falsch:
        w = 'Einsetzen: ' + '; '.join(f'({NR[i]}) {dz(b[i])} = {dz(b[i])} ✓' for i in range(3))
    else:
        w = 'Einsetzen: ' + '; '.join(f'({NR[i]}) {dz(sum(M[i][k] * t[k] for k in range(3)))} {"=" if erf[i] else "≠"} {dz(b[i])}' for i in range(3))
    if falsch and erf.count(False) > 1:
        # mehrere Gleichungen falsch: Antwort „die erste nicht erfüllte“ wäre mehrdeutig
        return None
    return auswahl(f'Ist ({dz(t[0])} | {dz(t[1])} | {dz(t[2])}) Lösung des Systems {system(M, b)}?', richtig, andere, w,
                   'Setze das Tripel in jede Gleichung ein.')


def g_stufenform(s):
    x = [R.randint(-6, 6) for _ in range(3)]
    if s == 1:
        a, d, h = 1, 1, R.randint(1, 4)
        bb, cc, f = R.randint(-3, 3), R.randint(-3, 3), R.randint(-3, 3)
    else:
        a, d, h = R.randint(1, 4), R.randint(1, 3), R.randint(1, 5) * R.choice([1, -1])
        bb, cc, f = R.randint(-4, 4), R.randint(-4, 4), R.randint(-4, 4)
    M = [[a, bb, cc], [0, d, f], [0, 0, h]]
    b = [sum(M[i][k] * x[k] for k in range(3)) for i in range(3)]
    if s == 3:
        text = f'Löse das System: (I) {lin([0, 0, h], b[2])}; (II) {lin([a, bb, cc], b[0])}; (III) {lin([0, d, f], b[1])}.'
        M_ = [[0, 0, h], [a, bb, cc], [0, d, f]]
        b_ = [b[2], b[0], b[1]]
        return luecken(text, LX, 'Werte von x, y, z', x,
                       f'Aus {lin([0, 0, h], b[2])}: z = {dz(x[2])}. Dann {lin([0, d, f], b[1])}: y = {dz(x[1])}. Dann x = {dz(x[0])}.',
                       'Suche die Gleichung mit nur einer Variablen und arbeite dich weiter.', c=cramer_c(M_, b_))
    return luecken(f'Löse das System in Stufenform: {system(M, b)}.', LX, 'Werte von x, y, z', x,
                   f'(III) z = {dz(b[2])} : {kl(h)} = {dz(x[2])}; (II) y = {dz(x[1])}; (I) x = {dz(x[0])}.',
                   'Beginne mit (III) und setze nach oben ein.', c=cramer_c(M, b))


def g_eliminieren(s):
    M, b, x = zufall_lgs(gr=4 if s > 1 else 3)
    i, j = R.sample(range(3), 2)
    a1, a2 = M[i][0], M[j][0]
    if a1 == 0 or a2 == 0: return None
    if s == 1:
        if a1 != a2 and a1 != -a2: return None
        k = 1 if a1 == a2 else -1
        op = '−' if k == 1 else '+'
        neu = [M[j][t] - k * M[i][t] for t in range(3)] + [b[j] - k * b[i]]
        anw = f'({NR[j]}) {op} ({NR[i]})'
    else:
        if a2 % a1 == 0:
            k = a2 // a1
            neu = [M[j][t] - k * M[i][t] for t in range(3)] + [b[j] - k * b[i]]
            anw = (f'({NR[j]}) − ({NR[i]})' if k == 1 else f'({NR[j]}) + ({NR[i]})' if k == -1 else
                   f'({NR[j]}) − {k} · ({NR[i]})' if k > 0 else f'({NR[j]}) + {-k} · ({NR[i]})')
        else:
            if a1 < 0: a1, a2 = -a1, -a2
            neu = [a1 * M[j][t] - a2 * M[i][t] for t in range(3)] + [a1 * b[j] - a2 * b[i]]
            f1 = '' if a1 == 1 else f'{a1} · '
            f2 = '' if abs(a2) == 1 else f'{abs(a2)} · '
            anw = f'{f1}({NR[j]}) {"−" if a2 > 0 else "+"} {f2}({NR[i]})'
            k = None
    assert neu[0] == 0
    if s == 3 and R.random() < 0.5:
        k2 = a2 // a1 if a2 % a1 == 0 else None
        if k2 is None or k2 in (0, 1, -1): return None
        falsch_rechts = b[j] - b[i]
        if falsch_rechts == neu[3]: return None
        return auswahl(f'Gegeben: ({NR[i]}) {lin(M[i], b[i])}; ({NR[j]}) {lin(M[j], b[j])}. Jemand berechnet ({NR[j]}) − {kl(k2)} · ({NR[i]}) und erhält {lin(neu[:3], falsch_rechts)}. Was stimmt?',
                       f'Falsch: Die rechte Seite muss {dz(b[j])} − {kl(k2)} · {kl(b[i])} = {dz(neu[3])} sein.',
                       ['Richtig, das ist die neue Gleichung.', f'Falsch: Das x hätte stehen bleiben müssen.',
                        f'Falsch: Die rechte Seite muss {dz(b[j] + b[i])} sein.'],
                       f'Auch die rechte Seite von ({NR[i]}) wird mit {kl(k2)} multipliziert: {dz(b[j])} − {kl(k2 * b[i])} = {dz(neu[3])}.',
                       'Wurde jedes Glied mit dem Faktor multipliziert?')
    return luecken(f'Gegeben: ({NR[i]}) {lin(M[i], b[i])}; ({NR[j]}) {lin(M[j], b[j])}. Berechne {anw}.', '□y + □z = □',
                   'Koeffizient von y, von z, rechte Seite (mit Vorzeichen)', neu[1:],
                   f'{anw}: x fällt weg, es bleibt {lin([0] + neu[1:3], neu[3])}.',
                   'Rechne Glied für Glied, auch auf der rechten Seite.',
                   c=([f'({M[j][t]}) - ({k}) * ({M[i][t]})' for t in (1, 2)] + [f'({b[j]}) - ({k}) * ({b[i]})'] if k is not None else
                      [f'({a1}) * ({M[j][t]}) - ({a2}) * ({M[i][t]})' for t in (1, 2)] + [f'({a1}) * ({b[j]}) - ({a2}) * ({b[i]})']))


def g_loesen(s):
    gr, lsg = {1: (1, 5), 2: (2, 6), 3: (3, 8)}[s]
    M, b, x = zufall_lgs(gr=gr, lsg=lsg)
    if s == 1 and sum(1 for row in M for c in row if c == 0) > 3: return None
    return luecken(f'Löse das Gleichungssystem: {system(M, b)}.', LX, 'Werte von x, y, z', x,
                   f'Eliminieren und Einsetzen ergibt x = {dz(x[0])}, y = {dz(x[1])}, z = {dz(x[2])}. Probe in allen drei Gleichungen.',
                   'Eliminiere mit zwei Gleichungspaaren dieselbe Variable.', c=cramer_c(M, b))


def g_parabel(s):
    a, bb, c = R.randint(-3, 3), R.randint(-5, 5), R.randint(-6, 6)
    if a == 0: return None
    if s == 1:
        xs = [0, 1, -1]
    elif s == 2:
        xs = R.choice([[0, 1, 2], [0, -1, 2], [0, 2, -2], [-1, 0, 1], [0, 1, 3]])
    else:
        xs = sorted(R.sample([-3, -2, -1, 1, 2, 3], 3))
    pts = [(t, a * t * t + bb * t + c) for t in xs]
    M = [[t * t, t, 1] for t, _ in pts]
    rhs = [y for _, y in pts]
    ptxt = ', '.join(f'({dz(t)} | {dz(y)})' for t, y in pts)
    return luecken(f'Die Parabel y = ax² + bx + c geht durch {ptxt}. Bestimme a, b und c.', 'a = □; b = □; c = □', 'Werte von a, b, c',
                   [a, bb, c], f'Einsetzen ergibt {system(M, rhs, ("a", "b", "c"))}. Lösung a = {dz(a)}, b = {dz(bb)}, c = {dz(c)}: y = {poly(a, bb, c)}.',
                   'Setze jeden Punkt ein: y-Wert links, x² vor a, x vor b.', c=cramer_c(M, rhs))


def g_sachaufgabe(s):
    typ = R.random()
    if s == 1:
        x = R.randint(1, 15)
        k, d = R.randint(2, 4), R.randint(1, 9)
        y, z = k * x, x + d
        return luecken(f'Drei Zahlen haben die Summe {x + y + z}. Die zweite ist {k}-mal so groß wie die erste, die dritte ist um {d} größer als die erste. Bestimme die Zahlen.',
                       LX.replace('x', 'erste').replace('y', 'zweite').replace('z', 'dritte'), 'erste, zweite, dritte Zahl', [x, y, z],
                       f'x + y + z = {x + y + z}, y = {k}x, z = x + {d} ⇒ {k + 2}x + {d} = {x + y + z} ⇒ x = {x}, y = {y}, z = {z}.',
                       'Drücke y und z durch x aus und setze in die Summe ein.',
                       c=cramer_c([[1, 1, 1], [-k, 1, 0], [-1, 0, 1]], [x + y + z, 0, d]))
    if s == 2 or typ < 0.5:
        e, k, r_ = R.randint(8, 20), R.randint(3, 10), R.randint(5, 15)
        if len({e, k, r_}) < 3: return None
        M = [[R.randint(1, 4), R.randint(1, 4), R.randint(1, 3)] for _ in range(3)]
        if det3(M) == 0: return None
        b = [M[i][0] * e + M[i][1] * k + M[i][2] * r_ for i in range(3)]
        gruppen = [f'{M[i][0]} Erwachsene, {M[i][1]} Kinder und {M[i][2]} Senioren zahlen {b[i]} €' for i in range(3)]
        return luecken(f'Im Zoo gilt: {"; ".join(gruppen)}. Wie viel kostet je eine Karte für Erwachsene, Kinder und Senioren?',
                       'Erwachsene □ €; Kinder □ €; Senioren □ €', 'Preise in Euro', [e, k, r_],
                       f'System {system(M, b, ("e", "k", "s"))} ergibt e = {e}, k = {k}, s = {r_}.',
                       'Eine Variable je Kartenart, eine Gleichung je Gruppe.', c=cramer_c(M, b))
    a_, b_, c_ = R.randint(1, 30), R.randint(1, 30), R.randint(1, 30)
    if len({a_, b_, c_}) < 3: return None
    s1, s2, s3 = a_ + b_, b_ + c_, a_ + c_
    return luecken(f'Drei Kisten A, B, C wiegen paarweise: A und B zusammen {s1} kg, B und C {s2} kg, A und C {s3} kg. Wie schwer ist jede Kiste?',
                   'A = □ kg; B = □ kg; C = □ kg', 'Massen von A, B, C', [a_, b_, c_],
                   f'Alle drei Gleichungen addieren: 2(A + B + C) = {s1 + s2 + s3} ⇒ A + B + C = {(s1 + s2 + s3) // 2}. Dann A = {a_}, B = {b_}, C = {c_}.',
                   'Addiere alle drei Gleichungen.', c=cramer_c([[1, 1, 0], [0, 1, 1], [1, 0, 1]], [s1, s2, s3]))


GEN = {'pruefen': g_pruefen, 'stufenform': g_stufenform, 'eliminieren': g_eliminieren, 'loesen': g_loesen,
       'parabel': g_parabel, 'sachaufgabe': g_sachaufgabe}

if __name__ == '__main__':
    bauen('gleichungen.lgs3',
          'Lineare Gleichungssysteme mit drei Unbekannten aufstellen und systematisch lösen, z. B. Parabel durch drei Punkte.',
          ['Lösung = Tripel, das alle drei Gleichungen erfüllt.', 'Additionsverfahren: Vielfache addieren/subtrahieren, bis eine Variable wegfällt.',
           'Zweimal dieselbe Variable eliminieren → System mit zwei Unbekannten.', 'Parabel durch drei Punkte: jeden Punkt in y = ax² + bx + c einsetzen.'],
          [('Grundlagen', ['pruefen', 'stufenform']), ('Lösungsverfahren', ['eliminieren', 'loesen']),
           ('Anwendungen', ['parabel', 'sachaufgabe'])],
          ETAPPEN, GEN,
          meiden={'parabel': ['(0 | 1), (1 | 2), (−1 | 4)']},
          offen=['Gleichungssysteme stehen in einer Zeile, getrennt durch „;“ und (I), (II), (III). Falls die App Zeilenumbrüche im Fragetext darstellen kann, untereinander schreiben.',
                 'Sonderfälle (keine oder unendlich viele Lösungen) sind nicht enthalten, weil der Lehrplan nur „aufstellen und lösen“ nennt.'])
