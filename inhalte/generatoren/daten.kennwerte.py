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
              ETAPPEN, GEN, vertiefung=['median'],
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


if __name__ == '__main__':
    schreibe(DATEI)
