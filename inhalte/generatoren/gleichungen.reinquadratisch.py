#!/usr/bin/env python3
"""Thema gleichungen.reinquadratisch – Reinquadratische Gleichungen (Realschule Bayern, Klasse 9)."""
import math
import sys
from math import isqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _rs import *  # noqa: E402,F403

start(1201)
L2, H2 = 'x₁ = □; x₂ = □', 'kleinere Lösung zuerst'
QUADRATE = {i * i for i in range(0, 40)}


def nz(n):
    return R.choice([i for i in range(-n, n + 1) if i != 0])


def kein_quadrat(lo, hi):
    while True:
        a = R.randint(lo, hi)
        if a not in QUADRATE: return a


def wurzel_c(a, nd):
    """Rechenausdruck für eine gerundete Wurzel (Literal mit 12 Stellen)."""
    return f'round({math.sqrt(a):.12f}, {nd})'


ETAPPEN = [
    {'lernziel': 'schaetzen', 'titel': 'Wurzeln einschätzen',
     'regel': '√a ist die ⟦nichtnegative⟧ Zahl, die quadriert a ergibt. Liegt a zwischen zwei Quadratzahlen, liegt √a zwischen deren Wurzeln: Aus ⟦49 < 55 < 64⟧ folgt ⟦7 < √55 < 8⟧. Wie bei einem quadratischen Teppich mit 55 m²: Die Seite ist etwas länger als 7 m.',
     'bild': {'typ': 'zahlenstrahl', 'start': 6, 'ende': 9, 'abschnitte': 3, 'beschriftet': 'alle'},
     'schritte': ['√55: Quadratzahlen in der Nähe sind 49 = 7² und 64 = 8².', '49 < 55 < 64, also ⟦7 < √55 < 8⟧. Weil 55 näher an 49 liegt, ist √55 ⟦näher an 7⟧ (√55 ≈ 7,42).'],
     'probe': '7,42² = 55,0564 ≈ 55 ✓',
     'fehler': '√55 ≈ 27,5 ist falsch: Die Wurzel ist ⟦nicht die Hälfte⟧. Gesucht ist die Zahl, die ⟦mit sich selbst⟧ malgenommen 55 ergibt.'},
    {'lernziel': 'grundform', 'titel': 'x² = a lösen',
     'regel': 'Die Gleichung ⟦x² = a⟧ hat für a > 0 ⟦zwei Lösungen⟧: x₁ = −√a und x₂ = √a. Für a = 0 gibt es ⟦eine⟧ Lösung (x = 0), für a < 0 ⟦keine⟧ – kein Quadrat ist negativ.',
     'schritte': ['x² = 81: Sowohl 9² = 81 als auch (−9)² = 81.', 'Also ⟦x₁ = −9; x₂ = 9⟧, L = {−9; 9}.'],
     'probe': '(−9)² = 81 ✓ und 9² = 81 ✓',
     'fehler': 'x² = 81 ⇒ x = 9 ist ⟦unvollständig⟧: Auch (−9)² = 81. Die negative Lösung darf nicht fehlen.'},
    {'lernziel': 'umformen', 'titel': 'Erst nach x² auflösen',
     'regel': 'Steht nicht x² allein, formst du zuerst um wie bei linearen Gleichungen, bis ⟦x² = Zahl⟧ dasteht. ⟦Erst dann⟧ ziehst du die Wurzel.',
     'schritte': ['3x² − 20 = 55 | + 20 ⇒ 3x² = 75 | : 3 ⇒ x² = 25.', 'Also ⟦x₁ = −5; x₂ = 5⟧.'],
     'probe': '3 · 25 − 20 = 55 ✓',
     'fehler': '3x² = 75 ⇒ x = ±√75 ist falsch: Vor dem Wurzelziehen muss x² ⟦allein⟧ stehen. Erst durch 3 teilen: x² = 25, x = ±5.'},
    {'lernziel': 'gerundet', 'titel': 'Lösungen runden',
     'regel': 'Ist a keine Quadratzahl, sind die Lösungen von x² = a ⟦irrationale Zahlen⟧. Du gibst sie exakt als ⟦±√a⟧ an oder ⟦gerundet⟧ mit dem Taschenrechner.',
     'schritte': ['x² = 30 ⇒ x = ±√30.', 'Taschenrechner: √30 = 5,4772… Auf zwei Dezimalen: ⟦x₁ ≈ −5,48; x₂ ≈ 5,48⟧.'],
     'probe': '5,48² = 30,0304 ≈ 30 ✓',
     'fehler': '√30 ≈ 5,47 ist falsch gerundet: Die dritte Dezimale ist 7, also wird ⟦aufgerundet⟧ auf 5,48.'},
    {'lernziel': 'klammer', 'titel': 'Quadrat einer Klammer: (x − p)² = q',
     'regel': 'Bei ⟦(x − p)² = q⟧ ziehst du die Wurzel aus beiden Seiten: ⟦x − p = −√q oder x − p = √q⟧. Dann p auf die andere Seite bringen.',
     'schritte': ['(x − 3)² = 16 ⇒ x − 3 = −4 oder x − 3 = 4.', 'x₁ = 3 − 4 = ⟦−1⟧, x₂ = 3 + 4 = ⟦7⟧.'],
     'probe': '(−1 − 3)² = (−4)² = 16 ✓ und (7 − 3)² = 16 ✓',
     'fehler': '(x − 3)² = 16 ⇒ x² − 9 = 16 ist falsch: Eine Klammer quadriert man mit der ⟦binomischen Formel⟧ – oder man zieht direkt die Wurzel.'},
    {'lernziel': 'sachaufgabe', 'titel': 'Sachaufgaben mit x² = a',
     'regel': 'Viele Formeln enthalten ein Quadrat: Quadratfläche ⟦A = a²⟧, Kreisfläche ⟦A = π · r²⟧, Fallweg ⟦s = 5 · t²⟧ (s in m, t in s). Stell nach dem Quadrat um, zieh die Wurzel – und nimm im Sachzusammenhang nur die ⟦positive⟧ Lösung.',
     'schritte': ['Ein Stein fällt 45 m tief: 5 · t² = 45 ⇒ t² = 9.', 't = 3 (die Lösung −3 passt nicht zu einer Zeit). Er fällt ⟦3 Sekunden⟧.'],
     'probe': '5 · 3² = 45 ✓',
     'fehler': 'Als Fallzeit „t = −3 s oder t = 3 s“ anzugeben ist falsch: Eine Zeitdauer ist ⟦positiv⟧. Die negative Lösung fällt im Sachzusammenhang weg.'},
]


