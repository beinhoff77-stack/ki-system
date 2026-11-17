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


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-1) ----------
# Prüfungsvorbilder: ISB „Leistungsaufgaben ohne Hilfsmittel“ Jahrgangsstufe 9 (I) (Wurzeln einordnen, Begriffe), Jahrgangsstufentest 9,
# Realschul-Abschlussprüfung (flächengleiche Figuren, Sachaufgaben mit Quadraten), Lehrplanformulierung „zu gegebenen Lösungsmengen
# passende reinquadratische Gleichungen formulieren“. Typ übernommen, Wortlaut und Zahlen eigen.
def durchsicht(d):
    import math
    from _rsib1 import Z, A, L, nachtrag, finde, rund
    T = lambda teil: finde(d, teil)
    XX = 'x₁ = □; x₂ = □'
    q90, c90 = rund(math.sqrt(90), 2)
    rk, ck = rund(math.sqrt(100 / math.pi), 2)
    r3, c3 = rund(2 * math.sqrt(3), 2)
    nachtrag(d,
        umstufen={
            T('Wie viele Lösungen hat x² − 25 = 0?'): 2,
            T('Wie lautet die exakte positive Lösung von x² = 236?'): 1,
            T('Wie lautet die exakte positive Lösung von x² = 172?'): 1,
            T('Eine quadratische Terrasse soll 136 m²'): 2,
            T('Eine quadratische Terrasse soll 147 m²'): 2,
            T('Wie lange fällt ein Stein 80 m tief?'): 1,
        },
        ersetzen={
            T('Jemand schätzt √238 ≈ 119.'):
                A(3, 'Ordne der Größe nach: √50, 7,2 und 7.', '7 < √50 < 7,2', ['√50 < 7 < 7,2', '7 < 7,2 < √50', '7,2 < 7 < √50'],
                  '7² = 49 < 50, also √50 > 7. 7,2² = 51,84 > 50, also √50 < 7,2.', 'Quadriere die Zahlen und vergleiche mit 50.'),
            T('Jemand schätzt √237 ≈ 118,5.'):
                Z(3, 'Wie viele ganze Zahlen liegen zwischen √10 und √90?', 6, '9 - 4 + 1',
                  '√10 liegt zwischen 3 und 4, √90 zwischen 9 und 10. Dazwischen: 4, 5, 6, 7, 8, 9 – sechs Zahlen.', 'Schätze beide Wurzeln ein.'),
            T('Welche Lösungsmenge hat 5x² + 6 = 0?'):
                L(3, 'Löse x² : 4 − 1 = 8.', XX, [-6, 6], ['-6', '6'], '+1: x² : 4 = 9. Mal 4: x² = 36. x = ±6.', 'Erst +1, dann mal 4.'),
            T('Eine quadratische Terrasse soll 58 m²'):
                Z(3, 'Ein quadratisches Grundstück wird an zwei anliegenden Seiten um je 2 m verbreitert. Danach ist es wieder quadratisch und 144 m² groß. Wie lang war eine Seite vorher?',
                  10, '12 - 2', 'Neue Seite: (x + 2)² = 144 ⇒ x + 2 = 12 (nur positiv) ⇒ x = 10 m.', 'Die neue Seite ist x + 2.', einheit='m'),
            T('Eine quadratische Terrasse soll 133 m²'):
                Z(3, 'Ein Würfel hat eine Oberfläche von 150 cm². Wie lang ist eine Kante?', 5, '150/6/5',
                  'Ein Würfel hat 6 gleiche Quadrate: 6a² = 150 ⇒ a² = 25 ⇒ a = 5 cm.', 'Aus wie vielen Quadraten besteht die Oberfläche?', einheit='cm'),
        },
        neu={
            'schaetzen': [
                A(3, 'Ein quadratisches Feld ist 300 m² groß. Ist eine Seite länger als 17 m?', 'Ja, denn 17² = 289 < 300.',
                  ['Nein, denn 17² = 289 < 300.', 'Nein, die Seite ist 150 m.', 'Ja, denn 300 : 17 > 17.'],
                  'Die Seite ist √300. Weil 17² = 289 kleiner als 300 ist, ist √300 größer als 17.', 'Vergleiche 17² mit 300.'),
                Z(3, '√a liegt zwischen 6 und 7. Wie viele ganze Zahlen a sind möglich?', 12, '48 - 37 + 1',
                  '36 < a < 49, also a = 37, 38, …, 48: zwölf Zahlen.', 'Quadriere die Grenzen.'),
            ],
            'grundform': [
                Z(3, 'Welche Zahl a muss in x² = a stehen, damit die Lösungen −1,5 und 1,5 sind?', 2.25, '1.5**2',
                  '1,5² = 2,25. Die Gleichung x² = 2,25 hat die Lösungen −1,5 und 1,5.', 'Quadriere eine der Lösungen.'),
                Z(3, 'Für welchen Wert von a hat die Gleichung x² = a − 4 genau eine Lösung?', 4, '4',
                  'Genau eine Lösung gibt es bei x² = 0. Also a − 4 = 0, a = 4. Die Lösung ist x = 0.', 'Wann hat x² = Zahl nur eine Lösung?'),
                A(3, 'Für welche a hat die Gleichung x² = a − 4 keine Lösung?', 'für a < 4', ['für a > 4', 'für a < 0', 'für a = 4'],
                  'Keine Lösung, wenn rechts eine negative Zahl steht: a − 4 < 0 ⇒ a < 4.', 'Wann ist die rechte Seite negativ?'),
            ],
            'umformen': [
                L(3, 'Löse 2(x² − 3) = x² + 10.', XX, [-4, 4], ['-4', '4'], 'Ausmultiplizieren: 2x² − 6 = x² + 10. −x², +6: x² = 16. x = ±4.',
                  'Erst die Klammer auflösen, dann alle x² auf eine Seite.'),
                Z(3, 'Für welche Zahl c hat die Gleichung 3x² + c = 0 die Lösungen −2 und 2?', -12, '-3*2**2',
                  'x = 2 einsetzen: 3 · 4 + c = 0 ⇒ c = −12.', 'Setze eine Lösung ein.'),
            ],
            'gerundet': [
                Z(3, 'Ein Rechteck ist 6 cm breit und 15 cm lang. Ein Quadrat soll denselben Flächeninhalt haben. Wie lang ist seine Seite? Runde auf zwei Dezimalen.',
                  q90, c90, 'Fläche 6 · 15 = 90 cm². a² = 90 ⇒ a = √90 ≈ 9,49 cm.', 'Berechne zuerst die Fläche.', einheit='cm', tol=0.01),
                Z(3, 'Ein Kreis soll denselben Flächeninhalt haben wie ein Quadrat mit 10 cm Seitenlänge. Berechne den Radius auf zwei Dezimalen.',
                  rk, ck, 'π · r² = 100 ⇒ r² = 100 : π ≈ 31,83 ⇒ r ≈ 5,64 cm.', 'Setze die Kreisfläche gleich 100 cm².', einheit='cm', tol=0.01),
                A(3, 'Jemand löst x² = 50 mit x ≈ 7,07 und macht die Probe: 7,07² = 49,9849. Warum kommt nicht genau 50 heraus?',
                  'Weil 7,07 ein gerundeter Wert ist.', ['Weil er sich verrechnet hat.', 'Weil x² = 50 keine Lösung hat.', 'Weil die richtige Lösung 25 ist.'],
                  '√50 = 7,0710… hat unendlich viele Nachkommastellen. Jede gerundete Zahl gibt im Quadrat nur ungefähr 50.',
                  'Wie viele Nachkommastellen hat √50?'),
                A(3, 'Zwischen welchen zwei Zahlen mit einer Dezimale liegt √30?', 'zwischen 5,4 und 5,5', ['zwischen 5,0 und 5,1', 'zwischen 5,5 und 5,6', 'zwischen 15,0 und 15,1'],
                  '5,4² = 29,16 < 30 und 5,5² = 30,25 > 30.', 'Quadriere die Kandidaten.'),
            ],
            'klammer': [
                L(3, 'Löse x² − 6x + 9 = 25.', XX, [-2, 8], ['3 - 5', '3 + 5'], 'Links steht (x − 3)². (x − 3)² = 25 ⇒ x − 3 = ±5 ⇒ x = −2 oder x = 8.',
                  'Erkennst du links eine binomische Formel?'),
                L(3, 'Für welchen Wert q hat (x − 4)² = q genau eine Lösung? Gib q und die Lösung an.', 'q = □; x = □', [0, 4], ['0', '4'],
                  'Nur (x − 4)² = 0 hat genau eine Lösung: x − 4 = 0 ⇒ x = 4.', 'Wann gibt es bei „Quadrat = Zahl“ nur eine Lösung?'),
            ],
            'sachaufgabe': [
                Z(3, 'Für den Bremsweg gilt näherungsweise s = v² : 100 (v in km/h, s in m). Ein Auto hat 49 m Bremsweg. Wie schnell war es?',
                  70, '7*10', 'v² : 100 = 49 ⇒ v² = 4 900 ⇒ v = 70 km/h (nur positiv).', 'Multipliziere zuerst mit 100.', einheit='km/h'),
                Z(3, 'Wie viele Sekunden länger fällt ein Stein aus 80 m Höhe als aus 20 m Höhe (s = 5 · t²)?', 2, '4 - 2',
                  '80 m: t² = 16, t = 4 s. 20 m: t² = 4, t = 2 s. Unterschied 2 s – vierfache Höhe heißt nur doppelte Zeit.',
                  'Rechne beide Fallzeiten aus.', einheit='s'),
                A(3, 'Der Flächeninhalt eines Quadrats wird vervierfacht. Wie ändert sich die Seitenlänge?', 'Sie verdoppelt sich.',
                  ['Sie vervierfacht sich.', 'Sie wird 16-mal so groß.', 'Sie bleibt gleich.'],
                  'Neue Fläche 4a² = (2a)². Die Seite ist also 2a.', 'Probiere es mit a = 3 aus.'),
                Z(3, 'Ein Kreis hat einen dreimal so großen Flächeninhalt wie ein Kreis mit r = 2 cm. Berechne seinen Radius auf zwei Dezimalen.',
                  r3, c3, 'π r² = 3 · π · 2² ⇒ r² = 12 ⇒ r = √12 ≈ 3,46 cm. π kürzt sich weg.', 'Setze die Flächen gleich; was passiert mit π?', einheit='cm', tol=0.01),
                Z(3, 'Ein Rechteck ist doppelt so lang wie breit und hat 98 cm² Flächeninhalt. Wie breit ist es?', 7, '7',
                  'Breite x, Länge 2x: 2x² = 98 ⇒ x² = 49 ⇒ x = 7 cm.', 'Nenne die Breite x. Wie lang ist das Rechteck dann?', einheit='cm'),
            ],
        })


