#!/usr/bin/env python3
"""Thema bruch.rechnen – Rechnen mit rationalen Zahlen (Klasse 6)."""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _basis import *  # noqa: E402,F403

R = random.Random(23)
E = eintrag_laden('bruch.rechnen')
HB = 'Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt, unechte Brüche wie 7/4 sind erlaubt.'
HBN = 'Zähler ins erste Kästchen (mit Minus, wenn das Ergebnis negativ ist), Nenner ins zweite. Vollständig gekürzt.'

def flaechenmodell():
    """Rechteck 4 × 3 Kästchen: 3/4 der Spalten und davon 2/3 der Zeilen gefärbt (2/3 · 3/4)."""
    b = raster(4, 3, 0)
    b['punkte']['_3_2'] = [3.0, 2.0]
    b['linien'] += [['_0_0', '_3_0', '3/4'], ['_0_0', '_0_2', '2/3']]
    b['flaeche'] = ['_0_0', '_3_0', '_3_2', '_0_2']
    return b


ETAPPEN = [
    {'lernziel': 'brueche_plus_minus', 'titel': 'Brüche addieren und subtrahieren',
     'regel': 'Bei ⟦gleichem Nenner⟧ addierst oder subtrahierst du nur die ⟦Zähler⟧, der Nenner bleibt. Bei verschiedenen Nennern erweiterst du zuerst auf den ⟦Hauptnenner⟧. Am Ende ⟦kürzen⟧.',
     'schritte': ['Eine Wanderung: Vormittags schaffst du 3/4 der Strecke, nachmittags noch 1/6. Wie viel ist geschafft? 3/4 + 1/6.', 'Hauptnenner 12: 3/4 = 9/12 und 1/6 = 2/12.',
                  '9/12 + 2/12 = ⟦11/12⟧ der Strecke.'],
     'probe': '11/12 − 1/6 = 11/12 − 2/12 = 9/12 = 3/4 ✓',
     'fehler': '3/4 + 1/6 = 4/10 ist falsch. Schon 3/4 allein ist mehr als 4/10 – durch Dazulaufen kann der Weg nicht kürzer werden! Nenner werden ⟦nie addiert⟧: Erst gleichnamig machen, dann nur die Zähler addieren.'},
    {'lernziel': 'dezimal_plus_minus', 'titel': 'Dezimalzahlen addieren, subtrahieren',
     'regel': 'Dezimalzahlen addierst und subtrahierst du ⟦stellengerecht⟧: ⟦Komma unter Komma⟧. Fehlende Stellen füllst du mit Nullen auf.',
     'schritte': ['4,7 + 2,85: Komma unter Komma schreiben, 4,70 + 2,85.', 'Stelle für Stelle addieren: ⟦7,55⟧.'],
     'probe': '7,55 − 2,85 = 4,70 = 4,7 ✓',
     'fehler': '4,7 + 2,85 = 3,32 ist falsch: Da wurden die Ziffern einfach rechtsbündig untereinandergeschrieben (47 + 285). Es gilt ⟦Komma unter Komma⟧.'},
    {'lernziel': 'vorzeichen', 'titel': 'Rationale Zahlen mit Vorzeichen',
     'regel': 'Für Brüche und Dezimalzahlen mit Vorzeichen gelten dieselben ⟦Vorzeichenregeln⟧ wie bei ganzen Zahlen. Eine negative Zahl subtrahieren heißt ⟦ihre Gegenzahl addieren⟧. Beim Malnehmen und Teilen: gleiche Vorzeichen ⟦plus⟧, verschiedene ⟦minus⟧.',
     'schritte': ['(−2,5) + 1,2: verschiedene Vorzeichen, also Beträge subtrahieren: 2,5 − 1,2 = 1,3.', 'Der größere Betrag (2,5) ist negativ: ⟦−1,3⟧.'],
     'probe': '−1,3 − 1,2 = −2,5 ✓',
     'fehler': '(−0,5) · (−0,4) = −0,2 ist falsch: Zwei negative Faktoren ergeben ein ⟦positives⟧ Ergebnis: 0,2.'},
    {'lernziel': 'brueche_mal', 'titel': 'Brüche multiplizieren',
     'regel': '„Mal“ heißt bei Brüchen ⟦„von“⟧: 2/3 · 3/4 ist 2/3 von 3/4. Rechne ⟦Zähler mal Zähler, Nenner mal Nenner⟧. ⟦Vorher kürzen⟧ (auch über Kreuz) spart Arbeit. Eine ganze Zahl schreibst du als Bruch mit Nenner 1: 4 = 4/1.',
     'schritte': ['2/3 · 3/4: Nimm von einem Rechteck 3/4 (3 von 4 Spalten) und davon 2/3 (2 von 3 Zeilen).',
                  'Gefärbt sind 2 · 3 = 6 von 3 · 4 = 12 Kästchen: 6/12 = 1/2. Genau das rechnet „Zähler mal Zähler, Nenner mal Nenner“.',
                  'Mit Kürzen vorher: 3/4 · 8/9 – 3 und 9 durch 3, 8 und 4 durch 4: 1/1 · 2/3 = ⟦2/3⟧.'],
     'bild': flaechenmodell(),
     'fehler': '2/3 · 4 = 8/12 ist falsch: 4 = 4/1, also wird nur der ⟦Zähler⟧ mal 4 genommen: 2/3 · 4 = 8/3.'},
    {'lernziel': 'brueche_geteilt', 'titel': 'Durch einen Bruch teilen',
     'regel': 'Teilen fragt: ⟦Wie oft passt der Teiler hinein?⟧ Wie viele halbe Pizzen sind 3 Pizzen? 6 Stück – also 3 : 1/2 = 3 · 2. Allgemein: Durch einen Bruch teilst du, indem du mit seinem ⟦Kehrbruch⟧ malnimmst. Kehrbruch heißt ⟦Zähler und Nenner vertauschen⟧: Der Kehrbruch von 3/8 ist 8/3.',
     'schritte': ['5/6 : 2/3 = 5/6 · 3/2.', 'Kürzen (3 und 6 durch 3): 5/2 · 1/2 = ⟦5/4⟧.'],
     'probe': '5/4 · 2/3 = 10/12 = 5/6 ✓',
     'fehler': '5/6 : 2/3 = 6/5 · 2/3 ist falsch: Umgedreht wird nur der ⟦Teiler⟧, also der Bruch ⟦hinter⟧ dem Geteiltzeichen.'},
    {'lernziel': 'dezimal_mal', 'titel': 'Dezimalzahlen multiplizieren',
     'regel': 'Rechne zuerst ⟦ohne Komma⟧. Das Ergebnis hat so viele ⟦Nachkommastellen wie beide Faktoren zusammen⟧. Warum? 0,3 = 3/10 und 0,04 = 4/100. Mal genommen: 12/1 000 – Zehntel mal Hundertstel gibt Tausendstel.',
     'schritte': ['0,3 · 0,04: ohne Komma 3 · 4 = 12. Nachkommastellen: 1 + 2 = 3.', 'Also 0,3 · 0,04 = ⟦0,012⟧.'],
     'probe': '0,012 ist kleiner als 0,04 – passt, denn mal 0,3 macht kleiner ✓',
     'fehler': '0,3 · 0,04 = 0,12 ist falsch: Die Faktoren haben zusammen ⟦3⟧ Nachkommastellen, also braucht das Ergebnis auch 3: 0,012.'},
    {'lernziel': 'dezimal_geteilt', 'titel': 'Durch eine Dezimalzahl teilen',
     'regel': 'Teilst du durch eine Dezimalzahl, verschiebst du das Komma ⟦bei beiden Zahlen gleich weit nach rechts⟧, bis der Teiler eine ⟦ganze Zahl⟧ ist. Der Wert des Quotienten ändert sich dabei nicht.',
     'schritte': ['4,8 : 0,06: Komma bei beiden um 2 Stellen nach rechts: 480 : 6.', '480 : 6 = ⟦80⟧.'],
     'probe': '80 · 0,06 = 4,8 ✓',
     'fehler': '4,8 : 0,06 = 0,8 ist falsch: Das Komma wurde nur beim Teiler verschoben. Es muss ⟦bei beiden Zahlen⟧ gleich weit wandern.'},
    {'lernziel': 'rechenvorteile', 'titel': 'Geschickt rechnen bei · und :',
     'regel': 'Bei ⟦Produkten⟧ darfst du Faktoren ⟦vertauschen⟧ und beliebig ⟦zusammenfassen⟧. Suche Paare, die eine runde Zahl ergeben: 0,25 · 4 = 1, 0,5 · 2 = 1, 2/3 · 3/2 = 1. Mehrmals teilen kannst du zusammenfassen: a : b : c = a : ⟦(b · c)⟧.',
     'schritte': ['0,25 · 7,3 · 4: Vertauschen zu (0,25 · 4) · 7,3.', '= 1 · 7,3 = ⟦7,3⟧.'],
     'fehler': '24 : 0,5 : 2 = 24 : (0,5 : 2) ist falsch: Beim Teilen darf man ⟦nicht beliebig klammern⟧. Richtig: 24 : 0,5 : 2 = 24 : (0,5 · 2) = 24.'},
    {'lernziel': 'gemischt', 'titel': 'Gemischte Rechnungen',
     'regel': '⟦Klammern zuerst⟧, dann ⟦Punkt vor Strich⟧ (· und : vor + und −), sonst ⟦von links nach rechts⟧. Brüche und Dezimalzahlen darfst du umwandeln, wenn es die Rechnung leichter macht.',
     'schritte': ['1/2 + 3/4 · 2/3: Punkt vor Strich, also zuerst 3/4 · 2/3 = 1/2.', '1/2 + 1/2 = ⟦1⟧.'],
     'fehler': '1/2 + 3/4 · 2/3 = 5/4 · 2/3 = 5/6 ist falsch: Hier wurde zuerst addiert. ⟦Punkt vor Strich⟧ – erst malnehmen!'},
    {'lernziel': 'fehler_finden', 'titel': 'Fehler in Rechnungen finden',
     'regel': 'Prüfe eine Rechnung mit einer ⟦Überschlagsrechnung⟧ oder der ⟦Umkehraufgabe⟧. Typische Fehler: Nenner addieren, Komma falsch setzen, falschen Bruch umdrehen, Punkt-vor-Strich vergessen.',
     'schritte': ['Behauptet: 2,4 · 0,5 = 12. Überschlag: 2,4 · 0,5 ist die Hälfte von 2,4, also etwa 1,2.', '12 ist viel zu groß. Fehler: ⟦Komma vergessen⟧, richtig ist 1,2.'],
     'fehler': 'Nur nachrechnen, ohne zu überlegen, ob das Ergebnis passen kann, übersieht Kommafehler. Mal eine Zahl kleiner als 1 macht ein Ergebnis ⟦kleiner⟧, geteilt durch eine Zahl kleiner als 1 macht es ⟦größer⟧.'},
]

MERKE = ['Plus/Minus: gleichnamig machen, Zähler rechnen, kürzen.', 'Mal: Zähler · Zähler, Nenner · Nenner (vorher kürzen).',
         'Geteilt: mit dem Kehrbruch malnehmen.', 'Dezimal mal: Nachkommastellen zusammenzählen. Dezimal geteilt: Komma bei beiden verschieben.',
         'Klammer vor Punkt vor Strich.']


