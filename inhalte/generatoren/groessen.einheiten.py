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

PRUEFUNG = pruefung_erklaerungen(ETAPPEN, 'groessen.einheiten')   # karten[].neu wörtlich übernommen

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
           ('Ein Brief mit zwei Blatt Papier wiegt etwa', 10, 'g', ['kg', 't', 'mg']), ('Ein Lied im Radio dauert etwa', 3, 'min', ['s', 'h', 'd']),
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
        alt = [gr(z, f) for f in falsch]          # gleiche Maßzahl, andere Einheiten – alle verschieden groß (Prüfung)
        return {**wahl_rund(R, r, alt), 'f': {'text': f'Was ist realistisch? {satz.replace(" etwa", "")} ungefähr …'}, 'w': f'{satz} {r}.', 'h': 'Gleiche Maßzahl, andere Einheit: Welche passt zur Wirklichkeit?'}
    art = R.randrange(3)
    if art == 2:
        if R.random() < .5:
            n = R.randint(2, 9)
            return {'y': 'zahl', 'f': {'text': f'Ein Stapel mit 100 Blatt Papier ist etwa 1 cm hoch. Wie viele Blatt sind etwa in einem {n} cm hohen Stapel?'},
                    'o': {'wert': 100 * n, 'toleranz': 10}, 'c': f'100 * {n}', 'w': f'Jeder Zentimeter sind etwa 100 Blatt: {n} · 100 = {zt(100 * n)} Blatt.',
                    'h': 'Wie viele Zentimeter hoch ist der Stapel? Jeder Zentimeter sind 100 Blatt.'}
        sch, km = R.choice([(50, 1), (50, 2), (80, 2), (80, 4), (125, 5), (40, 2), (75, 3)])
        anz = km * 100000 // sch
        return {'y': 'zahl', 'f': {'text': f'Ein Schritt ist etwa {sch} cm lang. Wie viele Schritte brauchst du etwa für {km} km?'},
                'o': {'wert': anz, 'toleranz': 100}, 'c': f'{km} * 100000 / {sch}',
                'w': f'{km} km = {zt(km * 100000)} cm. {zt(km * 100000)} : {sch} = {zt(anz)} Schritte.', 'h': 'Rechne die Strecke in cm um und teile durch die Schrittlänge.'}
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
            x = R.randint(2, 20); d = R.randint(1, k - 1)
            if R.random() < .5:      # die Angabe in der kleineren Einheit ist die größte (Prüfung)
                werte = [(Fr(x), a), (Fr(x * k + d), b), (Fr(x * k - d), b), (Fr(x - 1), a)]
            else:
                werte = [(Fr(x + 1), a), (Fr(x * k + d), b), (Fr(x), a), (Fr(x * k - d), b)]
            if len({umr(v, e2, b, tafel) for v, e2 in werte}) < 4 or min(v for v, _ in werte) <= 0: return g(3)
            groesst = max(werte, key=lambda t: umr(t[0], t[1], b, tafel))
            return {**wahl_rund(R, gr(*groesst), [gr(*t) for t in werte if t != groesst]), 'f': {'text': 'Welche Größe ist am größten: ' + ', '.join(gr(*t) for t in werte) + '?'},
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


ZEIT3 = {'n': 0}


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
        art = R.randrange(5)
        if art == 3:
            s_ = R.randint(70, 600)
            if s_ % 60 == 0: s_ += 13
            return luecke([s_ // 60, s_ % 60], f'Ein Lauf dauert {s_} s. Schreibe die Zeit in Minuten und Sekunden.', '□ min □ s', 'Erst die Minuten, dann die Sekunden.', [f'{s_} // 60', f'{s_} % 60'],
                          f'{s_} : 60 = {s_ // 60} Rest {s_ % 60}: {s_ // 60} min {s_ % 60} s.', 'Eine Minute hat 60 Sekunden.')
        if art == 4:
            a = R.randint(14 * 60, 20 * 60) // 5 * 5; d = R.randint(80, 150) // 5 * 5
            if d % 60 == 0: d += 10
            b = a + d
            return luecke([b // 60, b % 60], f'Ein Film beginnt um {uhr(a)} und dauert {d // 60} h {d % 60} min. Wann endet er?', '□:□ Uhr', 'Stunde ins erste Feld, Minuten ins zweite.',
                          [f'({a} + {d}) // 60', f'({a} + {d}) % 60'], f'{uhr(a)} + {d // 60} h = {uhr(a + d // 60 * 60)}, + {d % 60} min = {uhr(b)}.',
                          'Erst die Stunden addieren, dann die Minuten. Über 60 min gibt es eine Stunde mehr.')
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
    art = ZEIT3['n'] % 3; ZEIT3['n'] += 1          # Stufe 3 reihum: Ankunft, Dauer aus Uhrzeiten, über Mitternacht
    if art == 0:
        a = R.randint(6 * 60, 20 * 60) // 5 * 5
        d = R.randint(40, 200) // 5 * 5
        if d % 60 == 0: d += 25
        b = a + d
        return luecke([b // 60, b % 60], f'Ein Zug fährt um {uhr(a)} ab. Die Fahrt dauert {d // 60} h {d % 60} min. Wann kommt er an?', '□:□ Uhr', 'Stunde ins erste Feld, Minuten ins zweite.',
                      [f'({a} + {d}) // 60', f'({a} + {d}) % 60'], f'{uhr(a)} + {d // 60} h = {uhr(a + d // 60 * 60)}, + {d % 60} min = {uhr(b)}.', 'Erst die Stunden addieren, dann die Minuten. Über 60 min gibt es eine Stunde mehr.')
    if art == 1:      # Dauer aus zwei Uhrzeiten mit krummen Minuten (Prüfung)
        a = R.randint(6 * 60, 19 * 60); d = R.randint(50, 200)
        if a % 5 == 0 or (a + d) % 60 == 0 or d % 60 == 0: return g_zeit(3)
        b = a + d
        bis = 60 - a % 60
        return luecke([d // 60, d % 60], f'Ein Zug fährt um {uhr(a)} ab und kommt um {uhr(b)} an. Wie lange dauert die Fahrt?', '□ h □ min', 'Erst die Stunden, dann die Minuten.',
                      [f'({b} - {a}) // 60', f'({b} - {a}) % 60'],
                      f'Bis {uhr(a + bis)}: {bis} min. Dann bis {uhr(b - b % 60)}: {(b - b % 60 - a - bis) // 60} h. Dann bis {uhr(b)}: {b % 60} min. Zusammen {d // 60} h {d % 60} min.',
                      'Rechne in Schritten: bis zur vollen Stunde, volle Stunden, dann die restlichen Minuten.')
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
                'w': f'1 {g_} = {zt(n)} {k_}: {stellen} Stelle{"n" if stellen > 1 else ""} nach dem Komma. {gr(y, k_)} → {str(y).rjust(stellen, "0")}. Also {gr(v, g_)}.', 'h': f'Nach dem Komma {"steht 1 Stelle" if stellen == 1 else f"stehen {stellen} Stellen"} ({k_}), fehlende mit 0 auffüllen.'}
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
                'c': f'{k} * {m} / 100', 'w': f'Zuerst: 1 cm auf der Karte sind {zt(m)} cm = {zt(m // 100)} m. {k} · {zt(m // 100)} m = {zt(w_cm // 100)} m.', 'h': 'Was ist 1 cm auf der Karte in Wirklichkeit? Rechne das zuerst in m um.'}
    if st == 2:
        if R.random() < .5:
            k = Fr(R.randint(5, 60), 2) if m <= 25000 else Fr(R.randint(2, 20), 2)
            w = k * m
            if (w / 100000).denominator > 100: return g_mst(2)
            return {'y': 'zahl', 'f': {'text': f'Maßstab 1 : {zt(m)}. Auf der Karte misst ein Weg {gr(k, "cm")}. Wie viele km ist er wirklich lang?'}, 'o': {'wert': wert(w / 100000), 'einheit': 'km'},
                    'c': f'{float(k)} * {m} / 100000', 'w': f'Zuerst: 1 cm auf der Karte sind {zt(m)} cm = {zt(Fr(m, 100000))} km. {zt(k)} · {zt(Fr(m, 100000))} km = {zt(w / 100000)} km.', 'h': 'Was ist 1 cm auf der Karte in Wirklichkeit? Rechne das in km um (100 000 cm = 1 km).'}
        km = R.randint(1, 12)
        k = Fr(km * 100000, m)
        if (k * 10).denominator != 1 or k > 40: return g_mst(2)
        return {'y': 'zahl', 'f': {'text': f'Maßstab 1 : {zt(m)}. Wie lang ist eine {km} km lange Strecke auf der Karte (in cm)?'}, 'o': {'wert': wert(k), 'einheit': 'cm'}, 'c': f'{km} * 100000 / {m}',
                'w': f'{km} km = {zt(km * 100000)} cm. {zt(km * 100000)} : {zt(m)} = {zt(k)} cm.', 'h': 'Wirklichkeit in cm umrechnen und durch die Maßstabszahl teilen.'}
    art = R.randrange(3)
    if art == 0 and R.random() < .5:     # Maßstab bestimmen als Zahl (Prüfung)
        if R.random() < .5:
            l, mm_ = R.randint(3, 6), R.choice([20, 25, 50, 100])
            return {'y': 'zahl', 'f': {'text': f'Auf einem Plan ist ein {l} m langes Zimmer {zt(Fr(l * 100, mm_))} cm lang. Welcher Maßstab ist das? Gib die Zahl x in 1 : x an.'},
                    'o': {'wert': mm_}, 'c': f'{l} * 100 / {float(Fr(l * 100, mm_))}', 'w': f'{l} m = {l * 100} cm. {l * 100} : {zt(Fr(l * 100, mm_))} = {mm_}. Maßstab 1 : {mm_}.',
                    'h': 'Rechne die Wirklichkeit in cm um. Wie oft passt die Planlänge hinein?'}
        km, k = R.choice([(2, 8), (1, 4), (3, 6), (5, 5), (1, 10), (4, 8)])
        return {'y': 'zahl', 'f': {'text': f'Ein {km} km langer Weg ist auf der Karte {k} cm lang. Welcher Maßstab ist das? Gib die Zahl x in 1 : x an.'},
                'o': {'wert': km * 100000 // k}, 'c': f'{km} * 100000 / {k}', 'w': f'{km} km = {zt(km * 100000)} cm. {zt(km * 100000)} : {k} = {zt(km * 100000 // k)}. Maßstab 1 : {zt(km * 100000 // k)}.',
                'h': 'Rechne die Wirklichkeit in cm um und teile durch die Kartenlänge.'}
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
    raum = R.choice(['Zimmer', 'Zimmer', 'Turnhalle', 'Garten'])          # Zimmer 3–6 m, größere Maße: Turnhalle, Garten (Prüfung)
    if raum == 'Zimmer': l, b, mm = R.randint(4, 6), R.randint(3, 4), R.choice([50, 100])
    elif raum == 'Turnhalle': l, b, mm = R.choice([(30, 15), (27, 15), (45, 27)]), None, R.choice([300, 500])
    else: l, b, mm = R.choice([(20, 12), (15, 10), (25, 15)]), None, R.choice([200, 500])
    if b is None: l, b = l
    if l == b or (l * 100) % mm or (b * 100) % mm: return g_mst(3)
    artikel = {'Zimmer': 'Ein Zimmer', 'Turnhalle': 'Eine Turnhalle', 'Garten': 'Ein Garten'}[raum]
    a = luecke([l * 100 // mm, b * 100 // mm],
                  f'{artikel} ist {l} m lang und {b} m breit. Zeichne den Grundriss im Maßstab 1 : {mm}. Wie lang und breit wird der Grundriss auf dem Plan (in cm)?', 'Länge □ cm, Breite □ cm', 'Erst die Länge, dann die Breite.',
                  [f'{l} * 100 / {mm}', f'{b} * 100 / {mm}'], f'{l} m = {zt(l * 100)} cm, : {mm} = {l * 100 // mm} cm. {b} m = {zt(b * 100)} cm, : {mm} = {b * 100 // mm} cm.',
                  'Erst in cm umrechnen, dann durch die Maßstabszahl teilen.')
    a['f']['grafik'] = {'typ': 'figur', 'punkte': {'_A': [0, 0], '_B': [l, 0], '_C': [l, b], '_D': [0, b]}, 'flaeche': ['_A', '_B', '_C', '_D'],
                        'linien': [['_A', '_B', f'{l} m'], ['_B', '_C', f'{b} m'], ['_C', '_D'], ['_D', '_A']]}
    return a


# ---------- 8 Verstehen ----------
# Prüfung: alle Antworten mit Begründung, große Zahlen mit Leerzeichen
def g_vers(st):
    if st == 1:
        x = R.randint(2, 9)
        aussagen = [(f'{x} m = {x * 10} cm', f'Nein, 1 m = 100 cm, also {x} m = {x * 100} cm.', ['Ja, 1 m = 10 cm.', f'Nein, {x} m = {zt(x * 1000)} cm.']),
                    (f'{x} kg = {zt(x * 1000)} g', 'Ja, 1 kg = 1 000 g.', [f'Nein, 1 kg = 100 g, also {x * 100} g.', f'Nein, {x} kg = {x * 10} g.']),
                    (f'{x} h = {x * 100} min', f'Nein, 1 h = 60 min, also {x} h = {x * 60} min.', ['Ja, 1 h = 100 min.', f'Nein, {x} h = {zt(x * 3600)} min.']),
                    (f'{x} € = {x * 100} ct', 'Ja, 1 € = 100 ct.', [f'Nein, 1 € = 10 ct, also {x * 10} ct.', f'Nein, {x} € = {zt(x * 1000)} ct.'])]
    elif st == 2:
        x, y = R.randint(1, 9), R.randint(1, 9)
        aussagen = [(f'{x} m {y} cm = {x},{y} m', f'Nein, {y} cm = 0,0{y} m. Also {x},0{y} m.', ['Ja, die Zentimeter stehen direkt hinter dem Komma.', f'Nein, richtig ist {x},00{y} m.']),
                    (f'{x},{y} kg = {x} kg {y}00 g', f'Ja, {x},{y} kg = {zt(x * 1000 + y * 100)} g = {x} kg {y * 100} g.', [f'Nein, {x},{y} kg = {x} kg {y} g.', f'Nein, {x},{y} kg = {x} kg {y * 10} g.']),
                    (f'{x},5 h = {x} h 50 min', 'Nein, 0,5 h ist eine halbe Stunde = 30 min.', ['Ja, nach dem Komma stehen die Minuten.', 'Nein, 0,5 h = 5 min.']),
                    (f'{x},{y}0 € = {x} € {y}0 ct', 'Ja, zwei Stellen nach dem Komma sind Cent.', [f'Nein, {x},{y}0 € = {x} € {y} ct.', f'Nein, {x},{y}0 € = {x} € {y}00 ct.'])]
    else:
        aussagen = [('Ein Ei wiegt etwa 60 kg.', 'Nein, ein Ei wiegt etwa 60 g.', ['Ja, ein Ei wiegt etwa so viel wie eine Tafel Schokolade.', 'Nein, ein Ei wiegt etwa 60 mg.']),
                    ('Ein Klassenzimmer ist etwa 8 m lang.', 'Ja, das ist realistisch (etwa 8 Türbreiten von je 1 m).', ['Nein, ein Klassenzimmer ist etwa 8 cm lang.', 'Nein, ein Klassenzimmer ist etwa 80 m lang.']),
                    ('Mit dem Rad schafft man 15 km in etwa einer Stunde.', 'Ja, Radfahrer fahren etwa 15 km pro Stunde.', ['Nein, mit dem Rad schafft man nur etwa 1,5 km in einer Stunde.', 'Nein, mit dem Rad schafft man etwa 150 km in einer Stunde.']),
                    ('Ein Schulbus ist etwa 12 cm lang.', 'Nein, ein Bus ist etwa 12 m lang.', ['Ja, ein Bus ist etwa so lang wie ein Lineal.', 'Nein, ein Bus ist etwa 12 km lang.']),
                    ('Ein Kind wiegt etwa 40 t.', 'Nein, ein Kind wiegt etwa 40 kg.', ['Ja, 1 t ist dasselbe wie 1 kg.', 'Nein, ein Kind wiegt etwa 40 g.']),
                    ('Ein Fußweg von 1 km dauert etwa 15 min.', 'Ja, man geht etwa 4 bis 5 km in der Stunde.', ['Nein, 1 km zu Fuß dauert etwa 1 min.', 'Nein, 1 km zu Fuß dauert etwa 2 h.']),
                    ('Auf einer Karte 1 : 100 000 ist 1 cm in Wirklichkeit 1 km.', 'Ja, 100 000 cm = 1 000 m = 1 km.', ['Nein, 100 000 cm = 100 km.', 'Nein, 100 000 cm = 10 m.']),
                    ('Auf einer Karte 1 : 10 000 ist 1 cm in Wirklichkeit 10 km.', 'Nein, 10 000 cm = 100 m.', ['Ja, 10 000 cm = 10 km.', 'Nein, 10 000 cm = 1 m.'])]
    s_, grund, falsch = R.choice(aussagen)
    return {**wahl_rund(R, grund, falsch, 3), 'f': {'text': f'Stimmt das? „{s_}“'}, 'w': grund,
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

# Umbau U5 (Achte Runde, Vorgabe 16.11.): Lernkarten nach dem neuen Muster – einstieg, woerter (≤ 3), Kartenbild,
# Bildergeschichte (schritte mit bild), „Pass auf!“ (fehler + fehler_bild), MERKE (regel).
# Situationen: Klassenzimmer, Wäscheleine, Rezept, Kino, Preisschild, Schulweg, Wanderkarte.
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl5.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl5 import umbau  # noqa: E402

RAUM = [['_A', '_B'], ['_B', '_C', '?'], ['_C', '_D'], ['_D', '_A'], ['_T1', '_T4', 'Tür 2 m'], ['_T4', '_T3'], ['_T3', '_T2']]
FILM = [['18:40', '19:00', '20 min'], ['19:00', '20:00', '1 h'], ['20:00', '20:15', '15 min'], ['zusammen', '', '1 h 35 min']]

KARTEN = {
 'schaetzen': {
  'einstieg': 'Wie hoch ist dein Klassenzimmer? Ein Maßband reicht nicht bis zur Decke, also vergleichst du mit der Tür. Sie ist etwa 2 m hoch – eine ⟦Bezugsgröße⟧.',
  'woerter': [['Bezugsgröße', 'etwas, dessen Maß du kennst und mit dem du vergleichst'], ['Einheit', 'das Maß hinter der Zahl: m, kg, min']],
  'bild': {'typ': 'figur', 'punkte': {'_A': [0, 0], '_B': [5, 0], '_C': [5, 3], '_D': [0, 3], '_T1': [1, 0], '_T2': [2, 0], '_T3': [2, 2], '_T4': [1, 2], '_H1': [1.5, 2], '_H2': [1.5, 3]},
           'linien': RAUM},
  'schritte': [{'text': 'Die Tür ist etwa 2 m hoch.'},
               {'text': 'Über der Tür ist noch etwa eine halbe Tür Platz: 1 m.', 'bild': {'linien': RAUM + [['_H1', '_H2', '1 m', 'gestrichelt']]}},
               {'text': 'Zusammen: 2 m + 1 m = ⟦3 m⟧. Zahl und Einheit gehören zusammen.',
                'bild': {'linien': [l if l[:2] != ['_B', '_C'] else ['_B', '_C', '≈ 3 m'] for l in RAUM] + [['_H1', '_H2', '1 m', 'gestrichelt']]}}],
  'fehler': 'Nur auf die Zahl achten: Ein Bleistift ist 18 cm lang, nicht 18 m. 18 m wären ein Haus mit sechs Stockwerken.',
  'regel': 'Schätze mit einer ⟦Bezugsgröße⟧, die du kennst. Tür 2 m, Schokolade 100 g, Schulstunde 45 min. Schreibe immer Zahl und Einheit.'},
 'laenge': {
  'einstieg': 'Eine Wäscheleine ist 7 m lang. Im Bastelladen steht aber alles in Zentimetern. Dieselbe Länge in einer anderen Einheit schreiben heißt ⟦umrechnen⟧.',
  'woerter': [['umrechnen', 'dieselbe Länge in einer anderen Einheit schreiben: 7 m = 700 cm'], ['dm', 'Dezimeter: 10 cm, etwa eine Handbreite'],
              ['Einheitentafel', 'eine Tabelle mit einer Spalte je Einheit; in jede Spalte kommt eine Ziffer']],
  'bild': {'typ': 'stellentafel', 'stellen': ['m', 'dm', 'cm'], 'ziffern': ['', '', '']},
  'schritte': [{'text': 'Schreibe die 7 in der Einheitentafel unter m.', 'bild': {'ziffern': ['7', '', ''], 'markiert': 0}},
               {'text': 'Fülle die Spalten dm und cm mit Nullen.', 'bild': {'ziffern': ['7', '0', '0'], 'markiert': 2}},
               {'text': 'Lies bis cm ab: ⟦7 m = 700 cm⟧.'},
               {'text': 'Zwei Spalten weiter heißt zweimal mal 10, also mal 100.'}],
  'fehler': '7 m = 70 cm ist falsch: Das ist erst eine Spalte weiter, bei dm. Bis cm sind es zwei Spalten, also 700 cm.',
  'fehler_bild': {'ziffern': ['7', '0', ''], 'markiert': 1},
  'regel': 'In die kleinere ⟦Einheit⟧ nimmst du mal, in die größere teilst du. 1 m = 100 cm, 1 km = 1 000 m.'},
 'masse': {
  'einstieg': 'Im Rezept stehen 3 kg Kartoffeln, die Küchenwaage zeigt aber Gramm. Wie viel Gramm musst du abwiegen? Was man im Alltag Gewicht nennt, heißt in Mathe ⟦Masse⟧.',
  'woerter': [['Masse', 'wie schwer etwas ist (im Alltag: Gewicht)'], ['Umrechnungszahl', 'die Zahl, mit der man beim Umrechnen malnimmt oder teilt']],
  'bild': {'typ': 'stellentafel', 'stellen': ['kg', '100 g', '10 g', '1 g'], 'ziffern': ['', '', '', '']},
  'schritte': [{'text': 'Von kg zu g ist die Umrechnungszahl 1 000.'},
               {'text': 'Schreibe die 3 unter kg und fülle die Gramm-Spalten mit Nullen.', 'bild': {'ziffern': ['3', '0', '0', '0'], 'markiert': 0}},
               {'text': 'Abgelesen: ⟦3 kg = 3 000 g⟧.'}],
  'fehler': '3 kg = 300 g ist falsch. Bei Massen ist die Umrechnungszahl 1 000, nicht 100. 300 g wären nur zwei Kartoffeln.',
  'regel': 'Bei Massen ist die ⟦Umrechnungszahl 1 000⟧. 1 kg = 1 000 g und 1 t = 1 000 kg.'},
 'zeit': {
  'einstieg': 'Ein Film beginnt um 18:40 Uhr und endet um 20:15 Uhr. Wie lange dauert er? Die Zeit zwischen Anfang und Ende heißt ⟦Zeitspanne⟧.',
  'woerter': [['Zeitspanne', 'wie lange etwas dauert, zum Beispiel 1 h 35 min'], ['vollen Stunde', 'eine Uhrzeit mit :00, zum Beispiel 19:00 Uhr']],
  'bild': {'typ': 'tabelle', 'kopf': ['von', 'bis', 'Dauer'], 'zeilen': [['18:40', '20:15', '?']]},
  'schritte': [{'text': 'Bis zur vollen Stunde: 18:40 bis 19:00 Uhr sind 20 min.', 'bild': {'zeilen': FILM[:1]}},
               {'text': 'Dann 19:00 bis 20:00 Uhr: 1 h.', 'bild': {'zeilen': FILM[:2]}},
               {'text': 'Der Rest: 20:00 bis 20:15 Uhr sind 15 min.', 'bild': {'zeilen': FILM[:3]}},
               {'text': 'Zusammen: 1 h + 20 min + 15 min = ⟦1 h 35 min⟧.', 'bild': {'zeilen': FILM}}],
  'fehler': 'Uhrzeiten wie normale Zahlen abziehen: 2 015 − 1 840 = 175. Eine Stunde hat aber 60 Minuten, nicht 100.',
  'regel': 'Rechne Zeitspannen ⟦bis zur vollen Stunde⟧ und dann weiter. 1 h = 60 min, 1 min = 60 s, 1 d = 24 h.'},
 'kommaschreibweise': {
  'einstieg': 'Auf dem Preisschild steht 4,07 €: 4 Euro und 7 Cent. Genauso schreibt man Längen: 3,05 m sind 3 m und 5 cm. Das heißt ⟦Kommaschreibweise⟧.',
  'woerter': [['Kommaschreibweise', 'eine Größe mit Komma in einer Einheit: 3,05 m statt 3 m 5 cm']],
  'bild': {'typ': 'stellentafel', 'stellen': ['m', 'dm', 'cm'], 'ziffern': ['', '', '']},
  'schritte': [{'text': 'Schreibe 3 m 5 cm in die Tafel: 3 unter m, 5 unter cm.', 'bild': {'ziffern': ['3', '', '5']}},
               {'text': 'Die leere Spalte dm bekommt eine 0.', 'bild': {'ziffern': ['3', '0', '5'], 'markiert': 1}},
               {'text': 'Das Komma kommt hinter die Meter: ⟦3,05 m⟧.'}],
  'fehler': '3 m 5 cm = 3,5 m ist falsch. 3,5 m sind 3 m 50 cm. Wie beim Geld: 4,50 € sind nicht 4,05 €.',
  'fehler_bild': {'ziffern': ['3', '5', '0'], 'markiert': 1},
  'regel': 'Hinter dem Komma bekommt ⟦jede kleinere Einheit⟧ ihre Stelle. Bei m und cm sind es zwei Stellen, bei kg und g drei.'},
 'rechnen': {
  'einstieg': 'Du gehst 1,2 km zur Schule und danach 350 m zum Bäcker. Kilometer und Meter kann man nicht direkt zusammenzählen. Erst brauchen beide ⟦dieselbe Einheit⟧.',
  'woerter': [['dieselbe Einheit', 'beide Größen in Metern oder beide in Kilometern']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 2000, 'abschnitte': 4, 'beschriftet': 'alle'},
  'schritte': [{'text': '1 km = 1 000 m, also sind 1,2 km = 1 200 m.', 'bild': {'boegen': [{'von': 0, 'bis': 1200, 'name': 'Schule'}]}},
               {'text': 'Dazu kommen 350 m zum Bäcker.', 'bild': {'boegen': [{'von': 0, 'bis': 1200, 'name': 'Schule'}, {'von': 1200, 'bis': 1550, 'name': 'Bäcker'}]}},
               {'text': '1 200 m + 350 m = ⟦1 550 m⟧.', 'bild': {'punkte': [{'wert': 1550}]}}],
  'fehler': '1,2 + 350 = 351,2 ist falsch. Das zählt Kilometer und Meter zusammen, als wären sie dasselbe.',
  'regel': 'Vor plus und minus bringst du beide Größen auf ⟦dieselbe Einheit⟧. Oft rechnet es sich in der kleineren Einheit leichter.'},
 'massstab': {
  'einstieg': 'Auf der Wanderkarte ist dein Weg nur 4 cm lang. Am Rand steht 1 : 25 000. Diese Angabe heißt ⟦Maßstab⟧: 1 cm auf der Karte sind 25 000 cm draußen.',
  'woerter': [['Maßstab', 'sagt, wie stark eine Karte verkleinert ist'], ['1 : 25 000', 'gelesen „eins zu fünfundzwanzigtausend“']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 1000, 'abschnitte': 4, 'beschriftet': 'alle'},
  'schritte': [{'text': '1 cm auf der Karte sind 25 000 cm, also 250 m.', 'bild': {'boegen': [{'von': 0, 'bis': 250, 'name': '1 cm'}]}},
               {'text': 'Dein Weg ist 4 cm lang, also 4-mal 250 m.',
                'bild': {'boegen': [{'von': 0, 'bis': 250, 'name': '1 cm'}, {'von': 250, 'bis': 500}, {'von': 500, 'bis': 750}, {'von': 750, 'bis': 1000}]}},
               {'text': '4 · 250 m = 1 000 m = ⟦1 km⟧.', 'bild': {'punkte': [{'wert': 1000, 'name': 'Ziel'}]}}],
  'fehler': 'Mit dem Maßstab teilen statt malnehmen ist falsch. Auf der Karte ist alles kleiner, draußen also größer.',
  'regel': 'Bei 1 : 25 000 gilt: Wirklichkeit = ⟦Kartenlänge · 25 000⟧. Bei 10 : 1 ist das Bild 10-mal so groß.'},
 'verstehen': {
  'einstieg': 'Jemand erzählt: Sein Schulweg ist 1,5 km lang, zu Fuß braucht er 2 Minuten. So schnell geht niemand! Du prüfst, ob eine Angabe ⟦plausibel⟧ ist.',
  'woerter': [['plausibel', 'glaubwürdig, kann stimmen'], ['realistisch', 'passt zur Wirklichkeit']],
  'bild': {'typ': 'saeulen', 'einheit': 'min', 'werte': [{'name': 'Behauptung', 'wert': 2}], 'y_max': 25},
  'schritte': [{'text': 'Bezugsgröße: 1 km zu Fuß dauert etwa 12 bis 15 min.'},
               {'text': '1,5 km dauern also rund 20 min.', 'bild': {'werte': [{'name': 'Behauptung', 'wert': 2}, {'name': 'realistisch', 'wert': 20}]}},
               {'text': '2 min sind viel zu wenig. Die Angabe ist ⟦unrealistisch⟧.'}],
  'fehler': '„Ein Ei wiegt 60 kg“ hinschreiben, ohne nachzudenken. So viel wiegt ein Erwachsener. Richtig sind 60 g.',
  'regel': 'Prüfe jedes Ergebnis: Passt die ⟦Einheit⟧? Ist die Größe realistisch? Vergleiche mit einer Bezugsgröße.'},
}
umbau(DATEI, KARTEN)


# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl5) ----------
# Neue Übungen nach Prüfungsvorbild (Jahrgangsstufentest 6 Bayern: Umwandeln mit gemischten Einheiten, Größen ordnen,
# Fehler beschreiben, Schätzen mit Bezugsgröße, fehlende Information; Känguru: Zaunpfähle); eigene Zahlen und Einkleidung.
from _schwer_kl5 import A, L, Z, de, einzig, ergaenze, wahl  # noqa: E402


def _schwer():
    N = {}
    N['schaetzen'] = [
        wahl(2, 'Was ist realistisch? Ein Klassenzimmer ist etwa … lang.', ['9 m', '90 m', '9 cm', '900 m'], lambda o: o == '9 m',
             'Ein Klassenzimmer ist etwa so lang wie 4 bis 5 Türen hoch sind: rund 9 m.', 'Vergleiche mit einer Tür (etwa 2 m hoch).'),
        wahl(2, 'Ein Bus ist etwa 12 m lang. Wie viele Busse hintereinander sind ungefähr 1 km lang?', ['8', '80', '800', '8 000'],
             lambda o: abs(int(o.replace(' ', '')) - 1000 / 12) == min(abs(x - 1000 / 12) for x in (8, 80, 800, 8000)),
             '1 km = 1 000 m. 1 000 : 12 ist etwa 83, also ungefähr 80 Busse.', 'Rechne 1 km in m um und teile durch 12.'),
        wahl(3, 'Auf einem Foto steht ein Erwachsener (etwa 1,80 m groß) vor einem Baum. Der Baum ist etwa 6-mal so hoch wie der Mensch. Wie hoch ist der Baum ungefähr?',
             ['etwa 11 m', 'etwa 6 m', 'etwa 110 m', 'etwa 1,1 m'], lambda o: o == f'etwa {round(1.8 * 6)} m',
             '6 · 1,80 m = 10,80 m, also etwa 11 m.', 'Nimm die Größe des Menschen als Maßstab.'),
        wahl(3, 'Ein Herz schlägt etwa 70-mal in der Minute. Wie oft schlägt es ungefähr an einem Tag?', ['etwa 1 000-mal', 'etwa 10 000-mal', 'etwa 100 000-mal', 'etwa 1 000 000-mal'],
             lambda o: o == 'etwa 100 000-mal',
             '70 · 60 = 4 200 Schläge pro Stunde. 4 200 · 24 = 100 800, also etwa 100 000.', 'Rechne zuerst die Schläge pro Stunde aus, dann pro Tag.'),
        Z(3, 'Ein Blatt Papier ist etwa 0,1 mm dick. Wie hoch ist ein Stapel aus 500 Blatt? Gib das Ergebnis in cm an.', '500 * 0.1 / 10',
          '500 · 0,1 mm = 50 mm = 5 cm.', 'Rechne zuerst in mm, dann in cm um.', einheit='cm'),
        wahl(3, 'Ein Neugeborenes wird gewogen. Welche Angabe ist sicher falsch?', ['3 500 g', '3,5 kg', '35 kg', '3 kg 500 g'], lambda o: o == '35 kg',
             '3 500 g, 3,5 kg und 3 kg 500 g sind dasselbe und realistisch. 35 kg wiegt etwa ein Kind in der 5. Klasse.', 'Drei Angaben sind gleich groß. Welche passt nicht dazu?'),
    ]
    N['laenge'] = [
        Z(2, 'Rechne um: 3 km 40 m = ? m', '3 * 1000 + 40', '3 km = 3 000 m. Dazu 40 m: 3 040 m.', 'Achtung: 40 m sind keine 400 m.', einheit='m'),
        Z(2, 'Rechne um: 4 500 mm = ? dm', '4500 / 100', 'Von mm zu dm sind es zwei Stufen: : 10 und : 10, also : 100. 4 500 : 100 = 45 dm.', 'mm → cm → dm: zweimal durch 10.', einheit='dm'),
        Z(3, 'Wandle um: 15 m 4 cm = ? cm', '15 * 100 + 4', '15 m = 1 500 cm. Dazu 4 cm: 1 504 cm. Nicht 154 cm!', 'Rechne zuerst die Meter in Zentimeter um.', einheit='cm'),
        Z(3, 'Wandle um: 382 dm = ? mm', '382 * 100', 'dm → cm: mal 10, cm → mm: mal 10. 382 · 100 = 38 200 mm.', 'Wie viele Stufen sind es von dm bis mm?', einheit='mm'),
        Z(3, 'Ein Zebrastreifen beginnt und endet mit einem dunklen Streifen. Es gibt 8 weiße Streifen. Jeder Streifen ist 50 cm breit. Wie breit ist die Straße in m?',
          '(8 + 9) * 50 / 100', 'Zwischen und neben 8 weißen Streifen liegen 9 dunkle: 17 Streifen. 17 · 50 cm = 850 cm = 8,5 m.',
          'Zeichne eine Skizze. Wie viele dunkle Streifen gibt es bei 8 weißen?', einheit='m'),
        Z(3, 'Ein Zaun ist 24 m lang. Alle 3 m steht ein Pfosten, auch ganz am Anfang und ganz am Ende. Wie viele Pfosten sind es?', '24 // 3 + 1',
          '24 : 3 = 8 Abstände. Dazu kommt ein Pfosten mehr als Abstände: 9 Pfosten.', 'Zeichne einen kurzen Zaun, z. B. 6 m. Zähle Abstände und Pfosten.'),
    ]
    klein = {'2,08 kg': 2080, '2 kg 80 g': 2080, '2 kg 8 g': 2008, '2 800 g': 2800}
    N['masse'] = [
        Z(2, 'Rechne um: 2 t 50 kg = ? kg', '2 * 1000 + 50', '2 t = 2 000 kg. Dazu 50 kg: 2 050 kg.', 'Die Umrechnungszahl ist 1 000.', einheit='kg'),
        Z(2, 'Rechne um: 4 500 mg = ? g', '4500 / 1000', 'Von mg zu g: durch 1 000. 4 500 : 1 000 = 4,5 g.', 'Wie viele mg sind 1 g?', einheit='g'),
        wahl(3, 'Welche Masse ist am kleinsten?', list(klein), lambda o: klein[o] == min(klein.values()),
             'In Gramm: 2 080 g, 2 080 g, 2 008 g und 2 800 g. Am kleinsten ist 2 kg 8 g = 2 008 g.', 'Rechne alle Angaben in Gramm um.'),
        Z(3, 'Ein Lieferwagen wiegt leer 2 t 300 kg. Er darf mit Ladung höchstens 3,5 t wiegen. Geladen sind 40 Kisten zu je 25 kg. Wie viele kg darf er noch zuladen?',
          '3500 - 2300 - 40 * 25', 'Erlaubte Ladung: 3 500 kg − 2 300 kg = 1 200 kg. Geladen: 40 · 25 kg = 1 000 kg. Noch frei: 200 kg.',
          'Rechne alles in kg um.', einheit='kg'),
        Z(3, 'Ein volles Honigglas wiegt 750 g. Das leere Glas wiegt 250 g. Wie viel wiegt das Glas, wenn nur noch halb so viel Honig darin ist?', '250 + (750 - 250) // 2',
          'Honig: 750 g − 250 g = 500 g. Die Hälfte sind 250 g. Mit Glas: 250 g + 250 g = 500 g.', 'Rechne zuerst aus, wie viel der Honig allein wiegt.', einheit='g'),
        A(3, 'Jemand schreibt: 3 kg − 250 g = 2 kg 750 g = 2,75 kg. Stimmt das?', 'Ja, beides stimmt.',
          ['Nein, es sind 2,250 kg.', 'Nein, kg und g darf man nicht voneinander abziehen.', 'Nein, 2 kg 750 g sind 2,075 kg.'],
          '3 kg = 3 000 g. 3 000 g − 250 g = 2 750 g = 2 kg 750 g = 2,75 kg.', 'Rechne alles in Gramm und prüfe Schritt für Schritt.'),
    ]
    N['zeit'] = [
        Z(2, 'Wie viele Sekunden sind 3 min 20 s?', '3 * 60 + 20', '3 min = 180 s. Dazu 20 s: 200 s.', '1 min = 60 s.', einheit='s'),
        Z(2, 'Wie viele Stunden sind 3 Tage und 5 Stunden?', '3 * 24 + 5', '3 · 24 h = 72 h. Dazu 5 h: 77 h.', '1 Tag = 24 h.', einheit='h'),
        Z(3, 'Ein Kind beginnt um 15:50 Uhr mit den Hausaufgaben und braucht 1 h 25 min. Um 17:30 Uhr beginnt das Training, der Weg dauert 20 min. Wie viele Minuten kommt es zu spät?',
          '(15 * 60 + 50 + 85 + 20) - (17 * 60 + 30)', 'Fertig um 17:15 Uhr, am Training um 17:35 Uhr. Das sind 5 min zu spät.',
          'Rechne Schritt für Schritt: Wann ist es mit den Hausaufgaben fertig, wann beim Training?', einheit='min'),
        A(3, 'Jemand rechnet: 3 h 15 min = 315 min. Was ist falsch?', 'Eine Stunde hat 60 min, nicht 100. Richtig: 195 min.',
          ['Nichts, 315 min stimmt.', 'Richtig ist 3 h 15 min = 3,15 h.', 'Richtig ist 45 min.'],
          '3 h = 3 · 60 min = 180 min. Dazu 15 min: 195 min.', 'Wie viele Minuten hat eine Stunde?'),
        L(3, 'Eine Uhr geht jeden Tag 4 Minuten nach. Am Montag um 12:00 Uhr wird sie richtig gestellt. Was zeigt sie genau eine Woche später, wenn es wirklich 12:00 Uhr ist?',
          '□:□ Uhr', 'Trage Stunde und Minute ein.', ['(12 * 60 - 7 * 4) // 60', '(12 * 60 - 7 * 4) % 60'],
          'In 7 Tagen geht sie 7 · 4 = 28 min nach. Sie zeigt 12:00 Uhr − 28 min = 11:32 Uhr.', '„Nachgehen“ heißt: Die Uhr zeigt eine frühere Zeit.'),
        L(3, 'Ein Film dauert 135 min und endet um 21:10 Uhr. Wann hat er begonnen?', '□:□ Uhr', 'Trage Stunde und Minute ein.',
          ['(21 * 60 + 10 - 135) // 60', '(21 * 60 + 10 - 135) % 60'],
          '135 min = 2 h 15 min. 21:10 Uhr − 2 h = 19:10 Uhr, minus 15 min = 18:55 Uhr.', 'Rechne 135 min in Stunden und Minuten um und gehe rückwärts.'),
    ]
    lang = {'1,5 km': 1500, '1 km 50 m': 1050, '1 005 m': 1005, '1,505 km': 1505}
    nicht = {'6 m 4 cm': 604, '604 cm': 604, '60,4 dm': 604, '6 m 40 cm': 640}
    N['kommaschreibweise'] = [
        Z(2, 'Schreibe in Kommaschreibweise: 7 kg 45 g = ? kg', '7 + 45 / 1000', 'Gramm brauchen drei Stellen nach dem Komma: 45 g = 0,045 kg. Also 7,045 kg.',
          'Bei kg und g gibt es drei Stellen nach dem Komma.', einheit='kg'),
        Z(2, 'Schreibe in Kommaschreibweise: 8 m 9 cm = ? m', '8 + 9 / 100', 'Zwei Stellen für cm: 9 cm = 0,09 m. Also 8,09 m.', 'Die leere dm-Stelle bekommt eine 0.', einheit='m'),
        wahl(3, 'Welche Länge ist die zweitkleinste: 1,5 km; 1 km 50 m; 1 005 m; 1,505 km?', list(lang), lambda o: lang[o] == sorted(lang.values())[1],
             'In Meter: 1 500 m, 1 050 m, 1 005 m, 1 505 m. Der Größe nach: 1 005 < 1 050 < 1 500 < 1 505. Die zweitkleinste ist 1 km 50 m.',
             'Rechne alle Längen in Meter um.'),
        Z(3, 'Schreibe 4 km 30 m in km.', '4 + 30 / 1000', '30 m = 0,030 km. Also 4,03 km (nicht 4,3 km).', 'Bei km und m gibt es drei Stellen nach dem Komma.', einheit='km'),
        A(3, 'Jemand schreibt 2 kg 5 g = 2,5 kg. Was ist falsch?', 'Gramm brauchen drei Stellen: richtig ist 2,005 kg.',
          ['Nichts, das stimmt.', 'Richtig ist 2,05 kg.', 'Richtig ist 25 kg.'],
          '2,5 kg wären 2 kg 500 g. 5 g sind 0,005 kg, also 2,005 kg.', 'Schreibe die Zahl in eine Einheitentafel.'),
        wahl(3, 'Welche Angabe ist NICHT dasselbe wie 6,04 m?', list(nicht), lambda o: nicht[o] != 604,
             '6,04 m = 604 cm = 6 m 4 cm = 60,4 dm. 6 m 40 cm wären 6,40 m.', 'Rechne alle Angaben in cm um.'),
    ]
    N['rechnen'] = [
        Z(2, 'Berechne 2 m − 35 cm. Gib das Ergebnis in cm an.', '200 - 35', '2 m = 200 cm. 200 cm − 35 cm = 165 cm.', 'Rechne zuerst in dieselbe Einheit um.', einheit='cm'),
        Z(2, 'Berechne 1,5 kg + 750 g. Gib das Ergebnis in g an.', '1500 + 750', '1,5 kg = 1 500 g. 1 500 g + 750 g = 2 250 g.', 'Rechne kg in g um.', einheit='g'),
        A(3, 'Jemand rechnet 8 m − 40 cm = 80 cm − 40 cm = 40 cm. Was ist falsch?', '8 m sind 800 cm, nicht 80 cm. Richtig: 760 cm.',
          ['Nichts, 40 cm stimmt.', 'Man darf m und cm nicht abziehen.', 'Richtig ist 8 m − 40 m = −32 m.'],
          '1 m = 100 cm, also 8 m = 800 cm. 800 cm − 40 cm = 760 cm.', 'Wie viele cm hat ein Meter?'),
        Z(3, 'Für ein Klassenfest werden 3 Kuchen zu je 7,50 € gekauft. Vom Rest der 50 € gibt es Saft. Eine Flasche kostet 2,40 €. Wie viele Flaschen können höchstens gekauft werden?',
          '(50 - 3 * 7.5) // 2.4', 'Kuchen: 3 · 7,50 € = 22,50 €. Rest: 27,50 €. 11 Flaschen kosten 26,40 €, 12 Flaschen 28,80 € – zu viel. Also 11.',
          'Rechne zuerst den Rest aus. Probiere dann 10, 11, 12 Flaschen.'),
        wahl(3, 'Eine Leiste ist 3,60 m lang. Sie soll ohne Rest in gleich lange Stücke gesägt werden. Welche Stücklänge geht?', ['25 cm', '35 cm', '40 cm', '70 cm'],
             lambda o: 360 % int(o.split()[0]) == 0, '3,60 m = 360 cm. 360 : 40 = 9 geht ohne Rest. 360 : 25, 360 : 35 und 360 : 70 lassen einen Rest.',
             'Rechne 3,60 m in cm um und prüfe, welche Länge ohne Rest hineinpasst.'),
        Z(3, 'Ein leerer Korb wiegt 400 g. Mit 6 gleich schweren Äpfeln wiegt er 1,3 kg. Wie viele Gramm wiegt ein Apfel?', '(1300 - 400) / 6',
          '1,3 kg = 1 300 g. Äpfel zusammen: 1 300 g − 400 g = 900 g. Ein Apfel: 900 g : 6 = 150 g.', 'Rechne alles in g. Was wiegen die Äpfel ohne Korb?', einheit='g'),
    ]
    N['massstab'] = [
        Z(2, 'Maßstab 1 : 200 000. Auf der Karte sind es 3,5 cm. Wie viele km sind es in Wirklichkeit?', '3.5 * 200000 / 100000',
          '3,5 cm · 200 000 = 700 000 cm = 7 000 m = 7 km.', '1 km = 100 000 cm.', einheit='km'),
        Z(2, 'Ein Modellauto ist im Maßstab 1 : 20 gebaut und 21 cm lang. Wie lang ist das echte Auto in m?', '21 * 20 / 100',
          '21 cm · 20 = 420 cm = 4,20 m.', 'Wirklichkeit = Modelllänge · 20.', einheit='m'),
        L(3, 'Ein Floh ist 2 mm lang. Im Buch ist er 3 cm groß abgebildet. Wie heißt der Maßstab?', '□ : 1', 'Trage die Zahl vor dem Doppelpunkt ein.', ['30 // 2'],
          '3 cm = 30 mm. 30 mm : 2 mm = 15. Das Bild ist 15-mal so groß: 15 : 1.', 'Rechne beide Längen in mm um. Wie oft passt 2 mm in das Bild?'),
        L(3, 'Zwei Orte sind auf einer Karte im Maßstab 1 : 25 000 genau 8 cm voneinander entfernt. Auf einer anderen Karte sind es 4 cm. Welchen Maßstab hat die zweite Karte?',
          '1 : □', 'Trage die Zahl hinter dem Doppelpunkt ein.', ['8 * 25000 // 4'],
          'Wirklich: 8 cm · 25 000 = 200 000 cm. Auf der zweiten Karte sind das 4 cm: 200 000 : 4 = 50 000. Maßstab 1 : 50 000.',
          'Rechne zuerst die wirkliche Entfernung aus.'),
        Z(3, 'Auf einem Plan im Maßstab 1 : 100 ist ein Zimmer 4 cm lang und 3 cm breit. Wie viele m² hat das Zimmer in Wirklichkeit?', '(4 * 100 // 100) * (3 * 100 // 100)',
          'Länge: 4 cm · 100 = 400 cm = 4 m. Breite: 3 m. Fläche: 4 m · 3 m = 12 m².', 'Rechne zuerst Länge und Breite in Wirklichkeit aus, dann die Fläche.', einheit='m²'),
        A(3, 'Jemand sagt: „Bei 1 : 50 000 sind 2 cm auf der Karte 100 m in Wirklichkeit.“ Stimmt das?', 'Nein: 2 cm · 50 000 = 100 000 cm = 1 km.',
          ['Ja, das stimmt.', 'Nein, es sind 10 m.', 'Nein, es sind 100 km.'],
          '2 · 50 000 = 100 000 cm. 100 000 cm = 1 000 m = 1 km.', 'Rechne 100 000 cm schrittweise in m um.'),
    ]
    zeiten = {'1,5 h': 90, '100 min': 100, '1 h 35 min': 95, '5 400 s': 90}
    N['verstehen'] = [
        wahl(2, 'Stimmt das? „1,25 h = 1 h 25 min“', ['Nein, 0,25 h ist eine Viertelstunde = 15 min.', 'Ja, nach dem Komma stehen die Minuten.', 'Nein, 0,25 h = 2 min 5 s.'],
             lambda o: o.startswith('Nein, 0,25 h ist'), '0,25 h ist ein Viertel einer Stunde: 60 min : 4 = 15 min. Also 1,25 h = 1 h 15 min.',
             'Eine Stunde hat 60 min, nicht 100.'),
        wahl(2, 'Welche Angabe ist gleich 2 500 m?', ['2,5 km', '25 km', '250 km', '2,05 km'], lambda o: o == '2,5 km',
             '1 km = 1 000 m. 2 500 m = 2 km 500 m = 2,5 km.', 'Teile durch 1 000.'),
        wahl(3, 'Ein Kind hat 35 € gespart. Es kauft 2 Bücher und hat danach noch 11 € übrig. Welche Frage kann man damit NICHT beantworten?',
             ['Wie viel haben beide Bücher zusammen gekostet?', 'Wie viel kostet ein Buch, wenn beide gleich teuer sind?', 'Wie teuer war das teurere Buch?', 'Wie viel Geld hat das Kind ausgegeben?'],
             lambda o: o == 'Wie teuer war das teurere Buch?',
             'Zusammen 24 € ausgegeben, gleich teuer je 12 €. Wie sich 24 € auf zwei verschieden teure Bücher verteilen, weiß man nicht.',
             'Prüfe bei jeder Frage, ob die Angaben dafür reichen.'),
        A(3, 'Jemand sagt: „450 g ist mehr als 0,5 kg, weil 450 größer ist als 0,5.“ Stimmt das?', 'Nein: 0,5 kg = 500 g, und 500 g ist mehr als 450 g.',
          ['Ja, 450 ist größer als 0,5.', 'Nein, beide sind gleich schwer.', 'Man kann g und kg nicht vergleichen.'],
          'Vor dem Vergleichen in dieselbe Einheit umrechnen: 0,5 kg = 500 g > 450 g.', 'Rechne zuerst beide Angaben in dieselbe Einheit um.'),
        wahl(3, 'Ein Lkw soll 1 000 Schulranzen zu je etwa 4 kg transportieren. Jemand rechnet mit 40 t Ladung. Ist das realistisch?',
             ['Nein, 1 000 Ranzen wiegen nur etwa 4 t.', 'Ja, 1 000 · 4 kg = 40 t.', 'Nein, sie wiegen etwa 400 t.', 'Ja, Lkw laden immer 40 t.'],
             lambda o: o.startswith('Nein, 1 000 Ranzen'), '1 000 · 4 kg = 4 000 kg = 4 t. 40 t ist zehnmal zu viel.', 'Rechne 1 000 · 4 kg aus und wandle in t um.'),
        wahl(3, 'Welche Zeitspanne ist am längsten: 1,5 h; 100 min; 1 h 35 min; 5 400 s?', list(zeiten), lambda o: zeiten[o] == max(zeiten.values()),
             'In Minuten: 1,5 h = 90 min, 100 min, 1 h 35 min = 95 min, 5 400 s = 90 min. Am längsten sind 100 min.', 'Rechne alle Angaben in Minuten um.'),
    ]
    return N


ergaenze(DATEI, _schwer(), 1025)

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('groessen.einheiten', 13_5_4)
# a) richtige Antwort ist jedes Mal die „runde“ Zahl mit der größeren Einheit – ohne Umrechnen lösbar → Stufe 2
BF.stufe('laenge', 'Welche Größe ist am größten: 6 km, 5 887 m, 5 km, 4 113 m?', 2)
for _t in ['Welche Größe ist am größten: 7 kg, 6 920 g, 6 kg, 5 080 g?', 'Welche Größe ist am größten: 11 kg, 10 322 g, 10 kg, 9 678 g?',
           'Welche Größe ist am größten: 10 kg, 9 042 g, 9 kg, 8 958 g?', 'Welche Größe ist am größten: 5 t, 4 055 kg, 4 t, 3 945 kg?']:
    BF.stufe('masse', _t, 2)
# a) offensichtlich → Stufe 1
BF.stufe('verstehen', 'Stimmt das? „Ein Kind wiegt etwa 40 t.“', 1)
# a) gleicher Typ wie Stufe 1 (t → kg, Nullen anhängen)
BF.stufe('masse', 'Rechne um: 32 t = ? kg', 1)

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl5, siehe _durchsicht_kl5.py) ----
from _durchsicht_kl5 import Durchsicht, durchsicht_anwenden  # noqa: E402

DS = Durchsicht('groessen.einheiten', 19_5_11)
# a) Stufe 3 mit dem Gedanken von Stufe 2 (Zerlegen in zwei Einheiten, Ankunftszeit, zwei Rechenschritte beim Einkauf) → Stufe 2
for _lz, _t in [('laenge', 'Zerlege: 986 cm = □ m □ cm'),
        ('laenge', 'Zerlege: 215 mm = □ cm □ mm'),
        ('laenge', 'Zerlege: 321 mm = □ cm □ mm'),
        ('laenge', 'Zerlege: 626 mm = □ dm □ mm'),
        ('laenge', 'Wandle um: 382 dm = ? mm'),
        ('masse', 'Zerlege: 1 069 g = □ kg □ g'),
        ('masse', 'Zerlege: 3 608 g = □ kg □ g'),
        ('zeit', 'Ein Zug fährt um 13:05 Uhr ab. Die Fahrt dauert 3 h 15 min. Wann kommt er an?'),
        ('zeit', 'Ein Zug fährt um 18:10 Uhr ab. Die Fahrt dauert 1 h 10 min. Wann kommt er an?'),
        ('zeit', 'Ein Zug fährt um 6:20 Uhr ab. Die Fahrt dauert 1 h 5 min. Wann kommt er an?'),
        ('kommaschreibweise', 'Schreibe 4 km 30 m in km.'),
        ('rechnen', 'Einkauf: Brot 4,84 €, Käse 1,71 €, Obst 2,78 €. Bezahlt wird mit 20 €. Wie viel Rückgeld gibt es?'),
        ('rechnen', 'Einkauf: Brot 5,78 €, Käse 4,32 €, Obst 3,07 €. Bezahlt wird mit 20 €. Wie viel Rückgeld gibt es?'),
        ('rechnen', 'Einkauf: Brot 4,53 €, Käse 2,68 €, Obst 6,34 €. Bezahlt wird mit 20 €. Wie viel Rückgeld gibt es?'),
        ('rechnen', 'Ein Kind fährt an 4 Schultagen mit dem Rad zur Schule und zurück. Der Schulweg ist 2,5 km lang. Wie viele km sind das in der Woche?')]:
    DS.stufe(_lz, _t, 2, enthaelt=lambda x: x['s'] == 3)
durchsicht_anwenden(DATEI, DS)
# ---- DURCHSICHT ENDE ----

if __name__ == '__main__':
    schreibe(DATEI)
