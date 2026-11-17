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

# ---------- KARTEN: Lernkarten nach dem neuen Muster (Achte Runde, Vorgabe 16.11., Paket U6) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl6.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl6 import umbau  # noqa: E402

KARTEN = {
 'stellenwerte': {
  'einstieg': 'Die Waage auf dem Markt zeigt 3,472 kg Äpfel. Vor dem Komma stehen ganze Kilogramm, dahinter Teile davon. Jede Ziffer hat einen ⟦Stellenwert⟧.',
  'woerter': [['Stellenwert', 'wie viel eine Ziffer an ihrem Platz wert ist'],
              ['Stellenwerttafel', 'eine Tabelle mit einer Spalte für jede Stelle: E, z, h, t'],
              ['Hundertstel', 'die 2. Stelle nach dem Komma: 1/100']],
  'bild': {'typ': 'stellentafel', 'stellen': ['E', 'z', 'h', 't'], 'ziffern': [3, 4, 7, 2]},
  'schritte': [{'text': 'Trage 3,472 in die Stellenwerttafel ein.'},
               {'text': 'Die 7 steht in der Spalte h, bei den Hundertsteln.', 'bild': {'markiert': 2}},
               {'text': 'Die 7 ist also ⟦7/100 = 0,07⟧ kg wert. Das sind 70 g.'}],
  'fehler': 'Die 7 ist nicht 7 wert. Sonst lägen 7 kg mehr auf der Waage. Sie bedeutet 7 Hundertstel, also 70 g.',
  'regel': 'Der ⟦Platz⟧ bestimmt den Wert einer Ziffer. Nach dem Komma kommen Zehntel, Hundertstel und Tausendstel.'},
 'vergleichen_ordnen': {
  'einstieg': 'Ein Apfel kostet 0,45 €, eine Birne 0,5 €. In Cent ist es leicht: 45 gegen 50 Cent. So kannst du ⟦Dezimalzahlen vergleichen⟧.',
  'woerter': [['Dezimalzahl', 'eine Zahl mit Komma, z. B. 0,45'],
              ['Endnull', 'eine 0 ganz hinten nach dem Komma; sie ändert den Wert nicht']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0.4, 'ende': 0.5, 'abschnitte': 10, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': 'Hänge an 0,5 eine Endnull an: 0,5 = 0,50. Das sind 50 Cent.'},
               {'text': 'Vergleiche bei den Zehnteln: 4 gegen 5.'},
               {'text': '4 ist kleiner als 5, also ⟦0,45 < 0,5⟧. Der Apfel ist billiger.',
                'bild': {'punkte': [{'wert': 0.45, 'name': 'Apfel'}, {'wert': 0.5, 'name': 'Birne'}]}}],
  'fehler': '„0,45 ist größer, weil 45 > 5“ ist falsch. 0,5 sind 5 Zehntel, also 50 Cent.',
  'regel': 'Fülle mit ⟦Endnullen⟧ auf und vergleiche von links. Erst die Ganzen, dann Zehntel, dann Hundertstel.'},
 'runden': {
  'einstieg': 'Die Waage zeigt 4,368 kg Kartoffeln. So genau will das niemand aufschreiben, „etwa 4,4 kg“ genügt. Das heißt ⟦Runden⟧.',
  'woerter': [['Runden', 'eine Zahl auf weniger Stellen abkürzen, möglichst nah am echten Wert'],
              ['Rundungsstelle', 'die letzte Stelle, die stehen bleibt']],
  'bild': {'typ': 'zahlenstrahl', 'start': 4.3, 'ende': 4.4, 'abschnitte': 10, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': 'Runde auf Zehntel: Die Rundungsstelle ist die 3.'},
               {'text': 'Rechts daneben steht eine 6. Das ist 5 oder mehr, also aufrunden.'},
               {'text': '4,368 liegt näher an 4,4 als an 4,3: ⟦4,4 kg⟧.',
                'bild': {'punkte': [{'wert': 4.368, 'name': '4,368', 'zahl': False}], 'bereich': {'von': 4.35, 'bis': 4.4}}}],
  'fehler': '2,349 erst zu 2,35 und dann zu 2,4 runden ist falsch. Es zählt nur die Ziffer direkt rechts: 2,3.',
  'fehler_bild': {'typ': 'zahlenstrahl', 'start': 2.3, 'ende': 2.4, 'abschnitte': 10, 'beschriftet': 'anfang_ende',
                  'punkte': [{'wert': 2.349, 'name': '2,349', 'zahl': False}], 'bereich': {'von': 2.3, 'bis': 2.35}},
  'regel': 'Schau nur auf die Ziffer ⟦direkt rechts⟧ der Rundungsstelle. Bei 0 bis 4 abrunden, bei 5 bis 9 aufrunden.'},
 'bruch_zu_dezimal': {
  'einstieg': 'Im Rezept steht 3/8 Liter Milch. Dein Messbecher zeigt aber nur Kommazahlen. Du musst den Bruch ⟦in eine Dezimalzahl umwandeln⟧.',
  'woerter': [['Dezimalzahl', 'eine Zahl mit Komma, z. B. 0,375'],
              ['Zehnerbruch', 'ein Bruch mit dem Nenner 10, 100 oder 1 000']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 1, 'abschnitte': 8, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': '3/8 liegt beim 3. von 8 Strichen.', 'bild': {'punkte': [{'wert': 0.375, 'name': '3/8', 'zahl': False}]}},
               {'text': 'Mach daraus einen Zehnerbruch: 8 · 125 = 1 000.'},
               {'text': 'Erweitere mit 125: 3/8 = 375/1 000.'},
               {'text': '375 Tausendstel sind ⟦0,375⟧ Liter.', 'bild': {'punkte': [{'wert': 0.375, 'name': '3/8 = 0,375', 'zahl': False}]}}],
  'fehler': '3/8 = 3,8 ist falsch: Dann bräuchtest du fast 4 Liter Milch. Der Bruchstrich bedeutet 3 : 8.',
  'fehler_bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 4, 'abschnitte': 4, 'beschriftet': 'anfang_ende',
                  'punkte': [{'wert': 0.375, 'name': '3/8', 'zahl': False}, {'wert': 3.8, 'name': '3,8?', 'zahl': False}]},
  'regel': 'Erweitere auf ⟦10, 100 oder 1 000⟧ und schreibe mit Komma. Geht das nicht, teile den Zähler durch den Nenner.'},
 'dezimal_zu_bruch': {
  'einstieg': 'An der Kasse bekommst du 0,35 € zurück, also 35 Cent. Ein Euro hat 100 Cent. So schreibst du die Zahl ⟦als Bruch⟧: 35/100.',
  'woerter': [['Nachkommastelle', 'eine Ziffer hinter dem Komma']],
  'bild': {'typ': 'stellentafel', 'stellen': ['E', 'z', 'h'], 'ziffern': [0, 3, 5]},
  'schritte': [{'text': '0,35 hat 2 Nachkommastellen. Die 5 steht bei den Hundertsteln.', 'bild': {'markiert': 2}},
               {'text': 'Also kommt 100 in den Nenner: 0,35 = 35/100.'},
               {'text': 'Kürze durch 5: 35/100 = ⟦7/20⟧.',
                'bild': {'typ': 'bruchstreifen', 'teile': 20, 'gefaerbt': 7, 'teil_text': '7/20', 'ganzes': '1 € = 100 Cent'}}],
  'fehler': '0,35 = 35/10 ist falsch: Das wären 3,50 €, zehnmal zu viel. Zwei Nachkommastellen heißen Nenner 100.',
  'regel': 'Der Nenner bekommt ⟦so viele Nullen⟧ wie Nachkommastellen. Danach kürzt du.'},
 'periodisch': {
  'einstieg': 'Sechs Kinder teilen 5 € gerecht. Rechnest du 5 : 6, kommt 0,8333… heraus, ohne Ende. Solche Dezimalzahlen heißen ⟦periodisch⟧.',
  'woerter': [['periodisch', 'eine Ziffer oder Ziffernfolge wiederholt sich ohne Ende'],
              ['Periode', 'die Ziffern, die sich immer wiederholen'],
              ['Periodenstrich', 'ein Strich über der Periode: 0,83̅']],
  'bild': {'typ': 'tabelle', 'kopf': ['Rechnung', 'Ziffer', 'Rest'], 'zeilen': [['5 : 6', '0', '5']]},
  'schritte': [{'text': '5 : 6 = 0, Rest 5. Dann 50 : 6 = 8, Rest 2.',
                'bild': {'zeilen': [['5 : 6', '0', '5'], ['50 : 6', '8', '2']]}},
               {'text': 'Dann 20 : 6 = 3, Rest 2. Derselbe Rest kommt immer wieder.',
                'bild': {'zeilen': [['5 : 6', '0', '5'], ['50 : 6', '8', '2'], ['20 : 6', '3', '2'], ['20 : 6', '3', '2']]}},
               {'text': 'Die 3 ist die Periode. Mit Periodenstrich: 5/6 = ⟦0,83̅⟧.'}],
  'fehler': '1/3 = 0,3 ist falsch: Drei Kinder mit je 0,30 € hätten nur 0,90 €. Richtig ist 0,3̅.',
  'regel': 'Wiederholen sich Ziffern ohne Ende, ist die Zahl ⟦periodisch⟧. Das passiert, wenn der gekürzte Nenner andere Primfaktoren als 2 und 5 hat.'},
 'verstehen': {
  'einstieg': 'Jemand behauptet: „Zwischen 0,1 s und 0,2 s gibt es keine Zeit“. Doch die Stoppuhr zeigt 0,15 s. Ein Beispiel gegen eine Aussage heißt ⟦Gegenbeispiel⟧.',
  'woerter': [['Gegenbeispiel', 'ein Beispiel, das zeigt: Die Aussage stimmt nicht']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0.1, 'ende': 0.2, 'abschnitte': 10, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': 'Hänge Endnullen an: 0,1 = 0,10 und 0,2 = 0,20.'},
               {'text': 'Dazwischen liegen 0,11, 0,12 und so weiter bis 0,19.', 'bild': {'beschriftet': 'alle'}},
               {'text': '0,15 ist ein Gegenbeispiel. Die Aussage ist ⟦falsch⟧.',
                'bild': {'beschriftet': 'anfang_ende', 'punkte': [{'wert': 0.15, 'name': '0,15 s', 'zahl': False}]}}],
  'fehler': '„3,14 ist größer als 3,2, weil 14 > 2“ ist falsch. Bei den Zehnteln gilt 1 < 2, also ist 3,14 kleiner.',
  'fehler_bild': {'typ': 'zahlenstrahl', 'start': 3.1, 'ende': 3.2, 'abschnitte': 10, 'beschriftet': 'anfang_ende',
                  'punkte': [{'wert': 3.14, 'name': '3,14', 'zahl': False}]},
  'regel': 'Prüfe Aussagen ⟦Stelle für Stelle⟧. Ein Gegenbeispiel genügt, um eine Aussage zu widerlegen.'},
}