def py(x):
    """Zahl als exakter Python-Ausdruck für c."""
    x = Fr(x)
    try:
        s = zt(x).replace(' ', '').replace(',', '.').replace('−', '-')
    except ValueError:
        s = f'{x.numerator}/{x.denominator}'
    return f'({s})'


def bx(x):
    """Bruch für Texte, negative in Klammern."""
    x = Fr(x)
    return f'({bruch(x)})' if x < 0 else bruch(x)


def lb(x, text, w, h, c):
    x = Fr(x)
    assert x > 0 and x.denominator > 1, x
    return {'y': 'luecken', 'f': {'text': text, 'schablone': '□/□', 'hinweis': HB}, 'o': {'werte': [x.numerator, x.denominator]},
            'c': [f'({c}) * {x.denominator}', f'{x.denominator}'], 'w': w, 'h': h}


def lbn(x, text, w, h, c):
    """Lücke □/□, auch für negative Brüche (Minus im Zähler)."""
    x = Fr(x)
    assert x.denominator > 1, x
    return {'y': 'luecken', 'f': {'text': text, 'schablone': '□/□', 'hinweis': HBN}, 'o': {'werte': [x.numerator, x.denominator]},
            'c': [f'({c}) * {x.denominator}', f'{x.denominator}'], 'w': w, 'h': h}


def zk(x, k):
    """Zahl mit genau k Nachkommastellen: zk(4, 2) = '4,00'."""
    g, _, n = zt(x).partition(',')
    return g + ',' + n.ljust(k, '0')


def eu(x):
    """Geldbetrag mit zwei Nachkommastellen: 18,20 €."""
    x = Fr(x)
    s = zt(abs(x))
    g, _, n = s.partition(',')
    return ('−' if x < 0 else '') + f'{g},{n.ljust(2, "0")} €'


def gm(x):
    """Gemischte Zahl als Text: 7/3 -> 2 1/3."""
    g, r = divmod(x.numerator, x.denominator)
    return f'{g} {r}/{x.denominator}' if r else str(g)


def kreuz(a, b):
    """Lösungsweg mit Kürzschritt über Kreuz: '2 und 4 durch 2, 21 und 35 durch 7 → 1/5 · 3/2 = 3/10'."""
    z1, n1, z2, n2 = a.numerator, a.denominator, b.numerator, b.denominator
    g1, g2 = gcd(z1, n2), gcd(z2, n1)
    teile = ([f'{z1} und {n2} durch {g1}'] if g1 > 1 else []) + ([f'{z2} und {n1} durch {g2}'] if g2 > 1 else [])
    z1, n2, z2, n1 = z1 // g1, n2 // g1, z2 // g2, n1 // g2
    return f'{bruch(a)} · {bruch(b)}: ' + ', '.join(teile) + f' → {z1}/{n1} · {z2}/{n2} = {bruch(a * b)}.'


def zufallsbruch(R, nmax, zmax=None):
    while True:
        n = R.randint(2, nmax)
        z = R.randint(1, zmax or n - 1)
        x = Fr(z, n)
        if x.denominator > 1: return x


def dez(R, k, gmax=20):
    while True:
        x = Fr(R.randint(1, gmax * 10 ** k), 10 ** k)
        if (x * 10 ** k) % 10: return x


def kgv(a, b): return a * b // gcd(a, b)


def gn(a, b):
    """Text: beide Brüche auf den Hauptnenner."""
    h = kgv(a.denominator, b.denominator)
    return h, f'{a.numerator * h // a.denominator}/{h}', f'{b.numerator * h // b.denominator}/{h}'


# ---------- 1 Brüche plus/minus ----------
HN_PAARE = [(4, 6), (6, 8), (6, 9), (8, 12), (9, 12), (10, 15), (4, 10), (6, 10), (8, 6), (12, 8), (10, 4), (6, 4), (9, 6), (15, 6), (12, 9), (8, 10)]


def mit_nenner(n):
    z = R.randint(1, n - 1)
    while gcd(z, n) > 1: z = R.randint(1, n - 1)
    return Fr(z, n)


def g_bpm(st):
    if st == 1:
        if R.random() < .5:
            n = R.randint(3, 15)
            a, b = R.randint(1, n - 1), R.randint(1, n - 1)
            op = R.choice('+-')
            if op == '-' and a <= b: a, b = b, a
            if a == b: return g_bpm(1)
            r = Fr(a + b if op == '+' else a - b, n)
            if r.denominator == 1: return g_bpm(1)
            o = '+' if op == '+' else '−'
            zr = a + b if op == '+' else a - b
            return lb(r, f'Berechne {a}/{n} {o} {b}/{n}.', f'Gleicher Nenner: {a} {o} {b} = {zr}, also {zr}/{n}' + (f' = {bruch(r)} (gekürzt).' if r.denominator != n else '.'),
                      'Gleicher Nenner: Nur die Zähler rechnen, der Nenner bleibt.', f'{a}/{n} {op} {b}/{n}')
        n1 = R.randint(2, 6)
        n2 = n1 * R.randint(2, 3)
        a, b = mit_nenner(n1), mit_nenner(n2)
        if R.random() < .5: a, b = b, a
        op = R.choice('+-')
        if op == '-' and a < b: a, b = b, a
        r = a + b if op == '+' else a - b
        if r <= 0 or r.denominator == 1: return g_bpm(1)
        h, ta, tb = gn(a, b)
        o = '+' if op == '+' else '−'
        return lb(r, f'Berechne {bruch(a)} {o} {bruch(b)}.', f'{h} ist ein Vielfaches des anderen Nenners: {ta} {o} {tb} = {bruch(r)}.',
                  'Der größere Nenner ist schon ein Vielfaches des kleineren. Erweitere nur einen Bruch.', f'{py(a)} {op} {py(b)}')
    if st == 2:
        if R.random() < .3:
            return ergaenzen()
        n1, n2 = R.choice(HN_PAARE)
        a, b = mit_nenner(n1), mit_nenner(n2)
        op = R.choice('+-')
        if op == '-' and a < b: a, b = b, a
        r = a + b if op == '+' else a - b
        if r <= 0 or r.denominator == 1: return g_bpm(2)
        h, ta, tb = gn(a, b)
        o = '+' if op == '+' else '−'
        return lb(r, f'Berechne {bruch(a)} {o} {bruch(b)}.', f'Hauptnenner {h} (nicht {n1} · {n2} = {n1 * n2}): {ta} {o} {tb} = {bruch(r)}.',
                  'Suche das kleinste gemeinsame Vielfache der Nenner. Es ist kleiner als das Produkt der Nenner.', f'{py(a)} {op} {py(b)}')
    art = R.randrange(4)
    if art == 0:
        a, b, c = zufallsbruch(R, 6), zufallsbruch(R, 8), zufallsbruch(R, 6)
        r = a + b - c
        if r <= 0 or r.denominator == 1: return g_bpm(3)
        h = kgv(kgv(a.denominator, b.denominator), c.denominator)
        return lb(r, f'Berechne {bruch(a)} + {bruch(b)} − {bruch(c)}.', f'Hauptnenner {h}: {a.numerator * h // a.denominator}/{h} + {b.numerator * h // b.denominator}/{h} − {c.numerator * h // c.denominator}/{h} = {bruch(r)}.',
                  'Suche einen Nenner, in den alle drei Nenner passen.', f'{py(a)} + {py(b)} - {py(c)}')
    if art == 1:
        g = R.randint(1, 3)
        b, c = zufallsbruch(R, 9), zufallsbruch(R, 8)
        r = g - b - c
        if r <= 0 or r.denominator == 1 or b.denominator == c.denominator: return g_bpm(3)
        h = kgv(b.denominator, c.denominator)
        return lb(r, f'Berechne {g} − {bruch(b)} − {bruch(c)}.',
                  f'Hauptnenner {h}: {g} = {g * h}/{h}, {bruch(b)} = {b.numerator * h // b.denominator}/{h}, {bruch(c)} = {c.numerator * h // c.denominator}/{h}. '
                  f'{g * h}/{h} − {b.numerator * h // b.denominator}/{h} − {c.numerator * h // c.denominator}/{h} = {bruch(r)}.',
                  f'Schreibe {g} als Bruch mit dem Hauptnenner der beiden Brüche.', f'{g} - {py(b)} - {py(c)}')
    if art == 2:
        p, q = R.sample([2, 3, 4, 5, 6, 8], 2)
        a, b = Fr(1, p), Fr(1, q)
        r = 1 - a - b
        if r <= 0: return g_bpm(3)
        return lb(r, f'Von einer Pizza isst ein Kind 1/{p}, ein anderes 1/{q}. Welcher Anteil der Pizza bleibt übrig?',
                  f'Gegessen: 1/{p} + 1/{q} = {bruch(a + b)}. Übrig: 1 − {bruch(a + b)} = {bruch(r)}.', 'Die ganze Pizza ist 1. Ziehe beide Anteile ab.', f'1 - 1/{p} - 1/{q}')
    # gemischte Zahlen
    a = R.randint(1, 4) + zufallsbruch(R, 6)
    if R.random() < .5:
        b = R.randint(1, 3) + zufallsbruch(R, 6)
        if a == b: return g_bpm(3)
        r, o, op = a + b, '+', '+'
        txt = f'Berechne {gm(a)} + {gm(b)}.'
    else:
        g = R.randint(3, 6)
        b = a
        a = Fr(g)
        r, o, op = a - b, '−', '-'
        txt = f'Berechne {g} − {gm(b)}.'
    if r <= 0 or r.denominator == 1: return g_bpm(3)
    return lb(r, txt + ' Gib das Ergebnis als Bruch an.',
              (f'{gm(a)} = {bruch(a)}, ' if a.denominator > 1 else '') + f'{gm(b)} = {bruch(b)}. {bruch(a)} {o} {bruch(b)} = {bruch(r)} (= {gm(r)}).',
              f'Schreibe die gemischten Zahlen als Brüche, z. B. {gm(b)} = {b.numerator // b.denominator} + {b.numerator % b.denominator}/{b.denominator} = {bruch(b)}.',
              f'{py(a)} {op} {py(b)}')


def ergaenzen():
    """Fehlenden Bruch ergänzen: a + □/□ = 1 oder a − □/□ = c."""
    if R.random() < .5:
        a = zufallsbruch(R, 12)
        x = 1 - a
        return lb(x, f'Ergänze: {bruch(a)} + □/□ = 1', f'Bis zum Ganzen fehlen 1 − {bruch(a)} = {a.denominator}/{a.denominator} − {bruch(a)} = {bruch(x)}.',
                  'Wie viel fehlt bis 1? Schreibe 1 mit demselben Nenner.', f'1 - {py(a)}')
    a, c = zufallsbruch(R, 8), zufallsbruch(R, 8)
    if c >= a: a, c = c, a
    x = a - c
    if x <= 0 or x.denominator == 1 or a.denominator == c.denominator: return ergaenzen()
    h, ta, tc = gn(a, c)
    return lb(x, f'Ergänze: {bruch(a)} − □/□ = {bruch(c)}', f'Gesucht ist {bruch(a)} − {bruch(c)}. Hauptnenner {h}: {ta} − {tc} = {bruch(x)}.',
              'Die gesuchte Zahl ist der Unterschied zwischen den beiden Brüchen.', f'{py(a)} - {py(c)}')


# ---------- 2 Dezimal plus/minus ----------
def g_dpm(st):
    if st == 1:
        k = R.randint(1, 2)
        a, b = dez(R, k), dez(R, k)
        op = R.choice('+-')
        if op == '-' and a < b: a, b = b, a
        r = a + b if op == '+' else a - b
        o = '+' if op == '+' else '−'
        return {'y': 'zahl', 'f': {'text': f'Berechne {zt(a)} {o} {zt(b)}.'}, 'o': {'wert': wert(r)}, 'c': f'{py(a)} {op} {py(b)}',
                'w': f'Komma unter Komma: {zt(a)} {o} {zt(b)} = {zt(r)}.', 'h': 'Schreibe Komma unter Komma.'}
    if st == 2 and R.random() < .4:
        g = R.randint(1, 20)
        t = [Fr(g), dez(R, 2, 3), dez(R, 1, 9)]
        R.shuffle(t)
        r = sum(t)
        return {'y': 'zahl', 'f': {'text': 'Berechne ' + ' + '.join(zt(x) for x in t) + '.'}, 'o': {'wert': wert(r)}, 'c': ' + '.join(py(x) for x in t),
                'w': 'Nullen auffüllen, Komma unter Komma: ' + ' + '.join(zk(x, 2) for x in t) + f' = {zt(r)}.',
                'h': 'Eine ganze Zahl hat das Komma ganz rechts: 4 = 4,00. Fülle alle Zahlen auf zwei Nachkommastellen auf.'}
    if st == 2:
        a, b = dez(R, R.choice([1, 3]), 50), dez(R, 2, 50)
        op = R.choice('+-')
        if R.random() < .5: a, b = b, a
        if op == '-' and a < b: a, b = b, a
        r = a + b if op == '+' else a - b
        o = '+' if op == '+' else '−'
        return {'y': 'zahl', 'f': {'text': f'Berechne {zt(a)} {o} {zt(b)}.'}, 'o': {'wert': wert(r)}, 'c': f'{py(a)} {op} {py(b)}',
                'w': f'Mit Nullen auffüllen, Komma unter Komma: {zt(a)} {o} {zt(b)} = {zt(r)}.', 'h': 'Fülle fehlende Nachkommastellen mit Nullen auf.'}
    art = R.randrange(3)
    if art == 0:
        preise = sorted({dez(R, 2, 15) for _ in range(3)})
        s = sum(preise)
        g = R.choice([20, 50, 100]) if s < 20 else 100
        return {'y': 'zahl', 'f': {'text': 'Ein Einkauf kostet ' + ', '.join(f'{zt(p)} €' for p in preise) + f'. Bezahlt wird mit einem {g}-€-Schein. Wie viel Euro gibt es zurück?'},
                'o': {'wert': wert(g - s), 'einheit': '€'}, 'c': f'{g} - ' + ' - '.join(py(p) for p in preise),
                'w': f'Summe: {zt(s)} €. Rückgeld: {g} − {zt(s)} = {zt(g - s)} €.', 'h': 'Addiere zuerst alle Preise, dann ziehe die Summe vom Schein ab.'}
    if art == 1:
        a = dez(R, 1, 9)
        b = dez(R, 3, 9)
        if a < b: a, b = b, a
        if a == b: return g_dpm(3)
        return {'y': 'zahl', 'f': {'text': f'Wie viel fehlt von {zt(b)} bis {zt(a)}?'}, 'o': {'wert': wert(a - b)}, 'c': f'{py(a)} - {py(b)}',
                'w': f'{zt(a)} − {zt(b)}: auffüllen zu {zt(a)}00 − {zt(b)} = {zt(a - b)}.', 'h': 'Rechne die größere minus die kleinere Zahl. Nullen auffüllen!'}
    a = zufallsbruch(R, 5)
    while not all(p in (2, 5) for p in (a.denominator,)): a = zufallsbruch(R, 5)
    if a.denominator not in (2, 4, 5): a = Fr(3, 4)
    b = dez(R, 2, 3)
    return {'y': 'zahl', 'f': {'text': f'Berechne {bruch(a)} + {zt(b)}. Gib das Ergebnis als Dezimalzahl an.'}, 'o': {'wert': wert(a + b)}, 'c': f'{py(a)} + {py(b)}',
            'w': f'{bruch(a)} = {zt(a)}. {zt(a)} + {zt(b)} = {zt(a + b)}.', 'h': 'Wandle den Bruch zuerst in eine Dezimalzahl um.'}


# ---------- 3 Vorzeichen ----------
def g_vz(st):
    if st == 1:
        art = R.randrange(4)
        a, b = dez(R, 1, 9), dez(R, 1, 9)
        if art == 3:
            g = R.randint(2, 6)
            x, y = R.choice([(-a, Fr(g)), (Fr(g), -a)])
            r = x * y
            return {'y': 'zahl', 'f': {'text': f'Berechne {kl(x)} · {kl(y)}.'}, 'o': {'wert': wert(r)}, 'c': f'{py(x)} * {py(y)}',
                    'w': f'Beträge: {zt(abs(x))} · {zt(abs(y))} = {zt(abs(r))}. Verschiedene Vorzeichen: {zt(r)}.', 'h': 'Verschiedene Vorzeichen beim Malnehmen: Das Ergebnis ist negativ.'}
        if art == 2:
            n = R.choice([3, 5, 7, 8, 9])
            p, q = R.sample([k for k in range(1, n) if gcd(k, n) == 1], 2)
            r = Fr(q - p, n)
            if r.denominator == 1 or r == 0: return g_vz(1)
            return lbn(r, f'Berechne (−{p}/{n}) + {q}/{n}.', f'Gleicher Nenner: −{p} + {q} = {zt(q - p)}, also {bruch(Fr(q - p, n))}.',
                       'Gleicher Nenner: Rechne nur mit den Zählern wie mit ganzen Zahlen.', f'(-{p}/{n}) + {q}/{n}')
        if art == 0: x, y, op = -a, b, '+'
        else: x, y, op = a, -b, '-'
        r = x + y if op == '+' else x - y
        o = '+' if op == '+' else '−'
        return {'y': 'zahl', 'f': {'text': f'Berechne {kl(x)} {o} {kl(y)}.'}, 'o': {'wert': wert(r)}, 'c': f'{py(x)} {op} {py(y)}',
                'w': (f'Minus eine negative Zahl wird plus: {kl(x)} + {zt(-y)} = {zt(r)}.' if op == '-' else f'{kl(x)} + {kl(y)} = {zt(r)}.') + ' Vorzeichen wie bei ganzen Zahlen.',
                'h': 'Rechne wie mit ganzen Zahlen: erst die Vorzeichen klären, dann die Beträge rechnen.'}
    if st == 2:
        art = R.randrange(3)
        if art == 0:
            a, b = zufallsbruch(R, 6), zufallsbruch(R, 6)
            if R.random() < .5:
                x, y = -a, b
                r = x - y
                if r.denominator == 1 or a.denominator == b.denominator: return g_vz(2)
                h, ta, tb = gn(a, b)
                return lbn(r, f'Berechne {bx(x)} − {bruch(y)}.', f'Hauptnenner {h}: −{ta} − {tb} = {bruch(r)}. Beide Teile sind negativ, die Beträge addieren sich.',
                           'Gleichnamig machen. Minus und noch einmal minus: Das Ergebnis wird noch kleiner.', f'{py(x)} - {py(y)}')
            x, y = R.choice([(-a, -b), (-a, b), (a, -b)])
            r = x * y
            if r.denominator == 1: return g_vz(2)
            return lbn(r, f'Berechne {bx(x)} · {bx(y)}.', f'{bruch(a)} · {bruch(b)} = {bruch(a * b)}. ' + ('Gleiche Vorzeichen: positiv.' if r > 0 else 'Verschiedene Vorzeichen: negativ.') + f' Ergebnis {bruch(r)}.',
                       'Erst das Vorzeichen bestimmen, dann Zähler mal Zähler und Nenner mal Nenner.', f'{py(x)} * {py(y)}')
        if art == 1:
            a, b = dez(R, 2, 9), dez(R, 1, 9)
            x, y = -a, b
            r = x - y
            return {'y': 'zahl', 'f': {'text': f'Berechne {kl(x)} − {zt(y)}.'}, 'o': {'wert': wert(r)}, 'c': f'{py(x)} - {py(y)}',
                    'w': f'Von {zt(x)} aus noch {zt(y)} weiter nach links: Beträge addieren, {zt(a)} + {zt(b)} = {zt(a + b)}. Ergebnis {zt(r)}.',
                    'h': 'Minus heißt am Zahlenstrahl: nach links. Du bist schon im Negativen.'}
        a, b = dez(R, 1, 6), dez(R, R.choice([0, 1]), 9) if R.random() < .5 else Fr(R.randint(2, 9))
        x, y = R.choice([-1, 1]) * a, R.choice([-1, 1]) * b
        if x > 0 and y > 0: x = -x
        if R.random() < .5:
            r = x * y
            return {'y': 'zahl', 'f': {'text': f'Berechne {kl(x)} · {kl(y)}.'}, 'o': {'wert': wert(r)}, 'c': f'{py(x)} * {py(y)}',
                    'w': f'Beträge: {zt(abs(x))} · {zt(abs(y))} = {zt(abs(r))}. {"Gleiche" if (x < 0) == (y < 0) else "Verschiedene"} Vorzeichen: {zt(r)}.', 'h': 'Gleiche Vorzeichen: plus. Verschiedene: minus.'}
        p = x * y
        return {'y': 'zahl', 'f': {'text': f'Berechne {kl(p)} : {kl(y)}.'}, 'o': {'wert': wert(x)}, 'c': f'{py(p)} / {py(y)}',
                'w': f'Beträge: {zt(abs(p))} : {zt(abs(y))} = {zt(abs(x))}. {"Gleiche" if (p < 0) == (y < 0) else "Verschiedene"} Vorzeichen: {zt(x)}.', 'h': 'Gleiche Vorzeichen: plus. Verschiedene: minus.'}
    art = R.randrange(4)
    if art == 0:
        a, b = zufallsbruch(R, 8), zufallsbruch(R, 8)
        x, y = -a, b
        r = x + y
        if a == b: return g_vz(3)
        falsch = [bruch(-(a + b)), bruch(a - b), f'{b.numerator - a.numerator}/{a.denominator + b.denominator}']
        h, ta, tb = gn(a, b)
        return {**wahl(R, bruch(r), falsch), 'f': {'text': f'Berechne {bx(x)} + {bruch(y)}.'},
                'w': f'Hauptnenner {h}: −{ta} + {tb} = {bruch(r)}.', 'h': 'Gleichnamig machen, dann wie bei ganzen Zahlen rechnen.'}
    if art == 1:
        a, b = zufallsbruch(R, 6), zufallsbruch(R, 6)
        x, y = -a, b * R.choice([-1, 1])
        q = x / y
        if q.denominator == 1: return g_vz(3)
        return lbn(q, f'Berechne {bx(x)} : {bx(y)}.', f'Mit dem Kehrbruch malnehmen: {bx(x)} · {bx(1 / y)} = {bruch(q)}. ' + ('Gleiche Vorzeichen: positiv.' if q > 0 else 'Verschiedene Vorzeichen: negativ.'),
                   'Vorzeichen zuerst bestimmen, dann mit dem Kehrbruch malnehmen.', f'{py(x)} / {py(y)}')
    if art == 2:
        t = [R.choice([-1, 1]) * dez(R, 1, 5) for _ in range(3)]
        r = t[0] - t[1] + t[2]
        return {'y': 'zahl', 'f': {'text': f'Berechne {kl(t[0])} − {kl(t[1])} + {kl(t[2])}.'}, 'o': {'wert': wert(r)}, 'c': f'{py(t[0])} - {py(t[1])} + {py(t[2])}',
                'w': f'Von links nach rechts: {kl(t[0])} − {kl(t[1])} = {zt(t[0] - t[1])}; {kl(t[0] - t[1])} + {kl(t[2])} = {zt(r)}.', 'h': 'Rechne von links nach rechts. Minus einer negativen Zahl wird plus.'}
    k = Fr(R.randint(500, 5000), 100)
    ein = Fr(R.randint(1000, 6000), 100)
    ab = Fr(R.randint(500, 4000), 100)
    r = -k + ein - ab
    return {'y': 'zahl', 'f': {'text': f'Ein Konto steht auf {eu(-k)}. Es werden {eu(ein)} eingezahlt und danach {eu(ab)} abgebucht. Wie ist der neue Kontostand?'},
            'o': {'wert': wert(r), 'einheit': '€'}, 'c': f'-{py(k)} + {py(ein)} - {py(ab)}',
            'w': f'{eu(-k)} + {eu(ein)} = {eu(-k + ein)}; {eu(-k + ein)} − {eu(ab)} = {eu(r)}.', 'h': 'Einzahlen heißt plus, abbuchen heißt minus. Rechne von links nach rechts.'}


