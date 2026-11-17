#!/usr/bin/env python3
"""Thema groessen.verhaeltnisse – Verhältnisse und Raten (IB MYP 2, etwa Klasse 7)."""
import sys
from math import gcd
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403

start(2702)

HV = 'Zahlen ohne Einheit, ganz gekürzt'
DINGE = [('Mädchen', 'Jungen', 'In einer Klasse sind'), ('rote', 'blaue Perlen', 'In einer Dose liegen'),
         ('Erwachsene', 'Kinder', 'Im Zoo sind heute'), ('Äpfel', 'Birnen', 'In einer Kiste liegen'),
         ('Laubbäume', 'Nadelbäume', 'Im Park stehen')]


def ratio_luecke(text, a, b, w, h, c=None):
    return luecken(text, '□ : □', HV, [a, b], w, h, c=c)


ETAPPEN = [
    {'lernziel': 'kuerzen', 'titel': 'Verhältnisse kürzen',
     'regel': 'Ein ⟦Verhältnis⟧ (ratio) a : b vergleicht zwei Größen. Man ⟦kürzt⟧ (simplify) es wie einen Bruch: beide Zahlen durch dieselbe Zahl teilen, bis kein gemeinsamer Teiler mehr übrig ist. Bei Größen zuerst ⟦dieselbe Einheit⟧ herstellen.',
     'schritte': ['12 Mädchen und 18 Jungen: Verhältnis 12 : 18.', 'Der größte gemeinsame Teiler ist 6: 12 : 6 = 2 und 18 : 6 = 3.', 'Gekürzt: ⟦2 : 3⟧.'],
     'probe': '2 · 6 = 12 und 3 · 6 = 18 ✓',
     'fehler': '1 m : 25 cm = 1 : 25 ist falsch: Die Einheiten sind verschieden. Erst umrechnen: 100 cm : 25 cm = ⟦4 : 1⟧.'},
    {'lernziel': 'gleichwertig', 'titel': 'Gleichwertige Verhältnisse',
     'regel': 'Zwei Verhältnisse sind ⟦gleichwertig⟧ (equivalent), wenn man beide Zahlen mit ⟦derselben Zahl multipliziert⟧ (oder dividiert). 2 : 3 = 4 : 6 = 10 : 15. ⟦Addieren⟧ derselben Zahl ändert das Verhältnis.',
     'schritte': ['Gesucht: 3 : 5 = □ : 20.', 'Von 5 nach 20 multipliziert man mit 4.', 'Also auch 3 · 4 = 12: ⟦3 : 5 = 12 : 20⟧.'],
     'probe': '12 : 20 gekürzt mit 4 ergibt 3 : 5 ✓',
     'fehler': '3 : 5 = 18 : 20 („zu beiden 15 addiert“) ist falsch: Bei Verhältnissen wird ⟦multipliziert⟧, nicht addiert. Richtig ist 12 : 20.'},
    {'lernziel': 'aufteilen', 'titel': 'Im Verhältnis aufteilen',
     'regel': 'Um eine Menge im Verhältnis a : b aufzuteilen, zählst du die ⟦Teile⟧ zusammen (a + b), berechnest ⟦einen Teil⟧ und nimmst ihn a-mal bzw. b-mal.',
     'schritte': ['120 € im Verhältnis 3 : 5 aufteilen: 3 + 5 = 8 Teile.', 'Ein Teil: 120 € : 8 = 15 €.', 'Anteile: 3 · 15 € = ⟦45 €⟧ und 5 · 15 € = ⟦75 €⟧.'],
     'probe': '45 € + 75 € = 120 € ✓',
     'bild': {'typ': 'saeulen', 'einheit': '€', 'werte': [{'name': '3 Teile', 'wert': 45}, {'name': '5 Teile', 'wert': 75}], 'zahlen': True},
     'fehler': '120 € : 3 = 40 € und 120 € : 5 = 24 € ist falsch: Zusammen wären das nur 64 €. Man teilt durch die ⟦Summe der Teile⟧ (8), nicht durch jede Zahl einzeln.'},
    {'lernziel': 'proportion', 'titel': 'Proportionen lösen',
     'regel': 'Eine ⟦Proportion⟧ (proportion) ist eine Gleichung zweier Verhältnisse: a : b = c : d. Ist ein Wert unbekannt, findest du den ⟦Faktor⟧ zwischen den bekannten Zahlen oder rechnest über ⟦eins⟧ (Dreisatz).',
     'schritte': ['Für 4 Portionen braucht man 300 g Mehl. Wie viel für 6 Portionen?', '4 : 300 = 6 : x. Eine Portion: 300 g : 4 = 75 g.', '6 Portionen: 6 · 75 g = ⟦450 g⟧.'],
     'probe': '450 : 6 = 75 = 300 : 4 ✓',
     'fehler': '6 Portionen = 300 g + 2 g = 302 g („2 Portionen mehr“) ist falsch: Die Menge wächst ⟦im gleichen Verhältnis⟧, nicht um die Differenz der Portionen.'},
    {'lernziel': 'einheitsrate', 'titel': 'Einheitsraten und Stückpreise',
     'regel': 'Eine ⟦Rate⟧ (rate) vergleicht zwei Größen mit verschiedenen Einheiten, z. B. km pro Stunde. Die ⟦Einheitsrate⟧ (unit rate) bezieht sich auf ⟦genau 1⟧ Einheit: Preis pro Stück, pro kg, pro 100 g. So lassen sich Angebote vergleichen.',
     'schritte': ['Packung A: 750 g für 3,00 €. Packung B: 500 g für 2,20 €.', 'Pro 100 g: A 3,00 € : 7,5 = 0,40 €; B 2,20 € : 5 = 0,44 €.', '⟦Packung A ist günstiger⟧.'],
     'probe': '0,40 € · 7,5 = 3,00 € ✓',
     'fehler': 'B ist billiger, weil 2,20 € < 3,00 € – das ist falsch: B enthält auch weniger. Vergleichen kann man nur den ⟦Preis pro gleicher Menge⟧.'},
    {'lernziel': 'aenderung', 'titel': 'Änderungsraten berechnen',
     'regel': 'Die ⟦Änderungsrate⟧ (rate of change) sagt, wie stark sich eine Größe ⟦pro Einheit⟧ der anderen ändert: Änderungsrate = ⟦Zunahme der Größe : Zeitspanne⟧. Nimmt die Größe ab, ist die Rate ⟦negativ⟧.',
     'schritte': ['Um 9 Uhr zeigt das Thermometer 12 °C, um 13 Uhr 20 °C.', 'Änderung: 20 − 12 = 8 °C in 13 − 9 = 4 Stunden.', 'Rate: 8 : 4 = ⟦2 °C pro Stunde⟧.'],
     'probe': '12 °C + 4 · 2 °C = 20 °C ✓',
     'bild': {'typ': 'koordinaten', 'x': [8, 14], 'y': [0, 24], 'punkte': [{'x': 9, 'y': 12, 'name': '9 Uhr'}, {'x': 13, 'y': 20, 'name': '13 Uhr'}],
              'graphen': [{'art': 'linear', 'm': 2, 't': -6, 'bereich': [9, 13]}], 'name_x': 'Uhrzeit', 'name_y': '°C', 'schritt_y': 4},
     'fehler': '20 : 13 ≈ 1,5 °C pro Stunde ist falsch: Man teilt nicht die Endwerte, sondern die ⟦Änderungen⟧: (20 − 12) : (13 − 9) = 2.'},
]


def g_kuerzen(s):
    if s == 1:
        a, b = R.randint(1, 9), R.randint(1, 9)
        if gcd(a, b) != 1 or a == b: return None
        k = R.randint(2, 9)
        n1, n2, vor = R.choice(DINGE)
        return ratio_luecke(f'{vor} {a * k} {n1} und {b * k} {n2}. Gib das Verhältnis {n1} : {n2} gekürzt an.', a, b,
                            f'Größter gemeinsamer Teiler: {k}. {a * k} : {k} = {a}, {b * k} : {k} = {b}. Also {a} : {b}.',
                            'Teile beide Zahlen durch ihren größten gemeinsamen Teiler.', c=[f'{a * k} // {k}', f'{b * k} // {k}'])
    art = R.choice({2: ['einheit', 'einheit', 'zahl'], 3: ['drei', 'komma', 'einheit_gross']}[s])
    if art == 'zahl':
        a, b = R.randint(2, 15), R.randint(2, 15)
        if gcd(a, b) != 1 or a == b: return None
        k = R.choice([6, 8, 12, 15, 16, 25])
        return ratio_luecke(f'Kürze das Verhältnis {a * k} : {b * k} so weit wie möglich.', a, b,
                            f'{a * k} und {b * k} haben den größten gemeinsamen Teiler {k}. Gekürzt: {a} : {b}.',
                            'Kürze schrittweise, z. B. erst durch 2, dann weiter, bis es nicht mehr geht.', c=[f'{a * k} // {k}', f'{b * k} // {k}'])
    if art in ('einheit', 'einheit_gross'):
        typ = R.choice([('m', 'cm', 100), ('kg', 'g', 1000), ('h', 'min', 60), ('€', 'ct', 100), ('l', 'ml', 1000)])
        g1, g2, f = typ
        while True:
            a, b = R.randint(1, 5), R.choice([5, 10, 15, 20, 25, 30, 40, 45, 50, 75, 120, 150, 200, 250, 300, 400, 500, 750])
            if b < f * a and b != f and (f * a) % gcd(f * a, b) == 0: break
        x, y = f * a, b
        t = gcd(x, y)
        if art == 'einheit_gross' and R.random() < .5:
            return ratio_luecke(f'Kürze das Verhältnis {dz(b)} {g2} : {a} {g1}.', y // t, x // t,
                                f'{a} {g1} = {dz(x)} {g2}. {dz(y)} : {dz(x)} gekürzt durch {t}: {y // t} : {x // t}.',
                                f'Rechne zuerst {g1} in {g2} um.', c=[f'{y} // {t}', f'{x} // {t}'])
        return ratio_luecke(f'Kürze das Verhältnis {a} {g1} : {dz(b)} {g2}.', x // t, y // t,
                            f'{a} {g1} = {dz(x)} {g2}. {dz(x)} : {dz(y)} gekürzt durch {t}: {x // t} : {y // t}.',
                            f'Rechne zuerst {g1} in {g2} um.', c=[f'{x} // {t}', f'{y} // {t}'])
    if art == 'drei':
        a, b, c = R.sample(range(1, 10), 3)
        if gcd(gcd(a, b), c) != 1: return None
        k = R.randint(2, 8)
        return luecken(f'Ein Saft wird aus {a * k} l Orangensaft, {b * k} l Apfelsaft und {c * k} l Wasser gemischt. Gib das Verhältnis gekürzt an.',
                       '□ : □ : □', HV, [a, b, c], f'Alle drei Zahlen durch {k} teilen: {a} : {b} : {c}.',
                       'Auch bei drei Zahlen: durch den gemeinsamen Teiler aller drei teilen.', c=[f'{a * k} // {k}', f'{b * k} // {k}', f'{c * k} // {k}'])
    # komma
    a, b = R.randint(1, 9), R.randint(1, 9)
    if gcd(a, b) != 1 or a == b: return None
    return ratio_luecke(f'Kürze das Verhältnis {dz(a / 2)} : {dz(b / 2)} auf ganze Zahlen.', a, b,
                        f'Mit 2 multiplizieren: {dz(a / 2)} · 2 = {a}, {dz(b / 2)} · 2 = {b}. Also {a} : {b}.',
                        'Multipliziere zuerst beide Zahlen, bis keine Kommazahl mehr da ist.', c=[f'{a / 2} * 2', f'{b / 2} * 2'])


