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

MERKE = ['Systematisch zählen: erste Wahl festhalten, alle zweiten durchgehen.', 'Zählprinzip: Anzahlen der Schritte malnehmen.',
         'Ohne Wiederholung: in jedem Schritt eine Möglichkeit weniger.', 'Baumdiagramm: Anzahl der Pfade = Anzahl der Möglichkeiten.',
         'Reihenfolge egal (Händeschütteln): Zählprinzip zählt doppelt – durch 2 teilen.']

KLEID = [('Hosen', 'T-Shirts'), ('Röcke', 'Blusen'), ('Mützen', 'Schals'), ('Brotsorten', 'Beläge'), ('Eissorten', 'Waffeln'), ('Fahrradrahmen', 'Lenkerfarben')]
FARBEN = ['rot', 'blau', 'grün', 'gelb', 'weiß', 'schwarz']


# ---------- 1 Systematisch ----------
def g_sys(st):
    if st == 1:
        a, b = R.randint(2, 4), R.randint(2, 4)
        x, y = R.choice(KLEID)
        fa, fb = FARBEN[:a], FARBEN[a:a + b] if a + b <= 6 else FARBEN[:b]
        tab = {'typ': 'tabelle', 'kopf': [''] + fb, 'zeilen': [[f] + ['?'] * b for f in fa]}
        return {'y': 'zahl', 'f': {'text': f'Es gibt {a} {x} und {b} {y}. Wie viele Kombinationen aus einem Stück jeder Sorte gibt es? Die Tabelle hilft.', 'grafik': tab},
                'o': {'wert': a * b}, 'c': f'{a} * {b}', 'w': f'Jede der {a} Möglichkeiten ({x}) lässt sich mit allen {b} {y} kombinieren: {a} · {b} = {a * b}.', 'h': 'Jede Zeile der Tabelle hat gleich viele Felder.'}
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
    art = R.randrange(3)
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
    return {'y': 'zahl', 'f': {'text': f'Von A nach B führen {a} Wege, von B nach C {b} Wege. Wie viele verschiedene Wege gibt es von A über B nach C und auf einem der Wege wieder zurück nach A?'},
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
def g_baum(st):
    if st == 1:
        a, b = R.randint(2, 4), R.randint(2, 4)
        return {'y': 'zahl', 'f': {'text': f'Ein Baumdiagramm hat zwei Stufen. Auf der ersten Stufe gibt es {a} Äste, an jedem Ende gehen {b} Äste weiter. Wie viele Pfade hat das Baumdiagramm?'},
                'o': {'wert': a * b}, 'c': f'{a} * {b}', 'w': f'Jeder der {a} Äste verzweigt sich in {b}: {a} · {b} = {a * b} Pfade.', 'h': 'Zähle die Enden der zweiten Stufe.'}
    if st == 2 and R.random() < .6:
        m = R.randint(3, 5)
        farben = ['rote', 'blaue', 'grüne', 'gelbe', 'weiße'][:m]
        zur = R.random() < .5
        frage = R.choice(['alle', 'gleich'])
        if frage == 'alle':
            r = m * m if zur else m * (m - 1)
            return {'y': 'zahl', 'f': {'text': f'In einer Dose liegen {m} Kugeln: ' + ', '.join(f'eine {f}' for f in farben) + f'. Es wird zweimal gezogen, {"mit" if zur else "ohne"} Zurücklegen. Wie viele Pfade hat das Baumdiagramm?'},
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
        return {'y': 'zahl', 'f': {'text': f'Eine Münze wird {n}-mal geworfen. Wie viele Pfade im Baumdiagramm enthalten genau {k}-mal Kopf?'}, 'o': {'wert': r},
                'c': ' + '.join(['1'] * r), 'w': 'Pfade: ' + ', '.join(''.join(p) for p in product('KZ', repeat=n) if p.count('K') == k) + f' – also {r}.',
                'h': 'Schreibe alle Pfade auf (KKZ, KZK …) und zähle die passenden.'}
    art = R.randrange(2)
    if art == 0:
        n = 3
        bed = R.choice([('mindestens einmal Kopf', lambda p: 'K' in p), ('höchstens einmal Kopf', lambda p: p.count('K') <= 1), ('zweimal hintereinander dasselbe', lambda p: any(p[i] == p[i + 1] for i in range(n - 1)))])
        ps = [''.join(p) for p in product('KZ', repeat=n) if bed[1](''.join(p))]
        return {'y': 'zahl', 'f': {'text': f'Eine Münze wird dreimal geworfen. Wie viele der 8 Pfade erfüllen: {bed[0]}?'}, 'o': {'wert': len(ps)}, 'c': ' + '.join(['1'] * len(ps)),
                'w': 'Passend: ' + ', '.join(ps) + f'. Das sind {len(ps)}.', 'h': 'Schreibe alle 8 Pfade auf: KKK, KKZ, KZK, …'}
    z = R.choice([4, 5, 6])
    ps = [(a, b) for a in range(1, 7) for b in range(1, 7) if a + b == z]
    return {'y': 'zahl', 'f': {'text': f'Zwei Würfel werden nacheinander geworfen. Bei wie vielen der 36 Pfade ist die Augensumme {z}?'}, 'o': {'wert': len(ps)}, 'c': ' + '.join(['1'] * len(ps)),
            'w': 'Paare (1. Wurf, 2. Wurf): ' + ', '.join(f'({a}, {b})' for a, b in ps) + f' – {len(ps)} Pfade.', 'h': 'Gehe den ersten Wurf von 1 bis 6 durch und überlege, was der zweite zeigen muss.'}


# ---------- 5 Bedingungen ----------
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
        art = R.randrange(2)
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
    art = R.randrange(2)
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
    return {'y': 'zahl', 'f': {'text': f'Bei einer Feier gab es {m} Handschläge. Jeder hat jedem genau einmal die Hand gegeben. Wie viele Personen waren da?'}, 'o': {'wert': n},
            'c': f'{n}', 'w': f'Probieren: Bei {n} Personen gibt es {n} · {n - 1} : 2 = {m} Handschläge.', 'h': 'Probiere: 3 Personen → 3, 4 Personen → 6, 5 Personen → 10 …'}


# ---------- 7 Verstehen ----------
def g_vers(st):
    a, b = R.randint(2, 5), R.randint(2, 5)
    if st == 1:
        aussagen = [(f'Mit {a} Hosen und {b} T-Shirts gibt es {a + b} Outfits.', False, f'Nein, zu jeder Hose passen alle T-Shirts: {a} · {b} = {a * b}.'),
                    (f'Mit {a} Hosen und {b} T-Shirts gibt es {a * b} Outfits.', True, f'Ja, Zählprinzip: {a} · {b} = {a * b}.'),
                    ('Eine Münze zweimal geworfen hat 4 mögliche Ergebnisfolgen.', True, 'Ja: KK, KZ, ZK, ZZ.'), ('Eine Münze zweimal geworfen hat 3 mögliche Ergebnisfolgen.', False, 'Nein, KZ und ZK sind verschieden: 4 Folgen.')]
    elif st == 2:
        n = R.randint(3, 6)
        aussagen = [(f'{n} Kinder können sich auf {factorial(n)} Arten in eine Reihe stellen.', True, f'Ja, {" · ".join(str(i) for i in range(n, 0, -1))} = {factorial(n)}.'),
                    (f'{n} Kinder können sich auf {n * n} Arten in eine Reihe stellen.', False, f'Nein, ohne Wiederholung: {factorial(n)}.'),
                    (f'Bei {n} Kindern gibt es {n * (n - 1)} Handschläge, wenn jeder jedem die Hand gibt.', False, f'Nein, jeder Handschlag ist doppelt gezählt: {n * (n - 1) // 2}.'),
                    ('Mit den Ziffern 1, 2, 3 gibt es 6 zweistellige Zahlen ohne doppelte Ziffer.', True, 'Ja: 12, 13, 21, 23, 31, 32.'),
                    (f'Bei {n} Kindern gibt es {n * (n - 1) // 2} Handschläge, wenn jeder jedem einmal die Hand gibt.', True, f'Ja, {n} · {n - 1} : 2 = {n * (n - 1) // 2}.'),
                    (f'Für die Plätze 1 und 2 bei {n + 2} Läufern gibt es {(n + 2) * (n + 1)} Möglichkeiten.', True, f'Ja, {n + 2} · {n + 1} = {(n + 2) * (n + 1)}.'),
                    (f'Für die Plätze 1 und 2 bei {n + 2} Läufern gibt es {(n + 2) * (n + 2)} Möglichkeiten.', False, f'Nein, niemand kann beide Plätze belegen: {n + 2} · {n + 1} = {(n + 2) * (n + 1)}.')]
    else:
        aussagen = [('Es gibt 1 000 dreistellige Zahlen.', False, 'Nein, 9 · 10 · 10 = 900 (100 bis 999).'),
                    ('Ein Zahlenschloss mit 3 Rädchen (0–9) hat 1 000 Codes.', True, 'Ja, beim Schloss ist auch 0 vorne erlaubt: 10 · 10 · 10 = 1 000.'),
                    ('Werden zwei Würfel geworfen, gibt es 12 mögliche Paare.', False, 'Nein, 6 · 6 = 36 Paare.'),
                    ('Das Zählprinzip gilt nur, wenn in jedem Schritt gleich viele Möglichkeiten sind.', False, 'Nein, die Anzahlen dürfen verschieden sein (z. B. 3 · 4 · 2) – sie dürfen nur nicht vom vorigen Schritt abhängen.'),
                    (f'Aus {a + 3} Eissorten 2 verschiedene Kugeln in eine Waffel (Reihenfolge egal): {(a + 3) * (a + 2) // 2} Möglichkeiten.', True, f'Ja, ({a + 3} · {a + 2}) : 2 = {(a + 3) * (a + 2) // 2}.')]
    s, stimmt, grund = R.choice(aussagen)
    gegen = 'Ja, das stimmt.' if not stimmt else 'Nein, das ist falsch.'
    return {**wahl(R, grund, [gegen, 'Das kann man nicht entscheiden.'], 3), 'f': {'text': f'Stimmt die Aussage? „{s}“'}, 'w': grund, 'h': 'Und oder oder? Wiederholung? Reihenfolge wichtig?'}


GEN = {'systematisch': g_sys, 'zaehlprinzip': g_zp, 'reihenfolgen': g_rf, 'baumdiagramm': g_baum, 'bedingungen': g_bed, 'grenzen': g_gr, 'verstehen': g_vers}

DATEI = datei(E, 'Anzahlen systematisch, mit dem Zählprinzip und mit Baumdiagrammen bestimmen und prüfen, ob das Zählprinzip anwendbar ist.', MERKE,
              [('Systematisch zählen', ['systematisch', 'zaehlprinzip', 'reihenfolgen']),
               ('Baumdiagramm und Bedingungen', ['baumdiagramm', 'bedingungen']),
               ('Grenzen und Verstehen', ['grenzen', 'verstehen'])],
              ETAPPEN, GEN,
              offen=['Braucht Zeichnung: Baumdiagramm (Lernkarte baumdiagramm) kann die App noch nicht zeichnen; die Bäume sind in Worten beschrieben. Kombinationstabellen sind als Tabelle gezeichnet.',
                     'Begriffe wie Permutation, Variation, Kombination, n! und Binomialkoeffizient werden bewusst nicht eingeführt (höhere Klassen); alles läuft über Zählprinzip, Auflisten und „durch 2 teilen“.'])

if __name__ == '__main__':
    schreibe(DATEI)
