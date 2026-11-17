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
     'schritte': ['Die Sonne ist rund 150 000 000 km von der Erde entfernt.', 'Setze das Komma hinter die erste Ziffer: 1,5. Das Komma ist dabei 8 Stellen nach links gewandert.',
                  'Also 150 000 000 km = ⟦1,5 · 10⁸ km⟧.'],
     'probe': '1,5 · 100 000 000 = 150 000 000 ✓',
     'fehler': '150 000 000 = 15 · 10⁷ ist zwar richtig gerechnet, aber ⟦nicht wissenschaftlich⟧: Vor dem Komma darf nur eine Ziffer von 1 bis 9 stehen. Richtig: 1,5 · 10⁸.'},
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
     'schritte': ['Ein feines Sandkorn ist etwa 0,00047 m dick.', 'Das Komma muss hinter die 4 wandern: 4,7. Es wandert 4 Stellen nach rechts.', 'Also 0,00047 m = ⟦4,7 · 10⁻⁴ m⟧.'],
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
                    'w': f'10{hoch(n)} ist eine 1 mit ' + ('1 Null' if n == 1 else f'{n} Nullen') + f': {zt(10 ** n)}.', 'h': 'Der Exponent sagt dir, wie viele Nullen hinter der 1 stehen.'}
        return {'y': 'zahl', 'f': {'text': f'Wie viele Nullen hat die Zahl 10{hoch(n)}, wenn du sie ausschreibst?'}, 'o': {'wert': n}, 'c': f'{n}',
                'w': f'10{hoch(n)} = {zt(10 ** n)}. Das ' + (f'ist 1 Null' if n == 1 else f'sind {n} Nullen') + ' – genauso viele, wie der Exponent angibt.', 'h': 'Schau auf die hochgestellte Zahl.'}
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
        wort = WORTE[n] if n == 3 else f'Eine {WORTE[n]}'
        return {'y': 'zahl', 'f': {'text': f'{wort} ist eine Zehnerpotenz 10ⁿ. Wie groß ist n?'}, 'o': {'wert': n}, 'c': f'{n}',
                'w': f'{wort} = {zt(10 ** n)} hat {n} Nullen, also 10{hoch(n)}.', 'h': 'Schreibe die Zahl mit allen Nullen auf und zähle.'}
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
                ('Auf der Erde leben etwa', Fr(81, 10), 9, 'Menschen'),
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
    if st == 2 and R.random() < .3:
        satz, a, n, einh = R.choice(FAKTEN_GROSS)
        z = a * 10 ** n
        return {'y': 'zahl', 'f': {'text': f'{satz} {zt(z)} {einh}. Schreibe die Zahl als a · 10ⁿ. Wie groß ist n?'}, 'o': {'wert': n}, 'c': f'{n}',
                'w': f'Komma hinter die erste Ziffer: {zt(a)}. Es wandert {n} Stellen nach links: {zt(z)} = {wiss(a, n)}.', 'h': 'Zähle die Stellen hinter der ersten Ziffer.'}
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


# Nur gebräuchliche Kombinationen: kW, MW, GW, TW, kHz, MHz, GHz, kB, MB, GB, TB, km, kg
ERLAUBT = {'k': [('m', 'Meter'), ('g', 'Gramm'), ('W', 'Watt'), ('Hz', 'Hertz'), ('B', 'Byte')],
           'M': [('W', 'Watt'), ('Hz', 'Hertz'), ('B', 'Byte')],
           'G': [('W', 'Watt'), ('Hz', 'Hertz'), ('B', 'Byte')],
           'T': [('W', 'Watt'), ('B', 'Byte')]}


