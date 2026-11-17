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



# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl6): je Lernkarte 2 Übungen Stufe 2 + 4 Übungen Stufe 3 ----------
# Läuft nach allen bisherigen Aufgaben mit eigenem Zufallsstart; die bisherigen Aufgaben bleiben unverändert.
# Prüfungsvorbilder: Bayerischer Mathematik-Test Jgst. 8 (ISB) 2024 Aufg. 6a (Produkt aus bekanntem Ganzzahlprodukt, Kommastellen zählen),
# 2025 Aufg. 5 (Formel für den Mittelwert ohne Klammern), 2014 Gruppe B Aufg. 1c (Anteil vom Anteil) und Aufg. 2 (Bruchterm durch eine Zahl teilen),
# 2023 Aufg. 4b (Einheiten umrechnen mit Dezimalfaktor), 2023 Aufg. 5a (Restanteil);
# Jahrgangsstufentest Realschule Jgst. 6 (ISB) 2024 Nr. 7 (Lücken so füllen, dass das Ergebnis stimmt), Nr. 15 (Kassenbon prüfen),
# 2018 Nr. 14 (Klammern setzen), 2016 (Term zu einem Text); Fehler beschreiben (2020, 2022).
from _schwer_kl6 import ergaenzen, zahl, wahl, luecken, anteil  # noqa: E402

_HB = 'Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt; ein Minus gehört in den Zähler.'


def _bl(text, z, n, cz, cn, h, w):
    return luecken(text, '□/□', _HB, [z, n], [cz, cn], h, w)