# ---- STUFEN (Zwanzigste Runde, Zusatz RS/IB, Zweig stufen-rsib-1) ----
from _stufen_rsib1 import Stufen, stufen  # noqa: E402

ST = Stufen('gleichungen.reinquadratisch', 20_91_7)
Z, A, L = ST.Z, ST.A, ST.L
_X2 = 'x₁ = □; x₂ = □'

# schaetzen
ST.stufenleiter('schaetzen', 'Eine Wurzel zwischen zwei ganze Zahlen setzen, näher liegende Zahl erkennen, mit dem Taschenrechner runden.',
                'Ganze Zahlen zwischen zwei Wurzeln, Wurzeln und Dezimalzahlen ordnen, Seite eines Feldes einschätzen, auf Zehntel eingrenzen, größte Zahl unter einer Grenze.',
                'Fehler „Wurzel ist die Hälfte“, Anzahl ganzer Zahlen zwischen Wurzeln, √(a + b) ≠ √a + √b begründen, √a < a nur für a > 1, Mindestseite eines Rahmens, Prüfungsaufgabe.')
ST.typ('schaetzen', 'Zwischen welchen aufeinanderfolgenden', 'direkt')
ST.typ('schaetzen', 'Berechne √', 'direkt')
ST.typ('schaetzen', 'Liegt √', 'erkennen')
ST.typ('schaetzen', 'Jemand schätzt', 'fehler')
ST.typ('schaetzen', '/^(Welche ganzen Zahlen liegen|Ordne der Größe)/', 'mehrschritt')
ST.typ('schaetzen', 'Wie viele ganze Zahlen liegen', 'verknuepfen')
ST.typ('schaetzen', 'Ein quadratisches Feld', 'einkleidung')
ST.typ('schaetzen', '√a liegt zwischen', 'umkehr')
ST.neu('schaetzen', 'mehrschritt', A('Zwischen welchen Zahlen mit einer Dezimale liegt √12?', 'zwischen 3,4 und 3,5', ['zwischen 3,3 und 3,4', 'zwischen 3,5 und 3,6', 'zwischen 6,0 und 6,1'],
       '3,4² = 11,56 < 12 und 3,5² = 12,25 > 12. Also liegt √12 zwischen 3,4 und 3,5 (√12 ≈ 3,46).', 'Quadriere die Zahlen 3,4 und 3,5.'))
