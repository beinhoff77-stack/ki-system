#!/usr/bin/env python3
"""Thema groessen.indirekt – Indirekte Proportionalität (Gymnasium Bayern, Klasse 8). Nachbau Runde 5.

Erkennen (doppelt → halb), Vervielfachen in Tabellen, Produktgleichheit, Dreisatz, Hyperbel als Graph,
Abgrenzung zu direkt proportional und „weder noch“, Sachaufgaben.
"""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _nachbau import A, Z, baue, cz, dez, mit_bild, tabelle, zt  # noqa: E402

META = {'thema_schluessel': 'groessen.indirekt', 'thema_id': 93, 'block_id': 107, 'klasse': {'gym_by': 8, 'rs_by': 7}}


def tab(xn, yn, xs, ys):
    """Waagrechte Wertetabelle; None wird als „?“ gezeigt."""
    f = lambda v: '?' if v is None else zt(Fr(v))
    return tabelle([xn] + [f(x) for x in xs], [[yn] + [f(y) for y in ys]])


def hyp(k, x0=Fr(1, 2), x1=None, punkte=(), weitere=(), xmax=None, ymax=None):
    xmax = xmax or 12
    ymax = ymax or 12
    g = {'typ': 'koordinaten', 'x': [0, xmax], 'y': [0, ymax],
         'graphen': [{'art': 'hyperbel', 'a': int(k) if Fr(k).denominator == 1 else float(k), 'b': 0, 'c': 0, 'bereich': [round(float(Fr(k) / ymax), 2), xmax]}] + list(weitere)}
    if punkte: g['punkte'] = [dict(p) for p in punkte]
    return g


def endlich(x):
    return dez(Fr(x)) is not None


ETAPPEN = [
    {'lernziel': 'erkennen', 'titel': 'Was heißt indirekt proportional?',
     'regel': 'Zwei Größen sind ⟦indirekt proportional⟧, wenn zum Doppelten der einen Größe die ⟦Hälfte⟧ der anderen gehört, zum Dreifachen ein ⟦Drittel⟧ usw. '
              '„Je mehr, desto weniger“ allein reicht dafür ⟦nicht⟧ – es muss genau im umgekehrten Verhältnis weniger werden.',
     'schritte': ['Ein Zimmer streichen: 2 Personen brauchen 6 Stunden.',
                  'Doppelt so viele Personen (4) brauchen halb so lange: 6 h : 2 = ⟦3 h⟧. Dreimal so viele (6) brauchen ein Drittel: ⟦2 h⟧.'],
     'fehler': '„Je älter ein Auto, desto weniger ist es wert“ – trotzdem nicht indirekt proportional: Ein 1 Jahr altes Auto ist z. B. 20 000 € wert, ein 2 Jahre altes 17 000 €. '
               'Doppeltes Alter, aber ⟦nicht halber Wert⟧ (das wären 10 000 €).',
     'bild': tabelle(['Personen', '2', '4', '6'], [['Zeit in h', '6', '3', '2']])},
    {'lernziel': 'vervielfachen', 'titel': 'Doppelt so viele – halb so lange',
     'regel': 'In einer Tabelle einer indirekten Proportionalität gilt: Multiplizierst du x mit einer Zahl, musst du y durch ⟦dieselbe Zahl teilen⟧. '
              'Teilst du x, ⟦multiplizierst⟧ du y.',
     'schritte': ['Ein Futtervorrat reicht für 6 Pferde 20 Tage. Wie lange reicht er für 3 Pferde?',
                  '6 : 2 = 3 Pferde, also halb so viele. Dann reicht das Futter doppelt so lange: 20 · 2 = ⟦40 Tage⟧.'],
     'fehler': 'Mit derselben Rechnung auf beiden Seiten weitermachen wie bei direkter Proportionalität: 3 Pferde → 20 : 2 = 10 Tage ist falsch. '
               'Weniger Pferde fressen weniger, das Futter reicht also ⟦länger⟧: 40 Tage.',
     'bild': tabelle(['Pferde', '6', '3'], [['Tage', '20', '?']])},
    {'lernziel': 'produkt', 'titel': 'Produktgleichheit prüfen',
     'regel': 'Bei einer indirekten Proportionalität ist das ⟦Produkt x · y⟧ für alle Wertepaare ⟦gleich⟧. Dieses Produkt ist die Gesamtmenge, die aufgeteilt wird. '
              'Fehlende Werte findest du mit y = ⟦Produkt : x⟧.',
     'schritte': ['Ein Gewinn wird gleichmäßig verteilt: 2 Personen bekommen je 60 €, 3 Personen je 40 €, 5 Personen je 24 €.',
                  'Produkte: 2 · 60 = 120, 3 · 40 = 120, 5 · 24 = 120. Alle gleich – der Gewinn ist ⟦120 €⟧, die Zuordnung ist indirekt proportional.',
                  'Bei 8 Personen: 120 : 8 = ⟦15 €⟧ pro Person.'],
     'fehler': 'Nur zwei Paare prüfen: 2 · 60 = 120 und 4 · 30 = 120, aber 6 · 25 = 150. Ein einziges abweichendes Produkt genügt – dann ist die Zuordnung ⟦nicht⟧ indirekt proportional. Prüfe ⟦alle⟧ Paare.',
     'bild': tabelle(['Personen', '2', '3', '5', '8'], [['€ pro Person', '60', '40', '24', '?']])},
    {'lernziel': 'dreisatz', 'titel': 'Dreisatz bei indirekter Proportionalität',
     'regel': 'Dreisatz in drei Schritten: ⟦gegebener Wert⟧ → ⟦eine Einheit⟧ → ⟦gesuchter Wert⟧. Bei indirekter Proportionalität wird beim Schritt zur Einheit ⟦multipliziert⟧, '
              'nicht geteilt – eine Pumpe braucht ja länger als sechs.',
     'schritte': ['6 gleiche Pumpen leeren ein Becken in 10 Stunden. Wie lange brauchen 4 Pumpen?',
                  '1 Pumpe braucht 6-mal so lange: 10 h · 6 = 60 h.',
                  '4 Pumpen brauchen ein Viertel davon: 60 h : 4 = ⟦15 h⟧.'],
     'probe': '6 · 10 = 60 und 4 · 15 = 60 ✓',
     'fehler': 'Wie bei direkter Proportionalität rechnen: 10 h : 6 · 4 ≈ 6,7 h. Weniger Pumpen können aber nicht schneller sein! '
               'Frage dich vorher: ⟦Mehr oder weniger?⟧ Weniger Pumpen → ⟦mehr⟧ Zeit.'},
    {'lernziel': 'graph', 'titel': 'Der Graph: eine Hyperbel',
     'regel': 'Die Punkte (x | y) einer indirekten Proportionalität liegen auf einer ⟦Hyperbel⟧ mit y = k : x, wobei k das konstante Produkt ist. '
              'Der Graph geht ⟦nicht durch den Ursprung⟧ und kommt den Achsen immer näher, ohne sie zu berühren.',
     'schritte': ['Ein Rechteck soll 12 cm² groß sein. Breite x, Länge y: x · y = 12, also y = 12 : x.',
                  'Wertepaare: (1 | 12), (2 | 6), (3 | 4), (4 | 3), (6 | 2). Verbunden ergeben sie eine gebogene Kurve: die ⟦Hyperbel⟧.'],
     'fehler': 'Die Punkte mit geraden Strecken verbinden oder die Kurve bis zur Achse zeichnen. Bei x = 0 gäbe es kein Rechteck mit 12 cm² – die Kurve ⟦berührt die Achsen nie⟧.',
     'bild': {'typ': 'koordinaten', 'x': [0, 13], 'y': [0, 13], 'name_x': 'Breite x in cm', 'name_y': 'Länge y in cm',
              'graphen': [{'art': 'hyperbel', 'a': 12, 'b': 0, 'c': 0, 'bereich': [0.95, 13]}],
              'punkte': [{'x': 1, 'y': 12}, {'x': 2, 'y': 6}, {'x': 3, 'y': 4}, {'x': 4, 'y': 3}, {'x': 6, 'y': 2}]}},
    {'lernziel': 'unterscheiden', 'titel': 'Direkt, indirekt oder keins von beiden?',
     'regel': 'Prüfe mit der Tabelle: Ist der ⟦Quotient y : x⟧ immer gleich, ist die Zuordnung ⟦direkt⟧ proportional. Ist das ⟦Produkt x · y⟧ immer gleich, ist sie ⟦indirekt⟧ proportional. '
              'Ist beides nicht so, ist sie ⟦weder noch⟧ – dann hilft kein Dreisatz.',
     'schritte': ['Taxi: 2 km kosten 8 €, 4 km kosten 12 €, 6 km kosten 16 €.',
                  'Quotienten: 8 : 2 = 4, 12 : 4 = 3 – nicht gleich. Produkte: 16, 48 – nicht gleich.',
                  'Also ⟦weder noch⟧: Die Grundgebühr verhindert die Proportionalität.'],
     'fehler': '„y wird größer, also direkt proportional“ – beim Taxi wird der Preis größer, aber doppelte Strecke kostet nicht doppelt so viel (4 km: 12 € statt 16 €). '
               'Entscheide ⟦mit Rechnung⟧, nicht mit „je mehr, desto mehr“.',
     'bild': tabelle(['Strecke in km', '2', '4', '6'], [['Preis in €', '8', '12', '16']])},
    {'lernziel': 'sach', 'titel': 'Sachaufgaben lösen',
     'regel': 'Lies genau: Welche zwei Größen hängen zusammen? Frage dich: ⟦Doppelt so viel – doppelt oder halb?⟧ Erst dann wählst du den Rechenweg. '
              'Prüfe am Ende, ob das Ergebnis ⟦sinnvoll⟧ ist.',
     'schritte': ['Ein Auto braucht für eine Strecke bei 80 km/h genau 3 h. Wie lange braucht es bei 120 km/h?',
                  'Schneller → weniger Zeit: indirekt. Produkt: 80 · 3 = 240 (das ist die Strecke in km).',
                  '240 : 120 = ⟦2 h⟧.'],
     'probe': '120 km/h · 2 h = 240 km ✓',
     'fehler': 'Bei Aufgaben mit festem Grundbetrag (Eintritt + Fahrten, Taxi) den Dreisatz verwenden. Kostet 1 Fahrt mit Eintritt 7 €, kosten 3 Fahrten nicht 21 €, '
               'wenn der Eintritt nur ⟦einmal⟧ bezahlt wird.'},
]