def _rr():
    return {
        'brueche_plus_minus': [
            (2, lambda R: anteil('Berechne 5/6 − 3/8.', 20 - 9, 24, 'Hauptnenner von 6 und 8 ist 24.', '5/6 = 20/24, 3/8 = 9/24. 20/24 − 9/24 = 11/24.')),
            (2, lambda R: anteil('Berechne 1 3/4 + 2/3. Gib das Ergebnis als Bruch an.', 21 + 8, 12, 'Schreibe 1 3/4 als Bruch: 7/4. Hauptnenner 12.',
                                 '1 3/4 = 7/4 = 21/12, 2/3 = 8/12. 21/12 + 8/12 = 29/12.')),
            (3, lambda R: anteil('Von der Kasse für eine Klassenfahrt gehen 2/5 für die Unterkunft, 1/4 für die Fahrt und 1/6 für Eintritte weg. '
                                 'Welcher Anteil bleibt für das Essen?', 60 - 24 - 15 - 10, 60, 'Das Ganze ist 1. Hauptnenner von 5, 4 und 6 ist 60.',
                                 '2/5 = 24/60, 1/4 = 15/60, 1/6 = 10/60. Zusammen 49/60. Für das Essen bleiben 60/60 − 49/60 = 11/60.')),
            (3, lambda R: zahl('Welche Zahl gehört in das Kästchen? 1/3 + 1/□ = 1/2', 6, '1 / (1/2 - 1/3)',
                               'Rechne zuerst aus, wie viel von 1/3 bis 1/2 fehlt.', '1/2 − 1/3 = 3/6 − 2/6 = 1/6. Also gehört 6 in das Kästchen.')),
            (3, lambda R: anteil('Berechne, wie viel bis 1 fehlt: 1/2 + 1/4 + 1/8 + 1/16', 16 - 8 - 4 - 2 - 1, 16,
                                 'Schreibe alle Brüche in Sechzehnteln.', '8/16 + 4/16 + 2/16 + 1/16 = 15/16. Bis 1 fehlt 1/16.')),
            (3, lambda R: anteil('Ein Kind rechnet 2 1/2 − 1 3/4 so: 2 − 1 = 1 und 3/4 − 1/2 = 1/4, also 1 1/4. Wie heißt das richtige Ergebnis?',
                                 10 - 7, 4, 'Schreibe beide gemischten Zahlen als Brüche mit dem Nenner 4.',
                                 '2 1/2 = 10/4, 1 3/4 = 7/4. 10/4 − 7/4 = 3/4. Das Kind hat die Brüche vertauscht abgezogen.')),
        ],
        'dezimal_plus_minus': [
            (2, lambda R: zahl('Berechne 12 − 3,47.', Fr('8.53'), '12 - 3.47', 'Schreibe 12 als 12,00.', '12,00 − 3,47 = 8,53.')),
            (2, lambda R: zahl('Berechne 0,6 + 0,45 + 0,055.', Fr('1.105'), '0.6 + 0.45 + 0.055', 'Komma unter Komma, mit Endnullen auffüllen.',
                               '0,600 + 0,450 + 0,055 = 1,105.')),
            (3, lambda R: zahl('Ein Kind springt 3,85 m, 4,1 m und 3,9 m weit. Um wie viele Zentimeter ist der beste Sprung weiter als der schlechteste?', 25,
                               '(4.1 - 3.85) * 100', 'Finde den besten und den schlechtesten Sprung. Rechne am Ende in cm um.',
                               'Bester Sprung 4,10 m, schlechtester 3,85 m. 4,10 − 3,85 = 0,25 m = 25 cm.', einheit='cm')),
            (3, lambda R: zahl('Auf einem Kassenbon stehen 2,49 €, 0,89 € und 3,15 €. Die Kasse verlangt 6,83 €. Um wie viel Cent hat sich die Kasse verrechnet?', 30,
                               '(6.83 - (2.49 + 0.89 + 3.15)) * 100', 'Addiere die drei Preise und vergleiche mit 6,83 €.',
                               '2,49 € + 0,89 € + 3,15 € = 6,53 €. 6,83 € − 6,53 € = 0,30 € = 30 Cent zu viel.', einheit='Cent')),
            (3, lambda R: zahl('Eine Zahl wird um 2,75 vergrößert und danach um 4,6 verkleinert. Es kommt 1,2 heraus. Wie hieß die Zahl?', Fr('3.05'), '1.2 + 4.6 - 2.75',
                               'Rechne rückwärts: Mach jeden Schritt in umgekehrter Reihenfolge rückgängig.', '1,2 + 4,6 = 5,8. 5,8 − 2,75 = 3,05. Probe: 3,05 + 2,75 − 4,6 = 1,2.')),
            (3, lambda R: zahl('Ein Kind rechnet 5,3 + 2,48 = 7,51, weil es die Zahlen rechtsbündig untereinander geschrieben hat. Wie heißt das richtige Ergebnis?',
                               Fr('7.78'), '5.3 + 2.48', 'Komma unter Komma: 5,30 + 2,48.', '5,30 + 2,48 = 7,78. Rechtsbündig stand die 3 Zehntel unter den 8 Hundertsteln.')),
        ],
        'vorzeichen': [
            (2, lambda R: zahl('Berechne (−2,5) − 1,75.', Fr('-4.25'), '(-2.5) - 1.75', 'Du gehst von −2,5 noch weiter nach links.', '(−2,5) − 1,75 = −(2,5 + 1,75) = −4,25.')),
            (2, lambda R: _bl('Berechne (−2/3) + 1/4.', -5, 12, '-8 + 3', '12', 'Hauptnenner 12. Verschiedene Vorzeichen: Beträge abziehen.',
                              '(−8/12) + 3/12 = −5/12. Der größere Betrag (8/12) ist negativ.')),
            (3, lambda R: zahl('Welche Zahl gehört in das Kästchen? □ : (−0,5) = 14', -7, '14 * (-0.5)', 'Rechne rückwärts: Teilen macht man mit Malnehmen rückgängig.',
                               '□ = 14 · (−0,5) = −7. Probe: (−7) : (−0,5) = 14.')),
            (3, lambda R: zahl('Morgens sind es −3,5 °C. Bis mittags steigt die Temperatur um 7,8 °C, bis abends fällt sie um 5,25 °C. Wie warm ist es abends?',
                               Fr('-0.95'), '-3.5 + 7.8 - 5.25', 'Steigen heißt plus, fallen heißt minus.', '−3,5 + 7,8 = 4,3. 4,3 − 5,25 = −0,95. Abends sind es −0,95 °C.',
                               einheit='°C')),
            (3, lambda R: zahl('Berechne (−0,5) · (−2) · (−0,1) · (−3) · (−1).', Fr('-0.3'), '(-0.5) * (-2) * (-0.1) * (-3) * (-1)',
                               'Zähle zuerst die Minuszeichen: Gerade Anzahl ergibt plus, ungerade minus.',
                               'Fünf negative Faktoren: ungerade Anzahl, also minus. Beträge: 0,5 · 2 · 0,1 · 3 · 1 = 0,3. Ergebnis −0,3.')),
            (3, lambda R: _bl('Ein Kind rechnet (−3/4) − (−1/2) = −5/4. Wie heißt das richtige Ergebnis?', -1, 4, '-3 + 2', '4',
                              'Minus eine negative Zahl heißt: die Gegenzahl addieren.', '(−3/4) − (−1/2) = (−3/4) + 2/4 = −1/4. Das Kind hat −1/2 addiert statt abgezogen.')),
        ],
        'brueche_mal': [
            (2, lambda R: anteil('Berechne 2/3 · 9/16. Kürze vorher.', 2 * 9, 3 * 16, 'Kürze über Kreuz: 2 mit 16 und 3 mit 9.', '2/3 · 9/16 = (1 · 3)/(1 · 8) = 3/8.')),
            (2, lambda R: anteil('Berechne 1 1/2 · 2/9.', 3 * 2, 2 * 9, 'Schreibe 1 1/2 als Bruch.', '1 1/2 = 3/2. 3/2 · 2/9 = 6/18 = 1/3.')),
            (3, lambda R: anteil('3/4 der Besucher eines Festes kommen aus der Stadt. 2/5 davon kommen mit dem Rad. '
                                 'Welcher Anteil aller Besucher kommt aus der Stadt mit dem Rad?', 3 * 2, 4 * 5,
                                 '„2/5 davon“ heißt: 2/5 von 3/4. Von heißt mal.', '2/5 · 3/4 = 6/20 = 3/10. (Nicht 2/5 aller Besucher!)')),
            (3, lambda R: anteil('Für 4 Personen braucht man 3/4 l Milch. Wie viele Liter braucht man für 6 Personen?', 3 * 6, 4 * 4,
                                 'Wie viel braucht eine Person? Oder: 6 Personen sind 6/4 von 4 Personen.',
                                 'Eine Person: 3/4 : 4 = 3/16 l. Sechs Personen: 6 · 3/16 = 18/16 = 9/8 l.')),
            (3, lambda R: anteil('Mit welchem Bruch musst du 4/9 malnehmen, um 2/3 zu erhalten?', 2 * 9, 3 * 4,
                                 'Rückwärts: Das Gegenteil von Malnehmen ist Teilen. Rechne 2/3 : 4/9.', '2/3 : 4/9 = 2/3 · 9/4 = 18/12 = 3/2. Probe: 4/9 · 3/2 = 12/18 = 2/3.')),
            (3, lambda R: anteil('Ein Kind rechnet 2/5 · 3/5 = 6/5. Wie heißt das richtige Ergebnis?', 2 * 3, 5 * 5,
                                 'Beim Malnehmen werden auch die Nenner malgenommen.', '2/5 · 3/5 = (2 · 3)/(5 · 5) = 6/25. 6/5 wäre mehr als 1, aber ein Teil von 3/5 muss kleiner sein.')),
        ],
        'brueche_geteilt': [
            (2, lambda R: anteil('Berechne 5/6 : 10/9.', 5 * 9, 6 * 10, 'Mit dem Kehrbruch 9/10 malnehmen.', '5/6 · 9/10 = 45/60 = 3/4.')),
            (2, lambda R: zahl('Berechne 4 : 2/3.', 6, '4 / (2/3)', 'Mit dem Kehrbruch 3/2 malnehmen.', '4 · 3/2 = 12/2 = 6.')),
            (3, lambda R: anteil('Teile die Differenz von 2 1/2 und 3/4 durch 5.', 10 - 3, 4 * 5, 'Rechne zuerst die Differenz aus, dann teilen durch 5 = mal 1/5.',
                                 '2 1/2 − 3/4 = 10/4 − 3/4 = 7/4. 7/4 : 5 = 7/20.')),
            (3, lambda R: zahl('Ein Band ist 7 1/2 m lang. Es wird in Stücke zu je 3/4 m geschnitten. Wie viele Stücke entstehen?', 10, '(15/2) / (3/4)',
                               'Wie oft passt 3/4 in 7 1/2? Schreibe 7 1/2 als Bruch.', '7 1/2 = 15/2. 15/2 : 3/4 = 15/2 · 4/3 = 60/6 = 10 Stücke.')),
            (3, lambda R: anteil('Durch welchen Bruch musst du 3/5 teilen, um 9/10 zu erhalten?', 3 * 10, 5 * 9,
                                 'Rückwärts: 3/5 : □ = 9/10. Also □ = 3/5 : 9/10.', '3/5 : 9/10 = 3/5 · 10/9 = 30/45 = 2/3. Probe: 3/5 : 2/3 = 9/10.')),
            (3, lambda R: wahl(R, 'Ohne zu rechnen: Welche Rechnung hat das größte Ergebnis?', '7 : 1/2', ['7 · 1/2', '7 : 2', '7 − 1/2'],
                               'Durch eine Zahl kleiner als 1 teilen macht größer, mal eine Zahl kleiner als 1 macht kleiner.',
                               '7 : 1/2 = 14. 7 · 1/2 = 3,5; 7 : 2 = 3,5; 7 − 1/2 = 6,5.')),
        ],
        'dezimal_mal': [
            (2, lambda R: zahl('Berechne 0,25 · 0,36.', Fr('0.09'), '0.25 * 0.36', 'Rechne 25 · 36 und zähle die Nachkommastellen.', '25 · 36 = 900. Vier Nachkommastellen: 0,0900 = 0,09.')),
            (2, lambda R: zahl('Berechne 12,5 · 0,08.', 1, '12.5 * 0.08', 'Rechne 125 · 8 und zähle die Nachkommastellen.', '125 · 8 = 1 000. Drei Nachkommastellen: 1,000 = 1.')),
            (3, lambda R: zahl('Es gilt 37 · 23 = 851. Berechne damit 3,7 · 0,23.', Fr('0.851'), '3.7 * 0.23', 'Zähle die Nachkommastellen beider Faktoren.',
                               '3,7 hat eine, 0,23 hat zwei Nachkommastellen, zusammen drei. Also 0,851.')),
            (3, lambda R: zahl('Strom kostet 0,32 € je kWh. Ein Gerät braucht 0,15 kWh pro Stunde und läuft 40 Stunden. Was kostet der Strom?', Fr('1.92'),
                               '0.15 * 40 * 0.32', 'Rechne zuerst den ganzen Verbrauch in kWh aus.', '0,15 kWh · 40 = 6 kWh. 6 · 0,32 € = 1,92 €.', einheit='€')),
            (3, lambda R: zahl('Welche Zahl musst du mit 0,4 malnehmen, um 1 zu erhalten?', Fr('2.5'), '1 / 0.4', 'Rückwärts: 1 : 0,4.',
                               '1 : 0,4 = 10 : 4 = 2,5. Probe: 2,5 · 0,4 = 1.')),
            (3, lambda R: zahl('Ein Kind rechnet 0,6 · 0,6 = 3,6. Wie heißt das richtige Ergebnis?', Fr('0.36'), '0.6 * 0.6',
                               'Mal eine Zahl kleiner als 1 macht kleiner. Zähle die Nachkommastellen.', '6 · 6 = 36, zwei Nachkommastellen: 0,36. 3,6 ist größer als 0,6 – das kann nicht stimmen.')),
        ],
        'dezimal_geteilt': [
            (2, lambda R: zahl('Berechne 1,8 : 0,06.', 30, '1.8 / 0.06', 'Verschiebe das Komma bei beiden Zahlen um 2 Stellen.', '1,8 : 0,06 = 180 : 6 = 30.')),
            (2, lambda R: zahl('Berechne 0,09 : 0,3.', Fr('0.3'), '0.09 / 0.3', 'Verschiebe das Komma bei beiden Zahlen um 1 Stelle.', '0,09 : 0,3 = 0,9 : 3 = 0,3.')),
            (3, lambda R: zahl('1 Zoll sind 2,54 cm. Ein Bildschirm ist 63,5 cm breit. Wie viele Zoll sind das?', 25, '63.5 / 2.54',
                               'Wie oft passt 2,54 cm in 63,5 cm?', '63,5 : 2,54 = 6 350 : 254 = 25 Zoll.')),
            (3, lambda R: zahl('Packung A: 0,75 kg für 2,40 €. Packung B: 1,2 kg für 3,60 €. Wie viel kostet 1 kg bei der günstigeren Packung?', 3,
                               'min(2.40 / 0.75, 3.60 / 1.2)', 'Rechne für beide Packungen den Preis für 1 kg aus.',
                               'A: 2,40 € : 0,75 = 3,20 € je kg. B: 3,60 € : 1,2 = 3,00 € je kg. B ist günstiger: 3 €.', einheit='€')),
            (3, lambda R: zahl('Eine Zahl wird durch 0,5 geteilt und das Ergebnis durch 0,2. Es kommt 30 heraus. Wie hieß die Zahl?', 3, '30 * 0.2 * 0.5',
                               'Rechne rückwärts: Mach das Teilen durch Malnehmen rückgängig.', '30 · 0,2 = 6. 6 · 0,5 = 3. Probe: 3 : 0,5 = 6, 6 : 0,2 = 30.')),
            (3, lambda R: wahl(R, 'Ohne zu rechnen: Welches Ergebnis ist größer als 8?', '8 : 0,9', ['8 : 1,1', '8 · 0,9', '8 : 8,5'],
                               'Teilen durch eine Zahl kleiner als 1 macht größer.', '0,9 ist kleiner als 1, also ist 8 : 0,9 größer als 8 (etwa 8,9). Die anderen sind kleiner als 8.')),
        ],
        'rechenvorteile': [
            (2, lambda R: zahl('Berechne geschickt: 0,125 · 7,3 · 8', Fr('7.3'), '0.125 * 7.3 * 8', 'Fasse 0,125 · 8 zusammen.', '0,125 · 8 = 1. 1 · 7,3 = 7,3.')),
            (2, lambda R: zahl('Berechne geschickt: 2/5 · 17 · 5/2', 17, '(2/5) * 17 * (5/2)', 'Vertausche so, dass 2/5 und 5/2 nebeneinander stehen.', '2/5 · 5/2 = 1. 1 · 17 = 17.')),
            (3, lambda R: wahl(R, 'Wo müssen Klammern stehen, damit 36 : 4 · 3 das Ergebnis 3 hat?', '36 : (4 · 3)', ['(36 : 4) · 3', 'Man braucht keine Klammern.', '36 : 4 · (3)'],
                               'Rechne beide Möglichkeiten aus.', '36 : (4 · 3) = 36 : 12 = 3. Ohne Klammern rechnet man von links: 36 : 4 · 3 = 9 · 3 = 27.')),
            (3, lambda R: zahl('Berechne geschickt: 1,25 · 0,8 · 2,5 · 0,4 · 3,7', Fr('3.7'), '1.25 * 0.8 * 2.5 * 0.4 * 3.7',
                               'Suche Paare, die 1 ergeben.', '1,25 · 0,8 = 1 und 2,5 · 0,4 = 1. 1 · 1 · 3,7 = 3,7.')),
            (3, lambda R: wahl(R, 'Ein Kind rechnet 60 : 6 : 2 = 60 : 3 = 20. Was stimmt?', 'Falsch: Beim Teilen darf man nicht umklammern. 60 : 6 : 2 = 10 : 2 = 5.',
                               ['Richtig.', 'Falsch: Das Ergebnis ist 10.', 'Falsch: Das Ergebnis ist 180.'],
                               'Rechne von links nach rechts.', '60 : 6 = 10, 10 : 2 = 5. Das Kind hat 6 : 2 zuerst gerechnet – beim Teilen ist das nicht erlaubt.')),
            (3, lambda R: zahl('Welche Zahl gehört in das Kästchen? 3/4 · □ · 4/3 · 0,5 = 6', 12, '6 / ((3/4) * (4/3) * 0.5)',
                               'Fasse zuerst die bekannten Faktoren geschickt zusammen.', '3/4 · 4/3 = 1, also bleibt □ · 0,5 = 6. □ = 6 : 0,5 = 12.')),
        ],
        'gemischt': [
            (2, lambda R: zahl('Berechne 2,5 − 0,5 · 1,4.', Fr('1.8'), '2.5 - 0.5 * 1.4', 'Punkt vor Strich.', '0,5 · 1,4 = 0,7. 2,5 − 0,7 = 1,8.')),
            (2, lambda R: zahl('Berechne (3/4 − 1/2) : 1/8.', 2, '(3/4 - 1/2) / (1/8)', 'Zuerst die Klammer.', '3/4 − 1/2 = 1/4. 1/4 : 1/8 = 1/4 · 8 = 2.')),
            (3, lambda R: zahl('Für den Mittelwert von 52 und 60 tippt ein Kind in den Rechner: 52 + 60 : 2. Welche Zahl zeigt der Rechner an?', 82, '52 + 60 / 2',
                               'Der Rechner beachtet Punkt vor Strich.', 'Der Rechner teilt zuerst: 60 : 2 = 30, dann 52 + 30 = 82. Für den Mittelwert braucht man (52 + 60) : 2 = 56.')),
            (3, lambda R: zahl('Multipliziere die Differenz von 4,5 und 1,5 mit der Summe aus 0,2 und 0,3.', Fr('1.5'), '(4.5 - 1.5) * (0.2 + 0.3)',
                               'Differenz und Summe kommen in Klammern.', '(4,5 − 1,5) · (0,2 + 0,3) = 3 · 0,5 = 1,5.')),
            (3, lambda R: wahl(R, 'Welches Rechenzeichen gehört in das Kästchen? 1/2 □ 1/4 = 2', ':', ['·', '+', '−'],
                               'Probiere alle vier Rechenarten aus.', '1/2 : 1/4 = 1/2 · 4 = 2. (1/2 · 1/4 = 1/8, 1/2 + 1/4 = 3/4, 1/2 − 1/4 = 1/4.)')),
            (3, lambda R: zahl('Eine Familie kauft 3 Kinokarten zu je 8 € und 2 Getränke zu je 2,80 €. Auf die Karten gibt es 1/4 Nachlass. Wie viel Euro zahlt sie?',
                               Fr('23.6'), '3 * 8 * 3/4 + 2 * 2.8', 'Der Nachlass gilt nur für die Karten. Nach dem Nachlass bleiben 3/4 des Kartenpreises.',
                               'Karten: 3 · 8 € = 24 €, davon 3/4 = 18 €. Getränke: 2 · 2,80 € = 5,60 €. Zusammen 23,60 €.', einheit='€')),
        ],
        'fehler_finden': [
            (2, lambda R: zahl('Ein Kind rechnet 0,3 · 0,2 = 0,6. Wie heißt das richtige Ergebnis?', Fr('0.06'), '0.3 * 0.2', 'Zähle die Nachkommastellen beider Faktoren.',
                               '3 · 2 = 6, zwei Nachkommastellen: 0,06.')),
            (2, lambda R: wahl(R, 'Ein Kind rechnet 3/5 − 1/3 = 2/2 = 1. Was ist der Fehler?', 'Zähler und Nenner wurden einzeln abgezogen. Richtig ist 4/15.',
                               ['Es gibt keinen Fehler.', 'Man hätte die Nenner addieren müssen: 2/8.', 'Man hätte den Kehrbruch nehmen müssen.'],
                               'Kann das Ergebnis größer sein als 3/5?', '3/5 − 1/3 = 9/15 − 5/15 = 4/15. Das Ergebnis 1 ist sogar größer als 3/5.')),
            (3, lambda R: wahl(R, 'Ein Kind gibt für 4,2 · 0,35 das Ergebnis 14,7 an. Mache einen Überschlag. Welches Ergebnis stimmt?', '1,47', ['14,7', '0,147', '147'],
                               'Überschlag: 4 · 0,35 ist etwa 4 · 1/3.', '4 · 0,35 = 1,4, also etwa 1,4. 42 · 35 = 1 470, drei Nachkommastellen: 1,470 = 1,47.')),
            (3, lambda R: zahl('Ein Kind rechnet 7,2 : 0,9 = 0,8. Wie heißt das richtige Ergebnis?', 8, '7.2 / 0.9',
                               'Durch eine Zahl kleiner als 1 teilen macht größer. Verschiebe bei beiden Zahlen das Komma.', '7,2 : 0,9 = 72 : 9 = 8. Das Ergebnis muss größer als 7,2 sein.')),
            (3, lambda R: zahl('Ein Kind sollte eine Zahl mit 0,5 malnehmen. Aus Versehen hat es durch 0,5 geteilt und 18 erhalten. Welches Ergebnis wäre richtig gewesen?',
                               Fr('4.5'), '18 * 0.5 * 0.5', 'Finde zuerst die Zahl: Rechne das Teilen durch 0,5 rückwärts.',
                               'Die Zahl ist 18 · 0,5 = 9 (denn 9 : 0,5 = 18). Richtig wäre 9 · 0,5 = 4,5.')),
            (3, lambda R: zahl('Ein Kind rechnet 2 − 1/3 · 3 = 5/3 · 3 = 5. Wie heißt das richtige Ergebnis?', 1, '2 - (1/3) * 3', 'Punkt vor Strich.',
                               'Zuerst 1/3 · 3 = 1. Dann 2 − 1 = 1. Das Kind hat zuerst subtrahiert.')),
        ],
    }


