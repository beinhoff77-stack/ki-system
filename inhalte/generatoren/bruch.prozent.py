#!/usr/bin/env python3
"""Thema bruch.prozent – Prozent- und Zinsrechnung (Klasse 6)."""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _basis import *  # noqa: E402,F403

R = random.Random(24)
E = eintrag_laden('bruch.prozent')
HB = 'Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt.'

ETAPPEN = [
    {'lernziel': 'prozent_bedeutung', 'titel': 'Was bedeutet Prozent?',
     'regel': '⟦Prozent⟧ heißt ⟦Hundertstel⟧: 1 % = 1/100 = 0,01. So wandelst du um: 35 % = 35/100 = 0,35. Umgekehrt: Dezimalzahl ⟦mal 100⟧ ergibt die Prozentzahl.',
     'schritte': ['3/4 in Prozent: Erweitere auf Hundertstel, 3/4 = 75/100.', '75/100 = ⟦75 %⟧ = 0,75.'],
     'fehler': '0,5 = 5 % ist falsch: 0,5 = 50/100 = ⟦50 %⟧. Beim Umwandeln wandert das Komma ⟦zwei⟧ Stellen.'},
    {'lernziel': 'prozentwert', 'titel': 'Prozentwert berechnen',
     'regel': 'Der ⟦Grundwert G⟧ ist das Ganze (100 %). Der ⟦Prozentwert W⟧ ist der Teil davon. Es gilt ⟦W = G · p %⟧. Tipp: Rechne zuerst 1 % aus (G : 100).',
     'schritte': ['15 % von 240 €: 1 % von 240 € sind 2,40 €.', '15 % sind 15 · 2,40 € = ⟦36 €⟧.'],
     'probe': '36 : 240 = 0,15 = 15 % ✓',
     'fehler': '15 % von 240 € als 240 : 15 = 16 € zu rechnen ist falsch: 15 % heißt ⟦15 Hundertstel⟧. Also 240 · 15 : 100 = 36 €.'},
    {'lernziel': 'prozentsatz', 'titel': 'Prozentsatz berechnen',
     'regel': 'Den ⟦Prozentsatz⟧ findest du mit ⟦p % = W : G⟧ – Teil durch Ganzes. Das Ergebnis als Dezimalzahl mal 100 ergibt die Prozentzahl.',
     'schritte': ['Von 25 Aufgaben sind 21 richtig. 21 : 25 = 0,84.', '0,84 = ⟦84 %⟧.'],
     'probe': '84 % von 25 = 25 · 0,84 = 21 ✓',
     'fehler': '25 : 21 zu rechnen ist falsch: Der Anteil ist ⟦Teil durch Ganzes⟧, also 21 : 25. Ein Prozentsatz über 100 % wäre hier unmöglich.'},
    {'lernziel': 'grundwert', 'titel': 'Grundwert berechnen',
     'regel': 'Kennst du ⟦Prozentwert und Prozentsatz⟧, findest du den Grundwert rückwärts: ⟦G = W : p %⟧. Oder über 1 %: erst W : p, dann mal 100.',
     'schritte': ['30 % sind 12 kg. 1 % sind 12 kg : 30 = 0,4 kg.', '100 % sind 0,4 kg · 100 = ⟦40 kg⟧.'],
     'probe': '30 % von 40 kg = 12 kg ✓',
     'fehler': '12 kg · 0,3 = 3,6 kg ist falsch: Das wäre 30 % ⟦von⟧ 12 kg. Gesucht ist das Ganze – es muss ⟦größer⟧ als 12 kg sein.'},
    {'lernziel': 'rabatt_aufschlag', 'titel': 'Rabatt und Aufschlag',
     'regel': 'Bei ⟦Rabatt⟧ (Preisnachlass) zahlst du nur noch ⟦100 % − p %⟧ des alten Preises. Bei einem ⟦Aufschlag⟧ (z. B. Preiserhöhung) zahlst du ⟦100 % + p %⟧.',
     'schritte': ['Eine Jacke kostet 80 €, es gibt 25 % Rabatt. Du zahlst noch 100 % − 25 % = 75 %.', '80 € · 0,75 = ⟦60 €⟧.'],
     'probe': '25 % von 80 € = 20 €, und 80 € − 20 € = 60 € ✓',
     'fehler': '80 € − 25 € = 55 € ist falsch: Man zieht nicht 25 Euro ab, sondern ⟦25 % von 80 €⟧ = 20 €.'},
    {'lernziel': 'zinsen', 'titel': 'Zinsen berechnen',
     'regel': 'Legst du Geld (das ⟦Kapital K⟧) bei einer Bank an, zahlt sie dir ⟦Zinsen Z⟧. Der ⟦Zinssatz p %⟧ ist ein Prozentsatz pro Jahr. ⟦Jahreszinsen: Z = K · p %⟧.',
     'schritte': ['500 € werden ein Jahr lang zu 3 % angelegt. Zinsen: 500 € · 0,03 = 15 €.', 'Nach einem Jahr hat man 500 € + 15 € = ⟦515 €⟧.'],
     'fehler': 'Bei 3 % auf 500 € nur 3 € Zinsen anzunehmen ist falsch: 3 % heißt ⟦3 € für je 100 €⟧, also 5 · 3 € = 15 €.'},
    {'lernziel': 'verstehen', 'titel': 'Prozentaussagen prüfen',
     'regel': 'Bei Prozenten kommt es immer auf den ⟦Grundwert⟧ an: 10 % von 50 € ist etwas anderes als 10 % von 500 €. Prüfe Aussagen mit ⟦konkreten Zahlen⟧.',
     'schritte': ['Aussage: „Erst 10 % billiger, dann 10 % teurer – der Preis ist wieder gleich.“ Test mit 100 €.', '100 € → 90 € → 90 € + 9 € = 99 €. Das ist nicht 100 €, die Aussage ist ⟦falsch⟧.'],
     'fehler': 'Prozente einfach zu addieren oder zu subtrahieren ist oft falsch: Der zweite Schritt bezieht sich auf einen ⟦anderen Grundwert⟧ (hier 90 € statt 100 €).'},
]