ST.neu('schaetzen', 'umkehr', Z('Welche ganze Zahl ist die größte, deren Quadratwurzel kleiner als 9 ist?', 80, '9 * 9 - 1',
       '√81 = 9 ist nicht mehr kleiner als 9. Die größte ganze Zahl darunter ist 80, √80 ≈ 8,94.', 'Welche Zahl hat genau die Wurzel 9?'))
ST.neu('schaetzen', 'begruenden', A('Stimmt: √(16 + 9) = √16 + √9?', 'Nein: √25 = 5, aber √16 + √9 = 4 + 3 = 7.', ['Ja, immer.', 'Ja, aber nur bei Quadratzahlen.', 'Nein: Die linke Seite ist größer.'],
       'Die Wurzel einer Summe ist nicht die Summe der Wurzeln. Rechne immer erst die Summe aus.', 'Rechne beide Seiten aus.'))
ST.neu('schaetzen', 'begruenden', A('Stimmt: √0,25 ist größer als 0,25?', 'Ja: √0,25 = 0,5, und 0,5 > 0,25.', ['Nein, eine Wurzel ist immer kleiner.', 'Nein, beide sind gleich.', 'Das kann man nicht sagen.'],
       '0,5 · 0,5 = 0,25. Bei Zahlen zwischen 0 und 1 ist die Wurzel größer als die Zahl selbst.', 'Welche Zahl ergibt mit sich selbst multipliziert 0,25?'))
ST.neu('schaetzen', 'parameter', A('Für welche Zahlen a > 0 ist √a kleiner als a?', 'für a > 1', ['für alle a > 0', 'für 0 < a < 1', 'für keine'],
       'Beispiele: √4 = 2 < 4, aber √0,25 = 0,5 > 0,25 und √1 = 1. Also nur für a > 1.', 'Probiere eine Zahl größer und eine kleiner als 1.'))
ST.neu('schaetzen', 'transfer', Z('Ein quadratischer Bilderrahmen soll mindestens 1 000 cm² Fläche haben und wird in ganzen Zentimetern gebaut. Wie lang muss eine Seite mindestens sein?', 32, '32',
       '31² = 961 ist zu wenig, 32² = 1 024 reicht. Also mindestens 32 cm.', 'Suche die passenden Quadratzahlen.', einheit='cm'))
ST.neu('schaetzen', 'pruefung', L('a) Zwischen welchen aufeinanderfolgenden ganzen Zahlen liegt √70? b) Liegt √70 näher an der kleineren (1) oder an der größeren Zahl (2)? c) Runde √70 auf eine Dezimale und gib das Ergebnis in Zehnteln an (8,4 als 84).',
       'a) □ und □; b) □; c) □', [8, 9, 1, 84], ['8', '9', '1', '84'],
       'a) 64 < 70 < 81. b) 70 liegt näher an 64, also näher an 8. c) √70 ≈ 8,37 ≈ 8,4.', 'Suche die Quadratzahlen um 70.'))