ergaenzen(DATEI, _rr(), seed=6023)


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('bruch.rechnen', 13_6_4)
# a) Stufe 1–2
BF.stufe('brueche_plus_minus', 'Berechne 1/2 + 1/2 − 2/5.', 2)
# c) Ablenker „0/13“ ist kein üblich geschriebener Bruch → „0“
BF.ersetze('vorzeichen', 'Berechne (−1/8) + 1/5.', BF.A(
    'Berechne (−1/8) + 1/5 und gib das Ergebnis vollständig gekürzt an.', '3/40', ['−3/40', '0', '−13/40'],
    'Hauptnenner 40: −5/40 + 8/40 = 3/40. (Zähler und Nenner einzeln addieren ergäbe 0/13 = 0 – das ist falsch.)',
    'Gleichnamig machen, dann wie bei ganzen Zahlen rechnen.'))
# c) Preis unrealistisch niedrig (0,28 € je kg Äpfel)
BF.ersetze('dezimal_mal', 'Ein Kilogramm Äpfel kostet 0,28 €. Was kosten 5,2 kg? Runde auf Cent.', BF.Z(
    'Ein Kilogramm Äpfel kostet 2,79 €. Was kosten 1,6 kg? Runde auf Cent.', 4.46, '((2.79) * (1.6) * 100 + 1/2) // 1 / 100',
    '2,79 · 1,6 = 4,464 €, gerundet 4,46 €.', 'Preis pro kg mal Anzahl kg. Am Ende auf zwei Nachkommastellen runden.', einheit='€'))
