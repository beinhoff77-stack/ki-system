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