ST.knobel('schaetzen', Z('Wie viele natürliche Zahlen n zwischen 1 und 999 haben eine Quadratwurzel, die selbst eine natürliche Zahl ist?', 31, '31',
          'Das sind die Quadratzahlen 1, 4, 9, …, 961 = 31². 32² = 1 024 ist schon zu groß. Also 31 Zahlen.', 'Welche ist die größte Quadratzahl unter 1 000?'))
ST.knobel('schaetzen', A('Welche Zahl ist größer: √5 + √7 oder √3 + 3?', '√5 + √7', ['√3 + 3', 'Beide sind gleich.', 'Das kann man nicht entscheiden.'],
          'Quadrieren: (√5 + √7)² = 12 + 2√35 und (√3 + √9)² = 12 + 2√27. Wegen 35 > 27 ist die erste Summe größer (≈ 4,88 gegen ≈ 4,73).', 'Quadriere beide Summen.'))

# grundform
ST.stufenleiter('grundform', 'x² = a mit Quadratzahl a lösen; Anzahl der Lösungen erkennen.',
                'Brüche und Dezimalzahlen, a aus den Lösungen, Schnitt einer Parabel mit einer Waagrechten, Fenster als Sachsituation.',
                'Fehler „nur die positive Lösung“, Bedingungen an a, Summe der Lösungen begründen, Produkt aus Gegenzahlen, Umfang aus der Fläche, Prüfungsaufgabe.')
ST.typ('grundform', 'Löse x² = 100/49', 'mehrschritt')
ST.typ('grundform', 'Löse x²', 'direkt')
ST.typ('grundform', 'Wie viele Lösungen hat', 'erkennen')
ST.typ('grundform', 'Jemand löst', 'fehler')
ST.typ('grundform', 'Welche Zahl a muss', 'umkehr')
ST.typ('grundform', '/^Für welche[n]? (Wert von )?a/', 'parameter')
ST.neu('grundform', 'mehrschritt', A('Löse x² = 0,09.', 'x₁ = −0,3; x₂ = 0,3', ['x = 0,3', 'x₁ = −0,03; x₂ = 0,03', 'keine Lösung'],
       '0,3 · 0,3 = 0,09 und (−0,3) · (−0,3) = 0,09. 0,03² wäre 0,0009.', 'Wie viele Nachkommastellen hat das Quadrat von 0,3?'))
ST.neu('grundform', 'umkehr', Z('Die Gleichung x² = a hat die Lösung x = −0,7. Wie groß ist a?', 0.49, '0.7 * 0.7',
       'a = (−0,7)² = 0,49. Die zweite Lösung ist 0,7.', 'Setze die Lösung ein.'))
ST.neu('grundform', 'einkleidung', Z('Ein quadratisches Fenster hat 1,44 m² Glasfläche. Wie lang ist eine Seite?', 1.2, '1.2',
       's² = 1,44 ⇒ s = 1,2 m (die negative Lösung passt nicht zu einer Länge).', 'Welche Zahl ergibt quadriert 1,44?', einheit='m'))
ST.neu('grundform', 'darstellung', L('Die Normalparabel y = x² und die Gerade y = 49 schneiden sich. Gib die x-Werte der Schnittpunkte an.', _X2, [-7, 7], ['-7', '7'],
       'Schnittpunkte: x² = 49 ⇒ x = −7 oder x = 7.', 'Setze die beiden y gleich.'))
ST.neu('grundform', 'begruenden', A('Stimmt: Die beiden Lösungen von x² = a (a > 0) ergeben addiert immer 0?', 'Ja, denn sie heißen √a und −√a.', ['Nein, sie ergeben a.', 'Nein, sie ergeben 2√a.', 'Nur bei a = 1.'],
       '√a + (−√a) = 0. Die Lösungen liegen symmetrisch zur 0.', 'Wie heißen die beiden Lösungen?'))
ST.neu('grundform', 'transfer', Z('Zwei Zahlen unterscheiden sich nur im Vorzeichen. Ihr Produkt ist −36. Wie heißt die positive der beiden Zahlen?', 6, '6',
       'Die Zahlen sind x und −x. x · (−x) = −x² = −36 ⇒ x² = 36 ⇒ x = 6.', 'Nenne die positive Zahl x.'))
ST.neu('grundform', 'verknuepfen', Z('Ein Quadrat hat den Flächeninhalt 2,25 cm². Wie groß ist sein Umfang?', 6, '4 * 1.5',
       's² = 2,25 ⇒ s = 1,5 cm. Umfang 4 · 1,5 = 6 cm.', 'Erst die Seite, dann den Umfang.', einheit='cm'))
ST.neu('grundform', 'pruefung', L('Wie viele Lösungen haben die Gleichungen a) x² = 81, b) x² = 0, c) x² + 16 = 0?', 'a) □; b) □; c) □', [2, 1, 0], ['2', '1', '0'],
       'a) ±9: zwei. b) nur 0: eine. c) x² = −16: keine, denn ein Quadrat ist nie negativ.', 'Bringe jede Gleichung auf die Form x² = a.'))
ST.knobel('grundform', Z('Für wie viele ganze Zahlen x gilt x² ≤ 50?', 15, '2 * 7 + 1',
          '7² = 49 ≤ 50, 8² = 64 > 50. Also −7 ≤ x ≤ 7: das sind 15 ganze Zahlen (mit der 0).', 'Vergiss die negativen Zahlen und die 0 nicht.'))