# ---------- Generatoren ----------
def g_schaetzen(s):
    a = kein_quadrat(2, 300 if s > 1 else 99)
    n = isqrt(a)
    if s == 1:
        return luecken(f'Zwischen welchen aufeinanderfolgenden ganzen Zahlen liegt √{a}?', f'□ < √{a} < □', 'kleinere Zahl zuerst', [n, n + 1],
                       f'{n}² = {n * n} < {a} < {(n + 1) ** 2} = {n + 1}², also {n} < √{a} < {n + 1}.',
                       'Suche die Quadratzahlen direkt unter und über der Zahl.', c=[str(n), str(n + 1)])
    if s == 2:
        if R.random() < 0.5:
            naeher = n if a - n * n < (n + 1) ** 2 - a else n + 1
            if a - n * n == (n + 1) ** 2 - a: return None
            return auswahl(f'Liegt √{a} näher an {n} oder an {n + 1}?', f'näher an {naeher}', [f'näher an {2 * n + 1 - naeher}', 'genau in der Mitte'],
                           f'{n}² = {n * n}, {n + 1}² = {(n + 1) ** 2}. {a} liegt näher an {naeher * naeher}, also √{a} näher an {naeher}. (√{a} ≈ {dz(round(math.sqrt(a), 2))})',
                           'Vergleiche die Abstände zu den Quadratzahlen.')
        r = round(math.sqrt(a), 1)
        if gerundet(math.sqrt(a), 1) is None: return None
        return zahl(f'Berechne √{a} mit dem Taschenrechner und runde auf eine Dezimale.', f'√{a} = {dz(round(math.sqrt(a), 4))}… ≈ {dz(r)}. Probe: {dz(r)}² = {dz(round(r * r, 2))}.',
                    f'Es muss zwischen {n} und {n + 1} liegen.', r, wurzel_c(a, 1))
    art = R.random()
    if art < 0.4:
        m = R.randint(4, 15)
        b = m * m
        return luecken(f'Welche ganzen Zahlen liegen zwischen √{b - R.randint(1, m)} und √{b + R.randint(1, m)}? Gib die einzige ganze Zahl an.', '□',
                       'eine ganze Zahl', [m], f'Die Zahlen unter den Wurzeln liegen dicht um {b} = {m}². Also liegt nur {m} dazwischen.',
                       'Welche Quadratzahl liegt zwischen den beiden Zahlen unter der Wurzel?', c=[str(m)])
    if art < 0.7:
        return auswahl(f'Jemand schätzt √{a} ≈ {dz(Fr(a, 2))}. Was stimmt?', f'Falsch: √{a} liegt zwischen {n} und {n + 1}.',
                       ['Richtig, die Wurzel ist die Hälfte.', f'Falsch: √{a} ≈ {dz(Fr(a, 4))}.', f'Falsch: √{a} liegt zwischen {n - 1} und {n}.'],
                       f'{dz(Fr(a, 2))}² ist viel größer als {a}. Wegen {n * n} < {a} < {(n + 1) ** 2} gilt {n} < √{a} < {n + 1}.',
                       'Mach die Probe: Quadriere den Schätzwert.')
    k = R.choice([100, 10000])
    b = R.randint(2, 9) ** 2
    return zahl(f'Berechne ohne Taschenrechner: √{dz(b * k)}.', f'√{dz(b * k)} = √{b} · √{dz(k)} = {isqrt(b)} · {isqrt(k)} = {dz(isqrt(b) * isqrt(k))}.',
                'Zerlege in eine Quadratzahl mal 100 bzw. 10 000.', isqrt(b) * isqrt(k), f'{isqrt(b)} * {isqrt(k)}')


