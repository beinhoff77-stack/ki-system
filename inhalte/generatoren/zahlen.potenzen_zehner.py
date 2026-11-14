#!/usr/bin/env python3
"""Thema zahlen.potenzen_zehner – Zehnerpotenzen und wissenschaftliche Schreibweise (Klasse 6)."""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _basis import *  # noqa: E402,F403

R = random.Random(19)
E = eintrag_laden('zahlen.potenzen_zehner')

ETAPPEN = [
    {'lernziel': 'zehnerpotenz', 'titel': 'Was bedeutet 10 hoch n?',
     'regel': 'Eine ⟦Zehnerpotenz⟧ ist ein Produkt aus lauter Zehnen: 10⁴ = 10 · 10 · 10 · 10. Die hochgestellte Zahl heißt ⟦Exponent⟧. Sie sagt, wie oft die 10 malgenommen wird – und wie viele ⟦Nullen⟧ hinter der 1 stehen.',
     'schritte': ['10⁵ = 10 · 10 · 10 · 10 · 10.', 'Der Exponent ist 5, also stehen 5 Nullen hinter der 1: 10⁵ = ⟦100 000⟧.'],
     'probe': '100 000 hat 5 Nullen ✓',
     'fehler': '10⁵ = 50 ist falsch: Der Exponent heißt nicht „mal 5“, sondern ⟦5-mal die 10 malnehmen⟧. 10 · 5 = 50, aber 10⁵ = 100 000.',
     'bild': {'typ': 'stellentafel', 'stellen': ['HT', 'ZT', 'T', 'H', 'Z', 'E'], 'ziffern': [1, 0, 0, 0, 0, 0], 'markiert': 0}},
    {'lernziel': 'gross_wissenschaftlich', 'titel': 'Große Zahlen kurz schreiben',
     'regel': 'Große Zahlen schreibt man kurz als ⟦a · 10ⁿ⟧. Dabei steht vor dem Komma von a ⟦genau eine Ziffer von 1 bis 9⟧. Das heißt ⟦wissenschaftliche Schreibweise⟧.',
     'schritte': ['38 000 000: Setze das Komma hinter die erste Ziffer. So entsteht 3,8.', 'Das Komma ist dabei 7 Stellen nach links gewandert. Also 38 000 000 = ⟦3,8 · 10⁷⟧.'],
     'probe': '3,8 · 10 000 000 = 38 000 000 ✓',
     'fehler': '38 000 000 = 38 · 10⁶ ist zwar richtig gerechnet, aber ⟦nicht wissenschaftlich⟧: Vor dem Komma darf nur eine Ziffer stehen. Richtig: 3,8 · 10⁷.'},
    {'lernziel': 'vorsilben_gross', 'titel': 'Kilo, Mega, Giga, Tera',
     'regel': 'Vorsilben vor Einheiten stehen für Zehnerpotenzen: ⟦Kilo (k) = 10³⟧, ⟦Mega (M) = 10⁶⟧, ⟦Giga (G) = 10⁹⟧, ⟦Tera (T) = 10¹²⟧. 5 km sind also 5 · 10³ m = 5 000 m.',
     'schritte': ['2,5 MW (Megawatt) = 2,5 · 10⁶ W.', '2,5 · 1 000 000 = 2 500 000, also 2,5 MW = ⟦2 500 000 W⟧.'],
     'probe': '2 500 000 : 1 000 000 = 2,5 ✓',
     'fehler': '3 GW = 3 000 W ist falsch: Giga heißt ⟦10⁹⟧, nicht 10³. Richtig: 3 GW = 3 000 000 000 W.'},
    {'lernziel': 'negativer_exponent', 'titel': 'Zehnerpotenzen mit Minus im Exponenten',
     'regel': 'Für Zahlen kleiner als 1 gibt es Zehnerpotenzen mit ⟦negativem Exponenten⟧: 10⁻¹ = 1/10 = 0,1; 10⁻² = 1/100 = 0,01. Bei 10⁻ⁿ steht die 1 an der ⟦n-ten Stelle nach dem Komma⟧. Außerdem gilt 10⁰ = 1.',
     'schritte': ['10⁻⁴ = 1/10⁴ = 1/10 000.', 'Die 1 steht an der 4. Stelle nach dem Komma: 10⁻⁴ = ⟦0,0001⟧.'],
     'probe': '0,0001 · 10 000 = 1 ✓',
     'fehler': '10⁻³ = −1 000 ist falsch: Ein negativer Exponent macht die Zahl ⟦nicht negativ⟧, sondern klein. 10⁻³ = 0,001.'},
    {'lernziel': 'klein_wissenschaftlich', 'titel': 'Kleine Zahlen kurz schreiben',
     'regel': 'Auch kleine Zahlen schreibt man als ⟦a · 10ⁿ⟧ mit genau einer Ziffer von 1 bis 9 vor dem Komma. Wandert das Komma nach ⟦rechts⟧, ist der Exponent ⟦negativ⟧.',
     'schritte': ['0,00047: Das Komma muss hinter die 4 wandern. So entsteht 4,7.', 'Es wandert 4 Stellen nach rechts, also 0,00047 = ⟦4,7 · 10⁻⁴⟧.'],
     'probe': '4,7 · 0,0001 = 0,00047 ✓',
     'fehler': '0,00047 = 4,7 · 10⁴ ist falsch: 4,7 · 10⁴ = 47 000 ist riesig. Bei Zahlen kleiner als 1 ist der Exponent ⟦negativ⟧: 4,7 · 10⁻⁴.'},
    {'lernziel': 'vorsilben_klein', 'titel': 'Milli, Mikro, Nano',
     'regel': 'Für kleine Größen gibt es diese Vorsilben: ⟦Milli (m) = 10⁻³⟧, ⟦Mikro (µ) = 10⁻⁶⟧, ⟦Nano (n) = 10⁻⁹⟧. 1 mm = 10⁻³ m = 0,001 m.',
     'schritte': ['5 µm (Mikrometer) = 5 · 10⁻⁶ m.', '5 · 0,000001 = 0,000005, also 5 µm = ⟦0,000005 m⟧.'],
     'probe': '0,000005 · 1 000 000 = 5, also 5 µm ✓',
     'fehler': '1 µm = 0,001 m ist falsch: Das wäre 1 mm. Mikro heißt ⟦10⁻⁶⟧: 1 µm = 0,000001 m.'},
    {'lernziel': 'vergleichen_pruefen', 'titel': 'Vergleichen und Fehler finden',
     'regel': 'Zahlen in wissenschaftlicher Schreibweise vergleichst du so: Zuerst die ⟦Exponenten⟧ – der größere Exponent gibt die größere Zahl. Nur bei gleichem Exponenten vergleichst du die ⟦Zahl vor dem Malzeichen⟧.',
     'schritte': ['Vergleiche 9 · 10⁴ und 2 · 10⁵.', 'Der Exponent 5 ist größer als 4, also ist ⟦2 · 10⁵ größer⟧ (200 000 > 90 000).'],
     'fehler': '„9 · 10⁴ ist größer als 2 · 10⁵, weil 9 > 2“ ist falsch: Zuerst entscheidet der ⟦Exponent⟧. 90 000 ist kleiner als 200 000.'},
]