MERKE = ['p % = p/100. 50 % = 1/2, 25 % = 1/4, 20 % = 1/5, 10 % = 1/10.', 'W = G · p %   ·   p % = W : G   ·   G = W : p %.',
         'Rabatt p %: neuer Preis = G · (100 % − p %). Aufschlag: G · (100 % + p %).', 'Jahreszinsen: Z = K · p %.']

ANTEILE = [(Fr(1, 2), 50), (Fr(1, 4), 25), (Fr(3, 4), 75), (Fr(1, 5), 20), (Fr(2, 5), 40), (Fr(3, 5), 60), (Fr(4, 5), 80), (Fr(1, 10), 10),
           (Fr(3, 10), 30), (Fr(7, 10), 70), (Fr(9, 10), 90), (Fr(1, 20), 5), (Fr(1, 25), 4), (Fr(1, 50), 2), (Fr(1, 8), Fr(25, 2)), (Fr(3, 20), 15)]


def pz(p): return f'{zt(p)} %'


def ok(x, k=2):
    """endlich mit höchstens k Nachkommastellen"""
    return (Fr(x) * 10 ** k).denominator == 1


def euro(x):
    """Geldbetrag: ganze Euro ohne Komma, sonst immer zwei Nachkommastellen."""
    x = Fr(x)
    if x.denominator == 1: return f'{zt(x)} €'
    s = zt(x)
    g, n = s.split(',')
    return f'{g},{n.ljust(2, "0")} €'


