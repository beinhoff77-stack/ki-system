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
    if n < 0: return f'x^({dz(n)})'
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
     'fehler': '„y = x³ ist achsensymmetrisch zur y-Achse“ ist falsch: (−2)³ = −8, aber 2³ = 8. Bei ⟦ungeradem⟧ n ist der Graph punktsymmetrisch.'},
    {'lernziel': 'verlauf', 'titel': 'Verlauf und gemeinsame Punkte',
     'regel': 'y = xⁿ verläuft für ⟦n gerade⟧ von links oben nach rechts oben und durch (−1 | 1), (0 | 0), (1 | 1); für ⟦n ungerade⟧ von links unten nach rechts oben und durch (−1 | −1), (0 | 0), (1 | 1). ⟦a < 0⟧ spiegelt an der x-Achse.',
     'schritte': ['y = −x⁵: n = 5 ungerade, also y = x⁵ von links unten nach rechts oben.', 'a = −1 spiegelt an der x-Achse: ⟦von links oben nach rechts unten⟧.'],
     'probe': 'x = 2: −32 (unten), x = −2: 32 (oben) ✓',
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
     'fehler': 'f(4) = 4⁻² = −16 ist falsch: Ein negativer Exponent bedeutet ⟦Kehrwert⟧, nicht negatives Ergebnis: 4⁻² = 1/16.'},
    {'lernziel': 'wurzelfunktion', 'titel': 'Wurzelfunktionen und Umkehrung',
     'regel': 'y = x^(1/2) = √x und y = x^(1/3) = ∛x sind für ⟦x ≥ 0⟧ definiert. Sie sind die ⟦Umkehrfunktionen⟧ von y = x² bzw. y = x³ (für x ≥ 0): Aus y wird x zurückgerechnet.',
     'schritte': ['f(x) = x³ (x ≥ 0). Für welches x ist f(x) = 64?', 'Umkehrung: x = ∛64 = ⟦4⟧.'],
     'probe': '4³ = 64 ✓',
     'fehler': '„√x ist für alle x definiert“ ist falsch: √(−4) gibt es nicht. Die Wurzelfunktion hat die ⟦Definitionsmenge x ≥ 0⟧.'},
]


def g_werte(s):
    if s == 1:
        n, a, u = R.randint(2, 4), R.randint(1, 5), R.randint(1, 4)
    elif s == 2:
        n, a, u = R.randint(2, 5), nz(5), nz(3)
    else:
        n = R.randint(2, 6)
        a = nz(4)
        if R.random() < 0.5:
            u = Fr(R.choice([-5, -1, 1, 3, 5]), 10) if n < 5 else Fr(R.choice([-1, 1]), 2)
        else:
            u = R.choice([-3, -2, 2, 3])
    v = a * Fr(u) ** n
    return zahl(f'Berechne f({dz(u)}) für f(x) = {fa(a, n)}.', f'{kl(u)}{str(n).translate(H)} = {dz(Fr(u) ** n)}; f({dz(u)}) = {dz(a)} · {kl(Fr(u) ** n)} = {dz(v)}.',
                'Erst potenzieren, dann mit a multiplizieren. Klammern um negative Zahlen!', v, f'({a}) * ({float(u) if not isinstance(u, int) else u}) ** {n}')


