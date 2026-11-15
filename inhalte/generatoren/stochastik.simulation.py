#!/usr/bin/env python3
"""Thema stochastik.simulation – Simulation (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import json
from _bausatz import A, Z, baue, bruch, cz, ist_endlich, mit_bild, zt  # noqa: E402

META = {'thema_schluessel': 'stochastik.simulation', 'thema_id': 64, 'block_id': 90, 'klasse': {'gym_by': 8, 'rs_by': 9}}

ETAPPEN = [
    {'lernziel': 'zufallsgeraet', 'titel': 'Ein passendes Zufallsgerät wählen',
     'regel': 'Beim ⟦Simulieren⟧ ersetzt man einen echten Vorgang durch ein ⟦Zufallsgerät⟧ mit ⟦derselben Wahrscheinlichkeit⟧: Münze (1/2), Würfel (1/6), Urne oder Glücksrad (beliebige Anteile).',
     'schritte': ['Ein Spieler trifft mit Wahrscheinlichkeit 0,3.', 'Urne mit 10 Kugeln: 3 rote = Treffer, 7 weiße = kein Treffer.', 'Ziehen ⟦mit Zurücklegen⟧ simuliert einen Wurf.'],
     'fehler': 'Eine Münze passt nicht für p = 0,3: Sie liefert immer ⟦p = 0,5⟧. Das Zufallsgerät muss genau die gesuchte Wahrscheinlichkeit haben.',
     '_verbot': ['Wahrscheinlichkeit 0,3']},
    {'lernziel': 'regel', 'titel': 'Eine Simulationsregel festlegen',
     'regel': 'Für p = 0,4 nimmt man ⟦4 von 10⟧ Ziffern als Treffer. Für p = 0,35 reichen einzelne Ziffern nicht: Man nimmt ⟦Zahlen von 00 bis 99⟧ und lässt 35 davon als Treffer gelten.',
     'schritte': ['p = 0,35 = 35/100', 'Zweistellige Zufallszahlen 00–99 (100 Stück)', 'Regel: ⟦00–34 = Treffer⟧, 35–99 = kein Treffer'],
     'fehler': 'Die Regel „00–35 = Treffer“ ist für p = 0,35 falsch: Von 00 bis 35 sind es ⟦36⟧ Zahlen.'},
    {'lernziel': 'zufallsziffern', 'titel': 'Mit Zufallsziffern simulieren',
     'regel': 'Zufallsziffern 0–9 kommen ⟦gleich oft⟧ vor (je 1/10). Man legt fest, welche Ziffern als ⟦Treffer⟧ zählen, z. B. 0, 1, 2 für p = 0,3, und zählt dann die Treffer.',
     'schritte': ['Regel: 0–2 = Treffer (p = 0,3)', 'Ziffern: 7 1 4 0 9 2 5 8 3 6', 'Treffer: 1, 0, 2 → ⟦3 Treffer⟧ in 10 Versuchen'],
     'fehler': 'Bei der Regel „0–2 = Treffer“ zählt die 2 mit. 0, 1 und 2 sind ⟦drei⟧ Ziffern, also p = 3/10.',
     '_verbot': ['7 1 4 0 9 2 5 8 3 6']},
    {'lernziel': 'auswerten', 'titel': 'Simulationen auswerten',
     'regel': 'Aus einer Simulation ⟦schätzt⟧ man eine Wahrscheinlichkeit durch die relative Häufigkeit: ⟦Anzahl der Treffer : Anzahl der Durchgänge⟧. Je mehr Durchgänge, desto zuverlässiger.',
     'schritte': ['200 Durchgänge, 46-mal trat „mindestens zwei Sechsen“ ein', 'Relative Häufigkeit 46 : 200 = 0,23', 'Schätzwert: ⟦P ≈ 0,23⟧'],
     'fehler': 'Die Simulation liefert keinen genauen Wert. 0,23 ist eine ⟦Schätzung⟧ – eine neue Simulation ergibt meist eine etwas andere Zahl.',
     '_verbot': ['200 Durchgänge, 46-mal']},
    {'lernziel': 'monte_carlo', 'titel': 'Monte-Carlo-Methode',
     'regel': 'Bei der ⟦Monte-Carlo-Methode⟧ setzt man zufällig viele Punkte in ein Quadrat. Der ⟦Anteil der Punkte⟧ in einer Figur schätzt den ⟦Anteil der Fläche⟧: A(Figur) ≈ (Punkte in der Figur : alle Punkte) · A(Quadrat).',
     'schritte': ['Quadrat 10 cm × 10 cm = 100 cm². Darin ein Viertelkreis mit r = 10 cm. Im Bild sind 40 Zufallspunkte.', '31 der 40 Punkte liegen im Viertelkreis: Anteil 31 : 40 = 0,775.',
                  'A(Viertelkreis) ≈ 0,775 · 100 cm² = ⟦77,5 cm²⟧.'],
     'probe': 'Genau gerechnet: π · 10² : 4 ≈ 78,5 cm². Die Schätzung liegt nah dran – mit mehr Punkten meist noch näher.',
     'bild': {'typ': 'figur', 'punkte': {'_A': [0, 0], '_B': [10, 0], '_C': [10, 10], '_D': [0, 10], '_k0': [10.0, 0.0], '_k1': [9.85, 1.74], '_k2': [9.4, 3.42], '_k3': [8.66, 5.0], '_k4': [7.66, 6.43], '_k5': [6.43, 7.66], '_k6': [5.0, 8.66], '_k7': [3.42, 9.4], '_k8': [1.74, 9.85], '_k9': [0.0, 10.0]}, 'flaeche': ['_A', '_k0', '_k1', '_k2', '_k3', '_k4', '_k5', '_k6', '_k7', '_k8', '_k9'], 'linien': [['_A', '_B', '10 cm'], ['_B', '_C', '10 cm'], ['_C', '_D'], ['_D', '_A']], 'kreise': [{'m': [9.4, 0.4], 'r': 0.13}, {'m': [7.2, 1.8], 'r': 0.13}, {'m': [9.6, 0.5], 'r': 0.13}, {'m': [8.6, 6.7], 'r': 0.13}, {'m': [8.4, 9.7], 'r': 0.13}, {'m': [2.6, 3.5], 'r': 0.13}, {'m': [7.0, 2.9], 'r': 0.13}, {'m': [2.8, 2.4], 'r': 0.13}, {'m': [8.4, 8.5], 'r': 0.13}, {'m': [7.8, 2.4], 'r': 0.13}, {'m': [9.0, 5.1], 'r': 0.13}, {'m': [2.5, 4.6], 'r': 0.13}, {'m': [4.2, 1.0], 'r': 0.13}, {'m': [5.6, 3.7], 'r': 0.13}, {'m': [5.7, 9.0], 'r': 0.13}, {'m': [6.4, 4.1], 'r': 0.13}, {'m': [8.4, 9.7], 'r': 0.13}, {'m': [4.9, 9.2], 'r': 0.13}, {'m': [0.5, 1.6], 'r': 0.13}, {'m': [1.9, 9.1], 'r': 0.13}, {'m': [6.8, 7.1], 'r': 0.13}, {'m': [3.0, 5.0], 'r': 0.13}, {'m': [8.6, 1.2], 'r': 0.13}, {'m': [1.4, 0.7], 'r': 0.13}, {'m': [4.7, 8.2], 'r': 0.13}, {'m': [5.5, 4.1], 'r': 0.13}, {'m': [5.0, 2.0], 'r': 0.13}, {'m': [9.2, 3.6], 'r': 0.13}, {'m': [2.5, 3.2], 'r': 0.13}, {'m': [8.1, 3.3], 'r': 0.13}, {'m': [8.8, 3.5], 'r': 0.13}, {'m': [4.5, 1.0], 'r': 0.13}, {'m': [8.8, 7.8], 'r': 0.13}, {'m': [4.8, 1.4], 'r': 0.13}, {'m': [4.9, 3.8], 'r': 0.13}, {'m': [8.2, 9.0], 'r': 0.13}, {'m': [7.3, 3.0], 'r': 0.13}, {'m': [0.7, 8.7], 'r': 0.13}, {'m': [9.2, 1.8], 'r': 0.13}, {'m': [5.0, 4.8], 'r': 0.13}]},
     'fehler': 'A ≈ 152 cm² ist falsch: Die Anzahl der Punkte ist keine Fläche. Man braucht den ⟦Anteil⟧ der Punkte mal die Quadratfläche.',
     '_verbot': ['152 Punkte']},
    {'lernziel': 'beurteilen', 'titel': 'Ist die Simulation geeignet?',
     'regel': 'Eine Simulation ist ⟦geeignet⟧, wenn das Zufallsgerät für jeden Teilvorgang ⟦genau die richtige Wahrscheinlichkeit⟧ hat und die Durchgänge wie in der Wirklichkeit ablaufen.',
     'schritte': ['Ein Elfmeterschütze trifft mit 75 %.', 'Simulation mit einem Würfel: 1–4 = Treffer → p = 4/6 ≈ 67 %', '⟦Nicht geeignet⟧ – richtig wäre z. B. ein Glücksrad mit 270°-Trefferfeld.'],
     'fehler': 'Eine Urne ohne Zurücklegen verändert sich bei jedem Zug. Soll jeder Versuch dieselbe Wahrscheinlichkeit haben, muss man ⟦zurücklegen⟧.'},
]


# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'zufallsgeraet': {
  'einstieg': 'Tim trifft beim Basketball-Freiwurf in 3 von 10 Fällen. Um zu sehen, wie ein Spiel mit 20 Würfen ausgehen könnte, muss er nicht in die Halle. Er lässt ein Zufallsgerät für sich „werfen“, das genauso oft trifft. Das nennt man ⟦simulieren⟧.',
  'woerter': [['simulieren', 'einen echten Vorgang mit einem Zufallsgerät nachspielen'], ['Zufallsgerät', 'Münze, Würfel, Urne, Glücksrad oder Zufallsziffern'],
              ['p', 'die Wahrscheinlichkeit für einen Treffer, z. B. p = 0,3'], ['mit Zurücklegen', 'die gezogene Kugel kommt wieder in die Urne']],
  'schritte': ['Tim trifft mit der Wahrscheinlichkeit p = 0,3.', 'Eine Urne mit 10 Kugeln passt: 3 rote bedeuten Treffer, 7 weiße bedeuten kein Treffer.',
               'Nach jedem Zug kommt die Kugel zurück, damit beim nächsten Wurf wieder p = 0,3 gilt. Ein Zug ⟦mit Zurücklegen⟧ simuliert also einen Wurf.'],
  'regel': 'So wählst du ein ⟦Zufallsgerät⟧: Es muss ⟦dieselbe Wahrscheinlichkeit⟧ haben wie der echte Vorgang. Münze: 1/2, Würfel: 1/6, Urne oder Glücksrad: beliebige Anteile.'},
 'regel': {
  'einstieg': 'Bevor Tim simuliert, legt er fest, was als Treffer zählt. Bei p = 0,35 reichen die Ziffern 0 bis 9 nicht, denn 3,5 Ziffern gibt es nicht. Mit zweistelligen Zahlen von 00 bis 99 klappt es. Diese Festlegung heißt ⟦Simulationsregel⟧.',
  'woerter': [['Simulationsregel', 'die Festlegung, welche Zahlen als Treffer zählen'], ['00–99', 'alle zweistelligen Zahlen von 00 bis 99, zusammen 100 Stück'],
              ['00–34', 'die Zahlen von 00 bis einschließlich 34, das sind 35 Stück']],
  'schritte': ['Gesucht ist eine Regel für p = 0,35 = 35/100.', 'Man nimmt zweistellige Zufallszahlen von 00 bis 99. Das sind 100 gleich wahrscheinliche Zahlen.',
               '35 davon sollen Treffer sein. Also gilt die Regel: ⟦00–34 = Treffer⟧, 35–99 = kein Treffer.'],
  'regel': 'So legst du die ⟦Regel⟧ fest: p als Bruch mit Nenner 10 oder 100 schreiben. Bei p = 0,4 zählen ⟦4 von 10⟧ Ziffern, bei p = 0,35 zählen 35 der ⟦Zahlen 00 bis 99⟧. Zähle zur Kontrolle nach, wie viele es sind.'},
 'zufallsziffern': {
  'einstieg': 'Statt eine Urne zu benutzen, kann Tim eine Liste mit Zufallsziffern nehmen, zum Beispiel vom Taschenrechner. Jede Ziffer von 0 bis 9 kommt dort gleich oft vor. Mit einer Regel wird aus jeder Ziffer ein Treffer oder kein Treffer. Das heißt: ⟦mit Zufallsziffern simulieren⟧.',
  'woerter': [['Zufallsziffern', 'eine Folge von Ziffern 0–9, die zufällig entsteht; jede hat die Chance 1/10'], ['0–2', 'die Ziffern 0, 1 und 2 – drei Stück']],
  'schritte': ['Die Regel lautet: 0, 1, 2 = Treffer. Das sind 3 von 10 Ziffern, also p = 0,3.', 'Die Liste lautet: 7 1 4 0 9 2 5 8 3 6.',
               'Treffer sind die 1, die 0 und die 2. Das sind ⟦3 Treffer⟧ in 10 Versuchen.'],
  'regel': 'So simulierst du mit ⟦Zufallsziffern⟧: Regel festlegen, welche Ziffern ⟦Treffer⟧ sind. Dann die Liste Ziffer für Ziffer durchgehen und die Treffer zählen.'},
 'auswerten': {
  'einstieg': 'Tim hat 200-mal simuliert, ob in einem Spiel mindestens zwei Sechsen fallen. 46-mal war es so. Daraus kann er abschätzen, wie wahrscheinlich das ist. Die Simulation wird ⟦ausgewertet⟧.',
  'woerter': [['Durchgang', 'eine vollständige Wiederholung der Simulation'], ['Schätzwert', 'ein ungefährer Wert, kein genauer'], ['≈', 'ungefähr gleich']],
  'schritte': ['In 200 Durchgängen kam 46-mal „mindestens zwei Sechsen“ vor.', 'Die relative Häufigkeit ist 46 : 200 = 0,23.',
               'Sie ist ein Schätzwert für die Wahrscheinlichkeit: ⟦P ≈ 0,23⟧.'],
  'regel': 'So wertest du aus: ⟦Anzahl der Treffer : Anzahl der Durchgänge⟧ rechnen. Das Ergebnis ist ein ⟦Schätzwert⟧ für die Wahrscheinlichkeit. Mehr Durchgänge machen ihn zuverlässiger.'},
 'monte_carlo': {
  'einstieg': 'Auf ein quadratisches Blatt mit einem Kreisbogen fallen Regentropfen ganz zufällig. Fallen drei Viertel der Tropfen in die Kreisfigur, bedeckt sie etwa drei Viertel des Blatts. So kann man eine Fläche mit Zufallspunkten schätzen. Das ist die ⟦Monte-Carlo-Methode⟧.',
  'woerter': [['Monte-Carlo-Methode', 'Flächen mit vielen zufälligen Punkten schätzen; benannt nach einem Ort mit Spielkasino'], ['Zufallspunkt', 'ein Punkt an einer zufälligen Stelle im Quadrat'],
              ['Viertelkreis', 'ein Viertel eines Kreises']],
  'schritte': ['Das Quadrat ist 10 cm × 10 cm groß, also 100 cm². Darin liegt ein Viertelkreis mit r = 10 cm. Im Bild sind 40 Zufallspunkte.',
               '31 der 40 Punkte liegen im Viertelkreis. Der Anteil ist 31 : 40 = 0,775.', 'Die Fläche hat etwa denselben Anteil am Quadrat: A ≈ 0,775 · 100 cm² = ⟦77,5 cm²⟧.']},
 'beurteilen': {
  'einstieg': 'Ein Elfmeterschütze trifft in 3 von 4 Fällen. Jemand simuliert das mit einem Würfel: 1 bis 4 heißt Treffer. Passt das? Man prüft, ob das Zufallsgerät dieselbe Wahrscheinlichkeit hat. Dann ist die Simulation ⟦geeignet⟧.',
  'woerter': [['geeignet', 'die Simulation spielt den echten Vorgang richtig nach'], ['75 %', '75 von 100, also 3/4'], ['Trefferfeld', 'das Feld auf dem Glücksrad, das als Treffer zählt']],
  'schritte': ['Der Schütze trifft mit 75 % = 3/4.', 'Beim Würfel zählen 1 bis 4 als Treffer: 4 von 6, also p = 4/6 ≈ 67 %.',
               '67 % ist nicht 75 %. Die Simulation ist ⟦nicht geeignet⟧. Ein Glücksrad mit einem 270°-Trefferfeld würde passen, denn 270° von 360° sind 3/4.'],
  'regel': 'So prüfst du eine Simulation: Hat das Zufallsgerät für jeden Teilvorgang ⟦genau die richtige Wahrscheinlichkeit⟧? Und läuft jeder Durchgang ab wie in Wirklichkeit? Nur dann ist sie ⟦geeignet⟧.'},
}

for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))
# ---- KLAR ENDE ----


def p_text(p):
    return zt(p) if ist_endlich(p) else bruch(p)


GERAETE = [
    (Fr(1, 2), 'eine Münze (Wappen = Treffer)'), (Fr(1, 6), 'ein Würfel (Sechs = Treffer)'), (Fr(1, 3), 'ein Würfel (1 oder 2 = Treffer)'),
    (Fr(1, 4), 'ein Glücksrad mit einem 90°-Trefferfeld'), (Fr(3, 10), 'eine Urne mit 3 roten von 10 Kugeln (mit Zurücklegen)'),
    (Fr(2, 5), 'eine Urne mit 2 roten von 5 Kugeln (mit Zurücklegen)'), (Fr(3, 4), 'ein Glücksrad mit einem 270°-Trefferfeld'),
    (Fr(1, 10), 'eine Zufallsziffer (0 = Treffer)'), (Fr(2, 3), 'ein Würfel (1 bis 4 = Treffer)'), (Fr(5, 6), 'ein Würfel (1 bis 5 = Treffer)'),
    (Fr(7, 10), 'eine Urne mit 7 roten von 10 Kugeln (mit Zurücklegen)'), (Fr(1, 5), 'ein Glücksrad mit einem 72°-Trefferfeld'),
]
SACHE = ['Ein Basketballspieler trifft beim Freiwurf', 'Ein Samen keimt', 'Eine Ampel zeigt bei Ankunft Grün', 'Ein Kind gewinnt beim Losstand',
         'Ein Bus hat Verspätung', 'Ein Bauteil ist fehlerhaft', 'Eine Schülerin löst eine Rätselaufgabe']


def g_zufallsgeraet(R, st):
    if st == 1 or (st == 2 and R.random() < .5):
        p, g = R.choice(GERAETE)
        andere = [gg for pp, gg in GERAETE if pp != p]
        return A(R, f'{R.choice(SACHE)} mit der Wahrscheinlichkeit {p_text(p)}. Welches Zufallsgerät simuliert das richtig?', g[0].upper() + g[1:],
                 [x[0].upper() + x[1:] for x in R.sample(andere, 3)], f'{g[0].upper() + g[1:]} hat die Trefferwahrscheinlichkeit {p_text(p)}.',
                 'Berechne für jedes Gerät die Trefferwahrscheinlichkeit.')
    if st == 2:
        p = Fr(R.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 55, 60, 65, 70, 75, 80, 85, 90]), 100)
        n = R.choice([20, 40, 60, 100])
        if (p * n).denominator != 1: return g_zufallsgeraet(R, st)
        return Z(f'Mit einer Urne aus {n} Kugeln soll ein Treffer mit p = {zt(p)} simuliert werden. Wie viele rote (Treffer-)Kugeln braucht man?', p * n,
                 f'{n} * {cz(p)}', f'{zt(p)} · {n} = {zt(p * n)} rote Kugeln.', 'Anteil der roten Kugeln = Wahrscheinlichkeit.')
    p = Fr(R.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 55, 60, 65, 70, 75, 80, 85]), 100)
    return Z(f'Ein Glücksrad soll einen Treffer mit p = {zt(p)} simulieren. Wie groß muss der Mittelpunktswinkel des Trefferfeldes sein (in Grad)?', p * 360,
             f'{cz(p)} * 360', f'{zt(p)} · 360° = {zt(p * 360)}°.', 'Der Anteil am Vollwinkel 360° ist die Wahrscheinlichkeit.', '°')


def ziffern(R, n, gruppe=4):
    z = [str(R.randint(0, 9)) for _ in range(n)]
    return z, ' '.join(''.join(z[i:i + gruppe]) for i in range(0, n, gruppe))


def ziff_regel(k):
    if k == 1: return 'Nur die Ziffer 0 ist Treffer'
    if k == 2: return 'Die Ziffern 0 und 1 sind Treffer'
    return f'Die Ziffern 0 bis {k - 1} sind Treffer'


def g_zufallsziffern(R, st):
    if st == 1:
        k = R.choice([2, 3, 4, 5, 6])
        z, txt = ziffern(R, 20)
        treffer = sum(1 for x in z if int(x) < k)
        return Z(f'Regel: {ziff_regel(k)} (p = {zt(Fr(k, 10))}). Zähle die Treffer in den 20 Zufallsziffern {txt}.', treffer,
                 f'{treffer}', f'Treffer-Ziffern 0–{k - 1}: ' + ', '.join(x for x in z if int(x) < k) + f'. Das sind {treffer}.', 'Gehe die Ziffern einzeln durch.')
    if st == 2:
        k = R.choice([2, 3, 4, 5, 6, 7])
        z, txt = ziffern(R, 32)
        treffer = sum(1 for x in z if int(x) < k)
        if R.random() < .6:
            return Z(f'Regel: {ziff_regel(k)}. Zufallsziffern (32 Stück): {txt}. Gib die relative Häufigkeit der Treffer als Dezimalzahl an.', Fr(treffer, 32),
                     f'{treffer} / 32', f'{treffer} Treffer bei 32 Versuchen: {treffer} : 32 = {zt(Fr(treffer, 32))}.', 'Treffer zählen und durch die Anzahl der Ziffern teilen.')
        return Z(f'Regel: {ziff_regel(k)}. Zufallsziffern (32 Stück): {txt}. Wie viele Nicht-Treffer gibt es?', 32 - treffer,
                 f'32 - {treffer}', f'{treffer} Treffer, also 32 − {treffer} = {32 - treffer} Nicht-Treffer.', 'Zähle die Treffer und ziehe sie von 32 ab.')
    # Stufe 3: Gruppen als ein Durchgang
    k, g = R.choice([(3, 3), (5, 2), (2, 4), (4, 3), (1, 4)])
    z, _ = ziffern(R, g * 8)
    gruppen = [z[i:i + g] for i in range(0, len(z), g)]
    txt = ' '.join(''.join(x) for x in gruppen)
    erf = sum(1 for gr in gruppen if any(int(x) < k for x in gr))
    return Z(f'Jede {g}er-Gruppe ist ein Durchgang mit {g} Versuchen; {ziff_regel(k)[0].lower() + ziff_regel(k)[1:]}. In wie vielen Durchgängen gab es mindestens einen Treffer? Gruppen: {txt}',
             erf, f'{erf}', f'Gruppen mit mindestens einer Treffer-Ziffer ({"0" if k == 1 else "0–" + str(k - 1)}): ' + ', '.join(''.join(gr) for gr in gruppen if any(int(x) < k for x in gr)) + f'. Das sind {erf}.',
             'Prüfe jede Gruppe: Ist mindestens eine Treffer-Ziffer dabei?')


def g_regel(R, st):
    if st == 1:
        p = Fr(R.randint(1, 9), 10)
        return Z(f'Mit Zufallsziffern 0–9 soll p = {zt(p)} simuliert werden. Wie viele der zehn Ziffern müssen als Treffer zählen?', p * 10, f'{cz(p)} * 10',
                 f'Jede Ziffer hat p = 0,1. {zt(p)} : 0,1 = {zt(p * 10)} Ziffern.', 'Jede Ziffer hat die Wahrscheinlichkeit 1/10.')
    if st == 2:
        p = Fr(R.choice([k for k in range(5, 96) if k % 10]), 100)
        r = f'00 bis {p.numerator * (100 // p.denominator) - 1:02d}'
        n = int(p * 100)
        return A(R, f'Mit zweistelligen Zufallszahlen 00–99 soll p = {zt(p)} simuliert werden. Welche Regel ist richtig?', f'{r} = Treffer',
                 [f'00 bis {n:02d} = Treffer', f'01 bis {n - 1:02d} = Treffer', f'00 bis {n // 10} = Treffer'],
                 f'Es gibt 100 Zahlen. {zt(p)} · 100 = {n} Treffer-Zahlen: 00, 01, …, {n - 1:02d}.', 'Zähle genau: Von 00 bis 09 sind es 10 Zahlen.')
    art = R.choice(['wuerfel', 'nenner', 'zwei'])
    if art == 'zwei':
        p1, p2 = R.sample([Fr(k, 10) for k in range(1, 10)], 2)
        a1, a2 = int(p1 * 10), int(p2 * 10)
        rg = lambda a: '0' if a == 1 else f'0–{a - 1}'
        return A(R, f'Ein Spieler trifft beim ersten Wurf mit p = {zt(p1)}, beim zweiten mit p = {zt(p2)}. Welche Regel für eine Zweiergruppe von Zufallsziffern passt?',
                 f'1. Ziffer {rg(a1)} = Treffer, 2. Ziffer {rg(a2)} = Treffer',
                 [f'beide Ziffern {rg(a1)} = Treffer', f'1. Ziffer 0–{a1} = Treffer, 2. Ziffer 0–{a2} = Treffer', f'1. Ziffer {rg(a2)} = Treffer, 2. Ziffer {rg(a1)} = Treffer'],
                 f'Jede Ziffer steht für einen Wurf. Erster Wurf: {a1} von 10 Ziffern ({rg(a1)}), zweiter Wurf: {a2} von 10 Ziffern ({rg(a2)}).',
                 'Jeder Wurf bekommt seine eigene Regel.')
    if art == 'wuerfel':
        k = R.randint(1, 5)
        ereig = 'Augenzahl 1' if k == 1 else f'Augenzahl ≤ {k}'
        tr = '1' if k == 1 else f'1–{k}'
        return A(R, f'Mit Zufallsziffern soll ein Würfelwurf mit „{ereig}“ als Treffer simuliert werden. Welche Regel passt?',
                 f'Ziffern 1–6 verwenden, 0, 7, 8, 9 überspringen; {tr} = Treffer',
                 [f'Ziffern 0–{k} = Treffer, alle anderen kein Treffer', f'Ziffern {tr} = Treffer, 0 und 7–9 kein Treffer', 'Jede Ziffer zählt als eine Augenzahl'],
                 f'Für einen Würfel braucht man 6 gleich wahrscheinliche Ergebnisse. Die Ziffern 1–6 liefern das, wenn man die übrigen überspringt. p = {k}/6.',
                 'Ein Würfel hat 6 gleich wahrscheinliche Ergebnisse – wie bekommt man die mit Ziffern?')
    p = Fr(R.choice([1, 2]), 3)
    return A(R, f'Mit Zufallsziffern soll p = {bruch(p)} simuliert werden. Welche Regel passt?', f'Ziffern 1–9 verwenden, 0 überspringen; 1–{int(p * 9)} = Treffer',
             [f'Ziffern 0–{int(p * 10) - 1} = Treffer', f'Ziffern 0–{int(p * 10)} = Treffer', f'Ziffern 1–{int(p * 10)} = Treffer, 0 und Rest kein Treffer'],
             f'{bruch(p)} = {int(p * 9)}/9: Mit 9 gleich wahrscheinlichen Ziffern (1–9) geht es genau, mit 10 Ziffern nicht.',
             f'Welche Anzahl gleich wahrscheinlicher Ziffern ist durch {p.denominator} teilbar?')


EREIG = [('„mindestens eine Sechs bei vier Würfen“', Fr(671, 1296), '1 − (5/6)⁴ ≈ 0,518'), ('„alle drei Kinder sind Mädchen“', Fr(1, 8), '(1/2)³ = 0,125'),
         ('„genau zwei Wappen bei drei Münzwürfen“', Fr(3, 8), '3/8 = 0,375'), ('„der Bus kommt pünktlich“', Fr(4, 5), None), ('„Gewinn beim Losen“', Fr(3, 20), None)]


def realistisch(R, n, p):
    sd = (float(n * p * (1 - p))) ** .5
    lo, hi = max(1, int(float(n * p) - 2 * sd)), min(n - 1, int(float(n * p) + 2 * sd))
    return R.randint(lo, hi)


def g_auswerten(R, st):
    n = R.choice([50, 80, 100, 125, 200, 250, 400, 500, 1000])
    was, pw, pt = R.choice(EREIG)
    k = realistisch(R, n, pw)
    if st == 3 and R.random() < .5 and pt:
        rel = Fr(k, n)
        return A(R, f'Eine Simulation von {was} ergab {k} Treffer bei {n} Durchgängen. Berechnet ist P = {pt}. Was folgt?',
                 f'Die Simulation passt gut ({zt(rel) if ist_endlich(rel) and len(zt(rel)) <= 6 else "≈ " + zt(round(float(rel), 3))}).',
                 ['Die Rechnung muss falsch sein.', 'Simulationen sind wertlos.', 'Die Simulation hätte genau den berechneten Wert ergeben müssen.'],
                 f'Relative Häufigkeit {k} : {n} liegt nahe beim berechneten Wert. Kleine Abweichungen sind bei Simulationen normal.',
                 'Vergleiche die relative Häufigkeit mit dem berechneten Wert.')
    if st == 1:
        return Z(f'Eine Simulation mit {n} Durchgängen ergab {k}-mal das Ereignis {was}. Schätze die Wahrscheinlichkeit (als Dezimalzahl).', Fr(k, n), f'{k} / {n}',
                 f'P ≈ {k} : {n} = {zt(Fr(k, n))}.', 'Relative Häufigkeit = Treffer : Durchgänge.')
    if st == 2:
        m = R.choice([1000, 2000, 5000, 10000])
        return Z(f'Eine Simulation mit {n} Durchgängen ergab {k}-mal {was}. Wie oft ist das Ereignis bei {zt(m)} echten Durchgängen etwa zu erwarten?', Fr(k, n) * m,
                 f'{k} / {n} * {m}', f'P ≈ {zt(Fr(k, n))}. Erwartet: {zt(Fr(k, n))} · {zt(m)} = {zt(Fr(k, n) * m)}.', 'Erst die Wahrscheinlichkeit schätzen, dann mal die Anzahl.')
    n1, n2 = R.sample([20, 50, 100, 500, 1000, 2000], 2)
    gross = max(n1, n2)
    return A(R, f'Gruppe A simuliert {n1} Durchgänge, Gruppe B {n2}. Wessen Schätzwert für die Wahrscheinlichkeit ist vermutlich zuverlässiger?',
             f'Der von Gruppe {"A" if gross == n1 else "B"}, weil sie mehr Durchgänge hat.',
             [f'Der von Gruppe {"B" if gross == n1 else "A"}, weil sie weniger Durchgänge hat.', 'Beide gleich, Zufall bleibt Zufall.', 'Das hängt nur vom Zufallsgerät ab, nicht von der Anzahl.'],
             'Nach dem Gesetz der großen Zahlen schwankt die relative Häufigkeit bei vielen Durchgängen weniger.', 'Denke an das Gesetz der großen Zahlen.')


def g_monte_carlo(R, st):
    a = R.choice([2, 4, 5, 10, 20])
    n = R.choice([100, 200, 250, 400, 500, 1000])
    k = R.randint(n // 10, n - n // 10)
    if st == 1:
        return Z(f'In ein Quadrat werden {n} Zufallspunkte gesetzt, {k} liegen in einer Figur. Welcher Anteil der Punkte ist das? (als Dezimalzahl)', Fr(k, n), f'{k} / {n}',
                 f'{k} : {n} = {zt(Fr(k, n))}.', 'Punkte in der Figur durch alle Punkte.')
    if st == 2:
        return Z(f'Ein Quadrat hat die Seitenlänge {a} cm. Von {n} Zufallspunkten liegen {k} in einer Figur im Quadrat. Schätze den Flächeninhalt der Figur.', Fr(k, n) * a * a,
                 f'{k} / {n} * {a} ** 2', f'Anteil {zt(Fr(k, n))}, Quadrat {a * a} cm². A ≈ {zt(Fr(k, n))} · {a * a} = {zt(Fr(k, n) * a * a)} cm².',
                 'Anteil der Punkte mal Fläche des Quadrats.', 'cm²')
    # π schätzen: Viertelkreis im Einheitsquadrat
    k = R.randint(int(n * 0.74), int(n * 0.83))
    bild = {k_: v for k_, v in ETAPPEN[4]['bild'].items()}
    bild = json.loads(json.dumps(bild)); bild['linien'] = [[a, b] for a, b, *_ in bild['linien']]
    return mit_bild(Z(f'In ein Quadrat mit Seitenlänge 1 wird ein Viertelkreis mit Radius 1 gezeichnet (Bild: Ausschnitt mit 40 Punkten). Von {n} Zufallspunkten liegen {k} im Viertelkreis. Welchen Schätzwert für π erhält man?',
                      4 * Fr(k, n), f'4 * {k} / {n}', f'Viertelkreis A = π/4, Quadrat A = 1. Also π/4 ≈ {k}/{n} → π ≈ 4 · {zt(Fr(k, n))} = {zt(4 * Fr(k, n))}.',
                      'Der Viertelkreis hat die Fläche π/4. Setze den Punkteanteil gleich π/4.'), bild)


def dat(g):
    """Zufallsgerät im Dativ: „mit einer Münze“, „mit einem Würfel“."""
    if g.startswith('eine '): return 'einer ' + g[5:]
    if g.startswith('ein '): return 'einem ' + g[4:]
    return g


def g_beurteilen(R, st):
    sache = R.choice(SACHE)
    p, g = R.choice(GERAETE)
    if st == 3 and R.random() < .5:
        r = 'Nicht geeignet: Ohne Zurücklegen ändert sich die Wahrscheinlichkeit bei jedem Zug.'
        n = R.choice([5, 10]); k = int(p * n) if (p * n).denominator == 1 else 3
        return A(R, f'{sache} jedes Mal mit p = {zt(Fr(k, n))}. Simuliert werden 4 Versuche: Aus einer Urne mit {k} roten von {n} Kugeln wird 4-mal OHNE Zurücklegen gezogen. Ist das geeignet?',
                 r, ['Geeignet, weil der Anteil der roten Kugeln stimmt.', 'Geeignet, weil man mit einer Urne alles simulieren kann.', 'Nicht geeignet, weil eine Urne nie für Simulationen taugt.'],
                 'Nach jedem Zug fehlt eine Kugel, der Anteil der roten ändert sich. Mit Zurücklegen wäre es richtig.', 'Bleibt die Wahrscheinlichkeit bei jedem Zug gleich?')
    echt = p if R.random() < .4 else R.choice([pp for pp, _ in GERAETE if pp != p])
    ok = echt == p
    r = 'Ja, das Gerät hat genau die richtige Wahrscheinlichkeit.' if ok else f'Nein, das Gerät hat p = {p_text(p)}, gebraucht wird {p_text(echt)}.'
    f = (['Nein, Simulationen sind nie genau.', f'Nein, man braucht dafür immer eine Münze.', f'Nein, das Gerät hat p = {p_text(1 - p) if 1 - p != p else "1/3"}.'] if ok else
         ['Ja, das Gerät hat genau die richtige Wahrscheinlichkeit.', 'Ja, jedes Zufallsgerät ist geeignet.', f'Nein, das Gerät hat p = {p_text(echt)}, gebraucht wird {p_text(p)}.'])
    return A(R, f'{sache} mit p = {p_text(echt)}. Simuliert wird mit {dat(g)}. Ist das geeignet?', r, f,
             f'Das Gerät liefert p = {p_text(p)}, benötigt wird p = {p_text(echt)}.' + (' Das passt.' if ok else ' Das passt nicht.'),
             'Berechne die Trefferwahrscheinlichkeit des Geräts und vergleiche.')


GEN = {'zufallsgeraet': g_zufallsgeraet, 'zufallsziffern': g_zufallsziffern, 'regel': g_regel, 'auswerten': g_auswerten, 'monte_carlo': g_monte_carlo, 'beurteilen': g_beurteilen}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Simulieren', ['zufallsgeraet', 'regel', 'zufallsziffern']), ('Auswerten', ['auswerten', 'monte_carlo']), ('Verstehen', ['beurteilen'])],
         'Zufallsexperimente mit Münze, Würfel, Urne, Glücksrad und Zufallsziffern simulieren, auswerten und Flächen mit der Monte-Carlo-Methode schätzen.',
         ['Zufallsgerät muss genau die gesuchte Wahrscheinlichkeit haben.', 'Zufallsziffern: jede Ziffer p = 0,1; zweistellig 00–99: jede Zahl p = 0,01.',
          'Schätzwert = Treffer : Durchgänge. Monte-Carlo: Fläche ≈ Punkteanteil · Quadratfläche.'],
         offen=['Echte Simulationen (Würfeln, Ziehen, Zufallszahlen am Rechner) sind in der App nicht möglich; die Zufallsziffern werden fest vorgegeben. '
                'Eine kleine Simulationsfunktion in der App (Knopf „100-mal würfeln“) würde das Thema stark verbessern.',
                'Lehrplan: lehrplan_gym ist für dieses Thema leer – bitte im Aufbau klären.',
                'Monte-Carlo-Bild: Quadrat mit Viertelkreis und 40 Punkten (Behelf mit kleinen Kreisen); bei den Flächen-Aufgaben ohne bekannte Figur gibt es kein Bild.'])
