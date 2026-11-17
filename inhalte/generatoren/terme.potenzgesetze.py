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
     'regel': 'Ein negativer Exponent bedeutet ⟦Kehrbruch⟧: a⁻ⁿ = 1/aⁿ. Außerdem gilt ⟦a⁰ = 1⟧ (für a ≠ 0). Warum? Geht der Exponent um 1 runter, wird ⟦durch a geteilt⟧: 2³ = 8, 2² = 4, 2¹ = 2, 2⁰ = 1, 2⁻¹ = 1/2, 2⁻² = 1/4.',
     'schritte': ['Setze die Reihe fort: 2⁰ = 1, 2⁻¹ = 1/2, 2⁻² = 1/4, 2⁻³ = 1/8.', 'Also 2⁻³ = 1/2³ = ⟦1/8⟧ = 0,125.'],
     'probe': '2⁻³ · 2³ = 1/8 · 8 = 1 ✓',
     'fehler': '2⁰ = 0 ist falsch: Von 2¹ = 2 einmal durch 2 geteilt ergibt ⟦1⟧. Und 2⁻³ = −8 ist falsch: Das Minus im Exponenten macht ⟦keine negative Zahl⟧, sondern den Kehrbruch 1/8.'},
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
            return {**wahl(R, r, [str(n if frage == 'Basis' else b), str(b * n), str(b ** n)]), 'f': {'text': f'Was ist bei {pt(b, n)} {"die" if frage == "Basis" else "der"} {frage}?'},
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
        if b * n == b ** n: return g_begriff(3)
        r = -(b ** n)
        return {**wahl(R, zt(r), [zt(b ** n), zt(-b * n), zt(b * n)]), 'f': {'text': f'Was ergibt −{b}{hoch(n)}? (Ohne Klammer!)'},
                'w': f'Ohne Klammer gehört das Minus nicht zur Basis: −{b}{hoch(n)} = −({b}{hoch(n)}) = {zt(r)}. Dagegen wäre ({zt(-b)}){hoch(n)} = {b ** n}.', 'h': 'Der Exponent gehört nur zur Zahl direkt darunter.'}
    if art == 1:
        # nur knappe Fälle: Basis und Exponent vertauscht oder Werte nah beieinander
        (a, m), (b, n) = R.choice([((2, 5), (5, 2)), ((3, 4), (4, 3)), ((2, 4), (4, 2)), ((2, 6), (6, 2)), ((3, 3), (5, 2)), ((2, 7), (5, 3)),
                                   ((4, 4), (3, 5)), ((2, 8), (4, 4)), ((2, 9), (8, 3)), ((3, 5), (5, 3)), ((2, 10), (10, 3)), ((7, 2), (2, 6))])
        if R.random() < .5: (a, m), (b, n) = (b, n), (a, m)
        if a ** m == b ** n:
            r = 'Beide sind gleich groß'
            falsch = [pt(a, m), pt(b, n)]
        else:
            r = pt(a, m) if a ** m > b ** n else pt(b, n)
            falsch = [pt(b, n) if r == pt(a, m) else pt(a, m), 'Beide sind gleich groß']
        return {**wahl(R, r, falsch, 3), 'f': {'text': f'Welche Zahl ist größer: {pt(a, m)} oder {pt(b, n)}?'},
                'w': f'{pt(a, m)} = {zt(a ** m)}, {pt(b, n)} = {zt(b ** n)}. ' + ('Beide sind gleich groß.' if a ** m == b ** n else f'Größer: {r}.') + ' Vertauschen von Basis und Exponent ändert den Wert meistens.',
                'h': 'Rechne beide Potenzen aus. Raten nach der größeren Basis klappt hier nicht.'}
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
    art = R.randrange(4)
    if art == 3:
        b, n = R.choice([(10, 1), (10, 2), (10, 3), (10, 4), (2, 1), (2, 2), (2, 3), (2, 4), (5, 1), (5, 2), (4, 1), (4, 2), (20, 1), (25, 1)])
        x = Fr(1, b ** n)
        return {'y': 'zahl', 'f': {'text': f'{zt(x)} = {b}ᵏ. Wie groß ist k?'}, 'o': {'wert': -n}, 'c': f'-{n}',
                'w': f'{zt(x)} = 1/{zt(b ** n)} = 1/{pt(b, n)} = {pt(b, -n)}. Also k = {zt(-n)}.',
                'h': f'Schreibe {zt(x)} als Bruch mit Zähler 1. Welche Potenz von {b} steht im Nenner?'}
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
                'w': f'{m} + k = {s}, also k = {s} − {m} = {s - m}.', 'h': f'Welche Zahl musst du zu {m} addieren, damit {s} herauskommt?'}
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
                    'w': f'Exponenten subtrahieren: {kl(m)} − {kl(n)} = {zt(m - n)}.',
                    'h': 'Exponenten subtrahieren: oben minus unten. Minus eine negative Zahl wird plus.' if n < 0 else 'Gleiche Basis beim Teilen: Exponenten subtrahieren.'}
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


def zerlegen():
    """Rückwärts zerlegen: 36² = 4² · □² → 9."""
    a, x = R.choice([(2, 5), (4, 9), (3, 4), (2, 7), (5, 4), (4, 25), (3, 8), (6, 5), (2, 50), (8, 5), (4, 6)])
    n = R.randint(2, 5) if a * x <= 12 or a * x in (20, 100) else 2
    if R.random() < .5:
        txt = f'{pt(a * x, n)} = {pt(a, n)} · □{hoch(n)}. Welche Zahl gehört ins Kästchen?'
    else:
        txt = f'{pt(a * x, n)} = □{hoch(n)} · {pt(x, n)}. Welche Zahl gehört ins Kästchen?'
        a, x = x, a
    return {'y': 'zahl', 'f': {'text': txt}, 'o': {'wert': x}, 'c': f'{a * x} / {a}',
            'w': f'Gleicher Exponent: {pt(a, n)} · {pt(x, n)} = ({a} · {x}){hoch(n)} = {pt(a * x, n)}. Gesucht ist {a * x} : {a} = {x}.',
            'h': f'Gleicher Exponent heißt: Die Basen werden malgenommen. Welche Zahl mal {a} ergibt {a * x}?'}


def g_gleichexp(st):
    if st in (2, 3) and R.random() < .3:
        return zerlegen()
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
RECHNUNG = [0]   # Vorlage „Stimmt die Rechnung?“ höchstens 10-mal


def fehler_benennen():
    """Fehler in einer Potenzrechnung benennen (Auswahl)."""
    b = R.randint(2, 5)
    m, n = R.randint(2, 4), R.randint(2, 4)
    erk = {'basis': f'Die Basis bleibt {b}, nur die Exponenten werden addiert: {pt(b, m + n)}.',
           'mal': f'Die Exponenten werden addiert, nicht malgenommen: {pt(b, m + n)}.',
           'teilen': f'Exponenten subtrahieren, nicht teilen: {pt(b, m * n - n)}.',
           'negativ': f'Ein negativer Exponent bedeutet Kehrbruch, keine negative Zahl: {pt(b, -m)} = 1/{b ** m}.',
           'gleichexp': f'Gleicher Exponent: Basen malnehmen, der Exponent bleibt: {pt(10, m)}.'}
    art = R.choice(list(erk))
    if art == 'basis': txt = f'{pt(b, m)} · {pt(b, n)} = {pt(b * b, m + n)}'
    elif art == 'mal':
        if m * n == m + n: return fehler_benennen()
        txt = f'{pt(b, m)} · {pt(b, n)} = {pt(b, m * n)}'
    elif art == 'teilen': txt = f'{pt(b, m * n)} : {pt(b, n)} = {pt(b, m)}'
    elif art == 'negativ': txt = f'{pt(b, -m)} = {zt(-(b ** m))}'
    else: txt = f'{pt(2, m)} · {pt(5, m)} = {pt(10, 2 * m)}'
    andere = [erk[k] for k in erk if k != art]
    R.shuffle(andere)
    return {**wahl(R, erk[art], andere[:2] + ['Nichts, die Rechnung ist richtig.']), 'f': {'text': f'Ein Kind rechnet: {txt}. Was ist falsch?'},
            'w': erk[art], 'h': 'Schreibe die Potenzen aus oder rechne mit kleinen Zahlen nach.'}


