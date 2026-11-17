#!/usr/bin/env python3
"""Thema daten.kennwerte – Mittelwert und Häufigkeiten (Klasse 6)."""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _basis import *  # noqa: E402,F403

R = random.Random(58)
E = eintrag_laden('daten.kennwerte')

ETAPPEN = [
    {'lernziel': 'mittelwert', 'titel': 'Arithmetisches Mittel berechnen',
     'regel': 'Das ⟦arithmetische Mittel⟧ (der Mittelwert, „Durchschnitt“) ist ⟦Summe aller Werte : Anzahl der Werte⟧. Stell dir die Werte als Stapel vor: Du gibst von hohen Stapeln an niedrige ab, bis ⟦alle gleich hoch⟧ sind. Diese Höhe ist der Mittelwert.',
     'schritte': ['Vier Kinder haben 7, 9, 4 und 8 Punkte. Summe: 7 + 9 + 4 + 8 = 28.', 'Verteilt auf 4 Kinder: 28 : 4 = ⟦7⟧.',
                  'Ausgleichen: Der 9er-Stapel gibt 2 ab, der 8er-Stapel 1. Damit wird der 4er-Stapel zu 7. Jetzt sind alle 7 hoch.'],
     'bild': {'typ': 'saeulen', 'einheit': 'Punkte', 'werte': [{'name': 'A', 'wert': 7}, {'name': 'B', 'wert': 9}, {'name': 'C', 'wert': 4}, {'name': 'D', 'wert': 8}], 'zahlen': True},
     'probe': '4 · 7 = 28 ✓',
     'fehler': 'Bei 7, 9, 4, 8 durch 28 : 2 = 14 zu teilen ist falsch: Geteilt wird durch die ⟦Anzahl der Werte⟧ (4), nicht durch 2.'},
    {'lernziel': 'mittel_tabelle', 'titel': 'Mittelwert aus einer Häufigkeitstabelle',
     'regel': 'Steht in einer Tabelle, wie oft ein Wert vorkommt, rechnest du ⟦jeden Wert mal seine Häufigkeit⟧, addierst alles und teilst durch die ⟦Gesamtzahl⟧ der Werte.',
     'schritte': ['Noten: 1 → 2-mal, 2 → 5-mal, 3 → 3-mal. Summe: 1 · 2 + 2 · 5 + 3 · 3 = 21.', 'Anzahl: 2 + 5 + 3 = 10. Mittelwert: 21 : 10 = ⟦2,1⟧.'],
     'fehler': 'Die Werte 1, 2, 3 einfach zu mitteln ((1 + 2 + 3) : 3 = 2) ist falsch: Jeder Wert zählt so oft, wie er ⟦vorkommt⟧.',
     'bild': {'typ': 'tabelle', 'kopf': ['Note', '1', '2', '3', 'Summe'], 'zeilen': [['Anzahl', '2', '5', '3', '10'], ['Note · Anzahl', '2', '10', '9', '21']]}},
    {'lernziel': 'mittel_rueckwaerts', 'titel': 'Rückwärts rechnen mit dem Mittelwert',
     'regel': 'Aus dem Mittelwert bekommst du die ⟦Summe⟧ zurück: ⟦Summe = Mittelwert · Anzahl⟧. So findest du einen fehlenden Wert oder den neuen Mittelwert, wenn ein Wert dazukommt.',
     'schritte': ['Drei Tests haben im Mittel 8 Punkte, zwei davon 7 und 10. Summe aller drei: 8 · 3 = 24.', 'Fehlender Wert: 24 − 7 − 10 = ⟦7⟧.'],
     'probe': '(7 + 10 + 7) : 3 = 8 ✓',
     'fehler': 'Den fehlenden Wert als 8 anzunehmen, weil der Mittelwert 8 ist, ist falsch: Erst die ⟦Summe⟧ (Mittelwert · Anzahl) bilden, dann die bekannten Werte abziehen.'},
    {'lernziel': 'modal_spannweite', 'titel': 'Modalwert und Spannweite',
     'regel': 'Der ⟦Modalwert⟧ ist der Wert, der ⟦am häufigsten⟧ vorkommt. Die ⟦Spannweite⟧ ist ⟦größter Wert − kleinster Wert⟧ und zeigt, wie weit die Daten auseinanderliegen.',
     'schritte': ['Schuhgrößen: 36, 38, 37, 38, 40, 38, 35. Die 38 kommt dreimal vor: Modalwert ⟦38⟧.', 'Größter Wert 40, kleinster 35: Spannweite 40 − 35 = ⟦5⟧.'],
     'fehler': 'Die Spannweite als „letzter Wert − erster Wert“ der Liste zu rechnen ist falsch (35 − 36). Man nimmt ⟦größten minus kleinsten⟧ Wert.'},
    {'lernziel': 'median', 'titel': 'Der Median (Zentralwert)',
     'regel': 'Der ⟦Median⟧ steht in der ⟦Mitte der der Größe nach geordneten⟧ Liste. Bei einer geraden Anzahl von Werten ist er der ⟦Mittelwert der beiden mittleren⟧ Werte. Ausreißer beeinflussen ihn kaum.',
     'schritte': ['Werte: 12, 3, 8, 5, 20. Ordnen: 3, 5, 8, 12, 20.', 'In der Mitte steht die 8: Median = ⟦8⟧.'],
     'fehler': 'Den mittleren Wert der ⟦ungeordneten⟧ Liste nehmen. Bei 12, 3, 20, 5, 8 steht in der Mitte die 20 – aber 20 ist der größte Wert! Geordnet: 3, 5, 8, 12, 20, der Median ist ⟦8⟧. Zuerst ⟦ordnen⟧!'},
    {'lernziel': 'verstehen', 'titel': 'Kennwerte beurteilen',
     'regel': 'Der Mittelwert reagiert stark auf ⟦Ausreißer⟧ (einzelne sehr große oder kleine Werte). Er muss ⟦nicht⟧ in der Liste vorkommen und muss keine ganze Zahl sein. Prüfe Aussagen mit ⟦Zahlenbeispielen⟧.',
     'schritte': ['Taschengeld: 5 €, 6 €, 5 €, 4 €, 30 €. Mittelwert: 50 € : 5 = 10 €.', 'Vier von fünf Kindern bekommen weniger als 10 €. Der Ausreißer 30 € ⟦verzerrt⟧ den Mittelwert.'],
     'fehler': '„Der Mittelwert ist 10 €, also bekommen die meisten Kinder etwa 10 €“ ist falsch: Ein ⟦Ausreißer⟧ kann den Mittelwert stark nach oben ziehen.'},
]

MERKE = ['Mittelwert = Summe : Anzahl.', 'Häufigkeitstabelle: Wert · Häufigkeit addieren, durch Gesamtzahl teilen.', 'Summe = Mittelwert · Anzahl.',
         'Modalwert: häufigster Wert. Spannweite: größter − kleinster Wert.', 'Median: Mitte der geordneten Liste.']

SACHEN = [('Punkte im Test', ''), ('Tore pro Spiel', ''), ('Körpergröße', ' cm'), ('Weite beim Weitsprung', ' m'), ('Temperatur am Mittag', ' °C'), ('Taschengeld', ' €')]


def liste_mit_mittel(R, n, lo, hi, nachkomma=1):
    while True:
        xs = [R.randint(lo, hi) for _ in range(n)]
        m = Fr(sum(xs), n)
        if (m * 10 ** nachkomma).denominator == 1: return xs, m


def lt(xs, e=''):
    return ', '.join(zt(x) + e for x in xs)


# ---------- 1 Mittelwert ----------
BUCH = [('Gelesene Bücher im Monat', 'Bücher', ['Kind A', 'Kind B', 'Kind C', 'Kind D', 'Kind E'], 1, 8),
        ('Regentage im Monat', 'Tage', ['Jan', 'Feb', 'Mär', 'Apr', 'Mai'], 6, 15),
        ('Tore pro Spiel', 'Tore', ['Spiel 1', 'Spiel 2', 'Spiel 3', 'Spiel 4', 'Spiel 5'], 0, 5)]


def mittel_diagramm(st):
    titel, einheit, namen, lo, hi = R.choice(BUCH)
    n = R.choice([4, 5])
    xs, m = liste_mit_mittel(R, n, lo, hi, 0 if st == 1 else 1)
    return {'y': 'zahl', 'f': {'text': f'Das Säulendiagramm zeigt: {titel}. Berechne den Mittelwert.', 'grafik': saeulen(list(zip(namen[:n], xs)), einheit=einheit)},
            'o': {'wert': wert(m)}, 'c': f'({" + ".join(map(str, xs))}) / {n}',
            'w': f'Abgelesen: {lt(xs)}. Summe {sum(xs)}, Anzahl {n}: {sum(xs)} : {n} = {zt(m)}.', 'h': 'Lies alle Säulen ab, addiere und teile durch die Anzahl der Säulen.'}