def g_symmetrie(s):
    n = R.randint(2, 9)
    a = nz(5)
    if s == 1 or (s == 2 and R.random() < 0.4):
        r = 'achsensymmetrisch zur y-Achse' if n % 2 == 0 else 'punktsymmetrisch zum Ursprung'
        return auswahl(f'Welche Symmetrie hat der Graph von y = {fa(a, n)}?', r,
                       ['achsensymmetrisch zur y-Achse', 'punktsymmetrisch zum Ursprung', 'achsensymmetrisch zur x-Achse'],
                       f'n = {n} ist {"gerade" if n % 2 == 0 else "ungerade"}, also {r}.', 'Ist der Exponent gerade oder ungerade?')
    u = R.randint(1, 3)
    v = a * u ** n
    if s == 2:
        g = v if n % 2 == 0 else -v
        return zahl(f'Für f(x) = a · {xn(n)} gilt f({u}) = {dz(v)}. Bestimme f(−{u}) ohne a zu berechnen.',
                    f'n = {n} {"gerade: f(−x) = f(x)" if n % 2 == 0 else "ungerade: f(−x) = −f(x)"}, also f(−{u}) = {dz(g)}.',
                    'Nutze die Symmetrie des Graphen.', g, f'({v}) * (-1) ** {n}')
    typ = R.random()
    if typ < 0.5:
        m = R.randint(1, 4) * 2 + 1
        return auswahl(f'Jemand behauptet: „y = {fa(a, m)} ist achsensymmetrisch zur y-Achse, weil {fa(a, m)} für x = 1 und x = −1 gleich groß ist.“ Was stimmt?',
                       f'Falsch: f(1) = {dz(a)}, f(−1) = {dz(-a)}; der Graph ist punktsymmetrisch.',
                       ['Richtig, das ist die Bedingung für Achsensymmetrie.', 'Falsch: Der Graph ist zu keiner Achse und keinem Punkt symmetrisch.',
                        'Richtig, alle Potenzfunktionen sind achsensymmetrisch.'],
                       f'f(−1) = {dz(a)} · (−1){str(m).translate(H)} = {dz(-a)} ≠ {dz(a)} = f(1). Ungerader Exponent: punktsymmetrisch zum Ursprung.',
                       'Rechne f(1) und f(−1) wirklich aus.')
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
    a = nz(6) if s > 1 else R.choice([1, -1])
    if s < 3 or R.random() < 0.4:
        r = VERL[(n % 2, 1 if a > 0 else -1)]
        return auswahl(f'Wie verläuft der Graph von y = {fa(a, n)}?', r, list(VERL.values()),
                       f'n = {n} {"gerade" if n % 2 == 0 else "ungerade"}, a {"> 0" if a > 0 else "< 0"}: {r}.',
                       'Was passiert für große positive und große negative x-Werte?')
    if R.random() < 0.5:
        p = R.choice(['(−1 | 1)', '(−1 | −1)'])
        ger = p == '(−1 | 1)'
        r = 'alle mit geradem n' if ger else 'alle mit ungeradem n'
        m = R.randint(2, 9)
        return auswahl(f'Welche Graphen der Form y = xⁿ (n natürlich, n ≥ 2) gehen durch {p}? Denke z. B. an n = {m}.', r,
                       ['alle mit geradem n', 'alle mit ungeradem n', 'alle', 'keiner'],
                       f'(−1)ⁿ ist 1 für gerades n und −1 für ungerades n. Also gehen {r.replace("alle mit", "die Graphen mit")} durch {p}.',
                       'Berechne (−1)ⁿ für ein gerades und ein ungerades n.')
    n1, n2 = R.sample(range(2, 7), 2)
    u = Fr(1, 2)
    hoch = n1 if n1 < n2 else n2
    return auswahl(f'Welcher Graph liegt für 0 < x < 1 weiter oben: y = {xn(n1)} oder y = {xn(n2)}?', f'y = {xn(hoch)}',
                   [f'y = {xn(n1 + n2 - hoch)}', 'beide gleich', 'Das hängt von x ab.'],
                   f'Zwischen 0 und 1 wird die Zahl beim Potenzieren kleiner, z. B. 0,5{str(hoch).translate(H)} = {dz(u ** hoch)} > 0,5{str(n1 + n2 - hoch).translate(H)} = {dz(u ** (n1 + n2 - hoch))}.',
                   'Setze probeweise x = 0,5 ein.')


def g_parameter(s):
    if s == 1:
        n, a, u = R.randint(2, 3), nz(6), R.choice([1, 2, 3, -1, -2])
        v = a * u ** n
        return zahl(f'y = a · {xn(n)} geht durch P({dz(u)} | {dz(v)}). Bestimme a.', f'{dz(v)} = a · {kl(u)}{str(n).translate(H)} = {dz(u ** n)}a ⇒ a = {dz(a)}.',
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
                f'Quotient: {dz(v2)} : {dz(v1)} = ({dz(u2)} : {dz(u1)})ⁿ = {br(Fr(v2, v1))} ⇒ n = {n} (dann a = {dz(a)}).',
                'Teile die beiden Gleichungen durcheinander, dann fällt a weg.', n, f'{n}')


