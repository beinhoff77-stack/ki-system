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

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import ko, pkte, tab  # noqa: E402


def _l(m, t, name):
    return {'art': 'linear', 'm': m, 't': t, 'name': name}


_YX = _l(1, 0, 'y = x')
_PAR = {'art': 'poly', 'k': [0, 0, 1], 'name': 'y = x²'}
_F2 = {'art': 'poly', 'k': [5, -4, 1], 'name': 'f', 'bereich': [2, 4.4]}
_EXP = {'art': 'exp', 'a': 1, 'b': 2, 'name': 'y = 2ˣ'}
UMBAU = {
    'umkehrbar': {
        'einstieg': 'Eine Codiermaschine macht aus jeder Zahl eine Geheimzahl. Zum Entschlüsseln darf jede Geheimzahl nur einmal vorkommen. '
                    'Dann heißt die Maschine ⟦umkehrbar⟧.',
        'woerter': [['umkehrbar', 'jeder y-Wert kommt nur einmal vor; man kann eindeutig zurückrechnen'],
                    ['waagrechte Gerade', 'eine Linie quer durchs Bild, z. B. y = 4']],
        'bild': ko([-3, 3], [-1, 6], schritt=0, graphen=[_PAR]),
        'schritte': [
            {'text': 'Die Maschine y = x² macht aus 2 und aus −2 die 4.', 'bild': {'punkte': pkte({'(−2|4)': (-2, 4), '(2|4)': (2, 4)})}},
            {'text': 'Die waagrechte Gerade y = 4 trifft die Parabel zweimal.', 'bild': {'waagrecht': [4]}},
            {'text': 'Also ⟦nicht umkehrbar⟧: Aus 4 weiß man nicht, ob 2 oder −2.'},
            {'text': 'Nur mit x ≥ 0 bleibt ein Ast übrig, dann ist sie ⟦umkehrbar⟧.',
             'bild': {'graphen': [dict(_PAR, bereich=[0, 3])], 'punkte': pkte({'(2|4)': (2, 4)})}},
        ],
        'fehler': '„Zu jedem x gehört genau ein y“ reicht nicht, das gilt für jede Funktion. Für die Umkehrung braucht jedes y ⟦genau ein x⟧.',
        'regel': 'Umkehrbar heißt: Jeder y-Wert kommt nur einmal vor. Test: Jede ⟦waagrechte Gerade⟧ trifft den Graphen höchstens einmal.',
    },
    'werte': {
        'einstieg': 'Die Codiermaschine f macht aus 2 die Geheimzahl 5. Die Entschlüsselung macht aus 5 wieder 2. '
                    'Diese Rückwärts-Maschine heißt ⟦Umkehrfunktion⟧.',
        'woerter': [['Umkehrfunktion', 'rechnet rückwärts: aus f(a) = b wird f⁻¹(b) = a'],
                    ['f⁻¹', 'gelesen „f hoch minus eins“: die Umkehrfunktion, kein Kehrwert']],
        'bild': tab(['x', '0', '1', '2', '3'], ['f(x)', '1', '3', '5', '7']),
        'schritte': [
            {'text': 'Aus der Tabelle: f(2) = 5.'},
            {'text': 'Die Umkehrfunktion liest rückwärts: ⟦f⁻¹(5) = 2⟧.', 'bild': tab(['x', '1', '3', '5', '7'], ['f⁻¹(x)', '0', '1', '2', '3'])},
            {'text': 'Die beiden Zeilen tauschen also ihre Rollen.'},
        ],
        'fehler': 'f⁻¹(5) = 1/5 ist falsch. Das hochgestellte −1 heißt ⟦Umkehrfunktion⟧, nicht Kehrwert.',
        'regel': 'Ist f(a) = b, dann ist ⟦f⁻¹(b) = a⟧. Für f⁻¹ liest du die Tabelle von unten nach oben.',
    },
    'linear': {
        'einstieg': 'Die Maschine rechnet „mal 2, dann minus 6“. Rückwärts musst du alles umdrehen: erst plus 6, dann durch 2. '
                    'Rechnerisch klappt das mit einem Trick: ⟦x und y vertauschen⟧.',
        'woerter': [['nach y auflösen', 'umformen, bis y allein auf einer Seite steht']],
        'bild': ko([-7, 7], [-7, 7], schritt=0, graphen=[_l(2, -6, 'f')]),
        'schritte': [
            {'text': 'Aus y = 2x − 6 wird durch Tauschen x = 2y − 6.'},
            {'text': 'Nach y auflösen: 2y = x + 6, also ⟦y = 0,5x + 3⟧.', 'bild': {'graphen': [_l(2, -6, 'f'), _l(0.5, 3, 'f⁻¹')]}},
            {'text': 'Probe: f(4) = 2 und f⁻¹(2) = 4. Beide liegen spiegelbildlich zu y = x.',
             'bild': {'graphen': [_l(2, -6, 'f'), _l(0.5, 3, 'f⁻¹'), _YX], 'punkte': pkte({'(4|2)': (4, 2), '(2|4)': (2, 4)})}},
        ],
        'fehler': '0,5x − 6 ist falsch, nur die Steigung umzudrehen reicht nicht. Nach dem Tauschen ⟦vollständig nach y auflösen⟧.',
        'fehler_bild': {'graphen': [_l(2, -6, 'f'), _l(0.5, 3, 'f⁻¹'), _l(0.5, -6, 'falsch')], 'punkte': None},
        'regel': 'Umkehrfunktion: ⟦x und y vertauschen⟧, dann nach y auflösen. Bei f(x) = mx + t ist f⁻¹(x) = (x − t) : m.',
    },
    'quadratisch': {
        'einstieg': 'Quadrieren macht aus 3 die 9. Rückwärts zieht man die Wurzel: Aus 9 wird 3. '
                    'Damit das eindeutig klappt, nimmt man nur ⟦einen Ast⟧ der Parabel.',
        'woerter': [['Ast', 'eine Hälfte der Parabel, z. B. nur der Teil mit x ≥ 2']],
        'bild': ko([-1, 7], [-1, 7], schritt=0, graphen=[_F2]),
        'schritte': [
            {'text': 'f(x) = (x − 2)² + 1 mit x ≥ 2 ist ein Ast.'},
            {'text': 'Tauschen: x = (y − 2)² + 1.'},
            {'text': 'Minus 1: (y − 2)² = x − 1.'},
            {'text': 'Wurzel ziehen, plus 2: ⟦f⁻¹(x) = √(x − 1) + 2⟧.'},
            {'text': 'Probe: f(3) = 2 und f⁻¹(2) = √1 + 2 = 3.',
             'bild': {'graphen': [_F2, _YX], 'punkte': pkte({'(3|2)': (3, 2), '(2|3)': (2, 3)})}},
        ],
        'fehler': '√(x + 1) − 2 ist falsch. Beim Umkehren drehen sich die Rechenzeichen um: ⟦−1 unter der Wurzel⟧, +2 dahinter.',
        'regel': 'Eine Parabel nur auf ⟦einem Ast⟧ umkehren. Die Umkehrung von Quadrieren ist Wurzelziehen.',
    },
    'exp_log': {
        'einstieg': 'Ein Gerücht verdoppelt sich jede Stunde: Nach 5 Stunden kennen es 2⁵ = 32 Leute. '
                    'Rückwärts fragt man: Nach wie vielen Stunden sind es 32? Das sagt der ⟦Logarithmus⟧.',
        'woerter': [['Logarithmus', 'log₂ 32 ist die Hochzahl, mit der man 2 potenzieren muss, um 32 zu erhalten'],
                    ['lg', 'Logarithmus zur Basis 10']],
        'bild': ko([-1, 6], [-1, 35], schritt=0, schritt_y=5, graphen=[_EXP]),
        'schritte': [
            {'text': 'f(x) = 2ˣ: Nach 5 Stunden sind es 2⁵ = 32.', 'bild': {'punkte': pkte({'(5|32)': (5, 32)})}},
            {'text': 'Rückwärts: log₂ 32 = ⟦5⟧, denn 2⁵ = 32.', 'bild': {'strecken': [[0, 32, 5, 32, 'gestrichelt'], [5, 32, 5, 0, 'gestrichelt']]}},
            {'text': 'Für die Basis 10 schreibt man lg: lg 100 = 2.'},
        ],
        'fehler': 'log₂ 32 = 16 ist falsch. Der Logarithmus ist ⟦nicht 32 : 2⟧, sondern die Hochzahl: 2 hoch 5 ist 32.',
        'regel': 'Der ⟦Logarithmus⟧ ist die Umkehrung von bˣ. log_b x fragt: b hoch wie viel ergibt x?',
    },
    'spiegeln': {
        'einstieg': 'Legst du einen Spiegel auf die Linie y = x, siehst du darin die Umkehrfunktion. '
                    'x und y tauschen dabei ihre Plätze. Die Linie heißt ⟦Winkelhalbierende⟧.',
        'woerter': [['Winkelhalbierende', 'die Gerade y = x; sie halbiert den Winkel zwischen den Achsen']],
        'bild': ko([-3, 9], [-3, 9], schritt=0, graphen=[_EXP, _YX]),
        'schritte': [
            {'text': 'P(3 | 8) liegt auf y = 2ˣ.', 'bild': {'punkte': pkte({'P': (3, 8)})}},
            {'text': 'Spiegeln an der Winkelhalbierenden heißt: x und y tauschen.'},
            {'text': 'So entsteht ⟦P′(8 | 3)⟧ auf y = log₂ x.',
             'bild': {'graphen': [_EXP, _YX, {'art': 'log', 'b': 2, 'name': 'log₂ x'}], 'punkte': pkte({'P': (3, 8), 'P′': (8, 3)}),
                      'strecken': [[3, 8, 8, 3, 'gestrichelt']]}},
        ],
        'fehler': 'P′(−3 | −8) ist falsch, das wäre am ⟦Ursprung⟧ gespiegelt. An y = x werden die Koordinaten getauscht.',
        'regel': 'Graph von f⁻¹: an der ⟦Winkelhalbierenden y = x⟧ spiegeln. Aus P(a | b) wird P′(b | a).',
    },
}
UMBAU_OFFEN = ['Umbau (Paket UR): Den Graphen von √(x − 1) + 2 (Karte quadratisch) kann die App nicht zeichnen (Graph-Art wurzel nur als √x); '
               'die Karte zeigt stattdessen den Ast von f, die Gerade y = x und ein Punktepaar.']
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-1) ----------
# Prüfungsvorbilder: Realschul-Abschlussprüfung Mathematik I (Bayern), A 1.2 (2021): „Berechnen Sie die nach y aufgelöste Gleichung
# der Umkehrfunktion“, Definitions- und Wertemenge der Umkehrfunktion, Schnittpunkte mit den Achsen; IB-MYP-Formate zu inversen
# Funktionen (f(x) = f⁻¹(x), Werte rückwärts). Typ übernommen, Wortlaut und Zahlen eigen.
def durchsicht(d):
    from _rsib1 import Z, A, L, nachtrag, finde
    T = lambda teil: finde(d, teil)
    LT, HT = '□x + □', 'Tippe den Term ein, z. B. 2x − 4.'
    nachtrag(d,
        umstufen={
            T('f(x) = 4x + 6. Was ist f⁻¹(30)?'): 2,
            T('f(x) = 2x − 2. Was ist f⁻¹(4)?'): 2,
            T('Welche Funktion ist die Umkehrfunktion von f(x) = −0,25x − 1,5?'): 2,
            T('Welche Funktion ist die Umkehrfunktion von f(x) = 0,1x − 0,5?'): 2,
            T('P(2 | 100) liegt auf dem Graphen von y = 10ˣ.'): 2,
            T('P(2 | 9) liegt auf dem Graphen von y = 3ˣ.'): 2,
        },
        ersetzen={
            T('Auf welcher Menge ist f(x) = (x − 5)² umkehrbar?'):
                Z(3, 'f(x) = x² − 6x soll auf der Menge x ≥ a umkehrbar sein. Wie klein darf a höchstens sein?', 3, '6/2',
                  'Quadratische Ergänzung: x² − 6x = (x − 3)² − 9. Der Scheitel liegt bei x = 3. Rechts davon ist ein Ast: a = 3.',
                  'Wo liegt der Scheitel der Parabel?'),
            T('Auf welcher Menge ist f(x) = (x + 5)² umkehrbar?'):
                A(3, 'Welche Funktion ist auf ganz ℝ umkehrbar?', 'f(x) = x³', ['f(x) = x²', 'f(x) = x⁴', 'f(x) = 5'],
                  'x³ steigt überall, jeder y-Wert kommt einmal vor. Bei x² und x⁴ gehören 2 und −2 zum selben y; bei f(x) = 5 gehört jedes x zu 5.',
                  'Mache bei jeder Funktion den Test mit der waagrechten Geraden.'),
            T('Jemand gibt für f(x) = −0,25x + 1,25 die Umkehrfunktion'):
                Z(3, 'f(x) = m · x + 3 hat die Umkehrfunktion f⁻¹(x) = 0,5x − 1,5. Wie groß ist m?', 2, '1/0.5',
                  'Die Steigung der Umkehrfunktion ist 1 : m. 1 : m = 0,5 ⇒ m = 2. Probe: f(x) = 2x + 3, umgekehrt (x − 3) : 2 = 0,5x − 1,5.',
                  'Wie hängen die Steigungen von f und f⁻¹ zusammen?'),
            T('Jemand gibt für f(x) = 0,5x + 3,5 die Umkehrfunktion'):
                A(3, 'Welche Gerade ist ihre eigene Umkehrfunktion?', 'y = −x + 4', ['y = 2x', 'y = x + 1', 'y = 0,5x'],
                  'Tauschen bei y = −x + 4: x = −y + 4 ⇒ y = −x + 4. Gleich! Die Gerade steht senkrecht auf y = x.',
                  'Bilde zu jeder die Umkehrfunktion.'),
            T('Warum muss man bei f(x) = (x − 4)² + 2 die Definitionsmenge'):
                Z(3, 'f(x) = x² + 2 mit x ≥ 0. Für welches x ist f⁻¹(x) = 3?', 11, '3**2 + 2',
                  'f⁻¹(x) = 3 heißt f(3) = x. f(3) = 9 + 2 = 11.', 'Lies f⁻¹(x) = 3 rückwärts.'),
            T('Jemand spiegelt P(3 | −3) für die Umkehrfunktion zu P\'(−3 | 3).'):
                A(3, 'Der Graph von f geht durch (2 | 2) und (1 | 3). Welcher dieser Punkte liegt sicher auch auf dem Graphen von f⁻¹?', '(2 | 2)',
                  ['(1 | 3)', '(3 | 3)', 'keiner'],
                  'Punkte auf der Geraden y = x bleiben beim Spiegeln liegen: (2 | 2) wird zu (2 | 2). Aus (1 | 3) wird (3 | 1).',
                  'Was passiert beim Tauschen mit (2 | 2)?'),
        },
        neu={
            'umkehrbar': [
                A(3, 'Warum ist f(x) = 2 · 0,5ˣ + 1 (x ∈ ℝ) umkehrbar?', 'Weil der Graph überall fällt: Jeder y-Wert kommt nur einmal vor.',
                  ['Weil zu jedem x genau ein y gehört.', 'Weil der Graph die y-Achse bei 3 schneidet.', 'Weil 0,5 kleiner als 1 ist.'],
                  '0,5ˣ wird ständig kleiner, also auch 2 · 0,5ˣ + 1. Eine waagrechte Gerade trifft den Graphen höchstens einmal.',
                  'Steigt oder fällt der Graph überall?'),
                A(3, 'Eine Funktion hat nur die Werte f(1) = 3, f(2) = 5, f(3) = 3, f(4) = 7. Welchen x-Wert kann man streichen, damit sie umkehrbar wird?',
                  '1 oder 3', ['nur 2', 'nur 4', 'Man muss zwei Werte streichen.'],
                  'Der y-Wert 3 kommt zweimal vor (bei 1 und bei 3). Streicht man einen der beiden, kommt jeder y-Wert nur einmal vor.',
                  'Welcher y-Wert kommt doppelt vor?'),
            ],
            'werte': [
                Z(3, 'f(x) = 3x − 5. Für welches x gilt f(x) = f⁻¹(x)?', 2.5, '5/2',
                  'f und f⁻¹ treffen sich hier auf y = x: 3x − 5 = x ⇒ 2x = 5 ⇒ x = 2,5. Probe: f(2,5) = 2,5 und f⁻¹(2,5) = 2,5.',
                  'Wo schneidet f die Gerade y = x?'),
                Z(3, 'Für eine Funktion f gilt f(2) = 7 und f(7) = 2. Berechne f⁻¹(f⁻¹(2)).', 2, '2',
                  'f⁻¹(2) = 7, weil f(7) = 2. Dann f⁻¹(7) = 2, weil f(2) = 7.', 'Rechne von innen nach außen.'),
                L(3, 'Für eine Funktion f gilt f(3) = 5. Welcher Punkt liegt sicher auf dem Graphen von g(x) = f⁻¹(x) + 1?', 'P(□ | □)', [5, 4], ['5', '3 + 1'],
                  'f(3) = 5 ⇒ f⁻¹(5) = 3 ⇒ g(5) = 3 + 1 = 4. Also P(5 | 4).', 'Bestimme zuerst f⁻¹(5).'),
                A(3, 'f(x) = 0,5x + 2. Für welches x ist f⁻¹(x) doppelt so groß wie x?', 'für kein x', ['für x = 4', 'für x = 2', 'für jedes x'],
                  'f⁻¹(x) = 2x − 4. Gleichung 2x − 4 = 2x ⇒ −4 = 0: unmöglich. Es gibt kein solches x.',
                  'Bestimme zuerst f⁻¹ und stelle die Gleichung auf.'),
            ],
            'linear': [
                L(3, 'f(x) = 2x − 3. In welchem Punkt schneiden sich die Graphen von f und f⁻¹?', 'S(□ | □)', [3, 3], ['3', '3'],
                  'Gerade und Umkehrgerade schneiden sich auf y = x: 2x − 3 = x ⇒ x = 3. S(3 | 3).', 'Der Schnittpunkt liegt auf der Spiegelachse.'),
                L(3, 'Die Gerade f geht durch die Punkte (2 | 2) und (4 | 3). Gib die Umkehrfunktion an.', LT, [2, -2], ['2', '-2'],
                  'f⁻¹ geht durch (2 | 2) und (3 | 4): Steigung (4 − 2) : (3 − 2) = 2, f⁻¹(x) = 2x − 2.', 'Tausche die Koordinaten beider Punkte.', hinweis=HT),
                Z(3, 'Eine Gerade f hat die Steigung 4. Welche Steigung hat ihre Umkehrfunktion?', 0.25, '1/4',
                  'Beim Tauschen von x und y wird aus „4 nach oben pro 1 nach rechts“ „1 nach oben pro 4 nach rechts“: 1 : 4 = 0,25.',
                  'Was passiert mit dem Steigungsdreieck beim Spiegeln?'),
                Z(3, 'Für welches t geht der Graph der Umkehrfunktion von f(x) = 2x + t durch den Punkt (5 | 1)?', 3, '5 - 2*1',
                  '(5 | 1) auf f⁻¹ heißt (1 | 5) auf f: 2 · 1 + t = 5 ⇒ t = 3.', 'Welcher Punkt liegt dann auf f?'),
            ],
            'quadratisch': [
                L(3, 'f(x) = (x − 3)² + 1 mit x ≥ 3. Gib die Wertemenge der Umkehrfunktion f⁻¹ an.', 'W = {y | y ≥ □}', [3], ['3'],
                  'Die Wertemenge von f⁻¹ ist die Definitionsmenge von f: x ≥ 3.', 'Was tauschen f und f⁻¹ außer x und y noch?'),
                A(3, 'f(x) = x² mit x ≤ 0 (linker Ast). Welche Funktion ist die Umkehrfunktion?', 'f⁻¹(x) = −√x', ['f⁻¹(x) = √x', 'f⁻¹(x) = √(−x)', 'f⁻¹(x) = −x²'],
                  'Der linke Ast hat negative x-Werte. Die Umkehrung muss also negative Werte liefern: −√x. Probe: f(−3) = 9, −√9 = −3.',
                  'Welches Vorzeichen haben die x-Werte des linken Asts?'),
            ],
            'exp_log': [
                Z(3, 'f(x) = 2ˣ⁻¹. Berechne f⁻¹(16).', 5, '4 + 1', '2ˣ⁻¹ = 16 = 2⁴ ⇒ x − 1 = 4 ⇒ x = 5.', 'Schreibe 16 als Zweierpotenz.'),
                Z(3, 'f(x) = 3 · 2ˣ. Berechne f⁻¹(24).', 3, '3', '3 · 2ˣ = 24 ⇒ 2ˣ = 8 ⇒ x = 3.', 'Teile zuerst durch 3.'),
                A(3, 'f(x) = 2ˣ. Warum hat f⁻¹(−4) keinen Wert?', 'Weil 2ˣ nie negativ wird.', ['Weil man durch 0 teilen müsste.', 'Weil −4 keine Zweierpotenz ist, aber 4 schon.', 'Doch: f⁻¹(−4) = −2.'],
                  '2ˣ ist für jedes x positiv. Es gibt kein x mit 2ˣ = −4. Die Definitionsmenge von log₂ sind nur positive Zahlen.',
                  'Welche Werte kann 2ˣ annehmen?'),
                Z(3, 'Berechne lg 0,001.', -3, '-3', '10⁻³ = 1/1 000 = 0,001. Also lg 0,001 = −3.', '10 hoch wie viel ergibt 0,001?'),
            ],
            'spiegeln': [
                L(3, 'Der Graph von f ist eine Gerade durch (0 | 1) mit der Steigung 2. Wo schneidet der Graph von f⁻¹ die x-Achse?', 'N(□ | □)', [1, 0], ['1', '0'],
                  'f schneidet die y-Achse in (0 | 1). Gespiegelt: f⁻¹ schneidet die x-Achse in (1 | 0).', 'Spiegle den Schnittpunkt von f mit der y-Achse.'),
                L(3, 'f(x) = 3ˣ + 1. Wo schneidet der Graph von f⁻¹ die x-Achse?', 'N(□ | □)', [2, 0], ['3**0 + 1', '0'],
                  'f(0) = 1 + 1 = 2, also liegt (0 | 2) auf f. Gespiegelt: (2 | 0) auf f⁻¹.', 'Berechne zuerst f(0).'),
                L(3, 'Der Graph von f schneidet die x-Achse bei x = −4. Wo schneidet der Graph von f⁻¹ die y-Achse?', 'S(□ | □)', [0, -4], ['0', '-4'],
                  '(−4 | 0) liegt auf f. Gespiegelt: (0 | −4) auf f⁻¹.', 'Tausche die Koordinaten des Nullstellenpunkts.'),
            ],
        })


