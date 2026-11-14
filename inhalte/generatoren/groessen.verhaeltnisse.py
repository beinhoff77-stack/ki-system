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

bauen('groessen.verhaeltnisse',
      'Verhältnisse kürzen und vergleichen, im Verhältnis aufteilen, Proportionen lösen, Einheitsraten und Änderungsraten berechnen.',
      ['Verhältnis (ratio) a : b – kürzen und erweitern wie bei Brüchen, nie addieren.',
       'Aufteilen: Teile zählen, einen Teil berechnen, vervielfachen.',
       'Einheitsrate (unit rate): Wert für genau 1 Einheit – so vergleicht man Angebote.',
       'Änderungsrate (rate of change) = Änderung : Zeitspanne; Abnahme ergibt eine negative Rate.'],
      [('Verhältnisse', ['kuerzen', 'gleichwertig', 'aufteilen']), ('Proportionen', ['proportion']), ('Raten', ['einheitsrate', 'aenderung'])],
      ETAPPEN, GEN,
      offen=['Antworten bei Verhältnissen als Lücken □ : □ (je ein Zahlenfeld). Die App zeigt den Doppelpunkt aus der Schablone.',
             'Proportionen bewusst ohne Kreuzprodukt-Formel, sondern über Faktor und Dreisatz (Niveau MYP 2 ≈ Klasse 7).'])
