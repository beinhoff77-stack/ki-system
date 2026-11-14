#!/usr/bin/env python3
"""Thema terme.potenzgesetze – Potenzen und Potenzgesetze (Klasse 6)."""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _basis import *  # noqa: E402,F403

R = random.Random(30)
E = eintrag_laden('terme.potenzgesetze')
HB = 'Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt.'

ETAPPEN = [
    {'lernziel': 'potenz_begriff', 'titel': 'Was ist eine Potenz?',
     'regel': 'Eine ⟦Potenz⟧ aⁿ ist ein Produkt aus n gleichen Faktoren a: 2⁴ = 2 · 2 · 2 · 2. a heißt ⟦Basis⟧ (Grundzahl), n heißt ⟦Exponent⟧ (Hochzahl). Eine negative Basis steht in ⟦Klammern⟧: (−2)³.',
     'schritte': ['(−2)³ = (−2) · (−2) · (−2).', '(−2) · (−2) = 4 und 4 · (−2) = ⟦−8⟧.'],
     'fehler': '2⁴ = 8 ist falsch: Das wäre 2 · 4. Richtig ist ⟦2 · 2 · 2 · 2 = 16⟧. Achtung auch: −2² = −(2 · 2) = −4, aber (−2)² = 4.'},
    {'lernziel': 'negativer_exponent', 'titel': 'Negative Exponenten und Hoch 0',
     'regel': 'Ein negativer Exponent bedeutet ⟦Kehrbruch⟧: a⁻ⁿ = 1/aⁿ. Außerdem gilt ⟦a⁰ = 1⟧ (für a ≠ 0) und a¹ = a.',
     'schritte': ['2⁻³ = 1/2³.', '2³ = 8, also 2⁻³ = ⟦1/8⟧ = 0,125.'],
     'probe': '2⁻³ · 2³ = 1/8 · 8 = 1 ✓',
     'fehler': '2⁻³ = −8 ist falsch: Das Minus im Exponenten macht ⟦keine negative Zahl⟧, sondern den ⟦Kehrbruch⟧: 1/8.'},
    {'lernziel': 'mal_gleiche_basis', 'titel': 'Gleiche Basis: malnehmen',
     'regel': 'Potenzen mit ⟦gleicher Basis⟧ multiplizierst du, indem du die ⟦Exponenten addierst⟧: aᵐ · aⁿ = aᵐ⁺ⁿ. Die Basis bleibt gleich.',
     'schritte': ['2³ · 2⁴ = (2 · 2 · 2) · (2 · 2 · 2 · 2): Das sind 3 + 4 = 7 Faktoren 2.', 'Also 2³ · 2⁴ = ⟦2⁷⟧ = 128.'],
     'fehler': '2³ · 2⁴ = 2¹² ist falsch: Die Exponenten werden ⟦addiert⟧, nicht malgenommen. Auch 2³ · 2⁴ = 4⁷ ist falsch: Die ⟦Basis bleibt⟧ 2.'},
    {'lernziel': 'geteilt_gleiche_basis', 'titel': 'Gleiche Basis: teilen',
     'regel': 'Potenzen mit ⟦gleicher Basis⟧ dividierst du, indem du die ⟦Exponenten subtrahierst⟧: aᵐ : aⁿ = aᵐ⁻ⁿ. Ist der zweite Exponent größer, entsteht ein ⟦negativer⟧ Exponent.',
     'schritte': ['5⁶ : 5⁴ = (5 · 5 · 5 · 5 · 5 · 5) : (5 · 5 · 5 · 5). Vier Faktoren 5 kürzen sich weg.', 'Übrig bleiben 6 − 4 = 2 Faktoren: 5⁶ : 5⁴ = ⟦5²⟧ = 25.'],
     'fehler': '5⁶ : 5³ = 5² ist falsch: Die Exponenten werden ⟦subtrahiert⟧, nicht geteilt. Richtig: 5⁶⁻³ = 5³ = 125.'},
    {'lernziel': 'gleicher_exponent', 'titel': 'Gleicher Exponent: Basen zusammen',
     'regel': 'Potenzen mit ⟦gleichem Exponenten⟧ multiplizierst du, indem du die ⟦Basen multiplizierst⟧: aⁿ · bⁿ = (a · b)ⁿ. Beim Teilen: aⁿ : bⁿ = (a : b)ⁿ.',
     'schritte': ['2³ · 5³ = (2 · 5)³, denn 2 · 2 · 2 · 5 · 5 · 5 = (2 · 5) · (2 · 5) · (2 · 5).', '= 10³ = ⟦1 000⟧.'],
     'fehler': '2³ · 5³ = 10⁶ ist falsch: Bei ⟦verschiedenen Basen⟧ werden die Exponenten nicht addiert. Gleicher Exponent heißt: Basen malnehmen, Exponent bleibt – (2 · 5)³ = 10³.'},
    {'lernziel': 'anwenden', 'titel': 'Potenzgesetze geschickt nutzen',
     'regel': 'Prüfe zuerst, ob die ⟦Basen⟧ oder die ⟦Exponenten⟧ gleich sind – davon hängt ab, welches Gesetz passt. Manchmal hilft es, eine Zahl als Potenz zu schreiben: 4 = 2², 8 = 2³, 9 = 3².',
     'schritte': ['8 · 2⁴: Schreibe 8 = 2³. Dann gleiche Basis: 2³ · 2⁴.', 'Exponenten addieren: 2⁷ = ⟦128⟧.'],
     'fehler': '3² · 2³ = 6⁵ ist falsch: Weder die Basen noch die Exponenten sind gleich. Hier hilft ⟦kein⟧ Potenzgesetz – einfach ausrechnen: 9 · 8 = 72.'},
    {'lernziel': 'fehler_finden', 'titel': 'Fehler bei Potenzen finden',
     'regel': 'Bei Potenzen passieren typische Fehler: ⟦Basis mal Exponent⟧ statt Potenz, Exponenten ⟦malnehmen statt addieren⟧, ein negativer Exponent als ⟦negative Zahl⟧, Klammern bei negativer Basis vergessen. Prüfe mit einem ⟦Zahlenbeispiel⟧.',
     'schritte': ['Behauptet: 3² · 3³ = 3⁶. Prüfe: 9 · 27 = 243.', '3⁶ = 729, aber 3⁵ = 243. Also ist ⟦3⁵⟧ richtig – die Exponenten werden addiert.'],
     'fehler': 'Eine Regel nur auswendig anwenden, ohne sie an kleinen Zahlen zu prüfen, führt zu Verwechslungen. ⟦Ausschreiben⟧ hilft: 3² · 3³ = (3 · 3) · (3 · 3 · 3).'},
]