def speicher():
    """Speicher und Daten: MB, GB (1 GB = 1 000 MB)."""
    if R.random() < .5:
        foto = R.choice([2, 4, 5, 8])
        karte = R.choice([16, 32, 64, 128, 256])
        return {'y': 'zahl', 'f': {'text': f'Ein Foto hat {foto} MB. Wie viele Fotos passen auf eine {karte}-GB-Speicherkarte? (1 GB = 1 000 MB)'},
                'o': {'wert': karte * 1000 // foto}, 'c': f'{karte} * 1000 / {foto}',
                'w': f'{karte} GB = {zt(karte * 1000)} MB. {zt(karte * 1000)} : {foto} = {zt(karte * 1000 // foto)} Fotos.', 'h': 'Rechne zuerst GB in MB um (mal 1 000).'}
    g = R.choice([Fr(15, 10), Fr(25, 10), Fr(32, 10), Fr(45, 10), Fr(7, 10), Fr(12, 10)])
    return {'y': 'zahl', 'f': {'text': f'Ein Film hat {zt(g)} GB. Wie viele MB sind das? (1 GB = 1 000 MB)'}, 'o': {'wert': wert(g * 1000), 'einheit': 'MB'}, 'c': f'{float(g)} * 1000',
            'w': f'{zt(g)} · 1 000 = {zt(g * 1000)} MB.', 'h': 'Giga ist 1 000-mal so viel wie Mega.'}


def g_vg(st):
    if st == 1:
        if R.random() < .4:
            k, name, n = R.choice(VG)
            r = f'10{hoch(n)}'
            return {**wahl(R, r, [f'10{hoch(x)}' for _, _, x in VG if x != n] + ['10²']),
                    'f': {'text': f'Für welche Zehnerpotenz steht die Vorsilbe {name} ({k})?'},
                    'w': f'{name} ({k}) bedeutet 10{hoch(n)} = {zt(10 ** n)}.', 'h': 'Kilo = 10³. Jede nächste Vorsilbe ist 1 000-mal so groß.'}
        k, name, n = R.choice(VG[:2])
        e, ename = R.choice(ERLAUBT[k])
        x = R.randint(2, 40)
        return {'y': 'zahl', 'f': {'text': f'Wie viele {ename} ({e}) sind {x} {k}{e}?'}, 'o': {'wert': x * 10 ** n, 'einheit': e}, 'c': f'{x} * 10**{n}',
                'w': f'{name} = 10{hoch(n)}, also {x} {k}{e} = {x} · {zt(10 ** n)} {e} = {zt(x * 10 ** n)} {e}.', 'h': f'{name} bedeutet mal {zt(10 ** n)}.'}
    if st == 2:
        art = R.random()
        if art < .2:
            return speicher()
        if art < .35:
            t = mantisse(R, R.choice([0, 1]))
            return {'y': 'zahl', 'f': {'text': f'Wie viele Gramm sind {zt(t)} t? (1 t = 1 000 kg = 10⁶ g)'}, 'o': {'wert': wert(t * 10 ** 6), 'einheit': 'g'}, 'c': f'{float(t)} * 10**6',
                    'w': f'1 t = 1 000 kg = 1 000 000 g. {zt(t)} · 1 000 000 = {zt(t * 10 ** 6)} g.', 'h': 'Eine Tonne sind eine Million Gramm.'}
        k, name, n = R.choice(VG)
        e, ename = R.choice(ERLAUBT[k])
        a = mantisse(R, 1)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Rechne um: {zt(a)} {k}{e} = ? {e}'}, 'o': {'wert': wert(a * 10 ** n), 'einheit': e}, 'c': f'{float(a)} * 10**{n}',
                    'w': f'{name} = 10{hoch(n)}: {zt(a)} {k}{e} = {wiss(a, n)} {e} = {zt(a * 10 ** n)} {e}.', 'h': f'{k} steht für 10{hoch(n)}. Komma um {n} Stellen nach rechts.'}
        return {'y': 'zahl', 'f': {'text': f'Rechne um: {zt(a * 10 ** n)} {e} = ? {k}{e}'}, 'o': {'wert': wert(a), 'einheit': f'{k}{e}'}, 'c': f'{int(a * 10 ** n)} / 10**{n}',
                'w': f'{name} = 10{hoch(n)}: {zt(a * 10 ** n)} : 10{hoch(n)} = {zt(a)}, also {zt(a)} {k}{e}.', 'h': f'Teile durch 10{hoch(n)}: Komma um {n} Stellen nach links.'}
    art = R.randrange(4)
    if art == 3:
        return speicher()
    if art == 0:
        i = R.randint(1, 3)
        k, name, n = VG[i]
        k2, _, n2 = VG[i - 1]
        e, _ = R.choice([x for x in ERLAUBT[k] if x in ERLAUBT[k2]])
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
                'w': f'Mal 10{hoch(-n)}: Komma um ' + ('1 Stelle' if n == 1 else f'{n} Stellen') + f' nach links. {wiss(a, -n)} = {zt(z)}.', 'h': 'Mal 10⁻ⁿ heißt: Komma um n Stellen nach links verschieben.'}
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
    art = R.randrange(3)
    if art == 2:
        ding, a, n, ziel, ziel_m = R.choice([('Ein Bakterium ist', 2, -6, '1 mm', Fr(1, 1000)), ('Ein Haar ist', 8, -5, '1 cm', Fr(1, 100)),
                                             ('Ein Bakterium ist', 5, -6, '1 mm', Fr(1, 1000)), ('Ein Blatt Papier ist', 1, -4, '1 cm', Fr(1, 100)),
                                             ('Ein Haar ist', 5, -5, '1 cm', Fr(1, 100)), ('Ein Sandkorn ist', 4, -4, '1 dm', Fr(1, 10))])
        groesse = a * Fr(10) ** n
        anz = ziel_m / groesse
        wort = {'Ein Bakterium ist': ('lang', 'Bakterien hintereinander'), 'Ein Haar ist': ('dick', 'Haare nebeneinander'),
                'Ein Blatt Papier ist': ('dick', 'Blätter übereinander'), 'Ein Sandkorn ist': ('dick', 'Sandkörner nebeneinander')}[ding]
        return {'y': 'zahl', 'f': {'text': f'{ding} {wiss(a, n)} m {wort[0]}. Wie viele {wort[1]} ergeben {ziel}?'}, 'o': {'wert': wert(anz)},
                'c': f'{float(ziel_m)} / ({a} * 10**({n}))',
                'w': f'{ziel} = {zt(ziel_m)} m, eins ist {zt(groesse)} m. {zt(ziel_m)} : {zt(groesse)} = {zt(anz)}.',
                'h': f'Schreibe beide Längen in Meter als Dezimalzahl und teile.'}
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
                    'w': f'{name} bedeutet 10{hoch(n)} = {zt(Fr(10) ** n)}: {x} {k}{e} = {x} · {zt(Fr(10) ** n)} {e} = {zt(z)} {e}.', 'h': f'Komma um {-n} Stellen nach links.'}
        z = x * Fr(10) ** n
        return {'y': 'zahl', 'f': {'text': f'Rechne um: {zt(z)} {e} = ? {k}{e}'}, 'o': {'wert': x, 'einheit': f'{k}{e}'}, 'c': f'{float(z)} / 10**{n}',
                'w': f'{name} bedeutet 10{hoch(n)}: {zt(z)} : 10{hoch(n)} = {zt(z)} · {zt(10 ** -n)} = {x}, also {x} {k}{e}.', 'h': f'Durch 10{hoch(n)} teilen heißt Komma um {-n} Stellen nach rechts.'}
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
def gleicher_exponent():
    """Gleicher Exponent: Vorzahl vergleichen – oder Falle: kleinere Vorzahl, aber größerer Exponent."""
    if R.random() < .5:
        n = R.choice([R.randint(3, 9), -R.randint(2, 8)])
        a, b = mantisse(R, 1), mantisse(R, 1)
        if a == b: return gleicher_exponent()
        x, y = wiss(a, n), wiss(b, n)
        r = x if a > b else y
        return {**wahl(R, r, [y if r == x else x, 'Beide sind gleich groß'], 3), 'f': {'text': f'Welche Zahl ist größer: {x} oder {y}?'},
                'w': f'Gleicher Exponent {zt(n)}: Dann entscheidet die Zahl vor dem Malzeichen. {zt(max(a, b))} > {zt(min(a, b))}, also ist {r} größer.',
                'h': 'Die Exponenten sind gleich. Vergleiche die Zahlen vor dem Malzeichen.'}
    n = -R.randint(2, 6) if R.random() < .5 else R.randint(3, 8)
    a, b = Fr(R.randint(51, 99), 10), Fr(R.randint(10, 49), 10)
    x, y = wiss(a, n), wiss(b, n + 1)
    return {**wahl(R, y, [x, 'Beide sind gleich groß'], 3), 'f': {'text': f'Welche Zahl ist größer: {x} oder {y}?'},
            'w': f'{x} = {zt(a * Fr(10) ** n)}, {y} = {zt(b * Fr(10) ** (n + 1))}. Der Exponent {zt(n + 1)} ist größer als {zt(n)}, darum ist {y} größer, obwohl {zt(b)} < {zt(a)}.',
            'h': 'Zuerst die Exponenten vergleichen. Erst bei gleichem Exponenten zählt die Zahl vor dem Malzeichen.'}


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
                'w': f'Bei negativen Exponenten gilt: je kleiner der Exponent (hier {zt(min(ex))} < {zt(max(ex))}), desto kleiner die Zahl. Am kleinsten: {r}.',
                'h': f'Der Exponent entscheidet. {zt(min(ex))} ist kleiner als {zt(max(ex))}.'}
    art = R.randrange(5)
    if art == 4:
        return gleicher_exponent()
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

