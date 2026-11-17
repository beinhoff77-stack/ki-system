#!/usr/bin/env python3
"""Thema funktionen.folgen – Folgen (IB MYP 4, etwa Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403
from _rsib2 import PLAN2, art3  # noqa: E402

start(4104)

TIEF = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')


def a(n):
    """a mit tiefgestelltem Index: a(5) = 'a₅', a('n') = 'aₙ', a('n+1') = 'aₙ₊₁'."""
    if isinstance(n, int): return 'a' + str(n).translate(TIEF)
    return 'a' + n.replace('n', 'ₙ').replace('+', '₊').replace('-', '₋').translate(TIEF)


def folge_txt(xs):
    return '; '.join(dz(x) for x in xs) + '; …'


ETAPPEN = [
    {'lernziel': 'explizit', 'titel': 'Folgenglieder berechnen',
     'regel': 'Eine ⟦Folge⟧ (sequence) ist eine geordnete Liste von Zahlen, den ⟦Gliedern⟧ (terms) a₁, a₂, a₃, … Bei einer ⟦expliziten Formel⟧ (general term) für aₙ setzt man für n die ⟦Platznummer⟧ ein.',
     'schritte': ['aₙ = 3n − 2. Gesucht: a₅.', 'n = 5 einsetzen: 3 · 5 − 2 = ⟦13⟧.'],
     'probe': 'a₁ = 1, a₂ = 4, a₃ = 7, a₄ = 10, a₅ = 13 ✓',
     'bild': {'typ': 'tabelle', 'kopf': ['n', '1', '2', '3', '4', '5'], 'zeilen': [['aₙ = 3n − 2', '1', '4', '7', '10', '13']]},
     'fehler': 'a₅ als „fünfte Zahl in 3n − 2 einsetzen“ mit n = 13 zu verwechseln ist falsch: ⟦n ist die Platznummer⟧, aₙ ist der Wert an diesem Platz.'},
    {'lernziel': 'rekursiv', 'titel': 'Rekursiv weiterrechnen',
     'regel': 'Eine ⟦rekursive Formel⟧ (recursive formula) sagt, wie man aus einem Glied das ⟦nächste⟧ erhält, z. B. aₙ₊₁ = aₙ + 4. Dazu braucht man einen ⟦Startwert⟧ a₁. Man rechnet Schritt für Schritt.',
     'schritte': ['a₁ = 5, aₙ₊₁ = 2 · aₙ − 1.', 'a₂ = 2 · 5 − 1 = 9; a₃ = 2 · 9 − 1 = 17.', 'a₄ = 2 · 17 − 1 = ⟦33⟧.'],
     'probe': 'Jedes Glied aus dem vorigen berechnet ✓',
     'fehler': 'a₄ = 2 · 4 − 1 = 7 ist falsch: In der rekursiven Formel setzt man ⟦das vorige Glied⟧ ein, nicht die Platznummer.'},
    {'lernziel': 'arithmetisch', 'titel': 'Arithmetische Folgen',
     'regel': 'Bei einer ⟦arithmetischen Folge⟧ (arithmetic sequence) kommt immer ⟦dieselbe Zahl d⟧ dazu (die Differenz, common difference). Explizit: ⟦aₙ = a₁ + (n − 1) · d⟧.',
     'schritte': ['Folge 7; 11; 15; 19; … : d = 11 − 7 = 4.', 'a₂₀ = 7 + (20 − 1) · 4 = 7 + 76 = ⟦83⟧.'],
     'probe': 'a₄ = 7 + 3 · 4 = 19 ✓',
     'fehler': 'a₂₀ = 7 + 20 · 4 = 87 ist falsch: Von a₁ bis a₂₀ sind es nur ⟦19 Schritte⟧, also (n − 1) · d.'},
    {'lernziel': 'geometrisch', 'titel': 'Geometrische Folgen',
     'regel': 'Bei einer ⟦geometrischen Folge⟧ (geometric sequence) wird immer mit ⟦demselben Faktor q⟧ multipliziert (common ratio): q = a₂ : a₁. Explizit: ⟦aₙ = a₁ · qⁿ⁻¹⟧.',
     'schritte': ['Folge 3; 6; 12; 24; … : q = 6 : 3 = 2.', 'a₇ = 3 · 2⁶ = 3 · 64 = ⟦192⟧.'],
     'probe': '24 · 2 · 2 · 2 = 192 ✓',
     'fehler': 'a₇ = 3 · 2⁷ = 384 ist falsch: Von a₁ bis a₇ wird nur ⟦6-mal⟧ mit q multipliziert, also qⁿ⁻¹ = q⁶.'},
    {'lernziel': 'erkennen', 'titel': 'Folgen erkennen und prüfen',
     'regel': 'Prüfe ⟦Differenzen⟧ aufeinanderfolgender Glieder (gleich → arithmetisch) und ⟦Quotienten⟧ (gleich → geometrisch). Ist beides nicht konstant, ist die Folge ⟦weder noch⟧ – z. B. Quadratzahlen 1; 4; 9; 16.',
     'schritte': ['Folge 2; 6; 18; 54: Differenzen 4; 12; 36 – nicht gleich.', 'Quotienten 3; 3; 3 – gleich. ⟦Geometrisch mit q = 3⟧.'],
     'probe': '54 · 3 = 162 wäre das nächste Glied ✓',
     'fehler': 'Aus zwei Gliedern allein auf die Art zu schließen ist falsch: Bei 1; 4 könnte d = 3 oder q = 4 sein. Man braucht ⟦mindestens drei Glieder⟧.'},
]


def g_explizit(s):
    art = R.choice({1: ['linear', 'linear'], 2: ['quadrat', 'erste', 'quadrat'], 3: ['welches_n', 'quadrat', 'differenz']}[s])  # Durchsicht 19
    m, t = R.choice([2, 3, 4, 5, -2, -3, 6]), R.choice([x for x in range(-9, 13) if x])
    if art == 'linear':
        n = R.randint(2, 15) if s == 1 else R.randint(10, 40)
        return zahl(f'{a("n")} = {poly(m, t, v="n")}. Berechne {a(n)}.', f'n = {n} einsetzen: {kl(m)} · {n} {plus(t)} = {dz(m * n + t)}.',
                    'Setze die Platznummer für n ein.', m * n + t, f'{m} * {n} + ({t})')
    if art == 'quadrat':
        k, c = R.choice([1, 2, 3, -1]), R.randint(-5, 5)
        n = R.randint(3, 12)
        return zahl(f'{a("n")} = {poly(k, 0, c, v="n")}. Berechne {a(n)}.', f'{a(n)} = {"" if k == 1 else ("−" if k == -1 else dz(k) + " · ")}{n}² {plus(c) if c else ""} = {dz(k * n * n + c)}.'.replace('  ', ' '),
                    'Erst n quadrieren, dann den Rest.', k * n * n + c, f'{k} * {n} ** 2 + ({c})')
    if art == 'erste':
        xs = [m * i + t for i in range(1, 5)]
        return luecken(f'Gib die ersten drei Glieder von {a("n")} = {poly(m, t, v="n")} an.', f'{a(1)} = □; {a(2)} = □; {a(3)} = □', 'drei ganze Zahlen', xs[:3],
                       f'n = 1, 2, 3 einsetzen: {dz(xs[0])}; {dz(xs[1])}; {dz(xs[2])}.', 'Setze nacheinander n = 1, n = 2, n = 3 ein.',
                       c=[f'{m} * {i} + ({t})' for i in (1, 2, 3)])
    if art == 'welches_n':
        if m < 0: m = -m
        n = R.randint(8, 40)
        wert_ = m * n + t
        return zahl(f'{a("n")} = {poly(m, t, v="n")}. Das wievielte Glied hat den Wert {dz(wert_)}?', f'{poly(m, t, v="n")} = {dz(wert_)} ⇒ {m}n = {dz(wert_ - t)} ⇒ n = {n}.',
                    'Setze aₙ gleich dem Wert und löse nach n auf.', n, f'({wert_} - ({t})) / {m}')
    n = R.randint(5, 20)
    return zahl(f'{a("n")} = {poly(m, t, v="n")}. Um wie viel unterscheiden sich {a(n + 1)} und {a(n)} ({a(n + 1)} − {a(n)})?',
                f'{a(n + 1)} = {dz(m * (n + 1) + t)}, {a(n)} = {dz(m * n + t)}. Differenz: {dz(m)} – so groß wie der Faktor vor n.',
                'Rechne beide Glieder aus oder überlege, was sich ändert, wenn n um 1 wächst.', m, f'{m} * {n + 1} + ({t}) - ({m} * {n} + ({t}))')


def g_rekursiv(s):
    art = R.choice({1: ['plus', 'mal'], 2: ['plus', 'mal', 'linear'], 3: ['linear', 'rueck', 'zwei']}[s])
    a1 = R.randint(-5, 12)
    if art == 'plus':
        d = R.choice([2, 3, 4, 5, 7, -2, -3, -4])
        k = R.randint(3, 6)
        xs = [a1 + d * i for i in range(k)]
        return zahl(f'{a(1)} = {dz(a1)}, {a("n+1")} = {a("n")} {plus(d)}. Berechne {a(k)}.', f'{folge_txt(xs)[:-3]} → {a(k)} = {dz(xs[-1])}.',
                    f'Rechne Schritt für Schritt: jedes Mal {plus(d)}.', xs[-1], f'{a1} + {k - 1} * ({d})')
    if art == 'mal':
        q = R.choice([2, 3, -2, Fr(1, 2)])
        a1 = R.choice([1, 2, 3, 4, 5, 8, 16, 32, 64]) if q == Fr(1, 2) else R.randint(1, 6)
        k = R.randint(3, 5)
        xs = [a1 * q ** i for i in range(k)]
        if not all(endlich(x) for x in xs): return None
        return zahl(f'{a(1)} = {dz(a1)}, {a("n+1")} = {dz(q)} · {a("n")}. Berechne {a(k)}.', f'{"; ".join(dz(x) for x in xs)} → {a(k)} = {dz(xs[-1])}.',
                    'Multipliziere jedes Glied mit dem Faktor, um das nächste zu erhalten.', xs[-1], f'{a1} * ({float(q)}) ** {k - 1}')
    if art == 'linear':
        m, c = R.choice([2, 3, -1, -2]), R.randint(-4, 5)
        if c == 0: return None
        a1 = R.randint(-3, 5)
        k = R.randint(3, 4)
        xs, ex = [a1], str(a1)
        for _ in range(k - 1):
            xs.append(m * xs[-1] + c)
            ex = f'({m}) * ({ex}) + ({c})'
        if max(abs(x) for x in xs) > 500: return None
        return zahl(f'{a(1)} = {dz(a1)}, {a("n+1")} = {dz(m) if m not in (1, -1) else ("−" if m == -1 else "")}{"" if m in (1, -1) else " · "}{a("n")} {plus(c)}. Berechne {a(k)}.',
                    ' '.join(f'{a(i + 2)} = {kl(m)} · {kl(xs[i])} {plus(c)} = {dz(xs[i + 1])};' for i in range(k - 1)).rstrip(';') + '.',
                    'Setze immer das gerade berechnete Glied ein.', xs[-1], ex)
    if art == 'rueck':
        d = R.choice([3, 4, 5, 6, -3, -5])
        a3 = R.randint(-10, 30)
        a1_ = a3 - 2 * d
        return zahl(f'Für eine Folge gilt {a("n+1")} = {a("n")} {plus(d)} und {a(3)} = {dz(a3)}. Wie groß ist {a(1)}?', f'Rückwärts: {a(2)} = {dz(a3)} {plus(-d)} = {dz(a3 - d)}, {a(1)} = {dz(a3 - d)} {plus(-d)} = {dz(a1_)}.',
                    'Rückwärts rechnen: Umkehroperation zweimal anwenden.', a1_, f'{a3} - 2 * ({d})')
    b1, b2 = R.randint(1, 4), R.randint(1, 5)
    xs, ex = [b1, b2], [str(b1), str(b2)]
    for _ in range(4):
        xs.append(xs[-1] + xs[-2])
        ex.append(f'({ex[-1]}) + ({ex[-2]})')
    return zahl(f'{a(1)} = {b1}, {a(2)} = {b2} und {a("n+2")} = {a("n+1")} + {a("n")} (jedes Glied ist die Summe der beiden vorigen). Berechne {a(6)}.',
                f'{"; ".join(map(str, xs[:6]))} → {a(6)} = {xs[5]}.', 'Addiere jeweils die zwei letzten Glieder.', xs[5], ex[5])


def g_arithmetisch(s):
    a1, d = R.randint(-10, 20), R.choice([2, 3, 4, 5, 6, 7, -2, -3, -4, -5])
    art = R.choice({1: ['d', 'an_klein'], 2: ['an', 'term', 'aus_zwei'], 3: ['welches', 'sach', 'sach_rueck', 'aus_zwei_weit']}[s])
    xs = [a1 + d * i for i in range(4)]
    if art == 'd':
        return zahl(f'Bestimme die Differenz d der arithmetischen Folge {folge_txt(xs)}', f'd = {dz(xs[1])} − {kl(xs[0])} = {dz(d)}.',
                    'Ziehe ein Glied vom nächsten ab.', d, f'{xs[1]} - ({xs[0]})')
    if art in ('an', 'an_klein'):
        n = R.randint(6, 12) if art == 'an_klein' else R.randint(15, 60)
        return zahl(f'Arithmetische Folge {folge_txt(xs)} Berechne {a(n)}.', f'd = {dz(d)}. {a(n)} = {dz(a1)} + ({n} − 1) · {kl(d)} = {dz(a1)} {plus((n - 1) * d)} = {dz(a1 + (n - 1) * d)}.',
                    'aₙ = a₁ + (n − 1) · d.', a1 + (n - 1) * d, f'{a1} + ({n} - 1) * ({d})')
    if art == 'term':
        return luecken(f'Gib die explizite Formel der arithmetischen Folge {folge_txt(xs)} an.', f'{a("n")} = □n + □', 'Zahlen vor n und am Ende (auch negativ)', [d, a1 - d],
                       f'{a("n")} = {dz(a1)} + (n − 1) · {kl(d)} = {poly(d, a1 - d, v="n")}.', 'Setze a₁ und d in aₙ = a₁ + (n − 1) · d ein und vereinfache.',
                       c=[str(d), f'{a1} - ({d})'])
    if art in ('aus_zwei', 'aus_zwei_weit'):
        i, j = (1, R.randint(3, 6)) if art == 'aus_zwei' else (R.randint(2, 5), R.randint(8, 15))
        ai, aj = a1 + (i - 1) * d, a1 + (j - 1) * d
        frage = R.choice(['d', 'a1']) if art == 'aus_zwei_weit' else 'd'
        if frage == 'd':
            return zahl(f'Arithmetische Folge mit {a(i)} = {dz(ai)} und {a(j)} = {dz(aj)}. Berechne d.', f'Von {a(i)} bis {a(j)} sind es {j - i} Schritte: d = ({dz(aj)} − {kl(ai)}) : {j - i} = {dz(d)}.',
                        'Wie viele Schritte d liegen zwischen den beiden Gliedern?', d, f'({aj} - ({ai})) / {j - i}')
        return zahl(f'Arithmetische Folge mit {a(i)} = {dz(ai)} und {a(j)} = {dz(aj)}. Berechne {a(1)}.',
                    f'd = ({dz(aj)} − {kl(ai)}) : {j - i} = {dz(d)}. {a(1)} = {dz(ai)} − {i - 1} · {kl(d)} = {dz(a1)}.',
                    'Erst d bestimmen, dann zurück bis a₁ rechnen.', a1, f'{ai} - {i - 1} * ({aj} - ({ai})) / {j - i}')
    if art == 'welches':
        if d < 0: d = -d
        n = R.randint(12, 50)
        an = a1 + (n - 1) * d
        return zahl(f'Arithmetische Folge {folge_txt([a1 + d * i for i in range(4)])} Das wievielte Glied ist {dz(an)}?',
                    f'{dz(a1)} + (n − 1) · {d} = {dz(an)} ⇒ (n − 1) · {d} = {dz(an - a1)} ⇒ n − 1 = {n - 1} ⇒ n = {n}.',
                    'Setze aₙ ein und löse nach n auf.', n, f'({an} - ({a1})) / {d} + 1')
    if art == 'sach':
        r1, dd, n = R.randint(12, 24), R.choice([2, 3, 4]), R.randint(10, 30)
        return zahl(f'Ein Theater hat in der ersten Reihe {r1} Plätze, in jeder weiteren Reihe {dd} Plätze mehr. Wie viele Plätze hat Reihe {n}?',
                    f'a₁ = {r1}, d = {dd}. {a(n)} = {r1} + ({n} − 1) · {dd} = {r1 + (n - 1) * dd}.', 'Arithmetische Folge: a₁ und d herauslesen.',
                    r1 + (n - 1) * dd, f'{r1} + ({n} - 1) * {dd}')
    k0, rate, mon = R.choice([50, 80, 100, 120]), R.choice([15, 20, 25, 30]), R.randint(5, 20)
    ziel = k0 + rate * mon
    return zahl(f'Auf einem Sparkonto sind {k0} €. Jeden Monat kommen {rate} € dazu. Nach wie vielen Monaten sind {dz(ziel)} € auf dem Konto?',
                f'{k0} + {rate} · m = {dz(ziel)} ⇒ {rate} · m = {dz(ziel - k0)} ⇒ m = {mon}.', 'Wie oft muss die Rate dazukommen?', mon, f'({ziel} - {k0}) / {rate}')


def g_geometrisch(s):
    a1, q = R.choice([1, 2, 3, 4, 5]), R.choice([2, 3, -2, Fr(1, 2)])
    if q == Fr(1, 2): a1 = R.choice([64, 128, 256, 512, 96, 160])
    art = R.choice({1: ['q', 'an_klein'], 2: ['an', 'q', 'aus_zwei', 'an_neg'], 3: ['sach_bakt', 'sach_ball', 'welches', 'sach_wert']}[s])
    xs = [a1 * q ** i for i in range(4)]
    if not all(endlich(x) for x in xs): return None
    if art == 'q':
        return zahl(f'Bestimme den Faktor q der geometrischen Folge {folge_txt(xs)}', f'Quotient zweier Nachbarglieder: q = {dz(xs[1])} : {kl(xs[0])} = {dz(q)}.',
                    'Teile ein Glied durch das vorige.', q, f'{float(xs[1])} / {float(xs[0])}')
    if art in ('an', 'an_klein', 'an_neg'):
        if art == 'an_neg': q = R.choice([-2, -3]); xs = [a1 * q ** i for i in range(4)]
        n = R.randint(5, 7) if art == 'an_klein' else R.randint(6, 10)
        an = a1 * Fr(q) ** (n - 1)
        if not endlich(an) or abs(an) > 10 ** 6: return None
        return zahl(f'Geometrische Folge {folge_txt(xs)} Berechne {a(n)}.', f'q = {dz(q)}. {a(n)} = {dz(a1)} · {kl(q) if q == int(q) else "(" + dz(q) + ")"}^{n - 1} = {dz(an)}.',
                    'aₙ = a₁ · qⁿ⁻¹ – der Exponent ist eins kleiner als n.', an, f'{a1} * ({float(q)}) ** ({n} - 1)')
    if art == 'aus_zwei':
        q = R.choice([2, 3, 5])
        k = 2
        return zahl(f'Geometrische Folge mit positiven Gliedern, {a(1)} = {a1} und {a(3)} = {dz(a1 * q * q)}. Berechne q.', f'{a(3)} = {a(1)} · q² ⇒ q² = {dz(a1 * q * q)} : {a1} = {q * q} ⇒ q = {q}.',
                    'Von a₁ bis a₃ wird zweimal mit q multipliziert.', q, f'{q}')
    if art == 'welches':
        q = R.choice([2, 3])
        n = R.randint(5, 9)
        an = a1 * q ** (n - 1)
        return zahl(f'Geometrische Folge {folge_txt([a1 * q ** i for i in range(4)])} Das wievielte Glied ist {dz(an)}?',
                    f'{dz(an)} : {a1} = {dz(an // a1)} = {q}^{n - 1}. Also n − 1 = {n - 1}, n = {n}.', 'Teile durch a₁ und überlege, welche Potenz von q herauskommt.', n, f'{n}')
    if art == 'sach_bakt':
        b0, std = R.choice([50, 100, 200, 500]), R.randint(4, 8)
        return zahl(f'Eine Bakterienkultur hat {b0} Bakterien und verdoppelt sich jede Stunde. Wie viele Bakterien sind es nach {std} Stunden?',
                    f'Nach jeder Stunde · 2: {b0} · 2^{std} = {dz(b0 * 2 ** std)}.', 'Achtung: Nach 1 Stunde ist einmal verdoppelt.', b0 * 2 ** std, f'{b0} * 2 ** {std}')
    if art == 'sach_ball':
        h0 = R.choice([160, 200, 240, 320, 400])
        f = R.choice([Fr(1, 2), Fr(3, 4)])
        k = R.randint(2, 4)
        hk = h0 * f ** k
        if not endlich(hk): return None
        return zahl(f'Ein Ball fällt aus {h0} cm Höhe und springt jedes Mal auf {dz(f * 100)} % der vorigen Höhe zurück. Wie hoch springt er nach dem {k}. Aufprall (in cm)?',
                    f'q = {dz(f)}. Nach {k} Aufprallen: {h0} · {dz(f)}^{k} = {dz(hk)} cm.', 'Jeder Aufprall: mal q.', hk, f'{h0} * {float(f)} ** {k}', einheit='cm')
    w0 = R.choice([20000, 24000, 30000])
    p = R.choice([10, 20, 25])
    j = R.randint(2, 3)
    wj = w0 * Fr(100 - p, 100) ** j
    if not endlich(wj): return None
    return zahl(f'Ein Auto kostet neu {dz(w0)} €. Sein Wert sinkt jedes Jahr um {p} %. Wie viel ist es nach {j} Jahren noch wert?',
                f'q = 1 − {dz(Fr(p, 100))} = {dz(Fr(100 - p, 100))}. {dz(w0)} · {dz(Fr(100 - p, 100))}^{j} = {dz(wj)} €.',
                'Abnahme um p % heißt: mal (1 − p/100).', wj, f'{w0} * {float(Fr(100 - p, 100))} ** {j}', einheit='€')


def g_erkennen(s):
    art = R.choice({1: ['art', 'naechstes'], 2: ['art3', 'naechstes3', 'fehler_n', 'fehler_q'], 3: ['fehler_n', 'fehler_q', 'art3', 'naechstes3']}[s])  # Durchsicht 19
    def zufall_folge(typ):
        if typ == 'arith':
            a1, d = R.randint(-10, 20), R.choice([2, 3, 4, 5, 6, 9, -3, -4, -7])
            return [a1 + d * i for i in range(5)], f'arithmetisch (d = {dz(d)})', 'arithmetisch'
        if typ == 'geo':
            a1, q = R.randint(1, 5), R.choice([2, 3, -2, 4])
            return [a1 * q ** i for i in range(5)], f'geometrisch (q = {dz(q)})', 'geometrisch'
        k = R.choice(['quad', 'wachs'])
        if k == 'quad':
            c = R.randint(-3, 3)
            return [i * i + c for i in range(1, 6)], 'weder arithmetisch noch geometrisch', 'weder noch'
        st = R.randint(1, 5)
        xs = [st]
        for i in range(1, 5): xs.append(xs[-1] + i)
        return xs, 'weder arithmetisch noch geometrisch', 'weder noch'
    if art in ('art', 'art3'):
        typ = R.choice(['arith', 'geo', 'weder'])
        xs, r, kurz = zufall_folge(typ)
        zeig = xs[:4]
        return auswahl(f'Welche Art von Folge ist {folge_txt(zeig)}?', kurz, ['arithmetisch', 'geometrisch', 'weder noch'],
                       f'Differenzen: {"; ".join(dz(zeig[i + 1] - zeig[i]) for i in range(3))}. ' +
                       (f'Quotienten: {"; ".join(dz(Fr(zeig[i + 1], zeig[i])) if endlich(Fr(zeig[i + 1], zeig[i])) else br(Fr(zeig[i + 1], zeig[i])) for i in range(3))}. ' if 0 not in zeig[:3] else '') + f'Die Folge ist {r}.',
                       'Prüfe die Differenzen und die Quotienten aufeinanderfolgender Glieder.')
    if art in ('naechstes', 'naechstes3'):
        typ = R.choice(['arith', 'geo'] + (['weder'] if art == 'naechstes3' else []))
        xs, r, _ = zufall_folge(typ)
        return zahl(f'Setze die Folge fort: {folge_txt(xs[:4])} Wie heißt das nächste Glied?', f'Die Folge ist {r}. Nächstes Glied: {dz(xs[4])}.',
                    'Finde zuerst die Regel (plus d, mal q oder ein anderes Muster).', xs[4], f'{xs[4]}')
    if art == 'fehler_n':
        a1, d, n = R.randint(1, 15), R.randint(2, 9), R.randint(10, 40)
        r = f'Falsch: richtig ist {a(n)} = {a1} + {n - 1} · {d} = {a1 + (n - 1) * d}.'
        return auswahl(f'Arithmetische Folge mit {a(1)} = {a1}, d = {d}. Nina rechnet {a(n)} = {a1} + {n} · {d} = {a1 + n * d}. Stimmt das?', r,
                       ['Richtig.', f'Falsch: richtig ist {a(n)} = {n} · {d} = {n * d}.', f'Falsch: richtig ist {a(n)} = {a1} · {d}^{n - 1}.'],
                       f'Von {a(1)} bis {a(n)} sind es nur {n - 1} Schritte. Nina hat einmal zu viel addiert.', 'Wie viele Schritte liegen zwischen a₁ und aₙ?')
    a1, q, n = R.randint(2, 5), R.choice([2, 3]), R.randint(5, 8)  # Durchsicht 19: a₁ = 1 ergab widersprüchliche Antworten
    if a1 == q: return None  # sonst wäre auch „qⁿ“ richtig (mehrdeutig)
    r = f'Falsch: richtig ist {a(n)} = {a1} · {q}^{n - 1} = {dz(a1 * q ** (n - 1))}.'
    return auswahl(f'Geometrische Folge mit {a(1)} = {a1}, q = {q}. Lars rechnet {a(n)} = ({a1} · {q})^{n - 1} = {dz((a1 * q) ** (n - 1))}. Stimmt das?' if a1 > 1 else
                   f'Geometrische Folge mit {a(1)} = {a1}, q = {q}. Lars rechnet {a(n)} = {a1} · {q}^{n} = {a1 * q ** n}. Stimmt das?', r,
                   ['Richtig.', f'Falsch: richtig ist {a(n)} = {a1} + ({n} − 1) · {q} = {a1 + (n - 1) * q}.', f'Falsch: richtig ist {a(n)} = {q}^{n} = {dz(q ** n)}.'],
                   f'Nur q wird potenziert, und zwar mit n − 1 = {n - 1}: {a1} · {dz(q ** (n - 1))} = {dz(a1 * q ** (n - 1))}.',
                   'Welche Zahl wird potenziert – und mit welchem Exponenten?')


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-2) ----------
# Prüfungsvorbilder: IB MYP Extended / MYP-Fragenbanken (n-tes Glied, „Is 100 a term of the sequence?“, erstes Glied über einer Grenze,
# a₁ und d aus zwei Gliedern, Wachstum/Abnahme in Prozent, allgemeines Glied auswählen, zweite Differenzen). Eigene Zahlen.
def explizit3(art):
    if art == 'erstes_ueber':
        k, c = R.choice([1, 2, 3]), R.randint(-5, 5)
        g = R.choice([100, 150, 200, 300, 500])
        n = next(n for n in range(1, 100) if k * n * n + c > g)
        return zahl(f'{a("n")} = {poly(k, 0, c, v="n")}. Ab welchem Platz n ist das Glied größer als {g}?',
                    f'{a(n - 1)} = {k * (n - 1) ** 2 + c} ≤ {g}, aber {a(n)} = {k * n * n + c} > {g}. Also ab n = {n}.',
                    'Probiere Platznummern aus, bis das Glied die Grenze überschreitet.', n, f'{n}')
    # ist_glied
    m, c = R.choice([3, 4, 6, 7]), R.randint(-5, 9)
    z = R.randint(40, 150)
    ja = (z - c) % m == 0 and (z - c) // m >= 1
    n = (z - c) // m
    r = f'Ja, es ist {a(n)}.' if ja else 'Nein.'
    falsch = [f'Ja, es ist {a(round((z - c) / m))}.', 'Das kann man nicht entscheiden.', 'Nein.' if ja else f'Ja, es ist {a(n + 1)}.']
    return auswahl(f'Ist {z} ein Glied der Folge {a("n")} = {poly(m, c, v="n")}?', r, falsch,
                   f'{poly(m, c, v="n")} = {z} ⇒ {m}n = {z - c} ⇒ n = {dz(Fr(z - c, m)) if endlich(Fr(z - c, m)) else br(Fr(z - c, m))}. '
                   + (f'n ist eine natürliche Zahl: {z} = {a(n)}.' if ja else 'n ist keine natürliche Zahl, also kommt die Zahl nicht vor.'),
                   'Setze die Formel gleich der Zahl. Ist n eine natürliche Zahl?')


def rekursiv3(art):
    if art == 'kontext':
        f0, p, ab = R.choice([(100, 20, 10), (200, 10, 15), (120, 25, 20), (80, 50, 30), (400, 10, 30)])
        x1 = f0 * (100 + p) // 100 - ab
        x2 = x1 * (100 + p) / 100 - ab
        if x2 != int(x2): return None
        return zahl(f'In einem Teich leben {f0} Fische. Jedes Jahr wächst der Bestand um {p} %, danach werden {ab} Fische gefangen. Wie viele Fische leben nach 2 Jahren im Teich?',
                    f'Regel: {a("n+1")} = {dz(Fr(100 + p, 100))} · {a("n")} − {ab}. Nach 1 Jahr: {dz(Fr(100 + p, 100))} · {f0} − {ab} = {x1}. Nach 2 Jahren: {dz(Fr(100 + p, 100))} · {x1} − {ab} = {int(x2)}.',
                    'Erst wachsen lassen, dann abziehen – und das zweimal.', int(x2), f'(({f0} * {1 + p / 100} - {ab}) * {1 + p / 100}) - {ab}')
    # periodisch
    s_, a1 = R.randint(5, 12), R.randint(1, 4)
    a2 = s_ - a1
    if a1 == a2: return None
    k = R.choice([50, 99, 100, 101, 200])
    w = a1 if k % 2 else a2
    return zahl(f'{a(1)} = {a1}, {a("n+1")} = {s_} − {a("n")}. Berechne {a(k)}.',
                f'{a(2)} = {s_} − {a1} = {a2}, {a(3)} = {s_} − {a2} = {a1}, … Die Folge springt zwischen {a1} und {a2}: ungerade Platznummern {a1}, gerade {a2}. {k} ist {"ungerade" if k % 2 else "gerade"}: {a(k)} = {w}.',
                'Rechne die ersten Glieder aus und suche ein Muster.', w, f'{w}')


def arith3(art):
    if art == 'zwei_glieder':
        a1, d = R.randint(-8, 15), R.choice([2, 3, 4, 5, -3, -4])
        i, j = sorted(R.sample(range(2, 10), 2))
        ai, aj = a1 + (i - 1) * d, a1 + (j - 1) * d
        return luecken(f'Bei einer arithmetischen Folge ist {a(i)} = {dz(ai)} und {a(j)} = {dz(aj)}. Bestimme {a(1)} und d.', f'{a(1)} = □; d = □', 'zwei ganze Zahlen',
                       [a1, d], f'Von {a(i)} bis {a(j)}: {j - i} Schritte, d = ({dz(aj)} − {kl(ai)}) : {j - i} = {dz(d)}. {a(1)} = {dz(ai)} − {i - 1} · {kl(d)} = {dz(a1)}.',
                       'Wie viele Schritte d liegen zwischen den beiden bekannten Gliedern?', c=[f'{ai} - {i - 1} * ({aj} - ({ai})) / {j - i}', f'({aj} - ({ai})) / {j - i}'])
    # erstes_negativ
    a1, d = R.randint(40, 120), -R.choice([3, 4, 6, 7, 8, 9])
    n = next(n for n in range(1, 200) if a1 + (n - 1) * d < 0)
    if a1 + (n - 1) * d == 0: return None
    xs = [a1 + d * i for i in range(3)]
    return zahl(f'Arithmetische Folge {folge_txt(xs)} Wie heißt das erste negative Glied?',
                f'd = {dz(d)}. {a(n - 1)} = {dz(a1 + (n - 2) * d)} ≥ 0, {a(n)} = {dz(a1)} + {n - 1} · {kl(d)} = {dz(a1 + (n - 1) * d)} < 0. Das erste negative Glied ist {dz(a1 + (n - 1) * d)}.',
                f'Wie oft passt {abs(d)} in {a1}? Danach kommt der erste Schritt unter 0.', a1 + (n - 1) * d, f'{a1} + ({n} - 1) * ({d})')


def geo3(art):
    if art == 'zwei_glieder_geo':
        a1, q = R.randint(1, 6), R.choice([2, 3, 4])
        return zahl(f'Eine geometrische Folge mit positiven Gliedern hat {a(2)} = {a1 * q} und {a(4)} = {a1 * q ** 3}. Berechne {a(1)}.',
                    f'{a(4)} = {a(2)} · q² ⇒ q² = {a1 * q ** 3} : {a1 * q} = {q * q} ⇒ q = {q}. {a(1)} = {a1 * q} : {q} = {a1}.',
                    'Von a₂ bis a₄ wird zweimal mit q multipliziert. Danach einen Schritt zurück.', a1, f'{a1 * q} / {q}')
    # ab_wann
    a1, q = R.randint(2, 7), R.choice([2, 3])
    g = R.choice([1000, 5000, 10000])
    n = next(n for n in range(1, 40) if a1 * q ** (n - 1) > g)
    return zahl(f'Geometrische Folge {folge_txt([a1 * q ** i for i in range(3)])} Welches ist das erste Glied, das größer als {dz(g)} ist? Gib seine Platznummer an.',
                f'{a(n - 1)} = {dz(a1 * q ** (n - 2))} ≤ {dz(g)}, {a(n)} = {dz(a1 * q ** (n - 1))} > {dz(g)}. Also Platz {n}.',
                'Rechne weiter (mal q), bis die Grenze überschritten ist, und zähle die Plätze mit.', n, f'{n}')


def erkennen3(art):
    if art == 'formel_typ':
        a1, q = R.randint(2, 7), R.choice([2, 3, 4])
        if a1 == q: return None
        xs = [a1 * q ** i for i in range(3)]
        r = f'{a("n")} = {a1} · {q}^(n − 1)'
        return auswahl(f'Welche Formel gehört zur Folge {folge_txt(xs)}', r,
                       [f'{a("n")} = {a1} · {q}^n', f'{a("n")} = {q} · {a1}^(n − 1)', f'{a("n")} = {a1} + {xs[1] - a1}(n − 1)'],
                       f'Jedes Glied ist das {q}-Fache des vorigen: geometrisch mit {a(1)} = {a1}, q = {q}. Probe: n = 1 gibt {a1} · {q}⁰ = {a1}.',
                       'Bestimme die Art der Folge und setze n = 1 in jede Formel ein.')
    if art == 'zweite_diff':
        p, q_, r_ = R.choice([1, 2]), R.randint(-3, 4), R.randint(-2, 6)
        xs = [p * n * n + q_ * n + r_ for n in range(1, 6)]
        d1 = [xs[i + 1] - xs[i] for i in range(4)]
        return zahl(f'Setze die Folge fort: {folge_txt(xs[:4])} Wie heißt das nächste Glied?',
                    f'Differenzen: {"; ".join(dz(x) for x in d1[:3])} – sie wachsen jedes Mal um {2 * p}. Nächste Differenz: {dz(d1[3])}. Nächstes Glied: {dz(xs[3])} + {kl(d1[3])} = {dz(xs[4])}.',
                    'Weder arithmetisch noch geometrisch? Schau dir die Differenzen der Differenzen an.', xs[4], f'{xs[4]}')
    if art == 'beides':
        return auswahl('Gibt es eine Folge, die zugleich arithmetisch und geometrisch ist?', 'Ja, jede konstante Folge wie 5; 5; 5; … (d = 0, q = 1).',
                       ['Nein, das schließt sich aus.', 'Ja, zum Beispiel 1; 2; 4; 8; …', 'Ja, zum Beispiel 2; 4; 6; 8; …'],
                       'Bei 5; 5; 5; … ist jede Differenz 0 (arithmetisch) und jeder Quotient 1 (geometrisch). 1; 2; 4; 8 ist nur geometrisch, 2; 4; 6; 8 nur arithmetisch.',
                       'Welche Differenz und welcher Quotient sind möglich, wenn alle Glieder gleich sind?')
    # fehlendes_glied
    if R.random() < .5:
        a1, q = R.randint(1, 6), R.choice([2, 3, 4])
        xs = [a1 * q ** i for i in range(4)]
        return zahl(f'Die Folge {dz(xs[0])}; □; {dz(xs[2])}; {dz(xs[3])}; … ist geometrisch. Welche Zahl gehört in die Lücke?',
                    f'q = {dz(xs[3])} : {dz(xs[2])} = {q}. Lücke: {dz(xs[0])} · {q} = {dz(xs[1])} (Probe: {dz(xs[1])} · {q} = {dz(xs[2])}).',
                    'Bestimme q aus den beiden Nachbarn ohne Lücke.', xs[1], f'{xs[1]}')
    a1, d = R.randint(-5, 15), R.choice([3, 4, 5, 6, 7])
    xs = [a1 + d * i for i in range(4)]
    return luecken(f'Die Folge {dz(xs[0])}; □; □; {dz(xs[3])}; … ist arithmetisch. Welche Zahlen gehören in die Lücken?', '□ und □', 'zwei ganze Zahlen', xs[1:3],
                   f'Von {dz(xs[0])} bis {dz(xs[3])} sind es 3 Schritte: d = ({dz(xs[3])} − {kl(xs[0])}) : 3 = {d}. Lücken: {dz(xs[1])} und {dz(xs[2])}.',
                   'Zwischen dem ersten und dem vierten Glied liegen drei gleich große Schritte.', c=[str(xs[1]), str(xs[2])])


def _filter(g, s, teil, *, nicht=False):
    for _ in range(80):
        t = g(s)
        if t and ((teil in t['f']['text']) != nicht): return t
    return None


def g2_explizit(s):
    if s < 3: return g_explizit(s)
    art = art3('welches_n', 'erstes_ueber', 'ist_glied', ['welches_n', 'differenz', 'erstes_ueber', 'ist_glied'])
    if art == 'welches_n': return _filter(g_explizit, 3, 'Das wievielte')
    if art == 'differenz': return _filter(g_explizit, 3, 'unterscheiden')
    return explizit3(art)


def g2_rekursiv(s):
    if s < 3: return g_rekursiv(s)
    art = art3('zwei', 'kontext', 'periodisch', ['rueck', 'zwei', 'kontext', 'periodisch', 'rueck'])
    if art == 'zwei': return _filter(g_rekursiv, 3, 'Summe der beiden vorigen')
    if art == 'rueck': return _filter(g_rekursiv, 3, 'Wie groß ist')
    return rekursiv3(art)


def g2_arithmetisch(s):
    if s < 3: return g_arithmetisch(s)
    art = art3('zwei_glieder', 'sach', 'erstes_negativ', ['zwei_glieder', 'sach', 'erstes_negativ', 'welches', 'sparen'])
    if art == 'sach': return _filter(g_arithmetisch, 3, 'Theater')
    if art == 'sparen': return _filter(g_arithmetisch, 3, 'Sparkonto')
    if art == 'welches': return _filter(g_arithmetisch, 3, 'Das wievielte')
    return arith3(art)


def g2_geometrisch(s):
    if s < 3: return g_geometrisch(s)
    art = art3('wert', 'zwei_glieder_geo', 'ab_wann', ['wert', 'zwei_glieder_geo', 'ab_wann', 'bakt', 'ball'])
    if art == 'wert': return _filter(g_geometrisch, 3, 'Auto')
    if art == 'bakt': return _filter(g_geometrisch, 3, 'Bakterien')
    if art == 'ball': return _filter(g_geometrisch, 3, 'Ball')
    return geo3(art)


def g2_erkennen(s):
    if s < 3: return g_erkennen(s)
    art = art3('formel_typ', 'zweite_diff', 'beides', ['formel_typ', 'zweite_diff', 'fehler', 'fehlendes_glied', 'fehlendes_glied'])
    if art == 'fehler': return _filter(g_erkennen, 3, 'rechnet')
    return erkennen3(art)


GEN = schoen({'explizit': g2_explizit, 'rekursiv': g2_rekursiv, 'arithmetisch': g2_arithmetisch, 'geometrisch': g2_geometrisch, 'erkennen': g2_erkennen})

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import tab  # noqa: E402


def _s(werte, einheit='', namen=None):
    namen = namen or [f'a{"₁₂₃₄₅₆₇₈₉"[i]}' for i in range(len(werte))]
    return {'typ': 'saeulen', 'einheit': einheit, 'werte': [{'name': n, 'wert': w} for n, w in zip(namen, werte)], 'zahlen': True}


_K = ['Glied', '2', '6', '18', '54']
UMBAU = {
    'explizit': {
        'einstieg': 'Ein Muster aus Plättchen wächst. Bild 1 hat 1 Plättchen, Bild 2 hat 4, Bild 3 hat 7. '
                    'Die Anzahlen bilden eine ⟦Folge⟧.',
        'woerter': [['Folge', 'eine geordnete Liste von Zahlen a₁, a₂, a₃, …'],
                    ['aₙ', 'das Glied an Platz n; n ist die Platznummer']],
        'bild': _s([1, 4, 7], 'Plättchen'),
        'schritte': [
            {'text': 'Die Formel für die Anzahl lautet aₙ = 3n − 2.'},
            {'text': 'Für a₅ setzt du die Platznummer n = 5 ein.'},
            {'text': '3 · 5 − 2 = ⟦13⟧. Bild 5 hat 13 Plättchen.', 'bild': _s([1, 4, 7, 10, 13], 'Plättchen')},
        ],
        'fehler': 'n ist die ⟦Platznummer⟧, aₙ der Wert. a₅ heißt Platz 5, nicht Wert 5.',
        'regel': 'Explizite Formel: für n die ⟦Platznummer⟧ einsetzen. Das Ergebnis ist das Glied aₙ.',
    },
    'rekursiv': {
        'einstieg': 'Eine Regel sagt: Nimm die vorige Zahl, verdopple sie und zieh 1 ab. Start ist 5. '
                    'So eine Vorschrift heißt ⟦rekursiv⟧.',
        'woerter': [['rekursiv', 'jedes Glied wird aus dem vorigen berechnet'],
                    ['Startwert', 'das erste Glied a₁'],
                    ['aₙ₊₁', 'das Glied direkt nach aₙ']],
        'bild': _s([5]),
        'schritte': [
            {'text': 'Startwert a₁ = 5, Regel aₙ₊₁ = 2 · aₙ − 1.'},
            {'text': 'a₂ = 2 · 5 − 1 = 9.', 'bild': _s([5, 9])},
            {'text': 'a₃ = 2 · 9 − 1 = 17.', 'bild': _s([5, 9, 17])},
            {'text': 'a₄ = 2 · 17 − 1 = ⟦33⟧.', 'bild': _s([5, 9, 17, 33])},
        ],
        'fehler': 'a₄ = 2 · 4 − 1 = 7 ist falsch. Rekursiv setzt man ⟦das vorige Glied⟧ ein, nicht die Platznummer.',
        'regel': 'Rekursiv: aus dem ⟦vorigen Glied⟧ das nächste berechnen. Dazu braucht man einen Startwert.',
    },
    'arithmetisch': {
        'einstieg': 'Du hast 7 € im Sparschwein und legst jede Woche 4 € dazu. Es kommt immer gleich viel dazu. '
                    'So eine Folge heißt ⟦arithmetisch⟧.',
        'woerter': [['arithmetische Folge', 'immer dieselbe Zahl d kommt dazu'],
                    ['d', 'die Differenz zweier Nachbarglieder']],
        'bild': _s([7, 11, 15, 19], '€'),
        'schritte': [
            {'text': 'Arithmetische Folge 7; 11; 15; 19: d = 11 − 7 = 4.'},
            {'text': 'Bis a₂₀ sind es 19 Schritte zu je 4.'},
            {'text': 'a₂₀ = 7 + 19 · 4 = ⟦83⟧.', 'bild': _s([7, 11, 15, 19, 83], '€', ['a₁', 'a₂', 'a₃', 'a₄', 'a₂₀'])},
        ],
        'fehler': '7 + 20 · 4 = 87 ist falsch. Von a₁ bis a₂₀ sind es nur ⟦19 Schritte⟧.',
        'regel': 'Arithmetisch: immer ⟦+ d⟧. Es gilt aₙ = a₁ + (n − 1) · d.',
    },
    'geometrisch': {
        'einstieg': 'Am ersten Tag kennen 3 Leute ein Gerücht, jeden Tag verdoppelt sich die Zahl. '
                    'Hier wird immer mit demselben Faktor malgenommen. Die Folge ist ⟦geometrisch⟧.',
        'woerter': [['geometrische Folge', 'immer mit demselben Faktor q malnehmen'],
                    ['q', 'der Faktor: q = a₂ : a₁']],
        'bild': _s([3, 6, 12, 24], 'Leute'),
        'schritte': [
            {'text': 'Geometrische Folge 3; 6; 12; 24: q = 6 : 3 = 2.'},
            {'text': 'Bis a₇ wird 6-mal mit 2 malgenommen.'},
            {'text': 'a₇ = 3 · 2⁶ = 3 · 64 = ⟦192⟧.', 'bild': _s([3, 6, 12, 24, 48, 96, 192], 'Leute')},
        ],
        'fehler': '3 · 2⁷ = 384 ist falsch. Von a₁ bis a₇ wird nur ⟦6-mal⟧ malgenommen: q⁶.',
        'regel': 'Geometrisch: immer ⟦mal q⟧. Es gilt aₙ = a₁ · qⁿ⁻¹.',
    },
    'erkennen': {
        'einstieg': 'Ein Detektiv bekommt die Zahlen 2; 6; 18; 54. Wie geht es weiter? Er prüft zwei Spuren: '
                    'gleicher Abstand oder gleicher Faktor? So ⟦erkennt⟧ er die Folge.',
        'woerter': [['Differenz', 'Ergebnis von „Nachbar minus Glied“'],
                    ['Quotient', 'Ergebnis von „Nachbar geteilt durch Glied“']],
        'bild': tab(_K),
        'schritte': [
            {'text': 'Die Differenzen sind 4; 12; 36. Nicht gleich, also nicht arithmetisch.',
             'bild': tab(_K, ['Differenz', '', '4', '12', '36'])},
            {'text': 'Die Quotienten sind 3; 3; 3. Gleich!', 'bild': tab(_K, ['Differenz', '', '4', '12', '36'], ['Quotient', '', '3', '3', '3'])},
            {'text': '⟦Geometrisch mit q = 3⟧, das nächste Glied ist 162.'},
        ],
        'fehler': 'Aus zwei Gliedern kann man nichts schließen. Bei 1; 4 passt d = 3 oder q = 4. Man braucht ⟦mindestens drei Glieder⟧.',
        'regel': 'Differenzen gleich: arithmetisch. ⟦Quotienten gleich⟧: geometrisch. Sonst weder noch.',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


d = bauen('funktionen.folgen',
      'Folgenglieder explizit und rekursiv berechnen, arithmetische und geometrische Folgen erkennen, beschreiben und in Sachaufgaben anwenden.',
      ['Folge (sequence): a₁, a₂, a₃, …; n ist die Platznummer.',
       'Rekursiv (recursive): nächstes Glied aus dem vorigen; braucht einen Startwert.',
       'Arithmetisch: aₙ = a₁ + (n − 1) · d (immer plus d).',
       'Geometrisch: aₙ = a₁ · qⁿ⁻¹ (immer mal q).',
       'Art prüfen: Differenzen gleich → arithmetisch, Quotienten gleich → geometrisch.'],
      [('Folgen beschreiben', ['explizit', 'rekursiv']), ('Besondere Folgen', ['arithmetisch', 'geometrisch']), ('Erkennen', ['erkennen'])],
      ETAPPEN, GEN,
      offen=['Reihen und Summenschreibweise (im Umfang von funktionen.folgen genannt) stehen im eigenen Thema funktionen.reihen, damit sich die beiden Themen nicht doppeln.',
             'Indizes werden mit tiefgestellten Unicode-Ziffern geschrieben (a₅, aₙ₊₁). Falls die Schrift der App sie nicht darstellt, bitte melden.'], plan=PLAN2)
umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