ST.knobel('grundform', L('Löse x² = 2 025 ohne Taschenrechner.', _X2, [-45, 45], ['-45', '45'],
          '2 025 = 81 · 25 = 9² · 5² = (9 · 5)² = 45². Also x = 45 oder x = −45. Probe: 45 · 45 = 2 025.', 'Zerlege 2 025 in Faktoren, die Quadratzahlen sind.'))

# umformen
ST.stufenleiter('umformen', 'Gleichungen wie x² + c = d oder a · x² = b auf x² = … bringen und lösen; ersten Schritt erkennen.',
                'x² auf beiden Seiten, Faktoren und Brüche, Fliesen als Sachsituation, c aus den Lösungen.',
                'Fehler beim Teilen und beim gliedweisen Wurzelziehen, Sonderfall genau eine Lösung, Bedingung an c, Zahlenrätsel rückwärts, Quadrat plus Rechteck, (2x)², Prüfungsaufgabe.')
ST.typ('umformen', '/^Löse x² \\+ \\d+ = \\d+\\.$/', 'direkt')
ST.typ('umformen', 'Löse', 'mehrschritt')
ST.typ('umformen', 'Jemand löst', 'fehler')
ST.typ('umformen', 'Welche Lösungsmenge hat', 'erkennen')
ST.typ('umformen', 'Für welche Zahl c', 'umkehr')
ST.neu('umformen', 'erkennen', A('Was ist bei 3x² − 5 = 22 der erste Schritt?', '5 auf beiden Seiten addieren', ['durch 3 teilen', 'die Wurzel ziehen', '22 durch 5 teilen'],
       'Zuerst muss 3x² allein stehen: 3x² = 27. Dann durch 3: x² = 9. Dann Wurzel: x = ±3.', 'Was wurde mit x² zuletzt gemacht?'))
ST.neu('umformen', 'direkt', L('Löse 2x² = 50.', _X2, [-5, 5], ['-5', '5'], 'Durch 2: x² = 25 ⇒ x = ±5.', 'Teile durch 2.'))
ST.neu('umformen', 'einkleidung', Z('Vier gleich große quadratische Fliesen bedecken zusammen 0,36 m². Wie lang ist eine Fliesenseite in cm?', 30, '0.3 * 100',
       '4s² = 0,36 ⇒ s² = 0,09 ⇒ s = 0,3 m = 30 cm.', 'Stelle eine Gleichung für eine Fliese auf.', einheit='cm'))
ST.neu('umformen', 'begruenden', A('Stimmt: Die Gleichung 5x² + 3 = 3 hat genau eine Lösung?', 'Ja: 5x² = 0, also nur x = 0.', ['Nein, keine Lösung.', 'Nein, zwei Lösungen.', 'Nein, unendlich viele.'],
       '5x² + 3 = 3 ⇒ 5x² = 0 ⇒ x² = 0 ⇒ x = 0. Nur bei x² = 0 gibt es genau eine Lösung.', 'Forme um und schau, was rechts übrig bleibt.'))
ST.neu('umformen', 'parameter', A('Für welche Zahlen c hat x² + c = 10 zwei Lösungen?', 'für c < 10', ['für c > 10', 'für c = 10', 'für jedes c'],
       'x² = 10 − c. Zwei Lösungen gibt es, wenn 10 − c > 0, also c < 10.', 'Forme nach x² um.'))
ST.neu('umformen', 'rueckwaerts', Z('Denk dir eine Zahl, quadriere sie, multipliziere mit 3 und ziehe 7 ab. Du erhältst 68. Welche positive Zahl war es?', 5, '5',
       'Rückwärts: 68 + 7 = 75, 75 : 3 = 25, √25 = 5. Gleichung: 3x² − 7 = 68.', 'Mache die Schritte rückwärts.'))
ST.neu('umformen', 'transfer', Z('Ein quadratisches Grundstück und ein Rechteck von 4 m × 9 m haben zusammen 100 m² Fläche. Wie lang ist eine Seite des Quadrats?', 8, '8',
       'x² + 36 = 100 ⇒ x² = 64 ⇒ x = 8 m.', 'Stelle eine Gleichung für die Gesamtfläche auf.', einheit='m'))
ST.neu('umformen', 'fehler', A('Jemand löst x² − 9 = 16 so: „x − 3 = ±4.“ Was stimmt?', 'Falsch: Man darf nicht gliedweise die Wurzel ziehen. x² = 25, also x = ±5.',
       ['Richtig, also x = 7 oder x = −1.', 'Falsch: x = ±4.', 'Falsch: x = ±3.'], 'Erst 9 addieren: x² = 25, dann die Wurzel: x = ±5. Probe: 7² − 9 = 40 ≠ 16.', 'Mach die Probe mit x = 7.'))
ST.neu('umformen', 'verknuepfen', L('Löse (2x)² = 100.', _X2, [-5, 5], ['-5', '5'], '(2x)² = 4x² = 100 ⇒ x² = 25 ⇒ x = ±5.', 'Was ergibt (2x)² ausmultipliziert?'))
ST.neu('umformen', 'pruefung', L('Löse a) 2x² − 7 = 43; b) x² + 3 = 2x² − 61.', 'a) x₁ = □; x₂ = □; b) x₁ = □; x₂ = □', [-5, 5, -8, 8], ['-5', '5', '-8', '8'],
       'a) 2x² = 50 ⇒ x² = 25 ⇒ ±5. b) 3 + 61 = 2x² − x² ⇒ x² = 64 ⇒ ±8.', 'Bringe x² auf eine Seite.'))