MERKE = ['10ⁿ: eine 1 mit n Nullen. 10⁰ = 1.', '10⁻ⁿ: die 1 steht an der n-ten Stelle nach dem Komma.',
         'Wissenschaftliche Schreibweise: a · 10ⁿ mit 1 ≤ a < 10.',
         'k = 10³, M = 10⁶, G = 10⁹, T = 10¹²; m = 10⁻³, µ = 10⁻⁶, n = 10⁻⁹.']


def wiss(a, n):
    return f'{zt(a)} · 10{hoch(n)}'


def mantisse(R, nachkomma=None):
    k = nachkomma if nachkomma is not None else R.choice([0, 1, 1, 2])
    while True:
        m = Fr(R.randint(10 ** k, 10 ** (k + 1) - 1), 10 ** k)
        if k == 0 or (m * 10 ** k) % 10: return m


# ---------- 1 Zehnerpotenz ----------
WORTE = {3: 'Tausend', 6: 'Million', 9: 'Milliarde', 12: 'Billion'}
PLURAL = {3: 'Tausender', 6: 'Millionen', 9: 'Milliarden'}


def g_zehnerpotenz(st):
    if st == 1:
        n = R.randint(1, 9)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Schreibe 10{hoch(n)} als Zahl.'}, 'o': {'wert': 10 ** n}, 'c': f'10**{n}',
                    'w': f'10{hoch(n)} ist eine 1 mit {n} Nullen: {zt(10 ** n)}.', 'h': 'Der Exponent sagt dir, wie viele Nullen hinter der 1 stehen.'}
        return {'y': 'zahl', 'f': {'text': f'Wie viele Nullen hat die Zahl 10{hoch(n)}, wenn du sie ausschreibst?'}, 'o': {'wert': n}, 'c': f'{n}',
                'w': f'10{hoch(n)} = {zt(10 ** n)}. Das sind {n} Nullen – genauso viele, wie der Exponent angibt.', 'h': 'Schau auf die hochgestellte Zahl.'}
    if st == 2:
        n = R.randint(2, 10)
        art = R.randrange(3)
        if art == 0:
            return {'y': 'zahl', 'f': {'text': f'Schreibe {zt(10 ** n)} als Zehnerpotenz 10ⁿ. Wie groß ist der Exponent n?'}, 'o': {'wert': n}, 'c': f'{n}',
                    'w': f'{zt(10 ** n)} hat {n} Nullen, also {zt(10 ** n)} = 10{hoch(n)}.', 'h': 'Zähle die Nullen hinter der 1.'}
        if art == 1:
            r = zt(10 ** n)
            return {**wahl(R, r, [zt(10 * n), zt(10 ** (n - 1)), zt(10 ** (n + 1))]),
                    'f': {'text': f'Welche Zahl ist gleich 10{hoch(n)}?'},
                    'w': f'10{hoch(n)} ist eine 1 mit {n} Nullen: {r}. Achtung: 10 · {n} = {10 * n} ist etwas anderes.', 'h': 'Der Exponent gibt die Anzahl der Nullen an.'}
        n = R.choice(list(WORTE))
        return {'y': 'zahl', 'f': {'text': f'Eine {WORTE[n]} ist eine Zehnerpotenz 10ⁿ. Wie groß ist n?'}, 'o': {'wert': n}, 'c': f'{n}',
                'w': f'Eine {WORTE[n]} = {zt(10 ** n)} hat {n} Nullen, also 10{hoch(n)}.', 'h': 'Schreibe die Zahl mit allen Nullen auf und zähle.'}
    art = R.randrange(3)
    if art == 0:
        n = R.randint(4, 12)
        return {'y': 'zahl', 'f': {'text': f'Wie viele Tausender stecken in 10{hoch(n)}?'}, 'o': {'wert': 10 ** (n - 3)}, 'c': f'10**{n} / 10**3',
                'w': f'10{hoch(n)} : 10³ = {zt(10 ** n)} : 1 000 = {zt(10 ** (n - 3))}.', 'h': 'Teile 10ⁿ durch 1 000 = 10³. Dabei fallen drei Nullen weg.'}
    if art == 1:
        n, m = R.randint(5, 12), R.randint(1, 4)
        return {'y': 'zahl', 'f': {'text': f'Wie viel Mal so groß ist 10{hoch(n)} wie 10{hoch(m)}?'}, 'o': {'wert': 10 ** (n - m)}, 'c': f'10**{n} / 10**{m}',
                'w': f'{zt(10 ** n)} : {zt(10 ** m)} = {zt(10 ** (n - m))}. Es fallen {m} Nullen weg.', 'h': 'Teile die größere Zahl durch die kleinere. Streiche gleich viele Nullen.'}
    n = R.choice([6, 9, 12])
    m = R.choice([k for k in (3, 6, 9) if k < n])
    return {'y': 'zahl', 'f': {'text': f'Wie viele {PLURAL[m]} ergeben zusammen eine {WORTE[n]}?'},
            'o': {'wert': 10 ** (n - m)}, 'c': f'10**{n} / 10**{m}',
            'w': f'Eine {WORTE[n]} = 10{hoch(n)}, eine {WORTE[m]} = 10{hoch(m)}. 10{hoch(n)} : 10{hoch(m)} = {zt(10 ** (n - m))}.',
            'h': 'Schreibe beide Zahlen als Zehnerpotenz und teile.'}


