#!/usr/bin/env python3
"""Thema terme.quadratische_extreme – Quadratische Terme und Extremwerte (Realschule Bayern, Klasse 8)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _rs import *  # noqa: E402,F403

start(9701)
LX = 'x = □; T = □'
HX = 'Erst die Stelle x, dann den Extremwert T.'


def nz(n):
    return R.choice([i for i in range(-n, n + 1) if i != 0])


def quad(a, b, c):
    return poly(a, b, c)


def klammer(d):
    """(x − d) als Text"""
    return minus_klammer(d)


def scheitel(a, d, e):
    """a(x − d)² + e als Text"""
    vor = '' if a == 1 else ('−' if a == -1 else dz(a))
    if a != 1 and a != -1 and not isinstance(a, int) and Fr(a).denominator != 1: vor = dz(a)
    k = klammer(d) if d != 0 else 'x'
    teil = f'{vor}{k}²' if d != 0 else f'{vor}x²'
    return teil + (f' {plus(e)}' if e != 0 else '')


ETAPPEN = [
    {'lernziel': 'ergaenzen', 'titel': 'Zum Binom ergänzen',
     'regel': 'Ein Term x² + bx wird zu einem vollständigen Quadrat, wenn du ⟦(b : 2)²⟧ ergänzt: ⟦x² + bx + (b : 2)² = (x + b : 2)²⟧. Bild: x² + 6x sind ein Quadrat x mal x und zwei Streifen 3 mal x. Zum großen Quadrat (x + 3)² fehlt nur die ⟦Ecke 3 · 3 = 9⟧.',
     'bild': {'typ': 'figur', 'punkte': {'_a': [0, 0], '_b': [5, 0], '_c': [8, 0], '_d': [8, 5], '_e': [8, 8], '_f': [5, 8], '_g': [0, 8], '_h': [0, 5], '_m': [5, 5]},
              'flaeche': ['_m', '_d', '_e', '_f'],
              'linien': [['_a', '_b', 'x'], ['_b', '_c', '3'], ['_c', '_d'], ['_d', '_e'], ['_e', '_f'], ['_f', '_g'], ['_g', '_h', '3'], ['_h', '_a', 'x'],
                         ['_b', '_m'], ['_m', '_f'], ['_h', '_m'], ['_m', '_d']]},
     'schritte': ['x² + 6x: Hälfte von 6 ist 3, und 3² = 9.', 'x² + 6x + ⟦9⟧ = ⟦(x + 3)²⟧.'],
     'probe': '(x + 3)² = x² + 2 · 3 · x + 9 = x² + 6x + 9 ✓',
     'fehler': 'x² + 6x + 36 = (x + 6)² ist falsch: In die Klammer gehört die ⟦Hälfte⟧ von 6, also 3; ergänzt wird 3² = 9.'},
    {'lernziel': 'scheitelform', 'titel': 'Quadratische Ergänzung',
     'regel': 'Bei x² + bx + c ergänzt du (b : 2)² und ⟦ziehst es gleich wieder ab⟧ – so ändert sich der Wert nicht: ⟦x² + bx + c = (x + b : 2)² − (b : 2)² + c⟧.',
     'schritte': ['x² − 8x + 21 = x² − 8x + 16 − 16 + 21.', 'Zusammenfassen: ⟦(x − 4)² + 5⟧.'],
     'probe': 'x = 0: 0 − 0 + 21 = 21 und (0 − 4)² + 5 = 16 + 5 = 21 ✓',
     'fehler': 'x² − 8x + 21 = (x − 4)² + 21 ist falsch: Die ergänzte 16 muss auch wieder ⟦abgezogen⟧ werden, sonst ist der Term um 16 zu groß.'},
    {'lernziel': 'extremwert', 'titel': 'Minimum oder Maximum ablesen',
     'regel': 'Ein Quadrat ist ⟦nie negativ⟧: (x − 4)² ≥ 0, am kleinsten ist es (nämlich 0) für ⟦x = 4⟧. Also hat (x − 4)² + 5 das ⟦Minimum 5 für x = 4⟧. Steht ein ⟦Minus vor der Klammer⟧, z. B. −(x − 4)² + 5, gibt es ein ⟦Maximum⟧ 5 für x = 4.',
     'schritte': ['T(x) = (x + 2)² − 7: Die Klammer ist 0 für x = −2.', 'Kleinster Wert: ⟦T = −7 für x = −2⟧ (Minimum).'],
     'probe': 'x = −1: (1)² − 7 = −6 > −7 ✓',
     'fehler': 'Bei (x + 2)² − 7 das Minimum bei x = 2 abzulesen ist falsch: (x + 2) wird null für ⟦x = −2⟧.'},
    {'lernziel': 'mit_faktor', 'titel': 'Terme mit Faktor vor x²',
     'regel': 'Steht vor x² ein Faktor a ≠ 1, ⟦klammerst du a aus⟧ den x-Gliedern aus und ergänzt in der Klammer. Ist ⟦a > 0⟧, gibt es ein Minimum; ist ⟦a < 0⟧, ein Maximum.',
     'schritte': ['T(x) = 2x² − 12x + 23 = 2(x² − 6x) + 23 = 2(x² − 6x + 9 − 9) + 23.',
                  '= 2(x − 3)² − 18 + 23 = ⟦2(x − 3)² + 5⟧. Minimum ⟦T = 5 für x = 3⟧.'],
     'probe': 'T(3) = 18 − 36 + 23 = 5 ✓',
     'fehler': '2(x² − 6x + 9 − 9) + 23 = 2(x − 3)² − 9 + 23 ist falsch: Die −9 steht in der Klammer und muss ⟦mit 2 multipliziert⟧ werden: −18.'},
    {'lernziel': 'optimierung', 'titel': 'Optimierungsaufgaben',
     'regel': 'Bei Optimierungsaufgaben stellst du die Größe, die möglichst groß oder klein werden soll, als ⟦Term in x⟧ auf. Dann bestimmst du mit der quadratischen Ergänzung das ⟦Extremum⟧ und beantwortest die Frage im Sachzusammenhang.',
     'schritte': ['Ein Rechteck hat 20 m Umfang. Ist eine Seite x, ist die andere 10 − x. Fläche: A(x) = x(10 − x) = −x² + 10x.',
                  '−x² + 10x = −(x² − 10x + 25 − 25) = −(x − 5)² + 25. ⟦Maximum 25 m² für x = 5 m⟧ – ein Quadrat.'],
     'probe': 'x = 4: 4 · 6 = 24 < 25 ✓',
     'fehler': 'Die Fläche 25 m² als Seitenlänge anzugeben ist falsch: Lies genau, was gefragt ist – die ⟦Stelle x⟧ (Seitenlänge) oder den ⟦Extremwert⟧ (Fläche).'},
]


# ---------- Generatoren ----------
def g_ergaenzen(s):
    if s == 1:
        h = R.randint(1, 9)
        return luecken('Ergänze zu einem vollständigen Quadrat.', f'x² + {2 * h}x + □ = (x + □)²', 'Erst die ergänzte Zahl, dann die Zahl in der Klammer.',
                       [h * h, h], f'Hälfte von {2 * h} ist {h}, {h}² = {h * h}: x² + {2 * h}x + {h * h} = (x + {h})².',
                       'Halbiere die Zahl vor x und quadriere sie.', c=[f'({2 * h} / 2) ** 2', f'{2 * h} / 2'])
    if s == 2:
        h = R.randint(1, 12)
        if R.random() < 0.5:
            sg = R.choice([1, -1])
            return luecken(f'Schreibe x² {plus_v(sg * 2 * h)} + {h * h} als Quadrat einer Klammer.', '(x + □)²', 'Zahl in der Klammer; bei Minus eine negative Zahl.',
                           [sg * h], f'{h * h} = {h}² und {2 * h} = 2 · {h}: x² {plus_v(sg * 2 * h)} + {h * h} = {klammer(-sg * h)}².',
                           'Welche Zahl ergibt quadriert die Zahl am Ende? Passt das Doppelte zur Zahl vor x?', c=[f'({sg * 2 * h}) / 2'])
        return luecken('Ergänze so, dass ein Binom entsteht.', f'x² − {2 * h}x + □ = (x − □)²', 'Erst die ergänzte Zahl, dann die Zahl in der Klammer.',
                       [h * h, h], f'Hälfte von {2 * h} ist {h}, {h}² = {h * h}: x² − {2 * h}x + {h * h} = (x − {h})².',
                       'Das Minus bleibt in der Klammer. Ergänzt wird immer eine positive Zahl.', c=[f'({2 * h} / 2) ** 2', f'{2 * h} / 2'])
    art = R.random()
    h = nz(9)
    if art < 0.35:
        b = 2 * h
        return auswahl(f'Welche Zahl musst du zu x² {plus_v(b)} addieren, damit ein Binom entsteht?', dz(h * h),
                       [dz(b * b), dz(abs(b)), dz(-h * h)], f'(b : 2)² = ({dz(b)} : 2)² = {kl(h)}² = {dz(h * h)}.',
                       'Halbieren, dann quadrieren – das Ergebnis ist nie negativ.')
    if art < 0.7:
        b = R.choice([1, 3, 5, 7])
        sg = R.choice([1, -1])
        # (b/2)² als Dezimalzahl
        q = Fr(b * b, 4)
        return zahl(f'Welche Zahl muss man zu x² {plus_v(sg * b)} addieren, damit ein Binom entsteht? Gib sie als Dezimalzahl an.',
                    f'Hälfte von {b} ist {dz(Fr(b, 2))}, und {dz(Fr(b, 2))}² = {dz(q)}.', 'Auch bei ungeraden Zahlen: halbieren, dann quadrieren.',
                    q, f'({b} / 2) ** 2')
    k = R.randint(2, 9)
    return auswahl(f'Jemand schreibt: x² + {2 * k}x + {2 * k} = (x + {k})². Was stimmt?',
                   f'Falsch: Ergänzt werden muss {k * k}, also x² + {2 * k}x + {k * k} = (x + {k})².',
                   ['Richtig.', f'Falsch: Richtig ist (x + {2 * k})².', f'Falsch: Ergänzt werden muss {4 * k * k}.'],
                   f'(x + {k})² = x² + {2 * k}x + {k * k}. Die ergänzte Zahl ist ({2 * k} : 2)² = {k * k}, nicht {2 * k}.',
                   'Rechne (x + …)² mit der binomischen Formel aus.')


def g_scheitelform(s):
    LS, HS = 'T(x) = (x + □)² + □', 'Zahl in der Klammer, dann die Zahl dahinter. (x + (−3))² bedeutet (x − 3)².'
    d = nz(7) if s > 1 else R.randint(1, 6) * R.choice([1, -1])
    e = R.randint(-12, 12)
    b, c = -2 * d, d * d + e
    w = f'{quad(1, b, c)} = {quad(1, b, 0)} + {d * d} − {d * d} {plus(c)} = {klammer(d)}² {plus(e)}.'
    if s in (1, 2):
        return luecken(f'Bringe T(x) = {quad(1, b, c)} mit quadratischer Ergänzung in die Form (x + □)² + □.', LS, HS, [-d, e], w,
                       'Ergänze (b : 2)² und ziehe es gleich wieder ab.', c=[f'({b}) / 2', f'{c} - (({b}) / 2) ** 2'])
    art = R.random()
    if art < 0.4:
        falsch = [f'{klammer(d)}² {plus(c)}', f'{klammer(-d)}² {plus(e)}', f'{klammer(d)}² {plus(c + d * d)}']
        return auswahl(f'Welcher Term ist gleich T(x) = {quad(1, b, c)}?', f'{klammer(d)}² {plus(e)}', falsch, w,
                       'Was wurde ergänzt – und wurde es wieder abgezogen?')
    if art < 0.7:
        # Umkehr: Scheitelform ausmultiplizieren
        return luecken(f'Multipliziere T(x) = {klammer(d)}² {plus(e)} aus.', '□x² + □x + □', 'Tippe den ganzen Term ein, z. B. x² − 6x + 4.',
                       [1, b, c], f'{klammer(d)}² = {quad(1, b, d * d)}, dazu {dz(e)}: {quad(1, b, c)}.',
                       'Binomische Formel, dann die Zahl dazurechnen.', c=['1', str(b), str(c)])
    # mit ungeradem b
    h = Fr(R.choice([1, 3, 5, 7]), 2) * R.choice([1, -1])
    e2 = Fr(R.randint(-8, 8)) + Fr(R.choice([1, 3]), 4)
    c2 = h * h + e2
    b2 = 2 * h
    return zahl(f'T(x) = x² {plus_v(b2)} {plus(c2)}. Welchen kleinsten Wert kann T(x) annehmen?',
                f'T(x) = (x {plus(h)})² − {dz(h * h)} {plus(c2)} = (x {plus(h)})² {plus(e2)}. Kleinster Wert {dz(e2)} für x = {dz(-h)}.',
                'Auch mit Dezimalzahlen: Hälfte von b quadrieren, ergänzen und wieder abziehen.', e2, f'{cz(c2)} - ({cz(b2)} / 2) ** 2')


def g_extremwert(s):
    d, e = nz(8), R.randint(-15, 15)
    if s == 1:
        a = R.choice([1, -1])
        art = 'Minimum' if a > 0 else 'Maximum'
        return luecken(f'Bestimme Stelle und Wert des Extremums von T(x) = {scheitel(a, d, e)}.', LX, HX, [d, e],
                       f'Die Klammer ist 0 für x = {dz(d)}. {art} T = {dz(e)} für x = {dz(d)}.',
                       'Für welches x wird die Klammer null?', c=[str(d), str(e)])
    if s == 2:
        a = R.choice([1, -1, 2, -2, 3, Fr(1, 2), -3])
        if R.random() < 0.4:
            return auswahl(f'Hat T(x) = {scheitel(a, d, e)} ein Minimum oder ein Maximum?',
                           f'{"Minimum" if a > 0 else "Maximum"} {dz(e)} für x = {dz(d)}',
                           [f'{"Maximum" if a > 0 else "Minimum"} {dz(e)} für x = {dz(d)}', f'{"Minimum" if a > 0 else "Maximum"} {dz(e)} für x = {dz(-d)}',
                            f'{"Minimum" if a > 0 else "Maximum"} {dz(d)} für x = {dz(e)}'],
                           f'Vorfaktor {dz(a)} {"> 0: Das Quadrat wird addiert, also Minimum" if a > 0 else "< 0: Das Quadrat wird abgezogen, also Maximum"}. Klammer 0 für x = {dz(d)}, Wert {dz(e)}.',
                           'Wird das Quadrat addiert oder abgezogen?')
        return luecken(f'Bestimme Stelle und Wert des Extremums von T(x) = {scheitel(a, d, e)}.', LX, HX, [d, e],
                       f'Klammer 0 für x = {dz(d)}; T = {dz(e)}. Vorfaktor {dz(a)}: {"Minimum" if a > 0 else "Maximum"}.',
                       'Achte auf das Vorzeichen in der Klammer.', c=[str(d), str(e)])
    art = R.random()
    if art < 0.35:
        b, c = -2 * d, d * d + e
        sg = R.choice([1, -1])
        if sg == 1:
            return luecken(f'Bestimme Stelle und Wert des Minimums von T(x) = {quad(1, b, c)}.', LX, HX, [d, e],
                           f'T(x) = {klammer(d)}² {plus(e)}. Minimum T = {dz(e)} für x = {dz(d)}.',
                           'Erst quadratisch ergänzen, dann ablesen.', c=[f'-({b}) / 2', f'{c} - (({b}) / 2) ** 2'])
        return luecken(f'Bestimme Stelle und Wert des Maximums von T(x) = {quad(-1, -b, -c + 2 * e)}.', LX, HX, [d, e],
                       f'T(x) = −(x² {plus_v(b)} {plus(c - 2 * e)}) = −({klammer(d)}² {plus(-e)}) = −{klammer(d)}² {plus(e)}. Maximum T = {dz(e)} für x = {dz(d)}.',
                       'Klammere zuerst −1 aus.', c=[f'-({b}) / 2', f'-((({c - 2 * e}) - (({b}) / 2) ** 2))'])
    if art < 0.7:
        a = R.choice([1, 2, -1, -2])
        f = [f'T(x) kann für ein x kleiner als {dz(e)} werden.' if a > 0 else f'T(x) kann für ein x größer als {dz(e)} werden.',
             f'Der Extremwert ist {dz(d)}.', f'Für x = {dz(-d)} ist T(x) = {dz(e)}.']
        r = f'T(x) ist immer {"≥" if a > 0 else "≤"} {dz(e)}.'
        return auswahl(f'Welche Aussage über T(x) = {scheitel(a, d, e)} ist richtig?', r, f,
                       f'{scheitel(a, 0, 0).replace("x²", klammer(d) + "²")} ist {"nie negativ" if a > 0 else "nie positiv"}, also T(x) {"≥" if a > 0 else "≤"} {dz(e)}.',
                       'Was weißt du über das Vorzeichen eines Quadrats?')
    return auswahl(f'Für welches x ist T(x) = {scheitel(1, d, e)} am kleinsten – und gibt es auch einen größten Wert?',
                   f'Kleinster Wert bei x = {dz(d)}; einen größten Wert gibt es nicht.',
                   [f'Kleinster Wert bei x = {dz(d)}; größter Wert bei x = {dz(-d)}.', f'Kleinster Wert bei x = {dz(-d)}; einen größten Wert gibt es nicht.',
                    f'Kleinster Wert bei x = {dz(e)}; einen größten Wert gibt es nicht.'],
                   f'Die Klammer ist 0 für x = {dz(d)}. Je weiter x davon weg ist, desto größer wird das Quadrat – ohne Grenze.',
                   'Wie groß kann ein Quadrat werden?')


def g_mit_faktor(s):
    a = R.choice([2, 3, 4, 5]) * (1 if s == 1 else R.choice([1, -1]))
    d, e = nz(5), nz(12)
    b, c = -2 * a * d, a * d * d + e
    art = 'Minimum' if a > 0 else 'Maximum'
    w = (f'T(x) = {dz(a)}(x² {plus_v(b // a)}) {plus(c)} = {dz(a)}(x² {plus_v(b // a)} + {d * d} − {d * d}) {plus(c)} '
         f'= {dz(a)}{klammer(d)}² {plus(-a * d * d)} {plus(c)} = {dz(a)}{klammer(d)}² {plus(e)}. {art} T = {dz(e)} für x = {dz(d)}.')
    if s in (1, 2):
        return luecken(f'Bestimme Stelle und Wert des Extremums von T(x) = {quad(a, b, c)}.', LX, HX, [d, e], w,
                       f'Klammere {dz(a)} aus den x-Gliedern aus, ergänze in der Klammer.', c=[f'-({b}) / (2 * ({a}))', f'{c} - ({b}) ** 2 / (4 * ({a}))'])
    art_ = R.random()
    if art_ < 0.4:
        falsch = e + a * d * d - d * d
        return auswahl(f'Jemand formt T(x) = {quad(a, b, c)} um zu {dz(a)}{klammer(d)}² {plus(falsch)}. Was stimmt?',
                       f'Falsch: Die abgezogene {d * d} muss mit {dz(a)} multipliziert werden. Richtig: {dz(a)}{klammer(d)}² {plus(e)}.',
                       ['Richtig.', f'Falsch: Richtig ist {dz(a)}{klammer(-d)}² {plus(falsch)}.', f'Falsch: Richtig ist {klammer(d)}² {plus(e)}.'],
                       w, 'Setze x = 0 in beide Terme ein und vergleiche.')
    if art_ < 0.7:
        return auswahl(f'Hat T(x) = {quad(a, b, c)} ein Minimum oder ein Maximum?', art,
                       ['Maximum' if a > 0 else 'Minimum', 'beides', 'keins von beiden'],
                       f'Der Faktor vor x² ist {dz(a)} {"> 0, also Minimum" if a > 0 else "< 0, also Maximum"}.',
                       'Schau nur auf das Vorzeichen vor x².')
    a2 = Fr(R.choice([1, -1]), 2)
    d2 = R.choice([2, 4, 6, -2, -4])
    e2 = R.randint(-6, 6)
    b2, c2 = -2 * a2 * d2, a2 * d2 * d2 + e2
    return luecken(f'Bestimme Stelle und Wert des Extremums von T(x) = {quad(a2, b2, c2)}.', LX, HX, [d2, e2],
                   f'T(x) = {dz(a2)}(x² {plus_v(Fr(b2) / a2)}) {plus(c2)} = {dz(a2)}{klammer(d2)}² {plus(-a2 * d2 * d2)} {plus(c2)} = {dz(a2)}{klammer(d2)}² {plus(e2)}. '
                   f'{"Minimum" if a2 > 0 else "Maximum"} T = {dz(e2)} für x = {dz(d2)}.',
                   f'Klammere {dz(a2)} aus: Teilen durch {dz(a2)} heißt mal {dz(1 / a2)}.', c=[f'-({cz(b2)}) / (2 * {cz(a2)})', f'{cz(c2)} - ({cz(b2)}) ** 2 / (4 * {cz(a2)})'])


def g_optimierung(s):
    art = R.choice(['rechteck', 'mauer', 'zahlen', 'preis']) if s > 1 else R.choice(['rechteck', 'zahlen'])
    if art == 'rechteck':
        U = R.choice([12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 60, 80])
        h = U // 2
        x = Fr(h, 2)
        A = x * x
        if s == 1:
            return zahl(f'Ein Rechteck hat den Umfang {U} m. Seite x, andere Seite {h} − x. Wie lang muss x sein, damit die Fläche maximal wird?',
                        f'A(x) = x({h} − x) = −x² + {h}x = −(x − {dz(x)})² + {dz(A)}. Maximum für x = {dz(x)} m.',
                        'Stelle A(x) auf und ergänze quadratisch.', x, f'{h} / 2', einheit='m')
        return zahl(f'Aus {U} m Zaun soll ein rechteckiges Gehege mit möglichst großer Fläche entstehen. Wie groß ist diese Fläche höchstens?',
                    f'Seiten x und {h} − x. A(x) = −x² + {h}x = −(x − {dz(x)})² + {dz(A)}. Höchstens {dz(A)} m².',
                    'Halber Umfang = Summe zweier Seiten. A(x) aufstellen und das Maximum bestimmen.', A, f'({h} / 2) ** 2', einheit='m²')
    if art == 'mauer':
        L = R.choice([12, 16, 20, 24, 30, 36, 40, 48, 60])
        x = Fr(L, 4)
        A = x * (L - 2 * x)
        if R.random() < 0.5:
            return zahl(f'An einer langen Mauer wird mit {L} m Zaun ein rechteckiges Beet abgegrenzt (die Mauer ist eine Seite). Die zwei Seiten senkrecht zur Mauer sind je x m lang. Für welches x ist die Fläche maximal?',
                        f'A(x) = x({L} − 2x) = −2x² + {L}x = −2(x − {dz(x)})² + {dz(A)}. Maximum für x = {dz(x)} m.',
                        'Die Seite parallel zur Mauer ist L − 2x lang.', x, f'{L} / 4', einheit='m')
        return zahl(f'An einer Mauer wird mit {L} m Zaun ein Rechteck abgegrenzt (Mauer als eine Seite). Wie groß kann die Fläche höchstens werden?',
                    f'A(x) = x({L} − 2x) = −2(x − {dz(x)})² + {dz(A)}. Höchstens {dz(A)} m².',
                    'Zwei Seiten x, eine Seite L − 2x. A(x) aufstellen und ergänzen.', A, f'{L} / 4 * ({L} - 2 * {L} / 4)', einheit='m²')
    if art == 'zahlen':
        S = R.choice([8, 10, 12, 14, 16, 18, 20, 22, 26, 30, 7, 9, 11, 13])
        x = Fr(S, 2)
        P = x * x
        if s == 1 or R.random() < 0.5:
            return zahl(f'Die Summe zweier Zahlen ist {S}. Wie groß kann ihr Produkt höchstens sein?',
                        f'Zahlen x und {S} − x. P(x) = x({S} − x) = −(x − {dz(x)})² + {dz(P)}. Höchstens {dz(P)}.',
                        'Zweite Zahl: Summe minus erste Zahl. Produkt als Term in x.', P, f'({S} / 2) ** 2')
        D = R.choice([4, 6, 8, 10, 12])
        x = Fr(-D, 2)
        return zahl(f'Die Differenz zweier Zahlen ist {D}. Welches ist das kleinste mögliche Produkt?',
                    f'Zahlen x und x + {D}. P(x) = x² + {D}x = (x + {dz(Fr(D, 2))})² − {dz(Fr(D * D, 4))}. Kleinstes Produkt {dz(Fr(-D * D, 4))} für x = {dz(x)}.',
                    'Zahlen x und x + D. Produkt aufstellen, Minimum bestimmen.', Fr(-D * D, 4), f'-({D} / 2) ** 2')
    # Preis: Ein Kiosk verkauft n Stück zu p €; je 10 ct teurer, k Stück weniger
    p0 = R.choice([1, 2, 3])
    n0 = R.choice([200, 240, 300, 360])
    k = R.choice([10, 12, 15, 20])
    # Einnahme E(x) = (p0 + 0,1x)(n0 − kx); Maximum x* = (0,1 n0 − k p0)/(0,2 k)
    xs = (Fr(n0, 10) - k * p0) / (Fr(2, 10) * k)
    if xs.denominator != 1 or xs <= 0: return None
    E = (p0 + Fr(xs, 10)) * (n0 - k * xs)
    return zahl(f'Ein Kiosk verkauft täglich {n0} Brezen zu je {eur(p0)} €. Jede Preiserhöhung um 10 ct kostet {k} Käufer. Wie viele Erhöhungen um 10 ct bringen die größten Einnahmen?',
                f'E(x) = ({eur(p0)} + 0,1x)({n0} − {k}x) = {poly(-Fr(k, 10), Fr(n0, 10) - k * p0, p0 * n0)}. '
                f'Quadratische Ergänzung: Maximum für x = {dz(xs)} (Einnahmen {eur(E)} €).',
                'Einnahmen = Preis · Anzahl. Beides hängt von der Zahl x der Erhöhungen ab.', xs, f'({n0} / 10 - {k} * {p0}) / (0.2 * {k})')


GEN = {'ergaenzen': g_ergaenzen, 'scheitelform': g_scheitelform, 'extremwert': g_extremwert,
       'mit_faktor': g_mit_faktor, 'optimierung': g_optimierung}

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import tab  # noqa: E402

_P = {'_a': [0, 0], '_b': [5, 0], '_c': [8, 0], '_d': [8, 5], '_e': [8, 8], '_f': [5, 8], '_g': [0, 8], '_h': [0, 5], '_m': [5, 5]}
_L = [['_a', '_b', 'x'], ['_b', '_c', '3'], ['_c', '_d'], ['_d', '_m'], ['_m', '_f'], ['_f', '_g'], ['_g', '_h', '3'], ['_h', '_a', 'x'],
      ['_b', '_m'], ['_h', '_m']]


def _t(*zeilen):
    return tab(['', 'Term'], *zeilen)


_SF = [['Start', 'x² − 8x + 21'], ['+ 16 − 16', 'x² − 8x + 16 − 16 + 21'], ['Quadrat', '(x − 4)² − 16 + 21'], ['fertig', '(x − 4)² + 5']]
_MF = [['Start', '2x² − 12x + 23'], ['2 ausklammern', '2(x² − 6x) + 23'], ['ergänzen', '2(x² − 6x + 9 − 9) + 23'],
       ['−9 herausholen', '2(x − 3)² − 18 + 23'], ['fertig', '2(x − 3)² + 5']]
_X = ['−4', '−3', '−2', '−1', '0']


def _rechteck(a, b, ta, tb):
    return {'typ': 'figur', 'punkte': {'_A': [0, 0], '_B': [a, 0], '_C': [a, b], '_D': [0, b]}, 'flaeche': ['_A', '_B', '_C', '_D'],
            'linien': [['_A', '_B', ta], ['_B', '_C', tb], ['_C', '_D'], ['_D', '_A']]}


UMBAU = {
    'ergaenzen': {
        'einstieg': 'Ein quadratisches Beet hat die Seite x. An zwei Seiten kommt je ein Streifen der Breite 3 dazu. '
                    'Zum großen Quadrat fehlt nur eine Ecke. Sie dazuzunehmen heißt ⟦quadratisch ergänzen⟧.',
        'woerter': [['vollständiges Quadrat', 'ein Term wie (x + 3)², also eine Klammer hoch 2'],
                    ['quadratisch ergänzen', 'die fehlende Ecke (b : 2)² dazuzählen']],
        'bild': {'typ': 'figur', 'punkte': _P, 'linien': _L},
        'schritte': [
            {'text': 'x² + 6x sind das Quadrat x · x und zwei Streifen 3 · x.'},
            {'text': 'Die Hälfte von 6 ist 3, die Ecke hat 3 · 3 = 9.',
             'bild': {'linien': _L + [['_d', '_e'], ['_e', '_f']], 'flaeche': ['_m', '_d', '_e', '_f']}},
            {'text': 'x² + 6x + ⟦9⟧ = ⟦(x + 3)²⟧, ein vollständiges Quadrat.'},
        ],
        'fehler': 'x² + 6x + 36 = (x + 6)² ist falsch. In die Klammer gehört die ⟦Hälfte⟧ von 6, die Ecke ist nur 3 · 3 = 9.',
        'regel': 'Bei x² + bx ergänzt du ⟦(b : 2)²⟧. Dann ist x² + bx + (b : 2)² = (x + b : 2)².',
    },
    'scheitelform': {
        'einstieg': 'Beim Fliesenlegen leihst du dir 16 Fliesen für die Ecke und gibst sie gleich zurück. '
                    'Insgesamt ändert sich nichts, aber du siehst ein fertiges Quadrat. So funktioniert die ⟦quadratische Ergänzung⟧.',
        'woerter': [['quadratische Ergänzung', '(b : 2)² dazuzählen und gleich wieder abziehen']],
        'bild': _t(_SF[0]),
        'schritte': [
            {'text': 'Die Hälfte von −8 ist −4, und (−4)² = 16.'},
            {'text': '16 dazu und gleich wieder weg: x² − 8x + 16 − 16 + 21.', 'bild': _t(*_SF[:2])},
            {'text': 'Die ersten drei Glieder sind (x − 4)².', 'bild': _t(*_SF[:3])},
            {'text': 'Zusammenfassen: −16 + 21 = 5, also ⟦(x − 4)² + 5⟧.', 'bild': _t(*_SF)},
        ],
        'fehler': '(x − 4)² + 21 ist falsch. Die geliehene 16 muss auch ⟦zurück⟧, sonst ist der Term um 16 zu groß.',
        'fehler_bild': _t(_SF[0], ['falsch', '(x − 4)² + 21'], ['richtig', '(x − 4)² − 16 + 21']),
        'regel': 'Ergänzen und gleich wieder abziehen. So entsteht ⟦(x + b : 2)² − (b : 2)² + c⟧, der Wert bleibt gleich.',
    },
    'extremwert': {
        'einstieg': 'Ein Quadrat ist nie negativ: 3² = 9, (−3)² = 9, 0² = 0. Darum hat (x + 2)² − 7 einen kleinsten Wert. '
                    'Er heißt ⟦Minimum⟧.',
        'woerter': [['Minimum', 'der kleinste Wert, den der Term annehmen kann'],
                    ['Maximum', 'der größte Wert; es gibt ihn bei einem Minus vor der Klammer']],
        'bild': tab(['x', *_X], ['T(x)', '?', '?', '?', '?', '?']),
        'schritte': [
            {'text': 'T(x) = (x + 2)² − 7. Die Klammer ist 0 für x = −2.'},
            {'text': 'Dann ist T = 0 − 7 = −7.', 'bild': tab(['x', *_X], ['T(x)', '?', '?', '−7', '?', '?'])},
            {'text': 'Für jedes andere x kommt etwas Positives dazu.', 'bild': tab(['x', *_X], ['T(x)', '−3', '−6', '−7', '−6', '−3'])},
            {'text': 'Minimum: ⟦T = −7 für x = −2⟧.'},
            {'text': 'Mit Minus vor der Klammer, −(x + 2)² − 7, wäre −7 das Maximum.'},
        ],
        'fehler': 'Bei (x + 2)² − 7 liegt das Minimum nicht bei x = 2. Die Klammer wird null für ⟦x = −2⟧.',
        'regel': 'Die Klammer null setzen: Dort liegt das Extremum. Plus vor der Klammer heißt ⟦Minimum⟧, Minus heißt Maximum.',
    },
    'mit_faktor': {
        'einstieg': 'Steht vor x² eine Zahl wie 2, stört sie beim Ergänzen. Darum ziehst du sie zuerst vor eine Klammer. '
                    'Das heißt ⟦ausklammern⟧. Danach ergänzt du in der Klammer wie gewohnt.',
        'woerter': [['ausklammern', 'einen gemeinsamen Faktor vor eine Klammer ziehen: 2x² − 12x = 2(x² − 6x)']],
        'bild': _t(_MF[0]),
        'schritte': [
            {'text': '2 ausklammern: 2x² − 12x + 23 = 2(x² − 6x) + 23.', 'bild': _t(*_MF[:2])},
            {'text': 'In der Klammer ergänzen: 2(x² − 6x + 9 − 9) + 23.', 'bild': _t(*_MF[:3])},
            {'text': 'Die −9 mal 2 herausholen: 2(x − 3)² − 18 + 23.', 'bild': _t(*_MF[:4])},
            {'text': 'Ergebnis: ⟦2(x − 3)² + 5⟧, also Minimum ⟦T = 5 für x = 3⟧.', 'bild': _t(*_MF)},
        ],
        'fehler': '−9 + 23 ist hier falsch. Die −9 steht in der Klammer und wird ⟦mit 2 malgenommen⟧: −18 + 23 = 5.',
        'fehler_bild': _t(_MF[2], ['falsch', '2(x − 3)² − 9 + 23'], ['richtig', '2(x − 3)² − 18 + 23']),
        'regel': 'Erst den Faktor vor x² ausklammern, dann ergänzen. Faktor positiv: ⟦Minimum⟧, Faktor negativ: Maximum.',
    },
    'optimierung': {
        'einstieg': 'Mit 20 m Zaun soll ein rechteckiges Gehege möglichst groß werden. Ist ein langes, schmales besser oder ein Quadrat? '
                    'Solche Aufgaben heißen ⟦Optimierungsaufgaben⟧.',
        'woerter': [['Optimierungsaufgabe', 'gesucht ist das Beste: möglichst groß oder möglichst klein'],
                    ['Umfang', 'Länge des Zauns rund um das Rechteck']],
        'bild': _rechteck(7, 3, 'x', '10 − x'),
        'schritte': [
            {'text': 'Umfang 20 m: Eine Seite ist x, die andere 10 − x.'},
            {'text': 'Fläche: A(x) = x · (10 − x) = −x² + 10x.'},
            {'text': 'Ergänzen: −x² + 10x = −(x − 5)² + 25.'},
            {'text': '⟦Maximum 25 m² für x = 5 m⟧: ein Quadrat.', 'bild': _rechteck(5, 5, '5 m', '5 m')},
        ],
        'fehler': '25 ist hier die Fläche, nicht die Seite. Lies genau, was gefragt ist: die ⟦Stelle x⟧ oder der ⟦Extremwert⟧.',
        'regel': 'Zielgröße als Term in x aufstellen, dann ergänzen. Antwort im ⟦Sachzusammenhang⟧ geben: Stelle oder Wert?',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-1) ----------
# Prüfungsvorbilder: Realschul-Abschlussprüfung Mathematik I (Bayern) – Flächeninhalt A(x) einer Figur in Abhängigkeit von x,
# dann „Berechnen Sie den maximalen/kleinstmöglichen Flächeninhalt“ (z. B. AP 2004 A 1.5, AP 2011 B 2.4); Jahrgangsstufentest 8 I
# (Lücken in binomischen Formeln ergänzen). Typ übernommen, Wortlaut und Zahlen eigen.
def durchsicht(d):
    from _rsib1 import Z, A, L, nachtrag, finde
    T = lambda teil: finde(d, teil)
    XT = 'x = □; T = □'
    nachtrag(d,
        umstufen={
            T('Welche Zahl musst du zu x² + 14x addieren'): 1,
            T('Multipliziere T(x) = (x − 6)² − 12 aus.'): 2,
            T('Multipliziere T(x) = (x − 6)² − 5 aus.'): 2,
            T('Multipliziere T(x) = (x + 5)² + 8 aus.'): 2,
            T('Hat T(x) = −4x² − 32x − 65 ein Minimum oder ein Maximum?'): 1,
            T('Hat T(x) = 3x² + 12x + 17 ein Minimum oder ein Maximum?'): 1,
            T('Die Summe zweier Zahlen ist 18.'): 1,
            T('Die Summe zweier Zahlen ist 8.'): 1,
            T('Ein Kiosk verkauft täglich 200 Brezen'): 2,
        },
        ersetzen={
            T('T(x) = x² + 3x − 4. Welchen kleinsten Wert'):
                Z(3, 'Bringe T(x) = x² + 3x + 1 in die Form (x + d)² + e. Gib e als Dezimalzahl an.',
                  -1.25, '1 - (3/2)**2', 'Hälfte von 3 ist 1,5; 1,5² = 2,25. T(x) = (x + 1,5)² − 2,25 + 1 = (x + 1,5)² − 1,25.',
                  'Ergänze (3 : 2)² = 2,25 und ziehe es gleich wieder ab.'),
            T('T(x) = x² − x + 4,5. Welchen kleinsten Wert'):
                L(3, 'Ergänze die Lücken: (x + □)² + 3 = x² + 8x + □.', '(x + □)² + 3 = x² + 8x + □', [4, 19], ['8/2', '4**2 + 3'],
                  '8x kommt von 2 · 4 · x, also steht 4 in der Klammer. 4² = 16, dazu 3: 19.',
                  'Wie entsteht das 8x beim Ausmultiplizieren?'),
            T('T(x) = x² + 7x + 15. Welchen kleinsten Wert'):
                A(3, 'Jemand formt um: x² − 10x + 7 = (x − 5)² + 32. Was stimmt?',
                  'Falsch: Die 25 muss abgezogen werden, richtig ist (x − 5)² − 18.',
                  ['Richtig.', 'Falsch: Richtig ist (x − 10)² + 7.', 'Falsch: Richtig ist (x + 5)² − 18.'],
                  'x² − 10x + 25 − 25 + 7 = (x − 5)² − 18. Er hat die 25 addiert statt abgezogen.',
                  'Rechne die Klammer zur Probe aus.'),
        },
        neu={
            'ergaenzen': [
                L(3, 'Ergänze die Lücken so, dass die Gleichung stimmt.', 'x² − □x + 49 = (x − □)²', [14, 7], ['2*7', '7'],
                  '49 = 7², also steht 7 in der Klammer. Das mittlere Glied ist 2 · 7 · x = 14x.',
                  'Welche Zahl ergibt im Quadrat 49?'),
                L(3, 'Ergänze die Lücken so, dass ein vollständiges Quadrat entsteht.', '4x² + 12x + □ = (2x + □)²', [9, 3], ['3**2', '12/(2*2)'],
                  '(2x + b)² = 4x² + 4bx + b². 4b = 12, also b = 3 und b² = 9.',
                  'Multipliziere (2x + b)² aus und vergleiche.'),
                Z(3, 'Um wie viel ist x² + 10x + 30 größer als das vollständige Quadrat (x + 5)²?',
                  5, '30 - 5**2', '(x + 5)² = x² + 10x + 25. 30 − 25 = 5.', 'Multipliziere (x + 5)² aus.'),
            ],
            'scheitelform': [
                Z(3, 'Es gilt x² + 6x + c = (x + 3)² + 2. Wie groß ist c?', 11, '3**2 + 2',
                  '(x + 3)² + 2 = x² + 6x + 9 + 2 = x² + 6x + 11. Also c = 11.', 'Multipliziere die rechte Seite aus.'),
                A(3, 'Warum ist x² − 4x + 7 für jedes x positiv?',
                  'Weil x² − 4x + 7 = (x − 2)² + 3 und (x − 2)² nie negativ ist.',
                  ['Weil 7 positiv ist.', 'Weil x² immer größer als 4x ist.', 'Das stimmt nicht, für x = 4 wird es negativ.'],
                  'Quadratische Ergänzung: (x − 2)² + 3. Ein Quadrat ist mindestens 0, also ist der Term mindestens 3.',
                  'Bringe den Term in die Form (x − d)² + e.'),
                A(3, 'Welcher Term lässt sich als (x − 2)² − 1 schreiben?',
                  'x² − 4x + 3', ['x² − 4x − 1', 'x² + 4x + 3', 'x² − 2x − 1'],
                  '(x − 2)² − 1 = x² − 4x + 4 − 1 = x² − 4x + 3.', 'Multipliziere aus.'),
                A(3, 'Sind (x + 2)² + 1 und x² + 4x + 5 derselbe Term?',
                  'Ja, für jedes x gleich.', ['Nein, nur für x = 0 gleich.', 'Nein, sie unterscheiden sich um 4.', 'Nein, sie unterscheiden sich um 1.'],
                  '(x + 2)² + 1 = x² + 4x + 4 + 1 = x² + 4x + 5. Die Terme sind gleich.', 'Multipliziere den ersten Term aus.'),
                Z(3, 'Bringe x² − 5x in die Form (x − d)² − e. Gib e als Dezimalzahl an.',
                  6.25, '(5/2)**2', 'Hälfte von 5 ist 2,5; 2,5² = 6,25. x² − 5x = (x − 2,5)² − 6,25.',
                  'Die Hälfte von 5 ist eine Dezimalzahl.'),
            ],
            'extremwert': [
                Z(3, 'Für welches c hat T(x) = x² − 6x + c den kleinsten Wert 4?', 13, '4 + 3**2',
                  'T(x) = (x − 3)² − 9 + c. Kleinster Wert −9 + c = 4 ⇒ c = 13.', 'Ergänze quadratisch und lasse c stehen.'),
                A(3, 'Gibt es ein x, für das (x − 2)² + 5 den Wert 3 hat?',
                  'Nein, der kleinste Wert ist 5.', ['Ja, für x = 0.', 'Ja, für x = 2.', 'Ja, für x = −2.'],
                  '(x − 2)² ist nie negativ, also ist der Term immer mindestens 5. Der Wert 3 wird nie erreicht.',
                  'Welchen kleinsten Wert hat der Term?'),
            ],
            'mit_faktor': [
                Z(3, 'Der Term T(x) = a · x² − 8x + 3 hat sein Extremum bei x = 2. Wie groß ist a?', 2, '8/(2*2)',
                  'a ausklammern: a(x² − (8 : a)x) + 3. Das Extremum liegt bei x = (8 : a) : 2 = 4 : a. 4 : a = 2 ⇒ a = 2. Probe: 2x² − 8x + 3 = 2(x − 2)² − 5.',
                  'Bei a(x − d)² liegt das Extremum bei d. Wie hängt d mit 8 und a zusammen?'),
                L(3, 'Für den Flächeninhalt von Dreiecken gilt A(x) = (−0,5x² + 4x + 6) FE. Für welches x ist A maximal, und wie groß ist A dann?',
                  'x = □; A = □ FE', [4, 14], ['4/(2*0.5)', '6 + 0.5*4**2'],
                  '−0,5(x² − 8x) + 6 = −0,5(x − 4)² + 8 + 6 = −0,5(x − 4)² + 14. Maximum 14 FE für x = 4.',
                  'Klammere −0,5 aus und ergänze.'),
                A(3, 'Welcher der Terme 2x² − 8x + 1 und −2x² + 8x + 1 hat ein Maximum, und wo liegt es?',
                  '−2x² + 8x + 1, bei x = 2', ['2x² − 8x + 1, bei x = 2', '−2x² + 8x + 1, bei x = −2', 'beide, bei x = 2'],
                  'Negativer Faktor vor x² ⇒ Maximum. −2(x² − 4x) + 1 = −2(x − 2)² + 9: Maximum 9 bei x = 2.',
                  'Welches Vorzeichen hat der Faktor vor x²?'),
                A(3, 'Für welche c hat T(x) = 2x² − 12x + c ein negatives Minimum?',
                  'für c < 18', ['für c < 9', 'für c < 36', 'für c > 18'],
                  '2(x − 3)² − 18 + c. Minimum −18 + c < 0 ⇒ c < 18.', 'Ergänze und lasse c stehen.'),
            ],
            'optimierung': [
                Z(3, 'Ein Rechteck hat die Seitenlängen (10 − x) cm und (2x + 2) cm. Für welches x ist der Flächeninhalt maximal?',
                  4.5, '18/4', 'A(x) = (10 − x)(2x + 2) = −2x² + 18x + 20 = −2(x − 4,5)² + 60,5. Maximum für x = 4,5.',
                  'Multipliziere aus und ergänze quadratisch.', einheit='cm'),
                Z(3, 'Ein Rechteck hat die Seitenlängen (10 − x) cm und (2x + 2) cm. Wie groß ist der maximale Flächeninhalt?',
                  60.5, '(10 - 4.5)*(2*4.5 + 2)', 'A(x) = −2(x − 4,5)² + 60,5. Für x = 4,5: 5,5 cm · 11 cm = 60,5 cm².',
                  'Bestimme zuerst die Stelle des Maximums.', einheit='cm²'),
                Z(3, 'Ein Kino hat 120 Gäste bei 8 € Eintritt. Jede Senkung um 0,50 € bringt 10 Gäste mehr. Bei welchem Eintrittspreis sind die Einnahmen am größten?',
                  7, '8 - 0.5*2', 'n Senkungen: E = (8 − 0,5n)(120 + 10n) = −5n² + 20n + 960 = −5(n − 2)² + 980. n = 2: Preis 8 − 1 = 7 €.',
                  'Stelle die Einnahmen für n Senkungen auf.', einheit='€'),
                Z(3, 'Die Summe zweier Zahlen ist 12. Wie groß ist die Summe ihrer Quadrate mindestens?',
                  72, '6**2 + 6**2', 'x² + (12 − x)² = 2x² − 24x + 144 = 2(x − 6)² + 72. Kleinster Wert 72 für x = 6.',
                  'Die zweite Zahl ist 12 − x. Stelle x² + (12 − x)² auf.'),
                Z(3, 'In einer Hausecke soll mit 30 m Zaun ein rechteckiges Beet entstehen. Zwei Seiten bilden die Hauswände, der Zaun die anderen zwei. Wie groß kann das Beet höchstens werden?',
                  225, '15*15', 'Seiten x und 30 − x. A = x(30 − x) = −(x − 15)² + 225. Maximum 225 m².',
                  'Der Zaun bildet nur zwei Seiten.', einheit='m²'),
            ],
        })


# ---- STUFEN (Zwanzigste Runde, Zusatz RS/IB, Zweig stufen-rsib-1) ----
from _stufen_rsib1 import Stufen, stufen  # noqa: E402

ST = Stufen('terme.quadratische_extreme', 20_81_5)
Z, A, L = ST.Z, ST.A, ST.L

# ergaenzen
ST.stufenleiter('ergaenzen', 'x² + bx mit gerader Zahl b zu einem Binom ergänzen und ein Binom erkennen.',
                'Mit negativem b und ungeradem b (Dezimalzahl) ergänzen, ein Binom als Klammerquadrat schreiben, Eckquadrat am Bild bestimmen.',
                'Vom Binom zurück auf den mittleren Term, Faktor vor x², Abstand zum Binom, Fehler „b statt b/2“, b für ein Binom bestimmen, Nichtnegativität begründen, Prüfungsaufgabe.')
ST.typ('ergaenzen', 'Ergänze zu einem vollständigen Quadrat', 'direkt')
ST.typ('ergaenzen', 'Welche Zahl musst du zu', 'erkennen')
ST.typ('ergaenzen', 'Ergänze so, dass ein Binom', 'mehrschritt')
ST.typ('ergaenzen', 'Welche Zahl muss man zu', 'mehrschritt')
ST.typ('ergaenzen', 'Schreibe x² + 10x + 25', 'umkehr')
ST.typ('ergaenzen', 'Jemand schreibt', 'fehler')
ST.typ('ergaenzen', 'Ergänze die Lücken so, dass die Gleichung', 'rueckwaerts')
ST.typ('ergaenzen', 'Ergänze die Lücken so, dass ein vollständiges', 'transfer')
ST.typ('ergaenzen', 'Um wie viel ist', 'verknuepfen')
ST.neu('ergaenzen', 'erkennen', A('Welcher Term ist ein vollständiges Quadrat (ein Binom)?', 'x² + 12x + 36', ['x² + 12x + 12', 'x² + 6x + 36', 'x² + 12x + 144'],
       'x² + 12x + 36 = (x + 6)², denn die Hälfte von 12 ist 6 und 6² = 36.', 'Halbiere die Zahl vor x und quadriere.'))
ST.neu('ergaenzen', 'darstellung', Z('Ein Quadrat mit der Seite x wird um zwei Streifen mit je x · 5 ergänzt (Fläche x² + 10x). Wie groß ist das Eckquadrat, das zum großen Quadrat noch fehlt?', 25, '5 * 5',
       'Die Streifen sind 5 breit. Das fehlende Eckquadrat hat die Seite 5, also 25. Dann ist x² + 10x + 25 = (x + 5)².', 'Wie breit sind die Streifen?'))
ST.neu('ergaenzen', 'begruenden', A('Stimmt: x² + 6x + 9 ist für jedes x mindestens 0?', 'Ja, denn x² + 6x + 9 = (x + 3)², und ein Quadrat ist nie negativ.',
       ['Nein, für negative x wird es negativ.', 'Nur für x > 0.', 'Nein, für x = −3 ist es negativ.'], '(x + 3)² ≥ 0. Für x = −3 ist der Term genau 0, sonst positiv.', 'Schreibe den Term als Quadrat.'))
ST.neu('ergaenzen', 'parameter', L('Für welche Zahlen b ist x² + bx + 16 ein vollständiges Quadrat?', 'b₁ = □; b₂ = □', [-8, 8], ['-8', '8'],
       '16 = 4². (x + 4)² = x² + 8x + 16 und (x − 4)² = x² − 8x + 16. Also b = 8 oder b = −8.', 'Welche Zahl ergibt quadriert 16?'))
ST.neu('ergaenzen', 'pruefung', L('a) Welche Zahl musst du zu x² + 14x addieren, damit ein Binom entsteht? b) Schreibe das Binom als Quadrat. c) Welchen Wert hat es für x = −7?', 'a) □; b) (x + □)²; c) □', [49, 7, 0],
       ['7 * 7', '7', '0'], 'a) (14 : 2)² = 49. b) x² + 14x + 49 = (x + 7)². c) (−7 + 7)² = 0.', 'Halbieren, quadrieren.'))
ST.knobel('ergaenzen', Z('Berechne 47² im Kopf, indem du 47 = 50 − 3 nutzt.', 2209, '50 * 50 - 2 * 50 * 3 + 3 * 3',
          '(50 − 3)² = 50² − 2 · 50 · 3 + 3² = 2 500 − 300 + 9 = 2 209.', 'Binomische Formel mit Minus.'))
ST.knobel('ergaenzen', Z('Wie viele ganze Zahlen x erfüllen x² − 10x + 25 < 4?', 3, '3',
          'x² − 10x + 25 = (x − 5)². (x − 5)² < 4 heißt: x − 5 liegt zwischen −2 und 2 (ohne die Grenzen). Ganze Zahlen: x = 4, 5, 6. Also 3.', 'Erkenne das Binom.'))

# scheitelform
ST.stufenleiter('scheitelform', 'x² + bx + c mit quadratischer Ergänzung in die Form (x + d)² + e bringen; passende Form erkennen.',
                'Ungerade b mit Dezimalzahlen, Scheitelform ausmultiplizieren, c aus der Scheitelform, Term zu einer Wertetabelle.',
                'Lücken rückwärts füllen, Fehler bei b/2 und beim Abziehen finden, Positivität und Gleichheit begründen, Bedingung an c, Fontäne als Modell, Prüfungsaufgabe.')
ST.typ('scheitelform', '/^Bringe (T\\(x\\) = x² \\+ 3x|x² − 5x)/', 'mehrschritt')
ST.typ('scheitelform', 'Bringe T(x) = x²', 'direkt')
ST.typ('scheitelform', 'Welcher Term lässt sich', 'erkennen')
ST.typ('scheitelform', 'Multipliziere', 'umkehr')
ST.typ('scheitelform', 'Es gilt x² + 6x + c', 'umkehr')
ST.typ('scheitelform', 'Ergänze die Lücken', 'rueckwaerts')
ST.typ('scheitelform', 'Jemand formt um', 'fehler')
ST.typ('scheitelform', '/^(Warum ist|Sind \\()/', 'begruenden')
ST.neu('scheitelform', 'erkennen', A('Welche Zahl wird bei x² − 6x + 10 ergänzt und gleich wieder abgezogen?', '9', ['6', '36', '3'],
       'Die Hälfte von −6 ist −3, (−3)² = 9: x² − 6x + 9 − 9 + 10 = (x − 3)² + 1.', 'Halbieren, quadrieren.'))
ST.neu('scheitelform', 'darstellung', A('Eine Wertetabelle: x = 0, 1, 2, 3 ergibt T(x) = 5, 2, 1, 2. Welcher Term passt?', '(x − 2)² + 1', ['(x + 2)² + 1', '(x − 1)² + 2', '(x − 2)² − 1'],
       'Der kleinste Wert 1 liegt bei x = 2, links und rechts davon ist es symmetrisch. Probe: (0 − 2)² + 1 = 5, (3 − 2)² + 1 = 2.', 'Wo ist der kleinste Wert in der Tabelle?'))
ST.neu('scheitelform', 'fehler', A('Jemand formt x² + 8x + 3 um zu (x + 8)² − 61. Was stimmt?', 'Falsch: Man nimmt die Hälfte von 8: (x + 4)² − 13.',
       ['Richtig.', 'Falsch: (x + 4)² + 3.', 'Falsch: (x + 8)² + 3.'], 'Ergänzt wird (8 : 2)² = 16: x² + 8x + 16 − 16 + 3 = (x + 4)² − 13. Mit (x + 8)² stünde 16x statt 8x da.', 'Multipliziere (x + 8)² zur Probe aus.'))
ST.neu('scheitelform', 'parameter', A('Für welche Zahlen c ist x² + 4x + c für jedes x positiv?', 'für c > 4', ['für c > 0', 'für c > 2', 'für c < 4'],
       'x² + 4x + c = (x + 2)² + c − 4. Der kleinste Wert ist c − 4 (bei x = −2). Er ist positiv, wenn c > 4.', 'Bringe den Term in die Scheitelform.'))
ST.neu('scheitelform', 'transfer', Z('Ein Wasserstrahl hat die Höhe h(x) = −x² + 6x + 1 (alles in dm, x ist der waagrechte Abstand). Wie hoch steigt der Strahl höchstens?', 10, '9 + 1',
       '−x² + 6x + 1 = −(x² − 6x + 9) + 9 + 1 = −(x − 3)² + 10. Höchste Höhe 10 dm bei x = 3 dm.', 'Klammere das Minus vor x² aus und ergänze.', einheit='dm'))
ST.neu('scheitelform', 'pruefung', L('Gegeben ist T(x) = x² − 10x + 21. a) Bringe T in die Form (x + d)² + e. b) Für welches x ist die Klammer 0? c) Welchen Wert hat T dann?',
       'a) d = □; e = □; b) □; c) □', [-5, -4, 5, -4], ['-5', '21 - 25', '5', '0 - 4'],
       'a) x² − 10x + 25 − 25 + 21 = (x − 5)² − 4: d = −5, e = −4. b) x = 5. c) T(5) = −4.', 'Hälfte von −10 ist −5.'))
ST.knobel('scheitelform', Z('Für welches x wird (x − 3)² + (x − 5)² am kleinsten?', 4, '4',
          'Ausmultiplizieren: 2x² − 16x + 34 = 2(x² − 8x + 16) + 2 = 2(x − 4)² + 2. Am kleinsten für x = 4 – genau in der Mitte zwischen 3 und 5.', 'Multipliziere aus und ergänze.'))
ST.knobel('scheitelform', L('Welche Zahlen x und y erfüllen x² + y² − 6x + 4y + 13 = 0?', 'x = □; y = □', [3, -2], ['3', '-2'],
          'Ergänzen: (x² − 6x + 9) + (y² + 4y + 4) = 0, also (x − 3)² + (y + 2)² = 0. Zwei Quadrate ergeben nur 0, wenn beide 0 sind: x = 3, y = −2.', 'Ergänze für x und für y getrennt.'))

# extremwert
ST.stufenleiter('extremwert', 'An (x − d)² + e bzw. −(x − d)² + e Stelle und Wert des Extremums ablesen; Minimum oder Maximum erkennen.',
                'Erst ergänzen, dann ablesen; Parameter aus einem Extremwert; Gewinn als Sachsituation; Extremum aus einer Wertetabelle.',
                'Größter Wert existiert nicht – begründen, Aussagen über Schranken prüfen, Fehler beim Vorzeichen in der Klammer, Bedingung für ein Maximum, Temperaturverlauf, Prüfungsaufgabe.')
ST.typ('extremwert', 'Bestimme Stelle und Wert des Extremums', 'direkt')
ST.typ('extremwert', 'Hat T(x)', 'erkennen')
ST.typ('extremwert', '/^Bestimme Stelle und Wert des (Minimums|Maximums)/', 'mehrschritt')
ST.typ('extremwert', 'Für welches c hat', 'umkehr')
ST.typ('extremwert', 'Für welches x ist', 'verknuepfen')
ST.typ('extremwert', '/^(Welche Aussage|Gibt es ein x)/', 'begruenden')
ST.neu('extremwert', 'einkleidung', Z('Der Gewinn eines Standes ist G(x) = −(x − 30)² + 400 Euro, wenn x der Preis in Cent ist. Bei welchem Preis ist der Gewinn am größten?', 30, '30',
       'Die Klammer ist 0 für x = 30. Dann ist G = 400 € der größte Gewinn, weil sonst etwas abgezogen wird.', 'Wann wird nichts abgezogen?', einheit='ct'))
ST.neu('extremwert', 'darstellung', A('Eine Wertetabelle: x = 1, 2, 3, 4, 5 ergibt T(x) = 6, 3, 2, 3, 6. Wo liegt das Extremum?', 'Minimum 2 bei x = 3', ['Maximum 6 bei x = 1', 'Minimum 3 bei x = 2', 'Maximum 2 bei x = 3'],
       'Die Werte sind symmetrisch um x = 3 und dort am kleinsten: Minimum T = 2.', 'Suche den kleinsten Wert und die Symmetrie.'))
ST.neu('extremwert', 'umkehr', Z('T(x) = (x − d)² + 5 hat sein Minimum bei x = −2. Wie groß ist d?', -2, '-2',
       'Die Klammer ist 0 für x = d. Das Minimum liegt bei x = d = −2. Probe: (x + 2)² + 5.', 'Für welches x wird die Klammer null?'))
ST.neu('extremwert', 'fehler', A('Jemand liest bei T(x) = (x + 3)² − 2 ab: „Minimum −2 bei x = 3.“ Was stimmt?', 'Falsch: Die Klammer ist für x = −3 null, also Minimum −2 bei x = −3.',
       ['Richtig.', 'Falsch: Maximum −2 bei x = 3.', 'Falsch: Minimum 3 bei x = −2.'], 'x + 3 = 0 ⇒ x = −3. Probe: T(3) = 36 − 2 = 34, also kein Minimum.', 'Setze x = 3 zur Probe ein.'))
ST.neu('extremwert', 'parameter', A('Für welche Zahlen a hat T(x) = a · (x − 1)² + 4 ein Maximum?', 'für a < 0', ['für a > 0', 'für a > 4', 'für jedes a ≠ 0'],
       'Ist a negativ, wird von 4 immer etwas abgezogen (außer bei x = 1): Maximum 4. Ist a positiv, kommt etwas dazu: Minimum.', 'Wird etwas dazugezählt oder abgezogen?'))
ST.neu('extremwert', 'transfer', Z('Die Temperatur in einem Gewächshaus ist T(t) = −(t − 14)² + 30 (in °C, t = Uhrzeit in Stunden). Um wie viel Grad ist es um 17 Uhr kälter als zur wärmsten Zeit?', 9, '(17 - 14) ** 2',
       'Am wärmsten um 14 Uhr: 30 °C. Um 17 Uhr: −(17 − 14)² + 30 = −9 + 30 = 21 °C. Unterschied 9 Grad.', 'Wann ist es am wärmsten?', einheit='°C'))
ST.neu('extremwert', 'pruefung', L('Gegeben ist T(x) = x² + 6x + 2. a) Bringe T in die Form (x + d)² + e. b) Gib Stelle und Wert des Minimums an.', 'a) d = □; e = □; b) x = □; T = □', [3, -7, -3, -7],
       ['3', '2 - 9', '-3', '-7'], 'a) x² + 6x + 9 − 9 + 2 = (x + 3)² − 7. b) Minimum −7 bei x = −3.', 'Erst ergänzen, dann ablesen.'))
ST.knobel('extremwert', Z('Welchen größten Wert hat 1 : ((x − 2)² + 4)?', 0.25, '1 / 4',
          'Ein Bruch mit Zähler 1 ist am größten, wenn der Nenner am kleinsten ist. (x − 2)² + 4 ist mindestens 4 (bei x = 2). Größter Wert 1 : 4 = 0,25.', 'Wann ist ein Bruch mit Zähler 1 am größten?'))
ST.knobel('extremwert', Z('x darf nur ganze Zahlen annehmen. Welchen kleinsten Wert hat dann (x − 2,5)² + 1?', 1.25, '0.5 * 0.5 + 1',
          'Das Minimum 1 läge bei x = 2,5 – das ist keine ganze Zahl. Am nächsten liegen 2 und 3, beide mit Abstand 0,5: (0,5)² + 1 = 1,25.', 'Welche ganzen Zahlen liegen nah an 2,5?'))

# mit_faktor
ST.stufenleiter('mit_faktor', 'Bei a · x² + bx + c den Faktor a ausklammern, ergänzen und das Extremum angeben; Minimum oder Maximum am Vorzeichen von a erkennen.',
                'Negative und gebrochene Faktoren, Faktor a aus der Lage des Extremums, Flächeninhalt als Term.',
                'Fehler „Ausgleich nicht mit a malgenommen“, Lage des Extremums vergleichen, Bedingung an c, c aus dem Minimum zurück, Stückkosten als Modell, Prüfungsaufgabe.')
ST.typ('mit_faktor', '/^Bestimme Stelle und Wert des Extremums von T\\(x\\) = (−|0,5)/', 'mehrschritt')
ST.typ('mit_faktor', 'Bestimme Stelle und Wert des Extremums', 'direkt')
ST.typ('mit_faktor', 'Hat T(x)', 'erkennen')
ST.typ('mit_faktor', 'Der Term T(x) = a', 'umkehr')
ST.typ('mit_faktor', 'Für den Flächeninhalt', 'einkleidung')
ST.typ('mit_faktor', 'Jemand formt', 'fehler')
ST.typ('mit_faktor', 'Welcher der Terme', 'begruenden')
ST.typ('mit_faktor', 'Für welche c', 'parameter')
ST.neu('mit_faktor', 'rueckwaerts', Z('Der Term T(x) = 2x² − 12x + c hat das Minimum 3. Wie groß ist c?', 21, '3 + 18',
       '2x² − 12x + c = 2(x − 3)² − 18 + c. Minimum: −18 + c = 3 ⇒ c = 21.', 'Ergänze mit c und setze den kleinsten Wert gleich 3.'))
ST.neu('mit_faktor', 'transfer', Z('Die Kosten pro Stück sind K(x) = 0,5x² − 20x + 260 Euro (x in Hundert Stück). Bei welcher Menge sind sie am niedrigsten? Gib x an.', 20, '20 / (2 * 0.5)',
       '0,5(x² − 40x) + 260 = 0,5(x − 20)² − 200 + 260 = 0,5(x − 20)² + 60. Am niedrigsten bei x = 20, also 2 000 Stück, mit 60 € pro Stück.', 'Klammere 0,5 aus.'))
ST.neu('mit_faktor', 'begruenden', A('Stimmt: T(x) = 3x² + 6x + 10 und S(x) = x² + 2x + 10 haben ihr Minimum an derselben Stelle?', 'Ja, beide bei x = −1, aber mit verschiedenen Werten (7 und 9).',
       ['Nein, T hat es bei x = −3.', 'Ja, und beide haben den Wert 10.', 'Nein, T hat ein Maximum.'],
       'T(x) = 3(x² + 2x) + 10 = 3(x + 1)² + 7, S(x) = (x + 1)² + 9. Beide Klammern sind bei x = −1 null.', 'Klammere bei T die 3 aus und vergleiche die Klammern.'))
ST.neu('mit_faktor', 'fehler', A('Jemand bestimmt für T(x) = −2x² + 8x + 1 „das Minimum 9 bei x = 2“. Was stimmt?', 'Falsch: Wegen −2 ist es ein Maximum, 9 bei x = 2.',
       ['Richtig.', 'Falsch: Minimum 1 bei x = 0.', 'Falsch: Maximum 17 bei x = 2.'], '−2(x² − 4x) + 1 = −2(x − 2)² + 8 + 1 = −2(x − 2)² + 9. Der Faktor −2 öffnet nach unten: Maximum.', 'Achte auf das Vorzeichen von a.'))
ST.neu('mit_faktor', 'pruefung', L('Gegeben ist T(x) = −3x² + 12x − 5. Bringe T in die Form a · (x − d)² + e und gib a, d und e an.', 'a = □; d = □; e = □', [-3, 2, 7], ['-3', '2', '12 - 5'],
       '−3(x² − 4x) − 5 = −3(x² − 4x + 4 − 4) − 5 = −3(x − 2)² + 12 − 5 = −3(x − 2)² + 7. Größter Wert 7 bei x = 2.', 'Klammere −3 aus den ersten beiden Gliedern aus.'))
ST.knobel('mit_faktor', L('Für welches x ist das Produkt x · (12 − 2x) am größten, und wie groß ist es dann?', 'x = □; Produkt □', [3, 18], ['3', '3 * 6'],
          'x · (12 − 2x) = −2x² + 12x = −2(x² − 6x) = −2(x − 3)² + 18. Größtes Produkt 18 bei x = 3.', 'Multipliziere aus und ergänze mit Faktor.'))
ST.knobel('mit_faktor', Z('T(x) = a · x² + 4x + 1 (a > 0) hat ein Minimum. Für welches a ist dieses Minimum genau 0?', 4, '4',
          'a(x² + (4/a)x) + 1 = a(x + 2/a)² − 4/a + 1. Minimum 1 − 4/a = 0 ⇒ a = 4. Probe: 4x² + 4x + 1 = (2x + 1)².', 'Ergänze mit dem Buchstaben a.'))

# optimierung
ST.stufenleiter('optimierung', 'Bei Rechtecken mit festem Umfang und Zahlen mit fester Summe das größte Produkt bestimmen; den Flächenterm erkennen.',
                'Feste Differenz, Rechteck an einer Mauer, Preiserhöhung mit weniger Käufern, gesuchte Seitenlänge statt Fläche.',
                'Seitenlängen als Terme, Eintrittspreis, Summe von Quadraten, Hausecke als Modell, Fehler beim halben Umfang, Quadrat als bestes Rechteck begründen, Stallgehege als Prüfungsaufgabe.')
ST.typ('optimierung', 'Ein Rechteck hat den Umfang', 'direkt')
ST.typ('optimierung', 'Die Summe zweier Zahlen ist 30', 'direkt')
ST.typ('optimierung', '/^Die Summe zweier Zahlen ist \\d+\\. Wie groß kann/', 'direkt')
ST.typ('optimierung', '/^(Die Differenz zweier|Ein Kiosk)/', 'mehrschritt')
ST.typ('optimierung', '/^(An einer Mauer|Aus 20 m Zaun)/', 'einkleidung')
ST.typ('optimierung', 'An einer langen Mauer', 'umkehr')
ST.typ('optimierung', 'Ein Rechteck hat die Seitenlängen', 'verknuepfen')
ST.typ('optimierung', '/^(Ein Kino|Die Summe zweier Zahlen ist 12\\. Wie groß ist die Summe|In einer Hausecke)/', 'transfer')
ST.neu('optimierung', 'erkennen', A('Ein Rechteck hat den Umfang 24 cm. Welcher Term beschreibt seine Fläche, wenn eine Seite x cm lang ist?', 'x · (12 − x)', ['x · (24 − x)', '2x + 24', 'x² + 12'],
       'Zwei Seiten zusammen sind der halbe Umfang: 12 cm. Die andere Seite ist 12 − x, die Fläche x · (12 − x).', 'Wie lang sind zwei benachbarte Seiten zusammen?'))
ST.neu('optimierung', 'fehler', A('Jemand rechnet: Umfang 20 m, Seiten x und 20 − x, also größte Fläche 100 m² bei x = 10. Was stimmt?', 'Falsch: Die zweite Seite ist 10 − x; größte Fläche 25 m² bei x = 5.',
       ['Richtig.', 'Falsch: 50 m² bei x = 10.', 'Falsch: 400 m² bei x = 20.'], 'Zwei Seiten sind zusammen der halbe Umfang, 10 m. A = x(10 − x) = −(x − 5)² + 25.', 'Rechne den Umfang deines Rechtecks nach.'))
ST.neu('optimierung', 'begruenden', A('Stimmt: Unter allen Rechtecken mit gleichem Umfang hat das Quadrat die größte Fläche?', 'Ja: A(x) = x · (h − x) mit h = halber Umfang ist bei x = h/2 am größten – dann sind beide Seiten gleich.',
       ['Nein, das längste Rechteck hat die größte Fläche.', 'Nur bei Umfang 20.', 'Nein, alle haben dieselbe Fläche.'],
       'A(x) = −x² + hx = −(x − h/2)² + h²/4. Der größte Wert liegt bei x = h/2, die andere Seite ist dann ebenfalls h/2.', 'Ergänze x · (h − x) mit dem Buchstaben h.'))
ST.neu('optimierung', 'pruefung', L('Ein rechteckiges Gehege wird an eine Stallwand gebaut, 36 m Zaun reichen für die drei übrigen Seiten. x ist die Länge der beiden Seiten senkrecht zur Wand. a) Gib A(x) = □x² + □x an. b) Für welches x ist A maximal? c) Wie groß ist A dann?',
       'a) A(x) = □x² + □x; b) □; c) □', [-2, 36, 9, 162], ['-2', '36', '9', '9 * 18'],
       'a) Die Seite parallel zur Wand ist 36 − 2x: A = x(36 − 2x) = −2x² + 36x. b) −2(x − 9)² + 162 ⇒ x = 9 m. c) A = 162 m².', 'Wie lang ist die Seite parallel zur Wand?'))
ST.knobel('optimierung', Z('Ein 40 cm langer Draht wird in zwei Stücke geteilt, aus jedem wird ein Quadrat gebogen. Wie lang muss das erste Stück sein, damit beide Quadrate zusammen möglichst wenig Fläche haben?', 20, '20',
          'Stücke x und 40 − x, Seiten x/4 und (40 − x)/4. Fläche (x² + (40 − x)²) : 16 = (2x² − 80x + 1 600) : 16 = (2(x − 20)² + 800) : 16. Am kleinsten bei x = 20: zwei gleiche Quadrate mit je 25 cm².',
          'Stelle die Gesamtfläche als Term auf.', einheit='cm'))
ST.knobel('optimierung', Z('Mit 120 m Zaun wird ein Rechteck eingezäunt und durch einen Zaun parallel zu einer Seite in zwei Teile geteilt. Wie groß kann die eingezäunte Fläche höchstens werden?', 600, '20 * 30',
          'Seiten a und b, drei Zaunstücke der Länge b: 2a + 3b = 120 ⇒ a = 60 − 1,5b. A = b(60 − 1,5b) = −1,5b² + 60b = −1,5(b − 20)² + 600. Größte Fläche 600 m² bei b = 20 m, a = 30 m.',
          'Zähle genau, wie viele Zaunstücke welche Länge haben.', einheit='m²'))


if __name__ == '__main__':
    d = bauen('terme.quadratische_extreme',
          'Quadratische Terme mit der quadratischen Ergänzung umformen, ihr Minimum oder Maximum bestimmen und einfache Optimierungsaufgaben lösen.',
          ['Ergänzen: x² + bx + (b : 2)² = (x + b : 2)².',
           'Quadratische Ergänzung: (b : 2)² ergänzen und gleich wieder abziehen.',
           'a(x − d)² + e: für a > 0 Minimum e, für a < 0 Maximum e – jeweils bei x = d.',
           'Optimieren: Zielgröße als Term in x aufstellen, Extremum bestimmen, im Sachzusammenhang antworten.'],
          [('Quadratische Ergänzung', ['ergaenzen', 'scheitelform']), ('Extremwerte', ['extremwert', 'mit_faktor', 'optimierung'])],
          ETAPPEN, GEN,
          offen=['Laut Umfang ohne vollständige Parabellehre: keine Graphen, nur Termumformung und Extremwerte. Scheitelpunkt/Parabeln folgen in RS 9.',
                 'Schreibweise Extremwert: „x = □; T = □“ statt T_min/T_max (Indizes in der App schwer lesbar).'])
    umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
    durchsicht(d)
    stufen('terme.quadratische_extreme', ST)