BF.nicht_umgesetzt('brueche_plus_minus S2 „Ergänze: 1/2 − □/□ = 1/4“ nicht eindeutig (2/8, 3/12 …)', 'Der Hinweis „Vollständig gekürzt“ steht bereits in der Aufgabe; damit ist nur 1/4 richtig.')
BF.nicht_umgesetzt('gemischt S3 „3/2 · 2/5 − 1/4 · 5/2 …“ mit negativem Ergebnis', 'Laut Befund in Ordnung (Vorzeichen-Karte kommt vorher).')

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----


# ---------- LUECKEN (Achtzehnte Runde, Teil B, Zweig luecken-kl6) ----------
# Läuft nach allen bisherigen Abschnitten mit eigenem Zufallsstart; vorhandene Karten und Aufgaben bleiben unverändert.
# Lehrplan: LehrplanPLUS Gymnasium Bayern M6 1.3/1.4 (gemischte Zahlen addieren, subtrahieren, multiplizieren, dividieren; Potenzen mit
# natürlichen Exponenten und rationalen Grundzahlen), M6 1.5 (Sachprobleme mit „Anteilen von Anteilen“, Skizze, Überschlag).
# Prüfungsvorbilder: Bayerischer Mathematik-Test Jgst. 8 (ISB) 2021 Aufg. 1 (gehört das Minus zur Basis?), 2023 Aufg. 1c (Potenz eines Bruchs),
# 2014 Gruppe B Aufg. 1c (Anteil vom Anteil), 2023 Aufg. 5a (Restanteil); Grundwissentest Jgst. 7 der Realschule (ISB) 2015 Nr. 1, 2017 Nr. 1
# (Rechnen mit gemischten Zahlen), 2024 Nr. 3 (fehlende Punkte aus einem Anteil).
from _luecken_kl6 import karte_neu, karte_erweitern, zahl, wahl, gemischt, bruch as lbruch  # noqa: E402


def _gitter(flaeche=None):
    """Quadrat 1 m × 1 m in 4 · 4 Kästchen; flaeche: Liste von Eckpunkten (Hilfspunkte) für die gefärbte Fläche."""
    P = {}
    for i in range(5):
        for j in range(5):
            P[f'_{i}_{j}'] = [float(i), float(j)]
    L = [[f'_{i}_0', f'_{i}_4'] for i in range(5)] + [[f'_0_{j}', f'_4_{j}'] for j in range(5)] + [['_0_0', '_4_0', '1 m']]
    b = {'typ': 'figur', 'punkte': P, 'linien': L}
    if flaeche: b['flaeche'] = flaeche
    return b


_POT = {
    'lernziel': 'potenzen', 'titel': 'Potenzen von Brüchen und Dezimalzahlen',
    'einstieg': 'Ein quadratisches Beet ist 3/4 m lang und 3/4 m breit. Für die Fläche rechnest du 3/4 · 3/4. Kurz schreibt man (3/4)², eine ⟦Potenz⟧.',
    'woerter': [['Potenz', 'ein Produkt aus lauter gleichen Faktoren, kurz geschrieben: (3/4)² = 3/4 · 3/4'],
                ['Basis', 'die Zahl, die malgenommen wird; bei (3/4)² ist das 3/4'],
                ['Exponent', 'die kleine Zahl oben: wie oft die Basis als Faktor vorkommt']],
    'bild': _gitter(),
    'schritte': [
        {'text': 'Ein Quadrat mit 1 m Seite hat hier 16 gleiche Kästchen.'},
        {'text': 'Das Beet ist 3 mal 3 Kästchen groß: 9 von 16.', 'bild': {'flaeche': ['_0_0', '_3_0', '_3_3', '_0_3']}},
        {'text': 'Also ist (3/4)² = (3 · 3)/(4 · 4) = ⟦9/16⟧ m².'},
        {'text': 'Die Basis ist 3/4, der Exponent 2. Er zählt die Faktoren.'},
        {'text': 'Mit Dezimalzahl: 0,5³ = 0,5 · 0,5 · 0,5 = ⟦0,125⟧.'},
    ],
    'fehler': '(3/4)² ist nicht 6/8. Das wäre 3/4 · 2, also 12 Kästchen. Das Beet hat aber nur 9 Kästchen.',
    'fehler_bild': {'flaeche': ['_0_0', '_3_0', '_3_4', '_0_4']},
    'regel': 'Der ⟦Exponent⟧ sagt, wie oft die Basis malgenommen wird. Bei Brüchen: Zähler mal Zähler, Nenner mal Nenner.',
    'probe': '9/16 ist kleiner als 3/4 = 12/16. Mal eine Zahl kleiner als 1 macht kleiner.',
}


