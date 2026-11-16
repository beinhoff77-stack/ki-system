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
     'schritte': ['Vergleiche 0,45 und 0,5. Denk an Geld: 0,45 € sind 45 Cent.', '0,5 € sind 50 Cent – hänge eine Null an: 0,5 = 0,50.', '45 Cent sind weniger als 50 Cent, also ⟦0,45 < 0,5⟧.'],
     'fehler': '„0,45 ist größer als 0,5, weil 45 > 5“ ist falsch: Die 5 in 0,5 sind 5 ⟦Zehntel⟧ = 50 Hundertstel. Mehr Ziffern heißt ⟦nicht⟧ größer.',
     'bild': {'typ': 'zahlenstrahl', 'start': 0.4, 'ende': 0.5, 'abschnitte': 10, 'beschriftet': 'anfang_ende', 'pfeil': 5}},
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
     'regel': 'Manche Brüche ergeben eine ⟦periodische Dezimalzahl⟧: Die Ziffern wiederholen sich ohne Ende, z. B. 1/3 = 0,333… Man setzt einen ⟦Strich über die Periode⟧: 0,3̅. Ein vollständig gekürzter Bruch ist genau dann ⟦endlich⟧, wenn sein Nenner nur die Primfaktoren ⟦2 und 5⟧ hat. Warum? 10 = 2 · 5. Nur dann kannst du auf 10, 100 oder 1 000 erweitern. Auf 3 oder 6 geht das nie.',
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


def zk(x, k):
    """Zahl mit genau k Nachkommastellen (Endnullen bleiben stehen), z. B. zk(2.6, 2) = '2,60'."""
    s = zt(x)
    ganz, _, nach = s.partition(',')
    return ganz + (',' + nach.ljust(k, '0') if k else '')


# ---------- 1 Stellenwerte ----------
def tafel(x):
    """Stellenwerttafel E | z | h | t für eine Zahl < 10 mit höchstens 3 Nachkommastellen."""
    return {'typ': 'stellentafel', 'stellen': ['E', 'z', 'h', 't'], 'ziffern': [ziffer(x, k) for k in range(4)]}


def g_tafel(st):
    """Stellenwerttafel lesen (Stufe 1) oder Zahl eintragen und Ziffer ablesen (Stufe 2)."""
    x = Fr(R.randint(1, 9999), 1000)
    if ziffer(x, 3) == 0: return g_tafel(st)
    if st == 1:
        return {'y': 'zahl', 'f': {'text': 'Welche Zahl steht in der Stellenwerttafel?', 'grafik': tafel(x)}, 'o': {'wert': wert(x)},
                'c': ' + '.join(f'{ziffer(x, k)}/{10 ** k}' for k in range(4)),
                'w': f'E = {ziffer(x, 0)}, z = {ziffer(x, 1)}, h = {ziffer(x, 2)}, t = {ziffer(x, 3)}. Komma nach den Einern: {zt(x)}.',
                'h': 'Lies die Ziffern von links nach rechts. Nach den Einern (E) kommt das Komma.'}
    k, name = R.choice([(1, 'z'), (2, 'h'), (3, 't')])
    return {'y': 'zahl', 'f': {'text': f'Trage {zt(x)} in eine Stellenwerttafel mit E, z, h, t ein. Welche Ziffer steht bei {name}?'}, 'o': {'wert': ziffer(x, k)},
            'c': f'({float(x)} * 10**{k}) // 1 % 10', 'w': f'{zt(x)}: E = {ziffer(x, 0)}, z = {ziffer(x, 1)}, h = {ziffer(x, 2)}, t = {ziffer(x, 3)}. Bei {name} steht {ziffer(x, k)}.',
            'h': 'z = Zehntel (1. Stelle nach dem Komma), h = Hundertstel (2.), t = Tausendstel (3.).'}


