#!/usr/bin/env python3
"""Thema daten.darstellen – Daten erfassen und darstellen (Klasse 6)."""
import random
import sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _basis import *  # noqa: E402,F403

R = random.Random(57)
E = eintrag_laden('daten.darstellen')
HB = 'Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt.'

ETAPPEN = [
    {'lernziel': 'absolute_haeufigkeit', 'titel': 'Absolute Häufigkeit zählen',
     'regel': 'Die ⟦absolute Häufigkeit⟧ gibt an, ⟦wie oft⟧ ein Ergebnis vorkommt. Die gesammelten Daten in ihrer Reihenfolge heißen ⟦Urliste⟧. Zum Zählen hilft eine ⟦Strichliste⟧: ein Strich pro Wert, jeder fünfte Strich wird quer über die vier anderen gezogen.',
     'schritte': ['Urliste: 2, 4, 2, 6, 2, 4. Strichliste: 2 → III, 4 → II, 6 → I.', 'Die absolute Häufigkeit von 2 ist ⟦3⟧.'],
     'fehler': 'Die Anzahl ⟦verschiedener⟧ Werte (hier 3: die 2, die 4 und die 6) ist keine Häufigkeit. Die absolute Häufigkeit zählt, ⟦wie oft⟧ ein bestimmter Wert vorkommt.'},
    {'lernziel': 'relative_haeufigkeit', 'titel': 'Relative Häufigkeit bestimmen',
     'regel': 'Die ⟦relative Häufigkeit⟧ ist der ⟦Anteil⟧ an allen Werten: ⟦absolute Häufigkeit : Gesamtzahl⟧. Man gibt sie als Bruch, Dezimalzahl oder in Prozent an. Alle relativen Häufigkeiten zusammen ergeben ⟦1 = 100 %⟧.',
     'schritte': ['Von 25 Würfen zeigen 7 eine Sechs. Relative Häufigkeit: 7/25.', '7/25 = 0,28 = ⟦28 %⟧.'],
     'fehler': '7 Sechsen bei 25 Würfen sind ⟦nicht⟧ 7 %: Man muss durch die ⟦Gesamtzahl⟧ teilen. 7 : 25 = 0,28 = 28 %.'},
    {'lernziel': 'tabelle_auswerten', 'titel': 'Häufigkeitstabellen auswerten',
     'regel': 'In einer ⟦Häufigkeitstabelle⟧ stehen die Ergebnisse und ihre Häufigkeiten. Die ⟦Summe⟧ aller absoluten Häufigkeiten ist die ⟦Gesamtzahl⟧ – sie ist der Grundwert für alle Anteile.',
     'schritte': ['Tabelle Schulweg: Bus 12 | Rad 9 | zu Fuß 6 | Auto 3. Gesamt: 12 + 9 + 6 + 3 = 30.', 'Anteil Rad: 9 : 30 = 0,3 = ⟦30 %⟧.'],
     'fehler': 'Die größte Zahl in der Tabelle ist ⟦nicht⟧ die Gesamtzahl. Die Gesamtzahl ist die ⟦Summe⟧ aller Häufigkeiten (hier 30, nicht 12).'},
    {'lernziel': 'saeulendiagramm', 'titel': 'Säulendiagramme und Maßstab',
     'regel': 'Im ⟦Säulendiagramm⟧ zeigt die ⟦Höhe⟧ jeder Säule die Häufigkeit. Dafür wählt man einen ⟦Maßstab⟧ für die Hochachse, z. B. 1 cm für 4 Kinder. Die Hochachse beginnt bei ⟦0⟧, alle Säulen sind gleich breit.',
     'schritte': ['Maßstab: 1 cm für 4 Kinder. Die Säule für Fußball soll 18 Kinder zeigen.', '18 : 4 = 4,5, also ist die Säule ⟦4,5 cm⟧ hoch.'],
     'fehler': 'Die Säule für 18 Kinder 18 cm hoch zu zeichnen, passt nicht aufs Heft. Erst einen ⟦Maßstab⟧ wählen, dann ⟦Anzahl : Maßstab⟧ rechnen.'},
    {'lernziel': 'kreisdiagramm', 'titel': 'Kreisdiagramme berechnen',
     'regel': 'Im ⟦Kreisdiagramm⟧ ist der ganze Kreis 100 % = ⟦360°⟧. Der Winkel eines Kreisausschnitts ist ⟦relative Häufigkeit · 360°⟧. 1 % entspricht 3,6°. Kreisdiagramme zeigen gut ⟦Anteile am Ganzen⟧.',
     'schritte': ['12 von 40 Kindern kommen mit dem Rad: 12 : 40 = 0,3 = 30 %.', 'Winkel: 0,3 · 360° = ⟦108°⟧.'],
     'probe': '108° : 360° = 0,3 ✓',
     'fehler': '30 % als Winkel von 30° einzuzeichnen ist falsch: Der Vollkreis hat ⟦360°⟧, nicht 100°. 30 % sind 0,3 · 360° = 108°.'},
    {'lernziel': 'irrefuehrend', 'titel': 'Irreführende Diagramme erkennen',
     'regel': 'Diagramme können ⟦täuschen⟧: eine Hochachse, die ⟦nicht bei 0 beginnt⟧, ungleiche Abstände auf der Achse, Bilder statt Säulen (doppelt so hoch und breit = ⟦vierfache Fläche⟧) oder fehlende Beschriftung. Lies immer ⟦Achse und Zahlen⟧.',
     'schritte': ['Zwei Säulen zeigen 980 und 1 000 Besucher, die Hochachse beginnt bei 960. Die Säulen sind 20 und 40 Einheiten hoch.', 'Die zweite wirkt doppelt so hoch, ist aber nur ⟦20 Besucher⟧ (etwa 2 %) mehr.'],
     'fehler': 'Nur auf die Säulenhöhen zu schauen, ohne die Achse zu lesen, ist ein Fehler: Bei abgeschnittener Achse wirken kleine Unterschiede ⟦riesig⟧.'},
]