ST.knobel('umformen', Z('Für wie viele natürliche Zahlen n hat n · x² = 72 ganzzahlige Lösungen?', 4, '4',
          'x² = 72 : n muss eine Quadratzahl sein: 1, 4, 9 oder 36 (Teiler von 72, die Quadratzahlen sind). Dann ist n = 72, 18, 8 oder 2. Also 4 Zahlen.', 'Welche Quadratzahlen sind Teiler von 72?'))
ST.knobel('umformen', Z('Wie viele Lösungen hat die Gleichung x² = 4x²?', 1, '1',
          'x² = 4x² ⇒ 0 = 3x² ⇒ x = 0. Nur eine Lösung. Wer durch x² teilt, bekommt 1 = 4 und meint „keine Lösung“ – dabei verliert man x = 0.', 'Nicht durch x² teilen.'))

# gerundet
ST.stufenleiter('gerundet', 'Die positive Lösung von x² = a mit dem Taschenrechner auf eine Dezimale runden; die exakte Lösung √a erkennen.',
                'Negative Lösung, zwei Dezimalen, erst umformen, Quadrat mit gleicher Fläche wie ein Rechteck, Zahl aus gerundeter Lösung.',
                'Klammern, Kreis mit gleicher Fläche, Probe mit gerundeten Werten begründen, Rundungsfehler finden, mögliche c bei gegebenem Rundungswert, Prüfungsaufgabe.')
ST.typ('gerundet', '/Gib die positive Lösung auf eine Dezimale/', 'direkt')
ST.typ('gerundet', 'Wie lautet die exakte', 'erkennen')
ST.typ('gerundet', '/^Löse (x² = \\d+\\. Gib die negative|\\dx²)/', 'mehrschritt')
ST.typ('gerundet', '/^(Löse \\(x \\+ \\d\\)²|Ein Kreis soll)/', 'verknuepfen')
ST.typ('gerundet', 'Ein Rechteck ist 6 cm breit', 'einkleidung')
ST.typ('gerundet', 'Jemand löst x² = 50', 'begruenden')
ST.typ('gerundet', 'Zwischen welchen zwei Zahlen', 'mehrschritt')
ST.neu('gerundet', 'umkehr', Z('Die positive Lösung von x² = c ist auf zwei Dezimalen gerundet 3,16. c ist eine ganze Zahl. Wie groß ist c?', 10, '10',
       '3,155² ≈ 9,95 und 3,165² ≈ 10,02. Die einzige ganze Zahl dazwischen ist 10 (√10 ≈ 3,162).', 'Quadriere 3,16 und überlege, welche ganze Zahl in Frage kommt.'))
ST.neu('gerundet', 'fehler', A('Jemand rundet √19 ≈ 4,358 auf eine Dezimale zu 4,3. Was stimmt?', 'Falsch: Die zweite Dezimale ist 5, also aufrunden: 4,4.', ['Richtig.', 'Falsch: 4,35.', 'Falsch: 4,0.'],
       'Bei 4,358 entscheidet die zweite Dezimale 5: aufrunden auf 4,4.', 'Welche Ziffer entscheidet beim Runden?'))
ST.neu('gerundet', 'parameter', A('Für welche ganzen Zahlen c ergibt die positive Lösung von x² = c auf eine Dezimale gerundet 7,1?', 'c = 50 und c = 51', ['nur c = 50', 'c = 49 bis c = 51', 'nur c = 51'],
       'Die Lösung muss zwischen 7,05 und 7,15 liegen: 7,05² ≈ 49,70 und 7,15² ≈ 51,12. Ganze Zahlen dazwischen: 50 und 51.', 'Welche Zahlen werden auf 7,1 gerundet? Quadriere die Grenzen.'))
ST.neu('gerundet', 'begruenden', A('Stimmt: √2 · √2 ergibt genau 2, aber 1,41 · 1,41 nicht?', 'Ja: 1,41 ist gerundet, 1,41² = 1,9881.', ['Nein, beides ist genau 2.', 'Nein, √2 · √2 = 4.', 'Nein, 1,41 · 1,41 = 2,01.'],
       '√2 ist eine unendliche Dezimalzahl. Mit der gerundeten 1,41 wird das Quadrat etwas zu klein.', 'Rechne 1,41 · 1,41 aus.'))
ST.neu('gerundet', 'pruefung', L('Löse 3x² − 5 = 100. a) Gib x² an. b) Gib die positive Lösung auf zwei Dezimalen gerundet in Hundertsteln an (5,92 als 592).', 'a) x² = □; b) □', [35, 592], ['105 // 3', '592'],
       'a) 3x² = 105 ⇒ x² = 35. b) √35 ≈ 5,916 ≈ 5,92.', 'Erst x² allein, dann der Taschenrechner.'))
ST.knobel('gerundet', Z('Für wie viele ganze Zahlen c ergibt die positive Lösung von x² = c auf eine Dezimale gerundet genau 10,0?', 2, '2',
          'Die Lösung muss zwischen 9,95 und 10,05 liegen: 9,95² ≈ 99,0 und 10,05² ≈ 101,0. Ganze Zahlen: 100 und 101 (99 liegt mit 9,9499 knapp darunter). Also 2.', 'Quadriere die Rundungsgrenzen.'))
ST.knobel('gerundet', A('Die positive Lösung von x² = 2 liegt zwischen 1,41 und 1,42. Zwischen welchen Zahlen liegt die positive Lösung von x² = 200?', 'zwischen 14,1 und 14,2',
          ['zwischen 141 und 142', 'zwischen 1,41 und 1,42', 'zwischen 28,2 und 28,4'], '200 = 2 · 100, also √200 = √2 · 10. Die Grenzen werden mit 10 multipliziert.', 'Schreibe 200 als 2 mal eine Quadratzahl.'))