def g_gleichwertig(s):
    a, b = R.randint(1, 9), R.randint(2, 12)
    if gcd(a, b) != 1 or a == b: return None
    k = R.randint(2, 9) if s < 3 else R.randint(3, 12)
    art = R.choice({1: ['luecke_hinten', 'luecke_vorn'], 2: ['luecke_hinten', 'luecke_vorn', 'welches', 'teilen'], 3: ['vergleich', 'vergleich', 'fehler', 'welches']}[s])
    if art == 'luecke_hinten':
        return zahl(f'Ergänze: {a} : {b} = {a * k} : □', f'{a} · {k} = {a * k}, also auch {b} · {k} = {b * k}.',
                    f'Mit welcher Zahl wird {a} multipliziert, um {a * k} zu erhalten?', b * k, f'{b} * {k}')
    if art == 'luecke_vorn':
        return zahl(f'Ergänze: {a} : {b} = □ : {b * k}', f'{b} · {k} = {b * k}, also auch {a} · {k} = {a * k}.',
                    f'Mit welcher Zahl wird {b} multipliziert, um {b * k} zu erhalten?', a * k, f'{a} * {k}')
    if art == 'teilen':
        return zahl(f'Ergänze: {a * k} : {b * k} = □ : {b}', f'{b * k} : {k} = {b}, also auch {a * k} : {k} = {a}.',
                    'Durch welche Zahl wurde geteilt?', a, f'{a * k} // {k}')
    if art == 'welches':
        d = R.randint(2, 6)
        r = f'{a * k} : {b * k}'
        return auswahl(f'Welches Verhältnis ist gleichwertig zu {a} : {b}?', r,
                       [f'{a + d} : {b + d}', f'{b * k} : {a * k}', f'{a * k} : {b * k + 1}', f'{a * k} : {b + k}'],
                       f'{a} · {k} = {a * k} und {b} · {k} = {b * k}: beide Zahlen mit {k} multipliziert.',
                       'Prüfe, ob beide Zahlen mit derselben Zahl multipliziert wurden.')
    if art == 'fehler':
        d = R.randint(3, 9)
        r = f'Falsch: Man muss multiplizieren, richtig ist {a} : {b} = {a * k} : {b * k}.'
        return auswahl(f'Ina sagt: „{a} : {b} = {a + d} : {b + d}, weil ich zu beiden Zahlen {d} addiert habe.“ Stimmt das?', r,
                       ['Richtig, man darf zu beiden Zahlen dasselbe addieren.', f'Falsch: Man muss {d} abziehen.', f'Richtig, weil der Unterschied {abs(b - a)} gleich bleibt.'],
                       f'{a} : {b} und {a + d} : {b + d} sind nicht gleichwertig (Probe: {a} · {b + d} = {a * (b + d)}, aber {b} · {a + d} = {b * (a + d)}). Gleichwertig wird es nur durch Multiplizieren.',
                       'Prüfe mit Kürzen: Lässt sich das neue Verhältnis auf das alte kürzen?')
    # vergleich: welche Mischung ist stärker (Saft-Anteil)
    while True:
        s1, w1, s2, w2 = R.randint(1, 5), R.randint(2, 8), R.randint(1, 5), R.randint(2, 8)
        if s1 * w2 != s2 * w1 and s1 != s2 and w1 != w2: break
    staerker = 'A' if s1 * (s2 + w2) > s2 * (s1 + w1) else 'B'
    return auswahl(f'Mischung A: Sirup und Wasser im Verhältnis {s1} : {w1}. Mischung B: {s2} : {w2}. Welche schmeckt stärker nach Sirup?',
                   f'Mischung {staerker}', ['Mischung A', 'Mischung B', 'Beide gleich stark'],
                   f'Gleichnamig machen: A = {s1 * w2} : {w1 * w2}, B = {s2 * w1} : {w1 * w2}. Bei gleicher Wassermenge hat {staerker} mehr Sirup.',
                   'Bringe beide Verhältnisse auf dieselbe Wassermenge.')


def g_aufteilen(s):
    a, b = R.randint(1, 7), R.randint(1, 7)
    if a == b or gcd(a, b) != 1: return None
    n = a + b
    t = R.randint(3, 40) * (5 if s > 1 else 1)
    G = n * t
    k = R.choice([('€', 'Zwei Geschwister teilen sich', 'einen Gewinn von'), ('Bonbons', 'Zwei Kinder teilen', ''),
                  ('g', 'Ein Teig wird im Verhältnis Mehl : Zucker gemischt. Insgesamt sind es', ''),
                  ('m', 'Ein Seil wird im Verhältnis', '')])
    if s == 1:
        return luecken(f'Teile {dz(G)} im Verhältnis {a} : {b} auf.', '□ und □', 'beide Anteile', [a * t, b * t],
                       f'{a} + {b} = {n} Teile. Ein Teil: {dz(G)} : {n} = {t}. Anteile: {a} · {t} = {a * t} und {b} · {t} = {b * t}.',
                       'Zähle die Teile zusammen und berechne zuerst, wie viel ein Teil ist.', c=[f'{G} // {n} * {a}', f'{G} // {n} * {b}'])
    art = R.choice({2: ['geld', 'teig', 'seil'], 3: ['differenz', 'teilbekannt', 'drei']}[s])
    if art == 'geld':
        return luecken(f'Zwei Geschwister teilen sich {dz(G)} € Gewinn im Verhältnis {a} : {b}. Wie viel bekommt jedes?', '□ € und □ €', 'Beträge in €',
                       [a * t, b * t], f'{n} Teile, ein Teil = {dz(G)} € : {n} = {t} €. {a} · {t} € = {a * t} €, {b} · {t} € = {b * t} €.',
                       'Erst die Anzahl der Teile, dann den Wert eines Teils.', c=[f'{G} // {n} * {a}', f'{G} // {n} * {b}'])
    if art == 'teig':
        if a <= b: return None
        return zahl(f'Für einen Teig werden Mehl und Zucker im Verhältnis {a} : {b} gemischt, zusammen {dz(G)} g. Wie viel Gramm Zucker sind es?',
                    f'{n} Teile; ein Teil = {dz(G)} g : {n} = {t} g. Zucker: {b} · {t} g = {dz(b * t)} g.',
                    'Zucker ist der zweite Teil des Verhältnisses.', b * t, f'{G} // {n} * {b}', einheit='g')
    if art == 'seil':
        L = n * R.randint(1, 30) / 10 * 5
        if not endlich(Fr(L).limit_denominator(1000)): return None
        L = round(L, 1)
        tt = Fr(str(L)) / n
        if not endlich(tt * a): return None
        return zahl(f'Ein {dz(L)} m langes Seil wird im Verhältnis {a} : {b} zerschnitten. Wie lang ist das kürzere Stück?',
                    f'{n} Teile; ein Teil = {dz(L)} m : {n} = {dz(tt)} m. Kürzeres Stück: {min(a, b)} · {dz(tt)} m = {dz(tt * min(a, b))} m.',
                    'Das kürzere Stück gehört zur kleineren Zahl im Verhältnis.', tt * min(a, b), f'{L} / {n} * {min(a, b)}', einheit='m')
    if art == 'differenz':
        d = abs(a - b) * t
        return zahl(f'Zwei Freunde teilen Sammelkarten im Verhältnis {max(a, b)} : {min(a, b)}. Der eine hat {d} Karten mehr als der andere. Wie viele Karten sind es insgesamt?',
                    f'Der Unterschied sind {max(a, b)} − {min(a, b)} = {abs(a - b)} Teile = {d} Karten. Ein Teil = {t} Karten. Insgesamt {n} · {t} = {G}.',
                    'Der Unterschied entspricht der Differenz der Teile.', G, f'{d} // {abs(a - b)} * {n}')
    if art == 'teilbekannt':
        return zahl(f'Wasser und Saft werden im Verhältnis {a} : {b} gemischt. Es werden {a * t} ml Wasser verwendet. Wie viel ml Getränk entstehen insgesamt?',
                    f'{a} Teile = {a * t} ml, also ein Teil = {t} ml. Insgesamt {n} · {t} ml = {dz(G)} ml.',
                    'Wie viel ist ein Teil, wenn du das Wasser kennst?', G, f'{a * t} // {a} * {n}', einheit='ml')
    c = R.randint(1, 5)
    n3 = a + b + c
    G3 = n3 * t
    return luecken(f'{dz(G3)} € werden im Verhältnis {a} : {b} : {c} auf drei Personen verteilt. Wie viel bekommt jede?', '□ €, □ € und □ €', 'Beträge in €',
                   [a * t, b * t, c * t], f'{n3} Teile, ein Teil = {t} €: {a * t} €, {b * t} €, {c * t} €.',
                   'Zähle alle drei Teile zusammen.', c=[f'{G3} // {n3} * {a}', f'{G3} // {n3} * {b}', f'{G3} // {n3} * {c}'])