def g_grundform(s):
    r = R.randint(1, 15 if s > 1 else 12)
    if s == 1:
        return luecken(f'Löse x² = {r * r}.', L2, H2, [-r, r], f'Sowohl {r}² als auch (−{r})² ergeben {r * r}: x₁ = −{r}; x₂ = {r}.',
                       'Welche Zahl ergibt quadriert diese Zahl? Denk an beide Vorzeichen.', c=[f'-{r * r} / {r}', f'{r * r} / {r}'])
    if s == 2:
        art = R.random()
        if art < 0.3:
            return auswahl(f'Wie viele Lösungen hat x² = −{r * r}?', 'keine', ['eine', 'zwei', 'unendlich viele'],
                           f'Ein Quadrat ist nie negativ, also gibt es keine Zahl mit x² = −{r * r}. L = {{ }}.', 'Kann ein Quadrat negativ sein?')
        if art < 0.5:
            return auswahl('Welche Lösungsmenge hat x² = 0?', 'L = {0}', ['L = { }', 'L = {−1; 1}', 'L = {0; 1}'],
                           'Nur 0² = 0. Es gibt genau eine Lösung.', 'Welche Zahl ergibt quadriert 0?') if R.random() < 0.3 else None
        q = Fr(r, R.choice([10, 2, 5]))
        if not endlich(q * q) or q.denominator == 1: return None
        return auswahl(f'Löse x² = {dz(q * q)}.', f'x₁ = {dz(-q)}; x₂ = {dz(q)}',
                       [f'x = {dz(q)}', f'x₁ = {dz(-q * q / 2)}; x₂ = {dz(q * q / 2)}' if endlich(q * q / 2) else f'x₁ = {dz(-q * 10)}; x₂ = {dz(q * 10)}', 'keine Lösung'],
                       f'{dz(q)}² = {dz(q * q)} und ({dz(-q)})² = {dz(q * q)}.', 'Auch bei Dezimalzahlen: zwei Lösungen mit verschiedenen Vorzeichen.')
    art = R.random()
    if art < 0.4:
        return auswahl(f'Jemand löst x² = {r * r} so: x = {r}. Was stimmt?', f'Unvollständig: Auch x = −{r} ist eine Lösung.',
                       ['Richtig, das ist die einzige Lösung.', f'Falsch: x = {r * r // 2 if r * r % 2 == 0 else r + 1}.', f'Falsch: x = −{r} ist die einzige Lösung.'],
                       f'(−{r})² = {r * r}. L = {{−{r}; {r}}}.', 'Probe mit der Gegenzahl.')
    if art < 0.7:
        a = R.choice([r * r, -r * r, 0])
        anz = 'zwei' if a > 0 else ('keine' if a < 0 else 'eine')
        return auswahl(f'Wie viele Lösungen hat x² {plus(-a) if a else ""} = 0?'.replace('  ', ' '), anz, [x for x in ['keine', 'eine', 'zwei'] if x != anz] + ['drei'],
                       f'Umgeformt: x² = {dz(a)}. ' + ('Positiv: zwei Lösungen.' if a > 0 else ('Null: eine Lösung (x = 0).' if a == 0 else 'Negativ: keine Lösung.')),
                       'Stelle nach x² um und schau auf das Vorzeichen.')
    p = Fr(r, R.choice([2, 3, 5, 7]))
    if p.denominator == 1: return None
    return luecken(f'Löse x² = {br(p * p)}. Gib die positive Lösung als Bruch an.', '□/□', 'Zähler und Nenner (gekürzt)', [p.numerator, p.denominator],
                   f'√({br(p * p)}) = √{(p * p).numerator} : √{(p * p).denominator} = {br(p)}. Lösungen x = ±{br(p)}.',
                   'Wurzel aus Zähler und Nenner getrennt ziehen.', c=[str(p.numerator), str(p.denominator)])


