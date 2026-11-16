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
     'fehler': 'Die größte Zahl in der Tabelle ist ⟦nicht⟧ die Gesamtzahl. Die Gesamtzahl ist die ⟦Summe⟧ aller Häufigkeiten (hier 30, nicht 12).',
     'bild': {'typ': 'tabelle', 'kopf': ['Schulweg', 'Bus', 'Rad', 'zu Fuß', 'Auto', 'Summe'], 'zeilen': [['Anzahl', '12', '9', '6', '3', '30']]}},
    {'lernziel': 'saeulendiagramm', 'titel': 'Säulendiagramme und Maßstab',
     'regel': 'Im ⟦Säulendiagramm⟧ zeigt die ⟦Höhe⟧ jeder Säule die Häufigkeit. Dafür wählt man einen ⟦Maßstab⟧ für die Hochachse, z. B. 1 cm für 4 Kinder. Die Hochachse beginnt bei ⟦0⟧, alle Säulen sind gleich breit.',
     'schritte': ['Maßstab: 1 cm für 4 Kinder. Die Säule für Fußball soll 18 Kinder zeigen.', '18 : 4 = 4,5, also ist die Säule ⟦4,5 cm⟧ hoch.'],
     'fehler': 'Die Säule für 18 Kinder 18 cm hoch zu zeichnen, passt nicht aufs Heft. Erst einen ⟦Maßstab⟧ wählen, dann ⟦Anzahl : Maßstab⟧ rechnen.',
     'bild': {'typ': 'saeulen', 'einheit': 'Kinder', 'werte': [{'name': 'Fußball', 'wert': 18}, {'name': 'Schwimmen', 'wert': 10}, {'name': 'Turnen', 'wert': 6}, {'name': 'Tennis', 'wert': 4}],
              'y_start': 0, 'zahlen': True}},
    {'lernziel': 'kreisdiagramm', 'titel': 'Kreisdiagramme berechnen',
     'regel': 'Im ⟦Kreisdiagramm⟧ ist der ganze Kreis 100 % = ⟦360°⟧. Der Winkel eines Kreisausschnitts ist ⟦relative Häufigkeit · 360°⟧. 1 % entspricht 3,6°. Kreisdiagramme zeigen gut ⟦Anteile am Ganzen⟧.',
     'schritte': ['40 Kinder: 12 Rad, 16 Bus, 8 zu Fuß, 4 Auto. Rad: 12 : 40 = 0,3 = 30 %.', 'Winkel für Rad: 0,3 · 360° = ⟦108°⟧.',
                  'Ebenso: Bus 40 % → 144°, zu Fuß 20 % → 72°, Auto 10 % → 36°. Zusammen 360°.'],
     'probe': '108° + 144° + 72° + 36° = 360° ✓',
     'bild': {'typ': 'kreisdiagramm', 'einheit': ' %', 'werte': [{'name': 'Rad', 'wert': 30}, {'name': 'Bus', 'wert': 40}, {'name': 'zu Fuß', 'wert': 20}, {'name': 'Auto', 'wert': 10}],
              'zahlen': True},
     'fehler': '30 % als Winkel von 30° einzuzeichnen ist falsch: Der Vollkreis hat ⟦360°⟧, nicht 100°. 30 % sind 0,3 · 360° = 108°.'},
    {'lernziel': 'irrefuehrend', 'titel': 'Irreführende Diagramme erkennen',
     'regel': 'Diagramme können ⟦täuschen⟧: eine Hochachse, die ⟦nicht bei 0 beginnt⟧, ungleiche Abstände auf der Achse, Bilder statt Säulen (doppelt so hoch und breit = ⟦vierfache Fläche⟧) oder fehlende Beschriftung. Lies immer ⟦Achse und Zahlen⟧.',
     'schritte': ['Zwei Säulen zeigen 980 und 1 000 Besucher, die Hochachse beginnt bei 960. Die Säulen sind 20 und 40 Einheiten hoch.', 'Die zweite wirkt doppelt so hoch, ist aber nur ⟦20 Besucher⟧ (etwa 2 %) mehr.'],
     'fehler': 'Nur auf die Säulenhöhen zu schauen, ohne die Achse zu lesen, ist ein Fehler: Bei abgeschnittener Achse wirken kleine Unterschiede ⟦riesig⟧.',
     'bild': {'typ': 'saeulen', 'einheit': 'Besucher', 'werte': [{'name': 'Samstag', 'wert': 980}, {'name': 'Sonntag', 'wert': 1000}], 'y_start': 960, 'zahlen': True}},
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


def tab_daten(R, n_min=20, n_max=40, ziel=None):
    titel, kat = R.choice(THEMEN)
    k = R.randint(3, len(kat))
    kat = kat[:k]
    while True:
        h = [R.randint(1, 15) for _ in kat]
        if ziel is None and n_min <= sum(h) <= n_max and len(set(h)) == len(h): return titel, kat, h
        if ziel and sum(h) == ziel and len(set(h)) == len(h): return titel, kat, h


def tab_text(titel, kat, h): return f'{titel}: ' + ' | '.join(f'{a} {b}' for a, b in zip(kat, h))


def tab_bild(titel, kat, h, frage=None):
    """Häufigkeitstabelle als Bild; frage = Index der Zelle, die als „?“ erscheint."""
    return tabelle([titel] + list(kat), [['Anzahl'] + ['?' if j == frage else x for j, x in enumerate(h)]])