umbau(DATEI, KARTEN)



# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl6): je Lernkarte 2 Übungen Stufe 2 + 4 Übungen Stufe 3 ----------
# Läuft nach allen bisherigen Aufgaben mit eigenem Zufallsstart; die bisherigen Aufgaben bleiben unverändert.
# Prüfungsvorbilder: Jahrgangsstufentest Realschule Jgst. 6 (ISB) 2023 Nr. 6 (größtmögliche Zahl für einen Platzhalter),
# 2019 Nr. 6 (markierte Zahl am Zahlenstrahl), 2019 Nr. 19 und 2024 Nr. 5 (Runden begründen / richtig gerundet auswählen);
# Bayerischer Mathematik-Test Jgst. 8 (ISB) 2023 Aufg. 5a (Restanteil aus gemischten Angaben), 2024 Aufg. 3b („ein Drittel“ genau prüfen),
# 2021 Aufg. 6c (passenden Bruch auswählen).
from _schwer_kl6 import ergaenzen, zahl, wahl, luecken, anteil, mark  # noqa: E402


def _ue(z):
    """Ziffernfolge mit Periodenstrich (wie in den bisherigen Aufgaben: kombinierender Überstrich)."""
    return ''.join(c + '\u0305' for c in z)


def _dz():
    return {
        'stellenwerte': [
            (2, lambda R: wahl(R, 'Welchen Wert hat die Ziffer 7 in 3,072?', '7 Hundertstel', ['7 Zehntel', '7 Tausendstel', '70'],
                               'Zähle die Stellen nach dem Komma: Zehntel, Hundertstel, Tausendstel.',
                               '3,072: 0 Zehntel, 7 Hundertstel, 2 Tausendstel.')),
            (2, lambda R: zahl('Schreibe als Dezimalzahl: 4 Zehntel und 23 Tausendstel.', Fr('0.423'), '4/10 + 23/1000',
                               '23 Tausendstel sind 2 Hundertstel und 3 Tausendstel.', '0,4 + 0,023 = 0,423.')),
            (3, lambda R: zahl('Bilde mit den Ziffern 3, 8, 1 und 6 (jede genau einmal) die größte Dezimalzahl, die kleiner als 10 ist.', Fr('8.631'),
                               '8 + 6/10 + 3/100 + 1/1000', 'Kleiner als 10 heißt: genau eine Ziffer vor dem Komma. Welche Ziffer gehört nach vorn?',
                               'Vor das Komma kommt die größte Ziffer 8, danach absteigend 6, 3, 1: 8,631.')),
            (3, lambda R: zahl('Wie viele Hundertstel sind 2,4?', 240, '2.4 * 100', 'Ein Ganzes hat 100 Hundertstel, ein Zehntel hat 10 Hundertstel.',
                               '2 Ganze = 200 Hundertstel, 4 Zehntel = 40 Hundertstel. Zusammen 240 Hundertstel.')),
            (3, lambda R: zahl('Ich bin eine Dezimalzahl zwischen 5 und 6 mit genau zwei Nachkommastellen. Meine Zehntelziffer ist doppelt so groß '
                               'wie meine Hundertstelziffer. Zusammen ergeben die beiden Ziffern 9. Wer bin ich?', Fr('5.63'), '5 + 6/10 + 3/100',
                               'Die Zehntelziffer zählt wie zwei Hundertstelziffern. Zusammen sind es also drei gleiche Teile von 9.',
                               'Hundertstel h, Zehntel 2 · h. h + 2 · h = 9, also h = 3 und Zehntel 6. Die Zahl ist 5,63.')),
            (3, lambda R: zahl('Ein Kind schreibt 3 + 4/100 als 3,4. Wie heißt die Zahl richtig?', Fr('3.04'), '3 + 4/100',
                               '4/100 sind 4 Hundertstel. An welcher Stelle nach dem Komma stehen Hundertstel?',
                               '4 Hundertstel stehen an der 2. Stelle nach dem Komma, die Zehntelstelle ist 0: 3,04. (3,4 wären 4 Zehntel.)')),
        ],
        'vergleichen_ordnen': [
            (2, lambda R: wahl(R, 'Ordne 0,5; 0,45; 0,405 und 0,54, mit der kleinsten Zahl zuerst. Welche Zahl steht an zweiter Stelle?', '0,45',
                               ['0,405', '0,5', '0,54'], 'Fülle mit Endnullen auf: 0,500; 0,450; 0,405; 0,540.',
                               '0,405 < 0,450 < 0,500 < 0,540. An zweiter Stelle steht 0,45.')),
            (2, lambda R: mark('Markiere 0,35 am Zahlenstrahl (von 0 bis 0,5, 10 gleiche Teile).', 0, Fr('0.5'), 10, 7,
                               'Wie lang ist ein Teil? 0,5 : 10 = ?', 'Ein Teil ist 0,05 lang. 0,35 : 0,05 = 7, also der 7. Strich.', Fr('0.35'))),
            (3, lambda R: zahl('Welche Ziffer darf höchstens für □ stehen, damit 4,□7 < 4,58 gilt?', 5, '5',
                               'Probiere die Ziffern 5 und 6 aus und vergleiche Stelle für Stelle.',
                               '4,57 < 4,58 stimmt. 4,67 ist schon größer als 4,58. Also höchstens 5.')),
            (3, lambda R: zahl('Wie viele Dezimalzahlen mit genau zwei Nachkommastellen liegen zwischen 3,4 und 3,5? (Die Grenzen zählen nicht.)', 9, '49 - 41 + 1',
                               'Schreibe sie auf: 3,41; 3,42; …', 'Es sind 3,41 bis 3,49, also 9 Zahlen. (3,40 und 3,50 sind die Grenzen.)')),
            (3, lambda R: mark('Markiere 2,35 am Zahlenstrahl (von 2,2 bis 2,6, 8 gleiche Teile).', Fr('2.2'), Fr('2.6'), 8, 3,
                               'Die Strecke ist 0,4 lang. Wie lang ist ein Teil?', 'Ein Teil ist 0,4 : 8 = 0,05 lang. Von 2,2 bis 2,35 sind es 0,15, also 3 Teile.', Fr('2.35'))),
            (3, lambda R: wahl(R, 'Ein Kind ordnet so: 0,8 < 0,75 < 0,125, „weil mehr Stellen eine kleinere Zahl bedeuten“. Wie ist es richtig?',
                               '0,125 < 0,75 < 0,8', ['Die Reihenfolge stimmt.', '0,75 < 0,8 < 0,125', '0,8 < 0,125 < 0,75'],
                               'Fülle auf drei Nachkommastellen auf und vergleiche.', '0,800; 0,750; 0,125. Richtig ist 0,125 < 0,75 < 0,8.')),
        ],
        'runden': [
            (2, lambda R: zahl('Runde 0,0738 auf Tausendstel.', Fr('0.074'), 'round(0.0738, 3)', 'Die Tausendstelstelle ist die 3. Stelle nach dem Komma.',
                               'Rechts von der Tausendstelziffer 3 steht 8, also aufrunden: 0,074.')),
            (2, lambda R: zahl('Runde 12,345 auf Zehntel.', Fr('12.3'), '123 / 10', 'Schau nur auf die Ziffer direkt rechts von der Zehntelstelle.',
                               'Rechts von der 3 steht 4: abrunden. 12,3. Die 5 weiter hinten spielt keine Rolle.')),
            (3, lambda R: zahl('Runde 7,996 auf Hundertstel.', 8, '800 / 100', 'Die Hundertstelziffer 9 wird um 1 größer. Was passiert dann mit den Ziffern davor?',
                               'Rechts von der Hundertstelziffer steht 6: aufrunden. 7,99 + 0,01 = 8,00.')),
            (3, lambda R: zahl('Ein Kind rundet 2,449 erst auf Hundertstel (2,45) und dann auf Zehntel (2,5). Was ergibt richtiges Runden von 2,449 auf Zehntel?',
                               Fr('2.4'), '24 / 10', 'Runde in einem Schritt: Welche Ziffer steht direkt rechts von der Zehntelstelle?',
                               'Rechts von der Zehntelziffer 4 steht 4: abrunden, also 2,4. Zweimal runden hintereinander verfälscht das Ergebnis.')),
            (3, lambda R: zahl('Eine Zahl mit genau zwei Nachkommastellen ergibt auf Zehntel gerundet 6,3. Welche ist die größte solche Zahl?', Fr('6.34'), '634 / 100',
                               'Bis zu welcher Hundertstelziffer wird noch abgerundet?', 'Bei 0 bis 4 wird abgerundet. 6,34 → 6,3, aber 6,35 → 6,4. Die größte ist 6,34.')),
            (3, lambda R: zahl('3 Hefte kosten zusammen 4,00 €. Wie viel kostet ein Heft, auf ganze Cent gerundet?', Fr('1.33'), 'round(4 / 3, 2)',
                               'Teile 4 € durch 3 und runde auf zwei Nachkommastellen.', '4 : 3 = 1,333… €. Rechts von der Hundertstelstelle steht 3: abrunden, 1,33 €.',
                               einheit='€')),
        ],
        'bruch_zu_dezimal': [
            (2, lambda R: zahl('Schreibe 13/50 als Dezimalzahl.', Fr('0.26'), '13 / 50', 'Erweitere auf den Nenner 100.', '13/50 = 26/100 = 0,26.')),
            (2, lambda R: zahl('Schreibe die gemischte Zahl 2 3/4 als Dezimalzahl.', Fr('2.75'), '2 + 3/4', '2 3/4 heißt 2 + 3/4.', '3/4 = 75/100 = 0,75. 2 + 0,75 = 2,75.')),
            (3, lambda R: zahl('Ein Teig besteht zu 1/4 aus Mehl, zu 0,3 aus Zucker, zu 1/5 aus Butter, der Rest sind Eier. '
                               'Welcher Anteil sind Eier? Gib ihn als Dezimalzahl an.', Fr('0.25'), '1 - 1/4 - 0.3 - 1/5',
                               'Schreibe alle Anteile als Dezimalzahl. Alles zusammen ist 1.', '1/4 = 0,25 und 1/5 = 0,2. 1 − 0,25 − 0,3 − 0,2 = 0,25.')),
            (3, lambda R: zahl('Welche Zahl ist größer, 5/8 oder 0,6? Gib den Unterschied als Dezimalzahl an.', Fr('0.025'), '5/8 - 0.6',
                               'Schreibe 5/8 als Dezimalzahl (Achtel: 1/8 = 0,125).', '5/8 = 0,625. 0,625 − 0,6 = 0,025. 5/8 ist größer.')),
            (3, lambda R: zahl('Für welche Zahl n von 1 bis 10 ist 3/n eine Dezimalzahl mit genau drei Nachkommastellen?', 8, '8',
                               'Probiere alle n durch. Welche Nenner geben endliche Dezimalzahlen?',
                               '3/2 = 1,5; 3/4 = 0,75; 3/5 = 0,6; 3/6 = 0,5; 3/10 = 0,3; 3/7 und 3/9 sind periodisch. Nur 3/8 = 0,375 hat drei Nachkommastellen.')),
            (3, lambda R: zahl('Ein Kind schreibt 3/4 = 3,4. Wie heißt die Dezimalzahl richtig?', Fr('0.75'), '3 / 4',
                               'Ist 3/4 größer oder kleiner als 1? Und 3,4?', '3/4 ist kleiner als 1. Erweitern: 3/4 = 75/100 = 0,75. Der Bruchstrich ist kein Komma.')),
        ],
        'dezimal_zu_bruch': [
            (2, lambda R: anteil('Schreibe 0,85 als vollständig gekürzten Bruch.', 85, 100, 'Zwei Nachkommastellen: Nenner 100.', '0,85 = 85/100. Durch 5 kürzen: 17/20.')),
            (2, lambda R: anteil('Schreibe 2,4 als vollständig gekürzten Bruch. Ein Bruch größer als 1 ist erlaubt.', 24, 10, 'Eine Nachkommastelle: Nenner 10.',
                                 '2,4 = 24/10. Durch 2 kürzen: 12/5.')),
            (3, lambda R: anteil('Schreibe 0,125 + 0,5 als vollständig gekürzten Bruch.', 625, 1000, 'Rechne zuerst die Summe aus.',
                                 '0,125 + 0,5 = 0,625 = 625/1 000. Durch 125 kürzen: 5/8.')),
            (3, lambda R: wahl(R, 'Welcher Bruchteil eines Kilogramms sind 0,04 kg?', '1/25', ['4/10', '1/4', '4/1 000'],
                               'Zwei Nachkommastellen: Nenner 100. Dann kürzen.', '0,04 = 4/100 = 1/25. 4/10 wäre 0,4 und 1/4 wäre 0,25.')),
            (3, lambda R: zahl('Für □ soll eine Ziffer eingesetzt werden, sodass 0,□5 vollständig gekürzt den Nenner 4 hat. Wie viele Ziffern sind möglich?', 2, '2',
                               'Welche Brüche mit Nenner 4 haben zwei Nachkommastellen und enden auf 5?',
                               '1/4 = 0,25 und 3/4 = 0,75 passen. 0,05, 0,15, 0,35 … haben gekürzt den Nenner 20. Also 2 Ziffern (2 und 7).')),
            (3, lambda R: anteil('Ein Kind schreibt 0,07 = 7/10. Wie heißt der Bruch richtig?', 7, 100, 'Wie viele Nachkommastellen hat 0,07?',
                                 '0,07 hat zwei Nachkommastellen, also 7 Hundertstel: 7/100. 7/10 wäre 0,7.')),
        ],
        'periodisch': [
            (2, lambda R: wahl(R, 'Welche Dezimalzahl ist gleich 5/6?', '0,8' + _ue('3'), ['0,' + _ue('83'), '0,83', '0,' + _ue('56')],
                               'Teile 5 durch 6 schriftlich. Welche Ziffer wiederholt sich?', '5 : 6 = 0,8333… Nur die 3 wiederholt sich: 0,83 mit Strich über der 3.')),
            (2, lambda R: wahl(R, 'Ist 7/40 als Dezimalzahl endlich oder periodisch?', 'endlich, denn 40 = 2 · 2 · 2 · 5',
                               ['periodisch, denn 7 ist eine Primzahl', 'periodisch, denn 40 ist nicht durch 3 teilbar'],
                               'Zerlege den Nenner in Primfaktoren.', '40 = 2 · 2 · 2 · 5, nur 2 und 5. Also endlich: 7/40 = 175/1 000 = 0,175.', n=3)),
            (3, lambda R: zahl('2/7 = 0,' + _ue('285714') + '. Welche Ziffer steht an der 100. Nachkommastelle?', 7, '(2 * 10 ** 100 // 7) % 10',
                               'Die Periode hat 6 Ziffern. Wie oft passt 6 in 100, und was bleibt übrig?',
                               '100 = 16 · 6 + 4. Nach 16 vollen Perioden kommt die 4. Ziffer der Periode 285714, das ist 7.')),
            (3, lambda R: wahl(R, 'Welche Zahl ist größer: 0,' + _ue('3') + ' oder 0,33?', '0,' + _ue('3'), ['0,33', 'Beide sind gleich groß'],
                               'Schreibe beide Zahlen mit vier Nachkommastellen.', '0,' + _ue('3') + ' = 0,3333… und 0,33 = 0,3300. Also ist 0,' + _ue('3') + ' größer.', n=3)),
            (3, lambda R: zahl('Wie viele der Brüche 1/2, 1/3, 1/4, …, 1/10 sind periodische Dezimalzahlen?', 4, '9 - 5',
                               'Periodisch wird es, wenn der Nenner einen anderen Primfaktor als 2 und 5 hat.',
                               'Die Nenner 3, 6, 7 und 9 haben den Primfaktor 3 oder 7: 4 Brüche. 1/2, 1/4, 1/5, 1/8, 1/10 sind endlich.')),
            (3, lambda R: wahl(R, 'Ein Kind sagt: 1/6 = 0,' + _ue('16') + '. Was stimmt?', 'Falsch: 1/6 = 0,1' + _ue('6') + ' – nur die 6 wiederholt sich.',
                               ['Richtig.', 'Falsch: 1/6 = 0,16.', 'Falsch: 1/6 = 0,' + _ue('6') + '.'],
                               'Teile 1 durch 6 schriftlich und schau, welche Ziffern sich wiederholen.',
                               '1 : 6 = 0,1666… Die 1 kommt nur einmal, danach wiederholt sich die 6.')),
        ],
        'verstehen': [
            (2, lambda R: wahl(R, 'Stimmt die Aussage? „0,5 ist dasselbe wie 1/5.“', 'Nein: 0,5 = 5/10 = 1/2, aber 1/5 = 0,2.',
                               ['Ja, beide haben eine 5.', 'Das kann man nicht entscheiden.'], 'Schreibe 0,5 als Bruch.',
                               '0,5 sind 5 Zehntel = 1/2. 1/5 = 2/10 = 0,2.', n=3)),
            (2, lambda R: wahl(R, 'Stimmt die Aussage? „3,05 und 3,5 sind gleich groß, denn die Null zählt nicht.“',
                               'Nein: 3,05 hat 0 Zehntel, 3,5 hat 5 Zehntel.', ['Ja, Nullen ändern nie etwas.', 'Das kann man nicht entscheiden.'],
                               'Eine Null in der Mitte ist keine Endnull.', 'Endnullen nach dem Komma ändern nichts (3,5 = 3,50). Die Null in 3,05 ist keine Endnull: 3,05 < 3,50.', n=3)),
            (3, lambda R: wahl(R, 'Stimmt die Aussage? „0,3 ist genau ein Drittel.“', 'Nein: 1/3 = 0,' + _ue('3') + ' ist etwas größer als 0,3.',
                               ['Ja, 0,3 = 1/3.', 'Nein: 1/3 = 0,03.', 'Nein: 1/3 ist kleiner als 0,3.'],
                               'Teile 1 durch 3.', '1 : 3 = 0,333… Das ist mehr als 0,3 = 3/10. 0,3 ist nur ein gerundeter Wert.')),
            (3, lambda R: wahl(R, 'Stimmt die Aussage? „Jeder Bruch mit dem Nenner 15 ist periodisch.“', 'Nein: 3/15 = 1/5 = 0,2 ist endlich.',
                               ['Ja, denn 15 = 3 · 5.', 'Ja, denn 15 ist ungerade.', 'Nein: Jeder Bruch mit dem Nenner 15 ist endlich.'],
                               'Kürze zuerst. Probiere z. B. 3/15 oder 6/15.', '3/15 = 1/5 = 0,2 ist endlich. Erst nach dem Kürzen entscheidet der Nenner. 1/15 dagegen ist periodisch.')),
            (3, lambda R: wahl(R, 'Ein Kind rundet 5,96 auf Zehntel und schreibt 5,10. Was ist richtig?', '6,0', ['5,10', '5,9', '5,1'],
                               'Rechts von der Zehntelziffer 9 steht 6: aufrunden. Was ist 5,9 + 0,1?',
                               'Aufrunden: Aus 9 Zehnteln werden 10 Zehntel = 1 Ganzes. 5,9 + 0,1 = 6,0.')),
            (3, lambda R: wahl(R, 'Ein Kind sagt: „Hänge ich an eine Zahl hinten eine 0 an, wird sie 10-mal so groß.“ Stimmt das?',
                               'Nur bei ganzen Zahlen: 25 → 250. Bei 2,5 → 2,50 bleibt der Wert gleich.',
                               ['Ja, immer.', 'Nein, nie.', 'Nur bei Dezimalzahlen: 2,5 → 2,50 ist 10-mal so groß.'],
                               'Probiere mit 25 und mit 2,5.', '25 wird zu 250 (10-mal so groß). 2,5 wird zu 2,50 – eine Endnull nach dem Komma ändert nichts.')),
        ],
    }