def g_stellen(st):
    if st in (1, 2) and R.random() < .35:
        return g_tafel(st)
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
                'w': f'Rechts neben der Rundungsstelle steht {d}: {"aufrunden" if d >= 5 else "abrunden"}. {zt(x)} ≈ {zk(r, k)}.', 'h': 'Schau nur auf die Ziffer rechts neben der Rundungsstelle.'}
    if st == 2:
        k = R.choice([1, 2, 2, 3])
        x = zufall_dez(R, 30, k + R.randint(1, 2))
        if R.random() < .3:
            x = Fr(int(x * 10 ** k) // 10 * 10 + 9, 10 ** k) + Fr(R.randint(5, 9), 10 ** (k + 1))
        r = gerundet(x, k)
        d = ziffer(x, k + 1)
        uebertrag = ziffer(x, k) == 9 and d >= 5
        w = f'Rechts neben der {NAMEN[k]}stelle steht {d}: {"aufrunden" if d >= 5 else "abrunden"}. '
        if uebertrag: w += f'9 + 1 = 10, Übertrag: {zt(x)} ≈ {zk(r, k)}.'
        else: w += f'{zt(x)} ≈ {zk(r, k)}.'
        if k > 1 and zk(r, k).endswith('0'):
            w += f' Die Null am Ende bleibt stehen: Sie zeigt, dass auf {NAMEN[k]} gerundet wurde.'
        return {'y': 'zahl', 'f': {'text': f'Runde {zt(x)} auf {NAMEN[k]}.'}, 'o': {'wert': wert(r)}, 'c': c_runden(x, k), 'w': w,
                'h': 'Markiere die Rundungsstelle. Steht rechts daneben 5 oder mehr, wird sie um 1 größer.'}
    art = R.randrange(3)
    if art == 0:
        ware, lo, hi = R.choice([('Ein Liter Benzin', 1600, 1900), ('Ein Liter Diesel', 1550, 1850), ('Eine Kilowattstunde Strom', 300, 400)])
        x = Fr(R.randint(lo, hi), 1000)
        while ziffer(x, 3) == 0: x = Fr(R.randint(lo, hi), 1000)
        r = gerundet(x, 2)
        return {'y': 'zahl', 'f': {'text': f'{ware} kostet {zt(x)} €. Runde auf ganze Cent.'}, 'o': {'wert': wert(r), 'einheit': '€'}, 'c': c_runden(x, 2),
                'w': f'Cent sind Hundertstel Euro. Die Tausendstelziffer ist {ziffer(x, 3)}: {"aufrunden" if ziffer(x, 3) >= 5 else "abrunden"}. {zt(x)} € ≈ {zk(r, 2)} €.',
                'h': 'Ein Cent ist ein Hundertstel Euro. Runde auf Hundertstel.'}
    if art == 1:
        z = R.randint(1, 8)
        g = R.randint(0, 9)
        x = g + Fr(z, 10) + Fr(4, 100) + Fr(R.randint(5, 9), 1000)
        r = gerundet(x, 1)
        falsch = zk(gerundet(gerundet(x, 2), 1), 1)
        return {**wahl(R, zk(r, 1), [falsch, zk(gerundet(x, 2), 2), zk(r + Fr(2, 10), 1)]), 'f': {'text': f'Runde {zt(x)} auf Zehntel.'},
                'w': f'Rechts neben der Zehntelstelle steht 4: abrunden, {zk(r, 1)}. Erst auf Hundertstel und dann auf Zehntel zu runden ({falsch}) ist falsch.',
                'h': 'Nicht in mehreren Schritten runden! Nur die Hundertstelziffer zählt.'}
    g, z = R.randint(1, 9), R.randint(1, 8)
    ziel = g + Fr(z, 10)
    r = zt(ziel - Fr(R.randint(1, 5), 100))
    falsch = [zt(ziel - Fr(R.randint(6, 9), 100)), zt(ziel + Fr(R.randint(5, 9), 100)), zt(ziel + Fr(1, 10) + Fr(R.randint(1, 4), 100))]
    return {**wahl(R, r, falsch), 'f': {'text': f'Welche Zahl ergibt auf Zehntel gerundet {zt(ziel)}?'},
            'w': f'Auf {zt(ziel)} runden alle Zahlen von {zk(ziel - Fr(5, 100), 2)} bis unter {zk(ziel + Fr(5, 100), 2)}. Also {r}.', 'h': 'Runde jede Zahl auf Zehntel und vergleiche.'}


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
        if x.denominator == 1: return g_b2d(3)
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
    if st == 3 and R.random() < .3:
        return per_zu_bruch()
    gross = (st == 2 and R.random() < .35) or (st == 3 and R.random() < .45)
    if st == 3 and not gross:
        # Kürzen um große Faktoren: Nenner nach dem Kürzen 8, 16, 40, 80, 125 …
        x = Fr(R.randint(1, 15), R.choice([8, 16, 40, 80, 125, 200, 250]))
        if x >= 1 or x.denominator in (2, 4, 5, 10, 20, 25, 50, 100, 1000) or len(zt(x).split(',')[1]) > 3: return g_d2b(3)
        k = len(zt(x).split(',')[1])
    else:
        k = {1: 1, 2: R.choice([2, 2, 3]), 3: R.choice([1, 2, 2, 3])}[st]
        x = zufall_dez(R, 0, k)
    g = R.randint(1, 4) if gross else 0
    x = g + x
    zb = f'{int(x * 10 ** k)}/{zt(10 ** k)}'
    if st == 3 and not gross and R.random() < .3:
        r = bruch(x)
        falsch = [f'{int(x * 10 ** k)}/{zt(10 ** (k - 1))}', f'{int(x * 10 ** k)}/{zt(10 ** (k + 1))}', bruch(x * 10) if (x * 10).denominator > 1 else f'{x.denominator}/{x.numerator}']
        falsch = [f for f in falsch if f != r]
        return {**wahl(R, r, falsch), 'f': {'text': f'Welcher Bruch ist gleich {zt(x)}?'},
                'w': f'{zt(x)} = {zb} = {r} (gekürzt mit {int(x * 10 ** k) // x.numerator}).', 'h': 'Schreibe die Zahl als Zehnerbruch (Nenner 10, 100, 1 000) und kürze.'}
    w = f'{k} Nachkommastelle{"n" if k > 1 else ""}: {zt(x)} = {zb}'
    if int(x * 10 ** k) != x.numerator: w += f' = {bruch(x)} (gekürzt mit {int(x * 10 ** k) // x.numerator}).'
    else: w += ' – nicht kürzbar.'
    if gross: w += f' Probe: {x.numerator} : {x.denominator} = {zt(x)}.'
    return luecke(x, f'Schreibe {zt(x)} als vollständig gekürzten Bruch.' + (' Ein Bruch größer als 1 ist erlaubt.' if gross else ''), w,
                  'So viele Nullen im Nenner wie Nachkommastellen. Dann kürzen.' + (' Die Ganzen gehören mit in den Zähler.' if gross else ''), f'{float(x)}')


def per_zu_bruch():
    """Periodische Dezimalzahl → Bruch, nur einfache Fälle mit Nenner 3 oder 9 (Stufe 3, Auswahl)."""
    n = R.choice([3, 9, 9])
    z = R.randint(1, n - 1)
    x = Fr(z, n)
    p = entwicklung(x)[2]
    r = bruch(x)
    falsch = [f'{p}/10', f'{p}{p}/100', f'{p}/9' if bruch(x) != f'{p}/9' else f'{p}/99', f'1/{p}' if p != '1' else '1/10']
    falsch = [f for f in falsch if f != r and Fr(*map(int, f.split('/'))) != x]
    return {**wahl(R, r, falsch), 'f': {'text': f'Welcher Bruch ist gleich {per(x)}?'},
            'w': f'{per(x)} = 0,{p * 4}… Teile {z} durch {n}: {z} : {n} = {per(x)}. Also {per(x)} = {r}. {p}/10 = 0,{p} ist abgebrochen und kleiner.',
            'h': 'Denk an 1/3 = 0,3̅ und 1/9 = 0,1̅. Welcher Bruch ergibt beim Teilen genau diese Periode?'}


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


def per_wert(s):
    """Wert einer geschriebenen (periodischen) Dezimalzahl wie 0,18̅ oder 1,4̅2̅ – zum Prüfen der Ablenker."""
    g, _, nach = s.partition(',')
    vor, per_z, i = '', '', 0
    while i < len(nach):
        c = nach[i]
        if i + 1 < len(nach) and nach[i + 1] == STRICH:
            per_z += c; i += 2
        else:
            assert not per_z, s
            vor += c; i += 1
    x = Fr(int(g)) + (Fr(int(vor), 10 ** len(vor)) if vor else 0)
    if per_z: x += Fr(int(per_z), (10 ** len(per_z) - 1) * 10 ** len(vor))
    return x


def per_falsch(x):
    """Typische Fehlschreibweisen – jede numerisch verschieden vom richtigen Wert."""
    g, v, p = entwicklung(Fr(x))
    out = [f'{g},{(v + p)[:2] or "0"}']                                    # abgebrochen, ohne Strich
    if v: out.append(f'{g},' + ''.join(c + STRICH for c in v + p))        # Strich auch über der Vorperiode
    if len(p) > 1: out.append(f'{g},{v}{p[:-1]}{p[-1]}{STRICH}')           # Strich nur über der letzten Ziffer
    if len(p) > 2: out.append(f'{g},{v}' + ''.join(c + STRICH for c in p[:2]))   # zu kurze Periode
    out.append(f'{g},' + ''.join(c + STRICH for c in str(x.denominator)))  # Nenner als Periode
    if not v and len(p) == 1: out.append(f'{g},{p}{p}')                     # zweimal hingeschrieben
    richtig = per(x)
    return [f for f in dict.fromkeys(out) if f != richtig and per_wert(f) != Fr(x)]


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
                'w': f'Die Periode {entwicklung(x)[2]} hat {len(entwicklung(x)[2])} {"Ziffer" if len(entwicklung(x)[2]) == 1 else "Ziffern"}. Sie wiederholt sich, an der {k}. Stelle steht {ziffer(x, k)}.',
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
            'w': (f'Unter dem Strich steht 1 Ziffer: {entwicklung(x)[2]}.' if len(entwicklung(x)[2]) == 1 else f'Unter dem Strich stehen {len(entwicklung(x)[2])} Ziffern: {entwicklung(x)[2]}.'),
            'h': 'Zähle die Ziffern unter dem Periodenstrich.'}


