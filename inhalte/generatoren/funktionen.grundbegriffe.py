#!/usr/bin/env python3
"""Thema funktionen.grundbegriffe – Zuordnung und Funktion (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, L, Z, baue, cz, einsetzen, ist_endlich, kl, lin, mit_bild, zt  # noqa: E402

META = {'thema_schluessel': 'funktionen.grundbegriffe', 'thema_id': 32, 'block_id': 73, 'klasse': {'gym_by': 8, 'rs_by': 8}}

ETAPPEN = [
    {'lernziel': 'eindeutig', 'titel': 'Ist die Zuordnung eine Funktion?',
     'regel': 'Eine ⟦Funktion⟧ ordnet ⟦jedem⟧ x-Wert ⟦genau einen⟧ y-Wert zu. Beispiel: Jedem Kind deiner Klasse wird sein Geburtstag zugeordnet – jedes Kind hat genau einen. Dass zwei Kinder am selben Tag Geburtstag haben, ist erlaubt.',
     'schritte': ['Zuordnung: (1 | 5), (2 | 7), (3 | 5). Prüfe: Kommt ein x-Wert zweimal vor?',
                  'Nein, 1, 2 und 3 kommen je einmal vor. Dass 1 und 3 beide den y-Wert 5 haben, stört nicht – wie zwei Kinder mit demselben Geburtstag.',
                  '⟦Es ist eine Funktion.⟧'],
     'fehler': '(2 | 4), (2 | 6) ist ⟦keine⟧ Funktion: Der x-Wert 2 hat zwei y-Werte – wie ein Kind mit zwei Geburtstagen. Umgekehrt ist (2 | 4), (3 | 4) eine Funktion: Zwei x-Werte dürfen denselben y-Wert haben.',
     'bild': {'typ': 'tabelle', 'kopf': ['x', '1', '2', '3'], 'zeilen': [['y', '5', '7', '5']]},
     '_verbot': ['(1 | 5), (2 | 7), (3 | 5)']},
    {'lernziel': 'mengen', 'titel': 'Definitionsmenge und Wertemenge',
     'regel': 'Die ⟦Definitionsmenge⟧ D enthält alle x, die man einsetzen darf. Die ⟦Wertemenge⟧ W enthält alle y-Werte, die dabei herauskommen. Verboten ist zum Beispiel alles, was einen ⟦Nenner 0⟧ macht – durch 0 kann man nicht teilen.',
     'schritte': ['f(x) = 2x + 1 mit D = {0; 1; 3}.', 'Setze alle x ein: f(0) = 1, f(1) = 3, f(3) = 7.', '⟦W = {1; 3; 7}⟧'],
     'fehler': 'Bei f(x) = 1/(x − 2) ist D nicht ℚ \\ {−2}. Verboten ist das x, für das der Nenner 0 wird: x − 2 = 0, also x = 2. Richtig: ⟦D = ℚ \\ {2}⟧. Probe: f(−2) = 1/(−4) geht problemlos.',
     '_verbot': ['D = {0; 1; 3}']},
    {'lernziel': 'funktionswert', 'titel': 'Funktionswerte berechnen',
     'regel': 'Der ⟦Funktionsterm⟧ f(x) sagt, wie man aus x den y-Wert berechnet. f(3) heißt: ⟦3 für x einsetzen⟧.',
     'schritte': ['f(x) = 2x² − 3, gesucht f(−2)', 'f(−2) = 2 · (−2)² − 3 = 2 · 4 − 3', '⟦f(−2) = 5⟧'],
     'fehler': 'f(−2) bei f(x) = 2x² − 3 ist nicht 2 · (−4) − 3 = −11: (−2)² = ⟦+4⟧. Negative Zahlen beim Einsetzen immer in Klammern setzen.',
     '_verbot': ['2x² − 3']},
    {'lernziel': 'stelle', 'titel': 'Zu einem y-Wert das x finden',
     'regel': 'Gesucht ist die ⟦Stelle⟧ x, an der f den Wert y hat. Dazu setzt du f(x) = y und ⟦löst die Gleichung⟧ nach x.',
     'schritte': ['f(x) = 3x − 4. Für welches x ist f(x) = 11?', '3x − 4 = 11 → 3x = 15', '⟦x = 5⟧'],
     'probe': 'f(5) = 15 − 4 = 11 ✓',
     'fehler': 'Bei „f(x) = 11“ ist nicht f(11) gesucht. 11 ist der ⟦y-Wert⟧, x ist unbekannt.',
     '_verbot': ['f(x) = 3x − 4']},
    {'lernziel': 'wertetabelle', 'titel': 'Wertetabellen lesen und ergänzen',
     'regel': 'In einer ⟦Wertetabelle⟧ steht oben x, unten f(x). Fehlende Werte berechnest du mit dem Term. Ohne Term suchst du eine ⟦Regel⟧, die zu allen Paaren passt.',
     'schritte': ['f(x) = 4 − x²', 'x = −1: 4 − 1 = 3; x = 0: 4; x = 3: 4 − 9 = −5', 'Tabelle: (−1 | 3), (0 | 4), (3 | ⟦−5⟧)'],
     'fehler': 'Einen Term nur an zwei Paaren prüfen. Tabelle (1 | 2), (2 | 4), (3 | 8): f(x) = 2x passt bei x = 1 und x = 2. Aber f(3) = 2 · 3 = 6, nicht 8. Ein Term passt nur, wenn er für ⟦alle⟧ Paare stimmt.',
     'bild': {'typ': 'tabelle', 'kopf': ['x', '−1', '0', '3'], 'zeilen': [['f(x) = 4 − x²', '3', '4', '−5']]},
     '_verbot': ['4 − x²']},
    {'lernziel': 'graph_lesen', 'titel': 'Werte am Graphen ablesen',
     'regel': 'Der ⟦Graph⟧ zeigt alle Paare (x | f(x)) auf einmal. f(4) ablesen: Bei x = 4 ⟦senkrecht⟧ bis zum Graphen gehen, dann ⟦waagrecht⟧ zur y-Achse. Umgekehrt findest du zu einem y-Wert die passenden x-Werte – manchmal mehrere.',
     'schritte': ['Der Graph gehört zu f(x) = 0,5x² − 2. Gesucht: f(4).', 'Von x = 4 senkrecht nach oben bis zum Graphen, dann waagrecht nach links: ⟦f(4) = 6⟧.',
                  'Umgekehrt: Wo ist f(x) = 6? Gehe bei y = 6 waagrecht – du triffst den Graphen ⟦zweimal⟧: bei x = 4 und bei x = −4.'],
     'probe': 'f(4) = 0,5 · 16 − 2 = 6 ✓ und f(−4) = 0,5 · 16 − 2 = 6 ✓',
     'fehler': 'Bei „Wo ist f(x) = 6?“ nur x = 4 angeben. Die waagrechte Linie bei y = 6 trifft die Parabel ⟦zweimal⟧. Suche immer die ganze Linie entlang.',
     'bild': {'typ': 'koordinaten', 'x': [-5, 5], 'y': [-3, 7], 'graphen': [{'art': 'poly', 'k': [-2, 0, 0.5], 'name': 'f'}], 'senkrecht': [4], 'waagrecht': [6],
              'punkte': [{'x': 4, 'y': 6, 'name': '(4 | 6)'}, {'x': -4, 'y': 6, 'name': '(−4 | 6)'}]}},
    {'lernziel': 'nullstellen', 'titel': 'Nullstellen berechnen',
     'regel': 'Eine ⟦Nullstelle⟧ ist ein x mit f(x) = 0. Dort schneidet der Graph die ⟦x-Achse⟧. Du findest sie, indem du ⟦f(x) = 0⟧ löst.',
     'schritte': ['f(x) = 2x − 7', '2x − 7 = 0 → 2x = 7', '⟦x = 3,5⟧'],
     'fehler': 'Die Nullstelle von f(x) = 2x − 7 ist nicht −7: f(0) = −7 ist der ⟦y-Achsenabschnitt⟧. Für die Nullstelle muss ⟦y = 0⟧ sein.',
     'bild': {'typ': 'koordinaten', 'x': [-1, 5], 'y': [-8, 3], 'graphen': [{'art': 'linear', 'm': 2, 't': -7, 'name': 'f'}],
              'punkte': [{'x': 3.5, 'y': 0, 'name': 'N(3,5 | 0)'}, {'x': 0, 'y': -7, 'name': '(0 | −7)'}]},
     '_verbot': ['2x − 7']},
    {'lernziel': 'punkt_graph', 'titel': 'Liegt der Punkt auf dem Graphen?',
     'regel': 'Ein Punkt P(a | b) liegt auf dem ⟦Graphen⟧ von f, wenn ⟦f(a) = b⟧ ist. Setze die x-Koordinate ein und vergleiche mit der y-Koordinate.',
     'schritte': ['f(x) = x² − 2x. Liegt P(3 | 3) auf dem Graphen?', 'Setze die x-Koordinate 3 ein: f(3) = 9 − 6 = 3.',
                  'Das ist genau die y-Koordinate von P: ⟦P liegt auf dem Graphen.⟧', 'Q(3 | 1) hat dieselbe x-Koordinate, aber f(3) = 3 ≠ 1: ⟦Q liegt nicht darauf⟧, sondern darunter.'],
     'fehler': 'Bei P(3 | 1) setzt man nicht die 1 für x ein. Die ⟦erste⟧ Koordinate ist x, die ⟦zweite⟧ ist y.',
     'bild': {'typ': 'koordinaten', 'x': [-2, 4], 'y': [-2, 5], 'graphen': [{'art': 'poly', 'k': [0, -2, 1], 'name': 'f'}],
              'punkte': [{'x': 3, 'y': 3, 'name': 'P'}, {'x': 3, 'y': 1, 'name': 'Q', 'offen': True}]},
     '_verbot': ['x² − 2x']},
]

# Verständliche Fassung (15.11., nach Rückmeldung von Eltern und Kind: „verstehen gar nichts“):
# Alltagssituation zuerst (einstieg), jedes neue Wort erklärt (woerter), Beispiel in kleinen Schritten, Merksatz am Ende (regel).
KLAR = {
 'eindeutig': {
  'einstieg': 'Stell dir einen Getränkeautomaten vor. Du drückst eine Taste und es kommt ein Getränk heraus. Taste 1 gibt immer Cola, Taste 2 immer Wasser, Taste 3 auch Cola. Egal wie oft du drückst: Dieselbe Taste liefert immer dasselbe Getränk. So ein verlässlicher Automat heißt in Mathe ⟦Funktion⟧.',
  'woerter': [['Zuordnung', 'Zu jeder Eingabe gehört eine Ausgabe – wie Taste → Getränk.'], ['x-Wert', 'die Eingabe (beim Automaten: die Taste)'], ['y-Wert', 'die Ausgabe (beim Automaten: das Getränk)'], ['(1 | 5)', 'kurz für: Eingabe 1 ergibt Ausgabe 5']],
  'bild': {'typ': 'tabelle', 'kopf': ['x (Eingabe)', '1', '2', '3'], 'zeilen': [['y (Ausgabe)', '5', '7', '5']]},
  'schritte': ['In der Tabelle steht oben die Eingabe x, unten die Ausgabe y: Zu 1 gehört 5, zu 2 gehört 7, zu 3 gehört 5.',
               'Frage: Steht eine Eingabe ⟦doppelt⟧ da – mit zwei verschiedenen Ausgaben? Nein. 1, 2 und 3 kommen oben je einmal vor.',
               'Die 5 steht unten zweimal. Das ist erlaubt – wie beim Automaten, bei dem zwei Tasten Cola geben.',
               'Also: ⟦Es ist eine Funktion.⟧'],
  'regel': 'Eine ⟦Funktion⟧ ist eine Zuordnung, bei der zu ⟦jeder Eingabe x genau eine Ausgabe y⟧ gehört. So prüfst du: Kommt ein x zweimal mit verschiedenen y vor? Dann ist es keine Funktion.',
  'fehler': '(2 | 4) und (2 | 6) zusammen: Die Eingabe 2 hätte zwei Ausgaben, 4 und 6 – wie eine Taste, die mal Cola und mal Wasser gibt. Das ist ⟦keine⟧ Funktion. Aber (2 | 4) und (3 | 4) ist in Ordnung: Zwei Eingaben dürfen dieselbe Ausgabe haben.'},
 'mengen': {
  'einstieg': 'Bleiben wir beim Automaten. Er hat nur bestimmte Tasten – nur die kannst du drücken. Und er hat nur bestimmte Getränke – nur die können herauskommen. Bei Funktionen ist es genauso: Es gibt Zahlen, die man hineingeben darf, und Zahlen, die herauskommen können.',
  'woerter': [['f(x) = 2x + 1', 'die Rechenvorschrift: Nimm die Eingabe x mal 2 und zähle 1 dazu.'], ['Definitionsmenge D', 'alle Zahlen, die man für x einsetzen darf (alle Tasten)'], ['Wertemenge W', 'alle Zahlen, die herauskommen (alle Getränke)'], ['{0; 1; 3}', 'Mengenklammer: nur die Zahlen 0, 1 und 3'], ['ℚ \\ {2}', 'alle Bruchzahlen außer der 2']],
  'schritte': ['Die Rechenvorschrift ist f(x) = 2x + 1. Erlaubt sind nur die Eingaben 0, 1 und 3, also D = {0; 1; 3}.',
               'Rechne jede Eingabe durch. 0 ergibt 2 · 0 + 1 = 1.', '1 ergibt 2 · 1 + 1 = 3. Und 3 ergibt 2 · 3 + 1 = 7.',
               'Herausgekommen sind 1, 3 und 7: ⟦W = {1; 3; 7}⟧'],
  'regel': '⟦Definitionsmenge D⟧: alles, was man einsetzen darf. ⟦Wertemenge W⟧: alles, was herauskommt. Nicht einsetzen darf man Zahlen, bei denen man ⟦durch 0 teilen⟧ müsste.',
  'fehler': 'Bei f(x) = 1/(x − 2) darf unter dem Bruchstrich keine 0 stehen. x − 2 wird 0, wenn x = 2 ist. Verboten ist also die ⟦2⟧ und nicht die −2: D = ℚ \\ {2}. Probe mit −2: 1/(−2 − 2) = 1/(−4), das geht.'},
 'funktionswert': {
  'einstieg': 'Eine Funktion ist wie eine Maschine mit fester Rechenvorschrift: Vorne gibst du eine Zahl hinein, hinten kommt das Ergebnis heraus. Beispiel Taxi: 3 € Grundpreis und 2 € für jeden Kilometer. Für 5 km zahlst du 2 · 5 + 3 = 13 €.',
  'woerter': [['f(x)', 'gelesen „f von x“: das Ergebnis der Maschine f, wenn man x hineingibt'], ['Funktionsterm', 'die Rechenvorschrift, zum Beispiel 2x + 3'], ['f(5)', 'das Ergebnis, wenn man 5 hineingibt'], ['Funktionswert', 'das Ergebnis, also der y-Wert']],
  'schritte': ['Das Taxi als Funktion: t(x) = 2x + 3. Gesucht ist t(5), der Preis für 5 km.',
               'Schreibe überall, wo x steht, eine 5 hin: t(5) = 2 · 5 + 3.', 'Ausrechnen: 10 + 3 = 13. Also ⟦t(5) = 13⟧.',
               'Mit einer negativen Zahl: g(x) = 2x² − 3, gesucht g(−2). Setze −2 in Klammern ein: 2 · (−2)² − 3 = 2 · 4 − 3 = ⟦5⟧.'],
  'regel': 'f(3) berechnen heißt: im Funktionsterm ⟦jedes x durch 3 ersetzen⟧ und ausrechnen. Negative Zahlen dabei ⟦in Klammern⟧ setzen.'},
 'stelle': {
  'einstieg': 'Jetzt geht es rückwärts. Beim Taxi kennst du diesmal den Preis und willst wissen, wie weit du gefahren bist: 13 € bezahlt – wie viele Kilometer waren das? Du kennst also das Ergebnis und suchst die Eingabe.',
  'woerter': [['Stelle', 'der x-Wert, also die Eingabe'], ['f(x) = 11', 'die Frage: Für welche Eingabe x kommt 11 heraus?']],
  'schritte': ['f(x) = 3x − 4. Für welches x kommt 11 heraus?', 'Schreibe die Rechenvorschrift hin und setze sie gleich 11: 3x − 4 = 11.',
               'Auf beiden Seiten 4 dazuzählen: 3x = 15.', 'Beide Seiten durch 3 teilen: ⟦x = 5⟧'],
  'regel': 'Ist das Ergebnis y gegeben und x gesucht: ⟦f(x) = y⟧ als Gleichung hinschreiben und ⟦nach x auflösen⟧.',
  'fehler': 'Bei „f(x) = 11“ nicht die 11 einsetzen! Die 11 ist das ⟦Ergebnis⟧ (y). Gesucht ist die Eingabe x.'},
 'wertetabelle': {
  'einstieg': 'Eine Wertetabelle ist wie eine Preisliste: Oben stehen die Eingaben, darunter die Ergebnisse. Beim Taxi: 1 km kostet 5 €, 2 km kosten 7 €, 3 km kosten 9 €. So siehst du viele Werte auf einen Blick.',
  'woerter': [['Wertetabelle', 'Tabelle mit x oben und dem Ergebnis f(x) darunter'], ['(3 | −5)', 'zu x = 3 gehört das Ergebnis −5']],
  'schritte': ['f(x) = 4 − x². Fülle die Tabelle für x = −1, 0 und 3.', 'x = −1: 4 − (−1)² = 4 − 1 = 3.', 'x = 0: 4 − 0 = 4.', 'x = 3: 4 − 3² = 4 − 9 = ⟦−5⟧'],
  'regel': 'In der ⟦Wertetabelle⟧ steht oben x, unten f(x). Fehlt ein Wert, rechnest du ihn mit dem Term aus. Fehlt der Term, suchst du eine ⟦Regel, die zu allen Spalten passt⟧.'},
 'graph_lesen': {
  'einstieg': 'Ein Graph ist das Bild einer Funktion. Du kennst das von der Wetter-App: Unten steht die Uhrzeit, links die Temperatur. Willst du wissen, wie warm es um 14 Uhr ist, gehst du bei 14 Uhr nach oben bis zur Kurve und dann nach links zur Temperatur.',
  'woerter': [['Graph', 'die Linie im Koordinatensystem; sie zeigt alle Paare (x | y) der Funktion'], ['x-Achse', 'die waagrechte Achse (Eingaben)'], ['y-Achse', 'die senkrechte Achse (Ergebnisse)']],
  'schritte': ['Gesucht ist f(4). Suche auf der x-Achse die 4.', 'Gehe von dort ⟦senkrecht⟧ nach oben, bis du die Kurve triffst.',
               'Gehe von diesem Punkt ⟦waagrecht⟧ nach links zur y-Achse. Dort steht 6, also ⟦f(4) = 6⟧.',
               'Rückwärts: Wo ist f(x) = 6? Gehe bei y = 6 waagrecht durch das ganze Bild. Du triffst die Kurve ⟦zweimal⟧: bei x = 4 und bei x = −4.'],
  'regel': 'f(a) ablesen: bei x = a ⟦senkrecht⟧ zur Kurve, dann ⟦waagrecht⟧ zur y-Achse. Zu einem y-Wert die x-Werte finden: waagrecht durchgehen – es kann ⟦mehrere⟧ Treffer geben.'},
 'nullstellen': {
  'einstieg': 'Du hast 7 € Schulden bei deiner Schwester und zahlst jede Woche 2 € zurück. Nach wie vielen Wochen stehst du genau bei 0 €? Dein Kontostand nach x Wochen ist f(x) = 2x − 7. Die Stelle, an der 0 herauskommt, heißt ⟦Nullstelle⟧.',
  'woerter': [['Nullstelle', 'ein x-Wert, bei dem 0 herauskommt: f(x) = 0'], ['im Bild', 'dort schneidet der Graph die x-Achse']],
  'schritte': ['f(x) = 2x − 7. Für welches x kommt 0 heraus?', 'Setze den Term gleich 0: 2x − 7 = 0.', 'Auf beiden Seiten 7 dazuzählen: 2x = 7.',
               'Durch 2 teilen: ⟦x = 3,5⟧. Nach dreieinhalb Wochen bist du schuldenfrei.'],
  'probe': 'f(3,5) = 2 · 3,5 − 7 = 0 ✓',
  'regel': '⟦Nullstelle⟧ berechnen: ⟦f(x) = 0⟧ hinschreiben und nach x auflösen. Im Bild ist das der Punkt, an dem der Graph die ⟦x-Achse⟧ schneidet.'},
 'punkt_graph': {
  'einstieg': 'Der Graph besteht aus lauter Punkten, die zur Funktion passen. Ob ein bestimmter Punkt dazugehört, musst du nicht zeichnen – du kannst es ausrechnen. Wie bei einer Preisliste: Passt „3 km kosten 9 €“ zum Tarif? Rechne nach.',
  'woerter': [['P(3 | 3)', 'Punkt mit x = 3 (erste Zahl) und y = 3 (zweite Zahl)'], ['Koordinaten', 'die beiden Zahlen eines Punktes: erst x, dann y']],
  'schritte': ['f(x) = x² − 2x. Liegt P(3 | 3) auf dem Graphen?', 'Die erste Zahl ist x. Setze 3 ein: f(3) = 3² − 2 · 3 = 9 − 6 = 3.',
               'Vergleiche mit der zweiten Zahl von P: auch 3. Passt, also ⟦P liegt auf dem Graphen.⟧', 'Q(3 | 1): f(3) ist 3 und nicht 1. ⟦Q liegt nicht auf dem Graphen.⟧'],
  'regel': 'Punkt P(a | b) prüfen: ⟦a in den Term einsetzen⟧. Kommt ⟦genau b⟧ heraus, liegt P auf dem Graphen – sonst nicht.'},
}
for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))


def nz(R, lo=-6, hi=6):
    return R.choice([k for k in range(lo, hi + 1) if k])


def quad(a, b, c):
    """a·x² + b·x + c als Text."""
    s = ''
    if a: s = ('−' if a < 0 else '') + ('' if abs(a) == 1 else zt(abs(a))) + 'x²'
    for k, v in ((b, 'x'), (c, '')):
        if not k: continue
        t = lin(k, 0) if v else zt(k)
        s = t if not s else s + (' − ' if k < 0 else ' + ') + t.lstrip('−')
    return s or '0'


def paare(ps):
    return ', '.join(f'({zt(x)} | {zt(y)})' for x, y in ps)


EIND = ['Ja, jedem x ist genau ein y zugeordnet.', 'Nein, einem x sind zwei verschiedene y zugeordnet.',
        'Nein, zwei verschiedene x haben denselben y-Wert.', 'Nein, die y-Werte müssen größer werden.']
SITUATIONEN = [
    ('Jedem Schüler einer Klasse wird sein Geburtsdatum zugeordnet.', True),
    ('Jedem Datum wird zugeordnet, welche Schüler einer Klasse an diesem Tag Geburtstag haben (einzeln aufgezählt).', False),
    ('Jeder Zahl wird ihr Quadrat zugeordnet.', True),
    ('Jeder positiven Zahl wird eine Zahl zugeordnet, deren Quadrat sie ist.', False),
    ('Jeder Uhrzeit eines Tages wird die an einem Ort gemessene Temperatur zugeordnet.', True),
    ('Jeder gemessenen Temperatur wird die Uhrzeit zugeordnet, zu der sie gemessen wurde.', False),
    ('Jedem Auto wird sein Kennzeichen zugeordnet.', True),
    ('Jeder Postleitzahl wird eine Straße in diesem Gebiet zugeordnet.', False),
    ('Jeder Menge Äpfel (in kg) wird ihr Preis bei festem Kilopreis zugeordnet.', True),
    ('Jedem Kreis wird sein Flächeninhalt zugeordnet.', True),
    ('Jedem Flächeninhalt wird ein Rechteck mit diesem Inhalt zugeordnet.', False),
    ('Jeder natürlichen Zahl wird einer ihrer Teiler zugeordnet.', False),
    ('Jeder natürlichen Zahl wird die Anzahl ihrer Teiler zugeordnet.', True),
    ('Jeder Person wird ihre Körpergröße am heutigen Tag zugeordnet.', True),
    ('Jeder Körpergröße wird eine Person mit dieser Größe zugeordnet.', False),
]


UMKEHR = [
    ('Jedem Schüler wird sein Geburtstag zugeordnet. Und umgekehrt: Jedem Geburtstag wird ein Schüler zugeordnet.', 'Die erste ist eine Funktion, die zweite nicht.',
     'Jeder Schüler hat genau einen Geburtstag. Aber an einem Tag können mehrere Schüler Geburtstag haben (oder keiner).'),
    ('Jedem Auto wird sein Kennzeichen zugeordnet. Und umgekehrt: Jedem Kennzeichen wird sein Auto zugeordnet.', 'Beide sind Funktionen.',
     'Jedes Auto hat genau ein Kennzeichen, und jedes vergebene Kennzeichen gehört zu genau einem Auto.'),
    ('Jeder Zahl wird ihr Quadrat zugeordnet. Und umgekehrt: Jeder Quadratzahl wird eine Zahl zugeordnet, deren Quadrat sie ist.', 'Die erste ist eine Funktion, die zweite nicht.',
     'Jede Zahl hat genau ein Quadrat. Aber zu 9 gehören 3 und −3 – zwei Werte.'),
    ('Jedem Menschen wird seine Mutter zugeordnet. Und umgekehrt: Jeder Mutter wird ihr Kind zugeordnet.', 'Die erste ist eine Funktion, die zweite nicht.',
     'Jeder Mensch hat genau eine (leibliche) Mutter. Eine Mutter kann aber mehrere Kinder haben.'),
]
UMK_OPT = ['Die erste ist eine Funktion, die zweite nicht.', 'Beide sind Funktionen.', 'Keine ist eine Funktion.', 'Die zweite ist eine Funktion, die erste nicht.']


def g_eindeutig(R, st):
    if st >= 2 and R.random() < .25:
        t, ri, w = R.choice(UMKEHR)
        return A(R, f'{t} Welche Zuordnungen sind Funktionen?', ri, [o for o in UMK_OPT if o != ri], w,
                 'Prüfe jede Richtung einzeln: Gibt es zu einem Ausgangswert genau einen zugeordneten Wert?')
    if st >= 2 and R.random() < .3:
        # Punkte im Koordinatensystem
        if R.random() < .5:
            xs = R.sample(range(-3, 5), 4)
            ps = [(x, R.randint(-3, 4)) for x in xs]
            doppel = R.random() < .6
            if doppel:
                y2 = ps[0][1] + R.choice([-3, -2, 2, 3])
                ps.append((ps[0][0], y2))
            gr = {'typ': 'koordinaten', 'x': [-4, 5], 'y': [-6, 7], 'punkte': [{'x': x, 'y': y} for x, y in ps], 'streckung': 1}
            ri = (f'Nein, bei x = {zt(ps[0][0])} liegen zwei Punkte übereinander.' if doppel else 'Ja, über jedem x liegt höchstens ein Punkt.')
            fa = ['Ja, alle Punkte liegen im Bild.', 'Nein, zwei Punkte haben denselben y-Wert.' if not doppel else 'Ja, über jedem x liegt höchstens ein Punkt.',
                  'Ja, kein y kommt doppelt vor.' if doppel else f'Nein, bei x = {zt(ps[0][0])} liegen zwei Punkte übereinander.']
            return mit_bild(A(R, 'Können diese Punkte zum Graphen einer Funktion gehören?', ri, fa,
                              'Eine senkrechte Linie darf höchstens einen Punkt treffen. ' + ('Bei x = ' + zt(ps[0][0]) + ' trifft sie zwei.' if doppel else 'Das ist hier überall so.'),
                              'Ziehe in Gedanken senkrechte Linien durch die Punkte.'), gr)
        a = R.choice([1, -1, Fr(1, 2)]); c = R.randint(-2, 2)
        gr = {'typ': 'koordinaten', 'x': [-4, 4], 'y': [-5, 6], 'graphen': [{'art': 'poly', 'k': [c, 0, float(a) if Fr(a).denominator != 1 else int(a)], 'name': 'f'}]}
        return mit_bild(A(R, 'Ist der gezeichnete Graph der Graph einer Funktion?', 'Ja, jede senkrechte Linie trifft den Graphen höchstens einmal.',
                          ['Nein, zwei verschiedene x haben denselben y-Wert.', 'Nein, der Graph ist keine Gerade.', 'Das kann man ohne Term nicht entscheiden.'],
                          'Senkrechte-Linie-Test: Über jedem x liegt genau ein Punkt des Graphen. Dass links und rechts gleiche y-Werte vorkommen, ist erlaubt.',
                          'Ziehe in Gedanken senkrechte Linien durch das Bild.'), gr)
    if st == 2 and R.random() < .5:
        sit, ok = R.choice(SITUATIONEN)
        r = 'Ja, das ist eine Funktion.' if ok else 'Nein, das ist keine Funktion.'
        return A(R, f'Ist diese Zuordnung eine Funktion? {sit}', r,
                 ['Nein, das ist keine Funktion.' if ok else 'Ja, das ist eine Funktion.', 'Das kann man ohne Zahlen nicht entscheiden.'],
                 'Jedem Ausgangswert ist genau ein Wert zugeordnet.' if ok else 'Zu einem Ausgangswert kann es mehrere zugeordnete Werte geben (oder keinen).',
                 'Frage dich: Kann es zu einem Ausgangswert zwei verschiedene Ergebnisse geben?')
    n = R.randint(4, 6)
    xs = R.sample(range(-6, 10), n)
    ys = [R.randint(-5, 9) for _ in xs]
    art = R.choice(['ok', 'doppel_y', 'doppel_x']) if st == 1 else R.choice(['ok', 'doppel_y', 'doppel_x', 'doppel_y'])
    if art == 'doppel_y':
        ys[1] = ys[0]
    ps = list(zip(xs, ys))
    if art == 'doppel_x':
        x0 = xs[0]; ps.append((x0, ys[0] + R.choice([1, 2, -3])))
    R.shuffle(ps)
    if st == 3:
        # vier Zuordnungen, eine ist keine Funktion
        listen = []
        for k in range(4):
            xs = R.sample(range(-5, 9), 4); ys = [R.randint(-4, 8) for _ in xs]
            if k == 1: ys[1] = ys[0]
            ps2 = list(zip(xs, ys))
            if k == 0: ps2.append((xs[2], ys[2] + R.choice([1, -2])))
            R.shuffle(ps2)
            listen.append(paare(ps2))
        return A(R, 'Welche Zuordnung ist KEINE Funktion?', listen[0], listen[1:],
                 f'Bei {listen[0]} kommt ein x-Wert zweimal mit verschiedenen y-Werten vor. Gleiche y-Werte bei verschiedenen x sind erlaubt.',
                 'Suche einen x-Wert, der zweimal vorkommt.')
    r = EIND[1] if art == 'doppel_x' else EIND[0]
    return A(R, f'Ist die Zuordnung {paare(ps)} eine Funktion?', r, [e for e in EIND if e != r],
             'Ein x-Wert hat zwei y-Werte – keine Funktion.' if art == 'doppel_x' else 'Jeder x-Wert kommt nur einmal vor – also Funktion (gleiche y-Werte sind erlaubt).',
             'Schau nur auf die x-Werte: Kommt einer doppelt vor?')


def zufall_f(R, st):
    """(Text, Funktion) – lineare, quadratische oder Bruch-Funktion."""
    art = R.choice({1: ['lin'], 2: ['lin', 'quad', 'quad'], 3: ['quad', 'bruch', 'lin_dez']}[st])
    if art == 'lin':
        m, t = nz(R, -6, 6), R.randint(-9, 9)
        return lin(m, t), (lambda x: m * x + t), f'({m}) * ({{x}}) + ({t})'
    if art == 'lin_dez':
        m, t = Fr(nz(R, -9, 9), R.choice([2, 4, 5])), Fr(R.randint(-20, 20), 2)
        return lin(m, t), (lambda x: m * x + t), f'{cz(m)} * ({{x}}) + {cz(t)}'
    if art == 'quad':
        a, b, c = nz(R, -3, 3), R.randint(-5, 5), R.randint(-9, 9)
        return quad(a, b, c), (lambda x: a * x * x + b * x + c), f'({a}) * ({{x}})**2 + ({b}) * ({{x}}) + ({c})'
    a, b = nz(R, -12, 12), nz(R, -5, 5)
    return f'{zt(a)}/({lin(1, b)})', (lambda x: Fr(a) / (x + b)), f'{a} / (({{x}}) + ({b}))'


NULL = {'n': 0}


def g_funktionswert(R, st):
    while True:
        txt, f, c = zufall_f(R, st)
        x = Fr(R.randint(-6, 6))
        if x == 0 and NULL['n'] >= 2: continue
        if st == 3 and R.random() < .4: x = Fr(R.choice([-5, -3, -1, 1, 3, 5]), 2)
        try: y = f(x)
        except ZeroDivisionError: continue
        if ist_endlich(y) and len(zt(y)) <= 7: break
    if x == 0: NULL['n'] += 1
    return Z(f'Berechne f({zt(x)}) für f(x) = {txt}.', y, c.format(x=cz(x)),
             f'x = {zt(x)} einsetzen: f({zt(x)}) = {einsetzen(txt, x)} = {zt(y)}.',
             'Setze die Zahl für jedes x ein. Negative Zahlen in Klammern!')


def weg_lin(m, t, y, x):
    """Lösungsweg m·x + t = y ohne Leerschritte."""
    teile = [f'{lin(m, t)} = {zt(y)}']
    if t: teile.append(f'{lin(m, 0)} = {zt(y - t)}')
    if m != 1: teile.append(f'x = {zt(x)}')
    w = ' → '.join(dict.fromkeys(teile)) + '.'
    return w if len(teile) > 1 else f'Ansatz f(x) = {zt(y)}: {w} Probe: f({zt(x)}) = {zt(y)} ✓'


def g_stelle(R, st):
    art = R.choice({1: ['lin', 'lin', 'klammer'], 2: ['lin', 'klammer', 'quad_keine', 'bruch'], 3: ['bruch', 'lin', 'quad_keine', 'konstant']}[st])
    if art == 'quad_keine':
        c, y = R.randint(1, 9), None
        y = c - R.randint(1, 6)
        r = f'Für kein x: x² + {c} ist mindestens {c}.'
        return A(R, f'Für welches x gilt f(x) = {zt(y)}, wenn f(x) = x² + {c}?', r,
                 [f'x = {zt(y - c)}', f'x = {zt(c - y)}', f'Für jedes x.'],
                 f'x² ist nie negativ, also ist x² + {c} ≥ {c}. Der Wert {zt(y)} ist kleiner als {c} und wird nie erreicht.',
                 'Wie klein kann x² + eine positive Zahl werden?')
    if art == 'konstant':
        c = R.randint(-6, 9); y = c if R.random() < .5 else c + R.choice([-2, 1, 3])
        r = 'Für jedes x.' if y == c else 'Für kein x.'
        return A(R, f'Für welches x gilt f(x) = {zt(y)}, wenn f(x) = {zt(c)}?', r,
                 ['Für jedes x.' if y != c else 'Für kein x.', f'x = {zt(y)}', 'x = 0'],
                 f'f hat immer den Wert {zt(c)}. ' + ('Also gilt f(x) = ' + zt(y) + ' für jedes x.' if y == c else f'Der Wert {zt(y)} kommt nie vor.'),
                 'Hängt f(x) überhaupt von x ab?')
    if art == 'bruch':
        while True:
            a, y = nz(R, -24, 24), R.choice([k for k in range(-8, 9) if k not in (0, 1, -1)])
            x = Fr(a, y)
            if ist_endlich(x) and len(zt(x)) <= 5: break
        return Z(f'Für welches x ist f(x) = {zt(y)}, wenn f(x) = {zt(a)}/x?', x, f'{a} / ({y})',
                 f'{zt(a)}/x = {zt(y)} | · x → {zt(a)} = {zt(y)}x | : {kl(y)} → x = {zt(x)}.', 'Multipliziere mit x, dann teile.')
    if art == 'klammer':
        k, p = nz(R, -4, 5), R.randint(-6, 6)
        x = Fr(R.randint(-6, 8)); y = k * (x - p)
        if k == 1 or p == 0: return g_stelle(R, st)
        return Z(f'Für welches x gilt f(x) = {zt(y)}, wenn f(x) = {zt(k)}(x {"−" if p > 0 else "+"} {abs(p)})?', x, f'{cz(y)} / ({k}) + ({p})',
                 f'{zt(k)}(x {"−" if p > 0 else "+"} {abs(p)}) = {zt(y)} | : {kl(k)} → x {"−" if p > 0 else "+"} {abs(p)} = {zt(Fr(y, k))} → x = {zt(x)}.',
                 'Teile zuerst durch die Zahl vor der Klammer.')
    while True:
        m = Fr(nz(R, -6, 6)) if st < 3 else Fr(nz(R, -9, 9), R.choice([1, 2, 4]))
        t = Fr(R.randint(-9, 9))
        x = Fr(R.randint(-8, 9)) if st == 1 else Fr(R.randint(-16, 16), R.choice([1, 2]))
        y = m * x + t
        if m != 0 and (m, t) != (1, 0) and ist_endlich(y) and len(zt(y)) <= 6: break
    return Z(f'Für welches x gilt f(x) = {zt(y)}, wenn f(x) = {lin(m, t)}?', x, f'({cz(y)} - ({cz(t)})) / {cz(m)}',
             weg_lin(m, t, y, x), 'Setze den Term gleich dem y-Wert und löse nach x.')


def g_wertetabelle(R, st):
    if st == 3:
        m, t = nz(R, -5, 5), R.randint(-6, 6)
        xs = sorted(R.sample(range(-3, 5), 3))
        ps = [(x, m * x + t) for x in xs]
        richtig = lin(m, t)
        falsch = [lin(-m, t), lin(m, -t) if t else lin(m, 1), lin(t, m) if t and t != m else lin(m + 1, t), lin(m, ps[0][1] - m * xs[0] + 1)]
        # falsche Terme dürfen nicht zu allen Paaren passen
        falsch = [f for f, (mm, tt) in zip(falsch, [(-m, t), (m, -t if t else 1), (t, m) if t and t != m else (m + 1, t), (m, ps[0][1] - m * xs[0] + 1)])
                  if any(mm * x + tt != y for x, y in ps)]
        return A(R, f'Welcher Funktionsterm passt zur Wertetabelle {paare(ps)}?', f'f(x) = {richtig}', [f'f(x) = {f}' for f in falsch],
                 f'Probe: ' + '; '.join(f'f({zt(x)}) = {zt(y)}' for x, y in ps) + '. Nur f(x) = ' + richtig + ' passt zu allen Paaren.',
                 'Setze die x-Werte in jeden Term ein. Der richtige Term passt zu allen Paaren.')
    txt, f, c = zufall_f(R, 2 if st == 2 else 1)
    xs = sorted(R.sample(range(-4, 6), 4))
    try: ps = [(x, f(Fr(x))) for x in xs]
    except ZeroDivisionError: return g_wertetabelle(R, st)
    if any(not ist_endlich(y) for _, y in ps): return g_wertetabelle(R, st)
    k = R.randrange(4)
    if st == 2 and 'x²' not in txt and R.random() < .5:
        # fehlender x-Wert bei linearer Funktion
        x0, y0 = ps[k]
        tab = ', '.join(f'({zt(x)} | {zt(y)})' if i != k else f'(□ | {zt(y)})' for i, (x, y) in enumerate(ps))
        m = (ps[1][1] - ps[0][1]) / (xs[1] - xs[0]); t = ps[0][1] - m * xs[0]
        return Z(f'Wertetabelle zu f(x) = {txt}: {tab}. Welcher x-Wert fehlt?', x0, f'({cz(y0)} - ({cz(t)})) / {cz(m)}',
                 f'{txt} = {zt(y0)} lösen: x = {zt(x0)}.', 'Setze f(x) gleich dem y-Wert und löse nach x.')
    x0, y0 = ps[k]
    if R.random() < .5:
        gr = {'typ': 'tabelle', 'kopf': ['x'] + [zt(x) for x in xs], 'zeilen': [['f(x)'] + [zt(y) if i != k else '?' for i, (x, y) in enumerate(ps)]]}
        return mit_bild(Z(f'Die Tabelle gehört zu f(x) = {txt}. Welcher Wert gehört an die Stelle „?“?', y0, c.format(x=x0),
                          f'x = {zt(x0)} einsetzen: f({zt(x0)}) = {einsetzen(txt, x0)} = {zt(y0)}.', 'Setze den x-Wert über dem „?“ in den Term ein.'), gr)
    tab = ', '.join(f'({zt(x)} | {zt(y)})' if i != k else f'({zt(x)} | □)' for i, (x, y) in enumerate(ps))
    return Z(f'Wertetabelle zu f(x) = {txt}: {tab}. Welcher y-Wert fehlt?', y0, c.format(x=x0),
             f'x = {zt(x0)} einsetzen: f({zt(x0)}) = {einsetzen(txt, x0)} = {zt(y0)}.', 'Setze den x-Wert in den Term ein.')


def mengentext(xs):
    return '{' + '; '.join(zt(x) for x in sorted(set(xs))) + '}'


def g_mengen(R, st):
    if st == 1:
        b = nz(R, -9, 9); a = nz(R, -9, 9)
        return A(R, f'Gib die maximale Definitionsmenge von f(x) = {zt(a)}/({lin(1, -b)}) an.', f'D = ℚ \\ {{{zt(b)}}}',
                 [f'D = ℚ \\ {{{zt(-b)}}}', 'D = ℚ', f'D = ℚ \\ {{{zt(a)}}}' if a not in (b, -b) else 'D = ℚ \\ {0}'],
                 f'Der Nenner {lin(1, -b)} ist 0 für x = {zt(b)}. Diese Zahl muss raus.', 'Welche Zahl macht den Nenner 0?')
    if st == 2:
        txt, f, _ = zufall_f(R, 2)
        if '/' in txt: return g_mengen(R, st)
        D = sorted(R.sample(range(-3, 4), R.randint(3, 4)))
        W = [f(Fr(x)) for x in D]
        falsch = [mengentext(D), mengentext([w + 1 for w in W]), mengentext([-w for w in W]) if any(W) else mengentext([1, 2])]
        return A(R, f'f(x) = {txt} mit D = {mengentext(D)}. Gib die Wertemenge W an.', 'W = ' + mengentext(W), ['W = ' + s for s in falsch],
                 'Funktionswerte: ' + ', '.join(f'f({zt(x)}) = {zt(w)}' for x, w in zip(D, W)) + f'. W = {mengentext(W)}.',
                 'Berechne für jedes x aus D den Funktionswert. Gleiche Werte schreibt man nur einmal.')
    art = R.choice(['quadrat', 'betrag', 'konst', 'bruch2'])
    c = R.randint(-6, 6)
    if art == 'quadrat':
        r = f'Kein Funktionswert ist kleiner als {zt(c)}.'
        return A(R, f'f(x) = x² {"+" if c >= 0 else "−"} {abs(c)} mit D = ℚ. Welche Aussage über die Funktionswerte stimmt?', r,
                 [f'Kein Funktionswert ist größer als {zt(c)}.', 'Jede Zahl kommt als Funktionswert vor.', f'Der kleinste Funktionswert ist {zt(c + 1)}.'],
                 f'x² ist nie negativ, kleinster Wert 0 (bei x = 0). Also f(x) ≥ {zt(c)}; der kleinste Wert {zt(c)} wird bei x = 0 erreicht.',
                 'Welchen kleinsten Wert kann x² annehmen?')
    if art == 'konst':
        return A(R, f'f(x) = {zt(c)} mit D = ℚ. Welche Wertemenge hat f?', f'W = {{{zt(c)}}}', ['W = ℚ', f'W = ℚ \\ {{{zt(c)}}}', 'W = {0}' if c else 'W = {1}'],
                 f'Jedem x wird derselbe Wert {zt(c)} zugeordnet. Also W = {{{zt(c)}}}.', 'Welche y-Werte können überhaupt herauskommen?')
    if art == 'bruch2':
        a, b = R.sample([k for k in range(-6, 7) if k], 2)
        return A(R, f'Gib die maximale Definitionsmenge von f(x) = 1/(({lin(1, -a)})({lin(1, -b)})) an.', f'D = ℚ \\ {mengentext([a, b])}',
                 [f'D = ℚ \\ {mengentext([-a, -b])}', f'D = ℚ \\ {{{zt(a)}}}', 'D = ℚ'],
                 f'Der Nenner ist 0 für x = {zt(a)} und für x = {zt(b)}.', 'Ein Produkt ist 0, wenn einer der Faktoren 0 ist.')
    return A(R, f'f(x) = −x² {"+" if c >= 0 else "−"} {abs(c)} mit D = ℚ. Welche Aussage über die Funktionswerte stimmt?', f'Kein Funktionswert ist größer als {zt(c)}.',
             [f'Kein Funktionswert ist kleiner als {zt(c)}.', 'Jede Zahl kommt als Funktionswert vor.', 'Der größte Funktionswert ist 0.' if c else 'Der größte Funktionswert ist 1.'],
             f'−x² ist nie positiv, größter Wert 0 (bei x = 0). Also f(x) ≤ {zt(c)}.', 'Welchen größten Wert kann −x² annehmen?')


def g_nullstellen(R, st):
    if st == 1 or (st == 2 and R.random() < .5):
        while True:
            m = Fr(nz(R, -8, 8)); x0 = Fr(R.randint(-9, 9)) if st == 1 else Fr(R.randint(-20, 20), R.choice([2, 4, 5]))
            t = -m * x0
            if ist_endlich(x0) and t.denominator == 1: break
        return Z(f'Berechne die Nullstelle von f(x) = {lin(m, t)}.', x0, f'-({cz(t)}) / {cz(m)}',
                 weg_lin(m, t, 0, x0), 'Setze f(x) = 0 und löse nach x.')
    if st >= 2 and R.random() < .3:
        if R.random() < .6:
            c = R.randint(1, 9)
            return A(R, f'Welche Nullstellen hat f(x) = x² + {c}?', 'keine', [f'x = {zt(-c)}', f'x = 0', f'x = {zt(-c)} und x = {zt(c)}'],
                     f'x² ist nie negativ, also ist x² + {c} ≥ {c} > 0. Der Graph liegt ganz über der x-Achse: keine Nullstelle.',
                     'Kann x² + eine positive Zahl 0 werden?')
        c = nz(R, -9, 9)
        return A(R, f'Welche Nullstellen hat f(x) = {zt(c)}?', 'keine', [f'x = {zt(c)}', 'x = 0', 'jede Zahl'],
                 f'f hat immer den Wert {zt(c)} ≠ 0. Der Graph ist eine waagrechte Gerade, die die x-Achse nicht trifft.',
                 'Wann ist f(x) = 0?')
    if st == 2:
        a, b = R.sample([k for k in range(-7, 8) if k], 2)
        r = f'x = {zt(min(a, b))} und x = {zt(max(a, b))}'
        return A(R, f'Welche Nullstellen hat f(x) = ({lin(1, -a)})({lin(1, -b)})?', r,
                 [f'x = {zt(min(-a, -b))} und x = {zt(max(-a, -b))}', f'x = {zt(a * b)}', f'x = {zt(-a)} und x = {zt(b)}' if -a != b else 'keine Nullstelle'],
                 f'Ein Produkt ist 0, wenn ein Faktor 0 ist: {lin(1, -a)} = 0 → x = {zt(a)}; {lin(1, -b)} = 0 → x = {zt(b)}.',
                 'Wann ist ein Produkt gleich 0?')
    while True:
        a, b, c = nz(R, -6, 6), R.randint(-12, 12), nz(R, -6, 6)
        x0 = Fr(-b, a)
        if x0 != c and ist_endlich(x0) and len(zt(x0)) <= 5 and b: break
    if R.random() < .5:
        return Z(f'Berechne die Nullstelle von f(x) = ({lin(a, b)})/({lin(1, -c)}).', x0, f'-({b}) / ({a})',
                 f'Ein Bruch ist 0, wenn der Zähler 0 ist (und der Nenner nicht): {lin(a, b)} = 0 → x = {zt(x0)}. Nenner dort: {zt(x0 - c)} ≠ 0.',
                 'Ein Bruch ist 0, wenn sein Zähler 0 ist.')
    a, b = nz(R, -5, 5), nz(R, -12, 12)
    x1 = Fr(-b, a)
    if not ist_endlich(x1) or len(zt(x1)) > 5: return g_nullstellen(R, st)
    r = f'x = 0 und x = {zt(x1)}'
    return A(R, f'Welche Nullstellen hat f(x) = x({lin(a, b)})?', r, [f'nur x = {zt(x1)}', f'x = 0 und x = {zt(-x1)}', f'x = 0 und x = {zt(b)}' if b != x1 else 'nur x = 0'],
             f'x = 0 oder {lin(a, b)} = 0 → x = {zt(x1)}.', 'Ein Produkt ist 0, wenn einer der Faktoren 0 ist. Vergiss den Faktor x nicht.')


def g_punkt_graph(R, st):
    if st == 3:
        while True:
            a, k = nz(R, -5, 6), Fr(nz(R, -6, 6), R.choice([1, 1, 2]))
            t = R.randint(-6, 6)
            b = k * a + t
            if b.denominator == 1: break
        return Z(f'Der Punkt P({zt(a)} | {zt(b)}) liegt auf dem Graphen von f(x) = k · x {"+" if t >= 0 else "−"} {abs(t)}. Bestimme k.', k, f'({cz(b)} - ({t})) / ({a})',
                 f'f({zt(a)}) = {zt(b)}: k · {kl(a)} {"+" if t >= 0 else "−"} {abs(t)} = {zt(b)} → k · {kl(a)} = {zt(b - t)} → k = {zt(k)}.',
                 'Setze die Koordinaten von P in die Gleichung y = f(x) ein und löse nach k.')
    if st == 2 and R.random() < .35:
        # Ablesen am Graphen
        m, t = R.choice([Fr(1, 2), 1, 2, -1, Fr(-1, 2), 3]), R.randint(-3, 3)
        while True:
            x0 = R.randint(-4, 4)
            y0 = m * x0 + t
            if y0.denominator == 1 if isinstance(y0, Fr) else True: break
        gr = {'typ': 'koordinaten', 'x': [-5, 5], 'y': [-6, 6], 'graphen': [{'art': 'linear', 'm': float(m) if Fr(m).denominator != 1 else int(m), 't': t, 'name': 'f'}]}
        if R.random() < .5:
            return mit_bild(Z(f'Lies am Graphen ab: f({zt(x0)}) = ?', y0, f'{cz(Fr(m))} * ({x0}) + ({t})',
                              f'Bei x = {zt(x0)} senkrecht zum Graphen, dann waagrecht zur y-Achse: f({zt(x0)}) = {zt(y0)}.', 'Erst senkrecht zum Graphen, dann waagrecht zur y-Achse.'), gr)
        return mit_bild(Z(f'An welcher Stelle x hat der Graph den Wert {zt(y0)}?', x0, f'({cz(Fr(y0))} - ({t})) / {cz(Fr(m))}',
                          f'Bei y = {zt(y0)} waagrecht zum Graphen, dann senkrecht zur x-Achse: x = {zt(x0)}.', 'Erst waagrecht zum Graphen, dann senkrecht zur x-Achse.'), gr)
    txt, f, _ = zufall_f(R, st)
    if '/' in txt: return g_punkt_graph(R, st)
    while True:
        x = Fr(R.randint(-4, 5)); y = f(x)
        if y != x and abs(y) < 60: break
    richtig = f'P({zt(x)} | {zt(y)})'
    kand = [(y, x), (x, y + R.choice([1, -1, 2])), (-x, y), (x + 1, y), (x, -y), (x, y - 3)]
    falsch = []
    for p_, q_ in kand:      # jeden Ablenker mit f nachprüfen
        try:
            if f(Fr(p_)) == q_: continue
        except ZeroDivisionError:
            pass
        t_ = f'P({zt(p_)} | {zt(q_)})'
        if t_ != richtig and t_ not in falsch: falsch.append(t_)
    return A(R, f'Welcher Punkt liegt auf dem Graphen von f(x) = {txt}?', richtig, falsch,
             f'f({zt(x)}) = {zt(y)}, also liegt {richtig} auf dem Graphen.', 'Setze die x-Koordinate ein und vergleiche mit der y-Koordinate.')


def g_graph_lesen(R, st):
    art = R.choice(['lin', 'quad']) if st >= 2 else 'lin'
    if art == 'lin':
        m, t = R.choice([Fr(1, 2), 1, 2, -1, Fr(-1, 2), -2]), R.randint(-3, 3)
        f = lambda x: m * x + t
        g = {'art': 'linear', 'm': float(m) if Fr(m).denominator != 1 else int(m), 't': t, 'name': 'f'}
        name = lin(m, t)
    else:
        a, c = R.choice([Fr(1, 2), 1, -1, Fr(-1, 2)]), R.randint(-3, 3)
        f = lambda x: a * x * x + c
        g = {'art': 'poly', 'k': [c, 0, float(a) if Fr(a).denominator != 1 else int(a)], 'name': 'f'}
        name = None
    gr = {'typ': 'koordinaten', 'x': [-5, 5], 'y': [-7, 7], 'graphen': [g]}
    while True:
        x0 = R.randint(-4, 4); y0 = f(Fr(x0))
        if x0 == 0 and R.random() < .7: continue
        if Fr(y0).denominator == 1 and -6 <= y0 <= 6: break
    if st == 1 or R.random() < .4:
        return mit_bild(Z(f'Lies am Graphen ab: f({zt(x0)}) = ?', y0, f'{y0}', f'Bei x = {zt(x0)} senkrecht bis zum Graphen, dann waagrecht zur y-Achse: f({zt(x0)}) = {zt(y0)}.',
                          'Erst senkrecht zum Graphen, dann waagrecht zur y-Achse.'), gr)
    if art == 'quad' and x0 != 0:
        lo, hi = sorted((-x0, x0))
        if R.random() < .5:
            return mit_bild(L(f'Für welche x gilt f(x) = {zt(y0)}? Lies am Graphen ab (kleinere Stelle zuerst).', 'x₁ = □; x₂ = □', [lo, hi], [str(lo), str(hi)],
                              f'Die waagrechte Linie y = {zt(y0)} trifft die Parabel zweimal: bei x = {zt(lo)} und bei x = {zt(hi)}.',
                              'Gehe bei diesem y-Wert waagrecht durch das ganze Bild. Wie oft triffst du den Graphen?', hinweis='Trage beide Stellen ein.'), gr)
        return mit_bild(A(R, f'Für welche x gilt f(x) = {zt(y0)}?', f'x = {zt(lo)} und x = {zt(hi)}', [f'nur x = {zt(hi)}', f'x = {zt(y0)}', f'nur x = {zt(lo)}'],
                          f'Die waagrechte Linie y = {zt(y0)} trifft die Parabel zweimal: bei x = {zt(lo)} und bei x = {zt(hi)}.',
                          'Gehe bei diesem y-Wert waagrecht durch das ganze Bild.'), gr)
    if art == 'quad':
        return mit_bild(A(R, f'Wie oft nimmt f den Wert {zt(y0)} an?', 'genau einmal (am Scheitel)', ['zweimal', 'nie', 'unendlich oft'],
                          f'y = {zt(y0)} ist der Scheitelwert: Die waagrechte Linie berührt die Parabel nur im Punkt (0 | {zt(y0)}).',
                          'Gehe bei diesem y-Wert waagrecht durch das Bild.'), gr)
    return mit_bild(L(f'Lies am Graphen ab: An welcher Stelle hat f den Wert {zt(y0)}? Gib den Punkt an.', 'P(□ | □)', [x0, y0], [str(x0), str(y0)],
                      f'Bei y = {zt(y0)} waagrecht zum Graphen, dann senkrecht zur x-Achse: x = {zt(x0)}. Punkt P({zt(x0)} | {zt(y0)}).' + (f' Probe: f({zt(x0)}) = {einsetzen(name, x0)} = {zt(y0)}.' if name else ''),
                      'Erst waagrecht zum Graphen, dann senkrecht zur x-Achse.', hinweis='Trage x und y des Punktes ein.'), gr)


GEN = {'graph_lesen': g_graph_lesen, 'eindeutig': g_eindeutig, 'funktionswert': g_funktionswert, 'stelle': g_stelle, 'wertetabelle': g_wertetabelle,
       'mengen': g_mengen, 'nullstellen': g_nullstellen, 'punkt_graph': g_punkt_graph}


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl8.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl8 import mit_umbau  # noqa: E402

_TAB = {'typ': 'tabelle', 'kopf': ['Eingabe x', '1', '2', '3'], 'zeilen': [['Ausgabe y', '5', '7', '5']]}
_TAXI = {'typ': 'koordinaten', 'x': [0, 6], 'y': [0, 16], 'graphen': [{'art': 'linear', 'm': 2, 't': 3, 'name': 'Preis', 'bereich': [0, 6]}], 'name_x': 'km', 'name_y': '€', 'schritt_y': 2}
UMBAU = {
 'eindeutig': {
  'einstieg': 'Am Getränkeautomaten gibt Taste 1 immer Cola, Taste 2 immer Wasser und Taste 3 auch Cola. Dieselbe Taste liefert immer dasselbe Getränk. So eine verlässliche Zuordnung heißt ⟦Funktion⟧.',
  'woerter': [['Funktion', 'zu jeder Eingabe gehört genau eine Ausgabe'], ['Eingabe', 'was man hineingibt – beim Automaten die Taste, in Mathe x'], ['Ausgabe', 'was herauskommt – beim Automaten das Getränk, in Mathe y']],
  'bild': _TAB,
  'schritte': [{'text': 'Oben stehen die Eingaben 1, 2 und 3 – jede nur einmal.'},
               {'text': 'Die Ausgabe 5 steht zweimal. Das ist erlaubt, wie zwei Tasten für Cola.'},
               {'text': 'Keine Eingabe hat zwei Ausgaben. Also ⟦ist es eine Funktion⟧.'}],
  'fehler': 'Gehören zur Eingabe 2 die Ausgaben 4 und 6, ist es ⟦keine⟧ Funktion. Das wäre eine Taste, die mal Cola und mal Wasser gibt.',
  'fehler_bild': {'typ': 'tabelle', 'kopf': ['Eingabe x', '2', '2', '3'], 'zeilen': [['Ausgabe y', '4', '6', '4']]},
  'regel': 'Bei einer ⟦Funktion⟧ hat jede Eingabe genau eine Ausgabe. Kommt eine Eingabe mit zwei verschiedenen Ausgaben vor, ist es keine.'},
 'mengen': {
  'einstieg': 'Der Automat hat nur die Tasten 0, 1 und 3. Nur diese Zahlen darfst du hineingeben. Alles Erlaubte heißt ⟦Definitionsmenge⟧, alles, was herauskommt, ⟦Wertemenge⟧.',
  'woerter': [['Definitionsmenge D', 'alle Zahlen, die man einsetzen darf (alle Tasten)'], ['Wertemenge W', 'alle Zahlen, die herauskommen (alle Getränke)'], ['{0; 1; 3}', 'Mengenklammer: genau die Zahlen 0, 1 und 3']],
  'bild': {'typ': 'tabelle', 'kopf': ['Eingabe x', '0', '1', '3'], 'zeilen': [['2x + 1', '?', '?', '?']]},
  'schritte': [{'text': 'Die Vorschrift ist 2x + 1, die Definitionsmenge D = {0; 1; 3}.'},
               {'text': 'Taste 0 ergibt 2 · 0 + 1 = 1.', 'bild': {'zeilen': [['2x + 1', '1', '?', '?']]}},
               {'text': 'Taste 1 ergibt 3, Taste 3 ergibt 2 · 3 + 1 = 7.', 'bild': {'zeilen': [['2x + 1', '1', '3', '7']]}},
               {'text': 'Heraus kommen 1, 3 und 7, die Wertemenge W: ⟦W = {1; 3; 7}⟧.'}],
  'fehler': 'Bei 1/(x − 2) ist die 2 verboten, nicht die −2. Mit x = 2 stünde unten eine 0, und durch 0 kann man nicht teilen.',
  'fehler_bild': {'kopf': ['Eingabe x', '−2', '2'], 'zeilen': [['1/(x − 2)', '−1/4', 'geht nicht']]},
  'regel': 'Die ⟦Definitionsmenge⟧ ist alles, was man einsetzen darf. Die ⟦Wertemenge⟧ ist alles, was herauskommt. Teilen durch 0 ist nie erlaubt.'},
 'funktionswert': {
  'einstieg': 'Ein Taxi kostet 3 € Grundpreis und 2 € pro Kilometer. Die Rechenvorschrift ist wie eine Maschine: Kilometer hinein, Preis heraus. Was herauskommt, heißt ⟦Funktionswert⟧.',
  'woerter': [['t(x)', 'gelesen „t von x“: der Preis für x Kilometer'], ['t(5)', 'der Preis für 5 Kilometer'], ['Funktionswert', 'das Ergebnis der Maschine, also der y-Wert']],
  'bild': {**_TAXI, 'graphen': [{'art': 'linear', 'm': 2, 't': 3, 'name': 'Preis', 'bereich': [0, 6], 'name_x': 2}]},
  'schritte': [{'text': 'Die Taxi-Maschine heißt t(x) = 2x + 3. Gesucht ist t(5).'},
               {'text': 'Überall, wo x steht, eine 5 einsetzen: t(5) = 2 · 5 + 3.', 'bild': {'senkrecht': [5]}},
               {'text': 'Ausrechnen: 10 + 3 = 13. Also ⟦t(5) = 13⟧, die Fahrt kostet 13 €.', 'bild': {'punkte': [{'x': 5, 'y': 13, 'name': '(5 | 13)'}], 'waagrecht': [13]}}],
  'fehler': 't(5) ist nicht (2 + 3) · 5 = 25. Die 3 € Grundpreis zahlst du nur einmal, nicht für jeden Kilometer.',
  'fehler_bild': {'y': [0, 26], 'punkte': [{'x': 5, 'y': 13, 'name': 'richtig'}, {'x': 5, 'y': 25, 'name': '25?', 'offen': True}], 'waagrecht': []},
  'regel': 'Für t(5) ersetzt du ⟦jedes x durch 5⟧. Negative Zahlen setzt du dabei in Klammern: (−2)² = 4.'},
 'stelle': {
  'einstieg': 'Diesmal kennst du den Preis: Die Taxifahrt hat 15 € gekostet. Wie viele Kilometer waren das? Du kennst das Ergebnis und suchst die Eingabe, die ⟦Stelle⟧.',
  'woerter': [['Stelle', 'die Eingabe x, die zu einem Ergebnis gehört'], ['t(x) = 15', 'die Frage: Für welches x kommt 15 heraus?'], ['Gleichung', 'zwei Seiten, die gleich groß sein sollen']],
  'bild': {**_TAXI, 'x': [0, 8], 'y': [0, 20], 'graphen': [{'art': 'linear', 'm': 2, 't': 3, 'name': 'Preis', 'bereich': [0, 8]}]},
  'schritte': [{'text': 'Die Frage t(x) = 15 wird zur Gleichung: 2x + 3 = 15.', 'bild': {'waagrecht': [15]}},
               {'text': 'Auf beiden Seiten 3 abziehen: 2x = 12.'},
               {'text': 'Beide Seiten durch 2 teilen: ⟦x = 6⟧. Die Fahrt war 6 km lang.', 'bild': {'punkte': [{'x': 6, 'y': 15, 'name': '(6 | 15)'}], 'senkrecht': [6]}}],
  'fehler': 'Nicht die 15 für x einsetzen! t(15) wäre der Preis für 15 km, also 33 €. Die 15 ist hier das ⟦Ergebnis⟧.',
  'fehler_bild': {'x': [0, 16], 'y': [0, 36], 'graphen': [{'art': 'linear', 'm': 2, 't': 3, 'name': 'Preis', 'bereich': [0, 16]}], 'punkte': [{'x': 6, 'y': 15, 'name': 'richtig'}, {'x': 15, 'y': 33, 'name': 't(15)', 'offen': True}], 'senkrecht': [], 'waagrecht': []},
  'regel': 'Ist das Ergebnis gegeben, löst du ⟦f(x) = Ergebnis⟧ nach x auf. Das Ergebnis selbst setzt du nicht für x ein.'},
 'wertetabelle': {
  'einstieg': 'Der Taxifahrer hat eine Preisliste: oben die Kilometer, darunter der Preis. So siehst du viele Werte auf einen Blick. So eine Liste heißt ⟦Wertetabelle⟧.',
  'woerter': [['Wertetabelle', 'oben die Eingaben x, darunter die Ergebnisse f(x)'], ['Term', 'die Rechenvorschrift, hier 2x + 3']],
  'bild': {'typ': 'tabelle', 'kopf': ['x (km)', '1', '2', '3', '4'], 'zeilen': [['Preis (€)', '5', '7', '?', '11']]},
  'schritte': [{'text': 'Bei 3 km fehlt der Preis. Der Term ist 2x + 3.'},
               {'text': 'Setze 3 ein: 2 · 3 + 3 = ⟦9⟧.', 'bild': {'zeilen': [['Preis (€)', '5', '7', '9', '11']]}},
               {'text': 'Kontrolle: Pro Kilometer kommen immer 2 € dazu. 5, 7, 9, 11 passt.'}],
  'fehler': 'Ein Term muss zu ⟦allen⟧ Spalten passen. 4x + 1 passt bei 1 km, aber bei 2 km gäbe es 9 € statt 7 €.',
  'fehler_bild': {'zeilen': [['Preis (€)', '5', '7', '9', '11'], ['4x + 1', '5', '9', '13', '17']]},
  'regel': 'In der ⟦Wertetabelle⟧ steht oben x, darunter f(x). Fehlende Werte rechnest du mit dem Term aus. Ein gesuchter Term muss zu allen Spalten passen.'},
 'graph_lesen': {
  'einstieg': 'Ein Ball wird hochgeworfen. Das Bild zeigt, wie hoch er nach jeder Sekunde ist: unten die Zeit, links die Höhe. So ein Bild einer Funktion heißt ⟦Graph⟧.',
  'woerter': [['Graph', 'die Linie, die alle Paare (x | y) einer Funktion zeigt'], ['x-Achse', 'die waagrechte Achse, hier die Zeit in Sekunden'], ['y-Achse', 'die senkrechte Achse, hier die Höhe in Metern']],
  'bild': {'typ': 'koordinaten', 'x': [-1, 5], 'y': [-1, 5], 'graphen': [{'art': 'poly', 'k': [0, 4, -1], 'name': 'Höhe', 'bereich': [0, 4]}], 'name_x': 's', 'name_y': 'm'},
  'schritte': [{'text': 'Wie hoch ist der Ball nach 1 Sekunde? Suche die 1 auf der x-Achse.', 'bild': {'senkrecht': [1]}},
               {'text': 'Senkrecht hoch zur Kurve, dann waagrecht zur y-Achse: ⟦f(1) = 3⟧.', 'bild': {'punkte': [{'x': 1, 'y': 3, 'name': '(1 | 3)'}], 'waagrecht': [3]}},
               {'text': 'Rückwärts: Wann ist er 3 m hoch? Die waagrechte Linie trifft zweimal.', 'bild': {'punkte': [{'x': 1, 'y': 3, 'name': '(1 | 3)'}, {'x': 3, 'y': 3, 'name': '(3 | 3)'}], 'senkrecht': [1, 3]}},
               {'text': 'Also nach ⟦1 s und nach 3 s⟧ – einmal steigend, einmal fallend.'}],
  'fehler': 'Bei „Wann ist er 3 m hoch?“ nur 1 s angeben. Auf dem Weg nach unten ist der Ball noch einmal 3 m hoch: nach 3 s.',
  'fehler_bild': {'punkte': [{'x': 1, 'y': 3, 'name': '1 s'}, {'x': 3, 'y': 3, 'name': 'auch 3 s'}]},
  'regel': 'Ablesen: ⟦senkrecht⟧ zur Kurve, dann ⟦waagrecht⟧ zur Achse. Zu einem y-Wert kann es mehrere x-Werte geben.'},
 'nullstellen': {
  'einstieg': 'Du hast 7 € Schulden und zahlst jede Woche 2 € zurück. Nach x Wochen ist dein Kontostand 2x − 7 Euro. Die Stelle, an der er genau 0 ist, heißt ⟦Nullstelle⟧.',
  'woerter': [['Nullstelle', 'ein x, bei dem 0 herauskommt'], ['Kontostand', 'wie viel Geld du hast; Schulden sind negativ']],
  'bild': {'typ': 'koordinaten', 'x': [-1, 5], 'y': [-8, 3], 'graphen': [{'art': 'linear', 'm': 2, 't': -7, 'name': 'f'}], 'name_x': 'Wochen', 'name_y': '€'},
  'schritte': [{'text': 'Gesucht ist das x mit f(x) = 0. Also 2x − 7 = 0.'},
               {'text': 'Auf beiden Seiten 7 dazuzählen: 2x = 7.'},
               {'text': 'Durch 2 teilen: ⟦x = 3,5⟧. Nach 3,5 Wochen bist du schuldenfrei.', 'bild': {'punkte': [{'x': 3.5, 'y': 0, 'name': '(3,5 | 0)'}]}},
               {'text': 'Im Bild trifft die Gerade genau dort die x-Achse.'}],
  'fehler': 'Die Nullstelle ist nicht −7. f(0) = −7 ist dein Start: am Anfang 7 € Schulden. Für die Nullstelle muss ⟦f(x) = 0⟧ sein.',
  'fehler_bild': {'punkte': [{'x': 0, 'y': -7, 'name': 'Start'}, {'x': 3.5, 'y': 0, 'name': 'Nullstelle'}]},
  'regel': 'Für die ⟦Nullstelle⟧ setzt du f(x) = 0. Dort schneidet der Graph die x-Achse.'},
 'punkt_graph': {
  'einstieg': 'Auf einem Zettel steht: „4 km kosten 11 €.“ Passt das zum Taxi-Tarif? Du musst nicht zeichnen, du kannst es ausrechnen: Liegt der ⟦Punkt⟧ auf dem Graphen?',
  'woerter': [['P(4 | 11)', 'Punkt mit x = 4 (erste Zahl) und y = 11 (zweite Zahl)'], ['Koordinaten', 'die beiden Zahlen eines Punktes: erst x, dann y'], ['≠', '„ist nicht gleich“']],
  'bild': {**_TAXI, 'y': [0, 14], 'schritt_y': 2},
  'schritte': [{'text': 'Der Zettel als Punkt: P(4 | 11), mit den Koordinaten 4 und 11.', 'bild': {'punkte': [{'x': 4, 'y': 11, 'name': 'P'}]}},
               {'text': 'Setze x = 4 in den Tarif ein: 2 · 4 + 3 = 11.'},
               {'text': 'Es kommt genau 11 heraus. Also ⟦liegt P auf dem Graphen⟧.'},
               {'text': 'Q(4 | 10) passt nicht, denn 11 ≠ 10. ⟦Q liegt daneben.⟧', 'bild': {'punkte': [{'x': 4, 'y': 11, 'name': 'P'}, {'x': 4, 'y': 10, 'name': 'Q', 'offen': True}]}}],
  'fehler': 'Bei P(4 | 11) nicht die 11 für x einsetzen. Die ⟦erste⟧ Zahl ist immer x, hier die Kilometer.',
  'fehler_bild': {'x': [0, 12], 'graphen': [{'art': 'linear', 'm': 2, 't': 3, 'name': 'Preis', 'bereich': [0, 6]}], 'punkte': [{'x': 4, 'y': 11, 'name': 'P(4 | 11)'}, {'x': 11, 'y': 4, 'name': '(11 | 4)?', 'offen': True}]},
  'regel': 'Setze ⟦x in den Term ein⟧ und vergleiche mit y. Kommt genau y heraus, liegt der Punkt auf dem Graphen.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---- SCHWER (Zehnte Runde: schwerere Aufgaben nach Prüfungsvorbild, siehe _schwer_kl8.py) ----
# Vorbilder (Typ und Niveau, nicht Wortlaut/Zahlen): BMT8 2022/2025 (Tabellenkalkulations-Formel, Punkt vor Strich),
# BMT8 2024 (Rückwärts: Zahl ersetzen, damit eine vorgegebene Lösung herauskommt), Schulaufgaben-Typ „Zuordnung begründen,
# D und W im Sachzusammenhang, Achsenschnittpunkte, Punkt oberhalb/unterhalb“, Grundwissen 8 (Funktion ja/nein im Sachkontext).
from _schwer_kl8 import Neu, mit_schwer  # noqa: E402

N = Neu(10_8_1)
_g = lambda **k: {'typ': 'koordinaten', **k}

# eindeutig
N.a('eindeutig', 2, 'Jeder natürlichen Zahl wird ihre Quersumme zugeordnet. Und umgekehrt: Jeder Quersumme wird eine Zahl mit dieser Quersumme zugeordnet. Welche Zuordnungen sind Funktionen?',
    'Die erste ist eine Funktion, die zweite nicht.', ['Beide sind Funktionen.', 'Die zweite ist eine Funktion, die erste nicht.', 'Keine ist eine Funktion.'],
    'Jede Zahl hat genau eine Quersumme (z. B. 23 ↦ 5). Zur Quersumme 5 passen aber 5, 14, 23, 50, … – also mehrere Zahlen. Nur die erste ist eine Funktion.',
    'Suche für die Rückrichtung ein Beispiel: Gibt es zwei Zahlen mit derselben Quersumme?')
N.a('eindeutig', 2, 'Die Tabelle zeigt die Temperatur an einem Tag. Zuordnung A: Uhrzeit ↦ Temperatur. Zuordnung B: Temperatur ↦ Uhrzeit. Welche ist eine Funktion?',
    'nur A', ['nur B', 'beide', 'keine'],
    'Zu jeder Uhrzeit gehört genau eine Temperatur: A ist eine Funktion. Die Temperatur 15 °C kommt um 10 Uhr und um 14 Uhr vor – B ordnet ihr zwei Uhrzeiten zu, B ist keine Funktion.',
    'Prüfe bei B: Kommt eine Temperatur zweimal vor?',
    grafik={'typ': 'tabelle', 'kopf': ['Uhrzeit', '8 Uhr', '10 Uhr', '12 Uhr', '14 Uhr'], 'zeilen': [['Temp.', '12 °C', '15 °C', '18 °C', '15 °C']]})
N.a('eindeutig', 3, 'Ein Rennwagen fährt 3 Runden auf einem Rundkurs. Zuordnung A: Zeit seit dem Start ↦ Ort auf der Strecke. Zuordnung B: Ort auf der Strecke ↦ Geschwindigkeit. Welche Zuordnung ist sicher eine Funktion?',
    'nur A', ['nur B', 'beide', 'keine'],
    'Zu jedem Zeitpunkt ist der Wagen an genau einem Ort: A ist eine Funktion. An jedem Ort kommt er dreimal vorbei, meist mit verschiedener Geschwindigkeit – ein Ort hätte dann mehrere Werte. B ist nicht sicher eine Funktion.',
    'Denke an einen festen Ort, z. B. die Startlinie: Wie oft fährt der Wagen dort vorbei?', art='P')
N.a('eindeutig', 3, 'Mia behauptet: „Die Zuordnung x ↦ y mit y² = x ist eine Funktion. Denn zu x = 0 gehört nur y = 0.“ Was stimmt?',
    'Falsch: Zu x = 4 gehören y = 2 und y = −2.', ['Richtig: Ein passendes Beispiel beweist die Aussage.', 'Richtig: Zu jedem y gehört genau ein x.',
                                                    'Falsch: Eine Funktion darf nie den Wert 0 haben.'],
    'Ein einziges Beispiel beweist nichts. Ein Gegenbeispiel widerlegt: 2² = 4 und (−2)² = 4. Also gehören zu x = 4 zwei Werte y. Die Zuordnung ist keine Funktion.',
    'Suche ein x, zu dem zwei verschiedene y passen. Denke an negative Zahlen.', art='P')
N.z('eindeutig', 3, 'Die Zuordnung besteht aus den Paaren (1 | 4), (3 | 7), (5 | 7) und (a | 2). Für wie viele der Zahlen a = 1, 2, 3, 4, 5 ist sie KEINE Funktion?',
    3, '1 + 1 + 1',
    'Keine Funktion, wenn a schon als x vorkommt und dort nicht 2 steht: a = 1 (4 und 2), a = 3 (7 und 2), a = 5 (7 und 2). Das sind 3 Werte. Dass zweimal 7 vorkommt, ist erlaubt.',
    'Probiere jedes a: Kommt a schon als x-Wert vor? Gleiche y-Werte bei verschiedenen x stören nicht.', art='K')
N.a('eindeutig', 3, 'Ist der gezeichnete Kreis der Graph einer Funktion?',
    'Nein: Die senkrechte Linie x = 0 trifft ihn bei y = 3 und bei y = −3.', ['Ja: Der Kreis ist eine geschlossene Linie.', 'Ja: Zu jedem y gibt es höchstens zwei x.',
                                                                            'Nein: Ein Graph muss immer eine Gerade sein.'],
    'Prüfe mit senkrechten Linien. Die y-Achse (x = 0) schneidet den Kreis in (0 | 3) und (0 | −3). Zu x = 0 gehören also zwei Werte – keine Funktion.',
    'Lege in Gedanken ein senkrechtes Lineal an. Wie oft trifft es den Kreis?', art='K',
    grafik=_g(x=[-4, 4], y=[-4, 4], kreise=[{'m': [0, 0], 'r': 3}]))

# mengen
N.a('mengen', 2, 'Gib die maximale Definitionsmenge von f(x) = 6/(2x − 5) an.', 'D = ℚ \\ {2,5}', ['D = ℚ \\ {5}', 'D = ℚ \\ {−2,5}', 'D = ℚ \\ {0}'],
    'Der Nenner darf nicht 0 sein: 2x − 5 = 0 ⇔ 2x = 5 ⇔ x = 2,5. Also D = ℚ \\ {2,5}.', 'Setze den Nenner gleich 0 und löse nach x auf.')
N.a('mengen', 2, 'f(x) = 4 − x² mit D = ℚ. Welche Zahl ist KEIN Funktionswert von f?', '5', ['4', '0', '−5'],
    'x² ist nie negativ. Also ist 4 − x² höchstens 4 (bei x = 0). 0 kommt bei x = 2 vor, −5 bei x = 3. Nur 5 ist zu groß.',
    'Wie groß kann 4 − x² höchstens werden?')
N.a('mengen', 3, 'Ein Becken mit 60 m³ wird von n gleich starken Pumpen gefüllt. Es dauert t(n) = 60/n Stunden. Es gibt höchstens 4 Pumpen. Welche Definitionsmenge ist hier sinnvoll?',
    'D = {1; 2; 3; 4}', ['D = ℚ \\ {0}', 'D = {0; 1; 2; 3; 4}', 'D = ℚ⁺'],
    'n zählt Pumpen: nur ganze Zahlen. Mit 0 Pumpen füllt sich nichts (und durch 0 teilt man nicht). Mehr als 4 gibt es nicht. Also D = {1; 2; 3; 4}.',
    'Was kann n in der Wirklichkeit sein? Halbe Pumpen? Null Pumpen?', art='P')
N.a('mengen', 3, 'Becken mit 60 m³, n Pumpen, Füllzeit t(n) = 60/n Stunden, D = {1; 2; 3; 4}. Gib die Wertemenge an.',
    'W = {15; 20; 30; 60}', ['W = {1; 2; 3; 4}', 'W = {60; 120; 180; 240}', 'W = {0; 15; 20; 30; 60}'],
    't(1) = 60, t(2) = 30, t(3) = 20, t(4) = 15. Die Wertemenge enthält alle Ergebnisse: W = {15; 20; 30; 60}.',
    'Setze jede Zahl aus D ein. Teile, nicht malnehmen.', art='P')
N.a('mengen', 3, 'Gib die maximale Definitionsmenge von f(x) = (x + 3)/(x² + 1) an.', 'D = ℚ', ['D = ℚ \\ {−3}', 'D = ℚ \\ {−1}', 'D = ℚ \\ {−1; 1}'],
    'Nur der Nenner zählt. x² ist nie negativ, also ist x² + 1 immer mindestens 1 und nie 0. Man darf alles einsetzen: D = ℚ. Der Zähler darf 0 werden.',
    'Kann x² + 1 überhaupt 0 werden? Der Zähler spielt für D keine Rolle.', art='K')
N.z('mengen', 3, 'Die Funktion f(x) = 5/(x − a) hat die Definitionsmenge D = ℚ \\ {−4}. Bestimme a.', -4, '-4',
    'Ausgeschlossen ist die Zahl, für die x − a = 0 ist, also x = a. Da −4 ausgeschlossen ist, gilt a = −4. Probe: Nenner x − (−4) = x + 4 wird bei x = −4 null.',
    'Für welches x wird der Nenner x − a null? Rückwärts denken.', art='K')

# funktionswert
N.z('funktionswert', 2, 'Berechne f(−1,5) für f(x) = 2x² − x.', 6, '2 * (-1.5)**2 - (-1.5)',
    'f(−1,5) = 2 · (−1,5)² − (−1,5) = 2 · 2,25 + 1,5 = 4,5 + 1,5 = 6.', 'Erst das Quadrat, dann mal 2. Minus eine negative Zahl wird plus.')
N.z('funktionswert', 2, 'Berechne f(0,5) für f(x) = 4/x − 2x.', 7, '4 / 0.5 - 2 * 0.5',
    'f(0,5) = 4 : 0,5 − 2 · 0,5 = 8 − 1 = 7.', 'Durch 0,5 teilen heißt verdoppeln.')
N.z('funktionswert', 3, 'In einer Tabellenkalkulation steht in Zelle A1 die Zahl 3 und in A2 die Zahl −2. In B1 steht die Formel =A1*(A2+4)-A2. Welchen Wert zeigt B1?',
    8, '3 * ((-2) + 4) - (-2)',
    'Einsetzen: 3 · ((−2) + 4) − (−2) = 3 · 2 + 2 = 8. Erst die Klammer, dann mal, dann minus der negativen Zahl.',
    'Ersetze A1 und A2 durch ihre Zahlen. Achte auf Klammern und auf „minus minus“.', art='P')
N.a('funktionswert', 3, 'Eine Tabellenkalkulation soll f(x) = (x + 6) : 2 berechnen. x steht in Zelle A2. Welche Formel ist richtig?',
    '=(A2+6)/2', ['=A2+6/2', '=A2+(6/2)', '=(A2+6)*2'],
    'Punkt vor Strich: =A2+6/2 rechnet A2 + 3. Erst die Summe, dann teilen geht nur mit Klammer: =(A2+6)/2. Beispiel x = 4: (4 + 6) : 2 = 5, aber 4 + 6 : 2 = 7.',
    'Teste mit einer Zahl, z. B. x = 4. Was rechnet der Computer zuerst?', art='P')
N.z('funktionswert', 3, 'Für f(x) = x² − 3x gilt f(a) = f(a + 1). Bestimme a.', 1, '(3 - 1) / 2',
    'f(a + 1) = (a + 1)² − 3(a + 1) = a² + 2a + 1 − 3a − 3 = a² − a − 2. Gleichsetzen mit a² − 3a: −3a = −a − 2, also −2a = −2 und a = 1. Probe: f(1) = −2 und f(2) = −2.',
    'Setze a + 1 für x ein und multipliziere aus. Dann fällt a² weg.', art='K')
N.z('funktionswert', 3, 'f(x) = −x² + 4. Berechne f(2) − f(−3).', 5, '(-(2**2) + 4) - (-((-3)**2) + 4)',
    'f(2) = −4 + 4 = 0. f(−3) = −(−3)² + 4 = −9 + 4 = −5. Differenz: 0 − (−5) = 5.',
    'Bei −x² wird erst quadriert, dann kommt das Minus davor: −(−3)² = −9.')

# stelle
N.z('stelle', 2, 'Für welches x gilt f(x) = 0,5, wenn f(x) = 3/x?', 6, '3 / 0.5', '3/x = 0,5 ⇔ 3 = 0,5 · x ⇔ x = 3 : 0,5 = 6.', 'Multipliziere beide Seiten mit x.')
N.z('stelle', 2, 'Für welches x gilt f(x) = −7, wenn f(x) = 5 − 4x?', 3, '(5 - (-7)) / 4', '5 − 4x = −7 ⇔ −4x = −12 ⇔ x = 3.', 'Bringe die 5 auf die andere Seite.')
N.z('stelle', 3, 'Gegeben ist f(x) = 3(x − 2) + c. Welche Zahl muss c sein, damit f(5) = 4 gilt?', -5, '4 - 3 * (5 - 2)',
    'f(5) = 3 · (5 − 2) + c = 9 + c. Aus 9 + c = 4 folgt c = −5.', 'Setze x = 5 ein. Dann bleibt eine Gleichung für c.', art='P')
N.z('stelle', 3, 'Ein Handwerker berechnet K(t) = 45 + 52 · t (t in Stunden, K in €). Die Rechnung lautet über 279 €. Wie viele Stunden hat er gearbeitet?', 4.5, '(279 - 45) / 52',
    '45 + 52t = 279 ⇔ 52t = 234 ⇔ t = 4,5. Er hat 4,5 Stunden gearbeitet.', 'Ziehe zuerst die Anfahrt (45 €) ab.', einheit='h', art='P')
N.z('stelle', 3, 'Für welches x gilt f(x) = 2, wenn f(x) = (x + 3)/(x − 1)?', 5, '(3 + 2) / (2 - 1)',
    '(x + 3)/(x − 1) = 2 ⇔ x + 3 = 2(x − 1) = 2x − 2 ⇔ x = 5. x = 5 ist erlaubt (Nenner 4). Probe: 8/4 = 2.',
    'Multipliziere mit dem Nenner (x − 1). Prüfe am Ende, ob der Nenner 0 wird.')
N.l('stelle', 3, 'Für welche x gilt f(x) = 9, wenn f(x) = x² − 7? Gib beide Stellen an, die kleinere zuerst.', 'x₁ = □; x₂ = □', [-4, 4], ['-4', '4'],
    'x² − 7 = 9 ⇔ x² = 16. Das gilt für x = 4 und für x = −4, denn (−4)² = 16.', 'Welche Zahlen ergeben quadriert 16? Es gibt zwei.',
    'Je Lücke eine ganze Zahl, die kleinere zuerst.', art='K')

# wertetabelle
_schnee = {'typ': 'tabelle', 'kopf': ['Zeit (h)', '0', '2', '4', '6'], 'zeilen': [['Schnee (cm)', '12', '17', '22', '27']]}
N.z('wertetabelle', 2, 'Die Tabelle gehört zu f(x) = 2x − 3. Für welches x ist f(x) = 0?', 1.5, '3 / 2', '2x − 3 = 0 ⇔ 2x = 3 ⇔ x = 1,5.',
    'Setze den Term gleich 0.', grafik={'typ': 'tabelle', 'kopf': ['x', '0', '1', '?', '2'], 'zeilen': [['f(x)', '−3', '−1', '0', '1']]})
N.z('wertetabelle', 2, 'Die Tabelle gehört zu f(x) = −x² + 2x. Welcher Wert gehört an die Stelle „?“?', -3, '-((-1)**2) + 2 * (-1)', 'f(−1) = −(−1)² + 2 · (−1) = −1 − 2 = −3.',
    'Erst quadrieren, dann das Minus davor.', grafik={'typ': 'tabelle', 'kopf': ['x', '−1', '0', '3'], 'zeilen': [['f(x)', '?', '0', '−3']]})
N.a('wertetabelle', 3, 'Während eines Schneefalls wird die Schneehöhe gemessen (Tabelle). Welcher Term beschreibt die Höhe h(t) in cm nach t Stunden?',
    'h(t) = 12 + 2,5t', ['h(t) = 12 + 5t', 'h(t) = 2,5t', 'h(t) = 17 + 2,5t'],
    'Bei t = 0 liegen schon 12 cm. In 2 Stunden kommen 5 cm dazu, also 2,5 cm pro Stunde: h(t) = 12 + 2,5t. Probe: h(6) = 12 + 15 = 27.',
    'Was gilt bei t = 0? Wie viel kommt in einer Stunde dazu?', grafik=_schnee, art='P')
N.z('wertetabelle', 3, 'Die Schneehöhe wächst weiter wie in der Tabelle. Nach wie vielen Stunden (ab Beginn der Messung) liegen 42 cm Schnee?', 12, '(42 - 12) / 2.5',
    'h(t) = 12 + 2,5t = 42 ⇔ 2,5t = 30 ⇔ t = 12. Nach 12 Stunden.', 'Stelle zuerst den Term auf. Dann löse h(t) = 42.', einheit='h', grafik=_schnee, art='P')
N.z('wertetabelle', 3, 'In der Wertetabelle von f(x) = a · x² steht das Paar (2 | 12). Welcher Wert gehört zu x = −3?', 27, '(12 / 2**2) * (-3)**2',
    'Aus a · 2² = 12 folgt a = 3. Dann f(−3) = 3 · (−3)² = 3 · 9 = 27. Das Quadrat ist positiv.',
    'Bestimme zuerst a aus dem bekannten Paar.', art='K')
N.a('wertetabelle', 3, 'Welcher Term passt zur Wertetabelle?', 'f(x) = x² + 3', ['f(x) = −x² + 3', 'f(x) = 3x + 3', 'f(x) = x² + 3x'],
    'Die Werte sind zu 0 symmetrisch (f(−2) = f(2) = 7): typisch für x². f(0) = 3, f(1) = 1 + 3 = 4, f(2) = 4 + 3 = 7. Also f(x) = x² + 3.',
    'Vergleiche f(−1) und f(1). Teste jeden Term an allen Spalten.',
    grafik={'typ': 'tabelle', 'kopf': ['x', '−2', '−1', '0', '1', '2'], 'zeilen': [['f(x)', '7', '4', '3', '4', '7']]}, art='K')

# graph_lesen
_par = _g(x=[-4, 4], y=[-3, 7], graphen=[{'art': 'poly', 'k': [-2, 0, 0.5], 'name': 'f'}])
_wanne = _g(x=[0, 40], y=[0, 50], schritt_x=5, schritt_y=10, name_x='t in min', name_y='h in cm',
            graphen=[{'art': 'linear', 'm': 4, 't': 0, 'bereich': [0, 10]}, {'art': 'linear', 'm': 0, 't': 40, 'bereich': [10, 25]},
                     {'art': 'linear', 'm': -4, 't': 140, 'bereich': [25, 35]}])
N.z('graph_lesen', 2, 'Lies am Graphen der Parabel ab: Welchen Wert hat f(4)?', 6, '0.5 * 4**2 - 2', 'Bei x = 4 senkrecht zum Graphen, dann waagrecht zur y-Achse: f(4) = 6.',
    'Gehe von x = 4 senkrecht nach oben bis zur Kurve.', grafik=_par)
N.z('graph_lesen', 2, 'Der Graph zeigt den Wasserstand in einer Badewanne. Wie hoch steht das Wasser nach 5 Minuten?', 20, '4 * 5',
    'Bei t = 5 senkrecht nach oben zum Graphen, dann waagrecht zur Achse: 20 cm.', 'Eine Kästchenbreite sind 5 Minuten.', einheit='cm', grafik=_wanne)
N.a('graph_lesen', 3, 'Für welche x liegt der Graph von f unterhalb der x-Achse?', 'für −2 < x < 2', ['für x < −2 und x > 2', 'für −2 ≤ x ≤ 2', 'für x < 0'],
    'Der Graph schneidet die x-Achse bei −2 und bei 2. Dazwischen liegt er unter der Achse. An den Stellen −2 und 2 selbst ist f(x) = 0, also nicht darunter.',
    'Lies zuerst die Nullstellen ab. Liegt der Graph dazwischen oben oder unten?', grafik=_par, art='P')
N.z('graph_lesen', 3, 'Badewanne (Graph): Wie viele Minuten lang bleibt der Wasserstand gleich?', 15, '25 - 10',
    'Der Graph ist von t = 10 bis t = 25 waagrecht. Das sind 25 − 10 = 15 Minuten.', 'Wo verläuft der Graph waagrecht? Lies Anfang und Ende ab.',
    einheit='min', grafik=_wanne, art='P')
N.l('graph_lesen', 3, 'Badewanne (Graph): Zu welchen Zeitpunkten steht das Wasser 20 cm hoch? Gib beide an, den früheren zuerst.', 't₁ = □; t₂ = □ (in min)', [5, 30],
    ['20 / 4', '(140 - 20) / 4'],
    'Waagrechte Linie bei 20 cm: Sie trifft den Graphen beim Einlaufen (t = 5) und beim Ablaufen (t = 30).',
    'Ziehe eine waagrechte Linie bei h = 20. Wo trifft sie den Graphen?', 'Je Lücke eine ganze Zahl (Minuten).', grafik=_wanne, art='K')
N.z('graph_lesen', 3, 'Für welche Zahl c hat die Gleichung f(x) = c genau eine Lösung? Lies am Graphen ab.', -2, '0.5 * 0**2 - 2',
    'Eine waagrechte Linie y = c trifft die Parabel meist zweimal oder gar nicht. Nur durch den tiefsten Punkt (0 | −2) trifft sie genau einmal: c = −2.',
    'Denke an waagrechte Linien in verschiedener Höhe. Wann gibt es genau einen Treffpunkt?', grafik=_par, art='K')

# nullstellen
N.z('nullstellen', 2, 'Eine Kerze ist 18 cm hoch und brennt pro Stunde 1,5 cm ab: h(t) = 18 − 1,5t. Berechne die Nullstelle von h.', 12, '18 / 1.5',
    '18 − 1,5t = 0 ⇔ 1,5t = 18 ⇔ t = 12. Nach 12 Stunden ist die Kerze abgebrannt.', 'Setze h(t) = 0.', einheit='h')
N.z('nullstellen', 2, 'Berechne die Nullstelle von f(x) = −0,5x + 4.', 8, '4 / 0.5', '−0,5x + 4 = 0 ⇔ 0,5x = 4 ⇔ x = 8.', 'Setze f(x) = 0 und löse nach x auf.')
N.l('nullstellen', 3, 'Der Graph von f(x) = (2x − 6)/(x + 1) schneidet die x-Achse im Punkt N und die y-Achse im Punkt S. Gib beide Punkte an.',
    'N(□ | 0); S(0 | □)', [3, -6], ['6 / 2', '(2 * 0 - 6) / (0 + 1)'],
    'x-Achse: Zähler 0 setzen: 2x − 6 = 0 ⇔ x = 3 (Nenner 4, erlaubt). y-Achse: x = 0 einsetzen: f(0) = −6/1 = −6.',
    'Für die x-Achse ist y = 0, für die y-Achse ist x = 0.', 'Je Lücke eine ganze Zahl.', art='P')
N.a('nullstellen', 3, 'Welche Nullstellen hat f(x) = (x² − 9)/(x − 3)?', 'nur x = −3', ['x = −3 und x = 3', 'nur x = 3', 'keine'],
    'Der Zähler ist 0 für x = 3 und x = −3. Aber x = 3 macht den Nenner 0 und gehört nicht zur Definitionsmenge. Bleibt nur x = −3.',
    'Bestimme erst die Definitionsmenge. Eine Nullstelle muss erlaubt sein.', art='K')
N.z('nullstellen', 3, 'Für welchen Wert von b hat f(x) = 4x + b die Nullstelle x = −2,5?', 10, '-4 * (-2.5)',
    'f(−2,5) = 0 ⇔ 4 · (−2,5) + b = 0 ⇔ −10 + b = 0 ⇔ b = 10.', 'Setze die Nullstelle ein. f muss dort 0 ergeben.', art='P')
N.z('nullstellen', 3, 'f(x) = x(x − 3)(x + 5). Berechne die Summe aller Nullstellen von f.', -2, '0 + 3 + (-5)',
    'Ein Produkt ist 0, wenn ein Faktor 0 ist: x = 0, x = 3 oder x = −5. Summe: 0 + 3 + (−5) = −2.',
    'Jeder der drei Faktoren kann 0 sein. Vergiss den Faktor x nicht.', art='K')

# punkt_graph
N.a('punkt_graph', 2, 'Liegt der Punkt Q(−1 | 4) oberhalb, unterhalb oder auf dem Graphen von f(x) = x² + 2?', 'oberhalb', ['unterhalb', 'auf dem Graphen'],
    'f(−1) = 1 + 2 = 3. Der Punkt hat y = 4 > 3. Er liegt oberhalb des Graphen.', 'Berechne f(−1) und vergleiche mit der y-Koordinate.')
N.a('punkt_graph', 2, 'Welcher Punkt liegt auf dem Graphen von f(x) = 6/x?', 'P(−2 | −3)', ['P(−2 | 3)', 'P(3 | −2)', 'P(0 | 6)'],
    'f(−2) = 6 : (−2) = −3. Also liegt P(−2 | −3) auf dem Graphen. Für x = 0 ist f nicht definiert.', 'Setze die x-Koordinate ein. Achte auf das Vorzeichen.')
N.a('punkt_graph', 3, 'Liegt der Punkt P(3 | 5) oberhalb, unterhalb oder auf dem Graphen von f(x) = 2x − 0,5?', 'unterhalb', ['oberhalb', 'auf dem Graphen'],
    'f(3) = 6 − 0,5 = 5,5. Der Punkt hat y = 5 < 5,5. Er liegt unterhalb des Graphen.', 'Berechne den Funktionswert an der Stelle 3.', art='P')
N.l('punkt_graph', 3, 'Die Punkte A(1 | 3) und B(3 | 7) liegen auf dem Graphen von f(x) = m · x + t. Bestimme m und t.', 'm = □; t = □', [2, 1], ['(7 - 3) / (3 - 1)', '3 - 2 * 1'],
    'Von A nach B: x wächst um 2, y um 4. Also m = 4 : 2 = 2. Einsetzen von A: 3 = 2 · 1 + t ⇔ t = 1. f(x) = 2x + 1.',
    'Bestimme zuerst die Steigung aus beiden Punkten, dann t mit einem Punkt.', 'Je Lücke eine ganze Zahl.', art='P')
N.z('punkt_graph', 3, 'Der Punkt P(a | a) hat zwei gleiche Koordinaten und liegt auf dem Graphen von f(x) = 3x − 8. Bestimme a.', 4, '8 / 2',
    'Einsetzen: a = 3a − 8 ⇔ 8 = 2a ⇔ a = 4. Probe: f(4) = 12 − 8 = 4.', 'Setze für x und für y dieselbe Zahl a ein.', art='K')
N.a('punkt_graph', 3, 'Liegt P(2 | 1) auf dem Graphen von f(x) = 4/(x − 2) + 1?', 'Nein: x = 2 gehört nicht zur Definitionsmenge.',
    ['Ja: Für x = 2 ergibt sich 1.', 'Nein: f(2) = 3.', 'Ja: Jeder Punkt mit y = 1 liegt darauf.'],
    'Für x = 2 wird der Nenner x − 2 null. f(2) gibt es nicht. Also gibt es auf dem Graphen keinen Punkt mit x = 2.',
    'Prüfe zuerst: Darf man x = 2 überhaupt einsetzen?', art='K')

baue = mit_schwer(baue, N)
# ---- SCHWER ENDE ----


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, mit_befunden  # noqa: E402

BF = Befunde('funktionen.grundbegriffe', 13_8_1)
# a) gleicher Gedanke wie Stufe 1/2 (Paarliste prüfen) → Stufe 2
BF.stufe('eindeutig', 'Welche Zuordnung ist KEINE Funktion?', 2, anzahl=2)
# a) einschrittiges Einsetzen → Stufe 2
BF.stufe('funktionswert', 'Berechne f(6) für f(x) = 2/(x − 5).', 2)
# c) unübliche Schreibweise −1(x + 1) → −(x + 1)
_H = 'Das Minus vor der Klammer bedeutet „mal (−1)“. Teile zuerst durch −1.'
BF.ersetze('stelle', 'Für welches x gilt f(x) = −3, wenn f(x) = −1(x + 1)?',
           BF.Z('Für welches x gilt f(x) = −3, wenn f(x) = −(x + 1)?', 2, '-3 / (-1) + (-1)', '−(x + 1) = −3 | : (−1) → x + 1 = 3 → x = 2.', _H))
BF.ersetze('stelle', 'Für welches x gilt f(x) = −2, wenn f(x) = −1(x + 4)?',
           BF.Z('Für welches x gilt f(x) = −2, wenn f(x) = −(x + 4)?', -2, '-2 / (-1) + (-4)', '−(x + 4) = −2 | : (−1) → x + 4 = 2 → x = −2.', _H))
BF.ersetze('stelle', 'Für welches x gilt f(x) = −4, wenn f(x) = −1(x + 4)?',
           BF.Z('Für welches x gilt f(x) = −4, wenn f(x) = −(x + 4)?', 0, '-4 / (-1) + (-4)', '−(x + 4) = −4 | : (−1) → x + 4 = 4 → x = 0.', _H))
BF.nicht_umgesetzt('punkt_graph S2 „Lies am Graphen ab: f(4) = ?“ (gehört eher zu graph_lesen)',
                   'Bei erneuter Prüfung passend: Den Punkt (4 | f(4)) am Graphen ablesen gehört zu „Liegt der Punkt auf dem Graphen?“. Lösung richtig, kein Mangel.')
BF.fuer_sebastian('funktionen.grundbegriffe: Der Eintrag in „offen“ („Kreis kann die App nicht zeichnen“) ist veraltet – die App zeichnet Kreise (koordinaten.kreise). Nur der Haupt-Chat ändert „offen“.')

baue = mit_befunden(baue, BF)
# ---- BEFUNDE ENDE ----

# ---- LÜCKEN (Achtzehnte Runde, Teil B: neue Lernkarte „sachzusammenhang“ am Ende, siehe _luecken_kl8.py) ----
# LehrplanPLUS M8 1 (Funktion und Term): funktionale Zusammenhänge aus dem Alltag (z. B. Stromtarife, Temperaturverläufe) mit Tabellen,
# Diagrammen und, wo möglich, Termen erfassen und beschreiben (ISB, Schwerpunktsetzungen Jgst. 8).
# Vorbilder (Typ und Niveau, nicht Wortlaut/Zahlen): BMT8 2022/2025 (Tarif/Formel in Tabelle), BMT10 2024 (Schnittpunkt zweier Tarife),
# VERA-8 (Temperaturkurve lesen und deuten).
import collections  # noqa: E402

from _bausatz import eur  # noqa: E402
from _luecken_kl8 import K as _K, P as _P, Luecken, mit_luecken  # noqa: E402

LK = Luecken('funktionen.grundbegriffe', 18_8_1)
_LZ = 'sachzusammenhang'
_KO = lambda **k: {'typ': 'koordinaten', **k}

_KARTE = {
    'lernziel': _LZ, 'titel': 'Zusammenhänge aus dem Alltag beschreiben',
    'einstieg': 'Ein Handytarif kostet 5 € Grundgebühr im Monat und 2 € je GB. Der Preis hängt von den GB ab. '
                'Das ist ein ⟦funktionaler Zusammenhang⟧: Man zeigt ihn als Tabelle, Term oder Graph.',
    'woerter': [['funktionaler Zusammenhang', 'eine Größe hängt eindeutig von einer anderen ab, z. B. der Preis von den GB'],
                ['Grundgebühr', 'fester Betrag, den man immer zahlt, auch bei 0 GB']],
    'bild': _KO(x=[0, 7], y=[0, 18], graphen=[{'art': 'linear', 'm': 2, 't': 5, 'name': 'Preis', 'bereich': [0, 6.5]}], name_x='GB', name_y='€', schritt_y=2),
    'schritte': [{'text': 'Tabelle: 0 GB kosten 5 €, 1 GB 7 €, 2 GB 9 €.',
                  'bild': {'typ': 'tabelle', 'kopf': ['GB (Eingabe)', '0', '1', '2', '3'], 'zeilen': [['Preis in €', '5', '7', '9', '11']]}},
                 {'text': 'Je GB kommen 2 € dazu. Term: K(x) = 5 + 2 · x.'},
                 {'text': 'Im Graphen liegen diese Punkte auf einer Linie, Start bei 5 €.',
                  'bild': _KO(x=[0, 7], y=[0, 18], graphen=[{'art': 'linear', 'm': 2, 't': 5, 'name': 'Preis', 'bereich': [0, 6.5]}], name_x='GB', name_y='€', schritt_y=2,
                              punkte=[{'x': 0, 'y': 5}, {'x': 1, 'y': 7}, {'x': 2, 'y': 9}, {'x': 3, 'y': 11}])},
                 {'text': 'Am Graphen abgelesen: Für 15 € bekommt man ⟦5 GB⟧.',
                  'bild': {'strecken': [[0, 15, 5, 15, 'gestrichelt'], [5, 15, 5, 0, 'gestrichelt']], 'punkte': [{'x': 5, 'y': 15, 'name': '(5 | 15)'}]}}],
    'probe': 'K(5) = 5 + 2 · 5 = 15 ✓',
    'fehler': 'Die Grundgebühr nicht vergessen: 3 GB kosten 5 € + 3 · 2 € = 11 €, nicht 6 €. Wie eine Rechnung ohne den festen Monatspreis.',
    'fehler_bild': _KO(x=[0, 7], y=[0, 18], graphen=[{'art': 'linear', 'm': 2, 't': 5, 'name': 'richtig', 'bereich': [0, 6.5]},
                                                    {'art': 'linear', 'm': 2, 't': 0, 'name': 'ohne 5 €', 'bereich': [0, 6.5]}],
                       name_x='GB', name_y='€', schritt_y=2, punkte=[{'x': 3, 'y': 11, 'name': '11 €'}, {'x': 3, 'y': 6, 'name': '6 €'}]),
    'regel': 'Erst die feste Größe, dann die Änderung pro Einheit. Tabelle, Term und Graph zeigen denselben ⟦Zusammenhang⟧.',
}

# Tarife: (Wer, Einheit Einzahl, Einheit Mehrzahl, Grundgebühren, Preise je Einheit, Anzahlen, Mehrzahl im Dativ, Kurzname)
_TARIFE = [('Ein Handytarif', 'GB', 'GB', range(4, 11), [Fr(1), Fr(3, 2), Fr(2), Fr(5, 2), Fr(3)], range(2, 11), 'GB', 'Handytarife'),
           ('Ein Fahrradverleih', 'Stunde', 'Stunden', range(3, 9), [Fr(2), Fr(5, 2), Fr(3), Fr(4)], range(2, 9), 'Stunden', 'Tarife beim Fahrradverleih'),
           ('Ein Stromtarif', 'kWh', 'kWh', range(8, 16), [Fr(25, 100), Fr(3, 10), Fr(35, 100), Fr(4, 10)], range(100, 401, 20), 'kWh', 'Stromtarife'),
           ('Ein Kletterhallen-Abo', 'Besuch', 'Besuche', range(10, 31, 5), [Fr(4), Fr(5), Fr(6), Fr(15, 2)], range(2, 13), 'Besuchen', 'Abos der Kletterhalle')]
_W = collections.Counter()


def _wahl(R, st, arten):
    n = min(_W[(st, a)] for a in arten)
    a = R.choice([x for x in arten if _W[(st, x)] == n])
    _W[(st, a)] += 1
    return a


def _tarif(R, voll=False):
    wer, e1, e2, gs, ps, xs, e3, kurz = R.choice(_TARIFE)
    t = (wer, e1, e2, Fr(R.choice(list(gs))), R.choice(ps), list(xs))
    return t + (e3, kurz) if voll else t


def _temp(R):
    """Temperaturverlauf T(h) = M − (h − p)² : 4 zwischen 8 und 20 Uhr; ganze Werte bei geraden Abständen zu p."""
    M, p = R.randint(18, 27), R.choice([13, 14, 15])
    k = [M - Fr(p * p, 4), Fr(p, 2), Fr(-1, 4)]
    T = lambda h: M - Fr((h - p) ** 2, 4)
    gr = _KO(x=[8, 20], y=[M - 10, M + 2], graphen=[{'art': 'poly', 'k': [float(c) if Fr(c).denominator != 1 else int(c) for c in k], 'name': 'T', 'bereich': [8, 20]}],
             name_x='Uhr', name_y='°C', schritt_y=1, schritt_x=1)
    return M, p, T, gr


def g_sachzusammenhang(R, st):
    if st == 1:
        art = _wahl(R, 1, ['preis', 'temp_lesen', 'term'])
        if art == 'preis':
            wer, e1, e2, g, p, xs = _tarif(R)
            x = R.choice(xs)
            return Z(f'{wer} kostet {eur(g)} € Grundgebühr und {eur(p)} € je {e1}. Wie viel Euro kosten {x} {e2 if x != 1 else e1}?', g + p * x, f'{cz(g)} + {cz(p)} * {x}',
                     f'Grundgebühr plus {x} · {eur(p)} €: {eur(g)} € + {eur(p * x)} € = {eur(g + p * x)} €.', 'Die Grundgebühr zahlt man immer, dazu der Preis je Einheit mal die Anzahl.',
                     einheit='€')
        if art == 'temp_lesen':
            M, p, T, gr = _temp(R)
            h = R.choice([x for x in range(8, 21) if (x - p) % 2 == 0 and x != p])
            return Z(f'Der Graph zeigt den Temperaturverlauf an einem Sommertag. Wie warm war es um {h} Uhr?', T(h), f'{M} - ({h} - {p})**2 / 4',
                     f'Bei {h} Uhr senkrecht hoch zum Graphen, dann waagrecht zur Temperatur-Achse: {zt(T(h))} °C.', 'Suche die Uhrzeit unten auf der Achse und gehe senkrecht bis zum Graphen.',
                     einheit='°C') | {'f': {'text': f'Der Graph zeigt den Temperaturverlauf an einem Sommertag. Wie warm war es um {h} Uhr?', 'grafik': gr}}
        wer, e1, e2, g, p, xs = _tarif(R)
        return LK.A(f'{wer} kostet {eur(g)} € Grundgebühr und {eur(p)} € je {e1}. Welcher Term gibt die Kosten K in € für x {e2} an?', f'K(x) = {eur(g)} + {eur(p)} · x',
                    [f'K(x) = {eur(p)} + {eur(g)} · x', f'K(x) = ({eur(g)} + {eur(p)}) · x', f'K(x) = {eur(p)} · x'],
                    f'Fest sind {eur(g)} €, für jede Einheit kommen {eur(p)} € dazu: K(x) = {eur(g)} + {eur(p)} · x. Nur dieser Term ergibt bei x = 0 die Grundgebühr.',
                    'Welcher Betrag ist fest, welcher wird mit der Anzahl x multipliziert?')
    if st == 2:
        art = _wahl(R, 2, ['rueck', 'tab_term', 'temp_aenderung', 'temp_max'])
        if art == 'rueck':
            wer, e1, e2, g, p, xs = _tarif(R)
            x = R.choice(xs)
            k = g + p * x
            return Z(f'{wer} kostet {eur(g)} € Grundgebühr und {eur(p)} € je {e1}. Die Rechnung beträgt {eur(k)} €. Wie viele {e2} waren es?', x, f'({cz(k)} - {cz(g)}) / {cz(p)}',
                     f'Ohne Grundgebühr: {eur(k)} € − {eur(g)} € = {eur(k - g)} €. Geteilt durch {eur(p)} €: {x} {e2 if x != 1 else e1}.',
                     'Ziehe zuerst die Grundgebühr ab. Dann teile durch den Preis je Einheit.')
        if art == 'tab_term':
            wer, e1, e2, g, p, xs = _tarif(R)
            if p.denominator != 1 or g.denominator != 1: return g_sachzusammenhang(R, st)
            x0 = R.randint(1, 3)
            tab = {'typ': 'tabelle', 'kopf': [f'{e2} (x)'] + [str(x0 + i) for i in range(4)], 'zeilen': [['Kosten in €'] + [eur(g + p * (x0 + i)) for i in range(4)]]}
            return L(f'Die Tabelle gehört zu einem Tarif mit Grundgebühr und festem Preis je {e1}. Gib den Term an.', 'K(x) = □ + □ · x', [g, p], [cz(g), cz(p)],
                     f'Je {e1} mehr steigen die Kosten um {eur(p)} €: Preis je Einheit {eur(p)}. Rückwärts bis x = 0: {eur(g + p * x0)} − {x0} · {eur(p)} = {eur(g)} € Grundgebühr. '
                     f'K(x) = {eur(g)} + {eur(p)} · x.', 'Um wie viel steigen die Kosten von Spalte zu Spalte? Rechne dann zurück bis x = 0.',
                     hinweis='Zwei ganze Zahlen eintragen.') | {'f': {'text': f'Die Tabelle gehört zu einem Tarif mit Grundgebühr und festem Preis je {e1}. Gib den Term an.',
                                                                      'schablone': 'K(x) = □ + □ · x', 'hinweis': 'Zwei ganze Zahlen eintragen.', 'grafik': tab}}
        M, p, T, gr = _temp(R)
        if art == 'temp_max':
            t = f'Der Graph zeigt den Temperaturverlauf an einem Tag. Um wie viel Uhr war es am wärmsten?'
            return Z(t, p, f'{p}', f'Der höchste Punkt des Graphen liegt bei {p} Uhr ({M} °C). Davor steigt, danach sinkt die Temperatur.',
                     'Suche den höchsten Punkt des Graphen und lies unten die Uhrzeit ab.', einheit='Uhr') | {'f': {'text': t, 'grafik': gr}}
        h1 = R.choice([x for x in range(8, 13) if (x - p) % 2 == 0])
        h2 = R.choice([x for x in range(h1 + 2, p + 1) if (x - p) % 2 == 0] or [p])
        t = f'Der Graph zeigt den Temperaturverlauf an einem Tag. Um wie viel Grad ist es von {h1} Uhr bis {h2} Uhr wärmer geworden?'
        return Z(t, T(h2) - T(h1), f'({M} - ({h2} - {p})**2 / 4) - ({M} - ({h1} - {p})**2 / 4)',
                 f'Abgelesen: {h1} Uhr {zt(T(h1))} °C, {h2} Uhr {zt(T(h2))} °C. Unterschied: {zt(T(h2))} − {zt(T(h1))} = {zt(T(h2) - T(h1))} Grad.',
                 'Lies beide Temperaturen ab und bilde den Unterschied.', einheit='°C') | {'f': {'text': t, 'grafik': gr}}
    art = _wahl(R, 3, ['gleich', 'aussage', 'guenstiger'])
    if art in ('gleich', 'guenstiger'):
        for _ in range(200):
            wer, e1, e2, g, p, xs, e3, kurz = _tarif(R, voll=True)
            g2 = g + R.choice([2, 3, 4, 5, 6, 10])
            p2 = p - R.choice([Fr(1, 2), Fr(1), Fr(5, 100), Fr(1, 10)])
            if p2 <= 0: continue
            x = (g2 - g) / (p - p2)
            if x.denominator == 1 and xs[0] <= x <= xs[-1]: break
        else:
            return g_sachzusammenhang(R, st)
        tarif = f'Zwei {kurz}: A kostet {eur(g)} € Grundgebühr und {eur(p)} € je {e1}, B kostet {eur(g2)} € Grundgebühr und {eur(p2)} € je {e1}.'
        if art == 'gleich':
            return Z(f'{tarif} Bei wie vielen {e3} kosten beide gleich viel?', x, f'({cz(g2)} - {cz(g)}) / ({cz(p)} - {cz(p2)})',
                     f'B startet {eur(g2 - g)} € teurer, spart aber {eur(p - p2)} € je {e1}. Gleich teuer nach {eur(g2 - g)} : {eur(p - p2)} = {zt(x)} {e2}. '
                     f'Probe: {eur(g + p * x)} € = {eur(g2 + p2 * x)} €.', 'Wie viel teurer startet B, und wie viel spart B je Einheit?')
        x2 = x + R.choice([2, 4, 5]) * (1 if e1 != 'kWh' else 20)
        d = (g + p * x2) - (g2 + p2 * x2)
        return Z(f'{tarif} Um wie viel Euro ist B bei {zt(x2)} {e3} günstiger?', d, f'({cz(g)} + {cz(p)} * {zt(x2)}) - ({cz(g2)} + {cz(p2)} * {zt(x2)})',
                 f'A: {eur(g)} + {eur(p)} · {zt(x2)} = {eur(g + p * x2)} €. B: {eur(g2)} + {eur(p2)} · {zt(x2)} = {eur(g2 + p2 * x2)} €. Unterschied {eur(d)} €.',
                 'Rechne beide Rechnungen aus und vergleiche.', einheit='€')
    M, p, T, gr = _temp(R)
    hs = [x for x in range(8, 21) if (x - p) % 2 == 0 and x != p]
    a, b = R.sample([x for x in hs if x < p], 1)[0], R.sample([x for x in hs if x > p], 1)[0]
    richtig = f'Zwischen {p} Uhr und 20 Uhr sinkt die Temperatur.'
    falsch = [f'Zwischen {a} Uhr und {p} Uhr sinkt die Temperatur.', f'Um {b} Uhr ist es wärmer als um {p} Uhr.', f'Die höchste Temperatur beträgt {M + 2} °C.']
    return LK.A('Der Graph zeigt den Temperaturverlauf an einem Tag. Welche Aussage stimmt?', richtig, falsch,
                f'Der Graph steigt bis {p} Uhr (höchster Wert {M} °C) und fällt danach bis 20 Uhr. Deshalb stimmt nur: {richtig}',
                'Wo steigt der Graph, wo fällt er? Wo ist sein höchster Punkt?', grafik=gr)


_GR0 = _KO(x=[8, 20], y=[10, 22], graphen=[{'art': 'poly', 'k': [-29, 7, -0.25], 'name': 'T', 'bereich': [8, 20]}], name_x='Uhr', name_y='°C', schritt_y=1, schritt_x=1)
_FEST = [
    lambda: Z('Stromtarif A: 9 € Grundpreis im Monat und 0,30 € je kWh. Stromtarif B: 15 € Grundpreis und 0,25 € je kWh. Bei welchem Monatsverbrauch kosten beide gleich viel?',
              120, '(15 - 9) / (30/100 - 25/100)', 'B kostet 6 € mehr Grundpreis, ist aber je kWh 0,05 € billiger. 6 : 0,05 = 120 kWh. '
              'Probe: A: 9 + 0,30 · 120 = 45 €; B: 15 + 0,25 · 120 = 45 €.', 'Wie viel teurer startet B? Wie viel spart B je kWh?', einheit='kWh') | {'_art': _P},
    lambda: Z('Stromtarif A: 9 € Grundpreis und 0,30 € je kWh, Tarif B: 15 € Grundpreis und 0,25 € je kWh. Eine Familie verbraucht 200 kWh im Monat. '
              'Um wie viel Euro ist der günstigere Tarif billiger?', 4, '(9 + 30/100 * 200) - (15 + 25/100 * 200)',
              'A: 9 + 0,30 · 200 = 69 €. B: 15 + 0,25 · 200 = 65 €. B ist um 4 € billiger.', 'Berechne beide Monatsrechnungen.', einheit='€') | {'_art': _P},
    lambda: LK.A('Die Zuordnung Uhrzeit → Temperatur im Bild ist eine Funktion. Ist auch die Zuordnung Temperatur → Uhrzeit eine Funktion?',
                 'Nein: Zu 16 °C gehören zwei Uhrzeiten, 10 Uhr und 18 Uhr.',
                 ['Ja: Man vertauscht nur Eingabe und Ausgabe.', 'Ja: Zu jeder Uhrzeit gibt es genau eine Temperatur.', 'Nein: Temperaturen können negativ sein.'],
                 'Eine Funktion braucht zu jeder Eingabe genau eine Ausgabe. Eine waagrechte Linie bei 16 °C trifft den Graphen zweimal: um 10 Uhr und um 18 Uhr. '
                 'Rückwärts ist die Zuordnung also nicht eindeutig.', 'Gehe von einer Temperatur waagrecht zum Graphen. Wie oft triffst du ihn?', grafik=_GR0, art=_K),
]
LK.karte(_KARTE, nach='*', abschnitt='Graph und Nullstellen', gen=g_sachzusammenhang, fest=_FEST)
baue = mit_luecken(baue, LK)
# ---- LÜCKEN ENDE ----


# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Kl. 8, siehe _durchsicht_kl8.py) ----
from _durchsicht_kl8 import Durchsicht, mit_durchsicht  # noqa: E402

DS = Durchsicht('funktionen.grundbegriffe', 19_8_1)
# eindeutig: reine Paarlisten sind Stufe 1; „Schüler ↔ Geburtstag“ ist derselbe Gedanke wie die Alltagspaare der Stufe 2; Parabel-Graph = Standard
for _t in ['Ist die Zuordnung (8 | 9), (−5 | 1), (4 | 0), (0 | −7), (5 | 6), (0 | −4), (−3 | 9) eine Funktion?',
           'Ist die Zuordnung (0 | 4), (7 | 5), (3 | 1), (6 | −4), (−3 | 3), (−6 | −3) eine Funktion?',
           'Ist die Zuordnung (3 | −1), (4 | 0), (−6 | 0), (2 | 7) eine Funktion?']:
    DS.stufe('eindeutig', _t, 1)
DS.stufe('eindeutig', 'Jedem Schüler wird sein Geburtstag zugeordnet. Und umgekehrt: Jedem Geburtstag wird ein Schüler zugeordnet. Welche Zuordnungen sind Funktionen?', 2)
DS.stufe('eindeutig', 'Ist der gezeichnete Graph der Graph einer Funktion?', 2)
DS.stufen('eindeutig', 'S1 Paarliste prüfen; S2 teils dieselbe Paarliste, teils Alltag; S3 teils Alltag wie S2',
          'S1 Paarliste prüfen; S2 Alltagszuordnungen in beide Richtungen, Graph, „Welche ist keine?“; S3 Begründung bewerten, Kreis, Anzahl der Werte für a')
# funktionswert: Einsetzen in einen linearen Term ist kein anderer Gedanke → Stufe 2; neue Stufe 3 (Parameter, Fehler finden)
DS.stufe('funktionswert', 'Berechne f(−2) für f(x) = −x² + x.', 2)
DS.stufe('funktionswert', 'Berechne f(−4) für f(x) = 3x + 5,5.', 2)
DS.stufe('funktionswert', 'Berechne f(−0,5) für f(x) = 2,5x − 5.', 2)
DS.stufe('funktionswert', 'f(x) = −x² + 4. Berechne f(2) − f(−3).', 2)
DS.neu('funktionswert', 3, DS.Z('Für f(x) = a · x + 3 gilt f(2) = 11. Bestimme a.', 4, '(11 - 3) / 2',
                                'Einsetzen: a · 2 + 3 = 11. Also 2a = 8 und a = 4. Probe: f(2) = 4 · 2 + 3 = 11.',
                                'Setze x = 2 ein und schreibe die Gleichung a · 2 + 3 = 11 auf.'))
DS.neu('funktionswert', 3, DS.A('Lea berechnet f(−3) für f(x) = −x² + 2 so: −3² + 2 = −9 + 2 = −7. Ihr Freund meint, die Klammer fehlt. Was stimmt?',
                                'Lea hat richtig gerechnet: f(−3) = −(−3)² + 2 = −9 + 2 = −7.',
                                ['Richtig ist (−3)² + 2 = 11.', 'Richtig ist −(−3)² + 2 = 9 + 2 = 11.', 'Richtig ist −(−3) · 2 + 2 = 8.'],
                                'Das Minus vor x² bleibt vor dem Quadrat: −(−3)² = −9. Lea hat die Klammer nicht geschrieben, aber zufällig richtig gerechnet: −3² ist auch −9. Ergebnis −7.',
                                'Rechne sauber mit Klammer: −(−3)². Was kommt heraus?'))
DS.stufen('funktionswert', 'S1 linear einsetzen; S2 quadratisch einsetzen; S3 teils wieder nur einsetzen',
          'S1 linear einsetzen; S2 quadratisch, Brüche, negative Dezimalzahlen; S3 Tabellenkalkulation, Parameter, f(a) = f(a + 1), Fehler finden')
# stelle: einfache lineare Gleichungen auf Stufe 3 → 1/2
DS.stufe('stelle', 'Für welches x ist f(x) = 4, wenn f(x) = 2/x?', 2)
DS.stufe('stelle', 'Für welches x gilt f(x) = 21, wenn f(x) = 2,5x − 9?', 2)
DS.stufe('stelle', 'Für welches x gilt f(x) = −33, wenn f(x) = 3x − 3?', 1)
DS.stufen('stelle', 'S1 lineare Gleichung; S2 Klammer, a/x, „für kein x“; S3 teils dieselbe lineare Gleichung',
          'S1 lineare Gleichung; S2 Klammer, a/x, „für kein x“; S3 konstante Funktion, Parameter c, Bruchterm, zwei Stellen, Sachaufgabe')
# graph_lesen: f(a) ablesen ist Stufe 1, y → x ablesen ist Stufe 2
DS.stufe('graph_lesen', 'Lies am Graphen ab: f(−2) = ?', 1, enthaelt='"wert": 6')
DS.stufe('graph_lesen', 'Lies am Graphen ab: An welcher Stelle hat f den Wert −1? Gib den Punkt an.', 2, enthaelt='"werte": [-1, -1]')
DS.stufe('graph_lesen', 'Lies am Graphen ab: An welcher Stelle hat f den Wert 2? Gib den Punkt an.', 2, enthaelt='"werte": [-2, 2]')
DS.stufe('graph_lesen', 'Für welche x gilt f(x) = 1? Lies am Graphen ab (kleinere Stelle zuerst).', 2)
DS.stufen('graph_lesen', 'S1 f(a) ablesen; S2 x zu y ablesen; S3 zur Hälfte dasselbe wie S1/S2',
          'S1 f(a) ablesen; S2 x zu y ablesen (auch zwei Stellen); S3 Bereich unterhalb der Achse, Sachgraph Badewanne, c mit genau einer Lösung')
# nullstellen: lineare Nullstellen ohne Besonderheit → Stufe 1
DS.stufe('nullstellen', 'Berechne die Nullstelle von f(x) = −6x + 18.', 1)
DS.stufe('nullstellen', 'Berechne die Nullstelle von f(x) = 2x + 6.', 1)
DS.stufen('nullstellen', 'S1/S2 teils dieselbe lineare Nullstelle; S3 Bruchterm, Produkt',
          'S1 lineare Nullstelle; S2 Produktform, „keine“, Sachaufgabe; S3 Bruchterm, Achsenpunkte, Parameter b, gekürzter Bruchterm')
# punkt_graph: lineare Punktprobe ist Stufe 1; vier gleiche k-Aufgaben in Reihe → zwei ersetzt
DS.stufe('punkt_graph', 'Welcher Punkt liegt auf dem Graphen von f(x) = −2x − 7?', 1)
DS.stufe('punkt_graph', 'Welcher Punkt liegt auf dem Graphen von f(x) = 5x + 2?', 1)
DS.ersetze('punkt_graph', 'Der Punkt P(−5 | −26) liegt auf dem Graphen von f(x) = k · x + 4. Bestimme k.', DS.A(
    'Tom prüft, ob P(−2 | 7) auf dem Graphen von f(x) = −3x + 1 liegt. Er rechnet −3 · 7 + 1 = −20 und sagt: „−20 ≠ −2, also nein.“ Was stimmt?',
    'Tom hat x und y vertauscht. f(−2) = −3 · (−2) + 1 = 7: P liegt auf dem Graphen.',
    ['Tom hat recht, P liegt nicht auf dem Graphen.', 'Tom hat x und y vertauscht. f(−2) = 5, also liegt P nicht darauf.', 'Man muss 7 und −2 addieren: 5 ≠ 1, also nein.'],
    'In P(−2 | 7) ist −2 der x-Wert. Einsetzen: f(−2) = −3 · (−2) + 1 = 6 + 1 = 7. Das ist genau der y-Wert, also liegt P auf dem Graphen.',
    'Welche Zahl in P(−2 | 7) ist x? Setze nur diese ein.'))
DS.ersetze('punkt_graph', 'Der Punkt P(1 | −1) liegt auf dem Graphen von f(x) = k · x + 5. Bestimme k.', DS.Z(
    'Der Punkt Q(b | 10) liegt auf dem Graphen von f(x) = 2x² + 2. Seine x-Koordinate ist positiv. Bestimme b.', 2, '2',
    'Einsetzen: 2b² + 2 = 10, also 2b² = 8 und b² = 4. Es gibt b = 2 und b = −2; positiv ist b = 2. Probe: 2 · 2² + 2 = 10.',
    'Setze den y-Wert gleich: 2b² + 2 = 10. Welche Zahl ergibt im Quadrat 4?'))
DS.stufen('punkt_graph', 'S1 Punktprobe; S2 teils dieselbe Punktprobe; S3 viermal k bestimmen',
          'S1 Punktprobe linear; S2 quadratisch, Hyperbel, oberhalb/unterhalb; S3 Parameter k, Fehler finden, x zu gegebenem y, Definitionslücke, m und t aus zwei Punkten')
DS.stufen('mengen', 'S1 D von a/(x − b); S2 W aus endlicher D; S3 D mit zwei Lücken, Aussagen über W, Sachkontext, Parameter')
DS.stufen('wertetabelle', 'S1 y einsetzen; S2 quadratisch einsetzen und x rückwärts; S3 Term zur Tabelle, Sachtabelle, Parameter a')
DS.stufen('sachzusammenhang', 'S1 Tarif einsetzen, Temperatur ablesen, Term wählen; S2 rückwärts, Term aus Tabelle, Änderung ablesen; S3 Tarifvergleich, Aussage zur Kurve, Umkehrung keine Funktion')
baue = mit_durchsicht(baue, DS)
# ---- DURCHSICHT ENDE ----

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Was ist eine Funktion?', ['eindeutig', 'mengen']), ('Mit dem Term rechnen', ['funktionswert', 'stelle', 'wertetabelle', 'graph_lesen']),
          ('Graph und Nullstellen', ['nullstellen', 'punkt_graph'])],
         'Funktionen als eindeutige Zuordnungen erkennen; mit Funktionsterm, Wertetabelle und Graph arbeiten; Definitions- und Wertemenge sowie Nullstellen bestimmen.',
         ['Funktion: Jedem x genau ein y.', 'f(a) berechnen: a einsetzen. f(x) = b lösen: x gesucht.',
          'Nullstelle: f(x) = 0. P(a | b) liegt auf dem Graphen, wenn f(a) = b.'],
         offen=['„Ist dieser Graph eine Funktion?“: Gebaut sind Punktwolken (zwei Punkte übereinander) als Gegenbeispiel und Parabeln als Beispiel für „ja“. '
                'Einen Kreis kann die App inzwischen zeichnen (koordinaten.kreise); Aufgaben mit dem Kreis als Gegenbeispiel sind noch nicht gebaut (möglich als Ergänzung). '
                'Eine liegende Parabel gibt es nicht als Graph-Art.'])
