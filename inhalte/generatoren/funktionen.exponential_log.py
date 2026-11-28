#!/usr/bin/env python3
"""Thema funktionen.exponential_log – Exponential- und Logarithmusfunktionen (Klasse 10)."""
import sys
from math import log
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import *  # noqa: E402,F403
from _schwer_kl10 import ergaenzen  # noqa: E402
import math  # noqa: E402

start(1003)
TIEF = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')


def lb(b):
    return 'lg' if b == 10 else f'log{str(b).translate(TIEF)}'


def cf(x):
    x = Fr(x)
    if x.denominator == 1: return str(int(x))
    if endlich(x): return str(float(x))
    return f'({x.numerator}/{x.denominator})'


def zt(x):
    x = Fr(x)
    return dz(x) if endlich(x) else br(x)


def ft(a, b):
    """f(x) = a · b^x als Text"""
    return f'{dz(a) if a != 1 else ""}{" · " if a != 1 else ""}{zt(b)}^x' if not isinstance(b, Fr) or b.denominator == 1 or endlich(b) else f'{dz(a)} · ({br(b)})^x'


ETAPPEN = [
    {'lernziel': 'werte', 'titel': 'Funktionswerte von a · bˣ',
     'regel': 'Bei der ⟦Exponentialfunktion⟧ f(x) = a · b^x (a ≠ 0, b > 0, b ≠ 1) steht x im ⟦Exponenten⟧. a ist der ⟦Anfangswert⟧ f(0), b der ⟦Wachstumsfaktor⟧. b^(−n) = 1/bⁿ.',
     'schritte': ['f(x) = 5 · 2^x, gesucht f(3) und f(−1).', 'f(3) = 5 · 8 = ⟦40⟧; f(−1) = 5 · ½ = ⟦2,5⟧.'],
     'probe': 'f(0) = 5 · 1 = 5 = a ✓',
     'fehler': 'f(3) = (5 · 2)³ = 1 000 ist falsch: Nur ⟦2⟧ wird potenziert, dann mit 5 multipliziert: 5 · 2³ = 40.'},
    {'lernziel': 'faktor', 'titel': 'Wachstumsfaktor und Prozent',
     'regel': 'Zunahme um p % pro Schritt: ⟦b = 1 + p/100⟧. Abnahme um p %: ⟦b = 1 − p/100⟧. b > 1: Wachstum, 0 < b < 1: Zerfall.',
     'schritte': ['Ein Bestand nimmt jährlich um 12 % ab.', 'b = 1 − 0,12 = ⟦0,88⟧, also f(t) = f(0) · 0,88^t.'],
     'probe': '100 · 0,88 = 88, das sind 12 weniger ✓',
     'fehler': 'Bei 12 % Abnahme b = 0,12 zu nehmen ist falsch: Dann blieben nur 12 % übrig. Es bleiben ⟦88 %⟧, also b = 0,88.'},
    {'lernziel': 'modell', 'titel': 'Ein Wachstumsmodell aufstellen',
     'regel': 'Anfangswert a = f(0). Den Faktor b erhältst du aus dem Quotienten ⟦aufeinanderfolgender Werte⟧ (gleicher Abstand). Verdopplung alle T Schritte: ⟦f(t) = a · 2^(t/T)⟧.',
     'schritte': ['Bakterien: 400 zu Beginn, Verdopplung alle 3 Stunden.', 'f(t) = 400 · 2^(t/3); nach 12 h: 400 · 2⁴ = ⟦6 400⟧.'],
     'probe': 'f(3) = 400 · 2 = 800 ✓',
     'fehler': 'Nach 12 h mit 400 · 2 · 12 zu rechnen ist falsch: Das wäre ⟦lineares⟧ Wachstum. Exponentiell wird ⟦4-mal verdoppelt⟧.'},
    {'lernziel': 'graph', 'titel': 'Eigenschaften der Graphen',
     'regel': 'Der Graph von f(x) = a · b^x (a > 0) schneidet die y-Achse in ⟦(0 | a)⟧, hat die ⟦x-Achse als Asymptote⟧ und ist für b > 1 ⟦steigend⟧, für 0 < b < 1 ⟦fallend⟧. Er hat keine Nullstelle.',
     'schritte': ['f(x) = 3 · 0,5^x: b = 0,5 < 1.', 'Graph ⟦fällt⟧, geht durch (0 | 3) und nähert sich für große x der x-Achse.'],
     'probe': 'f(10) = 3 · 0,5¹⁰ ≈ 0,003 > 0 ✓',
     'fehler': '„f(x) = 3 · 0,5^x hat eine Nullstelle bei großem x“ ist falsch: Die Werte werden ⟦beliebig klein, aber nie 0⟧.'},
    {'lernziel': 'logfunktion', 'titel': 'Die Logarithmusfunktion',
     'regel': 'f(x) = log_b(x) ist die ⟦Umkehrfunktion⟧ von g(x) = b^x: x- und y-Werte werden ⟦vertauscht⟧. Sie ist nur für ⟦x > 0⟧ definiert und geht durch (1 | 0) und (b | 1).',
     'schritte': ['g(x) = 2^x geht durch (3 | 8).', 'f(x) = log₂(x) geht durch ⟦(8 | 3)⟧, denn log₂(8) = 3.'],
     'probe': '2³ = 8 ✓',
     'fehler': '„log₂(x) ist für alle x definiert“ ist falsch: 2^y ist immer positiv, deshalb gibt es log₂(x) nur für ⟦x > 0⟧.'},
    {'lernziel': 'zeitpunkt', 'titel': 'Wann wird ein Wert erreicht?',
     'regel': 'Gesucht ist x mit a · b^x = c: erst durch a teilen, dann ⟦logarithmieren⟧: x = log_b(c/a) = lg(c/a) : lg b. ⟦Verdopplungszeit⟧ T₂ = lg 2 : lg b, ⟦Halbwertszeit⟧ T½ = lg 0,5 : lg b.',
     'schritte': ['f(t) = 200 · 1,05^t. Wann ist f(t) = 300?', '1,05^t = 1,5 ⇒ t = lg 1,5 : lg 1,05 ≈ ⟦8,3⟧.'],
     'probe': '200 · 1,05^8,3 ≈ 300 ✓',
     'fehler': '200 · 1,05^t = 300 ⇒ 210^t = 300 ist falsch: 200 · 1,05^t ist ein Produkt, ⟦erst durch 200 teilen⟧.'},
]

_E = {e['lernziel']: e for e in ETAPPEN}
_E['werte']['bild'] = koord([{'art': 'exp', 'a': 5, 'b': 2, 'name': 'f'}], x=(-2, 4), y=(0, 45),
                            punkte=[{'x': 3, 'y': 40, 'name': '(3 | 40)'}, {'x': -1, 'y': 2.5, 'name': '(−1 | 2,5)'}])
_E['faktor']['bild'] = koord([{'art': 'exp', 'a': 100, 'b': 0.88, 'name': '100 · 0,88ᵗ'}, {'art': 'exp', 'a': 100, 'b': 1.12, 'name': '100 · 1,12ᵗ'}],
                             x=(0, 10), y=(0, 320), name_x='t')