MERKE = ['Absolute Häufigkeit: wie oft. Relative Häufigkeit: absolute Häufigkeit : Gesamtzahl.', 'Alle relativen Häufigkeiten zusammen: 1 = 100 %.',
         'Säulendiagramm: Höhe = Anzahl : Maßstab, Achse ab 0.', 'Kreisdiagramm: Winkel = relative Häufigkeit · 360°, 1 % = 3,6°.',
         'Täuschung erkennen: Achse ab 0? Gleiche Abstände? Bilder statt Säulen?']

THEMEN = [('Lieblingsobst', ['Apfel', 'Banane', 'Birne', 'Kiwi', 'Mango']), ('Schulweg', ['Bus', 'Rad', 'zu Fuß', 'Auto']),
          ('Lieblingssport', ['Fußball', 'Schwimmen', 'Tanzen', 'Basketball', 'Turnen']), ('Haustier', ['Hund', 'Katze', 'Hamster', 'Fisch', 'keins']),
          ('Lieblingsfach', ['Mathe', 'Deutsch', 'Sport', 'Kunst', 'Musik'])]


def urliste(R, kat, n):
    gew = [R.randint(1, 5) for _ in kat]
    return R.choices(kat, weights=gew, k=n)


def tabelle(R, n_min=20, n_max=40, ziel=None):
    titel, kat = R.choice(THEMEN)
    k = R.randint(3, len(kat))
    kat = kat[:k]
    while True:
        h = [R.randint(1, 15) for _ in kat]
        if ziel is None and n_min <= sum(h) <= n_max and len(set(h)) == len(h): return titel, kat, h
        if ziel and sum(h) == ziel and len(set(h)) == len(h): return titel, kat, h


def tab_text(titel, kat, h): return f'{titel}: ' + ' | '.join(f'{a} {b}' for a, b in zip(kat, h))


def pz(p): return f'{zt(p)} %'