def striche(k):
    """Strichliste als Text: Fünferbündel ||||| durch Leerzeichen getrennt."""
    return ' '.join(['|||||'] * (k // 5) + (['|' * (k % 5)] if k % 5 else []))


def schritt_app(hoch, unten=0):
    """Teilung der Hochachse wie in der App (lernSaeulen): 1-2-5-Schritte für etwa 5 Linien."""
    from math import floor, log10
    roh = (hoch - unten) / 5
    p = 10 ** floor(log10(roh))
    return next(m * p for m in (1, 2, 5, 10) if m * p >= roh - 1e-9)


def diagramm_daten():
    """Säulendiagramm zum Ablesen: alle Werte liegen genau auf Linien der Hochachse."""
    while True:
        titel, kat = R.choice(THEMEN)
        kat = kat[:R.randint(3, min(5, len(kat)))]
        sch = R.choice([2, 5, 10])
        h = R.sample(range(1, 6), len(kat)) if len(kat) <= 5 else None
        h = [x * sch for x in h]
        if max(h) <= 2 * sch: continue
        if abs(schritt_app(max(h)) - sch) < 1e-9: return titel, kat, h, sch


NICHT = [0]   # Vorlage „nicht … gewählt“ höchstens 4-mal


def pz(p): return f'{zt(p)} %'


# ---------- 1 Absolute Häufigkeit ----------
def g_abs(st):
    if st == 1:
        if R.random() < .5:
            titel, kat = R.choice(THEMEN)
            kat = kat[:R.randint(3, len(kat))]
            h = R.sample(range(3, 16), len(kat))
            i = R.randrange(len(kat))
            return {'y': 'zahl', 'f': {'text': f'Die Strichliste zeigt eine Umfrage zum Thema {titel}. Wie oft wurde „{kat[i]}“ genannt?',
                                       'grafik': tabelle([titel, 'Strichliste'], [[k, striche(x)] for k, x in zip(kat, h)])},
                    'o': {'wert': h[i]}, 'c': f'{h[i] // 5} * 5 + {h[i] % 5}',
                    'w': f'Bei „{kat[i]}“: {h[i] // 5} Fünferbündel' + (f' und {h[i] % 5} ' + ('einzelner Strich' if h[i] % 5 == 1 else 'einzelne Striche') if h[i] % 5 else '') + f': {h[i] // 5} · 5 + {h[i] % 5} = {h[i]}.', 'h': 'Ein Bündel ||||| steht für 5. Zähle die Bündel in Fünferschritten.'}
        n = R.randint(8, 12)
        liste = [R.randint(1, 6) for _ in range(n)]
        w = R.choice(liste)
        k = liste.count(w)
        return {'y': 'zahl', 'f': {'text': f'Würfelergebnisse: {", ".join(map(str, liste))}. Wie oft wurde die {w} gewürfelt?'}, 'o': {'wert': k}, 'c': ' + '.join(['1'] * k),
                'w': f'Die {w} kommt {k}-mal vor. Absolute Häufigkeit: {k}.', 'h': 'Streiche jede gefundene Zahl ab, damit du nichts doppelt zählst.'}
    if st == 2:
        if R.random() < .5:
            titel, kat = R.choice(THEMEN)
            kat = kat[:R.randint(3, len(kat))]
            h = R.sample(range(3, 16), len(kat))
            g = tabelle([titel, 'Strichliste'], [[k, striche(x)] for k, x in zip(kat, h)])
            if R.random() < .5:
                return {'y': 'zahl', 'f': {'text': f'Die Strichliste zeigt eine Umfrage zum Thema {titel}. Wie viele Kinder wurden insgesamt befragt?', 'grafik': g},
                        'o': {'wert': sum(h)}, 'c': ' + '.join(map(str, h)), 'w': 'Striche je Zeile: ' + ', '.join(f'{k} {x}' for k, x in zip(kat, h)) + f'. Zusammen {sum(h)}.',
                        'h': 'Zähle jede Zeile (Bündel = 5) und addiere.'}
            i, j = R.sample(range(len(kat)), 2)
            if h[i] < h[j]: i, j = j, i
            return {'y': 'zahl', 'f': {'text': f'Die Strichliste zeigt eine Umfrage zum Thema {titel}. Wie oft wurde „{kat[i]}“ häufiger genannt als „{kat[j]}“?', 'grafik': g},
                    'o': {'wert': h[i] - h[j]}, 'c': f'{h[i]} - {h[j]}', 'w': f'„{kat[i]}“: {h[i]}, „{kat[j]}“: {h[j]}. Unterschied: {h[i]} − {h[j]} = {h[i] - h[j]}.',
                    'h': 'Zähle beide Zeilen und bilde den Unterschied.'}
        titel, kat = R.choice(THEMEN)
        n = R.randint(12, 15)
        liste = urliste(R, kat, n)
        c = Counter(liste)
        if len(c) < 3: return g_abs(2)
        a, b = R.sample(list(c), 2)
        return {'y': 'zahl', 'f': {'text': f'Umfrage {titel}: {", ".join(liste)}. Wie viele Kinder nannten „{a}“ oder „{b}“?'}, 'o': {'wert': c[a] + c[b]}, 'c': f'{c[a]} + {c[b]}',
                'w': f'„{a}“: {c[a]}-mal, „{b}“: {c[b]}-mal. Zusammen {c[a] + c[b]}.', 'h': 'Mach eine Strichliste und addiere die beiden Häufigkeiten.'}
    art = R.randrange(3)
    if art == 0:
        titel, kat, h = tab_daten(R)
        n = sum(h)
        i = R.randrange(len(kat))
        rest = [x for j, x in enumerate(h) if j != i]
        return {'y': 'zahl', 'f': {'text': f'Es wurden {n} Kinder befragt. Welche Zahl fehlt in der Tabelle bei „{kat[i]}“?', 'grafik': tab_bild(titel, kat, h, frage=i)},
                'o': {'wert': h[i]}, 'c': f'{n} - (' + ' + '.join(map(str, rest)) + ')',
                'w': f'{n} − ({" + ".join(map(str, rest))}) = {n} − {sum(rest)} = {h[i]}.', 'h': 'Alle Häufigkeiten zusammen ergeben die Gesamtzahl.'}
    if art == 1:
        titel, kat = R.choice(THEMEN)
        liste = urliste(R, kat, R.randint(12, 15))
        c = Counter(liste)
        if len(c) < 3: return g_abs(3)
        a, b = R.sample(list(c), 2)
        rest = len(liste) - c[a] - c[b]
        return {'y': 'zahl', 'f': {'text': f'Umfrage {titel}: {", ".join(liste)}. Wie viele Kinder nannten weder „{a}“ noch „{b}“?'}, 'o': {'wert': rest},
                'c': f'{len(liste)} - {c[a]} - {c[b]}', 'w': f'Insgesamt {len(liste)} Antworten, davon „{a}“ {c[a]} und „{b}“ {c[b]}. Übrig: {len(liste)} − {c[a]} − {c[b]} = {rest}.',
                'h': 'Zähle alle Antworten und ziehe die beiden Häufigkeiten ab.'}
    k = R.randint(6, 28)
    fuenfer, rest = divmod(k, 5)
    return {'y': 'zahl', 'f': {'text': f'In einer Strichliste stehen bei „Hund“: {fuenfer} Fünferbündel' + ((f' und {rest} einzelne Striche.' if rest > 1 else ' und 1 einzelner Strich.') if rest else '.') + ' Wie oft wurde „Hund“ genannt?'},
            'o': {'wert': k}, 'c': f'{fuenfer} * 5 + {rest}', 'w': f'{fuenfer} Bündel zu je 5 und {rest} einzelne: {fuenfer} · 5 + {rest} = {k}.', 'h': 'Ein Bündel steht für 5 Striche.'}


# ---------- 2 Relative Häufigkeit ----------
def g_rel(st):
    if st == 1:
        n = R.choice([10, 12, 16, 20, 24, 30])
        k = R.randint(2, n - 1)
        x = Fr(k, n)
        ding = R.choice([('Würfen', 'zeigen eine Sechs'), ('Kindern', 'haben ein Haustier'), ('Losen', 'gewinnen'), ('Tagen', 'sind sonnig')])
        return {'y': 'luecken', 'f': {'text': f'{k} von {n} {ding[0]} {ding[1]}. Wie groß ist die relative Häufigkeit als Bruch?', 'schablone': '□/□', 'hinweis': HB},
                'o': {'werte': [x.numerator, x.denominator]}, 'c': [f'{k} / {n} * {x.denominator}', f'{x.denominator}'],
                'w': f'Relative Häufigkeit = {k}/{n}' + (f' = {bruch(x)}.' if x.denominator != n else '.'), 'h': 'Absolute Häufigkeit durch Gesamtzahl. Dann kürzen.'}
    if st == 2:
        n = R.choice([20, 25, 40, 50, 80, 125, 200, 250])
        k = R.randint(2, n - 1)
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
ZWEI = [('Schulweg', ['Bus', 'Rad', 'zu Fuß']), ('Lieblingssport', ['Fußball', 'Schwimmen', 'Turnen']), ('Haustier', ['Hund', 'Katze', 'keins'])]


def zwei_d():
    """Zweidimensionale Tabelle (Mädchen/Jungen) mit einer Frage."""
    titel, kat = R.choice(ZWEI)
    m = [R.randint(2, 12) for _ in kat]
    j = [R.randint(2, 12) for _ in kat]
    g = tabelle([titel, 'Mädchen', 'Jungen'], [[k, a, b] for k, a, b in zip(kat, m, j)])
    i = R.randrange(len(kat))
    art = R.randrange(3)
    if art == 0:
        wer, x = R.choice([('Jungen', j[i]), ('Mädchen', m[i])])
        return {'y': 'zahl', 'f': {'text': f'Die Tabelle zeigt eine Umfrage ({titel}). Wie viele {wer} nennen „{kat[i]}“?', 'grafik': g}, 'o': {'wert': x}, 'c': f'{x}',
                'w': f'Zeile „{kat[i]}“, Spalte {wer}: {x}.', 'h': 'Suche die Zeile und dann die Spalte.'}
    if art == 1:
        return {'y': 'zahl', 'f': {'text': f'Die Tabelle zeigt eine Umfrage ({titel}). Wie viele Kinder nennen „{kat[i]}“?', 'grafik': g}, 'o': {'wert': m[i] + j[i]},
                'c': f'{m[i]} + {j[i]}', 'w': f'Mädchen und Jungen zusammen: {m[i]} + {j[i]} = {m[i] + j[i]}.', 'h': 'Addiere beide Werte der Zeile.'}
    wer, sp = R.choice([('Mädchen', m), ('Jungen', j)])
    return {'y': 'zahl', 'f': {'text': f'Die Tabelle zeigt eine Umfrage ({titel}). Wie viele {wer} wurden befragt?', 'grafik': g}, 'o': {'wert': sum(sp)},
            'c': ' + '.join(map(str, sp)), 'w': f'Spalte {wer} addieren: {" + ".join(map(str, sp))} = {sum(sp)}.', 'h': 'Addiere alle Zahlen einer Spalte.'}


def g_tab(st):
    titel, kat, h = tab_daten(R)
    n = sum(h)
    g = tab_bild(titel, kat, h)
    if st == 1:
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Die Tabelle zeigt eine Umfrage zum Thema {titel}. Wie viele Kinder wurden insgesamt befragt?', 'grafik': g}, 'o': {'wert': n},
                    'c': ' + '.join(map(str, h)), 'w': f'Alle Häufigkeiten addieren: {" + ".join(map(str, h))} = {n}.', 'h': 'Addiere alle Häufigkeiten.'}
        r = kat[h.index(max(h))]
        return {**wahl(R, r, [k for k in kat if k != r]), 'f': {'text': f'Die Tabelle zeigt eine Umfrage zum Thema {titel}. Was wurde am häufigsten genannt?', 'grafik': g},
                'w': f'Die größte Häufigkeit ist {max(h)} bei „{r}“.', 'h': 'Suche die größte Zahl in der Tabelle.'}
    if st == 2:
        if R.random() < .35:
            return zwei_d()
        i, j = R.sample(range(len(kat)), 2)
        if R.random() < .3 and NICHT[0] < 4:
            NICHT[0] += 1
            return {'y': 'zahl', 'f': {'text': f'Die Tabelle zeigt eine Umfrage zum Thema {titel}. Wie viele Kinder haben nicht „{kat[i]}“ gewählt?', 'grafik': g},
                    'o': {'wert': n - h[i]}, 'c': ' + '.join(map(str, h)) + f' - {h[i]}',
                    'w': f'Gesamt {n}, davon {h[i]} „{kat[i]}“. Nicht: {n} − {h[i]} = {n - h[i]}.', 'h': 'Gesamtzahl minus die Häufigkeit dieser Antwort.'}
        return {'y': 'zahl', 'f': {'text': f'Die Tabelle zeigt eine Umfrage zum Thema {titel}. Wie viele Kinder haben „{kat[i]}“ oder „{kat[j]}“ gewählt?', 'grafik': g},
                'o': {'wert': h[i] + h[j]}, 'c': f'{h[i]} + {h[j]}',
                'w': f'„{kat[i]}“ {h[i]} und „{kat[j]}“ {h[j]}: {h[i]} + {h[j]} = {h[i] + h[j]}.', 'h': 'Addiere die beiden Häufigkeiten.'}
    n = R.choice([20, 25, 40, 50])
    titel, kat, h = tab_daten(R, ziel=n)
    g = tab_bild(titel, kat, h)
    i = R.randrange(len(kat))
    if R.random() < .5:
        return {'y': 'zahl', 'f': {'text': f'Die Tabelle zeigt eine Umfrage zum Thema {titel}. Wie viel Prozent haben „{kat[i]}“ gewählt?', 'grafik': g},
                'o': {'wert': wert(Fr(h[i] * 100, n)), 'einheit': '%'},
                'c': f'{h[i]} / (' + ' + '.join(map(str, h)) + ') * 100', 'w': f'Gesamt: {n}. {h[i]} : {n} = {zt(Fr(h[i], n))} = {pz(Fr(h[i] * 100, n))}.',
                'h': 'Zuerst die Gesamtzahl bilden. Sie ist der Grundwert.'}
    s_ = sorted(zip(h, kat), reverse=True)
    r = s_[1][1]
    return {**wahl(R, r, [k for k in kat if k != r]), 'f': {'text': f'Die Tabelle zeigt eine Umfrage zum Thema {titel}. Was wurde am zweithäufigsten genannt?', 'grafik': g},
            'w': 'Der Größe nach: ' + ', '.join(f'{k} {x}' for x, k in s_) + f'. Platz 2: {r}.', 'h': 'Ordne die Häufigkeiten der Größe nach.'}


# ---------- 4 Säulendiagramm ----------
def saeule_ablesen(st):
    titel, kat, h, sch = diagramm_daten()
    g = saeulen(list(zip(kat, h)), einheit='Kinder', zahlen=False)
    lies = f'Die Linien der Hochachse liegen {sch} Kinder auseinander. '
    if st == 1:
        i = R.randrange(len(kat))
        return {'y': 'zahl', 'f': {'text': f'Das Säulendiagramm zeigt eine Umfrage zum Thema {titel}. Wie viele Kinder nennen „{kat[i]}“?', 'grafik': g}, 'o': {'wert': h[i]},
                'c': f'{h[i]}', 'w': lies + f'Die Säule „{kat[i]}“ endet bei {h[i]}.', 'h': 'Fahre von der Oberkante der Säule waagrecht zur Hochachse.'}
    if st == 2:
        art = R.randrange(3)
        if art == 0:
            i, j = R.sample(range(len(kat)), 2)
            if h[i] < h[j]: i, j = j, i
            return {'y': 'zahl', 'f': {'text': f'Das Säulendiagramm zeigt eine Umfrage zum Thema {titel}. Wie viele Kinder mehr nennen „{kat[i]}“ als „{kat[j]}“?', 'grafik': g},
                    'o': {'wert': h[i] - h[j]}, 'c': f'{h[i]} - {h[j]}', 'w': lies + f'„{kat[i]}“: {h[i]}, „{kat[j]}“: {h[j]}. Unterschied: {h[i] - h[j]}.',
                    'h': 'Lies beide Säulen ab und bilde den Unterschied.'}
        if art == 1:
            return {'y': 'zahl', 'f': {'text': f'Das Säulendiagramm zeigt eine Umfrage zum Thema {titel}. Wie viele Kinder wurden befragt?', 'grafik': g}, 'o': {'wert': sum(h)},
                    'c': ' + '.join(map(str, h)), 'w': lies + 'Abgelesen: ' + ', '.join(f'{k} {x}' for k, x in zip(kat, h)) + f'. Zusammen {sum(h)}.',
                    'h': 'Lies jede Säule ab und addiere.'}
        i, j = R.sample(range(len(kat)), 2)
        return {'y': 'zahl', 'f': {'text': f'Das Säulendiagramm zeigt eine Umfrage zum Thema {titel}. Wie viele Kinder nennen „{kat[i]}“ oder „{kat[j]}“?', 'grafik': g},
                'o': {'wert': h[i] + h[j]}, 'c': f'{h[i]} + {h[j]}', 'w': lies + f'„{kat[i]}“: {h[i]}, „{kat[j]}“: {h[j]}. Zusammen {h[i] + h[j]}.',
                'h': 'Lies beide Säulen ab und addiere.'}
    n = sum(h)
    i = R.randrange(len(kat))
    p = Fr(h[i] * 100, n)
    if not ok2(p): return saeule_ablesen(3)
    return {'y': 'zahl', 'f': {'text': f'Das Säulendiagramm zeigt eine Umfrage zum Thema {titel}. Wie viel Prozent der Befragten nennen „{kat[i]}“?', 'grafik': g},
            'o': {'wert': wert(p), 'einheit': '%'}, 'c': f'{h[i]} / (' + ' + '.join(map(str, h)) + ') * 100',
            'w': lies + f'Alle zusammen: {" + ".join(map(str, h))} = {n}. „{kat[i]}“: {h[i]} : {n} = {zt(Fr(h[i], n))} = {pz(p)}.',
            'h': 'Erst alle Säulen ablesen und addieren (Grundwert), dann Anteil berechnen.'}


def g_saeule(st):
    if st == 2 or (st == 1 and R.random() < .5) or (st == 3 and R.random() < .4):
        return saeule_ablesen(st)
    if st == 1:
        m = R.choice([2, 4, 5, 10])
        k = R.randint(2, 9) * m + (m // 2 if R.random() < .3 and m % 2 == 0 else 0)
        h = Fr(k, m)
        return {'y': 'zahl', 'f': {'text': f'In einem Säulendiagramm steht 1 cm für {m} Kinder. Wie hoch wird die Säule für {k} Kinder?'}, 'o': {'wert': wert(h), 'einheit': 'cm'}, 'c': f'{k} / {m}',
                'w': f'{k} : {m} = {zt(h)}, die Säule ist {zt(h)} cm hoch.', 'h': 'Teile die Anzahl durch den Maßstab.'}
    art = R.randrange(2)
    if art == 0:
        groesst = R.randint(40, 180)
        hmax = R.choice([8, 10, 12, 15])
        m = -(-groesst // hmax)
        if groesst % hmax == 0:
            w = f'{groesst} : {hmax} = {m}. Also mindestens {m} Stimmen pro cm.'
        else:
            w = (f'{groesst} : {hmax} ≈ {zt((Fr(groesst, hmax) * 10 // 1) / 10)}. Mit {m - 1} pro cm wäre die Säule '
                 + (f'{zt(Fr(groesst, m - 1))} cm' if (Fr(groesst, m - 1) * 10).denominator == 1 else f'etwa {zt((Fr(groesst, m - 1) * 10 // 1) / 10)} cm')
                 + f' hoch – zu hoch. Also mindestens {m} Stimmen pro cm.')
        return {'y': 'zahl', 'f': {'text': f'Der größte Wert ist {groesst}. Die höchste Säule darf höchstens {hmax} cm hoch sein. Wie viele Stimmen muss 1 cm mindestens darstellen? (ganze Zahl)'},
                'o': {'wert': m}, 'c': f'-(-{groesst} // {hmax})', 'w': w, 'h': 'Teile den größten Wert durch die Höchsthöhe und runde auf.'}
    titel, kat, h = tab_daten(R, 20, 60)
    m = R.choice([2, 4, 5])
    i = h.index(max(h))
    hh = Fr(h[i], m)
    return {'y': 'zahl', 'f': {'text': f'Die Tabelle zeigt eine Umfrage zum Thema {titel}. Maßstab: 1 cm für {m} Kinder. Wie hoch wird die höchste Säule?', 'grafik': tab_bild(titel, kat, h)},
            'o': {'wert': wert(hh), 'einheit': 'cm'}, 'c': f'max({", ".join(map(str, h))}) / {m}',
            'w': f'Größter Wert: {h[i]} ({kat[i]}). {h[i]} : {m} = {zt(hh)} cm.', 'h': 'Suche den größten Wert und teile durch den Maßstab.'}


# ---------- 5 Kreisdiagramm ----------
KREISE = [((1, 2), (1, 4), (1, 4)), ((1, 2), (1, 3), (1, 6)), ((3, 4), (1, 4)), ((1, 3), (1, 3), (1, 3)), ((1, 2), (1, 4), (1, 8), (1, 8)), ((1, 4), (1, 2), (1, 4)),
          ((1, 6), (1, 2), (1, 3))]


def kreis_ablesen():
    teile = [Fr(*t) for t in R.choice(KREISE)]
    titel, kat = R.choice(THEMEN)
    kat = kat[:len(teile)]
    n = R.choice([x for x in (24, 30, 40, 48, 60, 72, 120) if all((t * x).denominator == 1 for t in teile)])
    g = kreisdiagramm([(k, int(t * 360)) for k, t in zip(kat, teile)], zahlen=False)
    i = R.randrange(len(kat))
    x = int(teile[i] * n)
    return {'y': 'zahl', 'f': {'text': f'Das Kreisdiagramm zeigt die Antworten von {n} Kindern zum Thema {titel}. Wie viele Kinder nennen „{kat[i]}“?', 'grafik': g},
            'o': {'wert': x}, 'c': f'{teile[i].numerator} / {teile[i].denominator} * {n}',
            'w': f'Der Ausschnitt „{kat[i]}“ ist {bruch(teile[i])} des Kreises. {bruch(teile[i])} von {n} = {x} Kinder.',
            'h': 'Schätze den Anteil des Ausschnitts: Halbkreis = 1/2, Viertelkreis = 1/4. Dann Anteil mal Gesamtzahl.'}


def g_kreis(st):
    if st == 1:
        if R.random() < .2:
            return {**wahl(R, '360°', ['100°', '180°', '90°']), 'f': {'text': 'In einem Kreisdiagramm ergeben alle Winkel zusammen …'},
                    'w': 'Der ganze Kreis hat 360°. Er steht für 100 % aller Befragten.', 'h': 'Wie viel Grad hat ein ganzer Kreis?'}
        if R.random() < .5:
            b, g = R.choice([(Fr(1, 2), 180), (Fr(1, 4), 90), (Fr(3, 4), 270), (Fr(1, 3), 120), (Fr(1, 6), 60), (Fr(1, 8), 45), (Fr(1, 10), 36), (Fr(2, 3), 240), (Fr(1, 5), 72)])
            return {'y': 'zahl', 'f': {'text': f'Ein Anteil von {bruch(b)} soll im Kreisdiagramm dargestellt werden. Wie groß ist der Winkel?'}, 'o': {'wert': g, 'einheit': '°'},
                    'c': f'{b.numerator} / {b.denominator} * 360', 'w': f'{bruch(b)} von 360° = 360° : {b.denominator} · {b.numerator} = {g}°.', 'h': 'Der ganze Kreis hat 360°.'}
        p = R.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])
        return {'y': 'zahl', 'f': {'text': f'Wie groß ist der Winkel für {pz(p)} im Kreisdiagramm?'}, 'o': {'wert': wert(Fr(p * 360, 100)), 'einheit': '°'}, 'c': f'{p} / 100 * 360',
                'w': f'{pz(p)} · 360° = {zt(Fr(p, 100))} · 360° = {zt(Fr(p * 360, 100))}°.', 'h': '1 % entspricht 3,6°.'}
    if st == 2:
        if R.random() < .5:
            return kreis_ablesen()
        n = R.choice([20, 24, 30, 36, 40, 45, 60, 72, 90, 120])
        k = R.randint(1, n - 1)
        g = Fr(k * 360, n)
        if not (g * 10).denominator == 1: return g_kreis(2)
        return {'y': 'zahl', 'f': {'text': f'{k} von {n} Befragten wählen „ja“. Wie groß ist der Winkel im Kreisdiagramm?'}, 'o': {'wert': wert(g), 'einheit': '°'}, 'c': f'{k} / {n} * 360',
                'w': f'Relative Häufigkeit {k}/{n}. Winkel: {k}/{n} · 360° = {zt(g)}°.', 'h': 'Relative Häufigkeit mal 360°.'}
    art = R.randrange(4)
    if art == 0:
        g = R.choice([18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198, 216, 234, 252, 270])
        return {'y': 'zahl', 'f': {'text': f'Ein Kreisausschnitt hat einen Winkel von {g}°. Wie viel Prozent stellt er dar?'}, 'o': {'wert': wert(Fr(g * 100, 360)), 'einheit': '%'}, 'c': f'{g} / 360 * 100',
                'w': f'{g}° : 360° = {zt(Fr(g, 360))} = {pz(Fr(g * 100, 360))}.', 'h': 'Winkel durch 360°, dann mal 100.'}
    if art == 1:
        n = R.choice([24, 30, 36, 40, 60, 72, 120])
        g = R.choice([x for x in range(30, 331, 30) if (Fr(x, 360) * n).denominator == 1])
        return {'y': 'zahl', 'f': {'text': f'In einem Kreisdiagramm über {n} Kinder hat der Ausschnitt „Rad“ einen Winkel von {g}°. Wie viele Kinder fahren Rad?'}, 'o': {'wert': int(Fr(g, 360) * n)},
                'c': f'{g} / 360 * {n}', 'w': f'Anteil {g}/360 = {bruch(Fr(g, 360))}. {bruch(Fr(g, 360))} von {n} = {int(Fr(g, 360) * n)} Kinder.', 'h': 'Winkel : 360° ergibt den Anteil. Den Anteil mal Gesamtzahl.'}
    if art == 2:
        a, b = R.sample(range(36, 181, 18), 2)
        c = 360 - a - b
        if c <= 0: return g_kreis(3)
        p = Fr(c * 100, 360)
        return {'y': 'zahl', 'f': {'text': f'Ein Kreisdiagramm hat die Winkel {a}° und {b}° und einen dritten Teil. Wie viel Prozent stellt der dritte Teil dar?'},
                'o': {'wert': wert(p), 'einheit': '%'}, 'c': f'(360 - {a} - {b}) / 360 * 100',
                'w': f'Dritter Winkel: 360° − {a}° − {b}° = {c}°. {c}° : 360° = {zt(Fr(c, 360))} = {pz(p)}.', 'h': 'Alle Winkel zusammen sind 360°. Berechne zuerst den dritten Winkel.'}
    fragen = [('Welche Darstellung zeigt am besten die Anteile am Ganzen (z. B. Verteilung des Taschengelds)?', 'Kreisdiagramm', ['Säulendiagramm mit abgeschnittener Achse', 'Strichliste', 'Urliste']),
              ('Welche Darstellung eignet sich am besten, um die Anzahlen mehrerer Gruppen direkt zu vergleichen?', 'Säulendiagramm', ['Kreisdiagramm ohne Beschriftung', 'Urliste', 'Strichliste ohne Bündel']),
              ('In einem Kreisdiagramm sind zwei Ausschnitte gleich groß. Was bedeutet das?', 'Beide Gruppen sind gleich häufig.', ['Beide Gruppen sind je 50 %.', 'Eine Gruppe ist doppelt so groß.', 'Man kann nichts sagen.'])]
    t, r, f = R.choice(fragen)
    return {**wahl(R, r, f), 'f': {'text': t}, 'w': f'Richtig: {r.rstrip(".")}. Kreisdiagramme zeigen Anteile am Ganzen (360° = 100 %), Säulendiagramme vergleichen Anzahlen.',
            'h': 'Was soll das Diagramm zeigen – Anteile oder Anzahlen?'}


# ---------- 6 Irreführend ----------
def achse_sehen():
    """Abgeschnittene Achse im Bild: Wie viel Mal so viel ist der zweite Wert wirklich?"""
    y0 = R.choice([80, 90, 180, 450, 900])
    sch = R.choice([1, 2, 5]) if y0 < 100 else R.choice([5, 10])
    d1 = sch * R.randint(1, 2)
    f = R.choice([2, 3, 4])
    a, b = y0 + d1, y0 + d1 * f
    if b - y0 > 5 * sch * 2: return achse_sehen()
    r = f'etwas mehr als 1-mal ({b - a} mehr)'
    return {**wahl(R, r, [f'{f}-mal', f'{f + 1}-mal', f'{2 * f}-mal']), 'f': {'text': f'Das Diagramm zeigt Punkte zweier Teams. Die Achse beginnt bei {y0}. Wie viel Mal so viel hat das zweite Team wirklich?',
                                                                      'grafik': saeulen([('Team 1', a), ('Team 2', b)], einheit='Punkte', y_start=y0)},
            'w': f'Abgelesen: {a} und {b}. Sichtbar sind nur {a - y0} und {b - y0} – darum wirkt die zweite Säule {f}-mal so hoch. Wirklich hat Team 2 nur {b - a} Punkte mehr als {a}, also etwas mehr als 1-mal so viel.',
            'h': 'Lies die echten Werte an der Achse ab, nicht die sichtbaren Säulenhöhen.'}


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
        if R.random() < .3:
            return achse_sehen()
        s = R.choice([100, 200, 500, 900, 950, 1000])
        d1 = R.choice([5, 10, 20, 25])
        f = R.choice([2, 3, 4, 5])
        a, b = s + d1, s + d1 * f
        g = saeulen([('Samstag', a), ('Sonntag', b)], einheit='Besucher', y_start=s)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Ein Säulendiagramm zeigt {zt(a)} und {zt(b)} Besucher. Die Hochachse beginnt bei {zt(s)}. Wie viel Mal so hoch wirkt die zweite Säule?', 'grafik': g},
                    'o': {'wert': f}, 'c': f'({b} - {s}) / ({a} - {s})', 'w': f'Sichtbare Höhen: {zt(a)} − {zt(s)} = {d1} und {zt(b)} − {zt(s)} = {d1 * f}. Sie wirkt {f}-mal so hoch.',
                    'h': 'Gezeichnet wird nur der Teil oberhalb des Achsenanfangs.'}
        mehr = Fr(b - a, a) * 100
        r = 'Nein, der Unterschied ist viel kleiner, als er aussieht.' if mehr < 50 else 'Ja, der Unterschied ist wirklich groß.'
        return {**wahl(R, r, ['Ja, der Unterschied ist wirklich groß.' if r.startswith('Nein') else 'Nein, der Unterschied ist viel kleiner, als er aussieht.', 'Das kann man ohne Achse nie sagen.'], 3),
                'f': {'text': f'Die Säulen für {zt(a)} und {zt(b)} Besucher sind bei einer Achse ab {zt(s)} gezeichnet. Die zweite Säule wirkt {f}-mal so hoch. Ist der Unterschied wirklich so groß?', 'grafik': g},
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
            'f': {'text': f'Ein Diagramm zur Wahl der Klassensprecherin zeigt {a} % und {b} %. Die Achse beginnt bei {s} %, deshalb wirkt die zweite Säule viel höher. Was ist irreführend?',
                  'grafik': saeulen([('Kandidatin A', a), ('Kandidatin B', b)], einheit='%', y_start=s)},
            'w': f'{b} % − {a} % = {b - a} Prozentpunkte. Mit einer Achse ab 0 sähen die Säulen fast gleich hoch aus.', 'h': 'Wo beginnt die Hochachse?'}


