#!/usr/bin/env python3
"""Thema funktionen.potenz – Potenzfunktionen (Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(908)
H = HOCHZ


def nz(n):
    return R.choice([i for i in range(-n, n + 1) if i != 0])


def xn(n):
    if n < 0: return 'x⁻' + str(-n).translate(H)
    return 'x' if n == 1 else f'x{str(n).translate(H)}'


def fa(a, n):
    """a·xⁿ als Text"""
    af = '' if a == 1 else '−' if a == -1 else dz(a)
    return f'{af}{xn(n)}'


ETAPPEN = [
    {'lernziel': 'werte', 'titel': 'Funktionswerte von a · xⁿ',
     'regel': 'Bei f(x) = a · xⁿ zuerst ⟦potenzieren⟧, dann mit a multiplizieren. Negative x-Werte in ⟦Klammern⟧ einsetzen: Gerade Potenz → positiv, ungerade → negativ.',
     'schritte': ['f(x) = −2x³, gesucht f(−3): (−3)³ = −27.', 'f(−3) = −2 · (−27) = ⟦54⟧.'],
     'probe': 'Vorzeichen: − mal − ergibt + ✓',
     'fehler': 'Erst −2 · (−3) = 6 und dann 6³ = 216 zu rechnen ist falsch: ⟦Potenz vor Punkt⟧. Richtig: (−3)³ = −27, dann −2 · (−27) = 54.'},
    {'lernziel': 'symmetrie', 'titel': 'Symmetrie erkennen',
     'regel': 'n gerade: Graph ⟦achsensymmetrisch zur y-Achse⟧, f(−x) = f(x). n ungerade: ⟦punktsymmetrisch zum Ursprung⟧, f(−x) = −f(x).',
     'schritte': ['f(x) = 0,5x⁴: n = 4 gerade, also achsensymmetrisch.', 'Aus f(2) = 8 folgt ohne Rechnen ⟦f(−2) = 8⟧.'],
     'probe': '0,5 · (−2)⁴ = 0,5 · 16 = 8 ✓',
     'bild': {'typ': 'koordinaten', 'x': [-3, 3], 'y': [-2, 10], 'graphen': [{'art': 'potenz', 'a': 0.5, 'n': 4, 'name': 'f'}], 'punkte': [{'x': 2, 'y': 8, 'name': '(2 | 8)'}, {'x': -2, 'y': 8, 'name': '(−2 | 8)'}]},
     'fehler': '„y = x³ ist achsensymmetrisch zur y-Achse“ ist falsch: (−2)³ = −8, aber 2³ = 8. Bei ⟦ungeradem⟧ n ist der Graph punktsymmetrisch.'},
    {'lernziel': 'verlauf', 'titel': 'Verlauf und gemeinsame Punkte',
     'regel': 'y = xⁿ verläuft für ⟦n gerade⟧ von links oben nach rechts oben und durch (−1 | 1), (0 | 0), (1 | 1); für ⟦n ungerade⟧ von links unten nach rechts oben und durch (−1 | −1), (0 | 0), (1 | 1). ⟦a < 0⟧ spiegelt an der x-Achse.',
     'schritte': ['y = −x⁵: n = 5 ungerade, also y = x⁵ von links unten nach rechts oben.', 'a = −1 spiegelt an der x-Achse: ⟦von links oben nach rechts unten⟧.'],
     'probe': 'x = 2: −32 (unten), x = −2: 32 (oben) ✓',
     'bild': {'typ': 'koordinaten', 'x': [-2, 2], 'y': [-3, 3], 'graphen': [{'art': 'potenz', 'a': 1, 'n': 2, 'name': 'x²'}, {'art': 'potenz', 'a': 1, 'n': 3, 'name': 'x³'}, {'art': 'potenz', 'a': 1, 'n': 4, 'name': 'x⁴'}], 'punkte': [{'x': -1, 'y': 1}, {'x': 1, 'y': 1}, {'x': -1, 'y': -1}, {'x': 0, 'y': 0}]},
     'fehler': '„Alle Potenzfunktionen y = xⁿ gehen durch (−1 | 1)“ ist falsch: Für ungerades n ist (−1)ⁿ = ⟦−1⟧.'},
    {'lernziel': 'parameter', 'titel': 'a oder n aus einem Punkt bestimmen',
     'regel': 'Liegt P(u | v) auf y = a · xⁿ, gilt ⟦v = a · uⁿ⟧. Ist n bekannt, teilst du durch uⁿ. Ist a = 1, suchst du die ⟦Hochzahl⟧ mit uⁿ = v.',
     'schritte': ['y = a · x³ geht durch P(2 | −24): −24 = a · 8.', 'a = −24 : 8 = ⟦−3⟧, also y = −3x³.'],
     'probe': '−3 · 2³ = −24 ✓',
     'fehler': '−24 = a · 2³ ⇒ a = −24 : 6 ist falsch: 2³ = 2 · 2 · 2 = ⟦8⟧, nicht 2 · 3.'},
    {'lernziel': 'negativ', 'titel': 'Potenzfunktionen mit x⁻ⁿ',
     'regel': '⟦y = x⁻ⁿ = 1/xⁿ⟧ ist für ⟦x ≠ 0⟧ definiert. Die Achsen sind Asymptoten. n gerade: achsensymmetrisch, n ungerade: punktsymmetrisch.',
     'schritte': ['f(x) = x⁻², gesucht f(4): f(4) = 1/4².', 'f(4) = 1/16 = ⟦0,0625⟧.'],
     'probe': '0,0625 · 16 = 1 ✓',
     'bild': {'typ': 'koordinaten', 'x': [-4, 4], 'y': [-4, 4], 'graphen': [{'art': 'potenz', 'a': 1, 'n': -2, 'name': 'x⁻²'}, {'art': 'potenz', 'a': 1, 'n': -1, 'name': 'x⁻¹'}]},
     'fehler': 'f(4) = 4⁻² = −16 ist falsch: Ein negativer Exponent bedeutet ⟦Kehrwert⟧, nicht negatives Ergebnis: 4⁻² = 1/16.'},
    {'lernziel': 'wurzelfunktion', 'titel': 'Wurzelfunktionen und Umkehrung',
     'regel': 'y = x^(1/2) = √x und y = x^(1/3) = ∛x sind für ⟦x ≥ 0⟧ definiert. Sie sind die ⟦Umkehrfunktionen⟧ von y = x² bzw. y = x³ (für x ≥ 0): Aus y wird x zurückgerechnet. Im Bild: Der Graph von √x ist der Graph von x², ⟦gespiegelt an der Geraden y = x⟧ – x und y tauschen die Rollen.',
     'bild': {'typ': 'koordinaten', 'x': [0, 4], 'y': [0, 4], 'graphen': [{'art': 'potenz', 'a': 1, 'n': 2, 'name': 'x²', 'bereich': [0, 2]}, {'art': 'wurzel', 'name': '√x'}], 'strecken': [[0, 0, 4, 4, 'gestrichelt']], 'punkte': [{'x': 2, 'y': 4, 'name': '(2 | 4)'}, {'x': 4, 'y': 2, 'name': '(4 | 2)'}]},
     'schritte': ['f(x) = x³ (x ≥ 0). Für welches x ist f(x) = 64?', 'Umkehrung: x = ∛64 = ⟦4⟧.'],
     'probe': '4³ = 64 ✓',
     'fehler': '„√x ist für alle x definiert“ ist falsch: √(−4) gibt es nicht. Die Wurzelfunktion hat die ⟦Definitionsmenge x ≥ 0⟧.'},
]


def kos(graphen, x=(-3, 3), y=(-4, 4), **extra):
    g = {'typ': 'koordinaten', 'x': list(x), 'y': list(y), 'graphen': graphen}
    g.update(extra)
    return g


def g_werte(s):
    if s == 3 and R.random() < 0.35:
        if R.random() < 0.5:
            n = R.choice([4, 6])
            u = R.choice([2, 3]) if n == 4 else 2
            v = -(u ** n)
            return auswahl(f'f(x) = −{xn(n)}. Jemand rechnet f(−{u}) = (−(−{u})){str(n).translate(H)} = {dz(u ** n)}. Was stimmt?',
                           f'Falsch: f(−{u}) = −(−{u}){str(n).translate(H)} = {dz(v)}.',
                           ['Richtig.', f'Falsch: f(−{u}) = {dz(-u * n)}.', f'Falsch: f(−{u}) = {dz(u * n)}.'],
                           f'Erst potenzieren: (−{u}){str(n).translate(H)} = {dz(u ** n)}, dann das Minus davor: {dz(v)}.',
                           'Was wird zuerst gerechnet: die Potenz oder das Minus davor?')
        a, n, u = R.choice([-2, -3, -4]), 3, R.choice([-2, -3])
        v = a * u ** n
        return auswahl(f'Berechne f({dz(u)}) für f(x) = {fa(a, n)}.', dz(v),
                       [dz(-v), dz((a * u) ** n), dz(a * u * n)],
                       f'({dz(u)})³ = {dz(u ** 3)}; f({dz(u)}) = {dz(a)} · ({dz(u ** 3)}) = {dz(v)}.',
                       'Potenz vor Punkt: Erst (−x)³, dann mit a multiplizieren.')
    if s == 1:
        n, a, u = R.randint(2, 4), R.randint(1, 5), R.randint(1, 4)
    elif s == 2:
        n, a, u = R.randint(2, 5), nz(5), nz(3)
    else:
        if R.random() < 0.6:
            n = R.randint(2, 5)
            a = R.choice([2, 4, 8, -2, -4, 3])
            u = Fr(R.choice([-5, -1, 1, 3, 5]), 10) if n < 4 else Fr(R.choice([-1, 1]), 2)
            if R.random() < 0.4: u = Fr(R.choice([-1, 1]), 4)
        else:
            n, a, u = R.choice([3, 5]), R.choice([-1, -2, -3]), R.choice([-3, -2])
            if n == 5: u = -2
    v = a * Fr(u) ** n
    return zahl(f'Berechne f({dz(u)}) für f(x) = {fa(a, n)}.', f'{kl(u)}{str(n).translate(H)} = {dz(Fr(u) ** n)}; f({dz(u)}) = {dz(a)} · {kl(Fr(u) ** n)} = {dz(v)}.',
                'Erst potenzieren, dann mit a multiplizieren. Klammern um negative Zahlen!', v, f'({a}) * ({float(u) if not isinstance(u, int) else u}) ** {n}')


SYM = ['achsensymmetrisch zur y-Achse', 'punktsymmetrisch zum Ursprung', 'keine dieser Symmetrien']


def g_symmetrie(s):
    n = R.randint(2, 9)
    a = nz(5)
    if s == 1:
        r = SYM[0] if n % 2 == 0 else SYM[1]
        return auswahl(f'Welche Symmetrie hat der Graph von y = {fa(a, n)}?', r, SYM,
                       f'n = {n} ist {"gerade" if n % 2 == 0 else "ungerade"}, also {r}.', 'Ist der Exponent gerade oder ungerade?')
    u = R.randint(1, 3)
    v = a * u ** n
    if s == 2:
        if R.random() < 0.5:
            n = R.randint(2, 5)
            a = R.choice([Fr(1, 2), 1, -1, 2, Fr(-1, 2)])
            r = SYM[0] if n % 2 == 0 else SYM[1]
            return bild(auswahl('Welche Symmetrie hat der gezeigte Graph?', r, SYM,
                                f'Der Graph gehört zu y = {fa(a, n)}. ' + ('Die linke Hälfte ist das Spiegelbild der rechten an der y-Achse.' if n % 2 == 0 else
                                                                          'Dreht man den Graphen um 180° um den Ursprung, liegt er wieder auf sich selbst.'),
                                'Klappe das Bild an der y-Achse oder drehe es um den Ursprung.'),
                        kos([{'art': 'potenz', 'a': wert(Fr(a)), 'n': n}], y=(-5, 5)))
        g = v if n % 2 == 0 else -v
        return zahl(f'Für f(x) = a · {xn(n)} gilt f({u}) = {dz(v)}. Bestimme f(−{u}) ohne a zu berechnen.',
                    f'n = {n} {"gerade: f(−x) = f(x)" if n % 2 == 0 else "ungerade: f(−x) = −f(x)"}, also f(−{u}) = {dz(g)}.',
                    'Nutze die Symmetrie des Graphen.', g, f'({v}) * (-1) ** {n}')
    typ = R.random()
    if typ < 0.35:
        m = R.randint(1, 4) * 2 + 1
        return auswahl(f'Jemand behauptet: „y = {fa(a, m)} ist achsensymmetrisch zur y-Achse, weil {fa(a, m)} für x = 1 und x = −1 gleich groß ist.“ Was stimmt?',
                       f'Falsch: f(1) = {dz(a)}, f(−1) = {dz(-a)}; der Graph ist punktsymmetrisch.',
                       ['Richtig, das ist die Bedingung für Achsensymmetrie.', 'Falsch: Der Graph ist zu keiner Achse und keinem Punkt symmetrisch.',
                        'Richtig, alle Potenzfunktionen sind achsensymmetrisch.'],
                       f'f(−1) = {dz(a)} · (−1){str(m).translate(H)} = {dz(-a)} ≠ {dz(a)} = f(1). Ungerader Exponent: punktsymmetrisch zum Ursprung.',
                       'Rechne f(1) und f(−1) wirklich aus.')
    if typ < 0.7:
        n1, n2 = R.sample(range(1, 8), 2)
        if n1 < n2: n1, n2 = n2, n1
        term = f'{xn(n1)} {"+" if R.random() < 0.5 else "−"} {xn(n2)}'
        if n1 % 2 == 0 and n2 % 2 == 0: r = SYM[0]
        elif n1 % 2 == 1 and n2 % 2 == 1: r = SYM[1]
        else: r = SYM[2]
        sig = -1 if '−' in term else 1
        f1, fm1 = 1 + sig, (-1) ** n1 + sig * (-1) ** n2
        return auswahl(f'Welche Symmetrie hat der Graph von y = {term}?', r, SYM,
                       f'{"Beide Exponenten gerade" if r == SYM[0] else "Beide Exponenten ungerade" if r == SYM[1] else "Ein gerader und ein ungerader Exponent"}: {r}. Probe: f(1) = {dz(f1)}, f(−1) = {dz(fm1)}.',
                       'Untersuche jeden Summanden: Sind alle Exponenten gerade, alle ungerade oder gemischt?')
    n1, n2 = R.sample(range(2, 9), 2)
    if n1 % 2 == n2 % 2: return None
    g = n1 if n1 % 2 == 0 else n2
    return auswahl(f'Welcher Graph ist achsensymmetrisch zur y-Achse: y = {xn(n1)} + 1 oder y = {xn(n2)} + 1?', f'y = {xn(g)} + 1',
                   [f'y = {xn(n1 + n2 - g)} + 1', 'beide', 'keiner'],
                   f'Bei y = {xn(g)} + 1 ist der Exponent gerade; die Verschiebung um 1 nach oben ändert die Achsensymmetrie nicht.',
                   'Eine Verschiebung nach oben erhält die Achsensymmetrie zur y-Achse.')


VERL = {(0, 1): 'von links oben nach rechts oben', (0, -1): 'von links unten nach rechts unten',
        (1, 1): 'von links unten nach rechts oben', (1, -1): 'von links oben nach rechts unten'}


def g_verlauf(s):
    n = R.randint(2, 9)
    a = R.choice([1, -1]) if s == 1 else nz(6)
    if s == 1 or (s == 2 and R.random() < 0.5):
        r = VERL[(n % 2, 1 if a > 0 else -1)]
        return auswahl(f'Wie verläuft der Graph von y = {fa(a, n)}?', r, list(VERL.values()),
                       f'n = {n} {"gerade" if n % 2 == 0 else "ungerade"}, a {"> 0" if a > 0 else "< 0"}: {r}.',
                       'Was passiert für große positive und große negative x-Werte?')
    if s == 2 or R.random() < 0.25:
        while True:
            fs = [(R.choice([1, -1]), R.randint(2, 5)) for _ in range(3)]
            if len(set(fs)) == 3 and len({VERL[(n_ % 2, a_)] for a_, n_ in fs}) >= 2: break
        namen = ['g', 'h', 'k']
        k = R.randrange(3)
        a, n = fs[k]
        return bild(auswahl(f'Welcher Graph gehört zu y = {fa(a, n)}?', f'Graph {namen[k]}', [f'Graph {x}' for x in namen],
                            f'y = {fa(a, n)}: n = {n} {"gerade" if n % 2 == 0 else "ungerade"}, a {"> 0" if a > 0 else "< 0"}, also {VERL[(n % 2, a)]}; durch (1 | {dz(a)}) und (−1 | {dz(a * (-1) ** n)}).',
                            'Prüfe den Verlauf und die Punkte bei x = 1 und x = −1.'),
                    kos([{'art': 'potenz', 'a': fs[i][0], 'n': fs[i][1], 'name': namen[i]} for i in range(3)], x=(-2, 2), y=(-4, 4)))
    typ = R.random()
    if typ < 0.3:
        p = R.choice(['(−1 | 1)', '(−1 | −1)'])
        ger = p == '(−1 | 1)'
        r = 'alle mit geradem n' if ger else 'alle mit ungeradem n'
        m = R.randint(2, 9)
        return auswahl(f'Welche Graphen der Form y = xⁿ (n natürlich, n ≥ 2) gehen durch {p}? Denke z. B. an n = {m}.', r,
                       ['alle mit geradem n', 'alle mit ungeradem n', 'alle', 'keiner'],
                       f'(−1)ⁿ ist 1 für gerades n und −1 für ungerades n. Also gehen {r.replace("alle mit", "die Graphen mit")} durch {p}.',
                       'Berechne (−1)ⁿ für ein gerades und ein ungerades n.')
    n1, n2 = R.sample(range(2, 8), 2)
    lo, hi = min(n1, n2), max(n1, n2)
    if typ < 0.65:
        u = Fr(1, 2)
        if R.random() < 0.5:
            return auswahl(f'Welcher Graph liegt für 0 < x < 1 weiter oben: y = {xn(n1)} oder y = {xn(n2)}?', f'y = {xn(lo)}',
                           [f'y = {xn(hi)}', 'beide gleich', 'Das hängt von x ab.'],
                           f'Zwischen 0 und 1 wird die Zahl beim Potenzieren kleiner, z. B. 0,5{str(lo).translate(H)} = {dz(u ** lo)} > 0,5{str(hi).translate(H)} = {dz(u ** hi)}.',
                           'Setze probeweise x = 0,5 ein.')
        return auswahl(f'Für x = 0,5: Ist x{str(n1).translate(H)} oder x{str(n2).translate(H)} größer?', f'x{str(lo).translate(H)}',
                       [f'x{str(hi).translate(H)}', 'beide gleich groß', 'Das kann man nicht sagen.'],
                       f'0,5{str(lo).translate(H)} = {dz(u ** lo)} und 0,5{str(hi).translate(H)} = {dz(u ** hi)}: Mit jedem weiteren Faktor 0,5 wird die Zahl kleiner.',
                       'Rechne beide Werte aus.')
    return auswahl(f'Welcher Graph liegt für x > 1 weiter oben: y = {xn(n1)} oder y = {xn(n2)}?', f'y = {xn(hi)}',
                   [f'y = {xn(lo)}', 'beide gleich', 'Das hängt von x ab.'],
                   f'Für x > 1 wird die Zahl mit jedem weiteren Faktor größer, z. B. 2{str(hi).translate(H)} = {dz(2 ** hi)} > 2{str(lo).translate(H)} = {dz(2 ** lo)}.',
                   'Setze probeweise x = 2 ein.')


def g_parameter(s):
    if s == 1:
        n, a, u = R.randint(2, 3), nz(6), R.choice([1, 2, 3, -1, -2])
        v = a * u ** n
        return zahl(f'y = a · {xn(n)} geht durch P({dz(u)} | {dz(v)}). Bestimme a.', f'{dz(v)} = a · {kl(u)}{str(n).translate(H)} = {"" if u ** n == 1 else "−" if u ** n == -1 else dz(u ** n)}a ⇒ a = {dz(a)}.',
                    'Setze den Punkt ein und teile durch die Potenz.', a, f'({v}) / ({u}) ** {n}')
    if s == 2:
        u = R.choice([2, 3, 4, 5, Fr(1, 2)])
        n = R.randint(2, 6 if u in (2, Fr(1, 2)) else 4)
        v = Fr(u) ** n
        if R.random() < 0.5:
            a = nz(4)
            vv = a * v
            return zahl(f'y = a · {xn(n)} geht durch P({dz(u)} | {dz(vv)}). Bestimme a.', f'{dz(vv)} = a · {dz(v)} ⇒ a = {dz(a)}.',
                        'Berechne zuerst die Potenz, dann teilen.', a, f'({float(vv)}) / ({float(u)}) ** {n}')
        return zahl(f'y = xⁿ geht durch P({dz(u)} | {dz(v)}). Bestimme den Exponenten n.', f'{dz(u)}ⁿ = {dz(v)}; probieren: {dz(u)}{str(n).translate(H)} = {dz(v)}, also n = {n}.',
                    'Multipliziere die Basis so oft mit sich selbst, bis das Ergebnis erreicht ist.', n, f'{n}')
    n = R.randint(2, 4)
    a = nz(4)
    u1, u2 = R.sample([1, 2, 3, -1, -2], 2)
    if abs(u1) == abs(u2): return None
    v1, v2 = a * u1 ** n, a * u2 ** n
    return zahl(f'Der Graph von y = a · xⁿ geht durch P({dz(u1)} | {dz(v1)}) und Q({dz(u2)} | {dz(v2)}). Bestimme n.',
                f'Quotient: {dz(v2)} : {kl(v1)} = ({dz(u2)} : {kl(u1)})ⁿ = {br(Fr(v2, v1))} ⇒ n = {n} (dann a = {dz(a)}).',
                'Teile die beiden Gleichungen durcheinander, dann fällt a weg.', n, f'{n}')


def g_negativ(s):
    if s == 1:
        n, u = R.randint(1, 3), R.choice([2, 4, 5, 10])
        v = Fr(1, u ** n)
        return zahl(f'Berechne f({u}) für f(x) = {xn(-n)}. Gib das Ergebnis als Dezimalzahl an.', f'f({u}) = 1/{u}{str(n).translate(H)} = 1/{dz(u ** n)} = {dz(v)}.',
                    'Negativer Exponent: Kehrwert der Potenz.', v, f'1 / {u} ** {n}')
    typ = R.random()
    if s == 2:
        if typ < 0.4:
            n, u = R.randint(1, 4), Fr(1, R.choice([2, 3, 4]))
            v = 1 / u ** n
            return zahl(f'Berechne f({br(u)}) für f(x) = {xn(-n)}.', f'f({br(u)}) = 1/({br(u)}){str(n).translate(H)} = {dz(v)}.',
                        'Der Kehrwert eines Bruchs: Zähler und Nenner tauschen.', v, f'1 / (1 / {u.denominator}) ** {n}')
        n = R.randint(1, 6)
        a = R.choice([1, 1, -1, 2, 3, -2, Fr(1, 2)])
        r = SYM[0] if n % 2 == 0 else SYM[1]
        return auswahl(f'Welche Symmetrie hat der Graph von y = {fa(a, -n)}?', r, SYM,
                       f'{xn(-n)} = 1/{xn(n)}; n = {n} {"gerade" if n % 2 == 0 else "ungerade"}: {r}.' + (f' Der Faktor {dz(a)} ändert daran nichts.' if a != 1 else ''),
                       'Wie bei xⁿ entscheidet, ob n gerade ist.')
    if typ < 0.25:
        n = R.randint(1, 5)
        return auswahl(f'Für welche x ist f(x) = {xn(-n)} definiert?', 'für alle x ≠ 0', ['für alle x', 'für alle x > 0', 'für alle x ≥ 0'],
                       f'{xn(-n)} = 1/x{str(n).translate(H)}; durch 0 darf man nicht teilen, also x ≠ 0.', 'Schreibe die Potenz als Bruch.')
    if typ < 0.5:
        n = R.randint(2, 4)
        u = R.choice([2, 3, 4, 5])
        return auswahl(f'Jemand rechnet {u}{"⁻" + str(n).translate(H)} = −{dz(u ** n)}. Was stimmt?', f'Falsch: {u}{"⁻" + str(n).translate(H)} = 1/{dz(u ** n)}',
                       ['Richtig', f'Falsch: {u}{"⁻" + str(n).translate(H)} = −1/{dz(u ** n)}', f'Falsch: {u}{"⁻" + str(n).translate(H)} = −{dz(u * n)}'],
                       f'Ein negativer Exponent bedeutet Kehrwert: {u}{"⁻" + str(n).translate(H)} = 1/{u}{str(n).translate(H)} = 1/{dz(u ** n)} > 0.',
                       'Was bedeutet ein negatives Vorzeichen im Exponenten?')
    if typ < 0.75:
        n = R.randint(1, 4)
        seite = R.choice(['x > 0', 'x < 0']) if n % 2 else 'x > 0'
        if n % 2 and seite == 'x < 0':
            r, f2 = 'y wird beliebig klein (stark negativ).', 'y wird beliebig groß.'
        else:
            r, f2 = 'y wird beliebig groß.', 'y wird beliebig klein (stark negativ).'
        return bild(auswahl(f'Was passiert mit y = {xn(-n)} für x nahe 0, {seite}?', r, [f2, 'y kommt 0 beliebig nahe.', 'y wird genau 1.'],
                            f'Setze z. B. x = {"0,01" if seite == "x > 0" else "−0,01"} ein: 1/({"0,01" if seite == "x > 0" else "−0,01"}){str(n).translate(H)} ist betragsmäßig sehr groß'
                            + (', und negativ.' if r.startswith('y wird beliebig klein') else ', und positiv.') + ' Die y-Achse ist Asymptote.',
                            'Setze eine Zahl sehr nahe bei 0 ein.'),
                    kos([{'art': 'potenz', 'a': 1, 'n': -n}], x=(-4, 4), y=(-4, 4)) if R.random() < 0.5 else None)
    n = R.randint(1, 4)
    return auswahl(f'Was passiert mit y = {xn(-n)} für sehr große x?', 'y kommt der x-Achse beliebig nahe (bleibt aber positiv).',
                   ['y wird beliebig groß.', 'y wird negativ.', 'y wird genau 0.'],
                   f'1/x{str(n).translate(H)} wird für große x sehr klein, aber nie 0: Die x-Achse ist Asymptote.',
                   'Setze z. B. x = 100 ein.')


def g_wurzelfunktion(s):
    if s == 1:
        n = R.choice([2, 3])
        r = R.randint(2, 12 if n == 2 else 6)
        return zahl(f'f(x) = x{str(n).translate(H)} für x ≥ 0. Für welches x ist f(x) = {dz(r ** n)}?',
                    f'x{str(n).translate(H)} = {dz(r ** n)} ⇒ x = {"√" if n == 2 else "∛"}{dz(r ** n)} = {r} (x ≥ 0).',
                    'Rechne mit der Umkehrung (Wurzel) zurück.', r, f'{r ** n} / {r} ** {n - 1}')
    typ = R.random()
    if s == 2:
        if typ < 0.5:
            n = R.choice([2, 3])
            r = R.randint(2, 15 if n == 2 else 6)
            return zahl(f'Berechne f({dz(r ** n)}) für f(x) = x^(1/{n}).', f'x^(1/{n}) = {"√x" if n == 2 else "∛x"}; f({dz(r ** n)}) = {r}.',
                        'Hoch 1/n bedeutet n-te Wurzel.', r, f'{r ** n} / {r} ** {n - 1}')
        a, n = R.randint(2, 5), R.choice([2, 3])
        r = R.randint(2, 6)
        v = a * r ** n
        return zahl(f'f(x) = {a}x{str(n).translate(H)} für x ≥ 0. Für welches x ist f(x) = {dz(v)}?',
                    f'{a}x{str(n).translate(H)} = {dz(v)} ⇒ x{str(n).translate(H)} = {dz(r ** n)} ⇒ x = {r}.',
                    'Erst durch a teilen, dann die Wurzel ziehen.', r, f'({v} / {a}) / {r} ** {n - 1}')
    if typ < 0.15:
        return bild(auswahl('Im Bild siehst du y = x² (für x ≥ 0), y = √x und die Gerade y = x. Wie liegen die beiden Kurven zueinander?',
                            'Spiegelbildlich zur Geraden y = x.', ['Spiegelbildlich zur x-Achse.', 'Spiegelbildlich zur y-Achse.', 'Sie sind parallel verschoben.'],
                            'Bei der Umkehrfunktion tauschen x und y die Rollen. Das ist eine Spiegelung an y = x: (2 | 4) wird zu (4 | 2).',
                            'Vergleiche einen Punkt auf x² mit dem passenden Punkt auf √x.'),
                    {'typ': 'koordinaten', 'x': [0, 5], 'y': [0, 5], 'graphen': [{'art': 'potenz', 'a': 1, 'n': 2, 'name': 'x²', 'bereich': [0, 2.2]}, {'art': 'wurzel', 'name': '√x'}],
                     'strecken': [[0, 0, 5, 5, 'gestrichelt']]})
    if typ < 0.3:
        u = R.randint(2, 5)
        return auswahl(f'Der Punkt ({u} | {dz(u ** 3)}) liegt auf y = x³. Welcher Punkt liegt auf y = ∛x?', f'({dz(u ** 3)} | {u})',
                       [f'({u} | {dz(u ** 3)})', f'({u} | {dz(Fr(u ** 3, 3)) if u ** 3 % 3 == 0 else dz(-u)})', f'({dz(u ** 3)} | {dz(-u)})'],
                       f'Umkehrfunktion: x und y tauschen. ∛{dz(u ** 3)} = {u}, also ({dz(u ** 3)} | {u}).',
                       'Was passiert mit x- und y-Koordinate bei der Umkehrung?')
    if typ < 0.5:
        return auswahl('Welche Funktion ist die Umkehrfunktion von f(x) = x² für x ≥ 0?', 'g(x) = √x',
                       ['g(x) = x^(−2)', 'g(x) = x / 2', 'g(x) = −x²'],
                       'Die Umkehrfunktion macht das Quadrieren rückgängig: Aus y = x² folgt x = √y. Also g(x) = √x = x^(1/2).',
                       'Welche Rechnung macht das Quadrieren rückgängig?')
    if typ < 0.7:
        n = R.choice([2, 4])
        return auswahl(f'Für welche x ist f(x) = x^(1/{n}) definiert?', 'für alle x ≥ 0', ['für alle x', 'für alle x ≠ 0', 'für alle x > 0'],
                       f'x^(1/{n}) ist die {n}. Wurzel; sie ist nur für x ≥ 0 erklärt.', 'Aus welchen Zahlen kann man eine Wurzel ziehen?')
    u, v = R.randint(2, 9), None
    v = u * u
    return auswahl(f'Der Punkt ({u} | {v}) liegt auf dem Graphen von y = x². Welcher Punkt liegt dann auf dem Graphen von y = √x?',
                   f'({v} | {u})', [f'({u} | {v})', f'({-u} | {v})', f'({v} | {-u})'],
                   f'Bei der Umkehrfunktion werden x und y vertauscht: √{v} = {u}, also ({v} | {u}).',
                   'Was passiert mit x- und y-Koordinate bei der Umkehrung?')


GEN = {'werte': g_werte, 'symmetrie': g_symmetrie, 'verlauf': g_verlauf, 'parameter': g_parameter, 'negativ': g_negativ,
       'wurzelfunktion': g_wurzelfunktion}

if __name__ == '__main__':
    bauen('funktionen.potenz',
          'Potenzfunktionen y = a · xⁿ untersuchen: Werte, Symmetrie, Verlauf, Parameter; Erweiterung auf negative und rationale Exponenten.',
          ['n gerade: achsensymmetrisch, durch (−1 | 1) und (1 | 1). n ungerade: punktsymmetrisch, durch (−1 | −1) und (1 | 1).',
           'a < 0 spiegelt an der x-Achse, |a| streckt oder staucht.', 'x⁻ⁿ = 1/xⁿ, nur für x ≠ 0.', 'x^(1/2) = √x und x^(1/3) = ∛x sind für x ≥ 0 die Umkehrungen von x² und x³.'],
          [('Natürliche Exponenten', ['werte', 'symmetrie', 'verlauf']), ('Parameter', ['parameter']),
           ('Erweiterung des Potenzbegriffs', ['negativ', 'wurzelfunktion'])],
          ETAPPEN, GEN,
          meiden={'werte': ['f(−3) für f(x) = −2x³'], 'symmetrie': ['f(2) = 8'], 'verlauf': ['y = −x⁵?'], 'parameter': ['P(2 | −24)'],
                  'negativ': ['f(4) für f(x) = x^(−2)'], 'wurzelfunktion': ['f(x) = 64?']},
          offen=['Negative Exponenten werden jetzt hochgestellt geschrieben (x⁻², wie in der Regel); bitte in der App prüfen, ob „⁻“ gut lesbar ist.'])