def g_umformen(s):
    r = R.randint(1, 10)
    if s == 1:
        b = R.randint(1, 50)
        return luecken(f'Löse x² + {b} = {r * r + b}.', L2, H2, [-r, r], f'x² = {r * r + b} − {b} = {r * r}, also x = ±{r}.',
                       'Bringe die Zahl auf die andere Seite.', c=[f'-{r}', str(r)])
    a = R.randint(2, 7)
    b = R.randint(-40, 40)
    c = a * r * r + b
    w = f'{a}x² {plus(b)} = {dz(c)} ⇔ {a}x² = {dz(a * r * r)} ⇔ x² = {r * r} ⇔ x = ±{r}.'
    if s == 2:
        if R.random() < 0.5:
            return luecken(f'Löse {a}x² {plus(b)} = {dz(c)}.', L2, H2, [-r, r], w, 'Erst die Zahl wegbringen, dann durch den Faktor teilen.',
                           c=[f'-{r}', str(r)])
        return luecken(f'Löse {a + 1}x² − {dz(c)} = x² {plus(-b)}.', L2, H2, [-r, r],
                       f'{a + 1}x² − x² = {dz(c)} {plus(-b)} ⇔ {a}x² = {dz(a * r * r)} ⇔ x² = {r * r} ⇔ x = ±{r}.',
                       'Alle x² auf eine Seite, alle Zahlen auf die andere.', c=[f'-{r}', str(r)])
    art = R.random()
    if art < 0.35:
        return auswahl(f'Jemand löst {a}x² = {dz(a * r * r)} so: x = ±√{dz(a * r * r)}. Was stimmt?',
                       f'Falsch: Erst durch {a} teilen: x² = {r * r}, also x = ±{r}.',
                       ['Richtig.', f'Falsch: x = ±{dz(Fr(a * r * r, 2))}.', f'Falsch: x = {r}, nur positiv.'],
                       f'{a}x² = {dz(a * r * r)} ⇔ x² = {r * r}. Erst dann die Wurzel: x = ±{r}.', 'Steht x² schon allein?')
    if art < 0.7:
        d = R.randint(1, 30)
        return auswahl(f'Welche Lösungsmenge hat {a}x² + {d} = 0?', 'L = { }',
                       [f'L = {{−{dz(Fr(d, a))}; {dz(Fr(d, a))}}}' if endlich(Fr(d, a)) else 'L = {0}', 'L = {0}', f'L = {{−{d}; {d}}}'],
                       f'{a}x² = −{d} ⇔ x² = −{br(Fr(d, a))}. Ein Quadrat ist nie negativ, also keine Lösung.',
                       'Stelle nach x² um. Ist die rechte Seite negativ?')
    # mit Dezimalfaktor
    q = R.choice([2, 4, 5])
    return luecken(f'Löse {dz(Fr(1, q))}x² = {dz(Fr(r * r, q))}.', L2, H2, [-r, r],
                   f'{dz(Fr(1, q))}x² = {dz(Fr(r * r, q))} | · {q} ⇒ x² = {r * r} ⇒ x = ±{r}.', f'Multipliziere beide Seiten mit {q}.', c=[f'-{r}', str(r)])


def g_gerundet(s):
    a = kein_quadrat(2, 99 if s == 1 else 400)
    nd = 1 if s == 1 else 2
    x = math.sqrt(a)
    if gerundet(x, nd) is None: return None
    r = round(x, nd)
    if s == 1:
        return zahl(f'Löse x² = {a}. Gib die positive Lösung auf eine Dezimale gerundet an.', f'x = ±√{a}; √{a} = {dz(round(x, 4))}… ≈ {dz(r)}.',
                    'Taschenrechner: Wurzeltaste. Dann runden.', r, wurzel_c(a, 1))
    if s == 2:
        k = R.randint(2, 6)
        b = R.randint(-30, 30)
        if R.random() < 0.5:
            return zahl(f'Löse {k}x² {plus(b)} = {dz(k * a + b)}. Gib die positive Lösung auf zwei Dezimalen gerundet an.',
                        f'{k}x² = {dz(k * a)} ⇔ x² = {a} ⇔ x = ±√{a} ≈ ±{dz(r)}.', 'Erst nach x² auflösen, dann Wurzel ziehen und runden.', r, wurzel_c(a, 2))
        return zahl(f'Löse x² = {a}. Gib die negative Lösung auf zwei Dezimalen gerundet an.', f'x = ±√{a} ≈ ±{dz(r)}. Negative Lösung: {dz(-r)}.',
                    'Die negative Lösung ist die Gegenzahl der positiven.', -r, f'-{wurzel_c(a, 2)}', toleranz=0.01)
    art = R.random()
    if art < 0.4:
        falsch = math.floor(x * 100) / 100
        if round(falsch, 2) == r: return None
        return auswahl(f'Jemand gibt als Lösung von x² = {a} an: x ≈ ±{dz(round(falsch, 2))}. Was stimmt?', f'Falsch gerundet: x ≈ ±{dz(r)}.',
                       ['Richtig.', f'Falsch: Es gibt nur x ≈ {dz(round(falsch, 2))}.', f'Falsch: x ≈ ±{dz(round(a / 2, 2))}.'],
                       f'√{a} = {dz(round(x, 4))}… Die dritte Dezimale ist ≥ 5, also aufrunden: {dz(r)}.', 'Schau auf die dritte Dezimale.')
    if art < 0.7:
        p = nz(6)
        return zahl(f'Löse (x {plus(-p)})² = {a}. Gib die größere Lösung auf zwei Dezimalen gerundet an.',
                    f'x {plus(-p)} = ±√{a} ⇒ x = {dz(p)} ± √{a}. Größere Lösung: {dz(p)} + {dz(round(x, 4))}… ≈ {dz(round(p + x, 2))}.',
                    'Wurzel ziehen, dann die Zahl aus der Klammer auf die andere Seite bringen.', round(p + x, 2), f'round({p} + {x:.12f}, 2)') \
            if gerundet(p + x, 2) is not None else None
    return auswahl(f'Wie lautet die exakte positive Lösung von x² = {a}?', f'√{a}', [f'{dz(r)}', f'{dz(Fr(a, 2))}', f'{a}²'],
                   f'Exakt ist nur √{a}; {dz(r)} ist ein gerundeter Wert, denn √{a} ist eine irrationale Zahl.',
                   'Exakt heißt: ohne zu runden.')