def g_proportion(s):
    art = R.choice({1: ['rein', 'rezept'], 2: ['rezept', 'karte', 'benzin'], 3: ['karte_rueck', 'umgekehrt_falle', 'rezept_krumm']}[s])
    if art == 'rein':
        a, b = R.randint(2, 9), R.randint(2, 12)
        k = R.randint(2, 8)
        return zahl(f'Löse die Proportion: {a} : {b} = {a * k} : x', f'{a} · {k} = {a * k}, also x = {b} · {k} = {b * k}.',
                    'Suche den Faktor zwischen den bekannten Zahlen.', b * k, f'{b} * {k}')
    if art in ('rezept', 'rezept_krumm'):
        p1 = R.choice([2, 4, 5, 6, 8])
        p2 = R.choice([x for x in (3, 6, 9, 10, 12, 15) if x != p1])
        z = R.choice([('Mehl', 'g'), ('Milch', 'ml'), ('Butter', 'g'), ('Zucker', 'g')])
        m1 = p1 * R.choice([25, 30, 40, 50, 60, 75])
        m2 = Fr(m1, p1) * p2
        if not endlich(m2): return None
        return zahl(f'Für {p1} Portionen braucht man {dz(m1)} {z[1]} {z[0]}. Wie viel {z[0]} braucht man für {p2} Portionen?',
                    f'Eine Portion: {dz(m1)} {z[1]} : {p1} = {dz(Fr(m1, p1))} {z[1]}. {p2} Portionen: {p2} · {dz(Fr(m1, p1))} {z[1]} = {dz(m2)} {z[1]}.',
                    'Rechne zuerst für eine Portion.', m2, f'{m1} / {p1} * {p2}', einheit=z[1])
    if art == 'karte':
        M = R.choice([10000, 25000, 50000])
        cm = R.randint(2, 18)
        km = Fr(cm * M, 100000)
        return zahl(f'Eine Wanderkarte hat den Maßstab 1 : {dz(M)}. Zwei Orte sind auf der Karte {cm} cm voneinander entfernt. Wie weit ist das in Wirklichkeit (in km)?',
                    f'1 cm auf der Karte = {dz(M)} cm in echt. {cm} cm = {cm} · {dz(M)} cm = {dz(cm * M)} cm = {dz(km)} km.',
                    '1 km = 100 000 cm.', km, f'{cm} * {M} / 100000', einheit='km')
    if art == 'karte_rueck':
        M = R.choice([20000, 25000, 50000])
        km = R.choice([1, 2, 3, 4, 5, 6, 7.5, 2.5, 1.5])
        cm = Fr(str(km)) * 100000 / M
        if not endlich(cm): return None
        return zahl(f'Maßstab 1 : {dz(M)}. Eine Strecke ist in Wirklichkeit {dz(km)} km lang. Wie lang ist sie auf der Karte (in cm)?',
                    f'{dz(km)} km = {dz(Fr(str(km)) * 100000)} cm. Auf der Karte: {dz(Fr(str(km)) * 100000)} : {dz(M)} = {dz(cm)} cm.',
                    'Rechne km in cm um und teile durch die Maßstabszahl.', cm, f'{km} * 100000 / {M}', einheit='cm')
    if art == 'benzin':
        km1 = R.choice([100, 150, 200, 250])
        l1 = R.choice([6, 7, 8, 9]) * km1 // 100
        km2 = R.choice([300, 350, 400, 450, 500, 600])
        l2 = Fr(l1 * km2, km1)
        if not endlich(l2): return None
        return zahl(f'Ein Auto braucht auf {km1} km {l1} Liter Benzin. Wie viele Liter braucht es auf {km2} km?',
                    f'Pro km: {l1} l : {km1}. Für {km2} km: {l1} · {km2} : {km1} = {dz(l2)} l.',
                    'Rechne über 100 km oder über 1 km.', l2, f'{l1} * {km2} / {km1}', einheit='l')
    # umgekehrt_falle: keine Proportion
    m = R.randint(2, 4)
    t = R.choice([40, 50, 60, 90])
    return auswahl(f'{m} Hemden hängen nebeneinander auf der Leine und sind nach {t} Minuten trocken. Wie lange brauchen {3 * m} Hemden, die ebenfalls gleichzeitig hängen?',
                   f'{t} Minuten', [f'{3 * t} Minuten', f'{t // 3} Minuten', f'{t + 2 * m} Minuten'],
                   f'Die Hemden trocknen gleichzeitig. Die Zeit hängt nicht von der Anzahl ab – das ist keine Proportion. Es bleiben {t} Minuten.',
                   'Prüfe zuerst: Wächst die Zeit wirklich mit der Anzahl?')


def g_einheitsrate(s):
    art = R.choice({1: ['stueck', 'tempo'], 2: ['pro100', 'tempo', 'vergleich'], 3: ['vergleich3', 'rueck', 'vergleich']}[s])
    if art == 'stueck':
        n = R.choice([3, 4, 5, 6, 8, 10, 12])
        p = R.randint(10, 60) * 5
        ges = Fr(p * n, 100)
        return zahl(f'{n} Hefte kosten zusammen {eu(ges)}. Wie viel kostet ein Heft?', f'{eu(ges)} : {n} = {eu(Fr(p, 100))}.',
                    'Teile den Gesamtpreis durch die Anzahl.', Fr(p, 100), f'{ges} / {n}', einheit='€')
    if art == 'tempo':
        h = R.choice([2, 3, 4, 5, Fr(1, 2), Fr(3, 2), Fr(5, 2)])
        v = R.choice([12, 15, 18, 20, 24, 60, 80, 90, 100])
        km = v * h
        if km.denominator != 1 if isinstance(km, Fr) else False: return None
        return zahl(f'Ein {"Radfahrer" if v < 30 else "Zug"} legt in {dz(h) if isinstance(h, int) else dz(float(h))} Stunden {dz(km)} km zurück. Wie viele km sind das pro Stunde?',
                    f'{dz(km)} km : {dz(float(h)) if not isinstance(h, int) else h} h = {v} km pro Stunde.',
                    'Rate = Weg : Zeit.', v, f'{km} / {float(h) if not isinstance(h, int) else h}', einheit='km/h')
    if art == 'pro100':
        g = R.choice([250, 400, 500, 750, 125, 200])
        p100 = Fr(R.randint(20, 80) * 5, 100)          # 1,00 € bis 4,00 € pro 100 g
        pr = p100 * g / 100
        if (pr * 100).denominator != 1: return None
        ware = R.choice(['Käse', 'Nüsse', 'Kaffee', 'Schokolade', 'Müsli'])
        return zahl(f'Eine Packung {ware} mit {g} g kostet {eu(pr)}. Wie viel kostet das pro 100 g?',
                    f'{g} g sind {dz(Fr(g, 100))}-mal 100 g. {eu(pr)} : {dz(Fr(g, 100))} = {eu(p100)}.',
                    'Wie oft passen 100 g in die Packung?', p100, f'{float(pr)} / ({g} / 100)', einheit='€')
    if art in ('vergleich', 'vergleich3'):
        for _ in range(100):
            ang = []
            for _ in range(2 if art == 'vergleich' else 3):
                g = R.choice([200, 250, 400, 500, 750, 1000])
                p = round(g * R.randint(80, 200) / 100 / 5) * 5      # 0,80 € bis 2,00 € pro 100 g, in 5-ct-Schritten
                ang.append((g, p))
            raten = [Fr(p, g) for g, p in ang]
            if len(set(raten)) == len(raten) and all(endlich(r * 100 / 100) for r in raten) and len({g for g, _ in ang}) == len(ang):
                best = min(range(len(ang)), key=lambda i: raten[i])
                guenstigster_preis = min(range(len(ang)), key=lambda i: ang[i][1])
                if best != guenstigster_preis: break
        else:
            return None
        namen = 'ABC'
        txt = ', '.join(f'{namen[i]}: {dz(g)} g für {eu(Fr(p, 100))}' for i, (g, p) in enumerate(ang))
        w = '; '.join(f'{namen[i]}: {eu(Fr(p, 100))} : {dz(Fr(g, 100))} ≈ {dz(round(p / g, 3))} € pro 100 g' for i, (g, p) in enumerate(ang))
        opts = [f'Angebot {namen[i]}' for i in range(len(ang))]
        if len(opts) < 3: opts.append('Beide gleich günstig')
        return auswahl(f'Kaffee wird angeboten – {txt}. Welches Angebot ist am günstigsten?', f'Angebot {namen[best]}', opts,
                       w + f'. Am wenigsten pro 100 g kostet {namen[best]}.', 'Berechne für jedes Angebot den Preis pro 100 g.')
    # rueck: aus Rate Gesamtwert
    rate = R.choice([Fr(3, 2), Fr(5, 4), Fr(12, 5), Fr(9, 10), Fr(7, 4)])
    menge_ = R.choice([4, 6, 8, 10, 12, 20])
    return zahl(f'Äpfel kosten {eu(rate)} pro kg. Wie viel kosten {menge_} kg?', f'{menge_} · {eu(rate)} = {eu(rate * menge_)}.',
                'Einheitsrate mal Menge.', rate * menge_, f'{float(rate)} * {menge_}', einheit='€')


def g_aenderung(s):
    art = R.choice({1: ['temp', 'wasser'], 2: ['temp', 'wasser', 'graph', 'abnahme'], 3: ['abnahme', 'graph', 'vergleich', 'rueck']}[s])
    if art == 'temp':
        t1 = R.randint(6, 10)
        dt = R.randint(2, 5)
        r = R.randint(1, 4) * (1 if s == 1 else R.choice([1, -1]))
        T1 = R.randint(4, 15) if r > 0 else R.randint(18, 28)
        T2 = T1 + r * dt
        return zahl(f'Um {t1} Uhr misst man {T1} °C, um {t1 + dt} Uhr {T2} °C. Berechne die Änderungsrate in °C pro Stunde.',
                    f'Änderung: {T2} − {T1} = {dz(T2 - T1)} °C in {dt} Stunden. Rate: {dz(T2 - T1)} : {dt} = {dz(r)} °C pro Stunde.',
                    'Teile die Temperaturänderung durch die Zeitspanne. Fällt die Temperatur, ist die Rate negativ.', r, f'({T2} - {T1}) / {dt}', einheit='°C/h')
    if art == 'wasser':
        m = R.randint(2, 10)
        r = R.choice([5, 8, 10, 12, 15, 20, 25])
        a0 = R.choice([0, 20, 50, 100])
        return zahl(f'Ein Becken enthält {a0} Liter Wasser. Nach {m} Minuten sind es {a0 + r * m} Liter. Wie viele Liter fließen pro Minute zu?',
                    f'({a0 + r * m} − {a0}) l : {m} min = {r} l pro Minute.', 'Zunahme durch Zeit.', r, f'({a0 + r * m} - {a0}) / {m}', einheit='l/min')
    if art == 'abnahme':
        d = R.randint(2, 8)
        r = R.choice([Fr(1, 2), 1, Fr(3, 2), 2, Fr(5, 2), 3])
        h0 = R.randint(20, 40)
        h1 = h0 - r * d
        return zahl(f'Eine Kerze ist {h0} cm hoch. Nach {d} Stunden ist sie noch {dz(h1)} cm hoch. Berechne die Änderungsrate der Höhe in cm pro Stunde.',
                    f'Änderung: {dz(h1)} − {h0} = {dz(h1 - h0)} cm in {d} h. Rate: {dz(h1 - h0)} : {d} = {dz(-r)} cm pro Stunde (negativ, weil die Kerze kürzer wird).',
                    'Rechne „Endwert minus Anfangswert“. Wird die Größe kleiner, ist die Rate negativ.', -r, f'({float(h1)} - {h0}) / {d}', einheit='cm/h')
    if art == 'graph':
        x1, x2 = R.randint(0, 3), R.randint(5, 8)
        m = R.choice([2, 3, 4, 5, -2, -3]) if s == 3 else R.choice([2, 3, 4, 5])
        t = R.randint(2, 10) if m > 0 else R.randint(25, 35)
        y1, y2 = m * x1 + t, m * x2 + t
        bild = {'typ': 'koordinaten', 'x': [0, 9], 'y': [0, max(y1, y2) + 4],
                'graphen': [{'art': 'linear', 'm': m, 't': t, 'bereich': [0, 9]}],
                'punkte': [{'x': x1, 'y': y1, 'name': f'({x1} | {y1})'}, {'x': x2, 'y': y2, 'name': f'({x2} | {y2})'}],
                'name_x': 'Tage', 'name_y': 'cm', 'schritt_y': 5 if max(y1, y2) > 25 else 2}
        was = 'Die Höhe einer Pflanze' if m > 0 else 'Der Wasserstand in einer Tonne'
        return mit_grafik(zahl(f'{was} wird täglich gemessen (siehe Graph). Berechne die Änderungsrate in cm pro Tag zwischen Tag {x1} und Tag {x2}.',
                               f'({y2} − {y1}) : ({x2} − {x1}) = {y2 - y1} : {x2 - x1} = {m} cm pro Tag.',
                               'Lies beide Punkte ab: Höhenänderung durch Anzahl der Tage.', m, f'({y2} - {y1}) / ({x2} - {x1})', einheit='cm/Tag'), bild)
    if art == 'vergleich':
        a_d, a_m = R.randint(2, 6), R.randint(2, 6)
        ra, rb = R.randint(2, 9), R.randint(2, 9)
        if ra == rb: return None
        sa, sb = a_d * ra, a_m * rb
        return auswahl(f'Robotermäher A mäht {sa} m² in {a_d} Minuten, Mäher B {sb} m² in {a_m} Minuten. Welcher mäht schneller?',
                       'Mäher A' if ra > rb else 'Mäher B', ['Mäher A', 'Mäher B', 'Beide gleich schnell'],
                       f'A: {sa} : {a_d} = {ra} m² pro Minute. B: {sb} : {a_m} = {rb} m² pro Minute.',
                       'Vergleiche die Raten pro Minute, nicht die Gesamtflächen.')
    # rueck
    r = R.choice([3, 4, 5, 6, 8])
    t = R.randint(3, 9)
    a0 = R.randint(10, 60)
    return zahl(f'Ein Tank wird mit {r} Litern pro Minute gefüllt. Am Anfang sind {a0} Liter darin. Wie viele Liter sind es nach {t} Minuten?',
                f'Zunahme: {r} · {t} = {r * t} l. Inhalt: {a0} + {r * t} = {a0 + r * t} l.',
                'Rate mal Zeit ergibt die Zunahme.', a0 + r * t, f'{a0} + {r} * {t}', einheit='l')