GEN = {'absolute_haeufigkeit': g_abs, 'relative_haeufigkeit': g_rel, 'tabelle_auswerten': g_tab, 'saeulendiagramm': g_saeule,
       'kreisdiagramm': g_kreis, 'irrefuehrend': g_irr}

DATEI = datei(E, 'Daten erfassen, absolute und relative Häufigkeiten bestimmen, Säulen- und Kreisdiagramme berechnen und irreführende Diagramme erkennen.', MERKE,
              [('Daten erfassen', ['absolute_haeufigkeit', 'relative_haeufigkeit', 'tabelle_auswerten']),
               ('Diagramme', ['saeulendiagramm', 'kreisdiagramm', 'irrefuehrend'])],
              ETAPPEN, GEN,
              offen=['Säulen- und Kreisdiagramme, Tabellen und abgeschnittene Achsen sind jetzt als Bilder in Lernkarten und Aufgaben eingebaut. Weiter offen: Diagramme selbst zeichnen (Säulenhöhe einstellen, Winkel einstellen) – das kann die App nicht.',
                     'Strichlisten stehen als Tabelle mit Strichen (||||| = Fünferbündel). Ein echtes Strichbündel mit Querstrich kann die App nicht zeichnen.',
                     'Bild-Diagramm (Münzen/Figuren statt Säulen) kann die App nicht zeichnen; die Aufgabe bleibt in Worten.',
                     'Kreisdiagramm-Ablesen ohne Zahlen nur mit gut erkennbaren Anteilen (1/2, 1/3, 1/4, 1/6, 1/8); andere Anteile lassen sich am Bild nicht sicher ablesen.'])