def g_klammer(s):
    p, r = nz(9), R.randint(1, 9)
    x1, x2 = p - r, p + r
    if s == 1:
        p = R.randint(1, 9)
        x1, x2 = p - r, p + r
        return luecken(f'Löse (x − {p})² = {r * r}.', L2, H2, [x1, x2], f'x − {p} = ±{r}: x₁ = {p} − {r} = {dz(x1)}, x₂ = {p} + {r} = {dz(x2)}.',
                       'Ziehe zuerst die Wurzel: Die Klammer ist ± die Wurzel.', c=[f'{p} - {r}', f'{p} + {r}'])
    if s == 2:
        return luecken(f'Löse {minus_klammer(p)}² = {r * r}.', L2, H2, [x1, x2],
                       f'{minus_klammer(p)[1:-1]} = ±{r}: x₁ = {dz(p)} − {r} = {dz(x1)}, x₂ = {dz(p)} + {r} = {dz(x2)}.',
                       'Achte auf das Vorzeichen in der Klammer.', c=[f'({p}) - {r}', f'({p}) + {r}'])
    art = R.random()
    if art < 0.35:
        k = R.randint(2, 4)
        b = R.randint(-20, 20)
        return luecken(f'Löse {k}{minus_klammer(p)}² {plus(b)} = {dz(k * r * r + b)}.', L2, H2, [x1, x2],
                       f'{k}{minus_klammer(p)}² = {dz(k * r * r)} ⇔ {minus_klammer(p)}² = {r * r} ⇔ x = {dz(p)} ± {r}: x₁ = {dz(x1)}, x₂ = {dz(x2)}.',
                       'Erst die Klammer² allein stellen.', c=[f'({p}) - {r}', f'({p}) + {r}'])
    if art < 0.7:
        return auswahl(f'Welche Lösungsmenge hat {minus_klammer(p)}² = −{r * r}?', 'L = { }',
                       [f'L = {{{dz(x1)}; {dz(x2)}}}', f'L = {{{dz(p)}}}', f'L = {{{dz(-r)}; {dz(r)}}}'],
                       f'Ein Quadrat kann nicht −{r * r} ergeben. Keine Lösung.', 'Kann ein Quadrat negativ sein?')
    return auswahl(f'Jemand löst {minus_klammer(p)}² = {r * r} so: {minus_klammer(p)[1:-1]} = {r}, also x = {dz(x2)}. Was stimmt?',
                   f'Unvollständig: Auch {minus_klammer(p)[1:-1]} = −{r}, also x = {dz(x1)}.',
                   ['Richtig, das ist die einzige Lösung.', f'Falsch: Richtig ist nur x = {dz(x1)}.', f'Falsch: x = {dz(r - p)}.'],
                   f'Die Klammer kann {r} oder −{r} sein: x = {dz(x2)} oder x = {dz(x1)}.', 'Welche Zahlen ergeben quadriert ' + str(r * r) + '?')