MERKE = ['aⁿ = a · a · … · a (n Faktoren). a⁰ = 1, a⁻ⁿ = 1/aⁿ.', 'Gleiche Basis: aᵐ · aⁿ = aᵐ⁺ⁿ und aᵐ : aⁿ = aᵐ⁻ⁿ.',
         'Gleicher Exponent: aⁿ · bⁿ = (a · b)ⁿ und aⁿ : bⁿ = (a : b)ⁿ.', 'Negative Basis in Klammern: (−2)² = 4, aber −2² = −4.']


def pt(b, n):
    """Potenz als Text."""
    b = Fr(b)
    if b.denominator != 1: s = f'({bruch(b)})'
    elif b < 0: s = f'({zt(b)})'
    else: s = zt(b)
    return s + hoch(n)


def pd(b, n):
    """Potenz mit Dezimal-Basis als Text."""
    return (f'({zt(b)})' if Fr(b) < 0 else zt(b)) + hoch(n)


def py(x):
    x = Fr(x)
    return f'({x.numerator}/{x.denominator})' if x.denominator != 1 else f'({x.numerator})'


def lb(x, text, w, h, c):
    x = Fr(x)
    assert x > 0 and x.denominator > 1
    return {'y': 'luecken', 'f': {'text': text, 'schablone': '□/□', 'hinweis': HB}, 'o': {'werte': [x.numerator, x.denominator]},
            'c': [f'({c}) * {x.denominator}', f'{x.denominator}'], 'w': w, 'h': h}


def ausgeschrieben(b, n):
    return ' · '.join([pt(b, 1)[:-1]] * n)


VARS = ['a', 'x', 'b', 'y', 'z']