ergaenzen(DATEI, _dz(), seed=6022)


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('bruch.dezimal', 13_6_3)
# c) Textfehler: 0,37 hat nur zwei Nachkommastellen (Beispiel passt nicht zur Aussage)
BF.ersetze('verstehen', 'Stimmt die Aussage? „Eine Zahl mit drei Nachkommastellen ist immer größer als eine mit einer, z. B. 0,37 > 0,8.“', BF.A(
    'Stimmt die Aussage? „Eine Zahl mit drei Nachkommastellen ist immer größer als eine mit einer, z. B. 0,375 > 0,8.“',
    'Nein, man vergleicht Stelle für Stelle. Schon bei den Zehnteln ist die zweite Zahl größer.',
    ['Das kann man nicht entscheiden.', 'Ja, die Aussage stimmt.'],
    'Nein. 0,375 hat 3 Zehntel, 0,8 hat 8 Zehntel: 0,375 < 0,8. Die Zahl der Nachkommastellen sagt nichts über die Größe.',
    'Prüfe mit der Stellenwerttafel oder suche ein Gegenbeispiel.'))
# d) enthält keinen Bruch, passt nicht zur Lernkarte „Bruch → Dezimalzahl“
BF.ersetze('bruch_zu_dezimal', 'Berechne 1 + 0,5 und gib das Ergebnis als Dezimalzahl an.', BF.Z(
    'Berechne 3/4 + 0,5 und gib das Ergebnis als Dezimalzahl an.', 1.25, '3/4 + 0.5', '3/4 = 0,75. 0,75 + 0,5 = 1,25.',
    'Wandle den Bruch zuerst in eine Dezimalzahl um.'))