# ---------- 1 Absolute Häufigkeit ----------
def g_abs(st):
    if st == 1:
        n = R.randint(8, 12)
        liste = [R.randint(1, 6) for _ in range(n)]
        w = R.choice(liste)
        k = liste.count(w)
        return {'y': 'zahl', 'f': {'text': f'Würfelergebnisse: {", ".join(map(str, liste))}. Wie oft wurde die {w} gewürfelt?'}, 'o': {'wert': k}, 'c': ' + '.join(['1'] * k),
                'w': f'Die {w} kommt {k}-mal vor. Absolute Häufigkeit: {k}.', 'h': 'Streiche jede gefundene Zahl ab, damit du nichts doppelt zählst.'}
    if st == 2:
        titel, kat = R.choice(THEMEN)
        n = R.randint(14, 22)
        liste = urliste(R, kat, n)
        if R.random() < .3:
            return {'y': 'zahl', 'f': {'text': f'Umfrage {titel}: {", ".join(liste)}. Wie viele Kinder wurden befragt?'}, 'o': {'wert': n}, 'c': ' + '.join(str(v) for v in Counter(liste).values()),
                    'w': 'Häufigkeiten: ' + ', '.join(f'{a} {b}' for a, b in Counter(liste).items()) + f'. Zusammen {n}.', 'h': 'Zähle alle Einträge der Urliste.'}
        w = R.choice(liste)
        k = liste.count(w)
        return {'y': 'zahl', 'f': {'text': f'Umfrage {titel}: {", ".join(liste)}. Wie oft wurde „{w}“ genannt?'}, 'o': {'wert': k}, 'c': ' + '.join(['1'] * k),
                'w': f'„{w}“ steht {k}-mal in der Liste.', 'h': 'Mach eine Strichliste.'}
    art = R.randrange(3)
    if art == 0:
        titel, kat, h = tabelle(R)
        n = sum(h)
        i = R.randrange(len(kat))
        rest = [x for j, x in enumerate(h) if j != i]
        txt = ' | '.join(f'{a} {"?" if j == i else b}' for j, (a, b) in enumerate(zip(kat, h)))
        return {'y': 'zahl', 'f': {'text': f'Es wurden {n} Kinder befragt. {titel}: {txt}. Welche Zahl fehlt bei „{kat[i]}“?'}, 'o': {'wert': h[i]}, 'c': f'{n} - (' + ' + '.join(map(str, rest)) + ')',
                'w': f'{n} − ({" + ".join(map(str, rest))}) = {n} − {sum(rest)} = {h[i]}.', 'h': 'Alle Häufigkeiten zusammen ergeben die Gesamtzahl.'}
    if art == 1:
        titel, kat = R.choice(THEMEN)
        liste = urliste(R, kat, R.randint(15, 22))
        c = Counter(liste)
        a, b = R.sample(list(c), 2)
        if c[a] == c[b]: return g_abs(3)
        if c[a] < c[b]: a, b = b, a
        return {'y': 'zahl', 'f': {'text': f'Umfrage {titel}: {", ".join(liste)}. Wie oft wurde „{a}“ häufiger genannt als „{b}“?'}, 'o': {'wert': c[a] - c[b]}, 'c': f'{c[a]} - {c[b]}',
                'w': f'„{a}“: {c[a]}-mal, „{b}“: {c[b]}-mal. Unterschied: {c[a] - c[b]}.', 'h': 'Zähle beide getrennt und bilde den Unterschied.'}
    k = R.randint(6, 28)
    fuenfer, rest = divmod(k, 5)
    return {'y': 'zahl', 'f': {'text': f'In einer Strichliste stehen bei „Hund“: {fuenfer} Fünferbündel' + (f' und {rest} einzelne Striche.' if rest else '.') + ' Wie oft wurde „Hund“ genannt?'},
            'o': {'wert': k}, 'c': f'{fuenfer} * 5 + {rest}', 'w': f'{fuenfer} Bündel zu je 5 und {rest} einzelne: {fuenfer} · 5 + {rest} = {k}.', 'h': 'Ein Bündel steht für 5 Striche.'}