# ---------- 1 Bedeutung ----------
def g_bed(st):
    if st == 1:
        art = R.randrange(3)
        if art == 0:
            p = R.randint(1, 99)
            return {'y': 'zahl', 'f': {'text': f'Schreibe {pz(p)} als Dezimalzahl.'}, 'o': {'wert': wert(Fr(p, 100))}, 'c': f'{p} / 100',
                    'w': f'{pz(p)} = {p}/100 = {zt(Fr(p, 100))}.', 'h': 'Prozent heißt Hundertstel: durch 100 teilen.'}
        if art == 1:
            d = Fr(R.randint(1, 99), 100)
            return {'y': 'zahl', 'f': {'text': f'Schreibe {zt(d)} in Prozent.'}, 'o': {'wert': wert(d * 100), 'einheit': '%'}, 'c': f'{float(d)} * 100',
                    'w': f'{zt(d)} = {int(d * 100)}/100 = {pz(d * 100)}.', 'h': 'Mal 100: Komma um zwei Stellen nach rechts.'}
        b, p = R.choice(ANTEILE[:11])
        return {'y': 'zahl', 'f': {'text': f'Wie viel Prozent sind {bruch(b)}?'}, 'o': {'wert': wert(p), 'einheit': '%'}, 'c': f'{b.numerator} / {b.denominator} * 100',
                'w': f'Auf Hundertstel erweitern: {bruch(b)} = {int(b * 100)}/100 = {pz(p)}.', 'h': 'Erweitere den Bruch auf den Nenner 100.'}
    if st == 2:
        art = R.randrange(3)
        if art == 0:
            p = R.choice([2, 4, 5, 6, 8, 12, 15, 16, 24, 35, 45, 55, 64, 85, 96, 120, 150, 250])
            x = Fr(p, 100)
            return {'y': 'luecken', 'f': {'text': f'Schreibe {pz(p)} als vollständig gekürzten Bruch.', 'schablone': '□/□', 'hinweis': HB}, 'o': {'werte': [x.numerator, x.denominator]},
                    'c': [f'{p} / 100 * {x.denominator}', f'{x.denominator}'], 'w': f'{pz(p)} = {p}/100 = {bruch(x)}.', 'h': 'Schreibe p/100 und kürze.'}
        if art == 1:
            d = Fr(R.randint(1, 999), 1000)
            while d * 1000 % 10 == 0: d = Fr(R.randint(1, 999), 1000)
            return {'y': 'zahl', 'f': {'text': f'Schreibe {zt(d)} in Prozent.'}, 'o': {'wert': wert(d * 100), 'einheit': '%'}, 'c': f'{float(d)} * 100',
                    'w': f'{zt(d)} · 100 = {zt(d * 100)}, also {pz(d * 100)}.', 'h': 'Komma um zwei Stellen nach rechts.'}
        b = Fr(R.randint(1, 49), R.choice([20, 25, 50, 40, 8]))
        while b >= 1 or b.denominator == 1: b = Fr(R.randint(1, 49), R.choice([20, 25, 50, 40, 8]))
        return {'y': 'zahl', 'f': {'text': f'Wie viel Prozent sind {bruch(b)}?'}, 'o': {'wert': wert(b * 100), 'einheit': '%'}, 'c': f'{b.numerator} / {b.denominator} * 100',
                'w': f'{bruch(b)} = {zt(b)} = {pz(b * 100)}.', 'h': 'Wandle zuerst in eine Dezimalzahl um, dann mal 100.'}
    art = R.randrange(3)
    if art == 0:
        b, p = R.choice(ANTEILE)
        q = Fr(p) + R.choice([-5, 5, -10, 10])
        a, c = (bruch(b), pz(q))
        r = a if b * 100 > q else c
        return {**wahl(R, r, [c if r == a else a, 'Beide sind gleich groß'], 3), 'f': {'text': f'Was ist mehr: {a} oder {c}?'},
                'w': f'{a} = {pz(p)}. Vergleich mit {c}: {r} ist mehr.', 'h': 'Wandle den Bruch in Prozent um.'}
    if art == 1:
        d = Fr(R.randint(101, 350), 100)
        return {'y': 'zahl', 'f': {'text': f'Schreibe {zt(d)} in Prozent.'}, 'o': {'wert': wert(d * 100), 'einheit': '%'}, 'c': f'{float(d)} * 100',
                'w': f'{zt(d)} · 100 = {zt(d * 100)}, also {pz(d * 100)}. Mehr als ein Ganzes ergibt mehr als 100 %.', 'h': '1 = 100 %. Was ist mehr als 1?'}
    n = R.choice([3, 6, 7, 9, 12])
    b = Fr(R.randint(1, n - 1), n)
    while b.denominator in (1, 2, 4, 5): b = Fr(R.randint(1, n - 1), n)
    gerundet = (b * 1000 + Fr(1, 2)) // 1 / Fr(10)
    return {'y': 'zahl', 'f': {'text': f'Wie viel Prozent sind {bruch(b)}? Runde auf eine Nachkommastelle.'}, 'o': {'wert': wert(gerundet), 'einheit': '%'},
            'c': f'({b.numerator} / {b.denominator} * 1000 + 1/2) // 1 / 10', 'w': f'{b.numerator} : {b.denominator} ≈ {zt(gerundet / 100)}, also etwa {pz(gerundet)}.',
            'h': 'Teile den Zähler durch den Nenner, nimm mal 100 und runde.'}


# ---------- 2 Prozentwert ----------
DINGE = [('Kinder einer Schule mit', 'Kindern', 'Kinder'), ('Plätze eines Stadions mit', 'Plätzen', 'Plätze'), ('Seiten eines Buches mit', 'Seiten', 'Seiten'),
         ('Mitglieder eines Vereins mit', 'Mitgliedern', 'Mitglieder')]


