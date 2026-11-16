#!/usr/bin/env python3
"""Thema funktionen.ganzrational – Ganzrationale Funktionen (Klasse 10). Schreibt inhalte/themen/funktionen.ganzrational.json."""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import *  # noqa: E402,F403
from _schwer_kl10 import ergaenzen  # noqa: E402

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


def _produktform_finden():
    nst = sorted(R.sample([i for i in range(-5, 6) if i], 3))
    kf = mal(*[[1, -v] for v in nst])
    p = R.choice(nst)
    q, r = [v for v in nst if v != p]
    b = kf[1] + p           # (x − p)(x² + bx + c) = x³ + (b − p)x² + (c − pb)x − pc
    c = -kf[3] // p
    return luecken(f'f(x) = {poly(*kf)} hat die Nullstelle x = {dz(p)}. Schreibe f in Produktform (kleinste Nullstelle zuerst).',
                   '(x − □)(x − □)(x − □)', 'die drei Nullstellen, kleinste zuerst (auch negativ)', nst,
                   f'Ansatz f(x) = {faktor(p)}(x² + bx + c). Absolutglied: −{kl(p)} · c = {dz(kf[3])} ⇒ c = {dz(c)}; '
                   f'x²-Glied: b − {kl(p)} = {dz(kf[1])} ⇒ b = {dz(b)}. {poly(1, b, c)} = {faktor(q)}{faktor(r)}. '
                   f'Also f(x) = {"".join(faktor(v) for v in nst)}.',
                   'Die anderen Nullstellen sind Teiler des Absolutglieds – probiere sie aus, oder vergleiche die Koeffizienten von (x − Nullstelle)(x² + bx + c).',
                   c=[f'{v} + ({wert_c(kf, v)})' for v in nst])


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
    if R.random() < 0.45:
        return _produktform_finden()
    a = R.choice([-2, -1, 2, 3])
    p, q = R.sample([i for i in range(-4, 5) if i], 2)
    k = [a * c for c in mal([1, -p], [1, -p], [1, -q])]
    return luecken(f'Multipliziere aus: f(x) = {produkt(a, {p: 2, q: 1})}.', '□x³ + □x² + □x + □', 'Koeffizienten (mit Vorzeichen)', k,
                   f'{faktor(p, 2)} = {poly(*mal([1, -p], [1, -p]))}; mal {faktor(q)} und mal {dz(a)}: {poly(*k)}.',
                   'Binomische Formel für das Quadrat, dann weiter multiplizieren, zuletzt mit dem Faktor davor.',
                   c=[f'{a}', f'{a} * (-2 * ({p}) - ({q}))', f'{a} * (({p}) ** 2 + 2 * ({p}) * ({q}))', f'{a} * (-({p}) ** 2 * ({q}))'])


GL = {(0, 1): 'Grad gerade, Leitkoeffizient positiv', (0, -1): 'Grad gerade, Leitkoeffizient negativ',
      (1, 1): 'Grad ungerade, Leitkoeffizient positiv', (1, -1): 'Grad ungerade, Leitkoeffizient negativ'}


def _rand_graph():
    n = R.choice([3, 3, 4, 4, 5])
    a = R.choice([1, -1])
    nst = sorted(R.sample(range(-3, 4), n if n < 5 else 3))
    viel = [1] * len(nst)
    while sum(viel) < n: viel[R.randrange(len(viel))] += 1
    if max(viel) > 2: return None
    kf = [a * c for c in mal(*[[1, -v] for v, k in zip(nst, viel) for _ in range(k)])]
    r = GL[(n % 2, a)]
    return mit_grafik(auswahl('Die Zeichnung zeigt den Graphen einer ganzrationalen Funktion. Welche Aussage über Grad und Leitkoeffizienten passt?', r, list(GL.values()),
                              f'Der Graph verläuft {VERL[(n % 2, a)]}: {"beide Enden auf derselben Seite ⇒ Grad gerade" if n % 2 == 0 else "Enden auf verschiedenen Seiten ⇒ Grad ungerade"}; '
                              f'{"rechts oben ⇒ Leitkoeffizient positiv" if a > 0 else "rechts unten ⇒ Leitkoeffizient negativ"}.',
                              'Schau nur auf die beiden Enden: Liegen sie auf derselben Seite der x-Achse? Wohin geht der Graph ganz rechts?'),
                      graph_bild(kf, nst))


def _rand_produkt():
    a = R.choice([1, -1, 2, -2, Fr(1, 2)])
    p, q = R.sample([i for i in range(-4, 5)], 2)
    m, n = R.choice([(1, 2), (2, 1), (2, 3), (3, 2), (1, 3), (3, 1), (2, 2), (1, 4)])
    g = m + n
    r = VERL[(g % 2, 1 if a > 0 else -1)]
    term = produkt(a, {p: m, q: n})
    return auswahl(f'Wie verläuft der Graph von f(x) = {term} für sehr kleine und sehr große x?', r, list(VERL.values()),
                   f'Ausmultipliziert beginnt f mit {dz(a) if a not in (1, -1) else ("−" if a < 0 else "")}x' + str(g).translate(HOCHZ) +
                   f': Grad {g} = {m} + {n} ({"gerade" if g % 2 == 0 else "ungerade"}), Leitkoeffizient {"positiv" if a > 0 else "negativ"}: {r}.',
                   'Du musst nicht ausmultiplizieren: Der Grad ist die Summe der Hochzahlen, der Leitkoeffizient der Faktor davor.')


def g_randverhalten(s):
    pool, nr = AKT['pool'], AKT['nr']
    # Regel: die Standardfrage „Wie verläuft … f(x) = …?“ höchstens 14-mal je Karte
    if s == 2 and ((pool == 'uebung' and nr % 3 != 0) or (pool != 'uebung' and nr % 2 == 0)):
        return _rand_graph()
    if s == 3 and nr % 3 != 2:
        return _rand_produkt()
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


def _substitution_wenige():
    """x⁴ + bx² + c mit z₁ > 0, z₂ < 0: nur zwei Lösungen."""
    a, c = R.randint(1, 5), R.randint(1, 9)
    kf = [1, 0, -(a * a - c), 0, -a * a * c]
    return luecken(f'Bestimme alle Nullstellen von f(x) = {poly(*kf)}.', 'x₁ = □; x₂ = □', 'kleinste zuerst', [-a, a],
                   f'z = x²: z² {plus(-(a * a - c))}z − {a * a * c} = 0 ⇒ z = {a * a} oder z = −{c}. x² = {a * a} ⇒ x = ±{a}; x² = −{c} hat keine Lösung.',
                   'Substituiere z = x². Liefert jede z-Lösung auch x-Werte?', c=[f'{v} + ({wert_c(kf, v)})' for v in (-a, a)])