# ---------- 2 Relative Häufigkeit ----------
def g_rel(st):
    if st == 1:
        n = R.choice([10, 12, 16, 20, 24, 30])
        k = R.randint(1, n - 1)
        x = Fr(k, n)
        ding = R.choice([('Würfen', 'zeigen eine Sechs'), ('Kindern', 'haben ein Haustier'), ('Losen', 'gewinnen'), ('Tagen', 'sind sonnig')])
        return {'y': 'luecken', 'f': {'text': f'{k} von {n} {ding[0]} {ding[1]}. Wie groß ist die relative Häufigkeit als Bruch?', 'schablone': '□/□', 'hinweis': HB},
                'o': {'werte': [x.numerator, x.denominator]}, 'c': [f'{k} / {n} * {x.denominator}', f'{x.denominator}'],
                'w': f'Relative Häufigkeit = {k}/{n}' + (f' = {bruch(x)}.' if x.denominator != n else '.'), 'h': 'Absolute Häufigkeit durch Gesamtzahl. Dann kürzen.'}
    if st == 2:
        n = R.choice([20, 25, 40, 50, 80, 125, 200, 250])
        k = R.randint(1, n - 1)
        if not (Fr(k * 100, n) * 10).denominator == 1: return g_rel(2)
        ding = R.choice([('Kindern', 'fahren Rad'), ('Würfen', 'zeigen „Kopf“'), ('Pflanzen', 'blühen'), ('Besuchern', 'kommen aus der Stadt')])
        return {'y': 'zahl', 'f': {'text': f'{k} von {n} {ding[0]} {ding[1]}. Gib die relative Häufigkeit in Prozent an.'}, 'o': {'wert': wert(Fr(k * 100, n)), 'einheit': '%'},
                'c': f'{k} / {n} * 100', 'w': f'{k} : {n} = {zt(Fr(k, n))} = {pz(Fr(k * 100, n))}.', 'h': 'Teile durch die Gesamtzahl und nimm mal 100.'}
    art = R.randrange(3)
    if art == 0:
        n = R.choice([20, 40, 50, 60, 80, 120, 200])
        p = R.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 75])
        if n * p % 100: return g_rel(3)
        return {'y': 'zahl', 'f': {'text': f'Bei {n} Münzwürfen lag die relative Häufigkeit für „Zahl“ bei {pz(p)}. Wie oft fiel „Zahl“?'}, 'o': {'wert': n * p // 100}, 'c': f'{n} * {p} / 100',
                'w': f'{pz(p)} von {n} = {n} · {zt(Fr(p, 100))} = {n * p // 100}.', 'h': 'Absolute Häufigkeit = relative Häufigkeit · Gesamtzahl.'}
    if art == 1:
        titel, kat = R.choice(THEMEN)
        k = R.randint(3, 4)
        ps = [R.choice([5, 10, 15, 20, 25, 30]) for _ in range(k - 1)]
        if sum(ps) >= 95: return g_rel(3)
        rest = 100 - sum(ps)
        txt = ', '.join(f'{a} {pz(p)}' for a, p in zip(kat, ps))
        return {'y': 'zahl', 'f': {'text': f'{titel}: {txt}, der Rest wählt {kat[k - 1]}. Wie viel Prozent wählen {kat[k - 1]}?'}, 'o': {'wert': rest, 'einheit': '%'},
                'c': '100 - (' + ' + '.join(map(str, ps)) + ')', 'w': f'Alle zusammen sind 100 %. 100 − {sum(ps)} = {rest} %.', 'h': 'Alle relativen Häufigkeiten ergeben zusammen 100 %.'}
    n1, n2 = R.choice([20, 25, 50]), R.choice([40, 80, 100, 200])
    k1 = R.randint(2, n1 - 2)
    k2 = R.randint(2, n2 - 2)
    p1, p2 = Fr(k1 * 100, n1), Fr(k2 * 100, n2)
    if p1 == p2 or not ok2(p1) or not ok2(p2): return g_rel(3)
    r = 'Gruppe A' if p1 > p2 else 'Gruppe B'
    return {**wahl(R, r, ['Gruppe B' if r == 'Gruppe A' else 'Gruppe A', 'Beide gleich', 'Die Gruppe mit mehr Kindern']),
            'f': {'text': f'In Gruppe A ({n1} Kinder) lesen {k1} gern, in Gruppe B ({n2} Kinder) lesen {k2} gern. Wo ist der Anteil der Leser größer?'},
            'w': f'A: {k1} : {n1} = {pz(p1)}, B: {k2} : {n2} = {pz(p2)}. Größerer Anteil: {r}.', 'h': 'Vergleiche Anteile, nicht Anzahlen: relative Häufigkeiten berechnen.'}


def ok2(p): return (Fr(p) * 10).denominator == 1


# ---------- 3 Tabelle auswerten ----------
def g_tab(st):
    titel, kat, h = tabelle(R)
    n = sum(h)
    if st == 1:
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'{tab_text(titel, kat, h)}. Wie viele Kinder wurden insgesamt befragt?'}, 'o': {'wert': n}, 'c': ' + '.join(map(str, h)),
                    'w': f'Alle Häufigkeiten addieren: {" + ".join(map(str, h))} = {n}.', 'h': 'Addiere alle Häufigkeiten.'}
        r = kat[h.index(max(h))]
        return {**wahl(R, r, [k for k in kat if k != r]), 'f': {'text': f'{tab_text(titel, kat, h)}. Was wurde am häufigsten genannt?'},
                'w': f'Die größte Häufigkeit ist {max(h)} bei „{r}“.', 'h': 'Suche die größte Zahl in der Tabelle.'}
    if st == 2:
        i, j = R.sample(range(len(kat)), 2)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'{tab_text(titel, kat, h)}. Wie viele Kinder haben nicht „{kat[i]}“ gewählt?'}, 'o': {'wert': n - h[i]}, 'c': ' + '.join(map(str, h)) + f' - {h[i]}',
                    'w': f'Gesamt {n}, davon {h[i]} „{kat[i]}“. Nicht: {n} − {h[i]} = {n - h[i]}.', 'h': 'Gesamtzahl minus die Häufigkeit dieser Antwort.'}
        return {'y': 'zahl', 'f': {'text': f'{tab_text(titel, kat, h)}. Wie viele Kinder haben „{kat[i]}“ oder „{kat[j]}“ gewählt?'}, 'o': {'wert': h[i] + h[j]}, 'c': f'{h[i]} + {h[j]}',
                'w': f'„{kat[i]}“ {h[i]} und „{kat[j]}“ {h[j]}: {h[i]} + {h[j]} = {h[i] + h[j]}.', 'h': 'Addiere die beiden Häufigkeiten.'}
    n = R.choice([20, 25, 40, 50])
    titel, kat, h = tabelle(R, ziel=n)
    i = R.randrange(len(kat))
    if R.random() < .5:
        return {'y': 'zahl', 'f': {'text': f'{tab_text(titel, kat, h)}. Wie viel Prozent haben „{kat[i]}“ gewählt?'}, 'o': {'wert': wert(Fr(h[i] * 100, n)), 'einheit': '%'},
                'c': f'{h[i]} / (' + ' + '.join(map(str, h)) + ') * 100', 'w': f'Gesamt: {n}. {h[i]} : {n} = {zt(Fr(h[i], n))} = {pz(Fr(h[i] * 100, n))}.',
                'h': 'Zuerst die Gesamtzahl bilden. Sie ist der Grundwert.'}
    s = sorted(zip(h, kat), reverse=True)
    r = s[1][1]
    return {**wahl(R, r, [k for k in kat if k != r]), 'f': {'text': f'{tab_text(titel, kat, h)}. Was wurde am zweithäufigsten genannt?'},
            'w': 'Der Größe nach: ' + ', '.join(f'{k} {x}' for x, k in s) + f'. Platz 2: {r}.', 'h': 'Ordne die Häufigkeiten der Größe nach.'}