GEN = {'kuerzen': g_kuerzen, 'gleichwertig': g_gleichwertig, 'aufteilen': g_aufteilen, 'proportion': g_proportion,
       'einheitsrate': g_einheitsrate, 'aenderung': g_aenderung}

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import ko, pkte, tab  # noqa: E402


def _bs(teile, gefaerbt, ganzes=None, teil_text=None, **kw):
    b = {'typ': 'bruchstreifen', 'teile': teile, 'gefaerbt': gefaerbt}
    if ganzes:
        b['ganzes'] = ganzes
    if teil_text:
        b['teil_text'] = teil_text
    b.update(kw)
    return b


def _rez(*m):
    return tab(['Portionen', '4', '1', '6'], ['Mehl in g', *m])


_T = ko([8, 14], [0, 24], pkte({'9 Uhr': (9, 12), '13 Uhr': (13, 20)}), schritt=0, schritt_x=1, schritt_y=4, name_x='Uhrzeit', name_y='°C')
UMBAU = {
    'kuerzen': {
        'einstieg': 'In der Klasse sind 12 Mädchen und 18 Jungen. Auf 2 Mädchen kommen also 3 Jungen. '
                    'So einen Vergleich nennt man ⟦Verhältnis⟧, geschrieben 2 : 3.',
        'woerter': [['Verhältnis', 'Vergleich zweier Größen, geschrieben a : b'],
                    ['kürzen', 'beide Zahlen durch dieselbe Zahl teilen']],
        'bild': _bs(30, 12, '30 Kinder', '12 Mädchen'),
        'schritte': [
            {'text': 'Mädchen : Jungen = 12 : 18.'},
            {'text': 'Zum Kürzen: Beide Zahlen sind durch 6 teilbar.'},
            {'text': '12 : 6 = 2 und 18 : 6 = 3. Gekürzt: ⟦2 : 3⟧.', 'bild': {'zeilen': [{'teile': 5, 'gefaerbt': 2}]}},
        ],
        'fehler': '1 m : 25 cm ist nicht 1 : 25. Erst ⟦gleiche Einheiten⟧: 100 cm : 25 cm = 4 : 1.',
        'regel': 'Verhältnis kürzen: ⟦beide Zahlen durch dieselbe Zahl⟧ teilen. Vorher gleiche Einheiten herstellen.',
    },
    'gleichwertig': {
        'einstieg': 'Für Saft mischst du 3 Becher Sirup mit 5 Bechern Wasser. Für eine große Kanne nimmst du von beidem viermal so viel. '
                    'Der Saft schmeckt gleich: Die Verhältnisse sind ⟦gleichwertig⟧.',
        'woerter': [['gleichwertig', 'beide Zahlen mit derselben Zahl malgenommen; das Verhältnis bleibt gleich']],
        'bild': _bs(8, 3, '8 Becher', '3 Sirup'),
        'schritte': [
            {'text': 'Gesucht: 3 : 5 = □ : 20.'},
            {'text': 'Von 5 nach 20 nimmt man mal 4.'},
            {'text': 'Also auch 3 · 4 = 12: ⟦3 : 5 = 12 : 20⟧.', 'bild': {'zeilen': [{'teile': 32, 'gefaerbt': 12}]}},
        ],
        'fehler': '18 : 20 ist falsch: Zu beiden 15 addieren verändert den Geschmack. Bei Verhältnissen wird ⟦multipliziert⟧.',
        'fehler_bild': {'zeilen': [{'teile': 38, 'gefaerbt': 18}]},
        'regel': 'Gleichwertig: beide Zahlen ⟦mit derselben Zahl malnehmen⟧ oder teilen. Addieren verändert das Verhältnis.',
    },
    'aufteilen': {
        'einstieg': 'Zwei Geschwister gewinnen 120 €. Eines hat 3 € Einsatz gezahlt, das andere 5 €. '
                    'Sie verteilen im Verhältnis 3 : 5. Dafür zählt man die ⟦Teile⟧.',
        'woerter': [['Teile', 'gleich große Stücke; bei 3 : 5 sind es zusammen 8']],
        'bild': _bs(8, 3, '120 €'),
        'schritte': [
            {'text': '3 + 5 = 8 Teile.'},
            {'text': 'Ein Teil: 120 € : 8 = 15 €.', 'bild': {'teil_text': '1 Teil = 15 €'}},
            {'text': '3 Teile: 3 · 15 € = ⟦45 €⟧.', 'bild': {'teil_text': '45 €'}},
            {'text': '5 Teile: 5 · 15 € = ⟦75 €⟧.', 'bild': {'teil_text': '45 €', 'zeilen': [{'teile': 8, 'gefaerbt': 5}]}},
        ],
        'fehler': '120 € : 3 und 120 € : 5 ist falsch. Zusammen wären das nur 64 €. Teile durch die ⟦Summe der Teile⟧.',
        'regel': 'Teile zusammenzählen, ⟦einen Teil berechnen⟧, dann mit a und mit b malnehmen.',
    },
    'proportion': {
        'einstieg': 'Ein Rezept für 4 Portionen braucht 300 g Mehl. Du willst 6 Portionen backen. '
                    'Die Mengen wachsen im gleichen Verhältnis. So eine Gleichung heißt ⟦Proportion⟧.',
        'woerter': [['Proportion', 'zwei gleiche Verhältnisse: a : b = c : d'],
                    ['Dreisatz', 'erst auf 1 rechnen, dann auf die gesuchte Zahl']],
        'bild': _rez('300', '?', '?'),
        'schritte': [
            {'text': 'Als Proportion: 4 : 300 = 6 : x.'},
            {'text': 'Dreisatz: 1 Portion braucht 300 g : 4 = 75 g.', 'bild': _rez('300', '75', '?')},
            {'text': '6 Portionen: 6 · 75 g = ⟦450 g⟧.', 'bild': _rez('300', '75', '450')},
        ],
        'fehler': '302 g ist falsch, nur 2 g mehr für 2 Portionen mehr. Die Menge wächst ⟦im gleichen Verhältnis⟧.',
        'fehler_bild': _rez('300', '?', '302 ✗'),
        'regel': 'Proportion: über ⟦eins⟧ rechnen oder den Faktor suchen. Beide Größen wachsen im gleichen Verhältnis.',
    },
    'einheitsrate': {
        'einstieg': 'Packung A hat 750 g für 3,00 €, Packung B 500 g für 2,20 €. Was ist günstiger? '
                    'Vergleiche den Preis für dieselbe Menge, die ⟦Einheitsrate⟧.',
        'woerter': [['Einheitsrate', 'der Wert für genau 1 Einheit, z. B. Preis pro 100 g'],
                    ['pro', 'je, für jede: 0,40 € pro 100 g']],
        'bild': {'typ': 'saeulen', 'einheit': '€', 'werte': [{'name': 'A 750 g', 'wert': 3.0}, {'name': 'B 500 g', 'wert': 2.2}], 'zahlen': True},
        'schritte': [
            {'text': 'A kostet mehr, enthält aber auch mehr.'},
            {'text': 'Pro 100 g: A kostet 3,00 € : 7,5 = 0,40 €.'},
            {'text': 'B kostet 2,20 € : 5 = 0,44 € pro 100 g.',
             'bild': {'einheit': '€ pro 100 g', 'werte': [{'name': 'A', 'wert': 0.4}, {'name': 'B', 'wert': 0.44}]}},
            {'text': 'Also ist ⟦Packung A günstiger⟧.'},
        ],
        'fehler': '„B ist billiger, weil 2,20 € < 3,00 €“ ist falsch. B enthält weniger. Vergleiche den ⟦Preis pro gleicher Menge⟧.',
        'regel': 'Angebote vergleichen: ⟦Preis pro Einheit⟧ berechnen, z. B. pro 100 g. Der kleinere Wert ist günstiger.',
    },
    'aenderung': {
        'einstieg': 'Um 9 Uhr zeigt das Thermometer 12 °C, um 13 Uhr schon 20 °C. Wie schnell wird es wärmer? '
                    'Das sagt die ⟦Änderungsrate⟧.',
        'woerter': [['Änderungsrate', 'wie stark sich eine Größe pro Einheit ändert, z. B. °C pro Stunde'],
                    ['Zeitspanne', 'wie viel Zeit vergangen ist']],
        'bild': _T,
        'schritte': [
            {'text': 'Die Temperatur steigt um 20 − 12 = 8 °C.', 'bild': {'strecken': [[13, 12, 13, 20, 'gestrichelt']]}},
            {'text': 'Zeitspanne: 13 − 9 = 4 Stunden.', 'bild': {'strecken': [[9, 12, 13, 12, 'gestrichelt'], [13, 12, 13, 20, 'gestrichelt']]}},
            {'text': 'Rate: 8 : 4 = ⟦2 °C pro Stunde⟧.', 'bild': {'graphen': [{'art': 'linear', 'm': 2, 't': -6, 'bereich': [9, 13]}]}},
        ],
        'fehler': '20 : 13 ≈ 1,5 ist falsch. Teile die ⟦Änderungen⟧, nicht die Endwerte: 8 : 4 = 2.',
        'regel': 'Änderungsrate = ⟦Änderung : Zeitspanne⟧. Nimmt die Größe ab, ist die Rate negativ.',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


d = bauen('groessen.verhaeltnisse',
      'Verhältnisse kürzen und vergleichen, im Verhältnis aufteilen, Proportionen lösen, Einheitsraten und Änderungsraten berechnen.',
      ['Verhältnis (ratio) a : b – kürzen und erweitern wie bei Brüchen, nie addieren.',
       'Aufteilen: Teile zählen, einen Teil berechnen, vervielfachen.',
       'Einheitsrate (unit rate): Wert für genau 1 Einheit – so vergleicht man Angebote.',
       'Änderungsrate (rate of change) = Änderung : Zeitspanne; Abnahme ergibt eine negative Rate.'],
      [('Verhältnisse', ['kuerzen', 'gleichwertig', 'aufteilen']), ('Proportionen', ['proportion']), ('Raten', ['einheitsrate', 'aenderung'])],
      ETAPPEN, GEN,
      offen=['Antworten bei Verhältnissen als Lücken □ : □ (je ein Zahlenfeld). Die App zeigt den Doppelpunkt aus der Schablone.',
             'Proportionen bewusst ohne Kreuzprodukt-Formel, sondern über Faktor und Dreisatz (Niveau MYP 2 ≈ Klasse 7).'])
umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-1) ----------
# Prüfungsvorbilder: IB-MYP-Aufgabenformate „Ratio, rates and proportion“ (Verhältnis aus Brüchen, Anteil aus Verhältnis,
# „best buy“, Wechselkurs, Maßstab bestimmen, Änderungsrate aus Tabelle, rückwärts rechnen). Typ übernommen, Wortlaut und Zahlen eigen.
def durchsicht(d):
    from _rsib1 import Z, A, L, nachtrag, finde
    T = lambda teil: finde(d, teil)
    nachtrag(d,
        umstufen={
            T('Kürze das Verhältnis 4 € : 15 ct.'): 2,
            T('Welches Verhältnis ist gleichwertig zu 8 : 9?'): 2,
            T('Für 4 Portionen braucht man 100 g Zucker. Wie viel Zucker braucht man für 6 Portionen?'): 2,
            T('Äpfel kosten 1,50 € pro kg. Wie viel kosten 6 kg?'): 1,
            T('Äpfel kosten 2,40 € pro kg. Wie viel kosten 12 kg?'): 1,
            T('Ein Tank wird mit 4 Litern pro Minute gefüllt. Am Anfang sind 35 Liter'): 1,
            T('Ein Tank wird mit 8 Litern pro Minute gefüllt. Am Anfang sind 19 Liter'): 1,
            T('Eine Kerze ist 36 cm hoch. Nach 7 Stunden'): 2,
            T('Robotermäher A mäht 20 m² in 4 Minuten'): 1,
        },
        ersetzen={
            T('Ina sagt: „7 : 9 = 14 : 16'):
                Z(3, 'Für welche positive Zahl x gilt 3 : x = x : 12?', 6, '6',
                  'Gleichwertig heißt: Von 3 zu x und von x zu 12 nimmt man mit demselben Faktor mal. 3 · 2 = 6 und 6 · 2 = 12. Also x = 6: 3 : 6 = 6 : 12 = 1 : 2.', 'Probiere x = 4, 5, 6 … und vergleiche die gekürzten Verhältnisse.'),
            T('4 Hemden hängen nebeneinander auf der Leine und sind nach 50 Minuten trocken.'):
                Z(3, '3 Maler brauchen für ein Haus 12 Tage. Wie viele Tage brauchen 4 Maler, wenn alle gleich schnell arbeiten?', 9, '3*12/4',
                  'Mehr Maler, weniger Tage: Das ist nicht proportional. 3 · 12 = 36 Malertage. 36 : 4 = 9 Tage.',
                  'Wächst die Zeit mit der Zahl der Maler – oder sinkt sie?', einheit='Tage'),
            T('Äpfel kosten 2,40 € pro kg. Wie viel kosten 20 kg?'):
                Z(3, 'Angebot A: 3 Stück für 2,40 €. Angebot B: 5 Stück für 3,75 €. Um wie viel Cent ist ein Stück bei B günstiger?', 5, '240/3 - 375/5',
                  'A: 2,40 € : 3 = 0,80 €. B: 3,75 € : 5 = 0,75 €. Unterschied 5 ct.', 'Berechne den Stückpreis bei beiden.', einheit='ct'),
            T('Äpfel kosten 2,40 € pro kg. Wie viel kosten 10 kg?'):
                Z(3, 'Aktion „4 nehmen, 3 bezahlen“: Ein Stück kostet sonst 1,20 €. Wie viel kostet ein Stück bei der Aktion?', 0.9, '3*1.2/4',
                  'Man zahlt 3 · 1,20 € = 3,60 € für 4 Stück. 3,60 € : 4 = 0,90 €.', 'Wie viel zahlt man für 4 Stück?', einheit='€'),
            T('Ein Tank wird mit 4 Litern pro Minute gefüllt. Am Anfang sind 59 Liter'):
                Z(3, 'Ein Tank wird mit 4 Litern pro Minute gefüllt. Nach 6 Minuten sind 83 Liter darin. Wie viel war am Anfang drin?', 59, '83 - 6*4',
                  'In 6 Minuten kommen 24 Liter dazu. 83 − 24 = 59 Liter.', 'Rechne rückwärts.', einheit='l'),
            T('Ein Tank wird mit 6 Litern pro Minute gefüllt. Am Anfang sind 49 Liter'):
                Z(3, 'Ein Tank enthält 35 Liter und wird mit 4 Litern pro Minute gefüllt. Nach wie vielen Minuten sind 75 Liter darin?', 10, '(75 - 35)/4',
                  'Es fehlen 75 − 35 = 40 Liter. 40 : 4 = 10 Minuten.', 'Wie viel muss noch dazukommen?', einheit='min'),
        },
        neu={
            'kuerzen': [
                L(3, 'Schreibe das Verhältnis 3/4 : 1/2 mit möglichst kleinen ganzen Zahlen.', '□ : □', [3, 2], ['3', '2'],
                  'Mal 4: 3/4 · 4 = 3 und 1/2 · 4 = 2. Also 3 : 2.', 'Multipliziere beide Teile mit dem gemeinsamen Nenner.'),
                L(3, 'In einer Klasse ist das Verhältnis Mädchen : Jungen = 3 : 4. Welcher Anteil der Klasse sind Mädchen?', '□/□', [3, 7], ['3', '3 + 4'],
                  '3 + 4 = 7 Teile, davon 3 Mädchen: 3/7.', 'Wie viele Teile sind es insgesamt?', hinweis='Zähler und Nenner eintragen.'),
                Z(3, 'In einer Gruppe ist das Verhältnis Mädchen : Jungen = 2 : 3. Kommen 2 Mädchen dazu, ist es 1 : 1. Wie viele Kinder waren es vorher?', 10, '5*2',
                  'Vorher 2k Mädchen, 3k Jungen. 2k + 2 = 3k ⇒ k = 2: 4 Mädchen, 6 Jungen, zusammen 10.', 'Probiere k = 1, 2, 3 für 2k : 3k.'),
            ],
            'gleichwertig': [
                Z(3, 'Mehl, Zucker und Butter stehen im Verhältnis 5 : 2 : 3. Man nimmt 600 g Butter. Wie viel Gramm Mehl braucht man?', 1000, '600/3*5',
                  '3 Teile = 600 g ⇒ 1 Teil = 200 g. Mehl: 5 · 200 g = 1 000 g.', 'Wie viel ist ein Teil?', einheit='g'),
                A(3, 'Welche beiden Verhältnisse sind gleichwertig?', '4 : 6 und 10 : 15', ['4 : 6 und 6 : 8', '6 : 8 und 10 : 15', '4 : 6 und 9 : 12'],
                  'Gekürzt: 4 : 6 = 2 : 3, 10 : 15 = 2 : 3, 6 : 8 = 3 : 4, 9 : 12 = 3 : 4. Gleich sind 4 : 6 und 10 : 15 (und 6 : 8 und 9 : 12).',
                  'Kürze jedes Verhältnis vollständig.'),
                Z(3, 'Mädchen und Jungen stehen im Verhältnis 3 : 4. Es sind 12 Mädchen. Wie viele Kinder sind es insgesamt?', 28, '12/3*7',
                  '3 Teile = 12 ⇒ 1 Teil = 4. Insgesamt 7 Teile = 28 Kinder.', 'Bestimme zuerst einen Teil.'),
            ],
            'aufteilen': [
                Z(3, 'Ein Erbe wird im Verhältnis 2 : 3 : 5 verteilt. Der kleinste Anteil beträgt 4 000 €. Wie groß ist das Erbe insgesamt?', 20000, '4000/2*10',
                  '2 Teile = 4 000 € ⇒ 1 Teil = 2 000 €. 2 + 3 + 5 = 10 Teile = 20 000 €.', 'Welcher Anteil ist der kleinste?', einheit='€'),
                Z(3, 'Ein Rechteck hat 64 cm Umfang. Länge und Breite stehen im Verhältnis 5 : 3. Wie lang ist das Rechteck?', 20, '64/2/8*5',
                  'Länge + Breite = 32 cm. 5 + 3 = 8 Teile ⇒ 1 Teil = 4 cm. Länge 5 · 4 = 20 cm.', 'Der Umfang enthält Länge und Breite je zweimal.', einheit='cm'),
            ],
            'proportion': [
                Z(3, 'Der Wechselkurs ist 1 € = 1,10 $. Wie viele Euro bekommt man für 220 $?', 200, '220/1.1',
                  '1,10 $ entsprechen 1 €. 220 : 1,10 = 200 €.', 'Wie viele „1,10-$-Päckchen“ stecken in 220 $?', einheit='€'),
                Z(3, 'Auf einer Karte entsprechen 6 cm in Wirklichkeit 3 km. Der Maßstab ist 1 : x. Wie groß ist x?', 50000, '300000/6',
                  '3 km = 300 000 cm. 6 cm : 300 000 cm = 1 : 50 000.', 'Rechne beide Längen in dieselbe Einheit um.'),
                Z(3, 'Ein Handyfoto ist 6 cm breit und 10 cm hoch. Als Poster soll es 45 cm breit werden. Wie hoch wird das Poster?', 75, '45/6*10',
                  'Faktor 45 : 6 = 7,5. Höhe 10 · 7,5 = 75 cm.', 'Um welchen Faktor wird das Bild vergrößert?', einheit='cm'),
            ],
            'einheitsrate': [
                Z(3, 'Saft: 1,5 l kosten 1,95 €, 0,75 l kosten 1,05 €. Wie viele Euro spart man pro Liter mit der großen Flasche?', 0.1, '1.05/0.75 - 1.95/1.5',
                  'Groß: 1,95 € : 1,5 = 1,30 € pro l. Klein: 1,05 € : 0,75 = 1,40 € pro l. Ersparnis 0,10 €.', 'Berechne den Literpreis beider Flaschen.', einheit='€'),
                Z(3, 'Ein Auto verbraucht 6 Liter auf 100 km. Wie weit kommt es mit 45 Litern?', 750, '45/6*100',
                  '1 Liter reicht für 100 : 6 km. 45 Liter: 45 : 6 · 100 = 750 km.', 'Wie viele „6-Liter-Portionen“ stecken in 45 Litern?', einheit='km'),
                Z(3, 'Ein Drucker druckt 18 Seiten in 45 Sekunden. Wie viele Seiten schafft er pro Minute?', 24, '18/45*60',
                  'Pro Sekunde 18 : 45 = 0,4 Seiten. Pro Minute 0,4 · 60 = 24 Seiten.', 'Achte auf die Einheit: Minute statt Sekunde.'),
                A(3, 'Läuferin A schafft 400 m in 80 s, Läuferin B 1 km in 210 s. Wer ist schneller?', 'A', ['B', 'beide gleich schnell'],
                  'A: 400 : 80 = 5 m/s. B: 1 000 : 210 ≈ 4,76 m/s. A ist schneller.', 'Berechne für beide die Meter pro Sekunde.'),
            ],
            'aenderung': [
                Z(3, 'Von 8 Uhr bis 12 Uhr steigt die Temperatur um 2,5 °C pro Stunde. Um 12 Uhr sind es 17 °C. Wie warm war es um 8 Uhr?', 7, '17 - 4*2.5',
                  '4 Stunden · 2,5 °C = 10 °C Anstieg. 17 − 10 = 7 °C.', 'Rechne rückwärts.', einheit='°C'),
                Z(3, 'Kerze A ist 30 cm hoch und brennt 2 cm pro Stunde ab. Kerze B ist 24 cm hoch und brennt 1 cm pro Stunde ab. Nach wie vielen Stunden sind beide gleich hoch?', 6, '(30 - 24)/(2 - 1)',
                  'A holt pro Stunde 1 cm auf B auf. Der Unterschied ist 6 cm: nach 6 Stunden, beide 18 cm hoch.', 'Um wie viel ändert sich der Unterschied pro Stunde?', einheit='h'),
                Z(3, 'Ein Pool enthält 450 Liter und verliert 3 Liter pro Minute. Nach wie vielen Minuten ist er leer?', 150, '450/3',
                  '450 : 3 = 150 Minuten (2,5 Stunden).', 'Wie oft passen 3 Liter in 450 Liter?', einheit='min'),
                A(3, 'Die Änderungsrate der Höhe einer Kerze ist −1,5 cm pro Stunde. Was bedeutet das?', 'Sie wird jede Stunde 1,5 cm kürzer.',
                  ['Sie ist 1,5 cm hoch.', 'Sie wächst jede Stunde 1,5 cm.', 'Sie brennt 1,5 Stunden lang.'],
                  'Das Minus zeigt eine Abnahme: pro Stunde 1,5 cm weniger.', 'Was sagt das Vorzeichen?'),
                Z(3, 'Ein Becken: nach 0 Minuten 20 l, nach 5 Minuten 45 l, nach 10 Minuten 70 l. Wie groß ist die Änderungsrate in Litern pro Minute?', 5, '(70 - 20)/10',
                  'In 10 Minuten kommen 50 l dazu: 50 : 10 = 5 l pro Minute (jeder 5-Minuten-Schritt bringt 25 l).', 'Nimm Anfangs- und Endwert.', einheit='l/min'),
                Z(3, 'Ein Flugzeug sinkt in 20 Minuten von 9 000 m auf 3 000 m Höhe. Berechne die Änderungsrate in m pro Minute.', -300, '(3000 - 9000)/20',
                  'Änderung 3 000 − 9 000 = −6 000 m. −6 000 : 20 = −300 m pro Minute.', 'Die Höhe nimmt ab – welches Vorzeichen hat die Rate?', einheit='m/min'),
            ],
        })


durchsicht(d)


# ---- STUFEN (Zwanzigste Runde, Zusatz RS/IB, Zweig stufen-rsib-1) ----
from _stufen_rsib1 import Stufen, stufen  # noqa: E402

ST = Stufen('groessen.verhaeltnisse', 20_21_12)
Z, A, L = ST.Z, ST.A, ST.L

# kuerzen
ST.stufenleiter('kuerzen', 'Ein Verhältnis aus einer Sachsituation aufstellen und vollständig kürzen; das gekürzte Verhältnis erkennen.',
                'Große Zahlen und verschiedene Einheiten kürzen, Verhältnis in einen Anteil umwandeln, ungekürzte Zahl rückwärts.',
                'Drei Größen, Dezimalzahlen und Brüche im Verhältnis, Änderung eines Verhältnisses rückwärts, Fehler „nicht vollständig gekürzt“, Unkürzbarkeit begründen, Prüfungsaufgabe.')
ST.typ('kuerzen', '/Gib das Verhältnis .* gekürzt an\\.$/', 'direkt')
ST.typ('kuerzen', 'Kürze das Verhältnis 1,5', 'verknuepfen')
ST.typ('kuerzen', 'Kürze das Verhältnis', 'mehrschritt')
ST.typ('kuerzen', 'Ein Saft wird aus', 'transfer')
ST.typ('kuerzen', 'Schreibe das Verhältnis', 'verknuepfen')
ST.typ('kuerzen', 'In einer Klasse ist das Verhältnis', 'darstellung')
ST.typ('kuerzen', 'In einer Gruppe ist das Verhältnis', 'rueckwaerts')
ST.neu('kuerzen', 'erkennen', A('Welches Verhältnis ist 12 : 18 vollständig gekürzt?', '2 : 3', ['4 : 6', '6 : 9', '3 : 2'],
       '12 und 18 sind beide durch 6 teilbar: 12 : 6 = 2, 18 : 6 = 3. 4 : 6 und 6 : 9 lassen sich noch weiter kürzen.', 'Suche den größten gemeinsamen Teiler.'))
ST.neu('kuerzen', 'umkehr', Z('Ein Verhältnis wurde durch 5 gekürzt und lautet jetzt 3 : 8. Wie hieß die erste Zahl vorher?', 15, '3 * 5',
       'Kürzen durch 5 heißt: beide Zahlen wurden durch 5 geteilt. Rückwärts: 3 · 5 = 15 (und 8 · 5 = 40).', 'Mache das Kürzen rückgängig.'))
ST.neu('kuerzen', 'fehler', A('Jemand kürzt 24 : 36 zu 4 : 6 und sagt: „Weiter geht es nicht.“ Was stimmt?', 'Falsch: 4 : 6 lässt sich noch durch 2 kürzen: 2 : 3.',
       ['Richtig.', 'Falsch: Richtig ist 3 : 4.', 'Falsch: Richtig ist 6 : 9.'], '4 und 6 sind beide gerade. Mit dem größten gemeinsamen Teiler 12 kürzt man direkt: 24 : 36 = 2 : 3.', 'Haben 4 und 6 noch einen gemeinsamen Teiler?'))
ST.neu('kuerzen', 'begruenden', A('Stimmt: Das Verhältnis 7 : 9 lässt sich nicht weiter kürzen?', 'Ja, 7 und 9 haben außer 1 keinen gemeinsamen Teiler.', ['Nein, durch 3.', 'Nein, durch 7.', 'Nur, wenn man Dezimalzahlen erlaubt.'],
       'Teiler von 7: 1, 7. Teiler von 9: 1, 3, 9. Gemeinsam ist nur die 1, also ist 7 : 9 schon vollständig gekürzt.', 'Schreibe die Teiler beider Zahlen auf.'))
ST.neu('kuerzen', 'pruefung', L('In einer Schule sind 240 Mädchen und 288 Jungen. a) Gib das Verhältnis Mädchen : Jungen gekürzt an. b) Welcher Anteil aller Kinder sind Mädchen? Gib ihn als gekürzten Bruch an.',
       'a) □ : □; b) □/□', [5, 6, 5, 11], ['240 // 48', '288 // 48', '5', '5 + 6'], 'a) Größter gemeinsamer Teiler 48: 5 : 6. b) 5 von 5 + 6 = 11 Teilen: 5/11.', 'Bei b) zählen alle Teile zusammen.'))
ST.knobel('kuerzen', L('Zwei Zahlen stehen im Verhältnis 3 : 5. Addiert man zu jeder 4, stehen sie im Verhältnis 2 : 3. Wie heißen die Zahlen?', '□ und □', [12, 20], ['3 * 4', '5 * 4'],
          'Die Zahlen sind 3k und 5k. (3k + 4) : (5k + 4) = 2 : 3 ⇒ 3 · (3k + 4) = 2 · (5k + 4) ⇒ 9k + 12 = 10k + 8 ⇒ k = 4. Also 12 und 20. Probe: 16 : 24 = 2 : 3.', 'Schreibe die Zahlen als 3k und 5k.'))
ST.knobel('kuerzen', L('Es gilt a : b = 2 : 3 und b : c = 4 : 5. Gib a : b : c mit möglichst kleinen ganzen Zahlen an.', '□ : □ : □', [8, 12, 15], ['8', '12', '15'],
          'b muss in beiden Verhältnissen gleich sein. 3 und 4 haben das kleinste gemeinsame Vielfache 12: a : b = 8 : 12 und b : c = 12 : 15. Also 8 : 12 : 15.', 'Bringe b in beiden Verhältnissen auf dieselbe Zahl.'))

# gleichwertig
ST.stufenleiter('gleichwertig', 'Gleichwertige Verhältnisse durch Erweitern ergänzen und erkennen.',
                'Mischungen vergleichen, Rezept mit drei Zutaten, Gesamtzahl aus einem Teil, Modellmaßstab, Verhältnis aus einem Bild.',
                'Fehler „addieren statt multiplizieren“, x : 3 = 12 : x, Mischung nachbessern, Prozent als Verhältnis, Sirupmenge rückwärts, Prüfungsaufgabe.')
ST.typ('gleichwertig', 'Ergänze', 'direkt')
ST.typ('gleichwertig', 'Welches Verhältnis ist gleichwertig zu', 'erkennen')
ST.typ('gleichwertig', 'Ina sagt', 'fehler')
ST.typ('gleichwertig', 'Mischung A', 'einkleidung')
ST.typ('gleichwertig', 'Für welche positive Zahl', 'parameter')
ST.typ('gleichwertig', '/^(Mehl, Zucker|Mädchen und Jungen)/', 'mehrschritt')
ST.typ('gleichwertig', 'Welche beiden Verhältnisse', 'begruenden')
ST.neu('gleichwertig', 'darstellung', A('Ein Bild zeigt 2 Becher Mehl und 1 Becher Milch. Welches Verhältnis Mehl : Milch ist dazu gleichwertig?', '6 : 3', ['3 : 6', '2 : 3', '4 : 3'],
       'Mehl : Milch = 2 : 1. Mal 3 erweitert: 6 : 3.', 'Lies erst das Verhältnis am Bild ab.'))
ST.neu('gleichwertig', 'einkleidung', Z('Ein Modellauto ist im Verhältnis 1 : 18 gebaut. Das echte Auto ist 4,5 m lang. Wie lang ist das Modell in cm?', 25, '450 / 18',
       '4,5 m = 450 cm. 450 cm : 18 = 25 cm.', 'Rechne zuerst in cm um.', einheit='cm'))
ST.neu('gleichwertig', 'transfer', Z('Für eine Fruchtschorle mischt man Saft und Wasser im Verhältnis 2 : 3. Man hat schon 1 l Saft und 1 l Wasser gemischt. Wie viel Liter Wasser muss man noch dazugeben?', 0.5, '1 * 3 / 2 - 1',
       'Zu 1 l Saft gehören 1 · 3 : 2 = 1,5 l Wasser. Es fehlen noch 0,5 l.', 'Wie viel Wasser gehört zu 1 l Saft?', einheit='l'))
ST.neu('gleichwertig', 'verknuepfen', A('Ein Teil ist 40 % des Ganzen. Welches Verhältnis Teil : Ganzes ist das?', '2 : 5', ['2 : 3', '4 : 6', '5 : 2'],
       '40 % = 40/100 = 2/5, also Teil : Ganzes = 2 : 5. (Teil : Rest wäre 2 : 3.)', 'Schreibe die Prozentzahl als gekürzten Bruch.'))
ST.neu('gleichwertig', 'rueckwaerts', Z('Sirup und Wasser wurden im Verhältnis 1 : 5 gemischt. Nach dem Dazugießen von 100 ml Wasser ist das Verhältnis 1 : 7. Wie viel ml Sirup ist im Getränk?', 50, '100 // 2',
       'Sirup s, Wasser 5s. Nachher 5s + 100 = 7s ⇒ 2s = 100 ⇒ s = 50 ml. Probe: 50 : 350 = 1 : 7.', 'Schreibe den Sirup als s.', einheit='ml'))
ST.neu('gleichwertig', 'pruefung', L('a) Sind 6 : 9 und 10 : 15 gleichwertig? (1 = ja, 0 = nein) b) Sind 4 : 5 und 12 : 16 gleichwertig? c) Ergänze: 9 : 12 = □ : 20.', 'a) □; b) □; c) □', [1, 0, 15],
       ['1', '0', '15'], 'a) Beide gekürzt 2 : 3: ja. b) 4 : 5 und 3 : 4: nein. c) 9 : 12 = 3 : 4 = 15 : 20.', 'Kürze die Verhältnisse zum Vergleichen.'))
ST.knobel('gleichwertig', Z('Für welche positive Zahl x sind x : 6 und 6 : (x + 5) gleichwertig?', 4, '4',
          'Gleichwertig heißt: x · (x + 5) = 6 · 6 = 36. Probieren: x = 4 ergibt 4 · 9 = 36. Probe: 4 : 6 = 2 : 3 und 6 : 9 = 2 : 3.', 'Schreibe die Bedingung als Produkt und probiere.'))
ST.knobel('gleichwertig', Z('Wie viele Verhältnisse a : b mit natürlichen Zahlen a und b, beide höchstens 20, sind gleichwertig zu 3 : 4?', 5, '20 // 4',
          'Gleichwertig sind 3k : 4k. Damit 4k ≤ 20 gilt, ist k = 1, …, 5: 3 : 4, 6 : 8, 9 : 12, 12 : 16, 15 : 20. Also 5.', 'Erweitere 3 : 4 schrittweise.'))

# aufteilen
ST.stufenleiter('aufteilen', 'Eine Größe im Verhältnis zweier Zahlen aufteilen; die Zahl der Teile erkennen.',
                'Sachsituationen mit Teig, Gewinn und Seil, drei Personen, Gesamtmenge aus einem Teil.',
                'Gesamtmenge aus Unterschied und kleinstem Anteil, Rechteck mit Umfang, Fehler „durch jede Zahl einzeln geteilt“, Hälfte begründen, Parameter k, Gewinn nach Einsatz, Prüfungsaufgabe.')
ST.typ('aufteilen', 'Teile ', 'direkt')
ST.typ('aufteilen', '/^(Für einen Teig|Zwei Geschwister|Ein [\\d,]+ m langes Seil)/', 'einkleidung')
ST.typ('aufteilen', 'Wasser und Saft', 'umkehr')
ST.typ('aufteilen', '240 € werden', 'mehrschritt')
ST.typ('aufteilen', '/^(Zwei Freunde|Ein Erbe)/', 'rueckwaerts')
ST.typ('aufteilen', 'Ein Rechteck', 'verknuepfen')
ST.neu('aufteilen', 'erkennen', A('110 € sollen im Verhältnis 7 : 4 aufgeteilt werden. In wie viele gleiche Teile teilt man zuerst?', 'in 11 Teile', ['in 7 Teile', 'in 4 Teile', 'in 28 Teile'],
       '7 + 4 = 11 Teile. Ein Teil ist 110 € : 11 = 10 €.', 'Zähle die Teile zusammen.'))
ST.neu('aufteilen', 'direkt', L('Verteile 60 Murmeln im Verhältnis 1 : 2.', '□ und □', [20, 40], ['60 // 3', '2 * 20'],
       '1 + 2 = 3 Teile, ein Teil 60 : 3 = 20. Also 20 und 40 Murmeln.', 'Wie viele Teile gibt es?'))
ST.neu('aufteilen', 'fehler', A('Jemand teilt 90 € im Verhältnis 2 : 1 so auf: 90 : 2 = 45 € und 90 : 1 = 90 €. Was stimmt?', 'Falsch: Es gibt 3 Teile zu je 30 €, also 60 € und 30 €.',
       ['Richtig.', 'Falsch: 45 € und 45 €.', 'Falsch: 80 € und 10 €.'], 'Zusammen müssen es 90 € sein, nicht 135 €. Erst die Teile zählen: 2 + 1 = 3, ein Teil 30 €.', 'Ergeben beide Beträge zusammen 90 €?'))
ST.neu('aufteilen', 'begruenden', A('Stimmt: Teilt man im Verhältnis 1 : 1 : 2, bekommt der Größte genau die Hälfte?', 'Ja: 2 von 1 + 1 + 2 = 4 Teilen sind die Hälfte.', ['Nein, ein Drittel.', 'Nein, zwei Drittel.', 'Das hängt vom Betrag ab.'],
       'Es gibt 4 Teile. Der Größte bekommt 2 davon, also 2/4 = 1/2 – egal wie groß der Betrag ist.', 'Wie viele Teile gibt es insgesamt?'))
ST.neu('aufteilen', 'parameter', Z('400 € werden im Verhältnis 3 : k aufgeteilt. Der erste Anteil ist 120 €. Wie groß ist k?', 7, '400 // 40 - 3',
       '3 Teile sind 120 €, ein Teil 40 €. 400 € sind 10 Teile, also 3 + k = 10 ⇒ k = 7.', 'Wie groß ist ein Teil?'))
ST.neu('aufteilen', 'transfer', Z('Drei Freunde zahlen für ein Los 5 €, 10 € und 15 €. Sie gewinnen 240 € und teilen gerecht nach ihren Einsätzen. Wie viel bekommt der, der 10 € gezahlt hat?', 80, '240 * 10 // 30',
       'Verhältnis 5 : 10 : 15 = 1 : 2 : 3, also 6 Teile zu je 40 €. Der Zweite bekommt 2 Teile: 80 €.', 'Stelle zuerst das Verhältnis der Einsätze auf.', einheit='€'))
ST.neu('aufteilen', 'pruefung', L('Ein Gewinn von 1 800 € wird im Verhältnis 2 : 3 : 4 verteilt. a) Wie viel Euro ist ein Teil? b) Wie viel bekommt der Größte? c) Wie viel mehr bekommt der Größte als der Kleinste?',
       'a) □ €; b) □ €; c) □ €', [200, 800, 400], ['1800 // 9', '4 * 200', '(4 - 2) * 200'], 'a) 2 + 3 + 4 = 9 Teile, 1 800 : 9 = 200 €. b) 4 · 200 = 800 €. c) 800 − 400 = 400 €.', 'Erst die Teile zählen.'))
ST.knobel('aufteilen', Z('Drei Geschwister teilen Bonbons im Verhältnis 2 : 3 : 4. Das jüngste bekommt 12 Bonbons weniger als das älteste. Wie viele Bonbons sind es insgesamt?', 54, '9 * 6',
          'Der Unterschied sind 4 − 2 = 2 Teile = 12 Bonbons, also ein Teil 6. Insgesamt 9 Teile: 54 Bonbons (12, 18, 24).', 'Wie viele Teile sind der Unterschied?'))
ST.knobel('aufteilen', Z('Ein Betrag wird im Verhältnis 3 : 5 geteilt. Bei einer Teilung im Verhältnis 1 : 1 bekäme der Erste 30 € mehr. Wie groß ist der Betrag?', 240, '8 * 30',
          '3 : 5 sind 8 Teile. Bei 1 : 1 bekommt jeder 4 Teile. Der Erste bekäme also 1 Teil mehr: 1 Teil = 30 €. Betrag 8 · 30 = 240 €.', 'Wie viele Teile bekommt der Erste jeweils?', einheit='€'))

# proportion
ST.stufenleiter('proportion', 'Eine Proportion lösen und Rezeptmengen mit dem Dreisatz umrechnen; die passende Proportion erkennen.',
                'Krumme Faktoren, Verbrauch eines Autos, Kartenmaßstab in beide Richtungen.',
                'Nicht proportionale Situationen begründen, indirekte Proportionalität, Wechselkurs und Poster als Modell, Maßstab rückwärts, Fehler „addiert statt multipliziert“, Prüfungsaufgabe Karte.')
ST.typ('proportion', 'Löse die Proportion', 'direkt')
ST.typ('proportion', 'Für 5 Portionen braucht man 250', 'direkt')
ST.typ('proportion', 'Für ', 'mehrschritt')
ST.typ('proportion', 'Ein Auto braucht', 'einkleidung')
ST.typ('proportion', 'Eine Wanderkarte', 'darstellung')
ST.typ('proportion', 'Maßstab 1 :', 'umkehr')
ST.typ('proportion', '/^\\d Hemden/', 'begruenden')
ST.typ('proportion', '3 Maler', 'verknuepfen')
ST.typ('proportion', '/^(Der Wechselkurs|Ein Handyfoto)/', 'transfer')
ST.typ('proportion', 'Auf einer Karte', 'rueckwaerts')
ST.neu('proportion', 'erkennen', A('3 Hefte kosten 6 €. Welche Proportion passt zur Frage „Was kosten 5 Hefte?“', '3 : 6 = 5 : x', ['3 : 5 = x : 6', '3 : 6 = x : 5', '6 : 3 = 5 : x'],
       'Hefte : Preis bleibt gleich: 3 : 6 = 5 : x. Dann x = 10 €.', 'Was steht links, was rechts im Verhältnis?'))
ST.neu('proportion', 'fehler', A('Jemand löst 3 : 4 = x : 12 mit x = 11: „Von 4 nach 12 sind es 8 mehr, also 3 + 8.“ Was stimmt?', 'Falsch: Man multipliziert, 4 · 3 = 12, also x = 3 · 3 = 9.',
       ['Richtig.', 'Falsch: x = 16.', 'Falsch: x = 1.'], 'Gleichwertige Verhältnisse entstehen durch Malnehmen. 11 : 12 ist nicht gleichwertig zu 3 : 4, aber 9 : 12 schon.', 'Mach die Probe mit gekürzten Verhältnissen.'))
ST.neu('proportion', 'pruefung', L('Eine Karte hat den Maßstab 1 : 200 000. a) Wie viele km sind 3 cm auf der Karte? b) Wie viele cm sind 10 km in Wirklichkeit auf der Karte?', 'a) □ km; b) □ cm', [6, 5],
       ['3 * 200000 // 100000', '10 * 100000 // 200000'], 'a) 3 cm · 200 000 = 600 000 cm = 6 km. b) 10 km = 1 000 000 cm, : 200 000 = 5 cm.', '1 km = 100 000 cm.'))
ST.knobel('proportion', Z('3 Katzen fangen in 3 Minuten 3 Mäuse. Wie viele Katzen fangen in 100 Minuten 100 Mäuse (alle gleich schnell)?', 3, '3',
          'Die 3 Katzen fangen zusammen 1 Maus pro Minute. In 100 Minuten fangen sie also 100 Mäuse. Man braucht nur 3 Katzen.', 'Wie viele Mäuse fangen die 3 Katzen pro Minute?'))
ST.knobel('proportion', Z('Ein Rezept für 4 Personen braucht 3 Eier. Für wie viele Personen reicht eine Packung mit 10 Eiern höchstens (Eier dürfen übrig bleiben)?', 13, '13',
          'Pro Person 3 : 4 = 0,75 Eier. 10 : 0,75 = 13,3… Für 13 Personen braucht man 9,75 Eier, für 14 schon 10,5. Also 13 Personen.', 'Wie viele Eier braucht eine Person?'))

# einheitsrate
ST.stufenleiter('einheitsrate', 'Den Wert für eine Einheit bestimmen (pro Stunde, pro Stück, pro kg) und anwenden; eine Einheitsrate erkennen.',
                'Preise pro 100 g, Angebote vergleichen, Aktion „4 für 3“, Reichweite aus dem Verbrauch.',
                'Mehrere Angebote, Ersparnis pro Stück und Liter, Seiten pro Minute, Geschwindigkeiten vergleichen, Fehler „Gesamtpreis verglichen“, gleich teurer Preis als Parameter, Prüfungsaufgabe.')
ST.typ('einheitsrate', '/^(Ein Radfahrer|\\d Hefte|Ein Zug|Äpfel kosten)/', 'direkt')
ST.typ('einheitsrate', 'Kaffee wird angeboten – A: 1 000', 'transfer')
ST.typ('einheitsrate', '/^(Kaffee wird angeboten|Eine Packung)/', 'mehrschritt')
ST.typ('einheitsrate', 'Aktion', 'einkleidung')
ST.typ('einheitsrate', 'Ein Auto verbraucht', 'umkehr')
ST.typ('einheitsrate', '/^(Angebot A: 3|Saft: 1,5|Ein Drucker)/', 'verknuepfen')
ST.typ('einheitsrate', 'Läuferin', 'begruenden')
ST.neu('einheitsrate', 'erkennen', A('Welche Angabe ist eine Einheitsrate?', '3 € pro kg', ['3 € für 2 kg', '2 kg Äpfel', '12 Äpfel in der Tüte'],
       'Eine Einheitsrate gibt an, wie viel auf genau eine Einheit kommt: 3 € für 1 kg.', 'Auf wie viel bezieht sich die Angabe?'))
ST.neu('einheitsrate', 'fehler', A('Jemand vergleicht 500 g für 4 € mit 1 kg für 7 € und sagt: „Das erste ist billiger, weil 4 € weniger ist als 7 €.“ Was stimmt?', 'Falsch: Pro kg kostet das erste 8 €, das zweite nur 7 €.',
       ['Richtig.', 'Falsch: Beide sind gleich teuer.', 'Falsch: Das zweite kostet 14 € pro kg.'], 'Man muss gleiche Mengen vergleichen: 500 g für 4 € sind 8 € pro kg.', 'Rechne beide auf 1 kg um.'))
ST.neu('einheitsrate', 'parameter', Z('Packung A: 400 g für 5,20 €. Packung B: 600 g für p €. Bei welchem Preis p sind beide gleich günstig?', 7.8, '5.2 / 4 * 6',
       'A kostet 5,20 € : 4 = 1,30 € pro 100 g. Gleich günstig: 6 · 1,30 € = 7,80 €.', 'Berechne den Preis pro 100 g.', einheit='€'))
ST.neu('einheitsrate', 'pruefung', L('Saft: einzeln 1 l für 1,20 € oder im 6er-Pack (je 1 l) für 6,30 €. a) Wie viel Cent kostet 1 l im 6er-Pack? b) Wie viel Cent spart man pro Liter?', 'a) □ ct; b) □ ct', [105, 15],
       ['630 // 6', '120 - 105'], 'a) 6,30 € : 6 = 1,05 € = 105 ct. b) 120 ct − 105 ct = 15 ct.', 'Rechne in Cent.'))
ST.knobel('einheitsrate', Z('Ein Wasserhahn füllt eine Wanne in 12 Minuten, ein zweiter in 6 Minuten. Wie lange dauert es mit beiden zusammen?', 4, '4',
          'Pro Minute füllt der erste 1/12, der zweite 1/6 = 2/12 der Wanne. Zusammen 3/12 = 1/4 pro Minute, also 4 Minuten.', 'Welchen Teil der Wanne füllt jeder Hahn pro Minute?', einheit='min'))
ST.knobel('einheitsrate', Z('Ein Auto fährt 60 km mit 60 km/h und danach 60 km mit 120 km/h. Wie groß ist die Durchschnittsgeschwindigkeit?', 80, '120 / 1.5',
          'Zeit: 1 h + 0,5 h = 1,5 h für 120 km. 120 : 1,5 = 80 km/h – nicht 90 km/h, denn das Auto ist länger langsam unterwegs.', 'Rechne die Gesamtzeit aus.', einheit='km/h'))

# aenderung
ST.stufenleiter('aenderung', 'Eine Änderungsrate aus Anfangs- und Endwert berechnen; schneller und langsamer erkennen.',
                'Negative Raten, Werte aus der Rate berechnen, Rate aus einer Tabelle, Leerlaufen eines Pools.',
                'Anfangswert rückwärts, gleiche Höhe zweier Kerzen, Bedeutung einer negativen Rate, Fehler beim Vorzeichen, Bereich für die Rate, Akku als Modell, Prüfungsaufgabe.')
ST.typ('aenderung', '/^(Ein Becken enthält|Um \\d+ Uhr)/', 'direkt')
ST.typ('aenderung', 'Robotermäher', 'erkennen')
ST.typ('aenderung', '/^Ein Tank (wird mit \\d+ Litern pro Minute gefüllt\\. Am Anfang|enthält)/', 'umkehr')
ST.typ('aenderung', '/^(Eine Kerze ist|Ein Flugzeug)/', 'mehrschritt')
ST.typ('aenderung', 'Ein Becken: nach', 'darstellung')
ST.typ('aenderung', 'Ein Pool', 'einkleidung')
ST.typ('aenderung', '/^(Ein Tank wird mit \\d+ Litern pro Minute gefüllt\\. Nach|Von 8 Uhr)/', 'rueckwaerts')
ST.typ('aenderung', 'Kerze A', 'verknuepfen')
ST.typ('aenderung', 'Die Änderungsrate', 'begruenden')
ST.neu('aenderung', 'fehler', A('Jemand berechnet die Änderungsrate von 20 °C um 14 Uhr auf 14 °C um 17 Uhr als (20 − 14) : 3 = +2 °C pro Stunde. Was stimmt?', 'Falsch: Die Temperatur sinkt, die Rate ist −2 °C pro Stunde.',
       ['Richtig.', 'Falsch: −6 °C pro Stunde.', 'Falsch: +6 °C pro Stunde.'], 'Änderung = Endwert − Anfangswert = 14 − 20 = −6 °C in 3 h, also −2 °C pro Stunde.', 'Rechne Endwert minus Anfangswert.'))
ST.neu('aenderung', 'parameter', A('Ein Becken enthält 100 l. Für welche Zuflussraten r (in Litern pro Minute) sind nach 10 Minuten mehr als 150 l darin?', 'für r > 5', ['für r > 15', 'für r < 5', 'für r > 50'],
       '100 + 10r > 150 ⇒ 10r > 50 ⇒ r > 5.', 'Stelle eine Ungleichung auf.'))
ST.neu('aenderung', 'transfer', Z('Ein Handyakku zeigt 80 % und verliert 6 Prozentpunkte pro Stunde. Bei 20 % kommt eine Warnung. Nach wie vielen Stunden?', 10, '(80 - 20) // 6',
       'Es müssen 80 − 20 = 60 Prozentpunkte verbraucht werden: 60 : 6 = 10 Stunden.', 'Wie viel muss sich ändern?', einheit='h'))
ST.neu('aenderung', 'pruefung', L('Eine Badewanne enthält 30 l. Es fließen 12 l pro Minute zu. a) Wie viel Liter sind es nach 5 Minuten? b) Nach wie vielen Minuten sind es 150 l?', 'a) □ l; b) □ min', [90, 10],
       ['30 + 12 * 5', '(150 - 30) // 12'], 'a) 30 + 12 · 5 = 90 l. b) 150 − 30 = 120 l, 120 : 12 = 10 min.', 'Anfangswert plus Rate mal Zeit.'))
ST.knobel('aenderung', Z('Kerze A ist 20 cm hoch und brennt in 4 Stunden ganz ab, Kerze B ist 15 cm hoch und brennt in 5 Stunden ab. Beide werden gleichzeitig angezündet. Nach wie vielen Stunden sind sie gleich hoch?', 2.5, '5 / 2',
          'Raten: A −5 cm/h, B −3 cm/h. 20 − 5t = 15 − 3t ⇒ 5 = 2t ⇒ t = 2,5 h. Dann sind beide 7,5 cm hoch.', 'Bestimme zuerst die Abbrennraten.', einheit='h'))
ST.knobel('aenderung', Z('Ein leeres Becken mit 200 l wird mit 8 l pro Minute gefüllt, gleichzeitig laufen 3 l pro Minute aus. Nach wie vielen Minuten ist es voll?', 40, '200 // (8 - 3)',
          'Insgesamt kommen pro Minute 8 − 3 = 5 l dazu. 200 : 5 = 40 Minuten.', 'Wie groß ist die Änderungsrate insgesamt?', einheit='min'))

stufen('groessen.verhaeltnisse', ST)