# ---------- 2 große Zahlen wissenschaftlich ----------
FAKTEN_GROSS = [('Die Entfernung von der Erde zur Sonne beträgt etwa', Fr(15, 10), 8, 'km'),
                ('Die Entfernung von der Erde zum Mond beträgt etwa', Fr(384, 100), 5, 'km'),
                ('Auf der Erde leben etwa', Fr(8), 9, 'Menschen'),
                ('Licht legt in einer Sekunde etwa', Fr(3), 5, 'km zurück'),
                ('Der Erdumfang beträgt etwa', Fr(4), 4, 'km'),
                ('Der Durchmesser der Sonne beträgt etwa', Fr(14, 10), 6, 'km'),
                ('Ein Mensch hat etwa', Fr(1), 5, 'Kopfhaare'),
                ('Ein Jahr hat etwa', Fr(315, 100), 7, 'Sekunden')]


def g_gross(st):
    if st == 1:
        a, n = mantisse(R), R.randint(3, 9)
        z = a * 10 ** n
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Schreibe ohne Zehnerpotenz: {wiss(a, n)}'}, 'o': {'wert': wert(z)}, 'c': f'{float(a)} * 10**{n}',
                    'w': f'Komma von {zt(a)} um {n} Stellen nach rechts verschieben: {wiss(a, n)} = {zt(z)}.', 'h': 'Mal 10ⁿ heißt: Komma um n Stellen nach rechts. Fehlende Stellen mit Nullen füllen.'}
        return {'y': 'zahl', 'f': {'text': f'{zt(z)} = {zt(a)} · 10ⁿ. Wie groß ist n?'}, 'o': {'wert': n}, 'c': f'{n}',
                'w': f'Das Komma wandert von hinten bis hinter die erste Ziffer: {n} Stellen. Also {zt(z)} = {wiss(a, n)}.', 'h': 'Zähle, wie viele Stellen hinter der ersten Ziffer stehen.'}
    if st == 2:
        a, n = mantisse(R, R.choice([1, 2])), R.randint(4, 11)
        z = a * 10 ** n
        if R.random() < .6:
            r = wiss(a, n)
            return {**wahl(R, r, [f'{zt(a * 10)} · 10{hoch(n - 1)}', wiss(a, n - 1), f'{zt(a / 10)} · 10{hoch(n + 1)}', wiss(a, n + 1)]),
                    'f': {'text': f'Welche Darstellung von {zt(z)} ist die wissenschaftliche Schreibweise?'},
                    'w': f'Komma hinter die erste Ziffer: {zt(a)}. Es wandert {n} Stellen, also {r}. Bei {zt(a * 10)} · 10{hoch(n - 1)} stehen zwei Ziffern vor dem Komma.',
                    'h': 'Vor dem Komma darf nur eine Ziffer von 1 bis 9 stehen. Prüfe dann, ob der Wert stimmt.'}
        return {'y': 'zahl', 'f': {'text': f'{zt(z)} = a · 10{hoch(n)} in wissenschaftlicher Schreibweise. Wie groß ist a?'}, 'o': {'wert': wert(a)}, 'c': f'{int(z)} / 10**{n}',
                'w': f'{zt(z)} : 10{hoch(n)}: Komma um {n} Stellen nach links. a = {zt(a)}.', 'h': 'Teile durch 10ⁿ: Komma um n Stellen nach links verschieben.'}
    art = R.randrange(3)
    if art == 0:
        satz, a, n, einh = R.choice(FAKTEN_GROSS)
        z = a * 10 ** n
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'{satz} {zt(z)} {einh}. Schreibe die Zahl als a · 10ⁿ. Wie groß ist n?'}, 'o': {'wert': n}, 'c': f'{n}',
                    'w': f'{zt(z)} = {wiss(a, n)}, das Komma wandert {n} Stellen.', 'h': 'Komma hinter die erste Ziffer setzen und die Stellen zählen.'}
        return {'y': 'zahl', 'f': {'text': f'{satz} {wiss(a, n)} {einh}. Schreibe die Zahl ohne Zehnerpotenz.'}, 'o': {'wert': wert(z)}, 'c': f'{float(a)} * 10**{n}',
                'w': f'{wiss(a, n)}: Komma um {n} Stellen nach rechts, also {zt(z)}.', 'h': 'Mal 10ⁿ: Komma um n Stellen nach rechts.'}
    if art == 1:
        a, n = mantisse(R, 1), R.randint(4, 10)
        b = a * 10
        return {'y': 'zahl', 'f': {'text': f'Schreibe {zt(b)} · 10{hoch(n)} wissenschaftlich als {zt(a)} · 10ᵏ. Wie groß ist k?'}, 'o': {'wert': n + 1}, 'c': f'{n} + 1',
                'w': f'{zt(b)} = {zt(a)} · 10. Also {zt(b)} · 10{hoch(n)} = {zt(a)} · 10 · 10{hoch(n)} = {wiss(a, n + 1)}.', 'h': 'Schreibe die Zahl vor dem Malzeichen selbst als ? · 10.'}
    a, b = mantisse(R, 0), mantisse(R, 0)
    n, m = R.randint(5, 9), R.randint(2, 4)
    z = a * 10 ** n + b * 10 ** m
    return {'y': 'zahl', 'f': {'text': f'Berechne {wiss(a, n)} + {wiss(b, m)} und schreibe das Ergebnis ohne Zehnerpotenz.'}, 'o': {'wert': wert(z)}, 'c': f'{a} * 10**{n} + {b} * 10**{m}',
            'w': f'{wiss(a, n)} = {zt(a * 10 ** n)} und {wiss(b, m)} = {zt(b * 10 ** m)}. Summe: {zt(z)}.', 'h': 'Schreibe beide Zahlen erst aus, dann addiere.'}


