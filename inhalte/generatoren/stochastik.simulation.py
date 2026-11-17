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


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl8.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl8 import mit_umbau  # noqa: E402

# Bild der Monte-Carlo-Karte: unverändert aus ETAPPEN (40 Zufallspunkte, 31 im Viertelkreis – nachgezählt).
_ZIFF = ['Ziffer', '7', '1', '4', '0', '9', '2', '5', '8', '3', '6']
UMBAU = {
 'zufallsgeraet': {
  'einstieg': 'Tim trifft beim Basketball-Freiwurf in 3 von 10 Fällen. Statt in die Halle zu gehen, lässt er ein Zufallsgerät mit derselben Trefferchance „werfen“. Das nennt man ⟦simulieren⟧.',
  'woerter': [['simulieren', 'einen echten Vorgang mit einem Zufallsgerät nachspielen'], ['Zufallsgerät', 'Münze, Würfel, Urne oder Glücksrad'], ['mit Zurücklegen', 'die gezogene Kugel kommt zurück in die Urne']],
  'bild': {'typ': 'bruchstreifen', 'teile': 10, 'gefaerbt': 3, 'ganzes': '10 Kugeln', 'teil_text': '3 rote'},
  'schritte': [{'text': 'Tim trifft mit der Wahrscheinlichkeit p = 0,3.'},
               {'text': 'Eine Urne mit 3 roten und 7 weißen Kugeln passt: rot heißt Treffer.'},
               {'text': 'Ziehen ⟦mit Zurücklegen⟧: So bleibt p bei jedem Wurf 0,3.'}],
  'fehler': 'Eine Münze passt nicht: Sie trifft immer mit ⟦p = 0,5⟧. Das Gerät braucht genau die echte Wahrscheinlichkeit.',
  'fehler_bild': {'teile': 2, 'gefaerbt': 1, 'ganzes': 'Münze', 'teil_text': '1/2'},
  'regel': 'Das Zufallsgerät braucht ⟦dieselbe Wahrscheinlichkeit⟧. Münze 1/2, Würfel 1/6, Urne oder Glücksrad: beliebige Anteile.'},
 'regel': {
  'einstieg': 'Bevor Tim simuliert, legt er fest, was als Treffer zählt. Bei p = 0,35 reichen die Ziffern 0 bis 9 nicht. Zweistellige Zahlen helfen; die Festlegung heißt ⟦Simulationsregel⟧.',
  'woerter': [['Simulationsregel', 'die Festlegung, welche Zahlen ein Treffer sind'], ['00 bis 99', 'alle 100 zweistelligen Zufallszahlen']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 100, 'abschnitte': 10, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': 'p = 0,35 = 35/100. Nimm die Zahlen 00 bis 99.'},
               {'text': 'Das sind 100 gleich wahrscheinliche Zahlen. 35 davon sollen Treffer sein.'},
               {'text': 'Regel: ⟦00–34 = Treffer⟧, 35–99 = kein Treffer.', 'bild': {'bereich': {'von': 0, 'bis': 35}, 'punkte': [{'wert': 35, 'name': 'ab 35 kein Treffer'}]}}],
  'fehler': '„00–35 = Treffer“ ist falsch: Von 00 bis 35 sind es ⟦36⟧ Zahlen.',
  'regel': 'Schreibe p mit ⟦Nenner 10 oder 100⟧. Dann so viele Ziffern oder Zahlen als Treffer festlegen und nachzählen.'},
 'zufallsziffern': {
  'einstieg': 'Statt einer Urne nimmt Tim eine Liste mit Zufallsziffern, etwa vom Taschenrechner. Jede Ziffer von 0 bis 9 kommt gleich oft vor. Mit einer Regel wird daraus ein ⟦Treffer⟧ oder keiner.',
  'woerter': [['Zufallsziffern', 'zufällig erzeugte Ziffern von 0 bis 9'], ['Treffer', 'ein Versuch, der zählt – hier ein getroffener Wurf']],
  'bild': {'typ': 'tabelle', 'kopf': _ZIFF, 'zeilen': [['Treffer?'] + ['?'] * 10]},
  'schritte': [{'text': 'Regel: 0, 1, 2 = Treffer. Das sind 3 von 10 Ziffern, p = 0,3.'},
               {'text': 'Die Liste lautet: 7 1 4 0 9 2 5 8 3 6.'},
               {'text': 'Treffer sind 1, 0 und 2: ⟦3 Treffer⟧ in 10 Versuchen.',
                'bild': {'zeilen': [['Treffer?', '–', 'ja', '–', 'ja', '–', 'ja', '–', '–', '–', '–']]}}],
  'fehler': 'Bei „0–2 = Treffer“ zählt die 2 mit. Das sind ⟦drei⟧ Ziffern, also p = 3/10.',
  'regel': 'Lege fest, welche Ziffern ⟦Treffer⟧ sind. Dann die Liste durchgehen und zählen.'},
 'auswerten': {
  'einstieg': 'Tim hat 200-mal simuliert, ob mindestens zwei Sechsen fallen. 46-mal war es so. Jetzt wird die Simulation ⟦ausgewertet⟧.',
  'woerter': [['ausgewertet', 'aus den Ergebnissen eine Aussage gewonnen'], ['Schätzwert', 'ein ungefährer Wert, kein genauer']],
  'bild': {'typ': 'saeulen', 'einheit': 'Durchgänge', 'werte': [{'name': 'ja', 'wert': 46}, {'name': 'nein', 'wert': 154}], 'zahlen': True},
  'schritte': [{'text': 'In 200 Durchgängen kam es 46-mal vor.'},
               {'text': 'Relative Häufigkeit: 46 : 200 = 0,23.', 'bild': {'typ': 'kreisdiagramm', 'einheit': ' %', 'werte': [{'name': 'ja', 'wert': 23}, {'name': 'nein', 'wert': 77}], 'zahlen': True}},
               {'text': 'Das ist ein Schätzwert: ⟦P ≈ 0,23⟧.'}],
  'fehler': '0,23 ist kein genauer Wert, sondern eine ⟦Schätzung⟧. Eine neue Simulation ergibt meist eine etwas andere Zahl.',
  'regel': 'Schätzwert = ⟦Treffer : Durchgänge⟧. Mehr Durchgänge machen ihn zuverlässiger.'},
 'monte_carlo': {
  'einstieg': 'Regentropfen fallen zufällig auf ein quadratisches Blatt mit einem Viertelkreis. Landen drei Viertel im Viertelkreis, bedeckt er etwa drei Viertel des Blatts. Das ist die ⟦Monte-Carlo-Methode⟧.',
  'woerter': [['Monte-Carlo-Methode', 'eine Fläche mit zufälligen Punkten schätzen'], ['Anteil', 'Teil geteilt durch Ganzes']],
  'bild': None,  # wird unten aus dem bisherigen Kartenbild übernommen
  'schritte': [{'text': 'Das Quadrat hat 100 cm², darin liegt ein Viertelkreis.'},
               {'text': '31 von 40 Zufallspunkten liegen im Viertelkreis: Anteil 0,775.'},
               {'text': 'Fläche ≈ 0,775 · 100 cm² = ⟦77,5 cm²⟧.'}],
  'fehler': 'Nicht die Punktzahl als Fläche nehmen: 31 Punkte sind nicht 31 cm². Man braucht den ⟦Anteil⟧ der Punkte mal 100 cm².',
  'regel': 'Anteil der Punkte ≈ ⟦Anteil der Fläche⟧. Mal die Quadratfläche ergibt die Fläche der Figur.'},
 'beurteilen': {
  'einstieg': 'Ein Elfmeterschütze trifft in 3 von 4 Fällen. Jemand simuliert das mit einem Würfel: 1 bis 4 heißt Treffer. Nur bei gleicher Wahrscheinlichkeit ist die Simulation ⟦geeignet⟧.',
  'woerter': [['geeignet', 'passend: gleiche Wahrscheinlichkeit wie in echt'], ['≈', '„ungefähr gleich“']],
  'bild': {'typ': 'kreisdiagramm', 'einheit': ' %', 'werte': [{'name': 'Treffer', 'wert': 75}, {'name': 'kein', 'wert': 25}], 'zahlen': True},
  'schritte': [{'text': 'Der Schütze trifft mit 3/4 = 75 %.'},
               {'text': 'Würfel, 1 bis 4: 4/6 ≈ 67 %.', 'bild': {'werte': [{'name': 'Treffer', 'wert': 67}, {'name': 'kein', 'wert': 33}]}},
               {'text': '67 % ist nicht 75 %: ⟦nicht geeignet⟧.'},
               {'text': 'Ein Glücksrad mit 270°-Trefferfeld passt: 270/360 = 3/4.', 'bild': {'einheit': '°', 'werte': [{'name': 'Treffer', 'wert': 270}, {'name': 'kein', 'wert': 90}]}}],
  'fehler': 'Eine Urne ohne Zurücklegen ändert sich bei jedem Zug. Für gleichbleibende Wahrscheinlichkeit musst du ⟦zurücklegen⟧.',
  'regel': 'Das Zufallsgerät braucht ⟦genau die richtige Wahrscheinlichkeit⟧. Und jeder Durchgang muss ablaufen wie in Wirklichkeit.'},
}
_mc_alt = next(e for e in ETAPPEN if e['lernziel'] == 'monte_carlo').get('bild')
UMBAU['monte_carlo']['bild'] = _mc_alt
UMBAU_OFFEN = ['Umbau 16.11.: Karte zufallsgeraet zeigt die Urne behelfsweise als Bruchstreifen (10 Kugeln, 3 rot). App-Wunsch Urne steht schon auf der Liste.']
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---- SCHWER (Zehnte Runde: schwerere Aufgaben nach Prüfungsvorbild, siehe _schwer_kl8.py) ----
# Vorbilder (Typ und Niveau, nicht Wortlaut/Zahlen): Echte bayerische Prüfungsaufgaben zur Simulation wurden nicht gefunden. Übertragen wurden:
# Materialaufgaben NRW (QUA-LiS, „Aufgabe zur Simulation“: Blatt einer Tabellenkalkulation mit Zufallszahlen deuten), BMT8 2022/2025 (Tabellenkalkulations-Formeln),
# VERA-8 2026 (Glücksrad: Prognose vs. Auswertung, „Würfelgedächtnis“; See-Fläche aus Karte schätzen), Kreisberechnung Kl. 8 (Monte-Carlo mit Kreis).
from _schwer_kl8 import Neu, mit_schwer  # noqa: E402