BF.ersetze('bruch_zu_dezimal', 'Berechne 1 + 0,4 und gib das Ergebnis als Dezimalzahl an.', BF.Z(
    'Berechne 2/5 + 1,4 und gib das Ergebnis als Dezimalzahl an.', 1.8, '2/5 + 1.4', '2/5 = 4/10 = 0,4. 0,4 + 1,4 = 1,8.',
    'Wandle den Bruch zuerst in eine Dezimalzahl um.'))
# a) schriftliche Division mit Periode → Stufe 2
BF.stufe('periodisch', 'Welche Dezimalzahl ist gleich 4/11?', 2)
# a) Standardform → Stufe 2
for _t in ['5 + 9/100 + 7/1 000', '6 + 7/100 + 1/1 000', '9 + 9/100 + 7/1 000', '9 + 7/100 + 2/1 000']:
    BF.stufe('stellenwerte', f'Schreibe als Dezimalzahl: {_t}', 2)
BF.nicht_umgesetzt('runden „Runde 2,596 auf Hundertstel“ (Test 30,096): Lösung als 2,6 bzw. 30,1 gespeichert',
                   'Die App wertet 2,60 = 2,6; der Lösungsweg nennt die Endnull bereits („2,596 ≈ 2,60. Die Null am Ende bleibt stehen …“).')

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----