# ---------- 7 Verstehen ----------
def g_versteh(st):
    a = zufall_dez(R, 9, 1)
    g = R.randint(1, 9)
    if st == 1:
        aussagen = [(f'{zt(a)} und {zt(a)}0 sind gleich groß.', True, f'Ja, {zt(a)} = {zt(a)}0, eine Endnull nach dem Komma ändert den Wert nicht.'),
                    (f'{zt(a)}0 ist größer als {zt(a)}, weil es mehr Ziffern hat.', False, f'Nein, {zt(a)}0 = {zt(a)}. Eine Endnull ändert den Wert nicht.'),
                    (f'{g},{R.randint(11, 19)} ist größer als {g},{R.randint(2, 9)}, weil die Zahl hinter dem Komma größer ist.', False,
                     'Nein, man vergleicht Stelle für Stelle: Bei den Zehnteln hat die zweite Zahl mehr.')]
    elif st == 2:
        x = zufall_dez(R, 20, 1)
        b = Fr(R.randint(1, 9) * 10 + R.randint(1, 9), 100)
        r1 = gerundet(b, 1)
        aussagen = [(f'Zwischen {zt(x)} und {zt(x + Fr(1, 10))} liegt keine andere Dezimalzahl.', False, f'Nein, z. B. {zt(x + Fr(5, 100))} liegt dazwischen.'),
                    (f'{zt(x)} · 10 = {zt(x)}0', False, f'Nein, mal 10 verschiebt das Komma: {zt(x)} · 10 = {zt(x * 10)}.'),
                    (f'{zt(x)} · 10 = {zt(x * 10)}', True, 'Ja, mal 10 verschiebt das Komma um eine Stelle nach rechts.'),
                    ('1/3 = 0,33', False, '1/3 = 0,3̅. 0,33 ist nur gerundet, denn 3 · 0,33 = 0,99.'),
                    (f'{zt(b)} ist kleiner als {zt(b + Fr(1, 10))}.', True, f'Ja, {zt(b + Fr(1, 10))} hat ein Zehntel mehr.'),
                    (f'{zt(b)} auf Zehntel gerundet ergibt {zk(r1, 1)}.', True, f'Ja, rechts neben der Zehntelstelle steht {ziffer(b, 2)}: {"aufrunden" if ziffer(b, 2) >= 5 else "abrunden"}.'),
                    (f'{zt(b)} auf Zehntel gerundet ergibt {zk(r1 + Fr(1, 10) if ziffer(b, 2) < 5 else r1 - Fr(1, 10), 1)}.', False,
                     f'Nein, rechts neben der Zehntelstelle steht {ziffer(b, 2)}: {"aufrunden" if ziffer(b, 2) >= 5 else "abrunden"}, also {zk(r1, 1)}.')]
    else:
        n = R.choice([3, 6, 7, 9, 12, 15])
        x = zufall_dez(R, 9, 2)
        m = R.choice([6, 12, 15, 24, 30, 16, 20, 25, 40, 50])
        e = all(p in (2, 5) for p in primf(m))
        if n in (3, 7, 9):
            beisp = f'Nein, z. B. {2 * n}/{n} = 2 ist endlich. Erst kürzen, dann entscheiden.'
        else:
            beisp = f'Nein, z. B. 3/{n} = {bruch(Fr(3, n))} = {zt(Fr(3, n))} ist endlich. Erst kürzen, dann entscheiden.'
        aussagen = [(f'Jeder Bruch mit dem Nenner {n} ist periodisch.', False, beisp),
                    (f'Zwischen {zt(x)} und {zt(x + Fr(1, 100))} liegt keine andere Dezimalzahl.', False, f'Nein, hänge eine Null an: {zk(x, 3)} und {zk(x + Fr(1, 100), 3)}. Dazwischen liegt z. B. {zt(x + Fr(5, 1000))}.'),
                    (f'Ein vollständig gekürzter Bruch mit dem Nenner {m} ist als Dezimalzahl endlich.', e,
                     f'{m} = {" · ".join(map(str, primf(m)))}. ' + ('Nur 2 und 5, also endlich.' if e else 'Ein anderer Primfaktor als 2 und 5, also periodisch.')),
                    ('Es gibt eine größte Dezimalzahl, die kleiner als 1 ist.', False, 'Nein, zu jeder Zahl findest du eine größere unter 1: 0,9 < 0,99 < 0,999 < …'),
                    (f'Eine Zahl mit drei Nachkommastellen ist immer größer als eine mit einer, z. B. {zt(Fr(R.randint(101, 399), 1000))} > {zt(Fr(R.randint(5, 9), 10))}.', False,
                     'Nein, man vergleicht Stelle für Stelle. Schon bei den Zehnteln ist die zweite Zahl größer.')]
    s_, stimmt, grund = R.choice(aussagen)
    if stimmt and not grund.startswith('Ja'): grund = 'Ja. ' + grund
    if not stimmt and not grund.startswith('Nein'): grund = 'Nein. ' + grund
    gegen = 'Ja, die Aussage stimmt.' if not stimmt else 'Nein, die Aussage ist falsch.'
    return {**wahl(R, grund, [gegen, 'Das kann man nicht entscheiden.'], 3), 'f': {'text': f'Stimmt die Aussage? „{s_}“'},
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
                     'Umwandlung periodische Dezimalzahl → Bruch (z. B. 0,3̅ = 1/3) bewusst nur in einfachen Fällen (Nenner 3 und 9, Auswahl, Stufe 3); das allgemeine Verfahren ist nicht Stoff der 6. Klasse.',
                     'Prüfung schlug für Dezimalzahlen > 1 eine gemischte Zahl (□ □/□) vor. Umgesetzt als unechter Bruch (□/□, z. B. 2,75 = 11/4), weil die App gemischte Zahlen nicht als eigenes Eingabeformat kennt (siehe auch bruch.rechnen).'])