# ---------- 3 Vorsilben groß ----------
VG = [('k', 'Kilo', 3), ('M', 'Mega', 6), ('G', 'Giga', 9), ('T', 'Tera', 12)]
EINH = [('m', 'Meter'), ('g', 'Gramm'), ('W', 'Watt'), ('Hz', 'Hertz')]


def g_vg(st):
    if st == 1:
        if R.random() < .4:
            k, name, n = R.choice(VG)
            r = f'10{hoch(n)}'
            return {**wahl(R, r, [f'10{hoch(x)}' for _, _, x in VG if x != n] + ['10²']),
                    'f': {'text': f'Für welche Zehnerpotenz steht die Vorsilbe {name} ({k})?'},
                    'w': f'{name} ({k}) bedeutet 10{hoch(n)} = {zt(10 ** n)}.', 'h': 'Kilo = 10³. Jede nächste Vorsilbe ist 1 000-mal so groß.'}
        k, name, n = R.choice(VG[:2])
        e, ename = R.choice(EINH)
        x = R.randint(2, 40)
        return {'y': 'zahl', 'f': {'text': f'Wie viele {ename} ({e}) sind {x} {k}{e}?'}, 'o': {'wert': x * 10 ** n, 'einheit': e}, 'c': f'{x} * 10**{n}',
                'w': f'{k} = 10{hoch(n)}, also {x} {k}{e} = {x} · {zt(10 ** n)} {e} = {zt(x * 10 ** n)} {e}.', 'h': f'{name} bedeutet mal {zt(10 ** n)}.'}
    if st == 2:
        k, name, n = R.choice(VG)
        e, ename = R.choice(EINH)
        a = mantisse(R, 1)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Rechne um: {zt(a)} {k}{e} = ? {e}'}, 'o': {'wert': wert(a * 10 ** n), 'einheit': e}, 'c': f'{float(a)} * 10**{n}',
                    'w': f'{zt(a)} {k}{e} = {wiss(a, n)} {e} = {zt(a * 10 ** n)} {e}.', 'h': f'{k} steht für 10{hoch(n)}. Komma um {n} Stellen nach rechts.'}
        return {'y': 'zahl', 'f': {'text': f'Rechne um: {zt(a * 10 ** n)} {e} = ? {k}{e}'}, 'o': {'wert': wert(a), 'einheit': f'{k}{e}'}, 'c': f'{int(a * 10 ** n)} / 10**{n}',
                'w': f'{zt(a * 10 ** n)} : 10{hoch(n)} = {zt(a)}, also {zt(a)} {k}{e}.', 'h': f'Teile durch 10{hoch(n)}: Komma um {n} Stellen nach links.'}
    art = R.randrange(3)
    if art == 0:
        i = R.randint(1, 3)
        k, name, n = VG[i]
        k2, _, n2 = VG[i - 1]
        e, _ = R.choice(EINH)
        a = mantisse(R, R.choice([0, 1]))
        return {'y': 'zahl', 'f': {'text': f'Rechne um: {zt(a)} {k}{e} = ? {k2}{e}'}, 'o': {'wert': wert(a * 10 ** (n - n2)), 'einheit': f'{k2}{e}'}, 'c': f'{float(a)} * 10**{n} / 10**{n2}',
                'w': f'{k} = 10{hoch(n)} und {k2} = 10{hoch(n2)}: Der Unterschied ist 10{hoch(n - n2)} = 1 000. {zt(a)} · 1 000 = {zt(a * 1000)}.',
                'h': 'Benachbarte Vorsilben unterscheiden sich um den Faktor 1 000.'}
    if art == 1:
        p = R.choice([2, 3, 4, 5, 6])
        g = R.choice([Fr(12, 10), Fr(15, 10), Fr(18, 10), Fr(24, 10), Fr(3), Fr(6)])
        anz = g * 1000 / p
        if anz.denominator != 1: return g_vg(3)
        return {'y': 'zahl', 'f': {'text': f'Ein Windrad leistet {p} MW. Wie viele solcher Windräder leisten zusammen {zt(g)} GW?'}, 'o': {'wert': int(anz)},
                'c': f'{float(g)} * 10**9 / ({p} * 10**6)',
                'w': f'{zt(g)} GW = {zt(g * 1000)} MW. {zt(g * 1000)} : {p} = {zt(anz)} Windräder.', 'h': 'Rechne zuerst GW in MW um (mal 1 000).'}
    x = R.choice([2, 5, 8, 12, 25, 40])
    return {'y': 'zahl', 'f': {'text': f'Ein Kraftwerk leistet {x * 10} MW. Wie viele Watt sind das? Schreibe die Zahl aus.'}, 'o': {'wert': x * 10 ** 7, 'einheit': 'W'}, 'c': f'{x * 10} * 10**6',
            'w': f'Mega = 10⁶, also {x * 10} MW = {x * 10} · 1 000 000 W = {zt(x * 10 ** 7)} W.', 'h': 'Mega bedeutet Million.'} if R.random() < .5 else \
        {'y': 'zahl', 'f': {'text': f'Ein Sender funkt mit {x * 100} MHz. Wie viele Hertz sind das?'}, 'o': {'wert': x * 10 ** 8, 'einheit': 'Hz'}, 'c': f'{x * 100} * 10**6',
         'w': f'{x * 100} MHz = {x * 100} · 10⁶ Hz = {zt(x * 10 ** 8)} Hz.', 'h': 'M steht für 10⁶ = 1 000 000.'}