if __name__ == '__main__':
    d = bauen('funktionen.umkehr',
          'Entscheiden, ob eine Funktion umkehrbar ist, Umkehrfunktionen bestimmen (Gerade, Parabelast, Exponentialfunktion) und den Graphen an y = x spiegeln.',
          ['Umkehrbar: Jeder y-Wert kommt nur einmal vor (waagrechte Gerade schneidet höchstens einmal).',
           'f(a) = b ⇔ f⁻¹(b) = a. D und W tauschen.', 'f⁻¹ bestimmen: x und y tauschen, nach y auflösen.',
           'Umkehrung von bˣ ist log_b x; von x² (x ≥ 0) ist √x.', 'Graph von f⁻¹: Spiegelung an y = x, P(a | b) ↦ P\'(b | a).'],
          [('Umkehrbarkeit', ['umkehrbar', 'werte']), ('Umkehrfunktionen bestimmen', ['linear', 'quadratisch', 'exp_log']), ('Graphen', ['spiegeln'])],
          ETAPPEN, GEN,
          offen=['Lehrplan-Feld leer: Annahme RS 10 (WPF I) – Umkehrbarkeit, Umkehrfunktion linearer Funktionen, eines Parabelastes und der Exponentialfunktion (Logarithmus), Spiegelung an y = x. Umkehrung gebrochen-rationaler Funktionen weggelassen.'])
    umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
    durchsicht(d)