SW = Neu(10_8_14)


def _zif(s):
    return [int(c) for c in s if c.isdigit()]


def _gruppen(s):
    return [[int(c) for c in g] for g in s.split()]


# zufallsgeraet
SW.a('zufallsgeraet', 2, 'Ein Ereignis tritt mit der Wahrscheinlichkeit 3/8 ein. Welches Zufallsgerät simuliert das richtig?', 'Ein Glücksrad mit 8 gleichen Feldern, 3 davon Treffer',
     ['Ein Würfel (1 bis 3 = Treffer)', 'Eine Münze (Wappen = Treffer)', 'Eine Zufallsziffer (0 bis 2 = Treffer)'],
     '3 von 8 gleich großen Feldern: p = 3/8. Der Würfel gibt 3/6 = 1/2, die Münze 1/2, die Ziffern 0–2 geben 3/10.', 'Welches Gerät hat genau 8 gleich wahrscheinliche Ausgänge?')
SW.a('zufallsgeraet', 2, 'Mit einem Würfel soll ein Ereignis mit p = 1/2 simuliert werden. Welche Regel passt?', 'gerade Augenzahl = Treffer', ['Sechs = Treffer', 'Augenzahl 1 oder 2 = Treffer',
     'Augenzahl größer als 4 = Treffer'], 'Gerade Zahlen: 2, 4, 6 – drei von sechs, also 1/2. „Größer als 4“ wären nur 5 und 6 (1/3).', 'Wie viele der sechs Zahlen brauchst du als Treffer?')
SW.a('zufallsgeraet', 3, 'In einer Tabellenkalkulation liefert =ZUFALLSBEREICH(1;6) eine zufällige ganze Zahl von 1 bis 6. Welche Formel simuliert einen Münzwurf (1 = Wappen, 2 = Zahl)?', '=ZUFALLSBEREICH(1;2)',
     ['=ZUFALLSBEREICH(1;6)/2', '=ZUFALLSBEREICH(2;2)', '=ZUFALLSBEREICH(1;3)'],
     'ZUFALLSBEREICH(1;2) liefert 1 oder 2, jeweils mit p = 1/2. Geteilt durch 2 ergäben sich auch Kommazahlen, (2;2) liefert immer 2, (1;3) drei Ausgänge.', 'Welche Formel hat genau zwei gleich wahrscheinliche Ergebnisse?', art='P')
SW.a('zufallsgeraet', 3, '=ZUFALLSBEREICH(1;10) liefert ganze Zahlen von 1 bis 10. Ein Treffer soll die Wahrscheinlichkeit 0,3 haben. Welche Bedingung passt?', 'Zahl ≤ 3', ['Zahl ≥ 3', 'Zahl < 3', 'Zahl = 3'],
     '≤ 3 sind 1, 2, 3 – drei von zehn: 0,3. „≥ 3“ wären 8 Zahlen, „< 3“ nur 2, „= 3“ nur 1.', 'Wie viele der zehn Zahlen müssen Treffer sein?', art='P')
SW.a('zufallsgeraet', 3, 'Eine Tennisspielerin gewinnt einen Punkt mit p = 0,55. Womit lässt sich das am einfachsten simulieren?', 'mit Zufallszahlen 00 bis 99, dabei 00 bis 54 = Treffer',
     ['mit einem Würfel, 1 bis 3 = Treffer', 'mit einer Münze, Wappen = Treffer', 'mit Zufallsziffern 0 bis 9, dabei 0 bis 5 = Treffer'],
     '0,55 = 55/100: Man braucht 100 gleich wahrscheinliche Ausgänge, davon 55 Treffer (00 bis 54). Würfel und Münze geben 0,5, Ziffern 0–5 geben 0,6.', 'Schreibe 0,55 als Bruch mit Nenner 100.', art='K')
SW.a('zufallsgeraet', 3, 'Kann man mit einer fairen Münze ein Ereignis mit p = 1/4 simulieren?', 'Ja: zweimal werfen, Treffer nur bei „zweimal Wappen“.', ['Nein, eine Münze hat nur p = 1/2.',
     'Ja: viermal werfen, Treffer bei einmal Wappen.', 'Nein, dafür braucht man ein Glücksrad.'],
     'Zwei Würfe haben 4 gleich wahrscheinliche Ergebnisse (WW, WZ, ZW, ZZ). Nur WW ist Treffer: 1/4.', 'Wie viele gleich wahrscheinliche Ergebnisse haben zwei Münzwürfe?', art='K')

# regel
SW.a('regel', 2, 'Mit Zufallsziffern 0 bis 9 soll p = 0,7 simuliert werden. Welche Regel ist richtig?', 'Ziffern 0 bis 6 = Treffer', ['Ziffern 0 bis 7 = Treffer', 'Ziffern 1 bis 6 = Treffer',
     'Ziffer 7 = Treffer'], '0 bis 6 sind 7 Ziffern von 10: p = 0,7. „0 bis 7“ wären 8 Ziffern.', 'Zähle die Ziffern – die 0 zählt mit.')
SW.z('regel', 2, 'Mit zweistelligen Zufallszahlen 00 bis 99 soll p = 0,08 simuliert werden. Wie viele der 100 Zahlen müssen Treffer sein?', 8, '0.08 * 100', '0,08 = 8/100: 8 Zahlen, z. B. 00 bis 07.',
     'Schreibe p als Bruch mit Nenner 100.')
SW.a('regel', 3, 'Mit dreistelligen Zufallszahlen 000 bis 999 soll p = 0,125 simuliert werden. Welche Regel ist richtig?', '000 bis 124 = Treffer', ['000 bis 125 = Treffer', '001 bis 125 = Treffer',
     '000 bis 12 = Treffer'], '0,125 = 125/1000. 000 bis 124 sind genau 125 Zahlen. 000 bis 125 wären 126.', 'Wie viele dreistellige Zahlen gibt es, und wie viele brauchst du?', art='P')
SW.a('regel', 3, 'Ein Spieler trifft mit p = 0,6 und wirft dreimal. Wie stellt man einen Durchgang mit Zufallsziffern dar?', '3 Ziffern, jede Ziffer 0 bis 5 = Treffer',
     ['1 Ziffer, 0 bis 5 = drei Treffer', '3 Ziffern, jede Ziffer 0 bis 6 = Treffer', '6 Ziffern, jede Ziffer 0 bis 2 = Treffer'],
     'Jeder Wurf braucht eine eigene Ziffer. 0 bis 5 sind 6 von 10 Ziffern: p = 0,6. Drei Würfe – drei Ziffern.', 'Wie viele Ziffern braucht ein Durchgang?', art='P')
SW.a('regel', 3, 'Kann man p = 0,35 mit Münzwürfen simulieren?', 'Nein: Mit Münzen erhält man nur Wahrscheinlichkeiten wie 1/2, 1/4, 3/8 …', ['Ja: 35 Münzen werfen.',
     'Ja: zwei Münzen, Treffer bei mindestens einem Wappen.', 'Ja: drei Münzen, Treffer bei genau einem Wappen.'],
     'Bei n Münzwürfen gibt es 2ⁿ gleich wahrscheinliche Ergebnisse – Nenner 2, 4, 8, 16, … 0,35 = 7/20 hat den Nenner 20, das passt nie. (Zwei Münzen, mind. ein Wappen: 3/4; drei Münzen, genau ein Wappen: 3/8.)',
     'Welche Nenner entstehen bei Münzwürfen?', art='K')