# ---------- 4 negativer Exponent ----------
def g_neg(st):
    if st == 1:
        n = R.randint(1, 7)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Schreibe 10{hoch(-n)} als Dezimalzahl.'}, 'o': {'wert': wert(Fr(1, 10 ** n))}, 'c': f'10**-{n}',
                    'w': f'Die 1 steht an der {n}. Stelle nach dem Komma: 10{hoch(-n)} = {zt(Fr(1, 10 ** n))}.', 'h': 'Der Exponent −n heißt: Die 1 steht an der n-ten Stelle nach dem Komma.'}
        return {'y': 'luecken', 'f': {'text': f'Schreibe 10{hoch(-n)} als Bruch.', 'schablone': '1/□', 'hinweis': 'Trage den Nenner ein.'}, 'o': {'werte': [10 ** n]}, 'c': [f'1 / 10**-{n}'],
                'w': f'10{hoch(-n)} = 1/10{hoch(n)} = 1/{zt(10 ** n)}.', 'h': '10⁻ⁿ = 1/10ⁿ.'}
    if st == 2:
        n = R.randint(2, 9)
        if R.random() < .25:
            return {'y': 'zahl', 'f': {'text': f'Schreibe 10{hoch(-n)} als Dezimalzahl. Wie viele Nullen stehen nach dem Komma vor der 1?'}, 'o': {'wert': n - 1}, 'c': f'{n} - 1',
                    'w': f'10{hoch(-n)} = {zt(Fr(1, 10 ** n))}: Die 1 steht an der {n}. Stelle nach dem Komma, davor stehen {n - 1} Nullen.', 'h': 'Schreibe die Zahl aus. Die 1 selbst ist die n-te Stelle.'}
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'{zt(Fr(1, 10 ** n))} = 10ⁿ. Wie groß ist n?'}, 'o': {'wert': -n}, 'c': f'-{n}',
                    'w': f'Die 1 steht an der {n}. Stelle nach dem Komma, also {zt(Fr(1, 10 ** n))} = 10{hoch(-n)}. n = {zt(-n)}.', 'h': 'Zähle die Stellen nach dem Komma bis zur 1. Denk an das Minus.'}
        r = zt(Fr(1, 10 ** n))
        return {**wahl(R, r, [zt(-10 ** n), zt(Fr(1, 10 ** (n + 1))), zt(-n), zt(Fr(1, 10 ** (n - 1)))]),
                'f': {'text': f'Welche Zahl ist gleich 10{hoch(-n)}?'},
                'w': f'10{hoch(-n)} = 1/{zt(10 ** n)} = {r}. Die Zahl ist positiv und kleiner als 1.', 'h': 'Ein Minus im Exponenten macht die Zahl klein, nicht negativ.'}
    art = R.randrange(3)
    if art == 0:
        n = R.randint(2, 7)
        return {'y': 'zahl', 'f': {'text': f'Wie oft passt 10{hoch(-n)} in die Zahl 1?'}, 'o': {'wert': 10 ** n}, 'c': f'1 / 10**-{n}',
                'w': f'10{hoch(-n)} = 1/{zt(10 ** n)}. In 1 passt das {zt(10 ** n)}-mal.', 'h': 'Schreibe 10⁻ⁿ als Bruch.'}
    if art == 1:
        ex = R.sample(range(-7, 3), 4)
        r = f'10{hoch(min(ex))}'
        return {**wahl(R, r, [f'10{hoch(x)}' for x in sorted(ex, key=lambda x: abs(x))]),
                'f': {'text': 'Welche dieser Zahlen ist am kleinsten: ' + ', '.join(f'10{hoch(x)}' for x in ex) + '?'},
                'w': 'Ausgeschrieben: ' + ', '.join(f'10{hoch(x)} = {zt(Fr(10) ** x)}' for x in sorted(ex)) + f'. Am kleinsten ist {r}.',
                'h': 'Schreibe die Zahlen aus. Je kleiner der Exponent, desto kleiner die Zahl.'}
    n, m = R.randint(1, 3), R.randint(4, 7)
    return {'y': 'zahl', 'f': {'text': f'Wie viel Mal so groß ist 10{hoch(-n)} wie 10{hoch(-m)}?'}, 'o': {'wert': 10 ** (m - n)}, 'c': f'10**-{n} / 10**-{m}',
            'w': f'{zt(Fr(1, 10 ** n))} : {zt(Fr(1, 10 ** m))} = {zt(10 ** (m - n))}. Die 1 steht {m - n} Stellen weiter vorne.', 'h': 'Schreibe beide Zahlen als Dezimalzahl und vergleiche die Stelle der 1.'}