# ---------- 1 Potenzbegriff ----------
def g_begriff(st):
    if st == 1:
        if R.random() < .25:
            b, n = R.randint(2, 9), R.randint(2, 6)
            frage = R.choice(['Basis', 'Exponent'])
            r = str(b if frage == 'Basis' else n)
            return {**wahl(R, r, [str(n if frage == 'Basis' else b), str(b * n), str(b ** n)]), 'f': {'text': f'Was ist bei {pt(b, n)} der {frage}?'},
                    'w': f'Bei {pt(b, n)} ist {b} die Basis (Grundzahl) und {n} der Exponent (Hochzahl).', 'h': 'Die Basis ist die große Zahl unten, der Exponent die kleine oben.'}
        b, n = R.randint(2, 10), R.randint(2, 4)
        return {'y': 'zahl', 'f': {'text': f'Berechne {pt(b, n)}.'}, 'o': {'wert': b ** n}, 'c': f'{b}**{n}',
                'w': f'{pt(b, n)} = {" · ".join([str(b)] * n)} = {zt(b ** n)}.', 'h': f'Schreibe {n} Faktoren {b} hin und nimm sie mal.'}
    if st == 2:
        art = R.randrange(3)
        if art == 0:
            b, n = -R.randint(2, 5), R.randint(2, 5)
            return {'y': 'zahl', 'f': {'text': f'Berechne {pt(b, n)}.'}, 'o': {'wert': b ** n}, 'c': f'({b})**{n}',
                    'w': f'{pt(b, n)} = {ausgeschrieben(b, n)} = {zt(b ** n)}. {n} Minuszeichen: {"gerade Anzahl, also positiv" if n % 2 == 0 else "ungerade Anzahl, also negativ"}.',
                    'h': 'Gerade Anzahl negativer Faktoren: positiv. Ungerade: negativ.'}
        if art == 1:
            b = R.choice([Fr(1, 2), Fr(1, 10), Fr(2, 10), Fr(3, 10), Fr(5, 10), Fr(15, 10), Fr(12, 10)])
            n = R.randint(2, 3)
            return {'y': 'zahl', 'f': {'text': f'Berechne {pd(b, n)}.'}, 'o': {'wert': wert(b ** n)}, 'c': f'{float(b)}**{n}',
                    'w': f'{pd(b, n)} = {" · ".join([zt(b)] * n)} = {zt(b ** n)}.', 'h': 'Rechne ohne Komma und zähle dann die Nachkommastellen zusammen.'}
        b = Fr(R.randint(1, 4), R.randint(2, 5))
        while b.denominator == 1: b = Fr(R.randint(1, 4), R.randint(2, 5))
        n = R.randint(2, 3)
        return lb(b ** n, f'Berechne {pt(b, n)}.', f'Zähler und Nenner hoch {n}: {b.numerator}{hoch(n)}/{b.denominator}{hoch(n)} = {bruch(b ** n)}.',
                  'Nimm Zähler und Nenner jeweils hoch den Exponenten.', f'{py(b)}**{n}')
    art = R.randrange(4)
    if art == 0:
        b, n = R.randint(2, 5), R.choice([2, 4])
        r = -(b ** n)
        return {**wahl(R, zt(r), [zt(b ** n), zt(-b * n), zt(b * n)]), 'f': {'text': f'Was ergibt −{b}{hoch(n)}? (Ohne Klammer!)'},
                'w': f'Ohne Klammer gehört das Minus nicht zur Basis: −{b}{hoch(n)} = −({b}{hoch(n)}) = {zt(r)}. Dagegen wäre ({zt(-b)}){hoch(n)} = {b ** n}.', 'h': 'Der Exponent gehört nur zur Zahl direkt darunter.'}
    if art == 1:
        a, m = R.randint(2, 5), R.randint(2, 5)
        b, n = R.randint(2, 5), R.randint(2, 5)
        if a ** m == b ** n or (a, m) == (b, n): return g_begriff(3)
        r = pt(a, m) if a ** m > b ** n else pt(b, n)
        return {**wahl(R, r, [pt(b, n) if r == pt(a, m) else pt(a, m), 'Beide sind gleich groß'], 3), 'f': {'text': f'Welche Zahl ist größer: {pt(a, m)} oder {pt(b, n)}?'},
                'w': f'{pt(a, m)} = {a ** m}, {pt(b, n)} = {b ** n}. Größer: {r}.', 'h': 'Rechne beide Potenzen aus.'}
    if art == 2:
        k = R.randint(2, 9)
        return {'y': 'zahl', 'f': {'text': f'Ein Würfel hat die Kantenlänge {k} cm. Sein Volumen ist {k}³ cm³. Berechne das Volumen.'}, 'o': {'wert': k ** 3, 'einheit': 'cm³'}, 'c': f'{k}**3',
                'w': f'{k}³ = {k} · {k} · {k} = {k ** 3} cm³.', 'h': 'Hoch 3 heißt: dreimal dieselbe Zahl malnehmen.'}
    n = R.randint(4, 10)
    return {'y': 'zahl', 'f': {'text': f'Eine Bakterienkultur verdoppelt sich jede Stunde. Am Anfang ist es 1 Bakterium. Wie viele sind es nach {n} Stunden? (2{hoch(n)})'},
            'o': {'wert': 2 ** n}, 'c': f'2**{n}', 'w': f'Jede Stunde · 2, also nach {n} Stunden 2{hoch(n)} = {zt(2 ** n)}.', 'h': 'Verdoppeln heißt mal 2 – so oft, wie Stunden vergangen sind.'}