# ---------- 4 Brüche mal ----------
def bild_mal():
    """Flächenmodell: p/m von q/n eines Rechtecks (n Spalten, m Zeilen)."""
    n, m = R.randint(2, 6), R.randint(2, 5)
    q, p = R.randint(1, n - 1), R.randint(1, m - 1)
    b = raster(n, m, 0)
    b['punkte']['_e'] = [float(q), float(p)]
    b['linien'] += [['_0_0', f'_{q}_0', f'{q}/{n}'], ['_0_0', f'_0_{p}', f'{p}/{m}']]
    b['flaeche'] = ['_0_0', f'_{q}_0', '_e', f'_0_{p}']
    b['label'] = f'Rechteck aus {n} mal {m} Kästchen, {q} von {n} Spalten und davon {p} von {m} Zeilen gefärbt'
    x = Fr(p, m) * Fr(q, n)
    a = lb(x, f'Das Bild zeigt {p}/{m} von {q}/{n} eines Rechtecks. Welcher Anteil des ganzen Rechtecks ist gefärbt?',
           f'Gefärbt sind {p} · {q} = {p * q} von {m} · {n} = {m * n} Kästchen: {p}/{m} · {q}/{n} = {p * q}/{m * n}' + (f' = {bruch(x)}.' if x.denominator != m * n else '.'),
           'Zähle die gefärbten Kästchen und alle Kästchen.', f'{p}/{m} * {q}/{n}')
    a['f']['grafik'] = b
    return a


def g_bmal(st):
    if st == 1 and R.random() < .3:
        return bild_mal()
    if st == 1:
        a = zufallsbruch(R, 9)
        if R.random() < .5:
            b = zufallsbruch(R, 9)
            r = a * b
            if r.denominator == 1: return g_bmal(1)
            return lb(r, f'Berechne {bruch(a)} · {bruch(b)}.', f'{a.numerator} · {b.numerator} = {a.numerator * b.numerator}, {a.denominator} · {b.denominator} = {a.denominator * b.denominator}: {a.numerator * b.numerator}/{a.denominator * b.denominator}' + (f' = {bruch(r)}.' if r.denominator != a.denominator * b.denominator else '.'),
                      'Zähler mal Zähler, Nenner mal Nenner.', f'{py(a)} * {py(b)}')
        g = R.randint(2, 9)
        r = a * g
        if r.denominator == 1: return g_bmal(1)
        return lb(r, f'Berechne {bruch(a)} · {g}.', f'{g} = {g}/1. {a.numerator} · {g} = {a.numerator * g}, Nenner {a.denominator}: {a.numerator * g}/{a.denominator}' + (f' = {bruch(r)}.' if r.denominator != a.denominator else '.'),
                  'Nur der Zähler wird mit der ganzen Zahl malgenommen.', f'{py(a)} * {g}')
    if st == 2:
        while True:
            p, q, s = R.randint(1, 9), R.randint(2, 9), R.randint(2, 6)
            a, b = Fr(p, q * s), Fr(q * R.randint(1, 3), R.randint(2, 9) * 1)
            if a.denominator > 1 and b.denominator > 1 and (a * b).denominator > 1 and gcd(a.numerator, b.denominator) * gcd(b.numerator, a.denominator) > 1: break
        r = a * b
        return lb(r, f'Berechne {bruch(a)} · {bruch(b)}. Kürze vorher.', 'Über Kreuz kürzen: ' + kreuz(a, b),
                  'Kürze über Kreuz: Zähler des einen mit Nenner des anderen.', f'{py(a)} * {py(b)}')
    art = R.randrange(3)
    if art == 0:
        a = Fr(R.randint(1, 4), R.choice([2, 3, 4, 5]))
        while a >= 1 or a.denominator == 1: a = Fr(R.randint(1, 4), R.choice([2, 3, 4, 5]))
        b = Fr(R.randint(1, 5), R.choice([2, 4, 5, 8]))
        while b.denominator == 1 or b > 2: b = Fr(R.randint(1, 5), R.choice([2, 4, 5, 8]))
        r = a * b
        if r.denominator == 1: return g_bmal(3)
        return lb(r, f'In einer Flasche sind {bruch(b)} l Saft. Davon wird {bruch(a)} getrunken. Wie viele Liter sind das?',
                  f'{bruch(a)} von {bruch(b)} l = {bruch(a)} · {bruch(b)} = {bruch(r)} l.', '„Bruchteil von“ heißt malnehmen.', f'{py(a)} * {py(b)}')
    if art == 1:
        a, b, c = zufallsbruch(R, 6), zufallsbruch(R, 8), zufallsbruch(R, 6)
        r = a * b * c
        if r.denominator == 1: return g_bmal(3)
        return lb(r, f'Berechne {bruch(a)} · {bruch(b)} · {bruch(c)}.', f'Zuerst {kreuz(a, b) if gcd(a.numerator, b.denominator) * gcd(b.numerator, a.denominator) > 1 else f"{bruch(a)} · {bruch(b)} = {bruch(a * b)}."} Dann {bruch(a * b)} · {bruch(c)} = {bruch(r)}.', 'Kürze, wo immer ein Zähler und ein Nenner einen gemeinsamen Teiler haben.',
                  f'{py(a)} * {py(b)} * {py(c)}')
    a = zufallsbruch(R, 9)
    lae, br = R.choice([(3, 4), (5, 8), (2, 3), (4, 5), (7, 10)]), None
    l1, b1 = Fr(*lae), a
    r = l1 * b1
    if r.denominator == 1: return g_bmal(3)
    return lb(r, f'Ein Rechteck ist {bruch(l1)} m lang und {bruch(b1)} m breit. Wie groß ist sein Flächeninhalt in m²?',
              f'Flächeninhalt = Länge · Breite = {bruch(l1)} · {bruch(b1)} = {bruch(r)} m².', 'Flächeninhalt eines Rechtecks: Länge mal Breite.', f'{py(l1)} * {py(b1)}')


# ---------- 5 Brüche geteilt ----------
def kehrbruch_frage():
    a = zufallsbruch(R, 9)
    z, n = a.numerator, a.denominator
    falsch = [bruch(a), f'{n - z}/{n}', f'{z}/{2 * n}']
    return {**wahl(R, f'{n}/{z}', falsch), 'f': {'text': f'Was ist der Kehrbruch von {bruch(a)}?'},
            'w': f'Zähler und Nenner tauschen: {n}/{z}. Probe: {bruch(a)} · {n}/{z} = 1.', 'h': 'Kehrbruch: Zähler und Nenner vertauschen. Bruch mal Kehrbruch ergibt 1.'}


def groesser_kleiner():
    """Wird das Ergebnis größer oder kleiner als die geteilte Zahl?"""
    a = zufallsbruch(R, 9)
    b = Fr(R.randint(1, 9), R.randint(2, 9))
    if b == 1 or b.denominator == 1: return groesser_kleiner()
    gr = b < 1
    r = 'größer, weil durch eine Zahl kleiner als 1 geteilt wird' if gr else 'kleiner, weil durch eine Zahl größer als 1 geteilt wird'
    falsch = ['kleiner, weil Teilen immer kleiner macht', 'größer, weil Teilen durch einen Bruch immer größer macht'] if gr else \
             ['größer, weil Teilen durch einen Bruch immer größer macht', 'kleiner, weil Teilen immer kleiner macht']
    falsch = [f for f in falsch if f != r] + ['gleich groß, weil man nur den Kehrbruch nimmt']
    return {**wahl(R, r, falsch), 'f': {'text': f'Ist {bruch(a)} : {bruch(b)} größer oder kleiner als {bruch(a)}?'},
            'w': f'{bruch(b)} ist {"kleiner" if gr else "größer"} als 1. {bruch(a)} : {bruch(b)} = {bruch(a)} · {b.denominator}/{b.numerator} = {bruch(a / b)} – {"größer" if gr else "kleiner"} als {bruch(a)}.',
            'h': 'Wie oft passt der Teiler hinein? Passt er öfter als einmal, wird das Ergebnis größer.'}


def g_bdiv(st):
    if st == 1:
        if R.random() < .3: return kehrbruch_frage()
        a = zufallsbruch(R, 9)
        if R.random() < .5:
            g = R.randint(2, 6)
            r = a / g
            return lb(r, f'Berechne {bruch(a)} : {g}.', f': {g} heißt · 1/{g}: {bruch(a)} · 1/{g} = {bruch(r)}.', f'Teilen durch {g} ist dasselbe wie malnehmen mit 1/{g}.', f'{py(a)} / {g}')
        g = R.randint(1, 5)
        r = g / a
        if r.denominator == 1:
            return {'y': 'zahl', 'f': {'text': f'Berechne {g} : {bruch(a)}.'}, 'o': {'wert': int(r)}, 'c': f'{g} / {py(a)}',
                    'w': f'Mit dem Kehrbruch malnehmen: {g} · {a.denominator}/{a.numerator} = {zt(r)}.', 'h': 'Teile durch einen Bruch: mit dem Kehrbruch malnehmen.'}
        return lb(r, f'Berechne {g} : {bruch(a)}.', f'Mit dem Kehrbruch malnehmen: {g} · {a.denominator}/{a.numerator} = {bruch(r)}.', 'Kehrbruch: Zähler und Nenner tauschen.', f'{g} / {py(a)}')
    if st == 2:
        a, b = zufallsbruch(R, 9), zufallsbruch(R, 9)
        r = a / b
        if r.denominator == 1 or a == b: return g_bdiv(2)
        return lb(r, f'Berechne {bruch(a)} : {bruch(b)}.', f'{bruch(a)} : {bruch(b)} = {bruch(a)} · {b.denominator}/{b.numerator} = {bruch(r)}.', 'Drehe den zweiten Bruch um und nimm mal.',
                  f'{py(a)} / {py(b)}')
    art = R.randrange(3)
    if art == 0:
        g = R.choice([Fr(3, 2), Fr(2), Fr(5, 2), Fr(3), Fr(9, 4), Fr(15, 4)])
        p = R.choice([Fr(1, 4), Fr(1, 8), Fr(3, 4), Fr(1, 2), Fr(3, 8)])
        r = g / p
        if r.denominator != 1: return g_bdiv(3)
        return {'y': 'zahl', 'f': {'text': f'Wie viele Gläser zu je {bruch(p)} l kann man aus {bruch(g)} l Saft füllen?'}, 'o': {'wert': int(r)}, 'c': f'{py(g)} / {py(p)}',
                'w': f'{bruch(g)} : {bruch(p)} = {bruch(g)} · {p.denominator}/{p.numerator} = {int(r)} Gläser.', 'h': 'Wie oft passt der kleine Bruch in den großen? Das ist eine Division.'}
    if art == 1:
        return groesser_kleiner()
    a, b = zufallsbruch(R, 8), zufallsbruch(R, 8)
    p = a * b
    if p.denominator == 1: return g_bdiv(3)
    return lb(a, f'Ein Rechteck hat den Flächeninhalt {bruch(p)} m² und ist {bruch(b)} m breit. Wie lang ist es?',
              f'Länge = Fläche : Breite = {bruch(p)} : {bruch(b)} = {bruch(p)} · {b.denominator}/{b.numerator} = {bruch(a)} m.', 'Fläche = Länge · Breite. Rechne rückwärts mit Teilen.',
              f'{py(p)} / {py(b)}') if a.denominator > 1 else g_bdiv(3)