# ---------- 4 Säulendiagramm ----------
def g_saeule(st):
    if st == 1:
        m = R.choice([2, 4, 5, 10])
        k = R.randint(2, 9) * m + (m // 2 if R.random() < .3 and m % 2 == 0 else 0)
        h = Fr(k, m)
        return {'y': 'zahl', 'f': {'text': f'In einem Säulendiagramm steht 1 cm für {m} Kinder. Wie hoch wird die Säule für {k} Kinder?'}, 'o': {'wert': wert(h), 'einheit': 'cm'}, 'c': f'{k} / {m}',
                'w': f'{k} : {m} = {zt(h)}, die Säule ist {zt(h)} cm hoch.', 'h': 'Teile die Anzahl durch den Maßstab.'}
    if st == 2:
        m = R.choice([2, 4, 5, 6, 8, 10, 20, 25, 50])
        h = Fr(R.randint(3, 19), 2)
        k = h * m
        if k.denominator != 1: return g_saeule(2)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'1 cm Säulenhöhe steht für {m} Stimmen. Eine Säule ist {zt(h)} cm hoch. Wie viele Stimmen zeigt sie?'}, 'o': {'wert': int(k)}, 'c': f'{float(h)} * {m}',
                    'w': f'{zt(h)} · {m} = {zt(k)} Stimmen.', 'h': 'Höhe mal Maßstab.'}
        h2 = h + Fr(R.randint(1, 6), 2)
        return {'y': 'zahl', 'f': {'text': f'1 cm steht für {m} Stimmen. Säule A ist {zt(h)} cm hoch, Säule B {zt(h2)} cm. Wie viele Stimmen mehr hat B?'}, 'o': {'wert': wert((h2 - h) * m)},
                'c': f'({float(h2)} - {float(h)}) * {m}', 'w': f'Unterschied: {zt(h2 - h)} cm · {m} = {zt((h2 - h) * m)} Stimmen.', 'h': 'Unterschied der Höhen mal Maßstab.'}
    art = R.randrange(2)
    if art == 0:
        groesst = R.randint(40, 180)
        hmax = R.choice([8, 10, 12, 15])
        m = -(-groesst // hmax)
        return {'y': 'zahl', 'f': {'text': f'Der größte Wert ist {groesst}. Die höchste Säule darf höchstens {hmax} cm hoch sein. Wie viele Stimmen muss 1 cm mindestens darstellen? (ganze Zahl)'},
                'o': {'wert': m}, 'c': f'-(-{groesst} // {hmax})', 'w': f'{groesst} : {hmax} = {zt(Fr(groesst, hmax)) if (Fr(groesst, hmax) * 100).denominator == 1 else "≈ " + zt((Fr(groesst, hmax) * 10 // 1) / 10)}. Aufrunden: mindestens {m} Stimmen pro cm.',
                'h': 'Teile den größten Wert durch die Höchsthöhe und runde auf.'}
    titel, kat, h = tabelle(R, 20, 60)
    m = R.choice([2, 4, 5])
    i = h.index(max(h))
    hh = Fr(h[i], m)
    return {'y': 'zahl', 'f': {'text': f'{tab_text(titel, kat, h)}. Maßstab: 1 cm für {m}. Wie hoch wird die höchste Säule?'}, 'o': {'wert': wert(hh), 'einheit': 'cm'}, 'c': f'max({", ".join(map(str, h))}) / {m}',
            'w': f'Größter Wert: {h[i]} ({kat[i]}). {h[i]} : {m} = {zt(hh)} cm.', 'h': 'Suche den größten Wert und teile durch den Maßstab.'}


# ---------- 5 Kreisdiagramm ----------
def g_kreis(st):
    if st == 1:
        if R.random() < .5:
            b, g = R.choice([(Fr(1, 2), 180), (Fr(1, 4), 90), (Fr(3, 4), 270), (Fr(1, 3), 120), (Fr(1, 6), 60), (Fr(1, 8), 45), (Fr(1, 10), 36), (Fr(2, 3), 240), (Fr(1, 5), 72)])
            return {'y': 'zahl', 'f': {'text': f'Ein Anteil von {bruch(b)} soll im Kreisdiagramm dargestellt werden. Wie groß ist der Winkel?'}, 'o': {'wert': g, 'einheit': '°'},
                    'c': f'{b.numerator} / {b.denominator} * 360', 'w': f'{bruch(b)} von 360° = 360° : {b.denominator} · {b.numerator} = {g}°.', 'h': 'Der ganze Kreis hat 360°.'}
        p = R.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])
        return {'y': 'zahl', 'f': {'text': f'Wie groß ist der Winkel für {pz(p)} im Kreisdiagramm?'}, 'o': {'wert': wert(Fr(p * 360, 100)), 'einheit': '°'}, 'c': f'{p} / 100 * 360',
                'w': f'{pz(p)} · 360° = {zt(Fr(p, 100))} · 360° = {zt(Fr(p * 360, 100))}°.', 'h': '1 % entspricht 3,6°.'}
    if st == 2:
        n = R.choice([20, 24, 30, 36, 40, 45, 60, 72, 90, 120])
        k = R.randint(1, n - 1)
        g = Fr(k * 360, n)
        if not (g * 10).denominator == 1: return g_kreis(2)
        return {'y': 'zahl', 'f': {'text': f'{k} von {n} Befragten wählen „ja“. Wie groß ist der Winkel im Kreisdiagramm?'}, 'o': {'wert': wert(g), 'einheit': '°'}, 'c': f'{k} / {n} * 360',
                'w': f'Relative Häufigkeit {k}/{n}. Winkel: {k}/{n} · 360° = {zt(g)}°.', 'h': 'Relative Häufigkeit mal 360°.'}
    art = R.randrange(3)
    if art == 0:
        g = R.choice([18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198, 216, 234, 252, 270])
        return {'y': 'zahl', 'f': {'text': f'Ein Kreisausschnitt hat einen Winkel von {g}°. Wie viel Prozent stellt er dar?'}, 'o': {'wert': wert(Fr(g * 100, 360)), 'einheit': '%'}, 'c': f'{g} / 360 * 100',
                'w': f'{g}° : 360° = {zt(Fr(g, 360))} = {pz(Fr(g * 100, 360))}.', 'h': 'Winkel durch 360°, dann mal 100.'}
    if art == 1:
        n = R.choice([24, 30, 36, 40, 60, 72, 120])
        g = R.choice([x for x in range(30, 331, 30) if (Fr(x, 360) * n).denominator == 1])
        return {'y': 'zahl', 'f': {'text': f'In einem Kreisdiagramm über {n} Kinder hat der Ausschnitt „Rad“ einen Winkel von {g}°. Wie viele Kinder fahren Rad?'}, 'o': {'wert': int(Fr(g, 360) * n)},
                'c': f'{g} / 360 * {n}', 'w': f'Anteil {g}/360 = {bruch(Fr(g, 360))}. {bruch(Fr(g, 360))} von {n} = {int(Fr(g, 360) * n)} Kinder.', 'h': 'Winkel : 360° ergibt den Anteil. Den Anteil mal Gesamtzahl.'}
    fragen = [('Welche Darstellung zeigt am besten die Anteile am Ganzen (z. B. Verteilung des Taschengelds)?', 'Kreisdiagramm', ['Säulendiagramm mit abgeschnittener Achse', 'Strichliste', 'Urliste']),
              ('Welche Darstellung eignet sich am besten, um die Anzahlen mehrerer Gruppen direkt zu vergleichen?', 'Säulendiagramm', ['Kreisdiagramm ohne Beschriftung', 'Urliste', 'Strichliste ohne Bündel']),
              ('In einem Kreisdiagramm ergeben alle Winkel zusammen …', '360°', ['100°', '180°', '90°']),
              ('In einem Kreisdiagramm sind zwei Ausschnitte gleich groß. Was bedeutet das?', 'Beide Gruppen sind gleich häufig.', ['Beide Gruppen sind je 50 %.', 'Eine Gruppe ist doppelt so groß.', 'Man kann nichts sagen.'])]
    t, r, f = R.choice(fragen)
    return {**wahl(R, r, f), 'f': {'text': t}, 'w': f'Richtig: {r}. Kreisdiagramme zeigen Anteile am Ganzen (360° = 100 %), Säulendiagramme vergleichen Anzahlen.', 'h': 'Was soll das Diagramm zeigen – Anteile oder Anzahlen?'}


