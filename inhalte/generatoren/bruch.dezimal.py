#!/usr/bin/env python3
"""Thema bruch.dezimal – Dezimalzahlen (Klasse 6)."""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _basis import *  # noqa: E402,F403

R = random.Random(22)
E = eintrag_laden('bruch.dezimal')
HB = 'Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt.'
STRICH = '̅'   # Periodenstrich (kombinierender Überstrich)

ETAPPEN = [
    {'lernziel': 'stellenwerte', 'titel': 'Stellenwerte nach dem Komma',
     'regel': 'Nach dem Komma kommen die Stellen ⟦Zehntel (z)⟧, ⟦Hundertstel (h)⟧ und ⟦Tausendstel (t)⟧. In 3,472 steht die 4 für 4 Zehntel, die 7 für 7 Hundertstel und die 2 für 2 Tausendstel.',
     'schritte': ['3,472 in der Stellenwerttafel: E = 3, z = 4, h = 7, t = 2.', 'Die 7 steht bei den Hundertsteln. Ihr Wert ist ⟦7/100 = 0,07⟧.'],
     'fehler': 'Zu sagen, die 7 in 3,472 hat den Wert 7, ist falsch: Sie steht an der ⟦Hundertstelstelle⟧ und bedeutet 7 Hundertstel = 0,07.',
     'bild': {'typ': 'stellentafel', 'stellen': ['E', 'z', 'h', 't'], 'ziffern': [3, 4, 7, 2], 'markiert': 2}},
    {'lernziel': 'vergleichen_ordnen', 'titel': 'Dezimalzahlen vergleichen',
     'regel': 'Dezimalzahlen vergleichst du ⟦Stelle für Stelle von links⟧: erst die Ganzen, dann die Zehntel, dann die Hundertstel. Tipp: ⟦Hänge Nullen an⟧, bis beide gleich viele Nachkommastellen haben – das ändert den Wert nicht.',
     'schritte': ['Vergleiche 0,45 und 0,5. Null anhängen: 0,5 = 0,50.', '45 Hundertstel sind weniger als 50 Hundertstel, also ⟦0,45 < 0,5⟧.'],
     'fehler': '„0,45 ist größer als 0,5, weil 45 > 5“ ist falsch: Die 5 in 0,5 sind 5 ⟦Zehntel⟧ = 50 Hundertstel. Mehr Ziffern heißt ⟦nicht⟧ größer.',
     'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 1, 'abschnitte': 10, 'beschriftet': 'anfang_ende'}},
    {'lernziel': 'runden', 'titel': 'Dezimalzahlen runden',
     'regel': 'Beim ⟦Runden⟧ schaust du nur auf die Ziffer ⟦direkt rechts neben der Rundungsstelle⟧. Ist sie 0, 1, 2, 3 oder 4, wird ⟦abgerundet⟧. Ist sie 5, 6, 7, 8 oder 9, wird ⟦aufgerundet⟧.',
     'schritte': ['Runde 4,368 auf Zehntel. Die Zehntelstelle ist die 3, rechts daneben steht die 6.', '6 ist 5 oder mehr, also aufrunden: 4,368 ≈ ⟦4,4⟧.'],
     'fehler': '2,349 auf Zehntel: erst 2,35, dann 2,4 – das ist falsch (Kettenrunden). Es zählt nur die Ziffer ⟦direkt rechts⟧ neben der Zehntelstelle, also die 4: ⟦2,3⟧.'},
    {'lernziel': 'bruch_zu_dezimal', 'titel': 'Bruch in Dezimalzahl umwandeln',
     'regel': 'Einen Bruch wandelst du in eine Dezimalzahl um, indem du ihn auf den Nenner ⟦10, 100 oder 1 000 erweiterst⟧. Geht das nicht, ⟦teilst du den Zähler durch den Nenner⟧.',
     'schritte': ['3/8: Erweitere mit 125, denn 8 · 125 = 1 000.', '3/8 = 375/1 000 = ⟦0,375⟧.'],
     'probe': '0,375 · 8 = 3 ✓',
     'fehler': '3/8 = 3,8 ist falsch: Der Bruchstrich ist kein Komma. 3/8 heißt ⟦3 : 8⟧ = 0,375.'},
    {'lernziel': 'dezimal_zu_bruch', 'titel': 'Dezimalzahl als Bruch schreiben',
     'regel': 'Eine endliche Dezimalzahl schreibst du als ⟦Zehnerbruch⟧: Der Nenner hat so viele Nullen, wie die Zahl ⟦Nachkommastellen⟧ hat. Danach ⟦kürzen⟧.',
     'schritte': ['0,35 hat 2 Nachkommastellen, also Hundertstel: 0,35 = 35/100.', 'Kürzen mit 5: 35/100 = ⟦7/20⟧.'],
     'probe': '7 : 20 = 0,35 ✓',
     'fehler': '0,35 = 35/10 ist falsch: Zwei Nachkommastellen bedeuten ⟦Hundertstel⟧, also Nenner 100.'},
    {'lernziel': 'periodisch', 'titel': 'Periodische Dezimalzahlen',
     'regel': 'Manche Brüche ergeben eine ⟦periodische Dezimalzahl⟧: Ziffern wiederholen sich ohne Ende, z. B. 1/3 = 0,333… Man setzt einen ⟦Strich über die Periode⟧: 0,3̅. Ein vollständig gekürzter Bruch ist genau dann ⟦endlich⟧, wenn sein Nenner nur die Primfaktoren ⟦2 und 5⟧ hat.',
     'schritte': ['5/6: Rechne 5 : 6 schriftlich: 0,8333…', 'Ab der zweiten Nachkommastelle wiederholt sich die 3: 5/6 = ⟦0,83̅⟧.'],
     'fehler': '1/3 = 0,3 ist falsch: 0,3 = 3/10, und 3 · 0,3 = 0,9, nicht 1. Richtig ist 1/3 = ⟦0,3̅⟧ – die 3 wiederholt sich ohne Ende.'},
    {'lernziel': 'verstehen', 'titel': 'Aussagen über Dezimalzahlen prüfen',
     'regel': 'Prüfe Aussagen über Dezimalzahlen mit der ⟦Stellenwerttafel⟧ oder mit einem ⟦Gegenbeispiel⟧. Endnullen nach dem Komma ändern den Wert nicht: 4,7 = 4,70.',
     'schritte': ['Aussage: „Zwischen 0,1 und 0,2 gibt es keine Zahl.“ Hänge eine Null an: 0,10 und 0,20.', 'Dazwischen liegt z. B. 0,15. Die Aussage ist ⟦falsch⟧.'],
     'fehler': '„3,14 ist größer als 3,2, weil 14 > 2“ ist falsch: Man vergleicht ⟦Stelle für Stelle⟧. Zehntel: 1 < 2, also 3,14 < 3,2.'},
]

MERKE = ['Stellen nach dem Komma: Zehntel, Hundertstel, Tausendstel.', 'Vergleichen: Nullen anhängen, Stelle für Stelle von links.',
         'Runden: nur die Ziffer rechts neben der Rundungsstelle zählt (ab 5 aufrunden).',
         'Bruch → Dezimalzahl: auf 10, 100, 1 000 erweitern oder Zähler : Nenner.', 'Endlich nur, wenn der gekürzte Nenner nur 2 und 5 enthält; sonst periodisch (0,3̅).']

STELLEN = [(1, 'Zehntel'), (2, 'Hundertstel'), (3, 'Tausendstel')]


def zufall_dez(R, ganz_max, k):
    """Zahl mit genau k Nachkommastellen (letzte Ziffer ≠ 0)."""
    while True:
        x = Fr(R.randint(0, ganz_max * 10 ** k + 10 ** k - 1), 10 ** k)
        if (x * 10 ** k) % 10 and x > 0: return x


def ziffer(x, k):
    return int((x * 10 ** k) // 1 % 10)


# ---------- 1 Stellenwerte ----------
def g_stellen(st):
    if st == 1:
        x = zufall_dez(R, 99, 3)
        k, name = R.choice(STELLEN)
        return {'y': 'zahl', 'f': {'text': f'Welche Ziffer steht in {zt(x)} an der {name}stelle?'}, 'o': {'wert': ziffer(x, k)}, 'c': f'({float(x)} * 10**{k}) // 1 % 10',
                'w': f'Nach dem Komma: 1. Stelle Zehntel, 2. Hundertstel, 3. Tausendstel. Die {k}. Stelle von {zt(x)} ist {ziffer(x, k)}.', 'h': f'Die {name} sind die {k}. Stelle nach dem Komma.'}
    if st == 2:
        if R.random() < .5:
            x = zufall_dez(R, 50, 3)
            k = R.choice([k for k, _ in STELLEN if ziffer(x, k) != 0] or [3])
            d = ziffer(x, k)
            namen = {1: 'Zehntel', 2: 'Hundertstel', 3: 'Tausendstel'}
            r = f'{d} {namen[k]}'
            falsch = [f'{d} {namen[j]}' for j in (1, 2, 3) if j != k] + [f'{d} Einer']
            return {**wahl(R, r, falsch), 'f': {'text': f'Welchen Wert hat die Ziffer {d} an der {k}. Nachkommastelle von {zt(x)}?'},
                    'w': f'Die {k}. Nachkommastelle sind die {namen[k]}: {d} {namen[k]} = {zt(Fr(d, 10 ** k))}.', 'h': 'Zähle die Stellen nach dem Komma: Zehntel, Hundertstel, Tausendstel.'}
        e, z, h, t = R.randint(0, 30), R.randint(0, 9), R.randint(0, 9), R.randint(1, 9)
        if R.random() < .5: z, h = 0, R.randint(1, 9)
        x = e + Fr(z, 10) + Fr(h, 100) + Fr(t, 1000)
        return {'y': 'zahl', 'f': {'text': f'Schreibe als Dezimalzahl: {e} Einer, {z} Zehntel, {h} Hundertstel, {t} Tausendstel.'}, 'o': {'wert': wert(x)},
                'c': f'{e} + {z}/10 + {h}/100 + {t}/1000', 'w': f'Ziffern in die Stellen eintragen: {zt(x)}.', 'h': 'Trage die Ziffern der Reihe nach in die Stellenwerttafel ein. Leere Stellen bekommen eine 0.'}
    art = R.randrange(3)
    if art == 0:
        z, h = R.randint(2, 9), R.randint(11, 25)
        x = Fr(z, 10) + Fr(h, 100)
        return {'y': 'zahl', 'f': {'text': f'Schreibe als Dezimalzahl: {z} Zehntel und {h} Hundertstel.'}, 'o': {'wert': wert(x)}, 'c': f'{z}/10 + {h}/100',
                'w': f'{h} Hundertstel = {h // 10} Zehntel und {h % 10} Hundertstel. Zusammen {z + h // 10} Zehntel, {h % 10} Hundertstel: {zt(x)}.',
                'h': '10 Hundertstel sind 1 Zehntel. Bündele zuerst.'}
    if art == 1:
        x = zufall_dez(R, 20, 3)
        k, name = R.choice(STELLEN)
        if ziffer(x, k) == 9: return g_stellen(3)
        return {'y': 'zahl', 'f': {'text': f'Die Ziffer an der {name}stelle von {zt(x)} wird um 1 größer. Wie heißt die neue Zahl?'}, 'o': {'wert': wert(x + Fr(1, 10 ** k))},
                'c': f'{float(x)} + 1/10**{k}', 'w': f'Ein {name} = {zt(Fr(1, 10 ** k))}. {zt(x)} + {zt(Fr(1, 10 ** k))} = {zt(x + Fr(1, 10 ** k))}.',
                'h': f'Die Zahl wird um ein {name} = {zt(Fr(1, 10 ** k))} größer.'}
    e = R.randint(1, 9)
    h, t = R.randint(1, 9), R.randint(1, 9)
    x = e + Fr(h, 100) + Fr(t, 1000)
    return {'y': 'zahl', 'f': {'text': f'Schreibe als Dezimalzahl: {e} + {h}/100 + {t}/1 000'}, 'o': {'wert': wert(x)}, 'c': f'{e} + {h}/100 + {t}/1000',
            'w': f'Keine Zehntel, also eine 0 an der Zehntelstelle: {zt(x)}.', 'h': 'Welche Stelle bleibt leer? Dort steht eine 0.'}


# ---------- 2 Vergleichen und ordnen ----------
def mark(x, start, ende, n, text, w, h):
    idx = (Fr(x) - start) * n / (ende - start)
    assert idx.denominator == 1 and 0 <= idx <= n
    return {'y': 'markierung', 'f': {'text': text, 'grafik': {'typ': 'zahlenstrahl', 'start': wert(start), 'ende': wert(ende), 'abschnitte': n, 'beschriftet': 'anfang_ende'}},
            'o': {'index': int(idx)}, 'zahl': wert(x), 'c': f'{float(start)} + ({float(ende)} - {float(start)}) * {int(idx)} / {n}', 'w': w, 'h': h}


def g_vgl(st):
    if st == 1:
        g = R.randint(0, 9)
        a = g + Fr(R.randint(1, 9), 10)
        b = g + Fr(R.randint(11, 99), 100)
        if R.random() < .5: a, b = b, a
        if a == b: return g_vgl(1)
        r = zt(max(a, b))
        return {**wahl(R, r, [zt(min(a, b)), 'Beide sind gleich groß'], 3), 'f': {'text': f'Welche Zahl ist größer: {zt(a)} oder {zt(b)}?'},
                'w': f'Nullen anhängen: {zt(a)} → {zt(a).ljust(len(zt(b)), "0") if len(zt(a)) < len(zt(b)) else zt(a)}, {zt(b)} → {zt(b).ljust(len(zt(a)), "0") if len(zt(b)) < len(zt(a)) else zt(b)}. Größer: {r}.',
                'h': 'Hänge Nullen an, bis beide Zahlen gleich viele Nachkommastellen haben.'}
    if st == 2:
        if R.random() < .5:
            g = R.randint(0, 5)
            xs = {g + Fr(R.randint(1, 9), 10), g + Fr(R.randint(1, 99), 100), g + Fr(R.randint(1, 999), 1000), g + Fr(R.randint(1, 9), 100)}
            xs = [x for x in xs if (x * 1000) % 10 or (x * 100) % 10 or (x * 10) % 10]
            if len(xs) < 4: return g_vgl(2)
            frage = R.choice(['größte', 'kleinste'])
            r = zt(max(xs) if frage == 'größte' else min(xs))
            return {**wahl(R, r, [zt(x) for x in xs]), 'f': {'text': f'Welche ist die {frage} Zahl: ' + ', '.join(zt(x) for x in xs) + '?'},
                    'w': 'Geordnet: ' + ' < '.join(zt(x) for x in sorted(xs)) + f'. Die {frage} ist {r}.', 'h': 'Vergleiche Stelle für Stelle. Mehr Ziffern heißt nicht größer.'}
        g = R.randint(0, 8)
        k = R.randint(1, 9)
        x = g + Fr(k, 10)
        return mark(x, g, g + 1, 10, f'Markiere {zt(x)} am Zahlenstrahl (von {g} bis {g + 1}, 10 gleiche Teile).',
                    f'Jeder Teil ist 0,1. {zt(x)} liegt {k} {"Teil" if k == 1 else "Teile"} rechts von {g}.', 'Jeder Strich ist ein Zehntel weiter.')
    art = R.randrange(3)
    if art == 0:
        a = zufall_dez(R, 20, 1)
        b = a + Fr(1, 10)
        m = (a + b) / 2
        return {'y': 'zahl', 'f': {'text': f'Welche Zahl liegt genau in der Mitte zwischen {zt(a)} und {zt(b)}?'}, 'o': {'wert': wert(m)}, 'c': f'({float(a)} + {float(b)}) / 2',
                'w': f'Null anhängen: {zt(a)}0 und {zt(b)}0. Die Mitte ist {zt(m)}.', 'h': 'Hänge an beide Zahlen eine 0 an. Dann siehst du die Hundertstel dazwischen.'}
    if art == 1:
        g = R.randint(0, 5)
        z = R.randint(0, 9)
        k = R.randint(1, 9)
        x = g + Fr(z, 10) + Fr(k, 100)
        s = g + Fr(z, 10)
        return mark(x, s, s + Fr(1, 10), 10, f'Markiere {zt(x)} am Zahlenstrahl (von {zt(s)} bis {zt(s + Fr(1, 10))}, 10 gleiche Teile).',
                    f'Jeder Teil ist 0,01. {zt(x)} liegt {k} {"Teil" if k == 1 else "Teile"} rechts von {zt(s)}.', 'Von Strich zu Strich geht es um ein Hundertstel weiter.')
    a = zufall_dez(R, 20, R.choice([1, 2]))
    k = len(zt(a).split(',')[1]) + 1
    r = a + Fr(1, 10 ** k)
    return {'y': 'zahl', 'f': {'text': f'Welche ist die kleinste Zahl mit {k} Nachkommastellen, die größer als {zt(a)} ist?'}, 'o': {'wert': wert(r)}, 'c': f'{float(a)} + 1/10**{k}',
            'w': f'{zt(a)} = {zt(a)}0. Eine {["", "Zehntel", "Hundertstel", "Tausendstel"][k]}stelle weiter: {zt(r)}.', 'h': 'Hänge eine 0 an und zähle an der letzten Stelle 1 dazu.'}


# ---------- 3 Runden ----------
def gerundet(x, k): return (x * 10 ** k + Fr(1, 2)) // 1 / Fr(10 ** k)


def c_runden(x, k): return f'({float(x)} * 10**{k} + 1/2) // 1 / 10**{k}'


NAMEN = {0: 'Ganze', 1: 'Zehntel', 2: 'Hundertstel', 3: 'Tausendstel'}


def g_runden(st):
    if st == 1:
        k = R.choice([0, 1])
        x = zufall_dez(R, 50, k + 1)
        r = gerundet(x, k)
        d = ziffer(x, k + 1)
        return {'y': 'zahl', 'f': {'text': f'Runde {zt(x)} auf {NAMEN[k]}.'}, 'o': {'wert': wert(r)}, 'c': c_runden(x, k),
                'w': f'Rechts neben der Rundungsstelle steht {d}: {"aufrunden" if d >= 5 else "abrunden"}. {zt(x)} ≈ {zt(r)}.', 'h': 'Schau nur auf die Ziffer rechts neben der Rundungsstelle.'}
    if st == 2:
        k = R.choice([1, 2, 2, 3])
        x = zufall_dez(R, 30, k + R.randint(1, 2))
        if R.random() < .3:
            x = Fr(int(x * 10 ** k) // 10 * 10 + 9, 10 ** k) + Fr(R.randint(5, 9), 10 ** (k + 1))
        r = gerundet(x, k)
        d = ziffer(x, k + 1)
        return {'y': 'zahl', 'f': {'text': f'Runde {zt(x)} auf {NAMEN[k]}.'}, 'o': {'wert': wert(r)}, 'c': c_runden(x, k),
                'w': f'Die Ziffer rechts neben der {NAMEN[k]}stelle ist {d}: {"aufrunden" if d >= 5 else "abrunden"}. {zt(x)} ≈ {zt(r)}.' + (' Beim Aufrunden einer 9 entsteht ein Übertrag.' if ziffer(x, k) == 9 and d >= 5 else ''),
                'h': 'Markiere die Rundungsstelle. Steht rechts daneben 5 oder mehr, wird sie um 1 größer.'}
    art = R.randrange(3)
    if art == 0:
        x = Fr(R.randint(1000, 2999), 1000)
        while ziffer(x, 3) == 0: x = Fr(R.randint(1000, 2999), 1000)
        ware = R.choice(['Ein Liter Benzin', 'Ein Liter Diesel', 'Eine Kilowattstunde Strom'])
        if ware.startswith('Eine Kilo'): x = Fr(R.randint(250, 450), 1000)
        r = gerundet(x, 2)
        return {'y': 'zahl', 'f': {'text': f'{ware} kostet {zt(x)} €. Runde auf ganze Cent.'}, 'o': {'wert': wert(r), 'einheit': '€'}, 'c': c_runden(x, 2),
                'w': f'Cent sind Hundertstel Euro. Die Tausendstelziffer ist {ziffer(x, 3)}: {zt(x)} € ≈ {zt(r)} €.', 'h': 'Ein Cent ist ein Hundertstel Euro. Runde auf Hundertstel.'}
    if art == 1:
        z = R.randint(1, 8)
        g = R.randint(0, 9)
        x = g + Fr(z, 10) + Fr(4, 100) + Fr(R.randint(5, 9), 1000)
        r = gerundet(x, 1)
        falsch = zt(gerundet(gerundet(x, 2), 1))
        return {**wahl(R, zt(r), [falsch, zt(gerundet(x, 2)), zt(r + Fr(2, 10))]), 'f': {'text': f'Runde {zt(x)} auf Zehntel.'},
                'w': f'Rechts neben der Zehntelstelle steht 4: abrunden, {zt(r)}. Erst auf Hundertstel und dann auf Zehntel zu runden ({falsch}) ist falsch.',
                'h': 'Nicht in mehreren Schritten runden! Nur die Hundertstelziffer zählt.'}
    g, z = R.randint(1, 9), R.randint(1, 8)
    ziel = g + Fr(z, 10)
    r = zt(ziel - Fr(R.randint(1, 5), 100))
    falsch = [zt(ziel - Fr(R.randint(6, 9), 100)), zt(ziel + Fr(R.randint(5, 9), 100)), zt(ziel + Fr(1, 10) + Fr(R.randint(1, 4), 100))]
    return {**wahl(R, r, falsch), 'f': {'text': f'Welche Zahl ergibt auf Zehntel gerundet {zt(ziel)}?'},
            'w': f'Auf {zt(ziel)} runden alle Zahlen von {zt(ziel - Fr(5, 100))} bis unter {zt(ziel + Fr(5, 100))}. Also {r}.', 'h': 'Runde jede Zahl auf Zehntel und vergleiche.'}


# ---------- 4 Bruch -> Dezimal ----------
def g_b2d(st):
    if st == 1:
        n = R.choice([2, 4, 5, 10, 20, 25, 50, 100])
        z = R.randint(1, n - 1)
        while gcd(z, n) > 1: z = R.randint(1, n - 1)
        x = Fr(z, n)
        ziel = next(10 ** k for k in range(1, 5) if 10 ** k % n == 0)
        f = ziel // n
        return {'y': 'zahl', 'f': {'text': f'Schreibe {z}/{n} als Dezimalzahl.'}, 'o': {'wert': wert(x)}, 'c': f'{z} / {n}',
                'w': (f'Erweitern mit {f}: {z}/{n} = {z * f}/{zt(ziel)} = {zt(x)}.' if f > 1 else f'{z}/{n} ist schon ein Zehnerbruch: {zt(x)}.'),
                'h': 'Erweitere auf 10, 100 oder 1 000.'}
    if st == 2:
        if R.random() < .5:
            n = R.choice([8, 16, 40, 80, 125, 200, 250])
            z = R.randint(1, n - 1)
            while gcd(z, n) > 1: z = R.randint(1, n - 1)
        else:
            n = R.choice([2, 4, 5, 8, 20])
            z = R.randint(n + 1, 4 * n)
            while gcd(z, n) > 1: z = R.randint(n + 1, 4 * n)
        x = Fr(z, n)
        if R.random() < .4:
            r = zt(x)
            falsch = [f'{z},{n}', zt(Fr(z, n * 10)) if z < n else zt(x / 10), zt(x * 10)]
            return {**wahl(R, r, falsch), 'f': {'text': f'Welche Dezimalzahl ist gleich {z}/{n}?'},
                    'w': f'{z}/{n} = {z} : {n} = {r}. Der Bruchstrich ist kein Komma.', 'h': 'Der Bruchstrich bedeutet „geteilt durch“.'}
        return {'y': 'zahl', 'f': {'text': f'Schreibe {z}/{n} als Dezimalzahl.'}, 'o': {'wert': wert(x)}, 'c': f'{z} / {n}',
                'w': f'Der Bruchstrich heißt „geteilt durch“: {z} : {n} = {zt(x)}.', 'h': 'Erweitere auf 10, 100 oder 1 000 – oder teile den Zähler durch den Nenner.'}
    art = R.randrange(2)
    if art == 0:
        x = Fr(R.randint(1, 19), R.choice([4, 5, 8, 20, 25]))
        k = R.choice([3, 7, 9, 11])
        z, n = x.numerator * k, x.denominator * k
        return {'y': 'zahl', 'f': {'text': f'Schreibe {z}/{n} als Dezimalzahl.'}, 'o': {'wert': wert(x)}, 'c': f'{z} / {n}',
                'w': f'Zuerst kürzen mit {k}: {z}/{n} = {bruch(x)}. Dann {bruch(x)} = {zt(x)}.', 'h': 'Kürze zuerst. Dann siehst du, auf welchen Zehnerbruch du erweitern kannst.'}
    a = Fr(R.randint(1, 9), R.choice([2, 4, 5, 8]))
    b = Fr(R.randint(1, 9), 10)
    return {'y': 'zahl', 'f': {'text': f'Berechne {bruch(a)} + {zt(b)} und gib das Ergebnis als Dezimalzahl an.'}, 'o': {'wert': wert(a + b)}, 'c': f'{a.numerator}/{a.denominator} + {float(b)}',
            'w': f'{bruch(a)} = {zt(a)}. {zt(a)} + {zt(b)} = {zt(a + b)}.', 'h': 'Wandle den Bruch zuerst in eine Dezimalzahl um.'}


# ---------- 5 Dezimal -> Bruch ----------
def luecke(x, text, w, h, c_ausdr):
    z, n = x.numerator, x.denominator
    return {'y': 'luecken', 'f': {'text': text, 'schablone': '□/□', 'hinweis': HB}, 'o': {'werte': [z, n]}, 'c': [f'({c_ausdr}) * {n}', f'{n}'], 'w': w, 'h': h}


def g_d2b(st):
    k = {1: 1, 2: R.choice([2, 2, 3]), 3: R.choice([1, 2, 2, 3])}[st]
    g = 0 if st < 3 else R.randint(1, 4)
    x = g + zufall_dez(R, 0, k)
    zb = f'{int(x * 10 ** k)}/{zt(10 ** k)}'
    if st == 3 and R.random() < .4:
        r = bruch(x)
        falsch = [f'{int(x * 10 ** k)}/{zt(10 ** (k - 1))}', bruch(x - g), f'{int(x * 10 ** k)}/{zt(10 ** (k + 1))}']
        falsch = [f for f in falsch if f != r]
        return {**wahl(R, r, falsch), 'f': {'text': f'Welcher Bruch ist gleich {zt(x)}?'},
                'w': f'{zt(x)} = {zb} = {r}.', 'h': 'Schreibe die Zahl als Zehnerbruch (Nenner 10, 100, 1 000) und kürze.'}
    return luecke(x, f'Schreibe {zt(x)} als vollständig gekürzten Bruch.', f'{k} Nachkommastelle{"n" if k > 1 else ""}: {zt(x)} = {zb}' + (f' = {bruch(x)}.' if bruch(x) != zb else '.'),
                  'So viele Nullen im Nenner wie Nachkommastellen. Dann kürzen.', f'{float(x)}')


# ---------- 6 Periodisch ----------
def entwicklung(x):
    """(ganz, vorperiode, periode) als Ziffernfolgen."""
    ganz = x.numerator // x.denominator
    r = x.numerator % x.denominator
    n = x.denominator
    ziffern, rest_pos = [], {}
    while r and r not in rest_pos:
        rest_pos[r] = len(ziffern)
        r *= 10
        ziffern.append(r // n)
        r %= n
    if not r: return ganz, ''.join(map(str, ziffern)), ''
    p = rest_pos[r]
    return ganz, ''.join(map(str, ziffern[:p])), ''.join(map(str, ziffern[p:]))


def per(x):
    g, v, p = entwicklung(Fr(x))
    if not p: return zt(x)
    return f'{g},{v}' + ''.join(c + STRICH for c in p)


def per_falsch(x):
    """Typische Fehlschreibweisen."""
    g, v, p = entwicklung(Fr(x))
    out = [f'{g},{(v + p)[:2] or "0"}']                       # abgebrochen, ohne Strich
    if v: out.append(f'{g},' + ''.join(c + STRICH for c in v + p))   # Strich auch über Vorperiode
    else: out.append(f'{g},{p[0]}' + ''.join(c + STRICH for c in p[1:] + p[0]) if len(p) > 1 else f'{g},{p}{p}')
    out.append(f'{g},' + ''.join(c + STRICH for c in str(x.denominator)))   # Nenner als Periode
    return out


def endlich(x): return all(p in (2, 5) for p in primf(Fr(x).denominator))


def primf(n):
    out, d = [], 2
    while n > 1:
        while n % d == 0: out.append(d); n //= d
        d += 1
    return out


def g_per(st):
    if st == 1:
        if R.random() < .5:
            n = R.choice([3, 9, 11, 6])
            z = R.randint(1, n - 1)
            while gcd(z, n) > 1: z = R.randint(1, n - 1)
            x = Fr(z, n)
            r = per(x)
            return {**wahl(R, r, per_falsch(x)), 'f': {'text': f'Welche Dezimalzahl ist gleich {z}/{n}?'},
                    'w': f'{z} : {n} = {per(x)} – die Ziffern wiederholen sich ohne Ende.', 'h': 'Rechne den Zähler durch den Nenner schriftlich, bis sich etwas wiederholt.'}
        n = R.choice([3, 4, 5, 6, 7, 8, 9, 12, 15, 16, 20, 25, 30, 40])
        z = R.randint(1, n - 1)
        while gcd(z, n) > 1: z = R.randint(1, n - 1)
        x = Fr(z, n)
        e = endlich(x)
        pf = ' · '.join(map(str, primf(n)))
        r = 'endlich, weil der Nenner nur 2 und 5 enthält' if e else 'periodisch, weil der Nenner einen anderen Primfaktor hat'
        falsch = ['periodisch, weil der Nenner einen anderen Primfaktor hat' if e else 'endlich, weil der Nenner nur 2 und 5 enthält',
                  f'{"periodisch" if e else "endlich"}, weil der Zähler {"ungerade" if z % 2 else "gerade"} ist']
        return {**wahl(R, r, falsch, 3), 'f': {'text': f'Ist {z}/{n} als Dezimalzahl endlich oder periodisch?'},
                'w': f'{z}/{n} ist vollständig gekürzt, {n} = {pf}. ' + (f'Nur 2 und 5: endlich, {z}/{n} = {zt(x)}.' if e else f'Anderer Primfaktor: periodisch, {z}/{n} = {per(x)}.'),
                'h': 'Zerlege den Nenner in Primfaktoren. Nur der Zähler spielt keine Rolle.'}
    if st == 2:
        n = R.choice([6, 7, 9, 11, 12, 15, 18, 22, 30])
        z = R.randint(1, 2 * n)
        while gcd(z, n) > 1 or z % n == 0: z = R.randint(1, 2 * n)
        x = Fr(z, n)
        r = per(x)
        return {**wahl(R, r, per_falsch(x)), 'f': {'text': f'Welche Dezimalzahl ist gleich {z}/{n}?'},
                'w': f'{z} : {n} = {r}. Der Strich steht nur über den Ziffern, die sich wiederholen.', 'h': 'Schriftlich teilen. Sobald ein Rest zum zweiten Mal kommt, wiederholen sich die Ziffern.'}
    art = R.randrange(3)
    if art == 0:
        n = R.choice([7, 11, 13, 3, 9, 27, 37])
        z = R.randint(1, n - 1)
        while gcd(z, n) > 1: z = R.randint(1, n - 1)
        x = Fr(z, n)
        k = R.randint(7, 15)
        return {'y': 'zahl', 'f': {'text': f'{z}/{n} = {per(x)}. Welche Ziffer steht an der {k}. Nachkommastelle?'}, 'o': {'wert': ziffer(x, k)}, 'c': f'({z}/{n} * 10**{k}) // 1 % 10',
                'w': f'Die Periode {entwicklung(x)[2]} hat {len(entwicklung(x)[2])} Ziffern. Sie wiederholt sich, an der {k}. Stelle steht {ziffer(x, k)}.',
                'h': 'Wie lang ist die Periode? Zähle in Periodenblöcken weiter.'}
    if art == 1:
        x = Fr(R.randint(1, 19), R.choice([4, 5, 8, 20, 25, 40]))
        k = R.choice([3, 7, 9])
        z, n = x.numerator * k, x.denominator * k
        r = 'endlich, denn nach dem Kürzen enthält der Nenner nur 2 und 5'
        return {**wahl(R, r, ['periodisch, denn der Nenner enthält ' + str(k), 'periodisch, denn der Zähler ist nicht durch 10 teilbar'], 3),
                'f': {'text': f'Ist {z}/{n} als Dezimalzahl endlich oder periodisch?'},
                'w': f'Zuerst kürzen: {z}/{n} = {bruch(x)}. Der Nenner {x.denominator} hat nur die Primfaktoren 2 und 5, also endlich: {zt(x)}.',
                'h': 'Kürze den Bruch zuerst vollständig!'}
    n = R.choice([3, 6, 7, 9, 11, 12, 13])
    x = Fr(1, n)
    return {'y': 'zahl', 'f': {'text': f'1/{n} = {per(x)}. Wie viele Ziffern hat die Periode?'}, 'o': {'wert': len(entwicklung(x)[2])}, 'c': f'{len(entwicklung(x)[2])}',
            'w': f'Unter dem Strich stehen {len(entwicklung(x)[2])} Ziffern: {entwicklung(x)[2]}.', 'h': 'Zähle die Ziffern unter dem Periodenstrich.'}


# ---------- 7 Verstehen ----------
def g_versteh(st):
    a = zufall_dez(R, 9, 1)
    b = zufall_dez(R, 0, 2)
    g = R.randint(1, 9)
    if st == 1:
        aussagen = [(f'{zt(a)} und {zt(a)}0 sind gleich groß.', True, f'Ja, {zt(a)} = {zt(a)}0, eine Endnull nach dem Komma ändert den Wert nicht.'),
                    (f'{zt(a)}0 ist größer als {zt(a)}, weil es mehr Ziffern hat.', False, f'Nein, {zt(a)}0 = {zt(a)}. Eine Endnull ändert den Wert nicht.'),
                    (f'{g},{R.randint(11, 19)} ist größer als {g},{R.randint(2, 9)}, weil die Zahl hinter dem Komma größer ist.', False,
                     'Nein, man vergleicht Stelle für Stelle: Bei den Zehnteln hat die zweite Zahl mehr.')]
    elif st == 2:
        x = zufall_dez(R, 20, 1)
        aussagen = [(f'Zwischen {zt(x)} und {zt(x + Fr(1, 10))} liegt keine andere Dezimalzahl.', False, f'Nein, z. B. {zt(x + Fr(5, 100))} liegt dazwischen.'),
                    (f'{zt(x)} · 10 = {zt(x)}0', False, f'Nein, mal 10 verschiebt das Komma: {zt(x)} · 10 = {zt(x * 10)}.'),
                    (f'{zt(x)} · 10 = {zt(x * 10)}', True, 'Ja, mal 10 verschiebt das Komma um eine Stelle nach rechts.'),
                    (f'1/3 = 0,33', False, '1/3 = 0,3̅. 0,33 ist nur gerundet, denn 3 · 0,33 = 0,99.')]
    else:
        n = R.choice([3, 6, 7, 9, 12, 15])
        zz = 3 if n in (6, 12, 15) else n
        aussagen = [(f'Jeder Bruch mit dem Nenner {n} ist periodisch.', False, f'Nein, z. B. {zz}/{n} = {bruch(Fr(zz, n))} = {zt(Fr(zz, n))} ist endlich. Erst kürzen, dann entscheiden.'),
                    (f'{zt(b)} ist kleiner als {zt(b + Fr(1, 10))}.', True, f'Ja, {zt(b + Fr(1, 10))} hat ein Zehntel mehr.'),
                    (f'{zt(gerundet(b, 1))} ist {zt(b)} auf Zehntel gerundet.', True, f'Ja, rechts neben der Zehntelstelle steht {ziffer(b, 2)}.'),
                    (f'{zt(gerundet(b, 1) + Fr(1, 10))} ist {zt(b)} auf Zehntel gerundet.', False, f'Nein, rechts neben der Zehntelstelle steht {ziffer(b, 2)}, also {zt(gerundet(b, 1))}.')]
    s, stimmt, grund = R.choice(aussagen)
    if stimmt and not grund.startswith('Ja'): grund = 'Ja. ' + grund
    if not stimmt and not grund.startswith('Nein'): grund = 'Nein. ' + grund
    gegen = 'Ja, die Aussage stimmt.' if not stimmt else 'Nein, die Aussage ist falsch.'
    return {**wahl(R, grund, [gegen, 'Das kann man nicht entscheiden.'], 3), 'f': {'text': f'Stimmt die Aussage? „{s}“'},
            'w': grund, 'h': 'Prüfe mit der Stellenwerttafel oder suche ein Gegenbeispiel.'}


GEN = {'stellenwerte': g_stellen, 'vergleichen_ordnen': g_vgl, 'runden': g_runden, 'bruch_zu_dezimal': g_b2d,
       'dezimal_zu_bruch': g_d2b, 'periodisch': g_per, 'verstehen': g_versteh}

DATEI = datei(E, 'Dezimalzahlen lesen, vergleichen, runden und zwischen Bruch und Dezimalzahl umwandeln – endlich und periodisch.', MERKE,
              [('Stellenwerte und Ordnung', ['stellenwerte', 'vergleichen_ordnen', 'runden']),
               ('Umwandeln', ['bruch_zu_dezimal', 'dezimal_zu_bruch', 'periodisch']),
               ('Verstehen', ['verstehen'])],
              ETAPPEN, GEN,
              offen=['themenliste.json nennt für dieses Thema keinen lehrplan_gym-Wortlaut; Umfang nach „umfang“ gebaut.',
                     'Periodenstrich als kombinierender Überstrich (U+0305) geschrieben, z. B. 0,83̅. Darstellung in der App prüfen; falls unschön, braucht die App eine eigene Periodendarstellung. Periodische Zahlen kommen deshalb nur in Auswahl-Antworten vor (nie als Eingabe).',
                     'Umwandlung periodische Dezimalzahl → Bruch (z. B. 0,3̅ = 1/3) bewusst nur in einfachen Fällen erklärt; das allgemeine Verfahren ist nicht Stoff der 6. Klasse.'])

if __name__ == '__main__':
    schreibe(DATEI)
