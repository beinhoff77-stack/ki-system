#!/usr/bin/env python3
"""Thema funktionen.ganzrational – Ganzrationale Funktionen (Klasse 10). Schreibt inhalte/themen/funktionen.ganzrational.json."""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import *  # noqa: E402,F403

start(1005)
IDX = '₁₂₃₄₅'
VERL = {(0, 1): 'von links oben nach rechts oben', (0, -1): 'von links unten nach rechts unten',
        (1, 1): 'von links unten nach rechts oben', (1, -1): 'von links oben nach rechts unten'}


def nz(n):
    return R.choice([i for i in range(-n, n + 1) if i != 0])


def mal(*fs):
    out = [1]
    for f in fs:
        n = [0] * (len(out) + len(f) - 1)
        for i, a in enumerate(out):
            for j, b in enumerate(f):
                n[i + j] += a * b
        out = n
    return out


def fwert(k, x):
    n = len(k) - 1
    return sum(c * Fr(x) ** (n - i) for i, c in enumerate(k))


def wert_c(k, x):
    n = len(k) - 1
    return ' + '.join(f'({c}) * ({x}) ** {n - i}' for i, c in enumerate(k))


def faktor(p, hoch=1):
    t = minus_klammer(p)
    return t + (str(hoch).translate(HOCHZ) if hoch > 1 else '')


def produkt(a, nst):
    """a · (x − p)^m … als Text aus {p: m}"""
    af = '' if a == 1 else '−' if a == -1 else dz(a) + ' · '
    return af + ' · '.join(faktor(p, m) for p, m in sorted(nst.items()))


def graph_bild(kf, nst=(), punkte=None, x=None):
    xs = sorted(set(nst)) or [0]
    lo, hi = (xs[0] - 1.5, xs[-1] + 1.5) if x is None else x
    lo, hi = math.floor(lo), math.ceil(hi)
    ws = sorted(abs(float(fwert(kf, lo + (hi - lo) * j / 60))) for j in range(61))
    m = ws[int(len(ws) * 0.75)] or 1
    pk = [{'x': v, 'y': 0} for v in xs if nst] + (punkte or [])
    return koord([g_poly(kf)], x=(lo, hi), ymax=max(4, m * 1.3), punkte=pk or None)


