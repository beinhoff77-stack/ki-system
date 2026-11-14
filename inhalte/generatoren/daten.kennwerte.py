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
     'regel': 'Das ⟦arithmetische Mittel⟧ (der Mittelwert, „Durchschnitt“) ist ⟦Summe aller Werte : Anzahl der Werte⟧. Er gibt an, wie groß jeder Wert wäre, wenn alle ⟦gleich verteilt⟧ wären.',
     'schritte': ['Punkte: 7, 9, 4, 8. Summe: 7 + 9 + 4 + 8 = 28.', 'Anzahl: 4 Werte. Mittelwert: 28 : 4 = ⟦7⟧.'],
     'probe': '4 · 7 = 28 ✓',
     'fehler': 'Bei 7, 9, 4, 8 durch 28 : 2 = 14 zu teilen ist falsch: Geteilt wird durch die ⟦Anzahl der Werte⟧ (4), nicht durch 2.'},
    {'lernziel': 'mittel_tabelle', 'titel': 'Mittelwert aus einer Häufigkeitstabelle',
     'regel': 'Steht in einer Tabelle, wie oft ein Wert vorkommt, rechnest du ⟦jeden Wert mal seine Häufigkeit⟧, addierst alles und teilst durch die ⟦Gesamtzahl⟧ der Werte.',
     'schritte': ['Noten: 1 → 2-mal, 2 → 5-mal, 3 → 3-mal. Summe: 1 · 2 + 2 · 5 + 3 · 3 = 21.', 'Anzahl: 2 + 5 + 3 = 10. Mittelwert: 21 : 10 = ⟦2,1⟧.'],
     'fehler': 'Die Werte 1, 2, 3 einfach zu mitteln ((1 + 2 + 3) : 3 = 2) ist falsch: Jeder Wert zählt so oft, wie er ⟦vorkommt⟧.'},
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
     'fehler': 'Den mittleren Wert der ⟦ungeordneten⟧ Liste zu nehmen (hier 8, zufällig richtig – bei 12, 3, 20, 5, 8 wäre es 20) ist falsch. Zuerst ⟦ordnen⟧!'},
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
def g_mittel(st):
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
        return {'y': 'zahl', 'f': {'text': f'{name}: {lt(xs, e)}. Berechne den Mittelwert.'}, 'o': {'wert': wert(m), **({'einheit': e.strip()} if e else {})},
                'c': f'({" + ".join(zt(x).replace(",", ".").replace("−", "-").replace(" ", "") for x in xs)}) / {n}',
                'w': f'Summe: {zt(sum(xs))}{e}. Anzahl: {n}. Mittelwert: {zt(sum(xs))} : {n} = {zt(m)}{e}.', 'h': 'Summe durch Anzahl. Negative Werte beim Addieren beachten.'}
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
def g_tab(st):
    werte = {1: [1, 2, 3], 2: [1, 2, 3, 4, 5], 3: [1, 2, 3, 4, 5, 6]}[st]
    while True:
        h = [R.randint(0 if st == 3 else 1, 8) for _ in werte]
        n = sum(h)
        s = sum(w * k for w, k in zip(werte, h))
        m = Fr(s, n)
        if n > 0 and (m * 100).denominator == 1: break
    art = R.choice(['Note', 'Tore', 'Geschwister'])
    if art == 'Note':
        txt = ' | '.join(f'Note {w}: {k}-mal' for w, k in zip(werte, h))
        frage = f'Notenspiegel – {txt}. Berechne die Durchschnittsnote.'
    elif art == 'Tore':
        txt = ' | '.join(f'{w - 1} Tore: {k} Spiele' for w, k in zip(werte, h))
        werte_t = [w - 1 for w in werte]
        s = sum(w * k for w, k in zip(werte_t, h)); m = Fr(s, n)
        if (m * 100).denominator != 1: return g_tab(st)
        return {'y': 'zahl', 'f': {'text': f'Tore einer Mannschaft – {txt}. Wie viele Tore schießt sie im Mittel pro Spiel?'}, 'o': {'wert': wert(m)},
                'c': f'({" + ".join(f"{w} * {k}" for w, k in zip(werte_t, h))}) / ({" + ".join(map(str, h))})',
                'w': f'Tore insgesamt: {" + ".join(f"{w} · {k}" for w, k in zip(werte_t, h))} = {s}. Spiele: {n}. Mittel: {s} : {n} = {zt(m)}.', 'h': 'Jede Torzahl mal die Anzahl der Spiele, dann durch alle Spiele teilen.'}
    else:
        werte = [w - 1 for w in werte][:4]
        h = h[:4]
        n = sum(h)
        if n == 0: return g_tab(st)
        s = sum(w * k for w, k in zip(werte, h)); m = Fr(s, n)
        if (m * 100).denominator != 1: return g_tab(st)
        txt = ' | '.join(f'{w}: {k} {"Kind" if k == 1 else "Kinder"}' for w, k in zip(werte, h))
        frage = f'Umfrage „Wie viele Geschwister hast du?“ – {txt}. Wie viele Geschwister hat ein Kind im Mittel?'
    return {'y': 'zahl', 'f': {'text': frage}, 'o': {'wert': wert(m)}, 'c': f'({" + ".join(f"{w} * {k}" for w, k in zip(werte, h))}) / ({" + ".join(map(str, h))})',
            'w': f'Summe: {" + ".join(f"{w} · {k}" for w, k in zip(werte, h))} = {s}. Anzahl: {" + ".join(map(str, h))} = {n}. Mittelwert: {s} : {n} = {zt(m)}.',
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
        m = R.randint(5, 20)
        bek = [R.randint(max(0, m - 8), m + 8) for _ in range(n - 1)]
        x = m * n - sum(bek)
        if x < 0: return g_rueck(2)
        name, e = R.choice([('Punkte', ''), ('Tore', ''), ('km', ' km')])
        return {'y': 'zahl', 'f': {'text': f'Der Mittelwert von {n} Werten ist {m}. Bekannt sind {lt(bek)}. Wie heißt der fehlende Wert?'}, 'o': {'wert': x}, 'c': f'{m} * {n} - (' + ' + '.join(map(str, bek)) + ')',
                'w': f'Summe aller Werte: {m} · {n} = {m * n}. Fehlend: {m * n} − {sum(bek)} = {x}.', 'h': 'Berechne zuerst die Summe aller Werte aus dem Mittelwert.'}
    art = R.randrange(2)
    if art == 0:
        n = R.choice([4, 5, 9])
        m = R.randint(6, 15)
        neu = R.randint(1, 30)
        m2 = Fr(m * n + neu, n + 1)
        if (m2 * 10).denominator != 1: return g_rueck(3)
        return {'y': 'zahl', 'f': {'text': f'{n} Kinder haben im Mittel {m} Punkte. Ein weiteres Kind kommt mit {neu} Punkten dazu. Wie groß ist der neue Mittelwert?'}, 'o': {'wert': wert(m2)},
                'c': f'({m} * {n} + {neu}) / {n + 1}', 'w': f'Alte Summe: {m} · {n} = {m * n}. Neue Summe: {m * n + neu}. Neuer Mittelwert: {m * n + neu} : {n + 1} = {zt(m2)}.',
                'h': 'Berechne die alte Summe, addiere den neuen Wert und teile durch die neue Anzahl.'}
    n = R.choice([3, 4, 5])
    m, ziel = R.randint(6, 12), None
    ziel = m + 1
    x = ziel * (n + 1) - m * n
    return {'y': 'zahl', 'f': {'text': f'Nach {n} Tests hat ein Kind im Mittel {m} Punkte. Wie viele Punkte braucht es im nächsten Test, damit der Mittelwert auf {ziel} steigt?'}, 'o': {'wert': x},
            'c': f'{ziel} * {n + 1} - {m} * {n}', 'w': f'Neue Summe nötig: {ziel} · {n + 1} = {ziel * (n + 1)}. Bisher: {m} · {n} = {m * n}. Benötigt: {x} Punkte.',
            'h': 'Welche Summe braucht man für den neuen Mittelwert? Ziehe die bisherige Summe ab.'}


# ---------- 4 Modalwert und Spannweite ----------
def g_modal(st):
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


# ---------- 6 Verstehen ----------
def g_vers(st):
    n = R.choice([4, 5])
    xs, m = liste_mit_mittel(R, n, 2, 12, 1)
    if st == 1:
        aussagen = [(f'Der Mittelwert von {lt(xs)} muss einer der Werte sein.', m in xs, f'{"Ja, hier zufällig" if m in xs else "Nein"}: Der Mittelwert ist {zt(m)}. Er muss nicht in der Liste vorkommen.'),
                    (f'Der Mittelwert von {lt(xs)} liegt zwischen dem kleinsten und dem größten Wert.', True, f'Ja, er ist {zt(m)} und liegt zwischen {min(xs)} und {max(xs)}.'),
                    (f'Der Mittelwert von {lt(xs)} ist {zt(Fr(sum(xs), 2))}.', False, f'Nein, man teilt durch die Anzahl {n}: {sum(xs)} : {n} = {zt(m)}.')]
    elif st == 2:
        k = R.randint(2, 5)
        aussagen = [(f'Wenn man zu jedem Wert von {lt(xs)} die Zahl {k} addiert, wird auch der Mittelwert um {k} größer.', True, f'Ja, neuer Mittelwert: {zt(m + k)}.'),
                    (f'Wenn ein sehr großer Wert dazukommt, kann der Mittelwert kleiner werden.', False, 'Nein, ein Wert über dem Mittelwert zieht ihn nach oben.'),
                    (f'Der Mittelwert von {lt(xs)} kann eine Dezimalzahl sein, auch wenn alle Werte ganze Zahlen sind.', True, f'Ja, hier z. B. {zt(m)}.' if m.denominator > 1 else 'Ja, z. B. Mittelwert von 1 und 2 ist 1,5.')]
    else:
        ausr = R.randint(40, 90)
        ys = xs + [ausr]
        m2 = Fr(sum(ys), n + 1)
        aussagen = [(f'Taschengeld (€): {lt(ys)}. Der Mittelwert zeigt gut, was ein typisches Kind bekommt.', False,
                     f'Nein, der Ausreißer {ausr} € zieht den Mittelwert auf etwa {zt((m2 * 10 + Fr(1, 2)) // 1 / 10)} €, obwohl fast alle viel weniger bekommen.'),
                    (f'Haben zwei Klassen den gleichen Mittelwert, haben sie auch die gleiche Spannweite.', False, 'Nein, z. B. 5, 5 und 1, 9: beide Mittelwert 5, Spannweiten 0 und 8.'),
                    (f'Die Spannweite von {lt(xs)} ist {max(xs) - min(xs)}.', True, f'Ja, {max(xs)} − {min(xs)} = {max(xs) - min(xs)}.')]
    s, stimmt, grund = R.choice(aussagen)
    if stimmt and not grund.startswith('Ja'): grund = 'Ja. ' + grund
    if not stimmt and not grund.startswith('Nein'): grund = 'Nein. ' + grund
    gegen = 'Ja, die Aussage stimmt.' if not stimmt else 'Nein, die Aussage ist falsch.'
    return {**wahl(R, grund, [gegen, 'Das kann man nicht entscheiden.'], 3), 'f': {'text': f'Stimmt die Aussage? „{s}“'},
            'w': grund, 'h': 'Rechne nach oder suche ein Gegenbeispiel.'}


GEN = {'mittelwert': g_mittel, 'mittel_tabelle': g_tab, 'mittel_rueckwaerts': g_rueck, 'modal_spannweite': g_modal, 'median': g_median, 'verstehen': g_vers}

DATEI = datei(E, 'Das arithmetische Mittel bestimmen und deuten, Modalwert, Spannweite und Median ermitteln und Kennwerte kritisch beurteilen.', MERKE,
              [('Mittelwert', ['mittelwert', 'mittel_tabelle', 'mittel_rueckwaerts']),
               ('Weitere Kennwerte', ['modal_spannweite', 'median', 'verstehen'])],
              ETAPPEN, GEN, vertiefung=['median'],
              offen=['„umfang“ nennt Median, Quartile und Boxplot; der Kl.-6-Lehrplan (lehrplan_gym) verlangt nur das arithmetische Mittel. Quartile und Boxplot weggelassen (höhere Klasse, Boxplot braucht außerdem eine Zeichnung). Median als Vertiefung (nicht Pflicht) aufgenommen, Modalwert und Spannweite als einfache Ergänzung zum Mittelwert.',
                     'Falls der Median doch Pflicht werden soll: in bewertung.lernziele_pflicht verschieben.'])

if __name__ == '__main__':
    schreibe(DATEI)