# ---------- 5 kleine Zahlen wissenschaftlich ----------
FAKTEN_KLEIN = [('Ein Kopfhaar ist etwa', Fr(7), -5, 'm dick'), ('Ein Blatt Papier ist etwa', Fr(1), -4, 'm dick'),
                ('Ein Bakterium ist etwa', Fr(2), -6, 'm lang'), ('Eine rote Blutzelle hat etwa', Fr(75, 10), -6, 'm Durchmesser'),
                ('Ein Staubkorn ist etwa', Fr(5), -5, 'm groß')]


def g_klein(st):
    if st == 1:
        a, n = mantisse(R, R.choice([0, 1])), R.randint(1, 5)
        z = a * Fr(1, 10 ** n)
        return {'y': 'zahl', 'f': {'text': f'Schreibe als Dezimalzahl: {wiss(a, -n)}'}, 'o': {'wert': wert(z)}, 'c': f'{float(a)} * 10**-{n}',
                'w': f'Mal 10{hoch(-n)}: Komma um {n} Stellen nach links. {wiss(a, -n)} = {zt(z)}.', 'h': 'Mal 10⁻ⁿ heißt: Komma um n Stellen nach links verschieben.'}
    if st == 2:
        a, n = mantisse(R, R.choice([0, 1, 2])), R.randint(2, 8)
        z = a * Fr(1, 10 ** n)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'{zt(z)} = {zt(a)} · 10ⁿ. Wie groß ist n?'}, 'o': {'wert': -n}, 'c': f'-{n}',
                    'w': f'Das Komma wandert {n} Stellen nach rechts bis hinter die erste Ziffer ungleich 0. Also n = {zt(-n)}.', 'h': 'Zähle die Stellen, die das Komma nach rechts wandert. Der Exponent ist negativ.'}
        r = wiss(a, -n)
        return {**wahl(R, r, [wiss(a, n), wiss(a, -n + 1), f'{zt(a * 10)} · 10{hoch(-n - 1)}', wiss(a, -n - 1)]),
                'f': {'text': f'Welche Darstellung von {zt(z)} ist die wissenschaftliche Schreibweise?'},
                'w': f'Komma hinter die erste Ziffer ungleich 0: {zt(a)}. Es wandert {n} Stellen nach rechts, also {r}.', 'h': 'Eine Ziffer vor dem Komma, und der Exponent ist negativ.'}
    art = R.randrange(2)
    if art == 0:
        satz, a, n, einh = R.choice(FAKTEN_KLEIN)
        z = a * Fr(10) ** n
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'{satz} {zt(z)} {einh}. Schreibe die Zahl als a · 10ⁿ. Wie groß ist n?'}, 'o': {'wert': n}, 'c': f'{n}',
                    'w': f'{zt(z)} = {wiss(a, n)}.', 'h': 'Komma hinter die erste Ziffer ungleich 0 setzen und die Stellen zählen.'}
        return {'y': 'zahl', 'f': {'text': f'{satz} {wiss(a, n)} {einh}. Schreibe die Zahl als Dezimalzahl.'}, 'o': {'wert': wert(z)}, 'c': f'{float(a)} * 10**{n}',
                'w': f'Komma um {-n} Stellen nach links: {zt(z)}.', 'h': 'Mal 10⁻ⁿ: Komma um n Stellen nach links.'}
    a, n = mantisse(R, 1), R.randint(2, 7)
    b = a / 10
    return {'y': 'zahl', 'f': {'text': f'Schreibe {zt(b)} · 10{hoch(-n)} wissenschaftlich als {zt(a)} · 10ᵏ. Wie groß ist k?'}, 'o': {'wert': -n - 1}, 'c': f'-{n} - 1',
            'w': f'{zt(b)} = {zt(a)} · 10⁻¹. Also {zt(b)} · 10{hoch(-n)} = {zt(a)} · 10⁻¹ · 10{hoch(-n)} = {wiss(a, -n - 1)}.', 'h': 'Schreibe die Zahl vor dem Malzeichen als ? · 10⁻¹.'}


# ---------- 6 Vorsilben klein ----------
VK = [('m', 'Milli', -3), ('µ', 'Mikro', -6), ('n', 'Nano', -9)]
EK = [('m', 'Meter'), ('g', 'Gramm'), ('s', 'Sekunden')]