# ---------- 6 Irreführend ----------
def g_irr(st):
    if st == 1:
        s0 = R.choice([50, 80, 90, 400, 500, 900, 950, 1000])
        p1, p2 = R.choice([30, 35, 40, 45]), R.choice([35, 40, 45])
        p3 = R.choice([30, 35]) if p1 + p2 < 75 else 35
        fragen = [(f'Die Hochachse eines Säulendiagramms beginnt bei {zt(s0)} statt bei 0. Was bewirkt das?', 'Kleine Unterschiede wirken sehr groß.', ['Die Werte werden genauer.', 'Nichts, es ist nur schöner.', 'Alle Säulen wirken gleich hoch.']),
                  ('Bei einem Säulendiagramm fehlt die Beschriftung der Hochachse. Was ist das Problem?', 'Man kann die Werte nicht ablesen.', ['Die Säulen sind zu breit.', 'Es gibt kein Problem.', 'Man kann die Farben nicht erkennen.']),
                  ('Auf der Hochachse stehen die Zahlen 0, 10, 20, 50, 100 in gleichen Abständen. Was ist falsch?', 'Die Abstände passen nicht zu den Zahlen.', ['Die Achse beginnt bei 0.', 'Es gibt zu wenige Zahlen.', 'Nichts, das ist richtig.']),
                  ('Statt Säulen werden Münzen gezeichnet. Der doppelte Wert wird als doppelt so hohe UND doppelt so breite Münze gezeigt. Wie wirkt das?', 'Viel größer, als es ist (vierfache Fläche).', ['Genau richtig.', 'Kleiner, als es ist.', 'Halb so groß.']),
                  (f'Ein Kreisdiagramm hat nur die Anteile {p1} %, {p2} % und {p3} %. Was stimmt nicht?', 'Zusammen sind es mehr als 100 %.', ['Es sind zu wenige Anteile.', 'Nichts, alles stimmt.', 'Kreisdiagramme dürfen keine Prozente zeigen.'])]
        t, r, f = R.choice(fragen)
        return {**wahl(R, r, f), 'f': {'text': t}, 'w': f'{r} Lies bei Diagrammen immer zuerst Achsen, Beschriftung und Summen.', 'h': 'Was würde ein ehrliches Diagramm anders machen?'}
    if st == 2:
        s = R.choice([100, 200, 500, 900, 950, 1000])
        d1 = R.choice([5, 10, 20, 25])
        f = R.choice([2, 3, 4, 5])
        a, b = s + d1, s + d1 * f
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Ein Säulendiagramm zeigt {zt(a)} und {zt(b)} Besucher. Die Hochachse beginnt bei {zt(s)}. Wie viel Mal so hoch wirkt die zweite Säule?'},
                    'o': {'wert': f}, 'c': f'({b} - {s}) / ({a} - {s})', 'w': f'Sichtbare Höhen: {zt(a)} − {zt(s)} = {d1} und {zt(b)} − {zt(s)} = {d1 * f}. Sie wirkt {f}-mal so hoch.',
                    'h': 'Gezeichnet wird nur der Teil oberhalb des Achsenanfangs.'}
        mehr = Fr(b - a, a) * 100
        r = 'Nein, der Unterschied ist viel kleiner, als er aussieht.' if mehr < 50 else 'Ja, der Unterschied ist wirklich groß.'
        return {**wahl(R, r, ['Ja, der Unterschied ist wirklich groß.' if r.startswith('Nein') else 'Nein, der Unterschied ist viel kleiner, als er aussieht.', 'Das kann man ohne Achse nie sagen.'], 3),
                'f': {'text': f'Die Säulen für {zt(a)} und {zt(b)} Besucher sind bei einer Achse ab {zt(s)} gezeichnet. Die zweite Säule wirkt {f}-mal so hoch. Ist der Unterschied wirklich so groß?'},
                'w': f'Echter Unterschied: {zt(b - a)} von {zt(a)}, also nur etwa {zt((mehr * 10 + Fr(1, 2)) // 1 / 10)} % mehr.', 'h': 'Vergleiche die echten Zahlen, nicht die Säulenhöhen.'}
    art = R.randrange(3)
    if art == 0:
        k = R.choice([2, 3, 4])
        return {'y': 'zahl', 'f': {'text': f'Ein Bild-Diagramm zeigt den {k}-fachen Wert durch ein Bild, das {k}-mal so hoch und {k}-mal so breit ist. Wie viel Mal so groß ist die Bildfläche?'},
                'o': {'wert': k * k}, 'c': f'{k} * {k}', 'w': f'Fläche = Höhe · Breite: {k} · {k} = {k * k}. Das Bild wirkt also {k * k}-mal so groß statt {k}-mal.', 'h': 'Fläche eines Rechtecks: Länge mal Breite.'}
    if art == 1:
        ps = [R.choice([15, 20, 25, 30, 35, 40]) for _ in range(3)]
        s = sum(ps)
        if s == 100: return g_irr(3)
        r = 'Nein, die Anteile ergeben zusammen nicht 100 %.'
        return {**wahl(R, r, ['Ja, alles passt.', 'Nein, ein Kreisdiagramm darf höchstens zwei Teile haben.'], 3),
                'f': {'text': f'Ein Kreisdiagramm zeigt die Anteile {pz(ps[0])}, {pz(ps[1])} und {pz(ps[2])} – mehr Teile gibt es nicht. Kann das stimmen?'},
                'w': f'{ps[0]} + {ps[1]} + {ps[2]} = {s} %. Bei einem Kreisdiagramm müssen es genau 100 % sein.', 'h': 'Addiere alle Anteile.'}
    s = R.choice([40, 45, 48, 50])
    a, b = s + R.randint(1, 3), s + R.randint(4, 8)
    r = f'Die Achse beginnt bei {s} %. So wirkt der Vorsprung von {b - a} Prozentpunkten riesig.'
    return {**wahl(R, r, ['Die zweite Kandidatin hat doppelt so viele Stimmen.', 'Die Säulen sind zu breit gezeichnet.', 'Alles ist korrekt dargestellt.']),
            'f': {'text': f'Ein Diagramm zur Wahl der Klassensprecherin zeigt {a} % und {b} %. Die Achse beginnt bei {s} %, deshalb wirkt die zweite Säule viel höher. Was ist irreführend?'},
            'w': f'{b} % − {a} % = {b - a} Prozentpunkte. Mit einer Achse ab 0 sähen die Säulen fast gleich hoch aus.', 'h': 'Wo beginnt die Hochachse?'}


