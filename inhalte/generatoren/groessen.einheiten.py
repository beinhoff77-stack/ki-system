#!/usr/bin/env python3
"""Thema groessen.einheiten – Größen und Einheiten (Klasse 5): Geld, Länge, Masse, Zeit, Kommaschreibweise, Schätzen, Maßstab."""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl5_rest import *  # noqa: E402,F403

R = random.Random(25)
E = eintrag_laden('groessen.einheiten')

ETAPPEN = [
    {'lernziel': 'schaetzen', 'titel': 'Größen schätzen',
     'regel': 'Eine ⟦Größe⟧ besteht aus ⟦Maßzahl und Einheit⟧: 18 cm. Zum Schätzen nimmst du ⟦Bezugsgrößen⟧ aus dem Alltag: Eine Tür ist etwa 2 m hoch, eine Tafel Schokolade wiegt 100 g, eine Schulstunde dauert 45 min.',
     'schritte': ['Wie hoch ist ein Klassenzimmer? Bezugsgröße: Eine Tür ist etwa 2 m hoch.', 'Über der Tür ist noch etwa eine halbe Tür Platz: etwa ⟦3 m⟧.'],
     'fehler': 'Nur auf die Maßzahl zu achten ist ein Fehler: Ein Bleistift ist 18 ⟦cm⟧ lang, nicht 18 m oder 18 mm. Die ⟦Einheit⟧ entscheidet.'},
    {'lernziel': 'laenge', 'titel': 'Längen umrechnen',
     'regel': 'Längeneinheiten: ⟦1 km = 1 000 m⟧, ⟦1 m = 10 dm = 100 cm⟧, ⟦1 dm = 10 cm⟧, ⟦1 cm = 10 mm⟧. In die kleinere Einheit: ⟦malnehmen⟧. In die größere Einheit: ⟦teilen⟧.',
     'schritte': ['Rechne 7 m in cm um. Von m nach cm ist die Umrechnungszahl 100.', 'cm ist kleiner, also mal 100: 7 m = ⟦700 cm⟧.'],
     'probe': '700 cm : 100 = 7 m ✓',
     'fehler': '7 m = 70 cm ist falsch: Zwischen m und cm liegt noch dm. Die Umrechnungszahl ist ⟦100⟧, nicht 10.'},
    {'lernziel': 'masse', 'titel': 'Massen umrechnen',
     'regel': 'Masseneinheiten: ⟦1 t = 1 000 kg⟧, ⟦1 kg = 1 000 g⟧, ⟦1 g = 1 000 mg⟧. Die Umrechnungszahl ist immer ⟦1 000⟧.',
     'schritte': ['Rechne 3 kg in g um: Umrechnungszahl 1 000.', 'g ist kleiner, also mal 1 000: 3 kg = ⟦3 000 g⟧.'],
     'probe': '3 000 g : 1 000 = 3 kg ✓',
     'fehler': '3 kg = 300 g ist falsch: Bei Massen ist die Umrechnungszahl ⟦1 000⟧, nicht 100.'},
    {'lernziel': 'zeit', 'titel': 'Mit Zeit rechnen',
     'regel': 'Zeiteinheiten: ⟦1 d = 24 h⟧, ⟦1 h = 60 min⟧, ⟦1 min = 60 s⟧. Achtung: Hier ist die Umrechnungszahl ⟦60⟧ bzw. 24, nicht 10 oder 100. Zeitspannen berechnest du am besten in ⟦Schritten bis zur vollen Stunde⟧.',
     'schritte': ['Ein Film beginnt um 18:40 Uhr und endet um 20:15 Uhr. Bis 19:00 Uhr: 20 min. Bis 20:00 Uhr: 1 h. Bis 20:15 Uhr: 15 min.', 'Zusammen: 1 h + 20 min + 15 min = ⟦1 h 35 min⟧.'],
     'fehler': '20:15 − 18:40 = 1:75 ist falsch: Eine Stunde hat ⟦60 Minuten⟧, nicht 100. Man darf Uhrzeiten nicht wie Kommazahlen abziehen.'},
    {'lernziel': 'kommaschreibweise', 'titel': 'Größen in Kommaschreibweise',
     'regel': 'Das ⟦Komma⟧ trennt die Einheit von den kleineren Einheiten: 3,45 m = 3 m 45 cm, 4,07 € = 4 € 7 ct, 2,5 kg = 2 kg 500 g. Die ⟦Einheitentafel⟧ hilft: Hinter dem Komma stehen so viele Stellen, wie die ⟦Umrechnungszahl Nullen⟧ hat.',
     'schritte': ['3 m 5 cm in m: 1 m = 100 cm, also zwei Stellen hinter dem Komma.', '5 cm sind 05 cm: 3 m 5 cm = ⟦3,05 m⟧.'],
     'probe': '3,05 m = 305 cm = 3 m 5 cm ✓',
     'fehler': '3 m 5 cm = 3,5 m ist falsch: 3,5 m = 3 m ⟦50⟧ cm. Bei cm brauchst du ⟦zwei⟧ Stellen nach dem Komma: 3,05 m.'},
    {'lernziel': 'rechnen', 'titel': 'Mit Größen rechnen',
     'regel': 'Bevor du Größen addierst oder subtrahierst, bringst du sie auf ⟦dieselbe Einheit⟧. Beim Vervielfachen und Teilen rechnest du oft leichter in der ⟦kleineren Einheit⟧ (ct statt €, cm statt m).',
     'schritte': ['1,2 km + 350 m: Beides in m, 1,2 km = 1 200 m.', '1 200 m + 350 m = ⟦1 550 m⟧.'],
     'fehler': '1,2 km + 350 m = 351,2 ist falsch: Man darf Maßzahlen mit ⟦verschiedenen Einheiten⟧ nicht einfach addieren. Erst umrechnen!'},
    {'lernziel': 'massstab', 'titel': 'Maßstab auf Karten und Plänen',
     'regel': 'Der ⟦Maßstab 1 : 25 000⟧ bedeutet: 1 cm auf der Karte sind ⟦25 000 cm⟧ in Wirklichkeit, also 250 m. Wirklichkeit = ⟦Kartenlänge · 25 000⟧. Bei ⟦10 : 1⟧ ist das Bild 10-mal so groß wie in Wirklichkeit.',
     'schritte': ['Karte 1 : 25 000, Strecke auf der Karte 4 cm. Wirklichkeit: 4 cm · 25 000 = 100 000 cm.', '100 000 cm = 1 000 m = ⟦1 km⟧.'],
     'fehler': '4 cm · 25 000 = 100 000 m ist falsch: Die Einheit bleibt erst einmal ⟦cm⟧. 100 000 cm sind nur 1 km.'},
    {'lernziel': 'verstehen', 'titel': 'Größen prüfen, Fehler finden',
     'regel': 'Prüfe jedes Ergebnis: ⟦Passt die Einheit?⟧ ⟦Ist die Größe realistisch?⟧ Vergleiche mit einer Bezugsgröße. Eine Umrechnung prüfst du durch ⟦Rückwärtsrechnen⟧.',
     'schritte': ['Behauptet: „Ein Schulweg von 1,5 km dauert zu Fuß 2 Minuten.“ Bezugsgröße: 1 km zu Fuß dauert etwa 12 bis 15 min.', '1,5 km dauern also etwa 20 min. Die Aussage ist ⟦unrealistisch⟧.'],
     'fehler': 'Ein Ergebnis wie „Ein Ei wiegt 60 kg“ einfach hinzuschreiben, ohne nachzudenken, ist der häufigste Fehler. Die ⟦Plausibilität⟧ prüfen – richtig wären 60 g.'},
]