ETAPPEN = [
    {'lernziel': 'grad', 'titel': 'Grad, Leitkoeffizient, Absolutglied',
     'regel': 'Eine ⟦ganzrationale Funktion⟧ ist eine Summe von Vielfachen von x-Potenzen. Die höchste Hochzahl ist der ⟦Grad⟧, ihr Faktor der ⟦Leitkoeffizient⟧, die Zahl ohne x das ⟦Absolutglied⟧ (= f(0)).',
     'schritte': ['f(x) = −2x³ + 5x − 7: höchste Potenz x³.', 'Grad ⟦3⟧, Leitkoeffizient ⟦−2⟧, Absolutglied ⟦−7⟧.'],
     'probe': 'f(0) = −7 ✓',
     'fehler': 'Bei f(x) = 4 + x² − 3x³ den Leitkoeffizienten 4 zu nennen ist falsch: Er gehört zur ⟦höchsten⟧ Potenz, also −3.'},
    {'lernziel': 'ausmultiplizieren', 'titel': 'Produktform ausmultiplizieren',
     'regel': 'Aus der ⟦Produktform⟧ entsteht durch ⟦Ausmultiplizieren⟧ die Summenform. Schrittweise: erst zwei Klammern, dann mit der dritten.',
     'schritte': ['(x − 1)(x + 2) = x² + x − 2.', '(x² + x − 2)(x − 3) = ⟦x³ − 2x² − 5x + 6⟧.'],
     'probe': 'x = 1 eingesetzt: 1 − 2 − 5 + 6 = 0 ✓ (1 ist Nullstelle)',
     'fehler': '(x − 1)(x + 2) = x² − 2 ist falsch: Die ⟦gemischten Glieder⟧ 2x und −x fehlen. Jedes Glied mit jedem multiplizieren.'},
    {'lernziel': 'randverhalten', 'titel': 'Verhalten für große |x|',
     'regel': 'Für sehr große und sehr kleine x bestimmt nur das ⟦Glied mit der höchsten Potenz⟧ den Verlauf. Gerader Grad: beide Enden gleich; ungerader Grad: Enden entgegengesetzt. Negativer Leitkoeffizient spiegelt.',
     'schritte': ['f(x) = −x⁴ + 10x³ − 2: höchstes Glied −x⁴.', 'Grad gerade, Leitkoeffizient negativ: ⟦von links unten nach rechts unten⟧.'],
     'probe': 'f(100) = −100 000 000 + 10 000 000 − 2 < 0 ✓',
     'fehler': '„Wegen +10x³ geht der Graph rechts nach oben“ ist falsch: Für große x ⟦überwiegt die höchste Potenz⟧ −x⁴.'},
    {'lernziel': 'symmetrie', 'titel': 'Symmetrie erkennen',
     'regel': 'Nur ⟦gerade⟧ Hochzahlen (Absolutglied zählt als x⁰): ⟦achsensymmetrisch⟧ zur y-Achse. Nur ⟦ungerade⟧ Hochzahlen: ⟦punktsymmetrisch⟧ zum Ursprung. Gemischt: keine dieser Symmetrien.',
     'schritte': ['f(x) = 2x⁴ − x² + 3: Hochzahlen 4, 2, 0.', 'Alle gerade: ⟦achsensymmetrisch zur y-Achse⟧.'],
     'probe': 'f(−1) = 2 − 1 + 3 = 4 = f(1) ✓',
     'fehler': 'f(x) = x³ + 1 als punktsymmetrisch zu bezeichnen ist falsch: Das Absolutglied 1 ist eine ⟦gerade⟧ Potenz (x⁰). f(−1) = 0, aber −f(1) = −2.'},
    {'lernziel': 'nullstellen', 'titel': 'Nullstellen und Vielfachheit',
     'regel': 'Nullstellen: ⟦f(x) = 0⟧ lösen (Produktform, Ausklammern, Substitution). An einer Nullstelle ⟦ungerader⟧ Vielfachheit ⟦schneidet⟧ der Graph die x-Achse, bei ⟦gerader⟧ ⟦berührt⟧ er sie.',
     'schritte': ['f(x) = x³ − 4x² + 4x = x(x − 2)².', 'Nullstellen ⟦x = 0⟧ (einfach, Schnitt) und ⟦x = 2⟧ (doppelt, Berührpunkt).'],
     'probe': 'f(2) = 8 − 16 + 8 = 0 ✓',
     'fehler': 'Aus (x − 2)² die Nullstellen 2 und −2 abzulesen ist falsch: Es gibt nur ⟦x = 2⟧, und zwar doppelt.'},
    {'lernziel': 'graph_term', 'titel': 'Graph und Term zuordnen',
     'regel': 'Vergleiche ⟦Randverhalten⟧ (Grad, Vorzeichen des Leitkoeffizienten), ⟦Nullstellen⟧ mit Schnitt oder Berührung und den ⟦y-Achsenabschnitt⟧ f(0).',
     'schritte': ['Graph: von links unten nach rechts oben, Nullstellen −1 (Schnitt) und 2 (Berührung).', 'Passend: ⟦f(x) = (x + 1)(x − 2)²⟧ (Grad 3, positiver Leitkoeffizient).'],
     'probe': 'f(0) = 1 · 4 = 4: Der Graph schneidet die y-Achse bei 4 ✓',
     'fehler': 'f(x) = (x − 1)(x + 2)² passt nicht: Die Nullstellen haben die ⟦falschen Vorzeichen⟧ (1 und −2 statt −1 und 2).'},
    {'lernziel': 'term_bestimmen', 'titel': 'Funktionsterm aus Nullstellen',
     'regel': 'Kennt man alle Nullstellen mit Vielfachheit, setzt man ⟦f(x) = a · (x − x₁)(x − x₂)…⟧ an und bestimmt a mit ⟦einem weiteren Punkt⟧.',
     'schritte': ['Nullstellen −1, 1, 3 (einfach), Punkt (0 | 6): f(x) = a(x + 1)(x − 1)(x − 3).', 'f(0) = a · 1 · (−1) · (−3) = 3a = 6 ⇒ ⟦a = 2⟧.'],
     'probe': 'f(0) = 2 · 3 = 6 ✓',
     'fehler': 'Den Punkt (0 | 6) als a = 6 zu deuten ist falsch: f(0) ist das Produkt ⟦a · (0 + 1)(0 − 1)(0 − 3)⟧ = 3a.'},
]
_E = {e['lernziel']: e for e in ETAPPEN}
_E['randverhalten']['bild'] = koord([g_poly([-1, 10, 0, 0, -2], name='f')], x=(-3, 11), y=(-1500, 2000), schritt_y=500)
_E['symmetrie']['bild'] = koord([g_poly([2, 0, -1, 0, 3], name='f')], x=(-2, 2), y=(0, 8), punkte=[{'x': -1, 'y': 4}, {'x': 1, 'y': 4}])
_E['nullstellen']['bild'] = koord([g_poly([1, -4, 4, 0], name='f')], x=(-1, 4), y=(-4, 4), punkte=[{'x': 0, 'y': 0, 'name': 'Schnitt'}, {'x': 2, 'y': 0, 'name': 'Berührung'}])
_E['graph_term']['bild'] = graph_bild(mal([1, 1], [1, -2], [1, -2]), [-1, 2], x=(-2, 4))
_E['term_bestimmen']['bild'] = koord([g_poly([2 * c for c in mal([1, 1], [1, -1], [1, -3])])], x=(-2, 4), y=(-15, 15),
                                     punkte=[{'x': -1, 'y': 0}, {'x': 1, 'y': 0}, {'x': 3, 'y': 0}, {'x': 0, 'y': 6, 'name': '(0 | 6)'}])