def g_sachaufgabe(s):
    art = R.choice(['quadrat', 'fall', 'kreis']) if s > 1 else R.choice(['quadrat', 'fall'])
    if art == 'quadrat':
        if s == 1:
            a = R.randint(3, 25)
            return zahl(f'Ein quadratisches Grundstück hat {dz(a * a)} m² Fläche. Wie lang ist eine Seite?', f'a² = {dz(a * a)} ⇒ a = √{dz(a * a)} = {a} m (nur positiv).',
                        'A = a². Welche Zahl ergibt quadriert die Fläche?', a, f'{a * a} / {a}', einheit='m')
        A = kein_quadrat(10, 150)
        if gerundet(math.sqrt(A), 1) is None: return None
        r = round(math.sqrt(A), 1)
        return zahl(f'Eine quadratische Terrasse soll {A} m² groß werden. Wie lang wird eine Seite? Runde auf eine Dezimale.',
                    f'a² = {A} ⇒ a = √{A} ≈ {dz(r)} m.', 'Wurzel aus der Fläche, dann runden.', r, wurzel_c(A, 1), einheit='m')
    if art == 'fall':
        t = R.randint(1, 6)
        if s == 1 or R.random() < 0.5:
            return zahl(f'Für den Fallweg gilt näherungsweise s = 5 · t² (s in m, t in s). Wie lange fällt ein Stein {5 * t * t} m tief?',
                        f'5t² = {5 * t * t} ⇒ t² = {t * t} ⇒ t = {t} s (nur positiv).', 'Teile durch 5, dann Wurzel.', t, f'({5 * t * t} / 5) / {t}', einheit='s')
        h = R.choice([12, 18, 22, 28, 33, 40, 55, 70, 90])
        x = math.sqrt(h / 5)
        if gerundet(x, 1) is None: return None
        return zahl(f'Ein Apfel fällt aus {h} m Höhe. Wie lange dauert der Fall (s = 5 · t²)? Runde auf eine Dezimale.',
                    f'5t² = {h} ⇒ t² = {dz(Fr(h, 5))} ⇒ t = √{dz(Fr(h, 5))} ≈ {dz(round(x, 1))} s.', 'Nach t² umstellen, dann Wurzel ziehen.',
                    round(x, 1), f'round({x:.12f}, 1)', einheit='s')
    A = R.choice([50, 80, 100, 150, 200, 250, 300, 500])
    x = math.sqrt(A / math.pi)
    if gerundet(x, 1) is None: return None
    if R.random() < 0.5:
        return zahl(f'Ein kreisrundes Beet soll {A} m² groß werden. Welchen Radius braucht es? Runde auf eine Dezimale.',
                    f'π · r² = {A} ⇒ r² = {A} : π ≈ {dz(round(A / math.pi, 2))} ⇒ r ≈ {dz(round(x, 1))} m.', 'A = π · r². Erst durch π teilen, dann Wurzel.',
                    round(x, 1), f'round({x:.12f}, 1)', einheit='m')
    r0 = round(x, 1)
    return auswahl(f'Für ein kreisrundes Beet mit {A} m² rechnet jemand: r = √{A} ≈ {dz(round(math.sqrt(A), 1))} m. Was stimmt?',
                   f'Falsch: Erst durch π teilen; r ≈ {dz(r0)} m.', ['Richtig.', f'Falsch: r ≈ {dz(round(A / math.pi, 1))} m.', f'Falsch: r ≈ {dz(round(math.sqrt(A) / 2, 1))} m.'],
                   f'π · r² = {A} ⇒ r² = {A} : π ⇒ r = √({A} : π) ≈ {dz(r0)} m.', 'Wo steckt das π in der Formel?')


GEN = {'schaetzen': g_schaetzen, 'grundform': g_grundform, 'umformen': g_umformen, 'gerundet': g_gerundet,
       'klammer': g_klammer, 'sachaufgabe': g_sachaufgabe}

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import tab  # noqa: E402


def _zs(a, b, n, **kw):
    return {'typ': 'zahlenstrahl', 'start': a, 'ende': b, 'abschnitte': n, 'beschriftet': kw.pop('beschriftet', 'anfang_ende'), **kw}


def _pk(*w):
    return [{'wert': x, 'name': n} for x, n in w]


