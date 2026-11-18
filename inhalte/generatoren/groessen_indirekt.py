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
            if min(ys) <= 0: return g_unterscheiden(R, s)
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

# ---------- KLAR: verständliche Erklärungen (Runde 7b, Pflicht seit 15.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _klar_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _klar_rest import mit_klar  # noqa: E402

KLAR = {
 'erkennen': {
  'einstieg': 'Ihr wollt ein Zimmer streichen. Zu zweit braucht ihr 6 Stunden. Kommen zwei Freunde dazu, seid ihr doppelt so viele – und braucht nur halb so lange. Gehört zum Doppelten der einen Größe immer genau die Hälfte der anderen, nennt man das ⟦indirekt proportional⟧.',
  'woerter': [['Größe', 'etwas, das man zählen oder messen kann: Personen, Zeit, Preis'],
              ['Zuordnung', 'jedem Wert der einen Größe gehört ein Wert der anderen: 2 Personen → 6 h'],
              ['h', 'Abkürzung für Stunden'],
              ['das Doppelte, das Dreifache', '2-mal so viel, 3-mal so viel'],
              ['indirekt proportional', 'zum Doppelten gehört die Hälfte, zum Dreifachen ein Drittel usw.']],
  'schritte': ['2 Personen brauchen 6 h. Von diesem Paar gehst du aus.',
               'Doppelt so viele Personen (4) brauchen halb so lange: 6 h : 2 = ⟦3 h⟧.',
               'Dreimal so viele Personen (6) brauchen ein Drittel der Zeit: 6 h : 3 = ⟦2 h⟧.',
               'Zum Doppelten gehört die Hälfte, zum Dreifachen ein Drittel – die Zuordnung ist indirekt proportional.'],
  'regel': 'So erkennst du eine indirekte Proportionalität: Gehört zum ⟦Doppelten⟧ der einen Größe die ⟦Hälfte⟧ der anderen, zum Dreifachen ein ⟦Drittel⟧ usw.? „Je mehr, desto weniger“ allein reicht dafür ⟦nicht⟧ – es muss genau im umgekehrten Verhältnis weniger werden.',
  'fehler': '„Je älter ein Auto, desto weniger ist es wert“ – trotzdem nicht indirekt proportional: Ein 1 Jahr altes Auto ist z. B. 20 000 € wert, ein 2 Jahre altes 17 000 €. Doppeltes Alter, aber ⟦nicht halber Wert⟧ (das wären 10 000 €).'},
 'vervielfachen': {
  'einstieg': 'Ein Bauer hat Futter für seine 6 Pferde, es reicht 20 Tage. Dann verkauft er 3 Pferde. Jetzt fressen nur noch halb so viele Pferde – das Futter reicht doppelt so lange. Was du mit der einen Größe machst, machst du mit der anderen umgekehrt. Das siehst du gut in einer Tabelle mit ⟦Wertepaaren⟧.',
  'woerter': [['Wertepaar', 'zwei zusammengehörige Werte, z. B. 6 Pferde und 20 Tage'],
              ['Tabelle', 'Wertepaare übersichtlich untereinander oder nebeneinander'],
              ['umgekehrt rechnen', 'aus Mal wird Geteilt, aus Geteilt wird Mal']],
  'schritte': ['In der Tabelle stehen 6 Pferde und 20 Tage. Gesucht sind die Tage für 3 Pferde.',
               'Von 6 auf 3 Pferde wird durch 2 geteilt: Es sind halb so viele.',
               'Die Tage rechnest du umgekehrt, also mal 2: 20 · 2 = 40.',
               'Das Futter reicht ⟦40 Tage⟧.'],
  'regel': 'So rechnest du in der Tabelle: Multiplizierst du die eine Größe mit einer Zahl, ⟦teilst⟧ du die andere durch ⟦dieselbe Zahl⟧. Teilst du die eine, ⟦multiplizierst⟧ du die andere.',
  'fehler': 'Wie bei „je mehr, desto mehr“ auf beiden Seiten dasselbe rechnen: 3 Pferde → 20 : 2 = 10 Tage ist falsch. Weniger Pferde fressen weniger, das Futter reicht also ⟦länger⟧: 40 Tage.'},
 'produkt': {
  'einstieg': 'Eine Tippgemeinschaft gewinnt 120 € und teilt gerecht. Spielen 2 Personen mit, bekommt jede 60 €, bei 3 Personen sind es 40 €. Egal wie viele mitspielen: Personen mal Betrag ergibt immer die 120 €. Diese Eigenschaft heißt ⟦Produktgleichheit⟧.',
  'woerter': [['x und y', 'die beiden Größen: x = Anzahl der Personen, y = Euro pro Person'],
              ['Produkt', 'das Ergebnis einer Malaufgabe, hier x · y'],
              ['Produktgleichheit', 'x · y ergibt bei allen Wertepaaren dieselbe Zahl'],
              ['Gesamtmenge', 'das, was verteilt wird – hier der Gewinn']],
  'schritte': ['Rechne für jedes Wertepaar das Produkt aus: 2 · 60 = 120, 3 · 40 = 120 und 5 · 24 = 120.',
               'Alle Produkte sind gleich. Das gemeinsame Produkt ist der Gewinn: ⟦120 €⟧. Die Zuordnung ist indirekt proportional.',
               'Für 8 Personen teilst du das Produkt durch 8: 120 € : 8 = ⟦15 €⟧ pro Person.'],
  'probe': '8 · 15 = 120 ✓',
  'regel': 'So prüfst du mit der ⟦Produktgleichheit⟧: Rechne für ⟦jedes⟧ Wertepaar x · y aus. Sind alle Produkte ⟦gleich⟧, ist die Zuordnung indirekt proportional. Fehlende Werte findest du mit y = ⟦Produkt : x⟧.',
  'fehler': 'Nur zwei Paare prüfen: 2 · 60 = 120 und 4 · 30 = 120, aber 6 · 25 = 150. Dann würde mehr Geld verteilt, als gewonnen wurde. Ein einziges abweichendes Produkt genügt – die Zuordnung ist ⟦nicht⟧ indirekt proportional. Prüfe ⟦alle⟧ Paare.'},
 'dreisatz': {
  'einstieg': 'Ein Schwimmbecken soll geleert werden. 6 gleiche Pumpen schaffen das in 10 Stunden, aber 2 Pumpen fallen aus. Wie lange brauchen die übrigen 4? Du rechnest in drei Sätzen: von 6 Pumpen auf 1 Pumpe und dann auf 4 Pumpen. Dieser Rechenweg heißt ⟦Dreisatz⟧.',
  'woerter': [['Dreisatz', 'ein Rechenweg in drei Schritten: gegebener Wert → eine Einheit → gesuchter Wert'],
              ['Einheit', 'hier: eine einzige Pumpe']],
  'schritte': ['Gegeben: 6 Pumpen brauchen 10 h.',
               'Auf eine Einheit: Eine Pumpe allein braucht 6-mal so lange, 10 h · 6 = 60 h.',
               'Auf den gesuchten Wert: 4 Pumpen schaffen es in einem Viertel der Zeit, 60 h : 4 = ⟦15 h⟧.'],
  'probe': '6 · 10 = 60 und 4 · 15 = 60 ✓',
  'regel': 'So rechnest du den Dreisatz bei indirekter Proportionalität: ⟦gegebener Wert⟧ → ⟦eine Einheit⟧ → ⟦gesuchter Wert⟧. Beim Schritt zur Einheit wird ⟦multipliziert⟧, nicht geteilt – eine Pumpe braucht ja länger als sechs.',
  'fehler': 'Wie bei direkter Proportionalität rechnen: 10 h : 6 · 4 ≈ 6,7 h. Weniger Pumpen können aber nicht schneller sein! Frage dich vorher: ⟦Mehr oder weniger?⟧ Weniger Pumpen → ⟦mehr⟧ Zeit.'},
 'graph': {
  'einstieg': 'Ein Etikett soll 12 cm² groß sein. Es kann 1 cm breit und 12 cm lang sein, 2 cm breit und 6 cm lang oder 3 cm breit und 4 cm lang. Trägst du alle Möglichkeiten in ein Koordinatensystem ein, liegen die Punkte auf einer gebogenen Kurve. Sie heißt ⟦Hyperbel⟧.',
  'woerter': [['cm²', 'Quadratzentimeter, eine Einheit für Flächen'],
              ['Koordinatensystem', 'zwei Achsen: nach rechts die Breite x, nach oben die Länge y'],
              ['(2 | 6)', 'der Punkt mit x = 2 und y = 6'],
              ['Ursprung', 'der Punkt (0 | 0), wo sich die Achsen kreuzen'],
              ['k', 'das Produkt, das immer gleich bleibt – hier 12'],
              ['Hyperbel', 'die gebogene Kurve einer indirekten Proportionalität, y = k : x']],
  'schritte': ['Breite mal Länge muss 12 ergeben: x · y = 12. Also ist y = 12 : x.',
               'Rechne Wertepaare aus: (1 | 12), (2 | 6), (3 | 4), (4 | 3) und (6 | 2).',
               'Trag die Punkte ins Koordinatensystem ein und verbinde sie mit einer gebogenen Linie, nicht mit geraden Strecken.',
               'Es entsteht eine ⟦Hyperbel⟧: Sie fällt erst steil und dann flach und kommt den Achsen immer näher.'],
  'regel': 'So erkennst du den Graphen: Die Punkte (x | y) einer indirekten Proportionalität liegen auf einer ⟦Hyperbel⟧ mit y = k : x, wobei k das gleichbleibende Produkt ist. Der Graph geht ⟦nicht durch den Ursprung⟧ und kommt den Achsen immer näher, ohne sie zu berühren.',
  'fehler': 'Die Punkte mit geraden Strecken verbinden oder die Kurve bis zur Achse zeichnen. Bei x = 0 gäbe es kein Etikett mit 12 cm² – die Kurve ⟦berührt die Achsen nie⟧.'},
 'unterscheiden': {
  'einstieg': 'Eine Taxifahrt kostet 4 € Grundgebühr und 2 € pro Kilometer. 2 km kosten 8 €, 4 km 12 € und 6 km 16 €. Mehr Kilometer kosten mehr Geld – aber doppelt so weit kostet nicht doppelt so viel. Solche Zuordnungen sind ⟦weder direkt noch indirekt proportional⟧.',
  'woerter': [['Grundgebühr', 'ein fester Betrag, den man immer zahlt, egal wie weit man fährt'],
              ['direkt proportional', 'zum Doppelten gehört das Doppelte; y : x ist immer gleich'],
              ['Quotient', 'das Ergebnis einer Geteiltaufgabe, hier y : x'],
              ['weder noch', 'keins von beiden']],
  'schritte': ['Prüfe die Quotienten y : x: 8 : 2 = 4 und 12 : 4 = 3. Sie sind nicht gleich, also ist die Zuordnung nicht direkt proportional.',
               'Prüfe die Produkte x · y: 2 · 8 = 16 und 4 · 12 = 48. Sie sind auch nicht gleich, also ist sie nicht indirekt proportional.',
               'Die Zuordnung ist ⟦weder noch⟧: Die Grundgebühr verhindert die Proportionalität.'],
  'regel': 'So prüfst du mit der Tabelle: Ist der ⟦Quotient y : x⟧ immer gleich, ist die Zuordnung ⟦direkt⟧ proportional. Ist das ⟦Produkt x · y⟧ immer gleich, ist sie ⟦indirekt⟧ proportional. Ist beides nicht so, ist sie ⟦weder noch⟧ – dann hilft kein Dreisatz.',
  'fehler': '„Der Preis wird größer, also direkt proportional“ – beim Taxi wird der Preis größer, aber die doppelte Strecke kostet nicht das Doppelte (4 km: 12 € statt 16 €). Entscheide ⟦mit Rechnung⟧, nicht mit „je mehr, desto mehr“.'},
 'sach': {
  'einstieg': 'Eine Familie fährt in den Urlaub. Bei 80 km/h dauert die Fahrt 3 Stunden. Wie lange dauert sie bei 120 km/h? Bevor du rechnest, überlegst du: Schneller fahren heißt weniger Zeit. So gehst du jede ⟦Sachaufgabe⟧ an.',
  'woerter': [['Sachaufgabe', 'eine Aufgabe mit einer Situation aus dem Alltag'],
              ['km/h', 'Kilometer pro Stunde: wie weit man in einer Stunde fährt'],
              ['sinnvoll', 'passt zur Situation']],
  'schritte': ['Welche Größen hängen zusammen? Geschwindigkeit und Fahrzeit. Doppelt so schnell heißt halb so lange – indirekt proportional.',
               'Das Produkt bleibt gleich: 80 · 3 = 240. Das ist die Strecke in km.',
               'Teile durch die neue Geschwindigkeit: 240 : 120 = ⟦2 h⟧.',
               'Prüfe, ob das sinnvoll ist: schneller gefahren, also weniger Zeit ✓.'],
  'probe': '120 km/h · 2 h = 240 km ✓',
  'regel': 'So löst du eine Sachaufgabe: Lies genau, welche zwei Größen zusammenhängen. Frage dich: ⟦Doppelt so viel – doppelt oder halb?⟧ Erst dann wählst du den Rechenweg. Prüfe am Ende, ob das Ergebnis ⟦sinnvoll⟧ ist.',
  'fehler': 'Bei Aufgaben mit festem Grundbetrag (Eintritt plus Fahrten, Taxi) den Dreisatz verwenden. Kostet 1 Fahrt mit Eintritt 7 €, kosten 3 Fahrten nicht 21 €, wenn der Eintritt nur ⟦einmal⟧ bezahlt wird.'},
}