ART = {'Grad': 'den Grad', 'Leitkoeffizient': 'den Leitkoeffizienten', 'Absolutglied': 'das Absolutglied'}


def g_grad(s):
    n = R.randint(2, 6)
    k = [nz(6)] + [R.randint(-6, 6) for _ in range(n)]
    if s == 1:
        frage = R.choice(['Grad', 'Leitkoeffizient', 'Absolutglied'])
        v = {'Grad': n, 'Leitkoeffizient': k[0], 'Absolutglied': k[-1]}[frage]
        return zahl(f'Bestimme {ART[frage]} von f(x) = {poly(*k)}.', f'Höchste Potenz x{str(n).translate(HOCHZ)} mit Faktor {dz(k[0])}, Absolutglied {dz(k[-1])}: {frage} = {dz(v)}.',
                    'Suche das Glied mit der höchsten Hochzahl bzw. die Zahl ohne x.', v,
                    {'Grad': f'{len(k) - 1}', 'Leitkoeffizient': f'{k[0]}', 'Absolutglied': f'{wert_c(k, 0)}'}[frage])
    if s == 2:
        # Summanden ungeordnet
        teile = [(c, n - i) for i, c in enumerate(k) if c]
        R.shuffle(teile)
        def term(c, e):
            if e == 0: return dz(c)
            return ('' if abs(c) == 1 else dz(abs(c))) + 'x' + (str(e).translate(HOCHZ) if e > 1 else '')
        t = ''
        for i, (c, e) in enumerate(teile):
            t += (('−' if c < 0 else '') + term(abs(c), e) if e else dz(c)) if i == 0 else (f' {"−" if c < 0 else "+"} ' + term(abs(c), e))
        frage = R.choice(['Grad', 'Leitkoeffizient'])
        v = n if frage == 'Grad' else k[0]
        return zahl(f'Bestimme {ART[frage]} von f(x) = {t}.', f'Nach Potenzen geordnet: f(x) = {poly(*k)}. {frage} = {dz(v)}.',
                    'Ordne zuerst nach fallenden Hochzahlen.', v, f'{len(k) - 1}' if frage == 'Grad' else f'{k[0]}')
    a = nz(4)
    nst = {p: R.randint(1, 3) for p in R.sample(range(-4, 5), R.randint(2, 3))}
    kf = [a * c for c in mal(*[[1, -p] for p, m in nst.items() for _ in range(m)])]
    frage = R.choice(['Grad', 'Leitkoeffizient', 'Absolutglied'])
    v = {'Grad': len(kf) - 1, 'Leitkoeffizient': a, 'Absolutglied': kf[-1]}[frage]
    return zahl(f'Bestimme ohne vollständiges Ausmultiplizieren {ART[frage]} von f(x) = {produkt(a, nst)}.',
                {'Grad': f'Grad = Summe der Exponenten = {" + ".join(str(m) for m in nst.values())} = {len(kf) - 1}.',
                 'Leitkoeffizient': f'Höchste Potenz entsteht aus a · x · x · …: Leitkoeffizient {dz(a)}.',
                 'Absolutglied': f'Absolutglied = f(0) = {dz(kf[-1])}.'}[frage],
                'Grad: Exponenten addieren. Leitkoeffizient: Faktor vor den Klammern. Absolutglied: f(0).', v,
                {'Grad': f'{len(kf) - 1}', 'Leitkoeffizient': f'{a}', 'Absolutglied': wert_c(kf, 0)}[frage])