# ---------- KARTEN: Lernkarten nach dem neuen Muster (Achte Runde, Vorgabe 16.11., Paket U6) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl6.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl6 import umbau  # noqa: E402

KARTEN = {
 'zehnerpotenz': {
  'einstieg': 'In große Stadien passen 100 000 Menschen. Beim Lesen musst du die Nullen zählen. Kürzer ist: fünfmal die 10 malgenommen, eine ⟦Zehnerpotenz⟧.',
  'woerter': [['Zehnerpotenz', 'lauter Zehnen malgenommen, z. B. 10⁵'],
              ['10⁵', 'gelesen „zehn hoch fünf“'],
              ['Exponent', 'die kleine Zahl oben: wie oft die 10 malgenommen wird']],
  'bild': {'typ': 'stellentafel', 'stellen': ['HT', 'ZT', 'T', 'H', 'Z', 'E'], 'ziffern': ['', '', '', '', '', 1]},
  'schritte': [{'text': '10⁵ heißt 10 · 10 · 10 · 10 · 10. Der Exponent ist 5.'},
               {'text': 'Jedes Mal mit 10 rückt die 1 eine Stelle nach links.', 'bild': {'ziffern': ['', '', '', 1, 0, 0]}},
               {'text': 'Nach 5 Schritten: 10⁵ = ⟦100 000⟧, eine 1 mit 5 Nullen.', 'bild': {'ziffern': [1, 0, 0, 0, 0, 0], 'markiert': 0}}],
  'fehler': '10⁵ = 50 ist falsch: 50 Menschen passen in einen Bus. 10⁵ = 100 000 füllen ein Stadion.',
  'regel': 'Der ⟦Exponent⟧ sagt, wie viele Nullen hinter der 1 stehen. So ist 10⁵ = 100 000.'},
 'gross_wissenschaftlich': {
  'einstieg': 'Die Sonne ist rund 150 000 000 km von der Erde entfernt. Mit so vielen Nullen verzählt man sich leicht. Kürzer ist die ⟦wissenschaftliche Schreibweise⟧.',
  'woerter': [['wissenschaftliche Schreibweise', 'eine Zahl als a · 10ⁿ, mit genau einer Ziffer von 1 bis 9 vor dem Komma']],
  'bild': {'typ': 'tabelle', 'kopf': ['Schreibweise', 'Abstand'], 'zeilen': [['normal', '150 000 000 km']]},
  'schritte': [{'text': 'Setze das Komma hinter die erste Ziffer: 1,5.'},
               {'text': 'Das Komma ist dabei 8 Stellen nach links gewandert.'},
               {'text': 'Also 150 000 000 km = ⟦1,5 · 10⁸ km⟧.',
                'bild': {'zeilen': [['normal', '150 000 000 km'], ['wissenschaftlich', '1,5 · 10⁸ km']]}}],
  'fehler': '15 · 10⁷ stimmt zwar, ist aber nicht wissenschaftlich. Vor dem Komma darf nur eine Ziffer stehen.',
  'regel': 'Komma hinter die ⟦erste Ziffer⟧, Stellen zählen: Das ist der Exponent. Vor dem Komma steht genau eine Ziffer von 1 bis 9.'},
 'vorsilben_gross': {
  'einstieg': 'Ein Windrad leistet etwa 2,5 Megawatt. „Mega“ heißt „mal eine Million“, so wie „Kilo“ „mal tausend“ heißt. Solche Wortteile heißen ⟦Vorsilben⟧.',
  'woerter': [['Vorsilbe', 'ein Wortteil vor der Einheit, der für eine Zehnerpotenz steht'],
              ['Mega (M)', '10⁶ = eine Million'],
              ['Watt (W)', 'Einheit für Leistung, z. B. bei Lampen und Kraftwerken']],
  'bild': {'typ': 'tabelle', 'kopf': ['Vorsilbe', 'k', 'M', 'G', 'T'], 'zeilen': [['Faktor', '10³', '10⁶', '10⁹', '10¹²']]},
  'schritte': [{'text': 'Mega bedeutet 10⁶: 2,5 MW = 2,5 · 10⁶ Watt.'},
               {'text': 'Mal eine Million heißt: Komma 6 Stellen nach rechts.'},
               {'text': 'Das Windrad leistet ⟦2 500 000 W⟧.'}],
  'fehler': '3 GW = 3 000 W ist falsch. Das schafft schon ein Wasserkocher, kein Kraftwerk. Giga heißt 10⁹.',
  'regel': 'Ersetze die ⟦Vorsilbe⟧ durch ihre Zehnerpotenz. k = 10³, M = 10⁶, G = 10⁹, T = 10¹².'},
 'negativer_exponent': {
  'einstieg': 'Teilst du einen Meter durch 10, hast du 0,1 m. Noch einmal geteilt: 0,01 m, dann 0,001 m. Hochzahlen unter null heißen ⟦negative Exponenten⟧.',
  'woerter': [['negative Exponenten', 'Hochzahlen mit Minus, z. B. 10⁻⁴'],
              ['10⁰', 'gelesen „zehn hoch null“; das ergibt 1']],
  'bild': {'typ': 'tabelle', 'kopf': ['Potenz', '10¹', '10⁰', '10⁻¹', '10⁻²', '10⁻³', '10⁻⁴'], 'zeilen': [['Wert', '10', '', '', '', '', '']]},
  'schritte': [{'text': 'Von 10¹ = 10 geht es durch 10 zu 10⁰ = 1.', 'bild': {'zeilen': [['Wert', '10', '1', '', '', '', '']]}},
               {'text': 'Weiter durch 10: 0,1, dann 0,01, dann 0,001.', 'bild': {'zeilen': [['Wert', '10', '1', '0,1', '0,01', '0,001', '']]}},
               {'text': 'Bei 10⁻⁴ steht die 1 an der 4. Stelle nach dem Komma: ⟦0,0001⟧.',
                'bild': {'zeilen': [['Wert', '10', '1', '0,1', '0,01', '0,001', '0,0001']]}}],
  'fehler': '10⁻³ = −1 000 ist falsch. Ein Millimeter ist winzig, aber nicht unter null. 10⁻³ = 0,001.',
  'regel': 'Bei ⟦10⁻ⁿ⟧ steht die 1 an der n-ten Stelle nach dem Komma. Die Zahl ist klein, nicht negativ.'},
 'klein_wissenschaftlich': {
  'einstieg': 'Ein feines Sandkorn ist etwa 0,00047 m dick. Auch so kleine Zahlen schreibt man kurz in ⟦wissenschaftlicher Schreibweise⟧. Der Exponent ist dann negativ.',
  'woerter': [['erste Ziffer ungleich 0', 'die erste Ziffer, die keine Null ist, hier die 4']],
  'bild': {'typ': 'tabelle', 'kopf': ['Schreibweise', 'Dicke'], 'zeilen': [['normal', '0,00047 m']]},
  'schritte': [{'text': 'Das Komma kommt hinter die erste Ziffer ungleich 0: 4,7.'},
               {'text': 'Es wandert dabei 4 Stellen nach rechts.'},
               {'text': 'Also 0,00047 m = ⟦4,7 · 10⁻⁴ m⟧.',
                'bild': {'zeilen': [['normal', '0,00047 m'], ['wissenschaftlich', '4,7 · 10⁻⁴ m']]}}],
  'fehler': '4,7 · 10⁴ m wären 47 km. So dick ist kein Sandkorn! Bei Zahlen unter 1 ist der Exponent negativ.',
  'regel': 'Wandert das Komma ⟦nach rechts⟧, ist der Exponent negativ. Vor dem Komma steht genau eine Ziffer von 1 bis 9.'},
 'vorsilben_klein': {
  'einstieg': 'Ein Spinnenfaden ist nur etwa 5 µm dick. Das µ heißt „Mikro“ und bedeutet ein Millionstel. Für kleine Größen gibt es solche ⟦Vorsilben⟧.',
  'woerter': [['Mikro (µ)', '10⁻⁶ = ein Millionstel'],
              ['Milli (m)', '10⁻³ = ein Tausendstel'],
              ['Nano (n)', '10⁻⁹ = ein Milliardstel']],
  'bild': {'typ': 'tabelle', 'kopf': ['Vorsilbe', 'm', 'µ', 'n'], 'zeilen': [['Faktor', '10⁻³', '10⁻⁶', '10⁻⁹']]},
  'schritte': [{'text': 'Mikro bedeutet 10⁻⁶: 5 µm = 5 · 10⁻⁶ m.'},
               {'text': 'Mal 10⁻⁶ heißt: Komma 6 Stellen nach links.'},
               {'text': 'Der Faden ist ⟦0,000005 m⟧ dick.'},
               {'text': 'Genauso ist Milli 10⁻³ und Nano 10⁻⁹.'}],
  'fehler': '1 µm = 0,001 m ist falsch: Das wäre ein ganzer Millimeter. Mikro heißt 10⁻⁶ = 0,000001.',
  'regel': 'Ersetze die ⟦Vorsilbe⟧ durch ihre Zehnerpotenz und verschiebe das Komma nach links. m = 10⁻³, µ = 10⁻⁶, n = 10⁻⁹.'},
 'vergleichen_pruefen': {
  'einstieg': 'Eine Stadt hat 9 · 10⁴ Einwohner, eine andere 2 · 10⁵. Wer nur auf 9 und 2 schaut, liegt falsch. Beim ⟦Vergleichen⟧ zählt zuerst der Exponent.',
  'woerter': [['Vergleichen', 'herausfinden, welche Zahl größer ist']],
  'bild': {'typ': 'tabelle', 'kopf': ['Stadt', 'Einwohner'], 'zeilen': [['A', '9 · 10⁴'], ['B', '2 · 10⁵']]},
  'schritte': [{'text': 'Vergleiche zuerst die Exponenten: 4 und 5.'},
               {'text': '5 ist größer. Also ist ⟦2 · 10⁵ größer⟧.'},
               {'text': 'Kontrolle: 90 000 gegen 200 000 Einwohner.',
                'bild': {'typ': 'saeulen', 'einheit': 'Einwohner', 'werte': [{'name': 'A', 'wert': 90000}, {'name': 'B', 'wert': 200000}], 'zahlen': True}}],
  'fehler': '„9 · 10⁴ ist größer, weil 9 > 2“ ist falsch. Die erste Stadt hat nur 90 000 Einwohner.',
  'regel': 'Zuerst vergleichst du den ⟦Exponenten⟧. Nur bei gleichem Exponenten zählt die Zahl davor.'},
}