# ---------- KLAR: verständliche Erklärungen (Siebte Runde, Pflicht seit 15.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _klar_kl6.py) – die Aufgaben bleiben wörtlich gleich.
from _klar_kl6 import klar  # noqa: E402

KLAR = {
 'stellenwerte': {
  'einstieg': 'Auf dem Markt legst du Äpfel auf eine Waage. Die Anzeige zeigt 3,472 kg. Vor dem Komma stehen die ganzen Kilogramm, hinter dem Komma die Teile eines Kilogramms – hier 472 Gramm. Jede Ziffer hinter dem Komma hat ihren eigenen Platz und Wert. Diese Plätze heißen ⟦Stellenwerte⟧.',
  'woerter': [['Dezimalzahl', 'eine Zahl mit Komma wie 3,472'],
              ['Nachkommastelle', 'ein Platz hinter dem Komma'],
              ['Stellenwert', 'was eine Ziffer an ihrem Platz wert ist'],
              ['E (Einer)', 'die Stelle direkt vor dem Komma: ganze Kilogramm'],
              ['z (Zehntel)', '1. Stelle nach dem Komma: 1/10, also 0,1 – bei der Waage 100 g'],
              ['h (Hundertstel)', '2. Stelle nach dem Komma: 1/100, also 0,01 – bei der Waage 10 g'],
              ['t (Tausendstel)', '3. Stelle nach dem Komma: 1/1 000, also 0,001 – bei der Waage 1 g'],
              ['Stellenwerttafel', 'eine Tabelle, in der jede Ziffer in die Spalte ihres Stellenwerts kommt']],
  'schritte': ['Trage 3,472 in die Stellenwerttafel ein: E = 3, z = 4, h = 7, t = 2.',
               'Gesucht ist der Wert der Ziffer 7. Sie steht in der zweiten Spalte nach dem Komma, also bei den Hundertsteln.',
               '7 Hundertstel Kilogramm sind 7 · 10 g = 70 g.',
               'Die 7 hat also den Wert ⟦7/100 = 0,07⟧ – und nicht 7.'],
  'regel': 'So liest du eine Dezimalzahl: Nach dem Komma kommen der Reihe nach ⟦Zehntel (z)⟧, ⟦Hundertstel (h)⟧ und ⟦Tausendstel (t)⟧. Der Platz einer Ziffer bestimmt ihren Wert: In 3,472 ist die 4 vier Zehntel, die 7 sieben Hundertstel und die 2 zwei Tausendstel.',
  'fehler': 'Zu sagen, die 7 in 3,472 hat den Wert 7, ist falsch: Dann lägen 7 kg zusätzliche Äpfel auf der Waage statt 70 g. Sie steht an der ⟦Hundertstelstelle⟧ und bedeutet 7 Hundertstel = 0,07.'},
 'vergleichen_ordnen': {
  'einstieg': 'Am Marktstand kostet ein Apfel 0,45 €, eine Birne 0,5 €. Was ist billiger? Mit Cent ist es leicht: 45 Cent gegen 50 Cent. Genauso ordnest du Zahlen mit Komma: Du vergleichst Stelle für Stelle. Das heißt ⟦Dezimalzahlen vergleichen⟧.',
  'woerter': [['Cent', 'ein Hundertstel Euro: 0,01 €'],
              ['Endnull', 'eine Null ganz hinten nach dem Komma; sie ändert den Wert nicht: 0,5 = 0,50'],
              ['< und >', '„ist kleiner als“ und „ist größer als“; die Spitze zeigt auf die kleinere Zahl'],
              ['Zahlenstrahl', 'eine Linie, auf der die Zahlen der Größe nach von links nach rechts liegen']],
  'schritte': ['Vergleiche 0,45 und 0,5. Die beiden Zahlen haben verschieden viele Nachkommastellen.',
               'Hänge an 0,5 eine Endnull an: 0,5 = 0,50. Das sind 50 Cent, und 0,45 sind 45 Cent.',
               'Jetzt vergleichst du Stelle für Stelle: Bei den Zehnteln steht 4 gegen 5.',
               'Weil 4 kleiner als 5 ist, gilt ⟦0,45 < 0,5⟧ – der Apfel ist billiger. Am Zahlenstrahl liegt 0,45 links von 0,5.'],
  'regel': 'So vergleichst du Dezimalzahlen: ⟦Hänge Endnullen an⟧, bis beide gleich viele Nachkommastellen haben. Vergleiche dann ⟦Stelle für Stelle von links⟧: erst die Ganzen, dann die Zehntel, dann die Hundertstel.',
  'fehler': '„0,45 ist größer als 0,5, weil 45 > 5“ ist falsch: Die 5 in 0,5 sind 5 ⟦Zehntel⟧, also 50 Cent – mehr als 45 Cent. Mehr Ziffern heißt ⟦nicht⟧ größer.'},
 'runden': {
  'einstieg': 'Die Waage zeigt 4,368 kg Kartoffeln. So genau will das niemand aufschreiben, „etwa 4,4 kg“ genügt. Du kürzt die Zahl auf weniger Stellen ab und bleibst dabei so nah wie möglich am echten Wert. Das heißt ⟦Runden⟧.',
  'woerter': [['runden', 'eine Zahl auf weniger Stellen kürzen, sodass sie fast gleich bleibt'],
              ['Rundungsstelle', 'die letzte Stelle, die stehen bleiben soll – „auf Zehntel“ heißt: die Zehntelstelle'],
              ['≈', 'bedeutet „ungefähr gleich“'],
              ['abrunden', 'die Rundungsstelle bleibt, alles dahinter fällt weg'],
              ['aufrunden', 'die Rundungsstelle wird um 1 größer, alles dahinter fällt weg']],
  'schritte': ['Runde 4,368 auf Zehntel. Die Zehntelstelle ist die 3 – sie ist die Rundungsstelle.',
               'Schau nur auf die Ziffer direkt rechts daneben: Das ist die 6.',
               '6 ist 5 oder mehr, also rundest du auf: Aus der 3 wird eine 4. Alles dahinter fällt weg.',
               'Ergebnis: 4,368 kg ≈ ⟦4,4 kg⟧.'],
  'regel': 'So rundest du: Markiere die ⟦Rundungsstelle⟧. Schau nur auf die Ziffer ⟦direkt rechts daneben⟧. Bei 0, 1, 2, 3 oder 4 wird ⟦abgerundet⟧, bei 5, 6, 7, 8 oder 9 wird ⟦aufgerundet⟧.',
  'fehler': '2,349 auf Zehntel erst zu 2,35 und dann zu 2,4 zu runden ist falsch: Das Ergebnis rückt dabei Schritt für Schritt vom echten Wert weg. Es zählt nur die Ziffer ⟦direkt rechts⟧ neben der Zehntelstelle, also die 4: ⟦2,3⟧.'},
 'bruch_zu_dezimal': {
  'einstieg': 'In Omas Kuchenrezept steht „3/8 Liter Milch“. Dein Messbecher zeigt aber nur Kommazahlen wie 0,25 l oder 0,5 l an. Du musst also den Bruch in eine Zahl mit Komma übersetzen. Das heißt ⟦einen Bruch in eine Dezimalzahl umwandeln⟧.',
  'woerter': [['umwandeln', 'dieselbe Zahl anders schreiben – ihr Wert bleibt gleich'],
              ['Zehnerbruch', 'ein Bruch mit dem Nenner 10, 100 oder 1 000; er lässt sich sofort mit Komma schreiben'],
              ['erweitern', 'Zähler und Nenner mit derselben Zahl malnehmen'],
              ['l', 'Liter']],
  'schritte': ['Du willst 3/8 als Zehnerbruch schreiben. Suche dafür eine Zahl, mit der 8 malgenommen 1 000 ergibt: 8 · 125 = 1 000.',
               'Erweitere Zähler und Nenner mit 125: 3 · 125 = 375, also 3/8 = 375/1 000.',
               '375 Tausendstel schreibt man mit drei Nachkommastellen: 0,375.',
               'Im Rezept bedeutet das ⟦0,375 l⟧ Milch – also etwas mehr als 0,25 l und weniger als 0,5 l.'],
  'regel': 'So wandelst du einen Bruch um: ⟦Erweitere auf den Nenner 10, 100 oder 1 000⟧ und schreibe die Zahl mit Komma. Geht das nicht, ⟦teile den Zähler durch den Nenner⟧.',
  'fehler': '3/8 = 3,8 ist falsch: Dann bräuchtest du fast 4 Liter Milch für einen Kuchen. Der Bruchstrich ist kein Komma, 3/8 heißt ⟦3 : 8⟧ = 0,375.'},
 'dezimal_zu_bruch': {
  'einstieg': 'An der Kasse bekommst du 0,35 € Wechselgeld, also 35 Cent. Ein Euro hat 100 Cent. Das Wechselgeld ist demnach 35 von 100 Teilen eines Euros. So schreibst du eine Zahl mit Komma ⟦als Bruch⟧.',
  'woerter': [['endliche Dezimalzahl', 'eine Zahl mit Komma, deren Ziffern irgendwann aufhören, z. B. 0,35'],
              ['kürzen', 'Zähler und Nenner durch dieselbe Zahl teilen; der Wert bleibt gleich'],
              ['vollständig gekürzt', 'Zähler und Nenner haben keinen gemeinsamen Teiler außer 1 mehr']],
  'schritte': ['0,35 hat 2 Nachkommastellen. Die letzte Ziffer steht bei den Hundertsteln.',
               'Darum kommt 100 in den Nenner: 0,35 = 35/100 – 35 Cent von 100 Cent.',
               '35 und 100 lassen sich beide durch 5 teilen: 35 : 5 = 7 und 100 : 5 = 20.',
               'Vollständig gekürzt ist 0,35 = ⟦7/20⟧.'],
  'regel': 'So schreibst du eine endliche Dezimalzahl als Bruch: Der Nenner bekommt ⟦so viele Nullen, wie die Zahl Nachkommastellen hat⟧ (10, 100, 1 000 …). Danach ⟦kürzen⟧.',
  'fehler': '0,35 = 35/10 ist falsch: Das wären 35 Zehntel Euro, also 3,50 € – zehnmal so viel Wechselgeld. Zwei Nachkommastellen bedeuten ⟦Hundertstel⟧, also Nenner 100.'},
 'periodisch': {
  'einstieg': 'Sechs Kinder wollen 5 € gerecht teilen. Rechnest du 5 : 6, hört die Rechnung nie auf: 0,8333… Die 3 kommt immer wieder, so lange du auch weiterrechnest. Eine Zahl mit Komma, deren Ziffern sich so ohne Ende wiederholen, heißt ⟦periodische Dezimalzahl⟧.',
  'woerter': [['…', 'die Ziffern gehen immer weiter'],
              ['Periode', 'die Ziffer oder Ziffernfolge, die sich ohne Ende wiederholt'],
              ['Periodenstrich', 'der Strich über der Periode: 0,83̅ heißt 0,8333…'],
              ['Primfaktor', 'eine Primzahl, die in einer Zahl als Faktor steckt: 6 = 2 · 3, also sind 2 und 3 die Primfaktoren von 6'],
              ['endlich', 'die Ziffern nach dem Komma hören irgendwann auf']],
  'schritte': ['Rechne 5 : 6 schriftlich. Es ergibt 0,8 und es bleibt ein Rest.',
               'Ab jetzt bleibt bei jedem Schritt derselbe Rest, darum kommt immer wieder eine 3: 0,8333…',
               'Die 8 kommt nur einmal, ab der zweiten Nachkommastelle wiederholt sich die 3. Die Periode ist also 3.',
               'Mit Periodenstrich: 5/6 = ⟦0,83̅⟧. Jedes Kind bekommt etwa 0,83 €, ein paar Cent bleiben übrig.'],
  'regel': 'So erkennst du periodische Dezimalzahlen: Kürze den Bruch vollständig und zerlege den Nenner in ⟦Primfaktoren⟧. Kommen ⟦nur 2 und 5⟧ vor, ist die Dezimalzahl endlich – denn 10 = 2 · 5, man kann auf 10, 100, 1 000 erweitern. Kommt ein ⟦anderer Primfaktor⟧ vor (z. B. 3), ist sie ⟦periodisch⟧. Die Periode bekommt einen ⟦Strich⟧: 0,3̅.',
  'fehler': '1/3 = 0,3 ist falsch: Drei Kinder mit je 0,30 € hätten zusammen nur 0,90 € statt 1 €. Richtig ist 1/3 = ⟦0,3̅⟧ – die 3 wiederholt sich ohne Ende.'},
 'verstehen': {
  'einstieg': 'Beim Sportfest misst eine Stoppuhr Zehntel- und Hundertstelsekunden. Jemand behauptet: „Zwischen 0,1 s und 0,2 s kann es keine Zeit geben.“ Doch die Uhr zeigt auch 0,15 s an. Ein einziges solches Beispiel genügt, um die Behauptung zu widerlegen. Es heißt ⟦Gegenbeispiel⟧.',
  'woerter': [['s', 'Sekunde'],
              ['Aussage', 'ein Satz, der wahr oder falsch sein kann'],
              ['Gegenbeispiel', 'ein Beispiel, bei dem eine Aussage nicht stimmt; eines genügt'],
              ['widerlegen', 'zeigen, dass etwas falsch ist']],
  'schritte': ['Die Aussage lautet: „Zwischen 0,1 und 0,2 gibt es keine Zahl.“',
               'Hänge an beide Zahlen eine Endnull an: 0,10 und 0,20. Der Wert bleibt gleich.',
               'Jetzt siehst du Hundertstel dazwischen: 0,11, 0,12, … 0,15 … 0,19.',
               '0,15 ist ein Gegenbeispiel, die Aussage ist ⟦falsch⟧.'],
  'regel': 'So prüfst du Aussagen über Dezimalzahlen: Schreibe die Zahlen in die ⟦Stellenwerttafel⟧ oder hänge Endnullen an und vergleiche Stelle für Stelle. Suche ein ⟦Gegenbeispiel⟧ – eines genügt, um eine Aussage zu widerlegen.',
  'fehler': '„3,14 ist größer als 3,2, weil 14 > 2“ ist falsch: Ein Weitsprung von 3,14 m ist kürzer als einer von 3,2 m = 3,20 m. Man vergleicht ⟦Stelle für Stelle⟧: Zehntel 1 < 2, also 3,14 < 3,2.'},
}

klar(DATEI, KLAR)


if __name__ == '__main__':
    schreibe(DATEI)