def g_vk(st):
    if st == 1:
        if R.random() < .4:
            k, name, n = R.choice(VK)
            r = f'10{hoch(n)}'
            return {**wahl(R, r, [f'10{hoch(x)}' for _, _, x in VK if x != n] + [f'10{hoch(-n)}']),
                    'f': {'text': f'Für welche Zehnerpotenz steht die Vorsilbe {name} ({k})?'},
                    'w': f'{name} ({k}) bedeutet 10{hoch(n)} = {zt(Fr(10) ** n)}.', 'h': 'Milli = 10⁻³. Jede nächste Vorsilbe ist 1 000-mal so klein.'}
        e, ename = R.choice(EK)
        x = R.randint(2, 60)
        return {'y': 'zahl', 'f': {'text': f'Wie viele Milli{ename.lower()} (m{e}) sind {x} {e}?'}, 'o': {'wert': x * 1000, 'einheit': f'm{e}'}, 'c': f'{x} / 10**-3',
                'w': f'1 {e} = 1 000 m{e}, also {x} {e} = {zt(x * 1000)} m{e}.', 'h': 'Milli heißt ein Tausendstel. In 1 passen 1 000 Tausendstel.'}
    if st == 2:
        k, name, n = R.choice(VK[:2])
        e, _ = R.choice(EK)
        x = R.choice([R.randint(2, 900), R.randint(11, 99) * 10])
        if R.random() < .5:
            z = x * Fr(10) ** n
            return {'y': 'zahl', 'f': {'text': f'Rechne um: {x} {k}{e} = ? {e}'}, 'o': {'wert': wert(z), 'einheit': e}, 'c': f'{x} * 10**{n}',
                    'w': f'{k} = 10{hoch(n)}: {x} {k}{e} = {x} · {zt(Fr(10) ** n)} {e} = {zt(z)} {e}.', 'h': f'Komma um {-n} Stellen nach links.'}
        z = x * Fr(10) ** n
        return {'y': 'zahl', 'f': {'text': f'Rechne um: {zt(z)} {e} = ? {k}{e}'}, 'o': {'wert': x, 'einheit': f'{k}{e}'}, 'c': f'{float(z)} / 10**{n}',
                'w': f'{zt(z)} : 10{hoch(n)} = {zt(z)} · {zt(10 ** -n)} = {x}, also {x} {k}{e}.', 'h': f'Durch 10{hoch(n)} teilen heißt Komma um {-n} Stellen nach rechts.'}
    art = R.randrange(3)
    if art == 0:
        i = R.randint(0, 1)
        k, _, n = VK[i]
        k2, _, n2 = VK[i + 1]
        e, _ = R.choice(EK)
        a = mantisse(R, R.choice([0, 1]))
        return {'y': 'zahl', 'f': {'text': f'Rechne um: {zt(a)} {k}{e} = ? {k2}{e}'}, 'o': {'wert': wert(a * 1000), 'einheit': f'{k2}{e}'}, 'c': f'{float(a)} * 10**{n} / 10**{n2}',
                'w': f'1 {k}{e} = 1 000 {k2}{e}. {zt(a)} · 1 000 = {zt(a * 1000)} {k2}{e}.', 'h': 'Die kleinere Einheit braucht die größere Maßzahl – mal 1 000.'}
    if art == 1:
        d = R.choice([40, 50, 80, 100, 125, 200])
        return {'y': 'zahl', 'f': {'text': f'Ein Faden ist {d} µm dick. Wie viele solcher Fäden liegen nebeneinander auf 1 cm?'}, 'o': {'wert': wert(Fr(10 ** 4, d))},
                'c': f'10**-2 / ({d} * 10**-6)',
                'w': f'1 cm = 10 mm = 10 000 µm. 10 000 : {d} = {zt(Fr(10 ** 4, d))} Fäden.', 'h': 'Rechne 1 cm in µm um: 1 cm = 10 mm, 1 mm = 1 000 µm.'}
    t = R.choice([2, 4, 5, 8, 10, 20, 25])
    return {'y': 'zahl', 'f': {'text': f'Ein Rechenschritt eines Computers dauert {t} ns. Wie viele Schritte schafft er in 1 Sekunde?'}, 'o': {'wert': 10 ** 9 // t},
            'c': f'1 / ({t} * 10**-9)',
            'w': f'1 s = 10⁹ ns = 1 000 000 000 ns. {zt(10 ** 9)} : {t} = {zt(10 ** 9 // t)} Schritte.', 'h': 'Nano = 10⁻⁹. Wie viele ns hat eine Sekunde?'}


# ---------- 7 Vergleichen und prüfen (Verstehen) ----------
def g_vgl(st):
    if st == 1:
        a, b = mantisse(R, 0), mantisse(R, 0)
        n = R.randint(3, 9)
        m = n + R.choice([-2, -1, 1, 2])
        if a <= b and m < n: a, b = b, a
        if a >= b and m > n: a, b = b, a
        if a == b: b = a + 1 if a < 9 else a - 1
        x, y = wiss(a, n), wiss(b, m)
        r = x if n > m else y
        return {**wahl(R, r, [y if r == x else x, 'Beide sind gleich groß'], 3), 'f': {'text': f'Welche Zahl ist größer: {x} oder {y}?'},
                'w': f'{x} = {zt(a * 10 ** n)}, {y} = {zt(b * 10 ** m)}. Der größere Exponent entscheidet: {r}.', 'h': 'Vergleiche zuerst die Exponenten.'}
    if st == 2:
        ex = R.sample(range(-8, -1), 4)
        zs = [(mantisse(R, 1), e) for e in ex]
        r = wiss(*min(zs, key=lambda t: t[0] * Fr(10) ** t[1]))
        return {**wahl(R, r, [wiss(*t) for t in zs]),
                'f': {'text': 'Welche Zahl ist am kleinsten? ' + ' | '.join(wiss(*t) for t in zs)},
                'w': f'Bei negativen Exponenten gilt: je kleiner der Exponent (z. B. −8 < −3), desto kleiner die Zahl. Am kleinsten: {r}.',
                'h': 'Der Exponent entscheidet. −7 ist kleiner als −4.'}
    art = R.randrange(4)
    if art == 0:
        a, n = mantisse(R, 1), R.randint(2, 5)
        z = a * Fr(1, 10 ** n)
        fehlerart = R.randrange(3)
        falsch = [wiss(a, n), wiss(a, -n + 1), f'{zt(a * 10)} · 10{hoch(-n - 1)}'][fehlerart]
        r = ['Der Exponent muss negativ sein.', 'Der Exponent ist um 1 falsch.', 'Vor dem Komma darf nur eine Ziffer stehen.'][fehlerart]
        return {**wahl(R, r, [o for o in ['Der Exponent muss negativ sein.', 'Der Exponent ist um 1 falsch.', 'Vor dem Komma darf nur eine Ziffer stehen.', 'Alles ist richtig.'] if o != r]),
                'f': {'text': f'Ein Kind schreibt: {zt(z)} = {falsch}. Was ist falsch?'},
                'w': f'Richtig ist {zt(z)} = {wiss(a, -n)}. Fehler: {r}', 'h': 'Rechne die Darstellung des Kindes zurück und vergleiche mit der Zahl.'}
    if art == 1:
        a, n = mantisse(R, 1), R.randint(4, 8)
        z = a * 10 ** n
        fehlerart = R.randrange(3)
        falsch = [wiss(a, n - 1), f'{zt(a * 10)} · 10{hoch(n - 1)}', wiss(a, -n)][fehlerart]
        r = ['Der Exponent ist um 1 zu klein.', 'Vor dem Komma darf nur eine Ziffer stehen.', 'Der Exponent muss positiv sein.'][fehlerart]
        return {**wahl(R, r, [o for o in ['Der Exponent ist um 1 zu klein.', 'Vor dem Komma darf nur eine Ziffer stehen.', 'Der Exponent muss positiv sein.', 'Alles ist richtig.'] if o != r]),
                'f': {'text': f'Ein Kind schreibt: {zt(z)} = {falsch}. Was ist falsch?'},
                'w': f'Richtig ist {zt(z)} = {wiss(a, n)}. Fehler: {r}', 'h': 'Prüfe zuerst die Form (eine Ziffer vor dem Komma), dann den Wert.'}
    if art == 2:
        a, b = mantisse(R, 0), mantisse(R, 0)
        while a % b and b % a: b = mantisse(R, 0)
        if a < b: a, b = b, a
        n, m = R.randint(6, 12), R.randint(2, 5)
        return {'y': 'zahl', 'f': {'text': f'Wie viel Mal so groß ist {wiss(a, n)} wie {wiss(b, m)}?'}, 'o': {'wert': wert(a / b * 10 ** (n - m))}, 'c': f'({a} * 10**{n}) / ({b} * 10**{m})',
                'w': f'{zt(a)} : {zt(b)} = {zt(a / b)} und 10{hoch(n)} : 10{hoch(m)} = 10{hoch(n - m)}. Zusammen: {zt(a / b * 10 ** (n - m))}.',
                'h': 'Teile die Zahlen vor dem Malzeichen und die Zehnerpotenzen getrennt.'}
    n = R.randint(2, 6)
    aussagen = [
        (f'10{hoch(-n)} ist eine negative Zahl.', False, f'Nein, 10{hoch(-n)} = {zt(Fr(1, 10 ** n))} ist positiv.'),
        (f'10{hoch(-n)} ist kleiner als 1.', True, f'Ja, 10{hoch(-n)} = {zt(Fr(1, 10 ** n))} < 1.'),
        (f'10{hoch(n)} ist dasselbe wie 10 · {n}.', False, f'Nein, 10{hoch(n)} = {zt(10 ** n)}, aber 10 · {n} = {10 * n}.'),
        (f'10{hoch(n)} · 10{hoch(-n)} = 1.', True, f'Ja, {zt(10 ** n)} · {zt(Fr(1, 10 ** n))} = 1.'),
    ]
    s, stimmt, grund = R.choice(aussagen)
    gegen = ('Nein, die Aussage ist falsch.' if stimmt else 'Ja, die Aussage stimmt.')
    return {**wahl(R, grund, [gegen, 'Das kann man nicht entscheiden.'], 3), 'f': {'text': f'Stimmt die Aussage? „{s}“'},
            'w': grund, 'h': 'Schreibe die Zehnerpotenz als Zahl aus und prüfe dann.'}


GEN = {'zehnerpotenz': g_zehnerpotenz, 'gross_wissenschaftlich': g_gross, 'vorsilben_gross': g_vg, 'negativer_exponent': g_neg,
       'klein_wissenschaftlich': g_klein, 'vorsilben_klein': g_vk, 'vergleichen_pruefen': g_vgl}

DATEI = datei(E, 'Sehr große und sehr kleine Zahlen mit Zehnerpotenzen, wissenschaftlicher Schreibweise und Vorsilben darstellen.', MERKE,
              [('Große Zahlen', ['zehnerpotenz', 'gross_wissenschaftlich', 'vorsilben_gross']),
               ('Kleine Zahlen', ['negativer_exponent', 'klein_wissenschaftlich', 'vorsilben_klein']),
               ('Vergleichen und prüfen', ['vergleichen_pruefen'])],
              ETAPPEN, GEN,
              offen=['themenliste.json nennt für dieses Thema keinen lehrplan_gym-Wortlaut; Umfang nach „umfang“ gebaut. Negative Exponenten bei 10⁻ⁿ aufgenommen, weil terme.potenzgesetze (Kl. 6) sie ebenfalls verlangt.',
                     'Das Zeichen µ (Mikro) und hochgestellte Exponenten (⁻⁴) sind Unicode-Zeichen – Darstellung in der App auf dem Testgerät prüfen.'])

if __name__ == '__main__':
    schreibe(DATEI)