def g_pw(st):
    if st == 1:
        p = R.choice([1, 10, 20, 25, 50, 75, 5])
        g = R.choice([20, 40, 60, 80, 100, 120, 200, 300, 400, 500, 800, 1000])
        e = R.choice(['€', 'kg', 'm', 'l'])
        w = Fr(g * p, 100)
        return {'y': 'zahl', 'f': {'text': f'Berechne {pz(p)} von {zt(g)} {e}.'}, 'o': {'wert': wert(w), 'einheit': e}, 'c': f'{g} * {p} / 100',
                'w': f'1 % von {zt(g)} {e} = {zt(Fr(g, 100))} {e}. {pz(p)}: {p} · {zt(Fr(g, 100))} = {zt(w)} {e}.', 'h': 'Rechne erst 1 % aus, dann mal die Prozentzahl.'}
    if st == 2:
        while True:
            p = R.randint(2, 95)
            g = R.randint(2, 99) * R.choice([5, 10, 20, 50])
            w = Fr(g * p, 100)
            if ok(w): break
        e = R.choice(['€', 'kg', 'km', 'l'])
        return {'y': 'zahl', 'f': {'text': f'Berechne {pz(p)} von {zt(g)} {e}.'}, 'o': {'wert': wert(w), 'einheit': e}, 'c': f'{g} * {p} / 100',
                'w': f'W = G · p % = {zt(g)} · {zt(Fr(p, 100))} = {zt(w)} {e}.', 'h': 'Schreibe p % als Dezimalzahl und nimm mit dem Grundwert mal.'}
    art = R.randrange(3)
    if art == 0:
        satz, dat, nom = R.choice(DINGE)
        p = R.choice([5, 12, 15, 24, 35, 45, 60, 85])
        g = R.choice([n for n in range(200, 2001, 20) if n * p % 100 == 0])
        return {'y': 'zahl', 'f': {'text': f'{pz(p)} der {satz} {zt(g)} {dat} – wie viele {nom} sind das?'}, 'o': {'wert': g * p // 100}, 'c': f'{g} * {p} / 100',
                'w': f'{zt(g)} · {zt(Fr(p, 100))} = {zt(g * p // 100)} {nom}.', 'h': 'Der Grundwert ist die Gesamtzahl. W = G · p %.'}
    if art == 1:
        p = R.choice([Fr(5, 2), Fr(15, 2), Fr(25, 2), Fr(3, 2), Fr(1, 2)])
        g = R.choice([n for n in range(40, 2001, 40)])
        w = g * p / 100
        if not ok(w): return g_pw(3)
        return {'y': 'zahl', 'f': {'text': f'Berechne {pz(p)} von {zt(g)} €.'}, 'o': {'wert': wert(w), 'einheit': '€'}, 'c': f'{g} * {float(p)} / 100',
                'w': f'{zt(g)} · {zt(p / 100)} = {zt(w)} €.', 'h': f'{pz(p)} = {zt(p / 100)} als Dezimalzahl.'}
    b, p = R.choice(ANTEILE[:8])
    g = b.denominator * R.randint(3, 40)
    w = g * b
    return {'y': 'zahl', 'f': {'text': f'Berechne {pz(p)} von {zt(g)} im Kopf. Tipp: {pz(p)} ist ein einfacher Bruch.'}, 'o': {'wert': wert(w)}, 'c': f'{g} * {p} / 100',
            'w': f'{pz(p)} = {bruch(b)}. {bruch(b)} von {zt(g)} = {zt(w)}.', 'h': '50 % = 1/2, 25 % = 1/4, 20 % = 1/5 …'}


# ---------- 3 Prozentsatz ----------
def g_ps(st):
    if st == 1:
        g = R.choice([100, 50, 20, 10, 200, 25])
        w = R.randint(1, g - 1)
        while not ok(Fr(w * 100, g), 1): w = R.randint(1, g - 1)
        p = Fr(w * 100, g)
        return {'y': 'zahl', 'f': {'text': f'Wie viel Prozent sind {w} von {g}?'}, 'o': {'wert': wert(p), 'einheit': '%'}, 'c': f'{w} / {g} * 100',
                'w': f'{w} : {g} = {zt(Fr(w, g))} = {pz(p)}.', 'h': 'Teil durch Ganzes, dann mal 100.'}
    if st == 2:
        while True:
            g = R.randint(12, 400)
            w = R.randint(1, g - 1)
            p = Fr(w * 100, g)
            if ok(p, 1) and g % 10: break
        return {'y': 'zahl', 'f': {'text': f'Wie viel Prozent sind {zt(w)} von {zt(g)}?'}, 'o': {'wert': wert(p), 'einheit': '%'}, 'c': f'{w} / {g} * 100',
                'w': f'{zt(w)} : {zt(g)} = {zt(Fr(w, g))} = {pz(p)}.', 'h': 'p % = W : G.'}
    art = R.randrange(3)
    if art == 0:
        alt = R.choice([20, 40, 50, 60, 80, 120, 150, 200, 250])
        p = R.choice([10, 20, 25, 30, 40, 15, 5])
        neu = alt - alt * p // 100
        if alt * p % 100: return g_ps(3)
        return {'y': 'zahl', 'f': {'text': f'Ein Preis sinkt von {zt(alt)} € auf {zt(neu)} €. Um wie viel Prozent wurde er gesenkt?'}, 'o': {'wert': p, 'einheit': '%'},
                'c': f'({alt} - {neu}) / {alt} * 100', 'w': f'Senkung: {zt(alt)} − {zt(neu)} = {zt(alt - neu)} €. {zt(alt - neu)} : {zt(alt)} = {zt(Fr(p, 100))} = {pz(p)}.',
                'h': 'Grundwert ist der alte Preis. Berechne zuerst den Unterschied.'}
    if art == 1:
        m = R.choice([3, 6, 9, 12, 15, 18, 24, 30, 36, 45, 48, 54])
        return {'y': 'zahl', 'f': {'text': f'Wie viel Prozent einer Stunde sind {m} Minuten?'}, 'o': {'wert': wert(Fr(m * 100, 60)), 'einheit': '%'}, 'c': f'{m} / 60 * 100',
                'w': f'1 h = 60 min. {m} : 60 = {zt(Fr(m, 60))} = {pz(Fr(m * 100, 60))}.', 'h': 'Grundwert: 60 Minuten.'}
    n = R.choice([20, 25, 40, 50])
    a, b = R.randint(2, n // 3), R.randint(2, n // 3)
    rest = n - a - b
    return {'y': 'zahl', 'f': {'text': f'Bei einer Umfrage unter {n} Kindern wählen {a} Fußball, {b} Schwimmen und der Rest Tanzen. Wie viel Prozent wählen Tanzen?'},
            'o': {'wert': wert(Fr(rest * 100, n)), 'einheit': '%'}, 'c': f'({n} - {a} - {b}) / {n} * 100',
            'w': f'Tanzen: {n} − {a} − {b} = {rest}. {rest} : {n} = {zt(Fr(rest, n))} = {pz(Fr(rest * 100, n))}.', 'h': 'Berechne zuerst, wie viele Kinder Tanzen wählen.'}


# ---------- 4 Grundwert ----------
def g_gw(st):
    if st == 1:
        p = R.choice([1, 10, 20, 25, 50, 5])
        g = R.choice([n for n in range(20, 1001, 20)])
        w = Fr(g * p, 100)
        e = R.choice(['€', 'kg', 'm'])
        return {'y': 'zahl', 'f': {'text': f'{pz(p)} sind {zt(w)} {e}. Wie viel sind 100 %?'}, 'o': {'wert': g, 'einheit': e}, 'c': f'{float(w)} / {p} * 100',
                'w': f'1 %: {zt(w)} : {p} = {zt(w / p)} {e}. 100 %: {zt(w / p)} · 100 = {zt(g)} {e}.', 'h': 'Rechne erst 1 % aus, dann mal 100.'}
    if st == 2:
        while True:
            p = R.choice([2, 4, 5, 8, 12, 15, 16, 24, 30, 35, 40, 45, 60, 75, 80])
            g = R.randint(2, 80) * R.choice([5, 10, 20])
            w = Fr(g * p, 100)
            if ok(w, 1): break
        e = R.choice(['€', 'kg', 'km', 'l'])
        return {'y': 'zahl', 'f': {'text': f'{pz(p)} des Grundwerts sind {zt(w)} {e}. Berechne den Grundwert.'}, 'o': {'wert': g, 'einheit': e}, 'c': f'{float(w)} / ({p} / 100)',
                'w': f'G = W : p % = {zt(w)} : {zt(Fr(p, 100))} = {zt(g)} {e}.', 'h': 'G = W : p %. Der Grundwert muss größer als W sein (wenn p < 100).'}
    art = R.randrange(3)
    if art == 0:
        p = R.choice([10, 20, 25, 30, 40, 15])
        g = R.choice([n for n in range(40, 401, 20) if n * p % 100 == 0])
        r = g * p // 100
        return {'y': 'zahl', 'f': {'text': f'Bei einem Rabatt von {pz(p)} spart man {zt(r)} €. Wie viel kostete die Ware vorher?'}, 'o': {'wert': g, 'einheit': '€'}, 'c': f'{r} / {p} * 100',
                'w': f'{pz(p)} entsprechen {zt(r)} €. 1 %: {zt(Fr(r, p))} €. 100 %: {zt(g)} €.', 'h': 'Die Ersparnis ist der Prozentwert. Gesucht ist der alte Preis (Grundwert).'}
    if art == 1:
        p = R.choice([20, 25, 40, 60, 75, 80])
        g = R.choice([n for n in range(20, 601, 20) if n * p % 100 == 0])
        w = g * p // 100
        return {'y': 'zahl', 'f': {'text': f'{w} Kinder einer Schule fahren mit dem Bus. Das sind {pz(p)} aller Kinder. Wie viele Kinder hat die Schule?'}, 'o': {'wert': g},
                'c': f'{w} / {p} * 100', 'w': f'{w} : {zt(Fr(p, 100))} = {zt(g)} Kinder.', 'h': 'Gesucht ist das Ganze, also der Grundwert.'}
    p = R.choice([110, 120, 125, 150, 200])
    g = R.choice([n for n in range(20, 401, 20)])
    w = Fr(g * p, 100)
    if not ok(w): return g_gw(3)
    return {'y': 'zahl', 'f': {'text': f'Nach einer Erhöhung beträgt ein Wert {pz(p)} des alten Werts, nämlich {zt(w)} €. Wie hoch war der alte Wert?'}, 'o': {'wert': g, 'einheit': '€'},
            'c': f'{float(w)} / {p} * 100', 'w': f'{zt(w)} : {zt(Fr(p, 100))} = {zt(g)} €.', 'h': f'{pz(p)} = {zt(Fr(p, 100))}. Teile dadurch.'}


# ---------- 5 Rabatt und Aufschlag ----------
WAREN = {'Eine Jacke': (40, 240), 'Ein Fahrrad': (200, 1000), 'Ein Paar Schuhe': (40, 160), 'Ein Rucksack': (30, 140), 'Eine Spielkonsole': (200, 600), 'Ein Zelt': (60, 400)}


def g_ra(st):
    while True:
        try:
            return _g_ra(st)
        except IndexError:
            pass


def _g_ra(st):
    ware = R.choice(list(WAREN))
    lo, hi = WAREN[ware]
    if st == 1:
        p = R.choice([10, 20, 25, 50, 30])
        g = R.choice([n for n in range(-(-lo // 10) * 10, hi + 1, 10) if n * p % 100 == 0])
        r = g * p // 100
        return {'y': 'zahl', 'f': {'text': f'{ware} kostet {zt(g)} €. Es gibt {pz(p)} Rabatt. Wie viel Euro spart man?'}, 'o': {'wert': r, 'einheit': '€'}, 'c': f'{g} * {p} / 100',
                'w': f'{pz(p)} von {zt(g)} € = {zt(r)} €.', 'h': 'Die Ersparnis ist der Prozentwert.'}
    if st == 2:
        while True:
            p = R.choice([5, 10, 15, 20, 25, 30, 35, 40])
            g = R.choice([n for n in range(-(-lo // 5) * 5, hi + 1, 5)])
            if ok(Fr(g * (100 - p), 100)): break
        if R.random() < .6:
            neu = Fr(g * (100 - p), 100)
            return {'y': 'zahl', 'f': {'text': f'{ware} kostet {zt(g)} €. Es gibt {pz(p)} Rabatt. Was kostet die Ware jetzt?'}, 'o': {'wert': wert(neu), 'einheit': '€'},
                    'c': f'{g} * (100 - {p}) / 100', 'w': f'Man zahlt {pz(100 - p)}: {zt(g)} · {zt(Fr(100 - p, 100))} = {euro(neu)}.', 'h': 'Rechne mit 100 % − Rabatt.'}
        p = R.choice([5, 10, 15, 20, 25])
        neu = Fr(g * (100 + p), 100)
        if not ok(neu): return _g_ra(2)
        return {'y': 'zahl', 'f': {'text': f'{ware} kostete {zt(g)} €. Der Preis steigt um {pz(p)}. Wie viel kostet die Ware jetzt?'}, 'o': {'wert': wert(neu), 'einheit': '€'},
                'c': f'{g} * (100 + {p}) / 100', 'w': f'Neuer Preis = {pz(100 + p)} des alten: {zt(g)} · {zt(Fr(100 + p, 100))} = {euro(neu)}.', 'h': 'Rechne mit 100 % + Aufschlag.'}
    art = R.randrange(3)
    if art == 0:
        p = R.choice([10, 20, 25, 40, 50, 30])
        g = R.choice([n for n in range(-(-lo // 20) * 20, hi + 1, 20) if n * (100 - p) % 100 == 0])
        neu = g * (100 - p) // 100
        return {'y': 'zahl', 'f': {'text': f'Nach {pz(p)} Rabatt kostet {ware[0].lower() + ware[1:]} {zt(neu)} €. Was kostete die Ware vorher?'},
                'o': {'wert': g, 'einheit': '€'}, 'c': f'{neu} / ({100 - p} / 100)',
                'w': f'{zt(neu)} € sind {pz(100 - p)} des alten Preises. 1 %: {zt(Fr(neu, 100 - p))} €, 100 %: {zt(g)} €.', 'h': 'Der neue Preis ist nicht 100 %, sondern 100 % − Rabatt.'}
    if art == 1:
        p = R.choice([10, 20, 25, 50])
        g = R.choice([n for n in range(-(-lo // 20) * 20, hi + 1, 20) if n * (100 - p) % 100 == 0])
        r = zt(Fr(g * (100 - p), 100))
        return {**wahl(R, f'{r} €', [f'{zt(g - p)} €', f'{zt(Fr(g * p, 100))} €', f'{zt(Fr(g * (100 + p), 100))} €']),
                'f': {'text': f'{ware} kostet {zt(g)} €, es gibt {pz(p)} Rabatt. Welcher neue Preis ist richtig?'},
                'w': f'{pz(100 - p)} von {zt(g)} € = {r} €. {zt(g - p)} € wäre falsch (dann hätte man {p} Euro statt {pz(p)} abgezogen).', 'h': 'Rabatt in Prozent ist nicht dasselbe wie Rabatt in Euro.'}
    a, b = R.choice([10, 20, 25]), R.choice([10, 20, 25, 30])
    g = R.choice([n for n in range(-(-lo // 100) * 100, hi + 1, 100)])
    neu = Fr(g * (100 - a) * (100 - b), 10000)
    if not ok(neu): return _g_ra(3)
    return {'y': 'zahl', 'f': {'text': f'{ware} kostet {zt(g)} €. Erst gibt es {pz(a)} Rabatt, dann auf den neuen Preis noch einmal {pz(b)}. Was kostet die Ware am Ende?'},
            'o': {'wert': wert(neu), 'einheit': '€'}, 'c': f'{g} * (100 - {a}) / 100 * (100 - {b}) / 100',
            'w': f'Nach {pz(a)}: {zt(Fr(g * (100 - a), 100))} €. Davon {pz(100 - b)}: {euro(neu)}. Das sind nicht {pz(a + b)} Rabatt insgesamt!', 'h': 'Der zweite Rabatt bezieht sich auf den schon reduzierten Preis.'}


# ---------- 6 Zinsen ----------
def g_zins(st):
    if st == 1:
        k = R.choice([100, 200, 300, 400, 500, 600, 800, 1000, 1500, 2000])
        p = R.choice([1, 2, 3, 4, 5])
        z = Fr(k * p, 100)
        return {'y': 'zahl', 'f': {'text': f'Ein Kapital von {zt(k)} € wird ein Jahr lang zu {pz(p)} angelegt. Wie viel Euro Zinsen gibt es?'}, 'o': {'wert': wert(z), 'einheit': '€'},
                'c': f'{k} * {p} / 100', 'w': f'Z = K · p % = {zt(k)} · {zt(Fr(p, 100))} = {zt(z)} €.', 'h': 'Zinsen sind der Prozentwert: Kapital mal Zinssatz.'}
    if st == 2:
        art = R.randrange(2)
        if art == 0:
            k = R.randint(4, 60) * 50
            p = R.choice([Fr(1, 2), Fr(3, 2), Fr(5, 2), 1, 2, 3, 4, Fr(7, 2)])
            z = k * Fr(p) / 100
            if not ok(z): return g_zins(2)
            return {'y': 'zahl', 'f': {'text': f'{zt(k)} € werden ein Jahr lang zu {pz(p)} angelegt. Wie hoch ist das Guthaben nach einem Jahr?'}, 'o': {'wert': wert(k + z), 'einheit': '€'},
                    'c': f'{k} + {k} * {float(p)} / 100', 'w': f'Zinsen: {zt(k)} · {zt(Fr(p) / 100)} = {zt(z)} €. Guthaben: {zt(k)} + {zt(z)} = {euro(k + z)}.', 'h': 'Erst die Zinsen ausrechnen, dann zum Kapital addieren.'}
        k = R.randint(2, 40) * 100
        p = R.choice([1, 2, 3, 4, 5, Fr(5, 2), Fr(3, 2)])
        z = k * Fr(p) / 100
        return {'y': 'zahl', 'f': {'text': f'Für {zt(k)} € zahlt eine Bank in einem Jahr {zt(z)} € Zinsen. Wie hoch ist der Zinssatz?'}, 'o': {'wert': wert(Fr(p)), 'einheit': '%'},
                'c': f'{float(z)} / {k} * 100', 'w': f'p % = Z : K = {zt(z)} : {zt(k)} = {zt(Fr(p) / 100)} = {pz(p)}.', 'h': 'Der Zinssatz ist ein Prozentsatz: Zinsen geteilt durch Kapital.'}
    art = R.randrange(3)
    if art == 0:
        k = R.randint(2, 50) * 100
        p = R.choice([1, 2, 3, 4, 5, Fr(5, 2)])
        z = k * Fr(p) / 100
        return {'y': 'zahl', 'f': {'text': f'Bei einem Zinssatz von {pz(p)} bekommt man in einem Jahr {euro(z)} Zinsen. Wie groß ist das Kapital?'}, 'o': {'wert': k, 'einheit': '€'},
                'c': f'{float(z)} / {float(p)} * 100', 'w': f'K = Z : p % = {zt(z)} : {zt(Fr(p) / 100)} = {zt(k)} €.', 'h': 'Das Kapital ist der Grundwert.'}
    if art == 1:
        k = R.randint(4, 60) * 100
        p = R.choice([2, 3, 4, 6])
        m = R.choice([3, 6, 9])
        z = Fr(k * p, 100) * Fr(m, 12)
        if not ok(z): return g_zins(3)
        return {'y': 'zahl', 'f': {'text': f'{zt(k)} € werden nur {m} Monate lang zu {pz(p)} (pro Jahr) angelegt. Wie viel Euro Zinsen gibt es?'}, 'o': {'wert': wert(z), 'einheit': '€'},
                'c': f'{k} * {p} / 100 * {m} / 12', 'w': f'Jahreszinsen: {zt(Fr(k * p, 100))} €. Für {m} von 12 Monaten: {zt(Fr(k * p, 100))} · {m}/12 = {euro(z)}.',
                'h': 'Berechne zuerst die Jahreszinsen. Dann nimm den passenden Bruchteil des Jahres.'}
    k = R.randint(2, 20) * 500
    p1, p2 = R.sample([1, 2, 3, 4, 5], 2)
    d = Fr(k * abs(p1 - p2), 100)
    return {'y': 'zahl', 'f': {'text': f'Bank A zahlt {pz(p1)}, Bank B zahlt {pz(p2)} Zinsen im Jahr. Wie viel Euro mehr Zinsen bringt die bessere Bank für {zt(k)} € in einem Jahr?'},
            'o': {'wert': wert(d), 'einheit': '€'}, 'c': f'{k} * {max(p1, p2)} / 100 - {k} * {min(p1, p2)} / 100',
            'w': f'Bank A: {zt(Fr(k * p1, 100))} €, Bank B: {zt(Fr(k * p2, 100))} €. Unterschied: {zt(d)} €.', 'h': 'Berechne die Zinsen für beide Banken und vergleiche.'}


# ---------- 7 Verstehen ----------
def g_vers(st):
    p = R.choice([10, 20, 25, 50])
    a, b = R.choice([(20, 50), (40, 25), (30, 60), (80, 50), (25, 40), (60, 15)])
    g = R.choice([40, 80, 200, 500])
    if st == 1:
        aussagen = [(f'{pz(p)} sind dasselbe wie {bruch(Fr(p, 100))}.', True, f'Ja, {p}/100 = {bruch(Fr(p, 100))}.'),
                    (f'0,{p // 10} sind {p // 10} %.' if p % 10 == 0 else '0,25 sind 2,5 %.', False, 'Nein, mal 100 ergibt die Prozentzahl: ' + (f'0,{p // 10} = {p} %.' if p % 10 == 0 else '0,25 = 25 %.')),
                    ('100 % sind das Ganze.', True, 'Ja, 100 % = 100/100 = 1 Ganzes.'),
                    (f'{pz(p)} von {g} € ist mehr als {pz(p)} von {g * 2} €.', False, f'Nein, gleicher Prozentsatz, aber kleinerer Grundwert: {zt(Fr(g * p, 100))} € < {zt(Fr(g * 2 * p, 100))} €.')]
    elif st == 2:
        aussagen = [(f'{pz(a)} von {b} ist dasselbe wie {pz(b)} von {a}.', True, f'Ja: {a}/100 · {b} = {b}/100 · {a} = {zt(Fr(a * b, 100))}.'),
                    (f'Erst {pz(p)} billiger, dann {pz(p)} teurer – dann kostet es wieder gleich viel.', False, f'Nein, Beispiel 100 €: → {100 - p} € → {zt(Fr((100 - p) * (100 + p), 100))} €.'),
                    ('Ein Prozentwert kann größer sein als der Grundwert.', True, 'Ja, wenn der Prozentsatz über 100 % liegt, z. B. 150 % von 20 = 30.'),
                    (f'{pz(p)} Rabatt auf {g} € heißt: Man zahlt {g - p} €.', False, f'Nein, man spart {zt(Fr(g * p, 100))} € und zahlt {zt(Fr(g * (100 - p), 100))} €.')]
    else:
        q = R.choice([10, 20])
        aussagen = [(f'Zweimal {pz(q)} Rabatt nacheinander ist dasselbe wie {pz(2 * q)} Rabatt.', False,
                     f'Nein, bei 100 €: → {100 - q} € → {zt(Fr((100 - q) ** 2, 100))} €. Mit {pz(2 * q)}: {100 - 2 * q} €.'),
                    (f'Steigt ein Preis von {g} € auf {g * 2} €, ist er um {pz(100)} gestiegen.', True, f'Ja, Anstieg {g} € von {g} € = 100 %.'),
                    (f'Sinkt ein Preis von {g * 2} € auf {g} €, ist er um {pz(100)} gesunken.', False, f'Nein, die Senkung ist {g} € von {g * 2} € = 50 %.'),
                    (f'Bei {pz(3)} Zinsen bekommt man für {zt(g * 10)} € in einem Jahr {zt(Fr(g * 30, 100))} € Zinsen.', True, f'Ja: {zt(g * 10)} · 0,03 = {zt(Fr(g * 30, 100))} €.')]
    s, stimmt, grund = R.choice(aussagen)
    gegen = 'Ja, die Aussage stimmt.' if not stimmt else 'Nein, die Aussage ist falsch.'
    return {**wahl(R, grund, [gegen, 'Das kann man nicht entscheiden.'], 3), 'f': {'text': f'Stimmt die Aussage? „{s}“'},
            'w': grund, 'h': 'Prüfe mit konkreten Zahlen. Achte darauf, worauf sich die Prozente beziehen.'}


GEN = {'prozent_bedeutung': g_bed, 'prozentwert': g_pw, 'prozentsatz': g_ps, 'grundwert': g_gw, 'rabatt_aufschlag': g_ra, 'zinsen': g_zins, 'verstehen': g_vers}

DATEI = datei(E, 'Prozentangaben verstehen, Prozentwert, Prozentsatz und Grundwert berechnen und einfache Aufgaben zu Rabatt, Aufschlag und Zinsen lösen.', MERKE,
              [('Grundbegriffe', ['prozent_bedeutung', 'prozentwert', 'prozentsatz', 'grundwert']),
               ('Prozente im Alltag', ['rabatt_aufschlag', 'zinsen', 'verstehen'])],
              ETAPPEN, GEN,
              offen=['Lehrplan Kl. 6 verlangt nur „einfache Prozentaufgaben (Rabatt, Zins)“; vermehrter/verminderter Grundwert rückwärts und Zinsen für Monate sind als Stufe 3 enthalten. Zinseszins bewusst weggelassen.',
                     'Prozentangaben im Text mit Leerzeichen vor % (25 %), wie in deutschen Schulbüchern üblich. Eingabe der Prozentzahl ohne %-Zeichen (Einheit „%“ ist hinterlegt).'])

if __name__ == '__main__':
    schreibe(DATEI)
