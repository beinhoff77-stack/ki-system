#!/usr/bin/env python3
"""Thema daten.stichproben – Stichproben und Aussagekraft (Realschule Bayern, Klasse 7)."""
import sys
from math import gcd
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _rs import *  # noqa: E402,F403

start(8101)

# Grundgesamtheit, Einheit (Plural), Merkmal (Frage), gute Auswahl, schlechte Auswahlen (Auswahl, Grund)
SZEN = [
    ('alle Schülerinnen und Schüler einer Realschule', 'Schulkinder', 'wie die Kinder zur Schule kommen',
     'aus jeder Klasse per Los einige Kinder',
     [('nur die Kinder, die morgens am Fahrradständer stehen', 'Radfahrer sind zu stark vertreten'),
      ('nur die Kinder der 5. Klassen', 'nur eine Jahrgangsstufe wird befragt'),
      ('nur die Kinder, die mit dem Schulbus kommen', 'Busfahrer sind zu stark vertreten')]),
    ('alle Einwohnerinnen und Einwohner einer Stadt', 'Personen', 'ob die Einwohner ein neues Hallenbad wollen',
     'zufällig ausgewählte Personen aus dem Einwohnerverzeichnis',
     [('nur die Besucher des alten Hallenbads', 'Schwimmer sind eher dafür'),
      ('nur die Bewohner eines Seniorenheims', 'nur eine Altersgruppe wird befragt'),
      ('nur Mitglieder des Schwimmvereins', 'Schwimmer sind eher dafür')]),
    ('alle Jugendlichen in Bayern', 'Jugendliche', 'wie viele Stunden Jugendliche pro Woche Sport treiben',
     'zufällig ausgewählte Jugendliche aus vielen Schulen in ganz Bayern',
     [('nur Mitglieder eines Fußballvereins', 'Sportler sind zu stark vertreten'),
      ('nur Besucher eines Computerspiel-Turniers', 'eine einseitige Gruppe wird befragt'),
      ('nur Jugendliche aus einer einzigen Stadt', 'nur ein Ort wird befragt')]),
    ('alle Kundinnen und Kunden eines Supermarkts', 'Kunden', 'wie zufrieden die Kunden mit den Öffnungszeiten sind',
     'an verschiedenen Tagen zu verschiedenen Uhrzeiten zufällig angesprochene Kunden',
     [('nur Kunden am Samstagvormittag', 'nur eine Tageszeit wird erfasst'),
      ('nur Kunden, die sich schon einmal beschwert haben', 'Unzufriedene sind zu stark vertreten'),
      ('nur die Angestellten des Supermarkts', 'sie gehören nicht zur Grundgesamtheit')]),
    ('alle Fahrgäste einer Buslinie', 'Fahrgäste', 'ob die Fahrgäste mit der Pünktlichkeit zufrieden sind',
     'an mehreren Tagen in verschiedenen Bussen zufällig ausgewählte Fahrgäste',
     [('nur Fahrgäste, die gerade auf einen verspäteten Bus warten', 'Verärgerte sind zu stark vertreten'),
      ('nur die Busfahrer', 'sie gehören nicht zur Grundgesamtheit'),
      ('nur Fahrgäste am Sonntagmorgen', 'nur eine ruhige Tageszeit wird erfasst')]),
    ('alle Haushalte einer Gemeinde', 'Haushalte', 'wie viele Haushalte ein Haustier haben',
     'jeden zehnten Haushalt aus der Adressliste',
     [('nur Kunden einer Zoohandlung', 'Tierbesitzer sind zu stark vertreten'),
      ('nur Haushalte in einem einzigen Hochhaus', 'nur eine Wohnform wird erfasst'),
      ('nur Haushalte, die beim Tierarzt im Wartezimmer sitzen', 'Tierbesitzer sind zu stark vertreten')]),
    ('alle Besucherinnen und Besucher eines Freizeitparks', 'Besucher', 'wie den Besuchern die neue Achterbahn gefällt',
     'am Ausgang zufällig angesprochene Besucher',
     [('nur Besucher, die gerade aus der Achterbahn steigen und noch einmal anstehen', 'Fans der Bahn sind zu stark vertreten'),
      ('nur Kinder unter 8 Jahren', 'nur eine Altersgruppe wird befragt'),
      ('nur die Mitarbeiter des Parks', 'sie gehören nicht zur Grundgesamtheit')]),
    ('alle Wahlberechtigten einer Stadt', 'Wahlberechtigte', 'wen die Wahlberechtigten zum Bürgermeister wählen wollen',
     'zufällig aus dem Wählerverzeichnis ausgewählte Personen',
     [('nur Mitglieder einer Partei', 'Anhänger einer Partei sind zu stark vertreten'),
      ('nur Leser eines Online-Forums, die freiwillig abstimmen', 'nur besonders Interessierte antworten'),
      ('nur Schülerinnen und Schüler einer 7. Klasse', 'sie sind gar nicht wahlberechtigt')]),
    ('alle Mitglieder eines Sportvereins', 'Mitglieder', 'ob die Mitglieder ein neues Vereinsheim wollen',
     'per Los aus der Mitgliederliste gezogene Mitglieder',
     [('nur die Mitglieder des Vorstands', 'nur eine kleine, besondere Gruppe wird befragt'),
      ('nur Zuschauer bei einem Heimspiel', 'viele Zuschauer sind keine Mitglieder'),
      ('nur die Mitglieder der Tennisabteilung', 'nur eine Abteilung wird befragt')]),
    ('alle Beschäftigten einer Firma', 'Beschäftigte', 'wie zufrieden die Beschäftigten mit der Kantine sind',
     'per Los aus allen Abteilungen ausgewählte Beschäftigte',
     [('nur Beschäftigte, die gerade in der Kantine essen', 'wer die Kantine meidet, fehlt'),
      ('nur die Köche der Kantine', 'sie bewerten ihr eigenes Essen'),
      ('nur die Beschäftigten einer einzigen Abteilung', 'nur eine Abteilung wird befragt')]),
]

FEHLER_ART = ['Die Stichprobe ist zu klein.', 'Die Auswahl ist einseitig.', 'Die Frage ist suggestiv (lenkt die Antwort).',
              'Nur Freiwillige antworten.']

SUGGESTIV = ['Sie sind doch sicher auch dafür, dass {x}?', 'Finden Sie nicht auch, dass es gut wäre, wenn {x}?', 'Jeder vernünftige Mensch ist dafür, dass {x}. Sie auch?']
SUG_X = ['die Pause länger wird', 'der Spielplatz erneuert wird', 'mehr Radwege gebaut werden', 'das Schwimmbad länger öffnet',
         'es in der Mensa mehr Gemüse gibt', 'der Bus öfter fährt']
FREI = ['Eine Zeitschrift will wissen, was ihre Leser zum Thema „{x}“ denken, und ruft sie auf, im Internet abzustimmen.',
        'Ein Radiosender will wissen, was seine Hörer zum Thema „{x}“ denken, und bittet sie anzurufen.',
        'Eine Schule will wissen, was ihre Kinder zum Thema „{x}“ denken. An der Schultür hängt ein Zettel: Wer möchte, wirft seine Meinung in den Briefkasten.']
FREI_SCHULE = {800: 80, 1200: 120, 3500: 350, 9000: 450}  # Prüfung neu 1: 9 000 Antworten an einer Schule sind unrealistisch
FREI_X = ['Neues Jugendzentrum', 'Handyverbot an Schulen', 'Längere Ladenöffnungszeiten', 'Autofreier Sonntag', 'Mehr Hausaufgaben']


def schwach(e):
    """Pluralform nach bestimmtem Artikel/Dativ: Jugendliche -> Jugendlichen."""
    return e + 'n' if e in ('Jugendliche', 'Wahlberechtigte', 'Beschäftigte') else e

ETAPPEN = [
    {'lernziel': 'begriffe', 'titel': 'Grundgesamtheit und Stichprobe',
     'regel': 'Die ⟦Grundgesamtheit⟧ sind alle, über die du etwas wissen willst. Befragst du alle, ist das eine ⟦Vollerhebung⟧. Meist befragt man nur einen Teil: die ⟦Stichprobe⟧. Ihre Größe heißt ⟦Stichprobenumfang⟧ n. Wie beim Kochen: Du probierst einen Löffel (Stichprobe), um den ganzen Topf (Grundgesamtheit) zu beurteilen.',
     'schritte': ['Eine Realschule hat 620 Kinder. 50 davon werden gefragt, wie sie zur Schule kommen.',
                  'Grundgesamtheit: ⟦alle 620 Kinder der Schule⟧. Stichprobe: die 50 Befragten, also ⟦n = 50⟧.'],
     'fehler': 'Die 50 Befragten als Grundgesamtheit zu bezeichnen ist falsch: Die Grundgesamtheit ist ⟦die ganze Gruppe⟧, über die man eine Aussage machen will – hier alle 620 Kinder.'},
    {'lernziel': 'hochrechnen', 'titel': 'Von der Stichprobe hochrechnen',
     'regel': 'Ist die Stichprobe gut gewählt, überträgt man ihre ⟦relative Häufigkeit⟧ auf die Grundgesamtheit: ⟦Anteil = Anzahl in der Stichprobe : n⟧, dann ⟦geschätzte Anzahl = Anteil · Größe der Grundgesamtheit⟧. Das Ergebnis ist eine ⟦Schätzung⟧, kein genauer Wert.',
     'schritte': ['Von 80 befragten Kindern einer Schule mit 640 Kindern kommen 28 mit dem Rad. Anteil: 28 : 80 = 0,35 = 35 %.',
                  'Hochrechnung: 0,35 · 640 = ⟦224⟧. Etwa 224 Kinder der Schule kommen mit dem Rad.'],
     'probe': '224 : 640 = 0,35 ✓',
     'fehler': '28 · 640 = 17 920 Kinder ist falsch: Erst den ⟦Anteil⟧ bilden (28 : 80), dann mit der Grundgesamtheit multiplizieren.'},
    {'lernziel': 'repraesentativ', 'titel': 'Ist die Stichprobe geeignet?',
     'regel': 'Eine Stichprobe ist ⟦repräsentativ⟧, wenn sie die Grundgesamtheit im Kleinen gut abbildet. Dafür sollte sie ⟦zufällig⟧ ausgewählt werden und ⟦groß genug⟧ sein. Befragt man nur eine besondere Gruppe, wird das Ergebnis ⟦verzerrt⟧.',
     'schritte': ['Frage: Wie viele Jugendliche in Bayern treiben Sport? Befragt werden nur Mitglieder eines Fußballvereins.',
                  'Nicht geeignet: ⟦Sportler sind zu stark vertreten⟧. Besser: zufällig ausgewählte Jugendliche aus vielen Schulen.'],
     'fehler': '„Wir haben 500 Leute befragt, also ist es repräsentativ“ ist falsch: Auch eine große Stichprobe ist ⟦verzerrt⟧, wenn sie nur aus einer besonderen Gruppe stammt.'},
    {'lernziel': 'fehlerquellen', 'titel': 'Wie entstehen verzerrte Ergebnisse?',
     'regel': 'Typische Fehlerquellen: die Stichprobe ist ⟦zu klein⟧, die Auswahl ist ⟦einseitig⟧, die Frage ist ⟦suggestiv⟧ (sie drängt zu einer Antwort), oder ⟦nur Freiwillige⟧ antworten – meist die mit einer starken Meinung.',
     'schritte': ['Ein Verein fragt: „Sie sind doch sicher auch dafür, dass der Spielplatz erneuert wird?“',
                  'Fehlerquelle: ⟦suggestive Frage⟧. Neutral wäre: „Soll der Spielplatz erneuert werden?“'],
     'fehler': 'Eine Online-Abstimmung mit 10 000 Stimmen für repräsentativ halten ist falsch: Wer ⟦freiwillig⟧ mitmacht, hat meist eine starke Meinung – die anderen fehlen.'},
    {'lernziel': 'aussagen', 'titel': 'Aussagen kritisch prüfen',
     'regel': 'Ergebnisse von Stichproben ⟦schwanken⟧: Zwei Stichproben aus derselben Grundgesamtheit liefern meist etwas verschiedene Anteile. Je ⟦größer⟧ die Stichprobe, desto weniger schwankt sie. Aus einer Stichprobe folgt deshalb nur „⟦ungefähr⟧“, nie „genau“.',
     'schritte': ['Stichprobe A: 7 von 10 Befragten (70 %) mögen das Mensaessen. Stichprobe B: 260 von 500 (52 %).',
                  'B ist ⟦aussagekräftiger⟧, weil sie viel größer ist. Der Unterschied beträgt 70 % − 52 % = ⟦18 Prozentpunkte⟧.'],
     'fehler': '„In der Stichprobe waren es 40 %, also sind es in der Grundgesamtheit genau 40 %“ ist falsch: Die Stichprobe liefert nur einen ⟦Schätzwert⟧.'},
]