def g_ausmultiplizieren(s):
    if s == 1:
        p, q = R.sample([i for i in range(-6, 7) if i], 2)
        k = mal([1, -p], [1, -q])
        return luecken(f'Multipliziere aus: f(x) = {faktor(p)} · {faktor(q)}.', 'x² + □x + □', 'Koeffizienten (mit Vorzeichen)', k[1:],
                       f'{faktor(p)} · {faktor(q)} = {poly(*k)}.', 'Jedes Glied der ersten Klammer mit jedem der zweiten multiplizieren.',
                       c=[f'-({p}) - ({q})', f'({p}) * ({q})'])
    if s == 2:
        p, q, r = R.sample([i for i in range(-4, 5) if i], 3)
        k = mal([1, -p], [1, -q], [1, -r])
        return luecken(f'Multipliziere aus: f(x) = {faktor(p)} · {faktor(q)} · {faktor(r)}.', 'x³ + □x² + □x + □', 'Koeffizienten (mit Vorzeichen)', k[1:],
                       f'{faktor(p)} · {faktor(q)} = {poly(*mal([1, -p], [1, -q]))}; mal {faktor(r)}: {poly(*k)}.', 'Erst zwei Klammern, dann mit der dritten.',
                       c=[f'-({p}) - ({q}) - ({r})', f'({p}) * ({q}) + ({p}) * ({r}) + ({q}) * ({r})', f'-({p}) * ({q}) * ({r})'])
    a = R.choice([-2, -1, 2, 3])
    p, q = R.sample([i for i in range(-4, 5) if i], 2)
    k = [a * c for c in mal([1, -p], [1, -p], [1, -q])]
    return luecken(f'Multipliziere aus: f(x) = {produkt(a, {p: 2, q: 1})}.', '□x³ + □x² + □x + □', 'Koeffizienten (mit Vorzeichen)', k,
                   f'{faktor(p, 2)} = {poly(*mal([1, -p], [1, -p]))}; mal {faktor(q)} und mal {dz(a)}: {poly(*k)}.',
                   'Binomische Formel für das Quadrat, dann weiter multiplizieren, zuletzt mit dem Faktor davor.',
                   c=[f'{a}', f'{a} * (-2 * ({p}) - ({q}))', f'{a} * (({p}) ** 2 + 2 * ({p}) * ({q}))', f'{a} * (-({p}) ** 2 * ({q}))'])