def _pot_aufgaben():
    U = 'uebung'
    def b(t, E, h, w): return lambda R: lbruch(t, E, h, w)
    def z(t, v, c, h, w): return lambda R: zahl(t, v, c, h, w)
    ZN = 'Zähler mit sich selbst malnehmen, Nenner mit sich selbst malnehmen.'
    KS = 'Rechne ohne Komma und zähle dann alle Nachkommastellen zusammen.'
    return [
        (U, 1, b('Berechne (2/3)².', '(2/3)**2', ZN, '(2 · 2)/(3 · 3) = 4/9.')),
        (U, 1, z('Berechne 0,3².', Fr('0.09'), '0.3**2', KS, '0,3 · 0,3: 3 · 3 = 9, zwei Nachkommastellen: 0,09.')),
        (U, 1, b('Berechne (1/2)³.', '(1/2)**3', 'Dreimal 1/2 als Faktor.', '1/2 · 1/2 · 1/2 = 1/8.')),
        (U, 1, z('Berechne 1,5².', Fr('2.25'), '1.5**2', KS, '15 · 15 = 225, zwei Nachkommastellen: 2,25.')),
        (U, 2, b('Berechne (−3/5)².', '(-3/5)**2', 'Minus mal Minus ergibt Plus.', '(−3/5) · (−3/5) = 9/25.')),
        (U, 2, z('Berechne (−0,2)³.', Fr('-0.008'), '(-0.2)**3', 'Drei negative Faktoren: Das Ergebnis ist negativ.', '0,2 · 0,2 · 0,2 = 0,008. Drei Minuszeichen: −0,008.')),
        (U, 2, b('Berechne (2/5)³.', '(2/5)**3', ZN, '(2 · 2 · 2)/(5 · 5 · 5) = 8/125.')),
        (U, 2, z('Berechne 0,1⁴.', Fr('0.0001'), '0.1**4', 'Jeder Faktor 0,1 schiebt das Komma eine Stelle nach links.', '0,1 · 0,1 · 0,1 · 0,1 = 0,0001.')),
        (U, 2, b('Berechne (1 1/2)². Gib das Ergebnis als Bruch an.', '(3/2)**2', 'Schreibe 1 1/2 zuerst als unechten Bruch.', '1 1/2 = 3/2. (3/2)² = 9/4.')),
        (U, 2, z('Berechne (−1,2)².', Fr('1.44'), '(-1.2)**2', 'Gerader Exponent: Das Ergebnis ist positiv.', '12 · 12 = 144, zwei Nachkommastellen: 1,44. Positiv, weil (−) · (−) = (+).')),
        (U, 3, z('Berechne −0,5² + (−0,5)².', 0, '-(0.5**2) + (-0.5)**2', 'Bei −0,5² gehört das Minus nicht zur Basis.',
                 '−0,5² = −(0,5 · 0,5) = −0,25. (−0,5)² = 0,25. Zusammen 0.')),
        (U, 3, b('Berechne (2/3)² · (3/2)³.', '(2/3)**2 * (3/2)**3', 'Schreibe alle Faktoren aus und kürze vor dem Ausrechnen.',
                 '4/9 · 27/8 = 108/72 = 3/2. Mit Kürzen: zwei Paare 2/3 · 3/2 ergeben 1, übrig bleibt 3/2.')),
        (U, 3, lambda R: wahl(R, 'Welche Zahl ist größer: (1/2)³ oder (1/3)²?', '(1/2)³', ['(1/3)²', 'Beide sind gleich groß.'],
                              'Rechne beide Potenzen als Bruch aus und vergleiche.', '(1/2)³ = 1/8 und (1/3)² = 1/9. 1/8 ist größer als 1/9.', n=3)),
        (U, 3, lambda R: wahl(R, 'Für welche Zahl ist das Quadrat kleiner als die Zahl selbst?', '0,5', ['2', '1', '1,5'],
                              'Rechne für jede Zahl das Quadrat aus.', '0,5² = 0,25 < 0,5. Dagegen 2² = 4, 1² = 1 (gleich), 1,5² = 2,25.')),
        (U, 3, b('Ein Kind rechnet (2/5)² = 4/5. Wie heißt das richtige Ergebnis?', '(2/5)**2', 'Auch der Nenner wird mit sich selbst malgenommen.',
                 '(2 · 2)/(5 · 5) = 4/25. Das Kind hat nur den Zähler quadriert.')),
        (U, 3, z('Ein Kind rechnet 0,2³ = 0,6. Wie heißt das richtige Ergebnis?', Fr('0.008'), '0.2**3', 'Potenz heißt malnehmen, nicht mal den Exponenten.',
                 '0,2 · 0,2 · 0,2 = 0,008. Das Kind hat 0,2 · 3 gerechnet.')),
        (U, 3, b('Ein Blatt Papier wird dreimal halbiert. Welcher Bruchteil des Blattes ist ein Stück?', '(1/2)**3',
                 'Jedes Halbieren nimmt die Hälfte vom vorigen Stück.', '1/2 · 1/2 · 1/2 = (1/2)³ = 1/8.')),
        (U, 3, lambda R: wahl(R, 'Welche Zahl ist negativ?', '(−1/2)³', ['(−1/2)²', '(−1/2)⁴', '(1/2)³'],
                              'Zähle die Minuszeichen: gerade Anzahl gibt Plus, ungerade Minus.', '(−1/2)³ = −1/8. Bei den Exponenten 2 und 4 wird es positiv, (1/2)³ ist ohnehin positiv.')),
        ('test', 2, b('Berechne (4/5)².', '(4/5)**2', '', '(4 · 4)/(5 · 5) = 16/25.')),
        ('korrektur', 2, z('Berechne 0,7².', Fr('0.49'), '0.7**2', '', '7 · 7 = 49, zwei Nachkommastellen: 0,49.')),
        ('korrektur', 2, b('Berechne (−1/3)³.', '(-1/3)**3', '', '(−1/3) · (−1/3) · (−1/3) = −1/27. Drei Minuszeichen ergeben Minus.')),
        ('korrektur', 2, z('Berechne 2,5².', Fr('6.25'), '2.5**2', '', '25 · 25 = 625, zwei Nachkommastellen: 6,25.')),
        ('sicherung', 2, b('Berechne (5/6)².', '(5/6)**2', '', '(5 · 5)/(6 · 6) = 25/36.')),
        ('sicherung', 2, z('Berechne 0,4³.', Fr('0.064'), '0.4**3', '', '4 · 4 · 4 = 64, drei Nachkommastellen: 0,064.')),
        ('sicherung', 2, b('Berechne (−2/3)².', '(-2/3)**2', '', '(−2/3) · (−2/3) = 4/9. Minus mal Minus ergibt Plus.')),
        ('sicherung', 2, z('Berechne (−0,3)².', Fr('0.09'), '(-0.3)**2', '', '(−0,3) · (−0,3) = 0,09.')),
        ('sicherung', 2, b('Berechne (3/2)³.', '(3/2)**3', '', '(3 · 3 · 3)/(2 · 2 · 2) = 27/8.')),
        ('sicherung', 2, z('Berechne 1,1².', Fr('1.21'), '1.1**2', '', '11 · 11 = 121, zwei Nachkommastellen: 1,21.')),
    ]