def _vielfachheit_am_graphen():
    """Nur ausmultiplizierte Form, eine Nullstelle verraten, Vielfachheit am Graphen ablesen."""
    p = R.choice([-3, -2, -1, 1, 2, 3])
    q = R.choice([v for v in range(-3, 4) if v != p])
    m, n = R.choice([(1, 2), (2, 1), (2, 2), (1, 1)])
    a = R.choice([1, -1])
    kf = [a * c for c in mal(*([[1, -p]] * m + [[1, -q]] * n))]
    richtig = 'doppelt – der Graph berührt dort die x-Achse' if m == 2 else 'einfach – der Graph schneidet dort die x-Achse'
    falsch = ['doppelt – der Graph schneidet dort die x-Achse', 'einfach – der Graph berührt dort die x-Achse',
              'einfach – der Graph schneidet dort die x-Achse' if m == 2 else 'doppelt – der Graph berührt dort die x-Achse']
    return mit_grafik(auswahl(f'f(x) = {poly(*kf)} hat die Nullstelle x = {dz(p)}. Die Zeichnung zeigt den Graphen. Ist x = {dz(p)} eine einfache oder eine doppelte Nullstelle?',
                              richtig, falsch,
                              f'Bei x = {dz(p)} {"berührt" if m == 2 else "schneidet"} der Graph die x-Achse, also {"gerade Vielfachheit: doppelt" if m == 2 else "ungerade Vielfachheit: einfach"}. '
                              f'Probe: f(x) = {produkt(a, {p: m, q: n})}.',
                              'Schneidet der Graph die x-Achse dort (Vorzeichenwechsel) oder berührt er sie nur?'),
                      graph_bild(kf, [p, q]))


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
        r = auswahl(f'f(x) = {poly(*kf)} = x · {faktor(p, 2)} · {faktor(q, m)}. An welchen Nullstellen berührt der Graph die x-Achse, ohne sie zu schneiden?',
                    f'x = {dz(p)}' + (f' und x = {dz(q)}' if m == 2 else ''), [f'x = 0', f'x = {dz(q)}' if m == 1 else f'x = {dz(p)}', f'x = {dz(-p)}'],
                    f'Gerade Vielfachheit = Berührung: {faktor(p)} kommt doppelt vor' + (f', {faktor(q)} auch' if m == 2 else '') + '.',
                    'Welche Faktoren kommen in gerader Anzahl vor?')
        return mit_grafik(r, graph_bild(kf, nst))
    nr = AKT['nr']
    typ = R.random()
    if nr % 3 == 0:
        return _vielfachheit_am_graphen()
    if nr % 3 == 1 and typ < 0.6:
        return _substitution_wenige()
    if nr % 3 == 2:
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