baue = mit_klar(baue, KLAR)


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl8.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl8 import mit_umbau  # noqa: E402

def _t(kopf, *zeilen):
    return {'typ': 'tabelle', 'kopf': list(kopf), 'zeilen': [list(z) for z in zeilen]}


_ET = [{'x': 1, 'y': 12, 'name': '(1 | 12)'}, {'x': 2, 'y': 6, 'name': '(2 | 6)'}, {'x': 3, 'y': 4, 'name': '(3 | 4)'}, {'x': 4, 'y': 3}, {'x': 6, 'y': 2, 'name': '(6 | 2)'}]
_ETG = [{'art': 'hyperbel', 'a': 12, 'b': 0, 'c': 0, 'bereich': [0.95, 13]}]
_TX = ['Strecke in km', '2', '4', '6']
UMBAU = {
 'erkennen': {
  'einstieg': 'Ihr streicht ein Zimmer: Zu zweit braucht ihr 6 Stunden. Zu viert seid ihr doppelt so viele und braucht halb so lange. Das heißt ⟦indirekt proportional⟧.',
  'woerter': [['indirekt proportional', 'zum Doppelten gehört die Hälfte, zum Dreifachen ein Drittel'], ['h', 'Abkürzung für Stunden']],
  'bild': _t(['Personen', '2', '4', '6'], ['Zeit in h', '6', '?', '?']),
  'schritte': [{'text': '2 Personen brauchen 6 h. Davon gehst du aus.'},
               {'text': 'Doppelt so viele brauchen halb so lange: 6 h : 2 = ⟦3 h⟧.', 'bild': _t(['Personen', '2', '4', '6'], ['Zeit in h', '6', '3', '?'])},
               {'text': 'Dreimal so viele brauchen ein Drittel: 6 h : 3 = 2 h.', 'bild': _t(['Personen', '2', '4', '6'], ['Zeit in h', '6', '3', '2'])},
               {'text': 'Doppelt → halb, dreifach → ein Drittel: indirekt proportional.'}],
  'fehler': '„Je älter, desto billiger“ reicht nicht. Ein doppelt so altes Auto ist nicht ⟦halb so viel⟧ wert.',
  'fehler_bild': _t(['Alter in Jahren', '1', '2'], ['Wert in €', '20 000', '17 000']),
  'regel': 'Doppelt so viel ⟦→ halb so viel⟧: indirekt proportional. „Je mehr, desto weniger“ allein reicht nicht.'},
 'vervielfachen': {
  'einstieg': 'Ein Bauer hat Futter für 6 Pferde, es reicht 20 Tage. Er verkauft 3 Pferde. Bei halb so vielen Pferden reicht das Futter ⟦doppelt so lange⟧.',
  'woerter': [['Wertepaar', 'zwei Werte, die zusammengehören: 6 Pferde – 20 Tage']],
  'bild': _t(['Pferde', '6', '3'], ['Tage', '20', '?']),
  'schritte': [{'text': 'Das Wertepaar ist 6 Pferde und 20 Tage.'},
               {'text': 'Von 6 auf 3 Pferde wird durch 2 geteilt.'},
               {'text': 'Die Tage umgekehrt mal 2: 20 · 2 = ⟦40⟧.', 'bild': _t(['Pferde', '6', '3'], ['Tage', '20', '40'])}],
  'fehler': '3 Pferde → 20 : 2 = 10 Tage ist falsch. Weniger Pferde fressen weniger, das Futter reicht ⟦länger⟧.',
  'fehler_bild': _t(['Pferde', '6', '3'], ['Tage', '20', '10 ?']),
  'regel': 'Teilst du die eine Größe, ⟦multiplizierst⟧ du die andere. Und umgekehrt, immer mit derselben Zahl.'},
 'produkt': {
  'einstieg': 'Eine Tippgemeinschaft gewinnt 120 € und teilt gerecht. Zu zweit bekommt jeder 60 €, zu dritt 40 €. Personen mal Betrag ergibt immer 120 €: ⟦Produktgleichheit⟧.',
  'woerter': [['Produktgleichheit', 'für alle Wertepaare ist x · y gleich'], ['Produkt', 'das Ergebnis einer Malrechnung']],
  'bild': _t(['Personen', '2', '3', '5', '8'], ['€ pro Person', '60', '40', '24', '?']),
  'schritte': [{'text': 'Produkte: 2 · 60, 3 · 40 und 5 · 24 ergeben je 120.'},
               {'text': 'Alle gleich: Das Produkt ist der Gewinn, 120 €.'},
               {'text': 'Für 8 Personen: 120 € : 8 = ⟦15 €⟧.', 'bild': _t(['Personen', '2', '3', '5', '8'], ['€ pro Person', '60', '40', '24', '15'])}],
  'fehler': 'Nur zwei Paare prüfen reicht nicht: 6 · 25 = 150 passt nicht zu 120. Prüfe ⟦alle⟧ Paare.',
  'fehler_bild': _t(['Personen', '2', '4', '6'], ['€ pro Person', '60', '30', '25'], ['Produkt', '120', '120', '150']),
  'regel': 'Gleiches ⟦Produkt x · y⟧ heißt indirekt proportional. Fehlende Werte: Produkt geteilt durch x.'},
 'dreisatz': {
  'einstieg': '6 Pumpen leeren ein Becken in 10 Stunden, dann fallen 2 aus. Wie lange brauchen die übrigen 4? Du rechnest über eine Pumpe, mit dem ⟦Dreisatz⟧.',
  'woerter': [['Dreisatz', 'in drei Schritten rechnen: gegeben → eine Einheit → gesucht']],
  'bild': _t(['Pumpen', '6', '1', '4'], ['Zeit in h', '10', '?', '?']),
  'schritte': [{'text': '6 Pumpen brauchen 10 h.'},
               {'text': 'Eine Pumpe allein braucht 6-mal so lange: 60 h.', 'bild': _t(['Pumpen', '6', '1', '4'], ['Zeit in h', '10', '60', '?'])},
               {'text': '4 Pumpen brauchen ein Viertel davon: 60 h : 4 = ⟦15 h⟧.', 'bild': _t(['Pumpen', '6', '1', '4'], ['Zeit in h', '10', '60', '15'])}],
  'fehler': '10 h : 6 · 4 ≈ 6,7 h ist falsch: Weniger Pumpen sind nicht schneller. Weniger Pumpen brauchen ⟦mehr⟧ Zeit.',
  'fehler_bild': _t(['Pumpen', '6', '1', '4'], ['Zeit in h', '10', '1,7 ?', '6,7 ?']),
  'regel': 'Zur Einheit ⟦malnehmen⟧, nicht teilen. Eine Pumpe braucht länger als sechs.'},
 'graph': {
  'einstieg': 'Ein Etikett soll 12 cm² groß sein, etwa 2 cm breit und 6 cm lang. Es gibt viele Möglichkeiten. Eingetragen liegen sie auf einer gebogenen Kurve, einer ⟦Hyperbel⟧.',
  'woerter': [['Hyperbel', 'die gebogene Kurve von y = k : x'], ['y = 12 : x', 'die Länge, wenn die Breite x ist']],
  'bild': {'typ': 'koordinaten', 'x': [0, 13], 'y': [0, 13], 'name_x': 'Breite', 'name_y': 'Länge', 'graphen': _ETG, 'punkte': _ET},
  'schritte': [{'text': 'Breite mal Länge ist 12, also y = 12 : x.', 'bild': {'graphen': [], 'punkte': []}},
               {'text': 'Wertepaare sind zum Beispiel (1 | 12), (2 | 6) und (3 | 4).', 'bild': {'punkte': _ET}},
               {'text': 'Die Punkte verbindest du mit einer gebogenen Linie: einer ⟦Hyperbel⟧.', 'bild': {'graphen': _ETG}}],
  'fehler': 'Die Kurve nicht bis zur Achse zeichnen. Bei Breite 0 gäbe es kein Etikett mit 12 cm²: Sie ⟦berührt die Achsen nie⟧.',
  'regel': 'Der Graph ist eine ⟦Hyperbel y = k : x⟧. Sie geht nicht durch den Ursprung.'},
 'unterscheiden': {
  'einstieg': 'Eine Taxifahrt kostet 4 € Grundgebühr und 2 € pro Kilometer. Mehr Kilometer kosten mehr, aber doppelt so weit kostet nicht doppelt so viel. Das ist ⟦weder noch⟧.',
  'woerter': [['Quotient', 'das Ergebnis einer Geteiltrechnung, hier y : x'], ['weder noch', 'weder direkt noch indirekt proportional']],
  'bild': _t(_TX, ['Preis in €', '8', '12', '16']),
  'schritte': [{'text': 'Quotienten: 8 : 2 = 4, aber 12 : 4 = 3.', 'bild': _t(_TX, ['Preis in €', '8', '12', '16'], ['y : x', '4', '3', '2,67'])},
               {'text': 'Produkte: 2 · 8 = 16, aber 4 · 12 = 48.', 'bild': _t(_TX, ['Preis in €', '8', '12', '16'], ['y : x', '4', '3', '2,67'], ['x · y', '16', '48', '96'])},
               {'text': 'Weder Quotient noch Produkt bleibt gleich: ⟦weder noch⟧.'}],
  'fehler': '„Der Preis steigt, also direkt proportional“ ist falsch. 4 km kosten 12 €, nicht ⟦das Doppelte⟧ von 8 €.',
  'regel': 'Gleicher ⟦Quotient⟧: direkt. Gleiches ⟦Produkt⟧: indirekt. Sonst weder noch – dann hilft kein Dreisatz.'},
 'sach': {
  'einstieg': 'Bei 80 km/h dauert die Urlaubsfahrt 3 Stunden. Wie lange dauert sie bei 120 km/h? Erst überlegst du: Schneller heißt weniger Zeit – so gehst du jede ⟦Sachaufgabe⟧ an.',
  'woerter': [['Sachaufgabe', 'eine Rechenaufgabe als Geschichte'], ['km/h', 'Kilometer pro Stunde: die Geschwindigkeit']],
  'bild': _t(['km/h', '80', '120'], ['Zeit in h', '3', '?']),
  'schritte': [{'text': 'Doppelt so schnell heißt halb so lange: indirekt proportional.'},
               {'text': 'Das Produkt bleibt: 80 · 3 = 240, die Strecke in km.'},
               {'text': '240 : 120 = ⟦2 h⟧. Schneller, also weniger Zeit: passt.', 'bild': _t(['km/h', '80', '120'], ['Zeit in h', '3', '2'])}],
  'fehler': 'Nicht bei jedem „mehr“ den Dreisatz nehmen. Mit Eintritt kosten 3 Fahrten nicht 3 · 7 €, denn der Eintritt wird nur ⟦einmal⟧ bezahlt.',
  'regel': 'Erst fragen: ⟦Doppelt so viel – doppelt oder halb?⟧ Dann rechnen und das Ergebnis auf Sinn prüfen.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---- SCHWER (Zehnte Runde: schwerere Aufgaben nach Prüfungsvorbild, siehe _schwer_kl8.py) ----
# Vorbilder (Typ und Niveau, nicht Wortlaut/Zahlen): Grundwissen 8 bayerischer Gymnasien (begründen, ob indirekt proportional; Wippe/Hebelgesetz;
# Hyperbel aus dem Graphen), Schulaufgaben-Typ Kl. 8 („Zuordnung benennen“, Dreisatz mit Änderung unterwegs), BMT10 2024 (Rechtecke unter einer Hyperbel),
# BMT8 2022/2025 (Tabellenkalkulations-Formel), Mathematik-Wettbewerbe (gemischte Proportionalität „Hennen und Eier“).
from _schwer_kl8 import Neu, mit_schwer  # noqa: E402

SW = Neu(10_8_15)
_k = lambda **k: {'typ': 'koordinaten', **k}
_ART = ['indirekt proportional', 'direkt proportional', 'weder noch']

# erkennen
SW.a('erkennen', 2, 'Ist diese Zuordnung indirekt proportional? Seitenlänge eines Quadrats → Flächeninhalt.', 'Nein: weder doppelt → halb noch doppelt → doppelt.',
     ['Ja: doppelt so viel → halb so viel.', 'Nein: doppelt so viel → doppelt so viel.'],
     'Doppelte Seitenlänge ergibt die vierfache Fläche (2 cm → 4 cm², 4 cm → 16 cm²). Das ist weder direkt noch indirekt proportional.', 'Rechne zwei Beispiele aus.')
SW.a('erkennen', 2, 'Ist diese Zuordnung indirekt proportional? Rechtecke mit dem Umfang 20 cm: Breite → Länge.', 'Nein: weder doppelt → halb noch doppelt → doppelt.',
     ['Ja: doppelt so viel → halb so viel.', 'Nein: doppelt so viel → doppelt so viel.'],
     'Breite + Länge = 10 cm bleibt gleich, nicht das Produkt. Breite 2 → Länge 8, Breite 4 → Länge 6 (nicht 4). Also weder noch.', 'Was bleibt hier gleich: die Summe oder das Produkt?')
SW.a('erkennen', 3, 'Ein Becken wird von gleich starken Pumpen geleert. Anzahl der Pumpen → Zeit ist indirekt proportional. Welche Begründung ist richtig?',
     'Doppelt so viele Pumpen schaffen in derselben Zeit doppelt so viel Wasser, brauchen also halb so lange.',
     ['Mit mehr Pumpen wird die Zeit kleiner.', 'Pumpenzahl und Zeit ergeben zusammen immer dieselbe Zahl.', 'Mit jeder Pumpe mehr dauert es eine Stunde weniger.'],
     '„Je mehr, desto weniger“ reicht nicht als Begründung. Entscheidend ist: doppelt → halb, dreifach → ein Drittel (das Produkt bleibt gleich).', 'Was passiert genau bei doppelt so vielen Pumpen?', art='P')
SW.a('erkennen', 3, 'Messwerte: 4 Arbeiter brauchen 6 h, 3 Arbeiter 8 h, 8 Arbeiter 4 h. Ist die Zuordnung Arbeiter → Zeit indirekt proportional?', 'Nein: 4 · 6 = 24 und 3 · 8 = 24, aber 8 · 4 = 32.',
     ['Ja: Mehr Arbeiter brauchen weniger Zeit.', 'Ja: Alle Produkte sind 24.', 'Nein: Die Zeiten müssten um gleich viel sinken.'],
     'Bei indirekter Proportionalität ist das Produkt immer gleich. Der dritte Messwert passt nicht (8 Arbeiter müssten 3 h brauchen).', 'Bilde für jedes Paar das Produkt.', art='P')
SW.a('erkennen', 3, 'x und y sind indirekt proportional. x wird um 50 % größer. Was passiert mit y?', 'y sinkt um etwa 33 % (auf 2/3).', ['y sinkt um 50 %.', 'y steigt um 50 %.', 'y halbiert sich.'],
     'x · 1,5 heißt y : 1,5 = y · 2/3. y wird also um ein Drittel kleiner, etwa 33 %, nicht 50 %.', 'Probiere mit x = 2, y = 6.', art='K')
SW.a('erkennen', 3, 'Ist y = 2/x eine indirekte Proportionalität?', 'Ja: x · y = 2 ist für alle Paare gleich.', ['Nein: Es fehlt die Form y = k · x.', 'Nein: Für x = 0 gibt es keinen Wert.',
     'Ja: y wird kleiner, wenn x größer wird.'],
     'y = 2/x heißt x · y = 2 – das Produkt ist konstant. Das ist genau die indirekte Proportionalität (k = 2). x = 0 ist ohnehin ausgeschlossen.', 'Multipliziere beide Seiten mit x.', art='K')

# vervielfachen
SW.z('vervielfachen', 2, 'Die Zuordnung Pumpen → Stunden ist indirekt proportional: 2 Pumpen brauchen 15 Stunden. Wie lange brauchen 6 Pumpen?', 5, '15 / 3',
     '6 Pumpen sind 3-mal so viele, also ein Drittel der Zeit: 15 h : 3 = 5 h.', 'Mit welcher Zahl wird die Pumpenzahl multipliziert?', einheit='h')
SW.z('vervielfachen', 2, 'Indirekt proportional: Zu x = 5 gehört y = 12. Welcher y-Wert gehört zu x = 2,5?', 24, '12 * 2', 'x wird halbiert, also wird y verdoppelt: 24.', 'Halb so viel → doppelt so viel.')
SW.z('vervielfachen', 3, 'Indirekt proportional: Bei 6 Bussen sitzen 45 Kinder in jedem Bus. Wie viele sind es pro Bus bei 9 Bussen?', 30, '45 * 6 / 9',
     'Über die 3 Busse: 6 : 2 = 3 Busse → 90 Kinder pro Bus; 3 · 3 = 9 Busse → 90 : 3 = 30. Oder: 6 · 45 = 270 Kinder, 270 : 9 = 30.', 'Gehe über einen Zwischenschritt (z. B. 3 Busse).', einheit='Kinder', art='P')
SW.l('vervielfachen', 3, 'Die Tabelle gehört zu einer indirekten Proportionalität. Ergänze die beiden fehlenden Werte.', 'x = □; y = □', [6, 4], ['48 / 8', '48 / 12'],
     'Produkt: 3 · 16 = 48 (auch 4 · 12 = 48). Fehlender x-Wert: 48 : 8 = 6. Fehlender y-Wert: 48 : 12 = 4.', 'Bestimme zuerst das konstante Produkt.', 'Je Lücke eine ganze Zahl.',
     grafik={'typ': 'tabelle', 'kopf': ['x', '3', '4', '?', '12'], 'zeilen': [['y', '16', '12', '8', '?']]}, art='P')
SW.z('vervielfachen', 3, 'x und y sind indirekt proportional. x wird mit 1,5 multipliziert, danach ist y = 10. Wie groß war y vorher?', 15, '10 * 1.5',
     'x · 1,5 bedeutet y : 1,5. Rückwärts: vorher y = 10 · 1,5 = 15.', 'Rechne rückwärts: Was wurde mit y gemacht?', art='K')
SW.z('vervielfachen', 3, 'Die Paare (2 | a) und (8 | a − 6) gehören zu derselben indirekten Proportionalität. Bestimme a.', 8, '48 / 6',
     'Gleiche Produkte: 2a = 8(a − 6) ⇔ 2a = 8a − 48 ⇔ 6a = 48 ⇔ a = 8. Probe: 2 · 8 = 16 und 8 · 2 = 16.', 'Setze die beiden Produkte gleich.', art='K')

# produkt
SW.z('produkt', 2, 'Eine indirekte Proportionalität enthält das Paar (0,5 | 36). Welcher y-Wert gehört zu x = 4,5?', 4, '0.5 * 36 / 4.5', 'Produkt: 0,5 · 36 = 18. y = 18 : 4,5 = 4.',
     'Erst das Produkt, dann teilen.')
SW.a('produkt', 2, 'Eine indirekte Proportionalität enthält das Paar (3 | 20). Welches Paar passt NICHT dazu?', '(5 | 15)', ['(6 | 10)', '(12 | 5)', '(15 | 4)'],
     'Das Produkt muss 60 sein. 5 · 15 = 75, alle anderen ergeben 60.', 'Bilde jeweils x · y.')
SW.a('produkt', 3, 'An einer Wippe herrscht Gleichgewicht. Gemessen: 20 kg bei 3 m, 30 kg bei 2 m, 40 kg bei 1,6 m, 60 kg bei 1 m Abstand. Welcher Messwert passt nicht zur indirekten Proportionalität?',
     '40 kg bei 1,6 m', ['20 kg bei 3 m', '30 kg bei 2 m', '60 kg bei 1 m'],
     'Gewicht · Abstand: 60, 60, 64, 60. Nur 40 · 1,6 = 64 weicht ab; richtig wären 1,5 m.', 'Bilde für jeden Messwert das Produkt.', art='P')
SW.a('produkt', 3, 'In einer Tabellenkalkulation steht x in Spalte A. In Spalte B soll y einer indirekten Proportionalität mit x · y = 120 stehen. Welche Formel gehört in B2?', '=120/A2',
     ['=120*A2', '=A2/120', '=120-A2'], 'Aus x · y = 120 folgt y = 120 : x. Also =120/A2.', 'Stelle x · y = 120 nach y um.', art='P')
SW.z('produkt', 3, 'Ein Rechteck ist 9 cm lang und 2 cm breit. Ein zweites Rechteck mit demselben Flächeninhalt ist doppelt so lang wie breit. Wie breit ist es?', 3, '18 / 6',
     'Fläche 18 cm². Breite b, Länge 2b: 2b · b = 18 ⇔ b · b = 9 ⇔ b = 3 cm (Länge 6 cm).', 'Schreibe die Länge als 2 · b.', einheit='cm', art='K')
SW.z('produkt', 3, 'Bei einer indirekten Proportionalität ist y = 9, wenn x = 4. Für welches positive x sind x und y gleich groß?', 6, '36 / 6',
     'Produkt 36. x = y heißt x · x = 36, also x = 6 (6 · 6 = 36).', 'Welche Zahl mal sich selbst ergibt das Produkt?', art='K')

# dreisatz
SW.z('dreisatz', 2, '4 gleich starke Pumpen leeren ein Becken in 9 Stunden. Wie lange brauchen 6 Pumpen?', 6, '4 * 9 / 6', 'Eine Pumpe: 36 h. Sechs Pumpen: 36 : 6 = 6 h.', 'Erst auf eine Pumpe zurückrechnen.',
     einheit='h')
SW.z('dreisatz', 2, 'Ein Futtervorrat reicht für 15 Tiere 8 Tage. Für wie viele Tiere reicht er 12 Tage?', 10, '15 * 8 / 12', '15 · 8 = 120 Tierfuttertage. 120 : 12 = 10 Tiere.',
     'Hier ist die Anzahl der Tiere gesucht.', einheit='Tiere')
SW.z('dreisatz', 3, '8 Maler brauchen für einen Auftrag 15 Tage. Nach 3 Tagen fallen 2 Maler aus. Wie viele Tage dauert der Auftrag insgesamt?', 19, '3 + (8 * 15 - 8 * 3) / 6',
     'Gesamtarbeit: 8 · 15 = 120 Malertage. Nach 3 Tagen sind 24 erledigt, 96 fehlen. 6 Maler brauchen 96 : 6 = 16 Tage. Insgesamt 3 + 16 = 19 Tage.',
     'Rechne in Malertagen (Maler · Tage).', einheit='Tage', art='P')
SW.z('dreisatz', 3, 'Bei 90 km/h dauert eine Fahrt 40 Minuten. Wie schnell muss man fahren, um 10 Minuten früher anzukommen?', 120, '90 * 40 / 30',
     'Gleiche Strecke: Geschwindigkeit · Zeit bleibt gleich. 90 · 40 = v · 30 ⇔ v = 120 km/h.', 'Welche Fahrzeit ist gesucht? Dann Produkt gleich setzen.', einheit='km/h', art='P')
SW.z('dreisatz', 3, '3 Hühner legen in 3 Tagen 3 Eier. Wie viele Eier legen 6 Hühner in 6 Tagen (bei gleicher Legeleistung)?', 12, '3 * 2 * 2',
     'Doppelt so viele Hühner: doppelt so viele Eier (6 in 3 Tagen). Doppelt so viele Tage: nochmal doppelt (12). Beides ist direkt proportional.', 'Ändere eine Größe nach der anderen.', einheit='Eier', art='K')
SW.z('dreisatz', 3, 'Ein Rohr füllt einen Tank in 6 Stunden. Wie viele gleich starke Rohre braucht man mindestens, damit es weniger als 1,5 Stunden dauert?', 5, '6 // 1.5 + 1',
     'n Rohre brauchen 6 : n Stunden. 4 Rohre brauchen genau 1,5 h – nicht weniger. Also mindestens 5 Rohre (1,2 h).', 'Prüfe 4 Rohre genau.', einheit='Rohre', art='K')

# graph
SW.a('graph', 2, 'Liegt der Punkt Q(0,5 | 48) auf dem Graphen von y = 24 : x?', 'Ja, denn 0,5 · 48 = 24.', ['Nein, denn 48 > 24.', 'Nein, denn 48 : 0,5 = 96 ≠ 24.'],
     '0,5 · 48 = 24. Das Produkt stimmt, Q liegt auf dem Graphen.', 'Prüfe x · y.')
SW.z('graph', 2, 'Der Graph gehört zu einer indirekten Proportionalität und geht durch P(4 | 3). Welchen y-Wert hat er bei x = 6?', 2, '4 * 3 / 6', 'k = 4 · 3 = 12. Bei x = 6: y = 12 : 6 = 2.',
     'Bestimme zuerst k aus P.', grafik=_k(x=[0, 8], y=[0, 8], graphen=[{'art': 'hyperbel', 'a': 12, 'b': 0, 'c': 0, 'bereich': [1.5, 8]}], punkte=[{'x': 4, 'y': 3, 'name': 'P'}]))
SW.z('graph', 3, 'P(2 | 9) und Q(6 | 3) liegen auf derselben Hyperbel y = k : x. Jeder Punkt bildet mit dem Ursprung und den Achsen ein Rechteck. Um wie viel cm² unterscheiden sich die Flächeninhalte?', 0,
     '2 * 9 - 6 * 3', 'P: 2 · 9 = 18, Q: 6 · 3 = 18. Beide Rechtecke haben 18 cm² – Unterschied 0. Das gilt für alle Punkte der Hyperbel.', 'Fläche = x · y.', einheit='cm²', art='P')
SW.a('graph', 3, 'Eine Hyperbel einer indirekten Proportionalität geht durch P(3 | 4). Durch welchen Punkt geht sie außerdem?', '(6 | 2)', ['(6 | 8)', '(1 | 7)', '(2 | 5)'],
     'k = 3 · 4 = 12. Nur 6 · 2 = 12. (6 | 8) wäre direkt proportional gedacht, (1 | 7) und (2 | 5) haben die Summe 7 wie P.', 'Bilde das Produkt.', art='P')
SW.z('graph', 3, 'Die Hyperbel y = k : x und die Gerade y = x schneiden sich bei x = 5 (x > 0). Bestimme k.', 25, '5 * 5', 'Schnittpunkt (5 | 5) liegt auf der Hyperbel: k = 5 · 5 = 25.',
     'Welchen y-Wert hat die Gerade bei x = 5?', art='K')
SW.a('graph', 3, 'Für welche x > 0 liegt der Graph von y = 12 : x oberhalb der Geraden y = 3?', 'für 0 < x < 4', ['für x > 4', 'für x > 3', 'für alle x > 0'],
     'Bei x = 4 ist y = 3. Für kleinere x ist 12 : x größer als 3, für größere kleiner.', 'Wo ist 12 : x genau 3?', art='K')

# unterscheiden
SW.a('unterscheiden', 2, 'Welche Art von Zuordnung beschreibt y = 15 : x?', 'indirekt proportional', ['direkt proportional', 'weder noch', 'quadratisch'],
     'x · y = 15 ist konstant: indirekt proportional.', 'Multipliziere mit x.')
SW.a('unterscheiden', 2, 'Welche Art von Zuordnung zeigt die Tabelle?', 'weder noch', ['indirekt proportional', 'direkt proportional'],
     'Produkte: 10, 16, 10 – nicht gleich. Quotienten: 10, 4, 0,4 – nicht gleich. Also weder noch.', 'Prüfe Produkt und Quotient für alle Paare.',
     grafik={'typ': 'tabelle', 'kopf': ['x', '1', '2', '5'], 'zeilen': [['y', '10', '8', '2']]})
SW.a('unterscheiden', 3, 'Ein Auto braucht 6 Liter auf 100 km. Zuordnung A: gefahrene Strecke → verbrauchter Kraftstoff. Zuordnung B: Verbrauch pro 100 km → Strecke, die man mit 30 Litern fahren kann. Welche Arten sind das?',
     'A direkt, B indirekt proportional', ['A indirekt, B direkt proportional', 'beide direkt proportional', 'beide indirekt proportional'],
     'A: doppelte Strecke, doppelter Verbrauch. B: Braucht ein Auto doppelt so viel pro 100 km, kommt es mit 30 Litern nur halb so weit.', 'Prüfe jeweils „doppelt → doppelt“ oder „doppelt → halb“.', art='P')
SW.a('unterscheiden', 3, 'In einer Tabellenkalkulation steht in A2 bis A6 x, in B2 die Formel =36/A2 (nach unten kopiert) und in C2 =A2*B2. Was zeigt Spalte C?', 'überall 36 – ein Zeichen für indirekte Proportionalität',
     ['die Quotienten, die alle gleich sind', 'lauter verschiedene Zahlen', 'überall 1'], 'C berechnet x · y = x · (36 : x) = 36. Konstantes Produkt: indirekt proportional.', 'Setze für x eine Zahl ein, z. B. 4.', art='P')
SW.a('unterscheiden', 3, 'Welche Gleichung beschreibt eine indirekte Proportionalität?', 'y = 3/x', ['y = x/3', 'y = 3 − x', 'y = 1/(x + 3)'],
     'Nur bei y = 3/x ist x · y immer 3. y = x/3 ist direkt proportional. y = 1/(x + 3) ist auch eine Hyperbel, aber x · y ist nicht konstant (x = 1: 0,25; x = 2: 0,4).',
     'Prüfe, ob x · y überall gleich ist.', art='K')
SW.a('unterscheiden', 3, 'Die Zuordnung x → y ist indirekt proportional. Was gilt für die Zuordnung x → 1/y?', 'Sie ist direkt proportional.', ['Sie ist auch indirekt proportional.', 'Sie ist weder noch.',
     'Das hängt von den Zahlen ab.'], 'Aus y = k/x folgt 1/y = x/k = (1/k) · x – eine direkte Proportionalität.', 'Bilde den Kehrwert von k/x.', art='K')

# sach
SW.z('sach', 2, 'Mit einer Schrittlänge von 75 cm braucht jemand für einen Weg 1 200 Schritte. Wie viele Schritte sind es bei 60 cm Schrittlänge?', 1500, '75 * 1200 / 60',
     '75 cm · 1 200 = 90 000 cm Weg. 90 000 : 60 = 1 500 Schritte.', 'Der Weg bleibt gleich.', einheit='Schritte')
SW.z('sach', 2, 'Ein Saftvorrat füllt 30 Gläser zu je 0,2 l. Wie viele Gläser zu je 0,25 l kann man damit füllen?', 24, '30 * 0.2 / 0.25', 'Vorrat: 30 · 0,2 l = 6 l. 6 : 0,25 = 24 Gläser.',
     'Berechne zuerst den ganzen Vorrat.', einheit='Gläser')
SW.z('sach', 3, 'Kind A (35 kg) sitzt auf einer Wippe 1,6 m vom Drehpunkt entfernt. Kind B sitzt auf der anderen Seite 1,4 m vom Drehpunkt. Wie schwer muss B sein, damit die Wippe im Gleichgewicht ist?',
     40, '35 * 1.6 / 1.4', 'Gewicht · Abstand gleich: 35 · 1,6 = 56. B: 56 : 1,4 = 40 kg.', 'Das Produkt aus Gewicht und Abstand ist auf beiden Seiten gleich.', einheit='kg', art='P')
SW.z('sach', 3, 'Zahnrad A hat 40 Zähne und dreht sich 30-mal pro Minute. Es greift in Zahnrad B mit 24 Zähnen. Wie oft dreht sich B pro Minute?', 50, '40 * 30 / 24',
     'Pro Minute greifen 40 · 30 = 1 200 Zähne ineinander. B: 1 200 : 24 = 50 Umdrehungen. Das kleinere Rad dreht sich schneller.', 'Zähnezahl · Umdrehungen ist für beide Räder gleich.', art='P')
SW.z('sach', 3, 'Für eine Fahrt wird ein Bus gemietet und die Kosten werden geteilt. Fahren 5 Kinder mehr mit, zahlt jedes nur noch 30 € statt 36 €. Wie viele Kinder wollten ursprünglich mitfahren?', 25,
     '30 * 5 / (36 - 30)', 'Gesamtpreis gleich: 36 · n = 30 · (n + 5) ⇔ 6n = 150 ⇔ n = 25. Probe: 36 · 25 = 900 = 30 · 30.', 'Der Buspreis bleibt gleich. Stelle eine Gleichung mit n auf.', einheit='Kinder', art='K')
SW.z('sach', 3, 'Ein Läufer braucht für eine Runde 80 Sekunden. Wie lange braucht er, wenn er 25 % schneller läuft?', 64, '80 / 1.25',
     'Geschwindigkeit · 1,25 heißt Zeit : 1,25 = 80 : 1,25 = 64 s. Nicht 80 · 0,75 = 60 s.', 'Zeit und Geschwindigkeit sind indirekt proportional.', einheit='s', art='K')

baue = mit_schwer(baue, SW)
# ---- SCHWER ENDE ----

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, mit_befunden  # noqa: E402

BF = Befunde('groessen.indirekt', 13_8_15)
# c) Beinahe-Dublette (Freizeitpark dreimal mit gleichem Aufbau) → anderer Sachkontext, gleicher Gedanke
BF.ersetze('sach', 'Ein Freizeitpark: Eintritt 3 €, jede Fahrt 4 €. 3 Fahrten kosten mit Eintritt 15 €. Jemand rechnet für 6 Fahrten: 15 · 2 = 30 €. Stimmt das?', BF.A(
    'Eine Handwerkerin berechnet 40 € Anfahrt und 50 € je Arbeitsstunde. 2 Stunden kosten zusammen 140 €. Jemand rechnet für 4 Stunden: 140 · 2 = 280 €. Stimmt das?',
    'Nein: Die Anfahrt wird nur einmal bezahlt, es sind 240 €.',
    ['Ja, doppelt so viele Stunden kosten doppelt so viel.', 'Nein: Es sind 70 €, weil es indirekt proportional ist.'],
    'Die Zuordnung ist weder noch, weil die Anfahrt fest ist: 40 + 4 · 50 = 240 €.',
    'Wird jeder Betrag bei mehr Stunden mehrfach bezahlt?'))
BF.nicht_umgesetzt('erkennen S3 „… Je mehr, desto weniger, also indirekt proportional.“ (4×)', 'Kein Fehler; Übungsreihe zum selben Fehlschluss mit verschiedenen Beispielen.')
BF.nicht_umgesetzt('unterscheiden S1/S2 „Welche Art von Zuordnung zeigt die Tabelle?“ (11×)', 'Kein Fehler; Stufe 2 hat den zusätzlichen Ablenker „nicht zu entscheiden“ und andere Tabellen.')
BF.nicht_umgesetzt('sach S2 „Taxi … Was kosten 6 km?“ (weder noch)', 'Laut Befund gut als Abgrenzung; Lösung richtig.')
BF.nicht_umgesetzt('Überschneidung mit funktionen.gebrochen/„indirekt“', 'Reihenfolge im Plan (Haupt-Chat), keine einzelne Aufgabe.')
BF.fuer_sebastian('groessen.indirekt: lehrplan_gym leer und Überschneidung mit funktionen.gebrochen/„indirekt“ – Reihenfolge im Plan klären. Karten-Texte nicht geändert.')

baue = mit_befunden(baue, BF)
# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Kl. 8, siehe _durchsicht_kl8.py) ----
from _durchsicht_kl8 import Durchsicht, mit_durchsicht  # noqa: E402

DSX = Durchsicht('groessen.indirekt', 19_8_5)
# erkennen: viermal dieselbe „Je mehr, desto weniger“-Frage in Reihe → zwei ersetzt
DSX.ersetze('erkennen', '„Bergwanderung: Höhe → Temperatur: Je mehr, desto weniger, also indirekt proportional.“ Stimmt die Begründung?', DSX.A(
    'Bei einer Zuordnung gehört zu x = 2 der Wert y = 9 und zu x = 6 der Wert y = 3. Was kann man sicher sagen?',
    'Sie kann indirekt proportional sein, direkt proportional ist sie sicher nicht.',
    ['Sie ist sicher direkt proportional.', 'Sie ist sicher indirekt proportional.', 'Sie kann direkt proportional sein, indirekt sicher nicht.'],
    'x wird verdreifacht (2 → 6), y wird gedrittelt (9 → 3); das Produkt ist beide Male 18. Das passt zu indirekt proportional. Direkt proportional geht nicht, '
    'sonst müsste y auch dreimal so groß werden. Sicher ist es aber nur, wenn alle weiteren Paare auch das Produkt 18 haben.',
    'Was passiert mit y, wenn x dreimal so groß wird? Reichen zwei Paare für ein sicheres Urteil?'))
DSX.ersetze('erkennen', '„Gebrauchtwagen: Alter → Wert: Je mehr, desto weniger, also indirekt proportional.“ Stimmt die Begründung?', DSX.A(
    'Anzahl der Maler → Tage, bis ein Haus gestrichen ist. Was muss gleich bleiben, damit diese Zuordnung indirekt proportional ist?',
    'Dasselbe Haus und gleich schnell arbeitende Maler.', ['Die Zahl der Tage.', 'Die Zahl der Maler.', 'Nichts, das gilt immer.'],
    'Indirekt proportional heißt: Das Produkt Maler · Tage (die Arbeit) bleibt gleich. Das stimmt nur bei derselben Arbeit und wenn jeder Maler gleich viel schafft.',
    'Was gibt das Produkt Maler · Tage an?'))
DSX.stufen('erkennen', 'S1 doppelt → halb prüfen; S2 indirekte Zuordnung auswählen, Messwerte prüfen; S3 viermal dieselbe „Je mehr, desto weniger“-Frage',
          'S1 doppelt → halb prüfen; S2 auswählen, Messwerte prüfen; S3 Begründungen bewerten, aus zwei Paaren schließen, Bedingungen des Modells, Prozent-Änderung')
# vervielfachen: fehlenden x-Wert suchen ist eine Umkehrung (Stufe 2), kein neuer Gedanke
for _w in (5, 6, 10, 4):
    DSX.stufe('vervielfachen', 'Die Zuordnung ' + {5: 'Pumpen → Stunden', 6: 'Personen → Stunden', 10: 'Personen → Stunden', 4: 'Helfer → Minuten'}[_w]
             + ' ist indirekt proportional. Welcher x-Wert fehlt?', 2, enthaelt=f'"wert": {_w}')
DSX.stufen('vervielfachen', 'S1/S2 Tabelle mit Faktor ergänzen; S3 fünfmal fehlender x-Wert (Umkehrung)',
          'S1 Tabelle mit ganzem Faktor; S2 Faktor nicht ganz, x-Wert gesucht, Einkleidung; S3 Zwischenschritt, zwei Lücken, Faktor 1,5 rückwärts, Parameter a')
# dreisatz: viermal derselbe Fehler „geteilt statt mal“ in Reihe → zwei durch andere Stufe-3-Gedanken ersetzt
DSX.ersetze('dreisatz', '3 Bagger heben eine Baugrube in 13 Tagen aus. Wie lange brauchen 6 Bagger? Jemand rechnet: 13 : 3 · 6 = 26 Tage. Was ist falsch?', DSX.Z(
    'Mit 4 gleich starken Pumpen dauert das Leeren eines Beckens 9 Stunden. Es soll höchstens 6 Stunden dauern. Wie viele Pumpen braucht man mindestens?', 6, '4 * 9 / 6',
    'Arbeit: 4 · 9 = 36 Pumpenstunden. In 6 Stunden schaffen das 36 : 6 = 6 Pumpen. Mit 5 Pumpen dauert es 7,2 h – zu lange.',
    'Rechne die Arbeit in Pumpenstunden aus. Wie viele Pumpen schaffen sie in 6 Stunden?', einheit='Pumpen'))
DSX.ersetze('dreisatz', '10 Helfer räumen eine Turnhalle in 51 Minuten auf. Wie lange brauchen 4 Helfer? Jemand rechnet: 51 : 10 · 4 = 20,4 Minuten. Was ist falsch?', DSX.Z(
    'Ein Futtervorrat reicht für 20 Schafe 30 Tage. Wie viele Schafe muss der Schäfer verkaufen, damit der Vorrat 40 Tage reicht?', 5, '20 - 20 * 30 / 40',
    'Vorrat: 20 · 30 = 600 Schaftage. Für 40 Tage reicht er für 600 : 40 = 15 Schafe. Verkaufen: 20 − 15 = 5 Schafe.',
    'Für wie viele Schafe reicht der Vorrat 40 Tage? Gefragt ist der Unterschied.', einheit='Schafe'))
DSX.stufen('dreisatz', 'S1 über die Einheit; S2 zwei Schritte, Rechnung wählen; S3 viermal derselbe Fehler',
          'S1 über die Einheit; S2 zwei Schritte, Rechnung wählen; S3 Fehler finden, Mindestanzahl, Verkauf, Ausfall mitten im Vorgang, Geschwindigkeit, zwei Größen gleichzeitig')
# graph: Bedeutung eines Punktes und y-Wert ablesen sind kein Stufe-3-Gedanke
for _p in ('P(12 | 3)', 'P(6 | 4)', 'P(2 | 12)'):
    _f = '36' if _p == 'P(12 | 3)' else '24'
    DSX.stufe('graph', f'Alle Rechtecke mit {_f} cm² Flächeninhalt: Breite x → Länge y. Der Punkt {_p} liegt auf dem Graphen. Was bedeutet der Punkt?', 2)
DSX.stufe('graph', 'Der Graph gehört zu y = 6 : x. Welchen y-Wert hat er bei x = 8? (Dezimalzahl)', 1)
DSX.stufen('graph', 'S1 k bestimmen; S2 Punktprobe; S3 teils Punkt deuten und Wert ablesen',
          'S1 k bestimmen, Wert ablesen; S2 Punktprobe, Punkt deuten; S3 zwei Hyperbeln unterscheiden, gleiche Rechteckflächen, Schnitt mit y = x, Bereich oberhalb')
# unterscheiden: Stufe 1 und 2 waren dieselbe Tabellenfrage → vier nach Stufe 1, zwei neue Stufe-2-Aufgaben
for _a in ['["indirekt proportional", "weder noch", "nicht zu entscheiden", "direkt proportional"]',
           '["weder noch", "direkt proportional", "nicht zu entscheiden", "indirekt proportional"]',
           '["weder noch", "nicht zu entscheiden", "direkt proportional", "indirekt proportional"]',
           '["indirekt proportional", "nicht zu entscheiden", "weder noch", "direkt proportional"]']:
    DSX.stufe('unterscheiden', 'Welche Art von Zuordnung zeigt die Tabelle?', 1, enthaelt=_a)
DSX.stufe('unterscheiden', 'Die Zuordnung ist indirekt proportional. Ergänze den fehlenden Wert.', 2, enthaelt='"wert": 3')
DSX.stufe('unterscheiden', 'Die Zuordnung ist indirekt proportional. Ergänze den fehlenden Wert.', 2, enthaelt='"wert": 5')
DSX.neu('unterscheiden', 2, DSX.Z('Die Zuordnung soll direkt proportional sein und enthält das Paar (4 | 10). Welcher y-Wert gehört zu x = 6?', 15, '10 / 4 * 6',
                                'Direkt proportional: gleicher Quotient. 10 : 4 = 2,5, also y = 2,5 · 6 = 15. (Indirekt wäre es 40 : 6.)',
                                'Direkt: Der Quotient y : x bleibt gleich.'))
DSX.neu('unterscheiden', 2, DSX.A('Eine Zuordnung enthält die Paare (2 | 6) und (6 | 2). Welche Art kann sie NICHT sein?', 'direkt proportional',
                                ['indirekt proportional', 'weder noch', 'Man kann keine ausschließen.'],
                                'Quotienten: 6 : 2 = 3, aber 2 : 6 = 1/3 – verschieden, also nicht direkt proportional. Produkte: 12 und 12 – indirekt ist möglich, ebenso weder noch.',
                                'Vergleiche die Quotienten und die Produkte der beiden Paare.'))
DSX.stufen('unterscheiden', 'S1 und S2 dieselbe Tabellenfrage; S3 teils Tabelle ergänzen wie Stufe 1',
          'S1 Art der Tabelle bestimmen; S2 Term zuordnen, Tabelle passend ergänzen, Art ausschließen; S3 Begründung bewerten, zwei Zuordnungen im Sachkontext, Tabellenkalkulation, x → 1/y')
# sach: Fahrzeiten wie auf Stufe 2
DSX.stufe('sach', 'Bei 60 km/h dauert eine Fahrt 120 Minuten. Wie viele Minuten dauert sie bei 100 km/h?', 2)
DSX.stufe('sach', 'Bei 80 km/h dauert eine Fahrt 90 Minuten. Wie viele Minuten dauert sie bei 150 km/h?', 2)
DSX.stufen('sach', 'S1 einfache Sachaufgabe; S2 Einkleidungen; S3 teils Fahrzeit wie S2',
          'S1 einfache Sachaufgabe; S2 Einkleidungen (Fliesen, Müsli, Fahrzeit), direkt oder indirekt?; S3 Fehler bei Grundgebühr, Wippe, Zahnrad, Gleichung mit Unbekannter, Prozent')
DSX.stufen('produkt', 'S1 Produkt bilden, Wert ergänzen; S2 Tabelle prüfen; S3 Fehler in Tabelle, Preisgeld rückwärts, Wippe, Tabellenkalkulation, x = y')
DSX.fuer_sebastian('groessen.indirekt überschneidet sich stark mit funktionen.gebrochen (Karten „indirekt“ und – seit der Achtzehnten Runde – „indirekt_sach“): '
                  'Doppelt → halb, Produktgleichheit, Dreisatz umgekehrt, Hyperbel und dieselben Pumpen-/Vorrat-Aufgaben kommen in beiden Flügen vor.')
baue = mit_durchsicht(baue, DSX)
# ---- DURCHSICHT ENDE ----

# ---- STUFEN (Zwanzigste Runde: echte Stufe 3 und Knobel-Bordkarten, siehe _stufen_kl8.py) ----
from _stufen_kl8 import Stufen, mit_stufen  # noqa: E402

ST = Stufen('groessen.indirekt', 20_8_14)
SA, SZ, SL = ST.A, ST.Z, ST.L
def T(lz, *regeln):
    for m, g in regeln: ST.typ(lz, m, g)

# --- erkennen ---
ST.leiter('erkennen', 'an einer Situation entscheiden, ob „doppelt → halb“ gilt',
          'passende Situation auswählen, Wertepaare mit dem Produkt prüfen, Gegenbeispiele (Quadrat, fester Umfang)',
          '„Je mehr, desto weniger“ als Fehlschluss, Bedingungen begründen, Prozentänderung, y = 2/x, Messwerte wie in einer Prüfung')
T('erkennen', (r'Seitenlänge eines Quadrats|Umfang 20 cm|Kann das indirekt proportional sein', 'mehrschritt'), (r'^Ist diese Zuordnung indirekt', 'erkennen'),
  (r'^Welche Zuordnung ist indirekt', 'einkleidung'), (r'Stimmt die Begründung|Was muss gleich bleiben', 'begruenden'), (r'Was kann man sicher sagen|y = 2/x', 'transfer'),
  (r'2 Maschinen|^Messwerte', 'pruefung'), (r'Welche Begründung', 'verknuepfen'), (r'50 %', 'parameter'))
ST.neu('erkennen', 'direkt', SZ('x und y sind indirekt proportional. Zu x = 3 gehört y = 8. Welcher y-Wert gehört zu x = 6?', 4, '3 * 8 / 6', 'Doppeltes x → halbes y: 8 : 2 = 4.', 'Doppelt so viel → halb so viel.'))
ST.neu('erkennen', 'darstellung', SA('Welche Wertetabelle kann zu einer indirekten Proportionalität gehören?', 'x: 1, 2, 4 → y: 12, 6, 3', ['x: 1, 2, 4 → y: 3, 6, 12', 'x: 1, 2, 4 → y: 12, 10, 8', 'x: 1, 2, 4 → y: 12, 6, 2'],
    'Nur dort ist x · y immer 12. Bei 12, 10, 8 nimmt y zwar ab, aber das Produkt ändert sich; bei 12, 6, 2 ist das letzte Produkt 8.', 'Bilde für jede Tabelle alle Produkte x · y.'))
ST.knobel('erkennen', SZ('x und y sind indirekt proportional. Vergrößert man x um 3, wird y halbiert. Wie groß ist x?', 3, '3',
    'Das Produkt bleibt gleich: x · y = (x + 3) · y/2 ⇒ 2x = x + 3 ⇒ x = 3. Probe: aus x = 3 wird 6 – das ist das Doppelte, also halbiert sich y.', 'Halbes y heißt: Das neue x muss das Doppelte des alten sein.'))
ST.knobel('erkennen', SA('Zu einer Zuordnung gehören die Paare (2 | 12), (3 | 8) und (6 | 5). Was stimmt?', 'Sie ist nicht indirekt proportional; schon ein Paar mit anderem Produkt genügt als Gegenbeispiel.',
    ['Sie ist indirekt proportional, weil zwei Paare das Produkt 24 haben.', 'Sie ist direkt proportional.', 'Man kann es erst mit mehr Paaren entscheiden.'],
    '2 · 12 = 24, 3 · 8 = 24, aber 6 · 5 = 30. Für eine indirekte Proportionalität müssten ALLE Produkte gleich sein – ein abweichendes Paar widerlegt sie.', 'Prüfe wirklich jedes Paar.'))

# --- vervielfachen ---
ST.leiter('vervielfachen', 'fehlenden Wert mit „doppelt → halb“ ergänzen',
          'nicht ganzzahlige Faktoren, x-Wert gesucht, Sachpaare (Pferde, Pumpen), Faktor 0,5',
          'Zwischenschritt verknüpfen, Busse als Transfer, zwei Lücken, rückwärts zum alten y, Parameter a, Fehler „mal statt geteilt“, begründen, Prüfungsauswahl')
T('vervielfachen', (r'Zwischenschritt|beiden fehlenden', 'verknuepfen'), (r'Welcher x-Wert fehlt', 'umkehr'), (r'Pferde|2 Pumpen brauchen|^Indirekt proportional: \d+ Pumpen', 'einkleidung'), (r'2,5', 'mehrschritt'),
  (r'Bussen', 'transfer'), (r'1,5 multipliziert', 'rueckwaerts'), (r'\(2 \| a\)', 'parameter'))
ST.typ('vervielfachen@1', r'Ergänze den fehlenden Wert\.$', 'direkt')
ST.typ('vervielfachen@2', r'Ergänze den fehlenden Wert\.$', 'mehrschritt')
ST.neu('vervielfachen', 'erkennen', SA('x und y sind indirekt proportional. x wird mit 4 multipliziert. Was passiert mit y?', 'y wird durch 4 geteilt.', ['y wird mit 4 multipliziert.', 'y wird um 4 kleiner.', 'y bleibt gleich.'],
    'Das Produkt x · y bleibt gleich: Was x vervielfacht, muss y ausgleichen.', 'Was bleibt bei einer indirekten Proportionalität gleich?'))
ST.neu('vervielfachen', 'fehler', SA('Indirekt proportional: 4 Personen brauchen 6 Stunden. Jemand rechnet für 8 Personen: 6 · 2 = 12 Stunden. Was stimmt?', 'Falsch: Doppelt so viele Personen brauchen halb so lange, also 3 Stunden.',
    ['Richtig.', 'Falsch: Es sind 6 + 4 = 10 Stunden.', 'Falsch: Es sind 6 − 2 = 4 Stunden.'], 'Er hat wie bei einer direkten Proportionalität gerechnet. Probe: 4 · 6 = 24 = 8 · 3.', 'Prüfe mit dem Produkt.'))
ST.neu('vervielfachen', 'begruenden', SA('Warum darf man bei einer indirekten Proportionalität aus (6 | 10) direkt auf (2 | 30) schließen?', 'Weil x durch 3 geteilt wird und y deshalb mit 3 multipliziert werden muss – das Produkt bleibt 60.',
    ['Weil 6 − 4 = 2 und 10 + 20 = 30.', 'Weil man immer mit 3 multipliziert.', 'Weil 2 und 30 beide gerade sind.'], 'Der Faktor bei x und der Faktor bei y sind Kehrwerte: : 3 und · 3.', 'Mit welchem Faktor wird x verändert?'))
ST.neu('vervielfachen', 'pruefung', SZ('Ein Vorrat reicht 12 Tieren 15 Tage. Nach 5 Tagen kommen 3 Tiere dazu. Wie viele Tage reicht der Rest dann noch?', 8, '12 * 10 / 15',
    'Nach 5 Tagen reicht der Rest für 12 Tiere noch 10 Tage. Mit 15 Tieren: 12 · 10 : 15 = 8 Tage.', 'Rechne zuerst, wie lange der Rest für die alten Tiere gereicht hätte.', einheit='Tage'))
ST.knobel('vervielfachen', SZ('x und y sind indirekt proportional. Wird x um 2 vergrößert, wird y um 2 kleiner; vorher war y = 6. Wie groß war x?', 4, '4',
    'Mit k = x · y gilt x · 6 = (x + 2) · 4 ⇒ 6x = 4x + 8 ⇒ x = 4. Probe: 4 · 6 = 24 = 6 · 4.', 'Setze die beiden Produkte gleich.'))
ST.knobel('vervielfachen', SZ('x und y sind indirekt proportional. Erst wird x verdoppelt, dann wird das neue x noch einmal um 50 % vergrößert. Auf welchen Bruchteil des Anfangswerts sinkt y? Gib ihn als Dezimalzahl auf drei Stellen an.', 0.333, 'round(1/3, 3)',
    'x wird insgesamt mit 2 · 1,5 = 3 multipliziert. y wird also durch 3 geteilt: 1/3 ≈ 0,333.', 'Fasse beide Veränderungen von x zu einem Faktor zusammen.', toleranz=0.001))

# --- produkt ---
ST.leiter('produkt', 'konstantes Produkt bilden und damit einen y-Wert ergänzen',
          'Tabelle auf gleiche Produkte prüfen, Dezimalwerte ergänzen, unpassendes Paar finden',
          'Fehler in der Tabelle finden, Preisgeld rückwärts, Wippe und Tabellenkalkulation, Rechteck verknüpfen, x = y als Parameter')
T('produkt', (r'Ergänze den fehlenden y-Wert', 'direkt'), (r'konstante Produkt', 'erkennen'), (r'Ist die Zuordnung in der Tabelle', 'darstellung'), (r'4,5', 'mehrschritt'), (r'NICHT', 'umkehr'),
  (r'Fehler eingeschlichen', 'fehler'), (r'Preisgeld', 'rueckwaerts'), (r'Wippe|Tabellenkalkulation', 'transfer'), (r'Rechteck', 'verknuepfen'), (r'gleich groß', 'parameter'))
ST.typ('produkt@2', r'Ergänze den fehlenden Wert\.$', 'mehrschritt')
ST.typ('produkt@3', r'Ergänze den fehlenden Wert\.$', 'verknuepfen')
ST.knobel('produkt', SZ('In einer Tabelle einer indirekten Proportionalität stehen die Paare (x | 18) und (x + 3 | 12). Wie groß ist x?', 6, '3 * 12 / (18 - 12)',
    'x · 18 = (x + 3) · 12 ⇒ 18x = 12x + 36 ⇒ x = 6. Probe: 6 · 18 = 108 = 9 · 12.', 'Beide Paare haben dasselbe Produkt.'))
ST.knobel('produkt', SZ('Bei einer indirekten Proportionalität ist das Produkt 36. Wie viele Paare aus zwei natürlichen Zahlen (x | y) gehören dazu?', 9, '9',
    'x muss ein Teiler von 36 sein: 1, 2, 3, 4, 6, 9, 12, 18, 36 – neun Teiler, also neun Paare (1 | 36), (2 | 18), …, (36 | 1).', 'Welche x sind möglich, wenn y eine natürliche Zahl sein soll?'))

# --- dreisatz ---
ST.leiter('dreisatz', 'Dreisatz: auf eine Einheit (mal), dann auf den gesuchten Wert (geteilt)',
          'krumme Ergebnisse, passende Rechnung erkennen, Tiere aus Tagen rückwärts',
          'Fehler „geteilt statt mal“, Anzahl für eine Frist rückwärts, Ausfall nach Tagen verknüpfen, Geschwindigkeit, Hühner-Rätsel wie im Wettbewerb, Mindestzahl')
T('dreisatz', (r'allein\?$', 'direkt'), (r'Jemand rechnet', 'fehler'), (r'höchstens|verkaufen|nur 18 Tage', 'rueckwaerts'), (r'fallen', 'verknuepfen'), (r'km/h|Rohr', 'transfer'), (r'Hühner', 'pruefung'),
  (r'Mit welcher Rechnung', 'darstellung'), (r'Für wie viele Tiere', 'umkehr'))
ST.typ('dreisatz@1', r'Wie lange brauchen', 'direkt')
ST.typ('dreisatz@2', r'Wie lange brauchen \d+ \w+\?$', 'mehrschritt')
ST.neu('dreisatz', 'erkennen', SA('5 Helfer brauchen 12 Minuten. Was ist beim Dreisatz der erste Schritt?', 'Ein Helfer braucht 5 · 12 = 60 Minuten.', ['Ein Helfer braucht 12 : 5 = 2,4 Minuten.', 'Ein Helfer braucht 12 Minuten.', 'Ein Helfer braucht 12 − 5 = 7 Minuten.'],
    'Weniger Helfer brauchen länger: Für einen Helfer wird multipliziert.', 'Braucht ein Helfer allein länger oder kürzer?'))
ST.knobel('dreisatz', SZ('Pumpe A leert ein Becken allein in 6 Stunden, Pumpe B allein in 3 Stunden. Wie viele Stunden brauchen beide zusammen?', 2, '1 / (1/6 + 1/3)',
    'In einer Stunde schafft A 1/6, B 1/3 = 2/6 des Beckens; zusammen 3/6 = 1/2. Das ganze Becken dauert also 2 Stunden.', 'Welchen Teil des Beckens schafft jede Pumpe in einer Stunde?', einheit='h'))
ST.knobel('dreisatz', SZ('6 Arbeiter wollen eine Arbeit in 10 Tagen schaffen. Nach 4 Tagen soll sie 2 Tage früher fertig werden als geplant. Wie viele Arbeiter müssen insgesamt arbeiten?', 9, '6 * 6 / 4',
    'Rest: 6 Tage für 6 Arbeiter = 36 Arbeitertage. Neu bleiben nur 10 − 2 − 4 = 4 Tage: 36 : 4 = 9 Arbeiter.', 'Rechne den Rest in „Arbeitertagen“.'))

# --- graph ---
ST.leiter('graph', 'Punkte auf y = k : x ablesen bzw. k bestimmen',
          'Punkt auf der Hyperbel prüfen, Graph auswählen, Punkt im Sachzusammenhang deuten, y aus einem Punkt',
          'zwei Hyperbeln verknüpfen, Rechtecke begründen, Schnitt mit y = x, oberhalb einer Geraden, falsche Graphen-Aussage, k rückwärts aus Fläche, Tabelle zu Graph')
T('graph', (r'y = x schneiden', 'parameter'), (r'Welche Aussage über den Graphen', 'erkennen'), (r'Welchen y-Wert hat er bei', 'direkt'), (r'Bestimme k\.$', 'direkt'), (r'^Liegt der Punkt', 'darstellung'), (r'Welcher Graph', 'darstellung'),
  (r'Welchen y-Wert hat die Hyperbel|geht durch P\(4', 'mehrschritt'), (r'Rechtecke mit', 'einkleidung'), (r'Rechteck$|Rechteck\b', 'begruenden'), (r'y = 6 : x und|oberhalb', 'verknuepfen'),
  (r'außerdem', 'pruefung'), (r'y = x schneiden', 'parameter'))
ST.neu('graph', 'fehler', SA('Jemand sagt: „Der Graph von y = 12 : x schneidet die x-Achse bei x = 12.“ Was stimmt?', 'Falsch: y = 12 : x wird nie 0, der Graph erreicht die x-Achse nicht.',
    ['Richtig.', 'Falsch: Er schneidet sie bei x = 1.', 'Falsch: Er schneidet sie bei x = 0.'], 'Bei x = 12 ist y = 1, nicht 0. Ein Quotient 12 : x ist nie 0 – die Hyperbel kommt der Achse nur immer näher.', 'Berechne y bei x = 12.'))
ST.neu('graph', 'rueckwaerts', SZ('Ein Punkt P der Hyperbel y = k : x (x > 0) bildet mit dem Ursprung und den Achsen ein Rechteck mit 18 cm² Flächeninhalt (1 LE = 1 cm). Wie groß ist k?', 18, '18',
    'Das Rechteck hat die Seiten x und y, also den Flächeninhalt x · y = k = 18.', 'Wie lang sind die Seiten des Rechtecks?'))
ST.neu('graph', 'transfer', SA('Eine Wertetabelle enthält (1 | 20), (2 | 10), (4 | 5), (5 | 4). Wie sieht der Graph aus?', 'eine Kurve, die von links oben nach rechts unten fällt und immer flacher wird',
    ['eine fallende Gerade', 'eine steigende Gerade durch den Ursprung', 'eine Kurve, die die x-Achse bei x = 20 trifft'],
    'Alle Produkte sind 20: Hyperbel y = 20 : x. Sie fällt erst steil (von 20 auf 10), dann immer flacher (von 5 auf 4).', 'Prüfe die Produkte und wie stark y jeweils fällt.'))
ST.knobel('graph', SZ('Die Hyperbeln y = 8 : x und y = 2 · x schneiden sich für x > 0 in einem Punkt. Welche x-Koordinate hat er?', 2, '2',
    '8 : x = 2x ⇒ 2x² = 8 ⇒ x² = 4 ⇒ x = 2 (x > 0). Probe: 8 : 2 = 4 = 2 · 2.', 'Setze beide Terme gleich und multipliziere mit x.'))
ST.knobel('graph', SZ('Auf der Hyperbel y = 24 : x liegen A(2 | 12) und B(6 | 4). Wie groß ist die Fläche des Dreiecks aus A, B und dem Punkt C(6 | 12)?', 16, '(6 - 2) * (12 - 4) / 2',
    'Bei C ist ein rechter Winkel: AC ist waagrecht (Länge 6 − 2 = 4), BC senkrecht (Länge 12 − 4 = 8). Fläche 4 · 8 : 2 = 16.', 'Zeichne die drei Punkte ein.', einheit='FE'))

# --- unterscheiden ---
ST.leiter('unterscheiden', 'an einer Tabelle direkt, indirekt oder weder noch erkennen',
          'Terme zuordnen, fehlenden Wert passend ergänzen, Art ausschließen',
          'Begründung mit „kleiner werdend“ prüfen, lineare Funktion, zwei Zuordnungen verknüpfen, Tabellenkalkulation, Kehrwert begründen, aus Paar rückwärts')
T('unterscheiden', (r'Ergänze den fehlenden Wert', 'mehrschritt'), (r'y = 15 : x', 'darstellung'), (r'soll direkt proportional', 'mehrschritt'), (r'NICHT', 'umkehr'),
  (r'weil die y-Werte', 'fehler'), (r'20 − 3|Tabellenkalkulation', 'transfer'), (r'6 Liter', 'verknuepfen'), (r'Welche Gleichung', 'pruefung'), (r'1/y', 'begruenden'))
ST.typ('unterscheiden@1', r'^Welche Art von Zuordnung zeigt', 'erkennen')
ST.typ('unterscheiden@2', r'^Welche Art von Zuordnung zeigt', 'darstellung')
ST.neu('unterscheiden', 'direkt', SZ('Eine Zuordnung ist direkt proportional mit dem Paar (3 | 12). Welcher y-Wert gehört zu x = 5?', 20, '12 / 3 * 5', 'Quotient y : x = 4. Zu x = 5 gehört 20.', 'Bei direkter Proportionalität ist y : x gleich.'))
ST.neu('unterscheiden', 'direkt', SZ('x und y sind indirekt proportional, (4 | 15) gehört dazu. Welcher y-Wert gehört zu x = 10?', 6, '4 * 15 / 10', 'Produkt 60. 60 : 10 = 6.', 'Bei indirekter Proportionalität ist x · y gleich.'))
ST.neu('unterscheiden', 'rueckwaerts', SA('Zu einer Zuordnung gehört y = 4 bei x = 6. Bei x = 3 ist y = 8. Welche Art kann sie sein?', 'indirekt proportional (oder weder noch), aber nicht direkt proportional',
    ['nur direkt proportional', 'sicher indirekt proportional', 'direkt oder indirekt proportional'], 'Beide Produkte sind 24, also passt indirekt. Direkt ginge nicht (4 : 6 ≠ 8 : 3). Zwei Paare reichen aber nicht, um „weder noch“ auszuschließen.',
    'Prüfe Produkt und Quotient – und überlege, was zwei Paare sicher zeigen.'))
ST.knobel('unterscheiden', SZ('Eine direkt proportionale und eine indirekt proportionale Zuordnung gehen beide durch (2 | 6). Die indirekte hat bei x = 4 den y-Wert a, die direkte bei x = 4 den y-Wert b. Wie groß ist b − a?', 9, '3*4 - 12/4',
    'Direkt: y = 3x, bei x = 4 also b = 12. Indirekt: x · y = 12, bei x = 4 also a = 3. b − a = 9.', 'Bestimme zuerst den Quotienten bzw. das Produkt aus (2 | 6).'))
ST.knobel('unterscheiden', SA('Bei einer Zuordnung ist y : x für alle Paare gleich UND x · y für alle Paare gleich. Wie viele verschiedene Paare (mit x > 0) kann sie höchstens haben?', 'nur eines',
    ['zwei', 'unendlich viele', 'keines'], 'Aus y = q · x und x · y = k folgt q · x² = k: Für x > 0 gibt es nur ein x. Eine Zuordnung kann also nicht zugleich direkt und indirekt proportional sein, außer mit einem einzigen Paar.',
    'Setze y = q · x in x · y = k ein.'))

# --- sach ---
ST.leiter('sach', 'einfache Sachaufgaben (Vorrat, Gewinn, Fahrzeit) mit indirekter Proportionalität',
          'Fliesen, Müsli, Fahrzeit, Gläser, Schritte; direkt oder indirekt? Werte rückwärts',
          'Fehler bei Grundgebühr, Wippe und Zahnrad übertragen, Bus mieten rückwärts, Prozent verknüpfen, Prüfungsaufgabe mit Zwischenstand')
T('sach', (r'Grundgebühr|Taxifahrt', 'mehrschritt'), (r'Jemand rechnet', 'fehler'), (r'Wippe|Zahnrad', 'transfer'), (r'gemietet', 'rueckwaerts'), (r'25 %', 'verknuepfen'),
  (r'Fliesen', 'mehrschritt'), (r'Müsli|Fahrrad|Minuten dauert sie|Maler|Schrittl|Saft', 'einkleidung'))
ST.typ('sach', r'Heuvorrat|Gewinn wird|Bei 50 km/h|Schullandheim', 'direkt')
ST.neu('sach', 'erkennen', SA('Ein Heuvorrat soll für mehr Pferde reichen. Wie ändert sich die Zahl der Tage?', 'Sie wird kleiner: doppelt so viele Pferde → halb so viele Tage.', ['Sie wird größer.', 'Sie bleibt gleich.', 'Sie wird um die Zahl der neuen Pferde kleiner.'],
    'Mehr Fresser leeren den Vorrat schneller; Pferde · Tage bleibt gleich.', 'Was bleibt gleich: der Vorrat oder die Tage?'))
ST.neu('sach', 'umkehr', SZ('Ein Weg wird mit 4 km/h in 45 Minuten zurückgelegt. Wie schnell muss man gehen, um nur 30 Minuten zu brauchen?', 6, '4 * 45 / 30', 'km/h · Minuten bleibt gleich: 4 · 45 = 180. 180 : 30 = 6 km/h.', 'Welches Produkt bleibt gleich?', einheit='km/h'))
ST.neu('sach', 'pruefung', SZ('Eine Klasse möchte für die Abschlussfahrt einen Bus für 540 € mieten; die Kosten werden gleich aufgeteilt. Erst sagen 18 Kinder zu, später kommen 9 dazu. Um wie viel Euro sinkt der Anteil für jedes Kind?', 10, '540 / 18 - 540 / 27',
    'Vorher 540 : 18 = 30 €, nachher 540 : 27 = 20 €. Er sinkt um 10 €.', 'Berechne beide Anteile.', einheit='€'))
ST.knobel('sach', SZ('Ein Vorrat reicht 10 Hühnern 30 Tage. Nach 6 Tagen werden 2 Hühner verschenkt, nach weiteren 10 Tagen kommen 8 Hühner dazu. Wie viele Tage reicht der Vorrat ab diesem Zeitpunkt noch?', 10, '(10*30 - 10*6 - 8*10) / 16',
    'Vorrat = 10 · 30 = 300 Hühnertage. Verbraucht: 10 · 6 = 60 und 8 · 10 = 80. Rest 160 Hühnertage für 8 + 8 = 16 Hühner: 160 : 16 = 10 Tage.',
    'Rechne mit „Hühnertagen“ statt mit Tagen.', einheit='Tage'))
ST.knobel('sach', SZ('Zahnrad A (36 Zähne) treibt Zahnrad B (24 Zähne), B treibt C (12 Zähne). A dreht sich 10-mal pro Minute. Wie oft dreht sich C pro Minute?', 30, '36 * 10 / 12',
    'Pro Minute greifen bei A 360 Zähne ein, also auch bei B und C. C: 360 : 12 = 30 Umdrehungen. Das mittlere Rad ändert daran nichts.', 'Wie viele Zähne laufen pro Minute an jedem Rad vorbei?', einheit='Umdrehungen'))
baue = mit_stufen(baue, ST)
# ---- STUFEN ENDE ----

# ---------- TEXT: Zweiundzwanzigste Runde (18.11., Auftrag des Lehrers) – mehr Textaufgaben, siehe _text_kl8.py ----------
from _text_kl8 import Text, mit_text, text_auf_datei  # noqa: E402
TX = Text('groessen.indirekt', 22_8_14)
TZ, TA, TL, TW = TX.Z, TX.A, TX.L, TX.W

TX.huerde_alt('erkennen', r'Ist die Zuordnung Arbeiter → Zeit indirekt proportional', 'entscheidung')
TX.huerde_alt('erkennen', r'Ein Handyakku.*Stimmt die Begründung', 'entscheidung')
TX.huerde_alt('vervielfachen', r'Nach 5 Tagen kommen 3 Tiere dazu', 'zwei')
TX.huerde_alt('dreisatz', r'Es soll höchstens 6 Stunden dauern', 'deuten')
TX.huerde_alt('dreisatz', r'weniger als 1,5 Stunden', 'deuten')
TX.huerde_alt('sach', r'Erst sagen 18 Kinder zu', 'zwei')
TX.huerde_alt('sach', r'3 Fahrten kosten mit Eintritt 15 €', 'entscheidung')

# --- vervielfachen ---
TX.u('vervielfachen', 'pruefung', TZ('Für einen Umzug fahren 2 gleich große Transporter je 12-mal. Ein Transporter kostet 90 € Miete am Tag. Wie oft muss jeder Transporter fahren, wenn man 3 davon mietet?', '2 * 12 / 3',
    TW('2 Transporter je 12 Fahrten; Miete spielt keine Rolle.', 'Fahrten je Transporter bei 3 Transportern.', 'Die Gesamtzahl der Fahrten bleibt gleich: indirekt proportional.', '2 · 12 = 24 Fahrten. 24 : 3 = 8.', 'Jeder Transporter muss 8-mal fahren.'),
    'Was bleibt gleich, wenn mehr Transporter fahren?'), huerde='ueberfluessig')

# --- produkt ---
TX.u('produkt', 'direkt', TZ('Ein Gewinn wird gleichmäßig geteilt. Bei 4 Personen bekommt jede 15 €. Wie groß ist der ganze Gewinn?', '4 * 15',
    TW('4 Personen je 15 €.', 'ganzer Gewinn (das Produkt).', 'Personen · Betrag = Gewinn.', '4 · 15 = 60.', 'Der Gewinn ist 60 €.'), 'Was ergibt Personen mal Betrag?', einheit='€'))
TX.u('produkt', 'einkleidung', TZ('In ein Fotobuch sollen 120 Fotos, auf jede Seite gleich viele. Mit 4 Fotos pro Seite braucht man 30 Seiten. Wie viele Seiten braucht man mit 6 Fotos pro Seite?', '120 / 6',
    TW('120 Fotos; 4 pro Seite ergibt 30 Seiten.', 'Seitenzahl bei 6 Fotos pro Seite.', 'Fotos pro Seite · Seiten = 120 bleibt gleich.', '120 : 6 = 20.', 'Man braucht 20 Seiten.'), 'Welches Produkt bleibt immer gleich?'))
TX.u('produkt', 'darstellung', TX.A('Eine Lehrerin teilt eine Klasse in gleich große Gruppen und notiert: 2 Gruppen mit je 15 Kindern, 3 Gruppen mit je 10, 5 Gruppen mit je 6, 6 Gruppen mit je 4 Kindern. Welche Notiz passt nicht zur selben Klasse?',
    '6 Gruppen mit je 4 Kindern', ['2 Gruppen mit je 15 Kindern', '3 Gruppen mit je 10 Kindern', '5 Gruppen mit je 6 Kindern'],
    TW('vier Notizen Gruppen · Kinder.', 'Notiz, die nicht passt.', 'Gleiche Klasse heißt gleiches Produkt.', '2 · 15 = 30, 3 · 10 = 30, 5 · 6 = 30, 6 · 4 = 24.', 'Die Notiz „6 Gruppen mit je 4“ passt nicht – das wären nur 24 Kinder.'),
    'Wie viele Kinder hat die Klasse nach jeder Notiz?'))
TX.u('produkt', 'mehrschritt', TZ('24 Personen teilen sich die Kosten für ein Geschenk, jede zahlt 2,50 €. Wie viel müsste jede zahlen, wenn nur 20 mitmachen?', '24 * 2.5 / 20',
    TW('24 Personen je 2,50 €.', 'Betrag pro Person bei 20 Personen.', 'Erst den Gesamtpreis, dann neu teilen.', '24 · 2,50 = 60 €. 60 : 20 = 3 €.', 'Jede müsste 3 € zahlen.'), 'Was kostet das Geschenk insgesamt?', einheit='€'))
TX.u('produkt', 'pruefung', TZ('Wer eine Radtour mit 20 km/h fährt, braucht 3 Stunden. Die Strecke führt durch 4 Dörfer und hat 350 Höhenmeter. Wie lange braucht man mit 15 km/h?', '20 * 3 / 15',
    TW('20 km/h → 3 h. Dörfer und Höhenmeter spielen keine Rolle.', 'Zeit bei 15 km/h.', 'Geschwindigkeit · Zeit = Strecke bleibt gleich.', '20 · 3 = 60 km. 60 : 15 = 4.', 'Man braucht 4 Stunden.'),
    'Welche Angaben gehören zu „Tempo mal Zeit“?', einheit='h'), huerde='ueberfluessig')
TX.u('produkt', 'begruenden', TX.A('Ein Bauer misst: 3 Rohre füllen sein Becken in 8 h, 4 Rohre in 6 h, 6 Rohre in 5 h. Er sagt: „Rohre → Zeit ist indirekt proportional.“ Was stimmt?',
    'Nein: 6 · 5 = 30, die anderen Produkte sind 24.', ['Ja: Mehr Rohre brauchen weniger Zeit.', 'Ja: Alle Produkte sind 24.', 'Nein: 3 · 8 = 11, also passt nichts.'],
    TW('(3 | 8), (4 | 6), (6 | 5).', 'Ist die Zuordnung indirekt proportional?', 'Alle Produkte vergleichen.', '3 · 8 = 24, 4 · 6 = 24, 6 · 5 = 30.', 'Nicht indirekt proportional: Ein Produkt weicht ab (mit 6 Rohren müssten es 4 h sein).'),
    '„Je mehr, desto weniger“ reicht nicht – prüfe die Produkte.'), huerde='entscheidung')
TX.s('produkt', TZ('Für eine Feier werden 96 Stühle in gleich lange Reihen gestellt. Bei 12 Reihen stehen 8 Stühle in jeder Reihe. Wie viele Stühle stehen in jeder Reihe, wenn es 16 Reihen sind?', '96 / 16',
    TW('96 Stühle, 12 Reihen zu je 8.', 'Stühle pro Reihe bei 16 Reihen.', 'Reihen · Stühle pro Reihe = 96.', '96 : 16 = 6.', 'Es stehen 6 Stühle in jeder Reihe.')))
TX.s('produkt', TZ('Ein Vorrat Hundefutter reicht für 2 Hunde 18 Tage. Wie viele Tage reicht er für 3 gleich große Hunde?', '2 * 18 / 3',
    TW('2 Hunde → 18 Tage.', 'Tage bei 3 Hunden.', 'Hunde · Tage bleibt gleich.', '2 · 18 = 36. 36 : 3 = 12.', 'Der Vorrat reicht 12 Tage.'), einheit='Tage'))
TX.k('produkt', TZ('Ein Kuchenblech wird gerecht geteilt. Bei 6 Personen bekommt jede 4 Stücke. Wie viele Stücke bekommt jede bei 8 Personen?', '6 * 4 / 8',
    TW('6 Personen je 4 Stücke.', 'Stücke pro Person bei 8 Personen.', 'Personen · Stücke = alle Stücke.', '6 · 4 = 24. 24 : 8 = 3.', 'Jede bekommt 3 Stücke.')))

# --- graph ---
TX.u('graph', 'direkt', TZ('Alle Rechtecke mit 48 cm² Flächeninhalt: Breite x → Länge y. Wie lang ist das Rechteck mit 8 cm Breite?', '48 / 8',
    TW('A = 48 cm², x = 8 cm.', 'Länge y.', 'x · y = 48, also y = 48 : x.', 'y = 48 : 8 = 6.', 'Das Rechteck ist 6 cm lang.'), 'Breite mal Länge ergibt immer was?', einheit='cm'))
TX.u('graph', 'einkleidung', TX.A('Für eine 60-km-Radtour gilt: Geschwindigkeit x (in km/h) → Fahrzeit y (in h). Liegt der Punkt (12 | 6) auf dem Graphen?',
    'Nein, bei 12 km/h braucht man 5 h.', ['Ja, 12 · 6 = 72 passt.', 'Ja, jeder Punkt mit x und y liegt darauf.', 'Nein, bei 12 km/h braucht man 6,5 h.'],
    TW('Strecke 60 km, Punkt (12 | 6).', 'Liegt der Punkt auf dem Graphen?', 'Auf dem Graphen gilt x · y = 60.', '12 · 6 = 72 ≠ 60; richtig wäre y = 60 : 12 = 5.', 'Der Punkt liegt nicht darauf: Bei 12 km/h dauert die Tour 5 h.'),
    'Was ergibt Tempo mal Zeit bei dieser Tour?'))
TX.u('graph', 'transfer', TZ('Ein Gärtner hat 240 Tulpenzwiebeln und pflanzt sie in Reihen mit gleich vielen Zwiebeln. In eine Reihe passen höchstens 25 Zwiebeln. Wie viele Reihen braucht er mindestens?', '-(-240 // 25)',
    TW('240 Zwiebeln, höchstens 25 pro Reihe.', 'Mindestzahl der Reihen.', 'Reihen · Zwiebeln pro Reihe = 240; Reihen = 240 : 25, dann aufrunden.', '240 : 25 = 9,6.', 'Er braucht mindestens 10 Reihen (dann 24 pro Reihe).'),
    'Wie viele Reihen ergibt die Rechnung, und geht eine „halbe“ Reihe?'), huerde='deuten')
TX.u('graph', 'pruefung', TZ('Für einen 36 km langen Radweg gehört zu jeder Durchschnittsgeschwindigkeit x (in km/h) eine Fahrzeit y (in h). Der Weg führt über 5 Brücken. Bei welcher Geschwindigkeit dauert die Fahrt genau 1,5 Stunden?', '36 / 1.5',
    TW('Strecke 36 km, y = 1,5 h; die Brücken spielen keine Rolle.', 'Geschwindigkeit x.', 'x · y = 36, also x = 36 : y.', 'x = 36 : 1,5 = 24.', 'Man muss 24 km/h fahren.'), 'Welches Produkt ist bei diesem Graphen immer gleich?', einheit='km/h'), huerde='ueberfluessig')
TX.u('graph', 'begruenden', TX.A('Für das Aufräumen der Turnhalle zeichnet jemand den Graphen „Anzahl der Helfer → Zeit“ und verlängert die Kurve bis zur y-Achse bei 0 Helfern. Was stimmt?',
    'Falsch: Bei 0 Helfern gibt es keinen Wert – die Hyperbel trifft die Achse nie.', ['Richtig: Bei 0 Helfern ist die Zeit 0.', 'Richtig: Der Graph ist eine Gerade durch den Ursprung.', 'Falsch: Bei 0 Helfern ist die Zeit 1 h.'],
    TW('Zuordnung Helfer → Zeit, indirekt proportional.', 'Darf die Kurve die y-Achse treffen?', 'Bei y = k : x ist x = 0 nicht erlaubt.', 'k : 0 gibt es nicht; je weniger Helfer, desto länger dauert es.', 'Die Verlängerung ist falsch: Ohne Helfer wird die Halle nie fertig.'),
    'Was müsste man bei 0 Helfern rechnen?'), huerde='entscheidung')
TX.s('graph', TZ('Alle Rechtecke mit 30 m² Flächeninhalt: Breite → Länge. Wie breit ist das Rechteck mit 7,5 m Länge?', '30 / 7.5',
    TW('A = 30 m², Länge 7,5 m.', 'Breite.', 'Breite · Länge = 30.', '30 : 7,5 = 4.', 'Es ist 4 m breit.'), einheit='m'))
TX.s('graph', TZ('Für einen 18 km langen Wanderweg gehört zu jeder Geschwindigkeit eine Gehzeit. Wie lange braucht man mit 4,5 km/h?', '18 / 4.5',
    TW('Strecke 18 km, 4,5 km/h.', 'Gehzeit.', 'Tempo · Zeit = 18.', '18 : 4,5 = 4.', 'Man braucht 4 Stunden.'), einheit='h'))
TX.k('graph', TZ('Ein Sparziel von 240 € soll mit gleich hohen Monatsraten erreicht werden. Wie hoch ist eine Rate, wenn man 16 Monate spart?', '240 / 16',
    TW('Sparziel 240 €, 16 Monate.', 'Monatsrate.', 'Rate · Monate = 240.', '240 : 16 = 15.', 'Eine Rate ist 15 €.'), einheit='€'))

# --- unterscheiden ---
_ART = ['direkt proportional', 'indirekt proportional', 'keins von beiden']
TX.u('unterscheiden', 'erkennen', TX.A('Im Kino kostet jede Karte 9 €. Welche Zuordnung ist „Anzahl der Karten → Preis“?', 'direkt proportional', _ART[1:],
    TW('9 € pro Karte, keine Grundgebühr.', 'Art der Zuordnung.', 'Doppelt so viele Karten → doppelter Preis? 0 Karten → 0 €?', '2 Karten 18 €, 4 Karten 36 €; 0 Karten 0 €.', 'Die Zuordnung ist direkt proportional.'),
    'Was kosten doppelt so viele Karten?'))
TX.u('unterscheiden', 'einkleidung', TX.A('Ein Handwerker nimmt 30 € Anfahrt und 40 € je Arbeitsstunde. Welche Zuordnung ist „Arbeitsstunden → Preis“?', 'keins von beiden', _ART[:2],
    TW('30 € einmalig, 40 € pro Stunde.', 'Art der Zuordnung.', 'Doppelte Zeit → doppelter Preis?', '1 h: 70 €, 2 h: 110 € – nicht das Doppelte, und das Produkt ist auch nicht gleich.', 'Keins von beiden – die Anfahrt stört.'),
    'Kosten 2 Stunden doppelt so viel wie 1 Stunde?'))
TX.u('unterscheiden', 'darstellung', TX.A('Für eine Wanderung gilt: mit 3 km/h dauert sie 8 h, mit 4 km/h 6 h, mit 6 km/h 4 h. Welche Zuordnung ist „Tempo → Zeit“?', 'indirekt proportional', [_ART[0], _ART[2]],
    TW('(3 | 8), (4 | 6), (6 | 4).', 'Art der Zuordnung.', 'Quotienten und Produkte vergleichen.', 'Produkte: 24, 24, 24 – immer gleich.', 'Die Zuordnung ist indirekt proportional (24 km Strecke).'),
    'Rechne Tempo mal Zeit für jedes Paar.'))
TX.u('unterscheiden', 'mehrschritt', TZ('500 Blatt Kopierpapier kosten 4 €. Der Preis ist proportional zur Zahl der Blätter. Was kosten 2 750 Blatt?', '4 / 500 * 2750',
    TW('500 Blatt für 4 €, direkt proportional.', 'Preis für 2 750 Blatt.', 'Über 1 Blatt oder über 250 Blatt rechnen.', '250 Blatt kosten 2 €. 2 750 = 11 · 250, also 11 · 2 € = 22 €.', '2 750 Blatt kosten 22 €.'), 'Was kosten 250 Blatt?', einheit='€'))
TX.u('unterscheiden', 'pruefung', TZ('Eine Klasse mietet für einen Ausflug einen Bus für 600 €, dazu kostet der Eintritt 8 € pro Kind. Die Busmiete wird gleich verteilt. Wie viel zahlt jedes Kind, wenn 24 Kinder mitfahren?', '600 / 24 + 8',
    TW('Bus 600 € (geteilt), Eintritt 8 € pro Kind, 24 Kinder.', 'Betrag pro Kind.', 'Busanteil ist indirekt proportional, der Eintritt bleibt fest.', '600 : 24 = 25 €. 25 + 8 = 33 €.', 'Jedes Kind zahlt 33 €.'),
    'Welcher Teil hängt von der Kinderzahl ab, welcher nicht?', einheit='€'), huerde='zwei')
TX.u('unterscheiden', 'begruenden', TX.A('Jemand sagt: „Bei einem Handytarif mit 5 € Grundgebühr und 9 Cent pro Minute ist der Preis direkt proportional zur Gesprächszeit, denn je länger, desto teurer.“ Was stimmt?',
    'Falsch: Bei 0 Minuten kostet es schon 5 €, doppelte Zeit heißt nicht doppelter Preis.', ['Richtig: Je länger, desto teurer reicht.', 'Falsch: Es ist indirekt proportional.', 'Richtig, weil 9 Cent immer gleich bleiben.'],
    TW('5 € Grundgebühr, 0,09 € pro Minute.', 'Ist die Begründung richtig?', 'Direkt proportional verlangt: 0 → 0 und doppelt → doppelt.', '0 min: 5 €. 100 min: 14 €, 200 min: 23 € – nicht das Doppelte.', 'Die Aussage ist falsch: keins von beiden.'),
    'Was kostet es bei 0 Minuten?'), huerde='entscheidung')
TX.s('unterscheiden', TX.A('Ein Liter Benzin kostet 1,80 €. Welche Zuordnung ist „getankte Liter → Preis“?', 'direkt proportional', _ART[1:],
    TW('1,80 € pro Liter.', 'Art der Zuordnung.', 'Doppelte Menge → doppelter Preis, 0 l → 0 €.', '10 l: 18 €, 20 l: 36 €.', 'Direkt proportional.')))
TX.s('unterscheiden', TX.A('Eine Gruppe teilt sich die Miete einer Hütte gleichmäßig. Welche Zuordnung ist „Anzahl der Personen → Betrag pro Person“?', 'indirekt proportional', [_ART[0], _ART[2]],
    TW('feste Miete, gleich geteilt.', 'Art der Zuordnung.', 'Doppelt so viele Personen → halber Betrag?', 'Personen · Betrag = Miete bleibt gleich.', 'Indirekt proportional.')))
TX.k('unterscheiden', TX.A('Eine Jahreskarte fürs Schwimmbad kostet 50 €, dazu zahlt man 1 € pro Besuch. Welche Zuordnung ist „Besuche → Gesamtkosten“?', 'keins von beiden', _ART[:2],
    TW('50 € fest, 1 € pro Besuch.', 'Art der Zuordnung.', 'Doppelt so viele Besuche → doppelte Kosten?', '10 Besuche: 60 €, 20 Besuche: 70 €.', 'Keins von beiden.')))
baue = mit_text(baue, TX)
# ---- TEXT ENDE ----

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


# ---- BEREINIGEN (Einundzwanzigste Runde) ----
if __name__ == '__main__':
    from _bereinigen import bereinigen_datei
    bereinigen_datei('groessen.indirekt')
# ---- BEREINIGEN ENDE ----
