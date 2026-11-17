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

def hunderterfeld():
    """Hunderterfeld (10 × 10 Kästchen), 75 Kästchen zeilenweise von unten gefärbt – Bild der Lernkarte prozent_bedeutung."""
    b = raster(10, 10, 0)
    b['punkte'].update({'_hA': [0, 0], '_hB': [10, 0], '_hC': [10, 7], '_hD': [5, 7], '_hE': [5, 8], '_hF': [0, 8]})
    b['flaeche'] = ['_hA', '_hB', '_hC', '_hD', '_hE', '_hF']
    return b


ETAPPEN = [
    {'lernziel': 'prozent_bedeutung', 'titel': 'Was bedeutet Prozent?',
     'regel': '⟦Prozent⟧ heißt ⟦Hundertstel⟧: 1 % = 1/100 = 0,01. So wandelst du um: 35 % = 35/100 = 0,35. Umgekehrt: Dezimalzahl ⟦mal 100⟧ ergibt die Prozentzahl.',
     'schritte': ['Ein Hunderterfeld hat 100 Kästchen. Jedes Kästchen ist 1 %.', '3/4 in Prozent: Erweitere auf Hundertstel, 3/4 = 75/100.',
                  'Im Feld sind 75 von 100 Kästchen gefärbt: ⟦75 %⟧ = 0,75.'],
     'bild': hunderterfeld(),
     'fehler': '0,5 = 5 % ist falsch: 0,5 = 50/100 = ⟦50 %⟧. Beim Umwandeln wandert das Komma ⟦zwei⟧ Stellen.'},
    {'lernziel': 'prozentwert', 'titel': 'Prozentwert berechnen',
     'regel': 'Der ⟦Grundwert G⟧ ist das Ganze (100 %). Der ⟦Prozentwert W⟧ ist der Teil davon. Es gilt ⟦W = G · p %⟧. Tipp: Rechne zuerst 1 % aus (G : 100).',
     'schritte': ['15 % von 240 €: 1 % von 240 € sind 240 € : 100 = 2,40 €.', '15 % sind 15 · 2,40 € = ⟦36 €⟧.',
                  'Schneller im Kopf: 10 % sind 24 €, 5 % sind die Hälfte davon, 12 €. Zusammen 24 € + 12 € = 36 €.'],
     'probe': '36 : 240 = 0,15 = 15 % ✓',
     'fehler': '15 % von 240 € als 240 : 15 = 16 € zu rechnen ist falsch: 15 % heißt ⟦15 Hundertstel⟧. Also 240 · 15 : 100 = 36 €.'},
    {'lernziel': 'prozentsatz', 'titel': 'Prozentsatz berechnen',
     'regel': 'Den ⟦Prozentsatz⟧ findest du mit ⟦p % = W : G⟧ – Teil durch Ganzes. Das Ergebnis als Dezimalzahl mal 100 ergibt die Prozentzahl.',
     'schritte': ['Von 25 Aufgaben sind 21 richtig. 21 : 25 = 0,84.', '0,84 = ⟦84 %⟧.'],
     'probe': 'Ohne Division: 21/25 mit 4 erweitern ergibt 84/100 = 84 % ✓',
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
def g_bed_bild(st):
    """Prozentsatz am Bild ablesen: Hunderterfeld (Stufe 1) oder Kreis (Stufe 2)."""
    if st == 1:
        k = R.randint(3, 97)
        return {'y': 'zahl', 'f': {'text': 'Das Hunderterfeld hat 100 Kästchen. Wie viel Prozent sind gefärbt?',
                                   'grafik': raster(10, 10, k, label=f'Hunderterfeld, {k} von 100 Kästchen gefärbt')},
                'o': {'wert': k, 'einheit': '%'}, 'c': f'{k} / 100 * 100',
                'w': f'Volle Spalten zählen (je 10 Kästchen), dann den Rest: {k} von 100 Kästchen = {k}/100 = {k} %.',
                'h': 'Jede volle Spalte hat 10 Kästchen. Jedes Kästchen ist 1 %.'}
    if R.random() < .5:
        a, b, welcher = R.choice([(1, 3, 'kleinere'), (1, 3, 'größere'), (3, 1, 'kleinere'), (3, 1, 'größere'), (1, 1, 'blaue')])
        g = (min(a, b) if welcher == 'kleinere' else max(a, b)) if a != b else a
        p = Fr(g * 100, a + b)
        werte = [('blau', a), ('weiß', b)]
        wort = {Fr(1, 4): 'ein Viertel', Fr(3, 4): 'drei Viertel', Fr(1, 2): 'die Hälfte'}[Fr(g, a + b)]
        return {'y': 'zahl', 'f': {'text': f'Wie viel Prozent des Kreises macht der {welcher} Teil aus?' if a != b else 'Wie viel Prozent des Kreises sind blau?',
                                   'grafik': kreisdiagramm(werte, zahlen=False)},
                'o': {'wert': wert(p), 'einheit': '%'}, 'c': f'{g} / {a + b} * 100',
                'w': f'Der Teil ist {wort} des Kreises: {bruch(Fr(g, a + b))} = {pz(p)}.', 'h': 'Ein halber Kreis ist 50 %, ein Viertelkreis 25 %.'}
    n = R.choice([4, 5, 10, 20])
    k = R.randint(1, n - 1)
    p = Fr(k * 100, n)
    return {'y': 'zahl', 'f': {'text': f'Der Kreis ist in {n} gleich große Teile geteilt. Wie viel Prozent sind gefärbt?',
                               'grafik': kreisteile(n, k, label=f'Kreis: {n} gleich große Teile, {k} davon gefärbt')},
            'o': {'wert': wert(p), 'einheit': '%'}, 'c': f'{k} / {n} * 100',
            'w': f'{k} von {n} Teilen: {k}/{n} = {k * (100 // n)}/100 = {pz(p)}.', 'h': f'Ein Teil ist 100 % : {n} = {zt(Fr(100, n))} %.'}


def g_bed(st):
    if st in (1, 2) and R.random() < .3:
        return g_bed_bild(st)
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
        w_ = (f'1 % ist der hundertste Teil: {zt(g)} {e} : 100 = {zt(w)} {e}.' if p == 1 else
              f'1 % von {zt(g)} {e} = {zt(g)} {e} : 100 = {zt(Fr(g, 100))} {e}. {pz(p)}: {p} · {zt(Fr(g, 100))} = {zt(w)} {e}.')
        if p in (10, 5) and R.random() < .5:
            w_ = f'10 % von {zt(g)} {e}: Komma eine Stelle nach links, {zt(Fr(g, 10))} {e}.' + (f' 5 % sind die Hälfte davon: {zt(w)} {e}.' if p == 5 else '')
        return {'y': 'zahl', 'f': {'text': f'Berechne {pz(p)} von {zt(g)} {e}.'}, 'o': {'wert': wert(w), 'einheit': e}, 'c': f'{g} * {p} / 100',
                'w': w_, 'h': 'Rechne erst 1 % aus, dann mal die Prozentzahl.'}
    if st == 2:
        while True:
            p = R.randint(2, 95)
            g = R.randint(2, 99) * R.choice([5, 10, 20, 50])
            w = Fr(g * p, 100)
            if ok(w): break
        e = R.choice(['€', 'kg', 'km', 'l'])
        return {'y': 'zahl', 'f': {'text': f'Berechne {pz(p)} von {zt(g)} {e}.'}, 'o': {'wert': wert(w), 'einheit': e}, 'c': f'{g} * {p} / 100',
                'w': f'W = G · p % = {zt(g)} · {zt(Fr(p, 100))} = {zt(w)} {e}.', 'h': 'Schreibe p % als Dezimalzahl und nimm mit dem Grundwert mal.'}
    art = R.randrange(4)
    if art == 3:
        return schaetzen()
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


def schaetzen():
    """Prozentwert überschlagen: krummer Prozentsatz und krummer Grundwert auf runde Zahlen."""
    p0, b = R.choice([(25, Fr(1, 4)), (50, Fr(1, 2)), (20, Fr(1, 5)), (10, Fr(1, 10)), (75, Fr(3, 4))])
    p = p0 + R.choice([-2, -1, 1, 2])
    g0 = R.choice([40, 60, 80, 120, 200, 300, 400, 600, 800, 1000])
    g = g0 + R.choice([-3, -2, -1, 1, 2, 3]) * (1 if g0 < 100 else R.choice([1, 2]))
    e = R.choice(['€', 'kg'])
    r = g0 * b
    if r.denominator > 1: return schaetzen()
    falsch = [f'etwa {zt(p)} {e}', f'etwa {zt(r / 10)} {e}' if (r / 10).denominator == 1 else f'etwa {zt(r * 2)} {e}', f'etwa {zt(r * 10)} {e}']
    return {**wahl(R, f'etwa {zt(r)} {e}', falsch), 'f': {'text': f'Etwa wie viel sind {pz(p)} von {zt(g)} {e}? Überschlage im Kopf.'},
            'w': f'{pz(p)} ≈ {pz(p0)} = {bruch(b)}, {zt(g)} {e} ≈ {zt(g0)} {e}. {bruch(b)} von {zt(g0)} {e} = {zt(r)} {e}.',
            'h': f'Runde {pz(p)} auf einen einfachen Prozentsatz und {zt(g)} auf eine runde Zahl.'}


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
        # (Satz, Frage, kleinstes/größtes Ganzes, Anteil von/bis in %)
        lage = R.choice([('In einer Klasse mit {g} Kindern tragen {w} eine Brille.', 'Wie viel Prozent der Kinder sind das?', 20, 32, 15, 50),
                         ('Von {g} Freiwürfen trifft ein Kind {w}.', 'Wie hoch ist die Trefferquote in Prozent?', 10, 50, 30, 90),
                         ('Bei einer Klassenarbeit gibt es {g} Punkte. Ein Kind erreicht {w} Punkte.', 'Wie viel Prozent der Punkte sind das?', 20, 60, 40, 100),
                         ('Von {g} gesäten Samen keimen {w}.', 'Wie viel Prozent der Samen keimen?', 20, 200, 50, 95),
                         ('Ein Verein hat {g} Mitglieder. {w} davon sind Kinder.', 'Wie viel Prozent der Mitglieder sind Kinder?', 40, 400, 10, 60)])
        satz, frage, glo, ghi, plo, phi = lage
        while True:
            g = R.randint(glo, ghi)
            w = R.randint(max(1, g * plo // 100), min(g - (phi < 100), g * phi // 100))
            p = Fr(w * 100, g)
            if ok(p, 1) and 0 < w: break
        return {'y': 'zahl', 'f': {'text': satz.format(g=zt(g), w=zt(w)) + ' ' + frage}, 'o': {'wert': wert(p), 'einheit': '%'}, 'c': f'{w} / {g} * 100',
                'w': f'Teil durch Ganzes: {zt(w)} : {zt(g)} = {zt(Fr(w, g))} = {pz(p)}.' + (f' Oder erweitern: {w}/{g} = {zt(p)}/100.' if 100 % g == 0 else ''),
                'h': 'Was ist das Ganze (Grundwert), was ist der Teil? p % = W : G.'}
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
    # Der bekannte Teil ist der Rest: erst dessen Prozentsatz bestimmen (100 % − p %), dann rückwärts.
    p = R.choice([10, 20, 25, 30, 40, 45, 60, 75])
    g = R.choice([n for n in range(100, 801, 20) if n * (100 - p) % 100 == 0])
    rest = g * (100 - p) // 100
    return {'y': 'zahl', 'f': {'text': f'{pz(p)} der Kinder einer Schule kommen mit dem Bus. Die übrigen {zt(rest)} Kinder kommen zu Fuß oder mit dem Rad. Wie viele Kinder hat die Schule?'},
            'o': {'wert': g}, 'c': f'{rest} / (100 - {p}) * 100',
            'w': f'Die übrigen Kinder sind 100 % − {pz(p)} = {pz(100 - p)}. 1 %: {zt(rest)} : {100 - p} = {zt(Fr(rest, 100 - p))}. 100 %: {zt(g)} Kinder.',
            'h': f'Zu welchem Prozentsatz gehören die {zt(rest)} Kinder? Es sind nicht {pz(p)}.'}


# ---------- 5 Rabatt und Aufschlag ----------
WAREN = {'Eine Jacke': (40, 240), 'Ein Fahrrad': (200, 1000), 'Ein Paar Schuhe': (40, 160), 'Ein Rucksack': (30, 140), 'Eine Spielkonsole': (200, 600), 'Ein Zelt': (60, 400)}
DER = {'Eine Jacke': 'die Jacke', 'Ein Fahrrad': 'das Fahrrad', 'Ein Paar Schuhe': 'das Paar Schuhe', 'Ein Rucksack': 'der Rucksack',
       'Eine Spielkonsole': 'die Spielkonsole', 'Ein Zelt': 'das Zelt'}


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
            return {'y': 'zahl', 'f': {'text': f'{ware} kostet {zt(g)} €. Es gibt {pz(p)} Rabatt. Was kostet {DER[ware]} jetzt?'}, 'o': {'wert': wert(neu), 'einheit': '€'},
                    'c': f'{g} * (100 - {p}) / 100', 'w': f'Man zahlt {pz(100 - p)}: {zt(g)} · {zt(Fr(100 - p, 100))} = {euro(neu)}.', 'h': 'Rechne mit 100 % − Rabatt.'}
        p = R.choice([5, 10, 15, 20, 25])
        neu = Fr(g * (100 + p), 100)
        if not ok(neu): return _g_ra(2)
        return {'y': 'zahl', 'f': {'text': f'{ware} kostete {zt(g)} €. Der Preis steigt um {pz(p)}. Wie viel kostet {DER[ware]} jetzt?'}, 'o': {'wert': wert(neu), 'einheit': '€'},
                'c': f'{g} * (100 + {p}) / 100', 'w': f'Neuer Preis = {pz(100 + p)} des alten: {zt(g)} · {zt(Fr(100 + p, 100))} = {euro(neu)}.', 'h': 'Rechne mit 100 % + Aufschlag.'}
    art = R.randrange(3)
    if art == 0:
        return angebote()
    if art == 1:
        p = R.choice([10, 20, 25, 50])
        g = R.choice([n for n in range(-(-lo // 20) * 20, hi + 1, 20) if n * (100 - p) % 100 == 0])
        r = zt(Fr(g * (100 - p), 100))
        return {**wahl(R, f'{r} €', [f'{zt(g - p)} €', f'{zt(Fr(g * p, 100))} €', f'{zt(Fr(g * (100 + p), 100))} €']),
                'f': {'text': f'{ware} kostet {zt(g)} €, es gibt {pz(p)} Rabatt. Welcher neue Preis ist richtig?'},
                'w': f'{pz(100 - p)} von {zt(g)} € = {r} €. {zt(g - p)} € wäre falsch (dann hätte man {p} Euro statt {pz(p)} abgezogen).', 'h': 'Rabatt in Prozent ist nicht dasselbe wie Rabatt in Euro.'}
    # Gutschein: p % Rabatt oder fester Betrag – was spart mehr?
    p = R.choice([10, 15, 20, 25])
    g = R.choice([n for n in range(-(-lo // 10) * 10, hi + 1, 10) if n * p % 100 == 0])
    ersp = g * p // 100
    fest = ersp + R.choice([-5, -3, -2, 2, 3, 5])
    if fest <= 0 or fest == ersp: return _g_ra(3)
    besser = f'der {pz(p)}-Gutschein ({zt(ersp)} € gespart)' if ersp > fest else f'der {zt(fest)}-€-Gutschein ({zt(ersp)} € bei {pz(p)})'
    r = 'Der Prozent-Gutschein' if ersp > fest else 'Der Euro-Gutschein'
    falsch = ['Der Euro-Gutschein' if ersp > fest else 'Der Prozent-Gutschein', 'Beide sparen gleich viel']
    return {**wahl(R, r, falsch, 3), 'f': {'text': f'{ware} kostet {zt(g)} €. Du darfst einen Gutschein einlösen: {pz(p)} Rabatt oder {zt(fest)} € Rabatt. Welcher spart mehr?'},
            'w': f'{pz(p)} von {zt(g)} € = {zt(ersp)} €. Der andere Gutschein spart {zt(fest)} €. Besser ist {besser}.',
            'h': 'Rechne den Prozent-Rabatt in Euro um und vergleiche.'}


def angebote():
    """Zwei Läden: verschiedener Preis und verschiedener Rabatt – wo ist es billiger?"""
    ware = R.choice(list(WAREN))
    lo, hi = WAREN[ware]
    pa, pb = R.sample([10, 20, 25, 30, 40, 50], 2)
    ga = R.choice([n for n in range(-(-lo // 10) * 10, hi + 1, 10) if n * (100 - pa) % 100 == 0])
    gb_ = [n for n in range(-(-lo // 5) * 5, hi + 1, 5) if n * (100 - pb) % 100 == 0 and n != ga and abs(n * (100 - pb) - ga * (100 - pa)) <= 15 * 100 and n * (100 - pb) != ga * (100 - pa)]
    if not gb_: return angebote()
    gb = R.choice(gb_)
    na, nb = Fr(ga * (100 - pa), 100), Fr(gb * (100 - pb), 100)
    if (ga < gb) == (na < nb): return angebote()     # nur Fälle, in denen der kleinere Ausgangspreis nicht billiger ist
    bill, teu = ('A', 'B') if na < nb else ('B', 'A')
    r = f'Laden {bill} ({euro(min(na, nb))} gegen {euro(max(na, nb))})'
    klein = 'A' if ga < gb else 'B'
    mehr = 'A' if pa > pb else 'B'
    falsch = [f'Laden {klein}, weil der Preis kleiner ist', 'Beide sind gleich teuer', f'Laden {teu} ({euro(max(na, nb))} gegen {euro(min(na, nb))})']
    if mehr != bill: falsch.insert(1, f'Laden {mehr}, weil der Rabatt größer ist')
    return {**wahl(R, r, falsch), 'f': {'text': f'Laden A: {DER[ware][0].upper() + DER[ware][1:]} kostet {zt(ga)} € mit {pz(pa)} Rabatt. Laden B: Sie kostet {zt(gb)} € mit {pz(pb)} Rabatt. Wo ist sie billiger?'
                                         .replace('Sie kostet', 'Es kostet' if DER[ware].startswith('das') else 'Er kostet' if DER[ware].startswith('der') else 'Sie kostet')
                                         .replace('Wo ist sie billiger', 'Wo ist es billiger' if DER[ware].startswith('das') else 'Wo ist er billiger' if DER[ware].startswith('der') else 'Wo ist sie billiger')},
            'w': f'A: {pz(100 - pa)} von {zt(ga)} € = {euro(na)}. B: {pz(100 - pb)} von {zt(gb)} € = {euro(nb)}. Billiger ist Laden {bill}.',
            'h': 'Berechne in beiden Läden den Preis nach dem Rabatt.'}


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
    """Aussage beurteilen. Je Aussage: richtiger Grund und ein typischer Fehlgrund (statt „kann man nicht entscheiden“)."""
    p = R.choice([10, 20, 25, 50])
    a, b = R.choice([(20, 50), (40, 25), (30, 60), (80, 50), (25, 40), (60, 15)])
    g = R.choice([40, 80, 200, 500])
    if st == 1:
        aussagen = [(f'{pz(p)} sind dasselbe wie {bruch(Fr(p, 100))}.', True, f'Ja, {p}/100 = {bruch(Fr(p, 100))}.',
                     f'Nein, {pz(p)} sind {p}/10.'),
                    (f'0,{p // 10} sind {p // 10} %.' if p % 10 == 0 else '0,25 sind 2,5 %.', False, 'Nein, mal 100 ergibt die Prozentzahl: ' + (f'0,{p // 10} = {p} %.' if p % 10 == 0 else '0,25 = 25 %.'),
                     'Ja, man lässt einfach die Null vor dem Komma weg.'),
                    ('100 % sind das Ganze.', True, 'Ja, 100 % = 100/100 = 1 Ganzes.', 'Nein, das Ganze sind 1 %.'),
                    (f'{pz(p)} von {g} € ist mehr als {pz(p)} von {g * 2} €.', False, f'Nein, gleicher Prozentsatz, aber kleinerer Grundwert: {zt(Fr(g * p, 100))} € < {zt(Fr(g * 2 * p, 100))} €.',
                     f'Ja, weil {g} € weniger Geld ist und man davon mehr Prozent bekommt.')]
    elif st == 2:
        aussagen = [(f'{pz(a)} von {b} ist dasselbe wie {pz(b)} von {a}.', True, f'Ja: {a}/100 · {b} = {b}/100 · {a} = {zt(Fr(a * b, 100))}.',
                     f'Nein, weil {pz(max(a, b))} mehr ist als {pz(min(a, b))}.'),
                    (f'Erst {pz(p)} billiger, dann {pz(p)} teurer – dann kostet es wieder gleich viel.', False, f'Nein, Beispiel 100 €: → {100 - p} € → {zt(Fr((100 - p) * (100 + p), 100))} €.',
                     f'Ja, weil − {pz(p)} und + {pz(p)} zusammen 0 % ergeben.'),
                    ('Ein Prozentwert kann größer sein als der Grundwert.', True, 'Ja, wenn der Prozentsatz über 100 % liegt, z. B. 150 % von 20 = 30.',
                     'Nein, ein Teil kann nie größer sein als das Ganze.'),
                    (f'{pz(p)} Rabatt auf {g} € heißt: Man zahlt {g - p} €.', False, f'Nein, man spart {zt(Fr(g * p, 100))} € und zahlt {zt(Fr(g * (100 - p), 100))} €.',
                     f'Ja, {pz(p)} Rabatt heißt {p} € weniger.')]
    else:
        q = R.choice([10, 20])
        aussagen = [(f'Zweimal {pz(q)} Rabatt nacheinander ist dasselbe wie {pz(2 * q)} Rabatt.', False,
                     f'Nein, bei 100 €: → {100 - q} € → {zt(Fr((100 - q) ** 2, 100))} €. Mit {pz(2 * q)}: {100 - 2 * q} €.',
                     f'Ja, weil {pz(q)} + {pz(q)} = {pz(2 * q)}.'),
                    (f'Steigt ein Preis von {g} € auf {g * 2} €, ist er um {pz(100)} gestiegen.', True, f'Ja, Anstieg {g} € von {g} € = 100 %.',
                     f'Nein, er ist um {pz(200)} gestiegen, weil er jetzt doppelt so hoch ist.'),
                    (f'Sinkt ein Preis von {g * 2} € auf {g} €, ist er um {pz(100)} gesunken.', False, f'Nein, die Senkung ist {g} € von {g * 2} € = 50 %.',
                     'Ja, weil Verdoppeln + 100 % ist, ist Halbieren − 100 %.'),
                    (f'Bei {pz(3)} Zinsen bekommt man für {zt(g * 10)} € in einem Jahr {zt(Fr(g * 30, 100))} € Zinsen.', True, f'Ja: {zt(g * 10)} · 0,03 = {zt(Fr(g * 30, 100))} €.',
                     f'Nein, bei {pz(3)} bekommt man 3 € Zinsen.')]
    s, stimmt, grund, fehlgrund = R.choice(aussagen)
    gegen = 'Ja, die Aussage stimmt.' if not stimmt else 'Nein, die Aussage ist falsch.'
    return {**wahl(R, grund, [fehlgrund, gegen], 3), 'f': {'text': f'Stimmt die Aussage? „{s}“'},
            'w': grund, 'h': 'Prüfe mit konkreten Zahlen. Achte darauf, worauf sich die Prozente beziehen.'}


GEN = {'prozent_bedeutung': g_bed, 'prozentwert': g_pw, 'prozentsatz': g_ps, 'grundwert': g_gw, 'rabatt_aufschlag': g_ra, 'zinsen': g_zins, 'verstehen': g_vers}

DATEI = datei(E, 'Prozentangaben verstehen, Prozentwert, Prozentsatz und Grundwert berechnen und einfache Aufgaben zu Rabatt, Aufschlag und Zinsen lösen.', MERKE,
              [('Grundbegriffe', ['prozent_bedeutung', 'prozentwert', 'prozentsatz', 'grundwert']),
               ('Prozente im Alltag', ['rabatt_aufschlag', 'zinsen', 'verstehen'])],
              ETAPPEN, GEN,
              offen=['Lehrplan Kl. 6 verlangt nur „einfache Prozentaufgaben (Rabatt, Zins)“. Nach der Prüfung entfernt: vermehrter/verminderter Grundwert rückwärts (Preis nach Rabatt → alter Preis, 200 % des alten Werts) und Doppelrabatt als Rechenaufgabe – das ist Stoff von bruch.prozent_grundwert (Kl. 7). Doppelrabatt bleibt nur als Verstehens-Aussage („zweimal 10 % ≠ 20 %“). Zinsen für Monate bleiben als Stufe 3, Zinseszins weggelassen.',
                     'Prozentangaben im Text mit Leerzeichen vor % (25 %), wie in deutschen Schulbüchern üblich. Eingabe der Prozentzahl ohne %-Zeichen (Einheit „%“ ist hinterlegt).'])

# ---------- KARTEN: Lernkarten nach dem neuen Muster (Achte Runde, Vorgabe 16.11., Paket U6) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl6.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl6 import umbau  # noqa: E402

KARTEN = {
 'prozent_bedeutung': {
  'einstieg': 'Dein Handy-Akku zeigt 75 %. Denk dir den vollen Akku in 100 gleiche Teile geteilt: 75 sind noch voll. ⟦Prozent⟧ heißt „von hundert“.',
  'woerter': [['Prozent', 'Hundertstel: 75 % = 75/100'],
              ['erweitern', 'Zähler und Nenner mit derselben Zahl malnehmen']],
  'bild': {'typ': 'bruchstreifen', 'teile': 4, 'gefaerbt': 3, 'teil_text': '3/4'},
  'schritte': [{'text': 'Der Akku ist zu 3/4 voll. Prozent braucht den Nenner 100.'},
               {'text': 'Mit 25 erweitern, denn 4 · 25 = 100: 3/4 = 75/100.',
                'bild': {'zeilen': [{'teile': 100, 'gefaerbt': 75, 'teil_text': '75/100'}]}},
               {'text': '75 Hundertstel sind ⟦75 %⟧, also 0,75.'}],
  'fehler': '0,5 = 5 % ist falsch: Ein halb voller Akku zeigt 50 %. Beim Umwandeln wandert das Komma zwei Stellen.',
  'fehler_bild': {'teile': 2, 'gefaerbt': 1, 'teil_text': '0,5 = 50 %', 'zeilen': [{'teile': 100, 'gefaerbt': 5, 'teil_text': '5 %'}]},
  'regel': '⟦Prozent heißt Hundertstel⟧: 35 % = 35/100 = 0,35. Eine Dezimalzahl mal 100 ergibt die Prozentzahl.'},
 'prozentwert': {
  'einstieg': 'Ein Fahrrad kostet 240 €, der Laden will 15 % als Anzahlung. Wie viel Euro sind das? Das ist der ⟦Prozentwert⟧.',
  'woerter': [['Grundwert', 'das Ganze, hier der Preis 240 €'],
              ['Prozentwert', 'der Teil in Euro, hier die Anzahlung'],
              ['Prozentsatz', 'der Anteil in Prozent, hier 15 %']],
  'bild': {'typ': 'bruchstreifen', 'teile': 20, 'gefaerbt': 0, 'ganzes': '240 € = 100 %'},
  'schritte': [{'text': 'Der Grundwert ist 240 €, der Prozentsatz ist 15 %.'},
               {'text': '1 % sind 240 € : 100 = 2,40 €.'},
               {'text': '15 % sind 15 · 2,40 € = ⟦36 €⟧.', 'bild': {'gefaerbt': 3, 'teil_text': '15 % = 36 €'}}],
  'fehler': '240 : 15 = 16 € ist falsch. Das wäre ein Fünfzehntel, nicht 15 Hundertstel.',
  'regel': 'Erst ⟦1 %⟧ ausrechnen, dann mal die Prozentzahl. Kurz: W = G · p %.'},
 'prozentsatz': {
  'einstieg': 'Du hast 21 von 25 Aufgaben richtig, deine Freundin 34 von 40. Wer war besser? Mit dem ⟦Prozentsatz⟧ kannst du es vergleichen.',
  'woerter': [['Prozentsatz', 'der Anteil in Prozent'],
              ['Teil durch Ganzes', 'so rechnest du einen Anteil aus']],
  'bild': {'typ': 'bruchstreifen', 'teile': 25, 'gefaerbt': 21, 'teil_text': '21 von 25', 'zeilen': [{'teile': 40, 'gefaerbt': 34, 'teil_text': '34 von 40'}]},
  'schritte': [{'text': 'Rechne Teil durch Ganzes: 21 : 25 = 0,84.'},
               {'text': 'Mal 100 ergibt die Prozentzahl: ⟦84 %⟧.'},
               {'text': 'Deine Freundin: 34 : 40 = 0,85, also ⟦85 %⟧. Sie war knapp besser.',
                'bild': {'typ': 'saeulen', 'einheit': '%', 'werte': [{'name': 'du', 'wert': 84}, {'name': 'Freundin', 'wert': 85}], 'zahlen': True}}],
  'fehler': '25 : 21 ergibt etwa 119 %. Das wären mehr richtige Aufgaben, als es überhaupt gibt.',
  'regel': 'Prozentsatz ist ⟦Teil durch Ganzes⟧, mal 100. So vergleichst du Ergebnisse mit verschiedenen Ganzen.'},
 'grundwert': {
  'einstieg': 'Ihr habt 12 kg Kartoffeln geerntet. Das sind erst 30 % der ganzen Ernte. Wie schwer wird die ganze Ernte, der ⟦Grundwert⟧?',
  'woerter': [['Grundwert', 'das Ganze, also 100 %']],
  'bild': {'typ': 'bruchstreifen', 'teile': 10, 'gefaerbt': 3, 'teil_text': '30 % = 12 kg', 'ganzes': '100 % = ? kg'},
  'schritte': [{'text': '30 % sind 3 von 10 Teilen, zusammen 12 kg.'},
               {'text': 'Ein Teil, also 10 %, sind 12 kg : 3 = 4 kg.', 'bild': {'gefaerbt': 1, 'teil_text': '10 % = 4 kg'}},
               {'text': '100 % sind 10-mal so viel: ⟦40 kg⟧.', 'bild': {'gefaerbt': 10, 'teil_text': '', 'ganzes': '100 % = 40 kg'}}],
  'fehler': '12 kg · 0,3 = 3,6 kg ist falsch. Das ist weniger, als schon geerntet ist. Das Ganze muss größer sein.',
  'regel': 'Rechne vom Teil über ⟦1 %⟧ auf 100 %. Kurz: G = W : p %.'},
 'rabatt_aufschlag': {
  'einstieg': 'Eine Jacke kostet 80 €. Im Schlussverkauf gibt es 25 % ⟦Rabatt⟧. Du zahlst nur den Teil, der übrig bleibt.',
  'woerter': [['Rabatt', 'ein Preisnachlass in Prozent'],
              ['Aufschlag', 'eine Preiserhöhung in Prozent']],
  'bild': {'typ': 'bruchstreifen', 'teile': 4, 'gefaerbt': 4, 'ganzes': '80 € = 100 %'},
  'schritte': [{'text': '25 % Rabatt heißt: Du zahlst noch 100 % − 25 % = 75 %.', 'bild': {'gefaerbt': 3, 'teil_text': '75 %'}},
               {'text': '75 % von 80 € sind 0,80 € · 75 = ⟦60 €⟧.', 'bild': {'teil_text': '75 % = 60 €'}},
               {'text': 'Bei 25 % Aufschlag zahlst du dagegen 125 %, also 100 €.'}],
  'fehler': '80 € − 25 € = 55 € ist falsch. Auf dem Schild stehen 25 Prozent, nicht 25 Euro.',
  'regel': 'Bei Rabatt zahlst du ⟦100 % − p %⟧. Bei Aufschlag zahlst du 100 % + p %. Der alte Preis ist der Grundwert.'},
 'zinsen': {
  'einstieg': 'Du bringst 500 € zur Bank und lässt sie ein Jahr dort. Dafür bekommst du 3 % dazu. Dieses Geld heißt ⟦Zinsen⟧.',
  'woerter': [['Zinsen', 'Geld, das die Bank dir für dein Erspartes zahlt'],
              ['Kapital', 'das Geld, das auf der Bank liegt'],
              ['Zinssatz', 'wie viel Prozent Zinsen es im Jahr gibt']],
  'bild': {'typ': 'saeulen', 'einheit': '€', 'werte': [{'name': 'Start', 'wert': 500}], 'zahlen': True},
  'schritte': [{'text': 'Das Kapital ist 500 €, der Zinssatz 3 %.'},
               {'text': '1 % sind 5 €, also sind 3 % ⟦15 €⟧ Zinsen.'},
               {'text': 'Nach einem Jahr hast du 500 € + 15 € = ⟦515 €⟧.',
                'bild': {'werte': [{'name': 'Start', 'wert': 500}, {'name': '1 Jahr', 'wert': 515}]}}],
  'fehler': 'Nur 3 € Zinsen zu erwarten ist falsch. 3 % heißt: 3 € für je 100 €. Bei 500 € sind das 15 €.',
  'regel': 'Zinsen sind der ⟦Prozentwert⟧ vom Kapital. Das neue Guthaben ist Kapital plus Zinsen.'},
 'verstehen': {
  'einstieg': 'Ein Spiel für 100 € wird erst 10 % billiger, dann 10 % teurer. Kostet es wieder 100 €? Frag immer nach dem ⟦Grundwert⟧: Prozent wovon?',
  'woerter': [['Grundwert', 'das Ganze, von dem die Prozente berechnet werden']],
  'bild': {'typ': 'saeulen', 'einheit': '€', 'werte': [{'name': 'Start', 'wert': 100}], 'zahlen': True},
  'schritte': [{'text': '10 % von 100 € sind 10 €. Das Spiel kostet 90 €.',
                'bild': {'werte': [{'name': 'Start', 'wert': 100}, {'name': '−10 %', 'wert': 90}]}},
               {'text': 'Jetzt ist 90 € der Grundwert. 10 % davon sind nur 9 €.'},
               {'text': 'Das Spiel kostet ⟦99 €⟧, nicht 100 €.',
                'bild': {'werte': [{'name': 'Start', 'wert': 100}, {'name': '−10 %', 'wert': 90}, {'name': '+10 %', 'wert': 99}]}}],
  'fehler': '−10 % und +10 % heben sich nicht auf. Die zweiten 10 % gehören zu einem anderen Grundwert.',
  'regel': 'Frag immer: ⟦Prozent wovon?⟧ Rechne mit Zahlen nach, am besten mit 100.'},
}

umbau(DATEI, KARTEN)



# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl6): je Lernkarte 2 Übungen Stufe 2 + 4 Übungen Stufe 3 ----------
# Läuft nach allen bisherigen Aufgaben mit eigenem Zufallsstart; die bisherigen Aufgaben bleiben unverändert.
# Prüfungsvorbilder: Bayerischer Mathematik-Test Jgst. 8 (ISB) 2021 Aufg. 5 („20 % weniger als“ – Grundwert erkennen),
# 2021 Aufg. 6c (Prozentpunkte statt Prozent), 2014 Gruppe B Aufg. 1c (Prozent vom Prozent), 2023 Aufg. 5a (Restanteil aus Prozent und Bruch),
# 2023 Aufg. 6 (99 % entfernt – 1 % bleibt), 2024 Aufg. 3a–c (Anteile ergänzen sich zu 100 %, „ein Drittel“ genau prüfen, Gesamtzahl aus
# Anzahl und Prozentsatz), 2025 Aufg. 6b/6d (Veränderung in beide Richtungen; gleicher Prozentsatz bei verschiedener Gesamtzahl);
# IQB VERA-8 (Aufgabe „Zwanzig Prozent“, Didaktische Handreichung).
from _basis import tabelle  # noqa: E402
from _schwer_kl6 import ergaenzen, zahl, wahl  # noqa: E402

_PW = 'Frag dich: Prozent wovon? Das ist der Grundwert.'


def _pz():
    return {
        'prozent_bedeutung': [
            (2, lambda R: wahl(R, 'Welche Angabe ist am größten: 0,35; 3/8; 36 % oder 7/20?', '3/8', ['0,35', '36 %', '7/20'],
                               'Schreibe alle Angaben in Prozent.', '0,35 = 35 %; 3/8 = 0,375 = 37,5 %; 36 %; 7/20 = 35/100 = 35 %. Am größten: 3/8.')),
            (2, lambda R: zahl('Wie viel Prozent sind 7/25?', 28, '7 / 25 * 100', 'Erweitere auf den Nenner 100.', '7/25 = 28/100 = 28 %.', einheit='%')),
            (3, lambda R: zahl('Ein Kind gibt 45 % seines Taschengelds für Süßes aus und spart 1/4. Der Rest ist für Bücher. Wie viel Prozent sind für Bücher?', 30,
                               '100 - 45 - 100 / 4', 'Schreibe 1/4 in Prozent. Alles zusammen sind 100 %.', '1/4 = 25 %. 100 % − 45 % − 25 % = 30 %.', einheit='%')),
            (3, lambda R: zahl('Die Tabelle zeigt, wie die Kinder einer Schule zur Schule kommen. Ein Wert fehlt. Wie viel Prozent kommen zu Fuß?', 30,
                               '100 - 35 - 100 / 5 - 0.15 * 100', 'Rechne alle Angaben in Prozent um. Zusammen müssen es 100 % sein.',
                               'Rad 1/5 = 20 %, Auto 0,15 = 15 %. 100 % − 35 % − 20 % − 15 % = 30 %.', einheit='%',
                               grafik=tabelle(['Weg', 'Bus', 'Rad', 'Auto', 'zu Fuß'], [['Anteil', '35 %', '1/5', '0,15', '?']]))),
            (3, lambda R: zahl('Die Recyclingquote einer Stadt steigt von 40 % auf 50 %. Um wie viele Prozentpunkte ist sie gestiegen?', 10, '50 - 40',
                               'Prozentpunkte sind der Unterschied zwischen zwei Prozentangaben.', '50 % − 40 % = 10 Prozentpunkte.', einheit='Prozentpunkte')),
            (3, lambda R: zahl('Wie viel Prozent sind 1 1/4?', 125, '(1 + 1/4) * 100', 'Ein Ganzes sind 100 %. Wie viel Prozent ist 1/4?',
                               '1 = 100 % und 1/4 = 25 %. Zusammen 125 %. Prozentangaben über 100 % sind möglich.', einheit='%')),
        ],
        'prozentwert': [
            (2, lambda R: zahl('Berechne 12,5 % von 64 kg.', 8, '64 * 12.5 / 100', '12,5 % sind 1/8.', '12,5 % = 1/8. 64 kg : 8 = 8 kg.', einheit='kg')),
            (2, lambda R: zahl('Berechne 150 % von 36 €.', 54, '36 * 150 / 100', '150 % sind 100 % und noch einmal 50 %.', '100 % = 36 €, 50 % = 18 €. Zusammen 54 €.', einheit='€')),
            (3, lambda R: zahl('70 % der Besucher eines Konzerts sind Erwachsene. 40 % dieser Erwachsenen sind älter als 50 Jahre. '
                               'Wie viel Prozent aller Besucher sind Erwachsene über 50?', 28, '70 * 40 / 100',
                               'Die 40 % beziehen sich nur auf die Erwachsenen. Rechne mit 100 Besuchern.',
                               'Bei 100 Besuchern: 70 Erwachsene. 40 % von 70 = 28. Also 28 % aller Besucher.', einheit='%')),
            (3, lambda R: zahl('Ein Luftfilter entfernt 99 % von 5 000 000 Pollenkörnern. Wie viele Pollenkörner bleiben übrig?', 50000, '5000000 * 1 / 100',
                               'Wie viel Prozent bleiben übrig?', 'Es bleibt 1 % übrig. 1 % von 5 000 000 = 50 000.')),
            (3, lambda R: zahl('15 % einer Zahl sind 9. Wie viel sind 35 % derselben Zahl?', 21, '9 / 15 * 35', 'Rechne zuerst 1 % oder 5 % der Zahl aus.',
                               '15 % = 9, also 5 % = 3. 35 % = 7 · 5 % = 21.')),
            (3, lambda R: zahl('Ein Kind rechnet 4 % von 250 € so: 250 : 4 = 62,50 €. Wie heißt das richtige Ergebnis?', 10, '250 * 4 / 100',
                               '4 % sind 4 Hundertstel, nicht ein Viertel.', '1 % von 250 € = 2,50 €. 4 % = 10 €. Das Kind hat 25 % ausgerechnet.', einheit='€')),
        ],
        'prozentsatz': [
            (2, lambda R: zahl('Von 40 Aufgaben sind 34 richtig. Wie viel Prozent sind richtig?', 85, '34 / 40 * 100', 'Teil durch Ganzes, mal 100.',
                               '34/40 = 85/100 = 85 %.', einheit='%')),
            (2, lambda R: zahl('Wie viel Prozent sind 450 g von 1,5 kg?', 30, '450 / 1500 * 100', 'Rechne beide in Gramm.', '1,5 kg = 1 500 g. 450/1 500 = 30/100 = 30 %.',
                               einheit='%')),
            (3, lambda R: zahl('Beim Spendenlauf liefen im ersten Jahr 40 Kinder mit, im zweiten Jahr 50. Um wie viel Prozent ist die Zahl gestiegen?', 25,
                               '(50 - 40) / 40 * 100', 'Grundwert ist der alte Wert 40.', 'Zunahme 10 Kinder. 10 von 40 = 25 %.', einheit='%')),
            (3, lambda R: zahl('Beim Spendenlauf liefen im ersten Jahr 50 Kinder mit, im zweiten Jahr 40. Um wie viel Prozent ist die Zahl gesunken?', 20,
                               '(50 - 40) / 50 * 100', 'Grundwert ist der alte Wert 50 – nicht 40.', 'Abnahme 10 Kinder. 10 von 50 = 20 %. (Umgekehrt waren es 25 %.)', einheit='%')),
            (3, lambda R: zahl('In einem Verein sind 30 Mädchen und 24 Jungen. Um wie viel Prozent sind es weniger Jungen als Mädchen?', 20, '(30 - 24) / 30 * 100',
                               '„Weniger als die Mädchen“: Die Mädchen sind der Grundwert.', '30 − 24 = 6. 6 von 30 = 20 %.', einheit='%')),
            (3, lambda R: zahl('Ein Quadrat hat 10 cm Seitenlänge. Jede Seite wird um 10 % länger. Um wie viel Prozent wächst der Flächeninhalt?', 21,
                               '(11 * 11 - 10 * 10) / (10 * 10) * 100', 'Rechne den alten und den neuen Flächeninhalt aus.',
                               'Neue Seite 11 cm. Alt 100 cm², neu 121 cm². Zunahme 21 cm² von 100 cm² = 21 % (nicht 10 %).', einheit='%')),
        ],
        'grundwert': [
            (2, lambda R: zahl('35 % sind 49 kg. Wie viel sind 100 %?', 140, '49 / 35 * 100', 'Rechne zuerst 1 % oder 5 % aus.', '5 % = 7 kg. 100 % = 20 · 7 kg = 140 kg.', einheit='kg')),
            (2, lambda R: zahl('12,5 % sind 15 €. Wie viel sind 100 %?', 120, '15 / 12.5 * 100', '12,5 % sind 1/8.', '1/8 sind 15 €, das Ganze 8 · 15 € = 120 €.', einheit='€')),
            (3, lambda R: zahl('In einem Chor sind 20 % weniger Jungen als Mädchen. Es singen 24 Jungen. Wie viele Mädchen singen im Chor?', 30, '24 / 80 * 100',
                               'Die Mädchen sind der Grundwert (100 %). Wie viel Prozent davon sind die Jungen?',
                               'Jungen = 80 % der Mädchen = 24. 1 % = 0,3, also 100 % = 30 Mädchen. (24 + 20 % von 24 = 28,8 wäre falsch.)')),
            (3, lambda R: zahl('Bei einer Untersuchung waren 63 Kinder sichere Schwimmer. Das sind 45 % aller untersuchten Kinder. Wie viele Kinder wurden untersucht?', 140,
                               '63 / 45 * 100', '63 Kinder sind der Prozentwert. Rechne über 5 % auf 100 %.', '45 % = 63, also 5 % = 7 und 100 % = 140 Kinder.')),
            (3, lambda R: zahl('Nach 20 % Rabatt kostet eine Jacke 64 €. Wie viel kostete sie vorher?', 80, '64 / 80 * 100',
                               '64 € sind nicht 100 %, sondern 100 % − 20 %.', '64 € = 80 %. 10 % = 8 €, 100 % = 80 €. (64 € + 20 % = 76,80 € wäre falsch.)', einheit='€')),
            (3, lambda R: zahl('Ein Kind hat 30 % seines Buchs gelesen. Es fehlen noch 154 Seiten. Wie viele Seiten hat das Buch?', 220, '154 / 70 * 100',
                               'Wie viel Prozent fehlen noch?', 'Es fehlen 70 % = 154 Seiten. 10 % = 22 Seiten, 100 % = 220 Seiten.')),
        ],
        'rabatt_aufschlag': [
            (2, lambda R: zahl('Ein Handy kostet 240 €. Im Angebot ist es 15 % billiger. Was kostet es jetzt?', 204, '240 * 85 / 100', 'Man zahlt 100 % − 15 % = 85 %.',
                               '15 % von 240 € = 36 €. 240 € − 36 € = 204 €.', einheit='€')),
            (2, lambda R: zahl('Eine Monatskarte kostet 48 €. Der Preis steigt um 12,5 %. Was kostet sie jetzt?', 54, '48 * 112.5 / 100', '12,5 % sind 1/8.',
                               '1/8 von 48 € = 6 €. 48 € + 6 € = 54 €.', einheit='€')),
            (3, lambda R: zahl('Ein Preis wird erst um 20 % erhöht und danach um 20 % gesenkt. Am Ende kostet die Ware 96 €. Wie viel kostete sie am Anfang?', 100,
                               '96 / (1.2 * 0.8)', 'Probiere mit 100 € als Anfangspreis.', '100 € → +20 % → 120 € → −20 % (von 120 €) → 96 €. Der Anfangspreis war 100 €.', einheit='€')),
            (3, lambda R: zahl('Nach einer Preiserhöhung um 25 % kostet ein Buch 15 €. Wie viel kostete es vorher?', 12, '15 / 125 * 100',
                               '15 € sind 125 % des alten Preises.', '125 % = 15 €, also 25 % = 3 € und 100 % = 12 €.', einheit='€')),
            (3, lambda R: zahl('Eine Packung kostet 4,50 €. Angebot A: 3 Packungen zum Preis von 2. Angebot B: 30 % Rabatt auf jede Packung. '
                               'Du kaufst 3 Packungen. Wie viel Euro sparst du mit dem günstigeren Angebot gegenüber dem anderen?', Fr('0.45'),
                               '3 * 4.5 * 0.7 - 2 * 4.5', 'Rechne für beide Angebote den Preis für 3 Packungen aus.',
                               'A: 2 · 4,50 € = 9,00 €. B: 3 · 4,50 € = 13,50 €, davon 70 % = 9,45 €. A ist um 0,45 € günstiger.', einheit='€')),
            (3, lambda R: zahl('Ein Kind sagt: „20 % Rabatt und danach noch einmal 10 % Rabatt sind zusammen 30 %.“ Wie viel Prozent Rabatt sind es wirklich?', 28,
                               '100 - 100 * 0.8 * 0.9', 'Rechne mit 100 €. Die zweiten 10 % gelten vom schon reduzierten Preis.',
                               '100 € → 80 € → 10 % von 80 € = 8 € → 72 €. Man spart 28 €, also 28 %.', einheit='%')),
        ],
        'zinsen': [
            (2, lambda R: zahl('Wie viel Euro Zinsen bringen 1 250 € in einem Jahr bei 2,4 %?', 30, '1250 * 2.4 / 100', 'Rechne 1 % von 1 250 € aus.',
                               '1 % = 12,50 €. 2,4 % = 2,4 · 12,50 € = 30 €.', einheit='€')),
            (2, lambda R: zahl('Ein Guthaben wächst in einem Jahr durch Zinsen von 800 € auf 820 €. Wie hoch ist der Zinssatz?', Fr('2.5'), '(820 - 800) / 800 * 100',
                               'Wie viel Euro Zinsen gab es? Teile durch das Kapital.', 'Zinsen 20 €. 20/800 = 2,5/100 = 2,5 %.', einheit='%')),
            (3, lambda R: zahl('Bei einem Zinssatz von 2 % bekommt man nach einem Jahr 36 € Zinsen. Wie hoch war das Kapital?', 1800, '36 / 2 * 100',
                               'Die Zinsen sind der Prozentwert, das Kapital ist der Grundwert.', '2 % = 36 €, 1 % = 18 €, 100 % = 1 800 €.', einheit='€')),
            (3, lambda R: zahl('Nach einem Jahr mit 3 % Zinsen sind 1 545 € auf dem Konto. Wie viel Geld wurde eingezahlt?', 1500, '1545 / 103 * 100',
                               'Das neue Guthaben sind 103 % des eingezahlten Betrags.', '103 % = 1 545 €, 1 % = 15 €, 100 % = 1 500 €.', einheit='€')),
            (3, lambda R: zahl('Ein Kredit über 600 € kostet 9 % Zinsen im Jahr. Er wird schon nach 8 Monaten zurückgezahlt. Wie viel Euro Zinsen fallen an?', 36,
                               '600 * 9 / 100 * 8 / 12', 'Rechne erst die Zinsen für ein ganzes Jahr, dann den Anteil für 8 von 12 Monaten.',
                               'Jahreszinsen: 9 % von 600 € = 54 €. 8 Monate sind 8/12 = 2/3 Jahr: 54 € : 3 · 2 = 36 €.', einheit='€')),
            (3, lambda R: zahl('1 000 € liegen zwei Jahre auf einem Konto mit 10 % Zinsen. Die Zinsen des ersten Jahres werden im zweiten Jahr mitverzinst. '
                               'Wie viel Geld ist nach zwei Jahren auf dem Konto?', 1210, '1000 * 1.1 * 1.1',
                               'Im zweiten Jahr ist der Grundwert das Guthaben nach dem ersten Jahr.', 'Nach 1 Jahr: 1 100 €. Nach 2 Jahren: 1 100 € + 110 € = 1 210 € (nicht 1 200 €).',
                               einheit='€')),
        ],
        'verstehen': [
            (2, lambda R: wahl(R, 'Stimmt die Aussage? „200 % von 15 sind 30.“', 'Ja: 200 % heißt das Doppelte, 2 · 15 = 30.',
                               ['Nein, mehr als 100 % gibt es nicht.', 'Nein, 200 % von 15 sind 3 000.'], _PW, '200 % = 2. 2 · 15 = 30.', n=3)),
            (2, lambda R: wahl(R, 'Stimmt die Aussage? „3/5 sind mehr als 55 %.“', 'Ja: 3/5 = 60 %.', ['Nein: 3/5 = 35 %.', 'Nein: 3/5 = 53 %.'],
                               'Schreibe 3/5 in Prozent.', '3/5 = 60/100 = 60 %. 60 % > 55 %.', n=3)),
            (3, lambda R: wahl(R, 'Bei einer Umfrage nannten 31 % Sport als Hobby. Jemand sagt: „Das ist mehr als ein Drittel.“ Stimmt das?',
                               'Nein: Ein Drittel sind etwa 33,3 %, 31 % ist weniger.', ['Ja: 31 % ist mehr als 30 %.', 'Ja: Ein Drittel sind 30 %.', 'Es ist genau ein Drittel.'],
                               'Wie viel Prozent ist 1/3?', '1/3 = 100 % : 3 ≈ 33,3 %. 31 % < 33,3 %.')),
            (3, lambda R: wahl(R, 'In Klasse A spielen 50 % der 20 Kinder ein Instrument, in Klasse B 40 % der 30 Kinder. Jemand sagt: „In A spielen mehr Kinder ein Instrument.“ Stimmt das?',
                               'Nein: In A sind es 10 Kinder, in B 12 Kinder.', ['Ja, denn 50 % ist mehr als 40 %.', 'Beide Klassen haben gleich viele.', 'Ja: In A 10 Kinder, in B 8 Kinder.'],
                               'Rechne die Anzahlen aus. Die Klassen sind verschieden groß.', '50 % von 20 = 10. 40 % von 30 = 12. Der größere Prozentsatz gehört zur kleineren Klasse.')),
            (3, lambda R: wahl(R, 'Der Anteil der Radfahrer steigt von 20 % auf 30 %. Jemand sagt: „Er ist um 10 % gestiegen.“ Was stimmt?',
                               'Er ist um 10 Prozentpunkte gestiegen. Das sind 50 % mehr Radfahrer-Anteil.',
                               ['Die Aussage stimmt genau.', 'Er ist um 30 % gestiegen.', 'Er ist um 10 Prozentpunkte gestiegen, das sind 10 % mehr.'],
                               'Unterscheide Prozentpunkte (Differenz) und Prozent (Veränderung im Vergleich zum alten Wert).',
                               '30 % − 20 % = 10 Prozentpunkte. Im Vergleich zum alten Wert: 10 von 20 = 50 % mehr.')),
            (3, lambda R: wahl(R, 'Stimmt die Aussage? „10 % von 10 % sind 1 %.“', 'Ja: 1/10 von 1/10 sind 1/100 = 1 %.', ['Nein, es sind 20 %.', 'Nein, es sind 100 %.', 'Nein, es sind 10 %.'],
                               'Rechne mit 1 000 €: 10 % davon, dann davon wieder 10 %.', '10 % von 1 000 € = 100 €. 10 % von 100 € = 10 € = 1 % von 1 000 €.')),
        ],
    }


ergaenzen(DATEI, _pz(), seed=6024)


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('bruch.prozent', 13_6_6)
_h = 'Prüfe mit konkreten Zahlen. Achte darauf, worauf sich die Prozente beziehen.'
# a) drei fast gleiche Zins-Aufgaben, einfache Rechnung → Stufe 2
for _g in ('800 € in einem Jahr 24 €', '2 000 € in einem Jahr 60 €', '5 000 € in einem Jahr 150 €'):
    BF.stufe('verstehen', f'Stimmt die Aussage? „Bei 3 % Zinsen bekommt man für {_g} Zinsen.“', 2)
# c) Schreibweise „1000 €“ statt „1 000 €“ (wie sonst im Bausatz)
BF.ersetze('verstehen', 'Stimmt die Aussage? „Sinkt ein Preis von 1000 € auf 500 €, ist er um 100 % gesunken.“', BF.A(
    'Stimmt die Aussage? „Sinkt ein Preis von 1 000 € auf 500 €, ist er um 100 % gesunken.“', 'Nein, die Senkung ist 500 € von 1 000 € = 50 %.',
    ['Ja, weil Verdoppeln + 100 % ist, ist Halbieren − 100 %.', 'Ja, die Aussage stimmt.'],
    'Nein. Gesunken ist der Preis um 500 €. Grundwert ist der alte Preis 1 000 €: 500 : 1 000 = 0,5 = 50 %. Um 100 % gesunken hieße: Der Preis ist 0 €.', _h))
BF.ersetze('verstehen', 'Stimmt die Aussage? „10 % von 500 € ist mehr als 10 % von 1000 €.“', BF.A(
    'Stimmt die Aussage? „10 % von 500 € ist mehr als 10 % von 1 000 €.“', 'Nein, gleicher Prozentsatz, aber kleinerer Grundwert: 50 € < 100 €.',
    ['Ja, die Aussage stimmt.', 'Ja, weil 500 € weniger Geld ist und man davon mehr Prozent bekommt.'],
    'Nein, gleicher Prozentsatz, aber kleinerer Grundwert: 10 % von 500 € sind 50 €, 10 % von 1 000 € sind 100 €.', _h))
# a) Stufe 1–2 bzw. Grundform mit Komma
BF.stufe('prozentsatz', 'Wie viel Prozent einer Stunde sind 30 Minuten?', 2)
BF.stufe('prozentwert', 'Berechne 2,5 % von 320 €.', 2)

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----


# ---------- LUECKEN (Achtzehnte Runde, Teil B, Zweig luecken-kl6) ----------
# Läuft nach allen bisherigen Abschnitten mit eigenem Zufallsstart; vorhandene Karten und Aufgaben bleiben unverändert.
# Lehrplan: LehrplanPLUS Gymnasium Bayern M6 3 (Prozentangaben aus Texten, z. B. Zeitungen, auf Korrektheit prüfen; zwischen Prozent und
# Prozentpunkten unterscheiden; Formulierungen wie „jeder Siebte“, „drei von fünf“). Prüfungsvorbilder: Bayerischer Mathematik-Test Jgst. 8 (ISB)
# 2021 Aufg. 6c (Prozentpunkte statt Prozent); Grundwissentest Jgst. 7 der Realschule (ISB) 2019 Nr. 18 (Aussage mit Prozentangabe prüfen).
from _luecken_kl6 import karte_erweitern, zahl, wahl  # noqa: E402


def _pp_aufgaben():
    PP = 'Prozentpunkte: Differenz der beiden Prozentangaben. Prozent: Differenz im Vergleich zum alten Wert.'
    return [
        (None, 2, lambda R: zahl('Der Anteil der Kinder mit Fahrradhelm steigt von 30 % auf 36 %. Um wie viele Prozentpunkte ist er gestiegen?', 6, '36 - 30',
                                 PP, '36 % − 30 % = 6 Prozentpunkte.', einheit='Prozentpunkte')),
        (None, 2, lambda R: wahl(R, 'In einem Text steht: „Jedes vierte Kind spielt ein Instrument.“ Wie viel Prozent sind das?', '25 %', ['4 %', '40 %', '75 %'],
                                 'Jedes vierte heißt: 1 von 4.', '1 von 4 = 1/4 = 25/100 = 25 %.')),
        (None, 3, lambda R: zahl('Der Anteil der Kinder mit Fahrradhelm steigt von 30 % auf 36 %. Um wie viel Prozent ist der Anteil gestiegen?', 20,
                                 '(36 - 30) / 30 * 100', PP, 'Der Anteil wächst um 6 Prozentpunkte. 6 von 30 sind 1/5 = 20 %.', einheit='%')),
        (None, 3, lambda R: wahl(R, 'In einer Zeitung steht: „Drei von fünf Kindern lesen täglich. Das ist mehr als die Hälfte.“ Stimmt das?',
                                 'Ja: 3 von 5 sind 60 %, und 60 % ist mehr als 50 %.',
                                 ['Nein: 3 von 5 sind 35 %.', 'Nein: Das ist genau die Hälfte.', 'Nein: 3 von 5 sind 30 %.'],
                                 'Schreibe „drei von fünf“ als Bruch und dann in Prozent.', '3/5 = 60/100 = 60 %. Die Hälfte wären 50 %.')),
        (None, 3, lambda R: wahl(R, 'Eine Quote sinkt von 40 % auf 30 %. In der Zeitung steht: „Sie ist um 10 % gesunken.“ Was stimmt?',
                                 'Sie ist um 10 Prozentpunkte gesunken. Das sind 25 % weniger.',
                                 ['Die Zeitung hat recht.', 'Sie ist um 10 Prozentpunkte gesunken, das sind 10 % weniger.', 'Sie ist um 30 % gesunken.'],
                                 PP, '40 % − 30 % = 10 Prozentpunkte. Im Vergleich zum alten Wert: 10 von 40 = 1/4 = 25 % weniger.')),
        (None, 3, lambda R: zahl('Ein Anteil steigt um 10 Prozentpunkte. Das sind 50 % mehr als vorher. Wie viel Prozent war der Anteil vorher?', 20,
                                 '10 / 50 * 100', '10 Prozentpunkte sind die Hälfte des alten Anteils.', '50 % mehr heißt: Die 10 Prozentpunkte sind die Hälfte des alten Werts. Also war er 20 %.',
                                 einheit='%')),
    ]


karte_erweitern(DATEI, 'verstehen', _pp_aufgaben(), seed=6201,
                schritte_einfuegen=[(3, {'text': 'Zweites Beispiel: Der Rad-Anteil steigt von 20 % auf 25 %.',
                                         'bild': {'einheit': ' %', 'werte': [{'name': 'vorher', 'wert': 20}, {'name': 'nachher', 'wert': 25}]}}),
                                    (4, {'text': 'Das sind 5 ⟦Prozentpunkte⟧ mehr. Aber 5 von 20 sind 25 % mehr.'})],
                woerter_dazu=[['Prozentpunkte', 'Abstand zwischen zwei Prozentangaben: von 20 % auf 25 % sind es 5 Prozentpunkte']])


if __name__ == '__main__':
    schreibe(DATEI)