SW.a('regel', 3, 'Mit Zufallsziffern soll p = 3/7 simuliert werden. Welche Regel passt?', 'Nur Ziffern 0 bis 6 verwenden (7, 8, 9 überspringen); 0 bis 2 = Treffer',
     ['Ziffern 0 bis 2 = Treffer, alle anderen kein Treffer', 'Ziffern 0 bis 6 = Treffer', 'Ziffern 3 bis 7 = Treffer'],
     'Man braucht 7 gleich wahrscheinliche Ausgänge: die Ziffern 0 bis 6. Davon 3 als Treffer. Ohne Überspringen wäre p = 3/10.', 'Wie bekommt man genau 7 gleich wahrscheinliche Ziffern?', art='K')

# zufallsziffern
_f1 = '4719 0382 6650 1197 2843'
_n1 = sum(1 for z in _zif(_f1) if z <= 5)
SW.z('zufallsziffern', 2, f'Regel: Die Ziffern 0 bis 5 sind Treffer (p = 0,6). Zähle die Treffer in den 20 Zufallsziffern {_f1}.', _n1, str(_n1),
     f'Treffer sind alle Ziffern 0 bis 5. Durchzählen ergibt {_n1} Treffer, also {_n1} von 20.', 'Gehe die Ziffern einzeln durch und mach eine Strichliste.')
_f2 = '5208 9134 7726 0381 6495'
_n2 = sum(1 for z in _zif(_f2) if z <= 2)
SW.z('zufallsziffern', 2, f'Regel: Die Ziffern 0 bis 2 sind Treffer. Zufallsziffern (20 Stück): {_f2}. Gib die relative Häufigkeit der Treffer als Dezimalzahl an.', Fr(_n2, 20),
     f'{_n2} / 20', f'Treffer (0, 1, 2): {_n2}. Relative Häufigkeit {_n2} : 20 = {zt(Fr(_n2, 20))}.', 'Zählen, dann durch 20 teilen.')
_g3 = '307 581 924 116 853 470 692 238'
_n3 = sum(1 for g in _gruppen(_g3) if sum(1 for z in g if z <= 4) >= 2)
SW.z('zufallsziffern', 3, f'Simulation „mindestens zwei Treffer bei drei Versuchen“: Jede 3er-Gruppe ist ein Durchgang, die Ziffern 0 bis 4 sind Treffer. In wie vielen Durchgängen gab es mindestens zwei Treffer? Gruppen: {_g3}',
     _n3, str(_n3), 'Zähle in jeder Gruppe die Ziffern 0 bis 4: 307 (2), 581 (1), 924 (2), 116 (2), 853 (1), 470 (2), 692 (1), 238 (2). Mindestens zwei: ' + str(_n3) + ' Durchgänge.',
     'Zähle Gruppe für Gruppe die Treffer.', art='P')
_g4 = '5183 7094 8812 3601'
_n4 = sum(1 for g in _gruppen(_g4) if sum(1 for z in g if z <= 6) >= 3)
SW.z('zufallsziffern', 3, f'Eine Fußballerin trifft mit p = 0,7 (Ziffern 0 bis 6 = Treffer). Ein Durchgang sind 4 Schüsse (4 Ziffern). In wie vielen Durchgängen trifft sie mindestens 3-mal? Durchgänge: {_g4}',
     _n4, str(_n4), '5183: 3 Treffer. 7094: 2 (7 und 9 nicht). 8812: 2. 3601: 4. Mindestens 3 Treffer: ' + str(_n4) + ' Durchgänge.', 'Nicht-Treffer sind nur 7, 8 und 9.', art='P')
_f5 = '3 8 5 0 6 2 9 1 6 4'
_gueltig = [z for z in _zif(_f5) if 1 <= z <= 6]
_n5 = _gueltig.index(6) + 1
SW.z('zufallsziffern', 3, f'„Warten auf die erste Sechs“: Ziffern 1 bis 6 sind Würfe, 0, 7, 8, 9 werden übersprungen. Ziffernfolge: {_f5}. Beim wievielten gültigen Wurf kommt die erste Sechs?', _n5, str(_n5),
     'Gültig: 3, (8 weg), 5, (0 weg), 6. Die Sechs ist der ' + str(_n5) + '. gültige Wurf.', 'Streiche zuerst alle Ziffern, die keine Würfelzahl sind.', art='K')
_p6 = '37 82 15 64 90 28 73 46'
_n6 = sum(1 for g in _gruppen(_p6) if all(z % 2 == 0 for z in g))
SW.z('zufallsziffern', 3, f'Familien mit zwei Kindern werden simuliert: gerade Ziffer (auch 0) = Mädchen, ungerade = Junge. Paare: {_p6}. In wie vielen Familien sind beide Kinder Mädchen?', _n6, str(_n6),
     'Beide Ziffern gerade: 82, 64, 28, 46. Bei 90 ist die 9 ungerade. Also ' + str(_n6) + ' Familien.', 'Prüfe in jedem Paar beide Ziffern.', art='K')

# auswerten
SW.z('auswerten', 2, 'Eine Simulation mit 300 Durchgängen ergab 84 Treffer. Gib den Schätzwert für die Wahrscheinlichkeit in Prozent an.', 28, '84 / 300 * 100', '84 : 300 = 0,28 = 28 %.',
     'Treffer durch Durchgänge.', einheit='%')
SW.z('auswerten', 2, 'Eine Simulation liefert für ein Ereignis den Schätzwert 0,32. Wie oft erwartest du es bei 250 echten Versuchen?', 80, '0.32 * 250', '0,32 · 250 = 80.',
     'Schätzwert mal Anzahl der Versuche.')
SW.z('auswerten', 3, 'Zwei Simulationen desselben Experiments: A ergab 30 Treffer in 50 Durchgängen, B 560 Treffer in 1 000. Fasse beide zusammen. Welcher Schätzwert ergibt sich? Runde auf zwei Nachkommastellen.',
     0.56, '(30 + 560) / (50 + 1000)', 'Zusammen: 590 Treffer in 1 050 Durchgängen. 590 : 1 050 ≈ 0,56. (Nicht den Mittelwert von 0,6 und 0,56 bilden – B zählt viel mehr.)',
     'Addiere alle Treffer und alle Durchgänge.', toleranz=0.01, art='P')
SW.a('auswerten', 3, 'Eine Münze zeigt in einer Simulation mit 50 Würfen 24-mal Wappen (0,48). Ist sie gezinkt?', 'Nein, so kleine Abweichungen von 0,5 sind bei 50 Würfen normal.',
     ['Ja, sonst wären es genau 25.', 'Ja, Wappen ist zu selten.', 'Das kann man nie entscheiden.'],
     'Der Schätzwert schwankt um die Wahrscheinlichkeit. 24 statt 25 ist eine sehr kleine Abweichung. Erst große, wiederholte Abweichungen bei vielen Würfen wären verdächtig.',
     'Wie groß ist die Abweichung von der Hälfte?', art='P')
SW.z('auswerten', 3, 'Eine Simulation ergab den Schätzwert 0,15 mit genau 21 Treffern. Wie viele Durchgänge waren es?', 140, '21 / 0.15', 'Treffer : Durchgänge = 0,15 ⇔ Durchgänge = 21 : 0,15 = 140.',
     'Rückwärts: Stelle Treffer : n = 0,15 nach n um.', art='K')
SW.z('auswerten', 3, 'Eine Simulation von „mindestens eine Sechs bei vier Würfen“ ergab den Schätzwert 0,52. Wie oft erwartest du bei 500 Durchgängen „keine Sechs bei vier Würfen“?', 240, '(1 - 0.52) * 500',
     'Gegenereignis: 1 − 0,52 = 0,48. Erwartet: 0,48 · 500 = 240.', '„Keine Sechs“ ist das Gegenteil von „mindestens eine Sechs“.', art='K')

# monte_carlo
SW.z('monte_carlo', 2, 'Ein Quadrat hat die Seitenlänge 6 cm. Von 400 Zufallspunkten liegen 100 in einer Figur. Schätze den Flächeninhalt der Figur.', 9, '100 / 400 * 36',
     'Anteil 100 : 400 = 0,25. Fläche ≈ 0,25 · 36 cm² = 9 cm².', 'Anteil der Punkte mal Fläche des Quadrats.', einheit='cm²')
SW.z('monte_carlo', 2, 'Ein Rechteck ist 10 cm lang und 5 cm breit. Von 250 Zufallspunkten darin liegen 140 in einer Figur. Schätze ihren Flächeninhalt.', 28, '140 / 250 * 50',
     'Anteil 0,56. Rechteck 50 cm². Fläche ≈ 0,56 · 50 = 28 cm².', 'Es geht auch mit einem Rechteck statt eines Quadrats.', einheit='cm²')