umbau(DATEI, KARTEN)



# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl6): je Lernkarte 2 Übungen Stufe 2 + 4 Übungen Stufe 3 ----------
# Läuft nach allen bisherigen Aufgaben mit eigenem Zufallsstart; die bisherigen Aufgaben bleiben unverändert.
# Prüfungsvorbilder: Bayerischer Mathematik-Test Jgst. 8 (ISB) 2021 Aufg. 6b (Stapelhöhe aus Anzahl · Dicke, Einheit wechseln),
# 2023 Aufg. 6 (Restmenge bei Milliarden), 2024 Aufg. 1b (Zahl so ersetzen, dass das Ergebnis stimmt); Wettbewerbs-Knobeleien eigene.
from _schwer_kl6 import ergaenzen, zahl, wahl  # noqa: E402


def _zp():
    return {
        'zehnerpotenz': [
            (2, lambda R: zahl('Eine Zehnerpotenz 10ⁿ hat ausgeschrieben 9 Stellen. Wie groß ist n?', 8, '9 - 1',
                               'Die 1 ist auch eine Stelle. Wie viele Nullen bleiben?',
                               '9 Stellen: eine 1 und 8 Nullen. Also 10⁸ und n = 8.')),
            (2, lambda R: wahl(R, 'Welche Zahl liegt zwischen 10⁴ und 10⁵?', '35 000', ['3 500', '350 000', '3 500 000'],
                               'Schreibe 10⁴ und 10⁵ aus und vergleiche die Stellenzahl.',
                               '10⁴ = 10 000 und 10⁵ = 100 000. Dazwischen liegt 35 000.')),
            (3, lambda R: zahl('In einer Kiste liegen 10 Schachteln, in jeder Schachtel 10 Päckchen, in jedem Päckchen 1 000 Perlen. '
                               'Wie viele Perlen sind in 100 Kisten? Gib das Ergebnis als 10ⁿ an. Wie groß ist n?', 7, '2 + 1 + 1 + 3',
                               'Schreibe jede Anzahl als Zehnerpotenz und zähle alle Nullen zusammen.',
                               '100 · 10 · 10 · 1 000 = 10 000 000 = 10⁷. Die Nullen: 2 + 1 + 1 + 3 = 7, also n = 7.')),
            (3, lambda R: wahl(R, 'Lena rechnet: 10³ = 30, denn 10 · 3 = 30. Was stimmt?',
                               'Falsch: 10³ = 10 · 10 · 10 = 1 000.',
                               ['Richtig, 10³ = 30.', 'Falsch: 10³ = 10 + 10 + 10 = 30.', 'Falsch: 10³ = 3 · 3 · 3 · … = 300.'],
                               'Der Exponent sagt, wie oft die 10 als Faktor vorkommt.',
                               '10³ heißt: dreimal die 10 als Faktor, 10 · 10 · 10 = 1 000. Lena hat 10 mit 3 malgenommen.')),
            (3, lambda R: zahl('Eine Zehnerpotenz 10ⁿ ist größer als eine Million, aber kleiner als eine Milliarde. '
                               'Wie viele verschiedene Zahlen n sind möglich?', 2, '(9 - 6) - 1',
                               'Eine Million ist 10⁶, eine Milliarde ist 10⁹. Welche Exponenten liegen echt dazwischen?',
                               'Million = 10⁶, Milliarde = 10⁹. Echt dazwischen liegen nur 10⁷ und 10⁸. Also 2 Möglichkeiten.')),
            (3, lambda R: zahl('Ein Zahlenschloss hat 6 Rädchen mit den Ziffern 0 bis 9. Wie viele verschiedene Codes gibt es? '
                               'Schreibe das Ergebnis als 10ⁿ. Wie groß ist n?', 6, '6',
                               'Für jedes Rädchen gibt es 10 Möglichkeiten. Wie oft nimmst du 10 mal?',
                               'Jedes der 6 Rädchen hat 10 Ziffern: 10 · 10 · 10 · 10 · 10 · 10 = 10⁶ = 1 000 000 Codes, also n = 6.')),
        ],
        'gross_wissenschaftlich': [
            (2, lambda R: wahl(R, 'Alle vier Angaben haben denselben Wert. Welche ist in wissenschaftlicher Schreibweise?', '1,25 · 10⁴',
                               ['12,5 · 10³', '0,125 · 10⁵', '125 · 10²'],
                               'Vor dem Komma muss genau eine Ziffer von 1 bis 9 stehen.',
                               'Nur bei 1,25 · 10⁴ steht vor dem Komma genau eine Ziffer (1). Alle anderen haben 0 oder zwei oder drei Ziffern vor dem Komma.')),
            (2, lambda R: zahl('Die Sonne ist etwa 150 Millionen km von der Erde entfernt. Schreibe die Zahl als a · 10ⁿ km. Wie groß ist n?', 8,
                               '6 + 2', 'Schreibe 150 Millionen zuerst ganz aus: 150 000 000.',
                               '150 Millionen = 150 000 000 = 1,5 · 10⁸. Das Komma wandert 8 Stellen, also n = 8 (nicht 6).')),
            (3, lambda R: zahl('Ein Papierstapel hat 2,5 Millionen Blätter. Jedes Blatt ist 0,1 mm dick. Wie hoch ist der Stapel in Metern?', 250,
                               '2500000 * 0.1 / 1000', 'Rechne zuerst die Höhe in mm aus, dann in m um (1 m = 1 000 mm).',
                               '2 500 000 · 0,1 mm = 250 000 mm. 250 000 mm : 1 000 = 250 m.', einheit='m')),
            (3, lambda R: zahl('In einem Becken sind 3 · 10⁹ Keime. Eine Anlage entfernt so viele, dass nur ein Hundertstel übrig bleibt. '
                               'Wie viele Keime bleiben? Schreibe das Ergebnis als a · 10ⁿ. Wie groß ist n?', 7, '9 - 2',
                               'Ein Hundertstel heißt: durch 100 teilen. Wie ändert sich der Exponent?',
                               '3 · 10⁹ : 100 = 3 · 10⁹ : 10² = 3 · 10⁷. Es bleiben 30 Millionen Keime, n = 7.')),
            (3, lambda R: zahl('Die Zahl 4,5 · 10ⁿ hat ausgeschrieben genau 11 Stellen. Wie groß ist n?', 10, '11 - 1',
                               'Probiere klein: 4,5 · 10¹ = 45 hat 2 Stellen. Wie hängen Stellen und n zusammen?',
                               '4,5 · 10ⁿ hat immer n + 1 Stellen (45 hat 2 Stellen bei n = 1). 11 Stellen heißt n = 10.')),
            (3, lambda R: wahl(R, 'Tom rechnet: 3 · 10⁴ + 5 · 10⁴ = 8 · 10⁸. Was ist richtig?',
                               '8 · 10⁴, denn 3 Zehntausender und 5 Zehntausender sind 8 Zehntausender.',
                               ['Tom hat recht: 8 · 10⁸.', '15 · 10⁴, denn 3 · 5 = 15.', '8 · 10¹⁶, denn 4 · 4 = 16.'],
                               'Schreibe beide Zahlen aus: 30 000 + 50 000.',
                               '30 000 + 50 000 = 80 000 = 8 · 10⁴. Beim Addieren bleibt die Zehnerpotenz gleich.')),
        ],
        'vorsilben_gross': [
            (2, lambda R: zahl('Rechne um: 0,45 GW = ? MW', 450, '0.45 * 1000',
                               'Giga ist 10⁹, Mega ist 10⁶. Ein GW sind also 1 000 MW.', '0,45 GW = 0,45 · 1 000 MW = 450 MW.', einheit='MW')),
            (2, lambda R: wahl(R, 'Welche Leistung ist am größten?', '0,3 GW', ['3 500 kW', '45 MW', '2 000 000 W'],
                               'Rechne alle Angaben in MW um.',
                               '0,3 GW = 300 MW; 3 500 kW = 3,5 MW; 45 MW; 2 000 000 W = 2 MW. Am größten ist 0,3 GW.')),
            (3, lambda R: zahl('Ein Spiel ist 60 GB groß. Der Download schafft 25 MB pro Sekunde. Wie viele Minuten dauert der Download? (1 GB = 1 000 MB)', 40,
                               '60 * 1000 / 25 / 60', 'Rechne GB in MB um, teile durch 25 MB pro Sekunde und rechne die Sekunden in Minuten um.',
                               '60 GB = 60 000 MB. 60 000 : 25 = 2 400 s. 2 400 s : 60 = 40 min.', einheit='min')),
            (3, lambda R: zahl('Eine Solaranlage liefert im Jahr 8 MWh Strom. Ein Haushalt braucht im Jahr 3 200 kWh. '
                               'Für wie viele Haushalte reicht der Strom vollständig?', 2, '(8 * 1000) // 3200',
                               'Rechne MWh in kWh um. Achtung: Nur ganze Haushalte zählen.',
                               '8 MWh = 8 000 kWh. 8 000 : 3 200 = 2,5. Für den dritten Haushalt reicht es nicht, also 2 Haushalte.')),
            (3, lambda R: zahl('Wie viele Kilobyte (kB) sind ein Terabyte (TB)? Schreibe das Ergebnis als 10ⁿ. Wie groß ist n?', 9, '12 - 3',
                               'Tera = 10¹², Kilo = 10³. Wie oft passt 10³ in 10¹²?',
                               '1 TB = 10¹² B, 1 kB = 10³ B. 10¹² : 10³ = 10⁹, also n = 9.')),
            (3, lambda R: wahl(R, 'Mia rechnet: 2,5 MW = 2 500 W. Was stimmt?', 'Falsch: Mega heißt 10⁶, also 2,5 MW = 2 500 000 W.',
                               ['Richtig.', 'Falsch: Mega heißt 10⁹, also 2 500 000 000 W.', 'Falsch: Man muss teilen, 2,5 MW = 0,0025 W.'],
                               'Welche Zehnerpotenz steht für M? Mia hat mit Kilo gerechnet.',
                               'M = 10⁶. 2,5 · 1 000 000 W = 2 500 000 W. Mia hat nur mit 1 000 (Kilo) malgenommen.')),
        ],
        'negativer_exponent': [
            (2, lambda R: wahl(R, 'Welche Zehnerpotenz ist gleich dem Bruch 1/1 000?', '10⁻³', ['10³', '−10³', '10⁻⁴'],
                               '1/1 000 = 0,001. Wie viele Stellen nach dem Komma?', '1/1 000 = 0,001 = 10⁻³ (die 1 steht an der 3. Stelle nach dem Komma).')),
            (2, lambda R: wahl(R, 'Welche Zahl liegt zwischen 10⁻³ und 10⁻²?', '0,005', ['0,0005', '0,05', '0,5'],
                               'Schreibe 10⁻³ und 10⁻² als Dezimalzahl.', '10⁻³ = 0,001 und 10⁻² = 0,01. Dazwischen liegt 0,005.')),
            (3, lambda R: zahl('Wie viel Mal so groß ist 10² wie 10⁻²?', 10000, '100 / (1/100)',
                               'Schreibe beide Zahlen aus: 100 und 0,01.', '10² = 100, 10⁻² = 0,01. 100 : 0,01 = 10 000. 100 ist 10 000-mal so groß.')),
            (3, lambda R: zahl('Die Zahl 10⁻ⁿ hat nach dem Komma genau 6 Nullen und dann die 1. Wie groß ist n?', 7, '6 + 1',
                               'Probiere klein: 10⁻² = 0,01 hat eine Null nach dem Komma.',
                               '0,0000001: Die 1 steht an der 7. Stelle nach dem Komma. Also 10⁻⁷, n = 7 (nicht 6).')),
            (3, lambda R: wahl(R, 'Ben sagt: „10⁻⁴ ist größer als 10⁻², weil 4 größer ist als 2.“ Was stimmt?',
                               'Falsch: 10⁻⁴ = 0,0001 ist kleiner als 10⁻² = 0,01.',
                               ['Ben hat recht.', 'Falsch: Beide Zahlen sind gleich groß.', 'Falsch: 10⁻⁴ ist eine negative Zahl.'],
                               'Schreibe beide Zahlen als Dezimalzahl.',
                               '10⁻⁴ = 0,0001 und 10⁻² = 0,01. Je weiter rechts die 1 steht, desto kleiner die Zahl. Ben irrt.')),
            (3, lambda R: zahl('Welchen Exponenten n musst du einsetzen, damit 0,01 · 10ⁿ = 1 000 gilt?', 5, '2 + 3',
                               'Mit welcher Zahl musst du 0,01 malnehmen, um 1 000 zu erhalten?',
                               '0,01 · 100 = 1 und 1 · 1 000 = 1 000. Zusammen 100 · 1 000 = 100 000 = 10⁵, also n = 5.')),
        ],
        'klein_wissenschaftlich': [
            (2, lambda R: zahl('Schreibe 0,000307 in wissenschaftlicher Schreibweise a · 10ⁿ. Wie groß ist a?', Fr('3.07'), '307 / 100',
                               'Verschiebe das Komma, bis genau eine Ziffer von 1 bis 9 davor steht.',
                               '0,000307 = 3,07 · 10⁻⁴. Also a = 3,07.')),
            (2, lambda R: zahl('Wie viele Nullen stehen direkt nach dem Komma, wenn du 4,2 · 10⁻⁶ ausschreibst?', 5, '6 - 1',
                               'Die erste Ziffer 4 steht an der 6. Stelle nach dem Komma.', '4,2 · 10⁻⁶ = 0,0000042. Vor der 4 stehen 5 Nullen nach dem Komma.')),
            (3, lambda R: zahl('Alufolie ist 1,5 · 10⁻⁵ m dick. Wie viele Lagen übereinander ergeben 3 mm?', 200, '(3/1000) / (15/1000000)',
                               'Rechne beide Längen in dieselbe Einheit um: 1,5 · 10⁻⁵ m = 0,015 mm.',
                               '1,5 · 10⁻⁵ m = 0,000015 m = 0,015 mm. 3 mm : 0,015 mm = 200 Lagen.')),
            (3, lambda R: zahl('Eine Plastiktüte ist 0,02 mm dick. Wie hoch wäre ein Stapel aus 5 Millionen Tüten? Gib das Ergebnis in Metern an.', 100,
                               '5000000 * 0.02 / 1000', 'Höhe = Anzahl · Dicke. Danach mm in m umrechnen.',
                               '5 000 000 · 0,02 mm = 100 000 mm = 100 m.', einheit='m')),
            (3, lambda R: wahl(R, 'Ein Kind schreibt: 0,00058 = 5,8 · 10⁻³. Was stimmt?', 'Falsch: richtig ist 5,8 · 10⁻⁴.',
                               ['Alles ist richtig.', 'Falsch: richtig ist 58 · 10⁻⁵.', 'Falsch: Der Exponent muss positiv sein.'],
                               'Zähle, um wie viele Stellen das Komma nach rechts wandert, bis 5,8 dasteht.',
                               'Von 0,00058 bis 5,8 wandert das Komma 4 Stellen nach rechts. Also 5,8 · 10⁻⁴. 58 · 10⁻⁵ hat den gleichen Wert, ist aber nicht wissenschaftlich.')),
            (3, lambda R: zahl('7 · 10⁻⁴ wird durch 1 000 geteilt. Das Ergebnis ist 7 · 10ⁿ. Wie groß ist n?', -7, '-4 - 3',
                               'Durch 1 000 teilen heißt: Komma 3 Stellen nach links. Was passiert mit dem Exponenten?',
                               '7 · 10⁻⁴ = 0,0007. 0,0007 : 1 000 = 0,0000007 = 7 · 10⁻⁷. Also n = −7.')),
        ],
        'vorsilben_klein': [
            (2, lambda R: zahl('Rechne um: 0,35 mm = ? µm', 350, '0.35 * 1000', '1 mm = 1 000 µm.', '0,35 mm = 0,35 · 1 000 µm = 350 µm.', einheit='µm')),
            (2, lambda R: wahl(R, 'Welche Länge ist am kleinsten?', '400 nm', ['0,5 µm', '0,001 mm', '2 · 10⁻⁶ m'],
                               'Rechne alle Längen in nm um (1 µm = 1 000 nm).',
                               '0,5 µm = 500 nm; 0,001 mm = 1 µm = 1 000 nm; 2 · 10⁻⁶ m = 2 µm = 2 000 nm. Am kleinsten: 400 nm.')),
            (3, lambda R: zahl('Ein rotes Blutkörperchen ist etwa 7,5 µm breit. Wie viele liegen nebeneinander auf einer Strecke von 3 mm?', 400,
                               '3 * 1000 / 7.5', 'Rechne 3 mm in µm um. Dann teilen.', '3 mm = 3 000 µm. 3 000 : 7,5 = 400.')),
            (3, lambda R: zahl('Eine Kamera braucht für ein Bild 4 ms. Wie viele Bilder schafft sie höchstens in 1,2 s?', 300,
                               '1.2 * 1000 / 4', 'Rechne 1,2 s in ms um (1 s = 1 000 ms).', '1,2 s = 1 200 ms. 1 200 : 4 = 300 Bilder.')),
            (3, lambda R: zahl('Wie viele Nanometer sind ein Millimeter? Schreibe das Ergebnis als 10ⁿ. Wie groß ist n?', 6, '9 - 3',
                               'Milli = 10⁻³, Nano = 10⁻⁹. Wie oft passt 10⁻⁹ in 10⁻³?',
                               '1 mm = 10⁻³ m, 1 nm = 10⁻⁹ m. 10⁻³ : 10⁻⁹ = 10⁶. Also 1 mm = 1 000 000 nm, n = 6.')),
            (3, lambda R: wahl(R, 'Jonas schreibt: 250 µm = 0,25 m. Was stimmt?', 'Falsch: 250 µm = 0,25 mm = 0,00025 m.',
                               ['Richtig.', 'Falsch: 250 µm = 250 000 m.', 'Falsch: 250 µm = 2,5 m.'],
                               '1 000 µm sind 1 mm. Wie viele mm sind 250 µm? Und wie viele m?',
                               '250 µm : 1 000 = 0,25 mm. 0,25 mm : 1 000 = 0,00025 m. Jonas hat nur einmal durch 1 000 geteilt.')),
        ],
        'vergleichen_pruefen': [
            (2, lambda R: wahl(R, 'Welche Zahl ist am größten?', '1,1 · 10⁵', ['9,9 · 10⁴', '99 000', '0,8 · 10⁵'],
                               'Schreibe alle Zahlen aus.', '1,1 · 10⁵ = 110 000; 9,9 · 10⁴ = 99 000; 0,8 · 10⁵ = 80 000. Am größten: 1,1 · 10⁵.')),
            (2, lambda R: wahl(R, 'Ordne der Größe nach, mit der kleinsten Zahl zuerst: 3 · 10⁻², 4 · 10⁻³, 2 · 10⁻¹, 5 · 10⁻⁴. Welche Zahl steht an zweiter Stelle?',
                               '4 · 10⁻³', ['5 · 10⁻⁴', '3 · 10⁻²', '2 · 10⁻¹'],
                               'Je kleiner der Exponent, desto kleiner die Zahl.',
                               'Exponenten: −4 < −3 < −2 < −1. Reihenfolge: 5 · 10⁻⁴, 4 · 10⁻³, 3 · 10⁻², 2 · 10⁻¹. An zweiter Stelle: 4 · 10⁻³.')),
            (3, lambda R: wahl(R, 'Stimmt die Aussage? „2 · 10⁶ ist doppelt so groß wie 10³.“', 'Nein, 2 · 10⁶ ist 2 000-mal so groß wie 10³.',
                               ['Ja, wegen der 2 vor der Zehnerpotenz.', 'Nein, 2 · 10⁶ ist 2-mal so klein.', 'Nein, 2 · 10⁶ ist 6-mal so groß.'],
                               'Schreibe beide Zahlen aus und teile die größere durch die kleinere.',
                               '2 · 10⁶ = 2 000 000 und 10³ = 1 000. 2 000 000 : 1 000 = 2 000.')),
            (3, lambda R: zahl('Ein Virus ist etwa 1 · 10⁻⁷ m lang, ein Bakterium etwa 2 · 10⁻⁶ m. Wie viel Mal so lang ist das Bakterium?', 20,
                               '(2/1000000) / (1/10000000)', 'Schreibe beide Längen aus und teile.',
                               '2 · 10⁻⁶ m = 0,000002 m; 1 · 10⁻⁷ m = 0,0000001 m. 0,000002 : 0,0000001 = 20.')),
            (3, lambda R: wahl(R, 'Für welche ganzen Zahlen n ist 3 · 10ⁿ größer als 0,02 und kleiner als 0,5?', 'n = −1 und n = −2',
                               ['nur n = −1', 'nur n = −2', 'n = −2 und n = −3'],
                               'Probiere n = 0, −1, −2, −3 aus und schreibe 3 · 10ⁿ jeweils aus.',
                               'n = 0: 3 (zu groß). n = −1: 0,3 passt. n = −2: 0,03 passt (größer als 0,02). n = −3: 0,003 (zu klein).')),
            (3, lambda R: wahl(R, 'Ein Kind sagt: „8 · 10⁻⁵ ist größer als 2 · 10⁻⁴, weil 8 größer ist als 2.“ Was stimmt?',
                               'Falsch: 2 · 10⁻⁴ = 0,0002 ist größer als 8 · 10⁻⁵ = 0,00008.',
                               ['Richtig.', 'Falsch: Beide Zahlen sind gleich groß.', 'Falsch: 8 · 10⁻⁵ ist negativ.'],
                               'Vergleiche zuerst die Exponenten: −4 oder −5, was ist größer?',
                               '−4 ist größer als −5, also ist 2 · 10⁻⁴ größer. Ausgeschrieben: 0,0002 > 0,00008.')),
        ],
    }