def g_randverhalten(s):
    n = R.randint(2, 7)
    a = nz(5)
    k = [a] + [R.randint(-9, 9) for _ in range(n)]
    r = VERL[(n % 2, 1 if a > 0 else -1)]
    if s == 3 and R.random() < 0.5:
        # Glied mit höchster Potenz nicht vorne, großes niedrigeres Glied als Ablenkung
        k[1] = R.choice([20, 30, -20, -30])
        teile = [(k[i], n - i) for i in range(len(k)) if k[i]]
        teile = teile[1:] + teile[:1]
        t = ''
        for i, (c, e) in enumerate(teile):
            tt = (('' if abs(c) == 1 else dz(abs(c))) + 'x' + (str(e).translate(HOCHZ) if e > 1 else '')) if e else dz(abs(c))
            t += (('−' if c < 0 else '') + tt) if i == 0 else f' {"−" if c < 0 else "+"} {tt}'
        return auswahl(f'Wie verläuft der Graph von f(x) = {t} für sehr kleine und sehr große x?', r, list(VERL.values()),
                       f'Entscheidend ist nur das Glied mit der höchsten Potenz: {poly(a, *([0] * n))}. Grad {n} {"gerade" if n % 2 == 0 else "ungerade"}, Leitkoeffizient {"positiv" if a > 0 else "negativ"}: {r}.',
                       'Suche das Glied mit der höchsten Hochzahl – die anderen spielen für große |x| keine Rolle.')
    return auswahl(f'Wie verläuft der Graph von f(x) = {poly(*k)} für sehr kleine und sehr große x?', r, list(VERL.values()),
                   f'Höchstes Glied {poly(a, *([0] * n))}: Grad {n} {"gerade" if n % 2 == 0 else "ungerade"}, Leitkoeffizient {"positiv" if a > 0 else "negativ"}: {r}.',
                   'Nur das Glied mit der höchsten Potenz zählt. Gerader oder ungerader Grad? Vorzeichen?')


def g_symmetrie(s):
    art = R.choice(['gerade', 'ungerade', 'gemischt'])
    n = R.randint(3, 6)
    k = []
    for i in range(n + 1):
        e = n - i
        if art == 'gerade' and e % 2: k.append(0)
        elif art == 'ungerade' and e % 2 == 0: k.append(0)
        else: k.append(R.randint(-6, 6))
    if k[0] == 0: k[0] = nz(4)
    # Grad nach Abschneiden prüfen
    while k and k[0] == 0: k.pop(0)
    exps = [len(k) - 1 - i for i, c in enumerate(k) if c]
    if len(exps) < 2: return None
    if all(e % 2 == 0 for e in exps): r = 'achsensymmetrisch zur y-Achse'
    elif all(e % 2 == 1 for e in exps): r = 'punktsymmetrisch zum Ursprung'
    else: r = 'keine dieser Symmetrien'
    if s < 3:
        return auswahl(f'Welche Symmetrie hat der Graph von f(x) = {poly(*k)}?', r,
                       ['achsensymmetrisch zur y-Achse', 'punktsymmetrisch zum Ursprung', 'keine dieser Symmetrien'],
                       f'Vorkommende Hochzahlen: {", ".join(map(str, exps))} – {"nur gerade" if r.startswith("achsen") else "nur ungerade" if r.startswith("punkt") else "gerade und ungerade gemischt"}.',
                       'Schau auf die Hochzahlen; das Absolutglied zählt als x⁰ (gerade).')
    u = R.randint(1, 3)
    fu = fwert(k, u)
    if r.startswith('keine'): return None
    g = fu if r.startswith('achsen') else -fu
    return zahl(f'Für f(x) = {poly(*k)} gilt f({u}) = {dz(fu)}. Bestimme f(−{u}) mithilfe der Symmetrie.',
                f'{r.capitalize()}: f(−x) = {"f(x)" if r.startswith("achsen") else "−f(x)"}, also f(−{u}) = {dz(g)}.', 'Welche Symmetrie hat der Graph?', g,
                wert_c(k, -u))