# ---------- Generatoren ----------
def schule():
    return R.choice(['Realschule', 'Grundschule', 'Mittelschule', 'Musikschule'])


def g_begriffe(s):
    gg, einh, merk, gut, schl = R.choice(SZEN)
    N = R.choice([240, 360, 480, 620, 750, 840, 1200, 1500, 2400])
    n = R.choice([20, 25, 30, 40, 50, 60, 80, 100, 120])
    if s == 1:
        if R.random() < 0.5:
            return zahl(f'Von {dz(N)} Personen einer Gruppe werden {n} befragt. Wie groß ist der Stichprobenumfang n?',
                        f'Der Stichprobenumfang ist die Anzahl der Befragten: n = {n}.', 'Wie viele werden tatsächlich gefragt?', n, str(n))
        return auswahl(f'Man will wissen, {merk}. Man befragt {gut}. Was ist die Grundgesamtheit?', gg[0].upper() + gg[1:],
                       [f'Nur die befragten {schwach(einh)}', f'{gut[0].upper() + gut[1:]}', 'Alle Menschen in Deutschland'],
                       f'Die Grundgesamtheit sind {gg} – über sie will man etwas wissen. Die Befragten sind die Stichprobe.',
                       'Über wen soll die Umfrage etwas aussagen?')
    if s == 2:
        art = R.random()
        if art < 0.35:
            return auswahl(f'Alle {dz(N)} Kinder einer {schule()} werden befragt. Wie nennt man das?', 'Vollerhebung',
                           ['Stichprobe', 'Zufallsstichprobe', 'Hochrechnung'],
                           'Werden alle aus der Grundgesamtheit befragt, ist das eine Vollerhebung.', 'Wird jemand ausgelassen?')
        if art < 0.7:
            p = R.choice([5, 10, 20, 25])
            nn = N * p // 100
            return zahl(f'Aus {dz(N)} Personen werden {p} % zufällig ausgewählt. Wie groß ist der Stichprobenumfang?',
                        f'{p} % von {dz(N)}: {dz(N)} · {p} : 100 = {dz(nn)}.', 'Prozentwert berechnen: Grundwert mal Prozentsatz.',
                        nn, f'{N} * {p} / 100')
        return auswahl(f'Man will wissen, {merk}, und befragt {gut}. Was ist hier die Stichprobe?', f'Die ausgewählten {schwach(einh)}',
                       [gg[0].upper() + gg[1:], 'Die Frage, die gestellt wird', 'Das Ergebnis der Umfrage'],
                       f'Die Stichprobe sind die ausgewählten {schwach(einh)}, die wirklich befragt werden.', 'Wer wird tatsächlich gefragt?')
    art = R.random()
    if art < 0.4:
        k, pro = R.randint(4, 12), R.randint(3, 8)
        return zahl(f'In einer Schule gibt es {k} Klassen. Aus jeder Klasse werden per Los gleich viele Kinder gezogen, insgesamt {k * pro}. Wie viele sind es pro Klasse?',
                    f'{k * pro} : {k} = {pro} Kinder pro Klasse. So ist jede Klasse gleich stark vertreten.', 'Teile den Stichprobenumfang auf die Klassen auf.',
                    pro, f'{k * pro} / {k}')
    if art < 0.7:
        return auswahl('Warum macht man meist eine Stichprobe statt einer Vollerhebung?',
                       'Eine Vollerhebung wäre zu teuer oder dauert zu lange.',
                       ['Eine Stichprobe ist immer genauer als eine Vollerhebung.', 'Bei einer Vollerhebung darf man nicht rechnen.',
                        'Eine Stichprobe braucht keine Grundgesamtheit.'],
                       'Alle zu befragen kostet viel Zeit und Geld. Eine gute Stichprobe liefert eine brauchbare Schätzung. Genauer als eine Vollerhebung ist sie nicht.',
                       'Stell dir vor, man müsste alle Menschen in Bayern befragen.')
    a, gr = R.choice(schl)
    return auswahl(f'Man will wissen, {merk}, und befragt {a}. Welcher Satz beschreibt das richtig?',
                   f'Das ist eine Stichprobe, aber keine geeignete: {gr}.',
                   ['Das ist eine Vollerhebung.', f'Das ist eine geeignete Stichprobe, weil alle Befragten {einh} sind.' if 'gehören nicht' not in gr else 'Das ist eine geeignete Stichprobe, weil viele Personen befragt werden.',
                    'Das ist die Grundgesamtheit.'],
                   f'Es wird nur ein Teil befragt (Stichprobe). Die Auswahl ist aber verzerrt: {gr}.', 'Wird ein Teil oder werden alle befragt? Und wie wurde ausgewählt?')