def g_negativ(s):
    if s == 1:
        n, u = R.randint(1, 3), R.choice([2, 4, 5, 10])
        v = Fr(1, u ** n)
        return zahl(f'Berechne f({u}) für f(x) = x^(−{n}). Gib das Ergebnis als Dezimalzahl an.', f'f({u}) = 1/{u}{str(n).translate(H)} = 1/{dz(u ** n)} = {dz(v)}.',
                    'Negativer Exponent: Kehrwert der Potenz.', v, f'1 / {u} ** {n}')
    typ = R.random()
    if s == 2:
        if typ < 0.4:
            n, u = R.randint(1, 4), Fr(1, R.choice([2, 3, 4]))
            v = 1 / u ** n
            return zahl(f'Berechne f({br(u)}) für f(x) = x^(−{n}).', f'f({br(u)}) = 1/({br(u)}){str(n).translate(H)} = {dz(v)}.',
                        'Der Kehrwert eines Bruchs: Zähler und Nenner tauschen.', v, f'1 / (1 / {u.denominator}) ** {n}')
        n = R.randint(1, 6)
        r = 'achsensymmetrisch zur y-Achse' if n % 2 == 0 else 'punktsymmetrisch zum Ursprung'
        return auswahl(f'Welche Symmetrie hat der Graph von y = x^(−{n})?', r,
                       ['achsensymmetrisch zur y-Achse', 'punktsymmetrisch zum Ursprung', 'achsensymmetrisch zur x-Achse'],
                       f'x^(−{n}) = 1/x{str(n).translate(H)}; n = {n} {"gerade" if n % 2 == 0 else "ungerade"}: {r}.', 'Wie bei xⁿ entscheidet, ob n gerade ist.')
    if typ < 0.35:
        n = R.randint(1, 5)
        return auswahl(f'Für welche x ist f(x) = x^(−{n}) definiert?', 'für alle x ≠ 0', ['für alle x', 'für alle x > 0', 'für alle x ≥ 0'],
                       f'x^(−{n}) = 1/x{str(n).translate(H)}; durch 0 darf man nicht teilen, also x ≠ 0.', 'Schreibe die Potenz als Bruch.')
    if typ < 0.7:
        n = R.randint(1, 4)
        u = R.choice([2, 4, 5, 10])
        return auswahl(f'Jemand rechnet {u}^(−{n}) = −{dz(u ** n)}. Was stimmt?', f'Falsch: {u}^(−{n}) = 1/{dz(u ** n)} = {dz(Fr(1, u ** n))}',
                       ['Richtig', f'Falsch: {u}^(−{n}) = −1/{dz(u ** n)}', f'Falsch: {u}^(−{n}) = {dz(u * n)}'],
                       f'Ein negativer Exponent bedeutet Kehrwert: {u}^(−{n}) = 1/{u}{str(n).translate(H)} = {dz(Fr(1, u ** n))} > 0.',
                       'Was bedeutet ein negatives Vorzeichen im Exponenten?')
    n = R.randint(1, 4)
    return auswahl(f'Was passiert mit y = x^(−{n}) für sehr große x?', 'y kommt der x-Achse beliebig nahe (bleibt aber positiv).',
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
    if typ < 0.4:
        return auswahl('Welche Funktion ist die Umkehrfunktion von f(x) = x² für x ≥ 0?', 'g(x) = √x',
                       ['g(x) = x^(−2)', 'g(x) = x / 2', 'g(x) = −x²'],
                       'Die Umkehrfunktion macht das Quadrieren rückgängig: Aus y = x² folgt x = √y. Also g(x) = √x = x^(1/2).',
                       'Welche Rechnung macht das Quadrieren rückgängig?')
    if typ < 0.7:
        n = R.choice([2, 4])
        return auswahl(f'Für welche x ist f(x) = x^(1/{n}) definiert?', 'für alle x ≥ 0', ['für alle x', 'für alle x ≠ 0', 'für alle x > 1'],
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
          offen=['Alle Lernkarten profitieren von Funktionsgraphen (y = xⁿ für mehrere n, Asymptoten bei x⁻ⁿ, Spiegelung bei der Umkehrfunktion). Die App kann noch keine Graphen zeichnen; Verlauf und Symmetrie werden deshalb in Worten abgefragt.',
                 'Negative Exponenten werden als „x^(−2)“ geschrieben (Hochstellung von Minuszeichen im Fließtext unsicher).'])