# ---------- KLAR: Lernkarten im neuen Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst nach dem Bauen der Aufgaben eingesetzt (bauen(..., klar=KLAR)), die Aufgaben bleiben wörtlich gleich.
# Muster: einstieg (≤ 35 Wörter) → Kartenbild → Schritte als {text, bild} (Bildergeschichte) → „Pass auf!“ (fehler + fehler_bild) → MERKE (regel).
_POSTEN = {'typ': 'tabelle', 'kopf': ['Posten', '−2x³', '5x', '−7']}
_MAL = {'typ': 'tabelle', 'kopf': ['·', 'x', '+ 2']}
_PROFIL = {'typ': 'koordinaten', 'x': [-1, 4], 'y': [-4, 4], 'graphen': [{'art': 'poly', 'k': [0, 4, -4, 1], 'name': 'f'}]}
_WURZELN = [{'x': -1, 'y': 0}, {'x': 1, 'y': 0}, {'x': 3, 'y': 0}]
KLAR = {
 'grad': {
  'einstieg': 'Ein Kassenbon besteht aus Posten, die zusammengezählt werden. Manche Funktionen sind genauso gebaut, mit Posten wie 5x, −2x³ und −7. '
              'So eine Summe heißt ⟦ganzrationale Funktion⟧.',
  'woerter': [['Grad', 'die höchste Hochzahl von x'],
              ['Leitkoeffizient', 'die Zahl vor der höchsten Potenz, mit Vorzeichen'],
              ['Absolutglied', 'der Posten ohne x; er ist gleich f(0)']],
  'bild': _POSTEN | {'zeilen': [['Hochzahl', '?', '?', '?'], ['Zahl davor', '?', '?', '?']]},
  'schritte': [{'text': 'f(x) = −2x³ + 5x − 7 hat drei Posten.'},
               {'text': 'Die Hochzahlen sind 3, 1 und 0. Der Grad ist ⟦3⟧.',
                'bild': {'zeilen': [['Hochzahl', '3', '1', '0'], ['Zahl davor', '?', '?', '?']]}},
               {'text': 'Vor x³ steht −2: Das ist der Leitkoeffizient.',
                'bild': {'zeilen': [['Hochzahl', '3', '1', '0'], ['Zahl davor', '−2', '5', '−7']]}},
               {'text': 'Der Posten ohne x ist das Absolutglied. Es ist ⟦f(0) = −7⟧.'}],
  'fehler': 'Bei 4 + x² − 3x³ ist der Leitkoeffizient nicht 4. Er gehört zur ⟦höchsten Potenz⟧, nicht zum ersten Posten: −3.',
  'fehler_bild': {'typ': 'tabelle', 'kopf': ['Posten', '4', 'x²', '−3x³'], 'zeilen': [['Hochzahl', '0', '2', '3: höchste'], ['Zahl davor', '4', '1', '−3']]},
  'regel': 'Die höchste Hochzahl ist der Grad. Die Zahl davor heißt ⟦Leitkoeffizient⟧, die Zahl ohne x Absolutglied.'},
 'ausmultiplizieren': {
  'einstieg': 'Ein rechteckiges Beet wird geplant. Es ist (x − 1) m lang und (x + 2) m breit. '
              'Rechnet man die Fläche als Summe aus, heißt das ⟦Ausmultiplizieren⟧.',
  'woerter': [['Produktform', 'Klammern, die miteinander malgenommen werden'],
              ['Ausmultiplizieren', 'jedes Glied mit jedem malnehmen, dann zusammenfassen'],
              ['gemischte Glieder', 'die Produkte „außen mal innen“, hier 2x und −x']],
  'bild': _MAL | {'zeilen': [['x', '?', '?'], ['− 1', '?', '?']]},
  'schritte': [{'text': 'Die Produktform (x − 1)(x + 2) wird ausgerechnet: jedes Glied mit jedem.'},
               {'text': 'Erste Zeile: x · x = x² und x · 2 = 2x.', 'bild': {'zeilen': [['x', 'x²', '2x'], ['− 1', '?', '?']]}},
               {'text': 'Zweite Zeile: −1 · x = −x und −1 · 2 = −2.', 'bild': {'zeilen': [['x', 'x²', '2x'], ['− 1', '−x', '−2']]}},
               {'text': 'Gemischte Glieder zusammenfassen: 2x − x = x. Ergebnis ⟦x² + x − 2⟧.'}],
  'fehler': '(x − 1)(x + 2) = x² − 2 ist falsch. Die ⟦gemischten Glieder⟧ 2x und −x fehlen. Probe x = 3: 2 · 5 = 10, nicht 7.',
  'fehler_bild': {'zeilen': [['x', 'x²', '2x fehlt'], ['− 1', '−x fehlt', '−2']]},
  'regel': 'Multipliziere jedes Glied mit jedem. Danach ⟦gleiche Potenzen zusammenfassen⟧. Bei drei Klammern erst zwei, dann die dritte.'},
 'randverhalten': {
  'einstieg': 'Beim Tauziehen stehen drei Kinder gegen ein Pferd. Wenn alle richtig ziehen, gewinnt das Pferd. '
              'Bei Funktionen ist die höchste Potenz das Pferd. Sie bestimmt das ⟦Randverhalten⟧.',
  'woerter': [['Randverhalten', 'wohin der Graph ganz links und ganz rechts geht'],
              ['Leitkoeffizient', 'die Zahl vor der höchsten Potenz']],
  'bild': {'typ': 'koordinaten', 'x': [-3, 11], 'y': [-1500, 2000], 'graphen': [{'art': 'poly', 'k': [-2, 0, 0, 10, -1], 'name': 'f'}], 'schritt_y': 500},
  'schritte': [{'text': 'f(x) = −x⁴ + 10x³ − 2: Die höchste Potenz ist −x⁴.'},
               {'text': 'Grad 4 ist gerade: Beide Enden zeigen in dieselbe Richtung.'},
               {'text': 'Der Leitkoeffizient −1 ist negativ: Beide Enden gehen nach unten.'},
               {'text': 'Also verläuft der Graph ⟦von links unten nach rechts unten⟧.',
                'bild': {'punkte': [{'x': -2.5, 'y': -197, 'name': 'links: unten'}, {'x': 10.8, 'y': -1010, 'name': 'rechts: unten'}]}}],
  'fehler': 'Wegen +10x³ geht der Graph rechts nicht nach oben. Für große x ⟦gewinnt die höchste Potenz⟧. Bei x = 100 ist x⁴ zehnmal so groß wie 10x³.',
  'regel': 'Am Rand zählt nur die höchste Potenz. Gerader Grad: beide Enden auf einer Seite. Negativer ⟦Leitkoeffizient⟧ spiegelt an der x-Achse.'},
 'symmetrie': {
  'einstieg': 'Ein Schmetterling sieht links und rechts gleich aus. Der Buchstabe S sieht nach einer halben Drehung wieder gleich aus. '
              'Auch Graphen können eine solche ⟦Symmetrie⟧ haben.',
  'woerter': [['achsensymmetrisch', 'an der y-Achse gespiegelt gleich: f(−x) = f(x)'],
              ['punktsymmetrisch', 'um (0 | 0) halb gedreht gleich'],
              ['x⁰', 'x hoch 0 ist 1; die Zahl ohne x zählt als Hochzahl 0']],
  'bild': {'typ': 'koordinaten', 'x': [-2, 2], 'y': [0, 8], 'graphen': [{'art': 'poly', 'k': [3, 0, -1, 0, 2], 'name': 'f'}]},
  'schritte': [{'text': 'f(x) = 2x⁴ − x² + 3 hat die Hochzahlen 4, 2 und 0.'},
               {'text': 'Die 3 zählt als 3 · x⁰. Alle Hochzahlen sind gerade.'},
               {'text': 'Dann ist f(−x) = f(x). Probe: f(1) = 4 und f(−1) = 4.', 'bild': {'punkte': [{'x': -1, 'y': 4, 'name': 'f(−1) = 4'}, {'x': 1, 'y': 4, 'name': 'f(1) = 4'}]}},
               {'text': 'Also ⟦achsensymmetrisch zur y-Achse⟧. Nur ungerade Hochzahlen hieße punktsymmetrisch.'}],
  'fehler': 'x³ + 1 ist nicht punktsymmetrisch. Die 1 zählt als ⟦gerade⟧ Hochzahl (x⁰). Probe: f(−1) = 0, aber −f(1) = −2.',
  'fehler_bild': {'typ': 'koordinaten', 'x': [-2, 2], 'y': [-4, 6], 'graphen': [{'art': 'poly', 'k': [1, 0, 0, 1], 'name': 'x³ + 1'}],
                  'punkte': [{'x': -1, 'y': 0, 'name': 'f(−1) = 0'}, {'x': 1, 'y': 2, 'name': 'f(1) = 2'}]},
  'regel': 'Nur gerade Hochzahlen: ⟦achsensymmetrisch⟧. Nur ungerade: punktsymmetrisch zum Ursprung. Gemischt: keine von beiden.'},
 'nullstellen': {
  'einstieg': 'Ein Wanderweg führt am See entlang. An einer Stelle führt er durchs flache Wasser. An einer anderen berührt er nur das Ufer. '
              'Diese Stellen sind ⟦Nullstellen⟧.',
  'woerter': [['Nullstelle', 'eine Stelle x mit f(x) = 0: der Weg auf Höhe des Wassers'],
              ['binomische Formel', '(a − b)² = a² − 2ab + b²'],
              ['doppelte Nullstelle', 'der Faktor kommt zweimal vor; der Graph berührt nur']],
  'bild': _PROFIL,
  'schritte': [{'text': 'f(x) = x³ − 4x² + 4x. Zuerst x ausklammern: x(x² − 4x + 4).'},
               {'text': 'Die Klammer ist eine binomische Formel: (x − 2)².'},
               {'text': 'Der Faktor x kommt einmal vor: Bei 0 schneidet der Graph die x-Achse.',
                'bild': {'punkte': [{'x': 0, 'y': 0, 'name': 'Schnitt'}]}},
               {'text': '2 ist eine doppelte Nullstelle: Dort ⟦berührt⟧ der Graph die x-Achse.',
                'bild': {'punkte': [{'x': 0, 'y': 0, 'name': 'Schnitt'}, {'x': 2, 'y': 0, 'name': 'Berührung'}]}}],
  'fehler': '(x − 2)² hat nicht die Nullstellen 2 und −2. Denn (−2 − 2)² = 16. Es gibt nur ⟦x = 2⟧, doppelt.',
  'fehler_bild': {'punkte': [{'x': 0, 'y': 0}, {'x': 2, 'y': 0, 'name': 'nur 2, doppelt'}]},
  'regel': 'Löse f(x) = 0. Ungerade Vielfachheit: Der Graph schneidet. Gerade: Er ⟦berührt⟧ die x-Achse nur.'},
 'graph_term': {
  'einstieg': 'Auf einer Wanderkarte ist ein Höhenprofil gezeichnet, aber die Beschriftung fehlt. Drei Rechenvorschriften stehen zur Wahl. '
              'Man vergleicht Merkmale, um den passenden ⟦Funktionsterm⟧ zu finden.',
  'woerter': [['Funktionsterm', 'die Rechenvorschrift, z. B. (x + 1)(x − 2)²'],
              ['y-Achsenabschnitt', 'wo der Graph die y-Achse schneidet: f(0)']],
  'bild': {'typ': 'koordinaten', 'x': [-2, 4], 'y': [-8, 8], 'graphen': [{'art': 'poly', 'k': [4, 0, -3, 1]}]},
  'schritte': [{'text': 'Von links unten nach rechts oben: ungerader Grad, Leitkoeffizient positiv.'},
               {'text': 'Schnitt bei −1, Berührung bei 2: (x + 1) einmal, (x − 2) zweimal.',
                'bild': {'punkte': [{'x': -1, 'y': 0, 'name': 'Schnitt'}, {'x': 2, 'y': 0, 'name': 'Berührung'}]}},
               {'text': 'Probe mit dem y-Achsenabschnitt: f(0) = 1 · 4 = 4. Das passt.',
                'bild': {'punkte': [{'x': -1, 'y': 0, 'name': 'Schnitt'}, {'x': 2, 'y': 0, 'name': 'Berührung'}, {'x': 0, 'y': 4, 'name': '(0 | 4)'}]}},
               {'text': 'Der Funktionsterm ist ⟦f(x) = (x + 1)(x − 2)²⟧.'}],
  'fehler': '(x − 1)(x + 2)² passt nicht. Die Klammer (x − 1) gehört zur Nullstelle ⟦1⟧, nicht zu −1. In der Klammer steht die Gegenzahl.',
  'fehler_bild': {'punkte': [{'x': 1, 'y': 0, 'name': '1?'}, {'x': -2, 'y': 0, 'name': '−2?'}]},
  'regel': 'Vergleiche Randverhalten, Nullstellen und f(0). Erst wenn ⟦alles passt⟧, gehört der Term zum Graphen.'},
 'term_bestimmen': {
  'einstieg': 'Von einem Weg kennt man nur die Stellen am Wasser und die Höhe am Start. Das reicht für die ganze Rechenvorschrift. '
              'So findet man den ⟦Funktionsterm aus Nullstellen⟧.',
  'woerter': [['Ansatz', 'die Form, in die man das Bekannte einsetzt'],
              ['a', 'der Streckfaktor: macht den Graphen steiler oder flacher']],
  'bild': {'typ': 'koordinaten', 'x': [-2, 4], 'y': [-15, 15], 'graphen': [{'art': 'poly', 'k': [6, -2, -6, 2]}]},
  'schritte': [{'text': 'Nullstellen −1, 1 und 3. Ansatz: f(x) = a(x + 1)(x − 1)(x − 3).', 'bild': {'punkte': _WURZELN}},
               {'text': 'Am Start: f(0) = 6. Einsetzen: a · 1 · (−1) · (−3) = 3a.',
                'bild': {'punkte': _WURZELN + [{'x': 0, 'y': 6, 'name': '(0 | 6)'}]}},
               {'text': 'Aus 3a = 6 folgt ⟦a = 2⟧.'}],
  'fehler': 'Aus f(0) = 6 folgt nicht a = 6. f(0) ist das ganze Produkt ⟦3a⟧. Erst daraus folgt a = 2.',
  'regel': 'Setze f(x) = a(x − x₁)(x − x₂)… an. Bestimme a mit ⟦einem weiteren Punkt⟧.'},
}