MERKE = ['km –1 000– m –10– dm –10– cm –10– mm', 't –1 000– kg –1 000– g –1 000– mg', '€ –100– ct', 'd –24– h –60– min –60– s',
         'Kommaschreibweise: so viele Nachkommastellen, wie die Umrechnungszahl Nullen hat.', 'Maßstab 1 : n: Wirklichkeit = Karte · n.']

LAENGE = {'km': 1_000_000, 'm': 1000, 'dm': 100, 'cm': 10, 'mm': 1}
MASSE = {'t': 10 ** 9, 'kg': 10 ** 6, 'g': 1000, 'mg': 1}
GELD = {'€': 100, 'ct': 1}

# Bezugsgrößen: (Satzanfang, Maßzahl, richtige Einheit, falsche Einheiten)
SCHAETZ = [('Ein Bleistift ist etwa', 18, 'cm', ['mm', 'm', 'dm']), ('Eine Zimmertür ist etwa', 2, 'm', ['cm', 'dm', 'km']),
           ('Ein Fußballfeld ist etwa', 100, 'm', ['cm', 'km', 'dm']), ('Eine Tafel Schokolade wiegt', 100, 'g', ['kg', 'mg', 't']),
           ('Ein Erwachsener wiegt etwa', 70, 'kg', ['g', 't', 'mg']), ('Ein Auto wiegt etwa', Fr(3, 2), 't', ['kg', 'g', 'mg']),
           ('Ein Apfel wiegt etwa', 150, 'g', ['kg', 'mg', 't']), ('Eine Schulstunde dauert', 45, 'min', ['s', 'h', 'd']),
           ('Zähneputzen dauert etwa', 3, 'min', ['s', 'h', 'd']), ('Ein Fingernagel ist etwa', 1, 'cm', ['m', 'dm', 'km']),
           ('Ein Elefant wiegt etwa', 5, 't', ['kg', 'g', 'mg']), ('Ein Marathonlauf ist etwa', 42, 'km', ['m', 'cm', 'dm']),
           ('Ein Ei wiegt etwa', 60, 'g', ['kg', 'mg', 't']), ('Ein Schuljahr hat etwa', 190, 'Schultage', None),
           ('Eine Ameise ist etwa', 5, 'mm', ['cm', 'm', 'dm']), ('Ein Stockwerk eines Hauses ist etwa', 3, 'm', ['cm', 'dm', 'km']),
           ('Eine Briefmarke wiegt etwa', 1, 'g', ['kg', 't', 'mg']), ('Ein Lied im Radio dauert etwa', 3, 'min', ['s', 'h', 'd']),
           ('Ein Schulheft wiegt etwa', 50, 'g', ['kg', 'mg', 't']), ('Ein Lineal ist etwa', 30, 'cm', ['mm', 'm', 'dm']),
           ('Ein Kinofilm dauert etwa', 2, 'h', ['min', 's', 'd']), ('Ein Lkw mit Ladung wiegt etwa', 40, 't', ['kg', 'g', 'mg'])]
SCHAETZ = [s for s in SCHAETZ if s[3]]


def gr(x, e): return f'{zt(x)} {e}'


def umr(x, von, nach, tafel):
    """Umrechnen exakt."""
    return Fr(x) * tafel[von] / tafel[nach]