# ---------- KARTEN: Lernkarten nach dem neuen Muster (Achte Runde, Vorgabe 16.11., Paket U6) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl6.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl6 import umbau  # noqa: E402

U6_SPORT = {'typ': 'saeulen', 'einheit': 'Kinder', 'werte': [{'name': 'Fußball', 'wert': 18}, {'name': 'Schwimmen', 'wert': 10},
         {'name': 'Turnen', 'wert': 6}, {'name': 'Tennis', 'wert': 4}], 'y_start': 0, 'zahlen': True}
U6_WEG_KOPF = ['Schulweg', 'Bus', 'Rad', 'zu Fuß', 'Auto', 'Summe']

KARTEN = {
 'absolute_haeufigkeit': {
  'einstieg': 'In der Pause würfelt ihr: 2, 4, 2, 6, 2, 4. Wie oft kam die 2? Diese Anzahl heißt ⟦absolute Häufigkeit⟧.',
  'woerter': [['Urliste', 'die Werte in der Reihenfolge, in der sie gesammelt wurden'],
              ['Strichliste', 'für jeden Wert ein Strich'],
              ['absolute Häufigkeit', 'wie oft ein Wert vorkommt']],
  'bild': {'typ': 'tabelle', 'kopf': ['Augenzahl', '2', '4', '6'], 'zeilen': [['Striche', '', '', '']]},
  'schritte': [{'text': 'Geh die Urliste der Reihe nach durch.'},
               {'text': 'Mach für jeden Wert einen Strich in der Strichliste.', 'bild': {'zeilen': [['Striche', '|||', '||', '|']]}},
               {'text': 'Bei der 2 stehen 3 Striche. Die absolute Häufigkeit ist ⟦3⟧.',
                'bild': {'zeilen': [['Striche', '|||', '||', '|'], ['Anzahl', '3', '2', '1']]}}],
  'fehler': '3 verschiedene Augenzahlen sind keine Häufigkeit. Gefragt ist, wie oft die 2 gewürfelt wurde.',
  'regel': 'Zähle mit einer ⟦Strichliste⟧, wie oft ein Wert vorkommt. Alle Striche zusammen ergeben die Zahl der Würfe.'},
 'relative_haeufigkeit': {
  'einstieg': 'Lena würfelt 25-mal und hat 7 Sechsen, Tom 50-mal und 11 Sechsen. Wer hatte öfter Glück? Vergleiche den Anteil: die ⟦relative Häufigkeit⟧.',
  'woerter': [['relative Häufigkeit', 'absolute Häufigkeit geteilt durch die Gesamtzahl'],
              ['Gesamtzahl', 'die Anzahl aller Werte, hier aller Würfe']],
  'bild': {'typ': 'bruchstreifen', 'teile': 25, 'gefaerbt': 7, 'teil_text': 'Lena: 7 von 25', 'zeilen': [{'teile': 50, 'gefaerbt': 11, 'teil_text': 'Tom: 11 von 50'}]},
  'schritte': [{'text': 'Lena: 7 Sechsen geteilt durch die Gesamtzahl 25. 7 : 25 = ⟦28 %⟧.'},
               {'text': 'Tom: 11 : 50 = 0,22 = 22 %.'},
               {'text': '28 % ist mehr als 22 %. Lena hatte öfter eine Sechs.',
                'bild': {'typ': 'saeulen', 'einheit': '%', 'werte': [{'name': 'Lena', 'wert': 28}, {'name': 'Tom', 'wert': 22}], 'zahlen': True}}],
  'fehler': '7 Sechsen sind nicht 7 %. 7 % wären 7 Sechsen bei 100 Würfen. Teile durch die Gesamtzahl 25.',
  'regel': 'Relative Häufigkeit ist ⟦Anzahl durch Gesamtzahl⟧. Alle relativen Häufigkeiten zusammen ergeben 100 %.'},
 'tabelle_auswerten': {
  'einstieg': 'Eure Klasse hat gefragt: Wie kommst du zur Schule? Jede Antwort steht mit ihrer Anzahl in einer Tabelle. Das ist eine ⟦Häufigkeitstabelle⟧.',
  'woerter': [['Häufigkeitstabelle', 'eine Tabelle mit jeder Antwort und ihrer Anzahl'],
              ['Summe', 'alles zusammengezählt']],
  'bild': {'typ': 'tabelle', 'kopf': U6_WEG_KOPF, 'zeilen': [['Anzahl', '12', '9', '6', '3', '?']]},
  'schritte': [{'text': 'Die Summe aller Anzahlen: 12 + 9 + 6 + 3 = 30.',
                'bild': {'zeilen': [['Anzahl', '12', '9', '6', '3', '30']]}},
               {'text': 'Anteil Rad: 9 : 30 = 0,3.'},
               {'text': 'Mit dem Rad kommen ⟦30 %⟧ der Klasse.',
                'bild': {'zeilen': [['Anzahl', '12', '9', '6', '3', '30'], ['Anteil', '40 %', '30 %', '20 %', '10 %', '100 %']]}}],
  'fehler': 'Die größte Zahl ist nicht die Gesamtzahl. Befragt wurden nicht 12, sondern alle 30 Kinder.',
  'regel': 'Bilde zuerst die ⟦Summe⟧ aller Anzahlen. Der Anteil ist Anzahl geteilt durch Summe.'},
 'saeulendiagramm': {
  'einstieg': 'Die Klasse zeichnet ihre Lieblingssportarten als Säulen. 18 Kinder mögen Fußball, aber 18 cm passen nicht ins Heft. Darum legt ihr einen ⟦Maßstab⟧ fest.',
  'woerter': [['Säulendiagramm', 'ein Bild, in dem die Höhe jeder Säule eine Anzahl zeigt'],
              ['Maßstab', 'wie viel 1 cm bedeutet, hier 4 Kinder']],
  'bild': U6_SPORT,
  'schritte': [{'text': 'Der Maßstab ist 1 cm für 4 Kinder.'},
               {'text': 'Für Fußball rechnest du 18 : 4 = 4,5.'},
               {'text': 'Die Fußball-Säule im Säulendiagramm wird ⟦4,5 cm⟧ hoch.'}],
  'fehler': 'Die Säule 18 cm hoch zu zeichnen sprengt die Heftseite. Erst den Maßstab wählen, dann teilen.',
  'regel': 'Säulenhöhe ist ⟦Anzahl durch Maßstab⟧. Die Achse beginnt bei 0.'},
 'kreisdiagramm': {
  'einstieg': 'In einer Klasse mit 40 Kindern fahren 12 Rad. Das soll ein Tortenstück zeigen, so groß wie sein Anteil. So ein Bild heißt ⟦Kreisdiagramm⟧.',
  'woerter': [['Kreisdiagramm', 'ein Kreis aus Stücken; jedes Stück zeigt einen Anteil'],
              ['Winkel', 'wie weit ein Stück geöffnet ist, in Grad (°)']],
  'bild': {'typ': 'kreisdiagramm', 'einheit': ' %', 'werte': [{'name': 'Rad', 'wert': 30}, {'name': 'Bus', 'wert': 40},
           {'name': 'zu Fuß', 'wert': 20}, {'name': 'Auto', 'wert': 10}], 'zahlen': True},
  'schritte': [{'text': 'Anteil Rad: 12 : 40 = 0,3 = 30 %.'},
               {'text': 'Der ganze Kreis hat 360°. Der Winkel für Rad ist 0,3 · 360° = ⟦108°⟧.'},
               {'text': 'Bus 144°, zu Fuß 72°, Auto 36°. Zusammen sind es 360°.'}],
  'fehler': '30 % sind nicht 30°. Dann wäre die ganze Torte nur 100° groß. Rechne mit 360°.',
  'regel': 'Der Winkel ist ⟦Anteil · 360°⟧. Alle Winkel zusammen ergeben 360°.'},
 'irrefuehrend': {
  'einstieg': 'Ein Freibad wirbt: „Sonntag doppelt so viele Besucher!“ Die Säule ist doppelt so hoch. Doch es waren 980 und 1 000 Besucher: ein ⟦irreführendes Diagramm⟧.',
  'woerter': [['irreführend', 'erzeugt einen falschen Eindruck, obwohl die Zahlen stimmen'],
              ['abgeschnittene Achse', 'die Achse beginnt nicht bei 0']],
  'bild': {'typ': 'saeulen', 'einheit': 'Besucher', 'werte': [{'name': 'Samstag', 'wert': 980}, {'name': 'Sonntag', 'wert': 1000}], 'y_start': 960, 'zahlen': True},
  'schritte': [{'text': 'Die Achse beginnt erst bei 960. Das ist eine abgeschnittene Achse.'},
               {'text': 'Sichtbar sind nur 20 und 40 Besucher. Darum wirkt Sonntag doppelt.'},
               {'text': 'Mit Achse ab 0 sieht man: nur ⟦20 Besucher⟧ mehr.', 'bild': {'y_start': 0}}],
  'fehler': 'Nur auf die Höhe der Säulen zu schauen ist ein Fehler. Lies immer zuerst die Zahlen an der Achse.',
  'regel': 'Lies immer ⟦Achse und Zahlen⟧. Beginnt die Achse nicht bei 0, wirken Unterschiede größer.'},
}