GEN = {'absolute_haeufigkeit': g_abs, 'relative_haeufigkeit': g_rel, 'tabelle_auswerten': g_tab, 'saeulendiagramm': g_saeule,
       'kreisdiagramm': g_kreis, 'irrefuehrend': g_irr}

DATEI = datei(E, 'Daten erfassen, absolute und relative Häufigkeiten bestimmen, Säulen- und Kreisdiagramme berechnen und irreführende Diagramme erkennen.', MERKE,
              [('Daten erfassen', ['absolute_haeufigkeit', 'relative_haeufigkeit', 'tabelle_auswerten']),
               ('Diagramme', ['saeulendiagramm', 'kreisdiagramm', 'irrefuehrend'])],
              ETAPPEN, GEN,
              offen=['Lernkarte saeulendiagramm braucht Zeichnung: Säulendiagramm zum Ablesen und zum selbst Zeichnen (Säulenhöhe einstellen). Bisher nur Maßstab-Rechnungen in Worten.',
                     'Lernkarte kreisdiagramm braucht Zeichnung: Kreisdiagramm mit Ausschnitten zum Ablesen bzw. Winkel einstellen. Bisher nur Winkelberechnung in Worten.',
                     'Lernkarte irrefuehrend braucht Zeichnung: Säulendiagramm mit abgeschnittener Hochachse und Bild-Diagramm zum Vergleichen. Bisher nur in Worten beschrieben.',
                     'Die Strichliste wird nur in Worten beschrieben („3 Fünferbündel und 2 einzelne Striche“); eine Grafik dafür fehlt.'])

if __name__ == '__main__':
    schreibe(DATEI)