SW.z('monte_carlo', 3, 'In ein Quadrat mit 10 cm Seitenlänge wird ein Kreis mit Radius 5 cm gezeichnet. Wie viele von 400 Zufallspunkten liegen ungefähr im Kreis? (π ≈ 3,14)', 314, '3.14 * 25 / 100 * 400',
     'Kreis: 3,14 · 25 = 78,5 cm², Quadrat 100 cm². Anteil 0,785. Erwartet: 0,785 · 400 = 314 Punkte.', 'Berechne den Flächenanteil des Kreises.', art='P')
SW.z('monte_carlo', 3, 'Ein See liegt auf einer Karte in einem Quadrat, das 2 km × 2 km darstellt. Von 300 Zufallspunkten liegen 87 im See. Schätze die Fläche des Sees.', 1.16, '87 / 300 * 4',
     'Anteil 87 : 300 = 0,29. Quadrat 4 km². Fläche ≈ 0,29 · 4 = 1,16 km².', 'Anteil der Punkte mal Fläche des Quadrats.', einheit='km²', art='P')
SW.z('monte_carlo', 3, 'Viertelkreis (Radius 1) im Einheitsquadrat: Wie viele von 1 000 Zufallspunkten erwartest du im Viertelkreis? (π ≈ 3,14)', 785, '3.14 / 4 * 1000',
     'Viertelkreis: π/4 ≈ 0,785, Quadrat 1. Erwartet ≈ 0,785 · 1 000 = 785 Punkte.', 'Welcher Anteil des Quadrats ist der Viertelkreis?', art='K')
SW.z('monte_carlo', 3, 'Die Diagonale teilt ein Quadrat in zwei gleiche Dreiecke. Von 200 Zufallspunkten liegen 112 im unteren Dreieck. Um wie viele Prozentpunkte weicht der Anteil vom wahren Anteil ab?', 6,
     '112 / 200 * 100 - 50', 'Wahrer Anteil: 50 %. Simuliert: 112 : 200 = 56 %. Abweichung: 6 Prozentpunkte.', 'Welcher Anteil wäre genau richtig?', einheit='%', art='K')

# beurteilen
SW.a('beurteilen', 2, 'Ein Ereignis hat p = 0,4. Simuliert wird mit einem Würfel, 1 und 2 sind Treffer. Ist das geeignet?', 'Nein, der Würfel hat p = 1/3.', ['Ja, das passt genau.',
     'Ja, jedes Zufallsgerät ist geeignet.'], '2 von 6 Zahlen: p = 1/3 ≈ 0,33, nicht 0,4.', 'Rechne die Wahrscheinlichkeit des Geräts aus.')
SW.a('beurteilen', 2, 'Ein Bus hat mit p = 0,25 Verspätung. Simuliert wird mit zwei Münzen: Treffer nur bei „zweimal Wappen“. Ist das geeignet?', 'Ja, das Gerät hat genau p = 1/4.',
     ['Nein, zwei Münzen haben p = 1/2.', 'Nein, man braucht vier Münzen.'], 'Zwei Münzen: WW, WZ, ZW, ZZ. Nur WW ist Treffer: 1/4 = 0,25.', 'Wie viele Ergebnisse haben zwei Münzen?')
SW.a('beurteilen', 3, 'Eine Elfmeterschützin trifft mit p = 0,8. Simuliert wird mit einem Würfel, 1 bis 5 = Treffer. Ist das geeignet?', 'Nein, der Würfel hat p = 5/6 ≈ 0,83 – das ist zu viel.',
     ['Ja, das passt genau.', 'Ja, 5 Treffer von 6 sind 80 %.', 'Nein, der Würfel hat p = 0,5.'], '5/6 ≈ 0,833, nicht 0,8. Geeignet wären z. B. Zufallsziffern 0 bis 7.', 'Rechne 5 : 6 aus.', art='P')
SW.a('beurteilen', 3, 'Ein Kind sagt: „Unsere Simulation mit 10 Durchgängen ergab 0,6. Also ist die Wahrscheinlichkeit genau 0,6.“ Was stimmt?', 'Das ist nur ein grober Schätzwert; mit viel mehr Durchgängen wird er verlässlicher.',
     ['Richtig, Simulationen liefern den genauen Wert.', 'Falsch, Simulationen sagen nichts über Wahrscheinlichkeiten.', 'Richtig, wenn das Zufallsgerät passt.'],
     'Bei 10 Durchgängen schwankt der Anteil stark. Er schätzt die Wahrscheinlichkeit nur grob. Nach dem Gesetz der großen Zahlen hilft eine größere Anzahl.', 'Was passiert bei wenigen Versuchen?', art='P')
SW.a('beurteilen', 3, 'Aus einer Urne mit 2 roten und 3 blauen Kugeln werden zwei Kugeln OHNE Zurücklegen gezogen. Jemand simuliert beide Züge mit Zufallsziffern (0 bis 3 = rot). Ist das geeignet?',
     'Nein: Beim zweiten Zug sind nur noch 4 Kugeln da, die Wahrscheinlichkeit ändert sich.', ['Ja, 0 bis 3 gibt p = 0,4 = 2/5.', 'Ja, Ziehen ohne Zurücklegen ist wie Würfeln.',
     'Nein, man muss 0 bis 2 nehmen.'],
     'Für den ersten Zug passt p = 0,4. Danach ist die Urne verändert (z. B. 1 rote von 4). Die feste Regel für beide Züge passt also nicht.', 'Bleibt die Urne nach dem ersten Zug gleich?', art='K')
SW.a('beurteilen', 3, 'Mit einer Urne aus 6 roten und 4 blauen Kugeln (mit Zurücklegen) wird p = 0,6 simuliert. Welche Urne ist genauso geeignet?', '3 rote und 2 blaue Kugeln',
     ['6 rote und 6 blaue Kugeln', '3 rote und 4 blaue Kugeln', '60 rote und 4 blaue Kugeln'],
     'Es kommt nur auf den Anteil an: 3 von 5 = 0,6. Die anderen ergeben 0,5, 3/7 ≈ 0,43 und 60/64 ≈ 0,94.', 'Berechne bei jeder Urne den Anteil der roten Kugeln.', art='K')

baue = mit_schwer(baue, SW)
# ---- SCHWER ENDE ----

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, mit_befunden  # noqa: E402

BF = Befunde('stochastik.simulation', 13_8_14)
# b) „etwa zu erwarten“ mit Kommazahl als exakte Lösung → ganze Zahlen 712 und 713 zulassen
BF.loesung('auswerten', 'Eine Simulation mit 400 Durchgängen ergab 57-mal „Gewinn beim Losen“. Wie oft ist das Ereignis bei 5000 echten Durchgängen etwa zu erwarten?',
           o={'wert': 712.5, 'toleranz': 0.5},
           w='P ≈ 57 : 400 = 0,1425. Erwartet: 0,1425 · 5000 = 712,5, also etwa 712- bis 713-mal.')
# c) Beinahe-Dublette (zweimal p = 5/6 mit Urne 7 von 10) → neue Prüfaufgabe
BF.ersetze('beurteilen', 'Ein Bauteil ist fehlerhaft mit p = 5/6. Simuliert wird mit einer Urne mit 7 roten von 10 Kugeln (mit Zurücklegen). Ist das geeignet?', BF.A(
    'Ein Bauteil ist mit p = 0,15 fehlerhaft. Simuliert wird mit Zufallszahlen von 00 bis 99; Treffer sind die Zahlen 00 bis 15. Ist das geeignet?',
    'Nein: 00 bis 15 sind 16 Zahlen, das Gerät hat also p = 0,16.',
    ['Ja, das Gerät hat genau p = 0,15.', 'Ja, jedes Zufallsgerät ist geeignet.', 'Nein, mit Zufallszahlen kann man nie Wahrscheinlichkeiten simulieren.'],
    'Von 00 bis 15 sind es 16 Zahlen (die 00 mitzählen!), also p = 16/100 = 0,16 ≠ 0,15. Richtig wären die Treffer 00 bis 14.',
    'Zähle die Treffer-Zahlen genau (die 00 mitzählen) und vergleiche die Wahrscheinlichkeit.'))
# a) einschrittig p · 360° → Stufe 2
for _p in ['0,35', '0,45', '0,6', '0,8']:
    BF.stufe('zufallsgeraet', f'Ein Glücksrad soll einen Treffer mit p = {_p} simulieren. Wie groß muss der Mittelpunktswinkel des Trefferfeldes sein (in Grad)?', 2)
BF.nicht_umgesetzt('auswerten S3 „Gruppe A 100 / B 50 Durchgänge – wessen Schätzwert …“ (3×)', 'Kein Fehler; Übungsreihe zum selben Gedanken mit verschiedenen Zahlen.')
BF.fuer_sebastian('stochastik.simulation: lehrplan_gym leer; Simulation steht im LehrplanPLUS Gym Kl. 8 nicht als eigener Inhalt – als Vertiefung zu Laplace/relative Häufigkeit führen? Karten-Texte nicht geändert.')

baue = mit_befunden(baue, BF)
# ---- BEFUNDE ENDE ----

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


