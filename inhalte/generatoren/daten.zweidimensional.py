#!/usr/bin/env python3
"""Thema daten.zweidimensional – Zweidimensionale Daten (IB MYP 3, etwa Klasse 8)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403

start(5903)

# Sachzusammenhänge: (x-Name, x-Einheit, y-Name, y-Einheit, x-Bereich, Steigung, Achsenabschnitt, Streuung-Grundwert, Wort für einen Datenpunkt)
SACH = [
    ('Lernzeit', 'h', 'Punkte im Test', 'Punkte', (1, 10), 5, 40, 6, 'Schüler'),
    ('Tagestemperatur', '°C', 'verkaufte Eiskugeln', 'Kugeln', (14, 32), 12, -100, 30, 'Tag'),
    ('Alter des Autos', 'Jahren', 'Wert', 'Tausend €', (1, 10), -2, 26, 2, 'Auto'),
    ('Körpergröße', 'cm', 'Schuhgröße', '', (150, 190), 0.25, 0, 1, 'Person'),
    ('Trainingsstunden pro Woche', 'h', '1000-m-Zeit', 's', (1, 9), -6, 300, 8, 'Läufer'),
    ('Fahrstrecke', 'km', 'Taxipreis', '€', (2, 20), 2, 4, 2, 'Fahrt'),
]


def korrelation(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    return sxy / (sxx * syy) ** .5 if sxx and syy else 0


def daten(sach, art, n=None):
    """art: stark_pos, schwach_pos, stark_neg, schwach_neg, kein. Gibt xs, ys zurück."""
    xn, xe, yn, ye, (x0, x1), m, t, st, _ = sach
    n = n or R.randint(8, 11)
    for _ in range(400):
        xs = sorted(R.sample(range(x0, x1 + 1), n)) if x1 - x0 + 1 >= n else None
        if xs is None: return None
        mm = abs(m) * (1 if 'pos' in art else -1)
        if art == 'kein':
            mitte = sum(abs(m) * x + t for x in xs) / n if m > 0 else sum(m * x + t for x in xs) / n
            ys = [round(mitte + R.uniform(-3, 3) * st) for _ in xs]
        else:
            f = 1 if 'stark' in art else 3.5
            ys = [round(mm * x + (t if m * mm > 0 else t + (m - mm) * (x0 + x1) / 2) + R.uniform(-1, 1) * st * f) for x in xs]
        r = korrelation(xs, ys)
        ok = {'stark_pos': r > .9, 'schwach_pos': .45 < r < .75, 'stark_neg': r < -.9, 'schwach_neg': -.75 < r < -.45, 'kein': abs(r) < .2}[art]
        if ok and min(ys) > 0: return xs, ys
    return None


def streubild(sach, xs, ys, namen=None, linie=None, x_rand=None):
    xn, xe, yn, ye = sach[:4]
    xa, xb = x_rand or (min(xs) - 1, max(xs) + 1)
    lo, hi = min(ys), max(ys)
    sp = hi - lo or 10
    st = next(k for k in (1, 2, 5, 10, 20, 25, 50, 100) if k >= sp / 8)
    ya, yb = max(0, (lo - st) // st * st), (hi + st) // st * st + st
    b = {'typ': 'koordinaten', 'x': [xa, xb], 'y': [ya, yb],
         'punkte': [{'x': x, 'y': y, **({'name': namen[i]} if namen else {})} for i, (x, y) in enumerate(zip(xs, ys))],
         'name_x': f'{xn}' + (f' in {xe}' if xe else ''), 'name_y': f'{yn}' + (f' in {ye}' if ye else ''), 'schritt_y': st}
    if xb - xa > 12: b['schritt_x'] = 2 if xb - xa <= 24 else 5
    if linie: b['graphen'] = [linie]
    return b


ETAPPEN = [
    {'lernziel': 'ablesen', 'titel': 'Streudiagramme lesen',
     'regel': 'Bei ⟦zweidimensionalen Daten⟧ (bivariate data) gehören zu jedem Objekt ⟦zwei Werte⟧, z. B. Lernzeit und Testpunkte eines Schülers. Im ⟦Streudiagramm⟧ (scatter graph) ist jedes Objekt ⟦ein Punkt⟧: x-Wert nach rechts, y-Wert nach oben.',
     'schritte': ['Ein Punkt liegt bei (4 | 60): Dieser Schüler hat 4 Stunden gelernt.', 'Sein y-Wert: ⟦60 Punkte⟧ im Test.'],
     'probe': 'Erst nach rechts zu x = 4, dann nach oben bis zum Punkt ✓',
     'bild': {'typ': 'koordinaten', 'x': [0, 9], 'y': [0, 100], 'punkte': [{'x': 2, 'y': 45}, {'x': 4, 'y': 60, 'name': '(4 | 60)'}, {'x': 6, 'y': 70}, {'x': 8, 'y': 85}],
              'name_x': 'Lernzeit in h', 'name_y': 'Punkte', 'schritt_y': 10},
     'fehler': 'Den Punkt (4 | 60) als „60 Stunden, 4 Punkte“ zu lesen ist falsch: Der ⟦erste Wert gehört zur x-Achse⟧ (nach rechts), der zweite zur y-Achse.'},
    {'lernziel': 'zusammenhang', 'titel': 'Art des Zusammenhangs erkennen',
     'regel': 'Steigen die Punkte von links nach rechts an, ist der Zusammenhang ⟦positiv⟧ (positive correlation): „je mehr x, desto mehr y“. Fallen sie, ist er ⟦negativ⟧. Liegen sie wie eine Wolke ohne Richtung, gibt es ⟦keinen⟧ Zusammenhang. Je enger die Punkte an einer Geraden liegen, desto ⟦stärker⟧ ist der Zusammenhang.',
     'schritte': ['Alter eines Autos und sein Wert: Die Punkte fallen von links oben nach rechts unten.', 'Sie liegen eng an einer Linie: ⟦stark negativer Zusammenhang⟧.'],
     'probe': 'Je älter das Auto, desto geringer der Wert – passt zu „negativ“ ✓',
     'bild': {'typ': 'koordinaten', 'x': [0, 11], 'y': [0, 30], 'punkte': [{'x': 1, 'y': 24}, {'x': 2, 'y': 22}, {'x': 4, 'y': 19}, {'x': 5, 'y': 16}, {'x': 7, 'y': 12}, {'x': 9, 'y': 9}, {'x': 10, 'y': 6}],
              'name_x': 'Alter in Jahren', 'name_y': 'Wert in Tausend €', 'schritt_y': 5},
     'fehler': '„Negativer Zusammenhang“ heißt nicht „kein Zusammenhang“ oder „schlecht“: Negativ beschreibt nur die ⟦Richtung⟧ – wenn x wächst, ⟦wird y kleiner⟧.'},
    {'lernziel': 'gerade', 'titel': 'Mit der Ausgleichsgeraden schätzen',
     'regel': 'Eine ⟦Ausgleichsgerade⟧ (line of best fit) läuft mitten durch die Punktwolke: etwa gleich viele Punkte darüber und darunter. Mit ihrer Gleichung y = m · x + t kann man ⟦Werte schätzen⟧. Innerhalb der Daten (⟦Interpolation⟧) ist das verlässlich, weit außerhalb (⟦Extrapolation⟧) nicht.',
     'schritte': ['Ausgleichsgerade: y = 5x + 40 (x Lernzeit in h, y Punkte).', 'Schätzung für 6 Stunden: y = 5 · 6 + 40 = ⟦70 Punkte⟧.'],
     'probe': 'Im Diagramm liegt bei x = 6 auch ein Punkt in der Nähe von 70 ✓',
     'bild': {'typ': 'koordinaten', 'x': [0, 11], 'y': [0, 100], 'punkte': [{'x': 1, 'y': 48}, {'x': 2, 'y': 47}, {'x': 3, 'y': 58}, {'x': 5, 'y': 62}, {'x': 7, 'y': 78}, {'x': 8, 'y': 77}, {'x': 10, 'y': 92}],
              'graphen': [{'art': 'linear', 'm': 5, 't': 40, 'bereich': [0, 11]}], 'name_x': 'Lernzeit in h', 'name_y': 'Punkte', 'schritt_y': 10},
     'fehler': 'Mit y = 5x + 40 für 20 Stunden 140 Punkte vorherzusagen ist unsinnig, wenn der Test nur 100 Punkte hat: Weit ⟦außerhalb der Daten⟧ gilt die Gerade nicht mehr.'},
    {'lernziel': 'ausreisser', 'titel': 'Ausreißer finden',
     'regel': 'Ein ⟦Ausreißer⟧ (outlier) ist ein Punkt, der ⟦weit weg vom Muster⟧ der anderen liegt. Er kann ein Messfehler sein oder ein echter Sonderfall. Ausreißer verschieben die Ausgleichsgerade, deshalb prüft man sie zuerst.',
     'schritte': ['Fast alle Punkte steigen eng an. Punkt C bei (3 | 90) liegt weit über allen Nachbarn.', '⟦C ist ein Ausreißer⟧.'],
     'probe': 'Die Nachbarn bei x = 2 und x = 4 liegen bei etwa 50 und 60 ✓',
     'bild': {'typ': 'koordinaten', 'x': [0, 9], 'y': [0, 100], 'punkte': [{'x': 1, 'y': 45, 'name': 'A'}, {'x': 2, 'y': 50, 'name': 'B'}, {'x': 3, 'y': 90, 'name': 'C'}, {'x': 4, 'y': 60, 'name': 'D'}, {'x': 6, 'y': 70, 'name': 'E'}, {'x': 8, 'y': 80, 'name': 'F'}],
              'name_x': 'Lernzeit in h', 'name_y': 'Punkte', 'schritt_y': 10},
     'fehler': 'Den Punkt mit dem ⟦größten y-Wert⟧ automatisch als Ausreißer zu nehmen ist falsch: Bei einem steigenden Zusammenhang gehört ein hoher y-Wert ganz rechts zum Muster. Entscheidend ist der ⟦Abstand zum Muster⟧.'},
    {'lernziel': 'kausal', 'titel': 'Korrelation oder Ursache?',
     'regel': 'Ein Zusammenhang in den Daten (⟦Korrelation⟧, correlation) beweist ⟦keine Ursache⟧ (causation). Oft steckt eine ⟦dritte Größe⟧ dahinter, die beide beeinflusst, oder es ist Zufall. Eine Ursache zeigt man erst mit einem ⟦Experiment⟧ oder einer guten Erklärung.',
     'schritte': ['In Sommermonaten werden mehr Eis und mehr Sonnencreme verkauft: positive Korrelation.', 'Eis verursacht keine Sonnencreme. Die dritte Größe ist das ⟦sonnige, warme Wetter⟧.'],
     'probe': 'Im Winter sinken beide Verkäufe – das Wetter erklärt beides ✓',
     'fehler': '„Kinder mit größeren Füßen lesen besser, also macht große Füße schlau“ ist falsch: Beide wachsen mit dem ⟦Alter⟧ – das ist die dritte Größe.'},
]


def g_ablesen(s):
    sach = R.choice([x for x in SACH if x[4][1] - x[4][0] <= 12])
    xn, xe, yn, ye = sach[:4]
    d = daten(sach, R.choice(['stark_pos', 'schwach_pos', 'stark_neg', 'schwach_neg']), n=R.randint(6, 8))
    if not d: return None
    xs, ys = d
    if len(set(ys)) < len(ys): return None
    bild = streubild(sach, xs, ys)
    st = bild['schritt_y']
    if any(y % (st // 2 or 1) for y in ys) and s == 1: return None
    art = R.choice({1: ['y_bei', 'anzahl'], 2: ['y_bei', 'groesste', 'ueber'], 3: ['differenz', 'ueber', 'x_bei']}[s])
    ein = f' {ye}' if ye else ''
    if art == 'y_bei':
        i = R.randrange(len(xs))
        return mit_grafik(zahl(f'Das Streudiagramm zeigt {xn} und {yn}. Lies ab: Welcher y-Wert gehört etwa zum Punkt mit x = {xs[i]}?', f'Bei x = {xs[i]} nach oben gehen: Der Punkt liegt bei y = {ys[i]} (Ablesen auf ±{dz(st / 2)} genau genügt).',
                               'Gehe auf der x-Achse zum Wert und dann senkrecht nach oben bis zum Punkt.', ys[i], f'{ys[i]}', tol=st / 2), bild)
    if art == 'anzahl':
        return mit_grafik(zahl(f'Das Streudiagramm zeigt {xn} und {yn}; jeder Punkt steht für {ART[sach[8]]}. Wie viele wurden erfasst?', f'Jeder Punkt ist ein Objekt: {len(xs)} Punkte.',
                               'Ein Punkt = ein Objekt mit zwei Werten.', len(xs), f'{len(xs)}'), bild)
    if art == 'groesste':
        i = max(range(len(ys)), key=lambda k: ys[k])
        return mit_grafik(zahl(f'Das Streudiagramm zeigt {xn} und {yn}. Welchen x-Wert hat der Punkt mit dem größten y-Wert?', f'Der höchste Punkt liegt bei y = {ys[i]}, sein x-Wert ist {xs[i]}.',
                               'Suche den höchsten Punkt und lies dann seinen x-Wert ab.', xs[i], f'{xs[i]}'), bild)
    if art == 'ueber':
        g = sorted(ys)[len(ys) // 2] // st * st
        if any(abs(y - g) < st / 2 for y in ys): return None
        k = sum(y > g for y in ys)
        return mit_grafik(zahl(f'Das Streudiagramm zeigt {xn} und {yn}. Bei wie vielen Punkten ist der y-Wert größer als {dz(g)}?', f'Über der Höhe {dz(g)} liegen {k} Punkte.',
                               f'Denke dir eine waagrechte Linie bei y = {dz(g)} und zähle die Punkte darüber.', k, f'{k}'), bild)
    if art == 'differenz':
        i, j = R.sample(range(len(xs)), 2)
        i, j = min(i, j), max(i, j)
        return mit_grafik(zahl(f'Das Streudiagramm zeigt {xn} und {yn}. Um wie viel unterscheiden sich etwa die y-Werte der Punkte bei x = {xs[i]} und x = {xs[j]}?',
                               f'y-Werte: etwa {ys[i]} und {ys[j]}. Unterschied: {abs(ys[j] - ys[i])} (Ablesen auf ±{dz(st)} genau genügt).', 'Lies beide y-Werte ab und ziehe den kleineren vom größeren ab.',
                               abs(ys[j] - ys[i]), f'abs({ys[j]} - {ys[i]})', tol=st), bild)
    i = R.randrange(len(xs))
    if ys.count(ys[i]) > 1: return None
    return mit_grafik(zahl(f'Das Streudiagramm zeigt {xn} und {yn}. Ein Punkt liegt auf der Höhe y = {ys[i]}. Welchen x-Wert hat er?', f'Auf Höhe {ys[i]} liegt der Punkt bei x = {xs[i]}.',
                           'Suche den Punkt auf der passenden Höhe und gehe senkrecht nach unten zur x-Achse.', xs[i], f'{xs[i]}'), bild)


ART = {'Schüler': 'einen Schüler', 'Tag': 'einen Tag', 'Auto': 'ein Auto', 'Person': 'eine Person', 'Läufer': 'einen Läufer', 'Fahrt': 'eine Fahrt'}
ZUS = {'stark_pos': 'stark positiv', 'schwach_pos': 'schwach positiv', 'stark_neg': 'stark negativ', 'schwach_neg': 'schwach negativ', 'kein': 'kein Zusammenhang'}
WORT = [  # (Beschreibung, Richtung)
    ('Je länger man ein Handy benutzt, desto leerer wird der Akku.', 'negativ'),
    ('Je mehr Personen in einem Haushalt leben, desto mehr Wasser verbraucht er.', 'positiv'),
    ('Je höher man auf einen Berg steigt, desto kälter wird es meistens.', 'negativ'),
    ('Je mehr Stunden ein Laden geöffnet hat, desto mehr verkauft er.', 'positiv'),
    ('Je schneller ein Auto fährt, desto länger ist sein Bremsweg.', 'positiv'),
    ('Je mehr Kunden vor einer Kasse warten, desto länger dauert es, bis man dran ist.', 'positiv'),
    ('Die Hausnummer und die Körpergröße der Bewohner', 'kein'),
    ('Je mehr Übungsaufgaben man richtig löst, desto weniger Fehler macht man im Test.', 'negativ'),
    ('Der Geburtsmonat und die Note in Mathe', 'kein'),
    ('Je älter ein Kind (bis 12 Jahre), desto größer ist es meistens.', 'positiv'),
]


def g_zusammenhang(s):
    if s == 1 or (s == 2 and R.random() < .5) or (s == 3 and R.random() < .35):
        if s == 1:
            art = R.choice(['stark_pos', 'stark_neg', 'kein'])
        else:
            art = R.choice(list(ZUS))
        sach = R.choice([x for x in SACH if (x[5] > 0) == ('pos' in art) or art == 'kein'])
        d = daten(sach, art)
        if not d: return None
        bild = streubild(sach, *d)
        if s <= 2:
            r = 'positiv' if 'pos' in art else 'negativ' if 'neg' in art else 'kein Zusammenhang'
            return mit_grafik(auswahl('Welche Art von Zusammenhang zeigt das Streudiagramm?', r, ['positiv', 'negativ', 'kein Zusammenhang'],
                                      {'positiv': 'Die Punkte steigen von links nach rechts an: positiver Zusammenhang.', 'negativ': 'Die Punkte fallen von links nach rechts: negativer Zusammenhang.',
                                       'kein Zusammenhang': 'Die Punkte bilden eine Wolke ohne Richtung: kein Zusammenhang.'}[r],
                                      'Fahre mit dem Finger von links nach rechts: Geht es mit den Punkten nach oben, nach unten oder gar nicht?'), bild)
        r = ZUS[art]
        return mit_grafik(auswahl('Beschreibe den Zusammenhang im Streudiagramm möglichst genau.', r, list(ZUS.values()),
                                  f'Richtung: {"steigend" if "pos" in art else "fallend" if "neg" in art else "keine"}. ' +
                                  ('Die Punkte liegen eng an einer gedachten Geraden: stark.' if 'stark' in art else 'Die Punkte streuen deutlich um eine gedachte Gerade: schwach.' if 'schwach' in art else 'Keine erkennbare Gerade.'),
                                  'Erst die Richtung (steigend/fallend), dann die Stärke (eng an einer Linie oder breit gestreut).'), bild)
    if s == 2:
        satz, ri = R.choice(WORT)
        r = {'positiv': 'positiver Zusammenhang', 'negativ': 'negativer Zusammenhang', 'kein': 'kein Zusammenhang'}[ri]
        return auswahl(f'Welche Art von Zusammenhang erwartest du? „{satz}“', r, ['positiver Zusammenhang', 'negativer Zusammenhang', 'kein Zusammenhang'],
                       {'positiv': 'Wächst die eine Größe, wächst auch die andere: positiv.', 'negativ': 'Wächst die eine Größe, wird die andere kleiner: negativ.',
                        'kein': 'Die beiden Größen haben nichts miteinander zu tun: kein Zusammenhang.'}[ri],
                       'Frage dich: Wenn die erste Größe wächst – was passiert mit der zweiten?')
    # s == 3: zwei Diagramme vergleichen in Worten (Tabelle)
    sach = R.choice(SACH[:3])
    a1, a2 = R.sample(['stark_pos', 'schwach_pos'] if sach[5] > 0 else ['stark_neg', 'schwach_neg'], 2)
    d1, d2 = daten(sach, a1, n=7), daten(sach, a2, n=7)
    if not d1 or not d2: return None
    bild = streubild(sach, d1[0] + d2[0], d1[1] + d2[1])
    for i in range(len(d1[0]), len(bild['punkte'])): bild['punkte'][i]['offen'] = True
    tab = bild
    staerker = 'Gruppe 1' if 'stark' in a1 else 'Gruppe 2'
    return mit_grafik(auswahl(f'Für zwei Gruppen wurden {sach[0]} (x) und {sach[2]} (y) erfasst. Gruppe 1: gefüllte Punkte, Gruppe 2: hohle Punkte. In welcher Gruppe ist der Zusammenhang stärker?',
                              staerker, ['Gruppe 1', 'Gruppe 2', 'In beiden gleich stark'],
                              f'Die Punkte von {staerker} liegen enger an einer Geraden (Korrelation r ≈ {dz(round(korrelation(*(d1 if staerker == "Gruppe 1" else d2)), 2))} gegenüber r ≈ {dz(round(korrelation(*(d2 if staerker == "Gruppe 1" else d1)), 2))}).',
                              'Schau, welche Punktart enger an einer gedachten Geraden liegt.'), tab)


def g_gerade(s):
    m = R.choice([2, 3, 4, 5, 6, -2, -3, -4]) if s > 1 else R.choice([2, 3, 4, 5])
    t = R.choice([10, 20, 30, 40, 50]) if m > 0 else R.choice([60, 70, 80])
    xn, xe, yn, ye, x1 = R.choice([('Übungszeit', 'h', 'Punkte', '', 'Stunde mehr Übungszeit'), ('Werbeausgaben', 'Tausend €', 'Verkäufe', 'Stück', '1000 € mehr Werbung'),
                                   ('Temperatur', '°C', 'Besucher', '', 'Grad mehr')])
    if m < 0: xn, xe, yn, ye, x1 = R.choice([('Alter des Geräts', 'Jahre', 'Wert', '€', 'Jahr mehr Alter'), ('Nutzungsdauer', 'h', 'Akkustand', '%', 'Stunde mehr Nutzung'),
                                            ('Fehlstunden', 'h', 'Punkte', '', 'Fehlstunde mehr')])
    art = R.choice({1: ['rechnen', 'rechnen', 'ablesen'], 2: ['rechnen', 'ablesen', 'steigung'], 3: ['umkehr', 'extrapol', 'steigung']}[s])
    xs = sorted(R.sample(range(1, 11), 7))
    ys = [m * x + t + R.choice([-3, -2, -1, 1, 2, 3]) for x in xs]
    bild = {'typ': 'koordinaten', 'x': [0, 12], 'y': [0, max(max(ys), m * 12 + t) + 10 if m > 0 else max(ys) + 10],
            'punkte': [{'x': x, 'y': y} for x, y in zip(xs, ys)], 'graphen': [{'art': 'linear', 'm': m, 't': t, 'bereich': [0, 12]}],
            'name_x': xn + (f' in {xe}' if xe else ''), 'name_y': yn + (f' in {ye}' if ye else ''), 'schritt_y': 10}
    gl = f'y = {poly(m, t)}'
    if art == 'rechnen':
        x = R.choice([v for v in range(1, 12) if v not in xs])
        return mit_grafik(zahl(f'Die Ausgleichsgerade hat die Gleichung {gl}. Schätze y für x = {x}.', f'y = {kl(m)} · {x} {plus(t)} = {m * x + t}.',
                               'Setze den x-Wert in die Gleichung ein.', m * x + t, f'{m} * {x} + {t}'), bild)
    if art == 'ablesen':
        x = R.choice([2, 4, 6, 8, 10])
        return mit_grafik(zahl(f'Lies an der Ausgleichsgeraden ab: Welcher y-Wert gehört zu x = {x}?', f'Bei x = {x} trifft man die Gerade bei y = {m * x + t} (Gleichung {gl}).',
                               'Gehe von x senkrecht nach oben bis zur Geraden, dann waagrecht zur y-Achse.', m * x + t, f'{m} * {x} + {t}', tol=5), bild)
    if art == 'steigung':
        r = f'Pro {x1} {"steigt" if m > 0 else "sinkt"} der Wert „{yn}“ um etwa {abs(m)}.'
        return mit_grafik(auswahl(f'x: {xn}' + (f' in {xe}' if xe else '') + f', y: {yn}. Die Ausgleichsgerade hat die Gleichung {gl}. Was bedeutet die Zahl {dz(m)}?', r,
                                  [f'Bei x = 0 ist der Wert „{yn}“ gleich {abs(m)}.', f'Pro {x1} {"sinkt" if m > 0 else "steigt"} der Wert „{yn}“ um etwa {abs(m)}.', f'Es wurden {abs(m)} Werte gemessen.'],
                                  f'Die Steigung {m} sagt, wie sich y ändert, wenn x um 1 wächst. Der Achsenabschnitt {t} ist der Wert bei x = 0.',
                                  'Welche Zahl in y = m · x + t gibt die Änderung pro Schritt an?'), bild)
    if art == 'umkehr':
        x = R.choice([v for v in range(1, 12) if v not in xs])
        y = m * x + t
        return mit_grafik(zahl(f'Die Ausgleichsgerade hat die Gleichung {gl}. Für welchen x-Wert schätzt sie y = {y}?', f'{y} = {kl(m)} · x {plus(t)} ⇒ {kl(m)} · x = {y - t} ⇒ x = {x}.',
                               'Setze y ein und löse die Gleichung nach x auf.', x, f'({y} - {t}) / {m}'), bild)
    x = R.choice([30, 40, 50, 60]) if m > 0 else R.choice([25, 30, 40])
    y = m * x + t
    r = 'Nein – das liegt weit außerhalb der Messwerte (Extrapolation).'
    return mit_grafik(auswahl(f'Gemessen wurde nur für x zwischen 1 und 10. Die Ausgleichsgerade {gl} liefert für x = {x} den Wert y = {dz(y)}. Ist diese Schätzung verlässlich?', r,
                              ['Ja – die Gleichung gilt immer.', 'Ja – weil die Gerade durch viele Punkte geht.', 'Nein – man darf nie mit einer Ausgleichsgeraden rechnen.'],
                              f'x = {x} liegt weit außerhalb von 1 bis 10. Ob der Zusammenhang dort noch gilt, weiß niemand' + (f' (ein negativer Wert {dz(y)} wäre sogar unmöglich).' if y < 0 else '.'),
                              'Liegt der x-Wert innerhalb oder außerhalb der gemessenen Daten?'), bild)


def g_ausreisser(s):
    m = R.choice([4, 5, 6, -4, -5])
    t = 20 if m > 0 else 80
    n = R.randint(6, 8)
    xs = sorted(R.sample(range(1, 11), n))
    ys = [m * x + t + R.choice([-2, -1, 0, 1, 2]) for x in xs]
    k = R.randrange(1, n - 1) if s > 1 else R.randrange(n)
    weg = R.choice([25, 30, 35]) * R.choice([1, -1])
    if ys[k] + weg < 5: weg = abs(weg)
    ys[k] += weg
    namen = 'ABCDEFGH'[:n]
    bild = streubild(('x', '', 'y', '', (0, 11), m, t, 2, ''), xs, ys, namen=list(namen), x_rand=(0, 11))
    if s == 1:
        return mit_grafik(auswahl('Welcher Punkt ist ein Ausreißer?', f'Punkt {namen[k]}', [f'Punkt {c}' for c in namen if c != namen[k]][:3] if True else [],
                                  f'Alle Punkte liegen auf einem gemeinsamen Muster, nur {namen[k]} liegt um etwa {abs(weg)} weit daneben.',
                                  'Suche den Punkt, der nicht zum Muster der anderen passt.'), bild)
    if s == 2:
        extrem = max(range(n), key=lambda i: ys[i]) if m > 0 else min(range(n), key=lambda i: ys[i])
        falsch = [f'Punkt {namen[extrem]}'] if extrem != k else []
        falsch += [f'Punkt {c}' for c in namen if c != namen[k] and f'Punkt {c}' not in falsch]
        return mit_grafik(auswahl('Ein Punkt passt nicht zum Muster. Welcher?', f'Punkt {namen[k]}', falsch[:3],
                                  f'{namen[k]} liegt bei ({xs[k]} | {ys[k]}); nach dem Muster der Nachbarn wären etwa {m * xs[k] + t} zu erwarten.',
                                  'Nicht der höchste oder tiefste Punkt ist gesucht, sondern der mit dem größten Abstand zum Muster.'), bild)
    art = R.choice(['wirkung', 'erwartung'])
    if art == 'erwartung':
        return mit_grafik(zahl(f'Punkt {namen[k]} ist ein Ausreißer. Die anderen Punkte liegen fast genau auf y = {poly(m, t)}. Welcher y-Wert wäre bei x = {xs[k]} zu erwarten?',
                               f'y = {kl(m)} · {xs[k]} {plus(t)} = {m * xs[k] + t}. Gemessen wurden aber {ys[k]}.', 'Setze den x-Wert des Ausreißers in die Gleichung ein.',
                               m * xs[k] + t, f'{m} * {xs[k]} + {t}'), bild)
    r = 'Prüfen, ob ein Mess- oder Schreibfehler vorliegt, bevor man die Ausgleichsgerade zeichnet.'
    return mit_grafik(auswahl(f'Punkt {namen[k]} ist ein Ausreißer. Was ist sinnvoll?', r,
                              ['Den Punkt einfach löschen, weil er stört.', 'Die Ausgleichsgerade genau durch diesen Punkt legen.', 'Daraus schließen, dass es keinen Zusammenhang gibt.'],
                              'Ein Ausreißer kann ein Fehler oder ein echter Sonderfall sein. Erst prüfen, dann entscheiden – und nie die Gerade nach ihm ausrichten.',
                              'Was könnte der Grund für den Ausreißer sein?'), bild)


KAUSAL = [  # (Beobachtung, richtige Erklärung, falsche Erklärungen)
    ('In Städten mit mehr Feuerwehrleuten gibt es mehr Brände.', 'Größere Städte haben mehr Häuser (mehr Brände) und brauchen mehr Feuerwehrleute.',
     ['Feuerwehrleute verursachen Brände.', 'Brände locken Feuerwehrleute an, deshalb ziehen sie dorthin.']),
    ('An Tagen mit hohem Eisverkauf gibt es mehr Badeunfälle.', 'An heißen Tagen wird mehr Eis gegessen und mehr gebadet.',
     ['Eis essen macht beim Schwimmen unvorsichtig.', 'Nach Badeunfällen kaufen Menschen mehr Eis.']),
    ('Kinder mit größeren Schuhgrößen können besser rechnen.', 'Ältere Kinder haben größere Füße und haben schon mehr Mathe gelernt.',
     ['Große Füße machen schlau.', 'Wer gut rechnet, bekommt größere Füße.']),
    ('Wer mehr Fernsehen schaut, hat oft schlechtere Noten.', 'Das zeigt nur einen Zusammenhang; ob Fernsehen die Ursache ist, muss man erst genauer untersuchen.',
     ['Fernsehen ist sicher die Ursache für schlechte Noten.', 'Schlechte Noten sind sicher die Ursache für mehr Fernsehen.']),
    ('In Monaten mit mehr verkauften Regenschirmen werden auch mehr Gummistiefel verkauft.', 'In regnerischen Monaten braucht man beides.',
     ['Regenschirme verursachen den Kauf von Gummistiefeln.', 'Gummistiefel machen Regen.']),
    ('Länder mit mehr Smartphones haben eine höhere Lebenserwartung.', 'Reichere Länder haben mehr Smartphones und eine bessere Gesundheitsversorgung.',
     ['Smartphones verlängern das Leben.', 'Wer lange lebt, kauft mehr Smartphones.']),
    ('Wer öfter ins Krankenhaus geht, ist im Durchschnitt kränker.', 'Kranke Menschen gehen ins Krankenhaus, weil sie krank sind – nicht umgekehrt.',
     ['Krankenhäuser machen krank.', 'Gesunde Menschen dürfen nicht ins Krankenhaus.']),
    ('Schulen mit größeren Bibliotheken haben bessere Abschlussnoten.', 'Gut ausgestattete Schulen haben oft auch andere Vorteile, etwa kleinere Klassen.',
     ['Bücher im Regal verbessern automatisch die Noten.', 'Gute Noten lassen die Bibliothek wachsen.']),
    ('In Wochen mit mehr verkauften Heizlüftern gibt es mehr Erkältungen.', 'In kalten Wochen braucht man Heizlüfter und erkältet sich häufiger.',
     ['Heizlüfter verbreiten Erkältungen.', 'Erkältete Menschen kaufen Heizlüfter, um gesund zu werden.']),
    ('Je mehr Besucher ein Freibad hat, desto mehr Pommes werden am Kiosk verkauft.', 'Mehr Besucher bedeuten mehr hungrige Gäste – hier ist ein direkter Grund plausibel.',
     ['Pommes locken Besucher ins Freibad.', 'Es gibt keinen Zusammenhang.']),
    ('Spieler mit mehr Trainingseinheiten gewinnen öfter.', 'Training kann helfen, aber auch Talent und Motivation spielen mit – die Daten allein beweisen es nicht.',
     ['Training ist sicher der einzige Grund.', 'Wer gewinnt, muss nicht mehr trainieren.']),
]


DRITTE = [
    ('In Wochen, in denen mehr Sonnenbrillen verkauft werden, gibt es mehr Sonnenbrand-Fälle.', 'das sonnige Wetter', ['die Farbe der Sonnenbrillen', 'der Preis von Sonnencreme', 'die Zahl der Apotheken']),
    ('Schüler, die mehr Nachhilfestunden haben, haben im Schnitt schlechtere Noten.', 'vorhandene Lernschwierigkeiten', ['die Länge der Nachhilfestunde', 'die Anzahl der Lehrer', 'das Wetter am Prüfungstag']),
    ('Städte mit mehr Ampeln haben mehr Verkehrsunfälle.', 'die Größe der Stadt und der Verkehr', ['die Farbe der Ampeln', 'die Anzahl der Fahrradwege', 'das Alter der Ampeln']),
    ('Familien mit mehr Autos haben größere Wohnungen.', 'das Einkommen der Familie', ['die Farbe der Autos', 'die Anzahl der Fenster', 'die Länge des Arbeitswegs']),
    ('In Jahren mit mehr Geburten sieht man mehr Störche (Beispiel aus einer alten Statistik).', 'ländliche Gegenden mit mehr Familien und mehr Nistplätzen', ['die Flugstrecke der Störche', 'die Zahl der Krankenhäuser in der Stadt', 'die Länge des Winters']),
    ('Wer mehr Kaffee trinkt, hat im Durchschnitt mehr graue Haare.', 'das Alter', ['die Kaffeesorte', 'die Haarlänge', 'die Tasse']),
    ('Kinder, die mehr Zeit im Freien verbringen, sind im Durchschnitt seltener kurzsichtig.', 'das Tageslicht draußen und weniger Nahsehen', ['die Farbe der Kleidung', 'die Schuhgröße', 'der Geburtsmonat']),
    ('Restaurants mit mehr Tischen haben mehr Personal.', 'die Größe des Restaurants', ['die Farbe der Tischdecken', 'die Länge der Speisekarte', 'die Öffnungszeit am Sonntag']),
    ('Je mehr Hausaufgaben eine Klasse bekommt, desto mehr Bleistifte werden gekauft.', 'die Menge an schriftlicher Arbeit insgesamt', ['die Farbe der Hefte', 'die Größe des Klassenzimmers', 'das Alter der Lehrkraft']),
]


def g_kausal(s):
    wahl_ = R.choice({1: ['erkl'], 2: ['erkl', 'beweis', 'dritte'], 3: ['rest']}[s])
    if wahl_ == 'dritte':
        s = 3
    if wahl_ == 'erkl':
        beob, r, fs = R.choice(KAUSAL)
        return auswahl(f'Beobachtung: „{beob}“ Welche Erklärung ist am vernünftigsten?', r, fs + ['Das ist ein Messfehler, es gibt keinen Zusammenhang.'],
                       f'{r} Die Korrelation allein beweist keine Ursache.', 'Gibt es eine dritte Größe, die beide Werte beeinflusst?')
    if wahl_ == 'beweis':
        beob, r, fs = R.choice(KAUSAL)
        rr = 'Nein, eine Korrelation beweist keine Ursache.'
        return auswahl(f'„{beob}“ Beweist das, dass das eine das andere verursacht?', rr,
                       ['Ja, weil der Zusammenhang positiv ist.', 'Ja, wenn die Punkte eng an einer Geraden liegen.', 'Nein, weil es keinen Zusammenhang gibt.'],
                       f'Die Daten zeigen nur, dass beides gemeinsam auftritt. Erklärung: {r}', 'Unterscheide „tritt gemeinsam auf“ und „ist die Ursache“.')
    art = 'dritte' if wahl_ == 'dritte' else R.choice(['experiment', 'richtung', 'stark', 'dritte', 'dritte', 'dritte'])
    if art == 'dritte':
        beob, dritte, falsch = R.choice(DRITTE)
        return auswahl(f'„{beob}“ Welche dritte Größe erklärt diesen Zusammenhang am besten?', dritte, falsch,
                       f'{dritte} beeinflusst beide beobachteten Größen. Deshalb hängen sie zusammen, ohne dass die eine die andere verursacht.',
                       'Suche eine Größe, die beide Beobachtungen gleichzeitig beeinflusst.')
    if art == 'experiment':
        r = 'Zwei gleich starke Gruppen bilden, nur eine Gruppe übt täglich 10 Minuten zusätzlich, dann beide Ergebnisse vergleichen.'
        return auswahl('Eine Schule vermutet: „Tägliches Kopfrechentraining verbessert die Mathenoten.“ Wie kann man das am besten überprüfen?', r,
                       ['Die Kinder mit den besten Noten fragen, ob sie Kopfrechnen üben.', 'Ein Streudiagramm Übungszeit gegen Note zeichnen – zeigt es einen Zusammenhang, ist es bewiesen.',
                        'Alle Kinder üben, und man schaut, ob die Noten im nächsten Jahr gut sind.'],
                       'Nur ein Vergleich mit einer Kontrollgruppe, in der sonst alles gleich ist, zeigt eine Ursache.',
                       'Wie kannst du andere Einflüsse ausschließen?')
    if art == 'richtung':
        r = 'Es könnte auch umgekehrt sein: Wer gesund ist, kann mehr Sport treiben.'
        return auswahl('In einer Umfrage treiben gesündere Menschen mehr Sport. Jemand folgert: „Sport macht gesund.“ Welcher Einwand ist berechtigt?', r,
                       ['Es gibt keinen Zusammenhang zwischen Sport und Gesundheit.', 'Die Korrelation ist negativ.', 'Eine Umfrage kann keine Zahlen liefern.'],
                       'Die Richtung der Ursache ist aus den Daten nicht ablesbar. Vielleicht gilt beides, vielleicht nur eine Richtung.',
                       'Könnte die Ursache auch in die andere Richtung wirken?')
    r = 'Nein. Auch ein sehr starker Zusammenhang kann durch eine dritte Größe oder Zufall entstehen.'
    return auswahl('Ein Streudiagramm zeigt einen sehr starken positiven Zusammenhang zwischen zwei Größen. Ist damit eine Ursache bewiesen?', r,
                   ['Ja, bei einem sehr starken Zusammenhang immer.', 'Ja, wenn mehr als 10 Punkte gemessen wurden.', 'Nein, weil starke Zusammenhänge immer Zufall sind.'],
                   'Die Stärke sagt nur, wie eng die Punkte an einer Geraden liegen – nicht, warum.', 'Was sagt die Stärke einer Korrelation aus – und was nicht?')


GEN = {'ablesen': g_ablesen, 'zusammenhang': g_zusammenhang, 'gerade': g_gerade, 'ausreisser': g_ausreisser, 'kausal': g_kausal}

bauen('daten.zweidimensional',
      'Zweidimensionale Daten im Streudiagramm darstellen und lesen, Zusammenhänge beschreiben, mit der Ausgleichsgeraden schätzen und Korrelation von Ursache unterscheiden.',
      ['Streudiagramm (scatter graph): ein Punkt pro Objekt, x nach rechts, y nach oben.',
       'Steigend = positiv, fallend = negativ, Wolke = kein Zusammenhang; eng an einer Linie = stark.',
       'Ausgleichsgerade (line of best fit): mitten durch die Punkte – Schätzen nur innerhalb der Daten.',
       'Korrelation ist keine Ursache (correlation is not causation) – an eine dritte Größe denken.'],
      [('Darstellen und lesen', ['ablesen', 'zusammenhang']), ('Auswerten', ['gerade', 'ausreisser']), ('Deuten', ['kausal'])],
      ETAPPEN, GEN,
      offen=['Ausgleichsgerade wird gegeben (Gleichung und Zeichnung), nicht selbst berechnet: Regressionsrechnung ist nicht Stoff von MYP 3. Den Korrelationskoeffizienten r nur im Lösungsweg einer Vergleichsaufgabe erwähnt.',
             'App-Wunsch (optional): Das Kind kann die Ausgleichsgerade noch nicht selbst einzeichnen; Aufgaben dazu fehlen deshalb.'],
      vertiefung=[])
