#!/usr/bin/env python3
"""Thema funktionen.umkehr – Umkehrfunktionen (Realschule Bayern Klasse 10, IB MYP 4)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _rs import *  # noqa: E402,F403

start(7701)
LT, HT = '□x + □', 'Tippe den Term ein, z. B. 2x − 3.'
LP, HP = "P'(□ | □)", 'x-Koordinate, y-Koordinate'
TIEF = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')


def nz(n):
    return R.choice([i for i in range(-n, n + 1) if i != 0])


def lg(b):
    return 'lg' if b == 10 else f'log{str(b).translate(TIEF)}'


def koord(gs, x=(-5, 5), y=(-5, 5), extra=None):
    b = {'typ': 'koordinaten', 'x': list(x), 'y': list(y), 'graphen': gs}
    if extra: b.update(extra)
    return b


ETAPPEN = [
    {'lernziel': 'umkehrbar', 'titel': 'Ist eine Funktion umkehrbar?',
     'regel': 'Eine Funktion ist ⟦umkehrbar⟧, wenn ⟦jeder y-Wert nur einmal⟧ vorkommt – dann kann man vom y-Wert eindeutig auf den x-Wert zurückschließen. Am Graphen: Jede ⟦waagrechte Gerade⟧ schneidet ihn ⟦höchstens einmal⟧. Wie ein Schlüssel, der nur zu einer Tür passt.',
     'bild': koord([{'art': 'poly', 'k': [0, 0, 1], 'name': 'y = x²'}], (-3, 3), (-1, 6), {'waagrecht': [4]}),
     'schritte': ['y = x² auf ganz ℝ: Die Gerade y = 4 schneidet die Parabel zweimal (x = −2 und x = 2).',
                  'Also ⟦nicht umkehrbar⟧. Schränkt man auf ⟦x ≥ 0⟧ ein, bleibt nur ein Ast – dann ist sie umkehrbar.'],
     'fehler': '„y = x² ist umkehrbar, weil zu jedem x genau ein y gehört“ ist falsch: Das gilt für ⟦jede Funktion⟧. Für die Umkehrung muss auch zu jedem y ⟦genau ein x⟧ gehören.'},
    {'lernziel': 'werte', 'titel': 'Werte der Umkehrfunktion',
     'regel': 'Die ⟦Umkehrfunktion f⁻¹⟧ macht f rückgängig: Ist ⟦f(a) = b⟧, dann ist ⟦f⁻¹(b) = a⟧. Definitionsmenge und Wertemenge ⟦tauschen⟧ die Rollen. Wie ein Wörterbuch Deutsch–Englisch und Englisch–Deutsch.',
     'bild': {'typ': 'tabelle', 'kopf': ['x', '0', '1', '2', '3'], 'zeilen': [['f(x)', '1', '3', '5', '7']]},
     'schritte': ['Aus der Tabelle: f(2) = 5.', 'Also ⟦f⁻¹(5) = 2⟧. Für f⁻¹ lies die Tabelle ⟦von unten nach oben⟧.'],
     'fehler': 'f⁻¹(5) = 1/5 ist falsch: Das hochgestellte −1 bedeutet ⟦Umkehrfunktion⟧, nicht „Kehrwert“.'},
    {'lernziel': 'linear', 'titel': 'Umkehrfunktion einer Geraden',
     'regel': 'So findest du f⁻¹: ⟦x und y vertauschen⟧, dann ⟦nach y auflösen⟧. Bei f(x) = m · x + t (m ≠ 0) erhältst du ⟦f⁻¹(x) = (x − t) : m⟧.',
     'schritte': ['f(x) = 2x − 6: y = 2x − 6. Tauschen: x = 2y − 6.', 'Auflösen: 2y = x + 6 ⇒ ⟦y = 0,5x + 3⟧. Also f⁻¹(x) = 0,5x + 3.'],
     'probe': 'f(4) = 2 und f⁻¹(2) = 1 + 3 = 4 ✓',
     'fehler': 'f⁻¹(x) = 0,5x − 6 ist falsch: Nur die Steigung umzudrehen reicht nicht. Nach dem Tauschen muss man ⟦vollständig nach y auflösen⟧: f⁻¹(x) = 0,5x + 3.'},
    {'lernziel': 'quadratisch', 'titel': 'Umkehrfunktion einer Parabel',
     'regel': 'Eine Parabel ist nur auf ⟦einem Ast⟧ umkehrbar, z. B. für x ≥ d. Für f(x) = (x − d)² + e mit x ≥ d gilt: ⟦f⁻¹(x) = √(x − e) + d⟧ mit x ≥ e. Die Umkehrung von „quadrieren“ ist „⟦Wurzel ziehen⟧“.',
     'bild': koord([{'art': 'poly', 'k': [0, 0, 1], 'name': 'y = x²', 'bereich': [0, 3]}, {'art': 'wurzel', 'name': 'y = √x'},
                    {'art': 'linear', 'm': 1, 't': 0, 'name': 'y = x'}], (-1, 6), (-1, 6)),
     'schritte': ['f(x) = (x − 2)² + 1, x ≥ 2. Tauschen: x = (y − 2)² + 1 ⇒ (y − 2)² = x − 1.',
                  'Wurzel (positiver Ast, weil y ≥ 2): y − 2 = √(x − 1) ⇒ ⟦f⁻¹(x) = √(x − 1) + 2⟧, x ≥ 1.'],
     'probe': 'f(5) = 9 + 1 = 10; f⁻¹(10) = √9 + 2 = 5 ✓',
     'fehler': 'f⁻¹(x) = √(x + 1) − 2 ist falsch: Beim Umkehren drehen sich die Rechenzeichen um: aus „+1“ wird ⟦„−1“ unter der Wurzel⟧, aus „−2“ wird ⟦„+2“⟧ dahinter.'},
    {'lernziel': 'exp_log', 'titel': 'Exponential- und Logarithmusfunktion',
     'regel': 'Die Umkehrfunktion von ⟦f(x) = bˣ⟧ ist die ⟦Logarithmusfunktion f⁻¹(x) = log_b x⟧ (für x > 0): ⟦log_b x ist der Exponent⟧, mit dem man b potenzieren muss, um x zu erhalten. Für b = 10 schreibt man ⟦lg x⟧.',
     'schritte': ['f(x) = 2ˣ: f(5) = 32.', 'Also f⁻¹(32) = log₂ 32 = ⟦5⟧, denn 2⁵ = 32.'],
     'probe': '2⁵ = 2 · 2 · 2 · 2 · 2 = 32 ✓',
     'fehler': 'log₂ 32 = 16 ist falsch: Der Logarithmus ist ⟦nicht 32 : 2⟧, sondern der ⟦Exponent⟧ – 2 hoch wie viel ergibt 32? Also 5.'},
    {'lernziel': 'spiegeln', 'titel': 'Graph der Umkehrfunktion',
     'regel': 'Den Graphen von f⁻¹ erhältst du, indem du den Graphen von f an der ⟦Winkelhalbierenden y = x⟧ spiegelst. Jeder Punkt ⟦P(a | b)⟧ wird zu ⟦P\'(b | a)⟧ – x und y tauschen.',
     'bild': koord([{'art': 'exp', 'a': 1, 'b': 2, 'name': 'y = 2ˣ'}, {'art': 'log', 'b': 2, 'name': 'y = log₂ x'},
                    {'art': 'linear', 'm': 1, 't': 0, 'name': 'y = x'}], (-3, 6), (-3, 6)),
     'schritte': ['P(3 | 8) liegt auf y = 2ˣ.', 'Gespiegelt an y = x: ⟦P\'(8 | 3)⟧ liegt auf y = log₂ x.'],
     'fehler': 'P(3 | 8) zu P\'(−3 | −8) zu spiegeln ist falsch: Das ist die Spiegelung am ⟦Ursprung⟧. An y = x werden die Koordinaten ⟦vertauscht⟧.'},
]


# ---------- Generatoren ----------
FUNKTIONEN = [
    ('f(x) = 3x − 1 (x ∈ ℝ)', True, 'Steigung ≠ 0: Die Gerade steigt überall, jeder y-Wert kommt einmal vor.'),
    ('f(x) = −0,5x + 4 (x ∈ ℝ)', True, 'Steigung ≠ 0: Die Gerade fällt überall, jeder y-Wert kommt einmal vor.'),
    ('f(x) = 5 (x ∈ ℝ)', False, 'Konstante Funktion: Der y-Wert 5 gehört zu allen x.'),
    ('f(x) = x² (x ∈ ℝ)', False, 'f(−2) = f(2) = 4: Ein y-Wert gehört zu zwei x-Werten.'),
    ('f(x) = x² (x ≥ 0)', True, 'Nur der rechte Ast: Die Funktion steigt, jeder y-Wert kommt einmal vor.'),
    ('f(x) = (x − 1)² (x ≤ 1)', True, 'Nur der linke Ast: Die Funktion fällt, jeder y-Wert kommt einmal vor.'),
    ('f(x) = (x + 3)² − 2 (x ∈ ℝ)', False, 'Eine ganze Parabel: Links und rechts vom Scheitel kommen gleiche y-Werte vor.'),
    ('f(x) = 2ˣ (x ∈ ℝ)', True, 'Die Exponentialfunktion steigt überall.'),
    ('f(x) = 0,5ˣ (x ∈ ℝ)', True, 'Die Exponentialfunktion fällt überall.'),
    ('f(x) = x³ (x ∈ ℝ)', True, 'x³ steigt überall: Jeder y-Wert kommt genau einmal vor.'),
    ('f(x) = x⁴ (x ∈ ℝ)', False, 'f(−1) = f(1) = 1: gleiche y-Werte für verschiedene x.'),
    ('f(x) = lg x (x > 0)', True, 'Die Logarithmusfunktion steigt überall.'),
]


def g_umkehrbar(s):
    if s == 1:
        txt, ja, w = R.choice(FUNKTIONEN)
        return auswahl(f'Ist {txt} umkehrbar?', 'Ja' if ja else 'Nein', ['Nein' if ja else 'Ja', 'Das hängt vom x-Wert ab.'], w,
                       'Kommt ein y-Wert mehrmals vor?')
    if s == 2:
        if R.random() < 0.5:
            xs = [R.randint(-4, 4) for _ in range(5)]
            xs = sorted(set(xs))
            if len(xs) < 4: return None
            ys = [R.randint(-5, 9) for _ in xs]
            ja = len(set(ys)) == len(ys)
            tab = {'typ': 'tabelle', 'kopf': ['x'] + [dz(x) for x in xs], 'zeilen': [['f(x)'] + [dz(y) for y in ys]]}
            doppelt = [y for y in ys if ys.count(y) > 1]
            a = auswahl('Die Tabelle zeigt alle Werte einer Funktion f. Ist f umkehrbar?', 'Ja' if ja else 'Nein',
                        ['Nein' if ja else 'Ja', 'Das kann man an einer Tabelle nicht erkennen.'],
                        'Alle y-Werte sind verschieden, also umkehrbar.' if ja else f'Der y-Wert {dz(doppelt[0])} kommt mehrmals vor, also nicht umkehrbar.',
                        'Kommt in der unteren Zeile eine Zahl doppelt vor?')
            return bild(a, tab)
        d, e = nz(3), R.randint(-2, 3)
        a = auswahl('Ist die gezeichnete Funktion (auf ganz ℝ) umkehrbar?', 'Nein, eine waagrechte Gerade schneidet den Graphen zweimal.',
                    ['Ja, der Graph ist eine durchgehende Linie.', 'Ja, weil zu jedem x genau ein y gehört.', 'Nein, weil der Graph die y-Achse schneidet.'],
                    f'Parabel mit Scheitel S({dz(d)} | {dz(e)}): Links und rechts vom Scheitel gibt es gleiche y-Werte.',
                    'Leg in Gedanken ein Lineal waagrecht über den Graphen.')
        return bild(a, koord([{'art': 'poly', 'k': [d * d + e, -2 * d, 1]}], (d - 3, d + 3), (e - 1, e + 8)))
    art = R.random()
    if art < 0.5:
        d = nz(5)
        return auswahl(f'Auf welcher Menge ist f(x) = {minus_klammer(d)}² umkehrbar?', f'x ≥ {dz(d)}',
                       [f'x ≥ {dz(-d)}', 'x ≥ 0', 'auf ganz ℝ'],
                       f'Der Scheitel liegt bei x = {dz(d)}. Rechts davon (x ≥ {dz(d)}) steigt die Parabel nur – dort ist sie umkehrbar (links davon ebenfalls, x ≤ {dz(d)}).',
                       'Wo liegt der Scheitel? Nimm nur einen Ast.')
    txt, ja, w = R.choice(FUNKTIONEN)
    return auswahl(f'Jemand behauptet: „{txt} ist umkehrbar, weil zu jedem x genau ein y gehört.“ Was stimmt?',
                   ('Ergebnis stimmt, Begründung nicht: Es kommt darauf an, dass jeder y-Wert nur einmal vorkommt.' if ja else
                    'Falsch: Es kommt darauf an, dass jeder y-Wert nur einmal vorkommt – das ist hier nicht so.'),
                   ['Richtig, genau so begründet man es.', 'Falsch: Keine Funktion ist umkehrbar.', 'Falsch: Umkehrbar sind nur Geraden.'],
                   w + ' Dass zu jedem x genau ein y gehört, gilt für jede Funktion.', 'Was muss für die Umkehrung eindeutig sein?')


def g_werte(s):
    m, t = nz(4), nz(8)
    if s == 1:
        xs = list(range(R.randint(-3, 0), R.randint(-3, 0) + 5))
        ys = [m * x + t for x in xs]
        i = R.randrange(len(xs))
        tab = {'typ': 'tabelle', 'kopf': ['x'] + [dz(x) for x in xs], 'zeilen': [['f(x)'] + [dz(y) for y in ys]]}
        a = zahl(f'Lies aus der Tabelle ab: f⁻¹({dz(ys[i])}) = ?', f'f({dz(xs[i])}) = {dz(ys[i])}, also f⁻¹({dz(ys[i])}) = {dz(xs[i])}.',
                 'Suche den Wert in der unteren Zeile und lies darüber ab.', xs[i], str(xs[i]))
        return bild(a, tab)
    x0 = nz(8)
    b = m * x0 + t
    if s == 2:
        if R.random() < 0.6:
            return zahl(f'f(x) = {poly(m, t)}. Berechne f⁻¹({dz(b)}).', f'f⁻¹({dz(b)}) ist das x mit f(x) = {dz(b)}: {poly(m, t)} = {dz(b)} ⇒ x = {dz(x0)}.',
                        'Gesucht ist das x, für das f(x) diesen Wert hat.', x0, f'(({b}) - ({t})) / ({m})')
        lo, hi = sorted([R.randint(-4, 0), R.randint(1, 5)])
        ylo, yhi = sorted([m * lo + t, m * hi + t])
        return luecken(f'f(x) = {poly(m, t)} hat die Definitionsmenge D = [{dz(lo)}; {dz(hi)}]. Gib die Definitionsmenge von f⁻¹ an.', 'D = [□; □]',
                       'kleinere Grenze zuerst', [ylo, yhi], f'D von f⁻¹ = Wertemenge von f: f({dz(lo)}) = {dz(m * lo + t)}, f({dz(hi)}) = {dz(m * hi + t)}. D = [{dz(ylo)}; {dz(yhi)}].',
                       'D und W tauschen die Rollen.', c=[f'min({m * lo + t}, {m * hi + t})', f'max({m * lo + t}, {m * hi + t})'])
    art = R.random()
    if art < 0.35:
        return auswahl(f'f(x) = {poly(m, t)}. Was ist f⁻¹({dz(b)})?', dz(x0),
                       [br(Fr(1, b)) if b else '0', dz(m * b + t), dz(-x0)],
                       f'f({dz(x0)}) = {dz(b)}, also f⁻¹({dz(b)}) = {dz(x0)}. f⁻¹ ist nicht der Kehrwert und nicht f noch einmal.',
                       'f⁻¹(b) ist das x mit f(x) = b.')
    if art < 0.7:
        return zahl(f'f(x) = {poly(m, t)}. Berechne f⁻¹(f({dz(x0)})).', f'f⁻¹ macht f rückgängig: f⁻¹(f({dz(x0)})) = {dz(x0)}.',
                    'Was passiert, wenn man etwas tut und es gleich wieder rückgängig macht?', x0, str(x0))
    return luecken(f'f hat die Wertemenge W = [{dz(min(b, t))}; {dz(max(b, t) + 1)}] und die Definitionsmenge D = [{dz(x0 - 3)}; {dz(x0 + 2)}]. Gib die Wertemenge von f⁻¹ an.',
                   'W = [□; □]', 'kleinere Grenze zuerst', [x0 - 3, x0 + 2],
                   f'W von f⁻¹ = D von f = [{dz(x0 - 3)}; {dz(x0 + 2)}].', 'Was wird beim Umkehren aus der Definitionsmenge?', c=[str(x0 - 3), str(x0 + 2)])


INV_M = [1, -1, 2, -2, 4, -4, 5, -5, 10]


def g_linear(s):
    p, q = R.choice(INV_M), nz(8)          # f⁻¹(x) = p·x + q
    m, t = Fr(1, p), Fr(-q, p)              # f(x) = m·x + t
    if s == 1:
        p = R.choice([1, 2, -2, 2, -1])
        q = R.choice([v for v in range(-8, 9) if v != 0 and v % p == 0])
        m, t = Fr(1, p), Fr(-q, p)
    w = f'y = {poly(m, t)}. Tauschen: x = {poly(m, t).replace("x", "y")}. Auflösen: y = {poly(p, q)}.'
    if s in (1, 2):
        return luecken(f'Bestimme die Umkehrfunktion von f(x) = {poly(m, t)}. f⁻¹(x) = ?', LT, HT, [p, q], w,
                       'x und y tauschen, dann nach y auflösen.', c=[str(p), str(q)])
    art = R.random()
    if art < 0.4:
        falsch1 = poly(p, t)
        falsch2 = poly(m, -t) if m != p else poly(p, -q)
        falsch3 = poly(-p, q)
        return auswahl(f'Welche Funktion ist die Umkehrfunktion von f(x) = {poly(m, t)}?', f'f⁻¹(x) = {poly(p, q)}',
                       [f'f⁻¹(x) = {falsch1}', f'f⁻¹(x) = {falsch2}', f'f⁻¹(x) = {falsch3}'], w,
                       'Probe: Setze einen Wert in f ein und das Ergebnis in f⁻¹.')
    if art < 0.7:
        x0 = nz(5)
        y0 = m * x0 + t
        return auswahl(f'Jemand gibt für f(x) = {poly(m, t)} die Umkehrfunktion g(x) = {poly(p, t)} an. Prüfe mit x = {dz(x0)}.',
                       f'Falsch: f({dz(x0)}) = {dz(y0)}, aber g({dz(y0)}) = {dz(p * y0 + t)} ≠ {dz(x0)}.',
                       ['Richtig, g macht f rückgängig.', f'Falsch: Richtig wäre g(x) = {poly(-p, -t)}.', 'Man kann das nicht mit einem Zahlenwert prüfen.'],
                       w + f' Probe mit der richtigen Funktion: f⁻¹({dz(y0)}) = {dz(x0)} ✓.', 'Erst f anwenden, dann g. Kommt der Startwert heraus?') \
            if p * y0 + t != x0 and endlich(y0) else None
    # Schnittpunkt von f und f⁻¹ auf y = x
    if m == 1: return None
    xs = t / (1 - m)
    if not endlich(xs) or xs.denominator != 1: return None
    return luecken(f'Die Graphen von f(x) = {poly(m, t)} und f⁻¹ schneiden sich auf der Geraden y = x. Berechne den Schnittpunkt.', 'S(□ | □)', 'x, y',
                   [xs, xs], f'Auf y = x: {poly(m, t)} = x ⇒ x = {dz(xs)}. S({dz(xs)} | {dz(xs)}).',
                   'Setze f(x) = x.', c=[f'{cz(t)} / (1 - {cz(m)})', f'{cz(t)} / (1 - {cz(m)})'])


def g_quadratisch(s):
    if s == 1:
        r = R.randint(1, 15)
        if R.random() < 0.5:
            return zahl(f'f(x) = x² mit x ≥ 0. Berechne f⁻¹({r * r}).', f'f⁻¹(x) = √x, also f⁻¹({r * r}) = √{r * r} = {r}.',
                        'Die Umkehrung von Quadrieren ist Wurzelziehen.', r, f'{r * r} / {r}')
        return auswahl('Welche Funktion ist die Umkehrfunktion von f(x) = x² mit x ≥ 0?', 'f⁻¹(x) = √x (x ≥ 0)',
                       ['f⁻¹(x) = 1/x²', 'f⁻¹(x) = −x²', 'f⁻¹(x) = x : 2'], 'Quadrieren wird durch Wurzelziehen rückgängig gemacht.',
                       'Was macht Quadrieren rückgängig?') if R.random() < 0.4 else \
            zahl(f'f(x) = x² mit x ≥ 0. Berechne f⁻¹({r * r}).', f'f⁻¹({r * r}) = √{r * r} = {r}.', 'Wurzel ziehen.', r, f'{r * r} / {r}')
    d, e = nz(5), nz(6)
    r = R.randint(1, 9)
    x0 = d + r
    y0 = r * r + e
    ftxt = f'f(x) = {minus_klammer(d)}² {plus(e)} mit x ≥ {dz(d)}'
    if s == 2:
        if R.random() < 0.5:
            return zahl(f'{ftxt}. Berechne f⁻¹({dz(y0)}).', f'{minus_klammer(d)}² {plus(e)} = {dz(y0)} ⇒ {minus_klammer(d)}² = {r * r} ⇒ x {plus(-d)} = {r} (x ≥ {dz(d)}) ⇒ x = {dz(x0)}.',
                        'Löse f(x) = Wert; nimm nur die Lösung mit x ≥ d.', x0, f'({d}) + {r * r} / {r}')
        return auswahl(f'Welche Funktion ist die Umkehrfunktion von {ftxt}?', f'f⁻¹(x) = √(x {plus(-e)}) {plus(d)}',
                       [f'f⁻¹(x) = √(x {plus(e)}) {plus(-d)}', f'f⁻¹(x) = √(x {plus(-d)}) {plus(e)}', f'f⁻¹(x) = (x {plus(-e)})² {plus(d)}'],
                       f'Tauschen: x = (y {plus(-d)})² {plus(e)} ⇒ (y {plus(-d)})² = x {plus(-e)} ⇒ y = √(x {plus(-e)}) {plus(d)}.',
                       'Rechenschritte rückwärts mit umgekehrten Rechenzeichen.')
    art = R.random()
    if art < 0.35:
        return luecken(f'Gib die Definitionsmenge der Umkehrfunktion von {ftxt} an.', 'D = {x | x ≥ □}', 'Grenze als Zahl', [e],
                       f'Die Wertemenge von f ist y ≥ {dz(e)} (Scheitel S({dz(d)} | {dz(e)})). Sie wird zur Definitionsmenge von f⁻¹: x ≥ {dz(e)}.',
                       'Welche y-Werte erreicht f? Die werden zu den x-Werten von f⁻¹.', c=[str(e)])
    if art < 0.7:
        return luecken(f'Der Punkt P({dz(x0)} | {dz(y0)}) liegt auf dem Graphen von {ftxt}. Welcher Punkt liegt dann auf dem Graphen von f⁻¹?', LP, HP,
                       [y0, x0], f"x und y tauschen: P'({dz(y0)} | {dz(x0)}).", 'Spiegelung an y = x.', c=[str(y0), str(x0)])
    return auswahl(f'Warum muss man bei f(x) = {minus_klammer(d)}² {plus(e)} die Definitionsmenge auf x ≥ {dz(d)} einschränken, um f⁻¹ zu bilden?',
                   'Sonst gehören zu einem y-Wert zwei x-Werte.', ['Weil man aus negativen Zahlen keine Wurzel ziehen kann.', 'Weil f sonst keine Funktion wäre.', 'Weil die Parabel sonst keinen Scheitel hat.'],
                   f'Ohne Einschränkung ist z. B. f({dz(d - r)}) = f({dz(d + r)}) = {dz(y0)}. Mit x ≥ {dz(d)} bleibt nur ein Ast.',
                   'Was ist die Bedingung für Umkehrbarkeit?')


def g_exp_log(s):
    b = R.choice([2, 3, 5, 10])
    n = R.randint(1, {2: 8, 3: 5, 5: 4, 10: 5}[b])
    v = b ** n
    if s == 1:
        return zahl(f'f(x) = {b}ˣ. Berechne f⁻¹({dz(v)}) = {lg(b)} {dz(v)}.', f'{b} hoch wie viel ergibt {dz(v)}? {b}^{n} = {dz(v)}, also {lg(b)} {dz(v)} = {n}.'.replace(f'{b}^{n}', f'{b}{str(n).translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))}'),
                    'Gesucht ist der Exponent.', n, f'{n}')
    if s == 2:
        art = R.random()
        if art < 0.4:
            return auswahl(f'Welche Funktion ist die Umkehrfunktion von f(x) = {b}ˣ?', f'f⁻¹(x) = {lg(b)} x', [f'f⁻¹(x) = x^{b}'.replace(f'^{b}', str(b).translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))), f'f⁻¹(x) = (1/{b})ˣ', f'f⁻¹(x) = x : {b}'],
                           f'Die Umkehrung des Potenzierens mit Basis {b} ist der Logarithmus zur Basis {b}.', 'Was liefert den Exponenten?')
        k = nz(4)
        return zahl(f'f(x) = {b}ˣ {plus(k)}. Berechne f⁻¹({dz(v + k)}).', f'{b}ˣ {plus(k)} = {dz(v + k)} ⇒ {b}ˣ = {dz(v)} ⇒ x = {lg(b)} {dz(v)} = {n}.',
                    'Erst die Zahl wegbringen, dann den Exponenten bestimmen.', n, str(n))
    art = R.random()
    if art < 0.35:
        k = nz(4)
        return auswahl(f'Welche Funktion ist die Umkehrfunktion von f(x) = {b}ˣ {plus(k)}?', f'f⁻¹(x) = {lg(b)} (x {plus(-k)})',
                       [f'f⁻¹(x) = {lg(b)} (x {plus(k)})', f'f⁻¹(x) = {lg(b)} x {plus(-k)}', f'f⁻¹(x) = {lg(b)} x {plus(k)}'],
                       f'Tauschen: x = {b}ʸ {plus(k)} ⇒ {b}ʸ = x {plus(-k)} ⇒ y = {lg(b)} (x {plus(-k)}).', 'x und y tauschen, dann den Exponenten freistellen.')
    if art < 0.7:
        return auswahl(f'Jemand rechnet {lg(b)} {dz(v)} = {dz(Fr(v, b))}. Was stimmt?', f'Falsch: {lg(b)} {dz(v)} = {n}, denn {b} hoch {n} ergibt {dz(v)}.',
                       ['Richtig.', f'Falsch: {lg(b)} {dz(v)} = {dz(v * b)}.', f'Falsch: {lg(b)} {dz(v)} = {dz(v - b)}.'],
                       f'Der Logarithmus ist der Exponent: {b} hoch {n} = {dz(v)}. Teilen durch {b} ist falsch.', 'Ist der Logarithmus ein Quotient oder ein Exponent?')
    return luecken(f'P({n} | {dz(v)}) liegt auf dem Graphen von y = {b}ˣ. Welcher Punkt liegt auf dem Graphen von y = {lg(b)} x?', LP, HP, [v, n],
                   f"x und y tauschen: P'({dz(v)} | {n}). Probe: {lg(b)} {dz(v)} = {n} ✓.", 'Umkehrfunktion: Koordinaten tauschen.', c=[str(v), str(n)])


def g_spiegeln(s):
    a, b = nz(8), nz(8)
    if s == 1:
        return luecken(f'P({dz(a)} | {dz(b)}) liegt auf dem Graphen von f. Welcher Punkt liegt auf dem Graphen von f⁻¹?', LP, HP, [b, a],
                       f"An y = x spiegeln heißt Koordinaten tauschen: P'({dz(b)} | {dz(a)}).", 'x und y vertauschen.', c=[str(b), str(a)])
    if s == 2:
        if R.random() < 0.5:
            return auswahl(f'P({dz(a)} | {dz(b)}) wird an der Geraden y = x gespiegelt. Wo liegt der Bildpunkt?', f"P'({dz(b)} | {dz(a)})",
                           [f"P'({dz(-a)} | {dz(-b)})", f"P'({dz(-b)} | {dz(-a)})", f"P'({dz(a)} | {dz(-b)})"],
                           'An y = x werden x- und y-Koordinate vertauscht.', 'Welche Spiegelung tauscht die Koordinaten?')
        m, t = R.choice([2, 3, Fr(1, 2), -2, -1]), nz(3)
        if m == -1 and t != 0:
            return auswahl(f'Welche besondere Eigenschaft hat f(x) = −x {plus(t)} bezüglich der Umkehrfunktion?', 'f ist ihre eigene Umkehrfunktion.',
                           ['f hat keine Umkehrfunktion.', f'Die Umkehrfunktion ist f⁻¹(x) = x {plus(-t)}.', f'Die Umkehrfunktion ist f⁻¹(x) = −x {plus(-t)}.'],
                           f'Tauschen: x = −y {plus(t)} ⇒ y = −x {plus(t)}. Der Graph steht senkrecht auf y = x und ist zu ihr symmetrisch.',
                           'Bestimme f⁻¹ und vergleiche mit f.')
        x0 = nz(3)
        y0 = m * x0 + t
        if not endlich(y0): return None
        a_ = luecken(f'Der Punkt P({dz(x0)} | {dz(y0)}) liegt auf der gezeichneten Geraden f. Welcher Punkt liegt auf f⁻¹?', LP, HP, [y0, x0],
                     f"Koordinaten tauschen: P'({dz(y0)} | {dz(x0)}).", 'Spiegelung an y = x.', c=[cz(y0), str(x0)]) if Fr(y0).denominator == 1 else None
        if a_ is None: return None
        return bild(a_, koord([{'art': 'linear', 'm': float(m), 't': t, 'name': 'f'}, {'art': 'linear', 'm': 1, 't': 0, 'name': 'y = x'}], (-7, 7), (-7, 7),
                              {'punkte': [{'x': x0, 'y': float(y0), 'name': 'P'}]}))
    art = R.random()
    if art < 0.35:
        return auswahl(f'Der Graph von f geht durch P({dz(a)} | {dz(b)}) und Q({dz(b)} | {dz(a + 1)}). Durch welchen Punkt geht der Graph von f⁻¹ sicher?',
                       f'({dz(a + 1)} | {dz(b)})', [f'({dz(-a)} | {dz(-b)})', f'({dz(b)} | {dz(a + 1)})', f'({dz(a)} | {dz(b)})'],
                       f"Q({dz(b)} | {dz(a + 1)}) liegt auf f, also liegt ({dz(a + 1)} | {dz(b)}) auf f⁻¹. Ebenso ({dz(b)} | {dz(a)}) aus P.",
                       'Jeden Punkt von f mit vertauschten Koordinaten.') if a + 1 != b and a != b else None
    if art < 0.7:
        return auswahl('Welche Gerade ist die Symmetrieachse zwischen dem Graphen von f und dem Graphen von f⁻¹?', 'y = x',
                       ['die x-Achse', 'die y-Achse', 'y = −x'], 'Die Graphen von f und f⁻¹ liegen spiegelbildlich zur Winkelhalbierenden y = x.',
                       'Welche Gerade tauscht x und y?') if R.random() < 0.3 else \
            auswahl(f'Jemand spiegelt P({dz(a)} | {dz(b)}) für die Umkehrfunktion zu P\'({dz(-a)} | {dz(-b)}). Was stimmt?', f"Falsch: Richtig ist P'({dz(b)} | {dz(a)}).",
                    ['Richtig.', f"Falsch: Richtig ist P'({dz(-b)} | {dz(-a)}).", f"Falsch: Richtig ist P'({dz(a)} | {dz(-b)})."],
                    'Für die Umkehrfunktion wird an y = x gespiegelt: Koordinaten tauschen. P(a | b) ↦ (−a | −b) wäre die Punktspiegelung am Ursprung.',
                    'Welche Spiegelung gehört zur Umkehrfunktion?')
    n = R.randint(1, 5)
    bb = R.choice([2, 3])
    return luecken(f'Der Graph von y = {lg(bb)} x geht durch einen Punkt mit der y-Koordinate {n}. Welcher Punkt ist das?', 'P(□ | □)', 'x, y',
                   [bb ** n, n], f'{lg(bb)} x = {n} ⇔ x = {bb}^{n} = {bb ** n}. P({bb ** n} | {n}).'.replace(f'{bb}^{n}', f'{bb}{str(n).translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))}'),
                   'Der Logarithmus ist der Exponent: Basis hoch y = x.', c=[f'{bb} ** {n}', str(n)])


GEN = {'umkehrbar': g_umkehrbar, 'werte': g_werte, 'linear': g_linear, 'quadratisch': g_quadratisch, 'exp_log': g_exp_log, 'spiegeln': g_spiegeln}

if __name__ == '__main__':
    bauen('funktionen.umkehr',
          'Entscheiden, ob eine Funktion umkehrbar ist, Umkehrfunktionen bestimmen (Gerade, Parabelast, Exponentialfunktion) und den Graphen an y = x spiegeln.',
          ['Umkehrbar: Jeder y-Wert kommt nur einmal vor (waagrechte Gerade schneidet höchstens einmal).',
           'f(a) = b ⇔ f⁻¹(b) = a. D und W tauschen.', 'f⁻¹ bestimmen: x und y tauschen, nach y auflösen.',
           'Umkehrung von bˣ ist log_b x; von x² (x ≥ 0) ist √x.', 'Graph von f⁻¹: Spiegelung an y = x, P(a | b) ↦ P\'(b | a).'],
          [('Umkehrbarkeit', ['umkehrbar', 'werte']), ('Umkehrfunktionen bestimmen', ['linear', 'quadratisch', 'exp_log']), ('Graphen', ['spiegeln'])],
          ETAPPEN, GEN,
          offen=['Lehrplan-Feld leer: Annahme RS 10 (WPF I) – Umkehrbarkeit, Umkehrfunktion linearer Funktionen, eines Parabelastes und der Exponentialfunktion (Logarithmus), Spiegelung an y = x. Umkehrung gebrochen-rationaler Funktionen weggelassen.'])