_SACH = {
    'lernziel': 'sach', 'titel': 'Sachaufgaben: Anteile von Anteilen',
    'einstieg': '2/3 der Klasse fahren mit zum Ausflug. Von ihnen kommen 3/4 mit dem Rad. Welcher Teil der ganzen Klasse radelt? Das ist ein ⟦Anteil vom Anteil⟧.',
    'woerter': [['Anteil vom Anteil', 'ein Bruchteil von einem Bruchteil: 3/4 von 2/3 heißt 3/4 · 2/3'],
                ['Überschlag', 'schnelle Probe mit runden Zahlen: Kann das Ergebnis stimmen?']],
    'bild': {'typ': 'bruchstreifen', 'teile': 3, 'gefaerbt': 2, 'ganzes': 'Klasse', 'teil_text': '2/3 fahren mit'},
    'schritte': [
        {'text': 'Zeichne die Klasse als Streifen. 2 von 3 Teilen fahren mit.'},
        {'text': 'Teile jedes Drittel in 4 Stücke. Mitfahrer sind 8 von 12.',
         'bild': {'zeilen': [{'teile': 12, 'gefaerbt': 8, 'teil_text': '8/12 fahren mit'}]}},
        {'text': '3/4 der 8 Stücke radeln, also 6 Stücke.', 'bild': {'zeilen': [{'teile': 12, 'gefaerbt': 6, 'teil_text': '6/12 radeln'}]}},
        {'text': '3/4 · 2/3 = 6/12 = ⟦1/2⟧. Die Hälfte der Klasse radelt.'},
        {'text': 'Überschlag: etwas weniger als 2/3 – das passt.'},
    ],
    'fehler': '3/4 von 2/3 ist nicht 3/4 der Klasse. Die 3/4 gelten nur für die Mitfahrer, nicht für alle.',
    'fehler_bild': {'zeilen': [{'teile': 4, 'gefaerbt': 3, 'teil_text': '3/4 der Klasse: falsch'}]},
    'regel': '„Von“ heißt ⟦mal⟧: 3/4 von 2/3 = 3/4 · 2/3. Mach eine Skizze und prüfe mit einem Überschlag.',
    'probe': '1/2 der Klasse ist weniger als 2/3 der Klasse – es fahren ja nicht alle Mitfahrer Rad.',
}


def _sach_aufgaben():
    U = 'uebung'
    def b(t, E, h, w): return lambda R: lbruch(t, E, h, w)
    def z(t, v, c, h, w, e=None): return lambda R: zahl(t, v, c, h, w, einheit=e)
    VON = '„Von“ heißt mal.'
    return [
        (U, 1, b('Wie viel ist 1/2 von 1/3?', '1/2 * 1/3', VON, '1/2 · 1/3 = 1/6.')),
        (U, 1, b('Wie viel ist 2/3 von 3/5?', '2/3 * 3/5', VON, '2/3 · 3/5 = 6/15 = 2/5.')),
        (U, 1, b('Eine halbe Pizza wird geviertelt. Welcher Bruchteil der ganzen Pizza ist ein Stück?', '1/4 * 1/2', 'Ein Stück ist 1/4 von 1/2.', '1/4 · 1/2 = 1/8.')),
        (U, 1, b('Wie viel ist 3/5 von 5/6?', '3/5 * 5/6', VON + ' Kürze vor dem Ausrechnen.', '3/5 · 5/6 = 15/30 = 1/2.')),
        (U, 2, z('Von 60 Kindern spielen 2/5 Fußball. Davon ist 1/3 Mädchen. Wie viele Mädchen spielen Fußball?', 8, '60 * 2/5 * 1/3',
                 'Rechne zuerst, wie viele Kinder Fußball spielen.', '2/5 von 60 = 24 Kinder. 1/3 von 24 = 8 Mädchen.')),
        (U, 2, b('4/5 der Kinder essen in der Mensa. Davon wählen 3/8 das Nudelgericht. Welcher Anteil aller Kinder isst Nudeln?', '3/8 * 4/5',
                 'Anteil vom Anteil: malnehmen.', '3/8 · 4/5 = 12/40 = 3/10.')),
        (U, 2, z('Ein Kuchen wiegt 1,2 kg. 3/4 werden verkauft. Der Rest wird halbiert. Wie viel Gramm wiegt eine Hälfte des Rests?', 150,
                 '1200 * (1 - 3/4) / 2', 'Welcher Anteil bleibt übrig? Rechne in Gramm.', '1,2 kg = 1 200 g. Rest 1/4 = 300 g. Die Hälfte: 150 g.', 'g')),
        (U, 2, z('Eine Flasche enthält 1,5 l Saft. 2/3 davon werden getrunken. Wie viele Liter bleiben?', Fr('0.5'), '1.5 * (1 - 2/3)',
                 'Es bleibt 1/3 übrig.', '1/3 von 1,5 l = 0,5 l.', 'l')),
        (U, 2, b('Die Hälfte eines Gartens ist Rasen. Auf 1/5 des Rasens stehen Bäume. Welcher Anteil des ganzen Gartens ist das?', '1/5 * 1/2',
                 'Anteil vom Anteil: 1/5 von 1/2.', '1/5 · 1/2 = 1/10.')),
        (U, 2, lambda R: wahl(R, 'Mache einen Überschlag: Etwa wie viel kosten 2,9 kg Äpfel zu 1,95 € je kg?', 'etwa 6 €', ['etwa 60 €', 'etwa 0,60 €', 'etwa 3 €'],
                              'Runde beide Zahlen auf Ganze.', '2,9 ≈ 3 und 1,95 ≈ 2. 3 · 2 = 6, also etwa 6 € (genau 5,66 €).')),
        (U, 3, b('3/5 der Besucher eines Zoos sind Kinder. 2/3 dieser Kinder gehen ins Affenhaus. Welcher Anteil aller Besucher sind Kinder im Affenhaus?',
                 '2/3 * 3/5', 'Die 2/3 beziehen sich nur auf die Kinder.', '2/3 · 3/5 = 6/15 = 2/5 aller Besucher.')),
        (U, 3, b('Ein Kind gibt 1/3 seines Taschengelds fürs Kino und 1/4 für Süßes aus. Vom Rest spart es die Hälfte. Welcher Anteil wird gespart?',
                 '(1 - 1/3 - 1/4) / 2', 'Rechne zuerst den Rest aus. Hauptnenner 12.', 'Rest: 1 − 4/12 − 3/12 = 5/12. Die Hälfte davon: 5/24.')),
        (U, 3, z('Ein Test hat Teil A und Teil B mit je 24 Punkten. Ein Kind schafft 5/6 von Teil A und 3/4 von Teil B. Wie viele Punkte fehlen ihm zur vollen Punktzahl?',
                 10, '48 - 24 * 5/6 - 24 * 3/4', 'Rechne die Punkte in jedem Teil aus.', 'A: 5/6 von 24 = 20. B: 3/4 von 24 = 18. 48 − 38 = 10 Punkte fehlen.')),
        (U, 3, z('Von einer Tafel Schokolade isst Lea die Hälfte. Tom isst 1/3 vom Rest, Mia die Hälfte des neuen Rests. Es bleiben 2 Stückchen. '
                 'Wie viele Stückchen hatte die Tafel?', 12, '2 / ((1 - 1/2) * (1 - 1/3) * (1 - 1/2))',
                 'Rechne rückwärts oder bestimme, welcher Anteil der Tafel am Ende übrig ist.',
                 'Übrig: 1/2 · 2/3 · 1/2 = 1/6 der Tafel. 1/6 sind 2 Stückchen, also hatte die Tafel 12.')),
        (U, 3, z('2/3 von 3/4 einer Wanderstrecke sind 12 km. Wie lang ist die ganze Strecke?', 24, '12 / (2/3 * 3/4)',
                 'Welcher Anteil der ganzen Strecke sind 2/3 von 3/4?', '2/3 · 3/4 = 1/2. Die Hälfte sind 12 km, also 24 km.', 'km')),
        (U, 3, lambda R: wahl(R, 'Ein Kind rechnet: „1/2 von 1/4 = 1/2 + 1/4 = 3/4.“ Was stimmt?', 'Falsch: „von“ heißt mal, 1/2 · 1/4 = 1/8.',
                              ['Richtig.', 'Falsch: 1/2 von 1/4 = 2/6.', 'Falsch: 1/2 von 1/4 = 2.'],
                              'Mach eine Skizze: die Hälfte von einem Viertel.', 'Die Hälfte eines Viertels ist ein Achtel. 3/4 wäre sogar mehr als 1/4 – das kann nicht sein.')),
        (U, 3, z('Ein Kind rechnet: 2/3 von 3/4 von 600 € sind 1 200 €. Mache einen Überschlag. Wie viel Euro ist es richtig?', 300, '600 * 3/4 * 2/3',
                 'Ein Anteil von 600 € kann nicht mehr als 600 € sein.', '3/4 von 600 € = 450 €. 2/3 von 450 € = 300 €.', '€')),
        (U, 3, z('Ein Radladen hat 120 Räder. 3/8 davon sind E-Bikes, und 2/5 der E-Bikes sind Lastenräder. Wie viele E-Bikes sind keine Lastenräder?', 27,
                 '120 * 3/8 * (1 - 2/5)', 'Rechne zuerst die E-Bikes aus.', '3/8 von 120 = 45 E-Bikes. 2/5 von 45 = 18 Lastenräder. 45 − 18 = 27.')),
        ('test', 2, b('Wie viel ist 2/5 von 5/8?', '2/5 * 5/8', '', '2/5 · 5/8 = 10/40 = 1/4.')),
        ('korrektur', 2, b('Wie viel ist 3/4 von 2/9?', '3/4 * 2/9', '', '3/4 · 2/9 = 6/36 = 1/6.')),
        ('korrektur', 2, z('Wie viel Euro sind 1/3 von 3/5 von 50 €?', 10, '50 * 3/5 * 1/3', '', '3/5 von 50 € = 30 €. 1/3 von 30 € = 10 €.', '€')),
        ('korrektur', 2, b('Wie viel ist 5/6 von 3/10?', '5/6 * 3/10', '', '5/6 · 3/10 = 15/60 = 1/4.')),
        ('sicherung', 2, b('Wie viel ist 1/3 von 3/4?', '1/3 * 3/4', '', '1/3 · 3/4 = 3/12 = 1/4.')),
        ('sicherung', 2, z('Wie viele Meter sind 2/3 von 1/2 von 90 m?', 30, '90 * 1/2 * 2/3', '', '1/2 von 90 m = 45 m. 2/3 von 45 m = 30 m.', 'm')),
        ('sicherung', 2, b('Wie viel ist 4/7 von 7/8?', '4/7 * 7/8', '', '4/7 · 7/8 = 28/56 = 1/2.')),
        ('sicherung', 2, z('Wie viel Gramm sind 3/4 von 2/5 von 200 g?', 60, '200 * 2/5 * 3/4', '', '2/5 von 200 g = 80 g. 3/4 von 80 g = 60 g.', 'g')),
        ('sicherung', 2, b('Wie viel ist 1/2 von 4/5?', '1/2 * 4/5', '', '1/2 · 4/5 = 4/10 = 2/5.')),
        ('sicherung', 2, z('Wie viele Kinder sind 1/4 von 2/3 von 120 Kindern?', 20, '120 * 2/3 * 1/4', '', '2/3 von 120 = 80. 1/4 von 80 = 20.')),
    ]