def g_nullstellen(s):
    if s == 1:
        a = R.choice([1, 2, -1])
        nst = R.sample(range(-5, 6), 3)
        kf = [a * c for c in mal(*[[1, -p] for p in nst])]
        return luecken(f'Bestimme die Nullstellen von f(x) = {produkt(a, {p: 1 for p in nst})}.', '; '.join(f'x{IDX[i]} = □' for i in range(3)),
                       'kleinste zuerst', sorted(nst), f'Jeder Faktor null: x = {", ".join(dz(p) for p in sorted(nst))}.', 'Satz vom Nullprodukt.',
                       c=[f'{p} + ({wert_c(kf, p)})' for p in sorted(nst)])
    if s == 2:
        p, q = R.sample([i for i in range(-5, 6) if i], 2)
        m = R.choice([1, 2])
        kf = mal(*([[1, -p]] * 2 + [[1, -q]] * m)) + [0]
        nst = sorted({0, p, q})
        r = auswahl(f'f(x) = {poly(*kf)} = x · {faktor(p, 2)} · {faktor(q, m)}. An welcher Nullstelle berührt der Graph die x-Achse, ohne sie zu schneiden?',
                    f'x = {dz(p)}' + (f' und x = {dz(q)}' if m == 2 else ''), [f'x = 0', f'x = {dz(q)}' if m == 1 else f'x = {dz(p)}', f'x = {dz(-p)}'],
                    f'Gerade Vielfachheit = Berührung: {faktor(p)} kommt doppelt vor' + (f', {faktor(q)} auch' if m == 2 else '') + '.',
                    'Welche Faktoren kommen in gerader Anzahl vor?')
        return mit_grafik(r, graph_bild(kf, nst))
    typ = R.random()
    if typ < 0.5:
        p, q = R.sample([i for i in range(-6, 7) if i], 2)
        kf = mal([1, -p], [1, -q]) + [0, 0]
        nst = sorted({0, p, q})
        return luecken(f'Bestimme alle Nullstellen von f(x) = {poly(*kf)}.', '; '.join(f'x{IDX[i]} = □' for i in range(len(nst))), 'kleinste zuerst', nst,
                       f'x²({poly(*kf[:-2])}) = 0 ⇒ x = 0 (doppelt), x = {dz(min(p, q))}, x = {dz(max(p, q))}.', 'Klammere die höchste gemeinsame Potenz von x aus.',
                       c=[f'{v} + ({wert_c(kf, v)})' for v in nst])
    a, b = sorted(R.sample(range(1, 6), 2))
    kf = [1, 0, -(a * a + b * b), 0, a * a * b * b]
    return luecken(f'Bestimme alle Nullstellen von f(x) = {poly(*kf)}.', '; '.join(f'x{IDX[i]} = □' for i in range(4)), 'kleinste zuerst', [-b, -a, a, b],
                   f'Substitution z = x²: z = {a * a} oder z = {b * b} ⇒ x = ±{a}, ±{b}.', 'Substituiere z = x².',
                   c=[f'{v} + ({wert_c(kf, v)})' for v in (-b, -a, a, b)])


def g_graph_term(s):
    a = R.choice([1, -1]) if s < 3 else R.choice([1, -1, 2, -2])
    p, q = sorted(R.sample(range(-3, 4), 2))
    m, n = R.choice([(1, 1), (1, 2), (2, 1)] if s == 1 else [(1, 2), (2, 1), (1, 1), (2, 2), (1, 3)])
    if p == -q and m == n: return None
    nst = {p: m, q: n}
    kf = [a * c for c in mal(*[[1, -v] for v, k in nst.items() for _ in range(k)])]
    richtig = 'f(x) = ' + produkt(a, nst)
    andere = ['f(x) = ' + produkt(-a, nst), 'f(x) = ' + produkt(a, {-p: m, -q: n}), 'f(x) = ' + produkt(a, {p: n, q: m}) if m != n else 'f(x) = ' + produkt(a, {p: m + 1, q: n})]
    return mit_grafik(auswahl('Welcher Funktionsterm gehört zum gezeichneten Graphen?', richtig, andere,
                              f'Nullstellen {dz(p)} ({"Schnitt" if m % 2 else "Berührung"}) und {dz(q)} ({"Schnitt" if n % 2 else "Berührung"}); Grad {m + n}, Leitkoeffizient {"positiv" if a > 0 else "negativ"} (Verlauf {VERL[((m + n) % 2, 1 if a > 0 else -1)]}).',
                              'Lies die Nullstellen ab (Vorzeichen!), achte auf Schnitt/Berührung und auf den Verlauf ganz links und rechts.'),
                      graph_bild(kf, [p, q]))