# ---------- 1 Schätzen ----------
def g_schaetz(st):
    satz, z, e, falsch = R.choice(SCHAETZ)
    if st == 1:
        return {**wahl(R, e, falsch), 'f': {'text': f'Welche Einheit passt? {satz} {zt(z)} …'},
                'w': f'{satz} {gr(z, e)}. Mit {falsch[0]} oder {falsch[1]} wäre die Größe viel zu klein oder zu groß.', 'h': 'Stell dir den Gegenstand vor und vergleiche mit einer Bezugsgröße.'}
    if st == 2:
        tafel = LAENGE if e in LAENGE else MASSE if e in MASSE else None
        if tafel is None:
            r = gr(z, e)
            return {**wahl(R, r, [gr(z * 60, e), gr(z, 'h' if e == 'min' else 'min'), gr(z * 10, e)]), 'f': {'text': f'Was ist realistisch? {satz.replace(" etwa", "")} …'},
                    'w': f'{satz} {r}.', 'h': 'Vergleiche mit Zeiten, die du kennst.'}
        r = gr(z, e)
        alt = [gr(z, f) for f in falsch[:2]] + [gr(z * 10 if z < 1000 else z, e) if z * 10 != z else gr(z + 1, e)]
        return {**wahl(R, r, alt), 'f': {'text': f'Was ist realistisch? {satz.replace(" etwa", "")} ungefähr …'}, 'w': f'{satz} {r}.', 'h': 'Gleiche Maßzahl, andere Einheit: Welche passt zur Wirklichkeit?'}
    art = R.randrange(2)
    if art == 0:
        n = R.randint(3, 9)
        bez = R.choice([('Eine Tür ist etwa 2 m hoch. Ein Haus ist etwa {n} Türen hoch.', 2, 'm'), ('Ein Schritt ist etwa 60 cm lang. Ein Weg ist {n}0 Schritte lang.', 60, 'cm'),
                        ('Eine Tafel Schokolade wiegt 100 g. Eine Packung enthält {n} Tafeln.', 100, 'g')])
        t, b, e = bez
        mult = n * 10 if '{n}0' in t else n
        wert_ = b * mult
        if e == 'cm':
            return {'y': 'zahl', 'f': {'text': t.format(n=n) + ' Wie viele Meter ist der Weg etwa lang?'}, 'o': {'wert': wert(Fr(wert_, 100)), 'einheit': 'm'}, 'c': f'{b} * {mult} / 100',
                    'w': f'{mult} · 60 cm = {zt(wert_)} cm = {zt(Fr(wert_, 100))} m.', 'h': 'Erst in cm rechnen, dann in m umrechnen.'}
        return {'y': 'zahl', 'f': {'text': t.format(n=n) + (' Wie hoch ist das Haus etwa?' if e == 'm' else ' Wie schwer ist die Packung (ohne Verpackung) in g?')},
                'o': {'wert': wert_, 'einheit': e}, 'c': f'{b} * {mult}', 'w': f'{mult} · {b} {e} = {zt(wert_)} {e}.', 'h': 'Vervielfache die Bezugsgröße.'}
    satz, z, e, falsch = R.choice(SCHAETZ)
    f = R.choice(falsch[:2])
    r = f'Nein, richtig wären etwa {gr(z, e)}.'
    return {**wahl(R, r, ['Ja, das ist realistisch.', f'Nein, richtig wären etwa {gr(z * 1000, f)}.' if f in ('mm', 'mg') else f'Nein, richtig wären etwa {gr(z * 10, e)}.']),
            'f': {'text': f'Ein Kind schreibt: „{satz} {gr(z, f)}.“ Stimmt das?'}, 'w': f'{satz} {gr(z, e)}, nicht {gr(z, f)}.', 'h': 'Prüfe die Einheit mit einer Bezugsgröße.'}