def g_mittel(st):
    if st in (1, 2) and R.random() < .35:
        return mittel_diagramm(st)
    if st == 1:
        n = R.choice([3, 4, 5])
        xs, m = liste_mit_mittel(R, n, 1, 20, 0)
        return {'y': 'zahl', 'f': {'text': f'Berechne den Mittelwert von {lt(xs)}.'}, 'o': {'wert': wert(m)}, 'c': f'({" + ".join(map(str, xs))}) / {n}',
                'w': f'Summe {" + ".join(map(str, xs))} = {sum(xs)}. {sum(xs)} : {n} = {zt(m)}.', 'h': 'Addiere alle Werte und teile durch die Anzahl.'}
    if st == 2:
        name, e = R.choice(SACHEN)
        n = R.choice([4, 5, 6, 8, 10])
        lo, hi = {'Punkte im Test': (5, 30), 'Tore pro Spiel': (0, 6), 'Körpergröße': (138, 162), 'Weite beim Weitsprung': (2, 4),
                  'Temperatur am Mittag': (-4, 25), 'Taschengeld': (3, 25)}[name]
        xs, m = liste_mit_mittel(R, n, lo, hi, 2)
        if name == 'Weite beim Weitsprung':
            xs = [Fr(R.randint(250, 420), 100) for _ in range(n)]
            m = sum(xs) / n
            if (m * 1000).denominator != 1: return g_mittel(2)
        neg = any(x < 0 for x in xs)
        return {'y': 'zahl', 'f': {'text': f'{name}: {lt(xs, e)}. Berechne den Mittelwert.'}, 'o': {'wert': wert(m), **({'einheit': e.strip()} if e else {})},
                'c': f'({" + ".join(zt(x).replace(",", ".").replace("−", "-").replace(" ", "") for x in xs)}) / {n}',
                'w': f'Summe: {zt(sum(xs))}{e}. Anzahl: {n}. Mittelwert: {zt(sum(xs))} : {n} = {zt(m)}{e}.',
                'h': 'Summe durch Anzahl.' + (' Negative Werte beim Addieren beachten.' if neg else '')}
    art = R.randrange(2)
    if art == 0:
        n = R.choice([5, 6, 7])
        xs, m = liste_mit_mittel(R, n, 10, 60, 1)
        return {'y': 'zahl', 'f': {'text': f'Ein Kind läuft an {n} Tagen {lt(xs, " min")}. Wie viele Minuten läuft es im Durchschnitt pro Tag?'}, 'o': {'wert': wert(m), 'einheit': 'min'},
                'c': f'({" + ".join(map(str, xs))}) / {n}', 'w': f'{sum(xs)} min : {n} = {zt(m)} min.', 'h': '„Im Durchschnitt“ heißt: Mittelwert.'}
    a, b = liste_mit_mittel(R, 4, 2, 12, 2)
    c, d = liste_mit_mittel(R, 4, 2, 12, 2)
    if b == d: return g_mittel(3)
    r = 'Gruppe A' if b > d else 'Gruppe B'
    return {**wahl(R, r, ['Gruppe B' if r == 'Gruppe A' else 'Gruppe A', 'Beide gleich', 'Die Gruppe mit dem größten Einzelwert']),
            'f': {'text': f'Gruppe A sammelt {lt(a, " kg")} Altpapier, Gruppe B {lt(c, " kg")}. Welche Gruppe hat im Mittel mehr gesammelt?'},
            'w': f'A: {sum(a)} : 4 = {zt(b)} kg, B: {sum(c)} : 4 = {zt(d)} kg. Mehr im Mittel: {r}.', 'h': 'Berechne für beide Gruppen den Mittelwert.'}


# ---------- 2 Häufigkeitstabelle ----------
NOTEN_GEWICHT = [1, 3, 3, 2, 1, 1]   # meiste Noten bei 2 bis 4, wenige 1, 5 und 6


def g_tab(st):
    werte = {1: [1, 2, 3], 2: [1, 2, 3, 4, 5], 3: [1, 2, 3, 4, 5, 6]}[st]
    art = R.choice(['Note', 'Tore', 'Geschwister'])
    if art == 'Note':
        werte = {1: [2, 3, 4], 2: [1, 2, 3, 4, 5], 3: [1, 2, 3, 4, 5, 6]}[st]
        while True:
            h = [max(0, min(9, round(R.gauss(NOTEN_GEWICHT[w - 1] * 2.2, 1.2)))) for w in werte]
            if st == 1: h = [max(1, x) for x in h]
            n = sum(h)
            s = sum(w * k for w, k in zip(werte, h))
            if n >= 8 and (Fr(s, n) * 100).denominator == 1 and max(h) == max(h[werte.index(2):werte.index(4) + 1]): break
        m = Fr(s, n)
        g = tabelle(['Note'] + werte, [['Anzahl'] + h])
        return {'y': 'zahl', 'f': {'text': 'Die Tabelle zeigt einen Notenspiegel. Berechne die Durchschnittsnote.', 'grafik': g}, 'o': {'wert': wert(m)},
                'c': f'({" + ".join(f"{w} * {k}" for w, k in zip(werte, h))}) / ({" + ".join(map(str, h))})',
                'w': f'Note · Anzahl: {" + ".join(f"{w} · {k}" for w, k in zip(werte, h))} = {s}. Anzahl: {" + ".join(map(str, h))} = {n}. Mittelwert: {s} : {n} = {zt(m)}.',
                'h': 'Note mal Anzahl, alles addieren, durch die Gesamtzahl teilen.'}
    while True:
        h = [R.randint(0 if st == 3 else 1, 8) for _ in werte]
        if art == 'Geschwister': h = h[:4]
        vs = [w - 1 for w in werte][:len(h)]
        n = sum(h)
        if n == 0: continue
        s = sum(w * k for w, k in zip(vs, h))
        m = Fr(s, n)
        if (m * 100).denominator == 1: break
    if art == 'Tore':
        g = tabelle(['Tore im Spiel'] + vs, [['Anzahl Spiele'] + h])
        return {'y': 'zahl', 'f': {'text': 'Die Tabelle zeigt, wie viele Tore eine Mannschaft in ihren Spielen geschossen hat. Wie viele Tore schießt sie im Mittel pro Spiel?', 'grafik': g},
                'o': {'wert': wert(m)}, 'c': f'({" + ".join(f"{w} * {k}" for w, k in zip(vs, h))}) / ({" + ".join(map(str, h))})',
                'w': 'Tore insgesamt: ' + ' + '.join(f'{w} · {k}' for w, k in zip(vs, h)) + f' = {s}. Spiele: {n}. Mittel: {s} : {n} = {zt(m)}.',
                'h': 'Jede Torzahl mal die Anzahl der Spiele, dann durch alle Spiele teilen.'}
    g = tabelle(['Geschwister'] + vs, [['Anzahl Kinder'] + h])
    return {'y': 'zahl', 'f': {'text': 'Die Tabelle zeigt die Umfrage „Wie viele Geschwister hast du?“. Wie viele Geschwister hat ein Kind im Mittel?', 'grafik': g},
            'o': {'wert': wert(m)}, 'c': f'({" + ".join(f"{w} * {k}" for w, k in zip(vs, h))}) / ({" + ".join(map(str, h))})',
            'w': f'Summe: {" + ".join(f"{w} · {k}" for w, k in zip(vs, h))} = {s}. Anzahl: {" + ".join(map(str, h))} = {n}. Mittelwert: {s} : {n} = {zt(m)}.',
            'h': 'Wert mal Häufigkeit, alles addieren, durch die Gesamtzahl teilen.'}


# ---------- 3 Rückwärts ----------
def g_rueck(st):
    if st == 1:
        n = R.choice([3, 4, 5, 6])
        m = R.randint(4, 20)
        return {'y': 'zahl', 'f': {'text': f'{n} Kinder haben im Mittel {m} Bücher gelesen. Wie viele Bücher sind das zusammen?'}, 'o': {'wert': n * m}, 'c': f'{m} * {n}',
                'w': f'Summe = Mittelwert · Anzahl = {m} · {n} = {n * m}.', 'h': 'Summe = Mittelwert · Anzahl.'}
    if st == 2:
        n = R.choice([3, 4, 5])
        m = R.randint(8, 22)
        bek = [R.randint(max(1, m - 8), min(30, m + 8)) for _ in range(n - 1)]
        x = m * n - sum(bek)
        if not 1 <= x <= 30 or x == m: return g_rueck(2)
        return {'y': 'zahl', 'f': {'text': f'In {n} Tests (je höchstens 30 Punkte) hat ein Kind im Mittel {m} Punkte. Bekannt sind {lt(bek)} Punkte. Wie viele Punkte hatte es im fehlenden Test?'},
                'o': {'wert': x}, 'c': f'{m} * {n} - (' + ' + '.join(map(str, bek)) + ')',
                'w': f'Summe aller Punkte: {m} · {n} = {m * n}. Fehlend: {m * n} − {sum(bek)} = {x}.', 'h': 'Berechne zuerst die Summe aller Werte aus dem Mittelwert.'}
    art = R.randrange(2)
    if art == 0:
        n = R.choice([4, 5, 9])
        m = R.randint(6, 15)
        neu = R.randint(1, 30)
        m2 = Fr(m * n + neu, n + 1)
        if neu == m or (m2 * 10).denominator != 1: return g_rueck(3)
        return {'y': 'zahl', 'f': {'text': f'{n} Kinder haben im Mittel {m} Punkte. Ein weiteres Kind kommt mit {neu} Punkten dazu. Wie groß ist der neue Mittelwert?'}, 'o': {'wert': wert(m2)},
                'c': f'({m} * {n} + {neu}) / {n + 1}', 'w': f'Alte Summe: {m} · {n} = {m * n}. Neue Summe: {m * n + neu}. Neuer Mittelwert: {m * n + neu} : {n + 1} = {zt(m2)}.',
                'h': 'Berechne die alte Summe, addiere den neuen Wert und teile durch die neue Anzahl.'}
    n = R.choice([3, 4, 5])
    m = R.randint(6, 12)
    ziel = m + R.choice([1, 2])
    x = ziel * (n + 1) - m * n
    if x > 30: return g_rueck(3)
    return {'y': 'zahl', 'f': {'text': f'Nach {n} Tests hat ein Kind im Mittel {m} Punkte. Wie viele Punkte braucht es im nächsten Test, damit der Mittelwert auf {ziel} steigt?'}, 'o': {'wert': x},
            'c': f'{ziel} * {n + 1} - {m} * {n}', 'w': f'Neue Summe nötig: {ziel} · {n + 1} = {ziel * (n + 1)}. Bisher: {m} · {n} = {m * n}. Benötigt: {x} Punkte.',
            'h': 'Welche Summe braucht man für den neuen Mittelwert? Ziehe die bisherige Summe ab.'}