umbau(DATEI, KARTEN)



# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl6): je Lernkarte 2 Übungen Stufe 2 + 4 Übungen Stufe 3 ----------
# Läuft nach allen bisherigen Aufgaben mit eigenem Zufallsstart; die bisherigen Aufgaben bleiben unverändert.
# Prüfungsvorbilder: Jahrgangsstufentest Realschule Jgst. 6 (ISB) 2014 Nr. 2 (Rangfolge aus Aussagen dem Diagramm zuordnen),
# 2019 Nr. 14 (Achse beginnt nicht bei 0 – fehlende Information), 2024 Nr. 19 (Gesamtzahl aus einem Diagrammteil), 2025 (Säulen ergänzen);
# Bayerischer Mathematik-Test Jgst. 8 (ISB) 2014 Gruppe B Aufg. 3 (relative Häufigkeit eines Buchstabens), 2021 Aufg. 6a (Rückgang wirkt
# dramatischer), 2022 Aufg. 5 (Kreisdiagramm in Prozent auswerten), 2023 Aufg. 5 (Tabelle mit Anteilen und Beträgen), 2024 Aufg. 3
# (Säulen in Prozent, „doppelt so groß“ prüfen, Gesamtzahl aus Prozentsatz), 2025 Aufg. 6a (Anteil einer Säule mit einem Drittel vergleichen).
from _schwer_kl6 import ergaenzen, zahl, wahl, anteil  # noqa: E402