# ---------- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl10) ----------
# Gesamtdurchsicht (seit D2 Klasse 10): jede Lernkarte und jede Aufgabe gelesen und nachgerechnet. Läuft ganz am Ende auf der fertigen Datei.
# Neue Stufe-3-Übungen nach den Beispielen des LehrplanPLUS M10 2 (Simulation bei nicht direkt berechenbaren Wahrscheinlichkeiten:
# Geburtstagsproblem, vertauschte Briefe, Ziegenproblem; Werte auf Plausibilität prüfen) – eigene Zahlen und Einkleidung.
def durchsicht():
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _durchsicht_kl10 import Durchsicht
    D = Durchsicht('stochastik.simulation', 19040)
    # zufallsgeraet: „Welches Zufallsgerät passt?“ steht gleich auf Stufe 1 und 2
    D.stufe([5, 8], 1, '')
    # regel: dreistellige Zufallszahlen = die zweistellige Regel mit einer Stelle mehr
    D.stufe(56, 2, 'Mit dreistelligen Zufallszahlen')
    # auswerten: „Wessen Schätzwert ist zuverlässiger?“ (dreimal) ist Grundwissen der Karte, kein anderer Gedanke
    D.stufe([101, 102, 103], 2, 'Gruppe A simuliert')
    # beurteilen: „Ist das Gerät geeignet?“ mit gleicher Rechnung wie Stufe 2 (bzw. 1)
    D.stufe([160, 163], 2, '')
    D.stufe(161, 1, 'Ein Bauteil ist fehlerhaft mit p = 0,3')
    D.neu('auswerten', 3, D.A('Eine Simulation mit 1 000 Schulklassen zu je 25 Kindern ergab 571-mal „mindestens zwei Kinder haben am selben Tag Geburtstag“. '
                              'Jemand meint: „Das kann nicht stimmen, das Jahr hat doch 365 Tage.“ Was stimmt?',
                              'Die Simulation ist plausibel: Bei 25 Kindern gibt es 300 Paare, die gleich sein können; berechnet ist P ≈ 0,57.',
                              ['Der Einwand stimmt: P ist etwa 25 : 365 ≈ 0,07.', 'Der Einwand stimmt: Bei 365 Tagen ist P genau 0.',
                               'Die Simulation ist falsch, weil man Geburtstage nicht simulieren kann.'],
                              'Es geht nicht um einen bestimmten Tag, sondern um irgendein Paar: 25 · 24 : 2 = 300 Paare. Gerechnet: P = 1 − (365 · 364 · … · 341) : 365²⁵ ≈ 0,569. '
                              'Der Schätzwert 0,571 passt.',
                              'Vergleiche nicht mit einem bestimmten Tag: Wie viele Paare von Kindern gibt es in der Klasse?'))
    D.neu('auswerten', 3, D.Z('Drei Briefe werden zufällig in drei adressierte Umschläge gesteckt. Eine Simulation ergab bei 600 Durchgängen 203-mal „kein Brief im richtigen Umschlag“. '
                              'Prüfe den Schätzwert: Bei wie vielen der 6 möglichen Reihenfolgen steckt kein Brief richtig?', 2, '6 - 1 - 3',
                              'Reihenfolgen der Briefe A, B, C in den Umschlägen A, B, C: ABC (3 richtig), ACB, BAC, CBA (je 1 richtig), BCA, CAB (keiner richtig). '
                              'Also 2 von 6: P = 1/3 ≈ 0,333; der Schätzwert 203 : 600 ≈ 0,338 passt.',
                              'Schreibe alle 6 Reihenfolgen auf und prüfe jede.'))
    D.neu('beurteilen', 3, D.A('Bei einer Spielshow steht hinter einer von drei Türen ein Auto. Nach der Wahl öffnet der Moderator eine andere Tür mit einer Ziege und bietet den Wechsel an. '
                               'Eine Simulation von 300 Spielen „immer wechseln“ ergab 198 Gewinne. Was stimmt?',
                               'Schätzwert 0,66 – das passt zum berechneten Wert 2/3.',
                               ['Schätzwert 0,66 – die Simulation ist falsch, richtig wäre 1/2.', 'Schätzwert 0,198 – Wechseln lohnt sich nicht.',
                                'Schätzwert 0,66 – das passt zum berechneten Wert 1/3.'],
                               'Wer wechselt, gewinnt genau dann, wenn die erste Wahl eine Ziege war: P = 2/3 ≈ 0,667. Der Schätzwert 198 : 300 = 0,66 passt.',
                               'Wann gewinnt man beim Wechseln? Wie wahrscheinlich ist es, zuerst eine Ziege zu wählen?'))
    D.fuer_sebastian('stochastik.simulation (seit D2 Klasse 10): Die Karten haben Klasse-8-Niveau (Zufallsgerät wählen, Regel, Ziffern zählen). LehrplanPLUS M10 2 nennt '
                     'Simulation für nicht direkt berechenbare Wahrscheinlichkeiten (vertauschte Briefe, Ziegenproblem, Geburtstagsproblem) – jetzt drei Stufe-3-Übungen, keine Lernkarte. '
                     'In der Themendatei steht weiter klasse gym_by 8 (Themenliste: 10). π-Übungen überschneiden sich mit stochastik.mehrstufig/pi_schaetzen.')
    D.anwenden()


if __name__ == '__main__':
    durchsicht()  # Neunzehnte Runde (durchsicht-kl10) – ganz am Ende