# ---------- 6 Dezimal mal ----------
def nks(x):
    s = zt(x)
    return len(s.split(',')[1]) if ',' in s else 0


def g_dmal(st):
    if st == 1:
        a = dez(R, 1, 9)
        b = Fr(R.randint(2, 9))
        if R.random() < .5:
            b = Fr(10 ** R.randint(1, 3))
            r = a * b
            return {'y': 'zahl', 'f': {'text': f'Berechne {zt(a)} · {zt(b)}.'}, 'o': {'wert': wert(r)}, 'c': f'{py(a)} * {py(b)}',
                    'w': f'Mal {zt(b)}: Komma um {len(str(int(b))) - 1} Stelle{"n" if b > 10 else ""} nach rechts. {zt(a)} · {zt(b)} = {zt(r)}.', 'h': 'Mal 10, 100, 1 000: Komma nach rechts verschieben.'}
        r = a * b
        return {'y': 'zahl', 'f': {'text': f'Berechne {zt(a)} · {zt(b)}.'}, 'o': {'wert': wert(r)}, 'c': f'{py(a)} * {py(b)}',
                'w': f'Ohne Komma: {int(a * 10)} · {zt(b)} = {int(a * 10 * b)}. Eine Nachkommastelle: {zt(r)}.', 'h': 'Rechne ohne Komma und setze dann das Komma.'}
    if st == 2:
        a, b = dez(R, R.choice([1, 2]), 9), dez(R, R.choice([1, 2]), 2)
        r = a * b
        ka, kb = nks(a), nks(b)
        return {'y': 'zahl', 'f': {'text': f'Berechne {zt(a)} · {zt(b)}.'}, 'o': {'wert': wert(r)}, 'c': f'{py(a)} * {py(b)}',
                'w': f'Ohne Komma: {int(a * 10 ** ka)} · {int(b * 10 ** kb)} = {int(a * 10 ** ka * b * 10 ** kb)}. Nachkommastellen: {ka} + {kb} = {ka + kb}. Ergebnis: {zt(r)}.',
                'h': 'Zähle die Nachkommastellen beider Faktoren zusammen.'}
    art = R.randrange(3)
    if art == 0:
        a = dez(R, 2, 3)
        b = Fr(R.randint(11, 60), 10)
        return {'y': 'zahl', 'f': {'text': f'Ein Kilogramm Äpfel kostet {zt(a)} €. Was kosten {zt(b)} kg? Runde auf Cent.'}, 'o': {'wert': wert((a * b * 100 + Fr(1, 2)) // 1 / Fr(100)), 'einheit': '€'},
                'c': f'({py(a)} * {py(b)} * 100 + 1/2) // 1 / 100', 'w': f'{zt(a)} · {zt(b)} = {zt(a * b)} €, gerundet {zt((a * b * 100 + Fr(1, 2)) // 1 / Fr(100))} €.',
                'h': 'Preis pro kg mal Anzahl kg. Am Ende auf zwei Nachkommastellen runden.'}
    if art == 1:
        a, b = Fr(R.randint(1, 9), 10), Fr(R.randint(1, 9), 100)
        r = a * b
        return {**wahl(R, zt(r), [zt(r * 10), zt(r * 100), zt(a + b)]), 'f': {'text': f'Was ergibt {zt(a)} · {zt(b)}?'},
                'w': f'{int(a * 10)} · {int(b * 100)} = {int(a * 10 * b * 100)}, Nachkommastellen 1 + 2 = 3: {zt(r)}.', 'h': 'Zähle die Nachkommastellen zusammen – das Ergebnis braucht genauso viele.'}
    l, b = Fr(R.randint(25, 80), 10), Fr(R.randint(25, 60), 10)
    if l == b or (l * 10) % 10 == 0 and (b * 10) % 10 == 0: return g_dmal(3)
    return {'y': 'zahl', 'f': {'text': f'Ein Zimmer ist {zt(l)} m lang und {zt(b)} m breit. Wie groß ist die Bodenfläche in m²?'}, 'o': {'wert': wert(l * b), 'einheit': 'm²'}, 'c': f'{py(l)} * {py(b)}',
            'w': f'{zt(l)} · {zt(b)} = {zt(l * b)} m².', 'h': 'Fläche eines Rechtecks: Länge mal Breite.'}


# ---------- 7 Dezimal geteilt ----------
def g_ddiv(st):
    if st == 1:
        q = dez(R, 1, 9)
        g = R.randint(2, 9)
        a = q * g
        if R.random() < .4:
            t = 10 ** R.randint(1, 3)
            a = dez(R, R.randint(0, 2), 99)
            return {'y': 'zahl', 'f': {'text': f'Berechne {zt(a)} : {zt(t)}.'}, 'o': {'wert': wert(a / t)}, 'c': f'{py(a)} / {t}',
                    'w': f'Durch {zt(t)}: Komma um {len(str(t)) - 1} Stelle{"n" if t > 10 else ""} nach links. {zt(a / t)}.', 'h': 'Durch 10, 100, 1 000: Komma nach links.'}
        return {'y': 'zahl', 'f': {'text': f'Berechne {zt(a)} : {g}.'}, 'o': {'wert': wert(q)}, 'c': f'{py(a)} / {g}',
                'w': f'Schriftlich teilen; beim Überschreiten des Kommas im Ergebnis das Komma setzen: {zt(a)} : {g} = {zt(q)}.', 'h': 'Teile wie gewohnt und setze das Komma, sobald du es in der geteilten Zahl überschreitest.'}
    if st == 2:
        t = dez(R, R.choice([1, 2]), 1) if R.random() < .5 else Fr(R.randint(2, 9), 10 ** R.choice([1, 2]))
        q = Fr(R.randint(2, 90)) if R.random() < .6 else dez(R, 1, 20)
        a = q * t
        k = nks(t)
        return {'y': 'zahl', 'f': {'text': f'Berechne {zt(a)} : {zt(t)}.'}, 'o': {'wert': wert(q)}, 'c': f'{py(a)} / {py(t)}',
                'w': f'Komma bei beiden um {k} Stelle{"n" if k > 1 else ""} nach rechts: {zt(a * 10 ** k)} : {zt(t * 10 ** k)} = {zt(q)}.',
                'h': 'Verschiebe das Komma bei beiden Zahlen, bis der Teiler keine Nachkommastellen mehr hat.'}
    art = R.randrange(4)
    if art == 3:
        return div_runden()
    if art == 0:
        t = R.choice([Fr(1, 2), Fr(1, 4), Fr(1, 5), Fr(3, 4), Fr(1, 10), Fr(1, 20)])
        if t == Fr(1, 20): t = Fr(5, 100)
        n = R.randint(4, 40)
        g = n * t
        return {'y': 'zahl', 'f': {'text': f'Eine Rolle Band ist {zt(g)} m lang. Wie viele Stücke von {zt(t)} m Länge kann man abschneiden?'}, 'o': {'wert': n}, 'c': f'{py(g)} / {py(t)}',
                'w': f'{zt(g)} : {zt(t)} = {zt(g * 10 ** nks(t))} : {zt(t * 10 ** nks(t))} = {n} Stücke.', 'h': 'Wie oft passt das kurze Stück in die ganze Länge? Teile.'}
    if art == 1:
        t = Fr(R.randint(2, 9), 100)
        q = R.randint(2, 90)
        a = q * t
        k = nks(a)
        falsch = [zt(Fr(q, 100)), zt(Fr(q, 10)), zt(q * 10)]
        return {**wahl(R, zt(q), falsch), 'f': {'text': f'Was ergibt {zt(a)} : {zt(t)}?'},
                'w': f'Komma bei beiden um 2 Stellen nach rechts: {zt(a * 100)} : {zt(t * 100)} = {q}.', 'h': 'Überschlag: Teilen durch eine Zahl kleiner als 1 macht das Ergebnis größer.'}
    while True:
        p, m = dez(R, 2, 30), dez(R, 1, 3)
        if (p * m * 100).denominator == 1 and p > 5: break
    g = p * m
    return {'y': 'zahl', 'f': {'text': f'{zt(m)} kg Käse kosten {zt(g)} €. Was kostet 1 kg?'}, 'o': {'wert': wert(p), 'einheit': '€'}, 'c': f'{py(g)} / {py(m)}',
            'w': f'Preis für 1 kg: {zt(g)} : {zt(m)} = {zt(g * 10)} : {zt(m * 10)} = {zt(p)} €.', 'h': 'Preis geteilt durch Menge ergibt den Preis pro kg.'}


def div_runden():
    """Division mit nicht abbrechendem Ergebnis, auf zwei Nachkommastellen runden (toleranz 0,01)."""
    b = R.choice([3, 6, 7, 9, 11, 12])
    a = R.randint(b + 1, 12 * b)
    if Fr(a, b).denominator in (1, 2, 4, 5) or all(p in (2, 5) for p in (Fr(a, b).denominator,)): return div_runden()
    gr = (Fr(a, b) * 100 + Fr(1, 2)) // 1 / Fr(100)
    if R.random() < .5:
        txt = f'Berechne {a} : {b} und runde auf zwei Nachkommastellen.'
        w = f'{a} : {b} = {zt((Fr(a, b) * 1000) // 1 / Fr(1000))}… Die dritte Nachkommastelle entscheidet: ≈ {zt(gr)}.'
        o = {'wert': wert(gr), 'toleranz': 0.01}
    else:
        txt = f'{b} Kinder teilen sich {a} € gerecht. Wie viel Euro bekommt jedes Kind? Runde auf ganze Cent.'
        w = f'{a} : {b} = {zt((Fr(a, b) * 1000) // 1 / Fr(1000))}… € ≈ {eu(gr)}. Es geht nicht genau auf, ein paar Cent bleiben übrig.'
        o = {'wert': wert(gr), 'einheit': '€', 'toleranz': 0.01}
    return {'y': 'zahl', 'f': {'text': txt}, 'o': o, 'c': f'({a} / {b} * 100 + 1/2) // 1 / 100', 'w': w,
            'h': 'Teile schriftlich bis zur dritten Nachkommastelle, dann runde auf die zweite.'}


# ---------- 8 Rechenvorteile ----------
PAARE = [(Fr(1, 4), Fr(4)), (Fr(1, 2), Fr(2)), (Fr(1, 5), Fr(5)), (Fr(5, 4), Fr(8)), (Fr(5, 2), Fr(4)), (Fr(1, 8), Fr(8)), (Fr(1, 20), Fr(20)), (Fr(1, 25), Fr(25)), (Fr(1, 2), Fr(20))]


def g_vort(st):
    if st == 1:
        a, b = R.choice(PAARE[:4])
        x = dez(R, 1, 20)
        fs = [a, x, b]
        R.shuffle(fs)
        r = a * b * x
        return {'y': 'zahl', 'f': {'text': 'Berechne geschickt: ' + ' · '.join(zt(f) for f in fs)}, 'o': {'wert': wert(r)}, 'c': ' * '.join(py(f) for f in fs),
                'w': f'Vertauschen: ({zt(a)} · {zt(b)}) · {zt(x)} = {zt(a * b)} · {zt(x)} = {zt(r)}.', 'h': 'Suche zwei Faktoren, deren Produkt eine runde Zahl ist.'}
    if st == 2:
        if R.random() < .5:
            a = zufallsbruch(R, 9)
            b = Fr(a.denominator, a.numerator) * R.choice([1, 1, 2, 3])
            x = zufallsbruch(R, 9)
            fs = [a, x, b]
            R.shuffle(fs)
            r = a * b * x
            if r.denominator == 1:
                return {'y': 'zahl', 'f': {'text': 'Berechne geschickt: ' + ' · '.join(bruch(f) for f in fs)}, 'o': {'wert': int(r)}, 'c': ' * '.join(py(f) for f in fs),
                        'w': f'{bruch(a)} · {bruch(b)} = {bruch(a * b)}, dann · {bruch(x)} = {zt(r)}.', 'h': 'Welche zwei Faktoren ergeben miteinander malgenommen eine ganze Zahl?'}
            return lb(r, 'Berechne geschickt: ' + ' · '.join(bruch(f) for f in fs), f'Zusammenfassen: {bruch(a)} · {bruch(b)} = {bruch(a * b)}. Dann · {bruch(x)} = {bruch(r)}.',
                      'Welche zwei Faktoren ergeben miteinander malgenommen eine ganze Zahl?', ' * '.join(py(f) for f in fs))
        a, b = R.choice(PAARE)
        x, y = dez(R, 1, 9), Fr(R.randint(2, 9))
        fs = [a, x, b, y]
        R.shuffle(fs)
        r = a * b * x * y
        return {'y': 'zahl', 'f': {'text': 'Berechne geschickt: ' + ' · '.join(zt(f) for f in fs)}, 'o': {'wert': wert(r)}, 'c': ' * '.join(py(f) for f in fs),
                'w': f'({zt(a)} · {zt(b)}) · {zt(x)} · {zt(y)} = {zt(a * b)} · {zt(x * y)} = {zt(r)}.', 'h': 'Ordne die Faktoren um: Zuerst die Paare, die runde Zahlen ergeben.'}
    art = R.randrange(3)
    if art == 0:
        b, c = R.choice([(Fr(1, 2), 2), (Fr(1, 4), 4), (Fr(5, 10), 4), (Fr(25, 100), 2), (Fr(2, 10), 5)])
        q = R.randint(2, 30)
        a = q * b * c
        return {'y': 'zahl', 'f': {'text': f'Berechne geschickt: {zt(a)} : {zt(b)} : {c}'}, 'o': {'wert': wert(q)}, 'c': f'{py(a)} / {py(b)} / {c}',
                'w': f'Zusammenfassen: {zt(a)} : ({zt(b)} · {c}) = {zt(a)} : {zt(b * c)} = {zt(q)}.', 'h': 'Zweimal teilen ist wie einmal durch das Produkt teilen.'}
    if art == 1:
        b, c = R.choice([(Fr(1, 2), 2), (Fr(1, 4), 4), (Fr(5, 10), 4)])
        q = R.randint(2, 30)
        a = q * b * c
        richtig = zt(q)
        falsch = [zt(a / (b / c)), zt(a * b * c), zt(a / b)]
        return {**wahl(R, richtig, falsch), 'f': {'text': f'Was ergibt {zt(a)} : {zt(b)} : {c}?'},
                'w': f'Von links: {zt(a)} : {zt(b)} = {zt(a / b)}, dann : {c} = {zt(q)}. Achtung: {zt(a)} : ({zt(b)} : {c}) wäre falsch geklammert.', 'h': 'Beim Teilen nicht beliebig klammern – rechne von links oder fasse zu : (b · c) zusammen.'}
    a, b = R.choice(PAARE[:5])
    x = zufallsbruch(R, 9)
    y = Fr(x.denominator, x.numerator)
    fs = [a, x, b, y]
    R.shuffle(fs)
    r = a * b * x * y
    txt = ' · '.join(bruch(f) if f.denominator not in (1,) and f in (x, y) else zt(f) for f in fs)
    return {'y': 'zahl', 'f': {'text': 'Berechne geschickt: ' + txt}, 'o': {'wert': wert(r)}, 'c': ' * '.join(py(f) for f in fs),
            'w': f'({bruch(x)} · {bruch(y)}) · ({zt(a)} · {zt(b)}) = 1 · {zt(a * b)} = {zt(r)}.', 'h': 'Ein Bruch mal sein Kehrbruch ergibt 1.'}


# ---------- 9 Gemischt ----------
EINFACH = [Fr(1, 2), Fr(1, 4), Fr(3, 4), Fr(1, 5), Fr(2, 5), Fr(3, 5), Fr(1, 8), Fr(3, 8), Fr(5, 2), Fr(3, 2)]


def g_gem(st):
    if st == 1:
        a, b, c = dez(R, 1, 9), Fr(R.randint(2, 6)), dez(R, 1, 9)
        op = R.choice('+-')
        if op == '-' and a < b * c: op = '+'
        r = a + b * c if op == '+' else a - b * c
        o = '+' if op == '+' else '−'
        return {'y': 'zahl', 'f': {'text': f'Berechne {zt(a)} {o} {zt(b)} · {zt(c)}.'}, 'o': {'wert': wert(r)}, 'c': f'{py(a)} {op} {py(b)} * {py(c)}',
                'w': f'Punkt vor Strich: {zt(b)} · {zt(c)} = {zt(b * c)}. Dann {zt(a)} {o} {zt(b * c)} = {zt(r)}.', 'h': 'Erst malnehmen, dann addieren oder subtrahieren.'}
    if st == 2:
        a, b, c = R.sample(EINFACH, 3)
        art = R.randrange(2)
        if art == 0:
            r = a + b * c
            return {'y': 'zahl', 'f': {'text': f'Berechne {bruch(a)} + {bruch(b)} · {bruch(c)}. Gib das Ergebnis als Dezimalzahl an.'}, 'o': {'wert': wert(r)}, 'c': f'{py(a)} + {py(b)} * {py(c)}',
                    'w': f'Punkt vor Strich: {bruch(b)} · {bruch(c)} = {bruch(b * c)}. {bruch(a)} + {bruch(b * c)} = {bruch(r)} = {zt(r)}.', 'h': 'Erst das Produkt, dann die Summe.'}
        r = (a + b) * c
        return {'y': 'zahl', 'f': {'text': f'Berechne ({bruch(a)} + {bruch(b)}) · {zt(c)}. Gib das Ergebnis als Dezimalzahl an.'}, 'o': {'wert': wert(r)}, 'c': f'({py(a)} + {py(b)}) * {py(c)}',
                'w': f'Klammer zuerst: {bruch(a)} + {bruch(b)} = {bruch(a + b)}. · {zt(c)} = {zt(r)}.', 'h': 'Was in der Klammer steht, wird zuerst gerechnet.'}
    art = R.randrange(3)
    if art == 0:
        a, b = dez(R, 1, 5), dez(R, 1, 5)
        c = R.choice([Fr(1, 2), Fr(1, 4), Fr(2, 10), Fr(5, 10)])
        r = (a - b) / c
        return {'y': 'zahl', 'f': {'text': f'Berechne ({zt(a)} − {zt(b)}) : {zt(c)}.'}, 'o': {'wert': wert(r)}, 'c': f'({py(a)} - {py(b)}) / {py(c)}',
                'w': f'Klammer: {zt(a)} − {zt(b)} = {zt(a - b)}. {zt(a - b)} : {zt(c)} = {zt(r)}.', 'h': 'Klammer zuerst. Bei negativen Zwischenergebnissen auf das Vorzeichen achten.'}
    if art == 1:
        a, b, c, d = R.sample(EINFACH, 4)
        r = a * b - c * d
        return {'y': 'zahl', 'f': {'text': f'Berechne {bruch(a)} · {bruch(b)} − {bruch(c)} · {bruch(d)}. Gib das Ergebnis als Dezimalzahl an.'}, 'o': {'wert': wert(r)},
                'c': f'{py(a)} * {py(b)} - {py(c)} * {py(d)}', 'w': f'Punkt vor Strich: {bruch(a * b)} − {bruch(c * d)} = {bruch(r)} = {zt(r)}.',
                'h': 'Rechne beide Produkte zuerst. Das Ergebnis kann negativ sein.'}
    p = dez(R, 2, 4)
    n1, n2 = R.randint(2, 6), R.randint(2, 6)
    q = dez(R, 2, 3)
    g = R.choice([20, 50])
    r = g - (n1 * p + n2 * q)
    if r < 0: return g_gem(3)
    return {'y': 'zahl', 'f': {'text': f'Ein Kind kauft {n1} Hefte zu je {eu(p)} und {n2} Stifte zu je {eu(q)}. Es bezahlt mit {g} €. Wie viel bekommt es zurück?'},
            'o': {'wert': wert(r), 'einheit': '€'}, 'c': f'{g} - ({n1} * {py(p)} + {n2} * {py(q)})',
            'w': f'{n1} · {eu(p)} = {eu(n1 * p)}, {n2} · {eu(q)} = {eu(n2 * q)}. Zusammen {eu(n1 * p + n2 * q)}. Zurück: {g} € − {eu(n1 * p + n2 * q)} = {eu(r)}.', 'h': 'Stelle einen Term mit Klammer auf: Geld − (Hefte + Stifte).'}


# ---------- 10 Fehler finden ----------
def g_fehler(st):
    typen = {1: ['nenner_add', 'komma_mal', 'kommaregel'], 2: ['kehrbruch', 'komma_div', 'nenner_add', 'punkt'], 3: ['punkt', 'kehrbruch', 'ueberschlag', 'vorzeichen']}[st]
    t = R.choice(typen)
    if t == 'nenner_add':
        a, b = zufallsbruch(R, 7), zufallsbruch(R, 7)
        if a.denominator == b.denominator: return g_fehler(st)
        falsch = f'{a.numerator + b.numerator}/{a.denominator + b.denominator}'
        r = 'Nenner dürfen nicht addiert werden.'
        return {**wahl(R, r, ['Die Rechnung ist richtig.', 'Man hätte die Zähler malnehmen müssen.', 'Man hätte den zweiten Bruch umdrehen müssen.']),
                'f': {'text': f'Ein Kind rechnet: {bruch(a)} + {bruch(b)} = {falsch}. Was ist der Fehler?'},
                'w': f'Richtig: Hauptnenner, {bruch(a)} + {bruch(b)} = {bruch(a + b)}. Nenner werden nie addiert.', 'h': 'Was passiert mit den Nennern beim Addieren?'}
    if t == 'komma_mal':
        a, b = Fr(R.randint(2, 9), 10), Fr(R.randint(2, 9), 10)
        r = zt(a * b)
        return {'y': 'zahl', 'f': {'text': f'Ein Kind rechnet: {zt(a)} · {zt(b)} = {zt(a * b * 10)}. Das ist falsch. Wie heißt das richtige Ergebnis?'}, 'o': {'wert': wert(a * b)}, 'c': f'{py(a)} * {py(b)}',
                'w': f'{int(a * 10)} · {int(b * 10)} = {int(a * b * 100)}, zwei Nachkommastellen: {r}.', 'h': 'Zähle die Nachkommastellen beider Faktoren.'}
    if t == 'kommaregel':
        a = dez(R, 1, 9)
        b = R.choice([Fr(2, 10), Fr(4, 10), Fr(5, 10), Fr(8, 10)])
        aussage = R.choice([(f'{zt(a)} · {zt(b)} ist größer als {zt(a)}.', False, f'Nein, mal {zt(b)} (kleiner als 1) macht kleiner: {zt(a * b)}.'),
                            (f'{zt(a)} : {zt(b)} ist größer als {zt(a)}.', True, f'Ja, durch eine Zahl kleiner als 1 teilen macht größer: {zt(a)} : {zt(b)} = {zt(a / b)}.')])
        s, stimmt, grund = aussage
        return {**wahl(R, grund, ['Ja, die Aussage stimmt.' if not stimmt else 'Nein, die Aussage ist falsch.', 'Das kann man nicht entscheiden.'], 3),
                'f': {'text': f'Stimmt die Aussage? „{s}“'}, 'w': grund, 'h': 'Überlege: Ist der zweite Faktor größer oder kleiner als 1?'}
    if t == 'kehrbruch':
        a, b = zufallsbruch(R, 8), zufallsbruch(R, 8)
        if a == b: return g_fehler(st)
        r = 'Es wurde der falsche Bruch umgedreht.'
        return {**wahl(R, r, ['Die Rechnung ist richtig.', 'Man hätte beide Brüche umdrehen müssen.', 'Man darf beim Teilen nicht kürzen.']),
                'f': {'text': f'Ein Kind rechnet: {bruch(a)} : {bruch(b)} = {a.denominator}/{a.numerator} · {bruch(b)}. Was ist der Fehler?'},
                'w': f'Nur der Teiler {bruch(b)} wird umgedreht: {bruch(a)} · {b.denominator}/{b.numerator} = {bruch(a / b)}.', 'h': 'Welcher Bruch steht hinter dem Geteiltzeichen?'}
    if t == 'komma_div':
        t_ = Fr(R.randint(2, 9), 10)
        q = R.randint(2, 30)
        a = q * t_
        return {'y': 'zahl', 'f': {'text': f'Ein Kind rechnet: {zt(a)} : {zt(t_)} = {zt(Fr(q, 10))}. Das ist falsch. Wie heißt das richtige Ergebnis?'}, 'o': {'wert': q}, 'c': f'{py(a)} / {py(t_)}',
                'w': f'Komma bei beiden um 1 Stelle nach rechts: {zt(a * 10)} : {zt(t_ * 10)} = {q}.', 'h': 'Teilen durch eine Zahl kleiner als 1 macht das Ergebnis größer.'}
    if t == 'punkt':
        a, b, c = R.sample(EINFACH[:8], 3)
        falsch = (a + b) * c
        r = a + b * c
        return {'y': 'zahl', 'f': {'text': f'Ein Kind rechnet: {bruch(a)} + {bruch(b)} · {bruch(c)} = {bruch(falsch)}. Das ist falsch. Wie heißt das richtige Ergebnis als Dezimalzahl?'},
                'o': {'wert': wert(r)}, 'c': f'{py(a)} + {py(b)} * {py(c)}', 'w': f'Punkt vor Strich: {bruch(b)} · {bruch(c)} = {bruch(b * c)}; {bruch(a)} + {bruch(b * c)} = {zt(r)}.',
                'h': 'Das Kind hat zuerst addiert. Was gilt bei Punkt und Strich?'}
    if t == 'ueberschlag':
        a, b = dez(R, 1, 40), dez(R, 1, 9)
        e = a * b
        vorschlaege = [e * 10, e / 10, e, e * 100]
        R.shuffle(vorschlaege)
        return {**wahl(R, zt(e), [zt(v) for v in vorschlaege]), 'f': {'text': f'Welches Ergebnis von {zt(a)} · {zt(b)} kann nach einem Überschlag stimmen?'},
                'w': f'Überschlag: etwa {round(float(a))} · {round(float(b))} = {round(float(a)) * round(float(b))}. Passend: {zt(e)}.', 'h': 'Runde beide Zahlen auf Ganze und rechne grob.'}
    x, y = dez(R, 1, 5), dez(R, 1, 5)
    r = -x - (-y)
    return {'y': 'zahl', 'f': {'text': f'Ein Kind rechnet: (−{zt(x)}) − (−{zt(y)}) = {zt(-x - y)}. Das ist falsch. Wie heißt das richtige Ergebnis?'}, 'o': {'wert': wert(r)}, 'c': f'(-{py(x)}) - (-{py(y)})',
            'w': f'Minus eine negative Zahl wird plus: −{zt(x)} + {zt(y)} = {zt(r)}.', 'h': 'Was wird aus „minus minus“?'}


def kurz(g):
    """Nur Zahl-Ergebnisse mit höchstens 3 Nachkommastellen."""
    def f(st):
        while True:
            a = g(st)
            if a['y'] != 'zahl' or nks(a['o']['wert']) <= 3: return a
    return f


GEN = {'brueche_plus_minus': g_bpm, 'dezimal_plus_minus': g_dpm, 'vorzeichen': g_vz, 'brueche_mal': g_bmal, 'brueche_geteilt': g_bdiv,
       'dezimal_mal': kurz(g_dmal), 'dezimal_geteilt': kurz(g_ddiv), 'rechenvorteile': kurz(g_vort), 'gemischt': kurz(g_gem), 'fehler_finden': kurz(g_fehler)}

DATEI = datei(E, 'Mit Brüchen und Dezimalzahlen – auch negativen – sicher addieren, subtrahieren, multiplizieren und dividieren und Rechenvorteile nutzen.', MERKE,
              [('Plus und Minus', ['brueche_plus_minus', 'dezimal_plus_minus', 'vorzeichen']),
               ('Mal und Geteilt', ['brueche_mal', 'brueche_geteilt', 'dezimal_mal', 'dezimal_geteilt']),
               ('Geschickt und gemischt', ['rechenvorteile', 'gemischt', 'fehler_finden'])],
              ETAPPEN, GEN,
              offen=['Negative Bruch-Ergebnisse kommen jetzt auch als Lücke (□/□, Minus im Zähler), weil die App negative ganze Zahlen in Lücken annimmt (README, Erfahrungen).',
                     'Gemischte Zahlen (z. B. 2 1/3) stehen in Stufe 3 der Lernkarte brueche_plus_minus in der Aufgabe; das Ergebnis wird als unechter Bruch eingegeben (□/□), weil die App kein Eingabeformat „□ □/□“ hat.'])

# ---------- KARTEN: Lernkarten nach dem neuen Muster (Achte Runde, Vorgabe 16.11., Paket U6) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl6.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl6 import umbau  # noqa: E402

KARTEN = {
 'brueche_plus_minus': {
  'einstieg': 'Bis zur Pause schafft ihr 3/4 des Weges, danach noch 1/6. Viertel und Sechstel sind verschieden lang. Mach sie erst gleich groß, dann kannst du ⟦Brüche addieren⟧.',
  'woerter': [['gleichnamig', 'Brüche mit demselben Nenner'],
              ['Hauptnenner', 'der kleinste gemeinsame Nenner']],
  'bild': {'typ': 'bruchstreifen', 'teile': 4, 'gefaerbt': 3, 'teil_text': '3/4', 'zeilen': [{'teile': 6, 'gefaerbt': 1, 'teil_text': '1/6'}]},
  'schritte': [{'text': 'Der Hauptnenner von 4 und 6 ist 12.'},
               {'text': 'Mach beide gleichnamig: 3/4 = 9/12 und 1/6 = 2/12.',
                'bild': {'teile': 12, 'gefaerbt': 9, 'teil_text': '9/12', 'zeilen': [{'teile': 12, 'gefaerbt': 2, 'teil_text': '2/12'}]}},
               {'text': 'Addiere nur die Zähler: 9/12 + 2/12 = ⟦11/12⟧ des Weges.',
                'bild': {'teile': 12, 'gefaerbt': 11, 'teil_text': '11/12', 'zeilen': []}}],
  'fehler': '3/4 + 1/6 = 4/10 ist falsch: 4/10 ist weniger als 3/4. Beim Weiterlaufen wird der Weg nicht kürzer.',
  'fehler_bild': {'teile': 10, 'gefaerbt': 4, 'teil_text': '4/10', 'zeilen': [{'teile': 4, 'gefaerbt': 3, 'teil_text': '3/4'}]},
  'regel': 'Erst ⟦gleichnamig⟧ machen, dann nur die Zähler rechnen. Der Nenner bleibt, am Ende kürzen.'},
 'dezimal_plus_minus': {
  'einstieg': 'Ein Brot kostet 4,70 €, ein Stück Kuchen 2,85 €. Du schreibst Euro unter Euro und Cent unter Cent. Das heißt ⟦Komma unter Komma⟧.',
  'woerter': [['Komma unter Komma', 'gleiche Stellen stehen genau untereinander'],
              ['Endnull', 'eine 0 ganz hinten nach dem Komma; sie ändert den Wert nicht'],
              ['Übertrag', 'eine 1, die zur nächsten Stelle links wandert']],
  'bild': {'typ': 'tabelle', 'kopf': ['', 'E', 'z', 'h'], 'zeilen': [['Brot', '4', '7', '0'], ['Kuchen', '2', '8', '5']]},
  'schritte': [{'text': 'Fülle 4,7 mit einer Endnull auf: 4,70. Gleiche Stellen stehen untereinander.'},
               {'text': 'Hundertstel: 0 + 5 = 5. Zehntel: 7 + 8 = 15, Übertrag 1.',
                'bild': {'zeilen': [['Brot', '4', '7', '0'], ['Kuchen', '2', '8', '5'], ['Summe', '', '5', '5']]}},
               {'text': 'Einer: 4 + 2 + 1 = 7. Zusammen zahlst du ⟦7,55 €⟧.',
                'bild': {'zeilen': [['Brot', '4', '7', '0'], ['Kuchen', '2', '8', '5'], ['Summe', '7', '5', '5']]}}],
  'fehler': '4,7 + 2,85 = 3,32 ist falsch. Dann kosteten beide zusammen weniger als das Brot allein.',
  'regel': 'Schreibe ⟦Komma unter Komma⟧ und fülle mit Endnullen auf. Dann rechnest du wie mit ganzen Zahlen.'},
 'vorzeichen': {
  'einstieg': 'Am Morgen zeigt das Thermometer −2,5 °C. Bis Mittag wird es 1,2 Grad wärmer. Zahlen mit Plus oder Minus davor heißen ⟦Zahlen mit Vorzeichen⟧.',
  'woerter': [['Vorzeichen', 'das + oder − vor einer Zahl'],
              ['Betrag', 'die Zahl ohne Vorzeichen: Der Betrag von −2,5 ist 2,5']],
  'bild': {'typ': 'thermometer', 'start': -5, 'ende': 5, 'schritt': 1, 'stand': -2.5, 'bereich_unter_null': True, 'einheit': '°C'},
  'schritte': [{'text': 'Gerechnet wird (−2,5) + 1,2. Die Vorzeichen sind verschieden.'},
               {'text': 'Ziehe die Beträge voneinander ab: 2,5 − 1,2 = 1,3.'},
               {'text': 'Der größere Betrag hat ein Minus. Mittags sind es ⟦−1,3 °C⟧.', 'bild': {'stand': -1.3}}],
  'fehler': '(−0,5) · (−0,4) = −0,2 ist falsch. Minus mal Minus ergibt Plus: 0,2.',
  'regel': 'Verschiedene Vorzeichen: ⟦Beträge abziehen⟧, Vorzeichen des größeren Betrags nehmen. Minus mal Minus ergibt Plus.'},
 'brueche_mal': {
  'einstieg': 'Im Schulgarten sind 3/4 Beet, auf 2/3 davon wachsen Kartoffeln. Welcher Teil des Gartens ist das? Du rechnest 2/3 · 3/4, einen ⟦Bruchteil vom Bruchteil⟧.',
  'woerter': [['Bruchteil vom Bruchteil', '„2/3 von 3/4“ rechnest du als 2/3 · 3/4'],
              ['über Kreuz kürzen', 'einen Zähler und den Nenner des anderen Bruchs durch dieselbe Zahl teilen']],
  'bild': {'typ': 'bruchstreifen', 'teile': 4, 'gefaerbt': 3, 'teil_text': 'Beet: 3/4', 'ganzes': 'Garten'},
  'schritte': [{'text': 'Teile den Garten in 12 Felder. Das Beet sind 9 davon.', 'bild': {'teile': 12, 'gefaerbt': 9, 'teil_text': 'Beet: 9/12'}},
               {'text': '2/3 von 9 Feldern sind 6 Felder mit Kartoffeln.', 'bild': {'zeilen': [{'teile': 12, 'gefaerbt': 6, 'teil_text': '6/12'}]}},
               {'text': 'Zähler mal Zähler, Nenner mal Nenner: 2/3 · 3/4 = 6/12 = ⟦1/2⟧.'},
               {'text': 'Schneller: erst über Kreuz kürzen, dann 1/1 · 1/2 = 1/2.'}],
  'fehler': '2/3 · 4 = 8/12 ist falsch. Vier Gärten mit je 2/3 Beet sind mehr als ein Garten. Richtig ist 8/3.',
  'regel': 'Zähler mal Zähler, ⟦Nenner mal Nenner⟧. Vorher über Kreuz kürzen spart Arbeit.'},
 'brueche_geteilt': {
  'einstieg': 'Du hast 5/6 l Saft, ein Becher fasst 2/3 l. Wie oft passt 2/3 in 5/6? Dafür brauchst du den ⟦Kehrbruch⟧.',
  'woerter': [['Kehrbruch', 'Zähler und Nenner vertauscht: Der Kehrbruch von 2/3 ist 3/2'],
              ['Teiler', 'die Zahl hinter dem Geteiltzeichen, hier 2/3']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 1, 'abschnitte': 6, 'beschriftet': 'anfang_ende', 'bereich': {'von': 0, 'bis': 5 / 6}},
  'schritte': [{'text': 'Ein Becher sind 4 Sechstel. Er passt einmal ganz hinein.',
                'bild': {'boegen': [{'von': 0, 'bis': 4 / 6, 'name': '1 Becher'}]}},
               {'text': 'Übrig bleibt 1/6 l, das ist ein Viertel Becher.',
                'bild': {'boegen': [{'von': 0, 'bis': 4 / 6, 'name': '1 Becher'}, {'von': 4 / 6, 'bis': 5 / 6, 'name': '1/4'}]}},
               {'text': 'Rechnung: mal den Kehrbruch des Teilers: 5/6 · 3/2 = 15/12 = ⟦5/4⟧.'}],
  'fehler': '6/5 · 2/3 ist falsch: Umgedreht wird nur der Teiler hinter dem Geteiltzeichen. Das ist der Becher, nicht der Saft.',
  'regel': 'Durch einen Bruch teilst du, indem du ⟦mit dem Kehrbruch⟧ malnimmst. Umgedreht wird nur der Teiler.'},
 'dezimal_mal': {
  'einstieg': 'Ein Stück Klebeband ist 0,3 m lang und 0,04 m breit. Seine Fläche ist 0,3 · 0,04 – aber wohin kommt das Komma? Das zeigen die ⟦Nachkommastellen⟧.',
  'woerter': [['Nachkommastelle', 'eine Ziffer hinter dem Komma'],
              ['Faktor', 'eine Zahl, die malgenommen wird']],
  'bild': {'typ': 'figur', 'punkte': {'_A': [0, 0], '_B': [30, 0], '_C': [30, 4], '_D': [0, 4]}, 'flaeche': ['_A', '_B', '_C', '_D'],
           'linien': [['_A', '_B', '0,3 m'], ['_B', '_C', '0,04 m'], ['_C', '_D'], ['_D', '_A']]},
  'schritte': [{'text': 'Rechne zuerst ohne Komma: 3 · 4 = 12.'},
               {'text': 'Die Faktoren haben zusammen 1 + 2 = 3 Nachkommastellen.'},
               {'text': 'Das Ergebnis bekommt auch 3 Nachkommastellen: ⟦0,012 m²⟧.'}],
  'fehler': '0,3 · 0,04 = 0,12 ist falsch. 0,12 m² wären 1 200 cm², viel zu viel für ein Klebeband.',
  'regel': 'Rechne ohne Komma und ⟦zähle die Nachkommastellen⟧ aller Faktoren. So viele bekommt das Ergebnis.'},
 'dezimal_geteilt': {
  'einstieg': 'Ein Aufkleber kostet 0,06 €, du hast 4,80 €. In Cent ist es leicht: 480 Cent : 6 Cent. Beide Zahlen gleich umrechnen heißt ⟦Komma verschieben⟧.',
  'woerter': [['Komma verschieben', 'bei beiden Zahlen das Komma gleich weit nach rechts setzen']],
  'bild': {'typ': 'tabelle', 'kopf': ['', 'Geld', 'Preis'], 'zeilen': [['in €', '4,8', '0,06']]},
  'schritte': [{'text': 'Der Preis 0,06 hat 2 Stellen nach dem Komma.'},
               {'text': 'Verschiebe bei beiden Zahlen das Komma um 2 Stellen: 480 : 6.',
                'bild': {'zeilen': [['in €', '4,8', '0,06'], ['in Cent', '480', '6']]}},
               {'text': '480 : 6 = ⟦80⟧. Du bekommst 80 Aufkleber.'}],
  'fehler': '4,8 : 0,06 = 0,8 ist falsch. Das Komma wurde nur beim Preis verschoben. Es muss bei beiden Zahlen wandern.',
  'fehler_bild': {'zeilen': [['in €', '4,8', '0,06'], ['falsch', '4,8', '6']]},
  'regel': 'Verschiebe das Komma ⟦bei beiden Zahlen⟧ gleich weit. Der Teiler muss ganz werden, dann teilst du normal.'},
 'rechenvorteile': {
  'einstieg': 'Vier 25-Cent-Münzen sind genau 1 €. Solche Paare machen Kopfrechnen leicht. Beim Malnehmen darfst du ⟦Faktoren vertauschen⟧, um sie zusammenzuholen.',
  'woerter': [['Faktoren vertauschen', 'die Reihenfolge beim Malnehmen ändern; das Ergebnis bleibt gleich']],
  'bild': {'typ': 'bruchstreifen', 'teile': 4, 'gefaerbt': 4, 'teil_text': '4 · 0,25 €', 'ganzes': '1 €'},
  'schritte': [{'text': 'Gerechnet wird 0,25 · 7,3 · 4.'},
               {'text': 'Vertausche: 0,25 · 4 · 7,3. Jetzt stehen 0,25 und 4 zusammen.'},
               {'text': '0,25 · 4 = 1, und 1 · 7,3 = ⟦7,3⟧.'}],
  'fehler': 'Beim Teilen darf man nicht umklammern. 24 : 0,5 : 2 ist 24, nicht 24 : 0,25 = 96.',
  'regel': 'Beim Malnehmen darfst du ⟦vertauschen und klammern⟧. Beim Teilen nicht.'},
 'gemischt': {
  'einstieg': 'Du hast eine halbe Pizza gegessen. Dazu kommen 2/3 von einer Dreiviertelpizza. Wie viel ist das zusammen nach ⟦Punkt vor Strich⟧?',
  'woerter': [['Punkt vor Strich', 'erst mal und geteilt, dann plus und minus']],
  'bild': {'typ': 'bruchstreifen', 'teile': 2, 'gefaerbt': 1, 'teil_text': '1/2', 'ganzes': '1 Pizza'},
  'schritte': [{'text': 'Gerechnet wird 1/2 + 3/4 · 2/3.'},
               {'text': 'Punkt vor Strich: 3/4 · 2/3 = 6/12 = 1/2.',
                'bild': {'zeilen': [{'teile': 4, 'gefaerbt': 3, 'teil_text': '3/4'}, {'teile': 12, 'gefaerbt': 6, 'teil_text': '2/3 davon'}]}},
               {'text': 'Dann plus: 1/2 + 1/2 = ⟦1⟧ ganze Pizza.', 'bild': {'gefaerbt': 2, 'teil_text': '1/2 + 1/2 = 1', 'zeilen': []}}],
  'fehler': 'Zuerst addieren ergibt 5/4 · 2/3 = 5/6. Dann hättest du auch von der gegessenen Hälfte 2/3 genommen.',
  'regel': 'Es gilt ⟦Punkt vor Strich⟧, auch bei Brüchen. Klammern rechnest du zuerst.'},
 'fehler_finden': {
  'einstieg': 'An der Obstwaage steht: 2,4 kg Äpfel zu 0,50 € pro kg kosten 12 €. Das kann nicht stimmen. Wer grob nachrechnet, macht einen ⟦Überschlag⟧.',
  'woerter': [['Überschlag', 'eine grobe Rechnung im Kopf, um ein Ergebnis zu prüfen']],
  'bild': {'typ': 'tabelle', 'kopf': ['', 'Rechnung', 'Ergebnis'], 'zeilen': [['Waage', '2,4 · 0,5', '12']]},
  'schritte': [{'text': 'Überschlag: Mal 0,5 heißt die Hälfte. Die Hälfte von 2,4 ist 1,2.',
                'bild': {'zeilen': [['Waage', '2,4 · 0,5', '12'], ['Überschlag', 'Hälfte', '1,2']]}},
               {'text': '12 ist zehnmal so groß wie 1,2. Das Komma wurde vergessen.'},
               {'text': 'Richtig ist 2,4 · 0,5 = ⟦1,2⟧. Die Äpfel kosten 1,20 €.',
                'bild': {'zeilen': [['Waage', '2,4 · 0,5', '12'], ['Überschlag', 'Hälfte', '1,2'], ['richtig', '2,4 · 0,5', '1,2']]}}],
  'fehler': 'Nur nachrechnen, ohne zu überlegen, übersieht Kommafehler. Mal eine Zahl unter 1 macht das Ergebnis kleiner.',
  'regel': 'Prüfe jedes Ergebnis mit einem ⟦Überschlag⟧. Mal einer Zahl unter 1 wird es kleiner, geteilt durch sie größer.'},
}

umbau(DATEI, KARTEN)


if __name__ == '__main__':
    schreibe(DATEI)