# klammer
ST.stufenleiter('klammer', '(x − d)² = c mit Quadratzahl c lösen: zwei Gleichungen aufschreiben.',
                'Faktoren und Zahlen vor der Klammer, binomischen Term erkennen, vergrößerter Teppich.',
                'Fehler „nur eine Lösung“, Bedingungen an q, Unterschied (x − 3)² = 16 und x − 3 = 4 begründen, Wurf als Modell, Abstand der Nullstellen, d aus den Lösungen, Prüfungsaufgabe.')
ST.typ('klammer', 'Löse (', 'direkt')
ST.typ('klammer', '/^Löse \\d\\(/', 'mehrschritt')
ST.typ('klammer', 'Löse x² − 6x + 9', 'darstellung')
ST.typ('klammer', 'Welche Lösungsmenge hat', 'erkennen')
ST.typ('klammer', 'Jemand löst', 'fehler')
ST.typ('klammer', 'Für welchen Wert q', 'parameter')
ST.neu('klammer', 'erkennen', A('Welche zwei Gleichungen entstehen beim Wurzelziehen aus (x − 2)² = 9?', 'x − 2 = 3 oder x − 2 = −3', ['x − 2 = 9 oder x − 2 = −9', 'x = 3 oder x = −3', 'x − 2 = 3 oder x + 2 = 3'],
       'Wurzel aus 9 ist 3 oder −3: x − 2 = ±3, also x = 5 oder x = −1.', 'Welche Zahlen ergeben quadriert 9?'))
ST.neu('klammer', 'einkleidung', Z('Ein quadratischer Teppich wird an jeder Seite um 1 m breiter gemacht (die Seitenlänge wächst also um 2 m) und ist dann 25 m² groß. Wie lang war eine Seite vorher?', 3, '5 - 2',
       '(x + 2)² = 25 ⇒ x + 2 = 5 (Länge positiv) ⇒ x = 3 m.', 'Stelle die Gleichung mit der neuen Seitenlänge auf.', einheit='m'))
ST.neu('klammer', 'begruenden', A('Stimmt: (x − 3)² = 16 und x − 3 = 4 haben dieselben Lösungen?', 'Nein: Die erste hat zwei Lösungen (7 und −1), die zweite nur x = 7.',
       ['Ja, beide haben x = 7.', 'Ja, beide haben x = 7 und x = −1.', 'Nein, die zweite hat keine Lösung.'], 'Aus (x − 3)² = 16 folgt x − 3 = 4 oder x − 3 = −4. Wer nur die positive Wurzel nimmt, verliert x = −1.', 'Prüfe x = −1 in beiden Gleichungen.'))
ST.neu('klammer', 'transfer', Z('Ein Ball wird geworfen, seine Höhe ist h = 20 − 5(t − 1)² (h in m, t in s). Nach wie vielen Sekunden landet er (h = 0)?', 3, '1 + 2',
       '20 − 5(t − 1)² = 0 ⇒ (t − 1)² = 4 ⇒ t − 1 = 2 (die Zeit nach dem Wurf) ⇒ t = 3 s. Die Lösung t = −1 passt nicht.', 'Setze h = 0.', einheit='s'))
ST.neu('klammer', 'verknuepfen', Z('Die Parabel y = (x − 3)² − 16 schneidet die x-Achse zweimal. Wie weit liegen die Schnittpunkte auseinander?', 8, '7 - (-1)',
       '(x − 3)² = 16 ⇒ x = 7 oder x = −1. Abstand 7 − (−1) = 8.', 'Löse (x − 3)² − 16 = 0.'))
ST.neu('klammer', 'rueckwaerts', Z('Die Gleichung (x − d)² = 9 hat die Lösungen 1 und 7. Wie groß ist d?', 4, '(1 + 7) // 2',
       'Die Lösungen liegen symmetrisch um d: d − 3 = 1 und d + 3 = 7 ⇒ d = 4.', 'Die Lösungen liegen gleich weit links und rechts von d.'))
ST.neu('klammer', 'parameter', A('Für welche Zahlen q hat (x + 2)² = q keine Lösung?', 'für q < 0', ['für q > 0', 'für q = 0', 'für q < −2'],
       'Ein Quadrat ist nie negativ. Für q < 0 gibt es keine Lösung, für q = 0 genau eine (x = −2), für q > 0 zwei.', 'Kann ein Quadrat negativ sein?'))
ST.neu('klammer', 'pruefung', L('Löse a) (x + 4)² = 49; b) 2(x − 1)² = 50.', 'a) x₁ = □; x₂ = □; b) x₁ = □; x₂ = □', [-11, 3, -4, 6], ['-4 - 7', '-4 + 7', '1 - 5', '1 + 5'],
       'a) x + 4 = ±7 ⇒ x = −11 oder 3. b) (x − 1)² = 25 ⇒ x − 1 = ±5 ⇒ x = −4 oder 6.', 'Bei b) zuerst durch 2 teilen.'))
ST.knobel('klammer', Z('Löse (x − 5)² = (x − 1)².', 3, '3',
          'Zwei Quadrate sind gleich, wenn die Zahlen gleich oder Gegenzahlen sind. x − 5 = x − 1 ist unmöglich. x − 5 = −(x − 1) ⇒ 2x = 6 ⇒ x = 3. Das ist die Mitte zwischen 1 und 5.', 'Gleiche Quadrate – welche Möglichkeiten gibt es?'))