_SATZ = 'ANNA NENNT NEUN NAMEN'
_BUCHST = _SATZ.replace(' ', '')
_T6 = tabelle(['Schulweg', '6a', '6b'], [['Bus', 12, 9], ['Rad', 7, 15], ['zu Fuß', 6, 6]])
_VF = tabelle(['', 'Haustier', 'kein Haustier'], [['Mädchen', 9, 5], ['Jungen', 6, 9]])


def _dd():
    return {
        'absolute_haeufigkeit': [
            (2, lambda R: zahl('Würfelergebnisse: 3, 5, 2, 5, 6, 1, 5, 3, 2, 5, 4, 3. Welche Augenzahl kam am häufigsten?', 5, '5',
                               'Zähle für jede Augenzahl, wie oft sie vorkommt.', '1: 1-mal, 2: 2-mal, 3: 3-mal, 4: 1-mal, 5: 4-mal, 6: 1-mal. Am häufigsten: 5.')),
            (2, lambda R: zahl('Die Strichliste zeigt eine Umfrage zum Schulweg. Wie viele Kinder kommen nicht mit dem Bus?', 23, '9 + 11 + 3',
                               'Zähle alle Striche außer bei „Bus“. Ein Bündel sind 5 Striche.', 'Rad 9, zu Fuß 11, Auto 3. Zusammen 23 Kinder.',
                               grafik=tabelle(['Schulweg', 'Strichliste'], [['Bus', '||||| ||'], ['Rad', '||||| ||||'], ['zu Fuß', '||||| ||||| |'], ['Auto', '|||']]))),
            (3, lambda R: wahl(R, 'Bei einer Wahl bekommt Pia mehr Stimmen als Ben. Lea bekommt weniger Stimmen als Tom, aber mehr als Pia. Wer hat die zweitmeisten Stimmen?',
                               'Lea', ['Tom', 'Pia', 'Ben'], 'Ordne Schritt für Schritt: Wer steht über wem?',
                               'Pia > Ben. Lea > Pia und Tom > Lea. Reihenfolge: Tom, Lea, Pia, Ben. Zweiter Platz: Lea.')),
            (3, lambda R: zahl('In einer Strichliste mit vier Farben stehen zusammen 30 Striche. „Rot“ hat doppelt so viele wie „Blau“, „Grün“ hat 3 mehr als „Blau“ '
                               'und „Gelb“ hat 3. Wie viele Striche hat „Rot“?', 12, '2 * ((30 - 3 - 3) // 4)',
                               'Rot und Grün hängen von Blau ab. Probiere Zahlen für Blau aus.',
                               'Ohne Gelb und ohne die 3 Extra-Striche von Grün bleiben 30 − 3 − 3 = 24 für 4 gleiche Teile (Blau, Rot = 2 Teile, Grün). '
                               'Blau 6, Rot 12, Grün 9, Gelb 3. Probe: 6 + 12 + 9 + 3 = 30.')),
            (3, lambda R: zahl('Ein Würfel wird 20-mal geworfen. Die Summe aller Augenzahlen ist 20. Wie oft fiel die 1?', 20, '20',
                               'Was ist die kleinste mögliche Augenzahl bei einem Wurf?', 'Jeder Wurf zählt mindestens 1. Bei 20 Würfen ist die Summe nur 20, wenn jeder Wurf eine 1 war.')),
            (3, lambda R: zahl('Bei 50 Würfen fiel die 6 genau 7-mal und die 1 doppelt so oft wie die 6. Wie oft fielen die Augenzahlen 2, 3, 4 und 5 zusammen?', 29,
                               '50 - 7 - 2 * 7', 'Rechne zuerst aus, wie oft die 1 fiel.', 'Die 1 fiel 14-mal. 50 − 7 − 14 = 29.')),
        ],
        'relative_haeufigkeit': [
            (2, lambda R: zahl('Von 80 Losen sind 12 Gewinne. Gib die relative Häufigkeit der Gewinne in Prozent an.', 15, '12 / 80 * 100', 'Anzahl durch Gesamtzahl.',
                               '12/80 = 3/20 = 15/100 = 15 %.', einheit='%')),
            (2, lambda R: anteil('18 von 45 Kindern spielen Fußball. Gib die relative Häufigkeit als vollständig gekürzten Bruch an.', 18, 45, 'Anzahl durch Gesamtzahl, dann kürzen.',
                                 '18/45, durch 9 gekürzt: 2/5.')),
            (3, lambda R: wahl(R, 'Das Diagramm zeigt, wie viele Runden die Kinder beim Spendenlauf geschafft haben. Haben mehr als ein Drittel aller Kinder genau 10 Runden geschafft?',
                               'Nein, es ist genau ein Drittel.', ['Ja, 50 ist die höchste Säule.', 'Nein, es ist weniger als ein Viertel.', 'Ja, es sind 50 %.'],
                               'Bilde zuerst die Summe aller Kinder.', '24 + 50 + 40 + 36 = 150 Kinder. 50 von 150 = 1/3 – genau ein Drittel, nicht mehr.',
                               grafik=saeulen([('5', 24), ('10', 50), ('15', 40), ('20', 36)], einheit='Kinder'))),
            (3, lambda R: anteil(f'Wie groß ist die relative Häufigkeit des Buchstabens N im Satz „{_SATZ}“? Zähle nur Buchstaben, keine Leerzeichen. Gib einen gekürzten Bruch an.',
                                 _BUCHST.count('N'), len(_BUCHST), 'Zähle zuerst alle Buchstaben, dann alle N.',
                                 f'Der Satz hat {len(_BUCHST)} Buchstaben, davon {_BUCHST.count("N")}-mal N. {_BUCHST.count("N")}/{len(_BUCHST)} = 1/2.')),
            (3, lambda R: zahl('In einer Klasse trägt 1/4 der Kinder eine Brille. Zwei neue Kinder mit Brille kommen dazu. Jetzt trägt 1/3 der Kinder eine Brille. '
                               'Wie viele Kinder sind jetzt in der Klasse?', 18, '16 + 2',
                               'Probiere: Die alte Klassengröße muss durch 4 teilbar sein, die neue durch 3.',
                               'Alt 16 Kinder, 4 mit Brille. Neu 18 Kinder, 6 mit Brille: 6/18 = 1/3. Es passt.')),
            (3, lambda R: zahl('Bei 24 Würfen gab es 6 Treffer. Ein Kind rechnet die relative Häufigkeit als 6/18 aus (Treffer durch Nicht-Treffer). '
                               'Wie groß ist sie richtig in Prozent?', 25, '6 / 24 * 100', 'Durch die Gesamtzahl aller Würfe teilen.', '6/24 = 1/4 = 25 %.', einheit='%')),
        ],
        'tabelle_auswerten': [
            (2, lambda R: zahl('Die Tabelle zeigt, wie viele Kinder einer Klasse ein Haustier haben. Wie viele Kinder haben ein Haustier?', 15, '9 + 6',
                               'Addiere die Spalte „Haustier“.', 'Mädchen 9, Jungen 6. Zusammen 15.', grafik=_VF)),
            (2, lambda R: zahl('Die Tabelle zeigt, wie viele Kinder einer Klasse ein Haustier haben. Wie viel Prozent der Jungen haben ein Haustier?', 40, '6 / (6 + 9) * 100',
                               'Ganzes sind nur die Jungen.', 'Jungen: 6 + 9 = 15. 6 von 15 = 2/5 = 40 %.', einheit='%', grafik=_VF)),
            (3, lambda R: zahl('Eine Schule hat 400 Kinder. Jedes Kind zahlt Kopiergeld: Die Tabelle zeigt, welcher Anteil der Kinder wie viel zahlt. Wie viel Euro kommen insgesamt zusammen?', 3640,
                               '400 * 60 / 100 * 8 + 400 / 4 * 10 + (400 - 240 - 100) * 12',
                               'Rechne für jede Gruppe die Zahl der Kinder aus. Der Rest ist das, was zu 100 % fehlt.',
                               '60 % von 400 = 240 Kinder · 8 € = 1 920 €. 1/4 = 100 Kinder · 10 € = 1 000 €. Rest 60 Kinder · 12 € = 720 €. Zusammen 3 640 €.',
                               einheit='€', grafik=tabelle(['Jahrgang', '5 bis 7', '8 bis 10', '11 bis 13'], [['Anteil', '60 %', '1/4', 'Rest'], ['Betrag', '8 €', '10 €', '12 €']]))),
            (3, lambda R: zahl('In der Tabelle fehlen Werte. Wie viele Kinder tragen insgesamt eine Brille?', 12, '5 + (16 - 9)',
                               'Rechne zuerst die fehlende Zahl bei den Jungen aus.', 'Jungen mit Brille: 16 − 9 = 7. Zusammen mit den 5 Mädchen: 12 Kinder.',
                               grafik=tabelle(['', 'Brille', 'keine Brille', 'Summe'], [['Mädchen', '5', '?', '14'], ['Jungen', '?', '9', '16']]))),
            (3, lambda R: wahl(R, 'Die Tabelle zeigt den Schulweg in zwei Klassen. Welche Aussage stimmt?', 'In der 6b fährt ein größerer Anteil Rad als in der 6a.',
                               ['Die Hälfte der 6a fährt Bus.', 'In der 6a fahren mehr Kinder Rad als Bus.', 'In der 6a fährt ein größerer Anteil Rad als in der 6b.'],
                               'Bilde für jede Klasse die Summe. Vergleiche Anteile, nicht nur Anzahlen.',
                               '6a: 25 Kinder, Rad 7/25 = 28 %, Bus 12/25 = 48 %. 6b: 30 Kinder, Rad 15/30 = 50 %. Nur die erste Aussage stimmt.', grafik=_T6)),
            (3, lambda R: zahl('Die Tabelle zeigt den Schulweg in zwei Klassen. Wie viel Prozent aller Kinder beider Klassen fahren Rad?', 40, '(7 + 15) / (25 + 30) * 100',
                               'Addiere alle Radfahrer und alle Kinder.', 'Rad: 7 + 15 = 22. Alle: 25 + 30 = 55. 22/55 = 2/5 = 40 %.', einheit='%', grafik=_T6)),
        ],
        'saeulendiagramm': [
            (2, lambda R: zahl('Das Säulendiagramm zeigt verkaufte Kugeln Eis. Um wie viele Kugeln ist die höchste Säule größer als die niedrigste?', 30, '55 - 25',
                               'Suche die höchste und die niedrigste Säule.', 'Höchste Säule 55 (Mi), niedrigste 25 (Di). 55 − 25 = 30.',
                               grafik=saeulen([('Mo', 40), ('Di', 25), ('Mi', 55), ('Do', 30), ('Fr', 50)], einheit='Kugeln'))),
            (2, lambda R: zahl('Maßstab im Säulendiagramm: 1 cm steht für 25 Kinder. Eine Säule ist 6,4 cm hoch. Für wie viele Kinder steht sie?', 160, '6.4 * 25',
                               'Rechne Höhe mal Maßstab.', '6,4 · 25 = 160 Kinder.')),
            (3, lambda R: zahl('Das Diagramm zeigt die Noten 1 bis 5 einer Klasse mit 28 Kindern. Die Säule für Note 6 fehlt. Wie viele Kinder haben Note 6?', 1, '28 - (3 + 7 + 10 + 5 + 2)',
                               'Addiere alle gezeichneten Säulen und vergleiche mit 28.', '3 + 7 + 10 + 5 + 2 = 27. 28 − 27 = 1 Kind hat Note 6.',
                               grafik=saeulen([('1', 3), ('2', 7), ('3', 10), ('4', 5), ('5', 2)], einheit='Kinder'))),
            (3, lambda R: zahl('Das Diagramm zeigt in Prozent, wie Kinder zur Schule kommen. Die Säule „Rad“ steht für 63 Kinder. Wie viele Kinder wurden befragt?', 180, '63 / 35 * 100',
                               '63 Kinder sind 35 %. Rechne über 5 % auf 100 %.', '35 % = 63 Kinder, 5 % = 9 Kinder, 100 % = 180 Kinder.',
                               grafik=saeulen([('Bus', 45), ('Rad', 35), ('zu Fuß', 20)], einheit='%'))),
            (3, lambda R: zahl('Ein Kind zeichnet Säulen für 12, 30 und 45 Kinder. Die kleinste Säule ist 2 cm hoch. Wie hoch wird die größte Säule?', Fr('7.5'), '45 / 12 * 2',
                               'Wie viele Kinder stehen für 1 cm?', '2 cm für 12 Kinder: 1 cm für 6 Kinder. 45 : 6 = 7,5 cm.', einheit='cm')),
            (3, lambda R: zahl('Das Säulendiagramm zeigt verkaufte Kugeln Eis. Wie viel Prozent aller Kugeln der Woche wurden am Mittwoch verkauft?', Fr('27.5'),
                               '55 / (40 + 25 + 55 + 30 + 50) * 100', 'Bilde zuerst die Summe der Woche.', 'Woche: 40 + 25 + 55 + 30 + 50 = 200. 55 von 200 = 27,5 %.', einheit='%',
                               grafik=saeulen([('Mo', 40), ('Di', 25), ('Mi', 55), ('Do', 30), ('Fr', 50)], einheit='Kugeln'))),
        ],
        'kreisdiagramm': [
            (2, lambda R: zahl('Wie groß ist der Winkel für den Anteil 3/8 im Kreisdiagramm?', 135, '360 * 3 / 8', 'Anteil mal 360°.', '360° : 8 = 45°. 45° · 3 = 135°.', einheit='°')),
            (2, lambda R: zahl('Es wurden 40 Personen befragt. Wie groß ist im Kreisdiagramm der Winkel für eine einzige Person?', 9, '360 / 40', 'Die 360° werden auf 40 Personen verteilt.',
                               '360° : 40 = 9°.', einheit='°')),
            (3, lambda R: zahl('Im Kreisdiagramm hat „Schwimmen“ einen Winkel von 72°. Das sind 56 Kinder. Wie viele Kinder wurden befragt?', 280, '56 * 360 / 72',
                               'Welcher Anteil des Kreises sind 72°?', '72° von 360° = 1/5. 56 Kinder sind 1/5, also 5 · 56 = 280 Kinder.')),
            (3, lambda R: zahl('Das Kreisdiagramm zeigt, welche Schulnote sich 1 200 Erwachsene in Mathematik selbst geben. Wie viele gaben sich Note 2 oder besser?', 564,
                               '1200 * (12 + 35) / 100', 'Addiere die Prozente für Note 1 und Note 2.', '12 % + 35 % = 47 %. 47 % von 1 200 = 564.',
                               grafik=kreisdiagramm([('Note 1', 12), ('Note 2', 35), ('Note 3', 28), ('Note 4', 15), ('Note 5', 7), ('Note 6', 3)], einheit=' %'))),
            (3, lambda R: zahl('Ein Kreisdiagramm hat drei Teile. Teil A ist doppelt so groß wie Teil B. Teil C ist so groß wie A und B zusammen. Wie groß ist der Winkel von A?', 120,
                               '2 * 360 / 6', 'Wenn B ein Stück ist, wie viele Stücke sind A und C?', 'B = 1 Stück, A = 2 Stücke, C = 3 Stücke: 6 Stücke = 360°, 1 Stück = 60°. A = 120°.',
                               einheit='°')),
            (3, lambda R: zahl('Ein Kind zeichnet 25 % als Kreisausschnitt mit 25°. Wie groß muss der Winkel richtig sein?', 90, '360 * 25 / 100',
                               'Der ganze Kreis hat 360°, nicht 100°.', '25 % = 1/4. 360° : 4 = 90°.', einheit='°')),
        ],
        'irrefuehrend': [
            (2, lambda R: wahl(R, 'An der Hochachse eines Säulendiagramms stehen keine Zahlen. Was kann man dann nicht ablesen?', 'die genauen Anzahlen',
                               ['welche Säule am höchsten ist', 'welche Säule am niedrigsten ist', 'wie viele Säulen es gibt'],
                               'Was zeigt eine Achse mit Zahlen?', 'Ohne Zahlen sieht man nur die Reihenfolge der Säulen, aber nicht die Werte.')),
            (2, lambda R: zahl('Ein Diagramm zeigt 200 und 210 Besucher. Die Hochachse beginnt bei 190, deshalb wirkt die zweite Säule doppelt so hoch. '
                               'Um wie viel Prozent sind es wirklich mehr Besucher?', 5, '(210 - 200) / 200 * 100', 'Rechne mit den echten Zahlen, nicht mit den Säulenhöhen.',
                               '10 mehr von 200 = 5 %. Nur wegen der abgeschnittenen Achse wirkt es wie das Doppelte.', einheit='%',
                               grafik=saeulen([('Tag 1', 200), ('Tag 2', 210)], einheit='Besucher', y_start=190))),
            (3, lambda R: wahl(R, 'Ein Säulendiagramm über Haarfarben in einer Klasse beginnt bei 6 Kindern. Bei „rot“ ist keine Säule zu sehen. Was kann man sagen?',
                               'Es könnten 0 bis 6 rothaarige Kinder sein – genau ablesen kann man es nicht.',
                               ['Es gibt keine rothaarigen Kinder.', 'Es gibt genau 6 rothaarige Kinder.', 'Das Diagramm ist falsch gezeichnet.'],
                               'Was passiert mit Werten, die kleiner sind als der Anfang der Achse?', 'Werte bis 6 sind unsichtbar. Es fehlt die Information, wie viele es genau sind.')),
            (3, lambda R: zahl('Ein Diagramm zeigt die Zahl der Vereinsmitglieder: 1 000 im ersten Jahr, 950 im zweiten. Die Achse beginnt bei 900, die zweite Säule wirkt halb so hoch. '
                               'Um wie viel Prozent ist die Zahl wirklich gesunken?', 5, '(1000 - 950) / 1000 * 100', 'Grundwert ist das erste Jahr.',
                               '50 weniger von 1 000 = 5 %. Die Säule wirkt halbiert, weil die Achse erst bei 900 beginnt.', einheit='%',
                               grafik=saeulen([('Jahr 1', 1000), ('Jahr 2', 950)], einheit='Mitglieder', y_start=900))),
            (3, lambda R: wahl(R, 'Der Anteil der Kinder ohne Fahrradhelm stieg von 12 % auf 20 %. In einer Zeitung steht: „Der Anteil hat sich verdoppelt.“ Stimmt das?',
                               'Nein: Verdoppelt wären 24 %. 20 % ist weniger als das Doppelte.',
                               ['Ja, er ist um 8 Prozentpunkte gestiegen.', 'Ja, 20 ist fast 24.', 'Nein, er hat sich verdreifacht.'],
                               'Was wäre das Doppelte von 12 %?', '2 · 12 % = 24 %. 20 % ist etwa das 1,7-Fache. „Verdoppelt“ übertreibt.')),
            (3, lambda R: zahl('Ein Bild-Diagramm zeigt den doppelten Wert durch einen Würfel mit doppelter Kantenlänge. Wie viel Mal so groß ist das Volumen des großen Würfels?', 8, '2 ** 3',
                               'Länge, Breite und Höhe werden jeweils verdoppelt.', '2 · 2 · 2 = 8. Der Würfel wirkt 8-mal so groß, obwohl der Wert nur doppelt so groß ist.')),
        ],
    }