ergaenzen(DATEI, _zp(), seed=6019)


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('zahlen.potenzen_zehner', 13_6_1)
# a) gleiche Rechnung wie Stufe 2, nur größere Zahl
for _e in ('10⁷', '10¹¹', '10¹²'):
    BF.stufe('zehnerpotenz', f'Wie viele Tausender stecken in {_e}?', 2)
# a) Grundform → Stufe 2
BF.stufe('gross_wissenschaftlich', 'Ein Jahr hat etwa 3,15 · 10⁷ Sekunden. Schreibe die Zahl ohne Zehnerpotenz.', 2)
BF.stufe('gross_wissenschaftlich', 'Licht legt in einer Sekunde etwa 300 000 km zurück. Schreibe die Zahl als a · 10ⁿ. Wie groß ist n?', 2)
BF.stufe('klein_wissenschaftlich', 'Ein Kopfhaar ist etwa 7 · 10⁻⁵ m dick. Schreibe die Zahl als Dezimalzahl.', 2)
# a) gleicher Exponent → Stufe 1
BF.stufe('vergleichen_pruefen', 'Welche Zahl ist größer: 1,9 · 10⁻² oder 5,3 · 10⁻²?', 1)

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----


# ---------- DURCHSICHT (Neunzehnte Runde, Teil A, Zweig durchsicht-kl6) ----------
from _durchsicht_kl6 import Befunde, befunde_anwenden  # noqa: E402

