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

# ---------- KLAR: verständliche Erklärungen (Siebte Runde, Pflicht seit 15.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _klar_kl6.py) – die Aufgaben bleiben wörtlich gleich.
from _klar_kl6 import klar  # noqa: E402

KLAR = {
 'absolute_haeufigkeit': {
  'einstieg': 'In der Pause würfelt ihr und schreibt jedes Ergebnis auf: 2, 4, 2, 6, 2, 4. Wie oft kam die 2? Du zählst nach und kommst auf 3. Diese Anzahl heißt ⟦absolute Häufigkeit⟧.',
  'woerter': [['Daten', 'gesammelte Werte, z. B. Würfelergebnisse oder Antworten einer Umfrage'],
              ['Urliste', 'die Daten in der Reihenfolge, in der sie gesammelt wurden'],
              ['Strichliste', 'für jeden Wert ein Strich; jeder fünfte Strich wird quer über die vier anderen gezogen (Fünferbündel)'],
              ['absolute Häufigkeit', 'wie oft ein Wert vorkommt – eine Anzahl']],
  'schritte': ['Die Urliste lautet: 2, 4, 2, 6, 2, 4.',
               'Geh die Liste von vorn nach hinten durch und mach für jeden Wert einen Strich: bei der 2 drei Striche, bei der 4 zwei, bei der 6 einen.',
               'Kontrolle: 3 + 2 + 1 = 6 Striche – genauso viele, wie es Würfe gab.',
               'Die absolute Häufigkeit der 2 ist ⟦3⟧.'],
  'regel': 'So bestimmst du die absolute Häufigkeit: Geh die ⟦Urliste⟧ der Reihe nach durch und führe eine ⟦Strichliste⟧. Die Zahl der Striche bei einem Wert ist seine ⟦absolute Häufigkeit⟧ – wie oft er vorkommt.',
  'fehler': 'Die Anzahl ⟦verschiedener⟧ Werte (hier 3: die 2, die 4 und die 6) ist keine Häufigkeit. Gefragt ist, ⟦wie oft⟧ ein bestimmter Wert gewürfelt wurde – bei der 2 dreimal.'},
 'relative_haeufigkeit': {
  'einstieg': 'Lena hat 25-mal gewürfelt und 7 Sechsen bekommen, Tom hat 50-mal gewürfelt und 11 Sechsen. Wer hatte öfter Glück? Die Anzahlen allein helfen nicht, denn die beiden haben verschieden oft gewürfelt. Vergleichen kannst du den Anteil der Sechsen an allen Würfen. Er heißt ⟦relative Häufigkeit⟧.',
  'woerter': [['Gesamtzahl', 'die Anzahl aller Werte – hier aller Würfe'],
              ['Anteil', 'Teil durch Ganzes, als Bruch, Dezimalzahl oder in Prozent'],
              ['relative Häufigkeit', 'absolute Häufigkeit geteilt durch die Gesamtzahl']],
  'schritte': ['Lena hat 7 Sechsen bei 25 Würfen. Teile die absolute Häufigkeit durch die Gesamtzahl: 7/25.',
               'Als Dezimalzahl: 7 : 25 = 0,28.',
               'In Prozent: 0,28 = ⟦28 %⟧.',
               'Tom: 11 : 50 = 0,22 = 22 %. Lena hatte also anteilig öfter eine Sechs.'],
  'regel': 'So bestimmst du die relative Häufigkeit: Rechne ⟦absolute Häufigkeit : Gesamtzahl⟧ und gib das Ergebnis als Bruch, Dezimalzahl oder in Prozent an. Alle relativen Häufigkeiten zusammen ergeben ⟦1 = 100 %⟧.',
  'fehler': '7 Sechsen bei 25 Würfen sind ⟦nicht⟧ 7 %: 7 % wären 7 Sechsen bei 100 Würfen. Man muss durch die ⟦Gesamtzahl⟧ teilen: 7 : 25 = 0,28 = 28 %.'},
 'tabelle_auswerten': {
  'einstieg': 'Eure Klasse hat eine Umfrage gemacht: Wie kommst du zur Schule? Statt 30 einzelne Antworten aufzuschreiben, fasst ihr sie zusammen: zu jeder Antwort die Anzahl. So eine Übersicht heißt ⟦Häufigkeitstabelle⟧.',
  'woerter': [['Umfrage', 'viele Personen bekommen dieselbe Frage gestellt'],
              ['Häufigkeitstabelle', 'eine Tabelle mit jeder Antwort und ihrer Anzahl'],
              ['Summe', 'das Ergebnis, wenn man alles zusammenzählt'],
              ['Grundwert', 'das Ganze (100 %) – hier alle 30 befragten Kinder']],
  'schritte': ['In der Tabelle stehen: Bus 12, Rad 9, zu Fuß 6, Auto 3.',
               'Zähle alle Anzahlen zusammen: 12 + 9 + 6 + 3 = 30. So viele Kinder wurden befragt.',
               'Für den Anteil der Radfahrer teilst du durch diese Gesamtzahl: 9 : 30 = 0,3.',
               'Mit dem Rad kommen ⟦30 %⟧ der Klasse.'],
  'regel': 'So wertest du eine Häufigkeitstabelle aus: Bilde zuerst die ⟦Summe⟧ aller Anzahlen – das ist die ⟦Gesamtzahl⟧. Sie ist der Grundwert für alle Anteile: Anteil = Anzahl : Gesamtzahl.',
  'fehler': 'Die größte Zahl in der Tabelle ist ⟦nicht⟧ die Gesamtzahl: 12 Kinder fahren Bus, befragt wurden aber alle 30. Die Gesamtzahl ist die ⟦Summe⟧ aller Anzahlen.'},
 'saeulendiagramm': {
  'einstieg': 'Die Klasse will das Ergebnis der Umfrage „Lieblingssport“ ins Heft zeichnen: für jeden Sport eine Säule, je höher, desto mehr Kinder. 18 Kinder mögen Fußball – eine 18 cm hohe Säule passt kaum auf die Seite. Darum legt ihr fest, wie viele Kinder 1 cm bedeutet. Diese Festlegung heißt ⟦Maßstab⟧.',
  'woerter': [['Säulendiagramm', 'ein Bild, in dem die Höhe jeder Säule eine Anzahl zeigt'],
              ['Hochachse', 'die senkrechte Linie links, an der man die Höhe abliest'],
              ['Skala', 'die gleichmäßige Einteilung der Hochachse mit Zahlen'],
              ['Maßstab', 'wie viel 1 cm im Diagramm bedeutet, z. B. 1 cm für 4 Kinder']],
  'schritte': ['Der Maßstab ist 1 cm für 4 Kinder. Die Säule für Fußball soll 18 Kinder zeigen.',
               'Frage: Wie oft passen 4 Kinder in 18 Kinder? Das rechnest du mit 18 : 4 = 4,5.',
               'Jeder Zentimeter steht für 4 Kinder, also brauchst du 4,5 Zentimeter.',
               'Die Fußball-Säule wird ⟦4,5 cm⟧ hoch. Die Hochachse beginnt dabei bei 0.'],
  'regel': 'So zeichnest du ein Säulendiagramm: Wähle einen ⟦Maßstab⟧ (z. B. 1 cm für 4 Kinder) und rechne jede Säulenhöhe als ⟦Anzahl : Maßstab⟧. Die Hochachse beginnt bei ⟦0⟧, alle Säulen sind gleich breit.',
  'fehler': 'Die Säule für 18 Kinder 18 cm hoch zu zeichnen, sprengt fast die Heftseite – bei mehr Kindern passt es gar nicht mehr. Erst einen ⟦Maßstab⟧ wählen, dann ⟦Anzahl : Maßstab⟧ rechnen.'},
 'kreisdiagramm': {
  'einstieg': 'In einer anderen Klasse mit 40 Kindern kommt bei derselben Umfrage heraus: 12 fahren Rad, 16 Bus, 8 gehen zu Fuß und 4 werden mit dem Auto gebracht. Das soll eine Torte zeigen, bei der jedes Stück so groß ist wie sein Anteil. So eine Darstellung heißt ⟦Kreisdiagramm⟧.',
  'woerter': [['Kreisdiagramm', 'ein Kreis, aufgeteilt in Stücke; jedes Stück zeigt einen Anteil'],
              ['Kreisausschnitt', 'ein „Tortenstück“ des Kreises'],
              ['Winkel', 'wie weit ein Tortenstück geöffnet ist, gemessen in Grad (°)'],
              ['360°', 'der ganze Kreis; er steht für 100 %']],
  'schritte': ['Rechne zuerst den Anteil der Radfahrer aus: 12 : 40 = 0,3 = 30 %.',
               'Der ganze Kreis hat 360°. Der Ausschnitt bekommt 30 % davon: 0,3 · 360° = 108°.',
               'Genauso rechnest du die anderen: Bus 40 % → 144°, zu Fuß 20 % → 72°, Auto 10 % → 36°.',
               'Der Ausschnitt für Rad hat ⟦108°⟧. Zur Kontrolle ergeben alle Winkel zusammen 360°.'],
  'regel': 'So berechnest du ein Kreisdiagramm: Bestimme für jede Antwort den ⟦Anteil⟧ (Anzahl : Gesamtzahl). Der Winkel ist ⟦Anteil · 360°⟧ – 1 % entspricht 3,6°. Alle Winkel zusammen ergeben ⟦360°⟧.',
  'fehler': '30 % als Winkel von 30° einzuzeichnen ist falsch: Dann wäre die ganze Torte nur 100° groß – nicht einmal ein halber Kreis. Der Vollkreis hat ⟦360°⟧: 30 % sind 0,3 · 360° = 108°.'},
 'irrefuehrend': {
  'einstieg': 'Ein Freibad wirbt: „Am Sonntag doppelt so viele Besucher wie am Samstag!“ Im Diagramm ist die Sonntagssäule tatsächlich doppelt so hoch. Liest du die Zahlen, waren es aber 980 und 1 000 Besucher. Das Bild täuscht, weil die Hochachse erst bei 960 beginnt. So ein Bild heißt ⟦irreführendes Diagramm⟧.',
  'woerter': [['irreführend', 'erzeugt einen falschen Eindruck, obwohl die Zahlen stimmen'],
              ['abgeschnittene Achse', 'die Hochachse beginnt nicht bei 0, sondern weiter oben'],
              ['Fläche', 'wie viel Platz eine Figur einnimmt; doppelt so hoch und doppelt so breit heißt viermal so viel Fläche']],
  'schritte': ['Die Säulen zeigen 980 und 1 000 Besucher. Die Hochachse beginnt bei 960.',
               'Sichtbar ist nur der Teil über 960: 980 − 960 = 20 und 1 000 − 960 = 40.',
               'Darum wirkt die Sonntagssäule doppelt so hoch wie die Samstagssäule.',
               'In Wirklichkeit kamen am Sonntag nur ⟦20 Besucher⟧ mehr – etwa 2 %.'],
  'regel': 'So erkennst du ein irreführendes Diagramm: Lies immer ⟦Achse und Zahlen⟧. Prüfe, ob die Hochachse ⟦bei 0 beginnt⟧, ob die Abstände auf der Achse gleich sind und ob alles beschriftet ist. Bei Bildern statt Säulen gilt: doppelt so hoch und doppelt so breit ergibt die ⟦vierfache Fläche⟧.',
  'fehler': 'Nur auf die Säulenhöhen zu schauen, ohne die Achse zu lesen, ist ein Fehler: Bei abgeschnittener Achse wirken kleine Unterschiede ⟦riesig⟧ – genau darauf setzt die Werbung des Freibads.'},
}

klar(DATEI, KLAR)


if __name__ == '__main__':
    schreibe(DATEI)