def anteil_daten():
    """n, k, N so, dass Anteil endlich (Prozent) und Hochrechnung ganzzahlig."""
    n = R.choice([20, 25, 40, 50, 80, 100, 125, 200, 250])
    k = R.randint(max(2, n // 10), n * 9 // 10)
    p = Fr(k, n)
    q = p.denominator
    N = q * R.randint(max(2, 200 // q), max(3, 3000 // q))
    if N <= n: return None
    return n, k, N, p


KONTEXTE = [('Kindern einer Schule mit {N} Kindern', 'kommen {k} mit dem Rad', 'mit dem Rad kommen', 'Kinder', 'Kindern'),
            ('Haushalten einer Gemeinde mit {N} Haushalten', 'haben {k} einen Hund', 'einen Hund haben', 'Haushalte', 'Haushalten'),
            ('Jugendlichen eines Landkreises mit {N} Jugendlichen', 'spielen {k} ein Instrument', 'ein Instrument spielen', 'Jugendliche', 'Jugendlichen'),
            ('Besuchern eines Festivals mit {N} Besuchern', 'reisen {k} mit dem Zug an', 'mit dem Zug anreisen', 'Besucher', 'Besuchern'),
            ('Beschäftigten einer Firma mit {N} Beschäftigten', 'essen {k} regelmäßig in der Kantine', 'regelmäßig in der Kantine essen', 'Beschäftigte', 'Beschäftigten'),
            ('Fahrgästen einer Bahnlinie mit {N} Fahrgästen pro Tag', 'haben {k} eine Monatskarte', 'eine Monatskarte haben', 'Fahrgäste', 'Fahrgästen')]


def g_hochrechnen(s):
    d = anteil_daten()
    if d is None: return None
    n, k, N, p = d
    kt, mt, frage, ein, ein_d = R.choice(KONTEXTE)
    satz = f'Von {n} befragten {kt.format(N=dz(N))} {mt.format(k=k)}.'
    proz = p * 100
    if s == 1:
        if not endlich(proz): return None
        return zahl(satz + ' Wie viel Prozent sind das in der Stichprobe?', f'{k} : {n} = {dz(p)} = {dz(proz)} %.',
                    'Anteil = Anzahl : Stichprobenumfang. Dann in Prozent umrechnen.', proz, f'{k} / {n} * 100', einheit='%')
    est = p * N
    w = f'Anteil: {k} : {n} = {dz(p)}. Hochrechnung: {dz(p)} · {dz(N)} = {dz(est)}.'
    if s == 2:
        return zahl(satz + f' Schätze, wie viele {ein} insgesamt {frage}.', w,
                    'Erst den Anteil in der Stichprobe, dann mal die Größe der Grundgesamtheit.', est, f'{k} / {n} * {N}')
    art = R.random()
    if art < 0.35:
        return auswahl(satz + f' Wie viele {ein} sind es vermutlich insgesamt, die {frage}?', dz(est),
                       [dz(k * N), dz(Fr(N, k)) if endlich(Fr(N, k)) else dz(N - k), dz(N - n + k)],
                       w + ' Das ist eine Schätzung.', 'Anteil bilden, nicht die Anzahl selbst hochrechnen.')
    if art < 0.7:
        # Umkehr: wie viele in der Stichprobe, wenn geschätzt est in N
        return zahl(f'In einer Grundgesamtheit von {dz(N)} {ein_d} schätzt man {dz(est)}, die {frage}. Die Schätzung beruht auf einer Stichprobe mit n = {n}. Wie viele waren es in der Stichprobe?',
                    f'Anteil: {dz(est)} : {dz(N)} = {dz(p)}. In der Stichprobe: {dz(p)} · {n} = {k}.',
                    'Gleicher Anteil in Stichprobe und Grundgesamtheit.', k, f'{cz(est)} / {N} * {n}')
    # Vergleich zweier Gruppen (Prozentpunkte)
    n2 = R.choice([20, 25, 40, 50, 100])
    k2 = R.randint(n2 // 10 + 1, n2 * 9 // 10)
    p2 = Fr(k2, n2) * 100
    if not endlich(proz) or not endlich(p2) or proz == p2: return None
    diff = abs(proz - p2)
    return zahl(f'Gefragt wird, wer {frage.replace("haben", "hat").replace("kommen", "kommt").replace("spielen", "spielt").replace("anreisen", "anreist").replace("essen", "isst")}. Stichprobe 1: {k} von {n} Befragten sagen ja. Stichprobe 2: {k2} von {n2}. Um wie viele Prozentpunkte unterscheiden sich die Anteile?',
                f'{k} : {n} = {dz(proz)} %, {k2} : {n2} = {dz(p2)} %. Unterschied: {dz(diff)} Prozentpunkte.',
                'Beide Anteile in Prozent umrechnen, dann die Differenz bilden.', diff, f'abs({k} / {n} * 100 - {k2} / {n2} * 100)')


def g_repraesentativ(s):
    gg, einh, merk, gut, schl = R.choice(SZEN)
    a, gr = R.choice(schl)
    n = R.choice([40, 60, 80, 100, 150, 200, 300, 500])
    if s == 1:
        if R.random() < 0.5:
            return auswahl(f'Man will wissen, {merk}. Grundgesamtheit: {gg}. Befragt werden {n} {einh}: {gut}. Ist die Stichprobe geeignet?',
                           'Ja, die Auswahl ist zufällig und deckt alle Gruppen ab.',
                           [f'Nein, {n} sind immer zu wenige.', 'Nein, man darf nur eine Vollerhebung machen.', 'Nein, weil nicht alle dieselbe Antwort geben.'],
                           'Die Auswahl ist zufällig und nicht auf eine besondere Gruppe beschränkt – sie ist geeignet.', 'Ist die Auswahl zufällig?')
        return auswahl(f'Man will wissen, {merk}. Grundgesamtheit: {gg}. Befragt werden {n} Personen: {a}. Ist die Stichprobe geeignet?',
                       f'Nein: {gr}.', ['Ja, weil viele Personen befragt werden.', 'Ja, jede Stichprobe ist geeignet.', 'Ja, weil die Befragten Bescheid wissen.'],
                       f'Die Auswahl ist einseitig: {gr}. Das Ergebnis wird verzerrt.', 'Wer wird befragt – und fehlt dabei jemand?')
    if s == 2:
        gute = gut[0].upper() + gut[1:]
        fal = [x[0][0].upper() + x[0][1:] for x in schl]
        if R.random() < 0.5:
            andere = [g for x in SZEN if x[0] != gg for _, g in x[4] if g != gr and 'gehören nicht' not in g]
            R.sample(andere, 3)  # Zufallsfolge wie bisher halten (Prüfung neu 1)
            # Prüfung neu 1: allgemeine Gründe („eine einseitige Gruppe …“, „nur eine Altersgruppe …“) passen auf jede
            # schlechte Auswahl und waren so eine zweite richtige Antwort. Jetzt: zwei echte Denkfehler + ein fremder Grund.
            fremd = sorted(g for g in andere if 'zu stark vertreten' in g and g.split()[0] not in gr)
            falsch = [f'{n} Personen sind zu viele.', 'Man darf nie nur einen Teil befragen, nur alle.',
                      fremd[(n + len(gr)) % len(fremd)]]
            return auswahl(f'Um herauszufinden, {merk}, werden {n} Personen befragt: {a}. Warum ist das keine geeignete Stichprobe?',
                           gr[0].upper() + gr[1:] + '.', [x[0].upper() + x[1:] + ('' if x.endswith('.') else '.') for x in falsch],
                           f'Grundgesamtheit sind {gg}. Bei dieser Auswahl gilt: {gr}.', 'Wer ist in dieser Gruppe besonders häufig – oder wer fehlt?')
        return auswahl(f'Man will wissen, {merk} (Grundgesamtheit: {gg}). Jeweils {n} Personen sollen befragt werden. Welche Auswahl ist am besten geeignet?', gute, fal,
                       f'Am besten: {gut}. Die anderen sind einseitig: ' + '; '.join(x[1] for x in schl) + '.',
                       'Welche Auswahl ist zufällig und betrifft alle Gruppen?')
    art = R.random()
    if art < 0.5:
        n_gross = R.choice([800, 1000, 1500, 2000])
        n_kl = R.choice([60, 80, 100, 120])
        return auswahl(f'Man will wissen, {merk}. Stichprobe A: {dz(n_gross)} {einh}, aber {a}. Stichprobe B: {n_kl} {einh}, {gut}. Welche ist aussagekräftiger?',
                       'B, weil sie zufällig ausgewählt ist.', ['A, weil sie größer ist.', 'Beide sind gleich gut.', 'Keine von beiden, man braucht eine Vollerhebung.'],
                       f'A ist zwar groß, aber verzerrt ({gr}). B ist kleiner, bildet die Grundgesamtheit aber besser ab.',
                       'Größe allein reicht nicht – wie wurde ausgewählt?')
    return auswahl(f'Jemand befragt {n} Personen, und zwar {a}, um herauszufinden, {merk}. Was ist das Hauptproblem?',
                   gr[0].upper() + gr[1:] + '.',
                   [f'{n} Personen sind zu viele.', 'Man hätte die Frage schriftlich stellen müssen.', 'Das Ergebnis lässt sich nicht in Prozent angeben.'],
                   f'Die Stichprobe ist einseitig: {gr}.', 'Passt die befragte Gruppe zur Grundgesamtheit?')


def g_fehlerquellen(s):
    art = R.randrange(4)
    if s == 1:
        art = R.choice([0, 2])
    if art == 0:
        n = R.randint(3, 8)
        gg, einh, merk, gut, schl = R.choice(SZEN)
        txt = f'Um herauszufinden, {merk}, werden {n} zufällig ausgewählte {einh} befragt.'
        richtig = FEHLER_ART[0]
        w = f'Die Auswahl ist zwar zufällig, aber {n} Befragte sind viel zu wenige – das Ergebnis schwankt stark.'
    elif art == 1:
        gg, einh, merk, gut, schl = R.choice(SZEN)
        a, gr = R.choice(schl)
        if 'gehören nicht' in gr or 'nicht wahlberechtigt' in gr or 'keine Mitglieder' in gr: return None
        n = R.choice([150, 200, 300, 400])
        txt = f'Um herauszufinden, {merk}, werden {n} Personen befragt: {a}.'
        richtig = FEHLER_ART[1]
        w = f'Die Auswahl ist einseitig: {gr}.'
    elif art == 2:
        x = R.choice(SUG_X)
        f = R.choice(SUGGESTIV).format(x=x)
        n = R.choice([100, 200, 250, 400])
        txt = f'Bei einer Umfrage unter {n} zufällig ausgewählten Personen lautet die Frage: „{f}“'
        richtig = FEHLER_ART[2]
        w = f'Die Frage drängt zu einem „Ja“. Neutral wäre: „Soll {x.replace("wird", "werden") if False else x}?“ als offene Ja-/Nein-Frage ohne Wertung.'
        w = 'Die Frage drängt zu einem „Ja“ (suggestiv). Neutral wäre eine Frage ohne Wertung, z. B. „Sind Sie dafür oder dagegen?“'
    else:
        x = R.choice(FREI_X)
        vorl = R.choice(FREI)
        anz = R.choice([800, 1200, 3500, 9000])
        if vorl.startswith('Eine Schule'): anz = FREI_SCHULE[anz]
        txt = vorl.format(x=x) + f' Es kommen {dz(anz)} Antworten.'
        richtig = FEHLER_ART[3]
        w = 'Es antworten nur Freiwillige – meist Menschen mit einer starken Meinung. Die vielen Antworten ändern daran nichts.'
    if s == 3 and R.random() < 0.5:
        # Verbesserung vorschlagen
        bess = {0: 'Mehr Personen zufällig auswählen.', 1: 'Statt einer besonderen Gruppe Personen aus allen Gruppen zufällig auswählen.',
                2: 'Die Frage neutral stellen, ohne Wertung.', 3: 'Nicht auf Meldungen warten, sondern Personen per Los auswählen und gezielt ansprechen.'}
        if art in (1, 3):  # Prüfung neu 1: „mehr zufällig auswählen“ wäre hier auch vertretbar – echter Denkfehler ist „einfach mehr“
            bess[0] = 'Einfach mehr Personen auf dieselbe Art befragen.'
        aus = {0: (), 1: (3,), 2: (), 3: (1,)}[art]
        return auswahl(txt + ' Wie verbessert man die Umfrage am wirksamsten?', bess[art], [v for k, v in bess.items() if k != art and k not in aus],
                       w, 'Finde zuerst die Fehlerquelle, dann die passende Verbesserung.')
    return auswahl(txt + ' Welche Fehlerquelle liegt vor?', richtig, [f for f in FEHLER_ART if f != richtig], w,
                   'Prüfe: Größe, Auswahl, Fragestellung, Freiwilligkeit.')


def g_aussagen(s):
    if s == 1:
        n1 = R.choice([8, 10, 12, 15, 20])
        n2 = R.choice([300, 400, 500, 800, 1000])
        return auswahl(f'Stichprobe A hat {n1} Befragte, Stichprobe B hat {n2}. Beide wurden zufällig ausgewählt. Welche schwankt vermutlich weniger?',
                       'B', ['A', 'Beide gleich', 'Das kann man nicht sagen.'],
                       'Je größer eine zufällige Stichprobe, desto weniger schwankt ihr Ergebnis.', 'Was macht eine Stichprobe zuverlässiger?')
    if s == 2:
        if R.random() < 0.5:
            n = R.choice([20, 25, 40, 50])
            k = R.randint(n // 5, n * 4 // 5)
            p = Fr(k, n) * 100
            ein, ein_d = R.choice([('Kinder', 'Kindern'), ('Jugendliche', 'Jugendlichen'), ('Kunden', 'Kunden'), ('Fahrgäste', 'Fahrgästen')])
            richtig = f'Ungefähr {dz(p)} % aller {schwach(ein)} – ein Schätzwert.'
            return auswahl(f'In einer guten Zufallsstichprobe sagen {k} von {n} {ein_d} „ja“. Was kann man über alle {schwach(ein)} sagen?', richtig,
                           [f'Genau {dz(p)} % aller {schwach(ein)} sagen „ja“.', f'Genau {k} {ein} sagen „ja“.', 'Man kann gar nichts sagen.'],
                           f'{k} : {n} = {dz(p)} %. Für die Grundgesamtheit ist das nur ein Schätzwert, weil Stichproben schwanken.',
                           'Ist eine Stichprobe genau gleich wie die Grundgesamtheit?')
        werte = []
        n = R.choice([20, 25, 50])
        for _ in range(4):
            werte.append(R.randint(n // 4, n * 3 // 4))
        if len(set(werte)) < 3: return None
        pr = [Fr(k, n) * 100 for k in werte]
        sp = max(pr) - min(pr)
        return zahl(f'Vier Gruppen ziehen je eine Zufallsstichprobe mit n = {n} aus derselben Schule. Sie zählen {", ".join(map(str, werte))} Kinder mit Haustier. '
                    f'Wie groß ist die Spannweite der Anteile in Prozentpunkten?',
                    f'Anteile: {", ".join(dz(x) + " %" for x in pr)}. Spannweite: {dz(max(pr))} − {dz(min(pr))} = {dz(sp)} Prozentpunkte.',
                    'Rechne jeden Anteil in Prozent um und ziehe den kleinsten vom größten ab.', sp,
                    f'(max({", ".join(map(str, werte))}) - min({", ".join(map(str, werte))})) / {n} * 100')
    art = R.random()
    if art < 0.35:
        n = R.choice([5, 6, 8, 10])
        k = R.randint(1, n - 1)
        p = Fr(k, n) * 100
        if not endlich(p): return None
        stadt = R.choice(['Augsburg', 'Regensburg', 'Würzburg', 'Ingolstadt'])
        return auswahl(f'Eine Zeitung schreibt: „{dz(p)} % der Einwohner von {stadt} wollen ein Stadion!“ Grundlage: {k} von {n} Personen in einer Fußballkneipe sagten ja. Wie ist die Aussage zu beurteilen?',
                       'Nicht haltbar: Stichprobe viel zu klein und einseitig.',
                       ['Haltbar, weil es eine Prozentangabe ist.', 'Nur zu klein, die Auswahl ist in Ordnung.', 'Nur einseitig, die Größe ist in Ordnung.'],
                       f'{n} Personen sind viel zu wenige, und Fußballfans sind eher für ein Stadion. Beide Fehler stecken drin.',
                       'Prüfe Größe UND Auswahl.')
    if art < 0.7:
        n = R.choice([200, 400, 500, 1000])
        p1 = R.choice([48, 49, 51, 52])
        p2 = 100 - p1
        return auswahl(f'Bei einer guten Zufallsstichprobe mit {n} Befragten sind {p1} % für Vorschlag A und {p2} % für Vorschlag B. Welche Aussage ist angemessen?',
                       'Es ist ziemlich knapp; in der Grundgesamtheit könnte es auch umgekehrt sein.',
                       [f'{"A" if p1 > p2 else "B"} hat sicher die Mehrheit.', f'Genau {max(p1, p2)} % aller sind für {"A" if p1 > p2 else "B"}.', 'Die Umfrage ist wertlos.'],
                       f'Der Unterschied beträgt nur {abs(p1 - p2)} Prozentpunkte. Stichproben schwanken – bei so wenig Abstand ist keine sichere Aussage möglich.',
                       'Wie stark können Stichproben schwanken?')
    n1, n2 = R.choice([10, 20]), R.choice([200, 500])
    k1 = R.randint(n1 // 5, n1 * 4 // 5)
    k2 = R.randint(n2 // 5, n2 * 4 // 5)
    p1, p2 = Fr(k1, n1) * 100, Fr(k2, n2) * 100
    if p1 == p2 or not endlich(p1) or not endlich(p2): return None
    return zahl(f'Klasse 7a befragt {n1} zufällig gewählte Kinder: {k1} lesen gern. Klasse 7b befragt {n2}: {k2} lesen gern. Um wie viele Prozentpunkte unterscheiden sich die Ergebnisse?',
                f'{k1} : {n1} = {dz(p1)} %; {k2} : {n2} = {dz(p2)} %. Unterschied {dz(abs(p1 - p2))} Prozentpunkte. Dem Ergebnis der 7b (größere Stichprobe) kann man eher trauen.',
                'Beide Anteile in Prozent, dann Differenz.', abs(p1 - p2), f'abs({k1} / {n1} * 100 - {k2} / {n2} * 100)')


GEN = {'begriffe': g_begriffe, 'hochrechnen': g_hochrechnen, 'repraesentativ': g_repraesentativ,
       'fehlerquellen': g_fehlerquellen, 'aussagen': g_aussagen}

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import tab  # noqa: E402


def _s(*w, einheit='Kinder'):
    return {'typ': 'saeulen', 'einheit': einheit, 'werte': [{'name': n, 'wert': x} for n, x in w], 'zahlen': True}


_FQ = tab(['Fehlerquelle', 'Beispiel'], ['zu klein', '5 Befragte'], ['einseitig', 'nur Vereinsmitglieder'],
          ['suggestiv', '„doch sicher dafür?“'], ['freiwillig', 'Online-Abstimmung'])
UMBAU = {
    'begriffe': {
        'einstieg': 'Beim Kochen probierst du einen Löffel, nicht den ganzen Topf. Eine Schule mit 620 Kindern macht es genauso: '
                    'Sie fragt nur 50 Kinder. Diese 50 sind die ⟦Stichprobe⟧.',
        'woerter': [['Grundgesamtheit', 'alle, über die man etwas wissen will – der ganze Topf'],
                    ['Stichprobe', 'der Teil, der wirklich befragt wird – der Löffel'],
                    ['Stichprobenumfang n', 'wie viele in der Stichprobe sind']],
        'bild': _s(('Schule', 620), ('befragt', 50)),
        'schritte': [
            {'text': 'Die Schule will wissen, wie alle 620 Kinder zur Schule kommen.', 'bild': _s(('Schule', 620))},
            {'text': 'Die Grundgesamtheit sind ⟦alle 620 Kinder⟧.'},
            {'text': 'Befragt werden nur 50 Kinder: die Stichprobe.', 'bild': _s(('Schule', 620), ('befragt', 50))},
            {'text': 'Ihr Stichprobenumfang n = ⟦50⟧.'},
        ],
        'fehler': 'Die 50 Befragten sind nicht die Grundgesamtheit. Die Grundgesamtheit ist ⟦die ganze Gruppe⟧, hier alle 620 Kinder.',
        'regel': 'Grundgesamtheit = alle, Stichprobe = der befragte Teil. Ihre Größe heißt ⟦Stichprobenumfang n⟧. Befragt man alle, heißt das ⟦Vollerhebung⟧.',
    },
    'hochrechnen': {
        'einstieg': 'Von 80 befragten Kindern kommen 28 mit dem Rad. Wie viele sind es an der ganzen Schule mit 640 Kindern? '
                    'Man überträgt den Anteil auf alle. Das heißt ⟦Hochrechnung⟧.',
        'woerter': [['relative Häufigkeit', 'der Anteil in der Stichprobe: Anzahl geteilt durch n'],
                    ['Hochrechnung', 'den Anteil der Stichprobe auf alle übertragen; ergibt eine Schätzung'],
                    ['Prozentpunkte', 'Unterschied zwischen zwei Prozentangaben, z. B. 40 % − 35 % = 5 Prozentpunkte']],
        'bild': {'typ': 'bruchstreifen', 'teile': 20, 'gefaerbt': 7, 'ganzes': '80 Kinder', 'teil_text': '28 mit Rad'},
        'schritte': [
            {'text': 'Relative Häufigkeit: 28 : 80 = 0,35, also 35 %.'},
            {'text': 'Die ganze Schule hat 640 Kinder, der Anteil bleibt gleich.', 'bild': {'ganzes': '640 Kinder', 'teil_text': '?'}},
            {'text': 'Hochrechnung: 0,35 · 640 = ⟦224⟧.', 'bild': {'teil_text': 'etwa 224'}},
            {'text': 'Etwa 224 Kinder kommen mit dem Rad. Das ist eine Schätzung.'},
        ],
        'fehler': '28 · 640 = 17 920 ist falsch, so viele Kinder hat die Schule gar nicht. Erst den ⟦Anteil⟧ bilden, dann malnehmen.',
        'regel': 'Erst den Anteil der Stichprobe, dann mal die Grundgesamtheit. Das Ergebnis ist nur eine ⟦Schätzung⟧.',
    },
    'repraesentativ': {
        'einstieg': 'Wie viele Jugendliche in Bayern treiben Sport? Ein Forscher fragt nur in einem Fußballverein. '
                    'Dort treiben alle Sport! Seine Stichprobe ist deshalb nicht ⟦repräsentativ⟧.',
        'woerter': [['repräsentativ', 'die Stichprobe sieht aus wie die Grundgesamtheit im Kleinen'],
                    ['verzerrt', 'schief, weil eine Gruppe zu stark vertreten ist'],
                    ['zufällig', 'jeder hat dieselbe Chance, ausgewählt zu werden']],
        'bild': _s(('Verein', 100), ('zufällig', 60), einheit='% Sport'),
        'schritte': [
            {'text': 'Im Fußballverein treiben ⟦100 %⟧ der Befragten Sport.', 'bild': _s(('Verein', 100), einheit='% Sport')},
            {'text': 'Bei zufällig Befragten aus vielen Schulen sind es zum Beispiel nur 60 %.',
             'bild': _s(('Verein', 100), ('zufällig', 60), einheit='% Sport')},
            {'text': 'Die Vereins-Stichprobe ist ⟦verzerrt⟧: Sportler sind zu stark vertreten.'},
        ],
        'fehler': '„500 Befragte, also repräsentativ“ ist falsch. Auch eine große Stichprobe ist ⟦verzerrt⟧, wenn alle aus einer besonderen Gruppe stammen.',
        'regel': 'Eine gute Stichprobe ist zufällig gewählt und groß genug. Nur dann ist sie ⟦repräsentativ⟧.',
    },
    'fehlerquellen': {
        'einstieg': 'Ein Verein will einen neuen Spielplatz. Er fragt: „Sie sind doch sicher auch dafür?“ Fast alle sagen Ja. '
                    'Die Frage gibt die Antwort schon vor. Sie ist ⟦suggestiv⟧.',
        'woerter': [['suggestiv', 'drängt zu einer bestimmten Antwort'],
                    ['einseitig', 'nur eine bestimmte Gruppe wird gefragt'],
                    ['freiwillig', 'nur wer will, antwortet – meist mit starker Meinung']],
        'bild': _FQ,
        'schritte': [
            {'text': 'Die Frage lautet: „Sie sind doch sicher auch dafür?“',
             'bild': tab(['Frage', 'neutral?'], ['„Sie sind doch sicher dafür?“', '?'])},
            {'text': 'Sie drängt zum Ja: Fehlerquelle ⟦suggestive Frage⟧.',
             'bild': tab(['Frage', 'neutral?'], ['„Sie sind doch sicher dafür?“', 'nein'])},
            {'text': 'Neutral fragen: „Soll der Spielplatz erneuert werden?“',
             'bild': tab(['Frage', 'neutral?'], ['„Sie sind doch sicher dafür?“', 'nein'], ['„Soll der Spielplatz erneuert werden?“', 'ja'])},
            {'text': 'Weitere Fehlerquellen: zu klein, einseitig, nur freiwillige Antworten.', 'bild': _FQ},
        ],
        'fehler': 'Eine Online-Abstimmung mit 10 000 Stimmen ist nicht repräsentativ. Es antworten nur ⟦Freiwillige⟧ mit starker Meinung.',
        'regel': 'Prüfe Größe, Auswahl, Frage und wer antwortet. ⟦Suggestive Fragen⟧ und einseitige Auswahl verzerren.',
    },
    'aussagen': {
        'einstieg': 'Zwei Klassen fragen nach dem Mensaessen. Die eine fragt 10 Kinder, die andere 500. '
                    'Die Ergebnisse sind verschieden. Stichproben ⟦schwanken⟧, kleine stärker als große.',
        'woerter': [['schwanken', 'bei jeder Stichprobe kommt ein etwas anderer Anteil heraus'],
                    ['Prozentpunkte', 'Unterschied zwischen zwei Prozentangaben, z. B. 70 % − 52 %']],
        'bild': _s(('A: 10', 70), ('B: 500', 52), einheit='% mögen es'),
        'schritte': [
            {'text': 'A: 7 von 10 mögen das Essen, das sind 70 %.', 'bild': _s(('A: 10', 70), einheit='% mögen es')},
            {'text': 'B: 260 von 500 mögen es, das sind 52 %.', 'bild': _s(('A: 10', 70), ('B: 500', 52), einheit='% mögen es')},
            {'text': 'Unterschied: 70 % − 52 % = ⟦18 Prozentpunkte⟧.'},
            {'text': 'B ist ⟦aussagekräftiger⟧, weil sie viel größer ist und weniger schwankt.'},
        ],
        'fehler': '„In der Stichprobe 40 %, also genau 40 % bei allen“ ist falsch. Eine Stichprobe liefert nur einen ⟦Schätzwert⟧.',
        'regel': 'Stichproben liefern nur ungefähre Werte. Je ⟦größer⟧ die Stichprobe, desto weniger schwankt sie.',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-1) ----------
# Prüfungsvorbilder: VERA-8 / Jahrgangsstufentests (Leitidee Daten: Aussagen zu Umfragen beurteilen, Hochrechnen),
# Fang-Wiederfang-Schätzung (Standardaufgabe zu Stichproben), Zeitungs- und Werbeaussagen prüfen. Typ übernommen, Wortlaut und Zahlen eigen.
def durchsicht(d):
    from _rsib1 import Z, A, nachtrag, finde
    T = lambda teil: finde(d, teil)
    nachtrag(d,
        umstufen={
            T('4 Klassen. Aus jeder Klasse werden per Los gleich viele Kinder gezogen, insgesamt 32'): 2,
            T('10 Klassen. Aus jeder Klasse werden per Los gleich viele Kinder gezogen, insgesamt 40'): 2,
            T('Von 100 befragten Jugendlichen eines Landkreises mit 860 Jugendlichen spielen 20'): 2,
            T('Von 200 befragten Fahrgästen einer Bahnlinie mit 2 600 Fahrgästen'): 2,
            T('„Jeder vernünftige Mensch ist dafür, dass der Bus öfter fährt. Sie auch?“'): 2,
            T('„Handyverbot an Schulen“ denken, und ruft sie auf, im Internet abzustimmen. Es kommen 1 200 Antworten'): 2,
            T('Klasse 7a befragt 10 zufällig gewählte Kinder'): 2,
            T('Klasse 7a befragt 20 zufällig gewählte Kinder'): 2,
        },
        ersetzen={
            T('4 Klassen. Aus jeder Klasse werden per Los gleich viele Kinder gezogen, insgesamt 16'):
                Z(3, 'Eine Schule mit 600 Kindern hat 24 Klassen. Aus jeder Klasse werden 2 Kinder ausgelost. Wie viel Prozent aller Kinder werden befragt?',
                  8, '24*2/600*100', '24 · 2 = 48 Kinder. 48 : 600 = 0,08 = 8 %.', 'Wie viele Kinder sind es zusammen? Welcher Anteil von 600 ist das?', einheit='%'),
            T('12 Klassen. Aus jeder Klasse werden per Los gleich viele Kinder gezogen, insgesamt 84'):
                A(3, 'Eine Firma will prüfen, wie lange ihre Feuerwerksraketen brennen. Warum testet sie nur eine Stichprobe?',
                  'Jede getestete Rakete ist danach verbraucht.', ['Eine Stichprobe ist genauer als eine Vollerhebung.', 'Raketen darf man nicht zählen.', 'Eine Vollerhebung ist verboten.'],
                  'Beim Test brennt die Rakete ab. Bei einer Vollerhebung bliebe keine Rakete zum Verkaufen übrig.',
                  'Was passiert mit einer Rakete beim Test?'),
            T('„20 % der Einwohner von Würzburg wollen ein Stadion!“'):
                A(3, 'Ein Prospekt wirbt: „9 von 10 Zahnärzten empfehlen unsere Zahnpasta.“ Befragt wurden 10 Zahnärzte, die der Hersteller ausgesucht hat. Wie ist die Aussage zu beurteilen?',
                  'Nicht haltbar: viel zu wenige und vom Hersteller ausgesucht.', ['Haltbar, weil 90 % sehr viel ist.', 'Haltbar, weil Zahnärzte Fachleute sind.', 'Nur zu klein, die Auswahl ist in Ordnung.'],
                  '10 Befragte schwanken stark, und wer vom Hersteller ausgesucht wird, ist vermutlich für das Produkt. Zwei Fehlerquellen zugleich.',
                  'Prüfe Größe und Auswahl der Stichprobe.'),
            T('Stichprobe A hat 12 Befragte, Stichprobe B hat 400'):
                A(1, 'Zwei kleine Zufallsstichproben (je 10 Kinder) aus derselben Schule ergeben 60 % und 40 %. Was ist die wahrscheinlichste Erklärung?',
                  'Kleine Stichproben schwanken zufällig.', ['Eine der Gruppen hat sich verrechnet.', 'Die Schule hat sich verändert.', 'Beide Stichproben sind gefälscht.'],
                  'Bei nur 10 Befragten machen 2 Kinder schon 20 Prozentpunkte aus. Solche Unterschiede entstehen durch Zufall.',
                  'Wie viel macht ein einzelnes Kind bei 10 Befragten aus?'),
            T('Stichprobe A hat 10 Befragte, Stichprobe B hat 500'):
                A(1, 'In einer Zufallsstichprobe sagen 30 % „ja“. Ist das sicher der Anteil in der ganzen Grundgesamtheit?',
                  'Nein, es ist ein Schätzwert.', ['Ja, genau 30 %.', 'Nein, es sind sicher mehr.', 'Nein, es sind sicher weniger.'],
                  'Eine Stichprobe zeigt nur einen Teil. 30 % ist ein Schätzwert; der wahre Anteil liegt vermutlich in der Nähe.',
                  'Wurden alle befragt?'),
        },
        neu={
            'begriffe': [
                Z(3, 'Eine Stadt hat 24 000 Haushalte. 1,5 % davon sollen befragt werden. Eine Interviewerin schafft 40 Haushalte. Wie viele Interviewerinnen braucht man mindestens?',
                  9, '24000*15/1000/40', '1,5 % von 24 000 = 360 Haushalte. 360 : 40 = 9 Interviewerinnen.',
                  'Rechne zuerst den Stichprobenumfang aus.'),
                A(3, 'Man will wissen, wie viele Siebtklässler in Bayern ein Handy haben. Befragt werden 300 Siebtklässler aus 15 Schulen. Was ist die Grundgesamtheit?',
                  'Alle Siebtklässler in Bayern', ['Die 300 befragten Kinder', 'Alle Kinder in Bayern', 'Die 15 Schulen'],
                  'Die Frage betrifft alle Siebtklässler in Bayern. Die 300 Kinder sind die Stichprobe, die Schulen nur der Ort der Befragung.',
                  'Über wen will man am Ende etwas sagen?'),
                A(3, 'Welche Auswahl ist eine Zufallsstichprobe aus allen 800 Kindern einer Schule?',
                  'Jedes 16. Kind auf der Schülerliste, Start beim ausgelosten Platz', ['Die ersten 50 Kinder am Schultor', 'Alle Kinder, die sich freiwillig melden', 'Die 50 Kinder der Klassensprecherwahl'],
                  'Nur bei der Liste mit ausgelostem Start hat jedes Kind dieselbe Chance. Am Schultor kommen zuerst die Frühaufsteher, freiwillig melden sich die Interessierten.',
                  'Hat jedes Kind die gleiche Chance, gezogen zu werden?'),
                Z(3, 'Aus jeder der 6 Klassen einer Jahrgangsstufe werden gleich viele Kinder ausgelost, zusammen 15 % der 240 Kinder. Wie viele Kinder kommen aus jeder Klasse?',
                  6, '240*15/100/6', '15 % von 240 = 36 Kinder. 36 : 6 = 6 Kinder je Klasse.',
                  'Rechne erst den Stichprobenumfang aus, dann teile.'),
            ],
            'hochrechnen': [
                Z(3, 'In einem Teich werden 50 Fische gefangen, markiert und wieder freigelassen. Später fängt man 40 Fische; 5 davon sind markiert. Schätze, wie viele Fische im Teich leben.',
                  400, '50*40/5', 'In der zweiten Stichprobe sind 5 von 40 = 12,5 % markiert. 50 Fische sind also etwa 12,5 % aller Fische: 50 : 0,125 = 400.',
                  'Welcher Anteil der zweiten Stichprobe ist markiert? Dieser Anteil gilt ungefähr für den ganzen Teich.'),
                A(3, 'Eine Schule hat 1 500 Kinder. Stichprobe A (50 Kinder) ergibt 30 % Radfahrer, Stichprobe B (200 Kinder) ergibt 24 %. Welche Hochrechnung ist vertrauenswürdiger?',
                  'Etwa 360 Radfahrer (aus B)', ['Etwa 450 Radfahrer (aus A)', 'Etwa 405 Radfahrer (Mittelwert)', 'Genau 360 Radfahrer'],
                  'Die größere Zufallsstichprobe schwankt weniger: 0,24 · 1 500 = 360. Es bleibt eine Schätzung, darum „etwa“.',
                  'Welche Stichprobe schwankt weniger?'),
                Z(3, 'In einer Stichprobe von 40 Kindern haben 30 % ein Haustier. Wie viele Kinder mit Haustier mehr hätten es in der Stichprobe sein müssen, damit die Hochrechnung für 800 Kinder 320 ergibt?',
                  4, '320*40/800 - 40*30/100', '320 von 800 sind 40 %. 40 % von 40 = 16 Kinder, 30 % von 40 = 12 Kinder. Es fehlen 4.',
                  'Welcher Anteil steckt hinter 320 von 800?'),
                Z(3, 'Von 50 befragten Kindern einer Schule mit 750 Kindern fahren 18 mit dem Rad. Schätze, wie viele Kinder der Schule NICHT mit dem Rad fahren.',
                  480, '750*(50-18)/50', '50 − 18 = 32 fahren nicht Rad: 32 : 50 = 64 %. 0,64 · 750 = 480.',
                  'Rechne mit dem Anteil der Kinder, die nicht Rad fahren.'),
            ],
            'repraesentativ': [
                A(3, 'Die Schülerzeitung befragt alle 120 Kinder, die am Montag in der Mensa essen. 80 % finden das Essen gut. Schlagzeile: „80 % der Schule mögen das Mensaessen“. Was ist das Hauptproblem?',
                  'Wer in der Mensa isst, mag das Essen eher.', ['120 Kinder sind zu wenige für eine Schule.', 'Man hätte in Prozentpunkten rechnen müssen.', 'Montag ist ein ungewöhnlicher Tag.'],
                  'Kinder, die das Essen nicht mögen, essen eher woanders. Sie fehlen in der Stichprobe: Die Auswahl ist einseitig.',
                  'Wer fehlt in der Stichprobe?'),
                A(3, 'Eine Umfrage zur Freizeit erreicht die Leute nur über das Festnetz-Telefon, vormittags an Werktagen. Welche Gruppe ist vermutlich zu schwach vertreten?',
                  'Berufstätige und Jugendliche', ['Rentnerinnen und Rentner', 'Menschen mit Festnetz', 'Alle Gruppen gleich'],
                  'Vormittags sind Berufstätige bei der Arbeit, Jugendliche in der Schule; viele Jüngere haben kein Festnetz. Rentner werden eher erreicht.',
                  'Wer ist vormittags zu Hause und hat Festnetz?'),
            ],
            'fehlerquellen': [
                A(3, 'Welche Frage ist neutral gestellt?',
                  '„Wie oft sollte der Bus fahren: alle 10, 20 oder 30 Minuten?“', ['„Sie wollen doch auch, dass der Bus öfter fährt?“', '„Finden Sie den seltenen Bus nicht auch ärgerlich?“', '„Jeder will mehr Busse. Sie auch?“'],
                  'Die neutrale Frage nennt mehrere Möglichkeiten und keine Meinung. Die anderen drängen zu einer Antwort.',
                  'Welche Frage verrät keine gewünschte Antwort?'),
                A(3, 'Ein Sportverein fragt auf seiner Internetseite: „Wollt ihr nicht auch endlich einen Kunstrasen?“ 400 Mitglieder klicken. Welche Fehlerquellen liegen vor?',
                  'Suggestive Frage und nur Freiwillige', ['Nur: Die Stichprobe ist zu klein.', 'Nur: Die Frage ist suggestiv.', 'Keine, 400 Antworten genügen.'],
                  '„Nicht auch endlich“ lenkt zum Ja. Und es klicken nur Mitglieder, die sich melden wollen. Zwei Fehlerquellen zugleich.',
                  'Prüfe die Frage und wer antwortet – getrennt.'),
                A(3, 'Die Schülerzeitung befragt 40 Kinder der Theater-AG, ob sie gern ins Theater gehen. Sie verdoppelt danach auf 80 Kinder der Theater-AG. Wird das Ergebnis aussagekräftiger für die ganze Schule?',
                  'Nein, die Auswahl bleibt einseitig.', ['Ja, doppelt so viele sind doppelt so gut.', 'Ja, ab 80 ist eine Stichprobe immer repräsentativ.', 'Nein, 80 sind zu viele.'],
                  'Mehr Kinder aus derselben besonderen Gruppe ändern die Verzerrung nicht. Man muss aus der ganzen Schule zufällig auswählen.',
                  'Was hat sich an der Auswahl geändert?'),
                A(3, 'Ein Hotel verschickt 500 Fragebögen. 60 kommen zurück, 50 davon „sehr zufrieden“. Das Hotel wirbt: „83 % unserer Gäste sind sehr zufrieden.“ Warum ist das fragwürdig?',
                  'Nur 12 % haben geantwortet – vor allem die mit starker Meinung.', ['50 von 60 sind nicht 83 %.', 'Fragebögen sind immer ungültig.', 'Man hätte 1 000 Bögen verschicken müssen.'],
                  '50 von 60 sind zwar etwa 83 %, aber nur 60 von 500 = 12 % haben geantwortet. Wer antwortet, entscheidet selbst – das verzerrt.',
                  'Wie viele der Gäste haben überhaupt geantwortet?'),
            ],
            'aussagen': [
                A(3, 'Umfrage A: 7 von 20 Kindern (35 %) lesen täglich. Umfrage B ein Jahr später: 1 200 von 4 000 (30 %). Ein Reporter schreibt: „Der Anteil ist von 35 % auf 30 % gesunken.“ Wie ist das zu beurteilen?',
                  'Unsicher: Bei nur 20 Befragten kann A leicht um 5 Prozentpunkte daneben liegen.', ['Sicher richtig, 35 > 30.', 'Falsch, der Anteil ist gestiegen.', 'Richtig, weil B so groß ist.'],
                  'Bei 20 Befragten macht ein Kind 5 Prozentpunkte aus. Der Unterschied kann reiner Zufall sein.',
                  'Wie viel macht ein Kind bei 20 Befragten aus?'),
                A(3, 'In einer guten Umfrage (1 000 Befragte) kommt eine Partei auf 5,2 %. Für den Einzug in den Landtag braucht sie 5 %. Welche Schlagzeile ist angemessen?',
                  '„Partei knapp über 5 % – Einzug unsicher“', ['„Partei sicher im Landtag“', '„Partei scheitert“', '„Genau 5,2 % wählen die Partei“'],
                  'Auch große Stichproben schwanken um einige Zehntel bis wenige Prozentpunkte. 5,2 % ist zu knapp für „sicher“.',
                  'Wie weit liegt 5,2 % von 5 % entfernt – und wie stark schwankt eine Umfrage?'),
                Z(3, 'Wie viele Personen muss man befragen, damit eine einzelne Person genau 0,5 Prozentpunkte ausmacht?',
                  200, '100/0.5', '1 Person = 0,5 % heißt: 100 % entsprechen 100 : 0,5 = 200 Personen.',
                  'Bei 100 Befragten ist eine Person 1 %. Wie viele für die Hälfte?'),
                Z(3, 'In einer Stichprobe mit 50 Befragten sagen 20 „ja“ (40 %). Wie viele „ja“ müssten es mindestens sein, damit der Anteil über 50 % liegt?',
                  26, '50/2 + 1', '50 % von 50 sind 25. „Über 50 %“ heißt mindestens 26.',
                  'Wie viele sind genau 50 %?'),
            ],
        })


# ---- STUFEN (Zwanzigste Runde, Zusatz RS/IB, Zweig stufen-rsib-1) ----
from _stufen_rsib1 import Stufen, stufen  # noqa: E402

ST = Stufen('daten.stichproben', 20_71_3)
Z, A, L = ST.Z, ST.A, ST.L

# begriffe
ST.stufenleiter('begriffe', 'Grundgesamtheit, Stichprobe und Stichprobenumfang benennen.',
                'Stichprobenumfang aus einem Prozentsatz, gleich viele je Klasse, Grundgesamtheit aus Umfang und Anteil zurückrechnen.',
                'Gründe für Stichproben begründen, Zufallsstichprobe beurteilen, Anteil der Befragten, Aufwand planen, Fehler „Vollerhebung heißt Stichprobe“, Schrittweite k, geschichtete Prüfungsaufgabe.')
ST.typ('begriffe', '/Stichprobenumfang n\\?$/', 'direkt')
ST.typ('begriffe', '/Was ist die Grundgesamtheit\\?$/', 'erkennen')
ST.typ('begriffe', '/^Aus [\\d ]+ Personen werden/', 'mehrschritt')
ST.typ('begriffe', 'Alle 1 200 Kinder', 'erkennen')
ST.typ('begriffe', 'In einer Schule gibt es', 'einkleidung')
ST.typ('begriffe', '/^(Warum macht man|Eine Firma will|Man will wissen, ob die Einwohner ein neues Hallenbad wollen, und)/', 'begruenden')
ST.typ('begriffe', 'Eine Schule mit 600', 'verknuepfen')
ST.typ('begriffe', 'Eine Stadt hat 24 000', 'transfer')
ST.typ('begriffe', 'Welche Auswahl ist eine Zufallsstichprobe', 'erkennen')
ST.typ('begriffe', 'Aus jeder der 6 Klassen', 'mehrschritt')
ST.neu('begriffe', 'umkehr', Z('Bei einer Umfrage wurden 45 Personen befragt; das sind 3 % der Grundgesamtheit. Wie groß ist die Grundgesamtheit?', 1500, '45 * 100 / 3',
       '3 % entsprechen 45 Personen, 1 % entspricht 15. 100 % sind 1 500 Personen.', 'Rechne zuerst aus, wie viele Personen 1 % sind.'))
ST.neu('begriffe', 'umkehr', Z('Eine Stichprobe von 60 Kindern ist ein Fünftel aller Kinder einer Jahrgangsstufe. Wie viele Kinder hat die Jahrgangsstufe?', 300, '60 * 5',
       'Ein Fünftel sind 60, das Ganze ist 5 · 60 = 300.', 'Ein Fünftel mal fünf ergibt das Ganze.'))
ST.neu('begriffe', 'fehler', A('Jemand sagt: „Wir haben alle 30 Kinder der Klasse 7a befragt. Das ist eine Stichprobe der Klasse 7a.“ Was stimmt?', 'Falsch: Wer alle befragt, macht eine Vollerhebung der Klasse 7a.',
       ['Richtig.', 'Falsch: 30 Kinder sind zu wenige für eine Stichprobe.', 'Falsch: Eine Stichprobe muss genau 10 Kinder haben.'],
       'Eine Stichprobe ist nur ein Teil der Grundgesamtheit. Für die Klasse 7a ist das eine Vollerhebung. Eine Stichprobe wäre es erst für eine größere Grundgesamtheit, etwa die ganze Schule.', 'Wurden alle oder nur ein Teil befragt?'))
ST.neu('begriffe', 'parameter', Z('Man befragt jede k-te Person einer Liste mit 1 200 Personen. Es sollen genau 60 Personen befragt werden. Wie groß muss k sein?', 20, '1200 // 60',
       '1 200 : k = 60 ⇒ k = 1 200 : 60 = 20. Jede 20. Person wird befragt.', 'Wie oft passt der Abstand k in die Liste?'))
ST.neu('begriffe', 'pruefung', L('Ein Verein hat 480 Mitglieder: Fußball 200, Tennis 120, Turnen 100, Schwimmen 60. 48 Mitglieder sollen befragt werden, jede Abteilung nach ihrem Anteil. Wie viele kommen aus dem Fußball, wie viele aus dem Schwimmen?',
       'Fußball □; Schwimmen □', [20, 6], ['200 * 48 // 480', '60 * 48 // 480'],
       '48 von 480 sind 10 %. Fußball: 10 % von 200 = 20. Schwimmen: 10 % von 60 = 6. (Tennis 12, Turnen 10 – zusammen 48.)', 'Welcher Anteil aller Mitglieder wird befragt?'))
ST.knobel('begriffe', Z('Aus den fünf Kindern A, B, C, D und E werden zwei per Los für eine Befragung gezogen. Wie viele verschiedene Stichproben sind möglich?', 10, '5 * 4 // 2',
          'Für das erste Kind gibt es 5, für das zweite 4 Möglichkeiten: 20. Jede Stichprobe ist dabei doppelt gezählt (AB und BA), also 10. Liste: AB, AC, AD, AE, BC, BD, BE, CD, CE, DE.', 'Schreibe alle Paare systematisch auf.'))
ST.knobel('begriffe', Z('Auf einer Liste stehen 100 Kinder. Man lost einen Startplatz von 1 bis 7 und befragt dann jedes 7. Kind (Startplatz, Startplatz + 7, …). Wie viele Kinder werden höchstens befragt?', 15, '15',
          'Start 1: 1, 8, …, 99 sind 15 Kinder (1 + 7 · 14 = 99). Start 2: 2, 9, …, 100 ebenfalls 15. Ab Start 3 sind es nur 14, weil 3 + 7 · 14 = 101 > 100. Höchstens 15.', 'Probiere verschiedene Startplätze.'))

# hochrechnen
ST.stufenleiter('hochrechnen', 'Den Anteil in der Stichprobe in Prozent ausrechnen.',
                'Auf die Grundgesamtheit hochrechnen, auch aus einem Diagramm; aus der Hochrechnung auf die Stichprobe zurück; Gegenanteil.',
                'Prozentpunkte vergleichen, Fische markieren, vertrauenswürdigere Hochrechnung begründen, fehlende Antworten rückwärts, Fehler „Anzahl mal Gesamtzahl“, Stichprobenumfang als Unbekannte, Verkehrszählung als Prüfungsaufgabe.')
ST.typ('hochrechnen', '/Wie viel Prozent sind das in der Stichprobe\\?$/', 'direkt')
ST.typ('hochrechnen', '/(Schätze, wie viele .* insgesamt|vermutlich insgesamt)/', 'mehrschritt')
ST.typ('hochrechnen', 'In einer Grundgesamtheit', 'umkehr')
ST.typ('hochrechnen', 'Gefragt wird', 'verknuepfen')
ST.typ('hochrechnen', 'In einem Teich', 'transfer')
ST.typ('hochrechnen', 'Eine Schule hat 1 500', 'begruenden')
ST.typ('hochrechnen', 'In einer Stichprobe von 40 Kindern', 'rueckwaerts')
ST.typ('hochrechnen', '/NICHT mit dem Rad/', 'mehrschritt')
ST.neu('hochrechnen', 'erkennen', A('Von 50 befragten Kindern haben 10 einen Hund. Welche Rechnung liefert den Anteil in der Stichprobe?', '10 : 50', ['50 : 10', '10 · 50', '50 − 10'],
       'Anteil = Teil : Ganzes = 10 : 50 = 0,2 = 20 %.', 'Teil durch Ganzes.'))
ST.neu('hochrechnen', 'darstellung', Z('Ein Kreisdiagramm zu einer Stichprobe zeigt: Ein Viertel der Befragten fährt mit dem Rad zur Schule. Die Schule hat 840 Kinder. Schätze, wie viele mit dem Rad kommen.', 210, '840 // 4',
       'Ein Viertel ist 25 %. 840 : 4 = 210 Kinder (Schätzung).', 'Welchen Anteil zeigt ein Viertelkreis?'))
ST.neu('hochrechnen', 'fehler', A('Jemand rechnet: „12 von 40 Befragten fahren Rad, die Schule hat 600 Kinder. Also fahren 12 · 600 = 7 200 Kinder Rad.“ Was stimmt?', 'Falsch: Erst den Anteil 12 : 40 = 30 % bilden, dann 30 % von 600 = 180.',
       ['Richtig.', 'Falsch: 600 : 12 = 50 Kinder.', 'Falsch: 600 − 12 = 588 Kinder.'], 'Man rechnet mit dem Anteil, nicht mit der Anzahl. 7 200 ist mehr als die ganze Schule – das kann nicht stimmen.', 'Kann das Ergebnis größer sein als die Schule?'))
ST.neu('hochrechnen', 'parameter', Z('In einer Stichprobe von n Kindern sagen 18 „ja“. Hochgerechnet auf 900 Kinder ergibt das 270 „ja“. Wie groß ist n?', 60, '18 * 900 // 270',
       'Der Anteil ist 270 : 900 = 0,3. In der Stichprobe: 18 : n = 0,3 ⇒ n = 18 : 0,3 = 60.', 'Welcher Anteil steckt in der Hochrechnung?'))
ST.neu('hochrechnen', 'pruefung', L('Bei einer Verkehrszählung werden an einer Kreuzung 250 Autos beobachtet, 40 davon sind Elektroautos. a) Wie viel Prozent sind das? b) Schätze, wie viele der 12 500 Autos der Stadt Elektroautos sind.',
       'a) □ %; b) □', [16, 2000], ['40 * 100 // 250', '12500 * 16 // 100'], 'a) 40 : 250 = 0,16 = 16 %. b) 16 % von 12 500 = 2 000 Elektroautos (Schätzung).', 'Erst der Anteil, dann die Hochrechnung.'))
ST.knobel('hochrechnen', Z('In einem See werden 60 Fische markiert. Beim zweiten Fang sind von 50 Fischen 6 markiert; die 44 unmarkierten werden nun auch markiert. Beim dritten Fang sind von 40 Fischen 10 markiert. Wie viele Fische schätzt man nach dem dritten Fang?', 416, '(60 + 44) * 40 // 10',
          'Nach dem zweiten Fang sind 60 + 44 = 104 Fische markiert. Im dritten Fang ist jeder 4. markiert (10 von 40). Also ist vermutlich ein Viertel aller Fische markiert: 104 · 4 = 416.', 'Wie viele Fische sind vor dem dritten Fang markiert?'))
ST.knobel('hochrechnen', Z('Stichprobe A: 50 Kinder, davon 20 % mit Haustier. Stichprobe B: 150 Kinder, davon 30 % mit Haustier. Wie viel Prozent sind es in beiden Stichproben zusammen?', 27.5, '(10 + 45) * 100 / 200',
          'A: 10 Kinder, B: 45 Kinder. Zusammen 55 von 200 = 27,5 %. Der einfache Mittelwert 25 % ist falsch, weil B dreimal so groß ist.', 'Rechne mit Anzahlen, nicht mit Prozenten.', einheit='%'))

# repraesentativ
ST.stufenleiter('repraesentativ', 'Erkennen, ob eine Stichprobe zufällig ist und alle Gruppen abdeckt.',
                'Aus mehreren Auswahlen die beste wählen, Grund für eine Verzerrung nennen, Zusammensetzung einer Tabelle vergleichen.',
                'Große verzerrte gegen kleine zufällige Stichprobe abwägen, Hauptproblem einer Umfrage finden, verzerrte Kanäle erkennen, passende Zusammensetzung als Prüfungsaufgabe.')
ST.typ('repraesentativ', '/Ist die Stichprobe geeignet\\?$/', 'erkennen')
ST.typ('repraesentativ', '/Welche Auswahl ist am besten geeignet\\?$/', 'einkleidung')
ST.typ('repraesentativ', 'Um herauszufinden, wie viele Haushalte', 'umkehr')
ST.typ('repraesentativ', '/Welche ist aussagekräftiger\\?$/', 'begruenden')
ST.typ('repraesentativ', '/^Jemand befragt/', 'fehler')
ST.typ('repraesentativ', '/^(Die Schülerzeitung|Eine Umfrage zur Freizeit)/', 'transfer')
ST.neu('repraesentativ', 'direkt', A('Man will wissen, wie viele Kinder einer Schule ein Instrument spielen, und befragt nur die Kinder der Bläserklasse. Welche Gruppe ist zu stark vertreten?', 'Kinder, die ein Instrument spielen',
       ['Kinder, die kein Instrument spielen', 'Kinder der unteren Klassen', 'Keine, die Stichprobe passt.'], 'In der Bläserklasse spielt jedes Kind ein Instrument. Das Ergebnis wäre fast 100 % und viel zu hoch.', 'Was haben alle Befragten gemeinsam?'))
ST.neu('repraesentativ', 'darstellung', A('Die Grundgesamtheit besteht zu 50 % aus Mädchen und zu 50 % aus Jungen. Stichprobe A hat 48 % Mädchen, Stichprobe B 80 % Mädchen. Welche passt in der Zusammensetzung besser?', 'A',
       ['B', 'Beide gleich gut', 'Keine von beiden'], 'A weicht nur um 2 Prozentpunkte ab, B um 30. B ist bei dieser Eigenschaft verzerrt.', 'Vergleiche jede Stichprobe mit 50 %.'))
ST.neu('repraesentativ', 'pruefung', Z('In einer Stadt sind 40 % der Einwohner jünger als 30 Jahre. Eine Umfrage soll 200 Personen befragen und dabei die Altersgruppen richtig abbilden. Wie viele der Befragten sollten jünger als 30 sein?', 80, '200 * 40 // 100',
       '40 % von 200 = 80 Personen unter 30 und 120 Personen ab 30.', 'Die Stichprobe soll dieselben Anteile haben wie die Stadt.'))
ST.knobel('repraesentativ', Z('Eine Schule mit 800 Kindern hat 400 Mädchen. In einer Stichprobe von 40 Kindern sind 30 Mädchen. Wie viele Jungen muss man noch zusätzlich befragen, damit Mädchen und Jungen im richtigen Verhältnis vertreten sind?', 20, '30 - 10',
          'In der Schule ist die Hälfte Mädchen. In der Stichprobe gibt es 30 Mädchen und 10 Jungen. Für das Verhältnis 1 : 1 braucht man 30 Jungen, also 20 zusätzliche. Dann sind es 60 Befragte.', 'Welches Verhältnis gilt in der ganzen Schule?'))
ST.knobel('repraesentativ', Z('Bei einer Umfrage sind von 100 befragten Erwachsenen 60 % und von 100 befragten Jugendlichen 20 % dafür. In der Stadt leben dreimal so viele Erwachsene wie Jugendliche. Welcher Anteil der Stadt ist vermutlich dafür?', 50, '(3 * 60 + 20) // 4',
          'Stell dir 3 Erwachsene und 1 Jugendlichen vor: (3 · 60 % + 1 · 20 %) : 4 = 200 % : 4 = 50 %. Der einfache Mittelwert 40 % wäre falsch, weil die Stichprobe die Jugendlichen zu stark gewichtet.', 'Gewichte die Gruppen nach ihrer Größe in der Stadt.', einheit='%'))

# fehlerquellen
ST.stufenleiter('fehlerquellen', 'Eine Fehlerquelle benennen (suggestive Frage, zu klein, einseitig, nur Freiwillige) und eine Frage neutral stellen.',
                'Fehlerquellen in Umfragen von Sender, Zeitschrift und Verein, mehrere Fehler zugleich, passende Situation zu einer Fehlerquelle.',
                'Wirksamste Verbesserung wählen, mehrere Mängel finden, Wirkung einer größeren Stichprobe begründen, Werbeaussage prüfen, Bewertung einer ganzen Umfrage wie in einer Prüfung.')
ST.typ('fehlerquellen', 'Welche Frage ist neutral', 'erkennen')
ST.typ('fehlerquellen', '/^(Um herauszufinden, ob die Mitglieder ein neues Vereinsheim wollen, werden 200|Ein Radiosender will wissen, was seine Hörer zum Thema „Mehr|Eine Zeitschrift)/', 'einkleidung')
ST.typ('fehlerquellen', '/Welche Fehlerquelle liegt vor\\?$/', 'erkennen')
ST.typ('fehlerquellen', '/^(Um herauszufinden, ob die Fahrgäste|Um herauszufinden, wen).*wirksamsten/', 'transfer')
ST.typ('fehlerquellen', '/wirksamsten\\?$/', 'begruenden')
ST.typ('fehlerquellen', '/^(Ein Sportverein|Ein Hotel)/', 'fehler')
ST.typ('fehlerquellen', 'Die Schülerzeitung', 'begruenden')
ST.neu('fehlerquellen', 'direkt', A('Mache die Frage „Sie wollen doch sicher auch einen neuen Pausenhof?“ neutral. Welche Frage passt?', '„Soll es einen neuen Pausenhof geben?“',
       ['„Wer will denn keinen neuen Pausenhof?“', '„Sie finden den alten Pausenhof doch auch hässlich?“', '„Alle wollen einen neuen Pausenhof. Sie auch?“'],
       'Eine neutrale Frage enthält keine Wertung und legt keine Antwort nahe.', 'Welche Frage verrät nicht, was die Fragenden hören wollen?'))
ST.neu('fehlerquellen', 'umkehr', A('Bei welcher Umfrage tritt die Fehlerquelle „nur Freiwillige antworten“ auf?', 'Online-Aufruf: Jeder, der will, kann abstimmen.',
       ['Per Los gezogene Personen werden angerufen.', 'Jede zehnte Person der Liste wird besucht.', 'Alle Kinder einer Klasse füllen einen Bogen aus.'],
       'Bei einem offenen Aufruf entscheiden die Leute selbst, ob sie mitmachen. Es antworten vor allem die mit starker Meinung.', 'Wer entscheidet, wer antwortet?'))
ST.neu('fehlerquellen', 'mehrschritt', A('Eine Umfrage fragt nur 5 Kinder: „Ihr wollt doch auch längere Pausen?“ Welche zwei Fehlerquellen liegen vor?', 'Suggestive Frage und zu kleine Stichprobe',
       ['Nur Freiwillige und einseitige Auswahl', 'Suggestive Frage und nur Freiwillige', 'Zu kleine Stichprobe und einseitige Auswahl'],
       '„Ihr wollt doch auch …“ lenkt die Antwort (suggestiv). 5 Kinder sind zu wenige, um etwas über eine Schule zu sagen.', 'Prüfe die Frage und die Zahl der Befragten getrennt.'))
ST.neu('fehlerquellen', 'pruefung', A('Ein Fitnessstudio fragt 20 seiner Mitglieder: „Sport ist gesund – wie oft trainieren Sie pro Woche?“ und schreibt danach: „Die Deutschen trainieren viermal pro Woche.“ Welche Mängel hat die Umfrage?',
       'Einseitige Auswahl, viel zu klein und eine wertende Einleitung', ['Nur die Frage ist wertend.', 'Nur die Stichprobe ist zu klein.', 'Keine, Mitglieder wissen am besten Bescheid.'],
       'Mitglieder eines Studios trainieren mehr als andere (einseitig). 20 Personen sind für „die Deutschen“ viel zu wenige. „Sport ist gesund“ lenkt die Antwort.', 'Prüfe Auswahl, Größe und Frage.'))
ST.knobel('fehlerquellen', Z('Ein Brief geht an 1 000 Haushalte. 30 % antworten, davon sind 80 % zufrieden. Wie viele Haushalte haben geantwortet und sind zufrieden?', 240, '1000 * 30 // 100 * 80 // 100',
          '30 % von 1 000 = 300 Antworten, 80 % davon = 240 zufriedene. Über die 700 Haushalte ohne Antwort weiß man nichts – darum ist „80 % sind zufrieden“ nicht haltbar. Sicher ist nur: mindestens 24 % aller Haushalte sind zufrieden.',
          'Rechne Schritt für Schritt – und überlege, was über die anderen bekannt ist.'))
ST.knobel('fehlerquellen', Z('Um ehrliche Antworten zu bekommen, würfelt jeder Befragte heimlich: Bei einer 6 sagt er „ja“, sonst antwortet er ehrlich auf die Frage „Bist du schon einmal schwarzgefahren?“. 40 % sagen „ja“. Schätze den Anteil der Schwarzfahrer in Prozent.', 28, '(40 - 100 / 6) * 6 / 5',
          'Ein Sechstel sagt wegen der 6 „ja“ (≈ 16,7 %). Die übrigen fünf Sechstel antworten ehrlich: 5/6 · p = 40 % − 1/6 = 23,3 %. Also p = 23,3 % · 6/5 = 28 %. Niemand muss ehrlich zugeben, dass er schwarzgefahren ist.',
          'Wie viele „ja“ kommen allein durch die Würfel-6 zustande?', einheit='%'))

# aussagen
ST.stufenleiter('aussagen', 'Erkennen, dass ein Stichprobenergebnis ein Schätzwert ist und große Stichproben weniger schwanken.',
                'Anteile als Schätzwert formulieren, Spannweite und Prozentpunkte berechnen, Gewicht einer Person.',
                'Schlagzeilen beurteilen, knappe Ergebnisse abwägen, Fehlschluss bei kleinen Umfragen finden, mindestens nötige Anzahl rückwärts bestimmen, Prüfungsaufgabe mit zwei Umfragen.')
ST.typ('aussagen', '/^(Stichprobe A hat|Zwei kleine|In einer Zufallsstichprobe sagen 30)/', 'erkennen')
ST.typ('aussagen', 'In einer guten Zufallsstichprobe', 'einkleidung')
ST.typ('aussagen', '/^(Vier Gruppen|Klasse 7a)/', 'mehrschritt')
ST.typ('aussagen', '/^(Eine Zeitung schreibt|Ein Prospekt)/', 'begruenden')
ST.typ('aussagen', '/^(Bei einer guten Zufallsstichprobe|In einer guten Umfrage)/', 'transfer')
ST.typ('aussagen', 'Umfrage A:', 'fehler')
ST.typ('aussagen', '/^(Wie viele Personen muss man|In einer Stichprobe mit 50)/', 'rueckwaerts')
ST.neu('aussagen', 'direkt', Z('In einer Zufallsstichprobe von 200 Personen sagen 46 „ja“. Wie viel Prozent sind das?', 23, '46 * 100 / 200',
       '46 : 200 = 0,23 = 23 %. Das ist ein Schätzwert für die Grundgesamtheit.', 'Teil durch Ganzes.', einheit='%'))
ST.neu('aussagen', 'umkehr', Z('Bei einer Umfrage mit 80 Befragten: Wie viele Prozentpunkte macht eine einzelne Person aus?', 1.25, '100 / 80',
       '100 % : 80 = 1,25 %. Jede Person ändert das Ergebnis um 1,25 Prozentpunkte.', 'Verteile 100 % auf alle Befragten.'))
ST.neu('aussagen', 'pruefung', L('Zwei Zufallsumfragen zu „Soll der Pausenhof begrünt werden?“: Umfrage 1: 18 von 30 Kindern sagen ja. Umfrage 2: 330 von 600. a) Gib beide Anteile in % an. b) Um wie viele Prozentpunkte unterscheiden sie sich?',
       'a) □ % und □ %; b) □', [60, 55, 5], ['18 * 100 // 30', '330 * 100 // 600', '60 - 55'],
       'a) 18 : 30 = 60 %, 330 : 600 = 55 %. b) 5 Prozentpunkte. Umfrage 2 ist wegen ihrer Größe verlässlicher.', 'Erst die Anteile, dann die Differenz.'))
ST.knobel('aussagen', Z('Eine Umfrage meldet genau 37 % „ja“. Wie viele Personen müssen mindestens befragt worden sein?', 100, '100',
          '37 % = 37/100, und dieser Bruch lässt sich nicht kürzen (37 ist eine Primzahl). Also muss die Zahl der Befragten ein Vielfaches von 100 sein: mindestens 100.', 'Schreibe 37 % als Bruch und kürze, wenn möglich.'))
ST.knobel('aussagen', Z('Eine Umfrage meldet „gerundet 43 %“. Wie viele Personen wurden mindestens befragt?', 7, '7',
          'Gesucht ist ein Bruch k/n zwischen 42,5 % und 43,5 % mit kleinem n. n = 1 bis 6 liefert gerundet nur 0 %, 17 %, 20 %, 25 %, 33 %, 40 %, 50 %, 60 %, 67 %, 75 %, 80 %, 83 % und 100 %. Erst 3/7 ≈ 42,9 % passt. Also mindestens 7.',
          'Probiere n = 1, 2, 3, … und alle möglichen Anteile.'))


if __name__ == '__main__':
    d = bauen('daten.stichproben',
          'Grundgesamtheit und Stichprobe unterscheiden, von Stichproben hochrechnen und beurteilen, ob eine Stichprobe repräsentativ ist.',
          ['Grundgesamtheit: alle, über die man etwas wissen will. Stichprobe: die tatsächlich Befragten (Umfang n).',
           'Hochrechnen: Anteil in der Stichprobe mal Größe der Grundgesamtheit – ergibt nur eine Schätzung.',
           'Repräsentativ: zufällig ausgewählt und groß genug.',
           'Fehlerquellen: zu klein, einseitig, suggestive Frage, nur Freiwillige.'],
          [('Grundbegriffe', ['begriffe', 'hochrechnen']), ('Aussagekraft', ['repraesentativ', 'fehlerquellen', 'aussagen'])],
          ETAPPEN, GEN,
          offen=['Umfang laut Liste nur „Repräsentativität und Grenzen von Aussagen“ (RS 7); die Hochrechnung mit relativen Häufigkeiten wurde als üblicher Schulstoff ergänzt.'])
    umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
    durchsicht(d)
    stufen('daten.stichproben', ST)