# ---------------- Situationen ----------------
def situation(R, art):
    if art == 'indirekt':
        n = R.choice(['pers', 'tempo', 'pumpen', 'futter', 'rechteck', 'busse'])
        if n == 'pers': return f'Ein Lottogewinn von {R.choice([600, 1200, 2400])} € wird gleichmäßig verteilt: Anzahl der Personen → Betrag pro Person'
        if n == 'tempo': return f'Eine Strecke von {R.choice([120, 180, 240])} km: Geschwindigkeit → Fahrzeit'
        if n == 'pumpen': return 'Gleich starke Pumpen leeren ein Becken: Anzahl der Pumpen → benötigte Zeit'
        if n == 'futter': return f'Ein Heuvorrat für {R.choice(["Pferde", "Kühe", "Schafe"])}: Anzahl der Tiere → Tage, die der Vorrat reicht'
        if n == 'rechteck': return f'Rechtecke mit {R.choice([24, 36, 48])} cm² Flächeninhalt: Breite → Länge'
        return f'{R.choice([120, 180, 240])} Kinder fahren mit gleich vollen Bussen: Anzahl der Busse → Kinder pro Bus'
    if art == 'direkt':
        n = R.choice(['brezen', 'benzin', 'strecke', 'stoff'])
        if n == 'brezen': return 'Brezen beim Bäcker: Anzahl → Preis'
        if n == 'benzin': return 'Tanken: Liter Benzin → Preis'
        if n == 'strecke': return f'Ein Zug fährt gleichmäßig {R.choice([80, 120, 160])} km/h: Fahrzeit → Strecke'
        return 'Stoff vom Meter: Länge → Preis'
    n = R.choice(['taxi', 'kerze', 'auto', 'orchester', 'alter', 'handy'])
    if n == 'taxi': return 'Taxi mit Grundgebühr: Strecke → Preis'
    if n == 'kerze': return 'Eine Kerze brennt ab: Brenndauer → Restlänge der Kerze'
    if n == 'auto': return 'Gebrauchtwagen: Alter → Wert'
    if n == 'orchester': return 'Ein Musikstück: Anzahl der Musiker → Dauer des Stücks'
    if n == 'alter': return 'Ein Kind wächst: Alter → Körpergröße'
    return 'Handyvertrag mit Grundgebühr: Gesprächsminuten → Monatsrechnung'


GRUND = {'Kerze': 'Je länger sie brennt, desto kürzer – aber doppelte Brenndauer heißt nicht halbe Länge.',
         'Gebrauchtwagen': 'Je älter, desto weniger wert – aber doppeltes Alter heißt nicht halber Wert.',
         'Musikstück': 'Mehr Musiker spielen das Stück nicht schneller; die Dauer bleibt gleich.',
         'Kind': 'Ein Kind wird größer, aber mit doppeltem Alter nicht doppelt so groß.',
         'Taxi': 'Die Grundgebühr zahlt man immer; doppelte Strecke kostet nicht doppelt so viel.',
         'Handyvertrag': 'Die Grundgebühr zahlt man immer; doppelte Minuten kosten nicht doppelt so viel.'}


def grund(text):
    for k, v in GRUND.items():
        if text.startswith(k) or k in text.split(':')[0]: return v
    return ''