GEN = schoen({'grad': g_grad, 'ausmultiplizieren': g_ausmultiplizieren, 'randverhalten': g_randverhalten, 'symmetrie': g_symmetrie,
              'nullstellen': g_nullstellen, 'graph_term': g_graph_term, 'term_bestimmen': g_term_bestimmen})

# ---------- Zehnte Runde (Zweig schwer-kl10): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Zufallsstart (nur zum Mischen der Antworten); wird erst NACH bauen(...) aufgerufen, alte Aufgaben bleiben gleich.
# Vorbilder (Typ und Niveau, eigene Zahlen): Abitur Bayern Prüfungsteil A (2023: Mindestgrad aus Eigenschaften begründen;
# 2025: Graph von g(2x − 1) aus g; IlluPA A2: f(x) = x⁴ − kx² mit Parameter; IlluPA A5: Symmetrie und Extrempunkte),
# Grundwissen G9 Kl. 10 (Randverhalten, Nullstellen und Faktorisieren von (x − 1) · x² · (x + 2)³), Bayerischer Mathematik-Test 10
# (Term mit vorgegebener Eigenschaft angeben). Lücken mit Term-Vorlage nur bis x³ (App-Regel); höhere Grade als Zahlenfelder.
def schwer():
    start(10014)
    N = []

    def neu(l, s, a):
        a['l'], a['s'] = l, s
        N.append(a)

    # --- grad ---
    neu('grad', 2, zahl('Bestimme den Leitkoeffizienten von f(x) = (2x² − 1)³.', 'Höchste Potenz: (2x²)³ = 8x⁶. Leitkoeffizient 8 (nicht 2).',
                        'Nur die höchsten Glieder der Klammer bestimmen das höchste Glied.', 8, '2 ** 3'))
    neu('grad', 2, zahl('Bestimme den Grad von f(x) = (x − 1)(x + 2) − x².', 'Ausmultipliziert: x² + x − 2 − x² = x − 2. Das x² fällt weg, der Grad ist 1.',
                        'Erst ausmultiplizieren und zusammenfassen, dann den Grad ablesen.', 1, '1'))
    neu('grad', 3, zahl('Eine ganzrationale Funktion ist punktsymmetrisch zum Ursprung und hat bei x = 2 eine doppelte Nullstelle. Welchen Grad hat sie mindestens?',
                        'Wegen der Punktsymmetrie ist auch x = −2 doppelte Nullstelle, und f(0) = −f(0) gibt f(0) = 0. Also stecken x · (x − 2)² · (x + 2)² darin: Grad mindestens 5.',
                        'Was folgt aus der Symmetrie für x = −2 und für x = 0?', 5, '1 + 2 + 2'))
    neu('grad', 3, zahl('Für welche Zahl a hat f(x) = (a − 2)x³ + 4x² − 1 den Grad 2?', 'Grad 2 heißt: Das Glied mit x³ verschwindet. a − 2 = 0 ⇒ a = 2.',
                        'Wann fällt das x³-Glied weg?', 2, '2'))
    neu('grad', 3, zahl('Wie groß ist die Summe aller Koeffizienten (mit Absolutglied) von f(x) = (2x − 1)⁵?',
                        'Die Summe aller Koeffizienten ist f(1), denn jede Potenz von 1 ist 1: f(1) = (2 − 1)⁵ = 1.', 'Setze eine geschickte Zahl für x ein, statt auszumultiplizieren.', 1, '(2 - 1) ** 5'))
    neu('grad', 3, auswahl('Welcher Term beschreibt keine ganzrationale Funktion?', 'f(x) = 2/x + x²', ['f(x) = √3 · x² − 1', 'f(x) = (x − 1)⁵', 'f(x) = x³ : 4'],
                           '2/x = 2 · x^(−1) hat einen negativen Exponenten. Ganzrational heißt: nur Potenzen x⁰, x¹, x², … mit beliebigen Zahlen als Faktor (auch √3 oder 1/4).',
                           'Ganzrational: Summe von Vielfachen von x hoch 0, 1, 2, … Welcher Exponent passt nicht?'))

    # --- ausmultiplizieren ---
    neu('ausmultiplizieren', 2, luecken('Multipliziere aus: f(x) = (x − 3)³.', 'x³ + □x² + □x + □', 'Koeffizienten', [-9, 27, -27],
                                        '(x − 3)² = x² − 6x + 9; mal (x − 3): x³ − 3x² − 6x² + 18x + 9x − 27 = x³ − 9x² + 27x − 27.',
                                        'Erst (x − 3)², dann noch einmal mal (x − 3).', c=['-3 - 6', '18 + 9', '-27']))
    neu('ausmultiplizieren', 2, luecken('Multipliziere aus: f(x) = (x² + 2)(x² − 3). Schreibe f(x) = x⁴ + b · x² + c.', 'b = □; c = □', 'Zwei Zahlen', [-1, -6],
                                        'x⁴ − 3x² + 2x² − 6 = x⁴ − x² − 6.', 'Jedes Glied der ersten Klammer mit jedem der zweiten.', c=['-3 + 2', '2 * (-3)']))
    neu('ausmultiplizieren', 3, luecken('f(x) = x³ + x² − 4x − 4. Schreibe f in Produktform (kleinste Nullstelle zuerst).', '(x − □)(x − □)(x − □)', 'Nullstellen aufsteigend',
                                        [-2, -1, 2], 'Gruppieren: x²(x + 1) − 4(x + 1) = (x + 1)(x² − 4) = (x + 1)(x + 2)(x − 2).',
                                        'Klammere aus den ersten beiden und aus den letzten beiden Gliedern aus.', c=['-2 + ((-2)**3 + (-2)**2 + 8 - 4)', '-1 + (-1 + 1 + 4 - 4)', '2 + (8 + 4 - 8 - 4)']))
    neu('ausmultiplizieren', 3, zahl('Für welche Zahl a gilt (x + a)(x − 2) = x² + 3x − 10?', 'Ausmultipliziert: x² + (a − 2)x − 2a. Vergleich: −2a = −10 ⇒ a = 5 (Probe: a − 2 = 3 ✓).',
                                     'Multipliziere aus und vergleiche das Absolutglied.', 5, '10 / 2'))
    neu('ausmultiplizieren', 3, zahl('Welchen Koeffizienten hat x² in f(x) = (x + 1)(x + 2)(x + 3)? Ohne vollständiges Ausmultiplizieren.',
                                     'x² entsteht, wenn man aus zwei Klammern x und aus der dritten die Zahl nimmt: 1 + 2 + 3 = 6.',
                                     'Welche Auswahl aus den drei Klammern liefert genau x²?', 6, '1 + 2 + 3'))
    neu('ausmultiplizieren', 3, auswahl('Jemand schreibt: (x + 2)³ = x³ + 8. Was stimmt?', 'Falsch: (x + 2)³ = x³ + 6x² + 12x + 8.',
                                        ['Richtig.', 'Falsch: (x + 2)³ = x³ + 6x + 8.', 'Falsch: (x + 2)³ = 3x + 6.'],
                                        '(x + 2)² = x² + 4x + 4; mal (x + 2): x³ + 6x² + 12x + 8. Probe mit x = 1: 3³ = 27, aber 1 + 8 = 9.',
                                        'Probe mit x = 1.'))

    # --- randverhalten ---
    neu('randverhalten', 2, auswahl('Wie verläuft der Graph von f(x) = 3x² − x⁴ + 2 für sehr kleine und sehr große x?', 'von links unten nach rechts unten',
                                    ['von links oben nach rechts oben', 'von links unten nach rechts oben', 'von links oben nach rechts unten'],
                                    'Höchstes Glied −x⁴: Grad gerade, Leitkoeffizient negativ: beide Enden unten.', 'Ordne zuerst nach Potenzen.'))
    neu('randverhalten', 2, auswahl('Wie verläuft der Graph von f(x) = −2 · (x − 1)³ für sehr kleine und sehr große x?', 'von links oben nach rechts unten',
                                    ['von links unten nach rechts oben', 'von links oben nach rechts oben', 'von links unten nach rechts unten'],
                                    'Höchstes Glied −2x³: ungerader Grad, negativer Leitkoeffizient.', 'Welches Glied entsteht beim Ausmultiplizieren als höchstes?'))
    neu('randverhalten', 3, auswahl('Wie verläuft der Graph von f(x) = (1 − x)³ · (x + 2)² für sehr kleine und sehr große x?', 'von links oben nach rechts unten',
                                    ['von links unten nach rechts oben', 'von links oben nach rechts oben', 'von links unten nach rechts unten'],
                                    'Höchstes Glied: (−x)³ · x² = −x⁵. Ungerader Grad, negativer Leitkoeffizient. Falle: In (1 − x) steht x mit Minus.',
                                    'Achte auf das Vorzeichen von x in (1 − x).'))
    neu('randverhalten', 3, auswahl('Der Graph von f(x) = a · x⁴ + x³ verläuft von links unten nach rechts unten. Was gilt für a?', 'a < 0', ['a > 0', 'a = 0', 'a < 1'],
                                    'Bei a ≠ 0 entscheidet a · x⁴: gerader Grad, beide Enden unten ⇒ a < 0. (Für a = 0 wäre f(x) = x³ von links unten nach rechts oben.)',
                                    'Welches Glied ist für große |x| entscheidend, und welches Vorzeichen braucht es?'))
    neu('randverhalten', 3, zahl('Eine ganzrationale Funktion vom Grad 4 verläuft von links oben nach rechts oben und hat f(0) = −1. Wie viele Nullstellen hat sie mindestens?',
                                 'Von links oben muss der Graph bis f(0) = −1 unter die x-Achse: eine Nullstelle links von 0. Danach muss er wieder nach oben: eine rechts von 0. Mindestens 2.',
                                 'Skizziere: Wo beginnt der Graph, wo ist er bei x = 0, wo endet er?', 2, '2'))
    neu('randverhalten', 3, auswahl('Was geschieht mit f(x) = −x⁶ + 100x⁵ für x → −∞ (x wird immer kleiner)?', 'f(x) wird beliebig klein (→ −∞).',
                                    ['f(x) wird beliebig groß (→ +∞).', 'f(x) nähert sich 0.', 'Das hängt vom Glied 100x⁵ ab.'],
                                    'Für große |x| überwiegt −x⁶ (gerader Grad, negativer Faktor) – auch wenn 100x⁵ für kleine x größer wirkt. Für x → −∞ gilt f(x) → −∞.',
                                    'Am Rand zählt nur die höchste Potenz – egal, wie groß die anderen Faktoren sind.'))

    # --- symmetrie ---
    neu('symmetrie', 2, auswahl('Welche Symmetrie hat der Graph von f(x) = (x − 1)² + (x + 1)²?', 'achsensymmetrisch zur y-Achse', ['punktsymmetrisch zum Ursprung', 'keine dieser Symmetrien'],
                                'Ausmultipliziert: x² − 2x + 1 + x² + 2x + 1 = 2x² + 2. Nur gerade Hochzahlen.', 'Erst ausmultiplizieren, dann die Hochzahlen ansehen.'))
    neu('symmetrie', 2, auswahl('Welche Symmetrie hat der Graph von f(x) = x · (x² − 4)?', 'punktsymmetrisch zum Ursprung', ['achsensymmetrisch zur y-Achse', 'keine dieser Symmetrien'],
                                'f(x) = x³ − 4x: nur ungerade Hochzahlen.', 'Multipliziere aus.'))
    neu('symmetrie', 3, zahl('Der Graph von f(x) = x⁴ − kx² hat bei x = 2 eine Nullstelle. Bestimme k.', 'f(2) = 16 − 4k = 0 ⇒ k = 4. Wegen der Achsensymmetrie ist dann auch x = −2 Nullstelle.',
                             'Setze x = 2 ein.', 4, '16 / 4'))
    neu('symmetrie', 3, luecken('Der Graph einer Funktion f ist punktsymmetrisch zum Ursprung und hat den Hochpunkt H(2 | 1). Welchen Tiefpunkt hat er sicher?', 'T(□ | □)', 'Koordinaten',
                                [-2, -1], 'Punktspiegelung am Ursprung: (2 | 1) → (−2 | −1). Aus dem Hochpunkt wird ein Tiefpunkt.', 'Was macht eine Punktspiegelung am Ursprung mit beiden Koordinaten?',
                                c=['-2', '-1']))
    neu('symmetrie', 3, zahl('Für welche Zahl a ist der Graph von f(x) = x³ + (a − 3)x² + x punktsymmetrisch zum Ursprung?',
                             'Nur ungerade Hochzahlen erlaubt: Das x²-Glied muss wegfallen, a − 3 = 0 ⇒ a = 3.', 'Welches Glied stört die Punktsymmetrie?', 3, '3'))
    neu('symmetrie', 3, auswahl('Jemand sagt: „f(x) = x³ + x² ist punktsymmetrisch zum Ursprung, weil der Grad ungerade ist.“ Was stimmt?',
                                'Falsch: x² ist eine gerade Hochzahl, f hat keine dieser Symmetrien.', ['Richtig.', 'Falsch: f ist achsensymmetrisch zur y-Achse.', 'Falsch: Symmetrie hängt nur vom Leitkoeffizienten ab.'],
                                'Es zählen alle Hochzahlen, nicht nur der Grad. Probe: f(1) = 2, f(−1) = 0 ≠ −2.', 'Prüfe mit x = 1 und x = −1.'))

    # --- nullstellen ---
    neu('nullstellen', 2, luecken('Bestimme die Nullstellen von f(x) = x⁴ − 4x².', 'x₁ = □; x₂ = □; x₃ = □', 'Nullstellen aufsteigend', [-2, 0, 2],
                                  'x²(x² − 4) = 0 ⇒ x = 0 (doppelt) oder x = ±2.', 'Klammere x² aus.', c=['-2 + (16 - 16)', '0', '2 + (16 - 16)']))
    neu('nullstellen', 2, zahl('f(x) = (x² − 1)(x + 1). Welche Vielfachheit hat die Nullstelle x = −1?', 'x² − 1 = (x − 1)(x + 1), also f(x) = (x − 1)(x + 1)². x = −1 ist doppelt.',
                               'Zerlege x² − 1 mit der dritten binomischen Formel.', 2, '2'))
    neu('nullstellen', 3, auswahl('Für welche x gilt f(x) < 0 bei f(x) = (x − 1) · x² · (x + 2)³?', 'für −2 < x < 1, außer x = 0', ['für x < −2 und x > 1', 'für −2 < x < 0', 'für 0 < x < 1'],
                                  'Vorzeichenwechsel nur bei −2 (dreifach) und 1 (einfach); bei 0 (doppelt) berührt der Graph. Grad 6, Leitkoeffizient positiv: außen positiv, zwischen −2 und 1 negativ – bei 0 ist f(0) = 0.',
                                  'Bestimme die Vielfachheiten und das Randverhalten, dann skizziere.'))
    neu('nullstellen', 3, zahl('Wie viele Nullstellen hat f(x) = x⁴ − 5x² + 4 im Bereich −1,5 < x < 1,5?', 'z = x²: z = 1 oder z = 4 ⇒ x = ±1 oder x = ±2. Im Bereich liegen nur −1 und 1.',
                               'Bestimme alle Nullstellen mit Substitution und prüfe, welche im Bereich liegen.', 2, '2'))
    neu('nullstellen', 3, zahl('Der Graph von f(x) = x³ − 3x + c berührt die x-Achse bei x = 1. Bestimme c.', 'f(1) = 1 − 3 + c = 0 ⇒ c = 2. Probe: x³ − 3x + 2 = (x − 1)²(x + 2) – doppelte Nullstelle bei 1.',
                               'Berühren heißt mindestens: f(1) = 0.', 2, '3 - 1'))
    neu('nullstellen', 3, auswahl('f(x) = x · (x − a)² hat genau zwei verschiedene Nullstellen. Was gilt für a?', 'a ≠ 0', ['a = 0', 'a > 0', 'für jede Zahl a'],
                                  'Nullstellen 0 und a. Verschieden sind sie nur für a ≠ 0; für a = 0 ist f(x) = x³ mit nur einer Nullstelle.', 'Welche Nullstellen hat f? Wann fallen sie zusammen?'))

    # --- graph_term ---
    kf = mal([-1, -2], [1, -1], [1, -1])  # −(x + 2)(x − 1)²
    neu('graph_term', 2, mit_grafik(auswahl('Welcher Funktionsterm gehört zum gezeichneten Graphen?', 'f(x) = −(x + 2) · (x − 1)²',
                                            ['f(x) = (x + 2) · (x − 1)²', 'f(x) = −(x + 2)² · (x − 1)', 'f(x) = −(x − 2) · (x + 1)²'],
                                            'Nullstellen −2 (Schnitt) und 1 (Berührung); Grad 3, von links oben nach rechts unten ⇒ Leitkoeffizient negativ.',
                                            'Schneiden oder berühren? Und wie verlaufen die Enden?'), graph_bild(kf, [-2, 1])))
    kf = mal([1, 0], [1, -2], [1, 2])
    neu('graph_term', 2, mit_grafik(auswahl('Welcher Funktionsterm gehört zum gezeichneten Graphen?', 'f(x) = x · (x − 2) · (x + 2)',
                                            ['f(x) = −x · (x − 2) · (x + 2)', 'f(x) = x² · (x − 2) · (x + 2)', 'f(x) = (x − 2) · (x + 2)'],
                                            'Drei einfache Nullstellen −2, 0, 2; Grad 3, von links unten nach rechts oben.', 'Zähle die Nullstellen und prüfe den Verlauf an den Enden.'),
                                    graph_bild(kf, [-2, 0, 2])))
    kf = [Fr(1, 2) * c for c in mal([1, 1], [1, 1], [1, -2])]
    neu('graph_term', 3, mit_grafik(auswahl('Welcher Funktionsterm gehört zum gezeichneten Graphen? Achte auch auf den Schnittpunkt mit der y-Achse.', 'f(x) = 0,5 · (x + 1)² · (x − 2)',
                                            ['f(x) = (x + 1)² · (x − 2)', 'f(x) = 2 · (x + 1)² · (x − 2)', 'f(x) = 0,5 · (x + 1) · (x − 2)²'],
                                            'Nullstellen −1 (Berührung) und 2 (Schnitt). Der Graph schneidet die y-Achse bei −1: f(0) = a · 1 · (−2) = −2a = −1 ⇒ a = 0,5.',
                                            'Die Nullstellen passen bei drei Termen. Entscheide mit f(0).'),
                                    graph_bild(kf, [-1, 2], punkte=[{'x': 0, 'y': -1}])))
    neu('graph_term', 3, auswahl('Ein Graph kommt von links oben, berührt die x-Achse bei x = −1, schneidet sie bei x = 2 und verläuft nach rechts unten. Welcher Term passt?',
                                 'f(x) = −(x + 1)² · (x − 2)', ['f(x) = (x + 1)² · (x − 2)', 'f(x) = −(x + 1) · (x − 2)²', 'f(x) = −(x − 1)² · (x + 2)'],
                                 'Berühren bei −1: (x + 1)². Schneiden bei 2: (x − 2). Grad 3, von links oben nach rechts unten: negativer Leitkoeffizient.',
                                 'Übersetze jede Eigenschaft in einen Teil des Terms.'))
    neu('graph_term', 3, luecken('f(x) = (x − 1)² · (x − 3). Der Graph von g(x) = f(x + 1) entsteht durch Verschieben. Bestimme die Nullstellen von g.', 'x₁ = □; x₂ = □',
                                 'Nullstellen aufsteigend', [0, 2], 'g(x) = (x + 1 − 1)² · (x + 1 − 3) = x² · (x − 2). Nullstellen 0 und 2: alles um 1 nach links verschoben.',
                                 'Setze x + 1 in f ein, oder überlege: In welche Richtung verschiebt f(x + 1)?', c=['0', '2']))
    neu('graph_term', 3, luecken('Der Graph von f(x) = a · x⁴ + b · x² ist achsensymmetrisch, hat den Leitkoeffizienten −1 und schneidet die x-Achse bei x = 2. Bestimme a und b.', 'a = □; b = □',
                                 'Zwei Zahlen', [-1, 4], 'a = −1. f(2) = −16 + 4b = 0 ⇒ b = 4. Also f(x) = −x⁴ + 4x² = −x²(x² − 4).',
                                 'Der Leitkoeffizient ist a. Setze dann x = 2 ein.', c=['-1', '16 / 4']))

    # --- term_bestimmen ---
    neu('term_bestimmen', 2, zahl('Eine Funktion 3. Grades mit Leitkoeffizient 1 hat die Nullstellen −1 (einfach) und 2 (doppelt). Berechne f(0).',
                                  'f(x) = (x + 1)(x − 2)². f(0) = 1 · (−2)² = 4.', 'Stelle zuerst die Produktform auf.', 4, '(0 + 1) * (0 - 2) ** 2'))
    neu('term_bestimmen', 2, zahl('f(x) = a · x · (x − 3) geht durch den Punkt (1 | 4). Bestimme a.', 'f(1) = a · 1 · (−2) = −2a = 4 ⇒ a = −2.', 'Setze den Punkt ein.', -2, '4 / (1 * (1 - 3))'))
    neu('term_bestimmen', 3, zahl('Der Graph einer Funktion 3. Grades berührt die x-Achse bei x = 2, schneidet sie bei x = −1 und geht durch (0 | 8). Bestimme a in f(x) = a · (x + 1) · (x − 2)².',
                                  'f(0) = a · 1 · 4 = 4a = 8 ⇒ a = 2.', 'Setze den Punkt (0 | 8) ein.', 2, '8 / ((0 + 1) * (0 - 2) ** 2)'))
    neu('term_bestimmen', 3, zahl('Ein Graph 4. Grades hat bei x = 1 und x = −1 je eine doppelte Nullstelle und geht durch (2 | 18). Bestimme a in f(x) = a · (x − 1)² · (x + 1)².',
                                  'f(2) = a · 1² · 3² = 9a = 18 ⇒ a = 2.', 'Setze x = 2 ein und rechne die Klammern aus.', 2, '18 / ((2 - 1) ** 2 * (2 + 1) ** 2)'))
    neu('term_bestimmen', 3, zahl('Die Parabel f(x) = a · (x − 1)(x − 4) hat ihren Scheitel auf der Höhe y = 9. Bestimme a.',
                                  'Der Scheitel liegt in der Mitte der Nullstellen: x = 2,5. f(2,5) = a · 1,5 · (−1,5) = −2,25a = 9 ⇒ a = −4.',
                                  'Wo liegt der Scheitel einer Parabel mit zwei Nullstellen?', -4, '9 / ((2.5 - 1) * (2.5 - 4))'))
    neu('term_bestimmen', 3, zahl('Ein Tunnel ist am Boden 8 m breit und in der Mitte 6 m hoch. Sein Querschnitt wird durch f(x) = a · (x + 4)(x − 4) beschrieben (x in m, Mitte bei x = 0). Bestimme a.',
                                  'f(0) = a · 4 · (−4) = −16a = 6 ⇒ a = −0,375.', 'Die Höhe in der Mitte ist f(0).', -0.375, '6 / (4 * (-4))'))
    return N


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('funktionen.ganzrational', 13_10_5)
# b) Lösungsweg: Kleinschreibung „zur y-achse“ / „zum ursprung“ (alle Pools)
BF.loesung('symmetrie', 'Für f(x) = −x⁶ + 4x⁴ + 3x² + 4 gilt f(3) = −374. Bestimme f(−3) mithilfe der Symmetrie.', pools=('uebung',), w='Achsensymmetrisch zur y-Achse: f(−x) = f(x), also f(−3) = −374.')
BF.loesung('symmetrie', 'Für f(x) = −x⁵ − 5x³ − 6x gilt f(3) = −396. Bestimme f(−3) mithilfe der Symmetrie.', pools=('uebung',), w='Punktsymmetrisch zum Ursprung: f(−x) = −f(x), also f(−3) = 396.')
BF.loesung('symmetrie', 'Für f(x) = −6x⁴ + 5x² − 3 gilt f(2) = −79. Bestimme f(−2) mithilfe der Symmetrie.', pools=('uebung',), w='Achsensymmetrisch zur y-Achse: f(−x) = f(x), also f(−2) = −79.')
BF.loesung('symmetrie', 'Für f(x) = 4x⁶ + 2x⁴ + 3x² + 2 gilt f(3) = 3 107. Bestimme f(−3) mithilfe der Symmetrie.', pools=('uebung',), w='Achsensymmetrisch zur y-Achse: f(−x) = f(x), also f(−3) = 3 107.')
BF.loesung('symmetrie', 'Für f(x) = 4x³ + 6x gilt f(1) = 10. Bestimme f(−1) mithilfe der Symmetrie.', pools=('uebung',), w='Punktsymmetrisch zum Ursprung: f(−x) = −f(x), also f(−1) = −10.')
BF.loesung('symmetrie', 'Für f(x) = −5x⁴ − 5x² − 4 gilt f(2) = −104. Bestimme f(−2) mithilfe der Symmetrie.', pools=('uebung',), w='Achsensymmetrisch zur y-Achse: f(−x) = f(x), also f(−2) = −104.')
# a) Grad 2 mit zwei einfachen Nullstellen ist leichter als die Stufe-2-Aufgaben (Grad 3/4 mit Berührung) – derselbe Typ wie Stufe 1
BF.stufe('graph_term', 'Welcher Funktionsterm gehört zum gezeichneten Graphen?', 1, enthaelt='f(x) = 2 · (x − 1)² · (x − 3)')
BF.stufe('graph_term', 'Welcher Funktionsterm gehört zum gezeichneten Graphen?', 1, enthaelt='f(x) = (x + 1)² · x')
BF.nicht_umgesetzt('randverhalten S1 mit Polynom 7. Grades und 8 Gliedern', 'Laut Befund inhaltlich richtig; nur das höchste Glied zählt, das ist der Lerninhalt der Karte.')

# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    datei = bauen('funktionen.ganzrational',
          'Ganzrationale Funktionen beschreiben: Grad und Koeffizienten, Randverhalten, Symmetrie, Nullstellen mit Vielfachheit; Graph und Term zuordnen und Terme aus Nullstellen bestimmen.',
          ['Grad = höchste Hochzahl, Leitkoeffizient = ihr Faktor, Absolutglied = f(0).', 'Randverhalten: nur das höchste Glied zählt.',
           'Nur gerade Hochzahlen: achsensymmetrisch; nur ungerade: punktsymmetrisch.', 'Ungerade Vielfachheit: Schnitt; gerade: Berührung.'],
          [('Aufbau', ['grad', 'ausmultiplizieren']), ('Eigenschaften', ['randverhalten', 'symmetrie', 'nullstellen']), ('Graph und Term', ['graph_term', 'term_bestimmen'])],
          ETAPPEN, GEN, klar=KLAR,
          meiden={'grad': ['−2x³ + 5x − 7.'], 'ausmultiplizieren': ['(x − 1) · (x + 2) · (x − 3)'], 'symmetrie': ['2x⁴ − x² + 3?'], 'nullstellen': ['x³ − 4x² + 4x']},
          offen=['Prüfung eingearbeitet (Runde 3): Produktform aus einer bekannten Nullstelle, Randverhalten am Graphen und in Produktform (Standardfrage höchstens 14-mal), Substitution mit nur zwei Lösungen, Vielfachheit am Graphen ablesen (nur ausmultiplizierte Form), Mehrzahl „An welchen Nullstellen …“.',
                 'Nicht umgesetzt: Hinweis der Prüfung zur Überschneidung von „nullstellen“ mit „vielfachheit“ in gleichungen.polynom. Beide Karten sind als „ok“ bewertet und blicken verschieden auf dasselbe (hier Graph, dort Gleichung); die Themen können unabhängig voneinander bearbeitet werden. Ein Verweis zwischen Themen ist Sache des Lehrplans (Reihenfolge), nicht der Karte.',
                 'Zeichnungen: Graphen in den Lernkarten „randverhalten“, „symmetrie“, „nullstellen“, „graph_term“, „term_bestimmen“; Aufgaben zu Berührung, „Welcher Term gehört zum Graphen?“ und „a aus Nullstellen und Punkt“ zeigen den Graphen.',
                 'Lückenaufgaben „Ausmultiplizieren“ nutzen die Term-Vorlage (z. B. „x³ + □x² + □x + □“): Das Kind tippt den Term frei ein; Koeffizienten können negativ sein.',
                 'Extrempunkte (Ableitung) sind nicht enthalten – das ist Stoff der Oberstufe.'])
    ergaenzen(datei, schwer())
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden
