#!/usr/bin/env python3
"""Thema stochastik.kombinatorik – Zählen und Kombinatorik (Klasse 5): systematisch zählen, Zählprinzip, Reihenfolgen,
Baumdiagramm, Bedingungen und Grenzen des Zählprinzips."""
import random
import sys
from itertools import permutations, product
from math import comb, factorial, perm
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl5_rest import *  # noqa: E402,F403

R = random.Random(60)
E = eintrag_laden('stochastik.kombinatorik')

ETAPPEN = [
    {'lernziel': 'systematisch', 'titel': 'Alle Möglichkeiten systematisch finden',
     'regel': 'Damit du ⟦keine Möglichkeit vergisst⟧ und ⟦keine doppelt⟧ zählst, gehst du ⟦systematisch⟧ vor: Halte die erste Wahl fest und gehe alle zweiten Wahlen durch, dann die nächste erste Wahl. Eine ⟦Tabelle⟧ hilft.',
     'schritte': ['2 Hosen (blau, schwarz) und 3 T-Shirts (rot, weiß, grün). Blaue Hose: mit rot, weiß, grün – 3 Möglichkeiten.', 'Schwarze Hose: wieder 3. Zusammen ⟦6 Outfits⟧.'],
     'bild': {'typ': 'tabelle', 'kopf': ['', 'rot', 'weiß', 'grün'], 'zeilen': [['blau', 'blau-rot', 'blau-weiß', 'blau-grün'], ['schwarz', 'schwarz-rot', 'schwarz-weiß', 'schwarz-grün']]},
     'fehler': '2 + 3 = 5 Outfits ist falsch: Zu ⟦jeder⟧ Hose passen alle 3 T-Shirts. Es wird ⟦malgenommen⟧: 2 · 3 = 6.'},
    {'lernziel': 'zaehlprinzip', 'titel': 'Das Zählprinzip',
     'regel': 'Wird in ⟦mehreren Schritten⟧ gewählt und gibt es in jedem Schritt eine ⟦feste Anzahl⟧ an Möglichkeiten, ist die Gesamtzahl das ⟦Produkt⟧ dieser Anzahlen (⟦Zählprinzip⟧).',
     'schritte': ['Menü: 3 Vorspeisen, 4 Hauptspeisen, 2 Nachspeisen.', 'Zählprinzip: 3 · 4 · 2 = ⟦24 Menüs⟧.'],
     'fehler': '3 + 4 + 2 = 9 Menüs ist falsch: Jedes Menü besteht aus ⟦einer Vorspeise UND einer Hauptspeise UND einer Nachspeise⟧. Bei „und nacheinander“ wird malgenommen.'},
    {'lernziel': 'reihenfolgen', 'titel': 'Reihenfolgen ohne Wiederholung',
     'regel': 'Werden Personen oder Dinge ⟦der Reihe nach⟧ angeordnet und jedes darf nur ⟦einmal⟧ vorkommen, wird die Auswahl in jedem Schritt um ⟦eins kleiner⟧: Für 4 Plätze bei 4 Kindern gibt es 4 · 3 · 2 · 1 Möglichkeiten.',
     'schritte': ['Platz 1, 2, 3 bei einem Lauf mit 6 Kindern. Platz 1: 6 Möglichkeiten, Platz 2: noch 5, Platz 3: noch 4.', '6 · 5 · 4 = ⟦120⟧ mögliche Siegerpodeste.'],
     'fehler': '6 · 6 · 6 ist falsch: Ein Kind kann nicht gleichzeitig Erster und Zweiter sein. Nach jeder Wahl gibt es ⟦eine Möglichkeit weniger⟧.'},
    {'lernziel': 'baumdiagramm', 'titel': 'Mit dem Baumdiagramm zählen',
     'regel': 'Im ⟦Baumdiagramm⟧ steht jede Stufe für einen Schritt; von jedem Punkt gehen so viele ⟦Äste⟧ ab, wie es Möglichkeiten gibt. Jeder ⟦Pfad⟧ vom Anfang bis zum Ende ist ein Ergebnis. Die Anzahl der Pfade ist die Anzahl der Möglichkeiten.',
     'schritte': ['Eine Münze wird dreimal geworfen (K = Kopf, Z = Zahl). Jede Stufe hat 2 Äste.', 'Pfade: 2 · 2 · 2 = 8. Genau zweimal Kopf: KKZ, KZK, ZKK – das sind ⟦3⟧ Pfade.'],
     'fehler': 'Bei „genau zweimal Kopf“ nur KKZ zu zählen ist falsch: Die Reihenfolge der Würfe macht ⟦verschiedene Pfade⟧ – auch KZK und ZKK gehören dazu.'},
    {'lernziel': 'bedingungen', 'titel': 'Zählen mit Bedingungen',
     'regel': 'Gibt es Bedingungen, überlegst du für ⟦jeden Schritt⟧, wie viele Möglichkeiten ⟦übrig bleiben⟧. Beginne mit dem Schritt, der die ⟦stärkste Einschränkung⟧ hat (z. B. „die erste Ziffer darf nicht 0 sein“).',
     'schritte': ['Dreistellige Zahlen aus den Ziffern 0, 1, …, 9 (Wiederholung erlaubt): Hunderter darf nicht 0 sein – 9 Möglichkeiten.', 'Zehner und Einer: je 10. Zusammen 9 · 10 · 10 = ⟦900⟧ dreistellige Zahlen.'],
     'fehler': '10 · 10 · 10 = 1 000 ist falsch: Zahlen wie 047 sind keine dreistelligen Zahlen. Die ⟦erste Stelle⟧ hat nur 9 Möglichkeiten.'},
    {'lernziel': 'grenzen', 'titel': 'Wann passt das Zählprinzip?',
     'regel': 'Das Zählprinzip zählt ⟦geordnete⟧ Auswahlen. Ist die ⟦Reihenfolge egal⟧ (Händeschütteln, Paare bilden), zählt es jede Möglichkeit ⟦doppelt⟧ – dann musst du ⟦durch 2 teilen⟧ oder systematisch auflisten.',
     'schritte': ['5 Kinder geben sich gegenseitig die Hand. Jedes Kind gibt 4 anderen die Hand: 5 · 4 = 20.', 'Dabei ist jeder Handschlag doppelt gezählt (A–B und B–A): 20 : 2 = ⟦10 Handschläge⟧.'],
     'fehler': '5 · 4 = 20 Handschläge ist falsch: A gibt B die Hand ist ⟦derselbe⟧ Handschlag wie B gibt A die Hand. Hier ist die Reihenfolge egal – also durch 2.'},
    {'lernziel': 'verstehen', 'titel': 'Zählaussagen prüfen',
     'regel': 'Prüfe Zählaussagen, indem du fragst: ⟦Und⟧ (nacheinander wählen → mal) oder ⟦oder⟧ (eins von beiden → plus)? ⟦Wiederholung⟧ erlaubt? ⟦Reihenfolge⟧ wichtig? Kleine Fälle kannst du ⟦auflisten⟧.',
     'schritte': ['Aussage: „Mit den Ziffern 1, 2, 3 kann man 9 verschiedene zweistellige Zahlen ohne doppelte Ziffer bilden.“', 'Ohne Wiederholung: 3 · 2 = 6 (12, 13, 21, 23, 31, 32). Die Aussage ist ⟦falsch⟧.'],
     'fehler': 'Nicht auf ⟦Wiederholung⟧ zu achten führt zu falschen Zahlen: Mit Wiederholung wären es 3 · 3 = 9, ohne nur 3 · 2 = 6.'},
]

PRUEFUNG = pruefung_erklaerungen(ETAPPEN, 'stochastik.kombinatorik')   # baumdiagramm: Bild (Münze dreimal)

MERKE = ['Systematisch zählen: erste Wahl festhalten, alle zweiten durchgehen.', 'Zählprinzip: Anzahlen der Schritte malnehmen.',
         'Ohne Wiederholung: in jedem Schritt eine Möglichkeit weniger.', 'Baumdiagramm: Anzahl der Pfade = Anzahl der Möglichkeiten.',
         'Reihenfolge egal (Händeschütteln): Zählprinzip zählt doppelt – durch 2 teilen.']

KLEID = [('Hosen', 'T-Shirts'), ('Röcke', 'Blusen'), ('Mützen', 'Schals'), ('Brotsorten', 'Beläge'), ('Eissorten', 'Waffeln'), ('Fahrradrahmen', 'Lenkerfarben')]
# Prüfung: Tabellenköpfe passend zum Sachkontext
DATIV = {'Beläge': 'Belägen'}
KONTEXT = [('Hosen', ['Jeans', 'Stoffhose', 'Shorts', 'Jogginghose'], 'T-Shirts', ['rot', 'blau', 'grün', 'gelb'], 'Wie viele verschiedene Outfits aus einer Hose und einem T-Shirt gibt es?'),
           ('Röcke', ['Jeansrock', 'Faltenrock', 'Minirock', 'Wickelrock'], 'Blusen', ['weiß', 'blau', 'gestreift', 'rosa'], 'Wie viele verschiedene Outfits aus einem Rock und einer Bluse gibt es?'),
           ('Mützen', ['Wollmütze', 'Kappe', 'Bommelmütze', 'Beanie'], 'Schals', ['rot', 'grau', 'bunt', 'schwarz'], 'Wie viele verschiedene Kombinationen aus einer Mütze und einem Schal gibt es?'),
           ('Brotsorten', ['Vollkorn', 'Weißbrot', 'Roggen', 'Dinkel'], 'Beläge', ['Käse', 'Wurst', 'Gurke', 'Ei'], 'Wie viele verschiedene belegte Brote mit genau einem Belag gibt es?'),
           ('Eissorten', ['Vanille', 'Schoko', 'Erdbeere', 'Zitrone'], 'Toppings', ['Sahne', 'Streusel', 'Soße', 'Nüsse'], 'Wie viele verschiedene Becher mit einer Kugel und einem Topping gibt es?'),
           ('Rahmenfarben', ['rot', 'blau', 'schwarz', 'weiß'], 'Lenkerfarben', ['silber', 'schwarz', 'gelb', 'grün'], 'Wie viele verschiedene Fahrräder aus Rahmenfarbe und Lenkerfarbe gibt es?')]
FARBEN = ['rot', 'blau', 'grün', 'gelb', 'weiß', 'schwarz']


# ---------- 1 Systematisch ----------
def g_sys(st):
    if st == 1:
        a, b = R.randint(2, 4), R.randint(2, 4)
        x, xs, y, ys, frage = R.choice(KONTEXT)
        fa, fb = xs[:a], ys[:b]
        tab = {'typ': 'tabelle', 'kopf': [''] + fb, 'zeilen': [[f] + ['?'] * b for f in fa]}
        return {'y': 'zahl', 'f': {'text': f'Es gibt {a} {x} ({", ".join(fa)}) und {b} {y} ({", ".join(fb)}). {frage} Die Tabelle hilft.', 'grafik': tab},
                'o': {'wert': a * b}, 'c': f'{a} * {b}', 'w': f'Jede der {a} Möglichkeiten ({x}) lässt sich mit allen {b} {DATIV.get(y, y)} kombinieren: {a} · {b} = {a * b}.', 'h': 'Jede Zeile der Tabelle hat gleich viele Felder.'}
    if st == 2 and R.random() < .35:          # Liste vervollständigen (Prüfung)
        if R.random() < .5:
            z = sorted(R.sample(range(1, 10), 3))
            alle = [10 * a + b for a, b in permutations(z, 2)]
            fehlt = R.choice(alle)
            liste = [v for v in alle if v != fehlt]
            f = [11 * z[0] if 11 * z[0] not in alle else 11 * z[1], 10 * fehlt % 100 + fehlt // 10 if fehlt % 10 != fehlt // 10 and (10 * (fehlt % 10) + fehlt // 10) not in liste else 10 * z[2] + z[2]]
            f = [str(v) for v in f] + [str(10 * z[0] + (set(range(1, 10)) - set(z)).pop())]
            return {**wahl_rund(R, str(fehlt), f), 'f': {'text': f'Jemand schreibt alle zweistelligen Zahlen aus den Ziffern {", ".join(map(str, z))} ohne doppelte Ziffer auf: {", ".join(map(str, liste))}. Welche Zahl fehlt?'},
                    'w': f'Systematisch: Zehner {z[0]}: {10 * z[0] + z[1]}, {10 * z[0] + z[2]}. Zehner {z[1]}: {10 * z[1] + z[0]}, {10 * z[1] + z[2]}. Zehner {z[2]}: {10 * z[2] + z[0]}, {10 * z[2] + z[1]}. Es fehlt {fehlt}.',
                    'h': 'Schreibe die Liste geordnet nach der Zehnerziffer auf.'}
        hosen, shirts = ['J', 'S', 'K'][:R.choice([2, 3])], ['r', 'g', 'b']
        alle = [h + t for h in hosen for t in shirts]
        fehlt = R.choice(alle)
        liste = [v for v in alle if v != fehlt]
        f = [fehlt[1] + fehlt[0], fehlt[0] + fehlt[0], 'Es fehlt keins.']
        return {**wahl_rund(R, fehlt, f), 'f': {'text': f'Outfits aus den Hosen {", ".join(hosen)} und den T-Shirts r, g, b werden aufgeschrieben (erst Hose, dann T-Shirt): {", ".join(liste)}. Welches Outfit fehlt?'},
                'w': 'Systematisch: ' + '; '.join(', '.join(h + t for t in shirts) for h in hosen) + f'. Das sind {len(alle)}, aufgeschrieben sind {len(liste)}. Es fehlt {fehlt}.',
                'h': 'Halte die Hose fest und gehe alle T-Shirts durch.'}
    if st == 2:
        z = R.sample(range(1, 10), R.randint(3, 4))
        wied = R.random() < .5
        n = len(z) ** 2 if wied else len(z) * (len(z) - 1)
        zs = ', '.join(map(str, sorted(z)))
        return {'y': 'zahl', 'f': {'text': f'Wie viele zweistellige Zahlen kann man aus den Ziffern {zs} bilden, wenn jede Ziffer {"mehrmals vorkommen darf" if wied else "höchstens einmal vorkommen darf"}?'},
                'o': {'wert': n}, 'c': f'{len(z)} * {len(z) if wied else len(z) - 1}',
                'w': f'Zehnerziffer: {len(z)} Möglichkeiten, Einerziffer: {len(z) if wied else len(z) - 1}. ' + (f'{len(z)} · {len(z)} = {n}.' if wied else f'{len(z)} · {len(z) - 1} = {n}.'),
                'h': 'Halte die Zehnerziffer fest und schreibe alle passenden Einerziffern auf.'}
    art = R.randrange(2)
    if art == 0:
        z = sorted(R.sample(range(1, 10), 3))
        ziel = R.choice(['größer als 50', 'gerade', 'durch 5 teilbar' if 5 in z else 'ungerade'])
        alle = [10 * a + b for a, b in permutations(z, 2)]
        if ziel == 'größer als 50': k = [v for v in alle if v > 50]
        elif ziel == 'gerade': k = [v for v in alle if v % 2 == 0]
        elif ziel == 'ungerade': k = [v for v in alle if v % 2]
        else: k = [v for v in alle if v % 5 == 0]
        return {'y': 'zahl', 'f': {'text': f'Bilde aus den Ziffern {", ".join(map(str, z))} alle zweistelligen Zahlen ohne doppelte Ziffer. Wie viele davon sind {ziel}?'},
                'o': {'wert': len(k)}, 'c': ' + '.join(['1'] * len(k)) if k else '0', 'w': 'Alle: ' + ', '.join(map(str, alle)) + f'. {ziel[0].upper() + ziel[1:]}: ' + (', '.join(map(str, k)) or 'keine') + f' – also {len(k)}.',
                'h': 'Schreibe zuerst alle Zahlen systematisch auf und streiche die unpassenden.'}
    a, b, c = R.randint(2, 3), R.randint(2, 3), R.randint(2, 3)
    return {'y': 'zahl', 'f': {'text': f'Beim Eis gibt es {a} Sorten, {b} Soßen und {c} Streusel. Ein Becher hat genau eine Sorte, eine Soße und einen Streusel. Wie viele verschiedene Becher gibt es?'},
            'o': {'wert': a * b * c}, 'c': f'{a} * {b} * {c}', 'w': f'{a} · {b} = {a * b} Paare aus Sorte und Soße, jedes mit {c} Streuseln: {a * b * c}.', 'h': 'Erst Sorte und Soße kombinieren, dann jeweils alle Streusel.'}


# ---------- 2 Zählprinzip ----------
def g_zp(st):
    if st == 1:
        a, b, c = R.randint(2, 5), R.randint(2, 6), R.randint(2, 4)
        return {'y': 'zahl', 'f': {'text': f'Eine Kantine bietet {a} Vorspeisen, {b} Hauptspeisen und {c} Nachspeisen an. Wie viele verschiedene Menüs aus je einem Gang gibt es?'},
                'o': {'wert': a * b * c}, 'c': f'{a} * {b} * {c}', 'w': f'Zählprinzip: {a} · {b} · {c} = {a * b * c}.', 'h': 'Nimm die Anzahlen der einzelnen Schritte mal.'}
    if st == 2:
        art = R.randrange(4)
        if art == 3:
            a, b, c = R.randint(2, 5), R.randint(2, 4), R.randint(2, 4)
            return {'y': 'zahl', 'f': {'text': f'Ein Kind hat {a} Mützen, {b} Schals und {c} Paar Handschuhe. Wie viele verschiedene Kombinationen aus je einem Teil kann es anziehen?'},
                    'o': {'wert': a * b * c}, 'c': f'{a} * {b} * {c}', 'w': f'Zählprinzip: {a} · {b} · {c} = {a * b * c}.', 'h': 'Mütze UND Schal UND Handschuhe: malnehmen.'}
        if art == 0:
            k = R.randint(2, 4)
            return {'y': 'zahl', 'f': {'text': f'Ein Zahlenschloss hat {k} Rädchen mit den Ziffern 0 bis 9. Wie viele Codes gibt es?'}, 'o': {'wert': 10 ** k}, 'c': f'10 ** {k}',
                    'w': f'Jedes Rädchen: 10 Möglichkeiten. {" · ".join(["10"] * k)} = {zt(10 ** k)}.', 'h': 'Jedes Rädchen kann jede Ziffer zeigen – auch doppelt.'}
        if art == 1:
            n = R.randint(2, 6)
            return {'y': 'zahl', 'f': {'text': f'Eine Münze wird {n}-mal geworfen. Wie viele verschiedene Ergebnisfolgen (Kopf/Zahl) gibt es?'}, 'o': {'wert': 2 ** n}, 'c': f'2 ** {n}',
                    'w': f'Jeder Wurf 2 Möglichkeiten: 2{hoch(n)} = {2 ** n}.', 'h': 'Bei jedem Wurf gibt es 2 Möglichkeiten.'}
        n = R.randint(2, 3)
        return {'y': 'zahl', 'f': {'text': f'Ein Würfel wird {n}-mal geworfen. Wie viele verschiedene Ergebnisfolgen gibt es?'}, 'o': {'wert': 6 ** n}, 'c': f'6 ** {n}',
                'w': f'Jeder Wurf 6 Möglichkeiten: {" · ".join(["6"] * n)} = {6 ** n}.', 'h': 'Bei jedem Wurf gibt es 6 Möglichkeiten.'}
    art = R.randrange(4)
    if art == 3:          # Umkehraufgaben (Prüfung)
        if R.random() < .5:
            h, t = R.randint(2, 6), R.randint(3, 8)
            return {'y': 'zahl', 'f': {'text': f'Ein Kind hat {h} Hosen und kann {h * t} verschiedene Outfits aus Hose und T-Shirt bilden. Wie viele T-Shirts hat es?'}, 'o': {'wert': t},
                    'c': f'{h * t} / {h}', 'w': f'{h} · T-Shirts = {h * t}, also T-Shirts = {h * t} : {h} = {t}.', 'h': 'Rückwärts rechnen: Gesamtzahl durch die bekannte Anzahl teilen.'}
        k, m = R.choice([(3, 10), (4, 10), (2, 10), (3, 6), (4, 2), (5, 2)])
        art_ = 'Ziffern 0 bis 9' if m == 10 else ('Ziffern 1 bis 6' if m == 6 else 'nur 0 und 1')
        return {'y': 'zahl', 'f': {'text': f'Ein Schloss hat Rädchen mit den {art_}. Es gibt {zt(m ** k)} verschiedene Codes. Wie viele Rädchen hat es?'}, 'o': {'wert': k},
                'c': f'{k}', 'w': f'Jedes Rädchen: {m} Möglichkeiten. ' + ' · '.join([str(m)] * k) + f' = {zt(m ** k)}, also {k} Rädchen.',
                'h': f'Nimm {m} so oft mal sich selbst, bis {zt(m ** k)} herauskommt.'}
    if art == 0:
        b, z = R.randint(1, 2), R.randint(2, 3)
        return {'y': 'zahl', 'f': {'text': f'Ein Vereinsausweis hat einen Code aus {b} Großbuchstaben (A bis Z, 26 Stück) und danach {z} Ziffern (0 bis 9). Wie viele Codes gibt es?'},
                'o': {'wert': 26 ** b * 10 ** z}, 'c': f'26 ** {b} * 10 ** {z}', 'w': f'{" · ".join(["26"] * b)} · {" · ".join(["10"] * z)} = {zt(26 ** b * 10 ** z)}.', 'h': 'Jede Stelle einzeln: Buchstaben 26, Ziffern 10.'}
    if art == 1:
        a, b = R.randint(2, 5), R.randint(2, 5)
        ges = a * b * R.randint(2, 4)
        c = ges // (a * b)
        return {'y': 'zahl', 'f': {'text': f'Es gibt {a} Hosen, {b} Pullover und einige Mützen. Insgesamt sind {ges} verschiedene Outfits aus je einem Teil möglich. Wie viele Mützen gibt es?'},
                'o': {'wert': c}, 'c': f'{ges} / ({a} * {b})', 'w': f'{a} · {b} · Mützen = {ges}, also Mützen = {ges} : {a * b} = {c}.', 'h': 'Rückwärts rechnen: Gesamtzahl durch die bekannten Anzahlen teilen.'}
    a, b = R.randint(3, 6), R.randint(3, 6)
    return {'y': 'zahl', 'f': {'text': f'Von A nach B führen {a} Wege, von B nach C {b} Wege. Jemand geht von A über B nach C und danach über B zurück nach A; dabei darf er jeden Weg beliebig wählen, auch denselben. Wie viele verschiedene Touren gibt es?'},
            'o': {'wert': (a * b) ** 2}, 'c': f'{a} * {b} * {b} * {a}', 'w': f'Hin: {a} · {b} = {a * b}. Zurück ebenso {a * b}. Zusammen {a * b} · {a * b} = {(a * b) ** 2}.', 'h': 'Hinweg und Rückweg sind zwei weitere Schritte.'}


# ---------- 3 Reihenfolgen ----------
def g_rf(st):
    if st == 1:
        n = R.randint(3, 5)
        kontext = R.choice(['{n} Kinder stellen sich in einer Reihe auf.', '{n} verschiedene Bücher werden nebeneinander ins Regal gestellt.',
                            '{n} Freunde setzen sich auf {n} Stühle in einer Reihe.', '{n} verschiedene Fotos werden nebeneinander an die Wand gehängt.'])
        return {'y': 'zahl', 'f': {'text': kontext.format(n=n) + ' Wie viele verschiedene Reihenfolgen gibt es?'}, 'o': {'wert': factorial(n)}, 'c': ' * '.join(str(i) for i in range(n, 0, -1)),
                'w': f'Für den 1. Platz {n}, dann jeweils eins weniger: {" · ".join(str(i) for i in range(n, 0, -1))} = {factorial(n)}.', 'h': 'Platz 1: alle, Platz 2: eins weniger …'}
    if st == 2:
        n, k = R.randint(5, 10), R.choice([2, 3])
        t = R.choice([('Bei einem Lauf starten {n} Kinder. Wie viele Möglichkeiten gibt es für die ersten {k} Plätze?', 'Plätze'),
                      ('Aus {n} Kindern werden {k} für die Ämter Klassensprecher{z} gewählt (jedes Kind höchstens ein Amt). Wie viele Möglichkeiten gibt es?', 'Ämter')])
        z = ', Stellvertreter und Kassenwart' if k == 3 else ' und Stellvertreter'
        return {'y': 'zahl', 'f': {'text': t[0].format(n=n, k=k, z=z)}, 'o': {'wert': perm(n, k)}, 'c': ' * '.join(str(n - i) for i in range(k)),
                'w': f'Erste Wahl {n}, dann jeweils eins weniger: {" · ".join(str(n - i) for i in range(k))} = {perm(n, k)}.', 'h': 'Nach jeder Wahl bleibt ein Kind weniger übrig.'}
    art = R.randrange(2)
    if art == 0:
        w = R.choice(['MAUS', 'BROT', 'HUND', 'BLAU', 'KATZE'])
        n = len(w)
        return {'y': 'zahl', 'f': {'text': f'Wie viele verschiedene „Wörter“ (auch sinnlose) kann man aus den Buchstaben von {w} bilden, wenn jeder Buchstabe genau einmal verwendet wird?'},
                'o': {'wert': factorial(n)}, 'c': ' * '.join(str(i) for i in range(n, 0, -1)), 'w': f'{n} verschiedene Buchstaben: {" · ".join(str(i) for i in range(n, 0, -1))} = {factorial(n)}.',
                'h': 'Alle Buchstaben sind verschieden. Wie viele Möglichkeiten für die erste Stelle, die zweite …?'}
    n = R.randint(4, 6)
    return {'y': 'zahl', 'f': {'text': f'{n} Kinder setzen sich auf {n} Stühle in einer Reihe. Ein bestimmtes Kind will unbedingt ganz links sitzen. Wie viele Sitzordnungen gibt es dann?'},
            'o': {'wert': factorial(n - 1)}, 'c': ' * '.join(str(i) for i in range(n - 1, 0, -1)), 'w': f'Der linke Platz ist fest. Die anderen {n - 1} Kinder: {" · ".join(str(i) for i in range(n - 1, 0, -1))} = {factorial(n - 1)}.',
            'h': 'Ein Platz ist schon vergeben. Ordne nur noch die anderen.'}


# ---------- 4 Baumdiagramm ----------
def baum(stufen):
    """Baumdiagramm aus einer Liste von Stufen (jede Stufe: Liste der Asttexte)."""
    def teil(i):
        if i == len(stufen): return None
        return [{'text': t, **({'aeste': teil(i + 1)} if i + 1 < len(stufen) else {})} for t in stufen[i]]
    return {'typ': 'baum', 'aeste': teil(0)}


def g_baum(st):
    if st == 1:
        if R.random() < .5:          # Pfade am Bild ablesen (Prüfung)
            s1, s2 = R.choice([(['Vanille', 'Schoko'], ['Waffel', 'Becher', 'Tüte']), (['Vanille', 'Schoko', 'Erdbeere'], ['Waffel', 'Becher']),
                               (['Bus', 'Rad'], ['Weg A', 'Weg B', 'Weg C']), (['Nudeln', 'Reis'], ['Soße 1', 'Soße 2', 'Soße 3', 'Soße 4'])])
            if R.random() < .5:
                return {'y': 'zahl', 'f': {'text': 'Wie viele Pfade hat das Baumdiagramm?', 'grafik': baum([s1, s2])}, 'o': {'wert': len(s1) * len(s2)}, 'c': f'{len(s1)} * {len(s2)}',
                        'w': f'{len(s1)} Äste auf der ersten Stufe, an jedem {len(s2)} weitere: {len(s1)} · {len(s2)} = {len(s1) * len(s2)} Pfade.', 'h': 'Zähle die Enden ganz rechts.'}
            x = R.choice(s1)
            return {'y': 'zahl', 'f': {'text': f'Bei wie vielen Pfaden ist „{x}“ dabei?', 'grafik': baum([s1, s2])}, 'o': {'wert': len(s2)}, 'c': f'{len(s2)}',
                    'w': f'Am Ast „{x}“ hängen {len(s2)} weitere Äste: {len(s2)} Pfade.', 'h': f'Folge dem Ast „{x}“ und zähle seine Enden.'}
        a, b = R.randint(2, 4), R.randint(2, 4)
        fr = {'text': f'Ein Baumdiagramm hat zwei Stufen. Auf der ersten Stufe gibt es {a} Äste, an jedem Ende gehen {b} Äste weiter. Wie viele Pfade hat das Baumdiagramm?'}
        if a * b <= 8: fr['grafik'] = baum([[str(i + 1) for i in range(a)], [chr(97 + j) for j in range(b)]])
        return {'y': 'zahl', 'f': fr,
                'o': {'wert': a * b}, 'c': f'{a} * {b}', 'w': f'Jeder der {a} Äste verzweigt sich in {b}: {a} · {b} = {a * b} Pfade.', 'h': 'Zähle die Enden der zweiten Stufe.'}
    if st == 2 and R.random() < .6:
        m = R.randint(3, 5)
        farben = ['rote', 'blaue', 'grüne', 'gelbe', 'weiße'][:m]
        zur = R.random() < .5
        frage = R.choice(['alle', 'gleich'])
        if frage == 'alle':
            r = m * m if zur else m * (m - 1)
            fr = {'text': f'In einer Dose liegen {m} Kugeln: ' + ', '.join(f'eine {f}' for f in farben) + f'. Es wird zweimal gezogen, {"mit" if zur else "ohne"} Zurücklegen. Wie viele Pfade hat das Baumdiagramm?'}
            if r <= 9 and not zur: fr['grafik'] = {'typ': 'baum', 'aeste': [{'text': f[:-1], 'aeste': [{'text': g[:-1]} for g in farben if g != f]} for f in farben]}
            elif r <= 9: fr['grafik'] = {'typ': 'baum', 'aeste': [{'text': f[:-1], 'aeste': [{'text': g[:-1]} for g in farben]} for f in farben]}
            return {'y': 'zahl', 'f': fr,
                    'o': {'wert': r}, 'c': f'{m} * {m if zur else m - 1}', 'w': f'Stufe 1: {m} Äste, Stufe 2: {m if zur else m - 1} Äste. {m} · {m if zur else m - 1} = {r} Pfade.',
                    'h': 'Mit Zurücklegen ist beim zweiten Zug wieder alles da, ohne Zurücklegen eine Kugel weniger.'}
        r = m if zur else 0
        return {'y': 'zahl', 'f': {'text': f'In einer Dose liegen {m} Kugeln: ' + ', '.join(f'eine {f}' for f in farben) + f'. Es wird zweimal gezogen, {"mit" if zur else "ohne"} Zurücklegen. Bei wie vielen Pfaden haben beide Kugeln dieselbe Farbe?'},
                'o': {'wert': r}, 'c': f'{r}', 'w': (f'Mit Zurücklegen: jede der {m} Farben kann zweimal kommen – {m} Pfade.' if zur else 'Ohne Zurücklegen ist jede Farbe nur einmal da – kein Pfad.'),
                'h': 'Kann dieselbe Kugel zweimal gezogen werden?'}
    if st == 2:
        n = R.randint(3, 4)
        k = R.randint(1, n - 1)
        r = comb(n, k)
        fr = {'text': f'Eine Münze wird {n}-mal geworfen. Wie viele Pfade im Baumdiagramm enthalten genau {k}-mal Kopf?'}
        if n == 3: fr['grafik'] = baum([['K', 'Z']] * 3)
        return {'y': 'zahl', 'f': fr, 'o': {'wert': r},
                'c': ' + '.join(['1'] * r), 'w': 'Pfade: ' + ', '.join(''.join(p) for p in product('KZ', repeat=n) if p.count('K') == k) + f' – also {r}.',
                'h': 'Schreibe alle Pfade auf (KKZ, KZK …) und zähle die passenden.'}
    art = R.randrange(2)
    if art == 0:
        n = 3
        bed = R.choice([('mindestens einmal Kopf', lambda p: 'K' in p), ('höchstens einmal Kopf', lambda p: p.count('K') <= 1), ('mindestens zweimal hintereinander dasselbe Ergebnis', lambda p: any(p[i] == p[i + 1] for i in range(n - 1)))])
        ps = [''.join(p) for p in product('KZ', repeat=n) if bed[1](''.join(p))]
        return {'y': 'zahl', 'f': {'text': f'Eine Münze wird dreimal geworfen. Wie viele der 8 Pfade erfüllen: {bed[0]}?'}, 'o': {'wert': len(ps)}, 'c': ' + '.join(['1'] * len(ps)),
                'w': 'Passend: ' + ', '.join(ps) + f'. Das sind {len(ps)}.', 'h': 'Schreibe alle 8 Pfade auf: KKK, KKZ, KZK, …'}
    z = R.choice([4, 5, 6])
    ps = [(a, b) for a in range(1, 7) for b in range(1, 7) if a + b == z]
    return {'y': 'zahl', 'f': {'text': f'Zwei Würfel werden nacheinander geworfen. Bei wie vielen der 36 Pfade ist die Augensumme {z}?'}, 'o': {'wert': len(ps)}, 'c': ' + '.join(['1'] * len(ps)),
            'w': 'Paare (1. Wurf, 2. Wurf): ' + ', '.join(f'({a}, {b})' for a, b in ps) + f' – {len(ps)} Pfade.', 'h': 'Gehe den ersten Wurf von 1 bis 6 durch und überlege, was der zweite zeigen muss.'}


# ---------- 5 Bedingungen ----------
BED = {'gerade': 0}


def _null_ziffer():
    """Ziffer 0 in der Auswahl (Prüfung)."""
    z = sorted([0] + R.sample(range(1, 10), 3))
    alle = [100 * a + 10 * b + c for a, b, c in permutations(z, 3) if a != 0]
    if R.random() < .5:
        return {'y': 'zahl', 'f': {'text': f'Aus den Ziffern {", ".join(map(str, z))} werden dreistellige Zahlen ohne doppelte Ziffer gebildet. Wie viele gibt es?'}, 'o': {'wert': len(alle)},
                'c': '3 * 3 * 2', 'w': f'Hunderter: 3 Möglichkeiten (nicht 0). Zehner: wieder 3 (die 0 ist jetzt erlaubt, die benutzte Ziffer nicht). Einer: 2. 3 · 3 · 2 = {len(alle)}.',
                'h': 'Die 0 darf nicht vorne stehen. Beginne mit der Hunderterziffer.'}
    ger = [v for v in alle if v % 2 == 0]
    mit0 = len([v for v in ger if v % 10 == 0])
    return {'y': 'zahl', 'f': {'text': f'Aus den Ziffern {", ".join(map(str, z))} werden dreistellige Zahlen ohne doppelte Ziffer gebildet. Wie viele davon sind gerade?'}, 'o': {'wert': len(ger)},
            'c': f'{mit0} + {len(ger) - mit0}', 'w': f'Endziffer 0: vorne und in der Mitte die drei anderen Ziffern, 3 · 2 = {mit0}. ' + (f'Andere gerade Endziffern ({", ".join(str(d) for d in z if d and d % 2 == 0)}): je 2 · 2 = 4, vorne keine 0. ' if len(ger) > mit0 else 'Keine andere gerade Ziffer. ') + f'Zusammen {len(ger)}.',
            'h': 'Unterscheide: Endziffer 0 oder eine andere gerade Endziffer.'}


def g_bed(st):
    if st == 1 and R.random() < .6:
        k, d = R.choice([3, 4]), R.randint(0, 9)
        wort = 'drei' if k == 3 else 'vier'
        return {'y': 'zahl', 'f': {'text': f'Wie viele {wort}stellige Zahlen enden mit der Ziffer {d}? (Die erste Ziffer ist nicht 0.)'}, 'o': {'wert': 9 * 10 ** (k - 2)},
                'c': f'9 * 10 ** {k - 2} * 1', 'w': f'Erste Ziffer 9 Möglichkeiten, mittlere je 10, letzte nur 1 (die {d}): 9 · {" · ".join(["10"] * (k - 2))} · 1 = {zt(9 * 10 ** (k - 2))}.',
                'h': 'Die letzte Stelle ist festgelegt – dort gibt es nur eine Möglichkeit.'}
    if st == 1:
        k = R.choice([2, 3, 4])
        return {'y': 'zahl', 'f': {'text': f'Wie viele {"zwei" if k == 2 else "drei" if k == 3 else "vier"}stellige Zahlen gibt es? (Ziffern 0 bis 9, Wiederholung erlaubt, die erste Ziffer ist nicht 0.)'},
                'o': {'wert': 9 * 10 ** (k - 1)}, 'c': f'9 * 10 ** {k - 1}', 'w': f'Erste Ziffer 9 Möglichkeiten, jede weitere 10: 9 · {" · ".join(["10"] * (k - 1))} = {zt(9 * 10 ** (k - 1))}.',
                'h': 'Die erste Ziffer darf nicht 0 sein.'}
    if st == 2:
        art = R.randrange(3)
        if art == 1 and BED['gerade'] >= 5: art = 2          # höchstens 5 „gerade dreistellige Zahlen“ (Prüfung)
        if art == 2: return _null_ziffer()
        if art == 1: BED['gerade'] += 1
        if art == 0:
            k = R.choice([2, 3])
            r = 9 * perm(9, k - 1)
            return {'y': 'zahl', 'f': {'text': f'Wie viele {"zwei" if k == 2 else "drei"}stellige Zahlen gibt es, in denen keine Ziffer doppelt vorkommt?'}, 'o': {'wert': r},
                    'c': '9 * ' + ' * '.join(str(9 - i) for i in range(k - 1)), 'w': f'Erste Ziffer: 9 (nicht 0). Dann 9, ' + ('dann 8. ' if k == 3 else '') + f'Zusammen {zt(r)}.',
                    'h': 'Erste Ziffer: keine 0. Danach ist die 0 wieder erlaubt, aber die schon benutzte Ziffer nicht.'}
        z = sorted(R.sample(range(1, 10), 4))
        ger = [d for d in z if d % 2 == 0]
        if not ger: return g_bed(2)
        r = len(ger) * 3 * 2
        return {'y': 'zahl', 'f': {'text': f'Aus den Ziffern {", ".join(map(str, z))} werden dreistellige Zahlen ohne doppelte Ziffer gebildet. Wie viele davon sind gerade?'}, 'o': {'wert': r},
                'c': f'{len(ger)} * 3 * 2', 'w': f'Gerade heißt: Einerziffer gerade ({", ".join(map(str, ger))}) – {len(ger)} Möglichkeiten. Dann Hunderter 3, Zehner 2: {len(ger)} · 3 · 2 = {r}.',
                'h': 'Beginne mit der Einerziffer – sie hat die stärkste Bedingung.'}
    art = R.randrange(3)
    if art == 2: return _null_ziffer()
    if art == 0:
        n = R.randint(4, 6)
        r = 2 * factorial(n - 1)
        return {'y': 'zahl', 'f': {'text': f'{n} Kinder stellen sich in einer Reihe auf. Zwei Geschwister wollen nebeneinander stehen. Wie viele Reihenfolgen gibt es?'}, 'o': {'wert': r},
                'c': f'2 * ' + ' * '.join(str(i) for i in range(n - 1, 0, -1)), 'w': f'Die Geschwister als ein „Block“: {n - 1} Teile, {factorial(n - 1)} Reihenfolgen. Im Block 2 Möglichkeiten: 2 · {factorial(n - 1)} = {r}.',
                'h': 'Denke dir die beiden zusammengeklebt. Wie viele Teile ordnest du dann?'}
    k = R.choice([3, 4])
    menge, m = R.choice([('nur ungerade Ziffern (1, 3, 5, 7, 9)', 5), ('nur die Ziffern 1 bis 6', 6), ('nur gerade Ziffern (0, 2, 4, 6, 8)', 5)])
    r = m ** k
    return {'y': 'zahl', 'f': {'text': f'Ein Code hat {k} Ziffern und darf {menge} enthalten, Wiederholung erlaubt. Wie viele Codes gibt es?'}, 'o': {'wert': r}, 'c': f'{m} ** {k}',
            'w': f'Jede Stelle: {m} Möglichkeiten. {" · ".join([str(m)] * k)} = {zt(r)}.', 'h': 'Wie viele Ziffern sind erlaubt? Bei einem Code darf die 0 auch vorne stehen.'}


# ---------- 6 Grenzen ----------
def g_gr(st):
    n = R.randint(3, 8)
    if st == 1:
        return {'y': 'zahl', 'f': {'text': f'{n} Kinder geben sich gegenseitig einmal die Hand. Wie viele Handschläge gibt es?'}, 'o': {'wert': comb(n, 2)}, 'c': f'{n} * {n - 1} / 2',
                'w': f'Jedes Kind gibt {n - 1} anderen die Hand: {n} · {n - 1} = {n * (n - 1)}. Jeder Handschlag doppelt gezählt: {n * (n - 1)} : 2 = {comb(n, 2)}.',
                'h': 'Zählprinzip, dann durch 2 – A–B ist derselbe Handschlag wie B–A.'}
    if st == 2:
        art = R.randrange(2)
        if art == 0:
            return {'y': 'zahl', 'f': {'text': f'Bei einem Turnier spielt jede von {n} Mannschaften genau einmal gegen jede andere. Wie viele Spiele gibt es?'}, 'o': {'wert': comb(n, 2)}, 'c': f'{n} * {n - 1} / 2',
                    'w': f'{n} · {n - 1} = {n * (n - 1)} zählt jedes Spiel doppelt. {n * (n - 1)} : 2 = {comb(n, 2)} Spiele.', 'h': 'Spiel A gegen B ist dasselbe wie B gegen A.'}
        t = R.choice([('aus {n} Kindern 2 für den Tischdienst (gleiche Aufgabe) ausgewählt', False), ('aus {n} Kindern ein Klassensprecher und ein Stellvertreter gewählt', True)])
        geordnet = t[1]
        r = 'Zählprinzip direkt: ' + str(n * (n - 1)) if geordnet else f'Zählprinzip, dann durch 2: {n * (n - 1) // 2}'
        return {**wahl(R, r, ['Zählprinzip direkt: ' + str(n * (n - 1)) if not geordnet else f'Zählprinzip, dann durch 2: {n * (n - 1) // 2}', f'Plus rechnen: {n} + {n - 1} = {2 * n - 1}']),
                'f': {'text': f'Es werden {t[0].format(n=n)}. Wie zählt man richtig?'},
                'w': ('Die Ämter sind verschieden, die Reihenfolge zählt: ' if geordnet else 'Beide machen dasselbe, die Reihenfolge ist egal: ') + r + '.', 'h': 'Ist die Reihenfolge der beiden Gewählten wichtig?'}
    art = R.randrange(2)
    if art == 0:
        return {'y': 'zahl', 'f': {'text': f'Wie viele Strecken kann man zwischen {n} Punkten zeichnen, von denen keine drei auf einer Geraden liegen?'}, 'o': {'wert': comb(n, 2)}, 'c': f'{n} * {n - 1} / 2',
                'w': f'Jeder Punkt mit {n - 1} anderen: {n} · {n - 1} = {n * (n - 1)}. Jede Strecke doppelt: {comb(n, 2)}.', 'h': 'Die Strecke [AB] ist dieselbe wie [BA].'}
    m = n * (n - 1) // 2
    if R.random() < .5:          # Turnier rückwärts (Prüfung)
        return {'y': 'zahl', 'f': {'text': f'Bei einem Turnier spielt jede Mannschaft genau einmal gegen jede andere. Es gibt {m} Spiele. Wie viele Mannschaften sind es?'}, 'o': {'wert': n},
                'c': f'{n}', 'w': f'Probieren: Bei {n} Mannschaften gibt es {n} · {n - 1} : 2 = {m} Spiele.', 'h': 'Probiere: 3 Mannschaften → 3 Spiele, 4 → 6, 5 → 10 …'}
    return {'y': 'zahl', 'f': {'text': f'Bei einer Feier gab es {m} Handschläge. Jeder hat jedem genau einmal die Hand gegeben. Wie viele Personen waren da?'}, 'o': {'wert': n},
            'c': f'{n}', 'w': f'Probieren: Bei {n} Personen gibt es {n} · {n - 1} : 2 = {m} Handschläge.', 'h': 'Probiere: 3 Personen → 3, 4 Personen → 6, 5 Personen → 10 …'}


# ---------- 7 Verstehen ----------
# Prüfung: Ablenker mit falscher Begründung
def g_vers(st):
    a, b = R.randint(2, 5), R.randint(2, 5)
    if a == b: b += 1
    if st == 1:
        aussagen = [(f'Mit {a} Hosen und {b} T-Shirts gibt es {a + b} Outfits.', f'Nein, zu jeder Hose passen alle T-Shirts: {a} · {b} = {a * b}.', [f'Ja, {a} + {b} = {a + b}.', f'Nein, jedes Teil zählt nur einmal: {max(a, b)}.']),
                    (f'Mit {a} Hosen und {b} T-Shirts gibt es {a * b} Outfits.', f'Ja, Zählprinzip: {a} · {b} = {a * b}.', [f'Nein, {a} + {b} = {a + b}.', f'Nein, jedes Teil zählt nur einmal: {max(a, b)}.']),
                    ('Eine Münze zweimal geworfen hat 4 mögliche Ergebnisfolgen.', 'Ja: KK, KZ, ZK, ZZ.', ['Nein, KZ und ZK sind dasselbe: 3 Folgen.', 'Nein, 2 + 2 = 4 ist Zufall, es sind 2 Folgen.']),
                    ('Eine Münze zweimal geworfen hat 3 mögliche Ergebnisfolgen.', 'Nein, KZ und ZK sind verschieden: 4 Folgen.', ['Ja, KZ und ZK sind dasselbe: KK, KZ, ZZ.', 'Nein, es sind 2 Folgen: Kopf oder Zahl.'])]
    elif st == 2:
        n = R.randint(3, 6)
        kette = ' · '.join(str(i) for i in range(n, 0, -1))
        aussagen = [(f'{n} Kinder können sich auf {factorial(n)} Arten in eine Reihe stellen.', f'Ja, {kette} = {factorial(n)}.', [f'Nein, {n} · {n} = {n * n}.', f'Nein, es sind {n} Arten, eine pro Kind.']),
                    (f'{n} Kinder können sich auf {n * n} Arten in eine Reihe stellen.', f'Nein, ohne Wiederholung: {kette} = {factorial(n)}.', [f'Ja, jedes Kind kann auf jedem der {n} Plätze stehen: {n} · {n}.', f'Nein, es sind {n} Arten, eine pro Kind.']),
                    (f'Bei {n} Kindern gibt es {n * (n - 1)} Handschläge, wenn jeder jedem die Hand gibt.', f'Nein, jeder Handschlag ist doppelt gezählt: {n * (n - 1)} : 2 = {n * (n - 1) // 2}.', [f'Ja, jedes Kind gibt {n - 1} anderen die Hand: {n} · {n - 1}.', f'Nein, es sind {n} Handschläge, einer pro Kind.']),
                    ('Mit den Ziffern 1, 2, 3 gibt es 6 zweistellige Zahlen ohne doppelte Ziffer.', 'Ja: 12, 13, 21, 23, 31, 32.', ['Nein, 12 und 21 sind dieselbe Zahl: 3.', 'Nein, 3 · 3 = 9.']),
                    (f'Bei {n} Kindern gibt es {n * (n - 1) // 2} Handschläge, wenn jeder jedem einmal die Hand gibt.', f'Ja, {n} · {n - 1} : 2 = {n * (n - 1) // 2}.', [f'Nein, {n} · {n - 1} = {n * (n - 1)}.', f'Nein, {n} · {n} = {n * n}.']),
                    (f'Für die Plätze 1 und 2 bei {n + 2} Läufern gibt es {(n + 2) * (n + 1)} Möglichkeiten.', f'Ja, {n + 2} · {n + 1} = {(n + 2) * (n + 1)}.', [f'Nein, {n + 2} · {n + 2} = {(n + 2) ** 2}.', f'Nein, {n + 2} + {n + 1} = {2 * n + 3}.']),
                    (f'Für die Plätze 1 und 2 bei {n + 2} Läufern gibt es {(n + 2) * (n + 2)} Möglichkeiten.', f'Nein, niemand kann beide Plätze belegen: {n + 2} · {n + 1} = {(n + 2) * (n + 1)}.', [f'Ja, für jeden Platz gibt es {n + 2} Läufer.', f'Nein, {n + 2} + {n + 1} = {2 * n + 3}.'])]
    else:
        aussagen = [('Es gibt 1 000 dreistellige Zahlen.', 'Nein, 9 · 10 · 10 = 900 (100 bis 999).', ['Ja, 10 · 10 · 10 = 1 000.', 'Nein, 9 · 9 · 9 = 729.']),
                    ('Ein Zahlenschloss mit 3 Rädchen (0–9) hat 1 000 Codes.', 'Ja, beim Schloss ist auch 0 vorne erlaubt: 10 · 10 · 10 = 1 000.', ['Nein, 9 · 10 · 10 = 900, vorne darf keine 0 stehen.', 'Nein, 10 + 10 + 10 = 30.']),
                    ('Werden zwei Würfel geworfen, gibt es 12 mögliche Paare.', 'Nein, 6 · 6 = 36 Paare.', ['Ja, 6 + 6 = 12.', 'Nein, 6 Paare, weil beide Würfel gleich sind.']),
                    ('Das Zählprinzip gilt nur, wenn in jedem Schritt gleich viele Möglichkeiten sind.', 'Nein, die Anzahlen dürfen verschieden sein (z. B. 3 · 4 · 2) – sie dürfen nur nicht vom vorigen Schritt abhängen.', ['Ja, sonst kann man nicht malnehmen.', 'Ja, sonst muss man addieren.']),
                    (f'Aus {a + 3} Eissorten 2 verschiedene Kugeln in eine Waffel (Reihenfolge egal): {(a + 3) * (a + 2) // 2} Möglichkeiten.', f'Ja, ({a + 3} · {a + 2}) : 2 = {(a + 3) * (a + 2) // 2}.', [f'Nein, {a + 3} · {a + 2} = {(a + 3) * (a + 2)}.', f'Nein, {a + 3} + {a + 2} = {2 * a + 5}.'])]
    s_, grund, f = R.choice(aussagen)
    return {**wahl_rund(R, grund, f, 3), 'f': {'text': f'Stimmt die Aussage? „{s_}“'}, 'w': grund, 'h': 'Und oder oder? Wiederholung? Reihenfolge wichtig?'}


GEN = {'systematisch': g_sys, 'zaehlprinzip': g_zp, 'reihenfolgen': g_rf, 'baumdiagramm': g_baum, 'bedingungen': g_bed, 'grenzen': g_gr, 'verstehen': g_vers}

DATEI = datei(E, 'Anzahlen systematisch, mit dem Zählprinzip und mit Baumdiagrammen bestimmen und prüfen, ob das Zählprinzip anwendbar ist.', MERKE,
              [('Systematisch zählen', ['systematisch', 'zaehlprinzip', 'reihenfolgen']),
               ('Baumdiagramm und Bedingungen', ['baumdiagramm', 'bedingungen']),
               ('Grenzen und Verstehen', ['grenzen', 'verstehen'])],
              ETAPPEN, GEN,
              offen=['Zeichnungen: Baumdiagramme (Bildtyp baum) in der Lernkarte baumdiagramm und in Aufgaben mit höchstens etwa 9 Pfaden; größere Bäume bleiben in Worten beschrieben. Kombinationstabellen als Tabelle mit passenden Zeilen- und Spaltenköpfen.',
                     'Begriffe wie Permutation, Variation, Kombination, n! und Binomialkoeffizient werden bewusst nicht eingeführt (höhere Klassen); alles läuft über Zählprinzip, Auflisten und „durch 2 teilen“.'])

# Umbau U5 (Achte Runde, Vorgabe 16.11.): Lernkarten nach dem neuen Muster – einstieg, woerter (≤ 3), Kartenbild,
# Bildergeschichte (schritte mit bild), „Pass auf!“ (fehler + fehler_bild), MERKE (regel).
# Situationen: Kleiderschrank, Restaurant-Menü, Sportfest, Münzwurf, Zahlenschloss, Händeschütteln.
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl5.py) – die Aufgaben bleiben wörtlich gleich.
import math  # noqa: E402

from _umbau_kl5 import umbau  # noqa: E402


def muenze(n, pfad=''):
    """Baumdiagramm für n Münzwürfe (K = Kopf, Z = Zahl)."""
    return [{'text': s, 'aeste': muenze(n - 1, pfad + s)} if n > 1 else {'text': s} for s in 'KZ']


def pfade(n, pfad=''):
    """Wie muenze, aber an den Blättern steht der ganze Pfad, mit ✓ bei genau zweimal K."""
    if n == 0:
        return []
    return [{'text': s, 'aeste': pfade(n - 1, pfad + s)} if n > 1 else {'text': (pfad + s) + (' ✓' if (pfad + s).count('K') == 2 else '')} for s in 'KZ']


OUTFIT = lambda z1, z2: {'zeilen': [['blau', *z1], ['schwarz', *z2]]}
MENUE = lambda h, n: {'zeilen': [['Vorspeise', '3', '3'], ['Hauptspeise', '4', h], ['Nachspeise', '2', n]]}
PLATZ = lambda *m: {'zeilen': [['1. Platz', m[0]], ['2. Platz', m[1]], ['3. Platz', m[2]]]}
STELLE = lambda h, z, e: {'zeilen': [['Hunderter', h], ['Zehner', z], ['Einer', e]]}
KINDER = {k: [round(3 * math.cos(math.radians(90 + 72 * i)), 3), round(3 * math.sin(math.radians(90 + 72 * i)), 3)] for i, k in enumerate('ABCDE')}
ZIFFERN = lambda z: {'zeilen': z}

KARTEN = {
 'systematisch': {
  'einstieg': 'Du hast 2 Hosen und 3 T-Shirts. Wie viele Kombinationen kannst du anziehen? Mit einem festen Plan vergisst du keine: Du gehst ⟦systematisch⟧ vor.',
  'woerter': [['systematisch', 'nach einem festen Plan, der Reihe nach'], ['Outfit', 'eine Hose mit einem T-Shirt']],
  'bild': {'typ': 'tabelle', 'kopf': ['Hose ↓  T-Shirt →', 'rot', 'weiß', 'grün'], 'zeilen': [['blau', '', '', ''], ['schwarz', '', '', '']]},
  'schritte': [{'text': 'Halte die blaue Hose fest: dazu rot, weiß, grün. 3 Outfits.', 'bild': OUTFIT(['✓', '✓', '✓'], ['', '', ''])},
               {'text': 'Dann die schwarze Hose: wieder 3 Outfits.', 'bild': OUTFIT(['✓', '✓', '✓'], ['✓', '✓', '✓'])},
               {'text': 'Zusammen: 3 + 3 = ⟦6 Outfits⟧.'}],
  'fehler': '2 + 3 = 5 Outfits ist falsch. Zu jeder Hose passen alle 3 T-Shirts: 2 · 3 = 6.',
  'regel': 'Erste Wahl festhalten, ⟦alle zweiten Wahlen⟧ durchgehen. Dann kommt die nächste erste Wahl dran.'},
 'zaehlprinzip': {
  'einstieg': 'Ein Restaurant hat 3 Vorspeisen, 4 Hauptspeisen und 2 Nachspeisen. Jedes passt zu jedem. Statt alle Menüs aufzuschreiben, nimmst du mal: das ⟦Zählprinzip⟧.',
  'woerter': [['Zählprinzip', 'bei Wahlen nacheinander die Anzahlen malnehmen'], ['Schritt', 'eine einzelne Wahl, zum Beispiel die Vorspeise']],
  'bild': {'typ': 'tabelle', 'kopf': ['Schritt', 'Auswahl', 'Menüs bis hier'], **MENUE('?', '?')},
  'schritte': [{'text': 'Zu jeder der 3 Vorspeisen passen 4 Hauptspeisen: 3 · 4 = 12.', 'bild': MENUE('12', '?')},
               {'text': 'Zu jedem davon passen 2 Nachspeisen: 12 · 2 = 24.', 'bild': MENUE('12', '24')},
               {'text': 'Kurz mit dem Zählprinzip, Schritt für Schritt: 3 · 4 · 2 = ⟦24 Menüs⟧.'}],
  'fehler': '3 + 4 + 2 = 9 Menüs ist falsch. Jedes Menü hat eine Vorspeise und eine Hauptspeise und eine Nachspeise.',
  'regel': 'Wahlen nacheinander: Anzahlen ⟦malnehmen⟧. Die Anzahlen dürfen in jedem Schritt verschieden sein.'},
 'reihenfolgen': {
  'einstieg': 'Beim Sportfest laufen 6 Kinder um die Wette, aufs Podest kommen drei. Wer Erster ist, kann nicht auch Zweiter sein. Das sind ⟦Reihenfolgen ohne Wiederholung⟧.',
  'woerter': [['ohne Wiederholung', 'jedes Kind darf nur einmal vorkommen'], ['Podest', 'das Siegerpodest mit den Plätzen 1, 2 und 3']],
  'bild': {'typ': 'tabelle', 'kopf': ['Platz', 'Möglichkeiten'], **PLATZ('?', '?', '?')},
  'schritte': [{'text': 'Platz 1: Alle 6 Kinder kommen infrage.', 'bild': PLATZ('6', '?', '?')},
               {'text': 'Platz 2: Der Sieger ist vergeben, es bleiben 5.', 'bild': PLATZ('6', '5', '?')},
               {'text': 'Platz 3: Es bleiben 4.', 'bild': PLATZ('6', '5', '4')},
               {'text': '6 · 5 · 4 = ⟦120⟧ mögliche Siegerpodeste.'}],
  'fehler': '6 · 6 · 6 ist falsch. Ein Kind kann nicht Erster und Zweiter zugleich sein: Jedes Mal bleibt eins weniger.',
  'regel': 'Bei jedem Platz wird die Auswahl ⟦um eins kleiner⟧. 4 Kinder auf 4 Plätzen: 4 · 3 · 2 · 1 = 24.'},
 'baumdiagramm': {
  'einstieg': 'Du wirfst eine Münze dreimal. Jedes Mal fällt Kopf oder Zahl. Zeichnest du alle Möglichkeiten als Äste, entsteht ein ⟦Baumdiagramm⟧.',
  'woerter': [['Stufe', 'ein Schritt im Baum, hier ein Wurf'], ['Pfad', 'ein ganzer Weg vom Start bis zum Ende, zum Beispiel K → Z → K']],
  'bild': {'typ': 'baum', 'aeste': muenze(1)},
  'schritte': [{'text': '1. Stufe, der erste Wurf: 2 Äste, K und Z.'},
               {'text': '2. und 3. Wurf: An jedem Ende wieder 2 Äste.', 'bild': {'aeste': muenze(3)}},
               {'text': '2 · 2 · 2 = 8 Pfade. Gesucht ist genau zweimal K.'},
               {'text': 'Das passt bei KKZ, KZK und ZKK: ⟦3⟧ Pfade.', 'bild': {'aeste': pfade(3)}}],
  'fehler': 'Bei „genau zweimal Kopf“ nur KKZ zählen ist falsch. KZK und ZKK sind andere Pfade und zählen mit.',
  'regel': 'Jeder ⟦Pfad⟧ vom Start bis zum Ende ist ein Ergebnis. Zähle die Pfade, die zur Frage passen.'},
 'bedingungen': {
  'einstieg': 'Ein Zahlenschloss hat drei Räder mit 0 bis 9. Eine echte dreistellige Zahl darf vorne aber keine 0 haben. So eine Einschränkung heißt ⟦Bedingung⟧.',
  'woerter': [['Bedingung', 'eine Vorgabe, die die Auswahl einschränkt'], ['dreistellige Zahl', 'eine Zahl von 100 bis 999']],
  'bild': {'typ': 'tabelle', 'kopf': ['Stelle', 'Möglichkeiten'], **STELLE('?', '?', '?')},
  'schritte': [{'text': 'Fang bei der Stelle mit Bedingung an: Hunderter nicht 0, also 9.', 'bild': STELLE('9', '?', '?')},
               {'text': 'Zehner und Einer: je 10 Möglichkeiten.', 'bild': STELLE('9', '10', '10')},
               {'text': '9 · 10 · 10 = ⟦900⟧ dreistellige Zahlen.'}],
  'fehler': '10 · 10 · 10 = 1 000 ist falsch. 047 ist keine dreistellige Zahl: Vorne gibt es nur 9 Möglichkeiten.',
  'regel': 'Beginne mit dem Schritt mit der ⟦stärksten Einschränkung⟧. Zähle für jeden Schritt, was übrig bleibt.'},
 'grenzen': {
  'einstieg': 'Nach dem Spiel geben sich 5 Kinder gegenseitig die Hand. Jedes schüttelt 4 Hände, aber sind das 5 · 4 = 20 Handschläge? Das Zählprinzip stößt hier an ⟦Grenzen⟧.',
  'woerter': [['Reihenfolge egal', 'A–B und B–A sind dasselbe, wie beim Händeschütteln'], ['doppelt gezählt', 'dieselbe Möglichkeit wurde zweimal mitgezählt']],
  'bild': {'typ': 'figur', 'punkte': KINDER},
  'schritte': [{'text': 'Kind A gibt 4 Kindern die Hand.', 'bild': {'linien': [['A', k] for k in 'BCDE']}},
               {'text': '5 · 4 = 20 zählt A–B und B–A. Reihenfolge egal: derselbe Handschlag.'},
               {'text': 'Jeder ist doppelt gezählt: 20 : 2 = ⟦10⟧ Handschläge.',
                'bild': {'linien': [[a, b] for i, a in enumerate('ABCDE') for b in 'ABCDE'[i + 1:]]}}],
  'fehler': '5 · 4 = 20 Handschläge ist falsch. Gibt A der B die Hand, ist das derselbe Handschlag wie B mit A.',
  'regel': 'Ist die ⟦Reihenfolge egal⟧, zählt das Zählprinzip doppelt. Dann durch 2 teilen oder alles auflisten.'},
 'verstehen': {
  'einstieg': 'Jemand sagt: Aus 1, 2 und 3 gibt es 9 zweistellige Zahlen ohne doppelte Ziffer. Ob das stimmt, hängt an „ohne doppelt“. Solche ⟦Zählaussagen⟧ prüfst du durch Auflisten.',
  'woerter': [['Zählaussage', 'eine Behauptung über eine Anzahl von Möglichkeiten'], ['auflisten', 'alle Möglichkeiten einzeln aufschreiben']],
  'bild': {'typ': 'tabelle', 'kopf': ['Zehner ↓  Einer →', '1', '2', '3'], 'zeilen': [['1', '–', '', ''], ['2', '', '–', ''], ['3', '', '', '–']]},
  'schritte': [{'text': 'Erste Stelle: 3 Möglichkeiten. Zweite Stelle: nur noch 2.'},
               {'text': 'Zählprinzip: 3 · 2 = 6.'},
               {'text': 'Auflisten bestätigt es: 12, 13, 21, 23, 31, 32.',
                'bild': ZIFFERN([['1', '–', '12', '13'], ['2', '21', '–', '23'], ['3', '31', '32', '–']])},
               {'text': '6 statt 9: Die Aussage ist ⟦falsch⟧.'}],
  'fehler': 'Nicht auf „ohne doppelt“ achten. Mit Wiederholung sind es 3 · 3 = 9. Ohne sind es nur 3 · 2 = 6.',
  'fehler_bild': ZIFFERN([['1', '11', '12', '13'], ['2', '21', '22', '23'], ['3', '31', '32', '33']]),
  'regel': 'Frag dich: ⟦Wiederholung⟧ erlaubt? Reihenfolge wichtig? Nacheinander wählen heißt mal. Kleine Fälle kannst du auflisten.'},
}
umbau(DATEI, KARTEN)


# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl5) ----------
# Neue Übungen nach Prüfungsvorbild (Jahrgangsstufentest 6 Bayern: vierstellige Zahlen aus 4 Ziffern, Melodien aus Tönen, Outfits aus
# Hosen/Gürteln/Shirts, Teilbarkeit 789□□; Mathematik-Olympiade Kl. 5: Reihenfolgen von Stationen; Känguru 5/6: Türme, Färben). Alle Anzahlen
# werden hier durch vollständiges Aufzählen berechnet. Eigene Zahlen und Einkleidung.
from itertools import combinations as _komb, permutations as _perm, product as _prod  # noqa: E402
from _schwer_kl5 import A, L, Z, de, einzig, ergaenze, wahl  # noqa: E402


def _schwer():
    N = {}
    zahlen246 = sorted((int(''.join(p)) for p in _perm('246')), reverse=True)
    N['systematisch'] = [
        Z(2, 'Aus den Ziffern 2, 4 und 6 werden alle dreistelligen Zahlen ohne doppelte Ziffer gebildet. Welche ist die drittgrößte?', str(zahlen246[2]),
          'Von groß nach klein: 642, 624, 462, 426, 264, 246. Die drittgrößte ist 462.', 'Schreibe alle Zahlen systematisch auf, mit der größten Hunderterziffer zuerst.'),
        Z(2, 'Drei Stationen A, B und C werden nacheinander besucht, jede genau einmal. Wie viele Reihenfolgen beginnen mit B?', str(sum(1 for p in _perm('ABC') if p[0] == 'B')),
          'B steht vorne fest. Danach A, C oder C, A: 2 Reihenfolgen (BAC, BCA).', 'Halte B fest und ordne den Rest.'),
        Z(3, 'Mit den Ziffernkarten 2, 4, 7 und 9 werden vierstellige Zahlen gelegt, jede Karte genau einmal. Wie viele dieser Zahlen sind größer als 7 000?',
          str(sum(1 for p in _perm('2479') if int(''.join(p)) > 7000)), 'Vorne muss 7 oder 9 stehen: 2 Möglichkeiten. Die übrigen 3 Karten: 3 · 2 · 1 = 6. Zusammen 12.',
          'Welche Karte darf vorne liegen? Wie viele Möglichkeiten gibt es danach jeweils?'),
        Z(3, 'Vier Stationen A, B, C und D werden nacheinander besucht, jede genau einmal. A muss direkt vor B kommen. Wie viele Reihenfolgen gibt es?',
          str(sum(1 for p in _perm('ABCD') if p.index('B') == p.index('A') + 1)), 'Fasse „AB“ zu einem Block zusammen. Dann sind 3 Teile zu ordnen: 3 · 2 · 1 = 6.',
          'Klebe A und B zusammen.'),
        Z(3, 'Aus 5 verschieden großen Scheiben werden Türme aus 3 Scheiben gebaut. Jede Scheibe muss kleiner sein als die darunter. Wie viele verschiedene Türme gibt es?',
          str(len(list(_komb(range(5), 3)))), 'Die Reihenfolge ist durch die Größe festgelegt – es zählt nur, welche 3 Scheiben man nimmt. Auflisten ergibt 10 Auswahlen.',
          'Liste auf, welche 3 Scheiben (1 bis 5) man nehmen kann: 123, 124, …'),
        Z(3, 'Wie viele dreistellige Zahlen haben die Quersumme 3?', str(sum(1 for n in range(100, 1000) if sum(map(int, str(n))) == 3)),
          'Systematisch: 102, 111, 120, 201, 210, 300. Das sind 6.', 'Beginne mit der Hunderterziffer 1, dann 2, dann 3.'),
    ]
    gruen = sum(1 for h, g, s in _prod(['grün', 'blau'], ['G1', 'G2', 'G3', 'ohne'], range(5)) if (h == 'grün') == (g == 'ohne'))
    faerb = sum(1 for f in _prod('rgb', repeat=3) if f[0] != f[1] and f[1] != f[2])
    menue = einzig([v for v in range(1, 20) if v * 15 * v == 60])
    N['zaehlprinzip'] = [
        Z(2, 'Für eine Reise packt jemand 2 Hosen, 3 Gürtel und 5 Shirts ein. Wie viele Outfits aus je einer Hose, einem Gürtel und einem Shirt sind möglich?', '2 * 3 * 5',
          'Zählprinzip: 2 · 3 · 5 = 30.', 'Nacheinander wählen heißt malnehmen.'),
        Z(2, 'Ein Kennwort besteht aus 2 Buchstaben (A, B oder C, auch doppelt) und danach 1 Ziffer (0 bis 9). Wie viele Kennwörter gibt es?', '3 * 3 * 10',
          '3 · 3 · 10 = 90.', 'Wie viele Möglichkeiten gibt es für jede Stelle?'),
        Z(3, 'Es gibt eine grüne und eine blaue Hose, 3 Gürtel und 5 Shirts. Die grüne Hose wird immer ohne Gürtel getragen, die blaue immer mit Gürtel. Wie viele Outfits gibt es?', str(gruen),
          'Grüne Hose: nur Shirts wählen, 5 Outfits. Blaue Hose: 3 · 5 = 15 Outfits. Zusammen 20.', 'Zähle die beiden Hosen getrennt und addiere.'),
        Z(3, 'Drei Felder liegen in einer Reihe. Jedes wird rot, gelb oder blau gefärbt. Nebeneinanderliegende Felder dürfen nicht dieselbe Farbe haben. Wie viele Färbungen gibt es?', str(faerb),
          'Erstes Feld: 3 Farben. Zweites: nicht wie das erste, 2 Farben. Drittes: nicht wie das zweite, 2 Farben. 3 · 2 · 2 = 12.', 'Wie viele Farben bleiben für jedes Feld übrig?'),
        Z(3, 'Ein Schloss hat 3 Rädchen mit den Ziffern 0 bis 9. Man weiß: Die drei Ziffern sind verschieden, und die erste ist eine 7. Wie viele Codes kommen noch infrage?',
          str(sum(1 for c in _prod(range(10), repeat=3) if c[0] == 7 and len(set(c)) == 3)), 'Erste Ziffer fest. Zweite: 9 Möglichkeiten (nicht 7). Dritte: 8. 9 · 8 = 72.',
          'Wie viele Ziffern bleiben für das zweite und dritte Rädchen?'),
        Z(3, 'Ein Menü aus Vor-, Haupt- und Nachspeise hat 60 Möglichkeiten. Es gibt gleich viele Vor- wie Nachspeisen und 15 Hauptspeisen. Wie viele Vorspeisen gibt es?', str(menue),
          '60 : 15 = 4 Möglichkeiten für Vor- und Nachspeise zusammen. Gleich viele: 2 · 2 = 4. Also 2 Vorspeisen.', 'Teile zuerst durch die Zahl der Hauptspeisen.'),
    ]
    gerade = sum(1 for p in _perm('2357') if int(p[-1]) % 2 == 0)
    nicht_neben = sum(1 for p in _perm('ABCDE') if abs(p.index('A') - p.index('B')) != 1)
    otto = len(set(_perm('OTTO')))
    foto = sum(1 for p in _perm('abcXY') if {p[0], p[-1]} == {'X', 'Y'})
    N['reihenfolgen'] = [
        Z(2, 'Aus den vier Tönen c, d, e und f wird eine Melodie gespielt, jeder Ton genau einmal. Wie viele verschiedene Melodien gibt es?', '4 * 3 * 2 * 1',
          'Erster Ton: 4, zweiter: 3, dritter: 2, vierter: 1. 4 · 3 · 2 · 1 = 24.', 'Bei jedem Ton ist einer weniger übrig.'),
        Z(2, 'Bei einem Wettlauf starten 8 Kinder. Wie viele Möglichkeiten gibt es für die Plätze 1, 2 und 3?', '8 * 7 * 6', '8 · 7 · 6 = 336.', 'Platz 1: 8 Kinder, Platz 2: …'),
        Z(3, 'Mit den Ziffern 2, 3, 5 und 7 werden vierstellige Zahlen ohne doppelte Ziffer gebildet. Wie viele davon sind gerade?', str(gerade),
          'Gerade heißt: Die letzte Ziffer ist 2. Die anderen drei Ziffern davor: 3 · 2 · 1 = 6.', 'Welche Ziffer muss hinten stehen?'),
        Z(3, '5 Kinder stellen sich in eine Reihe. Zwei bestimmte Kinder wollen nicht nebeneinander stehen. Wie viele Reihenfolgen gibt es?', str(nicht_neben),
          'Alle: 5 · 4 · 3 · 2 · 1 = 120. Nebeneinander (als Block, zwei Richtungen): 2 · 24 = 48. Nicht nebeneinander: 120 − 48 = 72.',
          'Zähle zuerst alle Reihenfolgen und ziehe die ab, bei denen die beiden nebeneinander stehen.'),
        Z(3, 'Wie viele verschiedene „Wörter“ (auch sinnlose) kann man aus den Buchstaben O, T, T, O bilden, wenn alle vier verwendet werden?', str(otto),
          'Auflisten: OOTT, OTOT, OTTO, TOOT, TOTO, TTOO. Das sind 6. (4 · 3 · 2 · 1 = 24 zählt gleiche Buchstaben mehrfach.)', 'Gleiche Buchstaben zu vertauschen ergibt kein neues Wort. Liste auf.'),
        Z(3, 'Für ein Foto stellen sich 3 Kinder und 2 Erwachsene in eine Reihe. Die Erwachsenen stehen ganz außen. Wie viele Aufstellungen gibt es?', str(foto),
          'Die Erwachsenen außen: 2 Möglichkeiten (wer links steht). Die Kinder in der Mitte: 3 · 2 · 1 = 6. Zusammen 2 · 6 = 12.', 'Ordne zuerst die Erwachsenen, dann die Kinder.'),
    ]
    rad = sum(1 for a, b in _prod(range(1, 4), repeat=2) if b > a)
    kein_kk = sum(1 for f in _prod('KZ', repeat=4) if 'KK' not in ''.join(f))
    prod12 = sum(1 for a, b in _prod(range(1, 7), repeat=2) if a * b == 12)
    baum = {'typ': 'baum', 'aeste': [{'text': 'K', 'aeste': [{'text': 'K'}, {'text': 'Z'}]}, {'text': 'Z', 'aeste': [{'text': 'K'}, {'text': 'Z'}]}]}
    N['baumdiagramm'] = [
        Z(2, 'Eine Münze wird 4-mal geworfen. Wie viele Pfade hat das Baumdiagramm?', '2 ** 4', 'Jede Stufe verdoppelt die Pfade: 2 · 2 · 2 · 2 = 16.', 'Wie viele Äste gehen bei jedem Wurf weiter?'),
        Z(2, 'Ein Glücksrad hat die Felder 1, 2 und 3. Es wird zweimal gedreht. Bei wie vielen Pfaden ist die zweite Zahl größer als die erste?', str(rad),
          'Passend: (1, 2), (1, 3), (2, 3). Das sind 3 Pfade.', 'Schreibe alle 9 Pfade auf und markiere die passenden.'),
        Z(3, 'In einer Dose liegen eine rote, eine blaue und eine grüne Kugel. Es wird zweimal OHNE Zurücklegen gezogen. Wie viele Pfade hat das Baumdiagramm?', str(len(list(_perm('rbg', 2)))),
          'Erste Stufe: 3 Äste. Zweite Stufe: nur noch 2 Kugeln, also 2 Äste. 3 · 2 = 6 Pfade.', 'Wie viele Kugeln sind beim zweiten Zug noch in der Dose?'),
        Z(3, 'Das Baumdiagramm zeigt zwei Münzwürfe (K = Kopf, Z = Zahl). Bei wie vielen Pfaden kommt mindestens einmal Z vor?', str(sum(1 for f in _prod('KZ', repeat=2) if 'Z' in f)),
          'Alle Pfade: KK, KZ, ZK, ZZ. Mindestens einmal Z: KZ, ZK, ZZ – also 3.', '„Mindestens einmal“ heißt: einmal oder öfter.', grafik=baum),
        Z(3, 'Eine Münze wird 4-mal geworfen. Bei wie vielen Pfaden kommt nie zweimal hintereinander Kopf?', str(kein_kk),
          'Systematisch aufzählen: ZZZZ, KZZZ, ZKZZ, ZZKZ, ZZZK, KZKZ, KZZK, ZKZK. Das sind 8.', 'Ordne nach der Zahl der Köpfe: 0, 1 oder 2 Köpfe.'),
        Z(3, 'Zwei Würfel werden nacheinander geworfen. Bei wie vielen der 36 Pfade ist das Produkt der Augenzahlen 12?', str(prod12),
          '12 = 2 · 6 = 3 · 4 = 4 · 3 = 6 · 2. Das sind 4 Pfade.', 'Zerlege 12 in zwei Faktoren von 1 bis 6. Die Reihenfolge zählt.'),
    ]
    teilbar = sum(1 for e in range(100) if (5200 + e) % 25 == 0)
    qs6 = sum(1 for n in range(100, 1000) if len(set(str(n))) == 3 and sum(map(int, str(n))) == 6)
    sieben = sum(1 for n in range(100, 1000) if '7' in str(n))
    code = sum(1 for c in _prod(range(10), repeat=3) if c[0] % 2 == 0 and c[2] % 2 == 1)
    N['bedingungen'] = [
        Z(2, 'Wie viele zweistellige Zahlen bestehen aus zwei gleichen Ziffern?', str(sum(1 for n in range(10, 100) if n % 11 == 0)), 'Das sind 11, 22, …, 99: 9 Zahlen.', 'Die erste Ziffer darf nicht 0 sein.'),
        Z(2, 'Wie viele dreistellige Zahlen enden mit einer 0?', '9 * 10 * 1', 'Hunderter: 9 (nicht 0), Zehner: 10, Einer: nur 0. 9 · 10 · 1 = 90.', 'Welche Stelle ist festgelegt?'),
        Z(3, 'Die Zahl 52□□ soll durch 25 teilbar sein. Wie viele Möglichkeiten gibt es für die beiden letzten Ziffern?', str(teilbar),
          'Durch 25 teilbar sind Zahlen, die auf 00, 25, 50 oder 75 enden: 4 Möglichkeiten (5 200, 5 225, 5 250, 5 275).', 'Auf welche Endungen enden Vielfache von 25?'),
        Z(3, 'Wie viele dreistellige Zahlen mit lauter verschiedenen Ziffern haben die Quersumme 6?', str(qs6),
          'Ziffern-Sätze: {1, 2, 3}: 6 Zahlen. {0, 1, 5} und {0, 2, 4}: je 4 (die 0 darf nicht vorne stehen). Zusammen 14.',
          'Suche zuerst drei verschiedene Ziffern mit der Summe 6. Zähle dann die Anordnungen.'),
        Z(3, 'Wie viele dreistellige Zahlen enthalten mindestens eine 7?', str(sieben),
          'Ohne 7: 8 · 9 · 9 = 648 (vorne nicht 0 und nicht 7). Alle: 900. Mindestens eine 7: 900 − 648 = 252.', 'Zähle das Gegenteil: Wie viele Zahlen haben gar keine 7?'),
        Z(3, 'Ein Code hat 3 Ziffern (0 bis 9, Wiederholung erlaubt). Die erste Ziffer ist gerade, die letzte ungerade. Wie viele Codes gibt es?', str(code),
          'Erste: 0, 2, 4, 6, 8 (5). Mitte: 10. Letzte: 1, 3, 5, 7, 9 (5). 5 · 10 · 5 = 250.', 'Achtung: Bei einem Code darf vorne auch 0 stehen.'),
    ]
    turnier = einzig([n for n in range(2, 30) if n * (n - 1) // 2 == 28])
    karten = einzig([n for n in range(2, 30) if n * (n - 1) == 30])
    N['grenzen'] = [
        Z(2, '10 Kinder geben sich gegenseitig einmal die Hand. Wie viele Handschläge gibt es?', '10 * 9 // 2', '10 · 9 = 90 zählt jeden Handschlag doppelt: 90 : 2 = 45.', 'Erst das Zählprinzip, dann durch 2.'),
        Z(2, 'Aus 5 Kindern werden 2 für den Tafeldienst ausgewählt (beide machen dasselbe). Wie viele Möglichkeiten gibt es?', '5 * 4 // 2', '5 · 4 = 20, aber „A und B“ ist dasselbe wie „B und A“: 20 : 2 = 10.',
          'Ist die Reihenfolge wichtig?'),
        Z(3, 'Bei einem Turnier spielt jede Mannschaft genau einmal gegen jede andere. Es finden 28 Spiele statt. Wie viele Mannschaften nehmen teil?', str(turnier),
          'Probieren: Bei 8 Mannschaften gibt es 8 · 7 : 2 = 28 Spiele.', 'Rechne für 6, 7, 8 Mannschaften die Zahl der Spiele aus.'),
        Z(3, 'Wie viele Diagonalen hat ein Sechseck?', f'{len(list(_komb(range(6), 2)))} - 6',
          'Verbindungen zwischen 6 Ecken: 6 · 5 : 2 = 15. Davon sind 6 die Seiten. Diagonalen: 15 − 6 = 9.', 'Zähle alle Verbindungslinien und ziehe die Seiten ab.'),
        wahl(3, 'Bei welcher Frage muss man nach dem Zählprinzip noch durch 2 teilen?', ['Wie viele Handschläge gibt es bei 6 Personen?', 'Wie viele Möglichkeiten gibt es für Platz 1 und 2 bei 6 Läufern?',
                                                                                      'Wie viele Outfits gibt es aus 6 Hosen und 2 Shirts?', 'Wie viele zweistellige Zahlen kann man aus 6 Ziffern bilden?'],
             lambda o: o.startswith('Wie viele Handschläge'), 'Nur beim Handschlag ist die Reihenfolge egal (A–B = B–A). Bei Plätzen und Zahlen ist sie wichtig, bei Outfits gibt es keine Doppelzählung.',
             'Wo würde man ein Paar doppelt zählen?'),
        Z(3, 'In einer Gruppe schreibt jedes Kind jedem anderen Kind eine Karte. Es werden 30 Karten geschrieben. Wie viele Kinder sind in der Gruppe?', str(karten),
          'Hier zählt die Richtung: Karte von A an B und von B an A sind zwei Karten. n · (n − 1) = 30 gilt für n = 6.', 'Muss man hier durch 2 teilen? Probiere kleine Gruppen.'),
    ]
    wege = sum(1 for p in set(_perm('RROO')))
    N['verstehen'] = [
        wahl(2, 'Stimmt die Aussage? „Mit 3 Hemden und 0 Hosen gibt es 0 Outfits aus Hemd und Hose.“', ['Ja: 3 · 0 = 0.', 'Nein: 3 Outfits.', 'Nein: 3 + 0 = 3 Outfits.'],
             lambda o: o.startswith('Ja'), 'Ohne Hose kann man kein Outfit aus Hemd und Hose bilden: 3 · 0 = 0.', 'Was passiert beim Malnehmen mit 0?'),
        wahl(2, 'Stimmt die Aussage? „Bei 4 Läufern gibt es 24 mögliche Zieleinläufe (ohne gleiche Plätze).“', ['Ja: 4 · 3 · 2 · 1 = 24.', 'Nein: 4 · 4 = 16.', 'Nein: 4 + 3 + 2 + 1 = 10.'],
             lambda o: o.startswith('Ja'), '4 · 3 · 2 · 1 = 24.', 'Wie viele Läufer kommen für jeden Platz noch infrage?'),
        A(3, 'Jemand sagt: „Aus den Ziffern 1, 1 und 2 lassen sich 6 dreistellige Zahlen bilden, weil 3 · 2 · 1 = 6.“ Stimmt das?',
          'Nein: Die beiden Einsen sind gleich. Es gibt nur 112, 121 und 211.', ['Ja, das stimmt.', 'Nein, es sind 9 Zahlen.', 'Nein, es sind 2 Zahlen.'],
          f'Vertauscht man die beiden Einsen, entsteht dieselbe Zahl. Es bleiben {len(set(_perm("112")))} Zahlen.', 'Liste alle Zahlen auf.'),
        wahl(3, '3 von 5 Büchern sollen nacheinander auf 3 Plätze ins Regal gestellt werden. Welche Rechnung passt?', ['5 · 4 · 3', '5 · 5 · 5', '5 + 4 + 3', '3 · 2 · 1'],
             lambda o: o == '5 · 4 · 3', 'Platz 1: 5 Bücher, Platz 2: noch 4, Platz 3: noch 3. 5 · 4 · 3 = 60.', 'Wie viele Bücher stehen für jeden Platz noch zur Wahl?'),
        wahl(3, 'Zwei Würfel werden geworfen. Stimmt die Aussage: „Augensumme 7 ist genauso oft möglich wie Augensumme 12.“?',
             ['Nein: Summe 7 hat 6 Pfade, Summe 12 nur einen (6 und 6).', 'Ja, jede Summe ist gleich oft möglich.', 'Nein: Summe 12 ist öfter möglich.', 'Ja, beide je 6-mal.'],
             lambda o: o.startswith('Nein: Summe 7'), f'Summe 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1 = {sum(1 for a, b in _prod(range(1, 7), repeat=2) if a + b == 7)} Pfade. Summe 12: nur 6+6.',
             'Zähle die Pfade für beide Summen.'),
        Z(3, 'In einem Gitter läufst du von der Ecke unten links zur Ecke oben rechts: genau 2 Schritte nach rechts und 2 Schritte nach oben, in beliebiger Reihenfolge. Wie viele Wege gibt es?', str(wege),
          'Auflisten (R = rechts, O = oben): RROO, RORO, ROOR, ORRO, OROR, OORR. Das sind 6.', 'Schreibe die Wege als Wörter aus 2 R und 2 O.'),
    ]
    return N


ergaenze(DATEI, _schwer(), 1060)

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('stochastik.kombinatorik', 13_5_11)
# a) gleicher Gedanke wie die Handschlag-Aufgaben (Stufe 1); mit 3 Punkten sogar leichter
_g = 'Wie viele Strecken kann man zwischen {} Punkten zeichnen, von denen keine drei auf einer Geraden liegen?'
BF.stufe('grenzen', _g.format(3), 1)
for _n in (6, 5, 7):
    BF.stufe('grenzen', _g.format(_n), 2)
# a) gleicher Typ und gleiches Ergebnis wie Stufe 2
for _z in ('0, 1, 5, 6', '0, 3, 8, 9', '0, 4, 6, 7'):
    BF.stufe('bedingungen', f'Aus den Ziffern {_z} werden dreistellige Zahlen ohne doppelte Ziffer gebildet. Wie viele gibt es?', 2)
# a) Zählprinzip-Grundform
for _t in ('2 Sorten, 3 Soßen und 2 Streusel', '3 Sorten, 2 Soßen und 2 Streusel'):
    BF.stufe('systematisch', f'Beim Eis gibt es {_t}. Ein Becher hat genau eine Sorte, eine Soße und einen Streusel. Wie viele verschiedene Becher gibt es?', 2)

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl5, siehe _durchsicht_kl5.py) ----
from _durchsicht_kl5 import Durchsicht, durchsicht_anwenden  # noqa: E402

DS = Durchsicht('stochastik.kombinatorik', 19_5_9)
# a) Stufe 3 mit derselben Vorlage oder demselben Gedanken wie Stufe 1/2 → Stufe 2
for _lz, _t in [('systematisch', 'Beim Eis gibt es 3 Sorten, 3 Soßen und 2 Streusel. Ein Becher hat genau eine Sorte, eine Soße und einen Streusel. Wie viele verschiedene Becher gibt es?'),
        ('zaehlprinzip', 'Es gibt 3 Hosen, 4 Pullover und einige Mützen. Insgesamt sind 48 verschiedene Outfits aus je einem Teil möglich. Wie viele Mützen gibt es?'),
        ('zaehlprinzip', 'Ein Vereinsausweis hat einen Code aus 1 Großbuchstaben (A bis Z, 26 Stück) und danach 3 Ziffern (0 bis 9). Wie viele Codes gibt es?'),
        ('reihenfolgen', 'Wie viele verschiedene „Wörter“ (auch sinnlose) kann man aus den Buchstaben von KATZE bilden, wenn jeder Buchstabe genau einmal verwendet wird?'),
        ('reihenfolgen', 'Wie viele verschiedene „Wörter“ (auch sinnlose) kann man aus den Buchstaben von HUND bilden, wenn jeder Buchstabe genau einmal verwendet wird?'),
        ('reihenfolgen', 'Wie viele verschiedene „Wörter“ (auch sinnlose) kann man aus den Buchstaben von MAUS bilden, wenn jeder Buchstabe genau einmal verwendet wird?'),
        ('bedingungen', 'Aus den Ziffern 0, 1, 6, 7 werden dreistellige Zahlen ohne doppelte Ziffer gebildet. Wie viele davon sind gerade?'),
        ('baumdiagramm', 'Das Baumdiagramm zeigt zwei Münzwürfe (K = Kopf, Z = Zahl). Bei wie vielen Pfaden kommt mindestens einmal Z vor?')]:
    DS.stufe(_lz, _t, 2, enthaelt=lambda x: x['s'] == 3)
durchsicht_anwenden(DATEI, DS)
# ---- DURCHSICHT ENDE ----
# ---- STUFEN (Zwanzigste Runde, Zweig stufen-kl5, siehe _stufen_kl5.py und _st5_stochastik_kombinatorik.py) ----
from _stufen_kl5 import stufen_anwenden  # noqa: E402
stufen_anwenden(DATEI, 'stochastik.kombinatorik')
# ---- STUFEN ENDE ----

if __name__ == '__main__':
    schreibe(DATEI)