# ---------- LUECKEN (Achtzehnte Runde, Teil B, Zweig luecken-kl6) ----------
# Läuft nach allen bisherigen Abschnitten mit eigenem Zufallsstart; vorhandene Karten und Aufgaben bleiben unverändert.
# Lehrplan: LehrplanPLUS Gymnasium Bayern M6 1.2 (Umwandlung Bruch ↔ Dezimalbruch bei passenden Zahlen auch im Kopf; Anzeigen digitaler
# Hilfsmittel wie „0,166666667“ bei 1 : 6 reflektiert lesen), M6 1.1 (Prozent als andere Schreibweise für Brüche).
# Prüfungsvorbilder: Grundwissentest Jgst. 7 der Realschule (ISB) 2009 Nr. 2 und 2023 Nr. 10 (Bruch mit einstelligem Zähler und zweistelligem
# Nenner zu 0,75 bzw. 0,25), 2024 Nr. 14 (Taschenrechner-Anzeige eines Bruchs runden), 2008 Nr. 3 (Zahl in der Mitte zwischen zwei Zahlen).
from _luecken_kl6 import karte_neu, zahl, wahl, luecken, bruch as lbruch  # noqa: E402

_KOPF = ['Bruch', '1/2', '1/4', '3/4', '1/5', '1/8']
_MERK = {
    'lernziel': 'merkwerte', 'titel': 'Merkwerte: Bruch, Dezimalzahl, Prozent',
    'einstieg': 'Im Laden steht „Die Hälfte gratis!“. Die Waage zeigt 0,5 kg, der Prospekt 50 %. Das ist immer derselbe Anteil. Solche ⟦Merkwerte⟧ kennst du am besten auswendig.',
    'woerter': [['Merkwert', 'ein Bruch mit seiner Dezimalzahl, den man auswendig weiß, z. B. 1/2 = 0,5'],
                ['Prozent', 'Hundertstel: 25 % = 25/100 = 0,25']],
    'bild': tabelle(_KOPF, [['Dezimal', '?', '?', '?', '?', '?']]),
    'schritte': [
        {'text': 'Die Hälfte: 1/2 = 0,5. Die Hälfte davon: 1/4 = ⟦0,25⟧.',
         'bild': {'zeilen': [['Dezimal', '0,5', '0,25', '?', '?', '?']]}},
        {'text': 'Drei Viertel sind dreimal so viel: 3/4 = 0,75.', 'bild': {'zeilen': [['Dezimal', '0,5', '0,25', '0,75', '?', '?']]}},
        {'text': '1/5 = 2/10 = 0,2. Und 1/8 ist die Hälfte von 1/4: 0,125.',
         'bild': {'zeilen': [['Dezimal', '0,5', '0,25', '0,75', '0,2', '0,125']]}},
        {'text': 'Prozent heißt Hundertstel: 0,25 = 25/100 = ⟦25 %⟧.',
         'bild': {'zeilen': [['Dezimal', '0,5', '0,25', '0,75', '0,2', '0,125'], ['Prozent', '50 %', '25 %', '75 %', '20 %', '12,5 %']]}},
    ],
    'fehler': '1/5 ist nicht 0,5. Ein Fünftel ist viel weniger als die Hälfte: 1/5 = 2/10 = 0,2.',
    'fehler_bild': {'typ': 'tabelle', 'kopf': ['Bruch', '1/2', '1/5'], 'zeilen': [['Dezimal', '0,5', '0,2 (nicht 0,5)']]},
    'regel': 'Merke ⟦1/2, 1/4, 3/4, 1/5, 1/8⟧ als Dezimalzahl und Prozent. Andere Werte leitest du davon ab.',
    'probe': '1/8 = 0,125: Zweimal 0,125 sind 0,25 = 1/4.',
}