def g_fehler(st):
    if st == 3 or (st == 2 and R.random() < .5) or RECHNUNG[0] >= 10:
        return fehler_benennen()
    b = R.randint(2, 5)
    m, n = R.randint(2, 4), R.randint(2, 4)
    if st == 1:
        aussagen = [(f'{pt(b, m)} = {b * m}', False, f'Nein, {pt(b, m)} = {" · ".join([str(b)] * m)} = {b ** m}.'),
                    (f'{pt(b, m)} · {pt(b, n)} = {pt(b, m + n)}', True, 'Ja, gleiche Basis: Exponenten addieren.'),
                    (f'{pt(b, -m)} ist eine negative Zahl.', False, f'Nein, {pt(b, -m)} = 1/{b ** m} ist positiv.'),
                    (f'{b}⁰ = 0', False, f'Nein, jede Zahl außer 0 hoch 0 ergibt 1: {b}⁰ = 1.')]
    else:
        aussagen = [(f'{pt(b, m)} · {pt(b, n)} = {pt(b, m * n)}', m * n == m + n, f'{"Ja" if m * n == m + n else "Nein"}, die Exponenten werden addiert: {pt(b, m + n)}.'),
                    (f'{pt(b, m + n)} : {pt(b, n)} = {pt(b, m)}', True, 'Ja, Exponenten subtrahieren.'),
                    (f'{pt(-b, 2)} = {zt(-b * b)}', False, f'Nein, ({zt(-b)}) · ({zt(-b)}) = {b * b}.'),
                    (f'{pt(2, m)} · {pt(5, m)} = {pt(10, 2 * m)}', False, f'Nein, gleicher Exponent: Basen malnehmen, Exponent bleibt: {pt(10, m)}.')]
    s_, stimmt, grund = R.choice(aussagen)
    if stimmt and not grund.startswith('Ja'): grund = 'Ja. ' + grund
    if not stimmt and not grund.startswith('Nein'): grund = 'Nein. ' + grund
    rechnung = '=' in s_
    if rechnung: RECHNUNG[0] += 1
    gegen = ('Ja, das stimmt.' if rechnung else 'Ja, die Aussage stimmt.') if not stimmt else ('Nein, das ist falsch.' if rechnung else 'Nein, die Aussage ist falsch.')
    return {**wahl(R, grund, [gegen, 'Das kann man nicht entscheiden.'], 3), 'f': {'text': f'Stimmt die Rechnung? {s_}' if rechnung else f'Stimmt die Aussage? „{s_}“'},
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

# ---------- KARTEN: Lernkarten nach dem neuen Muster (Achte Runde, Vorgabe 16.11., Paket U6) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl6.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl6 import umbau  # noqa: E402

KARTEN = {
 'potenz_begriff': {
  'einstieg': 'Du faltest ein Blatt immer wieder in der Mitte: 2, 4, 8, 16 Lagen. Statt 2 · 2 · 2 · 2 schreibt man kurz 2⁴. Das ist eine ⟦Potenz⟧.',
  'woerter': [['Potenz', 'ein Produkt aus lauter gleichen Faktoren, kurz geschrieben: 2⁴'],
              ['Basis', 'die Zahl unten, die malgenommen wird'],
              ['Exponent', 'die kleine Zahl oben: wie oft die Basis vorkommt']],
  'bild': {'typ': 'tabelle', 'kopf': ['Faltungen', '1', '2', '3', '4'], 'zeilen': [['Lagen', '2', '', '', '']]},
  'schritte': [{'text': 'Jedes Falten verdoppelt die Lagen: 2, 4, 8, 16.', 'bild': {'zeilen': [['Lagen', '2', '4', '8', '16']]}},
               {'text': 'Nach 4-mal Falten: 2 · 2 · 2 · 2 = ⟦2⁴ = 16⟧.',
                'bild': {'zeilen': [['Lagen', '2', '4', '8', '16'], ['Potenz', '2¹', '2²', '2³', '2⁴']]}},
               {'text': 'Bei 2⁴ ist die Basis 2 und der Exponent 4.'},
               {'text': 'Negative Basis in Klammern: (−2)³ = (−2) · (−2) · (−2) = ⟦−8⟧.'}],
  'fehler': '2⁴ = 8 ist falsch: Das wäre 2 · 4. Nach 4-mal Falten hast du aber 16 Lagen.',
  'fehler_bild': {'zeilen': [['Lagen', '2', '4', '8', '16'], ['2 · 4?', '', '', '', '8']]},
  'regel': 'Der ⟦Exponent⟧ sagt, wie oft die Basis malgenommen wird. Eine negative Basis steht in Klammern.'},
 'negativer_exponent': {
  'einstieg': 'Spiel das Falten rückwärts: 8, 4, 2, 1 Lage. Jedes Mal wird durch 2 geteilt, der Exponent wird um 1 kleiner. Hochzahlen unter null heißen ⟦negative Exponenten⟧.',
  'woerter': [['negative Exponenten', 'Hochzahlen mit Minus, z. B. 2⁻³'],
              ['Kehrbruch', 'Zähler und Nenner vertauscht: Der Kehrbruch von 8 ist 1/8']],
  'bild': {'typ': 'tabelle', 'kopf': ['Potenz', '2³', '2²', '2¹', '2⁰', '2⁻¹', '2⁻²', '2⁻³'], 'zeilen': [['Wert', '8', '4', '2', '', '', '', '']]},
  'schritte': [{'text': 'Von 2¹ = 2 einmal durch 2 geteilt: 2⁰ = ⟦1⟧.',
                'bild': {'zeilen': [['Wert', '8', '4', '2', '1', '', '', '']]}},
               {'text': 'Weiter durch 2: 2⁻¹ = 1/2, 2⁻² = 1/4, 2⁻³ = 1/8.',
                'bild': {'zeilen': [['Wert', '8', '4', '2', '1', '1/2', '1/4', '1/8']]}},
               {'text': '2⁻³ ist der Kehrbruch von 2³: ⟦1/8⟧.'}],
  'fehler': '2⁻³ = −8 ist falsch. Das Minus im Exponenten macht keine negative Zahl, sondern den Kehrbruch 1/8.',
  'regel': 'Ein ⟦negativer Exponent⟧ bedeutet Kehrbruch: a⁻ⁿ = 1/aⁿ. Außerdem gilt a⁰ = 1.'},
 'mal_gleiche_basis': {
  'einstieg': 'Ein Blatt wird erst 3-mal gefaltet, dann noch 4-mal. Zusammen sind das 7 Faltungen. Darum gilt 2³ · 2⁴ = 2⁷: ⟦gleiche Basis⟧, Exponenten addieren.',
  'woerter': [['gleiche Basis', 'beide Potenzen haben unten dieselbe Zahl']],
  'bild': {'typ': 'tabelle', 'kopf': ['Potenz', 'ausgeschrieben', 'Faktoren'], 'zeilen': [['2³', '2 · 2 · 2', '3'], ['2⁴', '2 · 2 · 2 · 2', '4']]},
  'schritte': [{'text': 'Schreib beide Potenzen als Malaufgabe aus, wie in der Tabelle.'},
               {'text': 'Zähle die Faktoren 2: 3 + 4 = 7.',
                'bild': {'zeilen': [['2³', '2 · 2 · 2', '3'], ['2⁴', '2 · 2 · 2 · 2', '4'], ['2³ · 2⁴', '7-mal die 2', '7']]}},
               {'text': 'Also ist 2³ · 2⁴ = ⟦2⁷ = 128⟧.'}],
  'fehler': '2³ · 2⁴ = 2¹² ist falsch. Gefaltet wird 3-mal und dann 4-mal, nicht 12-mal.',
  'regel': 'Bei ⟦gleicher Basis⟧ addierst du beim Malnehmen die Exponenten. Die Basis bleibt.'},
 'geteilt_gleiche_basis': {
  'einstieg': '1 000 000 € Gewinn werden an 10 000 Menschen verteilt. Das ist 10⁶ : 10⁴. Beim Teilen streichst du 4 Nullen: ⟦Exponenten subtrahieren⟧.',
  'woerter': [['subtrahieren', 'abziehen']],
  'bild': {'typ': 'tabelle', 'kopf': ['Potenz', 'Zahl'], 'zeilen': [['10⁶', '1 000 000'], ['10⁴', '10 000']]},
  'schritte': [{'text': 'Oben stehen 6 Faktoren 10, unten stehen 4.'},
               {'text': '4 Faktoren kürzen sich weg. Es bleiben 6 − 4 = 2.'},
               {'text': '10⁶ : 10⁴ = ⟦10² = 100⟧. Jeder bekommt 100 €.',
                'bild': {'zeilen': [['10⁶', '1 000 000'], ['10⁴', '10 000'], ['10⁶ : 10⁴', '100']]}}],
  'fehler': '10⁶ : 10³ = 10² ist falsch. Die Exponenten werden subtrahiert, nicht geteilt: 10³.',
  'regel': 'Bei ⟦gleicher Basis⟧ subtrahierst du beim Teilen die Exponenten. Die Basis bleibt.'},
 'gleicher_exponent': {
  'einstieg': '2 mal 5 ist 10. Dreimal die 2 und dreimal die 5 ergeben 3 Paare zu je 10. Das geht bei ⟦gleichem Exponenten⟧.',
  'woerter': [['gleichem Exponenten', 'beide Potenzen haben oben dieselbe Zahl']],
  'bild': {'typ': 'tabelle', 'kopf': ['Paar', '1', '2', '3'], 'zeilen': [['2 · 5', '10', '10', '10']]},
  'schritte': [{'text': '2³ · 5³ = 2 · 2 · 2 · 5 · 5 · 5.'},
               {'text': 'Ordne zu Paaren: 2 · 5 kommt dreimal vor, also (2 · 5)³.'},
               {'text': 'Jedes Paar ist 10: 10³ = ⟦1 000⟧.'}],
  'fehler': '2³ · 5³ = 10⁶ ist falsch. Es gibt nur 3 Paare zu je 10, nicht 6.',
  'regel': 'Bei ⟦gleichem Exponenten⟧ nimmst du die Basen mal. Der Exponent bleibt: aⁿ · bⁿ = (a · b)ⁿ.'},
 'anwenden': {
  'einstieg': 'Ein Stapel aus 8 Lagen wird noch 4-mal gefaltet. 8 Lagen entstehen durch 3-mal Falten, also 2³. Dann passt ein ⟦Potenzgesetz⟧.',
  'woerter': [['Potenzgesetz', 'eine Regel zum Zusammenfassen von Potenzen']],
  'bild': {'typ': 'tabelle', 'kopf': ['Zahl', '4', '8', '9'], 'zeilen': [['als Potenz', '2²', '2³', '3²']]},
  'schritte': [{'text': 'Gesucht ist 8 · 2⁴. Schreib 8 als Potenz: 8 = 2³.'},
               {'text': 'Jetzt hast du gleiche Basis: 2³ · 2⁴ = 2⁷.'},
               {'text': '2⁷ = ⟦128⟧ Lagen.'}],
  'fehler': '3² · 2³ = 6⁵ ist falsch. Weder Basis noch Exponent sind gleich. Rechne aus: 9 · 8 = 72.',
  'regel': 'Prüfe zuerst: ⟦gleiche Basis oder gleicher Exponent?⟧ Sonst schreib eine Zahl als Potenz oder rechne aus.'},
 'fehler_finden': {
  'einstieg': 'Ein Freund sagt: „Beim Malnehmen werden Exponenten malgenommen“. Er rechnet 3² · 3³ = 3⁶. Du prüfst das mit einer ⟦Zahlenprobe⟧.',
  'woerter': [['Zahlenprobe', 'beide Seiten mit Zahlen ausrechnen und vergleichen']],
  'bild': {'typ': 'tabelle', 'kopf': ['Rechnung', 'Wert'], 'zeilen': [['3² · 3³', '?'], ['3⁶', '?']]},
  'schritte': [{'text': 'Links: 3² · 3³ = 9 · 27 = 243.', 'bild': {'zeilen': [['3² · 3³', '243'], ['3⁶', '?']]}},
               {'text': 'Rechts: 3⁶ = 729. Das passt nicht.', 'bild': {'zeilen': [['3² · 3³', '243'], ['3⁶', '729']]}},
               {'text': 'Aber 3⁵ = 243. Richtig ist ⟦3⁵⟧.', 'bild': {'zeilen': [['3² · 3³', '243'], ['3⁶', '729'], ['3⁵', '243']]}}],
  'fehler': 'Regeln nur auswendig anzuwenden führt zu Verwechslungen. Schreib aus: (3 · 3) · (3 · 3 · 3) sind 5 Faktoren.',
  'regel': 'Prüfe Potenzen mit einer ⟦Zahlenprobe⟧ oder schreib sie aus. Typisch: Exponenten malnehmen statt addieren.'},
}

umbau(DATEI, KARTEN)



# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl6): je Lernkarte 2 Übungen Stufe 2 + 4 Übungen Stufe 3 ----------
# Läuft nach allen bisherigen Aufgaben mit eigenem Zufallsstart; die bisherigen Aufgaben bleiben unverändert.
# Prüfungsvorbilder: Bayerischer Mathematik-Test Jgst. 8 (ISB) 2021 Aufg. 1 (gehört das Minus zur Basis?), 2023 Aufg. 1c (Potenz eines Bruchs),
# 2025 Aufg. 2b (Maßstab 1 : 10 – Volumen ändert sich mit 10³), 2021 Aufg. 6b und 2023 Aufg. 6 (Größen mit Zehnerpotenzen);
# Känguru 5/6 / Mathematik-Olympiade Kl. 6: Endziffern von Potenzen, Potenzen ohne Ausrechnen vergleichen (eigene Aufgaben).
from _schwer_kl6 import ergaenzen, zahl, wahl, luecken, anteil  # noqa: E402

_HB = 'Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt.'


def _pg():
    return {
        'potenz_begriff': [
            (2, lambda R: zahl('Berechne (−2)³.', -8, '(-2) ** 3', 'Die Klammer gehört zur Basis: dreimal (−2) als Faktor.', '(−2) · (−2) · (−2) = 4 · (−2) = −8.')),
            (2, lambda R: zahl('Berechne (1/10)⁴. Gib das Ergebnis als Dezimalzahl an.', Fr('0.0001'), '(1/10) ** 4', '1/10 = 0,1. Wie oft wird 0,1 malgenommen?',
                               '0,1 · 0,1 · 0,1 · 0,1 = 0,0001.')),
            (3, lambda R: zahl('Berechne −3² + (−3)².', 0, '-(3 ** 2) + (-3) ** 2', 'Achtung: Bei −3² gehört das Minus nicht zur Basis.',
                               '−3² = −(3 · 3) = −9. (−3)² = (−3) · (−3) = 9. Zusammen −9 + 9 = 0.')),
            (3, lambda R: zahl('Ein Modellwürfel ist in jeder Kante 10-mal kürzer als ein großer Würfel. Wie viele Modellwürfel passen in den großen Würfel?', 1000,
                               '10 ** 3', 'Denke an Länge, Breite und Höhe: In jeder Richtung passen 10 kleine Würfel.',
                               '10 · 10 · 10 = 10³ = 1 000. Das Volumen ändert sich nicht mit 10, sondern mit 10³.')),
            (3, lambda R: zahl('Auf welche Ziffer endet 3²⁰?', 1, '3 ** 20 % 10', 'Schreibe die Endziffern von 3¹, 3², 3³, 3⁴, 3⁵ auf. Was fällt dir auf?',
                               'Die Endziffern wiederholen sich: 3, 9, 7, 1, 3, 9, 7, 1 … 20 ist durch 4 teilbar, also endet 3²⁰ wie 3⁴ auf 1.')),
            (3, lambda R: wahl(R, 'Welche Zahl ist größer: 2¹⁰ oder 10³?', '2¹⁰', ['10³', 'Beide sind gleich groß'],
                               'Rechne beide aus: 2¹⁰ durch Verdoppeln.', '2¹⁰ = 1 024 und 10³ = 1 000. 2¹⁰ ist etwas größer.', n=3)),
        ],
        'negativer_exponent': [
            (2, lambda R: luecken('Berechne (2/3)⁻².', '□/□', _HB, [9, 4], ['3 ** 2', '2 ** 2'], 'Negativer Exponent: Kehrbruch, dann quadrieren.',
                                  '(2/3)⁻² = (3/2)² = 9/4.')),
            (2, lambda R: zahl('Berechne 5⁰ + 5⁻¹. Gib das Ergebnis als Dezimalzahl an.', Fr('1.2'), '5 ** 0 + 5 ** -1', 'a⁰ = 1 und a⁻¹ = 1/a.', '5⁰ = 1, 5⁻¹ = 1/5 = 0,2. Zusammen 1,2.')),
            (3, lambda R: wahl(R, 'Welche dieser Zahlen ist negativ?', '(−2)⁻³', ['2⁻³', '(−2)⁻²', '(−2)⁰'],
                               'Ein negativer Exponent macht keine negative Zahl. Entscheidend ist die Basis und ob der Exponent gerade ist.',
                               '(−2)⁻³ = 1/(−2)³ = −1/8 ist negativ. 2⁻³ = 1/8, (−2)⁻² = 1/4, (−2)⁰ = 1 sind positiv.')),
            (3, lambda R: wahl(R, 'Welche Zahl ist am kleinsten: 2⁻³, 3⁻², 4⁻¹ oder 0,1?', '0,1', ['2⁻³', '3⁻²', '4⁻¹'],
                               'Schreibe alle als Bruch oder Dezimalzahl.', '2⁻³ = 1/8 = 0,125; 3⁻² = 1/9 ≈ 0,111; 4⁻¹ = 0,25; 0,1 = 1/10. Am kleinsten: 0,1.')),
            (3, lambda R: zahl('Für welchen Exponenten n gilt 4ⁿ = 1/64?', -3, '-3', 'Welche Potenz von 4 ergibt 64? Ein Kehrbruch heißt negativer Exponent.',
                               '4³ = 64, also 1/64 = 4⁻³ und n = −3.')),
            (3, lambda R: luecken('Ein Kind rechnet 5⁻² = 1/10. Wie heißt der Bruch richtig?', '□/□', _HB, [1, 25], ['1', '5 ** 2'],
                                  'Kehrbruch von 5², nicht von 5 · 2.', '5⁻² = 1/5² = 1/25. Das Kind hat 5 · 2 statt 5 · 5 gerechnet.')),
        ],
        'mal_gleiche_basis': [
            (2, lambda R: zahl('x² · x · x⁴ = xᵏ. Wie groß ist k?', 7, '2 + 1 + 4', 'Das x in der Mitte hat den Exponenten 1.', 'x² · x¹ · x⁴ = x²⁺¹⁺⁴ = x⁷.')),
            (2, lambda R: zahl('3⁴ · 3⁻⁶ = 3ᵏ. Wie groß ist k?', -2, '4 + (-6)', 'Exponenten addieren, auch wenn einer negativ ist.', '4 + (−6) = −2, also 3⁻².')),
            (3, lambda R: zahl('Ein Lichtjahr sind etwa 9,5 · 10¹² km. Wie viele km sind 10⁴ Lichtjahre? Schreibe das Ergebnis als 9,5 · 10ᵏ km. Wie groß ist k?', 16, '12 + 4',
                               'Gleiche Basis 10: Exponenten addieren.', '9,5 · 10¹² · 10⁴ = 9,5 · 10¹⁶ km, also k = 16.')),
            (3, lambda R: zahl('2ᵃ · 2ᵇ = 2¹⁰. a und b sind natürliche Zahlen ab 1. Wie viele Paare (a | b) gibt es?', 9, '10 - 1',
                               'a + b muss 10 ergeben. Schreibe die Paare auf: (1 | 9), (2 | 8), …', 'a + b = 10 mit a, b ≥ 1: a = 1 bis 9. Das sind 9 Paare.')),
            (3, lambda R: zahl('27 · 3⁵ = 3ᵏ. Wie groß ist k?', 8, '3 + 5', 'Schreibe 27 als Potenz von 3.', '27 = 3³. 3³ · 3⁵ = 3⁸, also k = 8.')),
            (3, lambda R: zahl('Ein Kind rechnet a³ · a⁴ = a¹². Wie heißt der richtige Exponent?', 7, '3 + 4', 'Schreibe die Faktoren aus: a · a · a mal a · a · a · a.',
                               'Es sind 3 + 4 = 7 Faktoren a, also a⁷. Das Kind hat die Exponenten malgenommen.')),
        ],
        'geteilt_gleiche_basis': [
            (2, lambda R: zahl('x⁸ : x = xᵏ. Wie groß ist k?', 7, '8 - 1', 'x hat den Exponenten 1.', 'x⁸ : x¹ = x⁸⁻¹ = x⁷.')),
            (2, lambda R: zahl('5³ : 5³ = 5ᵏ. Wie groß ist k?', 0, '3 - 3', 'Exponenten subtrahieren. Was ist 5³ : 5³ als Zahl?', '3 − 3 = 0, also 5⁰. Und tatsächlich: 125 : 125 = 1 = 5⁰.')),
            (3, lambda R: zahl('Eine Festplatte fasst 8 · 10¹² Byte, ein Film braucht 4 · 10⁹ Byte. Wie viele Filme passen auf die Festplatte?', 2000,
                               '(8 * 10 ** 12) / (4 * 10 ** 9)', 'Teile die Zahlen vorne und die Zehnerpotenzen getrennt.',
                               '8 : 4 = 2 und 10¹² : 10⁹ = 10³. Also 2 · 10³ = 2 000 Filme.')),
            (3, lambda R: zahl('2¹⁰ : 2ⁿ = 1/4. Wie groß ist n?', 12, '10 + 2', 'Schreibe 1/4 als Potenz von 2.',
                               '1/4 = 2⁻². Also 10 − n = −2 und n = 12.')),
            (3, lambda R: zahl('Berechne 6⁵ : (2⁵ · 3⁴).', 3, '6 ** 5 / (2 ** 5 * 3 ** 4)', 'Schreibe 6⁵ als 2⁵ · 3⁵.',
                               '6⁵ = 2⁵ · 3⁵. Geteilt durch 2⁵ · 3⁴ bleibt 3⁵ : 3⁴ = 3.')),
            (3, lambda R: zahl('Ein Kind rechnet 10⁶ : 10² = 10³. Wie heißt der richtige Exponent?', 4, '6 - 2',
                               'Beim Teilen werden die Exponenten subtrahiert, nicht geteilt.', '10⁶ : 10² = 10⁶⁻² = 10⁴ (1 000 000 : 100 = 10 000).')),
        ],
        'gleicher_exponent': [
            (2, lambda R: zahl('Berechne geschickt: 0,25³ · 8³', 8, '0.25 ** 3 * 8 ** 3', 'Gleicher Exponent: Basen zuerst malnehmen.', '0,25³ · 8³ = (0,25 · 8)³ = 2³ = 8.')),
            (2, lambda R: zahl('Berechne geschickt: 12³ : 4³', 27, '12 ** 3 / 4 ** 3', 'Gleicher Exponent: Basen zuerst teilen.', '12³ : 4³ = (12 : 4)³ = 3³ = 27.')),
            (3, lambda R: luecken('Berechne geschickt: (3/4)² · (4/9)²', '□/□', _HB, [1, 9], ['1', '3 ** 2'], 'Nimm zuerst die Brüche in der Klammer mal.',
                                  '(3/4 · 4/9)² = (12/36)² = (1/3)² = 1/9.')),
            (3, lambda R: zahl('Welche Zahl gehört ins Kästchen? □³ · 4³ = 1 000', Fr('2.5'), '10 / 4', 'Schreibe 1 000 als Potenz mit dem Exponenten 3.',
                               '1 000 = 10³. Also (□ · 4)³ = 10³ und □ · 4 = 10, □ = 2,5.')),
            (3, lambda R: zahl('Berechne geschickt: 25⁴ · 0,04⁴', 1, '(25 * 0.04) ** 4', 'Was ergibt 25 · 0,04?', '25 · 0,04 = 1. Also (25 · 0,04)⁴ = 1⁴ = 1.')),
            (3, lambda R: zahl('Ein Kind rechnet 2³ · 3³ = 6⁹. Richtig ist 6ᵏ. Wie groß ist k?', 3, '3', 'Gleicher Exponent: Die Basen werden malgenommen, der Exponent bleibt.',
                               '2³ · 3³ = (2 · 3)³ = 6³. Probe: 8 · 27 = 216 = 6³.')),
        ],
        'anwenden': [
            (2, lambda R: zahl('Berechne geschickt: 5³ · 2⁵', 4000, '5 ** 3 * 2 ** 5', 'Zerlege 2⁵ in 2³ · 2².', '5³ · 2⁵ = (5 · 2)³ · 2² = 1 000 · 4 = 4 000.')),
            (2, lambda R: zahl('100² · 10³ = 10ᵉ. Wie groß ist e?', 7, '2 * 2 + 3', 'Schreibe 100 als Potenz von 10.', '100² = 100 · 100 = 10² · 10² = 10⁴. 10⁴ · 10³ = 10⁷.')),
            (3, lambda R: zahl('Ein Blatt Papier ist 0,1 mm dick. Nach 10-mal Falten liegen 2¹⁰ Lagen übereinander. Wie hoch ist der Stapel in cm? Runde auf eine Nachkommastelle.',
                               Fr('10.2'), 'round(2 ** 10 * 0.1 / 10, 1)', 'Berechne 2¹⁰, dann die Höhe in mm, dann in cm.',
                               '2¹⁰ = 1 024 Lagen. 1 024 · 0,1 mm = 102,4 mm = 10,24 cm ≈ 10,2 cm.', einheit='cm', toleranz=0.1)),
            (3, lambda R: wahl(R, 'Welche Zahl ist größer: 2³⁰ oder 3²⁰?', '3²⁰', ['2³⁰', 'Beide sind gleich groß'],
                               'Fasse je 3 Faktoren 2 zu einer 8 und je 2 Faktoren 3 zu einer 9 zusammen.', '30 Faktoren 2 sind 10 Gruppen 2 · 2 · 2 = 8, also 2³⁰ = 8¹⁰. Ebenso 3²⁰ = 9¹⁰. Gleicher Exponent, größere Basis: 3²⁰ ist größer.', n=3)),
            (3, lambda R: zahl('4³ · 8² = 2ᵉ. Wie groß ist e?', 12, '2 * 3 + 3 * 2', 'Schreibe 4 und 8 als Potenz von 2.', '4³ = 2² · 2² · 2² = 2⁶ und 8² = 2³ · 2³ = 2⁶. 2⁶ · 2⁶ = 2¹².')),
            (3, lambda R: zahl('Wie viele Nullen stehen am Ende von 2⁶ · 5⁸, wenn du die Zahl ausschreibst?', 6, '6',
                               'Je ein Paar 2 · 5 gibt eine 10.', '2⁶ · 5⁸ = (2 · 5)⁶ · 5² = 10⁶ · 25 = 25 000 000. Am Ende stehen 6 Nullen.')),
        ],
        'fehler_finden': [
            (2, lambda R: zahl('Ein Kind rechnet (−1)⁴ = −1. Wie heißt das richtige Ergebnis?', 1, '(-1) ** 4', 'Vier Minuszeichen als Faktoren: gerade Anzahl.',
                               '(−1) · (−1) · (−1) · (−1) = 1. Bei geradem Exponenten wird es positiv.')),
            (2, lambda R: wahl(R, 'Ein Kind rechnet 0,2² = 0,4. Was ist der Fehler?', 'Es hat 0,2 · 2 gerechnet. Richtig: 0,2 · 0,2 = 0,04.',
                               ['Es gibt keinen Fehler.', 'Richtig wäre 0,02.', 'Richtig wäre 4.'],
                               'Der Exponent sagt, wie oft die Basis als Faktor vorkommt.', '0,2² = 0,2 · 0,2 = 0,04 (zwei Nachkommastellen).')),
            (3, lambda R: zahl('Ein Kind rechnet −4² = 16. Wie heißt das richtige Ergebnis?', -16, '-(4 ** 2)', 'Ohne Klammer gehört das Minus nicht zur Basis.',
                               '−4² = −(4 · 4) = −16. Nur (−4)² wäre 16.')),
            (3, lambda R: zahl('Ein Kind rechnet 2³ + 2³ = 2⁶. Welche Zahl ist richtig?', 16, '2 ** 3 + 2 ** 3', 'Für Plus gibt es kein Potenzgesetz. Rechne aus.',
                               '2³ + 2³ = 8 + 8 = 16 = 2⁴. 2⁶ wäre 64.')),
            (3, lambda R: wahl(R, 'Welche Rechnung ist richtig?', '3² · 3⁴ = 3⁶', ['3² + 3⁴ = 3⁶', '3⁴ : 3² = 1²', '2³ · 5³ = 10⁶'],
                               'Prüfe jede Rechnung mit dem passenden Potenzgesetz oder durch Ausrechnen.',
                               '3² · 3⁴ = 3⁶ stimmt (Exponenten addieren). 3² + 3⁴ = 90, 3⁶ = 729. 3⁴ : 3² = 3². 2³ · 5³ = 10³.')),
            (3, lambda R: wahl(R, 'Ein Kind behauptet: „aⁿ ist immer größer als a, wenn n größer als 1 ist.“ Welches Beispiel widerlegt das?',
                               'a = 1/2, n = 2', ['a = 3, n = 2', 'a = 2, n = 3', 'a = 10, n = 2'],
                               'Probiere eine Zahl kleiner als 1.', '(1/2)² = 1/4 ist kleiner als 1/2. Die anderen Beispiele bestätigen die Behauptung nur.')),
        ],
    }


ergaenzen(DATEI, _pg(), seed=6030)


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('terme.potenzgesetze', 13_6_5)
_h = 'Schreibe die Potenzen aus oder rechne mit kleinen Zahlen nach.'
_q = '{} Welcher Satz beschreibt den Fehler richtig?'


def _mal(b, m, n, falsch, art):
    """Kind rechnet b^m · b^n = falsch. art 'basis': Basis wurde mitmultipliziert; art 'exp': Exponenten malgenommen."""
    hoch = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')
    e = lambda x: str(x).translate(hoch)
    if art == 'basis':
        richtig = f'Die Basis bleibt {b}, nur die Exponenten werden addiert: {b}{e(m + n)}.'
        weg = f'Gleiche Basis: Die Basis bleibt {b}, die Exponenten werden addiert. Also {b}{e(m)} · {b}{e(n)} = {b}{e(m + n)}, nicht {b * b}{e(m + n)}.'
    else:
        richtig = f'Die Exponenten werden addiert, nicht malgenommen: {b}{e(m + n)}.'
        weg = f'Gleiche Basis: Exponenten addieren. {b}{e(m)} · {b}{e(n)} = {b}{e(m + n)}, nicht {b}{e(m * n)}.'
    falsche = ['Nichts, die Rechnung ist richtig.', f'Die Exponenten werden malgenommen: {b}{e(m * n)}.' if art == 'basis' else f'Die Basen werden malgenommen: {b * b}{e(m + n)}.',
               f'Die Exponenten werden subtrahiert: {b}{e(abs(m - n))}.']
    return BF.A(_q.format(f'Ein Kind rechnet: {b}{e(m)} · {b}{e(n)} = {falsch}.'), richtig, falsche, weg, _h)


# c) mehrdeutig: zwei Antworten sind wahre Sätze mit demselben richtigen Ergebnis → Ablenker mit anderen Ergebnissen
BF.ersetze('fehler_finden', 'Ein Kind rechnet: 4³ · 4² = 16⁵. Was ist falsch?', _mal(4, 3, 2, '16⁵', 'basis'))
BF.ersetze('fehler_finden', 'Ein Kind rechnet: 3³ · 3³ = 9⁶. Was ist falsch?', _mal(3, 3, 3, '9⁶', 'basis'))
BF.ersetze('fehler_finden', 'Ein Kind rechnet: 4⁴ · 4² = 16⁶. Was ist falsch?', _mal(4, 4, 2, '16⁶', 'basis'))
BF.ersetze('fehler_finden', 'Ein Kind rechnet: 4³ · 4³ = 4⁹. Was ist falsch?', _mal(4, 3, 3, '4⁹', 'exp'))
# c) Ablenker nennt dasselbe Ergebnis wie die richtige Antwort (verwirrend)
BF.ersetze('fehler_finden', 'Ein Kind rechnet: 3⁹ : 3³ = 3³. Was ist falsch?', BF.A(
    _q.format('Ein Kind rechnet: 3⁹ : 3³ = 3³.'), 'Exponenten subtrahieren, nicht teilen: 3⁶.',
    ['Nichts, die Rechnung ist richtig.', 'Die Exponenten werden addiert: 3¹².', 'Die Basen werden geteilt: 1³.'],
    'Gleiche Basis beim Teilen: Exponenten subtrahieren. 3⁹ : 3³ = 3⁹⁻³ = 3⁶, nicht 3⁹:³ = 3³.', _h))
# a) reines Ausrechnen bzw. Grundform
for _k in (4, 7, 9, 6):
    BF.stufe('potenz_begriff', f'Ein Würfel hat die Kantenlänge {_k} cm. Sein Volumen ist {_k}³ cm³. Berechne das Volumen.', 2)
for _t in ('Berechne 10⁵ : 10³.', 'Berechne 2⁸ : 2⁶.', 'Berechne 3⁷ : 3⁵.'):
    BF.stufe('geteilt_gleiche_basis', _t, 2)
BF.stufe('mal_gleiche_basis', 'Berechne 2² · 2² mit dem Potenzgesetz und gib den Wert an.', 1)

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----


# ---------- DURCHSICHT (Neunzehnte Runde, Teil A, Zweig durchsicht-kl6) ----------
from _durchsicht_kl6 import Befunde, befunde_anwenden  # noqa: E402

DS = Befunde('terme.potenzgesetze', 19_6_5)
_S = DS.stufe
# potenz_begriff: Würfelvolumen viermal hintereinander; eine Potenz direkt ausrechnen = Stufe-1-Gedanke
for _t in ('Ein Würfel hat die Kantenlänge 4 cm. Sein Volumen ist 4³ cm³. Berechne das Volumen.', 'Ein Würfel hat die Kantenlänge 9 cm. Sein Volumen ist 9³ cm³. Berechne das Volumen.'):
    _S('potenz_begriff', _t, 1)
# negativer_exponent: Summe zweier Potenzen mit negativem Exponenten viermal gleich gebaut = wie 5⁰ + 5⁻¹ in Stufe 2
for _t in ('Berechne 3⁻² + 3⁻¹.', 'Berechne 4⁻³ + 4⁻¹.', 'Berechne 3⁻² + 3⁻³.', 'Berechne 4⁻¹ + 4⁻².'):
    _S('negativer_exponent', _t, 2)
# mal_gleiche_basis: Exponenten addieren und Wert ausrechnen = Stufe 1; Dezimalzahl-Ergebnis und zweite Lücke = Stufe 2
_S('mal_gleiche_basis', 'Berechne 2³ · 2² mit dem Potenzgesetz und gib den Wert an.', 1)
for _t in ('Ergänze den Exponenten: 5⁵ · 5ᵏ = 5¹³. Wie groß ist k?', 'Berechne 10⁶ · 10⁻⁸ und gib das Ergebnis als Dezimalzahl an.',
           'Berechne 10² · 10⁻⁸ und gib das Ergebnis als Dezimalzahl an.'):
    _S('mal_gleiche_basis', _t, 2)
# geteilt_gleiche_basis: Dezimalzahl-Ergebnis und zwei Gesetze nacheinander = mehrere Schritte → S2
for _t in ('Berechne 10¹ : 10⁶ und gib das Ergebnis als Dezimalzahl an.', '2³ · 2³ : 2¹ = 2ᵉ. Wie groß ist e?', '3⁵ · 3³ : 3⁴ = 3ᵉ. Wie groß ist e?'):
    _S('geteilt_gleiche_basis', _t, 2)
# gleicher_exponent: Basen zum Produkt 1, 10, 100 zusammenfassen = Stufe-2-Muster („geschickt“)
for _t in ('Berechne geschickt: 2⁻¹ · 5⁻¹ und gib das Ergebnis als Dezimalzahl an.', 'Berechne geschickt: 5⁻¹ · 20⁻¹ und gib das Ergebnis als Dezimalzahl an.',
           'Berechne geschickt: (4/5)³ · 5³', 'Berechne geschickt: 25⁴ · 0,04⁴'):
    _S('gleicher_exponent', _t, 2)
# anwenden: Falten = Verdoppeln eingekleidet; 16 · 4 als Zweierpotenz und zweite Auswahl gleicher Bauart → S2
for _t in ('Ein Blatt Papier wird 8-mal in der Mitte gefaltet. Jedes Falten verdoppelt die Anzahl der Lagen. Wie viele Lagen liegen danach übereinander?',
           'Ein Blatt Papier wird 4-mal in der Mitte gefaltet. Jedes Falten verdoppelt die Anzahl der Lagen. Wie viele Lagen liegen danach übereinander?',
           '16 · 4 = 2ᵉ. Wie groß ist e?', 'Was ergibt 2³ · 5²?'):
    _S('anwenden', _t, 2)
# fehler_finden: zweiter „Basis malgenommen“-Fehler und negativer Exponent = schon in Stufe 2 → S2
for _t in ('Ein Kind rechnet: 4³ · 4² = 16⁵. Welcher Satz beschreibt den Fehler richtig?', 'Ein Kind rechnet: 4⁴ · 4² = 16⁶. Welcher Satz beschreibt den Fehler richtig?',
           'Ein Kind rechnet: 4⁻³ = −64. Was ist falsch?', 'Ein Kind rechnet: 2⁻³ = −8. Was ist falsch?'):
    _S('fehler_finden', _t, 2)
befunde_anwenden(DATEI, DS)
# ---- DURCHSICHT ENDE ----


# ---------- STUFEN (Zwanzigste Runde, Zweig stufen-kl6) ----------
from _stufen_kl6 import Stufen, stufen_datei  # noqa: E402

ST = Stufen('terme.potenzgesetze', 20_6_5)
Z, A, L, N, K, TB = ST.Z, ST.A, ST.L, ST.neu, ST.knobel, ST.typ_bau
B = '□/□'

lz = 'potenz_begriff'
ST.leiter(lz, 'Potenzen natürlicher Zahlen ausrechnen, Basis und Exponent benennen.', 'Potenzen von Brüchen, Dezimalzahlen und negativen Zahlen; Würfelvolumen; Basis zu einer Potenz finden.',
          'Potenzen vergleichen, Wachstum, −a² gegen (−a)², Endziffern, Würfel aus Würfeln, Fehler deuten, rückwärts über zweimal Quadrieren.')
TB(lz, 2, 'Ein Würfel hat', 'einkleidung')
TB(lz, 3, 'Welche Zahl ist größer', 'begruenden'); TB(lz, 3, 'Ein Modellwürfel', 'verknuepfen')
N(lz, Z('umkehr', 'Welche natürliche Zahl ergibt hoch 3 genau 125?', 5, '5', '5³ = 5 · 5 · 5 = 125.', 'Probiere kleine Zahlen aus.'))
N(lz, Z('fehler', 'Ein Kind rechnet 5³ = 15. Wie heißt das richtige Ergebnis?', 125, '5 ** 3', 'Es hat 5 · 3 gerechnet. Richtig: 5 · 5 · 5 = 125.', 'Was bedeutet der Exponent 3?'))
N(lz, Z('rueckwaerts', 'Eine positive Zahl wird quadriert und das Ergebnis noch einmal quadriert. Es kommt 81 heraus. Welche Zahl war es?', 3, '3', 'Zurück: 81 ist 9², und 9 ist 3². Also war die Zahl 3.', 'Welche Zahl ergibt quadriert 81?'))
K(lz, Z('knobel', 'Wie viele Quadratzahlen liegen zwischen 50 und 500?', 15, '22 - 8 + 1', 'Die kleinste ist 8² = 64, die größte 22² = 484 (23² = 529 ist zu groß). Von 8 bis 22 sind es 15 Zahlen.', 'Suche die kleinste und die größte passende Quadratzahl.'))
K(lz, Z('knobel', 'Auf welche Ziffer endet 7¹⁰⁰?', 1, '7 ** 100 % 10', 'Die Endziffern von 7¹, 7², 7³, 7⁴ sind 7, 9, 3, 1 – dann wiederholt es sich alle 4 Schritte. 100 ist durch 4 teilbar, also endet 7¹⁰⁰ wie 7⁴ auf 1.',
        'Schreibe die Endziffern von 7¹, 7², 7³, … auf.'))

lz = 'negativer_exponent'
ST.leiter(lz, 'a⁻ⁿ als Bruch schreiben, a⁰ = 1 kennen.', 'Potenzen von Brüchen mit negativem Exponenten, Brüche als Potenz schreiben, Summen, Größen aus dem Alltag.',
          'Verhältnisse, Vorzeichen, kleinste Zahl finden, Exponent bestimmen, Fehler deuten, rückwärts, Zahlen ordnen.')
TB(lz, 2, 'Schreibe 1/81', 'umkehr')
TB(lz, 3, 'Welche dieser Zahlen ist negativ', 'begruenden'); TB(lz, 3, 'Welche Zahl ist am kleinsten', 'verknuepfen')
N(lz, Z('einkleidung', 'Ein winziges Lebewesen ist 2⁻³ mm lang. Wie viele Millimeter sind das als Dezimalzahl?', 0.125, '2 ** -3', '2⁻³ = 1/2³ = 1/8 = 0,125 mm.', 'Schreibe 2⁻³ zuerst als Bruch.', einheit='mm'))
N(lz, Z('rueckwaerts', 'Von einer Zahl x wird die Potenz x⁻¹ genommen und mit 4 malgenommen. Es kommt 1/2 heraus. Wie heißt x?', 8, '4 / (1 / 2)', 'x⁻¹ · 4 = 1/2, also x⁻¹ = 1/8 und x = 8.', 'x⁻¹ ist der Kehrbruch von x.'))
N(lz, A('pruefung', 'Welche der Zahlen 2⁻¹, 2⁰, 2⁻² und (−2)⁻¹ ist am kleinsten?', '(−2)⁻¹', ['2⁻²', '2⁻¹', '2⁰'], '(−2)⁻¹ = −1/2 ist negativ. Die anderen: 1/2, 1, 1/4.', 'Schreibe alle als Bruch.'))
K(lz, L('knobel', 'Berechne 2⁻¹ + 2⁻² + 2⁻³ + 2⁻⁴ + 2⁻⁵.', B, [31, 32], ['2 ** 5 - 1', '2 ** 5'],
        'Das ist 1/2 + 1/4 + 1/8 + 1/16 + 1/32. Bis 1 fehlt immer genau der letzte Summand: Es fehlt 1/32. Also 31/32.', 'Stell dir vor, du gehst bis zur Hälfte, dann die Hälfte vom Rest, … Wie viel fehlt bis 1?'))
K(lz, Z('knobel', 'Für welche ganze Zahl n gilt 8ⁿ = 1/8?', -1, '-1', '8⁻¹ = 1/8. Also n = −1. (Andere Exponenten geben 8, 64, 1/64, …)', 'Was bedeutet ein Minus im Exponenten?'))

lz = 'mal_gleiche_basis'
ST.leiter(lz, 'Bei gleicher Basis die Exponenten addieren; die passende Regel erkennen.', 'Mit negativen Exponenten und Variablen, drei Faktoren, fehlenden Exponenten ergänzen, als Dezimalzahl.',
          'Lichtjahre, Zahl als Potenz umschreiben, Paare zählen, Fehler deuten, Aussagen prüfen, rückwärts, Zerlegen in Faktoren.')
for t in ('z³', 'y⁻³', 'a⁵', '10⁻¹', '3⁻²', 'x²', '3⁴'):
    TB(lz, 2, t, 'mehrschritt')
TB(lz, 3, 'Ergänze den Exponenten', 'umkehr', neu_s=2)
TB(lz, 3, 'Ein Lichtjahr', 'verknuepfen')
N(lz, A('erkennen', 'Welche Regel gilt bei a³ · a⁴?', 'Exponenten addieren: a⁷', ['Exponenten malnehmen: a¹²', 'Basen malnehmen: a²'], 'Gleiche Basis beim Malnehmen: Exponenten addieren, 3 + 4 = 7.', 'Schreibe a³ · a⁴ einmal ganz aus.'))
N(lz, Z('einkleidung', 'Eine Kiste enthält 10² Packungen mit je 10³ Schrauben. Es sind 10ᵏ Schrauben. Wie groß ist k?', 5, '2 + 3', '10² · 10³ = 10⁵ (100 · 1 000 = 100 000).', 'Gleiche Basis: Exponenten addieren.'))
N(lz, A('begruenden', 'Stimmt die Aussage? „2³ · 3³ kann man mit der Regel für gleiche Basen zusammenfassen.“', 'Nein, die Basen sind verschieden. Hier hilft die Regel für gleiche Exponenten: 6³.',
        ['Ja: 2³ · 3³ = 5⁶.', 'Ja: 2³ · 3³ = 6⁶.'], 'Die Regel „Exponenten addieren“ gilt nur bei gleicher Basis. Bei gleichem Exponenten werden die Basen malgenommen: 2³ · 3³ = 6³.', 'Sind die Basen gleich?'))
N(lz, Z('rueckwaerts', 'Eine Bakterienzahl verdoppelt sich jede Stunde. Nach k Stunden und dann noch 3 Stunden ist sie auf das 2⁹-fache gewachsen. Wie groß ist k?', 6, '9 - 3', '2ᵏ · 2³ = 2⁹, also k + 3 = 9, k = 6.', 'Schreibe das Wachstum als Produkt von Zweierpotenzen.'))
N(lz, Z('pruefung', 'Schreibe 8 · 16 · 32 als Zweierpotenz 2ᵉ. Wie groß ist e?', 12, '3 + 4 + 5', '8 = 2³, 16 = 2⁴, 32 = 2⁵. Zusammen 2³⁺⁴⁺⁵ = 2¹².', 'Schreibe jeden Faktor als Zweierpotenz.'))
N(lz, Z('transfer', 'Wie viele Dreierpotenzen 3ⁿ (n mindestens 1, jede höchstens 3⁵) muss man mindestens malnehmen, um 3¹² zu erhalten?', 3, '-(-12 // 5)',
        'Jeder Faktor bringt höchstens 5 zum Exponenten. Zwei Faktoren schaffen höchstens 10, drei schaffen 12 (z. B. 3⁵ · 3⁵ · 3²).', 'Wie viel kann jeder Faktor höchstens beitragen?'))
K(lz, Z('knobel', '2¹⁰ + 2¹⁰ = 2ᵏ. Wie groß ist k?', 11, '11', 'Zweimal dieselbe Zahl ist das Doppelte: 2 · 2¹⁰ = 2¹ · 2¹⁰ = 2¹¹. Also k = 11 (nicht 20!).', 'Was ist eine Zahl plus dieselbe Zahl?'))
K(lz, Z('knobel', '4⁵ · 8⁴ = 2ᵏ. Wie groß ist k?', 22, '2 * 5 + 3 * 4', '4 = 2², also 4⁵ = 2¹⁰. 8 = 2³, also 8⁴ = 2¹². Zusammen 2¹⁰ · 2¹² = 2²².', 'Schreibe 4 und 8 als Zweierpotenzen.'))

lz = 'geteilt_gleiche_basis'
ST.leiter(lz, 'Bei gleicher Basis die Exponenten subtrahieren; die passende Regel erkennen.', 'Negative Ergebnisse, Variablen, Malnehmen und Teilen gemischt, fehlenden Exponenten ergänzen, Sachsituation.',
          'Festplatte und Filme, rückwärts zum Exponenten, gemischte Basen zerlegen, Fehler deuten, Aussagen prüfen, für welche n, Speicher als Prüfungsaufgabe.')
for t in ('y⁵', 'a⁻³', '3⁴ :', 'z⁻²', '2¹ :', '2³ · 2³', '3⁵ · 3³', 'x⁸', '5³ :'):
    TB(lz, 2, t, 'mehrschritt')
TB(lz, 3, 'Eine Festplatte', 'verknuepfen'); TB(lz, 3, '2¹⁰ : 2ⁿ', 'rueckwaerts')
N(lz, A('erkennen', 'Welche Regel gilt bei a⁷ : a³?', 'Exponenten abziehen: a⁴', ['Exponenten teilen: a⁷ʹ³', 'Basen teilen: 1⁴'], 'Gleiche Basis beim Teilen: Exponenten abziehen, 7 − 3 = 4.', 'Kürze a⁷/a³ in Gedanken.'))
N(lz, Z('umkehr', 'Ergänze: 7ᵏ : 7² = 7⁵. Wie groß ist k?', 7, '5 + 2', 'k − 2 = 5, also k = 7.', 'Welcher Exponent minus 2 ergibt 5?'))
N(lz, Z('einkleidung', 'Ein Lager hat 10⁶ Schrauben. Sie werden in Kisten zu je 10² Stück verpackt. Es sind 10ᵏ Kisten. Wie groß ist k?', 4, '6 - 2', '10⁶ : 10² = 10⁴ = 10 000 Kisten.', 'Teilen bei gleicher Basis: Exponenten abziehen.'))
N(lz, A('begruenden', 'Stimmt die Aussage? „a⁵ : a⁵ = a⁰ = 0“', 'Nein: a⁵ : a⁵ = 1, also ist a⁰ = 1.', ['Ja, das stimmt.', 'Nein: a⁵ : a⁵ = a.'], 'Eine Zahl geteilt durch sich selbst ist 1. Deshalb gilt a⁰ = 1 (für a nicht 0).', 'Was ist 8 : 8?'))
N(lz, Z('parameter', 'Für wie viele natürliche Zahlen n von 1 bis 10 ist 2¹⁰ : 2ⁿ größer als 100?', 3, '3', '2¹⁰ : 2ⁿ = 2¹⁰⁻ⁿ. Größer als 100 ist das ab 2⁷ = 128, also für 10 − n ≥ 7, n = 1, 2, 3.', 'Welche Zweierpotenz ist die erste über 100?'))
N(lz, Z('pruefung', 'Ein Speicher fasst 2³⁰ Byte, eine Datei hat 2²⁰ Byte. Wie viele Dateien passen hinein? Gib die Anzahl als 2ᵉ an. Wie groß ist e?', 10, '30 - 20', '2³⁰ : 2²⁰ = 2¹⁰ = 1 024 Dateien.', 'Teile die beiden Potenzen.'))
N(lz, Z('transfer', 'Berechne 10⁴ : 10⁴ : 10⁴ · 10⁸.', 10000, '10 ** (4 - 4 - 4 + 8)', 'Von links: 10⁴ : 10⁴ = 10⁰ = 1, dann 1 : 10⁴ = 10⁻⁴, dann 10⁻⁴ · 10⁸ = 10⁴ = 10 000.', 'Rechne von links nach rechts mit den Exponenten.'))
K(lz, Z('knobel', 'Berechne (2¹⁰ − 2⁹) : 2⁸.', 2, '(2 ** 10 - 2 ** 9) // 2 ** 8', '2¹⁰ ist das Doppelte von 2⁹. Das Doppelte minus einmal ist einmal: 2¹⁰ − 2⁹ = 2⁹. Dann 2⁹ : 2⁸ = 2¹ = 2.', 'Wie viel ist 2¹⁰ − 2⁹? Denke an „das Doppelte minus einmal“.'))
K(lz, Z('knobel', 'Berechne 3¹⁰⁰ : 3⁹⁸ − 3⁰.', 8, '3 ** 2 - 1', 'Bei gleicher Basis Exponenten abziehen: 3¹⁰⁰ : 3⁹⁸ = 3¹⁰⁰⁻⁹⁸ = 3² = 9. Und 3⁰ = 1. Also 9 − 1 = 8.', 'Du musst die großen Potenzen nicht ausrechnen.'))

lz = 'gleicher_exponent'
ST.leiter(lz, 'Bei gleichem Exponenten die Basen malnehmen; das Ergebnis erkennen.', 'Geschickt rechnen mit Produkten 10, 1 oder 100, auch beim Teilen und mit Brüchen; fehlende Basis finden; Quadrat vergrößern.',
          'Drei Faktoren, Bruchbasen, Fehler deuten, Aussage „Summe“ widerlegen, rückwärts, für welche Basis, Würfel aus Würfeln, Nullen zählen.')
TB(lz, 2, 'Fasse zusammen', 'erkennen', neu_s=1)
TB(lz, 3, '36²', 'umkehr', neu_s=2); TB(lz, 3, '30²', 'umkehr', neu_s=2); TB(lz, 3, 'Welche Zahl gehört ins Kästchen? □³', 'umkehr', neu_s=2)
N(lz, Z('einkleidung', 'Ein Quadrat hat die Seitenlänge 2,5 cm. Ein zweites Quadrat hat eine 4-mal so lange Seite. Wie groß ist die Fläche des zweiten in cm²?', 100, '(2.5 * 4) ** 2', '(2,5 · 4)² = 10² = 100 cm². Geschickt: 2,5² · 4² = (2,5 · 4)².', 'Wie lang ist die Seite des zweiten Quadrats?', einheit='cm²'))
N(lz, A('begruenden', 'Stimmt die Aussage? „2³ + 5³ = 7³“', 'Nein: 8 + 125 = 133, aber 7³ = 343.', ['Ja, wie bei 2³ · 5³ = 10³.', 'Ja, gleicher Exponent heißt Basen addieren.'],
        'Die Regel für gleiche Exponenten gilt nur beim Malnehmen, nicht beim Addieren.', 'Rechne beide Seiten aus.'))
N(lz, Z('rueckwaerts', 'Eine positive Zahl wird quadriert und mit 4² malgenommen. Es kommt 400 heraus. Welche Zahl war es?', 5, '5', 'x² · 4² = (4x)² = 400 = 20². Also 4x = 20, x = 5.', 'Fasse x² · 4² zu einem Quadrat zusammen.'))
N(lz, Z('parameter', 'Für welche natürliche Zahl a gilt a³ · 5³ = 1 000 000?', 20, '100 // 5', 'a³ · 5³ = (5a)³ = 1 000 000 = 100³. Also 5a = 100, a = 20.', '1 000 000 ist eine Kubikzahl. Von welcher Zahl?'))
N(lz, Z('verknuepfen', 'Ein Würfel mit 4 cm Kantenlänge wird aus kleinen Würfeln mit 0,5 cm Kantenlänge gebaut. Wie viele kleine Würfel braucht man?', 512, '(4 / 0.5) ** 3', 'Je Kante passen 4 : 0,5 = 8 kleine Würfel. 8³ = 512.', 'Wie viele kleine Würfel liegen entlang einer Kante?'))
N(lz, Z('pruefung', 'Berechne 4⁵ · 25⁵ geschickt. Wie viele Nullen hat das Ergebnis?', 10, '10', '4⁵ · 25⁵ = (4 · 25)⁵ = 100⁵ = 10¹⁰: eine 1 mit 10 Nullen.', 'Was ergibt 4 · 25?'))
K(lz, Z('knobel', 'Welche Ziffer steht am Anfang der Zahl 2²⁰ · 5¹⁹?', 2, '2', '2²⁰ · 5¹⁹ = 2 · 2¹⁹ · 5¹⁹ = 2 · 10¹⁹. Das ist eine 2 mit 19 Nullen.', 'Nimm einen Faktor 2 heraus, damit gleiche Exponenten entstehen.'))
K(lz, Z('knobel', 'Wie viele Stellen hat die Zahl 2¹⁰ · 5⁸?', 9, '9', '2¹⁰ · 5⁸ = 2² · 2⁸ · 5⁸ = 4 · 10⁸ = 400 000 000. Das sind 9 Stellen.', 'Mache die Exponenten gleich, indem du Zweien abspaltest.'))

lz = 'anwenden'
ST.leiter(lz, 'Eine Zahl als Potenz schreiben und Exponenten addieren; die passende Regel erkennen.', 'Geschickt mit 2 · 5 = 10 rechnen, Teilen, Falten, Zahlen als Zweier- oder Zehnerpotenz darstellen.',
          'Stapelhöhe, große Potenzen vergleichen, Nullen am Ende, Fehler deuten, rückwärts zur Zahl der Faltungen, für welche n, Bevölkerungsdichte.')
TB(lz, 2, 'Ein Blatt Papier wird', 'einkleidung'); TB(lz, 2, '16 · 4', 'darstellung'); TB(lz, 2, '100²', 'darstellung')
TB(lz, 2, '10⁹ :', 'mehrschritt'); TB(lz, 2, '3⁶ :', 'mehrschritt')
TB(lz, 3, 'Was ergibt 3³', 'mehrschritt', neu_s=2); TB(lz, 3, '16 · 32', 'darstellung', neu_s=2)
TB(lz, 3, 'Ein Blatt Papier ist', 'verknuepfen'); TB(lz, 3, 'Welche Zahl ist größer', 'begruenden')
N(lz, A('erkennen', 'Welches Potenzgesetz brauchst du für 3⁴ · 3²?', 'gleiche Basis: Exponenten addieren', ['gleicher Exponent: Basen malnehmen', 'Exponenten malnehmen'], 'Die Basis 3 ist gleich, also 3⁴ · 3² = 3⁶.', 'Was ist gleich: die Basis oder der Exponent?'))
N(lz, Z('fehler', 'Ein Kind rechnet 2⁴ · 2³ = 4⁷. Wie viel ist das Ergebnis richtig als Zahl?', 128, '2 ** 7', 'Die Basis bleibt 2: 2⁴ · 2³ = 2⁷ = 128.', 'Was passiert mit der Basis?'))
N(lz, Z('rueckwaerts', 'Ein Blatt wird mehrmals in der Mitte gefaltet. Jedes Falten verdoppelt die Lagen. Am Ende liegen 128 Lagen übereinander. Wie oft wurde gefaltet?', 7, '7', '128 = 2⁷. Also wurde 7-mal gefaltet.', 'Schreibe 128 als Zweierpotenz.'))
N(lz, Z('parameter', 'Für welche natürliche Zahl n gilt 2ⁿ · 5ⁿ = 1 000 000?', 6, '6', '2ⁿ · 5ⁿ = 10ⁿ = 1 000 000 = 10⁶. Also n = 6.', 'Fasse 2ⁿ · 5ⁿ zusammen.'))
N(lz, Z('pruefung', 'Ein Land hat etwa 9 · 10⁶ Einwohner und eine Fläche von etwa 4,5 · 10⁵ km². Wie viele Einwohner kommen im Mittel auf 1 km²?', 20, '9 * 10 ** 6 / (4.5 * 10 ** 5)',
        '9 : 4,5 = 2 und 10⁶ : 10⁵ = 10. Also 2 · 10 = 20 Einwohner je km².', 'Teile die Zahlen vorne und die Zehnerpotenzen getrennt.'))
K(lz, A('knobel', 'Welche Zahl ist größer: 2¹⁰⁰ oder 10³⁰?', '2¹⁰⁰', ['10³⁰', 'Beide sind gleich groß.'],
        '2¹⁰ = 1 024 ist etwas mehr als 10³ = 1 000. 2¹⁰⁰ ist 2¹⁰ zehnmal malgenommen, 10³⁰ ist 10³ zehnmal malgenommen. Also ist 2¹⁰⁰ größer.', 'Vergleiche zuerst 2¹⁰ mit 10³.'))
K(lz, Z('knobel', 'Auf ein Schachbrett legt man auf das 1. Feld 1 Reiskorn, auf das 2. Feld 2, auf das 3. Feld 4 und so weiter, immer doppelt so viele. Auf welchem Feld liegen zum ersten Mal mehr als 1 000 Körner?', 11, '11',
        'Auf Feld n liegen 2ⁿ⁻¹ Körner. 2⁹ = 512 (Feld 10) ist noch zu wenig, 2¹⁰ = 1 024 liegt auf Feld 11.', 'Wie viele Körner liegen auf Feld n?'))

lz = 'fehler_finden'
ST.leiter(lz, 'Einfache Potenzrechnungen auf Richtigkeit prüfen; eine Potenz ausrechnen.', 'Den Fehler bei einer Regel benennen und berichtigen, auch in Sachsituationen; vom falschen Exponenten zum richtigen.',
          'Basis falsch, Exponent falsch, −4², Summe statt Produkt deuten; für welche Basis eine falsche Regel zufällig stimmt; rückwärts aus einem falschen Ergebnis.')
for t in ('Ein Kind rechnet', 'Stimmt die Rechnung'):
    TB(lz, 2, t, 'mehrschritt')
TB(lz, 3, 'Ein Kind rechnet 2³ + 2³', 'verknuepfen')
N(lz, Z('direkt', 'Rechne nach: Wie viel ist 2⁵?', 32, '2 ** 5', '2 · 2 · 2 · 2 · 2 = 32.', 'Nimm die 2 fünfmal mit sich selbst mal.'))
N(lz, Z('einkleidung', 'Ein Kind sagt: „Ein Würfel mit 3 cm Kantenlänge hat ein Volumen von 9 cm³.“ Wie groß ist das Volumen richtig?', 27, '3 ** 3', 'Volumen = 3³ = 27 cm³. Das Kind hat 3² gerechnet.', 'Volumen eines Würfels: Kante hoch 3.', einheit='cm³'))
N(lz, Z('umkehr', 'Ein Kind soll k in 2ᵏ = 32 finden und schreibt k = 16. Wie groß ist k richtig?', 5, '5', '2⁵ = 32. Das Kind hat 32 : 2 gerechnet.', 'Wie oft musst du 2 mit sich malnehmen, um 32 zu erhalten?'))
N(lz, A('parameter', 'Die Regel „a² · a³ = a⁶“ ist falsch. Für welche Zahlen a stimmt sie trotzdem?', 'für a = 0 und a = 1', ['nur für a = 2', 'für keine Zahl', 'für alle Zahlen'],
        'Richtig ist a² · a³ = a⁵. a⁵ und a⁶ sind nur für a = 0 und a = 1 gleich (0 = 0 und 1 = 1).', 'Für welche Zahlen ist jede Potenz gleich?'))
N(lz, Z('rueckwaerts', 'Ein Kind hat bei aᵏ · a² die Exponenten malgenommen und a¹² erhalten. Was wäre der richtige Exponent gewesen?', 8, '12 // 2 + 2', 'k · 2 = 12, also k = 6. Richtig: a⁶ · a² = a⁸.', 'Bestimme zuerst k.'))
K(lz, Z('knobel', 'Ein Kind schreibt 2⁵ + 2⁵ = 2¹⁰. Richtig ist 2ᵏ. Wie groß ist k?', 6, '6', '2⁵ + 2⁵ = 2 · 2⁵ = 2⁶ = 64. Das Kind hat die Exponenten addiert, als ob es malnehmen würde.', 'Was ist eine Zahl plus dieselbe Zahl?'))
K(lz, Z('knobel', 'Berechne (−2)³ + (−2)² + (−2)¹ + (−2)⁰.', -5, '(-2) ** 3 + (-2) ** 2 + (-2) + 1', '(−2)³ = −8, (−2)² = 4, (−2)¹ = −2, (−2)⁰ = 1. Zusammen: −8 + 4 − 2 + 1 = −5.', 'Achte bei jeder Potenz auf das Vorzeichen.'))

if __name__ == '__main__':
    schreibe(DATEI)
    stufen_datei('terme.potenzgesetze', ST)