# ---------- STUFEN (Zwanzigste Runde, Zweig stufen-kl10) ----------
def stufen():
    import math
    import sys as _sys
    from fractions import Fraction as _F
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _stufen_kl10 import Stufen
    S = Stufen('stochastik.simulation', 2040)
    Z, A, ZR = S.Z, S.A, S.ZR

    def B(text, zaehler, nenner, w, h):
        f = _F(zaehler, nenner)
        assert (f.numerator, f.denominator) == (zaehler, nenner), (text, f)
        return S.L(text, '□/□', [zaehler, nenner], [str(zaehler), str(nenner)], w, h, hinweis='Zähler und Nenner (gekürzt)')

    # --- zufallsgeraet ---
    S.stufenleiter('zufallsgeraet', 'Ein Zufallsgerät mit genau der gesuchten Wahrscheinlichkeit erkennen oder einrichten (Urne, Würfel, Ziffer).',
                   'Kugelzahl und Winkel für ein gegebenes p berechnen, Regeln für Würfel und Glücksrad.',
                   'Tabellenkalkulation, Münze für 1/4, Feldzahl als Parameter, Fehler „ohne Zurücklegen“, zwei Drehungen verknüpfen, Bedingung für gleiche Chancen wie im BMT.')
    S.g('zufallsgeraet', erkennen=[0, 1, 2, 3, 5, 8], mehrschritt=[4, 6, 7, 9], darstellung=[10, 11, 12, 13, 24], umkehr=[25],
        transfer=[26, 27], begruenden=[28, 29])
    S.ueberzaehlig(3, 5, 8)
    S.neu('zufallsgeraet', 'direkt', Z('Eine Urne mit 10 Kugeln soll p = 0,4 simulieren (rot = Treffer, mit Zurücklegen). Wie viele rote Kugeln braucht man?', 4, '10 * 0.4',
                                       '0,4 = 4/10: 4 rote von 10 Kugeln.', 'Schreibe p als Bruch mit Nenner 10.'))
    S.neu('zufallsgeraet', 'direkt', Z('Ein Würfel soll ein Ereignis mit p = 1/3 simulieren. Wie viele Augenzahlen müssen als Treffer zählen?', 2, '6 / 3',
                                       '1/3 = 2/6: zwei Augenzahlen, z. B. 1 und 2.', 'Schreibe p als Bruch mit Nenner 6.'))
    S.neu('zufallsgeraet', 'fehler', A('Jemand simuliert p = 0,3 mit einer Urne aus 3 roten und 7 weißen Kugeln, legt die gezogenen Kugeln aber nicht zurück. Was stimmt?',
                                       'Falsch: Ohne Zurücklegen ändert sich p nach jedem Zug; man muss zurücklegen.',
                                       ['Richtig, so ist es sogar genauer.', 'Falsch: Man braucht 30 rote Kugeln.', 'Richtig, solange man höchstens 10-mal zieht.'],
                                       'Nach einer roten Kugel wäre p = 2/9 ≈ 0,22, nach einer weißen 3/9 ≈ 0,33. Damit p jedes Mal 0,3 ist, muss die Kugel zurück.', 'Wie groß ist p beim zweiten Zug?'))
    S.neu('zufallsgeraet', 'parameter', Z('Ein Glücksrad hat n gleich große Felder, 3 davon sind Trefferfelder. Für welches n liefert es p = 0,15?', 20, '3 / 0.15',
                                          '3/n = 0,15 ⇒ n = 3 : 0,15 = 20.', 'Stelle die Gleichung 3/n = 0,15 auf.'))
    S.neu('zufallsgeraet', 'verknuepfen', Z('Ein Glücksrad hat zwei Trefferfelder mit 40° und 32°. Es wird zweimal gedreht. Wie groß ist P(zweimal Treffer)?', 0.04, '((40 + 32) / 360) ** 2',
                                            'Trefferfeld zusammen 72°, p = 72/360 = 0,2. Zwei Drehungen: 0,2 · 0,2 = 0,04.', 'Erst p für eine Drehung, dann die Pfadregel.'))
    S.neu('zufallsgeraet', 'pruefung', A('Ein Glücksrad hat vier Felder mit den Ziffern 1, 2, 3 und 4. Was muss zusätzlich gelten, damit jede Ziffer mit der Wahrscheinlichkeit 1/4 erscheint?',
                                         'Alle vier Felder sind gleich groß.', ['Das Rad wird viermal gedreht.', 'Die Ziffern stehen der Größe nach.', 'Feld 1 ist das größte.'],
                                         'Nur bei gleich großen Feldern (je 90°) ist jedes Ergebnis gleich wahrscheinlich (Laplace-Experiment).', 'Wovon hängt beim Glücksrad die Wahrscheinlichkeit eines Feldes ab?'))
    S.bonus('zufallsgeraet', A('Wie kann man mit einer fairen Münze ein Ereignis mit p = 1/3 simulieren?', 'Zweimal werfen: WW = Treffer, WZ oder ZW = kein Treffer, bei ZZ von vorn beginnen.',
                               ['Einmal werfen, Wappen = Treffer.', 'Dreimal werfen, genau einmal Wappen = Treffer.', 'Das geht mit einer Münze nicht.'],
                               'Die drei gültigen Ausgänge WW, WZ, ZW sind gleich wahrscheinlich; ZZ wird verworfen. Also hat WW den Anteil 1 von 3. „Dreimal werfen, genau einmal Wappen“ hätte 3/8.',
                               'Man darf Ergebnisse verwerfen und neu werfen.'))
    S.bonus('zufallsgeraet', A('Mit einem Würfel soll p = 1/5 simuliert werden. Welche Regel liefert genau 1/5?', '1 = Treffer, 2 bis 5 = kein Treffer, bei einer 6 noch einmal würfeln.',
                               ['1 = Treffer, sonst kein Treffer.', '1 oder 2 = Treffer, sonst kein Treffer.', 'Fünfmal würfeln, eine Sechs = Treffer.'],
                               'Verwirft man die 6, bleiben 5 gleich wahrscheinliche Augenzahlen; eine davon ist Treffer: 1/5. Die anderen Regeln liefern 1/6, 1/3 bzw. etwas anderes.',
                               'Wie viele gleich wahrscheinliche Ergebnisse braucht man?'))

    # --- regel ---
    S.stufenleiter('regel', 'Aus p die Zahl der Trefferziffern bestimmen und zu einer Regel die simulierte Wahrscheinlichkeit erkennen.',
                   'Zweistellige und dreistellige Zufallszahlen, Regeln für Sachsituationen, mehrere Ziffern je Durchgang.',
                   'Ziffern überspringen für 2/3 oder einen Würfel, zwei verschiedene p, Stellenzahl als Parameter, Fehler „00 bis 25“, Grenzen der Münze begründen.')
    S.g('regel', direkt=[30, 31, 32, 33], darstellung=[34, 35, 36, 37, 38, 39, 54], umkehr=[55], mehrschritt=[56, 57],
        transfer=[40, 43, 42], verknuepfen=[41, 59], begruenden=[58])
    S.neu('regel', 'erkennen', A('Regel: Die Zufallsziffern 0 bis 3 sind Treffer. Welche Wahrscheinlichkeit wird simuliert?', '0,4', ['0,3', '0,03', '0,04'],
                                 '0, 1, 2, 3 sind 4 von 10 Ziffern: p = 0,4.', 'Zähle die Trefferziffern – die 0 zählt mit.'))
    S.neu('regel', 'erkennen', A('Welche Zufallszahlen braucht man, um p = 0,37 zu simulieren?', 'zweistellige Zahlen 00 bis 99', ['Ziffern 0 bis 9', 'einen Würfel', 'eine Münze'],
                                 '0,37 = 37/100: Man braucht 100 gleich wahrscheinliche Zahlen.', 'Wie viele Nachkommastellen hat p?'))
    S.neu('regel', 'einkleidung', A('Ein Torwart hält 12 % der Elfmeter. Welche Regel mit Zufallszahlen 00 bis 99 passt?', '00 bis 11 = gehalten', ['00 bis 12 = gehalten', '0 bis 1 = gehalten (eine Ziffer)', '00 bis 88 = gehalten'],
                                    '12 % = 12 von 100 Zahlen: 00 bis 11. 00 bis 12 wären 13 Zahlen.', 'Zähle, wie viele Zahlen von 00 bis 11 sind.'))
    S.neu('regel', 'fehler', A('Jemand will p = 0,25 mit den Zahlen 00 bis 99 simulieren und wählt 00 bis 25 als Treffer. Was stimmt?', 'Falsch: 00 bis 25 sind 26 Zahlen; richtig ist 00 bis 24.',
                               ['Richtig.', 'Falsch: richtig ist 01 bis 26.', 'Falsch: richtig ist 00 bis 75.'],
                               'Von 00 bis 25 sind es 26 Zahlen, das gäbe p = 0,26. Mit 00 bis 24 sind es genau 25.', 'Zähle die Zahlen von 00 bis 25 – die 00 ist dabei.'))
    S.neu('regel', 'parameter', Z('Mit k-stelligen Zufallszahlen (alle Ziffern von 0 bis 9) soll p = 0,125 simuliert werden. Wie groß muss k mindestens sein?', 3, '3',
                                  '0,125 = 125/1 000: Man braucht 1 000 gleiche Zahlen, also 000 bis 999 – dreistellig.', 'Wie viele Nachkommastellen hat p?'))
    S.bonus('regel', Z('Ein Würfel wird mit Zufallsziffern simuliert: 1 bis 6 sind Würfe, 0, 7, 8 und 9 werden übersprungen. Wie viele Zufallsziffern braucht man im Mittel für 60 Würfe?', 100, '60 / (6 / 10)',
                       'Nur 6 von 10 Ziffern sind gültig. Für 60 gültige Ziffern braucht man im Mittel 60 : 0,6 = 100 Ziffern.', 'Welcher Anteil der Ziffern ist brauchbar?'))
    S.bonus('regel', A('Mit einer Zufallsziffer je Versuch soll p = 1/7 simuliert werden. Welche Regel passt?', 'Ziffern 1 bis 7 verwenden (0, 8, 9 überspringen), 1 = Treffer',
                       ['Ziffern 0 bis 9 verwenden, 0 = Treffer', 'Ziffern 0 bis 6 verwenden, 0 und 1 = Treffer', 'Ziffer 7 = Treffer, alle anderen nicht'],
                       'Nach dem Überspringen bleiben 7 gleich wahrscheinliche Ziffern; eine davon ist Treffer: 1/7. Die anderen Regeln liefern 1/10, 2/7 bzw. 1/10.',
                       'Man darf Ziffern überspringen.'))

    # --- zufallsziffern ---
    S.stufenleiter('zufallsziffern', 'Mit einer Regel Treffer in einer Ziffernliste erkennen und zählen.',
                   'Relative Häufigkeit und Nicht-Treffer, Sachsituationen auswerten, Durchgänge aus mehreren Ziffern.',
                   '„Mindestens“-Ereignisse in Durchgängen, Warten auf die erste Sechs, Regel als Parameter, Zählfehler finden, Unabhängigkeit der Listen begründen.')
    S.g('zufallsziffern', direkt=[60, 61, 62, 63, 84], mehrschritt=[64, 65, 67, 68, 85, 71], umkehr=[66, 69], einkleidung=[89],
        transfer=[70, 72, 73, 88], verknuepfen=[86, 87])
    S.ueberzaehlig(73)
    S.neu('zufallsziffern', 'erkennen', A('Die Ziffern 7 1 4 0 9 werden mit der Regel „0 bis 2 = Treffer“ ausgewertet. Welche Ziffern sind Treffer?', '1 und 0', ['7 und 9', '1, 4 und 0', 'nur 0'],
                                          'Nur 0, 1 und 2 sind Treffer; in der Liste kommen 1 und 0 vor.', 'Gehe die Ziffern einzeln durch.'))
    S.neu('zufallsziffern', 'erkennen', A('Was ist bei einer Simulation mit Zufallsziffern ein „Durchgang“?', 'eine Gruppe von Ziffern, die einmal das ganze Experiment darstellt',
                                          ['immer eine einzelne Ziffer', 'die ganze Ziffernliste', 'jede Ziffer 0'],
                                          'Besteht das Experiment aus 3 Würfen, ist ein Durchgang eine Gruppe aus 3 Ziffern.', 'Wie oft wird das echte Experiment pro Gruppe nachgespielt?'))
    S.neu('zufallsziffern', 'einkleidung', Z('Ein Basketballer trifft mit p = 0,4 (Regel: 0 bis 3 = Treffer). Die Ziffern für 10 Würfe: 5 0 8 3 1 9 6 2 7 4. Wie viele Treffer ergibt die Simulation?', 4, '4',
                                             'Treffer sind 0, 3, 1, 2: vier Treffer.', 'Markiere alle Ziffern von 0 bis 3.'))
    S.neu('zufallsziffern', 'einkleidung', Z('Eine Ampel ist mit p = 0,2 rot (Regel: 0 und 1 = rot). Simuliert werden 15 Ankünfte: 381 905 772 146 630. Wie oft ist die Ampel rot?', 4, '4',
                                             'Ziffern 0 oder 1: 3 8 1 | 9 0 5 | 7 7 2 | 1 4 6 | 6 3 0 – die 1, 0, 1, 0: viermal rot.', 'Lies jede Ziffer einzeln.'))
    S.neu('zufallsziffern', 'fehler', A('Regel: 0 bis 4 = Treffer. Ein Kind zählt in der Liste 3 7 0 5 9 4 die Treffer und schreibt „2“. Was stimmt?', 'Falsch: 3, 0 und 4 sind Treffer, also 3.',
                                        ['Richtig.', 'Falsch: Es sind 4 Treffer.', 'Falsch: Es ist 1 Treffer.'], 'Die 4 gehört noch dazu („0 bis 4“ schließt 4 ein).', 'Gehört die 4 zu „0 bis 4“?'))
    S.neu('zufallsziffern', 'parameter', Z('Eine Regel lautet „Ziffern 0 bis k sind Treffer“. Für welches k simuliert sie p = 0,8?', 7, '8 - 1', '0 bis 7 sind 8 Ziffern: p = 0,8. Also k = 7.', 'Wie viele Ziffern braucht man für 0,8?'))
    S.neu('zufallsziffern', 'begruenden', A('Darf man für eine zweite Simulation einfach dieselbe Ziffernliste noch einmal verwenden?', 'Nein: Sie liefert genau dasselbe Ergebnis und ist keine neue, unabhängige Simulation.',
                                            ['Ja, Ziffern sind Ziffern.', 'Ja, wenn man dieselbe Regel benutzt.', 'Nein, jede Ziffernliste darf nur in einem Fach verwendet werden.'],
                                            'Eine Simulation lebt vom Zufall. Mit derselben Liste und Regel kommt zwangsläufig dasselbe heraus – man erfährt nichts Neues über die Schwankung.',
                                            'Was käme beim zweiten Mal heraus?'))
    S.bonus('zufallsziffern', Z('In einer Vierergruppe zufälliger Ziffern (0 bis 9, gleich wahrscheinlich): Wie groß ist die Wahrscheinlichkeit, dass mindestens zwei gleiche Ziffern vorkommen?', 0.496,
                                '1 - 10 * 9 * 8 * 7 / 10 ** 4', 'Gegenereignis „alle verschieden“: 10/10 · 9/10 · 8/10 · 7/10 = 0,504. Also 1 − 0,504 = 0,496 – fast die Hälfte!',
                                'Rechne mit dem Gegenereignis „alle vier verschieden“.'))
    S.bonus('zufallsziffern', Z('In einer Liste aus 1 000 echten Zufallsziffern gibt es 999 Paare direkt benachbarter Ziffern. Wie viele davon erwartet man mit zwei gleichen Ziffern (z. B. „77“)?', 99.9, '999 / 10',
                                'Für jedes Paar ist die zweite Ziffer mit 1/10 gleich der ersten. Erwartet: 999 · 0,1 = 99,9. Liegen in einer Liste fast keine solchen Paare, war sie wohl von Hand „ausgedacht“.',
                                'Wie wahrscheinlich ist es, dass eine Ziffer ihren Vorgänger wiederholt?'))

    # --- auswerten ---
    S.stufenleiter('auswerten', 'Aus Treffern und Durchgängen den Schätzwert (relative Häufigkeit) bilden und deuten.',
                   'Auf viele echte Durchgänge hochrechnen, Prozentangaben, Durchgänge rückwärts, Schätzwert in eine erwartete Anzahl umrechnen.',
                   'Simulationen zusammenfassen, Abweichungen beurteilen, Gegenereignis, Briefe und Geburtstage, Durchgangszahl als Parameter, Fehler beim Mitteln.')
    S.g('auswerten', direkt=[90, 91, 92, 93], erkennen=[101, 102, 103], mehrschritt=[94, 95, 96, 97, 98, 99], darstellung=[114], einkleidung=[115], umkehr=[118],
        begruenden=[100, 117, 180], transfer=[116], verknuepfen=[119, 181])
    S.ueberzaehlig(91, 95, 98, 99)
    S.neu('auswerten', 'erkennen', A('Eine Simulation ergab 46 Treffer in 200 Durchgängen. Was ist 46 : 200 = 0,23?', 'die relative Häufigkeit, ein Schätzwert für die Wahrscheinlichkeit',
                                     ['die genaue Wahrscheinlichkeit', 'die absolute Häufigkeit', 'die Zahl der Durchgänge'],
                                     'Treffer geteilt durch Durchgänge ist die relative Häufigkeit. Sie schätzt P, ist aber nicht genau P.', 'Was wird hier durch was geteilt?'))
    S.neu('auswerten', 'fehler', A('Simulation A: 30 Treffer in 50 Durchgängen (0,6). Simulation B: 560 Treffer in 1 000 Durchgängen (0,56). Jemand fasst zusammen: „(0,6 + 0,56) : 2 = 0,58.“ Was stimmt?',
                                   'Falsch: Treffer und Durchgänge zusammenzählen: 590 : 1 050 ≈ 0,56.', ['Richtig.', 'Falsch: 0,6 · 0,56 ≈ 0,34.', 'Falsch: Man nimmt nur A, also 0,6.'],
                                   'Der einfache Mittelwert gibt der kleinen Simulation A zu viel Gewicht. Zusammengefasst: (30 + 560) : (50 + 1 000) ≈ 0,562.', 'Wie viele Treffer und Durchgänge sind es zusammen?'))
    S.neu('auswerten', 'parameter', Z('Nach n Durchgängen ist der Schätzwert 0,25. Danach folgen 100 weitere Durchgänge mit 40 Treffern; jetzt ist der Schätzwert 0,3. Wie groß war n?', 200, '(40 - 0.3 * 100) / (0.3 - 0.25)',
                                      '(0,25n + 40) : (n + 100) = 0,3 ⇒ 0,25n + 40 = 0,3n + 30 ⇒ 0,05n = 10 ⇒ n = 200.', 'Treffer vorher: 0,25 · n. Stelle die Gleichung für den neuen Schätzwert auf.'))
    S.bonus('auswerten', Z('Nach 100 Durchgängen ist der Schätzwert 0,4. Wie viele Treffer in Folge braucht man mindestens, damit der Schätzwert über 0,5 steigt?', 21, '21',
                           '(40 + k) : (100 + k) > 0,5 ⇒ 40 + k > 50 + 0,5k ⇒ k > 20. Bei k = 20 ist er genau 0,5 – also braucht man 21 Treffer.', 'Stelle die Ungleichung für k Treffer in Folge auf.'))
    S.bonus('auswerten', B('Drei Briefe werden zufällig in drei adressierte Umschläge gesteckt. Wie groß ist die Wahrscheinlichkeit, dass genau ein Brief im richtigen Umschlag steckt?', 1, 2,
                           'Die 6 Reihenfolgen: ABC (alle richtig), ACB, CBA, BAC (je genau einer richtig), BCA, CAB (keiner). Genau einer: 3 von 6 = 1/2. Genau zwei richtig ist unmöglich.',
                           'Schreibe alle 6 Möglichkeiten auf.'))

    # --- monte_carlo ---
    S.stufenleiter('monte_carlo', 'Den Anteil der Zufallspunkte in einer Figur bilden und als Flächenanteil deuten.',
                   'Flächen in Quadraten und Rechtecken schätzen, erwartete Punktzahl aus einer bekannten Fläche.',
                   'π schätzen, Seen auf Karten, Abweichungen beurteilen, Fehler „mit der Seite statt der Fläche“, Seitenlänge als Parameter, Dartbrett, Punktzahl rückwärts.')
    S.g('monte_carlo', direkt=[120, 121, 122, 123], mehrschritt=[124, 125, 126, 127, 128, 129, 144], einkleidung=[145], umkehr=[146, 148],
        verknuepfen=[130, 131, 132, 133], transfer=[147], begruenden=[149])
    S.neu('monte_carlo', 'erkennen', A('Wie schätzt man bei der Monte-Carlo-Methode eine Fläche?', 'über den Anteil zufälliger Punkte, die in der Figur liegen',
                                       ['durch Messen mit dem Lineal', 'über die Anzahl der Ecken der Figur', 'über den Umfang der Figur'],
                                       'Der Anteil der Punkte in der Figur schätzt den Anteil der Figur an der bekannten Gesamtfläche.', 'Wofür steht der Zufall bei dieser Methode?'))
    S.neu('monte_carlo', 'erkennen', A('Von 100 Zufallspunkten im Quadrat liegen 25 in einer Figur. Welchen Teil des Quadrats nimmt die Figur ungefähr ein?', 'ein Viertel', ['ein Drittel', '25 cm²', 'drei Viertel'],
                                       '25 von 100 ist ein Viertel. Eine Fläche in cm² kann man ohne die Größe des Quadrats nicht angeben.', 'Welcher Anteil ist 25 von 100?'))
    S.neu('monte_carlo', 'fehler', A('Ein Quadrat hat 4 cm Seitenlänge; 30 von 120 Zufallspunkten liegen in einer Figur. Jemand rechnet: „Fläche ≈ 30 : 120 · 4 = 1 cm².“ Was stimmt?',
                                     'Falsch: Man muss mit der Quadratfläche 16 cm² malnehmen: 0,25 · 16 = 4 cm².', ['Richtig.', 'Falsch: 30 · 4 = 120 cm².', 'Falsch: 120 : 30 = 4 cm².'],
                                     'Der Anteil bezieht sich auf die Fläche, nicht auf die Seitenlänge.', 'Womit muss der Anteil malgenommen werden?'))
    S.neu('monte_carlo', 'parameter', Z('Eine Figur von 16 cm² liegt in einem Quadrat mit der Seitenlänge a. Von 200 Zufallspunkten liegen etwa 50 in der Figur. Wie groß ist a?', 8, '8',
                                        'Anteil 50/200 = 1/4, also ist das Quadrat 4 · 16 = 64 cm² groß und a = 8 cm.', 'Wie groß muss das Quadrat sein?', einheit='cm'))
    S.neu('monte_carlo', 'transfer', ZR('Ein Dartbrett (Kreis mit Radius 20 cm) hängt in einem quadratischen Rahmen 50 cm × 50 cm. Ein Anfänger trifft zufällig irgendeine Stelle im Rahmen. '
                                        'Wie groß ist die Wahrscheinlichkeit, das Brett zu treffen? Runde auf zwei Nachkommastellen.', math.pi * 400 / 2500, 2,
                                        'Kreis: π · 20² ≈ 1 256,6 cm²; Rahmen 2 500 cm². Anteil ≈ 0,50.', 'Wahrscheinlichkeit = Kreisfläche : Rahmenfläche.'))
    S.neu('monte_carlo', 'rueckwaerts', Z('Eine Simulation mit 250 Punkten in einem Quadrat mit 10 cm Seitenlänge ergab für eine Figur den Schätzwert 60 cm². Wie viele Punkte lagen in der Figur?', 150, '250 * 60 / 100',
                                          'Anteil 60 : 100 = 0,6. 0,6 · 250 = 150 Punkte.', 'Welcher Anteil der Quadratfläche sind 60 cm²?'))
    S.bonus('monte_carlo', B('Ein Zufallspunkt (x | y) liegt im Einheitsquadrat (0 ≤ x ≤ 1, 0 ≤ y ≤ 1). Wie groß ist die Wahrscheinlichkeit für x + y < 1/2?', 1, 8,
                             'Die Punkte mit x + y < 1/2 bilden ein Dreieck mit den Ecken (0 | 0), (1/2 | 0), (0 | 1/2). Fläche 1/2 · 1/2 · 1/2 = 1/8.', 'Zeichne die Gerade x + y = 1/2.'))
    S.bonus('monte_carlo', B('Ein Zufallspunkt (x | y) liegt im Einheitsquadrat. Wie groß ist die Wahrscheinlichkeit, dass x größer als 2y ist?', 1, 4,
                             'x > 2y heißt y < x/2: das Dreieck unter der Geraden y = x/2 mit den Ecken (0 | 0), (1 | 0), (1 | 1/2). Fläche 1/2 · 1 · 1/2 = 1/4.', 'Zeichne die Gerade y = x/2 ins Quadrat.'))

    # --- beurteilen ---
    S.stufenleiter('beurteilen', 'Die Wahrscheinlichkeit eines Zufallsgeräts bestimmen und mit dem gesuchten p vergleichen.',
                   'Geräte mit Brüchen, Winkeln und mehreren Münzen prüfen, das passende Gerät für eine Sachsituation wählen.',
                   'Zählfehler und „zu viel“ erkennen, Simulation ohne Zurücklegen, gleichwertige Urnen, Ziegenproblem, Feldzahl als Parameter, Term für Anzahlen wie im BMT.')
    S.g('beurteilen', erkennen=[150, 151, 152, 153, 161], mehrschritt=[154, 155, 156, 157, 158, 159, 160, 163, 174], umkehr=[175],
        fehler=[162], begruenden=[176, 177], verknuepfen=[178], transfer=[179, 182])
    S.ueberzaehlig(153, 161, 157, 158, 159, 160, 163, 174)
    S.neu('beurteilen', 'direkt', B('Ein Würfel wird als Zufallsgerät benutzt: 1 bis 4 = Treffer. Welche Wahrscheinlichkeit simuliert er?', 2, 3, '4 von 6 Augenzahlen: 4/6 = 2/3.', 'Wie viele Augenzahlen sind Treffer?'))
    S.neu('beurteilen', 'direkt', Z('Ein Glücksrad hat ein Trefferfeld mit 90°. Welche Wahrscheinlichkeit simuliert es?', 0.25, '90 / 360', '90° von 360° = 1/4 = 0,25.', 'Welcher Anteil des Kreises sind 90°?'))
    S.neu('beurteilen', 'darstellung', A('Welches Glücksrad passt zu p = 0,3?', 'Trefferfeld 108°', ['Trefferfeld 30°', 'Trefferfeld 0,3°', 'Trefferfeld 130°'],
                                         '0,3 · 360° = 108°.', 'Welcher Teil von 360° ist gesucht?'))
    S.neu('beurteilen', 'einkleidung', A('Für 1 000 Kunden einer Bäckerei soll simuliert werden, ob sie Brezen kaufen (p = 0,45). Welches Gerät ist geeignet?', 'Zufallszahlen 00 bis 99, dabei 00 bis 44 = Breze',
                                         ['Würfel, 1 bis 3 = Breze', 'Münze, Wappen = Breze', 'Glücksrad mit 45 gleichen Feldern, eines davon Breze'],
                                         '45 von 100 Zahlen ergeben genau 0,45. Würfel und Münze liefern 0,5, das Glücksrad 1/45.', 'Welches Gerät liefert genau 0,45?'))
    S.neu('beurteilen', 'parameter', Z('Ein Glücksrad mit n gleich großen Feldern, davon 9 Trefferfelder, soll p = 0,45 simulieren. Wie groß muss n sein?', 20, '9 / 0.45',
                                       '9/n = 0,45 ⇒ n = 20.', 'Stelle die Gleichung 9/n = 0,45 auf.'))
    S.neu('beurteilen', 'pruefung', A('Ein Glücksrad mit den Ziffern 1 bis 4 wird dreimal gedreht; die Ziffern ergeben eine dreistellige Zahl. Welcher Term gibt die Anzahl der möglichen Zahlen an?', '4³',
                                      ['3⁴', '4 · 3', '4 + 4 + 4'], 'Für jede der 3 Stellen gibt es 4 Möglichkeiten: 4 · 4 · 4 = 4³ = 64.', 'Wie viele Äste hat das Baumdiagramm an jeder Stufe?'))
    S.bonus('beurteilen', A('„Mindestens ein Treffer“ soll mit p = 0,5 simuliert werden. Man dreht Rad A (120°-Trefferfeld) und Rad B (90°-Trefferfeld) je einmal. Ist das geeignet?',
                            'Ja: P(mindestens ein Treffer) = 1 − 2/3 · 3/4 = 1/2.', ['Nein: 120° + 90° = 210° sind mehr als die Hälfte.', 'Nein: Man bräuchte zwei gleiche Räder.', 'Ja, weil 1/3 + 1/4 ungefähr 1/2 ist.'],
                            'Kein Treffer bei A: 2/3, bei B: 3/4. Keiner: 2/3 · 3/4 = 1/2. Also mindestens einer: 1/2 – genau passend.', 'Rechne über das Gegenereignis „kein Treffer“.'))
    S.bonus('beurteilen', B('Spielshow mit 4 Türen: hinter einer ein Auto, hinter drei Ziegen. Nach der Wahl öffnet der Moderator eine andere Tür mit einer Ziege. Man wechselt zufällig zu einer der beiden anderen geschlossenen Türen. Wie groß ist die Gewinnwahrscheinlichkeit?', 3, 8,
                            'Die erste Wahl ist mit 3/4 falsch. Dann steht das Auto hinter einer der beiden anderen geschlossenen Türen, man trifft sie mit 1/2: 3/4 · 1/2 = 3/8. War die erste Wahl richtig (1/4), verliert man durch Wechseln.',
                            'Unterscheide: War die erste Wahl richtig oder falsch?'))
    S.anwenden()


if __name__ == '__main__':
    stufen()  # Zwanzigste Runde (stufen-kl10) – ganz am Ende