def g_erkennen(R, s):
    if s == 1:
        art = R.choice(['indirekt', 'indirekt', 'direkt', 'weder'])
        t = situation(R, art)
        richtig = {'indirekt': 'Ja: doppelt so viel → halb so viel.', 'direkt': 'Nein: doppelt so viel → doppelt so viel.',
                   'weder': 'Nein: weder doppelt → halb noch doppelt → doppelt.'}[art]
        falsch = [x for x in ['Ja: doppelt so viel → halb so viel.', 'Nein: doppelt so viel → doppelt so viel.', 'Nein: weder doppelt → halb noch doppelt → doppelt.'] if x != richtig]
        w = {'indirekt': 'Doppelt so viel von der ersten Größe → die Hälfte von der zweiten. Das ist indirekt proportional.',
             'direkt': 'Doppelt so viel → doppelt so viel. Das ist direkt proportional, nicht indirekt.',
             'weder': (grund(t) + ' Weder halb noch doppelt: weder noch.').strip()}[art]
        return A(R, f'Ist diese Zuordnung indirekt proportional? {t}.', richtig, falsch, w,
                 'Was passiert mit der zweiten Größe, wenn die erste verdoppelt wird?')
    if s == 2:
        art = R.choice(['paar', 'paar', 'welche'])
        if art == 'paar':
            x, y = R.choice([2, 3, 4, 5]), R.choice([6, 8, 12, 15, 18, 24])
            k = R.choice([2, 3])
            ist = R.random() < .5
            y2 = Fr(y, k) if ist else y - R.choice([1, 2, 3])
            if Fr(y2) == Fr(y, k) and not ist or not endlich(y2): return g_erkennen(R, s)
            text = f'{x} Personen brauchen für eine Arbeit {y} Stunden, {k * x} Personen brauchen {zt(y2)} Stunden. Kann das indirekt proportional sein?'
            if ist:
                return A(R, text, f'Ja: {k}-mal so viele Personen, {"die Hälfte" if k == 2 else "ein Drittel"} der Zeit.',
                         ['Nein: Es müsste doppelt so lange dauern.', f'Nein: Die Zeit müsste um {k} h kürzer sein.'],
                         f'{k * x} ist das {k}-Fache von {x}. {y} : {k} = {zt(y2)}. Das Produkt bleibt gleich: {x} · {y} = {k * x} · {zt(y2)} = {x * y}.',
                         'Wievielfach sind die Personen? Wie hat sich die Zeit verändert?')
            return A(R, text, f'Nein: Bei {k}-mal so vielen Personen müssten es {zt(Fr(y, k))} Stunden sein.',
                     ['Ja: Mehr Personen brauchen weniger Zeit.', f'Ja: Die Zeit ist um {y - y2} h kürzer.'],
                     f'Indirekt proportional hieße: {y} : {k} = {zt(Fr(y, k))} Stunden. {zt(y2)} Stunden passt nicht. „Weniger Zeit“ allein reicht nicht.',
                     'Wievielfach sind die Personen? Wie hätte sich die Zeit verändern müssen?')
        richtig = situation(R, 'indirekt')
        falsch = [situation(R, 'direkt'), situation(R, 'weder'), situation(R, 'weder')]
        return A(R, 'Welche Zuordnung ist indirekt proportional?', richtig, falsch,
                 f'„{richtig}“: Doppelt so viel von der ersten Größe → halb so viel von der zweiten. Bei den anderen ist das nicht so.',
                 'Teste jede Zuordnung: Was passiert beim Verdoppeln?')
    art = R.choice(['falle', 'aussage', 'falle'])
    if art == 'falle':
        t, gr = R.choice(FALLE)
        return A(R, f'„{t}: Je mehr, desto weniger, also indirekt proportional.“ Stimmt die Begründung?',
                 'Nein: „Je mehr, desto weniger“ reicht nicht.', ['Ja: Mehr führt zu weniger, das ist die Definition.', 'Ja: Die Zuordnung ist sogar direkt proportional.'],
                 gr + ' Für indirekte Proportionalität muss zum Doppelten genau die Hälfte gehören.',
                 'Prüfe: Gehört zum Doppelten wirklich genau die Hälfte?')
    x, y = R.choice([(2, 12), (3, 8), (4, 6), (2, 18), (3, 12)])
    k = R.choice([2, 3, 4])
    if (y % k): return g_erkennen(R, s)
    return A(R, f'Indirekt proportional: {x} Maschinen brauchen {y} Tage. Welche Aussage stimmt?',
             f'{k * x} Maschinen brauchen {y // k} Tage.', [f'{k * x} Maschinen brauchen {y * k} Tage.', f'{k * x} Maschinen brauchen {y - k} Tage.', f'{x + k} Maschinen brauchen {y - k} Tage.'],
             f'{k}-mal so viele Maschinen → ein {k}-tel der Zeit: {y} : {k} = {y // k}. Probe mit dem Produkt: {x} · {y} = {k * x} · {y // k} = {x * y}.',
             'Wievielfach sind die Maschinen? Was passiert dann mit der Zeit?')


# ---------------- Vervielfachen ----------------
# x-Größe, y-Größe, Dativ, größtes sinnvolles x, größtes sinnvolles y
KONTEXT = [('Personen', 'Stunden', 'Personen', 12, 60), ('Pumpen', 'Stunden', 'Pumpen', 12, 96), ('Pferde', 'Tage', 'Pferden', 20, 120),
           ('Busse', 'Kinder pro Bus', 'Bussen', 8, 60), ('Helfer', 'Minuten', 'Helfern', 20, 240), ('Bagger', 'Tage', 'Baggern', 8, 60)]
FALLE = [('Eine Kerze brennt ab: Brenndauer → Restlänge', 'Nach doppelter Brenndauer ist die Kerze nicht halb so lang wie vorher.'),
         ('Gebrauchtwagen: Alter → Wert', 'Doppeltes Alter heißt nicht halber Wert.'),
         ('Ein Becken läuft gleichmäßig leer: Zeit → Wasserhöhe', 'Die Wasserhöhe nimmt jede Minute um gleich viel ab, nach doppelter Zeit ist sie nicht halb so hoch.'),
         ('Ein Handyakku: Nutzungsdauer → Ladestand', 'Der Ladestand sinkt gleichmäßig; doppelte Nutzungsdauer heißt nicht halber Ladestand.'),
         ('Bergwanderung: Höhe → Temperatur', 'Die Temperatur sinkt pro 100 m um etwa gleich viel, aber auf doppelter Höhe ist es nicht halb so warm.')]


def ok(xn, xs, ys):
    for kk in KONTEXT:
        if kk[0] == xn:
            return all(0 < Fr(x) <= kk[3] for x in xs) and all(0 < Fr(y) <= kk[4] for y in ys)
    return True


def ca_(x):
    return zt(x) if endlich(x) else '≈ ' + zt(Fr(str(round(float(x), 2))))


def g_vervielfachen(R, s):
    for _ in range(200):
        a = _verv(R, s)
        if a: return a
    raise SystemExit('vervielfachen')


def _verv(R, s):
    xn, yn, dat, _, _ = R.choice(KONTEXT)
    if s == 1:
        x, y = R.randint(2, 8), R.choice([12, 16, 20, 24, 30, 36, 40, 48, 60])
        if R.random() < .5:
            x2, y2, op = 2 * x, Fr(y, 2), 'doppelt'
        else:
            if x % 2: x += 1
            x2, y2, op = x // 2, 2 * y, 'halb'
        if not ok(xn, [x, x2], [y, y2]): return None
        return mit_bild(Z(f'Die Zuordnung {xn} → {yn} ist indirekt proportional. Ergänze den fehlenden Wert.', y2, f'{y} * {x} / {x2}',
                          f'{x2} ist {"das Doppelte" if op == "doppelt" else "die Hälfte"} von {x}. Also {"die Hälfte" if op == "doppelt" else "das Doppelte"} von {y}: {zt(y2)}.',
                          'Wie hat sich x verändert? Mach mit y das Umgekehrte.'), tab(xn, yn, [x, x2], [y, None]))
    if s == 2:
        k = R.choice([3, 4, 5, 10])
        x, y = R.randint(2, 6), R.choice([30, 60, 120, 20, 40, 90, 36, 48])
        if R.random() < .5:
            x2, y2 = k * x, Fr(y, k)
            w = f'{x2} ist das {k}-Fache von {x}. Also y durch {k}: {y} : {k} = {zt(y2)}.'
        else:
            x, x2 = k * x, x
            y2 = y * k
            w = f'{x2} ist der {k}. Teil von {x}. Also y mal {k}: {y} · {k} = {y2}.'
        if not endlich(y2) or not ok(xn, [x, x2], [y, y2]): return None
        if R.random() < .3:
            return A(R, f'Indirekt proportional: {x} {xn} → {y} {yn}. Wie viele {yn} sind es bei {x2} {dat}?', zt(y2),
                     [ca_(Fr(y) * x2 / x), zt(y + x - x2) if y + x - x2 > 0 else zt(y + 1), zt(y)],
                     w + ' Wer wie bei direkter Proportionalität rechnet, bekommt den falschen Wert ' + ca_(Fr(y) * x2 / x) + '.',
                     'Mehr oder weniger? Erst überlegen, dann rechnen.')
        return mit_bild(Z(f'Die Zuordnung {xn} → {yn} ist indirekt proportional. Ergänze den fehlenden Wert.', y2, f'{y} * {x} / {x2}', w,
                          'Mit welcher Zahl wurde x multipliziert oder durch welche geteilt?'), tab(xn, yn, [x, x2], [y, None]))
    # Stufe 3: zwei Schritte (erst teilen, dann vervielfachen) oder Lücke in x
    while True:
        a, b = R.sample([2, 3, 4, 5, 6, 8, 9, 10, 12], 2)
        y = R.choice([12, 18, 24, 30, 36, 40, 45, 60, 72, 90])
        if Fr(y * a, b).denominator == 1 and a % b and b % a: break
    if not ok(xn, [a, b], [y, Fr(y * a, b)]): return None
    if R.random() < .5:
        return mit_bild(Z(f'Die Zuordnung {xn} → {yn} ist indirekt proportional. Ergänze den fehlenden Wert. Tipp: über einen Zwischenschritt.',
                          Fr(y * a, b), f'{y} * {a} / {b}',
                          f'Zwischenschritt über 1: 1 → {y} · {a} = {y * a}. Dann {b} → {y * a} : {b} = {zt(Fr(y * a, b))}.',
                          f'{b} ist kein Vielfaches von {a}. Rechne erst zurück auf 1.'), tab(xn, yn, [a, b], [y, None]))
    y2 = Fr(y * a, b)
    return mit_bild(Z(f'Die Zuordnung {xn} → {yn} ist indirekt proportional. Welcher x-Wert fehlt?', b, f'{y} * {a} / ({cz(y2)})',
                      f'Das Produkt ist {a} · {y} = {a * y}. Gesucht ist x mit x · {zt(y2)} = {a * y}: x = {a * y} : {zt(y2)} = {b}.',
                      'Auch hier hilft das Produkt der Paare.'), tab(xn, yn, [a, None], [y, y2]))