def _gem_rechnen(lz):
    g = lambda t, E, h, w: (lambda R: gemischt(t, E, h, w))
    MG = 'Schreibe die gemischten Zahlen zuerst als unechte Brüche. Das Ergebnis wieder als gemischte Zahl.'
    return {
        'brueche_plus_minus': [
            (None, 2, g('Berechne 1 1/2 + 2 1/3. Gib das Ergebnis als gemischte Zahl an.', '3/2 + 7/3', MG,
                        'Ganze: 1 + 2 = 3. Brüche: 1/2 + 1/3 = 3/6 + 2/6 = 5/6. Zusammen 3 5/6.')),
            (None, 3, g('Berechne 4 1/5 − 1 3/4. Gib das Ergebnis als gemischte Zahl an.', '21/5 - 7/4', MG + ' Hauptnenner 20.',
                        '21/5 − 7/4 = 84/20 − 35/20 = 49/20 = 2 9/20.')),
        ],
        'brueche_mal': [
            (None, 2, g('Berechne 2 1/4 · 2/3. Gib das Ergebnis als gemischte Zahl an.', '9/4 * 2/3', MG,
                        '2 1/4 = 9/4. 9/4 · 2/3 = 18/12 = 3/2 = 1 1/2.')),
            (None, 3, g('Berechne 1 1/2 · 1 2/3. Gib das Ergebnis als gemischte Zahl an.', '3/2 * 5/3', MG + ' Achtung: Nicht Ganze mal Ganze und Bruch mal Bruch!',
                        '3/2 · 5/3 = 15/6 = 5/2 = 2 1/2. (1 · 1 + 1/2 · 2/3 = 1 1/3 wäre falsch.)')),
        ],
        'brueche_geteilt': [
            (None, 2, g('Berechne 3 1/2 : 2/3. Gib das Ergebnis als gemischte Zahl an.', '7/2 / (2/3)', MG,
                        '3 1/2 = 7/2. 7/2 · 3/2 = 21/4 = 5 1/4.')),
            (None, 3, g('Berechne 2 1/4 : 1 1/2. Gib das Ergebnis als gemischte Zahl an.', '9/4 / (3/2)', MG,
                        '9/4 : 3/2 = 9/4 · 2/3 = 18/12 = 3/2 = 1 1/2.')),
        ],
    }[lz]


for _i, _lz in enumerate(('brueche_plus_minus', 'brueche_mal', 'brueche_geteilt')):
    karte_erweitern(DATEI, _lz, _gem_rechnen(_lz), seed=6191 + _i)
karte_neu(DATEI, _POT, _pot_aufgaben(), seed=6194, nach='dezimal_geteilt', teil_text='Potenzen mit Bruch oder Dezimalzahl als Basis berechnen')
karte_neu(DATEI, _SACH, _sach_aufgaben(), seed=6195, nach='fehler_finden', teil_text='Sachaufgaben mit Anteilen von Anteilen lösen')



# ---------- DURCHSICHT (Neunzehnte Runde, Teil A, Zweig durchsicht-kl6) ----------
# Stufen nach dem Gedanken: S1 = Beispiel mit anderen Zahlen, S2 = Abwandlung/Einkleidung/Umkehrung, S3 = anderer Gedanke.
from _durchsicht_kl6 import Befunde, befunde_anwenden  # noqa: E402

DS = Befunde('bruch.rechnen', 19_6_3)
_S = DS.stufe
# brueche_plus_minus: Ganze minus zwei Brüche (dreimal gleich gebaut) und Summe gemischter Zahlen = Abwandlung → S2
for _t in ('Berechne 3 − 1/8 − 6/7.', 'Berechne 3 − 2/3 − 3/5.', 'Berechne 3 − 8/9 − 3/7.', 'Berechne 2 1/3 + 3 1/6. Gib das Ergebnis als Bruch an.'):
    _S('brueche_plus_minus', _t, 2)
# dezimal_plus_minus: Rückgeld (viermal gleich gebaut) und „Wie viel fehlt?“ = Einkleidung bzw. Umkehrung → S2
for _t in ('Ein Einkauf kostet 6,47 €, 8,34 €, 8,66 €. Bezahlt wird mit einem 100-€-Schein. Wie viel Euro gibt es zurück?',
           'Ein Einkauf kostet 0,84 €, 6,47 €, 8,76 €. Bezahlt wird mit einem 50-€-Schein. Wie viel Euro gibt es zurück?',
           'Ein Einkauf kostet 7,51 €, 8,49 €, 12,07 €. Bezahlt wird mit einem 100-€-Schein. Wie viel Euro gibt es zurück?',
           'Ein Einkauf kostet 0,72 €, 6,46 €, 13,74 €. Bezahlt wird mit einem 100-€-Schein. Wie viel Euro gibt es zurück?',
           'Wie viel fehlt von 2,837 bis 5,8?', 'Wie viel fehlt von 4,8 bis 8,164?'):
    _S('dezimal_plus_minus', _t, 2)