ergaenzen(DATEI, _dd(), seed=6057)


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
import re as _re  # noqa: E402

from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('daten.darstellen', 13_6_7)
# c) „Wie oft wurde „X“ häufiger genannt als „Y“?“ ist sprachlich missverständlich → „Wie viele Nennungen hat „X“ mehr als „Y“?“
#    (alle Pools; Tabelle, Lösung und Weg bleiben gleich)
_muster = _re.compile(r'Wie oft wurde „([^“]+)“ häufiger genannt als „([^“]+)“\?')
for _a in [a for a in DATEI['aufgaben'] if _muster.search(a['f']['text'])]:
    _alt = _a['f']['text']
    _neu = BF.Z(_muster.sub(r'Wie viele Nennungen hat „\1“ mehr als „\2“?', _alt), _a['o']['wert'], _a['c'], _a['w'],
                _a.get('h', 'Zähle beide Zeilen und bilde den Unterschied.'), grafik=_a['f'].get('grafik'))
    BF.ersetze(_a['l'], _alt, _neu, pools=(_a['p'],))
# a) Grundform → Stufe 1
for _t in ['In einer Strichliste stehen bei „Hund“: 3 Fünferbündel. Wie oft wurde „Hund“ genannt?',
           'In einer Strichliste stehen bei „Hund“: 2 Fünferbündel und 2 einzelne Striche. Wie oft wurde „Hund“ genannt?',
           'In einer Strichliste stehen bei „Hund“: 4 Fünferbündel und 2 einzelne Striche. Wie oft wurde „Hund“ genannt?']:
    BF.stufe('absolute_haeufigkeit', _t, 1)
# a) Stufe 2
BF.stufe('kreisdiagramm', 'Ein Kreisausschnitt hat einen Winkel von 36°. Wie viel Prozent stellt er dar?', 2)
BF.stufe('relative_haeufigkeit', 'Bei 20 Münzwürfen lag die relative Häufigkeit für „Zahl“ bei 5 %. Wie oft fiel „Zahl“?', 2)

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    schreibe(DATEI)
