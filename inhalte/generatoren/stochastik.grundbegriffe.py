#!/usr/bin/env python3
"""Thema stochastik.grundbegriffe – Zufall und Laplace (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, L, Z, baue, bruch, ist_endlich, mit_bild, runde, sicher_rundbar, zt  # noqa: E402

META = {'thema_schluessel': 'stochastik.grundbegriffe', 'thema_id': 61, 'block_id': 92, 'klasse': {'gym_by': 8, 'rs_by': 9, 'ib_myp': 2}}

ETAPPEN = [
    {'lernziel': 'begriffe', 'titel': 'Ergebnis, Ergebnisraum, Ereignis',
     'regel': 'Ein ⟦Zufallsexperiment⟧ hat mehrere mögliche ⟦Ergebnisse⟧; welches eintritt, ist nicht vorhersagbar. Alle Ergebnisse zusammen bilden den ⟦Ergebnisraum Ω⟧. Ein ⟦Ereignis⟧ ist eine Teilmenge von Ω.',
     'schritte': ['Würfeln: Ω = {1; 2; 3; 4; 5; 6}', 'Ereignis E: „Augenzahl größer als 4“', '⟦E = {5; 6}⟧'],
     'fehler': 'Zweimal eine Münze werfen hat nicht 3 Ergebnisse (WW, WZ, ZZ). Stell dir eine 1-€- und eine 2-€-Münze vor: „1 € Wappen, 2 € Zahl“ ist etwas anderes als „1 € Zahl, 2 € Wappen“. Der Baum zeigt ⟦vier⟧ Wege: Ω = {WW; WZ; ZW; ZZ}.',
     'bild': {'typ': 'baum', 'aeste': [{'text': 'W', 'p': '1/2', 'aeste': [{'text': 'WW', 'p': '1/2'}, {'text': 'WZ', 'p': '1/2'}]},
                                       {'text': 'Z', 'p': '1/2', 'aeste': [{'text': 'ZW', 'p': '1/2'}, {'text': 'ZZ', 'p': '1/2'}]}]},
     '_verbot': ['Augenzahl größer als 4']},
    {'lernziel': 'rel_haeufigkeit', 'titel': 'Relative Häufigkeit',
     'regel': 'Die ⟦absolute Häufigkeit⟧ zählt, wie oft ein Ergebnis eintrat. Die ⟦relative Häufigkeit⟧ ist der Anteil: ⟦absolute Häufigkeit : Anzahl der Versuche⟧. Sie liegt zwischen 0 und 1.',
     'schritte': ['50 Würfe, 12-mal eine Sechs', 'relative Häufigkeit = 12 : 50', '= ⟦0,24 = 24 %⟧'],
     'fehler': 'Die relative Häufigkeit von 12 Sechsen bei 50 Würfen ist nicht 12. Das ist die ⟦absolute⟧ Häufigkeit. Relativ heißt: im Verhältnis zur Gesamtzahl.',
     '_verbot': ['50 Würfe, 12-mal']},
    {'lernziel': 'laplace', 'titel': 'Laplace-Wahrscheinlichkeit',
     'regel': 'Sind alle Ergebnisse ⟦gleich wahrscheinlich⟧ (Laplace-Experiment), gilt: ⟦P(E) = Anzahl der günstigen Ergebnisse : Anzahl aller Ergebnisse⟧.',
     'schritte': ['Urne: 3 rote, 5 blaue, 2 grüne Kugeln, eine wird gezogen.', 'Günstig für „rot“: 3, möglich: 10', '⟦P(rot) = 3/10 = 0,3⟧'],
     'fehler': 'P(rot) ist nicht 3/7 (rot zu nicht-rot). Im Nenner steht die Anzahl ⟦aller⟧ Kugeln: 3/10.',
     '_verbot': ['3 rote, 5 blaue, 2 grüne']},
    {'lernziel': 'laplace_pruefen', 'titel': 'Ist es ein Laplace-Experiment?',
     'regel': 'Ein Experiment ist nur dann ein ⟦Laplace-Experiment⟧, wenn ⟦alle Ergebnisse gleich wahrscheinlich⟧ sind. Ungleich große Glücksradfelder oder eine Reißzwecke sind kein Laplace-Experiment.',
     'schritte': ['Glücksrad: Feld A 180°, Feld B 90°, Feld C 90°', 'A ist doppelt so groß wie B und C.', '⟦Kein⟧ Laplace-Experiment: P(A) = 1/2, nicht 1/3.'],
     'fehler': 'Drei mögliche Ergebnisse bedeuten nicht automatisch P = 1/3 für jedes. Das gilt nur, wenn sie ⟦gleich wahrscheinlich⟧ sind.',
     'bild': {'typ': 'kreisdiagramm', 'einheit': '°', 'werte': [{'name': 'A', 'wert': 180}, {'name': 'B', 'wert': 90}, {'name': 'C', 'wert': 90}], 'zahlen': True},
     '_verbot': ['180°, Feld B 90°']},
    {'lernziel': 'gegenereignis', 'titel': 'Das Gegenereignis',
     'regel': 'Das ⟦Gegenereignis⟧ Ē tritt genau dann ein, wenn E ⟦nicht⟧ eintritt. Es gilt ⟦P(Ē) = 1 − P(E)⟧.',
     'schritte': ['E: „Sechs würfeln“, P(E) = 1/6', 'Ē: „keine Sechs“', '⟦P(Ē) = 1 − 1/6 = 5/6⟧'],
     'fehler': 'Das Gegenereignis zu „mindestens eine Sechs“ ist nicht „höchstens eine Sechs“, sondern ⟦„keine Sechs“⟧.',
     '_verbot': ['„Sechs würfeln“']},
    {'lernziel': 'grosse_zahlen', 'titel': 'Gesetz der großen Zahlen',
     'regel': 'Bei ⟦vielen⟧ Wiederholungen nähert sich die relative Häufigkeit meist der ⟦Wahrscheinlichkeit⟧ an. Bei n Versuchen erwartet man etwa ⟦n · P(E)⟧ Treffer – genau vorhersagen kann man es nie.',
     'schritte': ['Münze 1000-mal werfen, P(Wappen) = 0,5', 'Erwartet: 1000 · 0,5 = ⟦etwa 500-mal Wappen⟧', 'Tatsächlich z. B. 488 oder 513 – nicht genau 500.'],
     'fehler': 'Kam fünfmal keine Sechs, ist die Sechs beim nächsten Wurf ⟦nicht⟧ wahrscheinlicher. Der Würfel hat kein Gedächtnis: P bleibt 1/6.'},
]


# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'begriffe': {
  'einstieg': 'Beim Spieleabend würfelt Lena. Sie weiß vorher nicht, welche Zahl kommt – aber sie weiß, welche Zahlen überhaupt möglich sind: 1 bis 6. Ein Vorgang, dessen Ausgang man nicht vorhersagen kann, heißt ⟦Zufallsexperiment⟧.',
  'woerter': [['Zufallsexperiment', 'ein Vorgang mit mehreren möglichen Ausgängen, die man nicht vorhersagen kann'], ['Ergebnis', 'ein möglicher Ausgang, z. B. die 5'],
              ['Ergebnisraum Ω', 'alle möglichen Ergebnisse zusammen; Ω ist der griechische Buchstabe Omega'], ['Ereignis E', 'eine Auswahl von Ergebnissen, z. B. „größer als 4“'],
              ['{ ; }', 'geschweifte Klammern: darin stehen die Ergebnisse einer Menge']],
  'schritte': ['Lena würfelt. Möglich sind die Zahlen 1 bis 6: Ω = {1; 2; 3; 4; 5; 6}.', 'Sie gewinnt, wenn die Augenzahl größer als 4 ist. Das ist das Ereignis E.',
               'Größer als 4 sind nur die 5 und die 6: ⟦E = {5; 6}⟧.'],
  'regel': 'So beschreibst du ein ⟦Zufallsexperiment⟧: Erst alle möglichen ⟦Ergebnisse⟧ in Ω aufschreiben. Dann für ein ⟦Ereignis⟧ die passenden Ergebnisse heraussuchen.'},
 'rel_haeufigkeit': {
  'einstieg': 'Lena hat 50-mal gewürfelt und 12-mal eine Sechs bekommen. Ist das viel? Das sieht man erst, wenn man die 12 mit den 50 Würfen vergleicht. Diesen Anteil nennt man ⟦relative Häufigkeit⟧.',
  'woerter': [['absolute Häufigkeit', 'wie oft etwas eingetreten ist, z. B. 12-mal'], ['relative Häufigkeit', 'der Anteil: absolute Häufigkeit geteilt durch die Anzahl der Versuche'],
              ['Anteil', 'als Bruch, Dezimalzahl oder in Prozent, z. B. 0,24 = 24 %']],
  'schritte': ['Lena würfelt 50-mal und bekommt 12-mal eine Sechs.', 'Die 12 ist die absolute Häufigkeit. Für den Anteil teilt man durch die Anzahl der Würfe: 12 : 50.',
               'Das ergibt ⟦0,24 = 24 %⟧.'],
  'regel': 'So berechnest du die ⟦relative Häufigkeit⟧: ⟦absolute Häufigkeit : Anzahl der Versuche⟧. Das Ergebnis liegt immer zwischen 0 und 1.'},
 'laplace': {
  'einstieg': 'Auf dem Schulfest gibt es eine Lostrommel mit 3 roten, 5 blauen und 2 grünen Kugeln. Alle Kugeln sind gleich groß und gut gemischt, also hat jede dieselbe Chance. Dann kann man die Chance für „rot“ ausrechnen. Diese Zahl heißt ⟦Wahrscheinlichkeit⟧.',
  'woerter': [['Wahrscheinlichkeit P', 'eine Zahl zwischen 0 und 1, die angibt, wie wahrscheinlich ein Ereignis ist'], ['P(rot)', 'die Wahrscheinlichkeit für das Ereignis „rot“'],
              ['Laplace-Experiment', 'ein Zufallsexperiment, bei dem alle Ergebnisse gleich wahrscheinlich sind'], ['günstige Ergebnisse', 'die Ergebnisse, bei denen das Ereignis eintritt'],
              ['Urne', 'ein Gefäß mit Kugeln, aus dem man zufällig zieht']],
  'schritte': ['In der Trommel sind 3 rote, 5 blaue und 2 grüne Kugeln; eine wird gezogen.', 'Günstig für „rot“ sind die 3 roten Kugeln.',
               'Möglich sind alle 3 + 5 + 2 = 10 Kugeln. Also ist ⟦P(rot) = 3/10 = 0,3⟧.'],
  'regel': 'So berechnest du eine ⟦Laplace-Wahrscheinlichkeit⟧: ⟦P(E) = Anzahl der günstigen Ergebnisse : Anzahl aller Ergebnisse⟧. Das geht nur, wenn alle Ergebnisse gleich wahrscheinlich sind.'},
 'laplace_pruefen': {
  'einstieg': 'Auf dem Schulfest steht auch ein Glücksrad. Das Feld A ist halb so groß wie das ganze Rad, B und C sind kleiner. Es gibt drei Felder – aber hat jedes die Chance 1/3? Nur wenn alle Ergebnisse gleich wahrscheinlich sind, ist es ein ⟦Laplace-Experiment⟧.',
  'woerter': [['Laplace-Experiment', 'alle Ergebnisse haben dieselbe Wahrscheinlichkeit'], ['Mittelpunktswinkel', 'der Winkel eines Feldes an der Mitte des Rades'],
              ['Reißzwecke', 'ein Pin; er landet auf dem Kopf oder auf der Seite – nicht gleich oft']],
  'schritte': ['Glücksrad: Feld A hat 180°, Feld B 90°, Feld C 90°.', 'A ist doppelt so groß wie B und auch doppelt so groß wie C. Also bleibt der Zeiger öfter auf A stehen.',
               'Die Felder sind nicht gleich wahrscheinlich: ⟦kein⟧ Laplace-Experiment. Richtig ist P(A) = 180°/360° = 1/2, nicht 1/3.'],
  'regel': 'So prüfst du: Haben ⟦alle Ergebnisse dieselbe Chance⟧? Nur dann ist es ein ⟦Laplace-Experiment⟧. Sind Felder unterschiedlich groß, ist es keines.'},
 'gegenereignis': {
  'einstieg': 'Lena braucht beim Spiel keine Sechs, sonst muss sie zurück. Statt die Fälle „1, 2, 3, 4 oder 5“ zu zählen, kann sie rechnen: alles außer der Sechs. Das Ereignis „nicht E“ heißt ⟦Gegenereignis⟧.',
  'woerter': [['Gegenereignis Ē', 'tritt genau dann ein, wenn E nicht eintritt; gesprochen „E quer“'], ['1 − P(E)', 'der Rest bis 1, also bis zu 100 %'],
              ['mindestens eine', 'eine oder mehr'], ['keine', 'gar keine – das Gegenteil von „mindestens eine“']],
  'schritte': ['E heißt „Sechs würfeln“. Die Wahrscheinlichkeit ist P(E) = 1/6.', 'Das Gegenereignis Ē heißt „keine Sechs“.',
               'Beide zusammen ergeben immer 1. Also ist ⟦P(Ē) = 1 − 1/6 = 5/6⟧.'],
  'regel': 'So nutzt du das ⟦Gegenereignis⟧: Ist „nicht E“ leichter zu berechnen, rechne ⟦P(Ē) = 1 − P(E)⟧.'},
 'grosse_zahlen': {
  'einstieg': 'Wirft man eine Münze nur 10-mal, kommt vielleicht 7-mal Wappen. Wirft man sie 1000-mal, liegt der Anteil fast immer nahe bei der Hälfte. Je öfter man wiederholt, desto näher rückt die relative Häufigkeit an die Wahrscheinlichkeit. Das ist das ⟦Gesetz der großen Zahlen⟧.',
  'woerter': [['Gesetz der großen Zahlen', 'bei vielen Versuchen liegt die relative Häufigkeit meist nahe der Wahrscheinlichkeit'], ['n · P(E)', 'erwartete Anzahl der Treffer bei n Versuchen'],
              ['erwarten', 'ungefähr damit rechnen – es ist keine sichere Vorhersage']],
  'schritte': ['Eine Münze wird 1000-mal geworfen. P(Wappen) = 0,5.', 'Man erwartet 1000 · 0,5 = ⟦etwa 500-mal Wappen⟧.',
               'Tatsächlich kommt z. B. 488 oder 513 heraus. Der Zufall bleibt – nur der Anteil liegt nahe bei 0,5.'],
  'regel': 'So schätzt du: Bei n Versuchen erwartest du etwa ⟦n · P(E)⟧ Treffer. Je ⟦mehr⟧ Versuche, desto näher liegt die relative Häufigkeit meist an der ⟦Wahrscheinlichkeit⟧. Genau vorhersagen kann man es nie.'},
}

for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))
# ---- KLAR ENDE ----


def frac_opts(p, guenstig, alle):
    """Richtige Wahrscheinlichkeit als Bruch + typische Fehler."""
    f = [bruch(Fr(guenstig, max(1, alle - guenstig))) if alle - guenstig else '1/2', bruch(1 - p) if p != Fr(1, 2) else '1/3',
         bruch(Fr(alle - guenstig + 1, alle)) if Fr(alle - guenstig + 1, alle) != p else '2/3', f'{guenstig}/{alle + 1}']
    return [x for x in f if x != bruch(p)]


def g_begriffe(R, st):
    if st == 1:
        art = R.choice(['wuerfel', 'rad', 'urne', 'muenze2'])
        if art == 'wuerfel':
            n = R.choice([4, 6, 8, 10, 12, 20])
            return Z(f'Ein Spielwürfel hat {n} gleich große Flächen mit den Zahlen 1 bis {n}. Wie viele Ergebnisse hat der Ergebnisraum beim einmaligen Werfen?', n, f'{n}',
                     f'Ω = {{1; 2; …; {n}}}: {n} Ergebnisse.', 'Zähle, welche Zahlen oben liegen können.')
        if art == 'rad':
            n = R.randint(3, 12)
            return Z(f'Ein Glücksrad hat {n} Felder mit den Nummern 1 bis {n}. Wie viele Ergebnisse hat der Ergebnisraum bei einer Drehung?', n, f'{n}',
                     f'Jede Nummer ist ein Ergebnis: {n} Ergebnisse.', 'Jedes Feld ist ein mögliches Ergebnis.')
        if art == 'urne':
            farben = R.sample(['rot', 'blau', 'grün', 'gelb', 'weiß', 'schwarz'], R.randint(2, 5))
            anz = [R.randint(1, 6) for _ in farben]
            return Z(f'In einer Urne liegen {", ".join(f"{a} {f}e" for a, f in zip(anz, farben))} Kugeln. Man zieht eine Kugel und notiert die Farbe. Wie viele Ergebnisse hat der Ergebnisraum?',
                     len(farben), f'{len(farben)}', f'Ergebnis ist die Farbe: Ω = {{{"; ".join(farben)}}}, also {len(farben)} Ergebnisse (nicht {sum(anz)}).',
                     'Notiert wird nur die Farbe – wie viele verschiedene Farben gibt es?')
        k = R.choice([2, 3])
        return Z(f'Eine Münze wird {k}-mal geworfen, die Reihenfolge wird notiert. Wie viele Ergebnisse hat der Ergebnisraum?', 2 ** k, f'2 ** {k}',
                 f'Bei jedem Wurf 2 Möglichkeiten: 2{"²" if k == 2 else "³"} = {2 ** k}.', 'Schreibe alle Möglichkeiten auf: WW, WZ, …')
    if st == 2:
        n = R.choice([6, 8, 10, 12])
        ereig = R.choice([('gerade Zahl', lambda x: x % 2 == 0), ('ungerade Zahl', lambda x: x % 2 == 1), ('Primzahl', lambda x: x in (2, 3, 5, 7, 11)),
                          ('Zahl größer als 4', lambda x: x > 4), ('Teiler von 12', lambda x: 12 % x == 0), ('Vielfaches von 3', lambda x: x % 3 == 0),
                          ('Zahl kleiner als 3', lambda x: x < 3)])
        E = [x for x in range(1, n + 1) if ereig[1](x)]
        r = '{' + '; '.join(map(str, E)) + '}'
        rest = [x for x in range(1, n + 1) if x not in E]
        f = ['{' + '; '.join(map(str, rest)) + '}', '{' + '; '.join(map(str, E[:-1] or rest[:1])) + '}', '{' + '; '.join(map(str, sorted(set(E + rest[:1])))) + '}']
        if ereig[0] == 'Primzahl': f[1] = '{' + '; '.join(map(str, [1] + E)) + '}'
        return A(R, f'Ein Würfel mit den Zahlen 1 bis {n} wird geworfen. Welche Menge beschreibt das Ereignis „{ereig[0]}“?', r, f,
                 f'Alle Ergebnisse aus Ω, die passen: {r}.', 'Gehe Ω = {1; …; ' + str(n) + '} durch und prüfe jede Zahl.')
    if R.random() < .35:
        E, ri, fa = R.choice([('{1; 2; 3}', 'Augenzahl kleiner als 4', ['Augenzahl ungerade', 'Augenzahl höchstens 2', 'Augenzahl größer als 3']),
                              ('{2; 3; 5}', 'Augenzahl ist eine Primzahl', ['Augenzahl ungerade', 'Augenzahl kleiner als 5', 'Augenzahl größer als 1']),
                              ('{1; 3; 5}', 'Augenzahl ungerade', ['Augenzahl kleiner als 5', 'Augenzahl ist eine Primzahl', 'Augenzahl gerade']),
                              ('{3; 6}', 'Augenzahl ist durch 3 teilbar', ['Augenzahl größer als 2', 'Augenzahl gerade', 'Augenzahl ist eine Primzahl']),
                              ('{5; 6}', 'Augenzahl mindestens 5', ['Augenzahl größer als 5', 'Augenzahl gerade', 'Augenzahl höchstens 5']),
                              ('{1; 2; 3; 6}', 'Augenzahl ist ein Teiler von 6', ['Augenzahl kleiner als 4', 'Augenzahl gerade', 'Augenzahl ist durch 3 teilbar'])])
        return A(R, f'Beim Werfen eines Spielwürfels (1 bis 6) ist E = {E}. Wie kann man E in Worten beschreiben?', ri, fa,
                 f'{E} sind genau die Zahlen von 1 bis 6, für die gilt: {ri}. Bei den anderen Beschreibungen fehlt eine Zahl oder es ist eine zu viel.',
                 'Prüfe jede Beschreibung mit allen Zahlen von 1 bis 6.')
    if R.random() < .5:
        r = 'Ω = {WW; WZ; ZW; ZZ}'
        return A(R, f'Zwei Münzen werden nacheinander geworfen ({R.choice(["1-€ und 2-€", "zwei gleiche Münzen", "eine Münze zweimal"])}). Welcher Ergebnisraum ist richtig?', r,
                 ['Ω = {WW; WZ; ZZ}', 'Ω = {W; Z}', 'Ω = {WW; ZZ}'], 'Erst Wappen, dann Zahl (WZ) und erst Zahl, dann Wappen (ZW) sind verschiedene Ergebnisse.',
                 'Achte auf die Reihenfolge der Würfe.')
    n1, n2 = R.choice([(6, 6), (4, 6), (6, 8), (4, 4), (2, 6), (3, 4)])
    return Z(f'Ein Würfel mit {n1} Flächen und einer mit {n2} Flächen werden geworfen, notiert wird das Zahlenpaar. Wie viele Ergebnisse gibt es?', n1 * n2, f'{n1} * {n2}',
             f'Zu jeder der {n1} Zahlen des ersten Würfels gibt es {n2} Zahlen des zweiten: {n1} · {n2} = {n1 * n2}.', 'Denke an eine Tabelle: Zeilen mal Spalten.')


def sechsen(R, n):
    """Realistische Anzahl Sechsen bei n Würfen eines fairen Würfels (zwischen 0,12 · n und 0,22 · n)."""
    lo, hi = max(1, int(Fr(12, 100) * n)), max(2, int(Fr(22, 100) * n))
    return R.randint(lo, hi)


def g_rel_haeufigkeit(R, st):
    n = R.choice([20, 25, 40, 50, 80, 100, 125, 200, 250, 400, 500, 1000])
    k = sechsen(R, n)
    h = Fr(k, n)
    if st == 2 and R.random() < .35:
        if R.random() < .5:
            anz = [R.randint(7, 13) for _ in range(6)]
            n_ = sum(anz)
            while Fr(1, n_).denominator % 3 == 0 or any(c in (3, 7, 11, 13) for c in [n_ % 100]) and False: break
            z = R.randint(1, 6)
            hz = Fr(anz[z - 1], n_)
            gr = {'typ': 'tabelle', 'kopf': ['Augenzahl', '1', '2', '3', '4', '5', '6'], 'zeilen': [['Anzahl'] + [str(a) for a in anz]]}
            if not (ist_endlich(hz) and len(zt(hz)) <= 6):
                return mit_bild(Z(f'Die Tabelle zeigt {n_} Würfe. Wie groß ist die relative Häufigkeit der {z} in Prozent? (Runde auf eine Nachkommastelle.)', runde(hz * 100, 1),
                                  f'round({anz[z - 1]} / {n_} * 100, 1)', f'Gesamt: {n_} Würfe. {anz[z - 1]} : {n_} ≈ {zt(runde(hz * 100, 1))} %.', 'Addiere erst alle Anzahlen.', '%', toleranz=0.1), gr)
            return mit_bild(Z(f'Die Tabelle zeigt {n_} Würfe. Wie groß ist die relative Häufigkeit der {z}? Gib sie als Dezimalzahl an.', hz, f'{anz[z - 1]} / {n_}',
                              f'Gesamt: {" + ".join(map(str, anz))} = {n_} Würfe. {anz[z - 1]} : {n_} = {zt(hz)}.', 'Addiere erst alle Anzahlen.'), gr)
        farben = R.sample(['Blau', 'Rot', 'Grün', 'Gelb', 'Lila'], 4)
        while True:
            w = [R.randint(2, 12) for _ in farben]
            if sum(w) in (20, 25, 40, 50): break
        f0 = R.randrange(4)
        gr = {'typ': 'saeulen', 'einheit': 'Kinder', 'werte': [{'name': f, 'wert': x} for f, x in zip(farben, w)], 'zahlen': True}
        return mit_bild(Z(f'Das Säulendiagramm zeigt die Lieblingsfarben einer Gruppe. Welcher Anteil der Kinder mag {farben[f0]} am liebsten? Gib ihn in Prozent an.', Fr(w[f0] * 100, sum(w)),
                          f'{w[f0]} / {sum(w)} * 100', f'Insgesamt {" + ".join(map(str, w))} = {sum(w)} Kinder. {w[f0]} : {sum(w)} = {zt(Fr(w[f0], sum(w)))} = {zt(Fr(w[f0] * 100, sum(w)))} %.',
                          'Zähle erst alle Kinder zusammen.', '%'), gr)
    if st == 1:
        return Z(f'Bei {n} Würfen kam {k}-mal die Sechs. Berechne die relative Häufigkeit als Dezimalzahl.', h, f'{k} / {n}', f'Relative Häufigkeit = {k} : {n} = {zt(h)}.',
                 'Absolute Häufigkeit durch Anzahl der Versuche.')
    if st == 2:
        if R.random() < .5:
            k = R.randint(int(Fr(55, 100) * n), int(Fr(68, 100) * n)); h = Fr(k, n)
            return Z(f'Eine Reißzwecke wurde {n}-mal geworfen und landete {k}-mal auf dem Kopf. Gib die relative Häufigkeit in Prozent an.', h * 100, f'{k} / {n} * 100',
                     f'{k} : {n} = {zt(h)} = {zt(h * 100)} %.', 'Erst den Anteil berechnen, dann mal 100.', '%')
        p = Fr(R.choice([5, 10, 12, 15, 20, 24, 25, 30, 35, 40, 45, 60, 75]), 100)
        if not (p * n).denominator == 1: return g_rel_haeufigkeit(R, st)
        return Z(f'Bei {n} Versuchen beträgt die relative Häufigkeit eines Ergebnisses {zt(p * 100)} %. Wie oft trat es ein?', p * n, f'{n} * {zt(p).replace(",", ".")}',
                 f'{zt(p * 100)} % von {n} = {zt(p)} · {n} = {zt(p * n)}.', 'Absolute Häufigkeit = relative Häufigkeit · Anzahl der Versuche.')
    n1, n2 = R.sample([20, 25, 40, 50, 80, 100, 200], 2)
    k1, k2 = sechsen(R, n1), sechsen(R, n2)
    k = k1 + k2; n = n1 + n2
    h = Fr(k, n)
    if not sicher_rundbar(h * 100, 1): return g_rel_haeufigkeit(R, st)
    glatt = ist_endlich(h * 100) and (',' not in zt(h * 100) or len(zt(h * 100).split(',')[-1]) <= 1)
    se = lambda x: f'{x} Sechs' if x == 1 else f'{x} Sechsen'
    if glatt:
        return Z(f'Zwei Gruppen werfen einen Würfel: Gruppe A {n1}-mal mit {se(k1)}, Gruppe B {n2}-mal mit {se(k2)}. Wie groß ist die relative Häufigkeit der Sechs insgesamt in Prozent?',
                 h * 100, f'{k} / {n} * 100', f'Insgesamt {k} Sechsen bei {n} Würfen: {k} : {n} = {zt(h * 100)} %.',
                 'Addiere die Sechsen und die Würfe – nicht die Prozentsätze mitteln.', '%')
    return Z(f'Zwei Gruppen werfen einen Würfel: Gruppe A {n1}-mal mit {se(k1)}, Gruppe B {n2}-mal mit {se(k2)}. Wie groß ist die relative Häufigkeit der Sechs insgesamt in Prozent? (Runde auf eine Nachkommastelle.)',
             runde(h * 100, 1), f'round({k} / {n} * 100, 1)', f'Insgesamt {k} Sechsen bei {n} Würfen: {k} : {n} ≈ {zt(runde(h * 100, 1))} %.',
             'Addiere die Sechsen und die Würfe – nicht die Prozentsätze mitteln.', '%', toleranz=0.1)


def g_laplace(R, st):
    if st == 1:
        r, b, g = R.randint(1, 9), R.randint(1, 9), R.randint(0, 6)
        alle = r + b + g
        farbe, gn = R.choice([('rot', r), ('blau', b)] + ([('grün', g)] if g else []))
        p = Fr(gn, alle)
        txt = f'In einer Urne liegen {r} rote, {b} blaue{"" if not g else f" und {g} grüne"} Kugeln. Eine wird zufällig gezogen. Wie groß ist P({farbe})?'
        if ist_endlich(p) and len(zt(p)) <= 5 and R.random() < .5:
            return Z(txt + ' Gib sie als Dezimalzahl an.', p, f'{gn} / {alle}', f'{gn} günstige von {alle} Kugeln: P = {gn}/{alle} = {zt(p)}.', 'Günstige durch alle Kugeln.')
        return A(R, txt, bruch(p), frac_opts(p, gn, alle) + ([bruch(Fr(gn, alle - gn))] if alle != gn else []), f'{gn} günstige von {alle} Kugeln: P({farbe}) = {gn}/{alle}' + ('' if bruch(p) == f'{gn}/{alle}' else f' = {bruch(p)}') + '.',
                 'Im Nenner stehen alle Kugeln.')
    if st == 2:
        art = R.choice(['wuerfel', 'karten', 'rad'])
        if art == 'wuerfel':
            n = R.choice([6, 8, 10, 12, 20])
            name, f = R.choice([('eine gerade Zahl', lambda x: x % 2 == 0), ('eine Zahl größer als 3', lambda x: x > 3), ('eine Primzahl', lambda x: x in (2, 3, 5, 7, 11, 13, 17, 19)),
                                ('ein Vielfaches von 3', lambda x: x % 3 == 0), ('eine Zahl kleiner als 5', lambda x: x < 5)])
            guenstig = [x for x in range(1, n + 1) if f(x)]
            gn = len(guenstig); p = Fr(gn, n)
            auf = f'{", ".join(map(str, guenstig))} – das sind {gn} von {n} Ergebnissen' if gn <= 10 else f'{gn} von {n} Ergebnissen'
            txt = f'Ein fairer Würfel mit den Zahlen 1 bis {n} wird geworfen. Wie groß ist die Wahrscheinlichkeit für {name}?'
        elif art == 'karten':
            name, gn = R.choice([('eine Herz-Karte', 8), ('ein Ass', 4), ('eine rote Karte', 16), ('ein Bube oder eine Dame', 8), ('die Kreuz-Dame', 1), ('eine Bildkarte (Bube, Dame, König)', 12)])
            n = 32; p = Fr(gn, n)
            txt = f'Aus einem Skatblatt (32 Karten: 4 Farben, je 7, 8, 9, 10, Bube, Dame, König, Ass) wird eine Karte gezogen. Wie groß ist die Wahrscheinlichkeit für {name}?'
        else:
            n = R.choice([5, 8, 10, 12, 16, 20]); gn = R.randint(1, n - 1); p = Fr(gn, n)
            txt = f'Ein Glücksrad hat {n} gleich große Felder, {gn} davon sind rot. Wie groß ist die Wahrscheinlichkeit für „rot“?'
        if art != 'wuerfel': auf = f'{gn} günstige von {n} gleich wahrscheinlichen Ergebnissen'
        gekuerzt = '' if (p.numerator, p.denominator) == (gn, n) else f' = {bruch(p)}'
        if ist_endlich(p) and len(zt(p)) <= 6 and R.random() < .5:
            return Z(txt + ' Gib sie als Dezimalzahl an.', p, f'{gn} / {n}', f'{auf}: P = {gn}/{n} = {zt(p)}.', 'Zähle die günstigen Ergebnisse.')
        if R.random() < .5:
            return L(txt + ' Gib sie als vollständig gekürzten Bruch an.', '□/□', [p.numerator, p.denominator], [str(p.numerator), str(p.denominator)],
                     f'{auf}: P = {gn}/{n}{gekuerzt}.', 'Zähle die günstigen Ergebnisse. Kürze am Ende.', hinweis='Zähler oben, Nenner unten.')
        return A(R, txt, bruch(p), frac_opts(p, gn, n), f'{auf}: P = {gn}/{n}{gekuerzt}.', 'Zähle die günstigen Ergebnisse.')
    # Stufe 3: zwei Würfel / Urne ergänzen
    if R.random() < .5:
        s = R.randint(3, 11)
        gn = sum(1 for a in range(1, 7) for b in range(1, 7) if a + b == s); p = Fr(gn, 36)
        return A(R, f'Zwei faire Würfel werden geworfen. Wie groß ist die Wahrscheinlichkeit, dass die Augensumme {s} ist?', bruch(p),
                 [x for x in ['1/11', bruch(Fr(gn, 21)) if Fr(gn, 21) != p else '1/21', bruch(Fr(1, 6)) if p != Fr(1, 6) else '1/12', bruch(Fr(gn, 12))] if x != bruch(p)],
                 f'36 gleich wahrscheinliche Paare. Summe {s}: {gn} Paare. P = {gn}/36 = {bruch(p)}.', 'Schreibe alle 36 Paare als Tabelle. Die 11 möglichen Summen sind nicht gleich wahrscheinlich!')
    r, b = R.randint(2, 9), R.randint(1, 9)
    p = Fr(R.choice([1, 2, 3, 4]), R.choice([5, 10]))
    # Wie viele blaue Kugeln muss man dazulegen, damit P(rot) = p?  r/(r+b+x) = p -> x = r/p - r - b
    x = r / p - r - b
    if x.denominator != 1 or x <= 0: return g_laplace(R, st)
    return Z(f'In einer Urne liegen {r} rote und {b} blaue Kugeln. Wie viele blaue Kugeln muss man dazulegen, damit P(rot) = {zt(p)} ist?', x, f'{r} / {zt(p).replace(",", ".")} - {r} - {b}',
             f'{r} : (Gesamtzahl) = {zt(p)} → Gesamtzahl = {r} : {zt(p)} = {zt(r / p)}. Dazulegen: {zt(r / p)} − {r + b} = {zt(x)}.', 'Wie viele Kugeln muss es insgesamt geben?')


def g_gegenereignis(R, st):
    if st == 1:
        p = Fr(R.randint(60, 98), 100)
        return Z(f'Die Wahrscheinlichkeit, dass ein Bus pünktlich ist, beträgt {zt(p * 100)} %. Wie groß ist die Wahrscheinlichkeit, dass er nicht pünktlich ist (in %)?', 100 - p * 100,
                 f'100 - {zt(p * 100).replace(",", ".")}', f'P(Ē) = 100 % − {zt(p * 100)} % = {zt(100 - p * 100)} %.', 'P(Ē) = 1 − P(E), also 100 % − P(E).', '%')
    if st == 2 and R.random() < .5:
        pos, neg, lo, hi = R.choice([('ein Zug pünktlich ist', 'er nicht pünktlich ist', 75, 95), ('ein Elfmeter verwandelt wird', 'er nicht verwandelt wird', 70, 85),
                                     ('ein Samenkorn keimt', 'es nicht keimt', 80, 95), ('ein Los gewinnt', 'es nicht gewinnt', 3, 20)])
        pz = R.randint(lo, hi)
        return Z(f'Die Wahrscheinlichkeit, dass {pos}, beträgt {pz} %. Wie groß ist die Wahrscheinlichkeit, dass {neg} (in %)?', 100 - pz, f'100 - {pz}',
                 f'Gegenereignis: P(Ē) = 100 % − {pz} % = {100 - pz} %.', 'P(Ē) = 1 − P(E), also 100 % − P(E).', '%')
    if st == 2:
        paare = [('Zwei Würfe mit einem Spielwürfel', 'mindestens eine Sechs', 'keine Sechs', ['genau eine Sechs', 'höchstens eine Sechs', 'zwei Sechsen']),
                 ('Fünf Würfe auf eine Torwand', 'höchstens zwei Treffer', 'mindestens drei Treffer', ['mindestens zwei Treffer', 'weniger als zwei Treffer', 'genau drei Treffer']),
                 ('Drei Kugeln werden aus einer Urne gezogen', 'alle Kugeln sind rot', 'mindestens eine Kugel ist nicht rot', ['keine Kugel ist rot', 'genau eine Kugel ist nicht rot', 'alle Kugeln sind blau']),
                 ('Ein Spielwürfel wird geworfen', 'die Augenzahl ist gerade', 'die Augenzahl ist ungerade', ['die Augenzahl ist größer als 3', 'die Augenzahl ist 1', 'die Augenzahl ist 6']),
                 ('Zehn Würfe auf einen Korb', 'mehr als 4 Treffer', 'höchstens 4 Treffer', ['weniger als 4 Treffer', 'mindestens 4 Treffer', 'genau 5 Treffer']),
                 ('Zwei Würfe mit einem Spielwürfel', 'genau eine Sechs', 'keine oder zwei Sechsen', ['keine Sechs', 'zwei Sechsen', 'mindestens eine Sechs']),
                 ('Drei Münzwürfe', 'mindestens zwei Wappen', 'höchstens ein Wappen', ['höchstens zwei Wappen', 'genau ein Wappen', 'kein Wappen']),
                 ('Ein Spielwürfel wird geworfen', 'die Augenzahl ist größer als 2', 'die Augenzahl ist 1 oder 2', ['die Augenzahl ist kleiner als 2', 'die Augenzahl ist 3, 4, 5 oder 6', 'die Augenzahl ist höchstens 3'])]
        exp, e, g, falsch = R.choice(paare)
        return A(R, f'{exp}. Wie heißt das Gegenereignis zu „{e}“?', g, falsch, f'Das Gegenereignis umfasst genau die Fälle, in denen „{e}“ nicht eintritt: {g}.',
                 'Welche Fälle bleiben übrig, wenn E nicht eintritt? Zähle alle Möglichkeiten auf.')
    if R.random() < .4:
        if R.random() < .5:
            p1, p2 = Fr(R.choice([10, 15, 20, 25, 30]), 100), Fr(R.choice([15, 25, 35, 40]), 100)
            return Z(f'Bei einem Glücksrad ist P(rot) = {zt(p1)} und P(blau) = {zt(p2)}. Wie groß ist P(weder rot noch blau)?', 1 - p1 - p2, f'1 - {zt(p1).replace(",", ".")} - {zt(p2).replace(",", ".")}',
                     f'„Weder rot noch blau“ ist das Gegenereignis zu „rot oder blau“: 1 − ({zt(p1)} + {zt(p2)}) = {zt(1 - p1 - p2)}.', 'Was ist das Gegenereignis? Rechne 1 minus dessen Wahrscheinlichkeit.')
        k = R.choice([2, 3])
        p = 1 - Fr(5, 6) ** k
        return A(R, f'Ein Spielwürfel wird {k}-mal geworfen. Wie groß ist P(mindestens eine Sechs)?', bruch(p),
                 [bruch(Fr(5, 6) ** k), bruch(Fr(k, 6)), bruch(Fr(1, 6) ** k)],
                 f'Gegenereignis: keine Sechs. P(keine Sechs) = (5/6){"²" if k == 2 else "³"} = {bruch(Fr(5, 6) ** k)}. Also P = 1 − {bruch(Fr(5, 6) ** k)} = {bruch(p)}.',
                 '„Mindestens eine“ ist schwer zu zählen. Das Gegenereignis „keine“ ist leicht.')
    n = R.choice([6, 8, 10, 12, 20])
    k = R.randint(1, n - 1)
    p = 1 - Fr(k, n)
    if ist_endlich(p) and len(zt(p)) <= 5:
        return Z(f'Ein fairer Würfel hat die Zahlen 1 bis {n}. Wie groß ist die Wahrscheinlichkeit, KEINE Zahl kleiner oder gleich {k} zu werfen? Gib sie als Dezimalzahl an.', p,
                 f'1 - {k} / {n}', f'P(Zahl ≤ {k}) = {k}/{n}. Gegenereignis: 1 − {k}/{n} = {zt(p)}.', 'Berechne erst P(E) und nimm dann 1 − P(E).')
    return A(R, f'Ein fairer Würfel hat die Zahlen 1 bis {n}. Wie groß ist die Wahrscheinlichkeit, KEINE Zahl kleiner oder gleich {k} zu werfen?', bruch(p),
             [bruch(Fr(k, n)), bruch(Fr(n - k, n + 1)), bruch(Fr(n - k + 1, n)) if Fr(n - k + 1, n) != p else '1/2'],
             f'P(Zahl ≤ {k}) = {k}/{n}. Gegenereignis: 1 − {k}/{n} = {bruch(p)}.', 'Berechne erst P(E) und nimm dann 1 − P(E).')


def g_grosse_zahlen(R, st):
    if st >= 2 and R.random() < .3:
        ding, n, lo, hi = R.choice([('Eine Reißzwecke landete', 1000, 560, 660), ('Ein Legostein lag', 400, 70, 110), ('Ein Kronkorken landete', 500, 220, 300)])
        k = R.randint(lo, hi)
        lage = {'Eine Reißzwecke landete': 'auf dem Kopf', 'Ein Legostein lag': 'auf der Seite', 'Ein Kronkorken landete': 'mit der Öffnung nach oben'}[ding]
        return Z(f'{ding} bei {n} Würfen {k}-mal {lage}. Schätze die Wahrscheinlichkeit dafür auf zwei Nachkommastellen.', runde(Fr(k, n), 2), f'round({k} / {n}, 2)',
                 f'Bei vielen Würfen ist die relative Häufigkeit eine gute Schätzung: {k} : {n} = {zt(Fr(k, n))} ≈ {zt(runde(Fr(k, n), 2))}.',
                 'Relative Häufigkeit bei vielen Versuchen = Schätzwert für die Wahrscheinlichkeit.', toleranz=0.01)
    if st in (1, 2):
        art = R.choice(['muenze', 'wuerfel', 'rad'])
        if art == 'muenze':
            n = R.choice([100, 200, 500, 1000, 2000]); p = Fr(1, 2); was = 'Wappen beim Münzwurf'
        elif art == 'wuerfel':
            n = R.choice([60, 120, 300, 600, 1200, 3000]); p = Fr(1, 6); was = 'eine Sechs beim Würfeln'
        else:
            k = R.choice([4, 5, 8, 10]); g = R.randint(1, k - 1); n = R.choice([40, 80, 100, 200, 400]); p = Fr(g, k)
            was = f'„rot“ beim Glücksrad mit {k} gleichen Feldern, davon {g} rot'
            if (n * p).denominator != 1: return g_grosse_zahlen(R, st)
        return Z(f'Wie oft erwartest du bei {n} Versuchen ungefähr {was}?', n * p, f'{n} * {p.numerator} / {p.denominator}',
                 f'Erwartet: n · P = {n} · {bruch(p)} = {zt(n * p)}. Das tatsächliche Ergebnis schwankt um diesen Wert.', 'Anzahl der Versuche mal Wahrscheinlichkeit.')
    al = [('Bei 6000 Würfen eines fairen Würfels kommt die Sechs ungefähr 1000-mal.', True),
          ('Bei 6 Würfen eines fairen Würfels kommt die Sechs genau einmal.', False),
          ('Nach fünf Würfen ohne Sechs ist eine Sechs beim nächsten Wurf wahrscheinlicher.', False),
          ('Je öfter man eine Münze wirft, desto näher liegt meist der Anteil der Wappen bei 0,5.', True),
          ('Bei 10 Münzwürfen gibt es immer genau 5-mal Wappen.', False),
          ('Die relative Häufigkeit kann bei wenigen Versuchen stark von der Wahrscheinlichkeit abweichen.', True),
          ('Mit vielen Versuchen kann man eine unbekannte Wahrscheinlichkeit gut schätzen.', True),
          ('Wenn beim Roulette fünfmal Rot kam, muss jetzt Schwarz kommen.', False),
          ('Die absolute Anzahl der Wappen liegt bei vielen Würfen immer genau bei der Hälfte.', False)]
    wahr = [t for t, w in al if w]; falsch = [t for t, w in al if not w]
    if R.random() < .5:
        t = R.choice(wahr)
        return A(R, 'Welche Aussage zum Gesetz der großen Zahlen ist richtig?', t, R.sample(falsch, 3), f'Richtig: {t} Zufall hat kein Gedächtnis; erst bei vielen Versuchen stabilisiert sich die relative Häufigkeit.',
                 'Achte auf Wörter wie „genau“, „immer“ und „muss“.')
    t = R.choice(falsch)
    return A(R, 'Welche Aussage ist FALSCH?', t, R.sample(wahr, 3), f'Falsch: {t} Die relative Häufigkeit nähert sich nur ungefähr an, genaue Vorhersagen sind unmöglich.',
             'Achte auf Wörter wie „genau“, „immer“ und „muss“.')


def g_laplace_pruefen(R, st):
    if st == 3 or (st == 2 and R.random() < .5):
        k = R.randint(3, 6)
        gleich = R.random() < .4
        if gleich: w = [360 // k] * k if 360 % k == 0 else None
        else:
            while True:
                w = sorted([R.choice([30, 45, 60, 90, 120, 150, 180]) for _ in range(k - 1)])
                rest = 360 - sum(w)
                if rest > 0 and rest % 15 == 0 and len(set(w + [rest])) > 1: w = w + [rest]; break
        if w is None: return g_laplace_pruefen(R, st)
        felder = ', '.join(f'{chr(65 + i)} {x}°' for i, x in enumerate(w))
        rad = {'typ': 'kreisdiagramm', 'einheit': '°', 'werte': [{'name': chr(65 + i), 'wert': x} for i, x in enumerate(w)], 'zahlen': True}
        if st == 3 and not gleich:
            i = R.randrange(len(w))
            p = Fr(w[i], 360)
            if ist_endlich(p) and len(zt(p)) <= 6:
                return mit_bild(Z(f'Glücksrad mit den Feldern {felder} (siehe Bild). Wie groß ist die Wahrscheinlichkeit für Feld {chr(65 + i)}? Gib sie als Dezimalzahl an.', p, f'{w[i]} / 360',
                                  f'Kein Laplace-Experiment, aber P ist der Anteil am Vollwinkel: {w[i]}° : 360° = {zt(p)}.', 'Die Wahrscheinlichkeit ist der Anteil des Feldes am ganzen Kreis (360°).'), rad)
        r = 'Ja, alle Felder sind gleich groß.' if gleich else 'Nein, die Felder sind verschieden groß.'
        return mit_bild(A(R, f'Ein Glücksrad hat die Felder {felder}. Ist eine Drehung (Ergebnis: Feldname) ein Laplace-Experiment?', r,
                 ['Nein, die Felder sind verschieden groß.', 'Nein, ein Glücksrad ist nie ein Laplace-Experiment.', 'Nein, dafür braucht man genau 6 Felder.' if k != 6 else 'Nein, dafür braucht man eine gerade Anzahl Felder.'] if gleich else
                 ['Ja, alle Felder sind gleich groß.', 'Ja, jedes Glücksrad ist ein Laplace-Experiment.', f'Ja, weil es {k} Felder gibt.'], 'Gleich große Felder → gleich wahrscheinlich.' if gleich else 'Größere Felder werden häufiger getroffen.',
                 'Vergleiche die Winkel der Felder.'), rad)
    bank = [('Werfen eines fairen Spielwürfels', True), ('Werfen einer Reißzwecke (Kopf oder Seite)', False), ('Werfen einer fairen Münze', True),
            ('Ziehen einer Kugel aus 3 roten und 5 blauen Kugeln, notiert wird die Farbe', False),
            ('Ziehen einer von 8 gleichen, durchnummerierten Kugeln, notiert wird die Nummer', True),
            ('Werfen eines Quaders mit verschieden großen Seitenflächen', False), ('Ziehen einer Karte aus einem gut gemischten Skatblatt', True),
            ('Würfeln mit zwei Würfeln, notiert wird die Augensumme', False), ('Würfeln mit zwei Würfeln, notiert wird das Zahlenpaar', True),
            ('Werfen eines Kronkorkens', False), ('Ein Glücksrad mit 10 gleich großen Feldern', True), ('Werfen eines Legosteins', False)]
    t, w = R.choice(bank)
    r = 'Ja' if w else 'Nein'
    return A(R, f'Ist das ein Laplace-Experiment? {t}.', f'{r}, ' + ('alle Ergebnisse sind gleich wahrscheinlich.' if w else 'die Ergebnisse sind nicht gleich wahrscheinlich.'),
             ['Ja, alle Ergebnisse sind gleich wahrscheinlich.' if not w else 'Nein, die Ergebnisse sind nicht gleich wahrscheinlich.',
              'Nein, bei Zufallsexperimenten weiß man das nie.', 'Ja, weil es zwei oder mehr Ergebnisse gibt.'],
             'Alle Ergebnisse sind gleich wahrscheinlich.' if w else 'Die Ergebnisse haben verschiedene Wahrscheinlichkeiten (z. B. wegen Form, Anzahl oder Summenbildung).',
             'Sind wirklich alle Ergebnisse gleich wahrscheinlich?')


GEN = {'begriffe': g_begriffe, 'rel_haeufigkeit': g_rel_haeufigkeit, 'laplace': g_laplace, 'gegenereignis': g_gegenereignis,
       'grosse_zahlen': g_grosse_zahlen, 'laplace_pruefen': g_laplace_pruefen}


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl8.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl8 import mit_umbau  # noqa: E402

_AUG = ['Augenzahl', '1', '2', '3', '4', '5', '6']
_MUENZ = {"typ": "baum", "aeste": [{"text": "W", "p": "1/2", "aeste": [{"text": "WW", "p": "1/2"}, {"text": "WZ", "p": "1/2"}]},
                                   {"text": "Z", "p": "1/2", "aeste": [{"text": "ZW", "p": "1/2"}, {"text": "ZZ", "p": "1/2"}]}]}
UMBAU = {
 'begriffe': {
  'einstieg': 'Beim Spieleabend würfelt Lena. Sie weiß vorher nicht, welche Zahl kommt, aber möglich sind 1 bis 6. So ein Vorgang heißt ⟦Zufallsexperiment⟧.',
  'woerter': [['Zufallsexperiment', 'ein Vorgang, dessen Ausgang man nicht vorhersagen kann'], ['Ergebnisraum Ω', 'alle möglichen Ergebnisse, hier 1 bis 6'], ['Ereignis', 'eine Auswahl von Ergebnissen, z. B. „mehr als 4“']],
  'bild': {'typ': 'tabelle', 'kopf': _AUG, 'zeilen': [['mehr als 4?', '?', '?', '?', '?', '?', '?']]},
  'schritte': [{'text': 'Möglich sind 1 bis 6: Ergebnisraum Ω = {1; 2; 3; 4; 5; 6}.'},
               {'text': 'Lena gewinnt bei mehr als 4 Augen. Das ist das Ereignis E.'},
               {'text': 'Mehr als 4 sind nur 5 und 6: ⟦E = {5; 6}⟧.', 'bild': {'zeilen': [['mehr als 4?', 'nein', 'nein', 'nein', 'nein', 'ja', 'ja']]}}],
  'fehler': 'Zwei Münzwürfe haben nicht 3 Ergebnisse. WZ und ZW sind verschieden – der Baum zeigt ⟦vier⟧ Wege.',
  'fehler_bild': _MUENZ,
  'regel': 'Erst alle ⟦Ergebnisse⟧ in Ω aufschreiben. Dann für das Ereignis die passenden heraussuchen.'},
 'rel_haeufigkeit': {
  'einstieg': 'Lena hat 50-mal gewürfelt und 12-mal eine Sechs bekommen. Ist das viel? Das zeigt erst der Anteil an allen Würfen, die ⟦relative Häufigkeit⟧.',
  'woerter': [['absolute Häufigkeit', 'wie oft etwas vorkam, hier 12'], ['relative Häufigkeit', 'der Anteil: absolute Häufigkeit : Anzahl der Versuche']],
  'bild': {'typ': 'saeulen', 'einheit': 'Würfe', 'werte': [{'name': 'Sechs', 'wert': 12}, {'name': 'andere', 'wert': 38}], 'zahlen': True},
  'schritte': [{'text': '12 Sechsen: Das ist die absolute Häufigkeit.'},
               {'text': 'Für den Anteil teilst du durch alle Würfe: 12 : 50.'},
               {'text': 'Die relative Häufigkeit ist ⟦0,24 = 24 %⟧.', 'bild': {'typ': 'kreisdiagramm', 'einheit': ' %', 'werte': [{'name': 'Sechs', 'wert': 24}, {'name': 'andere', 'wert': 76}], 'zahlen': True}}],
  'fehler': 'Die relative Häufigkeit ist nicht 12. Das ist die ⟦absolute⟧ Häufigkeit; relativ heißt im Vergleich zu allen 50 Würfen.',
  'regel': 'Relative Häufigkeit = ⟦absolute Häufigkeit : Anzahl der Versuche⟧. Sie liegt immer zwischen 0 und 1.'},
 'laplace': {
  'einstieg': 'In der Lostrommel liegen 3 rote, 5 blaue und 2 grüne Kugeln, gut gemischt. Jede Kugel hat dieselbe Chance. Dann kannst du die ⟦Wahrscheinlichkeit⟧ für „rot“ ausrechnen.',
  'woerter': [['Wahrscheinlichkeit', 'wie groß die Chance ist, als Zahl von 0 bis 1'], ['günstig', 'passend zum Ereignis, hier: rot'], ['P(rot)', 'die Wahrscheinlichkeit für „rot“']],
  'bild': {'typ': 'saeulen', 'einheit': 'Kugeln', 'werte': [{'name': 'rot', 'wert': 3}, {'name': 'blau', 'wert': 5}, {'name': 'grün', 'wert': 2}], 'zahlen': True},
  'schritte': [{'text': 'Günstig für „rot“ sind die 3 roten Kugeln.'},
               {'text': 'Möglich sind alle 3 + 5 + 2 = 10 Kugeln.'},
               {'text': 'Also ist ⟦P(rot) = 3/10 = 0,3⟧.'}],
  'fehler': 'P(rot) ist nicht 3/7, also rot zu nicht-rot. Im Nenner stehen ⟦alle⟧ 10 Kugeln: 3/10.',
  'regel': '⟦P = günstige : alle Ergebnisse⟧. Das gilt nur, wenn alle gleich wahrscheinlich sind.'},
 'laplace_pruefen': {
  'einstieg': 'Ein Glücksrad hat drei Felder, aber Feld A ist halb so groß wie das ganze Rad. Hat trotzdem jedes Feld die Chance 1/3? Nur bei gleichen Chancen ist es ein ⟦Laplace-Experiment⟧.',
  'woerter': [['Laplace-Experiment', 'alle Ergebnisse haben dieselbe Chance']],
  'bild': {"typ": "kreisdiagramm", "einheit": "°", "werte": [{"name": "A", "wert": 180}, {"name": "B", "wert": 90}, {"name": "C", "wert": 90}], "zahlen": True},
  'schritte': [{'text': 'Feld A hat 180°, B und C haben je 90°.'},
               {'text': 'A ist doppelt so groß wie B. Der Zeiger bleibt öfter auf A stehen.'},
               {'text': 'Also ⟦kein Laplace-Experiment⟧: P(A) = 180/360 = 1/2.'}],
  'fehler': 'Drei Felder bedeuten nicht automatisch je 1/3. Das gilt nur bei ⟦gleich großen⟧ Feldern wie hier.',
  'fehler_bild': {"werte": [{"name": "A", "wert": 120}, {"name": "B", "wert": 120}, {"name": "C", "wert": 120}]},
  'regel': 'Laplace heißt: ⟦alle Ergebnisse gleich wahrscheinlich⟧. Unterschiedlich große Felder sind kein Laplace-Experiment.'},
 'gegenereignis': {
  'einstieg': 'Lena darf keine Sechs würfeln, sonst muss sie zurück. Statt „1, 2, 3, 4 oder 5“ zu zählen, rechnet sie: alles außer der Sechs. Das heißt ⟦Gegenereignis⟧.',
  'woerter': [['Gegenereignis Ē', '„nicht E“: alle Ergebnisse, die nicht zu E gehören'], ['P(E)', 'die Wahrscheinlichkeit von E']],
  'bild': {'typ': 'tabelle', 'kopf': _AUG, 'zeilen': [['E: Sechs', '–', '–', '–', '–', '–', '✓']]},
  'schritte': [{'text': 'E heißt „Sechs würfeln“, also P(E) = 1/6.'},
               {'text': 'Das Gegenereignis Ē heißt „keine Sechs“.', 'bild': {'zeilen': [['E: Sechs', '–', '–', '–', '–', '–', '✓'], ['Ē: keine', '✓', '✓', '✓', '✓', '✓', '–']]}},
               {'text': 'Zusammen ergeben beide 1: ⟦P(Ē) = 1 − 1/6 = 5/6⟧.'}],
  'fehler': 'Das Gegenteil von „mindestens eine Sechs“ ist nicht „höchstens eine“, sondern ⟦„keine Sechs“⟧.',
  'regel': '⟦P(Ē) = 1 − P(E)⟧. Nutze das, wenn „nicht E“ leichter zu zählen ist.'},
 'grosse_zahlen': {
  'einstieg': 'Wirfst du eine Münze 10-mal, kommt vielleicht 7-mal Wappen. Bei 1000 Würfen liegt der Anteil fast immer nahe der Hälfte. Das ist das ⟦Gesetz der großen Zahlen⟧.',
  'woerter': [['Gesetz der großen Zahlen', 'bei vielen Versuchen liegt der Anteil nahe der Wahrscheinlichkeit'], ['erwartest', 'du schätzt vorher, was ungefähr herauskommt']],
  'bild': {'typ': 'saeulen', 'einheit': 'Anteil', 'werte': [{'name': 'n = 10', 'wert': 0.7}, {'name': 'n = 100', 'wert': 0.47}, {'name': 'n = 1000', 'wert': 0.488}], 'zahlen': True},
  'schritte': [{'text': 'Eine Münze wird 1000-mal geworfen. P(Wappen) = 0,5.'},
               {'text': 'Du erwartest 1000 · 0,5 = ⟦etwa 500-mal Wappen⟧.'},
               {'text': 'Es kommt zum Beispiel 488-mal. Der Anteil 0,488 liegt nahe 0,5.'}],
  'fehler': 'Nach fünfmal keiner Sechs ist die Sechs ⟦nicht⟧ wahrscheinlicher. Der Würfel hat kein Gedächtnis: P bleibt 1/6.',
  'regel': 'Bei n Versuchen erwartest du ⟦etwa n · P⟧ Treffer. Genau vorhersagen kann man es nie.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---- SCHWER (Zehnte Runde: schwerere Aufgaben nach Prüfungsvorbild, siehe _schwer_kl8.py) ----
# Vorbilder (Typ und Niveau, nicht Wortlaut/Zahlen): VERA-8 2026 (Kugeln 1–100 mit Glücksziffer; „Würfelgedächtnis“ nach einer Serie;
# Glücksrad: aus absoluten Häufigkeiten ergänzen, Feld für „etwa jede zweite Drehung“; Kugeln aus zwei Säckchen zusammenschütten),
# BMT10 2024 (Kugeln 1–100, Ereignisse und ihre Schnittmenge), BMT10 2011 (Augensumme bei zwei Würfen), BMT10 2023 (Ereignis „keiner der beiden Schäden“),
# BMT8 2023 (fehlenden Anteil ergänzen), Grundwissen 8 (Ergebnismengen, relative Häufigkeiten).
from _schwer_kl8 import Neu, mit_schwer  # noqa: E402

SW = Neu(10_8_13)
_SIEBEN = sum('7' in str(i) for i in range(1, 101))
assert _SIEBEN == 19
_GROESSER = sum(1 for a in range(1, 7) for b in range(1, 7) if b > a)
_SUMME_UEBER_10 = sum(1 for a in range(1, 7) for b in range(1, 7) if a + b > 10)
_HB = 'Zähler und Nenner je als ganze Zahl, vollständig gekürzt.'

# begriffe
SW.a('begriffe', 2, 'Zwei Münzen werden geworfen. Notiert wird nur, wie oft Wappen fällt. Welcher Ergebnisraum passt?', 'Ω = {0; 1; 2}', ['Ω = {WW; WZ; ZW; ZZ}', 'Ω = {1; 2}', 'Ω = {W; Z}'],
     'Notiert wird eine Anzahl: kein, ein oder zwei Wappen. Ω = {0; 1; 2}. Der Ergebnisraum hängt davon ab, was man notiert.', 'Was wird aufgeschrieben – die Münzbilder oder eine Zahl?')
SW.z('begriffe', 2, 'Ein Spielwürfel (1 bis 6) wird geworfen. Wie viele Ergebnisse gehören zum Ereignis „Augenzahl ist keine Primzahl“?', 3, '6 - 3',
     'Primzahlen sind 2, 3, 5. Keine Primzahl: 1, 4, 6 – das sind 3 Ergebnisse. (1 ist keine Primzahl.)', 'Schreibe erst die Primzahlen bis 6 auf.')
SW.z('begriffe', 3, 'In einer Lostrommel liegen Kugeln mit den Nummern 1 bis 100. Wie viele Ergebnisse gehören zum Ereignis „Die Nummer enthält mindestens einmal die Ziffer 7“?', _SIEBEN, '10 + 10 - 1',
     'Einerziffer 7: 7, 17, …, 97 (10 Zahlen). Zehnerziffer 7: 70 bis 79 (10 Zahlen). Die 77 ist doppelt gezählt: 10 + 10 − 1 = 19.', 'Zähle Einer-7 und Zehner-7 getrennt. Welche Zahl zählst du doppelt?', art='P')
SW.z('begriffe', 3, 'Kugeln mit den Nummern 1 bis 30. A: „Nummer ist gerade“, B: „Nummer ist durch 5 teilbar“. Wie viele Nummern gehören zu A und zugleich zu B?', 3, '30 // 10',
     'Gerade und durch 5 teilbar heißt durch 10 teilbar: 10, 20, 30. Das sind 3.', 'Welche Zahlen sind gerade und durch 5 teilbar?', art='P')
SW.z('begriffe', 3, 'Ein Spielwürfel wird zweimal geworfen. Notiert wird die Augensumme. Wie viele Ergebnisse hat der Ergebnisraum?', 11, '12 - 2 + 1',
     'Die Summe kann 2, 3, …, 12 sein: 11 Ergebnisse (nicht 36 – das wären die Zahlenpaare).', 'Was ist die kleinste, was die größte Summe?', art='K')
SW.z('begriffe', 3, 'Eine Münze wird dreimal geworfen, die Reihenfolge wird notiert. Wie viele Ergebnisse gehören zum Ereignis „genau zweimal Wappen“?', 3, '3',
     'WWZ, WZW, ZWW – die eine Zahl kann an der 1., 2. oder 3. Stelle stehen: 3 Ergebnisse.', 'Wo kann die einzige Zahl stehen?', art='K')

# rel_haeufigkeit
SW.z('rel_haeufigkeit', 2, 'Ein Kronkorken wurde 80-mal geworfen. Die relative Häufigkeit für „Öffnung oben“ ist 0,35. Wie oft lag er so?', 28, '0.35 * 80', '0,35 · 80 = 28.',
     'Absolute Häufigkeit = relative Häufigkeit · Anzahl der Würfe.')
SW.z('rel_haeufigkeit', 2, 'In einer Klasse mit 25 Kindern tragen 6 eine Brille. Wie groß ist die relative Häufigkeit in Prozent?', 24, '6 / 25 * 100', '6 : 25 = 0,24 = 24 %.',
     'Teile durch die Gesamtzahl.', einheit='%')
SW.z('rel_haeufigkeit', 3, 'Ein Glücksrad wurde 180-mal gedreht: 72-mal rot, 63-mal grün, sonst blau. Wie groß ist die relative Häufigkeit von blau? Gib sie als Dezimalzahl an.', 0.25,
     '(180 - 72 - 63) / 180', 'Blau: 180 − 72 − 63 = 45. Relative Häufigkeit 45 : 180 = 0,25.', 'Bestimme zuerst, wie oft blau kam.', art='P')
SW.z('rel_haeufigkeit', 3, 'Bei einer Umfrage unter 160 Kindern kommen 40 % mit dem Bus, 1/4 mit dem Fahrrad, der Rest zu Fuß. Wie viele kommen zu Fuß?', 56, '160 * (1 - 0.4 - 0.25)',
     '1/4 = 25 %. Zu Fuß: 100 % − 40 % − 25 % = 35 %. 35 % von 160 = 56.', 'Schreibe alle Anteile in Prozent.', einheit='Kinder', art='P')
SW.z('rel_haeufigkeit', 3, 'Nach 40 Würfen ist die relative Häufigkeit der Sechs 0,15. Wie viele Sechsen müssen in den nächsten 10 Würfen fallen, damit sie danach 0,2 beträgt?', 4, '0.2 * 50 - 0.15 * 40',
     'Bisher 0,15 · 40 = 6 Sechsen. Nach 50 Würfen braucht man 0,2 · 50 = 10. Es fehlen 4.', 'Rechne mit absoluten Anzahlen vorher und nachher.', art='K')
SW.a('rel_haeufigkeit', 3, 'Lea würfelt 20-mal und hat 5 Sechsen, Tim würfelt 200-mal und hat 40 Sechsen. Wessen relative Häufigkeit liegt näher an 1/6 ≈ 0,167?', 'Tims (0,2)',
     ['Leas (0,25)', 'Beide gleich nah', 'Leas, weil sie weniger Fehlwürfe hat'],
     'Lea: 5 : 20 = 0,25 (Abstand 0,083). Tim: 40 : 200 = 0,2 (Abstand 0,033). Mit mehr Würfen liegt der Anteil meist näher an der Wahrscheinlichkeit.', 'Berechne beide relativen Häufigkeiten.', art='K')

# laplace
SW.l('laplace', 2, 'Aus Kugeln mit den Nummern 1 bis 20 wird eine gezogen. Wie groß ist die Wahrscheinlichkeit für ein Vielfaches von 4?', '□/□', [1, 4], ['1', '4'],
     'Vielfache von 4: 4, 8, 12, 16, 20 – das sind 5. P = 5/20 = 1/4.', 'Zähle die günstigen Nummern.', _HB)
SW.l('laplace', 2, 'Ein Glücksrad hat 12 gleich große Felder: 3 gelb, 4 rot, der Rest blau. Wie groß ist P(blau)?', '□/□', [5, 12], ['12 - 3 - 4', '12'],
     'Blau: 12 − 3 − 4 = 5 Felder. P = 5/12.', 'Wie viele Felder sind blau?', _HB)
SW.l('laplace', 3, 'Zwei faire Würfel werden geworfen. Wie groß ist die Wahrscheinlichkeit, dass die Augensumme größer als 10 ist?', '□/□', [1, 12], ['1', '36 // ' + str(_SUMME_UEBER_10)],
     'Summe 11: (5|6), (6|5). Summe 12: (6|6). 3 von 36 Paaren: 3/36 = 1/12.', 'Zähle die Zahlenpaare mit Summe 11 und 12.', _HB, art='P')
SW.l('laplace', 3, 'Säckchen A enthält 3 weiße und 2 schwarze Kugeln, Säckchen B 1 weiße und 9 schwarze. Beide werden in einen Sack geschüttet. Wie groß ist dann P(weiß)?', '□/□', [4, 15],
     ['3 + 1', '(5 + 10) // 1'], 'Im Sack: 4 weiße von 15 Kugeln. P = 4/15. Den Mittelwert aus 3/5 und 1/10 zu nehmen wäre falsch – die Säckchen sind verschieden groß.',
     'Zähle alle weißen und alle Kugeln im großen Sack.', _HB, art='P')
SW.z('laplace', 3, 'In einer Urne liegen 3 rote und 5 blaue Kugeln. Wie viele rote Kugeln muss man dazulegen, damit P(rot) = 3/4 ist?', 12, '(3 * 8 - 4 * 3) / (4 - 3)',
     '(3 + x)/(8 + x) = 3/4 ⇔ 12 + 4x = 24 + 3x ⇔ x = 12. Probe: 15/20 = 3/4.', 'Stelle eine Bruchgleichung auf.', art='K')
SW.l('laplace', 3, 'Ein Spielwürfel wird zweimal geworfen. Wie groß ist die Wahrscheinlichkeit, dass die zweite Zahl größer ist als die erste?', '□/□', [5, 12], ['5', '12'],
     f'Von 36 Paaren haben 6 gleiche Zahlen. Die übrigen 30 teilen sich gleich auf: {_GROESSER}-mal ist die zweite größer. P = 15/36 = 5/12.', 'Wie viele Paare haben gleiche Zahlen?', _HB, art='K')

# laplace_pruefen
SW.a('laplace_pruefen', 2, 'Aus einer Urne mit 3 roten und 1 blauen Kugel wird eine gezogen, notiert wird die Farbe. Ist das ein Laplace-Experiment?', 'Nein, rot ist wahrscheinlicher als blau.',
     ['Ja, jede Kugel ist gleich wahrscheinlich.', 'Ja, es gibt zwei Ergebnisse.'], 'Ergebnisse sind die Farben: P(rot) = 3/4, P(blau) = 1/4 – nicht gleich wahrscheinlich.',
     'Was sind hier die Ergebnisse: Kugeln oder Farben?')
SW.a('laplace_pruefen', 2, 'Zwei Würfel werden geworfen, notiert wird die Augensumme. Ist das ein Laplace-Experiment?', 'Nein, die Summe 7 ist wahrscheinlicher als die Summe 2.',
     ['Ja, jede Summe ist gleich wahrscheinlich.', 'Ja, weil die Würfel fair sind.'], 'Summe 2 nur mit (1|1), Summe 7 mit sechs Paaren. Die Summen sind nicht gleich wahrscheinlich.',
     'Auf wie viele Arten erhält man Summe 2, auf wie viele Summe 7?')
SW.a('laplace_pruefen', 3, 'Lisa sagt: „Beim Lotto ist die Reihe 1, 2, 3, 4, 5, 6 unwahrscheinlicher als eine gemischte Reihe wie 4, 11, 19, 23, 37, 42.“ Was stimmt?',
     'Falsch: Jede bestimmte Reihe ist gleich wahrscheinlich.', ['Richtig: Zahlen in Folge kommen selten.', 'Richtig: Kleine Zahlen werden seltener gezogen.', 'Falsch: 1, 2, 3, 4, 5, 6 ist wahrscheinlicher.'],
     'Jede Kugel hat dieselbe Chance. Darum hat jede einzelne Sechserreihe dieselbe Wahrscheinlichkeit. „Gemischt aussehende“ Reihen gibt es nur viel mehr.', 'Ist eine Kugel mit kleiner Nummer schwerer zu ziehen?', art='P')
SW.z('laplace_pruefen', 3, 'Ein Glücksrad soll so gestaltet werden, dass „grün“ bei etwa jeder zweiten Drehung kommt. Wie groß muss der Mittelpunktswinkel des grünen Feldes sein?', 180, '360 / 2',
     'Jede zweite Drehung heißt P = 1/2. Das grüne Feld muss den halben Kreis einnehmen: 180°.', 'Welcher Anteil des Kreises ist „jede zweite“?', einheit='°', art='P')
SW.a('laplace_pruefen', 3, 'Ein Glücksrad hat die Felder A (90°), B (90°) und C (180°). Wie kann man es trotzdem mit Laplace berechnen?', 'C gedanklich in zwei 90°-Felder teilen: 4 gleich wahrscheinliche Teile.',
     ['Gar nicht, es ist kein Laplace-Experiment.', 'P(A) = P(B) = P(C) = 1/3 setzen.', 'Nur wenn man es sehr oft dreht.'],
     'Teilt man C in C₁ und C₂, gibt es 4 gleich große Felder. Dann P(C) = 2/4 = 1/2, P(A) = P(B) = 1/4.', 'Kann man die Felder in gleich große Teile zerlegen?', art='K')
SW.a('laplace_pruefen', 3, 'Eine Münze zeigte 7-mal hintereinander Wappen. Ist sie deshalb sicher gezinkt?', 'Nein: Das ist bei einer fairen Münze selten, aber möglich.',
     ['Ja: Bei einer fairen Münze geht das nicht.', 'Ja: Jetzt muss Zahl kommen.', 'Nein: Bei 7 Würfen kommt immer 7-mal dasselbe.'],
     'Bei einer fairen Münze hat „7-mal Wappen“ die Wahrscheinlichkeit 1/128 – selten, aber nicht unmöglich. Es ist ein Verdacht, kein Beweis. Mehr Würfe würden helfen.',
     'Ist ein seltenes Ereignis unmöglich?', art='K')

# gegenereignis
SW.z('gegenereignis', 2, 'Aus Kugeln mit den Nummern 1 bis 50 wird eine gezogen. Wie groß ist die Wahrscheinlichkeit, dass die Nummer NICHT durch 5 teilbar ist? Gib sie als Dezimalzahl an.', 0.8,
     '1 - 10 / 50', 'Durch 5 teilbar: 10 Nummern, P = 0,2. Gegenereignis: 1 − 0,2 = 0,8.', 'Rechne erst P(durch 5 teilbar).')
SW.a('gegenereignis', 2, 'Ein Würfel wird viermal geworfen. Wie heißt das Gegenereignis zu „höchstens zwei Sechsen“?', 'mindestens drei Sechsen', ['höchstens drei Sechsen', 'keine Sechs',
     'genau zwei Sechsen'], 'Höchstens zwei: 0, 1 oder 2 Sechsen. Gegenteil: 3 oder 4 Sechsen, also mindestens drei.', 'Schreibe alle möglichen Anzahlen 0 bis 4 auf.')
SW.z('gegenereignis', 3, 'Aus Kugeln mit den Nummern 1 bis 100 wird eine gezogen. Wie groß ist die Wahrscheinlichkeit, dass ihre Nummer KEINE 7 enthält? Gib sie als Dezimalzahl an.', 0.81,
     '1 - 19 / 100', '19 Nummern enthalten eine 7 (siehe 7, 17, …, 97 und 70–79, die 77 nur einmal). P = 1 − 0,19 = 0,81.', 'Zähle die Nummern mit 7 – das ist leichter.', art='P')
SW.z('gegenereignis', 3, 'Von 100 untersuchten Bäumen haben 60 Trockenschäden, 30 Schädlingsschäden und 10 beide Schäden. Wie groß ist die Wahrscheinlichkeit, dass ein zufällig gewählter Baum keinen der beiden Schäden hat? Gib sie als Dezimalzahl an.',
     0.2, '(100 - (60 + 30 - 10)) / 100', 'Mit mindestens einem Schaden: 60 + 30 − 10 = 80 (die 10 nicht doppelt zählen). Ohne Schaden: 20 von 100, P = 0,2.',
     'Wie viele Bäume haben mindestens einen Schaden?', art='P')
SW.l('gegenereignis', 3, 'Zwei Würfel werden geworfen. Wie groß ist die Wahrscheinlichkeit für mindestens eine Sechs?', '□/□', [11, 36], ['36 - 25', '36'],
     'Gegenereignis „keine Sechs“: 5 · 5 = 25 Paare. P = 1 − 25/36 = 11/36. (Nicht 2/6 – die Sechs-Sechs würde doppelt gezählt.)', 'Zähle die Paare ganz ohne Sechs.', _HB, art='K')
SW.z('gegenereignis', 3, 'Die Wahrscheinlichkeit eines Ereignisses E ist dreimal so groß wie die seines Gegenereignisses. Wie groß ist P(E)? Gib sie als Dezimalzahl an.', 0.75, '3 / 4',
     'P(E) = 3 · (1 − P(E)) ⇔ 4 · P(E) = 3 ⇔ P(E) = 0,75.', 'P(E) und P(Ē) ergeben zusammen 1.', art='K')

# grosse_zahlen
SW.z('grosse_zahlen', 2, 'Ein Würfel wird 300-mal geworfen. Wie oft erwartest du ungefähr eine Zahl größer als 4?', 100, '300 * 2 / 6', 'Größer als 4: 5 oder 6, P = 2/6. Erwartet: 300 · 2/6 = 100.',
     'Bestimme zuerst die Wahrscheinlichkeit.')
SW.z('grosse_zahlen', 2, 'Ein Glücksrad hat ein Gewinnfeld mit 90° Mittelpunktswinkel. Wie viele Gewinne erwartest du bei 1 200 Drehungen ungefähr?', 300, '1200 * 90 / 360',
     'P(Gewinn) = 90/360 = 1/4. Erwartet: 1 200 · 1/4 = 300.', 'Welcher Anteil des Kreises ist 90°?')
SW.a('grosse_zahlen', 3, 'Ein Glücksrad zeigt mit der Wahrscheinlichkeit 1/3 „rot“. Es wird 180-mal gedreht. Welche Aussage stimmt?', 'Ungefähr 60-mal kommt rot, genau vorhersagen kann man es nicht.',
     ['Genau 60-mal kommt rot.', 'Das kann man nicht abschätzen, weil es Zufall ist.', 'Rot kommt höchstens 60-mal.'],
     'Erwartungswert: 180 · 1/3 = 60. Das ist eine Schätzung – es können auch 55 oder 66 sein. Zufall heißt nicht, dass man nichts abschätzen kann.',
     'Was erwartest du, und wie sicher ist das?', art='P')
SW.a('grosse_zahlen', 3, 'Bei einem Gewinnspiel wird jede Woche eine Kugel aus 100 gezogen. 20 Wochen lang hat niemand gewonnen. Hat man jetzt bessere Chancen?', 'Nein, jede Ziehung ist unabhängig von den vorigen.',
     ['Ja, jetzt ist ein Gewinn „fällig“.', 'Ja, weil die Gewinnkugeln sich gesammelt haben.', 'Nein, jetzt sind die Chancen schlechter.'],
     'Die Kugeln haben kein Gedächtnis: Es liegen jede Woche dieselben 100 Kugeln in der Trommel. Die Wahrscheinlichkeit bleibt gleich.', 'Ändert sich etwas an den Kugeln in der Trommel?', art='P')
SW.z('grosse_zahlen', 3, 'Ein Würfel wird 600-mal geworfen. Wie oft erwartest du ungefähr eine gerade Zahl, die größer als 2 ist?', 200, '600 * 2 / 6',
     'Gerade und größer als 2: 4 und 6. P = 2/6 = 1/3. Erwartet: 600 · 1/3 = 200.', 'Welche Augenzahlen erfüllen beide Bedingungen?', art='K')
SW.z('grosse_zahlen', 3, 'Ein Reißnagel landete bei 400 Würfen 248-mal auf dem Kopf. Wie oft erwartest du bei 1 000 weiteren Würfen, dass er auf der Seite landet?', 380, '1000 * (400 - 248) / 400',
     'Seite: 400 − 248 = 152, relative Häufigkeit 152 : 400 = 0,38. Erwartet: 1 000 · 0,38 = 380.', 'Gefragt ist die Seite, nicht der Kopf.', art='K')

baue = mit_schwer(baue, SW)
# ---- SCHWER ENDE ----

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, mit_befunden  # noqa: E402

BF = Befunde('stochastik.grundbegriffe', 13_8_13)
# c) Grammatik („1 grüne Kugeln“)
BF.ersetze('laplace', 'In einer Urne liegen 9 rote, 3 blaue und 1 grüne Kugeln. Eine wird zufällig gezogen. Wie groß ist P(grün)?', BF.A(
    'In einer Urne liegen 9 rote Kugeln, 3 blaue Kugeln und 1 grüne Kugel. Eine wird zufällig gezogen. Wie groß ist P(grün)?', '1/13',
    ['12/13', '1/12', '1'], '1 günstige von 13 Kugeln: P(grün) = 1/13.', 'Im Nenner stehen alle Kugeln.'))
# a) gleicher Typ wie Stufe 2
for _t in ['Ein Glücksrad hat die Felder A 60°, B 60°, C 60°, D 120°, E 60°. Ist eine Drehung (Ergebnis: Feldname) ein Laplace-Experiment?',
           'Ein Glücksrad hat die Felder A 120°, B 180°, C 60°. Ist eine Drehung (Ergebnis: Feldname) ein Laplace-Experiment?',
           'Ein Glücksrad hat die Felder A 30°, B 60°, C 60°, D 150°, E 60°. Ist eine Drehung (Ergebnis: Feldname) ein Laplace-Experiment?',
           'Ein Glücksrad hat die Felder A 30°, B 30°, C 90°, D 180°, E 30°. Ist eine Drehung (Ergebnis: Feldname) ein Laplace-Experiment?']:
    BF.stufe('laplace_pruefen', _t, 2)
# c) Beinahe-Dublette (Kronkorken 224/500 auf Stufe 2) → andere Stufe-3-Aufgabe (Schätzungen vergleichen)
BF.ersetze('grosse_zahlen', 'Ein Kronkorken landete bei 500 Würfen 225-mal mit der Öffnung nach oben. Schätze die Wahrscheinlichkeit dafür auf zwei Nachkommastellen.', BF.A(
    'Anna wirft einen Kronkorken 20-mal, er landet 12-mal mit der Öffnung nach oben. Ben wirft denselben Kronkorken 500-mal, er landet 225-mal so. Welche Schätzung für P(Öffnung oben) ist besser?',
    'Bens Schätzung 0,45, weil sie auf viel mehr Würfen beruht.',
    ['Annas Schätzung 0,6, weil sie größer ist.', 'Beide Schätzungen sind gleich gut.', 'Annas Schätzung, weil sie mit weniger Würfen schneller fertig war.'],
    'Anna: 12 : 20 = 0,6. Ben: 225 : 500 = 0,45. Je mehr Versuche, desto näher liegt die relative Häufigkeit meist an der Wahrscheinlichkeit. Bens Schätzung ist zuverlässiger.',
    'Berechne beide relativen Häufigkeiten. Welche beruht auf mehr Versuchen?'))
# c) umständliche Formulierung („KEINE Zahl kleiner oder gleich …“) → klare Gegenereignis-Aufgaben
BF.ersetze('gegenereignis', 'Ein fairer Würfel hat die Zahlen 1 bis 10. Wie groß ist die Wahrscheinlichkeit, KEINE Zahl kleiner oder gleich 1 zu werfen? Gib sie als Dezimalzahl an.', BF.Z(
    'Ein Glücksrad hat 10 gleich große Felder mit den Zahlen 1 bis 10. Wie groß ist die Wahrscheinlichkeit, dass die Zahl NICHT durch 3 teilbar ist? Gib sie als Dezimalzahl an.',
    0.7, '1 - 3 / 10', 'Durch 3 teilbar: 3, 6, 9 → P = 3/10. Gegenereignis: 1 − 3/10 = 0,7.', 'Berechne erst P(E) und nimm dann 1 − P(E).'))
BF.ersetze('gegenereignis', 'Ein fairer Würfel hat die Zahlen 1 bis 6. Wie groß ist die Wahrscheinlichkeit, KEINE Zahl kleiner oder gleich 3 zu werfen? Gib sie als Dezimalzahl an.', BF.Z(
    'Ein Spielwürfel wird einmal geworfen. Wie groß ist die Wahrscheinlichkeit, dass KEINE Primzahl fällt? Gib sie als Dezimalzahl an.',
    0.5, '1 - 3 / 6', 'Primzahlen: 2, 3, 5 → P = 3/6. Gegenereignis: 1 − 3/6 = 0,5 (es fallen 1, 4 oder 6).', 'Berechne erst P(E) und nimm dann 1 − P(E).'))
BF.nicht_umgesetzt('gegenereignis S3 „3 Würfe, P(mindestens eine Sechs) = 91/216“',
                   'Lösung richtig; Weg über das Gegenereignis (5/6)³ ist echte Stufe 3. Ob die Produktregel in Kl. 8 eingeführt ist, betrifft den Plan.')

baue = mit_befunden(baue, BF)
# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Kl. 8, siehe _durchsicht_kl8.py) ----
from _durchsicht_kl8 import Durchsicht, mit_durchsicht  # noqa: E402

DSX = Durchsicht('stochastik.grundbegriffe', 19_8_10)
# rel_haeufigkeit: viermal „Zwei Gruppen …“ in Reihe → zwei ersetzt
DSX.ersetze('rel_haeufigkeit', 'Zwei Gruppen werfen einen Würfel: Gruppe A 200-mal mit 37 Sechsen, Gruppe B 20-mal mit 3 Sechsen. Wie groß ist die relative Häufigkeit der Sechs insgesamt in Prozent? (Runde auf eine Nachkommastelle.)', DSX.A(
    'Gruppe A hat 100-mal gewürfelt (17 % Sechsen), Gruppe B 25-mal (12 % Sechsen). Mia rechnet für beide zusammen (17 % + 12 %) : 2 = 14,5 %. Was stimmt?',
    'Falsch: Die Gruppen sind verschieden groß. Richtig ist (17 + 3) : 125 = 16 %.',
    ['Richtig: Man nimmt den Mittelwert der beiden Anteile.', 'Falsch: Man muss die Anteile addieren, also 29 %.', 'Falsch: Richtig ist 17 % – die größere Gruppe zählt allein.'],
    'A hatte 17 Sechsen, B 3 Sechsen (12 % von 25). Zusammen 20 Sechsen bei 125 Würfen: 20 : 125 = 0,16 = 16 %. Der einfache Mittelwert wäre nur bei gleich großen Gruppen richtig.',
    'Rechne die absoluten Häufigkeiten aus und addiere sie.'))
DSX.ersetze('rel_haeufigkeit', 'Zwei Gruppen werfen einen Würfel: Gruppe A 50-mal mit 6 Sechsen, Gruppe B 20-mal mit 3 Sechsen. Wie groß ist die relative Häufigkeit der Sechs insgesamt in Prozent? (Runde auf eine Nachkommastelle.)', DSX.Z(
    'Ein Würfel wird 300-mal geworfen. Die relative Häufigkeit der 1 ist 0,15, die der 2 ist 0,2. Wie oft fiel eine 1 oder eine 2?', 105, '300 * (15/100 + 20/100)',
    'Einsen: 0,15 · 300 = 45. Zweien: 0,2 · 300 = 60. Zusammen 105-mal.', 'Rechne aus den relativen Häufigkeiten die absoluten aus.'))
DSX.stufen('rel_haeufigkeit', 'S1 rel. Häufigkeit berechnen; S2 Tabelle, rückwärts; S3 viermal „zwei Gruppen zusammen“',
           'S1 berechnen; S2 aus Tabelle/Diagramm, rückwärts zur absoluten Häufigkeit; S3 Gruppen zusammenlegen, Fehler beim Mitteln, Rest, nötige weitere Treffer, Vergleich mit 1/6')
# laplace_pruefen: einfache Ja-Fälle auf Stufe 2 sind Stufe-1-Aufgaben
for _t in ['Ist das ein Laplace-Experiment? Werfen einer fairen Münze.', 'Ist das ein Laplace-Experiment? Werfen eines fairen Spielwürfels.',
           'Ist das ein Laplace-Experiment? Ein Glücksrad mit 10 gleich großen Feldern.']:
    DSX.stufe('laplace_pruefen', _t, 1)
DSX.stufen('laplace_pruefen', 'S1 und S2 teils dieselbe Ja/Nein-Frage', 'S1 Ja/Nein mit Begründung; S2 Glücksrad mit Winkeln, Farbe statt Kugel, Augensumme; S3 Lotto-Irrtum, Winkel planen, Feld gedanklich teilen, Serie deuten')
# gegenereignis: 100 % − p ist Stufe 1; einfache „NICHT“-Wahrscheinlichkeiten sind Stufe 2
for _t in ['Die Wahrscheinlichkeit, dass ein Elfmeter verwandelt wird, beträgt 81 %. Wie groß ist die Wahrscheinlichkeit, dass er nicht verwandelt wird (in %)?',
           'Die Wahrscheinlichkeit, dass ein Zug pünktlich ist, beträgt 89 %. Wie groß ist die Wahrscheinlichkeit, dass er nicht pünktlich ist (in %)?',
           'Die Wahrscheinlichkeit, dass ein Elfmeter verwandelt wird, beträgt 76 %. Wie groß ist die Wahrscheinlichkeit, dass er nicht verwandelt wird (in %)?',
           'Die Wahrscheinlichkeit, dass ein Elfmeter verwandelt wird, beträgt 82 %. Wie groß ist die Wahrscheinlichkeit, dass er nicht verwandelt wird (in %)?',
           'Die Wahrscheinlichkeit, dass ein Zug pünktlich ist, beträgt 83 %. Wie groß ist die Wahrscheinlichkeit, dass er nicht pünktlich ist (in %)?']:
    DSX.stufe('gegenereignis', _t, 1)
DSX.stufe('gegenereignis', 'Ein Glücksrad hat 10 gleich große Felder mit den Zahlen 1 bis 10. Wie groß ist die Wahrscheinlichkeit, dass die Zahl NICHT durch 3 teilbar ist? Gib sie als Dezimalzahl an.', 2)
DSX.stufe('gegenereignis', 'Ein Spielwürfel wird einmal geworfen. Wie groß ist die Wahrscheinlichkeit, dass KEINE Primzahl fällt? Gib sie als Dezimalzahl an.', 2)
DSX.stufen('gegenereignis', 'S1 und S2 dieselbe Rechnung 100 % − p; S3 teils einfache Laplace-Gegenwahrscheinlichkeit',
           'S1 100 % − p; S2 Gegenereignis in Worten, „nicht durch 3 teilbar“; S3 mindestens eine Sechs, zwei Ereignisse, Überschneidung, keine 7, P(E) = 3 · P(Ē)')
DSX.stufe('grosse_zahlen', 'Wie oft erwartest du bei 100 Versuchen ungefähr Wappen beim Münzwurf?', 1)
DSX.ersetze('grosse_zahlen', 'Welche Aussage ist FALSCH?', DSX.A(
    'Serie A: 50 Münzwürfe, 30-mal Wappen. Serie B: 5 000 Münzwürfe, 2 560-mal Wappen. Was stimmt?',
    'B weicht in der Anzahl stärker von der Hälfte ab (60 statt 5), aber der Anteil liegt näher an 50 %.',
    ['B weicht in Anzahl und Anteil stärker ab.', 'A weicht in Anzahl und Anteil stärker ab.', 'Beide weichen gleich stark ab, denn beide haben mehr Wappen.'],
    'A: Hälfte wäre 25, also 5 mehr; Anteil 60 %. B: Hälfte wäre 2 500, also 60 mehr; Anteil 51,2 %. Das Gesetz der großen Zahlen sagt: Der Anteil nähert sich 50 %, die Anzahl muss es nicht.',
    'Vergleiche getrennt: Abweichung der Anzahl und Abweichung des Anteils.'), enthaelt='"index": 2')
DSX.stufen('grosse_zahlen', 'S1 n · P; S2 teils dieselbe Rechnung; S3 zweimal dieselbe Roulette-Aussage',
           'S1 n · P; S2 n · P mit Bruch, P schätzen, Winkel; S3 Fehlvorstellungen, Anzahl gegen Anteil, Schätzung vergleichen, Gegenereignis aus Schätzung')
DSX.stufen('begriffe', 'S1 Ergebnisraum zählen; S2 Ereignis als Menge; S3 zwei Würfel, Reihenfolge, Ereignis in Worten, Zählen bis 100')
DSX.stufen('laplace', 'S1 Urne; S2 Würfel, Karten, Glücksrad (Bruch und Dezimalzahl); S3 Kugeln dazulegen, Augensumme, Säcke mischen')
baue = mit_durchsicht(baue, DSX)
# ---- DURCHSICHT ENDE ----

# ---- STUFEN (Zwanzigste Runde: echte Stufe 3 und Knobel-Bordkarten, siehe _stufen_kl8.py) ----
from _stufen_kl8 import Stufen, mit_stufen  # noqa: E402

ST = Stufen('stochastik.grundbegriffe', 20_8_13)
SA, SZ, SL = ST.A, ST.Z, ST.L
def T(lz, *regeln):
    for m, g in regeln: ST.typ(lz, m, g)

# --- begriffe ---
ST.leiter('begriffe', 'Ergebnisraum einfacher Versuche nennen und zählen',
          'Ereignis als Menge schreiben, Ergebnisse eines Ereignisses zählen, anderer Ergebnisraum (Anzahl Wappen), Lose',
          'Zahlenpaare zählen, Reihenfolge begründen, Ereignis in Worten rückwärts, Ziffern zählen, zwei Bedingungen verknüpfen, Augensumme')
T('begriffe', (r'Augensumme', 'transfer'), (r'Wie viele Ergebnisse hat der Ergebnisraum\?$|Wie viele Ergebnisse hat der Ergebnisraum bei', 'direkt'), (r'Welche Menge beschreibt', 'darstellung'),
  (r'nur, wie oft Wappen|keine Primzahl', 'mehrschritt'), (r'4 Flächen|Nummern 1 bis 30', 'verknuepfen'), (r'Welcher Ergebnisraum ist richtig', 'begruenden'),
  (r'in Worten', 'rueckwaerts'), (r'entält|enthält|Augensumme', 'transfer'), (r'genau zwei', 'pruefung'))
ST.neu('begriffe', 'erkennen', SA('Was ist der Ergebnisraum beim einmaligen Werfen einer Münze?', 'Ω = {Wappen; Zahl}', ['Ω = {Wappen}', 'Ω = {1; 2}', 'Ω = {Wappen; Zahl; Rand}'], 'Alle möglichen Ergebnisse: Wappen oder Zahl.', 'Was kann alles oben liegen?'))
ST.neu('begriffe', 'einkleidung', SZ('Aus 50 Losen mit den Nummern 1 bis 50 wird eines gezogen. Wie viele Ergebnisse gehören zum Ereignis „Nummer ist durch 10 teilbar“?', 5, '50 // 10', '10, 20, 30, 40, 50 – fünf Ergebnisse.', 'Schreibe die passenden Nummern auf.'))
ST.neu('begriffe', 'parameter', SZ('Ein Glücksrad hat n Felder mit den Nummern 1 bis n. Es wird zweimal gedreht, notiert wird das Zahlenpaar. Der Ergebnisraum hat 49 Ergebnisse. Wie groß ist n?', 7, '7',
    'Zahlenpaare: n · n = 49 ⇒ n = 7.', 'Wie viele Paare gibt es bei n Feldern?'))
ST.knobel('begriffe', SZ('Eine Münze wird dreimal geworfen (Reihenfolge zählt). Wie viele verschiedene Ereignisse gibt es, die aus genau zwei Ergebnissen bestehen?', 28, '8 * 7 / 2',
    'Der Ergebnisraum hat 2 · 2 · 2 = 8 Ergebnisse. Ein Ereignis aus zwei Ergebnissen ist eine Auswahl von 2 aus 8: 8 · 7 : 2 = 28 (durch 2, weil die Reihenfolge der Auswahl egal ist).',
    'Zähle zuerst die Ergebnisse, dann die Paare daraus.'))
ST.knobel('begriffe', SZ('Zwei Spielwürfel werden geworfen, notiert wird das Produkt der Augenzahlen. Wie viele Ergebnisse hat dieser Ergebnisraum?', 18, '18',
    'Mögliche Produkte: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 30, 36. Viele kommen mehrfach vor (z. B. 6 = 1 · 6 = 2 · 3), zählen aber nur einmal: 18 Ergebnisse.',
    'Schreibe die Einmaleins-Tafel bis 6 · 6 und streiche doppelte Werte.'))

# --- rel_haeufigkeit ---
ST.leiter('rel_haeufigkeit', 'relative Häufigkeit = Anzahl : Gesamtzahl berechnen',
          'aus Tabelle und Säulendiagramm, Prozent, absolute Häufigkeit rückwärts, Klassen-Beispiel',
          'Gruppen zusammenlegen, Mittelwert-Fehler, Rest berechnen, Bruch/Prozent verknüpfen, nötige Treffer rückwärts, Vergleich begründen')
T('rel_haeufigkeit', (r'^Bei \d+ Würfen kam', 'direkt'), (r'Tabelle zeigt|Säulendiagramm', 'darstellung'), (r'Wie oft trat es ein|Kronkorken', 'umkehr'), (r'Brille', 'einkleidung'),
  (r'^Zwei Gruppen|Umfrage', 'verknuepfen'), (r'Mia rechnet', 'fehler'), (r'300-mal|nächsten 10', 'rueckwaerts'), (r'Glücksrad wurde', 'pruefung'), (r'^Lea', 'begruenden'))
ST.neu('rel_haeufigkeit', 'erkennen', SA('Was gibt die relative Häufigkeit an?', 'den Anteil der Versuche, bei denen das Ergebnis eintrat', ['wie oft das Ergebnis insgesamt eintrat', 'die Anzahl aller Versuche', 'wie wahrscheinlich das Ergebnis sicher ist'],
    'Relativ heißt: im Verhältnis zur Zahl aller Versuche. 12 Sechsen bei 60 Würfen sind 12/60 = 0,2.', 'Was ist der Unterschied zwischen „wie oft“ und „welcher Anteil“?'))
ST.neu('rel_haeufigkeit', 'direkt', SZ('Ein Glücksrad wurde 40-mal gedreht und blieb 10-mal auf Gelb stehen. Wie groß ist die relative Häufigkeit von Gelb in Prozent?', 25, '10 / 40 * 100', '10 : 40 = 0,25 = 25 %.', 'Anzahl durch Gesamtzahl.', einheit='%'))
ST.neu('rel_haeufigkeit', 'erkennen', SA('Welche Zahl kann KEINE relative Häufigkeit sein?', '1,2', ['0', '0,5', '1'], 'Eine relative Häufigkeit liegt immer zwischen 0 und 1 (0 % bis 100 %), denn der Teil ist nie größer als das Ganze.', 'Kann ein Ergebnis öfter eintreten, als man Versuche macht?'))
ST.knobel('rel_haeufigkeit', SZ('Nach 20 Würfen ist die relative Häufigkeit der Sechs 0,25. Wie viele weitere Würfe ohne Sechs braucht man mindestens, damit sie unter 0,2 fällt?', 6, '5 / (2/10) - 20 + 1',
    'Es gab 5 Sechsen. Nach n weiteren Würfen ohne Sechs: 5 : (20 + n) < 0,2 ⇒ 20 + n > 25 ⇒ n > 5. Bei n = 5 ist es genau 0,2, also braucht man 6.',
    'Die Zahl der Sechsen bleibt gleich – nur der Nenner wächst.'))
ST.knobel('rel_haeufigkeit', SZ('Eine Münze wird 10-mal geworfen, danach ist die relative Häufigkeit von Wappen 0,6. Nach 10 weiteren Würfen ist sie 0,45. Wie oft kam Wappen in den zweiten 10 Würfen?', 3, '45/100 * 20 - 6',
    'Nach 10 Würfen: 6 Wappen. Nach 20 Würfen: 0,45 · 20 = 9 Wappen. In den zweiten 10 also 9 − 6 = 3.', 'Rechne beide relativen Häufigkeiten in Anzahlen um.'))

# --- laplace ---
ST.leiter('laplace', 'P = günstige : mögliche Ergebnisse bei einer Urne berechnen',
          'Würfel, Skatblatt, Glücksrad (Bruch und Dezimalzahl), Rest-Farbe bestimmen',
          'Kugeln dazulegen rückwärts, Augensummen zweier Würfel, Säcke mischen begründen, „zweite größer“ verknüpfen')
T('laplace', (r'^In einer Urne liegen \d+ rote( Kugeln)?, \d+ blaue', 'direkt'), (r'Skatblatt', 'einkleidung'), (r'Rest blau', 'umkehr'), (r'^Ein fairer Würfel|Glücksrad hat \d+ gleich|Nummern 1 bis 20', 'mehrschritt'),
  (r'dazulegen', 'rueckwaerts'), (r'größer als 10', 'pruefung'), (r'Augensumme', 'transfer'), (r'Säckchen', 'begruenden'), (r'zweite Zahl größer', 'verknuepfen'))
ST.neu('laplace', 'erkennen', SA('Wann darf man P(E) = Anzahl günstiger : Anzahl möglicher Ergebnisse rechnen?', 'wenn alle Ergebnisse gleich wahrscheinlich sind', ['bei jedem Zufallsversuch', 'nur bei Würfeln', 'nur wenn es zwei Ergebnisse gibt'],
    'Das ist die Laplace-Regel; sie gilt nur bei gleich wahrscheinlichen Ergebnissen (z. B. fairer Würfel oder gut gemischte Karten).', 'Wie heißt diese Regel, und welche Voraussetzung hat sie?'))
ST.neu('laplace', 'fehler', SA('Tom sagt: „Bei zwei Würfeln ist die Augensumme 2 genauso wahrscheinlich wie die Summe 7, denn beides ist eine von 11 möglichen Summen.“ Was stimmt?', 'Falsch: Die 11 Summen sind nicht gleich wahrscheinlich; P(2) = 1/36, P(7) = 6/36.',
    ['Richtig, beide haben 1/11.', 'Falsch: Die 2 ist wahrscheinlicher.', 'Falsch: Beide haben 1/36.'],
    'Laplace geht nur mit gleich wahrscheinlichen Ergebnissen – das sind die 36 Zahlenpaare. Die 2 kommt nur als (1|1), die 7 als (1|6), (2|5), (3|4), (4|3), (5|2), (6|1).', 'Zähle die Zahlenpaare für jede Summe.'))
ST.knobel('laplace', SZ('In einer Urne ist P(rot) = 2/5. Legt man 4 rote Kugeln dazu, ist P(rot) = 1/2. Wie viele Kugeln waren ursprünglich in der Urne?', 20, '(4 - 2) / (1/2 - 2/5)',
    'Mit n Kugeln sind 0,4n rot. (0,4n + 4) : (n + 4) = 0,5 ⇒ 0,4n + 4 = 0,5n + 2 ⇒ 0,1n = 2 ⇒ n = 20 (8 rote). Probe: 12/24 = 1/2.', 'Schreibe die Zahl der roten Kugeln mit n.'))
ST.knobel('laplace', SZ('Aus den Zahlen 1 bis 30 wird eine zufällig gezogen. Wie groß ist die Wahrscheinlichkeit, dass sie durch 2 oder durch 3 teilbar ist? Gib sie als Dezimalzahl auf zwei Nachkommastellen an.', 0.67, 'round((15 + 10 - 5) / 30, 2)',
    'Durch 2: 15 Zahlen. Durch 3: 10 Zahlen. Durch beide (durch 6): 5 Zahlen – sonst doppelt gezählt. 15 + 10 − 5 = 20 günstige: 20/30 ≈ 0,67.', 'Achte auf Zahlen, die du doppelt zählst.', toleranz=0.01))

# --- laplace_pruefen ---
ST.leiter('laplace_pruefen', 'entscheiden, ob alle Ergebnisse gleich wahrscheinlich sind',
          'Glücksrad mit Winkeln, Farbe statt Kugel, Augensumme als Ergebnis',
          'Lotto-Irrtum, Winkel planen, Feld gedanklich teilen, Serie deuten, Parameter für Winkel, rückwärts zur fairen Urne, Prüfungsauswahl')
T('laplace_pruefen', (r'^Ist das ein Laplace-Experiment\?', 'erkennen'), (r'^Ein Glücksrad hat die Felder A \d+°, B', 'mehrschritt'), (r'Urne mit 3 roten', 'einkleidung'), (r'Augensumme', 'umkehr'),
  (r'^Lisa', 'fehler'), (r'jeder zweiten', 'transfer'), (r'trotzdem mit Laplace', 'verknuepfen'), (r'7-mal', 'begruenden'))
ST.neu('laplace_pruefen', 'direkt', SA('Ein Spielwürfel ist fair. Wie wahrscheinlich ist jede einzelne Augenzahl?', '1/6', ['1/2', '1/3', '1/12'], 'Sechs gleich wahrscheinliche Ergebnisse: jedes hat 1/6.', 'Wie viele Seiten hat der Würfel?'))
ST.neu('laplace_pruefen', 'parameter', SZ('Ein Glücksrad hat vier Felder: drei mit je a° und eines mit 2a°. Wie groß ist a?', 72, '360 / 5', '3a + 2a = 360° ⇒ a = 72°. Das große Feld (144°) ist doppelt so wahrscheinlich – kein Laplace-Rad.', 'Alle Winkel zusammen ergeben 360°.', einheit='°'))
ST.neu('laplace_pruefen', 'rueckwaerts', SZ('Eine Urne enthält 7 rote und 12 blaue Kugeln. „Farbe ziehen“ soll ein Laplace-Experiment werden. Wie viele rote Kugeln muss man dazulegen?', 5, '12 - 7',
    'Beide Farben müssen gleich wahrscheinlich sein, also gleich viele: 12 rote. 12 − 7 = 5.', 'Wann sind „rot“ und „blau“ gleich wahrscheinlich?'))
ST.neu('laplace_pruefen', 'pruefung', SA('Welches Experiment ist ein Laplace-Experiment?', 'aus 1 roten, 1 blauen und 1 grünen Kugel eine ziehen und die Farbe notieren',
    ['eine Reißzwecke werfen', 'zwei Würfel werfen und die Augensumme notieren', 'aus 2 roten und 1 blauen Kugel eine ziehen und die Farbe notieren'],
    'Nur bei je einer Kugel pro Farbe sind die drei Farben gleich wahrscheinlich.', 'Prüfe jeweils, ob alle Ergebnisse gleich wahrscheinlich sind.'))
ST.neu('laplace_pruefen', 'darstellung', SA('Eine Strichliste nach 600 Würfen eines Würfels zeigt: 1: 98, 2: 103, 3: 97, 4: 101, 5: 99, 6: 102. Was passt am besten?', 'Der Würfel verhält sich wie ein Laplace-Würfel.',
    ['Der Würfel ist gezinkt, weil nicht alle Zahlen gleich oft kamen.', 'Die 2 ist sicher wahrscheinlicher als die 3.', 'Man kann aus der Liste gar nichts schließen.'],
    'Erwartet sind je etwa 100. Abweichungen von wenigen Würfen sind bei Zufall normal – nichts spricht gegen gleich wahrscheinliche Augenzahlen.', 'Wie oft erwartest du jede Zahl bei 600 Würfen?'))
ST.neu('laplace_pruefen', 'begruenden', SA('Ein Quader-Würfel ist 1 cm × 2 cm × 3 cm groß; die Flächen sind mit 1 bis 6 beschriftet. Warum ist Werfen damit kein Laplace-Experiment?', 'Die Flächen sind verschieden groß, große Flächen liegen öfter unten bzw. oben.',
    ['Weil er nur sechs Flächen hat.', 'Weil die Zahlen nicht gleich groß gedruckt sind.', 'Er ist doch ein Laplace-Experiment.'],
    'Ein Körper landet bevorzugt auf großen, stabilen Flächen. Gleich wahrscheinlich sind die Seiten nur bei einem symmetrischen Würfel.', 'Welche Seite ist am stabilsten?'))
ST.knobel('laplace_pruefen', SA('Zwei Münzen werden geworfen; notiert wird nur „gleich“ (beide Wappen oder beide Zahl) oder „verschieden“. Ist das ein Laplace-Experiment?', 'Ja: Beide Ergebnisse haben die Wahrscheinlichkeit 1/2.',
    ['Nein, „gleich“ ist wahrscheinlicher.', 'Nein, „verschieden“ ist wahrscheinlicher.', 'Das lässt sich nicht entscheiden.'],
    'Die vier gleich wahrscheinlichen Ausgänge WW, ZZ, WZ, ZW verteilen sich 2 : 2 auf „gleich“ und „verschieden“.', 'Schreibe die vier Ausgänge mit Reihenfolge auf.'))
ST.knobel('laplace_pruefen', SA('Mit einem fairen Würfel soll ein Laplace-Experiment mit genau 4 gleich wahrscheinlichen Ergebnissen gebaut werden. Wie geht es?', 'Würfeln; bei 5 oder 6 noch einmal würfeln, sonst zählt die Zahl 1 bis 4.',
    ['Die Augenzahl durch 2 teilen und runden.', 'Die Augenzahlen 1–2, 3, 4 und 5–6 zusammenfassen.', 'Das ist unmöglich.'],
    'Wiederholt man bei 5 und 6, bleiben am Ende nur 1, 2, 3, 4 – und die sind gleich wahrscheinlich. Beim Zusammenfassen wären 1–2 und 5–6 doppelt so wahrscheinlich.', 'Was passiert, wenn man bestimmte Ergebnisse einfach nicht gelten lässt?'))

# --- gegenereignis ---
ST.leiter('gegenereignis', 'P(nicht E) = 100 % − P(E) berechnen, das Gegenereignis benennen',
          '„nicht durch 3 teilbar“, „keine Primzahl“ über das Gegenereignis, Sachbeispiel, E aus dem Gegenereignis finden',
          'mindestens eine Sechs, zwei Ereignisse und Überschneidung verknüpfen, „keine 7“, P(E) = 3 · P(Ē), falsches Gegenereignis, begründen warum P + P = 1')
T('gegenereignis', (r'beträgt \d+ %', 'direkt'), (r'Wie heißt das Gegenereignis', 'darstellung'), (r'NICHT|KEINE Primzahl', 'mehrschritt'),
  (r'mindestens eine Sechs|KEINE 7', 'transfer'), (r'weder rot noch blau|Bäumen', 'verknuepfen'), (r'dreimal so groß', 'parameter'))
ST.neu('gegenereignis', 'erkennen', SA('Ein Würfel wird einmal geworfen. Was ist das Gegenereignis zu „gerade Zahl“?', 'ungerade Zahl', ['Zahl größer als 3', 'die Sechs', 'keine Sechs'], 'Gegenereignis = alle anderen Ergebnisse: {1; 3; 5}.', 'Welche Ergebnisse bleiben übrig?'))
ST.neu('gegenereignis', 'einkleidung', SZ('In einer Tüte sind 20 Gummibärchen, 7 davon rot. Wie groß ist die Wahrscheinlichkeit, KEIN rotes zu ziehen? Gib sie als Dezimalzahl an.', 0.65, '13 / 20', '20 − 7 = 13 nicht rote: 13/20 = 0,65 (oder 1 − 0,35).', 'Zähle die nicht roten oder rechne mit dem Gegenereignis.'))
ST.neu('gegenereignis', 'umkehr', SA('Das Gegenereignis von E ist „höchstens eine Sechs bei drei Würfen“. Wie heißt E?', 'mindestens zwei Sechsen', ['genau eine Sechs', 'keine Sechs', 'höchstens zwei Sechsen'],
    'Höchstens eine heißt 0 oder 1. Alles andere – 2 oder 3 Sechsen – ist „mindestens zwei“.', 'Welche Anzahlen sind in „höchstens eine“ enthalten, welche nicht?'))
ST.neu('gegenereignis', 'fehler', SA('Jemand sagt: Das Gegenereignis von „mindestens eine Sechs“ ist „höchstens eine Sechs“. Was stimmt?', 'Falsch: Es ist „keine Sechs“.', ['Richtig.', 'Falsch: Es ist „genau eine Sechs“.', 'Falsch: Es ist „mindestens zwei Sechsen“.'],
    '„Genau eine Sechs“ gehört zu beiden Ereignissen – Gegenereignisse dürfen sich nicht überschneiden. Das Gegenteil von „mindestens eine“ ist „gar keine“.', 'Gibt es Ergebnisse, die zu beiden Ereignissen gehören?'))
ST.neu('gegenereignis', 'begruenden', SA('Warum gilt P(E) + P(Ē) = 1?', 'Bei jedem Versuch tritt genau eines von beiden ein.', ['Weil beide Wahrscheinlichkeiten 0,5 sind.', 'Weil man immer 100 Versuche macht.', 'Das gilt nur bei Würfeln.'],
    'E und Ē teilen den Ergebnisraum ohne Überschneidung auf. Zusammen sind sie sicher – das hat die Wahrscheinlichkeit 1.', 'Kann beides gleichzeitig passieren? Kann keines passieren?'))
ST.knobel('gegenereignis', SZ('Drei Münzen werden geworfen. Wie groß ist die Wahrscheinlichkeit für mindestens einmal Wappen? Gib sie als Dezimalzahl an.', 0.875, '1 - 1/8',
    'Gegenereignis: dreimal Zahl, P = 1/2 · 1/2 · 1/2 = 1/8. Also 1 − 1/8 = 7/8 = 0,875.', 'Das Gegenereignis ist viel einfacher zu zählen.'))
ST.knobel('gegenereignis', SZ('Wie oft muss man eine Münze mindestens werfen, damit die Wahrscheinlichkeit für „mindestens einmal Zahl“ größer als 0,95 ist?', 5, '5',
    'Gegenereignis: n-mal Wappen, P = (1/2)ⁿ. Gesucht: 1 − (1/2)ⁿ > 0,95, also (1/2)ⁿ < 0,05. 1/16 = 0,0625 reicht nicht, 1/32 ≈ 0,031 schon: n = 5.', 'Rechne mit dem Gegenereignis „nur Wappen“.'))

# --- grosse_zahlen ---
ST.leiter('grosse_zahlen', 'erwartete Anzahl = Versuche · Wahrscheinlichkeit',
          'Glücksrad mit Anteil, Wahrscheinlichkeit aus vielen Würfen schätzen, Winkel als Wahrscheinlichkeit',
          'Fehlvorstellungen (Roulette) begründen, Anzahl gegen Anteil, Schätzungen vergleichen, Gegenereignis aus Schätzung, „ausgleichen“ als Fehler')
T('grosse_zahlen', (r'^Wie oft erwartest du bei \d+ Versuchen ungefähr (Wappen|eine Sechs)|mit 4 gleichen Feldern', 'direkt'), (r'Glücksrad mit \d+ gleichen', 'mehrschritt'),
  (r'Schätze die Wahrscheinlichkeit', 'umkehr'), (r'größer als 4', 'einkleidung'), (r'90°', 'darstellung'), (r'FALSCH', 'begruenden'), (r'^Anna|gerade Zahl', 'transfer'),
  (r'^Serie', 'verknuepfen'), (r'1/3', 'pruefung'), (r'Gewinnspiel', 'fehler'), (r'Reißnagel', 'rueckwaerts'))
ST.neu('grosse_zahlen', 'erkennen', SA('Was sagt das Gesetz der großen Zahlen?', 'Bei sehr vielen Versuchen liegt die relative Häufigkeit meist nahe an der Wahrscheinlichkeit.',
    ['Bei vielen Versuchen tritt jedes Ergebnis genau gleich oft auf.', 'Nach vielen Fehlversuchen wird ein Treffer wahrscheinlicher.', 'Die absolute Häufigkeit wird immer genauer vorhersagbar.'],
    'Der Anteil pendelt sich ein, die Anzahl muss es nicht; und der Zufall „merkt sich“ nichts.', 'Geht es um Anzahlen oder um Anteile?'))
ST.knobel('grosse_zahlen', SZ('Ein Würfel wird 6 000-mal geworfen. Wie oft erwartest du ungefähr eine Augenzahl, die eine Primzahl oder die 1 ist?', 4000, '6000 * 4 / 6',
    'Primzahlen bis 6: 2, 3, 5; dazu die 1 – vier von sechs Ergebnissen. 4/6 · 6 000 = 4 000.', 'Welche Augenzahlen gehören dazu?'))
ST.knobel('grosse_zahlen', SA('Ein Kronkorken lag bei 1 000 Würfen 380-mal „oben“. Er wird noch 1 000-mal geworfen. Welche Aussage ist am vernünftigsten?', 'Man erwartet wieder etwa 380-mal „oben“, genau vorhersagen kann man es nicht.',
    ['Jetzt kommt öfter „oben“, damit es ausgeglichen wird.', 'Es kommt genau 380-mal „oben“.', 'Man kann gar nichts erwarten.'],
    'Die Schätzung P ≈ 0,38 gilt weiter; der Kronkorken gleicht nichts aus. Wegen des Zufalls wird es meist nicht genau 380 sein.', 'Hat der Kronkorken ein Gedächtnis?'))
baue = mit_stufen(baue, ST)
# ---- STUFEN ENDE ----

# ---------- TEXT: Zweiundzwanzigste Runde (18.11., Auftrag des Lehrers) – mehr Textaufgaben, siehe _text_kl8.py ----------
from _text_kl8 import Text, mit_text, text_auf_datei  # noqa: E402
TX = Text('stochastik.grundbegriffe', 22_8_13)
TZ, TA, TL, TW = TX.Z, TX.A, TX.L, TX.W

# --- begriffe ---
TX.u('begriffe', 'einkleidung', TZ('Bei einer Tombola gibt es Lose mit den Nummern 1 bis 50. Gewinn gibt es für jede Nummer, die durch 10 teilbar ist. Wie viele Ergebnisse gehören zum Ereignis „Gewinn“?', '50 // 10',
    TW('Nummern 1 bis 50, Gewinn bei Vielfachen von 10.', 'Anzahl der Ergebnisse im Ereignis.', 'Alle passenden Nummern aufzählen.', '10, 20, 30, 40, 50.', 'Zum Ereignis „Gewinn“ gehören 5 Ergebnisse.'), 'Schreib die Gewinnnummern auf.'))
TX.u('begriffe', 'mehrschritt', TZ('In der Pause wird ausgelost, wer den Ball holt und wer ihn zurückbringt. In einem Becher liegen die Namen von 4 Mädchen und 3 Jungen; es wird zweimal ohne Zurücklegen gezogen. Wie viele Ergebnisse hat der Ergebnisraum (Reihenfolge zählt)?', '7 * 6',
    TW('7 Namen, zwei Züge ohne Zurücklegen, Reihenfolge zählt.', 'Anzahl der Ergebnisse.', 'Erster Zug 7 Möglichkeiten, zweiter nur noch 6.', '7 · 6 = 42.', 'Der Ergebnisraum hat 42 Ergebnisse.'), 'Wie viele Namen sind beim zweiten Zug noch im Becher?'))
TX.u('begriffe', 'pruefung', TZ('Ein Eiscafé bietet 6 Sorten an, eine Kugel kostet 1,60 €. Ein Kind wählt einen Becher mit zwei verschiedenen Sorten, die Reihenfolge ist egal. Wie viele verschiedene Becher gibt es?', '6 * 5 // 2',
    TW('6 Sorten, zwei verschiedene, Reihenfolge egal. Der Preis spielt keine Rolle.', 'Anzahl der Becher.', 'Paare mit Reihenfolge zählen und halbieren.', '6 · 5 = 30, jedes Paar doppelt: 30 : 2 = 15.', 'Es gibt 15 verschiedene Becher.'),
    'Ist Vanille–Erdbeere dasselbe wie Erdbeere–Vanille?'), huerde='ueberfluessig')
TX.u('begriffe', 'transfer', TZ('Ein Fahrradschloss hat 3 Ringe mit den Ziffern 0 bis 9. Wie viele Codes beginnen mit einer 7 und enden mit einer geraden Ziffer?', '1 * 10 * 5',
    TW('3 Ringe, Ziffern 0 bis 9; erste Ziffer 7, letzte gerade.', 'Anzahl der passenden Codes.', 'Möglichkeiten je Ring multiplizieren.', '1 · 10 · 5 = 50.', 'Es gibt 50 solche Codes.'), 'Wie viele Möglichkeiten hat jeder Ring unter den Bedingungen?'), huerde='zwei')
TX.s('begriffe', TZ('Für die Sitzordnung werden die Plätze 1 bis 30 verlost. Wer eine Nummer über 25 zieht, sitzt am Fenster. Wie viele Ergebnisse gehören zum Ereignis „Fensterplatz“?', '30 - 25',
    TW('Plätze 1 bis 30, Fenster ab 26.', 'Anzahl der Ergebnisse.', 'Nummern über 25 zählen.', '26, 27, 28, 29, 30.', 'Es sind 5 Ergebnisse.')))
TX.s('begriffe', TZ('Ein Schulbus hält an 5 Haltestellen. Für zwei Geschwister wird notiert, wo jedes aussteigt (als Paar). Wie viele Ergebnisse hat der Ergebnisraum?', '5 * 5',
    TW('5 Haltestellen, zwei Kinder.', 'Anzahl der Paare.', 'Jedes Kind hat 5 Möglichkeiten.', '5 · 5 = 25.', 'Der Ergebnisraum hat 25 Ergebnisse.')))
TX.k('begriffe', TZ('Der Klassensprecher wird aus 12 Kandidaten ausgelost, 5 davon sind Mädchen. Wie viele Ergebnisse gehören zum Ereignis „Ein Junge wird gezogen“?', '12 - 5',
    TW('12 Kandidaten, 5 Mädchen.', 'Anzahl der Jungen.', '12 − 5.', '7.', 'Zum Ereignis gehören 7 Ergebnisse.')))

# --- rel_haeufigkeit ---
TX.u('rel_haeufigkeit', 'direkt', TZ('Bei einer Verkehrszählung fuhren in einer Stunde 80 Fahrzeuge vorbei, 20 davon waren Lkw. Wie groß ist die relative Häufigkeit der Lkw?', '20 / 80',
    TW('80 Fahrzeuge, 20 Lkw.', 'relative Häufigkeit.', 'Anteil = absolute Häufigkeit : Anzahl.', '20 : 80 = 0,25.', 'Die relative Häufigkeit der Lkw ist 0,25.'), 'Teile die Zahl der Lkw durch alle Fahrzeuge.'))
TX.u('rel_haeufigkeit', 'einkleidung', TZ('In einer Umfrage unter 250 Schülerinnen und Schülern nannten 95 Fußball ihren Lieblingssport. Wie viel Prozent sind das?', '95 / 250 * 100',
    TW('250 Befragte, 95 Fußball.', 'Anteil in Prozent.', 'Relative Häufigkeit · 100 %.', '95 : 250 = 0,38 = 38 %.', 'Es sind 38 %.'), 'Was ist hier das Ganze?', einheit='%'))
TX.u('rel_haeufigkeit', 'pruefung', TZ('Ein Basketballspieler trifft im Training 42 von 60 Freiwürfen, im Spiel 15 von 25. Um wie viele Prozentpunkte ist seine Trefferquote im Training höher?', '42 / 60 * 100 - 15 / 25 * 100',
    TW('Training 42 von 60, Spiel 15 von 25.', 'Unterschied der Quoten.', 'Beide relativen Häufigkeiten in Prozent, dann abziehen.', '42 : 60 = 70 %, 15 : 25 = 60 %; 70 − 60 = 10.', 'Im Training ist die Quote 10 Prozentpunkte höher.'),
    'Vergleiche Anteile, nicht Trefferzahlen.'), huerde='zwei')
TX.u('rel_haeufigkeit', 'begruenden', TX.A('In Klasse A kommen 12 von 30 Kindern mit dem Rad, in Klasse B 10 von 20. Eine Schülerzeitung schreibt: „In Klasse A fahren mehr Kinder Rad.“ Was stimmt?',
    'Absolut stimmt es, aber der Anteil ist in B größer (50 % statt 40 %).', ['Es stimmt, A hat auch den größeren Anteil.', 'Es ist falsch, in B fahren mehr Kinder Rad.', 'Man kann Klassen verschiedener Größe nicht vergleichen.'],
    TW('A: 12 von 30, B: 10 von 20.', 'Ist die Aussage richtig?', 'Absolute und relative Häufigkeit unterscheiden.', 'A: 12 Kinder, 40 %. B: 10 Kinder, 50 %.', 'In A fahren mehr Kinder, aber in B ein größerer Anteil.'), 'Rechne beide Anteile aus.'), huerde='entscheidung')
TX.u('rel_haeufigkeit', 'rueckwaerts', TZ('Bei einer Umfrage hatten 18 % der Befragten ein Haustier, das waren 54 Kinder. Wie viele Kinder wurden befragt?', '54 / 0.18',
    TW('18 % entsprechen 54 Kindern.', 'Anzahl der Befragten.', 'Anzahl = absolute Häufigkeit : relative Häufigkeit.', '54 : 0,18 = 300.', 'Es wurden 300 Kinder befragt.'), 'Wie viele Kinder sind 1 %?'))
TX.s('rel_haeufigkeit', TZ('Ein Kronkorken wurde 200-mal geworfen und landete 74-mal auf dem Rücken. Wie groß ist die relative Häufigkeit für „Rücken“?', '74 / 200',
    TW('200 Würfe, 74-mal Rücken.', 'relative Häufigkeit.', '74 : 200.', '0,37.', 'Die relative Häufigkeit ist 0,37.')))
TX.s('rel_haeufigkeit', TZ('Von 40 verkauften Eisbechern waren 14 mit Schokolade. Wie viel Prozent sind das?', '14 / 40 * 100',
    TW('40 Becher, 14 Schokolade.', 'Anteil in Prozent.', '14 : 40 · 100 %.', '0,35 = 35 %.', 'Es sind 35 %.'), einheit='%'))

# --- laplace ---
TX.u('laplace', 'direkt', TZ('Bei einer Tombola gibt es 200 Lose, 40 davon gewinnen. Wie groß ist die Wahrscheinlichkeit, mit einem gekauften Los zu gewinnen?', '40 / 200',
    TW('200 Lose, 40 Gewinne.', 'Gewinnwahrscheinlichkeit.', 'P = günstige : alle.', '40 : 200 = 0,2.', 'Sie beträgt 0,2.'), 'Wie viele Lose sind günstig, wie viele möglich?'))
TX.u('laplace', 'einkleidung', TZ('In einer Tüte sind 8 Erdbeer-, 5 Zitronen- und 7 Kirschbonbons. Du greifst blind hinein. Wie groß ist die Wahrscheinlichkeit für Kirsche in Prozent?', '7 / 20 * 100',
    TW('8 + 5 + 7 = 20 Bonbons, 7 Kirsche.', 'P(Kirsche) in %.', 'P = günstige : alle.', '7 : 20 = 0,35 = 35 %.', 'Die Wahrscheinlichkeit ist 35 %.'), 'Wie viele Bonbons sind es insgesamt?', einheit='%'))
TX.u('laplace', 'pruefung', TL('Für eine Klassenfahrt werden 28 Kinder auf 7 Viererzimmer verlost, 2 Zimmer haben einen Balkon. Die Jugendherberge liegt 3 km vom Bahnhof entfernt. Wie groß ist die Wahrscheinlichkeit, in ein Balkonzimmer zu kommen? Gib sie gekürzt an.', 'P = □/□', ['2', '7'],
    TW('28 Plätze, 2 Balkonzimmer zu je 4 Plätzen. Die Entfernung spielt keine Rolle.', 'P(Balkonzimmer).', 'günstige Plätze : alle Plätze.', '8 : 28 = 2/7.', 'Die Wahrscheinlichkeit ist 2/7.'),
    'Zähle Plätze, nicht Zimmer – oder Zimmer, nicht Plätze; beides geht.', hinweis='Zähler und Nenner, gekürzt.'), huerde='ueberfluessig')
TX.u('laplace', 'begruenden', TX.A('Losbude A hat 30 Gewinne bei 120 Losen, Losbude B hat 20 Gewinne bei 70 Losen. Wo ist die Gewinnchance größer?',
    'Bei B (etwa 29 % statt 25 %).', ['Bei A, weil es dort mehr Gewinne gibt.', 'Bei beiden gleich.', 'Bei A (25 % statt 20 %).'],
    TW('A: 30 von 120, B: 20 von 70.', 'größere Gewinnchance.', 'Beide Wahrscheinlichkeiten berechnen.', 'A: 30 : 120 = 0,25. B: 20 : 70 ≈ 0,286.', 'Bei B ist die Chance größer.'), 'Vergleiche Anteile, nicht Anzahlen.'), huerde='entscheidung')

# --- laplace_pruefen ---
TX.u('laplace_pruefen', 'einkleidung', TX.A('Ein Kind wirft eine Reißzwecke und sagt: „Sie landet auf dem Kopf oder auf der Seite, also jeweils mit der Wahrscheinlichkeit 1/2.“ Was stimmt?',
    'Falsch: Die beiden Lagen sind nicht gleich wahrscheinlich, das ist kein Laplace-Experiment.', ['Richtig: Es gibt zwei Ergebnisse, also je 1/2.', 'Richtig, wie bei einer Münze.', 'Falsch: Die Wahrscheinlichkeit ist je 1/3.'],
    TW('Reißzwecke, zwei mögliche Lagen.', 'Gilt P = 1/2?', 'Laplace nur, wenn alle Ergebnisse gleich wahrscheinlich sind.', 'Form und Gewicht sind ungleich verteilt.', 'Die Aussage ist falsch; man muss die Wahrscheinlichkeit durch Versuche schätzen.'),
    'Sind beide Lagen wirklich gleich wahrscheinlich?'))
TX.u('laplace_pruefen', 'darstellung', TZ('Ein Glücksrad auf dem Schulfest hat ein Gewinnfeld mit 45° und ein Nietenfeld mit 315°. Wie groß ist die Gewinnwahrscheinlichkeit?', '45 / 360',
    TW('Gewinnfeld 45° von 360°.', 'P(Gewinn).', 'Anteil des Winkels am Vollkreis.', '45 : 360 = 0,125.', 'Die Gewinnwahrscheinlichkeit ist 0,125.'), 'Welcher Teil des ganzen Kreises ist das Gewinnfeld?'))
TX.u('laplace_pruefen', 'pruefung', TZ('Ein Glücksrad für das Schulfest soll so geteilt werden, dass der Hauptgewinn mit 5 % und ein Trostpreis mit 25 % kommt, der Rest ist Niete. Wie groß muss der Winkel des Nietenfeldes sein?', '(100 - 5 - 25) / 100 * 360',
    TW('Hauptgewinn 5 %, Trostpreis 25 %.', 'Winkel des Nietenfeldes.', 'Erst den Anteil der Nieten, dann · 360°.', '100 − 5 − 25 = 70 %. 0,7 · 360° = 252°.', 'Das Nietenfeld braucht 252°.'), 'Welcher Anteil bleibt für die Nieten?', einheit='°'), huerde='zwei')
TX.u('laplace_pruefen', 'begruenden', TX.A('In einer Box liegen 4 Zettel: auf 3 steht „Kino“, auf 1 „Zoo“. Jemand sagt: „Es kommt Kino oder Zoo, also je 50 %.“ Was stimmt?',
    'Falsch: P(Kino) = 3/4 = 75 %.', ['Richtig: zwei Ergebnisse, je 50 %.', 'Falsch: P(Kino) = 1/3.', 'Falsch: P(Zoo) = 75 %.'],
    TW('3 Kino-Zettel, 1 Zoo-Zettel.', 'Stimmt „je 50 %“?', 'Gleich wahrscheinlich sind die Zettel, nicht die Wörter.', 'P(Kino) = 3 : 4 = 0,75.', 'Die Aussage ist falsch: Kino kommt mit 75 %.'), 'Welche Ergebnisse sind wirklich gleich wahrscheinlich?'), huerde='entscheidung')
TX.s('laplace_pruefen', TZ('Auf dem Schulfest wird ein Rad mit 8 gleich großen Feldern gedreht, 2 Felder gewinnen. Wie groß ist die Gewinnwahrscheinlichkeit?', '2 / 8',
    TW('8 gleiche Felder, 2 Gewinne.', 'P(Gewinn).', '2 : 8.', '0,25.', 'Sie beträgt 0,25.')))
TX.k('laplace_pruefen', TZ('Ein Glücksrad hat ein Gewinnfeld mit 72°. Wie groß ist die Gewinnwahrscheinlichkeit in Prozent?', '72 / 360 * 100',
    TW('Gewinnfeld 72°.', 'P(Gewinn) in %.', '72 : 360.', '0,2 = 20 %.', 'Sie beträgt 20 %.'), einheit='%'))

# --- gegenereignis ---
TX.u('gegenereignis', 'einkleidung', TZ('Ein Zug ist mit der Wahrscheinlichkeit 0,85 pünktlich. Wie groß ist die Wahrscheinlichkeit, dass er nicht pünktlich ist?', '1 - 0.85',
    TW('P(pünktlich) = 0,85.', 'P(nicht pünktlich).', 'Gegenereignis: 1 − P.', '1 − 0,85 = 0,15.', 'Die Wahrscheinlichkeit ist 0,15.'), 'Beide zusammen ergeben was?'))
TX.u('gegenereignis', 'umkehr', TZ('Bei einer Tombola gewinnen 30 % der Lose nicht. Wie groß ist die Gewinnwahrscheinlichkeit in Prozent?', '100 - 30',
    TW('30 % Nieten.', 'Gewinnwahrscheinlichkeit.', 'Gewinn ist das Gegenereignis von Niete.', '100 % − 30 % = 70 %.', 'Die Gewinnwahrscheinlichkeit ist 70 %.'), 'Was ist das Gegenteil von „nicht gewinnen“?', einheit='%'))
TX.u('gegenereignis', 'pruefung', TZ('Der Wetterdienst sagt für Samstag 35 % Regen voraus, dazu 22 °C und Wind mit 15 km/h. Wie groß ist die Wahrscheinlichkeit in Prozent, dass es nicht regnet?', '100 - 35',
    TW('P(Regen) = 35 %. Temperatur und Wind spielen keine Rolle.', 'P(kein Regen).', 'Gegenereignis.', '100 − 35 = 65.', 'Mit 65 % regnet es nicht.'), 'Welche Angabe gehört zum Ereignis „Regen“?', einheit='%'), huerde='ueberfluessig')
TX.u('gegenereignis', 'begruenden', TX.A('Ein Bus hat mit der Wahrscheinlichkeit 0,2 Verspätung. Jemand sagt: „Dann kommt er in 80 % der Fälle zu früh.“ Was stimmt?',
    'Falsch: 80 % heißt „keine Verspätung“, also pünktlich oder zu früh.', ['Richtig, das ist das Gegenereignis.', 'Falsch: Er kommt in 20 % der Fälle zu früh.', 'Richtig: Wenn er nicht zu spät kommt, kommt er zu früh.'],
    TW('P(Verspätung) = 0,2.', 'Was bedeutet 0,8?', 'Das Gegenereignis von „Verspätung“ ist „keine Verspätung“.', '1 − 0,2 = 0,8 für „keine Verspätung“.', 'Die Aussage ist falsch: Die 80 % umfassen pünktlich und zu früh.'),
    'Was genau ist das Gegenteil von „Verspätung“?'), huerde='entscheidung')
TX.s('gegenereignis', TZ('Ein Handyakku hält mit der Wahrscheinlichkeit 0,92 einen ganzen Tag. Wie groß ist die Wahrscheinlichkeit, dass er vorher leer ist?', '1 - 0.92',
    TW('P(hält) = 0,92.', 'P(vorher leer).', '1 − 0,92.', '0,08.', 'Die Wahrscheinlichkeit ist 0,08.')))
TX.s('gegenereignis', TZ('An einer Losbude gewinnen 15 % der Lose. Wie viel Prozent der Lose sind Nieten?', '100 - 15',
    TW('15 % Gewinne.', 'Anteil der Nieten.', 'Gegenereignis.', '100 − 15 = 85.', '85 % sind Nieten.'), einheit='%'))

# --- grosse_zahlen ---
TX.u('grosse_zahlen', 'direkt', TZ('Ein Basketballspieler trifft Freiwürfe mit der Wahrscheinlichkeit 0,7. Wie viele Treffer erwartest du ungefähr bei 50 Würfen?', '50 * 0.7',
    TW('P = 0,7, 50 Würfe.', 'erwartete Treffer.', 'n · P.', '50 · 0,7 = 35.', 'Etwa 35 Treffer.'), 'Wie viel sind 70 % von 50?'))
TX.u('grosse_zahlen', 'einkleidung', TZ('An einer Kreuzung biegen erfahrungsgemäß 30 % der Autos links ab. Wie viele von 400 Autos biegen ungefähr links ab?', '400 * 0.3',
    TW('30 %, 400 Autos.', 'erwartete Anzahl.', 'n · P.', '400 · 0,3 = 120.', 'Etwa 120 Autos biegen links ab.'), 'Welchen Anteil von 400 suchst du?'))
TX.u('grosse_zahlen', 'pruefung', TZ('Ein Hersteller weiß: 2 % seiner Glühbirnen sind defekt. Ein Laden bestellt 1 250 Stück und will für die defekten Ersatz bereithalten; Ersatz gibt es nur in Packungen zu 10 Stück. Wie viele Packungen sollte er bereithalten?', '-(-(1250 * 2 // 100) // 10)',
    TW('2 % von 1 250, Packungen zu 10.', 'Anzahl der Packungen.', 'Erwartete defekte Birnen, dann durch 10 und aufrunden.', '1 250 · 0,02 = 25. 25 : 10 = 2,5.', 'Er sollte 3 Packungen bereithalten.'),
    'Wie viele defekte Birnen erwartest du, und reichen 2 Packungen?'), huerde='deuten')
TX.u('grosse_zahlen', 'begruenden', TX.A('Ein Kronkorken landete bei 20 Würfen 14-mal auf dem Rücken, bei 1 000 Würfen 560-mal. Welcher Wert schätzt die Wahrscheinlichkeit für „Rücken“ besser?',
    '0,56 – er beruht auf viel mehr Würfen.', ['0,7 – er ist größer.', 'Beide sind gleich gut.', '0,63 – der Mittelwert aus beiden.'],
    TW('20 Würfe: 0,7. 1 000 Würfe: 0,56.', 'besserer Schätzwert.', 'Gesetz der großen Zahlen: Viele Versuche schwanken weniger.', 'Bei 1 000 Würfen ist die relative Häufigkeit stabiler.', '0,56 ist der bessere Schätzwert.'),
    'Welche Messreihe ist zuverlässiger?'), huerde='entscheidung')
TX.s('grosse_zahlen', TZ('Erfahrungsgemäß kommen 15 % der angemeldeten Gäste nicht. Mit wie vielen Gästen rechnest du ungefähr bei 240 Anmeldungen?', '240 * 0.85',
    TW('240 Anmeldungen, 15 % kommen nicht.', 'erwartete Gäste.', '85 % von 240.', '240 · 0,85 = 204.', 'Etwa 204 Gäste kommen.')))
TX.s('grosse_zahlen', TZ('Ein Elfmeterschütze trifft mit der Wahrscheinlichkeit 75 %. Wie viele Treffer erwartest du bei 40 Elfmetern?', '40 * 0.75',
    TW('P = 0,75, 40 Schüsse.', 'erwartete Treffer.', 'n · P.', '40 · 0,75 = 30.', 'Etwa 30 Treffer.')))
TX.k('grosse_zahlen', TZ('Bei einer Lotterie gewinnt jedes 8. Los. Wie viele Gewinne erwartest du bei 480 Losen?', '480 / 8',
    TW('P = 1/8, 480 Lose.', 'erwartete Gewinne.', 'n · P.', '480 : 8 = 60.', 'Etwa 60 Gewinne.')))
baue = mit_text(baue, TX)
# ---- TEXT ENDE ----

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Grundbegriffe', ['begriffe', 'rel_haeufigkeit']), ('Wahrscheinlichkeiten', ['laplace', 'laplace_pruefen', 'gegenereignis']), ('Zufall auf Dauer', ['grosse_zahlen'])],
         'Zufallsexperimente beschreiben, relative Häufigkeiten bestimmen und Laplace-Wahrscheinlichkeiten berechnen; das Gesetz der großen Zahlen verstehen.',
         ['Ω = alle Ergebnisse, Ereignis = Teilmenge von Ω.', 'Relative Häufigkeit = absolute Häufigkeit : Anzahl der Versuche.',
          'Laplace: P(E) = günstige : alle (nur bei gleich wahrscheinlichen Ergebnissen).', 'P(Ē) = 1 − P(E).'],
         offen=['Urnen werden nur in Worten beschrieben (kein passender Bildtyp); Glücksräder als Kreisdiagramm, Häufigkeiten als Tabelle oder Säulendiagramm.'])
