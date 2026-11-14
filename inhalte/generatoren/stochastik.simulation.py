#!/usr/bin/env python3
"""Thema stochastik.simulation – Simulation (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, Z, baue, bruch, cz, ist_endlich, zt  # noqa: E402

META = {'thema_schluessel': 'stochastik.simulation', 'thema_id': 64, 'block_id': 90, 'klasse': {'gym_by': 8, 'rs_by': 9}}

ETAPPEN = [
    {'lernziel': 'zufallsgeraet', 'titel': 'Ein passendes Zufallsgerät wählen',
     'regel': 'Beim ⟦Simulieren⟧ ersetzt man einen echten Vorgang durch ein ⟦Zufallsgerät⟧ mit ⟦derselben Wahrscheinlichkeit⟧: Münze (1/2), Würfel (1/6), Urne oder Glücksrad (beliebige Anteile).',
     'schritte': ['Ein Spieler trifft mit Wahrscheinlichkeit 0,3.', 'Urne mit 10 Kugeln: 3 rote = Treffer, 7 weiße = kein Treffer.', 'Ziehen ⟦mit Zurücklegen⟧ simuliert einen Wurf.'],
     'fehler': 'Eine Münze passt nicht für p = 0,3: Sie liefert immer ⟦p = 0,5⟧. Das Zufallsgerät muss genau die gesuchte Wahrscheinlichkeit haben.',
     '_verbot': ['Wahrscheinlichkeit 0,3']},
    {'lernziel': 'zufallsziffern', 'titel': 'Mit Zufallsziffern simulieren',
     'regel': 'Zufallsziffern 0–9 kommen ⟦gleich oft⟧ vor (je 1/10). Man legt fest, welche Ziffern als ⟦Treffer⟧ zählen, z. B. 0, 1, 2 für p = 0,3, und zählt dann die Treffer.',
     'schritte': ['Regel: 0–2 = Treffer (p = 0,3)', 'Ziffern: 7 1 4 0 9 2 5 8 3 6', 'Treffer: 1, 0, 2 → ⟦3 Treffer⟧ in 10 Versuchen'],
     'fehler': 'Bei der Regel „0–2 = Treffer“ zählt die 2 mit. 0, 1 und 2 sind ⟦drei⟧ Ziffern, also p = 3/10.',
     '_verbot': ['7 1 4 0 9 2 5 8 3 6']},
    {'lernziel': 'regel', 'titel': 'Eine Simulationsregel festlegen',
     'regel': 'Für p = 0,4 nimmt man ⟦4 von 10⟧ Ziffern als Treffer. Für p = 0,35 reichen einzelne Ziffern nicht: Man nimmt ⟦Zahlen von 00 bis 99⟧ und lässt 35 davon als Treffer gelten.',
     'schritte': ['p = 0,35 = 35/100', 'Zweistellige Zufallszahlen 00–99 (100 Stück)', 'Regel: ⟦00–34 = Treffer⟧, 35–99 = kein Treffer'],
     'fehler': 'Die Regel „00–35 = Treffer“ ist für p = 0,35 falsch: Von 00 bis 35 sind es ⟦36⟧ Zahlen.'},
    {'lernziel': 'auswerten', 'titel': 'Simulationen auswerten',
     'regel': 'Aus einer Simulation ⟦schätzt⟧ man eine Wahrscheinlichkeit durch die relative Häufigkeit: ⟦Anzahl der Treffer : Anzahl der Durchgänge⟧. Je mehr Durchgänge, desto zuverlässiger.',
     'schritte': ['200 Durchgänge, 46-mal trat „mindestens zwei Sechsen“ ein', 'Relative Häufigkeit 46 : 200 = 0,23', 'Schätzwert: ⟦P ≈ 0,23⟧'],
     'fehler': 'Die Simulation liefert keinen genauen Wert. 0,23 ist eine ⟦Schätzung⟧ – eine neue Simulation ergibt meist eine etwas andere Zahl.',
     '_verbot': ['200 Durchgänge, 46-mal']},
    {'lernziel': 'monte_carlo', 'titel': 'Monte-Carlo-Methode',
     'regel': 'Bei der ⟦Monte-Carlo-Methode⟧ setzt man zufällig viele Punkte in ein Quadrat. Der ⟦Anteil der Punkte⟧ in einer Figur schätzt den ⟦Anteil der Fläche⟧: A(Figur) ≈ (Punkte in der Figur : alle Punkte) · A(Quadrat).',
     'schritte': ['Quadrat 10 cm × 10 cm = 100 cm², 400 Zufallspunkte', '152 Punkte liegen in der Figur: Anteil 152 : 400 = 0,38', 'A(Figur) ≈ 0,38 · 100 cm² = ⟦38 cm²⟧'],
     'fehler': 'A ≈ 152 cm² ist falsch: Die Anzahl der Punkte ist keine Fläche. Man braucht den ⟦Anteil⟧ der Punkte mal die Quadratfläche.',
     '_verbot': ['152 Punkte']},
    {'lernziel': 'beurteilen', 'titel': 'Ist die Simulation geeignet?',
     'regel': 'Eine Simulation ist ⟦geeignet⟧, wenn das Zufallsgerät für jeden Teilvorgang ⟦genau die richtige Wahrscheinlichkeit⟧ hat und die Durchgänge wie in der Wirklichkeit ablaufen.',
     'schritte': ['Ein Elfmeterschütze trifft mit 75 %.', 'Simulation mit einem Würfel: 1–4 = Treffer → p = 4/6 ≈ 67 %', '⟦Nicht geeignet⟧ – richtig wäre z. B. ein Glücksrad mit 270°-Trefferfeld.'],
     'fehler': 'Eine Urne ohne Zurücklegen verändert sich bei jedem Zug. Soll jeder Versuch dieselbe Wahrscheinlichkeit haben, muss man ⟦zurücklegen⟧.'},
]


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


def g_zufallsziffern(R, st):
    if st == 1:
        k = R.choice([2, 3, 4, 5, 6])
        z, txt = ziffern(R, 20)
        treffer = sum(1 for x in z if int(x) < k)
        return Z(f'Regel: Die Ziffern 0 bis {k - 1} bedeuten Treffer (p = {zt(Fr(k, 10))}). Zähle die Treffer in den Zufallsziffern {txt}.', treffer,
                 f'{treffer}', f'Treffer-Ziffern 0–{k - 1}: ' + ', '.join(x for x in z if int(x) < k) + f'. Das sind {treffer}.', 'Gehe die Ziffern einzeln durch.')
    if st == 2:
        k = R.choice([2, 3, 4, 5, 6, 7])
        z, txt = ziffern(R, 30)
        treffer = sum(1 for x in z if int(x) < k)
        return Z(f'Regel: Ziffern 0 bis {k - 1} = Treffer. Zufallsziffern: {txt}. Gib die relative Häufigkeit der Treffer als Dezimalzahl an.', Fr(treffer, 30) if ist_endlich(Fr(treffer, 30)) else None,
                 f'{treffer} / 30', f'{treffer} Treffer bei 30 Versuchen: {treffer} : 30 = {zt(Fr(treffer, 30))}.', 'Treffer zählen und durch die Anzahl der Ziffern teilen.') \
            if ist_endlich(Fr(treffer, 30)) else Z(f'Regel: Ziffern 0 bis {k - 1} = Treffer. Zufallsziffern: {txt}. Wie viele Nicht-Treffer gibt es?', 30 - treffer,
                                                   f'30 - {treffer}', f'{treffer} Treffer, also 30 − {treffer} = {30 - treffer} Nicht-Treffer.', 'Zähle die Treffer und ziehe sie von 30 ab.')
    # Stufe 3: Gruppen als ein Durchgang
    k, g = R.choice([(3, 3), (5, 2), (2, 4), (4, 3), (1, 4)])
    z, _ = ziffern(R, g * 8)
    gruppen = [z[i:i + g] for i in range(0, len(z), g)]
    txt = ' '.join(''.join(x) for x in gruppen)
    erf = sum(1 for gr in gruppen if any(int(x) < k for x in gr))
    return Z(f'Jede {g}er-Gruppe ist ein Durchgang mit {g} Versuchen; Ziffern 0 bis {k - 1} sind Treffer. In wie vielen Durchgängen gab es mindestens einen Treffer? Gruppen: {txt}',
             erf, f'{erf}', f'Gruppen mit mindestens einer Ziffer 0–{k - 1}: ' + ', '.join(''.join(gr) for gr in gruppen if any(int(x) < k for x in gr)) + f'. Das sind {erf}.',
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
    art = R.choice(['wuerfel', 'nenner'])
    if art == 'wuerfel':
        k = R.randint(1, 5)
        return A(R, f'Mit Zufallsziffern soll ein Würfelwurf mit „Augenzahl ≤ {k}“ als Treffer simuliert werden. Welche Regel passt?',
                 f'Ziffern 1–6 verwenden, 0, 7, 8, 9 überspringen; 1–{k} = Treffer',
                 [f'Ziffern 0–{k} = Treffer, alle anderen kein Treffer', f'Ziffern 1–{k} = Treffer, 0 und 7–9 kein Treffer', 'Jede Ziffer zählt als eine Augenzahl'],
                 f'Für einen Würfel braucht man 6 gleich wahrscheinliche Ergebnisse. Die Ziffern 1–6 liefern das, wenn man die übrigen überspringt. p = {k}/6.',
                 'Ein Würfel hat 6 gleich wahrscheinliche Ergebnisse – wie bekommt man die mit Ziffern?')
    p = Fr(R.choice([1, 2]), 3)
    return A(R, f'Mit Zufallsziffern soll p = {bruch(p)} simuliert werden. Welche Regel passt?', f'Ziffern 1–9 verwenden, 0 überspringen; 1–{int(p * 9)} = Treffer',
             [f'Ziffern 0–{int(p * 10) - 1} = Treffer', f'Ziffern 0–{int(p * 10)} = Treffer', f'Ziffern 1–{int(p * 10)} = Treffer, 0 und Rest kein Treffer'],
             f'{bruch(p)} = {int(p * 9)}/9: Mit 9 gleich wahrscheinlichen Ziffern (1–9) geht es genau, mit 10 Ziffern nicht.',
             f'Welche Anzahl gleich wahrscheinlicher Ziffern ist durch {p.denominator} teilbar?')


def g_auswerten(R, st):
    n = R.choice([50, 80, 100, 125, 200, 250, 400, 500, 1000])
    k = R.randint(1, n - 1)
    was = R.choice(['„mindestens eine Sechs bei vier Würfen“', '„alle drei Kinder sind Mädchen“', '„genau zwei Treffer“', '„der Bus kommt pünktlich“', '„Gewinn beim Losen“'])
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
    return Z(f'In ein Quadrat mit Seitenlänge 1 wird ein Viertelkreis mit Radius 1 gezeichnet. Von {n} Zufallspunkten liegen {k} im Viertelkreis. Welchen Schätzwert für π erhält man?',
             4 * Fr(k, n), f'4 * {k} / {n}', f'Viertelkreis A = π/4, Quadrat A = 1. Also π/4 ≈ {k}/{n} → π ≈ 4 · {zt(Fr(k, n))} = {zt(4 * Fr(k, n))}.',
             'Der Viertelkreis hat die Fläche π/4. Setze den Punkteanteil gleich π/4.')


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
                'Monte-Carlo-Bilder (Quadrat mit Punkten) fehlen; die Anzahlen werden in Worten genannt.'])