# ---------- 2 Negativer Exponent ----------
def g_neg(st):
    if st == 1:
        if R.random() < .25:
            b = R.choice([2, 3, 5, 7, 10, 12, 100, 'a', 'x'])
            return {**wahl(R, '1', ['0', str(b), f'{"−" if isinstance(b, int) else ""}1' if isinstance(b, int) else '−1']), 'f': {'text': f'Was ergibt {b}⁰?'},
                    'w': f'Jede Zahl (außer 0) hoch 0 ergibt 1: {b}⁰ = 1.', 'h': 'Teile z. B. 2³ : 2³ – das ist 1 und auch 2³⁻³ = 2⁰.'}
        b, n = R.randint(2, 10), R.randint(1, 3)
        if b ** n > 1000: n = 1
        return lb(Fr(1, b ** n), f'Schreibe {pt(b, -n)} als Bruch.', f'{pt(b, -n)} = 1/{pt(b, n)} = 1/{b ** n}.', 'Negativer Exponent: Kehrbruch der Potenz mit positivem Exponenten.', f'{b}**-{n}')
    if st == 2:
        art = R.randrange(3)
        if art == 0:
            b = Fr(R.randint(1, 3), R.randint(2, 5))
            while b.denominator == 1: b = Fr(R.randint(1, 3), R.randint(2, 5))
            n = R.randint(1, 3)
            r = b ** -n
            if r.denominator == 1:
                return {'y': 'zahl', 'f': {'text': f'Berechne {pt(b, -n)}.'}, 'o': {'wert': int(r)}, 'c': f'{py(b)}**-{n}',
                        'w': f'Kehrbruch: {pt(b, -n)} = {pt(1 / b, n)} = {zt(r)}.', 'h': 'Bei einem Bruch heißt negativer Exponent: Bruch umdrehen.'}
            return lb(r, f'Berechne {pt(b, -n)}.', f'Kehrbruch: {pt(b, -n)} = {pt(1 / b, n)} = {bruch(r)}.', 'Bei einem Bruch heißt negativer Exponent: Bruch umdrehen.', f'{py(b)}**-{n}')
        if art == 1:
            b, n = R.choice([(2, 1), (4, 1), (5, 1), (2, 2), (5, 2), (2, 3), (10, 2), (10, 3), (4, 2), (20, 1), (25, 1), (8, 1), (2, 4), (5, 3)])
            return {'y': 'zahl', 'f': {'text': f'Schreibe {pt(b, -n)} als Dezimalzahl.'}, 'o': {'wert': wert(Fr(1, b ** n))}, 'c': f'{b}**-{n}',
                    'w': f'{pt(b, -n)} = 1/{b ** n} = {zt(Fr(1, b ** n))}.', 'h': 'Erst als Bruch schreiben, dann in eine Dezimalzahl umwandeln.'}
        b, n = R.choice([2, 3, 5, 10]), R.randint(2, 5)
        return {'y': 'zahl', 'f': {'text': f'Schreibe 1/{zt(b ** n)} als Potenz mit der Basis {b}. Wie heißt der Exponent?'}, 'o': {'wert': -n}, 'c': f'-{n}',
                'w': f'{zt(b ** n)} = {pt(b, n)}, also 1/{zt(b ** n)} = {pt(b, -n)}. Exponent: {zt(-n)}.', 'h': f'Schreibe zuerst den Nenner als Potenz von {b}.'}
    art = R.randrange(3)
    if art == 0:
        b, n = -R.randint(2, 4), R.choice([1, 3])
        r = Fr(b) ** -n
        return {**wahl(R, bruch(r), [bruch(-r), zt(b ** n), zt(-(b ** n))]), 'f': {'text': f'Berechne {pt(b, -n)}.'},
                'w': f'{pt(b, -n)} = 1/{pt(b, n)} = 1/({zt(b ** n)}) = {bruch(r)}.', 'h': 'Kehrbruch bilden – das Vorzeichen der Basis bleibt erhalten.'}
    if art == 1:
        b = R.choice([2, 3, 4, 5])
        m, n = R.sample([1, 2, 3], 2)
        r = Fr(b) ** -m + Fr(b) ** -n
        return lb(r, f'Berechne {pt(b, -m)} + {pt(b, -n)}.', f'{pt(b, -m)} = 1/{b ** m}, {pt(b, -n)} = 1/{b ** n}. Summe: {bruch(r)}.', 'Schreibe beide als Bruch und addiere mit Hauptnenner.',
                  f'{b}**-{m} + {b}**-{n}')
    b, n = R.randint(2, 6), R.randint(1, 3)
    return {'y': 'zahl', 'f': {'text': f'Berechne {pt(b, -n)} · {pt(b, n)}.'}, 'o': {'wert': 1}, 'c': f'{b}**-{n} * {b}**{n}',
            'w': f'1/{b ** n} · {b ** n} = 1 (oder: {pt(b, -n + n)} = 1).', 'h': 'Schreibe die erste Potenz als Bruch.'} if R.random() < .5 else \
        {'y': 'zahl', 'f': {'text': f'Wie viel Mal so groß ist {pt(b, n)} wie {pt(b, -n)}?'}, 'o': {'wert': b ** (2 * n)}, 'c': f'{b}**{n} / {b}**-{n}',
         'w': f'{pt(b, n)} : {pt(b, -n)} = {pt(b, 2 * n)} = {zt(b ** (2 * n))}.', 'h': 'Teile die beiden Potenzen. Exponenten subtrahieren: n − (−n).'}


# ---------- 3 Mal, gleiche Basis ----------
def g_mal(st):
    if st == 1:
        b = R.choice([2, 3, 5, 10, 7])
        m, n = R.randint(1, 6), R.randint(2, 6)
        return {'y': 'zahl', 'f': {'text': f'{pt(b, m)} · {pt(b, n)} = {b}ᵏ. Wie groß ist k?'}, 'o': {'wert': m + n}, 'c': f'{m} + {n}',
                'w': f'Gleiche Basis: Exponenten addieren, {m} + {n} = {m + n}. Also {pt(b, m + n)}.', 'h': 'Gleiche Basis beim Malnehmen: Exponenten addieren.'}
    if st == 2:
        art = R.randrange(3)
        if art == 0:
            v = R.choice(VARS)
            m, n = R.randint(-5, 6), R.randint(-5, 6)
            if 0 in (m, n): return g_mal(2)
            return {'y': 'zahl', 'f': {'text': f'{v}{hoch(m)} · {v}{hoch(n)} = {v}ᵏ. Wie groß ist k?'}, 'o': {'wert': m + n}, 'c': f'({m}) + ({n})',
                    'w': f'Exponenten addieren: {kl(m)} + {kl(n)} = {zt(m + n)}.', 'h': 'Auch negative Exponenten werden addiert. Achte auf die Vorzeichen.'}
        if art == 1:
            b = R.choice([2, 3, 10])
            e = [R.randint(-3, 5) for _ in range(3)]
            if 0 in e: return g_mal(2)
            return {'y': 'zahl', 'f': {'text': f'{pt(b, e[0])} · {pt(b, e[1])} · {pt(b, e[2])} = {b}ᵏ. Wie groß ist k?'}, 'o': {'wert': sum(e)}, 'c': ' + '.join(f'({x})' for x in e),
                    'w': f'Alle Exponenten addieren: {" + ".join(kl(x) for x in e)} = {zt(sum(e))}.', 'h': 'Bei drei Faktoren addierst du alle drei Exponenten.'}
        b = R.choice([2, 3, 5])
        m, n = R.randint(2, 4), R.randint(1, 3)
        r = pt(b, m + n)
        return {**wahl(R, r, [pt(b, m * n), pt(b * b, m + n), pt(b, m * n + 1) if m * n + 1 != m + n else pt(b, m + n + 1)]), 'f': {'text': f'Fasse zusammen: {pt(b, m)} · {pt(b, n)}'},
                'w': f'Gleiche Basis, Exponenten addieren: {pt(b, m)} · {pt(b, n)} = {r}.', 'h': 'Die Basis bleibt, die Exponenten werden addiert.'}
    art = R.randrange(3)
    if art == 0:
        m, n = R.randint(2, 6), -R.randint(3, 8)
        r = Fr(10) ** (m + n)
        return {'y': 'zahl', 'f': {'text': f'Berechne {pt(10, m)} · {pt(10, n)} und gib das Ergebnis als Dezimalzahl an.'}, 'o': {'wert': wert(r)}, 'c': f'10**{m} * 10**({n})',
                'w': f'{pt(10, m)} · {pt(10, n)} = {pt(10, m + n)} = {zt(r)}.', 'h': 'Erst die Exponenten addieren, dann ausrechnen.'}
    if art == 1:
        b = R.choice([2, 3, 5, 7])
        m, s = R.randint(2, 6), R.randint(8, 14)
        return {'y': 'zahl', 'f': {'text': f'Ergänze den Exponenten: {pt(b, m)} · {b}ᵏ = {pt(b, s)}. Wie groß ist k?'}, 'o': {'wert': s - m}, 'c': f'{s} - {m}',
                'w': f'{m} + k = {s}, also k = {s} − {m} = {s - m}.', 'h': 'Welche Zahl musst du zu m addieren, damit s herauskommt?'}
    b = R.choice([2, 3])
    m, n = R.randint(1, 3), R.randint(1, 3)
    return {'y': 'zahl', 'f': {'text': f'Berechne {pt(b, m)} · {pt(b, n)} mit dem Potenzgesetz und gib den Wert an.'}, 'o': {'wert': b ** (m + n)}, 'c': f'{b}**{m} * {b}**{n}',
            'w': f'{pt(b, m)} · {pt(b, n)} = {pt(b, m + n)} = {b ** (m + n)}.', 'h': 'Exponenten addieren, dann die Potenz ausrechnen.'}