# ---------- 2/3 Länge und Masse ----------
def g_tafel(tafel, paare):
    ein = list(tafel)

    def g(st):
        if st == 1:
            i = R.randrange(len(ein) - 1)
            a, b = ein[i], ein[i + 1]
            x = R.randint(2, 90)
            if R.random() < .5:
                return {'y': 'zahl', 'f': {'text': f'Rechne um: {gr(x, a)} = ? {b}'}, 'o': {'wert': wert(umr(x, a, b, tafel)), 'einheit': b}, 'c': f'{x} * {tafel[a]} / {tafel[b]}',
                        'w': f'1 {a} = {zt(umr(1, a, b, tafel))} {b}. {x} · {zt(umr(1, a, b, tafel))} = {zt(umr(x, a, b, tafel))} {b}.', 'h': 'In die kleinere Einheit: malnehmen.'}
            y = x * tafel[a] // tafel[b]
            return {'y': 'zahl', 'f': {'text': f'Rechne um: {gr(y, b)} = ? {a}'}, 'o': {'wert': x, 'einheit': a}, 'c': f'{y} * {tafel[b]} / {tafel[a]}',
                    'w': f'1 {a} = {zt(umr(1, a, b, tafel))} {b}. {zt(y)} : {zt(umr(1, a, b, tafel))} = {x} {a}.', 'h': 'In die größere Einheit: teilen.'}
        if st == 2:
            a, b = R.choice(paare)
            if R.random() < .5:
                x = R.randint(2, 60)
                return {'y': 'zahl', 'f': {'text': f'Rechne um: {gr(x, a)} = ? {b}'}, 'o': {'wert': wert(umr(x, a, b, tafel)), 'einheit': b}, 'c': f'{x} * {tafel[a]} / {tafel[b]}',
                        'w': f'1 {a} = {zt(umr(1, a, b, tafel))} {b}, also {gr(x, a)} = {gr(umr(x, a, b, tafel), b)}.', 'h': 'Gehe Schritt für Schritt durch die Einheitentafel.'}
            k = int(umr(1, a, b, tafel))
            x, y = R.randint(1, 30), R.randint(1, k - 1)
            ges = x * k + y
            return {'y': 'zahl', 'f': {'text': f'Schreibe in {b}: {gr(x, a)} {gr(y, b)}'}, 'o': {'wert': ges, 'einheit': b}, 'c': f'{x} * {tafel[a]} / {tafel[b]} + {y}',
                    'w': f'{gr(x, a)} = {gr(x * k, b)}, dazu {gr(y, b)}: {gr(ges, b)}.', 'h': 'Rechne die größere Einheit um und addiere den Rest.'}
        art = R.randrange(3)
        a, b = R.choice(paare)
        k = int(umr(1, a, b, tafel))
        if art == 0:
            x, y = R.randint(1, 40), R.randint(1, k - 1)
            ges = x * k + y
            return luecke([x, y], f'Zerlege: {gr(ges, b)} = □ {a} □ {b}', f'□ {a} □ {b}', f'Erst {a}, dann {b}.', [f'{ges} // {k}', f'{ges} % {k}'],
                          f'{zt(ges)} : {zt(k)} = {x} Rest {y}. Also {gr(x, a)} {gr(y, b)}.', f'Wie oft passen {zt(k)} {b} in {zt(ges)} {b}? Der Rest bleibt in {b}.')
        if art == 1:
            werte = []
            while len(werte) < 4:
                e2 = [a, b][len(werte) % 2]
                v = Fr(R.randint(1, 30) * (k // 10 if e2 == b and k >= 100 else 1) + (R.randint(1, 9) if e2 == b else 0))
                if all(umr(v, e2, b, tafel) != umr(w2, f2, b, tafel) for w2, f2 in werte): werte.append((v, e2))
            groesst = max(werte, key=lambda t: umr(t[0], t[1], b, tafel))
            return {**wahl(R, gr(*groesst), [gr(*t) for t in werte]), 'f': {'text': 'Welche Größe ist am größten: ' + ', '.join(gr(*t) for t in werte) + '?'},
                    'w': 'In ' + b + ': ' + ', '.join(f'{gr(*t)} = {gr(umr(t[0], t[1], b, tafel), b)}' for t in werte) + f'. Am größten: {gr(*groesst)}.', 'h': 'Rechne alle in dieselbe Einheit um.'}
        x = R.randint(2, 9)
        n = R.choice([4, 5, 8, 10, 20, 25])
        ges = x * k
        if k < 100 or ges % n: return g(3)
        return {'y': 'zahl', 'f': {'text': f'{gr(x, a)} werden in {n} gleiche Teile geteilt. Wie viel {b} ist ein Teil?'}, 'o': {'wert': ges // n, 'einheit': b}, 'c': f'{x} * {tafel[a]} / {tafel[b]} / {n}',
                'w': f'{gr(x, a)} = {gr(ges, b)}. {zt(ges)} : {n} = {gr(ges // n, b)}.', 'h': f'Rechne zuerst in {b} um, dann teile.'}
    return g


# ---------- 4 Zeit ----------
def uhr(m): return f'{m // 60}:{m % 60:02d} Uhr'


def g_zeit(st):
    if st == 1:
        art = R.randrange(3)
        x = R.randint(2, 12)
        if art == 0:
            return {'y': 'zahl', 'f': {'text': f'Wie viele Minuten sind {x} h?'}, 'o': {'wert': 60 * x, 'einheit': 'min'}, 'c': f'{x} * 60',
                    'w': f'1 h = 60 min, also {x} · 60 = {60 * x} min.', 'h': 'Eine Stunde hat 60 Minuten.'}
        if art == 1:
            return {'y': 'zahl', 'f': {'text': f'Wie viele Sekunden sind {x} min?'}, 'o': {'wert': 60 * x, 'einheit': 's'}, 'c': f'{x} * 60',
                    'w': f'1 min = 60 s, also {x} · 60 = {60 * x} s.', 'h': 'Eine Minute hat 60 Sekunden.'}
        x = R.randint(2, 7)
        return {'y': 'zahl', 'f': {'text': f'Wie viele Stunden haben {x} Tage?'}, 'o': {'wert': 24 * x, 'einheit': 'h'}, 'c': f'{x} * 24',
                'w': f'1 d = 24 h, also {x} · 24 = {24 * x} h.', 'h': 'Ein Tag hat 24 Stunden.'}
    if st == 2:
        art = R.randrange(3)
        if art == 0:
            m = R.randint(65, 400)
            if m % 60 == 0: m += 7
            return luecke([m // 60, m % 60], f'Schreibe {m} min in Stunden und Minuten.', '□ h □ min', 'Erst die Stunden, dann die Minuten.', [f'{m} // 60', f'{m} % 60'],
                          f'{m} : 60 = {m // 60} Rest {m % 60}. Also {m // 60} h {m % 60} min.', 'Wie viele volle 60 passen hinein?')
        if art == 1:
            a = R.randint(7 * 60, 18 * 60) // 5 * 5
            d = R.randint(25, 170) // 5 * 5
            b = a + d
            return {'y': 'zahl', 'f': {'text': f'Ein Ausflug beginnt um {uhr(a)} und endet um {uhr(b)}. Wie viele Minuten dauert er?'}, 'o': {'wert': d, 'einheit': 'min'},
                    'c': f'({b // 60} * 60 + {b % 60}) - ({a // 60} * 60 + {a % 60})', 'w': f'Von {uhr(a)} bis {uhr(b)}: {d // 60} h {d % 60} min = {d} min.',
                    'h': 'Rechne in Schritten bis zur vollen Stunde.'}
        x, y = R.randint(1, 5), R.randint(5, 55)
        return {'y': 'zahl', 'f': {'text': f'Wie viele Minuten sind {x} h {y} min?'}, 'o': {'wert': 60 * x + y, 'einheit': 'min'}, 'c': f'{x} * 60 + {y}',
                'w': f'{x} h = {60 * x} min, dazu {y} min: {60 * x + y} min.', 'h': 'Stunden in Minuten umrechnen, dann addieren.'}
    art = R.randrange(3)
    if art == 0:
        a = R.randint(6 * 60, 20 * 60) // 5 * 5
        d = R.randint(40, 200) // 5 * 5
        if d % 60 == 0: d += 25
        b = a + d
        return luecke([b // 60, b % 60], f'Ein Zug fährt um {uhr(a)} ab. Die Fahrt dauert {d // 60} h {d % 60} min. Wann kommt er an?', '□:□ Uhr', 'Stunde ins erste Feld, Minuten ins zweite.',
                      [f'({a} + {d}) // 60', f'({a} + {d}) % 60'], f'{uhr(a)} + {d // 60} h = {uhr(a + d // 60 * 60)}, + {d % 60} min = {uhr(b)}.', 'Erst die Stunden addieren, dann die Minuten. Über 60 min gibt es eine Stunde mehr.')
    if art == 1:
        s = R.randint(70, 600)
        if s % 60 == 0: s += 13
        return luecke([s // 60, s % 60], f'Ein Lauf dauert {s} s. Schreibe die Zeit in Minuten und Sekunden.', '□ min □ s', 'Erst die Minuten, dann die Sekunden.', [f'{s} // 60', f'{s} % 60'],
                      f'{s} : 60 = {s // 60} Rest {s % 60}: {s // 60} min {s % 60} s.', 'Eine Minute hat 60 Sekunden.')
    a = R.randint(20 * 60, 23 * 60) // 5 * 5
    b = R.randint(5 * 60, 8 * 60) // 5 * 5
    d = 24 * 60 - a + b
    return luecke([d // 60, d % 60], f'Ein Kind geht um {uhr(a)} schlafen und steht um {uhr(b)} auf. Wie lange schläft es?', '□ h □ min', 'Erst die Stunden, dann die Minuten.',
                  [f'(24 * 60 - {a} + {b}) // 60', f'(24 * 60 - {a} + {b}) % 60'], f'Bis Mitternacht: {(24 * 60 - a) // 60} h {(24 * 60 - a) % 60} min. Dann bis {uhr(b)}: {b // 60} h {b % 60} min. Zusammen {d // 60} h {d % 60} min.',
                  'Rechne bis Mitternacht und dann weiter.')


# ---------- 5 Kommaschreibweise ----------
KOMMA = [('m', 'cm', 100, LAENGE), ('km', 'm', 1000, LAENGE), ('kg', 'g', 1000, MASSE), ('t', 'kg', 1000, MASSE), ('€', 'ct', 100, GELD), ('cm', 'mm', 10, LAENGE)]


def g_komma(st):
    g_, k_, n, tafel = R.choice(KOMMA)
    stellen = len(str(n)) - 1
    if st == 1:
        x, y = R.randint(1, 20), R.randint(1, n - 1)
        while n > 10 and y % 10 == 0: y = R.randint(1, n - 1)
        v = x + Fr(y, n)
        return {'y': 'zahl', 'f': {'text': f'Schreibe in Kommaschreibweise: {gr(x, g_)} {gr(y, k_)} = ? {g_}'}, 'o': {'wert': wert(v), 'einheit': g_}, 'c': f'{x} + {y} / {n}',
                'w': f'1 {g_} = {zt(n)} {k_}: {stellen} Stelle{"n" if stellen > 1 else ""} nach dem Komma. {gr(y, k_)} → {str(y).rjust(stellen, "0")}. Also {gr(v, g_)}.', 'h': f'Nach dem Komma stehen {stellen} Stellen, fehlende mit 0 auffüllen.'}
    if st == 2:
        v = Fr(R.randint(1, 30 * n), n)
        while v.denominator == 1: v = Fr(R.randint(1, 30 * n), n)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Rechne um: {gr(v, g_)} = ? {k_}'}, 'o': {'wert': int(v * n), 'einheit': k_}, 'c': f'{float(v)} * {n}',
                    'w': f'Mal {zt(n)}: Komma um {stellen} Stelle{"n" if stellen > 1 else ""} nach rechts. {gr(v, g_)} = {gr(v * n, k_)}.', 'h': f'1 {g_} = {zt(n)} {k_}.'}
        return {'y': 'zahl', 'f': {'text': f'Rechne um: {gr(v * n, k_)} = ? {g_}'}, 'o': {'wert': wert(v), 'einheit': g_}, 'c': f'{int(v * n)} / {n}',
                'w': f'Durch {zt(n)}: Komma um {stellen} Stelle{"n" if stellen > 1 else ""} nach links. {gr(v * n, k_)} = {gr(v, g_)}.', 'h': f'{zt(n)} {k_} = 1 {g_}.'}
    art = R.randrange(2)
    if art == 0:
        x = R.randint(1, 15)
        y = R.randint(1, 9) if n > 10 else R.randint(1, 9)
        v = x + Fr(y, n)
        return luecke([x, y], f'Schreibe mit zwei Einheiten: {gr(v, g_)} = □ {g_} □ {k_}', f'□ {g_} □ {k_}', f'Erst {g_}, dann {k_}.', [f'{float(v)} // 1', f'{float(v)} * {n} % {n}'],
                      f'{gr(v, g_)}: vor dem Komma {x} {g_}, nach dem Komma {str(y).rjust(stellen, "0")} → {y} {k_}.', 'Achte auf die Nullen nach dem Komma.')
    x, y = R.randint(1, 9), R.randint(1, 9)
    falsch = x + Fr(y, 10)
    richtig = x + Fr(y, n)
    if n == 10: return g_komma(3)
    return {**wahl(R, gr(richtig, g_), [gr(falsch, g_), gr(x + Fr(y, n * 10), g_), gr(x * n + y, g_)]), 'f': {'text': f'Welche Kommaschreibweise ist richtig für {gr(x, g_)} {gr(y, k_)}?'},
            'w': f'{gr(y, k_)} sind {zt(Fr(y, n))} {g_} ({stellen} Stellen nach dem Komma). Also {gr(richtig, g_)}. {gr(falsch, g_)} wäre {gr(x, g_)} {gr(y * n // 10, k_)}.',
            'h': f'Wie viele Stellen nach dem Komma braucht {k_}?'}


# ---------- 6 Rechnen ----------
def g_rechnen(st):
    if st == 1:
        a, b = Fr(R.randint(100, 2000), 100), Fr(R.randint(100, 2000), 100)
        op = R.choice('+-')
        if op == '-' and a < b: a, b = b, a
        r = a + b if op == '+' else a - b
        o = '+' if op == '+' else '−'
        return {'y': 'zahl', 'f': {'text': f'Berechne {euro(a)} {o} {euro(b)}.'}, 'o': {'wert': wert(r), 'einheit': '€'}, 'c': f'{float(a)} {op} {float(b)}',
                'w': f'Komma unter Komma (oder in ct: {int(a * 100)} ct {o} {int(b * 100)} ct = {int(r * 100)} ct). Ergebnis {euro(r)}.', 'h': 'Rechne in Cent oder schreibe Komma unter Komma.'}
    if st == 2:
        art = R.randrange(3)
        if art == 0:
            a = Fr(R.randint(11, 60), 10)
            b = R.randint(50, 950) // 10 * 10
            return {'y': 'zahl', 'f': {'text': f'Berechne {gr(a, "km")} + {gr(b, "m")} in m.'}, 'o': {'wert': int(a * 1000 + b), 'einheit': 'm'}, 'c': f'{float(a)} * 1000 + {b}',
                    'w': f'{gr(a, "km")} = {gr(a * 1000, "m")}. {zt(a * 1000)} + {b} = {gr(a * 1000 + b, "m")}.', 'h': 'Erst beide Größen in m umrechnen.'}
        if art == 1:
            p = Fr(R.randint(45, 399), 100)
            n = R.randint(3, 9)
            ware = R.choice(['Ein Heft kostet', 'Ein Brötchen kostet', 'Ein Stift kostet', 'Eine Briefmarke kostet'])
            if ware.startswith('Ein Brötchen'): p = Fr(R.randint(35, 90), 100)
            return {'y': 'zahl', 'f': {'text': f'{ware} {euro(p)}. Was kosten {n} Stück?'}, 'o': {'wert': wert(p * n), 'einheit': '€'}, 'c': f'{float(p)} * {n}',
                    'w': f'In Cent: {int(p * 100)} ct · {n} = {int(p * 100 * n)} ct = {euro(p * n)}.', 'h': 'Rechne in Cent, dann zurück in Euro.'}
        l = R.choice([2, 3, 4, 5, 6])
        n = R.choice([4, 5, 8, 10, 20, 25])
        return {'y': 'zahl', 'f': {'text': f'Ein Band ist {l} m lang. Es wird in {n} gleich lange Stücke geschnitten. Wie lang ist ein Stück in cm?'}, 'o': {'wert': wert(Fr(l * 100, n)), 'einheit': 'cm'},
                'c': f'{l} * 100 / {n}', 'w': f'{l} m = {l * 100} cm. {l * 100} : {n} = {zt(Fr(l * 100, n))} cm.', 'h': 'Rechne zuerst in cm um.'}
    art = R.randrange(3)
    if art == 0:
        preise = [Fr(R.randint(80, 650), 100) for _ in range(3)]
        s = sum(preise)
        sch = 20 if s < 20 else 50
        return {'y': 'zahl', 'f': {'text': f'Einkauf: Brot {euro(preise[0])}, Käse {euro(preise[1])}, Obst {euro(preise[2])}. Bezahlt wird mit {sch} €. Wie viel Rückgeld gibt es?'},
                'o': {'wert': wert(sch - s), 'einheit': '€'}, 'c': f'{sch} - ({" + ".join(str(float(p)) for p in preise)})',
                'w': f'Summe: {euro(s)}. Rückgeld: {sch} € − {euro(s)} = {euro(sch - s)}.', 'h': 'Erst alles addieren, dann vom bezahlten Betrag abziehen.'}
    if art == 1:
        dinge = [('Laptop', Fr(R.randint(12, 25), 10), 'kg'), ('Bücher', R.randint(600, 1800) // 50 * 50, 'g'), ('Trinkflasche', R.randint(500, 900) // 50 * 50, 'g'),
                 ('Brotzeitbox', R.randint(250, 450) // 10 * 10, 'g')]
        ges_g = sum(Fr(v) * (1000 if e == 'kg' else 1) for _, v, e in dinge)
        return {'y': 'zahl', 'f': {'text': 'Im Rucksack sind: ' + ', '.join(f'{n} {gr(v, e)}' for n, v, e in dinge) + '. Wie schwer ist alles zusammen in kg?'},
                'o': {'wert': wert(ges_g / 1000), 'einheit': 'kg'}, 'c': '(' + ' + '.join(f'{float(v) * 1000 if e == "kg" else v}' for _, v, e in dinge) + ') / 1000',
                'w': f'In g: {" + ".join(zt(Fr(v) * (1000 if e == "kg" else 1)) for _, v, e in dinge)} = {zt(ges_g)} g = {zt(ges_g / 1000)} kg.', 'h': 'Rechne alles in g um, addiere, dann zurück in kg.'}
    t = R.choice([4, 5, 6])
    km = R.choice([Fr(3, 2), Fr(5, 2), Fr(12, 10), Fr(18, 10), 2, 3])
    ges = Fr(km) * t * 2
    return {'y': 'zahl', 'f': {'text': f'Ein Kind fährt an {t} Schultagen mit dem Rad zur Schule und zurück. Der Schulweg ist {gr(km, "km")} lang. Wie viele km sind das in der Woche?'},
            'o': {'wert': wert(ges), 'einheit': 'km'}, 'c': f'{float(km)} * 2 * {t}', 'w': f'Pro Tag: 2 · {gr(km, "km")} = {gr(2 * Fr(km), "km")}. In {t} Tagen: {gr(ges, "km")}.',
            'h': 'Hin und zurück – also zweimal pro Tag.'}


def euro(x):
    x = Fr(x)
    if x.denominator == 1: return f'{zt(x)},00 €'
    g, n = zt(x).split(',')
    return f'{g},{n.ljust(2, "0")} €'


# ---------- 7 Maßstab ----------
MST = [5000, 10000, 20000, 25000, 50000, 100000]


def g_mst(st):
    m = R.choice(MST)
    if st == 1:
        k = R.randint(1, 9)
        w_cm = k * m
        return {'y': 'zahl', 'f': {'text': f'Maßstab 1 : {zt(m)}. Auf der Karte sind es {k} cm. Wie viele Meter sind es in Wirklichkeit?'}, 'o': {'wert': w_cm // 100, 'einheit': 'm'},
                'c': f'{k} * {m} / 100', 'w': f'{k} cm · {zt(m)} = {zt(w_cm)} cm = {zt(w_cm // 100)} m.', 'h': 'Kartenlänge mal Maßstabszahl, dann cm in m umrechnen.'}
    if st == 2:
        if R.random() < .5:
            k = Fr(R.randint(5, 60), 2) if m <= 25000 else Fr(R.randint(2, 20), 2)
            w = k * m
            if (w / 100000).denominator > 100: return g_mst(2)
            return {'y': 'zahl', 'f': {'text': f'Maßstab 1 : {zt(m)}. Auf der Karte misst ein Weg {gr(k, "cm")}. Wie viele km ist er wirklich lang?'}, 'o': {'wert': wert(w / 100000), 'einheit': 'km'},
                    'c': f'{float(k)} * {m} / 100000', 'w': f'{gr(k, "cm")} · {zt(m)} = {zt(w)} cm = {zt(w / 100)} m = {zt(w / 100000)} km.', 'h': '100 000 cm = 1 km.'}
        km = R.randint(1, 12)
        k = Fr(km * 100000, m)
        if (k * 10).denominator != 1 or k > 40: return g_mst(2)
        return {'y': 'zahl', 'f': {'text': f'Maßstab 1 : {zt(m)}. Wie lang ist eine {km} km lange Strecke auf der Karte (in cm)?'}, 'o': {'wert': wert(k), 'einheit': 'cm'}, 'c': f'{km} * 100000 / {m}',
                'w': f'{km} km = {zt(km * 100000)} cm. {zt(km * 100000)} : {zt(m)} = {zt(k)} cm.', 'h': 'Wirklichkeit in cm umrechnen und durch die Maßstabszahl teilen.'}
    art = R.randrange(3)
    if art == 0:
        k = R.randint(2, 10)
        w_m = k * m // 100
        return luecke([m], f'Auf einer Karte sind {k} cm in Wirklichkeit {zt(w_m)} m. Wie heißt der Maßstab?', '1 : □', 'Trage die Maßstabszahl ein.', [f'{w_m} * 100 / {k}'],
                      f'{zt(w_m)} m = {zt(w_m * 100)} cm. {zt(w_m * 100)} : {k} = {zt(m)}. Maßstab 1 : {zt(m)}.', 'Rechne die Wirklichkeit in cm um und teile durch die Kartenlänge.')
    if art == 1:
        f = R.choice([5, 10, 20, 50])
        mm = R.choice([2, 3, 4, 5, 6, 8])
        tier = R.choice(['Eine Ameise', 'Ein Marienkäfer', 'Ein Floh', 'Eine Mücke'])
        return {'y': 'zahl', 'f': {'text': f'{tier} ist {mm} mm lang. Im Biologiebuch ist das Tier im Maßstab {f} : 1 abgebildet. Wie viele cm ist das Bild lang?'},
                'o': {'wert': wert(Fr(mm * f, 10)), 'einheit': 'cm'}, 'c': f'{mm} * {f} / 10', 'w': f'{f} : 1 heißt {f}-mal so groß: {mm} mm · {f} = {mm * f} mm = {zt(Fr(mm * f, 10))} cm.',
                'h': 'Bei f : 1 ist das Bild f-mal so groß wie in Wirklichkeit.'}
    l, b = R.choice([(12, 8), (10, 6), (15, 10), (9, 6), (14, 8)])
    mm = R.choice([50, 100])
    if (l * 100) % mm or (b * 100) % mm: return g_mst(3)
    a = luecke([l * 100 // mm, b * 100 // mm],
                  f'Ein Zimmer ist {l} m lang und {b} m breit. Zeichne es im Maßstab 1 : {mm}. Wie lang und breit wird es auf dem Plan (in cm)?', 'Länge □ cm, Breite □ cm', 'Erst die Länge, dann die Breite.',
                  [f'{l} * 100 / {mm}', f'{b} * 100 / {mm}'], f'{l} m = {l * 100} cm, : {mm} = {l * 100 // mm} cm. {b} m = {b * 100} cm, : {mm} = {b * 100 // mm} cm.',
                  'Erst in cm umrechnen, dann durch die Maßstabszahl teilen.')
    a['f']['grafik'] = {'typ': 'figur', 'punkte': {'_A': [0, 0], '_B': [l, 0], '_C': [l, b], '_D': [0, b]}, 'flaeche': ['_A', '_B', '_C', '_D'],
                        'linien': [['_A', '_B', f'{l} m'], ['_B', '_C', f'{b} m'], ['_C', '_D'], ['_D', '_A']]}
    return a


# ---------- 8 Verstehen ----------
def g_vers(st):
    if st == 1:
        x = R.randint(2, 9)
        aussagen = [(f'{x} m = {x * 10} cm', False, f'Nein, 1 m = 100 cm, also {x} m = {x * 100} cm.'),
                    (f'{x} kg = {x * 1000} g', True, 'Ja, bei Massen ist die Umrechnungszahl 1 000.'),
                    (f'{x} h = {x * 100} min', False, f'Nein, 1 h = 60 min, also {x} h = {x * 60} min.'),
                    (f'{x} € = {x * 100} ct', True, 'Ja, 1 € = 100 ct.')]
    elif st == 2:
        x, y = R.randint(1, 9), R.randint(1, 9)
        aussagen = [(f'{x} m {y} cm = {x},{y} m', False, f'Nein, {y} cm = 0,0{y} m. Also {x},0{y} m.'),
                    (f'{x},{y} kg = {x} kg {y}00 g', True, f'Ja, {x},{y} kg = {x * 1000 + y * 100} g = {x} kg {y * 100} g.'),
                    (f'{x},5 h = {x} h 50 min', False, f'Nein, 0,5 h ist eine halbe Stunde = 30 min.'),
                    (f'{x},{y}0 € = {x} € {y}0 ct', True, 'Ja, zwei Stellen nach dem Komma sind Cent.')]
    else:
        aussagen = [('Ein Ei wiegt etwa 60 kg.', False, 'Nein, ein Ei wiegt etwa 60 g.'),
                    ('Ein Klassenzimmer ist etwa 8 m lang.', True, 'Ja, das ist realistisch (etwa 4 Türbreiten mal 2).'),
                    ('Mit dem Rad schafft man 15 km in etwa einer Stunde.', True, 'Ja, Radfahrer fahren etwa 15 km pro Stunde.'),
                    ('Ein Schulbus ist etwa 12 cm lang.', False, 'Nein, ein Bus ist etwa 12 m lang.'),
                    ('Ein Kind wiegt etwa 40 t.', False, 'Nein, ein Kind wiegt etwa 40 kg.'),
                    ('Ein Fußweg von 1 km dauert etwa 15 min.', True, 'Ja, man geht etwa 4 bis 5 km in der Stunde.'),
                    ('Auf einer Karte 1 : 100 000 ist 1 cm in Wirklichkeit 1 km.', True, 'Ja, 100 000 cm = 1 000 m = 1 km.'),
                    ('Auf einer Karte 1 : 10 000 ist 1 cm in Wirklichkeit 10 km.', False, 'Nein, 10 000 cm = 100 m.')]
    s, stimmt, grund = R.choice(aussagen)
    gegen = 'Ja, das stimmt.' if not stimmt else 'Nein, das ist falsch.'
    return {**wahl(R, grund, [gegen, 'Das kann man nicht entscheiden.'], 3), 'f': {'text': f'Stimmt das? „{s}“'}, 'w': grund,
            'h': 'Prüfe die Umrechnungszahl oder vergleiche mit einer Bezugsgröße.'}


GEN = {'schaetzen': g_schaetz, 'laenge': g_tafel(LAENGE, [('km', 'm'), ('m', 'cm'), ('m', 'dm'), ('m', 'mm'), ('dm', 'cm'), ('cm', 'mm'), ('dm', 'mm')]), 'masse': g_tafel(MASSE, [('t', 'kg'), ('kg', 'g'), ('g', 'mg')]), 'zeit': g_zeit, 'kommaschreibweise': g_komma,
       'rechnen': g_rechnen, 'massstab': g_mst, 'verstehen': g_vers}

DATEI = datei(E, 'Geld, Längen, Massen und Zeitspannen schätzen, umrechnen und damit rechnen – auch in Kommaschreibweise und mit Maßstab.', MERKE,
              [('Größen und Einheiten', ['schaetzen', 'laenge', 'masse', 'zeit']),
               ('Rechnen mit Größen', ['kommaschreibweise', 'rechnen', 'massstab', 'verstehen'])],
              ETAPPEN, GEN,
              offen=['Flächen- und Volumeneinheiten aus „umfang“ hier weggelassen: Flächeneinheiten gehören laut LehrplanPLUS Kl. 5 zum Lernbereich Flächeninhalt (Thema messen.flaechen), Raumeinheiten sind Stoff Kl. 6.',
                     'Dreisatz/Schlussrechnung steht im eigenen Thema groessen.proportional und ist hier nicht noch einmal enthalten.',
                     'Zeichnung (neu): Grundriss beim Maßstab. Eine Karte mit Maßstabsleiste und eine Uhr für Zeitspannen kann die App noch nicht zeichnen.'])

if __name__ == '__main__':
    schreibe(DATEI)