# ---------- 4 Modalwert und Spannweite ----------
def mehrere_modal():
    """Kein oder mehrere Modalwerte (Auswahl)."""
    if R.random() < .5:
        a, b = sorted(R.sample(range(2, 10), 2))
        rest = R.sample([x for x in range(1, 12) if x not in (a, b)], R.randint(1, 2))
        xs = [a, a, b, b] + rest
        R.shuffle(xs)
        r = f'{a} und {b}'
        m = (Fr(sum(xs), len(xs)) * 10 // 1) / 10
        falsch = [str(a), str(b), f'Es gibt keinen Modalwert.']
        w = f'{a} und {b} kommen beide zweimal vor, alle anderen nur einmal. Es gibt zwei Modalwerte: {a} und {b}.'
    else:
        xs = R.sample(range(1, 15), R.randint(4, 6))
        r = 'Es gibt keinen Modalwert (jeder Wert kommt nur einmal vor).'
        falsch = [str(max(xs)), str(xs[len(xs) // 2]), str(min(xs))]
        w = 'Jeder Wert kommt genau einmal vor. Kein Wert ist häufiger als die anderen – es gibt keinen Modalwert.'
    return {**wahl(R, r, falsch), 'f': {'text': f'Welchen Modalwert hat {lt(xs)}?'}, 'w': w,
            'h': 'Zähle, wie oft jeder Wert vorkommt. Es kann mehrere häufigste Werte geben – oder keinen.'}


def g_modal(st):
    if st == 3 and R.random() < .35 or st == 2 and R.random() < .2:
        return mehrere_modal()
    n = {1: 7, 2: 10, 3: 12}[st]
    lo, hi = R.choice([(1, 9), (30, 42), (120, 160), (-5, 12)])
    while True:
        xs = [R.randint(lo, hi) for _ in range(n)]
        c = {x: xs.count(x) for x in xs}
        top = max(c.values())
        if list(c.values()).count(top) == 1 and top >= 2: break
    mod = max(c, key=c.get)
    if R.random() < .5:
        if st == 3 and R.random() < .5:
            r = zt(mod)
            return {**wahl(R, r, [zt(max(xs)), zt(xs[n // 2]), zt((Fr(sum(xs), n) * 10 // 1) / 10)]), 'f': {'text': f'Welcher Wert ist der Modalwert von {lt(xs)}?'},
                    'w': f'{zt(mod)} kommt {top}-mal vor, öfter als jeder andere Wert.', 'h': 'Modalwert = häufigster Wert, nicht größter oder mittlerer.'}
        return {'y': 'zahl', 'f': {'text': f'Bestimme den Modalwert von {lt(xs)}.'}, 'o': {'wert': mod}, 'c': f'{mod}',
                'w': f'{zt(mod)} kommt {top}-mal vor – häufiger als jeder andere Wert.', 'h': 'Welcher Wert kommt am häufigsten vor?'}
    sp = max(xs) - min(xs)
    if st == 3 and R.random() < .5:
        ts = [R.randint(-6, 12) for _ in range(7)]
        if min(ts) >= 0: ts[R.randrange(7)] = -R.randint(1, 6)
        return {'y': 'zahl', 'f': {'text': f'Temperaturen am Morgen in einer Woche (°C): {lt(ts)}. Wie groß ist die Spannweite?'}, 'o': {'wert': max(ts) - min(ts), 'einheit': '°C'},
                'c': f'max({", ".join(map(str, ts))}) - min({", ".join(map(str, ts))})',
                'w': f'Größter Wert {zt(max(ts))}, kleinster {zt(min(ts))}: {zt(max(ts))} − {kl(min(ts))} = {zt(max(ts) - min(ts))} °C.',
                'h': 'Größter minus kleinster Wert. Bei negativen Werten: minus minus wird plus.'}
    return {'y': 'zahl', 'f': {'text': f'Bestimme die Spannweite von {lt(xs)}.'}, 'o': {'wert': sp}, 'c': f'max({", ".join(map(str, xs))}) - min({", ".join(map(str, xs))})',
            'w': f'Größter Wert {zt(max(xs))}, kleinster Wert {zt(min(xs))}. Spannweite: {zt(max(xs))} − {kl(min(xs))} = {zt(sp)}.', 'h': 'Suche den größten und den kleinsten Wert.'}


# ---------- 5 Median ----------
def g_median(st):
    n = {1: R.choice([5, 7]), 2: R.choice([6, 8, 9]), 3: R.choice([8, 10, 11])}[st]
    while True:
        xs = [R.randint(1, 40) for _ in range(n)]
        s = sorted(xs)
        med = Fr(s[n // 2]) if n % 2 else Fr(s[n // 2 - 1] + s[n // 2], 2)
        if xs != s: break
    if st == 3 and R.random() < .35:
        return median_fehler()
    if st == 3 and R.random() < .4:
        ausr = R.randint(150, 400)
        ys = xs[:-1] + [ausr]
        s2 = sorted(ys)
        med2 = Fr(s2[n // 2]) if n % 2 else Fr(s2[n // 2 - 1] + s2[n // 2], 2)
        m2 = Fr(sum(ys), n)
        r = 'den Mittelwert'
        return {**wahl(R, r, ['den Median', 'beide gleich stark', 'keinen von beiden']), 'f': {'text': f'Daten: {lt(ys)}. Welchen Kennwert verändert der Ausreißer {ausr} stärker?'},
                'w': f'Median: {zt(med2)}. Mittelwert: {zt((m2 * 10 + Fr(1, 2)) // 1 / 10)} (gerundet). Der Ausreißer zieht den Mittelwert stark nach oben, der Median bleibt in der Mitte.',
                'h': 'Der Median schaut nur auf die Mitte der geordneten Liste.'}
    gerade = ' Die Anzahl ist gerade: Nimm den Mittelwert der beiden mittleren Werte.' if n % 2 == 0 else ''
    return {'y': 'zahl', 'f': {'text': f'Bestimme den Median von {lt(xs)}.'}, 'o': {'wert': wert(med)},
            'c': f'{s[n // 2]}' if n % 2 else f'({s[n // 2 - 1]} + {s[n // 2]}) / 2',
            'w': f'Geordnet: {lt(s)}. ' + (f'Mitte (Platz {n // 2 + 1}): {zt(med)}.' if n % 2 else f'Mittlere Werte {s[n // 2 - 1]} und {s[n // 2]}: ({s[n // 2 - 1]} + {s[n // 2]}) : 2 = {zt(med)}.'),
            'h': 'Ordne die Werte zuerst der Größe nach.' + gerade}


def median_fehler():
    """Fehler beim Median finden (Auswahl)."""
    if R.random() < .5:
        while True:
            xs = R.sample(range(1, 20), 5)
            s_ = sorted(xs)
            if xs[2] != s_[2]: break
        r = f'Die Werte wurden nicht geordnet; richtig: {lt(s_)} → {s_[2]}.'
        falsch = ['Es ist alles richtig.', f'Man muss den Mittelwert nehmen: {zt((Fr(sum(xs), 5) * 10 // 1) / 10)}.', f'Der Median ist der größte Wert: {max(xs)}.']
        return {**wahl(R, r, falsch), 'f': {'text': f'Jemand bestimmt den Median von {lt(xs)} als {xs[2]} (mittlere Zahl der Liste). Was ist falsch?'},
                'w': f'Zuerst ordnen: {lt(s_)}. In der Mitte steht {s_[2]}.', 'h': 'Was muss man vor dem Ablesen der Mitte tun?'}
    while True:
        s_ = sorted(R.sample(range(1, 20), 4))
        if (s_[1] + s_[2]) % 2 == 0: break
    med = (s_[1] + s_[2]) // 2
    r = f'Bei gerader Anzahl: ({s_[1]} + {s_[2]}) : 2 = {med}.'
    falsch = ['Es ist alles richtig.', f'Der Median ist {s_[1]}, der kleinere der beiden mittleren Werte.', 'Bei gerader Anzahl gibt es keinen Median.']
    return {**wahl(R, r, falsch), 'f': {'text': f'Jemand sagt: „Der Median von {lt(s_)} ist {s_[2]}.“ Was ist falsch?'},
            'w': f'Vier Werte – zwei stehen in der Mitte: {s_[1]} und {s_[2]}. Median = ({s_[1]} + {s_[2]}) : 2 = {med}.', 'h': 'Wie viele Werte hat die Liste? Gerade oder ungerade?'}


# ---------- 6 Verstehen ----------
def g_vers(st):
    """Aussagen mit eigenem Fehlgrund; etwa die Hälfte der Aussagen ist falsch."""
    n = R.choice([4, 5])
    xs, m = liste_mit_mittel(R, n, 2, 12, 1)
    if st == 1:
        k = R.choice([x for x in range(2, 13) if x not in xs])
        aussagen = [(f'Der Mittelwert von {lt(xs)} liegt zwischen dem kleinsten und dem größten Wert.', True, f'Ja, er ist {zt(m)} und liegt zwischen {min(xs)} und {max(xs)}.',
                     f'Nein, er kann größer als der größte Wert sein.'),
                    (f'Der Mittelwert von {lt(xs)} ist {zt(Fr(sum(xs), 2))}.', False, f'Nein, man teilt durch die Anzahl {n}: {sum(xs)} : {n} = {zt(m)}.',
                     f'Ja, man teilt die Summe {sum(xs)} durch 2.'),
                    (f'Der Mittelwert von {lt(xs)} ist {zt(m)}.', True, f'Ja: Summe {sum(xs)}, geteilt durch die Anzahl {n}: {sum(xs)} : {n} = {zt(m)}.', f'Nein, der Mittelwert muss einer der Werte sein.' if m not in xs else 'Nein, man teilt durch 2.'),
                    (f'Der Mittelwert ganzer Zahlen ist immer eine ganze Zahl.', False, 'Nein, z. B. Mittelwert von 7, 8, 9, 6 ist 7,5.', 'Ja, weil man nur ganze Zahlen addiert.')]
    elif st == 2:
        k = R.randint(2, 5)
        sp = max(xs) - min(xs)
        aussagen = [(f'Wenn man zu jedem Wert von {lt(xs)} die Zahl {k} addiert, wird auch der Mittelwert um {k} größer.', True, f'Ja, die Summe wächst um {n} · {k}, geteilt durch {n} also um {k}: neuer Mittelwert {zt(m)} + {k} = {zt(m + k)}.',
                     f'Nein, er wird um {k * n} größer, weil {n} Werte je {k} dazubekommen.'),
                    ('Wenn ein sehr großer Wert dazukommt, kann der Mittelwert kleiner werden.', False, 'Nein, ein Wert über dem Mittelwert zieht ihn nach oben.',
                     'Ja, weil dann durch eine größere Anzahl geteilt wird.'),
                    (f'Die Spannweite von {lt(xs)} ist {sp + R.choice([1, 2, 3])}.', False, f'Nein, größter minus kleinster Wert: {max(xs)} − {min(xs)} = {sp}.', 'Ja, Spannweite = letzter Wert − erster Wert.'),
                    (f'Die Spannweite von {lt(xs)} ist {sp}.', True, f'Ja, größter minus kleinster Wert: {max(xs)} − {min(xs)} = {sp}.', 'Nein, Spannweite = letzter Wert − erster Wert.')]
    else:
        ausr = R.randint(40, 90)
        ys = xs + [ausr]
        m2 = Fr(sum(ys), n + 1)
        aussagen = [(f'Taschengeld (€): {lt(ys)}. Der Mittelwert zeigt gut, was ein typisches Kind bekommt.', False,
                     f'Nein, der Ausreißer {ausr} € zieht den Mittelwert auf etwa {zt((m2 * 10 + Fr(1, 2)) // 1 / 10)} €, obwohl fast alle viel weniger bekommen.',
                     'Ja, der Mittelwert ist immer der typische Wert.'),
                    ('Haben zwei Klassen den gleichen Mittelwert, haben sie auch die gleiche Spannweite.', False, 'Nein, z. B. 5, 5 und 1, 9: beide Mittelwert 5, Spannweiten 0 und 8.',
                     'Ja, gleicher Mittelwert heißt gleiche Werte.'),
                    (f'Taschengeld (€): {lt(ys)}. Der Median beschreibt ein typisches Kind besser als der Mittelwert.', True,
                     f'Ja, der Median bleibt in der Mitte der geordneten Liste, der Ausreißer {ausr} € verändert ihn kaum.', 'Nein, der Mittelwert ist immer genauer.'),
                    (f'Lässt man bei {lt(ys)} den Ausreißer {ausr} weg, wird der Mittelwert kleiner.', True, f'Ja, ohne {ausr} ist er {zt(m)}, mit {ausr} etwa {zt((m2 * 10 + Fr(1, 2)) // 1 / 10)}.',
                     'Nein, ein einzelner Wert ändert den Mittelwert nicht.')]
    soll = R.random() < .5                       # etwa die Hälfte wahr, die Hälfte falsch
    s_, stimmt, grund, fehlgrund = R.choice([x for x in aussagen if x[1] == soll])
    gegen = 'Ja, die Aussage stimmt.' if not stimmt else 'Nein, die Aussage ist falsch.'
    return {**wahl(R, grund, [fehlgrund, gegen], 3), 'f': {'text': f'Stimmt die Aussage? „{s_}“'},
            'w': grund, 'h': 'Rechne nach oder suche ein Gegenbeispiel.'}


GEN = {'mittelwert': g_mittel, 'mittel_tabelle': g_tab, 'mittel_rueckwaerts': g_rueck, 'modal_spannweite': g_modal, 'median': g_median, 'verstehen': g_vers}

DATEI = datei(E, 'Das arithmetische Mittel bestimmen und deuten, Modalwert, Spannweite und Median ermitteln und Kennwerte kritisch beurteilen.', MERKE,
              [('Mittelwert', ['mittelwert', 'mittel_tabelle', 'mittel_rueckwaerts']),
               ('Weitere Kennwerte', ['modal_spannweite', 'median', 'verstehen'])],
              ETAPPEN, GEN, vertiefung=['modal_spannweite', 'median'],
              offen=['„umfang“ nennt Median, Quartile und Boxplot; der Kl.-6-Lehrplan (lehrplan_gym) verlangt nur das arithmetische Mittel. Quartile und Boxplot weggelassen (höhere Klasse, Boxplot braucht außerdem eine Zeichnung). Median als Vertiefung (nicht Pflicht) aufgenommen, Modalwert und Spannweite als einfache Ergänzung zum Mittelwert.',
                     'Falls der Median doch Pflicht werden soll: in bewertung.lernziele_pflicht verschieben.'])

# ---------- KARTEN: Lernkarten nach dem neuen Muster (Achte Runde, Vorgabe 16.11., Paket U6) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl6.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl6 import umbau  # noqa: E402

KARTEN = {
 'mittelwert': {
  'einstieg': 'Vier Kinder haben 7, 9, 4 und 8 Punkte. Die hohen Stapel geben ab, bis alle gleich hoch sind. Diese Höhe heißt ⟦Mittelwert⟧.',
  'woerter': [['Mittelwert', 'Summe aller Werte geteilt durch ihre Anzahl'],
              ['Summe', 'alle Werte zusammengezählt']],
  'bild': {'typ': 'saeulen', 'einheit': 'Punkte', 'werte': [{'name': 'Kind A', 'wert': 7}, {'name': 'Kind B', 'wert': 9},
           {'name': 'Kind C', 'wert': 4}, {'name': 'Kind D', 'wert': 8}], 'zahlen': True},
  'schritte': [{'text': 'Die Summe ist 7 + 9 + 4 + 8 = 28 Punkte.'},
               {'text': 'Verteile auf 4 Kinder: 28 : 4 = ⟦7⟧.',
                'bild': {'werte': [{'name': 'Kind A', 'wert': 7}, {'name': 'Kind B', 'wert': 7}, {'name': 'Kind C', 'wert': 7}, {'name': 'Kind D', 'wert': 7}]}},
               {'text': 'B gibt 2 ab, D gibt 1 ab. So hat C auch 7.'}],
  'fehler': 'Durch 2 statt durch 4 zu teilen ergibt 14 Punkte. Das ist mehr, als irgendein Kind hat.',
  'regel': 'Mittelwert ist ⟦Summe durch Anzahl⟧. So viel hätte jeder bei gerechter Verteilung.'},
 'mittel_tabelle': {
  'einstieg': 'Der Notenspiegel zeigt: zweimal die 1, fünfmal die 2, dreimal die 3. Wie lautet die ⟦Durchschnittsnote⟧?',
  'woerter': [['Notenspiegel', 'eine Tabelle: wie oft kam jede Note vor'],
              ['Durchschnittsnote', 'der Mittelwert aller Noten']],
  'bild': {'typ': 'tabelle', 'kopf': ['Note', '1', '2', '3', 'Summe'], 'zeilen': [['Anzahl', '2', '5', '3', '10']]},
  'schritte': [{'text': 'Jede Note zählt so oft, wie sie vorkommt: Note mal Anzahl.',
                'bild': {'zeilen': [['Anzahl', '2', '5', '3', '10'], ['Note · Anzahl', '2', '10', '9', '21']]}},
               {'text': 'Summe aller Noten: 2 + 10 + 9 = 21. Es sind 10 Noten.'},
               {'text': 'Die Durchschnittsnote ist 21 : 10 = ⟦2,1⟧.'}],
  'fehler': '(1 + 2 + 3) : 3 = 2 ist falsch. Dann zählt die 1 so viel wie die 2, obwohl die 2 fünfmal kam.',
  'regel': 'Nimm ⟦jeden Wert mal seine Anzahl⟧ und addiere. Teile durch die Gesamtzahl der Werte.'},
 'mittel_rueckwaerts': {
  'einstieg': 'Du hast in drei Tests im Mittel 8 Punkte. Zwei Ergebnisse kennst du: 7 und 10. Das dritte rechnest du ⟦rückwärts⟧ aus.',
  'woerter': [['rückwärts', 'aus dem Mittelwert die Summe zurückrechnen: Summe = Mittelwert · Anzahl']],
  'bild': {'typ': 'saeulen', 'einheit': 'Punkte', 'werte': [{'name': 'Test 1', 'wert': 7}, {'name': 'Test 2', 'wert': 10},
           {'name': 'Test 3', 'wert': 0}], 'zahlen': True},
  'schritte': [{'text': 'Summe aller drei Tests: 8 · 3 = 24 Punkte.'},
               {'text': 'Bekannt sind 7 + 10 = 17 Punkte.'},
               {'text': 'Test 3 hatte 24 − 17 = ⟦7⟧ Punkte.',
                'bild': {'werte': [{'name': 'Test 1', 'wert': 7}, {'name': 'Test 2', 'wert': 10}, {'name': 'Test 3', 'wert': 7}]}}],
  'fehler': 'Den fehlenden Test mit 8 anzunehmen ist falsch. Dann wäre der Mittelwert (7 + 10 + 8) : 3, also etwa 8,3.',
  'regel': 'Rückwärts gilt: ⟦Summe = Mittelwert · Anzahl⟧. Zieh davon die bekannten Werte ab.'},
 'modal_spannweite': {
  'einstieg': 'Ein Verein bestellt Turnschuhe: Größen 36, 38, 37, 38, 40, 38 und 35. Am häufigsten braucht er 38, die Größen reichen von 35 bis 40. Dafür gibt es ⟦Modalwert⟧ und ⟦Spannweite⟧.',
  'woerter': [['Modalwert', 'der Wert, der am häufigsten vorkommt'],
              ['Spannweite', 'größter Wert minus kleinster Wert']],
  'bild': {'typ': 'saeulen', 'einheit': 'Paare', 'werte': [{'name': '35', 'wert': 1}, {'name': '36', 'wert': 1}, {'name': '37', 'wert': 1},
           {'name': '38', 'wert': 3}, {'name': '39', 'wert': 0}, {'name': '40', 'wert': 1}], 'zahlen': True},
  'schritte': [{'text': 'Die 38 kommt dreimal vor, jede andere Größe nur einmal.'},
               {'text': 'Der Modalwert ist also ⟦38⟧.'},
               {'text': 'Größter Wert 40, kleinster 35. Die Spannweite ist 40 − 35 = ⟦5⟧.'}],
  'fehler': 'Letzter minus erster Wert der Liste ist falsch: 35 − 36 = −1. Nimm den größten minus den kleinsten Wert.',
  'regel': 'Der Modalwert kommt ⟦am häufigsten⟧ vor. Die Spannweite ist größter minus kleinster Wert.'},
 'median': {
  'einstieg': 'Fünf Kinder messen ihren Schulweg: 12, 3, 8, 5 und 20 Minuten. Der Größe nach aufgestellt, steht das Kind mit 8 Minuten in der Mitte. Dieser Wert heißt ⟦Median⟧.',
  'woerter': [['Median', 'der Wert in der Mitte der geordneten Liste'],
              ['ordnen', 'vom kleinsten zum größten Wert sortieren']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 20, 'abschnitte': 20, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': 'Zuerst der Größe nach ordnen: 3, 5, 8, 12, 20.',
                'bild': {'punkte': [{'wert': 3}, {'wert': 5}, {'wert': 8}, {'wert': 12}, {'wert': 20}]}},
               {'text': 'Bei 5 Werten steht der 3. Wert in der Mitte.'},
               {'text': 'Der Median ist ⟦8⟧ Minuten.',
                'bild': {'punkte': [{'wert': 3}, {'wert': 5}, {'wert': 8, 'name': 'Median'}, {'wert': 12}, {'wert': 20}]}}],
  'fehler': 'Ohne Ordnen ist die Mitte Zufall. Bei 12, 3, 20, 5, 8 stünde dort 20. Erst ordnen!',
  'regel': 'Ordne die Werte, dann ist der ⟦Median⟧ der Wert in der Mitte. Bei gerader Anzahl nimmst du den Mittelwert der beiden mittleren.'},
 'verstehen': {
  'einstieg': 'Fünf Kinder bekommen 5 €, 6 €, 5 €, 4 € und 30 € Taschengeld. Im Mittel sind das 10 €, aber vier bekommen weniger. Schuld ist ein ⟦Ausreißer⟧.',
  'woerter': [['Ausreißer', 'ein Wert, der weit weg von den anderen liegt']],
  'bild': {'typ': 'saeulen', 'einheit': '€', 'werte': [{'name': 'Kind A', 'wert': 5}, {'name': 'Kind B', 'wert': 6}, {'name': 'Kind C', 'wert': 5},
           {'name': 'Kind D', 'wert': 4}, {'name': 'Kind E', 'wert': 30}], 'zahlen': True},
  'schritte': [{'text': 'Der Mittelwert ist 50 € : 5 = ⟦10 €⟧.'},
               {'text': 'Vier von fünf Kindern bekommen weniger als 10 €.'},
               {'text': 'Der Median 5 € beschreibt die Gruppe besser. Der Ausreißer ⟦verzerrt⟧ den Mittelwert.'}],
  'fehler': '„Im Mittel 10 €, also bekommen die meisten etwa 10 €“ ist falsch. Kein Kind bekommt etwa 10 €.',
  'regel': 'Achte auf ⟦Ausreißer⟧: Sie ziehen den Mittelwert stark mit, den Median kaum.'},
}

umbau(DATEI, KARTEN)



# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl6): je Lernkarte 2 Übungen Stufe 2 + 4 Übungen Stufe 3 ----------
# Läuft nach allen bisherigen Aufgaben mit eigenem Zufallsstart; die bisherigen Aufgaben bleiben unverändert.
# Prüfungsvorbilder: Bayerischer Mathematik-Test Jgst. 8 (ISB) 2025 Aufg. 5 (Mittelwert-Formel ohne Klammern), 2025 Aufg. 6c (Median aus
# Häufigkeiten, Grenze knapp), 2023 Aufg. 5b/5c (Median einer langen Reihe; gewichteter Mittelwert, gleiche Änderungen heben sich nicht auf),
# 2021 Aufg. 7 (Median von 13 Werten mit Wiederholungen); Jahrgangsstufentest Realschule Jgst. 6 (ISB) 2025 (Notenverteilung passend ergänzen);
# SMART-Aufgabensammlung Univ. Bayreuth Jgst. 5 (Notenverteilung zu vorgegebenem Durchschnitt).
from _schwer_kl6 import ergaenzen, zahl, wahl  # noqa: E402

_RUNDEN = tabelle(['Runden', '5', '10', '15', '20'], [['Kinder', '24', '50', '40', '36']])


def _kw():
    return {
        'mittelwert': [
            (2, lambda R: zahl('Berechne den Mittelwert von 2,5; 3,1; 4,2 und 1,8.', Fr('2.9'), '(2.5 + 3.1 + 4.2 + 1.8) / 4', 'Summe durch Anzahl.',
                               'Summe 11,6. 11,6 : 4 = 2,9.')),
            (2, lambda R: zahl('Berechne den Mittelwert von −4, 6, −2 und 8.', 2, '(-4 + 6 - 2 + 8) / 4', 'Achte bei der Summe auf die Vorzeichen.',
                               'Summe: −4 + 6 − 2 + 8 = 8. 8 : 4 = 2.')),
            (3, lambda R: wahl(R, 'Mit welcher Rechnung bekommst du den Mittelwert von 52 und 60?', '(52 + 60) : 2', ['52 + 60 : 2', '52 : 2 + 60', '(52 + 60) · 2'],
                               'Erst die Summe, dann teilen. Denk an Punkt vor Strich.', '(52 + 60) : 2 = 56. Ohne Klammer würde nur 60 halbiert: 52 + 30 = 82.')),
            (3, lambda R: zahl('Der Mittelwert von fünf aufeinanderfolgenden natürlichen Zahlen ist 23. Wie heißt die größte der fünf Zahlen?', 25, '23 + 2',
                               'Bei aufeinanderfolgenden Zahlen steht der Mittelwert genau in der Mitte.', 'Die Zahlen sind 21, 22, 23, 24, 25. Summe 115, 115 : 5 = 23. Größte: 25.')),
            (3, lambda R: wahl(R, 'Bei welchem Notenspiegel ist der Durchschnitt genau 3,0?', '1: 2, 2: 4, 3: 6, 4: 4, 5: 2, 6: 0',
                               ['1: 4, 2: 4, 3: 6, 4: 4, 5: 2, 6: 0', '1: 2, 2: 4, 3: 6, 4: 4, 5: 0, 6: 2', '1: 0, 2: 4, 3: 6, 4: 4, 5: 2, 6: 2'],
                               'Rechne Note mal Anzahl, addiere und teile durch die Zahl der Kinder.',
                               '2 · 1 + 4 · 2 + 6 · 3 + 4 · 4 + 2 · 5 = 54 Punkte für 18 Kinder. 54 : 18 = 3,0. Die anderen ergeben 56 : 20 = 2,8; 56 : 18 ≈ 3,1; 64 : 18 ≈ 3,6.')),
            (3, lambda R: wahl(R, 'Ein Kind hat in vier Tests 14, 17, 12 und 13 Punkte. Es sagt: „Ohne den schlechtesten Test wäre mein Mittelwert um mehr als 1 Punkt höher.“ Stimmt das?',
                               'Nein, er wäre nur um etwa 0,7 Punkte höher.', ['Ja, um genau 2 Punkte.', 'Ja, um 1,5 Punkte.', 'Nein, er bliebe gleich.'],
                               'Rechne beide Mittelwerte aus.', 'Mit allen: 56 : 4 = 14. Ohne die 12: 44 : 3 ≈ 14,7. Unterschied etwa 0,7 Punkte.')),
        ],
        'mittel_tabelle': [
            (2, lambda R: zahl('Die Tabelle zeigt die Umfrage „Wie viele Geschwister hast du?“ in einer Klasse. Berechne den Mittelwert.', Fr('1.25'), '(0 * 4 + 1 * 9 + 2 * 5 + 3 * 2) / 20',
                               'Wert mal Anzahl, addieren, durch die Zahl der Kinder teilen.', '0 · 4 + 1 · 9 + 2 · 5 + 3 · 2 = 25. 20 Kinder. 25 : 20 = 1,25.',
                               grafik=tabelle(['Geschwister', '0', '1', '2', '3'], [['Kinder', '4', '9', '5', '2']]))),
            (2, lambda R: zahl('Die Tabelle zeigt einen Notenspiegel. Berechne die Durchschnittsnote.', 3, '(1 * 3 + 2 * 6 + 3 * 8 + 4 * 5 + 5 * 2 + 6 * 1) / 25',
                               'Note mal Anzahl, addieren, durch die Zahl der Kinder teilen.', '3 + 12 + 24 + 20 + 10 + 6 = 75. 25 Kinder. 75 : 25 = 3.',
                               grafik=tabelle(['Note', '1', '2', '3', '4', '5', '6'], [['Anzahl', '3', '6', '8', '5', '2', '1']]))),
            (3, lambda R: zahl('An einer Schule zahlen 55 % der Kinder 8 € Kopiergeld, 20 % zahlen 10 € und 25 % zahlen 12 €. Wie viel Euro zahlt ein Kind im Durchschnitt?',
                               Fr('9.4'), '(55 * 8 + 20 * 10 + 25 * 12) / 100', 'Rechne mit 100 Kindern.',
                               '100 Kinder: 55 · 8 € + 20 · 10 € + 25 · 12 € = 440 € + 200 € + 300 € = 940 €. 940 € : 100 = 9,40 €.', einheit='€')),
            (3, lambda R: zahl('An einer Schule zahlen 55 % der Kinder 8 € Kopiergeld, 20 % zahlen 10 € und 25 % zahlen 12 €. Im nächsten Jahr zahlt die erste Gruppe 1 € mehr, '
                               'die zweite Gruppe 1 € weniger. Um wie viel Euro steigt der Durchschnitt?', Fr('0.35'), '(55 * 1 - 20 * 1) / 100',
                               'Die Gruppen sind verschieden groß. Rechne wieder mit 100 Kindern.',
                               '55 Kinder zahlen zusammen 55 € mehr, 20 Kinder 20 € weniger. Plus 35 € für 100 Kinder: 0,35 € mehr. (Es hebt sich nicht auf!)', einheit='€')),
            (3, lambda R: zahl('Im Notenspiegel ist eine Anzahl verwischt: Note 1: 2 Kinder, Note 2: 3 Kinder, Note 3: ? Kinder, Note 4: 2 Kinder. '
                               'Der Durchschnitt ist genau 2,5. Wie viele Kinder haben Note 3?', 3, '(2.5 * 7 - (2 + 6 + 8)) / (3 - 2.5)',
                               'Probiere aus: 1, 2, 3 … Kinder mit Note 3. Rechne jeweils den Durchschnitt.',
                               'Mit 3 Kindern: 2 + 6 + 9 + 8 = 25 Notenpunkte für 10 Kinder. 25 : 10 = 2,5. Es passt.')),
            (3, lambda R: zahl('Eine Mannschaft hat in 4 Spielen 0 Tore, in 3 Spielen 1 Tor und in 3 Spielen 2 Tore geschossen. Ein Kind rechnet den Mittelwert als (0 + 1 + 2) : 3 = 1. '
                               'Wie groß ist er richtig?', Fr('0.9'), '(0 * 4 + 1 * 3 + 2 * 3) / 10', 'Jeder Wert zählt so oft, wie er vorkommt.',
                               'Tore: 0 · 4 + 1 · 3 + 2 · 3 = 9 in 10 Spielen. 9 : 10 = 0,9.')),
        ],
        'mittel_rueckwaerts': [
            (2, lambda R: zahl('Der Mittelwert von vier Zahlen ist 7,5. Drei der Zahlen sind 6, 9 und 8. Wie heißt die vierte Zahl?', 7, '7.5 * 4 - 6 - 9 - 8',
                               'Summe = Mittelwert · Anzahl.', 'Summe 7,5 · 4 = 30. 30 − 6 − 9 − 8 = 7.')),
            (2, lambda R: zahl('Eine Familie mit 4 Personen schaut im Mittel 1,5 Stunden am Tag auf Bildschirme. Wie viele Stunden sind das zusammen an einem Tag?', 6, '1.5 * 4',
                               'Summe = Mittelwert · Anzahl.', '1,5 h · 4 = 6 h.', einheit='h')),
            (3, lambda R: zahl('Nach drei Schulaufgaben hat ein Kind den Durchschnitt 3,0. Welche Note braucht es in der vierten Schulaufgabe, damit der Durchschnitt 2,5 wird?', 1,
                               '2.5 * 4 - 3 * 3', 'Wie viele Notenpunkte braucht es nach vier Arbeiten insgesamt?', 'Bisher 3 · 3,0 = 9. Nötig 4 · 2,5 = 10. 10 − 9 = 1, also eine 1.')),
            (3, lambda R: zahl('Fünf Kinder sind im Mittel 1,50 m groß. Ein Kind mit 1,62 m verlässt die Gruppe. Wie groß sind die übrigen vier im Mittel?', Fr('1.47'),
                               '(1.5 * 5 - 1.62) / 4', 'Rechne die Summe aller Größen aus und ziehe 1,62 m ab.', 'Summe 5 · 1,50 m = 7,50 m. 7,50 − 1,62 = 5,88 m. 5,88 : 4 = 1,47 m.', einheit='m')),
            (3, lambda R: zahl('Der Mittelwert von 3, 8, 10 und x ist genauso groß wie x. Wie groß ist x?', 7, '(3 + 8 + 10) / 3',
                               'Probiere Werte für x aus, oder: Wenn x der Mittelwert ist, gleichen sich die Abstände der anderen Zahlen zu x aus.',
                               'x = 7: (3 + 8 + 10 + 7) : 4 = 28 : 4 = 7. Es passt.')),
            (3, lambda R: zahl('In der 6a (20 Kinder) sind es im Mittel 12 Punkte, in der 6b (30 Kinder) 17 Punkte. Wie groß ist der Mittelwert aller 50 Kinder?', 15,
                               '(20 * 12 + 30 * 17) / 50', 'Rechne die Punktsumme jeder Klasse aus. Die Klassen sind verschieden groß.',
                               '6a: 240 Punkte, 6b: 510 Punkte. 750 : 50 = 15. (Nicht (12 + 17) : 2 = 14,5.)')),
        ],
        'modal_spannweite': [
            (2, lambda R: zahl('Bestimme die Spannweite von 2,4; 3,9; 1,7 und 2,8.', Fr('2.2'), '3.9 - 1.7', 'Größter minus kleinster Wert.', '3,9 − 1,7 = 2,2.')),
            (2, lambda R: wahl(R, 'Lieblingsfarben: rot, blau, rot, grün, blau, rot, gelb. Welcher Wert ist der Modalwert?', 'rot', ['blau', 'grün', 'Es gibt keinen.'],
                               'Welche Farbe kommt am häufigsten vor?', 'rot 3-mal, blau 2-mal, grün und gelb je 1-mal. Modalwert: rot.')),
            (3, lambda R: zahl('Eine Datenreihe hat die Spannweite 12. Der kleinste Wert ist −5. Wie groß ist der größte Wert?', 7, '-5 + 12', 'Rückwärts: größter = kleinster + Spannweite.',
                               'Größter Wert = kleinster Wert + Spannweite = −5 + 12 = 7.')),
            (3, lambda R: zahl('Zur Reihe 4, 7, 7, 9 kommt eine Zahl größer als 9 dazu. Danach ist die Spannweite 10 und der Modalwert immer noch 7. Welche Zahl kommt dazu?', 14, '4 + 10',
                               'Der kleinste Wert bleibt 4. Was muss der größte sein?', 'Spannweite 10 mit kleinstem Wert 4: größter Wert 14. Die 7 bleibt am häufigsten.')),
            (3, lambda R: zahl('Das Diagramm zeigt die Noten 1 bis 5 einer Klasse. Note 6 fehlt noch. Wie viele Kinder dürfen höchstens Note 6 haben, '
                               'damit Note 3 der einzige Modalwert bleibt?', 7, '8 - 1', 'Wie oft kommt Note 3 vor? Note 6 muss seltener sein.',
                               'Note 3 haben 8 Kinder. Note 6 darf höchstens 7-mal vorkommen, sonst gäbe es einen zweiten Modalwert.',
                               grafik=saeulen([('1', 2), ('2', 6), ('3', 8), ('4', 5), ('5', 3)], einheit='Kinder'))),
            (3, lambda R: zahl('Ein Kind sagt: „Die Spannweite von 12, 5, 9, 20 ist 8, weil 20 − 12 = 8.“ Wie groß ist die Spannweite richtig?', 15, '20 - 5',
                               'Nicht erster und letzter Wert, sondern größter und kleinster.', 'Größter Wert 20, kleinster 5. 20 − 5 = 15.')),
        ],
        'median': [
            (2, lambda R: zahl('Bestimme den Median von 3, 9, 4, 9, 1, 7.', Fr('5.5'), '(4 + 7) / 2', 'Ordne zuerst. Bei 6 Werten gibt es zwei mittlere.',
                               'Geordnet: 1, 3, 4, 7, 9, 9. Mitte: (4 + 7) : 2 = 5,5.')),
            (2, lambda R: zahl('Bestimme den Median von −2, 5, 0, −7, 3.', 0, '0', 'Ordne zuerst, auch die negativen Zahlen.', 'Geordnet: −7, −2, 0, 3, 5. In der Mitte steht 0.')),
            (3, lambda R: zahl('Punkte von 13 Kindern: 4, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 9, 10. Bestimme den Median.', 8, '8',
                               'Bei 13 Werten ist der 7. Wert die Mitte. Zähle genau, auch die doppelten Werte.',
                               'Die Werte sind schon geordnet. Der 7. Wert ist 8 (6 Werte davor, 6 danach).')),
            (3, lambda R: zahl('Die Tabelle zeigt, wie viele Runden 150 Kinder beim Spendenlauf geschafft haben. Bestimme den Median der Runden.', 15, '15',
                               'Bei 150 Werten liegen der 75. und 76. Wert in der Mitte. Zähle von vorne zusammen.',
                               '5 Runden: Platz 1–24. 10 Runden: Platz 25–74. 15 Runden: Platz 75–114. Der 75. und 76. Wert sind 15, also Median 15 (knapp nicht 10).',
                               grafik=_RUNDEN)),
            (3, lambda R: zahl('Zur Reihe 2, 5, 9, 12 kommt eine Zahl dazu. Danach ist der Median genau 6. Welche Zahl kommt dazu?', 6, '6',
                               'Bei 5 Werten ist der Median der 3. Wert der geordneten Reihe.', 'Damit der 3. Wert 6 ist, muss die neue Zahl 6 sein: 2, 5, 6, 9, 12.')),
            (3, lambda R: zahl('Median und Mittelwert von 3, 4, 5, 6 und x sollen gleich groß sein. x ist größer als 6. Wie groß ist x?', 7, '5 * 5 - (3 + 4 + 5 + 6)',
                               'Der Median ist 5 (x steht ganz rechts). Welche Summe braucht der Mittelwert 5?', 'Median 5. Mittelwert 5 heißt Summe 25. 25 − 18 = 7.')),
        ],
        'verstehen': [
            (2, lambda R: wahl(R, 'Stimmt die Aussage? „Der Mittelwert liegt immer zwischen dem kleinsten und dem größten Wert (oder ist gleich einem von ihnen).“',
                               'Ja: Beim gerechten Verteilen bekommt niemand mehr als der Größte oder weniger als der Kleinste hatte.',
                               ['Nein, Gegenbeispiel 2, 4, 6.', 'Nein, bei Ausreißern kann er größer sein als der größte Wert.'],
                               'Denke an gerechtes Verteilen.', 'Teilt man gerecht, gibt der Größte ab und der Kleinste bekommt dazu. Der Mittelwert liegt dazwischen.', n=3)),
            (2, lambda R: wahl(R, 'Stimmt die Aussage? „Verdoppelt man alle Werte, verdoppelt sich auch der Mittelwert.“', 'Ja: Die Summe verdoppelt sich, die Anzahl bleibt gleich.',
                               ['Nein, der Mittelwert bleibt gleich.', 'Nein, er wird um 2 größer.'], 'Probiere mit 1, 2, 3.', '1, 2, 3 → Mittel 2. 2, 4, 6 → Mittel 4.', n=3)),
            (3, lambda R: wahl(R, 'Klasse A hat im Mittel 12 Punkte, Klasse B 18 Punkte. Jemand sagt: „Der Mittelwert aller Kinder ist (12 + 18) : 2 = 15.“ Stimmt das?',
                               'Nur wenn beide Klassen gleich viele Kinder haben.', ['Ja, immer.', 'Nein, nie.', 'Nur wenn Klasse A mehr Kinder hat.'],
                               'Probiere: A hat 10 Kinder, B hat 30 Kinder.', 'Bei 10 und 30 Kindern: (120 + 540) : 40 = 16,5, nicht 15. Bei gleich großen Klassen passt 15.')),
            (3, lambda R: wahl(R, 'Stimmt die Aussage? „Der Median ist immer einer der Datenwerte.“', 'Nein: Bei 1, 2, 3, 4 ist der Median 2,5.',
                               ['Ja, er ist immer der mittlere Wert der Liste.', 'Nein: Der Median ist nie ein Datenwert.', 'Ja, außer bei negativen Zahlen.'],
                               'Denke an eine gerade Anzahl von Werten.', 'Bei gerader Anzahl ist der Median der Mittelwert der beiden mittleren Werte, z. B. (2 + 3) : 2 = 2,5.')),
            (3, lambda R: zahl('Drei natürliche Zahlen haben den Mittelwert 10 und den Median 4. Wie groß ist die größte Zahl mindestens?', 22, '3 * 10 - 4 - 4',
                               'Die Summe ist 30. Die kleinste Zahl ist höchstens 4. Wie groß darf sie sein, damit die größte möglichst klein wird?',
                               'Summe 30, Median 4. Die kleinste Zahl ist höchstens 4. Mit 4, 4, x: x = 30 − 8 = 22. Kleiner geht es nicht.')),
            (3, lambda R: wahl(R, 'Bei einem Test war der Mittelwert 15 Punkte, der Median 17 Punkte. Lisa hat 16 Punkte. Sie sagt: „Ich bin besser als die Hälfte der Klasse.“ Stimmt das?',
                               'Nein: Mindestens die Hälfte hat 17 Punkte oder mehr.', ['Ja, denn 16 ist mehr als der Mittelwert 15.', 'Ja, genau die Hälfte ist schlechter.', 'Das kann man nicht entscheiden.'],
                               'Was sagt der Median über die Hälfte der Klasse?',
                               'Median 17: Die bessere Hälfte hat mindestens 17 Punkte. Mit 16 liegt Lisa unter dem Median. Der Mittelwert sagt darüber nichts.')),
        ],
    }


ergaenzen(DATEI, _kw(), seed=6058)


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('daten.kennwerte', 13_6_8)
# a) Grundform mit negativen Zahlen → Stufe 2
BF.stufe('modal_spannweite', 'Bestimme die Spannweite von 7, 8, 7, 4, 7, 7, 10, 1, 2, −5, 8, −4.', 2)
BF.stufe('modal_spannweite', 'Bestimme die Spannweite von −2, 0, 2, 6, 12, 7, 9, 7, −4, 0, 7, −5.', 2)
BF.stufe('modal_spannweite', 'Temperaturen am Morgen in einer Woche (°C): −6, −2, −5, 1, −5, 5, 12. Wie groß ist die Spannweite?', 2)
# a)/c) sechs Aufgaben mit wörtlich gleichem Text auf Stufe 2 und 3: eine Stufe-3-Aufgabe (Mittel 1) → Stufe 2,
#        zwei Stufe-3-Aufgaben → andere Frage zur selben Tabelle
_q = 'Die Tabelle zeigt die Umfrage „Wie viele Geschwister hast du?“. Wie viele Geschwister hat ein Kind im Mittel?'
BF.stufe('mittel_tabelle', _q, 2, enthaelt='"4", "6", "2", "1"')
_t1 = {"typ": "tabelle", "kopf": ["Geschwister", "0", "1", "2", "3"], "zeilen": [["Anzahl Kinder", "4", "2", "2", "4"]]}
_t2 = {"typ": "tabelle", "kopf": ["Geschwister", "0", "1", "2", "3"], "zeilen": [["Anzahl Kinder", "7", "6", "3", "4"]]}
BF.ersetze('mittel_tabelle', _q, BF.Z(
    'Die Tabelle zeigt die Umfrage „Wie viele Geschwister hast du?“. Wie viele Kinder mit 3 Geschwistern müssten noch dazukommen, damit der Mittelwert genau 2 ist?',
    6, '(2 * 12 - 18) / (3 - 2)',
    'Bisher: Summe 0 · 4 + 1 · 2 + 2 · 2 + 3 · 4 = 18, Anzahl 12. Für Mittel 2 bräuchte man Summe 2 · Anzahl. Jedes neue Kind bringt 3, also 1 mehr als 2: Es fehlen 2 · 12 − 18 = 6, also 6 Kinder. Probe: 36 : 18 = 2.',
    'Wie groß müsste die Summe sein? Um wie viel erhöht jedes neue Kind die Summe mehr als nötig?', grafik=_t1), enthaelt='"4", "2", "2", "4"')
BF.ersetze('mittel_tabelle', _q, BF.Z(
    'Die Tabelle zeigt die Umfrage „Wie viele Geschwister hast du?“. Jemand rechnet (0 + 1 + 2 + 3) : 4 = 1,5. Wie groß ist der Mittelwert richtig?',
    1.2, '(0 * 7 + 1 * 6 + 2 * 3 + 3 * 4) / (7 + 6 + 3 + 4)',
    'Falsch ist, nur die vier Spaltenwerte zu mitteln. Jede Anzahl zählt so oft, wie Kinder sie haben: Summe 0 · 7 + 1 · 6 + 2 · 3 + 3 · 4 = 24, Anzahl 20. Mittelwert: 24 : 20 = 1,2.',
    'Wie viele Kinder wurden befragt? Jedes Kind zählt einmal.', grafik=_t2), enthaelt='"7", "6", "3", "4"')
# c) vierfach dieselbe Taschengeld-Aufgabe → zwei mit anderem Gedanken
BF.ersetze('verstehen', 'Stimmt die Aussage? „Taschengeld (€): 9, 8, 8, 9, 77. Der Median beschreibt ein typisches Kind besser als der Mittelwert.“', BF.Z(
    'Taschengeld (€): 9, 8, 8, 9, 77. Um wie viel € ist der Mittelwert größer als der Median?', 13.2, '(9 + 8 + 8 + 9 + 77) / 5 - 9',
    'Mittelwert: 111 : 5 = 22,2 €. Geordnet 8, 8, 9, 9, 77: Median 9 €. Unterschied: 22,2 − 9 = 13,2 €. Der Ausreißer 77 € zieht nur den Mittelwert nach oben.',
    'Berechne beide Werte. Für den Median zuerst ordnen.', einheit='€'))
BF.ersetze('verstehen', 'Stimmt die Aussage? „Taschengeld (€): 7, 4, 11, 12, 82. Der Median beschreibt ein typisches Kind besser als der Mittelwert.“', BF.A(
    'Stimmt die Aussage? „Lässt man bei 7, 4, 11, 12, 82 den Wert 82 weg, ändert sich der Median nicht.“',
    'Nein: Vorher ist der Median 11, danach (4, 7, 11, 12) ist er (7 + 11) : 2 = 9.',
    ['Ja, ein Ausreißer verändert den Median nie.', 'Ja, der Median bleibt immer 11.'],
    'Geordnet 4, 7, 11, 12, 82: Median 11. Ohne 82 bleiben 4 Werte, der Median ist der Mittelwert der beiden mittleren: (7 + 11) : 2 = 9. Er ändert sich – aber viel weniger als der Mittelwert (23,2 → 8,5).',
    'Ordne die Werte und bestimme den Median vorher und nachher.'))
BF.fuer_sebastian('daten.kennwerte: laut themenliste lehrplan_gym ist für Kl. 6 nur „Arithmetisches Mittel bestimmen“ vorgesehen; die Karten modal_spannweite und median gehen darüber hinaus (BMT8-Stoff bis Kl. 7). Als Vertiefung führen? Karten nicht geändert.')

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----


# ---------- DURCHSICHT (Neunzehnte Runde, Teil A, Zweig durchsicht-kl6) ----------
from _durchsicht_kl6 import Befunde, befunde_anwenden  # noqa: E402

DS = Befunde('daten.kennwerte', 19_6_9)
_S = DS.stufe
_R = {
    # mittelwert: Mittelwert eingekleidet ausrechnen bzw. zwei Mittelwerte vergleichen (viermal) = Stufe 2
    'mittelwert': ('Ein Kind läuft an 7 Tagen 42 min, 20 min, 57 min, 24 min, 17 min, 36 min, 42 min. Wie viele Minuten läuft es im Durchschnitt pro Tag?',
                   'Ein Kind läuft an 5 Tagen 36 min, 28 min, 14 min, 35 min, 27 min. Wie viele Minuten läuft es im Durchschnitt pro Tag?',
                   'Gruppe A sammelt 7 kg, 4 kg, 7 kg, 4 kg Altpapier, Gruppe B 8 kg, 12 kg, 7 kg, 11 kg. Welche Gruppe hat im Mittel mehr gesammelt?',
                   'Gruppe A sammelt 4 kg, 6 kg, 2 kg, 2 kg Altpapier, Gruppe B 8 kg, 11 kg, 9 kg, 2 kg. Welche Gruppe hat im Mittel mehr gesammelt?',
                   'Gruppe A sammelt 5 kg, 12 kg, 10 kg, 9 kg Altpapier, Gruppe B 2 kg, 9 kg, 11 kg, 2 kg. Welche Gruppe hat im Mittel mehr gesammelt?'),
    # mittel_rueckwaerts: „Kind kommt dazu“ und „nächster Test“ je dreimal → je zwei nach S2
    'mittel_rueckwaerts': ('4 Kinder haben im Mittel 15 Punkte. Ein weiteres Kind kommt mit 3 Punkten dazu. Wie groß ist der neue Mittelwert?',
                           '9 Kinder haben im Mittel 12 Punkte. Ein weiteres Kind kommt mit 2 Punkten dazu. Wie groß ist der neue Mittelwert?',
                           'Nach 4 Tests hat ein Kind im Mittel 6 Punkte. Wie viele Punkte braucht es im nächsten Test, damit der Mittelwert auf 7 steigt?',
                           'Nach 5 Tests hat ein Kind im Mittel 11 Punkte. Wie viele Punkte braucht es im nächsten Test, damit der Mittelwert auf 13 steigt?'),
    # modal_spannweite: Modalwert/Spannweite einer langen Reihe = Stufe 2 (nur mehr Werte)
    'modal_spannweite': ('Welcher Wert ist der Modalwert von 42, 35, 35, 37, 38, 41, 33, 34, 37, 33, 35, 32?',
                         'Bestimme die Spannweite von 124, 139, 151, 148, 157, 160, 122, 157, 155, 141, 144, 121.'),
    # median: Median einer ungeordneten Reihe = Stufe 2; zweiter gleicher Fehler und zweiter Ausreißer-Vergleich → S2
    'median': ('Bestimme den Median von 26, 13, 20, 34, 40, 24, 34, 4.', 'Bestimme den Median von 4, 28, 21, 6, 40, 9, 13, 4, 3, 35, 20.',
               'Punkte von 13 Kindern: 4, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 9, 10. Bestimme den Median.',
               'Jemand sagt: „Der Median von 7, 9, 13, 17 ist 13.“ Was ist falsch?', 'Daten: 27, 26, 25, 24, 5, 18, 14, 208. Welchen Kennwert verändert der Ausreißer 208 stärker?'),
    # verstehen: „Median typisch?“ dreimal → zwei nach S2; Ausreißer weglassen → Mittelwert kleiner ist direkt
    'verstehen': ('Stimmt die Aussage? „Taschengeld (€): 2, 6, 2, 6, 6, 52. Der Mittelwert zeigt gut, was ein typisches Kind bekommt.“',
                  'Stimmt die Aussage? „Taschengeld (€): 11, 4, 7, 9, 10, 41. Der Median beschreibt ein typisches Kind besser als der Mittelwert.“',
                  'Stimmt die Aussage? „Lässt man bei 11, 6, 10, 6, 2, 88 den Ausreißer 88 weg, wird der Mittelwert kleiner.“'),
}
for _lz, _ts in _R.items():
    for _t in _ts:
        _S(_lz, _t, 2)
# mittel_tabelle: Mittelwert aus Tabelle ablesen = genau das Stufe-2-Muster
_S('mittel_tabelle', 'Die Tabelle zeigt, wie viele Tore eine Mannschaft in ihren Spielen geschossen hat. Wie viele Tore schießt sie im Mittel pro Spiel?', 2, enthaelt='"s": 3', anzahl=2)
_S('mittel_tabelle', 'Die Tabelle zeigt die Umfrage „Wie viele Geschwister hast du?“. Wie viele Geschwister hat ein Kind im Mittel?', 2, enthaelt='"s": 3')
DS.fuer_sebastian('daten.kennwerte: Modalwert, Spannweite und Median stehen nicht im LehrplanPLUS M6 (dort: arithmetisches Mittel); die Karten modal_spannweite und median sind als Vertiefung markiert – so lassen?')
befunde_anwenden(DATEI, DS)
# ---- DURCHSICHT ENDE ----


if __name__ == '__main__':
    schreibe(DATEI)