ST.knobel('klammer', Z('Für wie viele ganze Zahlen x gilt (x − 3)² < 10?', 7, '7',
          '(x − 3)² < 10 heißt: x − 3 liegt zwischen −√10 und √10 ≈ ±3,16. Ganze Werte für x − 3: −3 bis 3, also x = 0, 1, …, 6: sieben Zahlen.', 'Welche ganzen Zahlen haben ein Quadrat unter 10?'))

# sachaufgabe
ST.stufenleiter('sachaufgabe', 'Seite eines Quadrats aus der Fläche und Fallzeit aus s = 5 · t² bestimmen; passende Gleichung erkennen.',
                'Gerundete Seiten und Fallzeiten, Radius eines Beets, Fallweg aus der Zeit.',
                'Verbreitertes Grundstück rückwärts, Fehler „π vergessen“, Würfel und Bremsweg als Modelle, Zeitdifferenzen, Vervierfachen begründen, Kreis mit dreifacher Fläche, Rechteck mit Seitenverhältnis, Prüfungsaufgabe Fall.')
ST.typ('sachaufgabe', 'Ein quadratisches Grundstück hat', 'direkt')
ST.typ('sachaufgabe', 'Für den Fallweg gilt', 'direkt')
ST.typ('sachaufgabe', '/^(Eine quadratische Terrasse|Ein Apfel)/', 'einkleidung')
ST.typ('sachaufgabe', 'Ein kreisrundes Beet', 'mehrschritt')
ST.typ('sachaufgabe', 'Für ein kreisrundes Beet', 'fehler')
ST.typ('sachaufgabe', 'Ein quadratisches Grundstück wird', 'rueckwaerts')
ST.typ('sachaufgabe', '/^(Ein Würfel hat|Für den Bremsweg|Ein Rechteck ist doppelt)/', 'transfer')
ST.typ('sachaufgabe', '/^(Wie viele Sekunden länger|Ein Kreis hat einen dreimal)/', 'verknuepfen')
ST.typ('sachaufgabe', 'Der Flächeninhalt eines Quadrats', 'begruenden')
ST.neu('sachaufgabe', 'erkennen', A('Ein quadratischer Platz hat 400 m² Fläche. Welche Gleichung beschreibt seine Seitenlänge s?', 's² = 400', ['2s = 400', '4s = 400', 's = 400²'],
       'Fläche eines Quadrats = s · s = s². Also s² = 400, s = 20 m. 4s = 400 wäre der Umfang.', 'Wie berechnet man die Fläche eines Quadrats?'))
ST.neu('sachaufgabe', 'umkehr', Z('Ein Stein fällt 4 Sekunden lang (s = 5 · t²). Wie tief fällt er?', 80, '5 * 4 * 4',
       's = 5 · 4² = 5 · 16 = 80 m.', 'Setze t ein.', einheit='m'))
ST.neu('sachaufgabe', 'pruefung', L('Für den freien Fall gilt s = 5 · t². a) Wie tief fällt ein Stein in 3 s? b) Wie lange braucht er für 125 m?', 'a) □ m; b) □ s', [45, 5], ['5 * 9', '5'],
       'a) 5 · 9 = 45 m. b) 5t² = 125 ⇒ t² = 25 ⇒ t = 5 s.', 'Bei b) eine reinquadratische Gleichung lösen.'))
ST.knobel('sachaufgabe', Z('Ein quadratischer Rasen ist ringsum von einem 1 m breiten Weg umgeben. Rasen und Weg zusammen bedecken 144 m². Wie lang ist eine Seite des Rasens?', 10, '12 - 2',
          'Rasen und Weg bilden ein Quadrat mit 144 m², also Seite 12 m. Der Weg nimmt auf jeder Seite 1 m weg: 12 − 2 = 10 m. Der Weg allein hat 144 − 100 = 44 m².', 'Wie lang ist die Seite des großen Quadrats?', einheit='m'))
ST.knobel('sachaufgabe', Z('Aus welcher Höhe fällt ein Stein doppelt so lange wie aus 20 m Höhe (s = 5 · t²)?', 80, '4 * 20',
          'Aus 20 m: 5t² = 20 ⇒ t = 2 s. Doppelt so lange: 4 s ⇒ s = 5 · 16 = 80 m. Doppelte Zeit heißt vierfache Höhe, weil t im Quadrat steht.', 'Was bewirkt das Quadrat bei der doppelten Zeit?', einheit='m'))


if __name__ == '__main__':
    d = bauen('gleichungen.reinquadratisch',
          'Wurzeln einschätzen und reinquadratische Gleichungen x² = a lösen: zwei, eine oder keine Lösung, exakt oder gerundet.',
          ['x² = a: für a > 0 zwei Lösungen ±√a, für a = 0 eine (x = 0), für a < 0 keine.',
           'Erst nach x² auflösen, dann die Wurzel ziehen.', '(x − p)² = q ⇒ x = p ± √q.',
           'Im Sachzusammenhang zählt meist nur die positive Lösung.'],
          [('Wurzeln', ['schaetzen']), ('Gleichungen lösen', ['grundform', 'umformen', 'gerundet', 'klammer']), ('Anwenden', ['sachaufgabe'])],
          ETAPPEN, GEN)
    umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
    durchsicht(d)
    stufen('gleichungen.reinquadratisch', ST)