_UF = [['Start', '3x² + 20 = 95'], ['− 20', '3x² = 75'], [': 3', 'x² = 25'], ['Wurzel', 'x = −5 oder x = 5']]
UMBAU = {
    'schaetzen': {
        'einstieg': 'Ein quadratischer Teppich hat 55 m² Fläche. Wie lang ist eine Seite? Gesucht ist die Zahl, '
                    'die mit sich selbst malgenommen 55 ergibt. Sie heißt ⟦Wurzel⟧ aus 55.',
        'woerter': [['Wurzel', '√55: die positive Zahl, die mal sich selbst 55 ergibt'],
                    ['Quadratzahl', 'eine Zahl wie 49 = 7 · 7 oder 64 = 8 · 8']],
        'bild': _zs(6, 9, 3, beschriftet='alle'),
        'schritte': [
            {'text': 'Quadratzahlen in der Nähe: 49 = 7 · 7 und 64 = 8 · 8.'},
            {'text': '49 < 55 < 64, also ⟦7 < √55 < 8⟧.', 'bild': {'bereich': {'von': 7, 'bis': 8}}},
            {'text': '55 liegt näher an 49, also ist √55 näher an 7: etwa 7,4.', 'bild': {'punkte': _pk((7.42, '√55'))}},
        ],
        'fehler': '√55 ≈ 27,5 ist falsch, die Wurzel ist ⟦nicht die Hälfte⟧. 27,5 · 27,5 wäre viel mehr als 55.',
        'regel': 'Wurzel einschätzen: Quadratzahlen links und rechts suchen. Aus ⟦49 < 55 < 64⟧ folgt 7 < √55 < 8.',
    },
    'grundform': {
        'einstieg': 'Eine quadratische Fliese hat 81 cm². Rechnerisch passen zwei Zahlen: 9 · 9 = 81 und (−9) · (−9) = 81. '
                    'Die Gleichung x² = 81 hat deshalb ⟦zwei Lösungen⟧.',
        'woerter': [['x₁ und x₂', 'erste und zweite Lösung; die kleine Zahl ist nur eine Nummer'],
                    ['Lösungsmenge L', 'alle Lösungen in einer Mengenklammer, z. B. L = {−9; 9}']],
        'bild': _zs(-10, 10, 20),
        'schritte': [
            {'text': '9² = 81 und auch (−9)² = 81.'},
            {'text': 'Die Lösungen heißen x₁ und x₂: ⟦x₁ = −9; x₂ = 9⟧.',
             'bild': {'punkte': _pk((-9, 'x₁'), (9, 'x₂')), 'boegen': [{'von': 0, 'bis': -9, 'name': '9'}, {'von': 0, 'bis': 9, 'name': '9'}]}},
            {'text': 'Lösungsmenge L = {−9; 9}.'},
            {'text': 'x² = 0: nur x = 0. x² = −4: ⟦keine Lösung⟧.', 'bild': {'punkte': _pk((0, 'x² = 0')), 'boegen': None}},
        ],
        'fehler': 'x² = 81, also x = 9, ist ⟦unvollständig⟧. Auch (−9)² = 81, die negative Lösung darf nicht fehlen.',
        'fehler_bild': {'punkte': _pk((-9, 'fehlt'), (9, 'x = 9')), 'boegen': None},
        'regel': 'Für a > 0 hat x² = a ⟦zwei Lösungen⟧. Sie heißen −√a und √a, für a < 0 gibt es keine.',
    },
    'umformen': {
        'einstieg': 'Drei gleiche quadratische Fliesen und ein Reststück von 20 cm² bedecken zusammen 95 cm². '
                    'Wie lang ist eine Fliese? Erst x² allein stellen, dann die ⟦Wurzel ziehen⟧.',
        'woerter': [['x² allein', 'auf einer Seite steht nur noch x², sonst nichts'],
                    ['Wurzel ziehen', 'aus x² = 25 wird x = −5 oder x = 5']],
        'bild': tab(['', 'Gleichung'], _UF[0]),
        'schritte': [
            {'text': 'Minus 20 auf beiden Seiten: 3x² = 75.', 'bild': tab(['', 'Gleichung'], *_UF[:2])},
            {'text': 'Durch 3 teilen: x² = 25. Jetzt steht x² allein.', 'bild': tab(['', 'Gleichung'], *_UF[:3])},
            {'text': 'Wurzel ziehen: ⟦x₁ = −5; x₂ = 5⟧.', 'bild': tab(['', 'Gleichung'], *_UF)},
            {'text': 'Eine Fliese ist also 5 cm lang.'},
        ],
        'fehler': 'Aus 3x² = 75 nicht sofort die Wurzel ziehen. Erst muss x² ⟦allein⟧ stehen: durch 3 teilen, x² = 25.',
        'fehler_bild': tab(['', 'Gleichung'], _UF[1], ['falsch', 'x = ±√75'], ['richtig', 'x² = 25']),
        'regel': 'Erst umformen, bis ⟦x² = Zahl⟧ dasteht. Dann die Wurzel ziehen, mit beiden Vorzeichen.',
    },
    'gerundet': {
        'einstieg': 'Ein quadratisches Beet soll 30 m² groß werden. 30 ist keine Quadratzahl, √30 hat unendlich viele Nachkommastellen. '
                    'Für den Zollstock reicht ein ⟦gerundeter⟧ Wert.',
        'woerter': [['irrationale Zahl', 'eine Zahl mit unendlich vielen Nachkommastellen ohne Muster, z. B. √30'],
                    ['±', 'plus oder minus: ±√30 steht für −√30 und √30']],
        'bild': _zs(5, 6, 10),
        'schritte': [
            {'text': 'x² = 30, also x = ±√30, eine irrationale Zahl.'},
            {'text': 'Taschenrechner: √30 = 5,4772…', 'bild': {'punkte': _pk((5.4772, '√30'))}},
            {'text': 'Zwei Dezimalen: Die dritte ist 7, also aufrunden auf 5,48.'},
            {'text': 'Lösungen: ⟦x₁ ≈ −5,48; x₂ ≈ 5,48⟧.'},
        ],
        'fehler': '√30 ≈ 5,47 ist falsch gerundet. Die dritte Dezimale ist 7, also wird ⟦aufgerundet⟧: 5,48.',
        'fehler_bild': {'start': 5.4, 'ende': 5.5, 'abschnitte': 10, 'punkte': _pk((5.4772, '√30'))},
        'regel': 'Ist a keine Quadratzahl, gibt es nur gerundete Werte. Exakt schreibst du ⟦±√a⟧.',
    },
    'klammer': {
        'einstieg': 'Eine Spielfigur steht auf Feld 3. Sie zieht so weit, dass das Quadrat der Strecke 16 ist. '
                    'Die Strecke ist also 4, nach links oder rechts. Das beschreibt ⟦(x − 3)² = 16⟧.',
        'woerter': [['x − 3', 'wie weit x von Feld 3 entfernt ist (mit Richtung)']],
        'bild': _zs(-2, 8, 10, beschriftet='alle', punkte=_pk((3, 'Start'))),
        'schritte': [
            {'text': 'Wurzel ziehen: x − 3 = −4 oder x − 3 = 4.'},
            {'text': 'Erste Lösung: x₁ = 3 − 4 = ⟦−1⟧.',
             'bild': {'punkte': _pk((3, 'Start'), (-1, 'x₁')), 'boegen': [{'von': 3, 'bis': -1, 'name': '4'}]}},
            {'text': 'Zweite Lösung: x₂ = 3 + 4 = ⟦7⟧.',
             'bild': {'punkte': _pk((3, 'Start'), (-1, 'x₁'), (7, 'x₂')),
                      'boegen': [{'von': 3, 'bis': -1, 'name': '4'}, {'von': 3, 'bis': 7, 'name': '4'}]}},
        ],
        'fehler': '(x − 3)² ist nicht x² − 9. Ohne binomische Formel lieber direkt die ⟦Wurzel ziehen⟧.',
        'regel': 'Bei (x − p)² = q direkt die Wurzel ziehen. Dann ist ⟦x = p − √q oder x = p + √q⟧.',
    },
    'sachaufgabe': {
        'einstieg': 'Ein Stein fällt in einen 45 m tiefen Brunnen. Für den Fallweg gilt ungefähr s = 5 · t². '
                    'Wie lange fällt er? Eine negative Zeit ergibt hier ⟦keinen Sinn⟧.',
        'woerter': [['Fallweg', 's: wie viele Meter der Stein gefallen ist'],
                    ['t', 'die Zeit in Sekunden seit dem Loslassen']],
        'bild': tab(['t in s', '0', '1', '2', '?'], ['s in m', '0', '5', '20', '45']),
        'schritte': [
            {'text': '5 · t² = 45, durch 5 teilen: t² = 9.'},
            {'text': 'Wurzel ziehen: t = −3 oder t = 3.'},
            {'text': 'Eine Zeit ist nie negativ, also ⟦t = 3⟧: drei Sekunden.',
             'bild': tab(['t in s', '0', '1', '2', '3'], ['s in m', '0', '5', '20', '45'])},
        ],
        'fehler': '„t = −3 s oder t = 3 s“ ist falsch. Eine Zeitdauer ist ⟦positiv⟧, die negative Lösung fällt weg.',
        'regel': 'Nach dem Quadrat umstellen und die Wurzel ziehen. Im Sachzusammenhang zählt meist nur die ⟦positive Lösung⟧.',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


if __name__ == '__main__':
    d = bauen('gleichungen.reinquadratisch',
          'Wurzeln einschätzen und reinquadratische Gleichungen x² = a lösen: zwei, eine oder keine Lösung, exakt oder gerundet.',
          ['x² = a: für a > 0 zwei Lösungen ±√a, für a = 0 eine (x = 0), für a < 0 keine.',
           'Erst nach x² auflösen, dann die Wurzel ziehen.', '(x − p)² = q ⇒ x = p ± √q.',
           'Im Sachzusammenhang zählt meist nur die positive Lösung.'],
          [('Wurzeln', ['schaetzen']), ('Gleichungen lösen', ['grundform', 'umformen', 'gerundet', 'klammer']), ('Anwenden', ['sachaufgabe'])],
          ETAPPEN, GEN)
    umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