_E['modell']['bild'] = koord([{'art': 'exp', 'a': 400, 'b': 2 ** (1 / 3), 'bereich': [0, 12]}], x=(0, 12), y=(0, 7000), name_x='t', schritt_x=3,
                             punkte=[{'x': t, 'y': 400 * 2 ** (t // 3)} for t in (0, 3, 6, 9, 12)])
_E['graph']['bild'] = koord([{'art': 'exp', 'a': 3, 'b': 0.5, 'name': 'f'}], x=(-2, 6), y=(0, 13), punkte=[{'x': 0, 'y': 3, 'name': '(0 | 3)'}])
_E['logfunktion']['bild'] = koord([{'art': 'exp', 'a': 1, 'b': 2, 'name': '2ˣ'}, {'art': 'log', 'b': 2, 'name': 'log₂ x', 'name_x': 5}, {'art': 'linear', 'm': 1, 't': 0}],
                                  x=(-3, 9), y=(-3, 9), punkte=[{'x': 3, 'y': 8, 'name': '(3 | 8)'}, {'x': 8, 'y': 3, 'name': '(8 | 3)'}])
_E['zeitpunkt']['bild'] = koord([{'art': 'exp', 'a': 200, 'b': 1.05, 'bereich': [0, 16]}], x=(0, 16), y=(0, 450), waagrecht=[300], senkrecht=[8.3], name_x='t')


def exp_bild(a, b, x=(-3, 4)):
    return koord([{'art': 'exp', 'a': zahlwert_json(a), 'b': zahlwert_json(b)}], x=x, ymax=abs(a) * 12)


def g_werte(s):
    if s == 1:
        a, b, x = R.randint(1, 9), R.choice([2, 3, 10]), R.randint(1, 4)
        if b == 10 and x > 3: return None
        v = a * b ** x
        return zahl(f'Berechne f({x}) für f(x) = {a} · {b}^x.', f'f({x}) = {a} · {b}^{x} = {a} · {dz(b ** x)} = {dz(v)}.',
                    'Erst potenzieren, dann mit a multiplizieren.', v, f'{a} * {b} ** {x}')
    if s == 2:
        a, b, x = R.choice([2, 4, 5, 8, 10, 20, 40, 100]), R.choice([2, 4, 5, 10]), R.randint(-3, -1)
        v = a * Fr(b) ** x
        if not endlich(v): return None
        return zahl(f'Berechne f({dz(x)}) für f(x) = {a} · {b}^x.', f'f({dz(x)}) = {a} · {b}^({dz(x)}) = {a} : {dz(b ** -x)} = {dz(v)}.',
                    'Ein negativer Exponent bedeutet Kehrwert.', v, f'{a} * {b} ** ({x})')
    a, b, x = R.choice([100, 200, 400, 1000]), R.choice([Fr(1, 2), Fr(3, 2), Fr(6, 5), Fr(4, 5), Fr(11, 10), Fr(9, 10)]), R.randint(2, 4)
    v = a * b ** x
    if not endlich(v): return None
    return zahl(f'Berechne f({x}) für f(x) = {a} · {dz(b)}^x.', f'{dz(b)}^{x} = {dz(b ** x)}; f({x}) = {a} · {dz(b ** x)} = {dz(v)}.',
                'Potenziere die Dezimalzahl sorgfältig (Nachkommastellen addieren sich).', v, f'{a} * {cf(b)} ** {x}')


# (Größe, Pronomen, mögliche Prozentsätze, Richtungen) – Einwohnerzahlen nur −3 % … +3 %, große Raten bei Bakterien, Medikamenten, Wertverlust.
DINGE = [('ein Guthaben', 'es', [1, 2, 3, 4, 5, 6], (True,)),
         ('eine Einwohnerzahl', 'sie', [1, 2, 3], (True, False)),
         ('ein Bestand an Tieren', 'er', [2, 4, 5, 6, 8, 10, 12, 15], (True, False)),
         ('der Wert eines Autos', 'er', [8, 10, 12, 15, 18, 20, 25], (False,)),
         ('eine Bakterienkultur', 'sie', [10, 15, 20, 25, 30, 40], (True,)),
         ('die Menge eines Medikaments im Blut', 'sie', [10, 12, 15, 18, 20, 25, 30], (False,)),
         ('die Zahl der Nutzer einer App', 'sie', [5, 8, 10, 12, 15, 20], (True, False))]


def g_faktor(s):
    ding, pron, raten, richtungen = R.choice(DINGE)
    p = R.choice(raten)
    zu = R.choice(richtungen)
    b = 1 + Fr(p, 100) if zu else 1 - Fr(p, 100)
    if s == 1:
        einheit_zeit = 'Stunde' if 'Bakterien' in ding or 'Medikament' in ding else 'Jahr'
        return zahl(f'{ding[0].upper() + ding[1:]} {"wächst" if zu else "nimmt"} jede {einheit_zeit} um {p} % {"" if zu else "ab"}'.rstrip() + '. Wie groß ist der Wachstumsfaktor b?'
                    if einheit_zeit == 'Stunde' else
                    f'{ding[0].upper() + ding[1:]} {"wächst" if zu else "nimmt"} jedes Jahr um {p} % {"" if zu else "ab"}'.rstrip() + '. Wie groß ist der Wachstumsfaktor b?',
                    f'b = 1 {"+" if zu else "−"} {p}/100 = {dz(b)}.', 'Wie viel Prozent bleiben bzw. kommen dazu?', b, f'1 {"+" if zu else "-"} {p} / 100')
    if s == 2:
        a = R.choice([50, 200, 1500, 8000, 120])
        return zahl(f'f(t) = {dz(a)} · {dz(b)}^t beschreibt einen Bestand (t in Jahren). Um wie viel Prozent {"wächst" if zu else "sinkt"} er pro Jahr?',
                    f'b = {dz(b)} {">" if zu else "<"} 1: {"Zunahme" if zu else "Abnahme"} um |{dz(b)} − 1| · 100 % = {p} %.', 'Vergleiche b mit 1.', p,
                    f'abs({cf(b)} - 1) * 100', einheit='%')
    if R.random() < 0.5:
        return auswahl(f'Beschreibt f(t) = {dz(R.choice([20, 300, 5000]))} · {dz(b)}^t Wachstum oder Zerfall, und um wie viel Prozent pro Schritt?',
                       f'{"Wachstum" if zu else "Zerfall"} um {p} %',
                       [f'{"Zerfall" if zu else "Wachstum"} um {p} %', f'{"Wachstum" if zu else "Zerfall"} um {dz(b * 100)} %',
                        f'{"Wachstum" if zu else "Zerfall"} um {100 - p} %'],
                       f'b = {dz(b)} {">" if zu else "<"} 1, Änderung {p} % pro Schritt.', 'Ist b größer oder kleiner als 1?')
    n = R.randint(2, 3)
    q = b ** n
    if not endlich(q) or len(dz(q)) > 9: return None
    zeit = 'Stunde' if 'Bakterien' in ding or 'Medikament' in ding else 'Jahr'
    satz = (f'{ding[0].upper() + ding[1:]} {"wächst" if zu else "sinkt"} {"jede Stunde" if zeit == "Stunde" else "jedes Jahr"} um {p} %. '
            f'Um welchen Faktor ändert {pron} sich in {n} {"Stunden" if zeit == "Stunde" else "Jahren"}?')
    return zahl(satz,
                f'Faktor pro Jahr {dz(b)}; in {n} Jahren {dz(b)}^{n} = {dz(q)}.', 'Die Faktoren werden multipliziert, nicht die Prozente addiert.', q,
                f'{cf(b)} ** {n}')


def _lin_oder_exp():
    a = R.choice([2, 3, 4, 5, 6, 8, 10])
    exp = R.random() < 0.5
    if exp:
        b = R.choice([2, 3])
        ys = [a * b ** i for i in range(4)]
        richtig = f'exponentiell, Faktor {b} je Schritt'
        falsch = [f'linear, +{dz(ys[1] - ys[0])} je Schritt', f'exponentiell, Faktor {dz(ys[1] - ys[0])} je Schritt', 'weder linear noch exponentiell']
        w = f'{" ; ".join(f"{dz(ys[i + 1])} : {dz(ys[i])} = {b}" for i in range(3))}: immer derselbe Quotient, also exponentiell mit Faktor {b}.'
    else:
        d = a * R.choice([1, 2])
        ys = [a + d * i for i in range(4)]
        q = Fr(ys[1], ys[0])
        richtig = f'linear, +{dz(d)} je Schritt'
        falsch = [f'exponentiell, Faktor {zt(q)} je Schritt', f'linear, +{dz(ys[1])} je Schritt', 'weder linear noch exponentiell']
        w = f'Differenzen: {", ".join(dz(ys[i + 1] - ys[i]) for i in range(3))} – immer gleich, also linear. Die Quotienten ({zt(Fr(ys[1], ys[0]))}, {zt(Fr(ys[2], ys[1]))}, …) sind nicht gleich.'
    a_ = auswahl('Die Tabelle zeigt Werte einer Funktion. Ist sie linear oder exponentiell?', richtig, falsch, w,
                 'Prüfe Differenzen (gleich ⇒ linear) und Quotienten (gleich ⇒ exponentiell) aufeinanderfolgender y-Werte.')
    return mit_grafik(a_, tabelle(['x', '0', '1', '2', '3'], [['y'] + [dz(y) for y in ys]]))


def _halbwertszeit_modell():
    T, einh, m0 = R.choice([(6, 'h', 80), (4, 'Jahre', 1200), (8, 'h', 160), (5, 'Tage', 400), (3, 'h', 64), (10, 'Jahre', 2000), (12, 'h', 240)])
    k = R.randint(2, 4)
    v = Fr(m0, 2 ** k)
    if not endlich(v): return None
    stoff, e = ('Ein Medikament', 'mg') if einh == 'h' else ('Ein radioaktiver Stoff', 'g')
    wo = ' im Blut' if einh == 'h' else ''
    return zahl(f'{stoff} hat eine Halbwertszeit von {T} {einh}. Anfangs sind {dz(m0)} {e}{wo} vorhanden. Wie viel {e} sind es nach {T * k} {einh}?',
                f'Modell f(t) = {dz(m0)} · 0,5^(t/{T}). f({T * k}) = {dz(m0)} · 0,5^{k} = {dz(v)} {e}.',
                'Stelle das Modell mit 0,5 hoch (t : Halbwertszeit) auf.', v, f'{m0} * 0.5 ** ({T * k} / {T})', einheit=e)


def g_modell(s):
    if s == 1:
        a, T, k = R.choice([50, 100, 200, 300, 400, 500]), R.choice([2, 3, 4, 5, 6, 20, 30]), R.randint(2, 5)
        t = T * k
        v = a * 2 ** k
        einh = 'min' if T >= 20 else 'h'
        return zahl(f'Eine Kultur enthält zu Beginn {a} Zellen und verdoppelt sich alle {T} {einh}. Wie viele Zellen sind es nach {t} {einh}?',
                    f'{t} : {T} = {k} Verdopplungen: {a} · 2^{k} = {dz(v)}.', 'Wie oft passt die Verdopplungszeit in die Zeitspanne?', v, f'{a} * 2 ** ({t} / {T})')
    if s == 2 and R.random() < 0.45:
        return _lin_oder_exp()
    if s == 2:
        a = R.choice([20, 40, 50, 80, 100, 250])
        b = R.choice([Fr(3, 2), 2, 3, Fr(5, 4), Fr(6, 5), Fr(1, 2), Fr(4, 5)])
        f1 = a * b
        if not endlich(f1): return None
        return zahl(f'Eine Exponentialfunktion hat f(0) = {a} und f(1) = {dz(f1)}. Bestimme den Wachstumsfaktor b in f(x) = a · b^x.',
                    f'a = f(0) = {a}; b = f(1) : f(0) = {dz(f1)} : {a} = {dz(b)}.', 'Teile zwei aufeinanderfolgende Werte.', b, f'{cf(f1)} / {a}')
    if R.random() < 0.35:
        return _halbwertszeit_modell()
    a = R.choice([10, 20, 50, 100, 200])
    b = R.choice([2, 3, Fr(3, 2), Fr(1, 2), Fr(6, 5), Fr(9, 10)])
    x1 = R.randint(1, 3)
    y1, y2 = a * b ** x1, a * b ** (x1 + 2)
    if not (endlich(y1) and endlich(y2)) or len(dz(y2)) > 9: return None
    if R.random() < 0.5:
        return zahl(f'Der Graph von f(x) = a · b^x (b > 0) geht durch P({x1} | {dz(y1)}) und Q({x1 + 2} | {dz(y2)}). Bestimme b.',
                    f'f({x1 + 2}) : f({x1}) = b² = {dz(y2)} : {dz(y1)} = {dz(b * b)} ⇒ b = {dz(b)} (b > 0).', 'Der Quotient der y-Werte ist b hoch Abstand der x-Werte.',
                    b, f'({cf(y2)} / {cf(y1)}) / {cf(b)}')
    return zahl(f'Der Graph von f(x) = a · b^x geht durch P({x1} | {dz(y1)}) und Q({x1 + 2} | {dz(y2)}). Bestimme den Anfangswert a.',
                f'b² = {dz(y2)} : {dz(y1)} ⇒ b = {dz(b)}; a = {dz(y1)} : {dz(b)}^{x1} = {dz(a)}.', 'Erst b bestimmen, dann a aus einem Punkt.', a,
                f'{cf(y1)} / {cf(b)} ** {x1}')


def g_graph(s):
    a = R.choice([1, 2, 3, 4, 5, 10])
    b = R.choice([Fr(1, 2), Fr(1, 3), 2, 3, Fr(3, 2), Fr(4, 5), 5])
    steig = b > 1
    typ = R.choice({1: 'abz', 2: 'abcz', 3: 'cdez'}[s])
    fx = f'f(x) = {a if a != 1 else ""}{" · " if a != 1 else ""}{"(" + br(b) + ")" if not endlich(b) else dz(b)}^x'
    bild = exp_bild(a, b)
    if typ == 'z':
        richtig = (f'{a} · ' if a != 1 else '') + (f'({br(b)})' if not endlich(b) else zt(b)) + '^x'
        kw = 1 / Fr(b)
        andere = [(f'{a} · ' if a != 1 else '') + (f'({br(kw)})' if not endlich(kw) else zt(kw)) + '^x',
                  f'{a + 1} · ' + (f'({br(b)})' if not endlich(b) else zt(b)) + '^x',
                  f'{zt(b)} · {a if a != 1 else 2}^x']
        return mit_grafik(auswahl('Welcher Funktionsterm f(x) passt zum gezeichneten Graphen?', richtig, andere,
                                  f'y-Achsenabschnitt (0 | {a}) ⇒ a = {a}; der Graph {"steigt" if steig else "fällt"} ⇒ b {">" if steig else "<"} 1; f(1) = {zt(a * b)} ⇒ b = {zt(b)}.',
                                  'Lies f(0) ab (das ist a) und vergleiche f(1) mit f(0) (Faktor b).'), bild)
    if typ == 'a':
        return mit_grafik(luecken(f'In welchem Punkt schneidet der Graph von {fx} die y-Achse? (Zur Kontrolle ist der Graph gezeichnet.)', 'S(□ | □)', 'x- und y-Koordinate', [0, a],
                       f'f(0) = {a} · 1 = {a}, also S(0 | {a}).', 'Setze x = 0 ein.', c=['0', f'{a} * {cf(b)} ** 0']), bild)
    if typ == 'b':
        w_r, w_f = ('steigend', 'fallend') if steig else ('fallend', 'steigend')
        richtig = f'{w_r}, weil b = {zt(b)} {">" if steig else "<"} 1'
        falsch = [f'{w_f}, weil b = {zt(b)} {">" if steig else "<"} 1']
        # Verwechslung von a und b
        grund = f'a = {a} > 1' if a > 1 else 'a = 1'
        falsch += [f'steigend, weil {grund}', f'fallend, weil {grund}']
        return auswahl(f'Ist der Graph von {fx} steigend oder fallend?', richtig, falsch,
                       f'Über Steigen oder Fallen entscheidet der Faktor b, nicht a (a > 0): b = {zt(b)} {">" if steig else "<"} 1, also {w_r}.',
                       'Welche der beiden Zahlen ist der Wachstumsfaktor?')
    if typ == 'c':
        return auswahl(f'Welche Aussage über den Graphen von {fx} ist richtig?', 'Er hat keine Nullstelle.',
                       ['Er schneidet die x-Achse genau einmal.', f'Er geht durch (1 | {a}).', 'Er hat die y-Achse als Asymptote.'],
                       f'{zt(b)}^x ist immer positiv, also auch {a} · {zt(b)}^x > 0. Die x-Achse ist Asymptote. f(1) = {zt(a * b)}.',
                       'Kann a · b^x null werden?')
    if typ == 'd':
        b2 = R.choice([2, 3, 4, 5])
        return auswahl(f'Wie entsteht der Graph von g(x) = (1/{b2})^x aus dem Graphen von f(x) = {b2}^x?', 'durch Spiegelung an der y-Achse',
                       ['durch Spiegelung an der x-Achse', 'durch Verschiebung nach unten', 'durch Spiegelung an der Winkelhalbierenden y = x'],
                       f'(1/{b2})^x = {b2}^(−x) = f(−x): Spiegelung an der y-Achse.', 'Schreibe 1/b als b hoch −1.')
    # verschobener Graph g(x) = B^x + m mit Zeichnung
    B = b if isinstance(b, int) else 2
    m = R.choice([1, 2, 3, 4, -1, -2, -3, -4])
    gb = koord([{'art': 'exp', 'a': 1, 'b': B, 'c': m}], x=(-4, 3), ymax=12, waagrecht=[m])
    if R.random() < 0.5:
        a_ = auswahl(f'Die Zeichnung zeigt den Graphen von g(x) = {B}^x {plus(m)}. Welche Gerade ist Asymptote?', f'y = {dz(m)}', ['y = 0', f'y = {dz(-m)}', f'x = {dz(m)}'],
                     f'{B}^x nähert sich für sehr kleine x der 0; um {dz(m)} verschoben nähert sich g(x) dem Wert {dz(m)}. Asymptote: y = {dz(m)}.',
                     'Wohin nähert sich b^x, und was bewirkt die Verschiebung?')
    else:
        a_ = luecken(f'Die Zeichnung zeigt den Graphen von g(x) = {B}^x {plus(m)}. In welchem Punkt schneidet er die y-Achse?', 'S(□ | □)', 'x- und y-Koordinate',
                     [0, 1 + m], f'g(0) = {B}⁰ {plus(m)} = 1 {plus(m)} = {dz(1 + m)}, also S(0 | {dz(1 + m)}).', 'Setze x = 0 ein; denk an b⁰ = 1.',
                     c=['0', f'{B} ** 0 + ({m})'])
    return mit_grafik(a_, gb)


def g_logfunktion(s):
    b = R.choice([2, 3, 4, 5, 10])
    if s == 1:
        n = R.randint(1, {2: 7, 3: 5, 4: 4, 5: 4, 10: 5}[b])
        x = b ** n
        return zahl(f'Berechne f({dz(x)}) für f(x) = {lb(b)}(x).', f'{b}^{n} = {dz(x)}, also f({dz(x)}) = {n}.', 'Mit welchem Exponenten wird die Basis zu x?', n,
                    f'{n} + ({b} ** {n} - {x})')
    typ = R.random()
    if s == 2:
        if typ < 0.5:
            n = R.randint(1, 4)
            x = b ** n
            return luecken(f'Der Graph von g(x) = {b}^x geht durch P({n} | {dz(x)}). Welcher Punkt liegt deshalb auf dem Graphen von f(x) = {lb(b)}(x)?',
                           'Q(□ | □)', 'x- und y-Koordinate', [x, n], f'Umkehrfunktion: Koordinaten tauschen ⇒ Q({dz(x)} | {n}).',
                           'Bei der Umkehrfunktion werden x und y vertauscht.', c=[f'{b} ** {n}', f'{n}'])
        if typ < 0.75:
            # Logarithmus im Kopf: Kehrwerte und Zehnerpotenzen
            n = R.randint(-3, -1) if b != 10 else R.randint(-4, -1)
            x = Fr(b) ** n
            xt = dz(x) if b == 10 else br(x)
            return zahl(f'Berechne ohne Taschenrechner: {lb(b)}({xt}).', f'{xt} = {b}^({dz(n)}), also {lb(b)}({xt}) = {dz(n)}.',
                        'Schreibe die Zahl als Potenz der Basis; Kehrwert heißt negativer Exponent.', n, f'{n} + ({b} ** ({n}) - {cf(x)})')
        return auswahl(f'Für welche x ist f(x) = {lb(b)}(x) definiert?', 'für alle x > 0', ['für alle x', 'für alle x ≥ 0', 'für alle x ≠ 0'],
                       f'{b}^y ist immer positiv, also gibt es {lb(b)}(x) nur für x > 0.', 'Welche Werte nimmt b^y an?')
    if typ < 0.3:
        # Graph der Logarithmusfunktion mit Zeichnung
        bb = R.choice([2, 3, 10])
        gb = koord([{'art': 'log', 'b': bb, 'name': lb(bb) + ' x'}], x=(-1, 9), y=(-3, 4))
        if R.random() < 0.5:
            a_ = luecken(f'Die Zeichnung zeigt den Graphen von f(x) = {lb(bb)}(x). In welchem Punkt schneidet er die x-Achse?', 'N(□ | □)', 'x- und y-Koordinate', [1, 0],
                         f'{lb(bb)}(1) = 0, denn {bb}⁰ = 1. Also N(1 | 0).', 'Für welches x ist der Exponent 0?', c=[f'{bb} ** 0', '0'])
        else:
            a_ = auswahl(f'Die Zeichnung zeigt den Graphen von f(x) = {lb(bb)}(x). Welche Gerade ist Asymptote?', 'die y-Achse (x = 0)',
                         ['die x-Achse (y = 0)', 'die Gerade y = x', 'die Gerade x = 1'],
                         f'Für x → 0 (x > 0) werden die Werte von {lb(bb)}(x) beliebig klein; der Graph nähert sich der y-Achse, erreicht sie aber nie.',
                         'Wo ist die Funktion nicht definiert, und wie verhält sich der Graph dort?')
        return mit_grafik(a_, gb)
    if typ < 0.45:
        n = R.randint(-3, -1)
        x = Fr(b) ** n
        return zahl(f'Berechne f({zt(x)}) für f(x) = {lb(b)}(x).', f'{b}^({dz(n)}) = {zt(x)}, also f({zt(x)}) = {dz(n)}.',
                    'Kehrwerte entstehen durch negative Exponenten.', n, f'{n} + ({b} ** ({n}) - {cf(x)})')
    if typ < 0.7:
        return auswahl(f'Durch welchen Punkt gehen die Graphen aller Funktionen f(x) = log_b(x)?', '(1 | 0)', ['(0 | 1)', '(0 | 0)', '(1 | 1)'],
                       'log_b(1) = 0 für jede Basis b, denn b⁰ = 1.', 'Welcher x-Wert liefert immer den Exponenten 0?') if R.random() < 0.5 else \
            auswahl(f'Welche Funktion ist die Umkehrfunktion von f(x) = {lb(b)}(x)?', f'g(x) = {b}^x', [f'g(x) = x^{b}', f'g(x) = {b}x', f'g(x) = −{lb(b)}(x)'],
                    f'{lb(b)} macht das Potenzieren mit Basis {b} rückgängig; umgekehrt: g(x) = {b}^x.', 'Was hebt den Logarithmus auf?')
    x = R.randint(2, 99)
    v = gerundet(logb(b, x), 2)
    if v is None or abs(logb(b, x) - round(logb(b, x))) < 0.01: return None
    return zahl(f'Berechne f({x}) für f(x) = {lb(b)}(x) auf zwei Nachkommastellen.', f'{lb(b)}({x}) = lg {x} : lg {b} ≈ {dz(v)}.',
                'Mit dem Taschenrechner: lg x : lg b.', v, f'round({K(logb(b, x))}, 2)', tol=0.01)


def d1(v):
    """Zahl mit genau einer Nachkommastelle (17,0 statt 17)."""
    return f'{v:.1f}'.replace('.', ',')


def g_zeitpunkt(s):
    if s == 1:
        a, b = R.choice([100, 200, 500, 1000]), R.choice([Fr(105, 100), Fr(11, 10), Fr(12, 10), Fr(103, 100), Fr(15, 10)])
        k = R.choice([2, 3, 5, 10])
        t = log(k) / log(float(b))
        v = gerundet(t, 1)
        if v is None: return None
        return zahl(f'f(t) = {dz(a)} · {dz(b)}^t. Für welches t ist f(t) = {dz(a * k)}? Runde auf eine Nachkommastelle.',
                    f'{dz(b)}^t = {k} ⇒ t = lg {k} : lg {dz(b)} ≈ {d1(v)}.', 'Erst durch den Anfangswert teilen, dann logarithmieren.', v, f'round({K(t)}, 1)', tol=0.1)
    if s == 2:
        p = R.choice([2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20])
        zu = R.random() < 0.5
        b = 1 + p / 100 if zu else 1 - p / 100
        T = log(2 if zu else 0.5) / log(b)
        v = gerundet(T, 1)
        if v is None: return None
        return zahl(f'Ein Bestand {"wächst" if zu else "nimmt"} um {p} % pro Jahr{"" if zu else " ab"}. Berechne die {"Verdopplungszeit" if zu else "Halbwertszeit"} (eine Nachkommastelle).',
                    f'b = {dz(Fr(100 + (p if zu else -p), 100))}; {"T₂ = lg 2" if zu else "T½ = lg 0,5"} : lg {dz(Fr(100 + (p if zu else -p), 100))} ≈ {d1(v)} Jahre.',
                    'Löse b^T = 2 bzw. b^T = 0,5.', v, f'round({K(T)}, 1)', einheit='Jahre', tol=0.1)
    # Getränk etwa 80–95 °C, Raum 20 °C: Übertemperatur höchstens 75 °C, Endwert 5–30 °C
    a, c = R.choice([(75, 25), (70, 14), (60, 15), (70, 10), (65, 20), (75, 30), (60, 12), (70, 5)])
    p = R.choice([5, 6, 8, 10, 12])
    b = 1 - p / 100
    t = log(c / a) / log(b)
    v = gerundet(t, 1)
    if v is None: return None
    return zahl(f'Ein heißes Getränk hat eine Übertemperatur von {a} °C (über der Raumtemperatur), die pro Minute um {p} % abnimmt. Nach wie vielen Minuten beträgt sie nur noch {c} °C (eine Nachkommastelle)?',
                f'{a} · {dz(Fr(100 - p, 100))}^t = {c} ⇒ t = lg({zt(Fr(c, a))}) : lg {dz(Fr(100 - p, 100))} ≈ {d1(v)} min.', 'Modell aufstellen, durch den Anfangswert teilen, logarithmieren.',
                v, f'round({K(t)}, 1)', einheit='min', tol=0.1)



# ---------- KLAR: Lernkarten im neuen Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst nach dem Bauen der Aufgaben eingesetzt (bauen(..., klar=KLAR)), die Aufgaben bleiben wörtlich gleich.
# Muster: einstieg (≤ 35 Wörter) → Kartenbild → Schritte als {text, bild} (Bildergeschichte) → „Pass auf!“ (fehler + fehler_bild) → MERKE (regel).
_PUNKTE_MODELL = [{'x': 0, 'y': 400}, {'x': 3, 'y': 800}, {'x': 6, 'y': 1600}, {'x': 9, 'y': 3200}]
KLAR = {
 'werte': {
  'einstieg': 'Wasserlinsen bedecken heute 5 m² eines Teichs. Jede Woche verdoppelt sich die Fläche: 10, 20, 40 m². '
              'So eine Rechnung heißt ⟦Exponentialfunktion⟧.',
  'woerter': [['Exponentialfunktion', 'f(x) = a · b^x: x steht oben im Exponenten'],
              ['Anfangswert', 'der Wert bei x = 0, hier 5 m²'],
              ['Wachstumsfaktor', 'damit wird pro Woche malgenommen, hier 2']],
  'bild': {'typ': 'koordinaten', 'x': [-2, 4], 'y': [0, 45], 'graphen': [{'art': 'exp', 'a': 5, 'b': 2, 'name': 'Fläche'}],
           'name_x': 'Wochen', 'name_y': 'm²', 'schritt_y': 10},
  'schritte': [{'text': 'Die Fläche ist f(x) = 5 · 2^x: Anfangswert 5, Wachstumsfaktor 2.', 'bild': {'punkte': [{'x': 0, 'y': 5, 'name': 'heute: 5'}]}},
               {'text': 'f(3): erst 2³ = 8, dann mal 5. Also ⟦f(3) = 40⟧.',
                'bild': {'punkte': [{'x': 0, 'y': 5, 'name': 'heute: 5'}, {'x': 3, 'y': 40, 'name': '3 Wochen: 40'}]}},
               {'text': 'f(−1) heißt: eine Woche vor heute. 2^(−1) ist 1/2.'},
               {'text': 'Also f(−1) = 5 · 1/2 = ⟦2,5⟧ m².',
                'bild': {'punkte': [{'x': 0, 'y': 5, 'name': 'heute: 5'}, {'x': 3, 'y': 40, 'name': '3 Wochen: 40'}, {'x': -1, 'y': 2.5, 'name': 'vorher: 2,5'}]}}],
  'fehler': 'f(3) = (5 · 2)³ = 1 000 ist falsch. Hoch 3 gilt nur für die 2. Richtig: ⟦5 · 2³ = 40⟧.',
  'fehler_bild': {'punkte': [{'x': 3, 'y': 40, 'name': '40, nicht 1 000'}]},
  'regel': 'Erst b^x ausrechnen, dann mit a malnehmen. Negative Exponenten: ⟦b^(−n) = 1/bⁿ⟧.'},
 'faktor': {
  'einstieg': 'Ein neues Auto kostet 20 000 € und verliert jedes Jahr 12 % Wert. Übrig bleiben jedes Jahr 88 %. '
              'Statt „minus 12 %“ rechnet man „mal 0,88“: Das ist der ⟦Wachstumsfaktor⟧.',
  'woerter': [['Wachstumsfaktor', 'die Zahl, mit der pro Jahr malgenommen wird'],
              ['Zerfall', 'Abnahme um einen festen Prozentsatz; der Faktor ist kleiner als 1']],
  'bild': {'typ': 'koordinaten', 'x': [0, 10], 'y': [0, 22000], 'graphen': [{'art': 'exp', 'a': 20000, 'b': 0.88, 'bereich': [0, 10], 'name': 'Wert'}],
           'name_x': 'Jahre', 'name_y': '€', 'schritt_y': 5000},
  'schritte': [{'text': '12 % Abnahme sind als Dezimalzahl 0,12.'},
               {'text': 'Übrig bleibt 1 − 0,12 = 0,88. Also ⟦b = 0,88⟧: ein Zerfall.'},
               {'text': 'Nach einem Jahr: 20 000 · 0,88 = 17 600 €.', 'bild': {'punkte': [{'x': 1, 'y': 17600, 'name': '17 600 €'}]}},
               {'text': 'Nach t Jahren: 20 000 · 0,88^t. Nach 5 Jahren etwa 10 555 €.',
                'bild': {'punkte': [{'x': 1, 'y': 17600, 'name': '17 600 €'}, {'x': 5, 'y': 10555, 'name': '≈ 10 555 €'}]}}],
  'fehler': 'b = 0,12 ist falsch. Dann wäre das Auto nach einem Jahr nur noch 2 400 € wert. Übrig bleiben ⟦88 %⟧, also b = 0,88.',
  'fehler_bild': {'graphen': [{'art': 'exp', 'a': 20000, 'b': 0.88, 'bereich': [0, 10], 'name': '0,88'},
                              {'art': 'exp', 'a': 20000, 'b': 0.12, 'bereich': [0, 10], 'name': '0,12?'}]},
  'regel': 'Zunahme um p %: b = 1 + p/100. Abnahme um p %: ⟦b = 1 − p/100⟧.'},
 'modell': {
  'einstieg': 'Im Labor sind 400 Bakterien. Alle 3 Stunden verdoppeln sie sich: 800, 1 600, 3 200. '
              'Eine Formel, die das für jede Zeit beschreibt, heißt ⟦Wachstumsmodell⟧.',
  'woerter': [['Wachstumsmodell', 'eine Formel, die das Wachstum für jede Zeit beschreibt'],
              ['Verdopplungszeit', 'die Zeit, in der sich die Anzahl verdoppelt, hier 3 Stunden']],
  'bild': {'typ': 'koordinaten', 'x': [0, 12], 'y': [0, 7000], 'graphen': [{'art': 'exp', 'a': 400, 'b': 1.2599210498948732, 'bereich': [0, 12]}],
           'name_x': 'Stunden', 'name_y': 'Anzahl', 'schritt_x': 3, 'schritt_y': 1000},
  'schritte': [{'text': 'Anfangswert a = 400, Verdopplungszeit T = 3 Stunden.', 'bild': {'punkte': [{'x': 0, 'y': 400, 'name': '400'}]}},
               {'text': 'Bis zur Zeit t wurde (t : 3)-mal verdoppelt: f(t) = 400 · 2^(t/3).', 'bild': {'punkte': _PUNKTE_MODELL}},
               {'text': 'Für t = 12 wurde viermal verdoppelt, und 2⁴ = 16.'},
               {'text': 'Also f(12) = 400 · 16 = ⟦6 400⟧ Bakterien.',
                'bild': {'punkte': _PUNKTE_MODELL + [{'x': 12, 'y': 6400, 'name': '12 h: 6 400'}]}}],
  'fehler': '400 · 2 · 12 = 9 600 ist falsch: Das wäre ⟦lineares⟧ Wachstum. Hier wird viermal verdoppelt: 800, 1 600, 3 200, 6 400.',
  'fehler_bild': {'punkte': _PUNKTE_MODELL + [{'x': 12, 'y': 6400, 'name': '6 400, nicht 9 600'}]},
  'regel': 'Der Anfangswert ist a = f(0). Verdopplung alle T Stunden: ⟦f(t) = a · 2^(t/T)⟧.'},
 'graph': {
  'einstieg': 'Grob gerechnet sind nach einer Spritze 3 mg Wirkstoff im Blut. Jede Stunde baut der Körper die Hälfte ab: 1,5 mg, dann 0,75 mg. '
              'Die x-Achse ist dann eine ⟦Asymptote⟧.',
  'woerter': [['Asymptote', 'eine Gerade, der sich der Graph immer weiter nähert, ohne sie zu erreichen'],
              ['fällt', 'der Graph geht von links nach rechts nach unten']],
  'bild': {'typ': 'koordinaten', 'x': [-1, 6], 'y': [0, 7], 'graphen': [{'art': 'exp', 'a': 3, 'b': 0.5, 'name': 'Wirkstoff'}],
           'name_x': 'Stunden', 'name_y': 'mg'},
  'schritte': [{'text': 'f(x) = 3 · 0,5^x: Der Faktor 0,5 ist kleiner als 1, der Graph fällt.'},
               {'text': 'f(0) = 3 · 1 = 3. Er schneidet die y-Achse bei ⟦(0 | 3)⟧.', 'bild': {'punkte': [{'x': 0, 'y': 3, 'name': '(0 | 3)'}]}},
               {'text': 'Nach 10 Stunden: f(10) ≈ 0,003 mg. Wenig, aber mehr als 0.'},
               {'text': 'Die x-Achse ist Asymptote. Es gibt ⟦keine Nullstelle⟧.'}],
  'fehler': 'Bei großem x gibt es keine Nullstelle. Die Hälfte von etwas Positivem ist immer noch positiv: ⟦beliebig klein, aber nie 0⟧.',
  'regel': 'Der Graph von a · b^x geht durch (0 | a). b > 1: ⟦steigt⟧, 0 < b < 1: fällt. Die x-Achse ist Asymptote.'},
 'logfunktion': {
  'einstieg': 'Am Teich ist 1 m² bedeckt, die Fläche verdoppelt sich jede Woche. Oft fragt man rückwärts: Nach wie vielen Wochen sind es 8 m²? '
              'Das beantwortet die ⟦Logarithmusfunktion⟧.',
  'woerter': [['Logarithmusfunktion', 'f(x) = log₂(x): die Wochen bis zur Fläche x'],
              ['Umkehrfunktion', 'macht die Zuordnung rückwärts: x und y werden vertauscht']],
  'bild': {'typ': 'koordinaten', 'x': [-3, 9], 'y': [-3, 9],
           'graphen': [{'art': 'exp', 'a': 1, 'b': 2, 'name': '2ˣ'}, {'art': 'log', 'b': 2, 'name': 'log₂ x', 'name_x': 5}, {'art': 'linear', 'm': 1, 't': 0, 'name': 'y = x'}]},
  'schritte': [{'text': 'g(x) = 2^x geht durch (3 | 8): Nach 3 Wochen sind es 8 m².', 'bild': {'punkte': [{'x': 3, 'y': 8, 'name': '(3 | 8)'}]}},
               {'text': 'Rückwärts gefragt: Wann sind es 8 m²? log₂(8) = 3.'},
               {'text': 'Bei der Umkehrfunktion werden x und y vertauscht: ⟦(8 | 3)⟧.',
                'bild': {'punkte': [{'x': 3, 'y': 8, 'name': '(3 | 8)'}, {'x': 8, 'y': 3, 'name': '(8 | 3)'}]}},
               {'text': 'Deshalb liegen beide Graphen spiegelbildlich zur Geraden y = x.'}],
  'fehler': 'log₂(x) gibt es nicht für alle x. Eine Fläche von 0 m² wird nie erreicht, denn 2^y ist immer positiv. Also nur ⟦x > 0⟧.',
  'regel': 'log_b(x) ist die Umkehrfunktion von b^x. Sie gilt nur für ⟦x > 0⟧ und geht durch (1 | 0).'},
 'zeitpunkt': {
  'einstieg': 'Ein Sportverein hat 200 Mitglieder, jedes Jahr kommen 5 % dazu. Wann hat er 300 Mitglieder? '
              'Gesucht ist diesmal kein Wert, sondern ein ⟦Zeitpunkt⟧.',
  'woerter': [['Zeitpunkt', 'die Zeit t, zu der ein Wert erreicht wird'],
              ['Logarithmieren', 'den Logarithmus bilden, um an den Exponenten zu kommen']],
  'bild': {'typ': 'koordinaten', 'x': [0, 16], 'y': [0, 450], 'graphen': [{'art': 'exp', 'a': 200, 'b': 1.05, 'bereich': [0, 16], 'name': 'Mitglieder'}],
           'waagrecht': [300], 'name_x': 'Jahre', 'name_y': 'Anzahl', 'schritt_y': 100},
  'schritte': [{'text': 'Gesucht ist t mit 200 · 1,05^t = 300.'},
               {'text': 'Durch 200 teilen, damit die Potenz allein steht: 1,05^t = 1,5.'},
               {'text': 'Logarithmieren: t = lg 1,5 : lg 1,05 ≈ ⟦8,3⟧ Jahre.',
                'bild': {'senkrecht': [8.3], 'punkte': [{'x': 8.3, 'y': 300, 'name': '≈ 8,3 Jahre'}]}}],
  'fehler': '200 · 1,05^t = 300 ⇒ 210^t = 300 ist falsch. Die 200 Mitglieder werden nicht potenziert: ⟦erst durch 200 teilen⟧.',
  'regel': 'Erst durch den Anfangswert teilen, dann logarithmieren. Verdopplungszeit: ⟦T = lg 2 : lg b⟧.'},
}


GEN = schoen({'werte': g_werte, 'faktor': g_faktor, 'modell': g_modell, 'graph': g_graph, 'logfunktion': g_logfunktion, 'zeitpunkt': g_zeitpunkt})

# ---------- Zehnte Runde (Zweig schwer-kl10): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Zufallsstart (nur zum Mischen der Antworten); wird erst NACH bauen(...) aufgerufen, alte Aufgaben bleiben gleich.
# Vorbilder (Typ und Niveau, eigene Zahlen und Einkleidung): Bayerischer Mathematik-Test 10 (2025, Aufgabe 5: Funktionswert berechnen
# und im Sachzusammenhang deuten), Realschul-Abschlussprüfung Bayern Mathematik I (2021 A 1: Prozent pro Zeiteinheit, zwei Vorgänge
# gleichsetzen; 2022 A 1: Rate aus zwei Werten, erstes Jahr über einer Grenze; 2022 B 1 / 2008 A 1: Logarithmusfunktion –
# Definitionsmenge, Asymptote, Spiegeln an der x-Achse und Verschieben; 2024 A 3.3: Verschiebung, die eine Nullstelle erzeugt).
def schwer():
    start(10012)
    N = []

    def neu(l, s, a):
        a['l'], a['s'] = l, s
        N.append(a)

    def rz(wahr, nd):
        return gerundet(wahr, nd), f'round({K(wahr)}, {nd})'

    # --- werte ---
    neu('werte', 2, zahl('Berechne f(−2) für f(x) = 64 · 0,5^x.', 'f(−2) = 64 · 0,5^(−2) = 64 · (1/0,5)² = 64 · 4 = 256.',
                         'Ein negativer Exponent bildet den Kehrwert: 0,5^(−1) = 2.', 256, '64 * 2 ** 2'))
    neu('werte', 2, auswahl('f(x) = 3 · 2^x. Wie ändert sich der Funktionswert, wenn x um 3 größer wird?', 'Er wird verachtfacht.',
                            ['Er wird um 8 größer.', 'Er wird verdreifacht.', 'Er wird um 24 größer.'],
                            'f(x + 3) = 3 · 2^(x + 3) = 3 · 2^x · 2³ = 8 · f(x). Bei Exponentialfunktionen wird multipliziert, nicht addiert.',
                            'Schreibe 2^(x + 3) als 2^x · 2³.'))
    neu('werte', 3, auswahl('Die Zahl der Abonnenten eines Kanals wird durch f(t) = 1 200 · 1,25^t beschrieben (t in Monaten seit Beobachtungsbeginn). Berechne f(−1) und deute das Ergebnis.',
                            'f(−1) = 960: Einen Monat vor Beobachtungsbeginn hatte der Kanal etwa 960 Abonnenten.',
                            ['f(−1) = 960: Nach einem Monat hat der Kanal 960 Abonnenten.', 'f(−1) = 960: Im ersten Monat kündigen 960 Abonnenten.',
                             'f(−1) hat keine Bedeutung, weil die Zeit nicht negativ sein kann.'],
                            'f(−1) = 1 200 : 1,25 = 960. t = −1 heißt: ein Monat vor dem Zeitpunkt t = 0 (Beobachtungsbeginn), sofern das Modell auch davor galt.',
                            'Was bedeutet t = 0, was t = −1?'))
    neu('werte', 3, zahl('Für f(x) = a · 2^x gilt f(3) − f(1) = 36. Bestimme a.', 'f(3) − f(1) = 8a − 2a = 6a = 36, also a = 6.',
                         'Setze 3 und 1 ein und klammere a aus.', 6, '36 / (2 ** 3 - 2)'))
    neu('werte', 3, zahl('f(x) = 5 · 3^x. Für welches x ist f(x) = 5/9?', '5 · 3^x = 5/9 ⇒ 3^x = 1/9 = 3^(−2) ⇒ x = −2.',
                         'Teile durch 5 und schreibe 1/9 als Potenz von 3.', -2, '-2 + (5 * 3 ** (-2) - 5 / 9)'))
    neu('werte', 3, zahl('f(x) = 2^x und g(x) = 2^(x + 3). Um welchen Faktor ist g(x) größer als f(x) – für jedes x?',
                         'g(x) = 2^x · 2³ = 8 · f(x). Die Verschiebung um 3 nach links wirkt wie eine Streckung mit dem Faktor 8.',
                         'Wende das Potenzgesetz 2^(x + 3) = 2^x · 2³ an.', 8, '2 ** 3'))

    # --- faktor ---
    neu('faktor', 2, zahl('Ein Bestand wächst in 2 Jahren insgesamt um 21 %, jedes Jahr um denselben Prozentsatz. Um wie viel Prozent pro Jahr?',
                          'b² = 1,21 ⇒ b = 1,1 ⇒ 10 % pro Jahr (nicht 10,5 %).', 'Zwei gleiche Faktoren b ergeben zusammen 1,21.', 10, '(11 - 10) * 10', einheit='%'))
    neu('faktor', 2, zahl('Ein Preis steigt um 20 % und sinkt danach um 20 %. Mit welchem Faktor wurde der ursprüngliche Preis insgesamt multipliziert?',
                          '1,2 · 0,8 = 0,96. Der Preis ist also um 4 % gesunken, nicht gleich geblieben.', 'Multipliziere die beiden Faktoren.', 0.96, '1.2 * 0.8'))
    w, c = rz((1 - 0.5 ** 0.25) * 100, 1)
    neu('faktor', 3, zahl('Ein Bestand wird durch f(t) = 80 · 0,5^(t/4) beschrieben (t in Stunden). Um wie viel Prozent nimmt er pro Stunde ab? Runde auf eine Nachkommastelle.',
                          f'Faktor pro Stunde: 0,5^(1/4) ≈ 0,8409. Abnahme: 1 − 0,8409 ≈ 0,1591, also etwa {dz(w)} % pro Stunde.',
                          'Setze t = 1 in 0,5^(t/4) ein. Das ist der Faktor pro Stunde.', w, c, einheit='%', tol=0.1))
    w, c = rz((1.05 ** 10 - 1) * 100, 1)
    neu('faktor', 3, zahl('Ein Bestand wächst jedes Jahr um 5 %. Um wie viel Prozent ist er nach 10 Jahren insgesamt gewachsen? Runde auf eine Nachkommastelle.',
                          f'1,05¹⁰ ≈ 1,6289. Das ist ein Zuwachs um etwa {dz(w)} % – mehr als 10 · 5 % = 50 %, weil auch der Zuwachs mitwächst.',
                          'Rechne den Faktor für 10 Jahre aus, nicht 10 · 5 %.', w, c, einheit='%', tol=0.1))
    neu('faktor', 3, auswahl('Angebot A: 4 % Zinsen pro Jahr. Angebot B: 2 % Zinsen pro Halbjahr (Zinseszins). Welches Angebot bringt nach einem Jahr mehr?',
                             'B, denn 1,02² = 1,0404 > 1,04.', ['A, denn 4 % sind mehr als 2 %.', 'Beide gleich viel, denn 2 · 2 % = 4 %.', 'A, denn 1,04 > 1,02².'],
                             'Bei B wird zweimal mit 1,02 multipliziert: 1,02² = 1,0404, also 4,04 % pro Jahr. Die Zinsen des ersten Halbjahrs werden mitverzinst.',
                             'Rechne den Faktor für ein ganzes Jahr bei B aus.'))
    w = gerundet((1 - 0.97 ** 10) * 100, 1)
    neu('faktor', 3, auswahl('Jemand sagt: „Nimmt ein Bestand jedes Jahr um 3 % ab, ist er nach 10 Jahren um 30 % kleiner.“ Was stimmt?',
                             f'Falsch: Er ist um etwa {dz(w)} % kleiner.', ['Richtig.', f'Falsch: Er ist um etwa {dz(gerundet(100 * 0.97 ** 10, 1))} % kleiner.', 'Falsch: Er ist um 3 % kleiner.'],
                             f'0,97¹⁰ ≈ 0,737. Es bleiben etwa 73,7 % übrig, die Abnahme beträgt also etwa {dz(w)} %. Jedes Jahr fehlen 3 % vom kleiner gewordenen Bestand.',
                             'Rechne 0,97 hoch 10.'))

    # --- modell ---
    neu('modell', 2, zahl('Für f(x) = a · b^x gilt f(2) = 18 und f(3) = 54. Bestimme a.', 'b = f(3) : f(2) = 54 : 18 = 3. Dann a = f(2) : b² = 18 : 9 = 2.',
                          'Erst b aus zwei benachbarten Werten, dann zurück bis x = 0 rechnen.', 2, '18 / (54 / 18) ** 2'))
    neu('modell', 2, zahl('Ein Stoff hat eine Halbwertszeit von 5 Tagen. Anfangs sind 80 g da: f(t) = 80 · 0,5^(t/5). Wie viel ist nach 15 Tagen übrig?',
                          'f(15) = 80 · 0,5³ = 80 · 0,125 = 10 g.', 'Wie viele Halbwertszeiten sind 15 Tage?', 10, '80 * 0.5 ** 3', einheit='g'))
    neu('modell', 3, zahl('Ein Auto ist 2 Jahre nach dem Kauf noch 19 200 € wert, nach 4 Jahren noch 12 288 €. Der Wert nimmt exponentiell ab. Wie hoch war der Neupreis?',
                          'b² = 12 288 : 19 200 = 0,64 ⇒ b = 0,8. Neupreis a = 19 200 : 0,8² = 19 200 : 0,64 = 30 000 €.',
                          'Zwischen den Werten liegen 2 Jahre: b² = Quotient. Danach 2 Jahre zurückrechnen.', 30000, '19200 / (12288 / 19200)', einheit='€'))
    neu('modell', 3, zahl('Bestand A wird durch 1 000 · 1,2^t beschrieben. Bestand B wächst jedes Jahr um 50 % und ist nach 2 Jahren genauso groß wie A. Wie groß war B am Anfang?',
                          'A nach 2 Jahren: 1 000 · 1,44 = 1 440. B: a · 1,5² = 1 440 ⇒ a = 1 440 : 2,25 = 640.',
                          'Berechne A nach 2 Jahren und setze B nach 2 Jahren gleich.', 640, '1000 * 1.2 ** 2 / 1.5 ** 2'))
    neu('modell', 3, zahl('Ein Algenteppich verdoppelt seine Fläche jeden Tag. Nach 20 Tagen bedeckt er den ganzen Teich. Nach wie vielen Tagen bedeckte er ein Viertel des Teichs?',
                          'Rückwärts: Am Tag 19 war es die Hälfte, am Tag 18 ein Viertel.', 'Denke vom Ende her: Was war einen Tag vorher?', 18, '20 - 2'))
    neu('modell', 3, zahl('Der Graph von f(x) = a · b^x geht durch (0 | 3) und (2 | 0,75). Berechne f(−1).',
                          'a = 3. b² = 0,75 : 3 = 0,25 ⇒ b = 0,5. f(−1) = 3 · 0,5^(−1) = 3 · 2 = 6.',
                          'Bestimme erst a und b, dann setze x = −1 ein.', 6, '3 / 0.5'))

    # --- graph ---
    neu('graph', 2, auswahl('Welche Wertemenge hat f(x) = 2^x − 3?', 'alle y > −3', ['alle y ≥ −3', 'alle y > 0', 'alle reellen Zahlen'],
                            '2^x nimmt alle Werte größer als 0 an, aber nie 0. Um 3 nach unten verschoben: alle Werte größer als −3. Asymptote y = −3.',
                            'Welche Werte nimmt 2^x an? Was macht „− 3“?'))
    neu('graph', 2, auswahl('Welche der Funktionen fällt (wird mit wachsendem x kleiner)?', 'f(x) = 2^(−x)', ['f(x) = −2^(−x)', 'f(x) = 0,5^(−x)', 'f(x) = 3 · 1,1^x'],
                            '2^(−x) = 0,5^x fällt. 0,5^(−x) = 2^x steigt. −2^(−x) = −0,5^x steigt (vom Negativen her gegen 0). 3 · 1,1^x steigt.',
                            'Schreibe jeden Term als a · b^x und schau auf b und das Vorzeichen von a.'))
    neu('graph', 3, auswahl('Der Graph von f(x) = 2^x wird an der x-Achse gespiegelt und danach um 4 nach oben verschoben. Welche Gleichung hat der neue Graph?',
                            'g(x) = −2^x + 4', ['g(x) = 2^(−x) + 4', 'g(x) = −2^(x + 4)', 'g(x) = −2^x − 4'],
                            'Spiegeln an der x-Achse ändert das Vorzeichen des Funktionswerts: −2^x. Verschieben nach oben addiert 4: −2^x + 4. (2^(−x) wäre die Spiegelung an der y-Achse.)',
                            'An der x-Achse spiegeln heißt: y wird zu −y.'))
    neu('graph', 3, luecken('Der Graph von g(x) = −2^x + 4 entsteht aus 2^x durch Spiegeln an der x-Achse und Verschieben. Wo schneidet er die x-Achse?', 'N(□ | □)',
                            'Koordinaten', [2, 0], '−2^x + 4 = 0 ⇒ 2^x = 4 = 2² ⇒ x = 2. Nullstelle N(2 | 0).', 'Setze g(x) = 0.', c=['2 + (-(2 ** 2) + 4)', '0']))
    neu('graph', 3, auswahl('Der Graph von f(x) = 3 · 2^x wird nach unten verschoben. Wie weit mindestens, damit er die x-Achse schneidet?',
                            'Jede Verschiebung um eine positive Zahl reicht.', ['Um mindestens 3.', 'Um mindestens 6.', 'Es geht nie, die x-Achse bleibt Asymptote.'],
                            'f nimmt alle Werte größer als 0 an, auch beliebig kleine. Verschiebt man um d > 0 nach unten, wird 3 · 2^x − d = 0 für 2^x = d/3 – das hat immer eine Lösung.',
                            'Welche Werte nimmt 3 · 2^x an? Wie nah kommt der Graph der x-Achse?'))
    neu('graph', 3, zahl('Die Graphen von f(x) = 2^x und g(x) = 8 · 0,5^x schneiden sich. Bestimme die x-Koordinate des Schnittpunkts.',
                         '0,5^x = 2^(−x). 2^x = 8 · 2^(−x) ⇒ 2^(2x) = 8 = 2³ ⇒ 2x = 3 ⇒ x = 1,5.',
                         'Schreibe 0,5^x als Potenz von 2 und bringe alles auf eine Seite.', 1.5, '3 / 2'))

    # --- logfunktion ---
    neu('logfunktion', 2, auswahl('Für welche x ist f(x) = log₂(x + 4) definiert?', 'x > −4', ['x > 4', 'x > 0', 'x ≥ −4'],
                                  'Das Argument muss positiv sein: x + 4 > 0 ⇒ x > −4.', 'Was muss für die Zahl in der Klammer gelten?'))
    neu('logfunktion', 2, zahl('Berechne f(3) für f(x) = log₃(x + 6) − 1.', 'f(3) = log₃(9) − 1 = 2 − 1 = 1.', 'Erst die Klammer, dann den Logarithmus.', 1, '2 - 1'))
    neu('logfunktion', 3, zahl('Bestimme die Nullstelle von f(x) = log₂(x − 1) − 3.', 'log₂(x − 1) = 3 ⇒ x − 1 = 2³ = 8 ⇒ x = 9.',
                               'Setze f(x) = 0 und schreibe die Gleichung als Potenz.', 9, '2 ** 3 + 1'))
    neu('logfunktion', 3, auswahl('Welche Gerade ist Asymptote des Graphen von f(x) = 2 · log₃(x + 5) − 1?', 'x = −5', ['y = −1', 'x = 5', 'y = −5'],
                                  'log₃(…) gibt es nur für x + 5 > 0. Nähert sich x der −5, fällt der Graph ohne Grenze: senkrechte Asymptote x = −5. Eine waagrechte gibt es nicht.',
                                  'Wo beginnt die Definitionsmenge? Dort liegt die Asymptote.'))
    neu('logfunktion', 3, auswahl('Welche Funktion ist die Umkehrfunktion von f(x) = 2^x + 1?', 'g(x) = log₂(x − 1)', ['g(x) = log₂(x) − 1', 'g(x) = log₂(x + 1)', 'g(x) = 1 : (2^x + 1)'],
                                  'y = 2^x + 1 ⇒ 2^x = y − 1 ⇒ x = log₂(y − 1). Variablen tauschen: g(x) = log₂(x − 1). Probe: f(2) = 5, g(5) = log₂(4) = 2.',
                                  'Löse y = 2^x + 1 nach x auf und tausche dann x und y.'))
    neu('logfunktion', 3, luecken('Welcher Punkt liegt auf dem Graphen von f(x) = log₂(x) und zugleich auf dem Graphen von g(x) = log₄(x)?', 'P(□ | □)', 'Koordinaten',
                                  [1, 0], 'log₂(x) = log₄(x) gilt nur, wenn beide 0 sind: x = 1. Für x ≠ 1 ist log₂(x) = 2 · log₄(x) ≠ log₄(x). Also P(1 | 0).',
                                  'Für welches x haben alle Logarithmusfunktionen denselben Wert?', c=['1', '0']))

    # --- zeitpunkt ---
    t = lg(10) / lg(1.2)
    neu('zeitpunkt', 2, zahl('f(t) = 50 · 1,2^t. Ab welchem ganzzahligen t ist f(t) erstmals größer als 500?',
                             f'1,2^t > 10 ⇒ t > lg 10 : lg 1,2 ≈ {dz(round(t, 2))}. Erste ganze Zahl: 13.', 'Teile durch 50, logarithmiere, runde auf.', math.floor(t) + 1, '13'))
    w, c = rz(30 * lg(0.1) / lg(0.5), 1)
    neu('zeitpunkt', 2, zahl('Ein Stoff hat eine Halbwertszeit von 30 Jahren. Nach wie vielen Jahren sind nur noch 10 % übrig? Runde auf eine Nachkommastelle.',
                             f'0,5^(t/30) = 0,1 ⇒ t = 30 · lg 0,1 : lg 0,5 ≈ {dz(w)} Jahre.', 'Ansatz 0,5^(t/30) = 0,1.', w, c, einheit='Jahre', tol=0.1))
    t = 5 * lg(400 / 240) / lg(1.25)
    neu('zeitpunkt', 3, zahl('Ein Grundstück kostete 2018 genau 240 000 € und 2023 genau 300 000 €. Der Preis steigt exponentiell. In welchem Jahr kostet es bei gleicher Entwicklung erstmals mehr als 400 000 €?',
                             f'b⁵ = 300 000 : 240 000 = 1,25. 240 000 · b^t > 400 000 ⇔ b^t > 5/3 ⇔ t > 5 · lg(5/3) : lg 1,25 ≈ {dz(round(t, 2))}. Also t = 12, das Jahr 2030.',
                             'Zähle t ab 2018. Aus 5 Jahren folgt b⁵ = 1,25.', 2018 + math.floor(t) + 1, '2018 + 12'))
    w, c = rz(lg(5 / 3) / lg(1.03 / 0.98), 1)
    neu('zeitpunkt', 3, zahl('Ort A hat 50 000 Einwohner und schrumpft jedes Jahr um 2 %. Ort B hat 30 000 Einwohner und wächst jedes Jahr um 3 %. Nach wie vielen Jahren sind es gleich viele? Runde auf eine Nachkommastelle.',
                             f'30 000 · 1,03^t = 50 000 · 0,98^t ⇒ (1,03 : 0,98)^t = 5/3 ⇒ t = lg(5/3) : lg(1,03 : 0,98) ≈ {dz(w)} Jahre.',
                             'Setze beide Terme gleich und bringe alle Potenzen mit t auf eine Seite.', w, c, einheit='Jahre', tol=0.1))
    w, c = rz(10 * lg(2) / lg(3), 1)
    neu('zeitpunkt', 3, zahl('Ein Bestand verdreifacht sich in 10 Jahren (exponentielles Wachstum). Wie lange dauert es, bis er sich verdoppelt? Runde auf eine Nachkommastelle.',
                             f'b¹⁰ = 3 ⇒ lg b = lg 3 : 10. Verdopplung: b^T = 2 ⇒ T = lg 2 : lg b = 10 · lg 2 : lg 3 ≈ {dz(w)} Jahre.',
                             'Du brauchst b nicht auszurechnen: Nutze lg b = lg 3 : 10.', w, c, einheit='Jahre', tol=0.1))
    neu('zeitpunkt', 3, auswahl('Jemand löst 80 · 1,04^t = 240 so: „t = 240 : 80 : 1,04 ≈ 2,9“. Was stimmt?', 'Falsch: 1,04^t = 3, also t = lg 3 : lg 1,04 ≈ 28,0.',
                                ['Richtig.', 'Falsch: t = 240 : 80 · 1,04 ≈ 3,1.', 'Falsch: t = (240 − 80) : 4 = 40.'],
                                't steht im Exponenten. Nach dem Teilen durch 80 bleibt 1,04^t = 3; man muss logarithmieren: t = lg 3 : lg 1,04 ≈ 28,0.',
                                'Wo steht t? Durch welche Rechnung holt man es dort heraus?'))
    return N


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('funktionen.exponential_log', 13_10_3)
# b) Fehler im Lösungsweg: „pro Jahr … in 2 Jahren“ statt „pro Stunde … in 2 Stunden“ (Lösung stimmt)
BF.loesung('faktor', 'Die Menge eines Medikaments im Blut sinkt jede Stunde um 15 %. Um welchen Faktor ändert sie sich in 2 Stunden?',
           w='Faktor pro Stunde 0,85; in 2 Stunden 0,85² = 0,7225.')
BF.loesung('faktor', 'Die Menge eines Medikaments im Blut sinkt jede Stunde um 25 %. Um welchen Faktor ändert sie sich in 2 Stunden?',
           w='Faktor pro Stunde 0,75; in 2 Stunden 0,75² = 0,5625.')
# a) Einschritt-Aufgaben → Stufe 2
for _f in ('300 · 1,04^t', '20 · 0,94^t', '5 000 · 1,01^t'):
    BF.stufe('faktor', f'Beschreibt f(t) = {_f} Wachstum oder Zerfall, und um wie viel Prozent pro Schritt?', 2)
# c) Schreibweise „1000“ statt „1 000“; Stufe 3 war nur die größere Rechnung → Stufe 2
BF.ersetze('werte', 'Berechne f(4) für f(x) = 1000 · 1,5^x.', BF.Z(
    'Berechne f(4) für f(x) = 1 000 · 1,5^x.', 5062.5, '1000 * 1.5 ** 4', '1,5⁴ = 5,0625; f(4) = 1 000 · 5,0625 = 5 062,5.',
    'Potenziere die Dezimalzahl sorgfältig (Nachkommastellen addieren sich).'), s=2)
# a) eher Stufe 2
BF.stufe('graph', 'Die Zeichnung zeigt den Graphen von g(x) = 3^x − 1. In welchem Punkt schneidet er die y-Achse?', 2)
BF.stufe('logfunktion', 'Berechne f(0,25) für f(x) = log₄(x).', 2)
BF.stufe('faktor', 'Ein Guthaben wächst jedes Jahr um 5 %. Um welchen Faktor ändert es sich in 3 Jahren?', 2)  # „in 2/3 Jahren“ der Liste = in 2 bzw. 3 Jahren

# ---- BEFUNDE ENDE ----

# ---------- Achtzehnte Runde (Zweig luecken-kl10): linear oder exponentiell? ----------
# Lücke laut Aufbau-Prüfung (inhalte/pruefung/aufbau/klasse10.json): LehrplanPLUS M10 1 verlangt, exponentielles Wachstum begründet von linearem
# abzugrenzen (gleiche Differenzen vs. gleiche Quotienten) und Modellgrenzen zu benennen. Neue Lernkarte „linear_oder_exponentiell“ nach „faktor“.
# Läuft ganz am Ende mit eigenem Zufallsstart (nur zum Mischen der Antworten); alle alten Aufgaben bleiben gleich.
# Prüfungsvorbilder (Typ und Niveau, eigene Zahlen und Einkleidung): Bayerischer Mathematik-Test Jgst. 10 (ISB; Tabellen mit Messwerten
# auf Wachstumsart prüfen, Modell fortsetzen), Grundwissen M10 bayerischer Gymnasien (Tabellen „linear oder exponentiell?“ begründen,
# Vergleich zweier Wachstumsmodelle).
_TAB_LE = {'typ': 'tabelle', 'kopf': ['Woche', 'A (m²)', 'B (m²)'], 'zeilen': [['0', '5', '5'], ['1', '10', '10'], ['2', '15', '20'], ['3', '20', '40']]}
_KS_LE = {'typ': 'koordinaten', 'x': [0, 4], 'y': [0, 90], 'schritt_y': 10, 'name_x': 'Wochen', 'name_y': 'm²',
          'graphen': [{'art': 'linear', 'm': 5, 't': 5, 'name': 'A', 'bereich': [0, 4]}, {'art': 'exp', 'a': 5, 'b': 2, 'name': 'B', 'bereich': [0, 4]}],
          'punkte': [{'x': 3, 'y': 20}, {'x': 3, 'y': 40}]}
KARTE_LIN_EXP = {
    'lernziel': 'linear_oder_exponentiell', 'titel': 'Linear oder exponentiell?',
    'einstieg': 'Zwei Teiche starten mit je 5 m² Wasserlinsen. In Teich A kommen jede Woche 5 m² dazu. In Teich B verdoppelt sich die Fläche. '
                'Gleiches Plus oder gleicher Faktor: ⟦linear⟧ oder ⟦exponentiell⟧.',
    'woerter': [['lineares Wachstum', 'in gleichen Schritten kommt immer gleich viel dazu: gleiche Differenzen'],
                ['exponentielles Wachstum', 'in gleichen Schritten wird immer mit derselben Zahl malgenommen: gleiche Quotienten'],
                ['Quotient', 'Ergebnis einer Division, hier: neuer Wert : alter Wert']],
    'bild': _TAB_LE,
    'schritte': [
        {'text': 'A: 10 − 5 = 5, 15 − 10 = 5. Gleiches Plus: ⟦lineares Wachstum⟧.',
         'bild': {'kopf': ['Woche', 'A (m²)', 'Plus'], 'zeilen': [['0', '5', ''], ['1', '10', '+ 5'], ['2', '15', '+ 5'], ['3', '20', '+ 5']]}},
        {'text': 'B: 10 : 5 = 2, 20 : 10 = 2. Gleicher Quotient: ⟦exponentielles Wachstum⟧.',
         'bild': {'kopf': ['Woche', 'B (m²)', 'mal'], 'zeilen': [['0', '5', ''], ['1', '10', '· 2'], ['2', '20', '· 2'], ['3', '40', '· 2']]}},
        {'text': 'Im Bild ist A eine Gerade, B eine immer steilere Kurve.', 'bild': _KS_LE},
        {'text': 'Nach 10 Wochen hätte B schon 5 120 m². Kein Teich ist so groß.',
         'bild': {'x': [0, 10], 'y': [0, 6000], 'schritt_y': 1000, 'schritt_x': 2,
                  'graphen': [{'art': 'linear', 'm': 5, 't': 5, 'name': 'A', 'bereich': [0, 10]}, {'art': 'exp', 'a': 5, 'b': 2, 'name': 'B', 'bereich': [0, 10]}],
                  'punkte': [{'x': 10, 'y': 5120, 'name': 'B: 5 120'}, {'x': 10, 'y': 55, 'name': 'A: 55'}]}}],
    'fehler': 'Aus 5, 10 auf „immer + 5“ zu schließen ist voreilig. Bei B folgt 20, also + 10. Prüfe ⟦mehrere Schritte⟧.',
    'fehler_bild': {'typ': 'tabelle', 'kopf': ['Woche', 'B (m²)', 'Plus'], 'zeilen': [['0', '5', ''], ['1', '10', '+ 5'], ['2', '20', '+ 10'], ['3', '40', '+ 20']]},
    'regel': 'Gleiche Differenzen: linear. ⟦Gleiche Quotienten: exponentiell⟧. Ein Modell gilt nur in einem sinnvollen Bereich.'}


def luecken_kl10():
    start(18020)
    V = []

    def neu(p, s, a):
        assert a is not None, 'zu wenige verschiedene Antworten'
        a['p'], a['s'] = p, s
        V.append(a)

    def zt_(x):
        x = Fr(x)
        return dz(x) if endlich(x) else br(x)

    def plus_t(x):
        return ('+ ' if x >= 0 else '− ') + zt_(abs(x))

    def art(ys):
        ys = [Fr(y) for y in ys]
        ds = [ys[i + 1] - ys[i] for i in range(len(ys) - 1)]
        qs = [ys[i + 1] / ys[i] for i in range(len(ys) - 1)]
        if len(set(ds)) == 1: return 'linear', ds[0], ds, qs
        if len(set(qs)) == 1: return 'exponentiell', qs[0], ds, qs
        return 'weder', None, ds, qs

    def tab(ys, name='y'):
        return {'typ': 'tabelle', 'kopf': ['x'] + [str(i) for i in range(len(ys))], 'zeilen': [[name] + [zt_(y) for y in ys]]}

    def tab_entscheiden(ys):
        typ, k, ds, qs = art(ys)
        assert typ != 'weder'
        if typ == 'linear':
            richtig = f'linear, {plus_t(k)} je Schritt'
            falsch = [f'exponentiell, Faktor {zt_(qs[0])} je Schritt', 'weder linear noch exponentiell', f'linear, {plus_t(-k)} je Schritt']
            w = f'Differenzen: {", ".join(plus_t(d) for d in ds)} – immer gleich, also linear. Die Quotienten ({", ".join(zt_(q) if endlich(q) else br(q) for q in qs[:2])}) sind verschieden.'
        else:
            richtig = f'exponentiell, Faktor {zt_(k)} je Schritt'
            falsch = [f'linear, {plus_t(ds[0])} je Schritt', 'weder linear noch exponentiell', f'exponentiell, Faktor {zt_(ds[0] if k > 1 else 1 - k)} je Schritt']
            w = f'Quotienten: {", ".join(zt_(q) for q in qs)} – immer gleich, also exponentiell. Die Differenzen ({", ".join(plus_t(d) for d in ds[:2])}) sind verschieden.'
        return mit_grafik(auswahl('Wächst oder fällt die Größe in der Tabelle linear oder exponentiell?', richtig, falsch, w,
                                  'Berechne für jeden Schritt die Differenz (neu − alt) und den Quotienten (neu : alt). Was bleibt gleich?'), tab(ys))

    def situation(text, typ):
        richtig = {'linear': 'linear', 'exp': 'exponentiell'}[typ]
        w = ('In gleichen Schritten ändert sich die Größe immer um denselben Betrag: gleiche Differenzen, also linear.' if typ == 'linear'
             else 'In gleichen Schritten wird immer mit demselben Faktor malgenommen (Prozent vom jeweiligen Wert): gleiche Quotienten, also exponentiell.')
        return auswahl(f'{text} Wie ändert sich die Größe?', richtig, ['exponentiell' if typ == 'linear' else 'linear', 'weder linear noch exponentiell'], w,
                       'Kommt in jedem Schritt derselbe Betrag dazu (bzw. weg) – oder ein fester Prozentsatz des jeweiligen Werts?')

    def weiter(ys, typ):
        a_, k, ds, qs = art(ys)
        assert a_ == typ
        n = ys[-1] + k if typ == 'linear' else Fr(ys[-1]) * k
        folge = '; '.join(zt_(y) for y in ys)
        if typ == 'linear':
            return zahl(f'Eine Größe ändert sich linear: {folge}; … Welcher Wert folgt?', f'Differenz je Schritt: {plus_t(k)}. Nächster Wert: {zt_(ys[-1])} {plus_t(k)} = {zt_(n)}.',
                        'Linear heißt: Es kommt immer derselbe Betrag dazu. Welcher?', n, f'{float(ys[-1]) if not float(ys[-1]).is_integer() else int(ys[-1])} + ({float(k) if not float(k).is_integer() else int(k)})')
        return zahl(f'Eine Größe ändert sich exponentiell: {folge}; … Welcher Wert folgt?', f'Quotient je Schritt: {zt_(ys[1])} : {zt_(ys[0])} = {zt_(k)}. Nächster Wert: {zt_(ys[-1])} · {zt_(k)} = {zt_(n)}.',
                    'Exponentiell heißt: Es wird immer mit derselben Zahl malgenommen. Mit welcher?', n, f'{zt_(ys[-1]).replace(",", ".").replace(" ", "")} * {zt_(k).replace(",", ".")}')

    def term_lin(ys):
        a_, k, ds, qs = art(ys)
        assert a_ == 'linear'
        return mit_grafik(luecken('Die Tabelle gehört zu einer linearen Funktion. Gib ihren Term an.', 'f(x) = □x + □', 'Steigung, dann Wert bei x = 0', [k, ys[0]],
                                  f'Pro Schritt {plus_t(k)}: Steigung m = {zt_(k)}. Bei x = 0 ist der Wert {zt_(ys[0])}. Also f(x) = {poly(k, ys[0])}.',
                                  'Die Steigung ist das Plus je Schritt; der Wert unter x = 0 ist f(0).', c=[f'{ys[1]} - ({ys[0]})', str(ys[0])]), tab(ys))

    def term_exp(ys):
        a_, k, ds, qs = art(ys)
        assert a_ == 'exponentiell' and Fr(k).denominator == 1
        return mit_grafik(luecken('Die Tabelle gehört zu einer Exponentialfunktion f(x) = a · b^x. Bestimme a und b.', 'a = □; b = □', 'Anfangswert und Faktor', [ys[0], int(k)],
                                  f'a = f(0) = {zt_(ys[0])}. Quotient je Schritt {zt_(ys[1])} : {zt_(ys[0])} = {zt_(k)} = b. Also f(x) = {zt_(ys[0])} · {zt_(k)}^x.',
                                  'a ist der Wert bei x = 0, b der Quotient je Schritt.', c=[str(ys[0]), f'{ys[1]} // {ys[0]}']), tab(ys))

    # ---- Stufe 1 ----
    neu('uebung', 1, tab_entscheiden([3, 6, 9, 12]))
    neu('uebung', 1, tab_entscheiden([3, 6, 12, 24]))
    neu('uebung', 1, situation('Eine Kerze ist 20 cm hoch und brennt jede Stunde um 2 cm ab.', 'linear'))
    neu('uebung', 1, situation('Ein Guthaben wächst jedes Jahr um 3 % Zinsen.', 'exp'))
    # ---- Stufe 2 ----
    neu('uebung', 2, tab_entscheiden([400, 300, 225, Fr(675, 4)]))
    neu('uebung', 2, weiter([200, 240, 288], 'exponentiell'))
    neu('uebung', 2, weiter([Fr(18, 10), Fr(25, 10), Fr(32, 10)], 'linear'))
    neu('uebung', 2, term_lin([7, 10, 13, 16]))
    neu('uebung', 2, term_exp([5, 15, 45, 135]))
    neu('uebung', 2, auswahl('Welche Beschreibung gehört zu exponentiellem Wachstum?', 'Die Zahl der Nutzer einer App steigt jeden Monat um 8 %.',
                             ['Ein Baum wird jedes Jahr um 30 cm höher.', 'Ein Tank verliert jede Minute 2 Liter.', 'Ein Taxi kostet 4 € Grundpreis und 2 € pro Kilometer.'],
                             '8 % mehr heißt: jeden Monat mal 1,08 – gleiche Quotienten. Baum, Tank und Taxi ändern sich je Schritt um denselben Betrag (linear).',
                             'Suche die Beschreibung mit einem festen Prozentsatz statt eines festen Betrags.'))
    # ---- Stufe 3 ----
    # Prüfungsvorbild BMT10: Messwerte in einer Tabelle auf exponentielles Wachstum prüfen, Wachstumsfaktor angeben, Modell fortsetzen
    ys = [2000, 2600, 3380, 4394]
    _, q, _, qs = art(ys)
    g = {'typ': 'tabelle', 'kopf': ['Monat', '0', '1', '2', '3'], 'zeilen': [['Spieler'] + [dz(y) for y in ys]]}
    neu('uebung', 3, mit_grafik(zahl('Die Tabelle zeigt, wie viele Spieler ein neues Online-Spiel in den ersten Monaten hatte. Prüfe, ob exponentielles Wachstum vorliegt, und gib den Wachstumsfaktor je Monat an.',
                                     f'Quotienten: 2 600 : 2 000 = {dz(qs[0])}, 3 380 : 2 600 = {dz(qs[1])}, 4 394 : 3 380 = {dz(qs[2])}. Immer gleich: exponentiell mit Faktor {dz(q)} (30 % mehr je Monat).',
                                     'Teile jeden Wert durch den vorigen. Sind die Quotienten gleich?', q, '2600 / 2000'), g))
    v = 2000 * 1.3 ** 5
    w5 = gerundet(v, 0)
    neu('uebung', 3, mit_grafik(zahl('Die Tabelle zeigt, wie viele Spieler ein neues Online-Spiel in den ersten Monaten hatte. Das Wachstum ist exponentiell. '
                                     'Mit wie vielen Spielern rechnet dieses Modell im Monat 5? Runde auf ganze Spieler.',
                                     f'Faktor 2 600 : 2 000 = 1,3. f(5) = 2 000 · 1,3⁵ = 2 000 · 3,71293 ≈ {dz(w5)}.', 'Stelle f(t) = a · b^t auf und setze t = 5 ein.',
                                     w5, 'round(2000 * 1.3 ** 5)', tol=1), g))
    # Knobelaufgabe: derselbe Anfang, zwei Modelle
    f0, f2 = 4, 36
    neu('uebung', 3, luecken(f'Eine Größe hat zu Beginn den Wert {f0}, nach zwei Jahren den Wert {f2}. Welchen Wert hatte sie nach einem Jahr, wenn sie linear wächst – und welchen, wenn sie exponentiell wächst?',
                             'linear: □; exponentiell: □', 'zwei ganze Zahlen', [(f0 + f2) // 2, 12],
                             f'Linear: zwei gleiche Schritte von {f0} bis {f2}, also je + {(f2 - f0) // 2}: Wert {(f0 + f2) // 2}. '
                             f'Exponentiell: zwei gleiche Faktoren mit b² = {f2} : {f0} = 9, also b = 3: Wert {f0} · 3 = 12.',
                             'Linear: gleiche Differenzen in beiden Jahren. Exponentiell: gleiche Faktoren in beiden Jahren.', c=[f'({f0} + {f2}) // 2', f'{f0} * 3']))
    # Vergleich zweier Modelle
    t = 0
    while 10 * 2 ** t <= 100 + 20 * t: t += 1
    neu('uebung', 3, zahl('Pflanze A ist 100 cm hoch und wächst jede Woche um 20 cm. Pflanze B ist 10 cm hoch und verdoppelt ihre Höhe jede Woche (Modell). '
                          'Nach wie vielen ganzen Wochen ist B zum ersten Mal höher als A?',
                          'Wertetabelle: Woche 3: A 160, B 80; Woche 4: A 180, B 160; Woche 5: A 200, B 320. Ab Woche 5 ist B höher.',
                          'Lege eine Tabelle an: A + 20 je Woche, B · 2 je Woche.', t, str(t), einheit='Wochen'))
    neu('uebung', 3, auswahl('Eine Bakterienkultur verdoppelt sich im Labor jede Stunde. Warum beschreibt das exponentielle Modell die Anzahl nach einigen Tagen nicht mehr?',
                             'Nährstoffe und Platz sind begrenzt; so viele Bakterien hätten keinen Platz.',
                             ['Weil 2^t für große t negativ wird.', 'Weil exponentielles Wachstum mit der Zeit von selbst langsamer wird.',
                              'Weil man 2^t für t > 24 nicht ausrechnen kann.'],
                             'Nach 3 Tagen (72 Stunden) wäre die Anzahl 2⁷² ≈ 4,7 · 10²¹-mal so groß. Dafür reichen Nahrung und Platz nicht: Das Modell gilt nur für einen begrenzten Zeitraum.',
                             'Rechne aus, wie groß die Anzahl nach 72 Stunden wäre. Was spricht in der Wirklichkeit dagegen?'))
    neu('uebung', 3, auswahl('Jemand sagt: „Die Werte 2, 4, 6, 8 wachsen exponentiell, weil sie sich am Anfang verdoppeln.“ Was stimmt?',
                             'Falsch: Die Differenzen sind alle + 2, also linear.',
                             ['Richtig.', 'Falsch: Die Quotienten sind alle 2, also linear.', 'Falsch: Die Werte wachsen weder linear noch exponentiell.'],
                             'Differenzen: + 2, + 2, + 2 (gleich). Quotienten: 2; 1,5; 1,33… (verschieden). Nur der erste Schritt ist eine Verdopplung – also linear.',
                             'Prüfe alle Schritte, nicht nur den ersten.'))
    # Prüfungsvorbild: Vergleich zweier Modelle mit beiden Graphen in einem Koordinatensystem
    t = 0
    while 1000 * 1.08 ** t <= 1000 + 100 * t: t += 1
    g = koord([{'art': 'linear', 'm': 100, 't': 1000, 'name': 'A', 'bereich': [0, 12]}, {'art': 'exp', 'a': 1000, 'b': 1.08, 'name': 'B', 'bereich': [0, 12]}],
              x=(0, 12), y=(0, 2600), schritt_x=1, schritt_y=200, name_x='Jahre', name_y='Mitglieder')
    neu('uebung', 3, mit_grafik(zahl('Zwei Vereine haben je 1 000 Mitglieder. Verein A gewinnt jedes Jahr 100 Mitglieder dazu, Verein B jedes Jahr 8 %. '
                                     'Nach wie vielen ganzen Jahren hat B zum ersten Mal mehr Mitglieder als A?',
                                     'A: 1 000 + 100 · t; B: 1 000 · 1,08^t. Jahr 6: A 1 600, B ≈ 1 587; Jahr 7: A 1 700, B ≈ 1 714. Also nach 7 Jahren.',
                                     'Vergleiche Jahr für Jahr; im Bild schneiden sich die Graphen.', t, str(t), einheit='Jahre'), g))
    neu('uebung', 3, auswahl('Zwei Sparkonten starten mit je 1 000 €. Konto A bekommt jedes Jahr 50 € dazu, Konto B jedes Jahr 5 % Zinsen. Welche Aussage stimmt?',
                             'Im ersten Jahr kommen bei beiden 50 € dazu, danach bei B jedes Jahr mehr.',
                             ['Bei A kommt immer mehr dazu, weil 50 € fest sind.', 'Bei beiden kommt jedes Jahr gleich viel dazu.', 'Ab dem zweiten Jahr kommt bei A mehr dazu als bei B.'],
                             'Jahr 1: 5 % von 1 000 € = 50 €, genau wie bei A. Jahr 2: 5 % von 1 050 € = 52,50 € > 50 €. Die Zinsen werden vom wachsenden Betrag berechnet.',
                             'Rechne für B das erste und das zweite Jahr aus.'))
    # ---- Test, Korrektur, Sicherung ----
    neu('test', 2, tab_entscheiden([4, 6, 9, Fr(27, 2)]))
    neu('korrektur', 2, tab_entscheiden([50, 47, 44, 41]))
    neu('korrektur', 2, weiter([500, 450, 405], 'exponentiell'))
    neu('korrektur', 2, auswahl('Welche Beschreibung gehört zu linearem Wachstum?', 'Eine Pflanze wächst jeden Tag 1,5 cm.',
                                ['Ein Kredit wächst jährlich um 4 % Zinsen.', 'Die Zahl der Erkrankten verdoppelt sich alle 3 Tage.', 'Ein Auto verliert jedes Jahr 15 % an Wert.'],
                                'Jeden Tag + 1,5 cm: gleiche Differenzen, also linear. Die anderen ändern sich um einen festen Faktor (Prozent oder Verdopplung).', 'x'))
    neu('sicherung', 2, tab_entscheiden([2, Fr(5, 2), 3, Fr(7, 2)]))
    neu('sicherung', 2, tab_entscheiden([64, 16, 4, 1]))
    neu('sicherung', 2, term_lin([12, 9, 6, 3]))
    neu('sicherung', 2, term_exp([2, 8, 32, 128]))
    neu('sicherung', 2, weiter([15, 22, 29], 'linear'))
    neu('sicherung', 2, situation('Der Luftdruck nimmt pro Kilometer Höhe um etwa 12 % ab.', 'exp'))
    return V


def luecken_einbauen():
    from _luecken_kl10 import karte_einfuegen, offen_ergaenzen
    karte_einfuegen('funktionen.exponential_log', KARTE_LIN_EXP, 'faktor', luecken_kl10())
    offen_ergaenzen('funktionen.exponential_log', 'Achtzehnte Runde (luecken-kl10): neue Lernkarte „linear_oder_exponentiell“ nach „faktor“ (LehrplanPLUS M10 1: '
                    'exponentielles von linearem Wachstum begründet abgrenzen, Modellgrenzen). Wertetabellen als „tabelle“, beide Graphen in einem Koordinatensystem.')


if __name__ == '__main__':
    datei = bauen('funktionen.exponential_log',
          'Exponentielles Wachstum und Zerfall mit f(x) = a · b^x beschreiben, Graphen deuten, Logarithmusfunktion als Umkehrung nutzen und Zeitpunkte berechnen.',
          ['f(x) = a · b^x: a = f(0) Anfangswert, b Wachstumsfaktor (b > 1 Wachstum, 0 < b < 1 Zerfall).', 'p % Zunahme: b = 1 + p/100; Abnahme: b = 1 − p/100.',
           'Graph: durch (0 | a), x-Achse als Asymptote, keine Nullstelle.', 'log_b(x) ist Umkehrfunktion von b^x, nur für x > 0; durch (1 | 0).'],
          [('Exponentialfunktion', ['werte', 'faktor', 'modell']), ('Graphen und Logarithmus', ['graph', 'logfunktion']), ('Anwenden', ['zeitpunkt'])],
          ETAPPEN, GEN, klar=KLAR,
          meiden={'werte': ['f(3) für f(x) = 5 · 2^x', 'f(−1) für f(x) = 5 · 2^x'], 'faktor': ['um 12 % ab.'], 'modell': ['400 Zellen und verdoppelt sich alle 3 h'],
                  'logfunktion': ['P(3 | 8)'], 'zeitpunkt': ['200 · 1,05^t. Für welches t ist f(t) = 300']},
          offen=['Prüfung eingearbeitet (Runde 3): realistische Raten je Größe mit passendem Pronomen, Tabelle „linear oder exponentiell?“, Modell aus Halbwertszeit, verschobene Graphen mit Zeichnung, Logarithmus im Kopf, Graph der Logarithmusfunktion, realistische Getränketemperaturen, eine Nachkommastelle immer angezeigt.',
                 'Nicht übernommen: Vorschlag (Meinung) der Prüfung, in „zeitpunkt“ die Faustregel „Verdopplungszeit ≈ 70 : p“ zu ergänzen. Die Karte ist als „ok“ bewertet; eine Näherungsregel neben der exakten Rechnung lädt dazu ein, sie auch bei großen p (wo sie ungenau wird) zu verwenden. Kann als Zusatz in einer späteren Runde kommen.',
                 'Zeichnungen: Jede Lernkarte hat ein Koordinatensystem (Exponential- und Logarithmuskurve, Spiegelung an y = x, Zielwert als waagrechte Linie). Aufgaben „Welcher Term passt zum Graphen?“ und y-Achsenabschnitt zeigen den Graphen.',
                 'Gerundete Ergebnisse mit Toleranz 0,1 bzw. 0,01; Logarithmuswerte als 12-stellige Konstanten in c.'])
    ergaenzen(datei, schwer())
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden
    luecken_einbauen()  # Achtzehnte Runde (luecken-kl10): neue Karte linear_oder_exponentiell – ganz am Ende


# ---------- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl10) ----------
# Gesamtdurchsicht: jede Lernkarte und jede Aufgabe gelesen und nachgerechnet. Läuft ganz am Ende auf der fertigen Datei.
# Stufen nach dem Gedanken (Stufe 1 = Beispiel mit anderen Zahlen, 2 = Abwandlung/Umkehrung/Einkleidung, 3 = anderer Gedanke):
# Aufgaben, die nur größere Zahlen oder dieselbe Rechnung wie Stufe 1/2 sind, werden heruntergestuft.
def durchsicht():
    from _durchsicht_kl10 import Durchsicht
    D = Durchsicht('funktionen.exponential_log', 19010)
    # werte: „Berechne f(n) für f(x) = 200 · 1,5^x“ ist das Beispiel mit größeren Zahlen → Stufe 1
    D.stufe([12, 14, 15, 16, 17], 1, 'Berechne f(')
    D.stufe(13, 1, 'Berechne f(4) für f(x) = 1 000')
    # faktor: Faktor in 2 Stunden = derselbe Gedanke wie „Faktor in 3 Jahren“ (Stufe 2)
    D.stufe([42, 43], 2, 'Die Menge eines Medikaments')
    # modell: Halbwertszeit mit glatter Zahl = Beispiel (Verdoppeln) rückwärts, eine Einkleidung → Stufe 2
    D.stufe([72, 73], 2, 'Ein Medikament hat eine Halbwertszeit')
    # graph: Stufe 2 wiederholte Stufe 1 (Term aus Graph, steigend/fallend, y-Achsenabschnitt) → Stufe 1;
    # „keine Nullstelle“ auf Stufe 3 ist dieselbe Frage wie auf Stufe 2 → Stufe 2
    D.stufe([91, 92, 93], 1, 'Welcher Funktionsterm')
    D.stufe(94, 1, 'Ist der Graph von')
    D.stufe(95, 1, 'In welchem Punkt schneidet')
    D.stufe([99, 101], 2, 'Welche Aussage über den Graphen')
    # logfunktion: Werte mit dem Rechner und reine Merkfakten (Asymptote, Punkt (1 | 0)) sind kein anderer Gedanke
    D.stufe(129, 1, 'Berechne f(95) für f(x) = lg')
    D.stufe([124, 126], 2, 'Berechne f(')
    D.stufe(127, 2, 'Die Zeichnung zeigt den Graphen von f(x) = lg')
    D.stufe(128, 2, 'Durch welchen Punkt')
    # zeitpunkt: sechsmal „heißes Getränk“ = Stufe-1-Rechnung in einer Einkleidung → Stufe 2
    D.stufe(range(152, 158), 2, 'Ein heißes Getränk')
    # Lernkarte zeitpunkt: Sprung von „Logarithmieren“ direkt zu t = lg 1,5 : lg 1,05 – die Potenzregel fehlte als Schritt
    D.karte('zeitpunkt',
            woerter=[['Zeitpunkt', 'die Zeit t, zu der ein Wert erreicht wird'],
                     ['Logarithmieren', 'den Logarithmus bilden, um an den Exponenten zu kommen'],
                     ['lg', 'der Logarithmus zur Basis 10; am Rechner die Taste „log“']],
            schritte=[{'text': 'Gesucht ist t mit 200 · 1,05^t = 300.'},
                      {'text': 'Durch 200 teilen, damit die Potenz allein steht: 1,05^t = 1,5.'},
                      {'text': 'Logarithmieren, also auf beiden Seiten lg nehmen: lg(1,05^t) = lg 1,5.'},
                      {'text': 'Der Exponent t darf vor das lg: t · lg 1,05 = lg 1,5.'},
                      {'text': 'Durch lg 1,05 teilen: t = lg 1,5 : lg 1,05 ≈ ⟦8,3⟧ Jahre.',
                       'bild': {'senkrecht': [8.3], 'punkte': [{'x': 8.3, 'y': 300, 'name': '≈ 8,3 Jahre'}]}}])
    D.fuer_nutzer('funktionen.exponential_log/zeitpunkt und gleichungen.exponential (wachstum, mit_log_loesen) überschneiden sich: Beide lösen a · b^t = c mit dem Logarithmus. '
                     'exponential_log steht in der Reihenfolge vor gleichungen.exponential, nutzt die Potenzregel also, bevor sie dort erklärt wird (jetzt als Schritt auf der Karte).')
    D.anwenden()


if __name__ == '__main__':
    durchsicht()  # Neunzehnte Runde (durchsicht-kl10) – ganz am Ende


# ---------- STUFEN (Zwanzigste Runde, Zweig stufen-kl10) ----------
# Jede Übung bekommt ihren Aufgabentyp g; neue Übungen nach Typ, je Lernkarte zwei Knobel-Bordkarten. Läuft ganz am Ende.
def stufen():
    import math
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _stufen_kl10 import Stufen
    S = Stufen('funktionen.exponential_log', 2010)
    Z, A, L, ZR = S.Z, S.A, S.L, S.ZR
    lg = math.log10

    # --- werte ---
    S.stufenleiter('werte', 'f(x) = a · bˣ für ganze x ausrechnen und a, b im Term erkennen.',
                   'Negative Exponenten, Summen von Funktionswerten, Werte in Sachsituationen, x aus einem einfachen Wert.',
                   'Rückwärts zu a, Fehler finden, Aussagen prüfen, Parameter, ein Modell selbst aufstellen.')
    S.g('werte', direkt=[0, 1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 17, 6, 7, 8, 9, 10, 11, 168], umkehr=[169, 172],
        pruefung=[170], rueckwaerts=[171], verknuepfen=[173])
    S.neu('werte', 'erkennen', A('Welcher Term beschreibt eine Exponentialfunktion mit dem Anfangswert 3 und dem Wachstumsfaktor 4?', '3 · 4^x',
                                 ['4 · 3^x', '3 · x⁴', '3 + 4x'], 'Anfangswert a vorn, Wachstumsfaktor b als Basis: f(x) = 3 · 4^x.', 'Form a · b^x: Wo steht der Faktor, wo die Basis?'))
    S.neu('werte', 'erkennen', A('Bei f(x) = 0,5 · 6^x: Was ist der Anfangswert, was der Wachstumsfaktor?', 'Anfangswert 0,5, Wachstumsfaktor 6',
                                 ['Anfangswert 6, Wachstumsfaktor 0,5', 'Anfangswert 3, Wachstumsfaktor 6', 'Anfangswert 0,5, Wachstumsfaktor 3'],
                                 'f(0) = 0,5 · 6⁰ = 0,5 ist der Anfangswert; die Basis 6 ist der Wachstumsfaktor.', 'Setze x = 0 ein.'))
    S.neu('werte', 'mehrschritt', Z('Berechne f(2) − f(−2) für f(x) = 8 · 2^x.', 30, '8 * 2 ** 2 - 8 * 2 ** (-2)',
                                    'f(2) = 8 · 4 = 32; f(−2) = 8 · 1/4 = 2; Differenz 32 − 2 = 30.', 'Rechne beide Werte einzeln aus. 2^(−2) = 1/4.'))
    S.neu('werte', 'mehrschritt', Z('f(x) = 9 · (1/3)^x. Berechne die Summe f(−2) + f(2).', 82, '9 * 3 ** 2 + 9 * Fraction(1, 9)'.replace('Fraction(1, 9)', '(1 / 9)'),
                                    '(1/3)^(−2) = 3² = 9, also f(−2) = 81; (1/3)² = 1/9, also f(2) = 1. Summe 82.', 'Ein negativer Exponent dreht den Bruch um.'))
    S.neu('werte', 'einkleidung', Z('Ein Guthaben wächst nach K(t) = 2 500 · 1,02^t (K in €, t in Jahren). Wie viel Euro sind nach 3 Jahren auf dem Konto? Runde auf Cent.',
                                    2653.02, 'round(2500 * 1.02 ** 3, 2)', 'K(3) = 2 500 · 1,02³ = 2 500 · 1,061208 ≈ 2 653,02 €.',
                                    'Setze t = 3 ein: erst 1,02³, dann mal 2 500.', einheit='€', toleranz=0.01))
    S.neu('werte', 'einkleidung', Z('Die Zahl der Pilze auf einer Wiese wird durch P(t) = 40 · 3^t beschrieben (t in Tagen). Wie viele Pilze sind es nach 4 Tagen?',
                                    3240, '40 * 3 ** 4', 'P(4) = 40 · 3⁴ = 40 · 81 = 3 240.', 'Erst 3⁴, dann mal 40.'))
    S.neu('werte', 'fehler', A('Jemand rechnet für f(x) = 4 · 3^x: „f(2) = 12² = 144“. Was stimmt?', 'Falsch: Erst 3² = 9, dann mal 4, also f(2) = 36.',
                               ['Richtig: f(2) = 144.', 'Falsch: Richtig wäre 4² · 3 = 48.', 'Falsch: Richtig wäre 4 · 3 · 2 = 24.'],
                               'Der Exponent gehört nur zur Basis 3: f(2) = 4 · 3² = 4 · 9 = 36. (4 · 3)² wäre ein anderer Term.', 'Wozu gehört der Exponent?'))
    S.neu('werte', 'begruenden', A('Stimmt die Aussage: „Für jede Funktion f(x) = a · 2^x gilt f(x + 1) = f(x) + 2“?',
                                   'Nein: f(x + 1) = 2 · f(x). Beispiel a = 1, x = 3: f(4) = 16, aber f(3) + 2 = 10.',
                                   ['Ja, weil der Wachstumsfaktor 2 ist.', 'Ja, aber nur für a = 1.', 'Nein: f(x + 1) = f(x) + a.'],
                                   'f(x + 1) = a · 2^(x + 1) = a · 2^x · 2 = 2 · f(x). Ein Gegenbeispiel genügt, um die Aussage zu widerlegen.',
                                   'Setze Zahlen ein, z. B. a = 1 und x = 3.'))
    S.neu('werte', 'parameter', Z('Für welche Basis b > 0 hat f(x) = 3 · b^x an der Stelle x = 2 denselben Wert wie g(x) = 12 · 2^x an der Stelle x = 0?', 2, '2',
                                  'g(0) = 12. Also 3 · b² = 12, b² = 4, b = 2 (b > 0).', 'Rechne g(0) aus und stelle eine Gleichung für b auf.'))
    S.neu('werte', 'transfer', Z('Ein Gerücht: Am Montag kennen es 3 Personen. Jeden Tag erzählt jede Person, die es kennt, es 2 neuen Personen. Wie viele Personen kennen es am Montag eine Woche später?',
                                 6561, '3 * 3 ** 7', 'Jeden Tag verdreifacht sich die Zahl (jeder Kenner plus zwei neue). Nach 7 Tagen: 3 · 3⁷ = 3 · 2 187 = 6 561.',
                                 'Um welchen Faktor wächst die Zahl an einem Tag?'))
    S.neu('werte', 'verknuepfen', Z('f(x) = 2^x. Für welches x ist f(x) = √8?', 1.5, '3 / 2', '√8 = 8^(1/2) = (2³)^(1/2) = 2^(3/2). Also x = 3/2 = 1,5.',
                                    'Schreibe 8 als Zweierpotenz und die Wurzel als Hochzahl 1/2.'))
    S.bonus('werte', Z('f(x) = 3^x. Für wie viele ganze Zahlen x liegt f(x) zwischen 0,001 und 1 000?', 13, '6 - (-6) + 1',
                       '3⁶ = 729 < 1 000 < 2 187 = 3⁷, also x ≤ 6. Für negative x ist 3^(−n) = 1/3ⁿ: 1/729 ≈ 0,00137 > 0,001, aber 1/2 187 < 0,001, also x ≥ −6. '
                       'Die ganzen Zahlen von −6 bis 6 sind 13 Stück.', 'Was passiert mit 3^x, wenn x das Vorzeichen wechselt?'))
    S.bonus('werte', Z('Für f(x) = a · b^x mit a > 0 und b > 0 gilt f(1) · f(3) = 144. Berechne f(2).', 12, '12',
                       'f(1) · f(3) = a · b · a · b³ = a² · b⁴ = (a · b²)² = f(2)². Also f(2)² = 144 und f(2) = 12, weil f(2) > 0. '
                       'Man braucht a und b gar nicht einzeln.', 'Schreibe f(1) · f(3) und f(2)² mit a und b und vergleiche.'))

    # --- faktor ---
    S.stufenleiter('faktor', 'Aus „+ p %“ oder „− p %“ den Faktor b bilden und im Term Wachstum oder Zerfall erkennen.',
                   'Aus b den Prozentsatz zurückgewinnen, Faktoren über mehrere Jahre, Prozentsatz aus einer Tabelle.',
                   'Rückwärts zum Anfangswert, Aussagen und Fehler zu Prozenten prüfen, Parameter p, Wurzel als Faktor je Stunde, Prüfungsaufgabe.')
    S.g('faktor', direkt=[28, 29, 31, 30, 32, 33], erkennen=[40, 41, 44], umkehr=[34, 36, 37, 39, 35, 38, 174],
        mehrschritt=[42, 43, 45, 175, 177], verknuepfen=[176], begruenden=[178], fehler=[179])
    S.ueberzaehlig(30, 32, 33, 38)
    S.neu('faktor', 'erkennen', A('Welcher Wachstumsfaktor beschreibt eine Abnahme?', '0,98', ['1,08', '1,8', '2,1'],
                                  'Abnahme heißt: Es bleibt weniger als 100 % übrig, also b < 1. Nur 0,98 ist kleiner als 1 (Abnahme um 2 %).', 'Ist der Faktor größer oder kleiner als 1?'))
    S.neu('faktor', 'darstellung', Z('Ein Bestand: Jahr 0: 5 000, Jahr 1: 4 600, Jahr 2: 4 232. Um wie viel Prozent nimmt er pro Jahr ab?', 8, '(1 - Fraction(4600, 5000)) * 100'.replace('Fraction(4600, 5000)', '(4600 / 5000)'),
                                     '4 600 : 5 000 = 0,92 und 4 232 : 4 600 = 0,92. Übrig bleiben 92 %, also Abnahme um 8 %.', 'Teile zwei aufeinanderfolgende Werte.', einheit='%'))
    S.neu('faktor', 'rueckwaerts', Z('Ein Gebrauchtwagen hat zwei Jahre lang jedes Jahr 12 % an Wert verloren und kostet jetzt 15 488 €. Wie viel kostete er vor zwei Jahren?',
                                     20000, '15488 / 0.88 ** 2', 'Faktor je Jahr 0,88. Jetzt = Preis · 0,88², also Preis = 15 488 : 0,7744 = 20 000 €.',
                                     'Teile rückwärts durch den Faktor – einmal je Jahr.', einheit='€'))
    S.neu('faktor', 'parameter', Z('Ein Guthaben wird ein Jahr lang mit p % verzinst. Für welches p ist es danach genauso groß wie ein gleich großes Guthaben, das zwei Jahre lang mit 5 % verzinst wird (Zinseszins)?',
                                   10.25, '(1.05 ** 2 - 1) * 100', '1 + p/100 = 1,05² = 1,1025, also p = 10,25.', 'Setze die beiden Faktoren gleich.', einheit='%'))
    S.neu('faktor', 'transfer', Z('Ein Blatt Papier ist 0,1 mm dick. Bei jedem Falten verdoppelt sich die Dicke des Stapels. Nach wie vielen Faltungen wäre er zum ersten Mal dicker als 1 m?',
                                  14, '14', '1 m = 1 000 mm. Gesucht: 0,1 · 2ⁿ > 1 000, also 2ⁿ > 10 000. 2¹³ = 8 192 reicht nicht, 2¹⁴ = 16 384 reicht: 14 Faltungen.',
                                  'Rechne in Millimetern und probiere Zweierpotenzen.', einheit='Faltungen'))
    S.neu('faktor', 'pruefung', A('Ein Bestand wird durch f(t) = 6 000 · 0,95^t beschrieben (t in Jahren). Welcher Term gibt an, um wie viel Prozent er in den ersten 3 Jahren insgesamt abnimmt?',
                                  '(1 − 0,95³) · 100 %', ['3 · 5 %', '0,95³ · 100 %', '(0,95 − 0,05³) · 100 %'],
                                  'Nach 3 Jahren ist der Faktor 0,95³ ≈ 0,857; es fehlen 1 − 0,857 ≈ 0,143, also etwa 14,3 %. 3 · 5 % = 15 % übersieht, dass die Prozente vom kleineren Rest genommen werden.',
                                  'Welcher Anteil ist nach 3 Jahren noch da, welcher fehlt?'))
    S.neu('faktor', 'begruenden', A('Ein Preis steigt erst um 10 % und dann um 20 %. Ein zweiter, gleich hoher Preis steigt erst um 20 % und dann um 10 %. Was gilt?',
                                    'Beide steigen insgesamt gleich stark, um 32 %.', ['Der erste steigt insgesamt stärker.', 'Der zweite steigt insgesamt stärker.', 'Beide steigen insgesamt um 30 %.'],
                                    '1,1 · 1,2 = 1,2 · 1,1 = 1,32. Die Reihenfolge der Faktoren ist egal; die Zunahme ist 32 %, nicht 30 %.', 'Schreibe beide Änderungen als Faktoren.'))
    S.bonus('faktor', Z('Ein Bestand wächst drei Jahre lang jedes Jahr um 25 % und nimmt danach drei Jahre lang jedes Jahr um 20 % ab. Wie viel Prozent des Anfangswerts sind es am Ende?',
                        100, '(Fraction(5, 4) * Fraction(4, 5)) ** 3 * 100'.replace('Fraction(5, 4)', '(5 / 4)').replace('Fraction(4, 5)', '(4 / 5)'),
                        'Faktoren: 1,25³ · 0,8³ = (1,25 · 0,8)³. Und 1,25 · 0,8 = 5/4 · 4/5 = 1. Also ist der Bestand am Ende genau so groß wie am Anfang: 100 %.',
                        'Ordne die sechs Faktoren geschickt zu Paaren.', einheit='%'))
    S.bonus('faktor', Z('Ein Kapital wird jedes Jahr mit 8 % verzinst (Zinseszins). Nach wie vielen ganzen Jahren hat es sich zum ersten Mal mehr als verdoppelt?', 10, '10',
                        '1,08² = 1,1664; 1,08⁴ = 1,1664² ≈ 1,3605; 1,08⁸ ≈ 1,3605² ≈ 1,8509; 1,08⁹ = 1,08⁸ · 1,08 ≈ 1,9990 – knapp unter 2! 1,08¹⁰ ≈ 1,9990 · 1,08 ≈ 2,1589. '
                        'Also erst nach 10 Jahren. Weil 1,08⁹ so knapp unter 2 liegt, muss man hier genau rechnen.', 'Quadriere geschickt: erst 1,08², dann 1,08⁴ = (1,08²)², dann 1,08⁸. Prüfe die Grenze genau.', einheit='Jahre'))

    # --- linear_oder_exponentiell ---
    S.stufenleiter('linear_oder_exponentiell', 'Differenzen und Quotienten bilden, lineares und exponentielles Wachstum erkennen.',
                   'Folgen fortsetzen, Terme aus Tabellen, Sachsituationen einem Modell zuordnen und rechnen.',
                   'Modelle vergleichen und Zeitpunkte bestimmen, Grenzen eines Modells begründen, Fehler finden, Parameter, Prüfungsaufgabe mit Tabelle.')
    S.g('linear_oder_exponentiell', erkennen=[204, 205, 206, 207, 213, 208], mehrschritt=[209, 210], darstellung=[211, 212, 214],
        pruefung=[215], rueckwaerts=[216], transfer=[217, 220], begruenden=[218, 221], fehler=[219])
    S.ueberzaehlig(205, 208)
    S.neu('linear_oder_exponentiell', 'direkt', Z('Bei den Werten 3; 6; 12; 24 ist der Quotient aufeinanderfolgender Werte immer gleich. Wie groß ist er?', 2, '6 / 3',
                                                  '6 : 3 = 12 : 6 = 24 : 12 = 2.', 'Teile jeden Wert durch seinen Vorgänger.'))
    S.neu('linear_oder_exponentiell', 'direkt', Z('Bei den Werten 7; 11; 15; 19 ist die Differenz aufeinanderfolgender Werte immer gleich. Wie groß ist sie?', 4, '11 - 7',
                                                  '11 − 7 = 15 − 11 = 19 − 15 = 4.', 'Ziehe jeden Wert von seinem Nachfolger ab.'))
    S.neu('linear_oder_exponentiell', 'direkt', Z('Eine Größe wächst exponentiell mit dem Faktor 1,5 je Schritt. Heute hat sie den Wert 40. Welchen Wert hat sie nach einem Schritt?', 60, '40 * 1.5',
                                                  'Neuer Wert = 40 · 1,5 = 60.', 'Exponentiell heißt: mit dem Faktor malnehmen.'))
    S.neu('linear_oder_exponentiell', 'einkleidung', ZR('Ein Tee kühlt ab. Seine Übertemperatur (über der Raumtemperatur) beträgt 80 °C, 64 °C und 51,2 °C, gemessen im Abstand von je 5 Minuten. '
                                                       'Die Abnahme ist exponentiell. Welche Übertemperatur ist 5 Minuten nach der letzten Messung zu erwarten? Runde auf eine Nachkommastelle.',
                                                       51.2 * 0.8, 1, '64 : 80 = 0,8 und 51,2 : 64 = 0,8. Nächster Wert: 51,2 · 0,8 = 40,96 ≈ 41,0 °C.', 'Bestimme den Faktor je 5 Minuten.', einheit='°C'))
    S.neu('linear_oder_exponentiell', 'einkleidung', Z('Eine Kerze ist 24 cm lang und nach 2 Stunden noch 21 cm. Sie brennt gleichmäßig ab. Nach wie vielen Stunden (vom Anzünden an) ist sie ganz abgebrannt?',
                                                      16, '24 / ((24 - 21) / 2)', 'Gleichmäßig heißt linear: 3 cm in 2 h, also 1,5 cm je Stunde. 24 : 1,5 = 16 Stunden.',
                                                      'Wie viele Zentimeter brennen in einer Stunde ab?', einheit='h'))
    S.neu('linear_oder_exponentiell', 'parameter', Z('f(x) = 2 · b^x und g(x) = 2 + 6x haben an der Stelle x = 1 denselben Wert. Für welche Basis b gilt das?', 4, '(2 + 6) / 2',
                                                    'g(1) = 8. Also 2 · b = 8 und b = 4.', 'Setze x = 1 in beide Terme ein.'))
    S.bonus('linear_oder_exponentiell', Z('Auf das erste Feld eines Schachbretts legt man 1 Reiskorn, auf jedes weitere Feld doppelt so viele wie auf das vorige. Auf welchem Feld liegen zum ersten Mal mehr als eine Million Körner?',
                                          21, '21', 'Auf Feld n liegen 2^(n − 1) Körner. Idee: 2¹⁰ = 1 024 ≈ 1 000, also 2²⁰ = 1 024² = 1 048 576 > 1 000 000, aber 2¹⁹ = 524 288 zu wenig. '
                                          'Feld n mit n − 1 = 20: Feld 21.', 'Merke dir 2¹⁰ ≈ 1 000. Achtung: Auf Feld 1 liegt 2⁰.'))
    S.bonus('linear_oder_exponentiell', Z('Größe A wächst linear: 1 000; 1 100; 1 200; … Größe B wächst exponentiell: 1; 2; 4; 8; … (beide je Schritt, Start bei Schritt 0). Nach wie vielen Schritten ist B zum ersten Mal größer als A?',
                                          12, '12', 'Nach n Schritten: A = 1 000 + 100n, B = 2ⁿ. n = 10: 1 024 < 2 000. n = 11: 2 048 < 2 100 (knapp!). n = 12: 4 096 > 2 200. Also nach 12 Schritten.',
                                          'Stelle beide Terme auf und vergleiche bei n = 10, 11, 12.'))

    # --- modell ---
    S.stufenleiter('modell', 'Ein Verdopplungsmodell auswerten und erkennen, welche Formel zu einer Beschreibung passt.',
                   'Den Faktor b aus zwei Werten bestimmen, Halbwertszeiten auswerten, a und b aus Tabellenwerten.',
                   'Aus zwei Punkten rückwärts, Fehler im Modell, Parameter T, Modelle vergleichen, Prüfungsaufgabe mit Prognose.')
    S.g('modell', direkt=[56, 57, 58, 59, 60, 61], erkennen=[65, 67], umkehr=[62, 63, 64, 66], einkleidung=[72, 73, 181], mehrschritt=[180, 69, 185],
        rueckwaerts=[68, 71, 182], transfer=[184], verknuepfen=[183])
    S.ueberzaehlig(60, 70)
    S.g('modell', rueckwaerts=[70])
    S.neu('modell', 'erkennen', A('Welche Formel beschreibt 500 Bakterien, die sich alle 4 Stunden verdoppeln (t in Stunden)?', 'f(t) = 500 · 2^(t/4)',
                                  ['f(t) = 500 · 2^(4t)', 'f(t) = 500 · 4^t', 'f(t) = 500 · 2 · t/4'],
                                  'Bis zur Zeit t wurde (t : 4)-mal verdoppelt: f(t) = 500 · 2^(t/4).', 'Wie oft wurde nach t Stunden verdoppelt?'))
    S.neu('modell', 'erkennen', A('f(t) = 60 · 0,5^(t/8) beschreibt die Menge eines Stoffs in Gramm (t in Tagen). Was bedeutet die 8?',
                                  'Halbwertszeit: Nach 8 Tagen ist noch die Hälfte da.', ['Jeden Tag gehen 8 % verloren.', 'Nach 8 Tagen ist nichts mehr da.', 'Am Anfang sind 8 g da.'],
                                  'Für t = 8 ist der Exponent 1: f(8) = 60 · 0,5 = 30, die Hälfte von 60.', 'Setze t = 8 ein.'))
    S.neu('modell', 'fehler', A('Jemand beschreibt 200 Zellen, die sich alle 6 Stunden verdoppeln, mit f(t) = 200 · 2^(6t) (t in Stunden). Was stimmt?',
                                'Falsch: Nach t Stunden wurde t/6-mal verdoppelt, also f(t) = 200 · 2^(t/6).',
                                ['Richtig.', 'Falsch: f(t) = 200 · 6^(2t).', 'Falsch: f(t) = 200 · 2 · 6t.'],
                                'Probe mit t = 6: 2^(6 · 6) wäre 2³⁶-mal so viel, nach 6 Stunden ist es aber nur das Doppelte. 2^(t/6) gibt für t = 6 genau 2.', 'Mach die Probe mit t = 6.'))
    S.neu('modell', 'parameter', Z('Ein Bestand wird durch f(t) = 100 · 2^(t/T) beschrieben (t in Stunden). Nach 12 Stunden sind es 800. Bestimme die Verdopplungszeit T in Stunden.',
                                   4, '12 / 3', '100 · 2^(12/T) = 800 ⇒ 2^(12/T) = 8 = 2³ ⇒ 12/T = 3 ⇒ T = 4.', 'Teile durch 100 und schreibe 8 als Zweierpotenz.', einheit='h'))
    S.neu('modell', 'pruefung', ZR('In einem See leben zu Beginn 1 200 Fische, nach einem Jahr 1 380. Man nimmt exponentielles Wachstum an. Mit wie vielen Fischen rechnet dieses Modell nach 4 Jahren? Runde auf ganze Fische.',
                                   1200 * 1.15 ** 4, 0, 'Faktor b = 1 380 : 1 200 = 1,15. f(4) = 1 200 · 1,15⁴ ≈ 1 200 · 1,749 ≈ 2 099 Fische.',
                                   'Erst den Faktor je Jahr bestimmen, dann das Modell auswerten.'))
    S.bonus('modell', Z('Ein Seerosenteppich verdreifacht seine Fläche jede Woche. Beginnt man mit einer Seerose, ist der Teich nach 9 Wochen bedeckt. Nach wie vielen Wochen wäre er bedeckt, wenn man mit 3 Seerosen beginnt?',
                        8, '9 - 1', 'Mit 3 Seerosen hat man von Anfang an den Stand, den eine einzelne Seerose erst nach einer Woche erreicht. Man ist also immer eine Woche voraus: 9 − 1 = 8 Wochen.',
                        'Wann hätte die einzelne Seerose genau 3 Seerosen?', einheit='Wochen'))
    S.bonus('modell', Z('Kultur A beginnt mit 100 Zellen und verdoppelt sich jede Stunde. Kultur B beginnt mit 800 Zellen und verdoppelt sich alle 2 Stunden. Nach wie vielen Stunden sind beide gleich groß?',
                        6, '6', '100 · 2^t = 800 · 2^(t/2) ⇒ 2^t : 2^(t/2) = 2^(t/2) = 8 = 2³ ⇒ t = 6. Probe: A = 100 · 64 = 6 400, B = 800 · 8 = 6 400.',
                        'Teile beide Seiten durch 100 und durch 2^(t/2).', einheit='h'))

    # --- graph ---
    S.stufenleiter('graph', 'Den y-Achsenabschnitt ablesen, steigend/fallend erkennen, Term und Graph zuordnen.',
                   'Aussagen über Graphen prüfen, verschobene Graphen (Schnittpunkt, Asymptote, Wertemenge), Graph aus Spiegelung und Verschiebung.',
                   'Spiegeln mit Potenzgesetzen erklären, Nullstellen verschobener Graphen, Schnittpunkte, Parameter aus Asymptote, Fehler, Prüfungsaufgabe.')
    S.g('graph', direkt=[84, 85, 89, 95], erkennen=[86, 87, 91, 92, 93, 88, 94], darstellung=[90, 99, 101, 188], umkehr=[187], mehrschritt=[96, 97, 186],
        verknuepfen=[98, 100, 189], begruenden=[190], transfer=[191])
    S.neu('graph', 'fehler', A('Jemand sagt: „Der Graph von f(x) = 2 · 3^x schneidet die y-Achse bei (0 | 3), denn die Basis ist 3.“ Was stimmt?',
                               'Falsch: f(0) = 2 · 3⁰ = 2, also (0 | 2).', ['Richtig.', 'Falsch: Er schneidet sie bei (0 | 6).', 'Falsch: Er schneidet die y-Achse nicht.'],
                               '3⁰ = 1, also f(0) = 2 · 1 = 2. Der y-Achsenabschnitt ist der Anfangswert a, nicht die Basis.', 'Setze x = 0 ein.'))
    S.neu('graph', 'parameter', Z('Der Graph von f(x) = a · 2^x + c hat die Asymptote y = −3 und schneidet die y-Achse bei (0 | 5). Bestimme a.', 8, '5 - (-3)',
                                  'Die Asymptote ist y = c, also c = −3. f(0) = a + c = 5, also a = 8.', 'Was bewirkt c am Graphen? Setze dann x = 0 ein.'))
    S.neu('graph', 'pruefung', Z('Gegeben ist f(x) = 4 − 2^(x + 1). Berechne die Nullstelle von f.', 1, '2 - 1',
                                 '4 − 2^(x + 1) = 0 ⇒ 2^(x + 1) = 4 = 2² ⇒ x + 1 = 2 ⇒ x = 1.', 'Setze f(x) = 0 und schreibe 4 als Zweierpotenz.'))
    S.bonus('graph', A('Wie viele gemeinsame Punkte haben die Graphen von f(x) = 2^x und g(x) = x²?', '3', ['1', '2', '4'],
                       'Rechts: x = 2 (4 = 4) und x = 4 (16 = 16), dazwischen ist x² größer, danach wächst 2^x schneller. Links (x < 0) fällt x² von großen Werten auf 0, '
                       '2^x liegt zwischen 0 und 1: Bei x = −1 ist x² = 1 > 0,5, bei x = 0 ist x² = 0 < 1 – also noch ein Schnittpunkt (bei etwa −0,77). Zusammen 3.',
                       'Prüfe auch negative x – vergleiche Werte bei x = −1 und x = 0.'))
    S.bonus('graph', Z('Für wie viele ganze Zahlen n liegt der Punkt (n | 1 000) zwischen den Graphen von f(x) = 2^x und g(x) = 3^x, das heißt 2ⁿ < 1 000 < 3ⁿ?', 3, '9 - 7 + 1',
                       '2ⁿ < 1 000 gilt bis n = 9 (2⁹ = 512, 2¹⁰ = 1 024). 3ⁿ > 1 000 gilt ab n = 7 (3⁶ = 729, 3⁷ = 2 187). Beides: n = 7, 8, 9 – drei Zahlen.',
                       'Bestimme die Grenzen für beide Bedingungen getrennt.'))

    # --- logfunktion ---
    S.stufenleiter('logfunktion', 'Einfache Logarithmen als Hochzahl ablesen und Eigenschaften des Graphen (x > 0, (1 | 0), Asymptote) erkennen.',
                   'Negative Logarithmen, Punkte der Umkehrfunktion, Werte mit dem Rechner, verschobene Logarithmusfunktionen.',
                   'Nullstellen und Punkte rückwärts, Umkehrfunktion bilden, Basis als Parameter, Fehler, Abschätzen, Dezibel als Sachmodell.')
    S.g('logfunktion', direkt=[112, 113, 114, 115, 116, 117, 129], erkennen=[118, 127, 128], mehrschritt=[119, 122, 125, 124, 126, 193],
        darstellung=[120, 121, 123, 195], umkehr=[192], rueckwaerts=[194, 196], begruenden=[197])
    S.ueberzaehlig(113, 115, 117, 125, 126)
    S.neu('logfunktion', 'fehler', A('Jemand rechnet: „log₂(8 + 8) = log₂(8) + log₂(8) = 3 + 3 = 6.“ Was stimmt?', 'Falsch: log₂(16) = 4, denn 2⁴ = 16.',
                                     ['Richtig.', 'Falsch: Es ist 3 · 3 = 9.', 'Falsch: log₂(16) = 8.'],
                                     'log₂(16) fragt: 2 hoch wie viel ist 16? Antwort 4. Den Logarithmus einer Summe darf man nicht in eine Summe von Logarithmen zerlegen.', 'Rechne erst 8 + 8 aus.'))
    S.neu('logfunktion', 'parameter', Z('Der Graph von f(x) = log_b(x) geht durch den Punkt (81 | 4). Bestimme die Basis b.', 3, '3',
                                       'log_b(81) = 4 heißt b⁴ = 81 = 3⁴, also b = 3.', 'Schreibe die Logarithmus-Aussage als Potenz.'))
    S.neu('logfunktion', 'pruefung', Z('Gegeben ist f(x) = log₂(x + 2) + 1. Der Punkt P(x | 4) liegt auf dem Graphen von f. Berechne x.', 6, '2 ** 3 - 2',
                                       'log₂(x + 2) + 1 = 4 ⇒ log₂(x + 2) = 3 ⇒ x + 2 = 2³ = 8 ⇒ x = 6.', 'Setze f(x) = 4 und stelle nach dem Logarithmus um.'))
    S.neu('logfunktion', 'verknuepfen', L('Zwischen welchen zwei aufeinanderfolgenden ganzen Zahlen liegt log₃(50)?', '□ < log₃(50) < □', [3, 4], ['3', '4'],
                                          '3³ = 27 < 50 < 81 = 3⁴, also liegt log₃(50) zwischen 3 und 4.', 'Zwischen welchen Dreierpotenzen liegt 50?'))
    S.neu('logfunktion', 'transfer', Z('Die Lautstärke in Dezibel ist L = 10 · lg(I : I₀). Ein Geräusch hat die 1 000-fache Schallintensität I₀ der Hörschwelle. Wie viel Dezibel sind das?',
                                       30, '10 * 3', 'I : I₀ = 1 000, lg(1 000) = 3, also L = 10 · 3 = 30 dB.', 'Setze den Quotienten I : I₀ ein.', einheit='dB'))
    S.bonus('logfunktion', Z('Für wie viele ganze Zahlen x gilt 2 < log₂(x) < 5?', 27, '31 - 5 + 1',
                             '2 < log₂(x) < 5 heißt 2² < x < 2⁵, also 4 < x < 32 (die Funktion steigt). Ganze Zahlen 5 bis 31: 27 Stück.',
                             'Übersetze die Ungleichung in eine Aussage über x ohne Logarithmus.'))
    S.bonus('logfunktion', Z('Für welches x gilt log₂(x) − log₄(x) = 2?', 16, '2 ** 4',
                             'Idee: Ist log₄(x) = y, dann x = 4^y = 2^(2y), also log₂(x) = 2y. Die Gleichung heißt 2y − y = 2, also y = 2 und x = 4² = 16. Probe: log₂ 16 − log₄ 16 = 4 − 2 = 2.',
                             'Schreibe 4 als 2² und vergleiche log₂(x) mit log₄(x).'))

    # --- zeitpunkt ---
    S.stufenleiter('zeitpunkt', 'a · b^t = c durch Teilen und Logarithmieren lösen; die passende Gleichung erkennen.',
                   'Verdopplungs- und Halbwertszeiten, Sachsituationen mit Übertemperatur, ganzzahlige Zeitpunkte, Prozentsatz aus der Verdopplungszeit.',
                   'Zwei Modelle gleichsetzen, aus Daten rückwärts, Faktor als Parameter, Aussagen prüfen, Ähnlichkeit verknüpfen, Tiefe statt Zeit.')
    S.g('zeitpunkt', direkt=[140, 141, 142, 143, 144, 145], einkleidung=[146, 149, 147, 148, 150, 151, 152, 153, 154, 155, 156, 157], mehrschritt=[198, 199],
        pruefung=[200], transfer=[201], rueckwaerts=[202], fehler=[203])
    S.ueberzaehlig(149, 148, 153, 150, 154)
    S.neu('zeitpunkt', 'direkt', ZR('Ein Bestand wird durch B(t) = 800 · 0,9^t beschrieben. Für welches t ist er auf 400 gesunken? Runde auf eine Nachkommastelle.', lg(0.5) / lg(0.9), 1,
                                    '0,9^t = 0,5 ⇒ t = lg 0,5 : lg 0,9 ≈ 6,6.', 'Erst durch 800 teilen, dann logarithmieren.'))
    S.neu('zeitpunkt', 'erkennen', A('Welche Gleichung muss man lösen, um zu bestimmen, wann 500 · 1,04^t den Wert 800 erreicht?', '1,04^t = 1,6',
                                     ['1,04^t = 300', '520^t = 800', '1,04 · t = 1,6'], 'Durch 500 teilen: 1,04^t = 800 : 500 = 1,6.', 'Was muss zuerst allein stehen?'))
    S.neu('zeitpunkt', 'erkennen', A('Welche Rechnung liefert die Lösung von 3^t = 20?', 't = lg 20 : lg 3', ['t = 20 : 3', 't = lg 20 − lg 3', 't = lg(20 : 3)'],
                                     'lg auf beiden Seiten: t · lg 3 = lg 20, also t = lg 20 : lg 3 ≈ 2,73.', 'Logarithmiere beide Seiten.'))
    S.neu('zeitpunkt', 'umkehr', ZR('Ein Bestand verdoppelt sich in 12 Jahren (exponentielles Wachstum). Um wie viel Prozent wächst er pro Jahr? Runde auf zwei Nachkommastellen.',
                                    (2 ** (1 / 12) - 1) * 100, 2, 'b¹² = 2 ⇒ b = 2^(1/12) ≈ 1,0595, also etwa 5,95 % pro Jahr.', 'Welcher Faktor ergibt zwölfmal hintereinander 2?', einheit='%'))
    S.neu('zeitpunkt', 'parameter', ZR('Für welchen Wachstumsfaktor b verdoppelt sich ein Bestand f(t) = a · b^t in genau 10 Jahren? Runde auf vier Nachkommastellen.', 2 ** 0.1, 4,
                                       'b¹⁰ = 2 ⇒ b = 2^(1/10) ≈ 1,0718 – unabhängig vom Anfangswert a.', 'Setze f(10) = 2a.'))
    S.neu('zeitpunkt', 'begruenden', A('Ein Bestand wächst exponentiell und in 5 Jahren um 50 %. Stimmt: „Dann wächst er in 10 Jahren um 100 %“?',
                                       'Nein: In 10 Jahren ist der Faktor 1,5² = 2,25, also wächst er um 125 %.', ['Ja: 2 · 50 % = 100 %.', 'Nein: Er wächst um 150 %.', 'Nein: Er wächst um 75 %.'],
                                       'Zweimal je 5 Jahre: Faktor 1,5 · 1,5 = 2,25. Prozente werden bei exponentiellem Wachstum nicht addiert.', 'Schreibe beide 5-Jahres-Abschnitte als Faktoren.'))
    S.neu('zeitpunkt', 'verknuepfen', Z('Ein Kopierer verkleinert ein Bild bei jedem Kopiervorgang auf 80 % der Länge und Breite. Nach wie vielen Vorgängen ist die Bildfläche zum ersten Mal kleiner als ein Zehntel der ursprünglichen Fläche?',
                                        6, '6', 'Längen mal 0,8 heißt Fläche mal 0,8² = 0,64. 0,64ⁿ < 0,1 ⇒ n > lg 0,1 : lg 0,64 ≈ 5,16. Also nach 6 Vorgängen.',
                                        'Wie ändert sich eine Fläche, wenn alle Längen mit 0,8 malgenommen werden?'))
    S.neu('zeitpunkt', 'transfer', ZR('Licht verliert in einem See je Meter Wassertiefe 8 % seiner Helligkeit. In welcher Tiefe ist nur noch 1 % des Lichts vorhanden? Runde auf ganze Meter.',
                                      lg(0.01) / lg(0.92), 0, '0,92^d = 0,01 ⇒ d = lg 0,01 : lg 0,92 ≈ 55,2, also etwa 55 m.', 'Die Tiefe spielt hier die Rolle der Zeit.', einheit='m'))
    S.bonus('zeitpunkt', Z('Kapital A wächst mit 4 % pro Jahr, das doppelt so große Kapital B mit 2 % pro Jahr. Nach wie vielen ganzen Jahren ist A zum ersten Mal größer als B?', 36, '36',
                           'A · 1,04^t > 2A · 1,02^t ⇒ (1,04 : 1,02)^t > 2. 1,04 : 1,02 ≈ 1,019608, t > lg 2 : lg 1,019608 ≈ 35,7. Also nach 36 Jahren.',
                           'Teile durch A und fasse die beiden Potenzen mit gleichem Exponenten zusammen.', einheit='Jahre'))
    S.bonus('zeitpunkt', Z('Bestand X halbiert sich alle 3 Tage, Bestand Y drittelt sich alle 4 Tage. Beide beginnen mit 1 296 Einheiten. Wie viele Einheiten hat X nach 12 Tagen mehr als Y?', 33,
                           '1296 // 2 ** 4 - 1296 // 3 ** 3', '12 Tage: X wird 4-mal halbiert, 1 296 : 16 = 81; Y wird 3-mal gedrittelt, 1 296 : 27 = 48. Unterschied 81 − 48 = 33.',
                           'Wie oft wird in 12 Tagen halbiert, wie oft gedrittelt?'))
    S.anwenden()


if __name__ == '__main__':
    stufen()  # Zwanzigste Runde (stufen-kl10) – ganz am Ende


# ---- BEREINIGEN (Einundzwanzigste Runde) ----
if __name__ == '__main__':
    from _bereinigen import bereinigen_datei
    bereinigen_datei('funktionen.exponential_log')
# ---- BEREINIGEN ENDE ----


# ---- AUFLOESEN (Vierundzwanzigste Runde, Zweig aufloesen, siehe _aufloesen.py und _af_plan.py) ----
if __name__ == '__main__':
    from _aufloesen import aufloesen_datei
    aufloesen_datei('funktionen.exponential_log')
# ---- AUFLOESEN ENDE ----