# vorzeichen: Kontostand = Einkleidung; Teilen mit Vorzeichen und Addieren mit Hauptnenner = dieselbe Regel wie S2 → S2
for _t in ('Ein Konto steht auf −32,39 €. Es werden 18,12 € eingezahlt und danach 34,12 € abgebucht. Wie ist der neue Kontostand?',
           'Berechne (−2/3) : (−4/5).', 'Berechne (−5/6) : (−2/3).', 'Berechne (−1/4) + 2/7.',
           'Berechne (−1/8) + 1/5 und gib das Ergebnis vollständig gekürzt an.', 'Berechne (−3/5) : 1/4.'):
    _S('vorzeichen', _t, 2)
# brueche_mal: Rechteckfläche und „Flasche … davon getrunken“ = Bruch · Bruch eingekleidet → S2
for _t in ('Ein Rechteck ist 2/3 m lang und 1/3 m breit. Wie groß ist sein Flächeninhalt in m²?', 'Ein Rechteck ist 3/4 m lang und 4/5 m breit. Wie groß ist sein Flächeninhalt in m²?',
           'In einer Flasche sind 1/5 l Saft. Davon wird 2/3 getrunken. Wie viele Liter sind das?', 'In einer Flasche sind 2/5 l Saft. Davon wird 1/2 getrunken. Wie viele Liter sind das?',
           'In einer Flasche sind 3/8 l Saft. Davon wird 1/5 getrunken. Wie viele Liter sind das?', 'In einer Flasche sind 1/4 l Saft. Davon wird 1/2 getrunken. Wie viele Liter sind das?'):
    _S('brueche_mal', _t, 2)
# brueche_geteilt: Gläser füllen und Rechteckseite aus Fläche = Teilen eingekleidet → S2
for _t in ('Wie viele Gläser zu je 3/4 l kann man aus 15/4 l Saft füllen?', 'Ein Rechteck hat den Flächeninhalt 1/6 m² und ist 1/3 m breit. Wie lang ist es?',
           'Ein Rechteck hat den Flächeninhalt 5/28 m² und ist 5/7 m breit. Wie lang ist es?', 'Ein Rechteck hat den Flächeninhalt 8/15 m² und ist 2/3 m breit. Wie lang ist es?'):
    _S('brueche_geteilt', _t, 2)
# dezimal_mal: Nachkommastellen zählen als Auswahl und Preis · Menge = S2
for _t in ('Was ergibt 0,7 · 0,05?', 'Was ergibt 0,4 · 0,04?', 'Was ergibt 0,2 · 0,05?', 'Ein Kilogramm Äpfel kostet 2,79 €. Was kosten 1,6 kg? Runde auf Cent.',
           'Ein Kilogramm Äpfel kostet 2,75 €. Was kosten 3,3 kg? Runde auf Cent.', 'Ein Kilogramm Äpfel kostet 1,94 €. Was kosten 4,3 kg? Runde auf Cent.'):
    _S('dezimal_mal', _t, 2)
# dezimal_geteilt: Auswahl, Band abschneiden, gerecht teilen und runden = S2
for _t in ('Was ergibt 2,07 : 0,09?', 'Eine Rolle Band ist 3,5 m lang. Wie viele Stücke von 0,25 m Länge kann man abschneiden?',
           'Eine Rolle Band ist 5,5 m lang. Wie viele Stücke von 0,25 m Länge kann man abschneiden?', '9 Kinder teilen sich 57 € gerecht. Wie viel Euro bekommt jedes Kind? Runde auf ganze Cent.',
           '9 Kinder teilen sich 84 € gerecht. Wie viel Euro bekommt jedes Kind? Runde auf ganze Cent.', 'Berechne 47 : 7 und runde auf zwei Nachkommastellen.'):
    _S('dezimal_geteilt', _t, 2)
# rechenvorteile: „Teilen nicht umklammern“ viermal hintereinander = die Falle der Karte direkt; lange Produkte = längere Rechnung → S2
for _t in ('Berechne geschickt: 7/3 · 3/7 · 2 · 0,5', 'Berechne geschickt: 14 : 0,5 : 2', 'Was ergibt 22 : 0,25 : 4?', 'Berechne geschickt: 8 · 0,5 · 2 · 1/8',
           'Was ergibt 42 : 0,5 : 4?', 'Berechne geschickt: 13 : 0,25 : 2', 'Berechne geschickt: 1,25 · 0,8 · 2,5 · 0,4 · 3,7'):
    _S('rechenvorteile', _t, 2)
# d) rechenvorteile: zwei Stufe-3-Aufgaben mit neuem Gedanken (Teiler vertauschen begründen; Rechenvorteil im Sachkontext)
DS.neu('rechenvorteile', 3, DS.A('Ist 36 : 4 : 3 dasselbe wie 36 : 3 : 4?', 'Ja: Beides ist 3. Man teilt nacheinander durch 4 und durch 3, die Reihenfolge der Teiler ist egal.',
                                  ['Nein: Beim Teilen darf man nie etwas vertauschen.', 'Nein: 36 : 3 : 4 = 48.', 'Ja, aber nur, weil 36 durch 12 teilbar ist.'],
                                  '36 : 4 : 3 = 9 : 3 = 3 und 36 : 3 : 4 = 12 : 4 = 3. Vertauschen der Teiler ist erlaubt (beides ist 36 : 12) – nur umklammern zu 36 : (4 : 3) ist verboten.',
                                  'Rechne beide Seiten von links nach rechts aus.'))
DS.neu('rechenvorteile', 3, DS.Z('Ein Kilogramm Kirschen kostet 4,80 €. Ein Kind kauft 0,25 kg, ein anderes 0,75 kg. Wie viel zahlen beide zusammen?', 4.8, '4.8 * (0.25 + 0.75)',
                                  'Geschickt: Beide zahlen zusammen für 0,25 kg + 0,75 kg = 1 kg. Also 4,80 €.', 'Rechne erst aus, wie viele Kilogramm beide zusammen kaufen.', einheit='€'))
# gemischt: (… ) : 0,25 und lange Produkt-Differenzen = längere Rechnung; Rückgeld = Einkleidung → S2
for _t in ('Berechne (3,4 − 1,8) : 0,25.', 'Berechne 3/2 · 2/5 − 1/4 · 5/2. Gib das Ergebnis als Dezimalzahl an.', 'Berechne 3/2 · 3/5 − 2/5 · 1/8. Gib das Ergebnis als Dezimalzahl an.',
           'Berechne 3/2 · 5/2 − 1/8 · 1/5. Gib das Ergebnis als Dezimalzahl an.', 'Ein Kind kauft 2 Hefte zu je 0,36 € und 2 Stifte zu je 0,54 €. Es bezahlt mit 20 €. Wie viel bekommt es zurück?',
           'Ein Kind kauft 2 Hefte zu je 1,81 € und 4 Stifte zu je 0,86 €. Es bezahlt mit 20 €. Wie viel bekommt es zurück?'):
    _S('gemischt', _t, 2)
# fehler_finden: „Nenner addiert“ ist der Stufe-1-Fehler → S1; Kehrbruch-Fehler und Überschlag wie in S2 → S2
for _t in ('Ein Kind rechnet: 3/4 + 2/7 = 5/11. Was ist der Fehler?', 'Ein Kind rechnet: 2/3 + 1/4 = 3/7. Was ist der Fehler?', 'Ein Kind rechnet: 2/3 + 1/2 = 3/5. Was ist der Fehler?'):
    _S('fehler_finden', _t, 1)
for _t in ('Ein Kind rechnet: 1/2 : 3/5 = 2/1 · 3/5. Was ist der Fehler?', 'Welches Ergebnis von 5,7 · 8,6 kann nach einem Überschlag stimmen?',
           'Welches Ergebnis von 29,3 · 4,7 kann nach einem Überschlag stimmen?'):
    _S('fehler_finden', _t, 2)
befunde_anwenden(DATEI, DS)
# ---- DURCHSICHT ENDE ----


if __name__ == '__main__':
    schreibe(DATEI)
