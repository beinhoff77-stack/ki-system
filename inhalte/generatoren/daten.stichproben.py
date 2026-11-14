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

SUGGESTIV = ['Sie sind doch sicher auch dafür, dass {x}?', 'Finden Sie nicht auch, dass {x}?', 'Jeder vernünftige Mensch ist dafür, dass {x}. Sie auch?']
SUG_X = ['die Pause länger wird', 'der Spielplatz erneuert wird', 'mehr Radwege gebaut werden', 'das Schwimmbad länger öffnet',
         'es in der Mensa mehr Gemüse gibt', 'der Bus öfter fährt']
FREI = ['Eine Zeitschrift ruft ihre Leser auf, im Internet zum Thema „{x}“ abzustimmen.', 'Ein Radiosender bittet Hörer, zum Thema „{x}“ anzurufen.',
        'An der Schultür hängt ein Zettel: Wer möchte, kann seine Meinung zum Thema „{x}“ in den Briefkasten werfen.']
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
            return auswahl(f'Um herauszufinden, {merk}, werden {n} Personen befragt: {a}. Warum ist das keine geeignete Stichprobe?',
                           gr[0].upper() + gr[1:] + '.', [x[0].upper() + x[1:] + '.' for x in R.sample(andere, 3)],
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
        txt = R.choice(FREI).format(x=x) + f' Es kommen {dz(R.choice([800, 1200, 3500, 9000]))} Antworten.'
        richtig = FEHLER_ART[3]
        w = 'Es antworten nur Freiwillige – meist Menschen mit einer starken Meinung. Die vielen Antworten ändern daran nichts.'
    if s == 3 and R.random() < 0.5:
        # Verbesserung vorschlagen
        bess = {0: 'Mehr Personen zufällig auswählen.', 1: 'Statt einer besonderen Gruppe Personen aus allen Gruppen zufällig auswählen.',
                2: 'Die Frage neutral stellen, ohne Wertung.', 3: 'Nicht auf Meldungen warten, sondern Personen per Los auswählen und gezielt ansprechen.'}
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

if __name__ == '__main__':
    bauen('daten.stichproben',
          'Grundgesamtheit und Stichprobe unterscheiden, von Stichproben hochrechnen und beurteilen, ob eine Stichprobe repräsentativ ist.',
          ['Grundgesamtheit: alle, über die man etwas wissen will. Stichprobe: die tatsächlich Befragten (Umfang n).',
           'Hochrechnen: Anteil in der Stichprobe mal Größe der Grundgesamtheit – ergibt nur eine Schätzung.',
           'Repräsentativ: zufällig ausgewählt und groß genug.',
           'Fehlerquellen: zu klein, einseitig, suggestive Frage, nur Freiwillige.'],
          [('Grundbegriffe', ['begriffe', 'hochrechnen']), ('Aussagekraft', ['repraesentativ', 'fehlerquellen', 'aussagen'])],
          ETAPPEN, GEN,
          offen=['Umfang laut Liste nur „Repräsentativität und Grenzen von Aussagen“ (RS 7); die Hochrechnung mit relativen Häufigkeiten wurde als üblicher Schulstoff ergänzt.'])