DS = Befunde('zahlen.potenzen_zehner', 19_6_4)
_S = DS.stufe
# gross_wissenschaftlich: „a · 10ⁿ + b · 10ᵐ ausschreiben“ dreimal gleich gebaut = Abwandlung → S2
for _t in ('Berechne 2 · 10⁵ + 9 · 10² und schreibe das Ergebnis ohne Zehnerpotenz.', 'Berechne 7 · 10⁶ + 1 · 10⁴ und schreibe das Ergebnis ohne Zehnerpotenz.',
           'Berechne 9 · 10⁷ + 1 · 10² und schreibe das Ergebnis ohne Zehnerpotenz.'):
    _S('gross_wissenschaftlich', _t, 2)
# vorsilben_gross: MW → W ist das Stufe-1-Muster; GB → MB und MB → kB wie in Stufe 2
_S('vorsilben_gross', 'Ein Kraftwerk leistet 20 MW. Wie viele Watt sind das? Schreibe die Zahl aus.', 1)
_S('vorsilben_gross', 'Ein Film hat 0,7 GB. Wie viele MB sind das? (1 GB = 1 000 MB)', 2)
_S('vorsilben_gross', 'Rechne um: 4,9 MB = ? kB', 2)
# negativer_exponent: „Welche ist am kleinsten?“ viermal gleich gebaut = Vergleichen → S2
for _t in ('Welche dieser Zahlen ist am kleinsten: 10⁻³, 10¹, 10⁻¹, 10⁻⁴?', 'Welche dieser Zahlen ist am kleinsten: 10², 10¹, 10⁻⁷, 10⁻⁴?',
           'Welche dieser Zahlen ist am kleinsten: 10⁻⁶, 10⁻², 10⁰, 10⁻⁷?', 'Welche dieser Zahlen ist am kleinsten: 10⁻⁵, 10¹, 10⁻¹, 10⁻⁴?'):
    _S('negativer_exponent', _t, 2)
# klein_wissenschaftlich: Bakterium in a · 10ⁿ = eingekleidetes Umschreiben → S2
_S('klein_wissenschaftlich', 'Ein Bakterium ist etwa 0,000002 m lang. Schreibe die Zahl als a · 10ⁿ. Wie groß ist n?', 2)
# vorsilben_klein: µm → nm ist Umrechnen wie S2; Computer-Takt dreimal hintereinander → zwei nach S2
_S('vorsilben_klein', 'Rechne um: 6 µm = ? nm', 2)
_S('vorsilben_klein', 'Ein Rechenschritt eines Computers dauert 10 ns. Wie viele Schritte schafft er in 1 Sekunde?', 2)
_S('vorsilben_klein', 'Ein Rechenschritt eines Computers dauert 5 ns. Wie viele Schritte schafft er in 1 Sekunde?', 2)
# vergleichen_pruefen: gleiche Mantisse, Exponent um 1 verschieden = Stufe-2-Vergleich
_S('vergleichen_pruefen', 'Wie viel Mal so groß ist 8 · 10⁶ wie 8 · 10⁵?', 2)
befunde_anwenden(DATEI, DS)
# ---- DURCHSICHT ENDE ----


if __name__ == '__main__':
    schreibe(DATEI)