# ---------- 4 Geteilt, gleiche Basis ----------
def g_geteilt(st):
    if st == 1:
        b = R.choice([2, 3, 5, 10, 7])
        n, m = R.randint(1, 5), R.randint(1, 5)
        m = n + m
        return {'y': 'zahl', 'f': {'text': f'{pt(b, m)} : {pt(b, n)} = {b}ᵏ. Wie groß ist k?'}, 'o': {'wert': m - n}, 'c': f'{m} - {n}',
                'w': f'Gleiche Basis: Exponenten subtrahieren, {m} − {n} = {m - n}. Also {pt(b, m - n)}.', 'h': 'Gleiche Basis beim Teilen: Exponenten subtrahieren.'}
    if st == 2:
        art = R.randrange(3)
        if art == 0:
            b = R.choice([2, 3, 5, 10])
            m, n = R.randint(1, 4), R.randint(5, 9)
            return {'y': 'zahl', 'f': {'text': f'{pt(b, m)} : {pt(b, n)} = {b}ᵏ. Wie groß ist k?'}, 'o': {'wert': m - n}, 'c': f'{m} - {n}',
                    'w': f'{m} − {n} = {zt(m - n)}. Also {pt(b, m - n)} = 1/{pt(b, n - m)}.', 'h': 'Der zweite Exponent ist größer – das Ergebnis hat einen negativen Exponenten.'}
        if art == 1:
            v = R.choice(VARS)
            m, n = R.randint(-4, 7), R.randint(-4, 7)
            if 0 in (m, n) or m == n: return g_geteilt(2)
            return {'y': 'zahl', 'f': {'text': f'{v}{hoch(m)} : {v}{hoch(n)} = {v}ᵏ. Wie groß ist k?'}, 'o': {'wert': m - n}, 'c': f'({m}) - ({n})',
                    'w': f'Exponenten subtrahieren: {kl(m)} − {kl(n)} = {zt(m - n)}.', 'h': 'Minus eine negative Zahl wird plus.'}
        b = R.choice([2, 3, 5])
        n = R.randint(2, 3)
        m = n * R.randint(2, 3)
        r = pt(b, m - n)
        return {**wahl(R, r, [pt(b, m // n), pt(b, m * n), pt(b, m + n)]), 'f': {'text': f'Fasse zusammen: {pt(b, m)} : {pt(b, n)}'},
                'w': f'Exponenten subtrahieren: {m} − {n} = {m - n}, also {r}.', 'h': 'Teilen bei gleicher Basis: Exponenten subtrahieren, nicht teilen.'}
    art = R.randrange(3)
    if art == 0:
        b = R.choice([2, 3, 5, 10])
        n, d = R.randint(2, 6), R.randint(1, 3)
        m = n + d
        return {'y': 'zahl', 'f': {'text': f'Berechne {pt(b, m)} : {pt(b, n)}.'}, 'o': {'wert': b ** d}, 'c': f'{b}**{m} / {b}**{n}',
                'w': f'{pt(b, m)} : {pt(b, n)} = {pt(b, d)} = {b ** d}.', 'h': 'Nicht beide Potenzen ausrechnen – erst das Gesetz anwenden.'}
    if art == 1:
        b = R.choice([2, 10])
        m, n = R.randint(1, 3), R.randint(4, 6)
        r = Fr(b) ** (m - n)
        return {'y': 'zahl', 'f': {'text': f'Berechne {pt(b, m)} : {pt(b, n)} und gib das Ergebnis als Dezimalzahl an.'}, 'o': {'wert': wert(r)}, 'c': f'{b}**{m} / {b}**{n}',
                'w': f'{pt(b, m)} : {pt(b, n)} = {pt(b, m - n)} = 1/{b ** (n - m)} = {zt(r)}.', 'h': 'Exponenten subtrahieren, dann den Kehrbruch als Dezimalzahl schreiben.'}
    b = R.choice([2, 3, 5])
    m, n, k = R.randint(3, 6), R.randint(2, 5), R.randint(1, 4)
    e = m + n - k
    return {'y': 'zahl', 'f': {'text': f'{pt(b, m)} · {pt(b, n)} : {pt(b, k)} = {b}ᵉ. Wie groß ist e?'}, 'o': {'wert': e}, 'c': f'{m} + {n} - {k}',
            'w': f'Von links: {pt(b, m)} · {pt(b, n)} = {pt(b, m + n)}; : {pt(b, k)} ergibt {pt(b, e)}.', 'h': 'Malnehmen: addieren. Teilen: subtrahieren.'}


# ---------- 5 Gleicher Exponent ----------
PAARE = [(2, 5), (4, 25), (5, 20), (2, 50), (4, 5), (25, 4), (8, 125), (2, 3), (3, 3)]


def g_gleichexp(st):
    if st == 1:
        a, b = R.choice([(2, 5), (4, 25), (5, 20), (20, 5), (5, 2), (2, 50), (25, 4), (50, 2)])
        n = R.randint(2, 4) if a * b == 10 else R.randint(2, 3)
        return {'y': 'zahl', 'f': {'text': f'Berechne geschickt: {pt(a, n)} · {pt(b, n)}'}, 'o': {'wert': (a * b) ** n}, 'c': f'{a}**{n} * {b}**{n}',
                'w': f'Gleicher Exponent: ({a} · {b}){hoch(n)} = {pt(a * b, n)} = {zt((a * b) ** n)}.', 'h': 'Gleicher Exponent: Erst die Basen malnehmen.'}
    if st == 2:
        art = R.randrange(3)
        if art == 0:
            q, b = R.randint(2, 5), R.randint(2, 6)
            a, n = q * b, R.randint(2, 3)
            return {'y': 'zahl', 'f': {'text': f'Berechne geschickt: {pt(a, n)} : {pt(b, n)}'}, 'o': {'wert': q ** n}, 'c': f'{a}**{n} / {b}**{n}',
                    'w': f'({a} : {b}){hoch(n)} = {pt(q, n)} = {q ** n}.', 'h': 'Gleicher Exponent: Erst die Basen teilen.'}
        if art == 1:
            a, b = R.choice([(Fr(1, 2), 2), (Fr(1, 4), 4), (Fr(1, 5), 5), (Fr(2, 10), 5), (Fr(5, 10), 2), (Fr(25, 100), 4)])
            n = R.randint(2, 6)
            return {'y': 'zahl', 'f': {'text': f'Berechne geschickt: {pd(a, n)} · {pt(b, n)}'}, 'o': {'wert': 1}, 'c': f'{float(a)}**{n} * {b}**{n}',
                    'w': f'({zt(a)} · {b}){hoch(n)} = 1{hoch(n)} = 1.', 'h': 'Was ergibt das Produkt der beiden Basen?'}
        a, b = R.choice([(2, 5), (4, 25), (2, 50), (5, 20)])
        n = R.randint(2, 4)
        r = pt(a * b, n)
        return {**wahl(R, r, [pt(a * b, 2 * n), pt(a + b, n), pt(a * b, n * n) if n > 2 else pt(a + b, 2 * n)]), 'f': {'text': f'Fasse zusammen: {pt(a, n)} · {pt(b, n)}'},
                'w': f'Gleicher Exponent: Basen malnehmen, Exponent bleibt: {r}.', 'h': 'Die Exponenten werden hier nicht addiert – nur die Basen malgenommen.'}
    art = R.randrange(3)
    if art == 0:
        p, q = R.randint(1, 4), R.randint(2, 5)
        a = Fr(p, q)
        if a.denominator == 1: return g_gleichexp(3)
        n = R.randint(2, 3)
        return {'y': 'zahl', 'f': {'text': f'Berechne geschickt: {pt(a, n)} · {pt(a.denominator, n)}'}, 'o': {'wert': a.numerator ** n}, 'c': f'{py(a)}**{n} * {a.denominator}**{n}',
                'w': f'({bruch(a)} · {a.denominator}){hoch(n)} = {pt(a.numerator, n)} = {a.numerator ** n}.', 'h': 'Bruch mal Nenner – was bleibt übrig?'}
    if art == 1:
        n = R.randint(1, 4)
        a, b = R.choice([(2, 5), (4, 25), (5, 20)])
        r = Fr(a * b) ** -n
        return {'y': 'zahl', 'f': {'text': f'Berechne geschickt: {pt(a, -n)} · {pt(b, -n)} und gib das Ergebnis als Dezimalzahl an.'}, 'o': {'wert': wert(r)}, 'c': f'{a}**-{n} * {b}**-{n}',
                'w': f'({a} · {b}){hoch(-n)} = {pt(a * b, -n)} = {zt(r)}.', 'h': 'Das Gesetz gilt auch mit negativem Exponenten.'}
    n = R.randint(2, 3)
    a, b, c = R.choice([(2, 3, 5), (2, 5, 3), (4, 5, 5), (2, 2, 5), (5, 4, 5)])
    return {'y': 'zahl', 'f': {'text': f'Berechne geschickt: {pt(a, n)} · {pt(b, n)} · {pt(c, n)}'}, 'o': {'wert': (a * b * c) ** n}, 'c': f'{a}**{n} * {b}**{n} * {c}**{n}',
            'w': f'({a} · {b} · {c}){hoch(n)} = {pt(a * b * c, n)} = {zt((a * b * c) ** n)}.', 'h': 'Alle drei Basen malnehmen, der Exponent bleibt.'}


# ---------- 6 Anwenden ----------
UMSCHREIBEN = [(4, 2, 2), (8, 2, 3), (16, 2, 4), (32, 2, 5), (9, 3, 2), (27, 3, 3), (25, 5, 2), (125, 5, 3), (100, 10, 2), (1000, 10, 3)]


def g_anw(st):
    if st == 1:
        z, b, k = R.choice(UMSCHREIBEN)
        n = R.randint(1, 5)
        return {'y': 'zahl', 'f': {'text': f'{zt(z)} · {pt(b, n)} = {b}ᵉ. Wie groß ist e?'}, 'o': {'wert': k + n}, 'c': f'{k} + {n}',
                'w': f'{zt(z)} = {pt(b, k)}. {pt(b, k)} · {pt(b, n)} = {pt(b, k + n)}, also e = {k + n}.', 'h': f'Schreibe {zt(z)} als Potenz von {b}.'}
    if st == 2:
        art = R.randrange(3)
        if art == 0:
            b = R.choice([2, 3, 10])
            m, n, k = R.randint(2, 5), R.randint(2, 5), R.randint(2, 6)
            e = m + n - k
            r = Fr(b) ** e
            if abs(e) > 4 or (b == 3 and e < 0): return g_anw(2)
            if r.denominator != 1 and not all(p in (2, 5) for p in (b,)): return g_anw(2)
            return {'y': 'zahl', 'f': {'text': f'Berechne: {pt(b, m)} · {pt(b, n)} : {pt(b, k)}' + (' (als Dezimalzahl)' if r.denominator != 1 else '')}, 'o': {'wert': wert(r)},
                    'c': f'{b}**{m} * {b}**{n} / {b}**{k}', 'w': f'Exponenten: {m} + {n} − {k} = {zt(e)}. {pt(b, e)} = {zt(r)}.', 'h': 'Erst die Exponenten zusammenfassen, dann ausrechnen.'}
        if art == 1:
            z, b, k = R.choice(UMSCHREIBEN)
            n = R.randint(k + 1, k + 6)
            return {'y': 'zahl', 'f': {'text': f'{pt(b, n)} : {zt(z)} = {b}ᵉ. Wie groß ist e?'}, 'o': {'wert': n - k}, 'c': f'{n} - {k}',
                    'w': f'{zt(z)} = {pt(b, k)}. {pt(b, n)} : {pt(b, k)} = {pt(b, n - k)}.', 'h': f'Schreibe {zt(z)} als Potenz von {b}.'}
        a, b = R.choice([(2, 5), (4, 25), (20, 5)])
        n, m = R.randint(2, 4), R.randint(1, 3)
        r = (a * b) ** n * b ** m
        return {'y': 'zahl', 'f': {'text': f'Berechne geschickt: {pt(a, n)} · {pt(b, n + m)}'}, 'o': {'wert': r}, 'c': f'{a}**{n} * {b}**{n + m}',
                'w': f'{pt(b, n + m)} = {pt(b, n)} · {pt(b, m)}. Dann ({a} · {b}){hoch(n)} · {pt(b, m)} = {zt((a * b) ** n)} · {b ** m} = {zt(r)}.',
                'h': 'Zerlege die zweite Potenz so, dass beide den gleichen Exponenten haben.'}
    art = R.randrange(3)
    if art == 0:
        (z1, b, k1), (z2, _, k2) = R.sample([u for u in UMSCHREIBEN if u[1] == 2], 2)
        return {'y': 'zahl', 'f': {'text': f'{z1} · {z2} = 2ᵉ. Wie groß ist e?'}, 'o': {'wert': k1 + k2}, 'c': f'{k1} + {k2}',
                'w': f'{z1} = {pt(2, k1)}, {z2} = {pt(2, k2)}. Produkt: {pt(2, k1 + k2)}.', 'h': 'Schreibe beide Zahlen als Potenz von 2.'}
    if art == 1:
        a, m, b, n = R.randint(2, 5), R.randint(2, 3), R.randint(2, 5), R.randint(2, 3)
        if a == b or m == n: return g_anw(3)
        r = a ** m * b ** n
        return {**wahl(R, zt(r), [pt(a * b, m + n), pt(a + b, m * n), zt(a * m * b * n)]), 'f': {'text': f'Was ergibt {pt(a, m)} · {pt(b, n)}?'},
                'w': f'Weder Basis noch Exponent gleich – kein Gesetz anwendbar. Ausrechnen: {a ** m} · {b ** n} = {zt(r)}.', 'h': 'Passt ein Potenzgesetz? Wenn nicht: einzeln ausrechnen.'}
    n = R.randint(3, 8)
    return {'y': 'zahl', 'f': {'text': f'Ein Blatt Papier wird {n}-mal in der Mitte gefaltet. Jedes Falten verdoppelt die Anzahl der Lagen. Wie viele Lagen liegen danach übereinander?'},
            'o': {'wert': 2 ** n}, 'c': f'2**{n}', 'w': f'Nach {n}-mal Falten: 2{hoch(n)} = {2 ** n} Lagen.', 'h': 'Jedes Falten heißt mal 2.'}


# ---------- 7 Fehler finden ----------
def g_fehler(st):
    b = R.randint(2, 5)
    m, n = R.randint(2, 4), R.randint(2, 4)
    if st == 1:
        aussagen = [(f'{pt(b, m)} = {b * m}', False, f'Nein, {pt(b, m)} = {" · ".join([str(b)] * m)} = {b ** m}.'),
                    (f'{pt(b, m)} · {pt(b, n)} = {pt(b, m + n)}', True, 'Ja, gleiche Basis: Exponenten addieren.'),
                    (f'{pt(b, -m)} ist eine negative Zahl.', False, f'Nein, {pt(b, -m)} = 1/{b ** m} ist positiv.'),
                    (f'{b}⁰ = 0', False, f'Nein, jede Zahl außer 0 hoch 0 ergibt 1: {b}⁰ = 1.')]
    elif st == 2:
        aussagen = [(f'{pt(b, m)} · {pt(b, n)} = {pt(b, m * n)}', m * n == m + n, f'{"Ja" if m * n == m + n else "Nein"}, die Exponenten werden addiert: {pt(b, m + n)}.'),
                    (f'{pt(b, m + n)} : {pt(b, n)} = {pt(b, m)}', True, 'Ja, Exponenten subtrahieren.'),
                    (f'{pt(-b, 2)} = {zt(-b * b)}', False, f'Nein, ({zt(-b)}) · ({zt(-b)}) = {b * b}.'),
                    (f'{pt(2, m)} · {pt(5, m)} = {pt(10, 2 * m)}', False, f'Nein, gleicher Exponent: Basen malnehmen, Exponent bleibt: {pt(10, m)}.')]
    else:
        aussagen = [(f'{pt(b, m)} · {pt(b, n)} = {pt(b * b, m + n)}', False, f'Nein, die Basis bleibt: {pt(b, m + n)}.'),
                    (f'{pt(b, 2 * m)} : {pt(b, m)} = {pt(b, 2)}', m == 2, f'{"Ja" if m == 2 else "Nein"}, Exponenten subtrahieren: {pt(b, 2 * m - m)}.'),
                    (f'−{b}² = {b * b}', False, f'Nein, ohne Klammer: −{b}² = −{b * b}.'),
                    (f'{pt(b, -1)} · {b} = 1', True, f'Ja, 1/{b} · {b} = 1.'),
                    (f'{pt(b, m)} + {pt(b, n)} = {pt(b, m + n)}', False, f'Nein, für Plus gibt es kein Potenzgesetz: {b ** m} + {b ** n} = {b ** m + b ** n}, aber {pt(b, m + n)} = {b ** (m + n)}.')]
    s, stimmt, grund = R.choice(aussagen)
    if stimmt and not grund.startswith('Ja'): grund = 'Ja. ' + grund
    if not stimmt and not grund.startswith('Nein'): grund = 'Nein. ' + grund
    gegen = 'Ja, das stimmt.' if not stimmt else 'Nein, das ist falsch.'
    return {**wahl(R, grund, [gegen, 'Das kann man nicht entscheiden.'], 3), 'f': {'text': f'Stimmt die Rechnung? {s}'},
            'w': grund, 'h': 'Prüfe mit Ausschreiben oder Ausrechnen.'}


GEN = {'potenz_begriff': g_begriff, 'negativer_exponent': g_neg, 'mal_gleiche_basis': g_mal, 'geteilt_gleiche_basis': g_geteilt,
       'gleicher_exponent': g_gleichexp, 'anwenden': g_anw, 'fehler_finden': g_fehler}

DATEI = datei(E, 'Potenzen mit natürlichen und ganzzahligen Exponenten verstehen und Potenzen mit gleicher Basis oder gleichem Exponenten zusammenfassen.', MERKE,
              [('Potenzen verstehen', ['potenz_begriff', 'negativer_exponent']),
               ('Potenzgesetze', ['mal_gleiche_basis', 'geteilt_gleiche_basis', 'gleicher_exponent']),
               ('Anwenden und prüfen', ['anwenden', 'fehler_finden'])],
              ETAPPEN, GEN,
              offen=['„umfang“ nennt auch rationale Exponenten; der Kl.-6-Lehrplan (lehrplan_gym) verlangt nur ganzzahlige Exponenten. Rationale Exponenten bewusst weggelassen (Stoff Kl. 9, eigenes Thema zahlen.rationale_exponenten).',
                     'Potenz einer Potenz (aᵐ)ⁿ = aᵐ·ⁿ ist nicht enthalten, weil der Kl.-6-Lehrplan nur gleiche Basis bzw. gleichen Exponenten nennt. Falls gewünscht, als eigene Lernkarte ergänzen.',
                     'Exponenten werden als Zahl abgefragt (z. B. „2³ · 2⁴ = 2ᵏ, k = ?“), weil die App keine Hochstellung eingeben kann.'])

if __name__ == '__main__':
    schreibe(DATEI)