def _merk_aufgaben():
    U = 'uebung'
    def b(t, E, h, w): return lambda R: lbruch(t, E, h, w)
    def z(t, v, c, h, w, e=None): return lambda R: zahl(t, v, c, h, w, einheit=e)
    AB = 'Leite den Wert aus einem Merkwert ab (halbieren, verdoppeln, mal 3 …).'
    return [
        (U, 1, z('Kopfrechnen: Schreibe 3/10 als Dezimalzahl.', Fr('0.3'), '3/10', 'Zehntel stehen an der ersten Stelle nach dem Komma.', '3/10 sind 3 Zehntel: 0,3.')),
        (U, 1, b('Kopfrechnen: Schreibe 0,2 als vollständig gekürzten Bruch.', '0.2', 'Denk an die Merkwerte in der Tabelle.', '0,2 = 2/10 = 1/5.')),
        (U, 1, z('Kopfrechnen: Wie viel Prozent sind 0,75?', 75, '0.75 * 100', 'Prozent heißt Hundertstel.', '0,75 = 75/100 = 75 %.', '%')),
        (U, 1, b('Kopfrechnen: Schreibe 50 % als vollständig gekürzten Bruch.', '50/100', '50 % sind 50 Hundertstel.', '50 % = 50/100 = 1/2.')),
        (U, 2, z('Kopfrechnen: Schreibe 3/8 als Dezimalzahl.', Fr('0.375'), '3/8', AB, '1/8 = 0,125. 3/8 = 3 · 0,125 = 0,375.')),
        (U, 2, b('Kopfrechnen: Schreibe 0,4 als vollständig gekürzten Bruch.', '0.4', AB, '0,4 = 2 · 0,2 = 2 · 1/5 = 2/5.')),
        (U, 2, z('Kopfrechnen: Wie viel Prozent sind 3/5?', 60, '3/5 * 100', AB, '1/5 = 20 %. 3/5 = 3 · 20 % = 60 %.', '%')),
        (U, 2, b('Kopfrechnen: Schreibe 1,25 als Bruch. Ein Bruch größer als 1 ist erlaubt.', '1.25', '1,25 = 1 + 0,25.', '1 + 1/4 = 4/4 + 1/4 = 5/4.')),
        (U, 2, z('Kopfrechnen: Schreibe 7/8 als Dezimalzahl.', Fr('0.875'), '7/8', 'Wie viel fehlt 7/8 bis zu einem Ganzen?', '7/8 = 1 − 1/8 = 1 − 0,125 = 0,875.')),
        (U, 2, lambda R: wahl(R, 'Welche Angabe ist genau 1/3?', '0,' + _ue('3'), ['0,3', '0,33', '30 %'],
                              '1/3 ist ein periodischer Dezimalbruch.', '1 : 3 = 0,333… = 0,3 mit Periodenstrich. 0,3 und 0,33 sind nur gerundet; 30 % = 0,3.')),
        (U, 3, (lambda R: luecken('Gib 0,75 als Bruch mit einstelligem Zähler und zweistelligem Nenner an.', '□/□', 'Zähler ins erste Kästchen, Nenner ins zweite.', [9, 12],
                            ['3 * 3', '4 * 3'], '0,75 = 3/4. Erweitere so, dass der Nenner zweistellig, der Zähler aber noch einstellig ist.',
                            '0,75 = 3/4. Mit 2 erweitert: 6/8 (Nenner einstellig). Mit 3 erweitert: 9/12 – das passt. Mit 4: 12/16 (Zähler zweistellig).'))),
        (U, 3, lambda R: wahl(R, 'Ein Taschenrechner zeigt für 1 : 6 die Anzeige 0,166666667. Was stimmt?', '1/6 = 0,1' + _ue('6') + '; der Rechner hat die letzte Stelle gerundet.',
                              ['1/6 hat genau 9 Nachkommastellen.', 'Die 7 am Ende gehört zur Periode.', '1/6 = 0,17 genau.'],
                              'Teile 1 durch 6 schriftlich: Hört die Rechnung auf?',
                              '1 : 6 = 0,1666… – die 6 wiederholt sich ohne Ende. Der Rechner hat nur Platz für wenige Stellen und rundet die letzte auf 7.')),
        (U, 3, z('Welche Zahl liegt genau in der Mitte zwischen 1/4 und 0,5? Gib sie als Dezimalzahl an.', Fr('0.375'), '(1/4 + 0.5) / 2',
                 'Schreibe 1/4 als Dezimalzahl.', '1/4 = 0,25. Mitte zwischen 0,25 und 0,5: (0,25 + 0,5) : 2 = 0,375.')),
        (U, 3, lambda R: wahl(R, 'Ordne 0,3; 1/3; 3/8 und 0,35 der Größe nach. Welche Zahl ist die zweitgrößte?', '0,35', ['3/8', '1/3', '0,3'],
                              'Schreibe alle als Dezimalzahl mit drei Nachkommastellen.', '0,300 < 0,333… (1/3) < 0,350 < 0,375 (3/8). Die zweitgrößte ist 0,35.')),
        (U, 3, b('Welcher Merkwert ist um genau 0,05 größer als 1/5? Gib ihn als Bruch an.', '1/5 + 0.05', '1/5 als Dezimalzahl, dann 0,05 dazu.',
                 '1/5 = 0,2. 0,2 + 0,05 = 0,25 = 1/4.')),
        (U, 3, z('Ein Kind schreibt 1/8 = 0,8. Wie heißt die Dezimalzahl richtig?', Fr('0.125'), '1/8', '1/8 ist die Hälfte von 1/4.',
                 '1/4 = 0,25, die Hälfte davon ist 0,125. 0,8 wären 8/10 – viel zu groß.')),
        (U, 3, z('3/4 l Saft und 0,5 l Wasser werden gemischt. Wie viele Liter sind das?', Fr('1.25'), '3/4 + 0.5', 'Schreibe 3/4 l als Dezimalzahl.',
                 '3/4 l = 0,75 l. 0,75 l + 0,5 l = 1,25 l.', 'l')),
        (U, 3, z('Ein Kind hat 7 von 8 Aufgaben richtig. Wie viel Prozent sind das?', Fr('87.5'), '7/8 * 100', '1/8 = 12,5 %.',
                 '7/8 = 1 − 1/8 = 100 % − 12,5 % = 87,5 %.', '%')),
        ('test', 2, z('Kopfrechnen: Wie viel Prozent sind 0,6?', 60, '0.6 * 100', '', '0,6 = 60/100 = 60 %.', '%')),
        ('korrektur', 2, b('Kopfrechnen: Schreibe 0,125 als vollständig gekürzten Bruch.', '0.125', '', '0,125 ist der Merkwert von 1/8.')),
        ('korrektur', 2, z('Kopfrechnen: Schreibe 2/5 als Dezimalzahl.', Fr('0.4'), '2/5', '', '1/5 = 0,2. 2/5 = 0,4.')),
        ('korrektur', 2, z('Kopfrechnen: Schreibe 20 % als Dezimalzahl.', Fr('0.2'), '20/100', '', '20 % = 20/100 = 0,2.')),
        ('sicherung', 2, z('Kopfrechnen: Schreibe 5/8 als Dezimalzahl.', Fr('0.625'), '5/8', '', '1/8 = 0,125. 5/8 = 5 · 0,125 = 0,625.')),
        ('sicherung', 2, b('Kopfrechnen: Schreibe 0,6 als vollständig gekürzten Bruch.', '0.6', '', '0,6 = 6/10 = 3/5.')),
        ('sicherung', 2, z('Kopfrechnen: Wie viel Prozent sind 1/4?', 25, '1/4 * 100', '', '1/4 = 0,25 = 25 %.', '%')),
        ('sicherung', 2, b('Kopfrechnen: Schreibe 0,875 als vollständig gekürzten Bruch.', '0.875', '', '0,875 = 1 − 0,125 = 1 − 1/8 = 7/8.')),
        ('sicherung', 2, z('Kopfrechnen: Schreibe 4/5 als Dezimalzahl.', Fr('0.8'), '4/5', '', '1/5 = 0,2. 4/5 = 4 · 0,2 = 0,8.')),
        ('sicherung', 2, b('Kopfrechnen: Schreibe 12,5 % als vollständig gekürzten Bruch.', '12.5/100', '', '12,5 % = 0,125 = 1/8.')),
    ]


karte_neu(DATEI, _MERK, _merk_aufgaben(), seed=6211, nach='dezimal_zu_bruch', teil_text='Merkwerte Bruch – Dezimalzahl – Prozent im Kopf umwandeln')


if __name__ == '__main__':
    schreibe(DATEI)