def g_term_bestimmen(s):
    nst = sorted(R.sample([i for i in range(-3, 4) if i], 2 if s == 1 else 3))
    a = nz(3)
    kf = [a * c for c in mal(*[[1, -v] for v in nst])]
    f0 = kf[-1]
    if f0 == 0: return None
    if s == 3 and R.random() < 0.5:
        u = R.choice([t for t in range(-4, 5) if t not in nst and t != 0])
        fu = fwert(kf, u)
        if abs(fu) > 60: return None
        return mit_grafik(zahl(f'Der Graph einer Funktion 3. Grades hat die einfachen Nullstellen {", ".join(dz(v) for v in nst)} und geht durch P({dz(u)} | {dz(fu)}). Bestimme a in f(x) = a · (x − x₁)(x − x₂)(x − x₃).',
                               f'f({dz(u)}) = a · {" · ".join("(" + dz(u) + " − " + kl(v) + ")" for v in nst)} = {dz(fu / a)}a = {dz(fu)} ⇒ a = {dz(a)}.',
                               'Setze die Nullstellen in die Produktform ein, dann den Punkt P.', a, f'({fu}) / ({" * ".join(f"({u} - ({v}))" for v in nst)})'),
                          graph_bild(kf, nst, punkte=[{'x': u, 'y': float(fu), 'name': 'P'}]))
    return mit_grafik(zahl(f'Der gezeichnete Graph hat die einfachen Nullstellen {", ".join(dz(v) for v in nst)} und schneidet die y-Achse bei {dz(f0)}. Bestimme a in f(x) = a · ' +
                           ''.join(f'(x − x{IDX[i]})' for i in range(len(nst))) + '.',
                           f'f(0) = a · {" · ".join(kl(-v) for v in nst)} = {dz(f0 // a)}a = {dz(f0)} ⇒ a = {dz(a)}.',
                           'Setze x = 0 in die Produktform ein.', a, f'({f0}) / ({" * ".join(f"(0 - ({v}))" for v in nst)})'),
                      graph_bild(kf, nst, punkte=[{'x': 0, 'y': f0, 'name': f'(0 | {dz(f0)})'}]))


GEN = schoen({'grad': g_grad, 'ausmultiplizieren': g_ausmultiplizieren, 'randverhalten': g_randverhalten, 'symmetrie': g_symmetrie,
              'nullstellen': g_nullstellen, 'graph_term': g_graph_term, 'term_bestimmen': g_term_bestimmen})

if __name__ == '__main__':
    bauen('funktionen.ganzrational',
          'Ganzrationale Funktionen beschreiben: Grad und Koeffizienten, Randverhalten, Symmetrie, Nullstellen mit Vielfachheit; Graph und Term zuordnen und Terme aus Nullstellen bestimmen.',
          ['Grad = höchste Hochzahl, Leitkoeffizient = ihr Faktor, Absolutglied = f(0).', 'Randverhalten: nur das höchste Glied zählt.',
           'Nur gerade Hochzahlen: achsensymmetrisch; nur ungerade: punktsymmetrisch.', 'Ungerade Vielfachheit: Schnitt; gerade: Berührung.'],
          [('Aufbau', ['grad', 'ausmultiplizieren']), ('Eigenschaften', ['randverhalten', 'symmetrie', 'nullstellen']), ('Graph und Term', ['graph_term', 'term_bestimmen'])],
          ETAPPEN, GEN,
          meiden={'grad': ['−2x³ + 5x − 7.'], 'ausmultiplizieren': ['(x − 1) · (x + 2) · (x − 3)'], 'symmetrie': ['2x⁴ − x² + 3?'], 'nullstellen': ['x³ − 4x² + 4x']},
          offen=['Zeichnungen: Graphen in den Lernkarten „randverhalten“, „symmetrie“, „nullstellen“, „graph_term“, „term_bestimmen“; Aufgaben zu Berührung, „Welcher Term gehört zum Graphen?“ und „a aus Nullstellen und Punkt“ zeigen den Graphen.',
                 'Lückenaufgaben „Ausmultiplizieren“ nutzen die Term-Vorlage (z. B. „x³ + □x² + □x + □“): Das Kind tippt den Term frei ein; Koeffizienten können negativ sein.',
                 'Extrempunkte (Ableitung) sind nicht enthalten – das ist Stoff der Oberstufe.'])