# ---------------- Produktgleichheit ----------------
def reihe(R, k, n, groesse=60):
    tl = [d for d in range(2, groesse + 1) if k % d == 0 and d < k]
    if len(tl) < n: return None
    return sorted(R.sample(tl, n))


def g_produkt(R, s):
    if s == 1:
        k = R.choice([24, 36, 48, 60, 72, 120])
        xs = reihe(R, k, 3, 12)
        if not xs: return g_produkt(R, s)
        if R.random() < .5:
            return mit_bild(Z('Die Tabelle gehört zu einer indirekten Proportionalität. Wie groß ist das konstante Produkt x · y?', k, f'{xs[0]} * {k // xs[0]}',
                              f'{xs[0]} · {k // xs[0]} = {k}; ebenso {xs[1]} · {k // xs[1]} = {k}.', 'Multipliziere die Zahlen eines Paares.'),
                            tab('x', 'y', xs, [k // x for x in xs]))
        x4 = R.choice([d for d in range(2, 25) if k % d == 0 and d not in xs] or [1])
        return mit_bild(Z('Die Tabelle gehört zu einer indirekten Proportionalität. Ergänze den fehlenden y-Wert.', k // x4, f'{k} // {x4}',
                          f'Produkt: {xs[0]} · {k // xs[0]} = {k}. Fehlender Wert: {k} : {x4} = {k // x4}.', 'Berechne zuerst das Produkt eines vollständigen Paares.'),
                        tab('x', 'y', xs + [x4], [k // x for x in xs] + [None]))
    if s == 2:
        art = R.choice(['pruefen', 'pruefen', 'luecke', 'luecke_dez'])
        k = R.choice([36, 48, 60, 72, 90, 120, 144, 180])
        xs = reihe(R, k, 4, 20)
        if not xs: return g_produkt(R, s)
        ys = [k // x for x in xs]
        if art == 'pruefen':
            ok = R.random() < .5
            if not ok:
                i = R.randrange(1, 4)
                ys[i] += R.choice([-2, -1, 1, 2, 3])
                if ys[i] <= 0: return g_produkt(R, s)
            prods = [x * y for x, y in zip(xs, ys)]
            richtig = 'Ja, alle Produkte sind gleich.' if ok else f'Nein, {xs[i]} · {ys[i]} = {prods[i]} passt nicht.'
            falsch = (['Nein, die y-Werte werden kleiner.', 'Nein, die Quotienten sind verschieden.'] if ok
                      else ['Ja, alle Produkte sind gleich.', 'Ja, die y-Werte werden kleiner.'])
            return mit_bild(A(R, 'Ist die Zuordnung in der Tabelle indirekt proportional?', richtig, falsch,
                              'Produkte: ' + ', '.join(f'{x} · {y} = {p}' for x, y, p in zip(xs, ys, prods)) + '.' + ('' if ok else ' Ein abweichendes Produkt genügt für „nein“.'),
                              'Berechne für jedes Paar x · y.'), tab('x', 'y', xs, ys))
        if art == 'luecke':
            i = R.randrange(1, 4)
            yy = ys[:]
            yy[i] = None
            return mit_bild(Z('Die Tabelle gehört zu einer indirekten Proportionalität. Ergänze den fehlenden Wert.', ys[i], f'{xs[0]} * {ys[0]} // {xs[i]}',
                              f'Produkt: {xs[0]} · {ys[0]} = {k}. Fehlender Wert: {k} : {xs[i]} = {ys[i]}.', 'Das Produkt x · y ist überall gleich.'), tab('x', 'y', xs, yy))
        x4 = R.choice([8, 16, 25, 40, 50])
        y4 = Fr(k, x4)
        if not endlich(y4) or x4 in xs: return g_produkt(R, s)
        return mit_bild(Z('Die Tabelle gehört zu einer indirekten Proportionalität. Ergänze den fehlenden Wert.', y4, f'{k} / {x4}',
                          f'Produkt: {xs[0]} · {ys[0]} = {k}. Fehlender Wert: {k} : {x4} = {zt(y4)}.', 'Das Produkt x · y ist überall gleich. Das Ergebnis darf eine Dezimalzahl sein.'),
                        tab('x', 'y', xs[:3] + [x4], ys[:3] + [None]))
    art = R.choice(['fehler', 'dezimal', 'gesamt'])
    if art == 'fehler':
        k = R.choice([48, 60, 72, 120, 144])
        xs = reihe(R, k, 4, 24)
        if not xs: return g_produkt(R, s)
        ys = [k // x for x in xs]
        i = R.randrange(4)
        ys[i] = ys[i] + R.choice([-3, -2, 2, 3, 4])
        if ys[i] <= 0: return g_produkt(R, s)
        return mit_bild(A(R, 'In der Tabelle einer indirekten Proportionalität hat sich ein Fehler eingeschlichen. Welches Paar ist falsch?',
                          f'({xs[i]} | {ys[i]})', [f'({x} | {y})' for j, (x, y) in enumerate(zip(xs, ys)) if j != i][:3],
                          'Produkte: ' + ', '.join(f'{x} · {y} = {x * y}' for x, y in zip(xs, ys)) + f'. Nur ({xs[i]} | {ys[i]}) weicht ab; richtig wäre {k // xs[i]}.',
                          'Berechne alle Produkte. Welches fällt aus der Reihe?'), tab('x', 'y', xs, ys))
    if art == 'dezimal':
        x1, y1 = R.choice([(Fr(5, 2), 8), (Fr(3, 2), 12), (Fr(1, 2), 30), (Fr(5, 4), 16), (Fr(15, 2), 4)])
        k = x1 * y1
        x2 = R.choice([d for d in (2, 4, 5, 8, 10, 16, 25) if endlich(k / d) and d != x1])
        return mit_bild(Z('Die Tabelle gehört zu einer indirekten Proportionalität. Ergänze den fehlenden Wert.', k / x2, f'{cz(x1)} * {y1} / {x2}',
                          f'Produkt: {zt(x1)} · {y1} = {zt(k)}. Fehlender Wert: {zt(k)} : {x2} = {zt(k / x2)}.', 'Auch mit Dezimalzahlen gilt: Produkt ist konstant.'),
                        tab('x', 'y', [x1, x2], [y1, None]))
    n, b = R.choice([(3, 40), (4, 30), (5, 24), (6, 20), (4, 45), (5, 36)])
    m = R.choice([d for d in (2, 3, 4, 5, 6, 8, 9, 10, 12) if (n * b) % d == 0 and d != n])
    return Z(f'Ein Preisgeld wird gleichmäßig aufgeteilt. Bei {n} Personen bekommt jede {b} €. Nun kommen noch Personen dazu, und jede bekommt nur noch {(n * b) // m} €. Wie viele Personen sind es jetzt?',
             m, f'{n} * {b} // {(n * b) // m}', f'Gesamtbetrag (Produkt): {n} · {b} = {n * b} €. Personen: {n * b} : {(n * b) // m} = {m}.',
             'Was bleibt gleich, egal wie viele Personen es sind?')


# ---------------- Dreisatz ----------------
# Plural, Singular (mit Artikel), Satz mit {t}, Zeiteinheit (Nominativ), Kurzzeichen, n-Bereich, t-Bereich
DS = [('gleich starke Pumpen', 'eine Pumpe', 'leeren ein Becken in {t} Stunden', 'Stunden', 'h', (2, 8), (4, 24)),
      ('Bagger', 'ein Bagger', 'heben eine Baugrube in {t} Tagen aus', 'Tage', 'Tage', (2, 6), (4, 30)),
      ('Helfer', 'ein Helfer', 'räumen eine Turnhalle in {t} Minuten auf', 'Minuten', 'min', (3, 12), (10, 60)),
      ('Erntehelfer', 'ein Erntehelfer', 'pflücken einen Obstgarten in {t} Stunden ab', 'Stunden', 'h', (3, 15), (4, 12))]


def gross(t):
    return t[0].upper() + t[1:]


def g_dreisatz(R, s):
    for _ in range(300):
        a = _dreisatz(R, s)
        if a: return a
    raise SystemExit('dreisatz')


def _dreisatz(R, s):
    wer, eins, satz, zeit, ein, nb, tb = R.choice(DS)
    kurz = wer.split()[-1]
    n, t = R.randint(*nb), R.randint(*tb)
    S = lambda tt: satz.format(t=tt)
    m_ok = lambda m: nb[0] - 1 <= m <= nb[1] + 4 and m != n
    if s == 1:
        if R.random() < .4:
            return Z(f'{n} {wer} {S(t)}. Wie lange braucht {eins} allein?', n * t, f'{n} * {t}',
                     f'{gross(eins)} braucht {n}-mal so lange: {t} · {n} = {n * t} {zeit}.', 'Mehr oder weniger Zeit? Einer allein braucht länger.', einheit=ein)
        ms = [d for d in range(1, 20) if (n * t) % d == 0 and m_ok(d) and d > 1]
        if not ms: return None
        m = R.choice(ms)
        return Z(f'{n} {wer} {S(t)}. Wie lange brauchen {m} {kurz}?', Fr(n * t, m), f'{n} * {t} / {m}',
                 f'{gross(eins)}: {t} · {n} = {n * t} {zeit}. {m} {kurz}: {n * t} : {m} = {zt(Fr(n * t, m))} {zeit}.', 'Rechne zuerst aus, wie lange einer allein braucht.', einheit=ein)
    if s == 2:
        art = R.choice(['normal', 'normal', 'rechnung', 'dez'])
        if art == 'rechnung':
            ms = [d for d in range(2, 20) if m_ok(d)]
            m = R.choice(ms)
            r = f'{t} · {n} : {m}'
            return A(R, f'{n} {wer} {S(t)}. Mit welcher Rechnung bestimmst du die Zeit für {m} {kurz}?', r,
                     [f'{t} : {n} · {m}', f'{t} · {m} : {n}', f'{t} − {n} + {m}'],
                     f'Erst auf einen: {t} · {n} (einer braucht länger). Dann auf {m}: : {m}. Also {r}.',
                     'Schritt zur Einheit: Braucht einer mehr oder weniger Zeit?')
        cands = [d for d in range(2, 20) if m_ok(d) and endlich(Fr(n * t, d)) and (((n * t) % d != 0) == (art == 'dez'))]
        if not cands: return None
        m = R.choice(cands)
        return Z(f'{n} {wer} {S(t)}. Wie lange brauchen {m} {kurz}?', Fr(n * t, m), f'{n} * {t} / {m}',
                 f'{gross(eins)}: {t} · {n} = {n * t} {zeit}. {m} {kurz}: {n * t} : {m} = {zt(Fr(n * t, m))} {zeit}.', 'Über die Einheit: erst einer, dann alle.', einheit=ein)
    art = R.choice(['anzahl', 'fehler', 'zusatz'])
    if art == 'anzahl':
        cands = [d for d in range(2, t) if (n * t) % d == 0 and m_ok((n * t) // d) and (n * t) // d > n]
        if not cands: return None
        t2 = R.choice(cands)
        return Z(f'{n} {wer} {S(t)}. Wie viele {kurz} braucht man, damit es nur {t2} {zeit} dauert?', (n * t) // t2, f'{n} * {t} // {t2}',
                 f'Das Produkt bleibt gleich: {n} · {t} = {n * t}. Anzahl: {n * t} : {t2} = {(n * t) // t2} {kurz}.', 'Gesucht ist diesmal die Anzahl. Das Produkt bleibt gleich.')
    if art == 'fehler':
        ms = [d for d in range(2, 20) if m_ok(d) and endlich(Fr(n * t, d)) and endlich(Fr(t * d, n))]
        if not ms: return None
        m = R.choice(ms)
        return A(R, f'{n} {wer} {S(t)}. Wie lange brauchen {m} {kurz}? Jemand rechnet: {t} : {n} · {m} = {zt(Fr(t * m, n))} {zeit}. Was ist falsch?',
                 'Der Schritt zur Einheit: Einer braucht länger, also mal statt geteilt.',
                 ['Nichts, die Rechnung stimmt.', f'Am Ende muss {m} addiert werden.', 'Man muss erst die Zeiten addieren.'],
                 f'Richtig: {t} · {n} : {m} = {zt(Fr(n * t, m))} {zeit}. Die falsche Rechnung behandelt die Aufgabe wie direkte Proportionalität.',
                 'Frage dich bei jedem Schritt: mehr oder weniger Zeit?')
    k = R.randint(1, 3)
    m = n + k
    tz = R.randint(1, t - 1)
    rest = (t - tz) * n
    if rest % m: return None
    return Z(f'{n} {wer} {S(t)}. Nach {tz} {zeit} kommen {k} weitere dazu. Wie lange dauert es dann noch?', rest // m, f'({t} - {tz}) * {n} // {m}',
             f'Nach {tz} {zeit} bleibt Arbeit, für die {n} {kurz} noch {t - tz} {zeit} bräuchten. {gross(eins)} allein bräuchte {rest} {zeit}. Mit {m} {kurz}: {rest} : {m} = {rest // m} {zeit}.',
             'Wie viel Arbeit ist noch übrig? Wer arbeitet ab jetzt mit?', einheit=ein)


# ---------------- Graph ----------------
def teiler_paare(k, grenze=12):
    return [(x, k // x) for x in range(1, grenze + 1) if k % x == 0 and k // x <= grenze]


def g_graph(R, s):
    if s == 1:
        k = R.choice([6, 8, 10, 12, 16, 18, 20, 24])
        paare = [p for p in teiler_paare(k) if p[0] != p[1]]
        x, y = R.choice(paare)
        art = R.choice(['k', 'y', 'merkmal'])
        if art == 'k':
            return mit_bild(Z(f'Der Punkt P liegt auf dem Graphen einer indirekten Proportionalität y = k : x. Bestimme k.', k, f'{x} * {y}',
                              f'P({x} | {y}): k = x · y = {x} · {y} = {k}.', 'k ist das Produkt der Koordinaten eines Punktes.'),
                            hyp(k, punkte=[{'x': x, 'y': y, 'name': 'P'}]))
        if art == 'y':
            x2, y2 = R.choice([p for p in paare if p[0] != x])
            return mit_bild(Z(f'Der Graph gehört zu y = {k} : x. Welchen y-Wert hat er bei x = {x2}?', y2, f'{k} // {x2}',
                              f'Einsetzen: y = {k} : {x2} = {y2}. Der Punkt ({x2} | {y2}) liegt auf dem Graphen.', 'Setze x in die Gleichung ein.'), hyp(k))
        return A(R, 'Welche Aussage über den Graphen einer indirekten Proportionalität stimmt?', 'Er kommt den Achsen immer näher, berührt sie aber nicht.',
                 ['Er ist eine Gerade durch den Ursprung.', 'Er schneidet die x-Achse.', 'Er ist eine fallende Gerade.'],
                 'Der Graph ist eine Hyperbel. Bei x = 0 ist y = k : 0 nicht definiert, und y wird nie 0, weil k : x nie 0 ist.',
                 'Was passiert mit y = k : x, wenn x sehr klein oder sehr groß wird?')
    if s == 2:
        art = R.choice(['liegt', 'liegt', 'welcher', 'ablesen'])
        k = R.choice([12, 18, 24, 30, 36, 40, 48])
        if art == 'liegt':
            x = R.choice([d for d in range(2, 13) if k % d == 0])
            y = k // x if R.random() < .5 else k // x + R.choice([-2, -1, 1, 2])
            if y <= 0: return g_graph(R, s)
            auf = x * y == k
            return A(R, f'Liegt der Punkt Q({x} | {y}) auf dem Graphen von y = {k} : x?', 'Ja' + f', denn {x} · {y} = {k}.' if auf else f'Nein, denn {x} · {y} = {x * y} ≠ {k}.',
                     ([f'Nein, denn {x} · {y} = {x * y + x} ≠ {k}.', f'Nein, denn {y} : {x} ≠ {k}.'] if auf else [f'Ja, denn {x} · {y} = {k}.', f'Ja, denn {y} < {k}.']),
                     f'Ein Punkt liegt auf dem Graphen, wenn x · y = k ist: {x} · {y} = {x * y}. ' + ('Passt.' if auf else f'Das ist nicht {k}. Bei x = {x} wäre y = {k // x if k % x == 0 else zt(Fr(k, x))}.'),
                     'Rechne x · y aus und vergleiche mit k.')
        if art == 'welcher':
            m = R.choice([Fr(1, 2), 1, 2])
            namen = R.sample(['f', 'g'], 2)
            g = hyp(12, weitere=[{'art': 'linear', 'm': float(m), 't': 0, 'name': namen[1]}])
            g['graphen'][0]['name'] = namen[0]
            return mit_bild(A(R, 'Welcher Graph gehört zu einer indirekten Proportionalität?', f'{namen[0]}, die gebogene Kurve',
                              [f'{namen[1]}, die Gerade durch den Ursprung', 'beide', 'keiner'],
                              f'{namen[1]} ist eine Ursprungsgerade: direkt proportional. {namen[0]} ist eine Hyperbel: z. B. (2 | 6) und (4 | 3) – doppelt so viel, halb so viel.',
                              'Lies zwei Punkte ab: Was passiert mit y, wenn x sich verdoppelt?'), g)
        x, y = R.choice([p for p in teiler_paare(k, 12) if p[0] != p[1]] or [(2, k // 2)])
        x2, y2 = R.choice([p for p in teiler_paare(k, 12) if p[0] != x] or [(1, k)])
        return mit_bild(Z(f'Der Punkt P liegt auf der Hyperbel. Welchen y-Wert hat die Hyperbel bei x = {x2}?', y2, f'{x} * {y} // {x2}',
                          f'k = {x} · {y} = {k}. Bei x = {x2}: y = {k} : {x2} = {y2}.', 'Bestimme zuerst k aus dem Punkt P.'),
                        hyp(k, punkte=[{'x': x, 'y': y, 'name': 'P'}], xmax=max(12, x2 + 1), ymax=max(12, y + 1, y2 + 1)))
    art = R.choice(['dezimal', 'vergleich', 'flaeche'])
    if art == 'dezimal':
        k = R.choice([6, 9, 10, 15])
        x = R.choice([d for d in (4, 5, 8) if endlich(Fr(k, d)) and k % d])
        return mit_bild(Z(f'Der Graph gehört zu y = {k} : x. Welchen y-Wert hat er bei x = {x}? (Dezimalzahl)', Fr(k, x), f'{k} / {x}',
                          f'y = {k} : {x} = {zt(Fr(k, x))}. Am Graphen siehst du: knapp über oder unter einer ganzen Zahl.', 'Setze ein und rechne genau.'), hyp(k))
    if art == 'vergleich':
        k1, k2 = R.sample([6, 8, 12, 16, 24], 2)
        g = hyp(max(k1, k2))
        g['graphen'] = [{'art': 'hyperbel', 'a': k1, 'b': 0, 'c': 0, 'name': 'f', 'bereich': [round(k1 / 12, 2), 12]},
                        {'art': 'hyperbel', 'a': k2, 'b': 0, 'c': 0, 'name': 'g', 'bereich': [round(k2 / 12, 2), 12]}]
        gross = 'f' if k1 > k2 else 'g'
        return mit_bild(A(R, f'Die Hyperbeln gehören zu y = {k1} : x und y = {k2} : x. Welche gehört zu y = {max(k1, k2)} : x?', gross,
                          ['g' if gross == 'f' else 'f', 'Man kann es nicht erkennen.'],
                          f'Bei gleichem x ist y = {max(k1, k2)} : x größer als y = {min(k1, k2)} : x. Die Hyperbel mit größerem k liegt weiter oben, hier {gross}.',
                          'Vergleiche die y-Werte bei x = 1 oder x = 2.'), g)
    k = R.choice([24, 36, 48])
    x, y = R.choice([p for p in teiler_paare(k) if p[0] != p[1]])
    return mit_bild(A(R, f'Alle Rechtecke mit {k} cm² Flächeninhalt: Breite x → Länge y. Der Punkt P({x} | {y}) liegt auf dem Graphen. Was bedeutet der Punkt?',
                      f'Ein Rechteck mit Breite {x} cm und Länge {y} cm hat {k} cm².', [f'Ein Rechteck mit Breite {x} cm hat {k} cm² Umfang.', f'Breite und Länge zusammen sind {x + y} cm².', f'Das Rechteck ist {x * y} cm lang.'],
                      f'x ist die Breite, y die Länge. Der Punkt steht für ein Rechteck mit {x} cm · {y} cm = {k} cm².', 'Was bedeuten die beiden Achsen?'),
                    {**hyp(k, punkte=[{'x': x, 'y': y, 'name': 'P'}], xmax=max(12, x + 1), ymax=max(12, y + 1)), 'name_x': 'Breite in cm', 'name_y': 'Länge in cm'})


# ---------------- Unterscheiden ----------------
def g_unterscheiden(R, s):
    OPT = ['direkt proportional', 'indirekt proportional', 'weder noch']
    if s <= 2:
        art = R.choice(['direkt', 'indirekt', 'weder', 'weder2'] if s == 2 else ['direkt', 'indirekt', 'weder'])
        xs = sorted(R.sample(range(1, 9), 3))
        if art == 'direkt':
            q = R.randint(2, 9); ys = [q * x for x in xs]
            r, w = 0, f'Quotienten y : x: alle gleich {q}. Also direkt proportional.'
        elif art == 'indirekt':
            k = 360 if s == 2 else 120
            xs = sorted(R.sample([d for d in range(1, 13) if k % d == 0], 3))
            ys = [k // x for x in xs]
            r, w = 1, f'Produkte x · y: alle gleich {k}. Also indirekt proportional.'
        elif art == 'weder':
            m, t = R.randint(2, 6), R.randint(1, 9)
            ys = [m * x + t for x in xs]
            r, w = 2, f'Quotienten: {zt(Fr(ys[0], xs[0]))} und {zt(Fr(ys[1], xs[1]))} – verschieden. Produkte: {xs[0] * ys[0]} und {xs[1] * ys[1]} – verschieden. Also weder noch.'
        else:
            t = R.randint(20, 40); m = R.randint(2, 4)
            ys = [t - m * x for x in xs]
            r, w = 2, f'y wird kleiner, aber die Produkte {", ".join(str(x * y) for x, y in zip(xs, ys))} sind verschieden. Also nicht indirekt proportional – weder noch.'
        return mit_bild(A(R, 'Welche Art von Zuordnung zeigt die Tabelle?', OPT[r], [o for o in OPT if o != OPT[r]] + (['nicht zu entscheiden'] if s == 2 else []), w,
                          'Berechne für jedes Paar den Quotienten y : x und das Produkt x · y.'), tab('x', 'y', xs, ys))
    art = R.choice(['gleichung', 'aussage', 'ergaenzen'])
    if art == 'gleichung':
        k = R.choice([12, 18, 20, 24, 30])
        m = R.randint(2, 6)
        typ = R.choice(['ind', 'dir', 'lin', 'fall'])
        gleich = {'ind': f'y = {k} : x', 'dir': f'y = {m} · x', 'lin': f'y = {m} · x + {R.randint(1, 9)}', 'fall': f'y = {k} − {m} · x'}[typ]
        r = {'ind': 1, 'dir': 0, 'lin': 2, 'fall': 2}[typ]
        return A(R, f'Welche Art von Zuordnung beschreibt {gleich}?', OPT[r], [o for o in OPT if o != OPT[r]] + ['quadratisch'],
                 {'ind': f'x · y = {k} ist konstant: indirekt proportional.', 'dir': f'y : x = {m} ist konstant: direkt proportional.',
                  'lin': 'Wegen des Summanden ist weder y : x noch x · y konstant: weder noch.', 'fall': f'y wird kleiner, aber x · y ist nicht konstant (z. B. x = 1 und x = 2 testen): weder noch.'}[typ],
                 'Setze zwei x-Werte ein, z. B. 1 und 2. Was passiert mit y?')
    if art == 'aussage':
        k = R.choice([24, 36, 48])
        xs = sorted(R.sample([d for d in range(1, 13) if k % d == 0], 3))
        ys = [k // x for x in xs]
        return mit_bild(A(R, '„Die Tabelle ist indirekt proportional, weil die y-Werte kleiner werden.“ Wie beurteilst du diese Begründung?',
                          'Ergebnis richtig, Begründung falsch: Entscheidend ist das gleiche Produkt.',
                          ['Alles richtig.', 'Ergebnis falsch: Die Tabelle ist direkt proportional.', 'Ergebnis falsch: Die Tabelle ist weder noch.'],
                          f'Produkte: {", ".join(f"{x} · {y} = {x * y}" for x, y in zip(xs, ys))}. Indirekt proportional stimmt. Aber „wird kleiner“ gilt auch für Zuordnungen, die weder noch sind.',
                          'Prüfe das Ergebnis mit den Produkten. Reicht „wird kleiner“ als Grund?'), tab('x', 'y', xs, ys))
    x1, y1 = R.choice([(2, 30), (3, 20), (4, 15), (5, 12), (6, 10)])
    x2 = R.choice([d for d in (10, 12, 15, 20) if d != x1])
    art2 = R.choice(['d', 'i'])
    if art2 == 'd':
        return mit_bild(Z('Die Zuordnung ist direkt proportional. Ergänze den fehlenden Wert.', Fr(y1 * x2, x1), f'{y1} * {x2} / {x1}',
                          f'Direkt: Quotient {y1} : {x1} = {zt(Fr(y1, x1))} bleibt gleich. y = {zt(Fr(y1, x1))} · {x2} = {zt(Fr(y1 * x2, x1))}. (Indirekt wäre es {zt(Fr(x1 * y1, x2))}.)',
                          'Achtung: Hier ist die Zuordnung direkt proportional.'), tab('x', 'y', [x1, x2], [y1, None]))
    return mit_bild(Z('Die Zuordnung ist indirekt proportional. Ergänze den fehlenden Wert.', Fr(x1 * y1, x2), f'{x1} * {y1} / {x2}',
                      f'Indirekt: Produkt {x1} · {y1} = {x1 * y1} bleibt gleich. y = {x1 * y1} : {x2} = {zt(Fr(x1 * y1, x2))}. (Direkt wäre es {zt(Fr(y1 * x2, x1))}.)',
                      'Achtung: Hier ist die Zuordnung indirekt proportional.'), tab('x', 'y', [x1, x2], [y1, None]))


# ---------------- Sachaufgaben ----------------
def g_sach(R, s):
    if s == 1:
        art = R.choice(['tempo', 'gewinn', 'busse', 'futter'])
        if art == 'tempo':
            v, t = R.choice([(60, 2), (80, 3), (90, 2), (50, 4), (100, 3)])
            v2 = R.choice([d for d in (40, 60, 80, 100, 120, 150) if d != v and (v * t) % d == 0])
            return Z(f'Bei {v} km/h dauert eine Fahrt {t} Stunden. Wie lange dauert sie bei {v2} km/h?', Fr(v * t, v2), f'{v} * {t} / {v2}',
                     f'Strecke: {v} · {t} = {v * t} km. Zeit: {v * t} : {v2} = {zt(Fr(v * t, v2))} h.', 'Berechne zuerst die Länge der Strecke.', einheit='h')
        if art == 'gewinn':
            g = R.choice([240, 360, 480, 600, 720])
            n = R.choice([d for d in range(3, 13) if g % d == 0])
            m = R.choice([d for d in range(2, 16) if g % d == 0 and d != n])
            return Z(f'Ein Gewinn wird gleichmäßig verteilt. Bei {n} Personen bekommt jede {g // n} €. Wie viel bekommt jede bei {m} Personen?', g // m, f'{n} * {g // n} // {m}',
                     f'Gewinn: {n} · {g // n} = {g} €. Pro Person: {g} : {m} = {g // m} €.', 'Wie groß ist der ganze Gewinn?', einheit='€')
        if art == 'busse':
            k = R.choice([120, 180, 240])
            n = R.choice([d for d in (2, 3, 4, 5, 6) if k % d == 0 and k // d <= 60])
            m = R.choice([d for d in (3, 4, 5, 6) if k % d == 0 and d != n and k // d <= 60])
            return Z(f'{k} Kinder fahren ins Schullandheim. Mit {n} gleich vollen Bussen sitzen {k // n} Kinder in jedem Bus. Wie viele sind es pro Bus bei {m} Bussen?', k // m,
                     f'{n} * {k // n} // {m}', f'{n} · {k // n} = {k} Kinder. {k} : {m} = {k // m} pro Bus.', 'Wie viele Kinder sind es insgesamt?')
        n, t = R.choice([(4, 30), (5, 24), (6, 20), (3, 40)])
        m = R.choice([d for d in (2, 8, 10, 12, 15) if (n * t) % d == 0 and d != n])
        return Z(f'Ein Heuvorrat reicht für {n} Pferde {t} Tage. Wie lange reicht er für {m} Pferde?', (n * t) // m, f'{n} * {t} // {m}',
                 f'Für 1 Pferd: {n} · {t} = {n * t} Tage. Für {m}: {n * t} : {m} = {(n * t) // m} Tage.', 'Mehr Pferde → kürzer, weniger Pferde → länger.', einheit='Tage')
    if s == 2:
        art = R.choice(['fliesen', 'tempo_min', 'entscheiden', 'portion'])
        if art == 'fliesen':
            n, a = R.choice([(120, 20), (200, 15), (96, 25), (150, 20)])
            a2 = R.choice([d for d in (10, 30, 40, 50) if endlich(Fr(n * a * a, d * d)) and (n * a * a) % (d * d) == 0])
            return Z(f'Für einen Boden braucht man {n} quadratische Fliesen mit {a} cm Seitenlänge. Wie viele Fliesen mit {a2} cm Seitenlänge braucht man?',
                     (n * a * a) // (a2 * a2), f'{n} * {a} * {a} // ({a2} * {a2})',
                     f'Fläche einer Fliese: {a * a} cm² bzw. {zt(a2 * a2)} cm². Boden: {n} · {a * a} = {zt(n * a * a)} cm². Anzahl: {zt(n * a * a)} : {zt(a2 * a2)} = {(n * a * a) // (a2 * a2)}.',
                     'Indirekt proportional sind Anzahl und Fläche einer Fliese – nicht die Seitenlänge!')
        if art == 'tempo_min':
            t, v = R.choice([(30, 12), (20, 15), (36, 10), (40, 12), (24, 15)])
            v2 = R.choice([d for d in (10, 12, 15, 16, 18, 20, 24) if (t * v) % d == 0 and d != v])
            return Z(f'Mit dem Fahrrad ({v} km/h) braucht jemand für den Schulweg {t} Minuten. Wie viele Minuten wären es mit {v2} km/h?', (t * v) // v2, f'{t} * {v} // {v2}',
                     f'Produkt: {t} · {v} = {t * v}. {t * v} : {v2} = {(t * v) // v2} Minuten.', 'Schneller → weniger Zeit. Das Produkt bleibt gleich.', einheit='min')
        if art == 'entscheiden':
            kind = R.choice(['dir', 'ind', 'weder'])
            if kind == 'dir':
                p = R.choice([3, 4, 5]); n = R.randint(2, 4); m = R.randint(5, 9)
                return A(R, f'{n} Kinokarten kosten {n * p * 2} €. Was kosten {m} Karten?', f'{m * p * 2} €', [f'{zt(Fr(n * n * p * 2, m))} €' if endlich(Fr(n * n * p * 2, m)) else f'{m * p} €', f'{n * p * 2 + m - n} €'],
                         f'Doppelt so viele Karten kosten doppelt so viel: direkt. 1 Karte: {2 * p} €, {m} Karten: {m * 2 * p} €.', 'Zuerst: direkt oder indirekt?')
            if kind == 'ind':
                n, t = R.choice([(3, 12), (4, 9), (2, 18), (6, 6)])
                m = R.choice([d for d in (2, 3, 4, 6, 9, 12) if (n * t) % d == 0 and d != n])
                return A(R, f'{n} Maler streichen ein Haus in {t} Tagen. Wie lange brauchen {m} Maler?', f'{(n * t) // m} Tage',
                         [f'{zt(Fr(t * m, n))} Tage' if endlich(Fr(t * m, n)) else f'{t + m} Tage', f'{t} Tage'],
                         f'Mehr Maler → weniger Zeit, doppelt → halb: indirekt. {n} · {t} = {n * t}, {n * t} : {m} = {(n * t) // m} Tage.', 'Zuerst: direkt oder indirekt?')
            g, p = R.choice([(3, 2), (4, 3), (5, 2)])
            n, m = R.randint(2, 4), R.randint(5, 9)
            return A(R, f'Eine Taxifahrt kostet {g} € Grundgebühr und {p} € pro km. {n} km kosten {g + n * p} €. Was kosten {m} km?', f'{g + m * p} €',
                     [f'{zt(Fr((g + n * p) * m, n))} €' if endlich(Fr((g + n * p) * m, n)) else f'{(g + n * p) * m} €', f'{zt(Fr((g + n * p) * n, m))} €' if endlich(Fr((g + n * p) * n, m)) else f'{m * p} €'],
                     f'Weder direkt noch indirekt – kein Dreisatz! {g} € + {m} · {p} € = {g + m * p} €.', 'Zuerst: direkt, indirekt oder keins von beiden?')
        g = R.choice([600, 800, 900, 1200])
        p = R.choice([d for d in (100, 150, 200, 250) if g % d == 0])
        p2 = R.choice([d for d in (50, 75, 120, 125, 300) if g % d == 0 and d != p])
        return Z(f'Eine Packung Müsli ({g} g) reicht für {g // p} Portionen zu {p} g. Wie viele Portionen sind es, wenn eine Portion {p2} g hat?', g // p2, f'{g // p} * {p} // {p2}',
                 f'Gesamtmenge: {g // p} · {p} = {g} g. {g} : {p2} = {g // p2} Portionen.', 'Kleinere Portionen → mehr Portionen.')
    art = R.choice(['zusatz', 'umrechnen', 'weder_fehler'])
    if art == 'zusatz':
        n, t = R.choice([(6, 20), (8, 15), (5, 24), (4, 30), (10, 12)])
        tz = R.randint(2, t // 2)
        k = R.randint(1, 4)
        rest = (t - tz) * n
        if rest % (n + k): return g_sach(R, s)
        return Z(f'Ein Vorrat reicht für {n} Pferde {t} Tage. Nach {tz} Tagen kommen {k} Pferde dazu. Wie viele Tage reicht der Rest noch?', rest // (n + k), f'({t} - {tz}) * {n} // ({n} + {k})',
                 f'Rest: reicht für {n} Pferde noch {t - tz} Tage = {rest} „Pferdetage“. Für {n + k} Pferde: {rest} : {n + k} = {rest // (n + k)} Tage.',
                 'Wie viel Vorrat ist nach den ersten Tagen noch übrig?', einheit='Tage')
    if art == 'umrechnen':
        v, t = R.choice([(80, 90), (60, 120), (100, 72), (120, 45)])
        v2 = R.choice([d for d in (40, 50, 60, 90, 100, 120, 150) if (v * t) % d == 0 and d != v])
        return Z(f'Bei {v} km/h dauert eine Fahrt {t} Minuten. Wie viele Minuten dauert sie bei {v2} km/h?', (v * t) // v2, f'{v} * {t} // {v2}',
                 f'Produkt: {v} · {t} = {zt(v * t)}. Zeit: {zt(v * t)} : {v2} = {(v * t) // v2} Minuten. Die Einheit Minuten bleibt einfach erhalten.', 'Du musst nicht in Stunden umrechnen – das Produkt reicht.', einheit='min')
    e, p = R.choice([(4, 3), (5, 2), (6, 3), (3, 4)])
    n = R.randint(2, 4)
    m = n * R.choice([2, 3])
    k = e + n * p
    return A(R, f'Ein Freizeitpark: Eintritt {e} €, jede Fahrt {p} €. {n} Fahrten kosten mit Eintritt {k} €. Jemand rechnet für {m} Fahrten: {k} · {m // n} = {k * m // n} €. Stimmt das?',
             f'Nein: Der Eintritt wird nur einmal bezahlt, es sind {e + m * p} €.', ['Ja, doppelt so viele Fahrten kosten doppelt so viel.' if m == 2 * n else 'Ja, dreimal so viele Fahrten kosten dreimal so viel.',
                                                                                f'Nein: Es sind {zt(Fr(k * n, m)) if endlich(Fr(k * n, m)) else k // 2} €, weil es indirekt proportional ist.'],
             f'Die Zuordnung ist weder noch, weil der Eintritt fest ist: {e} + {m} · {p} = {e + m * p} €.', 'Wird jeder Betrag bei mehr Fahrten mehrfach bezahlt?')


def bruch(x):
    return f'{x.numerator}/{x.denominator}'


GEN = {'erkennen': g_erkennen, 'vervielfachen': g_vervielfachen, 'produkt': g_produkt, 'dreisatz': g_dreisatz,
       'graph': g_graph, 'unterscheiden': g_unterscheiden, 'sach': g_sach}

TEIL = {'erkennen': 'erkennen', 'vervielfachen': 'erkennen', 'produkt': 'erkennen', 'dreisatz': 'rechnen', 'sach': 'rechnen',
        'graph': 'darstellen', 'unterscheiden': 'darstellen',
        '_texte': [('erkennen', 'Indirekte Proportionalität erkennen und mit Produktgleichheit prüfen'),
                   ('rechnen', 'Mit Dreisatz und Produkt rechnen, Sachaufgaben lösen'),
                   ('darstellen', 'Hyperbel deuten und Zuordnungsarten unterscheiden')]}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Erkennen', ['erkennen', 'vervielfachen', 'produkt']), ('Rechnen', ['dreisatz']),
          ('Darstellen und unterscheiden', ['graph', 'unterscheiden']), ('Anwenden', ['sach'])],
         'Indirekte Proportionalität erkennen, mit Produktgleichheit prüfen, mit Dreisatz rechnen, als Hyperbel darstellen und von direkter Proportionalität und „weder noch“ unterscheiden.',
         ['Indirekt proportional: doppelt so viel → halb so viel.', 'Das Produkt x · y ist für alle Paare gleich.',
          'Dreisatz: erst auf eine Einheit (mal!), dann auf den gesuchten Wert (geteilt).', 'Der Graph ist eine Hyperbel y = k : x; sie berührt die Achsen nie.',
          '„Je mehr, desto weniger“ allein reicht nicht – rechnen!'],
         offen=['Lehrplanbezug: lehrplan_gym ist leer; umgesetzt nach „umfang“ und dem Auftrag (Erkennen, Produktgleichheit, Dreisatz, Hyperbel, Abgrenzung). '
                'Der Funktionsbegriff y = k : x wird nur als Wertepaare/Graph genutzt, keine Funktionsuntersuchung (Asymptoten als Fachbegriff weggelassen).',
                'Hyperbeln nur im 1. Quadranten (x > 0), weil alle Sachsituationen positive Größen haben.'],
         teil=TEIL)
